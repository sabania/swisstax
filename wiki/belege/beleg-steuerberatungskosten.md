---
typ: beleg
titel: Rechnung Steuerberatung / Steuererklärungs-Ausfertigung (Treuhänder, Steuerberater)
jur: multi
beleg: steuerberatungskosten
relevanz: nein
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Rechnung Steuerberatung / Steuererklärungs-Ausfertigung (Treuhänder, Steuerberater)

> Relevanz: **nein** (Nicht relevant) · ID `steuerberatungskosten` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Begründung:** Kosten für Steuerberatung und Ausfertigung der Steuererklärung im Privatvermögen sind nicht abziehbar: sie gelten weder als Vermögensverwaltungskosten (Bund: ausdrücklich nicht zulässig) noch als Gewinnungskosten, sondern als Lebenshaltungskosten (Art. 34 lit. a DBG). SG/AR führen Steuerberatung ausdrücklich unter den nicht abzugsfähigen Kosten.

## Erkennen an

- Absender: Treuhandbüro, Steuerberater, Rechtsanwalt, Steuerexperte
- Titel «Honorarrechnung», «Rechnung Ausfertigung Steuererklärung», «Beratungshonorar Steuern/Nachlass»
- Begriffe: Ausfertigung der Steuererklärung, Steuerberatung, Erbschaftsberatung, Einsprache, Honorar nach Aufwand
- Rechnungsstellung an Privatperson (nicht an Firma)

## Wofür (Positionen)

- Vermögensverwaltungskosten bewegliches Vermögen `abzug.verwaltungskosten_wertschriften`
- Übrige Abzüge `abzug.uebrige`

## Was extrahieren

- Nichts für den Abzug. Allenfalls prüfen, ob ein Teil geschäftlich veranlasst ist (selbständige Erwerbstätigkeit: Aufwand der Jahresrechnung) – dann in Buchhaltung des Betriebs, nicht privat.

## Hinweise

- Für Selbständigerwerbende kann der geschäftsbezogene Teil Geschäftsaufwand sein; Aufteilung privat/geschäftlich nachvollziehbar belegen (Quelle dazu im Wiki nicht verifiziert – Fachperson).
- Kosten einer Einsprache oder eines Rechtsmittelverfahrens: Abzugsfähigkeit im Wiki nicht verifiziert; im Zweifel nicht abziehen.
- Nicht zu verwechseln mit abziehbarer Berufs-/Weiterbildung oder Liegenschaftsunterhalt; Rechnung dem passenden Beleg-Typ zuordnen.

## Kantonale Besonderheiten

- **SG:** Als nicht abzugsfähige Verwaltungskosten ausdrücklich aufgeführt: Finanz-, Anlage-, Erbschafts-, Vorsorge- und Steuerberatung (Ziff. 16.1).
- **AR:** Wie SG: Finanz-, Anlage-, Erbschafts-, Vorsorge- und Steuerberatung nicht abzugsfähig (Ziff. 16).

## Quellen

- [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0057.md) `bund-wl-2a-2025__c0057` – «für Steuerberatung, Ausfertigung von Steuererklärungen und»
- [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0091.md) `sg-wl-2025__c0091` – «die Finanz-, Anlage-, Erbschafts-, Vorsorge- und Steuerberatung;»
- [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0088.md) `ar-wl-2025__c0088` – «die Finanz-, Anlage-, Erbschafts-, Vorsorge- und Steuerberatung;»
- [DBG Art. 34](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-34.md) `bund-dbg-2025__art-34` – «die Aufwendungen für den Unterhalt des Steuerpflichtigen und seiner Familie»
