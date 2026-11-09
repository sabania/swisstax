---
typ: beleg
titel: ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg
jur: multi
beleg: oev-abo
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg

> Relevanz: **bedingt** (Bedingt relevant) · ID `oev-abo` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur wenn das Abonnement für den Weg zwischen Wohn- und Arbeitsstätte (ständige Benützung) benötigt wird; Freizeit-/Privatabos zählen nicht. Nicht abziehbar, wenn der Arbeitsweg vom Arbeitgeber unentgeltlich zur Verfügung gestellt wird (Lohnausweis Kästchen F) oder ein Geschäftsfahrzeug zur Verfügung steht.

## Erkennen an

- Absender: SBB, Verkehrsverbund (z.B. ZVV, Ostwind, Tarifverbund), Regionalbahn/-bus; Titel «Rechnung Abonnement», «Streckenabonnement», «Generalabonnement», «Verbundabo»
- Typische Begriffe: Gültigkeit von/bis, Zonen/Strecke, Jahresabo, Monatsabo, Klasse, Preis in CHF
- Quittung oder Kreditkarten-/Kontoauszug mit Abo-Belastung; Bestätigung des Arbeitgebers bei Beteiligung/Gratis-Abo (Lohnausweis Kästchen F)
- Arbeitgeberbestätigung bei Jobticket/Arbeitgeberzuschuss

## Wofür (Positionen)

- Fahrkosten Wohn-/Arbeitsstätte `abzug.berufskosten.fahrkosten`
- Mehrkosten Wochenaufenthalt `abzug.berufskosten.wochenaufenthalt`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 10.1, Form. 4 Ziff. 1.1 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 10.1, Form. 4 Ziff. 1.1 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | Form. 4 Ziff. 1.1 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | Form. 4 Ziff. 1.1 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 10.1, 10.2, Form. 4.2 Ziff. 2.1 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | Form. 4.2/4.3 Ziff. 2.1 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | Form. 360 Ziff. 1.1 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 11.1 / 11.2, Form. 360 Ziff. 1.1, Form. 360 Ziff. 1 (Zwischentotal) |

## Was extrahieren

- Tatsächlich bezahlter Abopreis des Steuerjahres (notwendige Kosten für die Strecke Wohn-/Arbeitsort)
- Strecke/Zonen, Gültigkeitsdauer; Arbeitgeberbeteiligung (abzuziehen)
- Bei Wochenaufenthalt: Fahrkosten Wohnort – Wochenaufenthaltsort
- Lohnausweis Kästchen F: unentgeltliche Beförderung zwischen Wohn- und Arbeitsort

## Hinweise

- Bei ständiger Benützung öffentlicher Verkehrsmittel: nachgewiesene (tatsächliche) Abonnementskosten, begrenzt durch den Maximalbetrag Fahrkosten des Kantons/Bundes (siehe kantone); Bund max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG, 2025; ZH WL 2025).
- Das Abo ist mit dem Mittagsheimfahrt-Abzug zu koordinieren: Hin- und Rückfahrt in der Mittagspause maximal in Höhe der abzugsberechtigten Verpflegungskosten (ZH).
- Bei Velo/Kleinmotorrad (gelbes Kontrollschild) gilt die Pauschale von Fr. 700 pro Jahr statt der effektiven Kosten.
- Mit Geschäftsfahrzeug oder gratis Beförderung durch den Arbeitgeber entfällt der Fahrkostenabzug (ZH WL, Lohnausweis Kästchen F).

## Kantonale Besonderheiten

- **ZH:** Notwendige Abonnementskosten oder effektive Kosten gemäss Aufstellung; Maximum Staatssteuer CHF 5'200, Bundessteuer CHF 3'300 (WL ZH 2025 Ziff. 11).
- **SG:** Tatsächliche Kosten; ab 1.1.2025 maximaler Fahrkostenabzug Fr. 8'000 (StB 39 Nr. 3); Formular 4 Ziff. 1.1.
- **AR:** Tatsächliche Kosten; Pendlerabzug begrenzt die Kosten für den Arbeitsweg bei Staats- und Gemeindesteuern auf max. Fr. 6'000 (alle Verkehrsmittel zusammen) (WL AR 2025 Ziff. 10.1).
- **TG:** Nachgewiesene Abonnementskosten sind für Staats- und Gemeindesteuern wie Bundessteuer abziehbar (StP 29 Nr. 2); Velo/Motorfahrrad/Kleinmotorrad bis Fr. 700.

## Quellen

- [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0062.md) `zh-wl-2025__c0062` – «die notwendigen Abonnementskosten»
- [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «Bei der Staatssteuer ist der Fahrkostenabzug auf CHF 5’200 beschränkt.»
- [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «Bei der direkten Bundessteuer ist der Fahrkostenabzug auf CHF 3’300 beschränkt.»
- [StB 39 Nr. 3 S. 1](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0002.md) `sg-stb-39-3__c0002` – «2025 beträgt der maximale Fahrkostenabzug Fr. 8'000»
- [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0074.md) `ar-wl-2025__c0074` – «zur Arbeit bei den Staats- und Gemeindesteuern auf max. Fr. 6’000.–.»
- [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0002.md) `tg-stp-29-2__c0002` – «die tatsächlich entstandenen (nachgewiesenen) Abonnementskosten abgezogen werden»
