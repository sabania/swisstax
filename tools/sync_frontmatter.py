#!/usr/bin/env python3
"""Gleicht die Metadaten-Frontmatter der Volltexte (sources/**/*.md) mit registry/sources.yaml ab.

Nur Metadaten (jahre, zeitbezug, gilt_ab, gilt_bis, ersetzt, ersetzt_durch, stand) – der Text bleibt unverändert.
Nach Änderungen an der Registry (z.B. Zeitmodell) ausführen; Chunks: tools/chunk.py (IDs/Texte bleiben stabil).

  python3 tools/sync_frontmatter.py [--check]
"""
from __future__ import annotations
import argparse
import yaml
from common import load_registry, source_path, ydump

FELDER = ["jahre", "zeitbezug", "gilt_ab", "gilt_bis", "ersetzt", "ersetzt_durch", "stand"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="nur melden, nichts schreiben")
    a = ap.parse_args()
    n = 0
    for e in load_registry():
        p = source_path(e)
        if not p.exists():
            continue
        txt = p.read_text(encoding="utf-8")
        if not txt.startswith("---\n"):
            continue
        end = txt.index("\n---\n", 4)
        fm = yaml.safe_load(txt[4:end]) or {}
        neu = dict(fm)
        for k in FELDER:
            if e.get(k) is not None:
                neu[k] = e[k]
            elif k in neu and k != "stand":
                neu.pop(k)
        if neu != fm:
            n += 1
            if not a.check:
                p.write_text("---\n" + ydump(neu, width=200).rstrip("\n") + txt[end:], encoding="utf-8")
    print(f"{n} Volltext-Frontmatter {'abweichend' if a.check else 'aktualisiert'}")


if __name__ == "__main__":
    main()
