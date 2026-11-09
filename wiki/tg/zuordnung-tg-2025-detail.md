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
- **Regel:** Massgebend sind die Verhältnisse am 31.12.2025 bzw. am Ende der Steuerpflicht (Stichtag). Gemeinsam besteuerte Personen: Person 1 und Person 2 in allen Formularen und Hilfsblättern durchgehend gleich zuordnen. Bei unterjähriger Steuerpflicht (Zuzug/Wegzug Ausland, Tod) Dauer von/bis oben links auf Seite 1 eintragen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0002.md) `tg-form-01-2025__c0002` – «Personalien, Berufs- und Familienverhältnisse am 31. Dezember 2025 oder am Ende der Steuerpflicht»
  - [WL TG 2025 S. 12](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0045.md) `tg-wl-2025__c0045` – «Achten Sie bitte darauf, in den Formularen unter Person 1 bzw. Person 2 durchgehend die Angaben»

<a id="seite-1-kinder-personalien"></a>
### Ziff. Seite 1 Kinder – Kinder (minderjährig, in Ausbildung oder erwerbsunfähig), Unterhalt wird bestritten; Zusatzangaben bei getrennt besteuerten Eltern

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1: Vorname/Name, Geburtsdatum, im Haushalt, Schule/Lehrfirma, Ausbildungsende, Unterhaltsbeiträge, Sorgerecht, Obhut
- **Regel:** Genaues Geburtsdatum angeben. Kinder mit Jahrgang 2005 und älter in Ausbildung: Ausbildungsstätte/Lehrfirma und voraussichtliches Ende der Ausbildung. Bei nicht gemeinsam besteuerten Eltern (getrennt, geschieden, Konkubinat mit gemeinsamen Kindern) Checkboxen Unterhaltsbeiträge/gemeinsames Sorgerecht/alternierende Obhut ausfüllen – sie steuern die Zuteilung von Kinderabzug, Versicherungsabzug, Vermögensfreibetrag und Tarif.
- **Quellen:**
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0003.md) `tg-form-01-2025__c0003` – «Minderjährige, in beruflicher Ausbildung stehende oder erwerbsunfähige Kinder, deren Unterhalt Sie bestreiten»
  - [WL TG 2025 S. 12](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0045.md) `tg-wl-2025__c0045` – «Für Kinder mit Jahrgang 2005 und älter, welche sich in Ausbildung befinden, geben Sie bitte»

<a id="seite-1-unterst-tzte-personen-personalien"></a>
### Ziff. Seite 1 Unterstützte Personen – Erwerbsunfähige und unterstützungsbedürftige Personen (Unterstützungsbetrag ≥ Fr. 12'000 Kanton / Fr. 6'800 Bund)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** – → Formular 1 Seite 1: Vorname/Name, Geburtsdatum, im Haushalt, Adresse, Unterstützungsbetrag
- **Regel:** Nur Personen ohne Kinder-/Ehegattenstatus. Formular nennt Mindestbeitrag Fr. 12'000 (Kanton) bzw. Fr. 6'800 (Bund); Wegleitung kantonal: nachweislich mindestens 50% des betreibungsrechtlichen Existenzminimums, Unterstützungsbedürftigkeit durch Bestätigung der Wohnsitzgemeinde belegen. Abzug siehe Ziff. 25.2.
- **Bemerkung:** Formulartext (Fr. 12'000 Kanton) und Wegleitung (mind. 50% des betreibungsrechtlichen Existenzminimums, Steuerpraxis) nennen unterschiedliche Kriterien; kein Widerspruch im Betrag des Abzugs, aber Mindestbeitrag in der Praxis nachprüfen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0004.md) `tg-form-01-2025__c0004` – «mindestens Fr. 12 000.– (Kanton) bzw. Fr. 6 800.– (Bund) unterstützen»
  - [WL TG 2025 S. 24–25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0114.md) `tg-wl-2025__c0114` – «lichen Existenzminimums der betreffenden erwerbsunfähigen und unterstützungsbedür»

<a id="seite-1-auszahlungskonto-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Seite 1 Auszahlungskonto – Auszahlungskonto für Steuerrückzahlungen und Rückerstattung Verrechnungssteuer (IBAN)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1: Kontoinhaber/in, IBAN, Bank/Post
- **Regel:** Konto nur bei Erstantrag oder Kontoänderung ausfüllen (IBAN, Bank oder Post). Kontoänderungen nach Einreichung der Steuererklärung möglichst vermeiden (Verzögerung der Rückerstattung).
- **Quellen:**
  - [Formular 1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0005.md) `tg-form-01-2025__c0005` – «Alle Rückerstattungen der Verrechnungssteuer sowie allfälliger Steuerrückzahlungen erfolgen auf»
  - [WL TG 2025 S. 35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0168.md) `tg-wl-2025__c0168` – «Um Verzögerungen bei der»

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Haupterwerb unselbständig (Code 100 Person 1 / 101 Person 2)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 Nettolohn; Pauschalspesen (Ziff. 13.2) in die Vorspalte «Pauschalspesen»
- **Regel:** Nettolohn gemäss Lohnausweis Ziff. 11 einsetzen (Brutto Ziff. 8 abzüglich AHV/IV/EO/ALV Ziff. 9 und BVG Ziff. 10). Pauschalspesen separat in der Vorspalte. Naturalbezüge/Trinkgelder, falls nicht im Lohnausweis, ergänzen. Alle Lohnausweise einreichen. Lohnausweis-Hinweise: Feld F (unentgeltliche Beförderung Wohn-/Arbeitsort, z.B. Geschäftsfahrzeug) angekreuzt = kein Fahrkostenabzug (Form. 4.2 Ziff. 2); Feld G (Kantinenverpflegung/Lunch-Checks) = nur halber Verpflegungsabzug (Form. 4.2 Ziff. 3.2); Ziff. 10.2 (Einkauf BVG) ist bereits im Nettolohn abgezogen und nicht nochmals in Ziff. 15.2 geltend zu machen; Ziff. 13.3 (Arbeitgeberbeiträge an Weiterbildung) mindert den Abzug Ziff. 16; Ziff. 15 Bemerkungen: Anzahl Schichttage (Beleg für Verpflegungsabzug), Teilzeit, Rektifikat, mehrere Lohnausweise.
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0006.md) `tg-form-01-2025__c0006` – «1.1 Haupterwerbstätigkeit   Person 1   100»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0049.md) `tg-wl-2025__c0049` – «In die Steuererklärung ist der in Ziffer 11 des Lohnausweises aufgeführte Nettolohn einzusetzen.»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «In diesem Feld ist der für die Steuererklärung massgebende Nettolohn anzugeben.»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Nebenerwerb unselbständig (Code 104 Person 1 / 105 Person 2), inkl. VR-/Behördenentschädigungen

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 Nettolohn des Nebenerwerbs
- **Regel:** Sämtliches Einkommen aus unselbständigem Nebenerwerb ohne Freigrenze deklarieren (auch Sitzungsgelder, VR-Honorare, Tantiemen). Feuerwehrsold: Kernaufgaben steuerfrei bis Fr. 5'000 (Staat) bzw. Fr. 5'300 (Bund); über dem Freibetrag steuerbar; in der Steuererklärung die kantonal steuerbaren Einkünfte deklarieren, Bund korrigiert die Steuerverwaltung von Amtes wegen. Berufsauslagen Nebenerwerb: Form. 4.2 Ziff. 6.
- **Limiten:**
  - Feuerwehrsold steuerfrei bis (CHF): Kanton **CHF 5'000 (Sold der Milizfeuerwehrleute für Kernaufgaben steuerfrei bis CHF 5'000 pro Jahr (Kanton); Pauschalzulagen für Kader, Funktionszulagen, administrative und freiwillige Dienstleistungen sind steuerbar.)** · Bund **CHF 5'300 (Sold der Milizfeuerwehrleute für Kernaufgaben steuerfrei bis CHF 5'300 pro Jahr)**
- **Bund:** Feuerwehrsold-Freibetrag Bund Fr. 5'300 (Kanton Fr. 5'000).
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0006.md) `tg-form-01-2025__c0006` – «1.2 Nebenerwerbstätigkeit   Person 1   104»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0051.md) `tg-wl-2025__c0051` – «Daher ist sämtliches Einkommen aus einer unselbständigen Nebenerwerbstätigkeit»
  - [WL TG 2025 S. 13](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0052.md) `tg-wl-2025__c0052` – «Fr. 5'000 bei der Staats- und Gemeindesteuer;»

<a id="1-3-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 1.3 – Im vereinfachten Abrechnungsverfahren bereits versteuerter Bruttolohn (Code 106 / 107)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der AHV-Ausgleichskasse (Bruttolohnsumme)
- **Regel:** Nur Information (Vorkolonne): im vereinfachten Verfahren bereits versteuerte Löhne werden weder als steuerbares noch als satzbestimmendes Einkommen berücksichtigt und fliessen nicht ins Zwischentotal Ziff. 6. Bescheinigung beilegen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0006.md) `tg-form-01-2025__c0006` – «1.3 Im vereinfachten Abrechnungsverfahren bereits versteuerter Bruttolohn»
  - [WL TG 2025 S. 14](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0053.md) `tg-wl-2025__c0053` – «Löhne werden nicht in die Berechnung des Zwischentotals unter Ziffer 6 miteinbezogen.»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit Haupterwerb (Code 112 Person 1 / 113 Person 2)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz und Erfolgsrechnung bzw. Aufstellung Einnahmen/Ausgaben/Aktiven/Passiven; ggf. Formular 14 (Fragebogen Selbständigerwerbende)
- **Regel:** Reingewinn nach geschäftsmässig begründeten Kosten (negativer Betrag mit Vorzeichen). Persönliche 2.-Säule-Beiträge nur im Umfang Arbeitgeberanteil im Geschäftsergebnis; Privatanteil und alle Säule-3a-Beiträge nur in Ziff. 13 bzw. 15.2. Direkt ausbezahlte Familienzulagen nicht hier, sondern Ziff. 3.4. Liquidationsgewinne (ab 55 / Invalidität) siehe Ziff. 23.3. Teilbesteuerung Beteiligungen im Geschäftsvermögen (Kanton 60% / Bund 70%) über Formular 14.
- **Bund:** Teilbesteuerung Beteiligungen Geschäftsvermögen beim Bund 70% (Kanton 60%); Steuerverwaltung nimmt Bundeskorrektur von Amtes wegen vor.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0006.md) `tg-form-01-2025__c0006` – «2.1 Haupterwerbstätigkeit   Person 1   112»
  - [WL TG 2025 S. 14–15](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0058.md) `tg-wl-2025__c0058` – «Deklarieren Sie hier aus Industrie, Handel, Gewerbe, freien Berufen sowie Land- und Forstwirtschaft»
  - [WL TG 2025 S. 15](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0061.md) `tg-wl-2025__c0061` – «sondern sind ausschliesslich in Ziffer 13 bzw. 15.2 der»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Selbständige Erwerbstätigkeit Nebenerwerb (Code 116 Person 1 / 117 Person 2)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Aufstellung Einnahmen/Ausgaben des Nebenerwerbs
- **Regel:** Nettoeinkommen aus selbständigem Nebenerwerb (z.B. Provisionen, Gutachterhonorare, Privatunterricht). Ausführungen zu Ziff. 2.1 gelten sinngemäss.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0006.md) `tg-form-01-2025__c0006` – «2.2 Nebenerwerbstätigkeit   Person 1»
  - [WL TG 2025 S. 17](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0074.md) `tg-wl-2025__c0074` – «Deklarieren Sie hier ein Netto-Einkommen aus einer selbständigen Nebenerwerbstätigkeit»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV-/IV-Renten (Code 130 Person 1 / 131 Person 2)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung AHV/IV (Jahresbetrag brutto)
- **Regel:** 100% steuerbar (Kanton und Bund). Steuerfrei und nicht anzugeben: Ergänzungsleistungen AHV/IV, Sozialhilfe, Genugtuungszahlungen. Beim Bezug von EL Kreuz auf Seite 1 setzen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0007.md) `tg-form-01-2025__c0007` – «3.1 AHV-/IV-Renten   Person 1   130»
  - [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0076.md) `tg-wl-2025__c0076` – «Renten der AHV/IV sind sowohl bei den Staats- und Gemeindesteuern als auch bei der direkten»
  - [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0076.md) `tg-wl-2025__c0076` – «Ergänzungsleistungen der AHV und IV;»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen (2. Säule, SUVA, Säule 3a, 3b, Leibrenten) mit steuerbarem Bruttobetrag und Prozent (Code 132 Person 1 / 133 Person 2)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente), Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Rentenbescheinigung der Vorsorgeeinrichtung/Versicherung: steuerbarer Bruttobetrag und Prozentsatz
- **Regel:** Bruttobetrag und steuerbaren Prozentsatz angeben. Renten aus beruflicher Vorsorge, gebundener Selbstvorsorge und Invaliditätsrenten (3b) zu 100%; Übergangsrecht 80% nur bei Rentenbeginn vor 1.1.1987 bzw. 1.1.1987–1.1.2002 mit Vorsorgeverhältnis per 31.12.1984/1986 und mind. 20% Eigenbeiträgen. Leibrenten: steuerbar im Ertragsanteil gemäss Bescheinigung, Überschussleistungen pauschal 70%. Bei mehr als zwei Renten Aufstellung beilegen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0007.md) `tg-form-01-2025__c0007` – «3.2 Renten/Pensionen   Steuerbar Bruttobetrag / Fr.   in Prozent»
  - [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0077.md) `tg-wl-2025__c0077` – «Grundsätzlich sind Renten aus beruflicher Vorsorge, aus gebundener Selbstvorsorge sowie»
  - [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0078.md) `tg-wl-2025__c0078` – «Überschussleistungen sind pauschal zu 70% steuerbar.»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigungen (Taggelder Kranken-/Unfall-/IV/ALV, Mutterschaft, EO) (Code 136 Person 1 / 137 Person 2)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Bescheinigung der Versicherung/Ausgleichskasse/ALV; Lohnausweis Ziff. 15 (Anzahl Tage mit Erwerbsausfallentschädigung)
- **Regel:** Nur soweit nicht bereits im Lohnausweis enthalten (sonst Doppelerfassung mit Ziff. 1). Taggelder ALV, SUVA, Kranken-/Unfall-/IV-Versicherung, Mutterschaftsentschädigung, EO-Entschädigungen direkt von der Ausgleichskasse. Steuerfrei und nicht anzugeben: Sold Militär/Zivilschutz/Feuerwehr, Taschengeld Zivildienst. Bescheinigung beilegen. Lohnausweis Ziff. 15 muss die Anzahl Tage nennen, wenn die Entschädigung nicht über den Arbeitgeber lief.
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0007.md) `tg-form-01-2025__c0007` – «3.3 Erwerbsausfallentschädigungen»
  - [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0079.md) `tg-wl-2025__c0079` – «Diese Entschädigungen sind insoweit anzugeben, als sie im Lohnausweis von den Arbeitgebenden»
  - [WL Lohnausweis 2026 S. 19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0052.md) `bund-wl-lohnausweis-2026__c0052` – «Anzahl der Tage mit Erwerbsausfallentschädigungen: Diese sind stets anzugeben,»

<a id="3-4-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.4 – Von Ausgleichskassen direkt ausbezahlte Familien-, Kinder- und Haushaltszulagen (Code 140)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Familienausgleichskasse (Kinder-, Haushalts-, Ausbildungs-, Geburts-, Adoptionszulagen)
- **Regel:** Nur direkt von der Ausgleichskasse ausbezahlte Zulagen an Selbständigerwerbende, Nichterwerbstätige und Landwirtschaft; Zulagen im Lohnausweis stecken bereits im Nettolohn (Ziff. 1). Nicht unter Ziff. 2 deklarieren.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0007.md) `tg-form-01-2025__c0007` – «3.4 Von Ausgleichskassen direkt ausbezahlte Familien-, Kinder- und Haushaltszulagen   140»
  - [WL TG 2025 S. 18](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0080.md) `tg-wl-2025__c0080` – «Deklarieren Sie hier von der Ausgleichskasse direkt ausbezahlte Familien- und Haushaltszulagen.»

<a id="4-einkommen-wertschriften"></a>
### Ziff. 4 – Wertschriften- und Zinserträge sowie Gewinne aus Geldspielen (Formular 2, Code 150)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Formular 2 (Wertschriftenverzeichnis) Total steuerbarer Ertrag Ziff. 9 (Code 150)
- **Regel:** Erst Formular 2 ausfüllen, dann Total steuerbarer Ertrag übertragen (Bruttoerträge Spalten 8+9 abzüglich Geschäftsanteil, Vermögensverwaltungskosten und pauschale Einsatzkosten Geldspiele). Steuerauszug der Bank einreichen, wenn Titel nur als Total deklariert werden. Lotterien/Geschicklichkeitsspiele: einzelne Gewinne bis Fr. 1'000 steuerfrei (Bund Fr. 1'100); übersteigt ein einzelner Gewinn die Grenze, ist dieser Einzelgewinn voll steuerbar (weitere Einzelgewinne unter der Grenze bleiben steuerfrei); ausländische Lotterien/Spiele immer voll steuerbar. Grossspiele/Online-Spielbank: einzelne Gewinne bis Fr. 1'000'000 (Bund Fr. 1'070'400) steuerfrei, steuerbar nur der übersteigende Anteil; Kleinspiele steuerfrei. Ausländische Erträge: Nettobetrag zuzüglich anrechenbarer Quellensteuer; Formular DA-1.
- **Limiten:**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'000 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'000 (Kanton; Bund CHF 1'100). Gewinne über der Grenze sind voll steuerbar.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'100)**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'000'000 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen nach BGS steuerfrei bis CHF 1'000'000 (Kanton); Bund CHF 1'070'400.)** · Bund **CHF 1'070'400 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'070'400)**
- **Bund:** Steuerfreigrenze Lotterien/Geschicklichkeitsspiele Bund Fr. 1'100 (Kanton Fr. 1'000); Grossspiele Bund Fr. 1'070'400 (Kanton Fr. 1'000'000); Bundeskorrektur von Amtes wegen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «4. Wertschriften- und Zinserträge sowie Gewinne aus Geldspielen   Formular 2 150»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0163.md) `tg-wl-2025__c0163` – «Das Total der steuerbaren Erträge in Ziffer 9 errechnen Sie, indem Sie vom Zwischentotal in Ziffer»
  - [WL TG 2025 S. 31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0146.md) `tg-wl-2025__c0146` – «Einzelne solche Gewinne bis zu einem Betrag von Fr. 1 000 sind hin»

<a id="5-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.1 – Unterhaltsbeiträge von Ehegatte/Partner bei Trennung/Scheidung (Name und Adresse Zahler/in) (Code 160)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil bzw. Vereinbarung; Zahlungsnachweise
- **Regel:** Periodische Unterhaltsbeiträge für sich selbst steuerbar; ebenso Mietwertanteil aus Überlassung eines Liegenschaftsanteils. Name/Adresse der zahlenden Person in der Zeile unter 5.1 angeben. Gegenstück: Abzug beim Zahler Ziff. 12.1.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «5.1 Unterhaltsbeiträge von Ehefrau/-mann bzw. Partnerin/Partner bei Trennung/Scheidung»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0081.md) `tg-wl-2025__c0081` – «Steuerbar sind periodische Unterhaltsbeiträge der Ehefrau oder des Ehemanns bzw. der»

<a id="5-2-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.2 – Unterhaltsbeiträge für minderjährige Kinder (inkl. Kinderzulagen) (Name und Adresse Zahler/in) (Code 162)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Urteil/Vereinbarung; Zahlungsnachweise; ggf. Alimentenbevorschussung
- **Regel:** Für Kinder unter eigener elterlicher Sorge steuerbar; bei unregelmässigen Zahlungen die tatsächlich im Jahr 2025 überwiesenen Beträge. Alimentenbevorschussung durch die Gemeinde vermerken. Ab Folgemonat der Volljährigkeit nicht mehr steuerbar. Wer die Alimente versteuert, erhält den Kinderabzug (Ziff. 25.1).
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «5.2 Unterhaltsbeiträge für minderjährige Kinder (Name, Adresse Zahler/in)   162»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0081.md) `tg-wl-2025__c0081` – «Periodische Unterhaltsbeiträge (inklusive Kinderzulagen), die Sie für die unter Ihrer elterlichen»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0081.md) `tg-wl-2025__c0081` – «Ab dem Folgemonat der Volljährigkeit des Kindes sind die»

<a id="5-3-einkommen-erbschaften-unverteilt"></a>
### Ziff. 5.3 – Ertrag aus unverteilten Erbschaften (Formular 3) (Code 164)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung der Erbengemeinschaft/Nachlassverwalter (Ertrag, Erbquote); Vermögensanteil Ziff. 30.5
- **Regel:** Erträge nach Erbquote zurechnen; Steuerpflicht beginnt am Tag nach dem Todestag. VSt-belastete Erträge im Umfang der Erbquote in Spalte A von Formular 2, nicht belastete in Spalte B. Rückerstattung im Wohnsitzkanton.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «5.3 Ertrag aus unverteilten Erbschaften   Formular 3 164»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0082.md) `tg-wl-2025__c0082` – «Einkünfte aus unverteilten Erbschaften werden den erbenden Personen entsprechend ihrer»

<a id="5-4-einkommen-uebrige"></a>
### Ziff. 5.4 – Weitere Einkünfte (Urheberrechte, Lizenzen, Patente, Wohnrecht, Nutzniessung, Lidlohn, Entschädigungen) (Code 168)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Verträge/Aufstellung; nähere Bezeichnung auf dem Formular
- **Regel:** Hier: Urheber-/Autorenrechte, Lizenzen, Patente, Nutzniessung, unentgeltliches Wohnrecht (bewertet mit der Miete einer entsprechenden Wohnung), Lidlöhne, Entschädigungen für Konkurrenzverbot/Verzicht auf Rechte, Untervermietung netto. Gewinne aus Geldspielen gehören in Ziff. 4, nicht hierher.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «5.4 Weitere Einkünfte (z.B. Urheberrechte, Lizenzen, Patente, Wohnrecht usw.)»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0083.md) `tg-wl-2025__c0083` – «In Ziffer 5.4 deklarieren Sie Einkünfte aus Urheber- und Autorenrechten, Lizenzen, Patenten»

<a id="5-5-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 5.5 – Kapitalabfindung für wiederkehrende Leistungen für … Jahre (Code 170)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung über die Kapitalabfindung (Rentenrückkauf, Lidlohn u.ä.)
- **Regel:** Zeitraum (Jahre) angeben, für den die Abfindung ausgerichtet wird; Besteuerung zum Satz, der sich bei entsprechender jährlicher Leistung ergäbe (bei Lebenszeit-Renten Umrechnung nach Rentenwerttabelle). Nicht hier, sondern Seite 4 unten: Kapitalleistungen aus Vorsorge.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «5.5 Kapitalabfindung für wiederkehrende Leistungen für»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0084.md) `tg-wl-2025__c0084` – «Anstelle von wiederkehrenden Leistungen ausbezahlte Kapitalabfindungen (z.B. Rentenrückkauf,»

<a id="6-berechnung-total"></a>
### Ziff. 6 – Zwischentotal der Einkünfte (Code 175)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 1.1–5.5 ohne 1.3)
- **Regel:** Summe der Einkünfte Ziff. 1 bis 5.5; vereinfacht abgerechnete Löhne (Ziff. 1.3) nicht einbeziehen. Ohne Liegenschaften direkt in Ziff. 20 übertragen, sonst über Ziff. 7/8/9.
- **Bemerkung:** Die Wegleitung 2025 beschreibt Ziff. 6.1/6.2 (ältere Formularstruktur mit Geschäftsfahrzeug-Einkommen); das Formular 2025 hat nur Ziff. 6 (Code 175) und Ziff. 7 (Übertrag von Ziff. 6).
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0008.md) `tg-form-01-2025__c0008` – «6. Zwischentotal der Einkünfte   175»
  - [WL TG 2025 S. 19](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0085.md) `tg-wl-2025__c0085` – «Andernfalls übertragen Sie zuerst den Betrag von Ziffer 6.1 in Ziffer 6.2 der Steuererklärung.»

<a id="7-berechnung-total"></a>
### Ziff. 7 – Übertrag von Ziffer 6 (Staatssteuer / Bundessteuer)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Übertrag Ziff. 6)
- **Regel:** Übertrag des Zwischentotals Ziff. 6 in die beiden Spalten Staatssteuer und Bundessteuer, falls Liegenschaftseinkünfte (Ziff. 8) anfallen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0009.md) `tg-form-01-2025__c0009` – «7. Übertrag von Ziffer 6»

<a id="8-1-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. 8.1 – Einkünfte aus Liegenschaften (Formular 7, Code 180; Staat und Bund getrennt)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Formular 7 Total Nettoerfolge (Code 180), je Spalte Staatssteuer/Bundessteuer
- **Regel:** Zuerst Formular 7 (und bei effektivem Unterhalt Formular 8) ausfüllen. Netto = Eigenmietwert (indexiert, nach Selbstnutzungsabzug) bzw. Mietzinsen abzüglich Unterhalts-/Betriebskosten (Pauschale oder effektiv); negativer Nettoerfolg mit Vorzeichen. Selbstnutzungsabzug nur für am Wohnsitz dauernd selbstbewohntes Eigentum: Kanton 40%, Bund 20%.
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **40 % (Selbstnutzungsabzug 40% vom Eigenmietwert für am Wohnsitz dauernd selbstbewohntes Wohneigentum (Bund 20%); nicht für Zweit-/Ferienwohnungen, landwirtschaftlich geschätzte Liegenschaften oder an Nahestehende überlassene Objekte.)** · Bund **n/a – Eigenmietwert wird nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt (Art. 21 Abs. 2 DBG); Abschaffung per 01.01.2029 beschlossen, 2025–2028 gilt bisheriges Recht. Der Eigenmietwert für die direkte Bundessteuer wird im kantonalen Veranlagungsverfahren festgesetzt; ein dort vorgesehener Abzug für die DBSt (z.B. TG 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Unterhaltspauschale 10% des Bruttomietertrags/Mietwerts/Eigenmietwerts für Gebäude bis zehn Jahre alt (am Ende der Steuerperiode); Wahl pro Liegenschaft und Periode; nicht bei Geschäftsvermögen, unüberbauten Grundstücken, Baurecht.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Unterhaltspauschale 20% für Gebäude, die älter als zehn Jahre sind.)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Bund:** Selbstnutzungsabzug Bund 20% (Kanton 40%) – deshalb unterschiedliche Nettoerfolge je Spalte.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0009.md) `tg-form-01-2025__c0009` – «8.1 Einkünfte aus Liegenschaften   Formular 7 180»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0225.md) `tg-wl-2025__c0225` – «nutzung kantonal einen Abzug von 40% und beim Bund von 20% vornehmen»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0238.md) `tg-wl-2025__c0238` – «10% für Gebäude, die am Ende der Steuerperiode bis zu zehn Jahre alt sind;»

<a id="9-berechnung-total"></a>
### Ziff. 9 – Total der Einkünfte, zu übertragen auf Seite 3 Ziffer 20 (Code 198; Staat/Bund)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 7 + Ziff. 8)
- **Regel:** Ziff. 7 plus Ziff. 8.1, je Spalte Staatssteuer/Bundessteuer; Übertrag in Ziff. 20.
- **Quellen:**
  - [Formular 1 TG 2025 S. 2](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0009.md) `tg-form-01-2025__c0009` – «9. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 20   198»

## Abzüge

<a id="10-1-berechnung-total"></a>
### Ziff. 10.1 – Berufsauslagen bei unselbständiger Erwerbstätigkeit Person 1 (Formular 4.2 Ziff. 7, Code 240; Staat/Bund)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg, Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Formular 4.2 Ziff. 7 Total der abzugsfähigen Berufsauslagen (Code 240)
- **Regel:** Total aus Formular 4.2 (Fahrkosten, Verpflegung, übrige Berufskosten, Wochenaufenthalt, Nebenerwerb) übertragen, je Spalte Staat/Bund (Fahrkostenmaximum und Km-Ansätze unterscheiden sich). Nicht vom Arbeitgeber übernommene Kosten abziehen. Lohnausweis prüfen: Feld F angekreuzt = keine Fahrkosten; Feld G = nur halbe Verpflegung.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «10.1 Person 1   Formular 4.2 240»
  - [WL TG 2025 S. 41](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0196.md) `tg-wl-2025__c0196` – «Tragen Sie in diese Ziffer die Summe der Berufsauslagen gemäss den Ziffern 2 bis 7 ein.»

<a id="10-2-berechnung-total"></a>
### Ziff. 10.2 – Berufsauslagen bei unselbständiger Erwerbstätigkeit Person 2 (Formular 4.3 Ziff. 7, Code 280; Staat/Bund)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg, Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Formular 4.2 Rückseite (Person 2, im Formular als «4.3» bezeichnet) Ziff. 7 (Code 280)
- **Regel:** Wie Ziff. 10.1 für Person 2 (Rückseite des Formulars 4.2, Codes 246–280).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «10.2 Person 2   Formular 4.3 280»
  - [Formular 4.2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0010.md) `tg-form-04-2-2025__c0010` – «7.   Total der abzugsfähigen Berufsauslagen   280»

<a id="11-abzug-schuldzinsen"></a>
### Ziff. 11 – Schuldzinsen (Formular 4.1, Code 290)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen) → Formular 4.1 Ziff. C Total Schuldzinsen (Code 290)
- **Regel:** Nur im Jahr 2025 fällig gewordene Schuldzinsen (keine Ratazinsen); mit der Schlussrechnung belastete Ausgleichszinsen ebenfalls abziehbar. Private Schuldzinsen höchstens im Umfang der deklarierten Erträge aus beweglichem und unbeweglichem Vermögen plus Fr. 50'000. Keine Amortisationen, Bau-/Landkreditzinsen (Anlagekosten), Leasingzinsen; Baurechtszinsen nur bei Fremdvermietung. WEF-Zusatzverbilligungen mindern die Schuldzinsen. Geschäftsschuldzinsen nur, wenn nicht schon in Ziff. 2 abgezogen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «11.   Schuldzinsen   Formular 4.1 290»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «Sie können private Schuldzinsen höchstens im Umfang der deklarierten Erträge aus beweglichem»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «und unbeweglichem Vermögen und weiterer Fr. 50 000 in Abzug bringen.»

<a id="12-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.1 – Unterhaltsbeiträge an Ehegatte/Partner bei Trennung/Scheidung (Empfänger/in, Adresse) (Code 300)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise; Kopie Scheidungs-/Trennungsurteil bei erstmaliger Deklaration
- **Regel:** Tatsächlich bezahlte periodische Beiträge; Name/Adresse der empfangenden Person angeben, sonst kein Abzug. Mietwertanteil aus Überlassung eines Liegenschaftsanteils zählt ebenfalls. Gegenstück bei der empfangenden Person: Ziff. 5.1.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «12.1 Unterhaltsbeiträge an Ehefrau/-mann bzw. Partnerin/Partner»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0087.md) `tg-wl-2025__c0087` – «Die Abzüge für Unterhaltsbeiträge und Rentenleistungen werden nur gewährt, wenn Zahlungs»

<a id="12-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.2 – Unterhaltsbeiträge für minderjährige Kinder (Code 302)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise an den anderen Elternteil; Urteil/Vereinbarung
- **Regel:** Dem anderen Elternteil für die unter dessen Sorge stehenden Kinder überwiesene Beiträge (inkl. Kinderzulagen), längstens bis und mit dem Monat der Mündigkeit. Wer abzieht, hat keinen Anspruch auf den Kinderabzug (Ziff. 25.1).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «12.2 Unterhaltsbeiträge für minderjährige Kinder   302»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0088.md) `tg-wl-2025__c0088` – «träge können längstens bis und mit dem Monat der Mündigkeit des Kindes abgezogen werden.»

<a id="12-3-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.3 – Rentenleistungen (Code 304)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Rentenvertrag; Beiblatt mit Name/Adresse des Empfängers
- **Regel:** Bezahlte Leibrenten sind zu 40% abziehbar; Umfang der Leistungen auf Beiblatt mit Name und Adresse des Empfängers angeben.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «12.3 Rentenleistungen   304»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0088.md) `tg-wl-2025__c0088` – «Im Jahr 2025 bezahlte Leibrenten können zu 40% vom Einkommen abgezogen werden.»

<a id="13-1-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.1 – Beiträge an Säule 3a Person 1, Anschluss 2. Säule (PK) ja/nein (Code 314)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Bescheinigung der Vorsorgeeinrichtung (Bank-/Versicherungsstiftung) über Einzahlungen 2025
- **Regel:** Max. Fr. 7'258 mit Pensionskassenanschluss; ohne 2. Säule 20% des Erwerbseinkommens, max. Fr. 36'288. Feld «Anschluss 2. Säule (PK)» ankreuzen. Voraussetzung: AHV-pflichtige Erwerbstätigkeit im Jahr, Vorsorgevertrag lautet auf die erwerbstätige Person, Erwerbseinkommen ausgewiesen. Höchstbeträge sind zugleich Einzahlungslimiten. Bescheinigung einreichen.
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a mit Anschluss an 2. Säule: 8% des oberen BVG-Grenzbetrags = CHF 7'258 (Steuerperiode 2025).)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug mit Zugehörigkeit zur 2. Säule (8 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a ohne 2. Säule: 20% des Erwerbseinkommens, maximal CHF 36'288 (40% von 90'720; Steuerperiode 2025).)** · Bund **CHF 36'288 (Säule 3a: Höchstabzug ohne 2. Säule (max. 36'288, 40 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Ohne 2. Säule: 20% des Erwerbseinkommens (gilt auch für Unselbständige ohne PK), maximal CHF 36'288.)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. CHF 36'288))**
- **Bund:** Gleiche Höchstbeträge bei der direkten Bundessteuer.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «13.1 Person 1   Anschluss 2. Säule (PK) m ja   314»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0090.md) `tg-wl-2025__c0090` – «Vorsorge (2. Säule) angehören   Fr. 7'258»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0005.md) `tg-stp-34-27__c0005` – «Fr. 7’258 | Fr. 36’288»

<a id="13-2-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.2 – Beiträge an Säule 3a Person 2, Anschluss 2. Säule (PK) ja/nein (Code 315)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Bescheinigung der Vorsorgeeinrichtung für Person 2
- **Regel:** Wie Ziff. 13.1 für Person 2; jede erwerbstätige Person hat einen eigenen Abzug (Vorsorgenehmer).
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a mit Anschluss an 2. Säule: 8% des oberen BVG-Grenzbetrags = CHF 7'258 (Steuerperiode 2025).)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug mit Zugehörigkeit zur 2. Säule (8 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a ohne 2. Säule: 20% des Erwerbseinkommens, maximal CHF 36'288 (40% von 90'720; Steuerperiode 2025).)** · Bund **CHF 36'288 (Säule 3a: Höchstabzug ohne 2. Säule (max. 36'288, 40 % des oberen BVG-Grenzbetrags))**
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0010.md) `tg-form-01-2025__c0010` – «13.2 Person 2   Anschluss 2. Säule (PK) m ja   315»
  - [WL TG 2025 S. 20](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0089.md) `tg-wl-2025__c0089` – «Bei gemeinsam besteuerten Personen (Ehe»

<a id="14-abzug-versicherungspraemien"></a>
### Ziff. 14 – Versicherungsprämien und Zinsen von Sparkapitalien (Formular 5.2, Code 330; Staat/Bund)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Formular 5.2 Abschnitt C (Code 330): tieferer Betrag von «A5» (bezahlte Prämien/Sparzinsen) und «B4» (Maximalabzug), getrennt Staat/Bund
- **Regel:** Abzug = niedrigerer Betrag aus tatsächlichen Prämien+Sparzinsen und Maximum. Maximum Kanton: Fr. 7'000 gemeinsam besteuert / Fr. 3'500 übrige, + Fr. 1'000 je Kind/unterstützte Person. Maximum Bund: Fr. 3'700 / Fr. 1'800 (ohne Beiträge an Säule 2/3a: Fr. 5'550 / Fr. 2'700, nicht kumulierbar), + Fr. 700 je Kind/unterstützte Person. Krankenkassenprämien netto nach Prämienverbilligung (IPV, inkl. EL-Prämienverbilligung) deklarieren; ohne Deklaration der KK-Prämien kann der Abzug verweigert werden.
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

<a id="15-1-abzug-ahv-nichterwerbstaetige"></a>
### Ziff. 15.1 – AHV-Beiträge für nichterwerbstätige Personen (Code 342)

- **Schlüssel:** `abzug.ahv_nichterwerbstaetige` (AHV/IV/EO-Beiträge Nichterwerbstätiger u.ä.) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse) → AHV-Beitragsverfügung/Rechnung Ausgleichskasse
- **Regel:** In der Regel nur AHV/IV/EO- und FAK-Beiträge Nichterwerbstätiger. Beiträge Unselbständiger sind schon im Nettolohn berücksichtigt, solche Selbständiger im Reingewinn (Ziff. 2) – nicht nochmals abziehen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «15.1 AHV-Beiträge für nichterwerbstätige Personen   342»
  - [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0093.md) `tg-wl-2025__c0093` – «Unter dieser Ziffer können in der Regel nur Beiträge an die AHV/IV/EO sowie FAK-Beiträge von»

<a id="15-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 15.2 – Beiträge an Einrichtungen der beruflichen Vorsorge Person 1 / Person 2 (Code 343 / 344)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) für selbst bezahlte, nicht vom Lohn abgezogene Einkäufe; Lohnausweis Ziff. 10.2 nur zur Kontrolle
- **Regel:** Nur soweit nicht im Lohnausweis abgezogen: Lohnausweis Ziff. 10.1 (ordentliche Beiträge) und Ziff. 10.2 (Einkäufe) sind bereits im Nettolohn (Ziff. 11) berücksichtigt und dürfen hier NICHT nochmals abgezogen werden. Selbst entrichtete Einkäufe (Überweisung direkt an die PK) mit Bescheinigung der Vorsorgeeinrichtung. Selbständigerwerbende: nur Privatanteil (Arbeitgeberanteil bereits in Ziff. 2; ohne Personal gilt die Hälfte als Arbeitgeberanteil).
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «15.2 Beiträge an Einrichtungen der beruflichen Vorsorge»
  - [WL TG 2025 S. 21](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0093.md) `tg-wl-2025__c0093` – «Die ordentlichen Beiträge sind in der Regel bereits vom Bruttolohn abgezogen»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «Vom Arbeitnehmer selber entrichtete, d. h. nicht vom Lohn abgezogene Einkaufsbeiträge an»

<a id="15-3-abzug-drittbetreuung"></a>
### Ziff. 15.3 – Kosten für die Drittbetreuung von Kindern unter 14 Jahren (Code 345; Staat/Bund)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ⚠️ strittig
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Rechnungen/Bestätigungen Kita, Tagesmutter, Hort; Nachweis Erwerbstätigkeit/Ausbildung der Eltern
- **Regel:** Kumulativ: Kind unter 14, im Haushalt des unterhaltenden Elternteils, Kosten kausal wegen Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit. Nur echte Betreuungskosten: ohne Gegenbeweis werden 75% der Rechnung anerkannt (100% bei nachgewiesen reinen Betreuungskosten). Maximum pro Kind: Kanton Fr. 10'100; Bund Fr. 25'800. Tagesschule/Internat: pauschal Fr. 800 pro Jahr und Kind (StP 34 Nr. 24). Getrennte Eltern: Abzug beim Elternteil im gleichen Haushalt; bei alternierender Obhut je max. die Hälfte des Maximalbetrags.
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

<a id="15-4-abzug-uebrige"></a>
### Ziff. 15.4 – Weitere Abzüge (nähere Bezeichnung) (Code 346)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Aufstellung/Belege zum jeweiligen Abzug; Prämien NBU, AHV/IV/EO/FAK-Beiträge Erwerbstätiger
- **Regel:** Begründen und belegen. Beispiele: Prämien obligatorische Nichtberufsunfallversicherung (NBUV) oder AHV/IV/EO/FAK-Beiträge Erwerbstätiger, soweit nicht bereits in Ziff. 1/2 berücksichtigt. NICHT hier: Prämien UVG-versicherter Nichterwerbstätiger (→ Ziff. 14), Vermögensverwaltungskosten (→ Formular 2), Einsatzkosten für nicht steuerbare Geldspielgewinne (nicht abziehbar).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «15.4 Weitere Abzüge:   346»
  - [WL TG 2025 S. 22](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0099.md) `tg-wl-2025__c0099` – «Unter dieser Ziffer geltend gemachte Abzüge sind zu begründen und zu belegen.»

<a id="15-5-abzug-parteispenden"></a>
### Ziff. 15.5 – Mitgliederbeiträge und Zuwendungen an politische Parteien (Formular 6, Code 347)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Formular 6 Spalte «politische Parteien», Total (Code 347); Quittung ab Fr. 1'000 pro Zuwendung
- **Regel:** Voraussetzung: Partei im Parteienregister eingetragen und in einem kantonalen Parlament vertreten oder bei letzten Wahlen mind. 3% Stimmenanteil. Maximum Kanton Fr. 10'000, Bund Fr. 10'600. Pauschalvermerke «Spenden an diverse Organisationen» werden nicht anerkannt.
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister, im kantonalen Parlament vertreten oder mind. 3% Stimmen): max. CHF 10'000.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
- **Bund:** Bund max. Fr. 10'600 (Kanton Fr. 10'000).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «15.5 Mitgliederbeiträge und Zuwendungen an politische Parteien   Formular 6 347»
  - [Formular 6 TG 2025 S. 1](../../chunks/tg/2025/tg-form-06-2025/tg-form-06-2025__c0002.md) `tg-form-06-2025__c0002` – «Staatssteuer: max. Fr. 10 000.– Bundessteuer: max. Fr. 10 600.–»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0219.md) `tg-wl-2025__c0219` – «mindestens 3% der Stimmen erreicht hat.»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0008.md) `tg-stp-34-27__c0008` – «2025 | Fr. 10’000 | Fr. 10’600»

<a id="15-6-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 15.6 – Teilbesteuerungsabzug Beteiligungen im Privatvermögen (Formular 2 Hilfsblatt, Code 341; Staat/Bund)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Formular 2 letzte Seite «Hilfsblatt qualifizierte Beteiligungen im Privatvermögen» Ziff. 3
- **Regel:** Für Beteiligungen ≥ 10% am Grund-/Stammkapital im Privatvermögen: Teilbesteuerungsabzug Kanton 40% (steuerbar 60%), Bund 30% (steuerbar 70%) vom Total der Beteiligungserträge. Antrag jedes Jahr über das Hilfsblatt stellen, Nachweis der Voraussetzungen durch die steuerpflichtige Person (sonst 100%). Erträge selbst weiterhin in Spalte 8/9 des Wertschriftenverzeichnisses.
- **Bund:** Teilbesteuerungsabzug Bund 30% (Kanton 40%).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «15.6 Teilbesteuerungsabzug Beteiligungen im Privatvermögen   Formular 2 341»
  - [Formular 2 TG 2025 S. 4](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0008.md) `tg-form-02-2025__c0008` – «3. Teilbesteuerungsabzug (Staatssteuer 40% / Bundessteuer 30%)»
  - [WL TG 2025 S. 34–35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0166.md) `tg-wl-2025__c0166` – «besteuerungsabzugs   3 einzusetzende Teilbesteuerungsabzug beträgt 40% bei den Staats- und Gemeindesteuern und»

<a id="16-1-abzug-weiterbildung"></a>
### Ziff. 16.1 – Berufsorientierte Aus- und Weiterbildungskosten Person 1 (Code 348)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Kursrechnungen/Zahlungsnachweise mit Aufstellung; Lohnausweis Ziff. 13.3 (Arbeitgeberbeiträge)
- **Regel:** Selbst getragene berufsorientierte Aus- und Weiterbildungskosten bis max. Fr. 13'000 pro Person (Kanton und Bund). Ausgenommen: Kosten bis zum Abschluss der Erstausbildung (Berufslehre/Sekundarstufe II); ohne Sek-II-Abschluss erst ab vollendetem 20. Lebensjahr. Nicht an Erwerbstätigkeit im Jahr gebunden. Kostenbeteiligungen Dritter (Arbeitgeber, Bund, Verbände) abziehen; Arbeitgeberbeiträge an die Weiterbildung, die dem Arbeitnehmer vergütet wurden, stehen im Lohnausweis Ziff. 13.3 (direkt an das Bildungsinstitut bezahlte Beträge werden dort nicht bescheinigt, mindern aber ebenfalls die eigenen Kosten). PC/Notebook/Smartphone etc. nur bei spezifischem Lehrgangsbezug mit ca. 50% Privatanteil. Liebhaberei/Selbstentfaltung nicht abziehbar.
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung: max. CHF 13'000 pro Person und Jahr (Kanton und Bund identisch). Ausgenommen Kosten bis zum ersten Abschluss Sekundarstufe II.)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Bund:** Maximum Fr. 13'000 auch beim Bund.
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «16.1 Person 1   348»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0102.md) `tg-wl-2025__c0102` – «maximal Fr. 13'000 pro Person beschränkt.»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0102.md) `tg-wl-2025__c0102` – «Kostenbeteiligungen Dritter (z.B. Arbeitgebende, Bund, Branchenverbände etc.) mindern die ab»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «In diesem Feld sind alle effektiven Vergütungen des Arbeitgebers für berufsorientierte Aus-»

<a id="16-2-abzug-weiterbildung"></a>
### Ziff. 16.2 – Berufsorientierte Aus- und Weiterbildungskosten Person 2 (Code 349)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Kursrechnungen/Zahlungsnachweise für Person 2; Lohnausweis Ziff. 13.3
- **Regel:** Wie Ziff. 16.1 für Person 2 (Maximum Fr. 13'000 pro Person).
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung: max. CHF 13'000 pro Person und Jahr (Kanton und Bund identisch). Ausgenommen Kosten bis zum ersten Abschluss Sekundarstufe II.)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «16.2 Person 2   349»
  - [WL TG 2025 S. 22–23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0102.md) `tg-wl-2025__c0102` – «Der Abzug ist sowohl bei den Staats- und Gemeindesteuern als auch bei der direkten Bundessteuer»

<a id="17-abzug-behinderungskosten"></a>
### Ziff. 17 – Behinderungsbedingte Kosten (Formular 5.1 Abschnitt C, Code 350)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung, Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Formular 5.1 Abschnitt C: Aufwendungen (A) abzüglich Vergütungen Dritter (B)
- **Regel:** Selbst getragene behinderungsbedingte Kosten vollständig abziehbar (ohne Selbstbehalt), alternativ jährliche Pauschalen: gehörlos Fr. 2'500, Dialyse Fr. 2'500, Hilflosenentschädigung leicht Fr. 2'500 / mittel Fr. 5'000 / schwer Fr. 7'500. Vergütungen Dritter (Krankenkasse, IV-Hilfsmittel, Hilflosenentschädigung, Pflegefinanzierung) und Anteil Lebenshaltungskosten (bei Heim i.d.R. Fr. 2'000/Monat) abziehen. Krankheits- und Unfallkosten gehören auch bei Behinderten in Ziff. 23.1 (mit Selbstbehalt).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «17.   Behinderungsbedingte Kosten   Formular 5 350»
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0003.md) `tg-form-05-1-2025__c0003` – «Abzugsfähige behinderungsbedingte Kosten   350»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0202.md) `tg-wl-2025__c0202` – «– Bezügerinnen/Bezüger einer Hilflosenentschädigung mittleren Grades   Fr. 5'000»

<a id="18-abzug-zweiverdiener"></a>
### Ziff. 18 – Zweiverdienerabzug (Code 356) – nur direkte Bundessteuer

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Berechnung aus Erwerbseinkommen beider Personen (Nettolohn bzw. Reingewinn abzüglich Berufsauslagen, Säule 2 und 3a)
- **Regel:** Nur Bundesspalte: 50% des niedrigeren Erwerbseinkommens der gemeinsam besteuerten Personen, mindestens Fr. 8'600 und höchstens Fr. 14'100 (2025). Liegt das niedrigere Erwerbseinkommen unter Fr. 8'600, kann nur dieser Betrag abgezogen werden. Erwerbseinkommen = Einkünfte nach Berufsauslagen sowie Beiträgen Säule 2/3a; Erwerbsausfallentschädigungen zählen mit; im vereinfachten Verfahren versteuerte Löhne zählen nicht. Kanton: kein Zweiverdienerabzug.
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

<a id="19-berechnung-total"></a>
### Ziff. 19 – Total Abzüge, zu übertragen in Ziffer 21 (Code 360; Staat/Bund)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 10–18)
- **Regel:** Summe der Abzüge Ziff. 10 bis 18, je Spalte Staatssteuer/Bundessteuer; Übertrag in Ziff. 21.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0011.md) `tg-form-01-2025__c0011` – «19.   Total Abzüge, zu übertragen in Ziffer 21   360»

## Einkommensberechnung

<a id="20-berechnung-total"></a>
### Ziff. 20 – Total der Einkünfte, Übertrag von Seite 2 (Ziffer 6 oder 9)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Übertrag Ziff. 6 bzw. 9)
- **Regel:** Ohne Liegenschaften Ziff. 6, mit Liegenschaften Ziff. 9 übertragen; Vorzeichen bei negativem Betrag.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «20.   Total der Einkünfte, Übertrag von Seite 2 (Ziffer 6 oder 9)»

<a id="21-berechnung-total"></a>
### Ziff. 21 – Total der Abzüge, Übertrag von Ziffer 19

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Übertrag Ziff. 19)
- **Regel:** Übertrag Total Abzüge Ziff. 19, je Spalte Staat/Bund.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «21.   Total der Abzüge, Übertrag von Ziffer 19»

<a id="22-berechnung-total"></a>
### Ziff. 22 – Nettoeinkommen (Code 362; Staat/Bund)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 20 minus Ziff. 21)
- **Regel:** Basis für den Selbstbehalt Krankheitskosten (5%) und das Maximum der Zuwendungen (20%): Staats- und Bundesspalte getrennt verwenden.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «22.   Nettoeinkommen   362»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0206.md) `tg-wl-2025__c0206` – «ziehen Sie einen Selbstbehalt von 5% des Nettoeinkommens gemäss Ziffer 22 der Steuererklä»

<a id="23-1-abzug-krankheitskosten"></a>
### Ziff. 23.1 – Krankheits- und Unfallkosten (Formular 5.1 Abschnitt D, Code 364; Staat/Bund)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 5.1 Abschnitt D: (A Aufwendungen – B Vergütungen) abzüglich 5% Selbstbehalt von Ziff. 22
- **Regel:** Selbst getragene Kosten über 5% des Nettoeinkommens (Ziff. 22; Staat und Bund je mit eigener Spalte) für sich und Personen mit Kinder-/Unterstützungsabzug. Vergütungen der Krankenkasse/Versicherungen/Hilflosenentschädigung und Anteil Lebenshaltungskosten abziehen. Nicht abziehbar: Krankenkassenprämien, Fahrkosten zum Arzt (ausser dauernde Pflegebedürftigkeit), Fitness/Schönheitsbehandlungen, nicht ärztlich verordnete Akupunktur/Prävention. Diät-Pauschale Fr. 2'500 bei lebensnotwendiger Diät (z.B. Zöliakie, nicht Diabetes), ausgeschlossen bei Leistungen Dritter. Belege zusammenstellen und einreichen.
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5% des Nettoeinkommens (Ziff. 22 der Steuererklärung).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Bund:** Selbstbehalt 5% des Bundes-Nettoeinkommens (rechte Spalte Ziff. 22).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «23.1 Krankheits- und Unfallkosten   Formular 5 364»
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0004.md) `tg-form-05-1-2025__c0004` – «abzüglich Selbstbehalt (5% von Ziffer 22 der Steuererklärung)»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0197.md) `tg-wl-2025__c0197` – «Soweit Sie die Kosten selber tragen und diese 5% des Nettoeinkommens (Ziffer 22) übersteigen,»
  - [WL TG 2025 S. 42](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0198.md) `tg-wl-2025__c0198` – «labzug ist in jedem Fall mangels selbst getragenen Mehrkosten ausgeschlossen, wenn Leistungen»

<a id="23-2-abzug-spenden"></a>
### Ziff. 23.2 – Freiwillige Zuwendungen (Formular 6, Code 366; Staat/Bund)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Formular 6 Spalte «gemeinnützige oder öffentliche Zwecke» (Code 366); Bestätigung ab Fr. 1'000 pro Zuwendung
- **Regel:** Zuwendungen an in der Schweiz ansässige steuerbefreite Institutionen (öffentliche/gemeinnützige Zwecke; Liste der Steuerverwaltung). Kanton: Selbstbehalt Fr. 200 (nur der übersteigende Betrag), max. Fr. 8'000 bei Nettoeinkommen bis Fr. 40'000, sonst max. 20% des Nettoeinkommens (Ziff. 22). Bund: ab Gesamtbetrag Fr. 100, ohne Selbstbehalt, max. 20% des Nettoeinkommens. Nicht abziehbar: religiöse, wohltätige, kulturelle, gesellige, sportliche Zwecke, Auslandssitz, ehrenamtliche Arbeit; keine Sammelvermerke.
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 200 (Freiwillige Zuwendungen kantonal nur abziehbar, soweit gesamthaft CHF 200 übersteigend (Bund: ab CHF 100).)** · Bund **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen (CH) bzw. Gemeinwesen: mindestens CHF 100 im Steuerjahr)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Maximal 20% des Nettoeinkommens (Ziff. 22); bei Nettoeinkommen bis CHF 40'000 maximal CHF 8'000. Nur an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentliche/gemeinnützige Zwecke) sowie Bund/Kantone/Gemeinden.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Bund:** Bund: Mindestbetrag Fr. 100 (Gesamtbetrag), ohne Selbstbehalt, max. 20% des Nettoeinkommens; Kanton: Selbstbehalt Fr. 200, max. Fr. 8'000 bzw. 20%.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «23.2 Freiwillige Zuwendungen   Formular 6 366»
  - [Formular 6 TG 2025 S. 1](../../chunks/tg/2025/tg-form-06-2025/tg-form-06-2025__c0002.md) `tg-form-06-2025__c0002` – «Nettoeinkommen (gem. Ziff. 22) über Fr. 40000.–: max. 20% vom Nettoeinkommen   366»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0218.md) `tg-wl-2025__c0218` – «Soweit die freiwilligen Zuwendungen gesamthaft Fr. 200 übersteigen, können Sie kantonal bei ei»

<a id="23-3-abzug-uebrige"></a>
### Ziff. 23.3 – Separat zu besteuernde Liquidationsgewinne (Code 368; Staat/Bund)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Berechnung Liquidationsgewinn (Formular 14a), Geschäftsabschlüsse der letzten zwei Jahre
- **Regel:** Bei definitiver Geschäftsaufgabe nach vollendetem 55. Altersjahr oder wegen Invalidität: in den letzten zwei Geschäftsjahren realisierte stille Reserven werden getrennt privilegiert besteuert; hier den in Ziff. 2.1/2.2 enthaltenen Liquidationsgewinn von den ordentlichen Einkünften abziehen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «23.3 Separat zu besteuernde Liquidationsgewinne   368»
  - [WL TG 2025 S. 23](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0106.md) `tg-wl-2025__c0106` – «Erfüllen Sie die entsprechenden Voraussetzungen, können Sie die im Geschäftsergebnis in den»

<a id="24-berechnung-total"></a>
### Ziff. 24 – Reineinkommen (Ziffer 22 abzüglich Ziffern 23.1 bis 23.3) (Code 372)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Ziff. 22 minus Ziff. 23.1–23.3, je Spalte Staat/Bund. Das Reineinkommen (Staat) ist satzbestimmend für den Abzug Ziff. 25.3.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0012.md) `tg-form-01-2025__c0012` – «24.   Reineinkommen (Ziffer 22 abzüglich Ziffern 23.1 bis 23.3)   372»

<a id="25-1-a-jg-2000-2005-sozialabzug-kinder"></a>
### Ziff. 25.1 a) Jg. 2000–2005 – Kinderabzug für jedes Kind in Ausbildung mit Jahrgang 2000–2005 (Code 380; Staat Fr. 10'600 / Bund Fr. 6'800)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1 (Kinder: Geburtsdatum, Ausbildung); Anzahl Kinder
- **Regel:** Pro Kind in Ausbildung (Stichtag 31.12.2025): Kanton Fr. 10'600, Bund Fr. 6'800. Nur eigene Kinder (nicht Pflege-/Stiefkinder); kein Abzug, wenn das volljährige Kind ein Einkommen für den selbständigen Lebensunterhalt erzielt. Zuteilung bei getrennt besteuerten Eltern nach Alimenten/Sorgerecht/Obhut; Kanton und Bund haben unterschiedliche Regeln (Kanton hälftig nur bei gemeinsamem Sorgerecht UND alternierender Obhut ohne Alimente).
- **Limiten:**
  - Ausbildungsabzug auswärtige Ausbildung/höhere Stufe (CHF): Kanton **CHF 10'600 (Kinderabzug in Ausbildung nach Vollendung des 20. Altersjahres bis höchstens zum vollendeten 26. Altersjahr: CHF 10'600 (WL 2025: Jahrgang 2000-2005). Keine Unterscheidung nach auswärtiger Ausbildung; Abstufung erfolgt nach Alter.)** · Bund **n/a – Bund: gleicher Kinderabzug CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 7'400 (Kinderabzug je Kind (nicht selbständig besteuert, in Ausbildung oder erwerbsunfähig; Steuerpflichtiger kommt für Unterhalt auf): CHF 7'400. Stichtag Ende Steuerperiode.)** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
- **Bund:** Bund Fr. 6'800 pro Kind (alle Jahrgänge).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «25.1 a) für jedes Kind in Ausbildung mit Jahrg. 2000 – 2005   Fr. 10 600   Fr. 6800   380»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0006.md) `tg-stp-36-1__c0006` – «- 20. Altersjahres bis zum vollendeten 26. Altersjahres | Fr. 10’600»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0108.md) `tg-wl-2025__c0108` – «Erzielt ein volljähriges Kind, obwohl es eine Ausbildung absolviert, ein Einkommen, das einen selb»

<a id="25-1-a-jg-2006-2009-sozialabzug-kinder"></a>
### Ziff. 25.1 a) Jg. 2006–2009 – Kinderabzug für jedes Kind in Ausbildung mit Jahrgang 2006–2009 (Code 382; Staat Fr. 8'500 / Bund Fr. 6'800)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1 (Kinder: Geburtsdatum, Ausbildung)
- **Regel:** Kinder ab vollendetem 16. Altersjahr in Ausbildung: Kanton Fr. 8'500, Bund Fr. 6'800. Zuteilungs- und Stichtagsregeln wie bei Code 380.
- **Limiten:**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 8'500 (Kinderabzug erhöht sich für jedes in Ausbildung stehende Kind nach Vollendung des 16. Altersjahres auf CHF 8'500 (WL 2025: Jahrgang 2006-2009).)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Kinderabzug CHF 6'800 wie für Minderjährige (kein höherer Ausbildungsabzug))**
- **Bund:** Bund Fr. 6'800.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «mit Jahrg. 2006 – 2009   Fr. 8 500   Fr. 6800   382»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0006.md) `tg-stp-36-1__c0006` – «- 16. Altersjahres auf | Fr. 8’500»

<a id="25-1-b-sozialabzug-kinder"></a>
### Ziff. 25.1 b) – Kinderabzug für jedes übrige Kind (Code 384; Staat Fr. 7'400 / Bund Fr. 6'800)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1 (Kinder: Geburtsdatum)
- **Regel:** Alle übrigen (nicht selbständig besteuerten, minderjährigen oder erwerbsunfähigen) Kinder: Kanton Fr. 7'400, Bund Fr. 6'800. Kinder mit Alimentenbezug (Ziff. 5.2): Abzug beim empfangenden Elternteil. Zusätzlich: Steuergutschrift Ziff. 28.1 und Versicherungs-/Vermögensfreibetrag je Kind.
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 7'400 (Kinderabzug je Kind (nicht selbständig besteuert, in Ausbildung oder erwerbsunfähig; Steuerpflichtiger kommt für Unterhalt auf): CHF 7'400. Stichtag Ende Steuerperiode.)** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
- **Bund:** Bund Fr. 6'800.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «b) für jedes übrige Kind   Fr. 7 400   Fr. 6800   384»
  - [WL TG 2025 S. 23–24](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0108.md) `tg-wl-2025__c0108` – «für jedes übrige Kind   Fr. 7'400   Fr. 6'800»

<a id="25-2-sozialabzug-unterstuetzung"></a>
### Ziff. 25.2 – Unterstützungsabzug für jede unterstützte Person (Code 386; Staat Fr. 2'700 / Bund Fr. 6'800)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1 (Erwerbsunfähige und unterstützungsbedürftige Personen); Bestätigung der Wohnsitzgemeinde/Fürsorgebehörde
- **Regel:** Kanton Fr. 2'700, wenn zur Hauptsache für den Unterhalt einer erwerbsunfähigen, unterstützungsbedürftigen Person aufgekommen wird (Praxis: mind. 50% des betreibungsrechtlichen Existenzminimums). Bund Fr. 6'800 bei nachgewiesenem Beitrag von mind. Fr. 6'800. Nicht für Ehegatte oder Kinder mit Kinderabzug/Unterhaltsabzug.
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'700 (Unterstützungsabzug CHF 2'700 je erwerbsunfähige/unterstützungsbedürftige Person, für deren Unterhalt der Steuerpflichtige zur Hauptsache aufkommt (nicht für Ehegatten und Kinder mit Kinderabzug).)** · Bund **CHF 6'800 (Unterstützungsabzug pro erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mindestens in Höhe des Abzugs unterstützt; nicht für Ehegatten und Kinder mit Kinderabzug)**
- **Bund:** Bund Fr. 6'800 (Kanton Fr. 2'700).
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «25.2 für jede unterstützte Person   Fr. 2 700   Fr. 6800   386»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0006.md) `tg-stp-36-1__c0006` – «Für jede unterstützte Person | Fr. 2’700 | Fr. 2’700»
  - [WL TG 2025 S. 24–25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0114.md) `tg-wl-2025__c0114` – «dürftigen Person auf, können Sie kantonal Fr. 2 700 abziehen.»

<a id="25-3-sozialabzug-alter-iv"></a>
### Ziff. 25.3 – Abzug für Personen mit AHV-Altersrenten sowie erwerbsunfähige oder verwitwete Personen (Code 388; nur Staat)

- **Schlüssel:** `sozialabzug.alter_iv` (Abzug für Personen im AHV-Alter, erwerbsunfähig oder verwitwet (kantonal)) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Reineinkommen Ziff. 24 (Staat); Rentenbescheinigung AHV/IV
- **Regel:** Nur Staats-/Gemeindesteuer: max. Fr. 4'200, abnehmend nach satzbestimmendem Reineinkommen Ziff. 24 (Alleinstehende voll bis Fr. 17'899, Ehepaare bis Fr. 25'299; je volle Fr. 1'000 Mehreinkommen Reduktion um Fr. 200; kein Abzug ab Fr. 37'900 bzw. Fr. 45'300). Tabelle in der Wegleitung (S. 25).
- **Limiten:**
  - Abzug AHV-Alter/erwerbsunfähig/verwitwet (CHF): Kanton **CHF 4'200 (Abzug für Steuerpflichtige im AHV-Alter, erwerbsunfähige oder verwitwete: max. CHF 4'200; ermässigt sich bei Reineinkommen über CHF 16'900 (in ungetrennter Ehe über CHF 24'300) je CHF 1'000 Mehreinkommen um CHF 200. Bund: kein Abzug.)** · Bund **n/a – Kantonaler Schlüssel; Art. 35 DBG kennt nur Kinder-, Unterstützungs- und Verheiratetenabzug.**
- **Bund:** Bund: kein Abzug.
- **Bemerkung:** Wegleitungstabelle: Zeile '36'900–37'689' ist offensichtlich ein Druckfehler für 37'899 (Gesetz/VAKP: Reduktion in 1'000er-Schritten bis 0 bei 37'900 bzw. 45'300); Tabelle vor Anwendung gegen WL S. 25 prüfen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «25.3 für Personen mit AHV-Altersrenten sowie erwerbsunfähige oder verwitwete Personen   388»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0116.md) `tg-wl-2025__c0116` – «bis   17'899   bis   25'299   4'200»
  - [VAKP TG § 1](../../chunks/tg/2025/tg-vakp/tg-vakp__par-1.md) `tg-vakp__par-1` – «beträgt das Reineinkommen mehr als Fr. 16'900, bei Steuerpflichtigen in ungetrennter Ehe mehr als Fr. 24'300, ermässigt sich der Abzug je Fr. 1'000 Mehreinkommen um Fr. 200»

<a id="25-4-sozialabzug-verheiratete"></a>
### Ziff. 25.4 – Abzug für gemeinsam besteuerte Personen (Code 390; nur Bund Fr. 2'800)

- **Schlüssel:** `sozialabzug.verheiratete` (Verheiratetenabzug (Bund)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Zivilstand)
- **Regel:** Nur direkte Bundessteuer: Fr. 2'800 für gemeinsam besteuerte Eheleute/Partner; bei Staats- und Gemeindesteuern kein solcher Abzug.
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
- **Regel:** Reineinkommen Ziff. 24 minus Sozialabzüge Ziff. 25.1–25.4, je Spalte Staat/Bund.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «26.   STEUERBARES EINKOMMEN (Ziffer 24 abzüglich Ziffern 25.1 bis 25.4)   398»

<a id="28-1-sozialabzug-kinder"></a>
### Ziff. 28.1 – Steuergutschrift Kanton für minderjährige Kinder (Anzahl Kinder)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Anzahl minderjährige Kinder mit Kinderabzug (Formular 1 Seite 1)
- **Regel:** Kein Abzug vom Einkommen, sondern Steuergutschrift mit der Schlussrechnung: max. Fr. 100 je minderjähriges Kind mit Kinderabzug; keine Auszahlung über den Steuerbetrag hinaus. Nur Anzahl eintragen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «28.1 Kanton: Steuergutschrift für minderjährige Kinder   Anzahl Kinder»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0118.md) `tg-wl-2025__c0118` – «gutschrift von maximal Fr. 100.»

<a id="28-2-sozialabzug-kinder"></a>
### Ziff. 28.2 – Bund: Ermässigung Steuerbetrag für Kinder und unterstützungsbedürftige Personen (Anzahl Personen)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Anzahl Kinder/unterstützte Personen im gleichen Haushalt (Elterntarif)
- **Regel:** Kein Einkommensabzug: Abzug vom Steuerbetrag Fr. 263 pro Kind bzw. unterstützte Person (Elterntarif), für Personen, die mit Kindern/unterstützungsbedürftigen Personen im gleichen Haushalt leben und deren Unterhalt zur Hauptsache bestreiten. Nur Anzahl eintragen.
- **Limiten:**
  - Abzug vom Steuerbetrag pro Kind (CHF, Bund): Kanton **n/a – Ermässigung vom Steuerbetrag (Elterntarif, CHF 263 pro Kind) nur bei der direkten Bundessteuer; kantonal Elterntarif über Divisor 2.0 (§ 37 Abs. 2 StG).** · Bund **CHF 263 (Ermässigung des Steuerbetrags pro Kind bzw. unterstützungsbedürftige Person (Elterntarif: Ehepaare und Alleinstehende mit Kindern im gleichen Haushalt))**
- **Bund:** Nur Bund: Fr. 263 pro Kind/unterstützte Person vom Steuerbetrag.
- **Quellen:**
  - [Formular 1 TG 2025 S. 3](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0013.md) `tg-form-01-2025__c0013` – «28.2 Bund: Ermässigung Steuerbetrag für Kinder und unterstützungsbedürftige Personen   Anzahl Personen»
  - [WL TG 2025 S. 25](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0119.md) `tg-wl-2025__c0119` – «Fr. 263 pro Kind und/oder pro unterstützte Person vom Steuerbetrag geltend machen.»
  - [StP 36 Nr. 1](../../chunks/tg/dauernd/tg-stp-36-1/tg-stp-36-1__c0007.md) `tg-stp-36-1__c0007` – «Ermässigung Steuerbetrag pro Kind\* | Fr. 263 | Fr. 259»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben (Formular 2, Code 410)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 Ziff. 9 Total Steuerwert (Code 410); Bank-/Postauszüge per 31.12.2025
- **Regel:** Steuerwert per 31.12.2025 (kotiert: Börsenkurs Ende Dezember bzw. Kursliste ESTV; nicht kotiert: Verkehrswert). Ansprüche gegen PK, Freizügigkeitskonten und Säule 3a bis zur Fälligkeit steuerfrei – nicht deklarieren. Vermögen und Erträge von Kindern unter elterlicher Sorge (Jahrgang 2008 und jünger) mitdeklarieren.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «30.1 Wertschriften und Guthaben   Formular 2 410»
  - [WL TG 2025 S. 30–31](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0143.md) `tg-wl-2025__c0143` – «Für in der Schweiz kotierte Wertpapiere gilt der Börsenkurs Ende des Monats Dezember 2025.»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 412)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bestandesaufnahme per 31.12.2025; Kursliste ESTV
- **Regel:** Inländisches Bargeld mit Bestand; ausländisches Bargeld, Gold und Edelmetalle zum Verkehrswert per 31.12.2025 (amtliche Kursliste).
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «30.2 Bargeld, Gold und andere Edelmetalle   412»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0122.md) `tg-wl-2025__c0122` – «Inländisches Bargeld ist mit dem Bestand per 31. Dezember 2025 aufzuführen.»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen, Rückkaufswert inkl. Überschussguthaben (Code 420)

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Steuerwertbescheinigung des Versicherers per 31.12.2025
- **Regel:** Steuerwert = Rückkaufswert inkl. Überschuss-/Gewinnanteile; auch Rentenversicherungen während der Rentenlaufzeit. Pro Police Gesellschaft, Abschluss-/Ablaufjahr, Versicherungssumme und Steuerwert erfassen; Bescheinigung beilegen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «Total Steuerwert Lebens- und Rentenversicherungen   420»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0122.md) `tg-wl-2025__c0122` – «Kapital- und Rentenversicherungen unterliegen mit ihrem Steuerwert (Rückkaufswert inkl. Über»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge (Marke, Kaufpreis, Anschaffungsjahr) (Code 422)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Fahrzeugausweis/Kaufvertrag (Kaufpreis, Anschaffungsjahr)
- **Regel:** Verkehrswert per 31.12.2025: Kaufpreis abzüglich 20% pro Jahr seit Erwerb; vor mehr als 5 Jahren gekaufte Fahrzeuge pro memoria Fr. 1.–. Geleaste Fahrzeuge nicht deklarieren. Oldtimer/Liebhaberfahrzeuge zum Verkehrswert unter Ziff. 30.6.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «Total Steuerwert der Motorfahrzeuge   422»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0123.md) `tg-wl-2025__c0123` – «Für die Ermittlung des Verkehrswerts kann pro Jahr seit Erwerb eine Wertvermin»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Anteile an unverteilten Erbschaften (Formular 3) (Code 424)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Inventar/Aufstellung der Erbengemeinschaft
- **Regel:** Anteil am Vermögen nach Erbquote; Ertragsanteil in Ziff. 5.3. Bei Erbanfall ≥ Fr. 50'000 während der Steuerperiode wird das hinzugekommene Vermögen ab Erbanfall (nicht für das ganze Jahr) besteuert.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «30.5 Anteile an unverteilten Erbschaften   Formular 3 424»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0123.md) `tg-wl-2025__c0123` – «Die Anteile an unverteilten Erbschaften und Nutzniessungen werden den einzelnen erbenden oder»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte, nähere Bezeichnung (Code 426)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung zum Verkehrswert per 31.12.2025
- **Regel:** Wohnwagen, Wohnmobile, Oldtimer, Boote, Flugzeuge, Reitpferde, Kunst/Schmuck, Sammlungen, immaterielle Güter: genau bezeichnen, Verkehrswert per 31.12. Hausrat ist steuerfrei.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0014.md) `tg-form-01-2025__c0014` – «30.6 Übrige Vermögenswerte, nähere Bezeichnung:   426»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0123.md) `tg-wl-2025__c0123` – «Unter die übrigen Vermögenswerte fallen z.B. Wohnwagen, Wohnmobile, Oldtimer, Liebhaberfahr»

<a id="31-vermoegen-liegenschaften"></a>
### Ziff. 31 – Liegenschaften (Formular 7, Code 430)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Formular 7 Total Steuerwerte (Code 430); Liegenschaftensteuerrechnung / amtliche Schätzung
- **Regel:** Rechtskräftiger amtlicher Verkehrswert am Ende der Steuerperiode (landwirtschaftliche Liegenschaften: Ertragswert). Ausserkantonale/ausländische Liegenschaften zum dortigen Steuerwert; Anpassung (Repartitionswert) durch die Veranlagungsbehörde. Unfertige Bauten: noch nicht geschätzte Investitionen angemessen berücksichtigen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «31.   Liegenschaften   Formular 7 430»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0239.md) `tg-wl-2025__c0239` – «Für nichtlandwirtschaftliche Liegenschaften geben Sie den am Ende der Steuerperiode bzw. der»

<a id="32-1-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.1 – Geschäftskapital in Kollektiv- und Kommanditgesellschaft (Code 440)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bescheinigung der Gesellschaft über den Vermögensanteil
- **Regel:** Anteil am Vermögen der Gesellschaft gemäss Bescheinigung der Gesellschaft; die Gesellschaft wird nicht als Einheit besteuert.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «32.1 Geschäftskapital in Kollektiv- und Kommanditgesellschaft   440»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0124.md) `tg-wl-2025__c0124` – «Kollektiv- und Kommanditgesellschaften werden nicht als Einheit besteuert.»

<a id="32-2-32-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.2–32.5 – Betriebsvermögen Einzelfirma: Bankkonti/Wertschriften/Guthaben, Vorräte, Viehhabe, Anlagevermögen ohne Grundeigentum

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz bzw. unterzeichnete Aufstellung Aktiven/Passiven
- **Regel:** Wertschriften zum bilanzierten Wert; Debitoren mit vollen Forderungsbeträgen; Vorräte zu Anschaffungs-/Herstellungskosten oder tieferem Marktpreis; Anlagevermögen zum Verkehrswert. Liegenschaften in Ziff. 31 (nicht hier). Unterzeichnete Bilanz/Erfolgsrechnung beilegen.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «32.5 Anlagevermögen ohne Grundeigentum (Fahrzeuge, Maschinen/Mobiliar usw.)»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0125.md) `tg-wl-2025__c0125` – «Setzen Sie das Anlagevermögen wie Maschinen, Werkzeuge, Mobilien oder Fahrzeuge mit dem»

<a id="32-6-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.6 – Total Geschäftsvermögen (Ziffern 32.2 bis 32.5) oder lt. Bilanz (Code 442)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Rechenzeile / Bilanz
- **Regel:** Summe 32.2–32.5 oder Eigenkapital gemäss Bilanz. Die Steuerverwaltung meldet das arbeitende Eigenkapital der Ausgleichskasse.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «32.6 Total Geschäftsvermögen (Ziffern 32.2 bis 32.5) oder lt. Bilanz   Fr.   442»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Ziffern 30.1 bis 32.6) (Code 464)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Summe Ziff. 30.1 bis 32.6 (nur Staats- und Gemeindesteuer; das Vermögen wird nur kantonal besteuert).
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «33.   Total der Vermögenswerte (Ziffern 30.1 bis 32.6)   464»
  - [WL TG 2025 S. 26](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0120.md) `tg-wl-2025__c0120` – «Das Vermögen wird nur kantonal besteuert.»

<a id="34-schulden-privat"></a>
### Ziff. 34 – Schulden (Formular 4.1, Code 466)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Leasingvertrag Fahrzeug / Leasingraten-Abrechnung → Formular 4.1 Ziff. C Total Privat- und Geschäftsschulden (Code 466); Bank-/Gläubigerbestätigungen per 31.12.2025
- **Regel:** Schuldenverzeichnis mit Gläubiger (genaue Adresse), Zinssatz, Schuld am 31.12. und fälligen Schuldzinsen. Rentenverpflichtungen mit Barwert, wenn gegen Entgelt zugesichert. Totale: Schulden → Ziff. 34, Schuldzinsen → Ziff. 11.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «34.   Schulden   Formular 4.1 466»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0127.md) `tg-wl-2025__c0127` – «Deklarieren Sie Schulden, füllen Sie das Formular 4.1»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Reinvermögen (Ziffer 33 abzüglich Ziffer 34) (Code 468)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Ziff. 33 minus Ziff. 34.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0015.md) `tg-form-01-2025__c0015` – «35.   Reinvermögen (Ziffer 33 abzüglich Ziffer 34)   468»

<a id="36-1-vermoegen-sozialabzug"></a>
### Ziff. 36.1 – Steuerfreier Abzug für gemeinsam besteuerte Personen Fr. 200'000 (Code 470)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand (Stichtag 31.12.2025)
- **Regel:** Fr. 200'000 für gemeinsam besteuerte Personen (Stichtag 31.12.2025 bzw. Ende der Steuerpflicht).
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 200'000 (Steuerfreier Betrag auf dem Reinvermögen für Steuerpflichtige in ungetrennter Ehe: CHF 200'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0016.md) `tg-form-01-2025__c0016` – «36.1 Abzug für gemeinsam besteuerte Personen (Eheleute / Partnerinnen oder Partner)   Fr. 200000   470»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0128.md) `tg-wl-2025__c0128` – «– gemeinsam besteuerte Personen   Fr. 200'000»

<a id="36-2-vermoegen-sozialabzug"></a>
### Ziff. 36.2 – Steuerfreier Abzug für alleinstehende Personen Fr. 100'000 (Code 472)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand (Stichtag 31.12.2025)
- **Regel:** Fr. 100'000 für ledige, getrenntlebende, geschiedene oder verwitwete Personen.
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 100'000 (Steuerfreier Betrag auf dem Reinvermögen für übrige (nicht in ungetrennter Ehe lebende) Steuerpflichtige: CHF 100'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0016.md) `tg-form-01-2025__c0016` – «36.2 Abzug für alleinstehende Personen   Fr. 100000   472»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0128.md) `tg-wl-2025__c0128` – «– ledige, getrenntlebende, geschiedene oder verwitwete Personen   Fr. 100'000»

<a id="36-3-vermoegen-sozialabzug"></a>
### Ziff. 36.3 – Steuerfreier Abzug für jedes nicht selbständig besteuerte Kind, Jahrgang 2008 und jünger, Fr. 100'000 (Code 474)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1 (Kinder: Geburtsdatum)
- **Regel:** Fr. 100'000 pro Kind (Jahrgang 2008 und jünger). Im Mündigkeitsjahr werden Kinder selbständig besteuert – dann kein Freibetrag der Eltern. Bei getrennt besteuerten Eltern erhält ihn der Elternteil mit Kinderabzug; hälftige Teilung nur bei gemeinsamem Sorgerecht, alternierender Obhut und ohne Alimente.
- **Limiten:**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 100'000 (Zusätzlich CHF 100'000 für jedes nicht selbständig besteuerte Kind.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0016.md) `tg-form-01-2025__c0016` – «36.3 Abzug für jedes nicht selbständig besteuerte Kind (Jahrgang 2008 und jüngere)   Fr. 100000   474»
  - [WL TG 2025 S. 27](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0128.md) `tg-wl-2025__c0128` – «– für jedes nicht selbständig besteuerte Kind (Jahrgang 2008 und jünger)   Fr. 100'000»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen gesamt (Ziffer 35 abzüglich Ziffern 36.1 bis 36.3) (Code 498)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Ziff. 35 minus Ziff. 36.1–36.3.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0016.md) `tg-form-01-2025__c0016` – «37.   STEUERBARES VERMÖGEN GESAMT (Ziffer 35 abzüglich Ziffern 36.1 bis 36.3)   498»

## Weitere Angaben

<a id="seite-4-schenkungen-info-schenkungen-erbschaften"></a>
### Ziff. Seite 4 Schenkungen – Schenkungen und erbrechtliche Vermögensanfälle (erhalten/ausgerichtet 2025)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Formular 1 Seite 4: Datum, Wert, Name/Adresse/Verwandtschaftsgrad; bei mehreren Hilfsblätter 'jahresunabhängige Formulare'
- **Regel:** Alle 2025 getätigten oder empfangenen Schenkungen, Erbvorbezüge, Erbschaften und Beteiligungen an Erbengemeinschaften mit Datum, Betrag, Geber/Empfänger (inkl. Adresse) und Verwandtschaftsgrad angeben. Bei Erbanfall ≥ Fr. 50'000 Vermögensgewichtung ab Erbanfall.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0017.md) `tg-form-01-2025__c0017` – «Schenkungen und erbrechtliche Vermögensanfälle»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0129.md) `tg-wl-2025__c0129` – «Führen Sie sämtliche im Jahre 2025 getätigten oder empfangenen Schenkungen und Erbvorbezüge»

<a id="seite-4-kapitalleistungen-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. Seite 4 Kapitalleistungen – Kapitalleistungen aus Vorsorge 2025 (Auszahlungsdatum, Quelle, Betrag)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung (Formular 563); Seite 4 unten der Steuererklärung
- **Regel:** Nicht in Ziff. 5.5, sondern Seite 4 unten: Quelle ankreuzen (AHV/IV, Säule 2, Freizügigkeit, Säule 3a, Kapital bei Tod/bleibenden Nachteilen). Separat zu 100% besteuert zum einheitlichen Satz der einfachen Steuer: 2.0% gemeinsam besteuerte, 2.4% Alleinstehende (mal Steuerfuss). Mehrere Leistungen: Aufstellung einreichen. Genugtuung bleibt steuerfrei.
- **Bund:** Bund: 1/5 des ordentlichen Tarifs (Tarif Alleinstehende bzw. Verheiratete); kein Elterntarif.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0018.md) `tg-form-01-2025__c0018` – «Kapitalleistungen aus Vorsorge 2025»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0131.md) `tg-wl-2025__c0131` – «tung, bei gemeinsam besteuerten Personen zu einem einheitlichen Satz von 2% besteuert.»
  - [WL TG 2025 S. 28](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0131.md) `tg-wl-2025__c0131` – «Bei Alleinstehenden beträgt der einheitliche Satz für die einfache Steuer 2,4%.»

<a id="seite-4-selbstanzeige-verfahren-einreichung"></a>
### Ziff. Seite 4 Selbstanzeige – Antrag auf erstmalige straflose Selbstanzeige (Steuerperioden)

- **Schlüssel:** `verfahren.einreichung` (Einreichung, Unterschrift, Beilagen, Fristen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 4: Checkbox + Perioden; unterzeichneter Antrag mit Aufstellung der nicht versteuerten Werte
- **Regel:** Nur bei erstmaliger Selbstanzeige: Feld ankreuzen und Antrag mit Sachverhalt, umfassender Aufstellung der unversteuerten Einkommens-/Vermögenswerte und Belegen beilegen; Nachsteuer maximal 10 Jahre. Entscheid der Steuerverwaltung (Rechtsdienst) folgt separat.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0018.md) `tg-form-01-2025__c0018` – «Antrag auf erstmalige straflose Selbstanzeige»
  - [WL TG 2025 S. 29](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0135.md) `tg-wl-2025__c0135` – «Wollen Sie eine erstmalige straflose Selbstanzeige vornehmen, können Sie in der Steuererklärung»

<a id="seite-4-bemerkungen-unterschrift-verfahren-einreichung"></a>
### Ziff. Seite 4 Bemerkungen/Unterschrift – Bemerkungen, Unterschrift, Einreichung und Fristen

- **Schlüssel:** `verfahren.einreichung` (Einreichung, Unterschrift, Beilagen, Fristen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Formular 1 Seite 4 Bemerkungszeilen/Unterschrift; Einreichungsdatum auf dem Formular; Quittung bei eFisc-Übermittlung
- **Regel:** Unterschrift beider Personen (auch bei Vollmacht). Einreichung beim Gemeindesteueramt bis zum aufgedruckten Datum; bei elektronischer Übermittlung gilt die Erklärung erst mit der unterzeichneten Quittung (zusammen mit dem Original-Hauptformular) als eingereicht. Immer beizulegen: sämtliche Lohnausweise, Steuerauszüge, Rechnungen Liegenschaftsunterhalt und Zuwendungsbestätigungen ab Fr. 1'000, 3a-Bescheinigungen. Fristerstreckung: Gesuch an das Gemeindesteueramt; Private erstmals bis 30.9. (Folgegesuch begründet bis 30.11.); gewerbsmässige Treuhänder/Steuerberater für Mandanten bis 31.12. des Deklarationsjahres; Arbeitsüberlastung ist kein Grund.
- **Quellen:**
  - [Formular 1 TG 2025 S. 4](../../chunks/tg/2025/tg-form-01-2025/tg-form-01-2025__c0018.md) `tg-form-01-2025__c0018` – «Diese Steuererklärung ist vollständig und wahrheitsgetreu ausgefüllt»
  - [WL TG 2025 S. 10](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0036.md) `tg-wl-2025__c0036` – «Bei elektronischer Datenübermittlung gilt die Steuererklärung erst als einge»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0002.md) `tg-stp-155-2__c0002` – «gewerbsmässig Steuererklärungen ausfüllen, können»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0002.md) `tg-stp-155-2__c0002` – «längstens bis zum 31. Dezember des Deklarationsjahres»
  - [WL TG 2025 S. 10](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0036.md) `tg-wl-2025__c0036` – «– Bestätigungen von freiwilligen Zuwendungen ab einem Betrag von Fr. 1'000;»

## Hilfsblatt Berufskosten

<a id="form-4-2-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2 Ziff. 1.2 – Geschäftsfahrzeug zur Verfügung für die Fahrt zur Arbeitsstätte (ja/nein, von–bis)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld F (unentgeltliche Beförderung Wohn-/Arbeitsort) und Ziff. 2.2 (Privatanteil Geschäftsfahrzeug)
- **Regel:** Steht ein Geschäftsfahrzeug für den Arbeitsweg kostenlos zur Verfügung, ist kein Fahrkostenabzug möglich (Privatanteil 0.9% pro Monat im Lohn enthält den Arbeitsweg, daher keine Aufrechnung). Lohnausweis Feld F angekreuzt = keine Fahrkosten (Ziff. 2.1–2.5) geltend machen; gilt ebenso bei Sammeltransport oder vergüteten effektiven Autokilometern von Aussendienstmitarbeitern; Vergütungen des Arbeitswegs in Lohnausweis Ziff. 2.3 sind kein Feld-F-Fall. Zeitraum von–bis angeben, falls nur zeitweise.
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0001.md) `tg-form-04-2-2025__c0001` – «1.2 Steht Ihnen für die Fahrt zur Arbeitsstätte»
  - [WL TG 2025 S. 37](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0176.md) `tg-wl-2025__c0176` – «Da der geldwerte Vorteil für den Arbeitsweg somit be»
  - [WL Lohnausweis 2026 S. 10–11](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0022.md) `bund-wl-lohnausweis-2026__c0022` – «In allen Fällen ist im Lohnausweis grundsätzlich das Feld F (unentgeltliche Beförderung zwi»

<a id="form-4-2-ziff-2-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2 Ziff. 2.1 – Abonnementskosten öffentliche Verkehrsmittel (Code 206; Person 2: 246)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg → ÖV-Abonnement/Beleg über tatsächliche Kosten
- **Regel:** Tatsächlich entstandene, nachgewiesene Abonnementskosten (Staat und Bund gleich). Nur wenn Feld F im Lohnausweis nicht angekreuzt ist; vom Arbeitgeber vergütete Kosten (Lohnausweis Ziff. 2.3) nicht abziehbar. Beachtenswerte Entfernung ab ca. 1 km. Fahrkostenbeschränkung gilt für alle Fahrkosten zusammen (inkl. Wochenaufenthalt).
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 pro Jahr (alle Fahrkosten inkl. Wochenaufenthalt und Nebenerwerb zusammen; keine Kürzung bei unterjähriger Steuerpflicht/Teilzeit).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0002.md) `tg-form-04-2-2025__c0002` – «2.1 Abonnementskosten für öffentliche Verkehrsmittel   206»
  - [WL TG 2025 S. 37–38](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0177.md) `tg-wl-2025__c0177` – «Bei Benützung öffentlicher Verkehrsmittel (Bahn, Tram, Autobus) können Sie die tatsächlich ent»

<a id="form-4-2-ziff-2-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2 Ziff. 2.2 – Fahrrad, Motorfahrrad, Kleinmotorrad bis 50 cm3, pauschal (Code 210; Person 2: 250)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Belege nötig (Pauschale)
- **Regel:** Pauschal bis Fr. 700 pro Jahr (Fahrrad, Motorfahrrad, Kleinmotorrad bis 45 km/h mit gelbem Kontrollschild).
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Fahrrad, Motorfahrrad/Kleinmotorrad (bis 45 km/h, gelbes Kontrollschild): bis CHF 700 pro Jahr.)** · Bund **CHF 700 (Pauschale pro Jahr für Fahrrad, Motorfahrrad und Motorrad mit gelbem Kontrollschild; tatsächliche Kosten zusätzlich nicht abziehbar)**
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0002.md) `tg-form-04-2-2025__c0002` – «2.2 Fahrrad, Kleinmotorrad bis 50 cm3 pauschal Fr. 700.–   210»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0002.md) `tg-stp-29-2__c0002` – «können im Jahr bis zu **Fr. 700** abgezogen werden»

<a id="form-4-2-ziff-2-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2 Ziff. 2.3 – Kosten für privates Motorfahrzeug (Auto / Motorrad über 50 cm3), km pro Tag × Anzahl Tage (Code 211; Person 2: 251; Staat und Bund getrennt)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Distanz Wohnadresse–Standort Fahrzeug am Arbeitsort/P+Rail; Jahreskilometer
- **Regel:** Nur in begründeten Ausnahmefällen (ÖV unzumutbar, z.B. Zeitersparnis über 1 Stunde pro Arbeitstag), sonst nur Kosten des ÖV-Abonnements. Kanton Auto gestaffelt: bis 3'000 km Fr. 0.60, 3'001–5'000 km Fr. 0.50, über 5'000 km Fr. 0.40 (inkl. Parkgebühren); Motorrad ab 45 km/h Fr. 0.40. Bund Auto einheitlich Fr. 0.70/km. In der Regel max. 225 Arbeitstage bei 100%-Pensum. Kanton und Bund separat berechnen, da unterschiedliche Spalten. Heimkehr am Mittag: Fahrkosten höchstens bis Höhe des Verpflegungsabzugs und dann kein zusätzlicher Verpflegungsabzug.
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

<a id="form-4-2-ziff-2-4-berechnung-total"></a>
### Ziff. Form. 4.2 Ziff. 2.4 – Total effektive Fahrkosten (Ziffern 2.1–2.3) (Code 212; Person 2: 252)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Summe 2.1 bis 2.3 (inkl. Fahrkosten Wochenaufenthalt gemäss Ziff. 5), separat je Spalte Staat/Bund.
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0002.md) `tg-form-04-2-2025__c0002` – «2.4 Total effektive Fahrkosten (Ziffern 2.1 – 2.3)   212»

<a id="form-4-2-ziff-2-5-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2 Ziff. 2.5 – Total abzugsfähige Fahrkosten, Staat max. Fr. 6'000 / Bund max. Fr. 3'300 (Code 213; Person 2: 253)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 2.4 begrenzt auf Maximum)
- **Regel:** Staat: min(Ziff. 2.4; Fr. 6'000), Bund: min(Ziff. 2.4; Fr. 3'300). Maximum wird bei unterjähriger Steuerpflicht/Erwerbsdauer oder Teilzeit nicht gekürzt. Beispiel WL: 12'150 km → Kanton Fr. 5'660, Bund effektiv Fr. 8'505 → Fr. 3'300.
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 pro Jahr (alle Fahrkosten inkl. Wochenaufenthalt und Nebenerwerb zusammen; keine Kürzung bei unterjähriger Steuerpflicht/Teilzeit).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Bund:** Bund max. Fr. 3'300 (Kanton Fr. 6'000).
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0002.md) `tg-form-04-2-2025__c0002` – «Total abzugsfähige Fahrkosten (Übertrag von Ziffer 2.4, aber Staat max. Fr. 6000.– / Bund max. Fr. 3300.–)   213»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0006.md) `tg-stp-29-2__c0006` – «Bei der direkten Bundessteuer beträgt der Maximalabzug:»
  - [StG TG § 29](../../chunks/tg/2025/tg-stg/tg-stg__par-29.md) `tg-stg__par-29` – «bis zu einem Maximalbetrag von Fr. 6'000»

<a id="form-4-2-ziff-3-1-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4.2 Ziff. 3.1 – Mehrkosten auswärtige Verpflegung ohne Verbilligung oder bei Schicht-/Nachtarbeit, Fr. 15 pro Tag, max. Fr. 3'200 (Code 214; Person 2: 254)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis (Feld G nicht angekreuzt; Ziff. 15 Anzahl Schichttage; Spesenreglement/Ziff. 13.2); Arbeitgeberbescheinigung Schichttage
- **Regel:** Fr. 15 pro auswärtige Hauptmahlzeit (i.d.R. Mittagessen), bei ständiger Verpflegung max. Fr. 3'200/Jahr, bei Teilzeit/Nebenberuf und unterjährig entsprechend gekürzt. Voraussetzung: Heimkehr am Mittag unzumutbar (grosse Entfernung oder sehr kurze Pause). Schicht-/Nachtarbeit: gleicher Abzug pro ausgewiesenem Tag mit mind. 8 Stunden durchgehender Schicht-/Nachtarbeit; Anzahl Schichttage in das Feld eintragen und belegen (Lohnausweis Ziff. 15 oder Arbeitgeberbescheinigung). Kein Abzug, wenn Mahlzeit unter Fr. 10 zu stehen kommt oder wenn Fahrkosten für Heimkehr am Mittag geltend gemacht werden. Lohnausweis Feld G angekreuzt → Ziff. 3.2 statt 3.1. Nicht kumulierbar mit Wochenaufenthalt (Ziff. 5.2) für denselben Zeitraum.
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

<a id="form-4-2-ziff-3-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4.2 Ziff. 3.2 – Mehrkosten auswärtige Verpflegung mit Verbilligung durch Arbeitgeber/Kantine, Fr. 7.50 pro Tag, max. Fr. 1'600 (Code 216; Person 2: 256)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten)
- **Regel:** Wenn der Arbeitgeber Mahlzeiten verbilligt (Barbeiträge, Gutscheine/Lunch-Checks) oder eine Kantine/Personalrestaurant zur Verfügung steht und trotzdem Mehrkosten entstehen: nur halber Abzug, Fr. 7.50/Tag, max. Fr. 1'600/Jahr. Lohnausweis Feld G angekreuzt ist das Signal (auch wenn nicht bekannt ist, ob die Kantine genutzt wird). Trägt der Arbeitgeber die Kosten des Mittagessens vollständig (z.B. Vermerk «Mittagessen durch Arbeitgeber bezahlt» in Lohnausweis Ziff. 15), entstehen keine Mehrkosten – kein Verpflegungsabzug (Folgerung aus WL: kein Abzug für vom Arbeitgeber übernommene Kosten). Teilzeit/Nebenberuf: angemessen kürzen.
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Halber Abzug (CHF 7.50 pro Tag), wenn Hauptmahlzeiten vom Arbeitgeber verbilligt (Gutscheine/Beiträge) oder Kantine/Personalrestaurant zur Verfügung steht. Kein Abzug, wenn Mahlzeit unter CHF 10 kostet.)** · Bund **CHF 7.50 (Halber Abzug CHF 7.50 pro Hauptmahlzeit, wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Halber Abzug bei verbilligter Verpflegung: maximal CHF 1'600 pro Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: CHF 1'600 pro Jahr)**
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft.
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0003.md) `tg-form-04-2-2025__c0003` – «3.2 mit Verbilligung durch Arbeitgeber/in oder Kantine,»
  - [WL TG 2025 S. 39–40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0185.md) `tg-wl-2025__c0185` – «Nur der halbe Abzug (Fr. 7.50 im Tag, Fr. 1'600 im Jahr) ist zulässig, wenn Hauptmahlzeiten von»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten   Buchstabe G»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Dieses Feld ist auch anzukreuzen bei Arbeitnehmern, die 40 % - 60 % der Arbeitszeit aus»

<a id="form-4-2-ziff-4-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4.2 Ziff. 4 – Übrige für die Ausübung des Berufes erforderliche Kosten: 3% vom Nettolohn, min. Fr. 2'000, max. Fr. 4'000, oder effektiv (Code 220; Person 2: 260)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 Nettolohn (Basis Pauschale); bei effektiven Kosten separate Aufstellung mit Belegen
- **Regel:** Pauschale 3% des Nettolohns (Lohnausweis Ziff. 11), mindestens Fr. 2'000, höchstens Fr. 4'000 (Kanton und Bund); bei unterjähriger Erwerbstätigkeit anteilmässig gekürzt. Alternativ nachgewiesene effektive Kosten gemäss Aufstellung – nicht kumulierbar mit der Pauschale. Deckt Berufswerkzeug, Fachliteratur, Kleider/Schuhverschleiss, Schwerarbeit, Berufsverbands-/Gewerkschaftsbeiträge. Erhaltene Spesenvergütungen mindern effektive Kosten.
- **Limiten:**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **3 % (Pauschale übrige Berufskosten: 3% des Nettolohnes (Alternative: Nachweis höherer tatsächlicher Kosten, keine Kumulation).)** · Bund **3 % (Übrige Berufskosten: 3 % des Nettolohns (Pauschale; Nachweis höherer Kosten möglich); bei Teilzeit/unterjährig angemessen kürzen)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **CHF 2'000 (Pauschale übrige Berufskosten: Minimum CHF 2'000.)** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 4'000 (Pauschale übrige Berufskosten: Maximum CHF 4'000.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
- **Bund:** Gleiche Pauschale beim Bund (3%, Fr. 2'000–4'000).
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0004.md) `tg-form-04-2-2025__c0004` – «3% vom Nettolohn, mindestens jedoch Fr. 2000.– und höchstens Fr. 4000.–»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0187.md) `tg-wl-2025__c0187` – «Pauschalabzug von 3% vom Nettolohn gemäss Ziffer 11 des Lohnausweises»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0187.md) `tg-wl-2025__c0187` – «Anstelle der Pauschale können Sie die notwendigen tatsächlichen Aufwendungen nachweisen.»

<a id="form-4-2-ziff-5-1-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4.2 Ziff. 5.1 – Wochenaufenthalt: Unterkunft, ortsübliche Auslagen für ein Zimmer (Code 226; Person 2: 266)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Mietvertrag/Mietzinsbeleg auswärtige Unterkunft
- **Regel:** Nur ein Zimmer (keine Wohnung) gilt als notwendig; bei kleiner Wohnung bis 3½ Zimmer Jahresmietzins : (Zimmerzahl + 1). Voraussetzung: regelmässige Heimkehr am Wochenende an den steuerlichen Wohnsitz. Fahrkosten der Heimkehr gehören unter Ziff. 2.1–2.3 (mit Fahrkostenbeschränkung).
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Wochenaufenthalt: ortsübliche Auslagen für ein Zimmer (keine Wohnung); bei kleiner Wohnung bis 3.5 Zimmer: Jahresmietzins : (Anzahl Zimmer + 1). Kein Abzug bei Naturallohn. Zusätzlich notwendige Fahrkosten der wöchentlichen Heimkehr (unter Fahrkostenbeschränkung).** · Bund **Mehrkosten Unterkunft: ortsübliche Auslagen für ein Zimmer (nicht eine Wohnung) abziehbar; Fahrkosten der regelmässigen Heimkehr bis zum Maximalbetrag nach Art. 5 Abs. 1 BKV**
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0004.md) `tg-form-04-2-2025__c0004` – «5.1 Unterkunft ortsübliche Auslagen für ein Zimmer   226»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0189.md) `tg-wl-2025__c0189` – «wendigen Mehrkosten der Unterkunft können Sie daher nur die ortsüblichen Auslagen für ein»

<a id="form-4-2-ziff-5-2-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4.2 Ziff. 5.2 – Wochenaufenthalt: Verpflegung, Fr. 30 pro Arbeitstag / max. Fr. 6'400, mit Verbilligung Fr. 22.50 / max. Fr. 4'800 (Code 230; Person 2: 270)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis (Feld G bei verbilligtem Mittagessen)
- **Regel:** Fr. 15 pro Hauptmahlzeit = Fr. 30/Tag, ganzjährig max. Fr. 6'400; bei Verbilligung des Mittagessens durch den Arbeitgeber (Feld G) nur halber Abzug für diese Mahlzeit = Fr. 22.50/Tag bzw. Fr. 4'800/Jahr. Nicht kumulierbar mit Ziff. 3 für denselben Zeitraum.
- **Limiten:**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 6'400 (Wochenaufenthalt Verpflegung: CHF 15 pro Hauptmahlzeit, CHF 30 pro Tag, bei ganzjährigem Wochenaufenthalt CHF 6'400 pro Jahr; bei Verbilligung Mittagessen CHF 22.50/Tag bzw. CHF 4'800/Jahr.)** · Bund **CHF 6'400 (Auswärtiger Wochenaufenthalt: Verpflegung CHF 30 pro Tag, max. CHF 6'400 pro Jahr; bei Verbilligung CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr; Nachweis höherer Kosten ausgeschlossen)**
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0004.md) `tg-form-04-2-2025__c0004` – «bei Verbilligung pro Arbeitstag Fr. 22.50 / im Jahr Fr. 4800.–»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0190.md) `tg-wl-2025__c0190` – «benden) und trotzdem Mehrkosten entstehen, wird für diese Mahlzeit nur der halbe Abzug (Fr. 7.50)»

<a id="form-4-2-ziff-6-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 4.2 Ziff. 6 – Auslagen bei Nebenbeschäftigung: 20% vom Nettolohn, min. Fr. 800, max. Fr. 2'400, oder effektiv (Code 232; Person 2: 272)

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 des Nebenerwerbs; bei effektiven Kosten Aufstellung
- **Regel:** Pauschal 20% der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400 (Kanton und Bund), höchstens bis zur Höhe des Nebenerwerbseinkommens; deckt Fahrt-, Verpflegungs- und übrige Berufskosten (keine Kumulation mit effektiven Kosten). Behördenmitglieder (Exekutive Gemeinde/Schul-/Kirchgemeinde, volksgewählt, nebenamtlich): 50% der Entschädigungen, min. Fr. 2'000, max. Fr. 4'000. Haupterwerb kann auch mehrere Teilzeitanstellungen umfassen.
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Nebenerwerb: Pauschale 20% der Nettoeinkünfte (statt effektiver Kosten, keine Kumulation); gilt auch beim Bund.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge))**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerbspauschale: Minimum CHF 800.)** · Bund **CHF 800 (Minimum Pauschale Nebenerwerb)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerbspauschale: Maximum CHF 2'400 (Nachweis höherer Kosten vorbehalten; maximal bis Höhe des Nebenerwerbseinkommens).)** · Bund **CHF 2'400 (Maximum Pauschale Nebenerwerb)**
- **Bund:** Gleiche Pauschale beim Bund.
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0005.md) `tg-form-04-2-2025__c0005` – «20% vom Nettolohn, mindestens Fr. 800.– und höchstens Fr. 2400.–»
  - [WL TG 2025 S. 40](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0191.md) `tg-wl-2025__c0191` – «werden. Der Abzug beträgt 20% der Nettoeinkünfte, mindestens aber Fr. 800 und höchstens»
  - [WL TG 2025 S. 41](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0194.md) `tg-wl-2025__c0194` – «Der Pauschalabzug beträgt 50% von den insgesamt ausgerichteten Behördenentschädigungen»

<a id="form-4-2-ziff-7-berechnung-total"></a>
### Ziff. Form. 4.2 Ziff. 7 – Total der abzugsfähigen Berufsauslagen (Code 240; Person 2: 280) → Steuererklärung Ziff. 10.1 / 10.2

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Summe Ziff. 2.5 bis 6; Übertrag in Ziff. 10.1 (Person 1) bzw. 10.2 (Person 2), Spalten Staat/Bund getrennt.
- **Quellen:**
  - [Formular 4.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0005.md) `tg-form-04-2-2025__c0005` – «7.   Total der abzugsfähigen Berufsauslagen   240»

## Hilfsblatt Versicherungsprämien

<a id="form-5-2-a-1-a-4-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 A.1–A.4 – Selbst getragene Prämien: private Krankenversicherung (netto nach Prämienverbilligung), private Unfallversicherung, Lebens-/Rentenversicherungen, erhaltene Sparzinsen

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Police Hausrat-/Privathaftpflichtversicherung (inkl. Gebäudeversicherung des Mieters/Mobiliar), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Jahresbestätigung Krankenkasse (Prämie abzüglich IPV), Prämienrechnungen Unfall/Leben/Rente, Zinsausweise Banken (Formular 2)
- **Regel:** Ziff. 1: Nettoprämie = Krankenkassenprämie abzüglich in der Steuerperiode erhaltener Prämienverbilligungen (inkl. EL-Prämienverbilligung und Nachzahlungen früherer Jahre); Deklaration der KK-Prämien ist Voraussetzung des Abzugs. Ziff. 2: private Unfallversicherung (ohne NBUV → Ziff. 15.4). Ziff. 3: private Lebens-/Rentenversicherungen. Ziff. 4: im Jahr 2025 erhaltene Zinsen von Sparkapitalien (Bank/Post, Obligationen, Hypothekar-/Darlehensguthaben, gemäss Formular 2).
- **Quellen:**
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0001.md) `tg-form-05-2-2025__c0001` – «1. private Krankenversicherung (netto, nach Abzug Prämienverbilligung gemäss Bestätigung Versicherung)»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0210.md) `tg-wl-2025__c0210` – «Tragen Sie in Ziffer 1 die selber bezahlten Einlagen, Prämien und Beiträge für die private Kran»

<a id="form-5-2-a-5-a-6-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 A.5–A.6 – Krankentaggeldversicherung gemäss Lohnausweis; Total selbst getragene Versicherungsprämien und Sparzinsen (Code 324, Feld «A5»)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 (Hinweis Krankentaggeld-Beiträge)
- **Regel:** Zusätzlich die dem Arbeitnehmer belasteten Krankentaggeld-Beiträge gemäss Lohnausweis eintragen (Lohnausweis weist sie ggf. in Ziff. 15 aus). Total ergibt «A5»/Code 324. Hinweis: Das Formular 2025 hat Zeilen 1–6 (Total in Zeile 6), die Wegleitung beschreibt noch das alte Schema 1–5/'A7'.
- **Bemerkung:** Lohnausweis-Regeln (Feld F/G, Ziff. 10.2, 13.3, 15) stammen aus der ESTV-Wegleitung zum Lohnausweis, gültig ab 01.01.2026 (bund-wl-lohnausweis-2026, jahr_ok); eine Fassung für 2025 liegt im Wiki nicht vor, der Lohnausweis ist ein ESTV-Formular und in diesen Punkten für TG 2025 inhaltlich massgebend, aber Fassung 2026 – Fachperson prüft. Zusätzlich: Zeilennummerierung Formular 5.2 (2025) vs. Wegleitung abweichend.
- **Quellen:**
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0001.md) `tg-form-05-2-2025__c0001` – «5. Krankentaggeldversicherung gemäss Lohnausweis»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0001.md) `tg-form-05-2-2025__c0001` – «6. Total selbst getragene Versicherungsprämien und Sparzinsen   324»
  - [WL Lohnausweis 2026 S. 14](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0034.md) `bund-wl-lohnausweis-2026__c0034` – «Arbeitnehmern belastete Beiträge an Krankentaggeldversicherungen sowie Prä»

<a id="form-5-2-b-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 B – Maximaler Abzug für Versicherungsprämien und Sparzinsen (Code 328; Feld «B4» Staat/Bund)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Zivilstand, Anzahl Kinder/unterstützte Personen, Beiträge Säule 2/3a)
- **Regel:** Staat: Fr. 7'000 gemeinsam besteuert / Fr. 3'500 übrige; Bund: Fr. 3'700 / Fr. 1'800 oder ohne Beiträge Säule 2/3a Fr. 5'550 / Fr. 2'700 (nur Bund); pro Kind und unterstützungsbedürftige Person mit Kinder-/Unterstützungsabzug zusätzlich Fr. 1'000 (Staat) bzw. Fr. 700 (Bund). Zuteilung bei getrennt besteuerten Eltern wie Kinderabzug (Kanton) bzw. nach Sorgerecht/Alimenten (Bund).
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 7'000 (Versicherungsprämien und Sparzinsen, Verheiratete in ungetrennter Ehe: max. CHF 7'000 (inkl. eingetragene Partnerschaft).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 3'500 (Versicherungsprämien und Sparzinsen, übrige Steuerpflichtige: max. CHF 3'500.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag Versicherungsabzug: CHF 1'000 je minderjähriges oder in Ausbildung stehendes Kind bzw. unterstützte Person (mit Kinder-/Unterstützungsabzug).)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
- **Bund:** Bund: 3'700 / 1'800 / ohne 2./3a 5'550 / 2'700 / Kind 700.
- **Quellen:**
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0002.md) `tg-form-05-2-2025__c0002` – «1. für gemeinsam besteuerte Personen (Eheleute / Partnerinnen oder Partner)   7000   3700»
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0002.md) `tg-form-05-2-2025__c0002` – «3. für jedes Kind und für jede unterstützungsbedürftige Person, für die ein Kinder- oder»
  - [WL TG 2025 S. 44](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0212.md) `tg-wl-2025__c0212` – «übrige steuerpflichtige Personen   Fr. 3'500   Fr. 1'800»

<a id="form-5-2-c-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 C – Berechnung zulässiger Abzug: niedrigerer Betrag aus «A5» und «B4» (Code 330; Staat/Bund)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Staat: min(A5; B4 Staat), Bund: min(A5; B4 Bund); Übertrag in Ziff. 14.
- **Quellen:**
  - [Formular 5.2 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0003.md) `tg-form-05-2-2025__c0003` – «2. Bundessteuer: der niedrigere Betrag von «A5» oder «B4 Bund»   330»

## Hilfsblatt Krankheitskosten

<a id="form-5-1-a-abzug-krankheitskosten"></a>
### Ziff. Form. 5.1 A – Aufwendungen: Selbstbehalt/Franchise, Arzt, Zahnarzt, Pflegepersonal, Spital/Heim, Therapien/Kur, Prothesen; getrennt Krankheits-/Unfallkosten und behinderungsbedingte Kosten

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Rechnungen und Kostenzusammenstellung der Krankenkasse (Selbstbehalt/Franchise); ärztliche Verordnung für Therapien/Kuren
- **Regel:** Nur selbst getragene Kosten; Belege geordnet beilegen. Ärztlich verordnete Therapien/Kuren: Kopie der Verordnung beilegen. Zahnarztkosten, Brillen, Apparate, Kuren abziehbar; nicht: Krankenkassenprämien, Fahrkosten zum Arzt (ausser dauernde Pflegebedürftigkeit), nicht verordnete Akupunktur, Prävention, Schönheit/Fitness, unentgeltliche Pflege durch Dritte. Kosten für Behinderung in die zweite Spalte.
- **Quellen:**
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0001.md) `tg-form-05-1-2025__c0001` – «1. Selbstbehalt / Franchise gemäss detaillierter Kostenzusammenstellung der Krankenkasse»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0205.md) `tg-wl-2025__c0205` – «Tragen Sie auf der Vorderseite von Formular 5 unter A die Aufwendungen, aufgeteilt in „Krankheits»

<a id="form-5-1-b-abzug-krankheitskosten"></a>
### Ziff. Form. 5.1 B – Vergütungen Dritter und Anteil Lebenshaltungskosten (Krankenkasse, Versicherungen, Hilflosenentschädigung, Lebenshaltungskosten)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Leistungsabrechnungen Krankenkasse/Versicherung; Bescheide IV/AHV/SUVA (Hilfsmittel, Hilflosenentschädigung)
- **Regel:** Von den Aufwendungen abziehen: Krankenkassen-/Versicherungsleistungen (inkl. Pflegefinanzierung), Hilflosenentschädigung AHV/IV/SUVA, Beiträge an Hilfsmittel und ein Anteil Lebenshaltungskosten (z.B. Ernährung/Unterkunft bei Kur oder Heim).
- **Quellen:**
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0002.md) `tg-form-05-1-2025__c0002` – «3. Hilflosenentschädigung AHV/IV/SUVA»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0203.md) `tg-wl-2025__c0203` – «Die von Krankenkassen, Versicherungen oder Dritten vergüteten Kosten, Beiträge der AHV, IV, MV»

<a id="form-5-1-c-abzug-behinderungskosten"></a>
### Ziff. Form. 5.1 C – Berechnung behinderungsbedingte Kosten (A–B) (Code 350) → Ziff. 17

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Total Aufwendungen behinderungsbedingte Kosten (A) minus Vergütungen (B); Übertrag Ziff. 17. Alternativ Pauschalen (Fr. 2'500/5'000/7'500).
- **Quellen:**
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0003.md) `tg-form-05-1-2025__c0003` – «Abzugsfähige behinderungsbedingte Kosten   350»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0205.md) `tg-wl-2025__c0205` – «vom Total A das Total B ab. Die so ermittelten abzugsfähigen behinderungsbedingten Kosten über»

<a id="form-5-1-d-abzug-krankheitskosten"></a>
### Ziff. Form. 5.1 D – Berechnung Krankheits- und Unfallkosten: (A–B) abzüglich 5% Selbstbehalt von Ziff. 22 (Code 364; Staat/Bund) → Ziff. 23.1

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Nettoeinkommen Ziff. 22 je Spalte)
- **Regel:** Total Aufwendungen minus Vergütungen minus 5% des Nettoeinkommens Ziff. 22 – Staat mit linker, Bund mit rechter Spalte von Ziff. 22 (Beispiel WL: Netto 40'000 → 2'000; Bund 44'000 → 2'200).
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5% des Nettoeinkommens (Ziff. 22 der Steuererklärung).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Quellen:**
  - [Formular 5.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-05-1-2025/tg-form-05-1-2025__c0004.md) `tg-form-05-1-2025__c0004` – «Abzugsfähige Krankheits- und Unfallkosten   364»
  - [WL TG 2025 S. 43](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0206.md) `tg-wl-2025__c0206` – «dasjenige für die direkte Bundessteuer aus der rechten Spalte.»

## Hilfsblatt Schulden

<a id="form-4-1-a-schulden-privat"></a>
### Ziff. Form. 4.1 A – Privatschulden: Gläubiger/in mit Adresse, Zinssatz, Schuld am 31.12.2025, fällige Schuldzinsen (Codes 455 / 286)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Kreditkartenabrechnung (Monats-/Jahresabrechnung, Karten-Jahresgebühr) → Bank-/Gläubigerbestätigung per 31.12.2025 (Schuld, Zinssatz, im Jahr fällig gewordene Zinsen)
- **Regel:** Gläubiger mit genauer Adresse und Zinssatz sind unerlässlich. Nur 2025 fällig gewordene Zinsen (keine Ratazinsen); Amortisationen, Bau-/Landkreditzinsen und Leasingzinsen sind keine abziehbaren Schuldzinsen. WEF-Zusatzverbilligung als Zinsminderung. Totale: Schulden Code 455, Zinsen Code 286.
- **Quellen:**
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0001.md) `tg-form-04-1-2025__c0001` – «Total Privatschulden   455   286»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0171.md) `tg-wl-2025__c0171` – «Unerlässlich ist insbesondere die Angabe der Gläubigerin bzw. des Gläubigers»

<a id="form-4-1-b-schulden-privat"></a>
### Ziff. Form. 4.1 B – Geschäftsschulden und zugehörige Schuldzinsen (Codes 460 / 288)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz / Schuldenaufstellung Geschäft
- **Regel:** Geschäftsschuldzinsen hier nur, wenn nicht bereits im Einkommen Ziff. 2 abgezogen. Totale: Schulden Code 460, Zinsen Code 288.
- **Quellen:**
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0001.md) `tg-form-04-1-2025__c0001` – «Total Geschäftsschulden   460   288»
  - [WL TG 2025 S. 36](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0173.md) `tg-wl-2025__c0173` – «Tragen Sie Schuldzinsen aus selbständiger Erwerbstätigkeit hier nur ein, sofern Sie diese nicht»

<a id="form-4-1-c-schulden-privat"></a>
### Ziff. Form. 4.1 C – Zusammenzug Privat- und Geschäftsschulden (Code 466) und Schuldzinsen (Code 290)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Total Schulden (Code 466) → Steuererklärung Ziff. 34 (Seite 4); Total Schuldzinsen (Code 290) → Ziff. 11 (Seite 3).
- **Quellen:**
  - [Formular 4.1 TG 2025 S. 1](../../chunks/tg/2025/tg-form-04-1-2025/tg-form-04-1-2025__c0002.md) `tg-form-04-1-2025__c0002` – «Total Privat- und Geschäftsschulden   466   290»

## Hilfsblatt Wertschriftenverzeichnis

<a id="form-2-spalten-7-9-einkommen-wertschriften"></a>
### Ziff. Form. 2 Spalten 7–9 – Detailverzeichnis Wertschriften und Guthaben: Steuerwert 31.12. (Spalte 7), Bruttoertrag mit Verrechnungssteuerabzug (Spalte 8, A), ohne (Spalte 9, B)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Steuerauszug/Depotverzeichnis der Bank; Zins- und Kapitalbescheinigungen (Bruttozins, Verrechnungssteuer, Kontostand 31.12.); E-Steuerauszug
- **Regel:** Je Titel/Konto: Bezeichnung mit Valoren-/ISIN-Nr., Steuerwert per 31.12.2025 (Spalte 7), Bruttoertrag. Spalte 8 (A): Erträge MIT Verrechnungssteuerabzug (CH-Dividenden/Zinsen, Bankkonti über Fr. 200 Bruttozins oder mehrere Gutschriften, Lotterietreffer über Fr. 1'000 usw.; Franken und Rappen). Spalte 9 (B): Erträge OHNE Verrechnungssteuer (Konti ≤ Fr. 200, ausländische Wertschriften, Darlehen/Hypotheken). Codes für Geschäftsvermögen (02), Nutzniessung (01), qualifizierte Beteiligung (05/06), Erbschaft/Schenkung (03/04). Ausländische Erträge: netto + anrechenbare Quellensteuer; DA-1 für Anrechnung/USA-Rückbehalt. Zugang/Abgang mit Datum. Kinder unter elterlicher Sorge (Jahrgang 2008 und jünger) mitdeklarieren.
- **Quellen:**
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0005.md) `tg-form-02-2025__c0005` – «Detailverzeichnis Wertschriften und Guthaben»
  - [WL TG 2025 S. 32](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0153.md) `tg-wl-2025__c0153` – «In der Spalte 9 „Erträge ohne Verrechnungssteuerabzug“ aufzuführen sind auch Erträge inländi»
  - [WL TG 2025 S. 32](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0153.md) `tg-wl-2025__c0153` – «Bank- und Postkonti aller Art, deren Bruttozins im Kalenderjahr Fr. 200 nicht übersteigt und»

<a id="form-2-ziff-10-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 2 Ziff. 10 – Verrechnungssteueranspruch: 35% von Bruttoertrag Total A (Rückerstattungsantrag)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2 Ziff. 10; Unterschrift Rückerstattungsantrag; Auszahlungskonto Formular 1 Seite 1
- **Regel:** 35% des Totals der Erträge Spalte 8 (Zwischentotal I). Rückerstattung nur bei Wohnsitz im Kanton TG am 31.12.2025 und vollständiger Deklaration der Erträge; unter Vorbehalt des Rückforderungsrechts der ESTV. Erträge unverteilter Erbschaften nach Erbquote in Spalte A (mit VSt) bzw. B. Wertschriftenverzeichnis zu unterzeichnen.
- **Quellen:**
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0006.md) `tg-form-02-2025__c0006` – «10. Verrechnungssteueranspruch: 35% von Bruttoertrag Total A»
  - [WL TG 2025 S. 35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0167.md) `tg-wl-2025__c0167` – «Vom Total I der Bruttoerträge 2025»

<a id="form-2-verm-gensverwaltungskosten-code-148-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. Form. 2 Vermögensverwaltungskosten (Code 148) – Vermögensverwaltungskosten (Code 148; im Formular als Ziffer 17 bzw. Wegleitung Ziffer 7)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.) → Depotgebührenausweis der Bank; bei Nachweis höherer Kosten Belege
- **Regel:** Pauschal 2 Promille des Steuerwerts der durch Dritte verwalteten Wertschriften des Privatvermögens, max. Fr. 6'000; Darlehen, Bankguthaben und nicht kotierte qualifizierte Beteiligungen zählen nicht zur Bemessung. Nachweis höherer Kosten vorbehalten. Nur Depotgebühren/Verwaltung – nicht Kontoführung, Anlageberatung, Kommissionen/Spesen An-/Verkauf, Tresormiete.
- **Bemerkung:** Zifferbezeichnung im Formular 2 (2025) in der PDF-Extraktion unklar ('17.'); Wegleitung nennt 'Ziffer 7' – Code 148 ist massgebend.
- **Quellen:**
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0006.md) `tg-form-02-2025__c0006` – «17. Vermögensverwaltungskosten   Code 148»
  - [WL TG 2025 S. 33–34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0159.md) `tg-wl-2025__c0159` – «Der Pauschalabzug beträgt maximal Fr. 6'000.»

<a id="form-2-einsatzkosten-geldspiele-code-145-einkommen-wertschriften"></a>
### Ziff. Form. 2 Einsatzkosten Geldspiele (Code 145) – Einsatzkosten für steuerbare Gewinne aus Geldspielen (Code 145; im Formular Ziffer 18 bzw. Wegleitung Ziffer 8/9)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Gewinnbescheinigung / Auszahlungsbelege
- **Regel:** Pauschal 5% pro steuerbarem Gewinn, max. Fr. 5'000 je Gewinn (Staat; Bund Fr. 5'400 – Korrektur von Amtes wegen); effektive Einsatzkosten nicht möglich. Online-Spielbank: abgebuchte Spieleinsätze, max. Fr. 25'000 (Bund Fr. 26'800). In der Steuererklärung Staatsmaximum deklarieren. Einsatzkosten für nicht steuerbare Gewinne nicht abziehbar.
- **Bund:** Bund: Pauschale max. Fr. 5'400 (Online-Spielbank Fr. 26'800); Kanton Fr. 5'000 / Fr. 25'000.
- **Bemerkung:** Ziffernbezeichnung im Formular 2 in der PDF-Extraktion unklar; Wegleitung nennt Ziffer 8 bzw. 9. Code 145 massgebend.
- **Quellen:**
  - [Formular 2 TG 2025 S. 2](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0006.md) `tg-form-02-2025__c0006` – «18. Einsatzkosten und Spieleinsätze für steuerbare Gewinne aus Geldspielen»
  - [WL TG 2025 S. 34](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0161.md) `tg-wl-2025__c0161` – «Formulars geltend machen. Von jedem einzelnen steuerbaren Gewinn können pauschal fünf Pro»

<a id="form-2-hilfsblatt-qualifizierte-beteiligungen-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. Form. 2 Hilfsblatt qualifizierte Beteiligungen – Hilfsblatt qualifizierte Beteiligungen im Privatvermögen: Name/Sitz, Beteiligungsquote (ab 10%), Beteiligungsertrag; Teilbesteuerungsabzug Staat 40% / Bund 30%

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Dividendenabrechnung/Bescheinigung; Nachweis Beteiligungsquote ≥ 10%
- **Regel:** Pro Gesellschaft Name/Sitz, Quote und im Jahr 2025 erzielten Beteiligungsertrag eintragen; Total Ziff. 2 × 40% (Staat) bzw. 30% (Bund) = Abzug Ziff. 3 → Steuererklärung Ziff. 15.6. Antrag jährlich nötig. Beteiligungen im Geschäftsvermögen: Formular 14.
- **Quellen:**
  - [Formular 2 TG 2025 S. 4](../../chunks/tg/2025/tg-form-02-2025/tg-form-02-2025__c0008.md) `tg-form-02-2025__c0008` – «Hilfsblatt qualifizierte Beteiligungen im Privatvermögen»
  - [WL TG 2025 S. 34–35](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0166.md) `tg-wl-2025__c0166` – «Der Antrag auf die Durchführung des Teilbesteuerungsverfahrens für Erträge aus Beteiligungen im»

## Hilfsblatt Liegenschaften

<a id="form-7-steuerwert-mietwert-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 7 Steuerwert / Mietwert – Angaben zur Liegenschaft: Steuerwert; Mietwert selbstgenutzt, Selbstnutzungsabzug, steuerbarer Eigenmietwert (Staatssteuer / Bundessteuer)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftensteuerrechnung (Januar des Folgejahres: Steuerwert, indexierter Mietwert) / Schätzungsverfügung
- **Regel:** Pro Liegenschaft: Gemeinde, Kanton, Art, Baujahr, Anteile, Amtsnummer, Steuerwert. Mietwert aus Selbstnutzung gemäss rechtskräftiger Schätzung, bereinigt mit dem Mietwertindex der Steuerperiode (aus Liegenschaftensteuerrechnung). Selbstnutzungsabzug nur am Wohnsitz dauernd selbstbewohnt: 40% Kanton / 20% Bund; kein Abzug bei Zweit-/Ferienwohnungen, landwirtschaftlich geschätzten oder unentgeltlich/unterpreislich an Nahestehende überlassenen Liegenschaften (100% steuerbar). Wohnsitz am Liegenschaftsort ausserkantonal: ausserkantonale Steuerwerte, Repartition durch Veranlagungsbehörde.
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **40 % (Selbstnutzungsabzug 40% vom Eigenmietwert für am Wohnsitz dauernd selbstbewohntes Wohneigentum (Bund 20%); nicht für Zweit-/Ferienwohnungen, landwirtschaftlich geschätzte Liegenschaften oder an Nahestehende überlassene Objekte.)** · Bund **n/a – Eigenmietwert wird nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt (Art. 21 Abs. 2 DBG); Abschaffung per 01.01.2029 beschlossen, 2025–2028 gilt bisheriges Recht. Der Eigenmietwert für die direkte Bundessteuer wird im kantonalen Veranlagungsverfahren festgesetzt; ein dort vorgesehener Abzug für die DBSt (z.B. TG 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Bund:** Selbstnutzungsabzug Bund 20% (Kanton 40%).
- **Quellen:**
  - [Formular 7 TG 2025 S. 1](../../chunks/tg/2025/tg-form-07-2025/tg-form-07-2025__c0002.md) `tg-form-07-2025__c0002` – «Mietwert selbstgenutzt»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0224.md) `tg-wl-2025__c0224` – «Bei selbstgenutzten Liegenschaften ist der per Ende Steuerperiode rechtskräftig eröffnete Miet»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0225.md) `tg-wl-2025__c0225` – «Für am Wohnsitz selbstgenutzte eigene Liegenschaften können Sie vom Mietwert aus Selbst»

<a id="form-7-mietertr-ge-einkommen-liegenschaften-mietertrag"></a>
### Ziff. Form. 7 Mieterträge – Miet- und Pachtzinsen sowie weitere Erträge, Bruttoertrag

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Mietverträge, Mietzinsabrechnung, Nebenkostenabrechnung; Einspeisevergütung Photovoltaik
- **Regel:** Sämtliche Miet-/Pachtzinseinnahmen, Naturalleistungen, Baurechtszinsen, Einspeisevergütungen PV (bei Eigenbedarfsanlagen steuerfrei, soweit die Vergütung den Strombezug nicht übersteigt), Mietzinsreduktion für Hauswarte. Nebenkostenzahlungen der Mieter nicht steuerbar, soweit sie die tatsächlichen Aufwendungen nicht übersteigen.
- **Quellen:**
  - [Formular 7 TG 2025 S. 1](../../chunks/tg/2025/tg-form-07-2025/tg-form-07-2025__c0002.md) `tg-form-07-2025__c0002` – «Miet- und Pachtzinsen»
  - [WL TG 2025 S. 47](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0222.md) `tg-wl-2025__c0222` – «Steuerbar sind sämtliche Miet- und Pachtzinseinnahmen, welche die steuerpflichtige Person aus»

<a id="form-7-unterhalt-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 7 Unterhalt – Unterhalts-/Betriebskosten: Pauschal oder Effektiv (Formular 8)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Rechnungen (Kopien ab Fr. 1'000 einreichen); Formular 8 je Liegenschaft; Merkblatt Liegenschaftsunterhalt
- **Regel:** Pro Steuerperiode und Liegenschaft Wahl zwischen Pauschale und effektiven Kosten. Pauschale: 10% für Gebäude bis 10 Jahre, 20% bei älteren Gebäuden (Alter am Ende der Steuerperiode), berechnet auf Mietertrag bzw. Mietwert/steuerbaren Eigenmietwert. Keine Pauschale bei Geschäftsvermögen, vorwiegend geschäftlich von Dritten genutzten, unüberbauten oder Baurechts-Grundstücken. Nicht kumulierbar mit übertragbaren Energie-/Rückbaukosten (dann alles effektiv).
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Unterhaltspauschale 10% des Bruttomietertrags/Mietwerts/Eigenmietwerts für Gebäude bis zehn Jahre alt (am Ende der Steuerperiode); Wahl pro Liegenschaft und Periode; nicht bei Geschäftsvermögen, unüberbauten Grundstücken, Baurecht.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Unterhaltspauschale 20% für Gebäude, die älter als zehn Jahre sind.)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Quellen:**
  - [Formular 7 TG 2025 S. 1](../../chunks/tg/2025/tg-form-07-2025/tg-form-07-2025__c0002.md) `tg-form-07-2025__c0002` – «Unterhalts-/Betriebskosten»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0238.md) `tg-wl-2025__c0238` – «Die Pauschale beträgt:»
  - [WL TG 2025 S. 50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0238.md) `tg-wl-2025__c0238` – «20% für Gebäude, die am Ende der Steuerperiode älter als zehn Jahre sind.»

<a id="form-7-totale-berechnung-total"></a>
### Ziff. Form. 7 Totale – Totale Steuerwerte (Code 430) und Nettoerfolge (Code 180) Staat/Bund

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Regel:** Total Steuerwerte → Steuererklärung Ziff. 31 (Seite 4); Total Nettoerfolge → Ziff. 8 (Seite 2), Spalten Staat und Bund getrennt.
- **Quellen:**
  - [Formular 7 TG 2025 S. 1](../../chunks/tg/2025/tg-form-07-2025/tg-form-07-2025__c0003.md) `tg-form-07-2025__c0003` – «Total Steuerwerte   430   Total Nettoerfolge   180»

<a id="form-8-abzug-liegenschaft-energie-umwelt"></a>
### Ziff. Form. 8 – Angaben zu Unterhalts- und Betriebskosten (je Liegenschaft): Rechnungsdatum, Rechnungsteller, Arbeit, Zahlungsbetrag, Anlagekosten/Mehrwert, abzugsfähige Kosten; Energiespar-/Umweltschutz-/Rückbaukosten; übertragbare Kosten

- **Schlüssel:** `abzug.liegenschaft.energie_umwelt` (Investitionen Energiesparen/Umweltschutz, Rückbaukosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Rechnungen mit Detailangaben; Hilfsblatt übertragbare Kosten (StP 34 Nr. 2); bei Stockwerkeigentum Abrechnung der Gemeinschaft
- **Regel:** Pro Liegenschaft ein Formular 8; Einzelbeträge ab Fr. 1'000 mit Rechnungskopie belegen. Wertvermehrende Investitionen, Neubau/Umbau, Ersatzbauten, Behebung konstruktiver Mängel, Fahrnis nicht abziehbar (Anteil in Spalte Anlagekosten/Mehrwert). Energiespar-/Umweltschutzmassnahmen und Rückbaukosten für Ersatzneubau abziehbar; Förderbeiträge mindern die Kosten. Überschiessende Kosten (negatives Reineinkommen) auf die nächsten zwei Steuerperioden übertragbar (2025: Kosten aus 2023/2024 geltend machen; Rest in 2026 und 2027). Zeitliche Abgrenzung nach Rechnungsstellung oder Bezahlung, Wahl beibehalten.
- **Quellen:**
  - [Formular 8 TG 2025 S. 1](../../chunks/tg/2025/tg-form-08-2025/tg-form-08-2025__c0001.md) `tg-form-08-2025__c0001` – «1. Füllen Sie bitte pro Liegenschaft ein Formular aus.»
  - [WL TG 2025 S. 49](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0234.md) `tg-wl-2025__c0234` – «Für Einzelbeträge ab Fr. 1'000 legen Sie der Steuererklärung bitte die Rechnungskopien (inkl. der»
  - [WL TG 2025 S. 49–50](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0235.md) `tg-wl-2025__c0235` – «nicht mit dem Reineinkommen verrechneten Kosten auf die beiden nachfolgenden Steuerperioden»

## Hilfsblatt Zuwendungen

<a id="form-6-gemeinn-tzig-abzug-spenden"></a>
### Ziff. Form. 6 gemeinnützig – Zuwendungen für gemeinnützige oder öffentliche Zwecke (Name und Sitz der Institution) → Berechnung abzugsfähige freiwillige Zuwendungen (Code 366)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigungen (ab Fr. 1'000 pro Zuwendung einreichen)
- **Regel:** Einzeln mit Name und Sitz der empfangenden Institution aufführen. Berechnung: Total minus Selbstbehalt Fr. 200 (Staat) bzw. ohne Selbstbehalt (Bund, ab Gesamtbetrag Fr. 100); Staat max. Fr. 8'000 bei Nettoeinkommen bis Fr. 40'000, sonst max. 20% des Nettoeinkommens; Bund max. 20%. Übertrag Ziff. 23.2.
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 200 (Freiwillige Zuwendungen kantonal nur abziehbar, soweit gesamthaft CHF 200 übersteigend (Bund: ab CHF 100).)** · Bund **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen (CH) bzw. Gemeinwesen: mindestens CHF 100 im Steuerjahr)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Maximal 20% des Nettoeinkommens (Ziff. 22); bei Nettoeinkommen bis CHF 40'000 maximal CHF 8'000. Nur an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentliche/gemeinnützige Zwecke) sowie Bund/Kantone/Gemeinden.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Bund:** Bund: kein Selbstbehalt, max. 20%.
- **Quellen:**
  - [Formular 6 TG 2025 S. 1](../../chunks/tg/2025/tg-form-06-2025/tg-form-06-2025__c0002.md) `tg-form-06-2025__c0002` – «abzüglich Selbstbehalt (Staats- und Gemeindesteuern)   –   200.–»
  - [WL TG 2025 S. 46](../../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0220.md) `tg-wl-2025__c0220` – «Deklaration   Führen Sie die freiwilligen Zuwendungen und/oder die Mitgliederbeiträge und Zuwendungen an po»

<a id="form-6-parteien-abzug-parteispenden"></a>
### Ziff. Form. 6 Parteien – Mitgliederbeiträge und Zuwendungen an politische Parteien (Code 347) → Ziff. 15.5

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Quittungen/Bescheinigungen der Partei (ab Fr. 1'000 pro Zuwendung einreichen)
- **Regel:** Spalte «politische Parteien»; Maximum Staat Fr. 10'000, Bund Fr. 10'600; Übertrag Ziff. 15.5.
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister, im kantonalen Parlament vertreten oder mind. 3% Stimmen): max. CHF 10'000.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
- **Quellen:**
  - [Formular 6 TG 2025 S. 1](../../chunks/tg/2025/tg-form-06-2025/tg-form-06-2025__c0002.md) `tg-form-06-2025__c0002` – «Total Mitgliederbeiträge und Zuwendungen an politische Parteien (Übertrag von Buchstabe B)   347»
