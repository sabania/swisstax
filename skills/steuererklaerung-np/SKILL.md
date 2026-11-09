---
name: steuererklaerung-np
description: Steuererklärung natürliche Person (AR/SG/TG/ZH, Bund) von Belegen bis Ausfüllhilfe – Triage, Zuordnung zu Ziffern/Codes, Limiten, Plausibilisierung.
---

# Steuererklärung natürliche Person – Fall-Ablauf

Wissensbasis: `steuerwiki/` (Regeln `steuerwiki/AGENTS.md`, Abfrage-Skill `steuerwiki`). Ergebnis ist eine
**Ausfüllhilfe mit Fundstellen** für die Fachperson (SB/ML), keine eingereichte Steuererklärung. Die fachliche Verantwortung
bleibt bei der Fachperson; Unsicherheiten werden als offene Punkte ausgewiesen, nie «wegerklärt».

## 1. Rahmen festlegen (vor jeder Zahl)

| Frage | Warum | Wo nachlesen |
|---|---|---|
| Steuerjahr (Steuerperiode)? | Werte/Formulare sind jahresgebunden | `quick/index.md` |
| Wohnsitzkanton am 31.12.? Unterjährige Steuerpflicht (Zuzug/Wegzug/Heirat/Tod)? | bestimmt Formular und Regeln | `wiki/<kt>/<kt>-ueberblick.md`, Themen `ehepaare-familie` |
| Zivilstand / gemeinsame Besteuerung, Kinder (Jahrgang, Ausbildung, Obhut), unterstützte Personen | Sozialabzüge, Tarif, Versicherungsabzug | `wiki/themen/kinder-sozialabzuege.md` |
| Erwerbssituation je Person (unselbständig, selbständig, Rente, Arbeitslos, Nebenerwerb) | Positionen und Pauschalen | `quick/zuordnung-<kt>-<jahr>.md` |
| Liegenschaften (selbstbewohnt/vermietet/andere Kantone) | Eigenmietwert, Unterhalt, Ausscheidung | Themen `liegenschaften-*`, `interkantonale-ausscheidung` |
| Quellensteuer? Auslandseinkünfte? | Sonderverfahren | Themen `quellensteuer`, `wertschriften-verrechnungssteuer` |

## 2. Belege triagieren

Für jedes Dokument mit `quick/belege-relevanz.md`:
1. **Typ erkennen** (Belegkarte `wiki/belege/beleg-<id>.md`, Abschnitt «Erkennen an»; Alltagsbegriffe via `wiki/glossar.md`). Unbekannt → als offener Punkt aufführen.
2. **Relevanz:** ja / bedingt (Bedingung prüfen) / nein (nicht verwenden; begründen).
3. **Werte extrahieren** gemäss Belegkarte «Was extrahieren» – mit Beleg-Referenz (Dateiname/Seite).
4. **Fallen** (aus `hinweise`) sofort prüfen, z.B. Lohnausweis Feld F (kein Fahrkostenabzug), Feld G (Verpflegung
   reduziert), Ziff. 10.2 (PK-Einkauf schon im Nettolohn – nicht doppelt), Ziff. 13.3 (Weiterbildung vom Arbeitgeber).

Fehlende Standardbelege aktiv anfordern (Checkliste): Lohnausweise/Rentenbescheinigungen, Steuerauszug bzw.
Kontoauszüge per 31.12. mit Zinsen, Säule-3a-Bescheinigung, PK-Einkaufsbestätigung, Krankenkassen-Prämienübersicht,
Hypothekar-/Schuldzinsbestätigung, Liegenschaftsunterlagen (Unterhaltsrechnungen, Eigenmietwert/Schätzung),
Kinderbetreuungsrechnungen, Weiterbildungsrechnungen, Spendenbestätigungen, Unterhaltszahlungen, Vorjahresveranlagung.

## 3. Zuordnen und berechnen

Für jeden extrahierten Wert:
1. Ziffer und Feldcode aus `quick/zuordnung-<kt>-<jahr>.md` (Kurzregel; volle Regel/Feld über ↗ in `wiki/<kt>/zuordnung-<kt>-<jahr>-detail.md`) bzw. `quick/belege-ziffern.md`.
2. Limite/Pauschale aus `quick/werte-<kt>-<jahr>.md` (Kanton) **und** `quick/werte-bund-<jahr>.md` (direkte
   Bundessteuer) – Abzüge getrennt rechnen, wo sie sich unterscheiden (Fahrkosten-Maximum, Versicherungsabzug,
   Kinderabzug, Drittbetreuung, Weiterbildung, Zweiverdiener, Parteispenden, Krankheitskosten-Selbstbehalt).
3. Pauschale vs. effektiv: beide rechnen, günstigere Variante wählen, wo das Recht die Wahl lässt (z.B. übrige
   Berufskosten, Liegenschaftsunterhalt je Steuerperiode und Liegenschaft – kantonale Regeln beachten).
4. Plafonierungen anwenden (Fahrkosten, Versicherungen, 3a, Weiterbildung, Drittbetreuung, Spenden in % des Reineinkommens,
   Krankheitskosten-Selbstbehalt in % des Nettoeinkommens).
5. Jede Zahl mit Fundstelle (Chunk-ID) und Status (✅/☑️/🟡/⚠️). Status 🟡 oder ⚠️ → in «offene Punkte».

## 4. Plausibilisieren

- Vermögensvergleich Vorjahr ↔ aktuelles Jahr (Vermögensentwicklung erklärbar durch Einkommen/Verbrauch?).
- Bruttoertrag Wertschriften ↔ Verrechnungssteuer-Anspruch (35 %), Steuerwerte per 31.12. gemäss Kursliste.
- Lohnausweis-Summe ↔ AHV-Einkommen; Nebenerwerb vollständig?
- Schuldzinsen ↔ Schulden per 31.12.; Abzugsgrenze Schuldzinsen (Vermögensertrag + CHF 50'000).
- Kinder: Alter/Ausbildung am 31.12., Alimente vs. Kinderabzug (nicht beides für dasselbe Kind).
- Säule 3a: Maximum mit/ohne 2. Säule; Einkauf ab 2026 nur unter den Voraussetzungen (KS 18a).

## 5. Ausgabe – Ausfüllhilfe

```
Mandant: <Kürzel> · Kanton: <kt> · Steuerjahr: <jahr> · Formular: <aus zuordnung>
| Ziffer | Code | Position | Betrag Kanton | Betrag Bund | Beleg | Regel/Limite | Fundstelle | Status |
|---|---|---|---|---|---|---|---|---|
...
Offene Punkte / Rückfragen an Mandant:
- …
Hinweise für SB/ML (Unsicherheiten, strittige Werte, Ermessen):
- …
```

## 6. Verfahren

Fristen, Fristerstreckung (auch Sammelgesuche für Treuhänder), Abgabeweg (E-Tax/Portal, Unterschrift, Belege),
Bezug/Zinsen: `wiki/themen/fristen-verfahren.md`, `wiki/themen/bezug-zinsen.md`, `wiki/<kt>/<kt>-ueberblick.md`.

## 7. Grenzen

Nicht abgedeckt bzw. nur Übersicht: selbständige Erwerbstätigkeit im Detail (Buchhaltung), Erbschafts-/Schenkungssteuer,
Grundstückgewinnsteuer, juristische Personen, internationale Doppelbesteuerung im Detail. In diesen Fällen: Fachperson
beiziehen, nur Hinweise mit Fundstelle geben. Nie Werte aus einem anderen Jahr/Kanton verwenden.
