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
- **Rein:** Ausweis/Zivilstandsdokument → Name, Geburtsdatum, Zivilstand, Konfession (Stand 31.12.2026) · Lohnausweis/Arbeitsvertrag → Beruf, Arbeitgeber/in, Arbeitsort · Verfügung Ergänzungsleistungen → Checkbox «EL zur AHV/IV» ja/nein · Aufdruck Original-Hauptformular S. 1 → Registernummer (AHVN13) für Software/Beilagen
- **Rechnen:** Stichtag 31.12.2026 bzw. Ende Steuerpflicht; Registernummer (= AHVN13) + Name auf allen Formularen und Beilagen
- **Regel:** Stand 31.12.2026 bzw. Ende der Steuerpflicht (Stichtagsprinzip). Bei gemeinsam besteuerten Personen durchgehend dieselbe Person als Person 1 bzw. Person 2 verwenden (Hauptformular und alle Hilfsblätter). Registernummer (AHVN13) auf Formularen und Beilagen angeben.
- **Beachten:** Gemeinsam Besteuerte: einmal gewählte Person 1/2 in Hauptformular und allen Hilfsblättern beibehalten
- **Beachten:** Kanton: Vollsplitting (Divisor 2) für Verheiratete/eingetr. Partner und Einelternfamilien → Zivilstand/Haushalt prüfen
- **Beachten:** EL zur AHV/IV nur ankreuzen – EL selbst sind steuerfrei, nicht in Ziff. 3.1 erfassen
- **Quellen:**
  - [Formular 1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0002.md) `tg-form-01-2026__c0002` – «Personalien, Berufs- und Familienverhältnisse am 31. Dezember 2026 oder am Ende der Steuerpflicht»
  - [WL TG 2026 S. 12](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0044.md) `tg-wl-2026__c0044` – «Achten Sie bitte darauf, in den Formularen unter Person 1 bzw. Person 2 durchgehend die Angaben»
  - [WL TG 2026 S. 9](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0029.md) `tg-wl-2026__c0029` – «Die Registernummer entspricht Ihrer AHVN13-Nummer.»
  - [WL TG 2026 S. 52](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0243.md) `tg-wl-2026__c0243` – «einkommen durch den Divisor 2 (Vollsplitting) zu teilen.»
  - [WL TG 2026 S. 18](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0073.md) `tg-wl-2026__c0073` – «Steuerfrei und deshalb nicht anzugeben sind: – Ergänzungsleistungen der AHV und IV;»

<a id="s-1-kinder-sozialabzug-kinder"></a>
### Ziff. S. 1 Kinder – Minderjährige, in Ausbildung stehende oder erwerbsunfähige Kinder, deren Unterhalt bestritten wird

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien der Kinder (Geburtsdatum, Haushalt, Schule/Lehrfirma, Ausbildungsende; bei getrennt besteuerten Eltern Alimente/Sorgerecht/Obhut)
- **Rein:** Geburtsurkunde/Familienausweis → genaues Geburtsdatum (Jahrgang bestimmt Abzugshöhe) · Lehrvertrag/Schul-/Studienbestätigung → Ausbildungsstätte + voraussichtliches Ende (Jg. 2007 und älter) · Scheidungs-/Trennungsurteil, Unterhaltsvertrag → Alimente ja/nein, gemeinsames Sorgerecht, alternierende Obhut · Angaben Mandant → Kind im eigenen Haushalt? gemeinsames Kind mit Konkubinatspartner/in?
- **Rechnen:** Ziff. 25.1 je Kind: Kanton Fr. 10'600 (Ausbildung, Jg. 2001–2006) / Fr. 8'500 (Ausbildung, Jg. 2007–2010) / Fr. 7'400 (übrige); Bund Fr. 6'800
- **Regel:** Genaues Geburtsdatum eintragen (Jahrgang entscheidet über die Höhe des Kinderabzugs, Ziff. 25.1). Bei Jahrgang 2007 und älter in Ausbildung: Ausbildungsstätte/Lehrfirma und voraussichtliches Ende der Ausbildung. Bei getrennt besteuerten Eltern zusätzlich Angaben zu Unterhaltsbeiträgen, gemeinsamem Sorgerecht und alternierender Obhut (Zuteilung Kinderabzug/Freibetrag/Drittbetreuung).
- **Beachten:** Kanton (minderjährig): mit Alimenten nur Empfänger; hälftig nur bei gem. Sorge + alternierender Obhut ohne Alimente
- **Beachten:** Bund: gem. Sorgerecht ohne Alimente genügt für hälftige Teilung; volljährige Kinder immer ungeteilt
- **Beachten:** Kein Abzug für Pflege-/Stiefkinder und volljährige Kinder mit Einkommen für selbständigen Lebensunterhalt
- **Limiten:**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 8'500 (Kind in Ausbildung nach Vollendung des 16. Altersjahres (WL 2026: Jahrgang 2007-2010): Fr. 8'500.)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Abzug CHF 6'800 (kein höherer Ausbildungsabzug beim Bund).)**
  - Kinderabzug Schulalter (CHF): Kanton **n/a** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800, keine Staffelung nach Alter; siehe sozialabzug.kind.**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 7'400 (Kinderabzug je Kind (nicht selbstaendig besteuert, in Ausbildung oder erwerbsunfaehig, Unterhalt wird getragen): Fr. 7'400 ('uebriges Kind'). Stichtag 31.12.2026. Zusaetzlich Steuergutschrift max. Fr. 100 pro minderjaehriges Kind mit der Schlussrechnung.)** · Bund **CHF 6'800 (Kinderabzug CHF 6'800 pro minderjähriges oder in beruflicher/schulischer Ausbildung stehendes Kind, für dessen Unterhalt die steuerpflichtige Person sorgt; bei getrennter Besteuerung der Eltern hälftig bei gemeinsamer elterlicher Sorge ohne Unterhaltsbeiträge.)**
  - Kinder-Ausbildungsabzug Zusatz/Höherstufe (kantonal verschieden: SG zusätzlicher Ausbildungskostenabzug über Selbstbehalt; TG erhöhter Kinderabzug 20.–26. Altersjahr, ersetzt Grund-/16+-Abzug, nicht kumulativ – siehe Text) (CHF): Kanton **CHF 10'600 (Kind in Ausbildung nach Vollendung des 20. bis zum vollendeten 26. Altersjahr (WL 2026: Jahrgang 2001-2006): Fr. 10'600. Anstelle von sozialabzug.kind/kind_ausbildung (der Abzug «erhöht sich … auf»), nicht zusätzlich.)** · Bund **n/a – Bund: kein erhöhter Abzug für auswärtige Ausbildung; einheitlich CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).**
- **Quellen:**
  - [Formular 1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0003.md) `tg-form-01-2026__c0003` – «Minderjährige, in beruflicher Ausbildung stehende oder erwerbsunfähige Kinder, deren Unterhalt Sie bestreiten»
  - [WL TG 2026 S. 12](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0044.md) `tg-wl-2026__c0044` – «Für Kinder mit Jahrgang 2007 und älter, welche sich in Ausbildung befinden, geben Sie bitte»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0107.md) `tg-wl-2026__c0107` – «für jedes Kind in Ausbildung mit Jahrgang 2001 – 2006 Fr. 10'600 Fr. 6'800»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0107.md) `tg-wl-2026__c0107` – «für jedes übrige Kind Fr. 7'400 Fr. 6'800»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0107.md) `tg-wl-2026__c0107` – «Kein Kinderabzug kann für Pflegekinder, Stiefkinder etc. geltend gemacht werden.»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0108.md) `tg-wl-2026__c0108` – «Der Kinderabzug steht nur dem die zu versteuernden Unterhaltsbeiträge (Alimente)»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0109.md) `tg-wl-2026__c0109` – «sich das (minderjährige) Kind in alternierender Obhut beider Elternteile, erfolgt eine hälftige Teilung»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0111.md) `tg-wl-2026__c0111` – «Besteht ein gemeinsames Sorgerecht und fliessen keine Unterhaltsbeiträge»
  - [WL TG 2026 S. 24–25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0112.md) `tg-wl-2026__c0112` – «Bei volljährigen Kindern wird der Kinderabzug immer ungeteilt einem Elternteil zugesprochen.»

<a id="s-1-unterst-tzte-sozialabzug-unterstuetzung"></a>
### Ziff. S. 1 Unterstützte – Erwerbsunfähige und unterstützungsbedürftige Personen (ohne aufgeführte Kinder)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Name, Geburtsdatum, Adresse, Haushalt, Unterstützungsbetrag
- **Rein:** Überweisungsbelege/Quittungen → jährlicher Unterstützungsbetrag · Nachweis Erwerbsunfähigkeit (gesundheitlich) und Bedürftigkeit → Voraussetzung · Personalien unterstützte Person → Name, Geburtsdatum, Adresse, gleicher Haushalt ja/nein
- **Rechnen:** Ziff. 25.2 je Person: Kanton Fr. 2'700 (Beitrag > 50 % betreibungsrechtl. Existenzminimum) / Bund Fr. 6'800 (Beitrag mind. Fr. 6'800)
- **Regel:** Formular nennt als Schwelle jährlicher Beitrag von mindestens Fr. 12'000 (Kanton) bzw. Fr. 6'800 (Bund). Wegleitung Ziff. 25.2 verlangt kantonal nachweislich mindestens 50% des betreibungsrechtlichen Existenzminimums; Bund mindestens Fr. 6'800 (Details siehe Ziff. 25.2).
- **Beachten:** Nicht für Ehegatte/eingetr. Partner/in und Kinder mit Kinderabzug oder abgezogenen Unterhaltsbeiträgen
- **Beachten:** Löst Zuschlag Versicherungsabzug aus: Kanton Fr. 1'000 / Bund Fr. 700 je unterstützte Person
- **Beachten:** Formular nennt Kanton mind. Fr. 12'000/Jahr, WL/StV § 12 «> 50 % Existenzminimum» – Nachweis sichern
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'700 (Unterstuetzungsabzug je erwerbsunfaehige und unterstuetzungsbeduerftige Person (nicht Ehegatte/Kind mit Kinderabzug): Fr. 2'700; Voraussetzung: Beitrag zu mehr als 50 % des betreibungsrechtlichen Existenzminimums.)** · Bund **CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag zum Versicherungsabzug: Fr. 1'000 je minderjaehriges oder in Ausbildung stehendes Kind bzw. unterstuetzte Person (fuer die Kinder-/Unterstuetzungsabzug moeglich ist).)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**
- **Quellen:**
  - [Formular 1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0004.md) `tg-form-01-2026__c0004` – «die Sie mit einem jährlichen Beitrag von mindestens Fr. 12 000.– (Kanton) bzw. Fr. 6 800.– (Bund) unterstützen»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0113.md) `tg-wl-2026__c0113` – «Bei der direkten Bundessteuer beträgt der Unterstützungsabzug Fr. 6'800 für jede erwerbsunfähige»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0113.md) `tg-wl-2026__c0113` – «können Sie kantonal Fr. 2 700 abziehen.»
  - [StV TG § 12](../../chunks/tg/2025/tg-stv/tg-stv__par-12.md) `tg-stv__par-12` – «sofern er zu mehr als 50 Prozent des betreibungsrechtlichen Existenzminimums zum Unterhalt beiträgt»
  - [StP 34 Nr. 27](../../chunks/tg/dauernd/tg-stp-34-27/tg-stp-34-27__c0002.md) `tg-stp-34-27__c0002` – «je Kind oder unterstützte Person | Fr. 1’000»

<a id="s-1-unterj-hrige-steuerpflicht-personalien"></a>
### Ziff. S. 1 unterjährige Steuerpflicht – Dauer bei unterjähriger Steuerpflicht – Person 1 / Person 2 (von Tag/Monat bis Tag/Monat)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zuzug-/Wegzugs-/Todesdatum (Angaben des Mandanten)
- **Rein:** Zu-/Wegzugsbestätigung Einwohneramt (Ausland) → Datum von/bis · Todesurkunde → Todesdatum (Ende bzw. Beginn der Steuerpflicht)
- **Rechnen:** Einkommen nur für Dauer der Steuerpflicht; Satz von Amtes wegen: regelmässige Einkünfte ÷ Monate Steuerpflicht × 12; Sozialabzüge anteilig
- **Regel:** Nur bei Steuerpflicht während eines Teils der Steuerperiode ausfüllen. Sozialabzüge für Kinder und unterstützte Personen: Verhältnisse am 31.12.2026 bzw. am Ende der Steuerpflicht massgebend; bei Teilperiode werden sie anteilig nach Dauer der Steuerpflicht gewährt.
- **Beachten:** Nur Zuzug aus/Wegzug ins Ausland und Tod; Zuzug aus anderem Kanton = ganzes Jahr TG, Wegzug = neuer Kanton
- **Beachten:** Tod Ehegatte/Partner: zwei Steuerpflichten – gemeinsam bis Todestag, danach überlebende Person separat
- **Beachten:** Einmalige Einkünfte (Gratifikation, Dividende, Jahreszins) nicht umrechnen; Vermögen per Wegzugsdatum
- **Quellen:**
  - [Formular 1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0001.md) `tg-form-01-2026__c0001` – «Dauer bei unterjähriger Steuerpflicht»
  - [WL TG 2026 S. 23–24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0106.md) `tg-wl-2026__c0106` – «Besteht die Steuerpflicht nur während eines Teils der Steuerperiode, werden die Sozialabzüge an-»
  - [WL TG 2026 S. 6](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0016.md) `tg-wl-2026__c0016` – «Zuzug aus / Wegzug ins Ausland»
  - [WL TG 2026 S. 6](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0013.md) `tg-wl-2026__c0013` – «Zuzüger aus einem anderen Kanton sind für die ganze Steuerperiode»
  - [WL TG 2026 S. 6](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0015.md) `tg-wl-2026__c0015` – «Beim Tod einer gemeinsam besteuerten Person»
  - [WL TG 2026 S. 7](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0019.md) `tg-wl-2026__c0019` – «(Fr. 28 000 : 8 x 12)»
  - [WL TG 2026 S. 7](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0018.md) `tg-wl-2026__c0018` – «Als unregelmässige Einkünfte gelten etwa Jahresgratifikationen, Treueprämien, Liquidationsgewinne, Dividenden»
  - [WL TG 2026 S. 6](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0013.md) `tg-wl-2026__c0013` – «Das Vermögen ist mit dem Stand per Datum des Wegzugs anzugeben.»
  - [WL TG 2026 S. 6–7](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0017.md) `tg-wl-2026__c0017` – «Regelmässig fliessende Einkünfte und regelmässig anfallende Aufwendungen werden bei ei- ner unterjährigen Steuerpflicht»

<a id="s-1-auszahlung-verrechnungssteuer-rueckerstattung"></a>
### Ziff. S. 1 Auszahlung – Steuerrückzahlungen inkl. Rückerstattung der Verrechnungssteuer – Auszahlungskonto (IBAN)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Vorgemerktes Auszahlungskonto bzw. Angaben bei Änderung (Kontoinhaber/in, IBAN, Bank/Post)
- **Rein:** Bank-/Postverbindung → Kontoinhaber/in, IBAN, Bank/Post (nur bei Erstantrag oder Änderung)
- **Rechnen:** VSt-Anspruch Form. 2 Ziff. 10 = 35 % × Total I Bruttoerträge Spalte 8 (Ziff. 3) → Auszahlung auf bezeichnetes Konto
- **Regel:** Alle Rückerstattungen der Verrechnungssteuer und allfällige Steuerrückzahlungen erfolgen auf das bezeichnete Konto. Ist kein Konto vorgemerkt oder soll es geändert werden, Felder ausfüllen; bei Bank und Post IBAN angeben. Kontoänderungen nach Einreichung der Steuererklärung unterlassen (Verzögerung).
- **Beachten:** Rückerstattung durch TG nur bei Wohnsitz TG am 31.12.2026 und deklarierten Erträgen
- **Beachten:** Kontoänderungen nach Einreichung vermeiden (Verzögerung); Auszahlung unter Rückforderungsvorbehalt ESTV
- **Beachten:** Erben: VSt auf Erträgen der Erbschaft im eigenen Wohnsitzkanton zurückfordern
- **Quellen:**
  - [Formular 1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0005.md) `tg-form-01-2026__c0005` – «Alle Rückerstattungen der Verrechnungssteuer sowie allfälliger Steuerrückzahlungen erfolgen»
  - [WL TG 2026 S. 12–13](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0046.md) `tg-wl-2026__c0046` – «wie auch beim Postkonto die IBAN-Nummer an.»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0166.md) `tg-wl-2026__c0166` – «sind 35% (Verrechnungssteueranspruch) in Ziffer 10 auf Seite 2 des Formulars 2 zu übertragen.»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0166.md) `tg-wl-2026__c0166` – «welche am 31. Dezember 2026 ihren Wohnsitz»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0167.md) `tg-wl-2026__c0167` – «erfolgt daher unter Vorbehalt des Rückforderungsrechtes»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0166.md) `tg-wl-2026__c0166` – «Ein Anspruch auf Rückerstattung der Verrechnungssteuer besteht nur, wenn Sie die Erträge in der Steuererklärung deklariert haben.»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0167.md) `tg-wl-2026__c0167` – «bitten wir Sie, von Kontoänderungen nach Einreichung der Steuererklä»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0166.md) `tg-wl-2026__c0166` – «Vom Total I der Bruttoerträge 2026 der Spalte 8 in Ziffer 3»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0167.md) `tg-wl-2026__c0167` – «Erbinnen und Erben haben die Verrechnungssteuer auf ihren Erbschaftserträgen in ihrem Wohn-»

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Haupterwerbstätigkeit unselbständig – Person 1 (Code 100) / Person 2 (Code 101)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 Nettolohn (Pauschalspesen: Vorspalte; Naturalbezüge/Trinkgelder falls nicht im Lohnausweis)
- **Rein:** Lohnausweis → Ziff. 11 Nettolohn (je Person, je Arbeitgeber) · Lohnausweis → Ziff. 13.2 Pauschalspesen → Vorspalte (*) · Aufstellung Trinkgelder/Naturalbezüge → Zuschlag, falls nicht im Lohnausweis · Lohnausweis → Felder F/G, Ziff. 15 (Schichttage) → Formular 4.2
- **Rechnen:** Σ LA Ziff. 11 (= Ziff. 8 − Ziff. 9 − Ziff. 10) je Person + nicht bescheinigte Trinkgelder/Naturalbezüge (volle Kost+Logis i.d.R. Fr. 11'880/Jahr)
- **Regel:** Nettolohn gemäss Lohnausweis Ziff. 11 einsetzen (Brutto Ziff. 8 minus AHV/ALV/BVG-Abzüge Ziff. 9 und 10). Pauschalspesen ohne entsprechende Ausgaben sind steuerbar und in die Vorspalte (*) einzutragen. Trinkgelder und nicht im Lohnausweis enthaltene Naturalbezüge zusätzlich deklarieren (volle Verpflegung/Unterkunft in der Regel Fr. 11'880/Jahr). Lohnausweis-Felder: Feld F (Kreuz = keine Arbeitswegkosten) → kein Fahrkostenabzug in Form. 4.2 Ziff. 2; Feld G (Lunch-Checks/Kantine/Personalrestaurant) → nur halber Verpflegungsabzug (Ziff. 3.2); Ziff. 10.2 (BVG-Einkauf, vom Lohn abgezogen) ist im Nettolohn schon berücksichtigt → nicht nochmals in Ziff. 15.2; Ziff. 13.3 (Arbeitgeberbeiträge Weiterbildung) mindern den Weiterbildungsabzug Ziff. 16; Ziff. 15 (Bemerkungen) enthält u.a. Anzahl Schichttage → Form. 4.2 Ziff. 3.1.
- **Beachten:** LA Feld F / Geschäftsfahrzeug (Privatanteil 0.9 %/Monat inkl. Arbeitsweg) → kein Fahrkostenabzug Form. 4.2
- **Beachten:** LA Feld G (Lunch-Checks, Kantine) → nur halber Verpflegungsabzug: Fr. 7.50/Tag, max. Fr. 1'600
- **Beachten:** PK-Einkauf per Lohnabzug (LA Ziff. 10.2) ist im Nettolohn bereits abgezogen → nicht nochmals in Ziff. 15.2
- **Bund:** Gleiche Erfassung; Spalten Staat/Bund identisch (Nettolohn Ziff. 11).
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0006.md) `tg-form-01-2026__c0006` – «1.1 Haupterwerbstätigkeit Person 1 100»
  - [WL TG 2026 S. 13](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0049.md) `tg-wl-2026__c0049` – «In die Steuererklärung ist der in Ziffer 11 des Lohnausweises aufgeführte Nettolohn einzusetzen.»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «In diesem Feld ist der für die Steuererklärung massgebende Nettolohn anzugeben.»
  - [WL TG 2026 S. 13](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0049.md) `tg-wl-2026__c0049` – «beträgt der Wert für volle Verpflegung und Unterkunft in der Regel Fr. 11'880 im Jahr»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «vom Bruttolohn total (Ziffer 8) das Total der Abzüge (Ziffer 9 und 10) abgezogen wird.»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer keine Kosten für den Arbeitsweg er»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0175.md) `tg-wl-2026__c0175` – «Im Gegenzug kann dafür kein Fahrkos-»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0175.md) `tg-wl-2026__c0175` – «Privatanteil Fahrzeug von 0.9 % pro Monat für die private Nut-»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer Lunch-Checks (vgl. Rz 18) abgege»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0185.md) `tg-wl-2026__c0185` – «Nur der halbe Abzug (Fr. 7.50 im Tag, Fr. 1'600 im Jahr) ist zulässig»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «In diesem Feld sind die im Bruttolohn enthaltenen, dem Arbeitnehmer vom Lohn abgezoge»
  - [WL Lohnausweis 2026 S. 17](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0045.md) `bund-wl-lohnausweis-2026__c0045` – «sind bei allen Arbeitnehmern im Lohnausweis betragsmässig anzugeben.»
  - [WL TG 2026 S. 13–14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0051.md) `tg-wl-2026__c0051` – «tragen Sie bitte in die entsprechenden Felder der Vorspalten zu den Ziffern 1.1 und 1.2 ein.»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0093.md) `tg-wl-2026__c0093` – «Die ordentlichen Beiträge sind in der Regel bereits vom Bruttolohn abgezogen»
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «die Anzahl im Kalenderjahr geleisteter Schichttage»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0184.md) `tg-wl-2026__c0184` – «Tragen Sie die Anzahl der geleisteten Schichttage bzw. Tage mit Nachtarbeit im Formular Berufs-»
  - [WL Lohnausweis 2026 S. 17](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0045.md) `bund-wl-lohnausweis-2026__c0045` – «Pauschale Spesenvergütungen (Einzelfallpauschalen gemäss Rz 52 fallen nicht darunter)»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Nebenerwerbstätigkeit unselbständig – Person 1 (Code 104) / Person 2 (Code 105)

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nebenerwerb) bzw. Honorarabrechnung; Verwaltungsratshonorare, Sitzungsgelder
- **Rein:** Lohnausweis Nebenerwerb → Ziff. 11 Nettolohn · Abrechnung Behörde/Verein/Prüfungskommission → Sitzungs-/Taggelder, Entschädigungen · Abrechnung VR-Honorare/Tantiemen → Betrag · Mietvertrag Hauswart/Verwalter → Differenz normaler − reduzierter Mietzins
- **Rechnen:** Σ Nettoeinkünfte aller Nebenerwerbe je Person (unabhängig von AHV-Freigrenzen) + Mietzinsreduktion; Pauschalspesen in Vorspalte
- **Regel:** Sämtliches Einkommen aus unselbständiger Nebentätigkeit ist unabhängig von der Höhe (auch unter AHV-Freigrenze) zu deklarieren: Behördenentschädigungen, Sitzungs-/Taggelder, VR-Honorare, Tantiemen, Mietzinsreduktion Hauswart (Differenz normaler/reduzierter Mietzins). Pauschalspesen in die Vorspalte. Berufsauslagen Nebenerwerb: Form. 4.2 Ziff. 6.
- **Beachten:** Form. 4.2 Ziff. 6: Pauschale 20 % der Nettoeinkünfte, min. Fr. 800 / max. Fr. 2'400 (Kanton = Bund), höchstens Einkommen
- **Beachten:** Einzige geringfügige Tätigkeit (z.B. Studenten, Rentner) gilt als Haupterwerb → Ziff. 1.1
- **Beachten:** Vom Volk gewählte Gemeinderäte/Schul-/Kirchenvorsteher: Behördenpauschale 50 %, min. Fr. 2'000, max. Fr. 4'000
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Nebenerwerb (unselbstaendig): Pauschale 20 % der Nettoeinkuenfte; sie gilt alle Berufskosten des Nebenerwerbs (Fahrt, Verpflegung, uebrige) ab. Nachweis hoeherer effektiver Kosten vorbehalten; maximal bis Hoehe des Nebenerwerbseinkommens.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb-Pauschale: Minimum Fr. 800 im Jahr.)** · Bund **CHF 800 (Mindestbetrag Pauschale Nebenerwerb.)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb-Pauschale: Maximum Fr. 2'400 im Jahr.)** · Bund **CHF 2'400 (Höchstbetrag Pauschale Nebenerwerb.)**
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0006.md) `tg-form-01-2026__c0006` – «1.2 Nebenerwerbstätigkeit Person 1 104»
  - [WL TG 2026 S. 13](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0050.md) `tg-wl-2026__c0050` – «Daher ist sämtliches Einkommen aus einer unselbständigen Nebenerwerbstätigkeit»
  - [WL TG 2026 S. 40–41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0190.md) `tg-wl-2026__c0190` – «Der Abzug beträgt 20% der Nettoeinkünfte, mindestens aber Fr. 800 und höchstens Fr. 2'400 im Jahr.»
  - [WL TG 2026 S. 41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0191.md) `tg-wl-2026__c0191` – «Ebenfalls als Haupterwerb betrachtet wird auch eine geringfügige Tätigkeit, sofern es sich um die einzige Er»
  - [WL TG 2026 S. 41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0192.md) `tg-wl-2026__c0192` – «Der Pauschalabzug beträgt 50% von den insgesamt ausgerichteten Behördenentschädigungen»
  - [WL TG 2026 S. 41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0192.md) `tg-wl-2026__c0192` – «mindestens Fr. 2'000 und höchstens Fr. 4'000.»
  - [WL TG 2026 S. 40–41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0190.md) `tg-wl-2026__c0190` – «Es können maximal Berufskosten bis zur Höhe des unselbständigen Erwerbseinkommens der zu- gehörigen Tätigkeit in Abzug gebracht werden.»
  - [WL TG 2026 S. 40–41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0190.md) `tg-wl-2026__c0190` – «Staats- und Gemeindesteuern als auch bei der direkten Bundessteuer ein Pauschalabzug getätigt»

<a id="1-2-feuerwehr-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 (Feuerwehr) – Sold Milizfeuerwehr (Kernaufgaben) – steuerfrei bis Freibetrag

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis / Soldabrechnung Feuerwehr
- **Rein:** Soldabrechnung/Lohnausweis Feuerwehr → Sold Kernaufgaben (Übungen, Kurse, Inspektionen, Pikett, Ernstfall) · Abrechnung Kader-/Funktionszulagen, Administration, Instruktion, freiwillige Dienste → voll steuerbar
- **Rechnen:** Kanton: max(0; Sold Kernaufgaben − Fr. 5'000) + Kader-/Funktionszulagen, Admin, freiwillige Dienste, Instruktion / Bund: Freibetrag Fr. 5'400
- **Regel:** Sold für Kernaufgaben (Übungen, Kurse, Inspektionen, Pikett, Ernstfalleinsätze) ist bis zum Freibetrag steuerfrei; darüber sowie Pauschalzulagen Kader, Funktionszulagen, administrative Arbeiten und Instruktorenentschädigung steuerbar. In der Steuererklärung die bei Staats-/Gemeindesteuern steuerbaren Einkünfte deklarieren; die Korrektur für die Bundessteuer macht die Steuerverwaltung von Amtes wegen.
- **Beachten:** Nur den kantonal steuerbaren Betrag deklarieren; Bundeskorrektur (Fr. 5'400) macht die Steuerverwaltung von Amtes wegen
- **Beachten:** Saalwachen, Verkehrsdienst u.ä. sind keine Kernaufgaben → voll steuerbar
- **Limiten:**
  - Feuerwehrsold steuerfrei bis (CHF): Kanton **CHF 5'000 (Sold der Milizfeuerwehrleute fuer Kernaufgaben bis Fr. 5'000 jaehrlich steuerfrei (Staats- und Gemeindesteuern); Bund Fr. 5'400 (Korrektur von Amtes wegen).)** · Bund **CHF 5'400 (Sold der Milizfeuerwehrleute für Kernaufgaben steuerfrei bis CHF 5'400 pro Jahr (ausgenommen Pauschalzulagen für Kader, Funktionszulagen, administrative Arbeiten, freiwillige Dienstleistungen); gesamter Sold im Lohnausweis deklarieren.)**
- **Bund:** Freibetrag Bund Fr. 5'400 (statt Fr. 5'000 Kanton); Korrektur von Amtes wegen.
- **Quellen:**
  - [WL TG 2026 S. 13–14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0051.md) `tg-wl-2026__c0051` – «Fr. 5'000 bei der Staats- und Gemeindesteuer;»
  - [WL TG 2026 S. 13–14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0051.md) `tg-wl-2026__c0051` – «Fr. 5'400 bei der direkten Bundessteuer.»
  - [WL TG 2026 S. 13–14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0051.md) `tg-wl-2026__c0051` – «Ebenfalls steuerbar ist die Instruktorenentschädigung.»
  - [WL TG 2026 S. 13–14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0051.md) `tg-wl-2026__c0051` – «Die Steuerverwaltung nimmt bei der direkten Bun- dessteuer von Amtes wegen eine Korrektur vor.»

<a id="1-3-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 1.3 – Im vereinfachten Abrechnungsverfahren bereits versteuerter Bruttolohn – Person 1 (Code 106) / Person 2 (Code 107)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der AHV-Ausgleichskasse (Bruttolohnsumme)
- **Rein:** Bescheinigung der AHV-Ausgleichskasse (vereinfachtes Abrechnungsverfahren) → Bruttolohnsumme in Vorkolonne
- **Rechnen:** Nur Information: Bruttolohn in Vorkolonne; nicht in Zwischentotal Ziff. 6, weder steuerbar noch satzbestimmend
- **Regel:** Nur zur Information deklarieren (Vorkolonne); wird nicht in das Zwischentotal Ziff. 6 einbezogen und weder als steuerbares noch als satzbestimmendes Einkommen berücksichtigt. Bescheinigung der Ausgleichskasse beilegen.
- **Beachten:** Diese Löhne nicht zusätzlich in Ziff. 1.1/1.2 erfassen (bereits per Quellensteuerabzug besteuert)
- **Beachten:** Bescheinigung der Ausgleichskasse beilegen
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0006.md) `tg-form-01-2026__c0006` – «1.3 Im vereinfachten Abrechnungsverfahren bereits versteuerter Bruttolohn»
  - [WL TG 2026 S. 14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0052.md) `tg-wl-2026__c0052` – «Diese Deklaration dient nur zu Informationszwecken.»
  - [WL TG 2026 S. 14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0052.md) `tg-wl-2026__c0052` – «weder als steuerbares noch als satzbestimmendes Einkommen berücksichtigt»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Haupterwerbstätigkeit selbständig – Person 1 (Code 112) / Person 2 (Code 113)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz/Erfolgsrechnung bzw. Einnahmen-/Ausgabenaufstellung; Privatkonto; Abschreibungstabelle; bei Kollektiv-/Kommanditgesellschaft Bescheinigung der Gesellschaft
- **Rein:** Jahresrechnung (Bilanz + Erfolgsrechnung, unterzeichnet, Abschluss 2026) → Reingewinn/-verlust · Vereinfachte Buchführung: Einnahmen-/Ausgabenaufstellung + Aktiven/Passiven → Ergebnis · Privatkonto, Abschreibungstabelle → Beilagen (Privatanteile, Abschreibungen) · Bescheinigung Kollektiv-/Kommanditgesellschaft → Gesellschafterlohn, Gewinnanteil, Kapitalzins
- **Rechnen:** Reingewinn lt. Abschluss inkl. Naturalbezüge/Mietwert Geschäftshaus; Form. 14: Betriebserfolg + Beteiligungs-Nettogewinn × 60 % Kanton / 70 % Bund; Wert Spalte Kanton
- **Regel:** Steuerbares selbständiges Erwerbseinkommen (Spalte Kanton; bei Beteiligungen nach Teilbesteuerung/Formular 14) eintragen; wenn negativ mit Minuszeichen (*). Naturalbezüge aus dem eigenen Geschäft und Mietwert Wohnung im Geschäftshaus sind steuerbar. Eigene BVG-Beiträge nur Privatanteil als Abzug in Ziff. 15.2 (Arbeitgeberanteil bereits im Geschäftsergebnis). Liquidationsgewinne (ab 55 / Invalidität) sind im Geschäftsergebnis enthalten und werden unter Ziff. 23.3 wieder abgezogen. Bei Bundessteuer wird das Einkommen von Amtes wegen angepasst (Teilbesteuerung).
- **Beachten:** Eigene BVG: im Geschäft nur Arbeitgeberanteil (ohne Personal ½); Privatanteil → Ziff. 15.2, Säule 3a → Ziff. 13
- **Beachten:** Liquidationsgewinn (Aufgabe nach 55. Altersjahr/Invalidität) im Ergebnis lassen, Abzug in Ziff. 23.3
- **Beachten:** Nicht selbständige Einkünfte (mit AK abgerechneter Lohn Ehepartner, Familienzulagen) ausscheiden → andere Ziffern
- **Bund:** Steuerbares Bundeseinkommen kann wegen abweichendem Teilbesteuerungsabzug (Kanton 60%/Bund 70% Einbezug) vom kantonalen abweichen; wird von Amtes wegen aufgenommen.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0006.md) `tg-form-01-2026__c0006` – «2.1 Haupterwerbstätigkeit Person 1 112»
  - [WL TG 2026 S. 17](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0071.md) `tg-wl-2026__c0071` – «In die Steuererklärung ist das in der Spalte Kanton berechnete steuerbare Einkommen zu»
  - [WL TG 2026 S. 14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0055.md) `tg-wl-2026__c0055` – «Führen Sie eine Buchhaltung nach kaufmännischen Grundsätzen, reichen Sie die unterzeichnete»
  - [WL TG 2026 S. 17](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0069.md) `tg-wl-2026__c0069` – «60% (Spalte Kanton) bzw. 70% (Spalte Bund) des in Ziffer 8 ausgewiesenen Nettogewinns»
  - [WL TG 2026 S. 15](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0059.md) `tg-wl-2026__c0059` – «Ist kein solches Personal vorhanden, gilt die Hälfte der Beiträge als Arbeitgebendenanteil.»
  - [WL TG 2026 S. 16](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0063.md) `tg-wl-2026__c0063` – «können Sie daher unter Ziffer 23.3 wieder von den Einkünften in Abzug bringen»
  - [WL TG 2026 S. 15–16](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0061.md) `tg-wl-2026__c0061` – «Dies gilt etwa für einen mit Ihrer Ausgleichskasse (bereits) abgerechneten Lohn des Ehepartners.»
  - [WL TG 2026 S. 14–15](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0056.md) `tg-wl-2026__c0056` – «der Mietwert der selbstbenutzten Wohnung im eigenen Geschäftshaus.»
  - [WL TG 2026 S. 17](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0071.md) `tg-wl-2026__c0071` – «indem Sie den Betrag in Ziffer 11 zum Betriebserfolg in Ziffer 10»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Nebenerwerbstätigkeit selbständig – Person 1 (Code 116) / Person 2 (Code 117)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Netto-Einkommen aus Nebenerwerb (Honorarabrechnung/Aufstellung); landwirtschaftliches Nebengewerbe: Buchhaltungsabschluss oder Formular 18
- **Rein:** Honorar-/Provisionsabrechnungen → Einnahmen · Ausgabenbelege/Aufstellung → geschäftsmässig begründete Gewinnungskosten · Landwirtschaftliches Nebengewerbe → Buchhaltungsabschluss bzw. Formular 18 · Transaktionsliste gewerbsmässiger Wertschriften-/Liegenschaftenhandel → Gewinne (Detailblatt)
- **Rechnen:** Einnahmen − geschäftsmässig begründete Gewinnungskosten = Netto-Einkommen je Person; negativ mit «–»
- **Regel:** Netto-Einkommen aus selbständigem Nebenerwerb (z.B. Vermittlungsprovisionen, Gutachterhonorare, Buchhaltungsarbeiten, Privatunterricht) deklarieren; Ziff. 2.1 gilt sinngemäss. Gewerbsmässiger Wertpapier- und Liegenschaftenhandel gehört ebenfalls hierher (Detailaufstellung).
- **Beachten:** Nebenerwerb setzt Haupterwerb voraus; einzige geringfügige Tätigkeit gilt als Haupterwerb → Ziff. 2.1
- **Beachten:** Gewerbsmässige Liegenschaftsgewinne unterliegen der Einkommenssteuer (Kanton und Bund)
- **Beachten:** Ziff.-2-Einkommen wird der Ausgleichskasse gemeldet → nur selbständige Einkünfte hier
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0006.md) `tg-form-01-2026__c0006` – «2.2 Nebenerwerbstätigkeit Person 1 116»
  - [WL TG 2026 S. 17–18](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0072.md) `tg-wl-2026__c0072` – «Deklarieren Sie hier ein Netto-Einkommen aus einer selbständigen Nebenerwerbstätigkeit»
  - [WL TG 2026 S. 41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0191.md) `tg-wl-2026__c0191` – «Ein Nebenerwerb setzt das Vorliegen einer unselbständigen oder selbständigen Haupterwerbstä»
  - [WL TG 2026 S. 15](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0058.md) `tg-wl-2026__c0058` – «Deklarieren Sie die Einkünfte nach Abzug der geschäftsmässig begründeten Gewinnungskosten.»
  - [WL TG 2026 S. 15–16](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0061.md) `tg-wl-2026__c0061` – «wird den Ausgleichskassen zur Festsetzung der Sozialversicherungsbeiträge gemel»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV-/IV-Renten – Person 1 (Code 130) / Person 2 (Code 131)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung AHV/IV (Jahresbetrag brutto)
- **Rein:** Rentenbescheinigung AHV/IV (Ausgleichskasse) → Jahresrente brutto je Person
- **Rechnen:** 100 % der AHV-/IV-Jahresrente je Person (Kanton und Bund)
- **Regel:** Zu 100% steuerbar (Staat und Bund). Ergänzungsleistungen zur AHV/IV sind steuerfrei und nicht anzugeben; ebenso Sozialhilfe und Genugtuungszahlungen.
- **Beachten:** EL zur AHV/IV, Sozialhilfe und Genugtuung sind steuerfrei → nicht angeben
- **Beachten:** Militärversicherungsrenten mit Beginn vor 1994 steuerfrei (ebenso AHV/IV im Umfang der MV-Kürzung)
- **Beachten:** Kanton: Zusatzabzug Ziff. 25.3 für AHV-Altersrentner/Erwerbsunfähige/Verwitwete max. Fr. 4'200; Bund keiner
- **Limiten:**
  - Abzug AHV-Alter/erwerbsunfähig/verwitwet (CHF): Kanton **CHF 4'200 (Abzug fuer AHV-Altersrentner, Erwerbsunfaehige und Verwitwete (nur Kanton): max. Fr. 4'200; Reduktion um Fr. 200 je Fr. 1'000 Mehreinkommen ab Reineinkommen ueber Fr. 16'900 (Alleinstehende) bzw. Fr. 24'300 (Gemeinsam Besteuerte); kein Abzug ab Fr. 37'900 bzw. Fr. 45'300.)** · Bund **n/a – Kantonaler Abzug; die direkte Bundessteuer kennt keinen Abzug für AHV-Alter/Erwerbsunfähigkeit/Verwitwung (Art. 35 DBG).**
- **Bund:** Ebenfalls 100% steuerbar.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0007.md) `tg-form-01-2026__c0007` – «3.1 AHV-/IV-Renten Person 1 130»
  - [WL TG 2026 S. 18](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0073.md) `tg-wl-2026__c0073` – «Bundessteuer zu 100% steuerbar.»
  - [Kurz-WL TG 2026 S. 1](../../chunks/tg/2026/tg-wl-kurz-2026/tg-wl-kurz-2026__c0007.md) `tg-wl-kurz-2026__c0007` – «für AHV-Altersrentner, Erwerbsunfähige oder Verwitwete max. Fr. 4 200 kein Abzug»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen (2. Säule, SUVA, Säule 3a/3b, Leibrenten) – steuerbarer Bruttobetrag und Prozentsatz – Person 1 (Code 132) / Person 2 (Code 133)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Rentenbescheinigung Pensionskasse/SUVA/Versicherung (steuerbarer Betrag und Prozentsatz)
- **Rein:** Rentenbescheinigung Pensionskasse → Bruttorente + Prozentsatz · Rentenbescheinigung SUVA/Unfallversicherer → Bruttorente · Bescheinigung Lebensversicherer (Leibrente, Säule 3b) → steuerbarer Ertragsanteil, Überschussleistungen · Bescheinigung Säule 3a-Rente / IV-Rente 3b → Bruttorente
- **Rechnen:** Je Rente: Bruttobetrag × Satz (BVG/3a/IV-Rente 3b 100 %; Übergangsrecht 80 %); Leibrente: Ertragsanteil lt. Bescheinigung + Überschüsse × 70 %
- **Regel:** Renten aus beruflicher Vorsorge, gebundener Selbstvorsorge und Invaliditätsrenten (3b) sind grundsätzlich zu 100% steuerbar. Übergangsbestimmung 80% nur bei mind. 20% Eigenbeiträgen und Rentenbeginn vor 1.1.1987 bzw. 1.1.1987–31.12.2001 (Vorsorgeverhältnis bestand am 31.12.1984; Bund 31.12.1986). Leibrenten: nur Ertragsanteil steuerbar, Überschussleistungen pauschal 70%; die Versicherung weist dies in der Bescheinigung aus (beilegen). Steuerbaren Betrag und Prozentsatz in die zwei Felder eintragen.
- **Beachten:** 80 % nur bei ≥ 20 % Eigenbeiträgen + Rentenbeginn vor 1987 bzw. vor 2002 mit Vorsorge am 31. Dezember 1984 (Bund 1986)
- **Beachten:** Mehr als zwei Renten: separate Aufstellung + Bescheinigungen beilegen; Leibrenten-Rückkauf: StP 24 Nr. 6
- **Beachten:** Kapitalleistungen aus Vorsorge nicht hier → Seite 4 unten (gesonderte Besteuerung)
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0007.md) `tg-form-01-2026__c0007` – «3.2 Renten/Pensionen Steuerbar Bruttobetrag / Fr. in Prozent»
  - [WL TG 2026 S. 18](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0074.md) `tg-wl-2026__c0074` – «Grundsätzlich sind Renten aus beruflicher Vorsorge, aus gebundener Selbstvorsorge sowie Invali-»
  - [WL TG 2026 S. 18](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0075.md) `tg-wl-2026__c0075` – «Überschussleistungen sind pauschal zu 70% steuerbar.»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0131.md) `tg-wl-2026__c0131` – «Kapitalleistungen mit Vorsorgecharakter aus AHV/IV, aus beruflicher Vorsorge und aus anerkann»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0083.md) `tg-wl-2026__c0083` – «Nicht in Ziffer 5.5, sondern auf der Steuererklärung, Seite 4 unten, sind Kapitalleistungen aus Vor-»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigungen (Taggelder ALV, KV, UV, IV, SUVA, Mutterschaft, EO) – Person 1 (Code 136) / Person 2 (Code 137)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Taggeldabrechnung/Bescheinigung (ALV, Krankentaggeld, Unfall, EO/Mutterschaft)
- **Rein:** Abrechnung Arbeitslosenkasse → ALV-Taggelder · Taggeldabrechnung Kranken-/Unfallversicherer, SUVA, IV → direkt ausbezahlte Taggelder · Abrechnung Ausgleichskasse (EO, Mutterschaft) → direkt ausbezahlte Entschädigung
- **Rechnen:** Σ Taggelder/EO/Mutterschaft je Person, soweit nicht im Lohnausweis bescheinigt und in Ziff. 1 enthalten
- **Regel:** Nur soweit nicht bereits im Lohnausweis bescheinigt und in Ziff. 1 enthalten (sonst doppelt). Dazu zählen auch ALV-Taggelder, SUVA-Taggelder, Mutterschaftsentschädigung und von der Ausgleichskasse direkt bezahlte EO. Soldzahlungen Militär/Zivilschutz/Feuerwehr und Taschengeld Zivildienst sind steuerfrei. Bescheinigung beilegen.
- **Beachten:** Über Arbeitgeber ausbezahlte Taggelder stehen im Lohnausweis → nicht doppelt erfassen
- **Beachten:** Sold Militär/Zivilschutz/Feuerwehr und Taschengeld Zivildienst steuerfrei → nicht angeben
- **Beachten:** Bescheinigung über die Bezüge beilegen
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0007.md) `tg-form-01-2026__c0007` – «3.3 Erwerbsausfallentschädigungen»
  - [WL TG 2026 S. 18](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0076.md) `tg-wl-2026__c0076` – «Diese Entschädigungen sind insoweit anzugeben, als sie im Lohnausweis von den Arbeitgebenden»

<a id="3-4-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.4 – Von Ausgleichskassen direkt ausbezahlte Familien-, Kinder- und Haushaltszulagen (Code 140)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Familienausgleichskasse
- **Rein:** Bescheinigung Familienausgleichskasse → direkt ausbezahlte Kinder-, Ausbildungs-, Haushalts-, Geburts-, Adoptionszulagen
- **Rechnen:** Σ 2026 direkt von der Ausgleichskasse ausbezahlte Zulagen (Selbständige, Nichterwerbstätige, Landwirtschaft)
- **Regel:** Nur direkt von der Ausgleichskasse ausbezahlte Zulagen (selbständig Erwerbende, Nichterwerbstätige, Landwirtschaft); im Lohnausweis enthaltene Kinderzulagen sind bereits im Nettolohn (Ziff. 1.1).
- **Beachten:** Über den Arbeitgeber bezahlte Kinderzulagen sind im Nettolohn (Ziff. 1.1) → nicht hier
- **Beachten:** Selbständige: nicht ins Geschäftsergebnis Ziff. 2 (nicht AHV-pflichtig)
- **Beachten:** Mit Kinderalimenten weitergeleitete Zulagen beim Empfänger in Ziff. 5.2
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0007.md) `tg-form-01-2026__c0007` – «3.4 Von Ausgleichskassen direkt ausbezahlte Familien-, Kinder- und Haushaltszulagen 140»
  - [WL TG 2026 S. 18–19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0077.md) `tg-wl-2026__c0077` – «Deklarieren Sie hier von der Ausgleichskasse direkt ausbezahlte Familien- und Haushaltszulagen.»
  - [WL TG 2026 S. 15–16](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0061.md) `tg-wl-2026__c0061` – «Direkt ausbezahlte Familienzulagen sind nicht AHV-pflichtig.»
  - [WL TG 2026 S. 13](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0049.md) `tg-wl-2026__c0049` – «Teuerungs-, Ferien- und Kinderzulagen»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0079.md) `tg-wl-2026__c0079` – «Periodische Unterhaltsbeiträge (inklusive Kinderzulagen)»

<a id="4-einkommen-wertschriften"></a>
### Ziff. 4 – Wertschriften- und Zinserträge sowie Gewinne aus Geldspielen (Formular 1 Code 150, Übertrag aus Formular 2)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Formular 2 Total steuerbarer Ertrag (Ziff. 9)
- **Rein:** Steuerauszug Bank/Depot → Formular 2: Steuerwerte, Erträge Spalte 8/A (mit VSt) bzw. 9/B (ohne VSt) · Zinsausweise/Kontoauszüge → Bruttozinsen (über Fr. 200/Jahr mit VSt) · Gutschriftsanzeigen ausländischer Dividenden → Nettobetrag + rückforderbare Quellensteuer; DA-1 · Lotterie-Auszahlungsbescheinigung (Original) bzw. Postanweisungsabschnitt → Geldspielgewinne
- **Rechnen:** Form. 2 Ziff. 9 = Ziff. 5 (Bruttoerträge A+B) − Ziff. 6 Geschäftsanteil − Ziff. 7 Verwaltung (2 ‰ Steuerwert fremdverwaltet, max. Fr. 6'000) − Ziff. 8 Einsatzkosten
- **Regel:** Erträge zuerst im Wertschriften- und Guthabenverzeichnis (Formular 2) erfassen, das Total steuerbarer Ertrag aus Ziff. 9 übertragen. Auch steuerbare Geldspielgewinne hier (nicht unter Ziff. 5).
- **Beachten:** Freigrenze Verkaufsförderung Fr. 1'000 / Bund Fr. 1'100; Freibetrag BGS-Grossspiele Fr. 1'000'000 / Bund Fr. 1'071'000
- **Beachten:** Ausland voll steuerbar; Einsatz 5 %/Gewinn, max. Fr. 5'000 / Bund Fr. 5'400 (Online-Casino Fr. 25'000 / Bund Fr. 26'800)
- **Beachten:** Kinder-Wertschriften: Jg. 2009+ bei Eltern; Jg. 2008 deklariert 2026 selbst (WL S. 6) – WL S. 30 nennt «2008 und jünger»
- **Limiten:**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'000 (Einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsfoerderung bis Fr. 1'000 steuerfrei; wird die Grenze ueberschritten, ist der gesamte Gewinn steuerbar. Auslaendische Lotterien voll steuerbar. Bund: Freigrenze Fr. 1'100.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (Art. 1 Abs. 2 lit. d und e BGS) steuerfrei, sofern die Grenze von CHF 1'100 nicht überschritten wird. Gewinne aus Kleinspielen (BGS) sind steuerfrei.)**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'000'000 (Einzelne Gewinne aus BGS-Grossspielen und Online-Spielbankenspielen bis Fr. 1'000'000 steuerfrei; nur der Mehrbetrag ist steuerbar (Bund: Fr. 1'071'000). Kleinspiele nach BGS vollstaendig steuerfrei.)** · Bund **CHF 1'071'000 (Einzelne Gewinne aus nach BGS zugelassenen Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'071'000; darüber steuerbar (abzüglich Einsatzkosten nach Art. 33 Abs. 4 DBG).)**
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «4. Wertschriften- und Zinserträge sowie Gewinne aus Geldspielen Formular 2 150»
  - [WL TG 2026 S. 18–19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0077.md) `tg-wl-2026__c0077` – «Wertschriften- und Gut-»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0162.md) `tg-wl-2026__c0162` – «den Geschäftsanteil am Vermögensertrag von Ziffer 6, die Vermögensverwaltungskosten von Zif»
  - [WL TG 2026 S. 33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0158.md) `tg-wl-2026__c0158` – «Der Pauschalabzug beträgt maximal Fr. 6'000.»
  - [Kurz-WL TG 2026 S. 1](../../chunks/tg/2026/tg-wl-kurz-2026/tg-wl-kurz-2026__c0001.md) `tg-wl-kurz-2026__c0001` – «2.0 ‰ auf fremdverwalteten Wertschriften und Kapitalanlagen max. Fr. 6 000»
  - [WL TG 2026 S. 32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0150.md) `tg-wl-2026__c0150` – «soweit die Brutto- zinsen im Kalenderjahr Fr. 200 übersteigen»
  - [WL TG 2026 S. 31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0146.md) `tg-wl-2026__c0146` – «Bei der direkten Bundessteuer beträgt die Steuerfreigrenze Fr. 1'100.»
  - [WL TG 2026 S. 31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0147.md) `tg-wl-2026__c0147` – «zum Betrag von Fr. 1'000'000 bei den Staats- und Gemeindesteuern und Fr. 1'071'000 bei der di»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0160.md) `tg-wl-2026__c0160` – «Bei den Staats- und Gemeindesteuern beträgt der Ma- ximalabzug pro Gewinn Fr. 5'000 und bei der direkten Bundessteuer Fr. 5'400.»
  - [WL TG 2026 S. 30](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0140.md) `tg-wl-2026__c0140` – «Ebenfalls zu deklarieren sind Vermögen und Erträge von Kindern unter Ihrer elterlichen Sorge (Jahrgang 2008 und jünger).»
  - [WL TG 2026 S. 33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0154.md) `tg-wl-2026__c0154` – «zuzüglich ausländischer Quellensteuern, soweit sie aufgrund eines Dop»
  - [WL TG 2026 S. 6](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0012.md) `tg-wl-2026__c0012` – «Personen mit Jahrgang 2008 sind somit für die Steuerperiode 2026 erstmals selbständig deklarationspflichtig.»
  - [WL TG 2026 S. 27–28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0128.md) `tg-wl-2026__c0128` – «für jedes nicht selbständig besteuerte Kind (Jahrgang 2009 und jünger)»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0161.md) `tg-wl-2026__c0161` – «Staats- und Gemeindesteuern Fr. 25'000 und bei der direkten Bundessteuer Fr. 26'800.»
  - [WL TG 2026 S. 31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0147.md) `tg-wl-2026__c0147` – «Solche Gewinne sind unabhängig des Betrags vollumfänglich steuerbar.»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0160.md) `tg-wl-2026__c0160` – «Von jedem einzelnen steuerbaren Gewinn können pauschal fünf Pro- zent als Einsatzkosten abgezogen werden.»
  - [WL TG 2026 S. 32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0151.md) `tg-wl-2026__c0151` – «Legen Sie bei den Lotterietreffern aller Art die Auszahlungsbescheinigung im Original bzw. den Postanweisungsabschnitt bei.»
  - [WL TG 2026 S. 33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0158.md) `tg-wl-2026__c0158` – «pauschal 2 Promille des Steuerwertes der durch Dritte verwalteten Wertschriften des Privatvermögens»

<a id="5-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.1 – Unterhaltsbeiträge von Ehefrau/-mann bzw. Partner/in bei Trennung/Scheidung (Code 160)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Urteil/Vereinbarung, Zahlungsnachweise; Name und Adresse der zahlenden Person
- **Rein:** Scheidungs-/Trennungsurteil bzw. -vereinbarung → vereinbarter Unterhaltsbeitrag für eigene Person · Kontoauszüge/Zahlungsbelege → 2026 erhaltene Beträge · Vereinbarung Überlassung Liegenschaftsanteil → Mietwertanteil
- **Rechnen:** Σ 2026 erhaltene periodische Unterhaltsbeiträge für sich + Mietwertanteil aus überlassenem Liegenschaftsanteil
- **Regel:** Periodische Unterhaltsbeiträge für die eigene Person sind steuerbar (inkl. Mietwertanteil bei Überlassung eines Liegenschaftsanteils). Name/Adresse der zahlenden Person auf der Zeile unter Ziff. 5.1 angeben.
- **Beachten:** Name und Adresse der zahlenden Person auf der Zeile unter Ziff. 5.1 angeben
- **Beachten:** Spiegelbild: zahlende Person zieht in Ziff. 12.1 ab (nur mit Zahlungsnachweis)
- **Beachten:** Kinderalimente separat in Ziff. 5.2
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «5.1 Unterhaltsbeiträge von Ehefrau/-mann bzw. Partnerin/Partner bei Trennung/Scheidung/Auflösung Partnerschaft»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0078.md) `tg-wl-2026__c0078` – «Steuerbar sind periodische Unterhaltsbeiträge der Ehefrau oder des Ehemanns bzw. der Partne-»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0086.md) `tg-wl-2026__c0086` – «Abziehbar sind die tatsächlich bezahlten periodischen Unterhaltsbeiträge»

<a id="5-2-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.2 – Unterhaltsbeiträge für minderjährige Kinder (Code 162)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Urteil/Vereinbarung, Zahlungsnachweise; Name und Adresse der zahlenden Person
- **Rein:** Urteil/Unterhaltsvertrag → Kinderunterhaltsbeitrag inkl. Kinderzulagen · Kontoauszüge → 2026 tatsächlich eingegangene Beträge · Bestätigung Gemeinde → Alimentenbevorschussung
- **Rechnen:** Σ 2026 tatsächlich erhaltene Kinderalimente inkl. Kinderzulagen je minderjähriges Kind, bis und mit Monat der Volljährigkeit
- **Regel:** Periodische Beiträge inkl. Kinderzulagen für Kinder unter elterlicher Sorge sind steuerbar. Bei unregelmässigen Zahlungen die 2026 tatsächlich überwiesenen Beträge; Alimentenbevorschussung vermerken. Ab dem Folgemonat der Volljährigkeit nicht mehr steuerbar.
- **Beachten:** Empfangender Elternteil erhält den kantonalen Kinderabzug; zahlender Elternteil zieht in Ziff. 12.2 ab
- **Beachten:** Unregelmässige/ausbleibende Zahlungen: nur effektiv 2026 überwiesene Beträge; Bevorschussung vermerken
- **Beachten:** Name und Adresse der zahlenden Person angeben (Zeile unter Ziff. 5.1)
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «5.2 Unterhaltsbeiträge für minderjährige Kinder»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0079.md) `tg-wl-2026__c0079` – «Ab dem Folgemonat der Volljährigkeit des Kindes sind die Un-»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0108.md) `tg-wl-2026__c0108` – «Der Kinderabzug steht nur dem die zu versteuernden Unterhaltsbeiträge (Alimente)»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0087.md) `tg-wl-2026__c0087` – «Kinder überwiesenen Kinderunterhaltsbeiträge (inkl. Kinderzulagen) ein.»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0079.md) `tg-wl-2026__c0079` – «sind die tatsächlich im Jahr 2026 überwiesenen Beträge anzu-»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0079.md) `tg-wl-2026__c0079` – «kann die Zeile direkt unterhalb der Ziffer 5.1 verwendet werden.»

<a id="5-3-einkommen-erbschaften-unverteilt"></a>
### Ziff. 5.3 – Ertrag aus unverteilten Erbschaften (Formular 3, Code 164)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung der Erbengemeinschaft/Formular 3
- **Rein:** Formular 3 / Abrechnung Erbengemeinschaft → Erträge der Erbschaft, Erbquote · Todesschein/Erbbescheinigung → Todestag, Erbquote
- **Rechnen:** Erträge der unverteilten Erbschaft ab Folgetag des Todestags × eigene Erbquote
- **Regel:** Einkünfte anteilig nach Erbquote; gleiches gilt für das Vermögen (Ziff. 30.5). Steuerpflicht für die Anteile beginnt am Folgetag des Todestags der erblassenden Person.
- **Beachten:** Vermögensanteil nach Erbquote in Ziff. 30.5; Erbanfall zusätzlich S. 4 unten (Vermögensanfälle) angeben
- **Beachten:** Liegenschaft im Nachlass: Ertrags-/Vermögensanteil in Formular 7, Schuldzinsanteil im Schuldenverzeichnis (Form. 4.1)
- **Beachten:** VSt: belastete Erbschaftserträge nach Erbquote in Form. 2 Spalte A, Rückforderung im Wohnsitzkanton
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «5.3 Ertrag aus unverteilten Erbschaften Formular 3 164»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0080.md) `tg-wl-2026__c0080` – «Einkünfte aus unverteilten Erbschaften werden den erbenden Personen entsprechend ihrer»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0129.md) `tg-wl-2026__c0129` – «Bitte führen Sie hier auch Vermögensanfälle aus Erbschaften auf.»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0167.md) `tg-wl-2026__c0167` – «unverteilten Erbschaft sind im Umfang der Erbquote in der Spalte A»
  - [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0050.md) `tg-info-faq__c0050` – «Sofern sich eine Liegenschaft im Nachlass befindet, sind die Vermögens- und Ertragsanteile daran separat im Formular 7»
  - [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0050.md) `tg-info-faq__c0050` – «Allfällige Hypothekar- und Schuldzinsanteile auf der betreffenden Liegenschaft sind diesfalls separat im Formular 4»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0167.md) `tg-wl-2026__c0167` – «Erbinnen und Erben haben die Verrechnungssteuer auf ihren Erbschaftserträgen in ihrem Wohn-»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0085.md) `tg-wl-2026__c0085` – «Deklarieren Sie im Formular 4.1»

<a id="5-4-einkommen-uebrige"></a>
### Ziff. 5.4 – Weitere Einkünfte (Urheberrechte, Lizenzen, Patente, Nutzniessung, Wohnrecht, Lidlohn; Code 168)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung/Vertrag; nähere Bezeichnung auf der Zeile
- **Rein:** Lizenz-/Urheberrechtsabrechnung → Erträge · Nutzniessungs-/Wohnrechtsvertrag → Erträge bzw. Marktmiete vergleichbarer Wohnung · Untermietvertrag + eigene Mietzins-/NK-Abrechnung → Nettoertrag Untermiete · Vereinbarung Konkurrenzverbot/Rechtsverzicht, Lidlohn → Entschädigung
- **Rechnen:** Σ Lizenz-/Urheber-/Nutzniessungserträge + Wohnrecht (Marktmiete) + Untermiete netto (− Mietzins-/NK-Anteil) + Lidlohn/Verzichtsentschädigungen
- **Regel:** Wohnrecht mit dem Mietwert einer vergleichbaren Wohnung bewerten; Untervermietung netto (nach Abzug Mietzinsanteil und Nebenkosten); Lidlöhne, Entschädigungen für Konkurrenzverbot/Rechtsverzicht. Steuerpflichtige Geldspielgewinne gehören dagegen in Ziff. 4.
- **Beachten:** Geldspielgewinne → Ziff. 4 (Formular 2), nicht hier
- **Beachten:** Lidlohn als Kapitalabfindung für mehrere Jahre → Ziff. 5.5 mit Anzahl Jahre
- **Beachten:** Nutzniessungsvermögen selbst beim Nutzniesser quotenmässig in Ziff. 30.5
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «5.4 Weitere Einkünfte (z.B. Urheberrechte, Lizenzen, Patente, Wohnrecht usw.)»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0081.md) `tg-wl-2026__c0081` – «Ebenfalls hier anzugeben sind Einkünfte aus Nutzniessung und unentgeltlichem Wohn-»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0082.md) `tg-wl-2026__c0082` – «Wertschriftenertrag und Ertrag aus Guthaben sowie Gewinne aus Geldspielen»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0083.md) `tg-wl-2026__c0083` – «Lidlohnansprüche für geleistete Arbeit etc.)»
  - [WL TG 2026 S. 26–27](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0123.md) `tg-wl-2026__c0123` – «Die Anteile an unverteilten Erbschaften und Nutzniessungen werden den einzelnen erbenden oder»

<a id="5-5-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 5.5 – Kapitalabfindung für wiederkehrende Leistungen für … Jahre (Code 170)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung/Vertrag; Zeitraum in Jahren angeben
- **Rein:** Abfindungsvereinbarung/Bescheinigung (z.B. Rentenrückkauf, Lidlohnanspruch) → Betrag + Anzahl Jahre
- **Rechnen:** Betrag in Ziff. 5.5; Satz: übrige Einkünfte + Abfindung ÷ Anzahl Jahre (= jährliche Leistung); lebenslängliche Leistung: Rentenwerttabelle
- **Regel:** Z.B. Rentenrückkauf, Lidlohnansprüche: Zeitraum angeben, für den die Abfindung ausgerichtet wird (Besteuerung zum Satz einer entsprechenden jährlichen Leistung). Kapitalleistungen aus Vorsorge gehören NICHT hierher, sondern auf Seite 4 unten.
- **Beachten:** Anzahl Jahre zwingend angeben (Grundlage der Satzbestimmung)
- **Beachten:** Vorsorgekapital → S. 4 unten: Kanton einfache Steuer 2 % gemeinsam / 2,4 % allein; Bund ein Fünftel des Tarifs
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «5.5 Kapitalabfindung für wiederkehrende Leistungen für Jahre 170»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0083.md) `tg-wl-2026__c0083` – «Nicht in Ziffer 5.5, sondern auf der Steuererklärung, Seite 4 unten, sind Kapitalleistungen aus Vor-»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0131.md) `tg-wl-2026__c0131` – «bei gemeinsam besteuerten Personen zu einem einheitlichen Satz von 2% besteuert.»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0131.md) `tg-wl-2026__c0131` – «Bei Alleinstehenden beträgt der einheitliche Satz für die einfache Steuer 2,4%.»
  - [DBG Art. 38](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-38.md) `bund-dbg-2026__art-38` – «Sie wird zu einem Fünftel der Tarife nach Artikel 36»

<a id="6-berechnung-total"></a>
### Ziff. 6 – Zwischentotal der Einkünfte (Code 175)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 1 bis 5.5)
- **Rein:** Übertrag aus Ziff. 1.1 bis 5.5 (Seite 2)
- **Rechnen:** Σ Ziff. 1.1 bis 5.5 (ohne Ziff. 1.3); negativ mit «–» → ohne Liegenschaften direkt in Ziff. 20, sonst Ziff. 7
- **Regel:** Summe der Ziffern 1 bis 5.5; negatives Ergebnis mit Minuszeichen. Ohne Liegenschaften (und ohne Einkommen aus Geschäftsfahrzeug-Besitz) direkt in Ziff. 20 übertragen, sonst über Ziff. 7 und 8 zu Ziff. 9.
- **Beachten:** WL spricht von Ziff. 6.1/6.2; Formular 2026 hat nur Ziff. 6 (Code 175) und Ziff. 7
- **Beachten:** Geschäftsfahrzeug: keine Aufrechnung Arbeitsweg (Privatanteil 0.9 %/Monat inkl. Arbeitsweg), dafür kein Fahrkostenabzug
- **Bemerkung:** Die Wegleitung spricht von «Ziffer 6.1/6.2»; das Formular 1 (2026) enthält nur Ziff. 6 (Code 175), 7 und 8.1 – Abweichung Wegleitungstext vs. Formular beachten.
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «6. Zwischentotal der Einkünfte 175»
  - [WL TG 2026 S. 19–20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0084.md) `tg-wl-2026__c0084` – «Zwischentotal der Einkünfte»
  - [WL TG 2026 S. 14](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0052.md) `tg-wl-2026__c0052` – «Diese Löhne werden nicht in die Berechnung des Zwischentotals unter Ziffer 6 miteinbezogen.»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0175.md) `tg-wl-2026__c0175` – «erfolgt keine Aufrechnung»

<a id="7-berechnung-total"></a>
### Ziff. 7 – Übertrag von Ziffer 6 (Staatssteuer / Bundessteuer)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rechnen:** Ziff. 7 Staat = Bund = Ziff. 6; Ziff. 9 (Code 198) = Ziff. 7 + Ziff. 8.1 je Spalte → Seite 3 Ziff. 20
- **Regel:** Übertrag des Zwischentotals Ziff. 6 in beide Spalten (Staat/Bund), falls Liegenschaften vorhanden.
- **Beachten:** Nur nötig bei Liegenschaften; sonst Ziff. 6 direkt in Ziff. 20
- **Beachten:** Ab hier getrennte Spalten Staat/Bund (Selbstnutzungsabzug Kanton 40 % / Bund 20 %)
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **40 % (Selbstnutzungsabzug: 40 % vom Mietwert fuer am Wohnsitz selbstgenutztes Wohneigentum (Bund: 20 %, tg-wl-2026__c0222). Kein Abzug bei Zweit-/Ferienwohnungen, landwirtschaftlichen Liegenschaften, an Nahestehende ueberlassenen Objekten.)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0009.md) `tg-form-01-2026__c0009` – «7. Übertrag von Ziffer 6»
  - [WL TG 2026 S. 19–20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0084.md) `tg-wl-2026__c0084` – «Danach füllen Sie die Ziffern 7 und/oder 8 aus.»
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0009.md) `tg-form-01-2026__c0009` – «9. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 20»
  - [WL TG 2026 S. 51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0240.md) `tg-wl-2026__c0240` – «kantonal einen Abzug von 40% und beim Bund von 20% vornehmen»

<a id="8-1-einkommen-liegenschaften-mietertrag"></a>
### Ziff. 8.1 – Einkünfte aus Liegenschaften (Formular 7, Code 180)

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Formular 7 Total Nettoerfolge (Spalte Staatssteuer / Bundessteuer)
- **Rein:** Formular 7 → Total Nettoerfolge (Code 180) Spalte Staat / Bund · Liegenschaftensteuerrechnung 2027 / Liegenschaftenschätzung → indexierter Mietwert selbstgenutzt · Mietverträge/Mietzinsabrechnung, PV-Einspeisevergütung → Miet-/Pachtzinsen, weitere Erträge · Unterhaltsrechnungen, STWEG-Abrechnung → Formular 8 (effektive Kosten)
- **Rechnen:** Je Liegenschaft: Mietwert − Selbstnutzungsabzug (Kanton 40 % / Bund 20 %) + Mieterträge = Bruttoertrag − Unterhalt (Pauschale/effektiv) = Nettoerfolg; Σ
- **Regel:** Total Nettoerfolge aus Formular 7 (Eigenmietwert und Mieterträge abzüglich Unterhalts- und Betriebskosten) getrennt für Staats- und Bundessteuer übertragen (Eigenmietwert-Abzug 40% Kanton / 20% Bund führt zu unterschiedlichen Beträgen).
- **Beachten:** Pauschale je Liegenschaft/Jahr wählbar: 10 % (Gebäude ≤ 10 J.) / 20 % (älter); nicht für Geschäftsliegenschaften
- **Beachten:** Altersstichtag Pauschale: Kanton (WL TG) Ende Steuerperiode / Bund (Art. 5 LKV) Beginn – bei Alter um 10 J. prüfen
- **Beachten:** Kein Selbstnutzungsabzug: Zweit-/Ferienwohnung, Landwirtschaft, Überlassung an Nahestehende; Belege ab Fr. 1'000
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **40 % (Selbstnutzungsabzug: 40 % vom Mietwert fuer am Wohnsitz selbstgenutztes Wohneigentum (Bund: 20 %, tg-wl-2026__c0222). Kein Abzug bei Zweit-/Ferienwohnungen, landwirtschaftlichen Liegenschaften, an Nahestehende ueberlassenen Objekten.)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Pauschalabzug Liegenschaftsunterhalt: 10 % des Bruttomietertrags bzw. (Eigen-)Mietwerts fuer Gebaeude bis 10 Jahre alt (Ende Steuerperiode); wahlweise statt effektiver Kosten, je Liegenschaft und Periode.)** · Bund **10 % (Pauschalabzug Liegenschaftskosten (anstelle effektiver Kosten, Wahl pro Periode und Liegenschaft): 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist.)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt: 20 % fuer Gebaeude, die ueber 10 Jahre alt sind.)** · Bund **20 % (Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist.)**
- **Bund:** Nettoerfolg einzeln pro Ebene (Selbstnutzungsabzug 40% Kanton / 20% Bund).
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0009.md) `tg-form-01-2026__c0009` – «8.1 Einkünfte aus Liegenschaften Formular 7 180»
  - [WL TG 2026 S. 51–52](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0242.md) `tg-wl-2026__c0242` – «Total der Nettoerfolge der Spalte Staatssteuer und Bundessteuer in die»
  - [WL TG 2026 S. 51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0240.md) `tg-wl-2026__c0240` – «kantonal einen Abzug von 40% und beim Bund von 20% vornehmen»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0235.md) `tg-wl-2026__c0235` – «10% für Gebäude, die am Ende der Steuerperiode bis zu zehn Jahre alt sind;»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0235.md) `tg-wl-2026__c0235` – «20% für Gebäude, die am Ende der Steuerperiode älter als zehn Jahre sind.»
  - [WL TG 2026 S. 51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0241.md) `tg-wl-2026__c0241` – «Die Summe der steuerbaren Eigenmietwerte und der Miet- und Pachtzinserträge»
  - [WL TG 2026 S. 49](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0231.md) `tg-wl-2026__c0231` – «Für Einzelbeträge ab Fr. 1'000 legen Sie der Steuererklärung bitte die Rechnungskopien»
  - [WL TG 2026 S. 51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0240.md) `tg-wl-2026__c0240` – «von Zweit- und Ferienwohnungen sowie von unentgeltlich oder unterpreislich an»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0221.md) `tg-wl-2026__c0221` – «Die Mietwerte aus Selbstnutzung werden jährlich indexiert.»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0221.md) `tg-wl-2026__c0221` – «Der indexierte Mietwert für die Steuerperiode 2026 ist in der Regel aus Ihrer Liegenschaften-»

<a id="9-berechnung-total"></a>
### Ziff. 9 – Total der Einkünfte (Code 198) – Übertrag auf Seite 3, Ziffer 20

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag aus Ziff. 7 (= Zwischentotal Ziff. 6, Code 175) · Formular 7 Liegenschaften → Ziff. 8.1 (Code 180)
- **Rechnen:** Code 198 = Ziff. 7 + Ziff. 8.1, je Spalte Staat / Bund → Übertrag in Ziff. 20
- **Regel:** Summe Ziff. 7 + 8 je Spalte (Staat/Bund); Übertrag in Ziff. 20.
- **Beachten:** Ohne Liegenschaften: Ziff. 6 direkt in Ziff. 20 übertragen (Formular: «Ziffer 6 oder 9»)
- **Beachten:** WL nennt Ziff. 6.1/6.2, Formular nur Ziff. 6 (Code 175) und 7 – im Original prüfen
- **Quellen:**
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0009.md) `tg-form-01-2026__c0009` – «9. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 20 198»
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «6. Zwischentotal der Einkünfte 175»
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0009.md) `tg-form-01-2026__c0009` – «8.1 Einkünfte aus Liegenschaften Formular 7 180»
  - [WL TG 2026 S. 19–20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0084.md) `tg-wl-2026__c0084` – «Total in Ziffer 6.1 (Summe der Ziffern 1 bis 5.5) direkt in Ziffer 20, Seite 3 der Steuererklärung.»
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «20. Total der Einkünfte, Übertrag von Seite 2 (Ziffer 6 oder 9)»

## Abzüge

<a id="10-1-10-2-berechnung-total"></a>
### Ziff. 10.1 / 10.2 – Berufsauslagen bei unselbständiger Erwerbstätigkeit – Person 1 (Formular 4.2, Code 240) / Person 2 (Formular 4.3, Code 280)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Form. 4.2 bzw. 4.3 Ziff. 7 Total der abzugsfähigen Berufsauslagen
- **Rein:** Formular 4.2 (Person 1) / 4.3 (Person 2) → Ziff. 7 Total (Code 240 / 280) · Lohnausweis → Ziff. 11 Nettolohn (Basis 3%-Pauschale Ziff. 4) · ÖV-Abo-Belege → Ziff. 2.1; Privatfahrzeug: Distanz Wohnadresse–Fahrzeugstandort, km/Tag × Tage → Ziff. 2.3 · AG-Bescheinigung Schichttage (falls nicht im Lohnausweis) → Ziff. 3.1
- **Rechnen:** Ziff. 7 = Σ 2.5–6 je Spalte; 2.5 = min(2.4; Kanton 6'000 / Bund 3'300); 3.1 = 15/Tag ≤ 3'200 (3.2: 7.50 ≤ 1'600); 4 = 3% × Nettolohn, min. 2'000, max. 4'000
- **Regel:** Total Ziff. 7 des Hilfsblatts in die linke Spalte (Staatssteuer) und rechte Spalte (Bundessteuer) übertragen; die Beträge können sich unterscheiden (Fahrkostenmaximum, Autoansatz).
- **Beachten:** Auto nur ausnahmsweise (ÖV unzumutbar): Kanton Fr. -.60/-.50/-.40 je km gestaffelt, Bund Fr. -.75/km → Spalten getrennt
- **Beachten:** Geschäftsfahrzeug für Arbeitsweg (Ziff. 1.2): kein Fahrkostenabzug, keine Aufrechnung (Privatanteil inkl. Arbeitsweg)
- **Beachten:** Unterjährige Erwerbstätigkeit: Pauschalen × Tage/360; vom Arbeitgeber übernommene Kosten nicht abziehbar
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstaette (Staats- und Gemeindesteuern): Maximalabzug Fr. 6'000 pro Person gesamthaft (inkl. Fahrkosten Wochenaufenthalt und Nebenerwerb); wird bei unterjaehriger Steuerpflicht/Teilzeit nicht gekuerzt.)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **Privatauto (nur in begruendeten Ausnahmefaellen, wenn OeV nicht zur Verfuegung steht/unzumutbar): gestaffelter Ansatz je jaehrlich gefahrener Kilometer: bis 3'000 km Fr. 0.60, 3'001-5'000 km Fr. 0.50, ueber 5'000 km Fr. 0.40 pro km (Parkgebuehren inbegriffen). Beispiel 12'150 km = Fr. 5'660.** · Bund **CHF 0.75 (Privatauto: CHF 0.75 pro Fahrkilometer, nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist; Gesamtmaximum CHF 3'300.)**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswaertige Verpflegung bei taeglicher Heimkehr: Fr. 15 pro auswaertige Hauptmahlzeit (in der Regel nur Mittagessen), wenn Heimkehr am Mittag wegen grosser Entfernung oder sehr kurzer Essenspause nicht zumutbar.)** · Bund **CHF 15 (Auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (in der Regel nur Mittagessen), nur Pauschale zulässig, wenn Hauptmahlzeit wegen grosser Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann oder bei durchgehender Schicht-/Nachtarbeit.)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei staendiger auswaertiger Verpflegung maximal Fr. 3'200 im Jahr; bei Teilzeit/Nebenberuf angemessene Kuerzung.)** · Bund **CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **3 % (Pauschale übrige Berufskosten (Form. 4.2 Ziff. 4: Berufswerkzeuge, Fachliteratur, Kleider-/Schuhverschleiss, Mehrauslagen für Schwerarbeit, Beiträge an Berufsverbände/Gewerkschaften): 3 % des Nettolohns (Ziff. 11 Lohnausweis), min. Fr. 2'000, max. Fr. 4'000 (Kanton und dBSt). Anstelle der Pauschale können die notwendigen tatsächlichen Aufwendungen nachgewiesen werden (keine Kumulation mit der Pauschale). Bei weniger als 12 Monaten unselbständiger Erwerbstätigkeit anteilmässig gekürzt.)** · Bund **3 % (Übrige Berufskosten (Art. 26 Abs. 1 lit. c DBG): Pauschale 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; anstelle der Pauschale ist der Nachweis höherer tatsächlicher übriger Berufskosten möglich. Fahrkosten (lit. a, max. 3'300) und Verpflegung (lit. b) werden zusätzlich abgezogen. Bei Teilzeit/Teiljahr angemessen kürzen.)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **CHF 2'000 (Pauschale uebrige Berufskosten: Minimum Fr. 2'000.)** · Bund **CHF 2'000 (Mindestbetrag der Pauschale übrige Berufskosten.)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 4'000 (Pauschale uebrige Berufskosten: Maximum Fr. 4'000.)** · Bund **CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Bei Verbilligung durch Arbeitgeber (Gutscheine, Kantine, Personalrestaurant) nur der halbe Abzug: Fr. 7.50 pro Tag. Kein Abzug, wenn Hauptmahlzeit unter Fr. 10 zu stehen kommt.)** · Bund **CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei Verbilligung durch Arbeitgeber: halber Abzug, maximal Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)**
- **Bund:** Rechte Spalte Bund: eigene Fahrkostenberechnung (Fr. 3'300 max.).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «10.1 Person 1 Formular 4.2 240»
  - [WL TG 2026 S. 41–42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0195.md) `tg-wl-2026__c0195` – «übertragen Sie diesen Betrag auf Seite 3 der Steuererklärung in die Ziffer 10.1»
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0002.md) `tg-form-04-2-2026__c0002` – «2.5 Total abzugsfähige Fahrkosten (Übertrag von Ziffer 2.4, aber Staat max. Fr. 6000.– / Bund max. Fr. 3300.–)»
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0003.md) `tg-form-04-2-2026__c0003` – «pro Arbeitstag Fr. 15.– / max. Fr. 3200.– pro Jahr»
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0004.md) `tg-form-04-2-2026__c0004` – «3% vom Nettolohn, mindestens jedoch Fr. 2000.– und höchstens Fr. 4000.–»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0187.md) `tg-wl-2026__c0187` – «Pauschalabzug von 3% vom Nettolohn gemäss Ziffer 11 des Lohnausweises»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0180.md) `tg-wl-2026__c0180` – «Bei der direkten Bundessteuer beträgt der Ansatz einheitlich Fr. -.75 pro gefahrenen Kilometer.»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0179.md) `tg-wl-2026__c0179` – «können Sie keine Fahrtkosten geltend machen (vgl. Ziff. 1.2).»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0174.md) `tg-wl-2026__c0174` – «Beispiel unterjährige Erwerbstätigkeit: Dauer von 01.04.2026 bis 31.12.2026 (Dauer 270 Tage)»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0173.md) `tg-wl-2026__c0173` – «Kein Abzug ist zulässig für Kosten, die Arbeitgebende übernommen haben.»
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0005.md) `tg-form-04-2-2026__c0005` – «7. Total der abzugsfähigen Berufsauslagen 240»
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0003.md) `tg-form-04-2-2026__c0003` – «pro Arbeitstag Fr. 7.50 / max. Fr. 1600.– pro Jahr»
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0002.md) `tg-form-04-2-2026__c0002` – «2.1 Abonnementskosten für öffentliche Verkehrsmittel 206»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0178.md) `tg-wl-2026__c0178` – «Die Kosten der Benützung von privaten Motorfahrzeugen können Sie nur in Ausnahmefällen»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0178.md) `tg-wl-2026__c0178` – «geben Sie die genaue Distanz zwischen der Wohnadresse und dem Standort des Fahrzeugs am Arbeitsort»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0184.md) `tg-wl-2026__c0184` – «ist nachzuweisen (Bescheinigung der Arbeitgebenden), sofern diese im»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0175.md) `tg-wl-2026__c0175` – «im Lohn berücksichtigt ist, erfolgt keine Aufrechnung.»

<a id="11-abzug-schuldzinsen"></a>
### Ziff. 11 – Schuldzinsen (Formular 4.1, Code 290)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 4.1 Total fällige Schuldzinsen (Zusammenzug C, Code 290)
- **Rein:** Hypothekar-/Kredit-/Darlehensbestätigung → 2026 fällige Zinsen, Gläubiger/in mit Adresse, Zinssatz, Schuld 31.12. · Formular 4.1 → Zusammenzug C Code 290 (= privat Code 286 + Geschäft Code 288) · Steuer-Schlussrechnung → 2026 belastete negative Ausgleichszinsen / Verzugszinsen
- **Rechnen:** Code 290 = Code 286 + Code 288; privat abziehbar min(Code 286; Vermögenserträge bewegl./unbewegl. + 50'000); Kanton = Bund
- **Regel:** Nur 2026 fällig gewordene Zinsen (keine Ratazinsen); mit der Schlussrechnung belastete Ausgleichszinsen abziehbar; WEF-Zusatzverbilligungen mindern die Schuldzinsen. Private Schuldzinsen höchstens im Umfang der deklarierten Erträge aus beweglichem und unbeweglichem Vermögen plus Fr. 50'000. Amortisationen, Baukreditzinsen, Leasingzinsen nicht abziehbar.
- **Beachten:** Nur 2026 fällig gewordene Zinsen (keine Ratazinsen); WEF-Zusatzverbilligungen als Schuldzinsminderung
- **Beachten:** Geschäftsschuldzinsen nur, soweit nicht schon in Ziff. 2 (selbständige Erwerbstätigkeit) abgezogen
- **Beachten:** Baurechtszinsen nur bei Fremdvermietung; Amortisationen, Bau-/Landkreditzinsen (Bauphase), Leasingzinsen nicht
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «11. Schuldzinsen Formular 4.1 290»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «Sie können private Schuldzinsen höchstens im Umfang der deklarierten Erträge aus beweglichem»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «und unbeweglichem Vermögen und weiterer Fr. 50 000 in Abzug bringen.»
  - [Formular 4.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-1-2026/tg-form-04-1-2026__c0003.md) `tg-form-04-1-2026__c0003` – «Total Privat- und Geschäftsschulden 466 290»
  - [Formular 4.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-1-2026/tg-form-04-1-2026__c0001.md) `tg-form-04-1-2026__c0001` – «Total Privatschulden 455 286»
  - [Formular 4.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-1-2026/tg-form-04-1-2026__c0002.md) `tg-form-04-1-2026__c0002` – «Total Geschäftsschulden 460 288»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0170.md) `tg-wl-2026__c0170` – «Tragen Sie nur die im Jahre 2026 fällig gewordenen Schuldzinsen ein (keine Ratazinsen).»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0170.md) `tg-wl-2026__c0170` – «Tragen Sie Schuldzinsen aus selbständiger Erwerbstätigkeit hier nur ein, sofern Sie diese nicht»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0170.md) `tg-wl-2026__c0170` – «Die im 2026 mit der Steuerschlussrechnung belasteten Ausgleichszinsen können Sie ebenfalls als»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «Bezahlte Baurechtszinsen sind nur bei Fremdvermietung der Liegenschaft»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t1.md) `bund-dbg-2026__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0169.md) `tg-wl-2026__c0169` – «Unerlässlich ist insbesondere die Angabe der Gläubigerin bzw. des Gläubigers»
  - [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0027.md) `tg-info-faq__c0027` – «Nachgewiesene Verzugszinsen sowie negative Ausgleichszinsen aus Steuerforderungen können als private Schuldzinsen abgezogen werden.»

<a id="12-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.1 – Unterhaltsbeiträge an Ehefrau/-mann bzw. Partner/in bei Trennung/Scheidung (Code 300)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise; Urteil/Trennungsvereinbarung bei erstmaliger Deklaration; Name/Adresse der empfangenden Person
- **Rein:** Zahlungsnachweise (Bank-/Postbelege) der bezahlten Unterhaltsbeiträge · Scheidungs-/Trennungsurteil bzw. Trennungsvereinbarung (Kopie bei erstmaliger Deklaration) · Name/Adresse Empfänger/in → Zeilen unter Ziff. 12
- **Rechnen:** Σ tatsächlich bezahlte periodische Unterhaltsbeiträge an (Ex-)Ehegatten/Partner/in (inkl. Mietwertanteil überlassener Liegenschaft); Kanton = Bund
- **Regel:** Nur tatsächlich bezahlte periodische Beiträge, nur mit Zahlungsnachweis. Name und Adresse der empfangenden Person auf den Zeilen unter Ziff. 12. Spiegelbild zu Ziff. 5.1 beim Empfänger.
- **Beachten:** Nicht abziehbar: güterrechtliche Leistungen, Kapitalabfindung statt Rente (nur periodische Beiträge)
- **Beachten:** Unterstützung von Verwandten (Eltern, Geschwister) nicht abziehbar
- **Beachten:** Empfänger/in versteuert spiegelbildlich in Ziff. 5.1 (Code 160)
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «12.1 Unterhaltsbeiträge an Ehefrau/-mann bzw. Partnerin/Partner»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0086.md) `tg-wl-2026__c0086` – «Die Abzüge für Unterhaltsbeiträge und Rentenleistungen werden nur gewährt, wenn Zahlungs-»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0086.md) `tg-wl-2026__c0086` – «auch der Mietwertanteil aus Überlassung eines Liegenschaftsanteils.»
  - [KS 30 S. 31](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0096.md) `bund-ks-30__c0096` – «Leistungen eines Ehegatten zur Erfüllung güterrechtlicher Forderungen stellen keine Unter- haltsbeiträge dar.»
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t2.md) `tg-stg__par-34-t2` – «nicht jedoch Leistungen in Erfüllung anderer familienrechtlicher Unterhalts- oder Unterstützungspflichten»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t1.md) `bund-dbg-2026__art-33-t1` – «die Unterhaltsbeiträge an den geschiedenen, gerichtlich oder tatsächlich getrennt lebenden Ehegatten»
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «5.1 Unterhaltsbeiträge von Ehefrau/-mann bzw. Partnerin/Partner bei Trennung/Scheidung/Auflösung Partnerschaft (Name, Adresse Zahler/in) 160»
  - [KS 30 S. 30–31](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0095.md) `bund-ks-30__c0095` – «kann der als Kapitalleistung gezahlte Betrag zum Unterhalt des»

<a id="12-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.2 – Unterhaltsbeiträge für minderjährige Kinder (Code 302)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise; Urteil/Vereinbarung
- **Rein:** Zahlungsnachweise der an den anderen Elternteil überwiesenen Kinderalimente · Urteil/Unterhaltsvereinbarung (Kopie bei erstmaliger Deklaration) · Name/Adresse Empfänger/in → Zeilen unter Ziff. 12
- **Rechnen:** Σ bezahlte Kinderunterhaltsbeiträge inkl. Kinderzulagen je Kind, bis und mit Monat der Mündigkeit; Kanton = Bund
- **Regel:** An den anderen Elternteil überwiesene Kinderunterhaltsbeiträge (inkl. Kinderzulagen) für Kinder unter dessen Sorge; längstens bis und mit dem Monat der Mündigkeit. Wer abzieht, hat kantonal keinen Anspruch auf den Kinderabzug.
- **Beachten:** Wer Kinderalimente abzieht, hat keinen Kinderabzug (Kanton; Bund gleiche Zuteilung bei Minderjährigen)
- **Beachten:** Unterhalt an volljährige Kinder: nicht abziehbar, beim Kind steuerfrei (Bund, ESTV-KS)
- **Beachten:** Empfänger/in versteuert spiegelbildlich in Ziff. 5.2 (Code 162)
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «12.2 Unterhaltsbeiträge für minderjährige Kinder 302»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0087.md) `tg-wl-2026__c0087` – «Tragen Sie in Ziffer 12.2 die dem andern Elternteil für die unter dessen elterlicher Sorge stehenden»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0108.md) `tg-wl-2026__c0108` – «Der die Alimente leistende Elternteil, welcher diese Unter-»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0111.md) `tg-wl-2026__c0111` – «Fliessen Unterhaltsbeiträge, gelten bei minderjährigen Kindern grundsätzlich die gleichen Zutei-»
  - [KS 30 S. 32](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0101.md) `bund-ks-30__c0101` – «Der leistende Elternteil kann die Unterhaltsbeiträge auch nicht mehr von seinem Einkommen absetzen.»
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «5.2 Unterhaltsbeiträge für minderjährige Kinder (Name, Adresse Zahler/in) 162»

<a id="12-3-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.3 – Rentenleistungen (Code 304)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rentenvertrag; Beiblatt mit Name/Adresse des Empfängers
- **Rein:** Leibrenten-/Verpfründungsvertrag (Kopie bei erstmaliger Deklaration) · Zahlungsnachweise der bezahlten Renten · Beiblatt: Name/Adresse Empfänger/in, Umfang der Leistungen
- **Rechnen:** Kanton: 40% × bezahlte Leibrenten (§ 34 StG TG) / Bund: Ertragsanteil nach Art. 22 Abs. 3 lit. c DBG × bezahlte Leibrenten
- **Regel:** Im Jahr 2026 bezahlte Leibrenten sind zu 40% abziehbar. Umfang der Leistungen auf Beiblatt mit Name/Adresse der empfangenden Person genau bezeichnen.
- **Beachten:** WL TG nennt pauschal 40%; DBG 2026 verweist für Bund auf variablen Ertragsanteil (Rendite-Formel) → Fachperson
- **Beachten:** Entgeltlich zugesicherte Rentenverpflichtung: Barwert als Schuld in Formular 4.1 (→ Ziff. 34)
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «12.3 Rentenleistungen 304»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0087.md) `tg-wl-2026__c0087` – «Im Jahr 2026 bezahlte Leibrenten können zu 40% vom Einkommen abgezogen werden.»
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t2.md) `tg-stg__par-34-t2` – «die dauernden Lasten sowie 40 Prozent der bezahlten Leibrenten;»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t1.md) `bund-dbg-2026__art-33-t1` – «die dauernden Lasten sowie der Ertragsanteil nach Artikel 22 Absatz 3 Buchstabe c der Leistungen aus Leibrenten- und aus Verpfründungsverträgen;»
  - [DBG Art. 22](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-22-t3.md) `bund-dbg-2026__art-22-t3` – «Bei Leistungen aus ausländischen Leibrentenversicherungen, aus Leibrenten- und aus Verpfründungsverträgen ist die Höhe der um 0,5 Prozentpunkte erhöhten annualisierten Rendite»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «Rentenverpflichtungen werden mit dem jeweiligen Barwert der Rente als Schuld berück-»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0169.md) `tg-wl-2026__c0169` – «Total der Schulden in Ziffer 34 auf Seite 4 der Steuererklärung.»

<a id="13-1-13-2-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.1 / 13.2 – Beiträge an Säule 3a – Person 1 (Code 314) / Person 2 (Code 315), mit Kästchen «Anschluss 2. Säule (PK)»

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → 3a-Bescheinigung der Bank/Versicherung (Einzahlungen 2026)
- **Rein:** 3a-Bescheinigung Bank/Versicherung → 2026 einbezahlte Beiträge je Person · Lohnausweis Ziff. 10.1 (ordentliche BVG-Beiträge) → Hinweis auf Anschluss 2. Säule (Kästchen) · Erwerbseinkommen Ziff. 1/2 je Person → Basis 20% (ohne 2. Säule)
- **Rechnen:** je Person: mit 2. Säule min(Einzahlung; 7'258) / ohne 2. Säule min(Einzahlung; 20% × Erwerbseinkommen; 36'288); Kanton = Bund
- **Regel:** Kästchen «Anschluss 2. Säule» ankreuzen, wenn einer Vorsorgeeinrichtung angeschlossen. Abzug nur mit AHV-pflichtigem Erwerbseinkommen 2026 und nur für die Person, auf die der Vorsorgevertrag lautet. Maximum 2026: mit 2. Säule Fr. 7'258; ohne 2. Säule 20% des Erwerbseinkommens, höchstens Fr. 36'288 (zugleich absolute Einzahlungslimite). Beiträge längstens bis 5 Jahre nach AHV-Alter. Bescheinigung beilegen.
- **Beachten:** Höchstbeträge = absolute Einzahlungslimiten: Überzahlung vom Vorsorgeträger zurückzahlen lassen
- **Beachten:** 20%-Regel gilt auch für Unselbständige ohne Pensionskasse
- **Beachten:** Einkauf für frühere Jahre (Lücken ab 2025) zusätzlich, max. 7'258 → separat bescheinigen lassen
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Saeule 3a 2026: max. Fr. 7'258 fuer Erwerbstaetige mit Anschluss an eine 2. Saeule (Pensionskasse); gleichzeitig absolute Einzahlungslimite.)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug CHF 7'258 pro Jahr für Personen, die einer Vorsorgeeinrichtung der 2. Säule angehören (8 % des oberen Grenzbetrags nach Art. 8 Abs. 1 BVG). Nur im Steuerjahr tatsächlich einbezahlte Beiträge, mit Bescheinigung.)**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Saeule 3a 2026: ohne Anschluss an 2. Saeule 20 % des Erwerbseinkommens, maximal Fr. 36'288.)** · Bund **CHF 36'288 (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens CHF 36'288 pro Jahr.)**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Saeule 3a ohne 2. Saeule: 20 % des Erwerbseinkommens (gilt auch fuer Unselbstaendige ohne Pensionskasse), max. Fr. 36'288.)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (alle Einkünfte aus selbständiger und unselbständiger, haupt- und nebenberuflicher Erwerbstätigkeit), max. CHF 36'288.)**
  - Säule 3a – Einkauf (Nachzahlung) Regel/Maximum: Kanton **CHF 7'258 (NEU ab 2025/2026: Einkauf (Nachzahlung) fuer fruehere Jahre bis zu 10 Jahre rueckwirkend; zusaetzlich zum ordentlichen Beitrag pro Jahr max. der kleine Beitrag (2026: Fr. 7'258). Voraussetzung: AHV-pflichtiges Erwerbseinkommen in der Schweiz im Einkaufsjahr und im Nachzahlungsjahr; ordentlicher Jahresbeitrag vollstaendig geleistet. Voll abzugsfaehig.)** · Bund **CHF 7'258 (Einkauf Säule 3a (ab Steuerperiode 2026, für Beitragslücken ab 1.1.2025): zusätzlich zum vollen ordentlichen Beitrag im Einkaufsjahr; max. Summe der Beitragslücken der letzten 10 Jahre (frühestens ab 2025), pro Steuerjahr höchstens CHF 7'258 (8 % des oberen BVG-Grenzbetrags, unabhängig von Zugehörigkeit zur 2. Säule); eine Jahresbeitragslücke nur durch einen einzigen Einkauf ausgleichbar; kein Einkauf nach Bezug einer Altersleistung der Säule 3a (Bezüge ab 5 Jahren vor Referenzalter zählen als Altersleistung).)**
- **Bund:** Gleiche Höchstbeträge und gleiche Zeile für Staat und Bund.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «13.1 Person 1 Anschluss 2. Säule (PK) m ja 314»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0089.md) `tg-wl-2026__c0089` – «Steuerpflichtige Personen, die einer Einrichtung der beruflichen Vorsorge (2. Säule) angehören Fr. 7'258»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0089.md) `tg-wl-2026__c0089` – «Steuerpflichtige Personen, die keiner Einrichtung der beruflichen Vorsorge (2. Säule) angehören: 20% des Erwerbseinkommens, maximal Fr. 36'288»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0089.md) `tg-wl-2026__c0089` – «Diese Höchstabzüge bilden zugleich die absoluten Einzahlungslimiten.»
  - [WL TG 2026 S. 20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0089.md) `tg-wl-2026__c0089` – «Der Abzug von 20% des Erwerbseinkommens gilt auch für unselbständig erwerbende Personen,»
  - [WL TG 2026 S. 20–21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0090.md) `tg-wl-2026__c0090` – «nannten «kleinen Beitrages» zulässig (2026 maximal 7’258 Fr.).»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «In diesem Feld sind die nach Gesetz, Statut oder Reglement geleisteten ordentlichen Bei»
  - [KS 18a S. 6](../../chunks/bund/dauernd/bund-ks-18a/bund-ks-18a__c0016.md) `bund-ks-18a__c0016` – «wobei dies erst für Beitragslücken ab dem Steuerjahr 2025 gilt.»

<a id="13-1-13-2-einkauf-abzug-vorsorge-saeule3a-einkauf"></a>
### Ziff. 13.1 / 13.2 (Einkauf) – Einkauf in die Säule 3a für frühere Jahre (neu ab 2025; keine eigene Zeile im Formular)

- **Schlüssel:** `abzug.vorsorge.saeule3a_einkauf` (Einkauf (Nachzahlung) Säule 3a – ab Steuerjahr 2026) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → 3a-Einkaufsbescheinigung der Vorsorgeeinrichtung (Einkauf separat ausweisen lassen)
- **Rein:** 3a-Einkaufsbescheinigung → Datum, Betrag, ausgeglichene Lückenjahre · 3a-Bescheinigung ordentlicher Beitrag 2026 (muss voll einbezahlt sein) · Nachweis AHV-pflichtiges Erwerbseinkommen CH im Einkaufs- und im Lückenjahr
- **Rechnen:** je Person: min(Einkauf; Σ Beitragslücken ab 2025; 7'258) zusätzlich zum vollen ordentlichen Beitrag; Kanton = Bund
- **Regel:** Neu: wer ab 1.1.2025 nicht jedes Jahr die maximal zulässigen Beiträge einbezahlt hat, kann diese bis zu 10 Jahre rückwirkend nachzahlen. Zusätzlich zum ordentlichen Beitrag pro Jahr maximal der «kleine Beitrag» (2026: Fr. 7'258). Voraussetzungen: AHV-pflichtiges Erwerbseinkommen in der Schweiz im Einkaufsjahr UND im Jahr, für das nachgezahlt wird; ordentlicher Jahresbeitrag des Einkaufsjahres muss vollständig entrichtet sein. Vollumfänglich abzugsfähig. Deklaration gemäss Wegleitung in Ziff. 13.1/13.2 (Formular 1 hat keine separate Einkaufszeile) – Bescheinigung beilegen.
- **Beachten:** Nur Beitragslücken ab Steuerjahr 2025, höchstens zehn Jahre zurück
- **Beachten:** Kein Einkauf nach Bezug einer 3a-Altersleistung (jeder Bezug ab fünf Jahren vor Referenzalter)
- **Beachten:** Formular ohne eigene Einkaufszeile → in Ziff. 13.1/13.2 mit ordentlichem Beitrag; Bescheinigung beilegen
- **Limiten:**
  - Säule 3a – Einkauf (Nachzahlung) Regel/Maximum: Kanton **CHF 7'258 (NEU ab 2025/2026: Einkauf (Nachzahlung) fuer fruehere Jahre bis zu 10 Jahre rueckwirkend; zusaetzlich zum ordentlichen Beitrag pro Jahr max. der kleine Beitrag (2026: Fr. 7'258). Voraussetzung: AHV-pflichtiges Erwerbseinkommen in der Schweiz im Einkaufsjahr und im Nachzahlungsjahr; ordentlicher Jahresbeitrag vollstaendig geleistet. Voll abzugsfaehig.)** · Bund **CHF 7'258 (Einkauf Säule 3a (ab Steuerperiode 2026, für Beitragslücken ab 1.1.2025): zusätzlich zum vollen ordentlichen Beitrag im Einkaufsjahr; max. Summe der Beitragslücken der letzten 10 Jahre (frühestens ab 2025), pro Steuerjahr höchstens CHF 7'258 (8 % des oberen BVG-Grenzbetrags, unabhängig von Zugehörigkeit zur 2. Säule); eine Jahresbeitragslücke nur durch einen einzigen Einkauf ausgleichbar; kein Einkauf nach Bezug einer Altersleistung der Säule 3a (Bezüge ab 5 Jahren vor Referenzalter zählen als Altersleistung).)**
- **Bund:** Gilt gemäss Vorwort der Wegleitung auch bei der direkten Bundessteuer.
- **Bemerkung:** Neuerung ggü. 2025-Wegleitung: Vorwort WL 2026 nennt Einkäufe in Säule 3a neu. Dass der Einkauf in dieselben Felder 13.1/13.2 gehört, folgt aus WL c0091 («Beiträge … in Ziffer 13.1/13.2»); das Formular zeigt keine separate Zeile – bei Unsicherheit Rückfrage Steuerverwaltung.
- **Quellen:**
  - [WL TG 2026 S. 20–21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0090.md) `tg-wl-2026__c0090` – «können diese Beiträge bis zu zehn Jahre»
  - [WL TG 2026 S. 20–21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0090.md) `tg-wl-2026__c0090` – «Zusätzlich zum ordentlichen Beitrag ist pro Jahr ein Einkauf in die Säule 3a in Höhe des soge-»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0091.md) `tg-wl-2026__c0091` – «Tragen Sie die Beiträge in Ziffer 13.1»
  - [KS 18a S. 6](../../chunks/bund/dauernd/bund-ks-18a/bund-ks-18a__c0016.md) `bund-ks-18a__c0016` – «wobei dies erst für Beitragslücken ab dem Steuerjahr 2025 gilt.»
  - [KS 18a S. 6](../../chunks/bund/dauernd/bund-ks-18a/bund-ks-18a__c0016.md) `bund-ks-18a__c0016` – «Die steuerpflichtige Person hat noch keine Altersleistung aus der Säule 3a bezogen»
  - [KS 18a S. 11](../../chunks/bund/dauernd/bund-ks-18a/bund-ks-18a__c0035.md) `bund-ks-18a__c0035` – «Die Jahre, für die eine Beitragslücke ausgeglichen werden soll und in welcher Höhe»
  - [WL 2a 2026 S. 7](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0050.md) `bund-wl-2a-2026__c0050` – «sein wie die Summe der Beitragslücken, die in den zehn Jahren»

<a id="14-abzug-versicherungspraemien"></a>
### Ziff. 14 – Versicherungsprämien und Zinsen von Sparkapitalien (Formular 5.2, Code 330)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 5.2 Teil C (Zeile 1 Staat, Zeile 2 Bund)
- **Rein:** KK-Jahresbestätigung → Nettoprämie (nach Abzug IPV) → Form. 5.2 A Ziff. 1 · Policen private Unfall-/Lebens-/Rentenversicherung → A Ziff. 2/3; Lohnausweis → Krankentaggeld A Ziff. 5 · Formular 2 → erhaltene Sparzinsen → A Ziff. 4
- **Rechnen:** Kanton min(Total A Code 324; 7'000 bzw. 3'500 + 1'000 je Kind/unterst. Person) / Bund min(Total A; 3'700 bzw. 1'800 + 700 je Kind) → Code 330
- **Regel:** Zulässiger Abzug = niedrigerer Betrag von «A5» (Total Prämien und Sparzinsen) und «B4» (Maximalabzug), getrennt für Staat und Bund. Krankenkassenprämie netto (nach IPV) deklarieren. Maximum Kanton: Fr. 7'000 gemeinsam / Fr. 3'500 übrige; Bund: Fr. 3'700 / Fr. 1'800 (ohne Beiträge an Säule 2/3a Fr. 5'550 / Fr. 2'700); pro Kind/unterstützte Person Kanton Fr. 1'000, Bund Fr. 700.
- **Beachten:** Bund ohne Beiträge Säule 2/3a: 5'550 bzw. 2'700 statt 3'700/1'800 (nicht kumulierbar); Kanton ohne Erhöhung
- **Beachten:** Ohne Deklaration der KK-Prämien kann der Abzug verweigert werden; NBU-Prämien → Ziff. 15.4
- **Beachten:** Form. 5.2 2026: Total A = Ziff. 6 (Code 324, inkl. Ziff. 5 Krankentaggeld); WL spricht von «A5»/«A7»
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
  - [Formular 5.2 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-2-2026/tg-form-05-2-2026__c0001.md) `tg-form-05-2-2026__c0001` – «5. Krankentaggeldversicherung gemäss Lohnausweis»
  - [Formular 5.2 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-2-2026/tg-form-05-2-2026__c0001.md) `tg-form-05-2-2026__c0001` – «6. Total selbst getragene Versicherungsprämien und Sparzinsen 324»
  - [Formular 5.2 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-2-2026/tg-form-05-2-2026__c0001.md) `tg-form-05-2-2026__c0001` – «4. erhaltene Sparzinsen gemäss Formular 2»
  - [Formular 5.2 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-2-2026/tg-form-05-2-2026__c0003.md) `tg-form-05-2-2026__c0003` – «1. Staatssteuer: der niedrigere Betrag von «A5» oder «B4 Staat» 330»
  - [WL TG 2026 S. 45–46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0213.md) `tg-wl-2026__c0213` – «Tragen Sie den niedrigeren der unter „A7“ und „B4 Staat“ ermittelten Beträge»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0209.md) `tg-wl-2026__c0209` – «Diesen Abzug können Sie nicht zusammen mit dem ordentlichen Abzug von Fr. 3'700 bzw.»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0206.md) `tg-wl-2026__c0206` – «Bei fehlender Deklaration behält sich die Veranlagungsbehörde vor»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0208.md) `tg-wl-2026__c0208` – «Prämien für die private Unfallversicherung (ausgenommen NBUV, vgl.»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0207.md) `tg-wl-2026__c0207` – «In Ziffer 1 zu deklarieren ist die Nettoprämie»

<a id="15-1-abzug-ahv-nichterwerbstaetige"></a>
### Ziff. 15.1 – AHV-Beiträge für nichterwerbstätige Personen (Code 342)

- **Schlüssel:** `abzug.ahv_nichterwerbstaetige` (AHV/IV/EO-Beiträge Nichterwerbstätiger u.ä.) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse) → AHV-Beitragsverfügung/Rechnung Ausgleichskasse
- **Rein:** AHV-Beitragsverfügung/Rechnung der Ausgleichskasse für Nichterwerbstätige → AHV/IV/EO- und FAK-Beiträge je Person
- **Rechnen:** Σ AHV/IV/EO- und FAK-Beiträge als Nichterwerbstätige/r; voll abziehbar (§ 34 Abs. 1 Ziff. 6 StG TG / Art. 33 Abs. 1 lit. d DBG); Kanton = Bund
- **Regel:** Nur AHV/IV/EO- sowie FAK-Beiträge von Nichterwerbstätigen. Beiträge von Selbständigen sind im Reingewinn (Ziff. 2) berücksichtigt, solche von Unselbständigen bereits im Nettolohn – dort nicht nochmals abziehen.
- **Beachten:** Selbständige: AHV im Reingewinn Ziff. 2.1/2.2; Unselbständige: im Nettolohn Ziff. 1.1/1.2 – nicht nochmals
- **Beachten:** AHV/FAK von Erwerbstätigen, soweit nicht in Ziff. 1/2 berücksichtigt → Ziff. 15.4
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «15.1 AHV-Beiträge für nichterwerbstätige Personen 342»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0092.md) `tg-wl-2026__c0092` – «Unter dieser Ziffer können in der Regel nur Beiträge an die AHV/IV/EO sowie FAK-Beiträge von»
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t2.md) `tg-stg__par-34-t2` – «die gemäss Gesetz, Statut oder Reglement geleisteten Einlagen, Prämien und Beiträge zum Erwerb von Ansprüchen aus Alters-, Hinterlassenen- und Invalidenversicherung»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t2.md) `bund-dbg-2026__art-33-t2` – «die gemäss Gesetz, Statut oder Reglement geleisteten Einlagen, Prämien und Beiträge an die Alters-, Hinterlassenen- und Invalidenversicherung»
  - [WL TG 2026 S. 22](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0098.md) `tg-wl-2026__c0098` – «versicherung oder AHV/IV/EO-Beiträge sowie FAK-Beiträge von erwerbstätigen Personen einge-»

<a id="15-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 15.2 – Beiträge an Einrichtungen der beruflichen Vorsorge (PK-Einkauf) – Person 1 (Code 343) / Person 2 (Code 344)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) für direkt bezahlte Einkäufe; Lohnausweis Ziff. 10.2 nur zur Kontrolle
- **Rein:** Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) → selbst bezahlte Einkäufe je Person · Lohnausweis Ziff. 10.1/10.2 → nur Kontrolle (vom Lohn abgezogen = bereits im Nettolohn) · Selbständige: PK-Beitragsbescheinigung → Privatanteil
- **Rechnen:** Σ direkt bezahlte Einkäufe gem. Bescheinigung (ohne LA Ziff. 10.1/10.2); Selbständige: Beiträge − Arbeitgeberanteil (ohne Personal: Hälfte); Kanton = Bund
- **Regel:** Nur Einkäufe, die NICHT bereits vom Lohn abgezogen und im Nettolohn (Lohnausweis Ziff. 10.2) berücksichtigt sind: selbst bezahlte Einkaufsbeiträge werden von der Vorsorgeeinrichtung separat bescheinigt. Ordentliche Beiträge (Lohnausweis 10.1) sind im Nettolohn bereits abgezogen. Selbständige: nur Privatanteil (Arbeitgeberanteil bereits im Geschäftsergebnis; ohne Personal gilt die Hälfte als Arbeitgeberanteil).
- **Beachten:** Kapitalbezug (auch WEF-Vorbezug) innert drei Jahren nach Einkauf → Einkauf nicht abzugsfähig (TG-Praxis)
- **Beachten:** Nach WEF-Vorbezug Einkauf erst zulässig, wenn Vorbezug zurückbezahlt (Art. 79b Abs. 3 BVG)
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «15.2 Beiträge an Einrichtungen der beruflichen Vorsorge»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0093.md) `tg-wl-2026__c0093` – «Die ordentlichen Beiträge sind in der Regel bereits vom Bruttolohn abgezogen und daher in Ziffer 1»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «Vom Arbeitnehmer selber entrichtete, d. h. nicht vom Lohn abgezogene Einkaufsbeiträge»
  - [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0029.md) `tg-info-faq__c0029` – «Daher ist bei diesem Sachverhalt der Einkauf in die Pensionskasse steuerlich nicht abzugsfähig.»
  - [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0028.md) `tg-info-faq__c0028` – «darf ein Einkauf von Beitragsjahren erst vorgenommen werden, wenn allfällig früher getätigte Vorbezüge für die Wohneigentumsförderung aus der 2. Säule zurückbezahlt worden sind.»
  - [KS 17 S. 6](../../chunks/bund/dauernd/bund-ks-17/bund-ks-17__c0012.md) `bund-ks-17__c0012` – «Um einen Kapitalbezug handelt es sich auch bei einem Vorbezug für das Wohneigentum.»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «nen Beiträge an Vorsorgeeinrichtungen (2. Säule) anzugeben, die der Verbesserung des»

<a id="15-3-abzug-drittbetreuung"></a>
### Ziff. 15.3 – Kosten für die Drittbetreuung von Kindern unter 14 Jahren (Code 345)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Rechnungen/Bestätigung Kita, Tagesfamilie, Hort (echte Betreuungskosten)
- **Rein:** Rechnungen/Zahlungsbelege Kita, Tagesfamilie, Hort je Kind · Nachweis Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit (Kausalität) · ggf. Nachweis, dass Rechnung keine Verpflegung/Unterhalt enthält (→ 100% statt 75%)
- **Rechnen:** je Kind < 14: Kanton min(75% × Rechnungen; 10'100) / Bund min(75% × Rechnungen; 25'800); 100% der Rechnungen, wenn nachweislich ohne Lebenshaltungskosten
- **Regel:** Kumulativ: Kind unter 14, im Haushalt des unterhaltspflichtigen Elternteils, Kosten kausal mit Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit verbunden. Nur echte Betreuungskosten: ohne Gegenbeweis werden in der Regel nur 75% der Rechnung anerkannt (Verpflegung/Unterhalt ausgeschieden). Maximum pro Kind Kanton Fr. 10'100, Bund Fr. 25'800. Getrennt besteuerte Eltern: Anspruch hat der Elternteil, der mit dem Kind zusammenlebt; bei alternierender Obhut je höchstens die Hälfte der Maxima (nur bei hälftiger Zuteilung des Kinderabzugs).
- **Beachten:** Alternierende Obhut: je Elternteil max. 50% (Kanton von 10'100, nur bei hälftigem Kinderabzug; Bund «25'500» ≠ 25'800)
- **Beachten:** Bund: Konkubinat mit gemeinsamer Sorge je max. Hälfte; Summe beider > Maximum → anteilig gekürzt
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 10'100 (Kinderdrittbetreuung: nachgewiesene echte Betreuungskosten, max. Fr. 10'100 pro Kind (in der Regel 75 % der Rechnungsbetraege anerkannt, ausser Nachweis ohne Verpflegung/Unterhalt). Alternierende Obhut: je Elternteil max. 50 % (Fr. 5'050) bei haelftiger Zuteilung des Kinderabzugs.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind, höchstens CHF 25'800; Kind unter 14 Jahren im gleichen Haushalt; Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 Jahre (Kind darf das 14. Altersjahr noch nicht vollendet haben; Kind lebt mit dem fuer den Unterhalt sorgenden Elternteil im gleichen Haushalt; kausaler Zusammenhang mit Erwerbstaetigkeit, Ausbildung oder Erwerbsunfaehigkeit. Betreuungsperson muss mind. 16 Jahre alt sein (§ 11c Abs. 2 StV).)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat.)**
- **Bund:** Bund: maximal Fr. 25'800 pro Kind (Wegleitung nennt bei alternierender Obhut «50% von Fr. 25'500» – Schreibfehler/Inkonsistenz in WL c0096 vs. Fr. 25'800 in c0096 erster Absatz).
- **Bemerkung:** Innere Inkonsistenz WL 2026 c0096: Fr. 25'800 (Maximalbetrag) vs. «50% von Fr. 25'500» bei alternierender Obhut. Massgebend wird Fr. 25'800 gesetzt; Fachperson prüft Hälfte bei alternierender Obhut.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «15.3 Kosten für die Drittbetreuung von Kindern unter 14 Jahren 345»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0094.md) `tg-wl-2026__c0094` – «Pro Kind können Sie kantonal die nachgewiesenen echten Kosten für die Drittbetreuung in Abzug»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0094.md) `tg-wl-2026__c0094` – «werden in der Regel daher jeweils nur 75% als echte Drittbetreuungskosten anerkannt.»
  - [WL TG 2026 S. 21](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0094.md) `tg-wl-2026__c0094` – «in den Rechnungsbeträgen nachgewiesenermassen keine Lebenshaltungskosten enthalten»
  - [WL TG 2026 S. 21–22](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0095.md) `tg-wl-2026__c0095` – «Hälfte des gesetzlichen Maximalbetrags (50% von Fr. 10'100) in Abzug bringen»
  - [WL TG 2026 S. 22](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0096.md) `tg-wl-2026__c0096` – «bis höchstens zur Hälfte der gesetzlichen Maximalbeträge (50% von Fr. 25'500) in Abzug bringen.»
  - [WL TG 2026 S. 22](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0096.md) `tg-wl-2026__c0096` – «Betragen die geltend gemachten Kosten beider Elternteile zusammen mehr als den Maximalbetrag»
  - [WL TG 2026 S. 22](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0097.md) `tg-wl-2026__c0097` – «Bei Konkubinatspaaren mit gemeinsamem Kind und gemeinsamer elterlicher Sorge»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t7.md) `bund-dbg-2026__art-33-t7` – «jedoch höchstens 25 800 Franken, für die Drittbetreuung jedes Kindes»

<a id="15-4-abzug-uebrige"></a>
### Ziff. 15.4 – Weitere Abzüge – genau bezeichnen (Code 346)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Begründung/Beleg zur Aufstellung (z.B. NBU-Prämien, AHV/IV/EO- und FAK-Beiträge Erwerbstätiger, soweit nicht in Ziff. 1/2 berücksichtigt)
- **Rein:** Separates Blatt mit genauer Bezeichnung + Belege · NBU-Prämienbelege (soweit nicht im Lohn berücksichtigt) · AHV/IV/EO-/FAK-Beitragsrechnungen Erwerbstätiger (soweit nicht in Ziff. 1/2)
- **Rechnen:** Σ einzeln bezeichnete, belegte Abzüge (z.B. obligatorische NBUV, AHV/IV/EO/FAK Erwerbstätiger), nur soweit nicht in Ziff. 1/2; je Spalte Staat / Bund
- **Regel:** Geltend gemachte Abzüge begründen und belegen. NICHT hier: Vermögensverwaltungskosten (→ Formular 2), Einsatzkosten für nicht steuerbare Geldspielgewinne (nicht abziehbar), Prämien KVG-Unfallversicherung Nichterwerbstätiger (→ Ziff. 14).
- **Beachten:** Nicht hier: KVG-Unfallprämien Nichterwerbstätiger → Ziff. 14; Vermögensverwaltungskosten → Formular 2
- **Beachten:** Einsatzkosten Geldspiele: steuerbare Gewinne → Formular 2; nicht steuerbare Gewinne → kein Abzug
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «15.4 Weitere Abzüge: 346»
  - [WL TG 2026 S. 22](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0098.md) `tg-wl-2026__c0098` – «Die geltend gemachten Abzüge sind zu begründen und zu belegen.»
  - [WL TG 2026 S. 22](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0098.md) `tg-wl-2026__c0098` – «Einsatzkosten für steuerbare Gewinne aus Geldspielen sind im Wertschriften- und Guthabenver-»
  - [WL TG 2026 S. 22](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0098.md) `tg-wl-2026__c0098` – «Vermögensverwaltungskosten sind im Wertschriften- und Guthabenverzeichnis in Abzug zu»

<a id="15-5-abzug-parteispenden"></a>
### Ziff. 15.5 – Mitgliederbeiträge und Zuwendungen an politische Parteien (Formular 6, Code 347)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Formular 6 (Spalte politische Parteien); Quittungen ab Fr. 1'000 pro Zuwendung
- **Rein:** Quittungen/Bescheinigungen der Partei (ab Fr. 1'000 pro Zuwendung beilegen) · Formular 6 Spalte «politische Parteien» → Total B → Code 347
- **Rechnen:** Kanton min(Σ Parteibeiträge/-zuwendungen; 10'000) / Bund min(Σ; 10'600)
- **Regel:** Voraussetzung: Partei im Parteienregister eingetragen und in einem kantonalen Parlament vertreten oder ≥3% Stimmen. Maximal Fr. 10'000 (Staat) / Fr. 10'600 (Bund). Einzeln mit Name/Sitz der Partei auflisten; Pauschalvermerke wie «Spenden an diverse Organisationen» werden nicht anerkannt.
- **Beachten:** Partei im Parteienregister UND in einem kantonalen Parlament vertreten oder ≥ 3% Stimmen
- **Beachten:** Getrennte Spalte in Form. 6; gemeinnützige Zuwendungen → Ziff. 23.2 (andere Limiten)
- **Beachten:** Einzeln mit Name/Sitz; Pauschalvermerke («Spenden an diverse Organisationen») nicht anerkannt
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeitraege und Zuwendungen an politische Parteien: max. Fr. 10'000 (Staats- und Gemeindesteuern); Bund Fr. 10'600.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister / kantonales Parlament / mind. 3 % Stimmen): bis Gesamtbetrag CHF 10'600.)**
- **Bund:** Maximalabzug Bund Fr. 10'600.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «15.5 Mitgliederbeiträge und Zuwendungen an politische Parteien Formular 6 347»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0216.md) `tg-wl-2026__c0216` – «Der Maximalabzug beträgt bei den Staats- und Gemeindesteuern Fr. 10 000 und bei der direkten»
  - [Formular 6 TG 2026 S. 1](../../chunks/tg/2026/tg-form-06-2026/tg-form-06-2026__c0003.md) `tg-form-06-2026__c0003` – «Staatssteuer: max. Fr. 10 000.– Bundessteuer: max. Fr. 10 600.–»
  - [Formular 6 TG 2026 S. 1](../../chunks/tg/2026/tg-form-06-2026/tg-form-06-2026__c0001.md) `tg-form-06-2026__c0001` – «Ab Fr. 1000.– pro Zuwendung reichen Sie bitte die entsprechende Quittung oder Bescheinigung mit Ihrer Steuererklärung ein.»
  - [WL TG 2026 S. 46–47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0218.md) `tg-wl-2026__c0218` – «Übertragen Sie das Total der geleisteten Mitgliederbeiträge und Zuwendungen an politische Par-»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0217.md) `tg-wl-2026__c0217` – «mit dem Vermerk „Spenden an diverse Organisationen“ oder ähnlichen Vermerken»

<a id="15-6-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 15.6 – Teilbesteuerungsabzug Beteiligungen im Privatvermögen (Formular 1 Code 341, Übertrag aus Formular 2 Hilfsblatt)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2, letzte Seite: Hilfsblatt qualifizierte Beteiligungen (Ziff. 3 Teilbesteuerungsabzug)
- **Rein:** Formular 2, Hilfsblatt qualifizierte Beteiligungen (S. 4) → Ziff. 3 Teilbesteuerungsabzug · Dividendenabrechnung → Beteiligungsertrag 2026 (brutto in Formular 2 Spalte 8/9) · Nachweis Beteiligungsquote ≥ 10% am Grund-/Stammkapital · Formular 2 Detailverzeichnis: Code 05 = qualifizierte Beteiligung im Privatvermögen
- **Rechnen:** Kanton 40% / Bund 30% × Σ Erträge qualifizierter Beteiligungen PV (Hilfsblatt Ziff. 2) → Ziff. 3 → Ziff. 15.6
- **Regel:** Nur auf Antrag über das Hilfsblatt: Beteiligungsquote ≥10% (Voraussetzungen siehe WL). Abzug Kanton 40%, Bund 30% der Beteiligungserträge; in beide Spalten Bund/Kanton übertragen. Beteiligungen im Geschäftsvermögen: Antrag über Formular 14, nicht hier.
- **Beachten:** Ertrag bleibt voll in Formular 2 (Spalte 8/9) deklariert; Entlastung nur über Antrag im Hilfsblatt
- **Beachten:** Ohne Nachweis der Voraussetzungen Besteuerung zu 100%
- **Beachten:** Erfasst: Dividenden, Gewinnanteile, Liquidationsüberschüsse, geldwerte Vorteile inkl. Gratisaktien
- **Bund:** 30% (statt 40% Kanton).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «15.6 Teilbesteuerungsabzug Beteiligungen im Privatvermögen Formular 2 341»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0164.md) `tg-wl-2026__c0164` – «3 einzusetzende Teilbesteuerungsabzug beträgt 40% bei den Staats- und Gemeindesteuern und»
  - [Formular 2 TG 2026 S. 4](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0008.md) `tg-form-02-2026__c0008` – «3. Teilbesteuerungsabzug (Staatssteuer 40% / Bundessteuer 30%)»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0163.md) `tg-wl-2026__c0163` – «mögen von mindestens 10% am Grund- oder Stammkapital einer Kapitalgesellschaft oder Genos-»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0163.md) `tg-wl-2026__c0163` – «Bei fehlendem Nachweis erfolgt die Besteuerung zu 100%»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0164.md) `tg-wl-2026__c0164` – «Die Erträge aus qualifizierten Beteiligungen im Privatvermögen sind grundsätzlich in Spalte 8»
  - [Formular 2 TG 2026 S. 3](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0007.md) `tg-form-02-2026__c0007` – «qualifiz. Beteiligung im Privatvermögen = 05»

<a id="16-1-16-2-abzug-weiterbildung"></a>
### Ziff. 16.1 / 16.2 – Berufsorientierte Aus- und Weiterbildungskosten – Person 1 (Code 348) / Person 2 (Code 349)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Kursrechnungen/Zahlungsnachweise mit Aufstellung; Lohnausweis Ziff. 13.3 (Arbeitgeberbeiträge)
- **Rein:** Kursrechnungen/Zahlungsnachweise + Aufstellung je Person · Lohnausweis Ziff. 13.3 → vom Arbeitgeber vergütete Weiterbildungskosten (mindern Abzug) · Bestätigungen Beiträge Dritter (Bund, Branchenverband)
- **Rechnen:** je Person: min(selbst getragene Kosten − Beiträge Dritter (inkl. LA Ziff. 13.3); 13'000); Kanton = Bund
- **Regel:** Maximal Fr. 13'000 pro Person (Staat und Bund). Erstausbildung (erster Abschluss Sek II) ausgenommen; ohne Sek-II-Abschluss erst ab 20 Jahren. Kostenbeteiligungen Dritter (Arbeitgeber, Bund, Branchenverbände) mindern den Abzug – Lohnausweis Ziff. 13.3 (an den Arbeitnehmer vergütete Beträge) abziehen. IT-Geräte nur bei direktem Bezug zum Lehrgang, Privatanteil in der Regel 50%. Liebhaberei/Selbstentfaltung nicht abzugsfähig. Aufstellung mit Belegen beilegen.
- **Beachten:** Abzug auch ohne Erwerbseinkommen im Steuerjahr möglich
- **Beachten:** AG-Direktzahlungen an Bildungsinstitut stehen nicht im LA 13.3 und sind nicht selbst getragen → kein Abzug
- **Beachten:** IT-Geräte nur bei spezifischem Lehrgangsbezug, abzüglich Privatanteil i.d.R. 50%
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung: max. Fr. 13'000 pro Person und Jahr (Kanton und Bund); Erstausbildung (Sek. II) ausgenommen; Kostenbeteiligung Dritter mindert.)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildungs- inkl. Umschulungskosten bis CHF 13'000 pro Jahr, sofern erster Abschluss Sek. II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)**
- **Bund:** Gleich: Fr. 13'000 pro Person.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «16.1 Person 1 348»
  - [WL TG 2026 S. 22–23](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0101.md) `tg-wl-2026__c0101` – «auf jährlich maximal Fr. 13'000 pro Person beschränkt.»
  - [WL TG 2026 S. 22–23](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0101.md) `tg-wl-2026__c0101` – «Kostenbeteiligungen Dritter (z.B. Arbeitgebende, Bund, Branchenverbände etc.) mindern die»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «Nicht anzugeben sind Vergütungen, die direkt an»
  - [WL TG 2026 S. 22](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0100.md) `tg-wl-2026__c0100` – «Abzug ist nicht (mehr) daran gebunden, dass in der betreffenden Steuerperiode ein Einkommen»
  - [WL TG 2026 S. 22](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0100.md) `tg-wl-2026__c0100` – «Die selbst getragenen Aufwendungen im Zusammenhang mit berufsorientierter Aus- und Weiterbil-»
  - [WL TG 2026 S. 23](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0102.md) `tg-wl-2026__c0102` – «Dabei ist ein angemessener Privatanteil von in der Regel 50% zu berücksichtigen.»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t4.md) `bund-dbg-2026__art-33-t4` – «bis zum Gesamtbetrag von 13 000 Franken»

<a id="17-abzug-behinderungskosten"></a>
### Ziff. 17 – Behinderungsbedingte Kosten (Formular 5.1 Teil C, Code 350)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 5.1 Teil C (Aufwendungen A minus Vergütungen B); Nachweise
- **Rein:** Rechnungen behinderungsbedingte Kosten (Hilfsmittel, Prothesen, Heim, Fahrzeugumbau) → Form. 5.1 A · Abrechnungen KK/IV/AHV/SUVA, Hilflosenentschädigung → Form. 5.1 B · IV-/HE-Verfügung als Nachweis der Behinderung bzw. für Pauschale
- **Rechnen:** Form. 5.1 C: Total A − Total B → Code 350, ohne Selbstbehalt; oder Pauschale gehörlos/Dialyse/HE leicht 2'500, HE mittel 5'000, HE schwer 7'500; Kanton = Bund
- **Regel:** Selbst getragene behinderungsbedingte Kosten für sich und Personen mit Kinder-/Unterstützungsabzug voll abziehbar (kein Selbstbehalt). Vergütungen Dritter, Hilflosenentschädigung und Anteil Lebenshaltungskosten abziehen. Alternativ Pauschalen: gehörlos / Dialyse / Hilflosenentschädigung leicht Fr. 2'500, mittel Fr. 5'000, schwer Fr. 7'500.
- **Beachten:** Heimaufenthalt: um Lebenshaltungskosten kürzen (i.d.R. Fr. 2'000 pro Monat)
- **Beachten:** Krankheitskosten einer behinderten Person → Ziff. 23.1 (mit 5% Selbstbehalt)
- **Beachten:** Diät (z.B. Zöliakie) oder Brille/Hörgerät begründet keine Behinderung
- **Bund:** Gleiche Regeln (voll abziehbar).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «17. Behinderungsbedingte Kosten Formular 5 350»
  - [WL TG 2026 S. 42–43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0200.md) `tg-wl-2026__c0200` – «– Bezügerinnen/Bezüger einer Hilflosenentschädigung schweren Grades Fr. 7'500»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0199.md) `tg-wl-2026__c0199` – «det werden müssen (in der Regel Fr. 2 000 pro Monat).»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0199.md) `tg-wl-2026__c0199` – «werden, als diese 5% des Nettoeinkommens (Ziff. 22) übersteigen.»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0198.md) `tg-wl-2026__c0198` – «die betroffene Person eine Diät einhalten muss (z.B. Zöliakie).»
  - [Formular 5.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-1-2026/tg-form-05-1-2026__c0003.md) `tg-form-05-1-2026__c0003` – «Abzugsfähige behinderungsbedingte Kosten 350»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t3.md) `bund-dbg-2026__art-33-t3` – «die behinderungsbedingten Kosten des Steuerpflichtigen oder der von ihm unterhaltenen Personen mit Behinderungen»
  - [Formular 5.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-1-2026/tg-form-05-1-2026__c0001.md) `tg-form-05-1-2026__c0001` – «Krankheits- und Unfallkosten Behinderungsbedingte Kosten Formular 5.1»
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «23.1 Krankheits- und Unfallkosten Formular 5 364»

<a id="18-abzug-zweiverdiener"></a>
### Ziff. 18 – Zweiverdienerabzug (Code 356)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Berechnung aus Erwerbseinkommen beider Eheleute (Ziff. 1/2 abzüglich Berufsauslagen, BVG, 3a)
- **Rechnen:** nur Bund: EK_tief = kleineres Erwerbseinkommen; Abzug = min(max(50% × EK_tief; 8'600); 14'100; EK_tief) / Kanton: kein Abzug
- **Regel:** NUR direkte Bundessteuer (Staat: kein Abzug). 50% des niedrigeren Erwerbseinkommens, mindestens Fr. 8'600, höchstens Fr. 14'100; liegt das niedrigere Erwerbseinkommen unter Fr. 8'600, nur dieser Teilbetrag.
- **Beachten:** Nur Ehegatten/eingetragene Partner in ungetrennter Ehe, beide mit Erwerbseinkommen
- **Beachten:** Erhebliche Mitarbeit im Betrieb des anderen bzw. gemeinsame Selbständigkeit: je Hälfte des gemeinsamen EK
- **Beachten:** Spalte Staat leer lassen
- **Limiten:**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **n/a – StP 34 Nr. 25: 'Im Gesetz ... ist kein Zweiverdienerabzug vorgesehen' (tg-stp-34-25__c0001); WL 2026 c0103.** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (Ehepaare in ungetrennter Ehe, beide erwerbstätig).)**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **n/a** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum.)**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **n/a** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum.)**
- **Bund:** Nur Bund (Fr. 8'600–14'100); bei Staats-/Gemeindesteuern gibt es keinen Zweiverdienerabzug.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «18. Zweiverdienerabzug 356»
  - [WL TG 2026 S. 23](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0103.md) `tg-wl-2026__c0103` – «Der Abzug beläuft sich auf mindestens Fr. 8'600 und höchstens Fr. 14'100.»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t6.md) `bund-dbg-2026__art-33-t6` – «wird jedem Ehegatten die Hälfte des gemeinsamen Erwerbseinkommens zugewiesen.»
  - [WL TG 2026 S. 23](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0103.md) `tg-wl-2026__c0103` – «Beträgt das so berechnete niedrigere Erwerbseinkommen weniger als Fr. 8'600,»

<a id="19-berechnung-total"></a>
### Ziff. 19 – Total Abzüge (Code 360) – Übertrag in Ziffer 21

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 10 bis 18)
- **Rein:** Übertrag Ziff. 10.1 bis 18 (Codes 240–356)
- **Rechnen:** Code 360 = Σ Ziff. 10.1–18 je Spalte Staat / Bund (Ziff. 18 nur Bund) → Übertrag Ziff. 21
- **Regel:** Summe der Abzüge Ziff. 10.1 bis 18, getrennt Staat/Bund; Übertrag in Ziff. 21.
- **Beachten:** Spalten getrennt summieren: Fahrkosten, Versicherungen, Drittbetreuung, Parteien, Teilbesteuerung weichen ab
- **Beachten:** Krankheitskosten (23.1) und Zuwendungen (23.2) nicht hier – erst nach Nettoeinkommen Ziff. 22
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «19. Total Abzüge, zu übertragen in Ziffer 21 360»
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0010.md) `tg-form-01-2026__c0010` – «10.1 Person 1 Formular 4.2 240»
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «18. Zweiverdienerabzug 356»
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «23.2 Freiwillige Zuwendungen Formular 6 366»

## Einkommensberechnung

<a id="20-berechnung-total"></a>
### Ziff. 20 – Total der Einkünfte, Übertrag von Seite 2 (Ziffer 6 oder 9)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 9 (Code 198) bzw. Ziff. 6 (Code 175) ohne Liegenschaften
- **Rechnen:** = Ziff. 9 oder Ziff. 6, je Spalte Staat / Bund
- **Regel:** Übertrag von Ziff. 6 (ohne Liegenschaften) bzw. Ziff. 9.
- **Beachten:** Ziff. 6 nur ohne Liegenschaften (Ziff. 8.1 leer); sonst Ziff. 9
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «20. Total der Einkünfte, Übertrag von Seite 2 (Ziffer 6 oder 9)»
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0009.md) `tg-form-01-2026__c0009` – «9. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 20 198»
  - [Formular 1 TG 2026 S. 2](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0008.md) `tg-form-01-2026__c0008` – «6. Zwischentotal der Einkünfte 175»
  - [WL TG 2026 S. 19–20](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0084.md) `tg-wl-2026__c0084` – «besitzen Sie keine Liegenschaften, übertragen Sie das»

<a id="21-berechnung-total"></a>
### Ziff. 21 – Total der Abzüge, Übertrag von Ziffer 19

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Ziff. 19 (Code 360)
- **Rechnen:** = Ziff. 19, je Spalte Staat / Bund
- **Regel:** Übertrag Ziff. 19, getrennt Staat/Bund.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «21. Total der Abzüge, Übertrag von Ziffer 19»
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0011.md) `tg-form-01-2026__c0011` – «19. Total Abzüge, zu übertragen in Ziffer 21 360»

<a id="22-berechnung-total"></a>
### Ziff. 22 – Nettoeinkommen (Code 362)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 20 minus Ziff. 21)
- **Rein:** Übertrag aus Ziff. 20 und Ziff. 21
- **Rechnen:** Code 362 = Ziff. 20 − Ziff. 21, je Spalte Staat / Bund
- **Regel:** Basis für Selbstbehalt Krankheitskosten (5%) und Limite freiwillige Zuwendungen (20%); Spalte Staat und Bund je getrennt verwenden.
- **Beachten:** Basis Selbstbehalt Ziff. 23.1: 5% × NE je Spalte (Staat mit NE Staat, Bund mit NE Bund)
- **Beachten:** Basis Zuwendungen Ziff. 23.2: Kanton NE ≤ 40'000 → max. 8'000, sonst 20% × NE; Bund 20% × NE
- **Beachten:** Kann negativ sein (Formular: «– wenn negativ»)
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten: abziehbar, soweit selbst getragen und ueber 5 % des Nettoeinkommens (Ziff. 22 Steuererklaerung). Diaet-Pauschale Fr. 2'500 (z.B. Zoeliakie, nicht Diabetes).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: max. 20 % des Nettoeinkommens (Ziff. 22); bei Nettoeinkommen bis Fr. 40'000 max. Fr. 8'000.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «22. Nettoeinkommen 362»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0203.md) `tg-wl-2026__c0203` – «ziehen Sie einen Selbstbehalt von 5% des Nettoeinkommens gemäss Ziffer 22 der Steuererklä-»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0215.md) `tg-wl-2026__c0215` – «nem Nettoeinkommen bis Fr. 40'000 maximal den Betrag von Fr. 8 000 abziehen.»
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «EINKOMMENSBERECHNUNG – wenn negativ»

<a id="23-1-abzug-krankheitskosten"></a>
### Ziff. 23.1 – Krankheits- und Unfallkosten (Formular 5.1 Teil D, Code 364)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 5.1 Teil D «Abzugsfähige Krankheits- und Unfallkosten» (Staat links / Bund rechts)
- **Rein:** KK-Kostenzusammenstellung → Franchise/Selbstbehalt (Form. 5.1 A Ziff. 1) und Vergütungen (B Ziff. 1) · Arzt-, Zahnarzt-, Spital-, Therapierechnungen → Form. 5.1 A Ziff. 2–6 · Ärztliche Verordnung (Kuren/Therapien, Diät) beilegen
- **Rechnen:** je Spalte: max(0; (Total A − Total B) − 5% × Ziff. 22) → Form. 5.1 D, Code 364 (Staat mit NE Staat, Bund mit NE Bund); Diät-Pauschale 2'500 statt effektiv
- **Regel:** Selbst getragene Kosten (Arzt, Zahnarzt, Spital, Medikamente, Brillen, Kuren; für sich und Personen mit Kinder-/Unterstützungsabzug) abzüglich Vergütungen Dritter (Krankenkasse, Versicherungen, Hilflosenentschädigung, Pflegefinanzierung, Anteil Lebenshaltungskosten) und abzüglich Selbstbehalt 5% des Nettoeinkommens (Ziff. 22, Staat und Bund je mit eigenem Nettoeinkommen). Diätpauschale Fr. 2'500 bei lebensnotwendiger Diät (z.B. Zöliakie; nicht Diabetes). Nicht abziehbar: Krankenkassenprämien, Fahrkosten zum Arzt, Prävention, Schönheits-/Fitnesskuren. Belege geordnet beilegen.
- **Beachten:** Nicht abziehbar: KK-Prämien, Arztfahrten (ausser dauernde Pflegebedürftigkeit), Prävention, Schönheits-/Fitnesskuren
- **Beachten:** Altersheim (nicht behinderungsbedingt): nur Pflegekosten; Diabetes: keine Diät-Pauschale, nur effektive Mehrkosten
- **Beachten:** Nur für sich und Personen mit Kinder-/Unterstützungsabzug; Behinderungskosten → Ziff. 17 (ohne Selbstbehalt)
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten: abziehbar, soweit selbst getragen und ueber 5 % des Nettoeinkommens (Ziff. 22 Steuererklaerung). Diaet-Pauschale Fr. 2'500 (z.B. Zoeliakie, nicht Diabetes).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
- **Bund:** Selbstbehalt 5% vom Nettoeinkommen der Spalte Bund (Betrag meist abweichend vom Staat).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «23.1 Krankheits- und Unfallkosten Formular 5 364»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0196.md) `tg-wl-2026__c0196` – «Soweit Sie die Kosten selber tragen und diese 5% des Nettoeinkommens (Ziffer 22) übersteigen,»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0196.md) `tg-wl-2026__c0196` – «können Sie anstelle der effektiven»
  - [Formular 5.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-1-2026/tg-form-05-1-2026__c0001.md) `tg-form-05-1-2026__c0001` – «1. Selbstbehalt / Franchise gemäss detaillierter Kostenzusammenstellung der Krankenkasse»
  - [Formular 5.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-1-2026/tg-form-05-1-2026__c0004.md) `tg-form-05-1-2026__c0004` – «abzüglich Selbstbehalt (5% von Ziffer 22 der Steuererklärung)»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0201.md) `tg-wl-2026__c0201` – «Ebenfalls nicht abziehen können Sie die Fahrkosten zum Arzt, Zahnarzt, Spital usw., ausgenommen»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0201.md) `tg-wl-2026__c0201` – «(allfällige Pflegekosten sind aber abzugsfähig), nicht ärztlich verordnete Akupunktur, Präventivmas-»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0201.md) `tg-wl-2026__c0201` – «Nicht abzugsfähig sind zudem die Krankenkassenprämien sowie»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0202.md) `tg-wl-2026__c0202` – «tragen Sie bitte in Ziffer 17 auf Seite 3 der Steuererklärung»

<a id="23-2-abzug-spenden"></a>
### Ziff. 23.2 – Freiwillige Zuwendungen (Formular 6, Code 366)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Formular 6 «Berechnung abzugsfähige freiwillige Zuwendungen»; Quittungen ab Fr. 1'000 pro Zuwendung
- **Rein:** Spendenquittungen/Bescheinigungen (ab Fr. 1'000 pro Zuwendung beilegen) · Formular 6 Spalte «gemeinnützige oder öffentliche Zwecke» → Total B · Kantonale Liste geprüfter Institutionen (steuerverwaltung.tg.ch)
- **Rechnen:** Kanton min(Σ − 200; 8'000 bei NE ≤ 40'000, sonst 20% × NE Staat) / Bund (wenn Σ ≥ 100) min(Σ; 20% × NE Bund)
- **Regel:** Nur Zuwendungen an in der Schweiz steuerbefreite Körperschaften für öffentliche/gemeinnützige Zwecke (kantonale Liste). Kanton: Abzug soweit gesamthaft über Fr. 200; max. Fr. 8'000 bei Nettoeinkommen bis Fr. 40'000, darüber max. 20% des Nettoeinkommens. Bund: ab Fr. 100 gesamthaft ohne Selbstbehalt bis max. 20% des Nettoeinkommens. Religiöse, wohltätige, kulturelle, gesellige, sportliche Zwecke und ausländische Empfänger nicht abziehbar.
- **Beachten:** Nicht abziehbar: ehrenamtliche Arbeit, Empfänger mit Sitz im Ausland, religiöse/sportliche u.ä. Zwecke
- **Beachten:** Auch Sachzuwendungen (übrige Vermögenswerte) und Leistungen an Bund/Kantone/Gemeinden abziehbar
- **Beachten:** Einzeln mit Name/Sitz; Pauschalvermerke («Spenden an diverse Organisationen») nicht anerkannt
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 200 (Freiwillige Zuwendungen: abziehbar, soweit sie gesamthaft Fr. 200 uebersteigen (Selbstbehalt Fr. 200). Bund: ab Fr. 100 ohne Selbstbehalt.)** · Bund **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn im Steuerjahr mindestens CHF 100 erreicht.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: max. 20 % des Nettoeinkommens (Ziff. 22); bei Nettoeinkommen bis Fr. 40'000 max. Fr. 8'000.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**
- **Bund:** Bund: Mindestbetrag Fr. 100, kein Selbstbehalt, max. 20% des Nettoeinkommens.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «23.2 Freiwillige Zuwendungen Formular 6 366»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0215.md) `tg-wl-2026__c0215` – «maximal den Betrag von Fr. 8 000 abziehen.»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0215.md) `tg-wl-2026__c0215` – «gesamthaft (ohne Selbstbehalt) bis maximal 20% des Nettoein-»
  - [Formular 6 TG 2026 S. 1](../../chunks/tg/2026/tg-form-06-2026/tg-form-06-2026__c0003.md) `tg-form-06-2026__c0003` – «abzüglich Selbstbehalt (Staats- und Gemeindesteuern) – 200.–»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0215.md) `tg-wl-2026__c0215` – «Sofern die freiwilligen Zuwendungen insgesamt den Betrag von Fr. 100 erreichen»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0214.md) `tg-wl-2026__c0214` – «willige Leistungen an Bund, Kantone, Gemeinden und deren Anstalten.»
  - [Formular 6 TG 2026 S. 1](../../chunks/tg/2026/tg-form-06-2026/tg-form-06-2026__c0001.md) `tg-form-06-2026__c0001` – «Ab Fr. 1000.– pro Zuwendung reichen Sie bitte die entsprechende Quittung oder Bescheinigung mit Ihrer Steuererklärung ein.»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0217.md) `tg-wl-2026__c0217` – «mit dem Vermerk „Spenden an diverse Organisationen“ oder ähnlichen Vermerken»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0214.md) `tg-wl-2026__c0214` – «Ebenfalls nicht abzugsfähig sind unentgelt- liche ehrenamtliche Arbeitsleistungen.»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0214.md) `tg-wl-2026__c0214` – «Freiwillige Zuwendungen von Geld oder von übrigen Vermögenswerten an eine Körperschaft»

<a id="23-3-abzug-uebrige"></a>
### Ziff. 23.3 – Separat zu besteuernde Liquidationsgewinne (Code 368)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 14a (Berechnung Liquidationsgewinn); StP 38b Nr. 1
- **Rein:** Jahresrechnung/Geschäftsabschluss → in Ziff. 2.1/2.2 enthaltener Liquidationsgewinn · Formular 14a → Berechnung Liquidationsgewinn (stille Reserven der letzten zwei Geschäftsjahre)
- **Rechnen:** Abzug = in Ziff. 2.1/2.2 enthaltene realisierte stille Reserven der letzten zwei Geschäftsjahre (Formular 14a), je Spalte Staat / Bund → Code 368
- **Regel:** Bei definitiver Geschäftsaufgabe nach vollendetem 55. Altersjahr oder wegen Invalidität werden die in den letzten zwei Geschäftsjahren realisierten stillen Reserven getrennt privilegiert besteuert; hier von den ordentlich steuerbaren Einkünften abziehen (im Geschäftsergebnis Ziff. 2.1/2.2 enthalten).
- **Beachten:** Nur bei definitiver Aufgabe nach vollendetem 55. Altersjahr oder wegen Invalidität (Kanton und Bund)
- **Beachten:** Erben/überlebende Ehegatten: nur ohne Fortführung; Abrechnung spätestens fünf Kalenderjahre nach Todesjahr
- **Beachten:** Kanton: fiktiver Einkauf wie Kapitalleistung (§ 39 StG), Rest einfache Steuer 5%; Bund: fiktiver Einkauf Art. 38 DBG
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «23.3 Separat zu besteuernde Liquidationsgewinne 368»
  - [WL TG 2026 S. 16](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0063.md) `tg-wl-2026__c0063` – «können Sie daher unter Ziffer 23.3 wieder von den Einkünften in Abzug bringen»
  - [WL TG 2026 S. 23](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0105.md) `tg-wl-2026__c0105` – «die mittels Erbgang übernommene Unternehmung nicht fortführen»
  - [WL TG 2026 S. 23](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0105.md) `tg-wl-2026__c0105` – «spätestens fünf Kalenderjahre nach Ablauf des Todesjahres der erblassenden Personen»
  - [WL TG 2026 S. 23](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0105.md) `tg-wl-2026__c0105` – «Sie können zudem das Formular 14a als ausfüllbare»
  - [KS 28 S. 26](../../chunks/bund/dauernd/bund-ks-28/bund-ks-28__c0075.md) `bund-ks-28__c0075` – «Der Liquidationsgewinn wird im Umfang des fiktiven Einkaufs wie eine Kapitalleistung aus Vorsorge nach Artikel 38 DBG besteuert»
  - [StG TG § 38b](../../chunks/tg/2025/tg-stg/tg-stg__par-38b.md) `tg-stg__par-38b` – «in gleicher Weise wie Kapitalleistungen aus Vorsorge gemäss § 39 erhoben»
  - [StG TG § 38b](../../chunks/tg/2025/tg-stg/tg-stg__par-38b.md) `tg-stg__par-38b` – «Der Restbetrag der realisierten stillen Reserven wird zum Satz der einfachen Steuer von 5 Prozent besteuert.»

<a id="24-berechnung-total"></a>
### Ziff. 24 – Reineinkommen (Code 372)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 22 minus 23.1 bis 23.3)
- **Rein:** Übertrag Ziff. 22 Nettoeinkommen (Code 362) · Übertrag Ziff. 23.1–23.3 (Codes 364, 366, 368)
- **Rechnen:** Ziff. 22 − (Ziff. 23.1 + 23.2 + 23.3), je Spalte Staat / Bund → Code 372
- **Regel:** Satzbestimmend für den Abzug AHV-Rentner/Erwerbsunfähige/Verwitwete (Ziff. 25.3).
- **Beachten:** Selbstbehalt Krankheitskosten (5%) und Spendenmaximum (20%) auf Basis Ziff. 22 rechnen, nicht Ziff. 24
- **Beachten:** Reineinkommen Spalte Staat ist massgebend für den Rentnerabzug Ziff. 25.3 (nur Kanton)
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0012.md) `tg-form-01-2026__c0012` – «24. Reineinkommen (Ziffer 22 abzüglich Ziffern 23.1 bis 23.3) 372»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0203.md) `tg-wl-2026__c0203` – «einen Selbstbehalt von 5% des Nettoeinkommens gemäss Ziffer 22»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0215.md) `tg-wl-2026__c0215` – «maximal 20% des Nettoeinkommens (Ziffer 22»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0114.md) `tg-wl-2026__c0114` – «je nach Höhe ihres Reineinkommens gemäss Ziffer 24 der Steuererklärung, kantonal Anspruch»

<a id="25-1-sozialabzug-kinder"></a>
### Ziff. 25.1 – Sozialabzug für Kinder: a) in Ausbildung Jg. 2001–2006 (Code 380); Jg. 2007–2010 (Code 382); b) übrige Kinder (Code 384)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien Kinder Seite 1 (Jahrgang, Ausbildung, Haushalt)
- **Rein:** Personalien (Kinder) → Jahrgang, Ausbildung/Erwerbsunfähigkeit, Unterhalt · Getrennte Eltern: Unterhaltsregelung → Alimente, Sorgerecht, Obhut (Zuteilung)
- **Rechnen:** Σ je Kind – Kanton: Ausbildung Jg. 2001–2006 10'600 (Code 380) / Jg. 2007–2010 8'500 (382) / übrige 7'400 (384); Bund 6'800 je Kind
- **Regel:** Pro nicht selbständig besteuertes, in Ausbildung stehendes oder erwerbsunfähiges eigenes Kind, für dessen Unterhalt aufgekommen wird (nicht Pflege-/Stiefkinder). Kanton: Jg. 2001–2006 in Ausbildung Fr. 10'600; Jg. 2007–2010 in Ausbildung Fr. 8'500; übrige Fr. 7'400. Bund einheitlich Fr. 6'800. Kein Abzug bei Kind mit selbständigem Lebensunterhalt. Stichtag 31.12.2026 (nicht pro rata). Getrennte Eltern: Zuteilung nach Alimenten/Sorgerecht/Obhut (Kanton und Bund unterschiedlich).
- **Beachten:** Stichtag 31. Dezember 2026, kein pro rata (nur bei unterjähriger Steuerpflicht anteilig); keine Pflege-/Stiefkinder
- **Beachten:** Kanton getrennt (minderjährig): Alimente-Empfänger; ohne Alimente hälftig nur bei gem. Sorge + alternierender Obhut
- **Beachten:** Bund: gem. Sorge ohne Alimente → hälftig; volljährige Kinder ungeteilt, i.d.R. an Unterhaltszahler
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 7'400 (Kinderabzug je Kind (nicht selbstaendig besteuert, in Ausbildung oder erwerbsunfaehig, Unterhalt wird getragen): Fr. 7'400 ('uebriges Kind'). Stichtag 31.12.2026. Zusaetzlich Steuergutschrift max. Fr. 100 pro minderjaehriges Kind mit der Schlussrechnung.)** · Bund **CHF 6'800 (Kinderabzug CHF 6'800 pro minderjähriges oder in beruflicher/schulischer Ausbildung stehendes Kind, für dessen Unterhalt die steuerpflichtige Person sorgt; bei getrennter Besteuerung der Eltern hälftig bei gemeinsamer elterlicher Sorge ohne Unterhaltsbeiträge.)**
  - Kinderabzug Vorschulalter (CHF): Kanton **n/a** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (Art. 35 Abs. 1 lit. a DBG), keine Staffelung nach Alter; siehe sozialabzug.kind.**
  - Kinderabzug Schulalter (CHF): Kanton **n/a** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800, keine Staffelung nach Alter; siehe sozialabzug.kind.**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 8'500 (Kind in Ausbildung nach Vollendung des 16. Altersjahres (WL 2026: Jahrgang 2007-2010): Fr. 8'500.)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Abzug CHF 6'800 (kein höherer Ausbildungsabzug beim Bund).)**
  - Kinder-Ausbildungsabzug Zusatz/Höherstufe (kantonal verschieden: SG zusätzlicher Ausbildungskostenabzug über Selbstbehalt; TG erhöhter Kinderabzug 20.–26. Altersjahr, ersetzt Grund-/16+-Abzug, nicht kumulativ – siehe Text) (CHF): Kanton **CHF 10'600 (Kind in Ausbildung nach Vollendung des 20. bis zum vollendeten 26. Altersjahr (WL 2026: Jahrgang 2001-2006): Fr. 10'600. Anstelle von sozialabzug.kind/kind_ausbildung (der Abzug «erhöht sich … auf»), nicht zusätzlich.)** · Bund **n/a – Bund: kein erhöhter Abzug für auswärtige Ausbildung; einheitlich CHF 6'800 (Art. 35 Abs. 1 lit. a DBG).**
- **Bund:** Bund Fr. 6'800 je Kind; Zuteilungsregeln bei getrennten Eltern weichen ab.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «25.1 a) für jedes Kind in Ausbildung mit Jahrg. 2001 – 2006 Fr. 10 600 Fr. 6800 380»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0107.md) `tg-wl-2026__c0107` – «für jedes Kind in Ausbildung mit Jahrgang 2007 – 2010 Fr. 8'500 Fr. 6'800»
  - [WL TG 2026 S. 23–24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0106.md) `tg-wl-2026__c0106` – «Für die Festsetzung der Sozialabzüge für Kinder und unterstützte Personen sind die Verhältnisse»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0108.md) `tg-wl-2026__c0108` – «Der Kinderabzug steht nur dem die zu versteuernden Unterhaltsbeiträge (Alimente)»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0109.md) `tg-wl-2026__c0109` – «sich das (minderjährige) Kind in alternierender Obhut beider Elternteile, erfolgt eine hälftige Teilung»
  - [WL TG 2026 S. 24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0111.md) `tg-wl-2026__c0111` – «Besteht ein gemeinsames Sorgerecht und fliessen keine Unterhaltsbeiträge»
  - [WL TG 2026 S. 24–25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0112.md) `tg-wl-2026__c0112` – «Bei volljährigen Kindern wird der Kinderabzug immer ungeteilt einem Elternteil zugesprochen.»

<a id="25-2-sozialabzug-unterstuetzung"></a>
### Ziff. 25.2 – Sozialabzug für jede unterstützte Person (Code 386)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Nachweis der Unterstützung (Zahlungsnachweise, Bestätigung)
- **Rein:** Zahlungsnachweise Unterstützung → Betrag je unterstützte Person · Angaben zur unterstützten Person → Erwerbsunfähigkeit, Bedürftigkeit
- **Rechnen:** Kanton 2'700 je Person, wenn Hauptunterhalt und Beitrag ≥ 50% des betreibungsrechtl. Existenzminimums; Bund 6'800, wenn Beitrag ≥ 6'800 → Code 386
- **Regel:** Kanton Fr. 2'700 bei Hauptunterhalt einer erwerbsunfähigen, unterstützungsbedürftigen Person (Kosten nachweislich ≥50% des betreibungsrechtlichen Existenzminimums). Bund Fr. 6'800 bei nachgewiesenem Beitrag von mindestens Fr. 6'800. Nicht für Ehegatte/Partner und Kinder mit Kinderabzug/Alimentenabzug.
- **Beachten:** Nicht für Ehegatte/Partner/in und Kinder mit Kinderabzug oder abgezogenen Unterhaltsbeiträgen
- **Beachten:** Kanton: erwerbsunfähig und unterstützungsbedürftig; Bund: erwerbsunfähig oder beschränkt erwerbsfähig
- **Beachten:** Stichtag 31. Dezember 2026; gleicher Haushalt + Hauptunterhalt → zusätzlich Ziff. 28.2 (Bund)
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'700 (Unterstuetzungsabzug je erwerbsunfaehige und unterstuetzungsbeduerftige Person (nicht Ehegatte/Kind mit Kinderabzug): Fr. 2'700; Voraussetzung: Beitrag zu mehr als 50 % des betreibungsrechtlichen Existenzminimums.)** · Bund **CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)**
- **Bund:** Bund Fr. 6'800.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «25.2 für jede unterstützte Person Fr. 2 700 Fr. 6800 386»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0113.md) `tg-wl-2026__c0113` – «dürftigen Person auf, können Sie kantonal Fr. 2 700 abziehen.»
  - [WL TG 2026 S. 23–24](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0106.md) `tg-wl-2026__c0106` – «Für die Festsetzung der Sozialabzüge für Kinder und unterstützte Personen sind die Verhältnisse»
  - [WL TG 2026 S. 25–26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0117.md) `tg-wl-2026__c0117` – «Personen, welche mit (eigenen) Kindern oder mit unterstützungsbedürftigen Personen im gleichen»

<a id="25-3-sozialabzug-alter-iv"></a>
### Ziff. 25.3 – Sozialabzug für Personen mit AHV-Altersrenten sowie erwerbsunfähige oder verwitwete Personen (Code 388) – nur Staatssteuer

- **Schlüssel:** `sozialabzug.alter_iv` (Abzug für Personen im AHV-Alter, erwerbsunfähig oder verwitwet (kantonal)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Reineinkommen Ziff. 24 (satzbestimmend) – Tabelle der Wegleitung
- **Rein:** Übertrag Ziff. 24 Reineinkommen (Spalte Staat) · Rentenstatus → AHV-Altersrente, Erwerbsunfähigkeit oder Verwitwung
- **Rechnen:** Kanton: 4'200 − 200 je volle 1'000 satzbestimmendes Reineinkommen (Ziff. 24) über 16'900 (allein) bzw. 24'300 (gemeinsam) → Code 388; Bund: kein Abzug
- **Regel:** Nur Kanton: gestaffelt nach satzbestimmendem Reineinkommen (Ziff. 24); maximal Fr. 4'200 (Alleinstehende bis Fr. 17'899, gemeinsam Besteuerte bis Fr. 25'299), danach in Stufen zu Fr. 200 abnehmend; kein Abzug ab Fr. 37'900 bzw. Fr. 45'300. Wegleitung-Tabelle exakt anwenden.
- **Beachten:** Kein Abzug ab Reineinkommen 37'900 (Alleinstehende) bzw. 45'300 (gemeinsam Besteuerte)
- **Beachten:** WL-Tabellenzeile «36'900–37'689» wohl Druckfehler (§ 36 StG: 200 bis unter 37'900) – Original WL S. 25 prüfen
- **Beachten:** Erwerbsunfähig = wegen körperlicher oder geistiger Gesundheit nicht arbeitsfähig
- **Limiten:**
  - Abzug AHV-Alter/erwerbsunfähig/verwitwet (CHF): Kanton **CHF 4'200 (Abzug fuer AHV-Altersrentner, Erwerbsunfaehige und Verwitwete (nur Kanton): max. Fr. 4'200; Reduktion um Fr. 200 je Fr. 1'000 Mehreinkommen ab Reineinkommen ueber Fr. 16'900 (Alleinstehende) bzw. Fr. 24'300 (Gemeinsam Besteuerte); kein Abzug ab Fr. 37'900 bzw. Fr. 45'300.)** · Bund **n/a – Kantonaler Abzug; die direkte Bundessteuer kennt keinen Abzug für AHV-Alter/Erwerbsunfähigkeit/Verwitwung (Art. 35 DBG).**
- **Bund:** Kein Abzug bei der direkten Bundessteuer.
- **Bemerkung:** Tabelle W c0115: Zeile «36'900–37'689» wirkt layout-/druckfehlerhaft (erwartet 37'899); Original-PDF prüfen.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «25.3 für Personen mit AHV-Altersrenten sowie erwerbsunfähige oder verwitwete Personen 388»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0115.md) `tg-wl-2026__c0115` – «37'900 u. mehr 45'300 u. mehr kein Abzug»
  - [StG TG § 36](../../chunks/tg/2025/tg-stg/tg-stg__par-36-t1.md) `tg-stg__par-36-t1` – «beträgt das Reineinkommen mehr als Fr. 16'900, bei Steuerpflichtigen in ungetrennter Ehe mehr als Fr. 24'300»
  - [StG TG § 36](../../chunks/tg/2025/tg-stg/tg-stg__par-36-t1.md) `tg-stg__par-36-t1` – «ermässigt sich der Abzug je Fr. 1'000 Mehreinkommen um Fr. 200»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0114.md) `tg-wl-2026__c0114` – «der körperlichen oder geistigen Gesundheit nicht in der Lage sind»

<a id="25-4-sozialabzug-verheiratete"></a>
### Ziff. 25.4 – Sozialabzug für gemeinsam besteuerte Personen (Code 390) – nur Bundessteuer

- **Schlüssel:** `sozialabzug.verheiratete` (Verheiratetenabzug (Bund)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand (Ehe/eingetragene Partnerschaft)
- **Rein:** Personalien → Zivilstand verheiratet / eingetragene Partnerschaft (gemeinsam besteuert)
- **Rechnen:** Bund: 2'800 je gemeinsam besteuertes Paar → Code 390; Kanton: kein Abzug
- **Regel:** Nur direkte Bundessteuer Fr. 2'800; bei den Staats- und Gemeindesteuern kein solcher Abzug.
- **Beachten:** Kanton berücksichtigt Ehe/Partnerschaft über Vollsplitting (Divisor 2) im Tarif statt Sozialabzug
- **Beachten:** Bund: nur rechtlich und tatsächlich ungetrennte Ehe/Partnerschaft
- **Limiten:**
  - Verheiratetenabzug (CHF, Bund): Kanton **n/a – WL 2026 c0116: 'Bei den Staats- und Gemeindesteuern kann dieser Abzug nicht geltend gemacht werden.'** · Bund **CHF 2'800 (Verheiratetenabzug CHF 2'800 für Ehepaare in rechtlich und tatsächlich ungetrennter Ehe.)**
- **Bund:** Fr. 2'800 nur Bund.
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «25.4 für gemeinsam besteuerte Personen 390»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0116.md) `tg-wl-2026__c0116` – «Sozialabzug von Fr. 2'800 tätigen.»
  - [WL TG 2026 S. 52](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0243.md) `tg-wl-2026__c0243` – «durch den Divisor 2 (Vollsplitting) zu teilen»

<a id="26-berechnung-total"></a>
### Ziff. 26 – Steuerbares Einkommen (Code 398)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 24 minus 25.1 bis 25.4)
- **Rein:** Übertrag Ziff. 25.1–25.4 Sozialabzüge (Codes 380–390)
- **Rechnen:** Ziff. 24 − Σ Ziff. 25.1 bis 25.4, getrennt Spalte Staat / Bund → Code 398
- **Regel:** Ergebnis getrennt für Staat und Bund; Basis für Tarif (Staat Vollsplitting Divisor 2 bei gemeinsam Besteuerten).
- **Beachten:** Staat: gemeinsam Besteuerte und Einelternfamilien Vollsplitting – satzbestimmend = Einkommen ÷ 2
- **Beachten:** Staat: einfache Steuer 0 bis 12'200, danach 2% … 8% (ab 158'400) × Steuerfuss Staat 109% plus Gemeindesteuerfüsse
- **Beachten:** Bund: Ermässigung 263 je Kind/unterstützte Person vom Steuerbetrag (Ziff. 28.2)
- **Limiten:**
  - Steuerfuss Kanton (%/Einheiten): Kanton **109 % (Staatssteuerfuss 2026: 109 % der einfachen Steuer (seit 2022 unveraendert). Gemeinde-, Schul- und Kirchensteuerfuesse je Gemeinde in tg-steuerfuesse-2026.)** · Bund **n/a – Kantonaler Steuerfuss; Bund hat einen eigenen Tarif (Art. 36 DBG) ohne Steuerfuss.**
  - Abzug vom Steuerbetrag pro Kind (CHF, Bund): Kanton **n/a – Kantonale Steuergutschrift Fr. 100: WL 2026 c0246 ('Steuergutschrift von maximal Fr. 100').** · Bund **CHF 263 (Ermässigung des Steuerbetrags um CHF 263 pro Kind oder unterstützungsbedürftige Person (Ehepaare sowie Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern/unterstützungsbedürftigen Personen im gleichen Haushalt, die deren Unterhalt zur Hauptsache bestreiten).)**
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «26. STEUERBARES EINKOMMEN (Ziffer 24 abzüglich Ziffern 25.1 bis 25.4) 398»
  - [WL TG 2026 S. 52](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0243.md) `tg-wl-2026__c0243` – «wird das Vollsplitting angewendet»
  - [WL TG 2026 S. 52](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0243.md) `tg-wl-2026__c0243` – «Fr. 10'133.00 für Fr. 158'400 und 8% für den Mehrbetrag»
  - [WL TG 2026 S. 52](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0243.md) `tg-wl-2026__c0243` – «Haushalt zusammenleben und deren Unterhalt zur Hauptsache bestreiten (Einelternfamilien), wird»

<a id="28-1-sozialabzug-kinder"></a>
### Ziff. 28.1 – Kanton: Steuergutschrift für minderjährige Kinder (Anzahl Kinder)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Anzahl Kinder mit Kinderabzug (minderjährig)
- **Rein:** Personalien (Kinder) → Anzahl minderjährige Kinder mit Kinderabzug (Ziff. 25.1)
- **Rechnen:** Eintrag: Anzahl minderjährige Kinder mit Kinderabzug; Kanton: Gutschrift = min(Anzahl × 100; Steuerbetrag), keine Auszahlung der Differenz
- **Regel:** Anzahl der minderjährigen Kinder eintragen, für die ein Kinderabzug geltend gemacht werden kann; Gutschrift max. Fr. 100 pro Kind mit der Schlussrechnung, keine Auszahlung über den Steuerbetrag hinaus.
- **Beachten:** Nur bei Wohnsitz im Kanton Thurgau und nur für minderjährige Kinder mit Kinderabzug
- **Beachten:** Gutschrift erfolgt mit der Schlussrechnung; Bund stattdessen Ziff. 28.2
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «28.1 Kanton: Steuergutschrift für minderjährige Kinder Anzahl Kinder»
  - [WL TG 2026 S. 25](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0116.md) `tg-wl-2026__c0116` – «gutschrift von maximal Fr. 100.»

<a id="28-2-sozialabzug-unterstuetzung"></a>
### Ziff. 28.2 – Bund: Ermässigung Steuerbetrag für Kinder und unterstützungsbedürftige Personen (Anzahl Personen)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Anzahl Kinder und unterstützte Personen im gleichen Haushalt (Elterntarif)
- **Rein:** Personalien (Kinder/unterstützte Personen) → Anzahl im gleichen Haushalt mit Unterhalt zur Hauptsache
- **Rechnen:** Eintrag: Anzahl Personen; Bund: Steuerbetrag − 263 × Anzahl Kinder/unterstützte Personen (Elterntarif)
- **Regel:** Bund: Abzug vom Steuerbetrag Fr. 263 pro Kind und/oder unterstützte Person bei Zusammenleben im gleichen Haushalt und überwiegender Unterhaltsleistung.
- **Beachten:** Nur bei Zusammenleben im gleichen Haushalt und überwiegender Unterhaltsleistung
- **Beachten:** Nicht anwendbar auf Kapitalleistungen aus Vorsorge
- **Beachten:** Kanton: keine Ermässigung, stattdessen Steuergutschrift Ziff. 28.1
- **Limiten:**
  - Abzug vom Steuerbetrag pro Kind (CHF, Bund): Kanton **n/a – Kantonale Steuergutschrift Fr. 100: WL 2026 c0246 ('Steuergutschrift von maximal Fr. 100').** · Bund **CHF 263 (Ermässigung des Steuerbetrags um CHF 263 pro Kind oder unterstützungsbedürftige Person (Ehepaare sowie Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern/unterstützungsbedürftigen Personen im gleichen Haushalt, die deren Unterhalt zur Hauptsache bestreiten).)**
- **Bund:** Fr. 263 je Kind/unterstützte Person (Elterntarif).
- **Quellen:**
  - [Formular 1 TG 2026 S. 3](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0013.md) `tg-form-01-2026__c0013` – «28.2 Bund: Ermässigung Steuerbetrag für Kinder und unterstützungsbedürftige Personen Anzahl Personen»
  - [WL TG 2026 S. 25–26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0117.md) `tg-wl-2026__c0117` – «Fr. 263 pro Kind und/oder pro unterstützte Person vom Steuerbetrag geltend machen.»
  - [WL TG 2026 S. 28–29](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0133.md) `tg-wl-2026__c0133` – «Der Elterntarif (vgl. Seite 55 der Wegleitung) findet bei Kapitalleistungen aus Vorsorge»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben (Formular 1 Code 410, Übertrag aus Formular 2)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 Total Steuerwerte (Ziff. 9); Steuerwerte per 31.12.2026
- **Rein:** Formular 2 Ziff. 9 → Total Steuerwert Privatvermögen (Code 410) · Steuer-/Depotauszug Bank → Steuerwerte und Kontosaldi per 31.12.2026 · ESTV-Kursliste → Kurse und Devisenkurse Ende Dezember 2026
- **Rechnen:** Formular 2: Ziff. 5 (Σ Steuerwerte = Verkehrswerte; kotiert Kurs Ende Dez. 2026, Ausland × ESTV-Devisenkurs) − Ziff. 6 Geschäftswertschriften = Ziff. 9 → Code 410
- **Regel:** Steuerwert = Verkehrswert; kotierte CH-Titel Börsenkurs Ende Dezember 2026, Auslandtitel Kurs Ende Dezember in CHF gemäss ESTV-Kursliste. PK-/Freizügigkeitsguthaben und nicht fällige 3a-Guthaben nicht deklarieren. Vermögen und Erträge der Kinder Jg. 2008 und jünger sind mitzudeklarieren.
- **Beachten:** PK-, Freizügigkeits- und nicht fällige 3a-Guthaben nicht deklarieren
- **Beachten:** Nicht kotiert: Verkehrswert 31. Dezember 2026, ersatzweise Wert per 1. Januar 2026
- **Beachten:** Kindervermögen: WL Formular 2 nennt «Jg. 2008 u. jünger», WL «Mündigkeit» Jg. 2008 ab 2026 selbständig → prüfen
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.1 Wertschriften und Guthaben Formular 2 410»
  - [WL TG 2026 S. 30–31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0143.md) `tg-wl-2026__c0143` – «Für in der Schweiz kotierte Wertpapiere gilt der Börsenkurs Ende des Monats Dezember 2026.»
  - [WL TG 2026 S. 30](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0140.md) `tg-wl-2026__c0140` – «Vermögen und Erträge von Kindern unter Ihrer elterlichen Sorge (Jahrgang 2008 und jünger)»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0162.md) `tg-wl-2026__c0162` – «Steuerwerte von Wertschriften und Guthaben im Privatvermögen übertragen Sie in Ziffer 30.1»
  - [WL TG 2026 S. 31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0144.md) `tg-wl-2026__c0144` – «Für nicht kotierte Wertpapiere gilt der Verkehrswert per 31. Dezember 2026.»
  - [WL TG 2026 S. 6](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0012.md) `tg-wl-2026__c0012` – «Personen mit Jahrgang 2008 sind somit für die Steuerperiode 2026 erstmals selbständig deklarationspflichtig.»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 412)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bestandesaufstellung per 31.12.2026; Kursliste ESTV
- **Rein:** Bestandesaufstellung Bargeld/Edelmetalle → Bestand per 31. Dezember 2026 · Amtliche Kursliste ESTV → Devisen- und Edelmetallkurse per 31. Dezember 2026
- **Rechnen:** CHF-Bargeld (Bestand) + Σ Fremdwährung, Gold, Edelmetalle × Kurs amtliche Kursliste per 31. Dezember 2026 → Code 412
- **Regel:** Inländisches Bargeld mit Bestand 31.12.2026; ausländisches Bargeld, Gold und Edelmetalle zum Verkehrswert 31.12.2026 (amtliche Kursliste).
- **Beachten:** Guthaben (Konti) gehören ins Formular 2 (Ziff. 30.1), nicht hierher
- **Beachten:** Kursliste ESTV jeweils im Februar des Folgejahres verfügbar
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.2 Bargeld, Gold und andere Edelmetalle 412»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0120.md) `tg-wl-2026__c0120` – «Inländisches Bargeld ist mit dem Bestand per 31. Dezember 2026 aufzuführen.»
  - [WL TG 2026 S. 30–31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0143.md) `tg-wl-2026__c0143` – «Diese Kurslisten sind jeweils im Februar des Folgejahres auf der Homepage der EStV»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen – Rückkaufswert inkl. Überschussguthaben (Code 420)

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Bescheinigung des Versicherers per 31.12.2026 (Steuerwert/Rückkaufswert)
- **Rein:** Steuerbescheinigung Versicherer per 31. Dezember 2026 → Steuerwert (Rückkaufswert inkl. Überschuss) · Police → Gesellschaft, Abschluss-/Ablaufjahr, Versicherungssumme
- **Rechnen:** Σ je Police: Rückkaufswert + Überschuss- und Gewinnanteile per 31. Dezember 2026 → Code 420
- **Regel:** Rückkaufswert inkl. Überschuss- und Gewinnanteile; auch Rentenversicherungen während der Rentenlaufzeit. Gesellschaft, Abschluss-/Ablaufjahr, Versicherungssumme und Steuerwert eintragen; Bescheinigung beilegen.
- **Beachten:** Rentenversicherungen auch während der Rentenlaufzeit deklarieren
- **Beachten:** Nicht fällige 3a-Ansprüche und nicht rückkaufsfähige Anwartschaften sind steuerfrei
- **Beachten:** Bescheinigungen der Versicherer der Steuererklärung beilegen
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.3 Lebens- und Rentenversicherungen (Rückkaufswert inkl. Überschussguthaben)»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0121.md) `tg-wl-2026__c0121` – «Kapital- und Rentenversicherungen unterliegen mit ihrem Steuerwert (Rückkaufswert inkl. Über-»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0118.md) `tg-wl-2026__c0118` – «nicht fällige Ansprüche aus anerkannten Formen der gebundenen Selbstvorsorge (Säule 3a)»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge – Marke, Kaufpreis, Anschaffungsjahr (Code 422)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg, Motorfahrzeug-Versicherungspolice (Haftpflicht/Kasko) und Verkehrssteuer-Rechnung → Kaufvertrag/Fahrzeugausweis (Kaufpreis, Anschaffungsjahr)
- **Rein:** Kaufvertrag/Fahrzeugausweis → Fahrzeugtyp, Kaufpreis, Anschaffungsjahr
- **Rechnen:** Kaufpreis − 20% des Kaufpreises je Jahr seit Erwerb (Verkehrswert 31.12.2026); Kauf vor > 5 Jahren → Fr. 1.– → Code 422
- **Regel:** Verkehrswert 31.12.2026: Wertverminderung 20% vom Kaufpreis pro Jahr seit Erwerb; vor mehr als 5 Jahren gekaufte Fahrzeuge pro memoria Fr. 1.–. Geleaste Fahrzeuge nicht deklarieren. Oldtimer/Liebhaberfahrzeuge unter Ziff. 30.6.
- **Beachten:** Geleaste Fahrzeuge nicht deklarieren
- **Beachten:** Oldtimer und Liebhaberfahrzeuge zum Verkehrswert unter Ziff. 30.6
- **Beachten:** Geschäftsfahrzeuge Selbständiger: Ziff. 32.5 Anlagevermögen
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.4 Motorfahrzeuge Steuerwert Fr.»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0122.md) `tg-wl-2026__c0122` – «Fahrzeuge die vor mehr als 5 Jahren gekauft»
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0015.md) `tg-form-01-2026__c0015` – «32.5 Anlagevermögen ohne Grundeigentum (Fahrzeuge, Maschinen/Mobiliar usw.)»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Anteile an unverteilten Erbschaften (Formular 3, Code 424)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung der Erbengemeinschaft/Formular 3
- **Rein:** Formular 3 / Aufstellung Erbengemeinschaft → Vermögen der Erbschaft und Erbquote
- **Rechnen:** Erbquote × Vermögen der unverteilten Erbschaft per 31. Dezember 2026 → Code 424; Ertragsanteil → Ziff. 5.3
- **Regel:** Anteil am Erbschaftsvermögen quotenmässig; analog Ertrag in Ziff. 5.3.
- **Beachten:** Steuerpflicht für den Erbanteil beginnt am Folgetag des Todestags
- **Beachten:** Erbschaft zusätzlich auf Seite 4 «Schenkungen und erbrechtliche Vermögensanfälle» aufführen
- **Beachten:** Nutzniessung: Vermögen wird der nutzniessenden Person zugerechnet
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.5 Anteile an unverteilten Erbschaften Formular 3 424»
  - [WL TG 2026 S. 26–27](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0123.md) `tg-wl-2026__c0123` – «Die Anteile an unverteilten Erbschaften und Nutzniessungen werden den einzelnen erbenden oder»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0080.md) `tg-wl-2026__c0080` – «Einkünfte aus unverteilten Erbschaften werden den erbenden Personen entsprechend ihrer»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0080.md) `tg-wl-2026__c0080` – «bereits ab dem Folgetag des Todestags der Erblasserin/des Erblassers beginnt»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0118.md) `tg-wl-2026__c0118` – «Vermögensstand am 31. Dezember 2026 bzw. am Ende der Steuerpflicht»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0129.md) `tg-wl-2026__c0129` – «Bitte führen Sie hier auch Vermögensanfälle aus Erbschaften auf.»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte – nähere Bezeichnung (Code 426)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung mit Verkehrswerten per 31.12.2026
- **Rein:** Kaufbelege/Schätzungen → Verkehrswert je Objekt per 31.12. · Eigene Aufstellung → nähere Bezeichnung der Objekte
- **Rechnen:** Σ Verkehrswerte per 31.12. der näher bezeichneten Objekte (z.B. Wohnmobil, Boot, Kunst, Schmuck, Sammlung, Patent) → Code 426
- **Regel:** Z.B. Wohnwagen, Wohnmobile, Oldtimer, Boote, Reitpferde, Kunst, Schmuck, Sammlungen, Patente: näher bezeichnen und zum Verkehrswert deklarieren. Hausrat ist steuerfrei.
- **Beachten:** Hausrat ist von der Vermögenssteuer befreit – nicht deklarieren
- **Beachten:** Oldtimer/Liebhaberfahrzeuge hier, nicht unter Ziff. 30.4
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.6 Übrige Vermögenswerte, nähere Bezeichnung: 426»
  - [WL TG 2026 S. 26–27](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0123.md) `tg-wl-2026__c0123` – «Unter die übrigen Vermögenswerte fallen z.B. Wohnwagen, Wohnmobile, Oldtimer, Liebhaberfahr-»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0118.md) `tg-wl-2026__c0118` – «Der Hausrat ist von der Vermögenssteuer befreit.»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0122.md) `tg-wl-2026__c0122` – «Oldtimer und Liebhaberfahrzeuge sind zum Verkehrswert unter der Ziffer 30.6»

<a id="31-vermoegen-liegenschaften"></a>
### Ziff. 31 – Liegenschaften (Formular 7, Code 430)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Formular 7 Total Steuerwerte; Liegenschaftensteuerrechnung/Schätzung
- **Rein:** Formular 7 → Total Steuerwerte (Code 430) · Liegenschaftensteuerrechnung TG (Versand Januar 2027) → amtlicher Verkehrswert · Steuerwertangabe anderer Kanton/Ausland → dortiger Steuerwert
- **Rechnen:** Σ Steuerwerte Formular 7: nichtlandwirtschaftlich amtlicher Verkehrswert, landwirtschaftlich Ertragswert (rechtskräftig Ende Steuerperiode) → Code 430
- **Regel:** Amtlicher Verkehrswert (rechtskräftig am Ende der Steuerperiode); landwirtschaftliche Liegenschaften Ertragswert; ausserkantonale/ausländische Liegenschaften zum dortigen Steuerwert (Repartitionswert durch Behörde). Noch nicht geschätzte Bauten/Umbauten angemessen berücksichtigen.
- **Beachten:** Ausserkantonal/Ausland: dortiger Steuerwert; Behörde passt an (Repartitionswert)
- **Beachten:** Nicht abgeschlossene Bauten/Umbauten: noch nicht geschätzte Investitionen angemessen deklarieren
- **Beachten:** Zugang/Wegfall in der Steuerperiode (Kauf, Verkauf, Schenkung, Erbgang) mit genauem Datum im Formular 7
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0015.md) `tg-form-01-2026__c0015` – «31. Liegenschaften Formular 7 430»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0236.md) `tg-wl-2026__c0236` – «Für nichtlandwirtschaftliche Liegenschaften geben Sie den am Ende der Steuerperiode bzw. der»
  - [WL TG 2026 S. 51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0238.md) `tg-wl-2026__c0238` – «(infolge Kauf, Verkauf, Schenkung oder Erbgang), deklarieren Sie bitte das genaue»
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0003.md) `tg-form-07-2026__c0003` – «Total Steuerwerte 430»

<a id="32-vermoegen-uebrige"></a>
### Ziff. 32 – Betriebsvermögen selbständig erwerbender Personen: Geschäftskapital Kollektiv-/Kommanditgesellschaft (Code 440), Total Geschäftsvermögen (Code 442)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz / Bescheinigung der Gesellschaft über Vermögensanteil
- **Rein:** Bilanz/Aufstellung Aktiven und Passiven (unterzeichnet) → Ziff. 32.2–32.5 bzw. Total · Bescheinigung Kollektiv-/Kommanditgesellschaft → Anteil Geschäftskapital (Code 440)
- **Rechnen:** 32.1 Anteil Geschäftskapital Kollektiv-/Kommanditges. → Code 440; 32.6 = Σ 32.2 bis 32.5 oder Total lt. Bilanz → Code 442
- **Regel:** Angaben 32.2–32.5 (Bankkonti/Wertschriften/Debitoren, Vorräte, Viehhabe, Anlagevermögen ohne Grundeigentum) oder Total lt. Bilanz in Ziff. 32.6; Geschäftsvermögen zu Verkehrswerten. Bei Kollektiv-/Kommanditgesellschaft persönlicher Anteil; Bescheinigung der Gesellschaft beilegen.
- **Beachten:** Bewertung: Wertschriften Bilanzwert; Debitoren voll (Verlust glaubhaft machen); Vorräte min(Kosten; Marktpreis)
- **Beachten:** Anlagevermögen zum Verkehrswert (Anschaffungswert − Abschreibung); Liegenschaften nur Ziff. 31
- **Beachten:** Präponderanz: > 50% geschäftlich genutzt → ganz Geschäftsvermögen; Geschäftsschulden Formular 4.1 B
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0015.md) `tg-form-01-2026__c0015` – «32.6 Total Geschäftsvermögen (Ziffern 32.2 bis 32.5) oder lt. Bilanz»
  - [WL TG 2026 S. 27](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0124.md) `tg-wl-2026__c0124` – «Kollektiv- und Kommanditgesellschaften werden nicht als Einheit besteuert.»
  - [WL TG 2026 S. 27](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0125.md) `tg-wl-2026__c0125` – «also zum bilanzierten Wert. Im Übrigen sind die unter Ziffer 31 aufgeführten»
  - [WL TG 2026 S. 27](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0125.md) `tg-wl-2026__c0125` – «zu den Anschaffungs- bzw. Herstellungskosten oder, wenn der»
  - [WL TG 2026 S. 27](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0126.md) `tg-wl-2026__c0126` – «Setzen Sie das Anlagevermögen wie Maschinen, Werkzeuge, Mobilien oder Fahrzeuge mit dem»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0119.md) `tg-wl-2026__c0119` – «die demnach überwiegend (mehr als 50%) der selbständigen»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0169.md) `tg-wl-2026__c0169` – «Deklarieren Sie Schulden und Schuldzinsen aufgeteilt in Privatschulden (unter A)»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 464)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 30.1 bis 32.6)
- **Rein:** Übertrag Ziff. 30.1–30.6, 31, 32.1 und 32.6
- **Rechnen:** Σ Codes 410 + 412 + 420 + 422 + 424 + 426 + 430 + 440 + 442 (Ziff. 32.2–32.5 nur via 32.6) → Code 464
- **Regel:** Summe aller Vermögenswerte vor Schulden (nur Staatssteuer; Vermögen wird nur kantonal besteuert).
- **Beachten:** Nur Staatssteuer; Stichtag 31. Dezember 2026 bzw. Ende der Steuerpflicht
- **Beachten:** Vermögen beider Ehegatten/Partner und der Kinder unter elterlicher Sorge einbeziehen
- **Beachten:** Hausrat, Anwartschaften 2. Säule und nicht fällige 3a-Ansprüche steuerfrei
- **Bund:** Kein Vermögen bei der direkten Bundessteuer.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0015.md) `tg-form-01-2026__c0015` – «33. Total der Vermögenswerte (Ziffern 30.1 bis 32.6) 464»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0118.md) `tg-wl-2026__c0118` – «Das Vermögen wird nur kantonal besteuert.»
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0014.md) `tg-form-01-2026__c0014` – «30.1 Wertschriften und Guthaben Formular 2 410»

<a id="34-schulden-privat"></a>
### Ziff. 34 – Schulden (Formular 4.1, Code 466)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Leasingvertrag Fahrzeug / Leasingraten-Abrechnung → Formular 4.1 Total Privat- und Geschäftsschulden (Zusammenzug C, Code 466)
- **Rein:** Formular 4.1 C → Total Privat- und Geschäftsschulden (Code 466) · Hypotheken-/Darlehens-/Kreditausweis → Schuld per 31. Dezember 2026, Zinssatz, Gläubiger/in
- **Rechnen:** Code 466 = Code 455 (A Privatschulden) + Code 460 (B Geschäftsschulden), Stand 31. Dezember 2026
- **Regel:** Schuldenstand am 31.12.2026 mit Gläubiger/in (genaue Adresse) und Zinssatz; Privat- (A) und Geschäftsschulden (B) getrennt. Rentenverpflichtungen mit Barwert, wenn entgeltlich zugesichert.
- **Beachten:** Gläubiger/in mit genauer Adresse und Zinssatz angeben (unerlässlich)
- **Beachten:** Schuldzinsen (Code 290) separat in Ziff. 11 übertragen; nur 2026 fällige Zinsen
- **Beachten:** Rentenverpflichtungen mit Barwert, wenn entgeltlich zugesichert; nur Schulden mit eigener Haftung
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0015.md) `tg-form-01-2026__c0015` – «34. Schulden Formular 4.1 466»
  - [WL TG 2026 S. 27](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0127.md) `tg-wl-2026__c0127` – «Übertragen Sie das Total der Schulden in die Steuerer-»
  - [Formular 4.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-1-2026/tg-form-04-1-2026__c0003.md) `tg-form-04-1-2026__c0003` – «Total Privat- und Geschäftsschulden 466 290»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0169.md) `tg-wl-2026__c0169` – «Unerlässlich ist insbesondere die Angabe der Gläubigerin bzw. des Gläubigers»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0170.md) `tg-wl-2026__c0170` – «Tragen Sie nur die im Jahre 2026 fällig gewordenen Schuldzinsen ein (keine Ratazinsen).»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «Rentenverpflichtungen werden mit dem jeweiligen Barwert der Rente als Schuld»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Reinvermögen (Code 468)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 33 minus 34)
- **Rein:** Übertrag Ziff. 33 (Code 464) und Ziff. 34 (Code 466)
- **Rechnen:** Ziff. 33 − Ziff. 34 → Code 468
- **Regel:** Ziff. 33 abzüglich Ziff. 34.
- **Beachten:** Nur Staatssteuer (Vermögen wird nur kantonal besteuert)
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0015.md) `tg-form-01-2026__c0015` – «35. Reinvermögen (Ziffer 33 abzüglich Ziffer 34) 468»
  - [WL TG 2026 S. 26](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0118.md) `tg-wl-2026__c0118` – «Das Vermögen wird nur kantonal besteuert.»

<a id="36-1-vermoegen-sozialabzug"></a>
### Ziff. 36.1 – Abzug für gemeinsam besteuerte Personen Fr. 200'000 (Code 470)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien Seite 1 (Stand 31.12.2026)
- **Rechnen:** 200'000 in voller Höhe (Code 470)
- **Regel:** Steuerfreier Betrag für gemeinsam besteuerte Personen, Verhältnisse am 31.12.2026.
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 200'000 (Steuerfreier Betrag Vermoegenssteuer: Fr. 200'000 fuer Steuerpflichtige in ungetrennter Ehe/Partnerschaft.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
- **Bund:** Kein Vermögenssteuerabzug bei der direkten Bundessteuer.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0016.md) `tg-form-01-2026__c0016` – «36.1 Abzug für gemeinsam besteuerte Personen (Eheleute / Partnerinnen oder Partner) Fr. 200000 470»

<a id="36-2-vermoegen-sozialabzug"></a>
### Ziff. 36.2 – Abzug für alleinstehende Personen Fr. 100'000 (Code 472)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien Seite 1 (Stand 31.12.2026)
- **Rechnen:** 100'000 in voller Höhe (Code 472)
- **Regel:** Steuerfreier Betrag für Alleinstehende, Verhältnisse am 31.12.2026.
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 100'000 (Steuerfreier Betrag Vermoegenssteuer: Fr. 100'000 fuer alle uebrigen Steuerpflichtigen (ledig, getrennt, geschieden, verwitwet). Stichtag 31.12.2026.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
- **Bund:** Kein Vermögenssteuerabzug bei der direkten Bundessteuer.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0016.md) `tg-form-01-2026__c0016` – «36.2 Abzug für alleinstehende Personen Fr. 100000 472»

<a id="36-3-vermoegen-sozialabzug"></a>
### Ziff. 36.3 – Abzug für jedes nicht selbständig besteuerte Kind (Jg. 2009 und jünger) Fr. 100'000 (Code 474)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Kinder (Jahrgang) Seite 1
- **Rechnen:** 100'000 × Kinder Jg. 2009 und jünger (eigene Zeile, Code 474)
- **Regel:** Fr. 100'000 je nicht selbständig besteuertes Kind Jg. 2009 und jünger; bei getrennt besteuerten Eltern erhält ihn der Elternteil mit dem Kinderabzug (hälftig nur bei gemeinsamem Sorgerecht, keinen Unterhaltsbeiträgen und alternierender Obhut). Kinder Jg. 2008 sind 2026 selbständig steuerpflichtig.
- **Limiten:**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 100'000 (Zusaetzlich Fr. 100'000 je nicht selbstaendig besteuertes Kind (WL 2026: Jahrgang 2009 und juenger). Bei getrennt besteuerten Eltern Zuteilung wie Kinderabzug; haelftig bei gemeinsamem Sorgerecht und alternierender Obhut ohne Alimente.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
- **Bund:** Kein Vermögenssteuerabzug bei der direkten Bundessteuer.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0016.md) `tg-form-01-2026__c0016` – «36.3 Abzug für jedes nicht selbständig besteuerte Kind (Jahrgang 2009 und jüngere) Fr. 100000 474»
  - [WL TG 2026 S. 27–28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0128.md) `tg-wl-2026__c0128` – «– für jedes nicht selbständig besteuerte Kind (Jahrgang 2009 und jünger) Fr. 100'000»
  - [WL TG 2026 S. 6](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0012.md) `tg-wl-2026__c0012` – «Personen mit Jahrgang 2008 sind somit für die Steuerperiode 2026 erstmals selbständig deklarationspflichtig.»
  - [WL TG 2026 S. 27–28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0128.md) `tg-wl-2026__c0128` – «Die Eltern können für ihre mündigen Kinder»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen gesamt (Code 498)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 35 minus 36.1 bis 36.3)
- **Rein:** Übertrag Ziff. 35 und Ziff. 36.1–36.3 (Codes 470–474)
- **Rechnen:** Ziff. 35 − Σ Ziff. 36.1 bis 36.3 → Code 498; einfache Vermögenssteuer = 1,1‰ × Ziff. 37, × Steuerfuss (Staat 109% + Gemeinde)
- **Regel:** Ergebnis ist Basis der Vermögenssteuer.
- **Beachten:** Erbschaft ≥ 50'000 im Steuerjahr: Zuwachs erst ab Erbanfall besteuert (nicht bei Schenkung/Erbvorbezug)
- **Beachten:** Nur Staatssteuer; Bund: kein Vermögen
- **Limiten:**
  - Steuerfuss Kanton (%/Einheiten): Kanton **109 % (Staatssteuerfuss 2026: 109 % der einfachen Steuer (seit 2022 unveraendert). Gemeinde-, Schul- und Kirchensteuerfuesse je Gemeinde in tg-steuerfuesse-2026.)** · Bund **n/a – Kantonaler Steuerfuss; Bund hat einen eigenen Tarif (Art. 36 DBG) ohne Steuerfuss.**
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0016.md) `tg-form-01-2026__c0016` – «37. STEUERBARES VERMÖGEN GESAMT (Ziffer 35 abzüglich Ziffern 36.1 bis 36.3) 498»
  - [WL TG 2026 S. 52–53](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0246.md) `tg-wl-2026__c0246` – «Die einfache Steuer beträgt für das gesamte steuerbare Vermögen einheitlich 1,1 Promille.»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0130.md) `tg-wl-2026__c0130` – «punkt des Erbanfalls an (und nicht während der ganzen Steuerperiode) besteuert.»

## Weitere Angaben

<a id="s-4-schenkungen-info-schenkungen-erbschaften"></a>
### Ziff. S. 4 Schenkungen – Schenkungen und erbrechtliche Vermögensanfälle (erhalten/ausgerichtet)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Schenkungsvertrag, Erbteilung, Erbvorbezugsvertrag
- **Rein:** Schenkungs-/Erbvorbezugsvertrag → Datum, Wert, Geber/in bzw. Empfänger/in · Erbschaftsunterlagen (auch unverteilte Erbschaft) → Erbanfall, Wert, Erblasser/in
- **Rechnen:** Je Vorgang: Datum, Wert Fr., Name/Adresse/Verwandtschaftsgrad von Geber/in bzw. Empfänger/in; «erhalten» und «ausgerichtet» getrennt
- **Regel:** Sämtliche 2026 erhaltenen oder ausgerichteten Schenkungen/Erbvorbezüge/Erbschaften mit Datum, Betrag, Geber/Empfänger inkl. Adresse und Verwandtschaftsgrad aufführen (auch unverteilte Erbschaften). Hilfsblätter auf der Homepage der Steuerverwaltung.
- **Beachten:** Auch unverteilte Erbschaften: Steuerpflicht ab Folgetag des Todestags der erblassenden Person
- **Beachten:** Erbschaft ≥ 50'000: Vermögenszuwachs erst ab Erbanfall besteuert (nicht Schenkung/Erbvorbezug)
- **Beachten:** Mehrere Vorgänge: Hilfsblätter (Homepage, «jahresunabhängige Formulare»; in eFisc2026 integriert)
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0017.md) `tg-form-01-2026__c0017` – «Schenkungen und erbrechtliche Vermögensanfälle»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0129.md) `tg-wl-2026__c0129` – «Führen Sie sämtliche im Jahre 2026 getätigten oder empfangenen Schenkungen und Erbvorbezüge»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0130.md) `tg-wl-2026__c0130` – «Bei Vermögensanfall aus Erbschaft (nicht jedoch infolge Schenkung oder Erbvorbezug)»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0130.md) `tg-wl-2026__c0130` – «stehen Ihnen die Hilfsblätter dort zur Verfügung, weshalb diesfalls kein Download notwendig ist.»

<a id="s-4-kapitalleistungen-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. S. 4 Kapitalleistungen – Kapitalleistungen aus Vorsorge 2026 (AHV/IV, Säule 2, Freizügigkeit, Säule 3a, Tod/Nachteile)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung (Betrag, Auszahlungsdatum, Art)
- **Rein:** Bescheinigung Vorsorgeeinrichtung (PK, Freizügigkeit, Säule 3a, AHV/IV) → Betrag, Auszahlungsdatum, Art · Abrechnung Unfall-/Haftpflichtversicherung → Kapital bei Tod oder bleibenden Nachteilen
- **Rechnen:** Kanton: einfache Steuer = Leistung × 2% (gemeinsam Besteuerte) bzw. 2,4% (übrige) × Steuerfuss; Bund: 1/5 des Tarifs Art. 36 DBG
- **Regel:** Quelle ankreuzen, Auszahlungsdatum und Betrag in ganzen Franken angeben; bei mehreren Leistungen Aufstellung einreichen. Immer zu 100% steuerbar, getrennt vom übrigen Einkommen besteuert (nicht in Ziff. 5.5!). Einfache Steuer Kanton: 2% (gemeinsam Besteuerte) bzw. 2,4% (Alleinstehende); Bund: 1/5 des ordentlichen Tarifs, kein Elterntarif.
- **Beachten:** Nicht in Ziff. 5.5, sondern Seite 4 unten; 100% steuerbar; mehrere Leistungen → Aufstellung
- **Beachten:** Keine Sozialabzüge; Satz nach Verhältnissen Ende Steuerperiode; Bund ohne Elterntarif
- **Beachten:** Genugtuung bleibt steuerfrei (WL-Beispiel, § 26 Ziff. 10 StG)
- **Bund:** 1/5 des ordentlichen Bundestarifs; Elterntarif nicht anwendbar.
- **Quellen:**
  - [Formular 1 TG 2026 S. 4](../../chunks/tg/2026/tg-form-01-2026/tg-form-01-2026__c0018.md) `tg-form-01-2026__c0018` – «Kapitalleistungen aus Vorsorge 2026»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0131.md) `tg-wl-2026__c0131` – «Bei Alleinstehenden beträgt der einheitliche Satz für die einfache Steuer 2,4%.»
  - [WL TG 2026 S. 28–29](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0133.md) `tg-wl-2026__c0133` – «Bei der direkten Bundessteuer beträgt die Steuer auf Kapitalleistungen aus Vorsorge 1/5 des or-»
  - [WL TG 2026 S. 19](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0083.md) `tg-wl-2026__c0083` – «Nicht in Ziffer 5.5, sondern auf der Steuererklärung, Seite 4 unten»
  - [StG TG § 39](../../chunks/tg/2025/tg-stg/tg-stg__par-39.md) `tg-stg__par-39` – «Die Sozialabzüge gemäss § 36 werden nicht gewährt.»
  - [TG FAQ NP](../../chunks/tg/dauernd/tg-info-faq/tg-info-faq__c0062.md) `tg-info-faq__c0062` – «Massgebend für den anzuwendenden Steuersatz sind die Verhältnisse am Ende der Steuerperiode oder am Ende der Steuerpflicht.»
  - [DBG Art. 38](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-38.md) `bund-dbg-2026__art-38` – «Sie wird zu einem Fünftel der Tarife nach Artikel 36 Absätze 1, 2 und 2bis erster Satz berechnet.»
  - [WL TG 2026 S. 28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0132.md) `tg-wl-2026__c0132` – «bleibt gemäss § 26 Ziffer 10 des Gesetzes über die Staats- und»

<a id="s-2-frist-verfahren-einreichung"></a>
### Ziff. S. 2 Frist – Einreichefrist und Fristerstreckung (Treuhänder)

- **Schlüssel:** `verfahren.einreichung` (Einreichung, Unterschrift, Beilagen, Fristen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Fristerstreckungsgesuch an das Gemeindesteueramt
- **Rein:** Formular 1 → vorgedrucktes Einreichedatum · Fristerstreckungsgesuch → schriftlich, begründet, rechtzeitig an Gemeindesteueramt
- **Rechnen:** Frist = vorgedrucktes Datum; Erstgesuch bis 30. September, weitere begründet bis 30. November; Treuhänder für Mandanten bis 31. Dezember des Deklarationsjahres
- **Regel:** Steuererklärung und Hilfsblätter bis zum vorgedruckten Datum beim Gemeindesteueramt einreichen; Fristverlängerung vorgängig, schriftlich und begründet beantragen. Erstes Gesuch grundsätzlich bis 30. September des Deklarationsjahres, weitere in begründeten Fällen bis 30. November; Treuhänder/Steuerberater können für Mandanten längstens bis 31. Dezember des Deklarationsjahres beantragen (Deklarationsjahr = Jahr der Einreichung).
- **Beachten:** Erstgesuch gebührenfrei, jedes weitere Gesuch Fr. 30 Kanzleigebühr (§ 39b StV TG)
- **Beachten:** Arbeitsüberlastung ist kein Grund; nach 30. November nur ausserordentliche, substanziiert dargelegte Gründe
- **Beachten:** Ausserkantonale: Einreichung bei der Liegenschafts- bzw. Betriebsstättengemeinde
- **Limiten:**
  - Fristerstreckung – Regel (Private / Treuhänder), Kosten: Kanton **Gesuch (schriftlich, begruendet, rechtzeitig) an das Gemeindesteueramt. Private: Erstgesuch bis max. 30. September des Deklarationsjahres; weitere Gesuche in begruendeten Faellen bis max. 30. November. Arbeitsueberlastung ist kein Grund. Treuhaender/Steuerberater, die gewerbsmaessig Steuererklaerungen ausfuellen: fuer ihre Mandanten bis max. 31. Dezember des Deklarationsjahres. Weitergehende Gesuche nur bei ausserordentlichen Gruenden.** · Bund **n/a – Kantonale Regelung; DBG nennt keine Frist/Erstreckungsgebühr (Einreichung über kantonale Steuererklärung).**
- **Bemerkung:** Fristen aus StP 155 Nr. 2 (jahresunabhängige Praxis, gültig für 2025 und 2026).
- **Quellen:**
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md) `tg-stp-155-2__c0001` – «längstens bis am 30. September des Deklarationsjahres»
  - [StP 155 Nr. 2](../../chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0002.md) `tg-stp-155-2__c0002` – «längstens bis zum 31. Dezember des Deklarationsjahres»
  - [WL TG 2026 S. 7–8](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0022.md) `tg-wl-2026__c0022` – «Die ausgefüllte Steuererklärung und die Hilfsblätter sind bis zum vorgedruckten Datum dem»
  - [StV TG § 39b](../../chunks/tg/2025/tg-stv/tg-stv__par-39b.md) `tg-stv__par-39b` – «Die erstmalige Fristerstreckung ist gebührenfrei.»
  - [StV TG § 39b](../../chunks/tg/2025/tg-stv/tg-stv__par-39b.md) `tg-stv__par-39b` – «Für jedes weitere Fristerstreckungsgesuch wird eine Kanzleigebühr von Fr. 30 erhoben.»

## Hilfsblatt Berufskosten (Form. 4.2 Person 1 / 4.3 Person 2)

<a id="form-4-2-ziff-1-1-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4.2 Ziff. 1.1 – Allgemeine Angaben: Arbeitgeber, Arbeitsort, Dauer der Erwerbstätigkeit, Arbeitspensum in %

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis (Arbeitgeber, Dauer), Arbeitsvertrag (Pensum)
- **Rein:** Lohnausweis → Arbeitgeber, Bst. E Lohnperiode (Ein-/Austrittsdaten) · Arbeitsvertrag/Bestätigung Arbeitgeber → Arbeitspensum in %
- **Rechnen:** Jahrespauschale × Erwerbstage / 360 bei unterjähriger Erwerbstätigkeit (z.B. 3'200 × 270 / 360 = 2'400); Basis 225 Arbeitstage bei 100%
- **Regel:** Pauschalen gelten für das ganze Jahr und sind bei unterjähriger Erwerbstätigkeit auf die Dauer umzurechnen; bei Teilzeit Kürzung der Verpflegungspauschale nach Beschäftigungsgrad; Berechnung grundsätzlich mit 225 Arbeitstagen. Kein Abzug für Kosten, die Arbeitgebende übernommen haben.
- **Beachten:** Teilzeit: Verpflegungspauschale nach Beschäftigungsgrad kürzen; Fahrkostenmaxima Kanton 6'000 / Bund 3'300 nicht kürzen
- **Beachten:** Unterjährige Steuerpflicht: Umrechnung der Pauschalen (für den Steuersatz) macht die Steuerverwaltung
- **Beachten:** Kein Abzug für Kosten, die Arbeitgebende übernommen haben
- **Limiten:**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **225 Tage (Bei der Berechnung der notwendigen Berufsauslagen ist in der Regel von 225 Arbeitstagen im Jahr auszugehen (100%-Pensum).)** · Bund **n/a – Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei staendiger auswaertiger Verpflegung maximal Fr. 3'200 im Jahr; bei Teilzeit/Nebenberuf angemessene Kuerzung.)** · Bund **CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstaette (Staats- und Gemeindesteuern): Maximalabzug Fr. 6'000 pro Person gesamthaft (inkl. Fahrkosten Wochenaufenthalt und Nebenerwerb); wird bei unterjaehriger Steuerpflicht/Teilzeit nicht gekuerzt.)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0001.md) `tg-form-04-2-2026__c0001` – «1.1 Arbeitgeber/in, Arbeitsort»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0173.md) `tg-wl-2026__c0173` – «Bei der Berechnung der notwendigen Auslagen ist in der Regel von 225»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0174.md) `tg-wl-2026__c0174` – «Beispiel unterjährige Erwerbstätigkeit: Dauer von 01.04.2026 bis 31.12.2026 (Dauer 270 Tage)»
  - [WL Lohnausweis 2026 S. 7–8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0008.md) `bund-wl-lohnausweis-2026__c0008` – «Lohnperiode Buchstabe E»
  - [WL Lohnausweis 2026 S. 7–8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0009.md) `bund-wl-lohnausweis-2026__c0009` – «In diesen Feldern sind die genauen Ein- und Austrittsdaten des Arbeitnehmers anzugeben.»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0184.md) `tg-wl-2026__c0184` – «erfolgt eine angemessene Kürzung des Pauschalbetrags. Bei einem Teilzeitpensum wird der»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0007.md) `tg-stp-29-2__c0007` – «werden auch bei unterjähriger Steuerpflicht, unterjähriger Erwerbsdauer oder Teilzeitarbeit nicht gekürzt»

<a id="form-4-2-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2 Ziff. 1.2 – Steht ein Geschäftsfahrzeug für die Fahrt zur Arbeitsstätte zur Verfügung? (Ja/Nein, von/bis)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld F (Kreuz «unentgeltliche Beförderung zwischen Wohn- und Arbeitsort»), Ziff. 2.2 Privatanteil Geschäftsfahrzeug
- **Rein:** Lohnausweis → Bst. F (unentgeltliche Beförderung Wohn-/Arbeitsort) · Lohnausweis → Ziff. 2.2 Privatanteil Geschäftsfahrzeug · Lohnausweis → Ziff. 2.3 vergütete Arbeitswegkosten (dann kein Kreuz in Bst. F)
- **Rechnen:** Geschäftsfahrzeug für Arbeitsweg → «Ja» + von/bis; kein Fahrkostenabzug in Ziff. 2 (Arbeitsweg im Privatanteil 0.9 % pro Monat enthalten, keine Aufrechnung)
- **Regel:** Lohnausweis Feld F angekreuzt (Geschäftsfahrzeug, Sammeltransport, GA aus geschäftlichen Gründen u.ä.) → «Ja» und KEIN Fahrkostenabzug (Ziff. 2). Der Privatanteil 0.9% pro Monat im Lohnausweis schliesst den Arbeitsweg ein, daher keine Aufrechnung, aber auch kein Abzug. Wurden die Arbeitswegkosten vergütet (Ziff. 2.3 Lohnausweis), ist Feld F nicht anzukreuzen.
- **Beachten:** Bst. F auch bei Sammeltransport, Aussendienst-Kilometervergütung, Autopauschale, geschäftlich nötigem GA → kein Abzug
- **Beachten:** GA ohne geschäftliche Notwendigkeit: Marktwert in LA Ziff. 2.3, Bst. F nicht angekreuzt
- **Beachten:** Bietet der Arbeitgeber eine Fahrmöglichkeit, besteht kein Abzug (§ 6 BKV TG)
- **Bemerkung:** Lohnausweis-Regel (Feld F) stammt aus Bund-Wegleitung Lohnausweis 2026 (ESTV, amtlich für alle Kantone).
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0001.md) `tg-form-04-2-2026__c0001` – «1.2 Steht Ihnen für die Fahrt zur Arbeitsstätte»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0175.md) `tg-wl-2026__c0175` – «Der im Lohnausweis berücksichtigte Privatanteil Fahrzeug von 0.9 % pro Monat für die private»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «die Beförderung zum Arbeitsort mittels Sammeltransports (v.a. im Baugewerbe)»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0011.md) `bund-wl-lohnausweis-2026__c0011` – «ohne dass eine geschäftliche Notwendigkeit besteht, ist dieses zum Marktwert unter Ziffer 2.3 des Lohnausweises zu deklarieren»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0011.md) `bund-wl-lohnausweis-2026__c0011` – «Vergütungen einer Autopauschale für Mitarbeitende mit sehr häufigem geschäftlichem»
  - [WL Lohnausweis 2026 S. 9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0016.md) `bund-wl-lohnausweis-2026__c0016` – «so wird der Betrag als Berufskostenentschädigung in Ziffer 2.3 deklariert»
  - [BKV TG § 6](../../chunks/tg/2025/tg-bkv/tg-bkv__par-6.md) `tg-bkv__par-6` – «Soweit Berufsauslagen vom Arbeitgeber oder von anderer Seite vergütet werden oder eine Fahrmöglichkeit geboten wird, steht dem Steuerpflichtigen kein Abzug zu.»
  - [WL Lohnausweis 2026 S. 10](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0019.md) `bund-wl-lohnausweis-2026__c0019` – «Privatanteil Geschäftsfahrzeug Ziffer 2.2»

<a id="form-4-2-4-3-ziff-2-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2/4.3 Ziff. 2.1 – Abonnementskosten öffentliche Verkehrsmittel (Code 206 Person 1 / 246 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg → Abo-Beleg (Jahresabo, Streckenabo, GA) – nachgewiesene Kosten
- **Rein:** ÖV-Abonnement/Quittung → nachgewiesene Abokosten Arbeitsweg · Lohnausweis → Bst. F nicht angekreuzt · ÖV-Belege Wochenaufenthalt → Heimkehr bzw. Unterkunft–Arbeitsstätte
- **Rechnen:** Σ nachgewiesene Abokosten (inkl. Wochenaufenthalt) → Ziff. 2.4; Plafond in Ziff. 2.5: Kanton 6'000 / Bund 3'300
- **Regel:** Tatsächlich entstandene (nachgewiesene) Abonnementskosten für Bahn/Tram/Bus. Nur wenn Lohnausweis Feld F NICHT angekreuzt ist. Auch Fahrkosten bei Wochenaufenthalt (Heimkehr, Unterkunft–Arbeitsstätte) hier einsetzen. Die Summe aus 2.1–2.3 unterliegt dem Fahrkostenmaximum (Ziff. 2.5).
- **Beachten:** Nur bei beachtenswerter Entfernung (ab ca. 1 km)
- **Beachten:** Bst. F angekreuzt (keine Kosten für den Arbeitsweg) → kein Abzug
- **Beachten:** Tatsächliche Abokosten gelten für Kanton und Bund gleich; Unterschied erst beim Plafond
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstaette (Staats- und Gemeindesteuern): Maximalabzug Fr. 6'000 pro Person gesamthaft (inkl. Fahrkosten Wochenaufenthalt und Nebenerwerb); wird bei unterjaehriger Steuerpflicht/Teilzeit nicht gekuerzt.)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0002.md) `tg-form-04-2-2026__c0002` – «2.1 Abonnementskosten für öffentliche Verkehrsmittel 206»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0177.md) `tg-wl-2026__c0177` – «Bei Benützung öffentlicher Verkehrsmittel (Bahn, Tram, Autobus) können Sie die tatsächlich»
  - [WL TG 2026 S. 37–38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0176.md) `tg-wl-2026__c0176` – «sofern es sich um eine beachtenswerte Entfernung (ab ca. 1 km) handelt.»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer keine Kosten für den Arbeitsweg»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0002.md) `tg-stp-29-2__c0002` – «sowohl für die Staats- und Gemeindesteuern als auch für die direkte Bundessteuer die tatsächlich entstandenen (nachgewiesenen) Abonnementskosten»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0188.md) `tg-wl-2026__c0188` – «Deklarieren Sie die Fahrkosten für den Wochenaufenthalt unter den Ziffern 2.1 bis 2.3.»

<a id="form-4-2-4-3-ziff-2-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2/4.3 Ziff. 2.2 – Fahrrad, Kleinmotorrad bis 50 cm³ pauschal Fr. 700 (Code 210 Person 1 / 250 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Keine Belege nötig (Pauschale)
- **Rein:** Kein Beleg nötig (Pauschale) · Angabe Fahrzeugart: Fahrrad, Motorfahrrad, Kleinmotorrad (gelbes Kontrollschild) · Form. 4.2 Ziff. 1.1 → Dauer der Erwerbstätigkeit (für Umrechnung)
- **Rechnen:** pauschal bis 700 pro Jahr (Kanton = Bund); bei unterjähriger Erwerbstätigkeit auf die Dauer umrechnen
- **Regel:** Pauschal bis Fr. 700 pro Jahr für Fahrrad, Motorfahrrad, Kleinmotorrad (bis 45 km/h, gelbes Kontrollschild).
- **Beachten:** Nur bis 45 km/h bzw. gelbes Kontrollschild; Motorrad mit weissem Schild → Ziff. 2.3 (0.40 pro km)
- **Beachten:** Nur bei beachtenswerter Entfernung (ab ca. 1 km)
- **Beachten:** Zählt zum Fahrkostenmaximum (Ziff. 2.5)
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Fahrrad, Motorfahrrad, Kleinmotorrad (bis 45 km/h, gelbes Kontrollschild): bis Fr. 700 im Jahr.)** · Bund **CHF 700 (Fahrrad, Motorfahrrad, Motorrad mit gelbem Kontrollschild: Pauschale CHF 700 pro Jahr; tatsächliche Kosten können nicht zusätzlich geltend gemacht werden.)**
  - Fahrkosten Motorrad – Ansatz pro km (CHF): Kanton **CHF 0.40 (Motorrad (Hoechstgeschwindigkeit ab 45 km/h, weisses Kontrollschild): bis Fr. 0.40 pro Fahrkilometer.)** · Bund **CHF 0.40 (Motorrad mit weissem Kontrollschild: CHF 0.40 pro Fahrkilometer (nur wenn kein öffentliches Verkehrsmittel zumutbar); Gesamtmaximum CHF 3'300.)**
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0002.md) `tg-form-04-2-2026__c0002` – «2.2 Fahrrad, Kleinmotorrad bis 50 cm3 pauschal Fr. 700.– 210»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0177.md) `tg-wl-2026__c0177` – «können Sie bis zu Fr. 700 im Jahr abziehen.»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0173.md) `tg-wl-2026__c0173` – «Die als Pauschalen ausgestalteten Berufsauslagen beziehen sich auf das ganze Jahr.»
  - [BKV TG § 1](../../chunks/tg/2025/tg-bkv/tg-bkv__par-1.md) `tg-bkv__par-1` – «ist pro Fahrkilometer ein Abzug bis Fr. 0.40 für Motorräder mit weissem Kontrollschild»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0006.md) `tg-stp-29-2__c0006` – «Bei der Fahrkostenbeschränkung werden sämtliche entstandenen Fahrkosten berücksichtigt»
  - [WL TG 2026 S. 37–38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0176.md) `tg-wl-2026__c0176` – «sofern es sich um eine beachtenswerte Entfernung (ab ca. 1 km) handelt.»

<a id="form-4-2-4-3-ziff-2-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2/4.3 Ziff. 2.3 – Kosten für privates Motorfahrzeug (Auto / Motorrad über 50 cm³): km pro Tag × Anzahl Tage (Code 211 Person 1 / 251 Person 2), Spalten Staat und Bund separat

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ⚠️ strittig
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Begründung der Notwendigkeit (Zeitersparnis, kein zumutbarer ÖV), Arbeitsweg-km und Arbeitstage
- **Rein:** Angaben Arbeitsweg → km pro Tag (Wohnadresse – Fahrzeugstandort am Arbeitsort bzw. P+Rail), Anzahl Tage · Begründung Unzumutbarkeit ÖV (Fahrplan, Umsteigen, Distanz Haltestelle, Zeitersparnis) · Belege Parkgebühren P+Rail
- **Rechnen:** km/Jahr = km/Tag × Tage (≤ 225 bei 100%); Kanton Auto: 3'000 km × 0.60 + nächste 2'000 × 0.50 + Rest × 0.40; Bund Auto km × 0.75 (strittig); Motorrad km × 0.40
- **Regel:** In der Regel nur der Betrag, der mit dem zur Verfügung stehenden ÖV auszulegen wäre; Privatfahrzeug nur in begründeten Fällen. Ansätze Kanton Auto: bis 3'000 km Fr. -.60; 3'001–5'000 km Fr. -.50; über 5'000 km Fr. -.40; Motorrad (weisses Kontrollschild) Fr. -.40/km. Bund einheitlich pro km (siehe Bemerkung: Quellen widersprüchlich Fr. 0.70 vs. 0.75). Bund und Kanton separat berechnen. Max. 225 Arbeitstage bei 100%.
- **Beachten:** Grundsatz nur ÖV-Kosten; Auto nur wenn ÖV unzumutbar, z.B. Zeitersparnis über 1 Stunde pro Arbeitstag
- **Beachten:** P+Rail grundsätzlich zumutbar (dann Parkgebühren abziehbar); in den km-Ansätzen sind Parkgebühren enthalten
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
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0178.md) `tg-wl-2026__c0178` – «wenn die Zeitersparnis bei Benützung des privaten Verkehrsmittels pro Arbeitstag über 1 Stunde beträgt»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0178.md) `tg-wl-2026__c0178` – «in diesem Fall auch die Parkgebühren abzugsfähig sind»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0178.md) `tg-wl-2026__c0178` – «Distanz zwischen der Wohnadresse und dem Standort des Fahrzeugs am Arbeitsort»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0004.md) `tg-stp-29-2__c0004` – «In diesen km-Ansätzen sind allfällige Parkgebühren bereits enthalten.»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0004.md) `tg-stp-29-2__c0004` – «Bei der direkten Bundessteuer beträgt der Ansatz einheitlich 70 Rp. pro gefahrenen Kilometer.»

<a id="form-4-2-4-3-ziff-2-4-berechnung-total"></a>
### Ziff. Form. 4.2/4.3 Ziff. 2.4 – Total effektive Fahrkosten (Ziff. 2.1–2.3) (Code 212 Person 1 / 252 Person 2)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag aus Ziff. 2.1, 2.2 und 2.3 (je Spalte Staat/Bund)
- **Rechnen:** Σ Ziff. 2.1 + 2.2 + 2.3, getrennt Kanton / Bund (Bund wegen km-Ansatz in Ziff. 2.3 abweichend)
- **Regel:** Summe 2.1 + 2.2 + 2.3 (Staat und Bund separat). Bei kostenloser Überlassung eines Geschäftsfahrzeugs: kein Abzug.
- **Beachten:** Geschäftsfahrzeug für den Arbeitsweg (Ziff. 1.2 «Ja») → keine Fahrkosten
- **Beachten:** Fahrkosten Wochenaufenthalt (Heimkehr, Unterkunft–Arbeitsstätte) hier einrechnen
- **Beachten:** Behinderungsbedingte Mehrkosten der Fahrt zur Arbeit nicht hier, sondern bei den behinderungsbedingten Kosten
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0002.md) `tg-form-04-2-2026__c0002` – «2.4 Total effektive Fahrkosten (Ziffern 2.1 – 2.3) 212»
  - [WL TG 2026 S. 38–39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0181.md) `tg-wl-2026__c0181` – «Ermitteln Sie das Total der effektiv selbst getragenen Fahrkosten, indem Sie die Beträge der Ziffern»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0179.md) `tg-wl-2026__c0179` – «Steht ihnen ein Geschäftsfahrzeug für die Fahrt zwischen Wohn- und Arbeitsstätte zur Verfügung»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0188.md) `tg-wl-2026__c0188` – «Deklarieren Sie die Fahrkosten für den Wochenaufenthalt unter den Ziffern 2.1 bis 2.3.»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0006.md) `tg-stp-29-2__c0006` – «Im Zusammenhang mit der Fahrt zur Arbeit entstandene behinderungsbedingte Mehrkosten sind nicht unter den Berufsauslagen»

<a id="form-4-2-4-3-ziff-2-5-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4.2/4.3 Ziff. 2.5 – Total abzugsfähige Fahrkosten – Staat max. Fr. 6'000 / Bund max. Fr. 3'300 (Code 213 Person 1 / 253 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile mit Plafonierung
- **Rein:** Übertrag aus Ziff. 2.4 (Spalten Staat/Bund)
- **Rechnen:** Kanton: min(Ziff. 2.4 Kanton; 6'000); Bund: min(Ziff. 2.4 Bund; 3'300) – je Person → Form. 4.2/4.3 Ziff. 7 (Code 240/280) → Steuererklärung Seite 3 Ziff. 10.1/10.2
- **Regel:** Total aus 2.4, aber Staat höchstens Fr. 6'000 und Bund höchstens Fr. 3'300 (gilt auch für Fahrkosten bei Wochenaufenthalt). Liegt 2.4 darunter, wird der effektive Betrag eingesetzt.
- **Beachten:** Plafond umfasst alle Fahrkosten inkl. Wochenaufenthalt und effektive Nebenerwerbs-Fahrkosten
- **Beachten:** Keine Kürzung bei unterjähriger Steuerpflicht/Erwerbsdauer oder Teilzeit
- **Beachten:** Beispiel 12'150 km: Kanton 5'660 (unter Maximum), Bund auf 3'300 begrenzt
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstaette (Staats- und Gemeindesteuern): Maximalabzug Fr. 6'000 pro Person gesamthaft (inkl. Fahrkosten Wochenaufenthalt und Nebenerwerb); wird bei unterjaehriger Steuerpflicht/Teilzeit nicht gekuerzt.)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Bund:** Bund max. Fr. 3'300.
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0002.md) `tg-form-04-2-2026__c0002` – «aber Staat max. Fr. 6000.– / Bund max. Fr. 3300.–)»
  - [WL TG 2026 S. 38–39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0181.md) `tg-wl-2026__c0181` – «Bei den Staats- und Gemeindesteuern können Fahrkosten von maximal Fr. 6'000 und bei der»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0006.md) `tg-stp-29-2__c0006` – «sämtliche entstandenen Fahrkosten berücksichtigt (öffentliche Verkehrsmittel, Fahrrad, Motorfahrrad, Motorrad, Privatauto inkl. der Fahrkosten bei Wochenaufenthalt)»
  - [WL TG 2026 S. 40–41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0190.md) `tg-wl-2026__c0190` – «Werden effektive Fahrkosten geltend gemacht, sind diese bei der»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0007.md) `tg-stp-29-2__c0007` – «werden auch bei unterjähriger Steuerpflicht, unterjähriger Erwerbsdauer oder Teilzeitarbeit nicht gekürzt»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0182.md) `tg-wl-2026__c0182` – «Daher kann bei der direkten Bundessteuer nur der Maximalabzug von Fr. 3'300»
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0005.md) `tg-form-04-2-2026__c0005` – «Übertrag in Steuererklärung Seite 3, Ziffer 10.1»
  - [Formular 4.2/4.3 TG 2026 S. 2](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0010.md) `tg-form-04-2-2026__c0010` – «7. Total der abzugsfähigen Berufsauslagen 280»

<a id="form-4-2-4-3-ziff-3-1-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4.2/4.3 Ziff. 3.1 – Mehrkosten auswärtige Verpflegung ohne Verbilligung: Fr. 15 pro Arbeitstag, max. Fr. 3'200/Jahr; Schichttage (Code 214 Person 1 / 254 Person 2)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Ziff. 15 (Anzahl Schichttage) bzw. Bescheinigung Arbeitgeber; Lohnausweis Feld G darf nicht angekreuzt sein
- **Rein:** Lohnausweis → Bst. G nicht angekreuzt (sonst Ziff. 3.2) · Lohnausweis Ziff. 15 bzw. Bescheinigung Arbeitgeber → Anzahl Schicht-/Nachttage · Form. 4.2 Ziff. 1.1 → Pensum, Dauer der Erwerbstätigkeit
- **Rechnen:** min(Tage × 15; 3'200 × Pensum %), unterjährig Max. × Erwerbstage / 360; Schicht/Nacht (mind. achtstündig): Schichttage × 15, max. 3'200; Kanton = Bund
- **Regel:** Fr. 15 pro auswärtige Hauptmahlzeit (in der Regel Mittagessen), max. Fr. 3'200/Jahr, wenn Heimkehr am Mittag unzumutbar (grosse Entfernung oder sehr kurze Essenspause). Schicht-/Nachtarbeit: gleiche Pauschale für jeden ausgewiesenen Tag mit durchgehender, mindestens achtstündiger Schicht- oder Nachtarbeit; Anzahl Schichttage ist nachzuweisen (Bescheinigung Arbeitgeber), sofern nicht im Lohnausweis (Ziff. 15 Bemerkungen) aufgeführt. Keine Kumulation mit Fahrkosten für Heimkehr über Mittag und nicht mit Wochenaufenthalt (Ziff. 5.2). Teilzeit: Kürzung nach Pensum.
- **Beachten:** Nur wenn Heimkehr am Mittag unzumutbar (grosse Entfernung oder sehr kurze Essenspause)
- **Beachten:** Nicht kumulierbar mit Mittags-Heimfahrkosten, Wochenaufenthalt (Ziff. 5.2) und Schicht-/Nachtabzug
- **Beachten:** Gestaffelte/unregelmässige Arbeitszeit = Schichtarbeit, wenn beide Hauptmahlzeiten nicht zu Hause möglich
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswaertige Verpflegung bei taeglicher Heimkehr: Fr. 15 pro auswaertige Hauptmahlzeit (in der Regel nur Mittagessen), wenn Heimkehr am Mittag wegen grosser Entfernung oder sehr kurzer Essenspause nicht zumutbar.)** · Bund **CHF 15 (Auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (in der Regel nur Mittagessen), nur Pauschale zulässig, wenn Hauptmahlzeit wegen grosser Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann oder bei durchgehender Schicht-/Nachtarbeit.)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei staendiger auswaertiger Verpflegung maximal Fr. 3'200 im Jahr; bei Teilzeit/Nebenberuf angemessene Kuerzung.)** · Bund **CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Durchgehende, mindestens achtstuendige Schicht- oder Nachtarbeit (ausgewiesen, Bescheinigung Arbeitgeber): gleiche Abzuege wie auswaertige Verpflegung (Fr. 15 pro Tag, max. Fr. 3'200 im Jahr; bei Verbilligung halb). Nicht kumulierbar mit Verpflegungs- oder Wochenaufenthaltsabzug.)** · Bund **CHF 15 (Schicht-/Nachtarbeit: gleiche Pauschale wie auswärtige Verpflegung, CHF 15 pro Tag bzw. max. CHF 3'200 pro Jahr (bei Verbilligung halber Abzug). Gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt (Art. 6 Abs. 4 BKV). Arbeitgeber muss Tage und Arbeitsort auf Verlangen bescheinigen.)**
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0003.md) `tg-form-04-2-2026__c0003` – «3.1 ohne Verbilligung durch Arbeitgeber/in oder Schicht-/Nachtarbeit:»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0183.md) `tg-wl-2026__c0183` – «Der Pauschalabzug beträgt Fr. 15 für jede auswärtige Hauptmahlzeit»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0184.md) `tg-wl-2026__c0184` – «Die Anzahl geleistete Tage mit mindestens achtstündiger Schicht- oder Nachtarbeit ist nachzuweisen»
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «die Anzahl im Kalenderjahr geleisteter Schichttage und die Höhe der im Bruttolohn»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0174.md) `tg-wl-2026__c0174` – «Beispiel unterjährige Erwerbstätigkeit: Dauer von 01.04.2026 bis 31.12.2026 (Dauer 270 Tage)»
  - [WL TG 2026 S. 38](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0179.md) `tg-wl-2026__c0179` – «können Sie den Abzug für auswärtige Verpflegung in Ziffer 3.1 bzw. Ziffer 3.2 nicht»
  - [BKV TG § 3](../../chunks/tg/2025/tg-bkv/tg-bkv__par-3.md) `tg-bkv__par-3` – «Der Abzug für Schicht- oder Nachtarbeit kann nicht zusätzlich zum Abzug für auswärtige Verpflegung oder für auswärtigen Wochenaufenthalt beansprucht werden.»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer Lunch-Checks»

<a id="form-4-2-4-3-ziff-3-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4.2/4.3 Ziff. 3.2 – Mehrkosten auswärtige Verpflegung mit Verbilligung durch Arbeitgeber/Kantine: Fr. 7.50 pro Arbeitstag, max. Fr. 1'600/Jahr (Code 216 Person 1 / 256 Person 2)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Feld G (Kantine/Lunch-Checks/Personalrestaurant) angekreuzt; Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt»
- **Rein:** Lohnausweis → Bst. G angekreuzt (Lunch-Checks, Kantine/Personalrestaurant, Mittagsentschädigung bei 40–60 % auswärts) · Spesenreglement/Bestätigung Arbeitgeber → Art der Verbilligung, Preis der Mahlzeit · Form. 4.2 Ziff. 1.1 → Pensum, Dauer der Erwerbstätigkeit
- **Rechnen:** min(Tage × 7.50; 1'600), Kanton = Bund; Teilzeit/unterjährig Max. kürzen; kein Abzug, wenn Mahlzeit < 10 bzw. AG-Bewertung < Mittag 10 / Abend 8 / Tag 21.50
- **Regel:** Lohnausweis Feld G angekreuzt (Lunch-Checks, verbilligtes Mittag-/Abendessen im Personalrestaurant – auch wenn unbekannt ist, ob davon Gebrauch gemacht wird) → nur halber Abzug: Fr. 7.50/Tag, max. Fr. 1'600/Jahr, und nur wenn trotzdem Mehrkosten entstehen. Kein Abzug, wenn die Hauptmahlzeiten auf weniger als Fr. 10 zu stehen kommen. Wenn der Arbeitgeber das Mittagessen vollständig bezahlt (Ziff. 15 Vermerk), kein Verpflegungsabzug.
- **Beachten:** Bst. G gilt auch, wenn unbekannt ist, ob die Kantine tatsächlich benutzt wird
- **Beachten:** Pflicht-Mahlzeit beim Arbeitgeber (z.B. Gastgewerbe): pro Tag höchstens ein halber Abzug
- **Beachten:** Vom AG bezahltes Mittagessen (LA Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt») → kein Abzug (§ 6 BKV TG)
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Bei Verbilligung durch Arbeitgeber (Gutscheine, Kantine, Personalrestaurant) nur der halbe Abzug: Fr. 7.50 pro Tag. Kein Abzug, wenn Hauptmahlzeit unter Fr. 10 zu stehen kommt.)** · Bund **CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei Verbilligung durch Arbeitgeber: halber Abzug, maximal Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)**
- **Bemerkung:** Lohnausweis-Regel Feld G aus Bund-WL Lohnausweis 2026 (ESTV).
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0003.md) `tg-form-04-2-2026__c0003` – «3.2 mit Verbilligung durch Arbeitgeber/in oder Kantine,»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0185.md) `tg-wl-2026__c0185` – «Nur der halbe Abzug (Fr. 7.50 im Tag, Fr. 1'600 im Jahr) ist zulässig»
  - [WL TG 2026 S. 39–40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0186.md) `tg-wl-2026__c0186` – «Kein Abzug ist mangels Mehrkosten zulässig, wenn die Hauptmahlzeiten auf weniger als»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer Lunch-Checks»
  - [BKV TG § 6](../../chunks/tg/2025/tg-bkv/tg-bkv__par-6.md) `tg-bkv__par-6` – «Soweit Berufsauslagen vom Arbeitgeber oder von anderer Seite vergütet werden oder eine Fahrmöglichkeit geboten wird, steht dem Steuerpflichtigen kein Abzug zu.»
  - [WL TG 2026 S. 37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0173.md) `tg-wl-2026__c0173` – «Die als Pauschalen ausgestalteten Berufsauslagen beziehen sich auf das ganze Jahr.»

<a id="form-4-2-4-3-ziff-4-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4.2/4.3 Ziff. 4 – Übrige für den Beruf erforderliche Kosten: 3% vom Nettolohn, min. Fr. 2'000, max. Fr. 4'000, oder effektiv (Code 220 Person 1 / 260 Person 2)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 Nettolohn (Berechnungsbasis); bei effektiven Kosten Aufstellung mit Belegen
- **Rein:** Lohnausweis → Ziff. 11 Nettolohn (Basis 3%) · Aufstellung + Belege effektive Kosten (Werkzeuge, Fachliteratur, Berufskleider, Verbandsbeiträge)
- **Rechnen:** max(2'000; min(3% × Nettolohn LA Ziff. 11; 4'000)) je Person, Kanton = Bund; < 12 Monate erwerbstätig: anteilmässig kürzen; oder effektiv
- **Regel:** Pauschale 3% des Nettolohns (Lohnausweis Ziff. 11), min. Fr. 2'000, max. Fr. 4'000 (Staat und Bund); bei weniger als 12 Monaten Erwerbstätigkeit anteilmässig gekürzt. Alternativ effektive Kosten nachweisen (separate Aufstellung) – keine Kumulation mit der Pauschale.
- **Beachten:** Pauschale oder effektive Kosten – keine Kumulation; effektiv nur mit separater Aufstellung und Belegen
- **Beachten:** Pauschale deckt u.a. Werkzeuge, Fachliteratur, Kleider-/Schuhverschleiss, Schwerarbeit, Berufsverbände
- **Beachten:** Nebenerwerb nicht hier, sondern separat in Ziff. 6
- **Limiten:**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **3 % (Pauschale übrige Berufskosten (Form. 4.2 Ziff. 4: Berufswerkzeuge, Fachliteratur, Kleider-/Schuhverschleiss, Mehrauslagen für Schwerarbeit, Beiträge an Berufsverbände/Gewerkschaften): 3 % des Nettolohns (Ziff. 11 Lohnausweis), min. Fr. 2'000, max. Fr. 4'000 (Kanton und dBSt). Anstelle der Pauschale können die notwendigen tatsächlichen Aufwendungen nachgewiesen werden (keine Kumulation mit der Pauschale). Bei weniger als 12 Monaten unselbständiger Erwerbstätigkeit anteilmässig gekürzt.)** · Bund **3 % (Übrige Berufskosten (Art. 26 Abs. 1 lit. c DBG): Pauschale 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; anstelle der Pauschale ist der Nachweis höherer tatsächlicher übriger Berufskosten möglich. Fahrkosten (lit. a, max. 3'300) und Verpflegung (lit. b) werden zusätzlich abgezogen. Bei Teilzeit/Teiljahr angemessen kürzen.)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **CHF 2'000 (Pauschale uebrige Berufskosten: Minimum Fr. 2'000.)** · Bund **CHF 2'000 (Mindestbetrag der Pauschale übrige Berufskosten.)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 4'000 (Pauschale uebrige Berufskosten: Maximum Fr. 4'000.)** · Bund **CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)**
- **Bund:** Gleich (Pauschale gilt kantonal und Bund).
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0004.md) `tg-form-04-2-2026__c0004` – «3% vom Nettolohn, mindestens jedoch Fr. 2000.– und höchstens Fr. 4000.–»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0187.md) `tg-wl-2026__c0187` – «Pauschalabzug von 3% vom Nettolohn gemäss Ziffer 11 des Lohnausweises»
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0005.md) `tg-form-04-2-2026__c0005` – «6. Auslagen bei Nebenbeschäftigung»

<a id="form-4-2-4-3-ziff-5-1-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4.2/4.3 Ziff. 5.1 – Wochenaufenthalt – Unterkunft: ortsübliche Auslagen für ein Zimmer (Code 226 Person 1 / 266 Person 2)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag/Mietzinsbestätigung Zimmer am Arbeitsort
- **Rein:** Mietvertrag/Mietzinsbelege Zimmer am Arbeitsort → Jahresmiete · Bei Wohnung bis 3,5 Zimmer: Mietvertrag → Jahresmietzins, Zimmerzahl
- **Rechnen:** Zimmer: ortsübliche Jahresmiete; Wohnung bis 3,5 Zi.: Jahresmietzins : (Zimmerzahl + 1), z.B. 10'800 : (3,5 + 1) = 2'400
- **Regel:** Nur ein Zimmer (nicht Wohnung) ist notwendig; bei kleiner Wohnung bis 3½ Zimmer: Jahresmietzins : (Zimmerzahl + 1) = Kosten des Zimmers. Fahrkosten der wöchentlichen Heimkehr unter Ziff. 2.1–2.3 (mit Fahrkostenmaximum).
- **Beachten:** Nur bei Wochenaufenthalt mit regelmässiger Heimkehr (Wochenende/freie Tage), Steuerpflicht am Wohnort
- **Beachten:** Unterkunft als Naturallohn erhalten → kein Abzug (§ 4 BKV TG)
- **Beachten:** Fahrkosten Heimkehr und Unterkunft–Arbeitsstätte in Ziff. 2.1–2.3; Fahrkostenmaximum gilt
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Wochenaufenthalt: notwendige Mehrkosten der Unterkunft - nur ortsuebliche Auslagen fuer ein Zimmer (nicht Wohnung). Bei gemieteter kleinerer Wohnung (bis 3.5 Zimmer): Jahresmietzins : (Anzahl Zimmer + 1) = Kosten des Zimmers. Kein Abzug bei Naturallohn.** · Bund **Wochenaufenthalt: abziehbar sind die ortsüblichen Auslagen für ein Zimmer (nicht eine Wohnung) am Arbeitsort sowie die Fahrkosten der regelmässigen Heimkehr (im Rahmen des Fahrkosten-Maximums).**
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0004.md) `tg-form-04-2-2026__c0004` – «5.1 Unterkunft ortsübliche Auslagen für ein Zimmer 226»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0189.md) `tg-wl-2026__c0189` – «Jahresmietzins : (Anzahl Zimmer + 1) = Kosten des Zimmers»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0188.md) `tg-wl-2026__c0188` – «über das Wochenende oder an den freien Tagen nach Hause zurückkehren»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0188.md) `tg-wl-2026__c0188` – «Beachten Sie bitte, dass die Fahrkostenbeschränkung auch für den Wochenaufenthalt gilt.»
  - [BKV TG § 4](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4.md) `tg-bkv__par-4` – «ein Abzug gemäss Ziff. 1 und Ziff. 2 ist nicht zulässig, wenn der Steuerpflichtige die entsprechende Leistung als Naturallohn erhält»

<a id="form-4-2-4-3-ziff-5-2-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4.2/4.3 Ziff. 5.2 – Wochenaufenthalt – Verpflegung: Fr. 30 pro Arbeitstag, max. Fr. 6'400/Jahr; bei Verbilligung Fr. 22.50, max. Fr. 4'800 (Code 230 Person 1 / 270 Person 2)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (verbilligtes Mittagessen) → Reduktion
- **Rein:** Angabe Arbeitstage am Wochenaufenthaltsort (Dauer Wochenaufenthalt) · Lohnausweis → Bst. G / Verbilligung Mittagessen (Kantine, Kostenbeitrag)
- **Rechnen:** Tage × 30, max. 6'400 (ganzjährig); Mittagessen verbilligt: Tage × 22.50, max. 4'800; Kanton = Bund
- **Regel:** Fr. 15 pro Hauptmahlzeit = Fr. 30 pro Tag, bei ganzjährigem Wochenaufenthalt Fr. 6'400; bei vom Arbeitgeber verbilligtem Mittagessen (Kantinenkost, Kostenbeitrag) für diese Mahlzeit nur der halbe Abzug, gesamthaft Fr. 22.50 pro Tag bzw. Fr. 4'800 im Jahr. Nicht kumulierbar mit Ziff. 3.
- **Beachten:** Für denselben Zeitraum nicht mit Ziff. 3 (tägliche Heimkehr) kumulieren
- **Beachten:** Verpflegung als Naturallohn erhalten → kein Abzug (§ 4 BKV TG)
- **Beachten:** Bund: Nachweis höherer Kosten ausgeschlossen
- **Limiten:**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 6'400 (Wochenaufenthalt Verpflegung: Fr. 15 pro Hauptmahlzeit = Fr. 30 pro Tag, bei ganzjaehrigem Wochenaufenthalt Fr. 6'400 im Jahr; bei Verbilligung des Mittagessens Fr. 22.50 pro Tag bzw. Fr. 4'800 im Jahr.)** · Bund **CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug CHF 30 pro Tag bzw. CHF 6'400 pro Jahr; gekürzter Abzug (verbilligtes Mittagessen) CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr. Nachweis höherer Kosten ausgeschlossen.)**
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0004.md) `tg-form-04-2-2026__c0004` – «bei Verbilligung pro Arbeitstag Fr. 22.50 / im Jahr Fr. 4800.–»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0189.md) `tg-wl-2026__c0189` – «im Tag, bei ganzjährigem Wochenaufenthalt Fr. 6'400 im Jahr abziehen.»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0189.md) `tg-wl-2026__c0189` – «gesamthaft Fr. 22.50 im Tag oder Fr. 4'800 im Jahr.»
  - [WL TG 2026 S. 39](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0183.md) `tg-wl-2026__c0183` – «gleichen Zeitraum nicht mit dem Abzug bei Wochenaufenthalt (vgl. Ziffer 5.2) kumulieren.»
  - [BKV TG § 4](../../chunks/tg/2025/tg-bkv/tg-bkv__par-4.md) `tg-bkv__par-4` – «ein Abzug gemäss Ziff. 1 und Ziff. 2 ist nicht zulässig, wenn der Steuerpflichtige die entsprechende Leistung als Naturallohn erhält»
  - [BKV Art. 9](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-9.md) `bund-bkv-2026__art-9` – «Der Nachweis höherer Kosten ist ausgeschlossen.»

<a id="form-4-2-4-3-ziff-6-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 4.2/4.3 Ziff. 6 – Auslagen bei Nebenbeschäftigung: 20% vom Nettolohn, min. Fr. 800, max. Fr. 2'400, oder effektiv (Code 232 Person 1 / 272 Person 2)

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Nebenerwerb Ziff. 11; bei effektiven Kosten Aufstellung
- **Rein:** Lohnausweis Nebenerwerb → Ziff. 11 Nettolohn · Aufstellung effektive Kosten (statt Pauschale) · Behördenmitglied: Abrechnung Funktionsentschädigungen, Sitzungsgelder, Pauschalspesen
- **Rechnen:** max(800; min(20% × Nettolohn NE; 2'400)) ≤ Einkommen der Tätigkeit, Kanton = Bund; Gemeinde-Exekutive: 50% × Entschädigungen, min. 2'000, max. 4'000
- **Regel:** Pauschale 20% der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400 (Staat und Bund); gilt alle Berufskosten der Nebentätigkeit ab (Fahrt, Verpflegung, übrige). Höchstens bis zur Höhe des Einkommens der zugehörigen Tätigkeit. Keine Kumulation Pauschale/effektiv. Pauschalabzug 50% (min. Fr. 2'000, max. Fr. 4'000) für Exekutivbehördenmitglieder.
- **Beachten:** Pauschale deckt Fahrt, Verpflegung, übrige Kosten; oder effektiv (keine Kumulation), Fahrkosten dann im Plafond
- **Beachten:** Setzt Haupterwerb voraus; einzige (auch geringfügige) Tätigkeit gilt als Haupterwerb
- **Beachten:** Behördenpauschale nur nebenamtliche, gewählte Gemeinde-Exekutive; Kommissionen/Parlamente: ordentliche 20%-Pauschale
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Nebenerwerb (unselbstaendig): Pauschale 20 % der Nettoeinkuenfte; sie gilt alle Berufskosten des Nebenerwerbs (Fahrt, Verpflegung, uebrige) ab. Nachweis hoeherer effektiver Kosten vorbehalten; maximal bis Hoehe des Nebenerwerbseinkommens.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb-Pauschale: Minimum Fr. 800 im Jahr.)** · Bund **CHF 800 (Mindestbetrag Pauschale Nebenerwerb.)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb-Pauschale: Maximum Fr. 2'400 im Jahr.)** · Bund **CHF 2'400 (Höchstbetrag Pauschale Nebenerwerb.)**
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0005.md) `tg-form-04-2-2026__c0005` – «20% vom Nettolohn, mindestens Fr. 800.– und höchstens Fr. 2400.–»
  - [WL TG 2026 S. 40–41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0190.md) `tg-wl-2026__c0190` – «Der Abzug beträgt 20% der Nettoeinkünfte, mindestens aber Fr. 800 und höchstens»
  - [WL TG 2026 S. 41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0192.md) `tg-wl-2026__c0192` – «Der Pauschalabzug beträgt 50% von den insgesamt ausgerichteten Behördenentschädigungen»
  - [WL TG 2026 S. 41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0192.md) `tg-wl-2026__c0192` – «mindestens Fr. 2'000 und höchstens Fr. 4'000»
  - [WL TG 2026 S. 41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0191.md) `tg-wl-2026__c0191` – «Ebenfalls als Haupterwerb betrachtet wird auch eine geringfügige Tätigkeit, sofern es sich um die einzige»
  - [WL TG 2026 S. 41](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0193.md) `tg-wl-2026__c0193` – «Sie können aber die ordentliche Nebenerwerbspauschale geltend machen.»
  - [WL TG 2026 S. 40](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0187.md) `tg-wl-2026__c0187` – «Nettolohn gemäss Ziffer 11 des Lohnausweises»

<a id="form-4-2-4-3-ziff-7-berechnung-total"></a>
### Ziff. Form. 4.2/4.3 Ziff. 7 – Total der abzugsfähigen Berufsauslagen (Code 240 Person 1 / 280 Person 2) – Übertrag Form. 1 Ziff. 10.1 / 10.2

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 2 bis 6)
- **Rein:** Übertrag aus Ziff. 2.5, 3.1, 3.2, 4, 5.1, 5.2 und 6 (Form. 4.2 Person 1 / 4.3 Person 2)
- **Rechnen:** Σ Ziff. 2.5 + 3.1 + 3.2 + 4 + 5.1 + 5.2 + 6, je Spalte Kanton/Bund → Form. 1 Ziff. 10.1 (Person 1) / 10.2 (Person 2)
- **Regel:** Summe Ziff. 2 bis 6 je Spalte Staat/Bund; Übertrag in Formular 1 Ziff. 10.1 (Person 1) bzw. 10.2 (Person 2).
- **Beachten:** Fahrkosten nur mit plafoniertem Betrag aus Ziff. 2.5 übernehmen
- **Beachten:** Linke Spalte Staats- und Gemeindesteuern, rechte Spalte direkte Bundessteuer
- **Quellen:**
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0005.md) `tg-form-04-2-2026__c0005` – «7. Total der abzugsfähigen Berufsauslagen 240»
  - [WL TG 2026 S. 41–42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0195.md) `tg-wl-2026__c0195` – «Tragen Sie in diese Ziffer die Summe der Berufsauslagen gemäss den Ziffern 2 bis 7 ein.»
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0002.md) `tg-form-04-2-2026__c0002` – «2.5 Total abzugsfähige Fahrkosten (Übertrag von Ziffer 2.4»
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0003.md) `tg-form-04-2-2026__c0003` – «3.2 mit Verbilligung durch Arbeitgeber/in oder Kantine,»
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0004.md) `tg-form-04-2-2026__c0004` – «5.1 Unterkunft ortsübliche Auslagen für ein Zimmer»
  - [Formular 4.2/4.3 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-2-2026/tg-form-04-2-2026__c0004.md) `tg-form-04-2-2026__c0004` – «5.2 Verpflegung (analog Ziffer 3.1)»

## Hilfsblatt Krankheit/Unfall/Behinderung (Form. 5.1)

<a id="form-5-1-a-1-a-9-abzug-krankheitskosten"></a>
### Ziff. Form. 5.1 A.1–A.9 – Aufwendungen: Selbstbehalt/Franchise, Arzt/Medikamente, Zahnarzt, Pflegepersonal, Spital/Heim, Therapien/Kuren, Prothesen/Invalidenfahrzeug, tatsächliche Kosten, Total (A)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Arzt-/Zahnarzt-/Spitalrechnungen; Kostenzusammenstellung der Krankenkasse (Franchise/Selbstbehalt); ärztliche Verordnung Therapien
- **Rein:** Kostenzusammenstellung Krankenkasse → Franchise/Selbstbehalt (A.1) · Arzt-, Zahnarzt-, Spital-/Heim-, Pflege-, Therapierechnungen (A.2–A.6) · Ärztliche Verordnung → Therapien/Kuren, Diät · Rechnungen Prothesen/Hilfsmittel/Invalidenfahrzeug (A.7)
- **Rechnen:** Σ A.1–A.8 je Spalte (Krankheit/Unfall | behinderungsbedingt) = Total A; für sich und Personen mit Kinder-/Unterstützungsabzug
- **Regel:** In zwei Spalten erfassen: Krankheits- und Unfallkosten sowie behinderungsbedingte Kosten. Belege geordnet beilegen; Kopie ärztliche Verordnung bei Therapien/Kuren. Krankenkassenprämien, Fahrkosten zum Arzt, Prävention und Schönheits-/Fitnessbehandlungen nicht abzugsfähig.
- **Beachten:** Nicht abziehbar: KK-Prämien, Arztfahrten (ausser dauernde Pflegebedürftigkeit), Prävention, Schönheits-/Fitnesskuren
- **Beachten:** Behinderungsbedingt nur bei Behinderung (z.B. IV-/HE-Bezüger); Brille, Hörgerät oder Diät allein genügen nicht
- **Beachten:** Nicht behinderungsbedingter Altersheimaufenthalt nicht abziehbar, darin enthaltene Pflegekosten schon
- **Quellen:**
  - [Formular 5.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-1-2026/tg-form-05-1-2026__c0001.md) `tg-form-05-1-2026__c0001` – «Selbstbehalt / Franchise gemäss detaillierter Kostenzusammenstellung der Krankenkasse»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0201.md) `tg-wl-2026__c0201` – «Nicht abzugsfähig sind zudem die Krankenkassenprämien»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0196.md) `tg-wl-2026__c0196` – «können Sie Krankheits- und Unfallkosten für sich und diejenigen Personen, für welche Sie einen»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0197.md) `tg-wl-2026__c0197` – «von Leistungen gemäss Invalidenversicherungsgesetz (IVG);»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0198.md) `tg-wl-2026__c0198` – «gilt nicht als Behinderung. Dasselbe gilt, wenn die Beeinträchtigung einzig darin besteht, dass»

<a id="form-5-1-b-1-b-6-abzug-krankheitskosten"></a>
### Ziff. Form. 5.1 B.1–B.6 – Vergütungen Dritter und Anteil Lebenshaltungskosten (Krankenkasse, Versicherungen, Hilflosenentschädigung, Lebenshaltungsanteil, weitere), Total (B)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Leistungsabrechnung/Jahresbestätigung Krankenkasse und Versicherungen; Verfügung Hilflosenentschädigung
- **Rein:** Leistungsabrechnungen Krankenkasse (B.1) · Abrechnungen Versicherungen inkl. Pflegefinanzierung (B.2) · Verfügung Hilflosenentschädigung AHV/IV/SUVA (B.3)
- **Rechnen:** Σ B.1–B.5 je Spalte = Total B; B.4 Lebenshaltungsanteil (Heimaufenthalt i.d.R. 2'000 pro Monat)
- **Regel:** Soweit nicht bereits unter A abgezogen. Vergütete Kosten, AHV/IV/MV/SUVA-Beiträge für Hilfsmittel, Hilflosenentschädigungen, Pflegefinanzierung sowie ein Anteil Lebenshaltungskosten (Ernährung/Unterkunft, z.B. bei Heim: Fr. 2'000 pro Monat) von den Kosten abziehen.
- **Beachten:** Nur Vergütungen, die nicht schon unter A abgezogen sind (keine Doppelerfassung)
- **Beachten:** Auch Beiträge AHV/IV/MV/SUVA an Hilfsmittel und Leistungen Pflegefinanzierung abziehen
- **Beachten:** Beispiel WL: B Krankheit = KK 700 + Lebenshaltungsanteil Kur 600 = 1'300; B behinderungsbedingt = IV an Prothese 2'500
- **Quellen:**
  - [Formular 5.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-1-2026/tg-form-05-1-2026__c0002.md) `tg-form-05-1-2026__c0002` – «3. Hilflosenentschädigung AHV/IV/SUVA»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0201.md) `tg-wl-2026__c0201` – «Die von Krankenkassen, Versicherungen oder Dritten vergüteten Kosten»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0199.md) `tg-wl-2026__c0199` – «(in der Regel Fr. 2 000 pro Monat)»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0204.md) `tg-wl-2026__c0204` – «Lebenshaltungskostenanteil Kuraufenthalt Fr. 600»

<a id="form-5-1-c-abzug-behinderungskosten"></a>
### Ziff. Form. 5.1 C – Abzugsfähige behinderungsbedingte Kosten (A minus B; Code 350) → Form. 1 Ziff. 17

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Rechenzeile; Pauschalen optional (gehörlos, Dialyse, Hilflosenentschädigung)
- **Rein:** Übertrag Total A und Total B, Spalte behinderungsbedingt · Verfügung Hilflosenentschädigung bzw. Nachweis Gehörlosigkeit/Dialyse (für Pauschale)
- **Rechnen:** Total A − Total B (behinderungsbedingt), ohne Selbstbehalt → Form. 1 Ziff. 17; z.B. 3'000 − 2'500 = 500
- **Regel:** Total A minus Total B; ohne Selbstbehalt; Übertrag in Ziff. 17 (identisch für Staat und Bund).
- **Beachten:** Statt effektiv Pauschale: gehörlos, Dialyse, HE leicht 2'500; HE mittel 5'000; HE schwer 7'500
- **Beachten:** Krankheits-/Unfallkosten Behinderter gehören in Teil D (mit 5% Selbstbehalt)
- **Beachten:** Behinderungsbedingte Mehrkosten der Fahrt zur Arbeit hier statt bei den Berufskosten
- **Quellen:**
  - [Formular 5.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-1-2026/tg-form-05-1-2026__c0003.md) `tg-form-05-1-2026__c0003` – «Abzugsfähige behinderungsbedingte Kosten 350»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0202.md) `tg-wl-2026__c0202` – «Danach ziehen Sie»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0204.md) `tg-wl-2026__c0204` – «Total behinderungsbedingte Kosten (Ziff. 17) Fr. 500»
  - [WL TG 2026 S. 42–43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0200.md) `tg-wl-2026__c0200` – «gehörlose Personen Fr. 2'500»
  - [WL TG 2026 S. 42–43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0200.md) `tg-wl-2026__c0200` – «Bezügerinnen/Bezüger einer Hilflosenentschädigung mittleren Grades Fr. 5'000»
  - [WL TG 2026 S. 42–43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0200.md) `tg-wl-2026__c0200` – «Bezügerinnen/Bezüger einer Hilflosenentschädigung schweren Grades Fr. 7'500»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0199.md) `tg-wl-2026__c0199` – «Solche Kosten können auch von einer behinderten Person nur insoweit abgezogen»
  - [StP 29 Nr. 2](../../chunks/tg/dauernd/tg-stp-29-2/tg-stp-29-2__c0006.md) `tg-stp-29-2__c0006` – «Im Zusammenhang mit der Fahrt zur Arbeit entstandene behinderungsbedingte Mehrkosten sind nicht unter den Berufsauslagen»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0197.md) `tg-wl-2026__c0197` – «vollständig von den Einkünften in Abzug bringen.»

<a id="form-5-1-d-abzug-krankheitskosten"></a>
### Ziff. Form. 5.1 D – Abzugsfähige Krankheits- und Unfallkosten nach Selbstbehalt 5% von Ziff. 22 (Code 364) → Form. 1 Ziff. 23.1

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Rechenzeile mit Selbstbehalt; Nettoeinkommen Ziff. 22 (Staat links / Bund rechts)
- **Rein:** Übertrag Total A und Total B, Spalte Krankheit/Unfall · Form. 1 Ziff. 22 → Nettoeinkommen Kanton (links) / Bund (rechts) · Ärztliche Anordnung lebensnotwendige Diät (für Pauschale)
- **Rechnen:** je Spalte: (A − B) − 5% × Ziff. 22 der Spalte, nur positiv → Ziff. 23.1; z.B. Kanton 8'600 − 5% × 40'000 = 6'600 / Bund 8'600 − 5% × 44'000 = 6'400
- **Regel:** Netto-Auslagen (A minus B) abzüglich 5% des Nettoeinkommens gemäss Ziff. 22, Staat und Bund je mit eigenem Nettoeinkommen; Übertrag in Ziff. 23.1. Diätpauschale Fr. 2'500 (z.B. Zöliakie, nicht Diabetes) anstelle der effektiven Kosten.
- **Beachten:** Diät-Pauschale 2'500 statt effektiv (z.B. Zöliakie; nicht Diabetes; nicht bei Kostenübernahme durch Dritte)
- **Beachten:** Nachweis der Kosten mit der Steuererklärung einreichen
- **Beachten:** Selbstbehalt je Spalte mit eigenem Nettoeinkommen → Abzug Kanton ≠ Bund
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten: abziehbar, soweit selbst getragen und ueber 5 % des Nettoeinkommens (Ziff. 22 Steuererklaerung). Diaet-Pauschale Fr. 2'500 (z.B. Zoeliakie, nicht Diabetes).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
- **Quellen:**
  - [Formular 5.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-1-2026/tg-form-05-1-2026__c0004.md) `tg-form-05-1-2026__c0004` – «abzüglich Selbstbehalt (5% von Ziffer 22 der Steuererklärung)»
  - [WL TG 2026 S. 43](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0203.md) `tg-wl-2026__c0203` – «ziehen Sie einen Selbstbehalt von 5% des Nettoeinkommens gemäss Ziffer 22 der Steuererklä-»
  - [WL TG 2026 S. 43–44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0205.md) `tg-wl-2026__c0205` – «Total der Auslagen für Krankheits- und Unfallkosten Fr. 8'600 Fr. 8'600»
  - [WL TG 2026 S. 43–44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0205.md) `tg-wl-2026__c0205` – «Abzug Krankheits- und Unfallkosten (Ziff. 23.1) Fr. 6'600 Fr. 6'400»
  - [WL TG 2026 S. 42](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0196.md) `tg-wl-2026__c0196` – «Krankheitskosten eine Pauschale von Fr. 2'500 geltend machen. An Diabetes erkrankte Personen»
  - [KS 11 S. 5–6](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0009.md) `bund-ks-11__c0009` – «eine Pauschale von CHF 2'500.-- geltend gemacht werden»

## Hilfsblatt Versicherungsprämien (Form. 5.2)

<a id="form-5-2-a-1-a-6-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 A.1–A.6 – Versicherungsprämien und Sparzinsen: private Krankenversicherung netto, private Unfallversicherung, Lebens-/Rentenversicherungen, erhaltene Sparzinsen, Krankentaggeld gemäss Lohnausweis; Total (Code 324 / «A5»)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Jahresbestätigung Krankenkasse (Prämie abzüglich IPV), Policen/Prämienrechnungen, Zinsausweise (Sparzinsen gemäss Formular 2), Lohnausweis (Krankentaggeldprämie)
- **Rein:** Jahresbestätigung Krankenkasse → Prämie netto nach IPV (A.1) · Prämienrechnungen/Policen private Unfall-, Lebens-, Rentenversicherung (A.2–A.3) · Formular 2 Wertschriftenverzeichnis → erhaltene Sparzinsen (A.4) · Lohnausweis → Krankentaggeldprämie (A.5)
- **Rechnen:** Σ A.1–A.5 = Total «A5» (Code 324); A.1 = KK-Prämie − in der Steuerperiode erhaltene IPV (inkl. via EL und Nachzahlungen)
- **Regel:** Ziff. 1: Nettoprämie Krankenkasse = Prämie abzüglich in der Steuerperiode erhaltener Prämienverbilligungen (IPV; inkl. über EL ausgerichtete IPV und Nachzahlungen). Ziff. 2: private Unfallversicherung (ohne NBU). Ziff. 3: Lebens-/Rentenversicherung. Ziff. 4: im Jahr 2026 erhaltene Sparzinsen. Ziff. 5: Krankentaggeld gemäss Lohnausweis. Deklaration der KK-Prämien wird vorausgesetzt (sonst kann Abzug verweigert werden).
- **Beachten:** Private KK-Prämien zwingend deklarieren, sonst kann der Versicherungsabzug ganz entfallen
- **Beachten:** Private Unfallversicherung ohne NBUV (diese gehört zu Form. 1 Ziff. 15.4)
- **Beachten:** Sparzinsen: im Steuerjahr erhaltene Zinsen auf Bank-/Postkonten, Obligationen, Darlehen
- **Quellen:**
  - [Formular 5.2 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-2-2026/tg-form-05-2-2026__c0001.md) `tg-form-05-2-2026__c0001` – «1. private Krankenversicherung (netto, nach Abzug Prämienverbilligung gemäss Bestätigung Versicherung)»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0207.md) `tg-wl-2026__c0207` – «Person im Umfang der erhaltenen Prämienverbilligungen. In Ziffer 1 zu deklarieren ist»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0206.md) `tg-wl-2026__c0206` – «Die Deklaration der Prämien der privaten Krankenversicherung wird vorausgesetzt.»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0206.md) `tg-wl-2026__c0206` – «Bei fehlender Deklaration behält sich die Veranlagungsbehörde vor»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0208.md) `tg-wl-2026__c0208` – «Prämien für die private Unfallversicherung (ausgenommen NBUV, vgl.»
  - [WL TG 2026 S. 44](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0208.md) `tg-wl-2026__c0208` – «Die im 2026 erhaltenen Zinsen von Sparkapitalien (Bank- und Postkontoguthaben jeder Art»

<a id="form-5-2-b-1-b-4-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 B.1–B.4 – Maximaler Abzug Versicherungsprämien/Sparzinsen: gemeinsam besteuerte Fr. 7'000 Staat / 3'700 Bund (ohne Säule 2/3a: Bund 5'550); alleinstehend Fr. 3'500 / 1'800 (Bund ohne Säule 2/3a 2'700); je Kind/unterstützte Person Fr. 1'000 / 700 (Code 328, «B4»)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien (Zivilstand, Kinder, Säule 2/3a-Beiträge ja/nein)
- **Rein:** Personalien → gemeinsam besteuert / alleinstehend · Kinder-/Unterstützungsabzüge Form. 1 → Anzahl Kinder/unterstützte Personen · Bescheinigungen Säule 2/3a → Beiträge geleistet ja/nein (nur Bund relevant)
- **Rechnen:** Kanton: 7'000 gemeinsam / 3'500 übrige + 1'000 je Kind/Unterstützte; Bund: 3'700 / 1'800 (ohne Säule 2/3a 5'550 / 2'700) + 700 je Kind/Unterstützte
- **Regel:** Der erhöhte Bundesabzug ohne Beiträge an Säule 2/3a (Fr. 5'550 bzw. 2'700) kann nicht zusammen mit dem ordentlichen Abzug beansprucht werden. Kinder-/Unterstützungszuschlag nur bei geltend gemachtem Kinder-/Unterstützungsabzug.
- **Beachten:** Bund: erhöhter Betrag ohne Säule 2/3a nicht zusammen mit 3'700 bzw. 1'800
- **Beachten:** Kinderzuschlag nur, wenn Kinder-/Unterstützungsabzug geltend gemacht werden kann
- **Beachten:** Getrennte Eltern: Kanton folgt Kinderabzug; Bund minderjährig → Alimentenempfänger, volljährig i.d.R. → Unterhaltszahler
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
  - [WL TG 2026 S. 44–45](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0210.md) `tg-wl-2026__c0210` – «demjenigen Elternteil zugesprochen, welcher auch den Kinderabzug geltend machen kann»
  - [WL TG 2026 S. 45](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0211.md) `tg-wl-2026__c0211` – «diese Kinder dem die Kinderunterhaltsbeiträge empfangenden Elternteil zu.»
  - [WL TG 2026 S. 45](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0212.md) `tg-wl-2026__c0212` – «ist dies in der Regel derjenige Elternteil, welcher die Unterhaltszahlungen leistet.»

<a id="form-5-2-c-abzug-versicherungspraemien"></a>
### Ziff. Form. 5.2 C – Zulässiger Abzug: niedrigerer Betrag von «A5» und «B4» (Code 330) → Form. 1 Ziff. 14

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Staat Zeile 1 / Bund Zeile 2)
- **Rein:** Übertrag Total «A5» (Teil A) und «B4 Staat» / «B4 Bund» (Teil B)
- **Rechnen:** Staat: min(A5; B4 Staat); Bund: min(A5; B4 Bund) → Form. 1 Ziff. 14 (Code 330), Spalten Staat/Bund
- **Regel:** Staat: min(A5; B4 Staat); Bund: min(A5; B4 Bund); Übertrag in Ziff. 14, Spalten Staat/Bund.
- **Beachten:** WL nennt für Staat «A7» – massgebend ist «A5» gemäss Formular
- **Beachten:** Zeile 1 Staatssteuer, Zeile 2 Bundessteuer
- **Bemerkung:** Hinweis Prüfung: WL c0213 nennt für den Staatsabzug «A7», Formular 5.2 und Bundesabsatz «A5» – massgebend ist das Total A (Code 324, «A5»).
- **Quellen:**
  - [Formular 5.2 TG 2026 S. 1](../../chunks/tg/2026/tg-form-05-2-2026/tg-form-05-2-2026__c0003.md) `tg-form-05-2-2026__c0003` – «1. Staatssteuer: der niedrigere Betrag von «A5» oder «B4 Staat» 330»
  - [WL TG 2026 S. 45–46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0213.md) `tg-wl-2026__c0213` – «Der für die direkte Bundessteuer zulässige Abzug entspricht dem niedrigeren der unter „A5“ und»

## Hilfsblatt Zuwendungen (Form. 6)

<a id="form-6-spalte-parteien-code-347-abzug-parteispenden"></a>
### Ziff. Form. 6 Spalte Parteien (Code 347) – Mitgliederbeiträge und Zuwendungen an politische Parteien (Total B) → Form. 1 Ziff. 15.5

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Quittung/Bescheinigung ab Fr. 1'000 pro Zuwendung
- **Rein:** Quittungen/Bescheinigungen Partei → Mitgliederbeiträge, Zuwendungen · Formular 6 Spalte politische Parteien → Total B
- **Rechnen:** Kanton: min(Σ Parteien; 10'000); Bund: min(Σ Parteien; 10'600) → Form. 1 Ziff. 15.5 (Code 347)
- **Regel:** Einzeln mit genauer Bezeichnung und Adresse der Partei auflisten; Maximum Staat Fr. 10'000 / Bund Fr. 10'600. Keine Pauschalvermerke.
- **Beachten:** Partei: im Parteienregister (Art. 76a BPR) oder in einem kantonalen Parlament vertreten oder mind. 3% Stimmen
- **Beachten:** Einzeln mit Name und Sitz der Partei; Sammel-/Pauschalvermerke werden nicht anerkannt
- **Beachten:** Belege ab Fr. 1'000 pro Zuwendung beilegen; kleinere auf Verlangen
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeitraege und Zuwendungen an politische Parteien: max. Fr. 10'000 (Staats- und Gemeindesteuern); Bund Fr. 10'600.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister / kantonales Parlament / mind. 3 % Stimmen): bis Gesamtbetrag CHF 10'600.)**
- **Bund:** Max. Fr. 10'600.
- **Quellen:**
  - [Formular 6 TG 2026 S. 1](../../chunks/tg/2026/tg-form-06-2026/tg-form-06-2026__c0003.md) `tg-form-06-2026__c0003` – «Staatssteuer: max. Fr. 10 000.– Bundessteuer: max. Fr. 10 600.–»
  - [Formular 6 TG 2026 S. 1](../../chunks/tg/2026/tg-form-06-2026/tg-form-06-2026__c0001.md) `tg-form-06-2026__c0001` – «Ab Fr. 1000.– pro Zuwendung reichen Sie bitte die entsprechende Quittung oder Bescheinigung»
  - [StG TG § 34](../../chunks/tg/2025/tg-stg/tg-stg__par-34-t5.md) `tg-stg__par-34-t5` – «in einem kantonalen Parlament vertreten sind, oder»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t3.md) `bund-dbg-2026__art-33-t3` – «in einem kantonalen Parlament vertreten sind, oder»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0216.md) `tg-wl-2026__c0216` – «im Parteienregister nach Artikel 76a des Bundesgesetzes über die politischen Rechte»
  - [WL TG 2026 S. 46–47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0218.md) `tg-wl-2026__c0218` – «einzeln und unter Angabe von Name und Sitz der empfangenden Institution»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0217.md) `tg-wl-2026__c0217` – «oder ähnlichen Vermerken werden nicht anerkannt»

<a id="form-6-spalte-gemeinn-tzig-code-366-abzug-spenden"></a>
### Ziff. Form. 6 Spalte gemeinnützig (Code 366) – Freiwillige Zuwendungen für gemeinnützige oder öffentliche Zwecke (Total) – Abzugsberechnung → Form. 1 Ziff. 23.2

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigung/Quittung der steuerbefreiten Institution ab Fr. 1'000 pro Zuwendung
- **Rein:** Spendenbestätigung/Quittung steuerbefreite Institution → Betrag je Zuwendung · Formular 6 Spalte gemeinnützig → Total B · Form. 1 Ziff. 22 → Nettoeinkommen Kanton/Bund
- **Rechnen:** Kanton: min(Σ − 200; NE ≤ 40'000: 8'000, sonst 20% × NE); Bund: falls Σ ≥ 100: min(Σ; 20% × NE Bund); NE = Ziff. 22 → Ziff. 23.2
- **Regel:** Staat: Selbstbehalt Fr. 200 (nur der übersteigende Betrag), dann Nettoeinkommen (Ziff. 22) bis Fr. 40'000: max. Fr. 8'000; darüber max. 20% des Nettoeinkommens. Bund: ab Fr. 100 gesamthaft, ohne Selbstbehalt, max. 20% des Nettoeinkommens.
- **Beachten:** Nur an steuerbefreite jur. Personen mit Sitz CH (öffentlich/gemeinnützig) sowie Bund, Kantone, Gemeinden
- **Beachten:** Nicht abziehbar: Sitz im Ausland; befreit für religiöse, wohltätige, kulturelle, gesellige, sportliche Zwecke; Ehrenamt
- **Beachten:** Belege ab Fr. 1'000 je Zuwendung; keine Pauschalvermerke; Liste geprüfter Institutionen auf steuerverwaltung.tg.ch
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 200 (Freiwillige Zuwendungen: abziehbar, soweit sie gesamthaft Fr. 200 uebersteigen (Selbstbehalt Fr. 200). Bund: ab Fr. 100 ohne Selbstbehalt.)** · Bund **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn im Steuerjahr mindestens CHF 100 erreicht.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen: max. 20 % des Nettoeinkommens (Ziff. 22); bei Nettoeinkommen bis Fr. 40'000 max. Fr. 8'000.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**
- **Bund:** Bund: max. 20% des Nettoeinkommens, kein Selbstbehalt (ab Fr. 100).
- **Quellen:**
  - [Formular 6 TG 2026 S. 1](../../chunks/tg/2026/tg-form-06-2026/tg-form-06-2026__c0003.md) `tg-form-06-2026__c0003` – «über Fr. 40000.–: max. 20% vom Nettoeinkommen 366»
  - [WL TG 2026 S. 46–47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0218.md) `tg-wl-2026__c0218` – «Übertragen Sie die geleisteten freiwilligen Zuwendungen (Maximalabzüge beachten) auf Seite 3 der»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0215.md) `tg-wl-2026__c0215` – «Soweit die freiwilligen Zuwendungen gesamthaft Fr. 200 übersteigen, können Sie kantonal»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0215.md) `tg-wl-2026__c0215` – «Sofern die freiwilligen Zuwendungen insgesamt den Betrag von Fr. 100 erreichen»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0214.md) `tg-wl-2026__c0214` – «Nicht abziehen können Sie dagegen freiwillige Zuwendungen an Körperschaften, welche im Hinblick»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0214.md) `tg-wl-2026__c0214` – «Leistungen an Bund, Kantone, Gemeinden und deren Anstalten»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0217.md) `tg-wl-2026__c0217` – «oder ähnlichen Vermerken werden nicht anerkannt»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0214.md) `tg-wl-2026__c0214` – «auf religiöse, wohltätige, kulturelle, gesellige oder sportliche Zwecke von der Steuerpflicht befreit»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0214.md) `tg-wl-2026__c0214` – «sowie an juristische Personen mit Sitz im Ausland.»
  - [WL TG 2026 S. 46](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0214.md) `tg-wl-2026__c0214` – «Ebenfalls nicht abzugsfähig sind unentgelt- liche ehrenamtliche Arbeitsleistungen.»

## Hilfsblatt Schuldenverzeichnis (Form. 4.1)

<a id="form-4-1-a-schulden-privat"></a>
### Ziff. Form. 4.1 A – Privatschulden: Gläubiger, Schuld am 31.12., Zinssatz, fällige Schuldzinsen; Total (Code 455 Schulden / 286 Zinsen)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Hypothekar-/Kreditbestätigung der Bank per 31.12.2026 mit Zinsausweis 2026
- **Rein:** Hypothekarbestätigung/Zinsausweis Bank → Schuld 31. Dez., Zinssatz, 2026 fällige Zinsen · Kredit-/Darlehensvertrag, Zinsbestätigung (privat) → Gläubiger mit Adresse, Saldo, Zins · Steuerschlussrechnung 2026 → belastete Ausgleichszinsen · WEF-Bestätigung (selbstbewohntes Wohneigentum) → erhaltene Zusatzverbilligung
- **Rechnen:** Code 455 = Σ Schulden 31. Dez.; Code 286 = Σ 2026 fällige Zinsen + Ausgleichszinsen − WEF-Zusatzverbilligung; max. Vermögensertrag + Fr. 50'000 (Kanton und Bund)
- **Regel:** Gläubiger/in mit genauer Adresse und Zinssatz unerlässlich. Nur 2026 fällig gewordene Schuldzinsen (keine Ratazinsen). Amortisationen sind keine Schuldzinsen.
- **Beachten:** Keine Schuldzinsen: Amortisationen, Bau-/Landkreditzinsen in Bauphase (Anlagekosten); Leasingzinsen nicht abziehbar
- **Beachten:** Baurechtszinsen nur bei Fremdvermietung abziehbar, nicht bei Eigengebrauch
- **Beachten:** Nur 2026 fällig gewordene Zinsen, keine Ratazinsen; Gläubiger mit genauer Adresse und Zinssatz
- **Quellen:**
  - [Formular 4.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-1-2026/tg-form-04-1-2026__c0001.md) `tg-form-04-1-2026__c0001` – «Total Privatschulden 455 286»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0169.md) `tg-wl-2026__c0169` – «Unerlässlich ist insbesondere die Angabe der Gläubigerin bzw. des Gläubigers»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0170.md) `tg-wl-2026__c0170` – «Die im 2026 mit der Steuerschlussrechnung belasteten Ausgleichszinsen können Sie ebenfalls als»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0170.md) `tg-wl-2026__c0170` – «erhaltene Zusatzverbilligungen nach dem Gesetz über die Wohnbau- und Eigentumsförderung (WEF)»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0170.md) `tg-wl-2026__c0170` – «Tragen Sie nur die im Jahre 2026 fällig gewordenen Schuldzinsen ein (keine Ratazinsen).»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «und unbeweglichem Vermögen und weiterer Fr. 50 000 in Abzug bringen»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «Kapitalrückzahlungen wie Amortisationen von Grundpfandschulden stellen keine Schuldzinsen dar»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «Bezahlte Baurechtszinsen sind nur bei Fremdvermietung der Liegenschaft»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «Leasingzinsen sind grundsätzlich nicht abzugsfähig»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t1.md) `bund-dbg-2026__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken»

<a id="form-4-1-b-schulden-privat"></a>
### Ziff. Form. 4.1 B – Geschäftsschulden: Gläubiger, Schuld am 31.12., Zinssatz, fällige Schuldzinsen; Total (Code 460 / 288)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz/Schuldenaufstellung Geschäft
- **Rein:** Jahresrechnung/Bilanz 2026 → Geschäftsschulden 31. Dez. · Bankbestätigung Geschäftskredit/-hypothek → Gläubiger, Zinssatz, 2026 fällige Zinsen · Erfolgsrechnung → bereits verbuchter Zinsaufwand (Doppelabzug vermeiden)
- **Rechnen:** Code 460 = Σ Geschäftsschulden 31. Dez.; Code 288 = Σ 2026 fällige Geschäftsschuldzinsen, soweit nicht schon in Form. 1 Ziff. 2 abgezogen
- **Regel:** Schuldzinsen aus selbständiger Erwerbstätigkeit hier nur, wenn nicht bereits im Einkommen Ziff. 2 abgezogen.
- **Beachten:** Begrenzung Vermögensertrag + Fr. 50'000 gilt nur für private Schuldzinsen
- **Beachten:** Gläubiger mit genauer Adresse und Zinssatz angeben
- **Quellen:**
  - [Formular 4.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-1-2026/tg-form-04-1-2026__c0002.md) `tg-form-04-1-2026__c0002` – «Total Geschäftsschulden 460 288»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0170.md) `tg-wl-2026__c0170` – «Tragen Sie Schuldzinsen aus selbständiger Erwerbstätigkeit hier nur ein, sofern Sie diese nicht»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «Sie können private Schuldzinsen höchstens im Umfang der deklarierten Erträge aus beweglichem»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «und unbeweglichem Vermögen und weiterer Fr. 50 000 in Abzug bringen»
  - [KS 22a S. 5](../../chunks/bund/dauernd/bund-ks-22a/bund-ks-22a__c0014.md) `bund-ks-22a__c0014` – «verbuchte Verbindlichkeiten, die für private Zwecke verwendet wurden, sind jedoch dem Privatvermögen zuzuordnen»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0169.md) `tg-wl-2026__c0169` – «Unerlässlich ist insbesondere die Angabe der Gläubigerin bzw. des Gläubigers»

<a id="form-4-1-c-schulden-privat"></a>
### Ziff. Form. 4.1 C – Zusammenzug: Total Privat- und Geschäftsschulden (Code 466) → Form. 1 Ziff. 34; Total Schuldzinsen (Code 290) → Form. 1 Ziff. 11

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag aus Form. 4.1 A (Codes 455/286) · Übertrag aus Form. 4.1 B (Codes 460/288)
- **Rechnen:** Code 466 = 455 + 460 → Form. 1 Ziff. 34 (S. 4); Code 290 = 286 + 288 → Form. 1 Ziff. 11 (S. 3)
- **Regel:** Total Schulden in Ziff. 34 (Seite 4), Total Schuldzinsen in Ziff. 11 (Seite 3).
- **Beachten:** Private Schuldzinsen max. Vermögensertrag + Fr. 50'000 (Kanton und Bund)
- **Beachten:** Geschäftszinsen, die schon in Form. 1 Ziff. 2 abgezogen sind, nicht nochmals erfassen
- **Quellen:**
  - [Formular 4.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-1-2026/tg-form-04-1-2026__c0003.md) `tg-form-04-1-2026__c0003` – «Total Privat- und Geschäftsschulden 466 290»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0169.md) `tg-wl-2026__c0169` – «Übertragen Sie das Total der Schuldzinsen in Ziffer 11 auf Seite 3, und das»
  - [Formular 4.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-1-2026/tg-form-04-1-2026__c0001.md) `tg-form-04-1-2026__c0001` – «Total Privatschulden 455 286»
  - [Formular 4.1 TG 2026 S. 1](../../chunks/tg/2026/tg-form-04-1-2026/tg-form-04-1-2026__c0002.md) `tg-form-04-1-2026__c0002` – «Total Geschäftsschulden 460 288»
  - [WL TG 2026 S. 36–37](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0171.md) `tg-wl-2026__c0171` – «und unbeweglichem Vermögen und weiterer Fr. 50 000 in Abzug bringen»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t1.md) `bund-dbg-2026__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken»
  - [WL TG 2026 S. 36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0170.md) `tg-wl-2026__c0170` – «Tragen Sie Schuldzinsen aus selbständiger Erwerbstätigkeit hier nur ein, sofern Sie diese nicht»

## Hilfsblatt Wertschriftenverzeichnis (Form. 2)

<a id="form-2-spalten-1-9-seite-2-3-einkommen-wertschriften"></a>
### Ziff. Form. 2 Spalten 1–9 (Seite 2/3) – Detailverzeichnis: Bezeichnung (Valor/ISIN/IBAN), Zugang/Abgang, Steuerwert 31.12.2026 (Sp. 7), Bruttoertrag mit Verrechnungssteuerabzug (Sp. 8, Kolonne A), ohne Verrechnungssteuerabzug (Sp. 9, Kolonne B)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → E-Steuerauszug / Steuerauszug der Bank (Steuerwerte 31.12., Bruttoerträge); Dividenden-/Zinsabrechnungen; Lotterie-/Spielgewinnbestätigung
- **Rein:** E-Steuerauszug/Steuerauszug Bank → Steuerwert 31.12. (Sp. 7), Bruttoerträge Sp. 8/9 · Kauf-/Verkaufsabrechnungen → Datum Zugang/Abgang 2026 · Dividenden-/Zinsabrechnung Ausland → Sp. 9; USA-Rückbehalt/Quellensteueranrechnung via DA-1 · Gewinnbestätigung Lotterie/Grossspiel (Original) → Sp. 8 bzw. 9
- **Rechnen:** Sp. 7 = Stück × Kurs Ende Dez. 2026 (ESTV-Kursliste) bzw. Saldo 31.12.; Sp. 8 brutto mit VSt-Abzug, Sp. 9 ohne; Ausland: netto + rückforderbare/anrechenbare QSt
- **Regel:** Sp. 8: Erträge mit Verrechnungssteuerabzug (CH-Dividenden/-Zinsen, Kontozinsen über Fr. 200 brutto/Jahr oder mehrfache Vergütung, Lotterietreffer über Fr. 1'000). Sp. 9: Erträge ohne VSt-Abzug (Kleinzinsen bis Fr. 200, ausländische Titel und Guthaben, Darlehen, Hypothekarforderungen, Ausgleichs-/Rückerstattungszinsen). Brutto deklarieren (Marchzinsen etc.). Steuerwert = Börsenkurs Ende Dezember 2026 (ESTV-Kursliste). Kinder-Vermögen Jg. 2008 und jünger mitdeklarieren. Codes zur Zuordnung (01–06: Nutzniessung, Geschäftsvermögen, Erbschaft, qualifizierte Beteiligung). Ausländische Quellensteuern: Formular DA-1. Steuerauszug der Bank kann das Detail ersetzen und bleibt bei den Akten.
- **Beachten:** Kontozins > Fr. 200/Jahr oder mehrfache Vergütung → Sp. 8, sonst Sp. 9; Marchzinsen aus Titelverkauf nicht
- **Beachten:** Kindervermögen: WL S. 6/Ziff. 36 → Jg. 2009 u. jünger (Jg. 2008 selbständig); WL Form. 2 nennt Jg. 2008 → prüfen
- **Beachten:** Grossspielgewinn: nur kantonal steuerbarer Teil in Sp. B (z.B. Fr. 1'025'000 → Sp. B Fr. 25'000)
- **Bund:** Gleiche Erträge für Staat und Bund (Steuerwerte nur Staatssteuer).
- **Quellen:**
  - [Formular 2 TG 2026 S. 2](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0005.md) `tg-form-02-2026__c0005` – «Detailverzeichnis Wertschriften und Guthaben»
  - [WL TG 2026 S. 32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0150.md) `tg-wl-2026__c0150` – «Dies gilt auch für Zinsen von Bank- und Postkonti aller Art, soweit die Brutto-»
  - [WL TG 2026 S. 32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0152.md) `tg-wl-2026__c0152` – «Bank- und Postkonti aller Art, deren Bruttozins im Kalenderjahr Fr. 200 nicht übersteigt und»
  - [WL TG 2026 S. 30–31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0143.md) `tg-wl-2026__c0143` – «Für in der Schweiz kotierte Wertpapiere gilt der Börsenkurs Ende des Monats Dezember 2026.»
  - [WL TG 2026 S. 30](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0140.md) `tg-wl-2026__c0140` – «bestehende Vermögen per 31.12.2026»
  - [WL TG 2026 S. 30](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0142.md) `tg-wl-2026__c0142` – «Bei Änderungen im Bestand von Obligationen, Aktien und Fondsanteilen im Jahre 2026 geben»
  - [WL TG 2026 S. 33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0154.md) `tg-wl-2026__c0154` – «Als steuerbarer Ertrag ausländischer Wertpapiere gilt der Nettobetrag gemäss»
  - [WL TG 2026 S. 33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0154.md) `tg-wl-2026__c0154` – «zuzüglich ausländischer Quellensteuern, soweit sie aufgrund eines»
  - [WL TG 2026 S. 33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0154.md) `tg-wl-2026__c0154` – «Deklarieren Sie im Formular DA-1 amerikanische Vermögenswerte»
  - [WL TG 2026 S. 33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0155.md) `tg-wl-2026__c0155` – «Mit Formular DA-1 können Sie die Anrechnung ausländischer Quellensteuern für Dividenden»
  - [WL TG 2026 S. 32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0151.md) `tg-wl-2026__c0151` – «herrührenden Marchzinsen führen Sie jedoch bitte nicht auf»
  - [WL TG 2026 S. 32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0151.md) `tg-wl-2026__c0151` – «Legen Sie bei den Lotterietreffern aller Art die Auszahlungsbescheinigung im Original»
  - [WL TG 2026 S. 6](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0012.md) `tg-wl-2026__c0012` – «Personen mit Jahrgang 2008 sind somit für die Steuerperiode 2026 erstmals selbständig deklarationspflichtig»
  - [WL TG 2026 S. 30](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0140.md) `tg-wl-2026__c0140` – «Vermögen und Erträge von Kindern unter Ihrer elterlichen Sorge (Jahrgang 2008 und jünger)»
  - [WL TG 2026 S. 27–28](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0128.md) `tg-wl-2026__c0128` – «für jedes nicht selbständig besteuerte Kind (Jahrgang 2009 und jünger)»
  - [WL TG 2026 S. 31–32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0148.md) `tg-wl-2026__c0148` – «den Staats- und Gemeindesteuern steuerbar ist, in Spalte B zu deklarieren»
  - [WL TG 2026 S. 31–32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0148.md) `tg-wl-2026__c0148` – «Gewinn Fr. 1'025'000 aus Teilnahme an nach dem BGS zugelassen Grossspiel»
  - [WL TG 2026 S. 31–32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0148.md) `tg-wl-2026__c0148` – «Somit ist in der Spalte A nichts und in der Spalte B Fr. 25'000 zu deklarieren»

<a id="form-2-ziff-7-im-formular-chunk-17-code-148-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. Form. 2 Ziff. 7 (im Formular-Chunk «17», Code 148) – Vermögensverwaltungskosten (Code 148)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Depotgebührenausweis der Bank (nur Verwahrung/Verwaltung)
- **Rein:** Steuerauszug/Depotauszug Bank → Steuerwert der durch Dritte verwalteten Wertschriften (Basis) · Depotgebührenabrechnung Bank → effektive Kosten (nur bei höherem Nachweis)
- **Rechnen:** Pauschal: min(2‰ × Steuerwert durch Dritte verwalteter Wertschriften des PV; Fr. 6'000) oder höhere effektive Kosten mit Nachweis → Code 148
- **Regel:** Pauschal 2 Promille des Steuerwerts der durch Dritte verwalteten Wertschriften des Privatvermögens, höchstens Fr. 6'000 (Darlehen, Bankguthaben, nichtkotierte qualifizierte Beteiligungen nicht in der Basis); höherer Nachweis vorbehalten. Abziehbar: Depotgebühren; nicht abziehbar: Kommissionen, Anlageberater, Tresor.
- **Beachten:** Wertschriften im Depot einer Bank gelten als durch Dritte verwahrt/verwaltet – ein Vermögensverwaltungsmandat ist nicht Voraussetzung der Pauschale
- **Beachten:** Formular 2 überträgt nur ein Total in Ziff. 4: Kantonsspalte nach Abzug Code 148; Bundesspalte siehe «Bund»
- **Beachten:** Basis ohne Darlehen, Bankguthaben aller Art, nichtkotierte qualifizierte Beteiligungen (§ 22 Abs. 2 StG)
- **Beachten:** Nicht abziehbar: Kontoführungsgebühren, Anlageberater, Kommissionen/Spesen An-/Verkauf, Tresor für Schmuck/Bilder
- **Beachten:** Ziffer: WL nennt Ziff. 7, Formular-Chunk zeigt «17» (Layout) → Original-PDF S. 2 prüfen
- **Bund:** Belegt sind nur effektive Verwahrungskosten (Depot-, Safegebühren, Inkassospesen; bund-wl-2a-2026__c0060); eine Bundes-Pauschale ist im Wiki nicht belegt → Bundesspalte effektiv (ohne Gebührenausweis 0) oder Kantonspauschale nur mit Vorbehalt (Fachperson).
- **Bemerkung:** Ziffernbezeichnung im Formular-Chunk (c0007) ist durch Layout verfälscht («11.–19.»); Wegleitung nennt Ziff. 1–10 (Ziff. 7 = Vermögensverwaltungskosten). Original-PDF Seite 2 prüfen.
- **Quellen:**
  - [Formular 2 TG 2026 S. 2](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0006.md) `tg-form-02-2026__c0006` – «17. Vermögensverwaltungskosten Code 148»
  - [WL TG 2026 S. 33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0158.md) `tg-wl-2026__c0158` – «Der Pauschalabzug beträgt maximal Fr. 6'000.»
  - [WL TG 2026 S. 33–34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0159.md) `tg-wl-2026__c0159` – «Kontoführungsgebühren, Auslagen für Anlageberater, Kommissionen oder Spesen für An- und»
  - [WL TG 2026 S. 33–34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0159.md) `tg-wl-2026__c0159` – «von privat genutztem Schmuck oder Bildern (Miete für Tresor/Schrankfächer)»
  - [StV TG § 10a](../../chunks/tg/2025/tg-stv/tg-stv__par-10a.md) `tg-stv__par-10a` – «pauschal 2 Promille des Steuerwertes der durch Dritte verwalteten Wertschriften des Privatvermögens, maximal Fr. 6'000 abgezogen werden»

<a id="form-2-ziff-8-im-formular-chunk-18-code-145-einkommen-lotterie-gewinne"></a>
### Ziff. Form. 2 Ziff. 8 (im Formular-Chunk «18», Code 145) – Einsatzkosten für steuerbare Gewinne aus Geldspielen (Code 145)

- **Schlüssel:** `einkommen.lotterie_gewinne` (Lotterie-/Geldspielgewinne (steuerbarer Teil)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Gewinnbestätigung (Lotterie, Grossspiel, Online-Spielbank)
- **Rein:** Gewinn-/Auszahlungsbescheinigung (Lotterie, Swisslotto, Sport-Toto, Grossspiel; Original) → Einzelgewinn · Auszug Online-Spielerkonto → 2026 abgebuchte Spieleinsätze · Verrechnungssteuerausweis zum Geldspielgewinn (beilegen)
- **Rechnen:** Je steuerbarer Einzelgewinn: min(5% × Gewinn; Kanton Fr. 5'000 / Bund Fr. 5'400); Online-Spielbank: min(Einsätze; Kanton Fr. 25'000 / Bund Fr. 26'800)
- **Regel:** Pauschal 5% jedes einzelnen steuerbaren Gewinns (Lotterien/Geschicklichkeitsspiele zur Verkaufsförderung, Grossspiele), max. Fr. 5'000 pro Gewinn Staat; effektive Einsatzkosten nicht geltend machbar. In der Steuererklärung den Staats-Maximalabzug deklarieren; Korrektur Bund von Amtes wegen.
- **Beachten:** Steuerbar: Lotterie > Kanton Fr. 1'000 / Bund Fr. 1'100 ganz; Grossspiel nur Teil > Kanton 1'000'000 / Bund 1'071'000
- **Beachten:** In SE Kantonsmaximum deklarieren, Bund-Korrektur von Amtes wegen; effektive Einsatzkosten nicht abziehbar
- **Beachten:** Ausländische Geldspielgewinne immer voll steuerbar; Gewinne in inländischen Spielbanken steuerfrei (Kanton/Bund)
- **Limiten:**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'000'000 (Einzelne Gewinne aus BGS-Grossspielen und Online-Spielbankenspielen bis Fr. 1'000'000 steuerfrei; nur der Mehrbetrag ist steuerbar (Bund: Fr. 1'071'000). Kleinspiele nach BGS vollstaendig steuerfrei.)** · Bund **CHF 1'071'000 (Einzelne Gewinne aus nach BGS zugelassenen Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'071'000; darüber steuerbar (abzüglich Einsatzkosten nach Art. 33 Abs. 4 DBG).)**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'000 (Einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsfoerderung bis Fr. 1'000 steuerfrei; wird die Grenze ueberschritten, ist der gesamte Gewinn steuerbar. Auslaendische Lotterien voll steuerbar. Bund: Freigrenze Fr. 1'100.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (Art. 1 Abs. 2 lit. d und e BGS) steuerfrei, sofern die Grenze von CHF 1'100 nicht überschritten wird. Gewinne aus Kleinspielen (BGS) sind steuerfrei.)**
- **Bund:** Max. Fr. 5'400 pro Gewinn (Korrektur von Amtes wegen).
- **Bemerkung:** Online-Spielbankenspiele (nach Bundesgesetz über die Spielbanken zugelassen): abgezogen werden die vom Online-Spielerkonto abgebuchten Spieleinsätze, Maximalabzug Staat Fr. 25'000 / Bund Fr. 26'800 (WL c0161); in der Steuererklärung Staats-Maximum deklarieren, Bund-Korrektur von Amtes wegen. Nummerierung: Wegleitung c0160 nennt «Ziffer 9» für den Pauschalabzug, das Formular zeigt Einsatzkosten vor dem Total (Ziff. 9) – Zeilennummer im Original-PDF prüfen.
- **Quellen:**
  - [Formular 2 TG 2026 S. 2](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0006.md) `tg-form-02-2026__c0006` – «Einsatzkosten und Spieleinsätze für steuerbare Gewinne aus Geldspielen»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0160.md) `tg-wl-2026__c0160` – «pro Gewinn Fr. 5'000 und bei der direkten Bundessteuer Fr. 5'400.»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0161.md) `tg-wl-2026__c0161` – «Fr. 25'000 und bei der direkten Bundessteuer Fr. 26'800.»
  - [WL TG 2026 S. 32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0151.md) `tg-wl-2026__c0151` – «Legen Sie bei den Lotterietreffern aller Art die Auszahlungsbescheinigung im Original»
  - [WL TG 2026 S. 31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0147.md) `tg-wl-2026__c0147` – «dass z.B. Swisslotto und Sport-Toto nicht unter diese Kategorie fallen»
  - [WL TG 2026 S. 30](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0142.md) `tg-wl-2026__c0142` – «dem Wertschriften- und Guthabenverzeichnis bei. Verrechnungssteuerausweise für allfällige»
  - [WL TG 2026 S. 31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0146.md) `tg-wl-2026__c0146` – «Sobald ein einzelner Gewinn die Steuerfreigrenze übersteigt, ist der gesamte Gewinn steuerbar.»
  - [WL TG 2026 S. 31](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0147.md) `tg-wl-2026__c0147` – «Steuerbar ist nur der Anteil des Einzelgewinns, welcher den Steuerfreibetrag übersteigt.»
  - [WL TG 2026 S. 32–33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0153.md) `tg-wl-2026__c0153` – «zur Verkaufsförderungen sind unabhängig des Betrags immer vollumfänglich steuerbar»
  - [WL TG 2026 S. 32](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0149.md) `tg-wl-2026__c0149` – «jedoch gemäss § 26 Ziffer 1 StG Gewinne bei inländischen Spielbanken»
  - [DBG Art. 24](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-24-t2.md) `bund-dbg-2026__art-24-t2` – «die Gewinne, die in Spielbanken mit Spielbankenspielen erzielt werden, die nach dem Geldspielgesetz vom 29. September 2017 (BGS) zugelassen sind»

<a id="form-2-ziff-9-codes-410-150-berechnung-total"></a>
### Ziff. Form. 2 Ziff. 9 (Codes 410 / 150) – Total Steuerwert (Code 410 → Form. 1 Ziff. 30.1) und steuerbarer Ertrag (Code 150 → Form. 1 Ziff. 4)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Form. 2 Ziff. 5 (Zwischentotal II: Steuerwerte, Erträge A+B) · Übertrag Ziff. 6 (Geschäftswertschriften/-erträge lt. Buchhaltung) · Übertrag Ziff. 7 (Code 148) und Ziff. 8 (Code 145)
- **Rechnen:** Code 410 = Ziff. 5 Steuerwerte − Ziff. 6 → Form. 1 Ziff. 30.1; Code 150 = Ziff. 5 Erträge − Ziff. 6 − Ziff. 7 − Ziff. 8 → Form. 1 Ziff. 4
- **Regel:** Total Steuerwerte = Zwischentotal minus Geschäftswertschriften; Total steuerbarer Ertrag = Zwischentotal minus Geschäftsanteil, Vermögensverwaltungskosten und Einsatzkosten.
- **Beachten:** Vorher Ziff. 3 Zwischentotal I, dann Ertrag A in Kolonne B übertragen (Ziff. 4, Code 149)
- **Beachten:** Ziff. 6 nur Werte/Erträge, die schon in Ziff. 2.1/2.2 bzw. 32.1/32.2 erfasst sind
- **Beachten:** Teilbesteuerungsabzug nicht hier, sondern Hilfsblatt (letzte Seite Form. 2) → Form. 1 Ziff. 15.6
- **Quellen:**
  - [Formular 2 TG 2026 S. 2](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0006.md) `tg-form-02-2026__c0006` – «Total Steuerwert und steuerbarer Ertrag»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0162.md) `tg-wl-2026__c0162` – «Steuerwerte von Wertschriften und Guthaben im Privatvermögen übertragen Sie in Ziffer 30.1 auf»
  - [WL TG 2026 S. 33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0157.md) `tg-wl-2026__c0157` – «das Total der Bruttoerträge der Kolonne A in die Ziffer 4 in Kolonne Bruttoertrag B»
  - [WL TG 2026 S. 33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0157.md) `tg-wl-2026__c0157` – «welche laut Buchhaltung bereits in den Geschäftseinkünften (Ziffer 2.1 und/oder Ziffer»

<a id="form-2-ziff-10-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 2 Ziff. 10 – Verrechnungssteueranspruch: 35% von Bruttoertrag Total A (Spalte 8)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Steuerauszug/Dividendenabrechnung mit Verrechnungssteuerabzug; Auszahlungskonto S. 1 Formular 1
- **Rein:** Übertrag Form. 2 Ziff. 3: Zwischentotal I Sp. 8 (Erträge mit VSt, inkl. Beiblätter) · Formular 1 S. 1 → Auszahlungskonto (bei Erstantrag oder Kontoänderung) · Bank-Steuerauszug anstelle Detailangaben → Bestandteil des Antrags
- **Rechnen:** Ziff. 10 = 35% × Total I Bruttoertrag Kolonne A (Sp. 8, Ziff. 3 inkl. Beiblätter)
- **Regel:** 35% der Bruttoerträge Kolonne A (Sp. 8). Rückerstattung nur bei Wohnsitz im Kanton TG am 31.12.2026 und ordnungsgemässer Deklaration der Erträge; Auszahlung auf das gespeicherte Konto (Formular 1 Seite 1). Unterschrift auf Formular 2 erforderlich.
- **Beachten:** Nur bei Wohnsitz TG am 31. Dezember 2026 und deklarierten Erträgen; Form. 2 unterzeichnen
- **Beachten:** Unverteilte Erbschaft: VSt-belastete Erträge nach Erbquote in Sp. A; STWE-Fonds nicht (Form. 25)
- **Beachten:** DA-1: Anrechnung ausländischer Quellensteuer nur, wenn insgesamt > Fr. 100
- **Limiten:**
  - Verrechnungssteuer auf Kapitalerträgen/Geldspielgewinnen (%), Rückerstattung über Wertschriftenverzeichnis: Kanton **–** · Bund **35 % (Verrechnungssteuer 35 % auf Kapitalerträgen (und steuerbaren Geldspielgewinnen); natürliche Personen fordern sie über das Wertschriftenverzeichnis der kantonalen Erklärung zurück (35 % der Erträge mit VSt-Abzug). Bundesrecht, gilt in allen Kantonen: Anspruch verwirkt, wenn die Einkünfte nicht deklariert werden (Art. 23 Abs. 1 VStG) – Ausnahme bei fahrlässiger Nichtangabe und Nachdeklaration bzw. Aufrechnung im noch offenen Verfahren (Art. 23 Abs. 2 VStG); Antrag innert 3 Jahren nach Ablauf des Fälligkeitsjahres (Art. 32 Abs. 1 VStG).)**
- **Quellen:**
  - [Formular 2 TG 2026 S. 2](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0006.md) `tg-form-02-2026__c0006` – «10. Verrechnungssteueranspruch: 35% von Bruttoertrag Total A»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0166.md) `tg-wl-2026__c0166` – «Ein Anspruch auf Rückerstattung der Verrechnungssteuer besteht nur, wenn Sie die Erträge in der»
  - [WL TG 2026 S. 30](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0142.md) `tg-wl-2026__c0142` – «Reichen Sie das Wertschriften- und Guthabenverzeichnis vollständig ausgefüllt und unterzeichnet»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0167.md) `tg-wl-2026__c0167` – «die gewünschte Kontoverbindung für die Auszahlung ein»
  - [WL TG 2026 S. 35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0167.md) `tg-wl-2026__c0167` – «Die mit der Verrechnungsteuer belasteten Erträge aus der unverteilten Erbschaft sind im Umfang der Erbquote in der Spalte A»
  - [WL TG 2026 S. 35–36](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0168.md) `tg-wl-2026__c0168` – «unabhängig von den Anträgen der einzelnen Gemeinschafter, mit dem Formular 25 bei der Eidg.»
  - [WL TG 2026 S. 33](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0155.md) `tg-wl-2026__c0155` – «Wenn die Steueranrechnung (DA-1, Spalte 11) insgesamt den Betrag von Fr. 100 nicht übersteigt»

<a id="form-2-letzte-seite-ziff-1-3-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. Form. 2 letzte Seite Ziff. 1–3 – Hilfsblatt qualifizierte Beteiligungen im Privatvermögen: Name/Sitz, Beteiligungsquote, Beteiligungsertrag; Teilbesteuerungsabzug Staat 40% / Bund 30% (→ Form. 1 Ziff. 15.6)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Dividendenabrechnung; Nachweis Beteiligungsquote (≥10%)
- **Rein:** Dividenden-/Ausschüttungsabrechnung 2026 → Beteiligungsertrag je Gesellschaft · Nachweis Beteiligungsquote (≥ 10% Grund-/Stammkapital) → Spalte Quote · Form. 2 Sp. 8/9 (Code 05) → Ertrag dort bereits brutto deklariert
- **Rechnen:** Ziff. 2 = Σ Beteiligungserträge 2026 (Quote ≥ 10%); Ziff. 3 = Kanton 40% / Bund 30% × Ziff. 2 → Form. 1 Ziff. 15.6 (Spalten Kanton/Bund)
- **Regel:** Antrag durch Ausfüllen des Hilfsblatts nötig. Staat 40% / Bund 30% des Total Beteiligungsertrags (Ziff. 2); Übertrag in Ziff. 15.6 beider Spalten. Beteiligungen im Geschäftsvermögen separat über Formular 14.
- **Beachten:** Antrag nötig; ohne Nachweis Besteuerung zu 100%
- **Beachten:** Steuerbar Kanton 60% / Bund 70%; gilt auch für Gratisaktien, Liquidationsüberschüsse, geldwerte Vorteile
- **Beachten:** Beteiligungen im Geschäftsvermögen nicht hier: Antrag Formular 14 S. 4 (WL; Hilfsblatt nennt «Formular 4»)
- **Bund:** Bund 30%.
- **Quellen:**
  - [Formular 2 TG 2026 S. 4](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0008.md) `tg-form-02-2026__c0008` – «3. Teilbesteuerungsabzug (Staatssteuer 40% / Bundessteuer 30%)»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0164.md) `tg-wl-2026__c0164` – «Die Durchführung des Teilbesteuerungsverfahrens ist jeweils zu beantragen.»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0163.md) `tg-wl-2026__c0163` – «mindestens 10% am Grund- oder Stammkapital»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0163.md) `tg-wl-2026__c0163` – «kantonal zu 60% und beim Bund zu 70% steuerbar»
  - [WL TG 2026 S. 34](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0163.md) `tg-wl-2026__c0163` – «Bei fehlendem Nachweis erfolgt die Besteuerung zu 100%»
  - [WL TG 2026 S. 34–35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0165.md) `tg-wl-2026__c0165` – «Geschäftsvermögen ist auf Seite 4 von Formular 14»
  - [WL TG 2026 S. 34–35](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0165.md) `tg-wl-2026__c0165` – «Übertragen Sie die in Ziffer 3 ermittelten Teilbesteuerungsabzüge auf Seite 3 der Steuererklärung»
  - [Formular 2 TG 2026 S. 2](../../chunks/tg/2026/tg-form-02-2026/tg-form-02-2026__c0005.md) `tg-form-02-2026__c0005` – «qualifiz. Beteiligung im Privatvermögen = 05»

## Hilfsblatt Liegenschaften (Form. 7)

<a id="form-7-steuerwert-vermoegen-liegenschaften"></a>
### Ziff. Form. 7 Steuerwert – Steuerwert der Liegenschaft (je Liegenschaft; Total Code 430 → Form. 1 Ziff. 31)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftensteuerrechnung/Schätzungsverfügung (Steuerwert)
- **Rein:** Liegenschaftensteuerrechnung (Versand Januar 2027) → amtlicher Verkehrswert · Rechtskräftige Schätzung → Verkehrswert bzw. Ertragswert (Landwirtschaft) · Ausserkantonal/Ausland: Steuerwert des Belegenheitsorts · Kaufvertrag/Erbteilung/Schenkung → Zugangs-/Wegfalldatum
- **Rechnen:** Je Liegenschaft: per Ende Steuerperiode rechtskräftiger amtlicher Verkehrswert (landwirtschaftlich: Ertragswert); Σ → Code 430 → Form. 1 Ziff. 31
- **Regel:** Rechtskräftiger amtlicher Verkehrswert (Ertragswert bei Landwirtschaft); Zugangs-/Wegfalldatum bei Kauf/Verkauf/Erbgang angeben.
- **Beachten:** Ausserkantonale/ausländische Liegenschaften zum dortigen Steuerwert; Repartition durch Behörde
- **Beachten:** Am Stichtag nicht abgeschlossene Bauten/Umbauten: Investitionen angemessen deklarieren
- **Beachten:** Angaben: Gemeinde, Kanton/Staat, Art, Baujahr, Anteile, Amtsnummer
- **Quellen:**
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0003.md) `tg-form-07-2026__c0003` – «Total Steuerwerte 430»
  - [WL TG 2026 S. 51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0238.md) `tg-wl-2026__c0238` – «Deklarieren Sie hier den Steuerwert Ihrer Liegenschaft»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0236.md) `tg-wl-2026__c0236` – «rechtskräftigen amtlichen Verkehrswert als Steuerwert an»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0236.md) `tg-wl-2026__c0236` – «setzen Sie den Ertragswert als Steuerwert ein»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0236.md) `tg-wl-2026__c0236` – «der im Januar 2027 versandten Liegenschaftensteuerrechnung entnehmen»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0236.md) `tg-wl-2026__c0236` – «dem dort gültigen Steuerwert»
  - [WL TG 2026 S. 50–51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0237.md) `tg-wl-2026__c0237` – «Machen Sie dabei Angaben über Belegenheitsort (Gemeinde, Kanton bzw.»

<a id="form-7-mietwert-selbstgenutzt-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 7 Mietwert selbstgenutzt – Mietwert selbstgenutzt (indexierter Eigenmietwert)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftensteuerrechnung/Schätzung mit Mietwertindex 2026
- **Rein:** Liegenschaftensteuerrechnung 2027 (Jan. 2027) → indexierter Mietwert 2026 · Schätzungsentscheid → Mietwert aus Selbstnutzung und Schätzungsjahr · Mietwertindex je Schätzungsjahr (Homepage Steuerverwaltung TG)
- **Rechnen:** Mietwert gemäss per Ende Steuerperiode rechtskräftiger Schätzung × Mietwertindex der Steuerperiode für das Schätzungsjahr = indexierter Mietwert
- **Regel:** Mietwert gemäss rechtskräftiger Schätzung, jährlich indexiert; 2026-Wert in der Regel aus der Liegenschaftensteuerrechnung 2027 ersichtlich. Zweit-/Ferienwohnungen und unentgeltlich oder unterpreislich an Nahestehende überlassene Liegenschaften: Mietwert zu 100%.
- **Beachten:** Checkbox «Am Wohnsitz selbstgenutzt ja» nur bei Selbstnutzung am Wohnsitz; bei Zweit-/Ferienwohnung leer lassen
- **Beachten:** Zweit-/Ferienwohnung, unentgeltlich/unterpreislich an Nahestehende überlassen: Mietwert zu 100% steuerbar
- **Beachten:** Unterpreisliche Vermietung an Nahestehende = Eigengebrauch → kantonal voller Mietwert
- **Quellen:**
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0002.md) `tg-form-07-2026__c0002` – «Mietwert selbstgenutzt»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0221.md) `tg-wl-2026__c0221` – «Die Mietwerte aus Selbstnutzung werden jährlich indexiert.»
  - [WL TG 2026 S. 51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0239.md) `tg-wl-2026__c0239` – «oder unterpreislich an nahestehende Dritte überlassene Liegenschaften zu 100% steuerbar und»
  - [WL TG 2026 S. 50–51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0237.md) `tg-wl-2026__c0237` – «Checkbox bei selbstgenutzten Zweit- und Ferienwohnungen dagegen immer leer zu lassen ist»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0219.md) `tg-wl-2026__c0219` – «Die unterpreisliche Vermietung an eine nahestehende Person ist dem Eigengebrauch»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0219.md) `tg-wl-2026__c0219` – «kantonal der volle Mietwert zu versteuern ist»
  - [StV TG § 2](../../chunks/tg/2025/tg-stv/tg-stv__par-2.md) `tg-stv__par-2` – «Grundlage bildet der durch den Liegenschaftenschätzer ermittelte Mietwert, welcher jährlich zu indexieren ist.»

<a id="form-7-selbstnutzungsabzug-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 7 Selbstnutzungsabzug – Selbstnutzungsabzug (Staatssteuer / Bundessteuer) und steuerbarer Eigenmietwert

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Rechenzeile (Mietwert minus Abzug)
- **Rein:** Übertrag «Mietwert selbstgenutzt» (Form. 7) · Checkbox «Am Wohnsitz selbstgenutzt ja» (Voraussetzung)
- **Rechnen:** Abzug = Kanton 40% / Bund 20% × Mietwert selbstgenutzt; steuerbarer Eigenmietwert = Mietwert − Abzug (je Spalte Staat/Bund)
- **Regel:** Nur für am Wohnsitz selbstgenutzte eigene Liegenschaften: Abzug 40% Kanton / 20% Bund vom Mietwert. Kein Abzug bei Zweit-/Ferienwohnungen, landwirtschaftlich geschätzten Liegenschaften und an Nahestehende überlassenen Liegenschaften (100% steuerbar).
- **Beachten:** Nur am Wohnsitz selbstgenutzte eigene Liegenschaft bzw. STWE-Anteil (inkl. Sonderrechte wie Autoabstellplatz)
- **Beachten:** Kein Abzug: landwirtschaftlich geschätzt, Zweit-/Ferienwohnung, an Nahestehende überlassen → 100% steuerbar
- **Beachten:** Nettoerfolg deshalb für Staat und Bund getrennt ermitteln
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **40 % (Selbstnutzungsabzug: 40 % vom Mietwert fuer am Wohnsitz selbstgenutztes Wohneigentum (Bund: 20 %, tg-wl-2026__c0222). Kein Abzug bei Zweit-/Ferienwohnungen, landwirtschaftlichen Liegenschaften, an Nahestehende ueberlassenen Objekten.)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Bund:** Selbstnutzungsabzug Bund 20% (Kanton 40%).
- **Quellen:**
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0002.md) `tg-form-07-2026__c0002` – «Selbstnutzungsabzug»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0222.md) `tg-wl-2026__c0222` – «Für am Wohnsitz selbstgenutzte eigene Liegenschaften können Sie vom Mietwert aus Selbst-»
  - [WL TG 2026 S. 50–51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0237.md) `tg-wl-2026__c0237` – «Wird eine Liegenschaft bzw. ein Stockwerkeigentumsanteil (Wohnung und dazu gehörende»
  - [WL TG 2026 S. 51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0240.md) `tg-wl-2026__c0240` – «Den so errechneten Abzug tragen Sie in der Zeile „Selbstnutzungsabzug“ in den Spalten „Staatssteuer“ und „Bundes-»
  - [WL TG 2026 S. 51–52](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0242.md) `tg-wl-2026__c0242` – «Selbstnutzungsabzugs der Nettoerfolg jeweils einzeln für die Staats- und Gemeindesteuern und die»

<a id="form-7-miet-pachtzinsen-einkommen-liegenschaften-mietertrag"></a>
### Ziff. Form. 7 Miet-/Pachtzinsen – Miet- und Pachtzinsen sowie weitere Erträge → Bruttoertrag

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Mietzinsaufstellung/Mietverträge; Abrechnung Einspeisevergütung Photovoltaik
- **Rein:** Mietverträge/Mietzinsaufstellung 2026 → Miet- und Pachtzinseinnahmen · Abrechnung Energieversorger → Einspeisevergütung Photovoltaik · Baurechts-/Pachtvertrag → Baurechtszinsen, Naturalleistungen, Kies-/Sandausbeutung · Hauswartvereinbarung → gewährte Mietzinsreduktion
- **Rechnen:** Bruttoertrag = steuerbarer Eigenmietwert + Σ Miet-/Pachtzinsen + weitere Erträge (PV-Einspeisung, Baurecht, Kies/Sand, Hauswart-Mietzinsreduktion)
- **Regel:** Sämtliche Miet-/Pachtzinseinnahmen, Einspeisevergütung PV, Baurechtszinsen, Erträge aus Kiesausbeutung; auch die dem Hauswart als Arbeitsentgelt gewährte Mietzinsreduktion. Bruttoertrag = steuerbarer Eigenmietwert plus übrige Erträge.
- **Beachten:** Mieterzahlungen für Heizung, Warmwasser, Reinigung nicht steuerbar, soweit ≤ tatsächliche Aufwendungen
- **Beachten:** PV-Eigenbedarfsanlage: kein Ertrag, wenn Vergütung ≤ Kosten Strombezug im Abrechnungszeitraum
- **Beachten:** Übrige Nebenkostenvergütungen deklarieren; unterpreisliche Vermietung an Nahestehende: kantonal voller Mietwert
- **Quellen:**
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0002.md) `tg-form-07-2026__c0002` – «Miet- und Pachtzinsen»
  - [WL TG 2026 S. 51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0241.md) `tg-wl-2026__c0241` – «Die Summe der steuerbaren Eigenmietwerte und der Miet- und Pachtzinserträge sowie allfällig wei-»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0220.md) `tg-wl-2026__c0220` – «Zahlungen der mietenden Personen für Heizung, Warmwasser und Reinigung von Treppenhaus»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0220.md) `tg-wl-2026__c0220` – «Einspeisevergütungen für Photovoltaikanlagen sind steuerbar. Bei Eigenbedarfsanlagen wird auf»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0220.md) `tg-wl-2026__c0220` – «Alle übrigen Vergütungen für Nebenkosten sind zu deklarieren.»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0219.md) `tg-wl-2026__c0219` – «Betrag der den hauswartenden Personen als Arbeitsentgelt gewährten Mietzinsreduktion»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0219.md) `tg-wl-2026__c0219` – «kantonal der volle Mietwert zu versteuern ist»

<a id="form-7-unterhalts-betriebskosten-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 7 Unterhalts-/Betriebskosten – Unterhalts- und Betriebskosten: Pauschal / Effektiv (Übertrag aus Formular 8)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Handwerkerrechnungen, Versicherungs-/Abgabenrechnungen, Abrechnung Stockwerkeigentümergemeinschaft; Formular 8 (bei effektiv)
- **Rein:** Übertrag Total Form. 8 → effektive Kosten · Sachversicherungs-, Liegenschaftensteuer-, Feuerungskontrollrechnungen → Betriebskosten · Abrechnung Stockwerkeigentümergemeinschaft → Erneuerungsfonds-Einlagen, Hauswart · Baujahr (Form. 7) → Pauschalsatz
- **Rechnen:** Pauschal 10% (Gebäude ≤ 10 J.) / 20% (> 10 J.) × Mietertrag bzw. Mietwert (Zweitwohnung) bzw. steuerbarer Eigenmietwert; oder effektiv = Total Form. 8
- **Regel:** Wahlrecht pro Liegenschaft und Steuerperiode: Pauschale 10% (Gebäude bis 10 Jahre) oder 20% (älter) vom Mietertrag bzw. Eigenmietwert, oder effektive Kosten (Formular 8). Pauschale ausgeschlossen bei Geschäftsvermögen, vorwiegend geschäftlich genutzten Liegenschaften, unüberbauten Grundstücken und Baurecht. Checkbox pauschal/effektiv ankreuzen. Übertragbare Energiespar-/Rückbaukosten nur bei effektiven Kosten. Stockwerkeigentum: Hauswartskosten bei Selbstbewohnung in der Regel nur 50%.
- **Beachten:** Gebäudealter: Kanton am Ende, Bund zu Beginn der Steuerperiode (Art. 5 LKV)
- **Beachten:** Pauschale ausgeschlossen: Geschäftsvermögen, vorwiegend geschäftliche Drittnutzung, unüberbaut, Baurechtsbelastung
- **Beachten:** Übertragbare Energiespar-/Rückbaukosten nur effektiv; STWE-Hauswart selbstbewohnt i.d.R. 50%
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Pauschalabzug Liegenschaftsunterhalt: 10 % des Bruttomietertrags bzw. (Eigen-)Mietwerts fuer Gebaeude bis 10 Jahre alt (Ende Steuerperiode); wahlweise statt effektiver Kosten, je Liegenschaft und Periode.)** · Bund **10 % (Pauschalabzug Liegenschaftskosten (anstelle effektiver Kosten, Wahl pro Periode und Liegenschaft): 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist.)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt: 20 % fuer Gebaeude, die ueber 10 Jahre alt sind.)** · Bund **20 % (Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist.)**
- **Quellen:**
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0002.md) `tg-form-07-2026__c0002` – «Unterhalts-/Betriebskosten»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0235.md) `tg-wl-2026__c0235` – «10% für Gebäude, die am Ende der Steuerperiode bis zu zehn Jahre alt sind;»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0235.md) `tg-wl-2026__c0235` – «20% für Gebäude, die am Ende der Steuerperiode älter als zehn Jahre sind.»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist»
  - [WL TG 2026 S. 48](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0225.md) `tg-wl-2026__c0225` – «Bei selbstbewohntem Stockwerkeigentum werden Hauswartskosten in der Regel nur zu 50% als abzugsfähiger Unterhalt anerkannt»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0233.md) `tg-wl-2026__c0233` – «Die Kumulation mit dem Pauschalabzug für Liegenschaftsunterhaltskosten ist nicht möglich»
  - [WL TG 2026 S. 48](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0224.md) `tg-wl-2026__c0224` – «die mit dem Grundbesitz verbundenen jährlichen Abgaben wie Liegenschaftensteuer»
  - [WL TG 2026 S. 48](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0224.md) `tg-wl-2026__c0224` – «Sachversicherungsprämien für die Liegenschaft (Brand-, Glas- und Wasserschäden etc.;»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0235.md) `tg-wl-2026__c0235` – «Die Pauschale wird prozentual vom Mietertrag (bei vermieteten Objekten), vom Mietwert aus»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0235.md) `tg-wl-2026__c0235` – «bei unüberbauten Grundstücken und bei solchen mit Baurechtsbelastung»
  - [WL TG 2026 S. 49](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0230.md) `tg-wl-2026__c0230` – «Pro Liegenschaft, für welche Sie effektive Unterhaltskosten geltend machen, füllen Sie bitte je ein»

<a id="form-7-nettoerfolg-totale-berechnung-total"></a>
### Ziff. Form. 7 Nettoerfolg / Totale – Nettoerfolg je Liegenschaft; Total Nettoerfolge Staat/Bund (Code 180 → Form. 1 Ziff. 8)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Bruttoertrag minus Unterhalts-/Betriebskosten)
- **Rein:** Übertrag Bruttoertrag und Unterhalts-/Betriebskosten je Liegenschaft (Form. 7) · Übertrag Nettoerfolge von Rückseite/Beiblättern
- **Rechnen:** Nettoerfolg = Bruttoertrag − Unterhalts-/Betriebskosten je Liegenschaft; Σ → Code 180 → Form. 1 Ziff. 8 S. 2 (Spalte Staat / Bund)
- **Regel:** Bei selbstgenutzten Liegenschaften Nettoerfolg je Staat und Bund einzeln ermitteln (unterschiedlicher Selbstnutzungsabzug), sonst Staat berechnen und für Bund übernehmen.
- **Beachten:** Am Wohnsitz selbstgenutzt: Staat und Bund getrennt rechnen (Abzug Kanton 40% / Bund 20%); übrige: Staat = Bund
- **Beachten:** Pauschale bei Gebäudealter um 10 Jahre: Kanton Alter Ende / Bund Beginn Steuerperiode → Spalten prüfen
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **40 % (Selbstnutzungsabzug: 40 % vom Mietwert fuer am Wohnsitz selbstgenutztes Wohneigentum (Bund: 20 %, tg-wl-2026__c0222). Kein Abzug bei Zweit-/Ferienwohnungen, landwirtschaftlichen Liegenschaften, an Nahestehende ueberlassenen Objekten.)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Quellen:**
  - [Formular 7 TG 2026 S. 1](../../chunks/tg/2026/tg-form-07-2026/tg-form-07-2026__c0003.md) `tg-form-07-2026__c0003` – «Total Nettoerfolge 180»
  - [WL TG 2026 S. 51–52](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0242.md) `tg-wl-2026__c0242` – «Bei am Wohnsitz selbst genutzten Liegenschaften ist aufgrund der unterschiedlichen Höhe des»
  - [WL TG 2026 S. 47](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0222.md) `tg-wl-2026__c0222` – «kantonal einen Abzug von 40% und beim Bund von 20% vornehmen»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0235.md) `tg-wl-2026__c0235` – «10% für Gebäude, die am Ende der Steuerperiode bis zu zehn Jahre alt sind;»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist»

## Hilfsblatt Liegenschaftsunterhalt (Form. 8)

<a id="form-8-rechnungsliste-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 8 Rechnungsliste – Einzelaufstellung Rechnungen: Datum, Rechnungssteller, Beschreibung, Zahlungsbetrag, davon Anlagekosten/Mehrwert, davon Unterhalts- und Betriebskosten

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Handwerkerrechnungen und Zahlungsnachweise (ab Fr. 1'000 pro Einzelbetrag Kopie beilegen)
- **Rein:** Handwerkerrechnungen + Zahlungsbelege → Datum, Rechnungssteller, Arbeit, bezahlter Nettobetrag · Abrechnung Stockwerkeigentümergemeinschaft (Kopie beilegen) · Prämien-/Abgaberechnungen (Sachversicherung Liegenschaft, Liegenschaftensteuer)
- **Rechnen:** Je Rechnung: Zahlungsbetrag = Anteil Anlagekosten/Mehrwert + Anteil Unterhalts-/Betriebskosten; nur letzterer abziehbar
- **Regel:** Ein Formular pro Liegenschaft; Kosten einzeln mit Rechnungsstellerin, Art der Arbeit und tatsächlich bezahltem Nettobetrag. Nicht abzugsfähige Anteile (Anlagekosten/Investitionen/Mehrwert, Lebenshaltungskosten) in die Spalte «Anlagekosten» ausscheiden; nur abzugsfähiger Anteil in «Unterhalts- und Betriebskosten». Zeitliche Abgrenzung nach Rechnungs- oder Zahlungsdatum der Steuerperiode 2026. Abgrenzung nach Merkblatt Liegenschaftenunterhalt/StP 34 Nr. 1–5.
- **Beachten:** Ein Formular pro Liegenschaft; Rechnungskopien für Einzelbeträge ab Fr. 1'000 beilegen
- **Beachten:** Zeitliche Abgrenzung: Rechnungs- oder Zahlungsdatum 2026; gewählte Methode beibehalten
- **Beachten:** Nicht abziehbar: Neu-/Um-/Anbau, wertvermehrend, Ersatzbau, konstruktive Mängel, Fahrnis (StP 34 Nr. 1, 5)
- **Quellen:**
  - [WL TG 2026 S. 49](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0230.md) `tg-wl-2026__c0230` – «Pro Liegenschaft, für welche Sie effektive Unterhaltskosten geltend machen, füllen Sie bitte je ein»
  - [WL TG 2026 S. 47–48](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0223.md) `tg-wl-2026__c0223` – «Von den Einkünften aus Liegenschaften können Sie die in der Steuerperiode 2026 angefallenen»
  - [WL TG 2026 S. 49](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0231.md) `tg-wl-2026__c0231` – «Für Einzelbeträge ab Fr. 1'000 legen Sie der Steuererklärung bitte die Rechnungskopien»
  - [WL TG 2026 S. 49](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0231.md) `tg-wl-2026__c0231` – «Daher ist der Zeitpunkt der Rechnungsstellung oder allenfalls der Bezahlung massgeblich. An der einmal getroffenen Wahl ist festzuhalten.»
  - [WL TG 2026 S. 49](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0229.md) `tg-wl-2026__c0229` – «Wertvermehrende Investitionen (StP 34 Nr. 1)»
  - [WL TG 2026 S. 49](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0229.md) `tg-wl-2026__c0229` – «Behebung konstruktiver Mängel (StP 34 Nr. 5)»
  - [WL TG 2026 S. 48](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0224.md) `tg-wl-2026__c0224` – «Sachversicherungsprämien für die Liegenschaft (Brand-, Glas- und Wasserschäden etc.;»
  - [WL TG 2026 S. 48](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0224.md) `tg-wl-2026__c0224` – «die mit dem Grundbesitz verbundenen jährlichen Abgaben wie Liegenschaftensteuer»

<a id="form-8-f-rderbeitr-ge-bertragbare-kosten-abzug-liegenschaft-energie-umwelt"></a>
### Ziff. Form. 8 Förderbeiträge / übertragbare Kosten – Förderbeiträge Energiespar-/Umweltschutzmassnahmen (Abzug) und aus Vorjahren übertragbare Kosten (Energiesparen, Umweltschutz, Rückbau)

- **Schlüssel:** `abzug.liegenschaft.energie_umwelt` (Investitionen Energiesparen/Umweltschutz, Rückbaukosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Förderbescheide (Bund, Kanton, Gemeinde); Aufstellung übertragbarer Kosten aus 2024/2025
- **Rein:** Förderzusage/Auszahlungsbestätigung (Bund, Kanton, Gemeinde, Stiftung Klimarappen) → Förderbeitrag · Berechnung übertragbare Kosten (Hilfsblatt StV TG, StP 34 Nr. 2) → Übertrag aus 2024/2025 · Veranlagung 2025 (Ziff. 24 Reineinkommen), sonst SE 2025 provisorisch
- **Rechnen:** Energiespar-/Umweltschutzkosten − Förderbeiträge; + Übertrag = Kosten 2024/2025 (inkl. Rückbau), mit Reineinkommen 2025 (Ziff. 24) nicht verrechnet
- **Regel:** Förderbeiträge mindern die abzugsfähigen Kosten. Ergibt sich durch Energiespar-/Umweltschutz- oder Rückbaukosten (Ersatzneubau) ein negatives Reineinkommen, sind die nicht verrechneten Kosten auf die beiden Folgeperioden übertragbar (Kosten 2026 bis längstens Steuerperiode 2028); nur im Rahmen effektiver Unterhaltskosten (keine Kumulation mit Pauschale).
- **Beachten:** Übertrag nur bei negativem Reineinkommen; Kosten 2026 längstens bis Steuerperiode 2028
- **Beachten:** Nur mit effektiven Kosten, keine Kumulation mit Pauschale; Berechnung der SE beilegen
- **Beachten:** Sozialabzüge nicht einbeziehen; zuerst nicht übertragbare Abzüge, dann übertragbare nach Ablauf
- **Quellen:**
  - [Formular 8 TG 2026 S. 1](../../chunks/tg/2026/tg-form-08-2026/tg-form-08-2026__c0003.md) `tg-form-08-2026__c0003` – «Förderbeiträge für Energiespar- und Umweltschutzmassnahmen (Bund, Kanton, Gemeinde etc.)»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0233.md) `tg-wl-2026__c0233` – «Die übertragbaren Kosten können nur im Rahmen der effektiven Liegenschaftsunterhaltskosten gel-»
  - [WL TG 2026 S. 49](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0228.md) `tg-wl-2026__c0228` – «vermindern die selbst getragenen Kosten»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0234.md) `tg-wl-2026__c0234` – «In der Steuerperiode 2026 können Sie die in den Jahren 2024 und 2025 angefallenen»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0234.md) `tg-wl-2026__c0234` – «Massgebend für die Berechnung der übertragbaren Kosten ist das veranlagte Reineinkommen 2025»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0234.md) `tg-wl-2026__c0234` – «Bitte reichen Sie Ihre Berechnung zusammen mit der Steuererklärung ein.»
  - [WL TG 2026 S. 49–50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0232.md) `tg-wl-2026__c0232` – «Die Sozialabzüge (z.B. Kinderabzug) werden bei der Berechnung nicht mit einbezogen»

<a id="form-8-total-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 8 Total – Total Unterhalts- und Betriebskosten (Übertrag auf Formular 7)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Spalte «Unterhalts- und Betriebskosten» (Vorder-/Rückseite, Hilfsblätter) · Übertrag Förderbeiträge und übertragbare Kosten Vorjahre (Form. 8)
- **Rechnen:** Total = Σ Unterhalts-/Betriebskosten (inkl. Rückseite/Hilfsblätter) − Förderbeiträge + übertragbare Vorjahreskosten → Form. 7 «Effektiv»
- **Regel:** Total abzugsfähiger Unterhalts- und Betriebskosten (nach Abzug Förderbeiträge, inkl. übertragbarer Kosten) → Formular 7 «effektiv».
- **Beachten:** Anlagekosten separat als «Total nicht abzugsfähige Kosten» ausweisen, nicht übertragen
- **Beachten:** In Form. 7 Checkbox «Effektiv» ankreuzen
- **Beachten:** Formular druckt bei Zeile übertragbare Kosten «–»; gemäss WL abziehbar (+) → Original-PDF S. 1 prüfen
- **Quellen:**
  - [Formular 8 TG 2026 S. 1](../../chunks/tg/2026/tg-form-08-2026/tg-form-08-2026__c0003.md) `tg-form-08-2026__c0003` – «Total Unterhalts- und Betriebskosten (Übertrag auf Formular 7)»
  - [WL TG 2026 S. 49–50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0232.md) `tg-wl-2026__c0232` – «Resultiert aufgrund der Geltendmachung von Investitionskosten für Energiespar- und»
  - [WL TG 2026 S. 51](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0241.md) `tg-wl-2026__c0241` – «Kreuzen Sie in der Checkbox an, ob Sie pauschale oder effektive Unterhalts- und Betriebskosten»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0233.md) `tg-wl-2026__c0233` – «Die übertragbaren Kosten können nur im Rahmen der effektiven Liegenschaftsunterhaltskosten»
  - [WL TG 2026 S. 50](../../chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0234.md) `tg-wl-2026__c0234` – «in der dafür vorgesehenen Zeile in Formular 8 ein. Bitte reichen Sie Ihre Berechnung»
  - [Formular 8 TG 2026 S. 1](../../chunks/tg/2026/tg-form-08-2026/tg-form-08-2026__c0003.md) `tg-form-08-2026__c0003` – «für Energiesparen und Umweltschutz sowie Rückbaukosten gemäss Aufstellung –»
