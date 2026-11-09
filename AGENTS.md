# AGENTS.md – Schema des Steuer-Wikis (Schweiz, natürliche Personen)

Dieses Repository ist eine **LLM-Wiki-Wissensbasis** (Muster nach Karpathy: Rohquellen → Wiki → Schema) für einen
KI-Steuerexperten, der Fachpersonen (SB/ML) beim Erstellen von Steuererklärungen natürlicher Personen unterstützt.
Abdeckung: **Bund** (DBG, StHG, VStG, ESTV-Praxis) und die Kantone **AR, SG, TG, ZH**, Steuerjahre **2025, 2026** (erweiterbar).
Die fachliche Beurteilung bleibt bei der Fachperson. Diese Datei ist das Regelwerk für jeden Agenten, der das Wiki liest oder pflegt.

## 1. Harte Regeln

1. **Jede Zahl mit Fundstelle.** Beträge, Sätze, Fristen nur aus amtlichen Quellen dieses Wikis nennen – immer mit
   Quelle (Chunk-ID bzw. Dokument + Seite/Ziffer/Artikel) und dem Steuerjahr. Nichts aus dem Gedächtnis ergänzen.
2. **Jurisdiktion × Steuerjahr sind fest.** Steuerjahr = Steuerperiode (die Wegleitung 2025 erscheint 2026). Werte nie
   von einem Jahr oder Kanton auf ein anderes übertragen. Fehlt ein Wert für das Jahr: sagen, dass er fehlt, und den
   Vorjahreswert höchstens ausdrücklich als «Vorjahr, nicht bestätigt» nennen.
3. **Staats-/Gemeindesteuer ≠ direkte Bundessteuer.** Natürliche Personen reichen eine kantonale Steuererklärung ein,
   die beide Ebenen abdeckt; Abzüge unterscheiden sich oft (Spalten «Kanton» und «Bund» beachten).
4. **Status respektieren:** `verifiziert` (Fachperson) > `agent-geprueft` > `extrahiert` > `offen`; `strittig` heisst
   Quellen widersprechen sich → Fachperson entscheidet. Nur Menschen setzen `verifiziert`.
5. **Unveränderlich:** `raw/` (Originale), `sources/` (Volltexte) und `chunks/` werden nur von den Tools in `tools/`
   erzeugt, nie von Hand oder per LLM umformuliert. Wissen wird in `data/` (YAML) und `wiki/` gepflegt.
6. **Keine Mandantendaten** im Wiki (Berufsgeheimnis). Abgelegte Antworten sind generisch und anonym.
7. **Unsicherheit offenlegen:** Quelle unklar, Seed-Wert «prüfen», Layoutfehler im PDF → so kennzeichnen und auf das
   Original (`raw/…pdf`, Seite) verweisen.

## 2. Aufbau (Schichten)

| Schicht | Ordner | Inhalt | Wer schreibt |
|---|---|---|---|
| 1 Quick Access | `quick/` | Belege-Relevanz, Zuordnung Beleg→Formularziffer je Kanton/Jahr, Eckwerte je Jurisdiktion/Jahr, Jahresvergleich | generiert aus `data/` (`tools/build_quick.py`) |
| Daten | `data/` | `belege.yaml`, `werte/<jur>/<jahr>.yaml`, `zuordnung/<kanton>/<jahr>.yaml` – jede Angabe mit Chunk-ID + wörtlichem Zitat | Agent (Ingest) + Fachperson |
| 2 Detailwissen | `wiki/` | `themen/` (Querschnitt), `belege/` (Detailkarte je Belegtyp), `<jur>/` Überblick, Zuordnung-/Werte-Detail (mit Zitaten), Quellenkatalog, `quellen/` (Zusammenfassung je Dokument) | Agent, Review durch Fachperson; `belege/` und `*-detail.md` generiert |
| 3 Volltext | `sources/<jur>/<jahr>/<id>.md` | verbatim konvertierte Quellen mit Seitenmarkern `<!-- Seite N -->` | `tools/convert.py`, `tools/laws.py` |
| 3 RAG-Chunks | `chunks/<jur>/<jahr>/<id>/<id>__cNNNN.md` bzw. `__art-33` | semantische/strukturelle Chunks (≤ ~1'500 Zeichen) mit Kontextzeile | `tools/chunk.py` |
| Index | `index/chunks.jsonl`, `index/quellen.jsonl` | alle Chunks/Quellen mit Metadaten (für Hybrid-RAG) | `tools/build_index.py` |
| Originale | `raw/<jur>/<jahr>/<id>.pdf|html|xml` | unveränderte Downloads (Backup, sha256 in Registry) | `tools/fetch.py` |
| Register | `registry/` | `sources.yaml` (alle Quellen), `taxonomy.yaml` (Schlüssel), `years.yaml`, `chunkplans/` | Tools + Agent |

`<jur>` ∈ `bund, ar, sg, tg, zh`. `<jahr>` = erstes Steuerjahr der Fassung, oder `dauernd` für jahresunabhängige
Dokumente (Kreisschreiben, Merkblätter, Praxis). Massgeblich ist immer das Feld `jahre` (Frontmatter/Registry).

## 3. Anfragen beantworten (Routing)

1. **Kanton und Steuerjahr klären** (Wohnsitz am 31.12.; bei Unklarheit nachfragen).
2. **Quick-Layer:** `quick/index.md` (Frage → Seite) → `quick/belege-relevanz.md` (ist ein Dokument relevant?) →
   `quick/zuordnung-<kt>-<jahr>.md` bzw. `quick/belege-ziffern.md` (welcher Wert in welche Ziffer?) →
   `quick/werte-<jur>-<jahr>.md` / `quick/vergleich-<jahr>.md` (Limiten/Pauschalen).
3. **Detail:** `wiki/<jur>/zuordnung-<kt>-<jahr>-detail.md`, `wiki/<jur>/werte-<jur>-<jahr>-detail.md` (Zitate),
   `wiki/belege/beleg-<id>.md`, `wiki/themen/<thema>.md`, `wiki/<jur>/<jur>-ueberblick.md`, `wiki/<jur>/quellen/<id>.md`.
4. **Beleg:** den zitierten Chunk öffnen (`chunks/…`); bei Tabellen/Layout das Original `raw/…pdf` (Seite) prüfen.
5. **Nicht abgedeckt?** Hybride Suche über `chunks/` (OpenClaw `memory_search`, qmd oder `index/chunks.jsonl`),
   Suchbegriff mit Kanton und Jahr anreichern (z.B. «Fahrkosten ZH 2025»), Treffer nach `jur`/`jahre` filtern.
   Gesetzesartikel: `chunks/<jur>/<jahr>/<gesetz-id>/<id>__art-<nr>.md` (Bund/AR/SG: Art.) bzw. `__par-<nr>.md` (ZH/TG: §);
   lange Artikel sind in Teile `-t1`, `-t2` … gesplittet (z.B. `bund-dbg-2025__art-33-t4.md`).
6. **Antwort:** Ergebnis, Steuerjahr, Kanton/Bund getrennt, Fundstelle(n), Status. Nichts gefunden → sagen.

## 4. Zitierformat

- Tabelle: Spalte «Quelle» mit Link auf den Chunk, z.B. `[WL ZH 2025 S. 14](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0042.md)`.
- Fliesstext: `^[zh-wl-2025__c0042]` (Chunk-ID) oder `^[bund-dbg-2026__art-33]`.
- Daten (`data/*.yaml`): `quelle: <chunk-id>` und `zitat: "<wörtlich aus dem Chunk>"` – `tools/lint.py` prüft das Zitat
  maschinell gegen den Chunk-Text.

## 5. Autorität bei Widersprüchen

Gesetz/Verordnung (Fassung des Steuerjahres) > amtliche Praxis des Jahres (Wegleitung, Weisung, Steuerbuch/Steuerpraxis,
ESTV-Kreis-/Rundschreiben) > Formulare/Merkblätter/Hilfetexte > Mitteilungen > Sekundärquellen. Unterschiede zwischen
Kantonen sind keine Widersprüche. Gleicher Schlüssel + Jurisdiktion + Jahr mit verschiedenen Werten → `status: strittig`,
beide Quellen nennen, Eintrag in `reports/`, Fachperson entscheidet.

## 6. Seitentypen (Frontmatter)

Alle Wiki-/Quick-Seiten beginnen mit YAML-Frontmatter: `typ` (quick-index | belege | zuordnung | werte | vergleich |
thema | ueberblick | quelle | quellenkatalog | antwort | beleg | werte-detail | zuordnung-detail), `titel`, `jur` (oder `multi`), `jahre`, `quellen` (IDs),
`status` (entwurf | stabil | veraltet), `generiert` (Tool/Agent, Datum), optional `verifiziert` (Kürzel, Datum).
Dateinamen: kebab-case, ASCII (ae/oe/ue), global eindeutig (`werte-zh-2025.md`), **nie** mit Datumspräfix `YYYY-MM-DD`
(OpenClaw behandelt solche Dateien als Tagesnotizen mit Zeitverfall).

## 7. Operationen (Pflege)

Detaillierte Abläufe: `skills/steuerwiki-pflege/SKILL.md`. Kurzfassung:

- **Ingest (neue Quelle):** Eintrag in `registry/sources.yaml` → `python3 tools/fetch.py --id <id>` →
  `tools/convert.py --id <id>` (Gesetze: `tools/laws.py`) → Chunk-Plan (Agent, `registry/chunkplans/<id>.json`,
  geprüft mit `tools/validate_plan.py`) → `tools/chunk.py --id <id>` → `tools/build_index.py` → Werte/Zuordnungen in
  `data/` nachführen (mit Zitat) → betroffene `wiki/`-Seiten aktualisieren → `tools/build_quick.py` → `tools/lint.py` → `log.md`.
- **Neues Steuerjahr:** `python3 tools/new_year.py --jahr 2027 --von 2026` (Gerüst mit gleichen Schlüsseln, Status
  `offen`), dann Quellen des neuen Jahres einlesen. **Nie** Werte ohne Quelle des neuen Jahres übernehmen.
- **Lint:** `python3 tools/lint.py` (deterministisch: Hash-Drift, Zitate, Links, Dateinamen) + inhaltliche Prüfung
  (Widersprüche, Lücken, auffällige Jahressprünge) → `reports/`.
- **Antwort ablegen:** gute, generische Antworten als `wiki/antworten/<slug>.md` (`status: entwurf`), mit Zitaten.

## 8. Log

`log.md` ist chronologisch, nur anhängen. Eintrag: `## [YYYY-MM-DD] <fetch|ingest|query|lint|verify|neues-jahr> | <Titel>`
gefolgt von 1–5 Zeilen (was, welche Dateien, offene Punkte). Letzte Einträge: `grep "^## \[" log.md | tail -5`.

## 9. Sitzungsstart (Agent)

1. Diese Datei lesen. 2. `index.md` und `quick/index.md` lesen. 3. Letzte 5 `log.md`-Einträge lesen.
4. Bei Pflegeaufgaben `reports/lint.md` prüfen.
