---
typ: beleg
titel: Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare)
jur: multi
beleg: lohnausweis
relevanz: ja
generiert: tools/build_quick.py aus data/belege-teil*.yaml (2026-11-09)
---

# Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare)

> Relevanz: **ja** (Relevant) · ID `lohnausweis` · Status: ☑️ agent-geprueft · [Belege-Übersicht](../../quick/belege-relevanz.md)

## Erkennen an

- Titel «Lohnausweis – Rentenbescheinigung» (Formular 11 SSK/ESTV), auch als eLohnausweis (mit Barcode)
- Absender: Arbeitgeber; Felder A–H, Ziffern 1–15
- Typische Begriffe: Bruttolohn total (Ziff. 8), Nettolohn/Rente (Ziff. 11), Spesenvergütungen (Ziff. 13), Bemerkungen (Ziff. 15)
- Kästchen F (unentgeltliche Beförderung) und G (Kantinenverpflegung/Lunch-Checks)

## Wofür (Positionen)

- Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn) `einkommen.unselbstaendig.haupterwerb`
- Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen) `einkommen.unselbstaendig.nebenerwerb`
- VR-Honorare, Sitzungsgelder, Tantiemen (wo separat ausgewiesen, z.B. SG/AR Ziff. 1.3) `einkommen.unselbstaendig.vr_honorare`
- Fahrkosten Wohn-/Arbeitsstätte `abzug.berufskosten.fahrkosten`
- Mehrkosten auswärtige Verpflegung / Schichtarbeit `abzug.berufskosten.verpflegung`
- Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen) `abzug.vorsorge.saeule2_einkauf`

## Ziffern je Kanton und Jahr

| Kanton/Jahr | Ziffern |
|---|---|
| [AR 2025](../../quick/zuordnung-ar-2025.md) | 1.1, 1.2, 1.3, 10.1, 13.2, 16.4, 16.6, Form. 4 Ziff. 1.1, Form. 4 Ziff. 2.1, Form. 4 Ziff. 2.2, Form. 4 Ziff. 2.3, Form. 4 Ziff. 3, Form. 4 Ziff. 5 |
| [AR 2026](../../quick/zuordnung-ar-2026.md) | 1.1, 1.2, 1.3, 10.1, 13.2, 16.4, 16.6, Form. 4 Ziff. 1.1, Form. 4 Ziff. 2.1, Form. 4 Ziff. 2.2, Form. 4 Ziff. 2.3, Form. 4 Ziff. 3, Form. 4 Ziff. 5 |
| [SG 2025](../../quick/zuordnung-sg-2025.md) | 1.1, 1.2, 1.3, Form. 4 Ziff. 2.2, Form. 4 Ziff. 2.3, Form. 4 Ziff. 4.2, Form. 4 Ziff. 5, Lohnausweis Feld F, Lohnausweis Ziff. 10.2, Lohnausweis Ziff. 13.3, Lohnausweis Ziff. 15 |
| [SG 2026](../../quick/zuordnung-sg-2026.md) | 1.1, 1.2, 1.3, Form. 4 Ziff. 2.2, Form. 4 Ziff. 2.3, Form. 4 Ziff. 4.2, Form. 4 Ziff. 5, Lohnausweis Feld F, Lohnausweis Feld G, Lohnausweis Ziff. 10.2, Lohnausweis Ziff. 13.3, Lohnausweis Ziff. 15 |
| [TG 2025](../../quick/zuordnung-tg-2025.md) | 1.1, 1.2, 3.3, 10.1, 10.2, 15.2, 16.1, 16.2, Seite 4 Bemerkungen/Unterschrift, Form. 4.2 Ziff. 1.2, Form. 4.2 Ziff. 3.1, Form. 4.2 Ziff. 3.2, Form. 4.2 Ziff. 4, Form. 4.2 Ziff. 5.2, Form. 4.2 Ziff. 6, Form. 5.2 A.5–A.6 |
| [TG 2026](../../quick/zuordnung-tg-2026.md) | 1.1, 1.2, 1.2 (Feuerwehr), Form. 4.2 Ziff. 1.1, Form. 4.2 Ziff. 1.2, Form. 4.2/4.3 Ziff. 3.1, Form. 4.2/4.3 Ziff. 3.2, Form. 4.2/4.3 Ziff. 4, Form. 4.2/4.3 Ziff. 5.2, Form. 4.2/4.3 Ziff. 6, Form. 5.2 A.1–A.6 |
| [ZH 2025](../../quick/zuordnung-zh-2025.md) | 1.1, 1.2, Form. 360 Ziff. 2.1 (verbilligt), Form. 360 Ziff. 2.1 (voll), Form. 360 Ziff. 2.2, Form. 360 Ziff. 3, Form. 360 Ziff. 5, Form. 367, Lohnausweis Feld F, Lohnausweis Feld G, Lohnausweis Ziff. 10.2, Lohnausweis Ziff. 13.3, Lohnausweis Ziff. 15 |
| [ZH 2026](../../quick/zuordnung-zh-2026.md) | 1.1, 1.2, 11.1 / 11.2, Form. 360 Ziff. 1.1, Form. 360 Ziff. 1 (Zwischentotal), Form. 360 Ziff. 2.1 (verbilligt), Form. 360 Ziff. 2.1 (voll), Form. 360 Ziff. 2.2, Form. 360 Ziff. 3, 16.1, 16.2, Form. 367 |

## Was extrahieren

- Ziff. 11 Nettolohn (= Bruttolohn Ziff. 8 minus Abzüge Ziff. 9 und 10) – Übertrag in die Steuererklärung
- Ziff. 6 Verwaltungsratsentschädigungen und Ziff. 5 Beteiligungsrechte (separat ausgewiesen, siehe Beiblatt)
- Ziff. 10.2 Einkaufsbeiträge 2. Säule (nur wenn vom Lohn abgezogen)
- Ziff. 12 Quellensteuerabzug (nur Information bei Quellensteuerpflicht)
- Ziff. 13 Spesen: Kreuz im Feld vor 13.1.1 = Vorgaben für Einzelfallpauschalen eingehalten (kein Betrag nötig); sonst effektive Spesen 13.1.1/13.1.2 betragsmässig (z.B. «Spesen für externen Arbeitsplatz»); Pauschalspesen 13.2 immer mit Betrag; Weiterbildung 13.3. Bei genehmigtem Spesenreglement kein Kreuz, sondern Vermerk in Ziff. 15
- Kästchen F (Arbeitsweg gratis → Fahrkostenabzug fällt weg), Kästchen G (Kantine/Lunch-Checks → reduzierte Verpflegungspauschale), Feld Ziff. 15 Bemerkungen

## Hinweise

- Pro Arbeitgeber ein Lohnausweis, auch bei Nebenbeschäftigungen; bei mehreren Lohnausweisen für dasselbe Jahr steht in Ziff. 15 «Einer von … Lohnausweisen», ein ersetzter Lohnausweis trägt den Vermerk «Dieser Lohnausweis ersetzt den Lohnausweis vom …».
- Erwerbslücken (Arbeitslosigkeit, Krankheit, Mutterschaft) müssen in der Steuererklärung bezeichnet und mit Bescheinigung belegt werden, sonst Rückfragen.
- Einkäufe, die der Arbeitnehmer selber bezahlt hat (nicht vom Lohn abgezogen), stehen nicht im Lohnausweis, sondern auf der Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) -> siehe bescheinigung-pk-einkauf.
- Taggelder/EO, die der Arbeitgeber ausbezahlt hat, stehen im Lohnausweis (Ziff. 7 bzw. Ziff. 1 mit Bemerkung Ziff. 15); nur direkt von der Versicherung ausbezahlte Beträge sind separat zu deklarieren.
- Die hinterlegte ESTV-Wegleitung zum Lohnausweis ist die Fassung 2026 (Formular 11); für 2025 ist die Fassung mit gleichem Aufbau massgebend – Ziffernbezeichnungen gelten gemäss der jeweiligen Wegleitung des Steuerjahres.

## Kantonale Besonderheiten

- **TG:** In der Steuererklärung ist der in Ziffer 11 des Lohnausweises aufgeführte Nettolohn einzusetzen; Trinkgelder sind auch ohne Ausweis im Lohnausweis steuerbar (WL TG 2025 Ziff. 1.1).
- **AR:** Nettolohn gemäss Lohnausweis in Ziff. 1.1; nicht im Lohnausweis abgerechnete NBUV-/2.-Säule-Beiträge werden unter Ziff. 16.6 abgezogen (WL AR 2025 Ziff. 1.1).
- **ZH:** Lohnausweise sind der Steuererklärung beizulegen; auch Nebenerwerb (Ziff. 1.2) wird mit Lohnausweis deklariert (WL ZH 2025 Ziff. 1.1, Formularbild S. 10).

> Bemerkung: korrigiert durch Prüfung: Kreuz bei 13.1.1 gehört zu den Einzelfallpauschalen (Rz 52), nicht zum genehmigten Spesenreglement (dort Vermerk Ziff. 15, Rz 60/65); ZH-Nebenerwerb nicht über Hilfsblatt. Wegleitung ist Fassung 2026, für 2025 gleicher Aufbau angenommen.

## Quellen

- [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «In diesem Feld ist der für die Steuererklärung massgebende Nettolohn anzugeben.»
- [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0032.md) `zh-wl-2025__c0032` – «Bitte vergessen Sie nicht, Ihre Lohnausweise der Steuererklärung beizulegen.»
- [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0049.md) `tg-wl-2025__c0049` – «In die Steuererklärung ist der in Ziffer 11 des Lohnausweises aufgeführte Nettolohn einzusetzen.»
- [StG TG § 156](../../chunks/tg/2025/tg-stg/tg-stg__par-156.md) `tg-stg__par-156` – «Lohnausweise über alle Einkünfte aus unselbständiger Erwerbstätigkeit»
- [WL Lohnausweis 2026 S. 19–20](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0054.md) `bund-wl-lohnausweis-2026__c0054` – «Wurden vom Arbeitgeber für dasselbe Jahr ausnahmsweise»
- [WL Lohnausweis 2026 S. 16](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0042.md) `bund-wl-lohnausweis-2026__c0042` – «genügt es, im vorangestellten kleinen Feld»
- [WL Lohnausweis 2026 S. 19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0053.md) `bund-wl-lohnausweis-2026__c0053` – «In diesem Fall ist in Ziffer 13.1.1 kein Kreuz zu machen»
