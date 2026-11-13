# AGENTS.md – Schema des Revisions-Wikis (eingeschränkte Revision CH, revio 4.0)

Wissensbasis für den **KI-Revisionsagenten** von consis (Muster wie das Steuer-Wiki: Rohquellen → Chunks → Daten → Quick/Wiki →
Werkzeug/MCP/Skills/Plugin). Der Agent **bereitet vor** (Prüfschritte, Textfelder, Notizen, Unterlagen, Rapport, GVB-Entwurf);
der Wirtschaftsprüfer (WP) entscheidet. **INTERN:** EXPERTsuisse-Werke (HWP, SER, SA-CH, Q&A, Muster) sind an consis lizenziert,
revio ist proprietär – nicht weitergeben. Diese Datei ist das Regelwerk für jeden Agenten, der das Wiki liest oder pflegt.

## 1. Harte Regeln
1. **Jede fachliche Aussage mit Fundstelle** (Chunk-Id + wörtliches Zitat). Nichts aus dem Gedächtnis ergänzen; Praxis ohne Quelle
   als «Praxis/intern» kennzeichnen.
2. **Quellenrang:** OR (Gesetz) > SER (massgebend für die eingeschränkte Revision) > HWP ER > HWP BuR, Q&A, Muster, ESTV-Praxis >
   Fachliteratur > intern (Konzept consis). SA-CH und HWP OR gelten nur für die **ordentliche** Revision: für die eingeschränkte Revision
   nicht als Grundlage verwenden; nur bei Fragen zur ordentlichen Revision zitieren und dann ausdrücklich so kennzeichnen.
3. **Grenzen des Agenten** (Konzept consis, `data/regeln.yaml`): nie Visum, ✓, Abschliessende Beurteilung, Abschluss/Siegel/Freigabe,
   Unterzeichnung/Datierung, Kundenversand, Buchung, Notiz löschen/erledigen, Wesentlichkeit/Planung ändern. Gesperrte revio-Werkzeuge
   (`wiki/revio/werkzeuge-nur-mensch.md`) nie aufrufen, auch nicht über `revio_call`.
4. **Status:** `verifiziert` (WP) > `agent-geprueft` (Fundstellen maschinell geprüft + Zweitprüfung) > `extrahiert` > `offen`.
   Nur Menschen setzen `verifiziert`.
5. **Unveränderlich:** `raw/`, `sources/`, `chunks/` nur durch `tools/ingest.py`, `tools/chunk.py` erzeugen. Wissen wird in `data/`
   gepflegt; `quick/` und `wiki/` (ausser Handseiten) erzeugt `tools/build_quick.py`.
6. **Keine Mandantendaten** im Wiki (Geheimhaltung der Revisionsstelle OR 730b Abs. 2 ^[or__art-730b], Berufsgeheimnis StGB 321
   ^[stgb__art-321]). Testdaten unter `eval/testdaten/` sind fiktiv.
7. **Steuerliche Werte** (ESTV-Zinssätze, Pauschalen, KS 6a) sind Praxis der Steuerbehörden, keine handelsrechtlichen Bewertungsregeln.

## 2. Aufbau
| Schicht | Ordner | Inhalt | Wer schreibt |
|---|---|---|---|
| Originale | `raw/` | PDF/DOCX/XLSX/XML, sha256 in `registry/sources.yaml`; `raw/revio/` = revio-MCP-Werkzeugliste (INTERN) | `tools/ingest.py` |
| Volltext | `sources/<id>.md` | mit `<!-- Seite N -->` | `tools/ingest.py` |
| Chunks | `chunks/<quelle>/<id>.md` | OR je Artikel (`or__art-725a`), HWP je Randziffer (`hwp-er-2026__rz-0113-s060`), SER je Abschnitt/Anhang (`ser-2022__anh-d-s075-1`), übrige je Seite/Abschnitt | `tools/chunk.py` |
| Index | `index/fts.sqlite` (Tabelle `chunk` + FTS5 mit Silbentrennungs-Ausgleich), `index/chunks.jsonl`, `index/lookup.json` | `tools/build_index.py`, `tools/build_lookup.py` |
| Daten | `data/katalog.yaml` (538 Schritte), `data/prueffelder/<code>.yaml`, `data/prozess/<p>.yaml`, `data/werte.yaml`, `data/regeln.yaml`, `data/themen.yaml`, `data/revio/` | Agent (Workflow mit Zweitprüfung) + WP |
| Quick | `quick/` | Index, Prüffelder, Prozess, Regeln, Werte, revio, PBC, Kundenfragen | `tools/build_quick.py` |
| Detail | `wiki/prueffelder/`, `wiki/prozess/`, `wiki/themen/`, `wiki/revio/`, `wiki/quellen.md` | generiert (mit allen Zitaten) | `tools/build_quick.py` |
| Werkzeug | `tools/revision.py` (CLI), `tools/mcp_server.py` (16 Tools), `skills/`, `openclaw/` (`revio-tool-policy.json` aus der OpenClaw-Liste) | Plugin `plugins/revisionswiki` | `tools/build_plugin.py` |
| Test | `eval/` | Testakte (fiktiv), Referenzlösung, Fragen, Messungen | Agent |

## 3. Anfragen beantworten (Routing)
1. **Werkzeug zuerst:** `python3 revision/tools/revision.py aufgabe "<Aufgabe/Frage>"` (Übersicht: `hilfe`) bzw. Tools `revisionswiki__…`.
2. Prüfschritt → `pruefschritt <id>`; Prüffeld → `prueffeld <code|stichwort>`; Ablauf/WP-Entscheid → `prozess [p1…p8]`, `regeln`;
   revio → `revio <bereich|code|id|stichwort|werkzeug|ketten|nur-mensch>`; Zahl → `wert`; Rechnen → `rechne`, `wesentlichkeit`,
   `kapitalverlust`, `revisionspflicht`; Thema → `thema`; sonst `suche` → `zeige`.
3. Antwort: Ergebnis · Fundstelle(n) · Status · was der WP entscheidet. Nichts gefunden → sagen.

## 4. Zitierformat
Fliesstext `^[chunk-id]`; Daten: `quelle: <chunk-id>` + `zitat: "<wörtlich>"` – `tools/lint.py` prüft jedes Zitat.

## 5. Pflege
- **Neue Quelle / neue Fassung:** Eintrag in `registry/sources.yaml` (neue Fassung als eigene Id, nie überschreiben) → `tools/ingest.py --id <id>`
  → `tools/chunk.py --id <id>` → `tools/build_index.py` → betroffene `data/`-Einträge nachführen → `tools/build_quick.py` → `tools/lint.py` → `log.md`.
- **Neuer revio-Katalog / neue revio-MCP-Version:** `data/katalog.yaml` bzw. `raw/revio/` ersetzen → Klassifikation `data/revio/werkzeuge.csv`
  nachführen (neue Werkzeuge = `unklar`, bis geprüft) → `tools/lint.py` (meldet unbekannte/unklassifizierte Werkzeuge).
- **Erfassung mit Agenten:** Workflows mit Zweitprüfung; Ergebnisse mit `tools/build_data.py --runs <workflow-dir>` übernehmen
  (Zitate werden geprüft/repariert, Bericht `reports/import-*.md`).
- **Plugin:** `python3 revision/tools/build_plugin.py --version x.y.z` (Ausgabe `plugins/revisionswiki`), Version in
  `.claude-plugin/marketplace.json` nachführen.

## 6. Log
`log.md` chronologisch, nur anhängen: `## [YYYY-MM-DD] <ingest|daten|lint|eval|plugin> | <Titel>` + 1–5 Zeilen.
