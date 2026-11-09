---
typ: beleg
titel: Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung)
jur: multi
beleg: kredit-darlehen-schuldzinsen
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung)

> Relevanz: **ja** (Relevant) · ID `kredit-darlehen-schuldzinsen` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Titel «Kreditvertrag», «Darlehensvertrag», «Privatkredit», «Lombardkredit», «Kreditkarten-/Kontokorrentabrechnung mit Sollzinsen»
- Absender: Bank, Kreditinstitut, Leasing-/Kreditgesellschaft oder Privatperson (Familiendarlehen)
- Typische Begriffe: Kreditsumme, Sollzins, Effektivzins, Restschuld per 31.12., bezahlte Zinsen, Gläubiger
- Jahreszinsbescheinigung oder Kontoauszug mit Zinsbelastung

## Wofür (Positionen)

- Private Schuldzinsen `abzug.schuldzinsen`
- Private Schulden (Hypotheken, Darlehen, Kredite) `schulden.privat`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 11, 34.1, Form. 5 Teil A |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 11, 34.1, Form. 5 Teil A |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 11, 34.1, Form. 5 Teil A |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 11, 34.1, Form. 5 (Schulden/Spenden) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 11, 34, Form. 4.1 A |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 11, 34, Form. 4.1 A, Form. 4.1 B |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 12, 34, Form. 355 Spalte Schuld, Form. 355 Spalte Schuldzinsen |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 12, 34 |

## Was extrahieren

- Restschuld per 31.12. – ins Schuldenverzeichnis
- Im Steuerjahr bezahlte Zinsen (ohne Kapitalrückzahlung, ohne Gebühren/Leasingraten)
- Gläubiger mit Name und Adresse, Zinssatz, Zweck/Datum der Aufnahme
- Bei Darlehen unter Nahestehenden (insbesondere von Kapitalgesellschaften an Beteiligte): Vertrag und marktübliche Bedingungen belegen (Art. 33 Abs. 1 lit. a DBG, 2. Satz)

## Hinweise

- Die Schuld muss steuerlich anerkannt sein (Kapitalforderung als Schuld anerkannt); bei Privatdarlehen Gläubiger und Zinssatz belegen.
- Private Schuldzinsen sind auf Vermögenserträge plus Fr. 50'000 begrenzt (Art. 33 Abs. 1 lit. a DBG, kantonal analog).
- Kredit-Zahlungen sind meist Annuitäten: Zins- und Tilgungsanteil trennen; nur der Zinsanteil ist abziehbar. Schuldzinsen auf Geschäftsschulden gehören in die Geschäftsrechnung, nicht in Ziff. Schuldzinsen privat.
- Darlehensforderungen, die der Mandant selber gewährt hat, gehören als Guthaben ins Wertschriften-/Guthabenverzeichnis (Vermögen), Zinsertrag ist steuerbares Einkommen.

## Kantonale Besonderheiten

- **SG:** Private Schulden/Zinsen auf Formular 5 Teil A; geschäftliche Schuldzinsen sind in der Jahresrechnung enthalten und nicht auf Formular 5 aufzuführen (WL SG 2025 Ziff. 11).
- **AR:** Formular 5 Teil A; Total in Ziffer 11 der Steuererklärung (WL AR 2025 Ziff. 11).
- **TG:** Formular 4.1 A/B; Total der Schuldzinsen in Ziff. 11, Schulden in Ziff. 34 (WL TG 2025).
- **ZH:** Schuldenverzeichnis beilegen; Ziff. 12 (WL ZH 2025).

## Quellen

- [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0083.md) `sg-wl-2025__c0083` – «Schuldzinsen sind abzugsfähig, sofern die Kapitalforderung selbst steuerrechtlich»
- [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0081.md) `ar-wl-2025__c0081` – «Zinsen für private Schul-»
- [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «und unbeweglichem Vermögen und weiterer Fr. 50 000 in Abzug bringen»
- [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken»
- [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0074.md) `zh-wl-2025__c0074` – «mögen (inkl. Eigenmietwert) und weiterer CHF 50’000 nicht übersteigen»
