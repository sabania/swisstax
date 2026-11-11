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


TOOLS = [
    {"name": "aufgabe", "fn": lambda a: rv.aufgabe(a.get("aufgabe") or None),
     "description": "IMMER ZUERST AUFRUFEN. Liefert zu einer Aufgabe in EINEM Aufruf alles Nötige: Ziel, Regeln, Checkliste mit den genauen "
                    "nächsten Aufrufen, revio-Werkzeugkette, Fertig-wenn, nächste Aufgabe. Eingabe: Aufgabe in eigenen Worten oder id "
                    "(mandat-start, import, prueffeld, unterlagen, rapport, gvb-bericht, pdf-akte, notiz, wesentlichkeit, kapitalschutz, "
                    "vorjahresabstimmung, delkredere, sachanlagen, abschluss, auftrag, fachfrage) oder direkt ein Prüffeld (C1) bzw. "
                    "einen Prüfschritt (C1-302). Ohne Eingabe: Liste aller Aufgaben.",
     "inputSchema": obj({"aufgabe": {**S, "description": "z.B. «Prüffeld C1 vorbereiten», «Rapport schreiben», «kapitalschutz», «C1-302»"}}, [])},
    {"name": "pruefschritt", "fn": lambda a: rv.pruefschritt(a["id"]),
     "description": "Ein Prüfschritt des revio-4.0-Katalogs (z.B. C1-302): Katalogtext, Typ, EP/WP, Prüfziele, Rolle des Agenten (vorbereiten / "
                    "teilweise / nur auf Anweisung / nur Mensch), konkretes Vorgehen, Nachweise, Rechenregel, wann Notiz/Feststellung, "
                    "Fundstellen (SER/HWP/OR) und passende revio-MCP-Werkzeuge. Für JEDEN Prüfschritt zuerst dieses Tool.",
     "inputSchema": obj({"id": {**S, "description": "Schritt-Id, z.B. C1-302, A1-101, SCH4-201"}}, ["id"])},
    {"name": "prueffeld", "fn": lambda a: rv.prueffeld(a["prueffeld"], bool(a.get("voll"))),
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
     "description": "Verbindliche Arbeitsregeln des Agenten mit Fundstelle: schritttyp (Befragung/Analytisch/Detail/Sonstige/WP), ablauf (je "
                    "Prüfschritt, Textfeld, Mandatskontext), notizen (Pendenz, Wesentliche Feststellungen, Schlussbesprechung), grenze "
                    "(nie Visum/Abschluss/Freigabe/Versand), wesentlichkeit, gesetz (OR-Kernregeln).",
     "inputSchema": obj({"bereich": S}, [])},
    {"name": "revio", "fn": lambda a: rv.revio(a.get("frage") or None),
     "description": "Welches revio-MCP-Werkzeug wann: Bereich (z.B. 10.9, 3.3, 4), Prüffeld (C1), Prüfschritt (C1-302), Aufgabe/Stichwort "
                    "(notiz, beilage, wesentlichkeit, saldenbilanz), Werkzeugketten (ketten, K1…), ein Werkzeugname (Art, Pfad, Parameter, "
                    "Body-Felder) oder nur-mensch (gesperrte Werkzeuge). Nie gesperrte Werkzeuge aufrufen.",
     "inputSchema": obj({"frage": S}, [])},
    {"name": "wert", "fn": lambda a: rv.wert(a["begriff"]),
     "description": "Schwellenwerte, Sätze, Fristen mit Fundstelle (z.B. revisionspflicht, kapitalverlust, reserven, aufbewahrung, "
                    "zinssatz darlehen aktionär 2026, verdecktes eigenkapital, delkredere, mwst, wesentlichkeit).",
     "inputSchema": obj({"begriff": S}, ["begriff"])},
    {"name": "rechne", "fn": lambda a: rv.rechne(a["ausdruck"]),
     "description": "Rechnet exakt statt im Kopf (Summen, Abstimmungen, Differenzen, %, min/max). Mehrere Rechnungen mit ; trennen, optional "
                    "«Name = Ausdruck». Jede Abstimmung (OP-Liste = Saldo, Bilanzgleichheit, Vorjahresdifferenz, Delkredere) damit.",
     "inputSchema": obj({"ausdruck": S}, ["ausdruck"])},
    {"name": "wesentlichkeit", "fn": lambda a: rv.wesentlichkeit(a["bezugsgroesse"], a["satz"], a.get("toleranz", 75), a.get("nichtaufgriff", 5), a.get("bezeichnung") or "Bezugsgrösse"),
     "description": "Plausibilisiert die Wesentlichkeit (revio 3.3): Gesamt-, Toleranz- (75 %) und Nichtaufgriffsgrenze (5 %) aus Bezugsgrösse "
                    "und Prozentsatz, mit Anwendungsregeln. Der Agent ändert 3.3 nie.",
     "inputSchema": obj({"bezugsgroesse": N, "satz": {**N, "description": "Prozent, z.B. 1 oder 5"}, "toleranz": N, "nichtaufgriff": N, "bezeichnung": S}, ["bezugsgroesse", "satz"])},
    {"name": "kapitalverlust", "fn": lambda a: rv.kapitalverlust(a["aktiven"], a["verbindlichkeiten"], a["aktienkapital"], a.get("kapitalreserve", 0), a.get("gewinnreserve", 0), a.get("rangruecktritt", 0)),
     "description": "Rechenhilfe OR 725a/725b: Kapitalverlust (Hälfte-Test), Überschuldung zu Buchwerten, Deckung durch Rangrücktritt; mit Gesetzeszitaten. Beurteilung durch den WP.",
     "inputSchema": obj({"aktiven": N, "verbindlichkeiten": N, "aktienkapital": N, "kapitalreserve": N, "gewinnreserve": N, "rangruecktritt": N},
                        ["aktiven", "verbindlichkeiten", "aktienkapital"])},
    {"name": "revisionspflicht", "fn": lambda a: rv.revisionspflicht(a["bilanzsumme"], a["umsatz"], a["vollzeitstellen"], a.get("vj_bilanzsumme"), a.get("vj_umsatz"), a.get("vj_vollzeitstellen")),
     "description": "Rechenhilfe OR 727/727a: ordentliche oder eingeschränkte Revision, Opting-out (≤ 10 Vollzeitstellen). Mit Vorjahreswerten.",
     "inputSchema": obj({"bilanzsumme": N, "umsatz": N, "vollzeitstellen": N, "vj_bilanzsumme": N, "vj_umsatz": N, "vj_vollzeitstellen": N},
                        ["bilanzsumme", "umsatz", "vollzeitstellen"])},
    {"name": "unterlagen", "fn": lambda a: rv.unterlagen(a.get("prueffeld") or None),
     "description": "PBC-Unterlagen je Prüffeld (oder alle): was der Agent in M-Files sucht bzw. als PBC-Vorschlag (10.10)/Pendenz erfasst.",
     "inputSchema": obj({"prueffeld": S}, [])},
    {"name": "fragen", "fn": lambda a: rv.fragen(a.get("prueffeld") or None),
     "description": "Fragen an den Kunden je Prüffeld (oder alle) – der Agent befragt nie selbst: Antwort aus 10.11/Protokollen auswerten, sonst Pendenz.",
     "inputSchema": obj({"prueffeld": S}, [])},
    {"name": "thema", "fn": lambda a: rv.thema(a["begriff"]),
     "description": "Themenseite mit Zitaten (z.B. Rangrücktritt, Hinweispflichten, Unabhängigkeit, Vollständigkeitserklärung, nahestehende "
                    "Personen, stille Reserven, Going Concern, Ereignisse nach dem Bilanzstichtag, Delkredere, verdecktes Eigenkapital).",
     "inputSchema": obj({"begriff": S}, ["begriff"])},
    {"name": "suche", "fn": lambda a: rv.suche(a["query"], a.get("quelle"), a.get("typ"), int(a.get("n") or 8)),
     "description": "Volltextsuche in allen Quellen (OR, SER, HWP ER, HWP BuR, Q&A, Muster, ESTV, Fachliteratur, Konzept). quelle = Präfix "
                    "(or, ser-2022, ser-2022__anh-d, hwp-er-2026, hwp-bur-2023, qa-kapitalverlust, muster-hwp-er-2026, estv, konzept). "
                    "Für Fragen, die die anderen Tools nicht beantworten; danach zeige.",
     "inputSchema": obj({"query": S, "quelle": S, "typ": S, "n": {"type": "integer"}}, ["query"])},
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
                "instructions": "Revisions-Wiki (eingeschränkte Revision CH, revio 4.0). IMMER ZUERST `aufgabe` mit der Aufgabe in eigenen Worten – "
                                "die Antwort nennt die nächsten Aufrufe (pruefschritt, revio, rechne …). Fachfrage: thema/wert/suche → zeige. "
                                "Agent bereitet nur vor (nie Visum/Abschluss/Freigabe/Versand)."}})
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
            except Exception as e:
                send({"jsonrpc": "2.0", "id": i, "result": {"content": [{"type": "text", "text": f"Fehler: {e}\n{traceback.format_exc(limit=2)}"}],
                                                            "isError": True}})
        elif meth == "ping":
            send({"jsonrpc": "2.0", "id": i, "result": {}})
        elif i is not None and not str(meth).startswith("notifications/"):
            send({"jsonrpc": "2.0", "id": i, "error": {"code": -32601, "message": f"Methode {meth} nicht unterstützt"}})


if __name__ == "__main__":
    main()
