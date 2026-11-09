---
typ: beleg
titel: Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters)
jur: multi
beleg: mietvertrag-wohnung
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters)

> Relevanz: **bedingt** (Bedingt relevant) · ID `mietvertrag-wohnung` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Der Mietzins der selbstbewohnten Wohnung ist Lebenshaltungsaufwand und nicht abziehbar (Art. 34 lit. a DBG). Relevant nur bei: (a) Untervermietung (Nettoertrag steuerbar), (b) Wochenaufenthalt am Arbeitsort (Mehrkosten Unterkunft abziehbar), (c) Mietzinsreduktion als Entgelt (z.B. Hauswart-Tätigkeit = Einkommen).

## Erkennen an

- Titel «Mietvertrag», «Mietzinsanpassung», «Nebenkostenabrechnung», «Mietzinsbestätigung»
- Absender: Vermieter/Liegenschaftsverwaltung (bei Mieter) oder Mieter (bei Untervermietung)
- Begriffe: Nettomietzins, Nebenkosten (akonto), Mietbeginn, Kündigungstermin, Mietkaution
- Mietkautionskonto (Sperrkonto) – separat für Vermögen relevant

## Wofür (Positionen)

- Mehrkosten Wochenaufenthalt `abzug.berufskosten.wochenaufenthalt`
- Mietertrag/übrige Liegenschaftserträge `einkommen.liegenschaften.mietertrag`
- Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …) `einkommen.uebrige`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | Form. 4 Ziff. 4 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | Form. 4 Ziff. 4 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | Form. 4 Ziff. 4.1 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | Form. 4 Ziff. 4.1 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | Form. 4.2/4.3 Ziff. 5.1 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | Form. 360 Ziff. 4 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | Form. 360 Ziff. 4 |

## Was extrahieren

- Jahresmietzins netto (ohne akonto-Nebenkosten) und Zimmerzahl – für Wochenaufenthalt-Unterkunftsberechnung: Jahresmietzins : (Zimmer + 1)
- Bei Untervermietung: erhaltene Untermiete abzüglich anteilig Mietzins und Nebenkosten für vermietete Räume (Nettoertrag)
- Bei Hauswart/Verwalter: Differenz zwischen normalem und reduziertem Mietzins als Einkommen
- Mietkaution (Sperrkonto) – nur als Guthaben im Vermögen, falls verzinst

## Hinweise

- Wochenaufenthalt: Mehrkosten der Unterkunft nur wenn regelmässige Rückkehr am Wochenende; bei kleinerer Wohnung (bis 3½ Zimmer) Anteil des Zimmers nach Formel (Beispiel TG: Fr. 10'800 : 4,5 = Fr. 2'400).
- Mietzinsen für Büro/Praxis von Selbständigen gehören in die Jahresrechnung (Geschäftsaufwand).
- Für Eigentümer entfällt der Beleg; massgebend sind Eigenmietwert und Unterhalt (siehe liegenschaft-*).

## Kantonale Besonderheiten

- **TG:** Untervermietung netto steuerbar nach Abzug des anteiligen Mietzinses und der Nebenkosten (Ziff. 5.4). Wochenaufenthalt: Mietzins : (Anzahl Zimmer + 1) bei Wohnungen bis 3½ Zimmer.
- **AR:** Mietzinsreduktion als Entgelt (z.B. Hauswart): Differenz als Einkommen deklarieren; Mehrkosten bei auswärtigem Wochenaufenthalt Ziff. 10.4 (Formular 4 Ziff. 4) (WL AR 2025).
- **SG:** Mietzinsreduktion (Hauswart) als Einkommen; Mehrkosten Wochenaufenthalt Ziff. 10.4 (Formular 4 Ziff. 4).

## Quellen

- [DBG Art. 34](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-34.md) `bund-dbg-2025__art-34` – «die Aufwendungen für den Unterhalt des Steuerpflichtigen und seiner Familie»
- [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0189.md) `tg-wl-2025__c0189` – «Jahresmietzins : (Anzahl Zimmer + 1) = Kosten des Zimmers»
- [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0083.md) `tg-wl-2025__c0083` – «nach Abzug der darauf entfallenden Kosten»
- [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0036.md) `ar-wl-2025__c0036` – «ist die Differenz zwischen normalem und reduziertem Mietzins als Einkommen»
- [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0043.md) `sg-wl-2025__c0043` – «ist die Differenz»
