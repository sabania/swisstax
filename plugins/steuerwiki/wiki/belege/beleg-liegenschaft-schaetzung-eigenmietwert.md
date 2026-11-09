---
typ: beleg
titel: Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung)
jur: multi
beleg: liegenschaft-schaetzung-eigenmietwert
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung)

> Relevanz: **ja** (Relevant) · ID `liegenschaft-schaetzung-eigenmietwert` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Absender: kantonale Steuerverwaltung, Gemeindesteueramt, Schätzungskommission; Titel «Schätzungsprotokoll», «Verfügung Steuerwert / Eigenmietwert», «Liegenschaftssteuerrechnung»
- Typische Begriffe: Verkehrswert, Steuerwert, Ertragswert (Landwirtschaft), Eigenmietwert/Mietwert, Schätzungsjahr, Grundstücknummer, Katasterwert
- Eröffnung mit Einsprachehinweis; ZH: Mitteilung Neubewertung, Fragebogen hedonische Methode
- Bei ausserkantonalen/ausländischen Liegenschaften: Steuerwertmitteilung des Belegenheitskantons bzw. Verkehrswertschätzung

## Wofür (Positionen)

- Eigenmietwert selbstbewohnter Liegenschaft `einkommen.liegenschaften.eigenmietwert`
- Liegenschaften (Steuerwert) `vermoegen.liegenschaften`
- Einschlag/Abzug auf dem Eigenmietwert (kantonal) `sozialabzug.eigenmietwert`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 5, 31, Form. 7 Abschn. A, Form. 7 Abschn. B a, Form. 7Z |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 5, 31, Form. 7 Abschn. A, Form. 7 Abschn. B a, Form. 7Z |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 5, 31, Form. 7 Abschnitt A, Form. 7 Abschnitt B.a |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 5, 31, Form. 7 (Liegenschaften) |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 8.1, 31, Form. 7 Steuerwert / Mietwert |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 8.1, 31, Form. 7 Steuerwert, Form. 7 Mietwert selbstgenutzt, Form. 7 Selbstnutzungsabzug |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 6, 31.1, Form. 350 Seite 1, Form. 350 Seite 2 Spalte Eigenmietwert, Form. 350 / WL Eigenmietwert |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 6, 6 (Härtefall/Unternutzung), 31.1, 31.2, Form. 350 |

## Was extrahieren

- Steuerwert (Vermögen) per 31.12. des Steuerjahres, Schätzungsjahr
- Eigenmietwert/Mietwert (Einkommen) laut rechtskräftiger Schätzung
- Datum der Eröffnung / Rechtskraft; Einsprachefrist
- Bei Neu-/Umbauten: Baukosten und Fertigstellungsdatum für den Zuschlag zum Steuerwert

## Hinweise

- Massgebend ist grundsätzlich der am Ende der Steuerperiode rechtskräftig eröffnete Wert; die Schätzung nicht selbst berechnen, ausser Neu-/Anbauten ohne neue Schätzung (kantonale Zuschläge).
- Der Eigenmietwert ist Einkommen (Art. 21 Abs. 1 lit. b DBG); Steuerwert ist Vermögen (Kanton, nicht Bund). Eigenmietwert bei dauernd selbstbewohntem Eigenheim: Kantone unterschiedlich (AR Abzug 20 %, SG Herabsetzung um 30 %, TG Abzug 40 %, ZH Weisung ohne pauschalen Einschlag; Bund kein prozentualer Abzug).
- Aussen-/Auslandsliegenschaften: Steuerwert des Belegenheitskantons, Veranlagungsbehörde nimmt Repartitionswert vor (TG).
- Reform Eigenmietwert: Der Bundesrat hat am 1.4.2026 beschlossen, die Abschaffung der Eigenmietwertbesteuerung auf den 1.1.2029 in Kraft zu setzen – für die Steuerjahre 2025/2026 gilt der Eigenmietwert unverändert. ZH hat ab 2026 eine neue Bewertungsweisung (Neubewertung 2026) – Einzelheiten und Übergangsregelung in data/werte prüfen (nicht in diesem Beleg bestätigt).

## Kantonale Besonderheiten

- **ZH:** Weisung 2009 (bis Steuerjahr 2025): schematische Ermittlung; liegt der Wert über 70 % oder unter 60 % der Marktmiete, ist eine individuelle Schätzung vorzunehmen (Weisung 2009 ZH Ziff. 83).
- **SG:** Der massgebliche Steuerwert wird vom Gemeindesteueramt eröffnet; bei Neu-/Anbauten ohne Schätzung Zuschlag von 80 % der Neu-/Anbaukosten zum Verkehrswert (WL SG 2025 Formular 7 A). Eigenmietwert des dauernd selbstbewohnten Eigenheims: Herabsetzung um 30 % (Art. 34 Abs. 3 StG SG).
- **AR:** Eigenmietwert = Mietwert der letzten amtlichen Schätzung abzüglich 20 %; bei Zweit-/Ferienwohnungen und Landwirtschaft entfällt der Abzug; wertvermehrende Investitionen 2.8 % Zuschlag (WL AR 2025 Formular 7 B).
- **TG:** Massgebend ist der am Ende der Steuerperiode rechtskräftig eröffnete Mietwert (StP 23 Nr. 1 Ziff. 3.3); Steuerwert = rechtskräftiger amtlicher Verkehrswert (WL TG 2025 Formular 7). Eigenmietwert des selbstgenutzten Wohneigentums: Abzug 40 % (§ 23 Abs. 3 StG TG).

## Quellen

- [DBG Art. 21](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-21.md) `bund-dbg-2025__art-21` – «der Mietwert von Liegenschaften oder Liegenschaftsteilen, die dem Steuerpflichtigen aufgrund von Eigentum»
- [Weisung 2009 ZH S. 16](../../chunks/zh/2025/zh-weisung-liegenschaften-2009/zh-weisung-liegenschaften-2009__c0033.md) `zh-weisung-liegenschaften-2009__c0033` – «der über 70% der Marktmiete oder unter 60% derselben liegt»
- [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0155.md) `sg-wl-2025__c0155` – «Der massgebliche Steuerwert wird vom Gemeindesteueramt eröffnet.»
- [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0166.md) `ar-wl-2025__c0166` – «Mietwert abzüglich 20 Prozent»
- [StP 23 Nr. 1](../../chunks/tg/dauernd/tg-stp-23-1/tg-stp-23-1__c0004.md) `tg-stp-23-1__c0004` – «Massgebend für die Bewertung ist in der Regel der am Ende der zu bemessenden Steuerperiode rechtskräftige»
- [StG SG Art. 34](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-34.md) `sg-stg-2025__art-34` – «um 30 Prozent herabgesetzt»
- [StG TG § 23](../../chunks/tg/2025/tg-stg/tg-stg__par-23.md) `tg-stg__par-23` – «ein Abzug von 40 Prozent vorgenommen»
- [MM Eigenmietwert](../../chunks/bund/dauernd/bund-mm-eigenmietwert-abschaffung/bund-mm-eigenmietwert-abschaffung__c0002.md) `bund-mm-eigenmietwert-abschaffung__c0002` – «die Reform der Wohneigentumsbesteuerung auf den 1. Januar 2029 in Kraft zu setzen»
