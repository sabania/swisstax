---
name: steuerwiki
description: Schweizer Steuerwissen (Bund, AR, SG, TG, ZH; Steuerjahre 2025/2026) – Belege prüfen, Formularziffern und Abzugslimiten mit Fundstelle nachschlagen.
---

# Steuer-Wiki nutzen (Abfrage)

Wissensbasis im Workspace unter `steuerwiki/` (Pfad ggf. anpassen). Regeln: `steuerwiki/AGENTS.md` (vor der ersten
Antwort einer Sitzung lesen). Antworten immer mit **Kanton**, **Steuerjahr**, **Fundstelle** und **Status**.

## Ablauf

1. **Kanton + Steuerjahr festlegen.** Wohnsitzkanton am 31.12. des Steuerjahres. Unklar → nachfragen.
2. **Quick-Layer zuerst** (kleine Dateien, mit `read` öffnen):
   - `steuerwiki/quick/index.md` – Matrix Kanton × Jahr
   - `steuerwiki/quick/belege-relevanz.md` – Ist ein Dokument steuerrelevant? Was daraus extrahieren?
   - `steuerwiki/quick/zuordnung-<kt>-<jahr>.md` – Beleg/Feld → Formularziffer, Limiten Kanton und Bund
   - `steuerwiki/quick/werte-<jur>-<jahr>.md` – Eckwerte (Pauschalen, Maxima, Sätze) mit Fundstelle
   - `steuerwiki/quick/vergleich-<jahr>.md` – alle Jurisdiktionen nebeneinander
3. **Detail:** `steuerwiki/wiki/themen/<thema>.md` (Querschnitt mit Fundstellen), `steuerwiki/wiki/<jur>/<jur>-ueberblick.md`,
   Quellenkatalog `steuerwiki/wiki/<jur>/<jur>-quellen.md`.
4. **Belegstelle öffnen:** verlinkten Chunk lesen (`steuerwiki/chunks/...`). Bei Tabellen/Formularen das Original
   (`steuerwiki/raw/...pdf`, Seite aus `seiten:`) prüfen.
5. **Suche, wenn nicht abgedeckt:** `memory_search` mit Kanton + Jahr + Fachbegriff, z.B.
   `"Fahrkosten Abzug ZH 2025"`, `"Art. 33 DBG Versicherungsprämien 2026"`, `"Liegenschaftsunterhalt Pauschale TG"`.
   Treffer nur verwenden, wenn `jur` (bzw. `bund`) und `jahre` passen (Frontmatter des Chunks).
   Alltagsbegriffe zuerst übersetzen (`steuerwiki/wiki/glossar.md`, z.B. Kita → Drittbetreuung, Alimente → Unterhaltsbeiträge).
   Ohne OpenClaw-Suche: `python3 steuerwiki/tools/search.py "<Begriffe>" --jur <kt>,bund --jahr <jahr> --expand`.
   **Unsicher oder widersprüchlich?** Die ganze Quelle lesen (`steuerwiki/sources/<jur>/<jahr>/<id>.md`, z.B. die
   Wegleitung des Jahres) statt sich auf einzelne Chunks zu verlassen; bei Tabellen das Original-PDF prüfen.
6. **Antwort:** Ergebnis · Kanton/Bund getrennt · Steuerjahr · Fundstelle(n) als Chunk-ID/Dokument+Seite · Status
   (✅ verifiziert, ☑️ agent-geprüft, 🟡 extrahiert, ⚠️ strittig). Werte nie aus einem anderen Jahr/Kanton übernehmen.

## Belege eines Mandanten triagieren

Für jedes Dokument: Typ erkennen (`belege-relevanz.md`, Spalte «Erkennen an») → relevant / bedingt / nicht relevant →
bei relevant: Felder gemäss «Was extrahieren» lesen → Ziffer gemäss `zuordnung-<kt>-<jahr>.md` → Limite prüfen
(`werte-…`) → Belegpflicht/Schwellen beachten (Werte `verfahren.beilagen_schwellen`). Mandantendaten nie ins Wiki schreiben.
