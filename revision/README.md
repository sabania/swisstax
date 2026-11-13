# Revisions-Wiki (eingeschränkte Revision CH, revio 4.0)

**INTERN (consis).** Die EXPERTsuisse-Werke (HWP, SER, SA-CH, Q&A, Muster) sind an consis lizenziert, revio ist proprietär. Nicht
weitergeben und nicht in ein öffentliches Repository übernehmen.

Wissensbasis und Werkzeug für den KI-Revisionsagenten. Der Agent **bereitet vor** (Prüfschritte, Textfeld-Entwürfe, Notizen,
Unterlagen, Rapport), der Wirtschaftsprüfer entscheidet. Er setzt nie ein Visum, schliesst nichts ab, gibt nichts frei, bucht nicht
und sendet nichts an Kunden.

| Datei | Inhalt |
|---|---|
| [AGENTS.md](AGENTS.md) | Regelwerk für Agenten: harte Regeln, Aufbau, Routing, Zitierformat, Pflege |
| [KONZEPT.md](KONZEPT.md) | Ziel, Schichten, Wissen, Führung schwacher Modelle (3a, 3b), revio-Zuordnung, offene Entscheide |
| [log.md](log.md) | Chronik aller Ingest-, Daten- und Messschritte |
| `quick/index.md` | Einstieg für Menschen: Frage → Seite |

## Aufbau

Rohquellen (`raw/`) → Volltext (`sources/`) → zitierfähige Chunks (`chunks/`, OR je Artikel, HWP je Randziffer, SER je Abschnitt) →
Daten mit Fundstelle und wörtlichem Zitat (`data/`) → Quick-/Detailseiten (`quick/`, `wiki/`) → Werkzeug (`tools/revision.py`),
MCP-Server (`tools/mcp_server.py`, 19 Tools), Skills (`skills/`) und Plugin (`tools/build_plugin.py`).

## Nutzung

```
python3 revision/tools/revision.py hilfe                       # Übersicht aller Befehle
python3 revision/tools/revision.py aufgabe "Prüffeld C1 vorbereiten"
python3 revision/tools/revision.py arbeitspaket <akte> --pf C1 --vj <vj-akte>     # Belegpaket, Teile mit --teil N
python3 revision/tools/revision.py akte <akte> --vj <vj-akte>   # Mandantenordner erschliessen (nur lesen)
python3 revision/tools/revision.py plan "Prüffeld C1 vorbereiten" --akte <akte> --vj <vj-akte>   # Turns für einen Orchestrator
python3 revision/tools/revision.py pruefschritt C1-302
python3 revision/tools/revision.py rechne "1'250'000 - 1'180'500"
```

**OpenClaw:** Plugin bauen (`python3 revision/tools/build_plugin.py --out revision/dist/revisionswiki --version x.y.z`), dann
`openclaw plugins install revision/dist/revisionswiki --force`. Den Inhalt von `openclaw/AGENTS.workspace-snippet.md` als AGENTS.md
in den Workspace des Agenten legen und den Block `tools` aus `openclaw/openclaw-tools-empfehlung.json` übernehmen (sperrt Versand,
Web, Automation). revio-MCP-Werkzeuge: `openclaw/revio-tool-policy.json`.

**Schwache Modelle (z.B. kleine lokale Modelle):** nicht den ganzen Auftrag in einem Turn geben. Ein Orchestrator ruft `plan` auf und
sendet je Turn eine Anweisung in derselben Session (KONZEPT 3b). Testfassung: `eval/orchestrator_openclaw.py`.

## Prüfen und messen

```
python3 revision/tools/lint.py                      # Zitate, Ids, Links, Werkzeugnamen, Testakten-Bezüge
python3 revision/eval/routing_test.py               # aufgabe-Router (Entwicklungsset; Holdouts als Argument)
python3 revision/eval/thema_test.py                 # Themen-Abdeckung
python3 revision/eval/werkzeug_test.py              # Werkzeug inkl. arbeitspaket und plan (fiktive Mini-Akte)
python3 revision/eval/beleg_abdeckung.py            # Belegstellen der Referenz in den Arbeitspaketen (ohne Modell)
```

Testakten unter `eval/testdaten/` sind fiktiv. Messläufe mit Haiku 4.5 in OpenClaw liegen unter `eval/laeufe/` (Rohantworten und
unabhängige Bewertungen); der Verlauf steht in `log.md` (Einträge «eval»).
