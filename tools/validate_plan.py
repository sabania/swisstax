#!/usr/bin/env python3
"""Prüft einen semantischen Chunk-Plan registry/chunkplans/<id>.json und zeigt eine Vorschau.

Plan-Format:
{"id": "<quelle-id>", "chunks": [
   {"start": 12, "titel": "Ziff. 1.1 Haupterwerb", "pfad": ["Einkünfte", "Ziff. 1"], "ziffer": "1.1",
    "stichworte": ["Lohnausweis", "Nettolohn"], "positionen": ["einkommen.unselbstaendig.haupterwerb"],
    "zusammenfassung": "…"},
   {"start": 40, "skip": true, "titel": "Inhaltsverzeichnis"} , ...]}
- start = 1-basierte Zeilennummer im TEXTKÖRPER von sources/<jur>/<jahr>/<id>.md (Zeile 1 = erste Zeile nach der
  Frontmatter); Plan-Feld "basis": "koerper". So bleiben Pläne gültig, wenn sich Metadaten in der Frontmatter ändern.
  (Ältere Pläne ohne "basis" zählen ab Dateianfang.)
- Starts streng aufsteigend; ein Chunk reicht bis zur Zeile vor dem nächsten Start.

  python3 tools/validate_plan.py <id> [--preview]
"""
import json, sys, re, yaml
from common import load_registry, source_path, ROOT
import chunk as ch

def main():
    pid = sys.argv[1]
    preview = "--preview" in sys.argv
    e = next(x for x in load_registry() if x["id"] == pid)
    plan = json.loads((ROOT / "registry" / "chunkplans" / f"{pid}.json").read_text(encoding="utf-8"))
    full = source_path(e).read_text(encoding="utf-8").splitlines()
    errs, warn = [], []
    starts = ch.plan_starts(plan, full) if all(isinstance(c.get("start"), int) for c in plan.get("chunks", [])) else [c.get("start") for c in plan.get("chunks", [])]
    if not starts:
        errs.append("keine chunks")
    body_start = next((i + 2 for i, l in enumerate(full[1:], 1) if l == "---"), 1)
    if starts and starts[0] > body_start + 6:
        warn.append(f"erster Start {starts[0]} – Zeilen {body_start}-{starts[0]-1} gehören zu keinem Chunk (wird verworfen)")
    for a, b in zip(starts, starts[1:]):
        if not (isinstance(a, int) and isinstance(b, int) and b > a):
            errs.append(f"Starts nicht streng aufsteigend: {a} -> {b}")
    if starts and starts[-1] > len(full):
        errs.append(f"Start {starts[-1]} > Dateilänge {len(full)}")
    known = set(yaml.safe_load((ROOT / "registry" / "taxonomy.yaml").read_text())["positionen"])
    for c in plan.get("chunks", []):
        for p in c.get("positionen") or []:
            if p not in known:
                errs.append(f"unbekannter Positionsschlüssel: {p}")
        if not c.get("skip") and not c.get("titel"):
            errs.append(f"Chunk ab Zeile {c.get('start')} ohne titel")
    items = ch.plan_items(e, full, plan) if not errs else []
    sizes = [len(i["text"]) for i in items]
    split = sum(1 for i in items if "(Teil " in (i.get("titel") or ""))
    tiny = [i["titel"] for i in items if len(i["text"]) < 150]
    print(f"{pid}: {len(plan.get('chunks', []))} Plan-Einträge -> {len(items)} Chunks; Zeichen min/median/max = "
          f"{min(sizes) if sizes else 0}/{sorted(sizes)[len(sizes)//2] if sizes else 0}/{max(sizes) if sizes else 0}; "
          f"automatisch geteilt: {split}; sehr klein (<150 Z.): {len(tiny)}")
    for w in warn: print("WARNUNG", w)
    for t in tiny[:10]: print("  klein:", t)
    for x in errs: print("FEHLER", x)
    if preview:
        for i in items:
            print(f"--- {i['id']} | {i['titel']} | S.{i.get('seiten')} | {len(i['text'])} Z.\n{i['text'][:200]}")
    sys.exit(1 if errs else 0)

if __name__ == "__main__":
    main()
