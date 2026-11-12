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
    if e.get("xml_url"):   # geprüfte Direkt-URL der Konsolidierung (SPARQL findet einzelne Erlasse nicht, z.B. GeBüV, MWSTV)
        dst = R / "raw" / f"{e['id']}.xml"
        urllib.request.urlretrieve(e["xml_url"], dst)
        e["download_url"] = e["xml_url"]
        return dst
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


def artikel_passt(label: str, auswahl: list) -> bool:
    m = re.match(r"Art\.\s*(\d+)([a-z]*)", label or "")
    if not m:
        return False
    n, suf = int(m.group(1)), m.group(2)
    for a in auswahl:
        a = str(a).strip()
        if "-" in a:
            lo, hi = a.split("-", 1)
            if int(lo) <= n <= int(hi):
                return True
        elif a == f"{n}{suf}" or (a.isdigit() and int(a) == n and not suf):
            return True
    return False


def html_md(html: str) -> str:
    """HTML (Hauptinhalt) → Markdown-nahe Textfassung: Überschriften, Absätze, Listen, Tabellen."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "nav", "header", "footer", "noscript", "form"]):
        t.decompose()
    root = soup.find("main") or soup.find("article") or soup.body or soup
    out = []
    for el in root.find_all(["h1", "h2", "h3", "h4", "p", "li", "tr", "dt", "dd"]):
        if el.name == "tr":
            cells = [c.get_text(" ", strip=True).replace("|", "/") for c in el.find_all(["th", "td"])]
            if any(cells):
                out.append("| " + " | ".join(cells) + " |")
            continue
        if el.find_parent(["li", "td", "th"]) and el.name in ("p",):
            continue
        t = el.get_text(" ", strip=True)
        if not t:
            continue
        if el.name in ("h1", "h2", "h3", "h4"):
            out += ["", "#" * (int(el.name[1]) + 1) + " " + t]
        elif el.name == "li":
            out.append("- " + t)
        else:
            out.append(t)
    return "\n".join(out)


def collector_md(d: dict) -> str:
    """admin.ch «api/collector»-JSON (Inhaltsbaum) → Text: Überschriften, Absätze, Tabellen in Dokumentreihenfolge."""
    out = []

    def walk(o):
        if isinstance(o, dict):
            pr = o.get("properties") or {}
            if pr.get("heading") and pr.get("label"):
                lvl = int(str(pr["heading"]).lstrip("h") or 2) if str(pr["heading"]).lstrip("h").isdigit() else 2
                out.extend(["", "#" * min(lvl + 1, 5) + " " + str(pr["label"])])
            for k in ("text", "html", "content", "body"):
                v = pr.get(k)
                if isinstance(v, str) and v.strip():
                    out.append(html_md(v) if "<" in v else v.strip())
            if isinstance(pr.get("bodyRows"), list):   # Tabellen: headerColumns + bodyRows[cellContent[text]]
                def zelle(c):
                    t = " ".join(x.get("text", "") for x in (c.get("cellContent") or []) if isinstance(x, dict)) if isinstance(c, dict) else str(c)
                    return re.sub(r"<[^>]+>", "", t).replace("|", "/").strip()
                if pr.get("caption"):
                    out.append(f"Tabelle: {re.sub(r'<[^>]+>', '', str(pr['caption']))}")
                hc = [re.sub(r"<[^>]+>", "", h.get("text", "")) for h in pr.get("headerColumns") or [] if isinstance(h, dict)]
                if hc:
                    out.extend(["| " + " | ".join(hc) + " |", "|" + "---|" * len(hc)])
                for r in pr["bodyRows"]:
                    if isinstance(r, list):
                        out.append("| " + " | ".join(zelle(c) for c in r) + " |")
            for k in ("rows", "tableRows", "cells"):
                if isinstance(pr.get(k), list):
                    for r in pr[k]:
                        if isinstance(r, list):
                            out.append("| " + " | ".join(str(c.get("text", c) if isinstance(c, dict) else c) for c in r) + " |")
            for k in ("content", "nestedContent", "children", "items"):
                if isinstance(o.get(k), list):
                    for x in o[k]:
                        walk(x)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    title = (d.get("metadata") or {}).get("title")
    if title:
        out.append(f"## {title}")
    walk(d.get("content") or d)
    return "\n".join(x for x in out if x is not None)


def download(e: dict) -> Path:
    raw = R / "raw" / f"{e['id']}.{e['format']}"
    req = urllib.request.Request(e["download_url"], headers={"User-Agent": "revisionswiki-ingest/1.0 (+intern)"})
    with urllib.request.urlopen(req, timeout=120) as r:
        raw.write_bytes(r.read())
    return raw


def ingest(e: dict) -> str:
    now = datetime.date.today().isoformat()
    if e.get("quelle") == "fedlex":
        import akn
        raw = fetch_fedlex(e)
        units = akn.parse_units(str(raw), e["kurz"], e.get("download_url"))
        if e.get("artikel"):   # nur ausgewählte Artikel (z.B. StGB 321, DBG 57–67)
            units = [u for u in units if artikel_passt(u["label"], e["artikel"])]
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
        elif e.get("download_url") and (not raw.exists() or e.get("neu_laden")):
            raw = download(e)
            e.pop("neu_laden", None)
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
        elif e["format"] == "html":
            text = html_md(raw.read_text(encoding="utf-8", errors="replace"))
        elif e["format"] == "json":
            text = collector_md(json.loads(raw.read_text(encoding="utf-8")))
        elif e["format"] == "png":
            text = "(Bild – Inhalt in wiki/ beschrieben)"
        e.update({"raw": f"raw/{raw.name}", "sha256": sha(raw), "abgerufen": e.get("abgerufen") or now})
    head = {k: e.get(k) for k in ("id", "kurz", "titel", "typ", "rang", "stand", "url", "raw", "sha256", "seiten", "lizenz", "transkript", "hinweis", "artikel") if e.get(k) is not None}
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
