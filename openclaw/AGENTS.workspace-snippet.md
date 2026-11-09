## Steuer-Wiki (Schweiz, natürliche Personen)

Wissensbasis: `steuerwiki/` – Bund + AR/SG/TG/ZH, Steuerjahre 2025/2026. Regeln: `steuerwiki/AGENTS.md` (bei der
ersten Steuerfrage einer Sitzung lesen). Skill `steuerwiki` beschreibt den Ablauf.

- Immer zuerst Kanton (Wohnsitz 31.12.) und Steuerjahr klären.
- Reihenfolge: `steuerwiki/quick/index.md` → `quick/belege-relevanz.md` (relevant?) → `quick/zuordnung-<kt>-<jahr>.md`
  (welche Zahl in welche Ziffer) → `quick/werte-<jur>-<jahr>.md` (Limiten) → `wiki/themen/*` → Chunk (`chunks/...`)
  → Original-PDF (`raw/...`). Suche: `memory_search` mit Kanton + Jahr + Begriff.
- Jede Zahl mit Fundstelle (Chunk-ID oder Dokument + Seite) und Steuerjahr. Kanton (Staats-/Gemeindesteuer) und
  Bund (DBG) getrennt angeben. Status nennen (✅ verifiziert · ☑️ agent-geprüft · 🟡 extrahiert · ⚠️ strittig).
- Werte nie aus anderem Jahr/Kanton übertragen. Fehlt etwas: offen sagen. Fachliche Beurteilung bleibt bei SB/ML.
- Keine Mandantendaten in `steuerwiki/` oder `MEMORY.md` schreiben.
