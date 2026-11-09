---
typ: zuordnung-detail
titel: Zuordnung TG 2026 – Detail
jur: tg
jahre:
- 2026
generiert: tools/build_quick.py aus data/zuordnung/tg/2026.yaml (2026-11-09)
---

# TG 2026: Zuordnung Beleg → Ziffer – Detail

> Kompaktansicht: [quick/zuordnung-tg-2026.md](../../quick/zuordnung-tg-2026.md) · Formular: Steuererklärung 2026 TG (Formular 1, Seiten 1–4) + Hilfsblätter: Form. 2 Wertschriften- und Guthabenverzeichnis, 4.1 Schuldenverzeichnis, 4.2/4.3 Berufsauslagen, 5.1 Krankheit/Unfall/Behinderung, 5.2 Versicherungsprämien, 6 Zuwendungen, 7 Liegenschaftenbesitz, 8 Liegenschaftsunterhalt (Staats-, Gemeinde- und direkte Bundessteuer) · Quelle der Wahrheit: `data/zuordnung/tg/2026.yaml`

## Personalien

<a id="s-1-personalien"></a>
### Ziff. S. 1 – Personalien, Berufs- und Familienverhältnisse am 31.12.2026 (Person 1 / Person 2)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben der Mandantin/des Mandanten (Geburtsdatum, Zivilstand, Beruf, Arbeitgeber, Ergänzungsleistungen ja/nein)
- **Regel:** Stand 31.12.2026 bzw. Ende der Steuerpflicht (Stichtagsprinzip). Bei gemeinsam besteuerten Personen durchgehend dieselbe Person als Person 1 bzw. Person 2 verwenden (Hauptformular und alle Hilfsblätter). Registernummer (AHVN13) auf Formularen und Beilagen angeben.
- **Quellen:**
  - [Formular 1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0002.md) `tg-form-01-2026__c0002` – «Personalien, Berufs- und Familienverhältnisse am 31. Dezember 2026 oder am Ende der Steuerpflicht»
  - [WL TG 2026 S. 12](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0044.md) `tg-wl-2026__c0044` – «Achten Sie bitte darauf, in den Formularen unter Person 1 bzw. Person 2 durchgehend die Angaben»

<a id="s-1-kinder-sozialabzug-kinder"></a>
### Ziff. S. 1 Kinder – Minderjährige, in Ausbildung stehende oder erwerbsunfähige Kinder, deren Unterhalt bestritten wird

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien der Kinder (Geburtsdatum, Haushalt, Schule/Lehrfirma, Ausbildungsende; bei getrennt besteuerten Eltern Alimente/Sorgerecht/Obhut)
- **Regel:** Genaues Geburtsdatum eintragen (Jahrgang entscheidet über die Höhe des Kinderabzugs, Ziff. 25.1). Bei Jahrgang 2007 und älter in Ausbildung: Ausbildungsstätte/Lehrfirma und voraussichtliches Ende der Ausbildung. Bei getrennt besteuerten Eltern zusätzlich Angaben zu Unterhaltsbeiträgen, gemeinsamem Sorgerecht und alternierender Obhut (Zuteilung Kinderabzug/Freibetrag/Drittbetreuung).
- **Limiten:**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 8'500 (Kind in Ausbildung nach Vollendung des 16. Altersjahres (WL 2026: Jahrgang 2007-2010): Fr. 8'500.)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Abzug CHF 6'800 (kein höherer Ausbildungsabzug beim Bund).)**
  - Kinderabzug Schulalter (CHF): Kanton **n/a** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800, keine Staffelung nach Alter; siehe sozialabzug.kind.**
- **Quellen:**
  - [Formular 1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0003.md) `tg-form-01-2026__c0003` – «Minderjährige, in beruflicher Ausbildung stehende oder erwerbsunfähige Kinder, deren Unterhalt Sie bestreiten»
  - [WL TG 2026 S. 12](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0044.md) `tg-wl-2026__c0044` – «Für Kinder mit Jahrgang 2007 und älter, welche sich in Ausbildung befinden, geben Sie bitte»

<a id="s-1-unterst-tzte-sozialabzug-unterstuetzung"></a>
### Ziff. S. 1 Unterstützte – Erwerbsunfähige und unterstützungsbedürftige Personen (ohne aufgeführte Kinder)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Name, Geburtsdatum, Adresse, Haushalt, Unterstützungsbetrag
- **Regel:** Formular nennt als Schwelle jährlicher Beitrag von mindestens Fr. 12'000 (Kanton) bzw. Fr. 6'800 (Bund). Wegleitung Ziff. 25.2 verlangt kantonal nachweislich mindestens 50% des betreibungsrechtlichen Existenzminimums; Bund mindestens Fr. 6'800 (Details siehe Ziff. 25.2).
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'700 (Unterstuetzungsabzug je erwerbsunfaehige und unterstuetzungsbeduerftige Person (nicht Ehegatte/Kind mit Kinderabzug): Fr. 2'700; Voraussetzung: Beitrag zu mehr als 50 % des betreibungsrechtlichen Existenzminimums.)** · Bund **CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)**
- **Quellen:**
  - [Formular 1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0004.md) `tg-form-01-2026__c0004` – «die Sie mit einem jährlichen Beitrag von mindestens Fr. 12 000.– (Kanton) bzw. Fr. 6 800.– (Bund) unterstützen»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0113.md) `tg-wl-2026__c0113` – «Bei der direkten Bundessteuer beträgt der Unterstützungsabzug Fr. 6'800 für jede erwerbsunfähige»

<a id="s-1-unterj-hrige-steuerpflicht-personalien"></a>
### Ziff. S. 1 unterjährige Steuerpflicht – Dauer bei unterjähriger Steuerpflicht – Person 1 / Person 2 (von Tag/Monat bis Tag/Monat)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zuzug-/Wegzugs-/Todesdatum (Angaben des Mandanten)
- **Regel:** Nur bei Steuerpflicht während eines Teils der Steuerperiode ausfüllen. Sozialabzüge für Kinder und unterstützte Personen: Verhältnisse am 31.12.2026 bzw. am Ende der Steuerpflicht massgebend; bei Teilperiode werden sie anteilig nach Dauer der Steuerpflicht gewährt.
- **Quellen:**
  - [Formular 1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0001.md) `tg-form-01-2026__c0001` – «Dauer bei unterjähriger Steuerpflicht»
  - [WL TG 2026 S. 23–24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0106.md) `tg-wl-2026__c0106` – «Besteht die Steuerpflicht nur während eines Teils der Steuerperiode, werden die Sozialabzüge an-»

<a id="s-1-auszahlung-verrechnungssteuer-rueckerstattung"></a>
### Ziff. S. 1 Auszahlung – Steuerrückzahlungen inkl. Rückerstattung der Verrechnungssteuer – Auszahlungskonto (IBAN)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Vorgemerktes Auszahlungskonto bzw. Angaben bei Änderung (Kontoinhaber/in, IBAN, Bank/Post)
- **Regel:** Alle Rückerstattungen der Verrechnungssteuer und allfällige Steuerrückzahlungen erfolgen auf das bezeichnete Konto. Ist kein Konto vorgemerkt oder soll es geändert werden, Felder ausfüllen; bei Bank und Post IBAN angeben. Kontoänderungen nach Einreichung der Steuererklärung unterlassen (Verzögerung).
- **Quellen:**
  - [Formular 1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0005.md) `tg-form-01-2026__c0005` – «Alle Rückerstattungen der Verrechnungssteuer sowie allfälliger Steuerrückzahlungen erfolgen»
  - [WL TG 2026 S. 12–13](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0046.md) `tg-wl-2026__c0046` – «wie auch beim Postkonto die IBAN-Nummer an.»

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Haupterwerbstätigkeit unselbständig – Person 1 (Code 100) / Person 2 (Code 101)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 Nettolohn (Pauschalspesen: Vorspalte; Naturalbezüge/Trinkgelder falls nicht im Lohnausweis)
- **Regel:** Nettolohn gemäss Lohnausweis Ziff. 11 einsetzen (Brutto Ziff. 8 minus AHV/ALV/BVG-Abzüge Ziff. 9 und 10). Pauschalspesen ohne entsprechende Ausgaben sind steuerbar und in die Vorspalte (*) einzutragen. Trinkgelder und nicht im Lohnausweis enthaltene Naturalbezüge zusätzlich deklarieren (volle Verpflegung/Unterkunft in der Regel Fr. 11'880/Jahr). Lohnausweis-Felder: Feld F (Kreuz = keine Arbeitswegkosten) → kein Fahrkostenabzug in Form. 4.2 Ziff. 2; Feld G (Lunch-Checks/Kantine/Personalrestaurant) → nur halber Verpflegungsabzug (Ziff. 3.2); Ziff. 10.2 (BVG-Einkauf, vom Lohn abgezogen) ist im Nettolohn schon berücksichtigt → nicht nochmals in Ziff. 15.2; Ziff. 13.3 (Arbeitgeberbeiträge Weiterbildung) mindern den Weiterbildungsabzug Ziff. 16; Ziff. 15 (Bemerkungen) enthält u.a. Anzahl Schichttage → Form. 4.2 Ziff. 3.1.
- **Bund:** Gleiche Erfassung; Spalten Staat/Bund identisch (Nettolohn Ziff. 11).
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0006.md) `tg-form-01-2026__c0006` – «1.1 Haupterwerbstätigkeit Person 1 100»
  - [WL TG 2026 S. 13](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0049.md) `tg-wl-2026__c0049` – «In die Steuererklärung ist der in Ziffer 11 des Lohnausweises aufgeführte Nettolohn einzusetzen.»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «In diesem Feld ist der für die Steuererklärung massgebende Nettolohn anzugeben.»
  - [WL TG 2026 S. 13](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0049.md) `tg-wl-2026__c0049` – «beträgt der Wert für volle Verpflegung und Unterkunft in der Regel Fr. 11'880 im Jahr»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Nebenerwerbstätigkeit unselbständig – Person 1 (Code 104) / Person 2 (Code 105)

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nebenerwerb) bzw. Honorarabrechnung; Verwaltungsratshonorare, Sitzungsgelder
- **Regel:** Sämtliches Einkommen aus unselbständiger Nebentätigkeit ist unabhängig von der Höhe (auch unter AHV-Freigrenze) zu deklarieren: Behördenentschädigungen, Sitzungs-/Taggelder, VR-Honorare, Tantiemen, Mietzinsreduktion Hauswart (Differenz normaler/reduzierter Mietzins). Pauschalspesen in die Vorspalte. Berufsauslagen Nebenerwerb: Form. 4.2 Ziff. 6.
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Nebenerwerb (unselbstaendig): Pauschale 20 % der Nettoeinkuenfte; sie gilt alle Berufskosten des Nebenerwerbs (Fahrt, Verpflegung, uebrige) ab. Nachweis hoeherer effektiver Kosten vorbehalten; maximal bis Hoehe des Nebenerwerbseinkommens.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)**
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0006.md) `tg-form-01-2026__c0006` – «1.2 Nebenerwerbstätigkeit Person 1 104»
  - [WL TG 2026 S. 13](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0050.md) `tg-wl-2026__c0050` – «Daher ist sämtliches Einkommen aus einer unselbständigen Nebenerwerbstätigkeit»

<a id="1-2-feuerwehr-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 (Feuerwehr) – Sold Milizfeuerwehr (Kernaufgaben) – steuerfrei bis Freibetrag

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis / Soldabrechnung Feuerwehr
- **Regel:** Sold für Kernaufgaben (Übungen, Kurse, Inspektionen, Pikett, Ernstfalleinsätze) ist bis zum Freibetrag steuerfrei; darüber sowie Pauschalzulagen Kader, Funktionszulagen, administrative Arbeiten und Instruktorenentschädigung steuerbar. In der Steuererklärung die bei Staats-/Gemeindesteuern steuerbaren Einkünfte deklarieren; die Korrektur für die Bundessteuer macht die Steuerverwaltung von Amtes wegen.
- **Limiten:**
  - Feuerwehrsold steuerfrei bis (CHF): Kanton **CHF 5'000 (Sold der Milizfeuerwehrleute fuer Kernaufgaben bis Fr. 5'000 jaehrlich steuerfrei (Staats- und Gemeindesteuern); Bund Fr. 5'400 (Korrektur von Amtes wegen).)** · Bund **CHF 5'400 (Sold der Milizfeuerwehrleute für Kernaufgaben steuerfrei bis CHF 5'400 pro Jahr (ausgenommen Pauschalzulagen für Kader, Funktionszulagen, administrative Arbeiten, freiwillige Dienstleistungen); gesamter Sold im Lohnausweis deklarieren.)**
- **Bund:** Freibetrag Bund Fr. 5'400 (statt Fr. 5'000 Kanton); Korrektur von Amtes wegen.
- **Quellen:**
  - [WL TG 2026 S. 13–14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0051.md) `tg-wl-2026__c0051` – «Fr. 5'000 bei der Staats- und Gemeindesteuer;»
  - [WL TG 2026 S. 13–14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0051.md) `tg-wl-2026__c0051` – «Fr. 5'400 bei der direkten Bundessteuer.»

<a id="1-3-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 1.3 – Im vereinfachten Abrechnungsverfahren bereits versteuerter Bruttolohn – Person 1 (Code 106) / Person 2 (Code 107)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der AHV-Ausgleichskasse (Bruttolohnsumme)
- **Regel:** Nur zur Information deklarieren (Vorkolonne); wird nicht in das Zwischentotal Ziff. 6 einbezogen und weder als steuerbares noch als satzbestimmendes Einkommen berücksichtigt. Bescheinigung der Ausgleichskasse beilegen.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0006.md) `tg-form-01-2026__c0006` – «1.3 Im vereinfachten Abrechnungsverfahren bereits versteuerter Bruttolohn»
  - [WL TG 2026 S. 14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0052.md) `tg-wl-2026__c0052` – «Diese Deklaration dient nur zu Informationszwecken.»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Haupterwerbstätigkeit selbständig – Person 1 (Code 112) / Person 2 (Code 113)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz/Erfolgsrechnung bzw. Einnahmen-/Ausgabenaufstellung; Privatkonto; Abschreibungstabelle; bei Kollektiv-/Kommanditgesellschaft Bescheinigung der Gesellschaft
- **Regel:** Steuerbares selbständiges Erwerbseinkommen (Spalte Kanton; bei Beteiligungen nach Teilbesteuerung/Formular 14) eintragen; wenn negativ mit Minuszeichen (*). Naturalbezüge aus dem eigenen Geschäft und Mietwert Wohnung im Geschäftshaus sind steuerbar. Eigene BVG-Beiträge nur Privatanteil als Abzug in Ziff. 15.2 (Arbeitgeberanteil bereits im Geschäftsergebnis). Liquidationsgewinne (ab 55 / Invalidität) sind im Geschäftsergebnis enthalten und werden unter Ziff. 23.3 wieder abgezogen. Bei Bundessteuer wird das Einkommen von Amtes wegen angepasst (Teilbesteuerung).
- **Bund:** Steuerbares Bundeseinkommen kann wegen abweichendem Teilbesteuerungsabzug (Kanton 60%/Bund 70% Einbezug) vom kantonalen abweichen; wird von Amtes wegen aufgenommen.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0006.md) `tg-form-01-2026__c0006` – «2.1 Haupterwerbstätigkeit Person 1 112»
  - [WL TG 2026 S. 17](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0071.md) `tg-wl-2026__c0071` – «In die Steuererklärung ist das in der Spalte Kanton berechnete steuerbare Einkommen zu»
  - [WL TG 2026 S. 14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0055.md) `tg-wl-2026__c0055` – «Führen Sie eine Buchhaltung nach kaufmännischen Grundsätzen, reichen Sie die unterzeichnete»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Nebenerwerbstätigkeit selbständig – Person 1 (Code 116) / Person 2 (Code 117)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Netto-Einkommen aus Nebenerwerb (Honorarabrechnung/Aufstellung); landwirtschaftliches Nebengewerbe: Buchhaltungsabschluss oder Formular 18
- **Regel:** Netto-Einkommen aus selbständigem Nebenerwerb (z.B. Vermittlungsprovisionen, Gutachterhonorare, Buchhaltungsarbeiten, Privatunterricht) deklarieren; Ziff. 2.1 gilt sinngemäss. Gewerbsmässiger Wertpapier- und Liegenschaftenhandel gehört ebenfalls hierher (Detailaufstellung).
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0006.md) `tg-form-01-2026__c0006` – «2.2 Nebenerwerbstätigkeit Person 1 116»
  - [WL TG 2026 S. 17–18](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0072.md) `tg-wl-2026__c0072` – «Deklarieren Sie hier ein Netto-Einkommen aus einer selbständigen Nebenerwerbstätigkeit»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV-/IV-Renten – Person 1 (Code 130) / Person 2 (Code 131)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung AHV/IV (Jahresbetrag brutto)
- **Regel:** Zu 100% steuerbar (Staat und Bund). Ergänzungsleistungen zur AHV/IV sind steuerfrei und nicht anzugeben; ebenso Sozialhilfe und Genugtuungszahlungen.
- **Bund:** Ebenfalls 100% steuerbar.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0007.md) `tg-form-01-2026__c0007` – «3.1 AHV-/IV-Renten Person 1 130»
  - [WL TG 2026 S. 18](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0073.md) `tg-wl-2026__c0073` – «Bundessteuer zu 100% steuerbar.»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen (2. Säule, SUVA, Säule 3a/3b, Leibrenten) – steuerbarer Bruttobetrag und Prozentsatz – Person 1 (Code 132) / Person 2 (Code 133)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Rentenbescheinigung Pensionskasse/SUVA/Versicherung (steuerbarer Betrag und Prozentsatz)
- **Regel:** Renten aus beruflicher Vorsorge, gebundener Selbstvorsorge und Invaliditätsrenten (3b) sind grundsätzlich zu 100% steuerbar. Übergangsbestimmung 80% nur bei mind. 20% Eigenbeiträgen und Rentenbeginn vor 1.1.1987 bzw. 1.1.1987–31.12.2001 (Vorsorgeverhältnis bestand am 31.12.1984; Bund 31.12.1986). Leibrenten: nur Ertragsanteil steuerbar, Überschussleistungen pauschal 70%; die Versicherung weist dies in der Bescheinigung aus (beilegen). Steuerbaren Betrag und Prozentsatz in die zwei Felder eintragen.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0007.md) `tg-form-01-2026__c0007` – «3.2 Renten/Pensionen Steuerbar Bruttobetrag / Fr. in Prozent»
  - [WL TG 2026 S. 18](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0074.md) `tg-wl-2026__c0074` – «Grundsätzlich sind Renten aus beruflicher Vorsorge, aus gebundener Selbstvorsorge sowie Invali-»
  - [WL TG 2026 S. 18](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0075.md) `tg-wl-2026__c0075` – «Überschussleistungen sind pauschal zu 70% steuerbar.»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigungen (Taggelder ALV, KV, UV, IV, SUVA, Mutterschaft, EO) – Person 1 (Code 136) / Person 2 (Code 137)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Taggeldabrechnung/Bescheinigung (ALV, Krankentaggeld, Unfall, EO/Mutterschaft)
- **Regel:** Nur soweit nicht bereits im Lohnausweis bescheinigt und in Ziff. 1 enthalten (sonst doppelt). Dazu zählen auch ALV-Taggelder, SUVA-Taggelder, Mutterschaftsentschädigung und von der Ausgleichskasse direkt bezahlte EO. Soldzahlungen Militär/Zivilschutz/Feuerwehr und Taschengeld Zivildienst sind steuerfrei. Bescheinigung beilegen.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0007.md) `tg-form-01-2026__c0007` – «3.3 Erwerbsausfallentschädigungen»
  - [WL TG 2026 S. 18](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0076.md) `tg-wl-2026__c0076` – «Diese Entschädigungen sind insoweit anzugeben, als sie im Lohnausweis von den Arbeitgebenden»

<a id="3-4-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.4 – Von Ausgleichskassen direkt ausbezahlte Familien-, Kinder- und Haushaltszulagen (Code 140)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Familienausgleichskasse
- **Regel:** Nur direkt von der Ausgleichskasse ausbezahlte Zulagen (selbständig Erwerbende, Nichterwerbstätige, Landwirtschaft); im Lohnausweis enthaltene Kinderzulagen sind bereits im Nettolohn (Ziff. 1.1).
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0007.md) `tg-form-01-2026__c0007` – «3.4 Von Ausgleichskassen direkt ausbezahlte Familien-, Kinder- und Haushaltszulagen 140»
  - [WL TG 2026 S. 18–19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0077.md) `tg-wl-2026__c0077` – «Deklarieren Sie hier von der Ausgleichskasse direkt ausbezahlte Familien- und Haushaltszulagen.»

<a id="4-einkommen-wertschriften"></a>
### Ziff. 4 – Wertschriften- und Zinserträge sowie Gewinne aus Geldspielen (Formular 2, Code 150)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Formular 2 Total steuerbarer Ertrag (Ziff. 9)
- **Regel:** Erträge zuerst im Wertschriften- und Guthabenverzeichnis (Formular 2) erfassen, das Total steuerbarer Ertrag aus Ziff. 9 übertragen. Auch steuerbare Geldspielgewinne hier (nicht unter Ziff. 5).
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «4. Wertschriften- und Zinserträge sowie Gewinne aus Geldspielen Formular 2 150»
  - [WL TG 2026 S. 18–19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0077.md) `tg-wl-2026__c0077` – «Wertschriften- und Gut-»

<a id="5-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.1 – Unterhaltsbeiträge von Ehefrau/-mann bzw. Partner/in bei Trennung/Scheidung (Code 160)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Urteil/Vereinbarung, Zahlungsnachweise; Name und Adresse der zahlenden Person
- **Regel:** Periodische Unterhaltsbeiträge für die eigene Person sind steuerbar (inkl. Mietwertanteil bei Überlassung eines Liegenschaftsanteils). Name/Adresse der zahlenden Person auf der Zeile unter Ziff. 5.1 angeben.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «5.1 Unterhaltsbeiträge von Ehefrau/-mann bzw. Partnerin/Partner bei Trennung/Scheidung/Auflösung Partnerschaft»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0078.md) `tg-wl-2026__c0078` – «Steuerbar sind periodische Unterhaltsbeiträge der Ehefrau oder des Ehemanns bzw. der Partne-»

<a id="5-2-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.2 – Unterhaltsbeiträge für minderjährige Kinder (Code 162)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Urteil/Vereinbarung, Zahlungsnachweise; Name und Adresse der zahlenden Person
- **Regel:** Periodische Beiträge inkl. Kinderzulagen für Kinder unter elterlicher Sorge sind steuerbar. Bei unregelmässigen Zahlungen die 2026 tatsächlich überwiesenen Beträge; Alimentenbevorschussung vermerken. Ab dem Folgemonat der Volljährigkeit nicht mehr steuerbar.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «5.2 Unterhaltsbeiträge für minderjährige Kinder»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0079.md) `tg-wl-2026__c0079` – «Ab dem Folgemonat der Volljährigkeit des Kindes sind die Un-»

<a id="5-3-einkommen-erbschaften-unverteilt"></a>
### Ziff. 5.3 – Ertrag aus unverteilten Erbschaften (Formular 3, Code 164)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung der Erbengemeinschaft/Formular 3
- **Regel:** Einkünfte anteilig nach Erbquote; gleiches gilt für das Vermögen (Ziff. 30.5). Steuerpflicht für die Anteile beginnt am Folgetag des Todestags der erblassenden Person.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «5.3 Ertrag aus unverteilten Erbschaften Formular 3 164»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0080.md) `tg-wl-2026__c0080` – «Einkünfte aus unverteilten Erbschaften werden den erbenden Personen entsprechend ihrer»

<a id="5-4-einkommen-uebrige"></a>
### Ziff. 5.4 – Weitere Einkünfte (Urheberrechte, Lizenzen, Patente, Nutzniessung, Wohnrecht, Lidlohn; Code 168)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung/Vertrag; nähere Bezeichnung auf der Zeile
- **Regel:** Wohnrecht mit dem Mietwert einer vergleichbaren Wohnung bewerten; Untervermietung netto (nach Abzug Mietzinsanteil und Nebenkosten); Lidlöhne, Entschädigungen für Konkurrenzverbot/Rechtsverzicht. Steuerpflichtige Geldspielgewinne gehören dagegen in Ziff. 4.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «5.4 Weitere Einkünfte (z.B. Urheberrechte, Lizenzen, Patente, Wohnrecht usw.)»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0081.md) `tg-wl-2026__c0081` – «Ebenfalls hier anzugeben sind Einkünfte aus Nutzniessung und unentgeltlichem Wohn-»

<a id="5-5-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 5.5 – Kapitalabfindung für wiederkehrende Leistungen für … Jahre (Code 170)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung/Vertrag; Zeitraum in Jahren angeben
- **Regel:** Z.B. Rentenrückkauf, Lidlohnansprüche: Zeitraum angeben, für den die Abfindung ausgerichtet wird (Besteuerung zum Satz einer entsprechenden jährlichen Leistung). Kapitalleistungen aus Vorsorge gehören NICHT hierher, sondern auf Seite 4 unten.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «5.5 Kapitalabfindung für wiederkehrende Leistungen für Jahre 170»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0083.md) `tg-wl-2026__c0083` – «Nicht in Ziffer 5.5, sondern auf der Steuererklärung, Seite 4 unten, sind Kapitalleistungen aus Vor-»

<a id="6-berechnung-total"></a>
### Ziff. 6 – Zwischentotal der Einkünfte (Code 175)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 1 bis 5.5)
- **Regel:** Summe der Ziffern 1 bis 5.5; negatives Ergebnis mit Minuszeichen. Ohne Liegenschaften (und ohne Einkommen aus Geschäftsfahrzeug-Besitz) direkt in Ziff. 20 übertragen, sonst über Ziff. 7 und 8 zu Ziff. 9.
- **Bemerkung:** Die Wegleitung spricht von «Ziffer 6.1/6.2»; das Formular 1 (2026) enthält nur Ziff. 6 (Code 175), 7 und 8.1 – Abweichung Wegleitungstext vs. Formular beachten.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «6. Zwischentotal der Einkünfte 175»
  - [WL TG 2026 S. 19–20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0084.md) `tg-wl-2026__c0084` – «Zwischentotal der Einkünfte»

<a id="7-berechnung-total"></a>
### Ziff. 7 – Übertrag von Ziffer 6 (Staatssteuer / Bundessteuer)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Übertrag des Zwischentotals Ziff. 6 in beide Spalten (Staat/Bund), falls Liegenschaften vorhanden.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0009.md) `tg-form-01-2026__c0009` – «7. Übertrag von Ziffer 6»
  - [WL TG 2026 S. 19–20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0084.md) `tg-wl-2026__c0084` – «Danach füllen Sie die Ziffern 7 und/oder 8 aus.»

<a id="8-1-einkommen-liegenschaften-mietertrag"></a>
### Ziff. 8.1 – Einkünfte aus Liegenschaften (Formular 7, Code 180)

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Formular 7 Total Nettoerfolge (Spalte Staatssteuer / Bundessteuer)
- **Regel:** Total Nettoerfolge aus Formular 7 (Eigenmietwert und Mieterträge abzüglich Unterhalts- und Betriebskosten) getrennt für Staats- und Bundessteuer übertragen (Eigenmietwert-Abzug 40% Kanton / 20% Bund führt zu unterschiedlichen Beträgen).
- **Bund:** Nettoerfolg einzeln pro Ebene (Selbstnutzungsabzug 40% Kanton / 20% Bund).
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0009.md) `tg-form-01-2026__c0009` – «8.1 Einkünfte aus Liegenschaften Formular 7 180»
  - [WL TG 2026 S. 51–52](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0242.md) `tg-wl-2026__c0242` – «Total der Nettoerfolge der Spalte Staatssteuer und Bundessteuer in die»

<a id="9-berechnung-total"></a>
### Ziff. 9 – Total der Einkünfte (Code 198) – Übertrag auf Seite 3, Ziffer 20

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Summe Ziff. 7 + 8 je Spalte (Staat/Bund); Übertrag in Ziff. 20.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0009.md) `tg-form-01-2026__c0009` – «9. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 20 198»

## Abzüge

<a id="10-1-10-2-berechnung-total"></a>
### Ziff. 10.1 / 10.2 – Berufsauslagen bei unselbständiger Erwerbstätigkeit – Person 1 (Formular 4.2, Code 240) / Person 2 (Formular 4.3, Code 280)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Form. 4.2 bzw. 4.3 Ziff. 7 Total der abzugsfähigen Berufsauslagen
- **Regel:** Total Ziff. 7 des Hilfsblatts in die linke Spalte (Staatssteuer) und rechte Spalte (Bundessteuer) übertragen; die Beträge können sich unterscheiden (Fahrkostenmaximum, Autoansatz).
- **Bund:** Rechte Spalte Bund: eigene Fahrkostenberechnung (Fr. 3'300 max.).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «10.1 Person 1 Formular 4.2 240»
  - [WL TG 2026 S. 41–42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0195.md) `tg-wl-2026__c0195` – «übertragen Sie diesen Betrag auf Seite 3 der Steuererklärung in die Ziffer 10.1»

<a id="11-abzug-schuldzinsen"></a>
### Ziff. 11 – Schuldzinsen (Formular 4.1, Code 290)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 4.1 Total fällige Schuldzinsen (Zusammenzug C, Code 290)
- **Regel:** Nur 2026 fällig gewordene Zinsen (keine Ratazinsen); mit der Schlussrechnung belastete Ausgleichszinsen abziehbar; WEF-Zusatzverbilligungen mindern die Schuldzinsen. Private Schuldzinsen höchstens im Umfang der deklarierten Erträge aus beweglichem und unbeweglichem Vermögen plus Fr. 50'000. Amortisationen, Baukreditzinsen, Leasingzinsen nicht abziehbar.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «11. Schuldzinsen Formular 4.1 290»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «Sie können private Schuldzinsen höchstens im Umfang der deklarierten Erträge aus beweglichem»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «und unbeweglichem Vermögen und weiterer Fr. 50 000 in Abzug bringen.»

<a id="12-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.1 – Unterhaltsbeiträge an Ehefrau/-mann bzw. Partner/in bei Trennung/Scheidung (Code 300)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise; Urteil/Trennungsvereinbarung bei erstmaliger Deklaration; Name/Adresse der empfangenden Person
- **Regel:** Nur tatsächlich bezahlte periodische Beiträge, nur mit Zahlungsnachweis. Name und Adresse der empfangenden Person auf den Zeilen unter Ziff. 12. Spiegelbild zu Ziff. 5.1 beim Empfänger.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «12.1 Unterhaltsbeiträge an Ehefrau/-mann bzw. Partnerin/Partner»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0086.md) `tg-wl-2026__c0086` – «Die Abzüge für Unterhaltsbeiträge und Rentenleistungen werden nur gewährt, wenn Zahlungs-»

<a id="12-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.2 – Unterhaltsbeiträge für minderjährige Kinder (Code 302)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise; Urteil/Vereinbarung
- **Regel:** An den anderen Elternteil überwiesene Kinderunterhaltsbeiträge (inkl. Kinderzulagen) für Kinder unter dessen Sorge; längstens bis und mit dem Monat der Mündigkeit. Wer abzieht, hat kantonal keinen Anspruch auf den Kinderabzug.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «12.2 Unterhaltsbeiträge für minderjährige Kinder 302»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0087.md) `tg-wl-2026__c0087` – «Tragen Sie in Ziffer 12.2 die dem andern Elternteil für die unter dessen elterlicher Sorge stehenden»

<a id="12-3-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.3 – Rentenleistungen (Code 304)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rentenvertrag; Beiblatt mit Name/Adresse des Empfängers
- **Regel:** Im Jahr 2026 bezahlte Leibrenten sind zu 40% abziehbar. Umfang der Leistungen auf Beiblatt mit Name/Adresse der empfangenden Person genau bezeichnen.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «12.3 Rentenleistungen 304»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0087.md) `tg-wl-2026__c0087` – «Im Jahr 2026 bezahlte Leibrenten können zu 40% vom Einkommen abgezogen werden.»

<a id="13-1-13-2-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.1 / 13.2 – Beiträge an Säule 3a – Person 1 (Code 314) / Person 2 (Code 315), mit Kästchen «Anschluss 2. Säule (PK)»

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → 3a-Bescheinigung der Bank/Versicherung (Einzahlungen 2026)
- **Regel:** Kästchen «Anschluss 2. Säule» ankreuzen, wenn einer Vorsorgeeinrichtung angeschlossen. Abzug nur mit AHV-pflichtigem Erwerbseinkommen 2026 und nur für die Person, auf die der Vorsorgevertrag lautet. Maximum 2026: mit 2. Säule Fr. 7'258; ohne 2. Säule 20% des Erwerbseinkommens, höchstens Fr. 36'288 (zugleich absolute Einzahlungslimite). Beiträge längstens bis 5 Jahre nach AHV-Alter. Bescheinigung beilegen.
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Saeule 3a 2026: max. Fr. 7'258 fuer Erwerbstaetige mit Anschluss an eine 2. Saeule (Pensionskasse); gleichzeitig absolute Einzahlungslimite.)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug CHF 7'258 pro Jahr für Personen, die einer Vorsorgeeinrichtung der 2. Säule angehören (8 % des oberen Grenzbetrags nach Art. 8 Abs. 1 BVG). Nur im Steuerjahr tatsächlich einbezahlte Beiträge, mit Bescheinigung.)**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Saeule 3a 2026: ohne Anschluss an 2. Saeule 20 % des Erwerbseinkommens, maximal Fr. 36'288.)** · Bund **CHF 36'288 (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens CHF 36'288 pro Jahr.)**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Saeule 3a ohne 2. Saeule: 20 % des Erwerbseinkommens (gilt auch fuer Unselbstaendige ohne Pensionskasse), max. Fr. 36'288.)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (alle Einkünfte aus selbständiger und unselbständiger, haupt- und nebenberuflicher Erwerbstätigkeit), max. CHF 36'288.)**
- **Bund:** Gleiche Höchstbeträge und gleiche Zeile für Staat und Bund.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «13.1 Person 1 Anschluss 2. Säule (PK) m ja 314»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0089.md) `tg-wl-2026__c0089` – «Steuerpflichtige Personen, die einer Einrichtung der beruflichen Vorsorge (2. Säule) angehören Fr. 7'258»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0089.md) `tg-wl-2026__c0089` – «Steuerpflichtige Personen, die keiner Einrichtung der beruflichen Vorsorge (2. Säule) angehören: 20% des Erwerbseinkommens, maximal Fr. 36'288»

<a id="13-1-13-2-einkauf-abzug-vorsorge-saeule3a-einkauf"></a>
### Ziff. 13.1 / 13.2 (Einkauf) – Einkauf in die Säule 3a für frühere Jahre (neu ab 2025; keine eigene Zeile im Formular)

- **Schlüssel:** `abzug.vorsorge.saeule3a_einkauf` (Einkauf (Nachzahlung) Säule 3a – ab Steuerjahr 2026) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → 3a-Einkaufsbescheinigung der Vorsorgeeinrichtung (Einkauf separat ausweisen lassen)
- **Regel:** Neu: wer ab 1.1.2025 nicht jedes Jahr die maximal zulässigen Beiträge einbezahlt hat, kann diese bis zu 10 Jahre rückwirkend nachzahlen. Zusätzlich zum ordentlichen Beitrag pro Jahr maximal der «kleine Beitrag» (2026: Fr. 7'258). Voraussetzungen: AHV-pflichtiges Erwerbseinkommen in der Schweiz im Einkaufsjahr UND im Jahr, für das nachgezahlt wird; ordentlicher Jahresbeitrag des Einkaufsjahres muss vollständig entrichtet sein. Vollumfänglich abzugsfähig. Deklaration gemäss Wegleitung in Ziff. 13.1/13.2 (Formular 1 hat keine separate Einkaufszeile) – Bescheinigung beilegen.
- **Limiten:**
  - Säule 3a – Einkauf (Nachzahlung) Regel/Maximum: Kanton **CHF 7'258 (NEU ab 2025/2026: Einkauf (Nachzahlung) fuer fruehere Jahre bis zu 10 Jahre rueckwirkend; zusaetzlich zum ordentlichen Beitrag pro Jahr max. der kleine Beitrag (2026: Fr. 7'258). Voraussetzung: AHV-pflichtiges Erwerbseinkommen in der Schweiz im Einkaufsjahr und im Nachzahlungsjahr; ordentlicher Jahresbeitrag vollstaendig geleistet. Voll abzugsfaehig.)** · Bund **CHF 7'258 (Einkauf Säule 3a (ab Steuerperiode 2026, für Beitragslücken ab 1.1.2025): zusätzlich zum vollen ordentlichen Beitrag im Einkaufsjahr; max. Summe der Beitragslücken der letzten 10 Jahre (frühestens ab 2025), pro Steuerjahr höchstens CHF 7'258 (8 % des oberen BVG-Grenzbetrags, unabhängig von Zugehörigkeit zur 2. Säule); eine Jahresbeitragslücke nur durch einen einzigen Einkauf ausgleichbar; kein Einkauf nach Bezug einer Altersleistung der Säule 3a (Bezüge ab 5 Jahren vor Referenzalter zählen als Altersleistung).)**
- **Bund:** Gilt gemäss Vorwort der Wegleitung auch bei der direkten Bundessteuer.
- **Bemerkung:** Neuerung ggü. 2025-Wegleitung: Vorwort WL 2026 nennt Einkäufe in Säule 3a neu. Dass der Einkauf in dieselben Felder 13.1/13.2 gehört, folgt aus WL c0091 («Beiträge … in Ziffer 13.1/13.2»); das Formular zeigt keine separate Zeile – bei Unsicherheit Rückfrage Steuerverwaltung.
- **Quellen:**
  - [WL TG 2026 S. 20–21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0090.md) `tg-wl-2026__c0090` – «können diese Beiträge bis zu zehn Jahre»
  - [WL TG 2026 S. 20–21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0090.md) `tg-wl-2026__c0090` – «Zusätzlich zum ordentlichen Beitrag ist pro Jahr ein Einkauf in die Säule 3a in Höhe des soge-»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0091.md) `tg-wl-2026__c0091` – «Tragen Sie die Beiträge in Ziffer 13.1»

<a id="14-abzug-versicherungspraemien"></a>
### Ziff. 14 – Versicherungsprämien und Zinsen von Sparkapitalien (Formular 5.2, Code 330)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 5.2 Teil C (Zeile 1 Staat, Zeile 2 Bund)
- **Regel:** Zulässiger Abzug = niedrigerer Betrag von «A5» (Total Prämien und Sparzinsen) und «B4» (Maximalabzug), getrennt für Staat und Bund. Krankenkassenprämie netto (nach IPV) deklarieren. Maximum Kanton: Fr. 7'000 gemeinsam / Fr. 3'500 übrige; Bund: Fr. 3'700 / Fr. 1'800 (ohne Beiträge an Säule 2/3a Fr. 5'550 / Fr. 2'700); pro Kind/unterstützte Person Kanton Fr. 1'000, Bund Fr. 700.
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 7'000 (Versicherungspraemien (Leben, Kranken, Unfall) und Sparzinsen: max. Fr. 7'000 fuer Verheiratete in ungetrennter Ehe.)** · Bund **CHF 3'700 (Versicherungsprämien und Zinsen von Sparkapitalien, Ehepaare in ungetrennter Ehe, mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 3'700.)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – WL 2026 c0209 und StG § 34 kennen die Erhoehung nur fuer die direkte Bundessteuer.** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an 2. Säule und Säule 3a: Höchstabzug CHF 5'550 (Erhöhung um die Hälfte).)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 3'500 (Versicherungspraemien und Sparzinsen: max. Fr. 3'500 fuer uebrige Steuerpflichtige.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 1'800.)**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – Nur direkte Bundessteuer, siehe WL 2026 c0209.** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: max. CHF 2'700.)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag zum Versicherungsabzug: Fr. 1'000 je minderjaehriges oder in Ausbildung stehendes Kind bzw. unterstuetzte Person (fuer die Kinder-/Unterstuetzungsabzug moeglich ist).)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**
- **Bund:** Eigene Spalte Bund mit tieferen Maxima (Fr. 3'700/1'800; Kind Fr. 700).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «14. Versicherungsprämien und Zinsen von Sparkapitalien Formular 5 330»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0209.md) `tg-wl-2026__c0209` – «für gemeinsam besteuerte Personen Fr. 7'000 Fr. 3'700»

<a id="15-1-abzug-ahv-nichterwerbstaetige"></a>
### Ziff. 15.1 – AHV-Beiträge für nichterwerbstätige Personen (Code 342)

- **Schlüssel:** `abzug.ahv_nichterwerbstaetige` (AHV/IV/EO-Beiträge Nichterwerbstätiger u.ä.) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse) → AHV-Beitragsverfügung/Rechnung Ausgleichskasse
- **Regel:** Nur AHV/IV/EO- sowie FAK-Beiträge von Nichterwerbstätigen. Beiträge von Selbständigen sind im Reingewinn (Ziff. 2) berücksichtigt, solche von Unselbständigen bereits im Nettolohn – dort nicht nochmals abziehen.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «15.1 AHV-Beiträge für nichterwerbstätige Personen 342»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0092.md) `tg-wl-2026__c0092` – «Unter dieser Ziffer können in der Regel nur Beiträge an die AHV/IV/EO sowie FAK-Beiträge von»

<a id="15-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 15.2 – Beiträge an Einrichtungen der beruflichen Vorsorge (PK-Einkauf) – Person 1 (Code 343) / Person 2 (Code 344)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) für direkt bezahlte Einkäufe; Lohnausweis Ziff. 10.2 nur zur Kontrolle
- **Regel:** Nur Einkäufe, die NICHT bereits vom Lohn abgezogen und im Nettolohn (Lohnausweis Ziff. 10.2) berücksichtigt sind: selbst bezahlte Einkaufsbeiträge werden von der Vorsorgeeinrichtung separat bescheinigt. Ordentliche Beiträge (Lohnausweis 10.1) sind im Nettolohn bereits abgezogen. Selbständige: nur Privatanteil (Arbeitgeberanteil bereits im Geschäftsergebnis; ohne Personal gilt die Hälfte als Arbeitgeberanteil).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «15.2 Beiträge an Einrichtungen der beruflichen Vorsorge»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0093.md) `tg-wl-2026__c0093` – «Die ordentlichen Beiträge sind in der Regel bereits vom Bruttolohn abgezogen und daher in Ziffer 1»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «Vom Arbeitnehmer selber entrichtete, d. h. nicht vom Lohn abgezogene Einkaufsbeiträge»

<a id="15-3-abzug-drittbetreuung"></a>
### Ziff. 15.3 – Kosten für die Drittbetreuung von Kindern unter 14 Jahren (Code 345)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Rechnungen/Bestätigung Kita, Tagesfamilie, Hort (echte Betreuungskosten)
- **Regel:** Kumulativ: Kind unter 14, im Haushalt des unterhaltspflichtigen Elternteils, Kosten kausal mit Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit verbunden. Nur echte Betreuungskosten: ohne Gegenbeweis werden in der Regel nur 75% der Rechnung anerkannt (Verpflegung/Unterhalt ausgeschieden). Maximum pro Kind Kanton Fr. 10'100, Bund Fr. 25'800. Getrennt besteuerte Eltern: Anspruch hat der Elternteil, der mit dem Kind zusammenlebt; bei alternierender Obhut je höchstens die Hälfte der Maxima (nur bei hälftiger Zuteilung des Kinderabzugs).
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 10'100 (Kinderdrittbetreuung: nachgewiesene echte Betreuungskosten, max. Fr. 10'100 pro Kind (in der Regel 75 % der Rechnungsbetraege anerkannt, ausser Nachweis ohne Verpflegung/Unterhalt). Alternierende Obhut: je Elternteil max. 50 % (Fr. 5'050) bei haelftiger Zuteilung des Kinderabzugs.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind, höchstens CHF 25'800; Kind unter 14 Jahren im gleichen Haushalt; Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 Jahre (Kind darf das 14. Altersjahr noch nicht vollendet haben; Kind lebt mit dem fuer den Unterhalt sorgenden Elternteil im gleichen Haushalt; kausaler Zusammenhang mit Erwerbstaetigkeit, Ausbildung oder Erwerbsunfaehigkeit. Betreuungsperson muss mind. 16 Jahre alt sein (§ 11c Abs. 2 StV).)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat.)**
- **Bund:** Bund: maximal Fr. 25'800 pro Kind (Wegleitung nennt bei alternierender Obhut «50% von Fr. 25'500» – Schreibfehler/Inkonsistenz in WL c0096 vs. Fr. 25'800 in c0096 erster Absatz).
- **Bemerkung:** Innere Inkonsistenz WL 2026 c0096: Fr. 25'800 (Maximalbetrag) vs. «50% von Fr. 25'500» bei alternierender Obhut. Massgebend wird Fr. 25'800 gesetzt; Fachperson prüft Hälfte bei alternierender Obhut.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «15.3 Kosten für die Drittbetreuung von Kindern unter 14 Jahren 345»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0094.md) `tg-wl-2026__c0094` – «Pro Kind können Sie kantonal die nachgewiesenen echten Kosten für die Drittbetreuung in Abzug»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0094.md) `tg-wl-2026__c0094` – «werden in der Regel daher jeweils nur 75% als echte Drittbetreuungskosten anerkannt.»

<a id="15-4-abzug-uebrige"></a>
### Ziff. 15.4 – Weitere Abzüge – genau bezeichnen (Code 346)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Begründung/Beleg zur Aufstellung (z.B. NBU-Prämien, AHV/IV/EO- und FAK-Beiträge Erwerbstätiger, soweit nicht in Ziff. 1/2 berücksichtigt)
- **Regel:** Geltend gemachte Abzüge begründen und belegen. NICHT hier: Vermögensverwaltungskosten (→ Formular 2), Einsatzkosten für nicht steuerbare Geldspielgewinne (nicht abziehbar), Prämien KVG-Unfallversicherung Nichterwerbstätiger (→ Ziff. 14).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «15.4 Weitere Abzüge: 346»
  - [WL TG 2026 S. 22](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0098.md) `tg-wl-2026__c0098` – «Die geltend gemachten Abzüge sind zu begründen und zu belegen.»

<a id="15-5-abzug-parteispenden"></a>
### Ziff. 15.5 – Mitgliederbeiträge und Zuwendungen an politische Parteien (Formular 6, Code 347)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Formular 6 (Spalte politische Parteien); Quittungen ab Fr. 1'000 pro Zuwendung
- **Regel:** Voraussetzung: Partei im Parteienregister eingetragen und in einem kantonalen Parlament vertreten oder ≥3% Stimmen. Maximal Fr. 10'000 (Staat) / Fr. 10'600 (Bund). Einzeln mit Name/Sitz der Partei auflisten; Pauschalvermerke wie «Spenden an diverse Organisationen» werden nicht anerkannt.
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeitraege und Zuwendungen an politische Parteien: max. Fr. 10'000 (Staats- und Gemeindesteuern); Bund Fr. 10'600.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister / kantonales Parlament / mind. 3 % Stimmen): bis Gesamtbetrag CHF 10'600.)**
- **Bund:** Maximalabzug Bund Fr. 10'600.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «15.5 Mitgliederbeiträge und Zuwendungen an politische Parteien Formular 6 347»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0216.md) `tg-wl-2026__c0216` – «Der Maximalabzug beträgt bei den Staats- und Gemeindesteuern Fr. 10 000 und bei der direkten»

<a id="15-6-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 15.6 – Teilbesteuerungsabzug Beteiligungen im Privatvermögen (Formular 2 Hilfsblatt, Code 341)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2, letzte Seite: Hilfsblatt qualifizierte Beteiligungen (Ziff. 3 Teilbesteuerungsabzug)
- **Regel:** Nur auf Antrag über das Hilfsblatt: Beteiligungsquote ≥10% (Voraussetzungen siehe WL). Abzug Kanton 40%, Bund 30% der Beteiligungserträge; in beide Spalten Bund/Kanton übertragen. Beteiligungen im Geschäftsvermögen: Antrag über Formular 14, nicht hier.
- **Bund:** 30% (statt 40% Kanton).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «15.6 Teilbesteuerungsabzug Beteiligungen im Privatvermögen Formular 2 341»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0164.md) `tg-wl-2026__c0164` – «3 einzusetzende Teilbesteuerungsabzug beträgt 40% bei den Staats- und Gemeindesteuern und»

<a id="16-1-16-2-abzug-weiterbildung"></a>
### Ziff. 16.1 / 16.2 – Berufsorientierte Aus- und Weiterbildungskosten – Person 1 (Code 348) / Person 2 (Code 349)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Kursrechnungen/Zahlungsnachweise mit Aufstellung; Lohnausweis Ziff. 13.3 (Arbeitgeberbeiträge)
- **Regel:** Maximal Fr. 13'000 pro Person (Staat und Bund). Erstausbildung (erster Abschluss Sek II) ausgenommen; ohne Sek-II-Abschluss erst ab 20 Jahren. Kostenbeteiligungen Dritter (Arbeitgeber, Bund, Branchenverbände) mindern den Abzug – Lohnausweis Ziff. 13.3 (an den Arbeitnehmer vergütete Beträge) abziehen. IT-Geräte nur bei direktem Bezug zum Lehrgang, Privatanteil in der Regel 50%. Liebhaberei/Selbstentfaltung nicht abzugsfähig. Aufstellung mit Belegen beilegen.
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung: max. Fr. 13'000 pro Person und Jahr (Kanton und Bund); Erstausbildung (Sek. II) ausgenommen; Kostenbeteiligung Dritter mindert.)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildungs- inkl. Umschulungskosten bis CHF 13'000 pro Jahr, sofern erster Abschluss Sek. II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)**
- **Bund:** Gleich: Fr. 13'000 pro Person.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «16.1 Person 1 348»
  - [WL TG 2026 S. 22–23](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0101.md) `tg-wl-2026__c0101` – «auf jährlich maximal Fr. 13'000 pro Person beschränkt.»
  - [WL TG 2026 S. 22–23](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0101.md) `tg-wl-2026__c0101` – «Kostenbeteiligungen Dritter (z.B. Arbeitgebende, Bund, Branchenverbände etc.) mindern die»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «Nicht anzugeben sind Vergütungen, die direkt an»

<a id="17-abzug-behinderungskosten"></a>
### Ziff. 17 – Behinderungsbedingte Kosten (Formular 5.1 Teil C, Code 350)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 5.1 Teil C (Aufwendungen A minus Vergütungen B); Nachweise
- **Regel:** Selbst getragene behinderungsbedingte Kosten für sich und Personen mit Kinder-/Unterstützungsabzug voll abziehbar (kein Selbstbehalt). Vergütungen Dritter, Hilflosenentschädigung und Anteil Lebenshaltungskosten abziehen. Alternativ Pauschalen: gehörlos / Dialyse / Hilflosenentschädigung leicht Fr. 2'500, mittel Fr. 5'000, schwer Fr. 7'500.
- **Bund:** Gleiche Regeln (voll abziehbar).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «17. Behinderungsbedingte Kosten Formular 5 350»
  - [WL TG 2026 S. 42–43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0200.md) `tg-wl-2026__c0200` – «– Bezügerinnen/Bezüger einer Hilflosenentschädigung schweren Grades Fr. 7'500»

<a id="18-abzug-zweiverdiener"></a>
### Ziff. 18 – Zweiverdienerabzug (Code 356)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Berechnung aus Erwerbseinkommen beider Eheleute (Ziff. 1/2 abzüglich Berufsauslagen, BVG, 3a)
- **Regel:** NUR direkte Bundessteuer (Staat: kein Abzug). 50% des niedrigeren Erwerbseinkommens, mindestens Fr. 8'600, höchstens Fr. 14'100; liegt das niedrigere Erwerbseinkommen unter Fr. 8'600, nur dieser Teilbetrag.
- **Limiten:**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **n/a – StP 34 Nr. 25: 'Im Gesetz ... ist kein Zweiverdienerabzug vorgesehen' (tg-stp-34-25__c0001); WL 2026 c0103.** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (Ehepaare in ungetrennter Ehe, beide erwerbstätig).)**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **n/a** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum.)**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **n/a** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum.)**
- **Bund:** Nur Bund (Fr. 8'600–14'100); bei Staats-/Gemeindesteuern gibt es keinen Zweiverdienerabzug.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «18. Zweiverdienerabzug 356»
  - [WL TG 2026 S. 23](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0103.md) `tg-wl-2026__c0103` – «Der Abzug beläuft sich auf mindestens Fr. 8'600 und höchstens Fr. 14'100.»

<a id="19-berechnung-total"></a>
### Ziff. 19 – Total Abzüge (Code 360) – Übertrag in Ziffer 21

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 10 bis 18)
- **Regel:** Summe der Abzüge Ziff. 10.1 bis 18, getrennt Staat/Bund; Übertrag in Ziff. 21.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «19. Total Abzüge, zu übertragen in Ziffer 21 360»

## Einkommensberechnung

<a id="20-berechnung-total"></a>
### Ziff. 20 – Total der Einkünfte, Übertrag von Seite 2 (Ziffer 6 oder 9)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Übertrag von Ziff. 6 (ohne Liegenschaften) bzw. Ziff. 9.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «20. Total der Einkünfte, Übertrag von Seite 2 (Ziffer 6 oder 9)»

<a id="21-berechnung-total"></a>
### Ziff. 21 – Total der Abzüge, Übertrag von Ziffer 19

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Übertrag Ziff. 19, getrennt Staat/Bund.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «21. Total der Abzüge, Übertrag von Ziffer 19»

<a id="22-berechnung-total"></a>
### Ziff. 22 – Nettoeinkommen (Code 362)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 20 minus Ziff. 21)
- **Regel:** Basis für Selbstbehalt Krankheitskosten (5%) und Limite freiwillige Zuwendungen (20%); Spalte Staat und Bund je getrennt verwenden.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «22. Nettoeinkommen 362»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0203.md) `tg-wl-2026__c0203` – «ziehen Sie einen Selbstbehalt von 5% des Nettoeinkommens gemäss Ziffer 22 der Steuererklä-»

<a id="23-1-abzug-krankheitskosten"></a>
### Ziff. 23.1 – Krankheits- und Unfallkosten (Formular 5.1 Teil D, Code 364)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 5.1 Teil D «Abzugsfähige Krankheits- und Unfallkosten» (Staat links / Bund rechts)
- **Regel:** Selbst getragene Kosten (Arzt, Zahnarzt, Spital, Medikamente, Brillen, Kuren; für sich und Personen mit Kinder-/Unterstützungsabzug) abzüglich Vergütungen Dritter (Krankenkasse, Versicherungen, Hilflosenentschädigung, Pflegefinanzierung, Anteil Lebenshaltungskosten) und abzüglich Selbstbehalt 5% des Nettoeinkommens (Ziff. 22, Staat und Bund je mit eigenem Nettoeinkommen). Diätpauschale Fr. 2'500 bei lebensnotwendiger Diät (z.B. Zöliakie; nicht Diabetes). Nicht abziehbar: Krankenkassenprämien, Fahrkosten zum Arzt, Prävention, Schönheits-/Fitnesskuren. Belege geordnet beilegen.
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten: abziehbar, soweit selbst getragen und ueber 5 % des Nettoeinkommens (Ziff. 22 Steuererklaerung). Diaet-Pauschale Fr. 2'500 (z.B. Zoeliakie, nicht Diabetes).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
- **Bund:** Selbstbehalt 5% vom Nettoeinkommen der Spalte Bund (Betrag meist abweichend vom Staat).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «23.1 Krankheits- und Unfallkosten Formular 5 364»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0196.md) `tg-wl-2026__c0196` – «Soweit Sie die Kosten selber tragen und diese 5% des Nettoeinkommens (Ziffer 22) übersteigen,»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0196.md) `tg-wl-2026__c0196` – «können Sie anstelle der effektiven»

<a id="23-2-abzug-spenden"></a>
### Ziff. 23.2 – Freiwillige Zuwendungen (Formular 6, Code 366)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Formular 6 «Berechnung abzugsfähige freiwillige Zuwendungen»; Quittungen ab Fr. 1'000 pro Zuwendung
- **Regel:** Nur Zuwendungen an in der Schweiz steuerbefreite Körperschaften für öffentliche/gemeinnützige Zwecke (kantonale Liste). Kanton: Abzug soweit gesamthaft über Fr. 200; max. Fr. 8'000 bei Nettoeinkommen bis Fr. 40'000, darüber max. 20% des Nettoeinkommens. Bund: ab Fr. 100 gesamthaft ohne Selbstbehalt bis max. 20% des Nettoeinkommens. Religiöse, wohltätige, kulturelle, gesellige, sportliche Zwecke und ausländische Empfänger nicht abziehbar.
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 200 (Freiwillige Zuwendungen: abziehbar, soweit sie gesamthaft Fr. 200 uebersteigen (Selbstbehalt Fr. 200). Bund: ab Fr. 100 ohne Selbstbehalt.)** · Bund **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn im Steuerjahr mindestens CHF 100 erreicht.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: max. 20 % des Nettoeinkommens (Ziff. 22); bei Nettoeinkommen bis Fr. 40'000 max. Fr. 8'000.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**
- **Bund:** Bund: Mindestbetrag Fr. 100, kein Selbstbehalt, max. 20% des Nettoeinkommens.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «23.2 Freiwillige Zuwendungen Formular 6 366»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0215.md) `tg-wl-2026__c0215` – «maximal den Betrag von Fr. 8 000 abziehen.»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0215.md) `tg-wl-2026__c0215` – «gesamthaft (ohne Selbstbehalt) bis maximal 20% des Nettoein-»

<a id="23-3-abzug-uebrige"></a>
### Ziff. 23.3 – Separat zu besteuernde Liquidationsgewinne (Code 368)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 14a (Berechnung Liquidationsgewinn); StP 38b Nr. 1
- **Regel:** Bei definitiver Geschäftsaufgabe nach vollendetem 55. Altersjahr oder wegen Invalidität werden die in den letzten zwei Geschäftsjahren realisierten stillen Reserven getrennt privilegiert besteuert; hier von den ordentlich steuerbaren Einkünften abziehen (im Geschäftsergebnis Ziff. 2.1/2.2 enthalten).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «23.3 Separat zu besteuernde Liquidationsgewinne 368»
  - [WL TG 2026 S. 16](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0063.md) `tg-wl-2026__c0063` – «können Sie daher unter Ziffer 23.3 wieder von den Einkünften in Abzug bringen»

<a id="24-berechnung-total"></a>
### Ziff. 24 – Reineinkommen (Code 372)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 22 minus 23.1 bis 23.3)
- **Regel:** Satzbestimmend für den Abzug AHV-Rentner/Erwerbsunfähige/Verwitwete (Ziff. 25.3).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «24. Reineinkommen (Ziffer 22 abzüglich Ziffern 23.1 bis 23.3) 372»

<a id="25-1-sozialabzug-kinder"></a>
### Ziff. 25.1 – Sozialabzug für Kinder: a) in Ausbildung Jg. 2001–2006 (Code 380); Jg. 2007–2010 (Code 382); b) übrige Kinder (Code 384)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien Kinder Seite 1 (Jahrgang, Ausbildung, Haushalt)
- **Regel:** Pro nicht selbständig besteuertes, in Ausbildung stehendes oder erwerbsunfähiges eigenes Kind, für dessen Unterhalt aufgekommen wird (nicht Pflege-/Stiefkinder). Kanton: Jg. 2001–2006 in Ausbildung Fr. 10'600; Jg. 2007–2010 in Ausbildung Fr. 8'500; übrige Fr. 7'400. Bund einheitlich Fr. 6'800. Kein Abzug bei Kind mit selbständigem Lebensunterhalt. Stichtag 31.12.2026 (nicht pro rata). Getrennte Eltern: Zuteilung nach Alimenten/Sorgerecht/Obhut (Kanton und Bund unterschiedlich).
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 7'400 (Kinderabzug je Kind (nicht selbstaendig besteuert, in Ausbildung oder erwerbsunfaehig, Unterhalt wird getragen): Fr. 7'400 ('uebriges Kind'). Stichtag 31.12.2026. Zusaetzlich Steuergutschrift max. Fr. 100 pro minderjaehriges Kind mit der Schlussrechnung.)** · Bund **CHF 6'800 (Kinderabzug CHF 6'800 pro minderjähriges oder in beruflicher/schulischer Ausbildung stehendes Kind, für dessen Unterhalt die steuerpflichtige Person sorgt; bei getrennter Besteuerung der Eltern hälftig bei gemeinsamer elterlicher Sorge ohne Unterhaltsbeiträge.)**
  - Kinderabzug Vorschulalter (CHF): Kanton **n/a** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (Art. 35 Abs. 1 lit. a DBG), keine Staffelung nach Alter; siehe sozialabzug.kind.**
  - Kinderabzug Schulalter (CHF): Kanton **n/a** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800, keine Staffelung nach Alter; siehe sozialabzug.kind.**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 8'500 (Kind in Ausbildung nach Vollendung des 16. Altersjahres (WL 2026: Jahrgang 2007-2010): Fr. 8'500.)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Abzug CHF 6'800 (kein höherer Ausbildungsabzug beim Bund).)**
  - Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF): Kanton **CHF 10'600 (Kind in Ausbildung nach Vollendung des 20. bis zum vollendeten 26. Altersjahr (WL 2026: Jahrgang 2001-2006): Fr. 10'600.)** · Bund **n/a – Bund: kein erhöhter Abzug für auswärtige Ausbildung; einheitlich CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).**
- **Bund:** Bund Fr. 6'800 je Kind; Zuteilungsregeln bei getrennten Eltern weichen ab.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «25.1 a) für jedes Kind in Ausbildung mit Jahrg. 2001 – 2006 Fr. 10 600 Fr. 6800 380»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0107.md) `tg-wl-2026__c0107` – «für jedes Kind in Ausbildung mit Jahrgang 2007 – 2010 Fr. 8'500 Fr. 6'800»
  - [WL TG 2026 S. 23–24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0106.md) `tg-wl-2026__c0106` – «Für die Festsetzung der Sozialabzüge für Kinder und unterstützte Personen sind die Verhältnisse»

<a id="25-2-sozialabzug-unterstuetzung"></a>
### Ziff. 25.2 – Sozialabzug für jede unterstützte Person (Code 386)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Nachweis der Unterstützung (Zahlungsnachweise, Bestätigung)
- **Regel:** Kanton Fr. 2'700 bei Hauptunterhalt einer erwerbsunfähigen, unterstützungsbedürftigen Person (Kosten nachweislich ≥50% des betreibungsrechtlichen Existenzminimums). Bund Fr. 6'800 bei nachgewiesenem Beitrag von mindestens Fr. 6'800. Nicht für Ehegatte/Partner und Kinder mit Kinderabzug/Alimentenabzug.
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'700 (Unterstuetzungsabzug je erwerbsunfaehige und unterstuetzungsbeduerftige Person (nicht Ehegatte/Kind mit Kinderabzug): Fr. 2'700; Voraussetzung: Beitrag zu mehr als 50 % des betreibungsrechtlichen Existenzminimums.)** · Bund **CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)**
- **Bund:** Bund Fr. 6'800.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «25.2 für jede unterstützte Person Fr. 2 700 Fr. 6800 386»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0113.md) `tg-wl-2026__c0113` – «dürftigen Person auf, können Sie kantonal Fr. 2 700 abziehen.»

<a id="25-3-sozialabzug-alter-iv"></a>
### Ziff. 25.3 – Sozialabzug für Personen mit AHV-Altersrenten sowie erwerbsunfähige oder verwitwete Personen (Code 388) – nur Staatssteuer

- **Schlüssel:** `sozialabzug.alter_iv` (Abzug für Personen im AHV-Alter, erwerbsunfähig oder verwitwet (kantonal)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Reineinkommen Ziff. 24 (satzbestimmend) – Tabelle der Wegleitung
- **Regel:** Nur Kanton: gestaffelt nach satzbestimmendem Reineinkommen (Ziff. 24); maximal Fr. 4'200 (Alleinstehende bis Fr. 17'899, gemeinsam Besteuerte bis Fr. 25'299), danach in Stufen zu Fr. 200 abnehmend; kein Abzug ab Fr. 37'900 bzw. Fr. 45'300. Wegleitung-Tabelle exakt anwenden.
- **Limiten:**
  - Abzug AHV-Alter/erwerbsunfähig/verwitwet (CHF): Kanton **CHF 4'200 (Abzug fuer AHV-Altersrentner, Erwerbsunfaehige und Verwitwete (nur Kanton): max. Fr. 4'200; Reduktion um Fr. 200 je Fr. 1'000 Mehreinkommen ab Reineinkommen ueber Fr. 16'900 (Alleinstehende) bzw. Fr. 24'300 (Gemeinsam Besteuerte); kein Abzug ab Fr. 37'900 bzw. Fr. 45'300.)** · Bund **n/a – Kantonaler Abzug; die direkte Bundessteuer kennt keinen Abzug für AHV-Alter/Erwerbsunfähigkeit/Verwitwung (Art. 35 DBG).**
- **Bund:** Kein Abzug bei der direkten Bundessteuer.
- **Bemerkung:** Tabelle W c0115: Zeile «36'900–37'689» wirkt layout-/druckfehlerhaft (erwartet 37'899); Original-PDF prüfen.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «25.3 für Personen mit AHV-Altersrenten sowie erwerbsunfähige oder verwitwete Personen 388»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0115.md) `tg-wl-2026__c0115` – «37'900 u. mehr 45'300 u. mehr kein Abzug»

<a id="25-4-sozialabzug-verheiratete"></a>
### Ziff. 25.4 – Sozialabzug für gemeinsam besteuerte Personen (Code 390) – nur Bundessteuer

- **Schlüssel:** `sozialabzug.verheiratete` (Verheiratetenabzug (Bund)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand (Ehe/eingetragene Partnerschaft)
- **Regel:** Nur direkte Bundessteuer Fr. 2'800; bei den Staats- und Gemeindesteuern kein solcher Abzug.
- **Limiten:**
  - Verheiratetenabzug (CHF, Bund): Kanton **n/a – WL 2026 c0116: 'Bei den Staats- und Gemeindesteuern kann dieser Abzug nicht geltend gemacht werden.'** · Bund **CHF 2'800 (Verheiratetenabzug CHF 2'800 für Ehepaare in rechtlich und tatsächlich ungetrennter Ehe.)**
- **Bund:** Fr. 2'800 nur Bund.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «25.4 für gemeinsam besteuerte Personen 390»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0116.md) `tg-wl-2026__c0116` – «Sozialabzug von Fr. 2'800 tätigen.»

<a id="26-berechnung-total"></a>
### Ziff. 26 – Steuerbares Einkommen (Code 398)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 24 minus 25.1 bis 25.4)
- **Regel:** Ergebnis getrennt für Staat und Bund; Basis für Tarif (Staat Vollsplitting Divisor 2 bei gemeinsam Besteuerten).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «26. STEUERBARES EINKOMMEN (Ziffer 24 abzüglich Ziffern 25.1 bis 25.4) 398»
  - [WL TG 2026 S. 52](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0243.md) `tg-wl-2026__c0243` – «wird das Vollsplitting angewendet»

<a id="28-1-sozialabzug-kinder"></a>
### Ziff. 28.1 – Kanton: Steuergutschrift für minderjährige Kinder (Anzahl Kinder)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Anzahl Kinder mit Kinderabzug (minderjährig)
- **Regel:** Anzahl der minderjährigen Kinder eintragen, für die ein Kinderabzug geltend gemacht werden kann; Gutschrift max. Fr. 100 pro Kind mit der Schlussrechnung, keine Auszahlung über den Steuerbetrag hinaus.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «28.1 Kanton: Steuergutschrift für minderjährige Kinder Anzahl Kinder»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0116.md) `tg-wl-2026__c0116` – «gutschrift von maximal Fr. 100.»

<a id="28-2-sozialabzug-unterstuetzung"></a>
### Ziff. 28.2 – Bund: Ermässigung Steuerbetrag für Kinder und unterstützungsbedürftige Personen (Anzahl Personen)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Anzahl Kinder und unterstützte Personen im gleichen Haushalt (Elterntarif)
- **Regel:** Bund: Abzug vom Steuerbetrag Fr. 263 pro Kind und/oder unterstützte Person bei Zusammenleben im gleichen Haushalt und überwiegender Unterhaltsleistung.
- **Limiten:**
  - Abzug vom Steuerbetrag pro Kind (CHF, Bund): Kanton **n/a – Kantonale Steuergutschrift Fr. 100: WL 2026 c0246 ('Steuergutschrift von maximal Fr. 100').** · Bund **CHF 263 (Ermässigung des Steuerbetrags um CHF 263 pro Kind oder unterstützungsbedürftige Person (Ehepaare sowie Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern/unterstützungsbedürftigen Personen im gleichen Haushalt, die deren Unterhalt zur Hauptsache bestreiten).)**
- **Bund:** Fr. 263 je Kind/unterstützte Person (Elterntarif).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «28.2 Bund: Ermässigung Steuerbetrag für Kinder und unterstützungsbedürftige Personen Anzahl Personen»
  - [WL TG 2026 S. 25–26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0117.md) `tg-wl-2026__c0117` – «Fr. 263 pro Kind und/oder pro unterstützte Person vom Steuerbetrag geltend machen.»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben (Formular 2, Code 410)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 Total Steuerwerte (Ziff. 9); Steuerwerte per 31.12.2026
- **Regel:** Steuerwert = Verkehrswert; kotierte CH-Titel Börsenkurs Ende Dezember 2026, Auslandtitel Kurs Ende Dezember in CHF gemäss ESTV-Kursliste. PK-/Freizügigkeitsguthaben und nicht fällige 3a-Guthaben nicht deklarieren. Vermögen und Erträge der Kinder Jg. 2008 und jünger sind mitzudeklarieren.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.1 Wertschriften und Guthaben Formular 2 410»
  - [WL TG 2026 S. 30–31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0143.md) `tg-wl-2026__c0143` – «Für in der Schweiz kotierte Wertpapiere gilt der Börsenkurs Ende des Monats Dezember 2026.»
  - [WL TG 2026 S. 30](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0140.md) `tg-wl-2026__c0140` – «Vermögen und Erträge von Kindern unter Ihrer elterlichen Sorge (Jahrgang 2008 und jünger)»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 412)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bestandesaufstellung per 31.12.2026; Kursliste ESTV
- **Regel:** Inländisches Bargeld mit Bestand 31.12.2026; ausländisches Bargeld, Gold und Edelmetalle zum Verkehrswert 31.12.2026 (amtliche Kursliste).
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.2 Bargeld, Gold und andere Edelmetalle 412»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0120.md) `tg-wl-2026__c0120` – «Inländisches Bargeld ist mit dem Bestand per 31. Dezember 2026 aufzuführen.»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen – Rückkaufswert inkl. Überschussguthaben (Code 420)

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Bescheinigung des Versicherers per 31.12.2026 (Steuerwert/Rückkaufswert)
- **Regel:** Rückkaufswert inkl. Überschuss- und Gewinnanteile; auch Rentenversicherungen während der Rentenlaufzeit. Gesellschaft, Abschluss-/Ablaufjahr, Versicherungssumme und Steuerwert eintragen; Bescheinigung beilegen.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.3 Lebens- und Rentenversicherungen (Rückkaufswert inkl. Überschussguthaben)»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0121.md) `tg-wl-2026__c0121` – «Kapital- und Rentenversicherungen unterliegen mit ihrem Steuerwert (Rückkaufswert inkl. Über-»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge – Marke, Kaufpreis, Anschaffungsjahr (Code 422)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg, Motorfahrzeug-Versicherungspolice (Haftpflicht/Kasko) und Verkehrssteuer-Rechnung → Kaufvertrag/Fahrzeugausweis (Kaufpreis, Anschaffungsjahr)
- **Regel:** Verkehrswert 31.12.2026: Wertverminderung 20% vom Kaufpreis pro Jahr seit Erwerb; vor mehr als 5 Jahren gekaufte Fahrzeuge pro memoria Fr. 1.–. Geleaste Fahrzeuge nicht deklarieren. Oldtimer/Liebhaberfahrzeuge unter Ziff. 30.6.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.4 Motorfahrzeuge Steuerwert Fr.»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0122.md) `tg-wl-2026__c0122` – «Fahrzeuge die vor mehr als 5 Jahren gekauft»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Anteile an unverteilten Erbschaften (Formular 3, Code 424)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung der Erbengemeinschaft/Formular 3
- **Regel:** Anteil am Erbschaftsvermögen quotenmässig; analog Ertrag in Ziff. 5.3.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.5 Anteile an unverteilten Erbschaften Formular 3 424»
  - [WL TG 2026 S. 26–27](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0123.md) `tg-wl-2026__c0123` – «Die Anteile an unverteilten Erbschaften und Nutzniessungen werden den einzelnen erbenden oder»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte – nähere Bezeichnung (Code 426)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung mit Verkehrswerten per 31.12.2026
- **Regel:** Z.B. Wohnwagen, Wohnmobile, Oldtimer, Boote, Reitpferde, Kunst, Schmuck, Sammlungen, Patente: näher bezeichnen und zum Verkehrswert deklarieren. Hausrat ist steuerfrei.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.6 Übrige Vermögenswerte, nähere Bezeichnung: 426»
  - [WL TG 2026 S. 26–27](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0123.md) `tg-wl-2026__c0123` – «Unter die übrigen Vermögenswerte fallen z.B. Wohnwagen, Wohnmobile, Oldtimer, Liebhaberfahr-»

<a id="31-vermoegen-liegenschaften"></a>
### Ziff. 31 – Liegenschaften (Formular 7, Code 430)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Formular 7 Total Steuerwerte; Liegenschaftensteuerrechnung/Schätzung
- **Regel:** Amtlicher Verkehrswert (rechtskräftig am Ende der Steuerperiode); landwirtschaftliche Liegenschaften Ertragswert; ausserkantonale/ausländische Liegenschaften zum dortigen Steuerwert (Repartitionswert durch Behörde). Noch nicht geschätzte Bauten/Umbauten angemessen berücksichtigen.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0015.md) `tg-form-01-2026__c0015` – «31. Liegenschaften Formular 7 430»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0236.md) `tg-wl-2026__c0236` – «Für nichtlandwirtschaftliche Liegenschaften geben Sie den am Ende der Steuerperiode bzw. der»

<a id="32-vermoegen-uebrige"></a>
### Ziff. 32 – Betriebsvermögen selbständig erwerbender Personen: Geschäftskapital Kollektiv-/Kommanditgesellschaft (Code 440), Total Geschäftsvermögen (Code 442)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz / Bescheinigung der Gesellschaft über Vermögensanteil
- **Regel:** Angaben 32.2–32.5 (Bankkonti/Wertschriften/Debitoren, Vorräte, Viehhabe, Anlagevermögen ohne Grundeigentum) oder Total lt. Bilanz in Ziff. 32.6; Geschäftsvermögen zu Verkehrswerten. Bei Kollektiv-/Kommanditgesellschaft persönlicher Anteil; Bescheinigung der Gesellschaft beilegen.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0015.md) `tg-form-01-2026__c0015` – «32.6 Total Geschäftsvermögen (Ziffern 32.2 bis 32.5) oder lt. Bilanz»
  - [WL TG 2026 S. 27](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0124.md) `tg-wl-2026__c0124` – «Kollektiv- und Kommanditgesellschaften werden nicht als Einheit besteuert.»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 464)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 30.1 bis 32.6)
- **Regel:** Summe aller Vermögenswerte vor Schulden (nur Staatssteuer; Vermögen wird nur kantonal besteuert).
- **Bund:** Kein Vermögen bei der direkten Bundessteuer.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0015.md) `tg-form-01-2026__c0015` – «33. Total der Vermögenswerte (Ziffern 30.1 bis 32.6) 464»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0118.md) `tg-wl-2026__c0118` – «Das Vermögen wird nur kantonal besteuert.»

<a id="34-schulden-privat"></a>
### Ziff. 34 – Schulden (Formular 4.1, Code 466)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Leasingvertrag Fahrzeug / Leasingraten-Abrechnung → Formular 4.1 Total Privat- und Geschäftsschulden (Zusammenzug C, Code 466)
- **Regel:** Schuldenstand am 31.12.2026 mit Gläubiger/in (genaue Adresse) und Zinssatz; Privat- (A) und Geschäftsschulden (B) getrennt. Rentenverpflichtungen mit Barwert, wenn entgeltlich zugesichert.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0015.md) `tg-form-01-2026__c0015` – «34. Schulden Formular 4.1 466»
  - [WL TG 2026 S. 27](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0127.md) `tg-wl-2026__c0127` – «Übertragen Sie das Total der Schulden in die Steuerer-»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Reinvermögen (Code 468)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 33 minus 34)
- **Regel:** Ziff. 33 abzüglich Ziff. 34.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0015.md) `tg-form-01-2026__c0015` – «35. Reinvermögen (Ziffer 33 abzüglich Ziffer 34) 468»

<a id="36-1-36-3-vermoegen-sozialabzug"></a>
### Ziff. 36.1–36.3 – Steuerfreie Beträge: gemeinsam Besteuerte Fr. 200'000 (Code 470); Alleinstehende Fr. 100'000 (Code 472); je nicht selbständig besteuertes Kind Jg. 2009 und jünger Fr. 100'000 (Code 474)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien/Kinder (Jahrgang) Seite 1
- **Regel:** Verhältnisse am 31.12.2026. Bei getrennt besteuerten Eltern erhält der Elternteil den Freibetrag je Kind, der den Kinderabzug erhält; hälftig nur bei gemeinsamem Sorgerecht, keinen periodischen Unterhaltsbeiträgen und alternierender Obhut. Für mündige Kinder (Mündigkeitsjahr) kein Freibetrag der Eltern.
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 100'000 (Steuerfreier Betrag Vermoegenssteuer: Fr. 100'000 fuer alle uebrigen Steuerpflichtigen (ledig, getrennt, geschieden, verwitwet). Stichtag 31.12.2026.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 200'000 (Steuerfreier Betrag Vermoegenssteuer: Fr. 200'000 fuer Steuerpflichtige in ungetrennter Ehe/Partnerschaft.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 100'000 (Zusaetzlich Fr. 100'000 je nicht selbstaendig besteuertes Kind (WL 2026: Jahrgang 2009 und juenger). Bei getrennt besteuerten Eltern Zuteilung wie Kinderabzug; haelftig bei gemeinsamem Sorgerecht und alternierender Obhut ohne Alimente.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
- **Bund:** Kein Vermögenssteuerabzug bei der direkten Bundessteuer.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0016.md) `tg-form-01-2026__c0016` – «36.1 Abzug für gemeinsam besteuerte Personen (Eheleute / Partnerinnen oder Partner) Fr. 200000 470»
  - [WL TG 2026 S. 27–28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0128.md) `tg-wl-2026__c0128` – «– für jedes nicht selbständig besteuerte Kind (Jahrgang 2009 und jünger) Fr. 100'000»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen gesamt (Code 498)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 35 minus 36.1 bis 36.3)
- **Regel:** Ergebnis ist Basis der Vermögenssteuer.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0016.md) `tg-form-01-2026__c0016` – «37. STEUERBARES VERMÖGEN GESAMT (Ziffer 35 abzüglich Ziffern 36.1 bis 36.3) 498»

## Weitere Angaben

<a id="s-4-schenkungen-info-schenkungen-erbschaften"></a>
### Ziff. S. 4 Schenkungen – Schenkungen und erbrechtliche Vermögensanfälle (erhalten/ausgerichtet)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Schenkungsvertrag, Erbteilung, Erbvorbezugsvertrag
- **Regel:** Sämtliche 2026 erhaltenen oder ausgerichteten Schenkungen/Erbvorbezüge/Erbschaften mit Datum, Betrag, Geber/Empfänger inkl. Adresse und Verwandtschaftsgrad aufführen (auch unverteilte Erbschaften). Hilfsblätter auf der Homepage der Steuerverwaltung.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0017.md) `tg-form-01-2026__c0017` – «Schenkungen und erbrechtliche Vermögensanfälle»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0129.md) `tg-wl-2026__c0129` – «Führen Sie sämtliche im Jahre 2026 getätigten oder empfangenen Schenkungen und Erbvorbezüge»

<a id="s-4-kapitalleistungen-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. S. 4 Kapitalleistungen – Kapitalleistungen aus Vorsorge 2026 (AHV/IV, Säule 2, Freizügigkeit, Säule 3a, Tod/Nachteile)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung (Betrag, Auszahlungsdatum, Art)
- **Regel:** Quelle ankreuzen, Auszahlungsdatum und Betrag in ganzen Franken angeben; bei mehreren Leistungen Aufstellung einreichen. Immer zu 100% steuerbar, getrennt vom übrigen Einkommen besteuert (nicht in Ziff. 5.5!). Einfache Steuer Kanton: 2% (gemeinsam Besteuerte) bzw. 2,4% (Alleinstehende); Bund: 1/5 des ordentlichen Tarifs, kein Elterntarif.
- **Bund:** 1/5 des ordentlichen Bundestarifs; Elterntarif nicht anwendbar.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0018.md) `tg-form-01-2026__c0018` – «Kapitalleistungen aus Vorsorge 2026»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0131.md) `tg-wl-2026__c0131` – «Bei Alleinstehenden beträgt der einheitliche Satz für die einfache Steuer 2,4%.»
  - [WL TG 2026 S. 28–29](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0133.md) `tg-wl-2026__c0133` – «Bei der direkten Bundessteuer beträgt die Steuer auf Kapitalleistungen aus Vorsorge 1/5 des or-»

<a id="s-2-frist-verfahren-einreichung"></a>
### Ziff. S. 2 Frist – Einreichefrist und Fristerstreckung (Treuhänder)

- **Schlüssel:** `verfahren.einreichung` (Einreichung, Unterschrift, Beilagen, Fristen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Fristerstreckungsgesuch an das Gemeindesteueramt
- **Regel:** Steuererklärung und Hilfsblätter bis zum vorgedruckten Datum beim Gemeindesteueramt einreichen; Fristverlängerung vorgängig, schriftlich und begründet beantragen. Erstes Gesuch grundsätzlich bis 30. September des Deklarationsjahres, weitere in begründeten Fällen bis 30. November; Treuhänder/Steuerberater können für Mandanten längstens bis 31. Dezember des Deklarationsjahres beantragen (Deklarationsjahr = Jahr der Einreichung).
- **Bemerkung:** Fristen aus StP 155 Nr. 2 (jahresunabhängige Praxis, gültig für 2025 und 2026).
- **Quellen:**
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md) `tg-stp-155-2__c0001` – «längstens bis am 30. September des Deklarationsjahres»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0002.md) `tg-stp-155-2__c0002` – «längstens bis zum 31. Dezember des Deklarationsjahres»
  - [WL TG 2026 S. 7–8](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0022.md) `tg-wl-2026__c0022` – «Die ausgefüllte Steuererklärung und die Hilfsblätter sind bis zum vorgedruckten Datum dem»

## Hilfsblatt Berufskosten (Form. 4.2 Person 1 / 4.3 Person 2)

<a id="form-4-2-ziff-1-1-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4.2 Ziff. 1.1 – Allgemeine Angaben: Arbeitgeber, Arbeitsort, Dauer der Erwerbstätigkeit, Arbeitspensum in %

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis (Arbeitgeber, Dauer), Arbeitsvertrag (Pensum)
- **Regel:** Pauschalen gelten für das ganze Jahr und sind bei unterjähriger Erwerbstätigkeit auf die Dauer umzurechnen; bei Teilzeit Kürzung der Verpflegungspauschale nach Beschäftigungsgrad; Berechnung grundsätzlich mit 225 Arbeitstagen. Kein Abzug für Kosten, die Arbeitgebende übernommen haben.
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0001.md) `tg-form-04-2-2026__c0001` – «1.1 Arbeitgeber/in, Arbeitsort»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0173.md) `tg-wl-2026__c0173` – «Bei der Berechnung der notwendigen Auslagen ist in der Regel von 225»

<a id="form-4-2-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2 Ziff. 1.2 – Steht ein Geschäftsfahrzeug für die Fahrt zur Arbeitsstätte zur Verfügung? (Ja/Nein, von/bis)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld F (Kreuz «unentgeltliche Beförderung zwischen Wohn- und Arbeitsort»), Ziff. 2.2 Privatanteil Geschäftsfahrzeug
- **Regel:** Lohnausweis Feld F angekreuzt (Geschäftsfahrzeug, Sammeltransport, GA aus geschäftlichen Gründen u.ä.) → «Ja» und KEIN Fahrkostenabzug (Ziff. 2). Der Privatanteil 0.9% pro Monat im Lohnausweis schliesst den Arbeitsweg ein, daher keine Aufrechnung, aber auch kein Abzug. Wurden die Arbeitswegkosten vergütet (Ziff. 2.3 Lohnausweis), ist Feld F nicht anzukreuzen.
- **Bemerkung:** Lohnausweis-Regel (Feld F) stammt aus Bund-Wegleitung Lohnausweis 2026 (ESTV, amtlich für alle Kantone).
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0001.md) `tg-form-04-2-2026__c0001` – «1.2 Steht Ihnen für die Fahrt zur Arbeitsstätte»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0175.md) `tg-wl-2026__c0175` – «Der im Lohnausweis berücksichtigte Privatanteil Fahrzeug von 0.9 % pro Monat für die private»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «die Beförderung zum Arbeitsort mittels Sammeltransports (v.a. im Baugewerbe)»

<a id="form-4-2-4-3-ziff-2-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2/4.3 Ziff. 2.1 – Abonnementskosten öffentliche Verkehrsmittel (Code 206 / 246)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg → Abo-Beleg (Jahresabo, Streckenabo, GA) – nachgewiesene Kosten
- **Regel:** Tatsächlich entstandene (nachgewiesene) Abonnementskosten für Bahn/Tram/Bus. Nur wenn Lohnausweis Feld F NICHT angekreuzt ist. Auch Fahrkosten bei Wochenaufenthalt (Heimkehr, Unterkunft–Arbeitsstätte) hier einsetzen. Die Summe aus 2.1–2.3 unterliegt dem Fahrkostenmaximum (Ziff. 2.5).
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0002.md) `tg-form-04-2-2026__c0002` – «2.1 Abonnementskosten für öffentliche Verkehrsmittel 206»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0177.md) `tg-wl-2026__c0177` – «Bei Benützung öffentlicher Verkehrsmittel (Bahn, Tram, Autobus) können Sie die tatsächlich»

<a id="form-4-2-4-3-ziff-2-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2/4.3 Ziff. 2.2 – Fahrrad, Kleinmotorrad bis 50 cm³ pauschal Fr. 700 (Code 210 / 250)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Belege nötig (Pauschale)
- **Regel:** Pauschal bis Fr. 700 pro Jahr für Fahrrad, Motorfahrrad, Kleinmotorrad (bis 45 km/h, gelbes Kontrollschild).
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Fahrrad, Motorfahrrad, Kleinmotorrad (bis 45 km/h, gelbes Kontrollschild): bis Fr. 700 im Jahr.)** · Bund **CHF 700 (Fahrrad, Motorfahrrad, Motorrad mit gelbem Kontrollschild: Pauschale CHF 700 pro Jahr; tatsächliche Kosten können nicht zusätzlich geltend gemacht werden.)**
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0002.md) `tg-form-04-2-2026__c0002` – «2.2 Fahrrad, Kleinmotorrad bis 50 cm3 pauschal Fr. 700.– 210»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0177.md) `tg-wl-2026__c0177` – «können Sie bis zu Fr. 700 im Jahr abziehen.»

<a id="form-4-2-4-3-ziff-2-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2/4.3 Ziff. 2.3 – Kosten für privates Motorfahrzeug (Auto / Motorrad über 50 cm³): km pro Tag × Anzahl Tage (Code 211 / 251), Spalten Staat und Bund separat

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ⚠️ strittig
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Begründung der Notwendigkeit (Zeitersparnis, kein zumutbarer ÖV), Arbeitsweg-km und Arbeitstage
- **Regel:** In der Regel nur der Betrag, der mit dem zur Verfügung stehenden ÖV auszulegen wäre; Privatfahrzeug nur in begründeten Fällen. Ansätze Kanton Auto: bis 3'000 km Fr. -.60; 3'001–5'000 km Fr. -.50; über 5'000 km Fr. -.40; Motorrad (weisses Kontrollschild) Fr. -.40/km. Bund einheitlich pro km (siehe Bemerkung: Quellen widersprüchlich Fr. 0.70 vs. 0.75). Bund und Kanton separat berechnen. Max. 225 Arbeitstage bei 100%.
- **Limiten:**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **Privatauto (nur in begruendeten Ausnahmefaellen, wenn OeV nicht zur Verfuegung steht/unzumutbar): gestaffelter Ansatz je jaehrlich gefahrener Kilometer: bis 3'000 km Fr. 0.60, 3'001-5'000 km Fr. 0.50, ueber 5'000 km Fr. 0.40 pro km (Parkgebuehren inbegriffen). Beispiel 12'150 km = Fr. 5'660.** · Bund **CHF 0.75 (Privatauto: CHF 0.75 pro Fahrkilometer, nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist; Gesamtmaximum CHF 3'300.)**
  - Fahrkosten Motorrad – Ansatz pro km (CHF): Kanton **CHF 0.40 (Motorrad (Hoechstgeschwindigkeit ab 45 km/h, weisses Kontrollschild): bis Fr. 0.40 pro Fahrkilometer.)** · Bund **CHF 0.40 (Motorrad mit weissem Kontrollschild: CHF 0.40 pro Fahrkilometer (nur wenn kein öffentliches Verkehrsmittel zumutbar); Gesamtmaximum CHF 3'300.)**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **225 Tage (Bei der Berechnung der notwendigen Berufsauslagen ist in der Regel von 225 Arbeitstagen im Jahr auszugehen (100%-Pensum).)** · Bund **n/a – Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).**
- **Bund:** Bund Auto einheitlich pro km; WL TG 2026 widerspricht sich selbst: Kurzübersicht (c0003) Fr. 0.70, Detailtext (c0180), Kurz-WL 2026 (tg-wl-kurz-2026) und Bund-BKV 2026 Anhang 1 Ziff. 2 Fr. –.75.
- **Bemerkung:** STRITTIG: WL TG 2026 c0003 (Kurzübersicht in der Wegleitung) nennt Bund Autoansatz Fr. 0.70/km; WL c0180, Kurz-WL TG 2026 c0003 und Verordnung Bund-BKV 2026 (Anhang Ziff. 2) Fr. –.75. Rangfolge Verordnung > Wegleitung spricht für Fr. –.75; Fachperson entscheidet. Kanton-Ansätze (0.60/0.50/0.40) sind einheitlich belegt. Ergänzung durch Prüfung: Das Rechenbeispiel in WL c0182 (12'150 km, Bund Fr. 8'505) entspricht Fr. -.70/km, das Beispiel in WL c0180 (Fr. 9'112.50) Fr. -.75/km; die Wegleitung widerspricht sich also auch intern. Bund-BKV Anhang Ziff. 2 (Verordnung) nennt Fr. –.75. Status bleibt strittig; Fachperson entscheidet (vor Anwendung Bund-Ansatz prüfen).
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0002.md) `tg-form-04-2-2026__c0002` – «Total Kosten für den Arbeitsweg mit dem Motorfahrzeug km pro Jahr 211»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0180.md) `tg-wl-2026__c0180` – «Bei der direkten Bundessteuer beträgt der Ansatz einheitlich Fr. -.75 pro gefahrenen Kilometer.»
  - [WL TG 2026 S. 4](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0003.md) `tg-wl-2026__c0003` – «für Autos Ansatz Bund: einheitlich Fr. 0.70 pro Fahrkilometer»
  - [BKV Anhang](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__anhang-1.md) `bund-bkv-2026__anhang-1` – «Autos | pro Fahrkilometer | –.75»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0182.md) `tg-wl-2026__c0182` – «Total effektive Fahrkosten (Ziffer 2.4) Fr. 5'660 Fr. 8'505»

<a id="form-4-2-4-3-ziff-2-4-berechnung-total"></a>
### Ziff. Form. 4.2/4.3 Ziff. 2.4 – Total effektive Fahrkosten (Ziff. 2.1–2.3) (Code 212 / 252)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Summe 2.1 + 2.2 + 2.3 (Staat und Bund separat). Bei kostenloser Überlassung eines Geschäftsfahrzeugs: kein Abzug.
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0002.md) `tg-form-04-2-2026__c0002` – «2.4 Total effektive Fahrkosten (Ziffern 2.1 – 2.3) 212»
  - [WL TG 2026 S. 38–39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0181.md) `tg-wl-2026__c0181` – «Ermitteln Sie das Total der effektiv selbst getragenen Fahrkosten, indem Sie die Beträge der Ziffern»

<a id="form-4-2-4-3-ziff-2-5-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2/4.3 Ziff. 2.5 – Total abzugsfähige Fahrkosten – Staat max. Fr. 6'000 / Bund max. Fr. 3'300 (Code 213 / 253)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile mit Plafonierung
- **Regel:** Total aus 2.4, aber Staat höchstens Fr. 6'000 und Bund höchstens Fr. 3'300 (gilt auch für Fahrkosten bei Wochenaufenthalt). Liegt 2.4 darunter, wird der effektive Betrag eingesetzt.
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstaette (Staats- und Gemeindesteuern): Maximalabzug Fr. 6'000 pro Person gesamthaft (inkl. Fahrkosten Wochenaufenthalt und Nebenerwerb); wird bei unterjaehriger Steuerpflicht/Teilzeit nicht gekuerzt.)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Bund:** Bund max. Fr. 3'300.
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0002.md) `tg-form-04-2-2026__c0002` – «aber Staat max. Fr. 6000.– / Bund max. Fr. 3300.–)»
  - [WL TG 2026 S. 38–39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0181.md) `tg-wl-2026__c0181` – «Bei den Staats- und Gemeindesteuern können Fahrkosten von maximal Fr. 6'000 und bei der»

<a id="form-4-2-4-3-ziff-3-1-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4.2/4.3 Ziff. 3.1 – Mehrkosten auswärtige Verpflegung ohne Verbilligung: Fr. 15 pro Arbeitstag, max. Fr. 3'200/Jahr; Schichttage (Code 214 / 254)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Ziff. 15 (Anzahl Schichttage) bzw. Bescheinigung Arbeitgeber; Lohnausweis Feld G darf nicht angekreuzt sein
- **Regel:** Fr. 15 pro auswärtige Hauptmahlzeit (in der Regel Mittagessen), max. Fr. 3'200/Jahr, wenn Heimkehr am Mittag unzumutbar (grosse Entfernung oder sehr kurze Essenspause). Schicht-/Nachtarbeit: gleiche Pauschale für jeden ausgewiesenen Tag mit durchgehender, mindestens achtstündiger Schicht- oder Nachtarbeit; Anzahl Schichttage ist nachzuweisen (Bescheinigung Arbeitgeber), sofern nicht im Lohnausweis (Ziff. 15 Bemerkungen) aufgeführt. Keine Kumulation mit Fahrkosten für Heimkehr über Mittag und nicht mit Wochenaufenthalt (Ziff. 5.2). Teilzeit: Kürzung nach Pensum.
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswaertige Verpflegung bei taeglicher Heimkehr: Fr. 15 pro auswaertige Hauptmahlzeit (in der Regel nur Mittagessen), wenn Heimkehr am Mittag wegen grosser Entfernung oder sehr kurzer Essenspause nicht zumutbar.)** · Bund **CHF 15 (Auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (in der Regel nur Mittagessen), nur Pauschale zulässig, wenn Hauptmahlzeit wegen grosser Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann oder bei durchgehender Schicht-/Nachtarbeit.)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei staendiger auswaertiger Verpflegung maximal Fr. 3'200 im Jahr; bei Teilzeit/Nebenberuf angemessene Kuerzung.)** · Bund **CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Durchgehende, mindestens achtstuendige Schicht- oder Nachtarbeit (ausgewiesen, Bescheinigung Arbeitgeber): gleiche Abzuege wie auswaertige Verpflegung (Fr. 15 pro Tag, max. Fr. 3'200 im Jahr; bei Verbilligung halb). Nicht kumulierbar mit Verpflegungs- oder Wochenaufenthaltsabzug.)** · Bund **CHF 15 (Schicht-/Nachtarbeit: gleiche Pauschale wie auswärtige Verpflegung, CHF 15 pro Tag bzw. max. CHF 3'200 pro Jahr (bei Verbilligung halber Abzug). Gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt (Art. 6 Abs. 4 BKV). Arbeitgeber muss Tage und Arbeitsort auf Verlangen bescheinigen.)**
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0003.md) `tg-form-04-2-2026__c0003` – «3.1 ohne Verbilligung durch Arbeitgeber/in oder Schicht-/Nachtarbeit:»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0183.md) `tg-wl-2026__c0183` – «Der Pauschalabzug beträgt Fr. 15 für jede auswärtige Hauptmahlzeit»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0184.md) `tg-wl-2026__c0184` – «Die Anzahl geleistete Tage mit mindestens achtstündiger Schicht- oder Nachtarbeit ist nachzuweisen»
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «die Anzahl im Kalenderjahr geleisteter Schichttage und die Höhe der im Bruttolohn»

<a id="form-4-2-4-3-ziff-3-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4.2/4.3 Ziff. 3.2 – Mehrkosten auswärtige Verpflegung mit Verbilligung durch Arbeitgeber/Kantine: Fr. 7.50 pro Arbeitstag, max. Fr. 1'600/Jahr (Code 216 / 256)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Feld G (Kantine/Lunch-Checks/Personalrestaurant) angekreuzt; Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt»
- **Regel:** Lohnausweis Feld G angekreuzt (Lunch-Checks, verbilligtes Mittag-/Abendessen im Personalrestaurant – auch wenn unbekannt ist, ob davon Gebrauch gemacht wird) → nur halber Abzug: Fr. 7.50/Tag, max. Fr. 1'600/Jahr, und nur wenn trotzdem Mehrkosten entstehen. Kein Abzug, wenn die Hauptmahlzeiten auf weniger als Fr. 10 zu stehen kommen. Wenn der Arbeitgeber das Mittagessen vollständig bezahlt (Ziff. 15 Vermerk), kein Verpflegungsabzug.
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Bei Verbilligung durch Arbeitgeber (Gutscheine, Kantine, Personalrestaurant) nur der halbe Abzug: Fr. 7.50 pro Tag. Kein Abzug, wenn Hauptmahlzeit unter Fr. 10 zu stehen kommt.)** · Bund **CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei Verbilligung durch Arbeitgeber: halber Abzug, maximal Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)**
- **Bemerkung:** Lohnausweis-Regel Feld G aus Bund-WL Lohnausweis 2026 (ESTV).
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0003.md) `tg-form-04-2-2026__c0003` – «3.2 mit Verbilligung durch Arbeitgeber/in oder Kantine,»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0185.md) `tg-wl-2026__c0185` – «Nur der halbe Abzug (Fr. 7.50 im Tag, Fr. 1'600 im Jahr) ist zulässig»
  - [WL TG 2026 S. 39–40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0186.md) `tg-wl-2026__c0186` – «Kein Abzug ist mangels Mehrkosten zulässig, wenn die Hauptmahlzeiten auf weniger als»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer Lunch-Checks»

<a id="form-4-2-4-3-ziff-4-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4.2/4.3 Ziff. 4 – Übrige für den Beruf erforderliche Kosten: 3% vom Nettolohn, min. Fr. 2'000, max. Fr. 4'000, oder effektiv (Code 220 / 260)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 Nettolohn (Berechnungsbasis); bei effektiven Kosten Aufstellung mit Belegen
- **Regel:** Pauschale 3% des Nettolohns (Lohnausweis Ziff. 11), min. Fr. 2'000, max. Fr. 4'000 (Staat und Bund); bei weniger als 12 Monaten Erwerbstätigkeit anteilmässig gekürzt. Alternativ effektive Kosten nachweisen (separate Aufstellung) – keine Kumulation mit der Pauschale.
- **Limiten:**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **3 % (Pauschale uebrige Berufskosten: 3 % des Nettolohns (Ziff. 11 Lohnausweis); alternativ Nachweis der effektiven Kosten (nicht kumulierbar). Bei weniger als 12 Monaten Erwerbstaetigkeit anteilmaessig gekuerzt.)** · Bund **3 % (Übrige Berufskosten: Pauschale 3 % des Nettolohns, mindestens CHF 2'000, höchstens CHF 4'000 pro Jahr; Nachweis höherer tatsächlicher Kosten möglich. Bei Teilzeit/Teiljahr angemessen zu kürzen.)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **CHF 2'000 (Pauschale uebrige Berufskosten: Minimum Fr. 2'000.)** · Bund **CHF 2'000 (Mindestbetrag der Pauschale übrige Berufskosten.)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 4'000 (Pauschale uebrige Berufskosten: Maximum Fr. 4'000.)** · Bund **CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)**
- **Bund:** Gleich (Pauschale gilt kantonal und Bund).
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0004.md) `tg-form-04-2-2026__c0004` – «3% vom Nettolohn, mindestens jedoch Fr. 2000.– und höchstens Fr. 4000.–»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0187.md) `tg-wl-2026__c0187` – «Pauschalabzug von 3% vom Nettolohn gemäss Ziffer 11 des Lohnausweises»

<a id="form-4-2-4-3-ziff-5-1-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4.2/4.3 Ziff. 5.1 – Wochenaufenthalt – Unterkunft: ortsübliche Auslagen für ein Zimmer (Code 226 / 266)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag/Mietzinsbestätigung Zimmer am Arbeitsort
- **Regel:** Nur ein Zimmer (nicht Wohnung) ist notwendig; bei kleiner Wohnung bis 3½ Zimmer: Jahresmietzins : (Zimmerzahl + 1) = Kosten des Zimmers. Fahrkosten der wöchentlichen Heimkehr unter Ziff. 2.1–2.3 (mit Fahrkostenmaximum).
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Wochenaufenthalt: notwendige Mehrkosten der Unterkunft - nur ortsuebliche Auslagen fuer ein Zimmer (nicht Wohnung). Bei gemieteter kleinerer Wohnung (bis 3.5 Zimmer): Jahresmietzins : (Anzahl Zimmer + 1) = Kosten des Zimmers. Kein Abzug bei Naturallohn.** · Bund **Wochenaufenthalt: abziehbar sind die ortsüblichen Auslagen für ein Zimmer (nicht eine Wohnung) am Arbeitsort sowie die Fahrkosten der regelmässigen Heimkehr (im Rahmen des Fahrkosten-Maximums).**
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0004.md) `tg-form-04-2-2026__c0004` – «5.1 Unterkunft ortsübliche Auslagen für ein Zimmer 226»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0189.md) `tg-wl-2026__c0189` – «Jahresmietzins : (Anzahl Zimmer + 1) = Kosten des Zimmers»

<a id="form-4-2-4-3-ziff-5-2-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4.2/4.3 Ziff. 5.2 – Wochenaufenthalt – Verpflegung: Fr. 30 pro Arbeitstag, max. Fr. 6'400/Jahr; bei Verbilligung Fr. 22.50, max. Fr. 4'800 (Code 230 / 270)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (verbilligtes Mittagessen) → Reduktion
- **Regel:** Fr. 15 pro Hauptmahlzeit = Fr. 30 pro Tag, bei ganzjährigem Wochenaufenthalt Fr. 6'400; bei vom Arbeitgeber verbilligtem Mittagessen (Kantinenkost, Kostenbeitrag) für diese Mahlzeit nur der halbe Abzug, gesamthaft Fr. 22.50 pro Tag bzw. Fr. 4'800 im Jahr. Nicht kumulierbar mit Ziff. 3.
- **Limiten:**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 6'400 (Wochenaufenthalt Verpflegung: Fr. 15 pro Hauptmahlzeit = Fr. 30 pro Tag, bei ganzjaehrigem Wochenaufenthalt Fr. 6'400 im Jahr; bei Verbilligung des Mittagessens Fr. 22.50 pro Tag bzw. Fr. 4'800 im Jahr.)** · Bund **CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug CHF 30 pro Tag bzw. CHF 6'400 pro Jahr; gekürzter Abzug (verbilligtes Mittagessen) CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr. Nachweis höherer Kosten ausgeschlossen.)**
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0004.md) `tg-form-04-2-2026__c0004` – «bei Verbilligung pro Arbeitstag Fr. 22.50 / im Jahr Fr. 4800.–»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0189.md) `tg-wl-2026__c0189` – «im Tag, bei ganzjährigem Wochenaufenthalt Fr. 6'400 im Jahr abziehen.»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0189.md) `tg-wl-2026__c0189` – «gesamthaft Fr. 22.50 im Tag oder Fr. 4'800 im Jahr.»

<a id="form-4-2-4-3-ziff-6-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 4.2/4.3 Ziff. 6 – Auslagen bei Nebenbeschäftigung: 20% vom Nettolohn, min. Fr. 800, max. Fr. 2'400, oder effektiv (Code 232 / 272)

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Nebenerwerb Ziff. 11; bei effektiven Kosten Aufstellung
- **Regel:** Pauschale 20% der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400 (Staat und Bund); gilt alle Berufskosten der Nebentätigkeit ab (Fahrt, Verpflegung, übrige). Höchstens bis zur Höhe des Einkommens der zugehörigen Tätigkeit. Keine Kumulation Pauschale/effektiv. Pauschalabzug 50% (min. Fr. 2'000, max. Fr. 4'000) für Exekutivbehördenmitglieder.
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Nebenerwerb (unselbstaendig): Pauschale 20 % der Nettoeinkuenfte; sie gilt alle Berufskosten des Nebenerwerbs (Fahrt, Verpflegung, uebrige) ab. Nachweis hoeherer effektiver Kosten vorbehalten; maximal bis Hoehe des Nebenerwerbseinkommens.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb-Pauschale: Minimum Fr. 800 im Jahr.)** · Bund **CHF 800 (Mindestbetrag Pauschale Nebenerwerb.)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb-Pauschale: Maximum Fr. 2'400 im Jahr.)** · Bund **CHF 2'400 (Höchstbetrag Pauschale Nebenerwerb.)**
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0005.md) `tg-form-04-2-2026__c0005` – «20% vom Nettolohn, mindestens Fr. 800.– und höchstens Fr. 2400.–»
  - [WL TG 2026 S. 40–41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0190.md) `tg-wl-2026__c0190` – «Der Abzug beträgt 20% der Nettoeinkünfte, mindestens aber Fr. 800 und höchstens»

<a id="form-4-2-4-3-ziff-7-berechnung-total"></a>
### Ziff. Form. 4.2/4.3 Ziff. 7 – Total der abzugsfähigen Berufsauslagen (Code 240 / 280) – Übertrag Form. 1 Ziff. 10.1 / 10.2

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 2 bis 6)
- **Regel:** Summe Ziff. 2 bis 6 je Spalte Staat/Bund; Übertrag in Formular 1 Ziff. 10.1 (Person 1) bzw. 10.2 (Person 2).
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0005.md) `tg-form-04-2-2026__c0005` – «7. Total der abzugsfähigen Berufsauslagen 240»
  - [WL TG 2026 S. 41–42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0195.md) `tg-wl-2026__c0195` – «Tragen Sie in diese Ziffer die Summe der Berufsauslagen gemäss den Ziffern 2 bis 7 ein.»

## Hilfsblatt Krankheit/Unfall/Behinderung (Form. 5.1)

<a id="form-5-1-a-1-a-9-abzug-krankheitskosten"></a>
### Ziff. Form. 5.1 A.1–A.9 – Aufwendungen: Selbstbehalt/Franchise, Arzt/Medikamente, Zahnarzt, Pflegepersonal, Spital/Heim, Therapien/Kuren, Prothesen/Invalidenfahrzeug, tatsächliche Kosten, Total (A)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Arzt-/Zahnarzt-/Spitalrechnungen; Kostenzusammenstellung der Krankenkasse (Franchise/Selbstbehalt); ärztliche Verordnung Therapien
- **Regel:** In zwei Spalten erfassen: Krankheits- und Unfallkosten sowie behinderungsbedingte Kosten. Belege geordnet beilegen; Kopie ärztliche Verordnung bei Therapien/Kuren. Krankenkassenprämien, Fahrkosten zum Arzt, Prävention und Schönheits-/Fitnessbehandlungen nicht abzugsfähig.
- **Quellen:**
  - [Formular 5.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-1-2026/tg-form-05-1-2026__c0001.md) `tg-form-05-1-2026__c0001` – «Selbstbehalt / Franchise gemäss detaillierter Kostenzusammenstellung der Krankenkasse»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0201.md) `tg-wl-2026__c0201` – «Nicht abzugsfähig sind zudem die Krankenkassenprämien»

<a id="form-5-1-b-1-b-6-abzug-krankheitskosten"></a>
### Ziff. Form. 5.1 B.1–B.6 – Vergütungen Dritter und Anteil Lebenshaltungskosten (Krankenkasse, Versicherungen, Hilflosenentschädigung, Lebenshaltungsanteil, weitere), Total (B)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Leistungsabrechnung/Jahresbestätigung Krankenkasse und Versicherungen; Verfügung Hilflosenentschädigung
- **Regel:** Soweit nicht bereits unter A abgezogen. Vergütete Kosten, AHV/IV/MV/SUVA-Beiträge für Hilfsmittel, Hilflosenentschädigungen, Pflegefinanzierung sowie ein Anteil Lebenshaltungskosten (Ernährung/Unterkunft, z.B. bei Heim: Fr. 2'000 pro Monat) von den Kosten abziehen.
- **Quellen:**
  - [Formular 5.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-1-2026/tg-form-05-1-2026__c0002.md) `tg-form-05-1-2026__c0002` – «3. Hilflosenentschädigung AHV/IV/SUVA»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0201.md) `tg-wl-2026__c0201` – «Die von Krankenkassen, Versicherungen oder Dritten vergüteten Kosten»

<a id="form-5-1-c-abzug-behinderungskosten"></a>
### Ziff. Form. 5.1 C – Abzugsfähige behinderungsbedingte Kosten (A minus B; Code 350) → Form. 1 Ziff. 17

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Rechenzeile; Pauschalen optional (gehörlos, Dialyse, Hilflosenentschädigung)
- **Regel:** Total A minus Total B; ohne Selbstbehalt; Übertrag in Ziff. 17 (identisch für Staat und Bund).
- **Quellen:**
  - [Formular 5.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-1-2026/tg-form-05-1-2026__c0003.md) `tg-form-05-1-2026__c0003` – «Abzugsfähige behinderungsbedingte Kosten 350»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0202.md) `tg-wl-2026__c0202` – «Danach ziehen Sie»

<a id="form-5-1-d-abzug-krankheitskosten"></a>
### Ziff. Form. 5.1 D – Abzugsfähige Krankheits- und Unfallkosten nach Selbstbehalt 5% von Ziff. 22 (Code 364) → Form. 1 Ziff. 23.1

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Rechenzeile mit Selbstbehalt; Nettoeinkommen Ziff. 22 (Staat links / Bund rechts)
- **Regel:** Netto-Auslagen (A minus B) abzüglich 5% des Nettoeinkommens gemäss Ziff. 22, Staat und Bund je mit eigenem Nettoeinkommen; Übertrag in Ziff. 23.1. Diätpauschale Fr. 2'500 (z.B. Zöliakie, nicht Diabetes) anstelle der effektiven Kosten.
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten: abziehbar, soweit selbst getragen und ueber 5 % des Nettoeinkommens (Ziff. 22 Steuererklaerung). Diaet-Pauschale Fr. 2'500 (z.B. Zoeliakie, nicht Diabetes).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
- **Quellen:**
  - [Formular 5.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-1-2026/tg-form-05-1-2026__c0004.md) `tg-form-05-1-2026__c0004` – «abzüglich Selbstbehalt (5% von Ziffer 22 der Steuererklärung)»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0203.md) `tg-wl-2026__c0203` – «ziehen Sie einen Selbstbehalt von 5% des Nettoeinkommens gemäss Ziffer 22 der Steuererklä-»

## Hilfsblatt Versicherungsprämien (Form. 5.2)

<a id="form-5-2-a-1-a-6-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 A.1–A.6 – Versicherungsprämien und Sparzinsen: private Krankenversicherung netto, private Unfallversicherung, Lebens-/Rentenversicherungen, erhaltene Sparzinsen, Krankentaggeld gemäss Lohnausweis; Total (Code 324 / «A5»)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Jahresbestätigung Krankenkasse (Prämie abzüglich IPV), Policen/Prämienrechnungen, Zinsausweise (Sparzinsen gemäss Formular 2), Lohnausweis (Krankentaggeldprämie)
- **Regel:** Ziff. 1: Nettoprämie Krankenkasse = Prämie abzüglich in der Steuerperiode erhaltener Prämienverbilligungen (IPV; inkl. über EL ausgerichtete IPV und Nachzahlungen). Ziff. 2: private Unfallversicherung (ohne NBU). Ziff. 3: Lebens-/Rentenversicherung. Ziff. 4: im Jahr 2026 erhaltene Sparzinsen. Ziff. 5: Krankentaggeld gemäss Lohnausweis. Deklaration der KK-Prämien wird vorausgesetzt (sonst kann Abzug verweigert werden).
- **Quellen:**
  - [Formular 5.2 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-2-2026/tg-form-05-2-2026__c0001.md) `tg-form-05-2-2026__c0001` – «1. private Krankenversicherung (netto, nach Abzug Prämienverbilligung gemäss Bestätigung Versicherung)»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0207.md) `tg-wl-2026__c0207` – «Person im Umfang der erhaltenen Prämienverbilligungen. In Ziffer 1 zu deklarieren ist»

<a id="form-5-2-b-1-b-4-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 B.1–B.4 – Maximaler Abzug Versicherungsprämien/Sparzinsen: gemeinsam besteuerte Fr. 7'000 Staat / 3'700 Bund (ohne Säule 2/3a: Bund 5'550); alleinstehend Fr. 3'500 / 1'800 (Bund ohne Säule 2/3a 2'700); je Kind/unterstützte Person Fr. 1'000 / 700 (Code 328, «B4»)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien (Zivilstand, Kinder, Säule 2/3a-Beiträge ja/nein)
- **Regel:** Der erhöhte Bundesabzug ohne Beiträge an Säule 2/3a (Fr. 5'550 bzw. 2'700) kann nicht zusammen mit dem ordentlichen Abzug beansprucht werden. Kinder-/Unterstützungszuschlag nur bei geltend gemachtem Kinder-/Unterstützungsabzug.
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 7'000 (Versicherungspraemien (Leben, Kranken, Unfall) und Sparzinsen: max. Fr. 7'000 fuer Verheiratete in ungetrennter Ehe.)** · Bund **CHF 3'700 (Versicherungsprämien und Zinsen von Sparkapitalien, Ehepaare in ungetrennter Ehe, mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 3'700.)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – WL 2026 c0209 und StG § 34 kennen die Erhoehung nur fuer die direkte Bundessteuer.** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an 2. Säule und Säule 3a: Höchstabzug CHF 5'550 (Erhöhung um die Hälfte).)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 3'500 (Versicherungspraemien und Sparzinsen: max. Fr. 3'500 fuer uebrige Steuerpflichtige.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 1'800.)**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – Nur direkte Bundessteuer, siehe WL 2026 c0209.** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: max. CHF 2'700.)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag zum Versicherungsabzug: Fr. 1'000 je minderjaehriges oder in Ausbildung stehendes Kind bzw. unterstuetzte Person (fuer die Kinder-/Unterstuetzungsabzug moeglich ist).)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**
- **Bund:** Bund: Fr. 3'700 / 1'800, Kind Fr. 700; ohne Säule 2/3a Fr. 5'550 / 2'700.
- **Quellen:**
  - [Formular 5.2 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-2-2026/tg-form-05-2-2026__c0002.md) `tg-form-05-2-2026__c0002` – «1. für gemeinsam besteuerte Personen (Eheleute / Partnerinnen oder Partner) 7000 3700»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0209.md) `tg-wl-2026__c0209` – «Diesen Abzug können Sie nicht zusammen mit dem ordentlichen Abzug von Fr. 3'700 bzw.»

<a id="form-5-2-c-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 C – Zulässiger Abzug: niedrigerer Betrag von «A5» und «B4» (Code 330) → Form. 1 Ziff. 14

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Staat Zeile 1 / Bund Zeile 2)
- **Regel:** Staat: min(A5; B4 Staat); Bund: min(A5; B4 Bund); Übertrag in Ziff. 14, Spalten Staat/Bund.
- **Bemerkung:** Hinweis Prüfung: WL c0213 nennt für den Staatsabzug «A7», Formular 5.2 und Bundesabsatz «A5» – massgebend ist das Total A (Code 324, «A5»).
- **Quellen:**
  - [Formular 5.2 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-2-2026/tg-form-05-2-2026__c0003.md) `tg-form-05-2-2026__c0003` – «1. Staatssteuer: der niedrigere Betrag von «A5» oder «B4 Staat» 330»
  - [WL TG 2026 S. 45–46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0213.md) `tg-wl-2026__c0213` – «Der für die direkte Bundessteuer zulässige Abzug entspricht dem niedrigeren der unter „A5“ und»

## Hilfsblatt Zuwendungen (Form. 6)

<a id="form-6-spalte-parteien-code-347-abzug-parteispenden"></a>
### Ziff. Form. 6 Spalte Parteien (Code 347) – Mitgliederbeiträge und Zuwendungen an politische Parteien (Total B) → Form. 1 Ziff. 15.5

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Quittung/Bescheinigung ab Fr. 1'000 pro Zuwendung
- **Regel:** Einzeln mit genauer Bezeichnung und Adresse der Partei auflisten; Maximum Staat Fr. 10'000 / Bund Fr. 10'600. Keine Pauschalvermerke.
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeitraege und Zuwendungen an politische Parteien: max. Fr. 10'000 (Staats- und Gemeindesteuern); Bund Fr. 10'600.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister / kantonales Parlament / mind. 3 % Stimmen): bis Gesamtbetrag CHF 10'600.)**
- **Bund:** Max. Fr. 10'600.
- **Quellen:**
  - [Formular 6 TG 2026 S. 1](../../chunks/tg/2026/tg-form-06-2026/tg-form-06-2026__c0003.md) `tg-form-06-2026__c0003` – «Staatssteuer: max. Fr. 10 000.– Bundessteuer: max. Fr. 10 600.–»
  - [Formular 6 TG 2026 S. 1](../../chunks/tg/2026/tg-form-06-2026/tg-form-06-2026__c0001.md) `tg-form-06-2026__c0001` – «Ab Fr. 1000.– pro Zuwendung reichen Sie bitte die entsprechende Quittung oder Bescheinigung»

<a id="form-6-spalte-gemeinn-tzig-code-366-abzug-spenden"></a>
### Ziff. Form. 6 Spalte gemeinnützig (Code 366) – Freiwillige Zuwendungen für gemeinnützige oder öffentliche Zwecke (Total) – Abzugsberechnung → Form. 1 Ziff. 23.2

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigung/Quittung der steuerbefreiten Institution ab Fr. 1'000 pro Zuwendung
- **Regel:** Staat: Selbstbehalt Fr. 200 (nur der übersteigende Betrag), dann Nettoeinkommen (Ziff. 22) bis Fr. 40'000: max. Fr. 8'000; darüber max. 20% des Nettoeinkommens. Bund: ab Fr. 100 gesamthaft, ohne Selbstbehalt, max. 20% des Nettoeinkommens.
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 200 (Freiwillige Zuwendungen: abziehbar, soweit sie gesamthaft Fr. 200 uebersteigen (Selbstbehalt Fr. 200). Bund: ab Fr. 100 ohne Selbstbehalt.)** · Bund **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn im Steuerjahr mindestens CHF 100 erreicht.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: max. 20 % des Nettoeinkommens (Ziff. 22); bei Nettoeinkommen bis Fr. 40'000 max. Fr. 8'000.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**
- **Bund:** Bund: max. 20% des Nettoeinkommens, kein Selbstbehalt (ab Fr. 100).
- **Quellen:**
  - [Formular 6 TG 2026 S. 1](../../chunks/tg/2026/tg-form-06-2026/tg-form-06-2026__c0003.md) `tg-form-06-2026__c0003` – «über Fr. 40000.–: max. 20% vom Nettoeinkommen 366»
  - [WL TG 2026 S. 46–47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0218.md) `tg-wl-2026__c0218` – «Übertragen Sie die geleisteten freiwilligen Zuwendungen (Maximalabzüge beachten) auf Seite 3 der»

## Hilfsblatt Schuldenverzeichnis (Form. 4.1)

<a id="form-4-1-a-schulden-privat"></a>
### Ziff. Form. 4.1 A – Privatschulden: Gläubiger, Schuld am 31.12., Zinssatz, fällige Schuldzinsen; Total (Code 455 Schulden / 286 Zinsen)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Hypothekar-/Kreditbestätigung der Bank per 31.12.2026 mit Zinsausweis 2026
- **Regel:** Gläubiger/in mit genauer Adresse und Zinssatz unerlässlich. Nur 2026 fällig gewordene Schuldzinsen (keine Ratazinsen). Amortisationen sind keine Schuldzinsen.
- **Quellen:**
  - [Formular 4.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-1-2026/tg-form-04-1-2026__c0001.md) `tg-form-04-1-2026__c0001` – «Total Privatschulden 455 286»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0169.md) `tg-wl-2026__c0169` – «Unerlässlich ist insbesondere die Angabe der Gläubigerin bzw. des Gläubigers»

<a id="form-4-1-b-schulden-privat"></a>
### Ziff. Form. 4.1 B – Geschäftsschulden: Gläubiger, Schuld am 31.12., Zinssatz, fällige Schuldzinsen; Total (Code 460 / 288)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz/Schuldenaufstellung Geschäft
- **Regel:** Schuldzinsen aus selbständiger Erwerbstätigkeit hier nur, wenn nicht bereits im Einkommen Ziff. 2 abgezogen.
- **Quellen:**
  - [Formular 4.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-1-2026/tg-form-04-1-2026__c0002.md) `tg-form-04-1-2026__c0002` – «Total Geschäftsschulden 460 288»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0170.md) `tg-wl-2026__c0170` – «Tragen Sie Schuldzinsen aus selbständiger Erwerbstätigkeit hier nur ein, sofern Sie diese nicht»

<a id="form-4-1-c-schulden-privat"></a>
### Ziff. Form. 4.1 C – Zusammenzug: Total Privat- und Geschäftsschulden (Code 466) → Form. 1 Ziff. 34; Total Schuldzinsen (Code 290) → Form. 1 Ziff. 11

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Total Schulden in Ziff. 34 (Seite 4), Total Schuldzinsen in Ziff. 11 (Seite 3).
- **Quellen:**
  - [Formular 4.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-1-2026/tg-form-04-1-2026__c0003.md) `tg-form-04-1-2026__c0003` – «Total Privat- und Geschäftsschulden 466 290»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0169.md) `tg-wl-2026__c0169` – «Übertragen Sie das Total der Schuldzinsen in Ziffer 11 auf Seite 3, und das»

## Hilfsblatt Wertschriftenverzeichnis (Form. 2)

<a id="form-2-spalten-1-9-seite-2-3-einkommen-wertschriften"></a>
### Ziff. Form. 2 Spalten 1–9 (Seite 2/3) – Detailverzeichnis: Bezeichnung (Valor/ISIN/IBAN), Zugang/Abgang, Steuerwert 31.12.2026 (Sp. 7), Bruttoertrag mit Verrechnungssteuerabzug (Sp. 8, Kolonne A), ohne Verrechnungssteuerabzug (Sp. 9, Kolonne B)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → E-Steuerauszug / Steuerauszug der Bank (Steuerwerte 31.12., Bruttoerträge); Dividenden-/Zinsabrechnungen; Lotterie-/Spielgewinnbestätigung
- **Regel:** Sp. 8: Erträge mit Verrechnungssteuerabzug (CH-Dividenden/-Zinsen, Kontozinsen über Fr. 200 brutto/Jahr oder mehrfache Vergütung, Lotterietreffer über Fr. 1'000). Sp. 9: Erträge ohne VSt-Abzug (Kleinzinsen bis Fr. 200, ausländische Titel und Guthaben, Darlehen, Hypothekarforderungen, Ausgleichs-/Rückerstattungszinsen). Brutto deklarieren (Marchzinsen etc.). Steuerwert = Börsenkurs Ende Dezember 2026 (ESTV-Kursliste). Kinder-Vermögen Jg. 2008 und jünger mitdeklarieren. Codes zur Zuordnung (01–06: Nutzniessung, Geschäftsvermögen, Erbschaft, qualifizierte Beteiligung). Ausländische Quellensteuern: Formular DA-1. Steuerauszug der Bank kann das Detail ersetzen und bleibt bei den Akten.
- **Bund:** Gleiche Erträge für Staat und Bund (Steuerwerte nur Staatssteuer).
- **Quellen:**
  - [Formular 2 TG 2026 S. 2](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0005.md) `tg-form-02-2026__c0005` – «Detailverzeichnis Wertschriften und Guthaben»
  - [WL TG 2026 S. 32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0150.md) `tg-wl-2026__c0150` – «Dies gilt auch für Zinsen von Bank- und Postkonti aller Art, soweit die Brutto-»
  - [WL TG 2026 S. 32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0152.md) `tg-wl-2026__c0152` – «Bank- und Postkonti aller Art, deren Bruttozins im Kalenderjahr Fr. 200 nicht übersteigt und»

<a id="form-2-ziff-7-im-formular-chunk-17-code-148-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. Form. 2 Ziff. 7 (im Formular-Chunk «17», Code 148) – Vermögensverwaltungskosten (Code 148)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Depotgebührenausweis der Bank (nur Verwahrung/Verwaltung)
- **Regel:** Pauschal 2 Promille des Steuerwerts der durch Dritte verwalteten Wertschriften des Privatvermögens, höchstens Fr. 6'000 (Darlehen, Bankguthaben, nichtkotierte qualifizierte Beteiligungen nicht in der Basis); höherer Nachweis vorbehalten. Abziehbar: Depotgebühren; nicht abziehbar: Kommissionen, Anlageberater, Tresor.
- **Bemerkung:** Ziffernbezeichnung im Formular-Chunk (c0007) ist durch Layout verfälscht («11.–19.»); Wegleitung nennt Ziff. 1–10 (Ziff. 7 = Vermögensverwaltungskosten). Original-PDF Seite 2 prüfen.
- **Quellen:**
  - [Formular 2 TG 2026 S. 2](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0006.md) `tg-form-02-2026__c0006` – «17. Vermögensverwaltungskosten Code 148»
  - [WL TG 2026 S. 33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0158.md) `tg-wl-2026__c0158` – «Der Pauschalabzug beträgt maximal Fr. 6'000.»

<a id="form-2-ziff-8-im-formular-chunk-18-code-145-einkommen-lotterie-gewinne"></a>
### Ziff. Form. 2 Ziff. 8 (im Formular-Chunk «18», Code 145) – Einsatzkosten für steuerbare Gewinne aus Geldspielen (Code 145)

- **Schlüssel:** `einkommen.lotterie_gewinne` (Lotterie-/Geldspielgewinne (steuerbarer Teil)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Gewinnbestätigung (Lotterie, Grossspiel, Online-Spielbank)
- **Regel:** Pauschal 5% jedes einzelnen steuerbaren Gewinns (Lotterien/Geschicklichkeitsspiele zur Verkaufsförderung, Grossspiele), max. Fr. 5'000 pro Gewinn Staat; effektive Einsatzkosten nicht geltend machbar. In der Steuererklärung den Staats-Maximalabzug deklarieren; Korrektur Bund von Amtes wegen.
- **Limiten:**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'000'000 (Einzelne Gewinne aus BGS-Grossspielen und Online-Spielbankenspielen bis Fr. 1'000'000 steuerfrei; nur der Mehrbetrag ist steuerbar (Bund: Fr. 1'071'000). Kleinspiele nach BGS vollstaendig steuerfrei.)** · Bund **CHF 1'071'000 (Einzelne Gewinne aus nach BGS zugelassenen Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'071'000; darüber steuerbar (abzüglich Einsatzkosten nach Art. 33 Abs. 4 DBG).)**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'000 (Einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsfoerderung bis Fr. 1'000 steuerfrei; wird die Grenze ueberschritten, ist der gesamte Gewinn steuerbar. Auslaendische Lotterien voll steuerbar. Bund: Freigrenze Fr. 1'100.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (Art. 1 Abs. 2 lit. d und e BGS) steuerfrei, sofern die Grenze von CHF 1'100 nicht überschritten wird. Gewinne aus Kleinspielen (BGS) sind steuerfrei.)**
- **Bund:** Max. Fr. 5'400 pro Gewinn (Korrektur von Amtes wegen).
- **Bemerkung:** Online-Spielbankenspiele (nach Bundesgesetz über die Spielbanken zugelassen): abgezogen werden die vom Online-Spielerkonto abgebuchten Spieleinsätze, Maximalabzug Staat Fr. 25'000 / Bund Fr. 26'800 (WL c0161); in der Steuererklärung Staats-Maximum deklarieren, Bund-Korrektur von Amtes wegen. Nummerierung: Wegleitung c0160 nennt «Ziffer 9» für den Pauschalabzug, das Formular zeigt Einsatzkosten vor dem Total (Ziff. 9) – Zeilennummer im Original-PDF prüfen.
- **Quellen:**
  - [Formular 2 TG 2026 S. 2](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0006.md) `tg-form-02-2026__c0006` – «Einsatzkosten und Spieleinsätze für steuerbare Gewinne aus Geldspielen»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0160.md) `tg-wl-2026__c0160` – «pro Gewinn Fr. 5'000 und bei der direkten Bundessteuer Fr. 5'400.»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0161.md) `tg-wl-2026__c0161` – «Fr. 25'000 und bei der direkten Bundessteuer Fr. 26'800.»

<a id="form-2-ziff-9-codes-410-150-berechnung-total"></a>
### Ziff. Form. 2 Ziff. 9 (Codes 410 / 150) – Total Steuerwert (Code 410 → Form. 1 Ziff. 30.1) und steuerbarer Ertrag (Code 150 → Form. 1 Ziff. 4)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Total Steuerwerte = Zwischentotal minus Geschäftswertschriften; Total steuerbarer Ertrag = Zwischentotal minus Geschäftsanteil, Vermögensverwaltungskosten und Einsatzkosten.
- **Quellen:**
  - [Formular 2 TG 2026 S. 2](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0006.md) `tg-form-02-2026__c0006` – «Total Steuerwert und steuerbarer Ertrag»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0162.md) `tg-wl-2026__c0162` – «Steuerwerte von Wertschriften und Guthaben im Privatvermögen übertragen Sie in Ziffer 30.1 auf»

<a id="form-2-ziff-10-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 2 Ziff. 10 – Verrechnungssteueranspruch: 35% von Bruttoertrag Total A (Spalte 8)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Steuerauszug/Dividendenabrechnung mit Verrechnungssteuerabzug; Auszahlungskonto S. 1 Formular 1
- **Regel:** 35% der Bruttoerträge Kolonne A (Sp. 8). Rückerstattung nur bei Wohnsitz im Kanton TG am 31.12.2026 und ordnungsgemässer Deklaration der Erträge; Auszahlung auf das gespeicherte Konto (Formular 1 Seite 1). Unterschrift auf Formular 2 erforderlich.
- **Quellen:**
  - [Formular 2 TG 2026 S. 2](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0006.md) `tg-form-02-2026__c0006` – «10. Verrechnungssteueranspruch: 35% von Bruttoertrag Total A»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0166.md) `tg-wl-2026__c0166` – «Ein Anspruch auf Rückerstattung der Verrechnungssteuer besteht nur, wenn Sie die Erträge in der»

<a id="form-2-letzte-seite-ziff-1-3-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. Form. 2 letzte Seite Ziff. 1–3 – Hilfsblatt qualifizierte Beteiligungen im Privatvermögen: Name/Sitz, Beteiligungsquote, Beteiligungsertrag; Teilbesteuerungsabzug Staat 40% / Bund 30% (→ Form. 1 Ziff. 15.6)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Dividendenabrechnung; Nachweis Beteiligungsquote (≥10%)
- **Regel:** Antrag durch Ausfüllen des Hilfsblatts nötig. Staat 40% / Bund 30% des Total Beteiligungsertrags (Ziff. 2); Übertrag in Ziff. 15.6 beider Spalten. Beteiligungen im Geschäftsvermögen separat über Formular 14.
- **Bund:** Bund 30%.
- **Quellen:**
  - [Formular 2 TG 2026 S. 4](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0008.md) `tg-form-02-2026__c0008` – «3. Teilbesteuerungsabzug (Staatssteuer 40% / Bundessteuer 30%)»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0164.md) `tg-wl-2026__c0164` – «Die Durchführung des Teilbesteuerungsverfahrens ist jeweils zu beantragen.»

## Hilfsblatt Liegenschaften (Form. 7)

<a id="form-7-steuerwert-vermoegen-liegenschaften"></a>
### Ziff. Form. 7 Steuerwert – Steuerwert der Liegenschaft (je Liegenschaft; Total Code 430 → Form. 1 Ziff. 31)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftensteuerrechnung/Schätzungsverfügung (Steuerwert)
- **Regel:** Rechtskräftiger amtlicher Verkehrswert (Ertragswert bei Landwirtschaft); Zugangs-/Wegfalldatum bei Kauf/Verkauf/Erbgang angeben.
- **Quellen:**
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0003.md) `tg-form-07-2026__c0003` – «Total Steuerwerte 430»
  - [WL TG 2026 S. 51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0238.md) `tg-wl-2026__c0238` – «Deklarieren Sie hier den Steuerwert Ihrer Liegenschaft»

<a id="form-7-mietwert-selbstgenutzt-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 7 Mietwert selbstgenutzt – Mietwert selbstgenutzt (indexierter Eigenmietwert)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftensteuerrechnung/Schätzung mit Mietwertindex 2026
- **Regel:** Mietwert gemäss rechtskräftiger Schätzung, jährlich indexiert; 2026-Wert in der Regel aus der Liegenschaftensteuerrechnung 2027 ersichtlich. Zweit-/Ferienwohnungen und unentgeltlich oder unterpreislich an Nahestehende überlassene Liegenschaften: Mietwert zu 100%.
- **Quellen:**
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0002.md) `tg-form-07-2026__c0002` – «Mietwert selbstgenutzt»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0221.md) `tg-wl-2026__c0221` – «Die Mietwerte aus Selbstnutzung werden jährlich indexiert.»

<a id="form-7-selbstnutzungsabzug-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 7 Selbstnutzungsabzug – Selbstnutzungsabzug (Staatssteuer / Bundessteuer) und steuerbarer Eigenmietwert

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Rechenzeile (Mietwert minus Abzug)
- **Regel:** Nur für am Wohnsitz selbstgenutzte eigene Liegenschaften: Abzug 40% Kanton / 20% Bund vom Mietwert. Kein Abzug bei Zweit-/Ferienwohnungen, landwirtschaftlich geschätzten Liegenschaften und an Nahestehende überlassenen Liegenschaften (100% steuerbar).
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **40 % (Selbstnutzungsabzug: 40 % vom Mietwert fuer am Wohnsitz selbstgenutztes Wohneigentum (Bund: 20 %). Kein Abzug bei Zweit-/Ferienwohnungen, landwirtschaftlichen Liegenschaften, an Nahestehende ueberlassenen Objekten.)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Bund:** Selbstnutzungsabzug Bund 20% (Kanton 40%).
- **Quellen:**
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0002.md) `tg-form-07-2026__c0002` – «Selbstnutzungsabzug»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0222.md) `tg-wl-2026__c0222` – «Für am Wohnsitz selbstgenutzte eigene Liegenschaften können Sie vom Mietwert aus Selbst-»

<a id="form-7-miet-pachtzinsen-einkommen-liegenschaften-mietertrag"></a>
### Ziff. Form. 7 Miet-/Pachtzinsen – Miet- und Pachtzinsen sowie weitere Erträge → Bruttoertrag

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Mietzinsaufstellung/Mietverträge; Abrechnung Einspeisevergütung Photovoltaik
- **Regel:** Sämtliche Miet-/Pachtzinseinnahmen, Einspeisevergütung PV, Baurechtszinsen, Erträge aus Kiesausbeutung; auch die dem Hauswart als Arbeitsentgelt gewährte Mietzinsreduktion. Bruttoertrag = steuerbarer Eigenmietwert plus übrige Erträge.
- **Quellen:**
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0002.md) `tg-form-07-2026__c0002` – «Miet- und Pachtzinsen»
  - [WL TG 2026 S. 51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0241.md) `tg-wl-2026__c0241` – «Die Summe der steuerbaren Eigenmietwerte und der Miet- und Pachtzinserträge sowie allfällig wei-»

<a id="form-7-unterhalts-betriebskosten-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 7 Unterhalts-/Betriebskosten – Unterhalts- und Betriebskosten: Pauschal / Effektiv (Übertrag aus Formular 8)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Handwerkerrechnungen, Versicherungs-/Abgabenrechnungen, Abrechnung Stockwerkeigentümergemeinschaft; Formular 8 (bei effektiv)
- **Regel:** Wahlrecht pro Liegenschaft und Steuerperiode: Pauschale 10% (Gebäude bis 10 Jahre) oder 20% (älter) vom Mietertrag bzw. Eigenmietwert, oder effektive Kosten (Formular 8). Pauschale ausgeschlossen bei Geschäftsvermögen, vorwiegend geschäftlich genutzten Liegenschaften, unüberbauten Grundstücken und Baurecht. Checkbox pauschal/effektiv ankreuzen. Übertragbare Energiespar-/Rückbaukosten nur bei effektiven Kosten. Stockwerkeigentum: Hauswartskosten bei Selbstbewohnung in der Regel nur 50%.
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Pauschalabzug Liegenschaftsunterhalt: 10 % des Bruttomietertrags bzw. (Eigen-)Mietwerts fuer Gebaeude bis 10 Jahre alt (Ende Steuerperiode); wahlweise statt effektiver Kosten, je Liegenschaft und Periode.)** · Bund **10 % (Pauschalabzug Liegenschaftskosten (anstelle effektiver Kosten, Wahl pro Periode und Liegenschaft): 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist.)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt: 20 % fuer Gebaeude, die ueber 10 Jahre alt sind.)** · Bund **20 % (Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist.)**
- **Quellen:**
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0002.md) `tg-form-07-2026__c0002` – «Unterhalts-/Betriebskosten»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0235.md) `tg-wl-2026__c0235` – «10% für Gebäude, die am Ende der Steuerperiode bis zu zehn Jahre alt sind;»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0235.md) `tg-wl-2026__c0235` – «20% für Gebäude, die am Ende der Steuerperiode älter als zehn Jahre sind.»

<a id="form-7-nettoerfolg-totale-berechnung-total"></a>
### Ziff. Form. 7 Nettoerfolg / Totale – Nettoerfolg je Liegenschaft; Total Nettoerfolge Staat/Bund (Code 180 → Form. 1 Ziff. 8)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Bruttoertrag minus Unterhalts-/Betriebskosten)
- **Regel:** Bei selbstgenutzten Liegenschaften Nettoerfolg je Staat und Bund einzeln ermitteln (unterschiedlicher Selbstnutzungsabzug), sonst Staat berechnen und für Bund übernehmen.
- **Quellen:**
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0003.md) `tg-form-07-2026__c0003` – «Total Nettoerfolge 180»
  - [WL TG 2026 S. 51–52](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0242.md) `tg-wl-2026__c0242` – «Bei am Wohnsitz selbst genutzten Liegenschaften ist aufgrund der unterschiedlichen Höhe des»

## Hilfsblatt Liegenschaftsunterhalt (Form. 8)

<a id="form-8-rechnungsliste-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 8 Rechnungsliste – Einzelaufstellung Rechnungen: Datum, Rechnungssteller, Beschreibung, Zahlungsbetrag, davon Anlagekosten/Mehrwert, davon Unterhalts- und Betriebskosten

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Handwerkerrechnungen und Zahlungsnachweise (ab Fr. 1'000 pro Einzelbetrag Kopie beilegen)
- **Regel:** Ein Formular pro Liegenschaft; Kosten einzeln mit Rechnungsstellerin, Art der Arbeit und tatsächlich bezahltem Nettobetrag. Nicht abzugsfähige Anteile (Anlagekosten/Investitionen/Mehrwert, Lebenshaltungskosten) in die Spalte «Anlagekosten» ausscheiden; nur abzugsfähiger Anteil in «Unterhalts- und Betriebskosten». Zeitliche Abgrenzung nach Rechnungs- oder Zahlungsdatum der Steuerperiode 2026. Abgrenzung nach Merkblatt Liegenschaftenunterhalt/StP 34 Nr. 1–5.
- **Quellen:**
  - [WL TG 2026 S. 49](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0230.md) `tg-wl-2026__c0230` – «Pro Liegenschaft, für welche Sie effektive Unterhaltskosten geltend machen, füllen Sie bitte je ein»
  - [WL TG 2026 S. 47–48](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0223.md) `tg-wl-2026__c0223` – «Von den Einkünften aus Liegenschaften können Sie die in der Steuerperiode 2026 angefallenen»

<a id="form-8-f-rderbeitr-ge-bertragbare-kosten-abzug-liegenschaft-energie-umwelt"></a>
### Ziff. Form. 8 Förderbeiträge / übertragbare Kosten – Förderbeiträge Energiespar-/Umweltschutzmassnahmen (Abzug) und aus Vorjahren übertragbare Kosten (Energiesparen, Umweltschutz, Rückbau)

- **Schlüssel:** `abzug.liegenschaft.energie_umwelt` (Investitionen Energiesparen/Umweltschutz, Rückbaukosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Förderbescheide (Bund, Kanton, Gemeinde); Aufstellung übertragbarer Kosten aus 2024/2025
- **Regel:** Förderbeiträge mindern die abzugsfähigen Kosten. Ergibt sich durch Energiespar-/Umweltschutz- oder Rückbaukosten (Ersatzneubau) ein negatives Reineinkommen, sind die nicht verrechneten Kosten auf die beiden Folgeperioden übertragbar (Kosten 2026 bis längstens Steuerperiode 2028); nur im Rahmen effektiver Unterhaltskosten (keine Kumulation mit Pauschale).
- **Quellen:**
  - [Formular 8 TG 2026 S. 1](../../chunks/tg/2026/tg-form-08-2026/tg-form-08-2026__c0003.md) `tg-form-08-2026__c0003` – «Förderbeiträge für Energiespar- und Umweltschutzmassnahmen (Bund, Kanton, Gemeinde etc.)»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0233.md) `tg-wl-2026__c0233` – «Die übertragbaren Kosten können nur im Rahmen der effektiven Liegenschaftsunterhaltskosten gel-»

<a id="form-8-total-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 8 Total – Total Unterhalts- und Betriebskosten (Übertrag auf Formular 7)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Total abzugsfähiger Unterhalts- und Betriebskosten (nach Abzug Förderbeiträge, inkl. übertragbarer Kosten) → Formular 7 «effektiv».
- **Quellen:**
  - [Formular 8 TG 2026 S. 1](../../chunks/tg/2026/tg-form-08-2026/tg-form-08-2026__c0003.md) `tg-form-08-2026__c0003` – «Total Unterhalts- und Betriebskosten (Übertrag auf Formular 7)»
  - [WL TG 2026 S. 49–50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0232.md) `tg-wl-2026__c0232` – «Resultiert aufgrund der Geltendmachung von Investitionskosten für Energiespar- und»
