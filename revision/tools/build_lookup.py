#!/usr/bin/env python3
"""Revisions-Wiki: kompakten Laufzeit-Index bauen → index/lookup.json (für tools/revision.py und den MCP-Server).

  python3 revision/tools/build_lookup.py

Liest registry/sources.yaml, data/katalog.yaml, data/regeln.yaml, data/prueffelder/*.yaml, data/prozess/*.yaml,
data/werte/*.yaml, data/themen/*.yaml, data/aufgaben.yaml, data/revio/{zuordnung,ketten}.yaml, data/revio/werkzeuge.csv
(Klassifikation) sowie raw/revio/revio-mcp-werkzeuge.{csv,md} und raw/revio/revio-schemas.json (nur Feldnamen).
Zur Laufzeit braucht das Werkzeug dann nur Python-Standardbibliothek.

Drift-Erkennung: `inputs_sha256` = Hash über alle Eingaben (eingaben()); je Prüffeld `pf[code]['_sha']` = sha256 der Datei
data/prueffelder/<code>.yaml (vor dem Entfernen von testakte_2025). tools/lint.py (aktualitaet) und tools/revision.py vergleichen.
"""
from __future__ import annotations
import csv, hashlib, json
from pathlib import Path
import yaml

R = Path(__file__).resolve().parents[1]


def y(p: Path, default=None):
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else default


def eingaben(r: Path = R) -> list[Path]:
    """Alle Dateien, aus denen lookup.json entsteht: registry/sources.yaml, data/**/*.yaml, data/revio/*.csv und die
    revio-Rohlisten unter raw/revio/, die werkzeuge() liest. Sortiert nach relativem Pfad (plattformunabhängig)."""
    fs = [r / "registry" / "sources.yaml", *(r / "data").rglob("*.yaml"), *(r / "data" / "revio").glob("*.csv"),
          *(r / "raw" / "revio" / n for n in ("revio-mcp-werkzeuge.csv", "revio-mcp-werkzeuge.md", "revio-schemas.json"))]
    return sorted({p for p in fs if p.is_file()}, key=lambda p: p.relative_to(r).as_posix())


def inputs_sha256(r: Path = R) -> str:
    """sha256 über (relativer Pfad, sha256 des Inhalts) aller Eingaben – ändert sich bei jeder Änderung, Umbenennung oder neuen Datei."""
    h = hashlib.sha256()
    for p in eingaben(r):
        h.update(p.relative_to(r).as_posix().encode("utf-8") + b"\0" + hashlib.sha256(p.read_bytes()).digest())
    return h.hexdigest()


def werkzeuge() -> dict:
    raw = R / "raw" / "revio" / "revio-mcp-werkzeuge.csv"
    out = {}
    if raw.exists():
        for r in csv.DictReader(raw.open(encoding="utf-8-sig"), delimiter=";"):
            out[r["werkzeug"]] = {"m": r["methode"], "p": r["pfad"], "mod": r["modul"], "pp": r["pfadparameter"], "b": r["body_schema"]}
    md = R / "raw" / "revio" / "revio-mcp-werkzeuge.md"
    if md.exists():  # 9 kuratierte revio_*-Werkzeuge stehen nur in der Markdown-Liste
        for line in md.read_text(encoding="utf-8").splitlines():
            if line.startswith("| `revio_"):
                name = line.split("`")[1]
                out[name] = {"m": "", "p": "", "mod": "revio (kuratiert)", "pp": "", "b": "", "z": line.split("|")[2].strip()}
    kl = R / "data" / "revio" / "werkzeuge.csv"
    if kl.exists():
        for r in csv.DictReader(kl.open(encoding="utf-8-sig"), delimiter=";"):
            w = out.setdefault(r["werkzeug"], {"m": r.get("methode", ""), "p": r.get("pfad", ""), "mod": r.get("modul", ""), "pp": "", "b": ""})
            w.update({"art": r.get("art", ""), "ber": r.get("revio_bereich", ""), "z": r.get("zweck") or w.get("z", ""), "g": r.get("begruendung", "")})
    sch = R / "raw" / "revio" / "revio-schemas.json"
    felder = {}
    if sch.exists():
        s = json.loads(sch.read_text(encoding="utf-8-sig"))
        for w in out.values():
            if w["b"] and w["b"] in s and isinstance(s[w["b"]], dict):
                felder[w["b"]] = list((s[w["b"]].get("properties") or {}).keys())
    return out, felder


def main():
    ein = inputs_sha256()   # vor dem Lesen: ändert sich eine Eingabe während des Laufs, gilt der lookup als veraltet (nie umgekehrt)
    reg = y(R / "registry" / "sources.yaml", [])
    quellen = {e["id"]: {"kurz": e.get("kurz"), "titel": e.get("titel"), "typ": e.get("typ"), "rang": e.get("rang"),
                         "lizenz": e.get("lizenz"), "stand": e.get("stand")} for e in reg}
    kat = y(R / "data" / "katalog.yaml", {})
    pf = {}
    for p in sorted((R / "data" / "prueffelder").glob("*.yaml")):
        b = p.read_bytes()   # Inhalt und Hash aus denselben Bytes
        d = yaml.safe_load(b.decode("utf-8"))
        d["_sha"] = hashlib.sha256(b).hexdigest()   # Drift-Prüfung (revision.py, lint.py): Hash der ganzen Datei, vor dem Entfernen von testakte_2025
        d.pop("testakte_2025", None)   # Testakte nur in eval/testfall-2025/hinweise/ (Tests) – nie im Laufzeitwissen, in quick/, wiki/ oder im Plugin
        pf[d["code"]] = d
    prozess = [y(p) for p in sorted((R / "data" / "prozess").glob("*.yaml"))]
    wz, felder = werkzeuge()
    lk = {
        "inputs_sha256": ein,
        "quellen": quellen,
        "katalog": {"prueffelder": kat.get("prueffelder", []), "schritte": {s["id"]: s for s in kat.get("schritte", [])}},
        "regeln": (y(R / "data" / "regeln.yaml", {}) or {}).get("regeln", []),
        "pf": pf,
        "prozess": prozess,
        "werte": [w for p in sorted((R / "data" / "werte").glob("*.yaml")) for w in (y(p, {}) or {}).get("werte", [])],
        "themen": [y(p) for p in sorted((R / "data" / "themen").glob("*.yaml"))],
        "aufgaben": (y(R / "data" / "aufgaben.yaml", {}) or {}).get("aufgaben", []),
        "pf_synonyme": (y(R / "data" / "aufgaben.yaml", {}) or {}).get("prueffeld_synonyme", {}),
        "revio": {**(y(R / "data" / "revio" / "zuordnung.yaml", {}) or {}),
                  "ketten": (y(R / "data" / "revio" / "ketten.yaml", {}) or {}).get("ketten", []),
                  "werkzeuge": wz, "felder": felder},
        "seiten": sorted(str(p.relative_to(R)) for d in ("quick", "wiki") for p in (R / d).rglob("*.md")),
    }
    (R / "index").mkdir(exist_ok=True)
    (R / "index" / "lookup.json").write_text(json.dumps(lk, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"lookup: {len(lk['katalog']['schritte'])} Schritte, {len(pf)} Prüffelder angereichert, {len(prozess)} Phasen, "
          f"{len(lk['werte'])} Werte, {len(wz)} revio-Werkzeuge, {len(lk['seiten'])} Seiten "
          f"({(R / 'index' / 'lookup.json').stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
