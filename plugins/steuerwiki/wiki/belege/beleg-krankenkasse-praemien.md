---
typ: beleg
titel: Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung)
jur: multi
beleg: krankenkasse-praemien
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung)

> Relevanz: **ja** (Relevant) · ID `krankenkasse-praemien` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Absender: Krankenversicherer (KVG-Grundversicherung und VVG-Zusatzversicherungen)
- Titel «Jahresbescheinigung für die Steuererklärung», «Prämienübersicht», «Prämienrechnung»
- Begriffe: Grundversicherung, Zusatzversicherung, Prämienverbilligung (IPV), Franchise, Selbstbehalt

## Wofür (Positionen)

- Versicherungsprämien und Zinsen von Sparkapitalien `abzug.versicherungspraemien`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 14, Form. 6 Teil A |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 14, Form. 6 Teil A |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 14, Form. 6 Teil A |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 14, Form. 6 (Versicherungen/Krankheitskosten) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 14, Form. 5.2 A.1–A.4 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 14, Form. 5.2 A.1–A.6 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 15, Form. 365 Teil A Ziff. 1–4, Form. 365 Teil A Ziff. 6 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 15, Form. 365 Teil A (Ziff. 1–6), Form. 370 Teil A–E |

## Was extrahieren

- Im Steuerjahr tatsächlich bezahlte Prämien (Grund- und Zusatzversicherung), je versicherte Person
- Erhaltene individuelle Prämienverbilligung (IPV) – Prämien netto oder Verbilligung separat ausweisen
- Unfallprämien (falls nicht obligatorisch über Arbeitgeber/NBUV)

## Hinweise

- Prämien sind nur im Rahmen des begrenzten Versicherungsabzugs (Pauschal-Höchstbetrag) abziehbar; der Abzug wird um erhaltene Prämienverbilligung gekürzt: Nur die selbst getragenen Prämien zählen.
- Prämien für Mobiliar-, Motorfahrzeug- und Haftpflichtversicherungen sowie für Sachversicherungen sind nicht abziehbar (-> hausrat-haftpflicht-police).
- Wird die Prämienverbilligung direkt mit der Prämienrechnung verrechnet (Regelfall), ist die um die IPV reduzierte Prämie einzutragen; nicht doppelt kürzen.
- Arbeitgeberprämien für obligatorische Unfall-/Krankentaggeldversicherung sind im Nettolohn bereits berücksichtigt.

## Kantonale Besonderheiten

- **TG:** Ziffer 1 des Formulars 5.2: Nettoprämie (nach IPV) eintragen, inkl. über Ergänzungsleistungen ausgerichteter Prämienverbilligung und Nachzahlungen früherer Jahre; Jahresbestätigung der Krankenkasse beilegen (WL TG 2025 S. 44).
- **ZH:** Erhaltene Prämienverbilligung wird in Ziff. 15 (Zeile 6) abgezogen, soweit nicht schon bei den Prämien berücksichtigt (WL ZH 2025 Ziff. 15).
- **SG:** Versicherungsabzug in Formular 6 ermitteln; individuelle Prämienverbilligungen anrechnen (WL SG 2025 Ziff. 14).
- **AR:** Versicherungsabzug in Formular 6 ermitteln; Prämien für Mobiliar-, Motorfahrzeug- und Haftpflichtversicherungen sind ausgeschlossen (WL AR 2025 Ziff. 14).

## Quellen

- [KS 30 S. 12](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0031.md) `bund-ks-30__c0031` – «nur die tat»
- [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t2.md) `bund-dbg-2025__art-33-t2` – «die Einlagen, Prämien und Beiträge für die Lebens-, die Kranken- und die nicht unter Buchstabe f fallende Unfallversicherung»
- [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0210.md) `tg-wl-2025__c0210` – «Tragen Sie in Ziffer 1 die selber bezahlten Einlagen, Prämien und Beiträge für die private Kran-»
- [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0085.md) `ar-wl-2025__c0085` – «Vom Abzug ausgeschlossen sind die Prämien für Mobiliar-, Motorfahrzeug- und»
- [WL SG 2025 S. 27](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0087.md) `sg-wl-2025__c0087` – «Dabei sind die individuellen Prämienverbilligungen, die für»
