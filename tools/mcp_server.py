#!/usr/bin/env python3
"""MCP-Server (stdio, JSON-RPC 2.0) für das Steuer-Wiki – stellt tools/steuer.py als Agent-Tools bereit.

Nur Python-Standardbibliothek. Start: python3 tools/mcp_server.py (wird vom Plugin über .mcp.json gestartet).
In OpenClaw heissen die Tools <server>__<tool>, z.B. steuerwiki__wert.
"""
from __future__ import annotations
import json, sys, traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import steuer  # noqa: E402

S = {"type": "string"}
TOOLS = [
    {"name": "wert", "fn": lambda a: steuer.wert(a["jur"], a["jahr"], a["begriff"]),
     "description": "Eckwerte/Limiten/Pauschalen (z.B. Fahrkosten-Maximum, Säule 3a, Versicherungsabzug) für EINE Jurisdiktion und EIN Steuerjahr, "
                    "mit Fundstelle und Status. Bei Kantonen kommt der Bundeswert automatisch mit. Zuerst dieses Tool für jede Zahlenfrage.",
     "inputSchema": {"type": "object", "properties": {"jur": {**S, "description": "bund, zh, sg, tg oder ar"},
                                                      "jahr": {**S, "description": "Steuerjahr, z.B. 2025"},
                                                      "begriff": {**S, "description": "Stichwort, z.B. fahrkosten, verpflegung, saeule3a, kinderabzug"}},
                     "required": ["jur", "jahr", "begriff"]}},
    {"name": "vergleich", "fn": lambda a: steuer.vergleich(a["begriff"], a["jahr"]),
     "description": "Vergleich: Eckwerte von Bund, ZH, SG, TG, AR nebeneinander für ein Steuerjahr (z.B. welcher Kanton hat den höchsten "
                    "Versicherungsabzug). Für Vergleichs- und Rangfolgefragen statt mehrerer wert-Aufrufe.",
     "inputSchema": {"type": "object", "properties": {"jahr": S, "begriff": S}, "required": ["jahr", "begriff"]}},
    {"name": "position", "fn": lambda a: steuer.position(a["kanton"], a["jahr"], a["ziffer_oder_begriff"]),
     "description": "Formularposition (Ziffer/Code des amtlichen Formulars) eines Kantons: welche Belege rein, wie rechnen, Limite Kanton/Bund, "
                    "Beachten, Belege, Fundstelle. Mit Ziffer (z.B. 11.1, 16.2) oder Stichwort (z.B. Kinderbetreuung).",
     "inputSchema": {"type": "object", "properties": {"kanton": {**S, "description": "zh, sg, tg oder ar"}, "jahr": S,
                                                      "ziffer_oder_begriff": S}, "required": ["kanton", "jahr", "ziffer_oder_begriff"]}},
    {"name": "formular", "fn": lambda a: steuer.formular(a["kanton"], a["jahr"]),
     "description": "Ganze Steuererklärung eines Kantons: ALLE Positionen in Formularreihenfolge (Einkünfte → Abzüge → Nettoeinkommen → "
                    "Abzüge auf Basis Nettoeinkommen → Sozialabzüge → steuerbares Einkommen → Vermögen) mit Limiten Kanton|Bund, "
                    "Hilfsblätter und Standardabzüge nach Haushalt (Ehepaar, Kinder, Erwerbstätige). Zuerst aufrufen bei kompletten Fällen.",
     "inputSchema": {"type": "object", "properties": {"kanton": {**S, "description": "zh, sg, tg oder ar"}, "jahr": S},
                     "required": ["kanton", "jahr"]}},
    {"name": "rechne", "fn": lambda a: steuer.rechne(a["ausdruck"]),
     "description": "Rechnet exakt statt im Kopf: Summen, Differenzen, Prozent, min/max (z.B. \"6'800 + 1'100 + 2*1'100; "
                    "min(27'300; 25'000); 3% * 103'000\"). Mehrere Rechnungen mit ; trennen, optional «Name = Ausdruck». "
                    "Jede Summe, jedes Total und jede Limite-Anwendung damit prüfen.",
     "inputSchema": {"type": "object", "properties": {"ausdruck": S}, "required": ["ausdruck"]}},
    {"name": "beleg", "fn": lambda a: steuer.beleg(a["begriff"], a.get("kanton"), a.get("jahr")),
     "description": "Belegkarte zu einem Dokumenttyp (z.B. Lohnausweis, Steuerauszug, Kita-Rechnung): steuerrelevant?, Werte entnehmen, "
                    "vom Dokument in die Steuererklärung: Feld → Position (Ziffer/Code) → Rechnen → Limite Kanton/Bund; Einreichepflicht (mit Zitat).",
     "inputSchema": {"type": "object", "properties": {"begriff": S, "kanton": S, "jahr": S}, "required": ["begriff"]}},
    {"name": "ablage", "fn": lambda a: steuer.ablage(a["text"], a.get("kanton"), a.get("jahr")),
     "description": "Eingegangenes Dokument einordnen (Titel/Text): Dokumenttyp (Top 3), steuerrelevant?, Steuerjahr, "
                    "Einreichepflicht im Kanton, Sicherheit der Erkennung. Kategorie danach aus der Kategorienliste (KATEGORIEN.md) wählen.",
     "inputSchema": {"type": "object", "properties": {"text": {**S, "description": "Titel und/oder (OCR-)Text des Dokuments"},
                                                      "kanton": S, "jahr": S}, "required": ["text"]}},
    {"name": "suche", "fn": lambda a: steuer.suche(a["query"], a.get("jur"), a.get("jahr"), a.get("typ"), int(a.get("n") or 8)),
     "description": "Volltextsuche über alle amtlichen Quellen-Chunks (Gesetze, Wegleitungen, Merkblätter, Formulare). Für Fragen, "
                    "die wert/position/beleg nicht beantworten. jur IMMER auf den Kanton der Frage setzen (bund für Bundesrecht), jahr setzen.",
     "inputSchema": {"type": "object", "properties": {"query": S, "jur": S, "jahr": S, "typ": S, "n": {"type": "integer"}},
                     "required": ["query"]}},
    {"name": "zeige", "fn": lambda a: steuer.zeige(a["ref"], a.get("abschnitt")),
     "description": "Zeigt einen Chunk (ID wie zh-wl-2025__c0065) im Wortlaut oder eine Wiki-Seite (Pfad wie quick/werte-zh-2025.md), "
                    "optional nur einen Abschnitt.",
     "inputSchema": {"type": "object", "properties": {"ref": S, "abschnitt": S}, "required": ["ref"]}},
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
                "serverInfo": {"name": "steuerwiki", "version": "1.0.0"},
                "instructions": "Steuer-Wiki Schweiz (Bund, AR, SG, TG, ZH; 2025/2026). Dokumente: ablage/beleg; Ausfüllen: "
                                "formular (ganzer Fall)/position/wert/vergleich; sonst suche → zeige. Immer Kanton und Steuerjahr angeben."}})
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
            except Exception as e:  # Fehler als Tool-Ergebnis zurückgeben, damit der Agent reagieren kann
                send({"jsonrpc": "2.0", "id": i, "result": {"content": [{"type": "text", "text": f"Fehler: {e}\n{traceback.format_exc(limit=2)}"}],
                                                            "isError": True}})
        elif meth == "ping":
            send({"jsonrpc": "2.0", "id": i, "result": {}})
        elif i is not None and not str(meth).startswith("notifications/"):
            send({"jsonrpc": "2.0", "id": i, "error": {"code": -32601, "message": f"Methode {meth} nicht unterstützt"}})


if __name__ == "__main__":
    main()
