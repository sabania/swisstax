---
name: steuerwiki
description: Schweizer Steuerwissen (Bund, AR, SG, TG, ZH; Steuerjahre 2025/2026) – Belege prüfen, Formularziffern und Abzugslimiten mit Fundstelle nachschlagen.
---

# Steuer-Wiki nutzen (Abfrage)

Wissensbasis im Workspace unter `steuerwiki/` (Pfad ggf. anpassen). Regeln: `steuerwiki/AGENTS.md` (vor der ersten
Antwort einer Sitzung lesen). Antworten immer mit **Kanton**, **Steuerjahr**, **Fundstelle** und **Status**.

## Ablauf

1. **Kanton + Steuerjahr festlegen.** Wohnsitzkanton am 31.12. des Steuerjahres. Unklar → nachfragen.
2. **Quick-Layer zuerst** (kompakte Tabellen, mit `read` öffnen; Spalte ↗ führt zur Detailstelle):
   - `steuerwiki/quick/index.md` – «Welche Frage → welche Seite», Matrix Kanton × Jahr, Datenstand/Lücken, Themen
   - `steuerwiki/quick/belege-relevanz.md` – Ist ein Dokument steuerrelevant? (ja / bedingt / nein) → Detailkarte
     `steuerwiki/wiki/belege/beleg-<id>.md` (Erkennen an, Was extrahieren, Hinweise je Kanton, Ziffern je Kanton/Jahr)
   - `steuerwiki/quick/belege-ziffern.md` – Beleg × Kanton/Jahr → Ziffern (Matrix)
   - `steuerwiki/quick/wegleitung-<kt>-<jahr>.md` – **Kompakt-Wegleitung**: je Formularziffer Rein (Dokumente → Feld) ·
     Rechnen (Kurzformel) · Limite Kanton/Bund · Beachten; `grep -n "^### <ziffer>"` springt zur Position
   - `steuerwiki/quick/zuordnung-<kt>-<jahr>.md` – Ziffer · Position · Beleg · Kurzregel · Limite Kanton/Bund (Tabelle)
   - `steuerwiki/quick/werte-<jur>-<jahr>.md` – Eckwerte (Pauschalen, Maxima, Sätze) mit Fundstelle und Status
   - `steuerwiki/quick/vergleich-<jahr>.md` – alle Jurisdiktionen nebeneinander (schnellster Weg für Vergleichsfragen)
   - `steuerwiki/quick/gueltigkeit-<jahr>.md` – welche Fassung (Gesetz, Wegleitung, Fristen-Weisung, KS) für Steuerjahr X gilt
3. **Detail:** `steuerwiki/wiki/<jur>/zuordnung-<kt>-<jahr>-detail.md` bzw. `werte-<jur>-<jahr>-detail.md` (volle Regel,
   Bund-Hinweis, Bemerkung, **wörtliche Zitate** je Quelle) · `steuerwiki/wiki/themen/<thema>.md` (Querschnitt, Sonderfälle,
   Checklisten) · `steuerwiki/wiki/<jur>/<jur>-ueberblick.md` (Verfahren, Fristen, Behörden) · Quellenkatalog
   `steuerwiki/wiki/<jur>/<jur>-quellen.md`. Grosse Seiten gezielt lesen (`grep -n "<schlüssel oder ziffer>"`, dann Zeilenbereich).
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

Für jedes Dokument: Typ erkennen (`belege-relevanz.md` → Detailkarte, Abschnitt «Erkennen an») → relevant / bedingt /
nicht relevant → bei relevant: Felder gemäss «Was extrahieren» lesen → Ziffer gemäss `zuordnung-<kt>-<jahr>.md` → Limite prüfen
(`werte-…`) → Belegpflicht/Schwellen beachten (Werte `verfahren.beilagen_schwellen`). Mandantendaten nie ins Wiki schreiben.

## Häufige Fallen (aus dem Praxistest)

- **Schwellen gelten für das Jahrestotal:** Spenden Bund ab CHF 100, TG kantonal erst über CHF 200 – eine Einzelspende unter
  der Schwelle zählt nur, wenn das Total die Schwelle erreicht.
- **Kein Doppelabzug:** PK-Einkauf via Lohnabzug (Lohnausweis Ziff. 10.2) steckt im Nettolohn; nur direkt bezahlte Einkäufe
  separat abziehen. Feld F (Gratis-Arbeitsweg) → kein Fahrkostenabzug.
- **Bund ≠ Kanton:** Fahrkosten-Maximum, Kinderabzug, Versicherungsabzug, Weiterbildung haben je eigene Beträge; Zweiverdiener-
  abzug z.B. in TG nur beim Bund. Immer beide Spalten ausweisen.
- **Altersstaffeln:** AR/SG/TG-Kinderabzüge je Alters-/Ausbildungsstufe (`sozialabzug.kind_vorschule` / `kind_schule` /
  `kind_ausbildung`), nicht `sozialabzug.kind`.
- **2026 = teils provisorisch:** ZH/SG 2026 nur Formular für unterjährige Steuerpflicht, AR 2026 Gerüst ohne Formular
  (siehe `quick/index.md` → Datenstand). Status ⬜ offen heisst: Wert fehlt – nicht aus 2025 übernehmen.
- **Strittig (⚠️):** beide Quellen nennen und auf die Fachperson verweisen (`reports/offene-punkte.md`).
