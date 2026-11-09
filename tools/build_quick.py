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
import json, os, collections, yaml
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


def write_werte(W):
    for (jur, jahr), d in W.items():
        rows = d.get("werte") or []
        known = {r["key"] for r in rows}
        missing = [k for k in TAX["werte"] if k not in known]
        L = [fm({"typ": "werte", "titel": f"Eckwerte {JUR_SHORT[jur]} {jahr}", "jur": jur, "jahre": [int(jahr)],
                 "generiert": f"tools/build_quick.py aus data/werte/{jur}/{jahr}.yaml ({today()})"}),
             f"# Eckwerte {JUR_LABEL[jur]} – Steuerjahr {jahr}", "",
             f"> Quelle der Wahrheit: [`data/werte/{jur}/{jahr}.yaml`](../data/werte/{jur}/{jahr}.yaml) · "
             f"Legende: ✅ verifiziert (Fachperson) · ☑️ agent-geprüft · 🟡 extrahiert · ⚠️ strittig · ⬜ offen · "
             f"[Vergleich aller Jurisdiktionen {jahr}](vergleich-{jahr}.md) · [Quick-Index](index.md)", ""]
        if d.get("hinweis"):
            L += [f"> **Hinweis:** {d['hinweis']}", ""]
        groups = collections.OrderedDict((g, []) for g in GROUP_ORDER)
        for r in rows:
            groups.setdefault(group_of(r["key"]), []).append(r)
        groups = collections.OrderedDict((g, rs) for g, rs in groups.items() if rs)
        for g, rs in groups.items():
            L += [f"## {g}", "", "| Eckwert | Wert | gilt für | Rechtsgrundlage | Quelle | Status |", "|---|---|---|---|---|---|"]
            for r in rs:
                label = TAX["werte"].get(r["key"], r["key"])
                bem = f"<br><small>{r['bemerkung']}</small>" if r.get("bemerkung") and r.get("status") != "na" else ""
                L.append(f"| {label} <br><small>`{r['key']}`</small> | **{fmt_wert(r)}**{bem} | {r.get('gilt_fuer', '')} | "
                         f"{r.get('rechtsgrundlage', '') or ''} | {qlinks(r)} | {st(r)} |")
            L.append("")
        if missing:
            L += ["## Nicht erfasste Schlüssel", "", ", ".join(f"`{k}`" for k in missing), ""]
        (Q / f"werte-{jur}-{jahr}.md").write_text("\n".join(L), encoding="utf-8")


GROUP_ORDER = ["Berufskosten", "Allgemeine Abzüge", "Vorsorge", "Liegenschaften", "Sozialabzüge", "Vermögen",
               "Steuerfreie Einkünfte", "Tarif / Steuerfuss", "Verfahren", "Bezug / Zinsen", "Weitere"]


def fmt_kurz(r) -> str:
    """Kompakter Wert für Vergleichstabellen (ohne Erläuterungstext)."""
    if r.get("status") == "na":
        return "n/a"
    if r.get("status") == "offen":
        return "offen"
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


def write_zuordnung(Z, W, B):
    beleg_name = {b["id"]: b.get("name", b["id"]) for b in (B or {}).get("belege", [])}
    for (kt, jahr), d in Z.items():
        wk = {r["key"]: r for r in ((W.get((kt, jahr)) or {}).get("werte") or [])}
        wb = {r["key"]: r for r in ((W.get(("bund", jahr)) or {}).get("werte") or [])}
        L = [fm({"typ": "zuordnung", "titel": f"Zuordnung Belege → Formular {JUR_SHORT[kt]} {jahr}", "jur": kt, "jahre": [int(jahr)],
                 "generiert": f"tools/build_quick.py aus data/zuordnung/{kt}/{jahr}.yaml ({today()})"}),
             f"# {JUR_SHORT[kt]} {jahr}: Welcher Beleg / welche Zahl gehört in welche Ziffer?", "",
             f"> Formular: {d.get('formular', '–')} · Quelle der Wahrheit: [`data/zuordnung/{kt}/{jahr}.yaml`](../data/zuordnung/{kt}/{jahr}.yaml) · "
             f"Eckwerte: [Kanton](werte-{kt}-{jahr}.md) · [Bund](werte-bund-{jahr}.md) · [Belege-Relevanz](belege-relevanz.md)", ""]
        if d.get("hinweis"):
            L += [f"> **Hinweis:** {d['hinweis']}", ""]
        sections = collections.OrderedDict()
        for r in d.get("positionen") or []:
            sections.setdefault(r.get("abschnitt") or "Positionen", []).append(r)
        for sec, rs in sections.items():
            L += [f"## {sec}", "", "| Ziffer | Position | Beleg → Feld | Regel / Limite (Kanton · Bund) | Quelle | Status |", "|---|---|---|---|---|---|"]
            for r in rs:
                bel = ", ".join(beleg_name.get(b, b) for b in r.get("belege") or [])
                feld = r.get("feld") or ""
                lim = []
                for k in r.get("werte_keys") or []:
                    a, b = wk.get(k), wb.get(k)
                    lab = TAX["werte"].get(k, k).split(" – ")[-1]
                    lim.append(f"{lab}: {fmt_wert(a) if a else '–'} · Bund {fmt_wert(b) if b else '–'}")
                regel = (r.get("regel") or "") + ("<br>" + "<br>".join(lim) if lim else "")
                if r.get("bund"):
                    regel += f"<br><small>Bund: {r['bund']}</small>"
                pos = f"{r.get('bezeichnung', '')}<br><small>`{r.get('key', '')}`</small>"
                L.append(f"| {r.get('ziffer', '')} | {pos} | {bel}{(' → ' + feld) if feld else ''} | {regel} | {qlinks(r)} | {st(r)} |")
            L.append("")
        # Rückwärts-Index Beleg -> Ziffern
        rev = collections.defaultdict(list)
        for r in d.get("positionen") or []:
            for b in r.get("belege") or []:
                rev[b].append(r.get("ziffer", "?"))
        if rev:
            L += ["## Beleg → Ziffern (Rückwärts-Index)", "", "| Beleg | Ziffern |", "|---|---|"]
            for b in sorted(rev):
                L.append(f"| {beleg_name.get(b, b)} | {', '.join(rev[b])} |")
            L.append("")
        (Q / f"zuordnung-{kt}-{jahr}.md").write_text("\n".join(L), encoding="utf-8")


def write_belege(B, Z):
    if not B:
        return
    L = [fm({"typ": "belege", "titel": "Belege-Relevanz (welche Dokumente sind steuerrelevant?)", "jur": "multi",
             "generiert": f"tools/build_quick.py aus data/belege.yaml ({today()})"}),
         "# Welche Dokumente sind steuerrelevant?", "",
         "> Triage für Mandantenunterlagen. **ja** = in die Steuererklärung übernehmen · **bedingt** = nur unter der genannten "
         "Bedingung · **nein** = nicht deklarieren (ggf. aufbewahren). Die Ziffern je Kanton/Jahr stehen auf den "
         "Zuordnungsseiten. Quelle der Wahrheit: [`data/belege.yaml`](../data/belege.yaml).", ""]
    pages = sorted(Z)
    for rel_, title in (("ja", "Relevant"), ("bedingt", "Bedingt relevant"), ("nein", "Nicht relevant")):
        rs = [b for b in B.get("belege", []) if b.get("relevanz") == rel_]
        if not rs:
            continue
        L += [f"## {title}", ""]
        if rel_ == "nein":
            L += ["| Dokument | Erkennen an | Warum nicht relevant | Quelle |", "|---|---|---|---|"]
            for b in rs:
                L.append(f"| **{b.get('name')}** <small>`{b['id']}`</small> | {sj(b.get('erkennen'))} | "
                         f"{sx(b.get('bedingung') or b.get('begruendung') or '')} | {qlinks(b)} |")
        else:
            L += ["| Dokument | Erkennen an | Wofür / Positionen | Was extrahieren | Hinweise (Kantone) | Quelle |", "|---|---|---|---|---|---|"]
            for b in rs:
                pos = "<br>".join(f"`{p}`" for p in b.get("positionen") or [])
                ziff = []
                for (kt, jahr) in pages:
                    zs = [r.get("ziffer") for r in Z[(kt, jahr)].get("positionen") or [] if b["id"] in (r.get("belege") or [])]
                    if zs:
                        ziff.append(f"[{JUR_SHORT[kt]} {jahr}](zuordnung-{kt}-{jahr}.md): {', '.join(dict.fromkeys(zs))}")
                hin = [sx(h) for h in (b.get("hinweise") or [])]
                for kt, txt in (b.get("kantone") or {}).items():
                    hin.append(f"**{JUR_SHORT.get(kt, kt)}:** {txt}")
                cond = f"<br>**Bedingung:** {b['bedingung']}" if rel_ == "bedingt" and b.get("bedingung") else ""
                L.append(f"| **{b.get('name')}** <small>`{b['id']}`</small>{cond} | {sj(b.get('erkennen'))} | "
                         f"{pos}{('<br>' + '<br>'.join(ziff)) if ziff else ''} | {sj(b.get('extrahieren'), '<br>')} | "
                         f"{'<br>'.join(hin)} | {qlinks(b)} |")
        L.append("")
    (Q / "belege-relevanz.md").write_text("\n".join(L), encoding="utf-8")


def write_index(W, Z):
    years = sorted({y for (_, y) in W} | {y for (_, y) in Z})
    L = [fm({"typ": "quick-index", "titel": "Quick-Access – Einstieg", "jur": "multi", "generiert": f"tools/build_quick.py ({today()})"}),
         "# Quick-Access", "",
         "Schnellzugriff für den Steuerexperten-Agenten. Erst hier nachschlagen, dann über die Links ins Detailwissen (`wiki/`) "
         "und zu den Belegstellen (`chunks/`, `raw/`).", "",
         "1. **Ist ein Dokument relevant?** → [Belege-Relevanz](belege-relevanz.md)",
         "2. **Welche Zahl gehört in welche Ziffer?** → Zuordnung je Kanton/Jahr (Tabelle unten)",
         "3. **Welche Limite/Pauschale gilt?** → Eckwerte je Jurisdiktion/Jahr bzw. Jahresvergleich", "",
         "| Jurisdiktion | " + " | ".join(years) + " |", "|---|" + "---|" * len(years)]
    for j in JURS:
        cells = []
        for y in years:
            parts = []
            if (j, y) in Z:
                parts.append(f"[Zuordnung](zuordnung-{j}-{y}.md)")
            if (j, y) in W:
                parts.append(f"[Eckwerte](werte-{j}-{y}.md)")
            cells.append(" · ".join(parts) or "–")
        L.append(f"| [{JUR_SHORT[j]}](../wiki/{j}/{j}-ueberblick.md) | " + " | ".join(cells) + " |")
    L += ["", "**Vergleich aller Jurisdiktionen:** " + " · ".join(f"[{y}](vergleich-{y}.md)" for y in years if any(k[1] == y for k in W)), "",
          "**Weitere Einstiege:** [Themen](../wiki/themen/index.md) · Quellenkataloge: " +
          " · ".join(f"[{JUR_SHORT[j]}](../wiki/{j}/{j}-quellen.md)" for j in JURS) + " · [Fristen & Verfahren](../wiki/themen/fristen-verfahren.md)", "",
          "Statuslegende: ✅ verifiziert (Fachperson) · ☑️ agent-geprüft · 🟡 extrahiert · ⚠️ strittig · ⬜ offen · – n/a"]
    (Q / "index.md").write_text("\n".join(L) + "\n", encoding="utf-8")


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
    write_index(W, Z)
    print(f"quick/: {len(W)} Werte-Seiten, {len(Z)} Zuordnungs-Seiten, Belege: {len((B or {}).get('belege', []))}")


if __name__ == "__main__":
    main()
