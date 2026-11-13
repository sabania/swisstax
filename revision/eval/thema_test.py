#!/usr/bin/env python3
"""Regressionstest für `thema`: Begriff → erwartetes Thema (Matching) und Ausgabe-Prüfungen (Reihenfolge, Kürzung, Hinweise).

  python3 revision/eval/thema_test.py [revision/eval/thema-test.yaml ...]

Zusätzlich für alle Themen (kompakt): «Für den Agenten» vor «Fundstellen», keine doppelte ^[chunk-id] in einer Zeile, kompakt nicht länger als --voll.
"""
import re
import sys
from pathlib import Path
import yaml

R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R / "tools"))
import revision as rv  # noqa: E402


def main():
    files = sys.argv[1:] or [str(R / "eval" / "thema-test.yaml")]
    tot = ok = 0

    def pruef(good: bool, msg: str):
        nonlocal tot, ok
        tot += 1
        ok += good
        if not good:
            print("FALSCH " + msg)

    for f in files:
        d = yaml.safe_load(Path(f).read_text(encoding="utf-8"))
        for c in d.get("faelle") or []:
            t, rang, seite = rv.thema_wahl(c["begriff"])
            got = t["id"] if t else None
            soll = c["thema"] if isinstance(c["thema"], list) else [c["thema"]]
            z = [f"{r[3]['id']} {r[0]:.1f}/{r[1]}" for r in rang[:3]]
            pruef(got in soll, f"[{Path(f).name}] {c['begriff']!r} → {got}{' (Rückfall)' if seite else ''} (erwartet {' | '.join(soll)}; Rang: {', '.join(z)})")
        for c in d.get("ausgabe") or []:
            o = rv.thema(c["begriff"], bool(c.get("voll")))
            i = o.find("## Für den Agenten")
            if "agent_vor_zeichen" in c:
                pruef(0 <= i < c["agent_vor_zeichen"], f"{c['begriff']!r}: «Für den Agenten» bei Zeichen {i} (soll < {c['agent_vor_zeichen']})")
            if "agent_vor_bytes" in c:
                b = len(o[:i].encode()) if i >= 0 else -1
                pruef(0 <= b < c["agent_vor_bytes"], f"{c['begriff']!r}: «Für den Agenten» bei Byte {b} (soll < {c['agent_vor_bytes']})")
            for x in c.get("enthaelt") or []:
                pruef(x in o, f"{c['begriff']!r}: fehlt {x!r}")
            for x in c.get("nicht") or []:
                pruef(x not in o, f"{c['begriff']!r}: enthält {x!r}")
    for t in rv.L().get("themen", []):   # Struktur aller Themen
        o, v = rv.thema(t["id"]), rv.thema(t["id"], True)
        i, j = o.find("## Für den Agenten"), o.find("## Fundstellen")
        pruef(not t.get("agent") or 0 <= i < j, f"{t['id']}: «Für den Agenten» ({i}) nicht vor «Fundstellen» ({j})")
        # angehängte ^[quelle] am Zeilenende darf nicht schon im Aussagetext stehen (Duplikate innerhalb der Daten selbst zählen nicht)
        fund = o[j:].splitlines() if j >= 0 else []
        dup = [z for z in fund if (m := re.search(r"(\^\[[^\]]+\])$", z)) and m.group(1) in z[:m.start()]]
        pruef(not dup, f"{t['id']}: angehängte Fundstelle doppelt in «{dup[0][:100] if dup else ''}»")
        pruef(len(o) <= len(v), f"{t['id']}: kompakt ({len(o)}) länger als --voll ({len(v)})")
    print(f"{ok}/{tot} richtig")
    sys.exit(0 if ok == tot else 1)


if __name__ == "__main__":
    main()
