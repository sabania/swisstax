---
name: steuerwiki
description: Steuerfachfragen Schweiz (Bund, AR, SG, TG, ZH; Steuerjahre 2025/2026) – Abzüge, Limiten, Pauschalen, Formularziffern, Fristen, Zinsen mit Fundstelle beantworten. Verwenden bei jeder inhaltlichen Steuerfrage.
---

# Steuerfachfragen beantworten

Werkzeug: Tools `steuerwiki__wert`, `__position`, `__beleg`, `__suche`, `__zeige` (ohne Plugin: `python3 steuerwiki/tools/steuer.py <befehl> …`).
Jede Ausgabe enthält schon Fundstelle (Chunk-ID) und Status – übernehmen, nicht neu erfinden.

## Ablauf (in dieser Reihenfolge, meist reichen 1–3 Aufrufe)

1. **Kanton + Steuerjahr** festlegen: Kanton = Wohnsitz am 31.12. (fehlt er → nachfragen); fehlt das Jahr → 2025 verwenden und nennen.
   Kanton nicht AR/SG/TG/ZH → «nicht im Wiki».
2. **Zahl/Limite/Pauschale/Frist/Zins** → `wert <jur> <jahr> <stichwort>` (Kanton liefert Bundeswert mit). Nur Bund → `wert bund <jahr> …`.
3. **Formularziffer, «wo eintragen», «wie rechnen»** → `position <kt> <jahr> <ziffer|stichwort>`.
4. **Dokument/Beleg** → `beleg <stichwort> --kanton <kt> --jahr <jahr>`.
5. **Nichts Passendes?** → `suche "<2–4 Fachbegriffe>" --jur <kt> --jahr <jahr>` (auch `--jur bund`), dann `zeige <chunk-id>`
   und die Stelle wörtlich lesen. Alltagswörter in Fachbegriffe übersetzen (Kita → Drittbetreuung, Alimente → Unterhaltsbeiträge,
   Pendler → Fahrkosten, 3a → gebundene Selbstvorsorge).
6. **Antwort:** Ergebnis · Kanton und Bund getrennt · Steuerjahr · Fundstelle(n) (Chunk-ID) · Status. Fehlt ein Wert: sagen.

## Status lesen
✅ verifiziert (Fachperson) · ☑️ agent-geprüft = Fundstelle geprüft, fachliche Abnahme offen · 🟡 extrahiert (ungeprüft) ·
⚠️ strittig = Quellen widersprechen sich → beide nennen, Fachperson entscheidet · ⬜ offen = kein Wert → nicht aus Vorjahr übernehmen.

## Häufige Fallen
- **Bund ≠ Kanton:** Fahrkosten-Maximum, Kinderabzug, Versicherungsabzug, Weiterbildung, Drittbetreuung, Zweiverdiener je eigene Beträge.
- **Altersstufen:** AR/SG/TG-Kinderabzüge je Stufe (`kind_vorschule`, `kind_schule`, `kind_ausbildung`).
- **Schwellen gelten fürs Jahrestotal** (z.B. Mindestbetrag Spenden: `wert bund <jahr> spenden`).
- **Kein Doppelabzug:** PK-Einkauf via Lohn (Lohnausweis Ziff. 10.2) steckt im Nettolohn; Feld F (Gratis-Arbeitsweg) → keine Fahrkosten.
- **«bedingt»** heisst relevant, wenn die Bedingung zutrifft – als bedingt mit Bedingung nennen.
- **2026 teils provisorisch** (ZH/SG 2026 nur Formulare für unterjährige Steuerpflicht; AR 2026 lückenhaft).
- **Zeitbezug:** Tools immer mit dem Steuerjahr der Erklärung aufrufen – die Ausgabe berücksichtigt, dass Fristen/Verfahren der
  Erklärung X aus der Fassung X+1 stammen (Frist der Erklärung 2025 = `wert <kt> 2025 einreichefrist`). Zinsen: Jahr der Zahlung.

## Vertiefung (nur wenn nötig)
`zeige quick/index.md` (Frage → Seite) · `zeige quick/wegleitung-<kt>-<jahr>.md --abschnitt "<ziffer>"` ·
`zeige wiki/<kt>/zuordnung-<kt>-<jahr>-detail.md --abschnitt "<ziffer>"` (alle Zitate) · `zeige wiki/themen/<thema>.md`.
