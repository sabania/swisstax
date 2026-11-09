## Steuer-Wiki (Schweiz, natürliche Personen)

Wissensbasis: `steuerwiki/` – Bund + AR/SG/TG/ZH, Steuerjahre 2025/2026. Regeln: `steuerwiki/AGENTS.md` (bei der
ersten Steuerfrage einer Sitzung lesen). Skills: `steuerwiki` (Nachschlagen), `steuererklaerung-np` (ganzer Fall: Belege → Ausfüllhilfe).

- Immer zuerst Kanton (Wohnsitz 31.12.) und Steuerjahr klären.
- Reihenfolge: `steuerwiki/quick/index.md` (Frage → Seite) → `quick/belege-relevanz.md` (relevant?) →
  `quick/zuordnung-<kt>-<jahr>.md` (welche Zahl in welche Ziffer) → `quick/werte-<jur>-<jahr>.md` bzw.
  `quick/vergleich-<jahr>.md` (Limiten) → Detail (↗-Link: `wiki/<jur>/*-detail.md`, `wiki/belege/*`, `wiki/themen/*`)
  → Chunk (`chunks/...`) → Original-PDF (`raw/...`). Suche: `memory_search` mit Kanton + Jahr + Begriff.
- Andere Kantone als AR/SG/TG/ZH sind nicht abgedeckt → «nicht im Wiki» sagen.
- Jede Zahl mit Fundstelle (Chunk-ID oder Dokument + Seite) und Steuerjahr. Kanton (Staats-/Gemeindesteuer) und
  Bund (DBG) getrennt angeben. Status nennen (✅ verifiziert · ☑️ agent-geprüft · 🟡 extrahiert · ⚠️ strittig).
- Werte nie aus anderem Jahr/Kanton übertragen. Fehlt etwas: offen sagen. Fachliche Beurteilung bleibt bei SB/ML.
- Keine Mandantendaten in `steuerwiki/` oder `MEMORY.md` schreiben.
