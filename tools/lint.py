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
        if not source_path(e).exists() and not e.get("same_as") and e.get("verarbeitung") != "original":
            errors.append(f"R2 {e['id']}: Volltext sources/ fehlt")
        if e.get("verarbeitung") == "chunk" and not e.get("same_as"):
            d = chunk_dir(e)
            files = list(d.glob("*.md")) if d.exists() else []
            if not files:
                errors.append(f"R2 {e['id']}: keine Chunks")
            big = [f.name for f in files if f.stat().st_size > 1800]
            if big:
                warnings.append(f"R2 {e['id']}: {len(big)} Chunk-Dateien > 1'800 Bytes (OpenClaw teilt sie), z.B. {big[0]}")


def check_integrity(reg):
    """R4: Chunks aus Agent-Plänen enthalten den Quelltext vollständig und unverändert (verbatim-Garantie)."""
    import json as _j
    plans = ROOT / "registry" / "chunkplans"
    for e in reg:
        pp = plans / f"{e['id']}.json"
        d = chunk_dir(e)
        if not pp.exists() or not d.exists() or e.get("strukturiert"):
            continue
        plan = _j.loads(pp.read_text(encoding="utf-8"))
        full = source_path(e).read_text(encoding="utf-8").splitlines()
        import chunk as _ch
        starts = _ch.plan_starts(plan, full) + [len(full) + 1]
        src = []
        for i, c in enumerate(plan["chunks"]):
            if c.get("skip"):
                continue
            src += [l for l in full[starts[i] - 1:starts[i + 1] - 1] if not l.startswith("<!-- Seite ")]
        want = re.sub(r"\s+", "", "".join(src))
        got = []
        for f in sorted(d.glob("*.md")):
            fm, body = read_frontmatter(f.read_text(encoding="utf-8"))
            parts = body.split("\n", 2)
            got.append(parts[2] if len(parts) > 2 and parts[0].startswith("> ") else body)
        have = re.sub(r"\s+", "", "".join(got))
        if want != have:
            errors.append(f"R4 {e['id']}: Chunk-Text weicht vom Quelltext ab (Plan/Chunks neu erzeugen: tools/chunk.py --id {e['id']})")


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
    bkeys = set(tax["belege"])
    global OFFEN
    OFFEN = collections.defaultdict(list)
    for kind, keyset in (("werte", wkeys), ("zuordnung", pkeys), ("belege", bkeys)):
        files = sorted((ROOT / "data" / kind).glob("*/*.yaml")) if kind != "belege" else sorted((ROOT / "data").glob("belege*.yaml"))
        for f in files:
            d = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
            jahr = d.get("jahr")
            rows = d.get(kind) or d.get("positionen") or []
            for r in rows:
                where = f"{f.relative_to(ROOT)}:{r.get('key') or r.get('ziffer') or r.get('id')}"
                st = r.get("status", "offen")
                stats[(kind, st)] += 1
                if st in ("strittig", "offen", "extrahiert"):
                    OFFEN[st].append((str(f.relative_to(ROOT)), r.get("key") or r.get("id"), r.get("ziffer"),
                                      (r.get("bemerkung") or r.get("hinweis") or "").strip()))
                k = r.get("key") if kind != "belege" else r.get("id")
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
                    if jahr and src and "jahre" in src and int(jahr) not in (src.get("jahre") or []) and not q.get("jahr_ok"):
                        warnings.append(f"D1 {where}: Jahres-Wache – Quelle {c['quelle_id']} gilt für {src['jahre']}, Wert für {jahr}")
    return stats


LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def check_links():
    targets = [ROOT / "index.md", ROOT / "README.md", ROOT / "AGENTS.md"] + list((ROOT / "quick").rglob("*.md")) + list((ROOT / "wiki").rglob("*.md")) + list((ROOT / "skills").rglob("*.md"))
    n = 0
    for p in targets:
        if not p.exists():
            continue
        txt = re.sub(r"```.*?```", "", p.read_text(encoding="utf-8"), flags=re.S)
        txt = re.sub(r"`[^`\n]*`", "", txt)  # Code-Beispiele ignorieren
        for m in LINK.finditer(txt):
            href = m.group(1).split("#")[0]
            if not href or re.match(r"^[a-z]+:", href):
                continue
            n += 1
            if not (p.parent / href).resolve().exists():
                errors.append(f"L1 {p.relative_to(ROOT)}: Link nicht auflösbar: {href}")
    return n


OFFEN = {}


def write_offen(stats):
    """reports/offene-punkte.md: Arbeitsliste für die Fachperson (strittig > extrahiert > offen)."""
    L = [f"# Offene Punkte für die Fachperson ({today()})", "",
         "> Generiert von `tools/lint.py` aus `data/`. **strittig** = Quellen widersprechen sich → Fachperson entscheidet und "
         "setzt den Status (`verifiziert` nur durch Menschen). **extrahiert** = Wert mit Zitat, aber ohne zweite Prüfung. "
         "**offen** = Wert fehlt (Quelle des Jahres noch nicht publiziert oder nicht im Wiki).", ""]
    for st, title in (("strittig", "Strittig – Entscheid nötig"), ("extrahiert", "Extrahiert – Zweitprüfung empfohlen"),
                      ("offen", "Offen – Wert fehlt")):
        rows = OFFEN.get(st, [])
        L += [f"## {title} ({len(rows)})", ""]
        if st == "offen":
            by = collections.defaultdict(list)
            for f, k, z, _ in rows:
                by[f].append(f"{k}" + (f" (Ziff. {z})" if z else ""))
            for f in sorted(by):
                L.append(f"- `{f}`: " + ", ".join(by[f]))
        else:
            L += ["| Datei | Schlüssel | Ziffer | Bemerkung |", "|---|---|---|---|"]
            for f, k, z, b in rows:
                b = re.sub(r"\s+", " ", b).replace("|", "/")
                L.append(f"| `{f}` | {k} | {z or ''} | {b[:400]}{'…' if len(b) > 400 else ''} |")
        L.append("")
    (ROOT / "reports" / "offene-punkte.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def main():
    reg = load_registry()
    cidx = chunk_index()
    check_registry(reg)
    check_integrity(reg)
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
    write_offen(stats)
    print(f"Fehler: {len(errors)}, Warnungen: {len(warnings)} -> reports/lint.md")
    for x in errors[:30]:
        print("  ", x)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
