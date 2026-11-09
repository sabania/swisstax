#!/usr/bin/env python3
"""Generiert die lesbaren Seiten zum Firmenprozess (consis) aus data/firma/*.yaml und data/einreichen/:

  wiki/firma/prozess-np.md       Prozess Steuererklärung NP (Grundsätze, Status, Schritte 1–6, Querschnitt, Agenten)
  wiki/firma/mfiles-ablage.md    M-Files Klasse StE: Kategorien, Zuordnung Dokumentart → Kategorie ↔ Belegtypen, offene Punkte
  quick/ablage-<kt>-<jahr>.md    Quick (Schritt 1+2): Belegtyp → relevant → M-Files-Kategorie → einreichen (Fundstelle) → Ziffern

  python3 tools/build_firma.py      (vorher tools/build_lookup.py; danach tools/build_quick.py für den Index)
"""
from __future__ import annotations
import os, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import steuer  # noqa: E402
from common import today  # noqa: E402

KT = ["zh", "sg", "tg", "ar"]


def fm(d):
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=200).strip() + "\n---\n"


def esc(s):
    return str(s if s is not None else "").replace("|", "/").replace("\n", " ")


def link_chunk(cid, von):
    d = steuer.chunk_dateien().get(cid)
    return f"[{cid}]({os.path.relpath(ROOT / d, von)})" if d else (cid or "–")


def prozess_seite():
    P = steuer.L()["prozess"]
    out = ROOT / "wiki" / "firma" / "prozess-np.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    L = [fm({"typ": "thema", "titel": P["titel"], "jur": "multi", "jahre": [2025, 2026], "quellen": [P["quelle"]],
             "status": "entwurf", "generiert": f"tools/build_firma.py ({today()})"}),
         f"# {P['titel']}", "",
         f"> Quelle: Prozessbeschrieb «Steuerprozess Natürliche Personen», Stand {P['stand']}, Version {P['version']} "
         f"([PDF](../../firma/quellen/steuerprozess-np-2026-10-27.pdf)) · Status: {P['status']}. Werkzeug: `steuer prozess …`. "
         "Steuerrecht dazu: Quick-Layer und Wiki; M-Files-Ablage: [mfiles-ablage.md](mfiles-ablage.md).", "",
         "## Grundsätze", ""]
    L += [f"- **{g['titel']}:** {g['text']}" for g in P["grundsaetze"]]
    L += ["", "**Rollen:** " + " · ".join(f"**{k}** = {v}" for k, v in P["rollen"].items()), "",
          f"**Gesamtablauf:** {P['gesamtablauf']}", "",
          "## Statusmodell (M-Files-Workflow «Steuererklärung nat», ID 122)", "",
          "| Status | Bedingung für Eintritt | wer setzt | Pflichtaktion |", "|---|---|---|---|"]
    L += [f"| {esc(s['name'])} | {esc(s['bedingung'])} | {esc(s['setzt'])} | {esc(s.get('pflicht', '–'))} |" for s in P["status"]]
    L += ["", "Kein Rückweg von «zur Kontrolle» nach «in Arbeit (St)»; zurück nach «Offen» nur über «Reset Workflow» (nur Mensch). "
          "Testphase: Kopie wflow.SteuererklrungNatTest (ID 152).", ""]
    for s in P["schritte"]:
        L += [f"## Schritt {s['nr']} · {s['titel']}", "",
              f"- **Status:** {s['status']} · **Auslöser:** {s['ausloeser']}",
              f"- **Agent:** {s['agent']} · **Output:** {s['output']} · Prozessbeschrieb S. {', '.join(map(str, s['seiten']))}"]
        if s.get("kanaele"):
            L.append("- **Eingangskanäle:** " + " · ".join(f"{k} {v}" for k, v in s["kanaele"].items()))
        L += ["", "| Nr. | Tätigkeit | wer | System | Regel / Detail |", "|---|---|---|---|---|"]
        L += [f"| {esc(t['nr'])} | {esc(t['taetigkeit'])} | {esc(t.get('wer'))} | {esc(t.get('system', '–'))} | {esc(t.get('regel', ''))} |"
              for t in s["teilschritte"]]
        for k in ("pruefkorb", "hinweis", "ablage", "regel"):
            if s.get(k):
                L += ["", f"**{k.capitalize()}:** {s[k]}"]
        if s.get("protokoll"):
            L += ["", "**Aufbau Besprechungsprotokoll:**", ""] + [f"- **{k}:** {v}" for k, v in s["protokoll"].items()]
        L.append("")
    q = P["querschnitt"]
    L += [f"## {q['titel']}", ""] + [f"{i}. {x}" for i, x in enumerate(q["ablauf"], 1)]
    L += ["", "## Agenten", "", "| ID | Agent | Schritte | Auslöser |", "|---|---|---|---|"]
    L += [f"| {a['id']} | {esc(a['name'])} | {esc(a['schritte'])} | {esc(a['ausloeser'])} |" for a in P["agenten"]]
    L += ["", f"> {P.get('agenten_hinweis', '')}", ""]
    out.write_text("\n".join(L), encoding="utf-8")
    return out


def mfiles_seite():
    M = steuer.L()["mfiles"]
    out = ROOT / "wiki" / "firma" / "mfiles-ablage.md"
    B = {b["id"]: b for b in steuer.L()["belege"]}
    L = [fm({"typ": "thema", "titel": "M-Files-Ablage Klasse StE (Kategorien, Zuordnung)", "jur": "multi", "jahre": [2025, 2026],
             "quellen": ["mfiles-kategorien-ste-2026-11-05", "steuerprozess-np-2026-10-27"], "status": "entwurf",
             "generiert": f"tools/build_firma.py ({today()})"}),
         "# M-Files-Ablage – Klasse StE", "",
         f"> Quelle: [M-Files_Kategorien_StE_Zuordnung](../../firma/quellen/mfiles-kategorien-ste-2026-11-05.xlsx), Stand {M['stand']} · "
         f"**{M['status']}**. Werkzeug: `steuer mfiles [begriff]`, `steuer ablage \"<titel>\"`. Kategorie je Kanton/Jahr: "
         "[quick/ablage-<kt>-<jahr>.md](../../quick/ablage-zh-2025.md).", "",
         "## Regel «je nach Kanton»", "", M["regel_je_nach_kanton"], "",
         "## Kategorien", "", "| Nr. | Kategorie | Was hinein gehört | Prozess | eingereicht? |", "|---|---|---|---|---|"]
    L += [f"| {k['nr']} | **{esc(k['kategorie'])}** | {esc(k['inhalt'])} | {esc(k['prozess'])} | {esc(k['eingereicht'])} |" for k in M["kategorien"]]
    L += ["", "## Zuordnung Dokumentart → Kategorie (↔ Belegtypen des Wikis)", "",
          "| Nr. | Dokumentart | Kategorie | eingereicht? | Beschreibung M-Files | Belegtypen (Wiki) | Quelle Zuordnung |", "|---|---|---|---|---|---|---|"]
    for d in M["dokumentarten"]:
        bl = ", ".join(f"[{b}](../belege/beleg-{b}.md)" for b in d.get("belege") or []) or "–"
        L.append(f"| {d['nr']} | {esc(d['dokumentart'])}{' – ' + esc(d['beispiele']) if d.get('beispiele') else ''} | **{esc(d.get('kategorie'))}** | "
                 f"{esc(d.get('eingereicht', '–'))} | {esc(d.get('beschreibung_mfiles', '–'))} | {bl} | {esc(d.get('quelle_zuordnung'))} |")
    ohne = [b for b in B if not any(b in (d.get("belege") or []) for d in M["dokumentarten"])]
    L += ["", "**Belegtypen ohne Zeile in der Zuordnungsliste:** " + ", ".join(
        f"{b} ({steuer.mfiles_kategorie(b)[0]})" for b in ohne), "",
          "## Ergänzungen aus dem Prozessbeschrieb", ""]
    L += [f"- **{e['thema']}:** {e['inhalt']} ({e['quelle']})" for e in M.get("ergaenzungen_prozessbeschrieb") or []]
    L += ["", "## Offene Punkte (mit FE klären)", ""] + [f"- {x}" for x in M.get("offene_punkte") or []] + [""]
    out.write_text("\n".join(L), encoding="utf-8")
    return out


def ablage_seiten():
    outs = []
    jahre = sorted({p["jahr"] for p in steuer.L()["positionen"]})
    for kt in KT:
        for j in jahre:
            pos = [p for p in steuer.L()["positionen"] if p["kt"] == kt and p["jahr"] == j]
            if not pos:
                continue
            out = ROOT / "quick" / f"ablage-{kt}-{j}.md"
            er = ((steuer.L().get("einreichen") or {}).get(kt) or {}).get(j) or {}
            L = [fm({"typ": "belege", "titel": f"Ablage & Erfassung {kt.upper()} {j} (Schritt 1+2)", "jur": kt, "jahre": [int(j)],
                     "quellen": ["mfiles-kategorien-ste-2026-11-05", f"{kt}-wl-{j}"], "status": "entwurf",
                     "generiert": f"tools/build_firma.py ({today()})"}),
                 f"# Ablage & Erfassung – {steuer.NAME[kt]} Steuerjahr {j}", "",
                 "> Je Belegtyp: steuerrelevant? → **M-Files-Kategorie** (Klasse StE) → Einreichepflicht laut Wegleitung (Fundstelle) → "
                 "**Formularziffern (DrTax-Positionen)**. Detail je Ziffer: `steuer position " + f"{kt} {j} <ziffer>` bzw. "
                 + (f"[Kompakt-Wegleitung](wegleitung-{kt}-{j}.md)" if (ROOT / "quick" / f"wegleitung-{kt}-{j}.md").exists() else "Kompakt-Wegleitung (für dieses Jahr nicht vorhanden)") + ". Regeln: [M-Files-Ablage](../wiki/firma/mfiles-ablage.md) · "
                 "[Prozess](../wiki/firma/prozess-np.md). Zuordnungsliste noch nicht von consis bestätigt.", ""]
            if not er:
                L += [f"> ⚠️ Für {kt.upper()} {j} ist keine Einreichepflicht aus der Wegleitung erfasst – Kategorie bei «je nach Kanton» "
                      "mit SB klären.", ""]
            for g in (er.get("allgemein") or [])[:6]:
                L.append(f"- Allgemein: {esc(g.get('regel'))} ({link_chunk(g.get('chunk'), out.parent)} «{esc(steuer.cut(g.get('zitat'), 120))}»)")
            L += ["", "| Belegtyp | relevant | M-Files-Kategorie | einreichen (Fundstelle) | Ziffern / DrTax-Positionen |", "|---|---|---|---|---|"]
            for b in steuer.L()["belege"]:
                kat, _ = steuer.mfiles_kategorie(b["id"], kt, j)
                e = steuer.einreichen(b["id"], kt, j)
                ein = "–"
                if e:
                    ein = e.get("einreichen", "–") + (f": {esc(steuer.cut(e.get('bedingung'), 90))}" if e.get("bedingung") else "")
                    if e.get("chunk"):
                        ein += f" ({link_chunk(e['chunk'], out.parent)})"
                zf = " · ".join(steuer.zf(p) for p in pos if b["id"] in (p.get("belege") or []))[:300] or "–"
                L.append(f"| [{esc(b['name'].split('(')[0].strip())}](../wiki/belege/beleg-{b['id']}.md) | {b.get('relevanz')} | {esc(kat)} | {ein} | {esc(zf)} |")
            L.append("")
            out.write_text("\n".join(L), encoding="utf-8")
            outs.append(out)
    return outs


def main():
    a = prozess_seite()
    b = mfiles_seite()
    c = ablage_seiten()
    print(f"{a.relative_to(ROOT)} · {b.relative_to(ROOT)} · {len(c)} Ablage-Seiten (quick/ablage-*)")


if __name__ == "__main__":
    main()
