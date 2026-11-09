---
typ: beleg
titel: Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten)
jur: multi
beleg: selbstaendig-jahresrechnung
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten)

> Relevanz: **ja** (Relevant) · ID `selbstaendig-jahresrechnung` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Titel «Jahresabschluss», «Bilanz und Erfolgsrechnung», «Einnahmen-/Ausgabenrechnung», «Buchhaltung», «Betriebsabrechnung»
- Absender: Treuhänder/Buchhalter/Mandant selbst; Buchhaltungssoftware-Export (Abacus, Bexio, Banana)
- Begriffe: Reingewinn, Eigenkapital, Privatbezüge/-einlagen, Abschreibungen, Rückstellungen, Warenlager, Debitoren
- Beilagen: Eigenkapital-/Privatkontoauszug, Abschreibungstabelle, Aktiven-/Passiven-Aufstellung

## Wofür (Positionen)

- Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft) `einkommen.selbstaendig`
- Übrige Vermögenswerte `vermoegen.uebrige`
- Beiträge Säule 3a (inkl. Einkäufe ab 2026) `abzug.vorsorge.saeule3a`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 2.1, 2.2, 4.3, 32.1, 32.2, 32.3, 34.2, Form. 5 Teil B |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 2.1, 2.2, 4.3, 32.1, 32.2, 32.3, 34.2, Form. 5 Teil B |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 2.1, 2.2, 4.3, 32.1-32.3, 34.2, Form. 5 Teil B |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 2.1, 2.2, 4.3, 32.1-32.3, 34.2 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 2.1, 2.2, 23.3, 32.1, 32.2–32.5, 32.6, Form. 4.1 B |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 2.1, 2.2, 23.3, 32, Form. 4.1 B |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 2.1, 2.2, 32 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 2.1, 2.2, 16.5 (übrige), 32 |

## Was extrahieren

- Reingewinn bzw. -verlust des im Steuerjahr abgeschlossenen Geschäftsjahres (Erfolgsrechnung)
- Eigenkapital per Bilanzstichtag (Geschäftsvermögen für die Vermögenssteuer)
- Privatbezüge/-einlagen, Privatanteile (z.B. Fahrzeug, Wohnung) laut Privatkonto
- Abschreibungen, Rückstellungen, Liquidationsgewinne/Kapitalgewinne separat ausweisen
- Beiträge des Selbständigen an die 2. Säule (inkl. Einkäufe) und Säule 3a: nicht in der Erfolgsrechnung, sondern bei den Abzügen (AR Ziff. 13). AHV/IV/EO-Beiträge sind bereits im Reingewinn berücksichtigt und nicht nochmals abzuziehen (TG Ziff. 15.1)

## Hinweise

- Bilanzen und Erfolgsrechnungen der im Steuerjahr abgeschlossenen Geschäftsjahre sind zwingend beizulegen; auch bei nebenberuflicher Tätigkeit besteht Buchführungs-/Aufzeichnungspflicht.
- Fehlt eine eigentliche Jahresrechnung, ist mindestens eine Einnahmen-Ausgaben-Rechnung samt Aktiven/Passiven (Vermögensübersicht) und Privatentnahmen/-einlagen einzureichen.
- Private Lebenshaltungskosten (z.B. persönliche Versicherungsbeiträge) dürfen nicht der Erfolgsrechnung belastet werden (Art. 34 lit. a DBG).
- Beteiligungen an Kollektiv-/Kommanditgesellschaften bzw. einfachen Gesellschaften: Angaben der Gesellschaft (Bescheinigung/Hilfsblatt) statt eigener Bilanz.
- Liquidationsgewinne in der Jahresrechnung sind in einer separaten Beilage auszuweisen (SG).

## Kantonale Besonderheiten

- **ZH:** Bei kaufmännischer Buchführung: unterzeichnete Jahresrechnung (Bilanz, Erfolgsrechnung, Anhang) plus Kontoblätter sämtlicher Privat- und Eigenkapitalkonten und Hilfsblatt Selbständige Erwerbstätigkeit; Patentbox/F&E-Zusatzabzug nur mit Form. 547.
- **SG:** Bilanz, Erfolgsrechnung, Eigenkapitalkonti (Privatkonti) und Abschreibungstabellen beilegen; Kollektiv-/Kommanditgesellschaften über Formular 11 (Ziff. 2.2).
- **TG:** Immer einzureichen (auch elektronisch): Aufstellung über Einnahmen/Ausgaben sowie Aktiven/Passiven oder Bilanz und Erfolgsrechnung.
- **AR:** Aufstellung über Aktiven/Passiven, Einnahmen/Ausgaben sowie Privatentnahmen und -einlagen ist in jedem Fall beizufügen; ohne Jahresrechnung Einnahmen-Ausgaben-Rechnung plus Vermögensübersicht.

> Bemerkung: korrigiert durch Prüfung: AHV/IV/EO-Beiträge Selbständiger sind laut WL TG im Reingewinn berücksichtigt, nicht separat abziehbar (vorher mit 2. Säule/3a gleichgestellt).

## Quellen

- [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0045.md) `sg-wl-2025__c0045` – «Steuererklärung sind die»
- [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0039.md) `ar-wl-2025__c0039` – «Die Pflicht zur Führung von Geschäfts»
- [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0039.md) `ar-wl-2025__c0039` – «ist eine Einnahmen-Ausgaben-Rechnung sowie»
- [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0039.md) `zh-wl-2025__c0039` – «reichen Sie eine unterzeichnete Jahresrechnung (Einzelabschluss»
- [WL TG 2025 S. 10](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0035.md) `tg-wl-2025__c0035` – «bei selbständiger Erwerbstätigkeit Aufstellungen über die Einnahmen und Ausgaben sowie über»
- [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0084.md) `ar-wl-2025__c0084` – «dürfen deshalb nicht der Erfolgsrechnung belastet werden.»
- [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0093.md) `tg-wl-2025__c0093` – «sind im Reingewinn (Ziff. 2.1 bzw. Ziff. 2.2) zu berücksichtigen.»
