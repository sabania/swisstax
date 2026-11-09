---
typ: beleg
titel: Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht)
jur: multi
beleg: spendenbestaetigung
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht)

> Relevanz: **bedingt** (Bedingt relevant) · ID `spendenbestaetigung` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur Zuwendungen in Geld oder Vermögenswerten an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentliche/gemeinnützige Zwecke); Total muss die Mindestschwelle erreichen (Bund/ZH/SG/AR: Fr. 100; TG kantonal: über Fr. 200) und ist auf 20 % des Nettoeinkommens begrenzt. Nicht abziehbar: Freiwilligenarbeit, Spenden an Geselligkeitsvereine (Musik-/Turnvereine), Parteibeiträge (separater Beleg parteispende), Spenden an Private/Ausland ohne Steuerbefreiung.

## Erkennen an

- Absender: steuerbefreite gemeinnützige Organisation (Stiftung, Verein, Hilfswerk, Kirchgemeinde-Fonds) mit Sitz in der Schweiz
- Titel «Spendenbescheinigung», «Spendenbestätigung», «Zuwendungsbestätigung», «Jahresspendenbescheinigung»; Hinweis «steuerbefreit» / Steuerbefreiungsverfügung
- Typische Begriffe: Spendenbetrag, Datum der Spende, Spender, Empfänger, Zahlungsbeleg/Einzahlungsschein
- Quittung oder Kontoauszug mit Zahlung an die Organisation

## Wofür (Positionen)

- Freiwillige Zuwendungen an gemeinnützige Institutionen `abzug.spenden`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 21.3, Form. 5 S. 2 Teil A |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 21.3, Form. 5 S. 2 Teil A |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 21.3, Form. 5 Rückseite Teil A |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 21.3, Form. 5 (Schulden/Spenden) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 23.2, Form. 6 gemeinnützig |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 23.2, Form. 6 Spalte gemeinnützig (Code 366) |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 22.2 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 22.2 |

## Was extrahieren

- Total der Zuwendungen im Steuerjahr je Empfänger (Name und Sitz der Organisation), Einzelbeträge mit Datum
- Bestätigung der Steuerbefreiung der Organisation (Verzeichnis kantonale Steuerverwaltung)
- Bei Naturalspenden: Wert und Art
- Gesamtbetrag aller Spenden (für Prüfung Mindest- und Höchstgrenze)

## Hinweise

- Mindestschwelle bezieht sich auf das Total aller Zuwendungen im Jahr, nicht auf einzelne Spenden (Bund: Art. 33a DBG, 100 Franken); Obergrenze 20 % des um die Aufwendungen verminderten Nettoeinkommens.
- Pauschalabzüge mit Vermerk «Spenden an diverse Organisationen» werden nicht anerkannt (TG).
- Die einzelnen Zuwendungen sind mit Name und Sitz der Organisation aufzulisten; Belege/Bescheinigungen auf Anforderung vorweisen können.
- Freiwillige Zuwendungen sind steuerlich nicht abziehbar, wenn die Organisation nicht steuerbefreit ist (Steuerstatus beim Sitzkanton klären).
- SG: Zuwendungen für Kultuszwecke sind nicht abziehbar; die Leistung muss völlig uneigennützig sein (WL SG 2025 Ziff. 21.3).

## Kantonale Besonderheiten

- **ZH:** Liste mit allen einzelnen Zuwendungen beilegen, Spendenbescheinigung auf Nachfrage vorweisen; Mindestens CHF 100, max. 20 % des Nettoeinkommens (Info ZH Spenden, WL ZH 2025 Ziff. 22.2). Belege erst auf Verlangen im Einschätzungsverfahren (WL ZH 2025 Beilagen).
- **SG:** Formular 5 Teil A (Ziff. 21.3); Belege sind bereitzuhalten und erst auf Verlangen einzureichen (WL SG 2025).
- **AR:** Formular 5 Teil A (Code 550, Ziff. 21.3); abzugsfähig ist der gesamte Betrag bei mind. Fr. 100, max. 20 % des Nettoeinkommens; Verzeichnis der steuerbefreiten Institutionen mit Sitz in AR im Internet (WL AR 2025 Ziff. 21).
- **TG:** Kantonal nur, wenn die Zuwendungen gesamthaft Fr. 200 übersteigen (bei Nettoeinkommen bis Fr. 40'000 max. Fr. 8'000, sonst max. 20 %); Bund ab Fr. 100. Belege erst ab Fr. 1'000 pro Zuwendung einreichen, darunter auf Verlangen (WL TG 2025 Ziff. 22).

## Quellen

- [DBG Art. 33a](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33a.md) `bund-dbg-2025__art-33a` – «wenn diese Leistungen im Steuerjahr 100 Franken erreichen und insgesamt 20 Prozent der um die Aufwendungen»
- [ZH Spenden](../../chunks/zh/dauernd/zh-info-spenden/zh-info-spenden__c0003.md) `zh-info-spenden__c0003` – «Die Zuwendungen in einem Jahr gesamthaft mindestens CHF 100 betragen.»
- [ZH Spenden](../../chunks/zh/dauernd/zh-info-spenden/zh-info-spenden__c0006.md) `zh-info-spenden__c0006` – «Auf Nachfrage müssen Sie dem Steueramt eine Spendenbescheinigung»
- [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0103.md) `ar-wl-2025__c0103` – «maximal jedoch 20 Prozent des Nettoeinkommens gemäss»
- [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0218.md) `tg-wl-2025__c0218` – «Soweit die freiwilligen Zuwendungen gesamthaft Fr. 200 übersteigen»
- [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0220.md) `tg-wl-2025__c0220` – «Für Zuwendungen unter Fr. 1'000 sind keine Belege einzureichen.»
- [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0102.md) `sg-wl-2025__c0102` – «Als freiwillige Zuwendungen gelten die freiwilligen Leistungen von Geld und»
- [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0102.md) `sg-wl-2025__c0102` – «dungen für Kultuszwecke sind nicht abziehbar.»
