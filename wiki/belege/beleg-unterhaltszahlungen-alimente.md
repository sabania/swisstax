---
typ: beleg
titel: Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge)
jur: multi
beleg: unterhaltszahlungen-alimente
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge)

> Relevanz: **ja** (Relevant) · ID `unterhaltszahlungen-alimente` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Scheidungsurteil/Scheidungskonvention, Trennungsvereinbarung, Eheschutzentscheid, Unterhaltsvertrag mit KESB/Gericht
- Typische Begriffe: Unterhaltsbeitrag, Kinderalimente, Ehegattenunterhalt, Kinderzulagen, Alimentenbevorschussung, Alimentenhilfe
- Zahlungsnachweise (Kontoauszüge, Einzahlungsscheine) der monatlichen Zahlungen
- Bescheinigung der Alimentenbevorschussungsstelle (Gemeinde/Kanton)

## Wofür (Positionen)

- Bezahlte Unterhaltsbeiträge (Alimente) und Renten `abzug.unterhaltsbeitraege`
- Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder `einkommen.unterhaltsbeitraege`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 6.1, 12.1, 12.2 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 6.1, 12.1, 12.2 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 6.1, 12.1, 12.2 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 6.1, 12.1, 12.2 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 5.1, 5.2, 12.1, 12.2, 12.3 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 5.1, 5.2, 12.1, 12.2 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 5.1, 5.2, 13.1, 13.2 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 5.1, 5.2, 13.1, 13.2, 13.3 |

## Was extrahieren

- Tatsächlich im Steuerjahr bezahlte Beträge (Bezahler) bzw. erhaltene Beträge (Empfänger), je Ehegatte und je Kind getrennt
- Name und Adresse der empfangenden/leistenden Person; Datum und Gericht/Behörde der Vereinbarung
- Geburtsdatum des Kindes (Mündigkeit: Abzug/Steuerbarkeit endet im Monat der Volljährigkeit)
- Bei erstmaliger Deklaration: Auszug/Kopie des Urteils bzw. der Vereinbarung

## Hinweise

- Abzug beim Zahlenden und Besteuerung beim Empfänger sind spiegelbildlich: Ehegattenunterhalt und Kinderalimente an Elternteil für Kinder in dessen Sorge/Obhut; Voraussetzung: effektiv bezahlt, familienrechtlich geschuldet (nicht freiwillig, KS 30 Ziff. 14.2.2).
- Alimente für volljährige Kinder sind weder beim Zahler abziehbar noch beim Empfänger steuerbar; ab Volljährigkeit steht dem Zahlenden stattdessen der Kinderabzug/Unterstützungsabzug zu.
- Können Unterhaltsbeiträge abgezogen werden, entfallen für denselben Zahler die Kinderabzüge für diese Kinder (SG/AR Hinweis bei Ziff. 12).
- Alimentenbevorschussungen sind den Alimenten gleichgestellt (steuerbar beim Empfänger, ZH WL Ziff. 5.2).
- Dauernde Lasten/Leibrenten (Ertragsanteil): separater Abzug (Art. 33 Abs. 1 lit. b DBG), bei Leibrenten Beiblatt mit Empfänger und Umfang einreichen.

## Kantonale Besonderheiten

- **ZH:** Abzug Ziff. 13.1 (Ehegatten, voll abziehbar) und 13.2 (minderjährige Kinder bis zum Monat der Volljährigkeit); Einkommen Ziff. 5.1/5.2; mit der Steuererklärung 2025 sind sämtliche Zahlungsnachweise einzureichen (WL ZH 2025 Ziff. 13).
- **SG:** Ziff. 12.1 (Ehegatte) und 12.2 (Kinder, je Kind separat ausweisen); bei erstmaliger Zahlung Auszug aus Scheidungsurteil/Trennungsvereinbarung und Zahlungsnachweis beilegen (WL SG 2025 Ziff. 12).
- **AR:** Ziff. 12.1/12.2 (minderjährige Kinder); bei erstmaliger Zahlung Urteil/Vereinbarung und Zahlungsnachweis beilegen (WL AR 2025 Ziff. 12).
- **TG:** Abzug nur bei eingereichten Zahlungsnachweisen mit Name und Adresse der empfangenden Person; bei erstmaliger Deklaration Kopie der Urteilspassagen/Vereinbarung beilegen; Kinderunterhalt inkl. Kinderzulagen, längstens bis und mit Monat der Mündigkeit (WL TG 2025 Ziff. 12).

## Quellen

- [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «die Unterhaltsbeiträge an den geschiedenen, gerichtlich oder tatsächlich getrennt lebenden Ehegatten»
- [KS 30 S. 32](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0100.md) `bund-ks-30__c0100` – «können diese Unterhaltszahlungen vom leistenden Elternteil vollumfänglich in Abzug»
- [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0076.md) `zh-wl-2025__c0076` – «Nach Erreichen des 18. Altersjahres geleistete Unterhaltsbeiträge können somit nicht mehr»
- [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0057.md) `zh-wl-2025__c0057` – «Den Alimenten gleichgestellt sind Alimentenbevorschussungen.»
- [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0084.md) `sg-wl-2025__c0084` – «Unterhaltsbeiträge, die an ein volljähriges Kind bezahlt werden, können einerseits»
- [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0087.md) `tg-wl-2025__c0087` – «Kopie der entsprechenden Passagen des Scheidungs- oder Trennungsurteils»
- [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0088.md) `tg-wl-2025__c0088` – «träge können längstens bis und mit dem Monat der Mündigkeit des Kindes abgezogen werden.»
