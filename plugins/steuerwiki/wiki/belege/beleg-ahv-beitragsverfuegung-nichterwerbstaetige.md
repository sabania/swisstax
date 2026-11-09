---
typ: beleg
titel: AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse)
jur: multi
beleg: ahv-beitragsverfuegung-nichterwerbstaetige
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse)

> Relevanz: **ja** (Relevant) · ID `ahv-beitragsverfuegung-nichterwerbstaetige` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Absender: kantonale Ausgleichskasse / SVA (Sozialversicherungsanstalt)
- Titel «Beitragsverfügung Nichterwerbstätige», «Rechnung AHV/IV/EO-Beiträge», «Beitragsrechnung für Nichterwerbstätige»
- Begriffe: Beitragspflicht Nichterwerbstätige, Vermögen/Renteneinkommen als Bemessungsgrundlage, Beitragsperiode, Verwaltungskostenbeitrag
- Beiträge für AHV, IV und EO (ggf. Familienausgleichskasse bei Kantonen mit FAK-Beitrag)

## Wofür (Positionen)

- AHV/IV/EO-Beiträge Nichterwerbstätiger u.ä. `abzug.ahv_nichterwerbstaetige`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 16.6 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 16.6 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 16.5 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 16.5 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 15.1 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 15.1 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 16.1 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 16.1 |

## Was extrahieren

- Im Steuerjahr bezahlte AHV/IV/EO-Beiträge (ohne Verwaltungskosten, falls getrennt ausgewiesen)
- Beitragsperiode (Zahlungsjahr vs. Verfügungsjahr: nur im Steuerjahr geleistete Beträge)
- Nachzahlungen/Akontobeiträge getrennt von Vorauszahlungen

## Hinweise

- Beiträge Nichterwerbstätiger an die AHV, IV und EO sind abziehbar; bei Erwerbstätigen sind AHV-Beiträge bereits im Nettolohn/Reingewinn berücksichtigt und dürfen nicht nochmals abgezogen werden.
- Zahlungsnachweis (Rechnung inkl. Zahlungsbeleg) ist massgebend, nicht die Verfügung allein.
- Familienausgleichskassen-(FAK-)Beiträge Nichterwerbstätiger: im Kanton TG ebenfalls dort einzutragen (WL TG 2025).

## Kantonale Besonderheiten

- **ZH:** Abzug unter Ziff. 16.1 «Beiträge an die AHV, IV und 2. Säule, sofern nicht unter Ziff. 1 und 2 abgezogen».
- **SG:** Ziff. 16.5 übrige Abzüge: AHV-Beiträge von nichterwerbstätigen Steuerpflichtigen (ordentliche AHV-Beiträge sind in Ziff. 1 und 2 bereits berücksichtigt).
- **TG:** Ziff. 15.1: nur Beiträge an AHV/IV/EO sowie FAK-Beiträge von nichterwerbstätigen Personen; Beiträge von Selbständigen im Reingewinn, von Angestellten im Nettolohn berücksichtigt.
- **AR:** Ziff. 16.6 übrige Abzüge: AHV-Beiträge von nichterwerbstätigen steuerpflichtigen Personen.

## Quellen

- [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0052.md) `bund-wl-2a-2025__c0052` – «Beiträge Nichterwerbstätiger an die AHV, IV und EO.»
- [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0093.md) `tg-wl-2025__c0093` – «können daher hier nicht nochmals abgezogen werden.»
- [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0097.md) `sg-wl-2025__c0097` – «AHV-Bei-     träge von nichterwerbstätigen Steuerpflichtigen»
- [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0077.md) `zh-wl-2025__c0077` – «Beiträge an die AHV, IV und 2. Säule, sofern nicht unter Ziff. 1 und 2 abgezogen»
- [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0094.md) `ar-wl-2025__c0094` – «Beiträge von nichterwerbstätigen steuerpflichtigen Personen»
