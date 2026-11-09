#!/usr/bin/env python3
"""Repariert Zitate in data/*.yaml nach einem Neu-Chunking.

Steht ein Zitat nicht (mehr) im zitierten Chunk, wird es in den Chunks derselben Quelle (Präfix der Chunk-ID)
gesucht; bei eindeutigem Fund wird die Chunk-ID ersetzt. Mehrdeutige/nicht gefundene Zitate werden gemeldet.

  python3 tools/build_index.py && python3 tools/repair_citations.py [--dry]
"""
from __future__ import annotations
import json, sys, yaml
from common import ROOT, ydump
from lint import norm


def main():
    dry = "--dry" in sys.argv
    by_src, texts = {}, {}
    for line in (ROOT / "index" / "chunks.jsonl").open(encoding="utf-8"):
        r = json.loads(line)
        texts[r["id"]] = norm(r["text"])
        by_src.setdefault(r["quelle_id"], []).append(r["id"])
    fixed = unresolved = 0
    files = sorted((ROOT / "data").glob("**/*.yaml"))
    for f in files:
        d = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        changed = False
        for key in ("werte", "positionen", "belege"):
            for row in d.get(key) or []:
                for q in row.get("quellen") or []:
                    cid, z = q.get("chunk"), q.get("zitat")
                    if not cid or not z:
                        continue
                    nz = norm(z)
                    if cid in texts and nz in texts[cid]:
                        continue
                    src = cid.split("__")[0]
                    hits = [c for c in by_src.get(src, []) if nz in texts[c]]
                    if len(hits) == 1:
                        print(f"{f.relative_to(ROOT)}: {cid} -> {hits[0]}")
                        q["chunk"] = hits[0]
                        changed = True
                        fixed += 1
                    else:
                        unresolved += 1
                        print(f"OFFEN {f.relative_to(ROOT)}: {row.get('key') or row.get('id') or row.get('ziffer')} {cid} "
                              f"({'mehrdeutig: ' + ', '.join(hits[:3]) if hits else 'nicht gefunden'})")
        if changed and not dry:
            f.write_text(ydump(d, width=200), encoding="utf-8")
    print(f"repariert: {fixed}, ungelöst: {unresolved}")


if __name__ == "__main__":
    main()
