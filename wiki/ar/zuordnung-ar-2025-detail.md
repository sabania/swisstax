---
typ: zuordnung-detail
titel: Zuordnung AR 2025 – Detail
jur: ar
jahre:
- 2025
generiert: tools/build_quick.py aus data/zuordnung/ar/2025.yaml (2026-11-09)
---

# AR 2025: Zuordnung Beleg → Ziffer – Detail

> Kompaktansicht: [quick/zuordnung-ar-2025.md](../../quick/zuordnung-ar-2025.md) · Formular: Steuererklärung 2025 Appenzell Ausserrhoden (Formular 1 Seiten 1-4, Hauptformular nicht online; Ziffern/Codes aus den Formular-Miniaturen der Wegleitung WL AR 2025) + Hilfsformulare 2 (Wertschriften), 4 (Berufskosten), 5 (Schulden, Zuwendungen, Parteispenden), 6 (Versicherungsprämien, Krankheits-/Behinderungskosten), 7/7Z (Liegenschaften), 10 (Kinderbetreuung) · Quelle der Wahrheit: `data/zuordnung/ar/2025.yaml`

## Personalien

<a id="seite-1-personalien"></a>
### Ziff. Seite 1 – Personalien, Berufs- und Familienverhältnisse, Dauer der Steuerpflicht, Kinder (Formular 1 Seite 1)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1 (Stammdaten, Erwerbsart, Kinder in Ihrem Haushalt, Unterhaltsbeiträge)
- **Regel:** Personalien sind bei der Steuerverwaltung gespeichert (Stand Ende Dezember) und bereits eingedruckt; Korrekturen auf der Steuererklärung vornehmen. Beruf und überwiegende Erwerbsart immer angeben; bei unselbständigem Hauptberuf Arbeitgeber. Kinder nur aufführen, wenn Abzug 23.1-23.3 beansprucht wird (Geburtsjahr/Jahrgang bestimmt Abzugsstufe und Vermögensabzug 36.3); bei Kindern in beruflicher Ausbildung Schule/Lehrfirma und voraussichtliche Dauer.
- **Bemerkung:** Keine Codes im Formularraster Seite 1 verifiziert.
- **Quellen:**
  - [WL AR 2025 S. 6](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0024.md) `ar-wl-2025__c0024` – «Die Angaben zu den Berufsverhältnissen (Beruf und überwiegende Erwerbsart)»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0025.md) `ar-wl-2025__c0025` – «Es sind nur diejenigen Kinder aufzuführen, für die Sie einen Abzug in den Ziffern 23.1, 23.2 oder 23.3 geltend machen»
  - [WL AR 2025 S. 6](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0024.md) `ar-wl-2025__c0024` – «Ende Dezember gespeicherten Daten»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0025.md) `ar-wl-2025__c0025` – «Aufgrund des Jahrgangs der Kinder können die für minderjährige Kinder»

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Haupterwerb unselbständig, Person 1 (Code 100) / Person 2 (Code 102)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn/Rente)
- **Regel:** Nettolohn gemäss Lohnausweis einsetzen (Brutto abzüglich AHV/IV/EO/ALV/NBUV und BVG-Beiträge, WL AR c0035; im Lohnausweis Ziff. 11 = Brutto abzüglich Ziff. 9 und 10, Ziff. 10.2 = vom Lohn abgezogene Einkäufe). Lohnausweise lückenlos belegen (Ziffern 1-10 des Lohnausweises); pro Arbeitgeber grundsätzlich ein Lohnausweis. Spesenpauschalen müssen im Lohnausweis stehen. Vom Arbeitgeber getragene berufsorientierte Aus-/Weiterbildung ist nicht steuerbar (im Lohnausweis Ziff. 13.3). Nicht im Nettolohn abgezogene NBUV-/BVG-Beiträge: Ziff. 16.6. Berufskosten: Ziff. 10 (Form. 4). Ein BVG-Einkauf in Ziff. 10.2 des Lohnausweises ist bereits im Nettolohn abgezogen; selbst bezahlte (nicht vom Lohn abgezogene) Einkäufe bescheinigt die Vorsorgeeinrichtung separat mit Formular 21 EDP.
- **Bund:** Gleiche Ziffer/Nettolohn für die direkte Bundessteuer (eine kantonale Steuererklärung für Staats-/Gemeindesteuer und DBSt).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Lohnausweis-Wegleitung (bund-wl-lohnausweis-2026) gilt für 2026: nur als Beschreibung der Lohnausweis-Felder zitiert (jahr_ok), Feldstruktur nicht für 2025 verifiziert. Zweitprüfung: «Einkauf Ziff. 10.2 nicht nochmals unter Ziff. 13.2 abziehen» ist eine Folgerung aus Lohnausweis Ziff. 10.2/11 (2026), in der WL AR 2025 nicht ausdrücklich belegt – Fachperson prüft.
- **Quellen:**
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0035.md) `ar-wl-2025__c0035` – «Einzusetzen ist der Nettolohn gemäss Lohnausweis»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0026.md) `ar-wl-2025__c0026` – «100 unselbständ iger Erwer Lohnausweis 102 13213211»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0034.md) `ar-wl-2025__c0034` – «Nicht steuerbar sind die vom Arbeitgeber getragenen Kosten der berufs»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «nicht vom Lohn abgezogene Einkaufsbeiträge»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0032.md) `ar-wl-2025__c0032` – «lückenlos zu belegen. Pro»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «In diesem Feld ist der für die Steuererklärung massgebende Nettolohn anzugeben.»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «In diesem Feld sind die im Bruttolohn enthaltenen, dem Arbeitnehmer vom Lohn abgezoge»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «In diesem Feld sind alle effektiven Vergütungen des Arbeitgebers für berufsorientierte»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0033.md) `ar-wl-2025__c0033` – «ein Lohnausweis einzurei»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Nebenerwerb unselbständig, Person 1 (Code 104) / Person 2 (Code 106), mit Art der Tätigkeit

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn) des Nebenarbeitgebers
- **Regel:** Nettolohn des zweiten Arbeitgebers; als Nebenerwerb gilt nur eine Tätigkeit neben einem Hauptberuf mit voller zeitlicher Beanspruchung für einen anderen Arbeitgeber. Berufskosten pauschal 20 % der Nettoeinkünfte (min. 800, max. 2'400) in Form. 4 Ziff. 5.1, alternativ tatsächliche Kosten (5.2). Mietzinsreduktion (z.B. Hauswart): Differenz zwischen normalem und reduziertem Mietzins als Einkommen deklarieren.
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Nebenerwerb: Pauschalabzug 20 % der Nettoeinkünfte (WL: Nettolohn), mind. CHF 800, max. CHF 2'400 (DBG-Ansatz).)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge))**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb Pauschale Minimum CHF 800.)** · Bund **CHF 800 (Minimum Pauschale Nebenerwerb)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb Pauschale Maximum CHF 2'400.)** · Bund **CHF 2'400 (Maximum Pauschale Nebenerwerb)**
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Nebenerwerb-Pauschale: Verweis auf DBG-Ansatz. (Lohnausweis-Ziffern: WL Lohnausweis 2026 mit jahr_ok, Feldstruktur nicht für 2025 verifiziert).
- **Quellen:**
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0035.md) `ar-wl-2025__c0035` – «Als Nebenerwerb gilt eine Tätigkeit, die gleichzeitig neben einem Hauptberuf»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0026.md) `ar-wl-2025__c0026` – «bstätigkeit 104»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0026.md) `ar-wl-2025__c0026` – «bstätigkeit 106»
  - [StV AR Art. 19](../../chunks/ar/2025/ar-stv/ar-stv__art-19.md) `ar-stv__art-19` – «werden die notwendigen Berufskosten nach den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «20 % der Nettoeinkünfte, mindestens im Jahr | 800.—»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0004.md) `ar-form-04-2025__c0004` – «5.1 Pauschalabzug: 20% der Nettoeinkünfte, mindestens Fr. 800,»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0036.md) `ar-wl-2025__c0036` – «ist die Differenz zwischen normalem und reduziertem Mietzins als Einkommen»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «In diesem Feld ist der für die Steuererklärung massgebende Nettolohn anzugeben.»

<a id="1-3-einkommen-unselbstaendig-vr-honorare"></a>
### Ziff. 1.3 – Sitzungsgelder, VR-Honorare, Behördenentschädigungen, Person 1 (Code 108) / Person 2 (Code 110)

- **Schlüssel:** `einkommen.unselbstaendig.vr_honorare` (VR-Honorare, Sitzungsgelder, Tantiemen (wo separat ausgewiesen, z.B. SG/AR Ziff. 1.3)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 6 (Verwaltungsratsentschädigungen) bzw. Bescheinigung der Behörde/Gesellschaft
- **Regel:** Nur soweit nicht bereits im Lohnausweis/Haupterwerb deklariert. Nebenamtliche Behördenmitglieder: zusätzlich zu den pauschalen Berufskosten bis max. Fr. 2'600 abziehbar (MB AR 15 Ziff. 3). Mit der Pauschale sind sämtliche Unkosten der Tätigkeit abgegolten; der Nachweis höherer effektiver Kosten bleibt vorbehalten.
- **Bund:** Zusatzabzug Fr. 2'600 für nebenamtliche Behördenmitglieder gilt nicht für die direkte Bundessteuer.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Lohnausweis Ziff. 6 (VR-Entschädigungen) aus WL Lohnausweis 2026 (jahr_ok, Feldstruktur nicht für 2025 verifiziert); Behörden: Bescheinigung der Behörde.
- **Quellen:**
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0037.md) `ar-wl-2025__c0037` – «zusätzlich bis max. Fr. 2’600.– abgezogen werden (gilt nicht für die direkte Bundessteuer)»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0026.md) `ar-wl-2025__c0026` – «108 13213211»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0026.md) `ar-wl-2025__c0026` – «Bescheinigung 110 13213211»
  - [MB AR 15 S. 1](../../chunks/ar/dauernd/ar-mb-15/ar-mb-15__c0003.md) `ar-mb-15__c0003` – «Mit dem Abzug der Pauschale sind sämtliche Unkosten im Zusammenhang mit den erwähnten Tätigkeiten abgegolten.»
  - [WL Lohnausweis 2026 S. 13](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0030.md) `bund-wl-lohnausweis-2026__c0030` – «In diesem Feld sind alle Entschädigungen anzugeben, die einer Person in ihrer Eigenschaft»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit (Industrie, Handel, Gewerbe, Landwirtschaft, freie Berufe, Internet-Plattformen), Person 1 (Code 112) / Person 2 (Code 114)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Jahresrechnung (Bilanz, Erfolgsrechnung, Eigenkapitalnachweis, Abschreibungstabelle) bzw. Einnahmen-Ausgaben-Rechnung
- **Regel:** Reine Einkünfte nach Abzug der Gewinnungskosten, ermittelt nach den im Steuerjahr 2025 abgeschlossenen Bilanzen und Erfolgsrechnungen (Layout der WL teilweise verzerrt, c0039). Aufstellung über Aktiven und Passiven, Einnahmen und Ausgaben sowie Privatentnahmen/-einlagen beilegen (Jahresrechnung, Eigenkapitalkonti, Abschreibungstabellen). Privatanteil an Vorsorgebeiträgen (2. Säule, 3a) nicht in der Erfolgsrechnung, sondern ausschliesslich in Ziff. 13.2 bzw. 13.1; Kinderzulagen der Ausgleichskasse in Ziff. 3.5 (Reingewinn entsprechend kürzen).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0038.md) `ar-wl-2025__c0038` – «Handels- und Gewerbebetrieben, aus Landwirtschaft sowie aus freien»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0026.md) `ar-wl-2025__c0026` – «112»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0026.md) `ar-wl-2025__c0026` – «selbständig 114»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0039.md) `ar-wl-2025__c0039` – «nach den im Kalenderjahr»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0039.md) `ar-wl-2025__c0039` – «Aufstellung über Aktiven und Passiven, Einnahmen und Ausgaben sowie Privat»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0040.md) `ar-wl-2025__c0040` – «pitalkonti (Privatkonti etc.)»
  - [WL AR 2025 S. 9](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0047.md) `ar-wl-2025__c0047` – «ausschliesslich in den Ziffern 13.2 bzw. 13.1 abgezogen werden.»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0054.md) `ar-wl-2025__c0054` – «sind in Ziffer 3.5 zu deklarieren»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Kollektiv-, Kommanditgesellschaften und einfache Gesellschaften, Person 1 (Code 120) / Person 2 (Code 122)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Angaben/Bescheinigung der Gesellschaft (inkl. Kapitalerträge)
- **Regel:** Einkünfte aus Beteiligungen an Kollektiv-/Kommanditgesellschaften und einfachen Gesellschaften (Konsortium) hier angeben. Verrechnungssteueransprüche auf Kapitalerträgen von Kollektiv-/Kommanditgesellschaften nicht in den persönlichen Rückerstattungsantrag aufnehmen; Rückerstattung mit Formular 25 direkt bei der Eidg. Steuerverwaltung (die Gesellschaft macht den Anspruch selber geltend).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Die WL nennt für die Gesellschaftsangaben «Formular 10», in 2025 ist Formular 10 jedoch Kinderbetreuungskosten – Beleg sind die Angaben der Firma.
- **Quellen:**
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0038.md) `ar-wl-2025__c0038` – «sind ebenfalls unter Ziffer 2.2 aufzuführen»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0027.md) `ar-wl-2025__c0027` – «120 13213211»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0027.md) `ar-wl-2025__c0027` – «Kommandit- 122»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0004.md) `ar-form-02-2025__c0004` – «Rückerstattung der Verrechnungssteuer mit Formular 25 direkt bei der Eidg. Steuerverwaltung»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0131.md) `ar-wl-2025__c0131` – «hat die Gesellschaft selber den Rückerstattungsanspruch mit dem Antrags»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV-/IV-Renten (zu 100 %), Person 1 (Code 126) / Person 2 (Code 128)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung der Ausgleichskasse (Jahresbetrag)
- **Regel:** Ordentliche und ausserordentliche AHV-/IV-Renten voll deklarieren. Ergänzungsleistungen sind nicht steuerbar (Unterstützungscharakter); Ziff. 8.3: Ergänzungsleistungen und Hilflosenentschädigungen sind steuerfrei, anzurechnen sind aber jene Ergänzungsleistungen, die zur Vergütung von Krankheits- und Behinderungskosten ausgerichtet werden.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0049.md) `ar-wl-2025__c0049` – «Die ordentlichen und ausserordentlichen AHV- und IV-Renten sind in vollem Um»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0049.md) `ar-wl-2025__c0049` – «nicht aber die ordentlichen und ausserordentlichen Ergänzungsleistungen»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0027.md) `ar-wl-2025__c0027` – «Versic herungen 126 32132111»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Ergänzungsleistungen und Hilflosenentschädigungen sind steuerfrei.»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Anzurechnen sind aber jene Ergänzungsleistungen, die zur Ver»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen (2. Säule, Säule 3a, Unfall-/Haftpflichtversicherung, Leibrenten) mit steuerbarem Prozentsatz, Person 1 (Code 130) / Person 2 (Code 132)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Rentenbescheinigung der Vorsorgeeinrichtung/Versicherung (Rentenbescheinigung Formular 11 gemäss WL Lohnausweis/Rentenbescheinigung)
- **Regel:** In der Vorkolonne vollen Betrag und Prozentsatz des steuerbaren Umfangs einsetzen (100 % in allen anderen Fällen; 80 % nur wenn die Rentenzahlung vor dem 31.12.2001 zu laufen begann, das Vorsorgeverhältnis vor dem 1.1.1985 bestand und der Versicherte mind. 20 % der Beiträge erbracht hat), Nettobetrag in die Hauptkolonne. Säule-3a-Renten 100 % steuerbar. Bei mehreren Renten Aufstellung beilegen. Leibrenten Säule 3b nach VVG: Ertragsanteil wird von der Versicherung bescheinigt; für privatrechtliche und ausländische Leibrenten siehe Ziff. 12.3.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Zuordnung 130/132 je Person aus Reihenfolge; Prozentfelder separat. «Formular 11» als Rentenbescheinigung: Bezeichnung aus WL Lohnausweis 2026 (jahr_ok), für 2025 nicht separat bestätigt.
- **Quellen:**
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0051.md) `ar-wl-2025__c0051` – «100 % in allen andern Fällen»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0050.md) `ar-wl-2025__c0050` – «Renten aus anerkannten Vorsorgeformen der Säule 3a 100 % steuerbar»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0027.md) `ar-wl-2025__c0027` – «130 gen. % sind beizule»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0051.md) `ar-wl-2025__c0051` – «des steuerbaren Ertragsanteils jährlich von der Versicherung bescheinigt.»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0052.md) `ar-wl-2025__c0052` – «ländischen Leibrenten wird auf Ziffer 12.3 verwiesen.»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «Wegleitung zum Ausfüllen des Lohnausweises bzw. der Rentenbescheinigung»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigungen, Taggelder aus Kranken-, Unfall-, Invalidenversicherung, Mutterschaftsentschädigung (nicht im Lohnausweis), Person 1 (Code 134) / Person 2 (Code 136)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Taggeldabrechnung/Bescheinigung der Versicherung bzw. Ausgleichskasse
- **Regel:** Nur soweit nicht im Lohnausweis enthalten. IV-Taggelder sind steuerbar. Damit zusammenhängende selbst getragene Krankheits-/Behinderungskosten über Formular 6 (Ziff. 21.1/21.2).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Codes 134/136 durch Reihenfolge (Miniatur stark verzerrt); Quelle für Code ist nur die Reihenfolge der Codes 126-146.
- **Quellen:**
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0053.md) `ar-wl-2025__c0053` – «IV-Taggelder gehören zum steuerbaren Einkommen und sind unter Ziffer 3.3»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0053.md) `ar-wl-2025__c0053` – «wie Mutterschaftsentschädigung sind unter Ziffer 3.3 insoweit anzugeben, als sie»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0028.md) `ar-wl-2025__c0028` – «211 134 321321 1»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0028.md) `ar-wl-2025__c0028` – «136 Aufstellung»

<a id="3-4-einkommen-ersatz-taggelder"></a>
### Ziff. 3.4 – Arbeitslosentaggelder (nicht im Lohnausweis), Person 1 (Code 138) / Person 2 (Code 140)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Arbeitslosenkasse
- **Regel:** Nur Taggelder, die nicht vom Arbeitgeber im Lohnausweis bescheinigt sind; Bescheinigung der Arbeitslosenkasse beilegen.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Codes 138/140 durch Reihenfolge abgeleitet.
- **Quellen:**
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0053.md) `ar-wl-2025__c0053` – «Taggelder aus Arbeitslosenversicherung sind insoweit anzugeben, als sie nicht»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0028.md) `ar-wl-2025__c0028` – «2 138 321321 1»

<a id="3-5-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.5 – Von Ausgleichskassen direkt ausbezahlte Kinder- und Familienzulagen (Code 142)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Familienausgleichskasse
- **Regel:** Nur direkt von der Ausgleichskasse ausbezahlte Zulagen; im Lohnausweis bereits enthaltene Zulagen nicht doppelt erfassen; bei Selbständigen Reingewinn entsprechend kürzen.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Code 142 durch Reihenfolge abgeleitet.
- **Quellen:**
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0054.md) `ar-wl-2025__c0054` – «Kinder- und Familienzulagen, die von Ausgleichskassen direkt ausbezahlt wurden,»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0028.md) `ar-wl-2025__c0028` – «Taggelder n-Taggelde 142»

<a id="4-1-einkommen-wertschriften"></a>
### Ziff. 4.1 – Erträge aus Wertschriften und Guthaben inkl. Lotterie-/Geldspielgewinne (Code 146), Übertrag Formular 2

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 Total Bruttoertrag A+B abzüglich Geschäftswertschriften (G) und Beteiligungserträge (BP, BG); Steuerauszug (eCH-0196)/Bankbescheinigungen
- **Regel:** Bruttoerträge 2025 nach Fälligkeit (Dividenden: Fälligkeitsdatum) im Wertschriftenverzeichnis; Total A+B abzüglich G, BP (-> Ziff. 4.2) und BG (-> Ziff. 4.3) in Ziff. 4.1. Kundenguthaben bis Fr. 200 Bruttozins je Kalenderjahr: Spalte B (ohne Verrechnungssteuer). Kryptowährungen sind im Wertschriften- und Guthabenverzeichnis anzugeben (inkl. Bitcoin, Ether etc.). Spielgewinne: einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen erst soweit > Fr. 1 Mio. steuerbar, aus Verkaufsförderungs-Lotterien erst wenn > Fr. 1'000; Gewinne aus Spielen mit ausschliesslicher Gratisteilnahme und aus ausländischen Spielen sind vollumfänglich steuerbar.
- **Limiten:**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'000'000 (Einzelne Gewinne aus zugelassenen Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1 Mio.)** · Bund **CHF 1'070'400 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'070'400)**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'000 (Gewinne aus Kleinspielen steuerfrei; einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'000.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'100)**
- **Bund:** Gleiche Erfassung in der kantonalen Steuererklärung für DBSt; Teilbesteuerung bei der DBSt: nicht aus AR-Quellen belegt.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 30.1 Seite 2 Ziffer 4.1»
  - [WL AR 2025 S. 23–24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0136.md) `ar-wl-2025__c0136` – «sind bis und mit Fr. 200.– je Kalenderjahr verrechnungssteuerfrei und daher in»
  - [WL AR 2025 S. 24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0138.md) `ar-wl-2025__c0138` – «einzelne Gewinne aus Grossspielen»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0028.md) `ar-wl-2025__c0028` – «146 13213211»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0128.md) `ar-wl-2025__c0128` – «rungen wie Bitcoin, Ether etc.).»
  - [WL AR 2025 S. 24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0138.md) `ar-wl-2025__c0138` – «und Geschicklichkeitsspielen zur Verkaufsförderung, wenn > Fr. 1’000.–;»
  - [WL AR 2025 S. 24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0138.md) `ar-wl-2025__c0138` – «Gewinne aus Spielen mit ausschliesslicher Gratisteilnahme sind vollumfäng»

<a id="4-2-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.2 – Erträge aus Beteiligungen ab 10 % (Privatvermögen, Code BP) (Code 147)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2: Erträge mit Code BP (Übertrag ohne Vorzeichen)
- **Regel:** Ausschüttungen von Schweizer Kapitalgesellschaften/Genossenschaften bei Beteiligung von mind. 10 % werden nur zu 60 % besteuert; der Teilbesteuerungsabzug (40 %) steht in Ziff. 16.7. Brutto-Ertrag hier ohne Vorzeichen eintragen.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 11](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0057.md) `ar-wl-2025__c0057` – «Sitz in der Schweiz werden nur zu 60 Prozent besteuert, wenn die steuerpflich»
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «Abzüglich Erträge aus Privatbeteiligung (BP) Übertrag in Steuererkl. Ziff. 4.2 (ohne Vorzeichen)»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0029.md) `ar-wl-2025__c0029` – «147 13213211»

<a id="4-3-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.3 – Erträge aus Beteiligungen ab 10 % (Geschäftsvermögen, Code BG) (Code 149)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 2: Erträge mit Code BG; Jahresrechnung
- **Regel:** Beteiligung gehört zum Geschäftsvermögen: ausgewiesenen Reingewinn (Ziff. 2) um diesen Betrag kürzen und hier deklarieren (sonst Doppelbesteuerung); kein Abzug Teilbesteuerung 16.7.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 11](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0057.md) `ar-wl-2025__c0057` – «Gehört eine solche Beteiligung zum Geschäftsvermögen selbständig Erwerbender»
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «Abzüglich Erträge aus Geschäftsbeteiligung Übertrag in Steuererkl. Ziff. 4.3 (ohne Vorzeichen)»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0029.md) `ar-wl-2025__c0029` – «n) 149 13213211»

<a id="5-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. 5 – Ertrag aus Liegenschaften: Eigenmietwert (abzüglich 20 % Selbstnutzungsabzug) und Mietertrag (Code 712), Übertrag Formular 7/7Z

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Formular 7 Abschn. B (Total Erträge a. und b.) bzw. Formular 7Z Spalte B
- **Regel:** Eigenmietwert = Mietwert gemäss amtlicher Grundstückschätzung; Selbstnutzungsabzug 20 % nur auf der am Wohnsitz dauernd selbst bewohnten Liegenschaft (nicht Zweit-/Ferienwohnung, nicht Landwirtschaft). Fremdnutzung: Mietzinsen ohne Nebenkosten (Netto-Mietzins), Leistungen Dritter und PV-Einspeisevergütung (netto nach Eigenverbrauch). Mehrere Liegenschaften: je Form. 7, Zusammenzug in Form. 7Z.
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **20 % (Selbstnutzungsabzug 20 % auf dem Eigenmietwert; nur auf der am Wohnsitz dauernd selbst bewohnten Liegenschaft.)** · Bund **n/a – Eigenmietwert wird nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt (Art. 21 Abs. 2 DBG); Abschaffung per 01.01.2029 beschlossen, 2025–2028 gilt bisheriges Recht. Der Eigenmietwert für die direkte Bundessteuer wird im kantonalen Veranlagungsverfahren festgesetzt; ein dort vorgesehener Abzug für die DBSt (z.B. TG 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Bund:** Eigenmietwert/Selbstnutzungsabzug: Behandlung bei der direkten Bundessteuer nicht aus AR-Quellen belegt - Bund-Wegleitung/ESTV-Quellen prüfen.
- **Bemerkung:** Code 712 laut Miniatur (Zeile Ertrag aus Liegenschaften).
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0002.md) `ar-form-07-2025__c0002` – «Übertrag in die Steuererklärung Seite 2 Ziffer 5»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0166.md) `ar-wl-2025__c0166` – «entspricht dem massgeblichen Mietwert abzüglich 20 Prozent»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0167.md) `ar-wl-2025__c0167` – «Miet- und Pachtzinsen bei Fremd- nutzung ohne Nebenkosten (Netto-Mietzins)»

<a id="6-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 6.1 – Erhaltene Unterhaltsbeiträge: für geschiedene/getrennt lebende Person (Code 154); für minderjährige Kinder (Code 156)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil bzw. Vereinbarung und Zahlungsnachweise
- **Regel:** Periodische Alimente für sich und Kinderalimente für unter Sorge/Obhut stehende minderjährige Kinder sind beim Empfänger steuerbar (Gegenstück beim Zahlenden: Ziff. 12.1/12.2). Wer Kinderalimente erhält, macht für dieses Kind keinen Kinderabzug geltend, wenn der Zahlende den Abzug nach Ziff. 12.2 beansprucht.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Zuordnung 154 = geschiedene/getrennte Person, 156 = minderjährige Kinder aus Reihenfolge abgeleitet.
- **Quellen:**
  - [WL AR 2025 S. 11–12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0060.md) `ar-wl-2025__c0060` – «sind bei der empfangenden Person steuerbar und daher»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0029.md) `ar-wl-2025__c0029` – «154 32132111»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0030.md) `ar-wl-2025__c0030` – «nfte iedene oder 156»

<a id="6-2-einkommen-erbschaften-unverteilt"></a>
### Ziff. 6.2 – Ertrag aus unverteilten Erbschaften (Code 158)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung des Erbenvertreters/Erbteilung, Inventar und Erbenverzeichnis
- **Regel:** Einkünfte unverteilter Erbschaften werden anteilig bei den Erben besteuert; detaillierte Aufstellung beilegen; Beteiligung zusätzlich im Wertschriftenverzeichnis (Form. 2 S. 1, Code 961) und Vermögensanteil in Ziff. 30.5. Zwischen Todestag und Erbteilung fällige Erträge anteilig hier.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0061.md) `ar-wl-2025__c0061` – «6.2 Einkünfte aus unverteilten Erbschaften und andern Vermögensmassen werden»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0030.md) `ar-wl-2025__c0030` – «158 321321 1»
  - [WL AR 2025 S. 25](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0143.md) `ar-wl-2025__c0143` – «beim Einkommen unter Ziffer 6.2, Ertrag aus unverteilter Erbschaft»

<a id="6-3-einkommen-uebrige"></a>
### Ziff. 6.3 – Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen, nicht verrechnete Förderbeiträge) mit Art (Code 162)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Mitarbeiterbeteiligung (Mitarbeiteraktien, Optionen, Anwartschaften/RSU, Beiblatt zum Lohnausweis), Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Aufstellung der Einkünfte; Mitarbeiterbeteiligungs-Bescheinigung
- **Regel:** Nur soweit nicht bereits in Ziff. 1-6.2 enthalten. Förderbeiträge/Subventionen, die im Vorjahr nicht mit dem Liegenschaftsunterhalt verrechnet werden konnten, sind hier anzugeben.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0061.md) `ar-wl-2025__c0061` – «6.3 Zu den übrigen Einkünften gehören beispielsweise Provisionen, Trinkgelder, Ein»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0030.md) `ar-wl-2025__c0030` – «162 321321 1»

<a id="6-4-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 6.4 – Kapitalabfindungen für wiederkehrende Leistungen mit Anzahl Jahre (Code 164)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der auszahlenden Stelle
- **Regel:** Auszahlungsbetrag und Anzahl Jahre einsetzen; Besteuerung zusammen mit den übrigen Einkünften zum Satz, der sich bei einer entsprechenden jährlichen Leistung ergäbe. Kapitalleistungen aus Vorsorge gehören nicht hierher, sondern auf Seite 4 (Ziff. 40/41).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0062.md) `ar-wl-2025__c0062` – «6.4 Die Kapitalabfindungen für wiederkehrende Leistungen sind mit dem Auszah»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0030.md) `ar-wl-2025__c0030` – «Jahre 164 321321»

## Einkommensberechnung

<a id="7-berechnung-total"></a>
### Ziff. 7 – Total der Einkünfte (Code 168)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 1-6)
- **Regel:** Summe der Einkünfte Ziff. 1.1-6.4; nicht enthalten sind Ergänzende Angaben (Ziff. 8) und Kapitalleistungen aus Vorsorge (Ziff. 40/41).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Textliche Bezeichnung «Total der Einkünfte» im Raster stark zerlegt (nur Code und Raster-Kontext belegt).
- **Quellen:**
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0030.md) `ar-wl-2025__c0030` – «168 e Einkünfte»

<a id="18-berechnung-total"></a>
### Ziff. 18 – Total der Abzüge (Zeile nach Ziff. 17)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Summe der Abzüge Ziff. 10-17.
- **Bemerkung:** Ziffer/Code in den AR-Quellen nicht belegt (konkordanz-CSV nennt 18/Code unverifiziert); Rechenlogik: Art. 28 StG (Einkünfte abzüglich Abzüge Art. 29-36). Geprüft: weiterhin offen; im Formular/in der WL ist Ziff. 18 nicht belegt, nur die Rechenlogik (Art. 28 Abs. 1 StG).
- **Quellen:**
  - [StG AR Art. 28](../../chunks/ar/2025/ar-stg/ar-stg__art-28.md) `ar-stg__art-28` – «werden von den gesamten steuerbaren Einkünften die Aufwendungen und allgemeinen Abzüge gemäss Art. 29–36 abgezogen»

<a id="20-berechnung-total"></a>
### Ziff. 20 – Nettoeinkommen (Basis für Selbstbehalt Krankheitskosten und Limite Zuwendungen)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Nettoeinkommen (Herleitung aus Einkünften und Abzügen im Formular Seite 3 in den vorliegenden Quellen nicht belegt – am Originalformular prüfen)
- **Regel:** Massgebende Grösse für Selbstbehalt 5 % (Ziff. 21.1) und für das 20 %-Maximum der Zuwendungen (Ziff. 21.3).
- **Bemerkung:** Code nicht verifiziert. Schlüssel berechnung.total wird mehrfach verwendet (Taxonomie kennt nur diesen Schlüssel für Totalzeilen); Zeile Ziff. 20 ist durch den Verweis «Nettoeinkommen gemäss Ziffer 20» belegt, die Rechenregel nicht.
- **Quellen:**
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0099.md) `ar-wl-2025__c0099` – «5 Prozent des Nettoeinkommens gemäss Ziffer 20 übersteigen»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0103.md) `ar-wl-2025__c0103` – «tens Fr. 100.– beträgt; maximal jedoch 20 Prozent des Nettoeinkommens»

<a id="21-1-abzug-krankheitskosten"></a>
### Ziff. 21.1 – Krankheits- und Unfallkosten nach Selbstbehalt (Vorkolonne: Total Formular 6; Hauptkolonne: über 5 % des Nettoeinkommens)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 6 Seite 2 Total Krankheits- und Unfallkosten (selbst getragen)
- **Regel:** Pro Rechnung Bruttobetrag abzüglich Beiträge Dritter (KK, UV, Hilflosenentschädigung) = selbst getragene Kosten; ärztliches Zeugnis bei Medikamenten/Diät. Abzugsfähig ist nur der Teil über 5 % des Nettoeinkommens (Ziff. 20). Anstelle effektiver Diätmehrkosten Pauschale Fr. 2'500 bei dauernder lebensnotwendiger Diät (Zöliakie, nicht Diabetes). Pensionskosten ohne Pflegebedarf sind nicht abzugsfähig.
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten: abziehbar, soweit sie 5 % der um die Aufwendungen gemäss Art. 28-35 verminderten steuerbaren Einkünfte übersteigen.)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Bund:** Bund: Selbstbehaltsregel DBSt nicht aus AR-Quellen belegt (Bund-Quellen prüfen).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [Formular 6 AR 2025 S. 2](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0003.md) `ar-form-06-2025__c0003` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.1 (Vorkolonne)»
  - [Formular 6 AR 2025 S. 2](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0003.md) `ar-form-06-2025__c0003` – «Abzugsfähig sind die tatsächlich selbst getragenen Kosten»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0099.md) `ar-wl-2025__c0099` – «5 Prozent des Nettoeinkommens gemäss Ziffer 20 übersteigen»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0099.md) `ar-wl-2025__c0099` – «notwendiger Diät (z.B. bei Zöliakie, nicht jedoch bei Diabetes) eine Pauschale von Fr. 2’500.– in Abzug gebracht werden»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0098.md) `ar-wl-2025__c0098` – «ist in die Vorkolonne von Ziffer»

<a id="21-2-abzug-behinderungskosten"></a>
### Ziff. 21.2 – Behinderungsbedingte Kosten (Übertrag Formular 6 Seite 2; Pflegeheim-Pauschale 2/3, Pauschalen 2'500/5'000/7'500)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 6 Seite 2 Behinderungsbedingte Kosten Total; Verfügung Hilflosenentschädigung; Bewohnerkonto Pflegeheim
- **Regel:** Ohne Selbstbehalt abziehbar. Dauerhafter Pflegeheimaufenthalt (ab Pflegestufe 4 bzw. ab 61 Min. Pflege-/Betreuungsaufwand): pauschal 2/3 der selbst getragenen Heimkosten, Hilflosenentschädigung AHV/IV abziehen, Bewohnerkonto beilegen. Statt effektiver Kosten Pauschale nach Hilflosenentschädigung: leicht Fr. 2'500, mittel Fr. 5'000, schwer Fr. 7'500 (Verfügung einreichen); Gehörlose und Dialyse-Patienten Fr. 2'500.
- **Bund:** Bund: Regel behinderungsbedingte Kosten DBSt nicht aus AR-Quellen belegt (Bund-Quellen prüfen).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [Formular 6 AR 2025 S. 2](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0004.md) `ar-form-06-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.2»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0100.md) `ar-wl-2025__c0100` – «Minuten Pflege- und Betreuungsaufwand) ausgewiesen ist»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0100.md) `ar-wl-2025__c0100` – «Selbstbehalt in Abzug gebracht»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0101.md) `ar-wl-2025__c0101` – «Fr. 2’500.– Auf der Internetseite www.ar.ch/»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0101.md) `ar-wl-2025__c0101` – «Fr. 5’000.– steuerverwaltung unter häufige»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0101.md) `ar-wl-2025__c0101` – «Fr. 7’500.–»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0101.md) `ar-wl-2025__c0101` – «schalabzug von Fr. 2’500.– anerkannt»

<a id="21-3-abzug-spenden"></a>
### Ziff. 21.3 – Freiwillige Zuwendungen an steuerbefreite juristische Personen (Code 550), Übertrag Formular 5 Teil A

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Formular 5 Teil A Total der Zuwendungen (Spendenbestätigungen auf Verlangen)
- **Regel:** Nur Geldleistungen/Vermögenswerte an in der Schweiz steuerbefreite gemeinnützige/öffentliche Institutionen, uneigennützig (Mitgliederbeiträge nicht abziehbar); Gesamtbetrag nur abzugsfähig, wenn Total mind. Fr. 100; Maximum 20 % des Nettoeinkommens (Ziff. 20). Religiöse Institutionen nur bei ausschliesslich gemeinnütziger Zweckbestimmung.
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Zuwendungen nur abziehbar, wenn sie in der Steuerperiode CHF 100 erreichen.)** · Bund **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen (CH) bzw. Gemeinwesen: mindestens CHF 100 im Steuerjahr)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen max. 20 % der um die Aufwendungen gemäss Art. 28-35 verminderten steuerbaren Einkünfte.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Bund:** Bund: Maximum und Mindestbetrag siehe data/werte/bund/2025.yaml (nicht aus AR-Quellen belegt).
- **Bemerkung:** Code 550 aus Hilfsblatt Form. 5.
- **Quellen:**
  - [Formular 5 AR 2025 S. 2](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0003.md) `ar-form-05-2025__c0003` – «Total der Zuwendungen 550 3213211»
  - [Formular 5 AR 2025 S. 2](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0003.md) `ar-form-05-2025__c0003` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.3»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0103.md) `ar-wl-2025__c0103` – «tens Fr. 100.– beträgt; maximal jedoch 20 Prozent des Nettoeinkommens»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0102.md) `ar-wl-2025__c0102` – «Mitgliederbeiträge sind nicht abzugsfähig»

<a id="22-berechnung-total"></a>
### Ziff. 22 – Reineinkommen

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeile (Nettoeinkommen abzüglich Abzüge Ziff. 21)
- **Regel:** Nettoeinkommen abzüglich zusätzliche Abzüge 21.1-21.3; Sozialabzüge (Ziff. 23) werden vom Reineinkommen abgezogen.
- **Bemerkung:** Ziffer/Code 22 in den AR-Quellen nicht belegt; Reineinkommen/Sozialabzüge laut Art. 28 und Art. 38 StG (ar-stg__art-28, ar-stg__art-38-t1). Geprüft: weiterhin offen; Ziffer/Code 22 nicht in WL/Formularraster belegt, nur die Rechenlogik (Art. 28, Art. 38 Abs. 1 StG).
- **Quellen:**
  - [StG AR Art. 28](../../chunks/ar/2025/ar-stg/ar-stg__art-28.md) `ar-stg__art-28` – «werden von den gesamten steuerbaren Einkünften die Aufwendungen und allgemeinen Abzüge gemäss Art. 29–36 abgezogen»
  - [StG AR Art. 38](../../chunks/ar/2025/ar-stg/ar-stg__art-38-t1.md) `ar-stg__art-38-t1` – «Vom Reineinkommen werden für die Steuerberechnung abgezogen»

<a id="23-1-sozialabzug-kinder"></a>
### Ziff. 23.1 – Kinderabzug: Kind bis zur Vollendung des 4. Altersjahrs

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Seite 1 der Steuererklärung (Kinder, Geburtsdatum) - Stichtag 31.12.2025
- **Regel:** Fr. 5'300 pro Kind bis zur Vollendung des 4. Altersjahrs, wenn Unterhalt zur Hauptsache bestritten, Kind auf Unterhalt angewiesen und kein Abzug Unterhaltsbeiträge (12.2) geltend gemacht. Kein Abzug, wenn Einkünfte des Kindes Fr. 18'000 übersteigen. Getrennte Eltern: hälftig bei gemeinsamer elterlicher Sorge und ohne Unterhaltsbeiträge.
- **Limiten:**
  - Kinderabzug Vorschulalter (CHF): Kanton **CHF 5'300 (Kinderabzug bis Vollendung des 4. Altersjahres: CHF 5'300 (indexiert per 1.1.2024).)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (sozialabzug.kind); Staffelung nach Alter nur kantonal.**
- **Bund:** Bund: Kinderabzug eigener Betrag (nicht nach Altersstufen; data/werte/bund/2025.yaml).
- **Bemerkung:** Der StG-Text nennt Fr. 5'000 (nicht indexiert); massgebend Anhang 1 StG (per 1.1.2024) und WL 2025: Fr. 5'300. MB 02 (Fassung 25.9.2025) nennt noch Fr. 5'000/7'000/11'000 - MB-Werte nicht indexiert, im Widerspruch zu Anhang 1/WL (Rangfolge: Gesetz-Anhang und WL gelten). Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «23.1 Für jedes Kind bis zur Vollendung des 4. Altersjahrs Fr. 5’300»
  - [StG AR Anhang 1 S. 1](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0001.md) `ar-stg-anhang-kp__c0001` – «Art. 38 Abs. 1 lit. a Ziff. 1 5'300»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Für die Festsetzung der Sozialabzüge sind die Verhältnisse am 31. Dezember 2025»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Fr. 18‘000 kann kein Kinderabzug geltend gemacht werden»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Werden die Eltern getrennt besteuert, kann der Kinderabzug hälftig aufgeteilt»

<a id="23-2-sozialabzug-kinder"></a>
### Ziff. 23.2 – Kinderabzug: Kind nach Vollendung des 4. bis zur Vollendung des 15. Altersjahrs

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Seite 1 der Steuererklärung (Kinder, Geburtsdatum)
- **Regel:** Fr. 7'400 pro Kind (4.-15. Altersjahr), Voraussetzungen wie 23.1.
- **Limiten:**
  - Kinderabzug Schulalter (CHF): Kanton **CHF 7'400 (Kinderabzug nach Vollendung des 4. bis Vollendung des 15. Altersjahres: CHF 7'400 (indexiert).)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (sozialabzug.kind).**
- **Bund:** Bund: Kinderabzug eigener Betrag.
- **Bemerkung:** MB 02 nennt Fr. 7'000 (nicht indexiert) - siehe 23.1. Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «des 15. Altersjahrs Fr. 7’400»
  - [StG AR Anhang 1 S. 1](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0001.md) `ar-stg-anhang-kp__c0001` – «Art. 38 Abs. 1 lit. a Ziff. 2 7'400»

<a id="23-3-sozialabzug-kinder"></a>
### Ziff. 23.3 – Kinderabzug: Kind nach Vollendung des 15. Altersjahrs bis Volljährigkeit sowie volljährig in beruflicher/schulischer Ausbildung bis 26. Altersjahr

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Seite 1 der Steuererklärung (Kinder, Schule/Lehrfirma, Dauer der Ausbildung)
- **Regel:** Fr. 11'600 pro Kind; für volljährige Kinder in Erstausbildung bis zur Vollendung des 26. Altersjahrs (Ausbildung angeben: Schule oder Lehrfirma und voraussichtliche Dauer). Unterhaltsbeiträge an volljährige Kinder sind nicht abziehbar (beim Empfänger unbesteuert, WL Ziff. 12.2).
- **Limiten:**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 11'600 (Kinderabzug nach 15. Altersjahr bis Volljährigkeit sowie volljährige Kinder in Ausbildung bis 26. Altersjahr: CHF 11'600 (indexiert).)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Kinderabzug CHF 6'800 wie für Minderjährige (kein höherer Ausbildungsabzug))**
- **Bund:** Bund: Kinderabzug eigener Betrag.
- **Bemerkung:** MB 02 nennt Fr. 11'000 (nicht indexiert) - siehe 23.1. Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «bis zur Vollendung des 26. Altersjahrs Fr. 11’600»
  - [StG AR Anhang 1 S. 1](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0001.md) `ar-stg-anhang-kp__c0001` – «Art. 38 Abs. 1 lit. a Ziff. 3 11'600»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «Unterhaltsbeiträge, die an ein volljähriges Kind bezahlt werden,»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0025.md) `ar-wl-2025__c0025` – «Bei Kindern in beruflicher Ausbildung ist zudem die Schule oder Lehrfirma und»

<a id="23-4-sozialabzug-unterstuetzung"></a>
### Ziff. 23.4 – Unterstützungsabzug für unterstützte Person (nur direkte Bundessteuer)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Bescheinigung der unterstützten Person/Zahlungsnachweise (Name, Adresse, Betrag)
- **Regel:** Fr. 6'800 nur bei der DBSt; Voraussetzung: Beiträge mind. in Höhe des Abzugs an eine erwerbsunfähige/beschränkt erwerbsfähige Person; nicht für Ehegatten/eingetragene Partner und nicht für Kinder mit Kinderabzug. Für Staats-/Gemeindesteuer kein Unterstützungsabzug.
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **n/a – Unterstützungsabzug (CHF 6'800) gilt gemäss WL 2025 Ziff. 23.4 nur für die direkte Bundessteuer; kantonal nicht vorgesehen (Art. 38 Abs. 1 lit. b StG aufgehoben).** · Bund **CHF 6'800 (Unterstützungsabzug pro erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mindestens in Höhe des Abzugs unterstützt; nicht für Ehegatten und Kinder mit Kinderabzug)**
- **Bund:** Nur DBSt: Fr. 6'800 (AR-Quelle WL).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «23.4 Abzug für jede unterstützte Person (gilt nur für die direkte Bundessteuer) Fr. 6’800»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0105.md) `ar-wl-2025__c0105` – «Dieser Abzug gilt nur für die»

<a id="24-berechnung-total"></a>
### Ziff. 24 – Steuerbares Einkommen

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Reineinkommen abzüglich Sozialabzüge)
- **Regel:** Steuersatz bestimmt sich auf dem steuerbaren Einkommen (Ziff. 24); vereinfacht abgerechnete Löhne (8.1) werden nicht berücksichtigt.
- **Bemerkung:** Code nicht verifiziert.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0063.md) `ar-wl-2025__c0063` – «stimmung des Steuersatzes auf dem steuerbaren Einkommen (Ziff. 24)»

## Weitere Angaben

<a id="8-1-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 8.1 – Im vereinfachten Abrechnungsverfahren (BGSA) abgerechneter Bruttolohn - nur Information (Code 290)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Abrechnung/Bescheinigung der AHV-Ausgleichskasse
- **Regel:** Bruttolohn einsetzen, nur zur Information (nicht im Total der Einkünfte Ziff. 7); mit 5 % Quellensteuerabzug sind DBSt und Kantons-/Gemeindesteuern abgegolten; keine Abzüge im ordentlichen Verfahren dafür.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Korrigiert durch Prüfung: Beleg lohnausweis entfernt; beim vereinfachten Verfahren (BGSA) wird kein Lohnausweis ausgestellt, Beleg ist die Abrechnung der AHV-Ausgleichskasse (kein passender Belegtyp in der Taxonomie).
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0063.md) `ar-wl-2025__c0063` – «In Ziff. 8.1 ist der Bruttolohn einzusetzen.»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0063.md) `ar-wl-2025__c0063` – «8.1 Gemäss Bundesgesetz gegen die Schwarzarbeit (BGSA) können Arbeitgeber klei»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0030.md) `ar-wl-2025__c0030` – «290 213211»

<a id="8-2-info-steuerfreie-leistungen"></a>
### Ziff. 8.2 – Ergänzungsleistungen (nur Information) (Code 291)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung/Bescheinigung der Ausgleichskasse
- **Regel:** Nur Angabe; Ergänzungsleistungen sind steuerfrei. Anzurechnen sind die zur Vergütung von Krankheits-/Behinderungskosten ausgerichteten Beträge (mindern Ziff. 21.1/21.2).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Ergänzungsleistungen und Hilflosenentschädigungen sind steuerfrei.»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0031.md) `ar-wl-2025__c0031` – «291 tragen»

<a id="8-3-info-steuerfreie-leistungen"></a>
### Ziff. 8.3 – Hilflosenentschädigungen (nur Information) (Code 292)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung der Hilflosenentschädigung
- **Regel:** Nur Angabe; steuerfrei, aber an die behinderungsbedingten Kosten (Form. 6, Ziff. 21.2) anzurechnen, für die sie bestimmt sind. Verfügung auch bei Pauschalabzug 21.2 einreichen.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Ergänzungsleistungen und Hilflosenentschädigungen sind steuerfrei.»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0031.md) `ar-wl-2025__c0031` – «292 213211»

<a id="8-4-info-steuerfreie-leistungen"></a>
### Ziff. 8.4 – Überbrückungsleistungen für ältere Arbeitslose (nur Information) (Code 293)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung über Überbrückungsleistungen
- **Regel:** Nur Angabe; steuerfrei (Bundesgesetz vom 19. Juni 2020).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Steuerfrei sind Einkünfte aus Überbrückungsleistungen für ältere Arbeitslose ge»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0031.md) `ar-wl-2025__c0031` – «293 213211»

<a id="40-41-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. 40-41 – Ausbezahlte Kapitalleistungen aus Vorsorge: 40.1 Säule 3a, 40.2 berufliche Vorsorge, 40.3 übrige; Total Ziff. 41 (Code 950)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung/Bank
- **Regel:** Gesondert besteuert (volle Jahressteuer), Sozialabzüge werden nicht gewährt; nicht in Ziff. 6.4/7. Tarif: Satz der einfachen Steuer nach Art. 41 StG (Tarifgrenze indexiert gem. Anhang 1: 417'200). Bescheinigung beilegen. Einkauf-Sperrfrist/WEF siehe MB 08/09/19.
- **Bund:** Besteuerung der Kapitalleistungen bei der DBSt: nicht aus AR-Quellen belegt (Bund-Quellen prüfen).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Einzelcodes 40.1-40.3 nicht erkennbar; nur Total-Code 950. 417'200 gilt als indexierter Anhang-Wert; StG-Text nennt 400'000 (nicht indexiert).
- **Quellen:**
  - [StG AR Art. 41](../../chunks/ar/2025/ar-stg/ar-stg__art-41.md) `ar-stg__art-41` – «Kapitalleistungen gemäss Art. 25 sowie Zahlungen bei Tod und für bleibende körperliche oder gesundheitliche Nachteile werden gesondert besteuert»
  - [StG AR Art. 41](../../chunks/ar/2025/ar-stg/ar-stg__art-41.md) `ar-stg__art-41` – «Die Sozialabzüge werden nicht gewährt.»
  - [StG AR Anhang 1 S. 1–2](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0002.md) `ar-stg-anhang-kp__c0002` – «Art. 41 Abs. 1 lit. a Ziff. 1 417'200»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0109.md) `ar-wl-2025__c0109` – «aus Vorso Bescheinigung»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0109.md) `ar-wl-2025__c0109` – «950»

## Abzüge

<a id="10-1-abzug-berufskosten-uebrige"></a>
### Ziff. 10.1 – Berufskosten unselbständig Erwerbende, Person 1 (Total Formular 4, Code 438); Person 2 unter Ziff. 10.2 (Code 488)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Formular 4 Ziff. 6 Total der Berufskosten (Person 1 Vorderseite, Person 2 Rückseite)
- **Regel:** Total aus Form. 4 (Fahrkosten max. 6'000, Verpflegung, übrige Kosten Pauschale oder effektiv, Wochenaufenthalt, Nebenerwerb) übertragen. Pauschale übrige Kosten (Fr. 700 + 10 % des Nettolohns, max. Fr. 2'400) kann jede unselbständig erwerbstätige Person beanspruchen. Hinweis: Nach Form. 4 nimmt Ziff. 10.1 das Total Person 1, Ziff. 10.2 das Total Person 2 auf (nicht Fahrkosten/Verpflegung wie in den Titeln der WL-Chunks).
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 (Pendlerabzug).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Übrige Berufskosten Pauschale: CHF 700 zuzüglich 10 % des Nettolohnes, max. CHF 2'400.)** · Bund **3 % (Übrige Berufskosten: 3 % des Nettolohns (Pauschale; Nachweis höherer Kosten möglich); bei Teilzeit/unterjährig angemessen kürzen)**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockelbetrag der Pauschale (zuzüglich 10 % des Nettolohnes).)** · Bund **n/a – Bund: 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; kein 'fix + %'-Modell.**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Maximum der Pauschale für übrige Berufskosten: CHF 2'400.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
- **Bund:** Direkte Bundessteuer hat eigene Maxima/Pauschalen (Fahrkosten, übrige Berufskosten): siehe data/werte/bund/2025.yaml; AR-Fr. 6'000 gilt nur für Staats-/Gemeindesteuer.
- **Bemerkung:** Hauptformular-Code für Ziff. 10.1/10.2: nicht verifiziert (438/488 sind die Codes der Total-Zeile in Form. 4). Gleichzeitig Zweiverdienerabzug: Berufskosten mindern Basis (Ziff. 17).
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0004.md) `ar-form-04-2025__c0004` – «Total der Berufskosten 438 13211 zu übertragen in die Steuererklärung Seite 3 Ziffer 10.1»
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0008.md) `ar-form-04-2025__c0008` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 10.2»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0065.md) `ar-wl-2025__c0065` – «10. Berufskosten bei unselbständiger Erwerbstätigkeit 4»

<a id="11-abzug-schuldzinsen"></a>
### Ziff. 11 – Schuldzinsen (privat), Übertrag Formular 5 Teil A (Code nicht verifiziert)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 5 Teil A Total private Schuldzinsen (Spalte rechts)
- **Regel:** Tatsächlich bezahlte Zinsen 2025 auf anerkannten Schulden; nicht abzugsfähig: Amortisationen, Anlagekosten-Zinsen (ausser Baukreditzinsen), Baurechtszinsen selbstgenutzter Eigenheime, Leasingraten. Private Schuldzinsen nur bis Wertschriften-/Guthabenerträge (Ziff. 4, ohne Lotteriegewinne) plus Liegenschaftserträge (Ziff. 5) zuzüglich Fr. 50'000.
- **Bund:** Schuldzinsen-Abzugsgrenze bei der DBSt nicht aus AR-Quellen belegt; Bundesregeln separat prüfen.
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0001.md) `ar-form-05-2025__c0001` – «Total private Schulden und private Schuldzinsen 213213211 13213211»
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0001.md) `ar-form-05-2025__c0001` – «Seite 3 Ziffer 11»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0081.md) `ar-wl-2025__c0081` – «zuzüglich Fr. 50’000.–»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0081.md) `ar-wl-2025__c0081` – «sind im Teil A des Formulars 5 zu deklarieren»

<a id="12-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.1 – Unterhaltsbeiträge an geschiedene/getrennt lebende Person

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungsurteil/Trennungsvereinbarung, Zahlungsnachweise
- **Regel:** Beiträge an die geschiedene, gerichtlich oder tatsächlich getrennt lebende Person; bei erstmaliger Zahlung Urteilsauszug und Zahlungsnachweis beilegen.
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «12.2 Die Unterhaltsbeiträge an einen Elternteil für die unter dessen elterlicher Sorge»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «Bei erstmaliger Zahlung von Unterhaltsbeiträgen»

<a id="12-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.2 – Unterhaltsbeiträge für minderjährige Kinder (an den Elternteil mit Sorge/Obhut)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungsurteil/Vereinbarung, Zahlungsnachweise
- **Regel:** Abziehbar nur für minderjährige Kinder unter der Sorge/Obhut des anderen Elternteils; dann entfällt der Kinderabzug 23.1-23.3. Beiträge an volljährige Kinder: nicht abziehbar (beim Empfänger unbesteuert).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «12.2 Die Unterhaltsbeiträge an einen Elternteil für die unter dessen elterlicher Sorge»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «Unterhaltsbeiträge, die an ein volljähriges Kind bezahlt werden»

<a id="12-3-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.3 – Rentenleistungen (Leibrenten nach OR, Ertragsanteil)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Vertrag/Bescheinigung der Rentenzahlung
- **Regel:** Abziehbar ist der Ertragsanteil, berechnet aus der Durchschnittsrendite zehnjähriger Bundesobligationen plus 0,5 %; der massgebende Prozentsatz wird jährlich von der ESTV veröffentlicht.
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Prozentsatz 2025 nicht in den AR-Quellen: bei ESTV prüfen.
- **Quellen:**
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «Bei der Finanzierung von Leibrenten nach Obligationenrecht berechnet sich der»

<a id="13-1-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.1 – Beiträge Säule 3a (gebundene Selbstvorsorge)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Bescheinigung der Bank-/Versicherungsstiftung (Formular 21 EDP)
- **Regel:** Nur 2025 tatsächlich bezahlte Beiträge, Bescheinigung beilegen. Max. Fr. 7'258 mit 2. Säule; ohne 2. Säule 20 % des Erwerbseinkommens, max. Fr. 36'288. Beide Partner können je den Abzug beanspruchen. Selbständige: Beiträge nicht in der Erfolgsrechnung, sondern hier.
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a: Erwerbstätige mit 2. Säule max. CHF 7'258 (nur im Jahr 2025 tatsächlich bezahlte Beiträge).)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug mit Zugehörigkeit zur 2. Säule (8 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a: Erwerbstätige ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288.)** · Bund **CHF 36'288 (Säule 3a: Höchstabzug ohne 2. Säule (max. 36'288, 40 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. CHF 36'288).)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. CHF 36'288))**
- **Bund:** Verweis auf DBG-Ansatz: Art. 35 lit. e StG AR gewährt den Abzug «im Umfang von Art. 82 BVG»; Höchstbeträge 2025 daher identisch mit Bund (7'258 / 36'288; data/werte/bund/2025.yaml). Einkauf 3a erst ab 2026.
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Verweis auf DBG-Ansatz (Art. 35 lit. e StG AR i.V.m. Art. 82 BVG).
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «Erwerbstätige mit 2. Säule (Belege) max. Fr. 7’258»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «Erwerbstätige ohne 2. Säule: 20 % des Erwerbseinkommens (Belege) max. Fr. 36’288»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0084.md) `ar-wl-2025__c0084` – «Sind beide Partner erwerbstätig und leisten sie Beiträge an eine anerkannte Vor»
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t2.md) `ar-stg__art-35-t2` – «im Sinn und im Umfang von Art. 82 des Bundesgesetzes über die berufliche Alters-, Hinterlassenen- und Invalidenvorsorge»
  - [BSV Masszahlen 25/26 S. 1](../../chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) `bund-bsv-masszahlen-2025-2026__c0003` – «Oberer Grenzbetrag bei Unterstellung unter 2. Säule 7'258 7'258»
  - [BSV Masszahlen 25/26 S. 1](../../chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) `bund-bsv-masszahlen-2025-2026__c0003` – «Oberer Grenzbetrag ohne Unterstellung unter 2. Säule 36'288 36'288»

<a id="13-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 13.2 – Beiträge/Einkäufe in die 2. Säule (soweit nicht im Lohnausweis abgezogen)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ⚠️ strittig
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) mit Einkaufsberechnung; Lohnausweis Ziff. 10.1/10.2
- **Regel:** Nur Beiträge, die nicht schon vom Lohn abgezogen und damit im Nettolohn (Lohnausweis Ziff. 11) berücksichtigt sind. Lohnausweis Ziff. 10.2 (Einkauf, vom Lohn abgezogen) ist bereits abgezogen -> nicht doppelt hier. Selbst bezahlte Einkäufe: Bescheinigung der Pensionskasse mit Formular 21 EDP plus Einkaufsberechnung; bei Selbständigen 100 % der Einkaufsbeiträge hier. Einkauf: 3-Jahres-Sperre für Kapitalbezug (MB 08) beachten.
- **Bund:** Einkauf in die 2. Säule bei der DBSt: Regeln nicht aus AR-Quellen belegt (Bund-Quellen prüfen).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). WL-intern widersprüchlich: Ziff. 13.2 (c0089, c0051, Hilfsformular) nimmt BVG-Beiträge/Einkäufe auf, Ziff. 1.1 (c0038) verweist für nicht im Nettolohn abgerechnete BVG-/NBUV-Beiträge auf Ziff. 16.6. Fachperson entscheidet; hier als Hauptzeile 13.2 geführt. Lohnausweis-Wegleitung gilt 2026 (jahr_ok).
- **Quellen:**
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0084.md) `ar-wl-2025__c0084` – «sind hier immer 100 % der Einkaufsbeiträge zu deklarieren»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0084.md) `ar-wl-2025__c0084` – «zulegen, zusammen mit der entsprechenden Einkaufsberechnung»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «nicht vom Lohn abgezogene Einkaufsbeiträge»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «Beiträge für den Einkauf von fehlenden Versicherungsjahren»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0035.md) `ar-wl-2025__c0035` – «bzw. im Lohnausweis nicht bereits abgerechnet sind, können unter der Ziffer 16.6 abgezogen werden»

<a id="14-abzug-versicherungspraemien"></a>
### Ziff. 14 – Versicherungsprämien und Zinsen von Sparkapitalien (Übertrag Formular 6 Teil C, Code 600)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 6 Teil C: niedrigerer Betrag aus A (bezahlte Prämien/Sparzinsen abzüglich Prämienverbilligung) und B (Maximum)
- **Regel:** A = Krankenversicherung (brutto), Unfall (ohne NBUV), Lebens-/Rentenversicherung, Sparzinsen gemäss Wertschriftenverzeichnis, abzüglich Prämienverbilligungen; B = Max. Fr. 5'400 gemeinsam / Fr. 2'700 übrige plus Fr. 1'000 je Kind mit Kinderabzug 23.1-23.3. Abzug = niedrigerer Betrag von A und B. Ausgeschlossen: Mobiliar-, Motorfahrzeug-, Haftpflicht- und Sachversicherungen.
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'400 (Versicherungsprämien und Sparzinsen: in ungetrennter Ehe lebende Personen max. CHF 5'400 (abzüglich Prämienverbilligung).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'700 (Versicherungsprämien und Sparzinsen: übrige Steuerpflichtige max. CHF 2'700 (abzüglich Prämienverbilligung).)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag pro Kind (bzw. unterstützte Person mit Abzug nach Art. 38) CHF 1'000.)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
- **Bund:** Versicherungsabzug beim Bund mit anderen Beträgen (data/werte/bund/2025.yaml); eine Berechnung im AR-Formular 6 nur für Staats-/Gemeindesteuer.
- **Bemerkung:** Code 600 (Hilfsblatt Form. 6, Hauptformular-Code für Ziff. 14 nicht separat verifiziert). Korrigiert durch Prüfung: Beleg hausrat-haftpflicht-police entfernt, da Mobiliar-/Haftpflicht-/Sachversicherungen vom Abzug ausgeschlossen sind.
- **Quellen:**
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Fr. 5’400 für gemeinsam Steuerpflichtige»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Fr. 2’700 für alleinstehende Steuerpflichtige»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Fr. 1’000 zusätzlich für jedes Kind»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Der niedrigere Betrag von (A) und (B) 600 13211 zu übertragen in die Steuererklärung Seite 3 Ziffer 14»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0085.md) `ar-wl-2025__c0085` – «Vom Abzug ausgeschlossen sind die Prämien für Mobiliar-, Motorfahrzeug- und»

<a id="15-abzug-liegenschaft-unterhalt"></a>
### Ziff. 15 – Unterhalts- und Verwaltungskosten Liegenschaften: Pauschalabzug (C1) oder tatsächliche Kosten (C2), Übertrag Formular 7/7Z

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Formular 7 Abschn. C bzw. Formular 7Z Spalte C1/C2
- **Regel:** Wahlrecht je Gebäude und Jahr: Pauschale 10 % (Gebäude bis und mit 10 Jahre) bzw. 20 % (über 10 Jahre) der Liegenschaftserträge (Ziff. B), nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes höchstens Fr. 100'000 beträgt und die Liegenschaft ganz/vorwiegend Wohnzwecken dient; sonst tatsächliche Kosten (Einzelbeträge ab Fr. 5'000 mit Rechnungskopien; Förderbeiträge Dritter abziehen). Pauschale umfasst alle Kosten inkl. Denkmalpflege.
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Pauschalabzug Liegenschaftsunterhalt: 10 % des Bruttomietertrags bei Gebäuden bis 10 Jahre (Wahlrecht je Gebäude und Periode zwischen Pauschale und effektiven Kosten); nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt: 20 % des Bruttomietertrags für ältere Gebäude (über 10 Jahre); nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Bund:** Pauschalabzug und Unterhaltskostenregeln DBSt nicht aus AR-Quellen belegt.
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Siehe auch MB 03 (Liegenschaftsunterhalt ab 2024), nicht im Detail geprüft.
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0003.md) `ar-form-07-2025__c0003` – «Übertrag in die Steuererklärung Seite 3 Ziffer 15»
  - [WL AR 2025 S. 32](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0175.md) `ar-wl-2025__c0175` – «bis und mit 10 Jahre 10 % vom Total Liegenschaftserträge»
  - [WL AR 2025 S. 32](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0175.md) `ar-wl-2025__c0175` – «über 10 Jahre 20 % vom Total Liegenschaftserträge»
  - [WL AR 2025 S. 32](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0175.md) `ar-wl-2025__c0175` – «Bruttomietertrag des gesamten Liegenschaftsbesitzes Fr. 100’000.–»
  - [Formular 7 AR 2025 S. 2](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0004.md) `ar-form-07-2025__c0004` – «Bitte fügen Sie für Einzelbeträge ab Fr. 5’000 die Rechnungskopien»

<a id="16-1-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. 16.1 – Verwaltungskosten Wertschriften/Kapitalanlagen (tatsächlich oder Pauschale)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Depotgebührenausweis der Bank / Steuerauszug (Bestand per 31.12. fremdverwalteter Titel)
- **Regel:** Tatsächliche Depot-/Safegebühren, Inkassospesen oder auf Antrag Pauschale auf dem drittverwalteten Wertschriftenbestand (Total Steuerwerte, ohne eigene Unternehmensaktien, private Darlehen, Geschäftskonti): 3 Promille, max. Fr. 6'000 (bis 2 Mio.); über 2 Mio. 1 Promille, max. Fr. 15'000. Nicht abziehbar: Courtagen, Emissionsabgaben, Anlage-/Steuerberatung, Karten-Gebühren.
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Die Textstelle zur 2-Mio.-Grenze ist über die Chunks c0092-c0094 verteilt (Spalten-Layout), Originalseite 15 prüfen.
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «Fremdverwaltete Wertschriften und Kapitalanlagen 3 ‰, max. jedoch Fr. 6’000»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0089.md) `ar-wl-2025__c0089` – «jedoch Fr. 15’000.–»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0088.md) `ar-wl-2025__c0088` – «vermögen: 1 Promille des drittverwalteten Wertschrif»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0088.md) `ar-wl-2025__c0088` – «die Finanz-, Anlage-, Erbschafts-, Vorsorge- und Steuerberatung»

<a id="16-2-abzug-drittbetreuung"></a>
### Ziff. 16.2 – Kinderbetreuungskosten durch Drittpersonen (Übertrag Formular 10)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Formular 10 Total Kinderbetreuungskosten (Rechnungen Krippe/Tagesfamilie, Empfänger muss ersichtlich sein)
- **Regel:** Nachgewiesene Kosten bis max. Fr. 25'000 pro Kind unter 14 Jahren im gleichen Haushalt, in direktem Zusammenhang mit Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit; Ehepaare in ungetrennter Ehe nur, wenn beide gleichzeitig erwerbstätig bzw. in Ausbildung sind oder erwerbsunfähig und zugleich betreuungsunfähig; Konkubinatspaare analog. Ohne Verpflegung (Lebenshaltungskosten); Betreuungsbeiträge nach Kinderbetreuungsgesetz abziehen. Fahrkosten zur Betreuungsstätte zählen mit.
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 25'000 (Kinderdrittbetreuungskosten: nachgewiesene Kosten max. CHF 25'000 pro Kind.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind bis max. CHF 25'800 (Kind unter 14, im gleichen Haushalt, Zusammenhang mit Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit))**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat (bis zum 14. Geburtstag), im gleichen Haushalt.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat)**
- **Bund:** Bund hat anderen Maximalbetrag (data/werte/bund/2025.yaml).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [Formular 10 AR 2025 S. 1](../../chunks/ar/2025/ar-form-10-2025/ar-form-10-2025__c0001.md) `ar-form-10-2025__c0001` – «jedoch höchstens Fr. 25’000.–, für die Drittbetreuung jedes Kindes, welches das 14. Altersjahr noch nicht vollendet hat»
  - [Formular 10 AR 2025 S. 1](../../chunks/ar/2025/ar-form-10-2025/ar-form-10-2025__c0001.md) `ar-form-10-2025__c0001` – «Total der abziehbaren Kinderbetreuungskosten (exkl. Verpflegung)»
  - [Formular 10 AR 2025 S. 1](../../chunks/ar/2025/ar-form-10-2025/ar-form-10-2025__c0002.md) `ar-form-10-2025__c0002` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 16.2»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0091.md) `ar-wl-2025__c0091` – «tatsächlichen Betreuungskosten sind um die erhaltenen Beiträge zu reduzieren»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0090.md) `ar-wl-2025__c0090` – «Fahrkosten zur Betreuungsstätte gehören ebenfalls»

<a id="16-3-abzug-parteispenden"></a>
### Ziff. 16.3 – Mitgliederbeiträge und Zuwendungen an politische Parteien (Code 555), Übertrag Formular 5 Teil B

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Formular 5 Teil B Total der Parteispenden
- **Regel:** Bis Fr. 10'000 pro Steuererklärung (gemeinsam Veranlagte zusammen) an im Parteienregister eingetragene bzw. im Kantonsparlament vertretene Parteien oder solche mit mind. 3 % Wähleranteil; nicht abziehbar: persönliche Wahlkampfkosten, Komitees, Beiträge direkt an Kandidaten.
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'000 (pro Steuererklärung).)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 10'000 (Gesamtbetrag CHF 10'000 gilt pro Steuererklärung, d.h. auch für gemeinsam Besteuerte (keine Verdoppelung).)** · Bund **n/a – Bund kennt nur einen Gesamtbetrag von CHF 10'600 (Art. 33 Abs. 1 lit. i DBG); keine Verdoppelung für Ehepaare in der Quelle.**
- **Bund:** Bundesmaximum abweichend (data/werte/bund/2025.yaml).
- **Bemerkung:** Code 555 aus Hilfsblatt Form. 5.
- **Quellen:**
  - [Formular 5 AR 2025 S. 2](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0004.md) `ar-form-05-2025__c0004` – «Total der Parteispenden 555 3213211 zu übertragen in die Steuererklärung Seite 3 Ziffer 16.3»
  - [WL AR 2025 S. 16–17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0092.md) `ar-wl-2025__c0092` – «Gesamtbetrag von Fr. 10’000.– (pro Steuererklärung) an politische Parteien»

<a id="16-4-abzug-weiterbildung"></a>
### Ziff. 16.4 – Berufsorientierte Aus- und Weiterbildungskosten inkl. Umschulung, Person 1 / Person 2 (Hauptformular, kein eigenes Hilfsblatt)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Kursrechnungen/Zahlungsbelege der steuerpflichtigen Person; Lohnausweis Ziff. 13.3 (Vergütungen des Arbeitgebers)
- **Regel:** Bis Fr. 12'000 pro Person nur nach erstem Abschluss Sek. II oder ab 20. Altersjahr (ohne Ausbildung bis zum ersten Abschluss); keine Pauschale; vom Arbeitgeber getragene Kosten sind nicht steuerbar und nicht zusätzlich als eigene Kosten abziehbar; dem Arbeitnehmer vergütete Beträge erscheinen im Lohnausweis Ziff. 13.3 (direkt an Dritte bezahlte nicht). Informatikmittel nur bei zwingendem Zusammenhang, bei privater Nutzung 50 %.
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 12'000 (Berufsorientierte Aus- und Weiterbildungskosten (inkl. Umschulung) bis CHF 12'000 pro steuerpflichtige Person.)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Bund:** Bundesmaximum abweichend (data/werte/bund/2025.yaml).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Lohnausweis-Wegleitung gilt für 2026 (jahr_ok), Ziff. 13.3 nur als Feldbeschreibung.
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «Berufsorientierte Aus-/Weiterbildungskosten Person 1 max. Fr. 12’000»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «Nicht anzugeben sind Vergütungen, die direkt an Dritte (z. B. Bildungsinstitut) bezahlt werden»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0034.md) `ar-wl-2025__c0034` – «Nicht steuerbar sind die vom Arbeitgeber getragenen Kosten der berufs»

<a id="16-6-abzug-uebrige"></a>
### Ziff. 16.6 – Übrige Abzüge (AHV-Beiträge Nichterwerbstätiger, Einsatzkosten Geldspiele, nicht im Nettolohn berücksichtigte NBUV-/BVG-Beiträge)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → AHV-Beitragsverfügung; Lohnausweis (NBUV/BVG-Abzüge Ziff. 9/10)
- **Regel:** AHV-Beiträge Nichterwerbstätiger; Einsatzkosten bei steuerbaren Geldspielgewinnen 5 %, max. Fr. 5'400 (Online-Spiele: Spieleinsätze max. Fr. 26'800); NBUV-Beiträge (und gemäss Ziff. 1.1 der WL auch BVG-Beiträge) nur, wenn nicht schon im Nettolohn bzw. Lohnausweis berücksichtigt (Regelfall: schon berücksichtigt -> kein nochmaliger Abzug). Abgrenzung zu Ziff. 13.2 siehe dort (WL widersprüchlich).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Ziff. 16.5 im Formular nicht beschrieben.
- **Quellen:**
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0094.md) `ar-wl-2025__c0094` – «Beiträge von nichterwerbstätigen steuerpflichtigen Personen (ordentliche»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0094.md) `ar-wl-2025__c0094` – «können 5 Prozent, jedoch höchstens Fr. 5’400.–, als Einsatzkosten»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0094.md) `ar-wl-2025__c0094` – «unter dieser Ziffer abgezogen werden»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0035.md) `ar-wl-2025__c0035` – «bzw. im Lohnausweis nicht bereits abgerechnet sind, können unter der Ziffer 16.6 abgezogen werden»

<a id="16-7-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 16.7 – Abzug Teilbesteuerung Beteiligungserträge (40 % der Erträge Ziff. 4.2)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Berechnung aus Ziff. 4.2 (Privatbeteiligungen ab 10 %)
- **Regel:** Erträge aus Beteiligungen ab 10 % sind nur zu 60 % steuerbar: Abzug = 40 % des in Ziff. 4.2 deklarierten Bruttoertrags (Abzug steht in Ziff. 16.7).
- **Bund:** Teilbesteuerungsquote DBSt: eigene Regelung (nicht aus AR-Quellen).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). 40 %-Satz ist die Ergänzung zu den belegten 60 % steuerbar.
- **Quellen:**
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0095.md) `ar-wl-2025__c0095` – «Der entsprechende Abzug für das Teilbesteuerungsverfahren kann auf der Seite 3, Ziffer 16.7, in Abzug gebracht»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0095.md) `ar-wl-2025__c0095` – «sind im Umfang von 60 Prozent steuerbar, wenn diese Beteili»

<a id="17-abzug-zweiverdiener"></a>
### Ziff. 17 – Zweiverdienerabzug (gemeinsam veranlagte, beide erwerbstätig)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechnung aus den beiden Nettoerwerbseinkommen
- **Regel:** 10 % des niedrigeren Erwerbseinkommens (nach allen damit zusammenhängenden Abzügen: Berufskosten, 3a, BVG-Einkauf), mind. Fr. 2'500, max. Fr. 5'200; unter Fr. 2'500: Abzug in Höhe des niedrigeren Einkommens; bei Fr. 0 kein Abzug. Bei Mitarbeit im Geschäft des Partners Einkommen hälftig aufteilen.
- **Limiten:**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **10 % (Zweiverdienerabzug: 10 % des niedrigeren Erwerbseinkommens bei ungetrennter Ehe, mindestens CHF 2'500, höchstens CHF 5'200.)** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (bei Ehegatten in ungetrennter Ehe mit beidseitigem Erwerbseinkommen))**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **CHF 2'500 (Zweiverdienerabzug Minimum CHF 2'500 (indexiert per 1.1.2024).)** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum)**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **CHF 5'200 (Zweiverdienerabzug Maximum CHF 5'200 (indexiert per 1.1.2024).)** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum)**
- **Bund:** Bund: anderer Zweiverdienerabzug (data/werte/bund/2025.yaml).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Gesetz (Art. 35 lit. h StG): Erwerbseinkommen = Einkünfte abzüglich Aufwendungen Art. 29-33 und allgemeine Abzüge Art. 35 lit. d-f; Betragsgrenzen 2'500/5'200 gemäss Anhang 1 (Gesetzestext nennt unindexiert 2'400/5'000).
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) `ar-wl-2025__c0004` – «Bei gemeinsamer Steuerpflicht, bei Erwerbstätigkeit beider Personen max. Fr. 5’200»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) `ar-wl-2025__c0004` – «abzug 10 %, mindestens Fr. 2’500»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0097.md) `ar-wl-2025__c0097` – «einkommens, jedoch mindestens Fr. 2’500.– und höchstens Fr. 5’200.–»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0096.md) `ar-wl-2025__c0096` – «abzüglich aller damit zusammenhängenden Abzüge»
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t3.md) `ar-stg__art-35-t3` – «vom niedrigeren Erwerbseinkommen, das ein Ehegatte unabhängig vom Beruf, Geschäft oder Gewerbe des anderen Ehegatten erzielt, 10 Prozent»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben inkl. Kryptowährungen (Code 300), Übertrag Formular 2

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 Total Steuerwert per 31.12.2025 (Spalte 'Steuerwert am 31. Dezember 2025'); Steuerauszug (eCH-0196)
- **Regel:** Stand per 31.12.2025; kotierte Wertpapiere: offizieller Steuerwert am Ende des Jahres 2025 gemäss Kursliste der ESTV; Kryptowährungen mit erfassen; Bestandesveränderungen (Erwerb, Veräusserung, Rückzahlung, Konversion) mit Datum des Zu- oder Abganges und Bankbelegen.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 30.1 Seite 2 Ziffer 4.1»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0113.md) `ar-wl-2025__c0113` – «gen Kapitalanlagen sind im Wertschriften- und Guthabenverzeichnis (Formular 2)»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «300 213213211»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0128.md) `ar-wl-2025__c0128` – «rungen wie Bitcoin, Ether etc.).»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0128.md) `ar-wl-2025__c0128` – «oder Abganges anzugeben und die Bankbelege beizulegen.»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0128.md) `ar-wl-2025__c0128` – «Massgebend ist in der Regel»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0134.md) `ar-wl-2025__c0134` – «Dieser kann der Kursliste der Eidg. Steuerverwaltung entnommen werden.»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 302)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Aufstellung/Bewertung zum Verkehrswert per 31.12.
- **Regel:** Inländisches und ausländisches Bargeld sowie Gold/Edelmetalle zum Verkehrswert (ESTV-Kursliste).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0113.md) `ar-wl-2025__c0113` – «30.2 Unter dieser Ziffer sind nebst dem inländischen Bargeld auch das ausländische»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «302»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen mit Rückkaufswert (Code 304) mit Versicherungsgesellschaft, Abschluss-/Ablaufjahr, Versicherungssumme

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Steuerwertbescheinigung der Versicherungsgesellschaft (Rückkaufswert + Überschussguthaben)
- **Regel:** Steuerwert = Rückkaufswert + Überschussguthaben/Gewinnbeteiligung; Rentenversicherungen mit aufgeschobener Rente ebenfalls; Rückkaufswert laufender Renten wird als Vermögen besteuert; Bescheinigung beilegen. Ansprüche gegenüber Einrichtungen der beruflichen Vorsorge (2. Säule) und aus gebundener Selbstvorsorge (Säule 3a) sind bis zur Fälligkeit steuerfreies Vermögen.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0114.md) `ar-wl-2025__c0114` – «wert (= Rückkaufswert + Überschussguthaben/Gewinnbeteiligung)»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «304 213213211 306»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0111.md) `ar-wl-2025__c0111` – «gebundener Selbstvorsorge (Säule 3a) stellen bis zu ihrer Fälligkeit steuerfreies»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge mit Art, Kaufpreis, Erwerbsjahr (Code 306)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg, Motorfahrzeug-Versicherungspolice (Haftpflicht/Kasko) und Verkehrssteuer-Rechnung → Kaufbeleg/Fahrzeugausweis (Anschaffungswert, Erwerbsjahr)
- **Regel:** Steuerwert = Anschaffungswert abzüglich 20 % pro Jahr seit Erwerb (inkl. Steuerjahr).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0114.md) `ar-wl-2025__c0114` – «Wertverminderung von 20 Prozent vom Anschaf»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «304 213213211 306»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Anteil an unverteilter Erbschaft (Code 308), mit Aufstellung

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Inventar und Erbenverzeichnis (Kopie beilegen)
- **Regel:** Sämtliche Ansprüche eines Erben/Vermächtnisnehmers an einem ungeteilten Nachlass (auch Nutzniessung Dritter); auch bei noch nicht feststehenden Anteilen; Bewertung nach Ziff. 30/31; Liegenschaftsanteile im Formular 7; zusätzlich Form. 2 Seite 1 (Code 961).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0115.md) `ar-wl-2025__c0115` – «Der Anteil an einer unverteilten Erbschaft umfasst sämtliche Ansprüche»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «308 213213»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «Sind Sie an einer unverteilten Erbschaft beteiligt?»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «13213211 961»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «Diese sind im Liegenschaftsformular 7 zu deklarieren.»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte (Boote, Reitpferde, Kunstsammlungen u.a.) (Code 310)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Aufstellung der Vermögenswerte mit Verkehrswert
- **Regel:** Mutmasslicher Verkehrswert; Hausrat und persönliche Gebrauchsgegenstände sind steuerfrei, nicht deklarieren.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0116.md) `ar-wl-2025__c0116` – «Für die Bewertung der übrigen Vermögenswerte ist in der Regel der mutmassli»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «310 213213»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0111.md) `ar-wl-2025__c0111` – «Nicht anzugeben sind der Hausrat und die persönlichen Gebrauchsgegen»

<a id="31-vermoegen-liegenschaften"></a>
### Ziff. 31 – Liegenschaften, Steuerwert (Code 710), Übertrag Formular 7 Abschn. A / 7Z

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Formular 7 Abschn. A Steuerwert; amtliche Schätzung (vom Grundbuchamt eröffnet)
- **Regel:** AR: amtlicher Verkehrs-/Ertragswert gemäss Schätzung; andere Kantone: dortiger Steuerwert; Ausland: mutmasslicher Verkehrswert. Neu-/Anbauten ohne Schätzung: Zuschlag 80 % der Baukosten. Pro Liegenschaft ein Formular 7, bei mehreren Zusammenzug Form. 7Z.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0001.md) `ar-form-07-2025__c0001` – «Übertrag in die Steuererklärung Seite 4 Ziffer 31»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0117.md) `ar-wl-2025__c0117` – «mitteln und gesamthaft in Ziffer 31 der Steuererklärung zu übertragen»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0165.md) `ar-wl-2025__c0165` – «im Ausland gelegene Grundstücke mit dem mutmasslichen»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0165.md) `ar-wl-2025__c0165` – «im Ausmass von 80 Prozent der Neu- oder An»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «710 213213»

<a id="32-1-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.1 – Geschäftskapital in Kollektiv-, Kommandit- und einfachen Gesellschaften (Code 314), mit Aufstellung

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Angaben/Bilanz der Gesellschaft (Anteil am Vermögen)
- **Regel:** Anteil am Vermögen der Gesellschaft; Bewertung wie Ziff. 32 (Einkommenssteuerwert/Buchwert).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Taxonomie hat keinen eigenen Schlüssel für Geschäftsvermögen; Zuordnung zu vermoegen.erbschaften_beteiligungen (Geschäftsvermögen).
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0119.md) `ar-wl-2025__c0119` – «32.1 Für das Geschäftsvermögen in Kollektiv-, Kommandit- oder einfachen Gesell»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «314 213213211»

<a id="32-2-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.2 – Geschäftsaktiven gemäss Schlussbilanz (ohne Liegenschaften) (Code 316)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Schlussbilanz/Zusammenstellung Betriebsvermögen
- **Regel:** Aktiven gemäss letzter Schlussbilanz; Buchwert der Liegenschaften abziehen (Ziff. 31 zum amtlichen Wert); Betriebsschulden im Formular 5 B -> Ziff. 34.2; Wertschriften des Geschäftsvermögens im Formular 2 mit Code G.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0120.md) `ar-wl-2025__c0120` – «32.2 Die Geschäftsaktiven sind der letzten Schlussbilanz oder der erfolgten Zusam»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0107.md) `ar-wl-2025__c0107` – «andit- und 316»

<a id="32-3-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.3 – Vermögen im landwirtschaftlichen Betrieb (Code 318)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Spezielle Landwirte-Formulare (12/14)
- **Regel:** Besondere Erläuterungen zu den Landwirte-Formularen beachten.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0120.md) `ar-wl-2025__c0120` – «32.3 Für die Angaben zum Vermögen im landwirtschaftlichen Betrieb sind die spezi»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 322)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 30-32)
- **Regel:** Summe Ziff. 30.1-32.3.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0107.md) `ar-wl-2025__c0107` – «gemäss b 322»

<a id="34-1-schulden-privat"></a>
### Ziff. 34.1 – Privatschulden (Code 504), Übertrag Formular 5 Teil A

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 5 Teil A Schuld am 31.12.2025 (Total); Hypothekar-/Kreditbestätigung
- **Regel:** Schuldbestand per 31.12.2025 je Gläubiger; Solidar-/Bürgschaftsschulden nur soweit selbst zu tragen; Steuerverwaltung kann nähere Angaben verlangen. Zinsen gleiches Formular -> Ziff. 11.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0001.md) `ar-form-05-2025__c0001` – «Total private Schulden und private Schuldzinsen 213213211 13213211»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0121.md) `ar-wl-2025__c0121` – «Als Schulden, die vom Vermögen in Abzug gebracht werden können, werden alle»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0107.md) `ar-wl-2025__c0107` – «504 –»

<a id="34-2-schulden-privat"></a>
### Ziff. 34.2 – Geschäftsschulden (Code 506), Übertrag Formular 5 Teil B

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 5 Teil B Total Geschäftsschulden (per Bilanzstichtag)
- **Regel:** Betriebsschulden per 31.12. bzw. Bilanzstichtag; geschäftliche Schuldzinsen gehören in die Jahresrechnung, nicht in Ziff. 11.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0002.md) `ar-form-05-2025__c0002` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 34.2»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0107.md) `ar-wl-2025__c0107` – «506 –»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Reinvermögen (Code 326)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 33 abzüglich 34)
- **Regel:** Total Vermögenswerte abzüglich Schulden.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «326»

<a id="36-1-vermoegen-sozialabzug"></a>
### Ziff. 36.1 – Sozialabzug alleinstehende Steuerpflichtige (Code 330)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien (Zivilstand 31.12.2025)
- **Regel:** Fr. 75'000 für alleinstehende Steuerpflichtige.
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 75'000 (Steuerfreier Betrag auf dem Reinvermögen: übrige Steuerpflichtige CHF 75'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Bund:** Keine Vermögenssteuer beim Bund.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0122.md) `ar-wl-2025__c0122` – «36.1 für alleinstehende Steuerpflichtige»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0122.md) `ar-wl-2025__c0122` – «Fr. 75’000.– sen am Ende der Steuerperi»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «36.1 Für alleinstehende Personen Fr. 75’000»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «(Ziffer 33 330»
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «für alle übrigen steuerpflichtigen Personen Fr. 75 000.–»

<a id="36-2-vermoegen-sozialabzug"></a>
### Ziff. 36.2 – Sozialabzug gemeinsam steuerpflichtige Ehegatten (Code 332)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien (Zivilstand 31.12.2025)
- **Regel:** Fr. 150'000 für Ehegatten in rechtlich und tatsächlich ungetrennter Ehe (gemeinsam steuerpflichtig); alle übrigen Steuerpflichtigen Fr. 75'000 (Ziff. 36.1).
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 150'000 (Steuerfreier Betrag auf dem Reinvermögen: Ehegatten in ungetrennter Ehe CHF 150'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Bund:** Keine Vermögenssteuer beim Bund.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0122.md) `ar-wl-2025__c0122` – «Fr. 150’000.– also per 31. Dezember 2025»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «36.2 Für gemeinsam steuerpflichtige Personen Fr. 150’000»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «332 –»
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «für Ehegatten, die in rechtlich und tatsächlich ungetrennter Ehe leben, Fr. 150 000.–»

<a id="36-3-vermoegen-sozialabzug"></a>
### Ziff. 36.3 – Sozialabzug je minderjähriges Kind (Code 334)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Seite 1 der Steuererklärung (Kinder, Jahrgang)
- **Regel:** Fr. 25'000 für jedes minderjährige Kind unter der elterlichen Sorge oder Obhut der steuerpflichtigen Person, für das ein Kinderabzug nach Art. 38 StG (Ziff. 23.1-23.3) geltend gemacht werden kann (Jahrgang auf Seite 1 massgebend).
- **Limiten:**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 25'000 (Zusätzlich pro minderjähriges Kind mit Kinderabzug CHF 25'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Bund:** Keine Vermögenssteuer beim Bund.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0122.md) `ar-wl-2025__c0122` – «36.3 für jedes minderjährige Kind»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «36.3 Zusätzlich für jedes minderjährige Kind Fr. 25’000»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «334 –»
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «zusätzlich für jedes minderjährige Kind, das unter der elterlichen Sorge oder Obhut der steuerpflichtigen Person steht»

<a id="36-5-vermoegen-sozialabzug"></a>
### Ziff. 36.5 – Ermässigung auf ausserrhodischen Beteiligungen (Code 335)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Beteiligungsbewertung
- **Regel:** Ermässigung nach Art. 31 StV für ausserrhodische Beteiligungen.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Höhe nicht in den geprüften Quellen.
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0122.md) `ar-wl-2025__c0122` – «36.5 Ermässigung auf ausserrhodischen Beteiligungen (vgl. Art. 31 StV)»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «335 –»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen gesamt (Code 338)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 35 abzüglich 36.1-36.5)
- **Regel:** Reinvermögen abzüglich Sozialabzüge.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «338»

## Hilfsblatt Berufskosten (Form. 4)

<a id="form-4-ziff-1-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.1 – Fahrkosten öffentliche Verkehrsmittel (Code 400 Person 1 / 450 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → ÖV-Abo/Fahrausweise (tatsächliche Kosten); Lohnausweis Feld F
- **Regel:** Tatsächliche ÖV-Kosten (Abo-Preis). Lohnausweis Feld F (unentgeltliche Beförderung/Sammeltransport/vom Arbeitgeber bezahltes GA) angekreuzt -> kein Fahrkostenabzug. Zusammen mit 1.2 und 1.3 begrenzt auf max. Fr. 6'000 (Pendlerabzug, nur Staats-/Gemeindesteuer). Fahrt über Mittag: Fahrkostenabzug höchstens Fr. 3'200 bzw. Fr. 1'600 (entspricht Verpflegung). Bei Geschäftsfahrzeug mit Privatanteil 0,9 %/Monat keine effektiven Fahrkosten.
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 (Pendlerabzug).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **220 Tage (In der Regel höchstens 220 Arbeitstage für Fahrkosten.)** · Bund **n/a – Bund kennt keine Festlegung massgebender Arbeitstage; abziehbar sind die tatsächlichen notwendigen Kosten bis zum Maximalbetrag (Art. 26 Abs. 1 lit. a DBG).**
- **Bund:** DBSt: Fahrkosten-Maximum Fr. 3'300 (Art. 26 Abs. 1 lit. a DBG, vgl. data/werte/bund/2025.yaml, Status agent-geprüft; die ESTV-Wegleitung 2a 2025 nennt abweichend 3'200); die Fr. 6'000 gelten nur für Staats-/Gemeindesteuer. Lohnausweis-Feld F: nach ESTV-Wegleitung Lohnausweis 2026 (Folgejahr, für 2025 nicht bestätigt).
- **Bemerkung:** Codes 400/450 aus Form. 4. Lohnausweis-Wegleitung gilt 2026 (jahr_ok), Regel Feld F in AR-WL 2025 bestätigt.
- **Quellen:**
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0074.md) `ar-wl-2025__c0074` – «Bei Benützung eines öffentlichen Verkehrsmittels (Bahn, Tram, Trolley- oder»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «muss auf dem Lohnausweis Feld F»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «Ein Abzug für die Fahrt zur Arbeit ist deshalb nicht möglich»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0074.md) `ar-wl-2025__c0074` – «zur Arbeit bei den Staats- und Gemeindesteuern auf max. Fr. 6’000.–»
  - [WL Lohnausweis 2026 S. 9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0016.md) `bund-wl-lohnausweis-2026__c0016` – «In die sem Fall ist kein Kreuz im Feld F zu setzen»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0001.md) `ar-form-04-2025__c0001` – «1.1 Öffentliche Verkehrsmittel Datum von bis Weg von nach 400»

<a id="form-4-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.2 – Fahrrad/Kleinmotorrad bis 50 cm3 (gelbes Kontrollschild) (Code 402 / 452)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Pauschale (keine Belege)
- **Regel:** Pauschal bis Fr. 700 pro Jahr; zählt zur Gesamtlimite Fr. 6'000.
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Benützung eines Fahrrades oder Kleinmotorrades: Pauschale bis CHF 700.)** · Bund **CHF 700 (Pauschale pro Jahr für Fahrrad, Motorfahrrad und Motorrad mit gelbem Kontrollschild; tatsächliche Kosten zusätzlich nicht abziehbar)**
- **Bund:** Bund: gleiche Pauschale Fr. 700 (BKV Anhang 2); Gesamtlimite Fr. 6'000 gilt nur kantonal (Bund 3'300).
- **Bemerkung:** Code 402 (Person 1); Person 2 Code 452 aus Form. 4 Rückseite.
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0001.md) `ar-form-04-2025__c0001` – «1.2 Fahrrad, Kleinmotorrad bis 50 cm3 (Kontrollschild mit gelbem Grund) 402»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0074.md) `ar-wl-2025__c0074` – «bis zu Fr. 700.– im Jahr»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Motorräder mit gelbem Kontrollschild | im Jahr | 700.—»

<a id="form-4-ziff-1-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.3 – Privates Motorfahrzeug in begründeten Fällen (Code 404/454); Zwischentotal 1.1-1.3 max. Fr. 6'000 (Code 405/455)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg, Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Fahrtenaufstellung (km, Tage), Begründung (Formular 4 Ankreuzfelder)
- **Regel:** Nur wenn kein ÖV vorhanden oder unzumutbar (Fussweg Haltestelle >15 Min., Krankheit/Gebrechlichkeit, Zeitaufwand ab 60 Min./Tag, Fahrzeugpflicht des Arbeitgebers): Auto Fr. 0.70/km, Motorrad Fr. 0.40/km (2025), in der Regel höchstens 220 Arbeitstage; Zwischentotal 1.1-1.3 max. Fr. 6'000. Ab 2026 Auto Fr. 0.75/km (News 2026; gilt auch für Staats-/Gemeindesteuer).
- **Limiten:**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.70 (Privates Motorfahrzeug in begründeten Fällen: CHF 0.70 pro km.)** · Bund **CHF 0.70 (Privatauto: Abzug pro Fahrkilometer CHF 0.70, nur wenn kein öffentliches Verkehrsmittel verfügbar/zumutbar (Steuerjahr 2025))**
  - Fahrkosten Motorrad – Ansatz pro km (CHF): Kanton **CHF 0.40 (Privates Motorrad (weisses Kontrollschild), sofern Benützung begründet: CHF 0.40 pro km (kantonaler Wert = DBG-Ansatz gemäss Verweis in Art. 15 Abs. 3 StV).)** · Bund **CHF 0.40 (Motorrad mit weissem Kontrollschild: CHF 0.40 pro Fahrkilometer (Steuerjahr 2025))**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 (Pendlerabzug).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **220 Tage (In der Regel höchstens 220 Arbeitstage für Fahrkosten.)** · Bund **n/a – Bund kennt keine Festlegung massgebender Arbeitstage; abziehbar sind die tatsächlichen notwendigen Kosten bis zum Maximalbetrag (Art. 26 Abs. 1 lit. a DBG).**
- **Bund:** DBSt: Fahrkosten-Maximum eigener Betrag (data/werte/bund/2025.yaml); km-Ansätze Auto 0.70/Motorrad 0.40 gleich.
- **Bemerkung:** Codes 404/405 Person 1, 454/455 Person 2 (Form. 4). Km-Ansätze: Verweis auf DBG-Ansatz (kantonale Verweisnorm + BKV-Anhang). Der Wert 2026 (0.75/km) steht in ar-news-2026, nicht für 2025 verwendet. data/werte/ar/2025.yaml führt auto_km 0.70 und motorrad_km 0.40 (Verweis auf DBG-Ansatz).
- **Quellen:**
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0074.md) `ar-wl-2025__c0074` – «je Fahrtkilometer 70 Rappen für Autos, bzw. 40 Rappen für Motorräder, wenn»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0002.md) `ar-form-04-2025__c0002` – «max. Fr. 6'000 405»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0001.md) `ar-wl-2025__c0001` – «Arbeitstage in der Regel höchstens 220 Tage»
  - [MB AR 01 S. 1](../../chunks/ar/dauernd/ar-mb-01/ar-mb-01__c0001.md) `ar-mb-01__c0001` – «ungenügenden Verbindungen mit öffentlichen Verkehrsmitteln oder ungünstigem Fahrplan»
  - [StV AR Art. 15](../../chunks/ar/2025/ar-stv/ar-stv__art-15.md) `ar-stv__art-15` – «gemäss den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen werden»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Autos | pro Fahrkilometer | –.70»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Motorräder mit weissem Kontrollschild | pro Fahrkilometer | –.40»

<a id="form-4-ziff-2-1-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.1 – Mehrkosten auswärtige Verpflegung: Fr. 15 pro Arbeitstag, max. Fr. 3'200 (Code 408 / 458)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis (Felder F/G, Ziff. 15); Arbeitstage
- **Regel:** Nur wenn die Heimkehr zum Mittagessen nicht möglich ist (grosse Entfernung): Fr. 15 pro Hauptmahlzeit, bei regelmässiger auswärtiger Verpflegung max. Fr. 3'200 pro Jahr. Lohnausweis Feld G angekreuzt -> nur Zeile 2.2 (halber Abzug). Nicht kombinierbar mit Schichtarbeit (2.3).
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswärtige Verpflegung CHF 15 pro Tag.)** · Bund **CHF 15 (Mehrkosten auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (i.d.R. Mittagessen); ausschliesslich Pauschale, wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Mehrkosten auswärtige Verpflegung höchstens CHF 3'200 pro Jahr.)** · Bund **CHF 3'200 (Bei ständiger auswärtiger Verpflegung CHF 3'200 pro Jahr (voller Abzug))**
- **Bund:** DBSt: Verpflegung Fr. 15/3'200 gleich (data/werte/bund/2025.yaml).
- **Bemerkung:** Code 408 Person 1, 458 Person 2. Verweis auf DBG-Ansatz (kantonale Verweisnorm + BKV-Anhang).
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0003.md) `ar-form-04-2025__c0003` – «Pro Arbeitstag Fr. 15 / im Jahr Fr. 3'200 408»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0076.md) `ar-wl-2025__c0076` – «mässiger auswärtiger Verpflegung (Mittagessen) Fr. 3’200.– im Jahr»
  - [StV AR Art. 16](../../chunks/ar/2025/ar-stv/ar-stv__art-16.md) `ar-stv__art-16` – «nach den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen werden»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Voller Abzug | pro Hauptmahlzeit bzw. Tag | 15.—»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «im Jahr | 3200.—»

<a id="form-4-ziff-2-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.2 – Verpflegung durch Arbeitgeber verbilligt (Kantine, Lunch-Checks, Beitrag): Fr. 7.50 pro Tag, max. Fr. 1'600 (Code 410 / 460)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten)
- **Regel:** Lohnausweis Feld G angekreuzt (Kantine, Lunch-Checks, Arbeitgeberbeitrag) -> in der Regel nur halber Abzug Fr. 7.50 pro Tag, max. Fr. 1'600 pro Jahr; bei so weit gehender Verbilligung, dass keine Mehrkosten gegenüber Zuhause entstehen: kein Abzug.
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Bei Kantinenverpflegung oder Arbeitgeberbeitrag CHF 7.50 pro Tag.)** · Bund **CHF 7.50 (Halber Abzug CHF 7.50 pro Hauptmahlzeit, wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei Kantinenverpflegung oder Arbeitgeberbeitrag höchstens CHF 1'600 pro Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: CHF 1'600 pro Jahr)**
- **Bund:** DBSt: gleiche Halbierung bei Feld G (Werte siehe data/werte/bund/2025.yaml).
- **Bemerkung:** Code 410 Person 1, 460 Person 2. Lohnausweis-Wegleitung gilt 2026 (jahr_ok). Verweis auf DBG-Ansatz (kantonale Verweisnorm + BKV-Anhang).
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0003.md) `ar-form-04-2025__c0003` – «Pro Arbeitstag Fr. 7.50 / im Jahr Fr. 1'600 410»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0076.md) `ar-wl-2025__c0076` – «pro Tag, Fr. 1’600.– im Jahr) zulässig. In diesem Fall ist auf dem Lohnausweis Feld G angekreuzt»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0076.md) `ar-wl-2025__c0076` – «kann kein Abzug gewährt werden»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer Lunch-Checks»
  - [StV AR Art. 16](../../chunks/ar/2025/ar-stv/ar-stv__art-16.md) `ar-stv__art-16` – «Nur der halbe Abzug ist zulässig, wenn die Verpflegung in einem Personalrestaurant eingenommen werden kann»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Halber Abzug | pro Hauptmahlzeit bzw. Tag | 7.50»

<a id="form-4-ziff-2-3-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.3 – Schicht-/Nachtarbeit (durchgehend mind. 8 Std.): Fr. 15 pro Schichttag, max. Fr. 3'200 (Code 412 / 462)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 (Bemerkungen: Anzahl Schichttage)
- **Regel:** Nur bei durchgehender, mindestens achtstündiger Schicht-/Nachtarbeit; Anzahl Schichttage vom Arbeitgeber bescheinigt (Lohnausweis Ziff. 15); nicht zusätzlich zum Abzug 2.1/2.2.
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Schicht- oder Nachtarbeit: CHF 15 pro Tag, max. CHF 3'200 pro Jahr.)** · Bund **CHF 15 (Durchgehende Schicht-/Nachtarbeit (gestaffelte Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich): CHF 15 pro ausgewiesenem Tag, bei ganzjähriger Schicht-/Nachtarbeit CHF 3'200 pro Jahr)**
- **Bund:** DBSt: gleiche Regel (data/werte/bund/2025.yaml).
- **Bemerkung:** Code 412 Person 1, 462 Person 2. Lohnausweis Ziff. 15 laut ESTV-Wegleitung (2026, jahr_ok). Verweis auf DBG-Ansatz (kantonale Verweisnorm + BKV-Anhang).
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0003.md) `ar-form-04-2025__c0003` – «Pro ausgewiesenen Schichttag Fr. 15 / im Jahr Fr. 3'200 412»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0077.md) `ar-wl-2025__c0077` – «Tätigkeit können für jeden Schichttag Fr. 15.–, bei ganzjähriger Schichtarbeit»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0077.md) `ar-wl-2025__c0077` – «Die Anzahl geleisteter Schichttage ist vom Arbeitgeber oder der Arbeitgeberin»
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «die Anzahl im Kalenderjahr geleisteter Schichttage»
  - [StV AR Art. 16](../../chunks/ar/2025/ar-stv/ar-stv__art-16.md) `ar-stv__art-16` – «sowie bei durchgehender Schichtarbeit»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Voller Abzug | pro Hauptmahlzeit bzw. Tag | 15.—»

<a id="form-4-ziff-3-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4 Ziff. 3 – Übrige Berufskosten: Pauschale Fr. 700 + 10 % des Nettolohns, max. Fr. 2'400 (Code 416 / 466) oder tatsächliche Kosten mit Aufstellung (Code 418 / 468)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Ziff. 11 (Nettolohn) für die Pauschale; Kostenaufstellung/Belege bei effektiv
- **Regel:** Pauschale für jede unselbständig erwerbstätige Person; auch bei Taggeldern der ALV sinngemäss. Höhere effektive Kosten nur gegen Nachweis (Beiblatt). Bei nicht ereignisbezogenen Pauschalspesen des Arbeitgebers keine zusätzliche Pauschale. Nebenamtliche Behörden: MB 15. Arbeitszimmer in der Privatwohnung nur, wenn spezifisch eingerichteter Arbeitsplatz ausgeschieden und mindestens 40 % der Tätigkeit (bezogen auf Vollzeit) zu Hause erledigt werden müssen (Art. 18 Abs. 3 StV AR).
- **Limiten:**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Übrige Berufskosten Pauschale: CHF 700 zuzüglich 10 % des Nettolohnes, max. CHF 2'400.)** · Bund **3 % (Übrige Berufskosten: 3 % des Nettolohns (Pauschale; Nachweis höherer Kosten möglich); bei Teilzeit/unterjährig angemessen kürzen)**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockelbetrag der Pauschale (zuzüglich 10 % des Nettolohnes).)** · Bund **n/a – Bund: 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; kein 'fix + %'-Modell.**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Maximum der Pauschale für übrige Berufskosten: CHF 2'400.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
  - Arbeitszimmer/Homeoffice – Regel: Kanton **Kosten eines Arbeitszimmers in der Privatwohnung sind abziehbar, wenn ein spezifisch eingerichteter Arbeitsplatz benötigt und tatsächlich ausgeschieden wird und mindestens 40 % der Tätigkeit (bezogen auf Vollzeit) zu Hause erledigt werden müssen; sonst nur Pauschale übrige Berufskosten bzw. Nachweis höherer Kosten.** · Bund **Privates Arbeitszimmer: nur als Teil der Pauschale 'übrige Berufskosten' bzw. bei Nachweis höherer Kosten abziehbar; Kosten (Miete, Heizung, Beleuchtung) nur, wenn das Zimmer für die Berufsarbeit benützt werden muss. Gelegentliche Arbeit in der Privatwohnung gibt keinen Abzug**
- **Bund:** DBSt: eigene Pauschale 3 % (min./max.) statt Fr. 700 + 10 % (data/werte/bund/2025.yaml).
- **Bemerkung:** Codes 416/418 Person 1, 466/468 Person 2. Pauschale ist kantonal (Art. 18 StV AR, kein Verweis auf DBG-Ansatz); Bund hat 3 %.
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0003.md) `ar-form-04-2025__c0003` – «Pauschalabzug: Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2'400 416»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0003.md) `ar-form-04-2025__c0003` – «Anstelle des Pauschalabzuges: tatsächliche Berufskosten»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0078.md) `ar-wl-2025__c0078` – «Bei Auszahlung nicht ereignis»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0078.md) `ar-wl-2025__c0078` – «3.1 Für diese Aufwendungen kann die steuerpflichtige Person von ihren Einkünf»
  - [StV AR Art. 18](../../chunks/ar/2025/ar-stv/ar-stv__art-18.md) `ar-stv__art-18` – «Fr. 700.– zuzüglich 10 Prozent der Nettoeinkünfte, höchstens aber Fr. 2400.–»
  - [StV AR Art. 18](../../chunks/ar/2025/ar-stv/ar-stv__art-18.md) `ar-stv__art-18` – «mindestens 40 Prozent der Tätigkeit, gemessen an einer Vollzeitbeschäftigung, zu Hause erledigt werden müssen»

<a id="form-4-ziff-4-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4 Ziff. 4 – Wochenaufenthalt: Zimmer (Code 426 / 476), Verpflegung Fr. 30/Tag, max. Fr. 6'400 bzw. Fr. 22.50/Tag, max. Fr. 4'800 (Code 428 / 478)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag/Quittungen des Zimmers; Lohnausweis (verbilligte Mahlzeiten)
- **Regel:** Nur wenn tägliche Rückkehr nicht zumutbar; Zimmer (keine Wohnung) tatsächliche Kosten max. Fr. 800 pro Monat; Verpflegung Fr. 30 pro Tag/max. Fr. 6'400, bei verbilligtem Mittagessen Fr. 22.50/max. Fr. 4'800; Heimkehr-Fahrkosten unter Ziff. 1 (unter Fahrkostenlimite).
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Wochenaufenthalt: Kosten für ein auswärtiges Zimmer je nach Arbeitsort bis max. CHF 800 pro Monat (ortsübliche Mietkosten).** · Bund **Mehrkosten Unterkunft: ortsübliche Auslagen für ein Zimmer (nicht eine Wohnung) abziehbar; Fahrkosten der regelmässigen Heimkehr bis zum Maximalbetrag nach Art. 5 Abs. 1 BKV**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 6'400 (Wochenaufenthalt: auswärtige Verpflegung CHF 30 pro Tag, max. CHF 6'400 pro Jahr (bei Vergünstigung durch Arbeitgeber CHF 22.50/Tag, max. CHF 4'800).)** · Bund **CHF 6'400 (Auswärtiger Wochenaufenthalt: Verpflegung CHF 30 pro Tag, max. CHF 6'400 pro Jahr; bei Verbilligung CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr; Nachweis höherer Kosten ausgeschlossen)**
- **Bund:** DBSt: Wochenaufenthalt-Verpflegung gleich (data/werte/bund/2025.yaml).
- **Bemerkung:** Codes 426/428 Person 1, 476/478 Person 2. Verpflegungspauschalen: Verweis auf DBG-Ansatz (kantonale Verweisnorm + BKV-Anhang). Zimmer: nur ortsübliche Mietkosten (Art. 17 Abs. 2 StV), WL nennt max. Fr. 800 pro Monat.
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0004.md) `ar-form-04-2025__c0004` – «Unterkunft: Ortsübliche Kosten für ein Zimmer Monate à Fr. 426»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0004.md) `ar-form-04-2025__c0004` – «Pro Arbeitstag Fr. 30 / im Jahr Fr. 6'400»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0079.md) `ar-wl-2025__c0079` – «betragen maximal Fr. 800.– pro Monat»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0002.md) `ar-wl-2025__c0002` – «4.2 Für die auswärtige Verpflegung Fr. 30 pro Tag»
  - [StV AR Art. 17](../../chunks/ar/2025/ar-stv/ar-stv__art-17.md) `ar-stv__art-17` – «Mehrkosten der auswärtigen Verpflegung bestimmt sich nach den für die direkte Bundessteuer massgebenden Pauschalansätzen»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Voller Abzug | im Tag im Jahr | 30.— 6400.—»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Gekürzter Abzug | im Tag im Jahr | 22.50 4800.—»

<a id="form-4-ziff-5-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 4 Ziff. 5 – Unselbständiger Nebenerwerb: Pauschale 20 % der Nettoeinkünfte, mind. Fr. 800, max. Fr. 2'400 (Code 432 / 482) oder tatsächliche Kosten (Code 434 / 484)

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 des Nebenarbeitgebers
- **Regel:** Nur bei echtem Nebenerwerb neben vollem Hauptberuf für einen anderen Arbeitgeber; bis Nettolohn Fr. 800: Auslagen bis zur Höhe des Nettolohns; darüber 20 %, mind. Fr. 800, max. Fr. 2'400. Kein Abzug für Pensionierte/Hausfrauen ohne Haupterwerb; in der Regel nicht für VR-Honorare.
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Nebenerwerb: Pauschalabzug 20 % der Nettoeinkünfte (WL: Nettolohn), mind. CHF 800, max. CHF 2'400 (DBG-Ansatz).)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge))**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb Pauschale Minimum CHF 800.)** · Bund **CHF 800 (Minimum Pauschale Nebenerwerb)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb Pauschale Maximum CHF 2'400.)** · Bund **CHF 2'400 (Maximum Pauschale Nebenerwerb)**
- **Bund:** DBSt: eigene Regel Nebenerwerb (data/werte/bund/2025.yaml).
- **Bemerkung:** Codes 432/434 Person 1, 482/484 Person 2. Verweis auf DBG-Ansatz (kantonale Verweisnorm + BKV-Anhang).
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0004.md) `ar-form-04-2025__c0004` – «Pauschalabzug: 20% der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0080.md) `ar-wl-2025__c0080` – «Fr. 800.–, wird in der Regel ohne besonderen Nachweis ein Pauschalabzug von»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0080.md) `ar-wl-2025__c0080` – «Der Abzug ist in der Regel auch nicht zulässig für Einkünfte aus Verwaltungsratstätigkeit»
  - [StV AR Art. 19](../../chunks/ar/2025/ar-stv/ar-stv__art-19.md) `ar-stv__art-19` – «werden die notwendigen Berufskosten nach den für die direkte Bundessteuer massgebenden Pauschalansätzen abgezogen»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «20 % der Nettoeinkünfte, mindestens im Jahr | 800.—»

<a id="form-4-ziff-6-berechnung-total"></a>
### Ziff. Form. 4 Ziff. 6 – Total der Berufskosten (Code 438 Person 1 -> Ziff. 10.1; Code 488 Person 2 -> Ziff. 10.2)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 4 Rechenzeile
- **Regel:** Summe Ziff. 1-5; Übertrag in Seite 3 Ziffer 10.1 (Person 1) bzw. 10.2 (Person 2).
- **Bemerkung:** Code 488 aus Form. 4 Rückseite (Person 2).
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0004.md) `ar-form-04-2025__c0004` – «Total der Berufskosten 438 13211 zu übertragen in die Steuererklärung Seite 3 Ziffer 10.1»
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0008.md) `ar-form-04-2025__c0008` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 10.2»

## Hilfsblatt Wertschriftenverzeichnis (Form. 2)

<a id="form-2-spalten-a-b-vermoegen-wertschriften-guthaben"></a>
### Ziff. Form. 2 Spalten A/B – Verzeichnis der Vermögenswerte: Steuerwert per 31.12.2025 und Bruttoertrag 2025, Spalte A (mit Verrechnungssteuerabzug) / Spalte B (ohne)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Steuerauszug (eCH-0196)/Bankbescheinigung: Valoren-Nr., Stückzahl, Steuerwert per 31.12.2025, Bruttoertrag 2025
- **Regel:** Spalte A: Titel/Guthaben mit 35 % Verrechnungssteuerabzug (u.a. Guthaben mit Bruttozins >Fr. 200, inländische Aktien/Obligationen/Fonds); Spalte B: ohne Verrechnungssteuer (u.a. Kundenguthaben bis Fr. 200 Bruttozins pro Jahr). Code-Abkürzungen: G Geschäftsvermögen, N Nutzniessung, E neuer Titel aus Erbschaft, S aus Schenkung, BP/BG Beteiligung mind. 10 % (Privat-/Geschäftsvermögen). Bisher nicht deklarierte Titel (Selbstanzeige) ausdrücklich als solche bezeichnen.
- **Bemerkung:** Spaltenüberschriften Form. 2 (Seite 2) nicht mit Zeilencodes versehen.
- **Quellen:**
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0005.md) `ar-form-02-2025__c0005` – «Steuerwert am 31. Dezember 2025 Bruttoertrag 2025»
  - [WL AR 2025 S. 26](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0147.md) `ar-wl-2025__c0147` – «In Spalte A sind die Vermögenswerte aufzuführen, deren Erträge der»
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «Total A und B Bruttoertrag»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0128.md) `ar-wl-2025__c0128` – «rungen wie Bitcoin, Ether etc.»
  - [WL AR 2025 S. 27](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0151.md) `ar-wl-2025__c0151` – «Kundenguthaben, deren Bruttozins Fr. 200.– nicht übersteigt;»

<a id="form-2-total-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 2 Total – Verrechnungssteueranspruch 35 % vom Bruttoertrag (Total A) (Code 999)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2 Total A (Rückerstattungsantrag Verrechnungssteuer)
- **Regel:** 35 % des Bruttoertrags Total A (nur Erträge mit abgezogener Verrechnungssteuer); Kollektiv-/Kommanditgesellschaften: Formular 25 direkt bei ESTV.
- **Bemerkung:** Code 999 aus Form. 2.
- **Quellen:**
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A) Fr./Rp. 999»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0004.md) `ar-form-02-2025__c0004` – «Rückerstattung der Verrechnungssteuer mit Formular 25 direkt bei der Eidg. Steuerverwaltung»

<a id="form-2-s-1-960-961-info-schenkungen-erbschaften"></a>
### Ziff. Form. 2 S. 1 (960/961) – Fragen Erbschaften: erhaltene Erbschaft/Vermächtnis (Code 960); Beteiligung an unverteilter Erbschaft mit Erbanteil (Code 961)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Erbteilungsvertrag/Erbteilungsakt (Kopie), Inventar und Erbenverzeichnis
- **Regel:** Fragen sind immer zu beantworten; bei Erbschaft im Jahr 2025 Erblasser, Todestag, Betrag, Teilungsdatum (Erbteilakt beilegen); unverteilte Erbschaft: Erbanteil ohne Liegenschaften (diese in Form. 7), Inventar/Erbenverzeichnis beilegen; Ertrag -> Ziff. 6.2, Vermögen -> Ziff. 30.5.
- **Bemerkung:** Codes 960/961 aus Form. 2. Schlüssel info.schenkungen_erbschaften kommt in dieser Datei zweimal vor (zwei Fragen-Blöcke).
- **Quellen:**
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «Haben Sie im Jahr 2025 eine Erbschaft oder ein Vermächtnis erhalten?»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «Sind Sie an einer unverteilten Erbschaft beteiligt?»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «(Kopie des Erbteilaktes beilegen)»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0132.md) `ar-wl-2025__c0132` – «in der Steuererklärung Ziffer 6.2 (Erträge) bzw. in Ziffer 30.5 (Vermö»

<a id="form-2-s-1-962-963-info-schenkungen-erbschaften"></a>
### Ziff. Form. 2 S. 1 (962/963) – Fragen Schenkungen: Vermögen aus Schenkung/Erbvorbezug erworben (Code 962); Vermögen verschenkt (Code 963)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Schenkungsvertrag/Aufstellung
- **Regel:** Betrag, Datum, Schenker/Beschenkter und Verwandtschaftsgrad angeben; Aufstellung beilegen. Erträge aus geschenkten Titeln: Code S im Verzeichnis.
- **Bemerkung:** Codes 962/963 aus Form. 2.
- **Quellen:**
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0003.md) `ar-form-02-2025__c0003` – «Haben Sie im Jahr 2025 Vermögen aus Schenkung oder Erbvorbezug erworben?»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0003.md) `ar-form-02-2025__c0003` – «(Zusammensetzung: Aufstellung beilegen)»

## Hilfsblatt Schulden/Zuwendungen (Form. 5)

<a id="form-5-teil-a-schulden-privat"></a>
### Ziff. Form. 5 Teil A – Private Schulden (Schuldbestand 31.12.2025) und Schuldzinsen 2025

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Hypothekar-/Kreditbestätigung der Bank: Gläubiger, Schuld per 31.12.2025, Zinsen 2025
- **Regel:** Je Gläubiger Schuld am 31.12.2025 und bezahlte Zinsen 2025; Total Schulden -> Ziff. 34.1, Total Zinsen -> Ziff. 11. Belege nur auf Verlangen einzureichen.
- **Bemerkung:** Beide Totale ohne eigene Codes.
- **Quellen:**
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0001.md) `ar-form-05-2025__c0001` – «Total private Schulden und private Schuldzinsen 213213211 13213211»
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0001.md) `ar-form-05-2025__c0001` – «Seite 3 Ziffer 11»

<a id="form-5-teil-b-schulden-privat"></a>
### Ziff. Form. 5 Teil B – Geschäftsschulden (Schuld am 31.12. bzw. Bilanzstichtag)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz/Schuldenbestätigung
- **Regel:** Nur Schuldbestand; geschäftliche Zinsen sind in der Jahresrechnung enthalten und hier nicht aufzuführen. Total -> Ziff. 34.2.
- **Quellen:**
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0002.md) `ar-form-05-2025__c0002` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 34.2»
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0002.md) `ar-form-05-2025__c0002` – «Total Geschäftsschulden 213213211»

<a id="form-5-s-2-teil-a-abzug-spenden"></a>
### Ziff. Form. 5 S. 2 Teil A – Freiwillige Zuwendungen: Institution, Datum, Betrag; Total (Code 550) -> Ziff. 21.3

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigung der steuerbefreiten Institution (auf Verlangen)
- **Regel:** Je Zuwendung Datum und Betrag; Total -> Ziff. 21.3 (Vorkolonne).
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Zuwendungen nur abziehbar, wenn sie in der Steuerperiode CHF 100 erreichen.)** · Bund **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen (CH) bzw. Gemeinwesen: mindestens CHF 100 im Steuerjahr)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen max. 20 % der um die Aufwendungen gemäss Art. 28-35 verminderten steuerbaren Einkünfte.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Bemerkung:** Code 550.
- **Quellen:**
  - [Formular 5 AR 2025 S. 2](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0003.md) `ar-form-05-2025__c0003` – «Total der Zuwendungen 550 3213211»

<a id="form-5-s-2-teil-b-abzug-parteispenden"></a>
### Ziff. Form. 5 S. 2 Teil B – Parteispenden: Partei, Datum, Betrag; Total (Code 555) -> Ziff. 16.3

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Bestätigung der Partei (auf Verlangen)
- **Regel:** Max. Fr. 10'000 pro Steuererklärung; Total -> Ziff. 16.3.
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'000 (pro Steuererklärung).)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
- **Bemerkung:** Code 555.
- **Quellen:**
  - [Formular 5 AR 2025 S. 2](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0004.md) `ar-form-05-2025__c0004` – «Total der Parteispenden 555 3213211»
  - [WL AR 2025 S. 16–17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0092.md) `ar-wl-2025__c0092` – «Gesamtbetrag von Fr. 10’000.– (pro Steuererklärung)»

## Hilfsblatt Versicherungsprämien/Krankheitskosten (Form. 6)

<a id="form-6-teil-a-abzug-versicherungspraemien"></a>
### Ziff. Form. 6 Teil A – Bezahlte Versicherungsprämien und Sparzinsen: a. Krankenversicherung (brutto), b. Unfallversicherung (ohne NBUV), c. Lebens-/Rentenversicherungen, d. Sparzinsen, e. abzüglich Prämienverbilligungen (Code 600 A)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Prämienrechnung/Jahresbescheinigung Krankenversicherung (brutto), Prämienverbilligungs-Verfügung, Zinsausweis (Sparzinsen gemäss Wertschriftenverzeichnis)
- **Regel:** Familien tragen Prämien/Sparzinsen der ganzen Familie hier ein; Prämienverbilligung (IPV) abziehen; NBUV, Mobiliar-, Haftpflicht-, Motorfahrzeugversicherungen nicht aufführen.
- **Bemerkung:** Code 600 A.
- **Quellen:**
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0001.md) `ar-form-06-2025__c0001` – «Private Krankenversicherung (brutto)»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0001.md) `ar-form-06-2025__c0001` – «abzüglich Prämienverbilligungen»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0001.md) `ar-form-06-2025__c0001` – «Total bezahlte Versicherungsprämien und Sparzinsen 600 A»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0085.md) `ar-wl-2025__c0085` – «Vom Abzug ausgeschlossen sind die Prämien für Mobiliar-, Motorfahrzeug- und»

<a id="form-6-teil-b-c-abzug-versicherungspraemien"></a>
### Ziff. Form. 6 Teil B/C – Maximaler Abzug (Code 600 B): Fr. 5'400 gemeinsam / Fr. 2'700 übrige + Fr. 1'000 je Kind; Abzug = niedrigerer Betrag aus A und B (Code 600) -> Ziff. 14

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeilen
- **Regel:** Siehe Ziff. 14.
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'400 (Versicherungsprämien und Sparzinsen: in ungetrennter Ehe lebende Personen max. CHF 5'400 (abzüglich Prämienverbilligung).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'700 (Versicherungsprämien und Sparzinsen: übrige Steuerpflichtige max. CHF 2'700 (abzüglich Prämienverbilligung).)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag pro Kind (bzw. unterstützte Person mit Abzug nach Art. 38) CHF 1'000.)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
- **Bemerkung:** Code 600 B / 600.
- **Quellen:**
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Fr. 5’400 für gemeinsam Steuerpflichtige»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Total der Abzüge für Versicherungsprämien und Sparzinsen 600 B»

<a id="form-6-s-2-abzug-krankheitskosten"></a>
### Ziff. Form. 6 S. 2 – Krankheits- und Unfallkosten: Rechnungsdatum, Arzt/Zahnarzt/Spital, Bruttobetrag abzüglich Beiträge Dritter = selbst getragene Kosten; Total -> Ziff. 21.1 (Vorkolonne)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Arzt-/Zahnarztrechnungen und KK-Leistungsabrechnung (Vergütungen Dritter)
- **Regel:** Nur selbst getragene Kosten; Selbstbehalt 5 % des Nettoeinkommens wird in der Steuererklärung (Ziff. 21.1) berechnet.
- **Quellen:**
  - [Formular 6 AR 2025 S. 2](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0003.md) `ar-form-06-2025__c0003` – «Hinweis: Abzugsfähig sind die tatsächlich selbst getragenen Kosten»
  - [Formular 6 AR 2025 S. 2](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0003.md) `ar-form-06-2025__c0003` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.1 (Vorkolonne)»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) `ar-wl-2025__c0004` – «Krankheits- und Unfallkosten, Selbstbehalt vom Nettoeinkommen 5%»

<a id="form-6-s-2-behinderungsbedingt-abzug-behinderungskosten"></a>
### Ziff. Form. 6 S. 2 (behinderungsbedingt) – Behinderungsbedingte Kosten (Einzelleistungen); Total -> Ziff. 21.2

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Rechnungen/Verfügungen (Hinweise in der Wegleitung)
- **Regel:** Selbst getragene Kosten ohne steuerlichen Selbstbehalt abziehbar (Vergütungen Dritter sind abzuziehen); Details siehe Ziff. 21.2.
- **Quellen:**
  - [Formular 6 AR 2025 S. 2](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0004.md) `ar-form-06-2025__c0004` – «Behinderungsbedingte Kosten (siehe Hinweise in der Wegleitung)»
  - [Formular 6 AR 2025 S. 2](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0004.md) `ar-form-06-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.2»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0100.md) `ar-wl-2025__c0100` – «können ohne steuerlichen»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0100.md) `ar-wl-2025__c0100` – «Selbstbehalt in Abzug gebracht»

## Hilfsblatt Liegenschaften (Form. 7/7Z)

<a id="form-7-abschn-a-vermoegen-liegenschaften"></a>
### Ziff. Form. 7 Abschn. A – Angaben zur Liegenschaft, Anteil Person 1/2, Nutzung, Baujahr, Steuerwert (Verkehrswert gemäss Grundstückschätzung)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Amtliche Grundstückschätzung (Steuerwert, Grundstücknummer, Baujahr)
- **Regel:** Pro Liegenschaft ein Formular; Baujahr bestimmt Alter (10-Jahres-Grenze Pauschale) am Stichtag der Vermögenssteuer; Zugang/Wegfall im Jahr 2025 mit Datum/Grund; Steuerwert -> Ziff. 31 (bzw. Form. 7Z).
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0001.md) `ar-form-07-2025__c0001` – «Steuerwert in Fr. (Verkehrswert gemäss Grundstückschätzung)»
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0001.md) `ar-form-07-2025__c0001` – «Pro Liegenschaft ist ein separates Formular zu verwenden»

<a id="form-7-abschn-b-a-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 7 Abschn. B a – Eigenmietwert abzüglich 20 % = anrechenbarer Eigenmietwert

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Amtliche Grundstückschätzung (Mietwert)
- **Regel:** Mietwert der letzten amtlichen Schätzung; nicht erfasste Um-/Anbauten +2,8 % der Aufwendungen; Selbstnutzungsabzug 20 % nur am Wohnsitz dauernd selbst bewohnt (nicht Zweit-/Ferienwohnung/Landwirtschaft).
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **20 % (Selbstnutzungsabzug 20 % auf dem Eigenmietwert; nur auf der am Wohnsitz dauernd selbst bewohnten Liegenschaft.)** · Bund **n/a – Eigenmietwert wird nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt (Art. 21 Abs. 2 DBG); Abschaffung per 01.01.2029 beschlossen, 2025–2028 gilt bisheriges Recht. Der Eigenmietwert für die direkte Bundessteuer wird im kantonalen Veranlagungsverfahren festgesetzt; ein dort vorgesehener Abzug für die DBSt (z.B. TG 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0002.md) `ar-form-07-2025__c0002` – «Total anrechenbarer Eigenmietwert»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0166.md) `ar-wl-2025__c0166` – «entspricht dem massgeblichen Mietwert abzüglich 20 Prozent»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0166.md) `ar-wl-2025__c0166` – «2.8 Prozent der Aufwendungen berücksichtigt»

<a id="form-7-abschn-b-b-einkommen-liegenschaften-mietertrag"></a>
### Ziff. Form. 7 Abschn. B b – Erträge Fremdnutzung und Leistungen Dritter (Miet-/Pachtzinsen abzüglich Nebenkosten), inkl. PV-Einspeisevergütung

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Mietverträge/Mietzinsabrechnung, Abrechnung Netzbetreiber
- **Regel:** Netto-Mietzins ohne Nebenkosten; Einspeisevergütung PV steuerbar abzüglich Eigenverbrauch (Netto); Total Erträge a.+b. -> Ziff. 5.
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0002.md) `ar-form-07-2025__c0002` – «Total steuerbare Erträge Fremdnutzung und Leistungen Dritter»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0167.md) `ar-wl-2025__c0167` – «Miet- und Pachtzinsen bei Fremd- nutzung ohne Nebenkosten (Netto-Mietzins)»

<a id="form-7-abschn-c-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 7 Abschn. C – Unterhalts- und Verwaltungskosten: Pauschalabzug (C1) oder tatsächliche Kosten (C2, Rückseite)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Rechnungen (Datum, Rechnungssteller, Beschreibung, Unterhalt/Anlagekosten/Verwaltung)
- **Regel:** Pauschale nur für private, ganz/vorwiegend Wohnzwecken dienende Liegenschaften; tatsächlich: nur selbst bezahlte Kosten (Versicherungsleistungen, Förderbeiträge abziehen), Einzelbeträge ab Fr. 5'000 mit Rechnungskopie; wertvermehrende Anlagekosten nicht abziehbar.
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Pauschalabzug Liegenschaftsunterhalt: 10 % des Bruttomietertrags bei Gebäuden bis 10 Jahre (Wahlrecht je Gebäude und Periode zwischen Pauschale und effektiven Kosten); nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt: 20 % des Bruttomietertrags für ältere Gebäude (über 10 Jahre); nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0003.md) `ar-form-07-2025__c0003` – «Der Pauschalabzug kann nur»
  - [Formular 7 AR 2025 S. 2](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0004.md) `ar-form-07-2025__c0004` – «Bitte fügen Sie für Einzelbeträge ab Fr. 5’000 die Rechnungskopien»
  - [Formular 7 AR 2025 S. 2](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0005.md) `ar-form-07-2025__c0005` – «Total Unterhalts- und Verwaltungskosten (C2)»

<a id="form-7z-vermoegen-liegenschaften"></a>
### Ziff. Form. 7Z – Zusammenzug aller Liegenschaften: Spalten Steuerwert (A) -> Ziff. 31, Erträge (B) -> Ziff. 5, Pauschalabzug (C1) / tatsächliche Kosten (C2) -> Ziff. 15

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Ergebnisse der einzelnen Formulare 7
- **Regel:** Nur bei mehr als einer Liegenschaft; einzelne Totale in die Steuererklärung übertragen.
- **Quellen:**
  - [Formular 7Z AR 2025 S. 1](../../chunks/ar/2025/ar-form-07z-2025/ar-form-07z-2025__c0003.md) `ar-form-07z-2025__c0003` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 31 Seite 2 Ziffer 5 Seite 3 Ziffer 15»
  - [Formular 7Z AR 2025 S. 1](../../chunks/ar/2025/ar-form-07z-2025/ar-form-07z-2025__c0001.md) `ar-form-07z-2025__c0001` – «Bei Besitz von mehr als einer Liegenschaft sind die einzelnen Ergebnisse je Liegenschaft von den Formularen 7 in»

## Hilfsblatt Kinderbetreuung (Form. 10)

<a id="form-10-abzug-drittbetreuung"></a>
### Ziff. Form. 10 – Kinderbetreuungskosten: Rechnungsdatum, Name des Kindes, Empfänger, Kosten; tatsächliche Kosten abzüglich erhaltene Beiträge; Total -> Ziff. 16.2

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Rechnungen Krippe/Tagesfamilie (Empfänger ersichtlich)
- **Regel:** Max. Fr. 25'000 pro Kind unter 14 Jahren; ohne Verpflegung; erhaltene Betreuungsbeiträge abziehen.
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 25'000 (Kinderdrittbetreuungskosten: nachgewiesene Kosten max. CHF 25'000 pro Kind.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind bis max. CHF 25'800 (Kind unter 14, im gleichen Haushalt, Zusammenhang mit Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit))**
- **Quellen:**
  - [Formular 10 AR 2025 S. 1](../../chunks/ar/2025/ar-form-10-2025/ar-form-10-2025__c0001.md) `ar-form-10-2025__c0001` – «Abzüglich erhaltene Beiträge»
  - [Formular 10 AR 2025 S. 1](../../chunks/ar/2025/ar-form-10-2025/ar-form-10-2025__c0002.md) `ar-form-10-2025__c0002` – «Total Kinderbetreuungskosten»
