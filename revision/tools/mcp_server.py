#!/usr/bin/env python3
"""MCP-Server (stdio, JSON-RPC 2.0) für das Revisions-Wiki – stellt tools/revision.py als Agent-Tools bereit.

Nur Python-Standardbibliothek. Start: python3 tools/mcp_server.py (wird vom Plugin über .mcp.json gestartet).
OpenClaw: Tools heissen revisionswiki__<tool>; Claude Code: mcp__plugin_revisionswiki_revisionswiki__<tool>.
"""
from __future__ import annotations
import json, sys, traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import revision as rv  # noqa: E402

S = {"type": "string"}
N = {"type": ["number", "string"]}


def obj(props: dict, req: list) -> dict:
    return {"type": "object", "properties": props, "required": req}


def ja(v) -> bool:
    """Wahrheitswert aus JSON (true/false) oder Text («false» ist falsch, nicht wahr wie bei bool("false"))."""
    if isinstance(v, str):
        return v.strip().lower() in ("1", "true", "ja", "yes", "wahr", "y", "j")
    return bool(v)


def ganz(v, was: str, std: int | None = None) -> int | None:
    """Ganze Zahl aus JSON oder Text mit deutscher Fehlermeldung (statt «invalid literal for int()»)."""
    if v in (None, ""):
        return std
    if isinstance(v, bool):
        raise ValueError(f"{was}: ganze Zahl erwartet, z.B. 401")
    if isinstance(v, (int, float)) and float(v).is_integer():
        return int(v)
    t = str(v).strip().replace("'", "").replace("’", "")
    if t.lstrip("-").isdigit():
        return int(t)
    raise ValueError(f"{was}: ganze Zahl erwartet, z.B. 401 (erhalten: {v!r})")


TOOLS = [
    {"name": "aufgabe", "fn": lambda a: rv.aufgabe(a.get("aufgabe") or None),
     "description": "IMMER ZUERST AUFRUFEN. Liefert zu einer Aufgabe oder Frage in EINEM Aufruf alles Nötige: Ziel, Grenze, Regeln, Checkliste mit den "
                    "genauen nächsten Aufrufen, revio-Werkzeugketten, Fertig-wenn, nächste Aufgabe; bei Fachfragen Themen, Regeln und Fundstellen. "
                    "Eingabe: Aufgabe/Frage in eigenen Worten oder id "
                    "(mandat-start, import, prueffeld, unterlagen, rapport, gvb-bericht, pdf-akte, notiz, wesentlichkeit, kapitalschutz, "
                    "vorjahresabstimmung, delkredere, sachanlagen, abschluss, auftrag, fachfrage) oder direkt ein Prüffeld (C1; mehrere: "
                    "«D1 und H3», «L1/N1») bzw. einen Prüfschritt (C1-302). Mehrere Prüffelder: alle Bündel nacheinander + eine Statustabelle. "
                    "Ohne Eingabe: Liste aller Aufgaben. Bei Prüffeld-Aufträgen danach `akte` (Mandantenordner erschliessen).",
     "inputSchema": obj({"aufgabe": {**S, "description": "z.B. «Prüffeld C1 vorbereiten», «Rapport schreiben», «kapitalschutz», «C1-302»"}}, [])},
    {"name": "pruefschritt", "fn": lambda a: rv.pruefschritt(a["id"]),
     "description": "Ein Prüfschritt des revio-4.0-Katalogs (z.B. C1-302): Katalogtext, Typ, EP/WP, Prüfziele, Rolle des Agenten (vorbereiten / "
                    "teilweise / nur auf Anweisung / nur Mensch), konkretes Vorgehen, Nachweise, Rechenregel, wann Notiz/Feststellung, "
                    "Fundstellen (SER/HWP/OR) und passende revio-MCP-Werkzeuge. Für jeden vorbereitbaren Schritt (1xx–3xx) einzeln aufrufen. "
                    "Mehrere Ids in einem Aufruf (z.B. «C1-401 C1-402 C1-403») = Sammelaufruf: 4xx- und WP-Schritte als kurze Karten "
                    "(so steht es im Bündel von `aufgabe`).",
     "inputSchema": obj({"id": {**S, "description": "Schritt-Id, z.B. C1-302, A1-101, SCH4-201; mehrere mit Leerzeichen/Komma getrennt"}}, ["id"])},
    {"name": "prueffeld", "fn": lambda a: rv.prueffeld(a["prueffeld"], ja(a.get("voll"))),
     "description": "Überblick eines Prüffelds (A1 … T1 oder Stichwort wie «Vorräte», «MWST», «Eigenkapital»): Risiken, Bewertungsregeln, "
                    "Unterlagen (PBC), Fragen an den Kunden, Fallstricke, alle Prüfschritte mit Rolle des Agenten, revio-Werkzeuge.",
     "inputSchema": obj({"prueffeld": S, "voll": {"type": "boolean", "description": "Schritttexte ungekürzt"}}, ["prueffeld"])},
    {"name": "prozess", "fn": lambda a: rv.prozess(a.get("phase") or None),
     "description": "Prozess der eingeschränkten Revision (kein starrer Ablauf): ohne Phase Übersicht p1–p8 inkl. Agent-Prozesse 1–6; mit Phase "
                    "(p1 Auftrag/Unabhängigkeit, p2 Planung/Wesentlichkeit, p3 Durchführung, p4 Beendigung/VE, p5 Bericht/Hinweise, "
                    "p6 Kapitalverlust/Überschuldung, p7 Qualität/Dokumentation/Datenschutz, p8 Agent-Ablauf) was nötig ist, WP-Entscheide, "
                    "Kundenfragen, Unterlagen, Muster, Fundstellen.",
     "inputSchema": obj({"phase": {**S, "description": "z.B. p2 oder Stichwort (bericht, rangrücktritt)"}}, [])},
    {"name": "regeln", "fn": lambda a: rv.regeln(a.get("bereich") or None),
     "description": "Verbindliche Arbeitsregeln des Agenten mit Fundstelle (Grenzen gehen vor). Ohne Bereich: alle Arbeitsregeln ohne gesetz. "
                    "Bereiche: grenze (nie Visum/Abschluss/Freigabe/Versand/Buchung; Vorjahr nur lesen; Mandatsdaten nur in freigegebenen "
                    "Systemen; nichts erfinden), schritttyp (Befragung/Analytisch/Detail/Sonstige/WP), ablauf (je Prüfschritt, Textfeld, "
                    "Mandatskontext), notizen (Pendenz, Wesentliche Feststellungen, Schlussbesprechung), wesentlichkeit, gesetz (OR-Kernregeln). "
                    "Auch ein Regelschlüssel oder Stichwort (z.B. vorjahr, datenschutz).",
     "inputSchema": obj({"bereich": S}, [])},
    {"name": "revio", "fn": lambda a: rv.revio(a.get("frage") or None),
     "description": "Welches revio-MCP-Werkzeug wann: Bereich (z.B. 10.9, 3.3, 4), Prüffeld (prueffeld C1), Prüfschritt (C1-302), Aufgabe/Stichwort "
                    "(notiz, beilage, wesentlichkeit, saldenbilanz), Werkzeugketten (ketten, K1…), ein Werkzeugname (Art, Pfad, Parameter, "
                    "Body-Felder) oder nur-mensch (gesperrte Werkzeuge). ⛔ = deny: nie aufrufen, auch nicht über revio_call.",
     "inputSchema": obj({"frage": S}, [])},
    {"name": "wert", "fn": lambda a: rv.wert(a["begriff"]),
     "description": "Schwellenwerte, Sätze, Fristen mit Fundstelle (z.B. revisionspflicht, kapitalverlust, reserven, aufbewahrung, "
                    "zinssatz darlehen aktionär 2026, verdecktes eigenkapital, delkredere, mwst, wesentlichkeit).",
     "inputSchema": obj({"begriff": S}, ["begriff"])},
    {"name": "rechne", "fn": lambda a: rv.rechne(a["ausdruck"]),
     "description": "Rechnet exakt statt im Kopf (Summen, Abstimmungen, Differenzen, %, min/max/abs/sum; round kaufmännisch, runden5 = auf "
                    "5 Rappen). Mehrere Rechnungen mit ; oder Zeilenumbruch; «name = Ausdruck» – Namen ohne Leerzeichen gelten in den "
                    "folgenden Teilen, z.B. «op = 1200; hb = 1500; hb - op». Datum TT.MM.JJJJ (JJJJ-MM-TT nur direkt in der Funktion): "
                    "tage(später, früher) (Tage), tage360(später, früher) (30E/360), monate(später, früher) (ganze Monate), "
                    "datum_plus(datum, jahre=6) (Fristende). Minus als -. "
                    "Jede Abstimmung (OP-Liste = Saldo, Bilanzgleichheit, Vorjahresdifferenz, Delkredere, Marchzins, Fälligkeit) damit.",
     "inputSchema": obj({"ausdruck": {**S, "description": "z.B. «a = 1200; b = 300; a - b» oder «tage(31.12.2025, 15.10.2025)»"}}, ["ausdruck"])},
    {"name": "wesentlichkeit", "fn": lambda a: rv.wesentlichkeit(a.get("bezugsgroesse"), a.get("satz"), a.get("toleranz"), a.get("nichtaufgriff"), a.get("bezeichnung") or "Bezugsgrösse", a.get("gesamt")),
     "description": "Wesentlichkeit: aus Gesamtwesentlichkeit (gesamt) ODER Bezugsgrösse × Satz → Toleranzwesentlichkeit (HWP ER 50–75 %), "
                    "Nichtaufgriffsgrenze (bis 5 %), mit Herkunft je Wert, Regeln, Richtwerten und Fundstellen. toleranz/nichtaufgriff wie in "
                    "revio 3.3 in % oder CHF; leer = Konzept-Standard 75 %/5 % (wird als «nicht aus 3.3» gekennzeichnet). Ohne gesamt bzw. "
                    "bezugsgroesse+satz: Aufrufhilfe. Der Agent ändert revio 3.3 nie.",
     "inputSchema": obj({"gesamt": {**N, "description": "Gesamtwesentlichkeit in CHF, falls bekannt (z.B. 50000)"},
                         "bezugsgroesse": {**N, "description": "Bezugsgrösse in CHF (z.B. Umsatz 5000000), nur ohne gesamt"},
                         "satz": {**N, "description": "Prozentsatz zur Bezugsgrösse, z.B. 1"},
                         "toleranz": {**N, "description": "Wert aus 3.3 in % (z.B. 75) oder CHF (z.B. 37500)"},
                         "nichtaufgriff": {**N, "description": "Wert aus 3.3 in % (z.B. 5) oder CHF (z.B. 2500)"}, "bezeichnung": S}, [])},
    {"name": "kapitalverlust", "fn": lambda a: rv.kapitalverlust(a["aktienkapital"], a.get("eigenkapital"), a.get("aktiven"), a.get("verbindlichkeiten"),
                                                                 a.get("kapitalreserve", 0), a.get("gewinnreserve", 0), ja(a.get("holding", False)),
                                                                 a.get("rangruecktritt", 0), a.get("buchwert"), a.get("verkehrswert"),
                                                                 a.get("freiwillige_reserven"), a.get("vortrag"), a.get("jahresergebnis"), a.get("eigene_aktien"),
                                                                 a.get("reserve_voll", 0), a.get("covid_kredit", 0)),
     "description": "Rechenhilfe Kapitalschutz OR 725a/725b/725c: geschütztes Kapital (gesetzliche Reserven höchstens 50 % bzw. Holding 20 % des "
                    "Aktienkapitals), Kapitalverlust (Hälfte-Test), Überschuldung, Rangrücktritt, zulässige Aufwertung (mit buchwert + verkehrswert). "
                    "Eigenkapital direkt ODER aus Bestandteilen (freiwillige_reserven, vortrag, jahresergebnis – Verluste negativ –, eigene_aktien) "
                    "ODER aktiven + verbindlichkeiten. reserve_voll = Gewinnreserven für eigene Kapitalanteile im Konzern/Aufwertungsreserve (zählen "
                    "voll zum geschützten Kapital); covid_kredit = Kredit nach Art. 3 Covid-19-SBüV bzw. Art. 21 HFMV 20 (kein Fremdkapital). "
                    "Alle Beträge in CHF. Mit Gesetzes-/HWP-Zitaten. "
                    "Beurteilung: WP.",
     "inputSchema": obj({"aktienkapital": {**N, "description": "Aktien- und PS-Kapital in CHF"}, "eigenkapital": {**N, "description": "bilanzielles Eigenkapital in CHF (inkl. Verluste, eigene Aktien)"},
                         "aktiven": N, "verbindlichkeiten": {**N, "description": "Fremdkapital inkl. Rückstellungen"},
                         "kapitalreserve": {**N, "description": "gesetzliche Kapitalreserve (z.B. Agio)"},
                         "gewinnreserve": {**N, "description": "nur gesetzliche Gewinnreserve i.e.S. (OR 672 Abs. 1) – ohne Aufwertungsreserve und Reserve für "
                                                               "eigene Kapitalanteile (diese in reserve_voll)"},
                         "freiwillige_reserven": N, "vortrag": {**N, "description": "Gewinn-/Verlustvortrag (Verlust negativ)"},
                         "jahresergebnis": {**N, "description": "Jahresgewinn/-verlust (Verlust negativ)"}, "eigene_aktien": {**N, "description": "Betrag eigene Aktien (wird abgezogen)"},
                         "holding": {"type": "boolean"}, "rangruecktritt": N, "buchwert": {**N, "description": "Buchwert Grundstück/Beteiligung (für Aufwertung)"},
                         "verkehrswert": {**N, "description": "wirklicher Wert/Netto-Marktwert (für Aufwertung)"},
                         "reserve_voll": {**N, "description": "gesetzl. Gewinnreserven für eigene Kapitalanteile im Konzern (OR 659b Abs. 2) und Aufwertungsreserve "
                                                             "(OR 725c) – ohne 50-%-Grenze; nicht zusätzlich in gewinnreserve"},
                         "covid_kredit": {**N, "description": "nur der nach Art. 3 Covid-19-SBüV verbürgte Kredit bzw. Darlehen/Kredit nach Art. 21 HFMV 20: "
                                                              "kein Fremdkapital (Art. 24 Covid-19-SBüG; HWP ER Rz 373); andere Kredite bleiben "
                                                              "Fremdkapital; verbindlichkeiten wie in der Bilanz eingeben"}},
                        ["aktienkapital"])},
    {"name": "revisionspflicht", "fn": lambda a: rv.revisionspflicht(a["bilanzsumme"], a["umsatz"], a["vollzeitstellen"], a.get("vj_bilanzsumme"), a.get("vj_umsatz"), a.get("vj_vollzeitstellen")),
     "description": "Rechenhilfe OR 727/727a: ordentliche oder eingeschränkte Revision nach Grössen (Bilanzsumme, Umsatz in CHF, Vollzeitstellen; "
                    "Berichts- und Vorjahr), Opting-out. NUR für die Revisionsart – nicht für Kapitalverlust (dafür kapitalverlust).",
     "inputSchema": obj({"bilanzsumme": {**N, "description": "in CHF, z.B. 22000000"}, "umsatz": {**N, "description": "Umsatzerlös in CHF"}, "vollzeitstellen": N,
                         "vj_bilanzsumme": N, "vj_umsatz": N, "vj_vollzeitstellen": N}, ["bilanzsumme", "umsatz", "vollzeitstellen"])},
    {"name": "unterlagen", "fn": lambda a: rv.unterlagen(a.get("prueffeld") or None),
     "description": "PBC-Unterlagen eines Prüffelds (z.B. C1): was der Agent in M-Files sucht; Fehlendes als Pendenz «PBC-Vorschlag». Ohne Prüffeld: Übersicht.",
     "inputSchema": obj({"prueffeld": S}, [])},
    {"name": "fragen", "fn": lambda a: rv.fragen(a.get("prueffeld") or None),
     "description": "Fragen an den Kunden eines Prüffelds (z.B. C1) – der Agent befragt nie selbst: Antwort aus 10.11/Protokollen auswerten, sonst Pendenz. "
                    "Ohne Prüffeld: Übersicht.",
     "inputSchema": obj({"prueffeld": S}, [])},
    {"name": "thema", "fn": lambda a: rv.thema(a["begriff"], ja(a.get("voll"))),
     "description": "Themenseite: zuerst «Für den Agenten» (Vorgehen, nummeriert) und «Nächste Aufrufe», dann Fundstellen (gekürzt, je mit "
                    "^[chunk-id]). Themen z.B. Rangrücktritt, Kapitalverlust, Hinweispflichten, Unabhängigkeit, Vollständigkeitserklärung, "
                    "nahestehende Personen, stille Reserven, Going Concern, Ereignisse nach dem Bilanzstichtag, Delkredere, verdecktes Eigenkapital, "
                    "MWST/Sozialversicherungen. voll=true: alle Aussagen ungekürzt.",
     "inputSchema": obj({"begriff": S, "voll": {"type": "boolean", "description": "true = alle Aussagen ungekürzt"}}, ["begriff"])},
    {"name": "suche", "fn": lambda a: rv.suche(a["query"], a.get("quelle"), a.get("typ"), ganz(a.get("n"), "n", 8)),
     "description": "Volltextsuche in allen Quellen (OR, SER, HWP ER, HWP BuR, Q&A, Muster, ESTV, Fachliteratur, Konzept). quelle = Präfix "
                    "(or, ser-2022, ser-2022__anh-d, hwp-er-2026, hwp-bur-2023, qa-kapitalverlust, muster-hwp-er-2026, estv, konzept, "
                    "rab (Unabhängigkeit, Aufsicht), rag/rav (Zulassung), hregv (Opting-out), gebuev (Aufbewahrung), mwstg/mwstv, vstg/vstv, "
                    "dsg/edoeb (Datenschutz/KI), stgb (Berufsgeheimnis), covid-sbueg, zgb, fusg). "
                    "Für Fragen, die die anderen Tools nicht beantworten; danach zeige.",
     "inputSchema": obj({"query": S, "quelle": S, "typ": S, "n": {"type": "integer"}}, ["query"])},
    {"name": "akte", "fn": lambda a: rv.akte(a["pfad"], a.get("vj"), a.get("pf"), a.get("suche"), a.get("datei"), ganz(a.get("von"), "von"),
                                             ganz(a.get("bis"), "bis"), a.get("inhalt"), a.get("abschnitt"), a.get("ueberschrift"),
                                             ganz(a.get("n"), "n", 40)),
     "description": "Mandantenakte (Ordner mit .md/.txt/.csv; andere Dateien nur gelistet) erschliessen – NUR LESEN, nichts wird gespeichert. "
                    "Nur pfad: Baum mit Zeilen/KB und vermutetem Prüffeld je Ordner/Datei. pf (z.B. C1): Dateien des Prüffelds, Treffer in "
                    "Saldoliste/Hauptbuch/Jahresrechnung und in Ordnern anderer Prüffelder (Datei:Zeile), Unterlagen → Fundort. suche: "
                    "Volltext über GJ (und vj), «a|b» = a oder b, Zahlen als ganzes Token (4711 ≠ 47110). inhalt (Datei): Überschriften, "
                    "Gliederung, Seiten mit Zeilennummern. abschnitt (Datei) + ueberschrift: Text bis zur nächsten gleichrangigen Überschrift. "
                    "datei + von/bis: Zeilen mit Nummern (höchstens 400). Grosse Dateien (> 30 KB) so lesen statt mit read. «fehlt» erst "
                    "nach suche in GJ und VJ. Pfad absolut, relativ zum Arbeitsordner oder zum OpenClaw-Workspace.",
     "inputSchema": obj({"pfad": {**S, "description": "Ordner der Akte (Geschäftsjahr), Pfad wie im Auftrag genannt"},
                         "vj": {**S, "description": "Ordner der Vorjahresakte (bei Übersicht, pf und suche mitgelesen)"},
                         "pf": {**S, "description": "Prüffeld-Code, z.B. C1"},
                         "suche": {**S, "description": "z.B. «Protokoll|Generalversammlung|Verwaltungsrat|Zirkular» oder «4711»"},
                         "datei": {**S, "description": "Datei relativ zur Akte (oder eindeutiger Dateiname) – Zeilen lesen"},
                         "von": {"type": ["integer", "string"]}, "bis": {"type": ["integer", "string"]},
                         "inhalt": {**S, "description": "Datei: Inhaltsverzeichnis mit Zeilennummern"},
                         "abschnitt": {**S, "description": "Datei, aus der ein Abschnitt gelesen wird (mit ueberschrift)"},
                         "ueberschrift": {**S, "description": "Überschrift oder Ziffer, z.B. «Anhang», «6», «5.8»"},
                         "n": {"type": "integer", "description": "höchstens n Treffer (Standard 40)"}}, ["pfad"])},
    {"name": "zeige", "fn": lambda a: rv.zeige(a["ref"], a.get("abschnitt")),
     "description": "Wortlaut eines Chunks (Id wie ser-2022__anh-d-s075-1, hwp-er-2026__rz-0113-s060, or__art-725a) oder einer Seite (quick/…md, wiki/…md).",
     "inputSchema": obj({"ref": S, "abschnitt": S}, ["ref"])},
]
BY = {t["name"]: t for t in TOOLS}


def send(o):
    sys.stdout.write(json.dumps(o, ensure_ascii=False) + "\n")
    sys.stdout.flush()


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            m = json.loads(line)
        except json.JSONDecodeError:
            continue
        i, meth, par = m.get("id"), m.get("method"), m.get("params") or {}
        if meth == "initialize":
            send({"jsonrpc": "2.0", "id": i, "result": {
                "protocolVersion": par.get("protocolVersion") or "2025-06-18",
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "revisionswiki", "version": "1.0.0"},
                "instructions": "Revisions-Wiki (eingeschränkte Revision CH, revio 4.0). IMMER ZUERST `aufgabe` mit der Aufgabe oder Frage in eigenen "
                                "Worten – die Antwort nennt die nächsten Aufrufe (akte, pruefschritt, revio, rechne …). Mandantenakte mit `akte` "
                                "erschliessen (grosse Dateien abschnittweise; «fehlt» erst nach `akte … suche`). Agent bereitet nur vor: nie Visum, ✓, "
                                "Abschluss/Status, Freigabe, Buchung, Unterzeichnung, Kundenversand; keine Nachrichten-, Mail- oder Web-Werkzeuge. "
                                "revio-Werkzeuge mit ⛔ (deny) nie aufrufen, auch nicht über revio_call."}})
        elif meth == "tools/list":
            send({"jsonrpc": "2.0", "id": i, "result": {"tools": [{k: t[k] for k in ("name", "description", "inputSchema")} for t in TOOLS]}})
        elif meth == "tools/call":
            t = BY.get(par.get("name"))
            if not t:
                send({"jsonrpc": "2.0", "id": i, "error": {"code": -32602, "message": f"unbekanntes Tool {par.get('name')}"}})
                continue
            try:
                txt = t["fn"](par.get("arguments") or {})
                send({"jsonrpc": "2.0", "id": i, "result": {"content": [{"type": "text", "text": txt}], "isError": False}})
            except (ValueError, KeyError) as e:   # Eingabefehler: kurze Meldung ohne Traceback
                msg = f"Fehler: Pflichtangabe fehlt: {e}" if isinstance(e, KeyError) else f"Fehler: {e}"
                send({"jsonrpc": "2.0", "id": i, "result": {"content": [{"type": "text", "text": msg}], "isError": True}})
            except Exception as e:
                send({"jsonrpc": "2.0", "id": i, "result": {"content": [{"type": "text", "text": f"Fehler: {e}\n{traceback.format_exc(limit=2)}"}],
                                                            "isError": True}})
        elif meth == "ping":
            send({"jsonrpc": "2.0", "id": i, "result": {}})
        elif i is not None and not str(meth).startswith("notifications/"):
            send({"jsonrpc": "2.0", "id": i, "error": {"code": -32601, "message": f"Methode {meth} nicht unterstützt"}})


if __name__ == "__main__":
    main()
