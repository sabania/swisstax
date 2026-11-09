---
typ: beleg
titel: Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.)
jur: multi
beleg: depotauszug
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.)

> Relevanz: **ja** (Relevant) · ID `depotauszug` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Titel «Depotauszug», «Depotverzeichnis», «Vermögensausweis», «Portfolio-Report»
- Absender: Depotbank, Online-Broker, Vermögensverwalter, Fondsgesellschaft
- Spalten: Titel/ISIN, Anzahl/Nominal, Kurs 31.12., Wert in CHF, Erträge (Dividenden, Coupons)

## Wofür (Positionen)

- Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis) `einkommen.wertschriften`
- Erträge aus qualifizierten Beteiligungen (Teilbesteuerung) `einkommen.beteiligungen_qualifiziert`
- Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto) `vermoegen.wertschriften_guthaben`
- Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1 `verrechnungssteuer.rueckerstattung`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 4.1, 16.1, 30.1, Form. 2 Spalten A/B |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 4.1, 16.1, 30.1, Form. 2 Spalten A/B |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 4.1, 4.2, 16.1, 30.1, Form. 2 Spalte A/B |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 4.1, 4.2, 16.1, 30.1, Form. 2 (Wertschriftenverzeichnis) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 4, 30.1, Form. 2 Spalten 7–9, Form. 2 Vermögensverwaltungskosten (Code 148) |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 4, 30.1, Form. 2 Spalten 1–9 (Seite 2/3) |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 4.1, 16.3, 30.1, Form. 340 Kolonne A |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 4.1, 16.3, 30.1, Form. 340 (Kolonnen A/B, Codes) |

## Was extrahieren

- Steuerwert je Titel per 31.12. (Schlusskurs des letzten Börsenhandelstages im Dezember, Kursliste ESTV)
- Bruttoerträge des Jahres je Titel (Dividenden, Zinsen) mit Verrechnungssteuer (A) bzw. ohne (B)
- Käufe/Verkäufe/Rückzahlungen im Jahr mit Datum (Zu-/Abgang)
- Unkotierte Titel / Beteiligungen ab 10 % (Code Q) separat kennzeichnen

## Hinweise

- Für den Steuerwert gilt der Kurs der amtlichen ESTV-Steuerkursliste 31.12.; nicht kotierte Titel zum Verkehrswert (Steuerwert Sitzkanton) – nicht zum Anschaffungswert.
- Bei Erwerb oder Veräusserung nichtkotierter Wertpapiere Kauf-/Verkaufsverträge beilegen; Mitarbeiteraktien/-optionen: Bescheinigung des Arbeitgebers beilegen (-> mitarbeiterbeteiligung).
- Auch im Jahr verkaufte oder zurückbezahlte Titel: Erträge bis zum Abgang sind steuerbar; Kapitalgewinne auf Privatvermögen sind in der Regel steuerfrei (nicht deklarieren), ausser gewerbsmässiger Handel.
- Verrechnungssteuer wird nur zurückerstattet, wenn Titel und Ertrag vollständig deklariert sind.

## Kantonale Besonderheiten

- **AR:** Bei Kauf/Verkauf kotierter und nichtkotierter Wertpapiere sind Kaufs- bzw. Verkaufsbelege unaufgefordert beizulegen; Darlehen ab Fr. 50'000 mit Vertragskopie (WL AR 2025 Formular 2 Beilagen).
- **SG:** Bei Veränderung des Bestandes Datum des Zu-/Abgangs und Bankbelege beilegen; nur bei nichtkotierten Titeln Kauf-/Verkaufsverträge (WL SG 2025).
- **TG:** Kurse gemäss ESTV-Kursliste; nicht kotierte Wertpapiere zum Verkehrswert per 31.12., ersatzweise Wert per 1.1. (WL TG 2025 S. 31).
- **ZH:** Steuerwert: Schlusskurs des letzten Börsenhandelstags im Dezember; Q-Kennzeichnung für Beteiligungen >= 10 % (WL ZH 2025).

## Quellen

- [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0156.md) `zh-wl-2025__c0156` – «Für den Steuerwert per Ende des Kalenderjahres ist der Schlusskurs des letzten Börsenhan-»
- [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0130.md) `ar-wl-2025__c0130` – «Bei Erwerb oder Veräusserung von kotierten und nichtkotierten Wertpapieren»
- [WL SG 2025 S. 35–36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0121.md) `sg-wl-2025__c0121` – «Bei Veränderung des Bestandes»
- [WL TG 2025 S. 30–31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0144.md) `tg-wl-2025__c0144` – «Für nicht kotierte Wertpapiere gilt der Verkehrswert per 31. Dezember 2025.»
- [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0155.md) `zh-wl-2025__c0155` – «Beteiligungen von mindestens 10 Prozent am Aktien-, Grund- oder Stammkapital»
