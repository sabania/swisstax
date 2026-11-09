---
typ: beleg
titel: Steuerrechnung / Akontorechnung / Schlussrechnung (Staats-, Gemeinde- und Bundessteuer)
jur: multi
beleg: steuerrechnung
relevanz: bedingt
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Steuerrechnung / Akontorechnung / Schlussrechnung (Staats-, Gemeinde- und Bundessteuer)

> Relevanz: **bedingt** (Bedingt relevant) · ID `steuerrechnung` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

**Bedingung:** Die bezahlten Steuern selbst sind NICHT abziehbar (Art. 34 lit. e DBG). Relevant sind nur Vergütungs-/Ausgleichszinsen zu Gunsten (steuerbarer Ertrag), Verzugs-/Ausgleichszinsen zu Lasten (Schuldzinsen) sowie die Rückzahlung/Verrechnung zur Kontrolle der Zahlungen.

## Erkennen an

- Absender: kantonale Steuerverwaltung, Gemeindesteueramt, Kirchgemeinde, ESTV (direkte Bundessteuer)
- Titel «Steuerrechnung», «Provisorische Rechnung», «Schlussrechnung», «Einzahlungsschein Steuern»
- Begriffe: Verfalltag, Ausgleichszins, Ratenzahlung, Vergütungszins, Verzugszins, Staatssteuer, Gemeindesteuer, Bundessteuer
- Referenznummer/ESR, Steuerperiode

## Wofür (Positionen)

- Rechnungen, Raten, Zinsen, Bezug `verfahren.bezug`
- Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis) `einkommen.wertschriften`
- Private Schuldzinsen `abzug.schuldzinsen`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | Seite 1 / 4 |

## Was extrahieren

- Ausgleichs-/Vergütungszinsen zu Gunsten der steuerpflichtigen Person (Betrag 1.1.–31.12.)
- Ausgleichs-/Verzugszinsen zu Lasten (private Schuldzinsen)
- Steuerperiode, Verfalltag und bezahlte Raten (Plausibilisierung gegen Akonto-Konto)

## Hinweise

- Einkommens-, Grundstückgewinn- und Vermögenssteuern von Bund, Kantonen und Gemeinden sowie gleichartige ausländische Steuern sind nicht abziehbar (Art. 34 lit. e DBG).
- Zinsen zu Gunsten aus Steuerabrechnungen (Ausgleichs- und Rückvergütungszinsen) sind steuerbarer Ertrag aus Guthaben; Zinsen zu Lasten sind Schuldzinsen.
- Die provisorische Rechnung wird durch die definitive Veranlagung ersetzt; Akonto-Zahlungen sind keine Abzüge. Bei grossen Abweichungen kann eine angepasste Rechnung beantragt werden (Ausgleichszins beachten).
- Der Steuerrechnung ist keine Angabe für die Steuererklärung zu entnehmen ausser den Zinsen; Grundstücksteuern/Liegenschaftssteuerrechnung (TG) dienen als Quelle für Mietwert-/Steuerwertdaten.

## Kantonale Besonderheiten

- **TG:** Provisorische Rechnung in drei Raten; die Liegenschaftensteuerrechnung (versandt im Januar) enthält den indexierten Mietwert und den Steuerwert (WL TG 2025).
- **AR:** Auf jeder Zahlung wird ein Ausgleichszins gutgeschrieben, auf dem veranlagten Betrag ab Verfalltag (30. Juni bei ganzjähriger Steuerpflicht) belastet.
- **SG:** Ausgleichs- und Rückvergütungszinsen sind in Ziff. 4.1 (Wertschriften und Guthaben) zu deklarieren; Zinsen zu Lasten = Schuldzinsen.

## Quellen

- [DBG Art. 34](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-34.md) `bund-dbg-2025__art-34` – «Einkommens-, Grundstückgewinn- und Vermögenssteuern von Bund, Kantonen und Gemeinden»
- [WL SG 2025 S. 19](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0063.md) `sg-wl-2025__c0063` – «Zinsen zu Ihren Gunsten aus Steuerabrechnungen, wie Ausgleichs- und Rück-»
- [WL AR 2025 S. 34](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0180.md) `ar-wl-2025__c0180` – «Auf jeder Zahlung wird ein»
- [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0224.md) `tg-wl-2025__c0224` – «Liegenschaften- steuerrechnung 2026, welche Sie im Januar 2026 erhalten»
- [WL TG 2025 S. 56](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0271.md) `tg-wl-2025__c0271` – «erfolgt der provisorische Steuerbezug in drei Raten»
