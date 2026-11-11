#!/usr/bin/env python3
"""Revisions-Wiki: Index bauen → index/chunks.jsonl (alle Chunks mit Metadaten) und index/fts.sqlite (SQLite-FTS5).

  python3 revision/tools/build_index.py
"""
from __future__ import annotations
import json, re, sqlite3
from pathlib import Path
import yaml

R = Path(__file__).resolve().parents[1]


def read_chunk(p: Path) -> dict:
    t = p.read_text(encoding="utf-8")
    _, fm, body = t.split("---\n", 2)
    meta = yaml.safe_load(fm)
    meta["datei"] = str(p.relative_to(R))
    lines = body.strip().split("\n", 2)
    meta["kontext"] = lines[0].lstrip("> ").strip() if lines and lines[0].startswith(">") else ""
    meta["text"] = (lines[2] if len(lines) > 2 else body).strip() if meta["kontext"] else body.strip()
    return meta


def main():
    rows = [read_chunk(p) for p in sorted((R / "chunks").glob("*/*.md"))]
    (R / "index").mkdir(exist_ok=True)
    with (R / "index" / "chunks.jsonl").open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    db = R / "index" / "fts.sqlite"
    if db.exists():
        db.unlink()
    con = sqlite3.connect(db)
    con.execute("create virtual table chunks using fts5(id unindexed, quelle unindexed, kurz unindexed, typ unindexed, "
                "rang unindexed, seiten unindexed, datei unindexed, titel, pfad, text, tokenize='unicode61 remove_diacritics 2')")
    con.executemany("insert into chunks values (?,?,?,?,?,?,?,?,?,?)",
                    [(r["id"], r["quelle"], r["kurz"], r["typ"], r.get("rang") or 9, str(r.get("seiten") or ""), r["datei"],
                      r.get("titel") or "", r.get("pfad") or "", r["text"]) for r in rows])
    con.commit()
    con.close()
    by = {}
    for r in rows:
        by[r["quelle"]] = by.get(r["quelle"], 0) + 1
    print(f"index: {len(rows)} Chunks aus {len(by)} Quellen")


if __name__ == "__main__":
    main()
