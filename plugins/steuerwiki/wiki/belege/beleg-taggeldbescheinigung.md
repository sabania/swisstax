---
typ: beleg
titel: Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft)
jur: multi
beleg: taggeldbescheinigung
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft)

> Relevanz: **ja** (Relevant) · ID `taggeldbescheinigung` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Absender: Arbeitslosenkasse (RAV/ALK), Krankentaggeldversicherer, Unfallversicherer (Suva u.a.), IV-Stelle, Ausgleichskasse (EO/Mutterschaft)
- Titel «Bescheinigung über Taggelder/Leistungen», «Taggeldabrechnung», «Jahresbescheinigung»
- Begriffe: Taggeld, Erwerbsersatz, Mutterschaftsentschädigung, Anzahl Taggelder, Bruttoleistung

## Wofür (Positionen)

- Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft) `einkommen.ersatz.taggelder`
- Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind `einkommen.ersatz.familienzulagen`
- Krankheits- und Unfallkosten (über Selbstbehalt) `abzug.krankheitskosten`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 3.3, 3.4, 3.5 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 3.3, 3.4, 3.5 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 3.3, 3.4 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 3.3, 3.4 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 3.3 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 3.3 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 3.3, 3.4 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 3.3, 3.4 |

## Was extrahieren

- Bruttobetrag der im Steuerjahr ausbezahlten Taggelder/Entschädigungen je Versicherer
- Zeitraum bzw. Anzahl Taggeldtage
- Prüfen, ob der Betrag bereits im Lohnausweis des Arbeitgebers enthalten ist (Ziff. 7 oder Bemerkung Ziff. 15)

## Hinweise

- Nur direkt von der Versicherung/Kasse ausbezahlte Taggelder separat deklarieren; vom Arbeitgeber ausbezahlte stehen im Lohnausweis (Doppeldeklaration vermeiden).
- IV-Taggelder sind Ersatz für Erwerbseinkommen und steuerbar; Taggelder KV/UV/IV sind vollumfänglich zu deklarieren. Zusammenhängende, selbst getragene Krankheitskosten sind separat als Abzug geltend zu machen (-> arzt-zahnarzt-rechnungen).
- Bei Arbeitslosigkeit Bescheinigung der Arbeitslosenkasse beilegen; Erwerbslücken in der Steuererklärung ausdrücklich bezeichnen.

## Kantonale Besonderheiten

- **ZH:** Ziff. 3.3 (ALV, direkt ausbezahlte EO) und Ziff. 3.4 (KV/UV/IV/MV-Taggelder, Familienzulagen, Mutterschaft): Bescheinigungen sind beizulegen (WL ZH 2025 Ziff. 3.3/3.4).
- **SG:** Ziff. 3.3 (IV/KV/UV) und 3.4 (ALV): Bescheinigung der Arbeitslosenkasse beilegen, soweit nicht im Lohnausweis (WL SG 2025 Ziff. 3.3-3.4).
- **AR:** Gleiche Gliederung wie SG: Ziff. 3.3 / 3.4 (WL AR 2025 Ziff. 3.3-3.5).
- **TG:** Taggelder aus Kranken-, Unfall- und Invalidenversicherung werden als Erwerbsausfallentschädigungen unter Ziff. 3.3 deklariert (WL TG 2025 Ziff. 3.3).

## Quellen

- [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0054.md) `zh-wl-2025__c0054` – «Die entsprechenden Bescheinigungen sind beizulegen.»
- [WL SG 2025 S. 19](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0060.md) `sg-wl-2025__c0060` – «Über nicht im Lohnausweis aufgeführte Bezüge ist eine»
- [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0053.md) `ar-wl-2025__c0053` – «IV-Taggelder gehören zum steuerbaren Einkommen»
- [WL Lohnausweis 2026 S. 19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0052.md) `bund-wl-lohnausweis-2026__c0052` – «Anzahl der Tage mit Erwerbsausfallentschädigungen»
