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
- **Regel:** Nettolohn gemäss Lohnausweis Ziff. 11 einsetzen (Bruttolohn Ziff. 8 abzüglich Abzüge Ziff. 9 und 10). Berufskosten separat in Ziff. 10 (Formular 4). Lohnausweis Ziff. 10.2 (BVG-Einkauf) ist im Nettolohn bereits abgezogen: nicht nochmals in Ziff. 13.2. Lohnausweis Ziff. 13.3 (Arbeitgeber-Weiterbildung) ist nicht steuerbar: nicht zusätzlich in Ziff. 16.4 abziehen. Bei unterjähriger Steuerpflicht nur während der Dauer zugeflossene Einkünfte (MB 8/2026).
- **Bemerkung:** Wegleitung 2026 nicht publiziert; Details der Wegleitung 2025 (sg-wl-2025) gelten für 2026 nicht bestätigt.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.1 Aus Haupterwerbstätigkeit Person 1 Lohnausweis 100»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «In diesem Feld ist der für die Steuererklärung massgebende Nettolohn anzugeben»
  - [StG SG Art. 30](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-30.md) `sg-stg-2026__art-30` – «Steuerbar sind alle Einkünfte aus privatrechtlichem oder öffentlich-rechtlichem Arbeitsverhältnis»
  - [MB 8/2026 SG S. 2](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0004.md) `sg-mb-8-2026__c0004` – «pflicht effektiv zugeflossenen Einkünfte und die Aufwendungen zu deklarieren»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Aus Nebenerwerbstätigkeit unselbständig (Code 104 Person 1 / 106 Person 2)

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn) des Nebenarbeitgebers
- **Regel:** Nettolohn Ziff. 11 des Lohnausweises aus Nebenerwerb. Berufskosten-Pauschale für Nebenerwerb im Formular 4 (20% der Nettoeinkünfte, mind. Fr. 800, max. Fr. 2'400 gemäss StB 39 Nr. 9). Nebenerwerb setzt einen Haupterwerb (mind. 2/3 eines Normalpensums) voraus.
- **Bemerkung:** Wegleitung 2026 nicht publiziert; Details der Wegleitung 2025 (sg-wl-2025) gelten für 2026 nicht bestätigt.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.2 Aus Nebenerwerbstätigkeit Person 1 Lohnausweis 104»
  - [StB 39 Nr. 9 S. 1](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0002.md) `sg-stb-39-9__c0002` – «sind 20% der Nettoeinkünfte, mindestens Fr. 800.-- und höchstens Fr. 2'400.-- abziehbar»

<a id="1-3-einkommen-unselbstaendig-vr-honorare"></a>
### Ziff. 1.3 – Sitzungsgelder, VR-Honorare usw. (Code 108 Person 1 / 110 Person 2)

- **Schlüssel:** `einkommen.unselbstaendig.vr_honorare` (VR-Honorare, Sitzungsgelder, Tantiemen (wo separat ausgewiesen, z.B. SG/AR Ziff. 1.3)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Bescheinigung der Gesellschaft/Behörde (bzw. Lohnausweis, falls dort enthalten)
- **Regel:** Entschädigungen für Dienstleistungen jeder Art (z.B. VR- und Behördentätigkeit) gemäss Bescheinigung; nur soweit nicht bereits in Ziff. 1.1/1.2 erfasst (Doppelerfassung vermeiden). Berufskosten nebenamtlicher Behördenmitglieder: pauschal bis Fr. 2'400 oder je Sitzung bis Fr. 60 (max. Fr. 4'000), Art. 22 Abs. 2 StV.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «1.3 Sitzungsgelder, VR-Honorare usw. Person 1 Bescheinigung 108»
  - [StV SG Art. 22](../../chunks/sg/2025/sg-stv/sg-stv__art-22.md) `sg-stv__art-22` – «pauschal bis Fr. 2400.–, oder»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit: Industrie-, Handels-, Gewerbebetriebe, Landwirtschaft, freie Berufe (Code 112 Person 1 / 114 Person 2)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Erfolgsrechnung/Reingewinn der Jahresrechnung (Aufstellung)
- **Regel:** Reingewinn gemäss Jahresrechnung (Bilanz/Erfolgsrechnung beilegen). Steuerbar sind alle Einkünfte aus Handels-, Gewerbe-, Land- und Forstwirtschaftsbetrieb und freien Berufen, inkl. Kapitalgewinne auf Geschäftsvermögen. Betriebsvermögen in Ziff. 32, Geschäftsschulden in Ziff. 34.2.
- **Bemerkung:** Wegleitung 2026 nicht publiziert; Details der Wegleitung 2025 (sg-wl-2025) gelten für 2026 nicht bestätigt.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «2.1 Person 1 112»
  - [StG SG Art. 31](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-31-t1.md) `sg-stg-2026__art-31-t1` – «Steuerbar sind alle Einkünfte aus einem Handels-, Industrie-, Gewerbe-, Land- und Forstwirtschaftsbetrieb»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Aus Kollektiv-, Kommandit- und einfachen Gesellschaften (Code 120 Person 1 / 122 Person 2)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Angaben der Gesellschaft (Anteil am Gewinn)
- **Regel:** Anteil an den Einkünften der Personengesellschaft gemäss Angaben der Gesellschaft; gehört zu den selbständigen Einkünften (Art. 31 StG). Geschäftskapital in Ziff. 32.1.
- **Bemerkung:** Formular 11 (Gesellschaft) für 2026 nicht im Wiki; Zuordnung Ziff. 2.2 laut Formular 1 UJ 2026.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0003.md) `sg-form-1-2026-uj__c0003` – «2.2 Aus Kollektiv-, Kommandit- und einfachen Gesellschaften»
  - [StG SG Art. 31](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-31-t1.md) `sg-stg-2026__art-31-t1` – «Steuerbar sind alle Einkünfte aus einem Handels-, Industrie-, Gewerbe-, Land- und Forstwirtschaftsbetrieb»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV/IV-Renten zu 100% (Code 126 Person 1 / 128 Person 2)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung Ausgleichskasse (Jahresbetrag brutto)
- **Regel:** AHV-/IV-Renten sind voll steuerbar (zu 100%). Ergänzungsleistungen sind steuerfrei (nicht hier, sondern Angabe in Ziff. 8.2).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0004.md) `sg-form-1-2026-uj__c0004` – «3.1 AHV/IV-Renten (zu 100%) Person 1 Bescheinigung 126»
  - [StG SG Art. 35](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-35-t1.md) `sg-stg-2026__art-35-t1` – «Steuerbar sind alle Einkünfte aus der Alters-, Hinterlassenen- und Invalidenversicherung»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen mit steuerbarem Prozentsatz (Code 130 Person 1 / 132 Person 2)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente), Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Rentenbescheinigung Pensionskasse/Versicherer: Jahresrente brutto; steuerbarer Prozentsatz
- **Regel:** Renten der 2. Säule und aus gebundener Selbstvorsorge sind steuerbar; Leibrenten (und Leibrentenversicherungen) nur im Umfang ihres Ertragsanteils. Prozentsatz in der Vorkolonne gemäss Bescheinigung, mehrere Renten in separater Aufstellung.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0004.md) `sg-form-1-2026-uj__c0004` – «3.2 Renten/Pensionen Bescheinigung / Aufstellung»
  - [StG SG Art. 35](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-35-t1.md) `sg-stg-2026__art-35-t1` – «Leibrentenversicherungen sowie Leibrenten- und Verpfründungsverträge sind im Umfang ihres Ertragsanteils steuerbar»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigung (Taggelder Kranken-, Unfall-, Invalidenversicherung, soweit nicht im Lohnausweis; Code 134 Person 1 / 136 Person 2)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Versicherung / Ausgleichskasse
- **Regel:** Ersatzeinkünfte (Taggelder, EO, Mutterschaftsentschädigung usw.) sind steuerbar, soweit nicht bereits im Lohnausweis (Ziff. 8) enthalten; nur Beträge, die nicht über den Lohnausweis laufen, hier deklarieren.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0004.md) `sg-form-1-2026-uj__c0004` – «3.3 Erwerbsausfallentschädigung Person 1 Bescheinigung 134»
  - [StG SG Art. 36](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-36.md) `sg-stg-2026__art-36` – «alle andern Einkünfte, die an die Stelle des Einkommens aus Erwerbstätigkeit treten»

<a id="3-4-einkommen-ersatz-taggelder"></a>
### Ziff. 3.4 – Arbeitslosen-Taggelder (Code 138 Person 1 / 140 Person 2)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Arbeitslosenkasse
- **Regel:** Arbeitslosentaggelder brutto gemäss Bescheinigung der Arbeitslosenkasse.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0004.md) `sg-form-1-2026-uj__c0004` – «3.4 Arbeitslosen-Taggelder Person 1 Bescheinigung 138»
  - [StG SG Art. 36](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-36.md) `sg-stg-2026__art-36` – «alle andern Einkünfte, die an die Stelle des Einkommens aus Erwerbstätigkeit treten»

<a id="3-5-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.5 – Von Ausgleichskassen direkt ausbezahlte Familienzulagen (Code 142)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung Familienausgleichskasse
- **Regel:** Nur Familienzulagen, die direkt von der Ausgleichskasse ausbezahlt wurden (nicht im Lohnausweis enthalten). Im Lohnausweis (Ziff. 1) enthaltene Kinder-/Familienzulagen sind bereits im Nettolohn.
- **Bemerkung:** Regel „nur direkt ausbezahlte“ ergibt sich aus Formulartext; Abgrenzung zum Lohnausweis (Zulagen sind Bestandteil des Lohnes) siehe bund-wl-lohnausweis-2026.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0004.md) `sg-form-1-2026-uj__c0004` – «3.5 Von Ausgleichskassen direkt ausbezahlte Familienzulagen 142»

<a id="4-1-einkommen-wertschriften"></a>
### Ziff. 4.1 – Einkünfte aus Wertschriften und Guthaben gemäss Formular 2 (Code 146), inkl. Lotterie-/Geldspielgewinne

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Formular 2 (Wertschriften- und Guthabenverzeichnis): Total Erträge; Steuerauszug/Bankbescheinigung
- **Regel:** Total der Erträge aus Formular 2 übertragen (Zinsen, Dividenden, Erträge aus kollektiven Kapitalanlagen usw.). Beteiligungserträge ab 10% separat in Ziff. 4.2/4.3. Unterjährig: nur zugeflossene Erträge, keine March-/pro-rata-Zinsen (MB 8/2026). Geldspielgewinne: Freibetrag einzelner Grossspiel-/Online-Spielbankengewinne Fr. 1'070'900 (neu 2026 laut MB 8/2026), Einsatzkosten Online-Spiele neu max. Fr. 26'800. Verwaltungskosten Ziff. 16.1.
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

<a id="4-2-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.2 – Erträge aus Beteiligungen an Gesellschaften ab 10 Prozent, Privatvermögen (Code 147)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2: Erträge aus qualifizierten Beteiligungen (Privatvermögen)
- **Regel:** Dividenden aus Beteiligungen von mindestens 10% des Kapitals im Privatvermögen. Teilbesteuerung über den Abzug in Ziff. 4.4 (30% der Einkünfte, d.h. 70% steuerbar).
- **Bemerkung:** Art. 31bis StG regelt die Teilbesteuerung im Geschäftsvermögen; für Privatvermögen gilt das Formular (Abzug 4.4, 30%). Bund: Satz nicht aus 2026-Quelle geprüft.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.2 aus Beteiligungen an Gesellschaften ab 10 Prozent (Privatvermögen) 147»
  - [StG SG Art. 31 bis](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-31bis.md) `sg-stg-2026__art-31bis` – «im Umfang von 70 Prozent steuerbar»

<a id="4-3-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.3 – Erträge aus Beteiligungen an Gesellschaften ab 10 Prozent, Geschäftsvermögen (Code 149)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 2 bzw. verbuchte Beteiligungserträge der Jahresrechnung
- **Regel:** Beteiligungserträge ab 10% im Geschäftsvermögen; Teilbesteuerung (70% steuerbar) über Abzug Ziff. 4.4.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.3 aus Beteiligungen an Gesellschaften ab 10 Prozent (Geschäftsvermögen) 149»
  - [StG SG Art. 31 bis](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-31bis.md) `sg-stg-2026__art-31bis` – «Dividenden, Gewinnanteile, Liquidationsüberschüsse und geldwerte Vorteile aus Aktien»

<a id="4-4-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 4.4 – Abzug Teilbesteuerung Beteiligungserträge (Code 150)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → 30% der Summe Ziff. 4.2 und 4.3
- **Regel:** Abzug (Minuszeile) von 30% der Beteiligungserträge Ziff. 4.2 und 4.3; steuerbar bleiben 70%.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.4 Abzug Teilbesteuerung Beteiligungserträge 150»
  - [StG SG Art. 31 bis](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-31bis.md) `sg-stg-2026__art-31bis` – «im Umfang von 70 Prozent steuerbar»

<a id="5-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. 5 – Ertrag aus Liegenschaften gemäss Formular 7 (Code 712)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Formular 7 «Total Erträge» (Eigenmietwert, Mietzinseinnahmen)
- **Regel:** Eigenmietwert und Mietzinseinnahmen aus Formular 7. Mietwert des dauernd selbst bewohnten Eigenheims am Wohnsitz wird um 30% herabgesetzt (Art. 34 Abs. 3 StG); Unternutzungsabzug nur auf Antrag; Reduktion nur für Steuerpflichtige im ordentlichen AHV-Rentenalter bei offensichtlichem Missverhältnis (Art. 34 Abs. 4 StG; nicht unter 60% der mittleren Marktmiete); Art. 14 StV: Mietwert > 30% der Bruttoeinkünfte und steuerbares Vermögen höchstens Fr. 600'000. Zweit-/Ferienwohnungen und vermietete Objekte: keine Herabsetzung.
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **30 % (Mietwert des Eigenheims, das am Wohnsitz dauernd selbst bewohnt wird, wird um 30 % herabgesetzt; dauerhafter Unternutzung wird auf Antrag Rechnung getragen. Im AHV-Rentenalter weitere Reduktion bei offensichtlichem Missverhältnis (nicht unter 60 % der Marktmiete; Art. 14 StV: Mietwert über 30 % der Bruttoeinkünfte und steuerbares Vermögen höchstens Fr. 600'000).)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Bemerkung:** Formular 7/2026 nicht publiziert (Ausfüllhilfe Formular 7/2025 nicht übertragbar).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Ertrag aus Liegenschaften Formular 7 712»
  - [StG SG Art. 34](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-34.md) `sg-stg-2026__art-34` – «wird um 30 Prozent herabgesetzt»
  - [StB 34 Nr. 1 S. 2–3](../../chunks/sg/dauernd/sg-stb-34-1/sg-stb-34-1__c0008.md) `sg-stb-34-1__c0008` – «Zweitwohnungen, Ferienwohnungen sowie von vermieteten Objekten»
  - [StV SG Art. 14](../../chunks/sg/2025/sg-stv/sg-stv__art-14.md) `sg-stv__art-14` – «das steuerbare Vermögen des Steuerpflichtigen höchstens Fr. 600 000.– beträgt»
  - [StV SG Art. 14](../../chunks/sg/2025/sg-stv/sg-stv__art-14.md) `sg-stv__art-14` – «er 30 Prozent der Bruttoeinkünfte des Steuerpflichtigen übersteigt»

<a id="6-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 6.1 – Unterhaltsbeiträge erhalten: für Steuerpflichtige (Code 154) / für minderjährige Kinder (Code 156)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil bzw. -vereinbarung, Zahlungsnachweise (Jahressumme)
- **Regel:** Erhaltene Unterhaltsbeiträge für sich (Code 154) und für unter der elterlichen Sorge/Obhut stehende Kinder (Code 156) sind voll steuerbar; nur laufende Beiträge (Art. 15 StV). Der Zahler zieht sie in Ziff. 12.1/12.2 ab.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «6.1 Unterhaltsbeiträge für den/die Steuerpflichtige(n) 154»
  - [StG SG Art. 36](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-36.md) `sg-stg-2026__art-36` – «Unterhaltsbeiträge, die ein Steuerpflichtiger bei Scheidung, gerichtlicher oder tatsächlicher Trennung für sich erhält»
  - [StV SG Art. 15](../../chunks/sg/2025/sg-stv/sg-stv__art-15.md) `sg-stv__art-15` – «gelten ausschliesslich die laufenden Beiträge»

<a id="6-2-einkommen-erbschaften-unverteilt"></a>
### Ziff. 6.2 – Ertrag aus unverteilten Erbschaften (Code 158)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung der Erbengemeinschaft (Anteil am Ertrag)
- **Regel:** Anteil am Ertrag der unverteilten Erbschaft (Erbengemeinschaft). Vermögensanteil in Ziff. 30.5. Der Vermögensanfall selbst (Erbschaft/Schenkung) ist steuerfrei (Art. 37 Bst. a StG).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «6.2 Ertrag aus unverteilten Erbschaften 158»
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t1.md) `sg-stg-2026__art-37-t1` – «der Vermögensanfall infolge Erbschaft, Vermächtnis, Schenkung oder güterrechtlicher Auseinandersetzung»

<a id="6-3-einkommen-uebrige"></a>
### Ziff. 6.3 – Übrige Einkünfte (Code 162): Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Urheberrechte, Lizenzen, Patente usw.

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Mitarbeiterbeteiligung (Mitarbeiteraktien, Optionen, Anwartschaften/RSU, Beiblatt zum Lohnausweis), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Aufstellung/Beleg der jeweiligen Einkunftsart
- **Regel:** Alle übrigen steuerbaren Einkünfte mit Angabe der Art. Erwerbsersatz-, Entschädigungs- und Leistungsarten gemäss Art. 36 StG. Mitarbeiterbeteiligungen: geldwerter Vorteil Lohnausweis Ziff. 5 / Beiblatt; vom Arbeitgeber getragene Weiterbildung ist kein geldwerter Vorteil (Art. 30 Abs. 1bis StG).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «6.3 Übrige Einkünfte Arten 162»
  - [StG SG Art. 36](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-36.md) `sg-stg-2026__art-36` – «Entschädigungen für die Aufgabe oder Nichtausübung einer Tätigkeit»

<a id="6-4-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 6.4 – Kapitalabfindungen für wiederkehrende Leistungen für … Jahre (Code 164)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Auszahlungsbetrag und Anzahl Jahre gemäss Bescheinigung
- **Regel:** Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz): Steuer zum Satz, der sich bei entsprechender jährlicher Leistung ergäbe (Art. 51 StG). Kapitalleistungen aus Vorsorge gehören auf Seite 4 (Ziff. 40), nicht hierher.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Kapitalabfindungen für wiederkehrende Leistungen für Jahre 164»
  - [StG SG Art. 51](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-51.md) `sg-stg-2026__art-51` – «wird die Steuer unter Berücksichtigung der übrigen Einkünfte zu dem Satz berechnet»

<a id="7-berechnung-total"></a>
### Ziff. 7 – Total der Einkünfte (Code 168)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Rechenzeile: Summe Ziff. 1 bis 6 (inkl. Abzugszeile 4.4). Ziff. 8 (ergänzende Angaben) zählt nicht mit.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «7. Total der Einkünfte 168»

## Einkünfte (ergänzende Angaben)

<a id="8-1-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 8.1 – Vereinfacht abgerechnete Einkünfte, Bruttolohn (Code 290; nicht im Total der Einkünfte)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Ausgleichskasse (Bruttolohn)
- **Regel:** Nur Information: im vereinfachten Verfahren (Steuern vom Arbeitgeber direkt mit Ausgleichskasse abgerechnet) bezogener Bruttolohn; nicht im Total der Einkünfte zu berücksichtigen.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «8.1 Vereinfacht abgerechnete Einkünfte Bescheinigung 290»
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «Ergänzende Angaben (nicht im Total der Einkünfte zu berücksichtigen)»

<a id="8-2-info-steuerfreie-leistungen"></a>
### Ziff. 8.2 – Ergänzungsleistungen / Überbrückungsleistungen für ältere Arbeitslose (Code 291)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung der Durchführungsstelle
- **Regel:** Nur Angabe, steuerfrei: Ergänzungsleistungen zur AHV/IV sind nicht steuerbar; nicht im Total der Einkünfte.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «8.2 Ergänzungsleistungen / Überbrückungsleistungen für ältere Arbeitslose 291»
  - [StG SG Art. 37](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-37-t2.md) `sg-stg-2026__art-37-t2` – «die Einkünfte aufgrund der Bundesgesetzgebung über Ergänzungsleistungen»

<a id="8-3-info-steuerfreie-leistungen"></a>
### Ziff. 8.3 – Hilflosenentschädigungen (Code 292)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung der Ausgleichskasse/Versicherung
- **Regel:** Nur Angabe (nicht im Total der Einkünfte). Hilflosenentschädigung kann in Ziff. 21.2 als behinderungsbedingte Kosten relevant sein.
- **Bemerkung:** Steuerfreiheit nicht aus einer Rechtsnorm 2026 zitiert; Formular führt Position unter «nicht im Total der Einkünfte».
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0006.md) `sg-form-1-2026-uj__c0006` – «8.3 Hilflosenentschädigungen 292»

## Abzüge

<a id="10-1-berechnung-total"></a>
### Ziff. 10.1 – Berufskosten bei unselbständiger Erwerbstätigkeit Person 1 gemäss Formular 4 (Code 438)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 4 «Total der Berufskosten» Person 1
- **Regel:** Total des Formulars 4 (Fahrkosten bis Fr. 8'000, Verpflegung, Wochenaufenthalt, übrige Berufskosten, Nebenerwerb) übertragen. Pauschalierte Abzüge werden bei unterjähriger Steuerpflicht anteilig gekürzt (MB 8/2026: Ziff. 10, Formular 4 Ziff. 3.1 und 5.1), Fahrkosten-Maximum nicht (StB 39 Nr. 3 Ziff. 3). Einzelheiten siehe Hilfsblatt-Positionen Formular 4 unten.
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 (Maximalabzug, keine Pauschale; bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Pauschale für übrige Berufskosten: höchstens Fr. 2'400.)** · Bund **CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)**
- **Bund:** Fahrkosten max. Fr. 3'300 (Art. 26 Abs. 1 Bst. a DBG); Pauschalen BKV-Anhang 2026.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «10.1 Person 1 Formular 4 438»
  - [StG SG Art. 39](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-39.md) `sg-stg-2026__art-39` – «die notwendigen Kosten für Fahrten zwischen Wohn- und Arbeitsstätte bis zum Betrag von Fr. 8000.–»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Berufskosten ( Formular 4, Ziffer 3.1 und 5.1 )»

<a id="10-2-berechnung-total"></a>
### Ziff. 10.2 – Berufskosten bei unselbständiger Erwerbstätigkeit Person 2 gemäss Formular 4 (Code 488)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 4 «Total der Berufskosten» Person 2
- **Regel:** Wie Ziff. 10.1 für Person 2; jeder unselbständig erwerbende Ehegatte hat eigene Berufskosten (StB 39 Nr. 8 Ziff. 1.1).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «10.2 Person 2 Formular 4 488»
  - [StB 39 Nr. 8 S. 1](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0002.md) `sg-stb-39-8__c0002` – «stehen die Abzüge für Berufskosten (z.B. für auswärtige Verpflegung) jedem unselbständig erwerbenden Ehegatten zu»

<a id="11-abzug-schuldzinsen"></a>
### Ziff. 11 – Schuldzinsen gemäss Formular 5 (Code 500)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 5 Teil A (private Schulden und Schuldzinsen); Schuldenausweis der Bank
- **Regel:** Private Schuldzinsen abziehbar im Umfang der steuerbaren Vermögenserträge (Art. 33, 33bis, 34 StG, inkl. Eigenmietwert) zuzüglich Fr. 50'000. Zinsen der Geschäftsschulden gehören in die Jahresrechnung (Ziff. 2). Die Schuld selbst in Ziff. 34.1.
- **Bund:** Art. 33 Abs. 1 Bst. a DBG: ebenfalls Vermögenserträge zuzüglich 50 000 Franken.
- **Bemerkung:** Formular 5/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «11. Schuldzinsen Formular 5 500»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t1.md) `sg-stg-2026__art-45-t1` – «zuzüglich Fr. 50 000.–»

<a id="12-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.1 – Unterhaltsbeiträge an Geschiedene oder Getrennte (Code 200)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungsurteil/Trennungsvereinbarung (bei erstmaliger Zahlung), Zahlungsnachweise
- **Regel:** Bezahlte laufende Unterhaltsbeiträge an den geschiedenen/getrennt lebenden Ehegatten voll abziehbar; beim Empfänger Einkommen (Ziff. 6.1). Nicht abziehbar: Leistungen in Erfüllung anderer familienrechtlicher Pflichten. Bei erstmaliger Zahlung Urteil/Vereinbarung beilegen.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «12.1 Unterhaltsbeiträge an Geschiedene oder Getrennte Aufstellung 200»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t1.md) `sg-stg-2026__art-45-t1` – «die Unterhaltsbeiträge an den geschiedenen, gerichtlich oder tatsächlich getrennt lebenden Ehegatten»

<a id="12-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.2 – Unterhaltsbeiträge für minderjährige Kinder (Code 202)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise je Kind, Urteil/Vereinbarung
- **Regel:** Unterhaltsbeiträge an den Elternteil für Kinder unter dessen Sorge/Obhut abziehbar; der Zahler kann dann keinen Kinderabzug (Ziff. 23) beanspruchen (Kinderabzug nur, wenn kein Abzug nach Art. 45 Abs. 1 Bst. c StG).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «12.2 Unterhaltsbeiträge für minderjährige Kinder Aufstellung 202»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «keinen Abzug nach Art. 45 Abs. 1 Bst. c dieses Erlasses beansprucht»

<a id="12-3-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.3 – Rentenleistungen (Code 204)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Vertrag/Nachweis dauernde Last bzw. Rentenbescheinigung
- **Regel:** Dauernde Lasten sowie der Ertragsanteil von Leibrenten und Verpfründungsverträgen (ausländische Leibrenten gemäss Art. 35 Abs. 3 Bst. c) abziehbar.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «12.3 Rentenleistungen Aufstellung 204»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t1.md) `sg-stg-2026__art-45-t1` – «die dauernden Lasten sowie der Ertragsanteil nach Art. 35 Abs. 3 Bst. c»

<a id="13-1-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.1 – Ordentliche Beiträge Säule 3a (Code 208 Person 1 / 210 Person 2)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → 3a-Bescheinigung der Vorsorgeeinrichtung: im Jahr 2026 bezahlter Betrag
- **Regel:** Im Steuerjahr 2026 einbezahlte ordentliche 3a-Beiträge gemäss Bescheinigung. Art. 45 Abs. 1 Bst. e StG SG verweist auf anerkannte Formen der gebundenen Selbstvorsorge nach Art. 82 BVG; die Höchstbeträge entsprechen daher dem Bundesrecht (BVV 3, 2026): Fr. 7'258 mit 2. Säule; ohne 2. Säule 20% des Erwerbseinkommens, höchstens Fr. 36'288.
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

<a id="13-1-einkauf-abzug-vorsorge-saeule3a-einkauf"></a>
### Ziff. 13.1 (Einkauf) – Einkaufsbeiträge Säule 3a, Jahr(e) (Code 212 Person 1 / 214 Person 2) – NEU 2026

- **Schlüssel:** `abzug.vorsorge.saeule3a_einkauf` (Einkauf (Nachzahlung) Säule 3a – ab Steuerjahr 2026) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Bescheinigung des Vorsorgeanbieters (Einkauf, Jahr(e) der Lücke)
- **Regel:** NEU 2026: Nachträgliche Einkäufe in die Säule 3a für Lücken ab 1.1.2025 (bis 10 Jahre), Abzug höchstens in Höhe des kleinen 3a-Maximalbetrags (Fr. 7'258 im Jahr 2026, Bundesrecht Art. 7a/7b BVV 3); erstmals in der Steuererklärung 2026. Voraussetzungen: AHV-pflichtiges Einkommen, Jahresbeitrag bereits geleistet, noch kein 3a-Kapital bezogen; Bestätigung des Vorsorgeanbieters beilegen. Jahr(e) der Einzahlung angeben.
- **Limiten:**
  - Säule 3a – Einkauf (Nachzahlung) Regel/Maximum: Kanton **Ab 2025 können fehlende Beiträge bis zu zehn Jahre nachträglich einbezahlt werden. Abzug höchstens kleiner Säule-3a-Maximalbetrag, erstmals mit der Steuererklärung 2026 geltend zu machen. Nur Lücken ab 1.1.2025; Voraussetzungen: AHV-pflichtiges Einkommen, Jahresbeitrag bereits geleistet, noch kein 3a-Kapital bezogen; Bestätigung des Vorsorgeanbieters als Beleg.** · Bund **CHF 7'258 (Einkauf Säule 3a (ab Steuerperiode 2026, für Beitragslücken ab 1.1.2025): zusätzlich zum vollen ordentlichen Beitrag im Einkaufsjahr; max. Summe der Beitragslücken der letzten 10 Jahre (frühestens ab 2025), pro Steuerjahr höchstens CHF 7'258 (8 % des oberen BVG-Grenzbetrags, unabhängig von Zugehörigkeit zur 2. Säule); eine Jahresbeitragslücke nur durch einen einzigen Einkauf ausgleichbar; kein Einkauf nach Bezug einer Altersleistung der Säule 3a (Bezüge ab 5 Jahren vor Referenzalter zählen als Altersleistung).)**
- **Bemerkung:** Betrag des kleinen 3a-Maximalbetrags aus Bundesquelle (werte/bund 2026: saeule3a.einkauf Fr. 7'258); SG-Quelle nennt keinen Betrag.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «Einkaufsbeiträge Säule 3a Jahr(e) Person 1 Bescheinigung 212»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0010.md) `sg-mb-8-2026__c0010` – «erstmals mit der Steuererklärung 2026 im Kanton St. Gallen geltend gemacht werden kann»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0010.md) `sg-mb-8-2026__c0010` – «gung des Vorsorgeanbieters belegt werden»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0051.md) `bund-wl-2a-2026__c0051` – «in jedem Fall aber maximal 7258 Fr.»

<a id="13-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 13.2 – Säule 2 (BVG) inkl. Einkaufsbeiträge (Code 218 Person 1 / 219 Person 2)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Bescheinigung der Vorsorgeeinrichtung (Form. 21 EDP) für selbst entrichtete Einkäufe
- **Regel:** Nur Einkaufsbeiträge/Beiträge, die NICHT bereits vom Lohn abgezogen wurden und im Lohnausweis stehen. Lohnausweis Ziff. 10.2 (vom Lohn abgezogene Einkäufe) ist im Nettolohn (Ziff. 11) bereits berücksichtigt: nicht nochmals abziehen. Vom Arbeitnehmer selbst bezahlte Einkäufe bescheinigt die Vorsorgeeinrichtung separat (Formular 21 EDP).
- **Bemerkung:** Gesetzliche Grundlage: Art. 45 Abs. 1 Bst. d StG (Einlagen, Prämien und Beiträge an Einrichtungen der beruflichen Vorsorge).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «13.2 Säule 2 (BVG) inkl. Einkaufsbeiträge Person 1 Bescheinigung 218»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «Beiträge für den Einkauf in die berufliche Vorsorge Ziffer 10.2»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «sind nicht durch den Arbeitgeber im Lohnausweis, sondern durch die Vorsorgeeinrichtung separat mit dem Formular 21 EDP zu bescheinigen»

<a id="14-abzug-versicherungspraemien"></a>
### Ziff. 14 – Versicherungsprämien und Sparzinsen gemäss Formular 6 (Code 600)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 6 Teil C «Abzug» (niedrigerer Betrag aus tatsächlichen Prämien und Höchstabzug)
- **Regel:** Prämien für Lebens-, Kranken- und nicht obligatorische Unfallversicherung sowie Sparzinsen bis Fr. 6'800 (gemeinsam steuerpflichtige Ehegatten) bzw. Fr. 3'400 (übrige); Zuschläge: + Fr. 1'100 bzw. + Fr. 500, wenn keine Beiträge nach Art. 45 Abs. 1 Bst. d und e (2. Säule/3a) abgezogen werden; + Fr. 1'100 je Kind mit Kinderabzug. Pauschalabzug: bei unterjähriger Steuerpflicht anteilig (MB 8/2026). AHV-/Vorsorgebeiträge sind separat abziehbar (Art. 45 Abs. 1 Bst. d), ebenso EO-/ALV-Beiträge und obligatorische Unfallversicherung (Bst. f).
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

<a id="15-abzug-liegenschaft-unterhalt"></a>
### Ziff. 15 – Unterhalts- und Verwaltungskosten für Liegenschaften gemäss Formular 7 (Code 716)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Formular 7 (Pauschale oder tatsächliche Kosten)
- **Regel:** Wahlrecht je Steuerperiode und Liegenschaft: tatsächliche Kosten (Unterhalt, Instandstellung neu erworbener Grundstücke, Versicherungsprämien, Verwaltung durch Dritte) oder Pauschalabzug 20% des Bruttomietertrags ohne Nebenkosten bzw. des angerechneten Eigenmietwerts (nur vorwiegend Wohnzwecken dienende Liegenschaften). Energiespar-/Umweltinvestitionen und Rückbaukosten gleichgestellt (Vortrag auf 2 Folgeperioden).
- **Bemerkung:** Weisungen zum Liegenschaftsunterhalt per 1.1.2026 überarbeitet (sg-stb-aenderungen-2026), Formular 7/2026 nicht publiziert: Pauschalen/Details prüfen.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «15. Unterhalts- und Verwaltungskosten für Liegenschaften Formular 7 716»
  - [StV SG Art. 29](../../chunks/sg/2025/sg-stv/sg-stv__art-29.md) `sg-stv__art-29` – «Pauschalabzug von 20 Prozent des Bruttomietertrags ohne Nebenkosten oder des angerechneten Eigenmietwerts»
  - [StG SG Art. 44](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-44-t2.md) `sg-stg-2026__art-44-t2` – «einen Pauschalabzug geltend machen»

<a id="16-1-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. 16.1 – Verwaltungskosten für Wertschriften und sonstige Kapitalanlagen (Code 220)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.) → Steuerauszug/Depotgebührenausweis; Kurswert des fremdverwalteten Vermögens
- **Regel:** Kosten der Verwaltung durch Dritte abziehbar (nicht Selbstverwaltung, nicht Anlageberatung/Courtagen). Wahl zwischen tatsächlichen Kosten und widerlegbarer Pauschale: 2 Promille bis Fr. 3 Mio. Wertschriftenvermögen, 1 Promille darüber, max. Fr. 15'000; Bemessungsgrundlage ohne Geschäftsvermögen, Darlehen, selbstverwaltete Titel und Kryptowährungen. Pauschalabzug bei unterjähriger Steuerpflicht anteilig (MB 8/2026).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.1 Verwaltungskosten für Wertschriften und sonstige Kapitalanlagen 220»
  - [StG SG Art. 44](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-44-t1.md) `sg-stg-2026__art-44-t1` – «können die Kosten der Verwaltung durch Dritte»
  - [StB 44 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-44-1/sg-stb-44-1__c0006.md) `sg-stb-44-1__c0006` – «Die Pauschale beträgt 2 Promille bis zu einem Wertschriftenvermögen von Fr. 3 Mio.»

<a id="16-2-abzug-drittbetreuung"></a>
### Ziff. 16.2 – Kinderbetreuungskosten bei Drittbetreuung gemäss Formular 10 (Code 258)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Formular 10: Rechnungen Kita/Tagesmutter, Name/Geburtsdatum Kind
- **Regel:** Betreuungskosten für Kinder unter 14 Jahren durch Drittpersonen, höchstens Fr. 26'800 je Kind (2026, bisher Fr. 26'700), wenn das Kind im gleichen Haushalt lebt und die Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit stehen. Pauschalabzug bei unterjähriger Steuerpflicht anteilig (MB 8/2026).
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 26'800 (Kinderdrittbetreuungskosten: höchstens Fr. 26'800 je Kind unter 14 Jahren, das im gleichen Haushalt lebt, soweit in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind, höchstens CHF 25'800; Kind unter 14 Jahren im gleichen Haushalt; Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 (Kinder unter 14 Jahren.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat.)**
- **Bemerkung:** Formular 10/2026 nicht publiziert. Bund: Kinderdrittbetreuung nicht aus 2026-Quelle geprüft.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.2 Kinderbetreuungskosten bei Drittbetreuung Formular 10 258»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t3.md) `sg-stg-2026__art-45-t3` – «höchstens Fr. 26 800.– für jedes Kind»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0011.md) `sg-mb-8-2026__c0011` – «Kinderbetreuung Abzug pro Kind»

<a id="16-3-abzug-parteispenden"></a>
### Ziff. 16.3 – Parteispenden gemäss Formular 5 (Code 555)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ⚠️ strittig
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Formular 5 Teil B: Bestätigung der Partei (Datum, Partei, Betrag)
- **Regel:** Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister, im kantonalen Parlament vertreten oder mind. 3% Stimmen) bis Fr. 21'400 (gemeinsam steuerpflichtige Ehegatten) bzw. Fr. 10'700 (übrige) laut StG-Jahresversion 2026. ACHTUNG: MB 8/2026 Ziff. 11 nennt unter 16.3 einen «Höheren Abzug Parteispenden», der Betrag fehlt im Quelltext.
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'700 (Mitgliederbeiträge und Zuwendungen an politische Parteien: bis Fr. 10'700 für übrige (alleinstehende) Steuerpflichtige.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister / kantonales Parlament / mind. 3 % Stimmen): bis Gesamtbetrag CHF 10'600.)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 21'400 (Parteispenden: bis Fr. 21'400 für gemeinsam steuerpflichtige Ehegatten.)** · Bund **–**
- **Bund:** Art. 33 Abs. 1 Bst. i DBG: Gesamtbetrag 10 600 Franken.
- **Bemerkung:** Strittig/unklar: StG SG Jahresversion 2026 nennt Fr. 10'700/21'400 (identisch zur Version 2025), MB 8/2026 kündigt «höheren Abzug» an, ohne Betrag (auch im PDF S. 4 fehlt er). Fachperson prüft Original raw/sg/2026/sg-mb-8-2026.pdf bzw. Gesetzessammlung.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.3 Parteispenden Formular 5 555»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t3.md) `sg-stg-2026__art-45-t3` – «bis zum Gesamtbetrag von Fr. 21 400.– für gemeinsam steuerpflichtige Ehegatten und von Fr. 10 700.– für die übrigen Steuerpflichtigen»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0011.md) `sg-mb-8-2026__c0011` – «16.3 Höherer Abzug»

<a id="16-4-abzug-weiterbildung"></a>
### Ziff. 16.4 – Kosten berufsorientierte Aus-/Weiterbildung (Code 223 Person 1 / 224 Person 2)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Aufstellung mit Rechnungsdatum, Bezeichnung, Betrag; Kursrechnungen
- **Regel:** Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis Fr. 13'000 je Steuerpflichtigen (Voraussetzung: erster Abschluss Sek. II oder vollendetes 20. Altersjahr und nicht Ausbildung bis zum ersten Abschluss Sek. II). Vom Arbeitgeber getragene Kosten der berufsorientierten Aus- und Weiterbildung (inkl. Umschulung) sind kein geldwerter Vorteil (Art. 30 Abs. 1bis StG).
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung: max. Fr. 13'000 je Steuerpflichtigen, wenn erster Abschluss Sekundarstufe II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildungs- inkl. Umschulungskosten bis CHF 13'000 pro Jahr, sofern erster Abschluss Sek. II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)**
- **Bund:** Art. 33 Abs. 1 Bst. j DBG (Weiterbildung, Maximum Bund nicht aus 2026-Quelle geprüft).
- **Bemerkung:** Seed «ohne Nachweis 400» für 2026 nicht bestätigt (offen).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «Kosten berufsorientierte Aus-/Weiterbildung Person 2 Aufstellung 224»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t4.md) `sg-stg-2026__art-45-t4` – «bis zum Gesamtbetrag von Fr. 13 000.– je Steuerpflichtigen»
  - [StG SG Art. 30](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-30.md) `sg-stg-2026__art-30` – «Die vom Arbeitgeber getragenen Kosten der berufsorientierten Aus- und Weiterbildung, einschliesslich Umschulungskosten,»

<a id="16-5-abzug-ahv-nichterwerbstaetige"></a>
### Ziff. 16.5 – Übrige Abzüge (Code 222), z.B. AHV-Beiträge Nichterwerbstätiger

- **Schlüssel:** `abzug.ahv_nichterwerbstaetige` (AHV/IV/EO-Beiträge Nichterwerbstätiger u.ä.) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse) → AHV-Beitragsverfügung für Nichterwerbstätige
- **Regel:** Beiträge an die AHV/IV (z.B. als Nichterwerbstätiger) sind nach Gesetz abziehbar; Art der Abzüge angeben.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.5 Übrige Abzüge Arten 222»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t1.md) `sg-stg-2026__art-45-t1` – «Einlagen, Prämien und Beiträge an die Alters-, Hinterlassenen- und Invalidenversicherung und an Einrichtungen der beruflichen Vorsorge»

<a id="17-abzug-zweiverdiener"></a>
### Ziff. 17 – Zweiverdienerabzug (Code 226)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Beilage (beide Ehegatten erwerbstätig)
- **Regel:** Gemeinsam steuerpflichtige Ehegatten: Fr. 500 vom Erwerbseinkommen, das ein Ehegatte unabhängig vom Betrieb des anderen erzielt; gleicher Abzug bei erheblicher Mitarbeit im Betrieb des anderen Ehegatten. Pauschalabzug bei unterjähriger Steuerpflicht anteilig (MB 8/2026).
- **Limiten:**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **n/a – Art. 45 Abs. 2 StG SG kennt nur einen Fixbetrag.** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (Ehepaare in ungetrennter Ehe, beide erwerbstätig).)**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **n/a – Fixbetrag Fr. 500 siehe zweiverdiener.max.** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum.)**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **CHF 500 (Gemeinsam steuerpflichtige Ehegatten: Abzug von Fr. 500 vom Erwerbseinkommen, das ein Ehegatte unabhängig vom Beruf/Geschäft des andern erzielt; gleicher Abzug bei erheblicher Mitarbeit im Beruf/Geschäft des andern Ehegatten.)** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum.)**
- **Bund:** Art. 33 Abs. 2 DBG: 50% des niedrigeren Erwerbseinkommens, mindestens 8 600, höchstens 14 100 Franken.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «17. Zweiverdienerabzug 226»
  - [StG SG Art. 45](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-45-t4.md) `sg-stg-2026__art-45-t4` – «Fr. 500.– abgezogen»

<a id="18-berechnung-total"></a>
### Ziff. 18 – Total der Abzüge (Code 230)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Rechenzeile Total der Abzüge (Ziff. 18, Code 230); welche Ziffern in die Summe eingehen, ist in den vorliegenden Quellen nicht belegt – am Formular prüfen.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «18. Total der Abzüge 230»

## Einkommensberechnung

<a id="20-berechnung-total"></a>
### Ziff. 20 – Nettoeinkommen (Code 234)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile: Ziffer 7 abzüglich Ziffer 18
- **Regel:** Ziff. 7 abzüglich Ziff. 18; Basis für Selbstbehalt Krankheitskosten (2%) und Zuwendungs-Limite (20%).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «20. Nettoeinkommen (Ziffer 7 abzüglich Ziffer 18) 234»

<a id="21-1-abzug-krankheitskosten"></a>
### Ziff. 21.1 – Krankheits- und Unfallkosten gemäss Formular 6 (Code 650), abzüglich Selbstbehalt 2% (Code 238), Abzug (Code 240)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 6 Rückseite: selbst getragene Kosten (Rechnungen abzüglich Kassenleistungen)
- **Regel:** Selbst getragene Krankheits- und Unfallkosten (des Steuerpflichtigen und der von ihm unterhaltenen Personen), soweit sie 2% des Nettoeinkommens (Ziff. 20) übersteigen; Brutto-Total in Code 650, Selbstbehalt in Code 238, Differenz in Code 240.
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **2 % (Krankheits- und Unfallkosten sind abziehbar, soweit selbst getragen und über 2 % der Nettoeinkünfte. Behinderungsbedingte Kosten: ohne Selbstbehalt (lit. abis).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
- **Bund:** Art. 33 Abs. 1 Bst. h DBG: Selbstbehalt 5% der um die Aufwendungen verminderten Einkünfte.
- **Bemerkung:** Formular 6/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «21.1 Krankheits- und Unfallkosten Formular 6 650»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «abzüglich Selbstbehalt 2% des Nettoeinkommens (Ziffer 20)»
  - [StG SG Art. 46](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-46.md) `sg-stg-2026__art-46` – «soweit der Steuerpflichtige die Kosten selbst trägt und diese 2 Prozent der Nettoeinkünfte übersteigen»

<a id="21-2-abzug-behinderungskosten"></a>
### Ziff. 21.2 – Behinderungsbedingte Kosten, ohne Selbstbehalt gemäss Formular 6 (Code 235)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Formular 6 Rückseite: behinderungsbedingte Kosten; Verfügung Hilflosenentschädigung
- **Regel:** Selbst getragene behinderungsbedingte Kosten von Personen mit Behinderung im Sinn des BehiG, ohne Selbstbehalt.
- **Bund:** Art. 33 Abs. 1 Bst. hbis DBG: ebenfalls ohne Selbstbehalt.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «21.2 Behinderungsbedingte Kosten (ohne Selbstbehalt) Formular 6 235»
  - [StG SG Art. 46](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-46.md) `sg-stg-2026__art-46` – «die behinderungsbedingten Kosten des Steuerpflichtigen oder der von ihm unterhaltenen Personen»

<a id="21-3-abzug-spenden"></a>
### Ziff. 21.3 – Freiwillige Zuwendungen gemäss Formular 5 (Code 244)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Formular 5 Rückseite Teil A: Spendenbestätigungen (Datum, Institution, Betrag)
- **Regel:** Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentlicher/gemeinnütziger Zweck) sowie an Bund, Kantone, Gemeinden: wenn im Steuerjahr mind. Fr. 100 erreicht, insgesamt höchstens 20% des Nettoeinkommens (Ziff. 20).
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn sie im Steuerjahr Fr. 100 erreichen.)** · Bund **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn im Steuerjahr mindestens CHF 100 erreicht.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: insgesamt höchstens 20 % der Nettoeinkünfte.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**
- **Bund:** Art. 33a DBG: ab 100 Franken, max. 20% der um die Aufwendungen verminderten Einkünfte.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «21.3 Freiwillige Zuwendungen (wenn mind. Fr.100, max. 20% Ziffer 20) Formular 5 244»
  - [StG SG Art. 46](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-46.md) `sg-stg-2026__art-46` – «höchstens 20 Prozent der Nettoeinkünfte»

<a id="22-berechnung-total"></a>
### Ziff. 22 – Reineinkommen (Code 248)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Ziff. 20 abzüglich Ziff. 21.1 bis 21.3.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «22. Reineinkommen (Ziffer 20 abzüglich Ziffern 21.1 bis 21.3) 248»

<a id="23-1-sozialabzug-kinder"></a>
### Ziff. 23.1 – Kinderabzug für jedes noch nicht schulpflichtige Kind (Fr. 7'600, Code 252)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien Seite 1 (Kinder, für deren Unterhalt zur Hauptsache aufgekommen wird)
- **Regel:** Fr. 7'600 je Kind unter elterlicher Sorge/Obhut, noch nicht schulpflichtig, wenn der Steuerpflichtige zur Hauptsache für den Unterhalt aufkommt und keinen Abzug für Unterhaltsbeiträge (Ziff. 12.2) beansprucht. Stichtag 31.12.2026 bzw. Ende der Steuerpflicht; bei unterjähriger Steuerpflicht anteilig (360-Tage-Methode, MB 8/2026), für den Satz voll.
- **Limiten:**
  - Kinderabzug Vorschulalter (CHF): Kanton **CHF 7'600 (Kinderabzug Fr. 7'600 für jedes unter der elterlichen Sorge oder Obhut stehende Kind, das noch nicht schulpflichtig ist.)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (Art. 35 Abs. 1 lit. a DBG), keine Staffelung nach Alter; siehe sozialabzug.kind.**
- **Bund:** Art. 35 Abs. 1 Bst. a DBG: 6 800 Franken je Kind (minderjährig oder in Ausbildung).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «23.1 Kinderabzug für jedes noch nicht schulpflichtige Kind Fr. 7’600 252»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «Fr. 7600.– für jedes unter der elterlichen Sorge oder Obhut des Steuerpflichtigen stehende Kind»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Kinderabzug für ganzes Kalenderjahr (satzbestimmend)»

<a id="23-2-sozialabzug-kinder"></a>
### Ziff. 23.2 – Kinderabzug für jedes Kind in Schule oder Ausbildung (Fr. 10'800, Code 254)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien Seite 1 (Schule/Ausbildung, Dauer bis)
- **Regel:** Fr. 10'800 je minderjähriges oder volljähriges Kind in schulischer/beruflicher Ausbildung (Unterhalt zur Hauptsache, kein Abzug nach Art. 45 Abs. 1 Bst. c). Bei unterjähriger Steuerpflicht anteilig: Fr. 10'800 ÷ 360 × Tage (MB 8/2026).
- **Limiten:**
  - Kinderabzug Schulalter (CHF): Kanton **CHF 10'800 (Kinderabzug Fr. 10'800 für jedes unter elterlicher Sorge/Obhut stehende oder volljährige Kind in schulischer oder beruflicher Ausbildung (gilt für Schulalter und Ausbildung).)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800, keine Staffelung nach Alter; siehe sozialabzug.kind.**
- **Bund:** Art. 35 Abs. 1 Bst. a DBG: einheitlich 6 800 Franken.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «23.2 Kinderabzug für jedes Kind in Schule oder Ausbildung Fr. 10’800 254»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «Fr. 10 800.– für jedes unter der elterlichen Sorge oder Obhut des Steuerpflichtigen stehende oder volljährige Kind»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Fr. 10’800 ÷ 360 × 180 Tage»

<a id="23-3-sozialabzug-kinder"></a>
### Ziff. 23.3 – Ausbildungskosten für Kinder in Schule oder Ausbildung gemäss Formular 10 (Code 256)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Formular 10: Rechnungen (Semestergebühren, Bücher, Fahrkosten, auswärtige Verpflegung/Unterkunft)
- **Regel:** NEU 2026 höher: Ausbildungskosten je Kind max. Fr. 13'800 (bisher Fr. 13'700), soweit selbst getragen und über Fr. 3'200 (Selbstbehalt).
- **Limiten:**
  - Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF): Kanton **CHF 13'800 (Zusätzlich zum Kinderabzug: höchstens weitere Fr. 13'800 für Ausbildungskosten je Kind in schulischer/beruflicher Ausbildung, soweit vom Steuerpflichtigen selbst getragen und über Fr. 3'200 (Selbstbehalt).)** · Bund **n/a – Bund: kein erhöhter Abzug für auswärtige Ausbildung; einheitlich CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).**
- **Bemerkung:** Formular 10/2026 nicht publiziert. Selbstbehalt Fr. 3'200 laut Art. 48 Abs. 1 Bst. a Ziff. 3 StG. «Bisher Fr. 13'700»: Vorjahreswert aus StG SG 2025 Art. 48 Abs. 1 Bst. a Ziff. 3 (jahr_ok, nur als Vergleich zum Vorjahr).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «23.3 Ausbildungskosten für Kinder in Schule oder Ausbildung Formular 10 256»
  - [StG SG Art. 48](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-48.md) `sg-stg-2026__art-48` – «höchstens weitere Fr. 13 800.– für Ausbildungskosten»
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0011.md) `sg-mb-8-2026__c0011` – «23.3 Ausbildungskosten pro Kind in Schule/Ausbildung neu max.»
  - [StG SG Art. 48](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-48.md) `sg-stg-2025__art-48` – «höchstens weitere Fr. 13 700.– für Ausbildungskosten»

<a id="23-4-sozialabzug-unterstuetzung"></a>
### Ziff. 23.4 – Abzug für unterstützte Personen (nur direkte Bundessteuer, Code 264)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Bedürftigkeit; Name/Adresse, Höhe der Unterstützung
- **Regel:** Gilt nur für die direkte Bundessteuer (nicht Kantons-/Gemeindesteuer): Fr. 6'800 je erwerbsunfähige/beschränkt erwerbsfähige unterstützte Person, wenn die Unterstützung mindestens dem Abzug entspricht; nicht für Ehegatten und Kinder mit Kinderabzug.
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **n/a – Unterstützungsabzug existiert nur bei der direkten Bundessteuer (data/werte/bund). Seed: WL 2025 Ziff. 23.4.** · Bund **CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)**
- **Bund:** Art. 35 Abs. 1 Bst. b DBG: 6 800 Franken.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «23.4 Abzug für unterstützte Personen ja Anzahl Bescheinigung 264»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «Abzug gilt nur für die direkte Bundessteuer»

<a id="24-berechnung-total"></a>
### Ziff. 24 – Steuerbares Einkommen gesamt (Code 268)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Ziff. 22 abzüglich Ziff. 23.1 bis 23.3 (kantonal). Direkte Bundessteuer: eigene Sozialabzüge (Ziff. 23.4 usw.).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «24. Steuerbares Einkommen gesamt (Ziffer 22 abzüglich Ziffern 23.1-23.3) 268»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben gemäss Formular 2 (Code 300)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 «Total» Steuerwert per 31.12.2026 (bzw. Ende der Steuerpflicht)
- **Regel:** Steuerwert am 31.12.2026: Wertpapiere zum Kurswert, sonst innerer Wert; bestrittene Forderungen mit Verlustwahrscheinlichkeit. Erträge in Ziff. 4.1.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.1 Wertschriften und Guthaben Formular 2 300»
  - [StG SG Art. 56](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-56.md) `sg-stg-2026__art-56` – «Wertpapiere werden nach dem Kurswert oder, wenn kein solcher besteht, nach dem inneren Wert bewertet»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 302)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung (Bestand 31.12., Kurswert)
- **Regel:** Bestand per Stichtag zum Verkehrswert; Hausrat und persönliche Gebrauchsgegenstände sind nicht steuerbar.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.2 Bargeld, Gold und andere Edelmetalle Aufstellung 302»
  - [StG SG Art. 54](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-54.md) `sg-stg-2026__art-54` – «Das Vermögen wird zum Verkehrswert bewertet»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen (Code 304)

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Bescheinigung der Versicherungsgesellschaft: Rückkaufswert per 31.12.
- **Regel:** Rückkaufswert per Stichtag; anwartschaftliche oder nicht rückkaufsfähige Ansprüche auf periodische Leistungen sind vermögenssteuerfrei (Art. 63 Abs. 1 Bst. b StG).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.3 Lebens- und Rentenversicherungen Bescheinigung»
  - [StG SG Art. 56](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-56.md) `sg-stg-2026__art-56` – «Lebens- und Rentenversicherungen unterliegen der Vermögenssteuer mit ihrem Rückkaufswert»
  - [StG SG Art. 63](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-63.md) `sg-stg-2026__art-63` – «anwartschaftliche oder nicht rückkaufsfähige Ansprüche auf periodische Leistungen»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge (Code 306)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Fahrzeugausweis/Kaufvertrag: Art, Kaufpreis, Erwerbsjahr
- **Regel:** Art, Kaufpreis und Erwerbsjahr deklarieren; steuerbar ist der Verkehrswert (Bewertung durch Steueramt). Hausrat/persönliche Gebrauchsgegenstände sind steuerfrei, Motorfahrzeuge werden deklariert.
- **Bemerkung:** Bewertungsmethode (Abschreibungssätze) in SG-Quellen 2026 nicht enthalten.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.4 Motorfahrzeuge Art»
  - [StG SG Art. 54](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-54.md) `sg-stg-2026__art-54` – «Das Vermögen wird zum Verkehrswert bewertet»
  - [StG SG Art. 63](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-63.md) `sg-stg-2026__art-63` – «der Hausrat und die persönlichen Gebrauchsgegenstände»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Anteile an unverteilten Erbschaften (Code 308)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung Nachlass / Erbteilungsunterlagen
- **Regel:** Anteil am Nachlass der Erbengemeinschaft zum Verkehrswert; Erträge in Ziff. 6.2.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.5 Anteile an unverteilten Erbschaften Aufstellung 308»
  - [StG SG Art. 54](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-54.md) `sg-stg-2026__art-54` – «Das Vermögen wird zum Verkehrswert bewertet»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte (Code 310): Boote, Reitpferde, Sammlungen; ohne Hausrat und persönliche Gebrauchsgegenstände

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung mit mutmasslichem Verkehrswert
- **Regel:** Hausrat und persönliche Gebrauchsgegenstände sind nicht steuerbar (Art. 63 StG); übrige Werte zum Verkehrswert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.6 Übrige Vermögenswerte Arten 310»
  - [StG SG Art. 63](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-63.md) `sg-stg-2026__art-63` – «der Hausrat und die persönlichen Gebrauchsgegenstände»

<a id="31-vermoegen-liegenschaften"></a>
### Ziff. 31 – Liegenschaften gemäss Formular 7 (Code 710)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Formular 7 Steuerwert gemäss Grundstückschätzung
- **Regel:** Steuerwert gemäss amtlicher Grundstückschätzung (Verkehrswert; überwiegend land-/forstwirtschaftlich genutzte Grundstücke im Geltungsbereich des bäuerlichen Bodenrechts zum Ertragswert, Art. 58 StG). Eigenmietwert in Ziff. 5.
- **Bemerkung:** Formular 7/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «31. Liegenschaften Formular 7 710»
  - [StG SG Art. 57](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-57.md) `sg-stg-2026__art-57` – «Der Verkehrswert von Grundstücken entspricht dem mittleren Preis»
  - [StG SG Art. 58](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-58.md) `sg-stg-2026__art-58` – «überwiegend land- oder forstwirtschaftlich genutzt werden, werden zum Ertragswert bewertet»

<a id="32-1-32-3-vermoegen-uebrige"></a>
### Ziff. 32.1-32.3 – Betriebsvermögen aus selbständiger Erwerbstätigkeit: Geschäftskapital Gesellschaften (Code 314), Aktiven Schlussbilanz (316), landwirtschaftlicher Betrieb Formular 12 (318)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Schlussbilanz (Aktiven), Formular 12 (Landwirtschaft)
- **Regel:** Geschäftsvermögen zum Einkommenssteuerwert (Buchwert ohne Geschäftsliegenschaften; diese in Ziff. 31). Schulden in Ziff. 34.2.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «32.1 Geschäftskapital in Kollektiv-, Kommandit- und einfachen Gesellschaften 314»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «32.3 Vermögen im landwirtschaftlichen Betrieb Formular 12 318»
  - [StG SG Art. 55](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-55.md) `sg-stg-2026__art-55` – «werden zum Einkommenssteuerwert bewertet»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 322)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Summe Ziff. 30 bis 32.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «33. Total der Vermögenswerte 322»

<a id="34-1-schulden-privat"></a>
### Ziff. 34.1 – Privatschulden gemäss Formular 5 (Code 504)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Leasingvertrag Fahrzeug / Leasingraten-Abrechnung → Formular 5 Teil A: Schuld am 31.12.2026 je Gläubiger (Schuldenausweis)
- **Regel:** Nachgewiesene Schulden, für die der Steuerpflichtige allein haftet, voll; Solidar-/Bürgschaftsschulden nur soweit er sie tragen muss. Schuldzinsen in Ziff. 11.
- **Bemerkung:** Formular 5/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «34.1 Privatschulden Formular 5 504»
  - [StG SG Art. 62](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-62.md) `sg-stg-2026__art-62` – «Nachgewiesene Schulden, für die der Steuerpflichtige allein haftet, werden voll abgezogen»

<a id="34-2-schulden-privat"></a>
### Ziff. 34.2 – Geschäftsschulden gemäss Formular 5 (Code 506)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 5 Teil B / Bilanz: Schuld am Bilanzstichtag
- **Regel:** Geschäftsschulden separat von den Privatschulden.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «34.2 Geschäftsschulden Formular 5 506»
  - [StG SG Art. 62](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-62.md) `sg-stg-2026__art-62` – «Nachgewiesene Schulden, für die der Steuerpflichtige allein haftet, werden voll abgezogen»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Reinvermögen (Code 326)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Ziff. 33 abzüglich Ziff. 34.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «35. Reinvermögen (Ziffer 33 abzüglich 34) 326»

<a id="36-1-36-3-vermoegen-sozialabzug"></a>
### Ziff. 36.1-36.3 – Sozialabzüge Vermögen: alleinstehend Fr. 75'000 (Code 330), gemeinsam steuerpflichtige Ehegatten Fr. 150'000 (332), je minderjähriges Kind Fr. 20'000 (334)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien/Kinder Seite 1 (Stichtag 31.12.2026)
- **Regel:** Abzug Fr. 75'000 je Steuerpflichtigen (Ehepaar 150'000) plus Fr. 20'000 je minderjähriges Kind mit Kinderabzug nach Art. 48 Abs. 1 lit. a. Verhältnisse am Ende der Steuerperiode. Einfache Vermögenssteuer 1,7 Promille.
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 75'000 (Sozialabzug vom Reinvermögen: Fr. 75'000 für jeden Steuerpflichtigen.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 150'000 (Gemeinsam steuerpflichtige Ehegatten: Fr. 75'000 für jeden Steuerpflichtigen, somit Fr. 150'000 gemeinsam.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 20'000 (Zusätzlich Fr. 20'000 für jedes minderjährige, unter der elterlichen Sorge oder Obhut stehende Kind, für das ein Kinderabzug nach Art. 48 Abs. 1 lit. a beansprucht werden kann.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «36.1 Abzug für alleinstehende Steuerpflichtige Fr. 75’000 330»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «36.3 Abzug für jedes minderjährige Kind Fr. 20’000 334»
  - [StG SG Art. 64](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-64.md) `sg-stg-2026__art-64` – «für jeden Steuerpflichtigen Fr. 75 000.–»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen gesamt (Code 338)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Ziff. 35 abzüglich Ziff. 36.1 bis 36.3. Einfache Steuer 1,7 Promille; Restbeträge unter Fr. 1'000 fallen ausser Betracht (Art. 65 StG).
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «37. Steuerbares Vermögen gesamt (Ziffer 35 abzüglich Ziffern 36.1 bis 36.3) 338»
  - [StG SG Art. 65](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-65.md) `sg-stg-2026__art-65` – «Die einfache Steuer vom steuerbaren Vermögen beträgt 1,7 Promille»

## Weitere Angaben

<a id="40-1-40-3-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. 40.1-40.3 – Kapitalleistungen aus Vorsorge: aus Säule 3a (40.1), aus 2. Säule (40.2), übrige (40.3)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung / Bank (Auszahlung 2026)
- **Regel:** Kapitalleistungen aus Vorsorge (gebundene 3a, 2. Säule, übrige) werden gesondert und zu einem separaten Satz besteuert (volle Jahressteuer: 2,0% Ehegatten bzw. 2,2% übrige); allgemeine Abzüge und Sozialabzüge werden nicht gewährt. Nicht in Ziff. 6.4 erfassen.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0013.md) `sg-form-1-2026-uj__c0013` – «40.1 aus gebundener Vorsorge Säule 3a Bescheinigung»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0013.md) `sg-form-1-2026-uj__c0013` – «40.2 aus Einrichtungen der beruflichen Vorsorge (2. Säule) Bescheinigung»
  - [StG SG Art. 52](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-52.md) `sg-stg-2026__art-52` – «werden gesondert besteuert»

<a id="41-berechnung-total"></a>
### Ziff. 41 – Total Kapitalleistungen aus Vorsorge (Code 950)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Summe Ziff. 40.1 bis 40.3.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0013.md) `sg-form-1-2026-uj__c0013` – «41. Total Kapitalleistungen aus Vorsorge 950»

## Hilfsblatt Berufskosten (Formular 4)

<a id="form-4-ziff-1-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.1 – Fahrkosten öffentliche Verkehrsmittel (Code 400 Person 1 / 450 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg → ÖV-Abo/Billett-Beleg; Weg von–nach
- **Regel:** Tatsächliche, nachgewiesene Kosten des öffentlichen Verkehrsmittels, höchstens Fr. 8'000 (kantonal; Maximalabzug, keine Pauschale, bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt). Basis 220 Arbeitstage; keine Fahrkosten für Homeoffice-Tage und Tage ohne Arbeitsleistung (bei Abo keine Kürzung). Lohnausweis Feld F angekreuzt = keine Arbeitswegkosten → kein Abzug.
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 (Maximalabzug, keine Pauschale; bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **220 Tage (Für die Berechnung des Fahrkostenabzugs wird von 220 Arbeitstagen pro Kalenderjahr (Vollzeitstelle) ausgegangen, sofern nicht eine höhere Anzahl nachgewiesen wird. Homeoffice-Tage und Tage ohne Arbeitsleistung zählen nicht.)** · Bund **n/a – Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).**
- **Bund:** Maximum Fr. 3'300 (Art. 26 Abs. 1 Bst. a DBG).
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [StB 39 Nr. 3 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0011.md) `sg-stb-39-3__c0011` – «Es handelt sich um einen Maximalabzug und nicht um eine Pauschale»
  - [StG SG Art. 39](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-39.md) `sg-stg-2026__art-39` – «die notwendigen Kosten für Fahrten zwischen Wohn- und Arbeitsstätte bis zum Betrag von Fr. 8000.–»
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0010.md) `sg-stb-39-3__c0010` – «Für Homeoffice-Tage und Tage ohne Arbeitsleistung»

<a id="form-4-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.2 – Fahrkosten Fahrrad, Motorfahrrad, Kleinmotorrad (Code 402 Person 1 / 452 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Belege (Pauschale)
- **Regel:** Pauschal Fr. 700 im Jahr (Fahrrad, Motorfahrrad, Kleinmotorrad bis 50 cm3 mit gelbem Schild), wenn zu Fuss/zur Haltestelle mehr als 10 Minuten nötig sind.
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Pauschale Fr. 700 im Jahr bei Benützung eines Fahrrades, eines Motorfahrrades oder eines Kleinmotorrades.)** · Bund **CHF 700 (Fahrrad, Motorfahrrad, Motorrad mit gelbem Kontrollschild: Pauschale CHF 700 pro Jahr; tatsächliche Kosten können nicht zusätzlich geltend gemacht werden.)**
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0009.md) `sg-stb-39-3__c0009` – «Fr. 700.-- im Jahr bei Benützung eines Fahrrades»
  - [StB 39 Nr. 3 S. 1](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0003.md) `sg-stb-39-3__c0003` – «mehr als 10 Minuten benötigt»

<a id="form-4-ziff-1-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.3 – Fahrkosten Motorfahrzeug (Auto/Motorrad): Fr. 0.75 pro km ab 2026 (Zwischentotal max. Fr. 8'000)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Begründung für Privatfahrzeug, Arbeitstage, km pro Weg; Bordbuch bei Geschäftsfahrzeug
- **Regel:** NEU 2026: Fr. 0.75 je Fahrkilometer (2025: Fr. 0.70), einheitlicher Ansatz. Privatfahrzeug nur, wenn kein ÖV zur Verfügung steht oder dessen Benützung nicht zumutbar ist; sonst nur ÖV-Kosten. Geschäftsfahrzeug mit Privatnutzung: Pauschalberechnung 0,9% des Kaufpreises pro Monat im Lohnausweis Ziff. 2.2 ersetzt zugleich den Fahrkostenabzug (kein Abzug).
- **Limiten:**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.75 (Privates Motorfahrzeug (Auto): 75 Rappen je Fahrkilometer, sofern kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung nicht zumutbar ist; im Rahmen des Maximalabzugs von Fr. 8'000.)** · Bund **CHF 0.75 (Privatauto: CHF 0.75 pro Fahrkilometer, nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist; Gesamtmaximum CHF 3'300.)**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **220 Tage (Für die Berechnung des Fahrkostenabzugs wird von 220 Arbeitstagen pro Kalenderjahr (Vollzeitstelle) ausgegangen, sofern nicht eine höhere Anzahl nachgewiesen wird. Homeoffice-Tage und Tage ohne Arbeitsleistung zählen nicht.)** · Bund **n/a – Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 (Maximalabzug, keine Pauschale; bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Bund:** Maximum Fr. 3'300; Autos Fr. –.75 pro km (BKV-Anhang 2026).
- **Bemerkung:** Seed bestätigt (0.75/km 2026). Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [MB 8/2026 SG S. 4](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0009.md) `sg-mb-8-2026__c0009` – «erhöht sich auf 75 Rappen pro Kilometer (bisher 70 Rappen)»
  - [StB 39 Nr. 3 S. 5–6](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0019.md) `sg-stb-39-3__c0019` – «Der einheitliche Kilometeransatz von Fr. --.75 gilt ab der Steuerperiode 2026»
  - [StV SG Art. 18a](../../chunks/sg/2025/sg-stv/sg-stv__art-18a.md) `sg-stv__art-18a` – «kann anstelle der Abrechnung über die tatsächlichen Kosten der privaten Nutzung und des Fahrkostenabzugs nach Art. 18 dieser Verordnung eine pauschale Fahrkostenberechnung vorgenommen werden»

<a id="form-4-ziff-2-1-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.1 – Mehrkosten auswärtige Verpflegung: Fr. 15 pro Hauptmahlzeit/Arbeitstag, max. Fr. 3'200 pro Jahr

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Belege (Pauschale); Arbeitstage ohne Homeoffice
- **Regel:** Voller Abzug, wenn wegen grosser Entfernung oder kurzer Essenspause eine Hauptmahlzeit nicht zu Hause eingenommen werden kann; Pauschale gemäss DBG-Ansätzen, höhere Kosten können nicht nachgewiesen werden. Kürzung im Verhältnis der Arbeitstage mit vergüteter Verpflegung (Spesenersatz).
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswärtige Verpflegung, voller Abzug: Fr. 15 pro Hauptmahlzeit bzw. Tag, max. Fr. 3'200 im Jahr (bei täglicher Heimkehr nicht gleichzeitig mit Wochenaufenthalt). Nachweis höherer Kosten nicht zulässig.)** · Bund **CHF 15 (Auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (in der Regel nur Mittagessen), nur Pauschale zulässig, wenn Hauptmahlzeit wegen grosser Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann oder bei durchgehender Schicht-/Nachtarbeit.)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Voller Abzug auswärtige Verpflegung: max. Fr. 3'200 im Jahr (bei Kürzung für vergütete Mahlzeiten anteilig nach Arbeitstagen).)** · Bund **CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)**
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). StB 39 Nr. 8 Stand 2021 (Ansätze unverändert); Ansätze auch im BKV-Anhang 2026.
- **Quellen:**
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0012.md) `sg-stb-39-8__c0012` – «voller Abzug pro Hauptmahlzeit bzw. 15.--»
  - [StV SG Art. 19](../../chunks/sg/2025/sg-stv/sg-stv__art-19.md) `sg-stv__art-19` – «wenn der Steuerpflichtige wegen grosser Entfernung zwischen Wohn- und Arbeitsstätte oder wegen kurzer Essenspause eine Hauptmahlzeit nicht zu Hause einnehmen kann»

<a id="form-4-ziff-2-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.2 – Verpflegung verbilligt durch Arbeitgeber (Kantine, Lunch-Checks): halber Abzug Fr. 7.50 / max. Fr. 1'600

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Feld G (Kantinenverpflegung / Lunch-Checks / Bezahlung von Mahlzeiten)
- **Regel:** Lohnausweis Feld G angekreuzt (Lunch-Checks, verbilligte Mahlzeit im Personalrestaurant – auch wenn nicht bekannt ist, ob davon Gebrauch gemacht wird) → nur halber Verpflegungsabzug (Fr. 7.50 pro Tag, max. Fr. 1'600 im Jahr). Auch bei freiwilligem Verzicht auf die Kantine nur halber Abzug.
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Halber Abzug Fr. 7.50 pro Hauptmahlzeit bzw. Tag, wenn Verpflegung im Personalrestaurant möglich ist oder durch angemessenen Arbeitgeberbeitrag verbilligt wird (Lohnausweis Feld G).)** · Bund **CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Halber Abzug bei verbilligter Verpflegung: max. Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)**
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten Buchstabe G»
  - [StV SG Art. 19](../../chunks/sg/2025/sg-stv/sg-stv__art-19.md) `sg-stv__art-19` – «Nur der halbe Abzug ist zulässig, wenn die Verpflegung in einem Personalrestaurant des Arbeitgebers eingenommen werden kann»
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0012.md) `sg-stb-39-8__c0012` – «halber Abzug pro Hauptmahlzeit bzw. 7.50»

<a id="form-4-ziff-2-3-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.3 – Schicht-/Nachtarbeit (mind. 8 Stunden durchgehend): Fr. 15 pro Schicht, max. Fr. 3'200

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 «Bemerkungen» (Anzahl Schichttage) oder Arbeitgeberbescheinigung
- **Regel:** Als Schichtarbeit gilt mindestens achtstündige durchgehende Arbeitszeit (gestaffelte/unregelmässige Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich). Anzahl Schichttage steht im Lohnausweis Ziff. 15 (freiwillige Angabe des Arbeitgebers). Nicht kumulierbar mit dem Abzug wegen Entfernung/kurzer Pause.
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Schicht-/Nachtarbeit (durchgehend; gleichgestellt gestaffelte/unregelmässige Arbeitszeit): gleiche Pauschale wie auswärtige Verpflegung, Fr. 15 pro Tag, max. Fr. 3'200 im Jahr.)** · Bund **CHF 15 (Schicht-/Nachtarbeit: gleiche Pauschale wie auswärtige Verpflegung, CHF 15 pro Tag bzw. max. CHF 3'200 pro Jahr (bei Verbilligung halber Abzug). Gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt (Art. 6 Abs. 4 BKV). Arbeitgeber muss Tage und Arbeitsort auf Verlangen bescheinigen.)**
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [StB 39 Nr. 8 S. 2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0006.md) `sg-stb-39-8__c0006` – «Als Schichtarbeit gilt eine mindestens achtstündige, durchgehende Arbeitszeit»
  - [StB 39 Nr. 8 S. 2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0006.md) `sg-stb-39-8__c0006` – «kann nicht zusätzlich zum Abzug für auswärtige Verpflegung»
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «die Anzahl im Kalenderjahr geleisteter Schichttage»

<a id="form-4-ziff-3-1-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4 Ziff. 3.1 – Pauschalabzug übrige Berufskosten: Fr. 700 + 10% des Nettolohnes, max. Fr. 2'400

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Nettolohn gemäss Ziff. 1.1 / Lohnausweis Ziff. 11
- **Regel:** Pauschale Fr. 700 zuzüglich 10% der Nettoeinkünfte, höchstens Fr. 2'400 (Nettoeinkünfte = Brutto abzüglich Beiträge nach Art. 45 Abs. 1 Bst. d und f StG, ohne Einkaufsbeiträge). Nachweis höherer Kosten (effektiv) möglich. Bei unterjähriger Steuerpflicht anteilig (MB 8/2026: Formular 4 Ziff. 3.1).
- **Limiten:**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockel der Pauschale für übrige Berufskosten: Fr. 700 (zuzüglich 10 % der Nettoeinkünfte).)** · Bund **n/a – Formel ohne fixen Anteil (3 % des Nettolohns, min. 2'000, max. 4'000).**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Übrige Berufskosten: Pauschale Fr. 700 zuzüglich 10 % der Nettoeinkünfte, höchstens Fr. 2'400. Nachweis höherer notwendiger Kosten bleibt vorbehalten. Nettoeinkünfte = Bruttoeinkünfte abzüglich AHV/BVG-/Sozialversicherungsprämien nach Art. 45 Abs. 1 lit. d und f StG (ohne Einkäufe).)** · Bund **3 % (Übrige Berufskosten: Pauschale 3 % des Nettolohns, mindestens CHF 2'000, höchstens CHF 4'000 pro Jahr; Nachweis höherer tatsächlicher Kosten möglich. Bei Teilzeit/Teiljahr angemessen zu kürzen.)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Pauschale für übrige Berufskosten: höchstens Fr. 2'400.)** · Bund **CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)**
- **Bund:** 3% des Nettolohnes, mind. Fr. 2'000, max. Fr. 4'000 (BKV-Anhang 2026).
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [StV SG Art. 21](../../chunks/sg/2025/sg-stv/sg-stv__art-21.md) `sg-stv__art-21` – «Für übrige notwendige Berufskosten werden Fr. 700.– zuzüglich 10 Prozent der Nettoeinkünfte, höchstens Fr. 2400.– abgezogen»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Berufskosten ( Formular 4, Ziffer 3.1 und 5.1 )»

<a id="form-4-ziff-3-2-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4 Ziff. 3.2 – Tatsächliche übrige Berufskosten anstelle Pauschale (Code 418 Person 1 / 468 Person 2)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Aufstellung/Beiblatt mit Belegen; Spesenreglement
- **Regel:** Nachweis höherer notwendiger Kosten bleibt vorbehalten (Art. 39 Abs. 2 StG; Art. 21 Abs. 3 StV). Ersetzt die Pauschale vollständig. Arbeitszimmer: StB 39 Nr. 1. Vom Arbeitgeber ersetzte Spesen (Lohnausweis Ziff. 13) nicht doppelt abziehen.
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). Code 418/468 laut Formular 4/2025 (nicht für 2026 bestätigt).
- **Quellen:**
  - [StV SG Art. 21](../../chunks/sg/2025/sg-stv/sg-stv__art-21.md) `sg-stv__art-21` – «Der Nachweis höherer notwendiger Kosten bleibt vorbehalten»
  - [StG SG Art. 39](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-39.md) `sg-stg-2026__art-39` – «dem Steuerpflichtigen steht im Falle von Abs. 1 Bst. c dieser Bestimmung der Nachweis höherer Kosten offen»

<a id="form-4-ziff-4-1-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4 Ziff. 4.1 – Wochenaufenthalt: Unterkunft, ortsübliche Kosten Zimmer

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag/Beleg Zimmer: Monate × Betrag
- **Regel:** Notwendiger Wochenaufenthalt am Arbeitsort: ortsübliche Auslagen für ein Zimmer; allgemein anerkannt Monatsmieten bis Fr. 800 (Zürich, Bern, Basel, Lausanne, Genf, grössere Kurorte) bzw. Fr. 500 sonst. Fahrkosten Heimkehr nach Fahrkostenregeln (Maximum).
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Abziehbar sind die ortsüblichen Mietkosten für ein Zimmer (1-Zimmerwohnung/Studio). Allgemein anerkannt: Monatsmieten bis Fr. 800 in den Städten Zürich, Bern, Basel, Lausanne, Genf und grösseren Kurorten, sonst bis Fr. 500. Komfortmehrkosten sind nicht abziehbar.** · Bund **Wochenaufenthalt: abziehbar sind die ortsüblichen Auslagen für ein Zimmer (nicht eine Wohnung) am Arbeitsort sowie die Fahrkosten der regelmässigen Heimkehr (im Rahmen des Fahrkosten-Maximums).**
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [StV SG Art. 20](../../chunks/sg/2025/sg-stv/sg-stv__art-20.md) `sg-stv__art-20` – «Als notwendige Mehrkosten der Unterkunft gelten die ortsüblichen Mietkosten für ein Zimmer»
  - [StB 39 Nr. 5 S. 2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0004.md) `sg-stb-39-5__c0004` – «Monatsmieten bis Fr. 800.--, an anderen Orten bis Fr. 500.-- allgemein anerkannt»

<a id="form-4-ziff-4-2-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4 Ziff. 4.2 – Wochenaufenthalt: Verpflegung Fr. 30 pro Arbeitstag, max. Fr. 6'400 pro Jahr (gekürzt Fr. 22.50 / Fr. 4'800)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (bei Verbilligung der Mahlzeiten)
- **Regel:** Pauschale nach DBG-Ansätzen: voll Fr. 30/Tag, Fr. 6'400/Jahr; gekürzt (Mahlzeit vom Arbeitgeber verbilligt oder Kantine möglich) Fr. 22.50/Tag, Fr. 4'800/Jahr. Nicht gleichzeitig mit dem Abzug bei täglicher Heimkehr (Ziff. 2.1).
- **Limiten:**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug Fr. 30 pro Tag, max. Fr. 6'400 im Jahr; gekürzter Abzug Fr. 22.50 pro Tag, max. Fr. 4'800 im Jahr (bei verbilligter Hauptmahlzeit).)** · Bund **CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug CHF 30 pro Tag bzw. CHF 6'400 pro Jahr; gekürzter Abzug (verbilligtes Mittagessen) CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr. Nachweis höherer Kosten ausgeschlossen.)**
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026).
- **Quellen:**
  - [StB 39 Nr. 5 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0003.md) `sg-stb-39-5__c0003` – «Voller Abzug im Tag 30.00 im Jahr 6'400.00»
  - [StB 39 Nr. 5 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0003.md) `sg-stb-39-5__c0003` – «Der reduzierte Abzug ist anzuwenden, wenn eine der beiden täglichen Hauptmahlzeiten vom Arbeitgeber verbilligt wird»

<a id="form-4-ziff-5-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 4 Ziff. 5 – Kosten bei unselbständiger Nebenerwerbstätigkeit: 20% der Nettoeinkünfte, mind. Fr. 800, max. Fr. 2'400

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 des Nebenerwerbs (Nettolohn Ziff. 1.2)
- **Regel:** Zusatzpauschale für Nebenerwerb neben einem Haupterwerb (mind. 2/3 eines Normalpensums); Nachweis höherer Kosten vorbehalten. Bei unterjähriger Steuerpflicht anteilig (MB 8/2026: Formular 4 Ziff. 5.1).
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Unselbständige Nebenerwerbstätigkeit: 20 % der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400 (Pauschalansätze der direkten Bundessteuer). Nachweis höherer notwendiger Kosten vorbehalten.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb: Pauschale mindestens Fr. 800; Nebenerwerbseinkünfte unter Fr. 800 sind nicht betroffen (siehe StB 39 Nr. 9).)** · Bund **CHF 800 (Mindestbetrag Pauschale Nebenerwerb.)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb: Pauschale höchstens Fr. 2'400.)** · Bund **CHF 2'400 (Höchstbetrag Pauschale Nebenerwerb.)**
- **Bund:** 20%, mind. Fr. 800, max. Fr. 2'400 (BKV-Anhang 2026).
- **Bemerkung:** Formular 4/2026 nicht publiziert: Ziffernnummerierung nach Formular 4/2025; Regel und Beträge aus 2026-Quellen (StG, StV, StB, MB 8/2026). MB 8/2026 nennt «Ziffer 5.1» (Nummerierung 2025: Ziff. 5).
- **Quellen:**
  - [StB 39 Nr. 9 S. 1](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0002.md) `sg-stb-39-9__c0002` – «sind 20% der Nettoeinkünfte, mindestens Fr. 800.-- und höchstens Fr. 2'400.-- abziehbar»
  - [MB 8/2026 SG S. 3](../../chunks/sg/2026/sg-mb-8-2026/sg-mb-8-2026__c0006.md) `sg-mb-8-2026__c0006` – «Berufskosten ( Formular 4, Ziffer 3.1 und 5.1 )»

## Lohnausweis (Regeln für Steuererklärung)

<a id="lohnausweis-feld-f-abzug-berufskosten-fahrkosten"></a>
### Ziff. Lohnausweis Feld F – Lohnausweis Feld F: unentgeltliche Beförderung zwischen Wohn- und Arbeitsort

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld F (Kästchen angekreuzt)
- **Regel:** Feld F angekreuzt (z.B. Geschäftsfahrzeug, Sammeltransport, GA aus geschäftlichen Gründen) = dem Arbeitnehmer erwachsen keine Arbeitswegkosten → in Formular 4 KEIN Fahrkostenabzug (bei Pauschal-Geschäftsfahrzeug auch kein Abzug nach Art. 18a StV). Bei privat nützlichem GA (ohne geschäftliche Notwendigkeit): Marktwert unter Lohnausweis Ziff. 2.3, Feld F NICHT angekreuzt, Abzug der Fahrkosten bis Maximum möglich. Vergütete Arbeitswegkosten: Ziff. 2.3, kein Kreuz, Abzug im Formular 4 bis Maximum.
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 (Maximalabzug, keine Pauschale; bei unterjähriger Steuerpflicht/Teilzeit nicht gekürzt; gilt für Haupt- und Nebenerwerb insgesamt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Bemerkung:** Quelle: bund-wl-lohnausweis-2026 Rz 9, 17; StB 39 Nr. 3 Ziff. 4.1 (SG).
- **Quellen:**
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer keine Kosten für den Arbeitsweg»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0011.md) `bund-wl-lohnausweis-2026__c0011` – «In diesem Fall ist das Feld F nicht anzukreuzen»
  - [WL Lohnausweis 2026 S. 9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0016.md) `bund-wl-lohnausweis-2026__c0016` – «kein Kreuz im Feld F zu setzen»

<a id="lohnausweis-feld-g-abzug-berufskosten-verpflegung"></a>
### Ziff. Lohnausweis Feld G – Lohnausweis Feld G: Kantinenverpflegung / Lunch-Checks / Bezahlung von Mahlzeiten

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (Kästchen angekreuzt)
- **Regel:** Feld G angekreuzt → Verpflegungsabzug in Formular 4 nur zur Hälfte (Ziff. 2.2: Fr. 7.50/Tag, max. Fr. 1'600) bzw. Wochenaufenthalt gekürzt (Ziff. 4.2). Lunch-Checks bis zur AHV-Limite (Stand 1.1.2022: Fr. 180 pro Monat) nur mit Kreuz in Feld G; darüber hinausgehende Beiträge im Lohn (Ziff. 1). Wer >60% der Arbeitszeit auswärts tätig ist und eine Mittagessensentschädigung erhält: Hinweis in Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt».
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Halber Abzug Fr. 7.50 pro Hauptmahlzeit bzw. Tag, wenn Verpflegung im Personalrestaurant möglich ist oder durch angemessenen Arbeitgeberbeitrag verbilligt wird (Lohnausweis Feld G).)** · Bund **CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Halber Abzug bei verbilligter Verpflegung: max. Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)**
- **Quellen:**
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten Buchstabe G»
  - [WL Lohnausweis 2026 S. 9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0016.md) `bund-wl-lohnausweis-2026__c0016` – «Die Abgabe von Lunch-Checks ist gemäss der Wegleitung über den massgebenden Lohn»
  - [StB 39 Nr. 8 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0014.md) `sg-stb-39-8__c0014` – «Auf dem Lohnausweis muss in diesem Fall das Feld G angekreuzt sein»

<a id="lohnausweis-ziff-10-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. Lohnausweis Ziff. 10.2 – Lohnausweis Ziff. 10.2: Beiträge für den Einkauf in die berufliche Vorsorge (BVG-Einkauf, bereits vom Lohn abgezogen)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Lohnausweis Ziff. 10.2 (Einkaufsbeiträge)
- **Regel:** Vom Lohn abgezogene Einkäufe (Ziff. 10.2) sind im Nettolohn Ziff. 11 bereits abgezogen → in Formular 1 Ziff. 13.2 NICHT nochmals abziehen. Nur direkt bezahlte Einkäufe (Bescheinigung der Vorsorgeeinrichtung, Formular 21 EDP) gehören in Ziff. 13.2.
- **Bemerkung:** Doppelabzugs-Verbot («nochmaliger Abzug unter Ziffer 13.2 ausgeschlossen») stammt aus der WL SG 2025 (jahr_ok; eine WL SG 2026 liegt im Wiki nicht vor, Formular 1/2026 UJ führt Ziff. 13.2 unverändert) – Fachperson prüft für 2026.
- **Quellen:**
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «Beiträge für den Einkauf in die berufliche Vorsorge Ziffer 10.2»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «Beiträge für den Einkauf von fehlenden Versicherungsjahren»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «sind nicht durch den Arbeitgeber im Lohnausweis, sondern durch die Vorsorgeeinrichtung separat mit dem Formular 21 EDP zu bescheinigen»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «dass vom Bruttolohn total (Ziffer 8) das Total der Abzüge (Ziffer»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0086.md) `sg-wl-2025__c0086` – «Deklaration des Nettolohnes»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «13.2 Säule 2 (BVG) inkl. Einkaufsbeiträge Person 1 Bescheinigung 218»

<a id="lohnausweis-ziff-13-3-abzug-weiterbildung"></a>
### Ziff. Lohnausweis Ziff. 13.3 – Lohnausweis Ziff. 13.3: Beiträge des Arbeitgebers für berufsorientierte Aus- und Weiterbildung (inkl. Umschulung)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Lohnausweis Ziff. 13.3
- **Regel:** Arbeitgeber-Vergütungen an den Arbeitnehmer für berufsorientierte Weiterbildung (auf Rechnungen auf den Namen des Arbeitnehmers); direkte Zahlungen an Bildungsinstitute werden nicht bescheinigt. Vom Arbeitgeber getragene Kosten sind kein geldwerter Vorteil (Art. 30 Abs. 1bis StG). Kosten, die der Arbeitgeber übernommen/vergütet hat, nicht in Ziff. 16.4 abziehen.
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung: max. Fr. 13'000 je Steuerpflichtigen, wenn erster Abschluss Sekundarstufe II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildungs- inkl. Umschulungskosten bis CHF 13'000 pro Jahr, sofern erster Abschluss Sek. II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)**
- **Quellen:**
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «In diesem Feld sind alle effektiven Vergütungen des Arbeitgebers für berufsorientierte Aus-»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «Nicht anzugeben sind Vergütungen, die direkt an Dritte»
  - [StG SG Art. 30](../../chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-30.md) `sg-stg-2026__art-30` – «stellen unabhängig von deren Höhe keinen anderen geldwerten Vorteil»

<a id="lohnausweis-ziff-15-abzug-berufskosten-verpflegung"></a>
### Ziff. Lohnausweis Ziff. 15 – Lohnausweis Ziff. 15: Bemerkungen (Anzahl Schichttage, «Einer von x Lohnausweisen», Hinweise)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 «Bemerkungen»
- **Regel:** Freiwillige Angaben: Anzahl geleisteter Schichttage (Grundlage für Schichtarbeit-Verpflegungsabzug, Formular 4 Ziff. 2.3), Höhe Kinderzulagen/Krankenkassenbeiträge im Bruttolohn. Mehrere Lohnausweise vom gleichen Arbeitgeber: Vermerk «Einer von zwei Lohnausweisen» → alle erfassen. Weitere Hinweise: «Privatanteil Geschäftsfahrzeug im Veranlagungsverfahren abzuklären», «Mittagessen durch Arbeitgeber bezahlt».
- **Quellen:**
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «die Anzahl im Kalenderjahr geleisteter Schichttage»
  - [WL Lohnausweis 2026 S. 7–8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0008.md) `bund-wl-lohnausweis-2026__c0008` – «Einer von zwei Lohnausweisen»
  - [WL Lohnausweis 2026 S. 10–11](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0021.md) `bund-wl-lohnausweis-2026__c0021` – «Privatanteil Geschäftsfahrzeug im Veranlagungsverfahren abzuklären»

## Hilfsblatt Wertschriften (Formular 2)

<a id="form-2-wertschriftenverzeichnis-einkommen-wertschriften"></a>
### Ziff. Form. 2 (Wertschriftenverzeichnis) – Wertschriften- und Guthabenverzeichnis: Steuerwert → Ziff. 30.1 (Code 300), Erträge → Ziff. 4.1 (Code 146)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Steuerauszug/Bankbescheinigung: Valoren-Nr., Steuerwert 31.12., Bruttoertrag
- **Regel:** Formular 2 liefert Steuerwert (Ziff. 30.1) und Erträge (Ziff. 4.1); Verwaltungskosten Ziff. 16.1. Formular 2/2026 nicht publiziert – Spalten/Codes (z.B. VST-Anspruch 35%, Code 999 laut 2025) nicht für 2026 bestätigt.
- **Bemerkung:** Weitere Zeilen (Code 999, 960–963) bewusst weggelassen: keine 2026-Quelle.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «4.1 aus Wertschriften und Guthaben 146»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «30.1 Wertschriften und Guthaben Formular 2 300»

## Hilfsblatt Schulden/Zuwendungen (Formular 5)

<a id="form-5-schulden-spenden-schulden-privat"></a>
### Ziff. Form. 5 (Schulden/Spenden) – Formular 5: Schuldzinsen → Ziff. 11 (Code 500); Privatschulden → 34.1 (504); Geschäftsschulden → 34.2 (506); Zuwendungen → 21.3 (244); Parteispenden → 16.3 (555)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht), Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Schuldenausweis Gläubiger (Schuld 31.12.2026, Zinsen 2026); Spendenbestätigungen
- **Regel:** Übertragsregeln gemäss Formular 1 UJ 2026; materielle Regeln siehe Ziff. 11, 21.3, 16.3, 34.1.
- **Bemerkung:** Formular 5/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0007.md) `sg-form-1-2026-uj__c0007` – «11. Schuldzinsen Formular 5 500»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0012.md) `sg-form-1-2026-uj__c0012` – «34.1 Privatschulden Formular 5 504»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «21.3 Freiwillige Zuwendungen (wenn mind. Fr.100, max. 20% Ziffer 20) Formular 5 244»

## Hilfsblatt Versicherungen/Krankheitskosten (Formular 6)

<a id="form-6-versicherungen-krankheitskosten-abzug-versicherungspraemien"></a>
### Ziff. Form. 6 (Versicherungen/Krankheitskosten) – Formular 6: Versicherungsprämien → Ziff. 14 (Code 600); Krankheitskosten → 21.1 (650); behinderungsbedingte Kosten → 21.2 (235)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung, Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Prämienrechnung Krankenkasse (brutto), Leistungsabrechnungen, Arztrechnungen
- **Regel:** Übertragsregeln gemäss Formular 1 UJ 2026; Limiten siehe Ziff. 14 (Art. 45 Abs. 1 Bst. g StG) und 21.1 (Selbstbehalt 2%).
- **Bemerkung:** Formular 6/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «14. Versicherungsprämien und Sparzinsen Formular 6 600»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0009.md) `sg-form-1-2026-uj__c0009` – «21.1 Krankheits- und Unfallkosten Formular 6 650»

## Hilfsblatt Liegenschaften (Formular 7)

<a id="form-7-liegenschaften-vermoegen-liegenschaften"></a>
### Ziff. Form. 7 (Liegenschaften) – Formular 7: Erträge → Ziff. 5 (Code 712); Unterhalts- und Verwaltungskosten → 15 (716); Steuerwert → 31 (710)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Schätzungsverfügung (Steuerwert, Mietwert), Mietzinsabrechnung, Unterhaltsrechnungen 2026
- **Regel:** Übertragsregeln gemäss Formular 1 UJ 2026; Regeln siehe Ziff. 5, 15, 31 (Eigenmietwert −30%, Pauschale 20%).
- **Bemerkung:** Formular 7/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 2](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0005.md) `sg-form-1-2026-uj__c0005` – «Ertrag aus Liegenschaften Formular 7 712»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «15. Unterhalts- und Verwaltungskosten für Liegenschaften Formular 7 716»
  - [Formular 1 SG 2026 UJ S. 4](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0011.md) `sg-form-1-2026-uj__c0011` – «31. Liegenschaften Formular 7 710»

## Hilfsblatt Kinder (Formular 10)

<a id="form-10-kinderbetreuung-ausbildung-abzug-drittbetreuung"></a>
### Ziff. Form. 10 (Kinderbetreuung/Ausbildung) – Formular 10: Kinderbetreuungskosten → Ziff. 16.2 (Code 258); Ausbildungskosten Kinder → 23.3 (256)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule), Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Rechnungen Kita/Tagesmutter, Ausbildungskosten
- **Regel:** Maxima 2026: Fr. 26'800 je Kind (Betreuung), Fr. 13'800 je Kind (Ausbildungskosten, über Fr. 3'200 Selbstbehalt).
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 26'800 (Kinderdrittbetreuungskosten: höchstens Fr. 26'800 je Kind unter 14 Jahren, das im gleichen Haushalt lebt, soweit in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind, höchstens CHF 25'800; Kind unter 14 Jahren im gleichen Haushalt; Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 10'800 (Kinderabzug für Kind in schulischer oder beruflicher Ausbildung (auch volljährig): Fr. 10'800.)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Abzug CHF 6'800 (kein höherer Ausbildungsabzug beim Bund).)**
- **Bemerkung:** Formular 10/2026 nicht publiziert.
- **Quellen:**
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0008.md) `sg-form-1-2026-uj__c0008` – «16.2 Kinderbetreuungskosten bei Drittbetreuung Formular 10 258»
  - [Formular 1 SG 2026 UJ S. 3](../../chunks/sg/2026/sg-form-1-2026-uj/sg-form-1-2026-uj__c0010.md) `sg-form-1-2026-uj__c0010` – «23.3 Ausbildungskosten für Kinder in Schule oder Ausbildung Formular 10 256»
