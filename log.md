# Log – Steuer-Wiki

Chronologisch, nur anhängen. Format: `## [YYYY-MM-DD] <fetch|ingest|query|lint|verify|neues-jahr|aufbau> | <Titel>`.
Letzte Einträge: `grep "^## \[" log.md | tail -5`

## [2026-11-09] aufbau | Grundgerüst, Registry und Download aller Seed-Quellen
- Seed: 5 Wissensdatenbank-Dateien (Bund, AR, SG, TG, ZH; Recherche 30.10.2026) nach `_seed/` übernommen.
- 203 URLs extrahiert, kuratiert in `registry/sources.yaml` (ID, Jurisdiktion, Jahr, Typ, Verarbeitung), alle mit HTTP 200 geladen.
- Ergänzt: ESTV-Formulare/Wegleitung 2025 aus dem ZIP, ZStB-Vorgängerfassungen «gültig bis 31.12.2025»,
  VKP ZH (ZStB 48.1, Fassungen ab 2024 und ab 2026).

## [2026-11-09] ingest | Bundesrecht aus Fedlex (Akoma-Ntoso-XML)
- SPARQL-Auflösung je Steuerjahr 2025/2026: DBG (2025, 2026), StHG, VStG, VStV (korrigierte ELI cc/1966/1585_1641_1624),
  BKV (2025, 2026), LKV, QStV (ab 10.01.2025), VKP (2025, 2026), BVV 3, WEFV → 1 Chunk pro Artikel.

## [2026-11-09] ingest | Kantonsrecht (LexWork AR/SG/TG, ZH-Lex), Praxis und Formulare
- Gesetze AR/SG/TG aus LexWork-JSON (Jahresfassungen), ZH StG/Verordnungen aus ZH-Lex-PDF (pdfplumber) → 1 Chunk je Artikel/§.
- Wegleitungen, Formulare, Merkblätter, Steuerbuch (ZH/SG), Steuerpraxis (TG): pdftotext/HTML → Chunk-Pläne (152, Agenten) →
  `tools/chunk.py`; total 285 Quellen, 8'876 Chunks (Bund 2'890 · ZH 2'136 · SG 1'502 · TG 1'462 · AR 886).
- Ergänzt: KS 11/18 (Gültigkeit KS 11a ab 2027), TG StP 34/24 Fassung 2025, QStV konsolidiert.

## [2026-11-09] ingest | Datenschicht (Werte, Zuordnungen, Belege) mit wörtlichen Zitaten
- `data/werte/<jur>/<jahr>.yaml` (10 Dateien, 72 Schlüssel), `data/zuordnung/<kt>/<jahr>.yaml` (7 + AR-2026-Gerüst),
  `data/belege-teil1..3.yaml` (45 Belegtypen); jedes Zitat maschinell gegen den Chunk geprüft (`tools/validate_data.py`).

## [2026-11-09] verify | Zweitprüfung (Sonnet) + Stichproben (Opus)
- Kritische Werte gegengeprüft (Bund DBG/BKV, ZH Drittbetreuung, AR Anhang 1, ZH Liegenschaft 20 %, SG Motorrad, ZH Form. 3.4).
- Strittig gesetzt: AR 2026 Kinderabzüge (Anhang 1 vs. MB 02), TG 2026 Bund-km-Ansatz (WL intern), ZH Leibrenten 40 % vs.
  Ertragsanteil (StHG Art. 7/72), SG 2026 Parteispenden, TG 2025 Drittbetreuung Bund, AR 2025 Ziff. 13.2 → `reports/offene-punkte.md`.

## [2026-11-09] ingest | Wiki-Seiten (Themen, Überblicke)
- 31 Themenseiten `wiki/themen/`, 5 Überblicke `wiki/<jur>/<jur>-ueberblick.md` (Sonnet), Links/Chunk-IDs per Lint geprüft.

## [2026-11-09] query | Praxistest Runde 1 (q01–q30) und Umbau Quick-Layer
- 30 Fragen, 6 Sonnet-Agenten nur mit Wiki: inhaltlich 30/30 korrekt (Review Opus gegen `eval/erwartet.yaml`).
- Befund Navigation: Quick-Seiten zu gross (bis 144 KB) → kompakte Quick-Tabellen + Detailseiten mit Zitaten
  (`wiki/<jur>/*-detail.md`), 45 Belegkarten `wiki/belege/`, `quick/belege-ziffern.md`, Frage-Router in `quick/index.md`.

## [2026-11-09] query | Praxistest Runde 2 (q31–q40 + Nachtest q01/q12/q23)
- 13/13 korrekt, Laufzeit halbiert. Lücke: Steuersätze Kapitalleistungen aus Vorsorge nur im Gesetz → neuer Eckwert
  `tarif.kapitalleistung_vorsorge` (alle Jurisdiktionen/Jahre, mit Zitat).

## [2026-11-09] verify | Zweitprüfung aller extrahierten Einträge
- 270 Einträge gegen Chunks geprüft (Sonnet), 226 bestätigt, 44 korrigiert (Fundstellen ergänzt, Unbelegtes gestrichen).

## [2026-11-09] aufbau | Zeitmodell, Nachvollziehbarkeit, Kompakt-Wegleitung
- Registry: zeitbezug/gilt_ab/gilt_bis/ersetzt(_durch) für alle 285 Quellen (Opus, gegengeprüft); quick/gueltigkeit-<jahr>.md;
  ZH-Fristen 2025 auf ZStB 132.1 ab 2026 umgestellt. tools/impact.py + index/abhaengigkeiten.json; Chunk-Pläne ab Textkörper.
- 724 Formularpositionen mit rein/berechnung/beachten (3'469 neue Zitate, Zahlen maschinell geprüft) → quick/wegleitung-*.

## [2026-11-09] query | Experimente in echtem OpenClaw 2026.11.2 (Läufe A/B)
- Retrieval: unicode61 > trigram; angereicherte Kontextzeile MRR 0.28 → 0.36. Agent navigiert v.a. dateibasiert.
- 64 Fragen (Praxis-, Blind-, Positionstest), unabhängig bewertet: A 61/64, B 63/64 voll richtig, 0 falsch → eval/laeufe/.

## [2026-11-09] ingest | Formulare 2026 (UJ) und Abnahme-Paket
- SG Form. 2/4/5/6/7/7Z und ZH Form. 340/360/365/367 (Fassung unterjährige Steuerpflicht 2026) eingelesen; 34 Hilfsblatt-
  Positionen ZH/SG 2026 gegen die Formulare geprüft (33 bestätigt, 1 korrigiert, 169 Formularzitate).
- reports/entscheidungsvorlage-strittig.md (10 Punkte, Recherche + Gegenprüfung, Empfehlungen); tools/abnahme.py mit
  priorisierten Checklisten 2025/2026 für die Fachperson.
