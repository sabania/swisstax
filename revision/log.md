
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
