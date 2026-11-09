#!/usr/bin/env python3
"""Strukturierte Gesetzestexte: Auflösen, Herunterladen, Konvertieren (1 Einheit pro Artikel/§).

Quellen:
  fedlex   – Bundesrecht als Akoma-Ntoso-XML (SPARQL https://fedlex.data.admin.ch/sparqlendpoint)
  lexwork  – kantonale Gesetzessammlungen (LexWork-JSON-API, z.B. SG/TG/AR) – siehe resolve_lexwork()
  pdf-law  – Gesetz nur als PDF: Artikel-/§-Erkennung per Regex (Fallback, z.B. ZH)

Schritte:
  python3 tools/laws.py resolve --jahre 2025 2026   # Fedlex: Fassungen je Steuerjahr ermitteln -> registry/sources.yaml
  python3 tools/fetch.py                            # XML/JSON/PDF laden (download_url)
  python3 tools/laws.py convert                     # -> sources/<jur>/<jahr>/<id>.md + <id>.articles.json
  python3 tools/chunk.py                            # -> 1 Chunk pro Artikel (IDs <id>__art-33, <id>__par-31)

Ein Registry-Eintrag pro Konsolidierung (Fassung). Gilt dieselbe Fassung für mehrere Steuerjahre, steht sie einmal
mit jahre: [2025, 2026] im Ordner des ersten Jahres.
"""
from __future__ import annotations
import argparse, json, re, sys, urllib.parse, urllib.request
from common import load_registry, save_registry, raw_path, source_path, frontmatter, ROOT, JUR_LABEL, today
import akn

ENDPOINT = "https://fedlex.data.admin.ch/sparqlendpoint"
# SR -> (Kurz, ID-Stamm, Titel)
FEDLEX_LAWS = {
    "642.11": ("DBG", "bund-dbg", "Bundesgesetz über die direkte Bundessteuer (DBG, SR 642.11)"),
    "642.14": ("StHG", "bund-sthg", "Steuerharmonisierungsgesetz (StHG, SR 642.14)"),
    "642.21": ("VStG", "bund-vstg", "Verrechnungssteuergesetz (VStG, SR 642.21)"),
    "642.211": ("VStV", "bund-vstv", "Verrechnungssteuerverordnung (VStV, SR 642.211)"),
    "642.118.1": ("BKV", "bund-bkv", "Berufskostenverordnung EFD (SR 642.118.1)"),
    "642.116": ("LKV", "bund-lkv", "Liegenschaftskostenverordnung (SR 642.116)"),
    "642.118.2": ("QStV", "bund-qstv", "Quellensteuerverordnung (QStV, SR 642.118.2)"),
    "642.119.2": ("VKP", "bund-vkp", "Verordnung über den Ausgleich der kalten Progression (VKP, SR 642.119.2)"),
    "831.461.3": ("BVV 3", "bund-bvv3", "Verordnung über die steuerliche Abzugsberechtigung für Beiträge an anerkannte Vorsorgeformen (BVV 3, SR 831.461.3)"),
    "831.411": ("WEFV", "bund-wefv", "Verordnung über die Wohneigentumsförderung mit Mitteln der beruflichen Vorsorge (WEFV, SR 831.411)"),
}
TYP = {"642.11": "gesetz", "642.14": "gesetz", "642.21": "gesetz"}

Q_APPLICABLE = """PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos:  <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd:   <http://www.w3.org/2001/XMLSchema#>
SELECT DISTINCT ?day ?sr ?act ?consolidation ?dateApplicability ?dateEndApplicability ?xmlFile ?htmlFile ?pdfFile
WHERE {
  VALUES ?day { %(days)s }
  VALUES ?sr  { %(srs)s }
  ?act a jolux:ConsolidationAbstract ; jolux:classifiedByTaxonomyEntry/skos:notation ?srNotation .
  FILTER(str(?srNotation) = ?sr)
  ?consolidation a jolux:Consolidation ; jolux:isMemberOf ?act ; jolux:dateApplicability ?dateApplicability .
  OPTIONAL { ?consolidation jolux:dateEndApplicability ?dateEndApplicability }
  FILTER(?dateApplicability <= ?day && (!BOUND(?dateEndApplicability) || ?dateEndApplicability >= ?day))
  ?consolidation jolux:isRealizedBy ?expr .
  ?expr jolux:language <http://publications.europa.eu/resource/authority/language/DEU> ; jolux:isEmbodiedBy ?mx .
  ?mx jolux:userFormat <https://fedlex.data.admin.ch/vocabulary/user-format/xml> ; jolux:isExemplifiedBy ?xmlFile .
  OPTIONAL { ?expr jolux:isEmbodiedBy ?mh . ?mh jolux:userFormat <https://fedlex.data.admin.ch/vocabulary/user-format/html> ; jolux:isExemplifiedBy ?htmlFile . }
  OPTIONAL { ?expr jolux:isEmbodiedBy ?mp . ?mp jolux:userFormat <https://fedlex.data.admin.ch/vocabulary/user-format/pdf-a> ; jolux:isExemplifiedBy ?pdfFile . }
}
ORDER BY ?sr ?day"""


def sparql(q: str) -> list[dict]:
    data = urllib.parse.urlencode({"query": q}).encode()
    req = urllib.request.Request(ENDPOINT, data=data, headers={"Accept": "application/sparql-results+json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return [{k: v["value"] for k, v in b.items()} for b in json.load(r)["results"]["bindings"]]


def resolve_fedlex(jahre: list[int]) -> None:
    """Ermittelt je Gesetz und Steuerjahr die am 1.1. anwendbare Fassung und pflegt die Registry."""
    rows = sparql(Q_APPLICABLE % {"days": " ".join(f'"{y}-01-01"^^xsd:date' for y in jahre),
                                  "srs": " ".join(f'"{s}"' for s in FEDLEX_LAWS)})
    # gleiche Konsolidierung -> ein Eintrag mit mehreren Jahren
    cons = {}
    for r in rows:
        y = int(r["day"][:4])
        c = cons.setdefault(r["consolidation"], dict(r, jahre=[]))
        if y not in c["jahre"]:
            c["jahre"].append(y)
    reg = load_registry()
    by_id = {e["id"]: e for e in reg}
    multi = {sr: len({c["consolidation"] for c in cons.values() if c["sr"] == sr}) > 1 for sr in FEDLEX_LAWS}
    for c in sorted(cons.values(), key=lambda c: (c["sr"], c["dateApplicability"])):
        kurz, stem, titel = FEDLEX_LAWS[c["sr"]]
        jahre = sorted(c["jahre"])
        cid = f"{stem}-{jahre[0]}" if multi[c["sr"]] else stem
        date = c["consolidation"].rsplit("/", 1)[1]
        eli = c["act"].split("/eli/")[1]
        e = by_id.get(cid) or {"id": cid}
        e.update({
            "jurisdiktion": "bund", "ordner_jahr": str(jahre[0]), "jahre": jahre,
            "typ": TYP.get(c["sr"], "verordnung"), "kurz": kurz,
            "titel": f"{titel} – Fassung gültig ab {c['dateApplicability'][8:10]}.{c['dateApplicability'][5:7]}.{c['dateApplicability'][:4]}",
            "url": f"https://www.fedlex.admin.ch/eli/{eli}/{date}/de", "download_url": c["xmlFile"], "format": "xml",
            "verarbeitung": "chunk", "strukturiert": "fedlex", "stand": c["dateApplicability"],
            "fedlex": {"sr": c["sr"], "eli": c["act"], "konsolidierung": c["consolidation"], "gilt_ab": c["dateApplicability"],
                       "gilt_bis": c.get("dateEndApplicability"), "html": c.get("htmlFile"), "pdf_a": c.get("pdfFile")},
        })
        if cid not in by_id:
            reg.append(e)
            by_id[cid] = e
        print(f"{cid:22} {kurz:6} {date} Jahre {jahre}")
    save_registry(reg)


ROMAN = None


def unit_key(eid: str, kind: str, label: str) -> str:
    if kind == "annex":
        return "anhang-" + eid.split("_")[-1]
    if kind in ("proviso", "transitional"):
        return ("schlussbest-" if kind == "proviso" else "uebergang-") + re.sub(r"[^a-z0-9]+", "-", eid.lower()).strip("-")
    k = eid.replace("art_", "art-")
    k = re.sub(r"_(?=[a-z])", "", k)            # art_33_a -> art-33a ; art_205_b_bis -> art-205bbis
    k = k.replace("_", "-")                     # art_43_48 -> art-43-48
    return k


def convert_fedlex(e: dict) -> int:
    xml = raw_path(e, "xml")
    units = akn.parse_units(str(xml), e["kurz"], e.get("download_url"))
    arts, md = [], []
    seen = set()
    for u in units:
        key = unit_key(u["eid"], u["kind"], u["label"])
        while key in seen:
            key += "x"
        seen.add(key)
        clean_body = akn.FN_RE.sub("", u["body"]).strip()
        heading = f"{u['label']} {e['kurz']}" + (f" – {u['title']}" if u["title"] else "")
        text = f"### {heading}\n\n" + clean_body + ("\n\n*(aufgehoben)*" if u["repealed"] and "ufgehoben" not in clean_body else "")
        arts.append({"key": key, "label": u["label"], "titel": heading, "pfad": u["path"] + [f"{u['label']} {u['title']}".strip()],
                     "text": text, "aufgehoben": u["repealed"], "eid": u["eid"]})
        md += [f"## {heading}", "", f"*{' > '.join([e['kurz']] + u['path'])}* · [Fedlex]({e['url']}#{u['eid']})", "", u["body"], ""]
        if u["footnotes"]:
            md += [""] + u["footnotes"] + [""]
    sp = source_path(e)
    sp.parent.mkdir(parents=True, exist_ok=True)
    fm = {"id": e["id"], "titel": e["titel"], "kurz": e["kurz"], "jurisdiktion": "bund", "jahre": e["jahre"], "typ": e["typ"],
          "stand": e.get("stand"), "quelle_url": e["url"], "raw": str(raw_path(e, 'xml').relative_to(ROOT)),
          "sha256": e.get("sha256"), "abgerufen": e.get("abgerufen"), "einheiten": len(arts),
          "konvertierung": "Akoma-Ntoso-XML (Fedlex) -> Markdown je Artikel (tools/akn.py); Fussnoten = Fedlex-Nummerierung"}
    head = f"# {e['titel']}\n\n> {JUR_LABEL['bund']} · Gesetzestext (konsolidierte Fassung) · Quelle: <{e['url']}>\n\n"
    sp.write_text(frontmatter(fm) + head + "\n".join(md), encoding="utf-8")
    sp.with_suffix(".articles.json").write_text(json.dumps(arts, ensure_ascii=False, indent=0), encoding="utf-8")
    return len(arts)


# ---------------------------------------------------------------- PDF-Gesetze (Fallback: Artikel/§ per Regex)
ART_RE = re.compile(r"^\s{0,6}(Art\.|§)\s*(\d+[a-z]?(?:\s?(?:bis|ter|quater|quinquies|sexies))?)\b\.?\s*(.*)$")


def convert_pdf_law(e: dict) -> int:
    """Teilt einen als PDF konvertierten Gesetzestext (sources/…md, pdftotext -layout) an Artikel-/§-Anfängen."""
    sp = source_path(e)
    text = sp.read_text(encoding="utf-8")
    body = text.split("\n---\n", 1)[1] if text.startswith("---\n") else text
    lines = body.splitlines()
    page = None
    cur, arts, path = None, [], []
    head_re = re.compile(r"^\s{0,4}(\d+(\.\d+)*\.?|[IVX]+\.|[A-Z]\.)\s+[A-ZÄÖÜ][^.]{2,80}$")
    for l in lines:
        m = re.match(r"<!-- Seite (\d+)", l)
        if m:
            page = int(m.group(1))
            continue
        am = ART_RE.match(l)
        if am and (am.group(3) == "" or len(am.group(3)) < 140):
            if cur:
                arts.append(cur)
            sym = "Art." if am.group(1).startswith("Art") else "§"
            nr = am.group(2).replace(" ", "")
            cur = {"label": f"{sym} {nr}", "titel_raw": am.group(3).strip(), "lines": [l], "seiten": [page] if page else [], "pfad": list(path)}
            continue
        if cur is None:
            if head_re.match(l):
                path = [l.strip()]
            continue
        cur["lines"].append(l)
        if page and page not in cur["seiten"]:
            cur["seiten"].append(page)
    if cur:
        arts.append(cur)
    out, seen = [], set()
    for a in arts:
        sym, nr = a["label"].split(" ", 1)
        key = ("art-" if sym == "Art." else "par-") + re.sub(r"[^0-9a-z]+", "", nr.lower())
        while key in seen:
            key += "x"
        seen.add(key)
        t = "\n".join(a["lines"]).strip()
        heading = f"{a['label']} {e['kurz']}"
        out.append({"key": key, "label": a["label"], "titel": heading, "pfad": [heading], "seiten": a["seiten"],
                    "text": f"### {heading}\n\n{t}"})
    sp.with_suffix(".articles.json").write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding="utf-8")
    return len(out)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("resolve")
    r.add_argument("--jahre", nargs="+", type=int, required=True)
    c = sub.add_parser("convert")
    c.add_argument("--id", action="append")
    a = ap.parse_args()
    if a.cmd == "resolve":
        resolve_fedlex(a.jahre)
        return
    n = 0
    for e in load_registry():
        if a.id and e["id"] not in a.id:
            continue
        s = e.get("strukturiert")
        if s == "fedlex" and raw_path(e, "xml").exists():
            k = convert_fedlex(e)
        elif s == "lexwork":
            import lexwork
            k = lexwork.convert(e)
        elif s == "zhlex" and raw_path(e, "pdf").exists():
            import zhlex
            k = zhlex.convert(e)
        elif s == "pdf-law" and source_path(e).exists():
            k = convert_pdf_law(e)
        else:
            continue
        n += 1
        print(f"{e['id']}: {k} Einheiten")
    print(f"{n} Gesetze konvertiert")


if __name__ == "__main__":
    main()
