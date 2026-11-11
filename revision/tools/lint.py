#!/usr/bin/env python3
"""Revisions-Wiki: deterministische Prüfung → reports/lint.md (Exit 1 bei Fehlern).

  python3 revision/tools/lint.py

Prüft: Zitate in data/ (wörtlich im Chunk), Schritt-Ids gegen Katalog, Prüffeld-Codes, revio-Werkzeugnamen gegen die
Werkzeugliste, Links in quick/ und wiki/, Dateinamen (kebab-case, ASCII, kein Datumspräfix), Hash der Originale (raw/).
"""
from __future__ import annotations
import csv, hashlib, re, sys
from pathlib import Path
import yaml

R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R / "tools"))
import revision as rv  # noqa: E402

ERR: list[str] = []
WARN: list[str] = []
N = {"zitate": 0, "links": 0, "dateien": 0}


def walk(o, path=""):
    if isinstance(o, dict):
        if "zitat" in o and ("quelle" in o or "chunk" in o):
            yield path, o.get("quelle") or o.get("chunk"), o.get("zitat")
        for k, v in o.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, f"{path}[{i}]")


def zitate():
    files = list((R / "data").rglob("*.yaml")) + list((R / "eval").glob("*/*.yaml"))
    for p in files:
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        for path, cid, z in walk(d):
            if not cid and not z:
                continue
            N["zitate"] += 1
            if not cid or not z:
                ERR.append(f"{p.relative_to(R)}{path}: quelle/zitat unvollständig")
                continue
            t = rv.chunk_text(cid)
            if t is None:
                ERR.append(f"{p.relative_to(R)}{path}: Chunk fehlt {cid}")
            elif not rv.zitat_ok(t, z):
                ERR.append(f"{p.relative_to(R)}{path}: Zitat nicht im Chunk {cid}: «{rv.cut(z, 80)}»")


def katalog():
    kat = yaml.safe_load((R / "data" / "katalog.yaml").read_text(encoding="utf-8"))
    ids = {s["id"] for s in kat["schritte"]}
    codes = {p["code"] for p in kat["prueffelder"]}
    for p in (R / "data" / "prueffelder").glob("*.yaml"):
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        if d["code"] not in codes:
            ERR.append(f"{p.name}: unbekannter Code {d['code']}")
        mine = {s["id"] for s in kat["schritte"] if s["prueffeld"] == d["code"]}
        have = {s["id"] for s in d.get("schritte") or []}
        if have - ids:
            ERR.append(f"{p.name}: unbekannte Schritte {sorted(have - ids)}")
        if mine - have:
            WARN.append(f"{p.name}: {len(mine - have)} Schritte ohne Detailwissen: {sorted(mine - have)[:8]}")
        for s in d.get("schritte") or []:
            if not s.get("fundstellen"):
                WARN.append(f"{p.name}: {s['id']} ohne Fundstelle")
    for p in (R / "data" / "prozess").glob("*.yaml"):
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        bad = [c for c in d.get("prueffelder") or [] if c not in codes]
        if bad:
            ERR.append(f"{p.name}: unbekannte Prüffelder {bad}")


def werkzeuge():
    raw = R / "raw" / "revio" / "revio-mcp-werkzeuge.csv"
    if not raw.exists():
        return
    wz = {r["werkzeug"] for r in csv.DictReader(raw.open(encoding="utf-8-sig"), delimiter=";")}
    wz |= {l.split("`")[1] for l in (R / "raw" / "revio" / "revio-mcp-werkzeuge.md").read_text(encoding="utf-8").splitlines() if l.startswith("| `revio_")}
    for p in (R / "data" / "revio").glob("*.yaml"):
        txt = p.read_text(encoding="utf-8")
        for n in set(re.findall(r"\b(rv_[A-Za-z0-9_]+|revio_[a-z_]+)\b", txt)):
            if n in ("revio_template_id", "revio_activity_id", "revio_bereich"):   # Spaltennamen der Vorlage, keine Werkzeuge
                continue
            if n not in wz:
                ERR.append(f"{p.relative_to(R)}: unbekanntes Werkzeug {n}")
    kl = R / "data" / "revio" / "werkzeuge.csv"
    if kl.exists():
        rows = list(csv.DictReader(kl.open(encoding="utf-8-sig"), delimiter=";"))
        names = {r["werkzeug"] for r in rows}
        if wz - names:
            ERR.append(f"werkzeuge.csv: {len(wz - names)} Werkzeuge nicht klassifiziert, z.B. {sorted(wz - names)[:5]}")
        art = {r["werkzeug"]: r.get("art") for r in rows}
        for n, a in art.items():
            if re.search(r"(?i)seal|visa|approve|archive|delete|remove|closedstate|lock", n) and a in ("lesen", "vorbereiten") and not n.startswith("rv_get_"):
                WARN.append(f"werkzeuge.csv: {n} als {a} – Sperre prüfen")
        if art.get("revio_call") not in ("gesperrt", "nur_mensch"):
            ERR.append("werkzeuge.csv: revio_call (generischer Aufruf) muss gesperrt sein – umgeht die Sperre je Werkzeug")


def links():
    for p in list((R / "quick").glob("*.md")) + list((R / "wiki").rglob("*.md")):
        N["dateien"] += 1
        name = p.stem
        if re.match(r"^\d{4}-\d{2}-\d{2}", name) or not re.match(r"^[a-z0-9-]+$", name):
            ERR.append(f"Dateiname nicht kebab-case/ASCII oder mit Datum: {p.relative_to(R)}")
        t = p.read_text(encoding="utf-8")
        if not t.startswith("---\n"):
            WARN.append(f"{p.relative_to(R)}: ohne Frontmatter")
        for m in re.finditer(r"\]\(([^)#\s]+)(#[^)]*)?\)", t):
            href = m.group(1)
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            N["links"] += 1
            if not (p.parent / href).resolve().exists():
                ERR.append(f"{p.relative_to(R)}: toter Link {href}")


def hashes():
    reg = yaml.safe_load((R / "registry" / "sources.yaml").read_text(encoding="utf-8"))
    for e in reg:
        p = R / (e.get("raw") or "")
        if e.get("raw") and p.exists() and e.get("sha256"):
            if hashlib.sha256(p.read_bytes()).hexdigest() != e["sha256"]:
                ERR.append(f"Hash-Drift {e['id']}: {e['raw']}")
        elif e.get("raw") and not p.exists():
            ERR.append(f"Original fehlt {e['id']}: {e['raw']}")


def main():
    zitate()
    katalog()
    werkzeuge()
    links()
    hashes()
    rep = ["# Lint Revisions-Wiki", "", f"Zitate geprüft: {N['zitate']} · Links: {N['links']} · Seiten: {N['dateien']}",
           f"**Fehler: {len(ERR)} · Warnungen: {len(WARN)}**", ""]
    if ERR:
        rep += ["## Fehler"] + [f"- {e}" for e in ERR] + [""]
    if WARN:
        rep += ["## Warnungen"] + [f"- {w}" for w in WARN[:300]] + ([f"- … {len(WARN) - 300} weitere"] if len(WARN) > 300 else [])
    (R / "reports").mkdir(exist_ok=True)
    (R / "reports" / "lint.md").write_text("\n".join(rep) + "\n", encoding="utf-8")
    print("\n".join(rep[:6]))
    for e in ERR[:20]:
        print("  ", e)
    sys.exit(1 if ERR else 0)


if __name__ == "__main__":
    main()
