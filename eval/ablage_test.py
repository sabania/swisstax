#!/usr/bin/env python3
"""Misst die deterministische Dokumenterkennung (tools/steuer.py ablage): Top-1/Top-3 gegen ein Testset (Standard eval/ablage-test.yaml)
oder mit --selbsttest: jeder Belegtyp/jedes Verfahrensdokument muss an seinem eigenen Namen erkannt werden."""
from __future__ import annotations
import re, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import steuer  # noqa: E402

GLEICH = {"steuerrechnung": {"veranlagung", "provisorische-rechnung"}, "vorjahresveranlagung": {"veranlagung"}}
if len(sys.argv) > 1 and sys.argv[1] == "--selbsttest":
    Lk = steuer.L()
    items = [(b["id"], b["name"].split("(")[0].strip()) for b in Lk["belege"]] + \
            [(k, v["name"].split("(")[0].split("/")[0].strip()) for k, v in Lk["erkennung"]["verfahrensdokumente"].items()]
    fehl = []
    for i, name in items:
        k = re.findall(r"^\d\. \*\*.+?\*\* \(`([a-z0-9\-]+)`\)", steuer.ablage(name + " 2025"), re.M)
        if not k or (k[0] != i and k[0] not in GLEICH.get(i, ())):
            fehl.append((i, name, k[:3]))
    print(f"Selbsttest Erkennung am eigenen Namen: {len(items) - len(fehl)}/{len(items)}")
    for x in fehl:
        print("  ", x)
    sys.exit(1 if fehl else 0)
DATEI = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "eval" / "ablage-test.yaml"
f = yaml.safe_load(DATEI.read_text(encoding="utf-8"))["faelle"]
t1 = t3 = 0
fehl = []
for c in f:
    out = steuer.ablage(c["text"])
    kand = re.findall(r"^\d\. \*\*.+?\*\* \(`([a-z0-9\-]+)`\)", out, re.M)
    # Belegtyp «steuerrechnung» = Verfahrensdokumente Veranlagung/definitive bzw. provisorische Rechnung
    if c["soll"] == "steuerrechnung":
        kand = ["steuerrechnung" if k in ("veranlagung", "provisorische-rechnung") else k for k in kand]
    if kand[:1] == [c["soll"]]:
        t1 += 1
    if c["soll"] in kand[:3]:
        t3 += 1
    else:
        fehl.append((c["soll"], kand[:3], c["text"][:70]))
    if kand[:1] != [c["soll"]] and c["soll"] in kand[:3]:
        fehl.append((c["soll"] + " (nur Top-3)", kand[:3], c["text"][:70]))
n = len(f)
sets = {}
for c in f:
    sets.setdefault(c.get("set", "alle"), [0, 0])
    sets[c.get("set", "alle")][1] += 1
print(f"{DATEI.name}: " + " · ".join(f"{k} n={v[1]}" for k, v in sets.items()))
print(f"Dokumenterkennung: Top-1 {t1}/{n} ({t1 / n:.0%}) · Top-3 {t3}/{n} ({t3 / n:.0%})")
for s, k, t in fehl:
    print(f"  soll {s:45} ist {k} · {t}")
