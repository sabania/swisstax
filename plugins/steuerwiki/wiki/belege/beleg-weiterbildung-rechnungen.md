---
typ: beleg
titel: Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren)
jur: multi
beleg: weiterbildung-rechnungen
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren)

> Relevanz: **bedingt** (Bedingt relevant) · ID `weiterbildung-rechnungen` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur berufsorientierte Aus- und Weiterbildung (inkl. Umschulung) nach erstem Abschluss auf Sekundarstufe II oder nach vollendetem 20. Lebensjahr; Hobby-/Liebhaberei-Kurse, Erstausbildung bis Sek. II und vom Arbeitgeber übernommene Kosten sind nicht abziehbar.

## Erkennen an

- Absender: Bildungsinstitution (Hochschule, Fachhochschule, höhere Fachschule, Berufsverband, Kursanbieter, Prüfungsstelle)
- Typische Begriffe: Kursgebühr, Semestergebühr, Lehrgang/Diplom, Prüfungsgebühr, Studienmaterial, Anmeldebestätigung
- Rechnungs- und Zahlungsdatum; Kursbeginn/-ende; Teilnehmername
- Arbeitgeberbeteiligung (Kostenübernahme) oder Lohnausweis Ziff. 13.3 (Weiterbildung)

## Wofür (Positionen)

- Berufsorientierte Aus- und Weiterbildungskosten `abzug.weiterbildung`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 16.4 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 16.4 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 16.4, 23.3, Lohnausweis Ziff. 13.3 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 16.4, 23.3, Lohnausweis Ziff. 13.3, Form. 10 (Kinderbetreuung/Ausbildung) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 16.1, 16.2 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 16.1 / 16.2 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 16.2, Form. 367, Lohnausweis Ziff. 13.3 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 16.2, Form. 367 |

## Was extrahieren

- Selbst getragene Kosten (Kurs-/Prüfungsgebühren, notwendiges Lehrmaterial) mit Rechnungs- bzw. Zahlungsdatum
- Kostenbeteiligungen Dritter (Arbeitgeber, Bund, Verband) – abzuziehen
- Berufsbezug (Zweck des Kurses), Kursbeginn/-ende, Abschluss (Diplom, Zertifikat)
- Informatikmittel (Hard-/Software): nur wenn zwingend für den Lehrgang, privater Anteil in der Regel 50 %

## Hinweise

- Für die Periodenzuordnung ist die Fälligkeit bzw. Zahlung massgebend, nicht der Kursbesuch (ZH WL 2025 Ziff. 16.2).
- Maximalbetrag pro Person und Jahr (nicht pro Kurs); beide Ehegatten haben je einen eigenen Höchstbetrag. Weitere damit zusammenhängende Kosten (Fahrten zum Kursort) laufen unter dem gleichen Höchstbetrag.
- Bund 2025: CHF 13'000 pro Person (WL ZH 2025 / WL TG 2025); die ältere KS 42 nennt CHF 12'000 (Grundbetrag, wird indexiert) – Betrag des Steuerjahres aus data/werte verwenden.
- Kinderausbildungskosten sind kein Weiterbildungsabzug; Selbstkosten Dritter (Eltern für Kinder) laufen unter Kinder-/Ausbildungsabzug des Kantons (SG: Formular 10 Ziff. 23.3).

## Kantonale Besonderheiten

- **ZH:** Staatssteuer max. CHF 12'400, Bundessteuer max. CHF 13'000; Hilfsblatt «Berufsorientierte Aus- und Weiterbildungskosten» ist der Steuererklärung beizulegen (WL ZH 2025 Ziff. 16.2).
- **SG:** Max. Fr. 13'000 pro Kalenderjahr und Person; Aufstellung mit Rechnungsdatum, Bezeichnung und Betrag erforderlich; ohne Nachweis pauschal Fr. 400 nur bei den Kantons-/Gemeindesteuern für hauptberuflich unselbständig Erwerbende, nicht beim Bund (WL SG 2025 Ziff. 16.4).
- **AR:** Max. Fr. 12'000 (kantonal); keine Pauschale; Informatikmittel nur, wenn zwingend (50 % Privatanteil) (WL AR 2025 Ziff. 16.4).
- **TG:** Max. Fr. 13'000 pro Person und Jahr für Staats- und Gemeindesteuer wie Bundessteuer; Aufstellung mit Belegen der Steuererklärung beilegen (WL TG 2025 Ziff. 16).

## Quellen

- [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0093.md) `zh-wl-2025__c0093` – «betrag von CHF 12’400 bei der Staatssteuer bzw. CHF 13’000 bei der Bundessteuer, sofern ein»
- [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0093.md) `zh-wl-2025__c0093` – «bildungskosten ist die Fälligkeit bzw. die Zahlung und nicht der Kursbesuch»
- [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0094.md) `sg-wl-2025__c0094` – «Um selbst bezahlte, berufsorientierte Aus-, Weiterbildungs- und»
- [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0093.md) `ar-wl-2025__c0093` – «Fr. 12‘000.– abgezogen werden, sofern»
- [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0102.md) `tg-wl-2025__c0102` – «auf jährlich maximal Fr. 13'000 pro Person beschränkt»
- [KS 42 S. 2](../../chunks/bund/dauernd/bund-ks-42/bund-ks-42__c0001.md) `bund-ks-42__c0001` – «Nicht abzugsfähig sind Kosten für Aus- und Weiterbildungen, die nicht berufsorientiert sind»
- [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0095.md) `sg-wl-2025__c0095` – «Nachweis pauschal Fr. 400»
