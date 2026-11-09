---
typ: beleg
titel: Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand)
jur: multi
beleg: krypto-auszug
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand)

> Relevanz: **bedingt** (Bedingt relevant) · ID `krypto-auszug` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur wenn Kryptowährungen gehalten werden (Bestand per 31.12. und Erträge wie Staking/Lending deklarieren).

## Erkennen an

- Absender: Krypto-Börse/-Broker (z.B. Bitcoin Suisse, Kraken, Binance, Bitpanda) oder Wallet-Export
- Begriffe: Bestand per 31.12., Kurs/Jahresendkurs, Staking-/Lending-Erträge, Transaktionshistorie
- Bitcoin, Ether, XRP, Bitcoin Cash, EOS und weitere Kryptowährungen

## Wofür (Positionen)

- Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto) `vermoegen.wertschriften_guthaben`
- Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis) `einkommen.wertschriften`
- Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …) `einkommen.uebrige`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 4.1, 30.1, Form. 2 Spalten A/B |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 4.1, 30.1, Form. 2 Spalten A/B |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 4.1, 30.1 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 4.1, 30.1 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 4, 30.1, Form. 2 Spalten 7–9 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 30.1, Form. 2 Spalten 1–9 (Seite 2/3) |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 4.1, 30.1, Form. 340 Kolonne B |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 4.1, 30.1 |

## Was extrahieren

- Bestand je Kryptowährung per 31.12. (Anzahl) und Wert in CHF zum ESTV-Jahresendkurs
- Erträge des Jahres: Staking, Lending, Zinsen, Airdrops, Mining (je Quelle)
- Plattform/Wallet und Adresse (Nachweis des Eigentums)

## Hinweise

- Kryptowährungen sind Vermögen (Wertschriften- und Guthabenverzeichnis); für Bitcoin und weitere geläufige Kryptowährungen publiziert die ESTV einen Jahresendsteuerkurs, andere zum Jahresschlusskurs der gängigsten Börsenplattform.
- Nachweis durch Kontoauszug der Plattform bzw. der digitalen Brieftasche (Wallet), Stand per Ende der Steuerperiode.
- Erträge aus Staking, Lending usw. sind Einkommen; Kursgewinne bei privater Haltung grundsätzlich steuerfrei, bei gewerbsmässigem Handel jedoch Einkommen – Einzelfallprüfung durch die Fachperson.
- Verluste auf Kryptowerten sind im Privatvermögen nicht abziehbar (Art. 34 DBG); ausländische Plattformen ohne Steuerauszug: Auszug zwingend selbst beschaffen.

## Kantonale Besonderheiten

- **SG:** Kryptowährungen ausdrücklich im Wertschriften- und Guthabenverzeichnis anzugeben (Bitcoin, Ether, XRP, Bitcoin Cash, EOS etc.) (WL SG 2025).
- **AR:** Kryptowährungen wie Bitcoin und Ether im Formular 2 anzugeben; Stichtag 31.12. (WL AR 2025).
- **ZH:** Nachweis mittels Wallet-/Plattformauszug per Ende der Steuerperiode; ESTV-Jahresendkurs (WL ZH 2025 Guthaben und Kryptowährungen).

> Bemerkung: Relevanz auf bedingt korrigiert durch Prüfung. TG: keine kantonale Krypto-Aussage in der Wegleitung gefunden. Steuerfreiheit privater Kursgewinne ist hier nicht mit Chunk belegt (Fachperson beurteilt).

## Quellen

- [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0159.md) `zh-wl-2025__c0159` – «Andere Kryptowährungen sind zum Jahresschlusskurs der für diese Währung gängigsten Börsenplattform zu deklarieren.»
- [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0159.md) `zh-wl-2025__c0159` – «Der Nachweis hat mittels Kontoauszug der digitalen Brieftasche»
- [WL SG 2025 S. 35–36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0121.md) `sg-wl-2025__c0121` – «inkl. Kryptowährungen»
- [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0128.md) `ar-wl-2025__c0128` – «(inkl. Kryptowäh-»
- [DBG Art. 34](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-34.md) `bund-dbg-2025__art-34` – «die Aufwendungen für die Anschaffung, Herstellung oder Wertvermehrung von Vermögensgegenständen»
