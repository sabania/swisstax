
## [2026-11-13] daten | Endimport, Reviews, Messungen B0/B1, Werkzeug für schwache Modelle
- Endimport: 29 Prüffelder (538 Schritte), 8 Prozessphasen, 216 Werte, 22 Themen, revio-Zuordnung (849 Werkzeuge, 17 Ketten), Referenzlösung Testakte (233 Befunde); Lint 0 Fehler.
- 29 amtliche Quellen strukturiert ergänzt (Fedlex-XML, ESTV/BSV/EDÖB/RAB); Seminar KI-Datenschutz und Flussdiagramm als Abschriften.
- Messung Haiku 4.5 (Ersatz für schwaches lokales Modell): B0 3/18/19 (richtig/teilweise/falsch, Ø 6.1 Aufrufe) → B1 6/30/4 (Ø 3.0).
- Review-Workflows (prüfen → verifizieren → korrigieren) für Aufgaben, revio, Skills umgesetzt; Code-Vorschläge eingebaut (Routing 82/82, Policy allow/approval/deny).

## [2026-11-13] daten | R2 Teil C: E2E-Führung (akte, aufgabe mit mehreren Prüffeldern, Checklisten, OpenClaw-Rechte)
- Neu `akte` (CLI + MCP, nur lesen): Übersicht mit vermutetem Prüffeld je Ordner/Datei, `--pf`, `--suche`, `--inhalt`/`--abschnitt`/`--datei`; generisch (keine Ordnerbuchstaben), auf beiden Testakten und einem synthetischen Schema geprüft.
- `aufgabe`: mehrere Prüffelder im Auftrag (alle Bündel + Statustabelle), Block «Arbeitsregeln Akte», Rollenhinweis 4xx/WP, Werkzeugnamen je revio-Kette, Akte-Pfade aus dem Auftrag; 16 E2E-Aufträge < 25 KB.
- data/aufgaben.yaml (mandat-start, import, prueffeld, unterlagen, notiz-Tabelle, wesentlichkeit), ketten.yaml K8 «Wann», Regel kritische_grundhaltung (SER 1.2); Skills, Snippet, openclaw/openclaw-tools-empfehlung.json, AGENTS.md/KONZEPT.md.
- Tests: routing 82/82, thema 145/145, lint 0 Fehler; offen: Plugin neu bauen (build_plugin.py), E1-Messung.

## [2026-11-13] daten | R2 Code-Durchgang 2: Nachzügler-Vorschläge (Daten)
- aufgaben.yaml: kapitalschutz checkliste[0] (Fremdkapital unverändert, Covid-Kredit Art. 3 SBüV/HFMV 20 nur `--covid-kredit`, Art. 4 bleibt FK, `--reserve-voll`) und [3] (`--rr-polster`); abschluss → `prozess p4 schritte`, Ereignisse nach Stichtag (SCH3-302 nur auf Anweisung); neue Aufgabe `planung` (p2, ohne Überschneidung mit mandat-start/wesentlichkeit), import.naechste.
- prozess/*.yaml: Feld `aufrufe` (p1, p2, p4, p5, p6), «Prozess N» → «Agent-Prozess N» (ausser Zitaten), p4 schritte[13] ohne gesperrtes Werkzeug. katalog.yaml: text '' bei P1-141, S1-151, T1-173.
- prueffelder: C1-401 (vorhandene Saldobestätigungen ohne Anweisung auswerten, HWP ER Rz 137), K1-101/K1-403 `tage()`, K1-301/L1-301 Namen in `rechne`, N1-105/N1-401/P1-313/A1-205 `--rr-polster` (+ aufrufe A1-205), kurzbeschrieb ≤ 300 (i1, s1, sch1–sch5), Unterlagen g2/i1 mit Fundstelle, Status f2/g2/i1 extrahiert (Nachprüfung offen); werte: Chunk-Ids zu «Rz N».
- Tests: lint 0 Fehler/0 Warnungen, routing 85/85 (3 neue Fälle planung), thema 170/170, E2E-Bündel max. 22 KB.

## [2026-11-13] daten | R2 Code-Durchgang 2: Prüferbefunde zu den Nachzügler-Vorschlägen korrigiert
- revision.py: Satzende nach «)»/«»» (Tor p7/p8 vollständig), Abkürzungen anh/vs/ff/bzgl; Notizregel je Rolle (WP/4xx ohne Anweisung kein Textfeld, Übergangsregel + Schwelle); `_schritt_ids` Komma-Listen; `prozess`: «Phase N»/«Prozess 7/8»/«agent prozess N», ganze Wörter vor Präfixen, Abschnitt an beliebiger Stelle, «|» → Hinweis, «ab N» geprüft, --voll in Teilen ≤ 24 KB, Kompaktansicht ≤ 5 KB (Bytes), Aufrufe nie halb gekürzt, Befragung gekennzeichnet, Hauptkette statt Hilfsaufgaben (p3, p8 mit planung); `prueffeld` ≤ 24 KB mit «+n weitere» und Abschnitten; kapitalverlust (negative Beträge, fehlende Reserven, Covid > FK, Polster Rz 421), revisionspflicht mit Teil-Vorjahreswerten; `aufgabe`: ein Hauptnachfolger, Rücksprung zur aufrufenden Checkliste; pf_code mit Synonymen.
- Daten: aufgaben (planung: kapitalverlust-Punkt, Ort der Planungsnotiz, Tor (2); naechste; abschluss Ziel/Stichwort; prueffeld Upload K15), regeln kunde + Themen (PBC-Vorschlag), werte covid (HFMV 20, nicht abziehen), p4 schritte[13] (K15-Bedingung), p7 Dauerakten, A1-205 (Fremdkapital laut Bilanz), O1-403, P1-141/S1-151 (Katalogpflege wie T1-173).
- Tests: neu eval/werkzeug_test.py 7/7; routing 88/88 (+3 Fälle abschluss/planung), thema 170/170, lint 0 Fehler/0 Warnungen, 16 E2E-Aufträge max. 22.6 KB.

## [2026-11-13] daten | R3 Teile A/B/D: arbeitspaket, plan, aufgabe-Router
- `arbeitspaket <akte> --pf <code>[,<code>] [--vj] [--schritt] [--teil N]` (CLI + MCP): Belegpaket je Prüffeld in Teilen ≤ 24 KB – Konten der Saldoliste (Gruppe/Bezeichnung wie `akte`, Rückfall Kontenklasse KMU, Saldo GJ/VJ/Δ/Vorjahresakte, Σ je Gruppe), Kontoblätter (auch Folgejahr, Journal), Jahresrechnung/Anhang, Dateien, Fundstellen, Vorjahresakte, Schritte; Kürzungsstufen bis ≤ 3 Teile. Generisch (Markdown-/CSV-Tabellen, Text-Saldoliste).
- `plan "<Auftrag>" [--akte] [--vj]` (CLI + MCP): JSON-Turns für einen Orchestrator (Belege/Konten → je 3–4 Schritte → 4xx/WP → Abschluss mit Statustabelle; andere Aufgaben: Checklistenpunkte je 3–4 → Fertig-wenn).
- Router: Prozess 2 «Akte erschliessen» und Arbeitsregel 1 → `arbeitspaket` zuerst; Import: Punkt «Saldoliste aller Konten» (A1-Paket); Mandatsstart: Hinweis. `akte --inhalt <Jahresrechnung>` löst Platzhalter über eindeutigen Dateinamen auf.
- Test: 29 Prüffelder (Entwicklungs-Testakte mit VJ) ohne Absturz, alle Teile ≤ 24 KB, ≤ 3 Teile; 16 E2E-Pläne gültig (alle Ids, Aufrufe ausführbar); werkzeug_test 9/9, Routing 181/183, Thema 170/170, lint 0.

## [2026-11-13] eval | Messung R2 mit Haiku 4.5 (Plugin R2, Werkzeugsperre message/Web)
- B2 Fachfragen (40): richtig 6 · teilweise 27 · falsch 7 (B1: 6/30/4, B0: 3/18/19) – kein Fortschritt; Ursachen behoben (Fachkontext bei Fragen, Aufzählungen in thema, Kettenzeile).
- E1 E2E bekannte Testakte (16): 351 Referenzbefunde, gefunden 17 · teilweise 37 · Note Ø 2.7 (E0: 14/41/2.6). H1 Holdout-Akte (8, unabhängig erstellt): 33 · 4 · 8 · 3.0 (H0 mit E0-Plugin: 4/10/3.1).
- Weniger Grenzverstösse (kein Sendeversuch, message/Web gesperrt), Akte konsequent mit `akte` erschlossen; Befund-Abdeckung unverändert. Hauptursache: schwaches Modell macht 10–25 Aufrufe und hört auf, liest Dateien nicht ganz, ruft Rechner nicht auf → R3 (Arbeitspakete, Orchestrierung in Turns).
- Routing-Holdouts (unabhängig formuliert): Holdout 2 38/45 (vor R2 = nach R2-Code), Holdout 3 43/50 (sauber, Stand R2); danach allgemeine Fehlerklassen behoben (2: 43/45, 3: 50/50, beide verbraucht).
