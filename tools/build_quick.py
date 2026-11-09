#!/usr/bin/env python3
"""Generiert den Quick-Access-Layer (quick/*.md) aus den Daten in data/ (Single Source of Truth).

  data/belege.yaml                    -> quick/belege-relevanz.md
  data/werte/<jur>/<jahr>.yaml        -> quick/werte-<jur>-<jahr>.md, quick/vergleich-<jahr>.md
  data/zuordnung/<kanton>/<jahr>.yaml -> quick/zuordnung-<kanton>-<jahr>.md
  alles                               -> quick/index.md

Die Markdown-Seiten NICHT von Hand bearbeiten – data/*.yaml ändern und dieses Skript laufen lassen.

  python3 tools/build_quick.py
"""
from __future__ import annotations
import json, os, re, collections, yaml
from common import ROOT, DATA, JUR_LABEL, JUR_SHORT, today

Q = ROOT / "quick"
TAX = yaml.safe_load((ROOT / "registry" / "taxonomy.yaml").read_text(encoding="utf-8"))
STATUS_ICON = {"verifiziert": "✅", "agent-geprueft": "☑️", "extrahiert": "🟡", "strittig": "⚠️", "offen": "⬜", "na": "–"}
KANTONE = ["ar", "sg", "tg", "zh"]
JURS = ["bund"] + KANTONE


def load_chunks():
    idx = {}
    p = ROOT / "index" / "chunks.jsonl"
    if p.exists():
        for line in p.open(encoding="utf-8"):
            r = json.loads(line)
            idx[r["id"]] = r
    return idx


CIDX = load_chunks()


def clink(cid: str, base=Q) -> str:
    """Link auf einen Chunk mit Kurzlabel (Dokument + Seite/Artikel)."""
    c = CIDX.get(cid)
    if not c:
        return f"`{cid}` (fehlt)"
    lab = c.get("kurz") or c["quelle_id"]
    if c.get("artikel"):
        lab += f" {c['artikel']}"
    elif c.get("seiten"):
        s = c["seiten"]
        lab += f" S. {s[0]}" + (f"–{s[-1]}" if len(s) > 1 else "")
    elif c.get("ziffer"):
        lab += f" Ziff. {c['ziffer']}"
    return f"[{lab}]({os.path.relpath(ROOT / c['datei'], base)})"


def qlinks(row, base=Q) -> str:
    qs = row.get("quellen") or ([{"chunk": row["quelle"]}] if row.get("quelle") else [])
    return "<br>".join(clink(q["chunk"], base) for q in qs if q.get("chunk")) or "–"


def st(row) -> str:
    s = row.get("status", "offen")
    return f"{STATUS_ICON.get(s, '')} {s}"


def fmt_wert(r) -> str:
    if r.get("status") == "na":
        return "n/a" + (f" – {r['bemerkung']}" if r.get("bemerkung") else "")
    w = r.get("wert")
    t = r.get("text")
    if w is None:
        return t or "–"
    if isinstance(w, (int, float)):
        e = r.get("einheit", "")
        if e == "CHF":
            ws = f"CHF {w:,.2f}".replace(",", "'").replace(".00", "") if isinstance(w, float) and not float(w).is_integer() else f"CHF {int(w):,}".replace(",", "'")
        elif e == "%":
            ws = f"{w:g} %"
        elif e in ("Text", "text", None):
            ws = f"{w:g}"
        else:
            ws = f"{w:g} {e}".strip()
        return ws + (f" ({t})" if t else "")
    return str(w) + (f" ({t})" if t else "")


def sx(x) -> str:
    """Listeneintrag als Text (YAML kann «Titel: …» als dict lesen)."""
    if isinstance(x, dict):
        return "; ".join(f"{k}: {v}" for k, v in x.items())
    return str(x)


def sj(items, sep=", ") -> str:
    return sep.join(sx(i) for i in (items or []))


def fm(d: dict) -> str:
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=1000).strip() + "\n---\n"


def load_yaml(p):
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else None


def werte_files():
    out = {}
    for p in sorted((DATA / "werte").glob("*/*.yaml")):
        d = load_yaml(p)
        if d:
            out[(p.parent.name, str(d.get("jahr", p.stem)))] = d
    return out


def zuordnung_files():
    out = {}
    for p in sorted((DATA / "zuordnung").glob("*/*.yaml")):
        d = load_yaml(p)
        if d:
            out[(p.parent.name, str(d.get("jahr", p.stem)))] = d
    return out


def group_of(key: str) -> str:
    return {"berufskosten": "Berufskosten", "weiterbildung": "Allgemeine Abzüge", "versicherung": "Allgemeine Abzüge",
            "saeule3a": "Vorsorge", "zweiverdiener": "Allgemeine Abzüge", "drittbetreuung": "Allgemeine Abzüge",
            "krankheitskosten": "Allgemeine Abzüge", "spenden": "Allgemeine Abzüge", "parteispenden": "Allgemeine Abzüge",
            "liegenschaft": "Liegenschaften", "sozialabzug": "Sozialabzüge", "steuerbetrag": "Sozialabzüge",
            "vermoegen": "Vermögen", "steuerfrei": "Steuerfreie Einkünfte", "tarif": "Tarif / Steuerfuss",
            "verfahren": "Verfahren", "bezug": "Bezug / Zinsen"}.get(key.split(".")[0], "Weitere")


ABK = set("ziff inkl abs art lit bzw ua max min nr s ca dh evtl ggf sog resp vgl gem fr bsp zb al ff lt mind ff sr stv stg dbg wl ks mb rz kap".split())


def kurz(t, n=140, satz=True) -> str:
    """Erster Satz (Abkürzungen wie «Ziff.», «inkl.» berücksichtigt) bzw. auf n Zeichen gekürzt."""
    t = re.sub(r"\s+", " ", sx(t or "")).strip().replace("|", "/")
    if satz:
        for m in re.finditer(r"[.!?](?=\s)", t):
            if m.start() < 25:
                continue
            w = re.findall(r"([A-Za-zÄÖÜäöüß.]+)$", t[:m.start()])
            last = w[0].replace(".", "").lower() if w else ""
            if t[m.start()] == "." and (last in ABK or len(last) <= 1 or re.search(r"\d$", t[:m.start()])):
                continue
            if m.end() <= n:
                return t[:m.end()]
            break
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + " …"


def anchor(*parts, seen=None) -> str:
    a = re.sub(r"[^a-z0-9]+", "-", "-".join(str(p) for p in parts if p).lower()).strip("-")
    if seen is not None:
        base, i = a, 2
        while a in seen:
            a, i = f"{base}-{i}", i + 1
        seen.add(a)
    return a


def first_link(row, base=Q) -> str:
    qs = row.get("quellen") or ([{"chunk": row["quelle"]}] if row.get("quelle") else [])
    return clink(qs[0]["chunk"], base) if qs and qs[0].get("chunk") else "–"


def quellen_detail(row, base) -> list[str]:
    out = []
    qs = row.get("quellen") or ([{"chunk": row["quelle"], "zitat": row.get("zitat")}] if row.get("quelle") else [])
    for q in qs:
        if not q.get("chunk"):
            continue
        z = f" – «{q['zitat']}»" if q.get("zitat") else ""
        out.append(f"  - {clink(q['chunk'], base)} `{q['chunk']}`{z}")
    return out


def write_werte(W):
    for (jur, jahr), d in W.items():
        rows = d.get("werte") or []
        known = {r["key"] for r in rows}
        missing = [k for k in TAX["werte"] if k not in known]
        det_rel = f"../wiki/{jur}/werte-{jur}-{jahr}-detail.md"
        L = [fm({"typ": "werte", "titel": f"Eckwerte {JUR_SHORT[jur]} {jahr}", "jur": jur, "jahre": [int(jahr)],
                 "generiert": f"tools/build_quick.py aus data/werte/{jur}/{jahr}.yaml ({today()})"}),
             f"# Eckwerte {JUR_LABEL[jur]} – Steuerjahr {jahr}", "",
             f"> Kompaktansicht. Wortlaut, Bedingungen und Zitate je Wert: [Detailseite]({det_rel}) · "
             f"Legende: ✅ verifiziert · ☑️ agent-geprüft · 🟡 extrahiert · ⚠️ strittig · ⬜ offen · – n/a · "
             f"[Vergleich {jahr}](vergleich-{jahr}.md) · [Quick-Index](index.md)", ""]
        if d.get("hinweis"):
            L += [f"> **Hinweis:** {kurz(d['hinweis'], 400)}", ""]
        groups = collections.OrderedDict((g, []) for g in GROUP_ORDER)
        for r in rows:
            groups.setdefault(group_of(r["key"]), []).append(r)
        seen = set()
        D = [fm({"typ": "werte-detail", "titel": f"Eckwerte {JUR_SHORT[jur]} {jahr} – Detail", "jur": jur, "jahre": [int(jahr)],
                 "generiert": f"tools/build_quick.py aus data/werte/{jur}/{jahr}.yaml ({today()})"}),
             f"# Eckwerte {JUR_LABEL[jur]} {jahr} – Detail mit Zitaten", "",
             f"> Kompaktansicht: [quick/werte-{jur}-{jahr}.md](../../quick/werte-{jur}-{jahr}.md) · "
             f"Quelle der Wahrheit: `data/werte/{jur}/{jahr}.yaml` · Zitate sind wörtlich aus dem verlinkten Chunk (maschinell geprüft).", ""]
        if d.get("hinweis"):
            D += [f"> **Hinweis:** {d['hinweis']}", ""]
        for g, rs in groups.items():
            if not rs:
                continue
            L += [f"## {g}", "", "| Eckwert | Wert | Hinweis | Quelle | St. |", "|---|---|---|---|---|"]
            D += [f"## {g}", ""]
            for r in rs:
                label = TAX["werte"].get(r["key"], r["key"])
                a = anchor(r["key"], seen=seen)
                b_ = re.sub(r"\s+", " ", r.get("bemerkung") or "").strip().replace("|", "/")
                lim_ = 420 if r.get("status") == "strittig" else 200
                hin = (("⚠️ " if r.get("status") == "strittig" else "") + (b_ if len(b_) <= lim_ else kurz(b_, lim_))) if b_ else ""
                if r.get("gilt_fuer") and r.get("gilt_fuer") not in ("kanton", "bund", "beide"):
                    hin = (hin + " · " if hin else "") + f"gilt für: {r['gilt_fuer']}"
                L.append(f"| {label} <small>`{r['key']}`</small> | **{fmt_kurz(r)}** | {hin} [↗]({det_rel}#{a}) | {first_link(r)} | "
                         f"{STATUS_ICON.get(r.get('status', 'offen'), '')} |")
                D += [f'<a id="{a}"></a>', f"### {label}", "",
                      f"- **Wert:** {fmt_wert(r)}",
                      f"- **Schlüssel:** `{r['key']}` · **gilt für:** {r.get('gilt_fuer', '–')} · **Status:** {st(r)}"]
                if r.get("rechtsgrundlage"):
                    D.append(f"- **Rechtsgrundlage:** {r['rechtsgrundlage']}")
                if r.get("bemerkung"):
                    D.append(f"- **Bemerkung:** {r['bemerkung']}")
                ql = quellen_detail(r, ROOT / "wiki" / jur)
                if ql:
                    D += ["- **Quellen:**"] + ql
                D.append("")
            L.append("")
        if missing:
            L += ["## Nicht erfasste Schlüssel", "", ", ".join(f"`{k}`" for k in missing), ""]
        (Q / f"werte-{jur}-{jahr}.md").write_text("\n".join(L), encoding="utf-8")
        (ROOT / "wiki" / jur).mkdir(parents=True, exist_ok=True)
        (ROOT / "wiki" / jur / f"werte-{jur}-{jahr}-detail.md").write_text("\n".join(D), encoding="utf-8")


GROUP_ORDER = ["Berufskosten", "Allgemeine Abzüge", "Vorsorge", "Liegenschaften", "Sozialabzüge", "Vermögen",
               "Steuerfreie Einkünfte", "Tarif / Steuerfuss", "Verfahren", "Bezug / Zinsen", "Weitere"]


def fmt_kurz(r) -> str:
    """Kompakter Wert für Vergleichstabellen (ohne Erläuterungstext)."""
    if r.get("status") == "na":
        return "n/a"
    if r.get("status") == "offen":
        return "offen"
    if r.get("kurz"):
        return str(r["kurz"])
    w = r.get("wert")
    if w is None:
        t = (r.get("text") or "").strip()
        return (t[:70] + "…") if len(t) > 70 else (t or "–")
    return fmt_wert({**r, "text": None})


def write_vergleich(W):
    years = sorted({y for (_, y) in W})
    for y in years:
        cols = [j for j in JURS if (j, y) in W]
        L = [fm({"typ": "vergleich", "titel": f"Vergleich Eckwerte {y}", "jur": "multi", "jahre": [int(y)],
                 "generiert": f"tools/build_quick.py ({today()})"}),
             f"# Vergleich der Eckwerte – Steuerjahr {y}", "",
             "> Kompaktansicht: Wert · Status · Fundstelle. Bedingungen und Erläuterungen stehen auf den Detailseiten "
             f"(Spaltenkopf anklicken). Kanton = Staats- und Gemeindesteuer, Bund = direkte Bundessteuer. "
             "✅ verifiziert · ☑️ agent-geprüft · 🟡 extrahiert · ⚠️ strittig", "",
             "| Eckwert | " + " | ".join(f"[{JUR_SHORT[j]}](werte-{j}-{y}.md)" for j in cols) + " |",
             "|---|" + "---|" * len(cols)]
        by = {j: {r["key"]: r for r in (W[(j, y)].get("werte") or [])} for j in cols}
        keys = [k for k in TAX["werte"] if any(k in by[j] for j in cols)]
        keys.sort(key=lambda k: GROUP_ORDER.index(group_of(k)) if group_of(k) in GROUP_ORDER else 99)
        cur = None
        for k in keys:
            g = group_of(k)
            if g != cur:
                L.append(f"| **{g}** |" + " |" * len(cols))
                cur = g
            cells = []
            for j in cols:
                r = by[j].get(k)
                if not r:
                    cells.append("–")
                    continue
                q = (r.get("quellen") or [{}])[0].get("chunk") or r.get("quelle")
                ok = r.get("status") not in ("na", "offen")
                cells.append(f"{fmt_kurz(r)}" + (f" {STATUS_ICON.get(r.get('status', ''), '')} {clink(q)}" if ok and q else ""))
            L.append(f"| {TAX['werte'][k]} | " + " | ".join(cells) + " |")
        (Q / f"vergleich-{y}.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def beleg_kurz(name: str) -> str:
    return re.split(r"\s*\(", name or "", maxsplit=1)[0].strip()


def write_zuordnung(Z, W, B):
    beleg_name = {b["id"]: b.get("name", b["id"]) for b in (B or {}).get("belege", [])}
    for (kt, jahr), d in Z.items():
        wk = {r["key"]: r for r in ((W.get((kt, jahr)) or {}).get("werte") or [])}
        wb = {r["key"]: r for r in ((W.get(("bund", jahr)) or {}).get("werte") or [])}
        det_rel = f"../wiki/{kt}/zuordnung-{kt}-{jahr}-detail.md"
        head = (f"> Formular: {kurz(d.get('formular', '–'), 300)} · Eckwerte: [Kanton](werte-{kt}-{jahr}.md) · "
                f"[Bund](werte-bund-{jahr}.md) · [Belege-Relevanz](belege-relevanz.md) · [Beleg × Ziffer](belege-ziffern.md)")
        L = [fm({"typ": "zuordnung", "titel": f"Zuordnung Belege → Formular {JUR_SHORT[kt]} {jahr}", "jur": kt, "jahre": [int(jahr)],
                 "generiert": f"tools/build_quick.py aus data/zuordnung/{kt}/{jahr}.yaml ({today()})"}),
             f"# {JUR_SHORT[kt]} {jahr}: Welcher Beleg / welche Zahl gehört in welche Ziffer?", "",
             head, f"> Kompaktansicht – vollständige Regel, Bund-Hinweis, Zitate: [Detailseite]({det_rel}) (↗ je Zeile). Eine Erklärung für "
             "Kanton und Bund: ohne «Bund:»-Vermerk gilt dieselbe Ziffer/Regel auch für die direkte Bundessteuer (Limiten: Kanton / Bund). "
             "Status: ✅ verifiziert · ☑️ agent-geprüft · 🟡 extrahiert · ⚠️ strittig · ⬜ offen", ""]
        D = [fm({"typ": "zuordnung-detail", "titel": f"Zuordnung {JUR_SHORT[kt]} {jahr} – Detail", "jur": kt, "jahre": [int(jahr)],
                 "generiert": f"tools/build_quick.py aus data/zuordnung/{kt}/{jahr}.yaml ({today()})"}),
             f"# {JUR_SHORT[kt]} {jahr}: Zuordnung Beleg → Ziffer – Detail", "",
             f"> Kompaktansicht: [quick/zuordnung-{kt}-{jahr}.md](../../quick/zuordnung-{kt}-{jahr}.md) · Formular: {d.get('formular', '–')} · "
             f"Quelle der Wahrheit: `data/zuordnung/{kt}/{jahr}.yaml`", ""]
        if d.get("hinweis"):
            L += [f"> **Hinweis:** {kurz(d['hinweis'], 400)}", ""]
            D += [f"> **Hinweis:** {d['hinweis']}", ""]
        sections = collections.OrderedDict()
        for r in d.get("positionen") or []:
            sections.setdefault(r.get("abschnitt") or "Positionen", []).append(r)
        seen = set()
        for sec, rs in sections.items():
            L += [f"## {sec}", "", "| Ziffer | Position | Beleg | Kurzregel · Limite (Kanton / Bund) | St. |", "|---|---|---|---|---|"]
            D += [f"## {sec}", ""]
            for r in rs:
                a = anchor(r.get("ziffer"), r.get("key"), seen=seen)
                bel = ", ".join(dict.fromkeys(beleg_kurz(beleg_name.get(b, b)) for b in r.get("belege") or []))
                lim, liml = [], []
                for k in r.get("werte_keys") or []:
                    x, y = wk.get(k), wb.get(k)
                    lab = TAX["werte"].get(k, k).split(" – ")[-1]
                    lim.append(f"{lab}: {fmt_kurz(x) if x else '–'} / {fmt_kurz(y) if y else '–'}")
                    liml.append(f"  - {TAX['werte'].get(k, k)}: Kanton **{fmt_wert(x) if x else '–'}** · Bund **{fmt_wert(y) if y else '–'}**")
                kr = kurz(r.get("regel"), 120) + ("<br>" + "<br>".join(lim) if lim else "")
                if r.get("bund"):
                    kr += f"<br>Bund: {kurz(r['bund'], 90, satz=False)}"
                L.append(f"| {r.get('ziffer', '')} | {kurz(r.get('bezeichnung', ''), 110, satz=False)} | {bel} | {kr} [↗]({det_rel}#{a}) | "
                         f"{STATUS_ICON.get(r.get('status', 'offen'), '')} |")
                D += [f'<a id="{a}"></a>', f"### Ziff. {r.get('ziffer', '?')} – {r.get('bezeichnung', '')}", "",
                      f"- **Schlüssel:** `{r.get('key', '')}` ({TAX['positionen'].get(r.get('key'), '')}) · **Status:** {st(r)}"]
                if r.get("belege") or r.get("feld"):
                    D.append(f"- **Beleg → Feld:** {', '.join(beleg_name.get(b, b) for b in r.get('belege') or []) or '–'}"
                             + (f" → {r['feld']}" if r.get("feld") else ""))
                if r.get("rein"):
                    D.append("- **Rein:** " + " · ".join(sx(x) for x in r["rein"]))
                if r.get("berechnung"):
                    D.append(f"- **Rechnen:** {r['berechnung']}")
                if r.get("regel"):
                    D.append(f"- **Regel:** {r['regel']}")
                for b in r.get("beachten") or []:
                    D.append(f"- **Beachten:** {sx(b)}")
                if liml:
                    D += ["- **Limiten:**"] + liml
                if r.get("bund"):
                    D.append(f"- **Bund:** {r['bund']}")
                if r.get("bemerkung"):
                    D.append(f"- **Bemerkung:** {r['bemerkung']}")
                ql = quellen_detail(r, ROOT / "wiki" / kt)
                if ql:
                    D += ["- **Quellen:**"] + ql
                D.append("")
            L.append("")
        rev = collections.defaultdict(list)
        for r in d.get("positionen") or []:
            for b in r.get("belege") or []:
                rev[b].append(r.get("ziffer", "?"))
        if rev:
            L += ["## Beleg → Ziffern (Rückwärts-Index)", "", "| Beleg | Ziffern |", "|---|---|"]
            for b in sorted(rev, key=lambda x: beleg_name.get(x, x)):
                L.append(f"| [{beleg_kurz(beleg_name.get(b, b))}](../wiki/belege/beleg-{b}.md) | {', '.join(dict.fromkeys(rev[b]))} |")
            L.append("")
        (Q / f"zuordnung-{kt}-{jahr}.md").write_text("\n".join(L), encoding="utf-8")
        (ROOT / "wiki" / kt).mkdir(parents=True, exist_ok=True)
        (ROOT / "wiki" / kt / f"zuordnung-{kt}-{jahr}-detail.md").write_text("\n".join(D), encoding="utf-8")


def write_wegleitung(Z, W, B):
    """quick/wegleitung-<kt>-<jahr>.md: Kompakt-Wegleitung je Formularposition (Rein · Rechnen · Limite · Beachten)."""
    beleg_name = {b["id"]: b.get("name", b["id"]) for b in (B or {}).get("belege", [])}
    for (kt, jahr), d in Z.items():
        rows = d.get("positionen") or []
        if not any(r.get("berechnung") or r.get("rein") for r in rows):
            continue
        wk = {r["key"]: r for r in ((W.get((kt, jahr)) or {}).get("werte") or [])}
        wb = {r["key"]: r for r in ((W.get(("bund", jahr)) or {}).get("werte") or [])}
        det = f"../wiki/{kt}/zuordnung-{kt}-{jahr}-detail.md"
        L = [fm({"typ": "wegleitung-kompakt", "titel": f"Kompakt-Wegleitung {JUR_SHORT[kt]} {jahr}", "jur": kt, "jahre": [int(jahr)],
                 "generiert": f"tools/build_quick.py aus data/zuordnung/{kt}/{jahr}.yaml ({today()})"}),
             f"# Kompakt-Wegleitung {JUR_LABEL[kt]} – Steuerjahr {jahr}", "",
             f"> Je Formularposition: **Rein** (welche Dokumente → welches Feld) · **Rechnen** (Kurzformel) · **Limite** (Kanton / Bund) · "
             f"**Beachten**. Volle Regel, Bund-Hinweis und wörtliche Zitate: ↗ Detail. Formular: {kurz(d.get('formular', '–'), 260)} · "
             f"[Tabelle](zuordnung-{kt}-{jahr}.md) · [Eckwerte](werte-{kt}-{jahr}.md) · [Gültigkeit {jahr}](gueltigkeit-{jahr}.md)", ""]
        if d.get("hinweis"):
            L += [f"> **Hinweis:** {kurz(d['hinweis'], 400)}", ""]
        sections = collections.OrderedDict()
        for r in rows:
            sections.setdefault(r.get("abschnitt") or "Positionen", []).append(r)
        L += ["**Abschnitte:** " + " · ".join(f"{sec} ({len(rs)})" for sec, rs in sections.items()), ""]
        seen = set()
        for sec, rs in sections.items():
            L += [f"## {sec}", ""]
            for r in rs:
                a = anchor(r.get("ziffer"), r.get("key"), seen=seen)
                L.append(f"### {r.get('ziffer', '')} · {kurz(r.get('bezeichnung', ''), 120, satz=False)} {STATUS_ICON.get(r.get('status', 'offen'), '')}")
                rein = r.get("rein") or ([f"{', '.join(beleg_kurz(beleg_name.get(b, b)) for b in r.get('belege') or [])}"
                                          + (f" → {r['feld']}" if r.get("feld") else "")] if (r.get("belege") or r.get("feld")) else [])
                if rein:
                    L.append("- **Rein:** " + " · ".join(sx(x) for x in rein))
                ber = r.get("berechnung") or kurz(r.get("regel"), 140)
                if ber:
                    L.append(f"- **Rechnen:** {ber}")
                lim = []
                for k in r.get("werte_keys") or []:
                    x, y = wk.get(k), wb.get(k)
                    lab = TAX["werte"].get(k, k).split(" – ")[-1]
                    lim.append(f"{lab}: {fmt_kurz(x) if x else '–'} / {fmt_kurz(y) if y else '–'}")
                if lim:
                    L.append("- **Limite (Kanton / Bund):** " + " · ".join(lim))
                for b in (r.get("beachten") or [])[:3]:
                    L.append(f"- **Beachten:** {sx(b)}")
                L.append(f"- ↗ [Detail]({det}#{a}) · {first_link(r)}")
                L.append("")
        (Q / f"wegleitung-{kt}-{jahr}.md").write_text("\n".join(L), encoding="utf-8")


REL_LABEL = {"ja": "Relevant", "bedingt": "Bedingt relevant", "nein": "Nicht relevant"}


def beleg_ziffern(b, Z):
    out = []
    for (kt, jahr) in sorted(Z):
        zs = [r.get("ziffer") for r in Z[(kt, jahr)].get("positionen") or [] if b["id"] in (r.get("belege") or [])]
        out.append(((kt, jahr), list(dict.fromkeys(z for z in zs if z))))
    return out


def write_belege(B, Z):
    if not B:
        return
    bdir = ROOT / "wiki" / "belege"
    bdir.mkdir(parents=True, exist_ok=True)
    L = [fm({"typ": "belege", "titel": "Belege-Relevanz (welche Dokumente sind steuerrelevant?)", "jur": "multi",
             "generiert": f"tools/build_quick.py aus data/belege-teil*.yaml ({today()})"}),
         "# Welche Dokumente sind steuerrelevant?", "",
         "> Triage für Mandantenunterlagen. **ja** = übernehmen · **bedingt** = nur unter der Bedingung · **nein** = nicht "
         "deklarieren (ggf. aufbewahren). Pro Dokument eine Detailkarte (Erkennen an, Was extrahieren, Hinweise je Kanton, "
         "Ziffern je Kanton/Jahr, Quellen). Ziffern-Matrix: [Beleg × Ziffer](belege-ziffern.md).", ""]
    for rel_ in ("ja", "bedingt", "nein"):
        rs = [b for b in B.get("belege", []) if b.get("relevanz") == rel_]
        if not rs:
            continue
        L += [f"## {REL_LABEL[rel_]}", ""]
        if rel_ == "nein":
            L += ["| Dokument | Warum nicht relevant |", "|---|---|"]
        elif rel_ == "bedingt":
            L += ["| Dokument | Bedingung | Wofür |", "|---|---|---|"]
        else:
            L += ["| Dokument | Wofür | Wichtigster Hinweis |", "|---|---|---|"]
        for b in rs:
            name = f"**[{b.get('name')}](../wiki/belege/beleg-{b['id']}.md)**"
            wof = kurz("; ".join(dict.fromkeys(TAX["positionen"].get(p, p) for p in (b.get("positionen") or []))), 160, satz=False)
            if rel_ == "nein":
                L.append(f"| {name} | {kurz(b.get('bedingung') or b.get('begruendung') or '', 200, satz=False)} |")
            elif rel_ == "bedingt":
                L.append(f"| {name} | {kurz(b.get('bedingung') or '', 230, satz=False)} | {wof} |")
            else:
                L.append(f"| {name} | {wof} | {kurz((b.get('hinweise') or [''])[0], 150)} |")
        L.append("")
        # Detailkarten
        for b in rs:
            C = [fm({"typ": "beleg", "titel": b.get("name"), "jur": "multi", "beleg": b["id"], "relevanz": rel_,
                     "generiert": f"tools/build_quick.py aus data/belege-teil*.yaml ({today()})"}),
                 f"# {b.get('name')}", "",
                 f"> Relevanz: **{rel_}** ({REL_LABEL[rel_]}) · ID `{b['id']}` · Status: {st(b)} · "
                 f"[Belege-Übersicht](../../quick/belege-relevanz.md)", ""]
            if b.get("bedingung") or b.get("begruendung"):
                C += [f"**{'Bedingung' if rel_ == 'bedingt' else 'Begründung'}:** {sx(b.get('bedingung') or b.get('begruendung'))}", ""]
            if b.get("erkennen"):
                C += ["## Erkennen an", ""] + [f"- {sx(x)}" for x in b["erkennen"]] + [""]
            if b.get("positionen"):
                C += ["## Wofür (Positionen)", ""] + [f"- {TAX['positionen'].get(p, p)} `{p}`" for p in b["positionen"]] + [""]
            zz = [(k, zs) for k, zs in beleg_ziffern(b, Z) if zs]
            if zz:
                C += ["## Ziffern je Kanton und Jahr", "", "| Kanton/Jahr | Ziffern |", "|---|---|"]
                C += [f"| [{JUR_SHORT[kt]} {jahr}](../../quick/zuordnung-{kt}-{jahr}.md) | {', '.join(zs)} |" for (kt, jahr), zs in zz] + [""]
            if b.get("extrahieren"):
                C += ["## Was extrahieren", ""] + [f"- {sx(x)}" for x in b["extrahieren"]] + [""]
            if b.get("hinweise"):
                C += ["## Hinweise", ""] + [f"- {sx(x)}" for x in b["hinweise"]] + [""]
            if b.get("kantone"):
                C += ["## Kantonale Besonderheiten", ""] + [f"- **{JUR_SHORT.get(k, k)}:** {sx(v)}" for k, v in b["kantone"].items()] + [""]
            if b.get("bemerkung"):
                C += [f"> Bemerkung: {b['bemerkung']}", ""]
            ql = quellen_detail(b, bdir)
            if ql:
                C += ["## Quellen", ""] + [x[2:] for x in ql] + [""]
            (bdir / f"beleg-{b['id']}.md").write_text("\n".join(C), encoding="utf-8")
    (Q / "belege-relevanz.md").write_text("\n".join(L), encoding="utf-8")
    # Matrix Beleg × Kanton/Jahr
    pages = sorted(Z)
    M = [fm({"typ": "belege", "titel": "Beleg × Ziffer (alle Kantone/Jahre)", "jur": "multi", "generiert": f"tools/build_quick.py ({today()})"}),
         "# Beleg × Ziffer – in welche Ziffer gehört ein Beleg?", "",
         "> Ziffern je Kanton/Jahr (nur Belege mit Relevanz ja/bedingt). Details: Spaltenkopf (Zuordnung) bzw. Beleg (Detailkarte).", "",
         "| Beleg | " + " | ".join(f"[{JUR_SHORT[kt]} {j}](zuordnung-{kt}-{j}.md)" for kt, j in pages) + " |",
         "|---|" + "---|" * len(pages)]
    for b in B.get("belege", []):
        if b.get("relevanz") == "nein":
            continue
        cells = []
        for _, zs in beleg_ziffern(b, Z):
            cells.append(", ".join(zs[:4]) + (" …" if len(zs) > 4 else "") if zs else "–")
        M.append(f"| [{beleg_kurz(b.get('name'))}](../wiki/belege/beleg-{b['id']}.md) | " + " | ".join(cells) + " |")
    (Q / "belege-ziffern.md").write_text("\n".join(M) + "\n", encoding="utf-8")


ROUTER = [
    ("Ist ein Dokument des Mandanten steuerrelevant?", "[Belege-Relevanz](belege-relevanz.md) → Detailkarte des Belegs"),
    ("Was gehört in Ziffer X, woher kommt die Zahl, wie rechne ich?", "**Kompakt-Wegleitung** Kanton/Jahr (Tabelle unten): je Position Rein · Rechnen · Limite · Beachten"),
    ("In welche Ziffer gehört ein Beleg / eine Zahl?", "[Beleg × Ziffer](belege-ziffern.md) bzw. Zuordnung/Kompakt-Wegleitung Kanton/Jahr (Tabelle unten)"),
    ("Welche Limite / Pauschale / welcher Satz gilt?", "Eckwerte Kanton/Jahr (Tabelle unten) oder [Vergleich 2025](vergleich-2025.md) · [2026](vergleich-2026.md)"),
    ("Kanton vs. Bund vergleichen, mehrere Kantone", "[Vergleich 2025](vergleich-2025.md) · [Vergleich 2026](vergleich-2026.md)"),
    ("Lohnausweis: Felder F/G, Ziff. 10.2, 13, 15?", "Zuordnung Kanton/Jahr → Abschnitt «Lohnausweis-Regeln» · [Belegkarte Lohnausweis](../wiki/belege/beleg-lohnausweis.md)"),
    ("Kinderabzug, Sozialabzüge, Vermögensfreibeträge", "Eckwerte → Abschnitt «Sozialabzüge»/«Vermögen» oder [Vergleich 2025](vergleich-2025.md) (AR/SG/TG: Altersstufen `kind_vorschule/_schule/_ausbildung`)"),
    ("Kapitalbezug 2. Säule / 3a, Renten", "Eckwerte → `tarif.kapitalleistung_vorsorge` · [Renten & Kapitalleistungen](../wiki/themen/renten-kapitalleistungen.md) · [Belegkarte](../wiki/belege/beleg-kapitalleistung-vorsorge.md)"),
    ("Alimente, Trennung, Konkubinat", "[Unterhaltsbeiträge](../wiki/themen/unterhaltsbeitraege.md) · [Ehepaare & Familie](../wiki/themen/ehepaare-familie.md)"),
    ("Regel im Detail, Sonderfälle, Praxis", "[Themen](../wiki/themen/index.md) (Stichworte unten) → Chunks"),
    ("Fristen, Fristerstreckung, Verfahren, Bezug", "[Fristen & Verfahren](../wiki/themen/fristen-verfahren.md) · Überblick je Kanton"),
    ("Was ändert sich (2026, 2027, Eigenmietwert 2029 …)?", "[Rechtsänderungen](../wiki/themen/rechtsaenderungen.md)"),
    ("Welche Fassung gilt für Steuerjahr X (Gesetz, Wegleitung, Fristen-Weisung)?", "[Gültigkeit 2025](gueltigkeit-2025.md) · [2026](gueltigkeit-2026.md) – materiell vs. Verfahren vs. Stichtag"),
    ("Alltagsbegriff → Fachbegriff («Kita», «Pendlerabzug»)", "[Glossar](../wiki/glossar.md)"),
    ("Gesetzesartikel wörtlich", "`chunks/<jur>/<jahr>/<gesetz-id>/<id>__art-<nr>[-tN].md` (Bund: Art., ZH/TG: §, AR/SG: Art.); lange Artikel in Teile `-t1`, `-t2` … gesplittet"),
    ("Nichts gefunden?", "Suche: `python3 tools/search.py \"<Begriffe>\" --jur <kt>,bund --jahr <jahr> --expand` bzw. `memory_search`"),
]


def write_index(W, Z):
    years = sorted({y for (_, y) in W} | {y for (_, y) in Z})
    L = [fm({"typ": "quick-index", "titel": "Quick-Access – Einstieg", "jur": "multi", "generiert": f"tools/build_quick.py ({today()})"}),
         "# Quick-Access – Einstieg", "",
         "Schnellzugriff für den Steuerexperten-Agenten: erst hier, dann über die Links ins Detailwissen (`wiki/`) und zu den "
         "Belegstellen (`chunks/`, `raw/`). **Abdeckung:** Bund + Kantone **AR, SG, TG, ZH**, Steuerjahre **"
         + ", ".join(years) + "**. Andere Kantone (z.B. BE, LU, SZ) sind **nicht** im Wiki → so sagen, keine Werte übertragen.", "",
         "## Welche Frage → welche Seite", "", "| Frage | Seite |", "|---|---|"]
    L += [f"| {a} | {b} |" for a, b in ROUTER]
    L += ["", "## Kanton × Jahr", "", "| Jurisdiktion | " + " | ".join(years) + " | Überblick |", "|---|" + "---|" * len(years) + "---|"]
    notes = []
    for j in JURS:
        cells = []
        for y in years:
            parts = []
            if (Q / f"wegleitung-{j}-{y}.md").exists():
                parts.append(f"[Kompakt-Wegleitung](wegleitung-{j}-{y}.md)")
            if (j, y) in Z:
                parts.append(f"[Zuordnung](zuordnung-{j}-{y}.md)")
            if (j, y) in W:
                parts.append(f"[Eckwerte](werte-{j}-{y}.md)")
            cells.append(" · ".join(parts) or "–")
            for d in (Z.get((j, y)), W.get((j, y))):
                if d and d.get("hinweis"):
                    notes.append(f"- **{JUR_SHORT[j]} {y}:** {kurz(d['hinweis'], 260)}")
        L.append(f"| {JUR_SHORT[j]} | " + " | ".join(cells) + f" | [{JUR_SHORT[j]}](../wiki/{j}/{j}-ueberblick.md) |")
    if notes:
        L += ["", "**Datenstand / Lücken:**", ""] + list(dict.fromkeys(notes))
    th = yaml.safe_load((ROOT / "registry" / "themen.yaml").read_text(encoding="utf-8"))["themen"]
    L += ["", "## Themen (Stichworte)", "",
          " · ".join(f"[{t['titel']}](../wiki/themen/{slug}.md)" for slug, t in th.items() if (ROOT / "wiki" / "themen" / f"{slug}.md").exists()), "",
          "## Weitere Einstiege", "",
          "- Quellenkataloge: " + " · ".join(f"[{JUR_SHORT[j]}](../wiki/{j}/{j}-quellen.md)" for j in JURS),
          "- Offene Punkte für die Fachperson (strittig/extrahiert/offen): `reports/offene-punkte.md` · Lint: `reports/lint.md`",
          "- Regeln für Antworten (Zitierpflicht, Kanton ≠ Bund, Jahr fix): `AGENTS.md`", "",
          "Statuslegende: ✅ verifiziert (Fachperson) · ☑️ agent-geprüft · 🟡 extrahiert · ⚠️ strittig · ⬜ offen · – n/a"]
    (Q / "index.md").write_text("\n".join(L) + "\n", encoding="utf-8")


ZEIT_LABEL = {"steuerperiode": "Materielles Recht / Unterlagen der Steuerperiode", "verfahren": "Verfahren (gilt zum Zeitpunkt der Handlung)",
              "stichtag": "Stichtagswerte", "dauernd": "Praxis (gilt bis zum Ersatz)", "info": "Information / Tools"}


def write_gueltigkeit():
    """quick/gueltigkeit-<jahr>.md: welche Fassung jeder Quelle für Steuerjahr X massgeblich ist (Zeitmodell)."""
    from common import load_registry
    reg = load_registry()
    years = sorted({y for e in reg for y in (e.get("jahre") or []) if isinstance(y, int) and y >= 2025})
    byid = {e["id"]: e for e in reg}
    for y in years:
        L = [fm({"typ": "gueltigkeit", "titel": f"Gültige Fassungen für Steuerjahr {y}", "jur": "multi", "jahre": [y],
                 "generiert": f"tools/build_quick.py aus registry/sources.yaml ({today()})"}),
             f"# Steuerjahr {y}: welche Fassung gilt?", "",
             f"> **Zeitmodell.** Steuerjahr {y} = Steuerperiode 1.1.–31.12.{y}; die Erklärung wird {y + 1} eingereicht und veranlagt. "
             f"**Materielles Recht** (Einkünfte, Abzüge, Tarife, Formular/Wegleitung): Fassung für die Periode {y}. "
             f"**Verfahren** (Einreichefrist, Fristerstreckung, Mahnung, Rechtsmittel, Gebühren): Regeln zum Zeitpunkt der Handlung, "
             f"also i.d.R. {y + 1}. **Bezug/Zinsen:** Sätze des Kalenderjahres der Zahlung (provisorisch {y}, Schlussrechnung {y + 1}). "
             f"**Stichtag:** Werte per 31.12.{y} (Kursliste, Vermögen). **Praxis** (Kreisschreiben, Merkblätter, Steuerbuch): "
             "Fassung, die gilt, solange sie nicht ersetzt ist – Anwendungsbeginn beachten (z.B. «ab Steuerperiode 2027»). "
             "Unterjährige Gesetzesänderungen wirken nur, wenn die Übergangsbestimmung es so vorsieht; sonst ab der nächsten Periode.", "",
             f"Werte/Zuordnungen für {y}: Quick-Seiten mit «{y}» im Namen. Andere Jahre nie übertragen (AGENTS.md).", ""]
        for jur in JURS:
            rows = [e for e in reg if e["jurisdiktion"] == jur and y in (e.get("jahre") or [])]
            if not rows:
                continue
            L += [f"## {JUR_LABEL[jur]}", "", "| Zeitbezug | Quelle | Fassung gilt | ersetzt / ersetzt durch |", "|---|---|---|---|"]
            order = ["steuerperiode", "verfahren", "stichtag", "dauernd", "info", None]
            rows.sort(key=lambda e: (order.index(e.get("zeitbezug")) if e.get("zeitbezug") in order else 9, e["typ"], e["id"]))
            for e in rows:
                kette = " · ".join(x for x in (f"ersetzt `{e['ersetzt']}`" if e.get("ersetzt") else "",
                                               f"→ `{e['ersetzt_durch']}`" if e.get("ersetzt_durch") else "") if x)
                sp = ROOT / "wiki" / jur / "quellen" / f"{e['id']}.md"
                ln = f"../wiki/{jur}/quellen/{e['id']}.md" if sp.exists() else e["url"]
                L.append(f"| {e.get('zeitbezug') or '–'} | [{e.get('kurz') or e['id']}]({ln}) `{e['id']}` | "
                         f"{e.get('gilt_ab') or '?'} – {e.get('gilt_bis') or 'offen'} | {kette} |")
            # Fassungen, die für dieses Jahr NICHT gelten, aber verwechselt werden können
            nicht = [e for e in reg if e["jurisdiktion"] == jur and y not in (e.get("jahre") or []) and
                     ((e.get("ersetzt_durch") and y in (byid.get(e["ersetzt_durch"], {}).get("jahre") or [])) or
                      (e.get("ersetzt") and y in (byid.get(e["ersetzt"], {}).get("jahre") or [])))]
            if nicht:
                L += ["", f"**Nicht für Steuerjahr {y}** (andere Fassung): " +
                      ", ".join(f"`{e['id']}` ({', '.join(map(str, e.get('jahre') or []))})" for e in nicht)]
            L.append("")
        (Q / f"gueltigkeit-{y}.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def write_themen_index():
    th = yaml.safe_load((ROOT / "registry" / "themen.yaml").read_text(encoding="utf-8"))["themen"]
    d = ROOT / "wiki" / "themen"
    d.mkdir(parents=True, exist_ok=True)
    L = [fm({"typ": "index", "titel": "Themen (Querschnitt)", "jur": "multi", "generiert": f"tools/build_quick.py ({today()})"}),
         "# Themen – Querschnitt über Bund und Kantone", "",
         "Jede Themenseite: Checkliste, Rechtsgrundlagen, Werte je Jurisdiktion/Jahr, Formularpositionen, Sonderfälle, Quellen. "
         "Zahlen stammen aus `data/` (siehe [Quick-Access](../../quick/index.md)).", "",
         "| Thema | Positionen | Eckwerte |", "|---|---|---|"]
    for slug, t in th.items():
        exists = (d / f"{slug}.md").exists()
        link = f"[{t['titel']}]({slug}.md)" if exists else f"{t['titel']} *(in Arbeit)*"
        L.append(f"| {link} | {', '.join(f'`{p}`' for p in t.get('positionen') or [])} | {len(t.get('werte') or [])} |")
    (d / "index.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def write_glossar():
    g = yaml.safe_load((ROOT / "registry" / "glossar.yaml").read_text(encoding="utf-8"))["glossar"]
    L = [fm({"typ": "glossar", "titel": "Glossar Praxis- und Fachbegriffe", "jur": "multi", "generiert": f"tools/build_quick.py ({today()})"}),
         "# Glossar – Alltags-/Praxisbegriffe ↔ Fach-/Gesetzesbegriffe", "",
         "Hilft beim Suchen (Mandanten sagen «Kita», das Gesetz sagt «Drittbetreuung»). Quelle: `registry/glossar.yaml`; "
         "lokale Suche mit Erweiterung: `python3 tools/search.py \"<Begriffe>\" --expand`.", "",
         "| Begriff | Synonyme / Fachbegriffe |", "|---|---|"]
    for k, syn in g.items():
        L.append(f"| **{k}** | {', '.join(syn)} |")
    (ROOT / "wiki" / "glossar.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def main():
    Q.mkdir(exist_ok=True)
    write_themen_index()
    write_glossar()
    W, Z = werte_files(), zuordnung_files()
    B = {"belege": []}
    for bp in [DATA / "belege.yaml"] + sorted(DATA.glob("belege-teil*.yaml")):
        d = load_yaml(bp)
        if d:
            B["belege"] += d.get("belege") or []
    order = {k: i for i, k in enumerate(TAX["belege"])}
    B["belege"].sort(key=lambda b: order.get(b["id"], 999))
    write_werte(W)
    write_vergleich(W)
    write_zuordnung(Z, W, B)
    write_belege(B, Z)
    write_wegleitung(Z, W, B)
    write_gueltigkeit()
    write_index(W, Z)
    print(f"quick/: {len(W)} Werte-Seiten, {len(Z)} Zuordnungs-Seiten, Belege: {len((B or {}).get('belege', []))}")


if __name__ == "__main__":
    main()
