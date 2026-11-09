---
typ: beleg
titel: Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung)
jur: multi
beleg: bescheinigung-saeule3a
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung)

> Relevanz: **ja** (Relevant) · ID `bescheinigung-saeule3a` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Titel «Bescheinigung über Vorsorgebeiträge», Formular 21 EDP (für Säule 3a: Ziffer 2 Beiträge, Ziffer 3 Einkäufe; dasselbe Formular dient der 2. Säule)
- Absender: Bankstiftung (z.B. Vorsorgekonto 3a) oder Versicherungsgesellschaft (3a-Police)
- Felder: Feld q «Total Beiträge an die Säule 3a», Datum der Einzahlungen, Ziffer 2 (Beiträge), Ziffer 3 (Einkäufe)

## Wofür (Positionen)

- Beiträge Säule 3a (inkl. Einkäufe ab 2026) `abzug.vorsorge.saeule3a`
- Einkauf (Nachzahlung) Säule 3a – ab Steuerjahr 2026 `abzug.vorsorge.saeule3a_einkauf`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 13.1 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 13.1 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 3.2, 13.1 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 3.2, 13.1, 13.1 (Einkauf) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 3.2, 13.1, 13.2 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 13.1 / 13.2, 13.1 / 13.2 (Einkauf) |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 14.1 / 14.2, 14.3 (ab 2026) |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 14.1 / 14.2, 14.3 |

## Was extrahieren

- Total der im Steuerjahr tatsächlich einbezahlten Beiträge (Feld q) je Vorsorgenehmer und je Vorsorgeträger
- Einzahlungsdatum (massgebend ist das Jahr der effektiven Zahlung, nicht das Jahr der Gutschrift im Folgejahr)
- Einkäufe in die Säule 3a (Ziffer 3, Feld x) separat vom ordentlichen Beitrag, mit Steuerperiode (Feld t)

## Hinweise

- Bescheinigt wird das Total der Beiträge – nicht nur der steuerlich abziehbare Teil; die Begrenzung (Max.-Beträge mit/ohne 2. Säule) wendet der Bearbeiter an. Werte siehe Werte-Dateien (saeule3a.max_*).
- Abzug nur für tatsächlich im Steuerjahr bezahlte Beiträge und nur bei AHV-pflichtiger Erwerbstätigkeit; bei Ehepaaren je Person mit eigenem Vertrag; Bescheinigung muss auf die erwerbstätige Person lauten.
- Einkäufe in die Säule 3a (BVV 3 Art. 7a/7b): im Einkaufsjahr zusätzlich zum vollen ordentlichen Beitrag und nur separat bescheinigt (Ziffer 3); Abzug für Einkäufe erst ab Steuerperiode 2026 – Details in den Werte-Dateien (saeule3a.einkauf).
- Selbständigerwerbende: 3a-Beiträge sind Privatentnahmen, nie als Geschäftsaufwand in der Erfolgsrechnung zu verbuchen.

## Kantonale Besonderheiten

- **SG:** Bescheinigung der Versicherung oder Bankstiftung (Form. 21 EDP) ist in jedem Fall beizulegen (WL SG 2025 Ziff. 13.1).
- **AR:** Bescheinigung (Form. 21 EDP) in jedem Fall beilegen (WL AR 2025 Ziff. 13.1).
- **ZH:** Bescheinigungen der Versicherung/Bankstiftung beilegen (WL ZH 2025 Ziff. 14).
- **TG:** Bescheinigung über Beiträge/Einkäufe 2. Säule und 3a ist Pflichtunterlage; Abzug setzt AHV/IV-pflichtige Erwerbstätigkeit voraus (WL TG 2025 Ziff. 13).

> Bemerkung: korrigiert durch Prüfung: Formulartitel präzisiert (Formular 21 heisst «Bescheinigung über Vorsorgebeiträge»). Einkauf 3a: Abzug erst ab Steuerperiode 2026 (vgl. data/werte/bund/2026.yaml saeule3a.einkauf).

## Quellen

- [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0081.md) `zh-wl-2025__c0081` – «Der Steuererklärung sind die Bescheinigungen der Versicherung oder»
- [MB 21 EDP S. 4–5](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0013.md) `bund-mb-21edp__c0013` – «Total der Beiträge für anerkannte Formen der gebundenen Selbstvorsorge (Säule 3a)»
- [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0085.md) `sg-wl-2025__c0085` – «Es dürfen nur die im Jahre»
- [MB 21 EDP S. 5](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0016.md) `bund-mb-21edp__c0016` – «Im Jahr, in dem der Einkauf erfolgt (Einkaufsjahr) kann maximal der kleine Säule 3a-Ab»
