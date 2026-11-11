#!/usr/bin/env python3
"""Revisions-Wiki: Quellen einlesen (Original → raw/, Volltext → sources/<id>.md mit Seitenmarkern).

  python3 revision/tools/ingest.py            # alle Quellen der Registry
  python3 revision/tools/ingest.py --id or     # nur eine

PDF: pdftotext je Seite (<!-- Seite N -->), Kopf-/Fusszeilen mit Lizenzvermerk werden entfernt.
DOCX: Absätze/Überschriften/Tabellen → Markdown. XLSX: je Blatt eine Markdown-Tabelle. OR: Fedlex-XML je Artikel (tools/akn.py).
Die Registry wird um raw, sha256, seiten, abgerufen ergänzt; das Feld «datei» (Pfad der Lieferung) wird durch «original» ersetzt.
"""
from __future__ import annotations
import argparse, datetime, hashlib, json, re, shutil, subprocess, sys, urllib.parse, urllib.request
from pathlib import Path
import yaml

R = Path(__file__).resolve().parents[1]           # revision/
ROOT = R.parent
sys.path.insert(0, str(ROOT / "tools"))
REG = R / "registry" / "sources.yaml"

LIZENZ_RE = re.compile(r"©\s*20\d\d\s*EXPERTsuisse.*$|Nutzungsberechtigt:.*$", re.M)


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def fm(d: dict) -> str:
    return "---\n" + yaml.safe_dump(d, allow_unicode=True, sort_keys=False, width=200) + "---\n"


def pdf_pages(p: Path) -> list[str]:
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(p)], capture_output=True, text=True).stdout).group(1))
    out = subprocess.run(["pdftotext", str(p), "-"], capture_output=True, text=True).stdout
    pages = out.split("\f")
    return [LIZENZ_RE.sub("", x).strip() for x in pages[:n]]


def docx_md(p: Path) -> str:
    import docx
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    d = docx.Document(str(p))
    out = []
    for el in d.element.body.iterchildren():
        tag = el.tag.split("}")[1]
        if tag == "p":
            para = Paragraph(el, d)
            t = para.text.strip()
            if not t:
                continue
            st = (para.style.name or "").lower()
            if st.startswith(("heading", "überschrift", "titel", "title")):
                lvl = "".join(c for c in st if c.isdigit()) or "1"
                out.append("#" * min(int(lvl) + 1, 6) + " " + t)
            elif "list" in st or "liste" in st:
                out.append("- " + t)
            else:
                out.append(t)
        elif tag == "tbl":
            tb = Table(el, d)
            for i, r in enumerate(tb.rows):
                cells = []
                for c in r.cells:
                    x = c.text.strip().replace("\n", " / ").replace("|", "/")
                    if not cells or cells[-1] != x:
                        cells.append(x)
                out.append("| " + " | ".join(cells) + " |")
                if i == 0:
                    out.append("|" + "---|" * len(cells))
            out.append("")
    return "\n".join(out)


def xlsx_md(p: Path) -> str:
    import openpyxl
    wb = openpyxl.load_workbook(str(p), data_only=True)
    out = []
    for ws in wb.worksheets:
        out += ["", f"## Blatt «{ws.title}»", ""]
        rows = [[("" if c is None else str(c)).replace("|", "/").replace("\n", " ") for c in r] for r in ws.iter_rows(values_only=True)]
        rows = [r for r in rows if any(x.strip() for x in r)]
        if not rows:
            continue
        w = max(len(r) for r in rows)
        for i, r in enumerate(rows):
            out.append("| " + " | ".join(r + [""] * (w - len(r))) + " |")
            if i == 0:
                out.append("|" + "---|" * w)
    return "\n".join(out)


FEDLEX = "https://fedlex.data.admin.ch/sparqlendpoint"
Q = """PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
SELECT DISTINCT ?act ?consolidation ?dateApplicability ?xmlFile WHERE {
  ?act a jolux:ConsolidationAbstract ; jolux:classifiedByTaxonomyEntry/skos:notation ?n . FILTER(str(?n) = "%s")
  ?consolidation a jolux:Consolidation ; jolux:isMemberOf ?act ; jolux:dateApplicability ?dateApplicability .
  OPTIONAL { ?consolidation jolux:dateEndApplicability ?end }
  FILTER(?dateApplicability <= "%s"^^xsd:date && (!BOUND(?end) || ?end >= "%s"^^xsd:date))
  ?consolidation jolux:isRealizedBy ?expr . ?expr jolux:language <http://publications.europa.eu/resource/authority/language/DEU> ;
  jolux:isEmbodiedBy ?mx . ?mx jolux:userFormat <https://fedlex.data.admin.ch/vocabulary/user-format/xml> ; jolux:isExemplifiedBy ?xmlFile . }"""


def fetch_fedlex(e: dict) -> Path:
    day = datetime.date.today().isoformat()
    data = urllib.parse.urlencode({"query": Q % (e["sr"], day, day)}).encode()
    req = urllib.request.Request(FEDLEX, data=data, headers={"Accept": "application/sparql-results+json"})
    rows = [{k: v["value"] for k, v in b.items()} for b in json.load(urllib.request.urlopen(req, timeout=120))["results"]["bindings"]]
    r = sorted(rows, key=lambda x: x["dateApplicability"])[-1]
    dst = R / "raw" / f"{e['id']}.xml"
    urllib.request.urlretrieve(r["xmlFile"], dst)
    eli = r["act"].split("/eli/")[1]
    date = r["consolidation"].rsplit("/", 1)[1]
    e.update({"url": f"https://www.fedlex.admin.ch/eli/{eli}/{date}/de", "stand": r["dateApplicability"], "download_url": r["xmlFile"]})
    return dst


def ingest(e: dict) -> str:
    now = datetime.date.today().isoformat()
    if e.get("quelle") == "fedlex":
        import akn
        raw = fetch_fedlex(e)
        units = akn.parse_units(str(raw), e["kurz"], e.get("download_url"))
        md, arts = [], []
        for u in units:
            body = akn.FN_RE.sub("", u["body"]).strip()
            head = f"{u['label']} {e['kurz']}" + (f" – {u['title']}" if u["title"] else "")
            md += [f"## {head}", "", f"*{' > '.join([e['kurz']] + u['path'])}*", "", body, ""]
            arts.append({"eid": u["eid"], "label": u["label"], "titel": head, "pfad": u["path"], "text": body,
                         "aufgehoben": u["repealed"]})
        (R / "sources" / f"{e['id']}.articles.json").write_text(json.dumps(arts, ensure_ascii=False), encoding="utf-8")
        text = "\n".join(md)
        e.update({"raw": f"raw/{raw.name}", "sha256": sha(raw), "einheiten": len(arts), "abgerufen": now})
    else:
        src = Path(e.pop("datei")) if e.get("datei") else None
        raw = R / "raw" / f"{e['id']}.{e['format']}"
        if src:
            shutil.copy2(src, raw)
            e["original"] = src.name
        if e.get("transkript"):
            # Bildscan ohne Textlayer: wörtliche Abschrift (Agent, nachgeprüft) aus registry/transkripte/ übernehmen
            text = (R / e["transkript"]).read_text(encoding="utf-8").strip()
            e["seiten"] = text.count("<!-- Seite ") or e.get("seiten")
        elif e["format"] == "pdf":
            pages = pdf_pages(raw)
            e["seiten"] = len(pages)
            text = "\n\n".join(f"<!-- Seite {i} -->\n{p}" for i, p in enumerate(pages, 1))
        elif e["format"] == "docx":
            text = docx_md(raw)
        elif e["format"] == "xlsx":
            text = xlsx_md(raw)
        elif e["format"] == "png":
            text = "(Bild – Inhalt in wiki/ beschrieben)"
        e.update({"raw": f"raw/{raw.name}", "sha256": sha(raw), "abgerufen": e.get("abgerufen") or now})
    head = {k: e.get(k) for k in ("id", "kurz", "titel", "typ", "rang", "stand", "url", "raw", "sha256", "seiten", "lizenz", "transkript", "hinweis") if e.get(k) is not None}
    (R / "sources" / f"{e['id']}.md").write_text(fm(head) + f"# {e['titel']}\n\n" + text + "\n", encoding="utf-8")
    return f"{e['id']}: {len(text):,} Zeichen"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", action="append")
    a = ap.parse_args()
    reg = yaml.safe_load(REG.read_text(encoding="utf-8"))
    for e in reg:
        if a.id and e["id"] not in a.id:
            continue
        print(ingest(e), flush=True)
    head = "\n".join(l for l in REG.read_text(encoding="utf-8").splitlines() if l.startswith("#"))
    REG.write_text(head + "\n" + yaml.safe_dump(reg, allow_unicode=True, sort_keys=False, width=200), encoding="utf-8")


if __name__ == "__main__":
    main()
