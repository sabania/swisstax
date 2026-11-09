#!/usr/bin/env python3
"""Baut die Laufzeit-Indizes für tools/steuer.py (L1-Lookup) – nur zur Build-Zeit wird PyYAML gebraucht.

  python3 tools/build_lookup.py          # -> index/lookup.json (+ index/fts.sqlite neu)

lookup.json fasst data/ (Eckwerte, Positionen, Belege, Einreichepflicht, Erkennung) und das Glossar
zusammen; fts.sqlite ist ein SQLite-FTS5-Volltextindex über alle Chunks (Tokenizer unicode61, Diakritika entfernt).
tools/steuer.py und tools/mcp_server.py brauchen zur Laufzeit nur die Python-Standardbibliothek.
"""
from __future__ import annotations
import json, sqlite3, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))


def ylo(p):
    return yaml.safe_load(Path(p).read_text(encoding="utf-8")) or {}


def kurzq(qs, n=3):
    return [{"chunk": q.get("chunk"), "zitat": q.get("zitat")} for q in (qs or [])[:n] if q.get("chunk")]


def main():
    out = {"werte": [], "positionen": [], "belege": [], "einreichen": {}, "glossar": {}, "formulare": {}}
    for p in sorted((ROOT / "data" / "werte").glob("*/*.yaml")):
        d = ylo(p)
        for i, r in enumerate(d.get("werte") or []):
            out["werte"].append({"jur": p.parent.name, "jahr": p.stem, "key": r["key"], "wert": r.get("wert"),
                                 "einheit": r.get("einheit"), "kurz": r.get("kurz"), "text": r.get("text"),
                                 "gilt_fuer": r.get("gilt_fuer"), "status": r.get("status"), "bemerkung": r.get("bemerkung"),
                                 "rechtsgrundlage": r.get("rechtsgrundlage"), "quellen": kurzq(r.get("quellen")),
                                 "ref": f"data/werte/{p.parent.name}/{p.name}#{r['key']}"})
    for p in sorted((ROOT / "data" / "zuordnung").glob("*/*.yaml")):
        d = ylo(p)
        out["formulare"][f"{p.parent.name}-{p.stem}"] = {"formular": d.get("formular"), "hinweis": d.get("hinweis"),
                                                         "bund_spalte": d.get("bund_spalte")}
        for r in d.get("positionen") or []:
            e = {k: r.get(k) for k in ("ziffer", "key", "abschnitt", "bezeichnung", "feld", "rein", "berechnung", "regel",
                                       "beachten", "bund", "belege", "werte_keys", "status", "bemerkung")}
            e.update({"kt": p.parent.name, "jahr": p.stem, "quellen": kurzq(r.get("quellen"), 3),
                      "ref": f"data/zuordnung/{p.parent.name}/{p.name}#{r.get('key')}@{r.get('ziffer')}"})
            out["positionen"].append(e)
    for p in sorted((ROOT / "data").glob("belege-teil*.yaml")):
        for r in ylo(p).get("belege") or []:
            e = {k: r.get(k) for k in ("id", "name", "erkennen", "relevanz", "zweck", "positionen", "extrahieren",
                                       "hinweise", "kantone", "status", "bemerkung")}
            e["quellen"] = kurzq(r.get("quellen"), 2)
            out["belege"].append(e)
    for p in sorted((ROOT / "data" / "einreichen").glob("*/*.yaml")):
        d = ylo(p)
        out["einreichen"].setdefault(p.parent.name, {})[p.stem] = d
    g = ylo(ROOT / "registry" / "glossar.yaml").get("glossar") or {}
    out["glossar"] = {k: v for k, v in g.items()}
    out["erkennung"] = ylo(ROOT / "data" / "ablage" / "erkennung.yaml")
    (ROOT / "index" / "lookup.json").write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":"), default=str),
                                                encoding="utf-8")
    print(f"index/lookup.json: {len(out['werte'])} Werte · {len(out['positionen'])} Positionen · {len(out['belege'])} Belege · "
          f"Einreichepflicht {sum(len(v) for v in out['einreichen'].values())} Kanton-Jahre")
    import steuer
    n = steuer.baue_fts(force=True)
    print(f"index/fts.sqlite: {n} Chunks")


if __name__ == "__main__":
    main()
