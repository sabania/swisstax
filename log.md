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
