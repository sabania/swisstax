---
typ: beleg
titel: Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien)
jur: multi
beleg: privatrechnungen-alltag
relevanz: nein
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien)

> Relevanz: **nein** (Nicht relevant) · ID `privatrechnungen-alltag` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Begründung:** Lebenshaltungskosten sind nicht abziehbar (Art. 34 lit. a DBG: Aufwendungen für den Unterhalt des Steuerpflichtigen und seiner Familie). Ausnahme nur bei klarem Zusammenhang mit einem eigens geregelten Abzug (z.B. Berufskosten, Krankheitskosten, Kinderbetreuung, Liegenschaftsunterhalt) – dann unter dem jeweiligen Beleg-Typ prüfen.

## Erkennen an

- Absender: Detailhandel, Online-Shops, Telekom-/Internetanbieter, Energieversorger (Wohnung), Restaurants, Reisebüros, Fitness
- Titel «Rechnung», «Quittung», «Kassenbon», «Bestellbestätigung»
- Keine Bezug zu Beruf, Krankheit, Liegenschaft, Vorsorge oder Spende
- Haushaltsabonnemente (Streaming, Zeitungen), Haushaltsführung

## Wofür (Positionen)

- Übrige Abzüge `abzug.uebrige`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 6.3, 23.4, 30.2, 30.6 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 6.3, 23.4, 30.2, 30.6 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 15.4, 17 |

## Was extrahieren

- Nichts extrahieren; nur Rückfragen: Handelt es sich um beruflich veranlasste Auslagen (Spesenreglement/Arbeitgeber) oder Kosten einer abziehbaren Kategorie?

## Hinweise

- Auch durch die berufliche Stellung bedingter Privataufwand (z.B. Kleider, Repräsentation) ist nicht abziehbar (Art. 34 lit. a DBG).
- Nebenkosten der selbstgenutzten Wohnung (Wasser, Strom, Heizung, Abwassergebühren) gelten als Lebenshaltungskosten (AR WL: nicht abzugsfähig); beim Liegenschaftsunterhalt nur bestimmte Positionen.
- Arbeitgeberbezogene Spesenrückerstattungen stehen im Lohnausweis (Ziff. 13) – Privatbelege dafür nicht einreichen.

## Kantonale Besonderheiten

- **AR:** Kosten wie Abwassergebühren und Kehrichtentsorgung gelten als nicht abzugsfähige Lebenshaltungskosten (WL AR 2025, Liegenschaftsunterhalt).

## Quellen

- [DBG Art. 34](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-34.md) `bund-dbg-2025__art-34` – «die Aufwendungen für den Unterhalt des Steuerpflichtigen und seiner Familie»
- [DBG Art. 34](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-34.md) `bund-dbg-2026__art-34` – «die Aufwendungen für den Unterhalt des Steuerpflichtigen und seiner Familie»
- [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0170.md) `ar-wl-2025__c0170` – «Diese Kosten gelten als nicht abzugsfähige Lebenshaltungskosten.»
