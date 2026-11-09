---
typ: zuordnung-detail
titel: Zuordnung SG 2025 – Detail
jur: sg
jahre:
- 2025
generiert: tools/build_quick.py aus data/zuordnung/sg/2025.yaml (2026-11-09)
---

# SG 2025: Zuordnung Beleg → Ziffer – Detail

> Kompaktansicht: [quick/zuordnung-sg-2025.md](../../quick/zuordnung-sg-2025.md) · Formular: Steuererklärung 2025 Formular 1 (Hauptformular, Kantons-, Gemeinde- und direkte Bundessteuer) + Hilfsblätter Formular 2 (Wertschriften- und Guthabenverzeichnis), 4 (Berufskosten), 5 (Schulden, freiwillige Zuwendungen, Parteispenden), 6 (Versicherungsprämien, Krankheits- und Unfallkosten), 7/7Z (Liegenschaften), 10 (Kinderbetreuung/Ausbildungskosten Kinder; Formular nicht im Wiki) · Quelle der Wahrheit: `data/zuordnung/sg/2025.yaml`

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Aus Haupterwerbstätigkeit unselbständig (Code 100 Person 1 / 102 Person 2)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn)
- **Regel:** Nettolohn gemäss Lohnausweis einsetzen (Bruttolohn abzüglich obligatorische Sozialversicherungsbeiträge und ordentliche BVG-Beiträge). Pro Arbeitgeber ein Lohnausweis. Berufskosten separat in Ziff. 10 (Formular 4). Familienzulagen, die nicht im Lohnausweis stehen (z.B. Arbeitgeber FL), in Ziff. 3.5. Lohnausweis Ziff. 10.2 (BVG-Einkauf) ist hier schon abgezogen, nicht nochmals in Ziff. 13.2. Lohnausweis Ziff. 13.3 (vom Arbeitgeber getragene Aus-/Weiterbildung) nicht steuerbar, nicht in Ziff. 16.4 abziehen.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) `sg-form-1-2025__c0004` – «1.1 Aus Haupterwerbstätigkeit Person 1 Lohnausweis 100»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0042.md) `sg-wl-2025__c0042` – «Einzusetzen ist der Nettolohn gemäss Lohnausweis»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Aus Nebenerwerbstätigkeit unselbständig (Code 104 Person 1 / 106 Person 2)

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn) des Nebenarbeitgebers
- **Regel:** Nebenerwerb = Tätigkeit neben einem Haupterwerb, grundsätzlich für einen anderen Arbeitgeber. Auch Mietzinsreduktion (z.B. Hauswart) als Einkommen deklarieren. Berufskostenpauschale für Nebenerwerb: Formular 4 Ziff. 5.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) `sg-form-1-2025__c0004` – «1.2 Aus Nebenerwerbstätigkeit Person 1 Lohnausweis 104»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0043.md) `sg-wl-2025__c0043` – «Als Nebenerwerb gilt eine Tätigkeit, die gleichzeitig neben einem Haupterwerb»

<a id="1-3-einkommen-unselbstaendig-vr-honorare"></a>
### Ziff. 1.3 – Sitzungsgelder, VR-Honorare usw. (Code 108 Person 1 / 110 Person 2)

- **Schlüssel:** `einkommen.unselbstaendig.vr_honorare` (VR-Honorare, Sitzungsgelder, Tantiemen (wo separat ausgewiesen, z.B. SG/AR Ziff. 1.3)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 6 (Verwaltungsratsentschädigungen) bzw. Bescheinigung der Gesellschaft/Behörde
- **Regel:** Nur soweit nicht bereits mit den übrigen Erwerbseinkünften deklariert (Doppelerfassung vermeiden). Behördentätigkeit: Steuerbuch SG StB 39 Nr. 4.
- **Bemerkung:** korrigiert durch Prüfung: Lohnausweis-Ziffer für VR-Entschädigungen ist Ziff. 6 (nicht Ziff. 4 = Kapitalleistungen); Beleg: Lohnausweis-Wegleitung (im Wiki nur 2026, Rz 30), Formularstruktur gilt unverändert.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) `sg-form-1-2025__c0004` – «1.3 Sitzungsgelder, VR-Honorare usw. Person 1 Bescheinigung 108»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0044.md) `sg-wl-2025__c0044` – «Sitzungs- und Taggelder, Verwaltungsratshonorare und Tantiemen»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit: Industrie-, Handels-, Gewerbebetriebe, Landwirtschaft, freie Berufe (Code 112 Person 1 / 114 Person 2)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Erfolgsrechnung/Reingewinn der Jahresrechnung
- **Regel:** Reingewinn nach den im Kalenderjahr 2025 abgeschlossenen Bilanzen/Erfolgsrechnungen; Bilanz, Erfolgsrechnung, Eigenkapitalkonti und Abschreibungstabellen beilegen. Ohne Buchführungspflicht: Aufstellung über Aktiven/Passiven und Einnahmen/Ausgaben. Beteiligungserträge >= 10% separat (Ziff. 4.3). Familienzulagen im Reingewinn: Gewinn entsprechend gekürzt, Ziff. 3.5.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) `sg-form-1-2025__c0004` – «2.1 Person 1 112»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0045.md) `sg-wl-2025__c0045` – «Das Einkommen aus selbständiger Erwerbstätigkeit umfasst alle Einkünfte aus»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Aus Kollektiv-, Kommandit- und einfachen Gesellschaften (Code 120 Person 1 / 122 Person 2)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Angaben der Firma im Formular 11 (Kollektiv- und Kommanditgesellschaften)
- **Regel:** Einkünfte gemäss Formular 11 der Gesellschaft (inkl. Kapitalerträge); auch Beteiligung an einfacher Gesellschaft (z.B. Konsortium). Achtung: SG-Ziff. 2.2 ist Gesellschaftsbeteiligung, nicht Nebenerwerb selbständig.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) `sg-form-1-2025__c0004` – «2.2 Aus Kollektiv-, Kommandit- und einfachen Gesellschaften»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0045.md) `sg-wl-2025__c0045` – «unter Ziffer 2.2 anzugeben»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV/IV-Renten zu 100% (Code 126 Person 1 / 128 Person 2)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung Ausgleichskasse (Jahresbetrag brutto)
- **Regel:** Ordentliche und ausserordentliche AHV-/IV-Renten voll deklarieren. Ergänzungsleistungen nicht hier (steuerfrei, siehe Ziff. 8.2).
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0005.md) `sg-form-1-2025__c0005` – «3.1 AHV/IV-Renten (zu 100%) Person 1 Bescheinigung 126»
  - [WL SG 2025 S. 18](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0056.md) `sg-wl-2025__c0056` – «sind in vollem Umfang zu deklarieren, nicht aber die Ergänzungsleistungen»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen mit steuerbarem Prozentsatz (Code 130 Person 1 / 132 Person 2)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente), Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Rentenbescheinigung Pensionskasse/Versicherer: Jahresrente brutto; steuerbarer Prozentsatz in Vorkolonne
- **Regel:** Voller Betrag und Prozentsatz in Vorkolonne, Nettobetrag in Hauptkolonne. 2. Säule 100% (80% nur wenn Rentenbeginn vor 1.1.2002, Vorsorgeverhältnis vor 1.1.1985 und Versicherter >= 20% der Beiträge erbracht hat); Säule 3a und reine Risikoversicherungen 100%; Leibrenten: Ertragsanteil (neu variabel, Versicherer bescheinigt bzw. ESTV publiziert). Mehrere Renten separat auflisten.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0005.md) `sg-form-1-2025__c0005` – «3.2 Renten/Pensionen»
  - [WL SG 2025 S. 18](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0058.md) `sg-wl-2025__c0058` – «100% in allen andern Fällen»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigung / Taggelder IV, Kranken-, Unfallversicherung (Code 134 Person 1 / 136 Person 2)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung Versicherung/EO (Brutto- bzw. Nettoauszahlung)
- **Regel:** Nur soweit nicht im Lohnausweis enthalten. IV-Taggelder hier. EO (Militär, Zivilschutz, Mutterschaft) hier, soweit nicht im Lohnausweis; bei Selbständigen nur bei Nettoauszahlung durch Ausgleichskasse, bei Bruttoauszahlung in der Jahresrechnung verbuchen.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0005.md) `sg-form-1-2025__c0005` – «3.3 Erwerbsausfallentschädigung Person 1 Bescheinigung 134»
  - [WL SG 2025 S. 19](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0060.md) `sg-wl-2025__c0060` – «Taggelder aus Invaliden-, Kranken- und Unfallversicherung sind voll-»

<a id="3-4-einkommen-ersatz-taggelder"></a>
### Ziff. 3.4 – Arbeitslosen-Taggelder (Code 138 Person 1 / 140 Person 2)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Arbeitslosenkasse
- **Regel:** Nur Bezüge, die nicht im Lohnausweis des Arbeitgebers bescheinigt sind. Bescheinigung der Arbeitslosenkasse beilegen.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0005.md) `sg-form-1-2025__c0005` – «3.4 Arbeitslosen-Taggelder Person 1 Bescheinigung 138»
  - [WL SG 2025 S. 19](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0060.md) `sg-wl-2025__c0060` – «Über nicht im Lohnausweis aufgeführte Bezüge ist eine Bescheinigung beizulegen»

<a id="3-5-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.5 – Von Ausgleichskassen direkt ausbezahlte Familienzulagen (Code 142)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung Familienausgleichskasse
- **Regel:** Nur Zulagen, die nicht im Lohnausweis stehen (z.B. Arbeitgeber im Fürstentum Liechtenstein). Bei Selbständigen: Leistungen der Familienausgleichskasse (nicht AHV-pflichtig) hier, Reingewinn Ziff. 2 entsprechend gekürzt.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0005.md) `sg-form-1-2025__c0005` – «3.5 Von Ausgleichskassen direkt ausbezahlte Familienzulagen 142»
  - [WL SG 2025 S. 19](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0061.md) `sg-wl-2025__c0061` – «die von Ausgleichskassen direkt ausbezahlt werden und somit nicht im Lohnaus»

<a id="4-1-einkommen-wertschriften"></a>
### Ziff. 4.1 – Einkünfte aus Wertschriften und Guthaben inkl. Lotterie-/Geldspielgewinne (Code 146)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Formular 2: Total Erträge (Spalten A + B) abzüglich Geschäfts- und Beteiligungserträge
- **Regel:** Übertrag aus Formular 2 (Total, abzüglich G/BG und BP-Erträge). Bruttoerträge deklarieren. Bankzinsen bis Fr. 200 pro Konto/Bank verrechnungssteuerfrei (Spalte B), darüber Spalte A. Dividenden: GV-Beschluss massgebend. Steuerbare Geldspielgewinne: nur einzelne Gewinne über den Schwellen (siehe WL). Ausländische Erträge mit Quellensteuer: DA-1.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «4.1 aus Wertschriften und Guthaben 146»
  - [Formular 2 SG 2025 S. 2](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0006.md) `sg-form-2-2025__c0006` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 30.1 Seite 2 Ziffer 4.1»
  - [WL SG 2025 S. 37](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0130.md) `sg-wl-2025__c0130` – «sind bis und mit Fr. 200 je Kalenderjahr verrechnungssteuerfrei»

<a id="4-2-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.2 – Beteiligungen an Gesellschaften ab 10 Prozent, Privatvermögen (Code 147)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2: Erträge Code BP (ohne Vorzeichen)
- **Regel:** 100% der Erträge deklarieren; Beteiligung mind. 10% am Grund-/Stammkapital. Im Wertschriftenverzeichnis Code BP; Übertrag in Ziff. 4.2. Die Reduktion von 30% (Teilbesteuerung 70%) wird in Ziff. 4.4 abgezogen.
- **Bund:** Bund: ebenfalls Teilbesteuerung 70% (Kreisschreiben Nr. 22a ESTV).
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «4.2 aus Beteiligungen an Gesellschaften ab 10 Prozent (Privatvermögen) 147»
  - [WL SG 2025 S. 20](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0065.md) `sg-wl-2025__c0065` – «Zu deklarieren sind 100% der Erträge»

<a id="4-3-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.3 – Beteiligungen an Gesellschaften ab 10 Prozent, Geschäftsvermögen (Code 149)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 2: Erträge Code BG; verbuchte Erträge der Jahresrechnung
- **Regel:** Verbuchte Erträge (brutto/netto) unter «Abzüglich Geschäftswertschriften bzw. -erträge (G und BG)» im Formular 2 abziehen und hier deklarieren, um Doppelerfassung zu vermeiden.
- **Bund:** Bund: ebenfalls Teilbesteuerung 70% (Kreisschreiben Nr. 23a ESTV).
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «4.3 aus Beteiligungen an Gesellschaften ab 10 Prozent (Geschäftsvermögen) 149»
  - [WL SG 2025 S. 20](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0066.md) `sg-wl-2025__c0066` – «Dadurch wird eine doppelte Berück-»

<a id="4-4-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 4.4 – Abzug Teilbesteuerung Beteiligungserträge (Code 150, 30%)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → 30% der Summe Ziff. 4.2 und 4.3
- **Regel:** Abzug beträgt 30% der Einkünfte aus Beteiligungen (Ziff. 4.2 + 4.3); von der steuerpflichtigen Person selbst zu berechnen (in E-Tax SG automatisch). Als Minusposten im Einkünfteteil, nicht im Abzugsteil.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «4.4 Abzug Teilbesteuerung Beteiligungserträge 150»
  - [WL SG 2025 S. 20](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0065.md) `sg-wl-2025__c0065` – «Die steuerliche Reduktion von 30% ist durch den Steuerpflichtigen zu berechnen»

<a id="5-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. 5 – Ertrag aus Liegenschaften (Code 712)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Formular 7 Abschnitt B «Total Erträge a. und b.» (bei mehreren Liegenschaften Formular 7Z Spalte B)
- **Regel:** Summe aus Eigenmietwert (Erstwohnung um 30% reduziert) und Mietertrag Fremdnutzung. Unterhalt separat in Ziff. 15 (nicht netto verrechnen). Geschäftsliegenschaften in Ziff. 2.
- **Quellen:**
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0003.md) `sg-form-7-2025__c0003` – «Total Erträge a. und b.»
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «5. Ertrag aus Liegenschaften Formular 7 712»
  - [WL SG 2025 S. 20](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0067.md) `sg-wl-2025__c0067` – «Anzugeben sind die Einkünfte aus Liegenschaften des Privatvermögens»

<a id="6-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 6.1 – Unterhaltsbeiträge erhalten: für Steuerpflichtige (Code 154) / für minderjährige Kinder (Code 156)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil, Zahlungsnachweise (Jahressumme)
- **Regel:** Periodische Unterhaltsbeiträge für sich und für Kinder unter Obhut getrennt aufführen. Beim Zahlenden abziehbar (Ziff. 12.1/12.2). Unterhalt an Volljährige: beim Zahlenden nicht abziehbar, beim Empfänger nicht steuerbar.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «6.1 Unterhaltsbeiträge für den/die Steuerpflichtige(n) 154»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0068.md) `sg-wl-2025__c0068` – «sind beim Empfänger steuerbar und daher unter dieser Ziffer zu»

<a id="6-2-einkommen-erbschaften-unverteilt"></a>
### Ziff. 6.2 – Ertrag aus unverteilten Erbschaften (Code 158)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Detaillierte Aufstellung der Erbengemeinschaft
- **Regel:** Anteilig bei den Berechtigten besteuert; Aufstellung beilegen. Beteiligung zusätzlich im Formular 2 Seite 1 (Code 961) vermerken und Vermögensanteil in Ziff. 30.5.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «6.2 Ertrag aus unverteilten Erbschaften 158»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0068.md) `sg-wl-2025__c0068` – «Einkünfte aus unverteilten Erbschaften und andern Vermögensmassen»

<a id="6-3-einkommen-uebrige"></a>
### Ziff. 6.3 – Übrige Einkünfte (Code 162)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Mitarbeiterbeteiligung (Mitarbeiteraktien, Optionen, Anwartschaften/RSU, Beiblatt zum Lohnausweis) → Aufstellung/Beleg der jeweiligen Einkunftsart
- **Regel:** Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Urheberrechte/Lizenzen/Patente, Förderbeiträge (E-Fahrzeuge, E-Bikes), Stromerzeugung (PV) soweit über Eigenverbrauch, IV-Assistenzbeiträge (soweit nicht neutralisiert, StB 46 Nr. 3). Nur soweit nicht in Ziff. 1 bis 6.2 enthalten.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «6.3 Übrige Einkünfte Arten 162»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0069.md) `sg-wl-2025__c0069` – «Erträge aus Stromerzeugung (Photovoltaikanlagen), soweit diese den Eigenver»

<a id="6-4-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 6.4 – Kapitalabfindungen für wiederkehrende Leistungen (Code 164, Anzahl Jahre)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Auszahlungsbetrag und Anzahl Jahre gemäss Bescheinigung
- **Regel:** Auszahlungsbetrag und Anzahl Jahre einsetzen; Besteuerung zum Satz einer entsprechenden jährlichen Leistung. Kapitalleistungen aus Vorsorge gehören NICHT hierher, sondern auf Seite 4 (Ziff. 40).
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «6.4 Kapitalabfindungen für wiederkehrende Leistungen für Jahre 164»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0070.md) `sg-wl-2025__c0070` – «Die Kapitalabfindungen für wiederkehrende Leistungen sind mit dem»

<a id="7-berechnung-total"></a>
### Ziff. 7 – Total der Einkünfte (Code 168)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Summe Ziff. 1 bis 6 (Ziff. 4.4 als Minusposten). Ziff. 8 (ergänzende Angaben) nicht im Total.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «7. Total der Einkünfte 168»

<a id="8-1-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 8.1 – Ergänzende Angaben: vereinfacht abgerechnete Einkünfte, Bruttolohn (Code 290)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bestätigung der Ausgleichskasse über Quellensteuerabzug (sonst Lohnabrechnungen)
- **Regel:** Nur Information, nicht im Total der Einkünfte. Bruttolohn einsetzen. Mit 5% Abzug sind Bundes-, Kantons- und Gemeindesteuer abgegolten; keine weiteren Steuerfolgen, kein Einfluss auf Steuersatz.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0007.md) `sg-form-1-2025__c0007` – «8.1 Vereinfacht abgerechnete Einkünfte Bescheinigung 290»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0071.md) `sg-wl-2025__c0071` – «In Ziffer 8.1 ist der Bruttolohn einzusetzen»

<a id="8-2-8-3-info-steuerfreie-leistungen"></a>
### Ziff. 8.2-8.3 – Ergänzende Angaben: Ergänzungsleistungen/Überbrückungsleistungen (Code 291), Hilflosenentschädigungen (Code 292)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung der Durchführungsstelle (EL/HE)
- **Regel:** Nur Information, steuerfrei. Anzurechnen sind aber EL, die zur Vergütung von Krankheits- und Behinderungskosten ausgerichtet werden; Hilflosenentschädigung wird an die behinderungsbedingten Kosten (Formular 6) angerechnet.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0007.md) `sg-form-1-2025__c0007` – «8.2 Ergänzungsleistungen / Überbrückungsleistungen für ältere Arbeitslose 291»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0072.md) `sg-wl-2025__c0072` – «Ergänzungsleistungen (inkl. Überbrückungsleistungen für»

<a id="lohnausweis-ziff-10-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. Lohnausweis Ziff. 10.2 – Lohnausweis Ziff. 10.2: BVG-Einkaufsbeiträge (bereits vom Lohn abgezogen)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Lohnausweis Ziff. 10.2 (Einkaufsbeiträge)
- **Regel:** Im Nettolohn (Ziff. 1.1/1.2) bereits berücksichtigt: Beiträge an die 2. Säule sind im Regelfall schon über die Deklaration des Nettolohnes berücksichtigt, ein nochmaliger Abzug unter Ziff. 13.2 ist ausgeschlossen. Einkauf über Lohnausweis abgerechnet: nicht doppelt abziehen; nur Einkäufe, die vom Lohn nicht abgezogen wurden (Direktzahlung), in Ziff. 13.2 mit Bescheinigung. Die Praxis zu Ziff. 10.2 stützt sich auf die Lohnausweis-Wegleitung (nur 2026 im Wiki); Fachperson prüft.
- **Bemerkung:** Spezifische Lohnausweis-Ziffer 10.2 in der SG-WL 2025 nicht erwähnt; Aussage zur Doppelerfassung aus WL SG 2025 Ziff. 13.2. Inhalt durch Prüfung bestätigt (Lohnausweis-Wegleitung Rz 45/47 bzw. 61, nur 2026 im Wiki); SG-Zitat nur indirekt, daher extrahiert.
- **Quellen:**
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0086.md) `sg-wl-2025__c0086` – «Deklaration des Nettolohnes»

<a id="lohnausweis-ziff-13-3-abzug-weiterbildung"></a>
### Ziff. Lohnausweis Ziff. 13.3 – Lohnausweis Ziff. 13.3: Beiträge des Arbeitgebers an Aus-/Weiterbildung

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Lohnausweis Ziff. 13.3
- **Regel:** Vom Arbeitgeber getragene Kosten der berufsorientierten Aus- und Weiterbildung (inkl. Umschulung) sind nicht steuerbar; entsprechend darf der Arbeitnehmer diese Kosten nicht nochmals in Ziff. 16.4 abziehen (nur selbst bezahlte Kosten).
- **Bemerkung:** Lohnausweis-Ziffer 13.3 wird in der WL SG 2025 nicht namentlich genannt; Regel aus WL SG 2025 Ziff. 1 und 16.4. Inhalt durch Prüfung bestätigt (Lohnausweis-Wegleitung Rz 45/47 bzw. 61, nur 2026 im Wiki); SG-Zitat nur indirekt, daher extrahiert.
- **Quellen:**
  - [WL SG 2025 S. 14](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0040.md) `sg-wl-2025__c0040` – «Nicht steuerbar sind die vom Arbeitgeber getragenen Kosten der berufsorientierten»
  - [WL SG 2025 S. 14](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0040.md) `sg-wl-2025__c0040` – «Aus- und Weiterbildung, einschliesslich Umschulungskosten.»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0094.md) `sg-wl-2025__c0094` – «Um selbst bezahlte, berufsorientierte Aus-, Weiterbildungs- und»

## Abzüge

<a id="10-1-berechnung-total"></a>
### Ziff. 10.1 – Berufskosten bei unselbständiger Erwerbstätigkeit Person 1 (Code 438)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 4 Person 1 Ziff. 6 «Total der Berufskosten» (Code 438)
- **Regel:** Übertrag des Totals aus Formular 4 (Vorderseite). Abzüge stehen jedem Partner individuell zu, soweit unselbständig erwerbstätig. Kein Abzug für vom Arbeitgeber übernommene Kosten. Ausgangsbasis ist der Nettolohn Ziff. 1.1.
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 pro Person (Maximalabzug, keine Pauschale; bei Teilzeit/unterjährig nicht gekürzt; gilt bei Haupt- und Nebenerwerb insgesamt). Bei direkter Bundessteuer tiefer (Fr. 3'300, siehe data/werte/bund).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Pauschale übrige Berufskosten höchstens Fr. 2'400.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
- **Bund:** Bund: abweichende Limiten (Fahrkosten max. Fr. 3'300; Pauschale übrige Kosten 3% des Nettolohnes, min. Fr. 2'000, max. Fr. 4'000) – die Veranlagungsbehörde passt automatisch an.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «10.1 Person 1 Formular 4 438»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0074.md) `sg-wl-2025__c0074` – «stehen jedem Partner individuell zu, soweit er unselbständig erwerbstätig ist»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0002.md) `sg-form-32-2025__c0002` – «Fahrkosten zwischen Wohn- und Arbeitsort max. Fr. 8‘000 max. Fr. 3‘300»

<a id="10-2-berechnung-total"></a>
### Ziff. 10.2 – Berufskosten bei unselbständiger Erwerbstätigkeit Person 2 (Code 488)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 4 Person 2 Ziff. 6 «Total der Berufskosten» (Code 488)
- **Regel:** Wie Ziff. 10.1, für Person 2 (Formular 4 Rückseite).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «10.2 Person 2 Formular 4 488»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0008.md) `sg-form-4-2025__c0008` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 10.2»

<a id="11-abzug-schuldzinsen"></a>
### Ziff. 11 – Schuldzinsen (Code 500)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 5 Teil A «Total private Schulden und private Schuldzinsen» (Schuldzinsen 2025)
- **Regel:** Nur private Schuldzinsen; abziehbar im Umfang der Einkünfte aus Wertschriften/Guthaben (Ziff. 4, ohne Lotteriegewinne) und Liegenschaften (Ziff. 5) zuzüglich Fr. 50'000. Nicht abzugsfähig: Amortisationen, Baukreditzinsen (Anlagekosten), Baurechtszinsen selbstgenutzter Eigenheime, Leasinggebühren. Geschäftliche Schuldzinsen sind in der Jahresrechnung enthalten (nicht in Formular 5). Hypothekarzinsen der Liegenschaft hier, nicht im Formular 7.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «11. Schuldzinsen Formular 5 500»
  - [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0083.md) `sg-wl-2025__c0083` – «Private Schuldzinsen sind nur im Umfang der Einkünfte aus Wertschriften und»
  - [Formular 5 SG 2025 S. 1](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0001.md) `sg-form-5-2025__c0001` – «Total private Schulden und private Schuldzinsen»

<a id="12-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.1 – Unterhaltsbeiträge an Geschiedene oder Getrennte (Code 200)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungsurteil/Trennungsvereinbarung (bei erstmaliger Zahlung), Zahlungsnachweise
- **Regel:** Nur Beiträge an geschiedenen/getrennt lebenden Partner. Bei erstmaliger Zahlung Auszug aus Urteil bzw. Vereinbarung beilegen. Hinweis: Können Unterhaltsbeiträge (für Kinder, Ziff. 12.2) abgezogen werden, entfallen die Kinderabzüge Ziff. 23.1-23.3 für dieses Kind.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «12.1 Unterhaltsbeiträge an Geschiedene oder Getrennte Aufstellung 200»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0084.md) `sg-wl-2025__c0084` – «Unterhaltsbeiträge an den geschiedenen, gerichtlich oder tatsächlich getrennt»

<a id="12-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.2 – Unterhaltsbeiträge für minderjährige Kinder (Code 202)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise je Kind, Urteil/Vereinbarung
- **Regel:** Beiträge an den Elternteil mit elterlicher Sorge/Obhut, separat je Kind ausweisen. Für dieses Kind kein Kinderabzug (Kind auf Seite 1 nicht aufführen). An volljährige Kinder bezahlte Beiträge nicht abziehbar.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «12.2 Unterhaltsbeiträge für minderjährige Kinder Aufstellung 202»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0084.md) `sg-wl-2025__c0084` – «Die Unterhaltsbeiträge an einen Elternteil für die unter dessen elterlicher Sorge»

<a id="12-3-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.3 – Rentenleistungen (Code 204)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Vertrag/Nachweis dauernde Last bzw. Rentenbescheinigung
- **Regel:** Nachgewiesene dauernde Lasten sowie Ertragsanteil der Leistungen aus Leibrenten und Verpfründungsverträgen (Art. 35 Abs. 3 lit. c StG).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «12.3 Rentenleistungen Aufstellung 204»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0084.md) `sg-wl-2025__c0084` – «Die nachgewiesenen dauernden Lasten sowie der Ertragsanteil»

<a id="13-1-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.1 – Vorsorgebeiträge Säule 3a (Code 208 Person 1 / 210 Person 2)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → 3a-Bescheinigung (Form. 21 EDP): im Jahr 2025 bezahlter Betrag
- **Regel:** Nur 2025 tatsächlich bezahlte Beiträge; Bescheinigung immer beilegen. Max. Fr. 7'258 (mit 2. Säule) bzw. 20% des Erwerbseinkommens, max. Fr. 36'288 (ohne 2. Säule). Beide erwerbstätigen Partner je eigener Abzug. Selbständige: nicht der Erfolgsrechnung belasten. Wer 3a abzieht, verliert den Zuschlag beim Versicherungsabzug (Ziff. 14).
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a: Erwerbstätige mit 2. Säule maximal Fr. 7'258 (beide Partner je für sich abziehbar). Nur im Jahr 2025 tatsächlich bezahlte Beiträge; Bescheinigung beilegen.)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug mit Zugehörigkeit zur 2. Säule (8 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a: Erwerbstätige ohne 2. Säule höchstens 20 % des Erwerbseinkommens, maximal Fr. 36'288.)** · Bund **CHF 36'288 (Säule 3a: Höchstabzug ohne 2. Säule (max. 36'288, 40 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. Fr. 36'288).)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. CHF 36'288))**
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «13.1 Säule 3a Person 1 Bescheinigung 208»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0085.md) `sg-wl-2025__c0085` – «maximal Fr. 7’258»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0085.md) `sg-wl-2025__c0085` – «maximal Fr. 36’288»

<a id="13-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 13.2 – Säule 2 (BVG) inkl. Einkaufsbeiträge (Code 218 Person 1 / 219 Person 2)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Bescheinigung Vorsorgeeinrichtung + Einkaufsberechnung (Lohnausweis Ziff. 10.2 = bereits abgezogen)
- **Regel:** Beiträge im Lohnausweis (Ziff. 10.1 ordentliche BVG-Beiträge) sind im Nettolohn schon berücksichtigt: nicht nochmals abziehen. Hier nur Einkäufe/Beiträge ausserhalb des Lohnausweises, bei Selbständigen 100% der Einkaufsbeiträge. Lohnausweis Ziff. 10.2 (Einkauf, vom Lohn abgezogen): im Nettolohn (Ziff. 11 = Ziff. 8 abzüglich Ziff. 9 und 10) bereits abgezogen, daher hier nicht nochmals (Lohnausweis-Wegleitung Rz 45/47, im Wiki nur 2026). Bescheinigung der Vorsorgeträgerin immer beilegen. Kein Abzug bei Einkauf mit vorzeitig bezogenen, steuerlich nicht erfassten Kapitalleistungen.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «13.2 Säule 2 (BVG) inkl. Einkaufsbeiträge Person 1 Bescheinigung 218»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0086.md) `sg-wl-2025__c0086` – «Deklaration des Nettolohnes»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0086.md) `sg-wl-2025__c0086` – «Die Berücksichtigung in der Erfolgsrechnung ist nicht zulässig»

<a id="14-abzug-versicherungspraemien"></a>
### Ziff. 14 – Versicherungsprämien und Sparzinsen (Code 600)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 6 Teil C «Abzug» (niedrigerer Betrag von A und B)
- **Regel:** Effektive Prämien (Kranken brutto, Unfall ohne NBU, Lebens-/Rentenvers.) + Sparzinsen, abzüglich Prämienverbilligungen (A) gegen Maximalbetrag (B): gemeinsam Fr. 6'800 / alleinstehend Fr. 3'400, + je Fr. 1'100 pro Kind mit Kinderabzug, + Fr. 1'100 / Fr. 500 wenn weder BVG- noch Säule-3a-Beiträge abgezogen (bei Verheirateten bei beiden Partnern). Niedrigerer Betrag von A und B. Nicht abziehbar: Mobiliar-, Motorfahrzeug-, Haftpflicht- und Sachversicherungen.
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 6'800 (Versicherungsprämien und Sparzinsen: Gesamtbetrag Fr. 6'800 für gemeinsam steuerpflichtige Ehegatten (Kranken-, Unfall-, Lebens-/Rentenversicherung, Zinsen von Sparkapitalien; Prämienverbilligungen sind anzurechnen).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 3'400 (Versicherungsprämien und Sparzinsen: Gesamtbetrag Fr. 3'400 für übrige Steuerpflichtige.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 7'900 (Gemeinsam Steuerpflichtige ohne Abzug von Beiträgen an 2. Säule/Säule 3a: Maximalabzug erhöht sich um Fr. 1'100 (6'800 + 1'100 = 7'900). Bei Verheirateten müssen die Voraussetzungen bei beiden Partnern erfüllt sein.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an Säule 2/3a (Erhöhung um die Hälfte))**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 3'900 (Übrige Steuerpflichtige ohne Abzug von Beiträgen an 2. Säule/Säule 3a: Erhöhung um Fr. 500 (3'400 + 500 = 3'900).)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'100 (Zuschlag Fr. 1'100 für jedes Kind, für das ein Kinderabzug geltend gemacht werden kann (Gesetz); WL: bis Fr. 1'100.)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
- **Bund:** Bund: gemeinsam max. Fr. 3'700, alleinstehend Fr. 1'800; Zuschläge ohne BVG/3a Fr. 1'850 / Fr. 900; pro Kind (und unterstützte Person) Fr. 700.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «14. Versicherungsprämien und Sparzinsen Formular 6 600»
  - [Formular 6 SG 2025 S. 1](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0002.md) `sg-form-6-2025__c0002` – «Fr. 3’400 für alleinstehende Steuerpflichtige»
  - [WL SG 2025 S. 27](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0088.md) `sg-wl-2025__c0088` – «Maximaler Abzug Fr. 6’800 Fr. 3’400»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0003.md) `sg-form-32-2025__c0003` – «Verheiratete max. Fr. 6'800 max. Fr. 3'700»

<a id="15-abzug-liegenschaft-unterhalt"></a>
### Ziff. 15 – Unterhalts- und Verwaltungskosten für Liegenschaften (Code 716)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Formular 7 Abschnitt C (Pauschale 20% der Erträge B oder tatsächliche Kosten C2) bzw. Formular 7Z Spalten C1/C2
- **Regel:** Pauschale 20% der Erträge (B) nur für private Liegenschaften, die ganz oder vorwiegend Wohnzwecken dienen, ODER tatsächliche Kosten (Rechnungsdatum 2025, selbst bezahlt, abzüglich Versicherungsleistungen/Förderbeiträge). Wahl pro Liegenschaft. Pauschale umfasst auch Denkmalpflege und Energiespar-/Umweltinvestitionen. Wertvermehrende Aufwendungen nicht abziehbar. Geschäftsliegenschaften in Ziff. 2.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «15. Unterhalts- und Verwaltungskosten für Liegenschaften Formular 7 716»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0161.md) `sg-wl-2025__c0161` – «20% des steuerlich massgebenden Mietertrages oder des steuer-»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0004.md) `sg-form-7-2025__c0004` – «Pauschalabzug 20% der Erträge (B)»

<a id="16-1-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. 16.1 – Verwaltungskosten für Wertschriften und sonstige Kapitalanlagen (Code 220)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.) → Steuerauszug/Depotgebührenausweis; Kurswert fremdverwaltetes Vermögen
- **Regel:** Tatsächliche Kosten (Depot-/Safegebühren, Inkassospesen) oder Pauschale 2 Promille des fremdverwalteten Wertschriftenvermögens, höchstens Fr. 6'000. Nicht abzugsfähig: Courtagen, Emissionsabgabe, Anlage-/Steuerberatung, Vermögensverwaltungsmandate. Darlehen und selbstverwaltete Wertschriften (eigene AG) gelten nicht als fremdverwaltet. Einsatzkosten Geldspiele: 5% des Gewinns, max. Fr. 5'400; Online-Spiele abgebuchte Einsätze, max. Fr. 26'700.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «16.1 Verwaltungskosten für Wertschriften und sonstige Kapitalanlagen 220»
  - [WL SG 2025 S. 27](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0090.md) `sg-wl-2025__c0090` – «2‰ des fremdverwalteten»

<a id="16-2-abzug-drittbetreuung"></a>
### Ziff. 16.2 – Kinderbetreuungskosten bei Drittbetreuung (Code 258)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Formular 10 (Kinderbetreuungsabzug): Rechnungen Kita/Tagesmutter; Vorname Kind, bezahlte Kosten, Name/Adresse Betreuungsperson
- **Regel:** Max. Fr. 26'700 pro Kind unter 14 Jahren, das im gleichen Haushalt lebt; nur bei direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit. Verpflegung nicht abziehbar (ohne separaten Ausweis Kürzung pauschal Fr. 8 pro Tag bei Betreuung ausserhalb des Haushalts). Formular 10 ist nicht im Wiki: Regel aus Wegleitung.
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 26'700 (Kinderdrittbetreuungskosten: höchstens Fr. 26'700 pro Kind unter 14 Jahren, das im gleichen Haushalt lebt; kausaler Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit. Verpflegungskosten nicht abziehbar.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind bis max. CHF 25'800 (Kind unter 14, im gleichen Haushalt, Zusammenhang mit Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit))**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 Jahre (Kinderdrittbetreuung: Kinder unter 14 Jahren.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat)**
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «16.2 Kinderbetreuungskosten bei Drittbetreuung Formular 10 258»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0092.md) `sg-wl-2025__c0092` – «Ein Kinderbetreuungsabzug von maximal Fr. 26’700 pro Kind kann geltend»

<a id="16-3-abzug-parteispenden"></a>
### Ziff. 16.3 – Parteispenden (Code 555)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Formular 5 Rückseite Teil B «Total der Parteispenden»; Spendenbestätigung
- **Regel:** Max. Fr. 10'700 (Alleinstehende, Verwitwete, getrennt Lebende) bzw. Fr. 21'400 (Ehepaare/eingetragene Partnerschaften). Begünstigte Partei: im Parteienregister eingetragen, im kantonalen Parlament vertreten oder bei letzten Wahlen mind. 3% Stimmen. Mitgliederbeiträge, Gesinnungsbeiträge, Spenden, Mandatssteuern.
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'700 (Mitgliederbeiträge und Zuwendungen an politische Parteien: höchstens Fr. 10'700 für Alleinstehende/übrige Steuerpflichtige (Partei im Parteienregister, in kantonalem Parlament vertreten oder mind. 3 % Stimmen).)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 21'400 (Parteispenden: höchstens Fr. 21'400 für gemeinsam steuerpflichtige Ehegatten/eingetragene Partner.)** · Bund **n/a – Bund kennt nur einen Gesamtbetrag von CHF 10'600 (Art. 33 Abs. 1 lit. i DBG); keine Verdoppelung für Ehepaare in der Quelle.**
- **Bund:** Bund: max. Fr. 10'600 (Gesamtbetrag, keine separate Grenze für Ehepaare; Art. 33 Abs. 1 lit. i DBG).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «16.3 Parteispenden Formular 5 555»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0093.md) `sg-wl-2025__c0093` – «Parteispenden können maximal in der Höhe von Fr. 10’700»
  - [Formular 5 SG 2025 S. 2](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0004.md) `sg-form-5-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 16.3»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0004.md) `sg-form-32-2025__c0004` – «Parteispenden max. Fr. 10'600»

<a id="16-4-abzug-weiterbildung"></a>
### Ziff. 16.4 – Kosten berufsorientierte Aus-/Weiterbildung (Code 223 Person 1 / 224 Person 2)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Aufstellung mit Rechnungsdatum, Bezeichnung, Betrag; Kursrechnungen
- **Regel:** Selbst bezahlte berufsorientierte Aus-, Weiterbildungs- und Umschulungskosten max. Fr. 13'000 pro Kalenderjahr und Person; Voraussetzung: erster Abschluss Sek. II oder 20. Altersjahr vollendet (nicht Ausbildung bis zum ersten Abschluss Sek. II). Ohne Nachweis Pauschale Fr. 400 für hauptberuflich Unselbständige (nur Kanton/Gemeinde, nicht Bund). Informatikmittel nur bei zwingender Anschaffung (Bestätigung Kursleitung), bei privater Nutzbarkeit 50%. Vom Arbeitgeber getragene Kosten (Lohnausweis Ziff. 13.3) sind nicht steuerbar und hier nicht abziehbar.
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung: höchstens Fr. 13'000 pro Person und Jahr (Voraussetzung: erster Abschluss Sek II oder 20. Altersjahr vollendet und nicht Ausbildung bis zum ersten Abschluss Sek II). Ohne Nachweis Pauschale Fr. 400 für unselbständig Erwerbende (nur Kanton/Gemeinde).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Bund:** Bund: max. Fr. 13'000, nur effektive Kosten (keine Pauschale).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «16.4 Kosten berufsorientierte Aus-/Weiterbildung Person 1 Aufstellung 223»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0094.md) `sg-wl-2025__c0094` – «von maximal Fr. 13’000 pro Kalenderjahr und Person»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0095.md) `sg-wl-2025__c0095` – «pauschal Fr. 400»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0096.md) `sg-wl-2025__c0096` – «können nur 50% der Aufwendungen als Aus- und Weiterbildungskosten abgezogen werden»

<a id="16-5-abzug-ahv-nichterwerbstaetige"></a>
### Ziff. 16.5 – Übrige Abzüge, z.B. AHV-Beiträge Nichterwerbstätiger (Code 222)

- **Schlüssel:** `abzug.ahv_nichterwerbstaetige` (AHV/IV/EO-Beiträge Nichterwerbstätiger u.ä.) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse) → AHV-Beitragsverfügung für Nichterwerbstätige
- **Regel:** Nur AHV-Beiträge von nichterwerbstätigen Steuerpflichtigen; ordentliche AHV-Beiträge Erwerbstätiger sind bereits in Ziff. 1/2 berücksichtigt. Weitere übrige Abzüge mit Art/Aufstellung.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «16.5 Übrige Abzüge Arten 222»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0097.md) `sg-wl-2025__c0097` – «Als übrige Abzüge, die unter dieser Ziffer aufzuführen sind»

<a id="17-abzug-zweiverdiener"></a>
### Ziff. 17 – Zweiverdienerabzug (Code 226)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Beilage (beide Personen erwerbstätig)
- **Regel:** Gemeinsam Steuerpflichtige, die beide erwerbstätig sind: Fr. 500; gleicher Abzug bei erheblicher Mitarbeit einer Person im Beruf/Geschäft der anderen.
- **Limiten:**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **n/a – Prozentsatz nur bei direkter Bundessteuer (siehe Bund).** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (bei Ehegatten in ungetrennter Ehe mit beidseitigem Erwerbseinkommen))**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **n/a** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum)**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **CHF 500 (Zweiverdienerabzug: Fr. 500 (einmal pro gemeinsam steuerpflichtigem Ehepaar, wenn beide erwerbstätig sind; derselbe Abzug bei erheblicher Mitarbeit eines Ehegatten im Beruf/Geschäft des anderen).)** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum)**
- **Bund:** Bund: 50% des niedrigeren Einkommens, min. Fr. 8'600, max. Fr. 14'100.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «17. Zweiverdienerabzug 226»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0097.md) `sg-wl-2025__c0097` – «Gemeinsam Steuerpflichtige, die beide einer Erwerbstätigkeit nachgehen»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0005.md) `sg-form-32-2025__c0005` – «Zweiverdienerabzug Fr. 500 min. Fr. 8'600»

<a id="18-berechnung-total"></a>
### Ziff. 18 – Total der Abzüge (Code 230)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Summe Ziff. 10 bis 17.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «18. Total der Abzüge 230»

## Einkommensberechnung

<a id="20-berechnung-total"></a>
### Ziff. 20 – Nettoeinkommen (Code 234)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile: Ziffer 7 abzüglich Ziffer 18
- **Regel:** Basis für Selbstbehalt Krankheitskosten (2%) und Limite freiwillige Zuwendungen (20%).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «20. Nettoeinkommen (Ziffer 7 abzüglich Ziffer 18) 234»

<a id="21-1-abzug-krankheitskosten"></a>
### Ziff. 21.1 – Krankheits- und Unfallkosten (Vorkolonne Code 650, Selbstbehalt Code 238, Abzug Code 240)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 6 Rückseite «Total» selbst getragene Kosten (Bruttobetrag abzüglich Beiträge Dritter)
- **Regel:** Nettobetrag (nach Abzug von Vergütungen Dritter) in Vorkolonne; abzugsfähig, soweit er 2% des Nettoeinkommens (Ziff. 20) übersteigt. Diät-Pauschale Fr. 2'500 bei dauernder lebensnotwendiger Diät (z.B. Zöliakie, nicht Diabetes; ärztliche Bescheinigung bei erstmaliger Deklaration). Wird auf Krankenkassen-Zusammenzug verwiesen, detaillierte Leistungsübersicht beilegen.
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **2 % (Krankheits-/Unfallkosten abziehbar, soweit sie 2 % der Nettoeinkünfte (Nettoeinkommen Ziff. 20) übersteigen. Behinderungsbedingte Kosten ohne Selbstbehalt. Pauschale Diät (Zöliakie) Fr. 2'500.)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Bund:** Bund: Selbstbehalt 5% der Nettoeinkünfte.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «abzüglich Selbstbehalt 2% des Nettoeinkommens (Ziffer 20)»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0098.md) `sg-wl-2025__c0098` – «2% des Nettoeinkommens gemäss Ziffer 20 übersteigen»
  - [Formular 6 SG 2025 S. 2](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0003.md) `sg-form-6-2025__c0003` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.1 (Vorkolonne)»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0005.md) `sg-form-32-2025__c0005` – «Selbstbehalt 5% der Nettoeinkünfte»

<a id="21-2-abzug-behinderungskosten"></a>
### Ziff. 21.2 – Behinderungsbedingte Kosten, ohne Selbstbehalt (Code 235)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Formular 6 Rückseite «Behinderungsbedingte Kosten» Total; Verfügung Hilflosenentschädigung
- **Regel:** Selbst getragene Kosten ohne Selbstbehalt, abzüglich Vergütungen Dritter (Hilflosenentschädigung). Pflegeheim (ab Pflegestufe 4 / 21 BESA-Punkten): Fr. 2'000 pro Monat gelten als Lebenshaltungskosten, nur Überschuss abziehbar. Alternativ Pauschale: Hilflosenentschädigung leicht Fr. 2'500, mittel Fr. 5'000, schwer Fr. 7'500; Gehörlose/Dialyse Fr. 2'500 (ärztlicher Fragebogen bei erstmaliger Geltendmachung).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «21.2 Behinderungsbedingte Kosten (ohne Selbstbehalt) Formular 6 235»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0099.md) `sg-wl-2025__c0099` – «Fr. 2’000 pro Monat als nicht abzugsberechtigte Lebenshaltungskosten»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0100.md) `sg-wl-2025__c0100` – «Bezüger einer Hilflosenentschädigung mittleren Grades: Fr. 5’000»

<a id="21-3-abzug-spenden"></a>
### Ziff. 21.3 – Freiwillige Zuwendungen (Code 244)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Formular 5 Rückseite Teil A «Total der Zuwendungen»; Spendenbestätigungen
- **Regel:** Nur an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentlicher/gemeinnütziger Zweck), völlig uneigennützig; nicht für Kultuszwecke. Abzug wenn Total mind. Fr. 100, insgesamt höchstens 20% des Nettoeinkommens (Ziff. 20).
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): Abzug, wenn im Steuerjahr gesamthaft mindestens Fr. 100. Kultuszwecke nicht abziehbar.)** · Bund **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen (CH) bzw. Gemeinwesen: mindestens CHF 100 im Steuerjahr)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: insgesamt höchstens 20 % der Nettoeinkünfte (Nettoeinkommen).)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «21.3 Freiwillige Zuwendungen (wenn mind. Fr.100, max. 20% Ziffer 20) Formular 5 244»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0102.md) `sg-wl-2025__c0102` – «insgesamt höchstens aber 20% des Nettoeinkommens gemäss Ziffer 20»

<a id="22-berechnung-total"></a>
### Ziff. 22 – Reineinkommen (Code 248)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile: Ziffer 20 abzüglich Ziffern 21.1 bis 21.3
- **Regel:** Rechenzeile.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «22. Reineinkommen (Ziffer 20 abzüglich Ziffern 21.1 bis 21.3) 248»

<a id="23-1-sozialabzug-kinder"></a>
### Ziff. 23.1 – Kinderabzug für jedes noch nicht schulpflichtige Kind (Fr. 7'600, Code 252)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Kinder, für deren Unterhalt zur Hauptsache aufgekommen wird)
- **Regel:** Verhältnisse am 31.12.2025 bzw. Ende der Steuerpflicht; bei unterjähriger Steuerpflicht anteilig. Kind, für das Unterhaltsbeiträge nach Ziff. 12.2 abgezogen werden, erhält keinen Kinderabzug.
- **Limiten:**
  - Kinderabzug Vorschulalter (CHF): Kanton **CHF 7'600 (Kinderabzug Fr. 7'600 für jedes unter der elterlichen Sorge/Obhut stehende Kind, das noch nicht schulpflichtig ist (Verhältnisse per 31.12.; Steuerpflichtiger kommt zur Hauptsache für Unterhalt auf und beansprucht keinen Unterhaltsabzug).)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (sozialabzug.kind); Staffelung nach Alter nur kantonal.**
- **Bund:** Bund: Kinderabzug einheitlich Fr. 6'800 pro Kind (kein Vorschul-/Schulabzug, Formular 32 und data/werte/bund/2025); zusätzlich Abzug vom Steuerbetrag Fr. 263 pro Kind (nur Bund).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0011.md) `sg-form-1-2025__c0011` – «23.1 Kinderabzug für jedes noch nicht schulpflichtige Kind Fr. 7’600 252»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0104.md) `sg-wl-2025__c0104` – «Steuerpflichtige, welche für den Unterhalt der Kinder zur Hauptsache aufkom-»

<a id="23-2-sozialabzug-kinder"></a>
### Ziff. 23.2 – Kinderabzug für jedes Kind in Schule oder Ausbildung (Fr. 10'800, Code 254)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Schule/Ausbildung, Dauer bis)
- **Regel:** Auch für volljährige Kinder in schulischer oder beruflicher Ausbildung, wenn zur Hauptsache für Unterhalt aufgekommen wird.
- **Limiten:**
  - Kinderabzug Schulalter (CHF): Kanton **CHF 10'800 (Kinderabzug Fr. 10'800 für jedes Kind (unter Sorge/Obhut oder volljährig) in schulischer oder beruflicher Ausbildung.)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (sozialabzug.kind).**
- **Bund:** Bund: einheitlich Fr. 6'800 pro Kind (Schule/Ausbildung).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0011.md) `sg-form-1-2025__c0011` – «23.2 Kinderabzug für jedes Kind in Schule oder Ausbildung Fr. 10’800 254»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0006.md) `sg-form-32-2025__c0006` – «Fr. 10'800 einheitlich Fr. 6'800»

<a id="23-3-sozialabzug-kinder"></a>
### Ziff. 23.3 – Ausbildungskosten für Kinder in Schule oder Ausbildung (Code 256)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Formular 10 (Ausbildungskosten Kinder): Rechnungen Semestergebühren, Bücher, Fahrkosten ÖV
- **Regel:** Nach Abzug eines Selbstbehalts von Fr. 3'200 und erhaltener Stipendien die effektiven, notwendigen, selbst getragenen Ausbildungskosten, max. Fr. 13'700; nur wenn für das Kind ein Abzug nach Ziff. 23.2 gilt. Nur Kanton/Gemeinde (nicht Bund).
- **Limiten:**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 10'800 (Kinder- bzw. Ausbildungsabzug Fr. 10'800 für Kind in schulischer oder beruflicher Ausbildung (auch volljährig).)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Kinderabzug CHF 6'800 wie für Minderjährige (kein höherer Ausbildungsabzug))**
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0011.md) `sg-form-1-2025__c0011` – «23.3 Ausbildungskosten für Kinder in Schule oder Ausbildung Formular 10 256»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0105.md) `sg-wl-2025__c0105` – «nach Abzug eines Selbstbehaltes von Fr. 3’200»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0105.md) `sg-wl-2025__c0105` – «geltend gemacht werden kann, maximal: 13’700»

<a id="23-4-sozialabzug-unterstuetzung"></a>
### Ziff. 23.4 – Abzug für unterstützte Personen (nur direkte Bundessteuer, Code 264)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Bedürftigkeit; Name/Adresse der unterstützten Person, geleisteter Betrag
- **Regel:** Gilt nur für die direkte Bundessteuer: Fr. 6'800 pro unterstützte erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mind. Fr. 6'800 an den Unterhalt beigetragen wurde. Nicht für Ehegatten und nicht für Kinder mit Kinderabzug. Kantonal kein Abzug.
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **n/a – Gemäss WL 2025 Ziff. 23.4 nur direkte Bundessteuer (Wert siehe data/werte/bund).** · Bund **CHF 6'800 (Unterstützungsabzug pro erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mindestens in Höhe des Abzugs unterstützt; nicht für Ehegatten und Kinder mit Kinderabzug)**
- **Bund:** Nur Bund: Fr. 6'800 pro Person.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0011.md) `sg-form-1-2025__c0011` – «23.4 Abzug für unterstützte Personen ja Anzahl Bescheinigung 264»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0106.md) `sg-wl-2025__c0106` – «Der Abzug von Fr. 6’800 für jede unterstützte Person»

<a id="24-berechnung-total"></a>
### Ziff. 24 – Steuerbares Einkommen gesamt (Code 268)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile: Ziffer 22 abzüglich Ziffern 23.1-23.3
- **Regel:** Rechenzeile (Bund zusätzlich Ziff. 23.4 und weitere Bundesabzüge, von der Behörde angepasst).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0011.md) `sg-form-1-2025__c0011` – «24. Steuerbares Einkommen gesamt (Ziffer 22 abzüglich Ziffern 23.1-23.3) 268»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben (Code 300)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 «Total» Steuerwert per 31.12.2025
- **Regel:** Steuerwert per 31.12.2025 gemäss Wertschriftenverzeichnis (inkl. Kryptowährungen). Kotierte Papiere: Kursliste; Fremdwährungen umrechnen. Ansprüche aus 2. Säule und Säule 3a bis zur Fälligkeit steuerfrei (nicht deklarieren). Hausrat steuerfrei.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «30.1 Wertschriften und Guthaben Formular 2 300»
  - [WL SG 2025 S. 35–36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0121.md) `sg-wl-2025__c0121` – «inkl. Kryptowährungen»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 302)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung (Bestand 31.12., Kursliste)
- **Regel:** Inländisches und ausländisches Bargeld, Gold und Edelmetalle zum Verkehrswert (amtliche Kursliste).
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «30.2 Bargeld, Gold und andere Edelmetalle Aufstellung 302»
  - [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0110.md) `sg-wl-2025__c0110` – «Gold und andere Edelmetalle mit dem Verkehrswert einzusetzen»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen (Code 304)

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Bescheinigung Versicherungsgesellschaft: Rückkaufswert inkl. Überschussanteil per 31.12.
- **Regel:** Rückkaufswert inkl. Überschussanteil; auch laufende und aufgeschobene Renten. Reine Risikoversicherungen ohne Rückkaufswert nicht deklarieren. Bescheinigung beilegen. Zeilenangaben: Versicherungsgesellschaft, Abschlussjahr, Ablaufjahr, Versicherungssumme.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «30.3 Lebens- und Rentenversicherungen Bescheinigung»
  - [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0110.md) `sg-wl-2025__c0110` – «Als steuerbares Vermögen gilt der Rückkaufswert inklusive»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge (Code 306)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Kaufvertrag/Fahrzeugausweis: Art, Kaufpreis, Erwerbsjahr
- **Regel:** Steuerwert = Anschaffungswert abzüglich 20% pro Jahr seit Erwerb.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «30.4 Motorfahrzeuge Art preis jahr 306»
  - [WL SG 2025 S. 33](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0111.md) `sg-wl-2025__c0111` – «eine Wertverminderung von 20% vom Anschaffungswert abgerechnet werden»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Anteile an unverteilten Erbschaften (Code 308)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung Nachlass / Erbteilungsunterlagen
- **Regel:** Ab Todestag deklarationspflichtig, auch wenn Anteile zahlenmässig noch nicht feststehen; ohne enthaltene Liegenschaften (Formular 7). Zusätzlich im Formular 2 Seite 1 (Code 961) vermerken.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «30.5 Anteile an unverteilten Erbschaften Aufstellung 308»
  - [WL SG 2025 S. 33](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0111.md) `sg-wl-2025__c0111` – «Die Erben sind ab Todestag für ihren Anteil de-»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte (Code 310)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung mit mutmasslichem Verkehrswert
- **Regel:** Boote, Reitpferde, Sammlungen, Kunst-/Schmuckgegenstände mit überdurchschnittlichem Wert; ohne Hausrat und persönliche Gebrauchsgegenstände. Verkehrswert.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «30.6 Übrige Vermögenswerte Arten 310»
  - [WL SG 2025 S. 33](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0112.md) `sg-wl-2025__c0112` – «Massgebend ist in der Regel der mutmassliche»

<a id="31-vermoegen-liegenschaften"></a>
### Ziff. 31 – Liegenschaften (Code 710)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Formular 7 Abschnitt A «Steuerwert» (bei mehreren Formular 7Z Spalte A)
- **Regel:** Steuerwert gemäss rechtskräftiger Verkehrs- oder Ertragswertschätzung (SG); Liegenschaften in anderen Kantonen/im Ausland mit dem entsprechenden Wert. Ein Formular 7 pro Liegenschaft.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «31. Liegenschaften Formular 7 710»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0002.md) `sg-form-7-2025__c0002` – «Übertrag in die Steuererklärung Seite 4 Ziffer 31»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0154.md) `sg-wl-2025__c0154` – «bestimmt sich nach der rechtskräftigen Verkehrs- oder Ertragswertschätzung»

<a id="32-1-32-3-vermoegen-uebrige"></a>
### Ziff. 32.1-32.3 – Betriebsvermögen aus selbständiger Erwerbstätigkeit: Geschäftskapital Gesellschaften (Code 314), Aktiven Schlussbilanz (Code 316), landwirtschaftlicher Betrieb (Code 318)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Schlussbilanz (Aktiven), Formular 12 (Landwirtschaft), Angaben Formular 11
- **Regel:** Aktiven gemäss Schlussbilanz (Fahrzeuge, Maschinen, Mobiliar, Geräte); Buchwert der Geschäftsliegenschaften NICHT hier, sondern in Ziff. 31. Geschäftsschulden in Ziff. 34.2.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «32.2 Aktiven gemäss Schlussbilanz per Aufstellung 316»
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «ohne Buchwert der»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 322)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Summe Ziff. 30 bis 32.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «33. Total der Vermögenswerte 322»

<a id="34-1-schulden-privat"></a>
### Ziff. 34.1 – Privatschulden (Code 504)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Leasingvertrag Fahrzeug / Leasingraten-Abrechnung → Formular 5 Teil A: Schuld am 31.12.2025 je Gläubiger (Schuldausweis der Bank)
- **Regel:** Nachgewiesene Schulden per 31.12.2025, voll bei alleiniger Haftung; Solidar-/Bürgschaftsschulden nur soweit selbst zu tragen. Zinsen gehören in Ziff. 11.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «34.1 Privatschulden Formular 5 504»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0117.md) `sg-wl-2025__c0117` – «Nachgewiesene Schulden, für die eine alleinige Haftung besteht»

<a id="34-2-schulden-privat"></a>
### Ziff. 34.2 – Geschäftsschulden (Code 506)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 5 Teil B: Schuld am 31.12. bzw. Bilanzstichtag
- **Regel:** Geschäftsschulden per Bilanzstichtag; geschäftliche Schuldzinsen sind in der Jahresrechnung enthalten und nicht hier aufzuführen.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «34.2 Geschäftsschulden Formular 5 506»
  - [Formular 5 SG 2025 S. 1](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0002.md) `sg-form-5-2025__c0002` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 34.2»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Reinvermögen (Code 326)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile: Ziffer 33 abzüglich 34
- **Regel:** Rechenzeile.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «35. Reinvermögen (Ziffer 33 abzüglich 34) 326»

<a id="36-1-36-3-vermoegen-sozialabzug"></a>
### Ziff. 36.1-36.3 – Sozialabzüge Vermögen: alleinstehend Fr. 75'000 (Code 330), gemeinsam Fr. 150'000 (Code 332), je minderjähriges Kind Fr. 20'000 (Code 334)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien/Kinder Seite 1 (Stichtag 31.12.2025)
- **Regel:** Festbeträge vom Reinvermögen nach den Verhältnissen am 31.12.2025; Kinderabzug für minderjährige Kinder unter elterlicher Sorge/Obhut. Bund kennt keine Vermögenssteuer.
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 75'000 (Sozialabzug auf dem Reinvermögen: Fr. 75'000 für jeden Steuerpflichtigen (Alleinstehende).)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 150'000 (Sozialabzug Vermögen für gemeinsam Steuerpflichtige: Fr. 150'000 (2 x Fr. 75'000).)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 20'000 (Zusätzlicher Vermögens-Sozialabzug Fr. 20'000 pro minderjähriges Kind unter elterlicher Sorge/Obhut, für das ein Kinderabzug beansprucht werden kann.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «36.1 Abzug für alleinstehende Steuerpflichtige Fr. 75’000 330»
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «36.2 Abzug für gemeinsam steuerpflichtige Ehegatten Fr. 150’000 332»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0118.md) `sg-wl-2025__c0118` – «20’000 zusätzlich für jedes minderjährige»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen gesamt (Code 338)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile: Ziffer 35 abzüglich Ziffern 36.1 bis 36.3
- **Regel:** Rechenzeile.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «37. Steuerbares Vermögen gesamt (Ziffer 35 abzüglich Ziffern 36.1 bis 36.3) 338»

## Weitere Angaben

<a id="40-1-40-3-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. 40.1-40.3 – Kapitalleistungen aus Vorsorge: Säule 3a (40.1), 2. Säule (40.2), übrige (40.3)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung / Bank (Auszahlung 2025)
- **Regel:** Im Jahr 2025 erhaltene Kapitalleistungen angeben; bei mehreren Leistungen Gesamtbetrag. Besteuerung gesondert vom übrigen Einkommen mit separater Jahressteuer; Deklaration nur zu Informationszwecken. Nicht in Ziff. 6.4.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0014.md) `sg-form-1-2025__c0014` – «40.1 aus gebundener Vorsorge Säule 3a Bescheinigung»
  - [WL SG 2025 S. 35](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0119.md) `sg-wl-2025__c0119` – «Kapitalleistungen werden gesondert vom übrigen Einkommen besteuert»

<a id="41-berechnung-total"></a>
### Ziff. 41 – Total Kapitalleistungen aus Vorsorge (Code 950)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Summe Ziff. 40.1-40.3
- **Regel:** Rechenzeile; Informationszweck.
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0014.md) `sg-form-1-2025__c0014` – «41. Total Kapitalleistungen aus Vorsorge 950»

## Hilfsblatt Wertschriftenverzeichnis

<a id="form-2-spalte-a-b-einkommen-wertschriften"></a>
### Ziff. Form. 2 Spalte A/B – Verzeichnis der Vermögenswerte: Steuerwert 31.12.2025, Bruttoertrag Spalte A (mit Verrechnungssteuerabzug) / Spalte B (ohne)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Steuerauszug/Bankbescheinigung: Valoren-Nr., Nennwert/Stückzahl, Steuerwert 31.12., Bruttoertrag
- **Regel:** Spalte A: Erträge mit 35% Verrechnungssteuer (u.a. Kundenguthaben mit Bruttozins über Fr. 200, inländische Aktien/Obligationen, Fonds, inländische Lotteriegewinne). Spalte B: ohne Verrechnungssteuer (z.B. Bankzinsen bis Fr. 200, ausländische Titel). Selbst errechnete Zinsen nicht eintragen. Zu- und Abgänge mit Datum und Bankbeleg. Codes: G Geschäftsvermögen, N Nutzniessung, E neuer Titel aus Erbschaft, S aus Schenkung, BP/BG Beteiligung mind. 10%.
- **Quellen:**
  - [Formular 2 SG 2025 S. 2](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0005.md) `sg-form-2-2025__c0005` – «Steuerwert am 31. Dezember 2025»
  - [WL SG 2025 S. 38](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0135.md) `sg-wl-2025__c0135` – «Kundenguthaben, deren Bruttozins Fr. 200 übersteigt»
  - [Formular 2 SG 2025 S. 2](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0006.md) `sg-form-2-2025__c0006` – «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A)»

<a id="form-2-code-999-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 2 Code 999 – Verrechnungssteueranspruch 35% vom Bruttoertrag Total A (Code 999)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Total A × 35%
- **Regel:** Rückerstattung wird über die Steuererklärung beantragt; bei Verwirkung (nicht deklarierte Erträge) kein Anspruch. Stockwerkeigentümer-Erneuerungsfonds: Formular 25 direkt bei ESTV.
- **Quellen:**
  - [Formular 2 SG 2025 S. 2](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0006.md) `sg-form-2-2025__c0006` – «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A) Fr./Rp. 999»

<a id="form-2-code-960-963-info-schenkungen-erbschaften"></a>
### Ziff. Form. 2 Code 960-963 – Fragen Erbschaften/Schenkungen: Erbschaft erhalten (960), unverteilte Erbschaft (961), Schenkung erhalten (962), verschenkt (963)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Erbteilungsakt / Schenkungsvertrag (Datum, Betrag, Verwandtschaftsgrad)
- **Regel:** Nur Information im Wertschriftenverzeichnis: Betrag, Todestag/Teilungsdatum bzw. Schenkungsdatum angeben, Erbteilungsakt beilegen. Erbanteil 961 ohne enthaltene Liegenschaften (Formular 7). Titel aus Erbschaft/Schenkung im Verzeichnis mit Code E bzw. S.
- **Quellen:**
  - [Formular 2 SG 2025 S. 1](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0002.md) `sg-form-2-2025__c0002` – «Haben Sie im Jahr 2025 eine Erbschaft oder ein Vermächtnis erhalten?»
  - [Formular 2 SG 2025 S. 1](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0003.md) `sg-form-2-2025__c0003` – «Haben Sie im Jahr 2025Vermögen verschenkt?»

## Hilfsblatt Berufskosten

<a id="form-4-ziff-1-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.1 – Fahrkosten öffentliche Verkehrsmittel (Code 400 Person 1 / 450 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg → ÖV-Abo/Billett-Beleg; Weg von-nach, Datum von-bis
- **Regel:** Tatsächliche Kosten des öffentlichen Verkehrsmittels für den Arbeitsweg. Kein Abzug wenn dem Arbeitnehmer keine Kosten erwachsen (Sammeltransport, vom Arbeitgeber getragenes GA aus geschäftlichen Gründen): Lohnausweis Feld F muss dann angekreuzt sein, kein Fahrkostenabzug. An Home-Office-Tagen und Tagen ohne Arbeitsleistung keine Fahrkosten. Ziff. 1.1-1.3 zusammen max. Fr. 8'000.
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 pro Person (Maximalabzug, keine Pauschale; bei Teilzeit/unterjährig nicht gekürzt; gilt bei Haupt- und Nebenerwerb insgesamt). Bei direkter Bundessteuer tiefer (Fr. 3'300, siehe data/werte/bund).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Bund:** Bund: Fahrkosten max. Fr. 3'300.
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0001.md) `sg-form-4-2025__c0001` – «1.1 Öffentliche Verkehrsmittel»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0075.md) `sg-wl-2025__c0075` – «muss auf dem Lohnausweis Feld F angekreuzt sein»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0077.md) `sg-wl-2025__c0077` – «Bei Benützung eines öffentlichen Verkehrsmittels (Bahn, Tram, Trolley- oder»

<a id="form-4-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.2 – Fahrkosten Fahrrad, Kleinmotorrad bis 50 cm3 (Code 402 Person 1 / 452 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Belege (Pauschale)
- **Regel:** Pauschal bis Fr. 700 im Jahr (Fahrrad oder Kleinmotorrad mit gelbem Kontrollschild).
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Fahrrad, Motorfahrrad oder Kleinmotorrad bis 50 ccm (gelbes Kontrollschild): Pauschale bis Fr. 700 im Jahr (Voraussetzung: mehr als 10 Minuten zu Fuss zur nächsten ÖV-Haltestelle).)** · Bund **CHF 700 (Pauschale pro Jahr für Fahrrad, Motorfahrrad und Motorrad mit gelbem Kontrollschild; tatsächliche Kosten zusätzlich nicht abziehbar)**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0001.md) `sg-form-4-2025__c0001` – «1.2 Fahrrad, Kleinmotorrad bis 50 cm3 (Kontrollschild mit gelbem Grund) 402»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0077.md) `sg-wl-2025__c0077` – «bis zu Fr. 700 im Jahr»

<a id="form-4-ziff-1-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.3 – Fahrkosten Motorfahrzeug, Fr. 0.70 pro km, Zwischentotal max. Fr. 8'000 (Code 404/406 Person 1; 454/456 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Begründung (Formular), Arbeitstage, km pro Weg; Fahrzeugausweis; Bordbuch bei Geschäftsfahrzeug
- **Regel:** Nur in begründeten Fällen (kein ÖV, Zeitersparnis über 60 Min./Tag, Arbeitgeberverlangen, ÖV unzumutbar mit Arztzeugnis). 70 Rp. pro Fahrkilometer, in der Regel max. 220 Arbeitstage. Zwischentotal 1.1-1.3 max. Fr. 8'000. Geschäftsfahrzeug mit Privatanteil 0,9% pro Monat (10,8% pro Jahr) versteuert: kein Fahrkostenabzug (ausser effektive Abrechnung mit Bordbuch). Home-Office-Tage ausschliessen.
- **Limiten:**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.70 (Privatfahrzeug (Auto) nur in begründeten Fällen (kein zumutbarer öV): Fr. 0.70 pro Fahrkilometer im Steuerjahr 2025.)** · Bund **CHF 0.70 (Privatauto: Abzug pro Fahrkilometer CHF 0.70, nur wenn kein öffentliches Verkehrsmittel verfügbar/zumutbar (Steuerjahr 2025))**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **220 Tage (In der Regel höchstens 220 Arbeitstage pro Jahr (Vollzeit); höhere Anzahl nachzuweisen. Für Homeoffice-Tage und Tage ohne Arbeitsleistung keine Fahrkosten (ausser ÖV-Abo).)** · Bund **n/a – Bund kennt keine Festlegung massgebender Arbeitstage; abziehbar sind die tatsächlichen notwendigen Kosten bis zum Maximalbetrag (Art. 26 Abs. 1 lit. a DBG).**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 pro Person (Maximalabzug, keine Pauschale; bei Teilzeit/unterjährig nicht gekürzt; gilt bei Haupt- und Nebenerwerb insgesamt). Bei direkter Bundessteuer tiefer (Fr. 3'300, siehe data/werte/bund).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Bund:** Bund: Maximalabzug Fahrkosten Fr. 3'300.
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0002.md) `sg-form-4-2025__c0002` – «km x Fr. 0.70 (Kostensatz gemäss Wegleitung) 404»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0002.md) `sg-form-4-2025__c0002` – «Zwischentotal Ziffern 1.1 – 1.3, max. Fr. 8'000»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0077.md) `sg-wl-2025__c0077` – «Bei Benützung eines Motorfahrzeuges in begründeten Fällen: 70 Rappen je»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0076.md) `sg-wl-2025__c0076` – «entsprechend 10,8% pro Jahr»

<a id="form-4-ziff-2-1-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.1 – Mehrkosten auswärtige Verpflegung, Fr. 15 pro Arbeitstag / Fr. 3'200 pro Jahr (Code 408 Person 1 / 458 Person 2)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Belege; Arbeitstage ohne Home-Office
- **Regel:** Nur wenn Arbeitspause die Heimkehr nicht ermöglicht (Hauptmahlzeit nicht zu Hause). Fr. 15 pro auswärtige Hauptmahlzeit, bei regelmässigem Mittagessen max. Fr. 3'200 pro Jahr. Nicht kombinierbar mit Schichtarbeit-Abzug (Ziff. 2.3). Keine Verpflegung an Home-Office-Tagen.
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswärtige Verpflegung: Fr. 15 pro auswärtige Hauptmahlzeit (Mittagessen), wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann.)** · Bund **CHF 15 (Mehrkosten auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (i.d.R. Mittagessen); ausschliesslich Pauschale, wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei regelmässiger auswärtiger Verpflegung (Mittagessen) Fr. 3'200 im Jahr.)** · Bund **CHF 3'200 (Bei ständiger auswärtiger Verpflegung CHF 3'200 pro Jahr (voller Abzug))**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «Pro Arbeitstag Fr. 15 / im Jahr Fr. 3'200 408»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0078.md) `sg-wl-2025__c0078` – «Fr. 15 für jede auswärtige Hauptmahlzeit»

<a id="form-4-ziff-2-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.2 – Verpflegung verbilligt durch Arbeitgeber (Kantine, Gutscheine/Lunch-Checks), Fr. 7.50 pro Tag / Fr. 1'600 pro Jahr (Code 410 Person 1 / 460 Person 2)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Feld G (Kantinenverpflegung / Lunch-Checks)
- **Regel:** Ist im Lohnausweis Feld G angekreuzt (Kantine, Barbeitrag oder Gutscheine/Lunch-Checks des Arbeitgebers), nur halber Abzug: Fr. 7.50 pro Tag, max. Fr. 1'600 pro Jahr (statt Ziff. 2.1). Bei so weitgehender Verbilligung, dass offensichtlich keine Mehrkosten entstehen: kein Abzug.
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Verpflegung in Kantine des Arbeitgebers oder durch Arbeitgeberbeitrag/Gutscheine verbilligt: in der Regel halber Abzug, Fr. 7.50 pro Tag (Lohnausweis Feld G). Keine Mehrkosten bei vollständiger Verbilligung: kein Abzug.)** · Bund **CHF 7.50 (Halber Abzug CHF 7.50 pro Hauptmahlzeit, wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei Verbilligung durch Arbeitgeber: halber Abzug, Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: CHF 1'600 pro Jahr)**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «Pro Arbeitstag Fr. 7.50 / im Jahr Fr. 1'600 410»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0078.md) `sg-wl-2025__c0078` – «In diesem Fall ist auf dem Lohnausweis Feld G»

<a id="form-4-ziff-2-3-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.3 – Schicht-/Nachtarbeit (mind. 8 Stunden durchgehend), Fr. 15 pro Schichttag / Fr. 3'200 pro Jahr (Code 412 Person 1 / 462 Person 2)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 «Bemerkungen» (Anzahl Schichttage) oder separates Arbeitgeberschreiben
- **Regel:** Anzahl geleisteter Schichttage muss der Arbeitgeber im Lohnausweis unter Ziff. 15 (Bemerkungen) oder in separatem Schreiben bescheinigen. Fr. 15 pro Schichttag, ganzjährig max. Fr. 3'200. Nicht zusammen mit Verpflegungsabzug Ziff. 2.1/2.2.
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Schicht-/Nachtarbeit mit durchgehender, mindestens achtstündiger Tätigkeit: Fr. 15 pro Schichttag, bei ganzjähriger Schichtarbeit Fr. 3'200. Nicht kumulierbar mit Abzug für auswärtige Verpflegung; Schichttage vom Arbeitgeber zu bescheinigen.)** · Bund **CHF 15 (Durchgehende Schicht-/Nachtarbeit (gestaffelte Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich): CHF 15 pro ausgewiesenem Tag, bei ganzjähriger Schicht-/Nachtarbeit CHF 3'200 pro Jahr)**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «Pro ausgewiesenen Schichttag Fr. 15 / im Jahr Fr. 3'200 412»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0079.md) `sg-wl-2025__c0079` – «geleisteter Schichttage ist vom Arbeit-»

<a id="form-4-ziff-3-1-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4 Ziff. 3.1 – Pauschalabzug übrige Berufskosten: Fr. 700 + 10% des Nettolohnes, max. Fr. 2'400 (Code 416 Person 1 / 466 Person 2)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Nettolohn gemäss Ziff. 1.1 / Lohnausweis Ziff. 11
- **Regel:** Pauschale ohne Nachweis; auch bei Bezug von ALV-Leistungen sinngemäss. Bei Auszahlung nicht ereignisbezogener Pauschalspesen nicht zusätzlich geltend zu machen.
- **Limiten:**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockelbetrag der Pauschale übrige Berufskosten: Fr. 700 (+ 10 % des Nettolohnes).)** · Bund **n/a – Bund: 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; kein 'fix + %'-Modell.**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Pauschale übrige Berufskosten: Fr. 700 zuzüglich 10 % der Nettoeinkünfte (Nettolohn), höchstens Fr. 2'400; Nachweis höherer Kosten vorbehalten. Nettoeinkünfte = Bruttoeinkünfte abzüglich Beiträge AHV/IV/EO/ALV/UV und BVG (ohne Einkäufe).)** · Bund **3 % (Übrige Berufskosten: 3 % des Nettolohns (Pauschale; Nachweis höherer Kosten möglich); bei Teilzeit/unterjährig angemessen kürzen)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Pauschale übrige Berufskosten höchstens Fr. 2'400.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
- **Bund:** Bund: 3% des Nettolohnes, mind. Fr. 2'000, max. Fr. 4'000.
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «Pauschalabzug: Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2'400 416»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0080.md) `sg-wl-2025__c0080` – «Pauschale von Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2’400»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0002.md) `sg-form-32-2025__c0002` – «max. Fr. 2'400 max. Fr. 4'000»

<a id="form-4-ziff-3-2-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4 Ziff. 3.2 – Tatsächliche übrige Berufskosten anstelle Pauschale (Code 418 Person 1 / 468 Person 2)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Aufstellung/Beiblatt mit Belegen
- **Regel:** Nur wenn die tatsächlichen Kosten die Pauschale übersteigen; Nachweis über Beiblatt, mit Formular 4 einreichen. Entweder Pauschale (3.1) oder effektiv (3.2).
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «3.2 Anstelle des Pauschalabzuges: tatsächliche Berufskosten»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0080.md) `sg-wl-2025__c0080` – «so können gegen Nachweis die tatsächlichen Auf»

<a id="form-4-ziff-4-1-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4 Ziff. 4.1 – Wochenaufenthalt: Unterkunft, ortsübliche Kosten Zimmer (Code 426 Person 1 / 476 Person 2)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag/Beleg Zimmer: Monate × Betrag
- **Regel:** Nur wenn tägliche Rückkehr aus zeitlichen oder finanziellen Gründen unzumutbar und steuerlicher Wohnsitz am Heimatort. Tatsächliche Kosten für ein Zimmer (nicht Wohnung), je nach Arbeitsort Fr. 500 bis Fr. 800 pro Monat. Heimfahrten unter Ziff. 1.
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Wochenaufenthalt: tatsächliche Kosten für ein auswärtiges Zimmer (nicht Wohnung), je nach Arbeitsort Fr. 500 bis Fr. 800 pro Monat (Fr. 800 in Zürich, Bern, Basel, Lausanne, Genf und grösseren Kurorten, sonst bis Fr. 500). Voraussetzung: tägliche Rückkehr nicht zumutbar; Fahrkosten separat unter Fahrkosten.** · Bund **Mehrkosten Unterkunft: ortsübliche Auslagen für ein Zimmer (nicht eine Wohnung) abziehbar; Fahrkosten der regelmässigen Heimkehr bis zum Maximalbetrag nach Art. 5 Abs. 1 BKV**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0004.md) `sg-form-4-2025__c0004` – «4.1 Unterkunft: Ortsübliche Kosten für ein Zimmer»
  - [WL SG 2025 S. 24–25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0081.md) `sg-wl-2025__c0081` – «je nach Arbeitsort Fr. 500 bis Fr. 800 pro Monat»

<a id="form-4-ziff-4-2-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4 Ziff. 4.2 – Wochenaufenthalt: Verpflegung Fr. 30 pro Arbeitstag / Fr. 6'400 pro Jahr (Code 428 Person 1 / 478 Person 2)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (bei Verbilligung der Mittagsmahlzeit)
- **Regel:** Fr. 30 pro Tag, ganzjährig max. Fr. 6'400. Bei Verbilligung der Mahlzeiten durch den Arbeitgeber (Kantine, Kostenbeitrag, Feld G) Fr. 22.50 pro Tag bzw. Fr. 4'800 pro Jahr.
- **Limiten:**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 6'400 (Wochenaufenthalt Verpflegung: Fr. 30 im Tag, bei ganzjährigem Wochenaufenthalt Fr. 6'400 im Jahr; bei Verbilligung durch Arbeitgeber Fr. 22.50 im Tag bzw. Fr. 4'800 im Jahr.)** · Bund **CHF 6'400 (Auswärtiger Wochenaufenthalt: Verpflegung CHF 30 pro Tag, max. CHF 6'400 pro Jahr; bei Verbilligung CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr; Nachweis höherer Kosten ausgeschlossen)**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0004.md) `sg-form-4-2025__c0004` – «Pro Arbeitstag Fr. 30 / im Jahr Fr. 6'400»
  - [WL SG 2025 S. 24–25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0081.md) `sg-wl-2025__c0081` – «gesamthaft Fr. 22.50 im Tag, bzw. Fr. 4’800 im Jahr»

<a id="form-4-ziff-5-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 4 Ziff. 5 – Kosten bei unselbständiger Nebenerwerbstätigkeit: Pauschale 20% der Nettoeinkünfte, min. Fr. 800, max. Fr. 2'400 (Code 432) bzw. tatsächliche Kosten (Code 434); Person 2: 482/484

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 des Nebenerwerbs (Nettolohn Ziff. 1.2)
- **Regel:** Auslagen bis Höhe des Nettolohns, soweit Nebeneinkünfte netto Fr. 800 nicht übersteigen; darüber 20% (min. Fr. 800, max. Fr. 2'400). Nachweis höherer Kosten vorbehalten. Kein Anspruch ohne Haupterwerbstätigkeit bei Dritten (Pensionierte, Hausfrauen); in der Regel nicht für VR-Honorare.
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Unselbständiger Nebenerwerb: Pauschale 20 % der Nettoeinkünfte aus der Nebentätigkeit, mindestens Fr. 800, höchstens Fr. 2'400 pro Jahr. Bei Nettolohn bis Fr. 800: Auslagen bis zur Höhe des Nettolohns. Kein Anspruch ohne Haupterwerb bei Dritten; in der Regel nicht für VR-Honorare.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge))**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb-Pauschale mindestens Fr. 800 (Nettoeinkünfte bis Fr. 800: Abzug bis zur Höhe des Nettolohns).)** · Bund **CHF 800 (Minimum Pauschale Nebenerwerb)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb-Pauschale höchstens Fr. 2'400 im Jahr.)** · Bund **CHF 2'400 (Maximum Pauschale Nebenerwerb)**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0004.md) `sg-form-4-2025__c0004` – «5.1 Pauschalabzug: 20% der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400 432»
  - [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0082.md) `sg-wl-2025__c0082` – «Steuerpflichtige, die keine Haupterwerbstätigkeit bei Dritten ausüben»

<a id="form-4-ziff-6-berechnung-total"></a>
### Ziff. Form. 4 Ziff. 6 – Total der Berufskosten (Code 438 Person 1 / 488 Person 2)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Ziff. 1 bis 5
- **Regel:** Übertrag in Steuererklärung Seite 3 Ziff. 10.1 (Person 1) bzw. 10.2 (Person 2). Formular 4 Vorderseite Person 1, Rückseite Person 2.
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0004.md) `sg-form-4-2025__c0004` – «6. Total der Berufskosten 438»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0004.md) `sg-form-4-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 10.1»

<a id="lohnausweis-feld-f-abzug-berufskosten-fahrkosten"></a>
### Ziff. Lohnausweis Feld F – Lohnausweis Feld F: unentgeltliche Beförderung zwischen Wohn- und Arbeitsort

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld F (Kästchen angekreuzt)
- **Regel:** Feld F angekreuzt = dem Arbeitnehmer erwachsen keine Kosten (Sammeltransport, vom Arbeitgeber getragenes GA aus geschäftlichen Gründen): kein Fahrkostenabzug in Formular 4 Ziff. 1. Hinweis: das Lohnausweis-Merkblatt in den Wiki-Quellen (bund-wl-lohnausweis-2026) gilt nur für 2026; Regel hier nach WL SG 2025.
- **Quellen:**
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0075.md) `sg-wl-2025__c0075` – «Ein Abzug für die Fahrt zur Arbeit ist deshalb nicht möglich»

<a id="lohnausweis-ziff-15-abzug-berufskosten-verpflegung"></a>
### Ziff. Lohnausweis Ziff. 15 – Lohnausweis Ziff. 15 Bemerkungen: Anzahl Schichttage; «Einer von xx Lohnausweisen»

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 (Bemerkungen)
- **Regel:** Schichtarbeit: Anzahl Schichttage hier bescheinigt (Grundlage für Fr. 15 pro Tag, Formular 4 Ziff. 2.3). Mehrere Lohnausweise des gleichen Arbeitgebers: Vermerk «Einer von xx Lohnausweisen».
- **Quellen:**
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0079.md) `sg-wl-2025__c0079` – «Ziffer 15 im Lohnausweis»
  - [WL SG 2025 S. 14](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0039.md) `sg-wl-2025__c0039` – «Ziffer 15 des Lohnaus»

## Hilfsblatt Schulden

<a id="form-5-teil-a-schulden-privat"></a>
### Ziff. Form. 5 Teil A – Private Schulden und private Schuldzinsen (→ Ziff. 34.1 und 11)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung) → Schuldenausweis Gläubiger: Schuld am 31.12.2025 und Schuldzinsen 2025
- **Regel:** Pro Gläubiger Name/Adresse, Schuld per 31.12.2025 und bezahlte Schuldzinsen 2025; Totale nach Ziff. 34.1 (Schuld) und Ziff. 11 (Zinsen). Belege auf Verlangen.
- **Quellen:**
  - [Formular 5 SG 2025 S. 1](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0001.md) `sg-form-5-2025__c0001` – «Total private Schulden und private Schuldzinsen»

<a id="form-5-teil-b-schulden-privat"></a>
### Ziff. Form. 5 Teil B – Geschäftsschulden (→ Ziff. 34.2)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz: Schuld am 31.12. bzw. Bilanzstichtag
- **Regel:** Nur Schuldbetrag; Geschäftszinsen sind in der Jahresrechnung enthalten und hier nicht aufzuführen.
- **Quellen:**
  - [Formular 5 SG 2025 S. 1](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0002.md) `sg-form-5-2025__c0002` – «sind in der Jahresrechnung enthalten und deshalb hier nicht aufzuführen»

## Hilfsblatt Zuwendungen

<a id="form-5-r-ckseite-teil-a-abzug-spenden"></a>
### Ziff. Form. 5 Rückseite Teil A – Freiwillige Zuwendungen (→ Ziff. 21.3)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigung: Datum, Institution, Betrag
- **Regel:** Institution mit Name/Adresse, Datum, Betrag 2025; Total nach Ziff. 21.3 (mind. Fr. 100, max. 20% des Nettoeinkommens).
- **Quellen:**
  - [Formular 5 SG 2025 S. 2](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0003.md) `sg-form-5-2025__c0003` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.3»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0102.md) `sg-wl-2025__c0102` – «insgesamt höchstens aber 20% des Nettoeinkommens gemäss Ziffer 20»

<a id="form-5-r-ckseite-teil-b-abzug-parteispenden"></a>
### Ziff. Form. 5 Rückseite Teil B – Parteispenden (→ Ziff. 16.3)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Bestätigung der Partei: Datum, Partei, Betrag
- **Regel:** Pro Partei Datum und Betrag 2025; Total nach Ziff. 16.3 (max. Fr. 10'700 / Fr. 21'400).
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'700 (Mitgliederbeiträge und Zuwendungen an politische Parteien: höchstens Fr. 10'700 für Alleinstehende/übrige Steuerpflichtige (Partei im Parteienregister, in kantonalem Parlament vertreten oder mind. 3 % Stimmen).)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 21'400 (Parteispenden: höchstens Fr. 21'400 für gemeinsam steuerpflichtige Ehegatten/eingetragene Partner.)** · Bund **n/a – Bund kennt nur einen Gesamtbetrag von CHF 10'600 (Art. 33 Abs. 1 lit. i DBG); keine Verdoppelung für Ehepaare in der Quelle.**
- **Quellen:**
  - [Formular 5 SG 2025 S. 2](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0004.md) `sg-form-5-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 16.3»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0093.md) `sg-wl-2025__c0093` – «Parteispenden können maximal in der Höhe von Fr. 10’700»

## Hilfsblatt Versicherungsprämien

<a id="form-6-teil-a-abzug-versicherungspraemien"></a>
### Ziff. Form. 6 Teil A – Bezahlte Versicherungsprämien und Sparzinsen: a. Krankenversicherung brutto, b. Unfallversicherung (ohne NBU), c. Lebens-/Rentenversicherungen, d. Sparzinsen, e. abzüglich Prämienverbilligungen

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Prämienrechnung/Jahresabrechnung Krankenkasse (brutto), Bescheinigung Prämienverbilligung, Zinsen gemäss Formular 2
- **Regel:** Tatsächlich bezahlte Prämien; Familien tragen Prämien der ganzen Familie ein. Prämienverbilligungen (IPV) für Steuerpflichtigen und Kinder abziehen. Total (A) wird mit Maximalabzug (B) verglichen.
- **Quellen:**
  - [Formular 6 SG 2025 S. 1](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0001.md) `sg-form-6-2025__c0001` – «a. Private Krankenversicherung (brutto)»
  - [Formular 6 SG 2025 S. 1](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0001.md) `sg-form-6-2025__c0001` – «e. abzüglich Prämienverbilligungen»

<a id="form-6-teil-b-c-abzug-versicherungspraemien"></a>
### Ziff. Form. 6 Teil B/C – Maximaler Abzug (Fr. 6'800 / Fr. 3'400, Zuschläge) und zulässiger Abzug (→ Ziff. 14)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenblatt
- **Regel:** Gemeinsam Fr. 6'800 (+ Fr. 1'100 ohne BVG/3a bei beiden), alleinstehend Fr. 3'400 (+ Fr. 500), + Fr. 1'100 pro Kind mit Kinderabzug nach Ziff. 23.1/23.2. Abzug = niedrigerer Betrag von A und B.
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 6'800 (Versicherungsprämien und Sparzinsen: Gesamtbetrag Fr. 6'800 für gemeinsam steuerpflichtige Ehegatten (Kranken-, Unfall-, Lebens-/Rentenversicherung, Zinsen von Sparkapitalien; Prämienverbilligungen sind anzurechnen).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 3'400 (Versicherungsprämien und Sparzinsen: Gesamtbetrag Fr. 3'400 für übrige Steuerpflichtige.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 7'900 (Gemeinsam Steuerpflichtige ohne Abzug von Beiträgen an 2. Säule/Säule 3a: Maximalabzug erhöht sich um Fr. 1'100 (6'800 + 1'100 = 7'900). Bei Verheirateten müssen die Voraussetzungen bei beiden Partnern erfüllt sein.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an Säule 2/3a (Erhöhung um die Hälfte))**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 3'900 (Übrige Steuerpflichtige ohne Abzug von Beiträgen an 2. Säule/Säule 3a: Erhöhung um Fr. 500 (3'400 + 500 = 3'900).)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'100 (Zuschlag Fr. 1'100 für jedes Kind, für das ein Kinderabzug geltend gemacht werden kann (Gesetz); WL: bis Fr. 1'100.)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
- **Quellen:**
  - [Formular 6 SG 2025 S. 1](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0002.md) `sg-form-6-2025__c0002` – «Der niedrigere Betrag von (A) und (B)»
  - [Formular 6 SG 2025 S. 1](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0002.md) `sg-form-6-2025__c0002` – «Fr. 1’100 zusätzlich für jedes Kind»

## Hilfsblatt Krankheitskosten

<a id="form-6-r-ckseite-krankheitskosten-abzug-krankheitskosten"></a>
### Ziff. Form. 6 Rückseite Krankheitskosten – Krankheits- und Unfallkosten: Rechnungsdatum, Arzt/Zahnarzt/Spital, Bruttobetrag, abzüglich Beiträge Dritter, selbst getragene Kosten (→ Ziff. 21.1 Vorkolonne)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Rechnungen und Leistungsabrechnung der Krankenkasse (Franchise/Selbstbehalt/Zahnarzt etc.)
- **Regel:** Nur tatsächlich selbst getragene Kosten (Beiträge Dritter wie Versicherungen, Krankenkassen, Hilflosenentschädigung abziehen). Bei Verweis auf Kassenauszug zwingend Aufstellung mit Details (inkl. Leistungsübersicht) einreichen. Krankenkassenprämien gehören NICHT hierher (Ziff. 14).
- **Quellen:**
  - [Formular 6 SG 2025 S. 2](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0003.md) `sg-form-6-2025__c0003` – «Abzugsfähig sind die tatsächlich selbst getragenen Kosten»

<a id="form-6-r-ckseite-behinderungskosten-abzug-behinderungskosten"></a>
### Ziff. Form. 6 Rückseite Behinderungskosten – Behinderungsbedingte Kosten (→ Ziff. 21.2)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Rechnungen, Verfügung Hilflosenentschädigung, Heimabrechnung
- **Regel:** Total nach Ziff. 21.2, ohne Selbstbehalt; Details siehe Ziff. 21.2.
- **Quellen:**
  - [Formular 6 SG 2025 S. 2](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0004.md) `sg-form-6-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.2»

## Hilfsblatt Liegenschaften

<a id="form-7-abschnitt-a-vermoegen-liegenschaften"></a>
### Ziff. Form. 7 Abschnitt A – Angaben zur Liegenschaft / Steuerwert (→ Ziff. 31)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Steuerliche Schätzung: Grundstücknummer, Steuerwert; Anteil Person 1/2 in %, Nutzungsart
- **Regel:** Ein Formular pro Liegenschaft; Zugang/Wegfall im Jahr 2025 mit Datum und Grund (Kauf, Verkauf, Schenkung, Erbschaft) angeben. Bei mehr als einer Liegenschaft Übertrag in Formular 7Z.
- **Quellen:**
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0001.md) `sg-form-7-2025__c0001` – «Pro Liegenschaft ist ein separates Formular zu verwenden»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0154.md) `sg-wl-2025__c0154` – «Im Weiteren sind die Anteile von Person 1 und Person 2 in Prozenten anzugeben»

<a id="form-7-abschnitt-b-a-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 7 Abschnitt B.a – Eigenmietwert (abzüglich 30%, Unternutzungs-/Härtefallabzug)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Schätzungsverfügung: Mietwert
- **Regel:** Eigenmietwert der am Wohnort dauernd selbstbewohnten Liegenschaft (Erstwohnung) um 30% herabgesetzt; übrige Objekte voller Mietwert. Unternutzungsabzug = (reduzierter EMW × nicht benutzte Zimmer) / (Zimmerzahl + 2), nur bei dauernder, überprüfbarer Nichtbenützung (leer, unmöbliert). Härtefallabzug von Amtes wegen für AHV-Rentner (max. 10% des Brutto-EMW), nicht bei steuerbarem Vermögen über Fr. 600'000. Teiljahr: anteilig.
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **30 % (Eigenmietwert des am Wohnsitz dauernd selbst bewohnten Eigenheims wird um 30 % herabgesetzt; Unternutzung auf Antrag; Reduktion für Personen im AHV-Alter bei offensichtlichem Missverhältnis (Härtefall Art. 14 StV: Mietwert über 30 % der Bruttoeinkünfte und Vermögen höchstens Fr. 600'000).)** · Bund **n/a – Eigenmietwert wird nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt (Art. 21 Abs. 2 DBG); Abschaffung per 01.01.2029 beschlossen, 2025–2028 gilt bisheriges Recht. Der Eigenmietwert für die direkte Bundessteuer wird im kantonalen Veranlagungsverfahren festgesetzt; ein dort vorgesehener Abzug für die DBSt (z.B. TG 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Quellen:**
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0003.md) `sg-form-7-2025__c0003` – «Eigenmietwert abzüglich 30%»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0156.md) `sg-wl-2025__c0156` – «Der Eigenmietwert des am Wohnsitz dauernd selbstbewohnten Eigenhei-»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0158.md) `sg-wl-2025__c0158` – «Übersteigt das steuerbare Vermögen Fr. 600’000»

<a id="form-7-abschnitt-b-b-einkommen-liegenschaften-mietertrag"></a>
### Ziff. Form. 7 Abschnitt B.b – Erträge Fremdnutzung und Leistungen Dritter (Miet-/Pachtzinsen, Geschäftsräume, abzüglich Nebenkosten)

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Mietzinsabrechnung/Liegenschaftenrechnung
- **Regel:** Miet-/Pachtzinsen ohne Nebenkosten (vertraglich inbegriffene Nebenkosten mit tatsächlichen Auslagen abziehen); inkl. Mietzinsreduktion Hauswart; Leistungen Dritter (Zinszuschüsse, Subventionen, Versicherungsleistungen). Möblierte Wohnung: i.d.R. 20% Einschlag. Überschüssiger PV-Strom nicht hier, sondern Ziff. 6.3.
- **Quellen:**
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0003.md) `sg-form-7-2025__c0003` – «Total steuerbare Erträge Fremdnutzung und Leistungen Dritter»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0159.md) `sg-wl-2025__c0159` – «Zum steuerbaren Mietertrag gehören die Miet- und Pachtzinsen bei»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0160.md) `sg-wl-2025__c0160` – «Der Einschlag beträgt in der Regel 20%.»

<a id="form-7-abschnitt-c-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 7 Abschnitt C – Unterhalts- und Verwaltungskosten: Pauschalabzug 20% der Erträge (B) oder tatsächliche Kosten (Rückseite, C2)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Rechnungen mit Datum 2025, Name Rechnungsteller, Beschreibung, Rechnungstotal netto, Anteil Anlagekosten (nicht abziehbar)
- **Regel:** Pauschale nur für private Wohnliegenschaften; sonst tatsächliche Kosten (Instandhaltung, Instandstellung, Ersatzbeschaffung, Betriebs-/Verwaltungskosten, Denkmalpflege, Energiespar-/Umweltinvestitionen, Rückbaukosten Ersatzneubau). Abzüglich Versicherungsleistungen/Förderbeiträge. Wertvermehrende Anteile (Anlagekosten) nicht abziehbar. Übertrag nach Ziff. 15.
- **Quellen:**
  - [Formular 7 SG 2025 S. 2](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0005.md) `sg-form-7-2025__c0005` – «Abzugsfähig sind nur die selbst bezahlten Kosten»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0161.md) `sg-wl-2025__c0161` – «Die Pauschale umfasst alle Aufwendungen inklusive Kosten denkmalpflegerischer Arbeiten»

<a id="form-7z-berechnung-total"></a>
### Ziff. Form. 7Z – Zusammenzug aller Liegenschaften: Steuerwert (A), Erträge (B), Pauschalabzug (C1), tatsächliche Kosten (C2)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Übertrag aus Formularen 7
- **Regel:** Nur bei mehr als einer Liegenschaft. Totale nach Seite 4 Ziff. 31 (A), Seite 2 Ziff. 5 (B), Seite 3 Ziff. 15 (C1+C2).
- **Quellen:**
  - [Formular 7Z SG 2025 S. 1](../../chunks/sg/2025/sg-form-7z-2025/sg-form-7z-2025__c0001.md) `sg-form-7z-2025__c0001` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 31 Seite 2 Ziffer 5 Seite 3 Ziffer 15»
