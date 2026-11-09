---
typ: beleg
titel: Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung
jur: multi
beleg: krankenkasse-leistungen
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung

> Relevanz: **bedingt** (Bedingt relevant) · ID `krankenkasse-leistungen` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur wenn Krankheits- oder Unfallkosten geltend gemacht werden, die den Selbstbehalt von 5 % des Nettoeinkommens übersteigen; dient dazu, Leistungen Dritter (Kasse) von den selbst getragenen Kosten abzuziehen.

## Erkennen an

- Absender: Krankenversicherer
- Titel «Leistungsabrechnung», «Kostenzusammenstellung», «Franchise-/Selbstbehaltsübersicht», «Jahresübersicht Leistungen»
- Begriffe: Rechnungsbetrag, Kassenleistung, Franchise, Selbstbehalt (10 %), Spitalbeitrag

## Wofür (Positionen)

- Krankheits- und Unfallkosten (über Selbstbehalt) `abzug.krankheitskosten`
- Behinderungsbedingte Kosten `abzug.behinderungskosten`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 21.1, 21.2, Form. 6 S. 2 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 21.1, 21.2, Form. 6 S. 2 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 21.1, Form. 6 Rückseite Krankheitskosten |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 21.1, Form. 6 (Versicherungen/Krankheitskosten) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 17, 23.1, Form. 5.1 A, Form. 5.1 B |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 17, 23.1, Form. 5.1 A.1–A.9, Form. 5.1 B.1–B.6, Form. 5.1 D |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 22.1, Form. 370 S.1 Teil A Ziff. 1, Form. 370 S.1 Teil B |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 16.4, 22.1, Form. 370 Teil A–E |

## Was extrahieren

- Franchise und Selbstbehalt (Kostenbeteiligung der versicherten Person) laut Jahresabrechnung
- Bruttokosten und Kassenleistungen je Rechnung (damit nur der selbst getragene Teil geltend gemacht wird)
- Leistungsübersicht (inkl. Details je Behandlung), wenn auf einen Kassenauszug verwiesen wird

## Hinweise

- Abzugsfähig sind nur die selbst getragenen Kosten: Beiträge Dritter (Krankenkasse, Unfallversicherer, Hilflosenentschädigung) sind abzuziehen. Abzug nur soweit über 5 % der um die Aufwendungen (Art. 26-33 DBG) verminderten steuerbaren Einkünfte (Bund) bzw. des Nettoeinkommens (Kantone).
- Franchise und Selbstbehalt gemäss detaillierter Kostenzusammenstellung der Krankenkasse sind abziehbar (Ziffer 1 der Kantonsformulare).
- Prämien sind keine Krankheitskosten (-> krankenkasse-praemien); Prämienverbilligung nicht hier berücksichtigen.
- Behinderungsbedingte Kosten unterliegen keinem Selbstbehalt (Art. 33 Abs. 1 lit. hbis DBG).

## Kantonale Besonderheiten

- **ZH:** Formular 370 «Aufstellung über Krankheits- und Unfallkosten» ist einzureichen; Kassen geben auf Verlangen jährlich Kosten- und Prämienzusammenstellungen ab (WL ZH 2025 Ziff. 22.1).
- **SG:** Belege auf Verlangen einzureichen; wird auf einen Kassenauszug verwiesen, ist zwingend die Aufstellung mit allen Details (inkl. Leistungsübersicht) mit der Deklaration einzureichen (Formular 6 SG 2025).
- **AR:** Belege auf Verlangen einzureichen (Formular 6 AR 2025).
- **TG:** Belege sind geordnet beizulegen (Formular 5.1 TG 2025).

## Quellen

- [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t3.md) `bund-dbg-2025__art-33-t3` – «soweit der Steuerpflichtige die Kosten selber trägt und diese 5 Prozent der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen»
- [Formular 6 SG 2025 S. 2](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0003.md) `sg-form-6-2025__c0003` – «Abzugsfähig sind die tatsächlich selbst getragenen Kosten.»
- [WL ZH 2025 S. 19](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0118.md) `zh-wl-2025__c0118` – «Viele Krankenkassen geben auf Verlangen jährlich Kosten- und»
- [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «1. Selbstbehalt gemäss Abrechnung Krankenkasse und Versicherung»
- [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0001.md) `tg-form-05-1-2025__c0001` – «Die Belege sind geordnet beizulegen»
