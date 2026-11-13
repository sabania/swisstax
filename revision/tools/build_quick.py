#!/usr/bin/env python3
"""Revisions-Wiki: Quick-Layer (quick/) und generierte Detailseiten (wiki/prueffelder, wiki/prozess, wiki/revio, wiki/themen,
wiki/quellen.md) aus data/ erzeugen. Danach index/lookup.json neu bauen.

  python3 revision/tools/build_quick.py

Prüffeld-Seiten (quick/prueffeld-<code>.md, wiki/prueffelder/<code>.md) tragen im Frontmatter `quelle_sha` = sha256 der
data/prueffelder/<code>.yaml (tools/lint.py aktualitaet() meldet veraltete Seiten). Das Feld testakte_2025 (fiktive Testakte)
wird nur nach eval/testfall-2025/hinweise/<code>.md geschrieben – nie nach quick/, wiki/, lookup oder Plugin.
"""
from __future__ import annotations
import collections, csv, datetime, hashlib, json, os, re, subprocess, sys
from pathlib import Path
import yaml

R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R / "tools"))
HEUTE = datetime.date.today().isoformat()
ZIELE = {"EX": "Bestand", "VO": "Vollständigkeit", "EN": "Eintritt", "RV": "Rechte/Verpflichtungen", "BE": "Bewertung",
         "PA": "Periodenabgrenzung", "DO": "Darstellung/Offenlegung", "RI": "Richtigkeit (vermutl.)"}
ICON = {"verifiziert": "✅", "agent-geprueft": "☑️", "extrahiert": "🟡", "offen": "⬜", "strittig": "⚠️"}


def y(p, d=None):
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else d


REG = {e["id"]: e for e in y(R / "registry" / "sources.yaml", [])}
KAT = y(R / "data" / "katalog.yaml", {})
SCH = {s["id"]: s for s in KAT.get("schritte", [])}
PFK = {p["code"]: p for p in KAT.get("prueffelder", [])}
def pf_laden():
    """data/prueffelder/*.yaml → (Daten je Code, sha256 je Code). Inhalt und Hash aus denselben Bytes (kein Versatz, wenn die
    Datei während des Laufs geändert wird; lint.py meldet die Seite dann als veraltet)."""
    pf, sha = {}, {}
    for p in sorted((R / "data" / "prueffelder").glob("*.yaml")):
        b = p.read_bytes()
        d = yaml.safe_load(b.decode("utf-8"))
        pf[d["code"]], sha[d["code"]] = d, hashlib.sha256(b).hexdigest()
    return pf, sha


PF, PF_SHA = pf_laden()
PH = sorted((y(p) for p in (R / "data" / "prozess").glob("*.yaml")), key=lambda d: d["id"])
WE = [w for p in sorted((R / "data" / "werte").glob("*.yaml")) for w in (y(p, {}) or {}).get("werte", [])]
RG = (y(R / "data" / "regeln.yaml", {}) or {}).get("regeln", [])
TH = [y(p) for p in sorted((R / "data" / "themen").glob("*.yaml"))]
RVZ = y(R / "data" / "revio" / "zuordnung.yaml", {}) or {}
RVK = (y(R / "data" / "revio" / "ketten.yaml", {}) or {}).get("ketten", [])
WZ = list(csv.DictReader((R / "data" / "revio" / "werkzeuge.csv").open(encoding="utf-8-sig"), delimiter=";")) if (R / "data" / "revio" / "werkzeuge.csv").exists() else []


def kurz(cid):
    return (REG.get((cid or "").split("__")[0]) or {}).get("kurz") or (cid or "").split("__")[0]


def link(cid, depth):
    if not cid:
        return "(Praxis/intern)"
    q = cid.split("__")[0]
    m = re.search(r"-s(\d{3})", cid)
    s = f" S. {int(m.group(1))}" if m else ""
    lab = kurz(cid) + (f" {cid.split('__art-')[1].split('-t')[0].upper()}" if "__art-" in cid else s)
    return f"[{lab}]({'../' * depth}chunks/{q}/{cid}.md)"


def zit(x, depth, n=220):
    cid = x.get("quelle")
    if not cid:
        return "(ohne Fundstelle)"
    z = re.sub(r"\s+", " ", x.get("zitat") or "").strip()
    z = z if len(z) <= n else z[: n - 1] + "…"
    return f"«{z}» — {link(cid, depth)}"


def fm(typ, titel, quellen, status="entwurf", **extra):
    """Frontmatter; extra (z.B. quelle_sha) wird nach «generiert» angehängt, leere Werte weggelassen."""
    d = {"typ": typ, "titel": titel, "jur": "ch", "quellen": sorted(set(q for q in quellen if q))[:40], "status": status,
         "generiert": f"tools/build_quick.py, {HEUTE}", **{k: v for k, v in extra.items() if v}}
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=200) + "---\n\n"


def weitere(x):
    """Zusätzliche Fundstellen eines Eintrags (gesetz/risiken/fallstricke/bewertung/unterlagen …): optionale Liste
    `fundstellen: [{quelle, zitat}]`, gleichwertig `weitere_fundstellen`. Nicht für Prüfschritte (dort ist `fundstellen` die Hauptliste)."""
    if not isinstance(x, dict):
        return []
    return [f for k in ("fundstellen", "weitere_fundstellen") for f in (x.get(k) or []) if isinstance(f, dict) and f.get("quelle")]


def praxis(x, *texte):
    """« (Praxis/intern)» für Einträge ohne Fundstelle (AGENTS.md §1.1), ausser der Text nennt schon «Praxis»."""
    if x.get("quelle") or weitere(x) or any("Praxis" in str(t or "") for t in texte):
        return ""
    return " (Praxis/intern)"


def fs_quick(x, depth=1):
    """quick/: alle Fundstellen eines Eintrags als Links (Haupt-Fundstelle zuerst), sonst leer."""
    ids = list(dict.fromkeys(c for c in [x.get("quelle")] + [f["quelle"] for f in weitere(x)] if c))
    return (" — " + " · ".join(link(c, depth) for c in ids)) if ids else ""


def fs_wiki(x, depth=2, n=220, sep=" — "):
    """wiki/: Haupt-Fundstelle mit Zitat, weitere Fundstellen als eingerückte Unterpunkte «auch: …», sonst leer."""
    fs = ([x] if x.get("quelle") else []) + weitere(x)
    if not fs:
        return ""
    return sep + zit(fs[0], depth, n) + "".join(f"\n  - auch: {zit(f, depth, n)}" for f in fs[1:])


def qs(*lists):
    out = []
    for L in lists:
        for x in L or []:
            if isinstance(x, dict):
                if x.get("quelle"):
                    out.append(x["quelle"].split("__")[0])
                for k in ("fundstellen", "weitere_fundstellen"):
                    for f in x.get(k) or []:
                        if isinstance(f, dict) and f.get("quelle"):
                            out.append(f["quelle"].split("__")[0])
    return out


def art_of(s):
    if s.get("kennzeichnung") in ("WP", "?"):   # «?» (unlesbar) bis zur Klärung wie WP (zuordnung schritt_typen[7])
        return "nur_mensch"
    return {"Befragung": "teilweise", "Analytisch": "vorbereiten", "Detail": "vorbereiten", "Sonstige": "auf_anweisung"}.get(s["typ"], "vorbereiten")


def cut(s, n):
    """Kürzen an der Wortgrenze."""
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    if len(s) <= n:
        return s
    t = s[: n - 1]
    w = t.rsplit(" ", 1)[0] if " " in t else t
    return (w if len(w) >= n // 2 else t).rstrip(" ,;:–-") + "…"


OC = next((b for b in RVZ.get("bereiche", []) if b.get("nr") == "OpenClaw"), {})   # harmonisierte OpenClaw-Liste
OC_L, OC_V = set(OC.get("werkzeuge_lesen", [])), set(OC.get("werkzeuge_vorbereiten", []))
NOTIZ_SCHREIBEN = ["rv_put_workpapers_UpdateNote", "rv_post_workpapers_MoveAttachmentsToNote"]


def besonderheiten(s):
    """Besonderheiten je Prüffeld bzw. Schritt (x-320/321/322 über schritt_nr, Ausnahmen über ausser) – wie tools/revision.py."""
    sid = str(s.get("id", ""))
    return [b for b in RVZ.get("prueffeld_besonderheiten", [])
            if (s.get("prueffeld") in (b.get("prueffelder") or []) or (sid and sid in (b.get("schritte") or []))
                or (sid and sid.split("-")[-1] in (b.get("schritt_nr") or []))) and sid not in (b.get("ausser") or [])]


def schritt_typ(s):
    """zuordnung.schritt_typen für den Schritt: WP, «?», 4xx = «auf Anweisung» (nicht der letzte «Sonstige»-Eintrag)."""
    such = ("WP-Schritte" if s.get("kennzeichnung") == "WP" else "Schritte mit unlesbarer" if s.get("kennzeichnung") == "?"
            else "Sonstige (4xx) – auf Anweisung" if s.get("typ") == "Sonstige" else s.get("typ", ""))
    return next((t for t in RVZ.get("schritt_typen", []) if t.get("typ", "").lower().startswith(such.lower())), {})


def write(rel, txt):
    p = R / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(txt, encoding="utf-8")


# ------------------------------------------------------------------ Prüffelder
def pf_seiten():
    rows = []
    for code, p in PFK.items():
        d = PF.get(code, {})
        st = [s for s in SCH.values() if s["prueffeld"] == code]
        arts = collections.Counter(art_of(s) for s in st)
        status = d.get("status", "offen")
        rows.append(f"| [{code}](prueffeld-{code.lower()}.md) | {p['bezeichnung']} | {len(st)} | {p['anzahl'].get('ep', 0)}/{p['anzahl'].get('wp', 0)} | "
                    f"{arts['vorbereiten']} · {arts['teilweise']} · {arts['auf_anweisung']} · {arts['nur_mensch']} | {ICON.get(status, '')} {status} | "
                    f"[Detail](../wiki/prueffelder/{code.lower()}.md) |")
        # quick/prueffeld-<code>.md (kompakt)
        q = [fm("prueffeld", f"Prüffeld {code} {p['bezeichnung']} – Schnellzugriff", qs(d.get("gesetz"), d.get("bewertung"), d.get("schritte")), "entwurf",
                quelle_sha=PF_SHA.get(code)),
             f"# {code} · {p['bezeichnung']}", "",
             f"revio Bereich 4 · {len(st)} Schritte (Befragung {p['anzahl'].get('befragung', 0)}, Analytisch {p['anzahl'].get('analytisch', 0)}, "
             f"Detail {p['anzahl'].get('detail', 0)}, Sonstige {p['anzahl'].get('sonstige', 0)}; EP {p['anzahl'].get('ep', 0)}, WP {p['anzahl'].get('wp', 0)}) · "
             f"Status {ICON.get(status, '')} {status} · Detail mit Zitaten: [wiki/prueffelder/{code.lower()}.md](../wiki/prueffelder/{code.lower()}.md)", ""]
        if d.get("kurzbeschrieb"):
            q += [d["kurzbeschrieb"], ""]
        if d.get("risiken"):
            q += ["## Risiken"] + [f"- {r['text']}" + (f" [{', '.join(r.get('pruefziele') or [])}]" if r.get("pruefziele") else "") +
                                   fs_quick(r) + praxis(r, r.get("text")) for r in d["risiken"]] + [""]
        if d.get("bewertung"):
            q += ["## Bewertung / Bilanzierung"] + [f"- {b['regel']}" + fs_quick(b) + praxis(b, b.get("regel")) for b in d["bewertung"]] + [""]
        if d.get("unterlagen"):
            q += ["## Unterlagen (PBC)"] + [f"- {u['dokument']} – {u.get('zweck', '')}" + praxis(u, u.get("dokument"), u.get("zweck"))
                                            for u in d["unterlagen"]] + [""]
        if d.get("fragen_kunde"):
            q += ["## Fragen an den Kunden (Pendenz / 10.11 – nie selbst befragen)"] + [f"- {f['frage']}" for f in d["fragen_kunde"]] + [""]
        if d.get("fallstricke"):
            q += ["## Fallstricke"] + [f"- {f['text']}" + fs_quick(f) + praxis(f, f.get("text")) for f in d["fallstricke"]] + [""]
        q += ["## Prüfschritte", "Rolle Agent: vorbereiten · teilweise (Befragung) · auf_anweisung (4xx) · nur_mensch (WP-Schritt). Tool: `pruefschritt <id>`.", "",
              "| Id | Typ | Kennz. | Ziele | Agent | Prüfschritt | Vorgehen (kurz) |", "|---|---|---|---|---|---|---|"]
        by = {s["id"]: s for s in d.get("schritte") or []}
        for s in st:
            e = by.get(s["id"], {})
            q.append(f"| {s['id']} | {s['typ']} | {s.get('kennzeichnung') or ''} | {' '.join(s.get('pruefziele') or [])} | {art_of(s)} | "
                     f"{cut(s['text'], 140).replace('|', '/')} | {cut(e.get('vorgehen'), 160).replace('|', '/')} |")
        write(f"quick/prueffeld-{code.lower()}.md", "\n".join(q) + "\n")
        # wiki/prueffelder/<code>.md (Detail mit allen Zitaten)
        if d:
            w = [fm("prueffeld-detail", f"Prüffeld {code} {p['bezeichnung']} – Detail mit Fundstellen", qs(d.get("gesetz"), d.get("bewertung"), d.get("risiken"), d.get("schritte")), "entwurf",
                    quelle_sha=PF_SHA.get(code)),
                 f"# {code} · {p['bezeichnung']} – Detail", "", f"Status {ICON.get(status, '')} {status} · erfasst {d.get('erfasst', {}).get('datum', '')} · "
                 f"Nachprüfung: {d.get('erfasst', {}).get('nachpruefung', {})} · Schnellzugriff: [quick/prueffeld-{code.lower()}.md](../../quick/prueffeld-{code.lower()}.md)", "",
                 d.get("kurzbeschrieb", ""), ""]
            # testakte_2025 bewusst nicht: nur eval/testfall-2025/hinweise/ (testfall_hinweise), nie in wiki/ oder Plugin
            for title, key, f in (("Gesetz", "gesetz", lambda g: f"- **{g.get('thema', '')}**:" + (fs_wiki(g, 2, 220, " ") or praxis(g, g.get("thema")))),
                                  ("Risiken", "risiken", lambda r: f"- {r['text']}" + (f" [{', '.join(r.get('pruefziele') or [])}]" if r.get('pruefziele') else '')
                                   + fs_wiki(r, 2, 160) + praxis(r, r.get("text"))),
                                  ("Bewertung / Bilanzierung", "bewertung", lambda b: f"- **{b['regel']}**" + fs_wiki(b, 2) + praxis(b, b.get("regel"))),
                                  ("Unterlagen (PBC)", "unterlagen", lambda u: f"- {u['dokument']} – {u.get('zweck', '')}" + fs_wiki(u, 2, 140)
                                   + praxis(u, u.get("dokument"), u.get("zweck"))),
                                  ("Fragen an den Kunden", "fragen_kunde", lambda x: f"- {x['frage']} ({x.get('zweck', '')})"),
                                  ("Fallstricke", "fallstricke", lambda x: f"- {x['text']}" + fs_wiki(x, 2, 160) + praxis(x, x.get("text")))):
                if d.get(key):
                    w += [f"## {title}"] + [f(x) for x in d[key]] + [""]
            w.append("## Prüfschritte")
            for s in st:
                e = by.get(s["id"], {})
                w += ["", f"### {s['id']} · {s['typ']}" + (f" · {s['kennzeichnung']}" if s.get("kennzeichnung") else "") + f" · Agent: {art_of(s)}",
                      f"Prüfziele: {', '.join(f'{z} {ZIELE.get(z, z)}' for z in s.get('pruefziele') or []) or '–'}", "",
                      f"> {s['text']}", ""]
                if s.get("beispiel_pflichtenheft"):
                    w.append(f"Beispiel Pflichtenheft: {s['beispiel_pflichtenheft']}")
                if e:
                    w += [f"**Vorgehen:** {e.get('vorgehen', '')}"]
                    if e.get("nachweise"):
                        w.append("**Nachweise:** " + "; ".join(e["nachweise"]))
                    if e.get("rechnen"):
                        w.append(f"**Rechnen:** {e['rechnen']}")
                    if e.get("feststellung_wenn"):
                        w.append(f"**Feststellung, wenn:** {e['feststellung_wenn']}")
                    if e.get("fundstellen"):
                        w += ["**Fundstellen:**"] + [f"- {zit(f, 2)}" for f in e["fundstellen"]]
            write(f"wiki/prueffelder/{code.lower()}.md", "\n".join(w) + "\n")
    hdr = [fm("quick-prueffelder", "Prüffelder revio 4.0 – Übersicht", ["katalog-revio4"], "entwurf"), "# Prüffelder (revio 4.0, Bereich 4)", "",
           "Spalte «Agent»: Anzahl Schritte vorbereiten · teilweise (Befragung) · auf Anweisung (4xx) · nur Mensch (WP).", "",
           "| Code | Prüffeld | Schritte | EP/WP | Agent | Status | Detail |", "|---|---|---|---|---|---|---|"]
    write("quick/prueffelder.md", "\n".join(hdr + rows) + "\n")


HINWEISE = Path("eval") / "testfall-2025" / "hinweise"


def testfall_hinweise():
    """Feld testakte_2025 → eval/testfall-2025/hinweise/<code>.md (nur für Tests; nicht in quick/, wiki/, lookup, Plugin).
    Testakte-Ordner nicht fest verdrahtet: erster Ordner eval/testdaten/*2025/text, in dem die Datei liegt."""
    ziel = R / HINWEISE
    basis = sorted((R / "eval" / "testdaten").glob("*2025/text"))
    alt = {p for p in ziel.glob("*.md")} if ziel.exists() else set()
    kopf = "> **Nur für Tests, nicht ins Plugin.** Bezüge der fiktiven Testakte 2025 (Feld `testakte_2025` in data/prueffelder/). " \
           "Nicht nach quick/ oder wiki/ übernehmen und nicht als Wissen des Agenten verwenden (Überanpassung an die Messung)."
    idx = []
    for code, d in PF.items():
        ta = [t for t in d.get("testakte_2025") or [] if isinstance(t, dict) and t.get("datei")]
        if not ta:
            continue
        bez = PFK.get(code, {}).get("bezeichnung") or d.get("bezeichnung", "")
        w = [fm("testfall-hinweise", f"Testakte 2025 (fiktiv) – Prüffeld {code} (nur für Tests, nicht ins Plugin)", [], "entwurf"),
             f"# {code} · {bez} – Testakte 2025 (fiktiv)", "", kopf, "", f"Quelle: data/prueffelder/{code.lower()}.yaml (Feld testakte_2025)", "",
             "## Testakte 2025 (fiktiv)"]
        for t in ta:
            b = next((x for x in basis if (x / t["datei"]).exists()), None)
            href = os.path.relpath(b / t["datei"], ziel).replace(os.sep, "/") if b else None
            w.append((f"- [{t['datei']}]({href})" if href else f"- {t['datei']} (Datei nicht gefunden)") + f" – {t.get('bezug', '')}")
        p = ziel / f"{code.lower()}.md"
        write(p.relative_to(R), "\n".join(w) + "\n")
        alt.discard(p)
        idx.append(f"| [{code}]({p.name}) | {bez} | {len(ta)} |")
    ix = ziel / "index.md"
    alt.discard(ix)
    write(ix.relative_to(R), "\n".join([fm("testfall-hinweise", "Testakte 2025 (fiktiv) – Hinweise je Prüffeld (nur für Tests, nicht ins Plugin)", []),
                                        "# Testakte 2025 (fiktiv) – Hinweise je Prüffeld", "", kopf, "",
                                        "| Prüffeld | Bezeichnung | Dateien |", "|---|---|---|"] + idx) + "\n")
    for p in alt:   # Prüffeld ohne testakte_2025 mehr → alte Hinweisseite entfernen
        p.unlink()
    return len(idx)


def pbc_fragen():
    u = [fm("pbc", "Unterlagen (PBC) je Prüffeld", qs(*[d.get("unterlagen") for d in PF.values()])), "# Unterlagen (PBC) je Prüffeld", "",
         "In M-Files suchen; Fehlendes als Notiz «Pendenz» (Konto, Datum, Betrag) und Vorschlag für die PBC-Liste 10.10. Die Anforderung beim Kunden macht der Mensch.", ""]
    f = [fm("fragen", "Fragen an den Kunden je Prüffeld", []), "# Fragen an den Kunden je Prüffeld", "",
         "Der Agent befragt nie selbst: schriftliche Antworten (10.11 Kundenbefragung, Protokolle, VE) auswerten, sonst Frage als Pendenz.", ""]
    for code, d in PF.items():
        if d.get("unterlagen"):
            u += [f"## {code} {PFK[code]['bezeichnung']}"] + [f"- {x['dokument']} – {x.get('zweck', '')}" for x in d["unterlagen"]] + [""]
        if d.get("fragen_kunde"):
            f += [f"## {code} {PFK[code]['bezeichnung']}"] + [f"- {x['frage']}" for x in d["fragen_kunde"]] + [""]
    write("quick/pbc-liste.md", "\n".join(u) + "\n")
    write("quick/fragen-kunde.md", "\n".join(f) + "\n")


# ------------------------------------------------------------------ Prozess
def prozess_seiten():
    q = [fm("prozess", "Prozess eingeschränkte Revision – Übersicht", qs(*[p.get("gesetz") for p in PH])), "# Prozess der eingeschränkten Revision – Übersicht", "",
         "Kein starrer Ablauf: je Phase prüfen, was im Mandat nötig ist. Der Agent bereitet vor, der WP entscheidet.", "",
         "| Phase | Ziel | Wann | WP entscheidet | Detail |", "|---|---|---|---|---|"]
    for p in PH:
        q.append(f"| **{p['id']}** {p['titel']} | {cut(p.get('ziel'), 160)} | {cut(p.get('wann'), 90)} | {len(p.get('entscheidungen_wp') or [])} | "
                 f"[Detail](../wiki/prozess/{p['id']}.md) |")
        w = [fm("prozess-detail", f"{p['id']} {p['titel']}", qs(p.get("gesetz"), p.get("schritte"), p.get("entscheidungen_wp"), p.get("dokumentation"))),
             f"# {p['id']} · {p['titel']}", "", f"Status {ICON.get(p.get('status'), '')} {p.get('status')} · Ziel: {p.get('ziel', '')}", "", f"**Wann:** {p.get('wann', '')}", ""]
        if p.get("gesetz"):
            w += ["## Gesetz / Standard"] + [f"- **{g.get('thema', '')}**: {zit(g, 2)}" for g in p["gesetz"]] + [""]
        if p.get("schritte"):
            w += ["## Was nötig ist (Reihenfolge flexibel)", "", "| Wer | Was | revio | M-Files | Fundstelle |", "|---|---|---|---|---|"]
            for s in p["schritte"]:
                f0 = (s.get("fundstellen") or [{}])
                w.append(f"| {s.get('wer', '')} | {s['was'].replace('|', '/')} | {s.get('revio', '').replace('|', '/')} | {s.get('mfiles', '').replace('|', '/')} | "
                         f"{'<br>'.join(link(f.get('quelle'), 2) for f in f0 if f.get('quelle'))} |")
            w.append("")
        for title, key, fn in (("Entscheide des Wirtschaftsprüfers", "entscheidungen_wp", lambda x: f"- {x['text']}" + fs_wiki(x, 2, 160) + praxis(x, x.get("text"))),
                               ("Fragen an den Kunden", "fragen_kunde", lambda x: f"- {x['frage']} ({x.get('zweck', '')})"),
                               ("Unterlagen", "unterlagen", lambda x: f"- {x['dokument']} – {x.get('zweck', '')}" + fs_wiki(x, 2, 140)
                                + praxis(x, x.get("dokument"), x.get("zweck"))),
                               ("Dokumentation", "dokumentation", lambda x: f"- {x['text']}" + fs_wiki(x, 2, 160) + praxis(x, x.get("text"))),
                               ("Fallstricke", "fallstricke", lambda x: f"- {x['text']}" + fs_wiki(x, 2, 160) + praxis(x, x.get("text"))),
                               ("Mustervorlagen", "muster", lambda x: f"- {x['vorlage']} — {link(x.get('chunk'), 2)}")):
            if p.get(key):
                w += [f"## {title}"] + [fn(x) for x in p[key]] + [""]
        if p.get("prueffelder"):
            w.append("Verknüpfte Prüffelder: " + ", ".join(f"[{c}](../prueffelder/{c.lower()}.md)" for c in p["prueffelder"]))
        write(f"wiki/prozess/{p['id']}.md", "\n".join(w) + "\n")
    q += ["", "## Agent-Prozesse 1–6 (Konzept consis)", "",
          "| Prozess | Ort | Agent | Grenze |", "|---|---|---|---|",
          "| 1 Import Jahresrechnung | M-Files → revio 1.1 | definitive Bilanz/ER suchen, importieren, Vorzeichen Passiven, Konten zuordnen, Bilanzgleichheit/Totale abstimmen | unklare Zuordnung → Pendenz; Testphase: Halt zur Kontrolle |",
          "| 2 Markierte Abschlussprüfungen | revio 4 Prüffelder | Prüfschritte nach Typ, Nachweise aus M-Files, Textfeld, Belege, Notizen | kein Visum, kein ✓, keine Abschliessende Beurteilung |",
          "| 3 Unterlagen zum Abschluss | revio 10.9 | Protokoll Vorjahr beschaffen, Zugehörigkeit prüfen, ablegen; fehlende Unterlagen → PBC-Vorschlag 10.10 | Status offen; Anforderung beim Kunden durch Mensch |",
          "| 4 Revisionsrapport | E-Mail an WP | Status aller Schritte, offene/wesentliche Punkte zuerst | nur an freigegebene WP-Adresse |",
          "| 5 GVB-Revisionsbericht | M-Files | Vorjahr kopieren, Zahlen/Stichtage/Ergebnis aktualisieren, gegen 7.1/7.5 prüfen | keine Unterzeichnung/Datierung; Vorjahresoriginale unverändert |",
          "| 6 PDF-Akte | revio → M-Files | nur auf Anweisung erzeugen, prüfen, ablegen | nichts überschreiben |",
          "", "Quelle: Konzept KI-Revisionsagent ([c011-2](../chunks/konzept-ki-revisionsagent-2026/konzept-ki-revisionsagent-2026__c011-2.md)). "
          "Grenzen und Arbeitsregeln: [quick/regeln.md](regeln.md). Werkzeugketten: [quick/revio.md](revio.md)."]
    write("quick/prozess.md", "\n".join(q) + "\n")


def regeln_seite():
    q = [fm("regeln", "Arbeitsregeln des Revisionsagenten", [r["quelle"].split("__")[0] for r in RG], "stabil"), "# Arbeitsregeln des Revisionsagenten", "",
         "Verbindlich für jede Aufgabe. Quelle: Konzept consis bzw. OR (Fundstelle je Regel).", ""]
    cur = None
    for r in RG:
        if r["bereich"] != cur:
            cur = r["bereich"]
            q += ["", f"## {cur}"]
        q.append(f"- **{r['key']}** – {r['regel']} — {zit(r, 1, 150)}")
    write("quick/regeln.md", "\n".join(q) + "\n")


def werte_seite():
    q = [fm("werte", "Schwellenwerte, Sätze, Fristen", [w["quelle"].split("__")[0] for w in WE]), "# Schwellenwerte, Sätze, Fristen", "",
         "Tool: `wert <stichwort>`. Steuerliche Werte (ESTV) sind Praxis der Steuerbehörden, keine handelsrechtliche Bewertungsregel.", ""]
    by = collections.defaultdict(list)
    for w in WE:
        by[w.get("kategorie", "uebrige")].append(w)
    for k in sorted(by):
        q += ["", f"## {k}", "", "| Wert | Betrag | gilt | Bemerkung | Fundstelle |", "|---|---|---|---|---|"]
        for w in by[k]:
            q.append(f"| {w['bezeichnung']} (`{w['key']}`) | **{w['wert']} {w.get('einheit', '')}** | {w.get('gilt', '')} | {cut(w.get('bemerkung'), 120).replace('|', '/')} | "
                     f"{link(w['quelle'], 1)} |")
    write("quick/werte.md", "\n".join(q) + "\n")


# ------------------------------------------------------------------ revio
def revio_seiten():
    q = [fm("revio", "revio 4.0 ↔ revio-MCP – Schnellzugriff (INTERN)", ["konzept-ki-revisionsagent-2026"]), "# revio 4.0 ↔ revio-MCP (INTERN – revio proprietär)", "",
         "Der Agent schreibt nur in Bereich 4 (Prüffelder) und 10 (Unterlagen zum Abschluss), alles andere lesen. Sperren über OpenClaw (allow/deny) und JWT;",
         "schreibende Werkzeuge in OpenClaw freigabepflichtig. Gesperrte Werkzeuge: [wiki/revio/werkzeuge-nur-mensch.md](../wiki/revio/werkzeuge-nur-mensch.md).", ""]
    if RVZ.get("bereiche"):
        q += ["## Bereiche der Revisionsakte", "", "| Bereich | Rolle Agent | lesen | vorbereiten | nur Mensch |", "|---|---|---|---|---|"]
        for b in RVZ["bereiche"]:
            q.append(f"| **{b['nr']}** {b['name']} | {cut(b.get('rolle_agent'), 120).replace('|', '/')} | {', '.join(f'`{w}`' for w in b.get('werkzeuge_lesen', [])[:4])} | "
                     f"{', '.join(f'`{w}`' for w in b.get('werkzeuge_vorbereiten', [])[:4])} | {len(b.get('nur_mensch', []))} |")
    std = RVZ.get("prueffeld_standard") or {}
    if std:
        q += ["", "## Standard für alle Prüffelder (Bereich 4)", f"- lesen: {', '.join(f'`{w}`' for w in std.get('werkzeuge_lesen', []))}",
              f"- vorbereiten: {', '.join(f'`{w}`' for w in std.get('werkzeuge_vorbereiten', []))}",
              f"- nur Mensch: {', '.join(f'`{w}`' for w in std.get('nur_mensch', []))}", f"- Parameter: {std.get('parameter', '')}", f"- {std.get('hinweise', '')}"]
    if RVZ.get("schritt_typen"):
        q += ["", "## Je Schritttyp", "", "| Typ | Art | lesen | vorbereiten | Vorgehen |", "|---|---|---|---|---|"]
        for t in RVZ["schritt_typen"]:
            q.append(f"| {t['typ']} | {t['art']} | {', '.join(f'`{w}`' for w in t.get('werkzeuge_lesen', [])[:4])} | {', '.join(f'`{w}`' for w in t.get('werkzeuge_vorbereiten', [])[:4])} | "
                     f"{cut(t.get('vorgehen'), 200).replace('|', '/')} |")
    if RVZ.get("prueffeld_besonderheiten"):
        q += ["", "## Besonderheiten je Prüffeld"] + [f"- **{b['code']}**: {', '.join(f'`{w}`' for w in b.get('werkzeuge', []))} – {b.get('zweck', '')}" for b in RVZ["prueffeld_besonderheiten"]]
    n = RVZ.get("notizen") or {}
    if n:
        q += ["", "## Notizen", f"- lesen: {', '.join(f'`{w}`' for w in n.get('lesen', []))}", f"- erfassen: {', '.join(f'`{w}`' for w in n.get('erfassen', []))}",
              f"- nie: {', '.join(f'`{w}`' for w in n.get('nie', []))}", f"- {n.get('hinweise', '')}"]
    if RVK:
        q += ["", "## Werkzeugketten (Detail: [wiki/revio/ketten.md](../wiki/revio/ketten.md); ⛔ = Kandidat/nur Mensch, nicht aufrufen)"] + [
            f"- **{k['id']}** {k['aufgabe']} ({k.get('prozess', '')}): " +
            " → ".join(f"{i} `{s['werkzeug']}`" + ("⛔" if s.get("art") in ("kandidat", "nur_mensch") else "") for i, s in enumerate(k.get("schritte", []), 1)) for k in RVK]
    if RVZ.get("offene_fragen"):
        q += ["", "## Offene Fragen"] + [f"- {x}" for x in RVZ["offene_fragen"]]
    write("quick/revio.md", "\n".join(q) + "\n")
    if RVK:
        w = [fm("revio-ketten", "revio-MCP Werkzeugketten (INTERN)", []), "# Werkzeugketten je Aufgabe (INTERN)", ""]
        for k in RVK:
            st = list(enumerate(k.get("schritte", []), 1))   # Nummern wie in den Daten (Querverweise «Schritt N»)
            erl = [(i, s) for i, s in st if s.get("art") in ("lesen", "vorbereiten") and not s.get("optional")]
            opt = [(i, s) for i, s in st if s.get("art") in ("lesen", "vorbereiten") and s.get("optional")]
            kand = [(i, s) for i, s in st if s.get("art") == "kandidat"]
            nie = [(i, s) for i, s in st if s.get("art") == "nur_mensch"]
            bed = lambda s: f" ({s['bedingung']})" if s.get("bedingung") else ""  # noqa: E731
            w += [f"## {k['id']} · {k['aufgabe']}", f"Wann: {k.get('wann', '')} · Prozess: {k.get('prozess', '')}", "",
                  "**Kurzablauf:** " + " → ".join(f"{i} `{s['werkzeug']}`" + (" (schreibt, Freigabe)" if s.get("art") == "vorbereiten" else "") for i, s in erl)]
            if opt:
                w.append("**Nur falls nötig:** " + "; ".join(f"{i} `{s['werkzeug']}`{bed(s)}" for i, s in opt))
            if kand:
                w.append("**Kandidat – nicht aufrufen (deny bis Entscheid consis):** " + "; ".join(f"{i} `{s['werkzeug']}`{bed(s)}" for i, s in kand))
            if nie:
                w.append("**Nie (nur Mensch):** " + ", ".join(f"{i} `{s['werkzeug']}`" for i, s in nie))
            w.append("")
            for i, s in st:
                w.append(f"{i}. `{s['werkzeug']}` [{s.get('art', '')}" + (", optional" if s.get("optional") else "") + "]" +
                         ("⛔" if s.get("art") in ("kandidat", "nur_mensch") else "") + f" – {s.get('zweck', '')}" +
                         (f"  \n   Bedingung: {s['bedingung']}" if s.get("bedingung") else "") +
                         (f"  \n   Parameter: {s['parameter']}" if s.get("parameter") else ""))
            if k.get("menschliche_freigabe"):
                w += ["", f"**Mensch:** {k['menschliche_freigabe']}"]
            if k.get("offene_fragen"):
                w += ["", "Offen: " + "; ".join(k["offene_fragen"])]
            w.append("")
        write("wiki/revio/ketten.md", "\n".join(w) + "\n")
    if WZ:
        by = collections.defaultdict(list)
        for r in WZ:
            by[r.get("art", "")].append(r)
        w = [fm("revio-werkzeuge", "revio-MCP: alle Werkzeuge mit Klassifikation (INTERN)", []), "# revio-MCP – alle Werkzeuge (INTERN)", "",
             " · ".join(f"{k or '?'}: {len(v)}" for k, v in sorted(by.items())), "", "| Werkzeug | Methode | Modul | Art | Bereich | Zweck |", "|---|---|---|---|---|---|"]
        for r in sorted(WZ, key=lambda r: (r.get("modul", ""), r["werkzeug"])):
            w.append(f"| `{r['werkzeug']}` | {r.get('methode', '')} | {r.get('modul', '')} | {r.get('art', '')} | {r.get('revio_bereich', '')} | {cut(r.get('zweck'), 100).replace('|', '/')} |")
        write("wiki/revio/werkzeuge.md", "\n".join(w) + "\n")
        g = [fm("revio-sperrliste", "revio-MCP: für den Agenten gesperrte Werkzeuge (OpenClaw deny, INTERN)", ["konzept-ki-revisionsagent-2026"], "entwurf"),
             "# Gesperrte revio-Werkzeuge (OpenClaw deny)", "",
             "Grundlage: Der Agent setzt nie Visum, schliesst nichts ab, gibt nichts frei; Notizen löscht oder erledigt er nie; Dienstbenutzer ohne Recht für Visum, "
             "Abschlussstatus, Freigabe und Kundenversand ([Konzept c009-3](../../chunks/konzept-ki-revisionsagent-2026/konzept-ki-revisionsagent-2026__c009-3.md)).",
             "**`revio_call` (generischer Aufruf) umgeht jede Sperre je Werkzeug → für den Agenten sperren** (oder nur mit serverseitiger Pfad-Allowlist zulassen).", "",
             "OpenClaw-Konfiguration: allow nur für die OpenClaw-Liste (zuordnung «OpenClaw»: lesen = allow, vorbereiten = allow mit Freigabe), "
             "alles übrige deny – Vorlage [openclaw/revio-tool-policy.json](../../openclaw/revio-tool-policy.json). «unklar» = deny bis Entscheid consis.", ""]
        for k in ("nur_mensch", "gesperrt", "unklar"):
            if by.get(k):
                g += [f"## {k} ({len(by[k])})", "", "| Werkzeug | Methode | Pfad | Begründung |", "|---|---|---|---|"]
                g += [f"| `{r['werkzeug']}` | {r.get('methode', '')} | {r.get('pfad', '')} | {cut(r.get('begruendung'), 120).replace('|', '/')} |" for r in sorted(by[k], key=lambda r: r["werkzeug"])]
                g.append("")
        write("wiki/revio/werkzeuge-nur-mensch.md", "\n".join(g) + "\n")
        # Policy aus der harmonisierten OpenClaw-Liste (zuordnung bereiche[nr=OpenClaw]) + revio_*-Komfortwerkzeuge mit CSV-art lesen
        art = {r["werkzeug"]: r.get("art", "") for r in WZ}
        allow = sorted(set(OC_L) | {n for n, a in art.items() if n.startswith("revio_") and a == "lesen"})
        approval = sorted(OC_V)
        deny = sorted(n for n in art if n not in set(allow) | set(approval))
        write("openclaw/revio-tool-policy.json", json.dumps({
            "hinweis": "Vorschlag Werkzeugrechte revio-MCP für den Revisionsagenten (OpenClaw), INTERN. Quelle: data/revio/zuordnung.yaml, Bereich «OpenClaw» "
                       "(harmonisierte Einstufung). allow = OpenClaw-werkzeuge_lesen + lesende revio_*-Komfortwerkzeuge; approval = OpenClaw-werkzeuge_vorbereiten "
                       "(allow mit Freigabe je Aufruf, Feldregeln im Agenten-Code); deny = alle übrigen, insbesondere revio_call und revio_create_client "
                       "sowie alle nur_mensch/gesperrt/unklar-Werkzeuge und jedes neue Werkzeug. Werkzeugnamen ggf. mit Server-Präfix (z.B. revio__) versehen.",
            "allow": allow, "approval": approval, "deny": deny}, ensure_ascii=False, indent=1))


def revio_pruefschritte():
    """Vorlage je Prüfschritt (Auftrag enco: zuordnung_pruefschritte.csv) + Übersicht je Prüffeld; revio-Ids erst aus echtem Dossier.
    Werkzeuge nach OpenClaw getrennt: werkzeug_lesen nur OpenClaw-lesen, werkzeug_vorbereiten nur OpenClaw-vorbereiten, übrige als Kandidat (deny)."""
    std = RVZ.get("prueffeld_standard") or {}
    rows = []
    for s in SCH.values():
        a = art_of(s)
        t = schritt_typ(s)
        bes = [w for b in besonderheiten(s) for w in b.get("werkzeuge", [])]
        alle_l = list(dict.fromkeys(std.get("werkzeuge_lesen", []) + t.get("werkzeuge_lesen", []) + bes))
        lesen = [w for w in alle_l if w in OC_L]
        vorb = NOTIZ_SCHREIBEN if a == "nur_mensch" else list(dict.fromkeys(std.get("werkzeuge_vorbereiten", []) + t.get("werkzeuge_vorbereiten", []) +
                                                                            [w for w in bes if w in OC_V]))
        kand = [w for w in bes if w not in OC_L and w not in OC_V]
        bem = {"teilweise": "Befragung: schriftliche Antwort (10.11) auswerten, sonst Pendenz; höchstens teilweise bearbeitet",
               "auf_anweisung": "Sonstige (4xx): nur auf Anweisung des WP; physische Tätigkeiten nie",
               "nur_mensch": "WP-Schritt: ohne ausdrückliche Anweisung des WP kein Eintrag im Textfeld (nur Notiz); mit Anweisung «Vorbereitung für WP»",
               "vorbereiten": ""}[a]
        if s.get("kennzeichnung") == "?":
            bem = "Kennzeichnung im Katalog unlesbar – bis Klärung wie WP (in revio nachlesen); " + bem
        if kand:
            bem = (bem + "; " if bem else "") + "Kandidat – nicht aufrufen: " + ", ".join(kand)
        rows.append([s["id"], s["prueffeld"], s["typ"], s.get("kennzeichnung") or "", "4", "", "", ",".join(lesen), ",".join(vorb),
                     "nur_mensch" if a == "nur_mensch" else "vorbereiten", bem])
    out = R / "data" / "revio" / "zuordnung_pruefschritte.csv"
    with out.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["schritt_id", "prueffeld", "typ", "kennz", "revio_bereich", "revio_template_id", "revio_activity_id",
                    "werkzeug_lesen", "werkzeug_vorbereiten", "art", "bemerkung"])
        w.writerows(rows)
    q = [fm("revio-prueffelder", "revio-Zuordnung je Prüffeld (INTERN)", ["katalog-revio4", "konzept-ki-revisionsagent-2026"]),
         "# revio-Zuordnung je Prüffeld (INTERN)", "",
         "Akte-Bereich 4 (Prüffelder); Ids der Prüfungshandlungen (templateId/activityId) erst aus dem echten Dossier (Kette K5). "
         "Je Schritt: [data/revio/zuordnung_pruefschritte.csv](../../data/revio/zuordnung_pruefschritte.csv). Besonderheiten x-320/321/322 gelten je Schritt-Nummer "
         "(Ausnahmen: E1-320 = stille Reserven, P1-321 = Dauerakten). ⛔ = Kandidat, deny bis Entscheid consis.", "",
         "| Prüffeld | lesen | vorbereiten | Menschen-Schritte (WP/«?») | Besonderheiten |", "|---|---|---|---|---|"]
    for code, p in PFK.items():
        wp = [x for x in SCH.values() if x["prueffeld"] == code and x.get("kennzeichnung") in ("WP", "?")]
        bw = [w for b in besonderheiten({"prueffeld": code}) for w in b.get("werkzeuge", [])]
        q.append(f"| **{code}** {p['bezeichnung']} | Standard | Standard | {len(wp)}: {', '.join(x['id'] for x in wp)} | "
                 f"{', '.join(f'`{w}`' + ('' if w in OC_L or w in OC_V else '⛔') for w in dict.fromkeys(bw))} |")
    q += ["", f"Standard lesen: {', '.join(f'`{w}`' for w in std.get('werkzeuge_lesen', []))}",
          "", f"Standard vorbereiten: {', '.join(f'`{w}`' for w in std.get('werkzeuge_vorbereiten', []))}",
          "", "Immer Mensch: Visum je Schritt, ✓ je Prüffeld, Abschliessende Beurteilung, Abschluss/Review, Status Bereich 10."]
    write("wiki/revio/zuordnung-prueffelder.md", "\n".join(q) + "\n")


# ------------------------------------------------------------------ Themen, Quellen, Index
def themen_seiten():
    for t in TH:
        w = [fm("thema", t["titel"], qs(t.get("aussagen"))), f"# {t['titel']}", "", t.get("kurz", ""), ""]
        for a in t.get("aussagen") or []:
            w.append(f"- {a['text']}" + (f" — {zit(a, 2, 200)}" if a.get("quelle") else ""))
        if t.get("agent"):
            w += ["", "## Für den Agenten"] + [f"- {x}" for x in t["agent"]]
        nx = t.get("naechste") or t.get("aufrufe")   # optionale Felder (build_data.py reicht sie durch; tools/revision.py thema)
        if nx:
            w += ["", "**Nächste Aufrufe:** " + " · ".join(f"`{x}`" for x in ([nx] if isinstance(nx, str) else nx))]
        if t.get("prueffelder"):
            w += ["", "Prüffelder: " + ", ".join(f"[{c}](../prueffelder/{c.lower()}.md)" for c in t["prueffelder"])]
        if t.get("phasen"):
            w += ["Phasen: " + ", ".join(f"[{p}](../prozess/{p}.md)" for p in t["phasen"])]
        write(f"wiki/themen/{t['id']}.md", "\n".join(w) + "\n")


def quellen_seite():
    n = collections.Counter(p.parent.name for p in (R / "chunks").glob("*/*.md"))
    q = [fm("quellenkatalog", "Quellenkatalog Revisions-Wiki", list(REG)), "# Quellenkatalog", "",
         "Rang: 1 Gesetz · 2 Standard · 3 Handbuch/Praxis/Fachliteratur EXPERTsuisse · 4 übrige Fachliteratur · 5 intern. "
         "EXPERTsuisse-Werke (HWP, SER, SA-CH, Q&A, Muster) sind an consis lizenziert – nur intern verwenden.", "",
         "| Id | Kurz | Titel | Typ | Rang | Chunks | Stand/Seiten |", "|---|---|---|---|---|---|---|"]
    for i, e in REG.items():
        q.append(f"| `{i}` | {e.get('kurz')} | {cut(e.get('titel'), 90)} | {e.get('typ')} | {e.get('rang')} | {n.get(i, 0)} | {e.get('stand') or e.get('seiten') or ''} |")
    write("wiki/quellen.md", "\n".join(q) + "\n")


def index_seite():
    q = [fm("quick-index", "Revisions-Wiki – Schnellzugriff", []), "# Revisions-Wiki – Schnellzugriff (eingeschränkte Revision, revio 4.0)", "",
         "Grundsatz: Der Agent **bereitet vor**; der Wirtschaftsprüfer entscheidet (Visum, Abschluss, Freigabe, Bericht). → [regeln.md](regeln.md)", "",
         "| Frage | Seite | Tool |", "|---|---|---|",
         "| Was ist bei Prüfschritt X zu tun? | [prueffeld-<code>.md](prueffelder.md) | `pruefschritt C1-302` |",
         "| Prüffeld: Risiken, Bewertung, PBC, Fragen | [prueffelder.md](prueffelder.md) | `prueffeld C1` |",
         "| Welche Unterlagen anfordern? | [pbc-liste.md](pbc-liste.md) | `unterlagen C1` |",
         "| Welche Fragen an den Kunden? | [fragen-kunde.md](fragen-kunde.md) | `fragen C1` |",
         "| Ablauf, Phasen, WP-Entscheide | [prozess.md](prozess.md) | `prozess p6` |",
         "| Was darf der Agent? Notizen? Ablauf je Schritt? | [regeln.md](regeln.md) | `regeln grenze` |",
         "| Welches revio-Werkzeug, welche Kette? | [revio.md](revio.md) | `revio C1-302` · `revio ketten` |",
         "| Schwellenwert, Satz, Frist | [werte.md](werte.md) | `wert <stichwort>` |",
         "| Querschnittsthema | [Themen](#themen) | `thema <stichwort>` |",
         "| Quellen | [../wiki/quellen.md](../wiki/quellen.md) | `suche` → `zeige` |", ""]
    q += ["## Prüffelder", " · ".join(f"[{c}](prueffeld-{c.lower()}.md) {p['bezeichnung']}" for c, p in PFK.items()), ""]
    if PH:
        q += ["## Phasen", " · ".join(f"[{p['id']}](../wiki/prozess/{p['id']}.md) {p['titel']}" for p in PH), ""]
    if TH:
        q += ["## Themen", " · ".join(f"[{t['titel']}](../wiki/themen/{t['id']}.md)" for t in TH), ""]
    write("quick/index.md", "\n".join(q) + "\n")


def main():
    pf_seiten()
    nh = testfall_hinweise()
    pbc_fragen()
    prozess_seiten()
    regeln_seite()
    werte_seite()
    revio_seiten()
    if RVZ:
        revio_pruefschritte()
    themen_seiten()
    quellen_seite()
    index_seite()
    subprocess.run([sys.executable, str(R / "tools" / "build_lookup.py")], check=True)
    n = sum(1 for _ in (R / "quick").glob("*.md")) + sum(1 for _ in (R / "wiki").rglob("*.md"))
    print(f"Seiten: {n} · Testfall-Hinweise (nur eval/, nicht im Plugin): {nh} Prüffelder")


if __name__ == "__main__":
    main()
