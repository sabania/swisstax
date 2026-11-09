#!/usr/bin/env python3
"""Werkzeugtest: findet `steuer wert`/`steuer position` mit realistischen Eingaben den erwarteten Eckwert bzw. die Ziffer?

  python3 eval/werkzeug_test.py                       # eval/werkzeug-test.yaml (Fehlgriffe aus echten Läufen)
  python3 eval/werkzeug_test.py eval/werkzeug-holdout.yaml --fehler
Treffer = einer der erwarteten Schlüssel/Ziffern unter den ersten 3 Treffern; «enthaelt» = Text steht in der Ausgabe.
"""
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import steuer  # noqa: E402


def pruefe(c, top=3):
    j, jahr, e = c["jur"], str(c["jahr"]), str(c["eingabe"])
    if c.get("enthaelt") or c.get("nicht_enthaelt"):
        if c["befehl"] == "rechne":
            out = steuer.rechne(e)
        elif c["befehl"] in ("ablage", "beleg"):
            out = getattr(steuer, c["befehl"])(e, j, jahr)
        elif c["befehl"] == "formular":
            out = steuer.formular(j, jahr)
        else:
            out = (steuer.wert if c["befehl"] == "wert" else steuer.position)(j, jahr, e)
        ok = (not c.get("enthaelt") or c["enthaelt"].lower() in out.lower()) and \
             (not c.get("nicht_enthaelt") or c["nicht_enthaelt"].lower() not in out.lower())
        return ok, out.splitlines()[0][:100]
    if c["befehl"] == "wert":
        if hasattr(steuer, "wert_treffer"):
            hits = [r["key"] for r in steuer.wert_treffer(j, jahr, e)]
        else:  # ältere Werkzeugstände: Ausgabe lesen
            hits = re.findall(r"^- \*\*([\w.]+)\*\* =", steuer.wert(j, jahr, e), re.M)
    else:
        if hasattr(steuer, "position_treffer"):
            hits = [str(p["ziffer"]) for p in steuer.position_treffer(j, jahr, e)]
        else:
            hits = [re.sub(r"^Ziff\. ", "", h) for h in re.findall(r"^### \S+ \d{4} · (.+?) · ", steuer.position(j, jahr, e), re.M)]
    ok = any(h in [str(x) for x in c["erwartet"]] for h in hits[:top])
    return ok, " | ".join(hits[:3]) or "–"


def main(argv):
    files = [a for a in argv if not a.startswith("--")] or [str(ROOT / "eval" / "werkzeug-test.yaml")]
    for f in files:
        faelle = yaml.safe_load(open(f, encoding="utf-8"))["faelle"]
        n, ok, fehl = Counter(), Counter(), []
        for c in faelle:
            r, info = pruefe(c)
            k = c["befehl"]
            n[k] += 1
            ok[k] += r
            if not r:
                fehl.append(f"  ✗ {k} {c['jur']} {c['jahr']} «{c['eingabe']}» → {info}  (erwartet {c.get('erwartet') or c.get('enthaelt')})")
        print(f"{Path(f).name}: " + " · ".join(f"{k} {ok[k]}/{n[k]} ({100 * ok[k] / n[k]:.0f}%)" for k in n)
              + f" · gesamt {sum(ok.values())}/{sum(n.values())}")
        if "--fehler" in argv:
            print("\n".join(fehl))


if __name__ == "__main__":
    main(sys.argv[1:])
