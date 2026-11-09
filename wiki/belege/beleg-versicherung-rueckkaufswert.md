---
typ: beleg
titel: Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.)
jur: multi
beleg: versicherung-rueckkaufswert
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.)

> Relevanz: **bedingt** (Bedingt relevant) · ID `versicherung-rueckkaufswert` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur bei rückkaufsfähigen Lebens-/Rentenversicherungen (Steuerwert = Rückkaufswert); reine Risikoversicherungen und Säule-3a-Policen sind nicht als Vermögen zu deklarieren.

## Erkennen an

- Absender: Lebensversicherungsgesellschaft
- Titel «Bescheinigung für die Steuererklärung», «Steuerwert per 31.12.», «Rückkaufswert»
- Begriffe: Rückkaufswert, Überschussanteil/Gewinnbeteiligung, Prämien des Jahres, Ertragsanteil

## Wofür (Positionen)

- Lebens-/Rentenversicherungen (Rückkaufswert) `vermoegen.lebensversicherungen`
- Versicherungsprämien und Zinsen von Sparkapitalien `abzug.versicherungspraemien`
- Übrige Renten (Leibrenten, ausländische Renten, Militär-/Unfallversicherung) `einkommen.vorsorge.uebrige_renten`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 14, 30.3, Form. 6 Teil A |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 14, 30.3, Form. 6 Teil A |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 14, 30.3, Form. 6 Teil A |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 14, 30.3 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 14, 30.3, Form. 5.2 A.1–A.4 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 14, 30.3, Form. 5.2 A.1–A.6 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 15, 30.3, Form. 365 Teil A Ziff. 1–4 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 15, Form. 365 Teil A (Ziff. 1–6), 30.3 |

## Was extrahieren

- Steuerwert = Rückkaufswert inkl. Überschussguthaben per 31.12. (nur für rückkaufsfähige Policen)
- Im Jahr bezahlte Prämien (für den Versicherungsabzug, soweit abziehbar)
- Bei laufenden Rentenversicherungen: Rückkaufswert und steuerbarer Ertragsanteil der Rente

## Hinweise

- Rückkaufsfähige Lebens- und Rentenversicherungen unterliegen der Vermögenssteuer; reine Risikoversicherungen haben keinen Rückkaufswert und sind nicht steuerbar.
- Policen der gebundenen Selbstvorsorge (Säule 3a) sind bis zur Fälligkeit steuerfrei und nicht als Vermögen zu deklarieren.
- Die Bescheinigung des Versicherers über den Steuerwert ist der Steuererklärung beizulegen; Bund erhebt keine Vermögenssteuer – nur kantonaler Vermögenswert.
- Prämien rückkaufsfähiger Policen fallen unter den begrenzten Versicherungsabzug (Art. 33 Abs. 1 lit. g DBG), nicht als eigenständiger Abzug.

## Kantonale Besonderheiten

- **AR:** Steuerwert = Rückkaufswert + Überschussguthaben; Bescheinigung der Gesellschaft beilegen; auch laufende Rentenversicherungen mit Rückkaufswert sind steuerbar (WL AR 2025 Ziff. 30.3).
- **SG:** Rückkaufswert inkl. Überschussanteil; Bescheinigung beilegen; reine Risikoversicherungen nicht steuerpflichtig (WL SG 2025 Ziff. 30.3).
- **ZH:** Vermögenssteuerwert gemäss von der Gesellschaft bescheinigtem Wert; nicht rückkaufsfähige laufende Renten sind nicht steuerbar (WL ZH 2025 Ziff. 30.3).
- **TG:** Bescheinigungen der Steuerwerte der Lebensversicherungen per 31.12.2025 gehören zu den benötigten Unterlagen; Versicherer ist nach § 158 StG TG bescheinigungspflichtig (WL TG 2025).

> Bemerkung: Relevanz auf bedingt korrigiert durch Prüfung (nur rückkaufsfähige Policen).

## Quellen

- [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0139.md) `zh-wl-2025__c0139` – «Rückkaufsfähige Lebens- und Rentenversicherungen unterliegen der Vermögenssteuer.»
- [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0114.md) `ar-wl-2025__c0114` – «Als steuerbares Vermögen gilt der Steuer»
- [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0110.md) `sg-wl-2025__c0110` – «Reine Risikoversicherun»
- [WL TG 2025 S. 8](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0027.md) `tg-wl-2025__c0027` – «Bescheinigungen der Steuerwerte Ihrer Lebensversicherungen per 31.12.2025.»
- [StG TG § 158](../../chunks/tg/2025/tg-stg/tg-stg__par-158.md) `tg-stg__par-158` – «Versicherer über den Rückkaufswert von Versicherungen»
