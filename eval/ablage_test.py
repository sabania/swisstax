#!/usr/bin/env python3
"""Misst die deterministische Dokumenterkennung (tools/steuer.py ablage) gegen eval/ablage-test.yaml: Top-1/Top-3."""
from __future__ import annotations
import re, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import steuer  # noqa: E402

f = yaml.safe_load((ROOT / "eval" / "ablage-test.yaml").read_text(encoding="utf-8"))["faelle"]
t1 = t3 = 0
fehl = []
for c in f:
    out = steuer.ablage(c["text"])
    ids = re.findall(r"\(`([a-z0-9\-]+)`\)|^\d\. \*\*(.+?)\*\* \(Prozessdokument\)", out, re.M)
    er = steuer.L()["erkennung"]["prozessdokumente"]
    name2id = {v["name"]: k for k, v in er.items()}
    kand = [a or name2id.get(b, b) for a, b in ids]
    if kand[:1] == [c["soll"]]:
        t1 += 1
    if c["soll"] in kand[:3]:
        t3 += 1
    else:
        fehl.append((c["soll"], kand[:3], c["text"][:70]))
    if kand[:1] != [c["soll"]] and c["soll"] in kand[:3]:
        fehl.append((c["soll"] + " (nur Top-3)", kand[:3], c["text"][:70]))
n = len(f)
print(f"Dokumenterkennung: Top-1 {t1}/{n} ({t1 / n:.0%}) · Top-3 {t3}/{n} ({t3 / n:.0%})")
for s, k, t in fehl:
    print(f"  soll {s:45} ist {k} · {t}")
