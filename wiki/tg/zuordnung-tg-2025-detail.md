---
typ: zuordnung-detail
titel: Zuordnung TG 2025 – Detail
jur: tg
jahre:
- 2025
generiert: tools/build_quick.py aus data/zuordnung/tg/2025.yaml (2026-11-09)
---

# TG 2025: Zuordnung Beleg → Ziffer – Detail

> Kompaktansicht: [quick/zuordnung-tg-2025.md](../../quick/zuordnung-tg-2025.md) · Formular: Steuererklärung 2025 TG (Formular 1, Staats-, Gemeinde- und direkte Bundessteuer) + Hilfsblätter Formular 2 (Wertschriftenverzeichnis), 4.1 (Schuldenverzeichnis), 4.2 (Berufsauslagen), 5.1 (Krankheitskosten/behinderungsbedingte Kosten), 5.2 (Versicherungsprämien), 6 (Zuwendungen), 7 (Liegenschaften), 8 (Liegenschaftsunterhalt) · Quelle der Wahrheit: `data/zuordnung/tg/2025.yaml`

## Personalien

<a id="seite-1-personalien-personalien"></a>
### Ziff. Seite 1 Personalien – Personalien, Berufs- und Familienverhältnisse (Stand 31.12.2025)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1: Name, Geburtsdatum, Zivilstand, Beruf, Arbeitgeber, Ergänzungsleistungen
- **Rein:** Personendaten per 31. Dezember 2025 → Name, Geburtsdatum, Zivilstand, Konfession, Beruf (je Person 1/2) · Lohnausweis → Arbeitgeber/in, Arbeitsort · EL-Verfügung AHV/IV → Kreuz «Beziehen Sie Ergänzungsleistungen» ja · Zuzug/Wegzug Ausland, Todesfall → «Dauer bei unterjähriger Steuerpflicht» von/bis
- **Rechnen:** keine Rechnung; Stichtag 31. Dezember 2025 bzw. Ende Steuerpflicht (Stichtagsprinzip)
- **Regel:** Massgebend sind die Verhältnisse am 31.12.2025 bzw. am Ende der Steuerpflicht (Stichtag). Gemeinsam besteuerte Personen: Person 1 und Person 2 in allen Formularen und Hilfsblättern durchgehend gleich zuordnen. Bei unterjähriger Steuerpflicht (Zuzug/Wegzug Ausland, Tod) Dauer von/bis oben links auf Seite 1 eintragen.
- **Beachten:** Person 1/Person 2 in allen Formularen und Hilfsblättern durchgehend gleich belegen.
- **Beachten:** Unterjährig nur bei Zuzug aus/Wegzug ins Ausland oder Tod: Dauer S. 1 links oben, nur Einkommen der Pflichtdauer.
- **Quellen:**
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0002.md) `tg-form-01-2025__c0002` – «Personalien, Berufs- und Familienverhältnisse am 31. Dezember 2025 oder am Ende der Steuerpflicht»
  - [WL TG 2025 S. 12](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0045.md) `tg-wl-2025__c0045` – «Achten Sie bitte darauf, in den Formularen unter Person 1 bzw. Person 2 durchgehend die Angaben»
  - [WL TG 2025 S. 5](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0009.md) `tg-wl-2025__c0009` – «Massgebend sind die Verhältnisse am Ende der Steuerperiode bzw. am Ende der Steuerpflicht.»
  - [WL TG 2025 S. 6](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0017.md) `tg-wl-2025__c0017` – «Bei unterjähriger Steuerpflicht ist auf der Steuererklärung, Seite 1, links oben die Dauer (von/bis)»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0048.md) `tg-wl-2025__c0048` – «Bei unterjähriger Steuerpflicht (Zuzug aus Ausland / Wegzug ins Ausland / Tod) ist nur das»
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0001.md) `tg-form-01-2025__c0001` – «Dauer bei unterjähriger Steuerpflicht:»

<a id="seite-1-kinder-personalien"></a>
### Ziff. Seite 1 Kinder – Kinder (minderjährig, in Ausbildung oder erwerbsunfähig), Unterhalt wird bestritten; Zusatzangaben bei getrennt besteuerten Eltern

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1: Vorname/Name, Geburtsdatum, im Haushalt, Schule/Lehrfirma, Ausbildungsende, Unterhaltsbeiträge, Sorgerecht, Obhut
- **Rein:** Geburtsdatum Kind (genau) → Geb.-datum, «In Ihrem Haushalt?» · Lehrvertrag/Schulbestätigung → Schule/Lehrfirma, Ausbildungsende (Kinder Jg. 2005 und älter) · Scheidungs-/Trennungsurteil, Sorgerechtsentscheid → Checkboxen Unterhaltsbeiträge, gemeinsames Sorgerecht, alternierende Obhut
- **Rechnen:** Folgeabzug Ziff. 25.1 je Kind (Stichtag 31. Dezember 2025): Kanton 7'400 / in Ausbildung Jg. 2006–2009: 8'500 / Jg. 2000–2005: 10'600; Bund 6'800
- **Regel:** Genaues Geburtsdatum angeben. Kinder mit Jahrgang 2005 und älter in Ausbildung: Ausbildungsstätte/Lehrfirma und voraussichtliches Ende der Ausbildung. Bei nicht gemeinsam besteuerten Eltern (getrennt, geschieden, Konkubinat mit gemeinsamen Kindern) Checkboxen Unterhaltsbeiträge/gemeinsames Sorgerecht/alternierende Obhut ausfüllen – sie steuern die Zuteilung von Kinderabzug, Versicherungsabzug, Vermögensfreibetrag und Tarif.
- **Beachten:** Getrennte Eltern: minderjährig → Kinderabzug beim Alimente-Empfänger (nicht Zahler); volljährig → i.d.R. beim Zahler.
- **Beachten:** Ohne Alimente hälftig: Kanton nur bei gem. Sorgerecht + alternierender Obhut; Bund schon bei gem. Sorgerecht.
- **Beachten:** Vermögen/Erträge Kinder Jg. 2008 und jünger in Formular 2 der Eltern; Jg. 2007 und älter versteuern selbst.
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 7'400 (Kinderabzug je Kind (nicht selbständig besteuert, in Ausbildung oder erwerbsunfähig; Steuerpflichtiger kommt für Unterhalt auf): CHF 7'400. Stichtag Ende Steuerperiode.)** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 8'500 (Kinderabzug erhöht sich für jedes in Ausbildung stehende Kind nach Vollendung des 16. Altersjahres auf CHF 8'500 (WL 2025: Jahrgang 2006-2009).)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Kinderabzug CHF 6'800 wie für Minderjährige (kein höherer Ausbildungsabzug))**
  - Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF): Kanton **CHF 10'600 (Kinderabzug in Ausbildung nach Vollendung des 20. Altersjahres bis höchstens zum vollendeten 26. Altersjahr: CHF 10'600 (WL 2025: Jahrgang 2000-2005). Keine Unterscheidung nach auswärtiger Ausbildung; Abstufung erfolgt nach Alter.)** · Bund **n/a – Bund: gleicher Kinderabzug CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).**
- **Quellen:**
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0003.md) `tg-form-01-2025__c0003` – «Minderjährige, in beruflicher Ausbildung stehende oder erwerbsunfähige Kinder, deren Unterhalt Sie bestreiten»
  - [WL TG 2025 S. 12](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0045.md) `tg-wl-2025__c0045` – «Für Kinder mit Jahrgang 2005 und älter, welche sich in Ausbildung befinden, geben Sie bitte»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0108.md) `tg-wl-2025__c0108` – «für jedes Kind in Ausbildung mit Jahrgang 2000 – 2005 Fr. 10'600 Fr. 6'800»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0108.md) `tg-wl-2025__c0108` – «für jedes Kind in Ausbildung mit Jahrgang 2006 – 2009 Fr. 8'500 Fr. 6'800»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0109.md) `tg-wl-2025__c0109` – «Der die Alimente leistende Elternteil, welcher diese Unter-»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0110.md) `tg-wl-2025__c0110` – «Das Vorliegen eines gemeinsamen Sorgerechts ohne alternierende Obhut reicht»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0112.md) `tg-wl-2025__c0112` – «Besteht ein gemeinsames Sorgerecht und fliessen keine Unterhaltsbeiträge, werden die Kin-»
  - [WL TG 2025 S. 30](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0139.md) `tg-wl-2025__c0139` – «Vermögen und Erträge von Kindern unter Ihrer elterlichen Sorge (Jahrgang 2008 und jünger).»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0107.md) `tg-wl-2025__c0107` – «am 31. Dezember 2025 bzw. am Ende der Steuerpflicht massgebend»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0111.md) `tg-wl-2025__c0111` – «Fliessen Unterhaltsbeiträge, ist»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0112.md) `tg-wl-2025__c0112` – «der Regel hat der Unterhaltszahlungen leistende Elternteil Anspruch auf den Abzug.»

<a id="seite-1-unterst-tzte-personen-personalien"></a>
### Ziff. Seite 1 Unterstützte Personen – Erwerbsunfähige und unterstützungsbedürftige Personen (Unterstützungsbetrag ≥ Fr. 12'000 Kanton / Fr. 6'800 Bund)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1: Vorname/Name, Geburtsdatum, im Haushalt, Adresse, Unterstützungsbetrag
- **Rein:** Zahlungsnachweise Unterstützung → Unterstützungsbetrag Fr. je Person · Bestätigung Wohnsitzgemeinde (Steuerausweis/Fürsorgebehörde) → Nachweis Unterstützungsbedürftigkeit
- **Rechnen:** Eintrag ab Unterstützung ≥ Kanton 12'000 / Bund 6'800 je Person; Folgeabzug Ziff. 25.2 je Person: Kanton 2'700 / Bund 6'800
- **Regel:** Nur Personen ohne Kinder-/Ehegattenstatus. Formular nennt Mindestbeitrag Fr. 12'000 (Kanton) bzw. Fr. 6'800 (Bund); Wegleitung kantonal: nachweislich mindestens 50% des betreibungsrechtlichen Existenzminimums, Unterstützungsbedürftigkeit durch Bestätigung der Wohnsitzgemeinde belegen. Abzug siehe Ziff. 25.2.
- **Beachten:** Kanton: Übernahme von mind. 50% des betreibungsrechtlichen Existenzminimums nachweisen (Steuerpraxis).
- **Beachten:** Nicht für Ehegatte/Partner und Kinder mit Kinderabzug oder abgezogenen Unterhaltsbeiträgen.
- **Beachten:** Erwerbsunfähig = gesundheitlich nicht arbeitsfähig; Stichtag Ende Steuerperiode, sonst kein Abzug (nicht pro rata).
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'700 (Unterstützungsabzug CHF 2'700 je erwerbsunfähige/unterstützungsbedürftige Person, für deren Unterhalt der Steuerpflichtige zur Hauptsache aufkommt (nicht für Ehegatten und Kinder mit Kinderabzug).)** · Bund **CHF 6'800 (Unterstützungsabzug pro erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mindestens in Höhe des Abzugs unterstützt; nicht für Ehegatten und Kinder mit Kinderabzug)**
- **Bemerkung:** Formulartext (Fr. 12'000 Kanton) und Wegleitung (mind. 50% des betreibungsrechtlichen Existenzminimums, Steuerpraxis) nennen unterschiedliche Kriterien; kein Widerspruch im Betrag des Abzugs, aber Mindestbeitrag in der Praxis nachprüfen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0004.md) `tg-form-01-2025__c0004` – «mindestens Fr. 12 000.– (Kanton) bzw. Fr. 6 800.– (Bund) unterstützen»
  - [WL TG 2025 S. 24–25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0114.md) `tg-wl-2025__c0114` – «lichen Existenzminimums der betreffenden erwerbsunfähigen und unterstützungsbedür»
  - [WL TG 2025 S. 24–25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0115.md) `tg-wl-2025__c0115` – «Die Unterstützungsbedürftigkeit ist durch eine Bestätigung der Wohnsitzgemeinde (Steuerausweis»
  - [WL TG 2025 S. 24–25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0115.md) `tg-wl-2025__c0115` – «Bei der direkten Bundessteuer beträgt der Unterstützungsabzug Fr. 6'800 für jede erwerbsunfähige»
  - [WL TG 2025 S. 24–25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0115.md) `tg-wl-2025__c0115` – «Nicht unter den Unterstützungsbeitrag fallen sowohl bei den Staats- und Gemeindesteuern als auch»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0107.md) `tg-wl-2025__c0107` – «kann der Sozialabzug nicht gewährt werden (auch nicht pro rata).»

<a id="seite-1-auszahlungskonto-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Seite 1 Auszahlungskonto – Auszahlungskonto für Steuerrückzahlungen und Rückerstattung Verrechnungssteuer (IBAN)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1: Kontoinhaber/in, IBAN, Bank/Post
- **Rein:** Bank-/Postkontoangaben → Kontoinhaber/in, IBAN, Bank/Post (nur Erstantrag oder Kontoänderung)
- **Rechnen:** keine Rechnung; ausbezahlt werden VSt-Anspruch (35% × Bruttoertrag Total A = Spalte 8 → Form. 2 Ziff. 10) + allfällige Steuerrückzahlungen
- **Regel:** Konto nur bei Erstantrag oder Kontoänderung ausfüllen (IBAN, Bank oder Post). Kontoänderungen nach Einreichung der Steuererklärung möglichst vermeiden (Verzögerung der Rückerstattung).
- **Beachten:** IBAN auch bei Postkonto angeben; Kontoänderung nach Einreichung vermeiden (Verzögerung).
- **Beachten:** VSt-Rückerstattung durch TG nur bei Wohnsitz TG am 31. Dezember 2025 und deklarierten Erträgen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0005.md) `tg-form-01-2025__c0005` – «Alle Rückerstattungen der Verrechnungssteuer sowie allfälliger Steuerrückzahlungen erfolgen auf»
  - [WL TG 2025 S. 35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0168.md) `tg-wl-2025__c0168` – «Um Verzögerungen bei der»
  - [WL TG 2025 S. 12](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0047.md) `tg-wl-2025__c0047` – «wie auch beim Postkonto die IBAN-Nummer an.»
  - [WL TG 2025 S. 35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0167.md) `tg-wl-2025__c0167` – «der Spalte 8 in Ziffer 3 (welches auch Beträge aus allfälligen Beiblättern einschliesst) sind 35%»
  - [WL TG 2025 S. 35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0167.md) `tg-wl-2025__c0167` – «Die Steuerverwaltung Thurgau kann die Verrechnungssteuer für die Fälligkeiten 2025 nur an»
  - [WL TG 2025 S. 35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0167.md) `tg-wl-2025__c0167` – «Ein Anspruch auf Rückerstattung der Verrechnungssteuer besteht nur, wenn Sie die Erträge in der»
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0006.md) `tg-form-02-2025__c0006` – «10. Verrechnungssteueranspruch: 35% von Bruttoertrag Total A»
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0005.md) `tg-form-01-2025__c0005` – «das von Ihnen bezeichnete Konto.»

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Haupterwerb unselbständig (Code 100 Person 1 / 101 Person 2)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 Nettolohn; Pauschalspesen (Ziff. 13.2) in die Vorspalte «Pauschalspesen»
- **Rein:** Lohnausweis (je Arbeitgeber) → Ziff. 11 Nettolohn · Lohnausweis → Pauschalspesen → Vorspalte «Pauschalspesen» · Aufstellung Trinkgelder/Naturalbezüge → Zuschlag, soweit nicht im Lohnausweis
- **Rechnen:** Σ Nettolohn LA Ziff. 11 aller Haupterwerb-Lohnausweise je Person + nicht im LA enthaltene Trinkgelder/Naturalbezüge; Pauschalspesen nur in Vorspalte
- **Regel:** Nettolohn gemäss Lohnausweis Ziff. 11 einsetzen (Brutto Ziff. 8 abzüglich AHV/IV/EO/ALV Ziff. 9 und BVG Ziff. 10). Pauschalspesen separat in der Vorspalte. Naturalbezüge/Trinkgelder, falls nicht im Lohnausweis, ergänzen. Alle Lohnausweise einreichen. Lohnausweis-Hinweise: Feld F (unentgeltliche Beförderung Wohn-/Arbeitsort, z.B. Geschäftsfahrzeug) angekreuzt = kein Fahrkostenabzug (Form. 4.2 Ziff. 2); Feld G (Kantinenverpflegung/Lunch-Checks) = nur halber Verpflegungsabzug (Form. 4.2 Ziff. 3.2); Ziff. 10.2 (Einkauf BVG) ist bereits im Nettolohn abgezogen und nicht nochmals in Ziff. 15.2 geltend zu machen; Ziff. 13.3 (Arbeitgeberbeiträge an Weiterbildung) mindert den Abzug Ziff. 16; Ziff. 15 Bemerkungen: Anzahl Schichttage (Beleg für Verpflegungsabzug), Teilzeit, Rektifikat, mehrere Lohnausweise.
- **Beachten:** Steuerbar auch Pauschalspesen ohne entsprechende Ausgaben, Zulagen, Dienstaltersgeschenke, Trinkgelder.
- **Beachten:** Naturalbezüge nicht im LA: volle Verpflegung + Unterkunft i.d.R. Fr. 11'880 im Jahr.
- **Beachten:** Geschäftsfahrzeug: Privatanteil 0.9 % pro Monat im LA deckt Arbeitsweg → kein Fahrkostenabzug in Form. 4.2.
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0006.md) `tg-form-01-2025__c0006` – «1.1 Haupterwerbstätigkeit   Person 1   100»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0049.md) `tg-wl-2025__c0049` – «In die Steuererklärung ist der in Ziffer 11 des Lohnausweises aufgeführte Nettolohn einzusetzen.»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «In diesem Feld ist der für die Steuererklärung massgebende Nettolohn anzugeben.»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0050.md) `tg-wl-2025__c0050` – «beträgt der Wert für volle Verpflegung und Unterkunft in der Regel Fr. 11'880 im Jahr»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0176.md) `tg-wl-2025__c0176` – «Der im Lohnausweis berücksichtigte Privatanteil Fahrzeug von 0.9 % pro Monat»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0052.md) `tg-wl-2025__c0052` – «Von Ihren Arbeitgebenden erhaltene Pauschalspesen für die Haupt- und/oder Nebenerwerbstätig-»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Nebenerwerb unselbständig (Code 104 Person 1 / 105 Person 2), inkl. VR-/Behördenentschädigungen

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 Nettolohn des Nebenerwerbs
- **Rein:** Lohnausweis Nebenerwerb → Ziff. 11 Nettolohn · Abrechnung Sitzungsgelder/VR-Honorare/Tantiemen/Behördenentschädigung → Entschädigung (soweit nicht im LA) · Soldabrechnung Feuerwehr → Sold Kernaufgaben über Freibetrag + Kader-/Funktionszulagen · Lohnausweis → Pauschalspesen Nebenerwerb → Vorspalte
- **Rechnen:** Σ Nettolöhne Nebenerwerb je Person (ohne Freigrenze) + max(0; Feuerwehrsold Kernaufgaben − Kanton 5'000) + Kader-/Funktionszulagen (Bund 5'300: Korrektur StV)
- **Regel:** Sämtliches Einkommen aus unselbständigem Nebenerwerb ohne Freigrenze deklarieren (auch Sitzungsgelder, VR-Honorare, Tantiemen). Feuerwehrsold: Kernaufgaben steuerfrei bis Fr. 5'000 (Staat) bzw. Fr. 5'300 (Bund); über dem Freibetrag steuerbar; in der Steuererklärung die kantonal steuerbaren Einkünfte deklarieren, Bund korrigiert die Steuerverwaltung von Amtes wegen. Berufsauslagen Nebenerwerb: Form. 4.2 Ziff. 6.
- **Beachten:** Ohne Freigrenze (AHV/UVG unbeachtlich); auch Hauswart-Mietzinsreduktion = normaler − reduzierter Mietzins.
- **Beachten:** Feuerwehrsold: kantonal steuerbaren Betrag eintragen; Bundeskorrektur durch StV von Amtes wegen.
- **Beachten:** Auslagen → Form. 4.2 Ziff. 6: 20% der Nettoeinkünfte (min. 800, max. 2'400) oder effektiv, keine Kumulation.
- **Limiten:**
  - Feuerwehrsold steuerfrei bis (CHF): Kanton **CHF 5'000 (Sold der Milizfeuerwehrleute für Kernaufgaben steuerfrei bis CHF 5'000 pro Jahr (Kanton); Pauschalzulagen für Kader, Funktionszulagen, administrative und freiwillige Dienstleistungen sind steuerbar.)** · Bund **CHF 5'300 (Sold der Milizfeuerwehrleute für Kernaufgaben steuerfrei bis CHF 5'300 pro Jahr)**
- **Bund:** Feuerwehrsold-Freibetrag Bund Fr. 5'300 (Kanton Fr. 5'000).
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0006.md) `tg-form-01-2025__c0006` – «1.2 Nebenerwerbstätigkeit   Person 1   104»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0051.md) `tg-wl-2025__c0051` – «Daher ist sämtliches Einkommen aus einer unselbständigen Nebenerwerbstätigkeit»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0052.md) `tg-wl-2025__c0052` – «Fr. 5'000 bei der Staats- und Gemeindesteuer;»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0191.md) `tg-wl-2025__c0191` – «Der Abzug beträgt 20% der Nettoeinkünfte, mindestens aber Fr. 800 und höchstens»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0191.md) `tg-wl-2025__c0191` – «Eine Kumulation von Pauschalabzug und effektiven Kosten ist»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0049.md) `tg-wl-2025__c0049` – «In die Steuererklärung ist der in Ziffer 11 des Lohnausweises aufgeführte Nettolohn einzusetzen.»

<a id="1-3-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 1.3 – Im vereinfachten Abrechnungsverfahren bereits versteuerter Bruttolohn (Code 106 / 107)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der AHV-Ausgleichskasse (Bruttolohnsumme)
- **Rein:** Bescheinigung AHV-Ausgleichskasse (vereinfachtes Abrechnungsverfahren) → Bruttolohnsumme je Person in Vorkolonne
- **Rechnen:** nur Information: Σ Bruttolöhne vereinfachtes Verfahren je Person; nicht in Zwischentotal Ziff. 6, weder steuerbar noch satzbestimmend
- **Regel:** Nur Information (Vorkolonne): im vereinfachten Verfahren bereits versteuerte Löhne werden weder als steuerbares noch als satzbestimmendes Einkommen berücksichtigt und fliessen nicht ins Zwischentotal Ziff. 6. Bescheinigung beilegen.
- **Beachten:** Bescheinigung der AHV-Ausgleichskasse beilegen.
- **Beachten:** Bereits per Quellensteuerabzug besteuert: nur Vorkolonne 1.3, weder steuerbar noch satzbestimmend.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0006.md) `tg-form-01-2025__c0006` – «1.3 Im vereinfachten Abrechnungsverfahren bereits versteuerter Bruttolohn»
  - [WL TG 2025 S. 14](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0053.md) `tg-wl-2025__c0053` – «Löhne werden nicht in die Berechnung des Zwischentotals unter Ziffer 6 miteinbezogen.»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit Haupterwerb (Code 112 Person 1 / 113 Person 2)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz und Erfolgsrechnung bzw. Aufstellung Einnahmen/Ausgaben/Aktiven/Passiven; ggf. Formular 14 (Fragebogen Selbständigerwerbende)
- **Rein:** Bilanz + Erfolgsrechnung 2025 (unterzeichnet), Privatkonto, Abschreibungstabelle → Reingewinn · Vereinfachte Buchführung: Einnahmen/Ausgaben, Aktiven/Passiven, Privatentnahmen/-einlagen → Reingewinn · Bescheinigung Kollektiv-/Kommanditgesellschaft → Anteil Gesellschafterlohn, Gewinn, Kapitalzins · Formular 14 → Einkommen nach Teilbesteuerung (Spalte Kanton)
- **Rechnen:** Reingewinn lt. Abschluss (nach geschäftsmässig begründetem Aufwand, inkl. Naturalbezüge); qual. Beteiligungen GV via Form. 14: Kanton 60% / Bund 70%
- **Regel:** Reingewinn nach geschäftsmässig begründeten Kosten (negativer Betrag mit Vorzeichen). Persönliche 2.-Säule-Beiträge nur im Umfang Arbeitgeberanteil im Geschäftsergebnis; Privatanteil und alle Säule-3a-Beiträge nur in Ziff. 13 bzw. 15.2. Direkt ausbezahlte Familienzulagen nicht hier, sondern Ziff. 3.4. Liquidationsgewinne (ab 55 / Invalidität) siehe Ziff. 23.3. Teilbesteuerung Beteiligungen im Geschäftsvermögen (Kanton 60% / Bund 70%) über Formular 14.
- **Beachten:** Eigene 2. Säule nur AG-Anteil (ohne Personal: Hälfte) im Geschäft; Rest + alle 3a-Beiträge → Ziff. 13 bzw. 15.2.
- **Beachten:** Direkt ausbezahlte Familienzulagen → Ziff. 3.4; bereits abgerechneter Lohn Ehepartner nicht hier.
- **Beachten:** Liquidationsgewinn bei Aufgabe nach vollendetem 55. Altersjahr / Invalidität → Abzug Ziff. 23.3 (separate Besteuerung).
- **Bund:** Teilbesteuerung Beteiligungen Geschäftsvermögen beim Bund 70% (Kanton 60%); Steuerverwaltung nimmt Bundeskorrektur von Amtes wegen vor.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0006.md) `tg-form-01-2025__c0006` – «2.1 Haupterwerbstätigkeit   Person 1   112»
  - [WL TG 2025 S. 14–15](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0058.md) `tg-wl-2025__c0058` – «Deklarieren Sie hier aus Industrie, Handel, Gewerbe, freien Berufen sowie Land- und Forstwirtschaft»
  - [WL TG 2025 S. 15](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0061.md) `tg-wl-2025__c0061` – «sondern sind ausschliesslich in Ziffer 13 bzw. 15.2 der»
  - [WL TG 2025 S. 14](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0056.md) `tg-wl-2025__c0056` – «Bilanz und Erfolgsrechnung des im Jahre 2025 abgeschlossenen Geschäftsjahrs»
  - [WL TG 2025 S. 14](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0057.md) `tg-wl-2025__c0057` – «gegliederte Aufstellung von Einnahmen und Ausgaben;»
  - [WL TG 2025 S. 14](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0057.md) `tg-wl-2025__c0057` – «die Bescheinigung der Gesellschaft über Ihren Anteil am Einkommen»
  - [WL TG 2025 S. 16](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0068.md) `tg-wl-2025__c0068` – «nur zu 60% und beim Bund nur zu 70% besteuert.»
  - [WL TG 2025 S. 17](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0074.md) `tg-wl-2025__c0074` – «In die Steuererklärung ist das in der Spalte Kanton berechnete steuerbare Einkommen zu»
  - [WL TG 2025 S. 15](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0063.md) `tg-wl-2025__c0063` – «Direkt ausbezahlte Familienzulagen sind nicht AHV-pflichtig.»
  - [WL TG 2025 S. 16](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0065.md) `tg-wl-2025__c0065` – «unter Ziffer 23.3 wieder von den Einkünften in Abzug bringen»
  - [WL TG 2025 S. 16](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0065.md) `tg-wl-2025__c0065` – «Erwerbstätigkeit nach dem vollendeten 55. Altersjahr oder wegen»
  - [WL TG 2025 S. 15](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0060.md) `tg-wl-2025__c0060` – «Deklarieren Sie die Einkünfte nach Abzug der geschäftsmässig begründeten Gewinnungskosten.»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Selbständige Erwerbstätigkeit Nebenerwerb (Code 116 Person 1 / 117 Person 2)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Aufstellung Einnahmen/Ausgaben des Nebenerwerbs
- **Rein:** Aufstellung Einnahmen/Ausgaben Nebenerwerb (Provisionen, Gutachter-, Buchhaltungshonorare, Privatunterricht) → Nettoeinkommen · Landw. Nebengewerbe: Buchhaltungsabschluss bzw. Formular 18 → Einkommen
- **Rechnen:** Nettoeinkommen = Einnahmen − geschäftsmässig begründete Kosten je Person; Regeln Ziff. 2.1 sinngemäss
- **Regel:** Nettoeinkommen aus selbständigem Nebenerwerb (z.B. Provisionen, Gutachterhonorare, Privatunterricht). Ausführungen zu Ziff. 2.1 gelten sinngemäss.
- **Beachten:** Landw. Nebengewerbe inkl. Viehhandel: Abschluss beilegen; ohne Buchhaltung Formular 18 (Fragebogen Landwirte).
- **Beachten:** Gewerbsmässiger Wertpapierhandel steuerbar: gehandelte Titel auf separatem Blatt auflisten.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0006.md) `tg-form-01-2025__c0006` – «2.2 Nebenerwerbstätigkeit   Person 1»
  - [WL TG 2025 S. 17](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0074.md) `tg-wl-2025__c0074` – «Deklarieren Sie hier ein Netto-Einkommen aus einer selbständigen Nebenerwerbstätigkeit»
  - [WL TG 2025 S. 17](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0075.md) `tg-wl-2025__c0075` – «Fragebogen für Landwirte (Formular 18)»
  - [WL TG 2025 S. 17](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0075.md) `tg-wl-2025__c0075` – «gewerbsmässigem Wertpapierhandel steuerbar. Diese sind auf einem separaten Blatt»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV-/IV-Renten (Code 130 Person 1 / 131 Person 2)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung AHV/IV (Jahresbetrag brutto)
- **Rein:** Rentenbescheinigung AHV/IV (Ausgleichskasse) → Jahresbetrag 2025 je Person
- **Rechnen:** 100% × Σ AHV-/IV-Renten 2025 je Person (Kanton und Bund)
- **Regel:** 100% steuerbar (Kanton und Bund). Steuerfrei und nicht anzugeben: Ergänzungsleistungen AHV/IV, Sozialhilfe, Genugtuungszahlungen. Beim Bezug von EL Kreuz auf Seite 1 setzen.
- **Beachten:** Nicht deklarieren: Ergänzungsleistungen AHV/IV, Sozialhilfe, Genugtuung (steuerfrei); EL-Bezug auf S. 1 ankreuzen.
- **Beachten:** AHV-Rentner: Abzug Ziff. 25.3 nur kantonal, max. 4'200 je nach Reineinkommen Ziff. 24 (Tabelle WL).
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0007.md) `tg-form-01-2025__c0007` – «3.1 AHV-/IV-Renten   Person 1   130»
  - [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0076.md) `tg-wl-2025__c0076` – «Renten der AHV/IV sind sowohl bei den Staats- und Gemeindesteuern als auch bei der direkten»
  - [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0076.md) `tg-wl-2025__c0076` – «Ergänzungsleistungen der AHV und IV;»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0116.md) `tg-wl-2025__c0116` – «je nach Höhe ihres Reineinkommens gemäss Ziffer 24 der Steuererklärung, kantonal Anspruch»
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0002.md) `tg-form-01-2025__c0002` – «Beziehen Sie Ergänzungs-»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen (2. Säule, SUVA, Säule 3a, 3b, Leibrenten) mit steuerbarem Bruttobetrag und Prozent (Code 132 Person 1 / 133 Person 2)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente), Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Rentenbescheinigung der Vorsorgeeinrichtung/Versicherung: steuerbarer Bruttobetrag und Prozentsatz
- **Rein:** Rentenbescheinigung Pensionskasse/SUVA → Bruttobetrag + Prozent (BVG 100, Übergangsrecht 80) · Rentenbescheinigung Säule 3a / IV-Rente 3b → Bruttobetrag, 100% · Bescheinigung Versicherung Leibrente → steuerbarer Ertragsanteil + Überschussleistungen
- **Rechnen:** steuerbar = Bruttorente × Satz: BVG/3a/IV-Rente 3b 100%; Übergangsrecht 80%; Leibrente = Ertragsanteil lt. Bescheinigung + 70% × Überschussleistungen
- **Regel:** Bruttobetrag und steuerbaren Prozentsatz angeben. Renten aus beruflicher Vorsorge, gebundener Selbstvorsorge und Invaliditätsrenten (3b) zu 100%; Übergangsrecht 80% nur bei Rentenbeginn vor 1.1.1987 bzw. 1.1.1987–1.1.2002 mit Vorsorgeverhältnis per 31.12.1984/1986 und mind. 20% Eigenbeiträgen. Leibrenten: steuerbar im Ertragsanteil gemäss Bescheinigung, Überschussleistungen pauschal 70%. Bei mehr als zwei Renten Aufstellung beilegen.
- **Beachten:** 80% nur bei ≥ 20% Eigenbeiträgen + Rentenbeginn vor 1987 oder vor 2002 bei Vorsorge schon Ende 1984 (Bund 1986).
- **Beachten:** Mehr als zwei Renten: separate Aufstellung + Bescheinigungen beilegen.
- **Beachten:** Kapitalleistungen aus Vorsorge nicht hier, sondern Seite 4 unten.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0007.md) `tg-form-01-2025__c0007` – «3.2 Renten/Pensionen   Steuerbar Bruttobetrag / Fr.   in Prozent»
  - [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0077.md) `tg-wl-2025__c0077` – «Grundsätzlich sind Renten aus beruflicher Vorsorge, aus gebundener Selbstvorsorge sowie»
  - [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0078.md) `tg-wl-2025__c0078` – «Überschussleistungen sind pauschal zu 70% steuerbar.»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0084.md) `tg-wl-2025__c0084` – «sondern auf der Steuererklärung, Seite 4 unten, sind Kapitalleistungen aus»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigungen (Taggelder Kranken-/Unfall-/IV/ALV, Mutterschaft, EO) (Code 136 Person 1 / 137 Person 2)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Bescheinigung der Versicherung/Ausgleichskasse/ALV; Lohnausweis Ziff. 15 (Anzahl Tage mit Erwerbsausfallentschädigung)
- **Rein:** Taggeldabrechnung Kranken-/Unfallversicherung, SUVA, IV → Taggelder 2025 (soweit nicht im Lohnausweis) · Bescheinigung Arbeitslosenkasse → ALV-Taggelder · Bescheinigung Ausgleichskasse → direkt ausbezahlte EO-/Mutterschaftsentschädigung
- **Rechnen:** Σ Taggelder/Entschädigungen 2025 je Person − bereits im Lohnausweis (Ziff. 1) enthaltene
- **Regel:** Nur soweit nicht bereits im Lohnausweis enthalten (sonst Doppelerfassung mit Ziff. 1). Taggelder ALV, SUVA, Kranken-/Unfall-/IV-Versicherung, Mutterschaftsentschädigung, EO-Entschädigungen direkt von der Ausgleichskasse. Steuerfrei und nicht anzugeben: Sold Militär/Zivilschutz/Feuerwehr, Taschengeld Zivildienst. Bescheinigung beilegen. Lohnausweis Ziff. 15 muss die Anzahl Tage nennen, wenn die Entschädigung nicht über den Arbeitgeber lief.
- **Beachten:** Über Arbeitgeber ausbezahlte Entschädigungen sind im Lohnausweis → nicht nochmals erfassen.
- **Beachten:** Steuerfrei: Sold Militär/Zivilschutz, Taschengeld Zivildienst; Feuerwehrsold steuerbar nur über Freibetrag (Ziff. 1.2).
- **Beachten:** Bescheinigung über die Bezüge beilegen.
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0007.md) `tg-form-01-2025__c0007` – «3.3 Erwerbsausfallentschädigungen»
  - [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0079.md) `tg-wl-2025__c0079` – «Diese Entschädigungen sind insoweit anzugeben, als sie im Lohnausweis von den Arbeitgebenden»
  - [WL Lohnausweis 2026 S. 19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0052.md) `bund-wl-lohnausweis-2026__c0052` – «Anzahl der Tage mit Erwerbsausfallentschädigungen: Diese sind stets anzugeben,»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0052.md) `tg-wl-2025__c0052` – «Kernaufgaben der Feuerwehr bei den Staats- und Gemeindesteuern ist bis zu einem festgelegten»

<a id="3-4-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.4 – Von Ausgleichskassen direkt ausbezahlte Familien-, Kinder- und Haushaltszulagen (Code 140)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Familienausgleichskasse (Kinder-, Haushalts-, Ausbildungs-, Geburts-, Adoptionszulagen)
- **Rein:** Bescheinigung Familienausgleichskasse → Σ direkt ausbezahlte Kinder-, Ausbildungs-, Haushalts-, Geburts-, Adoptionszulagen 2025
- **Rechnen:** Σ direkt von der Ausgleichskasse ausbezahlte Zulagen 2025 (Selbständige, Nichterwerbstätige, Landwirtschaft)
- **Regel:** Nur direkt von der Ausgleichskasse ausbezahlte Zulagen an Selbständigerwerbende, Nichterwerbstätige und Landwirtschaft; Zulagen im Lohnausweis stecken bereits im Nettolohn (Ziff. 1). Nicht unter Ziff. 2 deklarieren.
- **Beachten:** Zulagen über Arbeitgeber stecken im Nettolohn (Ziff. 1) → nicht hier.
- **Beachten:** Selbständige: nicht in Ziff. 2 (nicht AHV-pflichtig).
- **Beachten:** Vom anderen Elternteil weitergeleitete Kinderzulagen gehören zu den Alimenten Ziff. 5.2.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0007.md) `tg-form-01-2025__c0007` – «3.4 Von Ausgleichskassen direkt ausbezahlte Familien-, Kinder- und Haushaltszulagen   140»
  - [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0080.md) `tg-wl-2025__c0080` – «Deklarieren Sie hier von der Ausgleichskasse direkt ausbezahlte Familien- und Haushaltszulagen.»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0049.md) `tg-wl-2025__c0049` – «und Kinderzulagen, Dienstaltersgeschenke, Jubiläumszuwendungen usw.»
  - [WL TG 2025 S. 15](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0063.md) `tg-wl-2025__c0063` – «Direkt ausbezahlte Familienzulagen sind nicht AHV-pflichtig.»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0081.md) `tg-wl-2025__c0081` – «Periodische Unterhaltsbeiträge (inklusive Kinderzulagen), die Sie für die unter Ihrer elterlichen»

<a id="4-einkommen-wertschriften"></a>
### Ziff. 4 – Wertschriften- und Zinserträge sowie Gewinne aus Geldspielen (Formular 2, Code 150)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Formular 2 (Wertschriftenverzeichnis) Total steuerbarer Ertrag Ziff. 9 (Code 150)
- **Rein:** Steuerauszug/Depotauszug Bank → Steuerwert Sp. 7, Bruttoerträge Sp. 8 (mit VSt) / Sp. 9 (ohne VSt) · Zinsausweis Bank-/Postkonto → Bruttozins (bis Fr. 200, einmal jährlich: Spalte 9), Kontostand · Ausländische Dividenden-/Zinsabrechnung → Netto + anrechenbare Quellensteuer; Formular DA-1 · Auszahlungsbescheinigung Lotterie/Geldspiel (Original) → Gewinn Sp. 8 / Sp. 9
- **Rechnen:** Form. 2 Ziff. 9 = Ziff. 15 (Bruttoertrag A+B) − Ziff. 16 Geschäftserträge − Ziff. 17 Verwaltungskosten (2 Promille, max. 6'000) − Ziff. 18 Einsatzkosten
- **Regel:** Erst Formular 2 ausfüllen, dann Total steuerbarer Ertrag übertragen (Bruttoerträge Spalten 8+9 abzüglich Geschäftsanteil, Vermögensverwaltungskosten und pauschale Einsatzkosten Geldspiele). Steuerauszug der Bank einreichen, wenn Titel nur als Total deklariert werden. Lotterien/Geschicklichkeitsspiele: einzelne Gewinne bis Fr. 1'000 steuerfrei (Bund Fr. 1'100); übersteigt ein einzelner Gewinn die Grenze, ist dieser Einzelgewinn voll steuerbar (weitere Einzelgewinne unter der Grenze bleiben steuerfrei); ausländische Lotterien/Spiele immer voll steuerbar. Grossspiele/Online-Spielbank: einzelne Gewinne bis Fr. 1'000'000 (Bund Fr. 1'070'400) steuerfrei, steuerbar nur der übersteigende Anteil; Kleinspiele steuerfrei. Ausländische Erträge: Nettobetrag zuzüglich anrechenbarer Quellensteuer; Formular DA-1.
- **Beachten:** Lotterie/Verkaufsförderung: Einzelgewinn bis Kanton 1'000 / Bund 1'100 frei, darüber ganz steuerbar; Ausland immer.
- **Beachten:** Grossspiele: steuerbar nur über Kanton 1'000'000 / Bund 1'070'400; Einsatz fünf Prozent, max. Kanton 5'000 / Bund 5'400.
- **Beachten:** Qual. Beteiligung PV (≥ 10%): Ertrag voll in Sp. 8/9; Abzug Kanton 40% / Bund 30% via Hilfsblatt → Ziff. 15.6.
- **Limiten:**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'000 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'000 (Kanton; Bund CHF 1'100). Gewinne über der Grenze sind voll steuerbar.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'100)**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'000'000 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen nach BGS steuerfrei bis CHF 1'000'000 (Kanton); Bund CHF 1'070'400.)** · Bund **CHF 1'070'400 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'070'400)**
- **Bund:** Steuerfreigrenze Lotterien/Geschicklichkeitsspiele Bund Fr. 1'100 (Kanton Fr. 1'000); Grossspiele Bund Fr. 1'070'400 (Kanton Fr. 1'000'000); Bundeskorrektur von Amtes wegen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «4. Wertschriften- und Zinserträge sowie Gewinne aus Geldspielen   Formular 2 150»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0163.md) `tg-wl-2025__c0163` – «Das Total der steuerbaren Erträge in Ziffer 9 errechnen Sie, indem Sie vom Zwischentotal in Ziffer»
  - [WL TG 2025 S. 31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0146.md) `tg-wl-2025__c0146` – «Einzelne solche Gewinne bis zu einem Betrag von Fr. 1 000 sind hin»
  - [WL TG 2025 S. 33–34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0159.md) `tg-wl-2025__c0159` – «für sämtliche Kosten pauschal 2 Promille des Steuerwertes der»
  - [WL TG 2025 S. 33–34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0159.md) `tg-wl-2025__c0159` – «Der Pauschalabzug beträgt maximal Fr. 6'000.»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0161.md) `tg-wl-2025__c0161` – «ximalabzug pro Gewinn Fr. 5'000 und bei der direkten Bundessteuer Fr. 5'400.»
  - [WL TG 2025 S. 31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0148.md) `tg-wl-2025__c0148` – «Steuerbar ist nur der Anteil des Einzelgewinns, welcher den Steuerfreibetrag übersteigt.»
  - [WL TG 2025 S. 32](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0153.md) `tg-wl-2025__c0153` – «Bank- und Postkonti aller Art, deren Bruttozins im Kalenderjahr Fr. 200 nicht übersteigt und»
  - [WL TG 2025 S. 33](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0155.md) `tg-wl-2025__c0155` – «Als steuerbarer Ertrag ausländischer Wertpapiere gilt der Nettobetrag gemäss Auszahlungsbor-»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0164.md) `tg-wl-2025__c0164` – «mögen von mindestens 10% am Grund- oder Stammkapital einer Kapitalgesellschaft oder Genos-»
  - [WL TG 2025 S. 34–35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0166.md) `tg-wl-2025__c0166` – «3 einzusetzende Teilbesteuerungsabzug beträgt 40% bei den Staats- und Gemeindesteuern und»
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0006.md) `tg-form-02-2025__c0006` – «15. Zwischentotal II Steuerwerte und Bruttoertrag A und B»
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0006.md) `tg-form-02-2025__c0006` – «16. Abzüglich Geschäftswertschriften bzw. -erträge lt. Buchhaltung»
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0006.md) `tg-form-02-2025__c0006` – «17. Vermögensverwaltungskosten   Code 148»
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0006.md) `tg-form-02-2025__c0006` – «18. Einsatzkosten und Spieleinsätze für steuerbare Gewinne aus Geldspielen»
  - [WL TG 2025 S. 31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0147.md) `tg-wl-2025__c0147` – «Sobald ein einzelner Gewinn die Steuerfreigrenze übersteigt, ist der gesamte Gewinn steuerbar.»
  - [WL TG 2025 S. 31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0147.md) `tg-wl-2025__c0147` – «Solche Gewinne sind unabhängig des Betrags vollumfänglich steuerbar.»
  - [WL TG 2025 S. 32](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0152.md) `tg-wl-2025__c0152` – «Legen Sie bei den Lotterietreffern aller Art die Auszahlungsbescheinigung im Original bzw. den»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0165.md) `tg-wl-2025__c0165` – «Die Erträge aus qualifizierten Beteiligungen im Privatvermögen sind grundsätzlich in Spalte 8»

<a id="5-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.1 – Unterhaltsbeiträge von Ehegatte/Partner bei Trennung/Scheidung (Name und Adresse Zahler/in) (Code 160)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil bzw. Vereinbarung; Zahlungsnachweise
- **Rein:** Scheidungs-/Trennungsurteil bzw. Vereinbarung → periodischer Unterhaltsbeitrag für sich selbst · Zahlungsnachweise → erhaltene Beträge 2025 · Überlassung Liegenschaftsanteil → Mietwertanteil als Unterhaltsbeitrag · Personalien Zahler/in → Name, Adresse (Zeile unter Ziff. 5.1)
- **Rechnen:** Σ periodische Unterhaltsbeiträge 2025 für sich selbst + Mietwertanteil eines überlassenen Liegenschaftsanteils
- **Regel:** Periodische Unterhaltsbeiträge für sich selbst steuerbar; ebenso Mietwertanteil aus Überlassung eines Liegenschaftsanteils. Name/Adresse der zahlenden Person in der Zeile unter 5.1 angeben. Gegenstück: Abzug beim Zahler Ziff. 12.1.
- **Beachten:** Gilt bei Scheidung, Auflösung Partnerschaft sowie gerichtlicher oder tatsächlicher Trennung.
- **Beachten:** Gegenstück beim Zahler: Abzug Ziff. 12.1.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «5.1 Unterhaltsbeiträge von Ehefrau/-mann bzw. Partnerin/Partner bei Trennung/Scheidung»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0081.md) `tg-wl-2025__c0081` – «Steuerbar sind periodische Unterhaltsbeiträge der Ehefrau oder des Ehemanns bzw. der»
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «12.1 Unterhaltsbeiträge an Ehefrau/-mann bzw. Partnerin/Partner»

<a id="5-2-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.2 – Unterhaltsbeiträge für minderjährige Kinder (inkl. Kinderzulagen) (Name und Adresse Zahler/in) (Code 162)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Urteil/Vereinbarung; Zahlungsnachweise; ggf. Alimentenbevorschussung
- **Rein:** Urteil/Unterhaltsvertrag → periodische Kinderalimente inkl. Kinderzulagen · Kontoauszüge → tatsächlich 2025 eingegangene Beträge · Bestätigung Gemeinde Alimentenbevorschussung → bevorschusste Beträge (vermerken)
- **Rechnen:** Σ tatsächlich 2025 erhaltene Alimente inkl. Kinderzulagen je minderjähriges Kind (bis Monat der Volljährigkeit)
- **Regel:** Für Kinder unter eigener elterlicher Sorge steuerbar; bei unregelmässigen Zahlungen die tatsächlich im Jahr 2025 überwiesenen Beträge. Alimentenbevorschussung durch die Gemeinde vermerken. Ab Folgemonat der Volljährigkeit nicht mehr steuerbar. Wer die Alimente versteuert, erhält den Kinderabzug (Ziff. 25.1).
- **Beachten:** Ab Folgemonat der Volljährigkeit nicht mehr steuerbar.
- **Beachten:** Name/Adresse zahlende Person angeben; Bevorschussung durch Gemeinde vermerken.
- **Beachten:** Kinderabzug erhält der Alimente empfangende Elternteil (Bund grundsätzlich gleich).
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «5.2 Unterhaltsbeiträge für minderjährige Kinder (Name, Adresse Zahler/in)   162»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0081.md) `tg-wl-2025__c0081` – «Periodische Unterhaltsbeiträge (inklusive Kinderzulagen), die Sie für die unter Ihrer elterlichen»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0081.md) `tg-wl-2025__c0081` – «Ab dem Folgemonat der Volljährigkeit des Kindes sind die»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0109.md) `tg-wl-2025__c0109` – «Der Kinderabzug steht nur dem die zu versteuernden Unterhaltsbeiträge (Alimente) für minderjäh-»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0112.md) `tg-wl-2025__c0112` – «Fliessen Unterhaltsbeiträge, gelten bei minderjährigen Kindern grundsätzlich die gleichen Zutei-»

<a id="5-3-einkommen-erbschaften-unverteilt"></a>
### Ziff. 5.3 – Ertrag aus unverteilten Erbschaften (Formular 3) (Code 164)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung der Erbengemeinschaft/Nachlassverwalter (Ertrag, Erbquote); Vermögensanteil Ziff. 30.5
- **Rein:** Aufstellung Erbengemeinschaft/Willensvollstrecker (Formular 3) → Nachlassertrag × Erbquote · Steuerauszug Nachlasskonten → VSt-belastete Erträge anteilig in Form. 2 Spalte A, übrige in Spalte B
- **Rechnen:** Σ Nachlasserträge ab Folgetag des Todestags × eigene Erbquote; Vermögensanteil analog Ziff. 30.5
- **Regel:** Erträge nach Erbquote zurechnen; Steuerpflicht beginnt am Tag nach dem Todestag. VSt-belastete Erträge im Umfang der Erbquote in Spalte A von Formular 2, nicht belastete in Spalte B. Rückerstattung im Wohnsitzkanton.
- **Beachten:** Steuerpflicht für Ertrag und Vermögen beginnt am Folgetag des Todestags.
- **Beachten:** VSt auf Erbschaftserträgen im eigenen Wohnsitzkanton zurückfordern.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «5.3 Ertrag aus unverteilten Erbschaften   Formular 3 164»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0082.md) `tg-wl-2025__c0082` – «Einkünfte aus unverteilten Erbschaften werden den erbenden Personen entsprechend ihrer»
  - [WL TG 2025 S. 35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0169.md) `tg-wl-2025__c0169` – «unverteilten Erbschaft sind im Umfang der Erbquote in der Spalte A»
  - [WL TG 2025 S. 35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0168.md) `tg-wl-2025__c0168` – «Erbinnen und Erben haben die Verrechnungssteuer auf ihren Erbschaftserträgen in ihrem Wohn-»

<a id="5-4-einkommen-uebrige"></a>
### Ziff. 5.4 – Weitere Einkünfte (Urheberrechte, Lizenzen, Patente, Wohnrecht, Nutzniessung, Lidlohn, Entschädigungen) (Code 168)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Verträge/Aufstellung; nähere Bezeichnung auf dem Formular
- **Rein:** Lizenz-/Urheberrechts-/Patentabrechnungen → Einnahmen · Wohnrechts-/Nutzniessungsvertrag → Miete einer entsprechenden Wohnung (Wohnrecht) bzw. Nutzniessungsertrag · Untermietvertrag + eigener Mietvertrag/Nebenkostenabrechnung → Untermietertrag netto · Vereinbarung Konkurrenzverbot/Rechtsverzicht, Lidlohn → Entschädigung
- **Rechnen:** Σ Einkünfte; Wohnrecht = Marktmiete entsprechender Wohnung; Untermiete = Einnahmen − anteiliger Mietzins − anteilige Nebenkosten
- **Regel:** Hier: Urheber-/Autorenrechte, Lizenzen, Patente, Nutzniessung, unentgeltliches Wohnrecht (bewertet mit der Miete einer entsprechenden Wohnung), Lidlöhne, Entschädigungen für Konkurrenzverbot/Verzicht auf Rechte, Untervermietung netto. Gewinne aus Geldspielen gehören in Ziff. 4, nicht hierher.
- **Beachten:** Geldspielgewinne → Ziff. 4 (Formular 2), nicht hier.
- **Beachten:** Nähere Bezeichnung der Einkunft im Formular angeben.
- **Beachten:** Abgrenzung zu Formular 7 prüfen: Mietwert aus Nutzniessung/Wohnrecht an Liegenschaften auch dort genannt.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «5.4 Weitere Einkünfte (z.B. Urheberrechte, Lizenzen, Patente, Wohnrecht usw.)»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0083.md) `tg-wl-2025__c0083` – «In Ziffer 5.4 deklarieren Sie Einkünfte aus Urheber- und Autorenrechten, Lizenzen, Patenten»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0222.md) `tg-wl-2025__c0222` – «Nutzniessung oder Wohnrecht) für den Eigengebrauch zur Verfügung stehen.»

<a id="5-5-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 5.5 – Kapitalabfindung für wiederkehrende Leistungen für … Jahre (Code 170)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung über die Kapitalabfindung (Rentenrückkauf, Lidlohn u.ä.)
- **Rein:** Auszahlungsbestätigung (Rentenrückkauf, Lidlohnanspruch) → Betrag + Anzahl Jahre der abgegoltenen Leistung
- **Rechnen:** Betrag in Ziff. 5.5 + Anzahl Jahre angeben; Steuersatz wie für entsprechende jährliche Leistung; Lebenszeit-Leistung: Umrechnung nach Rentenwerttabelle
- **Regel:** Zeitraum (Jahre) angeben, für den die Abfindung ausgerichtet wird; Besteuerung zum Satz, der sich bei entsprechender jährlicher Leistung ergäbe (bei Lebenszeit-Renten Umrechnung nach Rentenwerttabelle). Nicht hier, sondern Seite 4 unten: Kapitalleistungen aus Vorsorge.
- **Beachten:** Kapitalleistungen aus Vorsorge nicht hier, sondern Seite 4 unten.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «5.5 Kapitalabfindung für wiederkehrende Leistungen für»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0084.md) `tg-wl-2025__c0084` – «Anstelle von wiederkehrenden Leistungen ausbezahlte Kapitalabfindungen (z.B. Rentenrückkauf,»
  - [StG TG § 38](../../chunks/tg/2025/tg-stg/tg-stg__par-38.md) `tg-stg__par-38` – «zu dem Steuersatz berechnet, der sich ergäbe, wenn anstelle der einmaligen Leistung eine entsprechende jährliche Leistung»

<a id="6-berechnung-total"></a>
### Ziff. 6 – Zwischentotal der Einkünfte (Code 175)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 1.1–5.5 ohne 1.3)
- **Rein:** Übertrag aus Ziff. 1.1, 1.2, 2.1–5.5 (ohne Vorkolonne 1.3)
- **Rechnen:** Ziff. 6 = Σ Ziff. 1.1 + 1.2 + 2.1 + 2.2 + 3.1–3.4 + 4 + 5.1–5.5 (beide Personen); Ziff. 1.3 nicht einrechnen
- **Regel:** Summe der Einkünfte Ziff. 1 bis 5.5; vereinfacht abgerechnete Löhne (Ziff. 1.3) nicht einbeziehen (WL c0053). Formular 2025: Ziff. 6 wird in Ziff. 7 übertragen, dazu Ziff. 8.1 Einkünfte aus Liegenschaften (Formular 7); das Total der Einkünfte Ziff. 9 (Code 198) ist auf Seite 3, Ziffer 20 zu übertragen. Die WL 2025 (c0085) beschreibt noch die ältere Struktur mit Ziff. 6.1/6.2.
- **Beachten:** Negative Beträge (z.B. Verlust Ziff. 2) mit Minuszeichen einrechnen.
- **Beachten:** WL 2025 beschreibt noch Ziff. 6.1/6.2; im Formular 2025 Ziff. 6 → Ziff. 7 übertragen.
- **Bemerkung:** Die Wegleitung 2025 beschreibt Ziff. 6.1/6.2 (ältere Formularstruktur mit Geschäftsfahrzeug-Einkommen); das Formular 2025 hat nur Ziff. 6 (Code 175) und Ziff. 7 (Übertrag von Ziff. 6).
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «6. Zwischentotal der Einkünfte   175»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0085.md) `tg-wl-2025__c0085` – «Andernfalls übertragen Sie zuerst den Betrag von Ziffer 6.1 in Ziffer 6.2 der Steuererklärung.»
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0009.md) `tg-form-01-2025__c0009` – «9. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 20 198»
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0009.md) `tg-form-01-2025__c0009` – «7. Übertrag von Ziffer 6»
  - [WL TG 2025 S. 14](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0053.md) `tg-wl-2025__c0053` – «Löhne werden nicht in die Berechnung des Zwischentotals unter Ziffer 6 miteinbezogen.»
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0006.md) `tg-form-01-2025__c0006` – «– wenn negativ»
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0007.md) `tg-form-01-2025__c0007` – «3.4 Von Ausgleichskassen direkt ausbezahlte Familien-, Kinder- und Haushaltszulagen»

<a id="7-berechnung-total"></a>
### Ziff. 7 – Übertrag von Ziffer 6 (Staatssteuer / Bundessteuer)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Übertrag Ziff. 6)
- **Rein:** Übertrag aus Ziff. 6 (Code 175)
- **Rechnen:** Ziff. 7 Staatssteuer = Ziff. 7 Bundessteuer = Ziff. 6
- **Regel:** Übertrag des Zwischentotals Ziff. 6 in die beiden Spalten Staatssteuer und Bundessteuer, falls Liegenschaftseinkünfte (Ziff. 8) anfallen.
- **Beachten:** Bundesabweichungen (Feuerwehrsold, Geldspiele, Teilbesteuerung GV) korrigiert die StV von Amtes wegen.
- **Beachten:** Ab hier zwei Spalten: Liegenschaftserfolg je Spalte verschieden (Selbstnutzungsabzug).
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0009.md) `tg-form-01-2025__c0009` – «7. Übertrag von Ziffer 6»
  - [WL TG 2025 S. 31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0148.md) `tg-wl-2025__c0148` – «Die Steuerverwaltung nimmt bei der direkten Bundessteuer von Amtes wegen eine Korrektur vor.»
  - [WL TG 2025 S. 17](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0074.md) `tg-wl-2025__c0074` – «vom kantonalen Einkommen abweichen und wird von Amtes wegen in die Veranlagung aufgenommen.»
  - [WL TG 2025 S. 51](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0244.md) `tg-wl-2025__c0244` – «Selbstnutzungsabzugs der Nettoerfolg jeweils einzeln für die Staats- und Gemeindesteuern und die»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0052.md) `tg-wl-2025__c0052` – «Deklarieren Sie in der Steuererklärung die bei den Staats- und Gemeindesteuern steuerbaren Ein-»
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «6. Zwischentotal der Einkünfte   175»

<a id="8-1-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. 8.1 – Einkünfte aus Liegenschaften (Formular 7, Code 180; Staat und Bund getrennt)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Formular 7 Total Nettoerfolge (Code 180), je Spalte Staatssteuer/Bundessteuer
- **Rein:** Liegenschaftensteuerrechnung 2026 / Schätzung → indexierter Mietwert selbstgenutzt (Form. 7) · Mietverträge, Einspeisevergütung PV → Miet- und Pachtzinsen sowie weitere Erträge · Unterhaltsrechnungen, STWEG-Abrechnung → effektive Kosten in Formular 8 (je Liegenschaft) · Formular 7 Total Nettoerfolge → Ziff. 8.1 je Spalte
- **Rechnen:** je Liegenschaft/Spalte: Bruttoertrag = Mietwert selbstgenutzt × (1 − Kanton 40% / Bund 20%) + Mieten; Nettoerfolg = Bruttoertrag − Unterhalt (effektiv oder 10%/20%)
- **Regel:** Zuerst Formular 7 (und bei effektivem Unterhalt Formular 8) ausfüllen. Netto = Eigenmietwert (indexiert, nach Selbstnutzungsabzug) bzw. Mietzinsen abzüglich Unterhalts-/Betriebskosten (Pauschale oder effektiv); negativer Nettoerfolg mit Vorzeichen. Selbstnutzungsabzug nur für am Wohnsitz dauernd selbstbewohntes Eigentum: Kanton 40%, Bund 20%.
- **Beachten:** Selbstnutzungsabzug nur am Wohnsitz; Zweit-/Ferienwohnung, landw. Schätzung, Nahestehende: Mietwert 100% steuerbar.
- **Beachten:** Pauschale 10% (Gebäude ≤ 10 Jahre am Periodenende) / 20%, vom steuerbaren EMW bzw. Mietertrag; Wahl je Objekt/Jahr.
- **Beachten:** Keine Pauschale bei Geschäftsvermögen, unüberbaut/Baurecht; Rechnungen ab Fr. 1'000 beilegen.
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **40 % (Selbstnutzungsabzug 40% vom Eigenmietwert für am Wohnsitz dauernd selbstbewohntes Wohneigentum (Bund 20%); nicht für Zweit-/Ferienwohnungen, landwirtschaftlich geschätzte Liegenschaften oder an Nahestehende überlassene Objekte.)** · Bund **n/a – Eigenmietwert wird nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt (Art. 21 Abs. 2 DBG); Abschaffung per 01.01.2029 beschlossen, 2025–2028 gilt bisheriges Recht. Der Eigenmietwert für die direkte Bundessteuer wird im kantonalen Veranlagungsverfahren festgesetzt; ein dort vorgesehener Abzug für die DBSt (z.B. TG 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Unterhaltspauschale 10% des Bruttomietertrags/Mietwerts/Eigenmietwerts für Gebäude bis zehn Jahre alt (am Ende der Steuerperiode); Wahl pro Liegenschaft und Periode; nicht bei Geschäftsvermögen, unüberbauten Grundstücken, Baurecht.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Unterhaltspauschale 20% für Gebäude, die älter als zehn Jahre sind.)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Bund:** Selbstnutzungsabzug Bund 20% (Kanton 40%) – deshalb unterschiedliche Nettoerfolge je Spalte.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0009.md) `tg-form-01-2025__c0009` – «8.1 Einkünfte aus Liegenschaften   Formular 7 180»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0225.md) `tg-wl-2025__c0225` – «nutzung kantonal einen Abzug von 40% und beim Bund von 20% vornehmen»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0238.md) `tg-wl-2025__c0238` – «10% für Gebäude, die am Ende der Steuerperiode bis zu zehn Jahre alt sind;»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0224.md) `tg-wl-2025__c0224` – «Der indexierte Mietwert für die Steuerperiode 2025 ist in der Regel aus Ihrer»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0224.md) `tg-wl-2025__c0224` – «Einspeisevergütungen für Photovoltaikanlagen sind steuerbar.»
  - [WL TG 2025 S. 49](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0233.md) `tg-wl-2025__c0233` – «Pro Liegenschaft, für welche Sie effektive Unterhaltskosten geltend machen, füllen Sie bitte je ein»
  - [WL TG 2025 S. 49](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0234.md) `tg-wl-2025__c0234` – «Für Einzelbeträge ab Fr. 1'000 legen Sie der Steuererklärung bitte die Rechnungskopien (inkl. der»
  - [WL TG 2025 S. 51](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0244.md) `tg-wl-2025__c0244` – «Kreuzen Sie in der Checkbox an, ob Sie pauschale oder effektive Unterhalts- und Betriebskosten»
  - [WL TG 2025 S. 49](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0234.md) `tg-wl-2025__c0234` – «Bei Stockwerkeigentum legen Sie bitte eine Kopie der»

<a id="9-berechnung-total"></a>
### Ziff. 9 – Total der Einkünfte, zu übertragen auf Seite 3 Ziffer 20 (Code 198; Staat/Bund)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 7 + Ziff. 8)
- **Rein:** Übertrag aus Ziff. 7 und Ziff. 8.1 (je Spalte)
- **Rechnen:** Ziff. 9 = Ziff. 7 + Ziff. 8.1, getrennt Staatssteuer / Bundessteuer → Übertrag Ziff. 20
- **Regel:** Ziff. 7 plus Ziff. 8.1, je Spalte Staatssteuer/Bundessteuer; Übertrag in Ziff. 20.
- **Beachten:** Spalten weichen bei selbstgenutztem Wohneigentum ab (Selbstnutzungsabzug Kanton 40% / Bund 20%).
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0009.md) `tg-form-01-2025__c0009` – «9. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 20   198»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0225.md) `tg-wl-2025__c0225` – «nutzung kantonal einen Abzug von 40% und beim Bund von 20% vornehmen»

## Abzüge

<a id="10-1-berechnung-total"></a>
### Ziff. 10.1 – Berufsauslagen bei unselbständiger Erwerbstätigkeit Person 1 (Formular 4.2 Ziff. 7, Code 240; Staat/Bund)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg, Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Formular 4.2 Ziff. 7 Total der abzugsfähigen Berufsauslagen (Code 240)
- **Rein:** Lohnausweis → Nettolohn Ziff. 11 (Basis 3%-Pauschale), Geschäftsfahrzeug · ÖV-Abonnement → Form. 4.2 Ziff. 2.1 · Arbeitsweg km × Arbeitstage (Privatauto, nur wenn ÖV unzumutbar) → Ziff. 2.3 · Mietvertrag Zimmer Wochenaufenthalt → Ziff. 5.1; Aufstellung Nebenerwerbskosten → Ziff. 6
- **Rechnen:** Form. 4.2 Ziff. 7 = min(Ziff. 2.4; Kanton 6'000 / Bund 3'300) + Ziff. 3 (15/Tag, max. 3'200) + Ziff. 4 (3% Nettolohn, min. 2'000, max. 4'000) + Ziff. 5 + 6
- **Regel:** Total aus Formular 4.2 (Fahrkosten, Verpflegung, übrige Berufskosten, Wochenaufenthalt, Nebenerwerb) übertragen, je Spalte Staat/Bund (Fahrkostenmaximum und Km-Ansätze unterscheiden sich). Nicht vom Arbeitgeber übernommene Kosten abziehen. Lohnausweis prüfen: Feld F angekreuzt = keine Fahrkosten; Feld G = nur halbe Verpflegung.
- **Beachten:** Auto nur bei ÖV unzumutbar: Kanton -.60 bis 3'000 km, -.50 bis 5'000, -.40 darüber / Bund -.70 je km; i.d.R. 225 Tage.
- **Beachten:** Verbilligung/Kantine 7.50/Tag, max. 1'600; Geschäftsfahrzeug: keine Fahrkosten; AG-getragene Kosten nicht abziehbar.
- **Beachten:** Unterjährige Tätigkeit: Pauschalen pro rata (z.B. 3'200 × 270/360); Teilzeit: Verpflegungspauschale angemessen gekürzt.
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 pro Jahr (alle Fahrkosten inkl. Wochenaufenthalt und Nebenerwerb zusammen; keine Kürzung bei unterjähriger Steuerpflicht/Teilzeit).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Pauschale CHF 15 pro auswärtige Hauptmahlzeit (in der Regel nur Mittagessen), wenn Heimkehr am Mittag wegen grosser Entfernung oder sehr kurzer Essenspause unzumutbar.)** · Bund **CHF 15 (Mehrkosten auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (i.d.R. Mittagessen); ausschliesslich Pauschale, wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei ständiger auswärtiger Verpflegung maximal CHF 3'200 pro Jahr; bei Teilzeitpensum Kürzung nach Beschäftigungsgrad (z.B. 80% = Fr. 2'560).)** · Bund **CHF 3'200 (Bei ständiger auswärtiger Verpflegung CHF 3'200 pro Jahr (voller Abzug))**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **3 % (Pauschale übrige Berufskosten: 3% des Nettolohnes (Alternative: Nachweis höherer tatsächlicher Kosten, keine Kumulation).)** · Bund **3 % (Übrige Berufskosten: 3 % des Nettolohns (Pauschale; Nachweis höherer Kosten möglich); bei Teilzeit/unterjährig angemessen kürzen)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **CHF 2'000 (Pauschale übrige Berufskosten: Minimum CHF 2'000.)** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 4'000 (Pauschale übrige Berufskosten: Maximum CHF 4'000.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «10.1 Person 1   Formular 4.2 240»
  - [WL TG 2025 S. 41](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0196.md) `tg-wl-2025__c0196` – «Tragen Sie in diese Ziffer die Summe der Berufsauslagen gemäss den Ziffern 2 bis 7 ein.»
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0002.md) `tg-form-04-2-2025__c0002` – «Staat max. Fr. 6000.– / Bund max. Fr. 3300.–»
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0003.md) `tg-form-04-2-2025__c0003` – «pro Arbeitstag Fr. 15.– / max. Fr. 3200.– pro Jahr»
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0003.md) `tg-form-04-2-2025__c0003` – «pro Arbeitstag Fr. 7.50 / max. Fr. 1600.– pro Jahr»
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0004.md) `tg-form-04-2-2025__c0004` – «3% vom Nettolohn, mindestens jedoch Fr. 2000.– und höchstens Fr. 4000.–»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0180.md) `tg-wl-2025__c0180` – «Bei der direkten Bundessteuer beträgt der Ansatz einheitlich Fr. -.70 pro gefahrenen Kilometer.»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0180.md) `tg-wl-2025__c0180` – «3'001 bis 5'000 km Fr. -.50»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0175.md) `tg-wl-2025__c0175` – «Kein Abzug ist zulässig für Kosten, die Arbeitgebende»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0175.md) `tg-wl-2025__c0175` – «Bei der Berechnung der notwendigen Auslagen ist in der Regel von 225»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0176.md) `tg-wl-2025__c0176` – «Der im Lohnausweis berücksichtigte Privatanteil Fahrzeug von 0.9 % pro Monat»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0176.md) `tg-wl-2025__c0176` – «Umrechnung Fr. 3'200 x 270 = Fr. 2'400»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0178.md) `tg-wl-2025__c0178` – «Die Kosten der Benützung von privaten Motorfahrzeugen können Sie nur in Ausnahmefällen»
  - [WL TG 2025 S. 39](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0183.md) `tg-wl-2025__c0183` – «erfolgt eine angemessene Kürzung des Pauschalbetrags.»
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0002.md) `tg-form-04-2-2025__c0002` – «2.4 Total effektive Fahrkosten (Ziffern 2.1 – 2.3)»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0180.md) `tg-wl-2025__c0180` – «bis   3'000 km   Fr. -.60»
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0005.md) `tg-form-04-2-2025__c0005` – «6.   Auslagen bei Nebenbeschäftigung»

<a id="10-2-berechnung-total"></a>
### Ziff. 10.2 – Berufsauslagen bei unselbständiger Erwerbstätigkeit Person 2 (Formular 4.3 Ziff. 7, Code 280; Staat/Bund)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg, Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Formular 4.2 Rückseite (Person 2, im Formular als «4.3» bezeichnet) Ziff. 7 (Code 280)
- **Rein:** Lohnausweis Person 2 → Ziff. 11 Nettolohn (Basis 3%-Pauschale); Dauer, Pensum, Geschäftsfahrzeug → Formular 4.3 Ziff. 1 · ÖV-Abo-Belege → Formular 4.3 Ziff. 2.1 (Code 246) · Fahrzeugausweis + km Arbeitsweg × Arbeitstage → Ziff. 2.3 (Code 251), nur wenn ÖV unzumutbar · Spesenreglement/Spesen im Lohnausweis → vom Arbeitgeber übernommene Kosten (nicht abziehbar)
- **Rechnen:** Formular 4.3: min(Ziff. 2.4; Staat 6'000 / Bund 3'300) + Ziff. 3 Verpflegung + Ziff. 4 (3% × Nettolohn, min. 2'000, max. 4'000) + Ziff. 5 + 6 = Code 280
- **Regel:** Wie Ziff. 10.1 für Person 2 (Rückseite des Formulars 4.2, Codes 246–280).
- **Beachten:** Geschäftsfahrzeug (Privatanteil 0.9 % pro Monat im Lohn) → kein Fahrkostenabzug
- **Beachten:** Auto nur ausnahmsweise: Kanton gestaffelt Fr. -.60/-.50/-.40 je km, Bund Fr. -.70 – Spalten getrennt rechnen
- **Beachten:** Unterjährige Tätigkeit: Pauschalen pro rata (Tage/360); vom Arbeitgeber übernommene Kosten nicht abziehbar
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 pro Jahr (alle Fahrkosten inkl. Wochenaufenthalt und Nebenerwerb zusammen; keine Kürzung bei unterjähriger Steuerpflicht/Teilzeit).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **3 % (Pauschale übrige Berufskosten: 3% des Nettolohnes (Alternative: Nachweis höherer tatsächlicher Kosten, keine Kumulation).)** · Bund **3 % (Übrige Berufskosten: 3 % des Nettolohns (Pauschale; Nachweis höherer Kosten möglich); bei Teilzeit/unterjährig angemessen kürzen)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **CHF 2'000 (Pauschale übrige Berufskosten: Minimum CHF 2'000.)** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 4'000 (Pauschale übrige Berufskosten: Maximum CHF 4'000.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **Privatauto, nur in Ausnahmefällen (wenn ÖV nicht zumutbar): gestaffelt nach jährlicher Fahrleistung bis 3'000 km CHF 0.60/km, 3'001-5'000 km CHF 0.50/km, über 5'000 km CHF 0.40/km (stufenweise Berechnung; inkl. Parkgebühren). Normalfall: Kosten des ÖV-Abonnements.** · Bund **CHF 0.70 (Privatauto: Abzug pro Fahrkilometer CHF 0.70, nur wenn kein öffentliches Verkehrsmittel verfügbar/zumutbar (Steuerjahr 2025))**
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «10.2 Person 2   Formular 4.3 280»
  - [Formular 4.2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0010.md) `tg-form-04-2-2025__c0010` – «7.   Total der abzugsfähigen Berufsauslagen   280»
  - [Formular 4.2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0007.md) `tg-form-04-2-2025__c0007` – «2.5 Total abzugsfähige Fahrkosten (Übertrag von Ziffer 2.4, aber Staat max. Fr. 6000.– / Bund max. Fr. 3300.–)   253»
  - [Formular 4.2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0007.md) `tg-form-04-2-2025__c0007` – «2.1 Abonnementskosten für öffentliche Verkehrsmittel   246»
  - [Formular 4.2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0009.md) `tg-form-04-2-2025__c0009` – «3% vom Nettolohn, mindestens jedoch Fr. 2000.– und höchstens Fr. 4000.–»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0187.md) `tg-wl-2025__c0187` – «3% vom Nettolohn gemäss Ziffer 11 des Lohnausweises»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0176.md) `tg-wl-2025__c0176` – «Der im Lohnausweis berücksichtigte Privatanteil Fahrzeug von 0.9 % pro Monat für die private Nut-»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0176.md) `tg-wl-2025__c0176` – «Im Gegenzug kann dafür kein Fahrkos-»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0180.md) `tg-wl-2025__c0180` – «Bei der direkten Bundessteuer beträgt der Ansatz einheitlich Fr. -.70 pro gefahrenen Kilometer.»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0175.md) `tg-wl-2025__c0175` – «Kein Abzug ist zulässig für Kosten, die Arbeitgebende»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0176.md) `tg-wl-2025__c0176` – «Umrechnung   Fr. 3'200 x 270   = Fr. 2'400»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0178.md) `tg-wl-2025__c0178` – «Die Kosten der Benützung von privaten Motorfahrzeugen können Sie nur in Ausnahmefällen»
  - [Formular 4.2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0008.md) `tg-form-04-2-2025__c0008` – «3. Mehrkosten der auswärtigen Verpflegung»

<a id="11-abzug-schuldzinsen"></a>
### Ziff. 11 – Schuldzinsen (Formular 4.1, Code 290)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen) → Formular 4.1 Ziff. C Total Schuldzinsen (Code 290)
- **Rein:** Hypothekar-/Zinsbestätigung Bank → im 2025 fällige Zinsen, Schuld per 31.12. (Formular 4.1 A) · Kredit-/Darlehensvertrag → Gläubiger mit Adresse, Zinssatz, Zins (A privat / B geschäftlich) · Steuerschlussrechnung → im 2025 belastete Ausgleichszinsen · WEF-Bestätigung → Zusatzverbilligung (mindert Schuldzinsen)
- **Rechnen:** Σ 2025 fällige Zinsen A privat (Code 286) + B Geschäft (Code 288) = C Code 290; privat max. Vermögenserträge + 50'000 (Kanton = Bund)
- **Regel:** Nur im Jahr 2025 fällig gewordene Schuldzinsen (keine Ratazinsen); mit der Schlussrechnung belastete Ausgleichszinsen ebenfalls abziehbar. Private Schuldzinsen höchstens im Umfang der deklarierten Erträge aus beweglichem und unbeweglichem Vermögen plus Fr. 50'000. Keine Amortisationen, Bau-/Landkreditzinsen (Anlagekosten), Leasingzinsen; Baurechtszinsen nur bei Fremdvermietung. WEF-Zusatzverbilligungen mindern die Schuldzinsen. Geschäftsschuldzinsen nur, wenn nicht schon in Ziff. 2 abgezogen.
- **Beachten:** Keine Ratazinsen, Amortisationen, Bau-/Landkreditzinsen (Anlagekosten), Leasingzinsen
- **Beachten:** Baurechtszinsen nur bei Fremdvermietung abziehbar, nicht bei Eigengebrauch
- **Beachten:** Geschäftsschuldzinsen nur, wenn nicht schon in Ziff. 2 (Reingewinn) abgezogen
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «11.   Schuldzinsen   Formular 4.1 290»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «Sie können private Schuldzinsen höchstens im Umfang der deklarierten Erträge aus beweglichem»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «und unbeweglichem Vermögen und weiterer Fr. 50 000 in Abzug bringen.»
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0002.md) `tg-form-04-1-2025__c0002` – «Total Privat- und Geschäftsschulden   466   290»
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0001.md) `tg-form-04-1-2025__c0001` – «Total Privatschulden   455   286»
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0001.md) `tg-form-04-1-2025__c0001` – «Total Geschäftsschulden   460   288»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0172.md) `tg-wl-2025__c0172` – «Tragen Sie nur die im Jahre 2025 fällig gewordenen Schuldzinsen ein (keine Ratazinsen).»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0172.md) `tg-wl-2025__c0172` – «Die im 2025 mit der Steuerschlussrechnung belasteten Ausgleichszinsen können Sie ebenfalls als»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0171.md) `tg-wl-2025__c0171` – «Unerlässlich ist insbesondere die Angabe der Gläubigerin bzw. des Gläubigers»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken»

<a id="12-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.1 – Unterhaltsbeiträge an Ehegatte/Partner bei Trennung/Scheidung (Empfänger/in, Adresse) (Code 300)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise; Kopie Scheidungs-/Trennungsurteil bei erstmaliger Deklaration
- **Rein:** Bank-/Postbelege → Σ 2025 bezahlte periodische Unterhaltsbeiträge · Scheidungs-/Trennungsurteil bzw. -vereinbarung → Kopie bei erstmaliger Deklaration · Angaben Empfänger/in → Name, Adresse (Zeile unter Ziff. 12)
- **Rechnen:** Σ 2025 tatsächlich bezahlte periodische Beiträge an (Ex-)Ehegatten/Partner(in) + Mietwertanteil überlassener Liegenschaftsanteil → Code 300
- **Regel:** Tatsächlich bezahlte periodische Beiträge; Name/Adresse der empfangenden Person angeben, sonst kein Abzug. Mietwertanteil aus Überlassung eines Liegenschaftsanteils zählt ebenfalls. Gegenstück bei der empfangenden Person: Ziff. 5.1.
- **Beachten:** Ohne Zahlungsnachweis und Name/Adresse der empfangenden Person kein Abzug
- **Beachten:** Nur periodische Beiträge; andere familienrechtliche Unterhalts-/Unterstützungsleistungen nicht abziehbar
- **Beachten:** Gegenstück: empfangende Person versteuert in Ziff. 5.1
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «12.1 Unterhaltsbeiträge an Ehefrau/-mann bzw. Partnerin/Partner»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0087.md) `tg-wl-2025__c0087` – «Die Abzüge für Unterhaltsbeiträge und Rentenleistungen werden nur gewährt, wenn Zahlungs»
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t2.md) `tg-stg__par-34-t2` – «nicht jedoch Leistungen in Erfüllung anderer familienrechtlicher Unterhalts- oder Unterstützungspflichten»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0081.md) `tg-wl-2025__c0081` – «Steuerbar sind periodische Unterhaltsbeiträge der Ehefrau oder des Ehemanns bzw. der Partne-»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0081.md) `tg-wl-2025__c0081` – «kann die Zeile direkt unterhalb der Ziffer 5.1 verwendet werden.»

<a id="12-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.2 – Unterhaltsbeiträge für minderjährige Kinder (Code 302)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise an den anderen Elternteil; Urteil/Vereinbarung
- **Rein:** Bank-/Postbelege an anderen Elternteil → Σ 2025 überwiesene Kinderalimente inkl. Kinderzulagen · Scheidungs-/Trennungsurteil bzw. -vereinbarung → Kopie bei erstmaliger Deklaration · Angaben Empfänger/in → Name, Adresse (Zeile unter Ziff. 12)
- **Rechnen:** Σ 2025 bezahlte Kinderunterhaltsbeiträge (inkl. Kinderzulagen) je Kind, längstens bis und mit Monat der Mündigkeit → Code 302
- **Regel:** Dem anderen Elternteil für die unter dessen Sorge stehenden Kinder überwiesene Beiträge (inkl. Kinderzulagen), längstens bis und mit dem Monat der Mündigkeit. Wer abzieht, hat keinen Anspruch auf den Kinderabzug (Ziff. 25.1).
- **Beachten:** Wer Kinderalimente abzieht, hat keinen Kinderabzug (Ziff. 25.1); Bund grundsätzlich gleich
- **Beachten:** Ab Folgemonat der Volljährigkeit: kein Abzug (beim Empfänger nicht mehr steuerbar)
- **Beachten:** Gegenstück: empfangender Elternteil versteuert in Ziff. 5.2
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «12.2 Unterhaltsbeiträge für minderjährige Kinder   302»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0088.md) `tg-wl-2025__c0088` – «träge können längstens bis und mit dem Monat der Mündigkeit des Kindes abgezogen werden.»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0109.md) `tg-wl-2025__c0109` – «Der die Alimente leistende Elternteil, welcher diese Unter-»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0109.md) `tg-wl-2025__c0109` – «haltsbeiträge vom Einkommen abziehen kann, hat keinen Anspruch auf den Kinderabzug.»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0081.md) `tg-wl-2025__c0081` – «terhaltsbeiträge nicht mehr steuerbar und müssen daher nicht mehr deklariert werden.»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0081.md) `tg-wl-2025__c0081` – «Periodische Unterhaltsbeiträge (inklusive Kinderzulagen), die Sie für die unter Ihrer elterlichen   Ziffer 5.2»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0087.md) `tg-wl-2025__c0087` – «Deklaration ist eine Kopie der entsprechenden Passagen des Scheidungs- oder Trennungsurteils,»
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «25.1 a) für jedes Kind in Ausbildung mit Jahrg. 2000 – 2005»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0112.md) `tg-wl-2025__c0112` – «Fliessen Unterhaltsbeiträge, gelten bei minderjährigen Kindern grundsätzlich die gleichen Zutei-»

<a id="12-3-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.3 – Rentenleistungen (Code 304)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Rentenvertrag; Beiblatt mit Name/Adresse des Empfängers
- **Rein:** Leibrenten-/Verpfründungsvertrag → Kopie bei erstmaliger Deklaration · Zahlungsbelege → im 2025 bezahlte Leibrenten; Beiblatt mit Name/Adresse Empfänger/in
- **Rechnen:** Kanton: 40% × im 2025 bezahlte Leibrenten / Bund: bezahlte Leibrente × Berechnungssatz ESTV (Ertragsanteil, Art. 22 Abs. 3 lit. c DBG) → Code 304
- **Regel:** Bezahlte Leibrenten sind zu 40% abziehbar; Umfang der Leistungen auf Beiblatt mit Name und Adresse des Empfängers angeben.
- **Beachten:** WL TG nennt 40% ohne Spaltentrennung; DBG/WL Bund: nur Ertragsanteil – Bundesspalte separat rechnen
- **Beachten:** Bund-Berechnungssatz wird jährlich von der ESTV publiziert
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «12.3 Rentenleistungen   304»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0088.md) `tg-wl-2025__c0088` – «Im Jahr 2025 bezahlte Leibrenten können zu 40% vom Einkommen abgezogen werden.»
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t2.md) `tg-stg__par-34-t2` – «die dauernden Lasten sowie 40 Prozent der bezahlten Leibrenten;»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «die dauernden Lasten sowie der Ertragsanteil nach Artikel 22 Absatz 3 Buchstabe c der Leistungen aus Leibrenten- und aus Verpfründungsverträgen»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0087.md) `tg-wl-2025__c0087` – «der Trennungsvereinbarung oder des Rentenvertrages beizulegen.»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0052.md) `bund-wl-2a-2025__c0052` – «Bezahlte Leibrente / Verpfründung x Berechnungssatz (in %)»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0052.md) `bund-wl-2a-2025__c0052` – «jährlich von der Eidgenössischen Steuerverwaltung ESTV publi»

<a id="13-1-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.1 – Beiträge an Säule 3a Person 1, Anschluss 2. Säule (PK) ja/nein (Code 314)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Bescheinigung der Vorsorgeeinrichtung (Bank-/Versicherungsstiftung) über Einzahlungen 2025
- **Rein:** Bescheinigung Säule 3a (Bankstiftung/Versicherung) → Einzahlungen 2025 Person 1 (Code 314) · Lohnausweis/PK-Ausweis → Kreuz «Anschluss 2. Säule (PK)» ja/nein · Lohnausweis Nettolohn bzw. Reingewinn → Erwerbseinkommen (Basis 20% ohne 2. Säule)
- **Rechnen:** mit 2. Säule: min(Einzahlung; 7'258) / ohne: min(Einzahlung; 20% × Erwerbseinkommen; 36'288); Kanton = Bund
- **Regel:** Max. Fr. 7'258 mit Pensionskassenanschluss; ohne 2. Säule 20% des Erwerbseinkommens, max. Fr. 36'288. Feld «Anschluss 2. Säule (PK)» ankreuzen. Voraussetzung: AHV-pflichtige Erwerbstätigkeit im Jahr, Vorsorgevertrag lautet auf die erwerbstätige Person, Erwerbseinkommen ausgewiesen. Höchstbeträge sind zugleich Einzahlungslimiten. Bescheinigung einreichen.
- **Beachten:** Nur bei AHV-pflichtiger Erwerbstätigkeit 2025; Vertrag auf die erwerbstätige Person
- **Beachten:** Höchstbeträge = Einzahlungslimiten: Überzahlung vom Vorsorgeträger zurückzahlen lassen
- **Beachten:** Einzahlung längstens fünf Jahre über das ordentliche AHV-Rentenalter hinaus; Bescheinigung beilegen
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a mit Anschluss an 2. Säule: 8% des oberen BVG-Grenzbetrags = CHF 7'258 (Steuerperiode 2025).)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug mit Zugehörigkeit zur 2. Säule (8 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a ohne 2. Säule: 20% des Erwerbseinkommens, maximal CHF 36'288 (40% von 90'720; Steuerperiode 2025).)** · Bund **CHF 36'288 (Säule 3a: Höchstabzug ohne 2. Säule (max. 36'288, 40 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Ohne 2. Säule: 20% des Erwerbseinkommens (gilt auch für Unselbständige ohne PK), maximal CHF 36'288.)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. CHF 36'288))**
- **Bund:** Gleiche Höchstbeträge bei der direkten Bundessteuer.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «13.1 Person 1   Anschluss 2. Säule (PK) m ja   314»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0090.md) `tg-wl-2025__c0090` – «Vorsorge (2. Säule) angehören   Fr. 7'258»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0005.md) `tg-stp-34-27__c0005` – «Fr. 7’258 | Fr. 36’288»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0089.md) `tg-wl-2025__c0089` – «Der Abzug setzt zwingend eine AHV/IV-pflichtige selbständige oder unselbständige Erwerbs-»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0089.md) `tg-wl-2025__c0089` – «sorgeformen (Säule 3a) können längstens bis fünf Jahre nach Erreichen des ordentlichen Renten-»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0091.md) `tg-wl-2025__c0091` – «Bescheinigungen der Vorsorgeeinrichtungen bei.»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0090.md) `tg-wl-2025__c0090` – «Vorsorge (2. Säule) angehören: 20% des Erwerbseinkommens, maximal   Fr. 36'288»

<a id="13-2-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.2 – Beiträge an Säule 3a Person 2, Anschluss 2. Säule (PK) ja/nein (Code 315)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Bescheinigung der Vorsorgeeinrichtung für Person 2
- **Rein:** Bescheinigung Säule 3a Person 2 → Einzahlungen 2025 (Code 315) · Lohnausweis/PK-Ausweis Person 2 → Kreuz «Anschluss 2. Säule (PK)» ja/nein · Lohnausweis Person 2 bzw. Reingewinn → Erwerbseinkommen (Basis 20% ohne 2. Säule)
- **Rechnen:** je Person separat: mit 2. Säule min(Einzahlung; 7'258) / ohne min(Einzahlung; 20% × Erwerbseinkommen; 36'288); Kanton = Bund
- **Regel:** Wie Ziff. 13.1 für Person 2; jede erwerbstätige Person hat einen eigenen Abzug (Vorsorgenehmer).
- **Beachten:** Eigener Abzug nur, wenn Vertrag auf Person 2 lautet und für sie Erwerbseinkommen ausgewiesen ist
- **Beachten:** Kreuz «Anschluss 2. Säule (PK)» für Person 2 separat setzen; Bescheinigung beilegen
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a mit Anschluss an 2. Säule: 8% des oberen BVG-Grenzbetrags = CHF 7'258 (Steuerperiode 2025).)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug mit Zugehörigkeit zur 2. Säule (8 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a ohne 2. Säule: 20% des Erwerbseinkommens, maximal CHF 36'288 (40% von 90'720; Steuerperiode 2025).)** · Bund **CHF 36'288 (Säule 3a: Höchstabzug ohne 2. Säule (max. 36'288, 40 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Ohne 2. Säule: 20% des Erwerbseinkommens (gilt auch für Unselbständige ohne PK), maximal CHF 36'288.)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. CHF 36'288))**
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «13.2 Person 2   Anschluss 2. Säule (PK) m ja   315»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0089.md) `tg-wl-2025__c0089` – «Bei gemeinsam besteuerten Personen (Ehe»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0090.md) `tg-wl-2025__c0090` – «in der Steuererklärung ein Erwerbseinkommen ausgewiesen werden.»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0089.md) `tg-wl-2025__c0089` – «gen Person zu, wenn der Vorsorgevertrag auf sie als Vorsorgenehmer lautet.»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0091.md) `tg-wl-2025__c0091` – «dafür vorgesehenen Feld unter Ziffer 13.1 bzw. Ziffer 13.2 an.»

<a id="14-abzug-versicherungspraemien"></a>
### Ziff. 14 – Versicherungsprämien und Zinsen von Sparkapitalien (Formular 5.2, Code 330; Staat/Bund)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Formular 5.2 Abschnitt C (Code 330): tieferer Betrag von «A5» (bezahlte Prämien/Sparzinsen) und «B4» (Maximalabzug), getrennt Staat/Bund
- **Rein:** KK-Jahresbestätigung → Nettoprämie nach IPV (Formular 5.2 A Ziff. 1) · Policen/Prämienrechnungen Unfall-, Lebens-, Rentenversicherung → A Ziff. 2/3 · Formular 2 → erhaltene Sparzinsen (A Ziff. 4); Lohnausweis → Krankentaggeldversicherung (A Ziff. 5)
- **Rechnen:** Kanton: min(A Code 324; 7'000 bzw. 3'500 + 1'000 je Kind) / Bund: min(A; 3'700 bzw. 1'800 [ohne Säule 2/3a 5'550 bzw. 2'700] + 700 je Kind) → Code 330
- **Regel:** Abzug = niedrigerer Betrag aus tatsächlichen Prämien+Sparzinsen und Maximum. Maximum Kanton: Fr. 7'000 gemeinsam besteuert / Fr. 3'500 übrige, + Fr. 1'000 je Kind/unterstützte Person. Maximum Bund: Fr. 3'700 / Fr. 1'800 (ohne Beiträge an Säule 2/3a: Fr. 5'550 / Fr. 2'700, nicht kumulierbar), + Fr. 700 je Kind/unterstützte Person. Krankenkassenprämien netto nach Prämienverbilligung (IPV, inkl. EL-Prämienverbilligung) deklarieren; ohne Deklaration der KK-Prämien kann der Abzug verweigert werden.
- **Beachten:** KK-Prämie netto nach IPV (inkl. EL-Prämienverbilligung, Nachzahlungen); ohne KK-Deklaration evtl. kein Abzug
- **Beachten:** NBUV-Prämien nicht hier, sondern Ziff. 15.4
- **Beachten:** Bund: Ansatz ohne Säule 2/3a nicht mit ordentlichem Ansatz kumulierbar
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 7'000 (Versicherungsprämien und Sparzinsen, Verheiratete in ungetrennter Ehe: max. CHF 7'000 (inkl. eingetragene Partnerschaft).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 3'500 (Versicherungsprämien und Sparzinsen, übrige Steuerpflichtige: max. CHF 3'500.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag Versicherungsabzug: CHF 1'000 je minderjähriges oder in Ausbildung stehendes Kind bzw. unterstützte Person (mit Kinder-/Unterstützungsabzug).)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – Erhöhung für Personen ohne Beiträge an Säulen 2/3a gibt es nur bei der direkten Bundessteuer (CHF 5'550); kantonal kein separater Betrag.** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an Säule 2/3a (Erhöhung um die Hälfte))**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – Nur direkte Bundessteuer (CHF 2'700); kantonal kein separater Betrag.** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an Säule 2/3a)**
- **Bund:** Bund: Fr. 3'700 / Fr. 1'800 (+ Fr. 700 je Kind); ohne Säule 2/3a Fr. 5'550 / Fr. 2'700 (StP 34 Nr. 27 Ziff. 2.2, ab 2025).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «14.   Versicherungsprämien und Zinsen von Sparkapitalien   Formular 5 330»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0003.md) `tg-form-05-2-2025__c0003` – «1. Staatssteuer: der niedrigere Betrag von «A5» oder «B4 Staat»   330»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0212.md) `tg-wl-2025__c0212` – «für gemeinsam besteuerte Personen   Fr. 7'000   Fr. 3'700»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0002.md) `tg-stp-34-27__c0002` – «Fr. 7’000 | Fr. 6’200»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0001.md) `tg-form-05-2-2025__c0001` – «5. Krankentaggeldversicherung gemäss Lohnausweis»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0001.md) `tg-form-05-2-2025__c0001` – «4. erhaltene Sparzinsen gemäss Formular 2»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0002.md) `tg-form-05-2-2025__c0002` – «1. für gemeinsam besteuerte Personen (Eheleute / Partnerinnen oder Partner)   7000   3700»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0210.md) `tg-wl-2025__c0210` – «Dazu zählen auch über Ergänzungsleistungen zur AHV und IV ausgerichtete»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0209.md) `tg-wl-2025__c0209` – «Bei fehlender Deklaration behält sich die Veranlagungsbehörde vor, in der Steuerveranlagung kei-»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0211.md) `tg-wl-2025__c0211` – «In Ziffer 2 zu deklarieren sind Prämien für die private Unfallversicherung (ausgenommen NBUV, vgl.»

<a id="15-1-abzug-ahv-nichterwerbstaetige"></a>
### Ziff. 15.1 – AHV-Beiträge für nichterwerbstätige Personen (Code 342)

- **Schlüssel:** `abzug.ahv_nichterwerbstaetige` (AHV/IV/EO-Beiträge Nichterwerbstätiger u.ä.) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse) → AHV-Beitragsverfügung/Rechnung Ausgleichskasse
- **Rein:** AHV-Beitragsverfügung/Rechnung Ausgleichskasse (Nichterwerbstätige) → 2025 bezahlte AHV/IV/EO- und FAK-Beiträge
- **Rechnen:** Σ im Steuerjahr bezahlte Beiträge Nichterwerbstätiger an AHV/IV/EO + FAK → Code 342
- **Regel:** In der Regel nur AHV/IV/EO- und FAK-Beiträge Nichterwerbstätiger. Beiträge Unselbständiger sind schon im Nettolohn berücksichtigt, solche Selbständiger im Reingewinn (Ziff. 2) – nicht nochmals abziehen.
- **Beachten:** Unselbständige: Beiträge schon im Nettolohn (Ziff. 1.1/1.2); Selbständige: im Reingewinn (Ziff. 2.1/2.2)
- **Beachten:** Typischer Fall: Frührentner/innen
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «15.1 AHV-Beiträge für nichterwerbstätige Personen   342»
  - [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0093.md) `tg-wl-2025__c0093` – «Unter dieser Ziffer können in der Regel nur Beiträge an die AHV/IV/EO sowie FAK-Beiträge von»
  - [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0018.md) `tg-info-faq__c0018` – «können in Abzug gebracht werden. Sie können in Ziffer 15.1 auf Seite 3 der Steuererklärung deklariert werden.»
  - [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0018.md) `tg-info-faq__c0018` – «Kann ich als Frührentner/in die bezahlten AHV-Beiträge für nichterwerbstätige Personen»

<a id="15-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 15.2 – Beiträge an Einrichtungen der beruflichen Vorsorge Person 1 / Person 2 (Code 343 / 344)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) für selbst bezahlte, nicht vom Lohn abgezogene Einkäufe; Lohnausweis Ziff. 10.2 nur zur Kontrolle
- **Rein:** Bescheinigung Vorsorgeeinrichtung (Formular 21 EDP) → selbst überwiesene Einkäufe/Beiträge 2025 (Code 343/344) · Lohnausweis → Ziff. 10.1/10.2 nur zur Kontrolle (bereits im Nettolohn) · Selbständige: PK-Beitragsrechnung → Privatanteil
- **Rechnen:** Σ direkt (nicht über Lohn) an die PK bezahlte Beiträge/Einkäufe je Person → Code 343 / 344; Selbständige: nur Privatanteil (ohne Personal: Hälfte)
- **Regel:** Nur soweit nicht im Lohnausweis abgezogen: Lohnausweis Ziff. 10.1 (ordentliche Beiträge) und Ziff. 10.2 (Einkäufe) sind bereits im Nettolohn (Ziff. 11) berücksichtigt und dürfen hier NICHT nochmals abgezogen werden. Selbst entrichtete Einkäufe (Überweisung direkt an die PK) mit Bescheinigung der Vorsorgeeinrichtung. Selbständigerwerbende: nur Privatanteil (Arbeitgeberanteil bereits in Ziff. 2; ohne Personal gilt die Hälfte als Arbeitgeberanteil).
- **Beachten:** Lohnausweis Ziff. 10.1/10.2 nicht nochmals abziehen (schon in Ziff. 1 der Steuererklärung)
- **Beachten:** Arbeitgeberanteil Selbständiger bereits in Ziff. 2 berücksichtigt
- **Beachten:** Bescheinigungen der Vorsorgeeinrichtung beilegen
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «15.2 Beiträge an Einrichtungen der beruflichen Vorsorge»
  - [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0093.md) `tg-wl-2025__c0093` – «Die ordentlichen Beiträge sind in der Regel bereits vom Bruttolohn abgezogen»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «Vom Arbeitnehmer selber entrichtete, d. h. nicht vom Lohn abgezogene Einkaufsbeiträge an»
  - [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0094.md) `tg-wl-2025__c0094` – «Selbständig erwerbende Personen dürfen hier nur den Privatanteil der für sich selber bezahlten»
  - [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0094.md) `tg-wl-2025__c0094` – «Ist kein solches Personal vorhanden, gilt die Hälfte der Beiträge als»
  - [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0094.md) `tg-wl-2025__c0094` – «Bescheinigungen der Vorsorgeeinrichtungen sind der Steuererklärung beizule-»

<a id="15-3-abzug-drittbetreuung"></a>
### Ziff. 15.3 – Kosten für die Drittbetreuung von Kindern unter 14 Jahren (Code 345; Staat/Bund)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ⚠️ strittig
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Rechnungen/Bestätigungen Kita, Tagesmutter, Hort; Nachweis Erwerbstätigkeit/Ausbildung der Eltern
- **Rein:** Rechnungen/Quittungen Kita, Hort, Tagesfamilie, Mittagstisch → Betreuungskosten je Kind · Lohnausweis/Ausbildungsbestätigung → Nachweis Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit · Schulgeldrechnung Tagesschule/Internat → Pauschale Fr. 800 je Kind
- **Rechnen:** je Kind < 14: min(75% der Rechnungen (100% bei Nachweis ohne Lebenshaltung) + Fahrtkosten zur Betreuung; Kanton 10'100 / Bund 25'800)
- **Regel:** Kumulativ: Kind unter 14, im Haushalt des unterhaltenden Elternteils, Kosten kausal wegen Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit. Nur echte Betreuungskosten: ohne Gegenbeweis werden 75% der Rechnung anerkannt (100% bei nachgewiesen reinen Betreuungskosten). Maximum pro Kind: Kanton Fr. 10'100; Bund Fr. 25'800. Tagesschule/Internat: pauschal Fr. 800 pro Jahr und Kind (StP 34 Nr. 24). Getrennte Eltern: Abzug beim Elternteil im gleichen Haushalt; bei alternierender Obhut je max. die Hälfte des Maximalbetrags.
- **Beachten:** Abzug max. kleineres Erwerbseinkommen − zugehörige Berufsauslagen
- **Beachten:** Mittagstisch: bis Fr. 8 pro Tag = Verpflegung (nicht abziehbar)
- **Beachten:** Alternierende Obhut: je max. 50% des Maximums; Bund: WL rechnet mit 25'500 statt 25'800 (strittig)
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 10'100 (Kinderdrittbetreuung: nachgewiesene Kosten, höchstens CHF 10'100 pro Kind und Jahr; in der Regel nur 75% der deklarierten Kosten anerkannt (Lebenshaltungsanteil); Tagesschule/Internat pauschal CHF 800 pro Jahr und Kind; bei alternierender Obhut je max. die Hälfte.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind bis max. CHF 25'800 (Kind unter 14, im gleichen Haushalt, Zusammenhang mit Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit))**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 Jahre (Kind darf das 14. Altersjahr noch nicht vollendet haben (Geburtstagsmonat entscheidend); gleicher Haushalt; Kosten im direkten Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat)**
- **Bund:** Bund max. Fr. 25'800 pro Kind (Kanton Fr. 10'100).
- **Bemerkung:** Bund-Maximum 2025: Kurzübersicht WL (S. 4), WL Ziff. 15.3 Satz 'maximal Fr. 25'800' und StP 34 Nr. 27 Ziff. 4 nennen Fr. 25'800; die Erläuterung zur alternierenden Obhut in der WL (wl c0102/c0103) rechnet dagegen mit '50% von Fr. 25'500' (Wert 2024 laut StP 34 Nr. 27). Vermutlich Redaktionsversehen der WL; Fachperson bestätigt. Kanton Fr. 10'100 unstrittig.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «15.3 Kosten für die Drittbetreuung von Kindern unter 14 Jahren   345»
  - [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0096.md) `tg-wl-2025__c0096` – «Pro Kind können Sie kantonal die nachgewiesenen echten Kosten für die Drittbetreuung in Abzug»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0007.md) `tg-stp-34-27__c0007` – «2025 | Fr. 10’100 | Fr. 25’800»
  - [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0096.md) `tg-wl-2025__c0096` – «bringen, maximal jedoch Fr. 10'100.»
  - [WL TG 2025 S. 21–22](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0097.md) `tg-wl-2025__c0097` – «Bei der direkten Bundessteuer können maximal Fr. 25'800 der nachgewiesenen echten Kosten»
  - [WL TG 2025 S. 21–22](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0097.md) `tg-wl-2025__c0097` – «bis höchstens zur Hälfte der gesetzlichen Maximalbeträge (50% von Fr. 25'500)»
  - [StP 34 Nr. 24 (V 1.7.2024) S. 3](../../chunks/tg/2025/tg-stp-34-24-bis-2025/tg-stp-34-24-bis-2025__c0010.md) `tg-stp-34-24-bis-2025__c0010` – «kann unter dem Titel Betreuungskosten ein Abzug von Fr. 800 pro Jahr und Kind geltend gemacht werden»
  - [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0095.md) `tg-wl-2025__c0095` – «werden in der Regel daher jeweils nur 75% als echte Drittbetreuungskosten anerkannt.»
  - [StP 34 Nr. 24 (V 1.7.2024) S. 1](../../chunks/tg/2025/tg-stp-34-24-bis-2025/tg-stp-34-24-bis-2025__c0003.md) `tg-stp-34-24-bis-2025__c0003` – «nicht höher sein, als die Differenz zwischen dem kleineren Erwerbseinkommen und»
  - [StP 34 Nr. 24 (V 1.7.2024) S. 3](../../chunks/tg/2025/tg-stp-34-24-bis-2025/tg-stp-34-24-bis-2025__c0009.md) `tg-stp-34-24-bis-2025__c0009` – «Nebst den Betreuungskosten selber gehören auch die Fahrtkosten zur Betreuungs-»
  - [StP 34 Nr. 24 (V 1.7.2024) S. 4](../../chunks/tg/2025/tg-stp-34-24-bis-2025/tg-stp-34-24-bis-2025__c0011.md) `tg-stp-34-24-bis-2025__c0011` – «Kosten von bis zu Fr. 8 pro Tag als reine Verpflegungskosten betrachtet.»

<a id="15-4-abzug-uebrige"></a>
### Ziff. 15.4 – Weitere Abzüge (nähere Bezeichnung) (Code 346)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Aufstellung/Belege zum jeweiligen Abzug; Prämien NBU, AHV/IV/EO/FAK-Beiträge Erwerbstätiger
- **Rein:** Prämienrechnung obligatorische NBUV (UVG) → selbst bezahlte Prämien · Beitragsrechnung AHV/IV/EO/FAK Erwerbstätiger → selbst bezahlte Beiträge · Eigene Aufstellung mit Begründung → Belege je Abzug
- **Rechnen:** Σ belegte übrige Abzüge (z.B. NBUV-Prämien, AHV/IV/EO/FAK Erwerbstätiger), soweit nicht schon in Ziff. 1 oder 2 → Code 346
- **Regel:** Begründen und belegen. Beispiele: Prämien obligatorische Nichtberufsunfallversicherung (NBUV) oder AHV/IV/EO/FAK-Beiträge Erwerbstätiger, soweit nicht bereits in Ziff. 1/2 berücksichtigt. NICHT hier: Prämien UVG-versicherter Nichterwerbstätiger (→ Ziff. 14), Vermögensverwaltungskosten (→ Formular 2), Einsatzkosten für nicht steuerbare Geldspielgewinne (nicht abziehbar).
- **Beachten:** Unfallprämien Nichterwerbstätiger nach KVG → Ziff. 14; Vermögensverwaltungskosten → Wertschriftenverzeichnis
- **Beachten:** Einsatzkosten nicht steuerbarer Geldspielgewinne nicht abziehbar; steuerbare → Wertschriftenverzeichnis
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «15.4 Weitere Abzüge:   346»
  - [WL TG 2025 S. 22](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0099.md) `tg-wl-2025__c0099` – «Unter dieser Ziffer geltend gemachte Abzüge sind zu begründen und zu belegen.»
  - [WL TG 2025 S. 22](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0100.md) `tg-wl-2025__c0100` – «Einsatzkosten für nicht steuerbare Gewinne aus Geldspielen können nicht abgezogen werden.»

<a id="15-5-abzug-parteispenden"></a>
### Ziff. 15.5 – Mitgliederbeiträge und Zuwendungen an politische Parteien (Formular 6, Code 347)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Formular 6 Spalte «politische Parteien», Total (Code 347); Quittung ab Fr. 1'000 pro Zuwendung
- **Rein:** Quittungen/Mitgliederbeitragsrechnungen Partei → Formular 6 Spalte «politische Parteien» (einzeln, Name/Sitz) · Quittung/Bescheinigung ab Fr. 1'000 je Zuwendung → beilegen
- **Rechnen:** Kanton: min(Σ Parteien Formular 6 B; 10'000) / Bund: min(Σ; 10'600) → Code 347
- **Regel:** Voraussetzung: Partei im Parteienregister eingetragen und in einem kantonalen Parlament vertreten oder bei letzten Wahlen mind. 3% Stimmenanteil. Maximum Kanton Fr. 10'000, Bund Fr. 10'600. Pauschalvermerke «Spenden an diverse Organisationen» werden nicht anerkannt.
- **Beachten:** Partei: im Parteienregister, in kantonalem Parlament vertreten oder mind. 3% Stimmen (je alternativ)
- **Beachten:** Pauschalvermerke («Spenden an diverse Organisationen») nicht anerkannt
- **Beachten:** Spenden an gemeinnützige Institutionen → Ziff. 23.2
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister, im kantonalen Parlament vertreten oder mind. 3% Stimmen): max. CHF 10'000.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
- **Bund:** Bund max. Fr. 10'600 (Kanton Fr. 10'000).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «15.5 Mitgliederbeiträge und Zuwendungen an politische Parteien   Formular 6 347»
  - [Formular 6 TG 2025 S. 1](../../chunks/tg/2025/tg-form-06-2025/tg-form-06-2025__c0002.md) `tg-form-06-2025__c0002` – «Staatssteuer: max. Fr. 10 000.– Bundessteuer: max. Fr. 10 600.–»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0219.md) `tg-wl-2025__c0219` – «mindestens 3% der Stimmen erreicht hat.»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0008.md) `tg-stp-34-27__c0008` – «2025 | Fr. 10’000 | Fr. 10’600»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0220.md) `tg-wl-2025__c0220` – «Ab Fr. 1'000 pro Zuwendung»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0220.md) `tg-wl-2025__c0220` – «Pauschalabzüge für freiwillige Zuwendungen sowie Mitgliederbeiträge und Zuwendungen an politi-»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0221.md) `tg-wl-2025__c0221` – «Steuererklärung in Ziffer 23.2.»
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t5.md) `tg-stg__par-34-t5` – «in einem kantonalen Parlament vertreten sind, oder»

<a id="15-6-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 15.6 – Teilbesteuerungsabzug Beteiligungen im Privatvermögen (Formular 2 Hilfsblatt, Code 341; Staat/Bund)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Formular 2 letzte Seite «Hilfsblatt qualifizierte Beteiligungen im Privatvermögen» Ziff. 3
- **Rein:** Dividendenabrechnung/Steuerauszug → Beteiligungsertrag 2025 je Gesellschaft · Nachweis Beteiligungsquote ≥ 10% am Grund-/Stammkapital → durch Steuerpflichtige zu erbringen · Hilfsblatt (letzte Seite Formular 2) → Name/Sitz Gesellschaft, Quote, Ertrag 2025 je Beteiligung
- **Rechnen:** Hilfsblatt Ziff. 2 Σ Erträge qualifizierter Beteiligungen (≥ 10%) × Kanton 40% / Bund 30% = Ziff. 3 → Code 341
- **Regel:** Für Beteiligungen ≥ 10% am Grund-/Stammkapital im Privatvermögen: Teilbesteuerungsabzug Kanton 40% (steuerbar 60%), Bund 30% (steuerbar 70%) vom Total der Beteiligungserträge. Antrag jedes Jahr über das Hilfsblatt stellen, Nachweis der Voraussetzungen durch die steuerpflichtige Person (sonst 100%). Erträge selbst weiterhin in Spalte 8/9 des Wertschriftenverzeichnisses.
- **Beachten:** Erträge selbst voll im Wertschriftenverzeichnis (Spalte 8 oder 9) deklarieren; Abzug jährlich beantragen
- **Beachten:** Ohne Nachweis der Voraussetzungen Besteuerung zu 100%
- **Beachten:** Beteiligungen im Geschäftsvermögen: Antrag im Formular 14 (S. 4), nicht hier
- **Bund:** Teilbesteuerungsabzug Bund 30% (Kanton 40%).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «15.6 Teilbesteuerungsabzug Beteiligungen im Privatvermögen   Formular 2 341»
  - [Formular 2 TG 2025 S. 4](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0008.md) `tg-form-02-2025__c0008` – «3. Teilbesteuerungsabzug (Staatssteuer 40% / Bundessteuer 30%)»
  - [WL TG 2025 S. 34–35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0166.md) `tg-wl-2025__c0166` – «besteuerungsabzugs   3 einzusetzende Teilbesteuerungsabzug beträgt 40% bei den Staats- und Gemeindesteuern und»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0164.md) `tg-wl-2025__c0164` – «mögen von mindestens 10% am Grund- oder Stammkapital einer Kapitalgesellschaft oder Genos-»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0164.md) `tg-wl-2025__c0164` – «Bei fehlendem Nachweis erfolgt die Besteuerung zu 100%»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0165.md) `tg-wl-2025__c0165` – «Die Erträge aus qualifizierten Beteiligungen im Privatvermögen sind grundsätzlich in Spalte 8»
  - [WL TG 2025 S. 34–35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0166.md) `tg-wl-2025__c0166` – «bitte das Hilfsblatt qualifizierte Beteiligungen im Privatvermögen auf der letzten Seite des Wert-»

<a id="16-1-abzug-weiterbildung"></a>
### Ziff. 16.1 – Berufsorientierte Aus- und Weiterbildungskosten Person 1 (Code 348)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Kursrechnungen/Zahlungsnachweise mit Aufstellung; Lohnausweis Ziff. 13.3 (Arbeitgeberbeiträge)
- **Rein:** Kursrechnungen/Zahlungsbelege Person 1 → Aufstellung selbst getragener Kosten · Lohnausweis Ziff. 13.3 → vom Arbeitgeber vergütete Weiterbildungskosten (mindern Abzug) · Bestätigungen Beiträge Dritter (Bund, Verbände) → abziehen
- **Rechnen:** min(Σ Bildungskosten − Kostenbeteiligungen Dritter; 13'000) je Person; Kanton = Bund
- **Regel:** Selbst getragene berufsorientierte Aus- und Weiterbildungskosten bis max. Fr. 13'000 pro Person (Kanton und Bund). Ausgenommen: Kosten bis zum Abschluss der Erstausbildung (Berufslehre/Sekundarstufe II); ohne Sek-II-Abschluss erst ab vollendetem 20. Lebensjahr. Nicht an Erwerbstätigkeit im Jahr gebunden. Kostenbeteiligungen Dritter (Arbeitgeber, Bund, Verbände) abziehen; Arbeitgeberbeiträge an die Weiterbildung, die dem Arbeitnehmer vergütet wurden, stehen im Lohnausweis Ziff. 13.3 (direkt an das Bildungsinstitut bezahlte Beträge werden dort nicht bescheinigt, mindern aber ebenfalls die eigenen Kosten). PC/Notebook/Smartphone etc. nur bei spezifischem Lehrgangsbezug mit ca. 50% Privatanteil. Liebhaberei/Selbstentfaltung nicht abziehbar.
- **Beachten:** Nicht: Kosten bis zum ersten Sek-II-Abschluss; ohne Sek II erst ab vollendetem 20. Lebensjahr
- **Beachten:** IT-Geräte nur bei Lehrgangsbezug, Privatanteil i.d.R. 50%; Liebhaberei/Selbstentfaltung nicht abziehbar
- **Beachten:** Keine Erwerbstätigkeit im Jahr nötig; Aufstellung mit Belegen beilegen
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung: max. CHF 13'000 pro Person und Jahr (Kanton und Bund identisch). Ausgenommen Kosten bis zum ersten Abschluss Sekundarstufe II.)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Bund:** Maximum Fr. 13'000 auch beim Bund.
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «16.1 Person 1   348»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0102.md) `tg-wl-2025__c0102` – «maximal Fr. 13'000 pro Person beschränkt.»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0102.md) `tg-wl-2025__c0102` – «Kostenbeteiligungen Dritter (z.B. Arbeitgebende, Bund, Branchenverbände etc.) mindern die ab»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «In diesem Feld sind alle effektiven Vergütungen des Arbeitgebers für berufsorientierte Aus-»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0101.md) `tg-wl-2025__c0101` – «Weiterbildung abzugsfähig, sofern die betreffende Person das 20. Lebensjahr vollendet hat und es»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0103.md) `tg-wl-2025__c0103` – «Dabei ist ein angemessener Privatanteil von in der Regel 50% zu berücksichtigen.»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0103.md) `tg-wl-2025__c0103` – «Nicht abzugsfähig sind Aufwendungen für Bildungslehrgänge, die der Liebhaberei oder der Selbst-»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0102.md) `tg-wl-2025__c0102` – «werden, wenn während des ganzen Jahres keine Erwerbstätigkeit ausgeübt worden ist.»

<a id="16-2-abzug-weiterbildung"></a>
### Ziff. 16.2 – Berufsorientierte Aus- und Weiterbildungskosten Person 2 (Code 349)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Kursrechnungen/Zahlungsnachweise für Person 2; Lohnausweis Ziff. 13.3
- **Rein:** Kursrechnungen/Zahlungsbelege Person 2 → Aufstellung selbst getragener Kosten · Abrechnung Arbeitgeber/Bund/Verband → Kostenbeteiligungen Dritter Person 2 (mindern Abzug)
- **Rechnen:** min(Σ Bildungskosten Person 2 − Kostenbeteiligungen Dritter; 13'000); Kanton = Bund
- **Regel:** Wie Ziff. 16.1 für Person 2 (Maximum Fr. 13'000 pro Person).
- **Beachten:** Wie Ziff. 16.1: kein Abzug bis zum ersten Sek-II-Abschluss; Liebhaberei nicht abziehbar
- **Beachten:** Maximum 13'000 gilt je Person (Person 1 und 2 je separat)
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung: max. CHF 13'000 pro Person und Jahr (Kanton und Bund identisch). Ausgenommen Kosten bis zum ersten Abschluss Sekundarstufe II.)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «16.2 Person 2   349»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0102.md) `tg-wl-2025__c0102` – «Der Abzug ist sowohl bei den Staats- und Gemeindesteuern als auch bei der direkten Bundessteuer»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0102.md) `tg-wl-2025__c0102` – «Kostenbeteiligungen Dritter (z.B. Arbeitgebende, Bund, Branchenverbände etc.) mindern die ab»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0102.md) `tg-wl-2025__c0102` – «auf jährlich maximal Fr. 13'000 pro Person beschränkt.»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0101.md) `tg-wl-2025__c0101` – «sind nur die Aufwendungen zur Erlangung der Erstausbildung.»

<a id="17-abzug-behinderungskosten"></a>
### Ziff. 17 – Behinderungsbedingte Kosten (Formular 5.1 Abschnitt C, Code 350)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung, Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Formular 5.1 Abschnitt C: Aufwendungen (A) abzüglich Vergütungen Dritter (B)
- **Rein:** Rechnungen Hilfsmittel, Prothesen, Heim, Pflege, Umbau → Formular 5.1 A (Spalte behinderungsbedingt) · Abrechnungen KK/Versicherung, Hilflosenentschädigung, Pflegefinanzierung → Formular 5.1 B · Verfügung Hilflosenentschädigung bzw. Nachweis Gehörlosigkeit/Dialyse → Pauschale
- **Rechnen:** Formular 5.1 C: A − B (inkl. Anteil Lebenshaltung, Heim i.d.R. 2'000/Monat), ohne Selbstbehalt; alternativ Pauschale 2'500 / 5'000 / 7'500 → Code 350
- **Regel:** Selbst getragene behinderungsbedingte Kosten vollständig abziehbar (ohne Selbstbehalt), alternativ jährliche Pauschalen: gehörlos Fr. 2'500, Dialyse Fr. 2'500, Hilflosenentschädigung leicht Fr. 2'500 / mittel Fr. 5'000 / schwer Fr. 7'500. Vergütungen Dritter (Krankenkasse, IV-Hilfsmittel, Hilflosenentschädigung, Pflegefinanzierung) und Anteil Lebenshaltungskosten (bei Heim i.d.R. Fr. 2'000/Monat) abziehen. Krankheits- und Unfallkosten gehören auch bei Behinderten in Ziff. 23.1 (mit Selbstbehalt).
- **Beachten:** Krankheits-/Unfallkosten Behinderter → Ziff. 23.1 (mit 5% Selbstbehalt)
- **Beachten:** Nur Kosten mit Kausalzusammenhang zur Behinderung, keine Lebenshaltungs- oder Luxusausgaben
- **Beachten:** Auch für Personen mit Kinder-/Unterstützungsabzug; Nachweis beilegen
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «17.   Behinderungsbedingte Kosten   Formular 5 350»
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0003.md) `tg-form-05-1-2025__c0003` – «Abzugsfähige behinderungsbedingte Kosten   350»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0202.md) `tg-wl-2025__c0202` – «– Bezügerinnen/Bezüger einer Hilflosenentschädigung mittleren Grades   Fr. 5'000»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0201.md) `tg-wl-2025__c0201` – «det werden müssen (in der Regel Fr. 2 000 pro Monat).»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0201.md) `tg-wl-2025__c0201` – «werden, als diese 5% des Nettoeinkommens (Ziff. 22) übersteigen.»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0201.md) `tg-wl-2025__c0201` – «Behinderung entstehen (kausaler Zusammenhang) und weder Lebenshaltungs- noch Luxusausga-»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0198.md) `tg-wl-2025__c0198` – «welche Sie einen Kinder- oder Unterstützungsabzug geltend machen können, vollständig von den»
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0002.md) `tg-form-05-1-2025__c0002` – «3. Hilflosenentschädigung AHV/IV/SUVA»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0206.md) `tg-wl-2025__c0206` – «in Ziffer 23.1 auf Seite 3 der Steuererklärung ein, je verschieden für die Staats- und Gemeindesteu-»
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0001.md) `tg-form-05-1-2025__c0001` – «Formular 5.1: Krankheitskosten 2025»
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0002.md) `tg-form-05-1-2025__c0002` – «4. Anteil Lebenshaltungskosten»

<a id="18-abzug-zweiverdiener"></a>
### Ziff. 18 – Zweiverdienerabzug (Code 356) – nur direkte Bundessteuer

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Berechnung aus Erwerbseinkommen beider Personen (Nettolohn bzw. Reingewinn abzüglich Berufsauslagen, Säule 2 und 3a)
- **Rein:** Lohnausweise beider Personen → Nettolohn; Formular 4.2/4.3 → Berufsauslagen je Person · Bescheinigungen Säule 3a/PK je Person → abziehen · Selbständige: Reingewinn (Ziff. 2); Taggelder ALV/Kranken/Unfall, Militär/Zivilschutz → zählen mit
- **Rechnen:** Nur Bund: EK je Person = Erwerbseinkünfte − Berufsauslagen − Säule 2/3a; Abzug = min(max(50% × tieferes EK; 8'600); 14'100; tieferes EK); Kanton: keiner
- **Regel:** Nur Bundesspalte: 50% des niedrigeren Erwerbseinkommens der gemeinsam besteuerten Personen, mindestens Fr. 8'600 und höchstens Fr. 14'100 (2025). Liegt das niedrigere Erwerbseinkommen unter Fr. 8'600, kann nur dieser Betrag abgezogen werden. Erwerbseinkommen = Einkünfte nach Berufsauslagen sowie Beiträgen Säule 2/3a; Erwerbsausfallentschädigungen zählen mit; im vereinfachten Verfahren versteuerte Löhne zählen nicht. Kanton: kein Zweiverdienerabzug.
- **Beachten:** Nur Ehepaare/eingetragene Partner mit beidseitigem Erwerbseinkommen
- **Beachten:** Im vereinfachten Abrechnungsverfahren besteuerte Löhne zählen nicht
- **Beachten:** Erhebliche Mitarbeit im Betrieb des Ehegatten ohne Lohn: Reingewinn i.d.R. hälftig aufteilen
- **Limiten:**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **n/a – Kein kantonaler Zweiverdienerabzug TG (nur direkte Bundessteuer).** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (bei Ehegatten in ungetrennter Ehe mit beidseitigem Erwerbseinkommen))**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **n/a – Nur Bund (Fr. 8'600).** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum)**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **n/a – Nur Bund (Fr. 14'100).** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum)**
- **Bund:** Nur Bund: 50% des niedrigeren Erwerbseinkommens, min. Fr. 8'600, max. Fr. 14'100 (2025); Kanton kein Abzug.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «18.   Zweiverdienerabzug   356»
  - [WL TG 2025 S. 23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0104.md) `tg-wl-2025__c0104` – «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0009.md) `tg-stp-34-27__c0009` – «- mindestens | Fr. 8’600 | Fr. 8’500»
  - [StP 34 Nr. 25](../../chunks/tg/dauernd/tg-stp-34-25/tg-stp-34-25__c0001.md) `tg-stp-34-25__c0001` – «Im Gesetz über die Staats- und Gemeindesteuern des Kantons Thurgau ist kein Zweiverdienerabzug vorgesehen.»
  - [StP 34 Nr. 25](../../chunks/tg/dauernd/tg-stp-34-25/tg-stp-34-25__c0004.md) `tg-stp-34-25__c0004` – «Diese Einkünfte werden somit bei der Berechnung des Zweiverdienerabzugs mitberücksichtigt.»
  - [StP 34 Nr. 25](../../chunks/tg/dauernd/tg-stp-34-25/tg-stp-34-25__c0005.md) `tg-stp-34-25__c0005` – «Ein im vereinfachten Abrechnungsverfahren besteuerter Lohn bleibt folglich auch bei der Berechnung des Zweiverdienerabzugs unberücksichtigt.»
  - [StP 34 Nr. 25](../../chunks/tg/dauernd/tg-stp-34-25/tg-stp-34-25__c0011.md) `tg-stp-34-25__c0011` – «erfolgt für die Berechnung des Zweiverdienerabzugs in der Regel eine hälftige Aufteilung des Reingewinns auf die Ehepartner.»
  - [WL TG 2025 S. 23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0104.md) `tg-wl-2025__c0104` – «kann nur dieser Teilbetrag abgezogen werden.»

<a id="19-berechnung-total"></a>
### Ziff. 19 – Total Abzüge, zu übertragen in Ziffer 21 (Code 360; Staat/Bund)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 10–18)
- **Rein:** Übertrag aus Ziff. 10.1 bis 18 (je Spalte Staat/Bund)
- **Rechnen:** Σ Ziff. 10.1 bis 18 je Spalte Staat / Bund = Code 360 → Übertrag Ziff. 21
- **Regel:** Summe der Abzüge Ziff. 10 bis 18, je Spalte Staatssteuer/Bundessteuer; Übertrag in Ziff. 21.
- **Beachten:** Ziff. 18 nur in der Bundesspalte
- **Beachten:** Krankheitskosten und Zuwendungen (Ziff. 23.1/23.2) nicht hier, sondern nach Ziff. 22
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «19.   Total Abzüge, zu übertragen in Ziffer 21   360»
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «24.   Reineinkommen (Ziffer 22 abzüglich Ziffern 23.1 bis 23.3)   372»
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «10.1 Person 1   Formular 4.2 240»
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «18.   Zweiverdienerabzug   356»
  - [WL TG 2025 S. 23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0104.md) `tg-wl-2025__c0104` – «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.»

## Einkommensberechnung

<a id="20-berechnung-total"></a>
### Ziff. 20 – Total der Einkünfte, Übertrag von Seite 2 (Ziffer 6 oder 9)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Übertrag Ziff. 6 bzw. 9)
- **Rein:** Übertrag Seite 2: Ziff. 6 (Code 175) ohne Liegenschaften bzw. Ziff. 9 (Code 198) mit Liegenschaften
- **Rechnen:** ohne Liegenschaften = Ziff. 6 (Σ Ziff. 1 bis 5.5); mit Liegenschaften = Ziff. 9 (Ziff. 7 Übertrag + 8.1 Formular 7), je Spalte
- **Regel:** Ohne Liegenschaften Ziff. 6, mit Liegenschaften Ziff. 9 übertragen; Vorzeichen bei negativem Betrag.
- **Beachten:** Negativer Betrag mit Vorzeichen «–»
- **Beachten:** WL nennt «Ziff. 6.1/6.2», Formular hat Ziff. 6 und Ziff. 7 (Übertrag) – nach Formular ausfüllen
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «20.   Total der Einkünfte, Übertrag von Seite 2 (Ziffer 6 oder 9)»
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «6. Zwischentotal der Einkünfte   175»
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0009.md) `tg-form-01-2025__c0009` – «9. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 20   198»
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0009.md) `tg-form-01-2025__c0009` – «8.1 Einkünfte aus Liegenschaften   Formular 7 180»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0085.md) `tg-wl-2025__c0085` – «Total in Ziffer 6.1 (Summe der Ziffern 1 bis 5.5) direkt in Ziffer 20, Seite 3 der Steuererklärung.»

<a id="21-berechnung-total"></a>
### Ziff. 21 – Total der Abzüge, Übertrag von Ziffer 19

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Übertrag Ziff. 19)
- **Rein:** Übertrag Ziff. 19 (Code 360)
- **Rechnen:** = Ziff. 19 je Spalte Staat / Bund
- **Regel:** Übertrag Total Abzüge Ziff. 19, je Spalte Staat/Bund.
- **Beachten:** Bundesspalte enthält zusätzlich den Zweiverdienerabzug (Ziff. 18)
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «21.   Total der Abzüge, Übertrag von Ziffer 19»
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «18.   Zweiverdienerabzug   356»
  - [WL TG 2025 S. 23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0104.md) `tg-wl-2025__c0104` – «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.»

<a id="22-berechnung-total"></a>
### Ziff. 22 – Nettoeinkommen (Code 362; Staat/Bund)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 20 minus Ziff. 21)
- **Rein:** Rechenzeile: Ziff. 20 − Ziff. 21
- **Rechnen:** Ziff. 20 − Ziff. 21 je Spalte → Code 362; Basis für 5% Selbstbehalt (Ziff. 23.1) und 20% Maximum Zuwendungen (Ziff. 23.2)
- **Regel:** Basis für den Selbstbehalt Krankheitskosten (5%) und das Maximum der Zuwendungen (20%): Staats- und Bundesspalte getrennt verwenden.
- **Beachten:** Kanton und Bund getrennt (Spalten können abweichen)
- **Beachten:** Kanton Zuwendungen: Nettoeinkommen bis 40'000 → max. 8'000, darüber 20%
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5% des Nettoeinkommens (Ziff. 22 der Steuererklärung).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Maximal 20% des Nettoeinkommens (Ziff. 22); bei Nettoeinkommen bis CHF 40'000 maximal CHF 8'000. Nur an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentliche/gemeinnützige Zwecke) sowie Bund/Kantone/Gemeinden.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «22.   Nettoeinkommen   362»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0206.md) `tg-wl-2025__c0206` – «ziehen Sie einen Selbstbehalt von 5% des Nettoeinkommens gemäss Ziffer 22 der Steuererklä»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0218.md) `tg-wl-2025__c0218` – «nem Nettoeinkommen bis Fr. 40'000 maximal den Betrag von Fr. 8 000 abziehen.»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0218.md) `tg-wl-2025__c0218` – «einkommen über Fr. 40'000 können Sie maximal 20% des Nettoeinkommens (Ziffer 22 der Steuer-»

<a id="23-1-abzug-krankheitskosten"></a>
### Ziff. 23.1 – Krankheits- und Unfallkosten (Formular 5.1 Abschnitt D, Code 364; Staat/Bund)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 5.1 Abschnitt D: (A Aufwendungen – B Vergütungen) abzüglich 5% Selbstbehalt von Ziff. 22
- **Rein:** Arzt-, Zahnarzt-, Spitalrechnungen, Medikamente, Brillen → Formular 5.1 A (Spalte Krankheit) · KK-Leistungsabrechnung → Franchise/Selbstbehalt (A Ziff. 1) und Vergütungen (B Ziff. 1) · Ärztliche Verordnung → Therapien/Kuren (A Ziff. 6), Diät
- **Rechnen:** Formular 5.1 D: (A − B) − 5% × Ziff. 22, je Spalte Staat / Bund → Code 364
- **Regel:** Selbst getragene Kosten über 5% des Nettoeinkommens (Ziff. 22; Staat und Bund je mit eigener Spalte) für sich und Personen mit Kinder-/Unterstützungsabzug. Vergütungen der Krankenkasse/Versicherungen/Hilflosenentschädigung und Anteil Lebenshaltungskosten abziehen. Nicht abziehbar: Krankenkassenprämien, Fahrkosten zum Arzt (ausser dauernde Pflegebedürftigkeit), Fitness/Schönheitsbehandlungen, nicht ärztlich verordnete Akupunktur/Prävention. Diät-Pauschale Fr. 2'500 bei lebensnotwendiger Diät (z.B. Zöliakie, nicht Diabetes), ausgeschlossen bei Leistungen Dritter. Belege zusammenstellen und einreichen.
- **Beachten:** Nicht abziehbar: KK-Prämien, Fahrten zum Arzt (ausser dauernde Pflegebedürftigkeit), Fitness, Schönheit
- **Beachten:** Diät-Pauschale Fr. 2'500 (z.B. Zöliakie; nicht Diabetes; nicht bei Leistungen Dritter)
- **Beachten:** Auch für Personen mit Kinder-/Unterstützungsabzug; Belege geordnet beilegen
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5% des Nettoeinkommens (Ziff. 22 der Steuererklärung).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Bund:** Selbstbehalt 5% des Bundes-Nettoeinkommens (rechte Spalte Ziff. 22).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «23.1 Krankheits- und Unfallkosten   Formular 5 364»
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0004.md) `tg-form-05-1-2025__c0004` – «abzüglich Selbstbehalt (5% von Ziffer 22 der Steuererklärung)»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0197.md) `tg-wl-2025__c0197` – «Soweit Sie die Kosten selber tragen und diese 5% des Nettoeinkommens (Ziffer 22) übersteigen,»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0198.md) `tg-wl-2025__c0198` – «labzug ist in jedem Fall mangels selbst getragenen Mehrkosten ausgeschlossen, wenn Leistungen»
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0001.md) `tg-form-05-1-2025__c0001` – «1. Selbstbehalt / Franchise gemäss detaillierter Kostenzusammenstellung der Krankenkasse»
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0001.md) `tg-form-05-1-2025__c0001` – «6. Ärztlich verordnete Therapien, wie Kuraufenthalte usw. (Kopie ärztliche Verordnung beilegen)»
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0001.md) `tg-form-05-1-2025__c0001` – «Die Belege sind geordnet beizulegen»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0203.md) `tg-wl-2025__c0203` – «Ebenfalls nicht abziehen können Sie die Fahrkosten zum Arzt, Zahnarzt, Spital usw., ausgenommen»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0203.md) `tg-wl-2025__c0203` – «bei dauernder Pflegebedürftigkeit. Nicht abzugsfähig sind zudem die Krankenkassenprämien sowie»
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0002.md) `tg-form-05-1-2025__c0002` – «B. Vergütungen Dritter und Anteil Lebenshaltungskosten»

<a id="23-2-abzug-spenden"></a>
### Ziff. 23.2 – Freiwillige Zuwendungen (Formular 6, Code 366; Staat/Bund)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Formular 6 Spalte «gemeinnützige oder öffentliche Zwecke» (Code 366); Bestätigung ab Fr. 1'000 pro Zuwendung
- **Rein:** Spendenbestätigungen/Quittungen → Formular 6 Spalte «gemeinnützige oder öffentliche Zwecke» (einzeln, Name/Sitz) · Quittung ab Fr. 1'000 je Zuwendung → beilegen · Liste steuerbefreiter Institutionen (Steuerverwaltung TG) → Abzugsfähigkeit prüfen
- **Rechnen:** Kanton: min(Σ − 200; Ziff. 22 ≤ 40'000: 8'000, sonst 20% × Ziff. 22) / Bund: falls Σ ≥ 100: min(Σ; 20% × Ziff. 22) → Code 366
- **Regel:** Zuwendungen an in der Schweiz ansässige steuerbefreite Institutionen (öffentliche/gemeinnützige Zwecke; Liste der Steuerverwaltung). Kanton: Selbstbehalt Fr. 200 (nur der übersteigende Betrag), max. Fr. 8'000 bei Nettoeinkommen bis Fr. 40'000, sonst max. 20% des Nettoeinkommens (Ziff. 22). Bund: ab Gesamtbetrag Fr. 100, ohne Selbstbehalt, max. 20% des Nettoeinkommens. Nicht abziehbar: religiöse, wohltätige, kulturelle, gesellige, sportliche Zwecke, Auslandssitz, ehrenamtliche Arbeit; keine Sammelvermerke.
- **Beachten:** Nicht abziehbar: religiöse, wohltätige, kulturelle, gesellige, sportliche Zwecke, Sitz im Ausland, ehrenamtliche Arbeit
- **Beachten:** Sammelvermerke («Spenden an diverse Organisationen») nicht anerkannt
- **Beachten:** Parteispenden → Ziff. 15.5
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 200 (Freiwillige Zuwendungen kantonal nur abziehbar, soweit gesamthaft CHF 200 übersteigend (Bund: ab CHF 100).)** · Bund **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen (CH) bzw. Gemeinwesen: mindestens CHF 100 im Steuerjahr)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Maximal 20% des Nettoeinkommens (Ziff. 22); bei Nettoeinkommen bis CHF 40'000 maximal CHF 8'000. Nur an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentliche/gemeinnützige Zwecke) sowie Bund/Kantone/Gemeinden.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Bund:** Bund: Mindestbetrag Fr. 100 (Gesamtbetrag), ohne Selbstbehalt, max. 20% des Nettoeinkommens; Kanton: Selbstbehalt Fr. 200, max. Fr. 8'000 bzw. 20%.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «23.2 Freiwillige Zuwendungen   Formular 6 366»
  - [Formular 6 TG 2025 S. 1](../../chunks/tg/2025/tg-form-06-2025/tg-form-06-2025__c0002.md) `tg-form-06-2025__c0002` – «Nettoeinkommen (gem. Ziff. 22) über Fr. 40000.–: max. 20% vom Nettoeinkommen   366»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0218.md) `tg-wl-2025__c0218` – «Soweit die freiwilligen Zuwendungen gesamthaft Fr. 200 übersteigen, können Sie kantonal bei ei»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0217.md) `tg-wl-2025__c0217` – «auf religiöse, wohltätige, kulturelle, gesellige oder sportliche Zwecke von der Steuerpflicht befreit»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0217.md) `tg-wl-2025__c0217` – «sind sowie an juristische Personen mit Sitz im Ausland.»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0220.md) `tg-wl-2025__c0220` – «Ab Fr. 1'000 pro Zuwendung»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0220.md) `tg-wl-2025__c0220` – «Pauschalabzüge für freiwillige Zuwendungen sowie Mitgliederbeiträge und Zuwendungen an politi-»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0221.md) `tg-wl-2025__c0221` – «teien (Maximalabzüge beachten) auf Seite 3 der Steuererklärung in Ziffer 15.5.»

<a id="23-3-abzug-uebrige"></a>
### Ziff. 23.3 – Separat zu besteuernde Liquidationsgewinne (Code 368; Staat/Bund)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Berechnung Liquidationsgewinn (Formular 14a), Geschäftsabschlüsse der letzten zwei Jahre
- **Rein:** Jahresrechnungen der letzten zwei Geschäftsjahre → realisierte stille Reserven · Formular 14a (Download TG) → berechneter Liquidationsgewinn · Übertrag: in Ziff. 2.1/2.2 enthaltener Liquidationsgewinn, je Spalte Staat/Bund
- **Rechnen:** Abzug = in Ziff. 2.1/2.2 enthaltener Liquidationsgewinn (stille Reserven der letzten zwei Geschäftsjahre), je Spalte Staat / Bund → Code 368
- **Regel:** Bei definitiver Geschäftsaufgabe nach vollendetem 55. Altersjahr oder wegen Invalidität: in den letzten zwei Geschäftsjahren realisierte stille Reserven werden getrennt privilegiert besteuert; hier den in Ziff. 2.1/2.2 enthaltenen Liquidationsgewinn von den ordentlichen Einkünften abziehen.
- **Beachten:** Nur bei definitiver Aufgabe nach vollendetem 55. Altersjahr oder wegen Invalidität; auch Erben ohne Fortführung
- **Beachten:** Separate Besteuerung Restbetrag: Kanton einfache Steuer 5 % / Bund Satz auf einem Fünftel, mind. 2 %
- **Beachten:** Einkauf berufl. Vorsorge abziehbar; sonst Einkaufspotenzial: Kanton wie Vorsorgekapital / Bund zu einem Fünftel Tarif
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «23.3 Separat zu besteuernde Liquidationsgewinne   368»
  - [WL TG 2025 S. 23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0106.md) `tg-wl-2025__c0106` – «Erfüllen Sie die entsprechenden Voraussetzungen, können Sie die im Geschäftsergebnis in den»
  - [WL TG 2025 S. 23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0105.md) `tg-wl-2025__c0105` – «Sowohl bei den Staats- und Gemeindesteuern als auch bei der direkten Bundessteuer werden bei»
  - [WL TG 2025 S. 23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0105.md) `tg-wl-2025__c0105` – «nach dem vollendeten 55. Altersjahr»
  - [WL TG 2025 S. 23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0106.md) `tg-wl-2025__c0106` – «die mittels Erbgang übernommene Unternehmung nicht fortführen»
  - [StG TG § 38b](../../chunks/tg/2025/tg-stg/tg-stg__par-38b.md) `tg-stg__par-38b` – «Der Restbetrag der realisierten stillen Reserven wird zum Satz der einfachen Steuer von 5 Prozent besteuert.»
  - [StG TG § 38b](../../chunks/tg/2025/tg-stg/tg-stg__par-38b.md) `tg-stg__par-38b` – «Einkaufsbeiträge gemäss § 34 Abs. 1 Ziff. 6 sind abziehbar.»
  - [StG TG § 38b](../../chunks/tg/2025/tg-stg/tg-stg__par-38b.md) `tg-stg__par-38b` – «in gleicher Weise wie Kapitalleistungen aus Vorsorge gemäss § 39 erhoben»
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t2.md) `tg-stg__par-34-t2` – «Prämien und Beiträge zum Erwerb von Ansprüchen aus Alters-, Hinterlassenen- und Invalidenversicherung und aus Einrichtungen der beruflichen Vorsorge»
  - [DBG Art. 37b](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-37b.md) `bund-dbg-2025__art-37b` – «ist ein Fünftel dieses Restbetrages massgebend, es wird aber in jedem Falle eine Steuer zu einem Satz von mindestens 2 Prozent erhoben»
  - [DBG Art. 37b](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-37b.md) `bund-dbg-2025__art-37b` – «zu einem Fünftel der Tarife nach Artikel 36 berechnet»

<a id="24-berechnung-total"></a>
### Ziff. 24 – Reineinkommen (Ziffer 22 abzüglich Ziffern 23.1 bis 23.3) (Code 372)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 22 Nettoeinkommen (Code 362) · Übertrag Ziff. 23.1 Formular 5 (Code 364), 23.2 Formular 6 (Code 366), 23.3 (Code 368)
- **Rechnen:** Ziff. 22 − (Ziff. 23.1 + 23.2 + 23.3), je Spalte Staat / Bund → Code 372
- **Regel:** Ziff. 22 minus Ziff. 23.1–23.3, je Spalte Staat/Bund. Das Reineinkommen (Staat) ist satzbestimmend für den Abzug Ziff. 25.3.
- **Beachten:** Reineinkommen Spalte Staat ist massgebend für den Abzug Ziff. 25.3 (AHV-Rente, erwerbsunfähig, verwitwet)
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «24.   Reineinkommen (Ziffer 22 abzüglich Ziffern 23.1 bis 23.3)   372»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0116.md) `tg-wl-2025__c0116` – «je nach Höhe ihres Reineinkommens gemäss Ziffer 24 der Steuererklärung, kantonal Anspruch»

<a id="25-1-a-jg-2000-2005-sozialabzug-kinder"></a>
### Ziff. 25.1 a) Jg. 2000–2005 – Kinderabzug für jedes Kind in Ausbildung mit Jahrgang 2000–2005 (Code 380; Staat Fr. 10'600 / Bund Fr. 6'800)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1 (Kinder: Geburtsdatum, Ausbildung); Anzahl Kinder
- **Rein:** Formular 1 S. 1 Kinder → Geburtsdatum, Haushalt, Schule/Lehrfirma, voraussichtliches Ausbildungsende · Formular 1 S. 1 (nur getrennt besteuerte Eltern) → Unterhaltsbeiträge des anderen Elternteils
- **Rechnen:** Anzahl Kinder Jg. 2000–2005 in Ausbildung am 31. Dezember 2025 × Kanton Fr. 10'600 / Bund Fr. 6'800 → Code 380
- **Regel:** Pro Kind in Ausbildung (Stichtag 31.12.2025): Kanton Fr. 10'600, Bund Fr. 6'800. Nur eigene Kinder (nicht Pflege-/Stiefkinder); kein Abzug, wenn das volljährige Kind ein Einkommen für den selbständigen Lebensunterhalt erzielt. Zuteilung bei getrennt besteuerten Eltern nach Alimenten/Sorgerecht/Obhut; Kanton und Bund haben unterschiedliche Regeln (Kanton hälftig nur bei gemeinsamem Sorgerecht UND alternierender Obhut ohne Alimente).
- **Beachten:** Ausbildung vor Stichtag beendet → kein Abzug, auch nicht pro rata; Pflege-/Stiefkinder ausgeschlossen
- **Beachten:** Kein Abzug, wenn das volljährige Kind ein Einkommen für den selbständigen Lebensunterhalt erzielt
- **Beachten:** Getrennte Eltern: Abzug ungeteilt beim Elternteil, der den Unterhalt hauptsächlich trägt (i.d.R. Alimente-Zahler)
- **Limiten:**
  - Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF): Kanton **CHF 10'600 (Kinderabzug in Ausbildung nach Vollendung des 20. Altersjahres bis höchstens zum vollendeten 26. Altersjahr: CHF 10'600 (WL 2025: Jahrgang 2000-2005). Keine Unterscheidung nach auswärtiger Ausbildung; Abstufung erfolgt nach Alter.)** · Bund **n/a – Bund: gleicher Kinderabzug CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 7'400 (Kinderabzug je Kind (nicht selbständig besteuert, in Ausbildung oder erwerbsunfähig; Steuerpflichtiger kommt für Unterhalt auf): CHF 7'400. Stichtag Ende Steuerperiode.)** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
- **Bund:** Bund Fr. 6'800 pro Kind (alle Jahrgänge).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «25.1 a) für jedes Kind in Ausbildung mit Jahrg. 2000 – 2005   Fr. 10 600   Fr. 6800   380»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0006.md) `tg-stp-36-1__c0006` – «- 20. Altersjahres bis zum vollendeten 26. Altersjahres | Fr. 10’600»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0108.md) `tg-wl-2025__c0108` – «Erzielt ein volljähriges Kind, obwohl es eine Ausbildung absolviert, ein Einkommen, das einen selb»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0107.md) `tg-wl-2025__c0107` – «am 31. Dezember 2025 bzw. am Ende der Steuerpflicht massgebend»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0107.md) `tg-wl-2025__c0107` – «kann der Sozialabzug nicht gewährt werden (auch nicht pro rata)»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0107.md) `tg-wl-2025__c0107` – «Pflegekinder, Stiefkinder etc. geltend gemacht werden.»
  - [WL TG 2025 S. 12](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0045.md) `tg-wl-2025__c0045` – «den Namen der Ausbildungsstätte oder der Lehrfirma sowie das voraussichtliche Ende»
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0003.md) `tg-form-01-2025__c0003` – «Leistet der andere Elternteil Unterhaltsbeiträge»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0111.md) `tg-wl-2025__c0111` – «Nach Erreichen der Volljährigkeit des Kindes steht der Kinderabzug demjenigen Elternteil zu, der»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0111.md) `tg-wl-2025__c0111` – «dies in der Regel der die Alimente leistende Elternteil.»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0112.md) `tg-wl-2025__c0112` – «Bei volljährigen Kindern wird der Kinderabzug immer ungeteilt einem Elternteil zugesprochen.»

<a id="25-1-a-jg-2006-2009-sozialabzug-kinder"></a>
### Ziff. 25.1 a) Jg. 2006–2009 – Kinderabzug für jedes Kind in Ausbildung mit Jahrgang 2006–2009 (Code 382; Staat Fr. 8'500 / Bund Fr. 6'800)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1 (Kinder: Geburtsdatum, Ausbildung)
- **Rein:** Formular 1 S. 1 Kinder → Geburtsdatum, Haushalt, Schule/Lehrfirma, voraussichtliches Ausbildungsende · Formular 1 S. 1 (nur getrennt besteuerte Eltern) → Unterhaltsbeiträge, Sorgerecht, Obhut
- **Rechnen:** Anzahl Kinder Jg. 2006–2009 in Ausbildung am 31. Dezember 2025 × Kanton Fr. 8'500 / Bund Fr. 6'800 → Code 382
- **Regel:** Kinder ab vollendetem 16. Altersjahr in Ausbildung: Kanton Fr. 8'500, Bund Fr. 6'800. Zuteilungs- und Stichtagsregeln wie bei Code 380.
- **Beachten:** Kanton: erhöhter Abzug nur in Ausbildung nach vollendetem 16. Altersjahr; sonst 25.1 b)
- **Beachten:** Jg. 2008–2009 mit Alimenten: nur Empfänger (Kanton + Bund); Jg. 2006–2007 (volljährig): Hauptunterhaltsträger
- **Beachten:** Minderjährige ohne Alimente hälftig: Kanton nur gem. Sorgerecht + alternierende Obhut; Bund schon gem. Sorgerecht
- **Limiten:**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 8'500 (Kinderabzug erhöht sich für jedes in Ausbildung stehende Kind nach Vollendung des 16. Altersjahres auf CHF 8'500 (WL 2025: Jahrgang 2006-2009).)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Kinderabzug CHF 6'800 wie für Minderjährige (kein höherer Ausbildungsabzug))**
- **Bund:** Bund Fr. 6'800.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «mit Jahrg. 2006 – 2009   Fr. 8 500   Fr. 6800   382»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0006.md) `tg-stp-36-1__c0006` – «- 16. Altersjahres auf | Fr. 8’500»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0107.md) `tg-wl-2025__c0107` – «am 31. Dezember 2025 bzw. am Ende der Steuerpflicht massgebend»
  - [VAKP TG § 1](../../chunks/tg/2025/tg-vakp/tg-vakp__par-1.md) `tg-vakp__par-1` – «der Abzug erhöht sich für jedes in Ausbildung stehende Kind nach Vollendung des 16. Altersjahres auf»
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0003.md) `tg-form-01-2025__c0003` – «Geburtsdatum   Haushalt?   Ausbildungsende (wenn in Ausbildung)»
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0003.md) `tg-form-01-2025__c0003` – «Gemeinsames Sorgerecht* m ja   Alternierende Obhut*»
  - [WL TG 2025 S. 30](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0139.md) `tg-wl-2025__c0139` – «Vermögen und Erträge von Kindern unter Ihrer elterlichen Sorge (Jahrgang 2008 und jünger)»
  - [WL TG 2025 S. 30](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0139.md) `tg-wl-2025__c0139` – «mögen und Erträge von Personen mit Jahrgang 2007 und älter sind durch diese selbst zu versteuern»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0109.md) `tg-wl-2025__c0109` – «Der Kinderabzug steht nur dem die zu versteuernden Unterhaltsbeiträge (Alimente) für minderjäh-»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0112.md) `tg-wl-2025__c0112` – «gelten bei minderjährigen Kindern grundsätzlich die gleichen Zutei-»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0111.md) `tg-wl-2025__c0111` – «Nach Erreichen der Volljährigkeit des Kindes steht der Kinderabzug demjenigen Elternteil zu, der»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0110.md) `tg-wl-2025__c0110` – «Das Vorliegen eines gemeinsamen Sorgerechts ohne alternierende Obhut reicht»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0112.md) `tg-wl-2025__c0112` – «Besteht ein gemeinsames Sorgerecht und fliessen keine Unterhaltsbeiträge, werden die Kin-»

<a id="25-1-b-sozialabzug-kinder"></a>
### Ziff. 25.1 b) – Kinderabzug für jedes übrige Kind (Code 384; Staat Fr. 7'400 / Bund Fr. 6'800)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1 (Kinder: Geburtsdatum)
- **Rein:** Formular 1 S. 1 Kinder → Geburtsdatum, Haushalt · Formular 1 S. 1 (nur getrennt besteuerte Eltern) → Unterhaltsbeiträge, Sorgerecht, Obhut
- **Rechnen:** Anzahl übrige Kinder × Kanton Fr. 7'400 / Bund Fr. 6'800 → Code 384
- **Regel:** Alle übrigen (nicht selbständig besteuerten, minderjährigen oder erwerbsunfähigen) Kinder: Kanton Fr. 7'400, Bund Fr. 6'800. Kinder mit Alimentenbezug (Ziff. 5.2): Abzug beim empfangenden Elternteil. Zusätzlich: Steuergutschrift Ziff. 28.1 und Versicherungs-/Vermögensfreibetrag je Kind.
- **Beachten:** Übrige = ohne 25.1 a): z.B. unter 16, minderjährig ohne Ausbildung, erwerbsunfähig, Kanton: Ausbildung über 26
- **Beachten:** Minderjährige mit Alimenten: Abzug nur beim empfangenden, nicht beim zahlenden Elternteil (Kanton + Bund)
- **Beachten:** Je Kind zudem: Gutschrift Ziff. 28.1 (max. Fr. 100, minderjährig); Versicherungsabzug + Kanton Fr. 1'000 / Bund Fr. 700
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 7'400 (Kinderabzug je Kind (nicht selbständig besteuert, in Ausbildung oder erwerbsunfähig; Steuerpflichtiger kommt für Unterhalt auf): CHF 7'400. Stichtag Ende Steuerperiode.)** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag Versicherungsabzug: CHF 1'000 je minderjähriges oder in Ausbildung stehendes Kind bzw. unterstützte Person (mit Kinder-/Unterstützungsabzug).)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
- **Bund:** Bund Fr. 6'800.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «b) für jedes übrige Kind   Fr. 7 400   Fr. 6800   384»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0108.md) `tg-wl-2025__c0108` – «für jedes übrige Kind   Fr. 7'400   Fr. 6'800»
  - [VAKP TG § 1](../../chunks/tg/2025/tg-vakp/tg-vakp__par-1.md) `tg-vakp__par-1` – «für nicht selbständig besteuerte, für in Ausbildung stehende oder erwerbsunfähige Kinder»
  - [VAKP TG § 1](../../chunks/tg/2025/tg-vakp/tg-vakp__par-1.md) `tg-vakp__par-1` – «bis höchstens zum vollendeten 26. Altersjahr auf»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0109.md) `tg-wl-2025__c0109` – «Der Kinderabzug steht nur dem die zu versteuernden Unterhaltsbeiträge (Alimente) für minderjäh-»
  - [WL TG 2025 S. 24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0112.md) `tg-wl-2025__c0112` – «gelten bei minderjährigen Kindern grundsätzlich die gleichen Zutei-»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0118.md) `tg-wl-2025__c0118` – «gutschrift von maximal Fr. 100.»

<a id="25-2-sozialabzug-unterstuetzung"></a>
### Ziff. 25.2 – Unterstützungsabzug für jede unterstützte Person (Code 386; Staat Fr. 2'700 / Bund Fr. 6'800)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1 (Erwerbsunfähige und unterstützungsbedürftige Personen); Bestätigung der Wohnsitzgemeinde/Fürsorgebehörde
- **Rein:** Formular 1 S. 1 Unterstützte Personen → Name, Geburtsdatum, Haushalt, Adresse, Unterstützungsbetrag · Bestätigung Wohnsitzgemeinde (Steuerausweis/Fürsorgebehörde) → Unterstützungsbedürftigkeit · Zahlungsnachweise → tatsächlich geleistete Unterstützung
- **Rechnen:** Anzahl unterstützte Personen × Kanton Fr. 2'700 / Bund Fr. 6'800 (Bund nur bei Beitrag ≥ Fr. 6'800 je Person) → Code 386
- **Regel:** Kanton Fr. 2'700, wenn zur Hauptsache für den Unterhalt einer erwerbsunfähigen, unterstützungsbedürftigen Person aufgekommen wird (Praxis: mind. 50% des betreibungsrechtlichen Existenzminimums). Bund Fr. 6'800 bei nachgewiesenem Beitrag von mind. Fr. 6'800. Nicht für Ehegatte oder Kinder mit Kinderabzug/Unterhaltsabzug.
- **Beachten:** Kanton: zur Hauptsache = mehr als 50 % des betreibungsrechtlichen Existenzminimums (§ 12 StV; WL: mind. 50 %)
- **Beachten:** Formular S. 1 nennt Mindestbeitrag Fr. 12 000 (Kanton) / Fr. 6 800 (Bund) – Abweichung zur WL, prüfen
- **Beachten:** Nicht für Ehegatten/Partner und Kinder mit Kinderabzug oder abgezogenen Unterhaltsbeiträgen
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'700 (Unterstützungsabzug CHF 2'700 je erwerbsunfähige/unterstützungsbedürftige Person, für deren Unterhalt der Steuerpflichtige zur Hauptsache aufkommt (nicht für Ehegatten und Kinder mit Kinderabzug).)** · Bund **CHF 6'800 (Unterstützungsabzug pro erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mindestens in Höhe des Abzugs unterstützt; nicht für Ehegatten und Kinder mit Kinderabzug)**
- **Bund:** Bund Fr. 6'800 (Kanton Fr. 2'700).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «25.2 für jede unterstützte Person   Fr. 2 700   Fr. 6800   386»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0006.md) `tg-stp-36-1__c0006` – «Für jede unterstützte Person | Fr. 2’700 | Fr. 2’700»
  - [WL TG 2025 S. 24–25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0114.md) `tg-wl-2025__c0114` – «dürftigen Person auf, können Sie kantonal Fr. 2 700 abziehen.»
  - [StV TG § 12](../../chunks/tg/2025/tg-stv/tg-stv__par-12.md) `tg-stv__par-12` – «sofern er zu mehr als 50 Prozent des betreibungsrechtlichen Existenzminimums zum Unterhalt beiträgt»
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0004.md) `tg-form-01-2025__c0004` – «die Sie mit einem jährlichen Beitrag von mindestens Fr. 12 000.– (Kanton) bzw. Fr. 6 800.– (Bund) unterstützen»
  - [WL TG 2025 S. 24–25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0115.md) `tg-wl-2025__c0115` – «Die Unterstützungsbedürftigkeit ist durch eine Bestätigung der Wohnsitzgemeinde (Steuerausweis»
  - [WL TG 2025 S. 24–25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0115.md) `tg-wl-2025__c0115` – «an deren Unterhalt Sie nachgewiesenermassen mindestens»
  - [WL TG 2025 S. 24–25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0115.md) `tg-wl-2025__c0115` – «in eingetragener Partnerschaft sowie Kinder, für die gemäss Ziffer 25.1 der Steuererklärung ein»

<a id="25-3-sozialabzug-alter-iv"></a>
### Ziff. 25.3 – Abzug für Personen mit AHV-Altersrenten sowie erwerbsunfähige oder verwitwete Personen (Code 388; nur Staat)

- **Schlüssel:** `sozialabzug.alter_iv` (Abzug für Personen im AHV-Alter, erwerbsunfähig oder verwitwet (kantonal)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Reineinkommen Ziff. 24 (Staat); Rentenbescheinigung AHV/IV
- **Rein:** Formular 1 S. 1 → Zivilstand (alleinstehend / gemeinsam besteuert) · AHV-Rentenbescheinigung bzw. Nachweis Erwerbsunfähigkeit/Verwitwung → Anspruch
- **Rechnen:** Kanton: max(0; 4'200 − 200 × volle Fr. 1'000 über Fr. 16'900 [gemeinsam Fr. 24'300]) auf Ziff. 24 / Bund: kein Abzug → Code 388
- **Regel:** Nur Staats-/Gemeindesteuer: max. Fr. 4'200, abnehmend nach satzbestimmendem Reineinkommen Ziff. 24 (Alleinstehende voll bis Fr. 17'899, Ehepaare bis Fr. 25'299; je volle Fr. 1'000 Mehreinkommen Reduktion um Fr. 200; kein Abzug ab Fr. 37'900 bzw. Fr. 45'300). Tabelle in der Wegleitung (S. 25).
- **Beachten:** Anspruch: AHV-Altersrente, erwerbsunfähig (Gesundheit) oder verwitwet; nur Staats- und Gemeindesteuer
- **Beachten:** Voller Abzug bis 17'899 / 25'299; kein Abzug ab 37'900 / 45'300 (Tabelle WL S. 25)
- **Beachten:** WL-Tabelle Zeile «36'900–37'689» (so auch im Original-PDF) vermutlich Druckfehler – Formel § 1 Ziff. 3 VAKP anwenden
- **Limiten:**
  - Abzug AHV-Alter/erwerbsunfähig/verwitwet (CHF): Kanton **CHF 4'200 (Abzug für Steuerpflichtige im AHV-Alter, erwerbsunfähige oder verwitwete: max. CHF 4'200; ermässigt sich bei Reineinkommen über CHF 16'900 (in ungetrennter Ehe über CHF 24'300) je CHF 1'000 Mehreinkommen um CHF 200. Bund: kein Abzug.)** · Bund **n/a – Kantonaler Schlüssel; Art. 35 DBG kennt nur Kinder-, Unterstützungs- und Verheiratetenabzug.**
- **Bund:** Bund: kein Abzug.
- **Bemerkung:** Wegleitungstabelle: Zeile '36'900–37'689' ist offensichtlich ein Druckfehler für 37'899 (Gesetz/VAKP: Reduktion in 1'000er-Schritten bis 0 bei 37'900 bzw. 45'300); Tabelle vor Anwendung gegen WL S. 25 prüfen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «25.3 für Personen mit AHV-Altersrenten sowie erwerbsunfähige oder verwitwete Personen   388»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0116.md) `tg-wl-2025__c0116` – «bis   17'899   bis   25'299   4'200»
  - [VAKP TG § 1](../../chunks/tg/2025/tg-vakp/tg-vakp__par-1.md) `tg-vakp__par-1` – «beträgt das Reineinkommen mehr als Fr. 16'900, bei Steuerpflichtigen in ungetrennter Ehe mehr als Fr. 24'300, ermässigt sich der Abzug je Fr. 1'000 Mehreinkommen um Fr. 200»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0117.md) `tg-wl-2025__c0117` – «36'900–37'689   44'300–45'299   200»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0117.md) `tg-wl-2025__c0117` – «37'900 u. mehr   45'300 u. mehr   kein Abzug»
  - [VAKP TG § 1](../../chunks/tg/2025/tg-vakp/tg-vakp__par-1.md) `tg-vakp__par-1` – «von im AHV-Alter stehenden, erwerbsunfähigen oder verwitweten Steuerpflichtigen Fr. 4'200»

<a id="25-4-sozialabzug-verheiratete"></a>
### Ziff. 25.4 – Abzug für gemeinsam besteuerte Personen (Code 390; nur Bund Fr. 2'800)

- **Schlüssel:** `sozialabzug.verheiratete` (Verheiratetenabzug (Bund)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Zivilstand)
- **Rein:** Formular 1 S. 1 → Zivilstand verheiratet / eingetragene Partnerschaft (gemeinsame Besteuerung)
- **Rechnen:** Bund: pauschal Fr. 2'800 je gemeinsam besteuertes Paar → Code 390 / Kanton: kein Abzug
- **Regel:** Nur direkte Bundessteuer: Fr. 2'800 für gemeinsam besteuerte Eheleute/Partner; bei Staats- und Gemeindesteuern kein solcher Abzug.
- **Beachten:** Gilt für gemeinsam besteuerte Eheleute und eingetragene Partner/innen; bei Staats- und Gemeindesteuer nicht zulässig
- **Limiten:**
  - Verheiratetenabzug (CHF, Bund): Kanton **n/a – Verheiratetenabzug gibt es nur bei der direkten Bundessteuer (CHF 2'800); kantonal Berücksichtigung über Divisor 2.0 im Tarif (§ 37 Abs. 2 StG).** · Bund **CHF 2'800 (Verheiratetenabzug für Ehepaare in rechtlich und tatsächlich ungetrennter Ehe)**
- **Bund:** Nur Bund: Fr. 2'800; Kanton kein Abzug.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «25.4 für gemeinsam besteuerte Personen   390»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0118.md) `tg-wl-2025__c0118` – «Gemeinsam besteuerten Eheleute bzw. Partnerinnen und Partner einer eingetragenen Partner»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0008.md) `tg-stp-36-1__c0008` – «für gemeinsam steuerpflichtige Personen | Fr. 2’800»

<a id="26-berechnung-total"></a>
### Ziff. 26 – Steuerbares Einkommen (Ziffer 24 abzüglich Ziffern 25.1 bis 25.4) (Code 398)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Sozialabzüge Ziff. 25.1–25.4 (Codes 380–390)
- **Rechnen:** Ziff. 24 − Σ Ziff. 25.1–25.4, je Spalte Staat / Bund → Code 398
- **Regel:** Reineinkommen Ziff. 24 minus Sozialabzüge Ziff. 25.1–25.4, je Spalte Staat/Bund.
- **Beachten:** Kinder-/Unterstützungsabzug: Verhältnisse am 31. Dezember 2025 bzw. Ende Steuerpflicht; sonst kein Abzug (kein pro rata)
- **Beachten:** Unterjährige Steuerpflicht: Sozialabzüge anteilig nach Dauer der Steuerpflicht
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «26.   STEUERBARES EINKOMMEN (Ziffer 24 abzüglich Ziffern 25.1 bis 25.4)   398»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0107.md) `tg-wl-2025__c0107` – «am 31. Dezember 2025 bzw. am Ende der Steuerpflicht massgebend»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0107.md) `tg-wl-2025__c0107` – «kann der Sozialabzug nicht gewährt werden (auch nicht pro rata)»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0107.md) `tg-wl-2025__c0107` – «teilig nach Massgabe der Dauer der Steuerpflicht gewährt»

<a id="28-1-sozialabzug-kinder"></a>
### Ziff. 28.1 – Steuergutschrift Kanton für minderjährige Kinder (Anzahl Kinder)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Anzahl minderjährige Kinder mit Kinderabzug (Formular 1 Seite 1)
- **Rein:** Formular 1 S. 1 Kinder → Anzahl minderjährige Kinder (Jg. 2008 und jünger) mit Kinderabzug
- **Rechnen:** Nur Anzahl eintragen; Gutschrift Kanton max. Fr. 100 × Anzahl, mit der Schlussrechnung, höchstens bis zum Steuerbetrag
- **Regel:** Kein Abzug vom Einkommen, sondern Steuergutschrift mit der Schlussrechnung: max. Fr. 100 je minderjähriges Kind mit Kinderabzug; keine Auszahlung über den Steuerbetrag hinaus. Nur Anzahl eintragen.
- **Beachten:** Nur bei Wohnsitz im Kanton Thurgau und nur für Kinder mit Kinderabzug (Ziff. 25.1)
- **Beachten:** Steuerbetrag < Gutschrift: keine Auszahlung der Differenz
- **Beachten:** Kein Einkommensabzug; Bund separat Ziff. 28.2
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «28.1 Kanton: Steuergutschrift für minderjährige Kinder   Anzahl Kinder»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0118.md) `tg-wl-2025__c0118` – «gutschrift von maximal Fr. 100.»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0118.md) `tg-wl-2025__c0118` – «Steuerpflichtige Personen mit Wohnsitz im Kanton Thurgau erhalten für jedes minderjährige Kind,»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0118.md) `tg-wl-2025__c0118` – «Sofern der Steuerbetrag geringer ist als die Steuergutschrift, erfolgt»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0119.md) `tg-wl-2025__c0119` – «Tragen Sie unter Ziffer 28.1 die Anzahl der Personen ein, für welche Sie die Voraussetzungen für»
  - [WL TG 2025 S. 30](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0139.md) `tg-wl-2025__c0139` – «Vermögen und Erträge von Kindern unter Ihrer elterlichen Sorge (Jahrgang 2008 und jünger)»

<a id="28-2-sozialabzug-kinder"></a>
### Ziff. 28.2 – Bund: Ermässigung Steuerbetrag für Kinder und unterstützungsbedürftige Personen (Anzahl Personen)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Anzahl Kinder/unterstützte Personen im gleichen Haushalt (Elterntarif)
- **Rein:** Formular 1 S. 1 Kinder / unterstützte Personen → «In Ihrem Haushalt? ja», Unterhalt zur Hauptsache
- **Rechnen:** Nur Anzahl eintragen; Bund: Steuerbetrag − Fr. 263 × Anzahl Kinder bzw. unterstützte Personen (Elterntarif)
- **Regel:** Kein Einkommensabzug: Abzug vom Steuerbetrag Fr. 263 pro Kind bzw. unterstützte Person (Elterntarif), für Personen, die mit Kindern/unterstützungsbedürftigen Personen im gleichen Haushalt leben und deren Unterhalt zur Hauptsache bestreiten. Nur Anzahl eintragen.
- **Beachten:** Voraussetzung: mit (eigenen) Kindern/Unterstützten im gleichen Haushalt und Unterhalt zur Hauptsache bestritten
- **Beachten:** Tarifarische Massnahme (Elterntarif), kein Sozialabzug
- **Limiten:**
  - Abzug vom Steuerbetrag pro Kind (CHF, Bund): Kanton **n/a – Ermässigung vom Steuerbetrag (Elterntarif, CHF 263 pro Kind) nur bei der direkten Bundessteuer; kantonal Elterntarif über Divisor 2.0 (§ 37 Abs. 2 StG).** · Bund **CHF 263 (Ermässigung des Steuerbetrags pro Kind bzw. unterstützungsbedürftige Person (Elterntarif: Ehepaare und Alleinstehende mit Kindern im gleichen Haushalt))**
- **Bund:** Nur Bund: Fr. 263 pro Kind/unterstützte Person vom Steuerbetrag.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «28.2 Bund: Ermässigung Steuerbetrag für Kinder und unterstützungsbedürftige Personen   Anzahl Personen»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0119.md) `tg-wl-2025__c0119` – «Fr. 263 pro Kind und/oder pro unterstützte Person vom Steuerbetrag geltend machen.»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0007.md) `tg-stp-36-1__c0007` – «Ermässigung Steuerbetrag pro Kind\* | Fr. 263 | Fr. 259»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0119.md) `tg-wl-2025__c0119` – «Personen, welche mit (eigenen) Kindern oder mit unterstützungsbedürftigen Personen im gleichen»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0119.md) `tg-wl-2025__c0119` – «Haushalt zusammenleben und deren Unterhalt zur Hauptsache bestreiten, haben Anspruch auf den»
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0003.md) `tg-form-01-2025__c0003` – «Geburtsdatum   Haushalt?   Ausbildungsende (wenn in Ausbildung)»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0007.md) `tg-stp-36-1__c0007` – «Bei der Ermässigung vom Steuerbetrag handelt es sich nicht um einen Sozialabzug, sondern um eine tarifarische Massnahme»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben (Formular 2, Code 410)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 Ziff. 9 Total Steuerwert (Code 410); Bank-/Postauszüge per 31.12.2025
- **Rein:** Formular 2 Ziff. 9 → Total Steuerwert Privatvermögen (Code 410) · Steuerauszug Bank/Depot → Steuerwert je Konto/Titel per 31.12.2025 · Kursliste ESTV → Kurs Ende Dezember 2025 (kotierte Titel)
- **Rechnen:** Formular 2: Zwischentotal Steuerwerte − Geschäftswertschriften = Ziff. 9 Total Steuerwert Privatvermögen → Code 410
- **Regel:** Steuerwert per 31.12.2025 (kotiert: Börsenkurs Ende Dezember bzw. Kursliste ESTV; nicht kotiert: Verkehrswert). Ansprüche gegen PK, Freizügigkeitskonten und Säule 3a bis zur Fälligkeit steuerfrei – nicht deklarieren. Vermögen und Erträge von Kindern unter elterlicher Sorge (Jahrgang 2008 und jünger) mitdeklarieren.
- **Beachten:** PK-, Freizügigkeits- und Säule-3a-Guthaben bis Fälligkeit steuerfrei – nicht aufführen
- **Beachten:** Vermögen von Kindern Jg. 2008 und jünger mitdeklarieren; Jg. 2007 und älter versteuern selbst
- **Beachten:** Nicht kotierte Titel: Verkehrswert 31. Dezember 2025, ersatzweise Wert per 1. Januar 2025
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «30.1 Wertschriften und Guthaben   Formular 2 410»
  - [WL TG 2025 S. 30–31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0143.md) `tg-wl-2025__c0143` – «Für in der Schweiz kotierte Wertpapiere gilt der Börsenkurs Ende des Monats Dezember 2025.»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0163.md) `tg-wl-2025__c0163` – «Steuerwerte von Wertschriften und Guthaben im Privatvermögen übertragen Sie in Ziffer 30.1 auf»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0163.md) `tg-wl-2025__c0163` – «Ziffer 6 erfassten Steuerwerte der Geschäftswertschriften abziehen.»
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0006.md) `tg-form-02-2025__c0006` – «Total in Ziffer 9 zu übertragen»
  - [WL TG 2025 S. 30–31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0144.md) `tg-wl-2025__c0144` – «genössischen Steuerverwaltung (EStV) entnehmen.»
  - [WL TG 2025 S. 30](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0139.md) `tg-wl-2025__c0139` – «sind bis zur Fälligkeit der Leistungen steuerfrei und daher vor deren Fälligkeit»
  - [WL TG 2025 S. 30](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0139.md) `tg-wl-2025__c0139` – «Vermögen und Erträge von Kindern unter Ihrer elterlichen Sorge (Jahrgang 2008 und jünger)»
  - [WL TG 2025 S. 30](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0139.md) `tg-wl-2025__c0139` – «mögen und Erträge von Personen mit Jahrgang 2007 und älter sind durch diese selbst zu versteuern»
  - [WL TG 2025 S. 30–31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0144.md) `tg-wl-2025__c0144` – «Für nicht kotierte Wertpapiere gilt der Verkehrswert per 31. Dezember 2025.»
  - [WL TG 2025 S. 30–31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0144.md) `tg-wl-2025__c0144` – «kannt, können Sie ersatzweise den Wert per 1. Januar 2025 eintragen.»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 412)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bestandesaufnahme per 31.12.2025; Kursliste ESTV
- **Rein:** Kassenbestand per 31.12.2025 → inländisches Bargeld · Amtliche Kursliste ESTV → Devisen-/Edelmetallkurse per 31.12.2025
- **Rechnen:** CHF-Bargeld zum Bestand + Fremdwährungen, Gold, Edelmetalle zum Verkehrswert per 31. Dezember 2025 → Code 412
- **Regel:** Inländisches Bargeld mit Bestand; ausländisches Bargeld, Gold und Edelmetalle zum Verkehrswert per 31.12.2025 (amtliche Kursliste).
- **Beachten:** Massgebliche Werte aus der amtlichen Kursliste der ESTV
- **Beachten:** Bank-/Postguthaben gehören ins Formular 2 (Ziff. 30.1), nicht hierher
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «30.2 Bargeld, Gold und andere Edelmetalle   412»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0122.md) `tg-wl-2025__c0122` – «Inländisches Bargeld ist mit dem Bestand per 31. Dezember 2025 aufzuführen.»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0122.md) `tg-wl-2025__c0122` – «Die massgeblichen Werte können der amtlichen Kursliste entnommen werden»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0122.md) `tg-wl-2025__c0122` – «Bargeld, Gold und andere Edelmetalle sind zum Verkehrswert per 31. Dezember 2025 einzuset-»
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «30.1 Wertschriften und Guthaben   Formular 2 410»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen, Rückkaufswert inkl. Überschussguthaben (Code 420)

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Steuerwertbescheinigung des Versicherers per 31.12.2025
- **Rein:** Steuerwertbescheinigung des Versicherers per 31.12.2025 → Rückkaufswert inkl. Überschussguthaben · Police → Gesellschaft, Abschluss-/Ablaufjahr, Versicherungssumme
- **Rechnen:** Σ je Police Rückkaufswert + Überschuss-/Gewinnanteile per 31. Dezember 2025 → Code 420
- **Regel:** Steuerwert = Rückkaufswert inkl. Überschuss-/Gewinnanteile; auch Rentenversicherungen während der Rentenlaufzeit. Pro Police Gesellschaft, Abschluss-/Ablaufjahr, Versicherungssumme und Steuerwert erfassen; Bescheinigung beilegen.
- **Beachten:** Rentenversicherungen auch während der Rentenlaufzeit steuerbar
- **Beachten:** Bescheinigungen der Versicherer der Steuererklärung beilegen
- **Beachten:** Nicht fällige Säule-3a-Ansprüche sind vermögenssteuerfrei – nicht hier deklarieren
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «Total Steuerwert Lebens- und Rentenversicherungen   420»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0122.md) `tg-wl-2025__c0122` – «Kapital- und Rentenversicherungen unterliegen mit ihrem Steuerwert (Rückkaufswert inkl. Über»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0120.md) `tg-wl-2025__c0120` – «aus anerkannten Formen der gebundenen Selbstvorsorge (Säule 3a).»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge (Marke, Kaufpreis, Anschaffungsjahr) (Code 422)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Fahrzeugausweis/Kaufvertrag (Kaufpreis, Anschaffungsjahr)
- **Rein:** Kaufvertrag / Fahrzeugausweis → Marke, Kaufpreis, Anschaffungsjahr
- **Rechnen:** Kaufpreis − 20 % des Kaufpreises × Jahre seit Erwerb; Kauf vor mehr als 5 Jahren: Fr. 1 pro memoria → Code 422
- **Regel:** Verkehrswert per 31.12.2025: Kaufpreis abzüglich 20% pro Jahr seit Erwerb; vor mehr als 5 Jahren gekaufte Fahrzeuge pro memoria Fr. 1.–. Geleaste Fahrzeuge nicht deklarieren. Oldtimer/Liebhaberfahrzeuge zum Verkehrswert unter Ziff. 30.6.
- **Beachten:** Geleaste Fahrzeuge nicht deklarieren
- **Beachten:** Oldtimer und Liebhaberfahrzeuge zum Verkehrswert unter Ziff. 30.6
- **Beachten:** Geschäftsfahrzeuge (Selbständige) unter Ziff. 32.5 Anlagevermögen
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «Total Steuerwert der Motorfahrzeuge   422»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0123.md) `tg-wl-2025__c0123` – «Für die Ermittlung des Verkehrswerts kann pro Jahr seit Erwerb eine Wertvermin»
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «32.5 Anlagevermögen ohne Grundeigentum (Fahrzeuge, Maschinen/Mobiliar usw.)»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Anteile an unverteilten Erbschaften (Formular 3) (Code 424)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Inventar/Aufstellung der Erbengemeinschaft
- **Rein:** Formular 3 / Aufstellung der Erbengemeinschaft → Nachlassvermögen per 31.12.2025 · Erbschaftsunterlagen → eigene Erbquote
- **Rechnen:** Vermögen der unverteilten Erbschaft × eigene Erbquote → Code 424; Ertragsanteil → Ziff. 5.3
- **Regel:** Anteil am Vermögen nach Erbquote; Ertragsanteil in Ziff. 5.3. Bei Erbanfall ≥ Fr. 50'000 während der Steuerperiode wird das hinzugekommene Vermögen ab Erbanfall (nicht für das ganze Jahr) besteuert.
- **Beachten:** Steuerpflicht für den Anteil ab Folgetag des Todestags der erblassenden Person
- **Beachten:** Erbanfall ab Fr. 50'000: Vermögen erst ab Erbanfall besteuert (nicht bei Schenkung/Erbvorbezug)
- **Beachten:** Vermögensanfall zusätzlich auf S. 4 unten (Schenkungen/Erbschaften) aufführen
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «30.5 Anteile an unverteilten Erbschaften   Formular 3 424»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0123.md) `tg-wl-2025__c0123` – «Die Anteile an unverteilten Erbschaften und Nutzniessungen werden den einzelnen erbenden oder»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0082.md) `tg-wl-2025__c0082` – «Einkünfte aus unverteilten Erbschaften werden den erbenden Personen entsprechend ihrer»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0082.md) `tg-wl-2025__c0082` – «schaft bereits ab dem Folgetag des Todestags der Erblasserin/des Erblassers beginnt.»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0130.md) `tg-wl-2025__c0130` – «Bei Vermögensanfall aus Erbschaft (nicht jedoch infolge Schenkung oder Erbvorbezug) von min-»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0130.md) `tg-wl-2025__c0130` – «destens Fr. 50'000 während der Steuerperiode wird das hinzugekommene Vermögen vom Zeit-»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0129.md) `tg-wl-2025__c0129` – «Bitte führen Sie hier auch Vermögensanfälle aus Erbschaften auf.»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte, nähere Bezeichnung (Code 426)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung zum Verkehrswert per 31.12.2025
- **Rein:** Kaufbelege / Schätzungen → Verkehrswert je Objekt per 31.12.2025
- **Rechnen:** Σ Verkehrswerte per 31.12. je Objekt, mit näherer Bezeichnung → Code 426
- **Regel:** Wohnwagen, Wohnmobile, Oldtimer, Boote, Flugzeuge, Reitpferde, Kunst/Schmuck, Sammlungen, immaterielle Güter: genau bezeichnen, Verkehrswert per 31.12. Hausrat ist steuerfrei.
- **Beachten:** Hausrat ist von der Vermögenssteuer befreit
- **Beachten:** Z.B. Wohnwagen, Wohnmobile, Oldtimer, Boote, Flugzeuge, Reitpferde, Kunst, Schmuck, Sammlungen, Patente
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «30.6 Übrige Vermögenswerte, nähere Bezeichnung:   426»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0123.md) `tg-wl-2025__c0123` – «Unter die übrigen Vermögenswerte fallen z.B. Wohnwagen, Wohnmobile, Oldtimer, Liebhaberfahr»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0120.md) `tg-wl-2025__c0120` – «Der Hausrat ist von der Vermögenssteuer befreit.»

<a id="31-vermoegen-liegenschaften"></a>
### Ziff. 31 – Liegenschaften (Formular 7, Code 430)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Formular 7 Total Steuerwerte (Code 430); Liegenschaftensteuerrechnung / amtliche Schätzung
- **Rein:** Formular 7 → Total Steuerwerte (Code 430) · Liegenschaftensteuerrechnung (Versand Januar 2026) → amtlicher Verkehrswert TG · Steuerwert-Angabe anderer Kanton/Ausland → dortiger Steuerwert
- **Rechnen:** Σ Steuerwerte je Liegenschaft/Anteil (Formular 7): nichtlandwirtschaftlich rechtskräftiger amtlicher Verkehrswert, landwirtschaftlich Ertragswert → Code 430
- **Regel:** Rechtskräftiger amtlicher Verkehrswert am Ende der Steuerperiode (landwirtschaftliche Liegenschaften: Ertragswert). Ausserkantonale/ausländische Liegenschaften zum dortigen Steuerwert; Anpassung (Repartitionswert) durch die Veranlagungsbehörde. Unfertige Bauten: noch nicht geschätzte Investitionen angemessen berücksichtigen.
- **Beachten:** Ausserkantonal/Ausland: dortigen Steuerwert deklarieren; Repartition durch Veranlagungsbehörde
- **Beachten:** Am Stichtag unfertige Bauten/Umbauten: noch nicht geschätzte Investitionen angemessen dazurechnen
- **Beachten:** Geschäftsliegenschaften hier deklarieren, im Geschäftsvermögen Ziff. 32 ausklammern
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «31.   Liegenschaften   Formular 7 430»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0239.md) `tg-wl-2025__c0239` – «Für nichtlandwirtschaftliche Liegenschaften geben Sie den am Ende der Steuerperiode bzw. der»
  - [Formular 7 TG 2025 S. 1](../../chunks/tg/2025/tg-form-07-2025/tg-form-07-2025__c0003.md) `tg-form-07-2025__c0003` – «Total Steuerwerte   430»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0125.md) `tg-wl-2025__c0125` – «Im Übrigen sind die unter Ziffer 31 aufgeführten»

<a id="32-1-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.1 – Geschäftskapital in Kollektiv- und Kommanditgesellschaft (Code 440)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bescheinigung der Gesellschaft über den Vermögensanteil
- **Rein:** Bescheinigung der Gesellschaft → Anteil am Gesellschaftsvermögen · Bilanz mit Beteiligungsrechten bzw. separates Blatt → Aktiven, Passiven, Erträge, Schuldzinsen
- **Rechnen:** Eigener Anteil am Vermögen der Kollektiv-/Kommanditgesellschaft gemäss Bescheinigung → Code 440
- **Regel:** Anteil am Vermögen der Gesellschaft gemäss Bescheinigung der Gesellschaft; die Gesellschaft wird nicht als Einheit besteuert.
- **Beachten:** Bescheinigung der Gesellschaft beilegen; Einkommensanteil unter Ziff. 2 (WL S. 12)
- **Beachten:** Ohne Bilanz: Details zu Aktiven, Passiven, Erträgen und Schuldzinsen auf separatem Blatt
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «32.1 Geschäftskapital in Kollektiv- und Kommanditgesellschaft   440»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0124.md) `tg-wl-2025__c0124` – «Kollektiv- und Kommanditgesellschaften werden nicht als Einheit besteuert.»

<a id="32-2-32-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.2–32.5 – Betriebsvermögen Einzelfirma: Bankkonti/Wertschriften/Guthaben, Vorräte, Viehhabe, Anlagevermögen ohne Grundeigentum

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz bzw. unterzeichnete Aufstellung Aktiven/Passiven
- **Rein:** Unterzeichnete Bilanz inkl. Erfolgsrechnung → Aktiven per Abschluss · Alternativ unterzeichnete Aufstellung Aktiven/Passiven und Erträge/Aufwendungen · Viehhabe → Versicherungswert im Formular angeben
- **Rechnen:** 32.2 Bank/Wertschriften (bilanzierter Wert) + Debitoren (voll) | 32.3 min(Anschaffungs-/Herstellkosten; Marktpreis) | 32.5 Verkehrswert
- **Regel:** Wertschriften zum bilanzierten Wert; Debitoren mit vollen Forderungsbeträgen; Vorräte zu Anschaffungs-/Herstellungskosten oder tieferem Marktpreis; Anlagevermögen zum Verkehrswert. Liegenschaften in Ziff. 31 (nicht hier). Unterzeichnete Bilanz/Erfolgsrechnung beilegen.
- **Beachten:** Geschäftsliegenschaften ausklammern → Ziff. 31
- **Beachten:** Präponderanz: Objekte zu mehr als 50 % geschäftlich genutzt gehören ganz ins Geschäftsvermögen
- **Beachten:** Anlagen: Anschaffungswert − angemessene Abschreibung; unsichere Debitoren nur bei glaubhaftem Verlust kürzen
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «32.5 Anlagevermögen ohne Grundeigentum (Fahrzeuge, Maschinen/Mobiliar usw.)»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0125.md) `tg-wl-2025__c0125` – «Setzen Sie das Anlagevermögen wie Maschinen, Werkzeuge, Mobilien oder Fahrzeuge mit dem»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0121.md) `tg-wl-2025__c0121` – «überwiegend (mehr als 50%) der selbständigen Erwerbstä-»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0121.md) `tg-wl-2025__c0121` – «tigkeit dienen, sind vollumfänglich dem Geschäftsvermögen zuzuweisen.»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0126.md) `tg-wl-2025__c0126` – «Der Verkehrswert entspricht dem Anschaffungswert unter Vornahme eines»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0126.md) `tg-wl-2025__c0126` – «Legen Sie der Steuererklärung eine unterzeichnete Bilanz (inklusive der Erfolgsrechnung) oder»

<a id="32-6-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.6 – Total Geschäftsvermögen (Ziffern 32.2 bis 32.5) oder lt. Bilanz (Code 442)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Rechenzeile / Bilanz
- **Rein:** Übertrag Ziff. 32.2–32.5 · oder Bilanz → Total Geschäftsvermögen
- **Rechnen:** Σ Ziff. 32.2–32.5 oder Total gemäss Bilanz (ohne Liegenschaften Ziff. 31) → Code 442
- **Regel:** Summe 32.2–32.5 oder Eigenkapital gemäss Bilanz. Die Steuerverwaltung meldet das arbeitende Eigenkapital der Ausgleichskasse.
- **Beachten:** Geschäftsschulden nicht hier abziehen: Formular 4.1 B (Code 460) → Total Code 466 → Ziff. 34
- **Beachten:** Arbeitendes Eigenkapital meldet die Steuerverwaltung der Ausgleichskasse
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «32.6 Total Geschäftsvermögen (Ziffern 32.2 bis 32.5) oder lt. Bilanz   Fr.   442»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0125.md) `tg-wl-2025__c0125` – «Im Übrigen sind die unter Ziffer 31 aufgeführten»
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0002.md) `tg-form-04-1-2025__c0002` – «Übertrag Total Geschäftsschulden aus B   460   288»
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0002.md) `tg-form-04-1-2025__c0002` – «Total Privat- und Geschäftsschulden   466   290»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0121.md) `tg-wl-2025__c0121` – «Die Steuerverwaltung Thurgau hat das gesamte im Geschäftsbetrieb arbeitende Eigenkapital ent-»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Ziffern 30.1 bis 32.6) (Code 464)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 30.1–30.6 (Codes 410, 412, 420, 422, 424, 426) · Übertrag Ziff. 31 (Code 430), 32.1 (Code 440), 32.6 (Code 442)
- **Rechnen:** Σ Codes 410 + 412 + 420 + 422 + 424 + 426 + 430 + 440 + 442 → Code 464 (nur Spalte Staat)
- **Regel:** Summe Ziff. 30.1 bis 32.6 (nur Staats- und Gemeindesteuer; das Vermögen wird nur kantonal besteuert).
- **Beachten:** Vermögen wird nur kantonal besteuert (Bund: keine Vermögenssteuer)
- **Beachten:** Stichtag 31. Dezember 2025 bzw. Ende Steuerpflicht; inkl. Vermögen der Kinder unter elterlicher Sorge
- **Beachten:** Steuerfrei: Hausrat, Anwartschaften 2. Säule, nicht fällige Säule 3a
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «33.   Total der Vermögenswerte (Ziffern 30.1 bis 32.6)   464»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0120.md) `tg-wl-2025__c0120` – «Das Vermögen wird nur kantonal besteuert.»
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «30.6 Übrige Vermögenswerte, nähere Bezeichnung:   426»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0120.md) `tg-wl-2025__c0120` – «Vermögensstand am 31. Dezember 2025 bzw. am Ende der Steuerpflicht.»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0120.md) `tg-wl-2025__c0120` – «gen beider Personen) und der Kinder unter ihrer elterlichen Sorge.»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0120.md) `tg-wl-2025__c0120` – «Der Hausrat ist von der Vermögenssteuer befreit.»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0120.md) `tg-wl-2025__c0120` – «sprüche gegenüber Einrichtungen der beruflichen Vorsorge (2. Säule) oder nicht fällige Ansprüche»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0120.md) `tg-wl-2025__c0120` – «aus anerkannten Formen der gebundenen Selbstvorsorge (Säule 3a).»

<a id="34-schulden-privat"></a>
### Ziff. 34 – Schulden (Formular 4.1, Code 466)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Leasingvertrag Fahrzeug / Leasingraten-Abrechnung → Formular 4.1 Ziff. C Total Privat- und Geschäftsschulden (Code 466); Bank-/Gläubigerbestätigungen per 31.12.2025
- **Rein:** Formular 4.1 C → Total Privat- und Geschäftsschulden per 31.12.2025 (Code 466) · Bank-/Hypothekarbestätigung per 31.12.2025 → Schuld, Zinssatz, fällige Zinsen · Darlehens-/Kreditverträge → Gläubiger mit genauer Adresse
- **Rechnen:** Privatschulden (Code 455) + Geschäftsschulden (Code 460) = Code 466 → Ziff. 34; Schuldzinsen Code 290 → Ziff. 11
- **Regel:** Schuldenverzeichnis mit Gläubiger (genaue Adresse), Zinssatz, Schuld am 31.12. und fälligen Schuldzinsen. Rentenverpflichtungen mit Barwert, wenn gegen Entgelt zugesichert. Totale: Schulden → Ziff. 34, Schuldzinsen → Ziff. 11.
- **Beachten:** Gläubiger mit genauer Adresse und Zinssatz sind unerlässlich
- **Beachten:** Nicht allein haftende Schulden nur soweit selbst zu tragen; Rentenverpflichtungen gegen Entgelt zum Barwert
- **Beachten:** Zinsen: nur im Jahr 2025 fällig gewordene Schuldzinsen (keine Ratazinsen)
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «34.   Schulden   Formular 4.1 466»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0127.md) `tg-wl-2025__c0127` – «Deklarieren Sie Schulden, füllen Sie das Formular 4.1»
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0002.md) `tg-form-04-1-2025__c0002` – «Übertrag Total Privatschulden aus A   455   286»
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0002.md) `tg-form-04-1-2025__c0002` – «Übertrag Total Geschäftsschulden aus B   460   288»
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0002.md) `tg-form-04-1-2025__c0002` – «Total Privat- und Geschäftsschulden   466   290»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0171.md) `tg-wl-2025__c0171` – «Unerlässlich ist insbesondere die Angabe der Gläubigerin bzw. des Gläubigers»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0171.md) `tg-wl-2025__c0171` – «mit genauer Adresse sowie des Zinssatzes.»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0171.md) `tg-wl-2025__c0171` – «Übertragen Sie das Total der Schuldzinsen in Ziffer 11 auf Seite 3, und das»
  - [StG TG § 49](../../chunks/tg/2025/tg-stg/tg-stg__par-49.md) `tg-stg__par-49` – «andere Schulden nur insoweit, als der Steuerpflichtige hiefür aufkommen muss»
  - [StG TG § 49](../../chunks/tg/2025/tg-stg/tg-stg__par-49.md) `tg-stg__par-49` – «Rentenverpflichtungen werden mit dem jeweiligen Barwert der Rente als Schuld berücksichtigt, wenn die Rente gegen Entgelt zugesichert wurde.»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0172.md) `tg-wl-2025__c0172` – «Tragen Sie nur die im Jahre 2025 fällig gewordenen Schuldzinsen ein (keine Ratazinsen).»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Reinvermögen (Ziffer 33 abzüglich Ziffer 34) (Code 468)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 33 (Code 464) · Übertrag Ziff. 34 (Code 466)
- **Rechnen:** Ziff. 33 − Ziff. 34 → Code 468 (nur Spalte Staat)
- **Regel:** Ziff. 33 minus Ziff. 34.
- **Beachten:** Danach Freibeträge Ziff. 36: gemeinsam Fr. 200'000, übrige Fr. 100'000, je Kind (Jg. 2008 und jünger) Fr. 100'000
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 200'000 (Steuerfreier Betrag auf dem Reinvermögen für Steuerpflichtige in ungetrennter Ehe: CHF 200'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 100'000 (Steuerfreier Betrag auf dem Reinvermögen für übrige (nicht in ungetrennter Ehe lebende) Steuerpflichtige: CHF 100'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 100'000 (Zusätzlich CHF 100'000 für jedes nicht selbständig besteuerte Kind.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «35.   Reinvermögen (Ziffer 33 abzüglich Ziffer 34)   468»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0128.md) `tg-wl-2025__c0128` – «gemeinsam besteuerte Personen   Fr. 200'000»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0128.md) `tg-wl-2025__c0128` – «ledige, getrenntlebende, geschiedene oder verwitwete Personen   Fr. 100'000»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0128.md) `tg-wl-2025__c0128` – «für jedes nicht selbständig besteuerte Kind (Jahrgang 2008 und jünger)   Fr. 100'000»

<a id="36-1-vermoegen-sozialabzug"></a>
### Ziff. 36.1 – Steuerfreier Abzug für gemeinsam besteuerte Personen Fr. 200'000 (Code 470)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand (Stichtag 31.12.2025)
- **Rein:** Formular 1 Seite 1 Personalien → Zivilstand am 31.12.2025 bzw. Ende Steuerpflicht (Ehe oder eingetragene Partnerschaft, gemeinsam besteuert)
- **Rechnen:** Fix Fr. 200'000 je gemeinsam besteuertes Paar (anstelle 36.2); Stichtag 31. Dezember 2025 bzw. Ende der Steuerpflicht
- **Regel:** Fr. 200'000 für gemeinsam besteuerte Personen (Stichtag 31.12.2025 bzw. Ende der Steuerpflicht).
- **Beachten:** Nur Staats-/Gemeindesteuer: Vermögen wird nur kantonal besteuert (kein Bund)
- **Beachten:** Getrenntlebende Ehegatten nicht hier, sondern 36.2
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 200'000 (Steuerfreier Betrag auf dem Reinvermögen für Steuerpflichtige in ungetrennter Ehe: CHF 200'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0016.md) `tg-form-01-2025__c0016` – «36.1 Abzug für gemeinsam besteuerte Personen (Eheleute / Partnerinnen oder Partner)   Fr. 200000   470»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0128.md) `tg-wl-2025__c0128` – «– gemeinsam besteuerte Personen   Fr. 200'000»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0120.md) `tg-wl-2025__c0120` – «Das Vermögen wird nur kantonal besteuert.»
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0002.md) `tg-form-01-2025__c0002` – «Personalien, Berufs- und Familienverhältnisse am 31. Dezember 2025 oder am Ende der Steuerpflicht»

<a id="36-2-vermoegen-sozialabzug"></a>
### Ziff. 36.2 – Steuerfreier Abzug für alleinstehende Personen Fr. 100'000 (Code 472)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand (Stichtag 31.12.2025)
- **Rein:** Formular 1 Seite 1 Personalien → Zivilstand am 31.12.2025 bzw. Ende Steuerpflicht (ledig, getrenntlebend, geschieden, verwitwet)
- **Rechnen:** Fix Fr. 100'000 je alleinstehende steuerpflichtige Person (anstelle 36.1); Stichtag 31. Dezember 2025 bzw. Ende der Steuerpflicht
- **Regel:** Fr. 100'000 für ledige, getrenntlebende, geschiedene oder verwitwete Personen.
- **Beachten:** Nur Staats-/Gemeindesteuer: Vermögen wird nur kantonal besteuert (kein Bund)
- **Beachten:** Getrenntlebende Ehegatten: je Person hier (nicht 36.1)
- **Beachten:** Jg. 2007: 2025 erstmals selbständig deklarationspflichtig (eigene Steuererklärung)
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 100'000 (Steuerfreier Betrag auf dem Reinvermögen für übrige (nicht in ungetrennter Ehe lebende) Steuerpflichtige: CHF 100'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0016.md) `tg-form-01-2025__c0016` – «36.2 Abzug für alleinstehende Personen   Fr. 100000   472»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0128.md) `tg-wl-2025__c0128` – «– ledige, getrenntlebende, geschiedene oder verwitwete Personen   Fr. 100'000»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0120.md) `tg-wl-2025__c0120` – «Das Vermögen wird nur kantonal besteuert.»
  - [WL TG 2025 S. 6](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0013.md) `tg-wl-2025__c0013` – «Personen mit Jahrgang 2007 sind somit für die Steuerperiode 2025 erstmals selbständig deklarationspflichtig»
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0002.md) `tg-form-01-2025__c0002` – «Personalien, Berufs- und Familienverhältnisse am 31. Dezember 2025 oder am Ende der Steuerpflicht»

<a id="36-3-vermoegen-sozialabzug"></a>
### Ziff. 36.3 – Steuerfreier Abzug für jedes nicht selbständig besteuerte Kind, Jahrgang 2008 und jünger, Fr. 100'000 (Code 474)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1 (Kinder: Geburtsdatum)
- **Rein:** Formular 1 Seite 1 Kinder → Geburtsdatum (Jg. 2008 und jünger) · Formular 1 Seite 1 Kinder (nur getrennt besteuerte Eltern) → Unterhaltsbeiträge, gemeinsames Sorgerecht, alternierende Obhut
- **Rechnen:** Anzahl nicht selbständig besteuerter Kinder Jg. 2008 und jünger × Fr. 100'000; getrennte Eltern: beim Elternteil mit Kinderabzug oder hälftig
- **Regel:** Fr. 100'000 pro Kind (Jahrgang 2008 und jünger). Im Mündigkeitsjahr werden Kinder selbständig besteuert – dann kein Freibetrag der Eltern. Bei getrennt besteuerten Eltern erhält ihn der Elternteil mit Kinderabzug; hälftige Teilung nur bei gemeinsamem Sorgerecht, alternierender Obhut und ohne Alimente.
- **Beachten:** Jg. 2007 und älter (Mündigkeitsjahr) versteuern ihr Vermögen selbst → kein Freibetrag bei den Eltern
- **Beachten:** Hälftig nur bei gemeinsamem Sorgerecht + alternierender Obhut + ohne periodische Unterhaltsbeiträge
- **Beachten:** Vermögen/Erträge der Kinder Jg. 2008 und jünger gehören ins Wertschriftenverzeichnis der Eltern
- **Limiten:**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 100'000 (Zusätzlich CHF 100'000 für jedes nicht selbständig besteuerte Kind.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0016.md) `tg-form-01-2025__c0016` – «36.3 Abzug für jedes nicht selbständig besteuerte Kind (Jahrgang 2008 und jüngere)   Fr. 100000   474»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0128.md) `tg-wl-2025__c0128` – «– für jedes nicht selbständig besteuerte Kind (Jahrgang 2008 und jünger)   Fr. 100'000»
  - [WL TG 2025 S. 30](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0139.md) `tg-wl-2025__c0139` – «Ebenfalls zu deklarieren sind Vermögen und Erträge von Kindern unter Ihrer elterlichen Sorge (Jahrgang 2008 und jünger)»
  - [WL TG 2025 S. 30](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0139.md) `tg-wl-2025__c0139` – «mit Jahrgang 2007 und älter sind durch diese selbst zu versteuern»
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0003.md) `tg-form-01-2025__c0003` – «Nur bei getrennt besteuerten Eltern auszufüllen»
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0003.md) `tg-form-01-2025__c0003` – «Leistet der andere Elternteil Unterhaltsbeiträge»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen gesamt (Ziffer 35 abzüglich Ziffern 36.1 bis 36.3) (Code 498)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 35 Reinvermögen (Code 468 = Ziff. 33 abzüglich Ziff. 34) · Übertrag Ziff. 36.1–36.3 (Codes 470, 472, 474)
- **Rechnen:** Ziff. 35 − Σ Ziff. 36.1 bis 36.3 → Code 498
- **Regel:** Ziff. 35 minus Ziff. 36.1–36.3.
- **Beachten:** Vermögensstand am 31. Dezember 2025 bzw. Ende der Steuerpflicht (Wegzug Ausland: per Wegzugsdatum)
- **Beachten:** Nur kantonal besteuert (kein Bund)
- **Beachten:** Erbanfall mind. Fr. 50'000: Zugang erst ab Erbanfall besteuert (nicht Schenkung/Erbvorbezug) → Seite 4 angeben
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0016.md) `tg-form-01-2025__c0016` – «37.   STEUERBARES VERMÖGEN GESAMT (Ziffer 35 abzüglich Ziffern 36.1 bis 36.3)   498»
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «35. Reinvermögen (Ziffer 33 abzüglich Ziffer 34) 468»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0120.md) `tg-wl-2025__c0120` – «Vermögensstand am 31. Dezember 2025 bzw. am Ende der Steuerpflicht.»
  - [WL TG 2025 S. 6](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0014.md) `tg-wl-2025__c0014` – «Das Vermögen ist mit dem Stand per Datum des Wegzugs anzugeben.»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0130.md) `tg-wl-2025__c0130` – «Bei Vermögensanfall aus Erbschaft (nicht jedoch infolge Schenkung oder Erbvorbezug)»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0130.md) `tg-wl-2025__c0130` – «Fr. 50'000 während der Steuerperiode wird das hinzugekommene Vermögen vom»

## Weitere Angaben

<a id="seite-4-schenkungen-info-schenkungen-erbschaften"></a>
### Ziff. Seite 4 Schenkungen – Schenkungen und erbrechtliche Vermögensanfälle (erhalten/ausgerichtet 2025)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Formular 1 Seite 4: Datum, Wert, Name/Adresse/Verwandtschaftsgrad; bei mehreren Hilfsblätter 'jahresunabhängige Formulare'
- **Rein:** Seite 4 ankreuzen: Schenkung / Erbvorbezug / Erbschaft / Beteiligung an Erbengemeinschaft · Schenkungs-/Erbvorbezugsvertrag → Datum, Wert Fr., Geber bzw. Empfänger (Name, Adresse, Verwandtschaftsgrad) · Erbbescheinigung/Erbteilung → Erbanfall 2025 inkl. Anteil an unverteilter Erbschaft · Mehrere Fälle → Hilfsblätter («jahresunabhängige Formulare» bzw. in eFisc2025)
- **Rechnen:** Keine Rechnung: je Fall Datum + Wert Fr. (erhalten / ausgerichtet); Erbanfall mind. Fr. 50'000: Zugang erst ab Erbanfall vermögensbesteuert
- **Regel:** Alle 2025 getätigten oder empfangenen Schenkungen, Erbvorbezüge, Erbschaften und Beteiligungen an Erbengemeinschaften mit Datum, Betrag, Geber/Empfänger (inkl. Adresse) und Verwandtschaftsgrad angeben. Bei Erbanfall ≥ Fr. 50'000 Vermögensgewichtung ab Erbanfall.
- **Beachten:** Unverteilte Erbschaft: Steuerpflicht für Erbanteil ab Folgetag des Todestags (Ertrag Ziff. 5.3, Vermögen Ziff. 30.5)
- **Beachten:** Gewichtung ab Erbanfall gilt nicht für Schenkung oder Erbvorbezug
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0017.md) `tg-form-01-2025__c0017` – «Schenkungen und erbrechtliche Vermögensanfälle»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0129.md) `tg-wl-2025__c0129` – «Führen Sie sämtliche im Jahre 2025 getätigten oder empfangenen Schenkungen und Erbvorbezüge»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0130.md) `tg-wl-2025__c0130` – «Bei Vermögensanfall aus Erbschaft (nicht jedoch infolge Schenkung oder Erbvorbezug)»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0130.md) `tg-wl-2025__c0130` – «Fr. 50'000 während der Steuerperiode wird das hinzugekommene Vermögen vom»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0082.md) `tg-wl-2025__c0082` – «Einkünfte aus unverteilten Erbschaften werden den erbenden Personen entsprechend ihrer»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0082.md) `tg-wl-2025__c0082` – «Dasselbe gilt für das Vermögen (vgl. Ziffer 30.5»

<a id="seite-4-kapitalleistungen-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. Seite 4 Kapitalleistungen – Kapitalleistungen aus Vorsorge 2025 (Auszahlungsdatum, Quelle, Betrag)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung (Formular 563); Seite 4 unten der Steuererklärung
- **Rein:** Bescheinigung Vorsorgeeinrichtung/Versicherung (AHV/IV, Säule 2, Freizügigkeit, Säule 3a, Tod/bleibende Nachteile) → Auszahlungsdatum, Betrag Fr. ohne Rappen, Quelle ankreuzen · Mehrere Kapitalleistungen → Aufstellung beilegen
- **Rechnen:** Kanton: einfache Steuer = Kapitalleistung × 2 % (gemeinsam) bzw. 2,4 % (alleinstehend), × Gesamtsteuerfuss / Bund: 1/5 des ordentlichen Tarifs
- **Regel:** Nicht in Ziff. 5.5, sondern Seite 4 unten: Quelle ankreuzen (AHV/IV, Säule 2, Freizügigkeit, Säule 3a, Kapital bei Tod/bleibenden Nachteilen). Separat zu 100% besteuert zum einheitlichen Satz der einfachen Steuer: 2.0% gemeinsam besteuerte, 2.4% Alleinstehende (mal Steuerfuss). Mehrere Leistungen: Aufstellung einreichen. Genugtuung bleibt steuerfrei.
- **Beachten:** Nicht in Ziff. 5.5 (Kapitalabfindung für wiederkehrende Leistungen), sondern nur Seite 4
- **Beachten:** Immer zu 100 % steuerbar, Satz unabhängig von der Höhe; Genugtuung steuerfrei (§ 26 Ziff. 10 StG)
- **Beachten:** Keine Sozialabzüge (Kanton und Bund); Bund: kein Elterntarif
- **Limiten:**
  - Kapitalleistungen aus Vorsorge – Steuersatz/Tarif (separate Jahressteuer): Kanton **Kapitalleistungen aus Vorsorge gesondert, volle Jahressteuer für das Zuflussjahr. Einfache Steuer 2 % für Verheiratete in ungetrennter Ehe, 2,4 % für die übrigen Steuerpflichtigen. Sozialabzüge nach § 36 nicht gewährt.** · Bund **Kapitalleistungen aus Vorsorge (Art. 22 DBG) und Zahlungen bei Tod/bleibenden Nachteilen werden gesondert besteuert (volle Jahressteuer, Steuerjahr des Zuflusses); Steuer = ein Fünftel der Tarife nach Art. 36 Abs. 1, 2 und 2bis erster Satz DBG (Bruchteil 1/5); keine Sozialabzüge.**
- **Bund:** Bund: 1/5 des ordentlichen Tarifs (Tarif Alleinstehende bzw. Verheiratete); kein Elterntarif.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0018.md) `tg-form-01-2025__c0018` – «Kapitalleistungen aus Vorsorge 2025»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0131.md) `tg-wl-2025__c0131` – «tung, bei gemeinsam besteuerten Personen zu einem einheitlichen Satz von 2% besteuert.»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0131.md) `tg-wl-2025__c0131` – «Bei Alleinstehenden beträgt der einheitliche Satz für die einfache Steuer 2,4%.»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0084.md) `tg-wl-2025__c0084` – «Nicht in Ziffer 5.5, sondern auf der Steuererklärung, Seite 4 unten, sind Kapitalleistungen aus»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0132.md) `tg-wl-2025__c0132` – «Bei der direkten Bundessteuer beträgt die Steuer auf Kapitalleistungen aus Vorsorge 1/5»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0132.md) `tg-wl-2025__c0132` – «Die Genugtuung von Fr. 50 000 bleibt gemäss § 26 Ziffer 10 des Gesetzes»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0132.md) `tg-wl-2025__c0132` – «Der Elterntarif (vgl. Seite 55 der Wegleitung) findet bei Kapitalleistungen aus Vorsorge keine»

<a id="seite-4-selbstanzeige-verfahren-einreichung"></a>
### Ziff. Seite 4 Selbstanzeige – Antrag auf erstmalige straflose Selbstanzeige (Steuerperioden)

- **Schlüssel:** `verfahren.einreichung` (Einreichung, Unterschrift, Beilagen, Fristen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 4: Checkbox + Perioden; unterzeichneter Antrag mit Aufstellung der nicht versteuerten Werte
- **Rein:** Unterzeichneter Antrag mit genauem Sachverhalt → Beilage; Feld Seite 4 ankreuzen + alle nicht verjährten Steuerperioden · Umfassende, vorbehaltlose Aufstellung der unversteuerten Einkommens-/Vermögenswerte + Belege → Beilage
- **Rechnen:** Keine Busse (Kanton und Bund); Nachsteuer max. 10 Jahre nach ordentlicher Veranlagung, inkl. Ausgleichszinsen
- **Regel:** Nur bei erstmaliger Selbstanzeige: Feld ankreuzen und Antrag mit Sachverhalt, umfassender Aufstellung der unversteuerten Einkommens-/Vermögenswerte und Belegen beilegen; Nachsteuer maximal 10 Jahre. Entscheid der Steuerverwaltung (Rechtsdienst) folgt separat.
- **Beachten:** Nur wenn noch nie eine straflose Selbstanzeige erfolgte; sonst Busse ein Fünftel der hinterzogenen Steuer
- **Beachten:** Kumulativ: Hinterziehung keiner Behörde bekannt, vorbehaltlose Mitwirkung, ernstliches Bemühen um Zahlung
- **Beachten:** Rechtsdienst StV entscheidet über Straflosigkeit; Nachsteuerentscheid separat (rechtsmittelfähig)
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0018.md) `tg-form-01-2025__c0018` – «Antrag auf erstmalige straflose Selbstanzeige»
  - [WL TG 2025 S. 29](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0135.md) `tg-wl-2025__c0135` – «Wollen Sie eine erstmalige straflose Selbstanzeige vornehmen, können Sie in der Steuererklärung»
  - [WL TG 2025 S. 29](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0133.md) `tg-wl-2025__c0133` – «steuern als auch der direkten Bundessteuer von einer Büssung abgesehen»
  - [WL TG 2025 S. 29](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0133.md) `tg-wl-2025__c0133` – «maximal für 10 Jahre, wird nach den Vorschriften über die ordentliche»
  - [WL TG 2025 S. 29](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0133.md) `tg-wl-2025__c0133` – «Veranlagung berechnet und inklusive Ausgleichszinsen nachgefordert»
  - [WL TG 2025 S. 29](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0133.md) `tg-wl-2025__c0133` – «die Hinterziehung keiner Behörde bekannt ist»
  - [WL TG 2025 S. 29](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0134.md) `tg-wl-2025__c0134` – «die Busse wird dann auf einem Fünftel der hinterzogenen»
  - [WL TG 2025 S. 29](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0136.md) `tg-wl-2025__c0136` – «Der Rechtsdienst der Steuerverwaltung wird überprüfen, ob die Voraussetzungen für eine»

<a id="seite-4-bemerkungen-unterschrift-verfahren-einreichung"></a>
### Ziff. Seite 4 Bemerkungen/Unterschrift – Bemerkungen, Unterschrift, Einreichung und Fristen

- **Schlüssel:** `verfahren.einreichung` (Einreichung, Unterschrift, Beilagen, Fristen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Formular 1 Seite 4 Bemerkungszeilen/Unterschrift; Einreichungsdatum auf dem Formular; Quittung bei eFisc-Übermittlung
- **Rein:** Immer beilegen: sämtliche Lohnausweise, 3a-Bescheinigungen, Bank-Steuerauszüge (bei Total-Deklaration), Aufstellungen Selbständigerwerbende · Ab Fr. 1'000: Rechnungskopien Liegenschaftsunterhalt, Bestätigungen freiwilliger Zuwendungen · eFisc2025 → unterzeichnete Quittung + leeres Original-Hauptformular 1 an Gemeindesteueramt
- **Rechnen:** Frist = vorgedrucktes Datum; Erstreckung (Deklarationsjahr): 1. Gesuch bis 30. September, weitere begründet bis 30. November; gewerbsm. Treuhänder bis 31. Dezember
- **Regel:** Unterschrift beider Personen (auch bei Vollmacht). Einreichung beim Gemeindesteueramt bis zum aufgedruckten Datum; bei elektronischer Übermittlung gilt die Erklärung erst mit der unterzeichneten Quittung (zusammen mit dem Original-Hauptformular) als eingereicht. Immer beizulegen: sämtliche Lohnausweise, Steuerauszüge, Rechnungen Liegenschaftsunterhalt und Zuwendungsbestätigungen ab Fr. 1'000, 3a-Bescheinigungen. Fristerstreckung: Gesuch an das Gemeindesteueramt; Private erstmals bis 30.9. (Folgegesuch begründet bis 30.11.); gewerbsmässige Treuhänder/Steuerberater für Mandanten bis 31.12. des Deklarationsjahres; Arbeitsüberlastung ist kein Grund.
- **Beachten:** Beide gemeinsam besteuerten Personen unterschreiben persönlich – auch bei Vertretungsvollmacht
- **Beachten:** Angaben ausserhalb der Formularfelder gelten als nicht getätigt → Bemerkungszeilen bzw. separate Beilage mit Verweis
- **Beachten:** Arbeitsüberlastung ist kein Fristerstreckungsgrund; elektronisch erst mit Eingang der Quittung eingereicht
- **Limiten:**
  - Fristerstreckung – Regel (Private / Treuhänder), Kosten: Kanton **Gesuch beim Gemeindesteueramt (schriftlich, begründet, rechtzeitig). Private: erstes Gesuch grundsätzlich bis 30. September des Deklarationsjahres, weitere in begründeten Fällen bis 30. November. Gewerbsmässige Treuhänder und Steuerberater können für ihre Mandanten bis 31. Dezember des Deklarationsjahres beantragen. Arbeitsüberlastung ist kein Grund. Weitere Gesuche darüber hinaus nur bei ausserordentlichen Gründen.** · Bund **n/a – Bund: keine eigene Regel; es gilt das kantonale Verfahren der Steuererklärung.**
  - Belegpflicht-Schwellen (z.B. Rechnungen ab CHF …): Kanton **Immer einzureichen: sämtliche Lohnausweise, Aufstellungen bei Selbständigen, Bankauszüge bei Total-Deklaration, Säule-3a-Bescheinigungen. Rechnungskopien Liegenschaftsunterhalt ab CHF 1'000; Bestätigungen freiwilliger Zuwendungen ab CHF 1'000 pro Zuwendung (darunter keine Belege, Nachforderung vorbehalten).** · Bund **n/a – Beilagen: Lohnausweise, Verzeichnisse über Wertschriften/Forderungen/Schulden (Art. 125 DBG); Schwellen sind kantonale Praxis.**
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0018.md) `tg-form-01-2025__c0018` – «Diese Steuererklärung ist vollständig und wahrheitsgetreu ausgefüllt»
  - [WL TG 2025 S. 10](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0036.md) `tg-wl-2025__c0036` – «Bei elektronischer Datenübermittlung gilt die Steuererklärung erst als einge»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0002.md) `tg-stp-155-2__c0002` – «gewerbsmässig Steuererklärungen ausfüllen, können»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0002.md) `tg-stp-155-2__c0002` – «längstens bis zum 31. Dezember des Deklarationsjahres»
  - [WL TG 2025 S. 10](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0036.md) `tg-wl-2025__c0036` – «– Bestätigungen von freiwilligen Zuwendungen ab einem Betrag von Fr. 1'000;»
  - [WL TG 2025 S. 8](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0024.md) `tg-wl-2025__c0024` – «haben beide die Steuererklärung persönlich zu unterschreiben. Diese Bestimmung gilt auch beim Vorliegen einer Vertretungsvollmacht»
  - [WL TG 2025 S. 29](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0137.md) `tg-wl-2025__c0137` – «ausserhalb der Formularfelder der Steuererklärungsformulare nicht berücksichtigt werden können»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md) `tg-stp-155-2__c0001` – «jedoch längstens bis am 30. September des Deklarationsjahres, gutgeheissen»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md) `tg-stp-155-2__c0001` – «Arbeitsüberlastung stellt keinen Fristverlängerungsgrund dar»
  - [WL TG 2025 S. 7](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0023.md) `tg-wl-2025__c0023` – «Die ausgefüllte Steuererklärung und die Hilfsblätter sind bis zum vorgedruckten Datum»
  - [WL TG 2025 S. 10](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0035.md) `tg-wl-2025__c0035` – «Reichen Sie Ihrem Steueramt die persönlich unterzeichnete Quittung zusammen mit dem»
  - [WL TG 2025 S. 10](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0035.md) `tg-wl-2025__c0035` – «bei selbständiger Erwerbstätigkeit Aufstellungen über die Einnahmen und Ausgaben»

## Hilfsblatt Berufskosten

<a id="form-4-2-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2 Ziff. 1.2 – Geschäftsfahrzeug zur Verfügung für die Fahrt zur Arbeitsstätte (ja/nein, von–bis)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld F (unentgeltliche Beförderung Wohn-/Arbeitsort) und Ziff. 2.2 (Privatanteil Geschäftsfahrzeug)
- **Rein:** Lohnausweis → Privatanteil Geschäftsfahrzeug 0.9 % pro Monat (enthält Arbeitsweg) · Arbeitgeber (Fahrzeugüberlassung) → Zeitraum von–bis der kostenlosen Zurverfügungstellung
- **Rechnen:** Ja → für den Zeitraum von–bis kein Fahrkostenabzug in Ziff. 2.1–2.3; keine Aufrechnung, da Arbeitsweg im Privatanteil 0.9 % pro Monat enthalten
- **Regel:** Steht ein Geschäftsfahrzeug für den Arbeitsweg kostenlos zur Verfügung, ist kein Fahrkostenabzug möglich (Privatanteil 0.9% pro Monat im Lohn enthält den Arbeitsweg, daher keine Aufrechnung). Lohnausweis Feld F angekreuzt = keine Fahrkosten (Ziff. 2.1–2.5) geltend machen; gilt ebenso bei Sammeltransport oder vergüteten effektiven Autokilometern von Aussendienstmitarbeitern; Vergütungen des Arbeitswegs in Lohnausweis Ziff. 2.3 sind kein Feld-F-Fall. Zeitraum von–bis angeben, falls nur zeitweise.
- **Beachten:** Privatanteil Kanton 0.9 % des Kaufpreises, mind. Fr. 150/Monat (§ 1a BKV TG) / Bund 0,9 % (Art. 5a BKV)
- **Beachten:** Generell kein Abzug, soweit Arbeitgeber Fahrkosten vergütet oder Fahrmöglichkeit bietet (§ 6 BKV TG)
- **Beachten:** Nur zeitweise zur Verfügung: Zeitraum von–bis angeben
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0001.md) `tg-form-04-2-2025__c0001` – «1.2 Steht Ihnen für die Fahrt zur Arbeitsstätte»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0176.md) `tg-wl-2025__c0176` – «Da der geldwerte Vorteil für den Arbeitsweg somit be»
  - [WL Lohnausweis 2026 S. 10–11](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0022.md) `bund-wl-lohnausweis-2026__c0022` – «In allen Fällen ist im Lohnausweis grundsätzlich das Feld F (unentgeltliche Beförderung zwi»
  - [BKV TG § 1a](../../chunks/tg/2025/tg-bkv/tg-bkv__par-1a.md) `tg-bkv__par-1a` – «0.9 Prozent des Kaufpreises des Fahrzeugs, mindestens aber Fr. 150 pro Monat»
  - [BKV Art. 5a](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-5a.md) `bund-bkv-2025__art-5a` – «gelten 0,9 Prozent des Kaufpreises des Fahrzeugs als monatliches Einkommen aus dieser Nutzung»
  - [BKV TG § 6](../../chunks/tg/2025/tg-bkv/tg-bkv__par-6.md) `tg-bkv__par-6` – «Soweit Berufsauslagen vom Arbeitgeber oder von anderer Seite vergütet werden oder eine Fahrmöglichkeit geboten wird, steht dem Steuerpflichtigen kein Abzug zu»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0179.md) `tg-wl-2025__c0179` – «können Sie keine Fahrtkosten geltend machen»
  - [WL TG 2025 S. 37–38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0177.md) `tg-wl-2025__c0177` – «selbst getragenen (notwendigen) Fahrkosten (Ziff. 2.1 bis 2.3)»

<a id="form-4-2-ziff-2-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2 Ziff. 2.1 – Abonnementskosten öffentliche Verkehrsmittel (Code 206; Person 2: 246)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg → ÖV-Abonnement/Beleg über tatsächliche Kosten
- **Rein:** ÖV-Abonnement (Rechnung/Quittung) → tatsächlich bezahlte Abokosten Arbeitsweg · Arbeitgeberbestätigung/Lohnausweis → vom Arbeitgeber übernommene Fahrkosten (kein Abzug)
- **Rechnen:** Σ nachgewiesene, selbst getragene Abokosten (Kanton = Bund); Begrenzung in Ziff. 2.5: Kanton max. Fr. 6'000 / Bund max. Fr. 3'300
- **Regel:** Tatsächlich entstandene, nachgewiesene Abonnementskosten (Staat und Bund gleich). Nur wenn Feld F im Lohnausweis nicht angekreuzt ist; vom Arbeitgeber vergütete Kosten (Lohnausweis Ziff. 2.3) nicht abziehbar. Beachtenswerte Entfernung ab ca. 1 km. Fahrkostenbeschränkung gilt für alle Fahrkosten zusammen (inkl. Wochenaufenthalt).
- **Beachten:** Nur bei beachtenswerter Entfernung (ab ca. 1 km)
- **Beachten:** Kein Abzug für vom Arbeitgeber übernommene Kosten oder bei Geschäftsfahrzeug (Ziff. 1.2)
- **Beachten:** Wochenaufenthalt: Fahrkosten (Heimkehr, Unterkunft–Arbeitsstätte) ebenfalls in Ziff. 2.1–2.3
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 pro Jahr (alle Fahrkosten inkl. Wochenaufenthalt und Nebenerwerb zusammen; keine Kürzung bei unterjähriger Steuerpflicht/Teilzeit).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0002.md) `tg-form-04-2-2025__c0002` – «2.1 Abonnementskosten für öffentliche Verkehrsmittel   206»
  - [WL TG 2025 S. 37–38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0177.md) `tg-wl-2025__c0177` – «Bei Benützung öffentlicher Verkehrsmittel (Bahn, Tram, Autobus) können Sie die tatsächlich ent»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0002.md) `tg-stp-29-2__c0002` – «sowohl für die Staats- und Gemeindesteuern als auch für die direkte Bundessteuer die tatsächlich entstandenen (nachgewiesenen) Abonnementskosten abgezogen werden»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0175.md) `tg-wl-2025__c0175` – «Kein Abzug ist zulässig für Kosten, die Arbeitgebende übernommen haben»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0188.md) `tg-wl-2025__c0188` – «Deklarieren Sie die Fahrkosten für den Wochenaufenthalt unter den Ziffern 2.1 bis 2.3»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0179.md) `tg-wl-2025__c0179` – «können Sie keine Fahrtkosten geltend machen (vgl. Ziff. 1.2)»

<a id="form-4-2-ziff-2-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2 Ziff. 2.2 – Fahrrad, Motorfahrrad, Kleinmotorrad bis 50 cm3, pauschal (Code 210; Person 2: 250)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Belege nötig (Pauschale)
- **Rein:** Keine Belege (Pauschale) – nur Fahrzeugart: Fahrrad, Motorfahrrad, Kleinmotorrad mit gelbem Kontrollschild
- **Rechnen:** Pauschal Fr. 700 pro Jahr (Kanton = Bund); unterjährige Erwerbstätigkeit: Fr. 700 × Erwerbstage/360; zählt zur Begrenzung Ziff. 2.5
- **Regel:** Pauschal bis Fr. 700 pro Jahr (Fahrrad, Motorfahrrad, Kleinmotorrad bis 45 km/h mit gelbem Kontrollschild).
- **Beachten:** Nur bis 45 km/h mit gelbem Kontrollschild; Motorrad mit weissem Kontrollschild → Ziff. 2.3
- **Beachten:** Bund: tatsächliche Kosten zusätzlich nicht abziehbar
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Fahrrad, Motorfahrrad/Kleinmotorrad (bis 45 km/h, gelbes Kontrollschild): bis CHF 700 pro Jahr.)** · Bund **CHF 700 (Pauschale pro Jahr für Fahrrad, Motorfahrrad und Motorrad mit gelbem Kontrollschild; tatsächliche Kosten zusätzlich nicht abziehbar)**
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0002.md) `tg-form-04-2-2025__c0002` – «2.2 Fahrrad, Kleinmotorrad bis 50 cm3 pauschal Fr. 700.–   210»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0002.md) `tg-stp-29-2__c0002` – «können im Jahr bis zu **Fr. 700** abgezogen werden»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0175.md) `tg-wl-2025__c0175` – «Die als Pauschalen ausgestalteten Berufsauslagen beziehen sich auf das ganze Jahr»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0176.md) `tg-wl-2025__c0176` – «Umrechnung Fr. 3'200 x 270 = Fr. 2'400»
  - [WL TG 2025 S. 37–38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0177.md) `tg-wl-2025__c0177` – «schwindigkeit bis 45 km/h, gelbes Kontrollschild) können Sie bis zu Fr. 700 im Jahr abziehen»

<a id="form-4-2-ziff-2-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2 Ziff. 2.3 – Kosten für privates Motorfahrzeug (Auto / Motorrad über 50 cm3), km pro Tag × Anzahl Tage (Code 211; Person 2: 251; Staat und Bund getrennt)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Distanz Wohnadresse–Standort Fahrzeug am Arbeitsort/P+Rail; Jahreskilometer
- **Rein:** Fahrzeugausweis → Fahrzeugart (Auto / Motorrad über 50 cm3) · Distanzangabe → km pro Tag Wohnadresse–Standort Fahrzeug am Arbeitsort bzw. P+Rail-Anlage · Arbeitszeitangaben → Anzahl Arbeitstage (100 %-Pensum i.d.R. max. 225)
- **Rechnen:** km/Jahr = km/Tag × Tage; Kanton Auto: erste 3'000 km × 0.60 + nächste 2'000 × 0.50 + Rest × 0.40 / Bund: km × 0.70; Motorrad beide × 0.40
- **Regel:** Nur in begründeten Ausnahmefällen (ÖV unzumutbar, z.B. Zeitersparnis über 1 Stunde pro Arbeitstag), sonst nur Kosten des ÖV-Abonnements. Kanton Auto gestaffelt: bis 3'000 km Fr. 0.60, 3'001–5'000 km Fr. 0.50, über 5'000 km Fr. 0.40 (inkl. Parkgebühren); Motorrad ab 45 km/h Fr. 0.40. Bund Auto einheitlich Fr. 0.70/km. In der Regel max. 225 Arbeitstage bei 100%-Pensum. Kanton und Bund separat berechnen, da unterschiedliche Spalten. Heimkehr am Mittag: Fahrkosten höchstens bis Höhe des Verpflegungsabzugs und dann kein zusätzlicher Verpflegungsabzug.
- **Beachten:** Nur wenn ÖV unzumutbar (z.B. Zeitersparnis über 1 Stunde pro Arbeitstag, nur Hin- und Rückweg) – sonst ÖV-Abokosten
- **Beachten:** Parkgebühren in den km-Ansätzen enthalten; P+Rail grundsätzlich zumutbar (Parkgebühren dann abziehbar)
- **Beachten:** Heimkehr über Mittag: Fahrkosten max. in Höhe Verpflegungsabzug, dann kein Abzug Ziff. 3.1/3.2
- **Limiten:**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **Privatauto, nur in Ausnahmefällen (wenn ÖV nicht zumutbar): gestaffelt nach jährlicher Fahrleistung bis 3'000 km CHF 0.60/km, 3'001-5'000 km CHF 0.50/km, über 5'000 km CHF 0.40/km (stufenweise Berechnung; inkl. Parkgebühren). Normalfall: Kosten des ÖV-Abonnements.** · Bund **CHF 0.70 (Privatauto: Abzug pro Fahrkilometer CHF 0.70, nur wenn kein öffentliches Verkehrsmittel verfügbar/zumutbar (Steuerjahr 2025))**
  - Fahrkosten Motorrad – Ansatz pro km (CHF): Kanton **CHF 0.40 (Motorrad (Höchstgeschwindigkeit ab 45 km/h, weisses Kontrollschild): bis CHF 0.40 pro Fahrkilometer, nur wenn ÖV nicht zumutbar.)** · Bund **CHF 0.40 (Motorrad mit weissem Kontrollschild: CHF 0.40 pro Fahrkilometer (Steuerjahr 2025))**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **225 Tage (Bei Privatauto-Berechnung bei 100%-Tätigkeit in der Regel für maximal 225 Arbeitstage pro Jahr.)** · Bund **n/a – Bund kennt keine Festlegung massgebender Arbeitstage; abziehbar sind die tatsächlichen notwendigen Kosten bis zum Maximalbetrag (Art. 26 Abs. 1 lit. a DBG).**
- **Bund:** Bund: Auto einheitlich Fr. 0.70/km (Kanton gestaffelt 0.60/0.50/0.40).
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0002.md) `tg-form-04-2-2025__c0002` – «Total Kosten für den Arbeitsweg mit dem Motorfahrzeug   km pro Jahr 211»
  - [WL TG 2025 S. 4](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0003.md) `tg-wl-2025__c0003` – «über 5'000 km   Fr. 0.40 pro Fahrkilometer»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0180.md) `tg-wl-2025__c0180` – «Bei der direkten Bundessteuer beträgt der Ansatz einheitlich Fr. -.70 pro gefahrenen Kilometer.»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0004.md) `tg-stp-29-2__c0004` – «Für Autos gelten, je nach jährlich gefahrener Kilometerzahl, für die Staats- und Gemeindesteuern die folgenden Ansätze:»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0178.md) `tg-wl-2025__c0178` – «über 1 Stunde beträgt, wobei für diese Berechnung nur die morgendliche Hinfahrt zur Arbeit und»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0179.md) `tg-wl-2025__c0179` – «Die Benutzung des P+Rail-Systems ist»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0179.md) `tg-wl-2025__c0179` – «Kosten abziehen, die für die Mehrkosten für auswärtige Verpflegung abzugsfähig»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0179.md) `tg-wl-2025__c0179` – «wobei in diesem Fall auch die Parkgebühren abzugsfähig sind»

<a id="form-4-2-ziff-2-4-berechnung-total"></a>
### Ziff. Form. 4.2 Ziff. 2.4 – Total effektive Fahrkosten (Ziffern 2.1–2.3) (Code 212; Person 2: 252)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 2.1 + 2.2 + 2.3 (je Spalte Staat / Bund)
- **Rechnen:** Σ Ziff. 2.1–2.3, getrennt Staat / Bund (verschiedene km-Ansätze in 2.3)
- **Regel:** Summe 2.1 bis 2.3 (inkl. Fahrkosten Wochenaufenthalt gemäss Ziff. 5), separat je Spalte Staat/Bund.
- **Beachten:** Fahrkosten Wochenaufenthalt (Heimkehr, Unterkunft–Arbeitsstätte) sind in 2.1–2.3 enthalten
- **Beachten:** Beispiel WL 12'150 km Auto: Kanton Fr. 5'660 / Bund Fr. 8'505
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0002.md) `tg-form-04-2-2025__c0002` – «2.4 Total effektive Fahrkosten (Ziffern 2.1 – 2.3)   212»
  - [WL TG 2025 S. 38–39](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0181.md) `tg-wl-2025__c0181` – «Ermitteln Sie das Total der effektiv selbst getragenen Fahrkosten, indem Sie die Beträge der Ziffern»
  - [WL TG 2025 S. 38–39](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0182.md) `tg-wl-2025__c0182` – «Total effektive Fahrkosten (Ziffer 2.4) Fr. 5'660 Fr. 8'505»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0188.md) `tg-wl-2025__c0188` – «Deklarieren Sie die Fahrkosten für den Wochenaufenthalt unter den Ziffern 2.1 bis 2.3»

<a id="form-4-2-ziff-2-5-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2 Ziff. 2.5 – Total abzugsfähige Fahrkosten, Staat max. Fr. 6'000 / Bund max. Fr. 3'300 (Code 213; Person 2: 253)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 2.4 begrenzt auf Maximum)
- **Rein:** Übertrag Ziff. 2.4 (je Spalte Staat / Bund)
- **Rechnen:** Staat: min(Ziff. 2.4; Fr. 6'000) / Bund: min(Ziff. 2.4; Fr. 3'300) → Ziff. 7
- **Regel:** Staat: min(Ziff. 2.4; Fr. 6'000), Bund: min(Ziff. 2.4; Fr. 3'300). Maximum wird bei unterjähriger Steuerpflicht/Erwerbsdauer oder Teilzeit nicht gekürzt. Beispiel WL: 12'150 km → Kanton Fr. 5'660, Bund effektiv Fr. 8'505 → Fr. 3'300.
- **Beachten:** Maxima nicht gekürzt bei unterjähriger Steuerpflicht/Erwerbsdauer oder Teilzeit
- **Beachten:** Begrenzung umfasst alle Fahrkosten (ÖV, Velo, Motorrad, Auto, inkl. Wochenaufenthalt)
- **Beachten:** Behinderungsbedingte Mehrkosten des Arbeitswegs nicht hier, sondern unter behinderungsbedingten Kosten
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 pro Jahr (alle Fahrkosten inkl. Wochenaufenthalt und Nebenerwerb zusammen; keine Kürzung bei unterjähriger Steuerpflicht/Teilzeit).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Bund:** Bund max. Fr. 3'300 (Kanton Fr. 6'000).
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0002.md) `tg-form-04-2-2025__c0002` – «Total abzugsfähige Fahrkosten (Übertrag von Ziffer 2.4, aber Staat max. Fr. 6000.– / Bund max. Fr. 3300.–)   213»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0006.md) `tg-stp-29-2__c0006` – «Bei der direkten Bundessteuer beträgt der Maximalabzug:»
  - [StG TG § 29](../../chunks/tg/2025/tg-stg/tg-stg__par-29.md) `tg-stg__par-29` – «bis zu einem Maximalbetrag von Fr. 6'000»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0007.md) `tg-stp-29-2__c0007` – «werden auch bei unterjähriger Steuerpflicht, unterjähriger Erwerbsdauer oder Teilzeitarbeit nicht gekürzt»

<a id="form-4-2-ziff-3-1-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4.2 Ziff. 3.1 – Mehrkosten auswärtige Verpflegung ohne Verbilligung oder bei Schicht-/Nachtarbeit, Fr. 15 pro Tag, max. Fr. 3'200 (Code 214; Person 2: 254)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis (Feld G nicht angekreuzt; Ziff. 15 Anzahl Schichttage; Spesenreglement/Ziff. 13.2); Arbeitgeberbescheinigung Schichttage
- **Rein:** Lohnausweis → Anzahl Schichttage (sofern aufgeführt) · Arbeitgeberbescheinigung → Anzahl Tage mit mind. achtstündiger Schicht-/Nachtarbeit (falls nicht im Lohnausweis) · Formular 4.2 Ziff. 1.1 → Erwerbsdauer und Arbeitspensum (Kürzung)
- **Rechnen:** min(Arbeits- bzw. Schichttage × Fr. 15; Fr. 3'200 × Beschäftigungsgrad); unterjährig Fr. 3'200 × Erwerbstage/360; Kanton = Bund
- **Regel:** Fr. 15 pro auswärtige Hauptmahlzeit (i.d.R. Mittagessen), bei ständiger Verpflegung max. Fr. 3'200/Jahr, bei Teilzeit/Nebenberuf und unterjährig entsprechend gekürzt. Voraussetzung: Heimkehr am Mittag unzumutbar (grosse Entfernung oder sehr kurze Pause). Schicht-/Nachtarbeit: gleicher Abzug pro ausgewiesenem Tag mit mind. 8 Stunden durchgehender Schicht-/Nachtarbeit; Anzahl Schichttage in das Feld eintragen und belegen (Lohnausweis Ziff. 15 oder Arbeitgeberbescheinigung). Kein Abzug, wenn Mahlzeit unter Fr. 10 zu stehen kommt oder wenn Fahrkosten für Heimkehr am Mittag geltend gemacht werden. Lohnausweis Feld G angekreuzt → Ziff. 3.2 statt 3.1. Nicht kumulierbar mit Wochenaufenthalt (Ziff. 5.2) für denselben Zeitraum.
- **Beachten:** Nur bei unzumutbarer Heimkehr am Mittag (grosse Entfernung/kurze Essenspause); kein Abzug bei Mahlzeit unter Fr. 10
- **Beachten:** Schichttage: nur ausgewiesene, durchgehende, mind. achtstündige Schicht-/Nachtarbeit; mit Verbilligung/Kantine → 3.2
- **Beachten:** Nicht kumulierbar mit Ziff. 5.2 (gleicher Zeitraum) oder Fahrkosten Heimkehr über Mittag
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Pauschale CHF 15 pro auswärtige Hauptmahlzeit (in der Regel nur Mittagessen), wenn Heimkehr am Mittag wegen grosser Entfernung oder sehr kurzer Essenspause unzumutbar.)** · Bund **CHF 15 (Mehrkosten auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (i.d.R. Mittagessen); ausschliesslich Pauschale, wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei ständiger auswärtiger Verpflegung maximal CHF 3'200 pro Jahr; bei Teilzeitpensum Kürzung nach Beschäftigungsgrad (z.B. 80% = Fr. 2'560).)** · Bund **CHF 3'200 (Bei ständiger auswärtiger Verpflegung CHF 3'200 pro Jahr (voller Abzug))**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Durchgehende, mindestens achtstündige Schicht-/Nachtarbeit (oder gleichgestellte gestaffelte Arbeitszeit): gleiche Abzüge wie auswärtige Verpflegung (CHF 15/Tag, max. CHF 3'200/Jahr; bei Verbilligung halb). Nicht kumulierbar mit Verpflegungs- oder Wochenaufenthaltsabzug.)** · Bund **CHF 15 (Durchgehende Schicht-/Nachtarbeit (gestaffelte Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich): CHF 15 pro ausgewiesenem Tag, bei ganzjähriger Schicht-/Nachtarbeit CHF 3'200 pro Jahr)**
- **Bund:** Gleiche Ansätze beim Bund.
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0003.md) `tg-form-04-2-2025__c0003` – «pro ausgewiesenem Schichttag, pro Arbeitstag Fr. 15.– / max. Fr. 3200.– pro Jahr   214»
  - [WL TG 2025 S. 39](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0183.md) `tg-wl-2025__c0183` – «Der Pauschalabzug beträgt Fr. 15 für jede auswärtige Hauptmahlzeit (in der Regel nur für Mittag»
  - [WL TG 2025 S. 39–40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0184.md) `tg-wl-2025__c0184` – «Für jeden ausgewiesenen Tag mit durchgehender, mindestens achtstündiger Schicht- oder»
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «die Anzahl im Kalenderjahr geleisteter Schichttage»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0176.md) `tg-wl-2025__c0176` – «Umrechnung Fr. 3'200 x 270 = Fr. 2'400»
  - [WL TG 2025 S. 39–40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0185.md) `tg-wl-2025__c0185` – «Fr. 10 zu stehen kommen bzw. wenn die Arbeitgebenden bei der Bewertung»
  - [BKV TG § 3](../../chunks/tg/2025/tg-bkv/tg-bkv__par-3.md) `tg-bkv__par-3` – «Der Abzug für Schicht- oder Nachtarbeit kann nicht zusätzlich zum Abzug für auswärtige Verpflegung oder für auswärtigen Wochenaufenthalt beansprucht werden»
  - [WL TG 2025 S. 38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0179.md) `tg-wl-2025__c0179` – «Kosten abziehen, die für die Mehrkosten für auswärtige Verpflegung abzugsfähig»
  - [BKV TG § 3](../../chunks/tg/2025/tg-bkv/tg-bkv__par-3.md) `tg-bkv__par-3` – «Der Arbeitgeber muss die Anzahl Tage mit Schicht- oder Nachtarbeit sowie den Arbeitsort auf Verlangen bescheinigen»

<a id="form-4-2-ziff-3-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4.2 Ziff. 3.2 – Mehrkosten auswärtige Verpflegung mit Verbilligung durch Arbeitgeber/Kantine, Fr. 7.50 pro Tag, max. Fr. 1'600 (Code 216; Person 2: 256)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten)
- **Rein:** Lohnausweis/Arbeitgeber → Verbilligung der Hauptmahlzeit durch Barbeiträge oder Gutscheine · Arbeitgeber → Kantine, Personalrestaurant oder Gaststätte des Arbeitgebers verfügbar
- **Rechnen:** min(Arbeitstage × Fr. 7.50; Fr. 1'600 × Beschäftigungsgrad); Kanton = Bund
- **Regel:** Wenn der Arbeitgeber Mahlzeiten verbilligt (Barbeiträge, Gutscheine/Lunch-Checks) oder eine Kantine/Personalrestaurant zur Verfügung steht und trotzdem Mehrkosten entstehen: nur halber Abzug, Fr. 7.50/Tag, max. Fr. 1'600/Jahr. Lohnausweis Feld G angekreuzt ist das Signal (auch wenn nicht bekannt ist, ob die Kantine genutzt wird). Trägt der Arbeitgeber die Kosten des Mittagessens vollständig (z.B. Vermerk «Mittagessen durch Arbeitgeber bezahlt» in Lohnausweis Ziff. 15), entstehen keine Mehrkosten – kein Verpflegungsabzug (Folgerung aus WL: kein Abzug für vom Arbeitgeber übernommene Kosten). Teilzeit/Nebenberuf: angemessen kürzen.
- **Beachten:** Halber Abzug schon, wenn Mahlzeit in Kantine/Personalrestaurant eingenommen werden kann
- **Beachten:** Hauptmahlzeit beim Arbeitgeber zwingend (z.B. Gastgewerbe): max. ein halber Abzug pro Tag
- **Beachten:** Kein Abzug bei Mahlzeit unter Fr. 10 bzw. Naturalbezug unter Mittagessen Fr. 10 / Abendessen Fr. 8 / Fr. 21.50 pro Tag
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Halber Abzug (CHF 7.50 pro Tag), wenn Hauptmahlzeiten vom Arbeitgeber verbilligt (Gutscheine/Beiträge) oder Kantine/Personalrestaurant zur Verfügung steht. Kein Abzug, wenn Mahlzeit unter CHF 10 kostet.)** · Bund **CHF 7.50 (Halber Abzug CHF 7.50 pro Hauptmahlzeit, wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Halber Abzug bei verbilligter Verpflegung: maximal CHF 1'600 pro Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: CHF 1'600 pro Jahr)**
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0003.md) `tg-form-04-2-2025__c0003` – «3.2 mit Verbilligung durch Arbeitgeber/in oder Kantine,»
  - [WL TG 2025 S. 39–40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0185.md) `tg-wl-2025__c0185` – «Nur der halbe Abzug (Fr. 7.50 im Tag, Fr. 1'600 im Jahr) ist zulässig, wenn Hauptmahlzeiten von»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten   Buchstabe G»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Dieses Feld ist auch anzukreuzen bei Arbeitnehmern, die 40 % - 60 % der Arbeitszeit aus»
  - [WL TG 2025 S. 39–40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0186.md) `tg-wl-2025__c0186` – «folgende Werte unterschreiten: Mittagessen Fr. 10, Abendessen Fr. 8 oder Fr. 21.50 pro Tag»
  - [WL TG 2025 S. 39–40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0186.md) `tg-wl-2025__c0186` – «erfolgt eine angemessene Kürzung des Pauschalbetrags»

<a id="form-4-2-ziff-4-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4.2 Ziff. 4 – Übrige für die Ausübung des Berufes erforderliche Kosten: 3% vom Nettolohn, min. Fr. 2'000, max. Fr. 4'000, oder effektiv (Code 220; Person 2: 260)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 Nettolohn (Basis Pauschale); bei effektiven Kosten separate Aufstellung mit Belegen
- **Rein:** Lohnausweis → Ziff. 11 Nettolohn (Basis Pauschale) · Aufstellung + Belege (Werkzeug, Fachliteratur, Berufskleider, Verbands-/Gewerkschaftsbeiträge) → nur statt Pauschale
- **Rechnen:** min(max(3 % × Nettolohn LA Ziff. 11; Fr. 2'000); Fr. 4'000), Kanton = Bund; Erwerb unter 12 Monaten: anteilmässig kürzen
- **Regel:** Pauschale 3% des Nettolohns (Lohnausweis Ziff. 11), mindestens Fr. 2'000, höchstens Fr. 4'000 (Kanton und Bund); bei unterjähriger Erwerbstätigkeit anteilmässig gekürzt. Alternativ nachgewiesene effektive Kosten gemäss Aufstellung – nicht kumulierbar mit der Pauschale. Deckt Berufswerkzeug, Fachliteratur, Kleider/Schuhverschleiss, Schwerarbeit, Berufsverbands-/Gewerkschaftsbeiträge. Erhaltene Spesenvergütungen mindern effektive Kosten.
- **Beachten:** Effektive Kosten nicht zusätzlich zur Pauschale
- **Beachten:** Vom Arbeitgeber vergütete Auslagen nicht abziehbar (§ 6 BKV TG)
- **Beachten:** Nur Haupterwerb; Nebenbeschäftigung → Ziff. 6
- **Limiten:**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **3 % (Pauschale übrige Berufskosten: 3% des Nettolohnes (Alternative: Nachweis höherer tatsächlicher Kosten, keine Kumulation).)** · Bund **3 % (Übrige Berufskosten: 3 % des Nettolohns (Pauschale; Nachweis höherer Kosten möglich); bei Teilzeit/unterjährig angemessen kürzen)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **CHF 2'000 (Pauschale übrige Berufskosten: Minimum CHF 2'000.)** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 4'000 (Pauschale übrige Berufskosten: Maximum CHF 4'000.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
- **Bund:** Gleiche Pauschale beim Bund (3%, Fr. 2'000–4'000).
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0004.md) `tg-form-04-2-2025__c0004` – «3% vom Nettolohn, mindestens jedoch Fr. 2000.– und höchstens Fr. 4000.–»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0187.md) `tg-wl-2025__c0187` – «Pauschalabzug von 3% vom Nettolohn gemäss Ziffer 11 des Lohnausweises»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0187.md) `tg-wl-2025__c0187` – «Anstelle der Pauschale können Sie die notwendigen tatsächlichen Aufwendungen nachweisen.»
  - [BKV TG § 6](../../chunks/tg/2025/tg-bkv/tg-bkv__par-6.md) `tg-bkv__par-6` – «Soweit Berufsauslagen vom Arbeitgeber oder von anderer Seite vergütet werden oder eine Fahrmöglichkeit geboten wird, steht dem Steuerpflichtigen kein Abzug zu»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0174.md) `tg-wl-2025__c0174` – «Berufsauslagen im Zusammenhang mit einer Nebenbeschäftigung in unselbständiger Anstellung»

<a id="form-4-2-ziff-5-1-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4.2 Ziff. 5.1 – Wochenaufenthalt: Unterkunft, ortsübliche Auslagen für ein Zimmer (Code 226; Person 2: 266)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Mietvertrag/Mietzinsbeleg auswärtige Unterkunft
- **Rein:** Mietvertrag/Mietzinsbelege auswärtige Unterkunft → Jahresmietzins, Anzahl Zimmer
- **Rechnen:** Zimmer: ortsübliche Kosten; Wohnung bis 3½ Zimmer: Jahresmietzins : (Anzahl Zimmer + 1)
- **Regel:** Nur ein Zimmer (keine Wohnung) gilt als notwendig; bei kleiner Wohnung bis 3½ Zimmer Jahresmietzins : (Zimmerzahl + 1). Voraussetzung: regelmässige Heimkehr am Wochenende an den steuerlichen Wohnsitz. Fahrkosten der Heimkehr gehören unter Ziff. 2.1–2.3 (mit Fahrkostenbeschränkung).
- **Beachten:** Nur bei regelmässiger Heimkehr (Wochenende/freie Tage) an den steuerlichen Wohnsitz
- **Beachten:** Kein Abzug, wenn Unterkunft als Naturallohn erhalten (§ 4 BKV TG)
- **Beachten:** Fahrkosten Heimkehr unter Ziff. 2.1–2.3 (Fahrkostenbeschränkung gilt)
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Wochenaufenthalt: ortsübliche Auslagen für ein Zimmer (keine Wohnung); bei kleiner Wohnung bis 3.5 Zimmer: Jahresmietzins : (Anzahl Zimmer + 1). Kein Abzug bei Naturallohn. Zusätzlich notwendige Fahrkosten der wöchentlichen Heimkehr (unter Fahrkostenbeschränkung).** · Bund **Mehrkosten Unterkunft: ortsübliche Auslagen für ein Zimmer (nicht eine Wohnung) abziehbar; Fahrkosten der regelmässigen Heimkehr bis zum Maximalbetrag nach Art. 5 Abs. 1 BKV**
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0004.md) `tg-form-04-2-2025__c0004` – «5.1 Unterkunft ortsübliche Auslagen für ein Zimmer   226»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0189.md) `tg-wl-2025__c0189` – «wendigen Mehrkosten der Unterkunft können Sie daher nur die ortsüblichen Auslagen für ein»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0188.md) `tg-wl-2025__c0188` – «über das Wochenende oder an den freien Tagen nach Hause zurückkehren»
  - [BKV TG § 4](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4.md) `tg-bkv__par-4` – «ein Abzug gemäss Ziff. 1 und Ziff. 2 ist nicht zulässig, wenn der Steuerpflichtige die entsprechende Leistung als Naturallohn erhält»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0188.md) `tg-wl-2025__c0188` – «Deklarieren Sie die Fahrkosten für den Wochenaufenthalt unter den Ziffern 2.1 bis 2.3»

<a id="form-4-2-ziff-5-2-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4.2 Ziff. 5.2 – Wochenaufenthalt: Verpflegung, Fr. 30 pro Arbeitstag / max. Fr. 6'400, mit Verbilligung Fr. 22.50 / max. Fr. 4'800 (Code 230; Person 2: 270)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis (Feld G bei verbilligtem Mittagessen)
- **Rein:** Lohnausweis/Arbeitgeber → Verbilligung des Mittagessens (Kantinenkost, Kostenbeitrag, Naturalleistung) · Aufstellung → Arbeitstage am Wochenaufenthaltsort
- **Rechnen:** min(Tage × Fr. 30; Fr. 6'400); Mittagessen verbilligt: min(Tage × Fr. 22.50; Fr. 4'800); Kanton = Bund
- **Regel:** Fr. 15 pro Hauptmahlzeit = Fr. 30/Tag, ganzjährig max. Fr. 6'400; bei Verbilligung des Mittagessens durch den Arbeitgeber (Feld G) nur halber Abzug für diese Mahlzeit = Fr. 22.50/Tag bzw. Fr. 4'800/Jahr. Nicht kumulierbar mit Ziff. 3 für denselben Zeitraum.
- **Beachten:** Nicht kumulierbar mit Ziff. 3.1/3.2 und Schicht-/Nachtarbeitsabzug für denselben Zeitraum
- **Beachten:** Kein Abzug, wenn Verpflegung als Naturallohn erhalten (§ 4 BKV TG)
- **Beachten:** Bund: Nachweis höherer Kosten ausgeschlossen
- **Limiten:**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 6'400 (Wochenaufenthalt Verpflegung: CHF 15 pro Hauptmahlzeit, CHF 30 pro Tag, bei ganzjährigem Wochenaufenthalt CHF 6'400 pro Jahr; bei Verbilligung Mittagessen CHF 22.50/Tag bzw. CHF 4'800/Jahr.)** · Bund **CHF 6'400 (Auswärtiger Wochenaufenthalt: Verpflegung CHF 30 pro Tag, max. CHF 6'400 pro Jahr; bei Verbilligung CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr; Nachweis höherer Kosten ausgeschlossen)**
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0004.md) `tg-form-04-2-2025__c0004` – «bei Verbilligung pro Arbeitstag Fr. 22.50 / im Jahr Fr. 4800.–»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0190.md) `tg-wl-2025__c0190` – «benden) und trotzdem Mehrkosten entstehen, wird für diese Mahlzeit nur der halbe Abzug (Fr. 7.50)»
  - [WL TG 2025 S. 39](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0183.md) `tg-wl-2025__c0183` – «Den Abzug für Mehrkosten der auswärtigen Verpflegung bei täglicher Heimkehr können Sie für den»
  - [BKV TG § 3](../../chunks/tg/2025/tg-bkv/tg-bkv__par-3.md) `tg-bkv__par-3` – «Der Abzug für Schicht- oder Nachtarbeit kann nicht zusätzlich zum Abzug für auswärtige Verpflegung oder für auswärtigen Wochenaufenthalt beansprucht werden»
  - [BKV TG § 4](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4.md) `tg-bkv__par-4` – «ein Abzug gemäss Ziff. 1 und Ziff. 2 ist nicht zulässig, wenn der Steuerpflichtige die entsprechende Leistung als Naturallohn erhält»

<a id="form-4-2-ziff-6-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 4.2 Ziff. 6 – Auslagen bei Nebenbeschäftigung: 20% vom Nettolohn, min. Fr. 800, max. Fr. 2'400, oder effektiv (Code 232; Person 2: 272)

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 des Nebenerwerbs; bei effektiven Kosten Aufstellung
- **Rein:** Lohnausweis Nebenerwerb → Nettolohn (Basis Pauschale) · Aufstellung effektive Kosten (Reihenfolge wie Haupterwerb) → nur statt Pauschale · Behördenentschädigungen (Funktionsentschädigung, Sitzungsgelder, Pauschalspesen) → Basis Behördenpauschale
- **Rechnen:** min(max(20 % × Nettoeinkünfte; Fr. 800); Fr. 2'400; Nebenerwerbseinkommen), Kanton = Bund; Behörde (Kanton): min(max(50 % × Entschädigungen; Fr. 2'000); Fr. 4'000)
- **Regel:** Pauschal 20% der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400 (Kanton und Bund), höchstens bis zur Höhe des Nebenerwerbseinkommens; deckt Fahrt-, Verpflegungs- und übrige Berufskosten (keine Kumulation mit effektiven Kosten). Behördenmitglieder (Exekutive Gemeinde/Schul-/Kirchgemeinde, volksgewählt, nebenamtlich): 50% der Entschädigungen, min. Fr. 2'000, max. Fr. 4'000. Haupterwerb kann auch mehrere Teilzeitanstellungen umfassen.
- **Beachten:** Pauschale deckt Fahrt-, Verpflegungs- und übrige Kosten; keine Kumulation mit effektiven Kosten
- **Beachten:** Behördenpauschale: nur volksgewählte Nebenamtliche der obersten kommunalen Exekutive (nicht Kommissionen/Parlamente)
- **Beachten:** Nebenerwerb setzt Haupterwerb voraus; einzige, auch geringfügige Tätigkeit gilt als Haupterwerb
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Nebenerwerb: Pauschale 20% der Nettoeinkünfte (statt effektiver Kosten, keine Kumulation); gilt auch beim Bund.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge))**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerbspauschale: Minimum CHF 800.)** · Bund **CHF 800 (Minimum Pauschale Nebenerwerb)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerbspauschale: Maximum CHF 2'400 (Nachweis höherer Kosten vorbehalten; maximal bis Höhe des Nebenerwerbseinkommens).)** · Bund **CHF 2'400 (Maximum Pauschale Nebenerwerb)**
- **Bund:** Gleiche Pauschale beim Bund.
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0005.md) `tg-form-04-2-2025__c0005` – «20% vom Nettolohn, mindestens Fr. 800.– und höchstens Fr. 2400.–»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0191.md) `tg-wl-2025__c0191` – «werden. Der Abzug beträgt 20% der Nettoeinkünfte, mindestens aber Fr. 800 und höchstens»
  - [WL TG 2025 S. 41](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0194.md) `tg-wl-2025__c0194` – «Der Pauschalabzug beträgt 50% von den insgesamt ausgerichteten Behördenentschädigungen»
  - [WL TG 2025 S. 41](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0193.md) `tg-wl-2025__c0193` – «Vom Volk gewählte, nebenamtlich tätige Mitglieder einer kommunalen Behörde, welche dem»
  - [WL TG 2025 S. 41](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0195.md) `tg-wl-2025__c0195` – «Mitglieder von Stadt- oder Gemeindeparlamenten»
  - [WL TG 2025 S. 41](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0192.md) `tg-wl-2025__c0192` – «Ein Nebenerwerb setzt das Vorliegen einer unselbständigen oder selbständigen»
  - [WL TG 2025 S. 41](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0192.md) `tg-wl-2025__c0192` – «betrachtet wird auch eine geringfügige Tätigkeit, sofern es sich um die einzige»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0174.md) `tg-wl-2025__c0174` – «Zweckmässigerweise erfolgt diese Aufstellung in der gleichen Reihenfolge der Ziffern»

<a id="form-4-2-ziff-7-berechnung-total"></a>
### Ziff. Form. 4.2 Ziff. 7 – Total der abzugsfähigen Berufsauslagen (Code 240; Person 2: 280) → Steuererklärung Ziff. 10.1 / 10.2

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 2.5, 3.1/3.2, 4, 5.1, 5.2, 6 (je Spalte Staat / Bund)
- **Rechnen:** Σ Ziff. 2.5 + 3.1/3.2 + 4 + 5.1 + 5.2 + 6 je Spalte → Formular 1 Ziff. 10.1 (Person 1) / 10.2 (Person 2); Staat links, Bund rechts
- **Regel:** Summe Ziff. 2.5 bis 6; Übertrag in Ziff. 10.1 (Person 1) bzw. 10.2 (Person 2), Spalten Staat/Bund getrennt.
- **Beachten:** Ziff. 2.5 (begrenzt), nicht 2.4 übernehmen
- **Beachten:** Person 2: eigenes Formular 4.3, wenn beide erwerbstätig
- **Beachten:** Pauschalen vorab auf die Erwerbsdauer umrechnen (unterjährige Erwerbstätigkeit)
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0005.md) `tg-form-04-2-2025__c0005` – «7.   Total der abzugsfähigen Berufsauslagen   240»
  - [WL TG 2025 S. 41](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0196.md) `tg-wl-2025__c0196` – «übertragen Sie diesen Betrag auf Seite 3 der Steuererklärung in die Ziffer 10.1»
  - [WL TG 2025 S. 41](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0196.md) `tg-wl-2025__c0196` – «in der linken Spalte für die Staats- und Gemeindesteuern und in die rechte»
  - [Formular 4.2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0006.md) `tg-form-04-2-2025__c0006` – «Berufsauslagen Person 2 Formular 4.3»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0174.md) `tg-wl-2025__c0174` – «Sind beide Eheleute bzw. Partnerinnen oder Partner in eingetragener Partnerschaft berufstätig»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0175.md) `tg-wl-2025__c0175` – «Die als Pauschalen ausgestalteten Berufsauslagen beziehen sich auf das ganze Jahr»
  - [WL TG 2025 S. 38–39](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0181.md) `tg-wl-2025__c0181` – «Liegt das Total der effektiven Fahrkosten in Ziffer 2.4 unter der Fahrkostenbeschränkung, ist in Ziffer 2.5 das Total der effektiven Fahrkosten einzutragen»
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0003.md) `tg-form-04-2-2025__c0003` – «3.2 mit Verbilligung durch Arbeitgeber/in oder Kantine»
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0004.md) `tg-form-04-2-2025__c0004` – «5.1 Unterkunft ortsübliche Auslagen für ein Zimmer 226»

## Hilfsblatt Versicherungsprämien

<a id="form-5-2-a-1-a-4-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 A.1–A.4 – Selbst getragene Prämien: private Krankenversicherung (netto nach Prämienverbilligung), private Unfallversicherung, Lebens-/Rentenversicherungen, erhaltene Sparzinsen

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Police Hausrat-/Privathaftpflichtversicherung (inkl. Gebäudeversicherung des Mieters/Mobiliar), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Jahresbestätigung Krankenkasse (Prämie abzüglich IPV), Prämienrechnungen Unfall/Leben/Rente, Zinsausweise Banken (Formular 2)
- **Rein:** Jahresbestätigung Krankenkasse → Prämie abzüglich 2025 erhaltener Prämienverbilligung (Zeile 1) · Prämienrechnungen private Unfall- (ohne NBUV) bzw. Lebens-/Rentenversicherung → Zeile 2 / Zeile 3 · Formular 2 / Zinsausweise Banken → 2025 erhaltene Sparzinsen (Zeile 4)
- **Rechnen:** Zeile 1 = KK-Prämien − IPV der Steuerperiode (inkl. EL-Prämienverbilligung, Nachzahlungen früherer Jahre); Zeilen 2–4 = effektiv 2025
- **Regel:** Ziff. 1: Nettoprämie = Krankenkassenprämie abzüglich in der Steuerperiode erhaltener Prämienverbilligungen (inkl. EL-Prämienverbilligung und Nachzahlungen früherer Jahre); Deklaration der KK-Prämien ist Voraussetzung des Abzugs. Ziff. 2: private Unfallversicherung (ohne NBUV → Ziff. 15.4). Ziff. 3: private Lebens-/Rentenversicherungen. Ziff. 4: im Jahr 2025 erhaltene Zinsen von Sparkapitalien (Bank/Post, Obligationen, Hypothekar-/Darlehensguthaben, gemäss Formular 2).
- **Beachten:** Deklaration der KK-Prämien ist Voraussetzung – sonst evtl. gar kein Versicherungsabzug
- **Beachten:** NBUV gehört in Ziff. 15.4 der Steuererklärung, nicht hier
- **Beachten:** Sparzinsen: Bank-/Postkonten, in- und ausländische Obligationen, Hypothekar- und Darlehensguthaben
- **Quellen:**
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0001.md) `tg-form-05-2-2025__c0001` – «1. private Krankenversicherung (netto, nach Abzug Prämienverbilligung gemäss Bestätigung Versicherung)»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0210.md) `tg-wl-2025__c0210` – «Tragen Sie in Ziffer 1 die selber bezahlten Einlagen, Prämien und Beiträge für die private Kran»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0209.md) `tg-wl-2025__c0209` – «Die Deklaration der Prämien der privaten Krankenversicherung wird vorausgesetzt»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0211.md) `tg-wl-2025__c0211` – «In Ziffer 2 zu deklarieren sind Prämien für die private Unfallversicherung (ausgenommen NBUV, vgl.»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0211.md) `tg-wl-2025__c0211` – «Die im 2025 erhaltenen Zinsen von Sparkapitalien (Bank- und Postkontoguthaben jeder Art, in- und»

<a id="form-5-2-a-5-a-6-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 A.5–A.6 – Krankentaggeldversicherung gemäss Lohnausweis; Total selbst getragene Versicherungsprämien und Sparzinsen (Code 324, Feld «A5»)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 (Hinweis Krankentaggeld-Beiträge)
- **Rein:** Lohnausweis → selbst getragene Krankentaggeld-Beiträge (Zeile 5) · Übertrag Zeilen 1–4 (Formular 5.2 A)
- **Rechnen:** Zeile 6 «A5» (Code 324) = Σ Zeilen 1–5
- **Regel:** Zusätzlich die dem Arbeitnehmer belasteten Krankentaggeld-Beiträge gemäss Lohnausweis eintragen (Lohnausweis weist sie ggf. in Ziff. 15 aus). Total ergibt «A5»/Code 324. Hinweis: Das Formular 2025 hat Zeilen 1–6 (Total in Zeile 6), die Wegleitung beschreibt noch das alte Schema 1–5/'A7'.
- **Beachten:** WL 2025 nennt Total in Ziff. 5 «A5» bzw. in Teil C «A7» – massgebend Formular 2025: Zeile 6 = «A5» (Code 324)
- **Beachten:** Zulässiger Abzug je Spalte = min(«A5»; «B4 Staat» bzw. «B4 Bund») → Code 330, Ziff. 14
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft. Zusätzlich: Zeilennummerierung Formular 5.2 (2025) vs. Wegleitung abweichend.
- **Quellen:**
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0001.md) `tg-form-05-2-2025__c0001` – «5. Krankentaggeldversicherung gemäss Lohnausweis»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0001.md) `tg-form-05-2-2025__c0001` – «6. Total selbst getragene Versicherungsprämien und Sparzinsen   324»
  - [WL Lohnausweis 2026 S. 14](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0034.md) `bund-wl-lohnausweis-2026__c0034` – «Arbeitnehmern belastete Beiträge an Krankentaggeldversicherungen sowie Prä»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0211.md) `tg-wl-2025__c0211` – «welches unter Ziffer 5 im Feld „A5“ einzutragen ist»
  - [WL TG 2025 S. 45](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0216.md) `tg-wl-2025__c0216` – «Tragen Sie den niedrigeren der unter „A7“ und „B4 Staat“ ermittelten Beträge»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0003.md) `tg-form-05-2-2025__c0003` – «der niedrigere Betrag von «A5» oder «B4 Staat»»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0003.md) `tg-form-05-2-2025__c0003` – «Übertrag in Steuererklärung Seite 3, Ziffer 14»
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «14. Versicherungsprämien und Zinsen von Sparkapitalien Formular 5 330»

<a id="form-5-2-b-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 B – Maximaler Abzug für Versicherungsprämien und Sparzinsen (Code 328; Feld «B4» Staat/Bund)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Zivilstand, Anzahl Kinder/unterstützte Personen, Beiträge Säule 2/3a)
- **Rein:** Formular 1 Seite 1 → Zivilstand / gemeinsame Besteuerung am Stichtag · Formular 1 Kinder-/Unterstützungsabzug → Anzahl berechtigter Kinder/unterstützter Personen · Formular 1 Ziff. 13 (Anschluss 2. Säule) / 3a-Bescheinigung → Beiträge Säule 2/3a geleistet? (nur Bund)
- **Rechnen:** B4 Staat = 7'000 bzw. 3'500 + 1'000 × Kinder/Unterstützte; B4 Bund = 3'700 bzw. 1'800 (ohne Säule 2/3a: 5'550 / 2'700) + 700 × Kinder/Unterstützte
- **Regel:** Staat: Fr. 7'000 gemeinsam besteuert / Fr. 3'500 übrige; Bund: Fr. 3'700 / Fr. 1'800 oder ohne Beiträge Säule 2/3a Fr. 5'550 / Fr. 2'700 (nur Bund); pro Kind und unterstützungsbedürftige Person mit Kinder-/Unterstützungsabzug zusätzlich Fr. 1'000 (Staat) bzw. Fr. 700 (Bund). Zuteilung bei getrennt besteuerten Eltern wie Kinderabzug (Kanton) bzw. nach Sorgerecht/Alimenten (Bund).
- **Beachten:** Abzug je Spalte = min(A-Total Code 324; B4) → Code 330, Ziff. 14
- **Beachten:** Bund-Ansatz ohne Säule 2/3a nicht zusätzlich zum ordentlichen Fr. 3'700 bzw. Fr. 1'800
- **Beachten:** Getrennte Eltern: Kanton beim Elternteil mit Kinderabzug / Bund (minderjährig) beim Empfänger der Unterhaltsbeiträge
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 7'000 (Versicherungsprämien und Sparzinsen, Verheiratete in ungetrennter Ehe: max. CHF 7'000 (inkl. eingetragene Partnerschaft).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 3'500 (Versicherungsprämien und Sparzinsen, übrige Steuerpflichtige: max. CHF 3'500.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag Versicherungsabzug: CHF 1'000 je minderjähriges oder in Ausbildung stehendes Kind bzw. unterstützte Person (mit Kinder-/Unterstützungsabzug).)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – Erhöhung für Personen ohne Beiträge an Säulen 2/3a gibt es nur bei der direkten Bundessteuer (CHF 5'550); kantonal kein separater Betrag.** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an Säule 2/3a (Erhöhung um die Hälfte))**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – Nur direkte Bundessteuer (CHF 2'700); kantonal kein separater Betrag.** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an Säule 2/3a)**
- **Bund:** Bund: 3'700 / 1'800 / ohne 2./3a 5'550 / 2'700 / Kind 700.
- **Quellen:**
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0002.md) `tg-form-05-2-2025__c0002` – «1. für gemeinsam besteuerte Personen (Eheleute / Partnerinnen oder Partner)   7000   3700»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0002.md) `tg-form-05-2-2025__c0002` – «3. für jedes Kind und für jede unterstützungsbedürftige Person, für die ein Kinder- oder»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0212.md) `tg-wl-2025__c0212` – «übrige steuerpflichtige Personen   Fr. 3'500   Fr. 1'800»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0003.md) `tg-form-05-2-2025__c0003` – «der niedrigere Betrag von «A5» oder «B4 Staat»»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0212.md) `tg-wl-2025__c0212` – «Diesen Abzug können Sie nicht zusammen mit dem ordentlichen Abzug von Fr. 3'700 bzw.»
  - [WL TG 2025 S. 44–45](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0213.md) `tg-wl-2025__c0213` – «Beachten Sie, dass unterschiedliche Zuteilungsregeln bei den Staats- und Gemeindesteuern und»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0001.md) `tg-form-05-2-2025__c0001` – «6. Total selbst getragene Versicherungsprämien und Sparzinsen 324»
  - [WL TG 2025 S. 44–45](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0214.md) `tg-wl-2025__c0214` – «Fliessen Unterhaltsbeiträge für minderjährige Kinder, steht der zusätzliche Versicherungsabzug für»
  - [WL TG 2025 S. 44–45](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0213.md) `tg-wl-2025__c0213` – «demjenigen Elternteil zugesprochen, welcher auch den Kinderabzug geltend machen kann»
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «Anschluss 2. Säule (PK)»
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «14. Versicherungsprämien und Zinsen von Sparkapitalien Formular 5 330»

<a id="form-5-2-c-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 C – Berechnung zulässiger Abzug: niedrigerer Betrag aus «A5» und «B4» (Code 330; Staat/Bund)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Form. 5.2 Feld «A5» (Code 324) → Total selbst getragene Prämien + Sparzinsen · Übertrag Form. 5.2 «B4 Staat» / «B4 Bund» (Code 328) → persönliches Maximum · Krankenkasse-Jahresbestätigung → Nettoprämie nach IPV (Basis Zeile A1)
- **Rechnen:** Kanton: min(A5; B4 Staat) / Bund: min(A5; B4 Bund) → Code 330 → Ziff. 14 (Spalten Staat/Bund)
- **Regel:** Staat: min(A5; B4 Staat), Bund: min(A5; B4 Bund); Übertrag in Ziff. 14.
- **Beachten:** B4 Kanton: 7'000 gemeinsam / 3'500 übrige + 1'000 je Kind/Unterstützte; Bund: 3'700 / 1'800 + 700
- **Beachten:** Bund ohne Beiträge Säule 2/3a: 5'550 / 2'700 anstelle (nicht zusätzlich zu) 3'700 / 1'800
- **Beachten:** A1 = KK-Prämie – 2025 erhaltene IPV (inkl. via EL, Nachzahlungen); ohne KK-Deklaration evtl. kein Abzug
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 7'000 (Versicherungsprämien und Sparzinsen, Verheiratete in ungetrennter Ehe: max. CHF 7'000 (inkl. eingetragene Partnerschaft).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 3'500 (Versicherungsprämien und Sparzinsen, übrige Steuerpflichtige: max. CHF 3'500.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag Versicherungsabzug: CHF 1'000 je minderjähriges oder in Ausbildung stehendes Kind bzw. unterstützte Person (mit Kinder-/Unterstützungsabzug).)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – Erhöhung für Personen ohne Beiträge an Säulen 2/3a gibt es nur bei der direkten Bundessteuer (CHF 5'550); kantonal kein separater Betrag.** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an Säule 2/3a (Erhöhung um die Hälfte))**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – Nur direkte Bundessteuer (CHF 2'700); kantonal kein separater Betrag.** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an Säule 2/3a)**
- **Quellen:**
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0003.md) `tg-form-05-2-2025__c0003` – «2. Bundessteuer: der niedrigere Betrag von «A5» oder «B4 Bund»   330»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0001.md) `tg-form-05-2-2025__c0001` – «6. Total selbst getragene Versicherungsprämien und Sparzinsen   324»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0002.md) `tg-form-05-2-2025__c0002` – «4. Total maximal Abzüge für Versicherungsprämien und Sparzinsen   328»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0212.md) `tg-wl-2025__c0212` – «für gemeinsam besteuerte Personen   Fr. 7'000   Fr. 3'700»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0212.md) `tg-wl-2025__c0212` – «Diesen Abzug können Sie nicht zusammen mit dem ordentlichen Abzug von Fr. 3'700 bzw.»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0210.md) `tg-wl-2025__c0210` – «die Nettoprämie (Krankenkassenprämie abzüglich allfälliger in der Steuerperiode erhaltener»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0210.md) `tg-wl-2025__c0210` – «Dazu zählen auch über Ergänzungsleistungen zur AHV und IV ausgerichtete»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0209.md) `tg-wl-2025__c0209` – «Bei fehlender Deklaration behält sich die Veranlagungsbehörde vor»

## Hilfsblatt Krankheitskosten

<a id="form-5-1-a-abzug-krankheitskosten"></a>
### Ziff. Form. 5.1 A – Aufwendungen: Selbstbehalt/Franchise, Arzt, Zahnarzt, Pflegepersonal, Spital/Heim, Therapien/Kur, Prothesen; getrennt Krankheits-/Unfallkosten und behinderungsbedingte Kosten

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Rechnungen und Kostenzusammenstellung der Krankenkasse (Selbstbehalt/Franchise); ärztliche Verordnung für Therapien/Kuren
- **Rein:** Krankenkasse: detaillierte Kostenzusammenstellung → Selbstbehalt/Franchise (A1) · Arzt-/Medikamenten-, Zahnarzt-, Pflege-, Spital-/Heimrechnungen → A2–A5 · Ärztliche Verordnung (Kopie) + Rechnung → Therapien/Kuren (A6) · Rechnungen Prothesen/Invalidenfahrzeug → A7; übrige Kosten gemäss Aufstellung → A8
- **Rechnen:** Σ selbst getragene Kosten A1–A8 = A9 (Total A), je Spalte «Krankheits-/Unfallkosten» bzw. «behinderungsbedingte Kosten»
- **Regel:** Nur selbst getragene Kosten; Belege geordnet beilegen. Ärztlich verordnete Therapien/Kuren: Kopie der Verordnung beilegen. Zahnarztkosten, Brillen, Apparate, Kuren abziehbar; nicht: Krankenkassenprämien, Fahrkosten zum Arzt (ausser dauernde Pflegebedürftigkeit), nicht verordnete Akupunktur, Prävention, Schönheit/Fitness, unentgeltliche Pflege durch Dritte. Kosten für Behinderung in die zweite Spalte.
- **Beachten:** Für sich + Personen mit Kinder-/Unterstützungsabzug; Zöliakie-Diät: Pauschale Fr. 2'500 statt effektiv (nicht Diabetes)
- **Beachten:** Spalte behinderungsbedingt nur bei Behinderung (IV-Leistungen, Hilflosenentschädigung, Heim/Spitex ≥ 60 Min./Tag)
- **Beachten:** Nicht: KK-Prämien, Arztfahrten (ausser dauernd pflegebedürftig), unverordnete Akupunktur, Prävention, Fitness
- **Quellen:**
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0001.md) `tg-form-05-1-2025__c0001` – «1. Selbstbehalt / Franchise gemäss detaillierter Kostenzusammenstellung der Krankenkasse»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0205.md) `tg-wl-2025__c0205` – «Tragen Sie auf der Vorderseite von Formular 5 unter A die Aufwendungen, aufgeteilt in „Krankheits»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0197.md) `tg-wl-2025__c0197` – «Krankheitskosten eine Pauschale von Fr. 2'500 geltend machen»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0197.md) `tg-wl-2025__c0197` – «An Diabetes erkrankte Personen»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0197.md) `tg-wl-2025__c0197` – «Kinder- oder Unterstützungsabzug geltend machen können, in Abzug bringen»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0199.md) `tg-wl-2025__c0199` – «60 Minuten pro Tag anfällt. Dieser Pflege- und Betreuungsaufwand wird»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0203.md) `tg-wl-2025__c0203` – «Ebenfalls nicht abziehen können Sie die Fahrkosten zum Arzt, Zahnarzt, Spital usw., ausgenommen»

<a id="form-5-1-b-abzug-krankheitskosten"></a>
### Ziff. Form. 5.1 B – Vergütungen Dritter und Anteil Lebenshaltungskosten (Krankenkasse, Versicherungen, Hilflosenentschädigung, Lebenshaltungskosten)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Leistungsabrechnungen Krankenkasse/Versicherung; Bescheide IV/AHV/SUVA (Hilfsmittel, Hilflosenentschädigung)
- **Rein:** Krankenkasse-Leistungsabrechnung → vergütete Kosten (B1) · Versicherungsabrechnung inkl. Pflegefinanzierung → B2 · Verfügungen AHV/IV/MV/SUVA → Hilflosenentschädigung (B3), Beiträge an Hilfsmittel · Heim-/Kurrechnung → Anteil Lebenshaltungskosten Ernährung/Unterkunft (B4)
- **Rechnen:** Σ B1–B5 = B6 (Total B), je Spalte Krankheits-/Unfallkosten bzw. behinderungsbedingt; nur soweit nicht schon in A abgezogen
- **Regel:** Von den Aufwendungen abziehen: Krankenkassen-/Versicherungsleistungen (inkl. Pflegefinanzierung), Hilflosenentschädigung AHV/IV/SUVA, Beiträge an Hilfsmittel und ein Anteil Lebenshaltungskosten (z.B. Ernährung/Unterkunft bei Kur oder Heim).
- **Beachten:** Behinderungsbedingter Heimaufenthalt: Lebenshaltungsanteil i.d.R. Fr. 2 000 pro Monat
- **Beachten:** WL-Beispiel: KK 700 + Kur-Lebenshaltung 600 = 1'300 (Krankheit); IV an Prothese 2'500 (behinderungsbedingt)
- **Beachten:** Abzuziehen auch Hilflosenrenten SUVA und Leistungen der Pflegefinanzierung
- **Quellen:**
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0002.md) `tg-form-05-1-2025__c0002` – «3. Hilflosenentschädigung AHV/IV/SUVA»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0203.md) `tg-wl-2025__c0203` – «Die von Krankenkassen, Versicherungen oder Dritten vergüteten Kosten, Beiträge der AHV, IV, MV»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0201.md) `tg-wl-2025__c0201` – «in der Regel Fr. 2 000 pro Monat»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0207.md) `tg-wl-2025__c0207` – «Vergütungen der Krankenkasse   Fr.   700»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0207.md) `tg-wl-2025__c0207` – «Beteiligung IV an Prothese   Fr. 2'500»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0207.md) `tg-wl-2025__c0207` – «Lebenshaltungskostenanteil Kuraufenthalt   Fr. 600»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0207.md) `tg-wl-2025__c0207` – «Total Abzüge (B)   Fr. 1'300   Fr. 2'500»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0204.md) `tg-wl-2025__c0204` – «(z.B. für Ernährung/Unterkunft).»

<a id="form-5-1-c-abzug-behinderungskosten"></a>
### Ziff. Form. 5.1 C – Berechnung behinderungsbedingte Kosten (A–B) (Code 350) → Ziff. 17

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Form. 5.1 A9, Spalte behinderungsbedingte Kosten (Total A) · Übertrag Form. 5.1 B6, Spalte behinderungsbedingte Kosten (Total B) · Verfügung Hilflosenentschädigung (Grad) / Nachweis Gehörlosigkeit bzw. Dialyse → Pauschale
- **Rechnen:** A – B (Spalte behinderungsbedingt) = Code 350 → Ziff. 17, ohne Selbstbehalt (WL-Bsp. 3'000 – 2'500 = 500); alternativ Pauschale 2'500 / 5'000 / 7'500
- **Regel:** Total Aufwendungen behinderungsbedingte Kosten (A) minus Vergütungen (B); Übertrag Ziff. 17. Alternativ Pauschalen (Fr. 2'500/5'000/7'500).
- **Beachten:** Pauschale statt effektiv: gehörlos, Dialyse, Hilflosenentschädigung leicht 2'500; mittel 5'000; schwer 7'500
- **Beachten:** Behinderungsbedingter Heimaufenthalt: Lebenshaltungsanteil (i.d.R. Fr. 2 000/Monat) in B abziehen
- **Beachten:** Krankheitskosten einer behinderten Person nicht hier, sondern in D (5% Selbstbehalt)
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5% des Nettoeinkommens (Ziff. 22 der Steuererklärung).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Quellen:**
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0003.md) `tg-form-05-1-2025__c0003` – «Abzugsfähige behinderungsbedingte Kosten   350»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0205.md) `tg-wl-2025__c0205` – «vom Total A das Total B ab. Die so ermittelten abzugsfähigen behinderungsbedingten Kosten über»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0202.md) `tg-wl-2025__c0202` – «Bezügerinnen/Bezüger einer Hilflosenentschädigung schweren Grades   Fr. 7'500»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0198.md) `tg-wl-2025__c0198` – «welche Sie einen Kinder- oder Unterstützungsabzug geltend machen können, vollständig von den»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0201.md) `tg-wl-2025__c0201` – «Solche Kosten können auch von einer behinderten Person nur insoweit abgezogen»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0201.md) `tg-wl-2025__c0201` – «in der Regel Fr. 2 000 pro Monat»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0207.md) `tg-wl-2025__c0207` – «Total behinderungsbedingte Kosten (Ziff. 17)   Fr. 500»

<a id="form-5-1-d-abzug-krankheitskosten"></a>
### Ziff. Form. 5.1 D – Berechnung Krankheits- und Unfallkosten: (A–B) abzüglich 5% Selbstbehalt von Ziff. 22 (Code 364; Staat/Bund) → Ziff. 23.1

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Nettoeinkommen Ziff. 22 je Spalte)
- **Rein:** Übertrag Form. 5.1 A9 / B6, Spalte Krankheits- und Unfallkosten · Steuererklärung Ziff. 22 Nettoeinkommen (linke Spalte Staat, rechte Spalte Bund)
- **Rechnen:** (A – B) – 5% × Nettoeinkommen Ziff. 22 = Code 364 → Ziff. 23.1; Kanton: Ziff. 22 links / Bund: Ziff. 22 rechts
- **Regel:** Total Aufwendungen minus Vergütungen minus 5% des Nettoeinkommens Ziff. 22 – Staat mit linker, Bund mit rechter Spalte von Ziff. 22 (Beispiel WL: Netto 40'000 → 2'000; Bund 44'000 → 2'200).
- **Beachten:** WL-Beispiel: 9'900 – 1'300 = 8'600; Staat – 2'000 (Netto 40'000) = 6'600; Bund – 2'200 (Netto 44'000) = 6'400
- **Beachten:** Nachweis der geltend gemachten Kosten mit der Steuererklärung einreichen
- **Beachten:** Auch Krankheitskosten Behinderter gehören hierher (mit Selbstbehalt), nicht zu den behinderungsbedingten Kosten
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5% des Nettoeinkommens (Ziff. 22 der Steuererklärung).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Quellen:**
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0004.md) `tg-form-05-1-2025__c0004` – «Abzugsfähige Krankheits- und Unfallkosten   364»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0206.md) `tg-wl-2025__c0206` – «dasjenige für die direkte Bundessteuer aus der rechten Spalte.»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0208.md) `tg-wl-2025__c0208` – «Abzug Krankheits- und Unfallkosten (Ziff. 23.1)   Fr. 6'600   Fr. 6'400»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0208.md) `tg-wl-2025__c0208` – «Annahme: Nettoeinkommen (Ziff. 22) direkte Bundessteuer Fr. 44'000»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0201.md) `tg-wl-2025__c0201` – «Solche Kosten können auch von einer behinderten Person nur insoweit abgezogen»

## Hilfsblatt Schulden

<a id="form-4-1-a-schulden-privat"></a>
### Ziff. Form. 4.1 A – Privatschulden: Gläubiger/in mit Adresse, Zinssatz, Schuld am 31.12.2025, fällige Schuldzinsen (Codes 455 / 286)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Kreditkartenabrechnung (Monats-/Jahresabrechnung, Karten-Jahresgebühr) → Bank-/Gläubigerbestätigung per 31.12.2025 (Schuld, Zinssatz, im Jahr fällig gewordene Zinsen)
- **Rein:** Bank-/Hypothekarbestätigung → Schuld 31. Dezember, Zinssatz, 2025 fällige Zinsen · Darlehensvertrag/Zinsbestätigung privater Gläubiger → Gläubiger mit Adresse, Zinssatz, Zinsen · Kreditkarten-/Konsumkreditabrechnung → Saldo 31. Dezember, belastete Zinsen · Steuer-Schlussrechnung → 2025 belastete Ausgleichszinsen
- **Rechnen:** Σ Schulden 31. Dezember = Code 455; Σ 2025 fällige Zinsen (– WEF-Zusatzverbilligung) = Code 286; privat max. Vermögensertrag + 50'000 (Kanton und Bund)
- **Regel:** Gläubiger mit genauer Adresse und Zinssatz sind unerlässlich. Nur 2025 fällig gewordene Zinsen (keine Ratazinsen); Amortisationen, Bau-/Landkreditzinsen und Leasingzinsen sind keine abziehbaren Schuldzinsen. WEF-Zusatzverbilligung als Zinsminderung. Totale: Schulden Code 455, Zinsen Code 286.
- **Beachten:** Nur 2025 fällige Zinsen, keine Ratazinsen; nicht: Amortisationen, Bau-/Landkreditzinsen (Bauphase), Leasingzinsen
- **Beachten:** Baurechtszinsen nur bei Fremdvermietung; mit Steuerschlussrechnung 2025 belastete Ausgleichszinsen abziehbar
- **Beachten:** Gläubiger mit genauer Adresse + Zinssatz zwingend; WEF-Zusatzverbilligung (selbstbewohnt) als Zinsminderung
- **Quellen:**
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0001.md) `tg-form-04-1-2025__c0001` – «Total Privatschulden   455   286»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0171.md) `tg-wl-2025__c0171` – «Unerlässlich ist insbesondere die Angabe der Gläubigerin bzw. des Gläubigers»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0172.md) `tg-wl-2025__c0172` – «Die im 2025 mit der Steuerschlussrechnung belasteten Ausgleichszinsen können Sie ebenfalls als»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0172.md) `tg-wl-2025__c0172` – «Tragen Sie nur die im Jahre 2025 fällig gewordenen Schuldzinsen ein (keine Ratazinsen).»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0172.md) `tg-wl-2025__c0172` – «Bei selbstbewohntem Wohneigentum sind erhaltene Zusatzverbilligungen nach dem Gesetz über»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «Sie können private Schuldzinsen höchstens im Umfang der deklarierten Erträge aus beweglichem»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «Bezahlte Baurechtszinsen sind nur bei Fremdvermietung der Liegenschaft»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «Leasingzinsen sind grundsätzlich nicht abzugsfähig.»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken»
  - [KS 36 S. 7–8](../../chunks/bund/dauernd/bund-ks-36/bund-ks-36__c0023.md) `bund-ks-36__c0023` – «des Bruttovermögensertrags und weiterer 50'000 Franken abziehbar»

<a id="form-4-1-b-schulden-privat"></a>
### Ziff. Form. 4.1 B – Geschäftsschulden und zugehörige Schuldzinsen (Codes 460 / 288)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz / Schuldenaufstellung Geschäft
- **Rein:** Bilanz/Jahresrechnung Geschäft → Geschäftsschulden per 31. Dezember · Erfolgsrechnung/Bankbelege → 2025 fällige Geschäftsschuldzinsen
- **Rechnen:** Σ Geschäftsschulden 31. Dezember = Code 460; Σ Geschäftsschuldzinsen, soweit nicht schon im Einkommen Ziff. 2 abgezogen = Code 288
- **Regel:** Geschäftsschuldzinsen hier nur, wenn nicht bereits im Einkommen Ziff. 2 abgezogen. Totale: Schulden Code 460, Zinsen Code 288.
- **Beachten:** Doppelabzug vermeiden: bereits in der Erfolgsrechnung (Ziff. 2) abgezogene Zinsen hier weglassen
- **Beachten:** Bund: Geschäftszinsen unbeschränkt; Abgrenzung privat/geschäftlich nach Mittelverwendung, sonst nach Aktiven
- **Beachten:** Auch hier Gläubiger mit genauer Adresse und Zinssatz angeben
- **Quellen:**
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0001.md) `tg-form-04-1-2025__c0001` – «Total Geschäftsschulden   460   288»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «Tragen Sie Schuldzinsen aus selbständiger Erwerbstätigkeit hier nur ein, sofern Sie diese nicht»
  - [KS 36 S. 7–8](../../chunks/bund/dauernd/bund-ks-36/bund-ks-36__c0023.md) `bund-ks-36__c0023` – «geschäftlichen Schuldzinsen unbeschränkt zum Abzug zugelassen.»
  - [KS 36 S. 7–8](../../chunks/bund/dauernd/bund-ks-36/bund-ks-36__c0023.md) `bund-ks-36__c0023` – «Nachweis der Mittelverwendung, erfolgt die Abgrenzung nach dem Verhältnis der Aktiven»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0171.md) `tg-wl-2025__c0171` – «Unerlässlich ist insbesondere die Angabe der Gläubigerin bzw. des Gläubigers»

<a id="form-4-1-c-schulden-privat"></a>
### Ziff. Form. 4.1 C – Zusammenzug Privat- und Geschäftsschulden (Code 466) und Schuldzinsen (Code 290)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Form. 4.1 A → Codes 455 / 286 · Übertrag Form. 4.1 B → Codes 460 / 288
- **Rechnen:** Schulden: 455 + 460 = Code 466 → Ziff. 34 (S. 4); Zinsen: 286 + 288 = Code 290 → Ziff. 11 (S. 3)
- **Regel:** Total Schulden (Code 466) → Steuererklärung Ziff. 34 (Seite 4); Total Schuldzinsen (Code 290) → Ziff. 11 (Seite 3).
- **Beachten:** Private Schuldzinsen in Ziff. 11 max. Vermögensertrag + 50'000 (Kanton und Bund)
- **Beachten:** Geschäftszinsen, die schon im Einkommen Ziff. 2 abgezogen sind, nicht nochmals in Ziff. 11
- **Quellen:**
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0002.md) `tg-form-04-1-2025__c0002` – «Total Privat- und Geschäftsschulden   466   290»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «Sie können private Schuldzinsen höchstens im Umfang der deklarierten Erträge aus beweglichem»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «Tragen Sie Schuldzinsen aus selbständiger Erwerbstätigkeit hier nur ein, sofern Sie diese nicht»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken»
  - [KS 36 S. 7–8](../../chunks/bund/dauernd/bund-ks-36/bund-ks-36__c0023.md) `bund-ks-36__c0023` – «des Bruttovermögensertrags und weiterer 50'000 Franken abziehbar»

## Hilfsblatt Wertschriftenverzeichnis

<a id="form-2-spalten-7-9-einkommen-wertschriften"></a>
### Ziff. Form. 2 Spalten 7–9 – Detailverzeichnis Wertschriften und Guthaben: Steuerwert 31.12. (Spalte 7), Bruttoertrag mit Verrechnungssteuerabzug (Spalte 8, A), ohne (Spalte 9, B)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Steuerauszug/Depotverzeichnis der Bank; Zins- und Kapitalbescheinigungen (Bruttozins, Verrechnungssteuer, Kontostand 31.12.); E-Steuerauszug
- **Rein:** Steuerauszug/Depotverzeichnis Bank → Steuerwert 31.12. (Sp. 7), Bruttoerträge mit/ohne VSt (Sp. 8/9) · Zins-/Kapitalbescheinigung Konti → Saldo 31.12., Bruttozins · Auszahlungsbordereau Auslandstitel → Nettoertrag + rückforderbare/anrechenbare Quellensteuer; DA-1 · Lotterie-Auszahlungsbescheinigung (Original) → Gewinn Sp. 8 bzw. 9
- **Rechnen:** Je Titel: Sp. 7 = Steuerwert 31.12.2025 (Kurs Ende Dezember / ESTV-Kursliste); Sp. 8 = Bruttoertrag mit VSt (Fr. mit Rappen); Sp. 9 = Ertrag ohne VSt
- **Regel:** Je Titel/Konto: Bezeichnung mit Valoren-/ISIN-Nr., Steuerwert per 31.12.2025 (Spalte 7), Bruttoertrag. Spalte 8 (A): Erträge MIT Verrechnungssteuerabzug (CH-Dividenden/Zinsen, Bankkonti über Fr. 200 Bruttozins oder mehrere Gutschriften, Lotterietreffer über Fr. 1'000 usw.; Franken und Rappen). Spalte 9 (B): Erträge OHNE Verrechnungssteuer (Konti ≤ Fr. 200, ausländische Wertschriften, Darlehen/Hypotheken). Codes für Geschäftsvermögen (02), Nutzniessung (01), qualifizierte Beteiligung (05/06), Erbschaft/Schenkung (03/04). Ausländische Erträge: netto + anrechenbare Quellensteuer; DA-1 für Anrechnung/USA-Rückbehalt. Zugang/Abgang mit Datum. Kinder unter elterlicher Sorge (Jahrgang 2008 und jünger) mitdeklarieren.
- **Beachten:** Sp. 8: CH-Dividenden/-Zinsen, Konti mit Bruttozins > Fr. 200 oder mehreren Gutschriften, Lotterietreffer > Fr. 1'000
- **Beachten:** Sp. 9: Konti ≤ Fr. 200, Darlehen, alle Auslandstitel (netto + rückforderbare QSt); DA-1-Anrechnung erst > Fr. 100
- **Beachten:** Kinder Jahrgang 2008 und jünger mitdeklarieren; PK-, Freizügigkeits-, Säule-3a-Guthaben nicht aufführen
- **Quellen:**
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0005.md) `tg-form-02-2025__c0005` – «Detailverzeichnis Wertschriften und Guthaben»
  - [WL TG 2025 S. 32](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0153.md) `tg-wl-2025__c0153` – «In der Spalte 9 „Erträge ohne Verrechnungssteuerabzug“ aufzuführen sind auch Erträge inländi»
  - [WL TG 2025 S. 32](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0153.md) `tg-wl-2025__c0153` – «Bank- und Postkonti aller Art, deren Bruttozins im Kalenderjahr Fr. 200 nicht übersteigt und»
  - [WL TG 2025 S. 32](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0151.md) `tg-wl-2025__c0151` – «im Inland ausgerichtete Geld- und Naturaltreffer von über Fr. 1'000 aus Lotterien»
  - [WL TG 2025 S. 33](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0155.md) `tg-wl-2025__c0155` – «Wenn die Steueranrechnung (DA-1, Spalte 11) insgesamt den Betrag von Fr. 100 nicht übersteigt,»
  - [WL TG 2025 S. 33](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0155.md) `tg-wl-2025__c0155` – «zuzüglich ausländischer Quellensteuern, soweit sie aufgrund eines»
  - [WL TG 2025 S. 30](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0139.md) `tg-wl-2025__c0139` – «Vermögen und Erträge von Kindern unter Ihrer elterlichen Sorge (Jahrgang 2008 und jünger)»
  - [WL TG 2025 S. 30](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0139.md) `tg-wl-2025__c0139` – «sind bis zur Fälligkeit der Leistungen steuerfrei und daher vor deren Fälligkeit»
  - [WL TG 2025 S. 30–31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0143.md) `tg-wl-2025__c0143` – «Für in der Schweiz kotierte Wertpapiere gilt der Börsenkurs Ende des Monats Dezember 2025.»
  - [WL TG 2025 S. 32](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0152.md) `tg-wl-2025__c0152` – «Legen Sie bei den Lotterietreffern aller Art die Auszahlungsbescheinigung im Original bzw. den»

<a id="form-2-ziff-10-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 2 Ziff. 10 – Verrechnungssteueranspruch: 35% von Bruttoertrag Total A (Rückerstattungsantrag)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2 Ziff. 10; Unterschrift Rückerstattungsantrag; Auszahlungskonto Formular 1 Seite 1
- **Rein:** Übertrag Form. 2 Ziff. 3 Zwischentotal I, Spalte 8 (inkl. Beiblätter) · Formular 1 S. 1 → Auszahlungskonto (bei Erstantrag/Kontoänderung) · Bank-Steuerauszug (statt Detailangaben) → Bestandteil des Antrags
- **Rechnen:** VSt-Anspruch = 35% × Σ Bruttoerträge Sp. 8 (Total I, Ziff. 3 inkl. Beiblätter) → Form. 2 Ziff. 10
- **Regel:** 35% des Totals der Erträge Spalte 8 (Zwischentotal I). Rückerstattung nur bei Wohnsitz im Kanton TG am 31.12.2025 und vollständiger Deklaration der Erträge; unter Vorbehalt des Rückforderungsrechts der ESTV. Erträge unverteilter Erbschaften nach Erbquote in Spalte A (mit VSt) bzw. B. Wertschriftenverzeichnis zu unterzeichnen.
- **Beachten:** Nur bei Wohnsitz TG am 31. Dezember 2025 und Deklaration der Erträge; Auszahlung unter Rückforderungsvorbehalt ESTV
- **Beachten:** Grossspielgewinne: VSt-belasteter Teil in Sp. A, nur kantonal steuerbarer Teil in Sp. B (WL: 929'600 / 70'400)
- **Beachten:** STWEG-Betriebs-/Erneuerungsfonds nicht aufführen (Gemeinschaft beantragt mit Formular 25 bei ESTV)
- **Quellen:**
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0006.md) `tg-form-02-2025__c0006` – «10. Verrechnungssteueranspruch: 35% von Bruttoertrag Total A»
  - [WL TG 2025 S. 35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0167.md) `tg-wl-2025__c0167` – «Vom Total I der Bruttoerträge 2025»
  - [WL TG 2025 S. 35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0168.md) `tg-wl-2025__c0168` – «Steuerauszüge von Banken, die anstelle von detaillierten Angaben im Formular 2 eingereicht»
  - [WL TG 2025 S. 35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0168.md) `tg-wl-2025__c0168` – «erfolgt daher unter Vorbehalt des Rückforderungsrechtes»
  - [WL TG 2025 S. 32](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0150.md) `tg-wl-2025__c0150` – «Fr. 929'600 in der Spalte A (Erträge mit Verrechnungssteuer)»
  - [WL TG 2025 S. 35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0169.md) `tg-wl-2025__c0169` – «mit dem Formular 25 bei der Eidg.»

<a id="form-2-verm-gensverwaltungskosten-code-148-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. Form. 2 Vermögensverwaltungskosten (Code 148) – Vermögensverwaltungskosten (Code 148; im Formular als Ziffer 17 bzw. Wegleitung Ziffer 7)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.) → Depotgebührenausweis der Bank; bei Nachweis höherer Kosten Belege
- **Rein:** Steuerauszug/Depotverzeichnis → Steuerwert der durch Dritte verwalteten Wertschriften PV (Bemessung) · Depotgebühren-/Verwaltungskostenausweis Bank → effektive Kosten (falls höher)
- **Rechnen:** Kanton: min(2 Promille × Steuerwert drittverwalteter Wertschriften PV; 6'000) oder höhere nachgewiesene Kosten → Code 148 (Zeile 7), vom Bruttoertrag ab
- **Regel:** Pauschal 2 Promille des Steuerwerts der durch Dritte verwalteten Wertschriften des Privatvermögens, max. Fr. 6'000; Darlehen, Bankguthaben und nicht kotierte qualifizierte Beteiligungen zählen nicht zur Bemessung. Nachweis höherer Kosten vorbehalten. Nur Depotgebühren/Verwaltung – nicht Kontoführung, Anlageberatung, Kommissionen/Spesen An-/Verkauf, Tresormiete.
- **Beachten:** Bemessung ohne Darlehen, Bankguthaben und nicht kotierte qualifizierte Beteiligungen (§ 22 Abs. 2 StG)
- **Beachten:** Nicht abziehbar: Kontoführung, Anlageberatung, Kommissionen/Spesen An-/Verkauf, Tresor-/Schrankfachmiete
- **Beachten:** Zeile 7 gemäss WL (PDF-Text zeigt «17.»); Ertrag nach Abzug via Ziff. 9 → Steuererklärung Ziff. 4
- **Bemerkung:** Zifferbezeichnung im Formular 2 (2025) in der PDF-Extraktion unklar ('17.'); Wegleitung nennt 'Ziffer 7' – Code 148 ist massgebend.
- **Quellen:**
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0006.md) `tg-form-02-2025__c0006` – «17. Vermögensverwaltungskosten   Code 148»
  - [WL TG 2025 S. 33–34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0159.md) `tg-wl-2025__c0159` – «Der Pauschalabzug beträgt maximal Fr. 6'000.»
  - [StV TG § 10a](../../chunks/tg/2025/tg-stv/tg-stv__par-10a.md) `tg-stv__par-10a` – «pauschal 2 Promille des Steuerwertes der durch Dritte verwalteten Wertschriften des Privatvermögens, maximal Fr. 6'000»
  - [WL TG 2025 S. 33–34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0160.md) `tg-wl-2025__c0160` – «Nicht abziehen können Sie Auslagen im Zusammenhang mit der Anlage von Vermögenswerten»

<a id="form-2-einsatzkosten-geldspiele-code-145-einkommen-wertschriften"></a>
### Ziff. Form. 2 Einsatzkosten Geldspiele (Code 145) – Einsatzkosten für steuerbare Gewinne aus Geldspielen (Code 145; im Formular Ziffer 18 bzw. Wegleitung Ziffer 8/9)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Gewinnbescheinigung / Auszahlungsbelege
- **Rein:** Gewinnbescheinigung / VSt-Ausweis (beilegen) → steuerbarer Einzelgewinn · Auszug Online-Spielerkonto (Spielbank) → im Steuerjahr abgebuchte Spieleinsätze
- **Rechnen:** Lotterie/Grossspiel: Σ min(5% × steuerbarer Einzelgewinn; Kanton 5'000 / Bund 5'400); Online-Spielbank: min(Einsätze; Kanton 25'000 / Bund 26'800) → Code 145
- **Regel:** Pauschal 5% pro steuerbarem Gewinn, max. Fr. 5'000 je Gewinn (Staat; Bund Fr. 5'400 – Korrektur von Amtes wegen); effektive Einsatzkosten nicht möglich. Online-Spielbank: abgebuchte Spieleinsätze, max. Fr. 25'000 (Bund Fr. 26'800). In der Steuererklärung Staatsmaximum deklarieren. Einsatzkosten für nicht steuerbare Gewinne nicht abziehbar.
- **Beachten:** Deklariert wird das Staatsmaximum; Bund korrigiert die Steuerverwaltung von Amtes wegen
- **Beachten:** Grossspiel/Online-Spielbank: steuerbar Teil > 1'000'000 (Bund 1'070'400); Lotterie Verkaufsförd. > 1'000 (Bund 1'100)
- **Beachten:** Effektive Einsatzkosten nicht abziehbar
- **Limiten:**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'000'000 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen nach BGS steuerfrei bis CHF 1'000'000 (Kanton); Bund CHF 1'070'400.)** · Bund **CHF 1'070'400 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'070'400)**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'000 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'000 (Kanton; Bund CHF 1'100). Gewinne über der Grenze sind voll steuerbar.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'100)**
- **Bund:** Bund: Pauschale max. Fr. 5'400 (Online-Spielbank Fr. 26'800); Kanton Fr. 5'000 / Fr. 25'000.
- **Bemerkung:** Ziffernbezeichnung im Formular 2 in der PDF-Extraktion unklar; Wegleitung nennt Ziffer 8 bzw. 9. Code 145 massgebend.
- **Quellen:**
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0006.md) `tg-form-02-2025__c0006` – «18. Einsatzkosten und Spieleinsätze für steuerbare Gewinne aus Geldspielen»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0161.md) `tg-wl-2025__c0161` – «Formulars geltend machen. Von jedem einzelnen steuerbaren Gewinn können pauschal fünf Pro»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0162.md) `tg-wl-2025__c0162` – «Staats- und Gemeindesteuern Fr. 25'000 und bei der direkten Bundessteuer Fr. 26'800.»
  - [WL TG 2025 S. 31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0146.md) `tg-wl-2025__c0146` – «Bei der direkten Bundessteuer beträgt die Steuerfreigrenze Fr. 1'100.»
  - [WL TG 2025 S. 31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0148.md) `tg-wl-2025__c0148` – «Steuerbar ist nur der Anteil des Einzelgewinns, welcher den Steuerfreibetrag übersteigt.»
  - [WL TG 2025 S. 31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0147.md) `tg-wl-2025__c0147` – «Sobald ein einzelner Gewinn die Steuerfreigrenze übersteigt, ist der gesamte Gewinn steuerbar.»
  - [WL TG 2025 S. 30](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0142.md) `tg-wl-2025__c0142` – «Verrechnungssteuerausweise für allfällige Ge-»
  - [WL TG 2025 S. 4](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0002.md) `tg-wl-2025__c0002` – «5% pro steuerbaren Gewinn (Swisslotto, Toto, Lotterien etc.) max. Fr. 5'000»
  - [VKP Art. 3](../../chunks/bund/2025/bund-vkp-2025/bund-vkp-2025__art-3-t4.md) `bund-vkp-2025__art-3-t4` – «werden 5 Prozent, jedoch höchstens 5400 Franken, als Einsatzkosten abgezogen»

<a id="form-2-hilfsblatt-qualifizierte-beteiligungen-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. Form. 2 Hilfsblatt qualifizierte Beteiligungen – Hilfsblatt qualifizierte Beteiligungen im Privatvermögen: Name/Sitz, Beteiligungsquote (ab 10%), Beteiligungsertrag; Teilbesteuerungsabzug Staat 40% / Bund 30%

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Dividendenabrechnung/Bescheinigung; Nachweis Beteiligungsquote ≥ 10%
- **Rein:** Dividendenabrechnung / Ausschüttungsbeleg → Beteiligungsertrag 2025 je Gesellschaft · Aktienbuch/Steuerauszug → Nachweis Beteiligungsquote ≥ 10% · Form. 2 Sp. 8/9 → dort deklarierte Beteiligungserträge
- **Rechnen:** Σ Erträge aus Beteiligungen ≥ 10% = Ziff. 2; Abzug Ziff. 3 = Kanton 40% / Bund 30% × Ziff. 2 → Ziff. 15.6
- **Regel:** Pro Gesellschaft Name/Sitz, Quote und im Jahr 2025 erzielten Beteiligungsertrag eintragen; Total Ziff. 2 × 40% (Staat) bzw. 30% (Bund) = Abzug Ziff. 3 → Steuererklärung Ziff. 15.6. Antrag jährlich nötig. Beteiligungen im Geschäftsvermögen: Formular 14.
- **Beachten:** Erträge zuerst voll in Form. 2 Sp. 8/9 deklarieren; Ergebnis: steuerbar Kanton 60% / Bund 70%
- **Beachten:** Antrag jeweils neu nötig; ohne Nachweis der Voraussetzungen Besteuerung zu 100%
- **Beachten:** Beteiligungen im Geschäftsvermögen nicht hier (Antrag im Fragebogen Selbständigerwerbende, S. 4)
- **Quellen:**
  - [Formular 2 TG 2025 S. 4](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0008.md) `tg-form-02-2025__c0008` – «Hilfsblatt qualifizierte Beteiligungen im Privatvermögen»
  - [WL TG 2025 S. 34–35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0166.md) `tg-wl-2025__c0166` – «Der Antrag auf die Durchführung des Teilbesteuerungsverfahrens für Erträge aus Beteiligungen im»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0164.md) `tg-wl-2025__c0164` – «ten Beteiligungen sind kantonal zu 60% und beim Bund zu 70% steuerbar.»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0164.md) `tg-wl-2025__c0164` – «Bei fehlendem Nachweis erfolgt die Besteuerung zu 100%»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0165.md) `tg-wl-2025__c0165` – «Die Erträge aus qualifizierten Beteiligungen im Privatvermögen sind grundsätzlich in Spalte 8»

## Hilfsblatt Liegenschaften

<a id="form-7-steuerwert-mietwert-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 7 Steuerwert / Mietwert – Angaben zur Liegenschaft: Steuerwert; Mietwert selbstgenutzt, Selbstnutzungsabzug, steuerbarer Eigenmietwert (Staatssteuer / Bundessteuer)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftensteuerrechnung (Januar des Folgejahres: Steuerwert, indexierter Mietwert) / Schätzungsverfügung
- **Rein:** Liegenschaftensteuerrechnung 2026 (Versand Januar 2026) → Grundstücksdaten, indexierter Mietwert 2025 · Rechtskräftige Liegenschaftenschätzung → amtlicher Verkehrswert (Steuerwert), Mietwert aus Selbstnutzung · Ausserkantonal/Ausland: dort gültiger Steuerwert · Grundbuchauszug/Kauf-, Schenkungs-, Erbunterlagen → Anteile, Amtsnummer, Zugangs-/Wegfalldatum
- **Rechnen:** Steuerbarer Eigenmietwert = Mietwert selbstgenutzt (indexiert) – Selbstnutzungsabzug Kanton 40% / Bund 20%; Zweit-/Ferienwhg., landw., Nahestehende: 100%
- **Regel:** Pro Liegenschaft: Gemeinde, Kanton, Art, Baujahr, Anteile, Amtsnummer, Steuerwert. Mietwert aus Selbstnutzung gemäss rechtskräftiger Schätzung, bereinigt mit dem Mietwertindex der Steuerperiode (aus Liegenschaftensteuerrechnung). Selbstnutzungsabzug nur am Wohnsitz dauernd selbstbewohnt: 40% Kanton / 20% Bund; kein Abzug bei Zweit-/Ferienwohnungen, landwirtschaftlich geschätzten oder unentgeltlich/unterpreislich an Nahestehende überlassenen Liegenschaften (100% steuerbar). Wohnsitz am Liegenschaftsort ausserkantonal: ausserkantonale Steuerwerte, Repartition durch Veranlagungsbehörde.
- **Beachten:** Steuerwert = rechtskräftiger amtlicher Verkehrswert Ende 2025 (landwirtschaftlich: Ertragswert)
- **Beachten:** Checkbox «Am Wohnsitz selbstgenutzt» bei Zweit-/Ferienwohnung leer lassen; Zu-/Wegfall mit genauem Datum
- **Beachten:** Am Wohnsitz selbstgenutzt: Nettoerfolg für Staat und Bund getrennt rechnen
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **40 % (Selbstnutzungsabzug 40% vom Eigenmietwert für am Wohnsitz dauernd selbstbewohntes Wohneigentum (Bund 20%); nicht für Zweit-/Ferienwohnungen, landwirtschaftlich geschätzte Liegenschaften oder an Nahestehende überlassene Objekte.)** · Bund **n/a – Eigenmietwert wird nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt (Art. 21 Abs. 2 DBG); Abschaffung per 01.01.2029 beschlossen, 2025–2028 gilt bisheriges Recht. Der Eigenmietwert für die direkte Bundessteuer wird im kantonalen Veranlagungsverfahren festgesetzt; ein dort vorgesehener Abzug für die DBSt (z.B. TG 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Bund:** Selbstnutzungsabzug Bund 20% (Kanton 40%).
- **Quellen:**
  - [Formular 7 TG 2025 S. 1](../../chunks/tg/2025/tg-form-07-2025/tg-form-07-2025__c0002.md) `tg-form-07-2025__c0002` – «Mietwert selbstgenutzt»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0224.md) `tg-wl-2025__c0224` – «Bei selbstgenutzten Liegenschaften ist der per Ende Steuerperiode rechtskräftig eröffnete Miet»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0225.md) `tg-wl-2025__c0225` – «Für am Wohnsitz selbstgenutzte eigene Liegenschaften können Sie vom Mietwert aus Selbst»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0239.md) `tg-wl-2025__c0239` – «Steuerpflicht rechtskräftigen amtlichen Verkehrswert als Steuerwert an»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0239.md) `tg-wl-2025__c0239` – «genschaften setzen Sie den Ertragswert als Steuerwert ein»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0239.md) `tg-wl-2025__c0239` – «der im Januar 2026 versandten Liegenschaftensteuerrechnung entnehmen.»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0239.md) `tg-wl-2025__c0239` – «Ausserkantonale Liegenschaften sowie im Ausland gelegene Liegenschaften deklarieren Sie zu»
  - [WL TG 2025 S. 50–51](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0240.md) `tg-wl-2025__c0240` – «Checkbox bei selbstgenutzten Zweit- und Ferienwohnungen dagegen immer leer zu lassen ist»
  - [WL TG 2025 S. 50–51](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0241.md) `tg-wl-2025__c0241` – «(infolge Kauf, Verkauf, Schenkung oder Erbgang), deklarieren Sie bitte das genaue Zugangs-»
  - [WL TG 2025 S. 51](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0244.md) `tg-wl-2025__c0244` – «Bei am Wohnsitz selbst genutzten Liegenschaften ist aufgrund der unterschiedlichen Höhe des»

<a id="form-7-mietertr-ge-einkommen-liegenschaften-mietertrag"></a>
### Ziff. Form. 7 Mieterträge – Miet- und Pachtzinsen sowie weitere Erträge, Bruttoertrag

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Mietverträge, Mietzinsabrechnung, Nebenkostenabrechnung; Einspeisevergütung Photovoltaik
- **Rein:** Mietverträge / Mietzinskonto → Miet- und Pachtzinseinnahmen 2025 · Nebenkostenabrechnung → vereinnahmte vs. effektive Nebenkosten · Abrechnung Energieversorger → PV-Einspeisevergütung vs. Strombezug · Baurechts-/Pachtvertrag → Baurechtszinsen, Naturalleistungen
- **Rechnen:** Bruttoertrag = steuerbarer Eigenmietwert + Σ Miet-/Pachtzinsen + weitere Erträge (PV-Einspeisung, Baurechtszinsen, Naturalleistungen, Hauswart-Rabatt)
- **Regel:** Sämtliche Miet-/Pachtzinseinnahmen, Naturalleistungen, Baurechtszinsen, Einspeisevergütungen PV (bei Eigenbedarfsanlagen steuerfrei, soweit die Vergütung den Strombezug nicht übersteigt), Mietzinsreduktion für Hauswarte. Nebenkostenzahlungen der Mieter nicht steuerbar, soweit sie die tatsächlichen Aufwendungen nicht übersteigen.
- **Beachten:** Mieter-Zahlungen für Heizung, Warmwasser, Treppenhausreinigung nur steuerbar, soweit über effektivem Aufwand
- **Beachten:** PV-Eigenbedarfsanlage: steuerfrei, solange Vergütung ≤ Strombezugskosten der Abrechnungsperiode
- **Beachten:** Unterpreisliche Vermietung an Nahestehende = Eigengebrauch → kantonal voller Mietwert
- **Quellen:**
  - [Formular 7 TG 2025 S. 1](../../chunks/tg/2025/tg-form-07-2025/tg-form-07-2025__c0002.md) `tg-form-07-2025__c0002` – «Miet- und Pachtzinsen»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0222.md) `tg-wl-2025__c0222` – «Steuerbar sind sämtliche Miet- und Pachtzinseinnahmen, welche die steuerpflichtige Person aus»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0223.md) `tg-wl-2025__c0223` – «Zahlungen der mietenden Personen für Heizung, Warmwasser und Reinigung von Treppenhaus»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0223.md) `tg-wl-2025__c0223` – «Betrag der den hauswartenden Personen als Arbeitsentgelt gewährten Mietzinsreduktion.»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0224.md) `tg-wl-2025__c0224` – «die Besteuerung eines Ertrags verzichtet, sofern die Entschädigung für die Stromerzeugung die»
  - [WL TG 2025 S. 51](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0244.md) `tg-wl-2025__c0244` – «Die Summe der steuerbaren Eigenmietwerte und der Miet- und Pachtzinserträge sowie allfällig»

<a id="form-7-unterhalt-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 7 Unterhalt – Unterhalts-/Betriebskosten: Pauschal oder Effektiv (Formular 8)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Rechnungen (Kopien ab Fr. 1'000 einreichen); Formular 8 je Liegenschaft; Merkblatt Liegenschaftsunterhalt
- **Rein:** Form. 8 → Total Unterhalts- und Betriebskosten (bei effektiv) · Form. 7 → Mietertrag, Mietwert selbstgenutzt bzw. steuerbarer Eigenmietwert (Basis Pauschale) · Schätzung / Form. 7 → Baujahr (Gebäudealter)
- **Rechnen:** Pauschal: 10% (Gebäude ≤ 10 Jahre) / 20% (> 10 Jahre) × Mietertrag bzw. Mietwert/steuerbarer Eigenmietwert; oder effektiv (Form. 8) – Wahl je Liegenschaft/Jahr
- **Regel:** Pro Steuerperiode und Liegenschaft Wahl zwischen Pauschale und effektiven Kosten. Pauschale: 10% für Gebäude bis 10 Jahre, 20% bei älteren Gebäuden (Alter am Ende der Steuerperiode), berechnet auf Mietertrag bzw. Mietwert/steuerbaren Eigenmietwert. Keine Pauschale bei Geschäftsvermögen, vorwiegend geschäftlich von Dritten genutzten, unüberbauten oder Baurechts-Grundstücken. Nicht kumulierbar mit übertragbaren Energie-/Rückbaukosten (dann alles effektiv).
- **Beachten:** Gebäudealter: Kanton am Ende, Bund (LKV Art. 5) zu Beginn der Steuerperiode
- **Beachten:** Keine Pauschale: Geschäftsvermögen, geschäftl. Drittnutzung, unüberbaut, Baurecht, übertragbare Energie-/Rückbaukosten
- **Beachten:** Effektiv: je Liegenschaft ein Form. 8; Rechnungskopien ab Fr. 1'000; STWEG: Abrechnung der Gemeinschaft
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Unterhaltspauschale 10% des Bruttomietertrags/Mietwerts/Eigenmietwerts für Gebäude bis zehn Jahre alt (am Ende der Steuerperiode); Wahl pro Liegenschaft und Periode; nicht bei Geschäftsvermögen, unüberbauten Grundstücken, Baurecht.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Unterhaltspauschale 20% für Gebäude, die älter als zehn Jahre sind.)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Quellen:**
  - [Formular 7 TG 2025 S. 1](../../chunks/tg/2025/tg-form-07-2025/tg-form-07-2025__c0002.md) `tg-form-07-2025__c0002` – «Unterhalts-/Betriebskosten»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0238.md) `tg-wl-2025__c0238` – «Die Pauschale beträgt:»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0238.md) `tg-wl-2025__c0238` – «20% für Gebäude, die am Ende der Steuerperiode älter als zehn Jahre sind.»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags»
  - [WL TG 2025 S. 49](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0233.md) `tg-wl-2025__c0233` – «Pro Liegenschaft, für welche Sie effektive Unterhaltskosten geltend machen, füllen Sie bitte je ein»
  - [WL TG 2025 S. 49](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0234.md) `tg-wl-2025__c0234` – «Für Einzelbeträge ab Fr. 1'000 legen Sie der Steuererklärung bitte die Rechnungskopien»
  - [WL TG 2025 S. 49–50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0236.md) `tg-wl-2025__c0236` – «Die Kumulation mit dem Pauschalabzug für Liegenschaftsunterhaltskosten»

<a id="form-7-totale-berechnung-total"></a>
### Ziff. Form. 7 Totale – Totale Steuerwerte (Code 430) und Nettoerfolge (Code 180) Staat/Bund

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Form. 7 je Liegenschaft (inkl. Rückseite) → Steuerwert, Nettoerfolg Staat/Bund
- **Rechnen:** Σ Steuerwerte = Code 430 → Ziff. 31 (S. 4); Σ Nettoerfolge (Bruttoertrag – Unterhalt) je Spalte Staat/Bund = Code 180 → Ziff. 8 (S. 2)
- **Regel:** Total Steuerwerte → Steuererklärung Ziff. 31 (Seite 4); Total Nettoerfolge → Ziff. 8 (Seite 2), Spalten Staat und Bund getrennt.
- **Beachten:** Am Wohnsitz selbstgenutzt: Nettoerfolg Staat/Bund getrennt; übrige: Staatsergebnis in Bundesspalte übernehmen
- **Beachten:** Ausserkantonale/ausländische Liegenschaften zum dortigen Steuerwert; Repartition durch die Veranlagungsbehörde
- **Quellen:**
  - [Formular 7 TG 2025 S. 1](../../chunks/tg/2025/tg-form-07-2025/tg-form-07-2025__c0003.md) `tg-form-07-2025__c0003` – «Total Steuerwerte   430   Total Nettoerfolge   180»
  - [WL TG 2025 S. 51](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0244.md) `tg-wl-2025__c0244` – «Bei am Wohnsitz selbst genutzten Liegenschaften ist aufgrund der unterschiedlichen Höhe des»
  - [WL TG 2025 S. 51](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0245.md) `tg-wl-2025__c0245` – «zuerst in der Spalte „Staatssteuer“ berechnen und das Ergebnis danach in die Spalte „Bundes-»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0239.md) `tg-wl-2025__c0239` – «Bei diesen Liegenschaften nimmt die Veranlagungsbehörde eine An-»

<a id="form-8-abzug-liegenschaft-energie-umwelt"></a>
### Ziff. Form. 8 – Angaben zu Unterhalts- und Betriebskosten (je Liegenschaft): Rechnungsdatum, Rechnungsteller, Arbeit, Zahlungsbetrag, Anlagekosten/Mehrwert, abzugsfähige Kosten; Energiespar-/Umweltschutz-/Rückbaukosten; übertragbare Kosten

- **Schlüssel:** `abzug.liegenschaft.energie_umwelt` (Investitionen Energiesparen/Umweltschutz, Rückbaukosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Rechnungen mit Detailangaben; Hilfsblatt übertragbare Kosten (StP 34 Nr. 2); bei Stockwerkeigentum Abrechnung der Gemeinschaft
- **Rein:** Handwerker-/Unternehmerrechnungen → Datum, Rechnungsteller, Arbeit, Zahlungsbetrag · STWEG: detaillierte Abrechnung der Gemeinschaft (Fondseinlagen) · Verfügungen Förderbeiträge (Bund, Kanton, Gemeinde, Klimarappen) → Kostenminderung · Hilfsblatt übertragbare Kosten + Veranlagung 2024 (Reineinkommen Ziff. 24) → Vortrag
- **Rechnen:** Je Rechnung: Zahlungsbetrag = Anteil Anlagekosten/Mehrwert + Unterhalt; Σ Unterhalt – Förderbeiträge + übertragbare Kosten Vorjahre → Übertrag Form. 7
- **Regel:** Pro Liegenschaft ein Formular 8; Einzelbeträge ab Fr. 1'000 mit Rechnungskopie belegen. Wertvermehrende Investitionen, Neubau/Umbau, Ersatzbauten, Behebung konstruktiver Mängel, Fahrnis nicht abziehbar (Anteil in Spalte Anlagekosten/Mehrwert). Energiespar-/Umweltschutzmassnahmen und Rückbaukosten für Ersatzneubau abziehbar; Förderbeiträge mindern die Kosten. Überschiessende Kosten (negatives Reineinkommen) auf die nächsten zwei Steuerperioden übertragbar (2025: Kosten aus 2023/2024 geltend machen; Rest in 2026 und 2027). Zeitliche Abgrenzung nach Rechnungsstellung oder Bezahlung, Wahl beibehalten.
- **Beachten:** Nicht abziehbar (→ Spalte Anlagekosten/Mehrwert): Neu-/Um-/Anbau, Ersatzbau, Mehrwert, konstruktive Mängel, Fahrnis
- **Beachten:** Rückbaukosten nur bei Ersatzneubau (gleiche Person, Grundstück, Nutzung; i.d.R. innert 2 Jahren)
- **Beachten:** 2025: unverrechnete Kosten 2023/2024 (Basis Reineinkommen 2024, Ziff. 24); Überschuss → 2026/2027; nur effektiv
- **Quellen:**
  - [Formular 8 TG 2025 S. 1](../../chunks/tg/2025/tg-form-08-2025/tg-form-08-2025__c0001.md) `tg-form-08-2025__c0001` – «1. Füllen Sie bitte pro Liegenschaft ein Formular aus.»
  - [WL TG 2025 S. 49](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0234.md) `tg-wl-2025__c0234` – «Für Einzelbeträge ab Fr. 1'000 legen Sie der Steuererklärung bitte die Rechnungskopien (inkl. der»
  - [WL TG 2025 S. 49–50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0235.md) `tg-wl-2025__c0235` – «nicht mit dem Reineinkommen verrechneten Kosten auf die beiden nachfolgenden Steuerperioden»
  - [Formular 8 TG 2025 S. 1](../../chunks/tg/2025/tg-form-08-2025/tg-form-08-2025__c0003.md) `tg-form-08-2025__c0003` – «Total Unterhalts- und Betriebskosten (Übertrag auf Formular 7)»
  - [WL TG 2025 S. 49](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0233.md) `tg-wl-2025__c0233` – «Investitionen in einen Neubau, in bauliche Veränderungen wie Um-, Ein- Anbauten sowie»
  - [WL TG 2025 S. 49](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0232.md) `tg-wl-2025__c0232` – «innert angemessener Frist errichtet werden (i.d.R. 2 Jahre seit Vornahme Rückbau)»
  - [WL TG 2025 S. 49](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0231.md) `tg-wl-2025__c0231` – «vermindern die selbst getragenen Kosten»
  - [WL TG 2025 S. 49–50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0236.md) `tg-wl-2025__c0236` – «In der Steuerperiode 2025 können Sie die in den Jahren 2023 und 2024 angefallenen»
  - [WL TG 2025 S. 49–50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0237.md) `tg-wl-2025__c0237` – «Massgebend für die Berechnung der übertragbaren Kosten ist das veranlagte Reineinkommen 2024»
  - [WL TG 2025 S. 48](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0228.md) `tg-wl-2025__c0228` – «Einlagen in den Reparatur- oder Erneuerungsfonds der Stockwerkeigentümergemeinschaft sind»

## Hilfsblatt Zuwendungen

<a id="form-6-gemeinn-tzig-abzug-spenden"></a>
### Ziff. Form. 6 gemeinnützig – Zuwendungen für gemeinnützige oder öffentliche Zwecke (Name und Sitz der Institution) → Berechnung abzugsfähige freiwillige Zuwendungen (Code 366)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigungen (ab Fr. 1'000 pro Zuwendung einreichen)
- **Rein:** Spendenbestätigung/Quittung je Institution → Betrag, Name und Sitz · Liste geprüfter Institutionen (steuerverwaltung.tg.ch) → Abzugsfähigkeit · Steuererklärung Ziff. 22 → Nettoeinkommen Staat/Bund (Maximum)
- **Rechnen:** Kanton: min(Σ – 200; Netto Ziff. 22 ≤ 40'000: 8'000, sonst 20% × Netto) / Bund: falls Σ ≥ 100: min(Σ; 20% × Netto Ziff. 22) → Code 366 → Ziff. 23.2
- **Regel:** Einzeln mit Name und Sitz der empfangenden Institution aufführen. Berechnung: Total minus Selbstbehalt Fr. 200 (Staat) bzw. ohne Selbstbehalt (Bund, ab Gesamtbetrag Fr. 100); Staat max. Fr. 8'000 bei Nettoeinkommen bis Fr. 40'000, sonst max. 20% des Nettoeinkommens; Bund max. 20%. Übertrag Ziff. 23.2.
- **Beachten:** Nur an steuerbefreite jur. Personen mit Sitz CH (öffentlich/gemeinnützig) + Gemeinwesen; nicht religiös/kulturell/Sport
- **Beachten:** Belege ab Fr. 1'000 pro Zuwendung einreichen; Pauschalvermerke («diverse Organisationen») nicht anerkannt
- **Beachten:** Ehrenamtliche Arbeitsleistungen und Zuwendungen an juristische Personen im Ausland nicht abziehbar
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 200 (Freiwillige Zuwendungen kantonal nur abziehbar, soweit gesamthaft CHF 200 übersteigend (Bund: ab CHF 100).)** · Bund **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen (CH) bzw. Gemeinwesen: mindestens CHF 100 im Steuerjahr)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Maximal 20% des Nettoeinkommens (Ziff. 22); bei Nettoeinkommen bis CHF 40'000 maximal CHF 8'000. Nur an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentliche/gemeinnützige Zwecke) sowie Bund/Kantone/Gemeinden.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Bund:** Bund: kein Selbstbehalt, max. 20%.
- **Quellen:**
  - [Formular 6 TG 2025 S. 1](../../chunks/tg/2025/tg-form-06-2025/tg-form-06-2025__c0002.md) `tg-form-06-2025__c0002` – «abzüglich Selbstbehalt (Staats- und Gemeindesteuern)   –   200.–»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0220.md) `tg-wl-2025__c0220` – «Deklaration   Führen Sie die freiwilligen Zuwendungen und/oder die Mitgliederbeiträge und Zuwendungen an po»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0217.md) `tg-wl-2025__c0217` – «Nicht abziehen können Sie dagegen freiwillige Zuwendungen an Körperschaften, welche im Hinblick»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0217.md) `tg-wl-2025__c0217` – «sind sowie an juristische Personen mit Sitz im Ausland. Ebenfalls nicht abzugsfähig sind unentgelt-»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0218.md) `tg-wl-2025__c0218` – «Sofern die freiwilligen Zuwendungen insgesamt den Betrag von Fr. 100 erreichen»

<a id="form-6-parteien-abzug-parteispenden"></a>
### Ziff. Form. 6 Parteien – Mitgliederbeiträge und Zuwendungen an politische Parteien (Code 347) → Ziff. 15.5

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Quittungen/Bescheinigungen der Partei (ab Fr. 1'000 pro Zuwendung einreichen)
- **Rein:** Quittung/Bescheinigung der Partei → Mitgliederbeiträge und Zuwendungen 2025 · Form. 6 Zeile B, Spalte «politische Parteien» → Total (Code 347)
- **Rechnen:** Kanton: min(Σ Parteibeiträge; 10'000) / Bund: min(Σ; 10'600) → Code 347 → Ziff. 15.5
- **Regel:** Spalte «politische Parteien»; Maximum Staat Fr. 10'000, Bund Fr. 10'600; Übertrag Ziff. 15.5.
- **Beachten:** Nur Parteien im Parteienregister (Art. 76a BPR) und im kant. Parlament vertreten oder ≥ 3% Stimmen
- **Beachten:** Einzeln mit Name/Sitz der Partei; Belege ab Fr. 1'000 pro Zuwendung; Pauschalvermerke nicht anerkannt
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister, im kantonalen Parlament vertreten oder mind. 3% Stimmen): max. CHF 10'000.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
- **Quellen:**
  - [Formular 6 TG 2025 S. 1](../../chunks/tg/2025/tg-form-06-2025/tg-form-06-2025__c0002.md) `tg-form-06-2025__c0002` – «Total Mitgliederbeiträge und Zuwendungen an politische Parteien (Übertrag von Buchstabe B)   347»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0219.md) `tg-wl-2025__c0219` – «im Parteienregister nach Artikel 76a des Bundesgesetzes über die politischen Rechte eingetra-»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0219.md) `tg-wl-2025__c0219` – «Parlaments mindestens 3% der Stimmen erreicht hat»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0220.md) `tg-wl-2025__c0220` – «Für Zuwendungen unter Fr. 1'000 sind keine Belege einzureichen. Ab Fr. 1'000 pro Zuwendung»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0221.md) `tg-wl-2025__c0221` – «B das Total der geleisteten Mitgliederbeiträge und Zuwendungen an politische Parteien sowie das»
