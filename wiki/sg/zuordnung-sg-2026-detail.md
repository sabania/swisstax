---
typ: zuordnung-detail
titel: Zuordnung SG 2026 – Detail
jur: sg
jahre:
- 2026
generiert: tools/build_quick.py aus data/zuordnung/sg/2026.yaml (2026-11-09)
---

# SG 2026: Zuordnung Beleg → Ziffer – Detail

> Kompaktansicht: [quick/zuordnung-sg-2026.md](../../quick/zuordnung-sg-2026.md) · Formular: Steuererklärung 2026 Formular 1 (Hauptformular, Kantons-, Gemeinde- und direkte Bundessteuer; vorliegend Fassung für unterjährige Steuerpflicht «UJ», Formular 1 SG 2026 UJ) + Hilfsblätter Formular 2, 4, 5, 6, 7, 10 (für 2026 nicht publiziert; nur Übertragsziffern aus Formular 1 UJ und 2026-Rechtsgrundlagen). Wegleitung 2026 noch nicht publiziert. · Quelle der Wahrheit: `data/zuordnung/sg/2026.yaml`

> **Hinweis:** Wegleitung und Hilfsblätter SG 2026 noch nicht publiziert (Stand 09.11.2026) – Zuordnung stützt sich auf Formular 1 SG 2026 UJ und die Rechtsgrundlagen 2026.

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Aus Haupterwerbstätigkeit unselbständig (Code 100 Person 1 / 102 Person 2)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn)
- **Rein:** Lohnausweis (je Arbeitgeber) → Ziff. 11 Nettolohn · Lohnausweis Ziff. 10.2 → BVG-Einkauf per Lohnabzug (nur Kontrolle) · Lohnausweis Ziff. 13.3 → Weiterbildungsvergütungen AG (nur Kontrolle) · Lohnausweis Ziff. 4 → Kapitalleistung (Vorsorgecharakter prüfen)
- **Rechnen:** Σ Lohnausweis Ziff. 11 (= Ziff. 8 − Ziff. 9 − Ziff. 10) je Person → Code 100 (P1) / 102 (P2); unterjährig nur während der Steuerpflicht Zugeflossenes
- **Regel:** Nettolohn gemäss Lohnausweis Ziff. 11 einsetzen (Bruttolohn Ziff. 8 abzüglich Abzüge Ziff. 9 und 10). Berufskosten separat in Ziff. 10 (Formular 4). Lohnausweis Ziff. 10.2 (BVG-Einkauf) ist im Nettolohn bereits abgezogen: nicht nochmals in Ziff. 13.2. Lohnausweis Ziff. 13.3 (Arbeitgeber-Weiterbildung) ist nicht steuerbar: nicht zusätzlich in Ziff. 16.4 abziehen. Bei unterjähriger Steuerpflicht nur während der Dauer zugeflossene Einkünfte (MB 8/2026).
- **Beachten:** LA Ziff. 10.2 (BVG-Einkauf) ist im Nettolohn schon abgezogen → nicht nochmals in Ziff. 13.2
- **Beachten:** LA Ziff. 13.3 (AG-Weiterbildung) ist kein geldwerter Vorteil → nicht zusätzlich in Ziff. 16.4 abziehen
- **Beachten:** LA Ziff. 4 Kapitalleistung mit Vorsorgecharakter: gesondert besteuert (Art. 52 StG; Bund: Fünftel-Tarif)
- **Bemerkung:** Wegleitung 2026 nicht publiziert; Details der Wegleitung 2025 (sg-wl-2025) gelten für 2026 nicht bestätigt.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.1 Aus Haupterwerbstätigkeit Person 1 Lohnausweis 100»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «In diesem Feld ist der für die Steuererklärung massgebende Nettolohn anzugeben»
  - [StG SG Art. 30](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-30.md) `sg-stg-2026__art-30` – «Steuerbar sind alle Einkünfte aus privatrechtlichem oder öffentlich-rechtlichem Arbeitsverhältnis»
  - [MB 8/2026 SG S. 2](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0004.md) `sg-mb-8-2026__c0004` – «pflicht effektiv zugeflossenen Einkünfte und die Aufwendungen zu deklarieren»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «In diesem Feld sind die im Bruttolohn enthaltenen, dem Arbeitnehmer vom Lohn»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «13.2 Säule 2 (BVG) inkl. Einkaufsbeiträge Person 1 Bescheinigung 218»
  - [StG SG Art. 30](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-30.md) `sg-stg-2026__art-30` – «stellen unabhängig von deren Höhe keinen anderen geldwerten Vorteil»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «alle effektiven Vergütungen des Arbeitgebers für berufsorientierte Aus-»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.4 Kosten berufsorientierte Aus-/Weiterbildung Person 1 Aufstellung 223»
  - [WL Lohnausweis 2026 S. 12](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0027.md) `bund-wl-lohnausweis-2026__c0027` – «Abgangsentschädigungen mit Vorsorgecharakter»
  - [StG SG Art. 52](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-52.md) `sg-stg-2026__art-52` – «gleichartige Kapitalabfindungen des Arbeitgebers sowie Zahlungen bei Tod»
  - [WL 2a 2026 S. 9](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0068.md) `bund-wl-2a-2026__c0068` – «Die Steuer darauf wird zu einem Fünftel der Tarife 2026 berechnet»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Aus Nebenerwerbstätigkeit unselbständig (Code 104 Person 1 / 106 Person 2)

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn) des Nebenarbeitgebers
- **Rein:** Lohnausweis Nebenarbeitgeber → Ziff. 11 Nettolohn · Arbeitsvertrag Haupterwerb → Pensum (Nachweis Haupterwerb ≥ zwei Drittel) · Lohnausweis Nebenerwerb → vergütete Fahrt-/Verpflegungsspesen (steuerbar)
- **Rechnen:** Σ Lohnausweis Ziff. 11 aller Nebenerwerbe je Person → Code 104/106; Pauschale Formular 4: 20% × Σ Nettoeinkünfte, min. 800, max. 2'400 (Kanton = Bund)
- **Regel:** Nettolohn Ziff. 11 des Lohnausweises aus Nebenerwerb. Berufskosten-Pauschale für Nebenerwerb im Formular 4 (20% der Nettoeinkünfte, mind. Fr. 800, max. Fr. 2'400 gemäss StB 39 Nr. 9). Nebenerwerb setzt einen Haupterwerb (mind. 2/3 eines Normalpensums) voraus.
- **Beachten:** Nur mit Haupterwerb ≥ zwei Drittel Pensum (Teilzeitstellen zusammenzählen); Überstunden beim Haupt-AG ≠ Nebenerwerb
- **Beachten:** Pauschale deckt auch Fahrkosten und Verpflegung; bei Nebeneinkünften < 800 höchstens Pauschale in gleicher Höhe
- **Beachten:** Vom AG vergütete Spesen (Fahrt, Verpflegung) sind Einkommen → Pauschale von Nettolohn plus Spesen
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Unselbständige Nebenerwerbstätigkeit: 20 % der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400 (Pauschalansätze der direkten Bundessteuer). Nachweis höherer notwendiger Kosten vorbehalten.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb: Pauschale mindestens Fr. 800; Nebenerwerbseinkünfte unter Fr. 800 sind nicht betroffen (siehe StB 39 Nr. 9).)** · Bund **CHF 800 (Mindestbetrag Pauschale Nebenerwerb.)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb: Pauschale höchstens Fr. 2'400.)** · Bund **CHF 2'400 (Höchstbetrag Pauschale Nebenerwerb.)**
- **Bemerkung:** Wegleitung 2026 nicht publiziert; Details der Wegleitung 2025 (sg-wl-2025) gelten für 2026 nicht bestätigt.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.2 Aus Nebenerwerbstätigkeit Person 1 Lohnausweis 104»
  - [StB 39 Nr. 9 S. 1](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0002.md) `sg-stb-39-9__c0002` – «sind 20% der Nettoeinkünfte, mindestens Fr. 800.-- und höchstens Fr. 2'400.-- abziehbar»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «In diesem Feld ist der für die Steuererklärung massgebende Nettolohn anzugeben»
  - [StB 39 Nr. 9 S. 2](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0005.md) `sg-stb-39-9__c0005` – «wenigstens zwei Drittel einer 100-prozentigen Arbeitszeit entspricht»
  - [StB 39 Nr. 9 S. 2](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0007.md) `sg-stb-39-9__c0007` – «bis die Mindestquote von zwei Drittel überschritten wird»
  - [StB 39 Nr. 9 S. 2–3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0009.md) `sg-stb-39-9__c0009` – «Überstunden für den Hauptarbeitgeber gelten nicht als Nebenerwerbstätigkeit»
  - [StB 39 Nr. 9 S. 3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0013.md) `sg-stb-39-9__c0013` – «schliesst die Nebenerwerbspauschale auch die Fahrkosten und die Mehrkosten»
  - [StB 39 Nr. 9 S. 3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0012.md) `sg-stb-39-9__c0012` – «höchstens ein Pauschalabzug in gleicher Höhe zulässig»
  - [StB 39 Nr. 9 S. 3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0012.md) `sg-stb-39-9__c0012` – «Die Pauschale von 20% errechnet sich aus der Summe aller Nebenerwerbseinkünfte»
  - [StB 39 Nr. 9 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0014.md) `sg-stb-39-9__c0014` – «von diesen Erwerbseinkünften (Nettolohn plus Spesen)»

<a id="1-3-einkommen-unselbstaendig-vr-honorare"></a>
### Ziff. 1.3 – Sitzungsgelder, VR-Honorare usw. (Code 108 Person 1 / 110 Person 2)

- **Schlüssel:** `einkommen.unselbstaendig.vr_honorare` (VR-Honorare, Sitzungsgelder, Tantiemen (wo separat ausgewiesen, z.B. SG/AR Ziff. 1.3)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Bescheinigung der Gesellschaft/Behörde (bzw. Lohnausweis, falls dort enthalten)
- **Rein:** Bescheinigung Gesellschaft/Behörde → Sitzungsgelder, VR-Honorare, Tantiemen · Sitzungsliste/Bescheinigung → Anzahl Sitzungen mit Sitzungsgeld (Behörden-Berufskosten)
- **Rechnen:** Σ Entschädigungen lt. Bescheinigung je Person, soweit nicht in Ziff. 1.1/1.2 → Code 108/110; Kanton Behördenkosten: bis 2'400 oder 60 je Sitzung (max. 4'000)
- **Regel:** Entschädigungen für Dienstleistungen jeder Art (z.B. VR- und Behördentätigkeit) gemäss Bescheinigung; nur soweit nicht bereits in Ziff. 1.1/1.2 erfasst (Doppelerfassung vermeiden). Berufskosten nebenamtlicher Behördenmitglieder: pauschal bis Fr. 2'400 oder je Sitzung bis Fr. 60 (max. Fr. 4'000), Art. 22 Abs. 2 StV.
- **Beachten:** VR-/Stiftungsrats-Entschädigungen auf Lohnausweis (Ziff. 6) sind im Brutto-/Nettolohn → nicht doppelt erfassen
- **Beachten:** Behördenpauschale (Art. 22 Abs. 2 StV) zusätzlich zum Nebenerwerbsabzug möglich; Nachweis höherer Kosten vorbehalten
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.3 Sitzungsgelder, VR-Honorare usw. Person 1 Bescheinigung 108»
  - [StV SG Art. 22](../../chunks/sg/2025/sg-stv/sg-stv__art-22.md) `sg-stv__art-22` – «pauschal bis Fr. 2400.–, oder»
  - [WL Lohnausweis 2026 S. 13](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0030.md) `bund-wl-lohnausweis-2026__c0030` – «alle Entschädigungen anzugeben, die einer Person in ihrer Eigenschaft»
  - [StB 39 Nr. 9 S. 4](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0015.md) `sg-stb-39-9__c0015` – «kann zusätzlich zum Nebenerwerbsabzug geltend gemacht werden»
  - [WL Lohnausweis 2026 S. 14](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0034.md) `bund-wl-lohnausweis-2026__c0034` – «das Total der Einkünfte gemäss den Ziffern 1 bis 7 des Lohnausweises»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit: Industrie-, Handels-, Gewerbebetriebe, Landwirtschaft, freie Berufe (Code 112 Person 1 / 114 Person 2)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Erfolgsrechnung/Reingewinn der Jahresrechnung (Aufstellung)
- **Rein:** Jahresrechnung (Bilanz + Erfolgsrechnung) → Reingewinn (Code 112 P1 / 114 P2) · ohne kaufm. Buchhaltung: Aufstellung Aktiven/Passiven, Einnahmen/Ausgaben, Privatentnahmen/-einlagen · Schlussbilanz → Aktiven Ziff. 32.2 / Geschäftsschulden Ziff. 34.2 · Verlustvortragsaufstellung → noch nicht verrechnete Verluste der sieben Vorjahre
- **Rechnen:** Reingewinn lt. Erfolgsrechnung (nur geschäftsmässig begründeter Aufwand, Art. 40 StG) − noch nicht verrechnete Verluste der sieben Vorjahre (Art. 42 StG)
- **Regel:** Reingewinn gemäss Jahresrechnung (Bilanz/Erfolgsrechnung beilegen). Steuerbar sind alle Einkünfte aus Handels-, Gewerbe-, Land- und Forstwirtschaftsbetrieb und freien Berufen, inkl. Kapitalgewinne auf Geschäftsvermögen. Betriebsvermögen in Ziff. 32, Geschäftsschulden in Ziff. 34.2.
- **Beachten:** Steuerbar auch Kapitalgewinne/Aufwertungen auf Geschäftsvermögen und Überführung ins Privatvermögen (Art. 31 Abs. 2 StG)
- **Beachten:** Bund: eigene BVG-Beiträge im Geschäft nur als «Arbeitgeberanteil»; Rest und Säule 3a separat als Vorsorgebeiträge
- **Beachten:** Bund: Privatanteil Haushalt 3'540/Jahr (1 Erwachsener) + 900 je weiteren Erwachsenen + 600 je Kind
- **Bemerkung:** Wegleitung 2026 nicht publiziert; Details der Wegleitung 2025 (sg-wl-2025) gelten für 2026 nicht bestätigt.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «2.1 Person 1 112»
  - [StG SG Art. 31](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-31-t1.md) `sg-stg-2026__art-31-t1` – «Steuerbar sind alle Einkünfte aus einem Handels-, Industrie-, Gewerbe-, Land- und Forstwirtschaftsbetrieb»
  - [StG SG Art. 40](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-40-t1.md) `sg-stg-2026__art-40-t1` – «Bei selbständiger Erwerbstätigkeit werden die geschäfts- oder berufsmässig begründeten Kosten abgezogen.»
  - [StG SG Art. 42](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-42.md) `sg-stg-2026__art-42` – «Verluste aus den sieben der Steuerperiode vorangegangenen Geschäftsjahren können abgezogen werden»
  - [WL 2a 2026 S. 2](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0010.md) `bund-wl-2a-2026__c0010` – «Einnahmen und Ausgaben sowie Privatentnahmen und»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «32.2 Aktiven gemäss Schlussbilanz per Aufstellung 316»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «34.2 Geschäftsschulden Formular 5 506»
  - [WL 2a 2026 S. 2](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0012.md) `bund-wl-2a-2026__c0012` – «mitarbeitenden Ehegatten dürfen nur im Ausmass des»
  - [WL 2a 2026 S. 2](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0013.md) `bund-wl-2a-2026__c0013` – «in den Ziffern 15.3 bzw. 13 der Steuererklärung abgezogen»
  - [WL 2a 2026 S. 2](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0009.md) `bund-wl-2a-2026__c0009` – «Haushalt mit 1 Erwachsenen im Jahr 3540.–»
  - [WL 2a 2026 S. 2](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0010.md) `bund-wl-2a-2026__c0010` – «im Jahr 900.– 600.–»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Aus Kollektiv-, Kommandit- und einfachen Gesellschaften (Code 120 Person 1 / 122 Person 2)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Angaben der Gesellschaft (Anteil am Gewinn)
- **Rein:** Abrechnung/Bestätigung der Gesellschaft → Anteil am Gewinn je Teilhaber (Code 120 P1 / 122 P2) · Jahresrechnung der Personengesellschaft → Reingewinn (Grundlage Anteil) · Kapitalkonto lt. Schlussbilanz → Geschäftskapital Ziff. 32.1
- **Rechnen:** Anteil am Einkommen der Kollektiv-/Kommandit-/einfachen Gesellschaft lt. Angaben der Gesellschaft, je Person (P1/P2 getrennt)
- **Regel:** Anteil an den Einkünften der Personengesellschaft gemäss Angaben der Gesellschaft; gehört zu den selbständigen Einkünften (Art. 31 StG). Geschäftskapital in Ziff. 32.1.
- **Beachten:** Gilt als selbständiges Einkommen: inkl. Kapitalgewinne auf Geschäftsvermögen (Art. 31 Abs. 2 StG)
- **Beachten:** Anteil Geschäftskapital am Stichtag in Ziff. 32.1 (Code 314) deklarieren
- **Beachten:** Verluste der sieben Vorjahre abziehbar, soweit noch nicht verrechnet (Art. 42 StG)
- **Bemerkung:** Formular 11 (Gesellschaft) für 2026 nicht im Wiki; Zuordnung Ziff. 2.2 laut Formular 1 UJ 2026.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «2.2 Aus Kollektiv-, Kommandit- und einfachen Gesellschaften»
  - [StG SG Art. 31](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-31-t1.md) `sg-stg-2026__art-31-t1` – «Steuerbar sind alle Einkünfte aus einem Handels-, Industrie-, Gewerbe-, Land- und Forstwirtschaftsbetrieb»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «32.1 Geschäftskapital in Kollektiv-, Kommandit- und einfachen Gesellschaften 314»
  - [StG SG Art. 42](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-42.md) `sg-stg-2026__art-42` – «Verluste aus den sieben der Steuerperiode vorangegangenen Geschäftsjahren können abgezogen werden»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV/IV-Renten zu 100% (Code 126 Person 1 / 128 Person 2)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung Ausgleichskasse (Jahresbetrag brutto)
- **Rein:** Rentenbescheinigung Ausgleichskasse/IV → Jahresbetrag Renten · Auszahlungsbeleg Rente Dezember (Bund-Praxis: beilegen) · EL-Verfügung → nicht hier, sondern Ziff. 8.2
- **Rechnen:** 100% (Kanton = Bund) der im Steuerjahr bezogenen AHV-/IV-Renten je Person → Code 126 (P1) / 128 (P2); unterjährig nur während der Steuerpflicht zugeflossene
- **Regel:** AHV-/IV-Renten sind voll steuerbar (zu 100%). Ergänzungsleistungen sind steuerfrei (nicht hier, sondern Angabe in Ziff. 8.2).
- **Beachten:** Ergänzungsleistungen steuerfrei → nur Angabe in Ziff. 8.2 (Code 291)
- **Beachten:** Kapitalleistungen aus Vorsorge nicht hier → Seite 4 (Ziff. 40)
- **Beachten:** Bund: IV-Kostenbeiträge (Eingliederung, Hilfsmittel, Sonderschulung) steuerfrei
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0004.md) `sg-form-1-2026-uj__c0004` – «3.1 AHV/IV-Renten (zu 100%) Person 1 Bescheinigung 126»
  - [StG SG Art. 35](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-35-t1.md) `sg-stg-2026__art-35-t1` – «Steuerbar sind alle Einkünfte aus der Alters-, Hinterlassenen- und Invalidenversicherung»
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t2.md) `sg-stg-2026__art-37-t2` – «die Einkünfte aufgrund der Bundesgesetzgebung über Ergänzungsleistungen»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «8.2 Ergänzungsleistungen / Überbrückungsleistungen für ältere Arbeitslose 291»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0013.md) `sg-form-1-2026-uj__c0013` – «40. Kapitalleistungen aus Vorsorge»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Kapitalleistungen aus Vorsorge sind auf Seite 4 unten»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0017.md) `bund-wl-2a-2026__c0017` – «Diese sind zu 100 % steuerbar.»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0018.md) `bund-wl-2a-2026__c0018` – «Hilfsmittel sowie für Sonderschulung sind steuerfrei»
  - [MB 8/2026 SG S. 2](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0004.md) `sg-mb-8-2026__c0004` – «pflicht effektiv zugeflossenen Einkünfte und die Aufwendungen zu deklarieren»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0018.md) `bund-wl-2a-2026__c0018` – «einen Auszahlungsbeleg der Rente vom Dezember 2026»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen mit steuerbarem Prozentsatz (Code 130 Person 1 / 132 Person 2)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente), Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Rentenbescheinigung Pensionskasse/Versicherer: Jahresrente brutto; steuerbarer Prozentsatz
- **Rein:** Rentenbescheinigung Pensionskasse/Freizügigkeitseinrichtung → Jahresrente brutto · Steuerbescheinigung Versicherer (Leibrentenversicherung) → steuerbarer Ertragsanteil · Bescheinigung Säule-3a-Rente → Jahresbetrag · Vertrag private Leibrente/Verpfründung → erhaltene Rente
- **Rechnen:** Σ Rente × steuerbarer % (Vorkolonne) → Code 130/132: BVG/3a 100%; Leibrente = Ertragsanteil; Altrenten Kanton steuerfrei 40%/20% / Bund steuerbar 60%/80%
- **Regel:** Renten der 2. Säule und aus gebundener Selbstvorsorge sind steuerbar; Leibrenten (und Leibrentenversicherungen) nur im Umfang ihres Ertragsanteils. Prozentsatz in der Vorkolonne gemäss Bescheinigung, mehrere Renten in separater Aufstellung.
- **Beachten:** Altrenten: fällig vor 1987, oder vor 2002 bei Vorsorgeverhältnis vor 1985 (Kanton) / per 31. Dezember 1986 (Bund)
- **Beachten:** Leibrentenversicherung CH: Ertragsanteil lt. Steuerbescheinigung Versicherer (Bund); Kanton: Überschussleistungen 70%
- **Beachten:** Ausländische/private Leibrenten, Verpfründung: Rente × ESTV-Satz (Bund); mehrere Renten: separate Aufstellung
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0004.md) `sg-form-1-2026-uj__c0004` – «3.2 Renten/Pensionen Bescheinigung / Aufstellung»
  - [StG SG Art. 35](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-35-t1.md) `sg-stg-2026__art-35-t1` – «Leibrentenversicherungen sowie Leibrenten- und Verpfründungsverträge sind im Umfang ihres Ertragsanteils steuerbar»
  - [StG SG Art. 280](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-280.md) `sg-stg-2026__art-280` – «40 Prozent der Einkünfte, wenn die Leistungen»
  - [StG SG Art. 280](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-280.md) `sg-stg-2026__art-280` – «20 Prozent der Einkünfte, wenn die Leistungen»
  - [StG SG Art. 280](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-280.md) `sg-stg-2026__art-280` – «die auf einem vor dem 1. Januar 1985 begründeten Vorsorgeverhältnis beruhen»
  - [DBG Art. 204](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-204.md) `bund-dbg-2026__art-204` – «die vor dem 1. Januar 1987 zu laufen begannen oder fällig wurden»
  - [DBG Art. 204](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-204.md) `bund-dbg-2026__art-204` – «auf einem Vorsorgeverhältnis beruhen, das am 31. Dezember 1986 bereits bestand»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0019.md) `bund-wl-2a-2026__c0019` – «zu 60 %, wenn die Leistungen»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0020.md) `bund-wl-2a-2026__c0020` – «zu 80 %, wenn die Leistungen, auf denen der Anspruch der»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0020.md) `bund-wl-2a-2026__c0020` – «Leistungen aus gebundener Selbstvorsorge werden zu 100 %»
  - [StG SG Art. 35](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-35-t2.md) `sg-stg-2026__art-35-t2` – «entspricht der Ertragsanteil 70 Prozent dieser Leistungen»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0023.md) `bund-wl-2a-2026__c0023` – «Bei inländischen Leibrentenversicherungen finden Sie den»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0016.md) `bund-wl-2a-2026__c0016` – «Erhaltene Leibrente / Verpfründung x Berechnungssatz (in %)»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigung (Taggelder Kranken-, Unfall-, Invalidenversicherung, soweit nicht im Lohnausweis; Code 134 Person 1 / 136 Person 2)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Versicherung / Ausgleichskasse
- **Rein:** Taggeldabrechnung Kranken-/Unfall-/IV-Versicherung → direkt ausbezahlte Taggelder · Bescheinigung Ausgleichskasse → EO/Mutterschaftsentschädigung (nicht via AG) · Lohnausweis Ziff. 1/7 und Ziff. 15 → Kontrolle, ob Taggelder schon im Lohn
- **Rechnen:** Σ Taggelder/EO brutto lt. Bescheinigung, soweit nicht im Lohnausweis (Ziff. 1 bzw. 7), je Person → Code 134 (P1) / 136 (P2)
- **Regel:** Ersatzeinkünfte (Taggelder, EO, Mutterschaftsentschädigung usw.) sind steuerbar, soweit nicht bereits im Lohnausweis (Ziff. 8) enthalten; nur Beträge, die nicht über den Lohnausweis laufen, hier deklarieren.
- **Beachten:** Über den AG ausbezahlte Taggelder/EO stehen im Lohnausweis (Ziff. 1 oder 7) → bereits in Ziff. 1.1
- **Beachten:** LA Ziff. 15 nennt Tage mit Erwerbsausfall, die nicht im Bruttolohn sind → dafür Bescheinigung einholen
- **Beachten:** EO für Militär-/Zivil-/Schutzdienst steuerbar; Militärsold selbst steuerfrei (Art. 37 Bst. g StG)
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0004.md) `sg-form-1-2026-uj__c0004` – «3.3 Erwerbsausfallentschädigung Person 1 Bescheinigung 134»
  - [StG SG Art. 36](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-36.md) `sg-stg-2026__art-36` – «alle andern Einkünfte, die an die Stelle des Einkommens aus Erwerbstätigkeit treten»
  - [WL Lohnausweis 2026 S. 9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0015.md) `bund-wl-lohnausweis-2026__c0015` – «das ordentliche Salär sowie die Taggelder aus Versicherungen, die durch den Ar»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.1 Aus Haupterwerbstätigkeit Person 1 Lohnausweis 100»
  - [WL Lohnausweis 2026 S. 13](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0031.md) `bund-wl-lohnausweis-2026__c0031` – «sofern sie nicht unter Ziffer 1 deklariert sind»
  - [WL Lohnausweis 2026 S. 19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0052.md) `bund-wl-lohnausweis-2026__c0052` – «Anzahl der Tage mit Erwerbsausfallentschädigungen»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0017.md) `bund-wl-2a-2026__c0017` – «Sämtliche Erwerbsausfallentschädigungen wie zum Beispiel für»
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t1.md) `sg-stg-2026__art-37-t1` – «der Sold für Militär- und Zivilschutzdienst»
  - [WL Lohnausweis 2026 S. 14](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0034.md) `bund-wl-lohnausweis-2026__c0034` – «das Total der Einkünfte gemäss den Ziffern 1 bis 7 des Lohnausweises»

<a id="3-4-einkommen-ersatz-taggelder"></a>
### Ziff. 3.4 – Arbeitslosen-Taggelder (Code 138 Person 1 / 140 Person 2)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Arbeitslosenkasse
- **Rein:** Jahresbescheinigung Arbeitslosenkasse (ggf. Formular 11) → ALV-Taggelder brutto · Lohnausweis Arbeitgeber Ziff. 7 → Kurzarbeits-/Schlechtwetterentschädigung (Kontrolle)
- **Rechnen:** Σ ALV-Taggelder brutto lt. Bescheinigung der Arbeitslosenkasse je Person → Code 138 (P1) / 140 (P2)
- **Regel:** Arbeitslosentaggelder brutto gemäss Bescheinigung der Arbeitslosenkasse.
- **Beachten:** Über den AG ausgerichtete ALV-Leistungen (Kurzarbeit, Schlechtwetter) stehen im Lohnausweis Ziff. 7 → in Ziff. 1.1
- **Beachten:** Bund ebenso: ALV-Bezüge nur, soweit nicht im Lohnausweis bescheinigt
- **Beachten:** Überbrückungsleistungen für ältere Arbeitslose sind steuerfrei → nur Ziff. 8.2, nicht hier
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0004.md) `sg-form-1-2026-uj__c0004` – «3.4 Arbeitslosen-Taggelder Person 1 Bescheinigung 138»
  - [StG SG Art. 36](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-36.md) `sg-stg-2026__art-36` – «alle andern Einkünfte, die an die Stelle des Einkommens aus Erwerbstätigkeit treten»
  - [WL Lohnausweis 2026 S. 13](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0031.md) `bund-wl-lohnausweis-2026__c0031` – «Kurzarbeits- und Schlechtwetterentschädigungen sowie Einarbei»
  - [WL Lohnausweis 2026 S. 7](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0006.md) `bund-wl-lohnausweis-2026__c0006` – «Feld anzukreuzen, wenn das Formular für die Bescheinigung von Ersatzeinkommen»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.1 Aus Haupterwerbstätigkeit Person 1 Lohnausweis 100»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0017.md) `bund-wl-2a-2026__c0017` – «Bezüge aus Arbeitslosenversicherung und Versicherungstag»
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t3.md) `sg-stg-2026__art-37-t3` – «Einkünfte aufgrund des Bundesgesetzes über Überbrückungsleistungen für ältere Arbeitslose»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «8.2 Ergänzungsleistungen / Überbrückungsleistungen für ältere Arbeitslose 291»
  - [WL Lohnausweis 2026 S. 14](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0034.md) `bund-wl-lohnausweis-2026__c0034` – «das Total der Einkünfte gemäss den Ziffern 1 bis 7 des Lohnausweises»

<a id="3-5-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.5 – Von Ausgleichskassen direkt ausbezahlte Familienzulagen (Code 142)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung Familienausgleichskasse
- **Rein:** Bescheinigung Familienausgleichskasse → direkt ausbezahlte Kinder-/Familienzulagen · Lohnausweis Ziff. 1 → Kontrolle: über AG bezahlte Zulagen (schon im Nettolohn)
- **Rechnen:** Σ direkt von der Ausgleichskasse ausbezahlte Kinder-/Familienzulagen → Code 142 (nur, was nicht über den Lohnausweis lief)
- **Regel:** Nur Familienzulagen, die direkt von der Ausgleichskasse ausbezahlt wurden (nicht im Lohnausweis enthalten). Im Lohnausweis (Ziff. 1) enthaltene Kinder-/Familienzulagen sind bereits im Nettolohn.
- **Beachten:** Über den AG bezahlte Kinder-/Familienzulagen sind Lohnbestandteil (LA Ziff. 1) → bereits in Ziff. 1.1/1.2
- **Beachten:** Bund ebenso: nur direkt von der Ausgleichskasse ausbezahlte Zulagen
- **Bemerkung:** Regel „nur direkt ausbezahlte“ ergibt sich aus Formulartext; Abgrenzung zum Lohnausweis (Zulagen sind Bestandteil des Lohnes) siehe bund-wl-lohnausweis-2026.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0004.md) `sg-form-1-2026-uj__c0004` – «3.5 Von Ausgleichskassen direkt ausbezahlte Familienzulagen 142»
  - [WL Lohnausweis 2026 S. 9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0015.md) `bund-wl-lohnausweis-2026__c0015` – «sämtliche Zulagen (z. B. Geburts-, Kinder- oder andere Familienzulagen»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0017.md) `bund-wl-2a-2026__c0017` – «direkt ausbezahlten Kinder- und Familienzulagen»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.2 Aus Nebenerwerbstätigkeit Person 1 Lohnausweis 104»
  - [WL Lohnausweis 2026 S. 14](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0034.md) `bund-wl-lohnausweis-2026__c0034` – «das Total der Einkünfte gemäss den Ziffern 1 bis 7 des Lohnausweises»

<a id="4-1-einkommen-wertschriften"></a>
### Ziff. 4.1 – Einkünfte aus Wertschriften und Guthaben gemäss Formular 2 (Code 146), inkl. Lotterie-/Geldspielgewinne

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Formular 2 (Wertschriften- und Guthabenverzeichnis): Total Erträge; Steuerauszug/Bankbescheinigung
- **Rein:** Formular 2 (Wertschriften- und Guthabenverzeichnis) → Total Bruttoerträge · Steuerauszug Bank/Depot → Zinsen, Dividenden, Ausschüttungen kollektiver Kapitalanlagen · Konto-/Zinsausweise → Bruttozinsen (vor VSt) · Gewinnbestätigung Lotterie/Online-Spielbank → Einzelgewinn, Spieleinsätze
- **Rechnen:** Σ Bruttoerträge Formular 2 (inkl. VSt-belastete) + steuerbare Geldspielgewinne → Code 146; Einsatzkosten (5%, max. 5'400; online max. 26'800) in Ziff. 16.1
- **Regel:** Total der Erträge aus Formular 2 übertragen (Zinsen, Dividenden, Erträge aus kollektiven Kapitalanlagen usw.). Beteiligungserträge ab 10% separat in Ziff. 4.2/4.3. Unterjährig: nur zugeflossene Erträge, keine March-/pro-rata-Zinsen (MB 8/2026). Geldspielgewinne: Freibetrag einzelner Grossspiel-/Online-Spielbankengewinne Fr. 1'070'900 (neu 2026 laut MB 8/2026), Einsatzkosten Online-Spiele neu max. Fr. 26'800. Verwaltungskosten Ziff. 16.1.
- **Beachten:** Steuerfrei: Casino; Gross-/Online-Gewinne je bis 1'070'900 (Bund 1'071'000); Kleinspiele; Verkaufsförderung ≤ 1'100
- **Beachten:** Beteiligungen ≥ 10% separat in Ziff. 4.2/4.3; Verwaltungs- und Einsatzkosten (Kanton = Bund) in Ziff. 16.1
- **Beachten:** Unterjährig: nur zugeflossene Erträge, keine March-/pro-rata-Zinsen; Wegzug: VSt nur bei Saldierung der Konti
- **Limiten:**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'070'900 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen (nach Geldspielgesetz) sind bis Fr. 1'070'900 steuerfrei; darüber steuerbar (abzüglich Einsatzkosten Art. 45 Abs. 3).)** · Bund **CHF 1'071'000 (Einzelne Gewinne aus nach BGS zugelassenen Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'071'000; darüber steuerbar (abzüglich Einsatzkosten nach Art. 33 Abs. 4 DBG).)**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'100 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (nicht dem Geldspielgesetz unterstellt): steuerfrei, solange die Grenze von Fr. 1'100 nicht überschritten wird (Freigrenze). Gewinne aus Kleinspielen (Geldspielgesetz) steuerfrei.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (Art. 1 Abs. 2 lit. d und e BGS) steuerfrei, sofern die Grenze von CHF 1'100 nicht überschritten wird. Gewinne aus Kleinspielen (BGS) sind steuerfrei.)**
- **Bemerkung:** Hilfsblatt Formular 2/2026 nicht publiziert. Steuerfreiheit Spielbankengewinne: Art. 37 Bst. n StG.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.1 aus Wertschriften und Guthaben 146»
  - [StG SG Art. 33](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-33-t1.md) `sg-stg-2026__art-33-t1` – «Steuerbar sind die Erträge aus beweglichem Vermögen»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0009.md) `sg-mb-8-2026__c0009` – «soweit > Fr. 1’070’900»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0011.md) `sg-mb-8-2026__c0011` – «Einsatzkosten Online-»
  - [MB 8/2026 SG S. 2–3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0005.md) `sg-mb-8-2026__c0005` – «March- oder pro rata temporis Zinsen sind nicht zu»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.1 Verwaltungskosten für Wertschriften und sonstige Kapitalanlagen 220»
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t2.md) `sg-stg-2026__art-37-t2` – «die Gewinne, die in Spielbanken mit Spielbankenspielen erzielt werden»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t5.md) `sg-stg-2026__art-45-t5` – «werden 5 Prozent, jedoch höchstens Fr. 5400.–, als Einsatzkosten abgezogen»
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t3.md) `sg-stg-2026__art-37-t3` – «die Gewinne aus Kleinspielen, die nach dem eidgenössischen Geldspielgesetz»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0025.md) `bund-wl-2a-2026__c0025` – «höchstens bis maximal 26 800 Fr. in Abzug gebracht werden.»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0026.md) `bund-wl-2a-2026__c0026` – «Einsätze können bis zu 5 %, jedoch maximal 5 400 Fr.»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0020.md) `bund-wl-2a-2026__c0020` – «verrechnungssteuerbelastete Einkommen sind immer in der»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0025.md) `bund-wl-2a-2026__c0025` – «Spielbankengewinne in Casinos sind steuerfrei»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0011.md) `sg-mb-8-2026__c0011` – «Einsatzkosten von den steuerbaren Gewinnen»

<a id="4-2-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.2 – Erträge aus Beteiligungen an Gesellschaften ab 10 Prozent, Privatvermögen (Code 147)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2: Erträge aus qualifizierten Beteiligungen (Privatvermögen)
- **Rein:** Formular 2 / Steuerauszug → Dividenden aus Beteiligungen ≥ 10% (Privatvermögen) · Aktienbuch/Statuten/Handelsregister → Beteiligungsquote am Grund-/Stammkapital · Dividenden-/Ausschüttungsabrechnung der Gesellschaft → Bruttoertrag inkl. geldwerte Vorteile
- **Rechnen:** Σ Bruttoerträge (Dividenden, Gewinnanteile, Liquidationsüberschüsse, geldwerte Vorteile) aus Beteiligungen ≥ 10% → Code 147; Teilbesteuerung via Ziff. 4.4
- **Regel:** Dividenden aus Beteiligungen von mindestens 10% des Kapitals im Privatvermögen. Teilbesteuerung über den Abzug in Ziff. 4.4 (30% der Einkünfte, d.h. 70% steuerbar).
- **Beachten:** Steuerbar 70% (Art. 33 Abs. 1bis StG / Bund Art. 20 Abs. 1bis DBG) → 30% Abzug in Ziff. 4.4
- **Beachten:** Massgebend: ≥ 10% des Grund- oder Stammkapitals einer Kapitalgesellschaft oder Genossenschaft
- **Beachten:** KER-Rückzahlung (Einlagen nach 31. Dezember 1996) wie Kapitalrückzahlung (Kanton = Bund); kotiert: Art. 33 Abs. 4 StG
- **Bemerkung:** Art. 31bis StG regelt die Teilbesteuerung im Geschäftsvermögen; für Privatvermögen gilt das Formular (Abzug 4.4, 30%). Bund: Satz nicht aus 2026-Quelle geprüft.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.2 aus Beteiligungen an Gesellschaften ab 10 Prozent (Privatvermögen) 147»
  - [StG SG Art. 31 bis](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-31bis.md) `sg-stg-2026__art-31bis` – «im Umfang von 70 Prozent steuerbar»
  - [StG SG Art. 33](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-33-t3.md) `sg-stg-2026__art-33-t3` – «sind im Umfang von 70 Prozent steuerbar, wenn diese Beteiligungsrechte wenigstens 10 Prozent»
  - [StG SG Art. 33](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-33-t3.md) `sg-stg-2026__art-33-t3` – «wird gleich behandelt wie die Rückzahlung von Grund- oder Stammkapital»
  - [DBG Art. 20](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-20-t3.md) `bund-dbg-2026__art-20-t3` – «sind im Umfang von 70 Prozent steuerbar, wenn diese Beteiligungsrechte mindestens 10 Prozent»
  - [StG SG Art. 33](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-33-t4.md) `sg-stg-2026__art-33-t4` – «ist die Rückzahlung im Umfang der halben Differenz zwischen der Rückzahlung und der Ausschüttung»
  - [DBG Art. 20](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-20-t3.md) `bund-dbg-2026__art-20-t3` – «wird gleich behandelt wie die Rückzahlung von Grund- oder Stammkapital»

<a id="4-3-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.3 – Erträge aus Beteiligungen an Gesellschaften ab 10 Prozent, Geschäftsvermögen (Code 149)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 2 bzw. verbuchte Beteiligungserträge der Jahresrechnung
- **Rein:** Formular 2 (Geschäftsvermögen) → Erträge aus Beteiligungen ≥ 10% · Jahresrechnung → im Reingewinn verbuchte Beteiligungserträge · Bund: Spartenrechnung → Ertrag nach zurechenbarem Aufwand
- **Rechnen:** Σ Dividenden, Gewinnanteile, Liquidationsüberschüsse, geldwerte Vorteile aus Beteiligungen ≥ 10% (Geschäftsvermögen) → Code 149; 70% steuerbar via Ziff. 4.4
- **Regel:** Beteiligungserträge ab 10% im Geschäftsvermögen; Teilbesteuerung (70% steuerbar) über Abzug Ziff. 4.4.
- **Beachten:** Veräusserungsgewinne solcher Beteiligungen ebenfalls 70% steuerbar, wenn ≥ 1 Jahr im Eigentum (Kanton = Bund)
- **Beachten:** Bund: verbuchte Erträge in Ziff. 2 abziehen, im WV mit «G» bezeichnen → Ziff. 4; Spartenrechnung beilegen
- **Beachten:** Beteiligung ≥ 20% kann beim Erwerb zum Geschäftsvermögen erklärt werden (Art. 31 Abs. 2 StG)
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.3 aus Beteiligungen an Gesellschaften ab 10 Prozent (Geschäftsvermögen) 149»
  - [StG SG Art. 31 bis](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-31bis.md) `sg-stg-2026__art-31bis` – «Dividenden, Gewinnanteile, Liquidationsüberschüsse und geldwerte Vorteile aus Aktien»
  - [DBG Art. 18b](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-18b.md) `bund-dbg-2026__art-18b` – «nach Abzug des zurechenbaren Aufwandes im Umfang von 70 Prozent steuerbar»
  - [DBG Art. 18b](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-18b.md) `bund-dbg-2026__art-18b` – «mindestens ein Jahr im Eigentum der steuerpflichtigen Person»
  - [StG SG Art. 31 bis](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-31bis.md) `sg-stg-2026__art-31bis` – «wenigstens ein Jahr im Eigentum des Steuerpflichtigen»
  - [WL 2a 2026 S. 2](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0011.md) `bund-wl-2a-2026__c0011` – «Die Erträge der zum Geschäftsvermögen gehörenden»
  - [WL 2a 2026 S. 2](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0011.md) `bund-wl-2a-2026__c0011` – «dort am Rande mit G zu bezeichnen und auf Ziffer»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0022.md) `bund-wl-2a-2026__c0022` – «Spartenrechnung wird von Amtes wegen bei der Bemessung»
  - [StG SG Art. 31](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-31-t1.md) `sg-stg-2026__art-31-t1` – «wenn der Eigentümer sie im Zeitpunkt des Erwerbs zum Geschäftsvermögen erklärt»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.4 Abzug Teilbesteuerung Beteiligungserträge 150»

<a id="4-4-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 4.4 – Abzug Teilbesteuerung Beteiligungserträge (Code 150)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → 30% der Summe Ziff. 4.2 und 4.3
- **Rein:** Übertrag Ziff. 4.2 (Code 147) · Übertrag Ziff. 4.3 (Code 149)
- **Rechnen:** − 30% × (Ziff. 4.2 + Ziff. 4.3) → Code 150 (Minuszeile); steuerbar bleiben 70% (Kanton = Bund)
- **Regel:** Abzug (Minuszeile) von 30% der Beteiligungserträge Ziff. 4.2 und 4.3; steuerbar bleiben 70%.
- **Beachten:** Geschäftsvermögen: Basis = Ertrag nach Abzug des zurechenbaren Aufwands
- **Beachten:** Nur Beteiligungen ≥ 10% des Grund-/Stammkapitals; übrige Dividenden voll in Ziff. 4.1
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.4 Abzug Teilbesteuerung Beteiligungserträge 150»
  - [StG SG Art. 31 bis](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-31bis.md) `sg-stg-2026__art-31bis` – «im Umfang von 70 Prozent steuerbar»
  - [StG SG Art. 33](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-33-t3.md) `sg-stg-2026__art-33-t3` – «sind im Umfang von 70 Prozent steuerbar, wenn diese Beteiligungsrechte wenigstens 10 Prozent»
  - [DBG Art. 20](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-20-t3.md) `bund-dbg-2026__art-20-t3` – «sind im Umfang von 70 Prozent steuerbar, wenn diese Beteiligungsrechte mindestens 10 Prozent»
  - [DBG Art. 18b](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-18b.md) `bund-dbg-2026__art-18b` – «nach Abzug des zurechenbaren Aufwandes im Umfang von 70 Prozent steuerbar»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Der Abzug beträgt 30 Prozent der»

<a id="5-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. 5 – Ertrag aus Liegenschaften gemäss Formular 7 (Code 712)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Formular 7 «Total Erträge» (Eigenmietwert, Mietzinseinnahmen)
- **Rein:** Formular 7 → Total Erträge (Code 712) · Schätzungsentscheid (Grundstückschätzung) → Mietwert selbst bewohnte Liegenschaft · Mietverträge/Mieterspiegel → Bruttomietzinse · Antrag Unternutzung → Nachweis dauernd unbenutzter Räume
- **Rechnen:** Σ Formular 7: Eigenmietwert (Kanton −30%, wenn am Wohnsitz dauernd selbst bewohnt) + Bruttomietzinse + übrige Erträge (Baurecht, Kies/Sand u.a.) → Code 712
- **Regel:** Eigenmietwert und Mietzinseinnahmen aus Formular 7. Mietwert des dauernd selbst bewohnten Eigenheims am Wohnsitz wird um 30% herabgesetzt (Art. 34 Abs. 3 StG); Unternutzungsabzug nur auf Antrag; Reduktion nur für Steuerpflichtige im ordentlichen AHV-Rentenalter bei offensichtlichem Missverhältnis (Art. 34 Abs. 4 StG; nicht unter 60% der mittleren Marktmiete); Art. 14 StV: Mietwert > 30% der Bruttoeinkünfte und steuerbares Vermögen höchstens Fr. 600'000. Zweit-/Ferienwohnungen und vermietete Objekte: keine Herabsetzung.
- **Beachten:** Keine 30%-Herabsetzung für Zweit-/Ferienwohnungen und vermietete Objekte (auch Vorzugsmiete/Gebrauchsleihe)
- **Beachten:** Unternutzung (auf Antrag, dauernd unbenutzt): Abzug = EMW nach 30% × unbenutzte Zimmer ÷ (Zimmer + 2)
- **Beachten:** Kanton, AHV-Alter: EMW > 30% Bruttoeinkünfte und Vermögen ≤ 600'000 → Kürzung um den Überschuss, min. 60% Marktmiete
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **30 % (Mietwert des Eigenheims, das am Wohnsitz dauernd selbst bewohnt wird, wird um 30 % herabgesetzt; dauerhafter Unternutzung wird auf Antrag Rechnung getragen. Im AHV-Rentenalter weitere Reduktion bei offensichtlichem Missverhältnis (nicht unter 60 % der Marktmiete; Art. 14 StV: Mietwert über 30 % der Bruttoeinkünfte und steuerbares Vermögen höchstens Fr. 600'000).)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Bemerkung:** Formular 7/2026 nicht publiziert (Ausfüllhilfe Formular 7/2025 nicht übertragbar).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Ertrag aus Liegenschaften Formular 7 712»
  - [StG SG Art. 34](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-34.md) `sg-stg-2026__art-34` – «wird um 30 Prozent herabgesetzt»
  - [StB 34 Nr. 1 S. 2–3](../../chunks/sg/dauernd/sg-stb-34-1/sg-stb-34-1__c0008.md) `sg-stb-34-1__c0008` – «Zweitwohnungen, Ferienwohnungen sowie von vermieteten Objekten»
  - [StV SG Art. 14](../../chunks/sg/2025/sg-stv/sg-stv__art-14.md) `sg-stv__art-14` – «das steuerbare Vermögen des Steuerpflichtigen höchstens Fr. 600 000.– beträgt»
  - [StV SG Art. 14](../../chunks/sg/2025/sg-stv/sg-stv__art-14.md) `sg-stv__art-14` – «er 30 Prozent der Bruttoeinkünfte des Steuerpflichtigen übersteigt»
  - [StB 34 Nr. 1 S. 4](../../chunks/sg/dauernd/sg-stb-34-1/sg-stb-34-1__c0013.md) `sg-stb-34-1__c0013` – «um 30% reduzierter Eigenmietwert (vgl. oben Ziff. 2.4) x Anzahl nicht benutzte Zimmer Anzahl Zimmer + 2»
  - [StB 34 Nr. 1 S. 3–4](../../chunks/sg/dauernd/sg-stb-34-1/sg-stb-34-1__c0012.md) `sg-stb-34-1__c0012` – «Vorausgesetzt ist eine tatsächliche und dauernde Nichtbenutzung von Räumen»
  - [StV SG Art. 14](../../chunks/sg/2025/sg-stv/sg-stv__art-14.md) `sg-stv__art-14` – «wird im Verfahren nach dem Gesetz über die Durchführung der Grundstückschätzung»
  - [StG SG Art. 34](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-34.md) `sg-stg-2026__art-34` – «Einkünfte aus der Ausbeutung von Kies, Sand und anderen Bestandteilen des Bodens»
  - [StG SG Art. 34](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-34.md) `sg-stg-2026__art-34` – «Eine Reduktion unter 60 Prozent der mittleren Marktmiete»
  - [StV SG Art. 14](../../chunks/sg/2025/sg-stv/sg-stv__art-14.md) `sg-stv__art-14` – «wird der Mietwert soweit reduziert, wie er 30 Prozent der Bruttoeinkünfte»

<a id="6-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 6.1 – Unterhaltsbeiträge erhalten: für Steuerpflichtige (Code 154) / für minderjährige Kinder (Code 156)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil bzw. -vereinbarung, Zahlungsnachweise (Jahressumme)
- **Rein:** Scheidungsurteil/Trennungsvereinbarung → vereinbarte Beiträge (für sich / je Kind) · Kontoauszüge/Zahlungsnachweise → im Steuerjahr erhaltene Beiträge
- **Rechnen:** Σ im Steuerjahr erhaltene laufende Unterhaltsbeiträge: für sich → Code 154; für minderjährige Kinder unter Sorge/Obhut → Code 156 (Kanton = Bund)
- **Regel:** Erhaltene Unterhaltsbeiträge für sich (Code 154) und für unter der elterlichen Sorge/Obhut stehende Kinder (Code 156) sind voll steuerbar; nur laufende Beiträge (Art. 15 StV). Der Zahler zieht sie in Ziff. 12.1/12.2 ab.
- **Beachten:** Kapitalabfindung statt laufender Beiträge: beim Empfänger nicht steuerbar (Bund); SG: nur laufende Beiträge
- **Beachten:** Beiträge für volljährige Kinder (z.B. Studium) nicht steuerbar – weder beim Elternteil noch beim Kind (Bund)
- **Beachten:** Naturalleistungen anstelle Barzahlung (Miete, KK-Prämien, Schuldzinsen) gelten als Unterhalt (Bund)
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «6.1 Unterhaltsbeiträge für den/die Steuerpflichtige(n) 154»
  - [StG SG Art. 36](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-36.md) `sg-stg-2026__art-36` – «Unterhaltsbeiträge, die ein Steuerpflichtiger bei Scheidung, gerichtlicher oder tatsächlicher Trennung für sich erhält»
  - [StV SG Art. 15](../../chunks/sg/2025/sg-stv/sg-stv__art-15.md) `sg-stv__art-15` – «gelten ausschliesslich die laufenden Beiträge»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0028.md) `bund-wl-2a-2026__c0028` – «werden, sind beim/bei der Empfänger/in nicht steuerbar»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0027.md) `bund-wl-2a-2026__c0027` – «Unterhaltspflicht über das Mündigkeitsalter des Kindes hinaus»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0028.md) `bund-wl-2a-2026__c0028` – «Elternteil wie beim volljährigen Kind.»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0028.md) `bund-wl-2a-2026__c0028` – «Den Alimenten gleichgesetzt sind Naturalleistungen wie Miete,»

<a id="6-2-einkommen-erbschaften-unverteilt"></a>
### Ziff. 6.2 – Ertrag aus unverteilten Erbschaften (Code 158)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung der Erbengemeinschaft (Anteil am Ertrag)
- **Rein:** Aufstellung Erbengemeinschaft/Willensvollstrecker → Anteil am Ertrag · Steuerauszug Nachlasskonten/-depots → Erträge und Verrechnungssteuer · Inventar/Aufstellung → Anteil Nachlassvermögen (Ziff. 30.5)
- **Rechnen:** Anteil an den Erträgen der unverteilten Erbschaft im Steuerjahr lt. Aufstellung → Code 158
- **Regel:** Anteil am Ertrag der unverteilten Erbschaft (Erbengemeinschaft). Vermögensanteil in Ziff. 30.5. Der Vermögensanfall selbst (Erbschaft/Schenkung) ist steuerfrei (Art. 37 Bst. a StG).
- **Beachten:** Vermögensanfall selbst (Erbschaft, Vermächtnis, Schenkung) steuerfrei (Art. 37 Bst. a StG)
- **Beachten:** Vermögensanteil in Ziff. 30.5 (Code 308) deklarieren
- **Beachten:** Bund: Aufstellung beilegen; VSt-Rückerstattung bei der kantonalen Steuerbehörde beantragen
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «6.2 Ertrag aus unverteilten Erbschaften 158»
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t1.md) `sg-stg-2026__art-37-t1` – «der Vermögensanfall infolge Erbschaft, Vermächtnis, Schenkung oder güterrechtlicher Auseinandersetzung»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.5 Anteile an unverteilten Erbschaften Aufstellung 308»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0029.md) `bund-wl-2a-2026__c0029` – «Über diese Einkünfte ist eine Aufstellung beizulegen.»

<a id="6-3-einkommen-uebrige"></a>
### Ziff. 6.3 – Übrige Einkünfte (Code 162): Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Urheberrechte, Lizenzen, Patente usw.

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Mitarbeiterbeteiligung (Mitarbeiteraktien, Optionen, Anwartschaften/RSU, Beiblatt zum Lohnausweis), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Aufstellung/Beleg der jeweiligen Einkunftsart
- **Rein:** Abrechnungen Provisionen/Lizenzen/Urheberrechte → Bruttoeinnahmen · Bescheinigung Auszahler → Entschädigungen (Aufgabe/Nichtausübung Tätigkeit oder Recht) · Beiblatt Mitarbeiterbeteiligungen → geldwerter Vorteil, falls nicht im Lohnausweis · Aufstellung Untervermietung → Nettoertrag (Bund-Praxis)
- **Rechnen:** Σ übrige steuerbare Einkünfte je Art mit Bezeichnung (Provisionen, Trinkgelder ausserhalb LA, Lizenzen, Entschädigungen Art. 36 StG) → Code 162
- **Regel:** Alle übrigen steuerbaren Einkünfte mit Angabe der Art. Erwerbsersatz-, Entschädigungs- und Leistungsarten gemäss Art. 36 StG. Mitarbeiterbeteiligungen: geldwerter Vorteil Lohnausweis Ziff. 5 / Beiblatt; vom Arbeitgeber getragene Weiterbildung ist kein geldwerter Vorteil (Art. 30 Abs. 1bis StG).
- **Beachten:** Mitarbeiterbeteiligungen/Trinkgelder nur, wenn nicht schon im Lohnausweis (Ziff. 5 bzw. 7) → sonst in Ziff. 1.1
- **Beachten:** Anwartschaften (noch nicht steuerbare Optionen, Phantom-Aktien): keine Deklaration LA Ziff. 5, nur Hinweis Ziff. 15
- **Beachten:** Lotterie-/Geldspielgewinne gehören in Ziff. 4.1 (Formular 2), nicht hierher
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «6.3 Übrige Einkünfte Arten 162»
  - [StG SG Art. 36](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-36.md) `sg-stg-2026__art-36` – «Entschädigungen für die Aufgabe oder Nichtausübung einer Tätigkeit»
  - [WL Lohnausweis 2026 S. 12–13](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0028.md) `bund-wl-lohnausweis-2026__c0028` – «aus Mitarbeiterbeteiligungen (z. B. Aktien und/oder Optionen usw.)»
  - [WL Lohnausweis 2026 S. 13](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0031.md) `bund-wl-lohnausweis-2026__c0031` – «Es gilt dieselbe Regelung wie bei der AHV.»
  - [WL Lohnausweis 2026 S. 12–13](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0029.md) `bund-wl-lohnausweis-2026__c0029` – «Bei anwartschaftlichen Rechten auf Mitarbeiterbeteiligungen wie beispielsweise auf noch»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0030.md) `bund-wl-2a-2026__c0030` – «aus Untervermietung von Wohnungen oder Zimmern und im»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0030.md) `bund-wl-2a-2026__c0030` – «Lohnausweis nicht ausgewiesene Trinkgelder sowie Beiträge an»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.1 Aus Haupterwerbstätigkeit Person 1 Lohnausweis 100»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Einschliesslich Gewinne aus Lotterien und anderen»

<a id="6-4-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 6.4 – Kapitalabfindungen für wiederkehrende Leistungen für … Jahre (Code 164)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Auszahlungsbetrag und Anzahl Jahre gemäss Bescheinigung
- **Rein:** Bescheinigung/Vereinbarung Auszahler → Kapitalbetrag und Anzahl Jahre · Aufhebungsvereinbarung Arbeitsvertrag → Abfindung (Grund, Vorsorgecharakter?)
- **Rechnen:** Kapitalbetrag → Code 164 (+ Anzahl Jahre); Satz wie bei entsprechender jährlicher Leistung zusammen mit übrigen Einkünften (Art. 51 StG / Art. 37 DBG)
- **Regel:** Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz): Steuer zum Satz, der sich bei entsprechender jährlicher Leistung ergäbe (Art. 51 StG). Kapitalleistungen aus Vorsorge gehören auf Seite 4 (Ziff. 40), nicht hierher.
- **Beachten:** Kapitalleistungen aus Vorsorge (Säule 3a, 2. Säule) nicht hier → Seite 4, Ziff. 40 (gesondert, Art. 52 StG)
- **Beachten:** Bund: z.B. Entschädigung für Aufgabe/Nichtausübung einer Tätigkeit oder eines Rechts, Abfindung aus Arbeitsvertrag
- **Beachten:** Bund: Abgangsentschädigung mit Vorsorgecharakter gesondert; ohne (z.B. «Golden Parachute») mit übrigem Einkommen
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Kapitalabfindungen für wiederkehrende Leistungen für Jahre 164»
  - [StG SG Art. 51](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-51.md) `sg-stg-2026__art-51` – «wird die Steuer unter Berücksichtigung der übrigen Einkünfte zu dem Satz berechnet»
  - [DBG Art. 37](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-37.md) `bund-dbg-2026__art-37` – «zu dem Steuersatz berechnet, der sich ergäbe, wenn anstelle der einmaligen Leistung»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0013.md) `sg-form-1-2026-uj__c0013` – «40.2 aus Einrichtungen der beruflichen Vorsorge (2. Säule) Bescheinigung»
  - [StG SG Art. 52](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-52.md) `sg-stg-2026__art-52` – «Kapitalleistungen nach Art. 35 dieses Erlasses, gleichartige Kapitalabfindungen des Arbeitgebers»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0027.md) `bund-wl-2a-2026__c0027` – «Werden Kapitalabfindungen für wiederkehrende Leistungen»
  - [WL 2a 2026 S. 9](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0068.md) `bund-wl-2a-2026__c0068` – «Kapitalabfindungen ohne Vorsorgecharakter (z.B. Abgangs-»

<a id="7-berechnung-total"></a>
### Ziff. 7 – Total der Einkünfte (Code 168)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 1.1–1.3, 2.1–2.2, 3.1–3.5 · Übertrag Ziff. 4.1–4.3 abzüglich Ziff. 4.4, Ziff. 5, Ziff. 6.1–6.4
- **Rechnen:** Σ Ziff. 1.1 bis 6.4 − Ziff. 4.4 (Code 150) → Code 168; Ziff. 8 (Codes 290–292) nicht mitzählen
- **Regel:** Rechenzeile: Summe Ziff. 1 bis 6 (inkl. Abzugszeile 4.4). Ziff. 8 (ergänzende Angaben) zählt nicht mit.
- **Beachten:** Ziff. 8.1–8.3 (vereinfacht abgerechnet, EL, Hilflosenentschädigung) gehören nicht ins Total
- **Beachten:** Kapitalleistungen aus Vorsorge (Ziff. 40) nicht im Total; gesondert besteuert (Art. 52 StG)
- **Beachten:** Unterjährig: Satz auf Jahreseinkommen umgerechnet von Amtes wegen; unregelmässige Einkünfte bezeichnen
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «7. Total der Einkünfte 168»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «Ergänzende Angaben (nicht im Total der Einkünfte zu berücksichtigen)»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.1 Aus Haupterwerbstätigkeit Person 1 Lohnausweis 100»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0013.md) `sg-form-1-2026-uj__c0013` – «41. Total Kapitalleistungen aus Vorsorge 950»
  - [StG SG Art. 52](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-52.md) `sg-stg-2026__art-52` – «werden gesondert besteuert. Sie unterliegen einer vollen Jahressteuer.»
  - [MB 8/2026 SG S. 2–3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0005.md) `sg-mb-8-2026__c0005` – «Unregelmässig fliessende Einkünfte sind zu bezeichnen und auszuweisen»

## Einkünfte (ergänzende Angaben)

<a id="8-1-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 8.1 – Vereinfacht abgerechnete Einkünfte, Bruttolohn (Code 290; nicht im Total der Einkünfte)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Ausgleichskasse (Bruttolohn)
- **Rein:** Bescheinigung/Bestätigung AHV-Ausgleichskasse (vereinfachtes Verfahren BGSA) → Bruttolohn
- **Rechnen:** Bruttolohn lt. Bescheinigung der Ausgleichskasse → Code 290 (nur Angabe, nicht im Total Ziff. 7)
- **Regel:** Nur Information: im vereinfachten Verfahren (Steuern vom Arbeitgeber direkt mit Ausgleichskasse abgerechnet) bezogener Bruttolohn; nicht im Total der Einkünfte zu berücksichtigen.
- **Beachten:** Steuer mit der AG-Abrechnung über die AHV-Ausgleichskasse abgegolten; Deklaration ohne Einfluss auf Steuer (Bund)
- **Beachten:** Bund: 0,5% auf kleine Arbeitsentgelte, ohne Berufskosten und Sozialabzüge (Art. 37a DBG)
- **Beachten:** SG: Bruttolohn zählt zu den Bruttoeinkünften für den Eigenmietwert-Härtefall (StB 34 Nr. 1)
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «8.1 Vereinfacht abgerechnete Einkünfte Bescheinigung 290»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «Ergänzende Angaben (nicht im Total der Einkünfte zu berücksichtigen)»
  - [WL 2a 2026 S. 9](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0067.md) `bund-wl-2a-2026__c0067` – «Die Deklaration auf der Steuererklärung hat keinen»
  - [DBG Art. 37a](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-37a.md) `bund-dbg-2026__art-37a` – «zu einem Satz von 0,5 Prozent zu erheben»
  - [StB 34 Nr. 1 S. 4–5](../../chunks/sg/dauernd/sg-stb-34-1/sg-stb-34-1__c0016.md) `sg-stb-34-1__c0016` – «./. alle anrechenbaren Eigenmietwerte + vereinfacht abgerechnete Bruttolöhne»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «7. Total der Einkünfte 168»

<a id="8-2-info-steuerfreie-leistungen"></a>
### Ziff. 8.2 – Ergänzungsleistungen / Überbrückungsleistungen für ältere Arbeitslose (Code 291)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung der Durchführungsstelle
- **Rein:** EL-Verfügung/Jahresbescheinigung der Durchführungsstelle → Jahresbetrag EL · Verfügung Überbrückungsleistungen für ältere Arbeitslose → Jahresbetrag
- **Rechnen:** Σ EL zur AHV/IV + Überbrückungsleistungen → Code 291 (nur Angabe, steuerfrei, nicht im Total Ziff. 7)
- **Regel:** Nur Angabe, steuerfrei: Ergänzungsleistungen zur AHV/IV sind nicht steuerbar; nicht im Total der Einkünfte.
- **Beachten:** Steuerfrei: EL (Art. 37 Bst. i StG) und Überbrückungsleistungen (Art. 37 Bst. r StG); Bund ebenso (Art. 24 DBG)
- **Beachten:** AHV-/IV-Rente selbst bleibt steuerbar → Ziff. 3.1
- **Beachten:** SG: EL zählen zu den Bruttoeinkünften für den Eigenmietwert-Härtefall (StB 34 Nr. 1)
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «8.2 Ergänzungsleistungen / Überbrückungsleistungen für ältere Arbeitslose 291»
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t2.md) `sg-stg-2026__art-37-t2` – «die Einkünfte aufgrund der Bundesgesetzgebung über Ergänzungsleistungen»
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t3.md) `sg-stg-2026__art-37-t3` – «Einkünfte aufgrund des Bundesgesetzes über Überbrückungsleistungen für ältere Arbeitslose»
  - [DBG Art. 24](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-24-t2.md) `bund-dbg-2026__art-24-t2` – «die Einkünfte aufgrund der Bundesgesetzgebung über Ergänzungsleistungen»
  - [DBG Art. 24](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-24-t3.md) `bund-dbg-2026__art-24-t3` – «Einkünfte aufgrund des Bundesgesetzes vom 19. Juni 2020 über Überbrückungsleistungen»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0004.md) `sg-form-1-2026-uj__c0004` – «3.1 AHV/IV-Renten (zu 100%) Person 1 Bescheinigung 126»
  - [StB 34 Nr. 1 S. 4–5](../../chunks/sg/dauernd/sg-stb-34-1/sg-stb-34-1__c0016.md) `sg-stb-34-1__c0016` – «+ Ergänzungsleistungen + Hilflosenentschädigungen»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «Ergänzende Angaben (nicht im Total der Einkünfte zu berücksichtigen)»

<a id="8-3-info-steuerfreie-leistungen"></a>
### Ziff. 8.3 – Hilflosenentschädigungen (Code 292)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung der Ausgleichskasse/Versicherung
- **Rein:** Verfügung Ausgleichskasse/IV/Unfall-/Militärversicherung → Jahresbetrag Hilflosenentschädigung (HE)
- **Rechnen:** Jahresbetrag Hilflosenentschädigung lt. Verfügung → Code 292 (nur Angabe, nicht im Total Ziff. 7)
- **Regel:** Nur Angabe (nicht im Total der Einkünfte). Hilflosenentschädigung kann in Ziff. 21.2 als behinderungsbedingte Kosten relevant sein.
- **Beachten:** Bund (KS 11): HE-Bezüger gelten als Personen mit Behinderung → Kosten Ziff. 21.2 ohne Selbstbehalt (Kanton Art. 46 StG)
- **Beachten:** Bund (KS 11): Pauschale statt effektiver Kosten – HE leicht 2'500 / mittel 5'000 / schwer 7'500; effektiv: HE anrechnen
- **Beachten:** SG: HE zählt zu den Bruttoeinkünften für den Eigenmietwert-Härtefall (StB 34 Nr. 1)
- **Bemerkung:** Steuerfreiheit nicht aus einer Rechtsnorm 2026 zitiert; Formular führt Position unter «nicht im Total der Einkünfte».
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «8.3 Hilflosenentschädigungen 292»
  - [KS 11 S. 6–7](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0011.md) `bund-ks-11__c0011` – «Bezüger von Hilflosenentschädigungen im Sinne von Artikel 43 bis des Bundesgesetzes»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «21.2 Behinderungsbedingte Kosten (ohne Selbstbehalt) Formular 6 235»
  - [StG SG Art. 46](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-46.md) `sg-stg-2026__art-46` – «die behinderungsbedingten Kosten des Steuerpflichtigen oder der von ihm unterhaltenen Personen»
  - [KS 11 S. 10](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0025.md) `bund-ks-11__c0025` – «Bezüger einer Hilflosenentschädigung leichten Grades: CHF 2'500.--»
  - [StB 34 Nr. 1 S. 4–5](../../chunks/sg/dauernd/sg-stb-34-1/sg-stb-34-1__c0016.md) `sg-stb-34-1__c0016` – «+ Ergänzungsleistungen + Hilflosenentschädigungen»
  - [KS 11 S. 10–11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0026.md) `bund-ks-11__c0026` – «und sind bei diesen Kosten anzurechnen»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «Ergänzende Angaben (nicht im Total der Einkünfte zu berücksichtigen)»

## Abzüge

<a id="10-1-berechnung-total"></a>
### Ziff. 10.1 – Berufskosten bei unselbständiger Erwerbstätigkeit Person 1 gemäss Formular 4 (Code 438)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 4 «Total der Berufskosten» Person 1
- **Rein:** Formular 4 «Total der Berufskosten» Person 1 → Code 438 · Lohnausweis Felder F/G, Ziff. 2.2 → Fahrkosten-/Verpflegungsabzug prüfen · Abo-/Fahrkostenbelege, Anzahl Arbeitstage → Fahrkosten · Belege übrige Berufskosten (nur bei Nachweis höherer Kosten)
- **Rechnen:** Formular 4: min(Fahrkosten; Kanton 8'000 / Bund 3'300) + Verpflegung + übrige (Kanton 700 + 10% Netto, max. 2'400 / Bund 3%, min. 2'000, max. 4'000) + Nebenerwerb
- **Regel:** Total des Formulars 4 (Fahrkosten bis Fr. 8'000, Verpflegung, Wochenaufenthalt, übrige Berufskosten, Nebenerwerb) übertragen. Pauschalierte Abzüge werden bei unterjähriger Steuerpflicht anteilig gekürzt (MB 8/2026: Ziff. 10, Formular 4 Ziff. 3.1 und 5.1), Fahrkosten-Maximum nicht (StB 39 Nr. 3 Ziff. 3). Einzelheiten siehe Hilfsblatt-Positionen Formular 4 unten.
- **Beachten:** Unterjährig: Pauschalen (Formular 4 Ziff. 3.1, 5.1) pro rata kürzen; Fahrkosten-Maximum nicht kürzen
- **Beachten:** Auto nur ohne zumutbaren ÖV: 0.75/km (Kanton = Bund); Kanton: 220 Arbeitstage, Homeoffice-Tage ohne Fahrkosten
- **Beachten:** Geschäftswagen mit Pauschale (LA Ziff. 2.2): Arbeitsweg abgegolten → kein Fahrkostenabzug
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 (Maximalabzug, keine Pauschale; bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Pauschale für übrige Berufskosten: höchstens Fr. 2'400.)** · Bund **CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockel der Pauschale für übrige Berufskosten: Fr. 700 (zuzüglich 10 % der Nettoeinkünfte).)** · Bund **n/a – Formel ohne fixen Anteil (3 % des Nettolohns, min. 2'000, max. 4'000).**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Übrige Berufskosten: Pauschale Fr. 700 zuzüglich 10 % der Nettoeinkünfte, höchstens Fr. 2'400. Nachweis höherer notwendiger Kosten bleibt vorbehalten. Nettoeinkünfte = Bruttoeinkünfte abzüglich AHV/BVG-/Sozialversicherungsprämien nach Art. 45 Abs. 1 lit. d und f StG (ohne Einkäufe).)** · Bund **3 % (Übrige Berufskosten: Pauschale 3 % des Nettolohns, mindestens CHF 2'000, höchstens CHF 4'000 pro Jahr; Nachweis höherer tatsächlicher Kosten möglich. Bei Teilzeit/Teiljahr angemessen zu kürzen.)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **n/a – Formel 700 + 10 % kennt kein Minimum (Art. 21 Abs. 1 StV SG).** · Bund **CHF 2'000 (Mindestbetrag der Pauschale übrige Berufskosten.)**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.75 (Privates Motorfahrzeug (Auto): 75 Rappen je Fahrkilometer, sofern kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung nicht zumutbar ist; im Rahmen des Maximalabzugs von Fr. 8'000.)** · Bund **CHF 0.75 (Privatauto: CHF 0.75 pro Fahrkilometer, nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist; Gesamtmaximum CHF 3'300.)**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **220 Tage (Für die Berechnung des Fahrkostenabzugs wird von 220 Arbeitstagen pro Kalenderjahr (Vollzeitstelle) ausgegangen, sofern nicht eine höhere Anzahl nachgewiesen wird. Homeoffice-Tage und Tage ohne Arbeitsleistung zählen nicht.)** · Bund **n/a – Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).**
- **Bund:** Fahrkosten max. Fr. 3'300 (Art. 26 Abs. 1 Bst. a DBG); Pauschalen BKV-Anhang 2026.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «10.1 Person 1 Formular 4 438»
  - [StG SG Art. 39](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-39.md) `sg-stg-2026__art-39` – «die notwendigen Kosten für Fahrten zwischen Wohn- und Arbeitsstätte bis zum Betrag von Fr. 8000.–»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Berufskosten ( Formular 4, Ziffer 3.1 und 5.1 )»
  - [StV SG Art. 21](../../chunks/sg/2025/sg-stv/sg-stv__art-21.md) `sg-stv__art-21` – «Für übrige notwendige Berufskosten werden Fr. 700.– zuzüglich 10 Prozent der Nettoeinkünfte, höchstens Fr. 2400.– abgezogen.»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0040.md) `bund-wl-2a-2026__c0040` – «Der Pauschalabzug beträgt 3 % des Nettolohnes, mindestens»
  - [StB 39 Nr. 3 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0011.md) `sg-stb-39-3__c0011` – «Es handelt sich um einen Maximalabzug und nicht um eine Pauschale.»
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0010.md) `sg-stb-39-3__c0010` – «Für Homeoffice-Tage und Tage ohne Arbeitsleistung»
  - [StB 39 Nr. 3 S. 5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0017.md) `sg-stb-39-3__c0017` – «Wird die Pauschale beansprucht, entfällt die Aufrechnung für den Arbeitsweg»
  - [StB 39 Nr. 3 S. 5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0018.md) `sg-stb-39-3__c0018` – «Im Lohnausweis muss in Ziff. 2.2 nur noch der Privatanteil deklariert werden»
  - [StB 39 Nr. 3 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0011.md) `sg-stb-39-3__c0011` – «wird der Betrag bei unterjähriger Steuerpflicht»
  - [StB 39 Nr. 3 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0011.md) `sg-stb-39-3__c0011` – «2026 Fr. 8'000.-- Fr. 3'300.--»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer keine Kosten für den Arbeitsweg»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «die Möglichkeit einräumt, das Mittag- oder Abendessen verbilligt»

<a id="10-2-berechnung-total"></a>
### Ziff. 10.2 – Berufskosten bei unselbständiger Erwerbstätigkeit Person 2 gemäss Formular 4 (Code 488)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 4 «Total der Berufskosten» Person 2
- **Rein:** Lohnausweis Person 2 → Nettolohn Ziff. 11; Felder F (Gratis-Arbeitsweg) / G (Kantine, Lunch-Checks) · Arbeitsweg Person 2 (Distanz, Arbeitstage, Verkehrsmittel/ÖV-Abo) → Fahrkosten Formular 4 · Belege höherer übriger Berufskosten (nur wenn über Pauschale) → Formular 4 · Übertrag Formular 4 «Total der Berufskosten» Person 2 → Code 488
- **Rechnen:** Formular 4 P2: Fahrkosten (max. 8'000 / Bund 3'300) + Verpflegung (15/Tag, max. 3'200) + übrige BK (700 + 10% Nettoeinkünfte, max. 2'400 / Bund 3%, 2'000–4'000)
- **Regel:** Wie Ziff. 10.1 für Person 2; jeder unselbständig erwerbende Ehegatte hat eigene Berufskosten (StB 39 Nr. 8 Ziff. 1.1).
- **Beachten:** Eigene BK je unselbständig erwerbendem Ehegatten; Mitarbeit beim andern nur mit Arbeitsverhältnis + Sozialvers.
- **Beachten:** Lohnausweis F angekreuzt → keine Fahrkosten; G → Verpflegung halb (7.50/Tag, max. 1'600); Auto 75 Rp./km (bisher 70)
- **Beachten:** UJ: Pauschalen Formular 4 Ziff. 3.1/5.1 nach Dauer kürzen, für den Satz voll
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 (Maximalabzug, keine Pauschale; bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.75 (Privates Motorfahrzeug (Auto): 75 Rappen je Fahrkilometer, sofern kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung nicht zumutbar ist; im Rahmen des Maximalabzugs von Fr. 8'000.)** · Bund **CHF 0.75 (Privatauto: CHF 0.75 pro Fahrkilometer, nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist; Gesamtmaximum CHF 3'300.)**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswärtige Verpflegung, voller Abzug: Fr. 15 pro Hauptmahlzeit bzw. Tag, max. Fr. 3'200 im Jahr (bei täglicher Heimkehr nicht gleichzeitig mit Wochenaufenthalt). Nachweis höherer Kosten nicht zulässig.)** · Bund **CHF 15 (Auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (in der Regel nur Mittagessen), nur Pauschale zulässig, wenn Hauptmahlzeit wegen grosser Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann oder bei durchgehender Schicht-/Nachtarbeit.)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Voller Abzug auswärtige Verpflegung: max. Fr. 3'200 im Jahr (bei Kürzung für vergütete Mahlzeiten anteilig nach Arbeitstagen).)** · Bund **CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Halber Abzug Fr. 7.50 pro Hauptmahlzeit bzw. Tag, wenn Verpflegung im Personalrestaurant möglich ist oder durch angemessenen Arbeitgeberbeitrag verbilligt wird (Lohnausweis Feld G).)** · Bund **CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Halber Abzug bei verbilligter Verpflegung: max. Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockel der Pauschale für übrige Berufskosten: Fr. 700 (zuzüglich 10 % der Nettoeinkünfte).)** · Bund **n/a – Formel ohne fixen Anteil (3 % des Nettolohns, min. 2'000, max. 4'000).**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Übrige Berufskosten: Pauschale Fr. 700 zuzüglich 10 % der Nettoeinkünfte, höchstens Fr. 2'400. Nachweis höherer notwendiger Kosten bleibt vorbehalten. Nettoeinkünfte = Bruttoeinkünfte abzüglich AHV/BVG-/Sozialversicherungsprämien nach Art. 45 Abs. 1 lit. d und f StG (ohne Einkäufe).)** · Bund **3 % (Übrige Berufskosten: Pauschale 3 % des Nettolohns, mindestens CHF 2'000, höchstens CHF 4'000 pro Jahr; Nachweis höherer tatsächlicher Kosten möglich. Bei Teilzeit/Teiljahr angemessen zu kürzen.)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Pauschale für übrige Berufskosten: höchstens Fr. 2'400.)** · Bund **CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **n/a – Formel 700 + 10 % kennt kein Minimum (Art. 21 Abs. 1 StV SG).** · Bund **CHF 2'000 (Mindestbetrag der Pauschale übrige Berufskosten.)**
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «10.2 Person 2 Formular 4 488»
  - [StB 39 Nr. 8 S. 1](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0002.md) `sg-stb-39-8__c0002` – «stehen die Abzüge für Berufskosten (z.B. für auswärtige Verpflegung) jedem unselbständig erwerbenden Ehegatten zu»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Ziffer 10 Berufskosten ( Formular 4, Ziffer 3.1 und 5.1 )»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Zur Satzbestimmung werden jedoch die»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0009.md) `sg-mb-8-2026__c0009` – «erhöht sich auf 75 Rappen pro Kilometer (bisher 70 Rappen)»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «wenn dem Arbeitnehmer keine Kosten für den Arbeitsweg er»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten Buchstabe G»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «In diesem Feld ist der für die Steuererklärung massgebende Nettolohn anzugeben.»
  - [StB 39 Nr. 8 S. 1](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0002.md) `sg-stb-39-8__c0002` – «wenn ein Arbeitsverhältnis besteht und hierüber mit den Sozialversicherungen abgerechnet wird»

<a id="11-abzug-schuldzinsen"></a>
### Ziff. 11 – Schuldzinsen gemäss Formular 5 (Code 500)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 5 Teil A (private Schulden und Schuldzinsen); Schuldenausweis der Bank
- **Rein:** Hypothekar-/Zinsbescheinigung Bank → private Schuldzinsen 2026 (Formular 5 Teil A; Schuld → Ziff. 34.1, Code 504) · Kredit-/Darlehensvertrag, Zinsausweis → private Schuldzinsen · Kontoauszug/Zinsausweis → Sollzinsen privater Konten · Übertrag Ziff. 4 (bewegliches Vermögen, nach Abzug 4.4) + Ziff. 5 (Liegenschaften, Code 712) → Limite
- **Rechnen:** min(Σ private Schuldzinsen 2026; steuerbare Vermögenserträge Ziff. 4 + Ziff. 5 + 50'000); Bund analog (Beteiligungserträge Privatvermögen zu 70%)
- **Regel:** Private Schuldzinsen abziehbar im Umfang der steuerbaren Vermögenserträge (Art. 33, 33bis, 34 StG, inkl. Eigenmietwert) zuzüglich Fr. 50'000. Zinsen der Geschäftsschulden gehören in die Jahresrechnung (Ziff. 2). Die Schuld selbst in Ziff. 34.1.
- **Beachten:** Nicht abziehbar: Baukreditzinsen (Anlagekosten); Bund zudem: Amortisation, Leasingraten, Baurechtszins Eigenheim
- **Beachten:** Geschäftsschuldzinsen nicht hier (→ Ziff. 2 selbständige Erwerbstätigkeit); Bund: im Jahr 2026 fällig gewordene Zinsen
- **Beachten:** Bund: teilbesteuerte Beteiligungserträge des Privatvermögens nur zu 70% in die Limite
- **Bund:** Art. 33 Abs. 1 Bst. a DBG: ebenfalls Vermögenserträge zuzüglich 50 000 Franken.
- **Bemerkung:** Formular 5/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «11. Schuldzinsen Formular 5 500»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t1.md) `sg-stg-2026__art-45-t1` – «zuzüglich Fr. 50 000.–»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.1 aus Wertschriften und Guthaben 146»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.4 Abzug Teilbesteuerung Beteiligungserträge 150»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «5. Ertrag aus Liegenschaften Formular 7 712»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «34.1 Privatschulden Formular 5 504»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «2. Einkünfte aus selbständiger Erwerbstätigkeit»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0048.md) `bund-wl-2a-2026__c0048` – «Die im Jahr 2026 fällig gewordenen Schuldzinsen»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0048.md) `bund-wl-2a-2026__c0048` – «abziehbar (wenn nicht bereits in Ziffer 2 berücksichtigt)»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0049.md) `bund-wl-2a-2026__c0049` – «werden nur zu 70 % in die Berechnung einbezogen.»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0049.md) `bund-wl-2a-2026__c0049` – «Zu beachten ist, dass Baukreditzinsen als Anlagekosten gelten»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0062.md) `bund-wl-2a-2026__c0062` – «die Aufwendungen für Schuldentilgung (Amortisation)»
  - [KS 22a S. 5](../../chunks/bund/dauernd/bund-ks-22a/bund-ks-22a__c0015.md) `bund-ks-22a__c0015` – «Leasingraten für privat genutzte Güter enthalten keine abzugsfähigen Zinsanteile»
  - [KS 22a S. 5](../../chunks/bund/dauernd/bund-ks-22a/bund-ks-22a__c0015.md) `bund-ks-22a__c0015` – «Baurechtszinsen für selbstgenutztes Wohneigentum gelten als nicht abzugsfähige»

<a id="12-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.1 – Unterhaltsbeiträge an Geschiedene oder Getrennte (Code 200)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungsurteil/Trennungsvereinbarung (bei erstmaliger Zahlung), Zahlungsnachweise
- **Rein:** Scheidungsurteil/Trennungsvereinbarung → vereinbarter Unterhaltsbeitrag (bei erstmaliger Zahlung beilegen) · Zahlungsnachweise (Bank) → 2026 bezahlte Beiträge (Aufstellung)
- **Rechnen:** Σ 2026 bezahlte Unterhaltsbeiträge an geschiedenen bzw. gerichtlich/tatsächlich getrennt lebenden Ehegatten (Kanton = Bund; Bund: ohne Kapitalabfindung)
- **Regel:** Bezahlte laufende Unterhaltsbeiträge an den geschiedenen/getrennt lebenden Ehegatten voll abziehbar; beim Empfänger Einkommen (Ziff. 6.1). Nicht abziehbar: Leistungen in Erfüllung anderer familienrechtlicher Pflichten. Bei erstmaliger Zahlung Urteil/Vereinbarung beilegen.
- **Beachten:** Gegenstück: beim Empfänger steuerbar (Ziff. 6.1, Code 154; Art. 36 Bst. f StG)
- **Beachten:** Nicht abziehbar: Leistungen aus anderen familienrechtlichen Unterhalts-/Unterstützungspflichten
- **Beachten:** Bund: Kapitalabfindung = Schuldentilgung, nicht abziehbar; Naturalleistungen (Miete, KK-Prämien) = Alimente
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «12.1 Unterhaltsbeiträge an Geschiedene oder Getrennte Aufstellung 200»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t1.md) `sg-stg-2026__art-45-t1` – «die Unterhaltsbeiträge an den geschiedenen, gerichtlich oder tatsächlich getrennt lebenden Ehegatten»
  - [StG SG Art. 36](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-36.md) `sg-stg-2026__art-36` – «Unterhaltsbeiträge, die ein Steuerpflichtiger bei Scheidung, gerichtlicher oder tatsächlicher Trennung für sich erhält»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «6.1 Unterhaltsbeiträge für den/die Steuerpflichtige(n) 154»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0051.md) `bund-wl-2a-2026__c0051` – «Unterhaltsbeiträge, die in Form einer Kapitalabfindung erbracht»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0052.md) `bund-wl-2a-2026__c0052` – «gelten als Schuldentilgung und sind daher nicht»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0051.md) `bund-wl-2a-2026__c0051` – «Den Alimenten gleichgesetzt sind Naturalleistungen wie Miete,»

<a id="12-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.2 – Unterhaltsbeiträge für minderjährige Kinder (Code 202)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise je Kind, Urteil/Vereinbarung
- **Rein:** Urteil/Vereinbarung → Unterhaltsbeitrag je Kind (bei erstmaliger Zahlung beilegen) · Zahlungsnachweise → 2026 bezahlte Beiträge, separat je Kind (Aufstellung)
- **Rechnen:** Σ je Kind 2026 bezahlte Unterhaltsbeiträge an den Elternteil, unter dessen elterlicher Sorge/Obhut das minderjährige Kind steht (Kanton = Bund)
- **Regel:** Unterhaltsbeiträge an den Elternteil für Kinder unter dessen Sorge/Obhut abziehbar; der Zahler kann dann keinen Kinderabzug (Ziff. 23) beanspruchen (Kinderabzug nur, wenn kein Abzug nach Art. 45 Abs. 1 Bst. c StG).
- **Beachten:** Für dieses Kind kein Kinderabzug (Art. 48 StG); Empfänger versteuert in Ziff. 6.1 (Code 156)
- **Beachten:** Bund: minderjährig = am 31.12.2026 noch nicht 18 Jahre alt
- **Beachten:** Bund: Unterhalt an volljähriges Kind (z.B. Studium) nicht hier, nur im Rahmen der Sozialabzüge (Bund-WL Ziff. 23.2)
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «12.2 Unterhaltsbeiträge für minderjährige Kinder Aufstellung 202»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «keinen Abzug nach Art. 45 Abs. 1 Bst. c dieses Erlasses beansprucht»
  - [StG SG Art. 36](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-36.md) `sg-stg-2026__art-36` – «Unterhaltsbeiträge, die ein Elternteil für die unter seiner elterlichen Sorge oder Obhut stehenden Kinder erhält»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «für minderjährige Kinder 156»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «6.1 Unterhaltsbeiträge für den/die Steuerpflichtige(n) 154»
  - [WL 2a 2026 S. 1](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0003.md) `bund-wl-2a-2026__c0003` – «am 31.12.2026 noch nicht 18 Jahre alte»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0051.md) `bund-wl-2a-2026__c0051` – «steuerbaren Leistungen nur im Rahmen von Ziffer 23.2 der»

<a id="12-3-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.3 – Rentenleistungen (Code 204)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Vertrag/Nachweis dauernde Last bzw. Rentenbescheinigung
- **Rein:** Leibrenten-/Verpfründungsvertrag + Zahlungsnachweis → 2026 bezahlte Rente/Verpfründung · Vertrag/Urteil/letztwillige Verfügung dauernde Last → 2026 erbrachte Leistung; Empfänger angeben (Bund) · ESTV-Publikation → Ertragsanteil-Satz (Bund)
- **Rechnen:** Σ dauernde Lasten + bezahlte Leibrente/Verpfründung × Ertragsanteil % (Kanton: Art. 35 Abs. 3 Bst. c StG; Bund: × ESTV-Satz ÷ 100)
- **Regel:** Dauernde Lasten sowie der Ertragsanteil von Leibrenten und Verpfründungsverträgen (ausländische Leibrenten gemäss Art. 35 Abs. 3 Bst. c) abziehbar.
- **Beachten:** Kanton: Formel Art. 7 Abs. 2 Bst. c StHG; r = Rendite zehnjähriger Bundesobligationen + 0,5 Pp. (Steuerjahr + neun VJ)
- **Beachten:** Kanton: r negativ/null → Ertragsanteil null; Bund: nur Leistungen aus Gesetz, Vertrag, Verfügung, kein Familienunterhalt
- **Beachten:** Bund-Beispiele: gesetzliche Haftpflichtrenten, vertraglich/testamentarisch auferlegte Leibrenten an Angestellte
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «12.3 Rentenleistungen Aufstellung 204»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t1.md) `sg-stg-2026__art-45-t1` – «die dauernden Lasten sowie der Ertragsanteil nach Art. 35 Abs. 3 Bst. c»
  - [StG SG Art. 35](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-35-t3.md) `sg-stg-2026__art-35-t3` – «um 0,5 Prozentpunkte erhöhten annualisierten Rendite zehnjähriger Bundesobligationen»
  - [StG SG Art. 35](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-35-t3.md) `sg-stg-2026__art-35-t3` – «während des betreffenden Steuerjahres und der neun vorangegangenen Jahre massgebend»
  - [StG SG Art. 35](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-35-t3.md) `sg-stg-2026__art-35-t3` – «nach der Formel in Art. 7 Abs. 2 Bst. c Ziff. 1 des eidgenössischen Steuerharmonisierungsgesetzes»
  - [StG SG Art. 35](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-35-t3.md) `sg-stg-2026__art-35-t3` – «Ist diese Rendite negativ oder null, so beträgt der Ertragsanteil null Prozent.»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0052.md) `bund-wl-2a-2026__c0052` – «Unter dieser Rubrik ist der Ertragsanteil der bezahlten»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0053.md) `bund-wl-2a-2026__c0053` – «Bezahlte Leibrente / Verpfründung x Berechnungssatz (in %)»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0053.md) `bund-wl-2a-2026__c0053` – «gründeten Verpflichtungen beruhen und nicht der Erfüllung»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0053.md) `bund-wl-2a-2026__c0053` – «Empfänger/in der Leistung ist anzugeben.»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0054.md) `bund-wl-2a-2026__c0054` – «leistungen sind z.B. die gesetzlichen Haftpflichtrenten und die»

<a id="13-1-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.1 – Ordentliche Beiträge Säule 3a (Code 208 Person 1 / 210 Person 2)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → 3a-Bescheinigung der Vorsorgeeinrichtung: im Jahr 2026 bezahlter Betrag
- **Rein:** 3a-Bescheinigung Bankstiftung/Versicherung (Formular 21 EDP Ziff. 2) → 2026 einbezahlter Betrag je Person (Code 208/210) · Lohnausweis/Jahresrechnung → Erwerbseinkommen (nur ohne 2. Säule, für 20%-Limite)
- **Rechnen:** je Person: mit 2. Säule min(Einzahlung 2026; 7'258); ohne 2. Säule min(Einzahlung; 20% × Erwerbseinkommen; 36'288) – Kanton = Bund
- **Regel:** Im Steuerjahr 2026 einbezahlte ordentliche 3a-Beiträge gemäss Bescheinigung. Art. 45 Abs. 1 Bst. e StG SG verweist auf anerkannte Formen der gebundenen Selbstvorsorge nach Art. 82 BVG; die Höchstbeträge entsprechen daher dem Bundesrecht (BVV 3, 2026): Fr. 7'258 mit 2. Säule; ohne 2. Säule 20% des Erwerbseinkommens, höchstens Fr. 36'288.
- **Beachten:** Nur 2026 tatsächlich einbezahlte Beiträge; Bescheinigung beilegen
- **Beachten:** Bund: nur mit Erwerbseinkommen + AHV-/IV-Pflicht; kein Abzug bei Verlust; vorübergehender Unterbruch schadet nicht
- **Beachten:** AG-Beiträge an 3a sind Lohn (Lohnausweis Ziff. 7); mit 3a-Abzug kein Zuschlag «ohne Vorsorge» in Ziff. 14
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a (kleiner Abzug): Höchstabzug CHF 7'258 pro Jahr für Personen, die einer Vorsorgeeinrichtung der 2. Säule angehören. SG verweist für die abziehbaren Beiträge auf die anerkannten Formen der gebundenen Selbstvorsorge nach Art. 82 BVG; Höchstbetrag nach BVV 3 (identisch mit DBG).)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug CHF 7'258 pro Jahr für Personen, die einer Vorsorgeeinrichtung der 2. Säule angehören (8 % des oberen Grenzbetrags nach Art. 8 Abs. 1 BVG). Nur im Steuerjahr tatsächlich einbezahlte Beiträge, mit Bescheinigung.)**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a (grosser Abzug) ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens CHF 36'288 pro Jahr (Bundesrecht, Art. 82 BVG / BVV 3; SG übernimmt via Verweis).)** · Bund **CHF 36'288 (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens CHF 36'288 pro Jahr.)**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens, max. CHF 36'288 (Bundesrecht BVV 3; SG verweist auf Art. 82 BVG).)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (alle Einkünfte aus selbständiger und unselbständiger, haupt- und nebenberuflicher Erwerbstätigkeit), max. CHF 36'288.)**
- **Bund:** Art. 33 Abs. 1 Bst. e DBG: Höhe der abzugsfähigen Beiträge durch Bundesrat festgelegt (BVV 3).
- **Bemerkung:** Verweis auf Bundesrecht (Art. 82 BVG / BVV 3); keine SG-eigene Limite.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «13.1 Ordentliche Beiträge Säule 3a Person 1 Bescheinigung 208»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «gebundenen Selbstvorsorge nach Art. 82 BVG»
  - [BVV 3 Art. 7](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7.md) `bund-bvv3__art-7` – «jährlich bis 8 Prozent des oberen Grenzbetrages nach Artikel 8 Absatz 1 BVG, wenn sie einer Vorsorgeeinrichtung nach Artikel 80 BVG angehören»
  - [BSV Masszahlen 25/26 S. 1](../../chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) `bund-bsv-masszahlen-2025-2026__c0003` – «Oberer Grenzbetrag bei Unterstellung unter 2. Säule 7'258 7'258»
  - [BSV Masszahlen 25/26 S. 1](../../chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) `bund-bsv-masszahlen-2025-2026__c0003` – «Oberer Grenzbetrag ohne Unterstellung unter 2. Säule 36'288 36'288»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0048.md) `bund-wl-2a-2026__c0048` – «Es können nur Beiträge abgezogen werden, die im Jahre 2026»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0048.md) `bund-wl-2a-2026__c0048` – «lassen, wenn eine Bescheinigung der Versicherungseinrichtung»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0054.md) `bund-wl-2a-2026__c0054` – «die ein Einkommen aus Erwerbstätigkeit erzielen»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0047.md) `bund-wl-2a-2026__c0047` – «und der AHV-/IV-Pflicht unterliegen»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0047.md) `bund-wl-2a-2026__c0047` – «nur vorübergehendem Unterbruch der Erwerbstätigkeit»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0047.md) `bund-wl-2a-2026__c0047` – «Kein Abzug kommt in Betracht, wenn sich»
  - [MB 21 EDP S. 4](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0012.md) `bund-mb-21edp__c0012` – «sind unter Ziffer 7 des Lohnausweises zu deklarieren»
  - [MB 21 EDP S. 4](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0012.md) `bund-mb-21edp__c0012` – «Die Bescheinigung ist von derjenigen Versicherungseinrichtung oder Bankstiftung zu erstellen»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «wenn keine Beiträge nach Bst. d und e dieser Bestimmung abgezogen werden»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «14. Versicherungsprämien und Sparzinsen Formular 6 600»

<a id="13-1-einkauf-abzug-vorsorge-saeule3a-einkauf"></a>
### Ziff. 13.1 (Einkauf) – Einkaufsbeiträge Säule 3a, Jahr(e) (Code 212 Person 1 / 214 Person 2) – NEU 2026

- **Schlüssel:** `abzug.vorsorge.saeule3a_einkauf` (Einkauf (Nachzahlung) Säule 3a – ab Steuerjahr 2026) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Bescheinigung des Vorsorgeanbieters (Einkauf, Jahr(e) der Lücke)
- **Rein:** 3a-Bescheinigungen der Lückenjahre ab 2025 → max. möglicher minus effektiv einbezahlter Beitrag · 3a-Bescheinigung 2026 → Nachweis voller ordentlicher Beitrag im Einkaufsjahr
- **Rechnen:** je Person: min(Einkauf 2026; Σ Jahresbeitragslücken ab 2025 (max. zehn Jahre zurück); 7'258) – Kanton = Bund
- **Regel:** NEU 2026: Nachträgliche Einkäufe in die Säule 3a für Lücken ab 1.1.2025 (bis 10 Jahre), Abzug höchstens in Höhe des kleinen 3a-Maximalbetrags (Fr. 7'258 im Jahr 2026, Bundesrecht Art. 7a/7b BVV 3); erstmals in der Steuererklärung 2026. Voraussetzungen: AHV-pflichtiges Einkommen, Jahresbeitrag bereits geleistet, noch kein 3a-Kapital bezogen; Bestätigung des Vorsorgeanbieters beilegen. Jahr(e) der Einzahlung angeben.
- **Beachten:** Voraussetzung: AHV-pflichtiges Einkommen, ordentlicher Beitrag 2026 voll geleistet, noch kein 3a-Kapital bezogen
- **Beachten:** Nur Lücken ab 1.1.2025; eine Jahresbeitragslücke nur durch einen einzigen Einkauf
- **Beachten:** Bund: Bezüge ab fünf Jahren vor Referenzalter gelten als Altersleistung (dann kein Einkauf)
- **Limiten:**
  - Säule 3a – Einkauf (Nachzahlung) Regel/Maximum: Kanton **Ab 2025 können fehlende Beiträge bis zu zehn Jahre nachträglich einbezahlt werden. Abzug höchstens kleiner Säule-3a-Maximalbetrag, erstmals mit der Steuererklärung 2026 geltend zu machen. Nur Lücken ab 1.1.2025; Voraussetzungen: AHV-pflichtiges Einkommen, Jahresbeitrag bereits geleistet, noch kein 3a-Kapital bezogen; Bestätigung des Vorsorgeanbieters als Beleg.** · Bund **CHF 7'258 (Einkauf Säule 3a (ab Steuerperiode 2026, für Beitragslücken ab 1.1.2025): zusätzlich zum vollen ordentlichen Beitrag im Einkaufsjahr; max. Summe der Beitragslücken der letzten 10 Jahre (frühestens ab 2025), pro Steuerjahr höchstens CHF 7'258 (8 % des oberen BVG-Grenzbetrags, unabhängig von Zugehörigkeit zur 2. Säule); eine Jahresbeitragslücke nur durch einen einzigen Einkauf ausgleichbar; kein Einkauf nach Bezug einer Altersleistung der Säule 3a (Bezüge ab 5 Jahren vor Referenzalter zählen als Altersleistung).)**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a (kleiner Abzug): Höchstabzug CHF 7'258 pro Jahr für Personen, die einer Vorsorgeeinrichtung der 2. Säule angehören. SG verweist für die abziehbaren Beiträge auf die anerkannten Formen der gebundenen Selbstvorsorge nach Art. 82 BVG; Höchstbetrag nach BVV 3 (identisch mit DBG).)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug CHF 7'258 pro Jahr für Personen, die einer Vorsorgeeinrichtung der 2. Säule angehören (8 % des oberen Grenzbetrags nach Art. 8 Abs. 1 BVG). Nur im Steuerjahr tatsächlich einbezahlte Beiträge, mit Bescheinigung.)**
- **Bemerkung:** Betrag des kleinen 3a-Maximalbetrags aus Bundesquelle (werte/bund 2026: saeule3a.einkauf Fr. 7'258); SG-Quelle nennt keinen Betrag.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «Einkaufsbeiträge Säule 3a Jahr(e) Person 1 Bescheinigung 212»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0010.md) `sg-mb-8-2026__c0010` – «erstmals mit der Steuererklärung 2026 im Kanton St. Gallen geltend gemacht werden kann»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0010.md) `sg-mb-8-2026__c0010` – «gung des Vorsorgeanbieters belegt werden»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0051.md) `bund-wl-2a-2026__c0051` – «in jedem Fall aber maximal 7258 Fr.»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0010.md) `sg-mb-8-2026__c0010` – «ein AHV-pflichtiges Einkommen, der Jahresbeitrag ist bereits geleistet»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0010.md) `sg-mb-8-2026__c0010` – «Abzug höchstens dem kleinen Säule-3a-Maximalbetrag entspricht»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0049.md) `bund-wl-2a-2026__c0049` – «den für sie maximal zulässigen ordentlichen Beitrag»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0050.md) `bund-wl-2a-2026__c0050` – «noch keine Altersleistung aus der Säule 3a bezogen hat,»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0050.md) `bund-wl-2a-2026__c0050` – «chen des Referenzalters erfolgen, als Bezug einer Altersleis-»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0051.md) `bund-wl-2a-2026__c0051` – «frühestens jedoch ab dem 1.1.2025»
  - [MB 21 EDP S. 5](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0014.md) `bund-mb-21edp__c0014` – «Differenz zwischen dem maximal für die steuerpflichtige Person möglichen Säule 3a Beitrag»
  - [MB 21 EDP S. 5](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0014.md) `bund-mb-21edp__c0014` – «In der Ziffer 3 sind Einkäufe in die Säule 3a zu bescheinigen.»
  - [MB 21 EDP S. 5](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0014.md) `bund-mb-21edp__c0014` – «ist für jedes Steuerjahr eine separate Zeile zu erstellen»

<a id="13-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 13.2 – Säule 2 (BVG) inkl. Einkaufsbeiträge (Code 218 Person 1 / 219 Person 2)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Bescheinigung der Vorsorgeeinrichtung (Form. 21 EDP) für selbst entrichtete Einkäufe
- **Rein:** Formular 21 EDP der Vorsorgeeinrichtung → selbst überwiesene Beiträge/Einkäufe 2026 je Person (Code 218/219) · Lohnausweis Ziff. 10.1/10.2 → vom Lohn abgezogene Beiträge/Einkäufe: bereits im Nettolohn (Ziff. 11), nicht hier
- **Rechnen:** Σ 2026 selbst (nicht über den Lohn) bezahlte BVG-Beiträge + Einkäufe gemäss Formular 21 EDP (Kanton = Bund)
- **Regel:** Nur Einkaufsbeiträge/Beiträge, die NICHT bereits vom Lohn abgezogen wurden und im Lohnausweis stehen. Lohnausweis Ziff. 10.2 (vom Lohn abgezogene Einkäufe) ist im Nettolohn (Ziff. 11) bereits berücksichtigt: nicht nochmals abziehen. Vom Arbeitnehmer selbst bezahlte Einkäufe bescheinigt die Vorsorgeeinrichtung separat (Formular 21 EDP).
- **Beachten:** Lohnausweis Ziff. 10.1/10.2 nie nochmals abziehen (Doppelabzug); z.B. Wiedereinkauf nach Scheidung via Formular 21
- **Beachten:** Einkauf erst nach Rückzahlung WEF-Vorbezüge; Leistungen daraus drei Jahre nicht als Kapital beziehbar
- **Beachten:** WEF-Rückzahlung nicht via Formular 21 (WEF-Formular ESTV), nicht hier
- **Bemerkung:** Gesetzliche Grundlage: Art. 45 Abs. 1 Bst. d StG (Einlagen, Prämien und Beiträge an Einrichtungen der beruflichen Vorsorge).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «13.2 Säule 2 (BVG) inkl. Einkaufsbeiträge Person 1 Bescheinigung 218»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «Beiträge für den Einkauf in die berufliche Vorsorge Ziffer 10.2»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «sind nicht durch den Arbeitgeber im Lohnausweis, sondern durch die Vorsorgeeinrichtung separat mit dem Formular 21 EDP zu bescheinigen»
  - [MB 21 EDP S. 2–3](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0006.md) `bund-mb-21edp__c0006` – «Zu diesen Beiträgen gehören beispielsweise Einkäufe oder Wiedereinkäufe infolge Scheidung»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «Ordentliche Beiträge für die berufliche Vorsorge Ziffer 10.1»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «das Total der Abzüge (Ziffer 9 und 10) abgezogen wird»
  - [KS 17 S. 6](../../chunks/bund/dauernd/bund-ks-17/bund-ks-17__c0012.md) `bund-ks-17__c0012` – «erst wieder vorgenommen werden, wenn allfällig früher getätigte Vorbezüge»
  - [KS 17 S. 6](../../chunks/bund/dauernd/bund-ks-17/bund-ks-17__c0012.md) `bund-ks-17__c0012` – «nächsten drei Jahre nicht in Kapitalform aus der Vorsorge zurückgezogen werden»
  - [MB 21 EDP S. 3](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0008.md) `bund-mb-21edp__c0008` – «Die Rückzahlung eines Vorbezugs für Wohneigentum (WEF-Vorbezug)»

<a id="14-abzug-versicherungspraemien"></a>
### Ziff. 14 – Versicherungsprämien und Sparzinsen gemäss Formular 6 (Code 600)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 6 Teil C «Abzug» (niedrigerer Betrag aus tatsächlichen Prämien und Höchstabzug)
- **Rein:** Krankenkasse-Prämienabrechnung 2026 → bezahlte Prämien Grund-/Zusatzversicherung · Policen Lebens-/Renten-/nicht obligatorische Unfallversicherung → bezahlte Prämien · Wertschriftenverzeichnis (Formular 2) → Zinsen von Sparkapitalien · Verfügung Prämienverbilligung → von den Prämien abziehen (Bund)
- **Rechnen:** min(Prämien + Sparzinsen; Max): Ehegatten 6'800 / übrige 3'400, ohne BVG/3a 7'900 / 3'900, +1'100 je Kind; Bund 3'700/1'800, ohne 5'550/2'700, +700
- **Regel:** Prämien für Lebens-, Kranken- und nicht obligatorische Unfallversicherung sowie Sparzinsen bis Fr. 6'800 (gemeinsam steuerpflichtige Ehegatten) bzw. Fr. 3'400 (übrige); Zuschläge: + Fr. 1'100 bzw. + Fr. 500, wenn keine Beiträge nach Art. 45 Abs. 1 Bst. d und e (2. Säule/3a) abgezogen werden; + Fr. 1'100 je Kind mit Kinderabzug. Pauschalabzug: bei unterjähriger Steuerpflicht anteilig (MB 8/2026). AHV-/Vorsorgebeiträge sind separat abziehbar (Art. 45 Abs. 1 Bst. d), ebenso EO-/ALV-Beiträge und obligatorische Unfallversicherung (Bst. f).
- **Beachten:** Kanton: Zuschlag «ohne Vorsorge» nur, wenn keine Beiträge nach Art. 45 Abs. 1 Bst. d und e StG abgezogen
- **Beachten:** Bund: Prämienverbilligung mindert die Prämien; Zuschlag +700 je Kind bzw. unterstützte Person
- **Beachten:** UJ: Maximalbetrag nach Dauer der Steuerpflicht kürzen, für den Satz voll
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 6'800 (Versicherungsprämien (Lebens-, Kranken-, nicht obligatorische Unfallversicherung) und Sparkapitalzinsen: gemeinsam steuerpflichtige Ehegatten bis Fr. 6'800.)** · Bund **CHF 3'700 (Versicherungsprämien und Zinsen von Sparkapitalien, Ehepaare in ungetrennter Ehe, mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 3'700.)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 3'400 (Versicherungsprämien und Sparkapitalzinsen: übrige Steuerpflichtige bis Fr. 3'400.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 1'800.)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 7'900 (Gemeinsam steuerpflichtige Ehegatten ohne Abzug von Beiträgen nach Art. 45 Abs. 1 lit. d und e (2. Säule/3a): Fr. 6'800 + Fr. 1'100 = Fr. 7'900.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an 2. Säule und Säule 3a: Höchstabzug CHF 5'550 (Erhöhung um die Hälfte).)**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 3'900 (Übrige Steuerpflichtige ohne Abzug von Beiträgen nach Art. 45 Abs. 1 lit. d und e (2. Säule/3a): Fr. 3'400 + Fr. 500 = Fr. 3'900.)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: max. CHF 2'700.)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'100 (Erhöhung des Versicherungsabzugs um Fr. 1'100 für jedes Kind, für das ein Kinderabzug geltend gemacht werden kann.)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**
- **Bund:** Art. 33 Abs. 1 Bst. g DBG: Ehepaare Fr. 3'700, übrige Fr. 1'800.
- **Bemerkung:** Formular 6/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «14. Versicherungsprämien und Sparzinsen Formular 6 600»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «bis zum Gesamtbetrag von Fr. 6800.– für gemeinsam steuerpflichtige Ehegatten und von Fr. 3400.– für die übrigen Steuerpflichtigen»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t1.md) `sg-stg-2026__art-45-t1` – «die nach Gesetz, Statut oder Reglement geleisteten Einlagen, Prämien und Beiträge an die Alters-, Hinterlassenen- und Invalidenversicherung»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «die Prämien und Beiträge für die Erwerbsersatzordnung, die Arbeitslosenversicherung und die obligatorische Unfallversicherung»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0052.md) `bund-wl-2a-2026__c0052` – «sowie die im Wertschriftenverzeichnis»
  - [KS 30 S. 12](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0031.md) `bund-ks-30__c0031` – «als aufwandmindernd zu berücksichtigen»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0054.md) `bund-wl-2a-2026__c0054` – «oder jede unterstützungsbedürftige Person, für welche Abzüge»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Ziffer 14 Versicherungsprämien und Sparzinsen»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «der Dauer der Steuerpflicht zu kürzen»

<a id="15-abzug-liegenschaft-unterhalt"></a>
### Ziff. 15 – Unterhalts- und Verwaltungskosten für Liegenschaften gemäss Formular 7 (Code 716)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Formular 7 (Pauschale oder tatsächliche Kosten)
- **Rein:** Formular 7 je Liegenschaft → Bruttomietertrag ohne Nebenkosten / angerechneter Eigenmietwert (Basis Pauschale) · Handwerker-/Unterhaltsrechnungen, STWEG-Abrechnung (Einlage Erneuerungsfonds) → tatsächliche Kosten · Prämien Sach-/Haftpflichtversicherung, Verwaltungsrechnungen Dritter, Grundsteuern/Unterhaltsperimeter → tatsächliche Kosten
- **Rechnen:** je Liegenschaft wählen: Σ tatsächliche Kosten ODER 20% × (Bruttomietertrag ohne NK bzw. angerechneter Eigenmietwert); Bund: 10% (Gebäude bis 10 J.) / 20%
- **Regel:** Wahlrecht je Steuerperiode und Liegenschaft: tatsächliche Kosten (Unterhalt, Instandstellung neu erworbener Grundstücke, Versicherungsprämien, Verwaltung durch Dritte) oder Pauschalabzug 20% des Bruttomietertrags ohne Nebenkosten bzw. des angerechneten Eigenmietwerts (nur vorwiegend Wohnzwecken dienende Liegenschaften). Energiespar-/Umweltinvestitionen und Rückbaukosten gleichgestellt (Vortrag auf 2 Folgeperioden).
- **Beachten:** Pauschale nur bei vorwiegend Wohnzwecken; Bund: nicht für Geschäftsvermögen / von Dritten vorwiegend geschäftlich
- **Beachten:** Nicht abziehbar: Wertvermehrung; Energiespar-/Umweltinvestitionen + Rückbau = Unterhalt, Vortrag zwei Folgeperioden
- **Beachten:** Weisungen StB 044 (Liegenschaftsunterhalt) per 01.01.2026 aktualisiert, u.a. Praxis wirtschaftlicher Neubau abgeschafft
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt bei vorwiegend Wohnzwecken dienenden Liegenschaften: 20 % des Bruttomietertrags ohne Nebenkosten oder des angerechneten Eigenmietwerts, anstelle der tatsächlichen Kosten (Wahl pro Periode und Liegenschaft).)** · Bund **10 % (Pauschalabzug Liegenschaftskosten (anstelle effektiver Kosten, Wahl pro Periode und Liegenschaft): 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist.)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Gleicher Pauschalsatz wie bei jüngeren Gebäuden: 20 % des Bruttomietertrags bzw. angerechneten Eigenmietwerts (keine Altersstaffelung in Art. 29 StV).)** · Bund **20 % (Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist.)**
- **Bemerkung:** Weisungen zum Liegenschaftsunterhalt per 1.1.2026 überarbeitet (sg-stb-aenderungen-2026), Formular 7/2026 nicht publiziert: Pauschalen/Details prüfen.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «15. Unterhalts- und Verwaltungskosten für Liegenschaften Formular 7 716»
  - [StV SG Art. 29](../../chunks/sg/2025/sg-stv/sg-stv__art-29.md) `sg-stv__art-29` – «Pauschalabzug von 20 Prozent des Bruttomietertrags ohne Nebenkosten oder des angerechneten Eigenmietwerts»
  - [StG SG Art. 44](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-44-t2.md) `sg-stg-2026__art-44-t2` – «einen Pauschalabzug geltend machen»
  - [StV SG Art. 29](../../chunks/sg/2025/sg-stv/sg-stv__art-29.md) `sg-stv__art-29` – «für jede Steuerperiode und für jede Liegenschaft zwischen dem Abzug der tatsächlichen Kosten und dem Pauschalabzug wählen»
  - [StV SG Art. 28](../../chunks/sg/2025/sg-stv/sg-stv__art-28.md) `sg-stv__art-28` – «soweit sie nicht wertvermehrende Aufwendungen darstellen»
  - [StV SG Art. 28](../../chunks/sg/2025/sg-stv/sg-stv__art-28.md) `sg-stv__art-28` – «Einlagen in den Reparatur- und Erneuerungsfonds von Stockwerkeigentümergemeinschaften»
  - [StV SG Art. 28](../../chunks/sg/2025/sg-stv/sg-stv__art-28.md) `sg-stv__art-28` – «wie Unterhaltsperimeter und Grundsteuern»
  - [StV SG Art. 28](../../chunks/sg/2025/sg-stv/sg-stv__art-28.md) `sg-stv__art-28` – «Prämien für Sach- und Haftpflichtversicherung für die Liegenschaft»
  - [StG SG Art. 44](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-44-t1.md) `sg-stg-2026__art-44-t1` – «in den zwei nachfolgenden Steuerperioden abziehbar»
  - [StG SG Art. 44](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-44-t1.md) `sg-stg-2026__art-44-t1` – «Den Unterhaltskosten gleichgestellt sind auch die Rückbaukosten im Hinblick auf den Ersatzneubau»
  - [WL 2a 2026 S. 5](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0036.md) `bund-wl-2a-2026__c0036` – «10 % vom Brutto-Mietertrag bzw. Brutto-Mietwert, wenn»
  - [WL 2a 2026 S. 5](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0037.md) `bund-wl-2a-2026__c0037` – «nicht in Betracht für Liegenschaften, die zum Geschäftsvermö»
  - [WL 2a 2026 S. 5](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0038.md) `bund-wl-2a-2026__c0038` – «vorwiegend geschäftlich genutzt werden.»
  - [StB SG Änderungen 2026 S. 1](../../chunks/sg/2026/sg-stb-aenderungen-2026/sg-stb-aenderungen-2026__c0002.md) `sg-stb-aenderungen-2026__c0002` – «Allgemeine Aktualisierung. Abschaffung der Praxis»
  - [StB SG Änderungen 2026 S. 1](../../chunks/sg/2026/sg-stb-aenderungen-2026/sg-stb-aenderungen-2026__c0002.md) `sg-stb-aenderungen-2026__c0002` – «zum wirtschaftlichen Neubau. Präzisierungen zum»

<a id="16-1-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. 16.1 – Verwaltungskosten für Wertschriften und sonstige Kapitalanlagen (Code 220)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.) → Steuerauszug/Depotgebührenausweis; Kurswert des fremdverwalteten Vermögens
- **Rein:** Steuerauszug/Wertschriften- und Guthabenverzeichnis (Spalten A + B) → Bemessungsgrundlage Pauschale · Bankbelege Depotgebühren, Inkassospesen, Kontoführungsgebühren → tatsächliche Kosten (Alternative)
- **Rechnen:** tatsächl. Kosten ODER Pauschale 2‰ × Basis bis 3 Mio. + 1‰ darüber, max. 15'000; Basis = Sp. A+B − Geschäftsvermögen − Darlehen − Selbstverwaltetes/Krypto
- **Regel:** Kosten der Verwaltung durch Dritte abziehbar (nicht Selbstverwaltung, nicht Anlageberatung/Courtagen). Wahl zwischen tatsächlichen Kosten und widerlegbarer Pauschale: 2 Promille bis Fr. 3 Mio. Wertschriftenvermögen, 1 Promille darüber, max. Fr. 15'000; Bemessungsgrundlage ohne Geschäftsvermögen, Darlehen, selbstverwaltete Titel und Kryptowährungen. Pauschalabzug bei unterjähriger Steuerpflicht anteilig (MB 8/2026).
- **Beachten:** Pauschale und tatsächliche Kosten pro Periode nicht kumulierbar; Selbstverwaltung → kein Abzug
- **Beachten:** Nicht abziehbar: Transaktionskosten, Beratung, aktives Depotmanagement; All-in-Fee je Depot schätzen (ohne 15'000)
- **Beachten:** Bund: gleiche Abzugsregeln wie Kanton; UJ: Pauschale nach Dauer kürzen
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.1 Verwaltungskosten für Wertschriften und sonstige Kapitalanlagen 220»
  - [StG SG Art. 44](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-44-t1.md) `sg-stg-2026__art-44-t1` – «können die Kosten der Verwaltung durch Dritte»
  - [StB 44 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0006.md) `sg-stb-44-1__c0006` – «Die Pauschale beträgt 2 Promille bis zu einem Wertschriftenvermögen von Fr. 3 Mio.»
  - [StB 44 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0006.md) `sg-stb-44-1__c0006` – «Sie ist auf maximal Fr. 15'000.-- begrenzt»
  - [StB 44 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0006.md) `sg-stb-44-1__c0006` – «(Spalten A + B) nach Abzug des Geschäftsvermögens, der Darlehen sowie der selbstverwalteten Wertschriften»
  - [StB 44 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0005.md) `sg-stb-44-1__c0005` – «Eine Kumulation von Pauschalabzug und dem Abzug von»
  - [StB 44 Nr. 1 S. 1–2](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0004.md) `sg-stb-44-1__c0004` – «Kein Abzug kann gewährt werden, wenn die steuerpflichtige Person ihr bewegliches»
  - [StB 44 Nr. 1 S. 1](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0001.md) `sg-stb-44-1__c0001` – «Auslagen und Kosten, die mit dem Erwerb, der Erhaltung, Umschichtung, Mehrung oder dem Verkauf von Vermögenswerten verbunden sind»
  - [StB 44 Nr. 1 S. 6–7](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0016.md) `sg-stb-44-1__c0016` – «Depotgebühren Die Kosten für die Aufbewahrung Ja»
  - [StB 44 Nr. 1 S. 6–7](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0016.md) `sg-stb-44-1__c0016` – «Inkassospesen Die Kosten für die Einforderung Ja»
  - [StB 44 Nr. 1 S. 6–7](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0016.md) `sg-stb-44-1__c0016` – «Kontoführungsge- Die Kosten für die Kontoführung Ja»
  - [StB 44 Nr. 1 S. 4](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0012.md) `sg-stb-44-1__c0012` – «Beratungskosten Die Kosten der Finanz-, Anlage-, Nein»
  - [StB 44 Nr. 1 S. 5–6](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0013.md) `sg-stb-44-1__c0013` – «Vermögensverwal- Die Kosten für die laufende Nein»
  - [StB 44 Nr. 1 S. 2–3](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0009.md) `sg-stb-44-1__c0009` – «die Abzugsbeschränkung von Fr. 15'000.-- greift nicht»
  - [StB 44 Nr. 1 S. 3–4](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0010.md) `sg-stb-44-1__c0010` – «Es gelten daher die gleichen Abzugsregeln wie im kantonalen Recht»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Ziffer 16.1 Verwaltungskosten für Wertschriften und sonstige Kapitalanlagen»

<a id="16-2-abzug-drittbetreuung"></a>
### Ziff. 16.2 – Kinderbetreuungskosten bei Drittbetreuung gemäss Formular 10 (Code 258)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Formular 10: Rechnungen Kita/Tagesmutter, Name/Geburtsdatum Kind
- **Rein:** Rechnungen Kita/Tagesfamilie/Hort 2026 → bezahlte Betreuungskosten je Kind (Formular 10) · Formular 10 → Name, Geburtsdatum Kind; Nachweis Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit
- **Rechnen:** Σ je Kind < 14 J. im gleichen Haushalt: min(nachgewiesene Drittbetreuungskosten; 26'800 / Bund 25'800)
- **Regel:** Betreuungskosten für Kinder unter 14 Jahren durch Drittpersonen, höchstens Fr. 26'800 je Kind (2026, bisher Fr. 26'700), wenn das Kind im gleichen Haushalt lebt und die Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit stehen. Pauschalabzug bei unterjähriger Steuerpflicht anteilig (MB 8/2026).
- **Beachten:** Nur bei direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit des Steuerpflichtigen
- **Beachten:** Bund: nicht abziehbar Betreuung ausserhalb Arbeits-/Ausbildungszeit sowie Verpflegung/Unterkunft der Kinder
- **Beachten:** Kanton neu max. 26'800 je Kind; UJ: Maximum nach Dauer kürzen, für den Satz voll
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 26'800 (Kinderdrittbetreuungskosten: höchstens Fr. 26'800 je Kind unter 14 Jahren, das im gleichen Haushalt lebt, soweit in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind, höchstens CHF 25'800; Kind unter 14 Jahren im gleichen Haushalt; Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 (Kinder unter 14 Jahren.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat.)**
- **Bemerkung:** Formular 10/2026 nicht publiziert. Bund: Kinderdrittbetreuung nicht aus 2026-Quelle geprüft.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.2 Kinderbetreuungskosten bei Drittbetreuung Formular 10 258»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t3.md) `sg-stg-2026__art-45-t3` – «höchstens Fr. 26 800.– für jedes Kind»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0011.md) `sg-mb-8-2026__c0011` – «Kinderbetreuung Abzug pro Kind»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0011.md) `sg-mb-8-2026__c0011` – «Kinderbetreuung Abzug pro Kind neu max. Fr.»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Ziffer 16.2 Kinderbetreuungskosten»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0058.md) `bund-wl-2a-2026__c0058` – «25 800 Fr., für die Drittbetreuung jedes Kindes (bis 14 Jahre),»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0059.md) `bund-wl-2a-2026__c0059` – «betreuungskosten ausserhalb der Arbeits- oder Ausbildungszeit»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0059.md) `bund-wl-2a-2026__c0059` – «Gleiches gilt für die Kosten für Verpflegung und Unterkunft der»

<a id="16-3-abzug-parteispenden"></a>
### Ziff. 16.3 – Parteispenden gemäss Formular 5 (Code 555)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ⚠️ strittig
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Formular 5 Teil B: Bestätigung der Partei (Datum, Partei, Betrag)
- **Rein:** Bestätigung/Beitragsrechnung der Partei → Mitgliederbeiträge und Zuwendungen (Formular 5 Teil B: Datum, Partei, Betrag)
- **Rechnen:** min(Σ Mitgliederbeiträge + Zuwendungen an Parteien; Ehegatten 21'400 / übrige 10'700); Bund: min(…; 10'600)
- **Regel:** Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister, im kantonalen Parlament vertreten oder mind. 3% Stimmen) bis Fr. 21'400 (gemeinsam steuerpflichtige Ehegatten) bzw. Fr. 10'700 (übrige) laut StG-Jahresversion 2026. ACHTUNG: MB 8/2026 Ziff. 11 nennt unter 16.3 einen «Höheren Abzug Parteispenden», der Betrag fehlt im Quelltext.
- **Beachten:** Partei: im Parteienregister, in einem kantonalen Parlament vertreten oder ≥ 3% Stimmen bei letzten Wahlen
- **Beachten:** STRITTIG: Merkblatt UJ 2026 nennt unter 16.3 «Höherer Abzug» ohne Betrag → Fachperson prüft Original-PDF
- **Beachten:** Bund: Gesamtbetrag 10'600 (keine separate Ehepaar-Limite genannt); Belege beifügen
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'700 (Mitgliederbeiträge und Zuwendungen an politische Parteien: bis Fr. 10'700 für übrige (alleinstehende) Steuerpflichtige.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister / kantonales Parlament / mind. 3 % Stimmen): bis Gesamtbetrag CHF 10'600.)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 21'400 (Parteispenden: bis Fr. 21'400 für gemeinsam steuerpflichtige Ehegatten.)** · Bund **–**
- **Bund:** Art. 33 Abs. 1 Bst. i DBG: Gesamtbetrag 10 600 Franken.
- **Bemerkung:** Strittig/unklar: StG SG Jahresversion 2026 nennt Fr. 10'700/21'400 (identisch zur Version 2025), MB 8/2026 kündigt «höheren Abzug» an, ohne Betrag (auch im PDF S. 4 fehlt er). Fachperson prüft Original raw/sg/2026/sg-mb-8-2026.pdf bzw. Gesetzessammlung.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.3 Parteispenden Formular 5 555»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t3.md) `sg-stg-2026__art-45-t3` – «bis zum Gesamtbetrag von Fr. 21 400.– für gemeinsam steuerpflichtige Ehegatten und von Fr. 10 700.– für die übrigen Steuerpflichtigen»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0011.md) `sg-mb-8-2026__c0011` – «16.3 Höherer Abzug»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0057.md) `bund-wl-2a-2026__c0057` – «können bis zum Gesamtbetrag von 10 600 Fr. abgezogen wer-»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0057.md) `bund-wl-2a-2026__c0057` – «Die Belege sind beizufügen.»

<a id="16-4-abzug-weiterbildung"></a>
### Ziff. 16.4 – Kosten berufsorientierte Aus-/Weiterbildung (Code 223 Person 1 / 224 Person 2)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Aufstellung mit Rechnungsdatum, Bezeichnung, Betrag; Kursrechnungen
- **Rein:** Kursrechnungen/Zahlungsbelege 2026 → selbst bezahlte Kosten je Person (Aufstellung: Rechnungsdatum, Bezeichnung, Betrag; Code 223/224) · Lohnausweis/Bestätigung Arbeitgeber → vom Arbeitgeber getragene oder rückvergütete Kosten (nicht abziehbar)
- **Rechnen:** je Person min(selbst getragene berufsorientierte Aus-/Weiterbildungs- inkl. Umschulungskosten; 13'000) – Kanton = Bund
- **Regel:** Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis Fr. 13'000 je Steuerpflichtigen (Voraussetzung: erster Abschluss Sek. II oder vollendetes 20. Altersjahr und nicht Ausbildung bis zum ersten Abschluss Sek. II). Vom Arbeitgeber getragene Kosten der berufsorientierten Aus- und Weiterbildung (inkl. Umschulung) sind kein geldwerter Vorteil (Art. 30 Abs. 1bis StG).
- **Beachten:** Voraussetzung: erster Abschluss Sek. II oder 20. Lebensjahr vollendet (nicht Kosten bis zum ersten Sek-II-Abschluss)
- **Beachten:** Vom AG getragene Kosten: kein Lohn (Art. 30 Abs. 1bis StG); Bund: Abzug bei Zahlung, spätere AG-Vergütung = Einkommen
- **Beachten:** Ausbildungskosten der Kinder nicht hier (→ Ziff. 23.3)
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung: max. Fr. 13'000 je Steuerpflichtigen, wenn erster Abschluss Sekundarstufe II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildungs- inkl. Umschulungskosten bis CHF 13'000 pro Jahr, sofern erster Abschluss Sek. II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)**
- **Bund:** Art. 33 Abs. 1 Bst. j DBG (Weiterbildung, Maximum Bund nicht aus 2026-Quelle geprüft).
- **Bemerkung:** Seed «ohne Nachweis 400» für 2026 nicht bestätigt (offen).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «Kosten berufsorientierte Aus-/Weiterbildung Person 2 Aufstellung 224»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t4.md) `sg-stg-2026__art-45-t4` – «bis zum Gesamtbetrag von Fr. 13 000.– je Steuerpflichtigen»
  - [StG SG Art. 30](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-30.md) `sg-stg-2026__art-30` – «Die vom Arbeitgeber getragenen Kosten der berufsorientierten Aus- und Weiterbildung, einschliesslich Umschulungskosten,»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0055.md) `bund-wl-2a-2026__c0055` – «Abziehbar sind die selbstgetragenen Kosten der»
  - [KS 42 S. 10–11](../../chunks/bund/dauernd/bund-ks-42/bund-ks-42__c0027.md) `bund-ks-42__c0027` – «Weiterbildungskosten im Zeitpunkt der Zahlung geltend machen»
  - [KS 42 S. 10–11](../../chunks/bund/dauernd/bund-ks-42/bund-ks-42__c0027.md) `bund-ks-42__c0027` – «im Jahr der Rückvergütung als steuerbares Einkommen»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «23.3 Ausbildungskosten für Kinder in Schule oder Ausbildung Formular 10 256»

<a id="16-5-abzug-ahv-nichterwerbstaetige"></a>
### Ziff. 16.5 – Übrige Abzüge (Code 222), z.B. AHV-Beiträge Nichterwerbstätiger

- **Schlüssel:** `abzug.ahv_nichterwerbstaetige` (AHV/IV/EO-Beiträge Nichterwerbstätiger u.ä.) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse) → AHV-Beitragsverfügung für Nichterwerbstätige
- **Rein:** AHV-Beitragsverfügung/-rechnung Nichterwerbstätige (Ausgleichskasse) → AHV/IV/EO-Beiträge · Belege weiterer übriger Abzüge → Aufstellung mit Art (Feld «Arten»)
- **Rechnen:** Σ AHV/IV/EO-Beiträge als Nichterwerbstätige + weitere übrige Abzüge (je mit Art) – Kanton = Bund
- **Regel:** Beiträge an die AHV/IV (z.B. als Nichterwerbstätiger) sind nach Gesetz abziehbar; Art der Abzüge angeben.
- **Beachten:** Art der Abzüge im Feld «Arten» angeben
- **Beachten:** Bund: Arbeitgeberbeiträge für privates Dienstpersonal nicht abziehbar
- **Beachten:** Grundlage Kanton: Art. 45 Abs. 1 Bst. d (AHV/IV) bzw. Bst. f (EO/ALV) StG
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.5 Übrige Abzüge Arten 222»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t1.md) `sg-stg-2026__art-45-t1` – «Einlagen, Prämien und Beiträge an die Alters-, Hinterlassenen- und Invalidenversicherung und an Einrichtungen der beruflichen Vorsorge»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «AHV-Beiträge von Nichterwerbstätigen, u.a.»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0055.md) `bund-wl-2a-2026__c0055` – «Beiträge Nichterwerbstätiger an die AHV, IV und EO.»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0055.md) `bund-wl-2a-2026__c0055` – «Nicht zulässig ist der Abzug von Arbeitgeberbeiträgen für das»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «die Prämien und Beiträge für die Erwerbsersatzordnung, die Arbeitslosenversicherung»

<a id="17-abzug-zweiverdiener"></a>
### Ziff. 17 – Zweiverdienerabzug (Code 226)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Beilage (beide Ehegatten erwerbstätig)
- **Rein:** Lohnausweise/Jahresrechnungen beider Ehegatten → Erwerbseinkommen je Ehegatte (Bund: niedrigeres massgebend) · Taggeldabrechnungen (ALV, Kranken-, Unfallversicherung) → Bund: dem Erwerbseinkommen gleichgestellt
- **Rechnen:** Kanton: fix 500; Bund: min(max(50% × niedrigeres Erwerbseinkommen; 8'600); 14'100), höchstens das niedrigere Erwerbseinkommen
- **Regel:** Gemeinsam steuerpflichtige Ehegatten: Fr. 500 vom Erwerbseinkommen, das ein Ehegatte unabhängig vom Betrieb des anderen erzielt; gleicher Abzug bei erheblicher Mitarbeit im Betrieb des anderen Ehegatten. Pauschalabzug bei unterjähriger Steuerpflicht anteilig (MB 8/2026).
- **Beachten:** Nur gemeinsam Steuerpflichtige; auch bei erheblicher Mitarbeit beim andern (Bund: vertraglich vorgesehen/erforderlich)
- **Beachten:** Bund-Erwerbseinkommen = Bruttolohn − Berufskosten − AHV/IV/EO/ALV/NBUV − Säule 2/3a; Verlust → kein Abzug
- **Beachten:** UJ: Abzug nach Dauer der Steuerpflicht kürzen, für den Satz voll
- **Limiten:**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **n/a – Art. 45 Abs. 2 StG SG kennt nur einen Fixbetrag.** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (Ehepaare in ungetrennter Ehe, beide erwerbstätig).)**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **n/a – Fixbetrag Fr. 500 siehe zweiverdiener.max.** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum.)**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **CHF 500 (Gemeinsam steuerpflichtige Ehegatten: Abzug von Fr. 500 vom Erwerbseinkommen, das ein Ehegatte unabhängig vom Beruf/Geschäft des andern erzielt; gleicher Abzug bei erheblicher Mitarbeit im Beruf/Geschäft des andern Ehegatten.)** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum.)**
- **Bund:** Art. 33 Abs. 2 DBG: 50% des niedrigeren Erwerbseinkommens, mindestens 8 600, höchstens 14 100 Franken.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «17. Zweiverdienerabzug 226»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t4.md) `sg-stg-2026__art-45-t4` – «Fr. 500.– abgezogen»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0062.md) `bund-wl-2a-2026__c0062` – «kommen können 50 Prozent, mindestens 8600 Fr. und»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0062.md) `bund-wl-2a-2026__c0062` – «Bruttolohn abzüglich der Berufskosten sowie der Beiträge an die»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0056.md) `bund-wl-2a-2026__c0056` – «ALV/NBUV und an die Säulen 2 und 3a gekürzte niedrigere»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0056.md) `bund-wl-2a-2026__c0056` – «kann nur dieser tiefere Betrag abgezogen werden»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0056.md) `bund-wl-2a-2026__c0056` – «kommt in Betracht, wenn sich aus der Erwerbstätigkeit ein»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0055.md) `bund-wl-2a-2026__c0055` – «Dem Erwerbseinkommen gleichgestellt sind»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0057.md) `bund-wl-2a-2026__c0057` – «sofern die Mitarbeit vertraglich vorgesehen oder durch»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Ziffer 17 Zweiverdienerabzug»

<a id="18-berechnung-total"></a>
### Ziff. 18 – Total der Abzüge (Code 230)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 10.1–17 (Seite 3, Codes 438 bis 226)
- **Rechnen:** Σ Ziff. 10.1 bis 17 (Berufskosten, Schuldzinsen, Unterhalt, Vorsorge, Versicherungen, Liegenschaften, weitere Abzüge, Zweiverdiener)
- **Regel:** Rechenzeile Total der Abzüge (Ziff. 18, Code 230); welche Ziffern in die Summe eingehen, ist in den vorliegenden Quellen nicht belegt – am Formular prüfen.
- **Beachten:** Bund weicht ab bei Ziff. 10, 14, 15 (Pauschale 10%), 16.2, 16.3 und 17 (andere Beträge)
- **Beachten:** Übertrag in Ziff. 20: Nettoeinkommen = Ziff. 7 − Ziff. 18
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt bei vorwiegend Wohnzwecken dienenden Liegenschaften: 20 % des Bruttomietertrags ohne Nebenkosten oder des angerechneten Eigenmietwerts, anstelle der tatsächlichen Kosten (Wahl pro Periode und Liegenschaft).)** · Bund **10 % (Pauschalabzug Liegenschaftskosten (anstelle effektiver Kosten, Wahl pro Periode und Liegenschaft): 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist.)**
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «18. Total der Abzüge 230»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «10.1 Person 1 Formular 4 438»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «17. Zweiverdienerabzug 226»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «20. Nettoeinkommen (Ziffer 7 abzüglich Ziffer 18) 234»

## Einkommensberechnung

<a id="20-berechnung-total"></a>
### Ziff. 20 – Nettoeinkommen (Code 234)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile: Ziffer 7 abzüglich Ziffer 18
- **Rein:** Übertrag Ziff. 7 (Total der Einkünfte, Code 168) · Übertrag Ziff. 18 (Total der Abzüge, Code 230)
- **Rechnen:** Ziff. 7 − Ziff. 18 (Code 168 − Code 230)
- **Regel:** Ziff. 7 abzüglich Ziff. 18; Basis für Selbstbehalt Krankheitskosten (2%) und Zuwendungs-Limite (20%).
- **Beachten:** Basis für Selbstbehalt Ziff. 21.1 (Kanton 2% / Bund 5%) und Zuwendungslimite Ziff. 21.3 (20%)
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **2 % (Krankheits- und Unfallkosten sind abziehbar, soweit selbst getragen und über 2 % der Nettoeinkünfte. Behinderungsbedingte Kosten: ohne Selbstbehalt (lit. abis).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: insgesamt höchstens 20 % der Nettoeinkünfte.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «20. Nettoeinkommen (Ziffer 7 abzüglich Ziffer 18) 234»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Total der Einkünfte 168»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «18. Total der Abzüge 230»

<a id="21-1-abzug-krankheitskosten"></a>
### Ziff. 21.1 – Krankheits- und Unfallkosten gemäss Formular 6 (Code 650), abzüglich Selbstbehalt 2% (Code 238), Abzug (Code 240)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 6 Rückseite: selbst getragene Kosten (Rechnungen abzüglich Kassenleistungen)
- **Rein:** Arzt-/Zahnarzt-/Spital-/Apothekenrechnungen 2026 → Kosten (Formular 6 Rückseite, Brutto-Total Code 650) · Leistungsabrechnung Krankenkasse/Unfall-/Haftpflichtversicherung → Leistungen Dritter abziehen · Übertrag Ziff. 20 → Basis Selbstbehalt (Code 238)
- **Rechnen:** Abzug (Code 240) = Σ selbst getragene Kosten (nach Versicherungs-/Drittleistungen) − 2% × Ziff. 20 (Code 238), nicht negativ; Bund: Selbstbehalt 5%
- **Regel:** Selbst getragene Krankheits- und Unfallkosten (des Steuerpflichtigen und der von ihm unterhaltenen Personen), soweit sie 2% des Nettoeinkommens (Ziff. 20) übersteigen; Brutto-Total in Code 650, Selbstbehalt in Code 238, Differenz in Code 240.
- **Beachten:** Nur selbst getragene Kosten (nach Versicherungsleistungen); auch für die unterhaltenen Personen
- **Beachten:** Bund nicht abziehbar: KK-Prämien (→ Ziff. 14), Prävention (z.B. Fitness), Schönheitsbehandlungen; Behinderung → 21.2
- **Beachten:** Bund: lebensnotwendige Diät pauschal 2'500 statt effektiv (Diabetes nur effektive Mehrkosten)
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **2 % (Krankheits- und Unfallkosten sind abziehbar, soweit selbst getragen und über 2 % der Nettoeinkünfte. Behinderungsbedingte Kosten: ohne Selbstbehalt (lit. abis).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
- **Bund:** Art. 33 Abs. 1 Bst. h DBG: Selbstbehalt 5% der um die Aufwendungen verminderten Einkünfte.
- **Bemerkung:** Formular 6/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «21.1 Krankheits- und Unfallkosten Formular 6 650»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «abzüglich Selbstbehalt 2% des Nettoeinkommens (Ziffer 20)»
  - [StG SG Art. 46](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-46.md) `sg-stg-2026__art-46` – «soweit der Steuerpflichtige die Kosten selbst trägt und diese 2 Prozent der Nettoeinkünfte übersteigen»
  - [KS 11 S. 10–11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0026.md) `bund-ks-11__c0026` – «Abzugsfähig sind nur diejenigen Kosten, die vom Steuerpflichtigen selbst getragen werden.»
  - [KS 11 S. 10–11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0026.md) `bund-ks-11__c0026` – «Haftpflicht- und private Unfallversicherung»
  - [KS 11 S. 4](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0004.md) `bund-ks-11__c0004` – «Keine Krankheitskosten stellen weiter die Krankenkassenprämien dar.»
  - [KS 11 S. 4](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0004.md) `bund-ks-11__c0004` – «der Prävention dienen (z.B. Abonnement für Fitness-Center)»
  - [KS 11 S. 5–6](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0009.md) `bund-ks-11__c0009` – «eine Pauschale von CHF 2'500.-- geltend gemacht werden»
  - [KS 11 S. 5–6](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0009.md) `bund-ks-11__c0009` – «können jedoch nur die effektiven Mehrkosten zum Abzug bringen»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0058.md) `bund-wl-2a-2026__c0058` – «Die Auslagen sind in einer separaten Aufstellung aufzulisten»

<a id="21-2-abzug-behinderungskosten"></a>
### Ziff. 21.2 – Behinderungsbedingte Kosten, ohne Selbstbehalt gemäss Formular 6 (Code 235)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Formular 6 Rückseite: behinderungsbedingte Kosten; Verfügung Hilflosenentschädigung
- **Rein:** Rechnungen Assistenz/Heimaufenthalt/Hilfsmittel/Pflegeartikel 2026 → selbst getragene behinderungsbedingte Kosten (Formular 6, Code 235) · Verfügung Hilflosenentschädigung (HE) → anrechnen bzw. Grundlage Pauschale (Bund)
- **Rechnen:** Σ selbst getragene behinderungsbedingte Kosten (nach Drittleistungen, z.B. HE), ohne Selbstbehalt; Bund alternativ Pauschale HE 2'500/5'000/7'500
- **Regel:** Selbst getragene behinderungsbedingte Kosten von Personen mit Behinderung im Sinn des BehiG, ohne Selbstbehalt.
- **Beachten:** Nur Personen mit Behinderung im Sinn des BehiG (Steuerpflichtige oder unterhaltene Personen)
- **Beachten:** Verbeiständete Behinderte: Beistandsentschädigung pauschal 60% Verwaltungskosten / 40% behinderungsbedingt
- **Beachten:** Bund: Pauschale 2'500 auch ohne HE für Gehörlose und Dialysepatienten; Belege beifügen
- **Bund:** Art. 33 Abs. 1 Bst. hbis DBG: ebenfalls ohne Selbstbehalt.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «21.2 Behinderungsbedingte Kosten (ohne Selbstbehalt) Formular 6 235»
  - [StG SG Art. 46](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-46.md) `sg-stg-2026__art-46` – «die behinderungsbedingten Kosten des Steuerpflichtigen oder der von ihm unterhaltenen Personen»
  - [KS 11 S. 10](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0025.md) `bund-ks-11__c0025` – «Bezüger einer Hilflosenentschädigung leichten Grades: CHF 2'500.--»
  - [KS 11 S. 10](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0025.md) `bund-ks-11__c0025` – «Bezüger einer Hilflosenentschädigung mittleren Grades: CHF 5'000.--»
  - [KS 11 S. 10](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0025.md) `bund-ks-11__c0025` – «Bezüger einer Hilflosenentschädigung schweren Grades: CHF 7'500.--»
  - [KS 11 S. 10](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0025.md) `bund-ks-11__c0025` – «Nierenkranke, die sich einer Dialyse unterziehen müssen»
  - [KS 11 S. 10–11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0026.md) `bund-ks-11__c0026` – «sind bei diesen Kosten anzurechnen»
  - [KS 11 S. 8](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0017.md) `bund-ks-11__c0017` – «Kosten für Heim- und Entlastungsaufenthalte»
  - [KS 11 S. 9](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0022.md) `bund-ks-11__c0022` – «Anschaffungs- oder Mietauslagen für Hilfsmittel»
  - [StB 44 Nr. 1 S. 1–2](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0004.md) `sg-stb-44-1__c0004` – «pauschal 60% der Entschädigung gemäss Art. 404 ZGB als Vermögensverwaltungskosten und 40% als behinderungsbedingte Kosten»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0058.md) `bund-wl-2a-2026__c0058` – «selber trägt. Die Belege sind beizufügen.»

<a id="21-3-abzug-spenden"></a>
### Ziff. 21.3 – Freiwillige Zuwendungen gemäss Formular 5 (Code 244)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Formular 5 Rückseite Teil A: Spendenbestätigungen (Datum, Institution, Betrag)
- **Rein:** Spendenbestätigungen → Σ Zuwendungen (Formular 5 Rückseite Teil A: Datum, Institution, Betrag) · Übertrag Ziff. 20 → Basis 20%-Limite
- **Rechnen:** wenn Σ Zuwendungen im Steuerjahr ≥ 100: min(Σ; 20% × Ziff. 20) – Kanton = Bund
- **Regel:** Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentlicher/gemeinnütziger Zweck) sowie an Bund, Kantone, Gemeinden: wenn im Steuerjahr mind. Fr. 100 erreicht, insgesamt höchstens 20% des Nettoeinkommens (Ziff. 20).
- **Beachten:** Nur an steuerbefreite jur. Personen mit Sitz CH (öffentlich/gemeinnützig) sowie Bund, Kantone, Gemeinden, Anstalten
- **Beachten:** Parteispenden nicht hier (→ Ziff. 16.3)
- **Beachten:** Bund: Aufstellung über die geleisteten Zuwendungen beifügen
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn sie im Steuerjahr Fr. 100 erreichen.)** · Bund **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn im Steuerjahr mindestens CHF 100 erreicht.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: insgesamt höchstens 20 % der Nettoeinkünfte.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**
- **Bund:** Art. 33a DBG: ab 100 Franken, max. 20% der um die Aufwendungen verminderten Einkünfte.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «21.3 Freiwillige Zuwendungen (wenn mind. Fr.100, max. 20% Ziffer 20) Formular 5 244»
  - [StG SG Art. 46](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-46.md) `sg-stg-2026__art-46` – «höchstens 20 Prozent der Nettoeinkünfte»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0060.md) `bund-wl-2a-2026__c0060` – «Der Steuererklärung ist eine Aufstellung über die geleisteten»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.3 Parteispenden Formular 5 555»

<a id="22-berechnung-total"></a>
### Ziff. 22 – Reineinkommen (Code 248)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 20 (Nettoeinkommen, Code 234) · Übertrag Ziff. 21.1 (Abzug Code 240), 21.2 (Code 235), 21.3 (Code 244)
- **Rechnen:** Ziff. 20 − Ziff. 21.1 (Code 240) − Ziff. 21.2 − Ziff. 21.3 = Code 248
- **Regel:** Ziff. 20 abzüglich Ziff. 21.1 bis 21.3.
- **Beachten:** Weiter: Ziff. 24 = Ziff. 22 − Sozialabzüge Ziff. 23.1 bis 23.3; Ziff. 23.4 (unterstützte Personen) nur Bund
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «22. Reineinkommen (Ziffer 20 abzüglich Ziffern 21.1 bis 21.3) 248»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «24. Steuerbares Einkommen gesamt (Ziffer 22 abzüglich Ziffern 23.1-23.3) 268»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «Abzug gilt nur für die direkte Bundessteuer»

<a id="23-1-sozialabzug-kinder"></a>
### Ziff. 23.1 – Kinderabzug für jedes noch nicht schulpflichtige Kind (Fr. 7'600, Code 252)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien Seite 1 (Kinder, für deren Unterhalt zur Hauptsache aufgekommen wird)
- **Rein:** Seite 1 Kinderangaben (Name, Geburtsdatum, «Im Vorschulalter») → Anzahl noch nicht schulpflichtiger Kinder
- **Rechnen:** Anzahl noch nicht schulpflichtiger Kinder unter Sorge/Obhut × 7'600; UJ: 7'600 ÷ 360 × Tage; Bund: 6'800 je Kind + 263 vom Steuerbetrag
- **Regel:** Fr. 7'600 je Kind unter elterlicher Sorge/Obhut, noch nicht schulpflichtig, wenn der Steuerpflichtige zur Hauptsache für den Unterhalt aufkommt und keinen Abzug für Unterhaltsbeiträge (Ziff. 12.2) beansprucht. Stichtag 31.12.2026 bzw. Ende der Steuerpflicht; bei unterjähriger Steuerpflicht anteilig (360-Tage-Methode, MB 8/2026), für den Satz voll.
- **Beachten:** Nur bei Unterhalt zur Hauptsache und ohne Abzug Unterhaltsbeiträge (Art. 45 Abs. 1 Bst. c) für dieses Kind
- **Beachten:** Stichtag 31. Dezember 2026 bzw. Ende Steuerpflicht; Kinder = leibliche, Adoptiv-, Stief-, Pflegekinder
- **Beachten:** Bund: getrennte Eltern mit gemeinsamer Sorge ohne Unterhaltsabzug → je halber Abzug
- **Limiten:**
  - Kinderabzug Vorschulalter (CHF): Kanton **CHF 7'600 (Kinderabzug Fr. 7'600 für jedes unter der elterlichen Sorge oder Obhut stehende Kind, das noch nicht schulpflichtig ist.)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (Art. 35 Abs. 1 lit. a DBG), keine Staffelung nach Alter; siehe sozialabzug.kind.**
  - Kinderabzug Grundbetrag (CHF): Kanton **n/a – Art. 48 Abs. 1 lit. a StG SG. Voraussetzung: Steuerpflichtiger kommt zur Hauptsache für den Unterhalt auf und beansprucht keinen Abzug für Unterhaltsbeiträge (Art. 45 Abs. 1 lit. c).** · Bund **CHF 6'800 (Kinderabzug CHF 6'800 pro minderjähriges oder in beruflicher/schulischer Ausbildung stehendes Kind, für dessen Unterhalt die steuerpflichtige Person sorgt; bei getrennter Besteuerung der Eltern hälftig bei gemeinsamer elterlicher Sorge ohne Unterhaltsbeiträge.)**
  - Abzug vom Steuerbetrag pro Kind (CHF, Bund): Kanton **n/a – Siehe data/werte/bund.** · Bund **CHF 263 (Ermässigung des Steuerbetrags um CHF 263 pro Kind oder unterstützungsbedürftige Person (Ehepaare sowie Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern/unterstützungsbedürftigen Personen im gleichen Haushalt, die deren Unterhalt zur Hauptsache bestreiten).)**
- **Bund:** Art. 35 Abs. 1 Bst. a DBG: 6 800 Franken je Kind (minderjährig oder in Ausbildung).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «23.1 Kinderabzug für jedes noch nicht schulpflichtige Kind Fr. 7’600 252»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «Fr. 7600.– für jedes unter der elterlichen Sorge oder Obhut des Steuerpflichtigen stehende Kind»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Kinderabzug für ganzes Kalenderjahr (satzbestimmend)»
  - [Formular 1 SG 2026 UJ S. 1](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0002.md) `sg-form-1-2026-uj__c0002` – «Kinder, für deren Unterhalt Sie zur Hauptsache aufkommen»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «wenn der Steuerpflichtige für den Unterhalt zur Hauptsache aufkommt»
  - [StV SG Art. 30](../../chunks/sg/2025/sg-stv/sg-stv__art-30.md) `sg-stv__art-30` – «Als Kinder gelten die leiblichen Kinder sowie die Adoptiv-, Stief- und Pflegekinder.»
  - [KS 30 S. 20](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0061.md) `bund-ks-30__c0061` – «Bei getrennt lebenden Eltern mit gemeinsamer elterlicher Sorge kann jeder Elternteil den halben Abzug beanspruchen»

<a id="23-2-sozialabzug-kinder"></a>
### Ziff. 23.2 – Kinderabzug für jedes Kind in Schule oder Ausbildung (Fr. 10'800, Code 254)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien Seite 1 (Schule/Ausbildung, Dauer bis)
- **Rein:** Seite 1 Kinderangaben → Kinder in Schule/Ausbildung; bei beruflicher Ausbildung Schule/Lehrfirma und «Dauer bis»
- **Rechnen:** Anzahl Kinder (unter Sorge/Obhut oder volljährig) in schulischer/beruflicher Ausbildung × 10'800; UJ ÷ 360 × Tage; Bund: 6'800 je Kind + 263 vom Steuerbetrag
- **Regel:** Fr. 10'800 je minderjähriges oder volljähriges Kind in schulischer/beruflicher Ausbildung (Unterhalt zur Hauptsache, kein Abzug nach Art. 45 Abs. 1 Bst. c). Bei unterjähriger Steuerpflicht anteilig: Fr. 10'800 ÷ 360 × Tage (MB 8/2026).
- **Beachten:** Nur bei Unterhalt zur Hauptsache und ohne Abzug nach Art. 45 Abs. 1 Bst. c (Unterhaltsbeiträge)
- **Beachten:** UJ-Beispiel: 10'800 ÷ 360 × 180 Tage = 5'400 (für den Satz voller Betrag)
- **Beachten:** Zusätzlich Ziff. 23.3: Ausbildungskosten über 3'200, max. 13'800 je Kind; Bund volljährig: Unterhalt ≥ Sozialabzug
- **Limiten:**
  - Kinderabzug Schulalter (CHF): Kanton **CHF 10'800 (Kinderabzug Fr. 10'800 für jedes unter elterlicher Sorge/Obhut stehende oder volljährige Kind in schulischer oder beruflicher Ausbildung (gilt für Schulalter und Ausbildung).)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800, keine Staffelung nach Alter; siehe sozialabzug.kind.**
  - Kinderabzug Grundbetrag (CHF): Kanton **n/a – Art. 48 Abs. 1 lit. a StG SG. Voraussetzung: Steuerpflichtiger kommt zur Hauptsache für den Unterhalt auf und beansprucht keinen Abzug für Unterhaltsbeiträge (Art. 45 Abs. 1 lit. c).** · Bund **CHF 6'800 (Kinderabzug CHF 6'800 pro minderjähriges oder in beruflicher/schulischer Ausbildung stehendes Kind, für dessen Unterhalt die steuerpflichtige Person sorgt; bei getrennter Besteuerung der Eltern hälftig bei gemeinsamer elterlicher Sorge ohne Unterhaltsbeiträge.)**
  - Abzug vom Steuerbetrag pro Kind (CHF, Bund): Kanton **n/a – Siehe data/werte/bund.** · Bund **CHF 263 (Ermässigung des Steuerbetrags um CHF 263 pro Kind oder unterstützungsbedürftige Person (Ehepaare sowie Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern/unterstützungsbedürftigen Personen im gleichen Haushalt, die deren Unterhalt zur Hauptsache bestreiten).)**
  - Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF): Kanton **CHF 13'800 (Zusätzlich zum Kinderabzug: höchstens weitere Fr. 13'800 für Ausbildungskosten je Kind in schulischer/beruflicher Ausbildung, soweit vom Steuerpflichtigen selbst getragen und über Fr. 3'200 (Selbstbehalt).)** · Bund **n/a – Bund: kein erhöhter Abzug für auswärtige Ausbildung; einheitlich CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).**
- **Bund:** Art. 35 Abs. 1 Bst. a DBG: einheitlich 6 800 Franken.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «23.2 Kinderabzug für jedes Kind in Schule oder Ausbildung Fr. 10’800 254»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «Fr. 10 800.– für jedes unter der elterlichen Sorge oder Obhut des Steuerpflichtigen stehende oder volljährige Kind»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Fr. 10’800 ÷ 360 × 180 Tage»
  - [Formular 1 SG 2026 UJ S. 1](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0002.md) `sg-form-1-2026-uj__c0002` – «Sofern in beruflicher Ausbildung: Dauer bis»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «soweit sie der Steuerpflichtige selbst trägt und sie Fr. 3200.– übersteigen»
  - [KS 30 S. 20](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0062.md) `bund-ks-30__c0062` – «ist erfüllt, wenn sie Beiträge mindestens in der Höhe des Sozialabzuges an das Kind ausrichtet»

<a id="23-3-sozialabzug-kinder"></a>
### Ziff. 23.3 – Ausbildungskosten für Kinder in Schule oder Ausbildung gemäss Formular 10 (Code 256)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Formular 10: Rechnungen (Semestergebühren, Bücher, Fahrkosten, auswärtige Verpflegung/Unterkunft)
- **Rein:** Rechnungen Ausbildung (Formular 10) → selbst getragene Ausbildungskosten je Kind · Kinderliste Seite 1 → Kind in Schule/Ausbildung (Voraussetzung Kinderabzug Ziff. 23.2)
- **Rechnen:** Kanton je Kind: min(selbst getragene Kosten − 3'200; 13'800), nur falls Kosten > 3'200 / Bund: kein Ausbildungskostenabzug (nur Kinderabzug 6'800)
- **Regel:** NEU 2026 höher: Ausbildungskosten je Kind max. Fr. 13'800 (bisher Fr. 13'700), soweit selbst getragen und über Fr. 3'200 (Selbstbehalt).
- **Beachten:** Voraussetzungen wie Kinderabzug Ziff. 23.2 (10'800): Unterhalt zur Hauptsache, Kind in Ausbildung (auch volljährig)
- **Beachten:** UJ: Abzug × Tage/360 kürzen, für Satzbestimmung voll (Art. 48 Abs. 3 StG; Merkblatt UJ Ziff. 7)
- **Beachten:** Verhältnisse am 31. Dezember 2026 bzw. Ende der Steuerpflicht massgebend (Art. 48 Abs. 2 StG)
- **Limiten:**
  - Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF): Kanton **CHF 13'800 (Zusätzlich zum Kinderabzug: höchstens weitere Fr. 13'800 für Ausbildungskosten je Kind in schulischer/beruflicher Ausbildung, soweit vom Steuerpflichtigen selbst getragen und über Fr. 3'200 (Selbstbehalt).)** · Bund **n/a – Bund: kein erhöhter Abzug für auswärtige Ausbildung; einheitlich CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 10'800 (Kinderabzug für Kind in schulischer oder beruflicher Ausbildung (auch volljährig): Fr. 10'800.)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Abzug CHF 6'800 (kein höherer Ausbildungsabzug beim Bund).)**
- **Bemerkung:** Formular 10/2026 nicht publiziert. Selbstbehalt Fr. 3'200 laut Art. 48 Abs. 1 Bst. a Ziff. 3 StG. «Bisher Fr. 13'700»: Vorjahreswert aus StG SG 2025 Art. 48 Abs. 1 Bst. a Ziff. 3 (jahr_ok, nur als Vergleich zum Vorjahr).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «23.3 Ausbildungskosten für Kinder in Schule oder Ausbildung Formular 10 256»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «höchstens weitere Fr. 13 800.– für Ausbildungskosten»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0011.md) `sg-mb-8-2026__c0011` – «23.3 Ausbildungskosten pro Kind in Schule/Ausbildung neu max.»
  - [StG SG Art. 48](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-48.md) `sg-stg-2025__art-48` – «höchstens weitere Fr. 13 700.– für Ausbildungskosten»
  - [DBG Art. 35](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-35.md) `bund-dbg-2026__art-35` – «6800 Franken für jedes minderjährige oder in der beruflichen oder schulischen Ausbildung stehende Kind»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Sofern Pauschal-, bzw. Maximalabzüge eingesetzt werden, sind diese im Umfang»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Kinderabzug für ganzes Kalenderjahr (satzbestimmend)»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «wenn der Steuerpflichtige für den Unterhalt zur Hauptsache aufkommt»

<a id="23-4-sozialabzug-unterstuetzung"></a>
### Ziff. 23.4 – Abzug für unterstützte Personen (nur direkte Bundessteuer, Code 264)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Bedürftigkeit; Name/Adresse, Höhe der Unterstützung
- **Rein:** Bescheinigung → Unterstützungsleistung je unterstützte Person im Jahr (mind. 6'800) · Formular 1 Ziff. 23.4 → «ja» + Anzahl unterstützte Personen · Nachweis Bedürftigkeit der unterstützten Person (Erwerbsunfähigkeit, Arbeitslosigkeit u.Ä.)
- **Rechnen:** Bund: 6'800 × Anzahl unterstützte Personen mit Unterstützung ≥ 6'800 je Person / Kanton: kein Abzug
- **Regel:** Gilt nur für die direkte Bundessteuer (nicht Kantons-/Gemeindesteuer): Fr. 6'800 je erwerbsunfähige/beschränkt erwerbsfähige unterstützte Person, wenn die Unterstützung mindestens dem Abzug entspricht; nicht für Ehegatten und Kinder mit Kinderabzug.
- **Beachten:** Nicht für Ehegatten und Kinder mit Kinderabzug; Kumulationsverbot gilt nur für dieselbe leistende Person
- **Beachten:** Person objektiv bedürftig; Leistung unentgeltlich (keine Gegenleistung wie Haushaltsbesorgung)
- **Beachten:** Bund je Person: Versicherungsabzug +700; Steuerbetrag −263 (Ehepaare; Alleinstehende nur bei gleichem Haushalt)
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **n/a – Unterstützungsabzug existiert nur bei der direkten Bundessteuer (data/werte/bund). Seed: WL 2025 Ziff. 23.4.** · Bund **CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'100 (Erhöhung des Versicherungsabzugs um Fr. 1'100 für jedes Kind, für das ein Kinderabzug geltend gemacht werden kann.)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**
  - Abzug vom Steuerbetrag pro Kind (CHF, Bund): Kanton **n/a – Siehe data/werte/bund.** · Bund **CHF 263 (Ermässigung des Steuerbetrags um CHF 263 pro Kind oder unterstützungsbedürftige Person (Ehepaare sowie Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern/unterstützungsbedürftigen Personen im gleichen Haushalt, die deren Unterhalt zur Hauptsache bestreiten).)**
- **Bund:** Art. 35 Abs. 1 Bst. b DBG: 6 800 Franken.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «23.4 Abzug für unterstützte Personen ja Anzahl Bescheinigung 264»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «Abzug gilt nur für die direkte Bundessteuer»
  - [DBG Art. 35](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-35.md) `bund-dbg-2026__art-35` – «6800 Franken für jede erwerbsunfähige oder beschränkt erwerbsfähige Person»
  - [KS 30 S. 21](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0065.md) `bund-ks-30__c0065` – «Wird in einem Steuerjahr weniger als der festgelegte Abzug geleistet, entfällt dieser Sozialabzug»
  - [KS 30 S. 21–22](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0067.md) `bund-ks-30__c0067` – «Dieses Kumulationsverbot von Kinderabzug und Unterstützungsabzug gilt aber nur für ein und dieselbe leistende Person»
  - [KS 30 S. 21](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0066.md) `bund-ks-30__c0066` – «müssen zudem unentgeltlich sein bzw. ohne Gegenleistung erfolgen»
  - [KS 30 S. 21](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0066.md) `bund-ks-30__c0066` – «als alleinerziehende Eltern mit vorschulpflichtigen Kindern aber kein»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t5.md) `bund-dbg-2026__art-33-t5` – «um 700 Franken für jedes Kind oder jede unterstützungsbedürftige Person»
  - [DBG Art. 36](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-36-t4.md) `bund-dbg-2026__art-36-t4` – «Der so ermittelte Steuerbetrag ermässigt sich um 263 Franken für jedes Kind oder jede unterstützungsbedürftige Person»
  - [DBG Art. 36](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-36-t4.md) `bund-dbg-2026__art-36-t4` – «die mit Kindern oder unterstützungsbedürftigen Personen im gleichen Haushalt zusammenleben»

<a id="24-berechnung-total"></a>
### Ziff. 24 – Steuerbares Einkommen gesamt (Code 268)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 22 (Reineinkommen) · Übertrag Ziff. 23.1–23.3 (Sozialabzüge Kanton)
- **Rechnen:** Kanton: Ziff. 22 − (23.1 + 23.2 + 23.3) / Bund: Reineinkommen − 6'800 je Kind − 6'800 je unterstützte Person − 2'800 Ehepaare
- **Regel:** Ziff. 22 abzüglich Ziff. 23.1 bis 23.3 (kantonal). Direkte Bundessteuer: eigene Sozialabzüge (Ziff. 23.4 usw.).
- **Beachten:** UJ: Sozialabzüge × Tage/360; Steuersatz auf Jahreseinkommen umgerechnet (von Amtes wegen)
- **Beachten:** Kanton: kein Verheiratetenabzug (Splittingtarif); Verheiratetenabzug nur Bund
- **Beachten:** Sozialabzüge nach Verhältnissen am Ende der Steuerperiode bzw. Steuerpflicht
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **n/a – Art. 48 Abs. 1 lit. a StG SG. Voraussetzung: Steuerpflichtiger kommt zur Hauptsache für den Unterhalt auf und beansprucht keinen Abzug für Unterhaltsbeiträge (Art. 45 Abs. 1 lit. c).** · Bund **CHF 6'800 (Kinderabzug CHF 6'800 pro minderjähriges oder in beruflicher/schulischer Ausbildung stehendes Kind, für dessen Unterhalt die steuerpflichtige Person sorgt; bei getrennter Besteuerung der Eltern hälftig bei gemeinsamer elterlicher Sorge ohne Unterhaltsbeiträge.)**
  - Unterstützungsabzug (CHF): Kanton **n/a – Unterstützungsabzug existiert nur bei der direkten Bundessteuer (data/werte/bund). Seed: WL 2025 Ziff. 23.4.** · Bund **CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)**
  - Verheiratetenabzug (CHF, Bund): Kanton **n/a – Siehe data/werte/bund.** · Bund **CHF 2'800 (Verheiratetenabzug CHF 2'800 für Ehepaare in rechtlich und tatsächlich ungetrennter Ehe.)**
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «24. Steuerbares Einkommen gesamt (Ziffer 22 abzüglich Ziffern 23.1-23.3) 268»
  - [DBG Art. 35](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-35.md) `bund-dbg-2026__art-35` – «2800 Franken für Ehepaare, die in rechtlich und tatsächlich ungetrennter Ehe leben»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «Die Sozialabzüge werden nach den Verhältnissen am Ende der Steuerperiode oder der Steuerpflicht festgelegt»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Kinderabzug für ganzes Kalenderjahr (satzbestimmend)»
  - [MB 8/2026 SG S. 2–3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0005.md) `sg-mb-8-2026__c0005` – «Massgebend für die Satzbestimmung sind immer die auf ein Jahr umgerechneten»
  - [DBG Art. 35](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-35.md) `bund-dbg-2026__art-35` – «Bei teilweiser Steuerpflicht werden die Sozialabzüge anteilsmässig gewährt»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben gemäss Formular 2 (Code 300)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 «Total» Steuerwert per 31.12.2026 (bzw. Ende der Steuerpflicht)
- **Rein:** Steuerauszug Bank/Depotauszug → Steuerwert per Stichtag (Total Formular 2) · Kontoauszug/Zinsausweis → Saldo per Stichtag · Krypto-Auszug → Bestand per Stichtag · Mitarbeiterbeteiligungen → im Wertschriftenverzeichnis aufführen
- **Rechnen:** Σ Steuerwerte Formular 2 per 31. Dezember 2026 bzw. Ende Steuerpflicht; Kurswert (ESTV-Kursliste), sonst innerer Wert
- **Regel:** Steuerwert am 31.12.2026: Wertpapiere zum Kurswert, sonst innerer Wert; bestrittene Forderungen mit Verlustwahrscheinlichkeit. Erträge in Ziff. 4.1.
- **Beachten:** Echte MA-Beteiligungen: Sperrfrist-Einschlag; gesperrte/nicht kotierte Optionen, unechte: steuerfrei, aber aufführen
- **Beachten:** Bestrittene/unsichere Forderungen: Verlustwahrscheinlichkeit berücksichtigen; Erträge → Ziff. 4.1
- **Beachten:** Fonds mit direktem Grundbesitz: nur Gesamtaktiven − direkter Grundbesitz steuerbar
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.1 Wertschriften und Guthaben Formular 2 300»
  - [StG SG Art. 56](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-56.md) `sg-stg-2026__art-56` – «Wertpapiere werden nach dem Kurswert oder, wenn kein solcher besteht, nach dem inneren Wert bewertet»
  - [SG EK/VM-Steuer](../../chunks/sg/dauernd/sg-info-ekst-vst/sg-info-ekst-vst__c0064.md) `sg-info-ekst-vst__c0064` – «die für die Bewertung der Wertpapiere und Devisen per Ende der Steuerperiode massgebend sind»
  - [StG SG Art. 53](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-53.md) `sg-stg-2026__art-53` – «Bei Anteilen an kollektiven Kapitalanlagen ist die Wertdifferenz zwischen den Gesamtaktiven der kollektiven Kapitalanlage und deren direktem Grundbesitz steuerbar»
  - [StG SG Art. 68](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-68.md) `sg-stg-2026__art-68` – «Das steuerbare Vermögen bemisst sich nach dem Stand am Ende der Steuerperiode oder der Steuerpflicht»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.1 aus Wertschriften und Guthaben 146»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 302)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung (Bestand 31.12., Kurswert)
- **Rein:** Eigene Aufstellung → Bargeld (CHF/Fremdwährung) per Stichtag · Bestand Gold/Edelmetalle → Menge × Kurs per Stichtag
- **Rechnen:** Σ Bargeld + Gold/Edelmetalle zum Verkehrswert per Stichtag; Devisen/Edelmetalle zum ESTV-Kurs Ende Steuerperiode
- **Regel:** Bestand per Stichtag zum Verkehrswert; Hausrat und persönliche Gebrauchsgegenstände sind nicht steuerbar.
- **Beachten:** Alltagsschmuck = persönlicher Gebrauchsgegenstand → steuerfrei; Wert deutlich über Üblichem → steuerbar (Art. 31 StV)
- **Beachten:** Stichtag Ende Steuerperiode; UJ: Wegzugs- oder Todestag
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.2 Bargeld, Gold und andere Edelmetalle Aufstellung 302»
  - [StG SG Art. 54](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-54.md) `sg-stg-2026__art-54` – «Das Vermögen wird zum Verkehrswert bewertet»
  - [SG EK/VM-Steuer](../../chunks/sg/dauernd/sg-info-ekst-vst/sg-info-ekst-vst__c0064.md) `sg-info-ekst-vst__c0064` – «Goldmünzen und Edelmetalle»
  - [SG EK/VM-Steuer](../../chunks/sg/dauernd/sg-info-ekst-vst/sg-info-ekst-vst__c0064.md) `sg-info-ekst-vst__c0064` – «die für die Bewertung der Wertpapiere und Devisen per Ende der Steuerperiode massgebend sind»
  - [StV SG Art. 31](../../chunks/sg/2025/sg-stv/sg-stv__art-31.md) `sg-stv__art-31` – «Als persönliche Gebrauchsgegenstände gelten die Gebrauchsgegenstände des Alltags, namentlich Kleider, Schmuck, Sportgeräte»
  - [MB 8/2026 SG S. 3–4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0008.md) `sg-mb-8-2026__c0008` – «Wegzugs- oder Todestag»
  - [StG SG Art. 63](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-63.md) `sg-stg-2026__art-63` – «der Hausrat und die persönlichen Gebrauchsgegenstände»
  - [StV SG Art. 31](../../chunks/sg/2025/sg-stv/sg-stv__art-31.md) `sg-stv__art-31` – «Vermögensgegenstände und Sammlungen, deren Wert das gemeinhin Übliche deutlich übersteigt»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen (Code 304)

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Bescheinigung der Versicherungsgesellschaft: Rückkaufswert per 31.12.
- **Rein:** Bescheinigung Versicherungsgesellschaft → Rückkaufswert per Stichtag · Police → Gesellschaft, Abschluss-/Ablaufjahr, Versicherungssumme (Formularfelder)
- **Rechnen:** Σ Rückkaufswerte je Police per Stichtag; anwartschaftliche oder nicht rückkaufsfähige Ansprüche auf periodische Leistungen steuerfrei
- **Regel:** Rückkaufswert per Stichtag; anwartschaftliche oder nicht rückkaufsfähige Ansprüche auf periodische Leistungen sind vermögenssteuerfrei (Art. 63 Abs. 1 Bst. b StG).
- **Beachten:** Stichtag 31. Dezember 2026 bzw. Ende der Steuerpflicht
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.3 Lebens- und Rentenversicherungen Bescheinigung»
  - [StG SG Art. 56](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-56.md) `sg-stg-2026__art-56` – «Lebens- und Rentenversicherungen unterliegen der Vermögenssteuer mit ihrem Rückkaufswert»
  - [StG SG Art. 63](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-63.md) `sg-stg-2026__art-63` – «anwartschaftliche oder nicht rückkaufsfähige Ansprüche auf periodische Leistungen»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge (Code 306)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Fahrzeugausweis/Kaufvertrag: Art, Kaufpreis, Erwerbsjahr
- **Rein:** Fahrzeugausweis/Kaufvertrag → Art, Kaufpreis, Erwerbsjahr je Fahrzeug
- **Rechnen:** Je Fahrzeug Art + Kaufpreis + Erwerbsjahr angeben; Steuerwert = Verkehrswert per Stichtag
- **Regel:** Art, Kaufpreis und Erwerbsjahr deklarieren; steuerbar ist der Verkehrswert (Bewertung durch Steueramt). Hausrat/persönliche Gebrauchsgegenstände sind steuerfrei, Motorfahrzeuge werden deklariert.
- **Beachten:** Motorfahrzeuge zählen nicht zum Hausrat → steuerbar (Art. 31 Abs. 3 StV)
- **Beachten:** Fahrzeuge im Geschäftsvermögen Selbständiger → Ziff. 32.2 (Aktiven Schlussbilanz)
- **Bemerkung:** Bewertungsmethode (Abschreibungssätze) in SG-Quellen 2026 nicht enthalten.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.4 Motorfahrzeuge Art»
  - [StG SG Art. 54](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-54.md) `sg-stg-2026__art-54` – «Das Vermögen wird zum Verkehrswert bewertet»
  - [StG SG Art. 63](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-63.md) `sg-stg-2026__art-63` – «der Hausrat und die persönlichen Gebrauchsgegenstände»
  - [StV SG Art. 31](../../chunks/sg/2025/sg-stv/sg-stv__art-31.md) `sg-stv__art-31` – «Nicht zum Hausrat oder zu den persönlichen Gebrauchsgegenständen zählen namentlich Motorfahrzeuge, Boote, Reitpferde und Kunstsammlungen»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Anteile an unverteilten Erbschaften (Code 308)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung Nachlass / Erbteilungsunterlagen
- **Rein:** Erbteilungs-/Nachlassaufstellung → eigener Anteil am unverteilten Nachlass per Stichtag
- **Rechnen:** Anteil am Nachlassvermögen der Erbengemeinschaft zum Verkehrswert per Stichtag
- **Regel:** Anteil am Nachlass der Erbengemeinschaft zum Verkehrswert; Erträge in Ziff. 6.2.
- **Beachten:** Erträge aus unverteilten Erbschaften → Ziff. 6.2
- **Beachten:** Erbanfall 2026 ≥ 50'000: Erbteil nur pro rata ab Erbgang besteuert (Art. 68 Abs. 3–4 StG; Art. 32ter StV)
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.5 Anteile an unverteilten Erbschaften Aufstellung 308»
  - [StG SG Art. 54](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-54.md) `sg-stg-2026__art-54` – «Das Vermögen wird zum Verkehrswert bewertet»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «6.2 Ertrag aus unverteilten Erbschaften 158»
  - [StG SG Art. 68](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-68.md) `sg-stg-2026__art-68` – «Erbt der Steuerpflichtige während der Steuerperiode Vermögen»
  - [StV SG Art. 32 ter](../../chunks/sg/2025/sg-stv/sg-stv__art-32ter.md) `sg-stv__art-32ter` – «wird die Veranlagung des Vermögens nur angepasst, wenn der Vermögensanfall mindestens Fr. 50 000.– beträgt»
  - [StG SG Art. 68](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-68.md) `sg-stg-2026__art-68` – «Besteht die Steuerpflicht nur während eines Teils der Steuerperiode, wird die diesem Zeitraum entsprechende Steuer erhoben»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte (Code 310): Boote, Reitpferde, Sammlungen; ohne Hausrat und persönliche Gebrauchsgegenstände

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung mit mutmasslichem Verkehrswert
- **Rein:** Eigene Aufstellung → Art und Verkehrswert (Boote, Reitpferde, Sammlungen) per Stichtag
- **Rechnen:** Σ Verkehrswerte der übrigen Vermögenswerte per Stichtag (ohne Hausrat und persönliche Gebrauchsgegenstände)
- **Regel:** Hausrat und persönliche Gebrauchsgegenstände sind nicht steuerbar (Art. 63 StG); übrige Werte zum Verkehrswert.
- **Beachten:** Steuerbar: Kunstsammlungen und Sammlungen, deren Wert das Übliche deutlich übersteigt (Art. 31 Abs. 3 StV)
- **Beachten:** Steuerfrei: Möbel, Bilder, Bücher, Kleider, Schmuck, Sportgeräte u.Ä. (Art. 31 Abs. 1–2 StV)
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.6 Übrige Vermögenswerte Arten 310»
  - [StG SG Art. 63](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-63.md) `sg-stg-2026__art-63` – «der Hausrat und die persönlichen Gebrauchsgegenstände»
  - [StV SG Art. 31](../../chunks/sg/2025/sg-stv/sg-stv__art-31.md) `sg-stv__art-31` – «Vermögensgegenstände und Sammlungen, deren Wert das gemeinhin Übliche deutlich übersteigt»
  - [StV SG Art. 31](../../chunks/sg/2025/sg-stv/sg-stv__art-31.md) `sg-stv__art-31` – «namentlich Möbel, Teppiche, Bilder, Küchen- und Gartengeräte, Geschirr, Bücher»
  - [StG SG Art. 54](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-54.md) `sg-stg-2026__art-54` – «Das Vermögen wird zum Verkehrswert bewertet»

<a id="31-vermoegen-liegenschaften"></a>
### Ziff. 31 – Liegenschaften gemäss Formular 7 (Code 710)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Formular 7 Steuerwert gemäss Grundstückschätzung
- **Rein:** Amtliche Grundstückschätzung → Verkehrswert (Steuerwert) je Grundstück · Formular 7 → Total Steuerwerte Liegenschaften · Grundbuchauszug → Eigentums-/Miteigentumsquote, Nutzniessung
- **Rechnen:** Σ je Grundstück: Verkehrs- bzw. Ertragswert gemäss Schätzung × Eigentumsquote; Neu-/Um-/Anbau ohne Schätzung: + 80 % der Neu-/Um-/Anbaukosten
- **Regel:** Steuerwert gemäss amtlicher Grundstückschätzung (Verkehrswert; überwiegend land-/forstwirtschaftlich genutzte Grundstücke im Geltungsbereich des bäuerlichen Bodenrechts zum Ertragswert, Art. 58 StG). Eigenmietwert in Ziff. 5.
- **Beachten:** Überwiegend land-/forstwirtschaftlich genutzte Grundstücke (bäuerliches Bodenrecht): Ertragswert
- **Beachten:** Nutzniessung → beim Nutzniesser; Wohnrecht → beim (Mit-)Eigentümer (BGer 9C_305/2023)
- **Beachten:** Geschäftsliegenschaften ebenfalls hier (nicht Ziff. 32); Ertrag/Eigenmietwert → Ziff. 5
- **Bemerkung:** Formular 7/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «31. Liegenschaften Formular 7 710»
  - [StG SG Art. 57](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-57.md) `sg-stg-2026__art-57` – «Der Verkehrswert von Grundstücken entspricht dem mittleren Preis»
  - [StG SG Art. 58](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-58.md) `sg-stg-2026__art-58` – «überwiegend land- oder forstwirtschaftlich genutzt werden, werden zum Ertragswert bewertet»
  - [StV SG Art. 30 bis](../../chunks/sg/2025/sg-stv/sg-stv__art-30bis.md) `sg-stv__art-30bis` – «Zuschlag zur geltenden Schätzung in der Höhe von 80 Prozent der Neu-, Um- und Anbaukosten»
  - [VGS SG Art. 8](../../chunks/sg/2025/sg-gsv/sg-gsv__art-8.md) `sg-gsv__art-8` – «als Steuerwerte der Miet- und Verkehrswert des Grundstücks»
  - [StB 34 Nr. 2 S. 1](../../chunks/sg/dauernd/sg-stb-34-2/sg-stb-34-2__c0002.md) `sg-stb-34-2__c0002` – «Massgebend ist die sachenrechtliche Quote gemäss Grundbucheintrag»
  - [StB 34 Nr. 2 S. 1](../../chunks/sg/dauernd/sg-stb-34-2/sg-stb-34-2__c0002.md) `sg-stb-34-2__c0002` – «ihm zur Nutzung überlassenen Teil an der Liegenschaft zu versteuern»
  - [StB 34 Nr. 2 S. 1](../../chunks/sg/dauernd/sg-stb-34-2/sg-stb-34-2__c0002.md) `sg-stb-34-2__c0002` – «Wohnrecht belastete Liegenschaft vermögenssteuerlich beim (Mit-)Eigentümer»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «(diese sind unter Ziffer 31»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «5. Ertrag aus Liegenschaften Formular 7 712»

<a id="32-1-32-3-vermoegen-uebrige"></a>
### Ziff. 32.1-32.3 – Betriebsvermögen aus selbständiger Erwerbstätigkeit: Geschäftskapital Gesellschaften (Code 314), Aktiven Schlussbilanz (316), landwirtschaftlicher Betrieb Formular 12 (318)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Schlussbilanz (Aktiven), Formular 12 (Landwirtschaft)
- **Rein:** Abschluss Personengesellschaft → Anteil Geschäftskapital (Ziff. 32.1) · Schlussbilanz → Aktiven (Fahrzeuge, Maschinen, Mobiliar, Geräte) ohne Geschäftsliegenschaften (Ziff. 32.2) · Formular 12 → Vermögen im landwirtschaftlichen Betrieb (Ziff. 32.3)
- **Rechnen:** Σ Ziff. 32.1 + 32.2 + 32.3 zum Einkommenssteuerwert (Art. 55 StG); ohne Buchwert Geschäftsliegenschaften (→ Ziff. 31)
- **Regel:** Geschäftsvermögen zum Einkommenssteuerwert (Buchwert ohne Geschäftsliegenschaften; diese in Ziff. 31). Schulden in Ziff. 34.2.
- **Beachten:** Geschäftsjahr ≠ Kalenderjahr: Stand am Ende des 2026 abgeschlossenen Geschäftsjahres (Art. 68 Abs. 2 StG)
- **Beachten:** Geschäftsschulden separat in Ziff. 34.2
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «32.1 Geschäftskapital in Kollektiv-, Kommandit- und einfachen Gesellschaften 314»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «32.3 Vermögen im landwirtschaftlichen Betrieb Formular 12 318»
  - [StG SG Art. 55](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-55.md) `sg-stg-2026__art-55` – «werden zum Einkommenssteuerwert bewertet»
  - [StG SG Art. 68](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-68.md) `sg-stg-2026__art-68` – «bestimmt sich das steuerbare Geschäftsvermögen nach dem Eigenkapital am Ende des in der Steuerperiode abgeschlossenen Geschäftsjahres»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «34.2 Geschäftsschulden Formular 5 506»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «(diese sind unter Ziffer 31»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 322)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 30.1–30.6, 31 und 32.1–32.3
- **Rechnen:** Σ Ziff. 30.1 bis 30.6 + Ziff. 31 + Ziff. 32.1 bis 32.3
- **Regel:** Summe Ziff. 30 bis 32.
- **Beachten:** Inkl. Vermögen der minderjährigen Kinder, Nutzniessungsvermögen und Auslandvermögen
- **Beachten:** Stichtag 31. Dezember 2026 bzw. Ende der Steuerpflicht
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «33. Total der Vermögenswerte 322»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «der Steuerpflichtigen und der minderjährigen Kinder, einschliesslich Nutzniessungsvermögen»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «Steuerwert am 31. Dezember 2026 bzw. am Ende der Steuerpflicht»

<a id="34-1-schulden-privat"></a>
### Ziff. 34.1 – Privatschulden gemäss Formular 5 (Code 504)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Leasingvertrag Fahrzeug / Leasingraten-Abrechnung → Formular 5 Teil A: Schuld am 31.12.2026 je Gläubiger (Schuldenausweis)
- **Rein:** Schuldenausweis Bank (Hypothek, Kredit) → Schuld per Stichtag (Formular 5) · Privater Darlehensvertrag → Saldo per Stichtag, Gläubiger
- **Rechnen:** Σ nachgewiesene Privatschulden per Stichtag; Solidar-/Bürgschaftsschulden nur selbst zu tragender Anteil
- **Regel:** Nachgewiesene Schulden, für die der Steuerpflichtige allein haftet, voll; Solidar-/Bürgschaftsschulden nur soweit er sie tragen muss. Schuldzinsen in Ziff. 11.
- **Beachten:** Solidarhypothek bei Miteigentum: Anteil nach interner Quote; hälftiges Miteigentum ohne Abrede: je Hälfte
- **Beachten:** Nutzniessung: Schulden auf belastetem Grundstück beim Nutzniesser; anwartschaftliche Schulden nicht abziehbar
- **Beachten:** Bürgschaft nur, soweit Bürge belangt werden kann; Schuldzinsen → Ziff. 11; Geschäftsschulden → Ziff. 34.2
- **Bemerkung:** Formular 5/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «34.1 Privatschulden Formular 5 504»
  - [StG SG Art. 62](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-62.md) `sg-stg-2026__art-62` – «Nachgewiesene Schulden, für die der Steuerpflichtige allein haftet, werden voll abgezogen»
  - [StB 34 Nr. 2 S. 1](../../chunks/sg/dauernd/sg-stb-34-2/sg-stb-34-2__c0003.md) `sg-stb-34-2__c0003` – «kann jeder Solidarschuldner den von ihm nach der internen Quote zu tragenden Anteil an der Gesamtschuld abziehen»
  - [StB 34 Nr. 2 S. 1](../../chunks/sg/dauernd/sg-stb-34-2/sg-stb-34-2__c0003.md) `sg-stb-34-2__c0003` – «der Abzug der auf dem nutzniessungsbelasteten Grundstück lastenden Schulden»
  - [StB 34 Nr. 2 S. 1–2](../../chunks/sg/dauernd/sg-stb-34-2/sg-stb-34-2__c0004.md) `sg-stb-34-2__c0004` – «Bloss voraussehbare, anwartschaftliche Schulden sind nicht abzugsfähig»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «11. Schuldzinsen Formular 5 500»
  - [StB 34 Nr. 2 S. 1](../../chunks/sg/dauernd/sg-stb-34-2/sg-stb-34-2__c0003.md) `sg-stb-34-2__c0003` – «beide Miteigentümer je die Hälfte der Schuld abziehen»
  - [StB 34 Nr. 2 S. 1–2](../../chunks/sg/dauernd/sg-stb-34-2/sg-stb-34-2__c0004.md) `sg-stb-34-2__c0004` – «werden nur berücksichtigt, wenn und soweit der Bürge für die verbürgte Schuld belangt werden kann»

<a id="34-2-schulden-privat"></a>
### Ziff. 34.2 – Geschäftsschulden gemäss Formular 5 (Code 506)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 5 Teil B / Bilanz: Schuld am Bilanzstichtag
- **Rein:** Schlussbilanz → Fremdkapital (Geschäftsschulden) per Bilanzstichtag · Formular 5 → Total Geschäftsschulden
- **Rechnen:** Σ Geschäftsschulden gemäss Schlussbilanz des in der Steuerperiode abgeschlossenen Geschäftsjahres
- **Regel:** Geschäftsschulden separat von den Privatschulden.
- **Beachten:** Geschäftsjahr ≠ Kalenderjahr: Stand Ende des 2026 abgeschlossenen Geschäftsjahres (Art. 68 Abs. 2 StG)
- **Beachten:** Privatschulden separat in Ziff. 34.1
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «34.2 Geschäftsschulden Formular 5 506»
  - [StG SG Art. 62](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-62.md) `sg-stg-2026__art-62` – «Nachgewiesene Schulden, für die der Steuerpflichtige allein haftet, werden voll abgezogen»
  - [StG SG Art. 68](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-68.md) `sg-stg-2026__art-68` – «bestimmt sich das steuerbare Geschäftsvermögen nach dem Eigenkapital am Ende des in der Steuerperiode abgeschlossenen Geschäftsjahres»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Reinvermögen (Code 326)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 33 (Total Vermögenswerte) · Übertrag Ziff. 34.1 + 34.2 (Schulden)
- **Rechnen:** Ziff. 33 − (Ziff. 34.1 + Ziff. 34.2)
- **Regel:** Ziff. 33 abzüglich Ziff. 34.
- **Beachten:** Steuerbar ist das gesamte Reinvermögen (Art. 53 Abs. 1 StG)
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «35. Reinvermögen (Ziffer 33 abzüglich 34) 326»
  - [StG SG Art. 53](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-53.md) `sg-stg-2026__art-53` – «Der Vermögenssteuer unterliegt das gesamte Reinvermögen»

<a id="36-1-36-3-vermoegen-sozialabzug"></a>
### Ziff. 36.1-36.3 – Sozialabzüge Vermögen: alleinstehend Fr. 75'000 (Code 330), gemeinsam steuerpflichtige Ehegatten Fr. 150'000 (332), je minderjähriges Kind Fr. 20'000 (334)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien/Kinder Seite 1 (Stichtag 31.12.2026)
- **Rein:** Personalien Seite 1 → Zivilstand und minderjährige Kinder am 31. Dezember 2026 bzw. Ende Steuerpflicht
- **Rechnen:** Alleinstehend 75'000 bzw. Ehegatten 150'000 (2 × 75'000) + 20'000 × minderjährige Kinder mit Kinderabzug
- **Regel:** Abzug Fr. 75'000 je Steuerpflichtigen (Ehepaar 150'000) plus Fr. 20'000 je minderjähriges Kind mit Kinderabzug nach Art. 48 Abs. 1 lit. a. Verhältnisse am Ende der Steuerperiode. Einfache Vermögenssteuer 1,7 Promille.
- **Beachten:** Kinder: nur minderjährig, unter Sorge/Obhut, mit Kinderabzug nach Art. 48 Abs. 1 lit. a StG
- **Beachten:** Verhältnisse am Ende der Steuerperiode bzw. Steuerpflicht (Art. 64 Abs. 2 StG)
- **Beachten:** Nur Kantons-/Gemeindesteuer: Bund erhebt keine Vermögenssteuer (Art. 1 DBG)
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 75'000 (Sozialabzug vom Reinvermögen: Fr. 75'000 für jeden Steuerpflichtigen.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 150'000 (Gemeinsam steuerpflichtige Ehegatten: Fr. 75'000 für jeden Steuerpflichtigen, somit Fr. 150'000 gemeinsam.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 20'000 (Zusätzlich Fr. 20'000 für jedes minderjährige, unter der elterlichen Sorge oder Obhut stehende Kind, für das ein Kinderabzug nach Art. 48 Abs. 1 lit. a beansprucht werden kann.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «36.1 Abzug für alleinstehende Steuerpflichtige Fr. 75’000 330»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «36.3 Abzug für jedes minderjährige Kind Fr. 20’000 334»
  - [StG SG Art. 64](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-64.md) `sg-stg-2026__art-64` – «für jeden Steuerpflichtigen Fr. 75 000.–»
  - [DBG Art. 1](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-1.md) `bund-dbg-2026__art-1` – «eine Einkommenssteuer von den natürlichen Personen»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen gesamt (Code 338)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 35 abzüglich Ziff. 36.1 bis 36.3
- **Rechnen:** Ziff. 35 − Σ Ziff. 36.1 bis 36.3; einfache Steuer = 1,7 ‰ × steuerbares Vermögen (Rest < 1'000 entfällt); Steuer = einfache Steuer × Steuerfüsse
- **Regel:** Ziff. 35 abzüglich Ziff. 36.1 bis 36.3. Einfache Steuer 1,7 Promille; Restbeträge unter Fr. 1'000 fallen ausser Betracht (Art. 65 StG).
- **Beachten:** Kantonssteuerfuss 105 %; Gemeinde-/Kirchensteuerfuss je Gemeinde
- **Beachten:** UJ: einfache Steuer × Tage/360 (Art. 68 Abs. 3 StG; Merkblatt UJ Ziff. 10)
- **Beachten:** Bund: keine Vermögenssteuer (DBG: nur Einkommenssteuer natürlicher Personen)
- **Limiten:**
  - Steuerfuss Kanton (%/Einheiten): Kanton **105 % (Kantonssteuerfuss 2026: 105 % der einfachen Steuer (Gemeinde- und Kirchensteuerfüsse je Gemeinde in der Steuerfusstabelle).)** · Bund **n/a – Kantonaler Steuerfuss; Bund hat einen eigenen Tarif (Art. 36 DBG) ohne Steuerfuss.**
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «37. Steuerbares Vermögen gesamt (Ziffer 35 abzüglich Ziffern 36.1 bis 36.3) 338»
  - [StG SG Art. 65](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-65.md) `sg-stg-2026__art-65` – «Die einfache Steuer vom steuerbaren Vermögen beträgt 1,7 Promille»
  - [MB 8/2026 SG S. 3–4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0008.md) `sg-mb-8-2026__c0008` – «Die Vermögenssteuer wird nach der Dauer der Steuerpflicht erhoben»
  - [StG SG Art. 68](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-68.md) `sg-stg-2026__art-68` – «wird die diesem Zeitraum entsprechende Steuer erhoben»
  - [DBG Art. 1](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-1.md) `bund-dbg-2026__art-1` – «eine Einkommenssteuer von den natürlichen Personen»

## Weitere Angaben

<a id="40-1-40-3-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. 40.1-40.3 – Kapitalleistungen aus Vorsorge: aus Säule 3a (40.1), aus 2. Säule (40.2), übrige (40.3)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung / Bank (Auszahlung 2026)
- **Rein:** Bescheinigung 3a-Bank/-Versicherung → Kapitalbezug 2026 (Ziff. 40.1) · Bescheinigung Pensionskasse/Freizügigkeitskonto/-police → Kapitalleistung 2. Säule (Ziff. 40.2) · Bescheinigung übrige Vorsorge (z.B. Kapitalabfindung AHV/IV) → Ziff. 40.3
- **Rechnen:** Kanton: einfache Steuer = 2,0 % (Ehegatten; Alleinstehende mit Kindern/Unterstützten) bzw. 2,2 % (übrige) × Leistung / Bund: Fünftel Tarif Art. 36 DBG
- **Regel:** Kapitalleistungen aus Vorsorge (gebundene 3a, 2. Säule, übrige) werden gesondert und zu einem separaten Satz besteuert (volle Jahressteuer: 2,0% Ehegatten bzw. 2,2% übrige); allgemeine Abzüge und Sozialabzüge werden nicht gewährt. Nicht in Ziff. 6.4 erfassen.
- **Beachten:** Gesondert, volle Jahressteuer (auch bei UJ), Zuflussjahr massgebend; keine allgemeinen Abzüge/Sozialabzüge
- **Beachten:** Nicht in Ziff. 6.4 oder Total der Einkünfte erfassen, sondern hier (Seite 4 unten)
- **Beachten:** Ebenso gesondert: gleichartige Arbeitgeber-Abfindungen, Zahlungen bei Tod/bleibenden gesundheitlichen Nachteilen
- **Limiten:**
  - Kapitalleistungen aus Vorsorge – Steuersatz/Tarif (separate Jahressteuer): Kanton **Kapitalleistungen aus Vorsorge gesondert, volle Jahressteuer. Einfache Steuer 2,0 % für gemeinsam steuerpflichtige Ehegatten (und Verwitwete/Getrennte/Geschiedene/Ledige mit Kindern bzw. Unterstützungsbedürftigen im gleichen Haushalt), 2,2 % für die übrigen Steuerpflichtigen. Allgemeine Abzüge und Sozialabzüge nicht gewährt; Steueranspruch im Zeitpunkt des Zuflusses.** · Bund **Kapitalleistungen aus Vorsorge (Art. 22 DBG) und Zahlungen bei Tod/bleibenden Nachteilen werden gesondert besteuert (volle Jahressteuer, Steuerjahr des Zuflusses); Steuer = ein Fünftel der Tarife nach Art. 36 Abs. 1, 2 und 2bis erster Satz DBG (Bruchteil 1/5); keine Sozialabzüge.**
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0013.md) `sg-form-1-2026-uj__c0013` – «40.1 aus gebundener Vorsorge Säule 3a Bescheinigung»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0013.md) `sg-form-1-2026-uj__c0013` – «40.2 aus Einrichtungen der beruflichen Vorsorge (2. Säule) Bescheinigung»
  - [StG SG Art. 52](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-52.md) `sg-stg-2026__art-52` – «werden gesondert besteuert»
  - [DBG Art. 38](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-38.md) `bund-dbg-2026__art-38` – «Sie wird zu einem Fünftel der Tarife nach Artikel 36 Absätze 1, 2 und 2bis erster Satz berechnet»
  - [DBG Art. 38](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-38.md) `bund-dbg-2026__art-38` – «Die Sozialabzüge werden nicht gewährt»
  - [StG SG Art. 35](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-35-t1.md) `sg-stg-2026__art-35-t1` – «Leistungen aus Vorsorgekassen, aus Spar- und Gruppenversicherungen sowie aus Freizügigkeitspolicen und Freizügigkeitskonten»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Kapitalleistungen aus Vorsorge sind auf Seite 4 unten einzu»
  - [StG SG Art. 35](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-35-t1.md) `sg-stg-2026__art-35-t1` – «mit Einschluss der Kapitalabfindungen und Rückzahlungen von Einlagen, Prämien und Beiträgen»
  - [StG SG Art. 52](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-52.md) `sg-stg-2026__art-52` – «Die einfache Steuer beträgt 2,0 Prozent für gemeinsam steuerpflichtige Ehegatten und 2,2 Prozent für die übrigen Steuerpflichtigen»
  - [StG SG Art. 52](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-52.md) `sg-stg-2026__art-52` – «Der Steueranspruch auf die Jahressteuer entsteht im Zeitpunkt, in dem die Leistung zufliesst»

<a id="41-berechnung-total"></a>
### Ziff. 41 – Total Kapitalleistungen aus Vorsorge (Code 950)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 40.1 + 40.2 + 40.3
- **Rechnen:** Σ Ziff. 40.1 bis 40.3
- **Regel:** Summe Ziff. 40.1 bis 40.3.
- **Beachten:** Nicht ins Total der Einkünfte (Ziff. 7); gesonderte Besteuerung (Art. 52 StG)
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0013.md) `sg-form-1-2026-uj__c0013` – «41. Total Kapitalleistungen aus Vorsorge 950»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Kapitalleistungen aus Vorsorge sind auf Seite 4 unten einzu»
  - [StG SG Art. 52](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-52.md) `sg-stg-2026__art-52` – «werden gesondert besteuert. Sie unterliegen einer vollen Jahressteuer»

## Hilfsblatt Berufskosten (Formular 4)

<a id="form-4-ziff-1-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.1 – Fahrkosten öffentliche Verkehrsmittel (Code 400 Person 1 / 450 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg → ÖV-Abo/Billett-Beleg; Weg von–nach
- **Rein:** ÖV-Abo/Billette → tatsächliche Kosten Wohn- bis Arbeitsort · Lohnausweis Feld F → angekreuzt = keine Arbeitswegkosten, kein Abzug · Lohnausweis Ziff. 2.3 → vom Arbeitgeber vergütete Fahrkosten (im Bruttolohn)
- **Rechnen:** Kanton: min(effektive ÖV-Kosten; 8'000) / Bund: min(…; 3'300); Billette nur für Arbeitstage (Vollzeit 220, ohne Homeoffice)
- **Regel:** Tatsächliche, nachgewiesene Kosten des öffentlichen Verkehrsmittels, höchstens Fr. 8'000 (kantonal; Maximalabzug, keine Pauschale, bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt). Basis 220 Arbeitstage; keine Fahrkosten für Homeoffice-Tage und Tage ohne Arbeitsleistung (bei Abo keine Kürzung). Lohnausweis Feld F angekreuzt = keine Arbeitswegkosten → kein Abzug.
- **Beachten:** Maximalabzug, keine Pauschale: bei UJ, Stellenantritt/-aufgabe, Teilzeit nicht kürzen; Haupt- + Nebenerwerb gesamt
- **Beachten:** Abo nicht um Homeoffice-Tage kürzen
- **Beachten:** Arbeitgeber zahlt GA ohne geschäftliche Notwendigkeit: Wert im Bruttolohn, Abzug nur Kosten Streckenabo
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 (Maximalabzug, keine Pauschale; bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **220 Tage (Für die Berechnung des Fahrkostenabzugs wird von 220 Arbeitstagen pro Kalenderjahr (Vollzeitstelle) ausgegangen, sofern nicht eine höhere Anzahl nachgewiesen wird. Homeoffice-Tage und Tage ohne Arbeitsleistung zählen nicht.)** · Bund **n/a – Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).**
- **Bund:** Maximum Fr. 3'300 (Art. 26 Abs. 1 Bst. a DBG).
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [StB 39 Nr. 3 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0011.md) `sg-stb-39-3__c0011` – «Es handelt sich um einen Maximalabzug und nicht um eine Pauschale»
  - [StG SG Art. 39](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-39.md) `sg-stg-2026__art-39` – «die notwendigen Kosten für Fahrten zwischen Wohn- und Arbeitsstätte bis zum Betrag von Fr. 8000.–»
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0010.md) `sg-stb-39-3__c0010` – «Für Homeoffice-Tage und Tage ohne Arbeitsleistung»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer keine Kosten für den Arbeitsweg»
  - [StB 39 Nr. 3 S. 4](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0013.md) `sg-stb-39-3__c0013` – «ist diese Entschädigung in Ziff. 2.3 des Lohnausweises zu deklarieren»
  - [StB 39 Nr. 3 S. 4–5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0014.md) `sg-stb-39-3__c0014` – «Das GA stellt für den Mitarbeitenden keine geschäftliche Notwendigkeit dar»
  - [StB 39 Nr. 3 S. 4–5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0014.md) `sg-stb-39-3__c0014` – «Fahrkosten für Streckenabo»

<a id="form-4-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.2 – Fahrkosten Fahrrad, Motorfahrrad, Kleinmotorrad (Code 402 Person 1 / 452 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Belege (Pauschale)
- **Rein:** Keine Belege (Pauschale); Angabe Arbeitsweg und Fussweg zur Haltestelle
- **Rechnen:** Pauschale 700 pro Jahr (Kanton = Bund); zählt zum Fahrkosten-Maximum Kanton 8'000 / Bund 3'300
- **Regel:** Pauschal Fr. 700 im Jahr (Fahrrad, Motorfahrrad, Kleinmotorrad bis 50 cm3 mit gelbem Schild), wenn zu Fuss/zur Haltestelle mehr als 10 Minuten nötig sind.
- **Beachten:** Kanton: nur wenn Arbeitsweg zu Fuss bzw. zur nächsten ÖV-Haltestelle > 10 Minuten (StB 39 Nr. 3)
- **Beachten:** Kleinmotorrad ≤ 50 cm3, gelbes Kontrollschild; übrige Motorräder → km-Ansatz Ziff. 1.3
- **Beachten:** Bund: tatsächliche Kosten nicht zusätzlich zur Pauschale abziehbar
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Pauschale Fr. 700 im Jahr bei Benützung eines Fahrrades, eines Motorfahrrades oder eines Kleinmotorrades.)** · Bund **CHF 700 (Fahrrad, Motorfahrrad, Motorrad mit gelbem Kontrollschild: Pauschale CHF 700 pro Jahr; tatsächliche Kosten können nicht zusätzlich geltend gemacht werden.)**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 (Maximalabzug, keine Pauschale; bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0009.md) `sg-stb-39-3__c0009` – «Fr. 700.-- im Jahr bei Benützung eines Fahrrades»
  - [StB 39 Nr. 3 S. 1](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0003.md) `sg-stb-39-3__c0003` – «mehr als 10 Minuten benötigt»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0043.md) `bund-wl-2a-2026__c0043` – «Tatsächliche Kosten können nicht zusätzlich zum Pauschalabzug»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0043.md) `bund-wl-2a-2026__c0043` – «Einen Pauschalabzug von 700 Fr. im Jahr bei Benützung»

<a id="form-4-ziff-1-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.3 – Fahrkosten Motorfahrzeug (Auto/Motorrad): Fr. 0.75 pro km ab 2026 (Zwischentotal max. Fr. 8'000)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Begründung für Privatfahrzeug, Arbeitstage, km pro Weg; Bordbuch bei Geschäftsfahrzeug
- **Rein:** Begründung Privatfahrzeug → kein ÖV bzw. Unzumutbarkeit (Gesundheit, Haltestelle, Fahrplan, Dienstfahrten) · Arbeitstage (ohne Homeoffice) und km Hin- und Rückweg · Arbeitgeberbescheinigung/Spesenabrechnung → Dienstfahrten mit Privatauto · Lohnausweis Ziff. 2.2 / Feld F → Geschäftsfahrzeug
- **Rechnen:** Kanton: min(Arbeitstage × km/Tag × 75 Rp.; 8'000) / Bund: min(Tage × km × 75 Rp. Auto bzw. 40 Rp. Motorrad weiss; 3'300)
- **Regel:** NEU 2026: Fr. 0.75 je Fahrkilometer (2025: Fr. 0.70), einheitlicher Ansatz. Privatfahrzeug nur, wenn kein ÖV zur Verfügung steht oder dessen Benützung nicht zumutbar ist; sonst nur ÖV-Kosten. Geschäftsfahrzeug mit Privatnutzung: Pauschalberechnung 0,9% des Kaufpreises pro Monat im Lohnausweis Ziff. 2.2 ersetzt zugleich den Fahrkostenabzug (kein Abzug).
- **Beachten:** ÖV unzumutbar: Gesundheit; Haltestelle > 10 Fussmin. (bei Parkplatz P+R: Auto nur bis dort); Mehraufwand > 60 Min./Tag
- **Beachten:** Ferner: unregelmässige Arbeitszeit/Präsenzpflicht, Auto für Dienstfahrten nötig; sonst nur ÖV; P+R-Parkgebühr = Fahrkosten
- **Beachten:** Geschäftsfahrzeug mit Pauschale 0,9 %/Monat (Lohnausweis Ziff. 2.2): kein Fahrkostenabzug
- **Limiten:**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.75 (Privates Motorfahrzeug (Auto): 75 Rappen je Fahrkilometer, sofern kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung nicht zumutbar ist; im Rahmen des Maximalabzugs von Fr. 8'000.)** · Bund **CHF 0.75 (Privatauto: CHF 0.75 pro Fahrkilometer, nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist; Gesamtmaximum CHF 3'300.)**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **220 Tage (Für die Berechnung des Fahrkostenabzugs wird von 220 Arbeitstagen pro Kalenderjahr (Vollzeitstelle) ausgegangen, sofern nicht eine höhere Anzahl nachgewiesen wird. Homeoffice-Tage und Tage ohne Arbeitsleistung zählen nicht.)** · Bund **n/a – Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 (Maximalabzug, keine Pauschale; bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
  - Fahrkosten Motorrad – Ansatz pro km (CHF): Kanton **CHF 0.75 (Motorräder: 75 Rappen je Fahrkilometer (gleicher Ansatz wie Autos), sofern kein öffentliches Verkehrsmittel zur Verfügung steht oder zumutbar ist.)** · Bund **CHF 0.40 (Motorrad mit weissem Kontrollschild: CHF 0.40 pro Fahrkilometer (nur wenn kein öffentliches Verkehrsmittel zumutbar); Gesamtmaximum CHF 3'300.)**
- **Bund:** Maximum Fr. 3'300; Autos Fr. –.75 pro km (BKV-Anhang 2026).
- **Bemerkung:** Seed bestätigt (0.75/km 2026). Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0009.md) `sg-mb-8-2026__c0009` – «erhöht sich auf 75 Rappen pro Kilometer (bisher 70 Rappen)»
  - [StB 39 Nr. 3 S. 5–6](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0019.md) `sg-stb-39-3__c0019` – «Der einheitliche Kilometeransatz von Fr. --.75 gilt ab der Steuerperiode 2026»
  - [StV SG Art. 18a](../../chunks/sg/2025/sg-stv/sg-stv__art-18a.md) `sg-stv__art-18a` – «kann anstelle der Abrechnung über die tatsächlichen Kosten der privaten Nutzung und des Fahrkostenabzugs nach Art. 18 dieser Verordnung eine pauschale Fahrkostenberechnung vorgenommen werden»
  - [StB 39 Nr. 3 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0004.md) `sg-stb-39-3__c0004` – «bei Entfernung von der nächsten Haltestelle von mehr als 10 Fussminuten»
  - [StB 39 Nr. 3 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0005.md) `sg-stb-39-3__c0005` – «mehr als 60 Minuten pro Tag ausmacht»
  - [StB 39 Nr. 3 S. 1](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0003.md) `sg-stb-39-3__c0003` – «kann sie als notwendige Kosten die Auslagen abziehen, die bei»
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0009.md) `sg-stb-39-3__c0009` – «Sie zählen zu den Fahrkosten»
  - [StB 39 Nr. 3 S. 5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0017.md) `sg-stb-39-3__c0017` – «Wird die Pauschale beansprucht, entfällt die Aufrechnung für den Arbeitsweg, gleichzeitig»
  - [StB 39 Nr. 3 S. 5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0015.md) `sg-stb-39-3__c0015` – «unter Ziff. 2.2 des Lohnausweises»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0044.md) `bund-wl-2a-2026__c0044` – «ist pro Fahrkilometer ein Abzug bis zu 40 Rp.»
  - [StB 39 Nr. 3 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0004.md) `sg-stb-39-3__c0004` – «ist das Park-and-Ride-System zumutbar, sodass die Autokosten nur für die Fahrt zur Haltestelle geltend gemacht werden können»
  - [StB 39 Nr. 3 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0005.md) `sg-stb-39-3__c0005` – «für eine steuerpflichtige Person, die zufolge unregelmässiger Arbeitszeit oder»
  - [StB 39 Nr. 3 S. 2](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0006.md) `sg-stb-39-3__c0006` – «eine Arbeitgeberbescheinigung sowie die entsprechenden»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «das zur Verfügung stellen eines Geschäftsfahrzeugs durch den Arbeitgeber»
  - [StB 39 Nr. 3 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0005.md) `sg-stb-39-3__c0005` – «weil sie es dort für berufliche Fahrten einsetzen muss»

<a id="form-4-ziff-2-1-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.1 – Mehrkosten auswärtige Verpflegung: Fr. 15 pro Hauptmahlzeit/Arbeitstag, max. Fr. 3'200 pro Jahr

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Belege (Pauschale); Arbeitstage ohne Homeoffice
- **Rein:** Keine Belege (Pauschale); Anzahl Arbeitstage mit auswärtiger Hauptmahlzeit · Lohnausweis Feld G → nicht angekreuzt (sonst halber Abzug Ziff. 2.2) · Spesenabrechnung Arbeitgeber → Tage mit vergüteter Verpflegung (Kürzung)
- **Rechnen:** min(Tage × 15; 3'200) (Kanton = Bund); Spesenersatz: × (Arbeitstage − vergütete Tage) / Arbeitstage, z.B. 3'200 × (220 − 44) / 220 = 2'560
- **Regel:** Voller Abzug, wenn wegen grosser Entfernung oder kurzer Essenspause eine Hauptmahlzeit nicht zu Hause eingenommen werden kann; Pauschale gemäss DBG-Ansätzen, höhere Kosten können nicht nachgewiesen werden. Kürzung im Verhältnis der Arbeitstage mit vergüteter Verpflegung (Spesenersatz).
- **Beachten:** Nur Pauschale, kein Nachweis höherer Kosten; Mittagessen muss tatsächlich auswärts eingenommen werden
- **Beachten:** Schicht-/Nachtarbeit: gleiche Pauschale, nicht zusätzlich zum Abzug wegen Entfernung/kurzer Pause
- **Beachten:** Nicht gleichzeitig mit Verpflegungsabzug Wochenaufenthalt; Zwischenverpflegung nicht abziehbar
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswärtige Verpflegung, voller Abzug: Fr. 15 pro Hauptmahlzeit bzw. Tag, max. Fr. 3'200 im Jahr (bei täglicher Heimkehr nicht gleichzeitig mit Wochenaufenthalt). Nachweis höherer Kosten nicht zulässig.)** · Bund **CHF 15 (Auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (in der Regel nur Mittagessen), nur Pauschale zulässig, wenn Hauptmahlzeit wegen grosser Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann oder bei durchgehender Schicht-/Nachtarbeit.)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Voller Abzug auswärtige Verpflegung: max. Fr. 3'200 im Jahr (bei Kürzung für vergütete Mahlzeiten anteilig nach Arbeitstagen).)** · Bund **CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)**
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). StB 39 Nr. 8 Stand 2021 (Ansätze unverändert); Ansätze auch im BKV-Anhang 2026.
- **Quellen:**
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0012.md) `sg-stb-39-8__c0012` – «voller Abzug pro Hauptmahlzeit bzw. 15.--»
  - [StV SG Art. 19](../../chunks/sg/2025/sg-stv/sg-stv__art-19.md) `sg-stv__art-19` – «wenn der Steuerpflichtige wegen grosser Entfernung zwischen Wohn- und Arbeitsstätte oder wegen kurzer Essenspause eine Hauptmahlzeit nicht zu Hause einnehmen kann»
  - [StB 39 Nr. 8 S. 4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0016.md) `sg-stb-39-8__c0016` – «wird der (volle oder halbe) Pauschalabzug im Verhältnis der Arbeitstage mit vergüteter Verpflegung»
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0011.md) `sg-stb-39-8__c0011` – «kann nicht von den Pauschalen abgewichen werden»
  - [StB 39 Nr. 8 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0005.md) `sg-stb-39-8__c0005` – «auch tatsächlich auswärts einnimmt»
  - [StB 39 Nr. 8 S. 2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0006.md) `sg-stb-39-8__c0006` – «Der Abzug für Schicht- oder Nachtarbeit kann nicht zusätzlich zum Abzug für auswärtige»
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0013.md) `sg-stb-39-8__c0013` – «Der Pauschalabzug für auswärtige Verpflegung bei täglicher Heimkehr kann nicht»
  - [StB 39 Nr. 8 S. 2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0007.md) `sg-stb-39-8__c0007` – «Für auswärts eingenommene Zwischenverpflegungen sieht das Steuergesetz keinen»
  - [StB 39 Nr. 8 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0014.md) `sg-stb-39-8__c0014` – «Auf dem Lohnausweis muss in diesem Fall das Feld G angekreuzt sein»

<a id="form-4-ziff-2-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.2 – Verpflegung verbilligt durch Arbeitgeber (Kantine, Lunch-Checks): halber Abzug Fr. 7.50 / max. Fr. 1'600

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Feld G (Kantinenverpflegung / Lunch-Checks / Bezahlung von Mahlzeiten)
- **Rein:** Lohnausweis Feld G angekreuzt → Kantine/Personalrestaurant oder Lunch-Checks · Anzahl Arbeitstage mit auswärtiger Hauptmahlzeit
- **Rechnen:** min(Tage × 7.50; 1'600) (Kanton = Bund)
- **Regel:** Lohnausweis Feld G angekreuzt (Lunch-Checks, verbilligte Mahlzeit im Personalrestaurant – auch wenn nicht bekannt ist, ob davon Gebrauch gemacht wird) → nur halber Verpflegungsabzug (Fr. 7.50 pro Tag, max. Fr. 1'600 im Jahr). Auch bei freiwilligem Verzicht auf die Kantine nur halber Abzug.
- **Beachten:** Halber Abzug auch bei freiwilligem Kantinenverzicht oder Mensa eng mit Arbeitsplatz verbunden; Kantine zu weit → voll
- **Beachten:** Kein Abzug bei Bewertung bzw. Preisen unter den behördlichen Ansätzen für Naturalbezüge (Art. 6 Abs. 3 BKV)
- **Beachten:** Spesenersatz an einzelnen Tagen: Kürzung im Verhältnis der vergüteten Arbeitstage
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Halber Abzug Fr. 7.50 pro Hauptmahlzeit bzw. Tag, wenn Verpflegung im Personalrestaurant möglich ist oder durch angemessenen Arbeitgeberbeitrag verbilligt wird (Lohnausweis Feld G).)** · Bund **CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Halber Abzug bei verbilligter Verpflegung: max. Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)**
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten Buchstabe G»
  - [StV SG Art. 19](../../chunks/sg/2025/sg-stv/sg-stv__art-19.md) `sg-stv__art-19` – «Nur der halbe Abzug ist zulässig, wenn die Verpflegung in einem Personalrestaurant des Arbeitgebers eingenommen werden kann»
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0012.md) `sg-stb-39-8__c0012` – «halber Abzug pro Hauptmahlzeit bzw. 7.50»
  - [StB 39 Nr. 8 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0014.md) `sg-stb-39-8__c0014` – «wenn es für den Arbeitnehmer aufgrund der Distanz unzumutbar ist, die Mahlzeit in der Kantine einzunehmen»
  - [StB 39 Nr. 8 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0015.md) `sg-stb-39-8__c0015` – «steht ihm trotz Verpflegung zu höheren Kosten nur der halbe Abzug zu»
  - [StB 39 Nr. 8 S. 2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0007.md) `sg-stb-39-8__c0007` – «Kein Abzug ist mangels Mehrkosten zulässig, wenn der Arbeitgeber bei der Bewertung von»
  - [StB 39 Nr. 8 S. 4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0016.md) `sg-stb-39-8__c0016` – «wird der (volle oder halbe) Pauschalabzug im Verhältnis der Arbeitstage mit vergüteter Verpflegung»
  - [StB 39 Nr. 8 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0015.md) `sg-stb-39-8__c0015` – «in enger Verbindung mit dem Arbeitsplatz steht»
  - [StB 39 Nr. 8 S. 2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0007.md) `sg-stb-39-8__c0007` – «oder wenn sich der Steuerpflichtige zu Preisen verpflegen kann, die unter diesen»

<a id="form-4-ziff-2-3-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.3 – Schicht-/Nachtarbeit (mind. 8 Stunden durchgehend): Fr. 15 pro Schicht, max. Fr. 3'200

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 «Bemerkungen» (Anzahl Schichttage) oder Arbeitgeberbescheinigung
- **Rein:** Lohnausweis → Ziff. 15 Anzahl Schichttage (freiwillige Angabe des AG) · Arbeitgeberbescheinigung → Schichttage + Arbeitsort (Bund: auf Verlangen, Art. 6 Abs. 5 BKV) · Lohnausweis → Feld G (Kantine/Verbilligung → halber Ansatz)
- **Rechnen:** min(Schichttage × 15; 3'200); Feld G (Kantine/Verbilligung): min(Tage × 7.50; 1'600) – Kanton = Bund
- **Regel:** Als Schichtarbeit gilt mindestens achtstündige durchgehende Arbeitszeit (gestaffelte/unregelmässige Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich). Anzahl Schichttage steht im Lohnausweis Ziff. 15 (freiwillige Angabe des Arbeitgebers). Nicht kumulierbar mit dem Abzug wegen Entfernung/kurzer Pause.
- **Beachten:** Nicht zusätzlich zum Abzug wegen grosser Entfernung/kurzer Essenspause – nur einer der beiden
- **Beachten:** Keine minimale Distanz Wohn-/Arbeitsort nötig; nur Pauschale, Nachweis höherer Kosten ausgeschlossen
- **Beachten:** Gestaffelte/unregelmässige Arbeitszeit nur, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Schicht-/Nachtarbeit (durchgehend; gleichgestellt gestaffelte/unregelmässige Arbeitszeit): gleiche Pauschale wie auswärtige Verpflegung, Fr. 15 pro Tag, max. Fr. 3'200 im Jahr.)** · Bund **CHF 15 (Schicht-/Nachtarbeit: gleiche Pauschale wie auswärtige Verpflegung, CHF 15 pro Tag bzw. max. CHF 3'200 pro Jahr (bei Verbilligung halber Abzug). Gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt (Art. 6 Abs. 4 BKV). Arbeitgeber muss Tage und Arbeitsort auf Verlangen bescheinigen.)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Voller Abzug auswärtige Verpflegung: max. Fr. 3'200 im Jahr (bei Kürzung für vergütete Mahlzeiten anteilig nach Arbeitstagen).)** · Bund **CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Halber Abzug Fr. 7.50 pro Hauptmahlzeit bzw. Tag, wenn Verpflegung im Personalrestaurant möglich ist oder durch angemessenen Arbeitgeberbeitrag verbilligt wird (Lohnausweis Feld G).)** · Bund **CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Halber Abzug bei verbilligter Verpflegung: max. Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)**
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [StB 39 Nr. 8 S. 2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0006.md) `sg-stb-39-8__c0006` – «Als Schichtarbeit gilt eine mindestens achtstündige, durchgehende Arbeitszeit»
  - [StB 39 Nr. 8 S. 2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0006.md) `sg-stb-39-8__c0006` – «kann nicht zusätzlich zum Abzug für auswärtige Verpflegung»
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «die Anzahl im Kalenderjahr geleisteter Schichttage»
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0012.md) `sg-stb-39-8__c0012` – «halber Abzug pro Hauptmahlzeit bzw. 7.50»
  - [StB 39 Nr. 8 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0014.md) `sg-stb-39-8__c0014` – «Auf dem Lohnausweis muss in diesem Fall das Feld G angekreuzt sein»
  - [StB 39 Nr. 8 S. 2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0006.md) `sg-stb-39-8__c0006` – «Der Verpflegungsabzug ist in diesen Fällen nicht abhängig von einer minimalen Entfernung»
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0011.md) `sg-stb-39-8__c0011` – «höhere Kosten anfallen, kann nicht von den Pauschalen abgewichen werden»
  - [BKV Art. 6](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-6-t2.md) `bund-bkv-2026__art-6-t2` – «Der Arbeitgeber muss die Anzahl Tage mit Schicht- oder Nachtarbeit sowie den Arbeitsort auf Verlangen bescheinigen»
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «Zudem können freiwillig Angaben gemacht werden»

<a id="form-4-ziff-3-1-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4 Ziff. 3.1 – Pauschalabzug übrige Berufskosten: Fr. 700 + 10% des Nettolohnes, max. Fr. 2'400

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Nettolohn gemäss Ziff. 1.1 / Lohnausweis Ziff. 11
- **Rein:** Lohnausweis → Ziff. 11 Nettolohn (Kanton: + Ziff. 10.2 Einkäufe zurückrechnen) · Übertrag Total Formular 4 → Formular 1 Ziff. 10.1/10.2 (Code 438 Person 1 / 488 Person 2)
- **Rechnen:** Kanton: min(700 + 10 % × Nettoeinkünfte; 2'400) / Bund: min(max(3 % × Nettolohn; 2'000); 4'000); UJ: × Tage ÷ 360 (Satz: voller Betrag)
- **Regel:** Pauschale Fr. 700 zuzüglich 10% der Nettoeinkünfte, höchstens Fr. 2'400 (Nettoeinkünfte = Brutto abzüglich Beiträge nach Art. 45 Abs. 1 Bst. d und f StG, ohne Einkaufsbeiträge). Nachweis höherer Kosten (effektiv) möglich. Bei unterjähriger Steuerpflicht anteilig (MB 8/2026: Formular 4 Ziff. 3.1).
- **Beachten:** Kanton: Nettoeinkünfte = Brutto − Beiträge Art. 45 Abs. 1 Bst. d/f StG ohne Einkäufe ⇒ LA Ziff. 11 + Ziff. 10.2
- **Beachten:** Pauschale deckt u.a. Arbeitszimmer; keine Kumulation mit effektiven Kosten
- **Beachten:** Bund: Pauschale bei Teilzeit/Teiljahr angemessen kürzen (Art. 7 Abs. 2 BKV)
- **Limiten:**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockel der Pauschale für übrige Berufskosten: Fr. 700 (zuzüglich 10 % der Nettoeinkünfte).)** · Bund **n/a – Formel ohne fixen Anteil (3 % des Nettolohns, min. 2'000, max. 4'000).**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Übrige Berufskosten: Pauschale Fr. 700 zuzüglich 10 % der Nettoeinkünfte, höchstens Fr. 2'400. Nachweis höherer notwendiger Kosten bleibt vorbehalten. Nettoeinkünfte = Bruttoeinkünfte abzüglich AHV/BVG-/Sozialversicherungsprämien nach Art. 45 Abs. 1 lit. d und f StG (ohne Einkäufe).)** · Bund **3 % (Übrige Berufskosten: Pauschale 3 % des Nettolohns, mindestens CHF 2'000, höchstens CHF 4'000 pro Jahr; Nachweis höherer tatsächlicher Kosten möglich. Bei Teilzeit/Teiljahr angemessen zu kürzen.)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Pauschale für übrige Berufskosten: höchstens Fr. 2'400.)** · Bund **CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **n/a – Formel 700 + 10 % kennt kein Minimum (Art. 21 Abs. 1 StV SG).** · Bund **CHF 2'000 (Mindestbetrag der Pauschale übrige Berufskosten.)**
- **Bund:** 3% des Nettolohnes, mind. Fr. 2'000, max. Fr. 4'000 (BKV-Anhang 2026).
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [StV SG Art. 21](../../chunks/sg/2025/sg-stv/sg-stv__art-21.md) `sg-stv__art-21` – «Für übrige notwendige Berufskosten werden Fr. 700.– zuzüglich 10 Prozent der Nettoeinkünfte, höchstens Fr. 2400.– abgezogen»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Berufskosten ( Formular 4, Ziffer 3.1 und 5.1 )»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «10.1 Person 1 Formular 4 438»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «10.2 Person 2 Formular 4 488»
  - [BKV Anhang](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__anhang-1.md) `bund-bkv-2026__anhang-1` – «3 % des Nettolohns, mindestens im Jahr»
  - [BKV Art. 7](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-7.md) `bund-bkv-2026__art-7` – «Der Pauschalabzug ist angemessen zu kürzen, wenn die unselbständige Erwerbstätigkeit bloss während eines Teils des Jahres oder als Teilzeitarbeit ausgeübt wird»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «vom Bruttolohn total (Ziffer 8) das Total der Abzüge (Ziffer 9 und 10) abgezogen wird»
  - [StB 39 Nr. 1 S. 1](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0001.md) `sg-stb-39-1__c0001` – «Sie gelten grundsätzlich als mit der Pauschale abgegolten.»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Fr. 10’800 ÷ 360 × 180 Tage»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «der Dauer der Steuerpflicht zu kürzen. Zur Satzbestimmung werden jedoch die»

<a id="form-4-ziff-3-2-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4 Ziff. 3.2 – Tatsächliche übrige Berufskosten anstelle Pauschale (Code 418 Person 1 / 468 Person 2)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Aufstellung/Beiblatt mit Belegen; Spesenreglement
- **Rein:** Rechnungen/Quittungen → Σ notwendige Berufsauslagen (Werkzeug, EDV, Fachliteratur, Berufskleider) · Mietvertrag bzw. Schätzung Eigenmietwert → Arbeitszimmeranteil · Spesenreglement / Lohnausweis Ziff. 13 → vom Arbeitgeber vergütete Auslagen (Abgleich)
- **Rechnen:** Σ belegte notwendige Kosten statt Pauschale; Arbeitszimmer = (Miete inkl. NK bzw. EMW −30 % +10 % NK) ÷ (Zimmer + 2), Teilzeit anteilig nach Einkommen – Kanton = Bund
- **Regel:** Nachweis höherer notwendiger Kosten bleibt vorbehalten (Art. 39 Abs. 2 StG; Art. 21 Abs. 3 StV). Ersetzt die Pauschale vollständig. Arbeitszimmer: StB 39 Nr. 1. Vom Arbeitgeber ersetzte Spesen (Lohnausweis Ziff. 13) nicht doppelt abziehen.
- **Beachten:** Zimmer nur bei ca. 40 % Arbeitszeit zu Hause (kein AG-Büro), Raum ausgeschieden; Abend-/Wochenendarbeit reicht nicht
- **Beachten:** Übersteigen die Kosten die Pauschale: sämtliche tatsächlichen Aufwendungen nachweisen (keine Kumulation)
- **Beachten:** Bund: vom Arbeitgeber oder Dritten übernommene Aufwendungen nicht abziehbar (Art. 1 Abs. 2 BKV)
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). Code 418/468 laut Formular 4/2025 (nicht für 2026 bestätigt).
- **Quellen:**
  - [StV SG Art. 21](../../chunks/sg/2025/sg-stv/sg-stv__art-21.md) `sg-stv__art-21` – «Der Nachweis höherer notwendiger Kosten bleibt vorbehalten»
  - [StG SG Art. 39](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-39.md) `sg-stg-2026__art-39` – «dem Steuerpflichtigen steht im Falle von Abs. 1 Bst. c dieser Bestimmung der Nachweis höherer Kosten offen»
  - [StB 39 Nr. 1 S. 1](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0001.md) `sg-stb-39-1__c0001` – «welche insgesamt die Pauschale übersteigen, müssen sämtliche tatsächlichen Aufwendungen nachgewiesen werden»
  - [StB 39 Nr. 1 S. 1](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0001.md) `sg-stb-39-1__c0001` – «Eine Kumu- lation der Pauschale mit einem Abzug der tatsächlichen Kosten für ein Arbeitszimmer ist nicht möglich»
  - [StB 39 Nr. 1 S. 1](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0003.md) `sg-stb-39-1__c0003` – «wenn sie ca. 40% der gesamten Arbeitszeit ausmacht»
  - [StB 39 Nr. 1 S. 1](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0003.md) `sg-stb-39-1__c0003` – «muss auch tatsächlich ausgeschieden worden sein»
  - [StB 39 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0005.md) `sg-stb-39-1__c0005` – «die Gesamtkosten durch die Anzahl Zimmer plus zwei geteilt werden»
  - [StB 39 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0005.md) `sg-stb-39-1__c0005` – «./. 30% Eigenmietwertreduktion»
  - [StB 39 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0005.md) `sg-stb-39-1__c0005` – «+ 10% davon für Nebenkosten (oder effektive Nebenkosten)»
  - [StB 39 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0005.md) `sg-stb-39-1__c0005` – «Bei Teilzeitarbeit besteht kein Anspruch auf den vollen Arbeitszimmerabzug»
  - [StB 39 Nr. 1 S. 1](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0004.md) `sg-stb-39-1__c0004` – «vermag die Notwendigkeit eines vorwiegend für berufliche Zwecke ausgeschiedenen»
  - [StB 39 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0006.md) `sg-stb-39-1__c0006` – «die Berechnung erfolgt ebenfalls gleich»
  - [BKV Art. 7](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-7.md) `bund-bkv-2026__art-7` – «Fachliteratur, privates Arbeitszimmer, Berufskleider»
  - [BKV Art. 1](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-1.md) `bund-bkv-2026__art-1` – «Nicht abziehbar sind die vom Arbeitgeber oder einem Dritten übernommenen Aufwendungen»
  - [WL Lohnausweis 2026 S. 15–16](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0039.md) `bund-wl-lohnausweis-2026__c0039` – «In den Feldern der Ziffern 13.1 und 13.2 sind die Vergütungen anzugeben, die Spesenersatz»

<a id="form-4-ziff-4-1-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4 Ziff. 4.1 – Wochenaufenthalt: Unterkunft, ortsübliche Kosten Zimmer

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag/Beleg Zimmer: Monate × Betrag
- **Rein:** Mietvertrag/Mietzinsquittungen Zimmer am Arbeitsort → Monatsmiete × Monate · Belege Heimkehr (ÖV-Abo/km) → Fahrkosten Wohnsitz–Arbeitsort
- **Rechnen:** Σ Monatsmiete Zimmer: ≤ 800/Mt (Städte Zürich, Bern, Basel, Lausanne, Genf, grössere Kurorte), sonst ≤ 500/Mt; Heimkehr bis Max. Kanton 8'000 / Bund 3'300
- **Regel:** Notwendiger Wochenaufenthalt am Arbeitsort: ortsübliche Auslagen für ein Zimmer; allgemein anerkannt Monatsmieten bis Fr. 800 (Zürich, Bern, Basel, Lausanne, Genf, grössere Kurorte) bzw. Fr. 500 sonst. Fahrkosten Heimkehr nach Fahrkostenregeln (Maximum).
- **Beachten:** Nur wenn tägliche Rückkehr nicht möglich/zumutbar; Bund: regelmässige Heimkehr an den Freitagen
- **Beachten:** Zimmer = 1-Zimmerwohnung/Studio; Mehrkosten für höheren Komfort = nicht abziehbare Lebenshaltung
- **Beachten:** Bund: ortsübliche Auslagen für ein Zimmer – Beträge Fr. 800/500 sind SG-Praxis (StB 39 Nr. 5)
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Abziehbar sind die ortsüblichen Mietkosten für ein Zimmer (1-Zimmerwohnung/Studio). Allgemein anerkannt: Monatsmieten bis Fr. 800 in den Städten Zürich, Bern, Basel, Lausanne, Genf und grösseren Kurorten, sonst bis Fr. 500. Komfortmehrkosten sind nicht abziehbar.** · Bund **Wochenaufenthalt: abziehbar sind die ortsüblichen Auslagen für ein Zimmer (nicht eine Wohnung) am Arbeitsort sowie die Fahrkosten der regelmässigen Heimkehr (im Rahmen des Fahrkosten-Maximums).**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 (Maximalabzug, keine Pauschale; bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [StV SG Art. 20](../../chunks/sg/2025/sg-stv/sg-stv__art-20.md) `sg-stv__art-20` – «Als notwendige Mehrkosten der Unterkunft gelten die ortsüblichen Mietkosten für ein Zimmer»
  - [StB 39 Nr. 5 S. 2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0004.md) `sg-stb-39-5__c0004` – «Monatsmieten bis Fr. 800.--, an anderen Orten bis Fr. 500.-- allgemein anerkannt»
  - [StB 39 Nr. 5 S. 2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0004.md) `sg-stb-39-5__c0004` – «In den Städten Zürich, Bern, Basel, Lausanne und Genf sowie in den grösseren Kurorten»
  - [StB 39 Nr. 5 S. 2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0004.md) `sg-stb-39-5__c0004` – «Unter einem Zimmer wird eine 1-Zimmer- wohnung oder ein Studio»
  - [StB 39 Nr. 5 S. 2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0004.md) `sg-stb-39-5__c0004` – «handelt es sich bei den Mehrkosten um nicht abziehbare Lebenshaltungskosten»
  - [StV SG Art. 20](../../chunks/sg/2025/sg-stv/sg-stv__art-20.md) `sg-stv__art-20` – «denen die alltägliche Rückkehr an den steuerrechtlichen Wohnsitz nicht möglich ist oder nicht zugemutet werden kann»
  - [StV SG Art. 20](../../chunks/sg/2025/sg-stv/sg-stv__art-20.md) `sg-stv__art-20` – «Für den Abzug der notwendigen Fahrkosten zwischen Arbeitsort und steuerrechtlichem Wohnsitz wird Art. 18 dieser Verordnung sachgemäss angewendet»
  - [BKV Art. 9](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-9.md) `bund-bkv-2026__art-9` – «jedoch regelmässig für die Freitage an den steuerlichen Wohnsitz zurückkehren»
  - [BKV Art. 9](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-9.md) `bund-bkv-2026__art-9` – «Als notwendige Mehrkosten der Unterkunft sind die ortsüblichen Auslagen für ein Zimmer abziehbar»
  - [BKV Art. 9](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-9.md) `bund-bkv-2026__art-9` – «Sie sind bis zum Maximalbetrag nach Artikel 5 Absatz 1 abziehbar»

<a id="form-4-ziff-4-2-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4 Ziff. 4.2 – Wochenaufenthalt: Verpflegung Fr. 30 pro Arbeitstag, max. Fr. 6'400 pro Jahr (gekürzt Fr. 22.50 / Fr. 4'800)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (bei Verbilligung der Mahlzeiten)
- **Rein:** Aufstellung Arbeitstage am Wochenaufenthaltsort → Tage × Tagesansatz · Lohnausweis → Feld G (verbilligte Mahlzeit/Kantine → gekürzter Ansatz)
- **Rechnen:** voll: min(Tage × 30; 6'400) / gekürzt: min(Tage × 22.50; 4'800) – Kanton = Bund (DBG-Pauschalansätze)
- **Regel:** Pauschale nach DBG-Ansätzen: voll Fr. 30/Tag, Fr. 6'400/Jahr; gekürzt (Mahlzeit vom Arbeitgeber verbilligt oder Kantine möglich) Fr. 22.50/Tag, Fr. 4'800/Jahr. Nicht gleichzeitig mit dem Abzug bei täglicher Heimkehr (Ziff. 2.1).
- **Beachten:** Nicht gleichzeitig mit Verpflegungsabzug bei täglicher Heimkehr
- **Beachten:** Nur Pauschale – Nachweis höherer Kosten ausgeschlossen
- **Beachten:** Gekürzt, wenn eine Hauptmahlzeit vom AG verbilligt oder in Kantine/Personalrestaurant möglich
- **Limiten:**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug Fr. 30 pro Tag, max. Fr. 6'400 im Jahr; gekürzter Abzug Fr. 22.50 pro Tag, max. Fr. 4'800 im Jahr (bei verbilligter Hauptmahlzeit).)** · Bund **CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug CHF 30 pro Tag bzw. CHF 6'400 pro Jahr; gekürzter Abzug (verbilligtes Mittagessen) CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr. Nachweis höherer Kosten ausgeschlossen.)**
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [StB 39 Nr. 5 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0003.md) `sg-stb-39-5__c0003` – «Voller Abzug im Tag 30.00 im Jahr 6'400.00»
  - [StB 39 Nr. 5 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0003.md) `sg-stb-39-5__c0003` – «Der reduzierte Abzug ist anzuwenden, wenn eine der beiden täglichen Hauptmahlzeiten vom Arbeitgeber verbilligt wird»
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0013.md) `sg-stb-39-8__c0013` – «Der Pauschalabzug für auswärtige Verpflegung bei täglicher Heimkehr kann nicht»
  - [StB 39 Nr. 8 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0014.md) `sg-stb-39-8__c0014` – «Auf dem Lohnausweis muss in diesem Fall das Feld G angekreuzt sein»
  - [BKV Art. 9](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-9.md) `bund-bkv-2026__art-9` – «Der Nachweis höherer Kosten ist ausgeschlossen.»
  - [BKV Anhang](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__anhang-1.md) `bund-bkv-2026__anhang-1` – «b. Bei auswärtigem Wochenaufenthalt (Art. 9 Abs. 2)»

<a id="form-4-ziff-5-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 4 Ziff. 5 – Kosten bei unselbständiger Nebenerwerbstätigkeit: 20% der Nettoeinkünfte, mind. Fr. 800, max. Fr. 2'400

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 des Nebenerwerbs (Nettolohn Ziff. 1.2)
- **Rein:** Lohnausweis Nebenerwerb → Ziff. 11 Nettolohn + vergütete Spesen (Form. 1 Ziff. 1.2, Code 104/106) · Arbeitsvertrag Haupterwerb → Pensum (mind. zwei Drittel) · Belege effektive Kosten → nur bei Nachweis höherer Kosten (dann für alle Nebenerwerbe)
- **Rechnen:** min(max(20 % × Σ Nettoeinkünfte aller Nebenerwerbe; 800); 2'400) – Kanton = Bund; Kanton: Einkünfte < 800 → max. = Einkünfte; UJ: × Tage ÷ 360
- **Regel:** Zusatzpauschale für Nebenerwerb neben einem Haupterwerb (mind. 2/3 eines Normalpensums); Nachweis höherer Kosten vorbehalten. Bei unterjähriger Steuerpflicht anteilig (MB 8/2026: Formular 4 Ziff. 5.1).
- **Beachten:** Setzt Haupterwerb von mind. zwei Drittel Normalpensum voraus; einzige Erwerbstätigkeit = Haupterwerb
- **Beachten:** Pauschale deckt auch Fahrkosten und Verpflegung – kein Zusatzabzug dafür
- **Beachten:** Nur unselbständiger Nebenerwerb; Basis = Nettolohn plus Spesenvergütungen
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Unselbständige Nebenerwerbstätigkeit: 20 % der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400 (Pauschalansätze der direkten Bundessteuer). Nachweis höherer notwendiger Kosten vorbehalten.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb: Pauschale mindestens Fr. 800; Nebenerwerbseinkünfte unter Fr. 800 sind nicht betroffen (siehe StB 39 Nr. 9).)** · Bund **CHF 800 (Mindestbetrag Pauschale Nebenerwerb.)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb: Pauschale höchstens Fr. 2'400.)** · Bund **CHF 2'400 (Höchstbetrag Pauschale Nebenerwerb.)**
- **Bund:** 20%, mind. Fr. 800, max. Fr. 2'400 (BKV-Anhang 2026).
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). MB 8/2026 nennt «Ziffer 5.1» (Nummerierung 2025: Ziff. 5).
- **Quellen:**
  - [StB 39 Nr. 9 S. 1](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0002.md) `sg-stb-39-9__c0002` – «sind 20% der Nettoeinkünfte, mindestens Fr. 800.-- und höchstens Fr. 2'400.-- abziehbar»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Berufskosten ( Formular 4, Ziffer 3.1 und 5.1 )»
  - [StB 39 Nr. 9 S. 2](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0005.md) `sg-stb-39-9__c0005` – «wenigstens zwei Drittel einer 100-prozentigen Arbeitszeit entspricht»
  - [StB 39 Nr. 9 S. 2](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0005.md) `sg-stb-39-9__c0005` – «lässt sich die erforderliche Quote dem Arbeitsvertrag entnehmen»
  - [StB 39 Nr. 9 S. 2](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0008.md) `sg-stb-39-9__c0008` – «Ein Erwerbstätiger mit nur einer Beschäftigung führt immer eine Haupterwerbstätigkeit aus»
  - [StB 39 Nr. 9 S. 3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0012.md) `sg-stb-39-9__c0012` – «höchstens ein Pauschalabzug in gleicher Höhe zulässig»
  - [StB 39 Nr. 9 S. 3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0012.md) `sg-stb-39-9__c0012` – «Die Pauschale von 20% errechnet sich aus der Summe aller Nebenerwerbseinkünfte»
  - [StB 39 Nr. 9 S. 3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0013.md) `sg-stb-39-9__c0013` – «schliesst die Nebenerwerbspauschale auch die Fahrkosten und die Mehrkosten der»
  - [StB 39 Nr. 9 S. 3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0010.md) `sg-stb-39-9__c0010` – «Nebenerwerb im Sinn dieser Abzugsregelung ist ausschliesslich eine unselbständige»
  - [StB 39 Nr. 9 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0014.md) `sg-stb-39-9__c0014` – «von diesen Erwerbseinkünften (Nettolohn plus Spesen)»
  - [BKV Anhang](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__anhang-1.md) `bund-bkv-2026__anhang-1` – «20 % der Nettoeinkünfte, mindestens im Jahr»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.2 Aus Nebenerwerbstätigkeit Person 1 Lohnausweis 104»

## Lohnausweis (Regeln für Steuererklärung)

<a id="lohnausweis-feld-f-abzug-berufskosten-fahrkosten"></a>
### Ziff. Lohnausweis Feld F – Lohnausweis Feld F: unentgeltliche Beförderung zwischen Wohn- und Arbeitsort

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld F (Kästchen angekreuzt)
- **Rein:** Lohnausweis → Feld F (Kreuz = keine Arbeitswegkosten) · Lohnausweis → Ziff. 2.2 Privatanteil Geschäftsfahrzeug · Lohnausweis → Ziff. 2.3 vergütete Arbeitswegkosten / privat nützliches GA (Marktwert)
- **Rechnen:** Feld F angekreuzt → Fahrkostenabzug 0; Vergütung in Ziff. 2.3 (kein Kreuz F) → Abzug notwendige Kosten bis Max. Kanton 8'000 / Bund 3'300
- **Regel:** Feld F angekreuzt (z.B. Geschäftsfahrzeug, Sammeltransport, GA aus geschäftlichen Gründen) = dem Arbeitnehmer erwachsen keine Arbeitswegkosten → in Formular 4 KEIN Fahrkostenabzug (bei Pauschal-Geschäftsfahrzeug auch kein Abzug nach Art. 18a StV). Bei privat nützlichem GA (ohne geschäftliche Notwendigkeit): Marktwert unter Lohnausweis Ziff. 2.3, Feld F NICHT angekreuzt, Abzug der Fahrkosten bis Maximum möglich. Vergütete Arbeitswegkosten: Ziff. 2.3, kein Kreuz, Abzug im Formular 4 bis Maximum.
- **Beachten:** Geschäftsauto-Pauschale 0,9 %/Mt Kaufpreis exkl. MWST (mind. 150/Mt, LA 2.2) → kein Fahrkostenabzug; Kanton = Bund
- **Beachten:** GA ohne geschäftliche Notwendigkeit: Marktwert Ziff. 2.3, kein Kreuz F, Kosten Streckenabo in Formular 4
- **Beachten:** Kreuz F u.a. bei Geschäftsfahrzeug, Sammeltransport, Autopauschale Aussendienst, geschäftlich benütztem GA
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 (Maximalabzug, keine Pauschale; bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Bemerkung:** Quelle: bund-wl-lohnausweis-2026 Rz 9, 17; StB 39 Nr. 3 Ziff. 4.1 (SG).
- **Quellen:**
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer keine Kosten für den Arbeitsweg»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0011.md) `bund-wl-lohnausweis-2026__c0011` – «In diesem Fall ist das Feld F nicht anzukreuzen»
  - [WL Lohnausweis 2026 S. 9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0016.md) `bund-wl-lohnausweis-2026__c0016` – «kein Kreuz im Feld F zu setzen»
  - [StB 39 Nr. 3 S. 5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0015.md) `sg-stb-39-3__c0015` – «der Betrag von 0,9% des Kaufpreises des Fahrzeugs»
  - [StB 39 Nr. 3 S. 5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0015.md) `sg-stb-39-3__c0015` – «inkl. sämtlichen Sonderausstattungen (exkl. Mehrwertsteuer) pro Monat»
  - [StB 39 Nr. 3 S. 5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0015.md) `sg-stb-39-3__c0015` – «mindestens aber Fr. 150.-- pro Monat, unter Ziff. 2.2 des Lohnausweises»
  - [StB 39 Nr. 3 S. 5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0015.md) `sg-stb-39-3__c0015` – «eine (identische) Bestimmung ergänzt»
  - [StB 39 Nr. 3 S. 5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0017.md) `sg-stb-39-3__c0017` – «Wird die Pauschale beansprucht, entfällt die Aufrechnung für den Arbeitsweg, gleichzeitig aber auch ein Fahrkostenabzug»
  - [StB 39 Nr. 3 S. 5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0017.md) `sg-stb-39-3__c0017` – «(Art. 18a Abs. 1 StV und Art. 5a Abs. 1 Berufskostenver-»
  - [StB 39 Nr. 3 S. 4](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0013.md) `sg-stb-39-3__c0013` – «dies ist aber nur bis zum Maximalbetrag möglich»
  - [StB 39 Nr. 3 S. 4–5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0014.md) `sg-stb-39-3__c0014` – «Fahrkosten für Streckenabo Fr. -2'025.-- (im Formular 4 geltend zu machen)»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «die Beförderung zum Arbeitsort mittels Sammeltransports»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0011.md) `bund-wl-lohnausweis-2026__c0011` – «Vergütungen einer Autopauschale für Mitarbeitende mit sehr häufigem geschäftlichem»

<a id="lohnausweis-feld-g-abzug-berufskosten-verpflegung"></a>
### Ziff. Lohnausweis Feld G – Lohnausweis Feld G: Kantinenverpflegung / Lunch-Checks / Bezahlung von Mahlzeiten

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (Kästchen angekreuzt)
- **Rein:** Lohnausweis → Feld G (Kantine/Lunch-Checks/verbilligte Mahlzeiten) · Lohnausweis → Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt» · Lohnausweis → Ziff. 1 (Lunch-Checks über AHV-Limite im Lohn)
- **Rechnen:** Feld G: min(Tage × 7.50; 1'600), Wochenaufenthalt min(Tage × 22.50; 4'800) – Kanton = Bund; Kanton: AG-Spesenersatz → × (Arbeitstage − vergütete Tage) ÷ Arbeitstage
- **Regel:** Feld G angekreuzt → Verpflegungsabzug in Formular 4 nur zur Hälfte (Ziff. 2.2: Fr. 7.50/Tag, max. Fr. 1'600) bzw. Wochenaufenthalt gekürzt (Ziff. 4.2). Lunch-Checks bis zur AHV-Limite (Stand 1.1.2022: Fr. 180 pro Monat) nur mit Kreuz in Feld G; darüber hinausgehende Beiträge im Lohn (Ziff. 1). Wer >60% der Arbeitszeit auswärts tätig ist und eine Mittagessensentschädigung erhält: Hinweis in Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt».
- **Beachten:** Lunch-Checks bis AHV-Limite (Stand 1.1.2022: CHF 180/Mt) nur Kreuz G; Mehrbetrag im Lohn Ziff. 1
- **Beachten:** Kreuz G auch bei Mittagsentschädigung und 40–60 % auswärts; > 60 %: nur Vermerk in Ziff. 15
- **Beachten:** Kantine distanzbedingt unzumutbar → voller Abzug; freiwilliger Verzicht auf zumutbare Kantine → nur halber
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Halber Abzug Fr. 7.50 pro Hauptmahlzeit bzw. Tag, wenn Verpflegung im Personalrestaurant möglich ist oder durch angemessenen Arbeitgeberbeitrag verbilligt wird (Lohnausweis Feld G).)** · Bund **CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Halber Abzug bei verbilligter Verpflegung: max. Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug Fr. 30 pro Tag, max. Fr. 6'400 im Jahr; gekürzter Abzug Fr. 22.50 pro Tag, max. Fr. 4'800 im Jahr (bei verbilligter Hauptmahlzeit).)** · Bund **CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug CHF 30 pro Tag bzw. CHF 6'400 pro Jahr; gekürzter Abzug (verbilligtes Mittagessen) CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr. Nachweis höherer Kosten ausgeschlossen.)**
- **Quellen:**
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten Buchstabe G»
  - [WL Lohnausweis 2026 S. 9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0016.md) `bund-wl-lohnausweis-2026__c0016` – «Die Abgabe von Lunch-Checks ist gemäss der Wegleitung über den massgebenden Lohn»
  - [StB 39 Nr. 8 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0014.md) `sg-stb-39-8__c0014` – «Auf dem Lohnausweis muss in diesem Fall das Feld G angekreuzt sein»
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0012.md) `sg-stb-39-8__c0012` – «halber Abzug pro Hauptmahlzeit bzw. 7.50»
  - [StB 39 Nr. 5 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0003.md) `sg-stb-39-5__c0003` – «Reduzierter Abzug im Tag 22.50»
  - [BKV Art. 6](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-6-t1.md) `bund-bkv-2026__art-6-t1` – «Nur der halbe Abzug ist zulässig»
  - [StB 39 Nr. 8 S. 4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0016.md) `sg-stb-39-8__c0016` – «wird der (volle oder halbe) Pauschalabzug im Verhältnis der Arbeitstage mit vergüteter Verpflegung herabgesetzt»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Dieses Feld ist auch anzukreuzen bei Arbeitnehmern, die 40 % - 60 % der Arbeitszeit»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «ausschliesslich unter Ziffer 15 folgender Hinweis anzubringen»
  - [StB 39 Nr. 8 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0014.md) `sg-stb-39-8__c0014` – «wird der volle Abzug gewährt, wenn es für den Arbeitnehmer aufgrund der Distanz unzumutbar ist»
  - [StB 39 Nr. 8 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0015.md) `sg-stb-39-8__c0015` – «steht ihm trotz Verpflegung zu höheren Kosten nur der halbe Abzug zu»

<a id="lohnausweis-ziff-10-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. Lohnausweis Ziff. 10.2 – Lohnausweis Ziff. 10.2: Beiträge für den Einkauf in die berufliche Vorsorge (BVG-Einkauf, bereits vom Lohn abgezogen)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Lohnausweis Ziff. 10.2 (Einkaufsbeiträge)
- **Rein:** Lohnausweis → Ziff. 10.2 Einkauf (nur Info; im Nettolohn Ziff. 11 abgezogen) · Bescheinigung Vorsorgeeinrichtung (Formular 21 EDP) → direkt bezahlter Einkauf · Übertrag → Formular 1 Ziff. 13.2 (Code 218 Person 1 / 219 Person 2)
- **Rechnen:** 13.2 = Σ direkt an VE bezahlte Beiträge/Einkäufe gem. Bescheinigung; LA 10.1/10.2 nicht nochmals, da Ziff. 11 = Ziff. 8 − (Ziff. 9 + 10)
- **Regel:** Vom Lohn abgezogene Einkäufe (Ziff. 10.2) sind im Nettolohn Ziff. 11 bereits abgezogen → in Formular 1 Ziff. 13.2 NICHT nochmals abziehen. Nur direkt bezahlte Einkäufe (Bescheinigung der Vorsorgeeinrichtung, Formular 21 EDP) gehören in Ziff. 13.2.
- **Beachten:** Ziff. 10.2 enthält auch vom AG übernommene AN-Beiträge, sofern in LA Ziff. 7 als Lohn aufgeführt
- **Beachten:** Ordentliche Beiträge Ziff. 10.1 ebenfalls bereits im Nettolohn abgezogen
- **Bemerkung:** Doppelabzugs-Verbot («nochmaliger Abzug unter Ziffer 13.2 ausgeschlossen») stammt aus der WL SG 2025 (jahr_ok; eine WL SG 2026 liegt im Wiki nicht vor, Formular 1/2026 UJ führt Ziff. 13.2 unverändert) – Fachperson prüft für 2026.
- **Quellen:**
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «Beiträge für den Einkauf in die berufliche Vorsorge Ziffer 10.2»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «Beiträge für den Einkauf von fehlenden Versicherungsjahren»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «sind nicht durch den Arbeitgeber im Lohnausweis, sondern durch die Vorsorgeeinrichtung separat mit dem Formular 21 EDP zu bescheinigen»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «dass vom Bruttolohn total (Ziffer 8) das Total der Abzüge (Ziffer»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0086.md) `sg-wl-2025__c0086` – «Deklaration des Nettolohnes»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «13.2 Säule 2 (BVG) inkl. Einkaufsbeiträge Person 1 Bescheinigung 218»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «Zusätzlich sind die vom Arbeitgeber übernommenen Arbeitnehmerbeiträge anzugeben»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «vom Bruttolohn total (Ziffer 8) das Total der Abzüge (Ziffer 9 und 10) abgezogen wird»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «Säule 2 (BVG) inkl. Einkaufsbeiträge Person 2 Bescheinigung 219»

<a id="lohnausweis-ziff-13-3-abzug-weiterbildung"></a>
### Ziff. Lohnausweis Ziff. 13.3 – Lohnausweis Ziff. 13.3: Beiträge des Arbeitgebers für berufsorientierte Aus- und Weiterbildung (inkl. Umschulung)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Lohnausweis Ziff. 13.3
- **Rein:** Lohnausweis → Ziff. 13.3 AG-Vergütungen Weiterbildung · Rechnungen/Zahlungsbelege Kurs/Studium (auf Namen AN) → selbst getragene Kosten · Übertrag → Formular 1 Ziff. 16.4 (Code 223 Person 1 / 224 Person 2)
- **Rechnen:** 16.4 = min(Σ selbst getragene Kosten (Rechnungen − AG-Vergütung LA Ziff. 13.3); 13'000) je Person; Max. Kanton = Bund
- **Regel:** Arbeitgeber-Vergütungen an den Arbeitnehmer für berufsorientierte Weiterbildung (auf Rechnungen auf den Namen des Arbeitnehmers); direkte Zahlungen an Bildungsinstitute werden nicht bescheinigt. Vom Arbeitgeber getragene Kosten sind kein geldwerter Vorteil (Art. 30 Abs. 1bis StG). Kosten, die der Arbeitgeber übernommen/vergütet hat, nicht in Ziff. 16.4 abziehen.
- **Beachten:** AG-getragene Kosten (auch direkt ans Institut): kein Lohn (Art. 30 Abs. 1bis StG); Bund: nur selbst getragene abziehbar
- **Beachten:** Nur mit erstem Abschluss Sek. II oder ab 20 J. (nicht Ausbildung bis erster Abschluss Sek. II)
- **Beachten:** Bund: spätere AG-Rückvergütung früher abgezogener Kosten = Einkommen im Jahr der Rückvergütung
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung: max. Fr. 13'000 je Steuerpflichtigen, wenn erster Abschluss Sekundarstufe II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildungs- inkl. Umschulungskosten bis CHF 13'000 pro Jahr, sofern erster Abschluss Sek. II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)**
- **Quellen:**
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «In diesem Feld sind alle effektiven Vergütungen des Arbeitgebers für berufsorientierte Aus-»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «Nicht anzugeben sind Vergütungen, die direkt an Dritte»
  - [StG SG Art. 30](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-30.md) `sg-stg-2026__art-30` – «stellen unabhängig von deren Höhe keinen anderen geldwerten Vorteil»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.4 Kosten berufsorientierte Aus-/Weiterbildung Person 1 Aufstellung 223»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «Kosten berufsorientierte Aus-/Weiterbildung Person 2 Aufstellung 224»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t4.md) `sg-stg-2026__art-45-t4` – «bis zum Gesamtbetrag von Fr. 13 000.– je Steuerpflichtigen»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t4.md) `sg-stg-2026__art-45-t4` – «das 20. Lebensjahr vollendet ist und es sich nicht um die Ausbildungskosten bis zum ersten Abschluss auf der Sekundarstufe II handelt»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0055.md) `bund-wl-2a-2026__c0055` – «Abziehbar sind die selbstgetragenen Kosten der berufs-»
  - [KS 42 S. 10–11](../../chunks/bund/dauernd/bund-ks-42/bund-ks-42__c0027.md) `bund-ks-42__c0027` – «im Jahr der Rückvergütung als steuerbares Einkommen»
  - [KS 42 S. 10–11](../../chunks/bund/dauernd/bund-ks-42/bund-ks-42__c0028.md) `bund-ks-42__c0028` – «Der Arbeitgeber hat die Rückvergütungen im Lohnausweis in Ziffer 13.3»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «Immer zu bescheinigen sind jedoch effektive Vergütungen für Rechnungen, die auf den Na»

<a id="lohnausweis-ziff-15-abzug-berufskosten-verpflegung"></a>
### Ziff. Lohnausweis Ziff. 15 – Lohnausweis Ziff. 15: Bemerkungen (Anzahl Schichttage, «Einer von x Lohnausweisen», Hinweise)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 «Bemerkungen»
- **Rein:** Lohnausweis → Ziff. 15 Schichttage → Formular 4 Schichtarbeit · Lohnausweis → Ziff. 15 «Einer von x Lohnausweisen» → alle LA desselben AG erfassen · Lohnausweis → Ziff. 15 Kinderzulagen/KK-Beiträge im Bruttolohn (nur Info)
- **Rechnen:** Schicht: min(Schichttage × 15; 3'200); Lohn: Σ Ziff. 11 aller Lohnausweise → Formular 1 Ziff. 1.1 (Code 100/102)
- **Regel:** Freiwillige Angaben: Anzahl geleisteter Schichttage (Grundlage für Schichtarbeit-Verpflegungsabzug, Formular 4 Ziff. 2.3), Höhe Kinderzulagen/Krankenkassenbeiträge im Bruttolohn. Mehrere Lohnausweise vom gleichen Arbeitgeber: Vermerk «Einer von zwei Lohnausweisen» → alle erfassen. Weitere Hinweise: «Privatanteil Geschäftsfahrzeug im Veranlagungsverfahren abzuklären», «Mittagessen durch Arbeitgeber bezahlt».
- **Beachten:** Im Lohn enthaltene Kinderzulagen nicht nochmals in Ziff. 3.5 (Code 142, nur direkt von Ausgleichskasse)
- **Beachten:** «Privatanteil Geschäftsfahrzeug … abzuklären»: AN trägt beträchtliche Kosten, keine Aufrechnung Ziff. 2.2
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Schicht-/Nachtarbeit (durchgehend; gleichgestellt gestaffelte/unregelmässige Arbeitszeit): gleiche Pauschale wie auswärtige Verpflegung, Fr. 15 pro Tag, max. Fr. 3'200 im Jahr.)** · Bund **CHF 15 (Schicht-/Nachtarbeit: gleiche Pauschale wie auswärtige Verpflegung, CHF 15 pro Tag bzw. max. CHF 3'200 pro Jahr (bei Verbilligung halber Abzug). Gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt (Art. 6 Abs. 4 BKV). Arbeitgeber muss Tage und Arbeitsort auf Verlangen bescheinigen.)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Voller Abzug auswärtige Verpflegung: max. Fr. 3'200 im Jahr (bei Kürzung für vergütete Mahlzeiten anteilig nach Arbeitstagen).)** · Bund **CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)**
- **Quellen:**
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «die Anzahl im Kalenderjahr geleisteter Schichttage»
  - [WL Lohnausweis 2026 S. 7–8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0008.md) `bund-wl-lohnausweis-2026__c0008` – «Einer von zwei Lohnausweisen»
  - [WL Lohnausweis 2026 S. 10–11](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0021.md) `bund-wl-lohnausweis-2026__c0021` – «Privatanteil Geschäftsfahrzeug im Veranlagungsverfahren abzuklären»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0004.md) `sg-form-1-2026-uj__c0004` – «3.5 Von Ausgleichskassen direkt ausbezahlte Familienzulagen 142»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.1 Aus Haupterwerbstätigkeit Person 1 Lohnausweis 100»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «Nettolohn Person 2 Lohnausweis 102»
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «Angaben über die Höhe der im Bruttolohn enthalte»
  - [WL Lohnausweis 2026 S. 10–11](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0021.md) `bund-wl-lohnausweis-2026__c0021` – «Übernimmt der Arbeitnehmer beträchtliche Kosten»
  - [WL Lohnausweis 2026 S. 10–11](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0021.md) `bund-wl-lohnausweis-2026__c0021` – «so ist im entsprechenden Feld 2.2 des Lohnausweises keine Aufrechnung vorzunehmen»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «In diesem Feld ist der für die Steuererklärung massgebende Nettolohn anzugeben»

## Hilfsblatt Wertschriften (Formular 2)

<a id="form-2-wertschriftenverzeichnis-einkommen-wertschriften"></a>
### Ziff. Form. 2 (Wertschriftenverzeichnis) – Wertschriften- und Guthabenverzeichnis: Steuerwert → Ziff. 30.1 (Code 300), Erträge → Ziff. 4.1 (Code 146)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Steuerauszug/Bankbescheinigung: Valoren-Nr., Steuerwert 31.12., Bruttoertrag
- **Rein:** Steuerauszug Bank/Depot → Steuerwert 31.12. und Bruttoerträge · Dividendenbelege Beteiligungen ≥ 10 % → Ziff. 4.2 PV (147) / 4.3 GV (149) · Bank-/Depotgebührenbelege → Ziff. 16.1 Verwaltungskosten (Code 220)
- **Rechnen:** 30.1 (300) = Σ Steuerwerte 31.12. bzw. Ende Steuerpflicht; 4.1 (146) = Σ Bruttoerträge; ≥ 10 %: −30 % (4.4/150); 16.1: 2 ‰ bis 3 Mio. + 1 ‰ darüber, max. 15'000
- **Regel:** Formular 2 liefert Steuerwert (Ziff. 30.1) und Erträge (Ziff. 4.1); Verwaltungskosten Ziff. 16.1. Formular 2/2026 nicht publiziert – Spalten/Codes (z.B. VST-Anspruch 35%, Code 999 laut 2025) nicht für 2026 bestätigt.
- **Beachten:** Bund-WL: VSt-belastete Erträge immer deklarieren; WS-Verzeichnis dient i.d.R. als Antrag auf VSt-Rückerstattung (35 %)
- **Beachten:** 16.1: Pauschale oder effektiv (keine Kumulation); Basis ohne Geschäftsvermögen, Darlehen, selbstverwaltete WS
- **Beachten:** UJ: nur effektiv zugeflossene Erträge, keine Marchzinsen; Pauschale 16.1 nach Dauer kürzen; 16.1 Kanton = Bund
- **Bemerkung:** Weitere Zeilen (Code 999, 960–963) bewusst weggelassen: keine 2026-Quelle.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.1 aus Wertschriften und Guthaben 146»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.1 Wertschriften und Guthaben Formular 2 300»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.2 aus Beteiligungen an Gesellschaften ab 10 Prozent (Privatvermögen) 147»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.3 aus Beteiligungen an Gesellschaften ab 10 Prozent (Geschäftsvermögen) 149»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.4 Abzug Teilbesteuerung Beteiligungserträge 150»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Der Abzug beträgt 30 Prozent der»
  - [StG SG Art. 33](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-33-t3.md) `sg-stg-2026__art-33-t3` – «sind im Umfang von 70 Prozent steuerbar, wenn diese Beteiligungsrechte wenigstens 10 Prozent»
  - [DBG Art. 20](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-20-t3.md) `bund-dbg-2026__art-20-t3` – «sind im Umfang von 70 Prozent steuerbar»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.1 Verwaltungskosten für Wertschriften und sonstige Kapitalanlagen 220»
  - [StB 44 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0006.md) `sg-stb-44-1__c0006` – «Die Pauschale beträgt 2 Promille bis zu einem Wertschriftenvermögen von Fr. 3 Mio. und»
  - [StB 44 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0006.md) `sg-stb-44-1__c0006` – «1 Promille auf dem Fr. 3 Mio. übersteigenden Wertschriftenvermögen. Sie ist auf maximal Fr. 15'000.-- begrenzt»
  - [StB 44 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0006.md) `sg-stb-44-1__c0006` – «nach Abzug des Geschäftsvermögens, der Darlehen sowie der selbstverwalteten Wertschriften»
  - [StB 44 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0005.md) `sg-stb-44-1__c0005` – «Eine Kumulation von Pauschalabzug und dem Abzug von»
  - [StB 44 Nr. 1 S. 3–4](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0010.md) `sg-stb-44-1__c0010` – «Es gelten daher die gleichen Abzugsregeln wie im kantonalen Recht»
  - [VStG Art. 13](../../chunks/bund/2025/bund-vstg/bund-vstg__art-13.md) `bund-vstg__art-13` – «35 Prozent der steuerbaren Leistung»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0020.md) `bund-wl-2a-2026__c0020` – «verrechnungssteuerbelastete Einkommen sind immer in der»
  - [WL 2a 2026 S. 3](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0020.md) `bund-wl-2a-2026__c0020` – «gleichzeitig als Antrag auf Rückerstattung der Ver»
  - [MB 8/2026 SG S. 2–3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0005.md) `sg-mb-8-2026__c0005` – «March- oder pro rata temporis Zinsen sind nicht zu deklarieren»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Ziffer 16.1 Verwaltungskosten für Wertschriften und sonstige Kapitalanlagen»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «Steuerwert am 31. Dezember 2026 bzw. am Ende der Steuerpflicht»

## Hilfsblatt Schulden/Zuwendungen (Formular 5)

<a id="form-5-schulden-spenden-schulden-privat"></a>
### Ziff. Form. 5 (Schulden/Spenden) – Formular 5: Schuldzinsen → Ziff. 11 (Code 500); Privatschulden → 34.1 (504); Geschäftsschulden → 34.2 (506); Zuwendungen → 21.3 (244); Parteispenden → 16.3 (555)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht), Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Schuldenausweis Gläubiger (Schuld 31.12.2026, Zinsen 2026); Spendenbestätigungen
- **Rein:** Schuldenausweis Gläubiger → Schuld 31.12.2026 bzw. Ende Steuerpflicht (34.1/504, 34.2/506) und Zinsen (Ziff. 11/500) · Spendenbestätigungen steuerbefreiter Institutionen → Ziff. 21.3 (Code 244) · Belege Parteibeiträge/-spenden → Ziff. 16.3 (Code 555)
- **Rechnen:** 11: min(Schuldzinsen; Vermögensertrag + 50'000); 21.3: min(Σ Zuwendungen; 20 % × Ziff. 20), wenn Σ ≥ 100; 16.3: Kanton ≤ 10'700 / 21'400 Ehepaar, Bund ≤ 10'600
- **Regel:** Übertragsregeln gemäss Formular 1 UJ 2026; materielle Regeln siehe Ziff. 11, 21.3, 16.3, 34.1.
- **Beachten:** Bund 21.3: Basis = um Aufwendungen (Art. 26–33 DBG) verminderte Einkünfte; Schuldzinsen ebenfalls Ertrag + 50'000
- **Beachten:** Parteien nur: im Parteienregister, im kant. Parlament vertreten oder ≥ 3 % Stimmen bei letzten Wahlen
- **Beachten:** Kanton: als Anlagekosten geltende Schuldzinsen nicht in Ziff. 11
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn sie im Steuerjahr Fr. 100 erreichen.)** · Bund **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn im Steuerjahr mindestens CHF 100 erreicht.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: insgesamt höchstens 20 % der Nettoeinkünfte.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'700 (Mitgliederbeiträge und Zuwendungen an politische Parteien: bis Fr. 10'700 für übrige (alleinstehende) Steuerpflichtige.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister / kantonales Parlament / mind. 3 % Stimmen): bis Gesamtbetrag CHF 10'600.)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 21'400 (Parteispenden: bis Fr. 21'400 für gemeinsam steuerpflichtige Ehegatten.)** · Bund **–**
- **Bemerkung:** Formular 5/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «11. Schuldzinsen Formular 5 500»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «34.1 Privatschulden Formular 5 504»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «21.3 Freiwillige Zuwendungen (wenn mind. Fr.100, max. 20% Ziffer 20) Formular 5 244»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t1.md) `sg-stg-2026__art-45-t1` – «soweit sie nicht als Anlagekosten gelten»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t1.md) `sg-stg-2026__art-45-t1` – «steuerbaren Vermögenserträge zuzüglich Fr. 50 000.–»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t1.md) `bund-dbg-2026__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken»
  - [StG SG Art. 46](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-46.md) `sg-stg-2026__art-46` – «wenn diese Leistungen im Steuerjahr Fr. 100.– erreichen, insgesamt höchstens 20 Prozent der Nettoeinkünfte»
  - [DBG Art. 33a](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33a.md) `bund-dbg-2026__art-33a` – «20 Prozent der um die Aufwendungen (Art. 26–33) verminderten Einkünfte nicht übersteigen»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t3.md) `sg-stg-2026__art-45-t3` – «bis zum Gesamtbetrag von Fr. 21 400.– für gemeinsam steuerpflichtige Ehegatten und von Fr. 10 700.– für die übrigen Steuerpflichtigen»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t3.md) `sg-stg-2026__art-45-t3` – «wenigstens 3 Prozent der Stimmen erreicht haben»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.3 Parteispenden Formular 5 555»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «34.2 Geschäftsschulden Formular 5 506»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «Steuerwert am 31. Dezember 2026 bzw. am Ende der Steuerpflicht»

## Hilfsblatt Versicherungen/Krankheitskosten (Formular 6)

<a id="form-6-versicherungen-krankheitskosten-abzug-versicherungspraemien"></a>
### Ziff. Form. 6 (Versicherungen/Krankheitskosten) – Formular 6: Versicherungsprämien → Ziff. 14 (Code 600); Krankheitskosten → 21.1 (650); behinderungsbedingte Kosten → 21.2 (235)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung, Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Prämienrechnung Krankenkasse (brutto), Leistungsabrechnungen, Arztrechnungen
- **Rein:** Prämienabrechnungen Kranken-/Lebens-/Unfallversicherung + Zinsausweise Sparkonten → Ziff. 14 (Code 600) · Arzt-/Zahnarzt-/Spitalrechnungen + KK-Leistungsabrechnungen → ungedeckter Teil Ziff. 21.1 (Code 650) · Belege behinderungsbedingte Kosten → Ziff. 21.2 (Code 235)
- **Rechnen:** 14 = min(Σ Prämien + Sparzinsen; Max): Kanton 6'800/3'400 (ohne 2./3a: 7'900/3'900) + 1'100 je Kind / Bund 3'700/1'800 (ohne: 5'550/2'700) + 700 je Kind
- **Regel:** Übertragsregeln gemäss Formular 1 UJ 2026; Limiten siehe Ziff. 14 (Art. 45 Abs. 1 Bst. g StG) und 21.1 (Selbstbehalt 2%).
- **Beachten:** 21.1 = selbst getragene Kosten − Selbstbehalt (Kanton 2 % × Ziff. 20 / Bund 5 %); 21.2 ohne Selbstbehalt
- **Beachten:** Max. je Ehepaar/übrige; Bund (KS 30): Prämienverbilligung mindert Abzug – nur selbst getragene Prämien
- **Beachten:** UJ: Ziff. 14 × Tage ÷ 360, für den Satz voller Betrag
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 6'800 (Versicherungsprämien (Lebens-, Kranken-, nicht obligatorische Unfallversicherung) und Sparkapitalzinsen: gemeinsam steuerpflichtige Ehegatten bis Fr. 6'800.)** · Bund **CHF 3'700 (Versicherungsprämien und Zinsen von Sparkapitalien, Ehepaare in ungetrennter Ehe, mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 3'700.)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 3'400 (Versicherungsprämien und Sparkapitalzinsen: übrige Steuerpflichtige bis Fr. 3'400.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 1'800.)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 7'900 (Gemeinsam steuerpflichtige Ehegatten ohne Abzug von Beiträgen nach Art. 45 Abs. 1 lit. d und e (2. Säule/3a): Fr. 6'800 + Fr. 1'100 = Fr. 7'900.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an 2. Säule und Säule 3a: Höchstabzug CHF 5'550 (Erhöhung um die Hälfte).)**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 3'900 (Übrige Steuerpflichtige ohne Abzug von Beiträgen nach Art. 45 Abs. 1 lit. d und e (2. Säule/3a): Fr. 3'400 + Fr. 500 = Fr. 3'900.)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: max. CHF 2'700.)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'100 (Erhöhung des Versicherungsabzugs um Fr. 1'100 für jedes Kind, für das ein Kinderabzug geltend gemacht werden kann.)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **2 % (Krankheits- und Unfallkosten sind abziehbar, soweit selbst getragen und über 2 % der Nettoeinkünfte. Behinderungsbedingte Kosten: ohne Selbstbehalt (lit. abis).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
- **Bemerkung:** Formular 6/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «14. Versicherungsprämien und Sparzinsen Formular 6 600»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «21.1 Krankheits- und Unfallkosten Formular 6 650»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «bis zum Gesamtbetrag von Fr. 6800.– für gemeinsam steuerpflichtige Ehegatten und von Fr. 3400.– für die übrigen Steuerpflichtigen»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «Diese Abzüge erhöhen sich um Fr. 1100.– für gemeinsam steuerpflichtige Ehegatten und um Fr. 500.– für die übrigen Steuerpflichtigen»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t2.md) `sg-stg-2026__art-45-t2` – «Sie erhöhen sich um Fr. 1100.– für jedes Kind»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t5.md) `bund-dbg-2026__art-33-t5` – «um die Hälfte für Steuerpflichtige ohne Beiträge nach Absatz 1 Buchstaben d und e»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t5.md) `bund-dbg-2026__art-33-t5` – «um 700 Franken für jedes Kind oder jede unterstützungsbedürftige Person»
  - [StG SG Art. 46](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-46.md) `sg-stg-2026__art-46` – «soweit der Steuerpflichtige die Kosten selbst trägt und diese 2 Prozent der Nettoeinkünfte übersteigen»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «abzüglich Selbstbehalt 2% des Nettoeinkommens (Ziffer 20)»
  - [KS 11 S. 11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0030.md) `bund-ks-11__c0030` – «Im Gegensatz dazu ist bei den behinderungsbedingten Kosten kein Selbstbehalt zu berücksichtigen»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «21.2 Behinderungsbedingte Kosten (ohne Selbstbehalt) Formular 6 235»
  - [KS 30 S. 12](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0031.md) `bund-ks-30__c0031` – «als aufwandmindernd zu berücksichtigen»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Ziffer 14 Versicherungsprämien und Sparzinsen»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Fr. 10’800 ÷ 360 × 180 Tage»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «der Dauer der Steuerpflicht zu kürzen. Zur Satzbestimmung werden jedoch die»

## Hilfsblatt Liegenschaften (Formular 7)

<a id="form-7-liegenschaften-vermoegen-liegenschaften"></a>
### Ziff. Form. 7 (Liegenschaften) – Formular 7: Erträge → Ziff. 5 (Code 712); Unterhalts- und Verwaltungskosten → 15 (716); Steuerwert → 31 (710)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Schätzungsverfügung (Steuerwert, Mietwert), Mietzinsabrechnung, Unterhaltsrechnungen 2026
- **Rein:** Schätzungsverfügung → Steuerwert (Ziff. 31, Code 710) und Eigenmietwert · Mietzinsabrechnung/Mieterspiegel → Bruttomietertrag (Ziff. 5, Code 712) · Unterhalts-/Verwaltungsrechnungen, Versicherungsprämien 2026 → Ziff. 15 (Code 716)
- **Rechnen:** 5 = Mieten + EMW (Kanton: selbstbewohntes Eigenheim −30 %); 15 = effektiv oder Pauschale Kanton 20 % / Bund 10 % (Gebäude ≤ 10 J. bei Periodenbeginn) bzw. 20 %
- **Regel:** Übertragsregeln gemäss Formular 1 UJ 2026; Regeln siehe Ziff. 5, 15, 31 (Eigenmietwert −30%, Pauschale 20%).
- **Beachten:** Pauschale: Kanton nur vorwiegend Wohnzwecke, Bund nicht bei vorw. geschäftl. Drittnutzung; Wahl je Liegenschaft/Periode
- **Beachten:** Energiespar-/Rückbaukosten: nicht verrechneter Teil in den zwei folgenden Perioden abziehbar (Kanton)
- **Beachten:** StB 044 Nr. 2 ab 01.01.2026: Praxis zum wirtschaftlichen Neubau abgeschafft
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt bei vorwiegend Wohnzwecken dienenden Liegenschaften: 20 % des Bruttomietertrags ohne Nebenkosten oder des angerechneten Eigenmietwerts, anstelle der tatsächlichen Kosten (Wahl pro Periode und Liegenschaft).)** · Bund **10 % (Pauschalabzug Liegenschaftskosten (anstelle effektiver Kosten, Wahl pro Periode und Liegenschaft): 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist.)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Gleicher Pauschalsatz wie bei jüngeren Gebäuden: 20 % des Bruttomietertrags bzw. angerechneten Eigenmietwerts (keine Altersstaffelung in Art. 29 StV).)** · Bund **20 % (Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist.)**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **30 % (Mietwert des Eigenheims, das am Wohnsitz dauernd selbst bewohnt wird, wird um 30 % herabgesetzt; dauerhafter Unternutzung wird auf Antrag Rechnung getragen. Im AHV-Rentenalter weitere Reduktion bei offensichtlichem Missverhältnis (nicht unter 60 % der Marktmiete; Art. 14 StV: Mietwert über 30 % der Bruttoeinkünfte und steuerbares Vermögen höchstens Fr. 600'000).)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Bemerkung:** Formular 7/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Ertrag aus Liegenschaften Formular 7 712»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «15. Unterhalts- und Verwaltungskosten für Liegenschaften Formular 7 716»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «31. Liegenschaften Formular 7 710»
  - [StG SG Art. 34](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-34.md) `sg-stg-2026__art-34` – «Der Mietwert des Eigenheims, das der Steuerpflichtige an seinem Wohnsitz dauernd selbst bewohnt, wird um 30 Prozent herabgesetzt»
  - [StG SG Art. 44](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-44-t1.md) `sg-stg-2026__art-44-t1` – «die Versicherungsprämien und die Kosten der Verwaltung durch Dritte abgezogen werden»
  - [StV SG Art. 29](../../chunks/sg/2025/sg-stv/sg-stv__art-29.md) `sg-stv__art-29` – «Für vorwiegend Wohnzwecken dienende Liegenschaften kann anstelle der tatsächlichen Kosten ein Pauschalabzug von 20 Prozent»
  - [StV SG Art. 29](../../chunks/sg/2025/sg-stv/sg-stv__art-29.md) `sg-stv__art-29` – «für jede Steuerperiode und für jede Liegenschaft zwischen dem Abzug der tatsächlichen Kosten und dem Pauschalabzug wählen»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «mehr als zehn Jahre alt ist: 20 Prozent des Brutto-Mietertrags»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «Ein Pauschalabzug ist ausgeschlossen, wenn die Liegenschaft von Dritten vorwiegend geschäftlich genutzt wird»
  - [StG SG Art. 44](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-44-t1.md) `sg-stg-2026__art-44-t1` – «sind in den zwei nachfolgenden Steuerperioden abziehbar»
  - [StB SG Änderungen 2026 S. 1](../../chunks/sg/2026/sg-stb-aenderungen-2026/sg-stb-aenderungen-2026__c0002.md) `sg-stb-aenderungen-2026__c0002` – «Allgemeine Aktualisierung. Abschaffung der Praxis»
  - [StB SG Änderungen 2026 S. 1](../../chunks/sg/2026/sg-stb-aenderungen-2026/sg-stb-aenderungen-2026__c0002.md) `sg-stb-aenderungen-2026__c0002` – «zum wirtschaftlichen Neubau. Präzisierungen zum»
  - [StB SG Änderungen 2026 S. 1](../../chunks/sg/2026/sg-stb-aenderungen-2026/sg-stb-aenderungen-2026__c0002.md) `sg-stb-aenderungen-2026__c0002` – «StB 044 Nr. 2 Liegenschaftsunterhalt / wertver-»

## Hilfsblatt Kinder (Formular 10)

<a id="form-10-kinderbetreuung-ausbildung-abzug-drittbetreuung"></a>
### Ziff. Form. 10 (Kinderbetreuung/Ausbildung) – Formular 10: Kinderbetreuungskosten → Ziff. 16.2 (Code 258); Ausbildungskosten Kinder → 23.3 (256)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule), Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Rechnungen Kita/Tagesmutter, Ausbildungskosten
- **Rein:** Rechnungen Kita/Tagesfamilie/Hort → Ziff. 16.2 (Code 258), je Kind unter 14 J. · Nachweis Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit → Kausalität Betreuung · Rechnungen Schul-/Ausbildungskosten Kind (selbst getragen) → Ziff. 23.3 (Code 256)
- **Rechnen:** 16.2 = min(Betreuungskosten; Kanton 26'800 / Bund 25'800) je Kind; 23.3 (nur Kanton) = min(max(Ausbildungskosten − 3'200; 0); 13'800) je Kind
- **Regel:** Maxima 2026: Fr. 26'800 je Kind (Betreuung), Fr. 13'800 je Kind (Ausbildungskosten, über Fr. 3'200 Selbstbehalt).
- **Beachten:** 16.2 nur für Kind unter 14 J. im gleichen Haushalt; Kosten kausal zu Erwerb/Ausbildung/Erwerbsunfähigkeit
- **Beachten:** UJ: 16.2 und 23.3 × Tage ÷ 360, Satz voll; 2026 neu: 16.2 max. 26'800, 23.3 max. 13'800
- **Beachten:** Bund: kein Ausbildungskostenabzug – nur Kinderabzug 6'800 (Art. 35 DBG)
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 26'800 (Kinderdrittbetreuungskosten: höchstens Fr. 26'800 je Kind unter 14 Jahren, das im gleichen Haushalt lebt, soweit in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind, höchstens CHF 25'800; Kind unter 14 Jahren im gleichen Haushalt; Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 10'800 (Kinderabzug für Kind in schulischer oder beruflicher Ausbildung (auch volljährig): Fr. 10'800.)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Abzug CHF 6'800 (kein höherer Ausbildungsabzug beim Bund).)**
  - Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF): Kanton **CHF 13'800 (Zusätzlich zum Kinderabzug: höchstens weitere Fr. 13'800 für Ausbildungskosten je Kind in schulischer/beruflicher Ausbildung, soweit vom Steuerpflichtigen selbst getragen und über Fr. 3'200 (Selbstbehalt).)** · Bund **n/a – Bund: kein erhöhter Abzug für auswärtige Ausbildung; einheitlich CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 (Kinder unter 14 Jahren.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat.)**
  - Kinderabzug Grundbetrag (CHF): Kanton **n/a – Art. 48 Abs. 1 lit. a StG SG. Voraussetzung: Steuerpflichtiger kommt zur Hauptsache für den Unterhalt auf und beansprucht keinen Abzug für Unterhaltsbeiträge (Art. 45 Abs. 1 lit. c).** · Bund **CHF 6'800 (Kinderabzug CHF 6'800 pro minderjähriges oder in beruflicher/schulischer Ausbildung stehendes Kind, für dessen Unterhalt die steuerpflichtige Person sorgt; bei getrennter Besteuerung der Eltern hälftig bei gemeinsamer elterlicher Sorge ohne Unterhaltsbeiträge.)**
- **Bemerkung:** Formular 10/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.2 Kinderbetreuungskosten bei Drittbetreuung Formular 10 258»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «23.3 Ausbildungskosten für Kinder in Schule oder Ausbildung Formular 10 256»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t3.md) `sg-stg-2026__art-45-t3` – «die Kosten der Betreuung von Kindern unter 14 Jahren durch Drittpersonen, höchstens Fr. 26 800.– für jedes Kind»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «höchstens weitere Fr. 13 800.– für Ausbildungskosten»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «soweit sie der Steuerpflichtige selbst trägt und sie Fr. 3200.– übersteigen»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «werden die Sozialabzüge anteilmässig gewährt; für die Bestimmung des Steuersatzes werden sie voll angerechnet»
  - [DBG Art. 35](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-35.md) `bund-dbg-2026__art-35` – «6800 Franken für jedes minderjährige oder in der beruflichen oder schulischen Ausbildung stehende Kind»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Ziffer 16.2 Kinderbetreuungskosten»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Ziffer 23 Sozialabzüge»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Fr. 10’800 ÷ 360 × 180 Tage»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0011.md) `sg-mb-8-2026__c0011` – «16.2 Höherer Abzug Kinderbetreuungskosten»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0011.md) `sg-mb-8-2026__c0011` – «Abzug pro Kind neu max. Fr.»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0011.md) `sg-mb-8-2026__c0011` – «23.3 Ausbildungskosten pro Kind in Schule/Ausbildung neu max. Fr.»
