#!/usr/bin/env python3
"""Routing-Test für den Einstieg `aufgabe`: Formulierung → erwartete Aufgabe (und ggf. Prüffeld/Schritt).

  python3 revision/eval/routing_test.py [revision/eval/routing-test.yaml ...]
"""
import sys
from pathlib import Path
import yaml

R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R / "tools"))
import revision as rv  # noqa: E402


def main():
    files = sys.argv[1:] or [str(R / "eval" / "routing-test.yaml")]
    tot = ok = 0
    for f in files:
        for c in yaml.safe_load(Path(f).read_text(encoding="utf-8"))["faelle"]:
            a, p = rv._aufgabe_finden(c["text"])
            got = a["id"] if a else None
            good = got == c["aufgabe"] and (not c.get("param") or (p or "") == c["param"])
            tot += 1
            ok += good
            if not good:
                print(f"FALSCH [{Path(f).name}]: {c['text']!r} → {got} {p or ''} (erwartet {c['aufgabe']} {c.get('param', '')})")
    print(f"{ok}/{tot} richtig")
    sys.exit(0 if ok == tot else 1)


if __name__ == "__main__":
    main()
