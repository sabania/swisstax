#!/usr/bin/env python3
"""Revisions-Wiki – Werkzeug für den Revisionsagenten (eingeschränkte Revision, revio 4.0).

  python3 revision/tools/revision.py suche "delkredere pauschal" [--quelle hwp-er-2026] [--typ standard] [--n 8]
  python3 revision/tools/revision.py zeige <chunk-id | pfad>
  (weitere Befehle: siehe main())
"""
from __future__ import annotations
import argparse, json, re, sqlite3, sys
from functools import lru_cache
from pathlib import Path

R = Path(__file__).resolve().parents[1]

STOP = set("""der die das den dem des ein eine einer einem eines und oder aber auch als am an auf aus bei bis da damit dass
durch für fuer gegen hat haben ist sind sein im in ins mit nach nicht noch nur ob ohne so über ueber um von vor wie wird
werden zu zum zur was wer wo welche welcher welches wann muss müssen soll sollen kann können darf dürfen ich du er sie es
wir ihr man sich bzw z b zb etc ja nein gibt gilt beim vom diese dieser dieses jede jeder jedes alle allen""".split())


def cut(s, n):
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def norm(s: str) -> str:
    s = s.lower()
    for a, b in (("ä", "a"), ("ö", "o"), ("ü", "u"), ("ß", "ss"), ("é", "e"), ("è", "e"), ("à", "a")):
        s = s.replace(a, b)
    return s


@lru_cache(maxsize=1)
def fts():
    return sqlite3.connect(R / "index" / "fts.sqlite", check_same_thread=False)


def terms_of(q: str) -> list[str]:
    toks = [t for t in re.findall(r"[a-z0-9]+", norm(q)) if t not in STOP and len(t) > 1]
    out = []
    for t in toks:
        if t not in out:
            out.append(t)
    return out[:12]


def suche(query: str, quelle: str | None = None, typ: str | None = None, n: int = 8) -> str:
    terms = terms_of(query)
    if not terms:
        return "Leere Suchanfrage."
    match = " OR ".join(f'"{t}"*' if len(t) >= 5 else f'"{t}"' for t in terms)
    sql = ("select id, kurz, titel, seiten, rang, snippet(chunks, 9, '«', '»', ' … ', 20), "
           "bm25(chunks, 0,0,0,0,0,0,0, 4.0, 1.5, 1.0) as r from chunks where chunks match ?")
    par: list = [match]
    if quelle:
        sql += " and quelle like ?"
        par.append(quelle.replace("*", "%") + ("%" if "%" not in quelle and "*" not in quelle else ""))
    if typ:
        sql += " and typ = ?"
        par.append(typ)
    sql += " order by r limit ?"
    par.append(max(n * 4, 30))
    try:
        rows = fts().execute(sql, par).fetchall()
    except sqlite3.OperationalError as e:
        return f"Suchfehler: {e}"
    # Treffer, die mehr Suchbegriffe enthalten, und ranghöhere Quellen leicht bevorzugen
    def score(r):
        txt = norm(f"{r[2]} {r[5]}")
        cover = sum(1 for t in terms if t[:5] in txt)
        return r[6] - 2.0 * cover + 0.4 * (r[4] or 5)
    rows = sorted(rows, key=score)[:n]
    if not rows:
        return f"Keine Treffer für «{query}»."
    out = [f"## Suche «{query}»" + (f" · Quelle {quelle}" if quelle else "") + (f" · Typ {typ}" if typ else ""), ""]
    for i, (cid, kurz, titel, seiten, rang, snip, _) in enumerate(rows, 1):
        out.append(f"{i}. **{cid}** · {kurz} · {cut(titel, 80)}" + (f" · S. {seiten}" if seiten else ""))
        out.append(f"   {cut(snip, 260)}")
    out.append("\nVolltext: `revision zeige <chunk-id>`.")
    return "\n".join(out)


@lru_cache(maxsize=1)
def chunk_files() -> dict:
    return {p.stem: p for p in (R / "chunks").glob("*/*.md")}


def zeige(ref: str, abschnitt: str | None = None) -> str:
    ref = ref.strip()
    p = chunk_files().get(ref)
    if not p:
        cand = R / ref if not ref.startswith("revision/") else R.parent / ref
        if cand.exists():
            p = cand
    if not p:
        near = [k for k in chunk_files() if k.startswith(ref.split("__")[0] + "__") and ref.split("__")[-1][:6] in k][:8]
        return f"Nicht gefunden: {ref}." + (f" Ähnlich: {', '.join(near)}" if near else " Chunk-Id aus `suche` verwenden.")
    t = p.read_text(encoding="utf-8")
    if abschnitt:
        parts = re.split(r"(?m)^(?=#{1,4} )", t)
        hit = [x for x in parts if norm(abschnitt) in norm(x.split("\n", 1)[0])]
        if hit:
            t = "\n".join(hit)
    return f"# {p.stem if p.suffix == '.md' else ref}\nDatei: {p.relative_to(R.parent)}\n\n" + t


def _flat(t: str) -> str:
    t = t.replace("\u00ad", "").replace("\x08", "").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = t.replace("«", '"').replace("»", '"').replace("–", "-").replace("—", "-").replace("\u2002", " ")
    return re.sub(r"\s+", " ", t).strip()


def zitat_ok(text: str, zitat: str) -> bool:
    """Zitat wörtlich im Chunk? (Leerraum, Silbentrennung am Zeilenende, Anführungszeichen ausgeglichen)"""
    a, z = _flat(text), _flat(zitat)
    if not z:
        return False
    if z in a:
        return True
    a2 = re.sub(r"(\w)- (\w)", r"\1\2", a)
    z2 = re.sub(r"(\w)- (\w)", r"\1\2", z)
    return z2 in a2 or z in a2 or z2 in a


@lru_cache(maxsize=None)
def chunk_text(cid: str) -> str | None:
    p = chunk_files().get(cid)
    if not p:
        return None
    t = p.read_text(encoding="utf-8").split("---\n", 2)[-1]
    return t


def pruefe_zitat(cid: str, zitat: str) -> str:
    t = chunk_text(cid)
    if t is None:
        return f"FEHLT: Chunk {cid} existiert nicht."
    return "OK" if zitat_ok(t, zitat) else f"NICHT GEFUNDEN in {cid}: «{cut(zitat, 120)}»"


def main(argv=None):
    ap = argparse.ArgumentParser(prog="revision")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("suche"); s.add_argument("query"); s.add_argument("--quelle"); s.add_argument("--typ"); s.add_argument("--n", type=int, default=8)
    z = sub.add_parser("zeige"); z.add_argument("ref"); z.add_argument("--abschnitt")
    pz = sub.add_parser("pruefe-zitat"); pz.add_argument("chunk"); pz.add_argument("zitat")
    a = ap.parse_args(argv)
    if a.cmd == "suche":
        print(suche(a.query, a.quelle, a.typ, a.n))
    elif a.cmd == "zeige":
        print(zeige(a.ref, a.abschnitt))
    elif a.cmd == "pruefe-zitat":
        print(pruefe_zitat(a.chunk, a.zitat))


if __name__ == "__main__":
    main()
