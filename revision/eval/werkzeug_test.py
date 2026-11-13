#!/usr/bin/env python3
"""Regressionstest für Werkzeug-Ausgaben (tools/revision.py), die schwache Modelle wörtlich befolgen:
Phasenwahl von `prozess`, Tor in der Kompaktansicht, Budgets, Schritt-Ids, Notizregel je Rolle, Rechner-Eingaben.

  python3 revision/eval/werkzeug_test.py
"""
import re
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


AKTE_GJ = R / "eval" / "testdaten" / "fiktive-zahlen-ag-2025" / "text"   # Entwicklungs-Testakte (fiktiv); nur Struktur prüfen
AKTE_VJ = R / "eval" / "testdaten" / "fiktive-zahlen-ag-2024" / "text"


def _teile(pf=None, schritt=None, vj=True) -> list[str]:
    """Alle Teile eines Arbeitspakets (Anzahl aus dem Kopf von Teil 1)."""
    import re
    t1 = rv.arbeitspaket(str(AKTE_GJ), pf, str(AKTE_VJ) if vj else None, schritt)
    n = int(re.search(r"– Teil 1/(\d+)", t1).group(1))
    return [t1] + [rv.arbeitspaket(str(AKTE_GJ), pf, str(AKTE_VJ) if vj else None, schritt, k) for k in range(2, n + 1)]


@fall("arbeitspaket: Teile ≤ 24 KB mit Kopf und Regeln, Abschnitte 2–8, Konten erkannt (Bilanz- und ER-Prüffeld), Schritt-/Mehrfach-Paket, Fehler")
def _arbeitspaket():
    import re
    if not AKTE_GJ.is_dir():
        return []
    f = []
    for pf, schritt, konten in (("B1", None, True), ("C1", None, True), ("R1", None, True), ("A1", None, True), ("T1", None, False),
                                ("L1,N1", None, True), (None, "C1-302", True)):
        teile = _teile(pf, schritt)
        alles = "\n".join(teile)
        for i, t in enumerate(teile, 1):
            if len(t.encode("utf-8")) > rv.AP_MAX:
                f.append(f"{pf or schritt} Teil {i}: {len(t.encode('utf-8'))} Bytes > {rv.AP_MAX}")
            if not re.search(rf"– Teil {i}/{len(teile)}\n", t) or "Regel 1:" not in t or "Regel 3:" not in t:
                f.append(f"{pf or schritt} Teil {i}: Kopf/Regeln fehlen")
        for nr in ("## 2.", "## 3.", "## 4.", "## 5.", "## 6.", "## 7."):
            if nr not in alles:
                f.append(f"{pf or schritt}: Abschnitt {nr} fehlt")
        if not schritt and "## 8." not in alles:
            f.append(f"{pf}: Abschnitt 8 (Schritte) fehlt")
        if schritt and "## 1. Schritt" not in alles:
            f.append(f"{schritt}: Schrittkarte fehlt")
        if konten and not re.search(r"^\| \d{3,5}[A-Za-z]? \|", alles, re.M):
            f.append(f"{pf or schritt}: keine Kontozeile erkannt")
        if "**Ende des Arbeitspakets.**" not in teile[-1]:
            f.append(f"{pf or schritt}: letzter Teil ohne Ende-Zeile")
    if "nicht gelesen" not in _teile("B1", vj=False)[-1]:
        f.append("ohne --vj: Hinweis «nicht gelesen» fehlt")
    for args, msg in (((str(AKTE_GJ), "XY9"), "unbekannt"), ((str(AKTE_GJ), "C1", None, None, 0), "gibt es nicht"),
                      ((str(AKTE_GJ), None, None, "C1-999"), "unbekannt"), ((str(AKTE_GJ),), "Prüffeld fehlt")):
        try:
            rv.arbeitspaket(*args)
            f.append(f"kein Fehler für {args[1:]}")
        except ValueError as e:
            if msg not in str(e):
                f.append(f"Fehlertext für {args[1:]}: {e}")
    return f


@fall("plan: gültiges JSON, Turn 1 mit aufgabe + arbeitspaket, jede Id genau einmal + Abschluss mit allen Ids, Grenze in jeder Anweisung")
def _plan():
    import json
    if not AKTE_GJ.is_dir():
        return []
    f = []
    for auftrag, a_id, codes in (("Prozess 2 – Bereite die Prüffelder L1/N1 und H2 vor.", "prueffeld", ["L1", "N1", "H2"]),
                                 ("Prüffeld C1-302 bearbeiten", "pruefschritt", ["C1"]), ("Starte das Mandat.", "mandat-start", []),
                                 ("Prozess 1 – Jahresrechnung mit Saldoliste abstimmen", "import", [])):
        p = json.loads(rv.plan(auftrag, str(AKTE_GJ), str(AKTE_VJ)))
        if p["aufgabe"] != a_id or p["prueffelder"] != codes:
            f.append(f"{auftrag!r}: {p['aufgabe']} {p['prueffelder']} (erwartet {a_id} {codes})")
        if [t["nr"] for t in p["turns"]] != list(range(1, len(p["turns"]) + 1)) or len(p["turns"]) < 2:
            f.append(f"{auftrag!r}: Turns nicht fortlaufend")
        if any("kein ✓" not in t["anweisung"] or "nichts senden" not in t["anweisung"] for t in p["turns"]):
            f.append(f"{auftrag!r}: Anweisung ohne Grenze")
        if codes:
            ids = [s for t in p["turns"][:-1] for s in t["schritte"]]
            soll = [x["id"] for c in codes for x in sum(rv._schritt_folge(c), [])] if a_id == "prueffeld" else ["C1-302"]
            if sorted(ids) != sorted(soll) or sorted(p["abschluss"]["schritte"]) != sorted(soll):
                f.append(f"{auftrag!r}: Schritte {len(ids)}/{len(soll)}")
            if not any(c.startswith("arbeitspaket ") for c in p["turns"][0]["aufrufe"]) or not p["turns"][0]["aufrufe"][0].startswith("aufgabe"):
                f.append(f"{auftrag!r}: Turn 1 ohne aufgabe/arbeitspaket")
    return f


# Kleine fiktive Akte mit abweichender Struktur (Namen und Beträge erfunden): Saldoliste als Kompositum ohne Gruppenspalte, mit Gruppen-
# zeilen und Kontonummern ausserhalb des Kontenrahmens KMU; Journal mit Kontoblatt-Überschrift «Bezeichnung (Nummer)» und Spalten
# Belastung/Gutschrift; Jahresrechnung als «Finanzbericht» im OR-Format (Positionszeilen ohne Konten) und Anhang mit Zession
SYNTH = {
    "Abschluss/Kontensaldenliste_2030.md": """# Abschluss/Kontensaldenliste_2030.xlsx

| Kto-Nr. | Kontobezeichnung | 31.12.2030 | 31.12.2029 |
|---|---|---|---|
| 100 | Flüssige Mittel | 14'691.37 | 11'802.64 |
| 1000 | Kasse | 4'213.58 | 1'907.23 |
| 1020 | Bank A Kontokorrent | 10'477.79 | 9'895.41 |
| 1400 | Forderungen Kunden Inland | 71'356.17 | 61'283.92 |
| 1401 | Forderungen Kunden Ausland | 29'771.46 | 19'624.31 |
| 2000 | Verbindlichkeiten Lieferanten | -41'238.66 | -34'919.08 |
| 2800 | Aktienkapital | -97'531.13 | -97'531.13 |
| 3400 | Dienstleistungsertrag | -307'418.59 | -281'366.47 |
| 6900 | Zinsaufwand Bank | 1'137.29 | 913.18 |
""",
    "Abschluss/Buchungsjournal_2030.md": """# Abschluss/Buchungsjournal_2030.pdf

## Forderungen Kunden Inland (1400)

| Datum | Beleg | Text | Gegenkonto | Belastung | Gutschrift | Saldo |
|---|---|---|---|---|---|---|
| 01.01.2030 | EB | Eröffnung | 9100 |  |  | 61'283.92 |
| 15.06.2030 | RE-2030-0007 | Faktura Kunde | 3400 | 24'567.11 |  | 85'851.03 |
| 30.09.2030 | ZE-2030-0003 | Zahlung Kunde | 1020 |  | 14'494.86 | 71'356.17 |
""",
    "Abschluss/Finanzbericht_2030.md": """# Abschluss/Finanzbericht_2030.pdf

## Bilanz per 31.12.2030

| Aktiven | Anhang | 31.12.2030 | 31.12.2029 |
|---|---|---|---|
| Flüssige Mittel |  | 14'691.37 | 11'802.64 |
| Forderungen aus Lieferungen und Leistungen | 2 | 101'127.63 | 80'908.23 |
| Total Aktiven |  | 115'819.00 | 92'710.87 |

## Anhang

### 1. Grundsätze
Nach den Vorschriften des Obligationenrechts.

### 2. Zur Sicherung eigener Verbindlichkeiten verwendete Aktiven
Forderungen von CHF 48'765 sind an Bank A zediert (Globalzession).
""",
}


@fall("arbeitspaket generisch: Saldoliste-Kompositum, Gruppenzeilen, Teiltreffer, Bilanzseite, Journal «(Nr)», Belastung/Gutschrift, "
      "Finanzbericht im OR-Format, Anhang-Begriffsgruppe")
def _arbeitspaket_generisch():
    import tempfile
    f = []
    with tempfile.TemporaryDirectory() as d:
        for rel, txt in SYNTH.items():
            (Path(d) / rel).parent.mkdir(parents=True, exist_ok=True)
            (Path(d) / rel).write_text(txt, encoding="utf-8")
        c1, b1 = rv.arbeitspaket(d, "C1"), rv.arbeitspaket(d, "B1")
    soll = {"C1: Konto 1400 (Teiltreffer «b»)": ("| 1400 | Forderungen Kunden Inland |" in c1 and "| b |" in c1),
            "C1: Kontoblatt «(1400)» aus dem Buchungsjournal": "### Konto 1400 · Abschluss/Buchungsjournal_2030.md" in c1,
            "C1: Gegenkonten aus Belastung/Gutschrift": "Gegenkonten der Buchungen" in c1,
            "C1: Positionszeile der Bilanz (OR-Format)": re.search(r"\|Forderungen aus Lieferungen und Leistungen\|2\|101'127.63", c1) is not None,
            "C1: Anhang «Zur Sicherung …» (Zession)": "Anhang «### 2. Zur Sicherung eigener Verbindlichkeiten" in c1,
            "B1: Gruppenzeile «100» als Gruppe, nicht als Konto": ("| 1020 | Bank A Kontokorrent | Flüssige Mittel |" in b1
                                                                  and not re.search(r"^\| 100 \|", b1, re.M) and "Gruppe 100 Flüssige Mittel" in b1),
            "B1: «Zinsaufwand» nicht bei den flüssigen Mitteln": "| 6900 | Zinsaufwand Bank" not in b1.split("Gegenkonten der Buchungen")[0]}
    f += [k for k, ok in soll.items() if not ok]
    namen = {"Kontensaldenliste_2030": rv._ist_saldoliste, "Hauptbuchsaldi_2030": rv._ist_saldoliste, "Finanzbericht_2030": rv._ist_jahresrechnung,
             "Abschluss_2030": rv._ist_jahresrechnung, "Buchungsjournal_2030": rv._ist_hauptbuch}
    f += [f"Name {n} nicht erkannt" for n, fn in namen.items() if not fn(n)]
    f += [f"Name {n} fälschlich erkannt" for n, fn in {"Saldobestaetigung_Bank_2030": rv._ist_saldoliste, "Abschlussbuchungen_2030":
                                                       rv._ist_jahresrechnung, "Anhang_Mietvertrag": rv._ist_jahresrechnung}.items() if fn(n)]
    if rv._pf_zu_namen("Offene_Posten_Kunden_31.12.2030")[0][:1] != ["C1"] or "B1" in rv._pf_zu_namen("Offene_Posten_Lieferanten")[0]:
        f.append("«Offene Posten» → B1 statt C1/K1")
    return f


@fall("plan generisch: Schrägstrich im Prüffeldnamen, ohne VJ keine Platzhalter, `aufgabe \"…\"` eindeutig, Code-Spans ausgeglichen")
def _plan_generisch():
    import json
    f = []
    p = json.loads(rv.plan("Prozess 2 – Bereite das Prüffeld Vorräte/Angefangene Arbeiten vor."))
    if p["prueffelder"] != ["F1", "F2"]:
        f.append(f"Vorräte/Angefangene Arbeiten → {p['prueffelder']}")
    if "(GV und VR)" not in rv._plan_route("Welche Protokolle (GV/VR) liegen vor? Akte: a/b-2030", "a/b-2030", None):
        f.append("(GV/VR) im Routing-Text entstellt")
    for auftrag in ("Starte das Mandat.", "Prüffeld C1 vorbereiten", "Prozess 3 – Welche \"Protokolle\" liegen vor?"):
        p = json.loads(rv.plan(auftrag, str(AKTE_GJ)) if AKTE_GJ.is_dir() else rv.plan(auftrag))
        for t in p["turns"]:
            txt = t["anweisung"] + json.dumps(t["aufrufe"], ensure_ascii=False)
            if re.search(r"<(?:vj-)?pfad>", txt):
                f.append(f"{auftrag!r} Turn {t['nr']}: Platzhalter")
            if t["anweisung"].count("`") % 2:
                f.append(f"{auftrag!r} Turn {t['nr']}: Backticks ungerade")
            if re.search(r"`aufgabe (?!\")", t["anweisung"]) or any(re.match(r"aufgabe (?!\")", c) for c in t["aufrufe"]):
                f.append(f"{auftrag!r} Turn {t['nr']}: aufgabe ohne Anführungszeichen")
            for c in t["aufrufe"]:
                if c.startswith("aufgabe ") and c.count('"') != 2:
                    f.append(f"{auftrag!r} Turn {t['nr']}: Aufruf mit Anführungszeichen im Text: {c[:60]}")
    if rv.cut_code("Rechne `a + b` und dann `rechne \"x = 1\"` weiter", 30).count("`") % 2:
        f.append("cut_code lässt einen Code-Span offen")
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
