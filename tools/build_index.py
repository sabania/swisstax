#!/usr/bin/env python3
"""Baut die maschinenlesbaren Indizes und die Quellenkataloge.

Erzeugt:
  index/chunks.jsonl      – alle Chunks mit vollständigen Metadaten + Text (für externes Hybrid-RAG: BM25 + Vektor)
  index/quellen.jsonl     – alle Quellen aus registry/sources.yaml + Statistik
  wiki/<jur>/<jur>-quellen.md – Quellenkatalog je Jurisdiktion (nach Jahr und Dokumenttyp)

  python3 tools/build_index.py
"""
from __future__ import annotations
import json, re, hashlib, collections
from common import (load_registry, source_path, chunk_dir, raw_path, read_frontmatter, ROOT, INDEX, JUR_LABEL, TYP_LABEL)

TYP_ORDER = ["gesetz", "verordnung", "weisung", "kreisschreiben", "rundschreiben", "wegleitung", "formular", "merkblatt",
             "praxis", "steuerfuss", "tarif", "mitteilung", "info", "portal", "tool"]


def rel(p, base):
    import os
    return os.path.relpath(p, base)


def main():
    reg = load_registry()
    INDEX.mkdir(exist_ok=True)
    nchunks = 0
    stats = collections.Counter()
    with open(INDEX / "chunks.jsonl", "w", encoding="utf-8") as out:
        for e in reg:
            d = chunk_dir(e)
            if not d.exists():
                continue
            meta = {}
            mp = d / "_meta.json"
            if mp.exists():
                meta = {m["id"]: m for m in json.loads(mp.read_text(encoding="utf-8"))}
            for f in sorted(d.glob("*.md")):
                fm, body = read_frontmatter(f.read_text(encoding="utf-8"))
                lines = body.split("\n", 2)
                crumb = lines[0][2:].strip() if lines and lines[0].startswith("> ") else ""
                text = lines[2] if len(lines) > 2 else body
                m = meta.get(fm.get("id"), {})
                seiten = m.get("seiten") or []
                rec = {
                    "id": fm.get("id"), "quelle_id": e["id"], "jurisdiktion": e["jurisdiktion"], "jahre": e.get("jahre"),
                    "typ": e["typ"], "dokument": e["titel"], "kurz": e.get("kurz"), "titel": fm.get("titel"),
                    "pfad": m.get("pfad"), "artikel": m.get("artikel"), "ziffer": m.get("ziffer"), "seiten": seiten,
                    "stand": e.get("stand"), "gilt_ab": e.get("gilt_ab"),
                    "quelle_url": e["url"] + (f"#page={seiten[0]}" if seiten and e.get("format") == "pdf" and not e.get("zip_member") else ""),
                    "datei": str(f.relative_to(ROOT)), "quelle_md": str(source_path(e).relative_to(ROOT)),
                    "raw": str(raw_path(e).relative_to(ROOT)), "stichworte": m.get("stichworte"),
                    "positionen": m.get("positionen"), "zusammenfassung": m.get("zusammenfassung"),
                    "vorher": m.get("vorher"), "nachher": m.get("nachher"), "chunking": m.get("chunking"),
                    "kontext": crumb, "text": text.strip(), "zeichen": len(text.strip()),
                    "sha256": hashlib.sha256(text.strip().encode()).hexdigest()[:16],
                }
                out.write(json.dumps({k: v for k, v in rec.items() if v not in (None, [], "")}, ensure_ascii=False) + "\n")
                nchunks += 1
                stats[e["jurisdiktion"]] += 1
    with open(INDEX / "quellen.jsonl", "w", encoding="utf-8") as out:
        for e in reg:
            d = chunk_dir(e)
            rec = dict(e)
            rec["chunks"] = len(list(d.glob("*.md"))) if d.exists() else 0
            rec["quelle_md"] = str(source_path(e).relative_to(ROOT)) if source_path(e).exists() else None
            rec["raw_datei"] = str(raw_path(e).relative_to(ROOT)) if raw_path(e).exists() else None
            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
    # Quellenkataloge
    for jur in JUR_LABEL:
        base = ROOT / "wiki" / jur
        base.mkdir(parents=True, exist_ok=True)
        rows = [e for e in reg if e["jurisdiktion"] == jur]
        by_year = collections.defaultdict(list)
        for e in rows:
            by_year[str(e["ordner_jahr"])].append(e)
        L = ["---", f"typ: quellenkatalog", f"jur: {jur}", f"titel: \"Quellenkatalog {JUR_LABEL[jur]}\"", "generiert: tools/build_index.py", "---",
             f"# Quellenkatalog – {JUR_LABEL[jur]}", "",
             "Alle erfassten Quellen dieser Jurisdiktion. Spalten: Kurzbezeichnung · Titel · gilt für Steuerjahre · Links "
             "(Volltext-Markdown, Chunks, Original). «Ordner» = erstes Steuerjahr der Fassung bzw. `dauernd` für jahresunabhängige Dokumente.", ""]
        for y in sorted(by_year, key=lambda x: (x == "dauernd", x)):
            L += [f"## Ordner {y}", "", "| Typ | Kurz | Titel | Jahre | Volltext | Chunks | Original |", "|---|---|---|---|---|---|---|"]
            for e in sorted(by_year[y], key=lambda e: (TYP_ORDER.index(e["typ"]) if e["typ"] in TYP_ORDER else 99, e["id"])):
                sp, cd, rp = source_path(e), chunk_dir(e), raw_path(e)
                n = len(list(cd.glob("*.md"))) if cd.exists() else 0
                vt = f"[md]({rel(sp, base)})" if sp.exists() else "–"
                ck = f"[{n}]({rel(cd, base)}/)" if n else "–"
                rw = f"[{e.get('format', '')}]({rel(rp, base)})" if rp.exists() else f"[web]({e['url']})"
                jahre = ", ".join(map(str, e.get("jahre") or []))
                titel = e["titel"].replace("|", "/")
                hint = f" ⚠ {e['hinweis']}" if e.get("hinweis") else ""
                L.append(f"| {TYP_LABEL.get(e['typ'], e['typ'])} | {e.get('kurz') or ''} | [{titel}]({e['url']}){hint} | {jahre} | {vt} | {ck} | {rw} |")
            L.append("")
        (base / f"{jur}-quellen.md").write_text("\n".join(L), encoding="utf-8")
    print(f"index/chunks.jsonl: {nchunks} Chunks {dict(stats)}; index/quellen.jsonl: {len(reg)} Quellen; Kataloge geschrieben")


if __name__ == "__main__":
    main()
