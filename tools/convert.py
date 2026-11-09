#!/usr/bin/env python3
"""Konvertiert raw/-Dateien (PDF, HTML) nach sources/<jur>/<jahr>/<id>.md (Volltext, verbatim).

PDF : pdftotext -layout (poppler) pro Seite, Seitenmarker <!-- Seite N -->, wiederkehrende
      Kopf-/Fusszeilen werden entfernt. Der Text bleibt sonst unverändert (keine Umformulierung).
HTML: Hauptinhalt je Website (Selektoren unten) -> Markdown (markdownify).
Gesetze mit strukturierter Quelle (Fedlex-XML, LexWork-JSON) werden von tools/laws.py verarbeitet.

  python3 tools/convert.py            # alle (ausser verarbeitung=link)
  python3 tools/convert.py --id ar-wl-2025
"""
from __future__ import annotations
import argparse, collections, re, subprocess, sys
from bs4 import BeautifulSoup
from markdownify import markdownify
from common import load_registry, raw_path, source_path, frontmatter, JUR_LABEL, TYP_LABEL, today

HTML_SELECTORS = [  # (host-substring, css selector)
    ("steuerpraxis.tg.ch", "article"),
    ("steuerverwaltung.tg.ch", "main"),
    ("sg.ch", "#content"),
    ("zh.ch", "main"),
    ("ar.ch", "main"),
    ("admin.ch", "main"),
    ("parlament.ch", "main"),
]
DROP_RE = re.compile(r"(breadcrumb|pfadnav|navigation|subnav|nav-|menu|sidebar|contact|kontakt|footer|share|social|cookie|skip|teaser-list|related|feedback|search)", re.I)


def pdf_pages(path) -> list[str]:
    out = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", str(path), "-"], capture_output=True, text=True).stdout
    pages = out.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


def norm_line(l: str) -> str:
    return re.sub(r"\d+", "#", l.strip())


def strip_headers_footers(pages: list[str]) -> list[str]:
    if len(pages) < 4:
        return pages
    cnt = collections.Counter()
    for p in pages:
        lines = [l for l in p.splitlines() if l.strip()]
        cand = set(norm_line(l) for l in lines[:3] + lines[-3:])
        cnt.update(cand)
    rep = {k for k, v in cnt.items() if v >= max(3, int(len(pages) * 0.5)) and len(k) < 160}
    cleaned = []
    for p in pages:
        lines = p.splitlines()
        nonempty = [i for i, l in enumerate(lines) if l.strip()]
        edge = set(nonempty[:3] + nonempty[-3:])
        cleaned.append("\n".join(l for i, l in enumerate(lines) if not (i in edge and norm_line(l) in rep)))
    return cleaned


def clean_text(t: str) -> str:
    t = t.replace("­", "")  # weiche Trennstriche
    t = re.sub("[    ]", " ", t)    # geschützte/schmale Leerzeichen -> Leerzeichen
    t = re.sub(r"(?<=\S)[ \t]{3,}", "   ", t)           # Spaltenabstände auf 3 Leerzeichen komprimieren
    t = re.sub(r"(?m)^[ \t]{5,}", "    ", t)            # Einzug auf max. 4 Leerzeichen (Randtitel bleiben unterscheidbar)
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{4,}", "\n\n\n", t)
    return t.strip("\n")


def pdf_to_md(e: dict, p) -> tuple[str, dict]:
    pages = strip_headers_footers(pdf_pages(p))
    max_pages = e.get("max_seiten")
    parts = []
    for i, pg in enumerate(pages, 1):
        if max_pages and i > max_pages:
            parts.append(f"<!-- Seite {i}–{len(pages)}: nicht konvertiert (max_seiten={max_pages}, siehe raw/) -->")
            break
        parts.append(f"<!-- Seite {i} -->\n{clean_text(pg)}")
    return "\n\n".join(parts) + "\n", {"seiten": len(pages), "konvertierung": "pdftotext -layout (poppler), Kopf-/Fusszeilen entfernt, sonst verbatim"}


def html_to_md(e: dict, p) -> tuple[str, dict]:
    soup = BeautifulSoup(p.read_bytes(), "lxml")
    url = e.get("final_url") or e["url"]
    sel = next((s for h, s in HTML_SELECTORS if h in url), "main")
    root = soup.select_one(sel) or soup.select_one("main") or soup.body
    for tag in root.find_all(["script", "style", "nav", "header", "footer", "aside", "form", "button", "svg", "noscript", "iframe"]):
        tag.decompose()
    for tag in root.find_all(True):
        if tag.decomposed if hasattr(tag, "decomposed") else False:
            continue
        attrs = getattr(tag, "attrs", None) or {}
        ident = " ".join([attrs.get("id", "") or ""] + list(attrs.get("class", []) or []))
        if ident and DROP_RE.search(ident) and tag.name not in ("main", "article", "body"):
            tag.decompose()
    # absolute Links
    from urllib.parse import urljoin
    for a in root.find_all("a", href=True):
        a["href"] = urljoin(url, a["href"])
    md = markdownify(str(root), heading_style="ATX", bullets="-", strip=["img"])
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = re.sub(r"[ \t]+\n", "\n", md)
    return md.strip() + "\n", {"konvertierung": f"HTML-Hauptinhalt ({sel}) -> Markdown (markdownify)"}


def convert(e: dict) -> bool:
    p = raw_path(e)
    if not p.exists():
        print(f"fehlt raw: {e['id']}", file=sys.stderr)
        return False
    if e["format"] == "pdf":
        body, meta = pdf_to_md(e, p)
    elif e["format"] == "html":
        body, meta = html_to_md(e, p)
    else:
        return False
    fm = {"id": e["id"], "titel": e["titel"], "kurz": e.get("kurz"), "jurisdiktion": e["jurisdiktion"],
          "jahre": e.get("jahre"), "typ": e["typ"], "stand": e.get("stand"), "quelle_url": e["url"],
          "raw": str(p.relative_to(p.parents[3])), "sha256": e.get("sha256"), "abgerufen": e.get("abgerufen")}
    fm.update(meta)
    fm = {k: v for k, v in fm.items() if v not in (None, "", [])}
    head = f"# {e['titel']}\n\n> {JUR_LABEL[e['jurisdiktion']]} · {TYP_LABEL.get(e['typ'], e['typ'])} · Quelle: <{e['url']}>\n\n"
    sp = source_path(e)
    sp.parent.mkdir(parents=True, exist_ok=True)
    sp.write_text(frontmatter(fm) + head + body, encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", action="append")
    a = ap.parse_args()
    n = 0
    for e in load_registry():
        if a.id and e["id"] not in a.id:
            continue
        if e.get("verarbeitung") in ("link", "original") or e.get("strukturiert"):
            continue
        if convert(e):
            n += 1
    print(f"{n} Quellen konvertiert")


if __name__ == "__main__":
    main()
