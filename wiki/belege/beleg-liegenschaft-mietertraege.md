---
typ: beleg
titel: Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung)
jur: multi
beleg: liegenschaft-mietertraege
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung)

> Relevanz: **bedingt** (Bedingt relevant) · ID `liegenschaft-mietertraege` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Nur bei vermieteten oder verpachteten Liegenschaften, Zimmern, Garagen oder Parkplätzen sowie bei Untervermietung; bei reiner Selbstnutzung irrelevant (dort nur Eigenmietwert, siehe liegenschaft-schaetzung-eigenmietwert).

## Erkennen an

- Mietvertrag(e) und Mietzinsabrechnung der Verwaltung (Liegenschaftsverwaltung, Immobilientreuhand) für das Steuerjahr
- Typische Begriffe: Nettomietzins, Bruttomietzins, Akontozahlungen Nebenkosten, Heiz- und Warmwasserkosten, Hauswart, Leerstand, Mietzinsausfall
- Jahresabrechnung der Verwaltung (Einnahmen-/Ausgabenrechnung, Nebenkostenabrechnung)
- Einnahmen aus Garagen, Abstellplätzen, Gewerberäumen, Reklame, Photovoltaik-Einspeisevergütung

## Wofür (Positionen)

- Mietertrag/übrige Liegenschaftserträge `einkommen.liegenschaften.mietertrag`
- Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten `abzug.liegenschaft.unterhalt`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 5, Form. 7 Abschn. B b |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 5, Form. 7 Abschn. B b |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 5, Form. 7 Abschnitt B.b |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 5, Form. 7 (Liegenschaften) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 8.1, Form. 7 Mieterträge |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 8.1, Form. 7 Miet-/Pachtzinsen |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 6, Form. 350 Seite 2 Spalte Eigenmietwert |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 6, Form. 350 |

## Was extrahieren

- Bruttomietertrag des Steuerjahres (sämtliche Miet-/Pachtzinsen inkl. Garagen, Gewerbe, Reklame)
- Von Mietern bezahlte Nebenkosten (Heizung, Warmwasser, Treppenhausreinigung): nur steuerfrei soweit sie die tatsächlichen Aufwendungen nicht übersteigen
- Mietzinsreduktion für Hauswart/Verwalter als Arbeitsentgelt (hinzurechnen)
- Leerstand/Mietzinsausfall und Vermietungsdauer bei Ferienwohnungen

## Hinweise

- Steuerbar sind sämtliche Miet- und Pachtzinseinnahmen, auch Garagen, Abstellplätze, gewerblich genutzte Räume; Nebenkostenakonti sind nur in Höhe der tatsächlichen Heiz-/Warmwasser-/Treppenhausreinigungskosten steuerfrei.
- Sind Heiz- und Nebenkosten im Mietzins inbegriffen, dürfen die tatsächlichen Auslagen hierfür vorweg vom Bruttomietertrag abgezogen werden; alle übrigen Nebenkostenvergütungen sind zu deklarieren.
- Einspeisevergütungen für Photovoltaikanlagen sind steuerbar (TG WL 2025); bei möblierten Ferienwohnungen gelten reduzierte Ansätze der Bruttoeinnahmen (WL 2a 2025).
- Der Pauschalabzug für Unterhalt/Verwaltung wird als Prozentsatz vom (um Mieter-Nebenkosten bereinigten) Bruttomietertrag berechnet – Mietabrechnung vollständig einholen.

## Kantonale Besonderheiten

- **ZH:** Liegenschaftsverzeichnis (Formular 350): Mieteinnahmen, Eigenmietwert und Unterhaltskosten pro Liegenschaft; Nettoertrag in Ziff. 6 der Steuererklärung (WL ZH 2025).
- **SG:** Formular 7 B.b Mietertrag und Leistungen Dritter.
- **AR:** Formular 7 Teil B: Eigenmietwert (Abzug 20 %), Mietertrag, Photovoltaik; Verbrauchskosten (Strom, Wasser, Heizung) bei Eigengebrauch nicht abziehbar (WL AR 2025).
- **TG:** Zahlungen der Mieter für Heizung, Warmwasser und Reinigung sind nicht steuerbar, soweit sie die tatsächlichen Aufwendungen nicht übersteigen (WL TG 2025 / StP 23 Nr. 1).

## Quellen

- [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0175.md) `zh-wl-2025__c0175` – «Steuerbar sind sämtliche Miet- und Pachtzinseinnahmen»
- [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0223.md) `tg-wl-2025__c0223` – «Zahlungen der mietenden Personen für Heizung, Warmwasser und Reinigung von Treppenhaus»
- [StP 23 Nr. 1](../../chunks/tg/dauernd/tg-stp-23-1/tg-stp-23-1__c0002.md) `tg-stp-23-1__c0002` – «Steuerbar sind sämtliche Miet- und Pachtzinseinnahmen, die der Steuerpflichtige aus Grundeigentum»
- [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0170.md) `ar-wl-2025__c0170` – «Kosten gelten als nicht abzugsfähige Lebenshaltungskosten.»
- [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0224.md) `tg-wl-2025__c0224` – «Einspeisevergütungen für Photovoltaikanlagen sind steuerbar.»
- [WL 2a 2025 S. 5](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0031.md) `bund-wl-2a-2025__c0031` – «Bei möblierten Ferienwohnungen sind in der Regel nur 4/5 der»
