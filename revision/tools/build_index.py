#!/usr/bin/env python3
"""Revisions-Wiki: Index bauen → index/chunks.jsonl (alle Chunks mit Metadaten) und index/fts.sqlite (SQLite-FTS5).

  python3 revision/tools/build_index.py
"""
from __future__ import annotations
import collections, json, os, re, sqlite3
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


WORT = re.compile(r"[A-Za-zÄÖÜäöüß]+")
TRENN = re.compile(r"([A-Za-zÄÖÜäöüß]+)-?\n([a-zäöüß]+)")


def entrenner(rows):
    """Silbentrennung am Zeilenende (im PDF ohne Trennstrich verloren, z.B. «Forde\nrungen») nur für den Suchindex auflösen:
    zusammenfügen, wenn das zusammengesetzte Wort im Korpus häufiger ist als beide Teile. Der Chunk-Text bleibt unverändert."""
    freq = collections.Counter(w.lower() for r in rows for w in WORT.findall(r["text"]))

    def fix(m):
        a, b = m.group(1), m.group(2)
        j = (a + b).lower()
        return a + b if freq[j] >= 3 and freq[j] > max(freq[a.lower()], freq[b.lower()]) else m.group(0)
    return lambda t: TRENN.sub(fix, t)


def main():
    rows = [read_chunk(p) for p in sorted((R / "chunks").glob("*/*.md"))]
    (R / "index").mkdir(exist_ok=True)
    with (R / "index" / "chunks.jsonl").open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    db = R / "index" / "fts.sqlite"
    tmp = db.with_suffix(".sqlite.tmp")
    if tmp.exists():
        tmp.unlink()
    con = sqlite3.connect(tmp)
    # Inhaltstabelle (Wortlaut für zeige/pruefe-zitat, Metadaten) + kontaktloser FTS5-Index über entrennten Text (gleiche rowid)
    con.execute("create table chunk (id text primary key, quelle text, kurz text, typ text, rang integer, seiten text, datei text, "
                "titel text, pfad text, kontext text, text text)")
    con.execute("create virtual table chunks using fts5(titel, pfad, text, content='', tokenize='unicode61 remove_diacritics 2')")
    ent = entrenner(rows)
    for i, r in enumerate(rows, 1):
        con.execute("insert into chunk(rowid, id, quelle, kurz, typ, rang, seiten, datei, titel, pfad, kontext, text) values (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (i, r["id"], r["quelle"], r["kurz"], r["typ"], r.get("rang") or 9, str(r.get("seiten") or ""), r["datei"],
                     r.get("titel") or "", r.get("pfad") or "", r.get("kontext") or "", r["text"]))
        con.execute("insert into chunks(rowid, titel, pfad, text) values (?,?,?,?)", (i, r.get("titel") or "", r.get("pfad") or "", ent(r["text"])))
    con.commit()
    con.execute("vacuum")
    con.close()
    os.replace(tmp, db)   # atomar: laufende Leser sehen alte oder neue Datei, nie eine halbe
    by = {}
    for r in rows:
        by[r["quelle"]] = by.get(r["quelle"], 0) + 1
    print(f"index: {len(rows)} Chunks aus {len(by)} Quellen")


if __name__ == "__main__":
    main()
