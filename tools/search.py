#!/usr/bin/env python3
"""Einfache lokale Volltextsuche (BM25) über index/chunks.jsonl – ohne Server, ohne Embeddings.

  python3 tools/search.py "Fahrkosten Auto km" --jur zh --jahr 2025
  python3 tools/search.py "Versicherungsprämien Abzug" --jur bund --jahr 2026 --typ gesetz -n 5
  python3 tools/search.py "Liegenschaftsunterhalt Pauschale" --jur tg,bund --full

Deutsch-spezifisch: Kleinschreibung, Umlaute gefaltet (ä->ae), Zahlen ohne Tausender-Apostroph (7'258 -> 7258),
einfache Endungs-Kürzung und Kompositum-Treffer (Suchwort als Wortteil, z.B. «fahrkosten» in «fahrkostenabzug»).
Für produktive Hybrid-Suche (BM25 + Vektor) siehe README (qmd / OpenClaw memory_search / eigener Index).
"""
from __future__ import annotations
import argparse, json, math, re, collections
from common import ROOT

STOP = set("der die das und oder in im am an auf aus bei bis für fur mit nach von vom zu zum zur ein eine einer eines dem den des ist sind wird werden als auch nicht nur wie wenn so es sie er ab je pro über ueber".split())


def fold(s: str) -> str:
    s = s.lower()
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss"), ("é", "e"), ("è", "e"), ("à", "a")):
        s = s.replace(a, b)
    s = re.sub(r"(?<=\d)['’ ](?=\d{3})", "", s)
    return s


def stem(t: str) -> str:
    for suf in ("ungen", "ung", "en", "er", "es", "e", "n", "s"):
        if len(t) > len(suf) + 3 and t.endswith(suf):
            return t[: -len(suf)]
    return t


def toks(s: str) -> list[str]:
    return [stem(t) for t in re.findall(r"[a-z0-9]+", fold(s)) if t not in STOP]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--jur", help="z.B. zh oder zh,bund")
    ap.add_argument("--jahr", type=int)
    ap.add_argument("--typ")
    ap.add_argument("--quelle", help="Quellen-ID-Präfix")
    ap.add_argument("-n", type=int, default=10)
    ap.add_argument("--full", action="store_true", help="Chunk-Text ausgeben")
    ap.add_argument("--expand", action="store_true", help="Suchbegriffe mit registry/glossar.yaml erweitern (Alltags- ↔ Fachbegriffe)")
    a = ap.parse_args()
    jurs = set(a.jur.split(",")) if a.jur else None
    docs = []
    for line in (ROOT / "index" / "chunks.jsonl").open(encoding="utf-8"):
        r = json.loads(line)
        if jurs and r["jurisdiktion"] not in jurs:
            continue
        if a.jahr and r.get("jahre") and a.jahr not in r["jahre"]:
            continue
        if a.typ and r["typ"] != a.typ:
            continue
        if a.quelle and not r["quelle_id"].startswith(a.quelle):
            continue
        txt = " ".join([r.get("kontext", ""), r.get("titel", ""), " ".join(r.get("stichworte") or []), r["text"]])
        docs.append((r, collections.Counter(toks(txt)), fold(txt)))
    if not docs:
        print("keine Chunks im Filter")
        return
    query = a.query
    if a.expand:
        import yaml
        g = yaml.safe_load((ROOT / "registry" / "glossar.yaml").read_text(encoding="utf-8"))["glossar"]
        fq = fold(query)
        extra = []
        for k, syn in g.items():
            terms = [k] + syn
            if any(fold(t) in fq for t in terms):
                extra += terms
        if extra:
            print("Erweitert um:", ", ".join(dict.fromkeys(extra)))
            query += " " + " ".join(extra)
    q = toks(query)
    N = len(docs)
    avg = sum(sum(c.values()) for _, c, _ in docs) / N
    df = collections.Counter()
    for _, c, _ in docs:
        for t in set(q):
            if c.get(t) or any(t in k for k in c if len(t) >= 5):
                df[t] += 1
    scored = []
    for r, c, ftxt in docs:
        dl = sum(c.values())
        s = 0.0
        for t in q:
            tf = c.get(t, 0)
            if not tf and len(t) >= 5:  # Kompositum: Suchwort als Wortteil
                tf = 0.5 * sum(v for k, v in c.items() if t in k)
            if tf:
                idf = math.log(1 + (N - df[t] + 0.5) / (df[t] + 0.5))
                s += idf * tf * 2.2 / (tf + 1.2 * (0.25 + 0.75 * dl / avg))
        if s > 0:
            scored.append((s, r))
    scored.sort(key=lambda x: -x[0])
    for s, r in scored[: a.n]:
        print(f"{s:6.2f}  {r['id']}  [{r['jurisdiktion']} {r.get('jahre')} {r['typ']}]  {r.get('titel', '')[:80]}")
        print(f"        {r['datei']}")
        if a.full:
            print("        " + r["text"][:1500].replace("\n", "\n        "))
            print()


if __name__ == "__main__":
    main()
