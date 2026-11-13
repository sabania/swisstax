#!/usr/bin/env python3
"""Regressionstest für Werkzeug-Ausgaben (tools/revision.py), die schwache Modelle wörtlich befolgen:
Phasenwahl von `prozess`, Tor in der Kompaktansicht, Budgets, Schritt-Ids, Notizregel je Rolle, Rechner-Eingaben.

  python3 revision/eval/werkzeug_test.py
"""
import sys
from pathlib import Path

R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R / "tools"))
import revision as rv  # noqa: E402

FAELLE = []


def fall(name):
    def deko(fn):
        FAELLE.append((name, fn))
        return fn
    return deko


def kopf(t: str) -> str:
    """Erste Zeile ohne Drift-Warnung."""
    return next((z for z in t.splitlines() if not z.startswith(rv.DRIFT_TXT)), "")


@fall("Phasenwahl prozess: Eingabe → Phase bzw. Agent-Prozess")
def _phasenwahl():
    soll = {"Phase 4": "# p4-", "Phase 1": "# p1-", "phase 2": "# p2-", "Prozessphase 3": "# p3-", "Prozess 7": "# p7-", "Prozess 8": "# p8-",
            "p4": "# p4-", "abschluss": "# p4-", "revisionsbericht": "# p5-", "bericht": "# p5-", "wesentlichkeit": "# p2-",
            "rangrücktritt": "# p6-", "Phase 4 schritte": "# p4-", "schritte p4": "# p4-", "fallstricke p6": "# p6-", "p4 fragen_kunde": "# p4-",
            "agent prozess 2": "Agent-Prozess 2", "Agent-Prozess 3": "Agent-Prozess 3", "Prozess 4": "Agent-Prozess 4"}
    return [f"{q!r} → {kopf(rv.prozess(q))[:60]!r} (erwartet {s!r})" for q, s in soll.items() if not kopf(rv.prozess(q)).startswith(s)]


@fall("prozess: «|»-Listen und «ab N» ohne Abschnitt geben einen Hinweis statt einer stillen Wahl")
def _pipes():
    f = []
    for q in ("p1 schritte|entscheide|fallstricke", "p3 entscheide|fallstricke|gesetz", "p6 schritte|entscheide"):
        if not rv.prozess(q).startswith("Bitte genau einen Abschnitt"):
            f.append(q)
    if "gilt für einen Abschnitt" not in rv.prozess("ab 3"):
        f.append("ab 3")
    if "nur 21 Einträge" not in rv.prozess("p8 schritte ab 99") and "nur " not in rv.prozess("p8 schritte ab 99"):
        f.append("p8 schritte ab 99")
    return f


@fall("Kompaktansicht: Tor-Schritt vollständig (p7/p8), Grösse ≤ PROZESS_KOMPAKT_MAX Bytes, keine «|»-Aufrufe, Aufrufe nie halb")
def _kompakt():
    f = []
    kern = {"p7": ["keine Kundenanfrage", "Meldung an den WP"],
            "p8": ["Fehlt die Bestätigung: nichts lesen", "Start nur auf Auftrag des WP", "Kontext-Schlüssel fixieren", "abbrechen, Pendenz erfassen"]}
    for p in rv.L().get("prozess", []):
        pid = p["id"].split("-")[0]
        t = rv.prozess(pid)
        t_ = "\n".join(z for z in t.splitlines() if not z.startswith(rv.DRIFT_TXT))
        if len(t_.encode("utf-8")) > rv.PROZESS_KOMPAKT_MAX:
            f.append(f"{pid}: {len(t_.encode('utf-8'))} Bytes")
        f += [f"{pid}: «{k}» fehlt" for k in kern.get(pid, []) if k not in t]
        for x in t.split("`")[1::2]:
            if x.startswith("prozess ") and "|" in x:
                f.append(f"{pid}: Pipe-Aufruf `{x}`")
            if x.startswith("kapitalverlust --") and "--gewinnreserve" not in x and "--buchwert" not in x:
                f.append(f"{pid}: gekürzter Aufruf `{x[:60]}…`")
    return f


@fall("Budgets: prueffeld ≤ 24 KB (auch --voll), prozess --voll in Teilen ≤ 24 KB")
def _budgets():
    f = []
    for p in rv.L()["katalog"]["prueffelder"]:
        for v in (False, True):
            n = len(rv.prueffeld(p["code"], v).encode("utf-8"))
            if n > 24 * 1024 + 200:
                f.append(f"prueffeld {p['code']} voll={v}: {n}")
    for p in rv.L().get("prozess", []):
        pid = p["id"].split("-")[0]
        for k in (1, 2, 3):
            n = len(rv.prozess(f"{pid} ab {k}", voll=True).encode("utf-8"))
            if n > 24 * 1024 + 200:
                f.append(f"prozess {pid} --voll ab {k}: {n}")
    return f


@fall("_schritt_ids: Einzel-Id, Liste mit «/», Bereich, Komma-Liste (keine Beträge)")
def _ids():
    soll = {"B1-102, 201, 202, 309, 310": {"B1-102", "B1-201", "B1-202", "B1-309", "B1-310"},
            "C1-106, 208, 304–308": {"C1-106", "C1-208", "C1-304", "C1-305", "C1-306", "C1-307", "C1-308"},
            "SCH5-101/201": {"SCH5-101", "SCH5-201"}, "I1-401–I1-403": {"I1-401", "I1-402", "I1-403"},
            "C1-302, 100'000 CHF": {"C1-302"}, "C1-302, 2025": {"C1-302"}}
    return [f"{t!r} → {sorted(rv._schritt_ids(t))}" for t, s in soll.items() if rv._schritt_ids(t) != s]


@fall("Notizregel je Rolle: WP/4xx ohne Anweisung kein Textfeld; 3xx mit Übergangsregel und Schwelle")
def _notiz():
    f = []
    for sid in ("B1-309", "C1-401", "SCH3-302"):
        t = rv.pruefschritt(sid)
        if "nur im Textfeld protokollieren;" in t.split("## Feststellung / Notiz")[-1].split("\n\n")[0].split("Mit Anweisung")[0]:
            f.append(f"{sid}: Textfeld-Gebot ohne Anweisung")
    v = rv._notiz_nag("vorbereiten")
    f += [f"3xx: «{k}» fehlt" for k in ("Übergangsregel bis Entscheid consis", "überschrittenen Schwelle") if k not in v]
    return f


@fall("Rechner: negative Beträge abgewiesen, fehlende Reserven gewarnt, Teil-Vorjahreswerte ausgewertet")
def _rechner():
    f = []
    try:
        rv.kapitalverlust(100000, aktiven=500000, verbindlichkeiten=600000, rangruecktritt=-50000)
        f.append("--rangruecktritt negativ angenommen")
    except ValueError:
        pass
    if "nicht angegeben" not in rv.kapitalverlust(100000, aktiven=500000, verbindlichkeiten=440000, kapitalreserve=0):
        f.append("keine Warnung bei fehlender --gewinnreserve")
    if "grösser als das Fremdkapital" not in rv.kapitalverlust(100000, aktiven=500000, verbindlichkeiten=100000, kapitalreserve=0,
                                                               gewinnreserve=0, covid_kredit=200000):
        f.append("keine Warnung Covid-Kredit > Fremdkapital")
    if "ORDENTLICHE" not in rv.revisionspflicht(25e6, 45e6, 100, 24e6, 44e6):
        f.append("revisionspflicht: 2 bekannte VJ-Grössen überschritten → ordentlich")
    if "EINGESCHRÄNKTE" not in rv.revisionspflicht(25e6, 45e6, 100, 1e6, 2e6):
        f.append("revisionspflicht: höchstens 1 VJ-Grösse möglich → eingeschränkt")
    return f


def main():
    fehler = 0
    for name, fn in FAELLE:
        f = fn()
        fehler += bool(f)
        print(("OK    " if not f else "FALSCH") + f" {name}" + "".join(f"\n       - {x}" for x in f))
    print(f"{len(FAELLE) - fehler}/{len(FAELLE)} richtig")
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main()
