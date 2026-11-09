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
- **Rein:** Lohnausweis (je Arbeitgeber einer) → Ziff. 11 Nettolohn · Lohnausweis → inkl. Nebenbezüge (Familienzulagen, Provisionen, Gratifikationen, Mitarbeiteraktien); Zulagen ausserhalb LA → Ziff. 3.5
- **Rechnen:** Σ Nettolohn gemäss Lohnausweis aller Haupterwerbs-Arbeitgeber je Person (Bruttolohn − AHV/IV/EO/ALV/NBUV − ordentliche BVG-Beiträge)
- **Regel:** Nettolohn gemäss Lohnausweis einsetzen (Bruttolohn abzüglich obligatorische Sozialversicherungsbeiträge und ordentliche BVG-Beiträge). Pro Arbeitgeber ein Lohnausweis. Berufskosten separat in Ziff. 10 (Formular 4). Familienzulagen, die nicht im Lohnausweis stehen (z.B. Arbeitgeber FL), in Ziff. 3.5. Lohnausweis Ziff. 10.2 (BVG-Einkauf) ist hier schon abgezogen, nicht nochmals in Ziff. 13.2. Lohnausweis Ziff. 13.3 (vom Arbeitgeber getragene Aus-/Weiterbildung) nicht steuerbar, nicht in Ziff. 16.4 abziehen.
- **Beachten:** Teilzeitstellen zusammenzählen bis Mindestquote zwei Drittel überschritten; nur weitere untergeordnete Tätigkeit → Ziff. 1.2
- **Beachten:** Spesen steuerbar, soweit kein Ersatz berufsnotwendiger Auslagen (Nachweis Empfänger); Pauschalspesen immer im Lohnausweis
- **Beachten:** Vom Arbeitgeber getragene berufsorientierte Aus-/Weiterbildung ist nicht steuerbar
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) `sg-form-1-2025__c0004` – «1.1 Aus Haupterwerbstätigkeit Person 1 Lohnausweis 100»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0042.md) `sg-wl-2025__c0042` – «Einzusetzen ist der Nettolohn gemäss Lohnausweis»
  - [WL SG 2025 S. 14](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0039.md) `sg-wl-2025__c0039` – «festgesetzte Besoldung, aber auch die Nebenbezüge wie Familienzulagen»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0041.md) `sg-wl-2025__c0041` – «Spesenentschädigungen sind dem steuerbaren Einkommen zuzurechnen»
  - [WL SG 2025 S. 14](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0040.md) `sg-wl-2025__c0040` – «Nicht steuerbar sind die vom Arbeitgeber getragenen Kosten der berufsorientierten»
  - [StB 39 Nr. 9 S. 2](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0007.md) `sg-stb-39-9__c0007` – «bis die Mindestquote von zwei Drittel überschritten wird»
  - [Formular 12 2025 S. 1](../../chunks/bund/2025/bund-form-12-2025/bund-form-12-2025__c0001.md) `bund-form-12-2025__c0001` – «Bezüge 2025 (gemäss Ziffer 11 des Lohnausweises)»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Aus Nebenerwerbstätigkeit unselbständig (Code 104 Person 1 / 106 Person 2)

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn) des Nebenarbeitgebers
- **Rein:** Lohnausweis Nebenarbeitgeber → Ziff. 11 Nettolohn · Abrechnung/Bescheinigung je Nebentätigkeit (Provisionen, Gutachten, Lehrtätigkeit, Vereinsleitung, Hauswartung) → Entschädigung · Mietvertrag Hauswart → Differenz normaler zu reduziertem Mietzins
- **Rechnen:** Σ Nettolöhne aller Nebenerwerbe je Person + (normaler − reduzierter Mietzins); Art der Tätigkeit angeben
- **Regel:** Nebenerwerb = Tätigkeit neben einem Haupterwerb, grundsätzlich für einen anderen Arbeitgeber. Auch Mietzinsreduktion (z.B. Hauswart) als Einkommen deklarieren. Berufskostenpauschale für Nebenerwerb: Formular 4 Ziff. 5.
- **Beachten:** Setzt einen Haupterwerb voraus; Überstunden beim Hauptarbeitgeber sind kein Nebenerwerb
- **Beachten:** Nur eine Beschäftigung (z.B. Rentner mit Teilpensum) ist immer Haupterwerb → Ziff. 1.1
- **Beachten:** Pauschale Form. 4 Ziff. 5.1: min(max(20% × Σ Nebenerwerb netto; 800); 2'400; Nettoeinkünfte); Bund gleiche Eckwerte
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Unselbständiger Nebenerwerb: Pauschale 20 % der Nettoeinkünfte aus der Nebentätigkeit, mindestens Fr. 800, höchstens Fr. 2'400 pro Jahr. Bei Nettolohn bis Fr. 800: Auslagen bis zur Höhe des Nettolohns. Kein Anspruch ohne Haupterwerb bei Dritten; in der Regel nicht für VR-Honorare.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge))**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb-Pauschale mindestens Fr. 800 (Nettoeinkünfte bis Fr. 800: Abzug bis zur Höhe des Nettolohns).)** · Bund **CHF 800 (Minimum Pauschale Nebenerwerb)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb-Pauschale höchstens Fr. 2'400 im Jahr.)** · Bund **CHF 2'400 (Maximum Pauschale Nebenerwerb)**
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) `sg-form-1-2025__c0004` – «1.2 Aus Nebenerwerbstätigkeit Person 1 Lohnausweis 104»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0043.md) `sg-wl-2025__c0043` – «Als Nebenerwerb gilt eine Tätigkeit, die gleichzeitig neben einem Haupterwerb»
  - [StB 39 Nr. 9 S. 2–3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0009.md) `sg-stb-39-9__c0009` – «Überstunden für den Hauptarbeitgeber gelten nicht als Nebenerwerbstätigkeit»
  - [StB 39 Nr. 9 S. 2](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0008.md) `sg-stb-39-9__c0008` – «Ein Erwerbstätiger mit nur einer Beschäftigung führt immer eine Haupterwerbstätigkeit aus»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0004.md) `sg-form-4-2025__c0004` – «5.1 Pauschalabzug: 20% der Nettoeinkünfte, mindestens Fr. 800,»
  - [StB 39 Nr. 9 S. 3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0012.md) `sg-stb-39-9__c0012` – «Die Pauschale von 20% errechnet sich aus der Summe aller Nebenerwerbseinkünfte»
  - [StB 39 Nr. 9 S. 3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0012.md) `sg-stb-39-9__c0012` – «höchstens ein Pauschalabzug in gleicher Höhe zulässig»
  - [Formular 12 2025 S. 1](../../chunks/bund/2025/bund-form-12-2025/bund-form-12-2025__c0001.md) `bund-form-12-2025__c0001` – «Bezüge 2025 (gemäss Ziffer 11 des Lohnausweises)»

<a id="1-3-einkommen-unselbstaendig-vr-honorare"></a>
### Ziff. 1.3 – Sitzungsgelder, VR-Honorare usw. (Code 108 Person 1 / 110 Person 2)

- **Schlüssel:** `einkommen.unselbstaendig.vr_honorare` (VR-Honorare, Sitzungsgelder, Tantiemen (wo separat ausgewiesen, z.B. SG/AR Ziff. 1.3)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 6 (Verwaltungsratsentschädigungen) bzw. Bescheinigung der Gesellschaft/Behörde
- **Rein:** Lohnausweis (Doppel) der Gesellschaft für das Mandat → Bezüge gemäss Lohnausweis Ziff. 11 · Bescheinigung Behörde/Gemeinde → Sitzungs- und Taggelder
- **Rechnen:** Σ Sitzungs-/Taggelder, VR-Honorare und Tantiemen je Person, soweit nicht bereits in Ziff. 1.1/1.2 deklariert
- **Regel:** Nur soweit nicht bereits mit den übrigen Erwerbseinkünften deklariert (Doppelerfassung vermeiden). Behördentätigkeit: Steuerbuch SG StB 39 Nr. 4.
- **Beachten:** VR zugleich Angestellter: alle Bezüge auf einem Lohnausweis → schon in Ziff. 1.1, nicht doppelt erfassen
- **Beachten:** Tantiemen: Kalenderjahr massgebend, in dem sie beschlossen und ausgerichtet/gutgeschrieben wurden
- **Beachten:** Nebenerwerbspauschale i.d.R. nicht für VR-Honorare (Unkosten meist zusätzlich vergütet)
- **Bemerkung:** korrigiert durch Prüfung: Lohnausweis-Ziffer für VR-Entschädigungen ist Ziff. 6 (nicht Ziff. 4 = Kapitalleistungen); Beleg: Lohnausweis-Wegleitung (im Wiki nur 2026, Rz 30), Formularstruktur gilt unverändert.
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) `sg-form-1-2025__c0004` – «1.3 Sitzungsgelder, VR-Honorare usw. Person 1 Bescheinigung 108»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0044.md) `sg-wl-2025__c0044` – «Sitzungs- und Taggelder, Verwaltungsratshonorare und Tantiemen»
  - [Formular 12 2025 S. 1](../../chunks/bund/2025/bund-form-12-2025/bund-form-12-2025__c0001.md) `bund-form-12-2025__c0001` – «Bezüge 2025 (gemäss Ziffer 11 des Lohnausweises)»
  - [Formular 12 2025 S. 2](../../chunks/bund/2025/bund-form-12-2025/bund-form-12-2025__c0003.md) `bund-form-12-2025__c0003` – «sind sämtliche Bezüge aus beiden Funktionen auf»
  - [Formular 12 2025 S. 2](../../chunks/bund/2025/bund-form-12-2025/bund-form-12-2025__c0003.md) `bund-form-12-2025__c0003` – «Absatz 2 DBG ein Doppel des Lohnausweises zuzustellen»
  - [Formular 12 2025 S. 2](../../chunks/bund/2025/bund-form-12-2025/bund-form-12-2025__c0002.md) `bund-form-12-2025__c0002` – «einem Lohnausweis aufzuführen. Bei der Bescheinigung von»
  - [Formular 12 2025 S. 2](../../chunks/bund/2025/bund-form-12-2025/bund-form-12-2025__c0002.md) `bund-form-12-2025__c0002` – «Tantiemen ist das Kalenderjahr massgebend»
  - [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0082.md) `sg-wl-2025__c0082` – «für Einkünfte aus Verwaltungsratstätigkeit, weil die damit verbundenen Unkosten»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit: Industrie-, Handels-, Gewerbebetriebe, Landwirtschaft, freie Berufe (Code 112 Person 1 / 114 Person 2)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Erfolgsrechnung/Reingewinn der Jahresrechnung
- **Rein:** Jahresrechnung (Bilanz, Erfolgsrechnung) der 2025 abgeschlossenen Geschäftsjahre → Reingewinn · Eigenkapital-/Privatkonti und Abschreibungstabellen → Beilage · Ohne Buchführungspflicht: Aufstellung Aktiven/Passiven, Einnahmen/Ausgaben, Privatentnahmen/-einlagen (ESTV-Form. 15a)
- **Rechnen:** Reingewinn gemäss Jahresrechnung inkl. Naturalbezüge/Privatanteile − darin enthaltene Familienzulagen (→ Ziff. 3.5) − Liquidationsgewinn (bei separater Besteuerung)
- **Regel:** Reingewinn nach den im Kalenderjahr 2025 abgeschlossenen Bilanzen/Erfolgsrechnungen; Bilanz, Erfolgsrechnung, Eigenkapitalkonti und Abschreibungstabellen beilegen. Ohne Buchführungspflicht: Aufstellung über Aktiven/Passiven und Einnahmen/Ausgaben. Beteiligungserträge >= 10% separat (Ziff. 4.3). Familienzulagen im Reingewinn: Gewinn entsprechend gekürzt, Ziff. 3.5.
- **Beachten:** Privatanteil Haushalts-Nebenkosten (falls dem Betrieb belastet): Fr. 3'540 + 900 je weiterer Erwachsener + 600 je Kind pro Jahr
- **Beachten:** Eigene BVG-Beiträge nur als Arbeitgeberanteil (ohne Personal: Hälfte); Rest, Einkäufe, Säule 3a → Ziff. 13
- **Beachten:** Beteiligungserträge ≥ 10% separat (Code BG → Ziff. 4.3); Liquidationsgewinn (ab 55. Altersjahr/Invalidität) in Beilage
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) `sg-form-1-2025__c0004` – «2.1 Person 1 112»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0045.md) `sg-wl-2025__c0045` – «Das Einkommen aus selbständiger Erwerbstätigkeit umfasst alle Einkünfte aus»
  - [WL SG 2025 S. 16](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0046.md) `sg-wl-2025__c0046` – «eine Aufstellung über Aktiven und Passiven, Einnahmen und Ausgaben sowie»
  - [WL SG 2025 S. 16](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0047.md) `sg-wl-2025__c0047` – «mindestens 10%, sind diese separat zu deklarieren»
  - [WL SG 2025 S. 16](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0048.md) `sg-wl-2025__c0048` – «die Naturalbezüge jeder Art»
  - [WL SG 2025 S. 19](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0061.md) `sg-wl-2025__c0061` – «ist dieser entsprechend gekürzt zu deklarieren»
  - [WL SG 2025 S. 16](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0049.md) `sg-wl-2025__c0049` – «Beträge als Privatanteil an den Unkosten anzurechnen»
  - [WL SG 2025 S. 17–18](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0054.md) `sg-wl-2025__c0054` – «Personal leistet. Ist kein solches Personal vorhanden, so gilt die Hälfte»
  - [WL SG 2025 S. 20](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0066.md) `sg-wl-2025__c0066` – «bender (Code «BG» im Wertschriftenverzeichnis)»
  - [WL SG 2025 S. 17](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0051.md) `sg-wl-2025__c0051` – «a) nach dem vollendeten 55. Altersjahr oder»
  - [WL SG 2025 S. 17](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0052.md) `sg-wl-2025__c0052` – «bereinigt um den Liquidationsgewinn, ist in der Steuererklärung aufzuführen»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Aus Kollektiv-, Kommandit- und einfachen Gesellschaften (Code 120 Person 1 / 122 Person 2)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Angaben der Firma im Formular 11 (Kollektiv- und Kommanditgesellschaften)
- **Rein:** Formular 11 der Kollektiv-/Kommanditgesellschaft → Anteil Einkünfte inkl. Kapitalerträge · Abrechnung einfache Gesellschaft (z.B. Konsortium) → Anteil am Ergebnis
- **Rechnen:** Σ Gewinnanteile gemäss Formular 11 der Firma (inkl. Kapitalerträge) + Anteile an einfachen Gesellschaften, je Person
- **Regel:** Einkünfte gemäss Formular 11 der Gesellschaft (inkl. Kapitalerträge); auch Beteiligung an einfacher Gesellschaft (z.B. Konsortium). Achtung: SG-Ziff. 2.2 ist Gesellschaftsbeteiligung, nicht Nebenerwerb selbständig.
- **Beachten:** VSt auf Kapitalerträgen der Gesellschaft nicht im persönlichen Antrag; Gesellschaft fordert mit Form. 25 bei ESTV zurück
- **Beachten:** Gewinn aus Veräusserung von Anteilen an der Personengesellschaft: mit letzter Jahresrechnung (Schlussabrechnung)
- **Beachten:** Form. 2 Seite 1: Frage Beteiligung an Kollektiv-/Kommanditgesellschaft beantworten (Firma angeben)
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) `sg-form-1-2025__c0004` – «2.2 Aus Kollektiv-, Kommandit- und einfachen Gesellschaften»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0045.md) `sg-wl-2025__c0045` – «unter Ziffer 2.2 anzugeben»
  - [WL SG 2025 S. 36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0124.md) `sg-wl-2025__c0124` – «Kollektiv- und Kommanditgesellschaften dürfen nicht in die persönlichen»
  - [WL SG 2025 S. 16](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0047.md) `sg-wl-2025__c0047` – «bei der Veräusserung von Anteilsrechten an einer Personengemeinschaft»
  - [Formular 2 SG 2025 S. 1](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0004.md) `sg-form-2-2025__c0004` – «Sind Sie an einer Kollektiv- oder Kommanditgesellschaft beteiligt?»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV/IV-Renten zu 100% (Code 126 Person 1 / 128 Person 2)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung Ausgleichskasse (Jahresbetrag brutto)
- **Rein:** Rentenbescheinigung Ausgleichskasse/IV → Jahresbetrag ordentliche und ausserordentliche AHV-/IV-Renten
- **Rechnen:** Σ AHV-/IV-Renten des Steuerjahres je Person, zu 100%
- **Regel:** Ordentliche und ausserordentliche AHV-/IV-Renten voll deklarieren. Ergänzungsleistungen nicht hier (steuerfrei, siehe Ziff. 8.2).
- **Beachten:** Ergänzungsleistungen nicht hier: steuerfrei, nur Information in Ziff. 8.2
- **Beachten:** Hilflosenentschädigung nicht hier: steuerfrei, Information in Ziff. 8.3
- **Beachten:** IV-Taggelder (Ersatz für Erwerbseinkommen) nicht hier, sondern Ziff. 3.3
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0005.md) `sg-form-1-2025__c0005` – «3.1 AHV/IV-Renten (zu 100%) Person 1 Bescheinigung 126»
  - [WL SG 2025 S. 18](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0056.md) `sg-wl-2025__c0056` – «sind in vollem Umfang zu deklarieren, nicht aber die Ergänzungsleistungen»
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0007.md) `sg-form-1-2025__c0007` – «8.2 Ergänzungsleistungen / Überbrückungsleistungen für ältere Arbeitslose 291»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0072.md) `sg-wl-2025__c0072` – «Hilflosenentschädigungen sind steuerfrei»
  - [WL SG 2025 S. 19](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0060.md) `sg-wl-2025__c0060` – «IV-Taggelder gehören zum steuerbaren Einkommen und sind unter»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen mit steuerbarem Prozentsatz (Code 130 Person 1 / 132 Person 2)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente), Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Rentenbescheinigung Pensionskasse/Versicherer: Jahresrente brutto; steuerbarer Prozentsatz in Vorkolonne
- **Rein:** Rentenbescheinigung Pensionskasse/früherer Arbeitgeber → Jahresrente brutto (Vorkolonne) + steuerbarer % · Bescheinigung Versicherer (Säule 3a/3b, Unfall-, Haftpflicht-, Leibrentenversicherung) → Rente bzw. steuerbarer Ertragsanteil · Verfügung/Abrechnung Militärversicherung (nach dem 1. Januar 1994 verfügt/revidiert) → beilegen
- **Rechnen:** je Rente: Brutto × steuerbarer % → Hauptkolonne (2. Säule 100%, Altfall 80%; Säule 3a und reine Risikoversicherung 100%; Leibrente: Ertragsanteil)
- **Regel:** Voller Betrag und Prozentsatz in Vorkolonne, Nettobetrag in Hauptkolonne. 2. Säule 100% (80% nur wenn Rentenbeginn vor 1.1.2002, Vorsorgeverhältnis vor 1.1.1985 und Versicherter >= 20% der Beiträge erbracht hat); Säule 3a und reine Risikoversicherungen 100%; Leibrenten: Ertragsanteil (neu variabel, Versicherer bescheinigt bzw. ESTV publiziert). Mehrere Renten separat auflisten.
- **Beachten:** 80% nur kumulativ: Rentenbeginn vor 2002, Vorsorgeverhältnis vor 1985 und mind. 20% der Beiträge selbst erbracht
- **Beachten:** Leibrente VVG: Ertragsanteil bescheinigt der Versicherer; OR-/ausländische Leibrenten: ESTV berechnet/publiziert
- **Beachten:** Mehrere Renten separat aufstellen; Kapitalleistungen aus Vorsorge nicht hier → Seite 4, Ziff. 40
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0005.md) `sg-form-1-2025__c0005` – «3.2 Renten/Pensionen»
  - [WL SG 2025 S. 18](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0058.md) `sg-wl-2025__c0058` – «100% in allen andern Fällen»
  - [WL SG 2025 S. 18](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0057.md) `sg-wl-2025__c0057` – «einschliesslich der vom früheren Arbeitgeber ausgerichteten Ruhegehälter»
  - [WL SG 2025 S. 18](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0057.md) `sg-wl-2025__c0057` – «Haftpflichtversicherung, gebundene Selbstvorsorge Säule 3a, freie»
  - [WL SG 2025 S. 18](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0059.md) `sg-wl-2025__c0059` – «nach VVG bescheinigen ihn die Versicherer»
  - [WL SG 2025 S. 18](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0059.md) `sg-wl-2025__c0059` – «Militärversicherungsleistungen, die nach dem 1. Januar 1994 neu ver»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0070.md) `sg-wl-2025__c0070` – «Vorsorge sind auf Seite 4 der»
  - [WL SG 2025 S. 35](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0119.md) `sg-wl-2025__c0119` – «In Ziffer 40.1 bis 40.3 sind die im Jahr 2025 erhaltenen Kapitalleistungen aus»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigung / Taggelder IV, Kranken-, Unfallversicherung (Code 134 Person 1 / 136 Person 2)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung Versicherung/EO (Brutto- bzw. Nettoauszahlung)
- **Rein:** Taggeldabrechnung Kranken-/Unfallversicherung bzw. IV → Taggelder, soweit nicht im Lohnausweis · EO-Abrechnung Ausgleichskasse (Militär, Zivilschutz, Mutterschaft) → Entschädigung, soweit nicht im Lohnausweis
- **Rechnen:** Σ Taggelder IV/KV/UV + EO-Entschädigungen je Person, ohne bereits im Lohnausweis enthaltene Beträge
- **Regel:** Nur soweit nicht im Lohnausweis enthalten. IV-Taggelder hier. EO (Militär, Zivilschutz, Mutterschaft) hier, soweit nicht im Lohnausweis; bei Selbständigen nur bei Nettoauszahlung durch Ausgleichskasse, bei Bruttoauszahlung in der Jahresrechnung verbuchen.
- **Beachten:** Selbständige: EO nur bei Nettoauszahlung (AHV abgezogen) hier; Bruttoauszahlung in der Jahresrechnung verbuchen
- **Beachten:** Selbst getragene Krankheits-/Unfall-/Behinderungskosten: Formular 6 → Ziff. 21.1/21.2
- **Beachten:** Nicht anzugeben: Unterstützungen bei Bedürftigkeit, IV-Kostenbeiträge (Eingliederung, Hilfsmittel, Sonderschulung)
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0005.md) `sg-form-1-2025__c0005` – «3.3 Erwerbsausfallentschädigung Person 1 Bescheinigung 134»
  - [WL SG 2025 S. 19](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0060.md) `sg-wl-2025__c0060` – «Taggelder aus Invaliden-, Kranken- und Unfallversicherung sind voll-»
  - [WL SG 2025 S. 16–17](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0050.md) `sg-wl-2025__c0050` – «sind unter Ziffer 3.3 zu deklarieren, sofern die AHV-Beiträge durch die Ausgleichs-»

<a id="3-4-einkommen-ersatz-taggelder"></a>
### Ziff. 3.4 – Arbeitslosen-Taggelder (Code 138 Person 1 / 140 Person 2)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Arbeitslosenkasse
- **Rein:** Bescheinigung der Arbeitslosenkasse → ausbezahlte Taggelder (beilegen) · Lohnausweis → prüfen, ob ALV-Taggelder dort bereits bescheinigt sind (dann nicht hier)
- **Rechnen:** Σ ALV-Taggelder gemäss Bescheinigung der Arbeitslosenkasse je Person, ohne vom Arbeitgeber im Lohnausweis bescheinigte Bezüge
- **Regel:** Nur Bezüge, die nicht im Lohnausweis des Arbeitgebers bescheinigt sind. Bescheinigung der Arbeitslosenkasse beilegen.
- **Beachten:** Kanton: bei ALV-Bezug Pauschale übrige Berufskosten (Fr. 700 + 10% Nettolohn, max. Fr. 2'400) sinngemäss abziehbar
- **Beachten:** Arbeitslose: Verpflegungsabzug analog möglich, wenn Verpflegung wegen Stellensuche auswärts
- **Limiten:**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockelbetrag der Pauschale übrige Berufskosten: Fr. 700 (+ 10 % des Nettolohnes).)** · Bund **n/a – Bund: 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; kein 'fix + %'-Modell.**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Pauschale übrige Berufskosten: Fr. 700 zuzüglich 10 % der Nettoeinkünfte (Nettolohn), höchstens Fr. 2'400; Nachweis höherer Kosten vorbehalten. Nettoeinkünfte = Bruttoeinkünfte abzüglich Beiträge AHV/IV/EO/ALV/UV und BVG (ohne Einkäufe).)** · Bund **3 % (Übrige Berufskosten (Art. 26 Abs. 1 lit. c DBG): Pauschale 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; anstelle der Pauschale ist der Nachweis höherer tatsächlicher übriger Berufskosten möglich. Fahrkosten (lit. a, max. 3'300 gemäss DBG 2025; WL 2a 2025 nennt 3'200 – Widerspruch siehe berufskosten.fahrkosten.max) und Verpflegung (lit. b) werden zusätzlich abgezogen. Bei Teilzeit/Teiljahr angemessen kürzen.)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Pauschale übrige Berufskosten höchstens Fr. 2'400.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0005.md) `sg-form-1-2025__c0005` – «3.4 Arbeitslosen-Taggelder Person 1 Bescheinigung 138»
  - [WL SG 2025 S. 19](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0060.md) `sg-wl-2025__c0060` – «Über nicht im Lohnausweis aufgeführte Bezüge ist eine Bescheinigung beizulegen»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0080.md) `sg-wl-2025__c0080` – «sinngemäss in Abzug gebracht werden»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0080.md) `sg-wl-2025__c0080` – «eine Pauschale von Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2’400,»
  - [StB 39 Nr. 8 S. 1](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0001.md) `sg-stb-39-8__c0001` – «Diese Voraussetzung erfüllt in analoger Anwendung auch ein Arbeitsloser,»

<a id="3-5-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.5 – Von Ausgleichskassen direkt ausbezahlte Familienzulagen (Code 142)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung Familienausgleichskasse
- **Rein:** Bescheinigung Familienausgleichskasse → direkt ausbezahlte Kinder-/Ausbildungszulagen · Selbständige: Buchungsnachweis → im Reingewinn verbuchte Familienzulagen (nicht AHV-pflichtig)
- **Rechnen:** Σ direkt ausbezahlte Kinder- und Ausbildungszulagen (nicht im Lohnausweis); Selbständige: Reingewinn Ziff. 2 um denselben Betrag kürzen
- **Regel:** Nur Zulagen, die nicht im Lohnausweis stehen (z.B. Arbeitgeber im Fürstentum Liechtenstein). Bei Selbständigen: Leistungen der Familienausgleichskasse (nicht AHV-pflichtig) hier, Reingewinn Ziff. 2 entsprechend gekürzt.
- **Beachten:** Zulagen im Lohnausweis sind schon in Ziff. 1.1 enthalten → nicht doppelt deklarieren
- **Beachten:** Typischer Fall: Arbeitgeber im Fürstentum Liechtenstein; Selbständige legen den Buchungsnachweis bei
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0005.md) `sg-form-1-2025__c0005` – «3.5 Von Ausgleichskassen direkt ausbezahlte Familienzulagen 142»
  - [WL SG 2025 S. 19](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0061.md) `sg-wl-2025__c0061` – «die von Ausgleichskassen direkt ausbezahlt werden und somit nicht im Lohnaus»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0042.md) `sg-wl-2025__c0042` – «etc. nicht im Lohnausweis enthalten (z.B. Arbeitgeber Fürstentum Liechtenstein),»
  - [WL SG 2025 S. 14](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0039.md) `sg-wl-2025__c0039` – «festgesetzte Besoldung, aber auch die Nebenbezüge wie Familienzulagen»
  - [WL SG 2025 S. 16–17](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0050.md) `sg-wl-2025__c0050` – «Leistungen aus Familienausgleichskassen (Haushaltungs- und Familien»

<a id="4-1-einkommen-wertschriften"></a>
### Ziff. 4.1 – Einkünfte aus Wertschriften und Guthaben inkl. Lotterie-/Geldspielgewinne (Code 146)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Formular 2: Total Erträge (Spalten A + B) abzüglich Geschäfts- und Beteiligungserträge
- **Rein:** Steuerauszug Bank/Depot → Bruttoerträge und Steuerwerte, Form. 2 Abschnitt A (mit VSt) / B (ohne VSt) · Zinsausweise Konten → Bruttozins; Lotto-/Totobescheinigung → Bargewinne aus inländischen Lotterien/Geldspielen in Spalte A (VSt); ausländische Geldspielgewinne und alle Naturalpreise in Spalte B; Übertrag Ziff. 4.1 · Formular DA-1 → Total Steuerwerte/Bruttoerträge ausländischer Titel mit Quellensteuer, Übertrag ins Form. 2 · Formular 2 → Total Erträge nach Abzugszeilen G/BG, BP, BG
- **Rechnen:** Form. 2: Σ Bruttoerträge A + B (inkl. DA-1, Ergänzungsblätter) − Abzugszeilen G/BG, BP (→ Ziff. 4.2) und BG (→ Ziff. 4.3)
- **Regel:** Übertrag aus Formular 2 (Total, abzüglich G/BG und BP-Erträge). Bruttoerträge deklarieren. Bankzinsen bis Fr. 200 pro Konto/Bank verrechnungssteuerfrei (Spalte B), darüber Spalte A. Dividenden: GV-Beschluss massgebend. Steuerbare Geldspielgewinne: nur einzelne Gewinne über den Schwellen (siehe WL). Ausländische Erträge mit Quellensteuer: DA-1.
- **Beachten:** Bankzinsen ≤ Fr. 200/Kalenderjahr VSt-frei → Abschnitt B; bei VSt-Abzug Bruttozins → A + Bankbeleg; nichts selbst errechnen
- **Beachten:** Geldspielgewinn steuerbar je Einzelgewinn > Kanton Fr. 1'069'800 / Bund Fr. 1'070'400; Verkaufsförderung > Fr. 1'100
- **Beachten:** Nicht rückforderbare ausl. Quellensteuer ≤ Fr. 100: keine Anrechnung, als Vermögensverwaltungskosten abziehbar
- **Limiten:**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'069'800 (Einzelne Gewinne aus Grossspielen (Geldspielgesetz) und Online-Spielbankenspielen sind steuerfrei bis Fr. 1'069'800.)** · Bund **CHF 1'070'400 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'070'400)**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'100 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (nicht dem Geldspielgesetz unterstehend) steuerfrei, sofern Fr. 1'100 nicht überschritten werden. Gewinne aus Kleinspielen (Geldspielgesetz) sind steuerfrei (lit. p).)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'100)**
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «4.1 aus Wertschriften und Guthaben 146»
  - [Formular 2 SG 2025 S. 2](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0006.md) `sg-form-2-2025__c0006` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 30.1 Seite 2 Ziffer 4.1»
  - [WL SG 2025 S. 37](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0130.md) `sg-wl-2025__c0130` – «sind bis und mit Fr. 200 je Kalenderjahr verrechnungssteuerfrei»
  - [WL SG 2025 S. 20](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0064.md) `sg-wl-2025__c0064` – «Steuerbar sind einzelne Gewinne aus Online-Spielbankenspielen, soweit»
  - [WL SG 2025 S. 41](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0145.md) `sg-wl-2025__c0145` – «nicht rückforderbaren Steuern gemäss DA-1 den Betrag von Fr. 100»
  - [WL SG 2025 S. 41](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0145.md) `sg-wl-2025__c0145` – «Das Total der Steuerwerte und Bruttoerträge ist aus dem Formular DA-1 in das»
  - [WL SG 2025 S. 41](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0145.md) `sg-wl-2025__c0145` – «ist als Vermögensverwaltungskosten ab»
  - [Formular 2 SG 2025 S. 1](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0004.md) `sg-form-2-2025__c0004` – «Ergänzungsblätter Steuerauszüge Bankbescheinigungen»
  - [WL SG 2025 S. 38](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0135.md) `sg-wl-2025__c0135` – «Bargewinne aus inländischen Lotterien und anderen Geldspielen»
  - [WL SG 2025 S. 40](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0139.md) `sg-wl-2025__c0139` – «Bargewinne aus ausländischen Lotterien und anderen Geldspielen sowie alle»

<a id="4-2-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.2 – Beteiligungen an Gesellschaften ab 10 Prozent, Privatvermögen (Code 147)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2: Erträge Code BP (ohne Vorzeichen)
- **Rein:** Steuerauszug/Dividendenabrechnung → Bruttoertrag der Beteiligung ≥ 10% (Privatvermögen) · Formular 2 → Erträge Code «BP», Übertrag ohne Vorzeichen
- **Rechnen:** Σ Bruttoerträge Code BP zu 100%; Reduktion 30% separat in Ziff. 4.4
- **Regel:** 100% der Erträge deklarieren; Beteiligung mind. 10% am Grund-/Stammkapital. Im Wertschriftenverzeichnis Code BP; Übertrag in Ziff. 4.2. Die Reduktion von 30% (Teilbesteuerung 70%) wird in Ziff. 4.4 abgezogen.
- **Beachten:** Voraussetzung: mind. 10% am Grund- oder Stammkapital einer Kapitalgesellschaft/Genossenschaft
- **Beachten:** Dividenden: Beschluss der Generalversammlung massgebend, nicht das Geschäftsjahr
- **Beachten:** Bund: ebenfalls Teilbesteuerung 70% (Kreisschreiben Nr. 22a ESTV)
- **Bund:** Bund: ebenfalls Teilbesteuerung 70% (Kreisschreiben Nr. 22a ESTV).
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «4.2 aus Beteiligungen an Gesellschaften ab 10 Prozent (Privatvermögen) 147»
  - [WL SG 2025 S. 20](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0065.md) `sg-wl-2025__c0065` – «Zu deklarieren sind 100% der Erträge»
  - [WL SG 2025 S. 38](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0131.md) `sg-wl-2025__c0131` – «Für Dividenden ist der Beschluss der Generalversammlung massgebend»
  - [Formular 2 SG 2025 S. 2](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0006.md) `sg-form-2-2025__c0006` – «Abzüglich Erträge aus Privatbeteiligung (BP) Übertrag in Steuererkl. Ziff. 4.2 (ohne Vorzeichen)»

<a id="4-3-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.3 – Beteiligungen an Gesellschaften ab 10 Prozent, Geschäftsvermögen (Code 149)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 2: Erträge Code BG; verbuchte Erträge der Jahresrechnung
- **Rein:** Jahresrechnung/Buchhaltung → im Reingewinn verbuchte Beteiligungserträge (brutto oder netto) · Formular 2 → Erträge Code «BG», Übertrag in Ziff. 4.3 ohne Vorzeichen
- **Rechnen:** Σ Erträge Code BG (≥ 10%, Geschäftsvermögen); dieselben verbuchten Erträge in Form. 2 unter «Abzüglich G und BG» abziehen
- **Regel:** Verbuchte Erträge (brutto/netto) unter «Abzüglich Geschäftswertschriften bzw. -erträge (G und BG)» im Formular 2 abziehen und hier deklarieren, um Doppelerfassung zu vermeiden.
- **Beachten:** Als verbucht nur den tatsächlich im Reingewinn enthaltenen Brutto- oder Nettoertrag abziehen
- **Beachten:** Abweichendes Geschäftsjahr: für die VSt-Rückforderung Kalenderjahreswerte deklarieren
- **Beachten:** Bund: ebenfalls Teilbesteuerung 70% (Kreisschreiben Nr. 23a ESTV); Reduktion 30% in Ziff. 4.4
- **Bund:** Bund: ebenfalls Teilbesteuerung 70% (Kreisschreiben Nr. 23a ESTV).
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «4.3 aus Beteiligungen an Gesellschaften ab 10 Prozent (Geschäftsvermögen) 149»
  - [WL SG 2025 S. 20](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0066.md) `sg-wl-2025__c0066` – «Dadurch wird eine doppelte Berück-»
  - [WL SG 2025 S. 40](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0141.md) `sg-wl-2025__c0141` – «im Reingewinn enthaltene Brutto- oder Nettoertrag abgezogen werden»
  - [WL SG 2025 S. 40](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0141.md) `sg-wl-2025__c0141` – «Auch wenn das Datum des Geschäftsabschlusses vom Kalenderjahr (31.12.)»
  - [Formular 2 SG 2025 S. 2](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0006.md) `sg-form-2-2025__c0006` – «Abzüglich Erträge aus Geschäftsbeteiligung (BG) Übertrag in Steuererkl. Ziff. 4.3 (ohne Vorzeichen)»
  - [WL SG 2025 S. 20](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0065.md) `sg-wl-2025__c0065` – «Die steuerliche Reduktion von 30% ist durch den Steuerpflichtigen zu berechnen»

<a id="4-4-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 4.4 – Abzug Teilbesteuerung Beteiligungserträge (Code 150, 30%)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → 30% der Summe Ziff. 4.2 und 4.3
- **Rein:** Übertrag aus Ziff. 4.2 (BP) und Ziff. 4.3 (BG)
- **Rechnen:** − 30% × (Ziff. 4.2 + Ziff. 4.3); E-Tax SG rechnet automatisch
- **Regel:** Abzug beträgt 30% der Einkünfte aus Beteiligungen (Ziff. 4.2 + 4.3); von der steuerpflichtigen Person selbst zu berechnen (in E-Tax SG automatisch). Als Minusposten im Einkünfteteil, nicht im Abzugsteil.
- **Beachten:** Als Minusposten im Einkünfteteil (Code 150) einsetzen, nicht unter den Abzügen
- **Beachten:** Bund: ebenfalls Teilbesteuerung 70% der Beteiligungserträge
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «4.4 Abzug Teilbesteuerung Beteiligungserträge 150»
  - [WL SG 2025 S. 20](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0065.md) `sg-wl-2025__c0065` – «Die steuerliche Reduktion von 30% ist durch den Steuerpflichtigen zu berechnen»

<a id="5-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. 5 – Ertrag aus Liegenschaften (Code 712)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Formular 7 Abschnitt B «Total Erträge a. und b.» (bei mehreren Liegenschaften Formular 7Z Spalte B)
- **Rein:** Schätzungsentscheid (Verkehrs-/Ertragswertschätzung) → Eigenmietwert · Mietverträge/Aufstellung (Form. 7M) → Miet-/Pachtzinsen ohne Nebenkosten, Leistungen Dritter · Formular 7 B «Total Erträge a. und b.» → Ziff. 5 (mehrere Liegenschaften: Form. 7Z Spalte B)
- **Rechnen:** Σ Liegenschaften: EMW − 30% (selbstbewohnte Erstwohnung) − Unternutzung [EMW red. × leere Zimmer ÷ (Zimmer + 2)] + Mieten ohne NK + Leistungen Dritter
- **Regel:** Summe aus Eigenmietwert (Erstwohnung um 30% reduziert) und Mietertrag Fremdnutzung. Unterhalt separat in Ziff. 15 (nicht netto verrechnen). Geschäftsliegenschaften in Ziff. 2.
- **Beachten:** Kauf/Verkauf im Jahr: Mietwert anteilsmässig; Zweit-/Ferienwohnung und Vermietetes ohne 30%-Herabsetzung
- **Beachten:** Härtefallabzug (AHV-Alter, von Amtes wegen): steuerbarer EMW > 30% Bruttoeinkünfte, Vermögen ≤ Fr. 600'000; max. 10% Brutto-EMW
- **Beachten:** Möbliert vermietet: i.d.R. 20% Einschlag; PV-Stromertrag über Eigenverbrauch → Ziff. 6.3
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **30 % (Eigenmietwert des am Wohnsitz dauernd selbst bewohnten Eigenheims wird um 30 % herabgesetzt; Unternutzung auf Antrag; Reduktion für Personen im AHV-Alter bei offensichtlichem Missverhältnis (Härtefall Art. 14 StV: Mietwert über 30 % der Bruttoeinkünfte und Vermögen höchstens Fr. 600'000).)** · Bund **n/a – Eigenmietwert wird nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt (Art. 21 Abs. 2 DBG); Abschaffung per 01.01.2029 beschlossen, 2025–2028 gilt bisheriges Recht. Der Eigenmietwert für die direkte Bundessteuer wird im kantonalen Veranlagungsverfahren festgesetzt; ein dort vorgesehener Abzug für die DBSt (z.B. TG 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Quellen:**
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0003.md) `sg-form-7-2025__c0003` – «Total Erträge a. und b.»
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «5. Ertrag aus Liegenschaften Formular 7 712»
  - [WL SG 2025 S. 20](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0067.md) `sg-wl-2025__c0067` – «Anzugeben sind die Einkünfte aus Liegenschaften des Privatvermögens»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0156.md) `sg-wl-2025__c0156` – «mes (Erstwohnung) wird um 30% herabgesetzt. Für alle übrigen Objekte ist der»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0158.md) `sg-wl-2025__c0158` – «Der Abzug kann maximal 10% des Brutto-»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0158.md) `sg-wl-2025__c0158` – «30% der Bruttoeinkünfte übersteigt»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0158.md) `sg-wl-2025__c0158` – «Übersteigt das steuerbare Vermögen Fr. 600’000»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0159.md) `sg-wl-2025__c0159` – «Zum steuerbaren Mietertrag gehören die Miet- und Pachtzinsen bei»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0159.md) `sg-wl-2025__c0159` – «Subventionen und Versicherungsleistungen. Erträge aus Stromerzeugung,»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0160.md) `sg-wl-2025__c0160` – «abgegolten wird. Der Einschlag beträgt in»
  - [StB 34 Nr. 1 S. 2–3](../../chunks/sg/dauernd/sg-stb-34-1/sg-stb-34-1__c0008.md) `sg-stb-34-1__c0008` – «Zweitwohnungen, Ferienwohnungen sowie von vermieteten Objekten»

<a id="6-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 6.1 – Unterhaltsbeiträge erhalten: für Steuerpflichtige (Code 154) / für minderjährige Kinder (Code 156)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil, Zahlungsnachweise (Jahressumme)
- **Rein:** Scheidungsurteil/Trennungsvereinbarung → periodische Unterhaltsbeiträge (Alimente) · Zahlungsnachweise → im Jahr erhaltene Beträge, getrennt für sich und für minderjährige Kinder
- **Rechnen:** Σ erhaltene periodische Alimente für sich → Code 154; Σ Kinderalimente für Kinder unter eigener Sorge/Obhut → Code 156
- **Regel:** Periodische Unterhaltsbeiträge für sich und für Kinder unter Obhut getrennt aufführen. Beim Zahlenden abziehbar (Ziff. 12.1/12.2). Unterhalt an Volljährige: beim Zahlenden nicht abziehbar, beim Empfänger nicht steuerbar.
- **Beachten:** Unterhalt für volljährige Kinder: beim Empfänger nicht steuerbar, beim Zahler nicht abziehbar
- **Beachten:** Spiegelbild: zahlende Person zieht die Beiträge in Ziff. 12.1/12.2 ab
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «6.1 Unterhaltsbeiträge für den/die Steuerpflichtige(n) 154»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0068.md) `sg-wl-2025__c0068` – «sind beim Empfänger steuerbar und daher unter dieser Ziffer zu»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0084.md) `sg-wl-2025__c0084` – «Unterhaltsbeiträge, die an ein volljähriges Kind bezahlt werden, können einerseits»

<a id="6-2-einkommen-erbschaften-unverteilt"></a>
### Ziff. 6.2 – Ertrag aus unverteilten Erbschaften (Code 158)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Detaillierte Aufstellung der Erbengemeinschaft
- **Rein:** Detaillierte Aufstellung der Erbengemeinschaft → Anteil an den Einkünften · Formular 2 Seite 1 → Beteiligung an unverteilter Erbschaft, Erbanteil (Code 961)
- **Rechnen:** Σ Anteil an Erträgen des Nachlasses (Fälligkeiten Todes- bis Teilungstag) gemäss Aufstellung; Nachlass-Liegenschaften über Formular 7
- **Regel:** Anteilig bei den Berechtigten besteuert; Aufstellung beilegen. Beteiligung zusätzlich im Formular 2 Seite 1 (Code 961) vermerken und Vermögensanteil in Ziff. 30.5.
- **Beachten:** Gilt auch für unverteilte ausserkantonale Vermögensmassen; detaillierte Aufstellung beilegen
- **Beachten:** Vermögensanteil in Ziff. 30.5 (ohne Liegenschaften); Erben ab Todestag deklarationspflichtig
- **Beachten:** Erbschaft ab Fr. 50'000 im Jahr: Vermögenszuwachs wird von Amtes wegen zeitlich gewichtet
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «6.2 Ertrag aus unverteilten Erbschaften 158»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0068.md) `sg-wl-2025__c0068` – «Einkünfte aus unverteilten Erbschaften und andern Vermögensmassen»
  - [Formular 2 SG 2025 S. 1](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0002.md) `sg-form-2-2025__c0002` – «Sind Sie an einer unverteilten Erbschaft beteiligt?»
  - [Formular 2 SG 2025 S. 1](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0002.md) `sg-form-2-2025__c0002` – «sind im Liegenschaftsformular 7 zu deklarieren»
  - [WL SG 2025 S. 41](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0142.md) `sg-wl-2025__c0142` – «Quotale Vermögenserträge aus unverteilten Erbschaften (Fälligkeiten zwischen dem Todes- und dem Teilungstag) sind unter Ziffer 6.2»
  - [WL SG 2025 S. 33](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0111.md) `sg-wl-2025__c0111` – «Die Erben sind ab Todestag für ihren Anteil»
  - [WL SG 2025 S. 11](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0028.md) `sg-wl-2025__c0028` – «wird der Vermögenszuwachs von Amtes wegen zeitlich»

<a id="6-3-einkommen-uebrige"></a>
### Ziff. 6.3 – Übrige Einkünfte (Code 162)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Mitarbeiterbeteiligung (Mitarbeiteraktien, Optionen, Anwartschaften/RSU, Beiblatt zum Lohnausweis) → Aufstellung/Beleg der jeweiligen Einkunftsart
- **Rein:** Abrechnungen Provisionen/Trinkgelder → Betrag, soweit nicht im Lohnausweis · Bescheinigung Arbeitgeber Mitarbeiteraktien/-optionen → Einkünfte aus Mitarbeiterbeteiligung, soweit nicht im Lohnausweis · Lizenz-/Urheberrechtsabrechnung, Verfügung Förderbeitrag (E-Fahrzeug/E-Bike), PV-Stromabrechnung → Vergütung
- **Rechnen:** Σ übrige Einkünfte nach Arten, soweit nicht in Ziff. 1 bis 6.2; PV nur Erlös über dem Eigenverbrauch
- **Regel:** Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Urheberrechte/Lizenzen/Patente, Förderbeiträge (E-Fahrzeuge, E-Bikes), Stromerzeugung (PV) soweit über Eigenverbrauch, IV-Assistenzbeiträge (soweit nicht neutralisiert, StB 46 Nr. 3). Nur soweit nicht in Ziff. 1 bis 6.2 enthalten.
- **Beachten:** IV-Assistenzbeiträge nur, soweit nicht durch abgerechnete Assistenzkosten neutralisiert
- **Beachten:** Mitarbeiteraktien/-optionen: Bescheinigung des Arbeitgebers beilegen
- **Beachten:** Online-Plattform-Einkünfte (z.B. Airbnb, Ricardo, YouTube) auch aus dem Ausland deklarieren
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «6.3 Übrige Einkünfte Arten 162»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0069.md) `sg-wl-2025__c0069` – «Erträge aus Stromerzeugung (Photovoltaikanlagen), soweit diese den Eigenver»
  - [WL SG 2025 S. 36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0123.md) `sg-wl-2025__c0123` – «Bei Mitarbeiteraktien und -optionen muss die vom Arbeitgeber ausgestellte»
  - [WL SG 2025 S. 14](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0038.md) `sg-wl-2025__c0038` – «Plattformeinkünfte, auch aus dem Ausland, müssen in der Steuererklärung»

<a id="6-4-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 6.4 – Kapitalabfindungen für wiederkehrende Leistungen (Code 164, Anzahl Jahre)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Auszahlungsbetrag und Anzahl Jahre gemäss Bescheinigung
- **Rein:** Vereinbarung/Bescheinigung des Leistenden → Auszahlungsbetrag und Anzahl Jahre der abgegoltenen Leistung
- **Rechnen:** Betrag voll in Ziff. 6.4 + Anzahl Jahre; Satzbestimmung wie bei entsprechender jährlicher Leistung (Betrag ÷ Jahre)
- **Regel:** Auszahlungsbetrag und Anzahl Jahre einsetzen; Besteuerung zum Satz einer entsprechenden jährlichen Leistung. Kapitalleistungen aus Vorsorge gehören NICHT hierher, sondern auf Seite 4 (Ziff. 40).
- **Beachten:** Kapitalleistungen aus Vorsorge (2. Säule, Säule 3a) nicht hier → Seite 4, Ziff. 40, separat besteuert
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «6.4 Kapitalabfindungen für wiederkehrende Leistungen für Jahre 164»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0070.md) `sg-wl-2025__c0070` – «Die Kapitalabfindungen für wiederkehrende Leistungen sind mit dem»
  - [WL SG 2025 S. 35](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0119.md) `sg-wl-2025__c0119` – «In Ziffer 40.1 bis 40.3 sind die im Jahr 2025 erhaltenen Kapitalleistungen aus»
  - [WL SG 2025 S. 35](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0119.md) `sg-wl-2025__c0119` – «Kapitalleistungen werden gesondert vom übrigen Einkommen besteuert»

<a id="7-berechnung-total"></a>
### Ziff. 7 – Total der Einkünfte (Code 168)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 1.1 bis 6.4 (Hauptkolonne)
- **Rechnen:** Σ Ziff. 1.1 bis 6.4, dabei Ziff. 4.4 (Abzug Teilbesteuerung) als Minusposten
- **Regel:** Summe Ziff. 1 bis 6 (Ziff. 4.4 als Minusposten). Ziff. 8 (ergänzende Angaben) nicht im Total.
- **Beachten:** Ziff. 8 (vereinfacht abgerechnete Löhne, EL, Hilflosenentschädigung) nicht im Total
- **Beachten:** Kapitalleistungen aus Vorsorge (Ziff. 40) nicht im Total; separate Jahressteuer
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «7. Total der Einkünfte 168»
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0007.md) `sg-form-1-2025__c0007` – «8. Ergänzende Angaben (nicht im Total der Einkünfte zu berücksichtigen)»
  - [WL SG 2025 S. 35](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0119.md) `sg-wl-2025__c0119` – «Kapitalleistungen werden gesondert vom übrigen Einkommen besteuert»

<a id="8-1-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 8.1 – Ergänzende Angaben: vereinfacht abgerechnete Einkünfte, Bruttolohn (Code 290)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bestätigung der Ausgleichskasse über Quellensteuerabzug (sonst Lohnabrechnungen)
- **Rein:** Bestätigung der AHV-Ausgleichskasse über den Quellensteuerabzug → Bruttolohn (fehlt sie: Lohnabrechnungen)
- **Rechnen:** Bruttolohn einsetzen (Information, nicht im Total der Einkünfte); Steuern mit 5% Quellensteuer abgegolten (Bund, Kanton, Gemeinde)
- **Regel:** Nur Information, nicht im Total der Einkünfte. Bruttolohn einsetzen. Mit 5% Abzug sind Bundes-, Kantons- und Gemeindesteuer abgegolten; keine weiteren Steuerfolgen, kein Einfluss auf Steuersatz.
- **Beachten:** Keine weiteren Steuerfolgen und nicht satzbestimmend für das steuerbare Einkommen (Ziff. 24)
- **Beachten:** Nur Löhne, die der Arbeitgeber im vereinfachten Verfahren (BGSA) direkt mit der AHV-Ausgleichskasse abrechnete
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0007.md) `sg-form-1-2025__c0007` – «8.1 Vereinfacht abgerechnete Einkünfte Bescheinigung 290»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0071.md) `sg-wl-2025__c0071` – «In Ziffer 8.1 ist der Bruttolohn einzusetzen»

<a id="8-2-8-3-info-steuerfreie-leistungen"></a>
### Ziff. 8.2-8.3 – Ergänzende Angaben: Ergänzungsleistungen/Überbrückungsleistungen (Code 291), Hilflosenentschädigungen (Code 292)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung der Durchführungsstelle (EL/HE)
- **Rein:** EL-Verfügung/Abrechnung → ausbezahlte Ergänzungs- bzw. Überbrückungsleistungen (Code 291) · Verfügung Hilflosenentschädigung → Jahresbetrag (Code 292)
- **Rechnen:** Information: Σ EL/Überbrückungsleistungen → Code 291; Σ Hilflosenentschädigung → Code 292; steuerfrei, nicht im Total
- **Regel:** Nur Information, steuerfrei. Anzurechnen sind aber EL, die zur Vergütung von Krankheits- und Behinderungskosten ausgerichtet werden; Hilflosenentschädigung wird an die behinderungsbedingten Kosten (Formular 6) angerechnet.
- **Beachten:** EL für Krankheits-/Behinderungskosten und Hilflosenentschädigung an die entsprechenden Kosten (Formular 6) anrechnen
- **Beachten:** HE-Bezüger: statt effektiver Kosten Pauschale leicht/mittel/schwer Fr. 2'500/5'000/7'500 (Ziff. 21.2), Verfügung beilegen
- **Quellen:**
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0007.md) `sg-form-1-2025__c0007` – «8.2 Ergänzungsleistungen / Überbrückungsleistungen für ältere Arbeitslose 291»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0072.md) `sg-wl-2025__c0072` – «Ergänzungsleistungen (inkl. Überbrückungsleistungen für»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0100.md) `sg-wl-2025__c0100` – «Bezüger einer Hilflosenentschädigung leichten Grades: Fr. 2’500»

<a id="lohnausweis-ziff-10-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. Lohnausweis Ziff. 10.2 – Lohnausweis Ziff. 10.2: BVG-Einkaufsbeiträge (bereits vom Lohn abgezogen)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Lohnausweis Ziff. 10.2 (Einkaufsbeiträge)
- **Rein:** Lohnausweis → Ziff. 10.2 Einkaufsbeiträge (vom Lohn abgezogen, im Nettolohn bereits berücksichtigt) · Bescheinigung Vorsorgeeinrichtung (Formular 21 EDP) + Einkaufsberechnung → direkt bezahlte Einkäufe → Ziff. 13.2 (Code 218/219)
- **Rechnen:** Ziff. 13.2 (Code 218 P1 / 219 P2) = Σ nicht über den Lohn bezahlte Einkäufe gem. Bescheinigung; Betrag LA Ziff. 10.2 → kein zusätzlicher Abzug
- **Regel:** Im Nettolohn (Ziff. 1.1/1.2) bereits berücksichtigt: Beiträge an die 2. Säule sind im Regelfall schon über die Deklaration des Nettolohnes berücksichtigt, ein nochmaliger Abzug unter Ziff. 13.2 ist ausgeschlossen. Einkauf über Lohnausweis abgerechnet: nicht doppelt abziehen; nur Einkäufe, die vom Lohn nicht abgezogen wurden (Direktzahlung), in Ziff. 13.2 mit Bescheinigung. Die Praxis zu Ziff. 10.2 stützt sich auf die Lohnausweis-Wegleitung (nur 2026 im Wiki); Fachperson prüft.
- **Beachten:** Über den Lohn abgerechnete BVG-Beiträge/Einkäufe nie nochmals in Ziff. 13.2
- **Beachten:** Bescheinigung der Vorsorgeträgerin samt Einkaufsberechnung immer beilegen
- **Beachten:** Kein Abzug, soweit vorzeitige Kapitalleistungen unversteuert in eine andere Vorsorgeeinrichtung eingebracht wurden
- **Bemerkung:** Spezifische Lohnausweis-Ziffer 10.2 in der SG-WL 2025 nicht erwähnt; Aussage zur Doppelerfassung aus WL SG 2025 Ziff. 13.2. Inhalt durch Prüfung bestätigt (Lohnausweis-Wegleitung Rz 45/47 bzw. 61, nur 2026 im Wiki); SG-Zitat nur indirekt, daher extrahiert. Zweitprüfung: Bedeutung von Lohnausweis Ziff. 10.2 aus WL Lohnausweis 2026 (jahr_ok; WL Lohnausweis 2025 nicht im Wiki, Feldstruktur für 2025 nicht separat bestätigt).
- **Quellen:**
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0086.md) `sg-wl-2025__c0086` – «Deklaration des Nettolohnes»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «In diesem Feld sind die im Bruttolohn enthaltenen, dem Arbeitnehmer vom Lohn abgezoge»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «sind nicht durch den Arbeitgeber im Lohnausweis, sondern durch die Vorsorgeeinrichtung separat mit dem Formular 21 EDP zu bescheinigen»
  - [MB 21 EDP S. 2–3](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0006.md) `bund-mb-21edp__c0006` – «nicht vom Lohn abgezogenen Beiträge nur im Formular 21 angegeben werden dürfen, nicht aber im Lohnausweis»
  - [MB 21 EDP S. 3](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0007.md) `bund-mb-21edp__c0007` – «die dem Arbeitnehmer direkt vom Lohn abgezogen wurden»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0086.md) `sg-wl-2025__c0086` – «zusammen mit der entsprechenden Einkaufsberechnung»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0086.md) `sg-wl-2025__c0086` – «steuerliche Erfassung in eine andere Vorsorgeeinrichtung eingebracht werden»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «Säule 2 (BVG) inkl. Einkaufsbeiträge Person 1 Bescheinigung 218»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «Säule 2 (BVG) inkl. Einkaufsbeiträge Person 2 Bescheinigung 219»

<a id="lohnausweis-ziff-13-3-abzug-weiterbildung"></a>
### Ziff. Lohnausweis Ziff. 13.3 – Lohnausweis Ziff. 13.3: Beiträge des Arbeitgebers an Aus-/Weiterbildung

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Lohnausweis Ziff. 13.3
- **Rein:** Lohnausweis → Ziff. 13.3 AG-Vergütung Weiterbildung (Rechnung auf AN) → nicht steuerbar, nicht abziehbar · Kursrechnungen (Datum, Bezeichnung, Betrag) → selbst bezahlter Anteil → Ziff. 16.4
- **Rechnen:** Code 223/224 = min(Σ Kursrechnungen − AG-Vergütung LA 13.3; 13'000) je Person; Kanton alternativ 400 pauschal (hauptberuflich Unselbständige) / Bund nur effektiv
- **Regel:** Vom Arbeitgeber getragene Kosten der berufsorientierten Aus- und Weiterbildung (inkl. Umschulung) sind nicht steuerbar; entsprechend darf der Arbeitnehmer diese Kosten nicht nochmals in Ziff. 16.4 abziehen (nur selbst bezahlte Kosten).
- **Beachten:** AG-getragene Kosten nicht steuerbar, auch bei Zahlung ans Institut; Rechnung auf AG → nicht im LA
- **Beachten:** Bund: spätere AG-Rückvergütung früher abgezogener Kosten → im Jahr der Rückvergütung steuerbar (LA 13.3)
- **Beachten:** Voraussetzung: Abschluss Sek II oder 20. Lebensjahr vollendet (nicht Erstausbildung bis Sek II)
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung: höchstens Fr. 13'000 pro Person und Jahr (Voraussetzung: erster Abschluss Sek II oder 20. Altersjahr vollendet und nicht Ausbildung bis zum ersten Abschluss Sek II). Ohne Nachweis Pauschale Fr. 400 für unselbständig Erwerbende (nur Kanton/Gemeinde).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Bemerkung:** Lohnausweis-Ziffer 13.3 wird in der WL SG 2025 nicht namentlich genannt; Regel aus WL SG 2025 Ziff. 1 und 16.4. Inhalt durch Prüfung bestätigt (Lohnausweis-Wegleitung Rz 45/47 bzw. 61, nur 2026 im Wiki); SG-Zitat nur indirekt, daher extrahiert. Zweitprüfung: Bedeutung von Lohnausweis Ziff. 13.3 aus WL Lohnausweis 2026 (jahr_ok; WL Lohnausweis 2025 nicht im Wiki, Feldstruktur für 2025 nicht separat bestätigt).
- **Quellen:**
  - [WL SG 2025 S. 14](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0040.md) `sg-wl-2025__c0040` – «Nicht steuerbar sind die vom Arbeitgeber getragenen Kosten der berufsorientierten»
  - [WL SG 2025 S. 14](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0040.md) `sg-wl-2025__c0040` – «Aus- und Weiterbildung, einschliesslich Umschulungskosten.»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0094.md) `sg-wl-2025__c0094` – «Um selbst bezahlte, berufsorientierte Aus-, Weiterbildungs- und»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «In diesem Feld sind alle effektiven Vergütungen des Arbeitgebers für berufsorientierte»
  - [KS 42 S. 9](../../chunks/bund/dauernd/bund-ks-42/bund-ks-42__c0025.md) `bund-ks-42__c0025` – «Dies gilt unabhängig davon, ob die Leistung des Arbeitgebers an den Arbeitnehmer oder an das Bildungsinstitut erfolgt»
  - [KS 42 S. 9](../../chunks/bund/dauernd/bund-ks-42/bund-ks-42__c0025.md) `bund-ks-42__c0025` – «Lautet dabei die Rechnung auf den Arbeitnehmer, bescheinigt der Arbeitgeber diese Vergütung im Lohnausweis in Ziffer 13.3»
  - [KS 42 S. 10–11](../../chunks/bund/dauernd/bund-ks-42/bund-ks-42__c0027.md) `bund-ks-42__c0027` – «im Jahr der Rückvergütung als steuerbares Einkommen»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0095.md) `sg-wl-2025__c0095` – «bende ohne besonderen Nachweis pauschal Fr. 400»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0095.md) `sg-wl-2025__c0095` – «Bei der direkten Bundes- steuer können nur effektive»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «Kosten berufsorientierte Aus-/Weiterbildung Person 1 Aufstellung 223»
  - [KS 42 S. 8–9](../../chunks/bund/dauernd/bund-ks-42/bund-ks-42__c0023.md) `bund-ks-42__c0023` – «Lautet die Rechnung auf den Arbeitgeber, müssen die übernommenen Kosten im Lohnausweis nicht bescheinigt werden»
  - [KS 42 S. 10–11](../../chunks/bund/dauernd/bund-ks-42/bund-ks-42__c0028.md) `bund-ks-42__c0028` – «Der Arbeitgeber hat die Rückvergütungen im Lohnausweis in Ziffer 13.3»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0095.md) `sg-wl-2025__c0095` – «lich unselbständig Erwer- bende ohne besonderen»

## Abzüge

<a id="10-1-berechnung-total"></a>
### Ziff. 10.1 – Berufskosten bei unselbständiger Erwerbstätigkeit Person 1 (Code 438)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 4 Person 1 Ziff. 6 «Total der Berufskosten» (Code 438)
- **Rein:** Formular 4 Person 1 → Ziff. 6 Total der Berufskosten (Code 438) · Lohnausweis → Nettolohn (Basis Pauschale), Feld F (Gratistransport), Feld G (Kantine/Verbilligung) · ÖV-Abo-Belege, Fahrtstrecke (km), Arbeitstage; Arbeitgeberbescheinigung Schichttage (Lohnausweis Ziff. 15) · Zimmermiete und Arbeitstage bei auswärtigem Wochenaufenthalt
- **Rechnen:** min(ÖV + Velo ≤ 700 + km × 0.70; 8'000) + Verpflegung 15/Tag max. 3'200 + min(700 + 10% Nettolohn; 2'400) + Wochenaufenthalt + Nebenerwerb
- **Regel:** Übertrag des Totals aus Formular 4 (Vorderseite). Abzüge stehen jedem Partner individuell zu, soweit unselbständig erwerbstätig. Kein Abzug für vom Arbeitgeber übernommene Kosten. Ausgangsbasis ist der Nettolohn Ziff. 1.1.
- **Beachten:** Bund: Fahrkosten max. Fr. 3'300; Pauschale 3% des Nettolohns, min. Fr. 2'000, max. Fr. 4'000
- **Beachten:** Homeoffice-/arbeitsfreie Tage: keine Fahr- und Verpflegungskosten; Kanton i.d.R. max. 220 Arbeitstage
- **Beachten:** Geschäftsauto mit Privatanteil 0,9%/Monat oder Lohnausweis Feld F angekreuzt: kein Fahrkostenabzug
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 pro Person (Maximalabzug, keine Pauschale; bei Teilzeit/unterjährig nicht gekürzt; gilt bei Haupt- und Nebenerwerb insgesamt). Bei direkter Bundessteuer tiefer (Fr. 3'300, siehe data/werte/bund).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Pauschale übrige Berufskosten höchstens Fr. 2'400.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.70 (Privatfahrzeug (Auto) nur in begründeten Fällen (kein zumutbarer öV): Fr. 0.70 pro Fahrkilometer im Steuerjahr 2025.)** · Bund **CHF 0.70 (Privatauto: Abzug pro Fahrkilometer CHF 0.70, nur wenn kein öffentliches Verkehrsmittel verfügbar/zumutbar (Steuerjahr 2025))**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Fahrrad, Motorfahrrad oder Kleinmotorrad bis 50 ccm (gelbes Kontrollschild): Pauschale bis Fr. 700 im Jahr (Voraussetzung: mehr als 10 Minuten zu Fuss zur nächsten ÖV-Haltestelle).)** · Bund **CHF 700 (Pauschale pro Jahr für Fahrrad, Motorfahrrad und Motorrad mit gelbem Kontrollschild; tatsächliche Kosten zusätzlich nicht abziehbar)**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswärtige Verpflegung: Fr. 15 pro auswärtige Hauptmahlzeit (Mittagessen), wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann.)** · Bund **CHF 15 (Mehrkosten auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (i.d.R. Mittagessen); ausschliesslich Pauschale, wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei regelmässiger auswärtiger Verpflegung (Mittagessen) Fr. 3'200 im Jahr.)** · Bund **CHF 3'200 (Bei ständiger auswärtiger Verpflegung CHF 3'200 pro Jahr (voller Abzug))**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockelbetrag der Pauschale übrige Berufskosten: Fr. 700 (+ 10 % des Nettolohnes).)** · Bund **n/a – Bund: 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; kein 'fix + %'-Modell.**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Pauschale übrige Berufskosten: Fr. 700 zuzüglich 10 % der Nettoeinkünfte (Nettolohn), höchstens Fr. 2'400; Nachweis höherer Kosten vorbehalten. Nettoeinkünfte = Bruttoeinkünfte abzüglich Beiträge AHV/IV/EO/ALV/UV und BVG (ohne Einkäufe).)** · Bund **3 % (Übrige Berufskosten (Art. 26 Abs. 1 lit. c DBG): Pauschale 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; anstelle der Pauschale ist der Nachweis höherer tatsächlicher übriger Berufskosten möglich. Fahrkosten (lit. a, max. 3'300 gemäss DBG 2025; WL 2a 2025 nennt 3'200 – Widerspruch siehe berufskosten.fahrkosten.max) und Verpflegung (lit. b) werden zusätzlich abgezogen. Bei Teilzeit/Teiljahr angemessen kürzen.)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **n/a – Formel in Art. 21 StV SG nennt nur Fix-Betrag, Satz und Maximum.** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **220 Tage (In der Regel höchstens 220 Arbeitstage pro Jahr (Vollzeit); höhere Anzahl nachzuweisen. Für Homeoffice-Tage und Tage ohne Arbeitsleistung keine Fahrkosten (ausser ÖV-Abo).)** · Bund **n/a – Bund kennt keine Festlegung massgebender Arbeitstage; abziehbar sind die tatsächlichen notwendigen Kosten bis zum Maximalbetrag (Art. 26 Abs. 1 lit. a DBG).**
- **Bund:** Bund: abweichende Limiten (Fahrkosten max. Fr. 3'300; Pauschale übrige Kosten 3% des Nettolohnes, min. Fr. 2'000, max. Fr. 4'000) – die Veranlagungsbehörde passt automatisch an.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «10.1 Person 1 Formular 4 438»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0074.md) `sg-wl-2025__c0074` – «stehen jedem Partner individuell zu, soweit er unselbständig erwerbstätig ist»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0002.md) `sg-form-32-2025__c0002` – «Fahrkosten zwischen Wohn- und Arbeitsort max. Fr. 8‘000 max. Fr. 3‘300»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0002.md) `sg-form-4-2025__c0002` – «km x Fr. 0.70 (Kostensatz gemäss Wegleitung)»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «Pro Arbeitstag Fr. 15 / im Jahr Fr. 3'200»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «3.1 Pauschalabzug: Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2'400»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0004.md) `sg-form-4-2025__c0004` – «6. Total der Berufskosten 438»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0075.md) `sg-wl-2025__c0075` – «wird), muss auf dem Lohnausweis Feld F angekreuzt sein»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0076.md) `sg-wl-2025__c0076` – «Monat 0,9% des Fahrzeugkaufpreises (exkl. Mehrwertsteuer)»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0077.md) `sg-wl-2025__c0077` – «1.3 Bei Benützung eines Motorfahrzeuges in begründeten Fällen: 70 Rappen je»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0077.md) `sg-wl-2025__c0077` – «bis zu Fr. 700 im Jahr»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0077.md) `sg-wl-2025__c0077` – «mit höchstens 220 Arbeits»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0078.md) `sg-wl-2025__c0078` – «In diesem Fall ist auf dem Lohnausweis Feld G»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0079.md) `sg-wl-2025__c0079` – «geber unter Bemerkungen (Ziffer 15 im Lohnausweis) oder in einem separaten»

<a id="10-2-berechnung-total"></a>
### Ziff. 10.2 – Berufskosten bei unselbständiger Erwerbstätigkeit Person 2 (Code 488)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 4 Person 2 Ziff. 6 «Total der Berufskosten» (Code 488)
- **Rein:** Formular 4 Person 2 (Rückseite) → Ziff. 6 Total der Berufskosten (Code 488) · Lohnausweis Person 2 → Nettolohn als Basis; Feld F/G · Belege Fahrkosten, Verpflegung, Wochenaufenthalt und Nebenerwerb von Person 2
- **Rechnen:** wie Ziff. 10.1 für Person 2: min(ÖV + Velo ≤ 700 + km × 0.70; 8'000) + Verpflegung + min(700 + 10% Nettolohn; 2'400) + Wochenaufenthalt + Nebenerwerb
- **Regel:** Wie Ziff. 10.1, für Person 2 (Formular 4 Rückseite).
- **Beachten:** Bund: Fahrkosten max. Fr. 3'300; Pauschale 3% des Nettolohns, min. Fr. 2'000, max. Fr. 4'000
- **Beachten:** Nebenerwerb Form. 4 Ziff. 5.1: 20% der Nettoeinkünfte, min. Fr. 800, max. Fr. 2'400
- **Beachten:** Jahrespauschalen Ziff. 3 und 5 bei unterjähriger Steuerpflicht nach Dauer umrechnen
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 pro Person (Maximalabzug, keine Pauschale; bei Teilzeit/unterjährig nicht gekürzt; gilt bei Haupt- und Nebenerwerb insgesamt). Bei direkter Bundessteuer tiefer (Fr. 3'300, siehe data/werte/bund).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.70 (Privatfahrzeug (Auto) nur in begründeten Fällen (kein zumutbarer öV): Fr. 0.70 pro Fahrkilometer im Steuerjahr 2025.)** · Bund **CHF 0.70 (Privatauto: Abzug pro Fahrkilometer CHF 0.70, nur wenn kein öffentliches Verkehrsmittel verfügbar/zumutbar (Steuerjahr 2025))**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Fahrrad, Motorfahrrad oder Kleinmotorrad bis 50 ccm (gelbes Kontrollschild): Pauschale bis Fr. 700 im Jahr (Voraussetzung: mehr als 10 Minuten zu Fuss zur nächsten ÖV-Haltestelle).)** · Bund **CHF 700 (Pauschale pro Jahr für Fahrrad, Motorfahrrad und Motorrad mit gelbem Kontrollschild; tatsächliche Kosten zusätzlich nicht abziehbar)**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockelbetrag der Pauschale übrige Berufskosten: Fr. 700 (+ 10 % des Nettolohnes).)** · Bund **n/a – Bund: 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; kein 'fix + %'-Modell.**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Pauschale übrige Berufskosten: Fr. 700 zuzüglich 10 % der Nettoeinkünfte (Nettolohn), höchstens Fr. 2'400; Nachweis höherer Kosten vorbehalten. Nettoeinkünfte = Bruttoeinkünfte abzüglich Beiträge AHV/IV/EO/ALV/UV und BVG (ohne Einkäufe).)** · Bund **3 % (Übrige Berufskosten (Art. 26 Abs. 1 lit. c DBG): Pauschale 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; anstelle der Pauschale ist der Nachweis höherer tatsächlicher übriger Berufskosten möglich. Fahrkosten (lit. a, max. 3'300 gemäss DBG 2025; WL 2a 2025 nennt 3'200 – Widerspruch siehe berufskosten.fahrkosten.max) und Verpflegung (lit. b) werden zusätzlich abgezogen. Bei Teilzeit/Teiljahr angemessen kürzen.)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Pauschale übrige Berufskosten höchstens Fr. 2'400.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **n/a – Formel in Art. 21 StV SG nennt nur Fix-Betrag, Satz und Maximum.** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Unselbständiger Nebenerwerb: Pauschale 20 % der Nettoeinkünfte aus der Nebentätigkeit, mindestens Fr. 800, höchstens Fr. 2'400 pro Jahr. Bei Nettolohn bis Fr. 800: Auslagen bis zur Höhe des Nettolohns. Kein Anspruch ohne Haupterwerb bei Dritten; in der Regel nicht für VR-Honorare.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge))**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb-Pauschale mindestens Fr. 800 (Nettoeinkünfte bis Fr. 800: Abzug bis zur Höhe des Nettolohns).)** · Bund **CHF 800 (Minimum Pauschale Nebenerwerb)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb-Pauschale höchstens Fr. 2'400 im Jahr.)** · Bund **CHF 2'400 (Maximum Pauschale Nebenerwerb)**
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «10.2 Person 2 Formular 4 488»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0008.md) `sg-form-4-2025__c0008` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 10.2»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0006.md) `sg-form-4-2025__c0006` – «km x Fr. 0.70 (Kostensatz gemäss Wegleitung)»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0006.md) `sg-form-4-2025__c0006` – «Zwischentotal Ziffern 1.1 – 1.3, max. Fr. 8'000»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0007.md) `sg-form-4-2025__c0007` – «3.1 Pauschalabzug: Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2'400»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0005.md) `sg-form-4-2025__c0005` – «Ziffer 3 und 5 sind nach Dauer der Steuerpflicht»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0002.md) `sg-form-32-2025__c0002` – «Fahrkosten zwischen Wohn- und Arbeitsort max. Fr. 8‘000 max. Fr. 3‘300»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0077.md) `sg-wl-2025__c0077` – «bis zu Fr. 700 im Jahr»

<a id="11-abzug-schuldzinsen"></a>
### Ziff. 11 – Schuldzinsen (Code 500)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 5 Teil A «Total private Schulden und private Schuldzinsen» (Schuldzinsen 2025)
- **Rein:** Hypothekar-/Zinsbescheinigung Bank → Schuldzinsen 2025 (Form. 5 Teil A; Schuldbetrag → Ziff. 34.1) · Kredit-/Darlehensvertrag, Zinsbescheinigung → private Schuldzinsen 2025 · Kontoauszug/Zinsausweis → belastete Sollzinsen privater Konten · Übertrag Ziff. 4 (Wertschriftenertrag) + Ziff. 5 (Liegenschaftsertrag) → Limite
- **Rechnen:** min(Σ private Schuldzinsen 2025; Ertrag Ziff. 4 ohne Lotterie-/Totogewinne + Ertrag Ziff. 5 + Fr. 50'000); Bund analog (Vermögensertrag + Fr. 50'000)
- **Regel:** Nur private Schuldzinsen; abziehbar im Umfang der Einkünfte aus Wertschriften/Guthaben (Ziff. 4, ohne Lotteriegewinne) und Liegenschaften (Ziff. 5) zuzüglich Fr. 50'000. Nicht abzugsfähig: Amortisationen, Baukreditzinsen (Anlagekosten), Baurechtszinsen selbstgenutzter Eigenheime, Leasinggebühren. Geschäftliche Schuldzinsen sind in der Jahresrechnung enthalten (nicht in Formular 5). Hypothekarzinsen der Liegenschaft hier, nicht im Formular 7.
- **Beachten:** Nicht abziehbar: Amortisationen, Baukreditzinsen (Anlagekosten), Baurechtszinsen eigenes Eigenheim, Leasinggebühren
- **Beachten:** Geschäftliche Schuldzinsen sind in der Jahresrechnung, nicht in Form. 5
- **Beachten:** Bund: im Jahr 2025 fällig gewordene Zinsen; teilbesteuerte Beteiligungserträge nur zu 70% in die Limite
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «11. Schuldzinsen Formular 5 500»
  - [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0083.md) `sg-wl-2025__c0083` – «Private Schuldzinsen sind nur im Umfang der Einkünfte aus Wertschriften und»
  - [Formular 5 SG 2025 S. 1](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0001.md) `sg-form-5-2025__c0001` – «Total private Schulden und private Schuldzinsen»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0048.md) `bund-wl-2a-2025__c0048` – «Die im Jahr 2025 fällig gewordenen Schuldzinsen sind wie folgt»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0048.md) `bund-wl-2a-2025__c0048` – «50 000 Fr.; Einkünfte aus Beteiligungen des Privatvermö-»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0049.md) `bund-wl-2a-2025__c0049` – «werden nur zu 70 % in die Berechnung einbezogen.»

<a id="12-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.1 – Unterhaltsbeiträge an Geschiedene oder Getrennte (Code 200)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungsurteil/Trennungsvereinbarung (bei erstmaliger Zahlung), Zahlungsnachweise
- **Rein:** Scheidungsurteil/Trennungsvereinbarung → vereinbarter Unterhaltsbeitrag (bei erstmaliger Zahlung Auszug beilegen) · Zahlungsnachweise (Bank) → 2025 bezahlte Beiträge (Aufstellung)
- **Rechnen:** Σ 2025 bezahlte periodische Unterhaltsbeiträge an geschiedenen bzw. gerichtlich/tatsächlich getrennt lebenden Partner (Kanton = Bund)
- **Regel:** Nur Beiträge an geschiedenen/getrennt lebenden Partner. Bei erstmaliger Zahlung Auszug aus Urteil bzw. Vereinbarung beilegen. Hinweis: Können Unterhaltsbeiträge (für Kinder, Ziff. 12.2) abgezogen werden, entfallen die Kinderabzüge Ziff. 23.1-23.3 für dieses Kind.
- **Beachten:** Gegenstück: beim Empfänger steuerbar (dort Ziff. 6.1)
- **Beachten:** Nicht abziehbar: Leistungen aus anderen familienrechtlichen Unterhalts-/Unterstützungspflichten
- **Beachten:** Nur periodische/laufende Beiträge: Kapitalabfindung gilt als Schuldentilgung, nicht abziehbar (WL 2a 2025); SG: StV Art. 15 – als Unterhaltsbeiträge gelten ausschliesslich die laufenden Beiträge (Empfängerseite)
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «12.1 Unterhaltsbeiträge an Geschiedene oder Getrennte Aufstellung 200»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0084.md) `sg-wl-2025__c0084` – «Unterhaltsbeiträge an den geschiedenen, gerichtlich oder tatsächlich getrennt»
  - [WL SG 2025 S. 21](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0068.md) `sg-wl-2025__c0068` – «sind beim Empfänger steuerbar und daher unter dieser Ziffer zu»
  - [StG SG Art. 45](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t1.md) `sg-stg-2025__art-45-t1` – «nicht jedoch Leistungen in Erfüllung anderer familienrechtlicher Unterhalts- oder Unterstützungspflichten»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0050.md) `bund-wl-2a-2025__c0050` – «Abziehbar sind die Alimentenleistungen an den geschiedenen»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0051.md) `bund-wl-2a-2025__c0051` – «Unterhaltsbeiträge, die in Form einer Kapitalabfindung erbracht»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0051.md) `bund-wl-2a-2025__c0051` – «gelten als Schuldentilgung und sind daher nicht»
  - [StV SG Art. 15](../../chunks/sg/2025/sg-stv/sg-stv__art-15.md) `sg-stv__art-15` – «gelten ausschliesslich die laufenden Beiträge»

<a id="12-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.2 – Unterhaltsbeiträge für minderjährige Kinder (Code 202)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise je Kind, Urteil/Vereinbarung
- **Rein:** Urteil/Vereinbarung → Unterhaltsbeitrag je Kind (bei erstmaliger Zahlung Auszug + Zahlungsnachweis beilegen) · Zahlungsnachweise → 2025 bezahlte Beiträge, separat je Kind
- **Rechnen:** Σ je Kind 2025 bezahlte Unterhaltsbeiträge an den Elternteil mit elterlicher Sorge/Obhut (nur minderjährige Kinder)
- **Regel:** Beiträge an den Elternteil mit elterlicher Sorge/Obhut, separat je Kind ausweisen. Für dieses Kind kein Kinderabzug (Kind auf Seite 1 nicht aufführen). An volljährige Kinder bezahlte Beiträge nicht abziehbar.
- **Beachten:** Für dieses Kind kein Kinderabzug 23.1–23.3; Kind nicht auf Seite 1 aufführen
- **Beachten:** An volljährige Kinder: nicht abziehbar (beim Kind unbesteuert); Bund: nur via Sozialabzug Ziff. 23.2 der Bundes-WL
- **Beachten:** Bund: Naturalleistungen (Miete, KK-Prämien, Schuldzinsen) anstelle Barzahlung = Alimente
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «12.2 Unterhaltsbeiträge für minderjährige Kinder Aufstellung 202»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0084.md) `sg-wl-2025__c0084` – «Die Unterhaltsbeiträge an einen Elternteil für die unter dessen elterlicher Sorge»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0104.md) `sg-wl-2025__c0104` – «auf Seite 1 der Steuererklä-»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0050.md) `bund-wl-2a-2025__c0050` – «steuerbaren Leistungen nur im Rahmen von Ziffer 23.2 der»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0051.md) `bund-wl-2a-2025__c0051` – «Den Alimenten gleichgesetzt sind Naturalleistungen wie Miete,»

<a id="12-3-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.3 – Rentenleistungen (Code 204)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Vertrag/Nachweis dauernde Last bzw. Rentenbescheinigung
- **Rein:** Leibrenten-/Verpfründungsvertrag + Zahlungsnachweis → 2025 bezahlte Rente/Verpfründung (Aufstellung, Empfänger angeben) · Vertrag/Nachweis dauernde Last → 2025 erbrachte Leistung · ESTV-Publikation → Ertragsanteil-Satz
- **Rechnen:** nachgewiesene dauernde Lasten + bezahlte Leibrente/Verpfründung × Ertragsanteil (%) nach Art. 35 Abs. 3 lit. c StG (Bund: × ESTV-Berechnungssatz)
- **Regel:** Nachgewiesene dauernde Lasten sowie Ertragsanteil der Leistungen aus Leibrenten und Verpfründungsverträgen (Art. 35 Abs. 3 lit. c StG).
- **Beachten:** Ertragsanteil flexibel (Rendite zehnjähriger Bundesobligationen), von der ESTV berechnet und publiziert
- **Beachten:** Bund: nur aus gesetzl./vertragl./letztwilliger Pflicht (z.B. Haftpflichtrenten), kein familienrechtl. Unterhalt
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «12.3 Rentenleistungen Aufstellung 204»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0084.md) `sg-wl-2025__c0084` – «Die nachgewiesenen dauernden Lasten sowie der Ertragsanteil»
  - [WL SG 2025 S. 18](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0059.md) `sg-wl-2025__c0059` – «Er wird von der ESTV berechnet und publiziert.»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0052.md) `bund-wl-2a-2025__c0052` – «Bezahlte Leibrente / Verpfründung x Berechnungssatz (in %)»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0053.md) `bund-wl-2a-2025__c0053` – «gründeten Verpflichtungen beruhen und nicht der Erfüllung einer familienrechtlichen Unterhaltspflicht dienen»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0053.md) `bund-wl-2a-2025__c0053` – «Empfänger/in der Leistung ist anzugeben.»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0053.md) `bund-wl-2a-2025__c0053` – «leistungen sind z.B. die gesetzlichen Haftpflichtrenten und die»

<a id="13-1-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.1 – Vorsorgebeiträge Säule 3a (Code 208 Person 1 / 210 Person 2)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → 3a-Bescheinigung (Form. 21 EDP): im Jahr 2025 bezahlter Betrag
- **Rein:** 3a-Bescheinigung Bankstiftung/Versicherung (Form. 21 EDP) → 2025 einbezahlter Beitrag je Person · Lohnausweis/Erfolgsrechnung → Erwerbseinkommen (nur ohne 2. Säule, für 20%-Limite)
- **Rechnen:** je Person: mit 2. Säule min(Einzahlung 2025; Fr. 7'258); ohne 2. Säule min(Einzahlung; 20% × Erwerbseinkommen; Fr. 36'288) – Kanton = Bund
- **Regel:** Nur 2025 tatsächlich bezahlte Beiträge; Bescheinigung immer beilegen. Max. Fr. 7'258 (mit 2. Säule) bzw. 20% des Erwerbseinkommens, max. Fr. 36'288 (ohne 2. Säule). Beide erwerbstätigen Partner je eigener Abzug. Selbständige: nicht der Erfolgsrechnung belasten. Wer 3a abzieht, verliert den Zuschlag beim Versicherungsabzug (Ziff. 14).
- **Beachten:** Nur 2025 tatsächlich einbezahlte Beiträge; Bescheinigung immer beilegen
- **Beachten:** Selbständige: Beiträge sind Privataufwand, nicht der Erfolgsrechnung belasten
- **Beachten:** Abzug 3a oder 2. Säule → kein Zuschlag «ohne Vorsorge» in Ziff. 14
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a: Erwerbstätige mit 2. Säule maximal Fr. 7'258 (beide Partner je für sich abziehbar). Nur im Jahr 2025 tatsächlich bezahlte Beiträge; Bescheinigung beilegen.)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug mit Zugehörigkeit zur 2. Säule (8 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a: Erwerbstätige ohne 2. Säule höchstens 20 % des Erwerbseinkommens, maximal Fr. 36'288.)** · Bund **CHF 36'288 (Säule 3a: Höchstabzug ohne 2. Säule (max. 36'288, 40 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. Fr. 36'288).)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. CHF 36'288))**
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «13.1 Säule 3a Person 1 Bescheinigung 208»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0085.md) `sg-wl-2025__c0085` – «maximal Fr. 7’258»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0085.md) `sg-wl-2025__c0085` – «maximal Fr. 36’288»
  - [Formular 6 SG 2025 S. 1](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0002.md) `sg-form-6-2025__c0002` – «zusätzlich, wenn keine Beiträge für die berufliche Vorsorge»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0048.md) `bund-wl-2a-2025__c0048` – «gehört: Höchstabzug von 7258 Fr. im Jahr;»

<a id="13-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 13.2 – Säule 2 (BVG) inkl. Einkaufsbeiträge (Code 218 Person 1 / 219 Person 2)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Bescheinigung Vorsorgeeinrichtung + Einkaufsberechnung (Lohnausweis Ziff. 10.2 = bereits abgezogen)
- **Rein:** Bescheinigung Vorsorgeeinrichtung (Form. 21 EDP) → selbst überwiesene Beiträge/Einkäufe 2025 · Einkaufsberechnung der Pensionskasse → beilegen · Lohnausweis → vom Lohn abgezogene BVG-Beiträge/Einkäufe: bereits im Nettolohn Ziff. 1.1/1.2
- **Rechnen:** Σ 2025 nicht vom Lohn abgezogene BVG-Beiträge + Einkäufe gemäss Bescheinigung; Selbständige: 100% der Einkaufsbeiträge hier (nicht Erfolgsrechnung)
- **Regel:** Beiträge im Lohnausweis (Ziff. 10.1 ordentliche BVG-Beiträge) sind im Nettolohn schon berücksichtigt: nicht nochmals abziehen. Hier nur Einkäufe/Beiträge ausserhalb des Lohnausweises, bei Selbständigen 100% der Einkaufsbeiträge. Lohnausweis Ziff. 10.2 (Einkauf, vom Lohn abgezogen): im Nettolohn (Ziff. 11 = Ziff. 8 abzüglich Ziff. 9 und 10) bereits abgezogen, daher hier nicht nochmals (Lohnausweis-Wegleitung Rz 45/47, im Wiki nur 2026). Bescheinigung der Vorsorgeträgerin immer beilegen. Kein Abzug bei Einkauf mit vorzeitig bezogenen, steuerlich nicht erfassten Kapitalleistungen.
- **Beachten:** Vom Lohn abgezogene Beiträge/Einkäufe stehen im Lohnausweis, nicht in Form. 21 → kein Doppelabzug
- **Beachten:** Kein Abzug für Einkauf mit vorzeitig bezogenen, steuerlich nicht erfassten Kapitalleistungen
- **Beachten:** Bescheinigung der Vorsorgeträgerin + Einkaufsberechnung immer beilegen
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «13.2 Säule 2 (BVG) inkl. Einkaufsbeiträge Person 1 Bescheinigung 218»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0086.md) `sg-wl-2025__c0086` – «Deklaration des Nettolohnes»
  - [WL SG 2025 S. 26](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0086.md) `sg-wl-2025__c0086` – «Die Berücksichtigung in der Erfolgsrechnung ist nicht zulässig»
  - [MB 21 EDP S. 2–3](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0006.md) `bund-mb-21edp__c0006` – «alle vom Arbeitnehmer aus eigenen Mitteln aufgebrachten, aber ihm nicht vom Lohn abgezogenen Beiträge nur im Formular 21 angegeben werden dürfen»
  - [MB 21 EDP S. 3](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0007.md) `bund-mb-21edp__c0007` – «die dem Arbeitnehmer direkt vom Lohn abgezogen wurden.»

<a id="14-abzug-versicherungspraemien"></a>
### Ziff. 14 – Versicherungsprämien und Sparzinsen (Code 600)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 6 Teil C «Abzug» (niedrigerer Betrag von A und B)
- **Rein:** KK-Prämienbescheinigung → Prämien brutto (Form. 6 A.a) · Prämienbelege Unfall-/Lebens-/Rentenversicherung → A.b (ohne NBU) / A.c · Formular 2 (Wertschriftenverzeichnis) → Sparzinsen (A.d) · Verfügung Prämienverbilligung → A.e abziehen
- **Rechnen:** min(A; B); A = Prämien + Sparzinsen − Verbilligung; B: Kanton 6'800/3'400 (+1'100/+500 ohne 2./3a), +1'100 je Kind; Bund 3'700/1'800 (+1'850/+900), +700 je Kind
- **Regel:** Effektive Prämien (Kranken brutto, Unfall ohne NBU, Lebens-/Rentenvers.) + Sparzinsen, abzüglich Prämienverbilligungen (A) gegen Maximalbetrag (B): gemeinsam Fr. 6'800 / alleinstehend Fr. 3'400, + je Fr. 1'100 pro Kind mit Kinderabzug, + Fr. 1'100 / Fr. 500 wenn weder BVG- noch Säule-3a-Beiträge abgezogen (bei Verheirateten bei beiden Partnern). Niedrigerer Betrag von A und B. Nicht abziehbar: Mobiliar-, Motorfahrzeug-, Haftpflicht- und Sachversicherungen.
- **Beachten:** Nicht abziehbar: Mobiliar-, Motorfahrzeug-, Haftpflicht- und andere Sachversicherungen
- **Beachten:** Zuschlag ohne Vorsorge nur, wenn weder 2. Säule noch 3a abgezogen (Verheiratete: bei beiden)
- **Beachten:** Kinderzuschlag nur für Kinder mit Abzug Ziff. 23.1/23.2; Bund auch je unterstützte Person
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
  - [Formular 6 SG 2025 S. 1](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0001.md) `sg-form-6-2025__c0001` – «Private Unfallversicherung (ohne Nichtberufsunfallversicherung)»
  - [Formular 6 SG 2025 S. 1](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0001.md) `sg-form-6-2025__c0001` – «Sparzinsen (gemäss Wertschriften- und Guthabenverzeichnis)»
  - [WL SG 2025 S. 27](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0087.md) `sg-wl-2025__c0087` – «Dabei sind die individuellen Prämienverbilligungen, die für»

<a id="15-abzug-liegenschaft-unterhalt"></a>
### Ziff. 15 – Unterhalts- und Verwaltungskosten für Liegenschaften (Code 716)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Formular 7 Abschnitt C (Pauschale 20% der Erträge B oder tatsächliche Kosten C2) bzw. Formular 7Z Spalten C1/C2
- **Rein:** Formular 7 Teil B → Total Erträge a. + b. (anrechenbarer Eigenmietwert + Mieterträge abzüglich Nebenkosten) = Basis Pauschale · Handwerker-/Unterhaltsrechnungen (Rechnungsdatum 2025, selbst bezahlt) → Form. 7 Rückseite, Anteil Unterhalt/Verwaltung (C2) · Gebäudeversicherung, Grundsteuer, STWEG-Abrechnung (inkl. Erneuerungsfonds), Liegenschaftenrechnung → C2 · Mehrere Liegenschaften → Form. 7Z Spalten C1/C2
- **Rechnen:** je Liegenschaft: Pauschale 20% × Erträge (B) ODER C2 = Σ selbst bezahlte Kosten − Versicherungs-/Förderleistungen; Bund: Pauschale 10% (Gebäude ≤ 10 J.) / 20% (> 10 J.)
- **Regel:** Pauschale 20% der Erträge (B) nur für private Liegenschaften, die ganz oder vorwiegend Wohnzwecken dienen, ODER tatsächliche Kosten (Rechnungsdatum 2025, selbst bezahlt, abzüglich Versicherungsleistungen/Förderbeiträge). Wahl pro Liegenschaft. Pauschale umfasst auch Denkmalpflege und Energiespar-/Umweltinvestitionen. Wertvermehrende Aufwendungen nicht abziehbar. Geschäftsliegenschaften in Ziff. 2.
- **Beachten:** Pauschale nur für ganz/vorwiegend Wohnzwecken dienende Privatliegenschaften; Wahl je Steuerperiode und Liegenschaft
- **Beachten:** Nicht abziehbar: Wertvermehrung; bei Eigengebrauch Wasser, Gas, Strom, Heizung/Warmwasser, Abwasser, Kehricht
- **Beachten:** Geschäftsliegenschaften: Kosten bei selbständiger Tätigkeit (Ziff. 2)
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt/Verwaltung: 20 % des Bruttomietertrags ohne Nebenkosten bzw. des angerechneten Eigenmietwerts, nur für vorwiegend Wohnzwecken dienende Privatliegenschaften; Wahl pro Periode und Liegenschaft zwischen Pauschale und effektiven Kosten.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Gleicher Pauschalsatz 20 % unabhängig vom Gebäudealter (SG kennt keine Staffelung nach 10 Jahren).)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «15. Unterhalts- und Verwaltungskosten für Liegenschaften Formular 7 716»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0161.md) `sg-wl-2025__c0161` – «20% des steuerlich massgebenden Mietertrages oder des steuer-»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0004.md) `sg-form-7-2025__c0004` – «Pauschalabzug 20% der Erträge (B)»
  - [StV SG Art. 29](../../chunks/sg/2025/sg-stv/sg-stv__art-29.md) `sg-stv__art-29` – «zwischen dem Abzug der tatsächlichen Kosten und dem Pauschalabzug wählen»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags»
  - [WL SG 2025 S. 46](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0164.md) `sg-wl-2025__c0164` – «Nicht abziehbar sind die Kosten (inklusive Grundgebühren) für Wasser, Gas,»
  - [WL SG 2025 S. 46](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0164.md) `sg-wl-2025__c0164` – «Nicht abzugsberechtigt sind Ausgaben, die eine Wertvermehrung der Liegenschaft»
  - [WL SG 2025 S. 47](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0169.md) `sg-wl-2025__c0169` – «auch die Einlagen in den Reparatur- und Erneuerungsfonds»
  - [WL SG 2025 S. 47](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0169.md) `sg-wl-2025__c0169` – «Wird für die Liegenschaft eine separate Liegenschaftenrechnung geführt, so kann»
  - [WL SG 2025 S. 27](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0089.md) `sg-wl-2025__c0089` – «sind bei der Ermittlung der Einkünfte aus selbständiger Tätigkeit (Ziffer 2) zu berücksichtigen»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0003.md) `sg-form-7-2025__c0003` – «Total anrechenbarer Eigenmietwert»
  - [Formular 7 SG 2025 S. 2](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0005.md) `sg-form-7-2025__c0005` – «Abzugsfähig sind nur die selbst bezahlten Kosten.»
  - [Formular 7 SG 2025 S. 2](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0005.md) `sg-form-7-2025__c0005` – «Übertrag in die Spalte (C2) des Formulars 7Z»

<a id="16-1-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. 16.1 – Verwaltungskosten für Wertschriften und sonstige Kapitalanlagen (Code 220)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Steuerauszug/Depotgebührenausweis; Kurswert fremdverwaltetes Vermögen
- **Rein:** Steuerauszug/Depotauszug Bank → Depot-/Safegebühren, Inkassospesen 2025 · Depotauszug → Wert fremdverwaltete Wertschriften (Basis Pauschale) · Gewinnbestätigung/Formular 2 → steuerbare Lotterie-/Geldspielgewinne (Einsatzkosten)
- **Rechnen:** tatsächliche Kosten ODER min(2‰ × fremdverwaltete Wertschriften; Fr. 6'000); Einsatzkosten je Gewinn 5% (max. Fr. 5'400), online max. Kanton 26'700 / Bund 26'800
- **Regel:** Tatsächliche Kosten (Depot-/Safegebühren, Inkassospesen) oder Pauschale 2 Promille des fremdverwalteten Wertschriftenvermögens, höchstens Fr. 6'000. Nicht abzugsfähig: Courtagen, Emissionsabgabe, Anlage-/Steuerberatung, Vermögensverwaltungsmandate. Darlehen und selbstverwaltete Wertschriften (eigene AG) gelten nicht als fremdverwaltet. Einsatzkosten Geldspiele: 5% des Gewinns, max. Fr. 5'400; Online-Spiele abgebuchte Einsätze, max. Fr. 26'700.
- **Beachten:** Wertschriften im Depot einer Bank gelten als durch Dritte verwahrt/verwaltet – ein Vermögensverwaltungsmandat ist nicht Voraussetzung der Pauschale
- **Beachten:** Nicht abziehbar: Courtagen, Ausgabe-/Rücknahmekommissionen, Emissionsabgabe, Anlage-/Steuerberatung, Verwaltungsmandate
- **Beachten:** Darlehen und selbstverwaltete Wertschriften (z.B. Aktien eigene AG) gelten nicht als fremdverwaltet
- **Beachten:** Bund: abziehbar nur Depot-/Safegebühren inkl. Inkasso-/Affidavitspesen; keine Entschädigung eigener Bemühungen
- **Bund:** Belegt sind nur effektive Verwahrungskosten (Depot-, Safegebühren, Inkassospesen; bund-wl-2a-2025__c0056); eine Bundes-Pauschale ist im Wiki nicht belegt → Bundesspalte effektiv (ohne Gebührenausweis 0) oder Kantonspauschale nur mit Vorbehalt (Fachperson).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «16.1 Verwaltungskosten für Wertschriften und sonstige Kapitalanlagen 220»
  - [WL SG 2025 S. 27](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0090.md) `sg-wl-2025__c0090` – «2‰ des fremdverwalteten»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0091.md) `sg-wl-2025__c0091` – «die Finanz-, Anlage-, Erbschafts-, Vorsorge- und Steuerberatung;»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0091.md) `sg-wl-2025__c0091` – «nicht als fremdverwaltetes Wertschriftenvermögen»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0004.md) `sg-form-32-2025__c0004` – «von Online-Spielen, die abgebuchten Spieleinsätze max. Fr. 26'700 max. Fr. 26'800»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0056.md) `bund-wl-2a-2025__c0056` – «(sog. Safegebühren) mit Einschluss der zur Erzielung des Ertra-»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0056.md) `bund-wl-2a-2025__c0056` – «Nicht zulässig ist die Anrechnung einer Entschädigung für ei-»
  - [WL SG 2025 S. 27](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0090.md) `sg-wl-2025__c0090` – «anderen Geldspielen können 5%, jedoch höchstens Fr. 5’400»
  - [WL SG 2025 S. 38](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0134.md) `sg-wl-2025__c0134` – «können unter Ziffer 16.1 5%,»

<a id="16-2-abzug-drittbetreuung"></a>
### Ziff. 16.2 – Kinderbetreuungskosten bei Drittbetreuung (Code 258)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Formular 10 (Kinderbetreuungsabzug): Rechnungen Kita/Tagesmutter; Vorname Kind, bezahlte Kosten, Name/Adresse Betreuungsperson
- **Rein:** Rechnungen Kita/Tagesmutter/Hort 2025 → bezahlte Betreuungskosten je Kind (Formular 10) · Formular 10 → Vorname Kind, Name/Adresse Betreuungsperson
- **Rechnen:** je Kind unter 14 im gleichen Haushalt: min(Betreuungskosten − Verpflegungsanteil; Kanton Fr. 26'700 / Bund Fr. 25'800)
- **Regel:** Max. Fr. 26'700 pro Kind unter 14 Jahren, das im gleichen Haushalt lebt; nur bei direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit. Verpflegung nicht abziehbar (ohne separaten Ausweis Kürzung pauschal Fr. 8 pro Tag bei Betreuung ausserhalb des Haushalts). Formular 10 ist nicht im Wiki: Regel aus Wegleitung.
- **Beachten:** Nur bei direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit
- **Beachten:** Verpflegung nicht abziehbar (Bund: auch Unterkunft); Kanton: ohne separaten Ausweis, Betreuung ausser Haus − Fr. 8/Tag
- **Beachten:** Bund: Drittbetreuung ausserhalb der Arbeits-/Ausbildungszeit nicht abziehbar
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 26'700 (Kinderdrittbetreuungskosten: höchstens Fr. 26'700 pro Kind unter 14 Jahren, das im gleichen Haushalt lebt; kausaler Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit. Verpflegungskosten nicht abziehbar.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind bis max. CHF 25'800 (Kind unter 14, im gleichen Haushalt, Zusammenhang mit Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit))**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 Jahre (Kinderdrittbetreuung: Kinder unter 14 Jahren.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat)**
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «16.2 Kinderbetreuungskosten bei Drittbetreuung Formular 10 258»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0092.md) `sg-wl-2025__c0092` – «Ein Kinderbetreuungsabzug von maximal Fr. 26’700 pro Kind kann geltend»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0054.md) `bund-wl-2a-2025__c0054` – «25 800 Fr., für die Drittbetreuung jedes Kindes (bis 14 Jahre),»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0055.md) `bund-wl-2a-2025__c0055` – «betreuungskosten ausserhalb der Arbeits- oder Ausbildungszeit»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0055.md) `bund-wl-2a-2025__c0055` – «Gleiches gilt für die Kosten für Verpflegung und Unterkunft der»

<a id="16-3-abzug-parteispenden"></a>
### Ziff. 16.3 – Parteispenden (Code 555)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Formular 5 Rückseite Teil B «Total der Parteispenden»; Spendenbestätigung
- **Rein:** Spendenbestätigung/Beitragsrechnung Partei → Σ 2025 (Form. 5 Rückseite Teil B: Datum, Partei, Betrag)
- **Rechnen:** min(Σ Mitgliederbeiträge + Spenden + Gesinnungsbeiträge + Mandatssteuern 2025; Kanton Fr. 10'700 übrige / Fr. 21'400 Ehepaare; Bund Fr. 10'600)
- **Regel:** Max. Fr. 10'700 (Alleinstehende, Verwitwete, getrennt Lebende) bzw. Fr. 21'400 (Ehepaare/eingetragene Partnerschaften). Begünstigte Partei: im Parteienregister eingetragen, im kantonalen Parlament vertreten oder bei letzten Wahlen mind. 3% Stimmen. Mitgliederbeiträge, Gesinnungsbeiträge, Spenden, Mandatssteuern.
- **Beachten:** Partei: im Parteienregister, im kantonalen Parlament vertreten oder in einem Kanton ≥ 3% Stimmen bei letzten Wahlen
- **Beachten:** Bund: Fr. 10'600 auch für Ehepaare (keine separate Grenze)
- **Beachten:** Spenden an gemeinnützige Institutionen nicht hier (→ Ziff. 21.3)
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'700 (Mitgliederbeiträge und Zuwendungen an politische Parteien: höchstens Fr. 10'700 für Alleinstehende/übrige Steuerpflichtige (Partei im Parteienregister, in kantonalem Parlament vertreten oder mind. 3 % Stimmen).)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 21'400 (Parteispenden: höchstens Fr. 21'400 für gemeinsam steuerpflichtige Ehegatten/eingetragene Partner.)** · Bund **n/a – Bund kennt nur einen Gesamtbetrag von CHF 10'600 (Art. 33 Abs. 1 lit. i DBG); keine Verdoppelung für Ehepaare in der Quelle.**
- **Bund:** Bund: max. Fr. 10'600 (Gesamtbetrag, keine separate Grenze für Ehepaare; Art. 33 Abs. 1 lit. i DBG).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «16.3 Parteispenden Formular 5 555»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0093.md) `sg-wl-2025__c0093` – «Parteispenden können maximal in der Höhe von Fr. 10’700»
  - [Formular 5 SG 2025 S. 2](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0004.md) `sg-form-5-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 16.3»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0004.md) `sg-form-32-2025__c0004` – «Parteispenden max. Fr. 10'600»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0053.md) `bund-wl-2a-2025__c0053` – «können bis zum Gesamtbetrag von 10 600 Fr. abgezogen wer-»
  - [Formular 5 SG 2025 S. 2](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0003.md) `sg-form-5-2025__c0003` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.3»

<a id="16-4-abzug-weiterbildung"></a>
### Ziff. 16.4 – Kosten berufsorientierte Aus-/Weiterbildung (Code 223 Person 1 / 224 Person 2)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Aufstellung mit Rechnungsdatum, Bezeichnung, Betrag; Kursrechnungen
- **Rein:** Kursrechnungen/Zahlungsbelege → selbst bezahlte Kosten 2025 (Aufstellung: Rechnungsdatum, Bezeichnung, Betrag) · Bestätigung Kursleitung → zwingend angeschaffte Informatikmittel
- **Rechnen:** je Person: Bund = min(selbst bezahlte berufsorientierte Kosten; Fr. 13'000); Kanton = höherer Betrag aus diesen Kosten und der Pauschale Fr. 400 ohne Nachweis (hauptberuflich Unselbständige), max. Fr. 13'000; Informatik privat nutzbar × 50%
- **Regel:** Selbst bezahlte berufsorientierte Aus-, Weiterbildungs- und Umschulungskosten max. Fr. 13'000 pro Kalenderjahr und Person; Voraussetzung: erster Abschluss Sek. II oder 20. Altersjahr vollendet (nicht Ausbildung bis zum ersten Abschluss Sek. II). Ohne Nachweis Pauschale Fr. 400 für hauptberuflich Unselbständige (nur Kanton/Gemeinde, nicht Bund). Informatikmittel nur bei zwingender Anschaffung (Bestätigung Kursleitung), bei privater Nutzbarkeit 50%. Vom Arbeitgeber getragene Kosten (Lohnausweis Ziff. 13.3) sind nicht steuerbar und hier nicht abziehbar.
- **Beachten:** Voraussetzung: erster Abschluss Sek II oder 20. Lebensjahr vollendet; nicht Ausbildung bis zum ersten Sek-II-Abschluss
- **Beachten:** Pauschale Fr. 400 nur Kanton/Gemeinde, nur hauptberuflich Unselbständige; Bund nur effektive Kosten
- **Beachten:** Ausbildungskosten der Kinder → Ziff. 23.3 (Formular 10)
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
- **Rein:** AHV-Beitragsverfügung/-rechnung Nichterwerbstätige (Ausgleichskasse) → AHV/IV/EO-Beiträge · Weitere übrige Abzüge → Aufstellung mit Art
- **Rechnen:** Σ AHV/IV/EO-Beiträge als Nichterwerbstätige(r) + weitere übrige Abzüge (Art angeben)
- **Regel:** Nur AHV-Beiträge von nichterwerbstätigen Steuerpflichtigen; ordentliche AHV-Beiträge Erwerbstätiger sind bereits in Ziff. 1/2 berücksichtigt. Weitere übrige Abzüge mit Art/Aufstellung.
- **Beachten:** Ordentliche AHV-Beiträge Erwerbstätiger nicht hier (bereits in Ziff. 1 und 2)
- **Beachten:** Bund: Arbeitgeberbeiträge für privates Dienstpersonal nicht abziehbar
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «16.5 Übrige Abzüge Arten 222»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0097.md) `sg-wl-2025__c0097` – «Als übrige Abzüge, die unter dieser Ziffer aufzuführen sind»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0052.md) `bund-wl-2a-2025__c0052` – «Beiträge Nichterwerbstätiger an die AHV, IV und EO.»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0052.md) `bund-wl-2a-2025__c0052` – «Nicht zulässig ist der Abzug von Arbeitgeberbeiträgen für das private Dienstpersonal.»

<a id="17-abzug-zweiverdiener"></a>
### Ziff. 17 – Zweiverdienerabzug (Code 226)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Beilage (beide Personen erwerbstätig)
- **Rein:** Lohnausweise/Erfolgsrechnungen beider Ehegatten → Erwerbseinkommen beider (Bund: niedrigeres Erwerbseinkommen)
- **Rechnen:** Kanton: Fr. 500 fix; Bund: 50% × niedrigeres Erwerbseinkommen, min. Fr. 8'600 (höchstens dieses Einkommen), max. Fr. 14'100
- **Regel:** Gemeinsam Steuerpflichtige, die beide erwerbstätig sind: Fr. 500; gleicher Abzug bei erheblicher Mitarbeit einer Person im Beruf/Geschäft der anderen.
- **Beachten:** Nur gemeinsam Steuerpflichtige, beide erwerbstätig oder erhebliche Mitarbeit (Bund: rechtlich/tatsächlich ungetrennt)
- **Beachten:** Bund-Erwerbseinkommen = Bruttolohn − Berufskosten − AHV/IV/EO/ALV/NBUV − 2. Säule − 3a; Taggelder/EO gleichgestellt
- **Beachten:** Bund: kein Abzug bei Verlust aus Erwerbstätigkeit; Mitarbeit nur, wenn vertraglich vorgesehen oder durch Tätigkeit nötig
- **Limiten:**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **n/a – Prozentsatz nur bei direkter Bundessteuer (siehe Bund).** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (bei Ehegatten in ungetrennter Ehe mit beidseitigem Erwerbseinkommen))**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **n/a** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum)**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **CHF 500 (Zweiverdienerabzug: Fr. 500 (einmal pro gemeinsam steuerpflichtigem Ehepaar, wenn beide erwerbstätig sind; derselbe Abzug bei erheblicher Mitarbeit eines Ehegatten im Beruf/Geschäft des anderen).)** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum)**
- **Bund:** Bund: 50% des niedrigeren Einkommens, min. Fr. 8'600, max. Fr. 14'100.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «17. Zweiverdienerabzug 226»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0097.md) `sg-wl-2025__c0097` – «Gemeinsam Steuerpflichtige, die beide einer Erwerbstätigkeit nachgehen»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0005.md) `sg-form-32-2025__c0005` – «Zweiverdienerabzug Fr. 500 min. Fr. 8'600»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0058.md) `bund-wl-2a-2025__c0058` – «lich und tatsächlich ungetrennter Ehe leben und beide ein»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0059.md) `bund-wl-2a-2025__c0059` – «Bruttolohn abzüglich der Berufskosten sowie der Beiträge an die»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0059.md) `bund-wl-2a-2025__c0059` – «Dem Erwerbseinkommen gleichgestellt sind Erwerbsausfallen-»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0060.md) `bund-wl-2a-2025__c0060` – «Erwerbseinkommen unter dem Minimalbetrag von 8600 Fr., so»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0061.md) `bund-wl-2a-2025__c0061` – «kommt in Betracht, wenn sich aus der Erwerbstätigkeit ein Ver-»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0061.md) `bund-wl-2a-2025__c0061` – «gatten, sofern die Mitarbeit vertraglich vorgesehen oder durch»

<a id="18-berechnung-total"></a>
### Ziff. 18 – Total der Abzüge (Code 230)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 10–17 (Seite 3)
- **Rechnen:** Σ Ziff. 10 bis 17
- **Regel:** Summe Ziff. 10 bis 17.
- **Beachten:** Abweichende Bundesabzüge (Merkblatt 32) passt die Steuerbehörde automatisch an
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «18. Total der Abzüge 230»
  - [WL SG 2025 S. 49](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0173.md) `sg-wl-2025__c0173` – «werden die erforderlichen Anpassungen durch die Steuerbehörde automatisch»

## Einkommensberechnung

<a id="20-berechnung-total"></a>
### Ziff. 20 – Nettoeinkommen (Code 234)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile: Ziffer 7 abzüglich Ziffer 18
- **Rein:** Übertrag Ziff. 7 (Total der Einkünfte) · Übertrag Ziff. 18 (Total der Abzüge)
- **Rechnen:** Ziff. 7 − Ziff. 18
- **Regel:** Basis für Selbstbehalt Krankheitskosten (2%) und Limite freiwillige Zuwendungen (20%).
- **Beachten:** Basis Selbstbehalt Krankheitskosten Ziff. 21.1 (Kanton 2% / Bund 5%) und Limite Zuwendungen Ziff. 21.3 (20%)
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **2 % (Krankheits-/Unfallkosten abziehbar, soweit sie 2 % der Nettoeinkünfte (Nettoeinkommen Ziff. 20) übersteigen. Behinderungsbedingte Kosten ohne Selbstbehalt. Pauschale Diät (Zöliakie) Fr. 2'500.)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: insgesamt höchstens 20 % der Nettoeinkünfte (Nettoeinkommen).)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «20. Nettoeinkommen (Ziffer 7 abzüglich Ziffer 18) 234»

<a id="21-1-abzug-krankheitskosten"></a>
### Ziff. 21.1 – Krankheits- und Unfallkosten (Vorkolonne Code 650, Selbstbehalt Code 238, Abzug Code 240)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 6 Rückseite «Total» selbst getragene Kosten (Bruttobetrag abzüglich Beiträge Dritter)
- **Rein:** Arzt-/Zahnarzt-/Spital-/Therapierechnungen 2025 → Bruttobetrag (Form. 6 Rückseite) · KK-Leistungsabrechnung → Beiträge Dritter abziehen (bei Verweis auf Zusammenzug: Leistungsübersicht beilegen) · Ärztliches Zeugnis/Bescheinigung → Medikamente/Heilmittel, Diät-Pauschale (erstmals) · Übertrag Ziff. 20 → Basis Selbstbehalt
- **Rechnen:** Vorkolonne = Σ (brutto − Beiträge Dritter) [+ Diät-Pauschale Fr. 2'500]; Abzug = max(0; Vorkolonne − 2% × Ziff. 20); Bund: Selbstbehalt 5%
- **Regel:** Nettobetrag (nach Abzug von Vergütungen Dritter) in Vorkolonne; abzugsfähig, soweit er 2% des Nettoeinkommens (Ziff. 20) übersteigt. Diät-Pauschale Fr. 2'500 bei dauernder lebensnotwendiger Diät (z.B. Zöliakie, nicht Diabetes; ärztliche Bescheinigung bei erstmaliger Deklaration). Wird auf Krankenkassen-Zusammenzug verwiesen, detaillierte Leistungsübersicht beilegen.
- **Beachten:** Diät-Pauschale nur bei andauernder lebensnotwendiger Diät (z.B. Zöliakie, nicht Diabetes)
- **Beachten:** Auch Kosten der unterhaltenen Personen, soweit selbst getragen
- **Beachten:** Behinderungsbedingte Kosten nicht hier (→ Ziff. 21.2, ohne Selbstbehalt)
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **2 % (Krankheits-/Unfallkosten abziehbar, soweit sie 2 % der Nettoeinkünfte (Nettoeinkommen Ziff. 20) übersteigen. Behinderungsbedingte Kosten ohne Selbstbehalt. Pauschale Diät (Zöliakie) Fr. 2'500.)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Bund:** Bund: Selbstbehalt 5% der Nettoeinkünfte.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «abzüglich Selbstbehalt 2% des Nettoeinkommens (Ziffer 20)»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0098.md) `sg-wl-2025__c0098` – «2% des Nettoeinkommens gemäss Ziffer 20 übersteigen»
  - [Formular 6 SG 2025 S. 2](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0003.md) `sg-form-6-2025__c0003` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.1 (Vorkolonne)»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0005.md) `sg-form-32-2025__c0005` – «Selbstbehalt 5% der Nettoeinkünfte»
  - [StG SG Art. 46](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-46.md) `sg-stg-2025__art-46` – «die Krankheits- und Unfallkosten des Steuerpflichtigen und der von ihm unterhaltenen Personen»

<a id="21-2-abzug-behinderungskosten"></a>
### Ziff. 21.2 – Behinderungsbedingte Kosten, ohne Selbstbehalt (Code 235)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Formular 6 Rückseite «Behinderungsbedingte Kosten» Total; Verfügung Hilflosenentschädigung
- **Rein:** Heim-/Pflege-/Betreuungsrechnungen 2025 → selbst getragene Kosten (Form. 6 Rückseite) · Verfügung Hilflosenentschädigung (HE) → abziehen bzw. Grundlage Pauschale (einreichen) · Ärztlicher Fragebogen → Pauschale Gehörlose/Dialyse (bei erstmaliger Geltendmachung)
- **Rechnen:** effektiv: Σ selbst getragene Kosten − Beiträge Dritter (Heim ab Pflegestufe 4: − Fr. 2'000 × Monate) ODER Pauschale HE leicht 2'500 / mittel 5'000 / schwer 7'500
- **Regel:** Selbst getragene Kosten ohne Selbstbehalt, abzüglich Vergütungen Dritter (Hilflosenentschädigung). Pflegeheim (ab Pflegestufe 4 / 21 BESA-Punkten): Fr. 2'000 pro Monat gelten als Lebenshaltungskosten, nur Überschuss abziehbar. Alternativ Pauschale: Hilflosenentschädigung leicht Fr. 2'500, mittel Fr. 5'000, schwer Fr. 7'500; Gehörlose/Dialyse Fr. 2'500 (ärztlicher Fragebogen bei erstmaliger Geltendmachung).
- **Beachten:** Gehörlose/Dialysepatienten auch ohne HE: Pauschale Fr. 2'500 (nicht Schwerhörige)
- **Beachten:** Altersheim ohne spezielle Pflege: Lebenshaltungskosten, kein Abzug
- **Beachten:** HE-Pauschale + Gehörlosen-/Dialyse-Pauschale kombiniert nur nach Einzelfallabklärung
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «21.2 Behinderungsbedingte Kosten (ohne Selbstbehalt) Formular 6 235»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0099.md) `sg-wl-2025__c0099` – «Fr. 2’000 pro Monat als nicht abzugsberechtigte Lebenshaltungskosten»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0100.md) `sg-wl-2025__c0100` – «Bezüger einer Hilflosenentschädigung mittleren Grades: Fr. 5’000»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0101.md) `sg-wl-2025__c0101` – «anstelle der effektiven Kosten eine Pauschale von Fr. 2’500 geltend»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0101.md) `sg-wl-2025__c0101` – «Gehörlose (gilt nicht für Schwerhörige; diese können nur die effektiven Kosten»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0101.md) `sg-wl-2025__c0101` – «bedürfen aber stets einer Einzelfallabklärung.»

<a id="21-3-abzug-spenden"></a>
### Ziff. 21.3 – Freiwillige Zuwendungen (Code 244)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Formular 5 Rückseite Teil A «Total der Zuwendungen»; Spendenbestätigungen
- **Rein:** Spendenbestätigungen 2025 → Σ Zuwendungen (Form. 5 Rückseite Teil A: Institution, Datum, Betrag) · Übertrag Ziff. 20 → Basis 20%-Limite
- **Rechnen:** wenn Σ Zuwendungen 2025 ≥ Fr. 100: min(Σ; 20% × Ziff. 20) (Kanton = Bund)
- **Regel:** Nur an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentlicher/gemeinnütziger Zweck), völlig uneigennützig; nicht für Kultuszwecke. Abzug wenn Total mind. Fr. 100, insgesamt höchstens 20% des Nettoeinkommens (Ziff. 20).
- **Beachten:** Nur an steuerbefreite jur. Personen mit Sitz CH (gemeinnützig/öffentlich) sowie Bund, Kantone, Gemeinden; uneigennützig
- **Beachten:** Zuwendungen für Kultuszwecke nicht abziehbar
- **Beachten:** Parteispenden nicht hier (→ Ziff. 16.3)
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): Abzug, wenn im Steuerjahr gesamthaft mindestens Fr. 100. Kultuszwecke nicht abziehbar.)** · Bund **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen (CH) bzw. Gemeinwesen: mindestens CHF 100 im Steuerjahr)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: insgesamt höchstens 20 % der Nettoeinkünfte (Nettoeinkommen).)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «21.3 Freiwillige Zuwendungen (wenn mind. Fr.100, max. 20% Ziffer 20) Formular 5 244»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0102.md) `sg-wl-2025__c0102` – «insgesamt höchstens aber 20% des Nettoeinkommens gemäss Ziffer 20»
  - [StG SG Art. 46](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-46.md) `sg-stg-2025__art-46` – «Im gleichen Umfang abziehbar sind entsprechende freiwillige Leistungen an Bund, Kantone und Gemeinden»
  - [Formular 5 SG 2025 S. 2](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0004.md) `sg-form-5-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 16.3»
  - [Formular 5 SG 2025 S. 2](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0003.md) `sg-form-5-2025__c0003` – «Total der Zuwendungen»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0056.md) `bund-wl-2a-2025__c0056` – «Die Leistungen müssen im Steuerjahr mindestens 100 Fr. errei-»

<a id="22-berechnung-total"></a>
### Ziff. 22 – Reineinkommen (Code 248)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile: Ziffer 20 abzüglich Ziffern 21.1 bis 21.3
- **Rein:** Übertrag Ziff. 20 (Nettoeinkommen) · Übertrag Ziff. 21.1 (Abzug nach Selbstbehalt), 21.2, 21.3
- **Rechnen:** Ziff. 20 − Ziff. 21.1 (nach Selbstbehalt) − 21.2 − 21.3
- **Regel:** Rechenzeile.
- **Beachten:** Weiter: Ziff. 24 steuerbares Einkommen = Ziff. 22 − Sozialabzüge 23.1–23.3 (23.4 nur Bund)
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «22. Reineinkommen (Ziffer 20 abzüglich Ziffern 21.1 bis 21.3) 248»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0011.md) `sg-form-1-2025__c0011` – «24. Steuerbares Einkommen gesamt (Ziffer 22 abzüglich Ziffern 23.1-23.3)»

<a id="23-1-sozialabzug-kinder"></a>
### Ziff. 23.1 – Kinderabzug für jedes noch nicht schulpflichtige Kind (Fr. 7'600, Code 252)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Kinder, für deren Unterhalt zur Hauptsache aufgekommen wird)
- **Rein:** Seite 1 Kinderangaben (Vorname, Name, Geburtsdatum, Schulpflicht) → Anzahl noch nicht schulpflichtige Kinder
- **Rechnen:** Anzahl Kinder unter Sorge/Obhut, noch nicht schulpflichtig × Fr. 7'600; Bund: Fr. 6'800 je Kind + Steuerbetrag − max. Fr. 263 je Kind im gleichen Haushalt
- **Regel:** Verhältnisse am 31.12.2025 bzw. Ende der Steuerpflicht; bei unterjähriger Steuerpflicht anteilig. Kind, für das Unterhaltsbeiträge nach Ziff. 12.2 abgezogen werden, erhält keinen Kinderabzug.
- **Beachten:** Kindergarten zählt zur Schulpflicht (→ 23.2)
- **Beachten:** Stichtag 31. Dezember 2025 bzw. Ende Steuerpflicht; bei unterjähriger Steuerpflicht anteilig
- **Beachten:** Kein Abzug, wenn für das Kind Unterhaltsbeiträge Ziff. 12.2 abgezogen werden
- **Limiten:**
  - Kinderabzug Vorschulalter (CHF): Kanton **CHF 7'600 (Kinderabzug Fr. 7'600 für jedes unter der elterlichen Sorge/Obhut stehende Kind, das noch nicht schulpflichtig ist (Verhältnisse per 31.12.; Steuerpflichtiger kommt zur Hauptsache für Unterhalt auf und beansprucht keinen Unterhaltsabzug).)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (sozialabzug.kind); Staffelung nach Alter nur kantonal.**
  - Kinderabzug Grundbetrag (CHF): Kanton **n/a – Siehe kind_vorschule, kind_schule, kind_ausbildung, kind_ausbildung_auswaerts. Kein Abzug, wenn Unterhaltsbeiträge nach Art. 45 Abs. 1 lit. c StG geltend gemacht werden.** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
  - Abzug vom Steuerbetrag pro Kind (CHF, Bund): Kanton **n/a – Bund-Wert siehe data/werte/bund.** · Bund **CHF 263 (Ermässigung des Steuerbetrags pro Kind bzw. unterstützungsbedürftige Person (Elterntarif: Ehepaare und Alleinstehende mit Kindern im gleichen Haushalt))**
- **Bund:** Bund: Kinderabzug einheitlich Fr. 6'800 pro Kind (kein Vorschul-/Schulabzug, Formular 32 und data/werte/bund/2025); zusätzlich Abzug vom Steuerbetrag Fr. 263 pro Kind (nur Bund).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0011.md) `sg-form-1-2025__c0011` – «23.1 Kinderabzug für jedes noch nicht schulpflichtige Kind Fr. 7’600 252»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0104.md) `sg-wl-2025__c0104` – «Steuerpflichtige, welche für den Unterhalt der Kinder zur Hauptsache aufkom-»
  - [WL SG 2025 S. 13](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0035.md) `sg-wl-2025__c0035` – «Von den Angaben zur Ausbildung resp. Schulpflicht (umfasst auch Kindergarten)»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0103.md) `sg-wl-2025__c0103` – «werden die Sozialabzüge anteilig nach Massgabe der Dauer der Steuerpflicht gewährt»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0006.md) `sg-form-32-2025__c0006` – «einheitlich Fr. 6'800»

<a id="23-2-sozialabzug-kinder"></a>
### Ziff. 23.2 – Kinderabzug für jedes Kind in Schule oder Ausbildung (Fr. 10'800, Code 254)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Schule/Ausbildung, Dauer bis)
- **Rein:** Seite 1 Kinderangaben → Kinder in Schule/Ausbildung; bei beruflicher Ausbildung Schule/Lehrfirma und voraussichtliche Dauer
- **Rechnen:** Anzahl Kinder in Schule (ab Kindergarten) oder Ausbildung (unter Sorge/Obhut oder volljährig) × Fr. 10'800; Bund: Fr. 6'800 je Kind + Steuerbetrag − max. Fr. 263
- **Regel:** Auch für volljährige Kinder in schulischer oder beruflicher Ausbildung, wenn zur Hauptsache für Unterhalt aufgekommen wird.
- **Beachten:** Nur wenn zur Hauptsache für den Unterhalt aufgekommen wird
- **Beachten:** Kein Abzug für Kind mit Unterhaltsbeitragsabzug Ziff. 12.2
- **Beachten:** Voraussetzung für Ausbildungskostenabzug Ziff. 23.3
- **Limiten:**
  - Kinderabzug Schulalter (CHF): Kanton **CHF 10'800 (Kinderabzug Fr. 10'800 für jedes Kind (unter Sorge/Obhut oder volljährig) in schulischer oder beruflicher Ausbildung.)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (sozialabzug.kind).**
  - Kinderabzug Grundbetrag (CHF): Kanton **n/a – Siehe kind_vorschule, kind_schule, kind_ausbildung, kind_ausbildung_auswaerts. Kein Abzug, wenn Unterhaltsbeiträge nach Art. 45 Abs. 1 lit. c StG geltend gemacht werden.** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
  - Abzug vom Steuerbetrag pro Kind (CHF, Bund): Kanton **n/a – Bund-Wert siehe data/werte/bund.** · Bund **CHF 263 (Ermässigung des Steuerbetrags pro Kind bzw. unterstützungsbedürftige Person (Elterntarif: Ehepaare und Alleinstehende mit Kindern im gleichen Haushalt))**
- **Bund:** Bund: einheitlich Fr. 6'800 pro Kind (Schule/Ausbildung).
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0011.md) `sg-form-1-2025__c0011` – «23.2 Kinderabzug für jedes Kind in Schule oder Ausbildung Fr. 10’800 254»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0006.md) `sg-form-32-2025__c0006` – «Fr. 10'800 einheitlich Fr. 6'800»
  - [WL SG 2025 S. 13](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0035.md) `sg-wl-2025__c0035` – «Bei Kindern in beruflicher Ausbildung sind zudem die Schule oder Lehrfirma und»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0104.md) `sg-wl-2025__c0104` – «Unterhaltsbeiträge gemäss Ziffer 12.2 geltend gemacht»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0105.md) `sg-wl-2025__c0105` – «Abzug gebracht werden, wenn für das Kind ein Abzug»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0006.md) `sg-form-32-2025__c0006` – «für Kinder in Schule oder Ausbildung Fr. 10'800 einheitlich Fr. 6'800»

<a id="23-3-sozialabzug-kinder"></a>
### Ziff. 23.3 – Ausbildungskosten für Kinder in Schule oder Ausbildung (Code 256)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Formular 10 (Ausbildungskosten Kinder): Rechnungen Semestergebühren, Bücher, Fahrkosten ÖV
- **Rein:** Rechnungen Semestergebühren, Bücher, Skripte 2025 → Formular 10 · ÖV-Abo zum Ausbildungsort, Belege Wochenaufenthalt/auswärtige Verpflegung → Formular 10 · Stipendienverfügung → erhaltene Stipendien abziehen
- **Rechnen:** je Kind mit Abzug 23.2: min(max(0; selbst getragene Ausbildungskosten − Stipendien − Fr. 3'200); Fr. 13'700); nur Kanton (Bund: kein Abzug)
- **Regel:** Nach Abzug eines Selbstbehalts von Fr. 3'200 und erhaltener Stipendien die effektiven, notwendigen, selbst getragenen Ausbildungskosten, max. Fr. 13'700; nur wenn für das Kind ein Abzug nach Ziff. 23.2 gilt. Nur Kanton/Gemeinde (nicht Bund).
- **Beachten:** Lehrlinge: je halbe Kosten als Ausbildungs- bzw. Berufskosten
- **Beachten:** Fahrkosten nur mit öffentlichen Verkehrsmitteln
- **Limiten:**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 10'800 (Kinder- bzw. Ausbildungsabzug Fr. 10'800 für Kind in schulischer oder beruflicher Ausbildung (auch volljährig).)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Kinderabzug CHF 6'800 wie für Minderjährige (kein höherer Ausbildungsabzug))**
  - Kinder-Ausbildungsabzug Zusatz/Höherstufe (kantonal verschieden: SG zusätzlicher Ausbildungskostenabzug über Selbstbehalt; TG erhöhter Kinderabzug 20.–26. Altersjahr, ersetzt Grund-/16+-Abzug, nicht kumulativ – siehe Text) (CHF): Kanton **CHF 13'700 (Zusätzlicher Ausbildungskostenabzug je Kind in Ausbildung: effektive, notwendige, selbst getragene Kosten, soweit sie den Selbstbehalt von Fr. 3'200 übersteigen (nach Abzug Stipendien), höchstens Fr. 13'700.)** · Bund **n/a – Bund: gleicher Kinderabzug CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).**
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0011.md) `sg-form-1-2025__c0011` – «23.3 Ausbildungskosten für Kinder in Schule oder Ausbildung Formular 10 256»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0105.md) `sg-wl-2025__c0105` – «nach Abzug eines Selbstbehaltes von Fr. 3’200»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0105.md) `sg-wl-2025__c0105` – «geltend gemacht werden kann, maximal: 13’700»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0006.md) `sg-form-32-2025__c0006` – «oder beruflicher Ausbildung, maximal Fr. 13'700 -»

<a id="23-4-sozialabzug-unterstuetzung"></a>
### Ziff. 23.4 – Abzug für unterstützte Personen (nur direkte Bundessteuer, Code 264)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Bedürftigkeit; Name/Adresse der unterstützten Person, geleisteter Betrag
- **Rein:** Bescheinigung Unterstützungsbedürftigkeit (Lebensunterhalt nicht aus eigenen Mitteln bestreitbar) → beilegen · Zahlungsnachweise → geleisteter Betrag 2025; Name, Vorname, Adresse der unterstützten Person
- **Rechnen:** Nur Bund: Anzahl unterstützte Personen (Beitrag je ≥ Fr. 6'800) × Fr. 6'800; Kanton: kein Abzug
- **Regel:** Gilt nur für die direkte Bundessteuer: Fr. 6'800 pro unterstützte erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mind. Fr. 6'800 an den Unterhalt beigetragen wurde. Nicht für Ehegatten und nicht für Kinder mit Kinderabzug. Kantonal kein Abzug.
- **Beachten:** Nur erwerbsunfähige oder beschränkt erwerbsfähige Personen
- **Beachten:** Nicht für Ehegatten/eingetragene Partner und Kinder mit Kinderabzug
- **Beachten:** Bund zusätzlich: Versicherungsabzug +Fr. 700 je Person; Fr. 263 vom Steuerbetrag (gleicher Haushalt)
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **n/a – Gemäss WL 2025 Ziff. 23.4 nur direkte Bundessteuer (Wert siehe data/werte/bund).** · Bund **CHF 6'800 (Unterstützungsabzug pro erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mindestens in Höhe des Abzugs unterstützt; nicht für Ehegatten und Kinder mit Kinderabzug)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'100 (Zuschlag Fr. 1'100 für jedes Kind, für das ein Kinderabzug geltend gemacht werden kann (Gesetz); WL: bis Fr. 1'100.)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
  - Abzug vom Steuerbetrag pro Kind (CHF, Bund): Kanton **n/a – Bund-Wert siehe data/werte/bund.** · Bund **CHF 263 (Ermässigung des Steuerbetrags pro Kind bzw. unterstützungsbedürftige Person (Elterntarif: Ehepaare und Alleinstehende mit Kindern im gleichen Haushalt))**
- **Bund:** Nur Bund: Fr. 6'800 pro Person.
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0011.md) `sg-form-1-2025__c0011` – «23.4 Abzug für unterstützte Personen ja Anzahl Bescheinigung 264»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0106.md) `sg-wl-2025__c0106` – «Der Abzug von Fr. 6’800 für jede unterstützte Person»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0003.md) `sg-form-32-2025__c0003` – «Für jedes Kind (und bei der direkten Bundessteuer für jede un-»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0006.md) `sg-form-32-2025__c0006` – «Gilt auch für unterstützte Personen im gleichen Haushalt.»

<a id="24-berechnung-total"></a>
### Ziff. 24 – Steuerbares Einkommen gesamt (Code 268)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile: Ziffer 22 abzüglich Ziffern 23.1-23.3
- **Rein:** Übertrag aus Ziff. 22 Reineinkommen (Code 248) · Personalien/Kinder Seite 1 (Stichtag 31. Dezember 2025) → Ziff. 23.1/23.2 (Codes 252/254) · Formular 10 → Ziff. 23.3 Ausbildungskosten Kinder (Code 256) · Bescheinigung Unterstützung → Ziff. 23.4 (Code 264, nur Bund)
- **Rechnen:** Kanton: Ziff. 22 − 7'600 × Kind Vorschule − 10'800 × Kind Ausbildung − 23.3 (max. 13'700/Kind) → 268 / Bund: − 6'800 × Kind − 6'800 × Unterstützte − 2'800 Ehepaar
- **Regel:** Rechenzeile (Bund zusätzlich Ziff. 23.4 und weitere Bundesabzüge, von der Behörde angepasst).
- **Beachten:** Stichtag 31. Dezember 2025; unterjährige Steuerpflicht: Sozialabzüge anteilig, für den Steuersatz voll
- **Beachten:** Kinderabzug nur bei Unterhalt zur Hauptsache; entfällt für Kinder mit Unterhaltsbeiträgen (Ziff. 12.2)
- **Beachten:** Bund: Behörde entnimmt Angaben derselben Erklärung (Merkblatt 32); kein 23.3; 23.4 nicht in Code 268
- **Limiten:**
  - Kinderabzug Vorschulalter (CHF): Kanton **CHF 7'600 (Kinderabzug Fr. 7'600 für jedes unter der elterlichen Sorge/Obhut stehende Kind, das noch nicht schulpflichtig ist (Verhältnisse per 31.12.; Steuerpflichtiger kommt zur Hauptsache für Unterhalt auf und beansprucht keinen Unterhaltsabzug).)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (sozialabzug.kind); Staffelung nach Alter nur kantonal.**
  - Kinderabzug Schulalter (CHF): Kanton **CHF 10'800 (Kinderabzug Fr. 10'800 für jedes Kind (unter Sorge/Obhut oder volljährig) in schulischer oder beruflicher Ausbildung.)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (sozialabzug.kind).**
  - Kinderabzug Grundbetrag (CHF): Kanton **n/a – Siehe kind_vorschule, kind_schule, kind_ausbildung, kind_ausbildung_auswaerts. Kein Abzug, wenn Unterhaltsbeiträge nach Art. 45 Abs. 1 lit. c StG geltend gemacht werden.** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
  - Unterstützungsabzug (CHF): Kanton **n/a – Gemäss WL 2025 Ziff. 23.4 nur direkte Bundessteuer (Wert siehe data/werte/bund).** · Bund **CHF 6'800 (Unterstützungsabzug pro erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mindestens in Höhe des Abzugs unterstützt; nicht für Ehegatten und Kinder mit Kinderabzug)**
  - Verheiratetenabzug (CHF, Bund): Kanton **n/a – Bund-Wert siehe data/werte/bund.** · Bund **CHF 2'800 (Verheiratetenabzug für Ehepaare in rechtlich und tatsächlich ungetrennter Ehe)**
- **Quellen:**
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0011.md) `sg-form-1-2025__c0011` – «24. Steuerbares Einkommen gesamt (Ziffer 22 abzüglich Ziffern 23.1-23.3) 268»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «22. Reineinkommen (Ziffer 20 abzüglich Ziffern 21.1 bis 21.3)»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0006.md) `sg-form-32-2025__c0006` – «Abzug für unterstützungsbedürftige Personen»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0001.md) `sg-form-32-2025__c0001` – «Die Veranlagungsbehörde entnimmt daraus – trotz teils unterschiedlicher gesetzlicher Regelung – die Angaben für die Veranlagung beider Steuern»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0103.md) `sg-wl-2025__c0103` – «werden die Sozialabzüge anteilig nach Massgabe der Dauer der Steuerpflicht gewährt»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0104.md) `sg-wl-2025__c0104` – «Der Kinderabzug entfällt für»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0104.md) `sg-wl-2025__c0104` – «Steuerpflichtige, welche für den Unterhalt der Kinder zur Hauptsache aufkom-»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0105.md) `sg-wl-2025__c0105` – «gemäss Ziffer 23.2 geltend gemacht werden kann, maximal: 13’700»
  - [WL SG 2025 S. 31](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0106.md) `sg-wl-2025__c0106` – «Der Abzug von Fr. 6’800 für jede unterstützte Person setzt voraus»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben (Code 300)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 «Total» Steuerwert per 31.12.2025
- **Rein:** Formular 2 → Total Steuerwert nach Abzug G/BG (Übertrag Seite 4 Ziff. 30.1) · Steuerauszug Bank / Depotauszug → Steuerwert 31.12.2025 je Titel bzw. Total · Kontoauszug / Zinsausweis → Saldo 31.12.2025 je Konto · Krypto-Auszug → Bestand und Steuerwert 31.12.2025
- **Rechnen:** Σ Steuerwert 31.12.2025 aller Titel und Guthaben (Form. 2 Total) − Geschäftswertschriften (G/BG) → Ziff. 30.1 (Code 300)
- **Regel:** Steuerwert per 31.12.2025 gemäss Wertschriftenverzeichnis (inkl. Kryptowährungen). Kotierte Papiere: Kursliste; Fremdwährungen umrechnen. Ansprüche aus 2. Säule und Säule 3a bis zur Fälligkeit steuerfrei (nicht deklarieren). Hausrat steuerfrei.
- **Beachten:** Kotierte Titel: Jahresendkurs Kursliste ESTV; Fremdwährung zum Devisen-Jahresendkurs
- **Beachten:** Nichtkotierte Titel: innerer Wert (KS Nr. 28 SSK), Pauschalabzug 30% bei Beteiligung bis 50%
- **Beachten:** Ansprüche 2. Säule und Säule 3a bis zur Fälligkeit steuerfrei (nicht deklarieren)
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «30.1 Wertschriften und Guthaben Formular 2 300»
  - [WL SG 2025 S. 35–36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0121.md) `sg-wl-2025__c0121` – «inkl. Kryptowährungen»
  - [Formular 2 SG 2025 S. 2](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0006.md) `sg-form-2-2025__c0006` – «Abzüglich Geschäftswertschriften bzw. -erträge (G und BG)»
  - [WL SG 2025 S. 37](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0127.md) `sg-wl-2025__c0127` – «Kurswert am Ende des Jahres 2025 (Jahresendkurs) als massgebender»
  - [WL SG 2025 S. 37](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0129.md) `sg-wl-2025__c0129` – «Die Umrechnung von Kursen aus fremden Währungen in Franken erfolgt zum Devisenkurs für Wertschriften»
  - [WL SG 2025 S. 37](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0128.md) `sg-wl-2025__c0128` – «für Minderheitsaktionäre (Beteiligung bis max. 50%) beträgt 30%»
  - [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0107.md) `sg-wl-2025__c0107` – «(Säule 3a) stellen bis zu ihrer Fälligkeit steuerfreies»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 302)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung (Bestand 31.12., Kursliste)
- **Rein:** Aufstellung Bestand 31. Dezember 2025 → Bargeld CHF und Fremdwährungen · Aufstellung Gold/Edelmetalle → Menge × Wert gemäss amtlicher Kursliste
- **Rechnen:** Σ Bargeld (CHF + Fremdwährungen) + Σ Gold/Edelmetalle, je zum Verkehrswert gemäss amtlicher Kursliste per Jahresende → Code 302
- **Regel:** Inländisches und ausländisches Bargeld, Gold und Edelmetalle zum Verkehrswert (amtliche Kursliste).
- **Beachten:** Bank-/Postkonten und übrige Guthaben nicht hier, sondern im Formular 2 (Ziff. 30.1)
- **Beachten:** Schmuck = steuerfreier Gebrauchsgegenstand, ausser Wert deutlich über dem Üblichen (→ Ziff. 30.6)
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «30.2 Bargeld, Gold und andere Edelmetalle Aufstellung 302»
  - [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0110.md) `sg-wl-2025__c0110` – «Gold und andere Edelmetalle mit dem Verkehrswert einzusetzen»
  - [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0109.md) `sg-wl-2025__c0109` – «Die Wertschriften und Guthaben des Privatvermögens einschliesslich aller»
  - [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0109.md) `sg-wl-2025__c0109` – «deren Wert das gemeinhin Übliche deutlich übersteigt»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen (Code 304)

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Bescheinigung Versicherungsgesellschaft: Rückkaufswert inkl. Überschussanteil per 31.12.
- **Rein:** Bescheinigung Versicherungsgesellschaft → Rückkaufswert inkl. Überschussanteil per 31. Dezember 2025 (beilegen) · Police → Gesellschaft, Abschluss-/Ablaufjahr, Versicherungssumme (Zeilenangaben)
- **Rechnen:** Σ Rückkaufswert inkl. Überschussanteil je Police (auch aufgeschobene und laufende Rentenversicherungen) → Code 304
- **Regel:** Rückkaufswert inkl. Überschussanteil; auch laufende und aufgeschobene Renten. Reine Risikoversicherungen ohne Rückkaufswert nicht deklarieren. Bescheinigung beilegen. Zeilenangaben: Versicherungsgesellschaft, Abschlussjahr, Ablaufjahr, Versicherungssumme.
- **Beachten:** Reine Risikoversicherungen ohne Rückkaufswert nicht deklarieren
- **Beachten:** Säule-3a-Ansprüche bis zur Fälligkeit steuerfrei (nicht hier)
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «30.3 Lebens- und Rentenversicherungen Bescheinigung»
  - [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0110.md) `sg-wl-2025__c0110` – «Als steuerbares Vermögen gilt der Rückkaufswert inklusive»
  - [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0107.md) `sg-wl-2025__c0107` – «(Säule 3a) stellen bis zu ihrer Fälligkeit steuerfreies»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge (Code 306)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Kaufvertrag/Fahrzeugausweis: Art, Kaufpreis, Erwerbsjahr
- **Rein:** Kaufvertrag/Rechnung → Kaufpreis (Anschaffungswert) und Erwerbsjahr · Fahrzeugausweis → Art des Fahrzeugs
- **Rechnen:** Je Fahrzeug: Anschaffungswert − 20% × Anschaffungswert × Jahre seit Erwerb → Code 306
- **Regel:** Steuerwert = Anschaffungswert abzüglich 20% pro Jahr seit Erwerb.
- **Beachten:** Motorfahrzeuge zählen nicht zu den steuerfreien persönlichen Gebrauchsgegenständen
- **Beachten:** Fahrzeuge im Geschäftsvermögen Selbständiger in Ziff. 32.2, nicht hier
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «30.4 Motorfahrzeuge Art preis jahr 306»
  - [WL SG 2025 S. 33](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0111.md) `sg-wl-2025__c0111` – «eine Wertverminderung von 20% vom Anschaffungswert abgerechnet werden»
  - [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0109.md) `sg-wl-2025__c0109` – «Nicht dazu zählen Motorfahrzeuge, Boote»
  - [WL SG 2025 S. 33](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0114.md) `sg-wl-2025__c0114` – «Mobilien, Fahrzeuge sowie entgeltlich erworbene immaterielle Güter»
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «32.2 Aktiven gemäss Schlussbilanz per»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Anteile an unverteilten Erbschaften (Code 308)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung Nachlass / Erbteilungsunterlagen
- **Rein:** Aufstellung Nachlass / Erbteilungsunterlagen → Erbanteil und Nachlasswerte (ohne Liegenschaften)
- **Rechnen:** Anteil × Nachlassvermögen (Bewertung nach Ziff. 30/31) − enthaltene Liegenschaften (→ Form. 7) − anderswo deklarierte Anteile → Code 308
- **Regel:** Ab Todestag deklarationspflichtig, auch wenn Anteile zahlenmässig noch nicht feststehen; ohne enthaltene Liegenschaften (Formular 7). Zusätzlich im Formular 2 Seite 1 (Code 961) vermerken.
- **Beachten:** Ab Todestag deklarationspflichtig, auch wenn Anteile noch offen; zusätzlich Form. 2 Seite 1 (Code 961) vermerken
- **Beachten:** Quotale Erträge (Todes- bis Teilungstag) in Ziff. 6.2; VSt darauf quotal im eigenen Form. 2
- **Beachten:** Umfasst auch Nachlass mit Nutzniessung zugunsten eines Dritten
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «30.5 Anteile an unverteilten Erbschaften Aufstellung 308»
  - [WL SG 2025 S. 33](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0111.md) `sg-wl-2025__c0111` – «Die Erben sind ab Todestag für ihren Anteil de-»
  - [Formular 2 SG 2025 S. 1](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0002.md) `sg-form-2-2025__c0002` – «ohne darin enthaltene Liegenschaft(en)»
  - [WL SG 2025 S. 41](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0142.md) `sg-wl-2025__c0142` – «Quotale Vermögenserträge aus unverteilten Erbschaften (Fälligkeiten zwischen dem Todes- und dem Teilungstag) sind unter Ziffer 6.2»
  - [WL SG 2025 S. 36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0125.md) `sg-wl-2025__c0125` – «von jedem Erben quotal im persönlichen Wertschriftenverzeichnis»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte (Code 310)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung mit mutmasslichem Verkehrswert
- **Rein:** Aufstellung je Objekt (Boot, Reitpferd, Kunst, Schmuck, Sammlung) → mutmasslicher Verkehrswert 31. Dezember 2025
- **Rechnen:** Σ mutmasslicher Verkehrswert je Objekt → Code 310
- **Regel:** Boote, Reitpferde, Sammlungen, Kunst-/Schmuckgegenstände mit überdurchschnittlichem Wert; ohne Hausrat und persönliche Gebrauchsgegenstände. Verkehrswert.
- **Beachten:** Hausrat und persönliche Gebrauchsgegenstände steuerfrei (nicht anzugeben)
- **Beachten:** Nur Werte deutlich über dem Üblichen oder mit erheblichem Wertzuwachspotenzial
- **Beachten:** Motorfahrzeuge → Ziff. 30.4
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «30.6 Übrige Vermögenswerte Arten 310»
  - [WL SG 2025 S. 33](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0112.md) `sg-wl-2025__c0112` – «Massgebend ist in der Regel der mutmassliche»
  - [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0108.md) `sg-wl-2025__c0108` – «Nicht anzugeben sind der Hausrat und die persönlichen Gebrauchsgegenstände»
  - [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0109.md) `sg-wl-2025__c0109` – «deren Wert das gemeinhin Übliche deutlich übersteigt»

<a id="31-vermoegen-liegenschaften"></a>
### Ziff. 31 – Liegenschaften (Code 710)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Formular 7 Abschnitt A «Steuerwert» (bei mehreren Formular 7Z Spalte A)
- **Rein:** Formular 7 Abschn. A → Steuerwert je Liegenschaft (bei mehreren: Formular 7Z Total Spalte A) · Verkehrs-/Ertragswertschätzung (vom Gemeindesteueramt eröffnet) → Steuerwert SG-Grundstücke · Andere Kantone: dortiger Steuerwert; Ausland: mutmasslicher Verkehrswert
- **Rechnen:** Σ Steuerwert aller Liegenschaften (Form. 7 bzw. 7Z Spalte A) → Code 710; Neu-/Anbau ohne Schätzung: Schätzung + 80% der Baukosten (Ertragswert 40%)
- **Regel:** Steuerwert gemäss rechtskräftiger Verkehrs- oder Ertragswertschätzung (SG); Liegenschaften in anderen Kantonen/im Ausland mit dem entsprechenden Wert. Ein Formular 7 pro Liegenschaft.
- **Beachten:** Ein Formular 7 pro Liegenschaft; Anteile Person 1/2 in % angeben
- **Beachten:** Geschäftsliegenschaften zum amtlichen Verkehrswert hier (Buchwert nicht in Ziff. 32.2)
- **Beachten:** Zugang/Wegfall 2025 (Kauf, Verkauf, Erbschaft, Schenkung) mit Datum im Form. 7
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «31. Liegenschaften Formular 7 710»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0002.md) `sg-form-7-2025__c0002` – «Übertrag in die Steuererklärung Seite 4 Ziffer 31»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0154.md) `sg-wl-2025__c0154` – «bestimmt sich nach der rechtskräftigen Verkehrs- oder Ertragswertschätzung»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0155.md) `sg-wl-2025__c0155` – «Der massgebliche Steuerwert wird vom Gemeindesteueramt eröffnet»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0155.md) `sg-wl-2025__c0155` – «wertschätzung im Ausmass von 80% der Neu- oder Anbaukosten»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0155.md) `sg-wl-2025__c0155` – «Ertragswert geschätzten Grundstücken (Landwirtschaft) beträgt der Zuschlag 40% der Neu- oder Anbaukosten»
  - [Formular 7Z SG 2025 S. 1](../../chunks/sg/2025/sg-form-7z-2025/sg-form-7z-2025__c0001.md) `sg-form-7z-2025__c0001` – «Bei Besitz von mehr als einer Liegenschaft sind die einzelnen Ergebnisse je Liegenschaft von den Formularen 7 in»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0154.md) `sg-wl-2025__c0154` – «Anteile von Person 1 und Person 2 in Prozenten anzugeben»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0116.md) `sg-wl-2025__c0116` – «jedem Fall zum amtlichen Verkehrswert erfasst werden und unter Ziffer 31»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0002.md) `sg-form-7-2025__c0002` – «Zugang, bzw. Wegfall der Liegenschaft im Jahr 2025»

<a id="32-1-32-3-vermoegen-uebrige"></a>
### Ziff. 32.1-32.3 – Betriebsvermögen aus selbständiger Erwerbstätigkeit: Geschäftskapital Gesellschaften (Code 314), Aktiven Schlussbilanz (Code 316), landwirtschaftlicher Betrieb (Code 318)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Schlussbilanz (Aktiven), Formular 12 (Landwirtschaft), Angaben Formular 11
- **Rein:** Schlussbilanz → Total Aktiven abzüglich Buchwert Geschäftsliegenschaften (Ziff. 32.2, Code 316) · Formular 11 → Anteil am Vermögen Kollektiv-/Kommanditgesellschaft (Ziff. 32.1, Code 314) · Formular 12 → Vermögen landwirtschaftlicher Betrieb (Ziff. 32.3, Code 318)
- **Rechnen:** 32.2 = Aktiven Schlussbilanz − Buchwert Geschäftsliegenschaften; Anlagen = Anschaffungswert − Entwertung; Waren = min(Anschaffungs-/Herstellkosten; Marktwert)
- **Regel:** Aktiven gemäss Schlussbilanz (Fahrzeuge, Maschinen, Mobiliar, Geräte); Buchwert der Geschäftsliegenschaften NICHT hier, sondern in Ziff. 31. Geschäftsschulden in Ziff. 34.2.
- **Beachten:** Geschäftsliegenschaften zum amtlichen Verkehrswert in Ziff. 31
- **Beachten:** Geschäftswertschriften im Form. 2 mit «G»/«BG»; Steuerwert = Einkommenssteuerwert (i.d.R. Bilanzwert)
- **Beachten:** Betriebsschulden separat im Formular 5 Teil B (Ziff. 34.2)
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «32.2 Aktiven gemäss Schlussbilanz per Aufstellung 316»
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «ohne Buchwert der»
  - [WL SG 2025 S. 33](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0114.md) `sg-wl-2025__c0114` – «Massgebend ist der Anschaffungswert, vermindert um die eingetretene»
  - [WL SG 2025 S. 33–34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0115.md) `sg-wl-2025__c0115` – «den Anschaffungs- oder Herstellungskosten bewertet»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0116.md) `sg-wl-2025__c0116` – «Liegenschaften ist vom Total der Aktiven abzurechnen»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0116.md) `sg-wl-2025__c0116` – «entsprechend den Angaben im Formular 11»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0116.md) `sg-wl-2025__c0116` – «Die Betriebsschulden sind im Schuldenverzeichnis (Formular 5)»
  - [WL SG 2025 S. 40](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0141.md) `sg-wl-2025__c0141` – «Massgebend für die Vermögensbesteuerung ist der Einkommenssteuerwert»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 322)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag aus Ziff. 30.1–30.6 (Codes 300–310), Ziff. 31 (Code 710), Ziff. 32.1–32.3 (Codes 314–318)
- **Rechnen:** Σ Ziff. 30.1–30.6 + Ziff. 31 + Ziff. 32.1–32.3 → Code 322
- **Regel:** Summe Ziff. 30 bis 32.
- **Beachten:** Vermögen der minderjährigen Kinder und Nutzniessungsvermögen einschliessen (In- und Ausland)
- **Beachten:** Auch deklarieren, wenn nach Schulden/Sozialabzügen kein steuerbares Vermögen bleibt
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «33. Total der Vermögenswerte 322»
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «der Steuerpflichtigen und der minderjährigen Kinder»
  - [WL SG 2025 S. 32](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0107.md) `sg-wl-2025__c0107` – «Einzusetzen sind auch Vermögenswerte, aus denen sich nach Abzug der Schulden und/oder der Sozialabzüge kein steuerbares»

<a id="34-1-schulden-privat"></a>
### Ziff. 34.1 – Privatschulden (Code 504)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Leasingvertrag Fahrzeug / Leasingraten-Abrechnung → Formular 5 Teil A: Schuld am 31.12.2025 je Gläubiger (Schuldausweis der Bank)
- **Rein:** Schuldausweis/Hypothekarbestätigung Bank → Schuld per 31. Dezember 2025 je Gläubiger (Form. 5 Teil A) · Kredit-/Darlehensvertrag, Kontoauszug → Saldo per 31. Dezember 2025
- **Rechnen:** Σ Schulden 31. Dezember 2025 (Form. 5 Teil A Total) → Code 504; alleinige Haftung voll, Solidar-/Bürgschaftsschulden nur selbst zu tragender Teil
- **Regel:** Nachgewiesene Schulden per 31.12.2025, voll bei alleiniger Haftung; Solidar-/Bürgschaftsschulden nur soweit selbst zu tragen. Zinsen gehören in Ziff. 11.
- **Beachten:** Schuldzinsen 2025 derselben Schulden: Form. 5 Spalte Schuldzinsen → Ziff. 11
- **Beachten:** Leasinggebühren privater Fahrzeuge sind keine abziehbaren Schuldzinsen
- **Beachten:** Geschäftsschulden nicht hier, sondern Form. 5 Teil B (Ziff. 34.2)
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «34.1 Privatschulden Formular 5 504»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0117.md) `sg-wl-2025__c0117` – «Nachgewiesene Schulden, für die eine alleinige Haftung besteht»
  - [Formular 5 SG 2025 S. 1](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0001.md) `sg-form-5-2025__c0001` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 34.1»
  - [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0083.md) `sg-wl-2025__c0083` – «Leasinggebühren persönlicher Gebrauchsgegenstände und privater Fahr»

<a id="34-2-schulden-privat"></a>
### Ziff. 34.2 – Geschäftsschulden (Code 506)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 5 Teil B: Schuld am 31.12. bzw. Bilanzstichtag
- **Rein:** Schlussbilanz/Jahresrechnung → Geschäftsschulden je Gläubiger per Bilanzstichtag (Form. 5 Teil B)
- **Rechnen:** Σ Geschäftsschulden per 31. Dezember 2025 bzw. Bilanzstichtag (Form. 5 Teil B Total) → Code 506
- **Regel:** Geschäftsschulden per Bilanzstichtag; geschäftliche Schuldzinsen sind in der Jahresrechnung enthalten und nicht hier aufzuführen.
- **Beachten:** Geschäftliche Schuldzinsen nicht im Form. 5 bzw. Ziff. 11 (in Jahresrechnung enthalten)
- **Beachten:** Aktiven in Ziff. 32, Betriebsschulden separat im Formular 5
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «34.2 Geschäftsschulden Formular 5 506»
  - [Formular 5 SG 2025 S. 1](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0002.md) `sg-form-5-2025__c0002` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 34.2»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0116.md) `sg-wl-2025__c0116` – «Die Betriebsschulden sind im Schuldenverzeichnis (Formular 5)»
  - [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0083.md) `sg-wl-2025__c0083` – «sind in der Jahresrechnung enthalten und deshalb nicht im Formular 5 aufzuführen»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Reinvermögen (Code 326)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile: Ziffer 33 abzüglich 34
- **Rein:** Übertrag aus Ziff. 33 (Code 322) und Ziff. 34.1/34.2 (Codes 504/506)
- **Rechnen:** Ziff. 33 − (Ziff. 34.1 + 34.2) → Code 326
- **Regel:** Rechenzeile.
- **Beachten:** Reinvermögen ist Ausgangswert für die Sozialabzüge Ziff. 36
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «35. Reinvermögen (Ziffer 33 abzüglich 34) 326»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0118.md) `sg-wl-2025__c0118` – «Vom Reinvermögen gemäss Ziffer 35 können die folgenden Beträge»

<a id="36-1-36-3-vermoegen-sozialabzug"></a>
### Ziff. 36.1-36.3 – Sozialabzüge Vermögen: alleinstehend Fr. 75'000 (Code 330), gemeinsam Fr. 150'000 (Code 332), je minderjähriges Kind Fr. 20'000 (Code 334)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien/Kinder Seite 1 (Stichtag 31.12.2025)
- **Rein:** Personalien Seite 1 → Zivilstand am 31. Dezember 2025 (alleinstehend / gemeinsam steuerpflichtig) · Kinderangaben Seite 1 → Anzahl minderjährige Kinder unter elterlicher Sorge/Obhut
- **Rechnen:** Kanton: 75'000 (alleinstehend) bzw. 150'000 (gemeinsam) + 20'000 × minderjähriges Kind / Bund: keine Vermögenssteuer
- **Regel:** Festbeträge vom Reinvermögen nach den Verhältnissen am 31.12.2025; Kinderabzug für minderjährige Kinder unter elterlicher Sorge/Obhut. Bund kennt keine Vermögenssteuer.
- **Beachten:** Verhältnisse am Ende der Steuerperiode massgebend (i.d.R. 31. Dezember 2025)
- **Beachten:** Nur minderjährige Kinder unter elterlicher Sorge/Obhut; volljährige Kinder in Ausbildung: kein 36.3
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 75'000 (Sozialabzug auf dem Reinvermögen: Fr. 75'000 für jeden Steuerpflichtigen (Alleinstehende).)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 150'000 (Sozialabzug Vermögen für gemeinsam Steuerpflichtige: Fr. 150'000 (2 x Fr. 75'000).)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 20'000 (Zusätzlicher Vermögens-Sozialabzug Fr. 20'000 pro minderjähriges Kind unter elterlicher Sorge/Obhut, für das ein Kinderabzug beansprucht werden kann.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «36.1 Abzug für alleinstehende Steuerpflichtige Fr. 75’000 330»
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «36.2 Abzug für gemeinsam steuerpflichtige Ehegatten Fr. 150’000 332»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0118.md) `sg-wl-2025__c0118` – «20’000 zusätzlich für jedes minderjährige»
  - [DBG Art. 1](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-1.md) `bund-dbg-2025__art-1` – «eine Einkommenssteuer von den natürlichen Personen»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen gesamt (Code 338)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile: Ziffer 35 abzüglich Ziffern 36.1 bis 36.3
- **Rein:** Übertrag aus Ziff. 35 (Code 326) und Ziff. 36.1–36.3 (Codes 330/332/334)
- **Rechnen:** Ziff. 35 − (36.1 bzw. 36.2) − 36.3 → Code 338
- **Regel:** Rechenzeile.
- **Beachten:** Nur Kantons-/Gemeindesteuer; Bund erhebt keine Vermögenssteuer
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «37. Steuerbares Vermögen gesamt (Ziffer 35 abzüglich Ziffern 36.1 bis 36.3) 338»
  - [DBG Art. 1](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-1.md) `bund-dbg-2025__art-1` – «eine Einkommenssteuer von den natürlichen Personen»

## Weitere Angaben

<a id="40-1-40-3-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. 40.1-40.3 – Kapitalleistungen aus Vorsorge: Säule 3a (40.1), 2. Säule (40.2), übrige (40.3)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung / Bank (Auszahlung 2025)
- **Rein:** Bescheinigung Bank/Versicherung Säule 3a → Kapitalauszahlung 2025 (Ziff. 40.1) · Bescheinigung Vorsorgeeinrichtung 2. Säule → Kapitalleistung 2025 (Ziff. 40.2) · Bescheinigung übrige Kapitalleistung mit Vorsorgecharakter → Betrag 2025 (Ziff. 40.3)
- **Rechnen:** Σ 2025 erhaltene Kapitalleistungen; separate Steuer: Kanton einfache Steuer 2,0% Ehegatten bzw. 2,2% übrige / Bund ein Fünftel der Tarife Art. 36 DBG
- **Regel:** Im Jahr 2025 erhaltene Kapitalleistungen angeben; bei mehreren Leistungen Gesamtbetrag. Besteuerung gesondert vom übrigen Einkommen mit separater Jahressteuer; Deklaration nur zu Informationszwecken. Nicht in Ziff. 6.4.
- **Beachten:** Nur Information; separate volle Jahressteuer: Kanton ohne allgemeine und Sozialabzüge / Bund ohne Sozialabzüge
- **Beachten:** Mehrere Leistungen: zusammengerechneter Gesamtbetrag
- **Beachten:** Kanton: Ehegattensatz auch für Alleinstehende, die mit Kindern/Unterstützten zusammenleben
- **Limiten:**
  - Kapitalleistungen aus Vorsorge – Steuersatz/Tarif (separate Jahressteuer): Kanton **Kapitalleistungen aus Vorsorge gesondert, volle Jahressteuer. Einfache Steuer 2,0 % für gemeinsam steuerpflichtige Ehegatten (und Verwitwete/Getrennte/Geschiedene/Ledige mit Kindern bzw. Unterstützungsbedürftigen im gleichen Haushalt), 2,2 % für die übrigen Steuerpflichtigen. Allgemeine Abzüge und Sozialabzüge nicht gewährt; Steueranspruch im Zeitpunkt des Zuflusses.** · Bund **Kapitalleistungen aus Vorsorge (Art. 22 DBG) und Zahlungen bei Tod/bleibenden Nachteilen werden gesondert besteuert (volle Jahressteuer, Steuerjahr des Zuflusses); Steuer = ein Fünftel der Tarife nach Art. 36 Abs. 1, 2 und 2bis erster Satz DBG (Bruchteil 1/5); keine Sozialabzüge.**
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0014.md) `sg-form-1-2025__c0014` – «40.1 aus gebundener Vorsorge Säule 3a Bescheinigung»
  - [WL SG 2025 S. 35](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0119.md) `sg-wl-2025__c0119` – «Kapitalleistungen werden gesondert vom übrigen Einkommen besteuert»
  - [StG SG Art. 52](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-52.md) `sg-stg-2025__art-52` – «Die einfache Steuer beträgt 2,0 Prozent für gemeinsam steuerpflichtige Ehegatten und 2,2 Prozent für die übrigen Steuerpflichtigen»
  - [StG SG Art. 52](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-52.md) `sg-stg-2025__art-52` – «Die allgemeinen Abzüge und die Sozialabzüge werden nicht gewährt»
  - [StG SG Art. 52](../../chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-52.md) `sg-stg-2025__art-52` – «die mit Kindern oder unterstützungsbedürftigen Personen zusammen leben»
  - [DBG Art. 38](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-38.md) `bund-dbg-2025__art-38` – «Sie wird zu einem Fünftel der Tarife nach Artikel 36 Absätze 1, 2 und 2bis erster Satz berechnet»
  - [DBG Art. 38](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-38.md) `bund-dbg-2025__art-38` – «Die Sozialabzüge werden nicht gewährt»
  - [WL SG 2025 S. 35](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0119.md) `sg-wl-2025__c0119` – «ist der zusammengerechnete Gesamtbetrag zu deklarieren»

<a id="41-berechnung-total"></a>
### Ziff. 41 – Total Kapitalleistungen aus Vorsorge (Code 950)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Summe Ziff. 40.1-40.3
- **Rein:** Übertrag aus Ziff. 40.1–40.3
- **Rechnen:** Σ Ziff. 40.1 + 40.2 + 40.3 → Code 950
- **Regel:** Rechenzeile; Informationszweck.
- **Beachten:** Informationszweck; keine weiteren Steuerfolgen in der ordentlichen Veranlagung (separate Jahressteuer)
- **Quellen:**
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0014.md) `sg-form-1-2025__c0014` – «41. Total Kapitalleistungen aus Vorsorge 950»
  - [WL SG 2025 S. 35](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0119.md) `sg-wl-2025__c0119` – «Informationszwecken und hat keine weiteren Steuerfolgen»

## Hilfsblatt Wertschriftenverzeichnis

<a id="form-2-spalte-a-b-einkommen-wertschriften"></a>
### Ziff. Form. 2 Spalte A/B – Verzeichnis der Vermögenswerte: Steuerwert 31.12.2025, Bruttoertrag Spalte A (mit Verrechnungssteuerabzug) / Spalte B (ohne)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Steuerauszug/Bankbescheinigung: Valoren-Nr., Nennwert/Stückzahl, Steuerwert 31.12., Bruttoertrag
- **Rein:** Steuerauszug Bank → Steuerwert 31. Dezember 2025 und Bruttoertrag A/B (Totale übertragen; bei Papiereinreichung Auszug beilegen) · Zinsausweis/Kontoauszug → Saldo und Bruttozins je Konto · Dividenden-/Couponabrechnung Ausland → Bruttoertrag in CHF vor Quellensteuer (Spalte B bzw. DA-1) · Kursliste ESTV → Jahresendkurs kotierter Titel und Devisen
- **Rechnen:** Je Titel Steuerwert + Bruttoertrag (A mit 35% VSt / B ohne); Steuerwert − G/BG → Ziff. 30.1; Ertrag A+B − G/BG − BP (Ziff. 4.2) − BG (Ziff. 4.3) → Ziff. 4.1
- **Regel:** Spalte A: Erträge mit 35% Verrechnungssteuer (u.a. Kundenguthaben mit Bruttozins über Fr. 200, inländische Aktien/Obligationen, Fonds, inländische Lotteriegewinne). Spalte B: ohne Verrechnungssteuer (z.B. Bankzinsen bis Fr. 200, ausländische Titel). Selbst errechnete Zinsen nicht eintragen. Zu- und Abgänge mit Datum und Bankbeleg. Codes: G Geschäftsvermögen, N Nutzniessung, E neuer Titel aus Erbschaft, S aus Schenkung, BP/BG Beteiligung mind. 10%.
- **Beachten:** Bankzinsen bis Fr. 200/Jahr → B, mit VSt-Abzug → A; selbst errechnete Zinsen nicht eintragen
- **Beachten:** Ausland: Bruttoertrag vor Quellensteuer in B; DBA-Anrechnung via DA-1 (nicht rückforderbar ≤ Fr. 100: keine)
- **Beachten:** Zu-/Abgänge mit Datum und Bankbeleg; Codes G, N, E, S, BP, BG in Spalte 1
- **Quellen:**
  - [Formular 2 SG 2025 S. 2](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0005.md) `sg-form-2-2025__c0005` – «Steuerwert am 31. Dezember 2025»
  - [WL SG 2025 S. 38](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0135.md) `sg-wl-2025__c0135` – «Kundenguthaben, deren Bruttozins Fr. 200 übersteigt»
  - [Formular 2 SG 2025 S. 2](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0006.md) `sg-form-2-2025__c0006` – «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A)»
  - [WL SG 2025 S. 36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0122.md) `sg-wl-2025__c0122` – «Steuerauszüge sind bei Einreichung der Steuererklärung auf Papier immer komplett dem Formular 2 beizulegen»
  - [WL SG 2025 S. 37](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0130.md) `sg-wl-2025__c0130` – «Selbst errechnete Zinsen dürfen nicht ein-»
  - [WL SG 2025 S. 40](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0139.md) `sg-wl-2025__c0139` – «ausländische Aktien, Obligationen, Anteile an GmbH, Genossenschaften»
  - [WL SG 2025 S. 41](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0143.md) `sg-wl-2025__c0143` – «ertrag in Schweizer Franken, vor Abzug von Quellensteuern und Kommissionen»
  - [WL SG 2025 S. 41](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0145.md) `sg-wl-2025__c0145` – «nicht rückforderbaren Steuern gemäss DA-1 den Betrag von Fr. 100»
  - [WL SG 2025 S. 37](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0127.md) `sg-wl-2025__c0127` – «Kurswert am Ende des Jahres 2025 (Jahresendkurs) als massgebender»
  - [WL SG 2025 S. 37](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0129.md) `sg-wl-2025__c0129` – «Die Umrechnung von Kursen aus fremden Währungen in Franken erfolgt zum Devisenkurs für Wertschriften»
  - [WL SG 2025 S. 35–36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0121.md) `sg-wl-2025__c0121` – «sind in die entsprechenden Spalten das Datum des Zu- oder Abganges anzugeben und die Bankbelege beizulegen»
  - [WL SG 2025 S. 41](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0142.md) `sg-wl-2025__c0142` – «Spalte 1 mit «E» bzw. «S» zu»
  - [Formular 2 SG 2025 S. 2](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0006.md) `sg-form-2-2025__c0006` – «Abzüglich Erträge aus Privatbeteiligung (BP)»

<a id="form-2-code-999-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 2 Code 999 – Verrechnungssteueranspruch 35% vom Bruttoertrag Total A (Code 999)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Total A × 35%
- **Rein:** Übertrag aus Form. 2 Total Bruttoertrag Spalte A · Steuerauszug Bank → Total Erträge mit Verrechnungssteuerabzug (A)
- **Rechnen:** Total Bruttoertrag Spalte A (vor Abzug G/BG/BP) × 35% → Code 999
- **Regel:** Rückerstattung wird über die Steuererklärung beantragt; bei Verwirkung (nicht deklarierte Erträge) kein Anspruch. Stockwerkeigentümer-Erneuerungsfonds: Formular 25 direkt bei ESTV.
- **Beachten:** Anspruch Fälligkeiten 2025 verwirkt ohne Antrag bis Ende 2028; Fristerstreckung hemmt nicht
- **Beachten:** Nicht deklarierte Erträge/Vermögen: Anspruch verwirkt (ausser fahrlässig und nachträglich angegeben)
- **Beachten:** Kollektiv-/Kommanditgesellschaft und STWE-Erneuerungsfonds: Formular 25 direkt an ESTV
- **Quellen:**
  - [Formular 2 SG 2025 S. 2](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0006.md) `sg-form-2-2025__c0006` – «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A) Fr./Rp. 999»
  - [WL SG 2025 S. 39](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0138.md) `sg-wl-2025__c0138` – «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A)»
  - [WL SG 2025 S. 36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0124.md) `sg-wl-2025__c0124` – «Der Verrechnungssteuersatz für die Fälligkeiten 2025 beträgt 35%»
  - [WL SG 2025 S. 36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0125.md) `sg-wl-2025__c0125` – «spätestens Ende 2028»
  - [WL SG 2025 S. 36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0125.md) `sg-wl-2025__c0125` – «nicht innert drei Jahren nach Ablauf des Kalenderjahres»
  - [WL SG 2025 S. 37](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0126.md) `sg-wl-2025__c0126` – «verwirkt den Anspruch auf Rückerstattung der von diesen»
  - [WL SG 2025 S. 37](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0126.md) `sg-wl-2025__c0126` – «fahrlässig nicht angegeben wurden»
  - [WL SG 2025 S. 36](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0124.md) `sg-wl-2025__c0124` – «Antragsformular 25 bei der Eidg. Steuerverwaltung geltend zu machen»
  - [WL SG 2025 S. 38](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0131.md) `sg-wl-2025__c0131` – «Antragsformular 25 direkt bei der Eidg. Steuerverwaltung»

<a id="form-2-code-960-963-info-schenkungen-erbschaften"></a>
### Ziff. Form. 2 Code 960-963 – Fragen Erbschaften/Schenkungen: Erbschaft erhalten (960), unverteilte Erbschaft (961), Schenkung erhalten (962), verschenkt (963)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Erbteilungsakt / Schenkungsvertrag (Datum, Betrag, Verwandtschaftsgrad)
- **Rein:** Erbteilungsakt (Kopie beilegen) → Erblasser, Todestag, Teilungsdatum, Betrag (Code 960) · Nachlassaufstellung → Erbanteil unverteilte Erbschaft ohne Liegenschaften (Code 961) · Aufstellung Zusammensetzung (beilegen) → Schenkungsdatum, Betrag, Verwandtschaftsgrad (Codes 962/963)
- **Rechnen:** Kein Rechenfeld: Betrag je Vorgang 2025 (960 Erbschaft erhalten, 961 Erbanteil unverteilt, 962 Schenkung erhalten, 963 verschenkt)
- **Regel:** Nur Information im Wertschriftenverzeichnis: Betrag, Todestag/Teilungsdatum bzw. Schenkungsdatum angeben, Erbteilungsakt beilegen. Erbanteil 961 ohne enthaltene Liegenschaften (Formular 7). Titel aus Erbschaft/Schenkung im Verzeichnis mit Code E bzw. S.
- **Beachten:** Fragen von allen zu beantworten; inkl. Erbvorbezüge, Erbauskäufe, Schenkungen unter Nutzniessungsvorbehalt
- **Beachten:** Neue Titel im Verzeichnis mit «E»/«S»; nur seit Erwerb zugeflossene Erträge deklarieren
- **Beachten:** Liegenschaften aus Erbschaft im Formular 7, nicht in Code 961
- **Quellen:**
  - [Formular 2 SG 2025 S. 1](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0002.md) `sg-form-2-2025__c0002` – «Haben Sie im Jahr 2025 eine Erbschaft oder ein Vermächtnis erhalten?»
  - [Formular 2 SG 2025 S. 1](../../chunks/sg/2025/sg-form-2-2025/sg-form-2-2025__c0003.md) `sg-form-2-2025__c0003` – «Haben Sie im Jahr 2025Vermögen verschenkt?»
  - [WL SG 2025 S. 35](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0120.md) `sg-wl-2025__c0120` – «allen Steuerpflichtigen zu beantworten, da sie von allgemeiner Bedeutung sind»
  - [WL SG 2025 S. 35](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0120.md) `sg-wl-2025__c0120` – «Deklaration von Erbschaften und Schenkungen (inkl. Erbvorbezüge und»
  - [WL SG 2025 S. 35](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0120.md) `sg-wl-2025__c0120` – «deklarieren, wenn sie unter»
  - [WL SG 2025 S. 41](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0142.md) `sg-wl-2025__c0142` – «der Vermögenswerte tatsächlich zugeflossenen Erträge aufzuführen»
  - [WL SG 2025 S. 41](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0142.md) `sg-wl-2025__c0142` – «Spalte 1 mit «E» bzw. «S» zu»

## Hilfsblatt Berufskosten

<a id="form-4-ziff-1-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.1 – Fahrkosten öffentliche Verkehrsmittel (Code 400 Person 1 / 450 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg → ÖV-Abo/Billett-Beleg; Weg von-nach, Datum von-bis
- **Rein:** ÖV-Abo/Billettbelege → tatsächliche Kosten Arbeitsweg 2025 (Weg von–nach, Datum von–bis) · Lohnausweis Feld F → angekreuzt = kein Abzug (Sammeltransport/GA vom Arbeitgeber)
- **Rechnen:** Tatsächliche ÖV-Kosten; Σ Ziff. 1.1–1.3: Kanton max. Fr. 8'000 / Bund max. Fr. 3'300 (Maximalabzug, bei Teilzeit/unterjährig nicht gekürzt)
- **Regel:** Tatsächliche Kosten des öffentlichen Verkehrsmittels für den Arbeitsweg. Kein Abzug wenn dem Arbeitnehmer keine Kosten erwachsen (Sammeltransport, vom Arbeitgeber getragenes GA aus geschäftlichen Gründen): Lohnausweis Feld F muss dann angekreuzt sein, kein Fahrkostenabzug. An Home-Office-Tagen und Tagen ohne Arbeitsleistung keine Fahrkosten. Ziff. 1.1-1.3 zusammen max. Fr. 8'000.
- **Beachten:** Home-Office-/arbeitsfreie Tage: keine Fahrkosten; ÖV-Abo aber nicht um Home-Office-Tage kürzen
- **Beachten:** Vom Arbeitgeber übernommene Kosten nicht abziehbar
- **Beachten:** Privatfahrzeug ohne Begründung (Ziff. 1.3): nur Kosten, die mit ÖV angefallen wären
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 pro Person (Maximalabzug, keine Pauschale; bei Teilzeit/unterjährig nicht gekürzt; gilt bei Haupt- und Nebenerwerb insgesamt). Bei direkter Bundessteuer tiefer (Fr. 3'300, siehe data/werte/bund).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Bund:** Bund: Fahrkosten max. Fr. 3'300.
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0001.md) `sg-form-4-2025__c0001` – «1.1 Öffentliche Verkehrsmittel»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0075.md) `sg-wl-2025__c0075` – «muss auf dem Lohnausweis Feld F angekreuzt sein»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0077.md) `sg-wl-2025__c0077` – «Bei Benützung eines öffentlichen Verkehrsmittels (Bahn, Tram, Trolley- oder»
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0010.md) `sg-stb-39-3__c0010` – «muss die Abo-Kosten nicht um die Homeoffice-Tage kürzen»
  - [StB 39 Nr. 3 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0011.md) `sg-stb-39-3__c0011` – «der Betrag bei unterjähriger Steuerpflicht, bei Aufnahme oder Aufgabe der Erwerbstätigkeit während des Jahres sowie bei Teilzeitarbeit nicht gekürzt»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0002.md) `sg-form-32-2025__c0002` – «Fahrkosten zwischen Wohn- und Arbeitsort»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0074.md) `sg-wl-2025__c0074` – «Abzug ist zulässig für Kosten, die der Arbeitgeber übernommen hat»
  - [StB 39 Nr. 3 S. 1](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0003.md) `sg-stb-39-3__c0003` – «kann sie als notwendige Kosten die Auslagen abziehen, die bei»

<a id="form-4-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.2 – Fahrkosten Fahrrad, Kleinmotorrad bis 50 cm3 (Code 402 Person 1 / 452 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Belege (Pauschale)
- **Rein:** Keine Belege; Fahrrad/Kleinmotorrad bis 50 cm3 (gelbes Kontrollschild) → Pauschale Code 402
- **Rechnen:** Pauschale bis Fr. 700/Jahr (Kanton und Bund); zählt zu Σ Ziff. 1.1–1.3 (Kanton max. Fr. 8'000 / Bund max. Fr. 3'300)
- **Regel:** Pauschal bis Fr. 700 im Jahr (Fahrrad oder Kleinmotorrad mit gelbem Kontrollschild).
- **Beachten:** Nur wenn Fussweg zur Arbeit bzw. zur ÖV-Haltestelle mehr als 10 Minuten
- **Beachten:** Grössere Motorräder: Ziff. 1.3 (nur in begründeten Fällen)
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Fahrrad, Motorfahrrad oder Kleinmotorrad bis 50 ccm (gelbes Kontrollschild): Pauschale bis Fr. 700 im Jahr (Voraussetzung: mehr als 10 Minuten zu Fuss zur nächsten ÖV-Haltestelle).)** · Bund **CHF 700 (Pauschale pro Jahr für Fahrrad, Motorfahrrad und Motorrad mit gelbem Kontrollschild; tatsächliche Kosten zusätzlich nicht abziehbar)**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 pro Person (Maximalabzug, keine Pauschale; bei Teilzeit/unterjährig nicht gekürzt; gilt bei Haupt- und Nebenerwerb insgesamt). Bei direkter Bundessteuer tiefer (Fr. 3'300, siehe data/werte/bund).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0001.md) `sg-form-4-2025__c0001` – «1.2 Fahrrad, Kleinmotorrad bis 50 cm3 (Kontrollschild mit gelbem Grund) 402»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0077.md) `sg-wl-2025__c0077` – «bis zu Fr. 700 im Jahr»
  - [StB 39 Nr. 3 S. 1](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0003.md) `sg-stb-39-3__c0003` – «zur nächsten Haltestelle des öffentlichen Verkehrs mehr als 10 Minuten»
  - [StB 39 Nr. 3 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0004.md) `sg-stb-39-3__c0004` – «Die Kosten des privaten Autos oder Motorrades können nur in Abzug gebracht werden»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0002.md) `sg-form-32-2025__c0002` – «Fahrkosten zwischen Wohn- und Arbeitsort»

<a id="form-4-ziff-1-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.3 – Fahrkosten Motorfahrzeug, Fr. 0.70 pro km, Zwischentotal max. Fr. 8'000 (Code 404/406 Person 1; 454/456 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Begründung (Formular), Arbeitstage, km pro Weg; Fahrzeugausweis; Bordbuch bei Geschäftsfahrzeug
- **Rein:** Formular 4 → Begründung ankreuzen (kein ÖV, Einsparung über 60 Min./Tag, Arbeitgeberverlangen, Arztzeugnis) · Formular 4 Zeile → Weg von–nach, km/Weg, km/Tag, Tage, Total km · Arbeitgeberbescheinigung + Spesenabrechnungen, wenn mit Dienstfahrten begründet · Bordbuch bei Geschäftsfahrzeug mit effektiver Abrechnung
- **Rechnen:** km/Tag × Arbeitstage (i.d.R. max. 220) × Fr. 0.70 (Code 404); Σ 1.1–1.3: Kanton max. Fr. 8'000 (Code 406) / Bund max. Fr. 3'300
- **Regel:** Nur in begründeten Fällen (kein ÖV, Zeitersparnis über 60 Min./Tag, Arbeitgeberverlangen, ÖV unzumutbar mit Arztzeugnis). 70 Rp. pro Fahrkilometer, in der Regel max. 220 Arbeitstage. Zwischentotal 1.1-1.3 max. Fr. 8'000. Geschäftsfahrzeug mit Privatanteil 0,9% pro Monat (10,8% pro Jahr) versteuert: kein Fahrkostenabzug (ausser effektive Abrechnung mit Bordbuch). Home-Office-Tage ausschliessen.
- **Beachten:** Geschäftsfahrzeug mit Privatanteil 0,9%/Monat (10,8%/Jahr): kein Abzug; mit Bordbuch effektiv bis Maximum
- **Beachten:** Motorrad: Kanton Fr. 0.70 / Bund Fr. 0.40 pro km
- **Beachten:** 2025 gilt 70 Rp./km; der Ansatz 75 Rp. im StB 39 Nr. 3 (Fassung 2026) gilt erst ab 2026
- **Limiten:**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.70 (Privatfahrzeug (Auto) nur in begründeten Fällen (kein zumutbarer öV): Fr. 0.70 pro Fahrkilometer im Steuerjahr 2025.)** · Bund **CHF 0.70 (Privatauto: Abzug pro Fahrkilometer CHF 0.70, nur wenn kein öffentliches Verkehrsmittel verfügbar/zumutbar (Steuerjahr 2025))**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **220 Tage (In der Regel höchstens 220 Arbeitstage pro Jahr (Vollzeit); höhere Anzahl nachzuweisen. Für Homeoffice-Tage und Tage ohne Arbeitsleistung keine Fahrkosten (ausser ÖV-Abo).)** · Bund **n/a – Bund kennt keine Festlegung massgebender Arbeitstage; abziehbar sind die tatsächlichen notwendigen Kosten bis zum Maximalbetrag (Art. 26 Abs. 1 lit. a DBG).**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 pro Person (Maximalabzug, keine Pauschale; bei Teilzeit/unterjährig nicht gekürzt; gilt bei Haupt- und Nebenerwerb insgesamt). Bei direkter Bundessteuer tiefer (Fr. 3'300, siehe data/werte/bund).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Fahrkosten Motorrad – Ansatz pro km (CHF): Kanton **CHF 0.70 (Motorrad/Motorfahrzeug: gleicher Ansatz wie Auto, Fr. 0.70 pro Fahrkilometer (2025); nur wenn kein öV zumutbar.)** · Bund **CHF 0.40 (Motorrad mit weissem Kontrollschild: CHF 0.40 pro Fahrkilometer (Steuerjahr 2025))**
- **Bund:** Bund: Maximalabzug Fahrkosten Fr. 3'300.
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0002.md) `sg-form-4-2025__c0002` – «km x Fr. 0.70 (Kostensatz gemäss Wegleitung) 404»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0002.md) `sg-form-4-2025__c0002` – «Zwischentotal Ziffern 1.1 – 1.3, max. Fr. 8'000»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0077.md) `sg-wl-2025__c0077` – «Bei Benützung eines Motorfahrzeuges in begründeten Fällen: 70 Rappen je»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0076.md) `sg-wl-2025__c0076` – «entsprechend 10,8% pro Jahr»
  - [StB 39 Nr. 3 S. 5–6](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0019.md) `sg-stb-39-3__c0019` – «Für die Steuerperiode 2025 beträgt der Kilometeransatz Fr. --.70»
  - [StB 39 Nr. 3 S. 5–6](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0019.md) `sg-stb-39-3__c0019` – «Der einheitliche Kilometeransatz von Fr. --.75 gilt ab der Steuerperiode»
  - [StB 39 Nr. 3 S. 3](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0009.md) `sg-stb-39-3__c0009` – «75 Rappen je Fahrkilometer für Motorräder und Autos»
  - [StB 39 Nr. 3 S. 2](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0006.md) `sg-stb-39-3__c0006` – «eine Arbeitgeberbescheinigung sowie die entsprechenden»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0002.md) `sg-form-32-2025__c0002` – «Fahrkosten zwischen Wohn- und Arbeitsort»

<a id="form-4-ziff-2-1-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.1 – Mehrkosten auswärtige Verpflegung, Fr. 15 pro Arbeitstag / Fr. 3'200 pro Jahr (Code 408 Person 1 / 458 Person 2)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Belege; Arbeitstage ohne Home-Office
- **Rein:** Arbeitstage mit auswärtiger Hauptmahlzeit (ohne Home-Office/Absenzen) → Anzahl Tage · Lohnausweis Feld G → angekreuzt: Kantine/Verbilligung, dann Ziff. 2.2 statt 2.1
- **Rechnen:** min(Fr. 15 × Arbeitstage mit auswärtiger Hauptmahlzeit; Fr. 3'200) – Kanton und Bund gleich
- **Regel:** Nur wenn Arbeitspause die Heimkehr nicht ermöglicht (Hauptmahlzeit nicht zu Hause). Fr. 15 pro auswärtige Hauptmahlzeit, bei regelmässigem Mittagessen max. Fr. 3'200 pro Jahr. Nicht kombinierbar mit Schichtarbeit-Abzug (Ziff. 2.3). Keine Verpflegung an Home-Office-Tagen.
- **Beachten:** Verbilligung durch Arbeitgeber/Kantine: Ziff. 2.2 halber Abzug Fr. 7.50/Tag, max. Fr. 1'600
- **Beachten:** Nicht kumulierbar mit Schicht-/Nachtarbeit (Ziff. 2.3)
- **Beachten:** Kein Abzug ohne Mehrkosten gegenüber Verpflegung zu Hause; nicht an Home-Office-Tagen
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswärtige Verpflegung: Fr. 15 pro auswärtige Hauptmahlzeit (Mittagessen), wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann.)** · Bund **CHF 15 (Mehrkosten auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (i.d.R. Mittagessen); ausschliesslich Pauschale, wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei regelmässiger auswärtiger Verpflegung (Mittagessen) Fr. 3'200 im Jahr.)** · Bund **CHF 3'200 (Bei ständiger auswärtiger Verpflegung CHF 3'200 pro Jahr (voller Abzug))**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Verpflegung in Kantine des Arbeitgebers oder durch Arbeitgeberbeitrag/Gutscheine verbilligt: in der Regel halber Abzug, Fr. 7.50 pro Tag (Lohnausweis Feld G). Keine Mehrkosten bei vollständiger Verbilligung: kein Abzug.)** · Bund **CHF 7.50 (Halber Abzug CHF 7.50 pro Hauptmahlzeit, wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei Verbilligung durch Arbeitgeber: halber Abzug, Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: CHF 1'600 pro Jahr)**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «Pro Arbeitstag Fr. 15 / im Jahr Fr. 3'200 408»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0078.md) `sg-wl-2025__c0078` – «Fr. 15 für jede auswärtige Hauptmahlzeit»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0079.md) `sg-wl-2025__c0079` – «Der Abzug für Schicht- und»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0078.md) `sg-wl-2025__c0078` – «Geht jedoch die Verbilligung so weit, dass offensichtlich gar keine Mehrkosten gegenüber der Verpflegung zu Hause entstehen»

<a id="form-4-ziff-2-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.2 – Verpflegung verbilligt durch Arbeitgeber (Kantine, Gutscheine/Lunch-Checks), Fr. 7.50 pro Tag / Fr. 1'600 pro Jahr (Code 410 Person 1 / 460 Person 2)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Feld G (Kantinenverpflegung / Lunch-Checks)
- **Rein:** Lohnausweis → Feld G angekreuzt (Kantine, Gutscheine/Lunch-Checks, AG-Beitrag) · Arbeitszeitnachweis → Arbeitstage mit auswärtiger Hauptmahlzeit (ohne Homeoffice-/Absenztage) · Spesenabrechnung/Spesenreglement → Tage mit Spesenersatz fürs Mittagessen (Kürzung)
- **Rechnen:** min(Arbeitstage × 7.50; 1'600) je Person → Code 410 (P1) / 460 (P2); bei Spesenersatz × (Tage − Spesentage) / Tage; Kanton = Bund
- **Regel:** Ist im Lohnausweis Feld G angekreuzt (Kantine, Barbeitrag oder Gutscheine/Lunch-Checks des Arbeitgebers), nur halber Abzug: Fr. 7.50 pro Tag, max. Fr. 1'600 pro Jahr (statt Ziff. 2.1). Bei so weitgehender Verbilligung, dass offensichtlich keine Mehrkosten entstehen: kein Abzug.
- **Beachten:** Verbilligung so weit, dass offensichtlich keine Mehrkosten entstehen → kein Abzug
- **Beachten:** Kantine zumutbar, aber freiwillig nicht genutzt → trotzdem nur halber Abzug
- **Beachten:** Homeoffice-Tage und Tage ohne Arbeitsleistung zählen nicht; nicht kumulierbar mit Schichtabzug 2.3
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Verpflegung in Kantine des Arbeitgebers oder durch Arbeitgeberbeitrag/Gutscheine verbilligt: in der Regel halber Abzug, Fr. 7.50 pro Tag (Lohnausweis Feld G). Keine Mehrkosten bei vollständiger Verbilligung: kein Abzug.)** · Bund **CHF 7.50 (Halber Abzug CHF 7.50 pro Hauptmahlzeit, wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei Verbilligung durch Arbeitgeber: halber Abzug, Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: CHF 1'600 pro Jahr)**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «Pro Arbeitstag Fr. 7.50 / im Jahr Fr. 1'600 410»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0078.md) `sg-wl-2025__c0078` – «In diesem Fall ist auf dem Lohnausweis Feld G»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0007.md) `sg-form-4-2025__c0007` – «Pro Arbeitstag Fr. 7.50 / im Jahr Fr. 1'600 460»
  - [StB 39 Nr. 8 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0015.md) `sg-stb-39-8__c0015` – «steht ihm trotz Verpflegung zu höheren Kosten nur der halbe Abzug zu»
  - [StB 39 Nr. 8 S. 4](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0016.md) `sg-stb-39-8__c0016` – «Pauschalabzug im Verhältnis der Arbeitstage mit vergüteter Verpflegung herabgesetzt»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0002.md) `sg-form-4-2025__c0002` – «An Home-Office-Tagen und»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0002.md) `sg-form-4-2025__c0002` – «Tagen ohne Arbeitsleistung entstehen keine Kosten für»
  - [StB 39 Nr. 8 S. 2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0006.md) `sg-stb-39-8__c0006` – «Der Abzug für Schicht- oder Nachtarbeit kann nicht zusätzlich zum Abzug für auswärtige Verpflegung»

<a id="form-4-ziff-2-3-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.3 – Schicht-/Nachtarbeit (mind. 8 Stunden durchgehend), Fr. 15 pro Schichttag / Fr. 3'200 pro Jahr (Code 412 Person 1 / 462 Person 2)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 «Bemerkungen» (Anzahl Schichttage) oder separates Arbeitgeberschreiben
- **Rein:** Lohnausweis → Ziff. 15 Bemerkungen: Anzahl Schichttage · Arbeitgeberbescheinigung (separates Schreiben) → Anzahl Schichttage, falls nicht im Lohnausweis
- **Rechnen:** min(Schichttage × 15; 3'200) je Person → Code 412 (P1) / 462 (P2); Kanton = Bund
- **Regel:** Anzahl geleisteter Schichttage muss der Arbeitgeber im Lohnausweis unter Ziff. 15 (Bemerkungen) oder in separatem Schreiben bescheinigen. Fr. 15 pro Schichttag, ganzjährig max. Fr. 3'200. Nicht zusammen mit Verpflegungsabzug Ziff. 2.1/2.2.
- **Beachten:** Nur durchgehende, mind. achtstündige Schicht/Nacht; gestaffelt nur, wenn beide Hauptmahlzeiten nicht zu Hause möglich
- **Beachten:** Nicht kumulierbar mit Verpflegungsabzug 2.1/2.2; keine Mindestdistanz Wohn-/Arbeitsort nötig
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Schicht-/Nachtarbeit mit durchgehender, mindestens achtstündiger Tätigkeit: Fr. 15 pro Schichttag, bei ganzjähriger Schichtarbeit Fr. 3'200. Nicht kumulierbar mit Abzug für auswärtige Verpflegung; Schichttage vom Arbeitgeber zu bescheinigen.)** · Bund **CHF 15 (Durchgehende Schicht-/Nachtarbeit (gestaffelte Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich): CHF 15 pro ausgewiesenem Tag, bei ganzjähriger Schicht-/Nachtarbeit CHF 3'200 pro Jahr)**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «Pro ausgewiesenen Schichttag Fr. 15 / im Jahr Fr. 3'200 412»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0079.md) `sg-wl-2025__c0079` – «geleisteter Schichttage ist vom Arbeit-»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0007.md) `sg-form-4-2025__c0007` – «Pro ausgewiesenen Schichttag Fr. 15 / im Jahr Fr. 3'200 462»
  - [StB 39 Nr. 8 S. 2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0006.md) `sg-stb-39-8__c0006` – «sofern beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause eingenommen werden können»
  - [StB 39 Nr. 8 S. 2](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0006.md) `sg-stb-39-8__c0006` – «Verpflegungsabzug ist in diesen Fällen nicht abhängig von einer minimalen Entfernung»

<a id="form-4-ziff-3-1-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4 Ziff. 3.1 – Pauschalabzug übrige Berufskosten: Fr. 700 + 10% des Nettolohnes, max. Fr. 2'400 (Code 416 Person 1 / 466 Person 2)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Nettolohn gemäss Ziff. 1.1 / Lohnausweis Ziff. 11
- **Rein:** Lohnausweis → Nettolohn (= Steuererklärung Ziff. 1.1, Code 100/102) · Lohnausweis/Spesenreglement → ausbezahlte nicht ereignisbezogene Pauschalspesen (dann keine Pauschale) · ALV-Abrechnung → Taggelder (Pauschale sinngemäss)
- **Rechnen:** Kanton: min(700 + 10% × Nettolohn; 2'400) / Bund: min(max(3% × Nettolohn; 2'000); 4'000) → Code 416 (P1) / 466 (P2); Teiljahr umrechnen
- **Regel:** Pauschale ohne Nachweis; auch bei Bezug von ALV-Leistungen sinngemäss. Bei Auszahlung nicht ereignisbezogener Pauschalspesen nicht zusätzlich geltend zu machen.
- **Beachten:** Nicht zusätzlich zu ausbezahlten nicht ereignisbezogenen Pauschalspesen
- **Beachten:** Arbeitszimmer ist mit der Pauschale abgegolten (keine Kumulation)
- **Beachten:** Bund-Abweichung (3%-Pauschale) nimmt das Steueramt automatisch vor
- **Limiten:**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockelbetrag der Pauschale übrige Berufskosten: Fr. 700 (+ 10 % des Nettolohnes).)** · Bund **n/a – Bund: 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; kein 'fix + %'-Modell.**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Pauschale übrige Berufskosten: Fr. 700 zuzüglich 10 % der Nettoeinkünfte (Nettolohn), höchstens Fr. 2'400; Nachweis höherer Kosten vorbehalten. Nettoeinkünfte = Bruttoeinkünfte abzüglich Beiträge AHV/IV/EO/ALV/UV und BVG (ohne Einkäufe).)** · Bund **3 % (Übrige Berufskosten (Art. 26 Abs. 1 lit. c DBG): Pauschale 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; anstelle der Pauschale ist der Nachweis höherer tatsächlicher übriger Berufskosten möglich. Fahrkosten (lit. a, max. 3'300 gemäss DBG 2025; WL 2a 2025 nennt 3'200 – Widerspruch siehe berufskosten.fahrkosten.max) und Verpflegung (lit. b) werden zusätzlich abgezogen. Bei Teilzeit/Teiljahr angemessen kürzen.)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Pauschale übrige Berufskosten höchstens Fr. 2'400.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **n/a – Formel in Art. 21 StV SG nennt nur Fix-Betrag, Satz und Maximum.** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
- **Bund:** Bund: 3% des Nettolohnes, mind. Fr. 2'000, max. Fr. 4'000.
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «Pauschalabzug: Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2'400 416»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0080.md) `sg-wl-2025__c0080` – «Pauschale von Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2’400»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0002.md) `sg-form-32-2025__c0002` – «max. Fr. 2'400 max. Fr. 4'000»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0007.md) `sg-form-4-2025__c0007` – «Pauschalabzug: Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2'400 466»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0001.md) `sg-form-4-2025__c0001` – «Ziffer 3 und 5 sind nach Dauer der Steuerpflicht»
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) `sg-form-1-2025__c0004` – «Aus Haupterwerbstätigkeit Person 1 Lohnausweis 100»
  - [StB 39 Nr. 1 S. 1](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0001.md) `sg-stb-39-1__c0001` – «Sie gelten grundsätzlich als mit der Pauschale abgegolten»
  - [WL SG 2025 S. 49](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0173.md) `sg-wl-2025__c0173` – «erforderlichen Anpassungen durch die Steuerbehörde automatisch»

<a id="form-4-ziff-3-2-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4 Ziff. 3.2 – Tatsächliche übrige Berufskosten anstelle Pauschale (Code 418 Person 1 / 468 Person 2)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Aufstellung/Beiblatt mit Belegen
- **Rein:** Quittungen/Rechnungen übrige Berufskosten (z.B. Berufswerkzeuge) → Beiblatt zu Formular 4 · Mietvertrag bzw. Eigenmietwert + Nebenkosten → Arbeitszimmeranteil (nur bei beruflicher Notwendigkeit) · Arbeitsvertrag/AG-Bestätigung → kein Arbeitsplatz beim AG, Anteil Arbeit zu Hause
- **Rechnen:** Σ belegte Kosten (Beiblatt) → Code 418 (P1) / 468 (P2), nur wenn > 3.1; Arbeitszimmer = Miete bzw. EMW netto (inkl. NK) / (Zimmer + 2), Teilzeit anteilig
- **Regel:** Nur wenn die tatsächlichen Kosten die Pauschale übersteigen; Nachweis über Beiblatt, mit Formular 4 einreichen. Entweder Pauschale (3.1) oder effektiv (3.2).
- **Beachten:** Entweder Pauschale 3.1 oder effektiv: dann sämtliche übrigen Kosten inkl. Arbeitszimmer belegen
- **Beachten:** Arbeitszimmer kumulativ: ca. 40% der Arbeitszeit zu Hause, kein AG-Arbeitsplatz, ausgeschiedener Raum
- **Beachten:** Bund: gleiche Voraussetzungen und Berechnung fürs Arbeitszimmer
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «3.2 Anstelle des Pauschalabzuges: tatsächliche Berufskosten»
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0080.md) `sg-wl-2025__c0080` – «so können gegen Nachweis die tatsächlichen Auf»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0007.md) `sg-form-4-2025__c0007` – «Anstelle des Pauschalabzuges: tatsächliche Berufskosten Aufstellung»
  - [StB 39 Nr. 9 S. 1](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0001.md) `sg-stb-39-9__c0001` – «übrige Berufskosten (z.B. Arbeitszimmer zu Hause, Berufswerkzeuge u.a.)»
  - [StB 39 Nr. 1 S. 1](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0001.md) `sg-stb-39-1__c0001` – «müssen sämtliche tatsächlichen Aufwendungen nachgewiesen werden»
  - [StB 39 Nr. 1 S. 1](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0003.md) `sg-stb-39-1__c0003` – «ca. 40% der gesamten Arbeitszeit ausmacht»
  - [StB 39 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0005.md) `sg-stb-39-1__c0005` – «wobei für die Berechnung die Gesamtkosten durch die Anzahl Zimmer plus zwei geteilt werden»
  - [StB 39 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0005.md) `sg-stb-39-1__c0005` – «Bei Teilzeitarbeit besteht kein Anspruch auf den vollen Arbeitszimmerabzug»
  - [StB 39 Nr. 1 S. 2](../../chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0006.md) `sg-stb-39-1__c0006` – «Die Abzugsvoraussetzungen sind gleich wie im kantonalen Recht; die Berechnung erfolgt ebenfalls gleich»

<a id="form-4-ziff-4-1-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4 Ziff. 4.1 – Wochenaufenthalt: Unterkunft, ortsübliche Kosten Zimmer (Code 426 Person 1 / 476 Person 2)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag/Beleg Zimmer: Monate × Betrag
- **Rein:** Mietvertrag/Mietzinsbelege Zimmer bzw. Studio am Arbeitsort → Monate × Monatsmiete · Arbeitszeit-/Arbeitswegangaben → Begründung, dass tägliche Rückkehr unzumutbar ist
- **Rechnen:** Monate × tatsächliche Zimmermiete, anerkannt bis 800/Mt. (Städte Zürich, Bern, Basel, Lausanne, Genf, gr. Kurorte), sonst bis 500/Mt. → Code 426 (P1) / 476 (P2)
- **Regel:** Nur wenn tägliche Rückkehr aus zeitlichen oder finanziellen Gründen unzumutbar und steuerlicher Wohnsitz am Heimatort. Tatsächliche Kosten für ein Zimmer (nicht Wohnung), je nach Arbeitsort Fr. 500 bis Fr. 800 pro Monat. Heimfahrten unter Ziff. 1.
- **Beachten:** Zimmer = 1-Zimmerwohnung/Studio; teurere Unterkunft = nicht abziehbare Lebenshaltung
- **Beachten:** Tägliche Rückkehr zumutbar → i.d.R. Wohnsitz am Arbeitsort (kein Abzug)
- **Beachten:** Heimfahrten unter Form. 4 Ziff. 1 (Fahrkosten)
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Wochenaufenthalt: tatsächliche Kosten für ein auswärtiges Zimmer (nicht Wohnung), je nach Arbeitsort Fr. 500 bis Fr. 800 pro Monat (Fr. 800 in Zürich, Bern, Basel, Lausanne, Genf und grösseren Kurorten, sonst bis Fr. 500). Voraussetzung: tägliche Rückkehr nicht zumutbar; Fahrkosten separat unter Fahrkosten.** · Bund **Mehrkosten Unterkunft: ortsübliche Auslagen für ein Zimmer (nicht eine Wohnung) abziehbar; Fahrkosten der regelmässigen Heimkehr bis zum Maximalbetrag nach Art. 5 Abs. 1 BKV**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0004.md) `sg-form-4-2025__c0004` – «4.1 Unterkunft: Ortsübliche Kosten für ein Zimmer»
  - [WL SG 2025 S. 24–25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0081.md) `sg-wl-2025__c0081` – «je nach Arbeitsort Fr. 500 bis Fr. 800 pro Monat»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0008.md) `sg-form-4-2025__c0008` – «Unterkunft: Ortsübliche Kosten für ein Zimmer Monate à Fr. 476»
  - [StB 39 Nr. 5 S. 2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0004.md) `sg-stb-39-5__c0004` – «Monatsmieten bis Fr. 800.--, an anderen Orten bis Fr. 500.-- allgemein anerkannt»
  - [StB 39 Nr. 5 S. 2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0004.md) `sg-stb-39-5__c0004` – «oder ein Studio mit Bad und kleiner Küche bzw. Kochecke verstanden»
  - [StB 39 Nr. 5 S. 1](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0002.md) `sg-stb-39-5__c0002` – «ist in der Regel davon auszugehen, dass er auch seinen steuerlichen Wohnsitz und damit sein Hauptsteuerdomizil an den Arbeitsort verlegt»

<a id="form-4-ziff-4-2-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4 Ziff. 4.2 – Wochenaufenthalt: Verpflegung Fr. 30 pro Arbeitstag / Fr. 6'400 pro Jahr (Code 428 Person 1 / 478 Person 2)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (bei Verbilligung der Mittagsmahlzeit)
- **Rein:** Lohnausweis → Feld G (Verbilligung) → reduzierter Ansatz · Arbeitszeitnachweis → Arbeitstage am Wochenaufenthaltsort
- **Rechnen:** Voll: min(Tage × 30; 6'400); verbilligt (Kantine/Feld G): min(Tage × 22.50; 4'800) → Code 428 (P1) / 478 (P2); Kanton = Bund
- **Regel:** Fr. 30 pro Tag, ganzjährig max. Fr. 6'400. Bei Verbilligung der Mahlzeiten durch den Arbeitgeber (Kantine, Kostenbeitrag, Feld G) Fr. 22.50 pro Tag bzw. Fr. 4'800 pro Jahr.
- **Beachten:** Reduziert schon, wenn eine der beiden Hauptmahlzeiten verbilligt bzw. Kantine verfügbar ist
- **Beachten:** Nicht zusätzlich zur Verpflegungspauschale bei täglicher Heimkehr
- **Beachten:** Nachweis höherer Verpflegungskosten ausgeschlossen
- **Limiten:**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 6'400 (Wochenaufenthalt Verpflegung: Fr. 30 im Tag, bei ganzjährigem Wochenaufenthalt Fr. 6'400 im Jahr; bei Verbilligung durch Arbeitgeber Fr. 22.50 im Tag bzw. Fr. 4'800 im Jahr.)** · Bund **CHF 6'400 (Auswärtiger Wochenaufenthalt: Verpflegung CHF 30 pro Tag, max. CHF 6'400 pro Jahr; bei Verbilligung CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr; Nachweis höherer Kosten ausgeschlossen)**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0004.md) `sg-form-4-2025__c0004` – «Pro Arbeitstag Fr. 30 / im Jahr Fr. 6'400»
  - [WL SG 2025 S. 24–25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0081.md) `sg-wl-2025__c0081` – «gesamthaft Fr. 22.50 im Tag, bzw. Fr. 4’800 im Jahr»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0008.md) `sg-form-4-2025__c0008` – «Verbilligung der Mahlzeiten durch den Arbeitgeber pro Arbeitstag Fr. 22.50 / im Jahr Fr. 4'800 478»
  - [StB 39 Nr. 5 S. 1–2](../../chunks/sg/dauernd/sg-stb-39-5/sg-stb-39-5__c0003.md) `sg-stb-39-5__c0003` – «Der reduzierte Abzug ist anzuwenden, wenn eine der beiden täglichen Hauptmahlzeiten vom Arbeitgeber verbilligt wird»
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0013.md) `sg-stb-39-8__c0013` – «Der Pauschalabzug für auswärtige Verpflegung bei täglicher Heimkehr kann nicht»
  - [StB 39 Nr. 8 S. 3](../../chunks/sg/dauernd/sg-stb-39-8/sg-stb-39-8__c0011.md) `sg-stb-39-8__c0011` – «kann nicht von den Pauschalen abgewichen werden»

<a id="form-4-ziff-5-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 4 Ziff. 5 – Kosten bei unselbständiger Nebenerwerbstätigkeit: Pauschale 20% der Nettoeinkünfte, min. Fr. 800, max. Fr. 2'400 (Code 432) bzw. tatsächliche Kosten (Code 434); Person 2: 482/484

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 des Nebenerwerbs (Nettolohn Ziff. 1.2)
- **Rein:** Lohnausweis Nebenerwerb (NE) → Nettolohn (= Steuererklärung Ziff. 1.2, Code 104/106) · Arbeitsvertrag Haupterwerb → Pensum (Haupterwerb mind. zwei Drittel) · Belege effektive Kosten (alle Nebenerwerbe) → Code 434/484, nur wenn > Pauschale
- **Rechnen:** NE-Nettolohn ≤ 800: Abzug bis Höhe Nettolohn; sonst min(max(20% × Σ Netto aller NE; 800); 2'400) → Code 432 (P1) / 482 (P2); Kanton = Bund; Teiljahr umrechnen
- **Regel:** Auslagen bis Höhe des Nettolohns, soweit Nebeneinkünfte netto Fr. 800 nicht übersteigen; darüber 20% (min. Fr. 800, max. Fr. 2'400). Nachweis höherer Kosten vorbehalten. Kein Anspruch ohne Haupterwerbstätigkeit bei Dritten (Pensionierte, Hausfrauen); in der Regel nicht für VR-Honorare.
- **Beachten:** Pauschale deckt auch Fahrkosten und Verpflegung des Nebenerwerbs (kein Zusatzabzug)
- **Beachten:** Haupterwerb bei Dritten nötig (mind. zwei Drittel Pensum); nicht für Pensionierte/Hausfrauen, i.d.R. nicht VR-Honorare
- **Beachten:** Pauschale oder effektiv einheitlich für alle Nebenerwerbe
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Unselbständiger Nebenerwerb: Pauschale 20 % der Nettoeinkünfte aus der Nebentätigkeit, mindestens Fr. 800, höchstens Fr. 2'400 pro Jahr. Bei Nettolohn bis Fr. 800: Auslagen bis zur Höhe des Nettolohns. Kein Anspruch ohne Haupterwerb bei Dritten; in der Regel nicht für VR-Honorare.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge))**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb-Pauschale mindestens Fr. 800 (Nettoeinkünfte bis Fr. 800: Abzug bis zur Höhe des Nettolohns).)** · Bund **CHF 800 (Minimum Pauschale Nebenerwerb)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb-Pauschale höchstens Fr. 2'400 im Jahr.)** · Bund **CHF 2'400 (Maximum Pauschale Nebenerwerb)**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0004.md) `sg-form-4-2025__c0004` – «5.1 Pauschalabzug: 20% der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400 432»
  - [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0082.md) `sg-wl-2025__c0082` – «Steuerpflichtige, die keine Haupterwerbstätigkeit bei Dritten ausüben»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0008.md) `sg-form-4-2025__c0008` – «Pauschalabzug: 20% der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400 482»
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) `sg-form-1-2025__c0004` – «Aus Nebenerwerbstätigkeit Person 1 Lohnausweis 104»
  - [StB 39 Nr. 9 S. 2](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0005.md) `sg-stb-39-9__c0005` – «wenigstens zwei Drittel einer 100-prozentigen Arbeitszeit entspricht»
  - [StB 39 Nr. 9 S. 3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0012.md) `sg-stb-39-9__c0012` – «Die Pauschale von 20% errechnet sich aus der Summe aller Nebenerwerbseinkünfte»
  - [StB 39 Nr. 9 S. 3](../../chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0013.md) `sg-stb-39-9__c0013` – «schliesst die Nebenerwerbspauschale auch die Fahrkosten und die Mehrkosten»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0001.md) `sg-form-4-2025__c0001` – «Ziffer 3 und 5 sind nach Dauer der Steuerpflicht»

<a id="form-4-ziff-6-berechnung-total"></a>
### Ziff. Form. 4 Ziff. 6 – Total der Berufskosten (Code 438 Person 1 / 488 Person 2)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Ziff. 1 bis 5
- **Rein:** Übertrag Form. 4 Ziff. 1–5 je Person (P1 Vorderseite, P2 Rückseite)
- **Rechnen:** Code 438 = Fahrkosten-Zwischentotal 406 (max. 8'000) + Verpflegung 2.x + übrige 3.x + Wochenaufenthalt 4.x + Nebenerwerb 5.x → Ziff. 10.1; P2: Code 488 → Ziff. 10.2
- **Regel:** Übertrag in Steuererklärung Seite 3 Ziff. 10.1 (Person 1) bzw. 10.2 (Person 2). Formular 4 Vorderseite Person 1, Rückseite Person 2.
- **Beachten:** Bund: Fahrkosten max. 3'300 und Pauschale übrige Berufskosten abweichend – Anpassung durch Steueramt automatisch
- **Beachten:** Fahrkosten-Max. gilt für Haupt- und Nebenerwerb insgesamt und wird bei Teilzeit/Teiljahr nicht gekürzt
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 pro Person (Maximalabzug, keine Pauschale; bei Teilzeit/unterjährig nicht gekürzt; gilt bei Haupt- und Nebenerwerb insgesamt). Bei direkter Bundessteuer tiefer (Fr. 3'300, siehe data/werte/bund).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Quellen:**
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0004.md) `sg-form-4-2025__c0004` – «6. Total der Berufskosten 438»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0004.md) `sg-form-4-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 10.1»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0002.md) `sg-form-4-2025__c0002` – «Zwischentotal Ziffern 1.1 – 1.3, max. Fr. 8'000 (siehe Wegleitung) 406»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0008.md) `sg-form-4-2025__c0008` – «Total der Berufskosten 488»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0008.md) `sg-form-4-2025__c0008` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 10.2»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0002.md) `sg-form-32-2025__c0002` – «Fahrkosten zwischen Wohn- und Arbeitsort max. Fr. 8‘000 max. Fr. 3‘300»
  - [WL SG 2025 S. 49](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0173.md) `sg-wl-2025__c0173` – «erforderlichen Anpassungen durch die Steuerbehörde automatisch»
  - [StB 39 Nr. 3 S. 3–4](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0011.md) `sg-stb-39-3__c0011` – «Die Begrenzung gilt, sofern eine (unselbständige) Haupt- und Nebenerwerbstätigkeit vorliegt, insgesamt»

<a id="lohnausweis-feld-f-abzug-berufskosten-fahrkosten"></a>
### Ziff. Lohnausweis Feld F – Lohnausweis Feld F: unentgeltliche Beförderung zwischen Wohn- und Arbeitsort

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld F (Kästchen angekreuzt)
- **Rein:** Lohnausweis → Feld F angekreuzt (Sammeltransport, AG-GA aus geschäftlichen Gründen) · Lohnausweis → Ziff. 2.2 Privatanteil Geschäftsfahrzeug (Gehaltsnebenleistung) · Lohnausweis → Ziff. 2.3 Fahrkostenentschädigung im Bruttolohn (dann kein Kreuz in Feld F)
- **Rechnen:** Feld F angekreuzt oder Geschäftsauto mit Privatanteil 0,9%/Mt. → kein Fahrkostenabzug (Form. 4 Ziff. 1); Entschädigung LA 2.3 → Abzug bis Kanton 8'000 / Bund 3'300
- **Regel:** Feld F angekreuzt = dem Arbeitnehmer erwachsen keine Kosten (Sammeltransport, vom Arbeitgeber getragenes GA aus geschäftlichen Gründen): kein Fahrkostenabzug in Formular 4 Ziff. 1. Hinweis: das Lohnausweis-Merkblatt in den Wiki-Quellen (bund-wl-lohnausweis-2026) gilt nur für 2026; Regel hier nach WL SG 2025.
- **Beachten:** AG-GA ohne geschäftliche Notwendigkeit: Feld F leer, Vorteil im Lohn; Streckenabo-Kosten in Form. 4 abziehbar
- **Beachten:** Bordbuch statt Privatanteil-Pauschale: effektive Arbeitswegkosten bis Maximalabzug abziehbar
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 8'000 (Fahrkosten Wohn-/Arbeitsstätte: Maximalabzug Fr. 8'000 pro Person (Maximalabzug, keine Pauschale; bei Teilzeit/unterjährig nicht gekürzt; gilt bei Haupt- und Nebenerwerb insgesamt). Bei direkter Bundessteuer tiefer (Fr. 3'300, siehe data/werte/bund).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Quellen:**
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0075.md) `sg-wl-2025__c0075` – «Ein Abzug für die Fahrt zur Arbeit ist deshalb nicht möglich»
  - [StB 39 Nr. 3 S. 4](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0013.md) `sg-stb-39-3__c0013` – «In diesem Fall ist kein Kreuz im Feld F»
  - [StB 39 Nr. 3 S. 4](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0013.md) `sg-stb-39-3__c0013` – «ist diese Entschädigung in Ziff. 2.3 des Lohnausweises zu deklarieren»
  - [StB 39 Nr. 3 S. 4–5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0014.md) `sg-stb-39-3__c0014` – «weshalb auf dem Lohnausweis das Feld F nicht anzukreuzen ist»
  - [StB 39 Nr. 3 S. 5](../../chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0015.md) `sg-stb-39-3__c0015` – «unter Ziff. 2.2 des Lohnausweises»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0076.md) `sg-wl-2025__c0076` – «Monat 0,9% des Fahrzeugkaufpreises (exkl. Mehrwertsteuer)»
  - [WL SG 2025 S. 23](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0076.md) `sg-wl-2025__c0076` – «können die effektiven Kosten»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0002.md) `sg-form-32-2025__c0002` – «Fahrkosten zwischen Wohn- und Arbeitsort max. Fr. 8‘000 max. Fr. 3‘300»

<a id="lohnausweis-ziff-15-abzug-berufskosten-verpflegung"></a>
### Ziff. Lohnausweis Ziff. 15 – Lohnausweis Ziff. 15 Bemerkungen: Anzahl Schichttage; «Einer von xx Lohnausweisen»

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 (Bemerkungen)
- **Rein:** Lohnausweis Ziff. 15 Bemerkungen → Anzahl Schichttage (→ Form. 4 Ziff. 2.3) · Lohnausweis Ziff. 15 → Vermerk «Einer von xx Lohnausweisen» (alle LA des Arbeitgebers beiziehen)
- **Rechnen:** Schichtabzug = min(Schichttage × 15; 3'200) → Code 412 (P1) / 462 (P2); Vermerk «Einer von xx»: alle LA des AG einreichen, Nettolöhne zusammenzählen
- **Regel:** Schichtarbeit: Anzahl Schichttage hier bescheinigt (Grundlage für Fr. 15 pro Tag, Formular 4 Ziff. 2.3). Mehrere Lohnausweise des gleichen Arbeitgebers: Vermerk «Einer von xx Lohnausweisen».
- **Beachten:** Fehlt der Vermerk: Schichttage mit separatem AG-Schreiben bescheinigen lassen
- **Beachten:** Einkünfte mit Lohnausweisen lückenlos belegen; grundsätzlich ein LA pro Arbeitgeber
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Schicht-/Nachtarbeit mit durchgehender, mindestens achtstündiger Tätigkeit: Fr. 15 pro Schichttag, bei ganzjähriger Schichtarbeit Fr. 3'200. Nicht kumulierbar mit Abzug für auswärtige Verpflegung; Schichttage vom Arbeitgeber zu bescheinigen.)** · Bund **CHF 15 (Durchgehende Schicht-/Nachtarbeit (gestaffelte Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich): CHF 15 pro ausgewiesenem Tag, bei ganzjähriger Schicht-/Nachtarbeit CHF 3'200 pro Jahr)**
- **Quellen:**
  - [WL SG 2025 S. 24](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0079.md) `sg-wl-2025__c0079` – «Ziffer 15 im Lohnausweis»
  - [WL SG 2025 S. 14](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0039.md) `sg-wl-2025__c0039` – «Ziffer 15 des Lohnaus»
  - [Formular 4 SG 2025 S. 2](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0007.md) `sg-form-4-2025__c0007` – «Pro ausgewiesenen Schichttag Fr. 15 / im Jahr Fr. 3'200 462»
  - [Formular 4 SG 2025 S. 1](../../chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md) `sg-form-4-2025__c0003` – «Pro ausgewiesenen Schichttag Fr. 15 / im Jahr Fr. 3'200 412»
  - [WL SG 2025 S. 14](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0039.md) `sg-wl-2025__c0039` – «grundsätzlich ein Lohnaus- weis einzureichen»

## Hilfsblatt Schulden

<a id="form-5-teil-a-schulden-privat"></a>
### Ziff. Form. 5 Teil A – Private Schulden und private Schuldzinsen (→ Ziff. 34.1 und 11)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung) → Schuldenausweis Gläubiger: Schuld am 31.12.2025 und Schuldzinsen 2025
- **Rein:** Bank-/Hypothekarauszug per 31. Dezember 2025 → Schuld je Gläubiger · Zinsausweis/Jahresabrechnung 2025 → bezahlte Schuldzinsen · Darlehensvertrag/Bestätigung Privatdarlehen → Schuld und Zins
- **Rechnen:** Σ Schulden 31. Dezember 2025 → Ziff. 34.1 (Code 504); Σ Zinsen 2025 → Ziff. 11 (Code 500), max. Ertrag Ziff. 4 (ohne Lotteriegewinne) + Ziff. 5 + 50'000
- **Regel:** Pro Gläubiger Name/Adresse, Schuld per 31.12.2025 und bezahlte Schuldzinsen 2025; Totale nach Ziff. 34.1 (Schuld) und Ziff. 11 (Zinsen). Belege auf Verlangen.
- **Beachten:** Nicht abziehbar: Amortisationen, Baukreditzinsen, Baurechtszinsen Eigenheim, Leasing privat
- **Beachten:** Solidar-/Bürgschaftsschulden und deren Zinsen nur im selbst getragenen Anteil (interne Quote, Nachweis)
- **Beachten:** Bund: private Zinsen bis Bruttovermögensertrag + 50'000; Geschäftsschulden/-zinsen nicht hier (Teil B/Jahresrechnung)
- **Quellen:**
  - [Formular 5 SG 2025 S. 1](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0001.md) `sg-form-5-2025__c0001` – «Total private Schulden und private Schuldzinsen»
  - [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0083.md) `sg-wl-2025__c0083` – «und der Einkünfte aus Liegenschaften gemäss Ziffer 5 zuzüglich Fr. 50’000»
  - [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0083.md) `sg-wl-2025__c0083` – «Schuldzinsen, die als Anlagekosten gelten (namentlich Baukreditzinsen)»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0117.md) `sg-wl-2025__c0117` – «andere Schulden, wie Solidar- und Bürgschaftsschulden, nur insoweit, als diese selbst getragen werden müssen»
  - [StB 34 Nr. 2 S. 3](../../chunks/sg/dauernd/sg-stb-34-2/sg-stb-34-2__c0009.md) `sg-stb-34-2__c0009` – «die auf den nach der internen Quote von ihm zu tragenden Anteil an der Gesamtschuld»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0008.md) `sg-form-1-2025__c0008` – «Schuldzinsen Formular 5 500»
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «34.1 Privatschulden Formular 5 504»
  - [KS 36 S. 7–8](../../chunks/bund/dauernd/bund-ks-36/bund-ks-36__c0023.md) `bund-ks-36__c0023` – «die privaten Schuldzinsen nur bis zur Höhe des Bruttovermögensertrags und weiterer 50'000 Franken abziehbar»

<a id="form-5-teil-b-schulden-privat"></a>
### Ziff. Form. 5 Teil B – Geschäftsschulden (→ Ziff. 34.2)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz: Schuld am 31.12. bzw. Bilanzstichtag
- **Rein:** Schlussbilanz/Jahresrechnung → Geschäftsschulden per 31. Dezember 2025 bzw. Bilanzstichtag (Gläubiger)
- **Rechnen:** Σ Geschäftsschulden gem. Bilanz → Ziff. 34.2 (Code 506); Geschäftszinsen bleiben in der Jahresrechnung
- **Regel:** Nur Schuldbetrag; Geschäftszinsen sind in der Jahresrechnung enthalten und hier nicht aufzuführen.
- **Beachten:** Geschäftliche Schuldzinsen weder in Formular 5 noch in Ziff. 11
- **Beachten:** Solidar-/Bürgschaftsschulden nur im selbst getragenen Anteil
- **Quellen:**
  - [Formular 5 SG 2025 S. 1](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0002.md) `sg-form-5-2025__c0002` – «sind in der Jahresrechnung enthalten und deshalb hier nicht aufzuführen»
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0013.md) `sg-form-1-2025__c0013` – «34.2 Geschäftsschulden Formular 5 506»
  - [WL SG 2025 S. 25](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0083.md) `sg-wl-2025__c0083` – «sind in der Jahresrechnung enthalten und deshalb nicht im Formular 5 aufzuführen»
  - [WL SG 2025 S. 34](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0117.md) `sg-wl-2025__c0117` – «andere Schulden, wie Solidar- und Bürgschaftsschulden, nur insoweit, als diese selbst getragen werden müssen»

## Hilfsblatt Zuwendungen

<a id="form-5-r-ckseite-teil-a-abzug-spenden"></a>
### Ziff. Form. 5 Rückseite Teil A – Freiwillige Zuwendungen (→ Ziff. 21.3)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigung: Datum, Institution, Betrag
- **Rein:** Spendenbestätigung der Institution → Datum, Name/Adresse, Betrag 2025 · Übertrag Nettoeinkommen Ziff. 20 → Obergrenze
- **Rechnen:** Ziff. 21.3 (Code 244) = min(Σ Zuwendungen 2025; 20% × Nettoeinkommen Ziff. 20), nur wenn Σ ≥ 100; Kanton = Bund
- **Regel:** Institution mit Name/Adresse, Datum, Betrag 2025; Total nach Ziff. 21.3 (mind. Fr. 100, max. 20% des Nettoeinkommens).
- **Beachten:** Nur an steuerbefreite jur. Personen mit Sitz in der Schweiz (öffentlich/gemeinnützig); Kultuszwecke nicht abziehbar
- **Beachten:** Völlig uneigennützig: kein direkter oder indirekter Nutzen für den Spender
- **Beachten:** Parteispenden nicht hier, sondern separat in Teil B
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): Abzug, wenn im Steuerjahr gesamthaft mindestens Fr. 100. Kultuszwecke nicht abziehbar.)** · Bund **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen (CH) bzw. Gemeinwesen: mindestens CHF 100 im Steuerjahr)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: insgesamt höchstens 20 % der Nettoeinkünfte (Nettoeinkommen).)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Quellen:**
  - [Formular 5 SG 2025 S. 2](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0003.md) `sg-form-5-2025__c0003` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.3»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0102.md) `sg-wl-2025__c0102` – «insgesamt höchstens aber 20% des Nettoeinkommens gemäss Ziffer 20»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «21.3 Freiwillige Zuwendungen (wenn mind. Fr.100, max. 20% Ziffer 20) Formular 5 244»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0102.md) `sg-wl-2025__c0102` – «Zuwen- dungen für Kultuszwecke sind nicht abziehbar»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0102.md) `sg-wl-2025__c0102` – «der Leistende darf aus der Tätigkeit der bedachten Institution weder direkt noch indirekt einen Nutzen ziehen»

<a id="form-5-r-ckseite-teil-b-abzug-parteispenden"></a>
### Ziff. Form. 5 Rückseite Teil B – Parteispenden (→ Ziff. 16.3)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Bestätigung der Partei: Datum, Partei, Betrag
- **Rein:** Bestätigung/Quittung der Partei → Datum, Partei, Betrag 2025 (Mitglieder-, Gesinnungsbeiträge, Spenden, Mandatssteuern)
- **Rechnen:** Kanton: min(Σ; 10'700 allein / 21'400 Ehepaar, eingetr. Partnerschaft) / Bund: min(Σ; 10'600) → Ziff. 16.3 (Code 555)
- **Regel:** Pro Partei Datum und Betrag 2025; Total nach Ziff. 16.3 (max. Fr. 10'700 / Fr. 21'400).
- **Beachten:** Partei im Parteienregister, in einem kant. Parlament vertreten oder ≥ 3% Stimmen bei letzten kant. Parlamentswahlen
- **Beachten:** Bund-Abweichung (10'600) nimmt das Steueramt automatisch vor
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'700 (Mitgliederbeiträge und Zuwendungen an politische Parteien: höchstens Fr. 10'700 für Alleinstehende/übrige Steuerpflichtige (Partei im Parteienregister, in kantonalem Parlament vertreten oder mind. 3 % Stimmen).)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 21'400 (Parteispenden: höchstens Fr. 21'400 für gemeinsam steuerpflichtige Ehegatten/eingetragene Partner.)** · Bund **n/a – Bund kennt nur einen Gesamtbetrag von CHF 10'600 (Art. 33 Abs. 1 lit. i DBG); keine Verdoppelung für Ehepaare in der Quelle.**
- **Quellen:**
  - [Formular 5 SG 2025 S. 2](../../chunks/sg/2025/sg-form-5-2025/sg-form-5-2025__c0004.md) `sg-form-5-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 16.3»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0093.md) `sg-wl-2025__c0093` – «Parteispenden können maximal in der Höhe von Fr. 10’700»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0004.md) `sg-form-32-2025__c0004` – «Parteispenden max. Fr. 10'600»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «16.3 Parteispenden Formular 5 555»
  - [WL SG 2025 S. 49](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0173.md) `sg-wl-2025__c0173` – «erforderlichen Anpassungen durch die Steuerbehörde automatisch»
  - [WL SG 2025 S. 28](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0093.md) `sg-wl-2025__c0093` – «mindes- tens 3 Prozent der Stimmen erreicht hat»

## Hilfsblatt Versicherungsprämien

<a id="form-6-teil-a-abzug-versicherungspraemien"></a>
### Ziff. Form. 6 Teil A – Bezahlte Versicherungsprämien und Sparzinsen: a. Krankenversicherung brutto, b. Unfallversicherung (ohne NBU), c. Lebens-/Rentenversicherungen, d. Sparzinsen, e. abzüglich Prämienverbilligungen

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Prämienrechnung/Jahresabrechnung Krankenkasse (brutto), Bescheinigung Prämienverbilligung, Zinsen gemäss Formular 2
- **Rein:** Prämienabrechnung Krankenkasse → Bruttoprämien (a) · Prämienrechnungen private Unfall- (ohne NBU), Lebens-/Rentenversicherung → bezahlte Prämien (b, c) · Formular 2 (Wertschriftenverzeichnis) → Sparzinsen (d) · Verfügung/Abrechnung Prämienverbilligung (IPV) → Abzug (e)
- **Rechnen:** A = a + b + c + d − e (bezahlte Beträge 2025 der ganzen Familie); Abzug = min(A; B) gem. Teil B/C
- **Regel:** Tatsächlich bezahlte Prämien; Familien tragen Prämien der ganzen Familie ein. Prämienverbilligungen (IPV) für Steuerpflichtigen und Kinder abziehen. Total (A) wird mit Maximalabzug (B) verglichen.
- **Beachten:** Nicht abziehbar: Mobiliar-, Motorfahrzeug-, Haftpflicht- und andere Sachversicherungen
- **Beachten:** NBU nicht hier: bereits im Nettolohn abgezogen
- **Beachten:** IPV für Steuerpflichtige und unterhaltene Kinder anrechnen
- **Quellen:**
  - [Formular 6 SG 2025 S. 1](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0001.md) `sg-form-6-2025__c0001` – «a. Private Krankenversicherung (brutto)»
  - [Formular 6 SG 2025 S. 1](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0001.md) `sg-form-6-2025__c0001` – «e. abzüglich Prämienverbilligungen»
  - [WL SG 2025 S. 27](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0088.md) `sg-wl-2025__c0088` – «Mobiliar-, Motorfahrzeug- und Haftpflichtversiche»
  - [WL SG 2025 S. 27](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0088.md) `sg-wl-2025__c0088` – «rungen sowie für andere Sachversicherungen»
  - [WL SG 2025 S. 15](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0042.md) `sg-wl-2025__c0042` – «obligatorische Sozialversicherungsbeiträge [AHV, IV, EO, ALV, NBUV]»
  - [WL SG 2025 S. 27](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0087.md) `sg-wl-2025__c0087` – «den Steuerpflichtigen und für die von ihm unterhaltenen Kinder ausbezahlt»

<a id="form-6-teil-b-c-abzug-versicherungspraemien"></a>
### Ziff. Form. 6 Teil B/C – Maximaler Abzug (Fr. 6'800 / Fr. 3'400, Zuschläge) und zulässiger Abzug (→ Ziff. 14)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenblatt
- **Rein:** Übertrag Total (A) aus Teil A · Zivilstand + Kinder mit Kinderabzug Ziff. 23.1/23.2 → Zuschläge
- **Rechnen:** Kanton: 6'800 gemeinsam / 3'400 allein (+1'100 / +500 ohne 2. Säule+3a) + 1'100 je Kind; Bund: 3'700 / 1'800 (+1'850 / +900) + 700 je Kind; Code 600 = min(A; B)
- **Regel:** Gemeinsam Fr. 6'800 (+ Fr. 1'100 ohne BVG/3a bei beiden), alleinstehend Fr. 3'400 (+ Fr. 500), + Fr. 1'100 pro Kind mit Kinderabzug nach Ziff. 23.1/23.2. Abzug = niedrigerer Betrag von A und B.
- **Beachten:** Zuschlag ohne Vorsorgebeiträge bei Ehepaaren nur, wenn bei beiden erfüllt
- **Beachten:** Bund: Kinderzuschlag auch für unterstützungsbedürftige Personen
- **Beachten:** Bund-Werte setzt das Steueramt automatisch um (eine Deklaration)
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 6'800 (Versicherungsprämien und Sparzinsen: Gesamtbetrag Fr. 6'800 für gemeinsam steuerpflichtige Ehegatten (Kranken-, Unfall-, Lebens-/Rentenversicherung, Zinsen von Sparkapitalien; Prämienverbilligungen sind anzurechnen).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 3'400 (Versicherungsprämien und Sparzinsen: Gesamtbetrag Fr. 3'400 für übrige Steuerpflichtige.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 7'900 (Gemeinsam Steuerpflichtige ohne Abzug von Beiträgen an 2. Säule/Säule 3a: Maximalabzug erhöht sich um Fr. 1'100 (6'800 + 1'100 = 7'900). Bei Verheirateten müssen die Voraussetzungen bei beiden Partnern erfüllt sein.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an Säule 2/3a (Erhöhung um die Hälfte))**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 3'900 (Übrige Steuerpflichtige ohne Abzug von Beiträgen an 2. Säule/Säule 3a: Erhöhung um Fr. 500 (3'400 + 500 = 3'900).)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'100 (Zuschlag Fr. 1'100 für jedes Kind, für das ein Kinderabzug geltend gemacht werden kann (Gesetz); WL: bis Fr. 1'100.)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
- **Quellen:**
  - [Formular 6 SG 2025 S. 1](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0002.md) `sg-form-6-2025__c0002` – «Der niedrigere Betrag von (A) und (B)»
  - [Formular 6 SG 2025 S. 1](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0002.md) `sg-form-6-2025__c0002` – «Fr. 1’100 zusätzlich für jedes Kind»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0003.md) `sg-form-32-2025__c0003` – «Verheiratete max. Fr. 6'800 max. Fr. 3'700»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0003.md) `sg-form-32-2025__c0003` – «Alleinstehende max. Fr. 3'400 max. Fr. 1'800»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0003.md) `sg-form-32-2025__c0003` – «terstützungsbedürftige Person), zusätzlich bis Fr. 1'100 bis Fr. 700»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «14. Versicherungsprämien und Sparzinsen Formular 6 600»
  - [WL SG 2025 S. 49](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0173.md) `sg-wl-2025__c0173` – «erforderlichen Anpassungen durch die Steuerbehörde automatisch»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0003.md) `sg-form-32-2025__c0003` – «gebundene Selbstvorsorge (Säule 3a), zusätzlich bis Fr. 1'100 bis Fr. 1'850»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0003.md) `sg-form-32-2025__c0003` – «gebundene Selbstvorsorge, zusätzlich bis Fr. 500 bis Fr. 900»

## Hilfsblatt Krankheitskosten

<a id="form-6-r-ckseite-krankheitskosten-abzug-krankheitskosten"></a>
### Ziff. Form. 6 Rückseite Krankheitskosten – Krankheits- und Unfallkosten: Rechnungsdatum, Arzt/Zahnarzt/Spital, Bruttobetrag, abzüglich Beiträge Dritter, selbst getragene Kosten (→ Ziff. 21.1 Vorkolonne)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Rechnungen und Leistungsabrechnung der Krankenkasse (Franchise/Selbstbehalt/Zahnarzt etc.)
- **Rein:** Arzt-/Zahnarzt-/Spital-/Therapierechnungen 2025 → Bruttobetrag · Leistungsabrechnung Krankenkasse/Versicherung, Hilflosenentschädigung → Beiträge Dritter (abziehen) · Ärztliches Zeugnis → Medikamente/Heilmittel, Diät (Pauschale Zöliakie 2'500)
- **Rechnen:** Σ (Brutto − Beiträge Dritter) → Ziff. 21.1 Vorkolonne (Code 650); Abzug (Code 240) = Σ − Selbstbehalt Kanton 2% / Bund 5% × Nettoeinkommen Ziff. 20, falls positiv
- **Regel:** Nur tatsächlich selbst getragene Kosten (Beiträge Dritter wie Versicherungen, Krankenkassen, Hilflosenentschädigung abziehen). Bei Verweis auf Kassenauszug zwingend Aufstellung mit Details (inkl. Leistungsübersicht) einreichen. Krankenkassenprämien gehören NICHT hierher (Ziff. 14).
- **Beachten:** Bei Verweis auf Kassenauszug: Detailaufstellung inkl. Leistungsübersicht zwingend beilegen
- **Beachten:** Diät-Pauschale 2'500 statt effektiv (z.B. Zöliakie, nicht Diabetes); erstmals ärztliche Bescheinigung
- **Beachten:** Prämien nicht hier (Teil A); behinderungsbedingte Kosten separat ohne Selbstbehalt
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **2 % (Krankheits-/Unfallkosten abziehbar, soweit sie 2 % der Nettoeinkünfte (Nettoeinkommen Ziff. 20) übersteigen. Behinderungsbedingte Kosten ohne Selbstbehalt. Pauschale Diät (Zöliakie) Fr. 2'500.)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Quellen:**
  - [Formular 6 SG 2025 S. 2](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0003.md) `sg-form-6-2025__c0003` – «Abzugsfähig sind die tatsächlich selbst getragenen Kosten»
  - [Formular 32 SG 2025 S. 1](../../chunks/sg/2025/sg-form-32-2025/sg-form-32-2025__c0005.md) `sg-form-32-2025__c0005` – «Selbstbehalt 2% der Selbstbehalt 5% der»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «21.1 Krankheits- und Unfallkosten Formular 6 650»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0098.md) `sg-wl-2025__c0098` – «nicht jedoch bei Diabetes) eine Pauschale von Fr. 2’500 in Abzug gebracht werden»
  - [WL SG 2025 S. 29](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0098.md) `sg-wl-2025__c0098` – «2% des Nettoeinkommens gemäss Ziffer 20 übersteigen»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «abzüglich Selbstbehalt 2% des Nettoeinkommens (Ziffer 20)»

<a id="form-6-r-ckseite-behinderungskosten-abzug-behinderungskosten"></a>
### Ziff. Form. 6 Rückseite Behinderungskosten – Behinderungsbedingte Kosten (→ Ziff. 21.2)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Rechnungen, Verfügung Hilflosenentschädigung, Heimabrechnung
- **Rein:** Heim-/Pflege-/Betreuungsrechnungen → selbst getragene Kosten · Verfügung Hilflosenentschädigung (HE) → Grad für Pauschale bzw. als Beitrag Dritter abziehen · Ärztlicher Fragebogen → Pauschale Gehörlose/Dialyse (erstmalig)
- **Rechnen:** Σ selbst getragene Kosten − Dritte (Heim: − 2'000 × Monate) oder Pauschale HE leicht/mittel/schwer 2'500/5'000/7'500 bzw. Gehörlose/Dialyse 2'500 → Code 235
- **Regel:** Total nach Ziff. 21.2, ohne Selbstbehalt; Details siehe Ziff. 21.2.
- **Beachten:** Heim nur ab Pflegestufe 4 bzw. 21 BESA-Punkten; Altersheim ohne Pflege = Lebenshaltung
- **Beachten:** Pauschale HE: Verfügung einreichen; Schwerhörige nur effektive Kosten
- **Beachten:** Kumulation HE- und Gehörlosen-/Dialyse-Pauschale nur nach Einzelfallabklärung
- **Quellen:**
  - [Formular 6 SG 2025 S. 2](../../chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0004.md) `sg-form-6-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.2»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0099.md) `sg-wl-2025__c0099` – «Fr. 2’000 pro Monat als nicht abzugsberechtigte Lebenshaltungskosten»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0099.md) `sg-wl-2025__c0099` – «Pflegebedürftigkeit ab Pflegestufe 4 oder 21 BESA-Punkten»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0100.md) `sg-wl-2025__c0100` – «Bezüger einer Hilflosenentschädigung mittleren Grades: Fr. 5’000»
  - [WL SG 2025 S. 30](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0101.md) `sg-wl-2025__c0101` – «Gehörlose (gilt nicht für Schwerhörige; diese können nur die effektiven Kosten»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md) `sg-form-1-2025__c0010` – «21.2 Behinderungsbedingte Kosten (ohne Selbstbehalt) Formular 6 235»

## Hilfsblatt Liegenschaften

<a id="form-7-abschnitt-a-vermoegen-liegenschaften"></a>
### Ziff. Form. 7 Abschnitt A – Angaben zur Liegenschaft / Steuerwert (→ Ziff. 31)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Steuerliche Schätzung: Grundstücknummer, Steuerwert; Anteil Person 1/2 in %, Nutzungsart
- **Rein:** Steueramtliche Schätzung (Verkehrs-/Ertragswert) → Grundstück-Nr., Steuerwert · Grundbuchauszug → Anteile P1/P2 in %; Kauf-/Schenkungs-/Erbvertrag → Datum Zugang/Wegfall 2025 · Schätzung Lagekanton → Steuerwert ausserkantonal; Ausland: mutmasslicher Verkehrswert · Bauabrechnung Neu-/Anbau ohne neue Schätzung → Zuschlag zum Steuerwert
- **Rechnen:** Steuerwert lt. rechtskräftiger Schätzung (Neu-/Anbau ohne Schätzung: + 80% der Neu-/Anbaukosten; Ertragswert + 40%) → Ziff. 31 (Code 710) bzw. Form. 7Z
- **Regel:** Ein Formular pro Liegenschaft; Zugang/Wegfall im Jahr 2025 mit Datum und Grund (Kauf, Verkauf, Schenkung, Erbschaft) angeben. Bei mehr als einer Liegenschaft Übertrag in Formular 7Z.
- **Beachten:** Ein Formular je Liegenschaft; bei mehreren Totale in Form. 7Z übertragen
- **Beachten:** Steuerwert wird vom Gemeindesteueramt eröffnet
- **Beachten:** Nur Kanton/Gemeinde: direkte Bundessteuer kennt keine Vermögenssteuer
- **Quellen:**
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0001.md) `sg-form-7-2025__c0001` – «Pro Liegenschaft ist ein separates Formular zu verwenden»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0154.md) `sg-wl-2025__c0154` – «Im Weiteren sind die Anteile von Person 1 und Person 2 in Prozenten anzugeben»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0155.md) `sg-wl-2025__c0155` – «im Ausmass von 80% der Neu- oder Anbaukosten»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0155.md) `sg-wl-2025__c0155` – «beträgt der Zuschlag 40% der Neu- oder Anbaukosten»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0155.md) `sg-wl-2025__c0155` – «Der massgebliche Steuerwert wird vom Gemeindesteueramt eröffnet»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0155.md) `sg-wl-2025__c0155` – «Kantonen gelegene Grundstücke sind mit dem entsprechenden Steuerwert»
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «31. Liegenschaften Formular 7 710»
  - [WL SG 2025 S. 43](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0152.md) `sg-wl-2025__c0152` – «Pro Liegenschaft ist je ein Formular 7 auszufüllen. Die ermittelten Totale sind zu»
  - [WL SG 2025 S. 49](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0173.md) `sg-wl-2025__c0173` – «direkten Bundessteuer 2025, welche jedoch keine Vermögenssteuer»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0002.md) `sg-form-7-2025__c0002` – «Zugang, bzw. Wegfall der Liegenschaft im Jahr 2025»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0002.md) `sg-form-7-2025__c0002` – «Übertrag in Formular 7 Z»

<a id="form-7-abschnitt-b-a-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 7 Abschnitt B.a – Eigenmietwert (abzüglich 30%, Unternutzungs-/Härtefallabzug)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Schätzungsverfügung: Mietwert
- **Rein:** Schätzungsverfügung (Verkehrs-/Ertragswertschätzung) → Mietwert · Nachweis dauernd leerer Zimmer → Unternutzungsabzug (Antrag) · Kauf-/Verkaufsvertrag → Datum für anteiligen Mietwert
- **Rechnen:** Erstwohnung: EMW − 30% − Unternutzung [(EMW − 30%) × nicht benutzte Zimmer / (Zimmer + 2)]; übrige Objekte voller EMW; Teiljahr anteilig → Ziff. 5 (Code 712)
- **Regel:** Eigenmietwert der am Wohnort dauernd selbstbewohnten Liegenschaft (Erstwohnung) um 30% herabgesetzt; übrige Objekte voller Mietwert. Unternutzungsabzug = (reduzierter EMW × nicht benutzte Zimmer) / (Zimmerzahl + 2), nur bei dauernder, überprüfbarer Nichtbenützung (leer, unmöbliert). Härtefallabzug von Amtes wegen für AHV-Rentner (max. 10% des Brutto-EMW), nicht bei steuerbarem Vermögen über Fr. 600'000. Teiljahr: anteilig.
- **Beachten:** Härtefall (AHV-Alter) v.A.w.: steuerbarer EMW > 30% Bruttoeinkünfte; max. 10% Brutto-EMW; nicht bei Vermögen > 600'000
- **Beachten:** Unternutzung nur auf Antrag: Räume dauernd leer/unmöbliert (kein Gäste-/Stauraum), Nachweis beilegen
- **Beachten:** Miteigentum: EMW nach Grundbuchquote; Zweit-/Ferienwohnung und vermietete Objekte ohne 30%-Reduktion
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **30 % (Eigenmietwert des am Wohnsitz dauernd selbst bewohnten Eigenheims wird um 30 % herabgesetzt; Unternutzung auf Antrag; Reduktion für Personen im AHV-Alter bei offensichtlichem Missverhältnis (Härtefall Art. 14 StV: Mietwert über 30 % der Bruttoeinkünfte und Vermögen höchstens Fr. 600'000).)** · Bund **n/a – Eigenmietwert wird nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt (Art. 21 Abs. 2 DBG); Abschaffung per 01.01.2029 beschlossen, 2025–2028 gilt bisheriges Recht. Der Eigenmietwert für die direkte Bundessteuer wird im kantonalen Veranlagungsverfahren festgesetzt; ein dort vorgesehener Abzug für die DBSt (z.B. TG 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Quellen:**
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0003.md) `sg-form-7-2025__c0003` – «Eigenmietwert abzüglich 30%»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0156.md) `sg-wl-2025__c0156` – «Der Eigenmietwert des am Wohnsitz dauernd selbstbewohnten Eigenhei-»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0158.md) `sg-wl-2025__c0158` – «Übersteigt das steuerbare Vermögen Fr. 600’000»
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «Ertrag aus Liegenschaften Formular 7 712»
  - [StB 34 Nr. 1 S. 3–4](../../chunks/sg/dauernd/sg-stb-34-1/sg-stb-34-1__c0011.md) `sg-stb-34-1__c0011` – «wird jedoch nur auf Antrag der steuerpflichtigen Person berücksichtigt»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0157.md) `sg-wl-2025__c0157` – «muss tatsächlich leer, d.h. unmöbliert sein»
  - [StB 34 Nr. 2 S. 2](../../chunks/sg/dauernd/sg-stb-34-2/sg-stb-34-2__c0005.md) `sg-stb-34-2__c0005` – «Massgebend ist die sachenrechtliche Quote gemäss Grundbucheintrag»
  - [StB 34 Nr. 1 S. 2–3](../../chunks/sg/dauernd/sg-stb-34-1/sg-stb-34-1__c0008.md) `sg-stb-34-1__c0008` – «Ferienwohnungen sowie von vermieteten Objekten»

<a id="form-7-abschnitt-b-b-einkommen-liegenschaften-mietertrag"></a>
### Ziff. Form. 7 Abschnitt B.b – Erträge Fremdnutzung und Leistungen Dritter (Miet-/Pachtzinsen, Geschäftsräume, abzüglich Nebenkosten)

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Mietzinsabrechnung/Liegenschaftenrechnung
- **Rein:** Mietverträge/Mietzinsabrechnung → Miet-/Pachtzinsen ohne Nebenkosten (inkl. Mietzinsreduktion Hauswart) · Nebenkostenabrechnung → tatsächliche NK abziehen, wenn im Mietzins inbegriffen · Belege Zinszuschüsse, Subventionen, Versicherungsleistungen → Leistungen Dritter · Liegenschaftenrechnung (falls geführt) → Total direkt einsetzen, beilegen
- **Rechnen:** Σ Miet-/Pachtzinsen − inbegriffene NK (effektiv) + Leistungen Dritter; möbliert − 20% Einschlag → Total a. + b. → Ziff. 5 (Code 712) bzw. Form. 7Z (B)
- **Regel:** Miet-/Pachtzinsen ohne Nebenkosten (vertraglich inbegriffene Nebenkosten mit tatsächlichen Auslagen abziehen); inkl. Mietzinsreduktion Hauswart; Leistungen Dritter (Zinszuschüsse, Subventionen, Versicherungsleistungen). Möblierte Wohnung: i.d.R. 20% Einschlag. Überschüssiger PV-Strom nicht hier, sondern Ziff. 6.3.
- **Beachten:** Stromerzeugung über Eigenverbrauch (z.B. PV) nicht hier, sondern Ziff. 6.3
- **Beachten:** Miteigentum: Erträge nach Grundbuchquote
- **Beachten:** Formular 7M für die Aufstellung Fremdnutzung verfügbar
- **Quellen:**
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0003.md) `sg-form-7-2025__c0003` – «Total steuerbare Erträge Fremdnutzung und Leistungen Dritter»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0159.md) `sg-wl-2025__c0159` – «Zum steuerbaren Mietertrag gehören die Miet- und Pachtzinsen bei»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0160.md) `sg-wl-2025__c0160` – «Der Einschlag beträgt in der Regel 20%.»
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «Ertrag aus Liegenschaften Formular 7 712»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0160.md) `sg-wl-2025__c0160` – «Wird für die Liegenschaft eine separate Liegenschaftenrechnung geführt»
  - [StB 34 Nr. 2 S. 2](../../chunks/sg/dauernd/sg-stb-34-2/sg-stb-34-2__c0005.md) `sg-stb-34-2__c0005` – «Massgebend ist die sachenrechtliche Quote gemäss Grundbucheintrag»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0159.md) `sg-wl-2025__c0159` – «soweit diese den Eigenverbrauch übersteigen, sind unter Ziffer 6.3»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0003.md) `sg-form-7-2025__c0003` – «Übertrag in die Spalte (B) des Formulars 7 Z»

<a id="form-7-abschnitt-c-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 7 Abschnitt C – Unterhalts- und Verwaltungskosten: Pauschalabzug 20% der Erträge (B) oder tatsächliche Kosten (Rückseite, C2)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Rechnungen mit Datum 2025, Name Rechnungsteller, Beschreibung, Rechnungstotal netto, Anteil Anlagekosten (nicht abziehbar)
- **Rein:** Handwerker-/Unterhaltsrechnungen 2025 → Datum, Rechnungssteller, Betrag netto, Anteil Anlagekosten · Gebäudeversicherung, Grundsteuer, Wartungsverträge → Betriebskosten · STWEG-Abrechnung → Anteil Unterhalt/Verwaltung inkl. Erneuerungsfonds · Förderbeitrags-/Versicherungsabrechnung → Leistungen Dritter (abziehen)
- **Rechnen:** Kanton: 20% × Erträge (B) oder C2 = Σ netto − Anlagekosten − Leistungen Dritter → Ziff. 15 (Code 716) / Bund: 10% (Gebäude ≤ 10 J.) bzw. 20% × Bruttoertrag
- **Regel:** Pauschale nur für private Wohnliegenschaften; sonst tatsächliche Kosten (Instandhaltung, Instandstellung, Ersatzbeschaffung, Betriebs-/Verwaltungskosten, Denkmalpflege, Energiespar-/Umweltinvestitionen, Rückbaukosten Ersatzneubau). Abzüglich Versicherungsleistungen/Förderbeiträge. Wertvermehrende Anteile (Anlagekosten) nicht abziehbar. Übertrag nach Ziff. 15.
- **Beachten:** Wahl Pauschale/effektiv je Liegenschaft und Periode; Pauschale nur für vorwiegend Wohnzwecken dienende Liegenschaft
- **Beachten:** Nicht abziehbar: Anlagekosten, Kanalisations-/Perimeterbeiträge; bei Eigengebrauch Wasser, Strom, Heizung
- **Beachten:** Miteigentum: Kosten bzw. Pauschale nur im Umfang des Eigentumsanteils
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt/Verwaltung: 20 % des Bruttomietertrags ohne Nebenkosten bzw. des angerechneten Eigenmietwerts, nur für vorwiegend Wohnzwecken dienende Privatliegenschaften; Wahl pro Periode und Liegenschaft zwischen Pauschale und effektiven Kosten.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Gleicher Pauschalsatz 20 % unabhängig vom Gebäudealter (SG kennt keine Staffelung nach 10 Jahren).)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Quellen:**
  - [Formular 7 SG 2025 S. 2](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0005.md) `sg-form-7-2025__c0005` – «Abzugsfähig sind nur die selbst bezahlten Kosten»
  - [WL SG 2025 S. 45](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0161.md) `sg-wl-2025__c0161` – «Die Pauschale umfasst alle Aufwendungen inklusive Kosten denkmalpflegerischer Arbeiten»
  - [StV SG Art. 29](../../chunks/sg/2025/sg-stv/sg-stv__art-29.md) `sg-stv__art-29` – «für jede Liegenschaft zwischen dem Abzug der tatsächlichen Kosten und dem Pauschalabzug wählen»
  - [StB 34 Nr. 1 S. 6](../../chunks/sg/dauernd/sg-stb-34-1/sg-stb-34-1__c0020.md) `sg-stb-34-1__c0020` – «beträgt bei Eigenheimen 20% des angerechneten Eigenmietwertes»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «Unterhalts- und Verwaltungskosten für Liegenschaften Formular 7 716»
  - [WL SG 2025 S. 46](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0164.md) `sg-wl-2025__c0164` – «Baubeiträge an die Kanalisation und Gewässerschutzanlagen sowie Bauperimeter»
  - [WL SG 2025 S. 46](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0164.md) `sg-wl-2025__c0164` – «Nicht abziehbar sind die Kosten (inklusive Grundgebühren) für Wasser, Gas, Strom etc.»
  - [WL SG 2025 S. 47](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0169.md) `sg-wl-2025__c0169` – «die Einlagen in den Reparatur- und Erneuerungsfonds als Unterhalts»
  - [StB 34 Nr. 2 S. 3](../../chunks/sg/dauernd/sg-stb-34-2/sg-stb-34-2__c0008.md) `sg-stb-34-2__c0008` – «Er steht jedem Miteigentümer im Umfang seines Anteils an der»

<a id="form-7z-berechnung-total"></a>
### Ziff. Form. 7Z – Zusammenzug aller Liegenschaften: Steuerwert (A), Erträge (B), Pauschalabzug (C1), tatsächliche Kosten (C2)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Übertrag aus Formularen 7
- **Rein:** Formular 7 (je Liegenschaft, auch ausserkantonal/Ausland) → Teil A Steuerwert → Spalte (A) · Formular 7 → Teil B «Total Erträge a. und b.» (Eigenmietwert, Fremdnutzung) → Spalte (B) · Formular 7 → Teil C Pauschalabzug → (C1) bzw. Rückseite «Total Unterhalts- und Verwaltungskosten (C2)» → (C2)
- **Rechnen:** Je Spalte Σ Formulare 7 (+ Hertrag Ergänzungsblätter): Σ A → Ziff. 31 (Code 710); Σ B → Ziff. 5 (712); Σ C1 + Σ C2 → Ziff. 15 (716)
- **Regel:** Nur bei mehr als einer Liegenschaft. Totale nach Seite 4 Ziff. 31 (A), Seite 2 Ziff. 5 (B), Seite 3 Ziff. 15 (C1+C2).
- **Beachten:** Nur bei mehreren Liegenschaften (bei einer: Form. 7 direkt übertragen); Zeile = gewählte Liegenschaften-Nr.
- **Beachten:** Je Liegenschaft C1 oder C2; C1 = Kanton 20 % von B, nur vorwiegend Wohnzweck / Bund 10 % (Gebäude ≤ 10 J.) bzw. 20 %
- **Beachten:** A: am 31.12.2025 nicht mehr im Besitz → kein Übertrag; A nur Kanton; Bund-Abweichungen passt Steuerbehörde an
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt/Verwaltung: 20 % des Bruttomietertrags ohne Nebenkosten bzw. des angerechneten Eigenmietwerts, nur für vorwiegend Wohnzwecken dienende Privatliegenschaften; Wahl pro Periode und Liegenschaft zwischen Pauschale und effektiven Kosten.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Gleicher Pauschalsatz 20 % unabhängig vom Gebäudealter (SG kennt keine Staffelung nach 10 Jahren).)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Quellen:**
  - [Formular 7Z SG 2025 S. 1](../../chunks/sg/2025/sg-form-7z-2025/sg-form-7z-2025__c0001.md) `sg-form-7z-2025__c0001` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 31 Seite 2 Ziffer 5 Seite 3 Ziffer 15»
  - [WL SG 2025 S. 42](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0146.md) `sg-wl-2025__c0146` – «Bei Besitz einer einzigen Liegenschaft ist nur das Formular 7 auszufüllen.»
  - [WL SG 2025 S. 43](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0152.md) `sg-wl-2025__c0152` – «Pro Liegenschaft ist je ein Formular 7 auszufüllen. Die ermittelten Totale sind zu»
  - [WL SG 2025 S. 43](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0152.md) `sg-wl-2025__c0152` – «Der Eintrag hat auf jener Zeile zu erfolgen, die»
  - [WL SG 2025 S. 43](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0153.md) `sg-wl-2025__c0153` – «das Total der einzelnen Spalten zu ermitteln und in die jeweiligen Ziffern der»
  - [WL SG 2025 S. 43](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0153.md) `sg-wl-2025__c0153` – «Total 3'196'000 210'899 55'816»
  - [Formular 7Z SG 2025 S. 1](../../chunks/sg/2025/sg-form-7z-2025/sg-form-7z-2025__c0001.md) `sg-form-7z-2025__c0001` – «Hertrag von weiteren Ergänzungsblättern»
  - [Formular 7Z SG 2025 S. 1](../../chunks/sg/2025/sg-form-7z-2025/sg-form-7z-2025__c0001.md) `sg-form-7z-2025__c0001` – «Gemeinde und Kanton»
  - [WL SG 2025 S. 44](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0154.md) `sg-wl-2025__c0154` – «de, Kanton/Staat, Adresse) auch die Grundstück-Nummer anzugeben»
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «Vermögen im In- und Ausland»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0002.md) `sg-form-7-2025__c0002` – «Übertrag in Formular 7 Z»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0003.md) `sg-form-7-2025__c0003` – «Total Erträge a. und b.»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0003.md) `sg-form-7-2025__c0003` – «Übertrag in die Spalte (B) des Formulars 7 Z»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0004.md) `sg-form-7-2025__c0004` – «Pauschalabzug 20% der Erträge (B)»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0004.md) `sg-form-7-2025__c0004` – «Übertrag in die Spalte (C1) des Formulars 7 Z»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0004.md) `sg-form-7-2025__c0004` – «die ganz oder vorwiegend»
  - [Formular 7 SG 2025 S. 1](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0004.md) `sg-form-7-2025__c0004` – «Wohnzwecken dienen, geltend»
  - [Formular 7 SG 2025 S. 2](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0005.md) `sg-form-7-2025__c0005` – «kosten anstelle des Pauschalabzugs geltend gemacht werden.»
  - [Formular 7 SG 2025 S. 2](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0005.md) `sg-form-7-2025__c0005` – «Total Unterhalts- und Verwaltungskosten (C2)»
  - [Formular 7 SG 2025 S. 2](../../chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0005.md) `sg-form-7-2025__c0005` – «Übertrag in die Spalte (C2) des Formulars 7Z»
  - [WL SG 2025 S. 42](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0149.md) `sg-wl-2025__c0149` – «31. Dezember 2025 nicht»
  - [WL SG 2025 S. 42](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0149.md) `sg-wl-2025__c0149` – «mehr in Ihrem Besitz war. Es»
  - [WL SG 2025 S. 42](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0149.md) `sg-wl-2025__c0149` – «erfolgt jedoch kein Übertrag»
  - [WL SG 2025 S. 42](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0149.md) `sg-wl-2025__c0149` – «in das Formular 7 Z.»
  - [Formular 1 SG 2025 S. 4](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0012.md) `sg-form-1-2025__c0012` – «31. Liegenschaften Formular 7 710»
  - [Formular 1 SG 2025 S. 2](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) `sg-form-1-2025__c0006` – «5. Ertrag aus Liegenschaften Formular 7 712»
  - [Formular 1 SG 2025 S. 3](../../chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0009.md) `sg-form-1-2025__c0009` – «15. Unterhalts- und Verwaltungskosten für Liegenschaften Formular 7 716»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «mehr als zehn Jahre alt ist: 20 Prozent des Brutto-Mietertrags»
  - [WL SG 2025 S. 49](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0173.md) `sg-wl-2025__c0173` – «direkten Bundessteuer 2025, welche jedoch keine Vermögenssteuer für natür»
  - [WL SG 2025 S. 49](../../chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0173.md) `sg-wl-2025__c0173` – «gegenüber den Kantons- und Gemeindesteuern zu beachten sind, werden die erforderlichen Anpassungen durch die Steuerbehörde automatisch»
