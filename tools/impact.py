#!/usr/bin/env python3
"""Abhängigkeiten und Änderungsauswirkungen im Steuer-Wiki (Quelle → Chunk → Daten-Eintrag → Seite).

Hierarchie (jede Ebene verweist eindeutig auf die darunterliegende):
  Quelle   registry/sources.yaml  id, jur, ordner_jahr, jahre, zeitbezug, gilt_ab/gilt_bis, stand, sha256, raw/…, sources/…
  Chunk    chunks/<jur>/<ordner>/<quelle>/<quelle>__<teil>.md   (Frontmatter: id, quelle, jur, jahre, seiten/artikel)
  Eintrag  data/werte|zuordnung/<jur>/<jahr>.yaml, data/belege-teil*.yaml   (Schlüssel + quellen: [{chunk, zitat}])
  Seite    generiert: quick/*, wiki/<jur>/*-detail.md, wiki/belege/*  (aus data/, build_quick.py)
           handgeschrieben: wiki/themen/*, wiki/<jur>/<jur>-ueberblick.md, wiki/antworten/*  (verlinken Chunks)

  python3 tools/impact.py --quelle zh-wl-2025           # was hängt an dieser Quelle?
  python3 tools/impact.py --chunk zh-wl-2025__c0065     # wer zitiert diesen Chunk?
  python3 tools/impact.py --datei data/werte/zh/2025.yaml   # Quellen eines Datenblatts + generierte Seiten
  python3 tools/impact.py --seite wiki/themen/fahrkosten.md # worauf stützt sich eine Seite?
  python3 tools/impact.py --geaendert                   # lokale Originale mit abweichendem sha256 + Auswirkungen
  python3 tools/impact.py --bau                         # index/abhaengigkeiten.json + reports/abhaengigkeiten.md schreiben
"""
from __future__ import annotations
import argparse, collections, hashlib, json, re
from pathlib import Path
import yaml
from common import ROOT, load_registry, raw_path, today

CHUNK_RE = re.compile(r"\b([a-z0-9][a-z0-9-]*__(?:c\d{4}|art-[0-9a-z-]+|par-[0-9a-z-]+|anhang-[0-9a-z-]+|[a-z0-9-]+))\b")
HAND = ["wiki/themen", "wiki/antworten"]


def load_chunk_index():
    idx = {}
    for line in (ROOT / "index" / "chunks.jsonl").open(encoding="utf-8"):
        r = json.loads(line)
        idx[r["id"]] = {"quelle": r["quelle_id"], "datei": r["datei"], "jahre": r.get("jahre"), "sha": r.get("sha256")}
    return idx


def data_files():
    fs = sorted((ROOT / "data" / "werte").glob("*/*.yaml")) + sorted((ROOT / "data" / "zuordnung").glob("*/*.yaml"))
    fs += sorted((ROOT / "data").glob("belege*.yaml"))
    return fs


def generated_pages(rel: str) -> list[str]:
    """Welche Seiten build_quick.py aus einer Datendatei erzeugt."""
    p = rel.split("/")
    if p[1] == "werte":
        jur, jahr = p[2], p[3][:4]
        out = [f"quick/werte-{jur}-{jahr}.md", f"quick/vergleich-{jahr}.md", f"wiki/{jur}/werte-{jur}-{jahr}-detail.md"]
        kts = [jur] if jur != "bund" else ["ar", "sg", "tg", "zh"]
        for kt in kts:
            for stem in (f"quick/zuordnung-{kt}-{jahr}.md", f"quick/wegleitung-{kt}-{jahr}.md", f"wiki/{kt}/zuordnung-{kt}-{jahr}-detail.md"):
                if (ROOT / stem).exists():
                    out.append(stem)
        return out
    if p[1] == "zuordnung":
        kt, jahr = p[2], p[3][:4]
        out = [f"quick/zuordnung-{kt}-{jahr}.md", f"wiki/{kt}/zuordnung-{kt}-{jahr}-detail.md", "quick/belege-ziffern.md"]
        if (ROOT / f"quick/wegleitung-{kt}-{jahr}.md").exists():
            out.append(f"quick/wegleitung-{kt}-{jahr}.md")
        return out
    return ["quick/belege-relevanz.md", "quick/belege-ziffern.md", "wiki/belege/beleg-<id>.md"]


def build():
    reg = {e["id"]: e for e in load_registry()}
    cidx = load_chunk_index()
    chunk_eintraege = collections.defaultdict(list)   # chunk -> [eintrag-ref]
    eintraege = {}                                    # ref -> info
    for f in data_files():
        rel = str(f.relative_to(ROOT))
        d = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        rows = d.get("werte") or d.get("positionen") or d.get("belege") or []
        for i, r in enumerate(rows):
            key = r.get("key") or r.get("id")
            ref = f"{rel}#{i}:{key}" + (f"@{r['ziffer']}" if r.get("ziffer") else "")
            qs = r.get("quellen") or ([{"chunk": r["quelle"]}] if r.get("quelle") else [])
            cids = [q.get("chunk") for q in qs if q.get("chunk")]
            eintraege[ref] = {"datei": rel, "index": i, "key": key, "ziffer": r.get("ziffer"), "status": r.get("status"),
                              "chunks": cids, "seiten": generated_pages(rel) if "belege" not in rel else
                              ["quick/belege-relevanz.md", "quick/belege-ziffern.md", f"wiki/belege/beleg-{key}.md"]}
            for c in cids:
                chunk_eintraege[c].append(ref)
    chunk_seiten = collections.defaultdict(set)       # chunk -> handgeschriebene Seiten
    seite_chunks = {}
    pages = []
    for base in HAND:
        pages += sorted((ROOT / base).glob("*.md"))
    pages += sorted((ROOT / "wiki").glob("*/*-ueberblick.md"))
    for p in pages:
        rel = str(p.relative_to(ROOT))
        found = {c for c in CHUNK_RE.findall(p.read_text(encoding="utf-8")) if c in cidx}
        seite_chunks[rel] = sorted(found)
        for c in found:
            chunk_seiten[c].add(rel)
    quellen = {}
    for qid, e in reg.items():
        cids = [c for c, v in cidx.items() if v["quelle"] == qid]
        used = [c for c in cids if c in chunk_eintraege or c in chunk_seiten]
        ein = sorted({r for c in cids for r in chunk_eintraege.get(c, [])})
        sei = sorted({s for c in cids for s in chunk_seiten.get(c, [])})
        gen = sorted({s for r in ein for s in eintraege[r]["seiten"]})
        quellen[qid] = {"jur": e["jurisdiktion"], "ordner": str(e["ordner_jahr"]), "jahre": e.get("jahre"),
                        "zeitbezug": e.get("zeitbezug"), "gilt_ab": e.get("gilt_ab"), "gilt_bis": e.get("gilt_bis"),
                        "stand": e.get("stand"), "sha256": (e.get("sha256") or "")[:16], "chunks": len(cids),
                        "chunks_verwendet": len(used), "eintraege": ein, "seiten_hand": sei, "seiten_generiert": gen}
    return {"stand": today(), "quellen": quellen, "eintraege": eintraege,
            "chunks": {c: {"quelle": cidx[c]["quelle"], "datei": cidx[c]["datei"], "eintraege": chunk_eintraege.get(c, []),
                           "seiten_hand": sorted(chunk_seiten.get(c, []))}
                       for c in set(chunk_eintraege) | set(chunk_seiten) if c in cidx},
            "seiten": seite_chunks}


def load_graph():
    p = ROOT / "index" / "abhaengigkeiten.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else build()


def show_quelle(G, qid):
    q = G["quellen"].get(qid)
    if not q:
        print(f"Quelle {qid} unbekannt")
        return
    print(f"Quelle {qid}  [{q['jur']} · Ordner {q['ordner']} · Steuerjahre {q['jahre']} · Zeitbezug {q.get('zeitbezug') or '–'} · "
          f"gilt {q.get('gilt_ab') or '?'} – {q.get('gilt_bis') or 'offen'} · Stand {q.get('stand') or '–'}]")
    print(f"  Chunks: {q['chunks']} (davon zitiert: {q['chunks_verwendet']})")
    print(f"  Daten-Einträge ({len(q['eintraege'])}) – bei Änderung Zitat/Wert prüfen:")
    for r in q["eintraege"]:
        e = G["eintraege"][r]
        print(f"    - {r}  [{e['status']}]")
    print(f"  Generierte Seiten (nach Datenänderung `python3 tools/build_quick.py`): {', '.join(q['seiten_generiert']) or '–'}")
    print(f"  Handgeschriebene Seiten (manuell prüfen): {', '.join(q['seiten_hand']) or '–'}")
    print("  Ablauf bei neuer Fassung: fetch.py --id → convert/laws → (chunkplan prüfen) chunk.py --id → build_index.py →"
          " repair_citations.py → validate_data.py → betroffene Einträge/Seiten oben anpassen → build_quick.py → lint.py → log.md")


def show_chunk(G, cid):
    c = G["chunks"].get(cid)
    if not c:
        print(f"Chunk {cid}: von keinem Daten-Eintrag und keiner handgeschriebenen Seite zitiert")
        return
    print(f"Chunk {cid}  (Quelle {c['quelle']}, Datei {c['datei']})")
    for r in c["eintraege"]:
        print(f"  Eintrag: {r}  [{G['eintraege'][r]['status']}]  → Seiten: {', '.join(G['eintraege'][r]['seiten'])}")
    for s in c["seiten_hand"]:
        print(f"  Seite (hand): {s}")


def show_datei(G, rel):
    es = [v for v in G["eintraege"].values() if v["datei"] == rel]
    if not es:
        print(f"{rel}: keine Einträge")
        return
    qs = collections.Counter(G["chunks"][c]["quelle"] for e in es for c in e["chunks"] if c in G["chunks"])
    print(f"{rel}: {len(es)} Einträge, stützt sich auf {len(qs)} Quellen:")
    for q, n in qs.most_common():
        print(f"  {q}: {n} Zitate")
    print(f"  erzeugt: {', '.join(es[0]['seiten'])}")


def show_seite(G, rel):
    cs = G["seiten"].get(rel)
    if cs is None:
        print(f"{rel}: keine handgeschriebene Seite im Index")
        return
    qs = collections.Counter(G["chunks"][c]["quelle"] for c in cs if c in G["chunks"])
    print(f"{rel}: zitiert {len(cs)} Chunks aus {len(qs)} Quellen")
    for q, n in qs.most_common():
        print(f"  {q}: {n}")


def geaendert(G):
    out = []
    for e in load_registry():
        p = raw_path(e)
        if p.exists() and e.get("sha256"):
            h = hashlib.sha256(p.read_bytes()).hexdigest()
            if h != e["sha256"]:
                out.append(e["id"])
    if not out:
        print("Keine lokalen Originale mit abweichendem sha256 (Neu-Download: python3 tools/fetch.py --id <id>).")
    for q in out:
        show_quelle(G, q)


def write_report(G):
    (ROOT / "index").mkdir(exist_ok=True)
    (ROOT / "index" / "abhaengigkeiten.json").write_text(json.dumps(G, ensure_ascii=False, indent=0), encoding="utf-8")
    L = [f"# Abhängigkeiten Quelle → Daten → Seiten ({G['stand']})", "",
         "> Generiert von `tools/impact.py --bau`. Pro Quelle: wie viele Chunks zitiert werden, welche Daten-Einträge und Seiten "
         "betroffen sind, wenn sich die Quelle ändert. Details: `python3 tools/impact.py --quelle <id>`.", "",
         "| Quelle | Jur | Steuerjahre | Zeitbezug | gilt ab–bis | Chunks (zitiert) | Daten-Einträge | Seiten hand |", "|---|---|---|---|---|---|---|---|"]
    for qid, q in sorted(G["quellen"].items(), key=lambda x: (x[1]["jur"], -len(x[1]["eintraege"]), x[0])):
        if not q["chunks"]:
            continue
        L.append(f"| `{qid}` | {q['jur']} | {', '.join(map(str, q['jahre'] or []))} | {q.get('zeitbezug') or '–'} | "
                 f"{q.get('gilt_ab') or '?'} – {q.get('gilt_bis') or ''} | {q['chunks']} ({q['chunks_verwendet']}) | "
                 f"{len(q['eintraege'])} | {len(q['seiten_hand'])} |")
    (ROOT / "reports" / "abhaengigkeiten.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"index/abhaengigkeiten.json + reports/abhaengigkeiten.md: {len(G['quellen'])} Quellen, "
          f"{len(G['eintraege'])} Einträge, {len(G['chunks'])} zitierte Chunks, {len(G['seiten'])} Hand-Seiten")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quelle")
    ap.add_argument("--chunk")
    ap.add_argument("--datei")
    ap.add_argument("--seite")
    ap.add_argument("--geaendert", action="store_true")
    ap.add_argument("--bau", action="store_true")
    a = ap.parse_args()
    if a.bau:
        write_report(build())
        return
    G = build()
    if a.quelle:
        show_quelle(G, a.quelle)
    if a.chunk:
        show_chunk(G, a.chunk)
    if a.datei:
        show_datei(G, a.datei)
    if a.seite:
        show_seite(G, a.seite)
    if a.geaendert:
        geaendert(G)


if __name__ == "__main__":
    main()
