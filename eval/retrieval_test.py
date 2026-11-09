#!/usr/bin/env python3
"""Retrieval-Test: findet die Suche die Belegstellen (Gold-Chunks) einer Frage?

Gold: Chunk-IDs aus eval/erwartet.yaml (Soll-Antworten) und eval/blindtest-fragen.yaml (fundstellen).
Treffer: Ergebnis ist die Gold-Chunk-Datei ODER der gefundene Abschnitt einer Quick-/Wiki-Seite zitiert die Gold-Chunk-ID.

  python3 eval/retrieval_test.py --backend openclaw --agent steuer --workspace ~/.openclaw/workspace-steuer --label trigram
  python3 eval/retrieval_test.py --backend search.py --label bm25            # tools/search.py (lokal, ohne OpenClaw)
  python3 eval/retrieval_test.py --backend search.py --expand --label bm25+glossar

Ausgabe: Hit@1/3/5/10 und MRR, plus JSON mit Einzelergebnissen (--out).
"""
from __future__ import annotations
import argparse, json, re, subprocess, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
CID = re.compile(r"\b[a-z0-9][a-z0-9-]*__(?:c\d{4}|art-[0-9a-z-]+|par-[0-9a-z-]+|anhang-[0-9a-z-]+)\b")


def testset():
    fr = {q["id"]: q["frage"] for q in yaml.safe_load((ROOT / "eval/fragen.yaml").read_text(encoding="utf-8"))["fragen"]}
    erw = yaml.safe_load((ROOT / "eval/erwartet.yaml").read_text(encoding="utf-8"))["erwartet"]
    out = []
    for qid, txt in erw.items():
        gold = set(CID.findall(txt))
        # Kurzformen «bund-rs-2-215__c0010/c0011» auflösen
        for m in re.finditer(r"([a-z0-9-]+)__c\d{4}((?:/c\d{4})+)", txt):
            for extra in m.group(2).split("/")[1:]:
                gold.add(f"{m.group(1)}__{extra}")
        if gold and qid in fr:
            out.append({"id": qid, "query": fr[qid], "gold": sorted(gold)})
    bp = ROOT / "eval/blindtest-fragen.yaml"
    if bp.exists():
        for q in yaml.safe_load(bp.read_text(encoding="utf-8"))["blindtest"]["fragen"]:
            if q.get("fundstellen"):
                out.append({"id": q["id"], "query": q["frage"], "gold": sorted(set(q["fundstellen"]))})
    return out


STOP = set("der die das und oder in im am an auf aus bei bis für mit nach von vom zu zum zur ein eine einer eines dem den des ist sind wird werden als auch nicht nur wie wenn so es sie er ab je pro über welche welcher welches wie hoch gilt gibt darf kann was wo wann wer bitte mit fundstellen dürfen soll muss beim noch einen einem".split())


def stichworte(q: str) -> str:
    """Stichwort-Anfrage wie sie Agenten formulieren: Fragewörter/Füllwörter weg, Fachbegriffe/Zahlen/Kürzel bleiben."""
    ws = re.findall(r"[A-Za-zÄÖÜäöüß0-9'.-]+", q)
    return " ".join(w.strip(".") for w in ws if w.lower().strip(".") not in STOP and len(w.strip(".")) > 1)


def hits_openclaw(q, a):
    cmd = [a.openclaw, "memory", "search", "--agent", a.agent, "--json", "--max-results", str(a.k), "--query", q]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    try:
        res = json.loads(p.stdout)["results"]
    except Exception:
        return None
    ws = Path(a.workspace).expanduser()
    out = []
    for r in res:
        f = ws / r["path"]
        ids = set()
        stem = Path(r["path"]).stem
        if "__" in stem:
            ids.add(stem)
        try:
            lines = f.read_text(encoding="utf-8").splitlines()[max(0, r["startLine"] - 1): r["endLine"]]
            ids |= set(CID.findall("\n".join(lines)))
        except Exception:
            pass
        out.append({"path": r["path"], "ids": sorted(ids)})
    return out


def hits_search(q, a):
    cmd = [sys.executable, str(ROOT / "tools/search.py"), q, "-n", str(a.k)] + (["--expand"] if a.expand else [])
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=180, cwd=ROOT / "tools")
    out = []
    for line in p.stdout.splitlines():
        m = re.match(r"\s*[\d.]+\s+(\S+__\S+)\s", line)
        if m:
            out.append({"path": m.group(1), "ids": [m.group(1)]})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=["openclaw", "search.py"], required=True)
    ap.add_argument("--agent", default="steuer")
    ap.add_argument("--workspace", default=".")
    ap.add_argument("--openclaw", default="openclaw")
    ap.add_argument("--expand", action="store_true")
    ap.add_argument("-k", type=int, default=10)
    ap.add_argument("--label", default="lauf")
    ap.add_argument("--out")
    ap.add_argument("--stichworte", action="store_true", help="Frage in Stichwort-Anfrage umwandeln (wie Agenten suchen)")
    a = ap.parse_args()
    ts = testset()
    if a.stichworte:
        for t in ts:
            t["query"] = stichworte(t["query"])
    rows, mrr = [], 0.0
    hit = {1: 0, 3: 0, 5: 0, 10: 0}
    for t in ts:
        res = hits_openclaw(t["query"], a) if a.backend == "openclaw" else hits_search(t["query"], a)
        rank = None
        for i, r in enumerate(res or []):
            if set(r["ids"]) & set(t["gold"]):
                rank = i + 1
                break
        for k in hit:
            hit[k] += 1 if rank and rank <= k else 0
        mrr += 1 / rank if rank else 0
        rows.append({**t, "rank": rank, "top": [r["path"] for r in (res or [])[:5]]})
        print(f"{t['id']}: rank {rank}", flush=True)
    n = len(ts)
    summ = {"label": a.label, "n": n, **{f"hit@{k}": round(v / n, 3) for k, v in hit.items()}, "mrr": round(mrr / n, 3)}
    print(json.dumps(summ, ensure_ascii=False))
    if a.out:
        Path(a.out).write_text(json.dumps({"summary": summ, "rows": rows}, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
