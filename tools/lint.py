#!/usr/bin/env python3
"""Deterministische Qualitätsprüfung des Steuer-Wikis -> reports/lint.md (Exit-Code 1 bei Fehlern).

Prüft:
  R1 Registry: eindeutige IDs, Pflichtfelder, Original vorhanden, sha256 = Datei (Hash-Drift)
  R2 Volltext (sources/) und Chunks vorhanden, Chunk-Dateigrösse (OpenClaw ~1'600 Zeichen)
  R3 Keine Dateinamen mit Datumspräfix YYYY-MM-DD (OpenClaw-Recency-Decay)
  D1 data/werte + data/zuordnung: Schlüssel in taxonomy.yaml, zitierter Chunk existiert,
     ZITAT steht wörtlich im Chunk (normalisiert: Leerraum, Apostrophe, Striche), Jahres-Wache
  L1 Relative Markdown-Links in quick/, wiki/, index.md, README.md, AGENTS.md auflösbar

  python3 tools/lint.py
"""
from __future__ import annotations
import re, sys, json, hashlib, collections, yaml
from common import load_registry, source_path, chunk_dir, raw_path, ROOT, read_frontmatter, today

errors, warnings = [], []


def norm(s: str) -> str:
    s = s.replace(" ", " ").replace(" ", " ").replace(" ", " ").replace("­", "")
    s = re.sub("[’‘´ʼ`]", "'", s)
    s = re.sub("[–—‑‐]", "-", s)
    s = s.replace("“", '"').replace("”", '"').replace("«", '"').replace("»", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


def chunk_index():
    idx = {}
    p = ROOT / "index" / "chunks.jsonl"
    if p.exists():
        for line in p.open(encoding="utf-8"):
            r = json.loads(line)
            idx[r["id"]] = r
    return idx


def check_registry(reg):
    ids = collections.Counter(e["id"] for e in reg)
    for i, n in ids.items():
        if n > 1:
            errors.append(f"R1 doppelte Quellen-ID: {i}")
    for e in reg:
        for k in ("id", "jurisdiktion", "ordner_jahr", "typ", "titel", "url", "verarbeitung"):
            if not e.get(k):
                errors.append(f"R1 {e.get('id')}: Pflichtfeld {k} fehlt")
        if e.get("verarbeitung") == "link" or e.get("format") == "zip":
            continue
        rp = raw_path(e)
        if not rp.exists():
            errors.append(f"R1 {e['id']}: Original fehlt ({rp.relative_to(ROOT)})")
            continue
        if e.get("sha256") and hashlib.sha256(rp.read_bytes()).hexdigest() != e["sha256"]:
            errors.append(f"R1 {e['id']}: sha256 weicht ab (Original geändert -> neu konvertieren/prüfen)")
        if not source_path(e).exists() and not e.get("same_as"):
            errors.append(f"R2 {e['id']}: Volltext sources/ fehlt")
        if e.get("verarbeitung") == "chunk" and not e.get("same_as"):
            d = chunk_dir(e)
            files = list(d.glob("*.md")) if d.exists() else []
            if not files:
                errors.append(f"R2 {e['id']}: keine Chunks")
            big = [f.name for f in files if f.stat().st_size > 1800]
            if big:
                warnings.append(f"R2 {e['id']}: {len(big)} Chunk-Dateien > 1'800 Bytes (OpenClaw teilt sie), z.B. {big[0]}")


def check_filenames():
    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts:
            continue
        if re.match(r"\d{4}-\d{2}-\d{2}", p.name):
            errors.append(f"R3 Dateiname mit Datumspräfix (OpenClaw-Decay): {p.relative_to(ROOT)}")


def check_data(reg, cidx):
    tax = yaml.safe_load((ROOT / "registry" / "taxonomy.yaml").read_text(encoding="utf-8"))
    wkeys, pkeys = set(tax["werte"]), set(tax["positionen"])
    regby = {e["id"]: e for e in reg}
    stats = collections.Counter()
    for kind, keyset in (("werte", wkeys), ("zuordnung", pkeys)):
        for f in sorted((ROOT / "data" / kind).glob("*/*.yaml")):
            d = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
            jahr = d.get("jahr")
            rows = d.get(kind) or d.get("positionen") or []
            for r in rows:
                where = f"{f.relative_to(ROOT)}:{r.get('key') or r.get('ziffer')}"
                st = r.get("status", "offen")
                stats[(kind, st)] += 1
                k = r.get("key")
                if k and k not in keyset:
                    errors.append(f"D1 {where}: Schlüssel nicht in taxonomy.yaml")
                if st in ("offen", "na"):
                    continue
                refs = r.get("quellen") or ([{"chunk": r.get("quelle"), "zitat": r.get("zitat")}] if r.get("quelle") else [])
                if not refs:
                    errors.append(f"D1 {where}: Status {st} ohne Quelle")
                for q in refs:
                    cid, zitat = q.get("chunk"), q.get("zitat")
                    c = cidx.get(cid)
                    if not c:
                        errors.append(f"D1 {where}: zitierter Chunk {cid} existiert nicht")
                        continue
                    if not zitat:
                        warnings.append(f"D1 {where}: kein wörtliches Zitat")
                    elif norm(zitat) not in norm(c["text"]):
                        errors.append(f"D1 {where}: Zitat nicht im Chunk {cid} gefunden: «{zitat[:80]}»")
                    src = regby.get(c["quelle_id"], {})
                    if jahr and src.get("jahre") and int(jahr) not in src["jahre"] and not q.get("jahr_ok"):
                        warnings.append(f"D1 {where}: Jahres-Wache – Quelle {c['quelle_id']} gilt für {src['jahre']}, Wert für {jahr}")
    return stats


LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def check_links():
    targets = [ROOT / "index.md", ROOT / "README.md", ROOT / "AGENTS.md"] + list((ROOT / "quick").rglob("*.md")) + list((ROOT / "wiki").rglob("*.md")) + list((ROOT / "skills").rglob("*.md"))
    n = 0
    for p in targets:
        if not p.exists():
            continue
        for m in LINK.finditer(p.read_text(encoding="utf-8")):
            href = m.group(1).split("#")[0]
            if not href or re.match(r"^[a-z]+:", href):
                continue
            n += 1
            if not (p.parent / href).resolve().exists():
                errors.append(f"L1 {p.relative_to(ROOT)}: Link nicht auflösbar: {href}")
    return n


def main():
    reg = load_registry()
    cidx = chunk_index()
    check_registry(reg)
    check_filenames()
    stats = check_data(reg, cidx)
    nlinks = check_links()
    out = ROOT / "reports" / "lint.md"
    out.parent.mkdir(exist_ok=True)
    L = [f"# Lint-Bericht ({today()})", "", f"- Quellen: {len(reg)} · Chunks: {len(cidx)} · geprüfte Links: {nlinks}",
         f"- Fehler: {len(errors)} · Warnungen: {len(warnings)}", "", "## Status der Daten (Werte/Zuordnungen)", ""]
    for (k, st), n in sorted(stats.items()):
        L.append(f"- {k} · {st}: {n}")
    L += ["", "## Fehler", ""] + [f"- {x}" for x in errors] + ["", "## Warnungen", ""] + [f"- {x}" for x in warnings]
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"Fehler: {len(errors)}, Warnungen: {len(warnings)} -> reports/lint.md")
    for x in errors[:30]:
        print("  ", x)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
