---
typ: beleg
titel: Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten)
jur: multi
beleg: rentenbescheinigung-ahv-iv
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten)

> Relevanz: **ja** (Relevant) · ID `rentenbescheinigung-ahv-iv` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Absender: kantonale/eidgenössische Ausgleichskasse (SVA, AHV-Zweigstelle, SAK, Pensionsversicherung des Bundes)
- Titel «Rentenbescheinigung» bzw. «Bescheinigung der Renten» für das Steuerjahr
- Begriffe: AHV-Altersrente, IV-Rente, Hinterlassenenrente, Kinder-/Zusatzrente, Hilflosenentschädigung
- Alternativ: Postabschnitte/Rentenverfügung (nur Monatsbetrag, nicht Jahresbescheinigung)

## Wofür (Positionen)

- AHV-/IV-Renten `einkommen.sozialversicherung.ahv_iv`
- Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe) `info.steuerfreie_leistungen`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 3.1 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 3.1 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 3.1 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 3.1 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 3.1, 25.3 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 3.1 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 3.1 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 3.1 |

## Was extrahieren

- Jahresbruttobetrag der AHV-/IV-Renten (inkl. Kinder- und Zusatzrenten), getrennt je Person
- Rentenart (AHV oder IV) und Dauer, falls nicht ganzes Jahr
- Hilflosenentschädigung und Ergänzungsleistungen separat ausweisen (nicht steuerbar, nur Angabe)

## Hinweise

- AHV-/IV-Renten sind zu 100 % steuerbar (Bund und Kantone); Ergänzungsleistungen zur AHV/IV, Sozialhilfe und Genugtuungszahlungen sind steuerfrei und nicht zu deklarieren (-> ergaenzungsleistungen).
- Bei Ehepaaren je Person eine Bescheinigung; Rentenbezüge nur zum Teil des Jahres (Eintritt Rentenalter) – Bruttobetrag des Kalenderjahres massgebend, nicht der Monatsbetrag mal 12.
- Gleiches Formular 11 (Rentenbescheinigung) kann auch von Pensionskassen verwendet werden -> rentenbescheinigung-vorsorge.

## Kantonale Besonderheiten

- **TG:** AHV-/IV-Rentenausweise bzw. Postabschnitte gelten als Unterlage; steuerfrei sind u.a. Ergänzungsleistungen (WL TG 2025 Ziff. 3).
- **ZH:** AHV- und IV-Renten zu 100 % steuerbar (Ziff. 3.1); Rentenbescheinigungen sind zu den Unterlagen bereitzuhalten (WL ZH 2025 Ziff. 3.1, Checkliste).

> Bemerkung: korrigiert durch Prüfung: ZH-Hinweis «AHV getrennt von IV» war nicht belegt, ersetzt durch belegte Aussage.

## Quellen

- [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0049.md) `ar-wl-2025__c0049` – «Die ordentlichen und ausserordentlichen AHV- und IV-Renten sind in vollem Um-»
- [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0076.md) `tg-wl-2025__c0076` – «Ergänzungsleistungen der AHV und IV;»
- [DBG Art. 22](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-22-t1.md) `bund-dbg-2025__art-22-t1` – «Steuerbar sind alle Einkünfte aus der Alters-, Hinterlassenen- und Invalidenversicherung»
- [WL TG 2025 S. 8](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0026.md) `tg-wl-2025__c0026` – «AHV- und PK-Rentenausweise oder Postabschnitte über Renten;»
- [WL ZH 2025 S. 32](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0208.md) `zh-wl-2025__c0208` – «Rentenbescheinigungen»
