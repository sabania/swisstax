---
name: steuerwiki-pflege
description: Steuer-Wiki pflegen – neue Quelle einlesen, neues Steuerjahr anlegen, Werte mit Zitat erfassen, Lint ausführen.
---

# Steuer-Wiki pflegen (Ingest · neues Jahr · Lint)

Arbeitsverzeichnis: Wurzel des Steuer-Wikis (dort liegen `AGENTS.md`, `tools/`). Python 3 mit `requests`, `pyyaml`,
`beautifulsoup4`, `lxml`, `markdownify`; `pdftotext` (poppler). Nach jeder Operation `log.md` ergänzen.

## A. Neue Quelle einlesen (Ingest)

1. Registry-Eintrag in `registry/sources.yaml` ergänzen (Felder siehe bestehende Einträge):
   `id` (`<jur>-<kürzel>[-<jahr>]`, kebab-case), `jurisdiktion`, `ordner_jahr` (erstes Steuerjahr oder `dauernd`),
   `jahre`, `typ`, `kurz`, `titel`, `url`, `format`, `verarbeitung` (`chunk` | `volltext` | `link`).
2. `python3 tools/fetch.py --id <id>` (lädt nach `raw/`, speichert sha256).
3. `python3 tools/convert.py --id <id>` (PDF/HTML → `sources/`). Gesetze: Bundesrecht `python3 tools/laws.py resolve --jahre <J>`
   + `tools/laws.py convert`; kantonale Gesetze siehe `tools/laws.py` (LexWork/PDF-Fallback).
4. **Semantischer Chunk-Plan** (nur PDF, nicht Gesetze): Volltext ganz lesen, Grenzen je Ziffer/Abschnitt festlegen,
   als `registry/chunkplans/<id>.json` speichern (Format: Docstring `tools/validate_plan.py`), prüfen mit
   `python3 tools/validate_plan.py <id>`. HTML-Quellen werden automatisch an Überschriften gechunkt.
5. `python3 tools/chunk.py --id <id>` → `python3 tools/build_index.py`.
6. **Wissen nachführen:** betroffene Werte in `data/werte/<jur>/<jahr>.yaml` und Zuordnungen in
   `data/zuordnung/<kt>/<jahr>.yaml` ergänzen – jede Angabe mit `quellen: [{chunk: <id>, zitat: "<wörtlich>"}]` und
   `status: extrahiert`. Danach `wiki/themen/*` und `wiki/<jur>/quellen/<id>.md` (Zusammenfassung) aktualisieren.
7. `python3 tools/build_quick.py` → `python3 tools/lint.py` (muss ohne Fehler laufen) → `log.md`.

## B. Neues Steuerjahr (z.B. 2027)

1. `python3 tools/new_year.py --jahr 2027 --von 2026` – legt `data/werte/*/2027.yaml` und `data/zuordnung/*/2027.yaml`
   mit denselben Schlüsseln an (Werte leer, `status: offen`) und listet die zu suchenden Quellen (Wegleitungen,
   Rundschreiben kalte Progression, Steuerfüsse …) in `reports/neues-jahr-2027.md`.
2. Bundesrecht: `python3 tools/laws.py resolve --jahre 2027` → fetch → convert → chunk.
3. Jede neue Quelle gemäss A einlesen. **Werte nie ohne Quelle des neuen Jahres übernehmen.** Unverändert bestätigte
   Werte mit der neuen Quelle zitieren.
4. `registry/years.yaml` aktualisieren (Status `teilweise`/`vollständig`), Lint, Log.

## C. Lint

`python3 tools/lint.py` → `reports/lint.md`. Fehlerklassen: R1 Registry/Hash-Drift (Original geändert → neu
konvertieren und betroffene Werte prüfen), R2 fehlende Volltexte/Chunks, R3 Datumspräfix im Dateinamen,
D1 Zitat nicht im Chunk / unbekannter Schlüssel / Jahres-Wache, L1 tote Links. Inhaltlich zusätzlich prüfen:
Widersprüche gleicher Schlüssel/Jahr/Jurisdiktion, auffällige Jahressprünge, Lücken (`offen`).

## D. Verifikation durch Fachperson

Fachperson prüft Werte/Zuordnungen und setzt `status: verifiziert` sowie `verifiziert: {von: <Kürzel>, am: <Datum>}`.
Agenten setzen höchstens `extrahiert` bzw. nach unabhängiger Gegenprüfung `agent-geprueft`.

## Änderungen nachvollziehen (Pflicht vor jeder Änderung)

- `python3 tools/impact.py --quelle <id>` / `--chunk <id>` / `--datei data/…yaml` / `--seite wiki/…md` zeigt alle
  betroffenen Daten-Einträge, generierten und handgeschriebenen Seiten; `--geaendert` prüft sha256 der Originale.
- Neue Fassung einer Quelle **nie überschreiben**: neuer Registry-Eintrag mit `zeitbezug`, `gilt_ab`, `ersetzt: <alte id>`
  (bei der alten `ersetzt_durch` und `gilt_bis` setzen), `jahre` nach Zeitmodell (AGENTS.md Regel 2a).
- Nach Registry-Änderungen: `python3 tools/sync_frontmatter.py` (Metadaten der Volltexte) → `python3 tools/chunk.py --id <id>`
  (IDs/Texte bleiben stabil; Chunk-Pläne zählen ab Textkörper) → `build_index.py` → `build_quick.py` → `lint.py`.
- Kompakt-Wegleitung pflegen: Felder `rein`, `berechnung`, `beachten` je Position in `data/zuordnung/<kt>/<jahr>.yaml`; jede
  Zahl muss in einem zitierten Chunk oder in einem verknüpften Eckwert (`werte_keys`) stehen.
