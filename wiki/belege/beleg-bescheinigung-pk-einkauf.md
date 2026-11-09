---
typ: beleg
titel: Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP)
jur: multi
beleg: bescheinigung-pk-einkauf
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP)

> Relevanz: **ja** (Relevant) · ID `bescheinigung-pk-einkauf` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Absender: Pensionskasse, Vorsorgestiftung, Sammelstiftung
- Titel «Bescheinigung über Vorsorgebeiträge», Formular 21 EDP (Ziffer 1: Beiträge an Einrichtungen der 2. Säule, auch Einkäufe von Beitragsjahren)
- Begriffe: Einkaufssumme, Einkauf Beitragsjahre, freiwillige Einlage, Einkaufsberechnung/Einkaufsmöglichkeit
- Zahlungsdatum der Einzahlung

## Wofür (Positionen)

- Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen) `abzug.vorsorge.saeule2_einkauf`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 13.2 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 13.2 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 13.2, Lohnausweis Ziff. 10.2 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 13.2, Lohnausweis Ziff. 10.2 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 15.2 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 15.2 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 16.1, Lohnausweis Ziff. 10.2 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 16.1 |

## Was extrahieren

- Total der im Steuerjahr geleisteten Einkaufsbeiträge (jede Einzahlung mit genauem Datum)
- Ordentliche Beiträge, soweit nicht bereits im Lohnausweis (Ziff. 10) abgezogen
- Ggf. Einkaufsberechnung/Einkaufspotenzial; Hinweis auf frühere WEF-Vorbezüge

## Hinweise

- Einkäufe von Beitragsjahren: massgebend ist das Jahr der effektiven Zahlung (nicht der Verbuchung); bei ordentlichen und Erhöhungsbeiträgen das Jahr, für das sie bestimmt sind und fakturiert werden.
- 3-Jahres-Sperrfrist: Einkäufe sind steuerlich nicht abziehbar, soweit innerhalb von drei Jahren ein Kapitalbezug erfolgt; Einkauf erst nach Rückzahlung früherer WEF-Vorbezüge zulässig (Art. 79b Abs. 3 BVG).
- Rückzahlungen von WEF-Vorbezügen sind keine abziehbaren Einkäufe (separates WEF-Formular, nicht Formular 21 EDP).
- Vom Lohn abgezogene Einkäufe sind im Lohnausweis (Ziff. 10.2) bescheinigt; selbst überwiesene nur mit Formular 21 EDP der Vorsorgeeinrichtung – nicht doppelt abziehen.

## Kantonale Besonderheiten

- **AR:** Bescheinigung der Vorsorgeträgerin ist in jedem Fall zusammen mit der Einkaufsberechnung beizulegen; Selbständigerwerbende deklarieren immer 100 % der Einkaufsbeiträge (WL AR 2025 Ziff. 13.2).
- **ZH:** Abziehbare Einkaufsbeiträge sind der Bescheinigung der Vorsorgeeinrichtung zu entnehmen (Ziff. 16.1); Sperrfrist 3 Jahre (WL ZH 2025 Ziff. 16.1).
- **TG:** Kapitalbezug innerhalb von 3 Jahren nach Einkauf und WEF-Vorbezug: siehe TG FAQ Vorsorge 2. und 3. Säule.

> Bemerkung: korrigiert durch Prüfung: Formulartitel und Zuordnungsjahr präzisiert (ordentliche vs. Einkaufsbeiträge, MB 21 EDP Rz 16).

## Quellen

- [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0092.md) `zh-wl-2025__c0092` – «Die abziehbaren Einkaufsbeiträge sind der von der Vorsorgeeinrichtung ausgestellten»
- [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0092.md) `zh-wl-2025__c0092` – «Einkäufe steuerlich nicht zum Abzug zugelassen»
- [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0084.md) `ar-wl-2025__c0084` – «Der Steuererklärung ist in jedem Fall die Bescheinigung der Vorsorgeträgerin bei»
- [MB 21 EDP S. 3–4](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0009.md) `bund-mb-21edp__c0009` – «Massgebend für die Zuordnung bei Einkäufen von Beitragsjahren ist das Jahr»
- [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0028.md) `tg-info-faq__c0028` – «Gemäss Artikel 79b Absatz 3 Satz 2 BVG darf ein Einkauf von Beitragsjahren erst vorgenommen werden»
- [MB 21 EDP S. 3](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0008.md) `bund-mb-21edp__c0008` – «Die Rückzahlung eines Vorbezugs für Wohneigentum (WEF-Vorbezug)»
