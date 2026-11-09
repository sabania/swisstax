#!/usr/bin/env python3
"""Legt ein neues Steuerjahr an (Gerüst), ohne Werte zu übernehmen.

  python3 tools/new_year.py --jahr 2027 --von 2026

- data/werte/<jur>/<jahr>.yaml      : gleiche Schlüssel wie im Vorjahr, wert: null, status: offen,
                                      Vorjahreswert nur als Hinweis (vorjahr: …) – NIE als Wert
- data/zuordnung/<kt>/<jahr>.yaml   : gleiche Ziffern/Positionen, status: offen (Formular kann sich ändern!)
- registry/years.yaml               : Jahr mit Status «geplant»
- reports/neues-jahr-<jahr>.md      : Checkliste der zu beschaffenden Quellen (aus den Vorjahresquellen abgeleitet)

Danach: Quellen des neuen Jahres registrieren/laden/chunken (skills/steuerwiki-pflege, Abschnitt A),
Bundesrecht mit `python3 tools/laws.py resolve --jahre <jahr>`.
"""
from __future__ import annotations
import argparse, copy, yaml
from common import ROOT, DATA, load_registry, ydump, today

KEEP = ("key", "einheit", "gilt_fuer", "ziffer", "abschnitt", "formular", "bezeichnung", "belege", "feld", "werte_keys")


def skeleton(rows: list[dict], kind: str) -> list[dict]:
    out = []
    for r in rows:
        n = {k: copy.deepcopy(r[k]) for k in KEEP if k in r}
        if kind == "werte":
            n["wert"] = None
            if r.get("wert") is not None or r.get("text"):
                n["vorjahr"] = r.get("text") or r.get("wert")
        n["status"] = "offen"
        n["quellen"] = []
        out.append(n)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jahr", type=int, required=True)
    ap.add_argument("--von", type=int, required=True)
    a = ap.parse_args()
    made = []
    for kind, key in (("werte", "werte"), ("zuordnung", "positionen")):
        for p in sorted((DATA / kind).glob(f"*/{a.von}.yaml")):
            d = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
            q = p.with_name(f"{a.jahr}.yaml")
            if q.exists():
                print(f"existiert bereits: {q.relative_to(ROOT)}")
                continue
            nd = {k: v for k, v in d.items() if k not in (key, "generiert", "hinweis")}
            nd["jahr"] = a.jahr
            nd["hinweis"] = f"Gerüst aus {a.von} erzeugt am {today()} – alle Werte offen; nur mit Quellen {a.jahr} füllen."
            nd[key] = skeleton(d.get(key) or [], kind)
            q.write_text(ydump(nd, width=200), encoding="utf-8")
            made.append(str(q.relative_to(ROOT)))
    yp = ROOT / "registry" / "years.yaml"
    years = yaml.safe_load(yp.read_text(encoding="utf-8")) if yp.exists() else {"jahre": {}}
    years.setdefault("jahre", {})[a.jahr] = {"status": "geplant", "angelegt": today()}
    yp.write_text(ydump(years), encoding="utf-8")
    # Checkliste aus Vorjahresquellen
    reg = load_registry()
    prev = [e for e in reg if e.get("jahre") and a.von in e["jahre"] and e.get("verarbeitung") != "link"
            and e["typ"] in ("wegleitung", "formular", "rundschreiben", "steuerfuss", "merkblatt", "gesetz", "verordnung", "weisung")]
    L = [f"# Neues Steuerjahr {a.jahr} – Checkliste", "", f"Erzeugt {today()} aus den Quellen {a.von}. Für jede Zeile die "
         f"Nachfolgefassung {a.jahr} suchen, in `registry/sources.yaml` eintragen und einlesen. Dauerhaft gültige Dokumente "
         f"(Kreisschreiben, Praxis) nur prüfen, ob sie geändert wurden (`tools/fetch.py --refresh` meldet Änderungen).", "",
         "| Jur | Typ | Vorjahresquelle | erledigt |", "|---|---|---|---|"]
    for e in sorted(prev, key=lambda e: (e["jurisdiktion"], e["typ"], e["id"])):
        L.append(f"| {e['jurisdiktion']} | {e['typ']} | {e.get('kurz') or e['id']}: [{e['titel']}]({e['url']}) | ☐ |")
    L += ["", "Bundesrecht (Fedlex): `python3 tools/laws.py resolve --jahre " + str(a.jahr) + "` → `fetch.py` → `laws.py convert` → `chunk.py`."]
    (ROOT / "reports").mkdir(exist_ok=True)
    (ROOT / "reports" / f"neues-jahr-{a.jahr}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("angelegt:", *made, f"reports/neues-jahr-{a.jahr}.md", sep="\n  ")


if __name__ == "__main__":
    main()
