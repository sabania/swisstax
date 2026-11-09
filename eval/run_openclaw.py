#!/usr/bin/env python3
"""Stellt Testfragen an einen echten OpenClaw-Agenten und protokolliert die Antworten.

  python3 eval/run_openclaw.py --agent steuer --fragen eval/fragen.yaml --out eval/openclaw-lauf.md [--ids q01,q05] [-j 3]
  python3 eval/run_openclaw.py --agent steuer --fragen eval/blindtest-fragen.yaml --out eval/openclaw-blindtest.md

Voraussetzung: `openclaw` im PATH (bzw. --openclaw <pfad>), Agent mit installiertem Steuer-Wiki (openclaw/README.md).
Jede Frage läuft als eigener `openclaw agent --local --json`-Turn in einer eigenen Session. Rohantworten werden als
JSON neben die Ausgabedatei gelegt (<out>.d/<id>.json), das Protokoll enthält Antwort, Tools und Dauer.
"""
from __future__ import annotations
import argparse, json, subprocess, time, concurrent.futures as cf
from pathlib import Path
import yaml


def load_questions(p: Path):
    d = yaml.safe_load(p.read_text(encoding="utf-8"))
    if "fragen" in d:
        qs = d["fragen"]
    else:
        qs = d["blindtest"]["fragen"]
    erw = {}
    ep = p.parent / "erwartet.yaml"
    if ep.exists():
        erw = (yaml.safe_load(ep.read_text(encoding="utf-8")) or {}).get("erwartet") or {}
    return [{"id": q["id"], "frage": q["frage"], "soll": q.get("soll") or erw.get(q["id"])} for q in qs]


def run(q, a):
    raw = Path(a.out + ".d") / f"{q['id']}.json"
    if raw.exists() and not a.force:
        d = json.loads(raw.read_text(encoding="utf-8"))
        if "error" not in d:
            return q["id"], d, 0.0
    t0 = time.time()
    cmd = [a.openclaw, "agent", "--local", "--agent", a.agent, "--session-id", f"eval-{a.tag}-{q['id']}", "--json",
           "--timeout", str(a.timeout), "--message", q["frage"]]
    for versuch in range(5):
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=a.timeout + 60)
        try:
            d = json.loads(p.stdout)
        except json.JSONDecodeError:
            d = {"error": (p.stderr or p.stdout)[-2000:]}
        if "busy" in json.dumps(d.get("error", "")):
            time.sleep(10 * (versuch + 1))
            continue
        break
    dt = time.time() - t0
    d["_dauer_s"] = round(dt, 1)
    raw.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    return q["id"], d, dt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent", required=True)
    ap.add_argument("--fragen", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--ids")
    ap.add_argument("-j", type=int, default=1, help="parallele Turns (nur mit laufendem Gateway sinnvoll; --local sperrt den State)")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--openclaw", default="openclaw")
    ap.add_argument("--tag", default="lauf")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    qs = load_questions(Path(a.fragen))
    if a.ids:
        want = set(a.ids.split(","))
        qs = [q for q in qs if q["id"] in want]
    Path(a.out + ".d").mkdir(parents=True, exist_ok=True)
    res = {}
    with cf.ThreadPoolExecutor(a.j) as ex:
        for qid, d, dt in ex.map(lambda q: run(q, a), qs):
            res[qid] = d
            print(f"{qid}: {d.get('_dauer_s', dt):.0f}s", "FEHLER" if "error" in d else "ok", flush=True)
    ver = subprocess.run([a.openclaw, "--version"], capture_output=True, text=True).stdout.strip()
    L = [f"# OpenClaw-Testlauf: {Path(a.fragen).name}", "",
         f"- OpenClaw: {ver} · Agent: `{a.agent}` · Fragen: {len(qs)} · Lauf: {time.strftime('%Y-%m-%d %H:%M')}",
         "- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.", ""]
    for q in qs:
        d = res.get(q["id"], {})
        meta = d.get("meta") or {}
        ts = meta.get("toolSummary") or {}
        ans = "\n\n".join(p.get("text", "") for p in d.get("payloads") or [] if isinstance(p, dict)) or json.dumps(d.get("error", "–"), ensure_ascii=False)
        L += [f"## {q['id']}", "", f"**Frage:** {q['frage']}", ""]
        if q.get("soll"):
            L += [f"**Soll (Referenz):** {q['soll']}", ""]
        L += [f"**Antwort des Agenten** ({d.get('_dauer_s', '?')} s · Tools: {ts.get('calls', '?')} Aufrufe "
              f"{', '.join(t.replace('mcp__openclaw__', '') for t in ts.get('tools', []))}):", "",
              "\n".join("> " + x for x in ans.strip().splitlines()), ""]
    Path(a.out).write_text("\n".join(L) + "\n", encoding="utf-8")
    print("->", a.out)


if __name__ == "__main__":
    main()
