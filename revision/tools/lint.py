#!/usr/bin/env python3
"""Revisions-Wiki: deterministische Prüfung → reports/lint.md (Exit 1 bei Fehlern).

  python3 revision/tools/lint.py
  python3 revision/tools/lint.py --datei data/prueffelder/c1.yaml   # nur Zitate einer Datei

Prüft: Zitate in data/ (wörtlich im Chunk), Schritt-Ids gegen Katalog, Prüffeld-Codes, revio-Werkzeugnamen gegen die
Werkzeugliste, OpenClaw-Liste ↔ Klassifikation (werkzeuge.csv) ↔ Ketten ↔ Policy, Besonderheiten (Codes/Schritte), ^[chunk-id] in
Code/Skills/OpenClaw, Links in quick/ und wiki/, Dateinamen (kebab-case, ASCII, kein Datumspräfix), Hash der Originale (raw/).
"""
from __future__ import annotations
import csv, hashlib, json, re, sys
from pathlib import Path
import yaml

R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R / "tools"))
import revision as rv  # noqa: E402

ERR: list[str] = []
WARN: list[str] = []
N = {"zitate": 0, "links": 0, "dateien": 0, "verweise": 0}


def walk(o, path=""):
    if isinstance(o, dict):
        if "zitat" in o and ("quelle" in o or "chunk" in o):
            yield path, o.get("quelle") or o.get("chunk"), o.get("zitat")
        for k, v in o.items():
            yield from walk(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk(v, f"{path}[{i}]")


DATEI = None


def zitate():
    files = [R / DATEI] if DATEI else list((R / "data").rglob("*.yaml")) + list((R / "eval").glob("*/*.yaml"))
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
        openclaw(art)


ARTEN_KETTE = {"lesen", "vorbereiten", "kandidat", "nur_mensch"}


def openclaw(art: dict):
    """OpenClaw-Liste (zuordnung bereiche[nr=OpenClaw]) ↔ werkzeuge.csv ↔ Ketten ↔ openclaw/revio-tool-policy.json."""
    z = yaml.safe_load((R / "data" / "revio" / "zuordnung.yaml").read_text(encoding="utf-8")) or {}
    oc = next((b for b in z.get("bereiche", []) if b.get("nr") == "OpenClaw"), None)
    if not oc:
        ERR.append("zuordnung.yaml: Bereich «OpenClaw» (harmonisierte allow/deny-Liste) fehlt")
        return
    L, V = set(oc.get("werkzeuge_lesen", [])), set(oc.get("werkzeuge_vorbereiten", []))
    deny = set(oc.get("nur_mensch", [])) | set(oc.get("kandidaten", []))
    for n in sorted(L & V):
        ERR.append(f"OpenClaw: {n} zugleich lesen und vorbereiten")
    for n in sorted((L | V) & deny):
        ERR.append(f"OpenClaw: {n} zugleich allow und deny (nur_mensch/kandidaten)")
    for n, a in sorted(art.items()):
        soll = "lesen" if n in L else "vorbereiten" if n in V else None
        if a in ("lesen", "vorbereiten") and a != soll and not n.startswith("revio_"):
            ERR.append(f"werkzeuge.csv: {n} art={a}, OpenClaw={soll or 'deny'}")
        if n in deny and a in ("lesen", "vorbereiten"):
            ERR.append(f"werkzeuge.csv: {n} art={a}, in OpenClaw aber nur_mensch/Kandidat (deny)")
        if n in (L | V) and a not in ("lesen", "vorbereiten"):
            ERR.append(f"werkzeuge.csv: {n} art={a or 'leer'}, in OpenClaw aber allow")
    for n in sorted((L | V) - set(art)):
        ERR.append(f"OpenClaw: {n} fehlt in werkzeuge.csv")
    # Ketten: Art je Schritt, Werkzeug passend zur OpenClaw-Liste, nur_mensch nur am Ende
    kt = yaml.safe_load((R / "data" / "revio" / "ketten.yaml").read_text(encoding="utf-8")) or {}
    for k in kt.get("ketten", []):
        sch = k.get("schritte", [])
        for i, s in enumerate(sch, 1):
            w, a = s.get("werkzeug", ""), s.get("art", "")
            ort = f"ketten.yaml {k['id']} Schritt {i} `{w}`"
            if a not in ARTEN_KETTE:
                ERR.append(f"{ort}: art={a!r} (erlaubt: {', '.join(sorted(ARTEN_KETTE))})")
            elif w.startswith("revio_"):
                if a in ("lesen", "vorbereiten") and art.get(w) != "lesen":
                    ERR.append(f"{ort}: art={a}, werkzeuge.csv={art.get(w) or 'fehlt'} (revio_* nur mit art lesen erlaubt)")
            elif a == "lesen" and w not in L:
                ERR.append(f"{ort}: art=lesen, aber nicht in OpenClaw werkzeuge_lesen ({'vorbereiten' if w in V else 'deny'})")
            elif a == "vorbereiten" and w not in V:
                ERR.append(f"{ort}: art=vorbereiten, aber nicht in OpenClaw werkzeuge_vorbereiten ({'lesen' if w in L else 'deny'})")
            elif a == "kandidat" and w in (L | V):
                ERR.append(f"{ort}: art=kandidat, aber in OpenClaw allow")
            elif a == "nur_mensch" and w in (L | V):
                ERR.append(f"{ort}: art=nur_mensch, aber in OpenClaw allow")
            if s.get("optional") and a not in ("lesen", "vorbereiten", "kandidat"):
                WARN.append(f"{ort}: optional bei art={a}")
        arts = [s.get("art") for s in sch]
        if "nur_mensch" in arts and any(a != "nur_mensch" for a in arts[arts.index("nur_mensch"):]):
            ERR.append(f"ketten.yaml {k['id']}: nur_mensch-Schritte nur am Kettenende (Nummern/Querverweise)")
    # Policy (generiert von build_quick.py) aktuell?
    pol = R / "openclaw" / "revio-tool-policy.json"
    if pol.exists():
        d = json.loads(pol.read_text(encoding="utf-8"))
        allow = L | {n for n, a in art.items() if n.startswith("revio_") and a == "lesen"}
        if set(d.get("allow", [])) != allow or set(d.get("approval", [])) != V:
            ERR.append("openclaw/revio-tool-policy.json veraltet (allow/approval ≠ OpenClaw-Liste) → python3 revision/tools/build_quick.py")
        for n in ("revio_call", "revio_create_client"):
            if n in set(d.get("allow", [])) | set(d.get("approval", [])):
                ERR.append(f"openclaw/revio-tool-policy.json: {n} muss deny sein")
    # Besonderheiten: Prüffeld-Codes und Schritt-Ids gegen den Katalog
    kat = yaml.safe_load((R / "data" / "katalog.yaml").read_text(encoding="utf-8"))
    ids, codes = {s["id"] for s in kat["schritte"]}, {p["code"] for p in kat["prueffelder"]}
    for b in z.get("prueffeld_besonderheiten", []):
        for c in b.get("prueffelder") or []:
            if c not in codes:
                ERR.append(f"zuordnung.yaml Besonderheit «{b.get('code', '')[:40]}»: unbekanntes Prüffeld {c}")
        for sid in (b.get("schritte") or []) + (b.get("ausser") or []):
            if sid not in ids:
                ERR.append(f"zuordnung.yaml Besonderheit «{b.get('code', '')[:40]}»: unbekannter Schritt {sid}")
        if not (b.get("prueffelder") or b.get("schritte") or b.get("schritt_nr")):
            ERR.append(f"zuordnung.yaml Besonderheit «{b.get('code', '')[:40]}»: weder prueffelder noch schritte/schritt_nr – trifft nie")


def verweise():
    """^[chunk-id] in Werkzeug-Code, Aufgaben, revio-Daten, Skills und OpenClaw-Snippet müssen existieren."""
    files = [R / "tools" / "revision.py", R / "tools" / "mcp_server.py", R / "data" / "aufgaben.yaml", *(R / "data" / "revio").glob("*.yaml"),
             *(R / "openclaw").glob("*.md"), *(R / "skills").rglob("*.md")]
    for p in files:
        if not p.exists():
            continue
        for cid in sorted(set(re.findall(r"\^\[([a-z0-9][\w.-]*__[\w.-]+)\]", p.read_text(encoding="utf-8")))):
            N["verweise"] += 1
            if rv.chunk_text(cid) is None:
                ERR.append(f"{p.relative_to(R)}: Verweis auf fehlenden Chunk ^[{cid}]")


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
    global DATEI
    if len(sys.argv) > 2 and sys.argv[1] == "--datei":   # nur Zitate einer Datei prüfen (für Korrektur-Agenten)
        DATEI = sys.argv[2].removeprefix("revision/")
        zitate()
        print(f"{DATEI}: {N['zitate']} Zitate, {len(ERR)} Fehler")
        for e in ERR:
            print("  ", e)
        sys.exit(1 if ERR else 0)
    zitate()
    katalog()
    werkzeuge()
    verweise()
    links()
    hashes()
    rep = ["# Lint Revisions-Wiki", "", f"Zitate geprüft: {N['zitate']} · Verweise ^[…]: {N['verweise']} · Links: {N['links']} · Seiten: {N['dateien']}",
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
