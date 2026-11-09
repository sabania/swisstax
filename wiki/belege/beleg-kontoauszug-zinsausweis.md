---
typ: beleg
titel: Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post)
jur: multi
beleg: kontoauszug-zinsausweis
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post)

> Relevanz: **ja** (Relevant) · ID `kontoauszug-zinsausweis` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Titel «Zins- und Kapitalausweis», «Saldomeldung», «Jahresabschluss/Kontoauszug per 31.12.»
- Absender: Bank, Kantonalbank, Raiffeisen, PostFinance, Versicherer (Sparkonti), Mieterkautionskonto
- Begriffe: Saldo 31.12., Bruttozins, Verrechnungssteuer 35 %, Nettozins

## Wofür (Positionen)

- Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis) `einkommen.wertschriften`
- Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto) `vermoegen.wertschriften_guthaben`
- Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1 `verrechnungssteuer.rueckerstattung`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 4.1, 30.1, Form. 2 Spalten A/B |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 4.1, 30.1, Form. 2 Spalten A/B |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 4.1, 11, 14, 30.1, Form. 2 Spalte A/B, Form. 6 Teil A |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 4.1, 11, 14, 30.1, Form. 2 (Wertschriftenverzeichnis) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 4, 14, 30.1, Form. 5.2 A.1–A.4, Form. 2 Spalten 7–9 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 4, 11, 14, 30.1, Form. 5.2 A.1–A.6, Form. 4.1 A, Form. 2 Spalten 1–9 (Seite 2/3) |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 4.1, 15, 30.1, Form. 365 Teil A Ziff. 1–4, Form. 340 Kolonne A, Form. 340 Kolonne B |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 4.1, 15, Form. 365 Teil A (Ziff. 1–6), 30.1, Form. 340 (Kolonnen A/B, Codes) |

## Was extrahieren

- Saldo per 31.12. (Vermögen; bei ausländischer Währung in CHF umrechnen)
- Bruttozins des Jahres und abgezogene Verrechnungssteuer (falls vorhanden)
- Kontonummer/IBAN und Kontoart, Eröffnungs- bzw. Saldierungsdatum innerhalb des Jahres

## Hinweise

- Auch Konti ohne oder mit geringen Zinsen (z.B. Lohnkonto) und im Jahr saldierte Konti sind zu deklarieren; Bruchzinsen bei Saldierung sind steuerbar. Selbst errechnete Zinsen dürfen nicht eingetragen werden.
- Bruttozinsen von Kundenguthaben bei inländischen Banken bis und mit Fr. 200 pro Jahr sind verrechnungssteuerfrei (Kolonne B); über Fr. 200 mit Verrechnungssteuer (Kolonne A).
- Fehlt der Bank-Steuerauszug: Kontoauszug 31.12. genügt als Nachweis; Konti bei mehreren Banken immer vollständig erfassen (Vermögensverheimlichung vermeiden).
- Zinsen von Mieterkautionskonti sind vom Mieter anzugeben.

## Kantonale Besonderheiten

- **AR:** Bei Konti mit Bruttozins unter Fr. 200, aber Verrechnungssteuerabzug, ist der Nachweis beizulegen (WL AR 2025 Deklaration der Erträge a).
- **SG:** Bankbeleg mit Verrechnungssteuernachweis beilegen, wenn Abzug erfolgte (WL SG 2025 Deklaration der Erträge a).
- **TG:** Zins- und Kapitalbescheinigungen müssen Bruttozinsen, abgezogene Verrechnungssteuer und Kontostand zeigen (WL TG 2025 Benötigte Unterlagen).
- **ZH:** Kolonne A (Kundenguthaben mit Bruttozins über CHF 200) / Kolonne B (bis CHF 200); Abrechnungsbelege bei Festgeld beilegen (WL ZH 2025 Kolonnen A/B).

## Quellen

- [WL AR 2025 S. 23–24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0136.md) `ar-wl-2025__c0136` – «sind bis und mit Fr. 200.– je Kalenderjahr verrechnungssteuerfrei»
- [WL SG 2025 S. 37](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0130.md) `sg-wl-2025__c0130` – «Selbst errechnete Zinsen dürfen nicht ein»
- [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0162.md) `zh-wl-2025__c0162` – «Dies gilt auch für Kundenguthaben mit einem Bruttozins von mehr als»
- [WL TG 2025 S. 8](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0026.md) `tg-wl-2025__c0026` – «aus denen die Bruttozinsen, die»
- [WL AR 2025 S. 23–24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0137.md) `ar-wl-2025__c0137` – «Bruchzinsen (Zinsen bei Aufgabe, Rückzahlung, Einlösung oder Konversion»
