#!/usr/bin/env python3
"""Erzeugt RAG-Chunks: chunks/<jur>/<jahr>/<quelle-id>/<quelle-id>__cNNNN.md (+ index/chunks.jsonl via build_index.py)

Strategien (automatisch gewählt):
  1. law      : strukturierte Gesetze (sources/.../<id>.articles.json aus tools/laws.py) -> 1 Chunk pro Artikel/§
                Chunk-ID strukturell und stabil: <id>__art-33, <id>__par-31
  2. plan     : semantischer Chunk-Plan eines Agenten (registry/chunkplans/<id>.json) -> Schnitt an Zeilennummern,
                Text bleibt verbatim
  3. headings : Markdown-Überschriften (HTML-Quellen), kleine Abschnitte zusammengefasst, grosse an Absätzen geteilt
  4. pages    : Fallback für PDFs ohne Plan: Seitenweise, an Absätzen auf Zielgrösse geteilt

  python3 tools/chunk.py              # alle Quellen mit verarbeitung=chunk
  python3 tools/chunk.py --id zh-wl-2025
"""
from __future__ import annotations
import argparse, json, re, shutil
from common import (load_registry, source_path, chunk_dir, read_frontmatter, frontmatter, slugify,
                    JUR_LABEL, JUR_SHORT, TYP_LABEL, ROOT)

# Grössen in Tokens (≈ Zeichen/4). OpenClaw zerlegt jede .md-Datei selbst in ~400 Tokens (~1'600 Zeichen):
# Chunk-Dateien (Frontmatter + Kontextzeile + Text) bleiben darunter, damit 1 Datei = 1 Such-Treffer.
TARGET = 250      # Zieltext ~1'000 Zeichen
MAXTOK = 330      # Text max. ~1'320 Zeichen
MINTOK = 40
PLANS = ROOT / "registry" / "chunkplans"


def ntok(s: str) -> int:
    return max(1, len(s) // 4)


def body_lines(e):
    fm, body = read_frontmatter(source_path(e).read_text(encoding="utf-8"))
    return fm, body.splitlines()


def page_at(lines: list[str], idx: int) -> int | None:
    for i in range(min(idx, len(lines) - 1), -1, -1):
        m = re.match(r"<!-- Seite (\d+)", lines[i])
        if m:
            return int(m.group(1))
    return None


def pages_in(lines, a, b):
    p0 = page_at(lines, a)
    ps = [int(m.group(1)) for l in lines[a:b] for m in [re.match(r"<!-- Seite (\d+)", l)] if m]
    allp = ([p0] if p0 else []) + ps
    return sorted(set(allp)) if allp else []


def split_paragraphs(text: str, target=TARGET, maxtok=MAXTOK) -> list[str]:
    """teilt an Leerzeilen; Tabellenblöcke (Zeilen mit |) bleiben zusammen"""
    if ntok(text) <= maxtok:
        return [text]
    paras = re.split(r"\n\s*\n", text)
    out, cur = [], ""
    for p in paras:
        if cur and ntok(cur) + ntok(p) > target and not (p.lstrip().startswith("|") and cur.rstrip().endswith("|")):
            out.append(cur)
            cur = p
        else:
            cur = (cur + "\n\n" + p) if cur else p
    if cur:
        out.append(cur)
    # einzelne Riesenabsätze hart an Zeilen teilen
    res = []
    for c in out:
        if ntok(c) <= maxtok:
            res.append(c)
            continue
        buf = ""
        for line in c.splitlines():
            if buf and ntok(buf) + ntok(line) > target:
                res.append(buf)
                buf = line
            else:
                buf = (buf + "\n" + line) if buf else line
        if buf:
            res.append(buf)
    # sehr kleine Teile (z.B. nur Überschrift) mit dem Nachfolger zusammenführen
    merged = []
    for c in res:
        if merged and ntok(merged[-1]) < MINTOK * 2 and ntok(merged[-1]) + ntok(c) <= maxtok * 1.15:
            merged[-1] = merged[-1] + "\n\n" + c
        else:
            merged.append(c)
    # sehr kleiner Rest am Ende an den Vorgänger anhängen
    if len(merged) > 1 and ntok(merged[-1]) < MINTOK * 2 and ntok(merged[-2]) + ntok(merged[-1]) <= maxtok * 1.15:
        merged[-2] = merged[-2] + "\n\n" + merged.pop()
    return merged


def fmt_pages(seiten):
    if not seiten:
        return None
    return str(seiten[0]) if len(seiten) == 1 else f"{seiten[0]}-{seiten[-1]}"


def yq(v: str) -> str:
    """YAML-sicherer Skalar (immer in Anführungszeichen)"""
    return '"' + str(v).replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_chunks(e: dict, fm_src: dict, items: list[dict]) -> int:
    """Schreibt Chunk-Dateien mit schlanker Frontmatter (wird von OpenClaw/BM25 als Text mitindexiert).
    Vollständige Metadaten stehen in index/chunks.jsonl (tools/build_index.py)."""
    d = chunk_dir(e)
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True, exist_ok=True)
    ids = [it["id"] for it in items]
    jahre = e.get("jahre") or []
    jstr = "[" + ", ".join(map(str, jahre)) + "]"
    meta_all = []
    for n, it in enumerate(items):
        pfad = it.get("pfad") or []
        seiten = it.get("seiten") or []
        sp = fmt_pages(seiten)
        crumb = " · ".join(x for x in [
            JUR_SHORT[e["jurisdiktion"]], ("Steuerjahr " + "/".join(map(str, jahre))) if jahre else None,
            e.get("kurz") or e["titel"], " › ".join(pfad[-3:]) if pfad else None,
            ("S. " + sp.replace("-", "–")) if sp else None] if x)
        titel = it.get("titel") or (pfad[-1] if pfad else e["titel"])
        lines = ["---", f"id: {it['id']}", f"quelle: {e['id']}", f"jur: {e['jurisdiktion']}", f"jahre: {jstr}",
                 f"typ: {e['typ']}", f"titel: {yq(titel)}"]
        if it.get("artikel"):
            lines.append(f"artikel: {yq(it['artikel'])}")
        if it.get("ziffer"):
            lines.append(f"ziffer: {yq(it['ziffer'])}")
        if sp:
            lines.append(f"seiten: {yq(sp)}")
        lines.append(f"qmd: {{metadata: {{jur: {e['jurisdiktion']}, jahre: {jstr}, typ: {e['typ']}}}}}")
        lines.append("---")
        text = it["text"].strip("\n")
        (d / f"{it['id']}.md").write_text("\n".join(lines) + "\n" + f"> {crumb}\n\n" + text + "\n", encoding="utf-8")
        meta_all.append({"id": it["id"], "titel": titel, "pfad": pfad, "seiten": seiten, "artikel": it.get("artikel"),
                         "ziffer": it.get("ziffer"), "stichworte": it.get("stichworte"), "positionen": it.get("positionen"),
                         "zusammenfassung": it.get("zusammenfassung"), "chunking": it.get("chunking"),
                         "vorher": ids[n - 1] if n > 0 else None, "nachher": ids[n + 1] if n + 1 < len(ids) else None})
    (d / "_meta.json").write_text(json.dumps(meta_all, ensure_ascii=False, indent=0), encoding="utf-8")
    return len(items)


# ---------------------------------------------------------------- Strategien
def strat_law(e, fm, arts_path):
    arts = json.loads(arts_path.read_text(encoding="utf-8"))
    items = []
    for a in arts:
        parts = split_paragraphs(a["text"])
        for k, t in enumerate(parts):
            cid = f"{e['id']}__{a['key']}" + (f"-t{k + 1}" if len(parts) > 1 else "")
            items.append(dict(id=cid, titel=a.get("titel") + (f" (Teil {k + 1}/{len(parts)})" if len(parts) > 1 else ""),
                              pfad=a.get("pfad"), artikel=a.get("label"), seiten=a.get("seiten"),
                              text=t if k == 0 else f"### {a.get('titel')} (Fortsetzung)\n\n{t}", chunking="gesetz (Artikel)"))
    return items


def plan_items(e, full_lines, plan):
    """Plan-Zeilennummern beziehen sich auf die VOLLSTÄNDIGE Datei sources/.../<id>.md (1-basiert, wie Read/cat -n)."""
    starts = [c["start"] for c in plan["chunks"]] + [len(full_lines) + 1]
    items, n = [], 0
    for i, c in enumerate(plan["chunks"]):
        a, b = c["start"] - 1, starts[i + 1] - 1
        if c.get("skip"):
            continue
        seg = "\n".join(l for l in full_lines[a:b] if not l.startswith("<!-- Seite ")).strip("\n")
        if not seg.strip():
            continue
        parts = split_paragraphs(seg)
        for k, t in enumerate(parts):
            n += 1
            items.append(dict(id=f"{e['id']}__c{n:04d}", titel=c.get("titel", "") + (f" (Teil {k + 1}/{len(parts)})" if len(parts) > 1 else ""),
                              pfad=c.get("pfad"), ziffer=c.get("ziffer"), seiten=pages_in(full_lines, a, b),
                              stichworte=c.get("stichworte"), positionen=c.get("positionen"),
                              zusammenfassung=c.get("zusammenfassung") if k == 0 else None, text=t, chunking="semantisch (Agent-Plan)"))
    return items


def strat_plan(e, fm, lines, plan):
    full = source_path(e).read_text(encoding="utf-8").splitlines()
    return plan_items(e, full, plan)


def strat_headings(e, fm, lines):
    # Abschnitte an Markdown-Überschriften (#..####)
    secs, cur, stack = [], {"pfad": [], "lines": []}, []
    for i, l in enumerate(lines):
        m = re.match(r"^(#{1,4})\s+(.*\S)\s*$", l)
        if m:
            if cur["lines"]:
                secs.append(cur)
            lvl, title = len(m.group(1)), m.group(2).strip("# ")
            stack = [s for s in stack if s[0] < lvl] + [(lvl, title)]
            cur = {"pfad": [s[1] for s in stack], "lines": [l], "start": i}
        else:
            cur["lines"].append(l)
    if cur["lines"]:
        secs.append(cur)
    # kleine Abschnitte mit Nachfolger zusammenführen
    merged, carry = [], ""
    for s in secs:
        txt = "\n".join(s["lines"]).strip()
        if not txt or re.fullmatch(r"(#+\s*)+", txt):
            continue
        if carry:
            txt, carry = carry + "\n\n" + txt, ""
        if ntok(txt) < MINTOK:          # zu klein (z.B. nur Überschrift): an nächsten Abschnitt anhängen
            carry = txt
            continue
        if merged and ntok(merged[-1]["text"]) < MINTOK * 2 and ntok(merged[-1]["text"]) + ntok(txt) < TARGET * 1.5:
            merged[-1]["text"] += "\n\n" + txt
            continue
        merged.append({"pfad": s["pfad"], "text": txt})
    if carry:
        if merged:
            merged[-1]["text"] += "\n\n" + carry
        else:
            merged.append({"pfad": [], "text": carry})
    items, n = [], 0
    for s in merged:
        for k, t in enumerate(split_paragraphs(s["text"])):
            n += 1
            items.append(dict(id=f"{e['id']}__c{n:04d}", pfad=s["pfad"], titel=(s["pfad"][-1] if s["pfad"] else e["titel"]),
                              text=t, chunking="überschriften"))
    return items


def strat_pages(e, fm, lines):
    text = "\n".join(lines)
    blocks = re.split(r"(?=<!-- Seite \d+)", text)
    items, n, buf, bufpages = [], 0, "", []

    def flush():
        nonlocal n, buf, bufpages
        if buf.strip():
            for t in split_paragraphs(buf):
                n += 1
                items.append(dict(id=f"{e['id']}__c{n:04d}", seiten=sorted(set(bufpages)), titel=f"{e.get('kurz') or e['titel']} – Abschnitt {n}",
                                  text=t, chunking="seiten (Fallback)"))
        buf, bufpages = "", []
    for b in blocks:
        m = re.match(r"<!-- Seite (\d+)", b)
        p = int(m.group(1)) if m else None
        if buf and ntok(buf) + ntok(b) > TARGET * 1.6:
            flush()
        buf += b
        if p:
            bufpages.append(p)
    flush()
    return items


def chunk(e: dict) -> tuple[int, str]:
    sp = source_path(e)
    arts = sp.with_suffix(".articles.json")
    if arts.exists():
        fm, _ = read_frontmatter(sp.read_text(encoding="utf-8")) if sp.exists() else ({}, "")
        return write_chunks(e, fm, strat_law(e, fm, arts)), "law"
    if not sp.exists():
        return 0, "keine Quelle"
    fm, lines = body_lines(e)
    plan_p = PLANS / f"{e['id']}.json"
    if plan_p.exists():
        return write_chunks(e, fm, strat_plan(e, fm, lines, json.loads(plan_p.read_text(encoding="utf-8")))), "plan"
    if e.get("format") == "html":
        return write_chunks(e, fm, strat_headings(e, fm, lines)), "headings"
    return write_chunks(e, fm, strat_pages(e, fm, lines)), "pages"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", action="append")
    a = ap.parse_args()
    tot, stats = 0, {}
    for e in load_registry():
        if a.id and e["id"] not in a.id:
            continue
        if e.get("verarbeitung") != "chunk" or e.get("same_as"):
            continue
        n, how = chunk(e)
        tot += n
        stats[how] = stats.get(how, 0) + 1
    print(f"{tot} Chunks erzeugt; Strategien: {stats}")


if __name__ == "__main__":
    main()
