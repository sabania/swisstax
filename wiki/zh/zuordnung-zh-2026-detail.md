---
typ: zuordnung-detail
titel: Zuordnung ZH 2026 – Detail
jur: zh
jahre:
- 2026
generiert: tools/build_quick.py aus data/zuordnung/zh/2026.yaml (2026-11-09)
---

# ZH 2026: Zuordnung Beleg → Ziffer – Detail

> Kompaktansicht: [quick/zuordnung-zh-2026.md](../../quick/zuordnung-zh-2026.md) · Formular: Steuererklärung 2026 Kanton Zürich, Hauptformular Form. 300 – gemäss Formular/Wegleitung 2026 für unterjährige Steuerpflicht (zh-form-300-2026-uj, zh-wl-2026-uj; reguläres Formular 2026 noch nicht publiziert, Ziffern/Codes gelten voraussichtlich unverändert, am regulären Formular prüfen). Hilfsblätter: Berufsauslagen (Form. 360), Versicherungsprämien (Form. 365), Berufsorientierte Aus- und Weiterbildungskosten (Form. 367) mit Aufstellung behinderungsbedingte Kosten, Aufstellung Krankheits- und Unfallkosten (Form. 370), Wertschriften- und Guthabenverzeichnis (Form. 340), Liegenschaftenverzeichnis (Form. 350), Schuldenverzeichnis (Form. 355). Neu 2026: Ziff. 14.3 Einkauf Säule 3a. · Quelle der Wahrheit: `data/zuordnung/zh/2026.yaml`

> **Hinweis:** Reguläres Formular/Wegleitung ZH 2026 noch nicht publiziert (Stand 09.11.2026) – Zuordnung stützt sich auf die Fassung für unterjährige Steuerpflicht (UJ); Ziffern/Codes am regulären Formular prüfen.

## Weitere Angaben

<a id="s-1-personalien-personalien"></a>
### Ziff. S. 1 Personalien – Personalien per 31.12.2026 bzw. per Ende der Steuerpflicht (Zivilstand, Konfession, Beruf, Pensionskassen-Frage; Dauer der Steuerpflicht)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Mandantenstammdaten; Vorjahresveranlagung
- **Rein:** Stammdaten/Ausweise → Zivilstand, Konfession, Beruf per 31.12.2026 bzw. Ende der Steuerpflicht · Lohnausweis → Ziff. 10.1 Ordentliche Beiträge 2. Säule → Frage «Ordentliche Beiträge an die Pensionskasse?» ja/nein · Abmelde-/Todesnachweis → Datum Wegzug ins Ausland bzw. Todestag (Ende der Steuerpflicht)
- **Rechnen:** PK ja → Ziff. 15 max. Kanton 5'800/2'900, Bund 3'700/1'800; weder 2. Säule noch 3a → Kanton 8'700/4'350, Bund 5'550/2'700 (verh./übrige)
- **Regel:** Stichtag der Verhältnisse ist der 31.12.2026 bzw. das Ende der Steuerpflicht. Die Frage «Ordentliche Beiträge an die Pensionskasse (2. Säule)?» steuert den höheren Versicherungsabzug (Ziff. 15, Teil B). Bei unterjähriger Steuerpflicht ist die Dauer der Steuerpflicht einzutragen.
- **Beachten:** Eingetragene Partnerschaft = Ehe; Person 1 = Partner/in mit alphabetisch erstem Nachnamen
- **Beachten:** Tod eines Ehegatten: bis und mit Todestag gemeinsame Steuererklärung, danach Überlebender separat
- **Beachten:** Unterjährig: regelmässige Einkünfte werden für den Satz auf zwölf Monate umgerechnet (durch das Steueramt)
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'800 (Versicherungsprämien und Sparzinsen (Staatssteuer), in ungetrennter Ehe lebende Steuerpflichtige mit Beiträgen an 2. Säule/Säule 3a: Fr. 5'800.)** · Bund **CHF 3'700 (Versicherungsprämien und Zinsen von Sparkapitalien, Ehepaare in ungetrennter Ehe, mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 3'700.)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'900 (Versicherungsprämien und Sparzinsen (Staatssteuer), übrige Steuerpflichtige (nicht in ungetrennter Ehe) mit Vorsorgebeiträgen: Fr. 2'900.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 1'800.)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 8'700 (Gemeinsam Besteuerte ohne Beiträge an 2. Säule und Säule 3a (weder durch Steuerpflichtige noch Arbeitgeber): Abzug erhöht sich um die Hälfte, höchstens Fr. 8'700.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an 2. Säule und Säule 3a: Höchstabzug CHF 5'550 (Erhöhung um die Hälfte).)**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 4'350 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: Abzug erhöht sich um die Hälfte, höchstens Fr. 4'350.)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: max. CHF 2'700.)**
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0002.md) `zh-form-300-2026-uj__c0002` – «Personalien per 31.12.2026 bzw. per Ende der Steuerpflicht»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0031.md) `zh-wl-2026-uj__c0031` – «2. Säule 10.1 Ordentliche Beiträge»
  - [WL ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0001.md) `zh-wl-2026-uj__c0001` – «derjenigen Person, deren Nachname alphabetisch an erster Stelle kommt»
  - [WL ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0002.md) `zh-wl-2026-uj__c0002` – «Bis und mit dem Todestag sind die Ehegatten gemeinsam einzuschätzen.»
  - [WL ZH 2026 UJ S. 6](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0011.md) `zh-wl-2026-uj__c0011` – «Für das satzbestimmende Einkommen werden die regelmässig fliessenden Einkünfte auf zwölf Monate umgerechnet.»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0080.md) `zh-wl-2026-uj__c0080` – «oder: sofern weder Beiträge an die 2. noch an die 3. Säule a geleistet wurden»
  - [WL ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0002.md) `zh-wl-2026-uj__c0002` – «für den Zeitraum ab Beginn der Steuerperiode 2026 bis zum Wegzug.»

<a id="s-1-kinder-personalien"></a>
### Ziff. S. 1 Kinder – Kinder im und ausserhalb des Haushalts (Jahrgänge 2009–2026 oder in beruflicher Erstausbildung)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Geburtsdatum, Ausbildung (Schule/Lehrfirma), Ausbildungsende, ob der andere Elternteil Unterhaltsbeiträge leistet
- **Rein:** Familienausweis/Geburtsurkunde → Vorname, Name, Geburtsdatum (Jg. 2009–2026 oder in Erstausbildung) · Lehrvertrag/Schulbestätigung → Schule/Lehrfirma, voraussichtliches Ausbildungsende · Scheidungsurteil/Unterhaltsvertrag → Sorgerecht; Unterhaltsbeiträge des anderen Elternteils ja/nein
- **Rechnen:** je Kind Ziff. 24.1: Kanton 9'400 / Bund 6'800 (Code 370 im, 372 ausserhalb Haushalt); halb 4'700 / 3'400; Zuschlag Ziff. 15: 1'300 / 700 (halb 650 / 350)
- **Regel:** Grundlage für Kinderabzug (Ziff. 24.1), Versicherungszuschlag (Ziff. 15 Teil B), Kinderdrittbetreuung (Ziff. 16.6). Angabe «Leistet der andere Elternteil Unterhaltsbeiträge?» ist bei ledigen, geschiedenen oder getrennt lebenden Eltern auszufüllen und entscheidet über ganzen oder halben Kinderabzug.
- **Beachten:** Stand 31. Dezember 2026: minderjährig oder volljährig in beruflicher Erstausbildung, Unterhalt zur Hauptsache bestritten
- **Beachten:** Gemeinsame Sorge: Alimente erhalten → ganz, keine → halb; Alimentenzahler: kein Kinderabzug, dafür Alimentenabzug
- **Beachten:** Fremdbetreuung Ziff. 16.6 nur Jg. 2012–2026, max. Kanton 25'300 / Bund 25'800 je Kind
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 9'400 (Kinderabzug je Kind (minderjährig unter elterlicher Sorge/Obhut oder volljährig in beruflicher Erstausbildung, Unterhalt zur Hauptsache): Fr. 9'400. Bei nicht gemeinsam besteuerten Eltern hälftig aufgeteilt (Fr. 4'700), wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge für das Kind abgezogen werden.)** · Bund **CHF 6'800 (Kinderabzug CHF 6'800 pro minderjähriges oder in beruflicher/schulischer Ausbildung stehendes Kind, für dessen Unterhalt die steuerpflichtige Person sorgt; bei getrennter Besteuerung der Eltern hälftig bei gemeinsamer elterlicher Sorge ohne Unterhaltsbeiträge.)**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 9'400 (Volljährige Kinder in beruflicher Erstausbildung, deren Unterhalt zur Hauptsache bestritten wird: gleicher Kinderabzug Fr. 9'400.)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Abzug CHF 6'800 (kein höherer Ausbildungsabzug beim Bund).)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'300 (Zuschlag zum Versicherungsabzug: Fr. 1'300 für jedes Kind oder jede unterstützungsbedürftige Person mit Kinder-/Unterstützungsabzug nach § 34 Abs. 1; bei hälftig aufgeteiltem Kinderabzug Fr. 650.)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 25'300 (Kinderdrittbetreuungskosten: nachgewiesene Kosten, höchstens Fr. 25'300 pro Kind (Staatssteuer); bei Konkubinat/alternierender Obhut mit gemeinsamer Sorge je halber Abzug (Fr. 12'650).)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind, höchstens CHF 25'800; Kind unter 14 Jahren im gleichen Haushalt; Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)**
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0003.md) `zh-form-300-2026-uj__c0003` – «Kinder der Jahrgänge 2009–2026 oder in beruflicher Erstausbildung stehende Kinder»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0125.md) `zh-wl-2026-uj__c0125` – «Abzug für Kinder in Ihrem Haushalt (gemäss Seite 1)»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0125.md) `zh-wl-2026-uj__c0125` – «das am 31. Dezember 2026 minderjährig ist»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0126.md) `zh-wl-2026-uj__c0126` – «pro Kind (CHF 4’700) pro Kind (CHF 3’400)»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0127.md) `zh-wl-2026-uj__c0127` – «Sie können jedoch die für das Kind geleisteten Unterhaltsbeiträge abziehen.»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0123.md) `zh-wl-2026-uj__c0123` – «Abzug für fremdbetreute Kinder (Jahrg. 2012–2026)»
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0087.md) `zh-wl-2026-uj__c0087` – «CHF 700 für jedes Kind oder jede unterstützungsbedürftige Person»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0126.md) `zh-wl-2026-uj__c0126` – «können Sie den ganzen Kinderabzug geltend»

<a id="s-1-unterst-tzte-personen-personalien"></a>
### Ziff. S. 1 Unterstützte Personen – Erwerbsunfähige oder beschränkt erwerbsfähige unterstützte Personen (im und ausserhalb des Haushalts)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Name, Geburtsjahr, Adresse, Unterstützungsbetrag pro Jahr; Bestätigung der unterstützten Person
- **Rein:** Bestätigung der unterstützten Person → Art, Zeitpunkt und Höhe der Unterstützung · Zahlungsbelege (Ausland: Post-/Bankbelege) → Unterstützungsbetrag pro Jahr (auf Verlangen)
- **Rechnen:** Unterstützung/Jahr ≥ Kanton 2'800 / Bund 6'800 → Abzug je Person Ziff. 24.2 (Code 374): Kanton 2'800 / Bund 6'800; Zuschlag Versicherungsabzug 1'300 / 700
- **Regel:** Voraussetzung Unterstützung von mindestens CHF 2'800 (Staatssteuer) bzw. CHF 6'800 (Bundessteuer) pro Jahr. Abzug erfolgt in Ziff. 24.2.
- **Beachten:** Nur für Personen, die wegen Gebrechen oder anderer objektiver Gründe erwerbsunfähig bzw. beschränkt erwerbsfähig sind
- **Beachten:** Kein Abzug für Ehegatten, Kinder mit Kinderabzug oder Personen, für die Alimente abgezogen werden
- **Beachten:** Bestätigung der unterstützten Person zwingend mit der Steuererklärung einreichen
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'800 (Unterstützungsabzug für erwerbsunfähige oder beschränkt erwerbsfähige Personen, an deren Unterhalt mindestens in Höhe des Abzugs beigetragen wird: Fr. 2'800 je Person. Nicht für Ehegatten und Kinder mit Kinderabzug oder Unterhaltsbeitragsabzug.)** · Bund **CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'300 (Zuschlag zum Versicherungsabzug: Fr. 1'300 für jedes Kind oder jede unterstützungsbedürftige Person mit Kinder-/Unterstützungsabzug nach § 34 Abs. 1; bei hälftig aufgeteiltem Kinderabzug Fr. 650.)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**
- **Bund:** Mindestunterstützung CHF 6'800 (Abzug 6'800) statt CHF 2'800.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0003.md) `zh-form-300-2026-uj__c0003` – «Erwerbsunfähige oder beschränkt erwerbsfähige Personen»
  - [WL ZH 2026 UJ S. 20](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0134.md) `zh-wl-2026-uj__c0134` – «des Unterstützungsabzuges von CHF 2’800»
  - [WL ZH 2026 UJ S. 20](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0133.md) `zh-wl-2026-uj__c0133` – «infolge körperlicher oder geistiger Gebrechen oder aus anderen objektiven Gründen erwerbsunfähig oder nur beschränkt erwerbsfähig sind»
  - [WL ZH 2026 UJ S. 20](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0133.md) `zh-wl-2026-uj__c0133` – «eine Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der erfolgten Unterstützungen einzureichen»
  - [WL ZH 2026 UJ S. 20](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0133.md) `zh-wl-2026-uj__c0133` – «wenn für die gleiche Person Unterhaltsbeiträge (Alimente) in Abzug gebracht werden»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0125.md) `zh-wl-2026-uj__c0125` – «24.2 Abzug für unterstützte Personen»
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0087.md) `zh-wl-2026-uj__c0087` – «CHF 1’300 für jedes Kind oder jede u nterstützungsbedürftige Person»

<a id="40-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. 40 – Kapitalleistungen aus AHV/IV, 2. Säule, Freizügigkeitskonto/-police, Säule 3a, Kapitalzahlungen bei Tod oder bleibenden Nachteilen (Code 510)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung (Form. 563) mit Auszahlungsdatum und Betrag
- **Rein:** Auszahlungsbescheinigung Pensionskasse/Freizügigkeitsstiftung/3a-Einrichtung → Betrag und Auszahlungsdatum · AHV/IV-Verfügung → Kapitalleistung · Bescheinigung Kapitalzahlung bei Tod/bleibenden Nachteilen → Betrag
- **Rechnen:** Σ Kapitalleistungen 2026 (zu 100%) = Code 510; Kanton: Satz für ein Zwanzigstel, einfache Staatssteuer mind. 2% / Bund: ein Fünftel Tarif Art. 36 Abs. 1 und 2 DBG
- **Regel:** Sämtliche im Jahr 2026 ausbezahlten Kapitalleistungen mit Auszahlungsdatum angeben; mehrere Leistungen: Aufstellung und Gesamtbetrag. Zu 100% steuerbar, gesondert vom übrigen Einkommen besteuert: Staatssteuer zum Satz einer jährlichen Leistung von einem Zwanzigstel, einfache Staatssteuer mind. 2%. Steuerfrei: bei Stellenwechsel ausbezahlte 2.-Säule-Kapitalleistungen, soweit innert Jahresfrist in eine andere Vorsorgeeinrichtung eingekauft.
- **Beachten:** Mehrere Leistungen: Aufstellung beilegen, Gesamtbetrag eintragen
- **Beachten:** Steuerfrei: 2.-Säule-Leistung bei Stellenwechsel, soweit innert Jahresfrist in neue Vorsorgeeinrichtung eingekauft
- **Beachten:** Gesondert, volle Jahressteuer, keine Sozialabzüge; Kapitalabfindungen für wiederkehrende Leistungen → Ziff. 5.5
- **Limiten:**
  - Kapitalleistungen aus Vorsorge – Steuersatz/Tarif (separate Jahressteuer): Kanton **Kapitalleistungen aus Vorsorge (§ 22) gesondert zum Satz, der sich bei einer jährlichen Leistung von einem Zwanzigstel der Kapitalleistung ergäbe (Rentensatz 1/20); einfache Staatssteuer mindestens 2 % (Mindestsatz); stets volle Jahressteuer; keine Sozialabzüge nach § 34.** · Bund **Kapitalleistungen aus Vorsorge (Art. 22 DBG) und Zahlungen bei Tod/bleibenden Nachteilen werden gesondert besteuert (volle Jahressteuer, Steuerjahr des Zuflusses); Steuer = ein Fünftel der Tarife nach Art. 36 Abs. 1, 2 und 2bis erster Satz DBG (Bruchteil 1/5); keine Sozialabzüge.**
- **Bund:** Steuer zu einem Fünftel der Tarife nach Art. 36 Abs. 1 und 2 DBG.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0013.md) `zh-form-300-2026-uj__c0013` – «40. Kapital- aus AHV / IV aus Einrichtung der beruflichen Vorsorge (2. Säule)»
  - [WL ZH 2026 UJ S. 22](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0144.md) `zh-wl-2026-uj__c0144` – «• Kapitalleistungen aus Vorsorge sind zu 100% steuerbar.»
  - [WL ZH 2026 UJ S. 22](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0145.md) `zh-wl-2026-uj__c0145` – «ausgerichtet würde; die einfache Staatssteuer beträgt jedoch mindestens 2%.»
  - [WL ZH 2026 UJ S. 22](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0145.md) `zh-wl-2026-uj__c0145` – «Die Steuer wird zu einem Fünftel der Tarife nach Artikel 36 Abs. 1 und 2 DBG berechnet.»
  - [WL ZH 2026 UJ S. 22](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0143.md) `zh-wl-2026-uj__c0143` – «der Steuererklärung ist der Gesamtbetrag aller Kapitalleistungen anzugeben.»
  - [WL ZH 2026 UJ S. 22](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0144.md) `zh-wl-2026-uj__c0144` – «Vorsorge (2. Säule) und gleichartige Kapitalzahlungen des Arbeitgebers, soweit sie innert»
  - [DBG Art. 38](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-38.md) `bund-dbg-2026__art-38` – «Die Sozialabzüge werden nicht gewährt.»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «5.5 Kapitalabfindungen für wiederkehrende Leistungen»
  - [StG ZH § 37](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-37.md) `zh-stg-2026__par-37` – «Die Sozialabzüge gemäss § 34 werden nicht gewährt.»
  - [WL ZH 2026 UJ S. 22](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0145.md) `zh-wl-2026-uj__c0145` – «Es wird stets eine volle Jahressteuer erhoben.»

<a id="50-1-50-2-info-schenkungen-erbschaften"></a>
### Ziff. 50.1 / 50.2 – Schenkungen, Erbvorbezüge, Erbschaften, Beteiligung an Erbengemeinschaften: erhalten (Code 516) / ausgerichtet (Code 519)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Schenkungsvertrag, Erbteilungsvertrag/Erbbescheinigung (Datum, Name, Adresse, Verwandtschaftsgrad, Wert)
- **Rein:** Schenkungs-/Erbvorbezugsvertrag → Datum, Gegenpartei (Name, Adresse, Verwandtschaftsgrad), Wert · Erbbescheinigung/Erbteilungsvertrag → Todestag, Erbquote, Wert des Anteils · Aufstellung unverteilte Erbschaft → Erben/Quoten, Vermögenswerte, Erträge, Schulden
- **Rechnen:** je Zuwendung Datum + Wert: erhalten → Code 516, ausgerichtet → Code 519; Erträge ab Anfall und Vermögen (anteilmässig) bei Einkünften/Vermögen deklarieren
- **Regel:** Alle 2026 erhaltenen bzw. ausgerichteten Schenkungen, Erbvorbezüge und Vermögensanfälle von Todes wegen angeben (auch bei noch nicht erfolgter Erbteilung). Besondere Schenkungssteuererklärung nur nötig, wenn nicht Ehegatte/Partner, Nachkommen oder Gelegenheitsgeschenke bis CHF 5'000 je Geschenk.
- **Beachten:** Erbanfall: Vermögenssteuer Erblasser bis Erbgang, Erbe ab Erbgang; Schenkung/Erbvorbezug: ganzes Jahr beim Empfänger
- **Beachten:** Schenkungssteuererklärung innert dreier Monate, ausser Ehegatte/Partner, Nachkommen, Gelegenheitsgeschenk ≤ CHF 5'000
- **Beachten:** Unverteilte Erbschaft: Einkünfte ab Folgetag Todestag anteilig; Wertschriften aus Erbschaft/Schenkung mit Code E/S
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0014.md) `zh-form-300-2026-uj__c0014` – «50.1 Am T T M M 2026 erhalten von Wert: 516»
  - [WL ZH 2026 UJ S. 23](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0148.md) `zh-wl-2026-uj__c0148` – «bei Gelegenheitsgeschenken, die den Wert von je CHF 5’000 nicht übersteigen.»
  - [WL ZH 2026 UJ S. 6](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0012.md) `zh-wl-2026-uj__c0012` – «ab Erbgang bis Ende der Steuerpflicht (Steuerpflicht des Erben/Vermächtnisnehmers).»
  - [WL ZH 2026 UJ S. 23](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0147.md) `zh-wl-2026-uj__c0147` – «Personen hat der Empfänger innert dreier Monate nach Vollzug der Schenkung»
  - [WL ZH 2026 UJ S. 23](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0149.md) `zh-wl-2026-uj__c0149` – «Zu deklarieren sind die Einkünfte, welche ab dem auf den Todestag folgenden Tag bis zum»
  - [WL ZH 2026 UJ S. 23](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0151.md) `zh-wl-2026-uj__c0151` – «Namen, Adressen und Erbquoten sämtlicher Erben»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0156.md) `zh-wl-2026-uj__c0156` – «mit E die Werte, die Sie 2026 aus Erbschaften übernommen haben»

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Unselbständige Erwerbstätigkeit – Haupterwerb, Person 1 / Person 2 (Code 100/101)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis (Form. 11) Ziff. 11 Nettolohn/Rente
- **Rein:** Lohnausweis → Ziff. 11 Nettolohn/Rente (je Arbeitgeber) · Lohnausweis → Ziff. 8 Bruttolohn, Ziff. 9 AHV/IV/EO/ALV/NBUV, Ziff. 10 Berufliche Vorsorge (Kontrolle) · Lohnausweis → Ziff. 12 Quellensteuerabzug (nur Quellensteuerpflichtige) · Bescheinigungen über Mitarbeiterbeteiligungen → beilegen
- **Rechnen:** Σ LA Ziff. 11 je Person (= Ziff. 8 − Ziff. 9 − Ziff. 10) → Person 1 Code 100 / Person 2 Code 101
- **Regel:** Nettolohn gemäss Lohnausweis Ziff. 11 einsetzen (= Bruttolohn Ziff. 8 abzüglich Ziff. 9 und 10); Lohnausweis beilegen. Was im Lohnausweis unter Ziff. 10.1/10.2 (ordentliche PK-Beiträge, PK-Einkauf) bereits abgezogen ist, NICHT nochmals bei Ziff. 16.1 abziehen. Vom Arbeitgeber erhaltene Weiterbildungsvergütungen (LA Ziff. 13.3) sind bei Ziff. 16.2 zu berücksichtigen. LA Feld F (unentgeltliche Beförderung) und Feld G (Kantine/Lunch-Checks) steuern Ziff. 11/Form. 360. LA Ziff. 15 liefert Schichttage und Zusatzangaben. Zeitliche Lücken in der Erwerbstätigkeit ausdrücklich bezeichnen. Je Arbeitgeber eine Zeile (Haupt-/Nebenerwerb abgrenzen). Quellensteuerpflichtige: Bruttolohn/Quellensteuerabzug LA Ziff. 12 beachten.
- **Beachten:** In LA Ziff. 10.1/10.2 bereits abgezogene PK-Beiträge/Einkäufe nicht nochmals in Ziff. 16.1 abziehen
- **Beachten:** Inkl. Gratifikationen, Trinkgelder, Naturalbezüge, Mitarbeiterbeteiligungen; Erwerbslücken ausdrücklich bezeichnen
- **Beachten:** Quellensteuerpflichtige (Wohnsitz CH) ab Bruttolohn CHF 120'000: nachträgliche ordentliche Veranlagung
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0004.md) `zh-form-300-2026-uj__c0004` – «1. Einkünfte aus unselbständiger Erwerbstätigkeit»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0028.md) `zh-wl-2026-uj__c0028` – «In der Steuererklärung ist der Nettolohn (d.h. der Lohn nach Abzug von AHV/IV/EO- und»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «dass vom Bruttolohn total (Ziffer 8) das Total der Abzüge (Ziffer 9 und 10) abgezogen wird.»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0031.md) `zh-wl-2026-uj__c0031` – «10.2 Beiträge für den Einkauf»
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0088.md) `zh-wl-2026-uj__c0088` – «soweit die unter Ziffern 1 und 2 der Steuererklärung deklarierten Einkünfte nicht bereits um diese Beiträge gekürzt worden sind»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0026.md) `zh-wl-2026-uj__c0026` – «geschenke, Gratifikationen, Trinkgelder, Tantiemen;»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0027.md) `zh-wl-2026-uj__c0027` – «Mitarbeiterbeteiligungen (wie Aktien, Optionen, Anwartschaften).»
  - [WL ZH 2026 UJ S. 31](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0216.md) `zh-wl-2026-uj__c0216` – «Bescheinigungen über Mitarbeiterbeteiligungen;»
  - [WL ZH 2026 UJ S. 5](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0007.md) `zh-wl-2026-uj__c0007` – «ein Bruttojahreseinkommen aus unselbstständiger Erwerbstätigkeit von mindestens CHF 120’000 erzielen»
  - [WL Lohnausweis 2026 S. 14](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0034.md) `bund-wl-lohnausweis-2026__c0034` – «Arbeitnehmeranteil für AHV/IV/EO/ALV/NBUV betragsmässig anzugeben»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Unselbständige Erwerbstätigkeit – Nebenerwerb, Person 1 / Person 2 (Code 102/103)

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nebenerwerb); Bescheinigung für VR-Honorare/Behördenentschädigungen
- **Rein:** Lohnausweis Nebenerwerb → Ziff. 11 Nettolohn · Bescheinigung über VR-Entschädigungen → erhaltene Entschädigungen · Bescheinigung AHV-Ausgleichskasse (Quellensteuer BG gegen Schwarzarbeit) → nur beilegen, nicht eintragen
- **Rechnen:** Σ Einkünfte Nebenerwerb je Person → Code 102 / 103; Berufsauslagen Ziff. 5: min(max(20 % × Nebenerwerbseinkünfte; 800); 2'400) (Kanton = Bund)
- **Regel:** Sämtliche Einkünfte aus unselbständigen Nebenerwerbstätigkeiten, auch Dienstleistungsentschädigungen, Amtsvergütungen, Verwaltungsrats-/Vorstandshonorare, Tantiemen, Lizenzen (Formularfussnote 1.2/2.2); in ZH keine eigene Zeile für VR-Honorare. Quellensteuerpflichtige Nebeneinkünfte nach BG gegen Schwarzarbeit nicht aufführen, aber Bescheinigung der AHV-Ausgleichskasse beilegen. Berufsauslagen: Form. 360 Ziff. 5 (Nebenerwerb) statt Ziff. 1–4.
- **Beachten:** Inkl. Dienstleistungsentschädigungen, Amtsvergütungen, VR-/Vorstandshonorare, Tantiemen, Lizenzen, Autorenrechte
- **Beachten:** Nach BG gegen Schwarzarbeit quellenbesteuerte Einkünfte nicht aufführen, AHV-Bescheinigung beilegen
- **Beachten:** Pauschale deckt auch Fahr-/Verpflegungskosten; höhere Kosten detailliert aufführen, Aufstellung beilegen
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Auslagen bei Nebenbeschäftigung in unselbstständiger Stellung (inkl. Fahrkosten, auswärtige Verpflegung): 20 % der Einkünfte aus der Nebenbeschäftigung.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Mindestbetrag der Nebenerwerbs-Pauschale: Fr. 800.)** · Bund **CHF 800 (Mindestbetrag Pauschale Nebenerwerb.)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Höchstbetrag der Nebenerwerbs-Pauschale: Fr. 2'400. Höhere effektive Kosten sind detailliert aufzuführen und nachzuweisen.)** · Bund **CHF 2'400 (Höchstbetrag Pauschale Nebenerwerb.)**
- **Quellen:**
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0029.md) `zh-wl-2026-uj__c0029` – «Hier sind sämtliche Einkünfte aus unselbständigen Nebenerwerbstätigkeiten aufzuführen.»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0030.md) `zh-wl-2026-uj__c0030` – «gegen die Schwarzarbeit bezahlt wurden. Der Steuererklärung ist jedoch die Bescheinigung»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0004.md) `zh-form-300-2026-uj__c0004` – «Verwaltungsrats- und Vorstands honorare, Tantiemen, Lizenzen,»
  - [WL ZH 2026 UJ S. 31](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0218.md) `zh-wl-2026-uj__c0218` – «Verwaltungsräte • Bescheinigung über erhaltene Entschädigungen.»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0067.md) `zh-wl-2026-uj__c0067` – «20% der Einkünfte aus allen Nebenbeschäftigungen, insgesamt mindestens jedoch CHF 800 und höchstens CHF 2’400.»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0067.md) `zh-wl-2026-uj__c0067` – «so sind diese Auslagen bei Nebenerwerb detailliert aufzuführen»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit – Haupterwerb, Person 1 / Person 2 (Code 120/121)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsblatt A (Landwirtschaft: Hilfsblatt B oder G): steuerbarer Reingewinn; unterzeichnete Jahresrechnung
- **Rein:** Unterzeichnete Jahresrechnung (Bilanz, Erfolgsrechnung, Anhang) → Reingewinn/-verlust · Vereinfachte Buchführung → Aufstellung Aktiven/Passiven, Einnahmen/Ausgaben, Privatentnahmen/-einlagen · Hilfsblatt A (Landwirtschaft: B oder G) → Code 1750 Einkünfte aus selbständiger Erwerbstätigkeit · Formular «Liquidationsgewinn» / Hilfsblatt «Qualifizierte Beteiligungen im Geschäftsvermögen» → beilegen, falls zutreffend
- **Rechnen:** Hilfsblatt A: Reingewinn (1810) + Korrekturen (1811–1815) = AHV-Einkommen (1740) + pers. AHV/IV/EO (1741) − 1742 − 1743 = 1750 → Code 120/121
- **Regel:** Ergebnis aus Hilfsblatt A (bzw. B/G) übertragen; unterzeichnete Jahresrechnung (Bilanz, Erfolgsrechnung, Anhang) bzw. bei vereinfachter Buchführung Aufstellungen über Aktiven/Passiven und Einnahmen/Ausgaben beilegen. Enthält auch Erträge aus qualifizierten Beteiligungen im Geschäftsvermögen und Liquidationsgewinne (Abzug siehe Ziff. 16.5). Eigenkapital in Ziff. 32.
- **Beachten:** Pers. AHV/IV/EO-Beiträge im Hilfsblatt aufrechnen (1741), Abzug in Ziff. 16.1
- **Beachten:** Liquidationsgewinne (Aufgabe nach 55. Altersjahr/Invalidität, letzte zwei Geschäftsjahre) gesondert → Abzug Ziff. 16.5
- **Beachten:** Geschäftsgrundstücke: Gewinn voll deklarieren; Staat: Grundstückgewinnteil in Ziff. 16.5 abziehen, Bund voll steuerbar
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0004.md) `zh-form-300-2026-uj__c0004` – «2. Einkünfte aus selbständiger Erwerbstätigkeit in Handel, Gewerbe,»
  - [WL ZH 2026 UJ S. 31](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0217.md) `zh-wl-2026-uj__c0217` – «Unterzeichnete Jahresrechnung (Bilanz, Erfolgsrechnung und Anhang) für Steuerpflichtige»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0035.md) `zh-wl-2026-uj__c0035` – «Reingewinn bzw. -verlust gemäss Erfolgsrechnung»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0036.md) `zh-wl-2026-uj__c0036` – «Subtotal = Einkünfte aus selbständiger Erwerbstätigkeit für AHV-Zwecke 1740»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0036.md) `zh-wl-2026-uj__c0036` – «Persönliche AHV/IV/EO-Beiträge (in Ziff. 16.1 der Steuererklärung abzuziehen)»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0037.md) `zh-wl-2026-uj__c0037` – «Einkünfte aus selbständiger Erwerbstätigkeit 1750»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0038.md) `zh-wl-2026-uj__c0038` – «Solche Liquidationsgewinne können unter Ziffer 16.5 wieder von den Einkünften abgezogen werden.»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0039.md) `zh-wl-2026-uj__c0039` – «Demgegenüber unterliegen bei der Bundessteuer Gewinne auf Grundstücken des Geschäftsvermögens vollumfänglich der Einkommenssteuer.»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Selbständige Erwerbstätigkeit – Nebenerwerb, Person 1 / Person 2 (Code 122/123)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsblatt bzw. Aufstellung über Nebenerwerb
- **Rein:** Hilfsblatt A Nebenerwerb (Code 1692/1693) bzw. Aufstellung Einnahmen/Ausgaben → Reingewinn · Kauf-/Verkaufsabrechnungen Wertschriften/Liegenschaften → Veräusserungsgewinne (nur bei Tätigkeit über Vermögensverwaltung hinaus)
- **Rechnen:** Hilfsblatt A Code 1750 (Kästchen Nebenerwerb 1692/1693) bzw. Reingewinn lt. Aufstellung je Person → Person 1 Code 122 / Person 2 Code 123
- **Regel:** Sämtliche Einkünfte aus selbständigen Nebenerwerbstätigkeiten, einschliesslich Gewinne aus Veräusserung von Wertschriften/Liegenschaften, wenn die Tätigkeit über blosse Vermögensverwaltung hinausgeht.
- **Beachten:** Veräusserungsgewinne nur, wenn die Tätigkeit die schlichte Vermögensverwaltung übersteigt
- **Beachten:** Staat: freizustellenden Grundstückgewinnteil in Ziff. 16.5 (Kolonne Staatssteuer) abziehen
- **Beachten:** Jahresrechnung bzw. Aufstellungen wie bei Ziff. 2.1 beilegen
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0004.md) `zh-form-300-2026-uj__c0004` – «2.2 Nebenerwerb Person 1 Hilfsblatt 122»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0042.md) `zh-wl-2026-uj__c0042` – «Hier sind sämtliche Einkünfte aus selbständigen Nebenerwerbstätigkeiten anzugeben.»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0033.md) `zh-wl-2026-uj__c0033` – «Nebenerwerb 1692 Person 1 1693 Person 2»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0043.md) `zh-wl-2026-uj__c0043` – «stammen, welche die schlichte Vermögensverwaltung übersteigt.»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0043.md) `zh-wl-2026-uj__c0043` – «Für die Staatssteuer ist der bei der Einkommenssteuer freizustellende Teil des Grund»
  - [WL ZH 2026 UJ S. 31](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0217.md) `zh-wl-2026-uj__c0217` – «Aufstellungen über Aktiven und Passiven, Einnahmen und Ausgaben sowie Privatentnahmen»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0037.md) `zh-wl-2026-uj__c0037` – «Einkünfte aus selbständiger Erwerbstätigkeit 1750»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV-/IV-Renten (100%), Person 1 / Person 2 (Code 130/131)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung AHV/IV (Form. 11 Rentenbescheinigung) Jahresbetrag
- **Rein:** AHV-/IV-Rentenbescheinigung bzw. Rentenverfügung → ausbezahlte Renten 2026
- **Rechnen:** Σ AHV-/IV-Renten 2026 × 100 % je Person → Person 1 Code 130 / Person 2 Code 131 (AHV oder IV ankreuzen)
- **Regel:** Zu 100% steuerbar. Ankreuzen AHV oder IV. Ergänzungsleistungen, Hilflosenentschädigungen u.ä. sind nicht steuerbar (nicht eintragen).
- **Beachten:** Nicht steuerbar: Ergänzungsleistungen, Hilflosenentschädigung, Pflegebeiträge, Beihilfen an AHV-/IV-Bezüger
- **Beachten:** Kapitalleistungen der AHV/IV → Ziff. 40, nicht hier
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0005.md) `zh-form-300-2026-uj__c0005` – «3.1 AHV- / IV-Renten (100%) Person 1 AHV IV 130»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0044.md) `zh-wl-2026-uj__c0044` – «Renten und Pensionen [ Ziffer 3.2]»
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0048.md) `zh-wl-2026-uj__c0048` – «Beihilfen, Arbeitslosenhilfen und Gemeindezuschüsse, welche Bezügern von AHV-, IV- und»
  - [WL ZH 2026 UJ S. 22](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0141.md) `zh-wl-2026-uj__c0141` – «Hier sind sämtliche Kapitalleistungen aus der Alters-, Hinterlassenen- und Invalidenversicherung,»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen 2. Säule, Säule 3a, Arbeitgeber, UVG/Militärversicherung (Betrag/Prozente Code 960–967, Hauptkolonne 134–137)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Rentenbescheinigung (Lohnausweis/Rentenbescheinigung Form. 11) bzw. Bescheinigung der Vorsorgeeinrichtung
- **Rein:** Rentenbescheinigung Pensionskasse/Vorsorgeeinrichtung → Jahresrente brutto, Rentenbeginn · Rentenbescheinigung Säule 3a, Arbeitgeber, SUVA/UVG, Militärversicherung → Jahresrente · Für 80 %-Satz: Nachweis Beginn Rente/Vorsorgeverhältnis und Eigenbeiträge ≥ 20 %
- **Rechnen:** Vorkolonne Betrag × Prozente = Hauptkolonne; Person 1: 960/962 × 961/963 → 134/135; Person 2: 964/966 × 965/967 → 136/137; Regelfall 100 %
- **Regel:** In die Vorkolonne (Betrag, Prozente) Gesamtbetrag und steuerbaren Prozentsatz, in die Hauptkolonne den steuerbaren Teilbetrag. Je Rentenart eine Zeile: PK-Renten grundsätzlich 100% (80% nur bei Rentenbeginn vor 1.1.1987 bzw. 1987–2001 mit altem Vorsorgeverhältnis und mind. 20% Eigenleistung); Arbeitgeberrenten 100%; Renten Säule 3a 100%; SUVA/UVG-Renten 60/80/100% je nach Unfalldatum und Prämientragung; Militärversicherung 100% (Ausnahmen steuerfrei).
- **Beachten:** PK 80 %: Beginn vor 1987, oder 1987–2001 und Vorsorgeverhältnis Ende 1985 (Bund Ende 1986); je ≥ 20 % Eigenbeiträge
- **Beachten:** UVG/SUVA 60 % bzw. 80 % nur bei Nichtberufsunfall vor 1986 und Prämien ganz bzw. ≥ 20 % selbst getragen
- **Beachten:** MV steuerfrei: Invaliden-/Hinterlassenenrenten mit Beginn vor 1994, Integritätsschadensrenten, Genugtuung
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0005.md) `zh-form-300-2026-uj__c0005` – «Person 1 960 113211 961 111 134 3213211»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0044.md) `zh-wl-2026-uj__c0044` – «Von Arbeitgebern (also nicht von einer Pensionskasse) ausgerichtete Renten»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0047.md) `zh-wl-2026-uj__c0047` – «Bei nicht zu 100% steuerbaren Renten ist in den Vorkolonnen der Steuererklärung der»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0045.md) `zh-wl-2026-uj__c0045` – «Folgende Leistungen der Militärversicherung sind jedoch steuerfrei»

<a id="3-2-einkommen-vorsorge-uebrige-renten"></a>
### Ziff. 3.2 – Leibrenten und Verpfründung (Ertragsanteil; Code 960–967 / 134–137)

- **Schlüssel:** `einkommen.vorsorge.uebrige_renten` (Übrige Renten (Leibrenten, ausländische Renten, Militär-/Unfallversicherung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Steuerbescheinigung der Versicherungseinrichtung (Ertragsanteil); bei privaten/ausländischen Leibrenten Zahlungsbelege
- **Rein:** Steuerbescheinigung des Versicherers (CH-Leibrentenversicherung) → steuerbarer Ertragsanteil · Zahlungsbelege private/ausländische Leibrente, Verpfründung → erhaltener Gesamtbetrag
- **Rechnen:** Vorkolonne «Betrag» = Gesamtbetrag; Hauptkolonne = Ertragsanteil (CH: lt. Bescheinigung; privat/ausl.: Rente × ESTV-Satz % / 100); «Prozente» leer
- **Regel:** Gesamtbetrag in die Vorkolonne «Betrag», steuerbarer Ertragsanteil in die Hauptkolonne; Kolonne «Prozente» leer lassen. Private und ausländische Leibrenten: Ertragsanteil = Rente x ESTV-Berechnungssatz / 100; schweizerische Leibrentenversicherungen: Satz aus der Steuerbescheinigung.
- **Beachten:** ESTV-Berechnungssatz der aktuellen Steuerperiode auf estv.admin.ch bzw. zh.ch nachschlagen
- **Beachten:** Steuerbescheinigung bzw. Belege über die Zahlungseingänge beilegen
- **Beachten:** Gegenstück: Zahler zieht in Ziff. 13.3 den Ertragsanteil der bezahlten Leibrente ab
- **Quellen:**
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0046.md) `zh-wl-2026-uj__c0046` – «Berechnungsformel: Erhaltene Leibrente / Verpfründung x Berechnungssatz (in %)»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0047.md) `zh-wl-2026-uj__c0047` – «Kolonne «Prozente» ist leer zu lassen.»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0046.md) `zh-wl-2026-uj__c0046` – «Bei Leibrentenversicherungen finden Sie den steuerbaren Ertragsanteil in der jährlich vom Versicherer auszustellenden Steuerbescheinigung.»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0046.md) `zh-wl-2026-uj__c0046` – «rechnungssatz und weitere Informationen finden Sie auf unserer Website unter»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0071.md) `zh-wl-2026-uj__c0071` – «Abzugsfähig ist der Ertragsanteil der bezahlten Leibrenten und Verpfründungen.»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigungen aus Arbeitslosenversicherung, direkt ausbezahlt, Person 1 / Person 2 (Code 140/141)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Arbeitslosenkasse (Taggelder brutto)
- **Rein:** Bescheinigung der Arbeitslosenkasse → direkt ausbezahlte Taggelder 2026
- **Rechnen:** Σ direkt von der Arbeitslosenkasse ausbezahlte Erwerbsausfallentschädigungen je Person → Person 1 Code 140 / Person 2 Code 141
- **Regel:** Nur direkt von der Arbeitslosenkasse ausbezahlte Entschädigungen; vom Arbeitgeber ausbezahlte Leistungen stehen bereits im Lohnausweis. Bescheinigung beilegen.
- **Beachten:** Nur direkt ausbezahlte Entschädigungen (Formularhinweis zu 3.3)
- **Beachten:** Bescheinigung der Arbeitslosenkasse beilegen
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0005.md) `zh-form-300-2026-uj__c0005` – «3.3 Erwerbsausfallentschädigungen aus Arbeitslosenversicherung»
  - [WL ZH 2026 UJ S. 31](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0218.md) `zh-wl-2026-uj__c0218` – «Bescheinigung der Arbeitslosenkasse über erhaltene Taggelder.»
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0048.md) `zh-wl-2026-uj__c0048` – «Die entsprechenden Bescheinigungen sind beizulegen.»

<a id="3-4-einkommen-ersatz-taggelder"></a>
### Ziff. 3.4 – Taggelder aus Kranken-, Unfall-, Invaliden-, Militärversicherung, EO, Mutterschaftsentschädigungen, Person 1 / Person 2 (Code 142/143)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Versicherung/EO-Ausgleichskasse
- **Rein:** Taggeldabrechnung Kranken-, Unfall-, Invalidenversicherung, Militärversicherung → Taggelder 2026 · Bescheinigung der Ausgleichskasse → EO- und Mutterschaftsentschädigungen
- **Rechnen:** Σ nicht im Lohnausweis enthaltene Taggelder, EO- und Mutterschaftsentschädigungen je Person → Person 1 Code 142 / Person 2 Code 143
- **Regel:** Steuerpflichtiges Einkommen, wenn nicht durch den Arbeitgeber im Lohnausweis bescheinigt und mit dem Lohn übertragen. Bescheinigung der Versicherungseinrichtung einholen und beilegen. Nicht steuerbar: Ergänzungsleistungen, Hilflosenentschädigungen u.ä. (siehe separate Zeile).
- **Beachten:** Vom Arbeitgeber im Lohnausweis bescheinigte und mit dem Lohn übertragene Taggelder nicht nochmals erfassen
- **Beachten:** Bescheinigung bei der Versicherungseinrichtung verlangen und beilegen
- **Beachten:** Direkt von der Ausgleichskasse ausbezahlte Kinder-/Familienzulagen gehören in dieselbe Zeile
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0049.md) `zh-wl-2026-uj__c0049` – «Taggelder aus Kranken-, Unfall- und Invalidenversicherung, aus Militärversicherung sowie die»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0005.md) `zh-form-300-2026-uj__c0005` – «3.4 Kinder- und Familienzulagen, Mutterschaftsentschädigungen, Taggelder»

<a id="3-4-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.4 – Kinder- und Familienzulagen, direkt von der Ausgleichskasse ausbezahlt (Code 142/143)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Familienausgleichskasse (nicht im Lohnausweis enthaltene Zulagen)
- **Rein:** Bescheinigung der Familienausgleichskasse → direkt ausbezahlte Kinder- und Familienzulagen 2026
- **Rechnen:** Σ direkt von der Ausgleichskasse ausbezahlte Kinder-/Familienzulagen je Person → Code 142 / 143 (zusammen mit Taggeldern)
- **Regel:** Nur Zulagen eintragen, die nicht über den Arbeitgeber im Lohnausweis (Ziff. 1) enthalten sind, sondern direkt von der Ausgleichskasse ausgerichtet wurden – sonst Doppelerfassung.
- **Beachten:** Im Lohnausweis bescheinigte und mit dem Lohn übertragene Zulagen → hier nicht (Doppelerfassung)
- **Beachten:** Bescheinigung der Ausgleichskasse beilegen
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0005.md) `zh-form-300-2026-uj__c0005` – «3.4 Kinder- und Familienzulagen, Mutterschaftsentschädigungen, Taggelder»
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0049.md) `zh-wl-2026-uj__c0049` – «von Ausgleichskassen direkt ausbezahlten Kinder- und Familienzulagen und Mutterschafts-»
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0049.md) `zh-wl-2026-uj__c0049` – «eine Bescheinigung über diese Einkünfte und reichen Sie diese mit der Steuererklärung ein.»
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0049.md) `zh-wl-2026-uj__c0049` – «Sind sie nicht durch die Arbeitgeber im»

<a id="3-hinweis-info-steuerfreie-leistungen"></a>
### Ziff. 3 (Hinweis) – Nicht steuerbare Unterstützungsleistungen (Ergänzungsleistungen, Hilflosenentschädigungen, Pflegebeiträge u.ä.) – nur Angabe, nicht einsetzen

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung/Bescheinigung der EL-Stelle
- **Rein:** Verfügung/Bescheinigung EL-Stelle, Hilflosenentschädigung, Pflegebeiträge → nur Kontrolle, kein Eintrag
- **Rechnen:** Kein Eintrag (steuerfrei): EL, Hilflosenentschädigungen, Pflegebeiträge, Beihilfen, Arbeitslosenhilfen, Gemeindezuschüsse an AHV-/IV-/UVG-Bezüger
- **Regel:** Nicht in die Einkünfte aufnehmen; Pflegebeiträge, Hilflosenentschädigungen, Ergänzungsleistungen, Beihilfen, Arbeitslosenhilfen und Gemeindezuschüsse für Bezüger von AHV-, IV- und UVG-Leistungen sind nicht steuerbar. Die Renten und Taggelder selbst (AHV/IV, UVG usw.) bleiben steuerbar (Ziff. 3.1–3.4).
- **Beachten:** Die zugrunde liegenden AHV-/IV-/UVG-Renten und Taggelder bleiben steuerbar (Ziff. 3.1–3.4)
- **Beachten:** Bei Unsicherheit über die Steuerbarkeit das Gemeindesteueramt fragen
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0048.md) `zh-wl-2026-uj__c0048` – «ausgerichtet werden, sind nicht steuerbar.»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0044.md) `zh-wl-2026-uj__c0044` – «Diese sind wie folgt steuerbar: AHV- und IV-Renten [ Ziffer 3.1]»
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0052.md) `zh-wl-2026-uj__c0052` – «Bei Unsicherheiten über die Steuerbarkeit wenden Sie sich an das zuständige Gemeindesteueramt.»

<a id="4-1-einkommen-wertschriften"></a>
### Ziff. 4.1 – Ertrag aus Wertschriften, Guthaben und Lotterien (Code 150)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Wertschriften- und Guthabenverzeichnis (Form. 340) Total Bruttoertrag Kolonne A + B; eSteuerauszug der Bank
- **Rein:** eSteuerauszug/Steuerauszug Bank → Import in Form. 340 (Bruttoerträge, Steuerwerte) · Zins-/Kontoauszüge → Bruttozinsen (Kolonne A bei VSt-Abzug, sonst B) · Dividenden-/Fondsabrechnungen Ausland → Bruttoertrag in CHF zum Tageskurs; ggf. Antrag DA-1
- **Rechnen:** Form. 340: Σ Bruttoertrag Kolonne A (mit VSt) + Kolonne B (ohne VSt, inkl. DA-1-Total) → Code 150; Fremdwährung × Tageskurs
- **Regel:** Total aus dem Wertschriftenverzeichnis übertragen (Online: Import eSteuerauszug). Erträge brutto, Auslandserträge zum Tageskurs in CHF. Ertrag aus Nutzniessung zu 100%. Vorsorgeguthaben (2. Säule, Säule 3a) nicht aufführen. Gewinne aus nicht steuerfreien Geldspielen/Lotterien ebenfalls hier (Freibeträge siehe separate Zeile).
- **Beachten:** Kolonne A: CH-Zinsen/-Dividenden, Kundenguthaben mit Zins > CHF 200; Kolonne B: Zins ≤ CHF 200, Auslandserträge
- **Beachten:** Einbeziehen: Kinder Jg. 2009 und jünger, Nutzniessungsvermögen (100 %); nicht: 2. Säule, Säule 3a
- **Beachten:** DA-1-Anrechnung nur bei nicht rückforderbaren ausl. Steuern > CHF 100; Fonds: auch thesaurierte Erträge steuerbar
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «4.1 Ertrag aus Wertschriften, Guthaben und Lotterien Wertschriftenverzeichnis 150»
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0050.md) `zh-wl-2026-uj__c0050` – «Ertrag aus Nutzniessung ist zu 100% einzutragen.»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0153.md) `zh-wl-2026-uj__c0153` – «Online-Steuererklärung importieren und müssen die darin enthaltenen Angaben nicht mehr ins»
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0160.md) `zh-wl-2026-uj__c0160` – «Dies gilt auch für Kundenguthaben mit einem Bruttozins von mehr als»
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0166.md) `zh-wl-2026-uj__c0166` – «Kundenguthaben, wenn der Zins nicht um die eidg. Verrechnungssteuer gekürzt wurde (Zinsertrag bis und mit CHF 200).»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0154.md) `zh-wl-2026-uj__c0154` – «minderjährigen Kinder des Jahrgangs 2009 und jüngeren sowie das Vermögen, an dem Sie»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0155.md) `zh-wl-2026-uj__c0155` – «sind bis zur Fälligkeit der Leistungen steuerfrei und nicht im Wertschriftenverzeichnis aufzuführen.»
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0168.md) `zh-wl-2026-uj__c0168` – «Devisen ausgerichteten Erträge solcher Wertschriften sind zum Tageskurs in Schweizer»
  - [WL ZH 2026 UJ S. 26–27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0169.md) `zh-wl-2026-uj__c0169` – «Die Totalbeträge des DA-1 übertragen Sie in die Zeile «Übertrag ab Formular DA-1» im Wertschriftenverzeichnis (Seite 3), wobei das Total Bruttoertrag unter»
  - [WL ZH 2026 UJ S. 26–27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0169.md) `zh-wl-2026-uj__c0169` – «insgesamt den Betrag von CHF 100 nicht übersteigen, wird keine Anrechnung ausländischer»
  - [WL ZH 2026 UJ S. 25–26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0163.md) `zh-wl-2026-uj__c0163` – «Neben den ausgeschütteten sind auch zurückbehaltene (thesaurierte) Erträge steuerbar.»

<a id="4-1-einkommen-lotterie-gewinne"></a>
### Ziff. 4.1 – Lotto-, Grossspiel- und Online-Spielbankengewinne (Teil von Code 150)

- **Schlüssel:** `einkommen.lotterie_gewinne` (Lotterie-/Geldspielgewinne (steuerbarer Teil)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Gewinnbescheinigung der Lotteriegesellschaft/Bank; Verrechnungssteuer-Abzugsabschnitt
- **Rein:** Gewinnbescheinigung Lotteriegesellschaft/Bank bzw. Auszahlungsabschnitt Post → Bruttogewinn, VSt-Abzug · Belege über Einsätze (Online-Spielbanken) → effektive Einsätze für Ziff. 16.5
- **Rechnen:** je Gewinn Grossspiel/Online-Spielbank: steuerbar = max(0; Gewinn − Kanton 1'046'400 / Bund 1'071'000); Verkaufsförderung > 1'000 / 1'100 → ganzer Gewinn
- **Regel:** Gewinne aus in der Schweiz zugelassenen Grossspielen und Online-Spielbankenspielen sind bis zum Freibetrag steuerfrei (nur der übersteigende Teil steuerbar). Lotteriegewinne mit Verrechnungssteuerabzug im Wertschriftenverzeichnis aufführen, Bescheinigung beilegen. Einsatzkostenabzug: Ziff. 16.5.
- **Beachten:** Einsatzkosten Ziff. 16.5: 5 %, max. Kanton 5'200 / Bund 5'400; Online-Spielbanken effektiv max. 26'200 / 26'800
- **Beachten:** Gewinne aus ausländischen Spielbanken, Lotterien, Sportwetten steuerbar (Kolonne B)
- **Beachten:** Natural-/Sachgewinne: Freigrenze Kanton 1'000 / Bund 1'100
- **Limiten:**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'046'400 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen (BGS) steuerfrei bis Fr. 1'046'400 (Freibetrag: nur der übersteigende Anteil ist steuerbar).)** · Bund **CHF 1'071'000 (Einzelne Gewinne aus nach BGS zugelassenen Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'071'000; darüber steuerbar (abzüglich Einsatzkosten nach Art. 33 Abs. 4 DBG).)**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'000 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei, sofern die Grenze von Fr. 1'000 nicht überschritten wird (Freigrenze: bei Überschreitung ist der gesamte Gewinn steuerbar). Gewinne aus Kleinspielen (BGS) sind steuerfrei.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (Art. 1 Abs. 2 lit. d und e BGS) steuerfrei, sofern die Grenze von CHF 1'100 nicht überschritten wird. Gewinne aus Kleinspielen (BGS) sind steuerfrei.)**
- **Bund:** Freibetrag Grossspielgewinne CHF 1'071'000 (statt CHF 1'046'400); Kleingewinne Verkaufsförderung CHF 1'100 (statt CHF 1'000).
- **Quellen:**
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0164.md) `zh-wl-2026-uj__c0164` – «etc.) und aus Online-Spielbankenspielen sind bis zu einem Betrag von CHF 1’046’400 bei»
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0165.md) `zh-wl-2026-uj__c0165` – «CHF 1’000 (Staatssteuer) bzw. CHF 1’100 (Bundessteuer) steuerfrei»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0102.md) `zh-wl-2026-uj__c0102` – «Von den steuerbaren Gewinnen aus nicht steuerfreien Geldspielen können 5%, jedoch»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0102.md) `zh-wl-2026-uj__c0102` – «tens CHF 5’200 (Staatssteuer) bzw. CHF 5’400 (Bundessteuer), als Einsatzkosten abgezogen»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0103.md) `zh-wl-2026-uj__c0103` – «die effektiven Einsätze, maximal jedoch CHF 26’200 (Staatssteuer) bzw. CHF 26’800 (Bundes-»
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0166.md) `zh-wl-2026-uj__c0166` – «Gewinne aus ausländischen Spielbanken, Lotterien und Sportwetten sind steuerbar.»
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0166.md) `zh-wl-2026-uj__c0166` – «Natural- und Sachgewinne sind bis zu einem Betrag von CHF 1’000 (Staatssteuer) bzw.»

<a id="4-2-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.2 – Davon aus qualifizierten Beteiligungen (Code 151)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Ausschüttungsabrechnung/Dividendenbeleg; Wertschriftenverzeichnis mit Code Q
- **Rein:** Formular «Qualifizierte Beteiligungen im Privatvermögen» → Teilbesteuerungsabzug
- **Rechnen:** Code 151 = Σ Bruttoausschüttungen Code Q (bereits in 4.1/Code 150 enthalten); Teilbesteuerungsabzug Ziff. 16.5: Kanton 50 % / Bund 30 %
- **Regel:** Beteiligungen von mindestens 10% (Code «Q» im Wertschriftenverzeichnis): Ausschüttungen ungekürzt (brutto) in Ziff. 4.1 UND als «davon» in Ziff. 4.2 eintragen; der Teilbesteuerungsabzug erfolgt separat unter Ziff. 16.5 gemäss Formular «Qualifizierte Beteiligungen im Privatvermögen».
- **Beachten:** Beteiligung ≥ 10 % am Grund-/Stammkapital; ungekürzt brutto; Kolonne A bei VSt, sonst Kolonne B
- **Beachten:** Qualif. Beteiligungen im Geschäftsvermögen: Ertrag in Ziff. 2; Abzug Kanton 50 % / Bund 30 % nach Spartenrechnung
- **Beachten:** Gutschriftsanzeigen der qualifizierten Beteiligungen beilegen
- **Bund:** Teilbesteuerungsabzug 30% (Privatvermögen) statt 50% bei der Staatssteuer.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «4.2 Davon aus qualifizierten Beteiligungen»
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0162.md) `zh-wl-2026-uj__c0162` – «Sie sind ungekürzt, d.h. mit dem Bruttobetrag der Ausschüttung,»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0100.md) `zh-wl-2026-uj__c0100` – «im Geschäftsvermögen nach Abzug des zurechenbaren Aufwandes gemäss Spartenrechnung ebenfalls 50%.»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0100.md) `zh-wl-2026-uj__c0100` – «qualifizierte Beteiligungen im Privatvermögen beträgt 30%, für qualifizierte Beteiligungen im»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0170.md) `zh-wl-2026-uj__c0170` – «Sind die Gutschriftsanzeigen vollständig beigelegt für:»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0040.md) `zh-wl-2026-uj__c0040` – «Inklusive Erträge aus qualifizierten Beteiligungen im Geschäftsvermögen»

<a id="5-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.1 – Erhaltene Unterhaltsbeiträge vom geschiedenen/getrennten Ehegatten/Partner (Code 160)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil, Konvention, Zahlungsnachweise; Name/Adresse des Zahlers
- **Rein:** Scheidungsurteil/Trennungsvereinbarung → Unterhaltsbeiträge für den Ehegatten · Konto-/Zahlungsnachweise → 2026 tatsächlich erhaltene Beträge
- **Rechnen:** Σ 2026 erhaltene Unterhaltsbeiträge für den Ehegatten persönlich (ohne Kinderalimente) → Code 160
- **Regel:** Alimente für den Ehegatten persönlich sind von diesem als Einkommen anzugeben (Name/Adresse des Alimentenzahlers angeben).
- **Beachten:** Name/Adresse des Alimentenzahlers im Formular angeben
- **Beachten:** Kinderalimente separat in Ziff. 5.2 (Code 161)
- **Beachten:** Gegenstück: Zahler zieht dieselben Beiträge in Ziff. 13.1 voll ab
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0051.md) `zh-wl-2026-uj__c0051` – «Unterhaltsbeiträge (Alimente), die den geschiedenen, gerichtlich oder tatsächlich getrennt»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «5.1 und 5.2 Name/Adresse Alimentenzahler/in»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «5.2 Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit) 161»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0070.md) `zh-wl-2026-uj__c0070` – «Ehegatten persönlich bestimmt sind, können voll abgezogen werden.»

<a id="5-2-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.2 – Erhaltene Unterhaltsbeiträge für minderjährige Kinder (Code 161)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Urteil/Konvention, Zahlungsnachweise; Alimentenbevorschussung
- **Rein:** Urteil/Unterhaltsvertrag → Kinderalimente je Kind · Abrechnung Alimentenbevorschussung → bevorschusste Beträge · Konto-/Zahlungsnachweise → erhaltene Zahlungen bis und mit Monat des 18. Geburtstags
- **Rechnen:** Σ Kinderalimente + Bevorschussungen bis und mit dem Monat, in dem das Kind 18 wird → Code 161; danach nicht mehr deklarieren
- **Regel:** Kinderalimente bis und mit dem Monat der Volljährigkeit (18. Altersjahr) als Einkommen deklarieren; Alimentenbevorschussungen sind gleichgestellt. Ab dem Folgemonat nicht mehr deklarieren. Wirkt auf den Kinderabzug (Ziff. 24.1: ganzer Abzug bei erhaltenen Alimenten und gemeinsamer Sorge).
- **Beachten:** Erhaltene Alimente bei gemeinsamer Sorge → ganzer Kinderabzug Kanton 9'400 / Bund 6'800 (Ziff. 24.1)
- **Beachten:** Volljährige in Erstausbildung: Kinderabzug nur, wenn Sie trotz Alimenten zur Hauptsache für den Unterhalt aufkommen
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 9'400 (Kinderabzug je Kind (minderjährig unter elterlicher Sorge/Obhut oder volljährig in beruflicher Erstausbildung, Unterhalt zur Hauptsache): Fr. 9'400. Bei nicht gemeinsam besteuerten Eltern hälftig aufgeteilt (Fr. 4'700), wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge für das Kind abgezogen werden.)** · Bund **CHF 6'800 (Kinderabzug CHF 6'800 pro minderjähriges oder in beruflicher/schulischer Ausbildung stehendes Kind, für dessen Unterhalt die steuerpflichtige Person sorgt; bei getrennter Besteuerung der Eltern hälftig bei gemeinsamer elterlicher Sorge ohne Unterhaltsbeiträge.)**
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0051.md) `zh-wl-2026-uj__c0051` – «dem das Kind das 18. Altersjahr erreicht, als Einkommen in die Steuererklärung einzutragen.»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «5.2 Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit) 161»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0126.md) `zh-wl-2026-uj__c0126` – «wenn die elterliche Sorge Ihnen und dem anderen Elternteil gemeinsam zusteht und Sie steuerbare Unterhaltsbeiträge für das Kind erhalten»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0126.md) `zh-wl-2026-uj__c0126` – «wenn der andere Elternteil für das Kind keine Unterhaltsbeiträge leistet oder wenn Unterhaltsbeiträge geleistet werden, Sie aber»

<a id="5-3-einkommen-uebrige"></a>
### Ziff. 5.3 – Ertrag aus Geschäfts- und Korporationsanteilen (Code 162)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung über Kapital und Ertrag
- **Rein:** Aufstellung über Kapital und Ertrag der Geschäfts-/Korporationsanteile → eigener Ertragsanteil
- **Rechnen:** Ertrag × eigene Beteiligungsquote → Code 162
- **Regel:** Anteilmässig nach Beteiligungsquote deklarieren; Aufstellung über Kapital und Ertrag beilegen. Vermögenswert: Ziff. 30.5.
- **Beachten:** Aufstellung über Kapital und Ertrag beilegen
- **Beachten:** Vermögenswert ebenfalls anteilmässig in Ziff. 30.5 deklarieren
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0051.md) `zh-wl-2026-uj__c0051` – «Einkünfte aus Geschäfts- und Korporationsanteilen sind von den Inhabern anteilmässig ent-»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «5.3 Ertrag aus Geschäfts- und Korporationsanteilen Aufstellung 162»
  - [WL ZH 2026 UJ S. 31](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0218.md) `zh-wl-2026-uj__c0218` – «Inhaber von Geschäfts- und Korporationsanteilen • Aufstellung über Kapital und Ertrag.»
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0139.md) `zh-wl-2026-uj__c0139` – «Geschäfts- und Korporationsanteile sind von den Inhabern anteilmässig entsprechend ihrer Beteiligungsquote zu deklarieren.»

<a id="5-4-einkommen-uebrige"></a>
### Ziff. 5.4 – Weitere Einkünfte, nähere Bezeichnung (Code 163)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung/Bescheinigung je Einkunftsart
- **Rein:** Aufstellung/Belege je Einkunftsart (z.B. im Lohnausweis nicht ausgewiesene Trinkgelder) → Betrag + Bezeichnung · Verfügung Förderbeitrag Energie/Umwelt → ausbezahlter Betrag (falls nicht mit Unterhaltskosten verrechnet) · Verfügung Bundesbeitrag an Vorbereitungskurs eidg. Prüfung → Beitrag
- **Rechnen:** Σ übrige steuerbare Einkünfte mit näherer Bezeichnung → Code 163; Bundesbeiträge Vorbereitungskurse: nur Überschuss über geltend gemachte Weiterbildungskosten
- **Regel:** Auffangposition für steuerpflichtige Einkünfte, die unter den übrigen Ziffern nicht aufgeführt sind: im Lohnausweis nicht ausgewiesene Trinkgelder, wiederkehrende Zahlungen bei Tod/bleibenden Nachteilen, Bundesbeiträge an Vorbereitungskurse (soweit sie die geltend gemachten Weiterbildungskosten übersteigen), Förderbeiträge für Energiemassnahmen (im Jahr der Auszahlung, soweit nicht direkt mit den Unterhaltskosten verrechnet). Naturalbezüge jeder Art sind steuerpflichtig.
- **Beachten:** Förderbeiträge im Auszahlungsjahr, soweit nicht direkt von den Unterhaltskosten im Liegenschaftenverzeichnis abgezogen
- **Beachten:** Wiederkehrende Zahlungen bei Tod/bleibenden Nachteilen hier; Vorsorge-Kapital → Ziff. 40; Kapitalabfindungen → 5.5
- **Beachten:** Naturalbezüge jeder Art steuerbar; bei Unsicherheit Gemeindesteueramt fragen
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0052.md) `zh-wl-2026-uj__c0052` – «Hier sind weitere Einkünfte einzutragen, die der Steuerpflicht unterliegen und unter den übrigen»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0197.md) `zh-wl-2026-uj__c0197` – «Förderbeiträge für Energiespar- und Umweltschutzmassnahmen sind im Jahr der Auszahlung»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0198.md) `zh-wl-2026-uj__c0198` – «unter Ziffer 5.4 der Steuererklärung als weitere Einkünfte zu deklarieren, soweit sie nicht direkt»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0043.md) `zh-wl-2026-uj__c0043` – «5.5: Kapitalleistungen aus Vor- sorge sind auf Seite 4, Ziffer 40 einzutragen.»

<a id="5-5-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 5.5 – Kapitalabfindungen für wiederkehrende Leistungen (Code 164)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung des Leistungserbringers; Anzahl Monate
- **Rein:** Bescheinigung/Abrechnung des Leistungserbringers → Kapitalabfindung (Betrag) und Anzahl abgegoltene Monate
- **Rechnen:** Betrag → Code 164; Anzahl Monate → Code 1641; Satzbestimmung zum Betrag der jährlichen Leistung
- **Regel:** Für die Satzbestimmung den Betrag einsetzen, der der jährlichen Leistung entspricht (Anzahl Monate angeben). Kapitalleistungen aus Vorsorge gehören NICHT hierher, sondern auf Seite 4 Ziff. 40.
- **Beachten:** Kapitalleistungen aus Vorsorge (AHV/IV, 2. Säule, Freizügigkeit, Säule 3a) → Seite 4 Ziff. 40, nicht hier
- **Beachten:** Kapitalzahlungen bei Tod und für bleibende Nachteile ebenfalls → Ziff. 40
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0053.md) `zh-wl-2026-uj__c0053` – «Diese werden bei der Ermittlung des Steuersatzes zu dem Betrag eingesetzt, welcher der jährlichen Leistung entspricht.»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0043.md) `zh-wl-2026-uj__c0043` – «5.5: Kapitalleistungen aus Vor- sorge sind auf Seite 4, Ziffer 40 einzutragen.»
  - [WL ZH 2026 UJ S. 22](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0141.md) `zh-wl-2026-uj__c0141` – «Hier sind sämtliche Kapitalleistungen aus der Alters-, Hinterlassenen- und Invalidenversicherung,»
  - [WL ZH 2026 UJ S. 22](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0142.md) `zh-wl-2026-uj__c0142` – «Arbeitgebers mit Vorsorgecharakter und sämtliche Kapitalzahlungen bei Tod und für bleibende»

<a id="6-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. 6 – Nettoertrag aus Liegenschaften – Eigenmietwert selbstbewohnter Liegenschaften (Code 188)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftenverzeichnis (Form. 350) Rückseite: Eigenmietwert/Miet- und Pachtzinseinnahmen; Liegenschaftenbewertung der Gemeinde
- **Rein:** Liegenschaftenneubewertung 2026 (Gemeindesteueramt) → Eigenmietwert EFH/STWE; mit der Erklärung einreichen · Mieterspiegel/Verwaltungsabrechnung → Miet- und Pachtzinseinnahmen · Aufstellung/Belege Unterhalts- und Verwaltungskosten (nur bei effektivem Abzug) · Liegenschaftenverzeichnis (Form. 350) → Code 3953 Nettoertrag
- **Rechnen:** Σ je Liegenschaft: EMW + Miet-/Pachtzinsen − Unterhalt/Verwaltung (effektiv oder Pauschale) = Form. 350 Code 3953 → Code 188
- **Regel:** Nettoertrag (Eigenmietwert bzw. Mieteinnahmen abzüglich Unterhalt/Verwaltung) aus Form. 350 Code 3953 übertragen. Liegenschaften bis und mit Baujahr 2025: weiterhin Eigenmietwert nach Weisung 2009 (ohne Erhöhung); Neubauten ab 2026: Weisung 2026 mit pauschalem Abzug von 10%. Selbstgenutzte Wohnung im MFH/Geschäftshaus (ohne STWE): 70% des erzielbaren Mietzinses. Wohnrecht/Nutzniessung: Eigenmietwert beim Berechtigten.
- **Beachten:** Baujahr ≤ 2025: EMW nach Weisung 2009 (ohne Erhöhung); Neubau ab 2026: EMW nach Weisung 2026 − 10 %
- **Beachten:** Wohnung im eigenen MFH/Geschäftshaus (ohne STWE): 70 % der Drittmiete; Wohnrecht/Nutzniessung: 100 % beim Berechtigten
- **Beachten:** Pauschale (Wahl je Liegenschaft): Kanton 20 % / Bund 10 % (≤ 10 J.) bzw. 20 %; nicht bei vorwiegend geschäftl. Nutzung
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **10 % (Eigenmietwert: Für Liegenschaften bis und mit Baujahr 2025 gelten weiterhin die Eigenmietwerte nach Weisung 2009 (ohne Erhöhung); für Neubauten ab 2026 gilt die Weisung 2026 mit einem pauschalen Abzug von 10 % zum Ausgleich der höheren Eigenmietwerte. Selbstgenutzte Wohnungen in Mehrfamilien-/Geschäftshäusern: 70 % des erzielbaren Mietzinses. Gesetzliche Leitlinie: Eigenmietwert max. 70 % des Marktwerts.)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **20 % (Pauschalabzug für Unterhalts- und Verwaltungskosten von Liegenschaften des Privatvermögens: 20 % des Brutto-Mietertrags bzw. Mietwerts je Liegenschaft; ZH kennt keine Abstufung nach Gebäudealter. Wahl pro Liegenschaft und Steuerperiode; nicht bei ganz oder vorwiegend geschäftlich genutzten Liegenschaften; daneben nur Baurechtszinsen abziehbar.)** · Bund **10 % (Pauschalabzug Liegenschaftskosten (anstelle effektiver Kosten, Wahl pro Periode und Liegenschaft): 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist.)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Gleicher Satz wie für jüngere Gebäude: 20 % des Brutto-Mietertrags bzw. Mietwerts (keine Altersabstufung in ZH).)** · Bund **20 % (Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist.)**
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «6. Nettoertrag aus Liegenschaften Liegenschaftenverzeichnis 188»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0181.md) `zh-wl-2026-uj__c0181` – «gelten für Zürcher Liegenschaften bis und mit Baujahr 2025 deshalb weiterhin die bisherigen»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0182.md) `zh-wl-2026-uj__c0182` – «Abzug von 10% vorgenommen»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0178.md) `zh-wl-2026-uj__c0178` – «(ohne Stockwerkeigentum) sind 70% des Mietzinses einzusetzen, der bei»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0177.md) `zh-wl-2026-uj__c0177` – «Nettoertrag aus Liegenschaften 3953»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0179.md) `zh-wl-2026-uj__c0179` – «tum ist auf der Liegenschaftenneubewertung 2026 ausgewiesen.»
  - [WL ZH 2026 UJ S. 8](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0022.md) `zh-wl-2026-uj__c0022` – «Die Liegenschaftenneubewertung 2026 ist zusammen mit der Steuer- erklärung 2026 einzureichen.»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0184.md) `zh-wl-2026-uj__c0184` – «Für vermietete Liegenschaften ist eine detaillierte Ertragsaufstellung (Mieterspiegel) beizu-»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0191.md) `zh-wl-2026-uj__c0191` – «und beträgt 20% für jede Liegenschaft.»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0190.md) `zh-wl-2026-uj__c0190` – «ist der Eigenmietwert zu 100% durch die wohnrechts- bzw. nutzniessungsberechtigte Person zu versteuern.»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0190.md) `zh-wl-2026-uj__c0190` – «Ein Pauschalabzug ist jedoch nicht zulässig, wenn die Liegen- schaft vorwiegend geschäftlich genutzt wird.»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags»

<a id="6-h-rtefall-unternutzung-sozialabzug-eigenmietwert"></a>
### Ziff. 6 (Härtefall/Unternutzung) – Einschlag auf dem Eigenmietwert (Unternutzung; Härtefalleinschlag auf Antrag)

- **Schlüssel:** `sozialabzug.eigenmietwert` (Einschlag/Abzug auf dem Eigenmietwert (kantonal)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Antrag/Begründung bei der Gemeinde bzw. im Liegenschaftenverzeichnis
- **Rein:** Angaben Zimmerzahl, Bewohner, tatsächlich genutzte Räume → Unternutzungseinschlag (Weisung ZStB 21.2) · Antrag mit Nachweis Einkünfte/Vermögen des Haushalts → Härtefall-Herabsetzung (§ 21 Abs. 2 lit. d StG)
- **Rechnen:** EMW − angemessener Einschlag; Härtefall (selbst bewohnt, auf Antrag): Herabsetzung, wenn EMW vs. Einkünfte/Vermögen des Haushalts dauernd übermässig
- **Regel:** Unternutzung: In Ausnahmefällen angemessener Einschlag bei verminderten Wohnbedürfnis (z.B. Wegzug der Kinder; keine Unternutzung bei 4–6 Zimmern und 2 Personen). Härtefall: § 21 Abs. 2 lit. d StG (Nachtrag 132, Stand 1.4.2026) sieht auf Antrag eine angemessene Herabsetzung bei übermässiger Belastung vor; die WL 2026 UJ liess offen, ob die zugehörige Weisung bereits per 1.1.2026 gilt – Anwendung (ZStB 21.3) im Einzelfall prüfen.
- **Beachten:** Unternutzung nur bei vermindertem Wohnbedarf (z.B. Wegzug der Kinder); vier bis sechs Zimmer ab zwei Bewohnern: keine
- **Beachten:** Zweifamilienhaus teils vermietet: EMW des selbstbewohnten Teils nach den Unternutzungsregeln
- **Beachten:** Bund: Unternutzung nur bei dauernd unbenutzten Räumen (Nachweis Stpfl.); Härtefall-Weisung ZH 2026 offen → zh.ch prüfen
- **Bemerkung:** Inkrafttreten des Härtefalleinschlags (Weisung) in der WL 2026 UJ offen; StG-Fassung Stand 1.4.2026 enthält § 21 Abs. 2 lit. d.
- **Quellen:**
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0186.md) `zh-wl-2026-uj__c0186` – «Auf dem Eigenmietwert kann in Ausnahmefällen ein angemessener Einschlag gewährt wer-»
  - [StG ZH § 21](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-21-t2.md) `zh-stg-2026__par-21-t2` – «ist der Eigenmietwert auf Antrag angemessen herabzusetzen»
  - [WL ZH 2026 UJ S. 8](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0023.md) `zh-wl-2026-uj__c0023` – «die (Wieder-)Einführung eines Härtefalleinschlags auf dem Eigenmietwert beschlossen.»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0188.md) `zh-wl-2026-uj__c0188` – «Wohneigentum mit vier bis sechs Zimmern liegt keine Unternutzung vor, wenn zwei oder»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0188.md) `zh-wl-2026-uj__c0188` – «(z.B. Wegzug der Kinder) nur noch einen Teil seines Wohneigentums tatsächlich nutzt.»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0030.md) `bund-wl-2a-2026__c0030` – «nen Räume dauernd nicht benutzt werden.»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0030.md) `bund-wl-2a-2026__c0030` – «Unternutzung ist von der steuerpflichtigen Person zu erbringen.»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0189.md) `zh-wl-2026-uj__c0189` – «betreffend Festsetzung des Eigenmietwertes bei tatsächlicher Unternutzung (ZStB 21.2)»»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0183.md) `zh-wl-2026-uj__c0183` – «nach den Regeln der Unternutzung berechnet werden.»
  - [DBG Art. 21](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-21.md) `bund-dbg-2026__art-21` – «unter Berücksichtigung der ortsüblichen Verhältnisse und der tatsächlichen Nutzung der am Wohnsitz selbstbewohnten Liegenschaft»
  - [WL 2a 2026 S. 4](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0030.md) `bund-wl-2a-2026__c0030` – «Eine weniger intensive Nutzung berechtigt nicht zum Abzug.»
  - [WL ZH 2026 UJ S. 8](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0023.md) `zh-wl-2026-uj__c0023` – «per 1.1.2026 oder zu einem späteren Zeitpunkt in Kraft treten werden»

<a id="6-einkommen-liegenschaften-mietertrag"></a>
### Ziff. 6 – Nettoertrag aus Liegenschaften – Miet- und Pachtzinserträge vermieteter Liegenschaften (Code 188)

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Liegenschaftenverzeichnis (Form. 350) Rückseite; Mieterspiegel oder Verwaltungsabrechnung
- **Rein:** Mieterspiegel (Ertragsaufstellung) → Miet-/Pachtzinse je Objekt (inkl. Garagen, Abstellplätze, Gewerberäume, Reklame) · Verwaltungsrechnung (Kopie) → Mietzinseinnahmen ohne NK-Entschädigungen (Heizung, Warmwasser, Treppenhaus) · Beiblatt zum Liegenschaftenverzeichnis → nur falls weder Ertragsaufstellung noch Verwaltungsrechnung vorliegt · Liegenschaftenverzeichnis (Rückseite) → Nettoertrag aus Liegenschaften → Ziff. 6 (Code 188)
- **Rechnen:** je Liegenschaft: Miet-/Pachtzinse (ohne NK-Entschädigungen ≤ Aufwand) + EMW selbst genutzt − Unterhalt; Σ + Übertrag weitere Verzeichnisse = Nettoertrag → Code 188
- **Regel:** Steuerbar sind sämtliche Miet- und Pachtzinseinnahmen (inkl. Garagen, Abstellplätze, gewerbliche Räume, Reklame) ohne Entschädigungen der Mieter für Heizung, Warmwasser, Treppenhausreinigung, soweit diese die tatsächlichen Aufwendungen nicht übersteigen. Je Liegenschaft Ertragsaufstellung (Mieterspiegel) beilegen; liegt keine vor: Beiblatt zum Liegenschaftenverzeichnis.
- **Beachten:** NK-Entschädigungen nur ausklammern, soweit sie den tatsächlichen Aufwand nicht übersteigen
- **Beachten:** Selbst genutzte Wohnung im MFH/Geschäftshaus (ohne STWE): EMW = 70 % der erzielbaren Drittmiete
- **Beachten:** Anteil an Liegenschaft in unverteilter Erbschaft: zusätzliche Deklarationshinweise WL S. 23
- **Quellen:**
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0176.md) `zh-wl-2026-uj__c0176` – «Steuerbar sind sämtliche Miet- und Pachtzinseinnahmen (inkl. Einnahmen z.B. für Gara»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0179.md) `zh-wl-2026-uj__c0179` – «Für jede Liegenschaft ist eine Ertragsaufstellung (Mieterspiegel) mit folgenden Angaben beizulegen:»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «6. Nettoertrag aus Liegenschaften Liegenschaftenverzeichnis 188»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0177.md) `zh-wl-2026-uj__c0177` – «Übertrag der Zahlen aus weiteren Liegenschaftenverzeichnissen»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0178.md) `zh-wl-2026-uj__c0178` – «sind 70% des Mietzinses einzusetzen, der bei»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0178.md) `zh-wl-2026-uj__c0178` – «Wir bitten Sie für jede Liegenschaft, in der Reihenfolge wie auf der Vorderseite, die gewünschten Angaben über Eigenmietwert/Miet- und»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0202.md) `zh-wl-2026-uj__c0202` – «beachten Sie bitte zusätzlich die Deklarationshinweise auf Seite 23.»

<a id="6-abzug-liegenschaft-unterhalt"></a>
### Ziff. 6 – Nettoertrag aus Liegenschaften – Unterhalts- und Verwaltungskosten (Pauschale oder effektiv; im Netto-Code 188 enthalten)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Rechnungen/Verwaltungsabrechnung, Gebäudeversicherungsprämien; Beiblatt zum Liegenschaftenverzeichnis
- **Rein:** Handwerker-/Unterhaltsrechnungen → effektive Kosten (Datum, Art der Leistung, Empfänger, Betrag) · Verwaltungsabrechnung → Unterhalts- und Verwaltungskosten durch Dritte · Prämienrechnung Gebäudeversicherung → Versicherungsprämien · Baurechtsvertrag / Zinsbelege → Baurechtszinsen (separate Aufstellung)
- **Rechnen:** je Liegenschaft wählen: pauschal Kanton 20 % / Bund 10 % (Gebäude ≤ 10 J.) bzw. 20 % × Bruttomietertrag/EMW | effektiv Σ Belege; + Baurechtszins
- **Regel:** Pro Liegenschaft Wahlrecht Pauschale oder effektive Kosten. Pauschale (Staatssteuer) 20% des deklarierten Bruttomietertrags (bei vermieteten Liegenschaften abzüglich Heizungs-/Warmwasser-/Treppenhausentschädigungen); kein Pauschalabzug bei vorwiegend geschäftlicher Nutzung; bei Pauschale keine weiteren Abzüge (ausser Baurechtszinsen). Effektiv: detaillierte Aufstellung (Datum, Art, Empfänger, Betrag) beilegen. Baurechtszinsen zusätzlich abziehbar (Aufstellung beilegen).
- **Beachten:** Pauschale schliesst weitere Abzüge aus (ausser Baurechtszins); vorwiegend geschäftlich genutzt: nur effektiv
- **Beachten:** Effektiv: Aufstellung bzw. Verwaltungsabrechnung beilegen, sonst Beiblatt zum Liegenschaftenverzeichnis
- **Beachten:** Bund: Baurechtszins nicht abziehbar bei EMW auf Zeitbauwert; Wahl pauschal/effektiv jede Periode neu (LKV Art. 5)
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **20 % (Pauschalabzug für Unterhalts- und Verwaltungskosten von Liegenschaften des Privatvermögens: 20 % des Brutto-Mietertrags bzw. Mietwerts je Liegenschaft; ZH kennt keine Abstufung nach Gebäudealter. Wahl pro Liegenschaft und Steuerperiode; nicht bei ganz oder vorwiegend geschäftlich genutzten Liegenschaften; daneben nur Baurechtszinsen abziehbar.)** · Bund **10 % (Pauschalabzug Liegenschaftskosten (anstelle effektiver Kosten, Wahl pro Periode und Liegenschaft): 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist.)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Gleicher Satz wie für jüngere Gebäude: 20 % des Brutto-Mietertrags bzw. Mietwerts (keine Altersabstufung in ZH).)** · Bund **20 % (Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist.)**
- **Bund:** Pauschale bei der direkten Bundessteuer: 10% des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist, sonst 20% (Art. 5 Abs. 2 LKV); Wahl pro Liegenschaft. Baurechtszinsen: bei der direkten Bundessteuer nicht abziehbar, wenn der Eigenmietwert auf dem Zeitbauwert beruht (siehe WL 2026 UJ).
- **Bemerkung:** korrigiert durch Prüfung: Bund-Pauschale (10%/20% nach Gebäudealter, LKV) ergänzt; die ZH-Wegleitung nennt nur 20%.
- **Quellen:**
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0191.md) `zh-wl-2026-uj__c0191` – «beträgt 20% für jede Liegenschaft»
  - [WL ZH 2026 UJ S. 28–29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0192.md) `zh-wl-2026-uj__c0192` – «Für jede Liegenschaft, für welche die tatsächlichen Aufwendungen geltend gemacht werden,»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0199.md) `zh-wl-2026-uj__c0199` – «Zusätzlich zu den Unterhalts- und Verwaltungskosten können (bei der Staats- und direkten»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0190.md) `zh-wl-2026-uj__c0190` – «Bei solchen Liegenschaften sind stets nur die effektiven Aufwendungen abzugsfähig.»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0190.md) `zh-wl-2026-uj__c0190` – «Bei Liegenschaften im Privatvermögen können die Unterhaltskosten, die Versicherungs-»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0201.md) `zh-wl-2026-uj__c0201` – «Der Baurechtszins ist bei der direkten Bundessteuer nicht abzugsberechtigt, wenn für die»

<a id="6-abzug-liegenschaft-energie-umwelt"></a>
### Ziff. 6 – Nettoertrag aus Liegenschaften – Energiespar-/Umweltschutzinvestitionen und Rückbaukosten (im Netto-Code 188 enthalten)

- **Schlüssel:** `abzug.liegenschaft.energie_umwelt` (Investitionen Energiesparen/Umweltschutz, Rückbaukosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Rechnungen Investitionen; Beiblatt/Aufstellung; Subventionsbescheide
- **Rein:** Rechnungen Energiespar-/Umweltschutzmassnahmen → Investitionskosten (in effektiver Unterhaltsaufstellung) · Förder-/Subventionsverfügung → Beitrag (Kostenminderung oder Ziff. 5.4) · Rückbau-Abrechnung (Demontage, Abbruch, Abtransport, Entsorgung) → Rückbaukosten Ersatzneubau
- **Rechnen:** Σ Investitionen + Rückbaukosten − direkt verrechnete Förderbeiträge → effektiver Unterhalt Form. 350 → Ziff. 6; nicht verrechnete Förderbeiträge → Ziff. 5.4
- **Regel:** Den Unterhaltskosten gleichgestellt, soweit nicht subventioniert (ZStB 30.4); Rückbaukosten für Ersatzneubau abziehbar; nicht berücksichtigte Beträge können auf die zwei Folgeperioden übertragen werden. Erhaltene Förderbeiträge: Ziff. 5.4, soweit nicht direkt mit den Kosten verrechnet.
- **Beachten:** Nur bei Effektivabzug (Pauschale schliesst sie ein); nicht berücksichtigte Kosten ab 2020 → 2 Folgeperioden
- **Beachten:** Bund: Übertrag nur bei negativem Reineinkommen, dann auch dort keine Pauschale (LKV Art. 4)
- **Beachten:** Bund (LKV Art. 2): Rückbau ohne Altlasten/Aushub/Planierung; nur bei Ersatzneubau durch dieselbe Person
- **Quellen:**
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0193.md) `zh-wl-2026-uj__c0193` – «Den abzugsfähigen Unterhaltskosten gleichgestellt sind Aufwendungen für Massnahmen, wel-»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0194.md) `zh-wl-2026-uj__c0194` – «abzugsfähig sind Rückbaukosten für einen Ersatzneubau.»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0191.md) `zh-wl-2026-uj__c0191` – «Wird der Pauschalabzug beansprucht, können (mit Ausnahme der Baurechtszinsen, siehe»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0195.md) `zh-wl-2026-uj__c0195` – «nachfolgenden Steuerperioden übertragen werden, soweit diese Aufwendungen im Jahr, in»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0198.md) `zh-wl-2026-uj__c0198` – «unter Ziffer 5.4 der Steuererklärung als weitere Einkünfte zu deklarieren, soweit sie nicht direkt»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «d. der Investitionen, die dem Energiesparen und dem Umweltschutz dienen;»
  - [LKV Art. 4](../../chunks/bund/2025/bund-lkv/bund-lkv__art-4.md) `bund-lkv__art-4` – «Der Übertrag erfolgt, sofern das Reineinkommen negativ ist.»
  - [LKV Art. 4](../../chunks/bund/2025/bund-lkv/bund-lkv__art-4.md) `bund-lkv__art-4` – «Werden Kosten auf eine folgende Steuerperiode übertragen, so kann auch in dieser Steuerperiode kein Pauschalabzug geltend gemacht werden.»
  - [LKV Art. 2](../../chunks/bund/2025/bund-lkv/bund-lkv__art-2.md) `bund-lkv__art-2` – «Rückbaukosten sind nur insoweit abziehbar, als der Ersatzneubau durch dieselbe steuerpflichtige Person vorgenommen wird.»
  - [LKV Art. 2](../../chunks/bund/2025/bund-lkv/bund-lkv__art-2.md) `bund-lkv__art-2` – «Nicht abziehbar sind insbesondere die Kosten von Altlastensanierungen des Bodens»
  - [LKV Art. 1](../../chunks/bund/2025/bund-lkv/bund-lkv__art-1.md) `bund-lkv__art-1` – «so kann die steuerpflichtige Person nur die Kosten abziehen, die sie selbst trägt.»

<a id="7-berechnung-total"></a>
### Ziff. 7 – Total der Einkünfte, Übertrag auf Seite 3 Ziff. 19 (Code 199)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Summe Ziff. 1–6
- **Rein:** Übertrag der Beträge Ziff. 1–6 (S. 2, Hauptkolonne)
- **Rechnen:** Σ Ziff. 1–6 (Hauptkolonne; ohne «davon»-Ziff. 4.2 und Vorkolonnen, z.B. Monate Ziff. 5.5) → Code 199 → S. 3 Ziff. 19
- **Regel:** Rechenzeile; Staatssteuer- und Bundessteuer-Spalte getrennt führen.
- **Beachten:** Kapitalleistungen aus Vorsorge nicht hier, sondern S. 4 Ziff. 40
- **Beachten:** S. 2 einspaltig; Staat/Bund getrennt ab Ziff. 19 (qual. Beteiligungen: Abzug Ziff. 16.5, Staat 50 % / Bund 30 %)
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «7. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 19 199»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0004.md) `zh-form-300-2026-uj__c0004` – «Einkünfte im In- und Ausland CHF ohne Rappen»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0004.md) `zh-form-300-2026-uj__c0004` – «1.1 Haupterwerb Person 1 Lohnausweis»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «19. Total der Einkünfte Übertrag von Seite 2, Ziffer 7 199»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0007.md) `zh-form-300-2026-uj__c0007` – «Abzüge Staatssteuer Bundessteuer»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0100.md) `zh-wl-2026-uj__c0100` – «Nicht steuerbarer Teil der Erträge aus qualifizierten Beteiligungen bei der direkten»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «16.5 Weitere Abzüge (z.B. Beiträge an politische Parteien)»

## Abzüge

<a id="11-1-11-2-berechnung-total"></a>
### Ziff. 11.1 / 11.2 – Berufsauslagen bei unselbständiger Erwerbstätigkeit, Person 1 (Code 220) / Person 2 (Code 240)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Formular Berufsauslagen (Form. 360) Ziff. 6 Total Berufsauslagen, je Person
- **Rein:** Hilfsblatt Berufsauslagen (Form. 360) Ziff. 6 → Code 220 je Spalte Staat/Bund · Person 2: Rückseite Form. 360 → Ziff. 11.2 (Code 240) · Lohnausweis (Nettolohn, Felder F/G, Spesen) → Grundlage der Teilpositionen Ziff. 1–5
- **Rechnen:** je Person und Spalte: Ziff. 1 (Zwischentotal, plafoniert) + 2 + 3 + 4 + 5 = Ziff. 6 → Code 220 → Ziff. 11.1 (Person 2: Code 240 → Ziff. 11.2)
- **Regel:** Total des Hilfsblatts Berufsauslagen übertragen (Staats- und Bundessteuer-Spalte). Pro Person ein Hilfsblatt, vollständig und genau ausgefüllt beilegen. Pauschalen oder effektive Kosten siehe Zeilen Form. 360 Ziff. 1–5.
- **Beachten:** Vom Arbeitgeber vergütete Berufsauslagen: kein Abzug (Verfügung LS 631.33 III)
- **Beachten:** Beide Ehegatten erwerbstätig: Abzüge je Person nach Massgabe der eigenen Beschäftigung
- **Beachten:** Ziff. 2.1 und 2.2 (Verpflegung/Schicht) nicht kumulieren
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0007.md) `zh-form-300-2026-uj__c0007` – «11. Berufsauslagen bei unselbständiger Erwerbstätigkeit»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0057.md) `zh-wl-2026-uj__c0057` – «6. Total der Berufsauslagen 220»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0054.md) `zh-wl-2026-uj__c0054` – «Person 1 (Berufskosten Person 2 siehe Rückseite)»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0056.md) `zh-wl-2026-uj__c0056` – «Mehrkosten bei auswärtigem Wochenaufenthalt (gemäss Aufstellung, siehe Wegleitung)»
  - [LS 631.33 (ab 2026) S. 3–4](../../chunks/zh/2026/zh-pauschalierung-berufsauslagen-2026/zh-pauschalierung-berufsauslagen-2026__c0007.md) `zh-pauschalierung-berufsauslagen-2026__c0007` – «Soweit Berufsauslagen vom Arbeitgeber vergütet werden, steht der steuerpflichtigen Person kein Abzug zu.»
  - [LS 631.33 (ab 2026) S. 3–4](../../chunks/zh/2026/zh-pauschalierung-berufsauslagen-2026/zh-pauschalierung-berufsauslagen-2026__c0007.md) `zh-pauschalierung-berufsauslagen-2026__c0007` – «Sind beide Ehegatten erwerbstätig, werden die Abzüge für Be-»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0061.md) `zh-wl-2026-uj__c0061` – «Die vorstehenden Abzüge dürfen nicht kumuliert werden.»

<a id="12-abzug-schuldzinsen"></a>
### Ziff. 12 – Schuldzinsen (soweit nicht schon unter Ziff. 2 abgezogen) (Code 250)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen) → Schuldenverzeichnis (Form. 355) Total private Schuldzinsen (Code 3201); Zinsausweis Bank per 31.12.
- **Rein:** Zinsausweis Bank/Gläubiger → private Schuldzinsen je Schuld · Hypothekarbestätigung → Hypothekarzins · Schuldenverzeichnis (Form. 355) → Total private Schuldzinsen → Ziff. 12; Total Privatschulden (Code 3200) → Ziff. 34
- **Rechnen:** min(Σ private Schuldzinsen; Bruttoertrag bewegl. + unbewegl. Privatvermögen inkl. EMW + 50'000) → Code 250 (Kanton = Bund)
- **Regel:** Private Schuldzinsen abziehbar bis zum Bruttoertrag aus beweglichem und unbeweglichem Privatvermögen (inkl. Eigenmietwert) plus CHF 50'000. Nicht abziehbar: Amortisationen und Leasingraten (inkl. Zinsanteil). Baurechtszinsen gehören zu den Liegenschaftsunterhaltskosten (Ziff. 6), nicht hierher. Schuldzinsen aus selbständiger Erwerbstätigkeit bereits in Ziff. 2.
- **Beachten:** Amortisationen und Leasingraten (inkl. Zinsanteil) nicht abziehbar
- **Beachten:** Baurechtszinsen nicht hier, sondern beim Liegenschaftsunterhalt (Ziff. 6, ausserhalb Plafond)
- **Beachten:** Bund: nicht abziehbar sind Zinsen auf Darlehen nahestehender Kapitalgesellschaften zu nicht marktüblichen Bedingungen
- **Bund:** Gleiche Regel (Bruttoertrag plus CHF 50'000).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0007.md) `zh-form-300-2026-uj__c0007` – «12. Schuldzinsen (soweit nicht schon unter Ziff. 2 abgezogen) Schuldenverzeichnis 250»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0069.md) `zh-wl-2026-uj__c0069` – «mögen (inkl. Eigenmietwert) und weiterer CHF 50’000 nicht übersteigen.»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0068.md) `zh-wl-2026-uj__c0068` – «abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0070.md) `zh-wl-2026-uj__c0070` – «Total Privatschulden / private Schuldzinsen 3200 / 3201»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0070.md) `zh-wl-2026-uj__c0070` – «Steuererklärung Seite 4, Ziffer 34»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t1.md) `bund-dbg-2026__art-33-t1` – «Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten»

<a id="13-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 13.1 – Unterhaltsbeiträge an den geschiedenen oder getrennt lebenden Ehegatten/Partner (Code 254)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungsurteil/Konvention; Zahlungsnachweise
- **Rein:** Scheidungsurteil / Trennungsvereinbarung → Unterhalt für den Ehegatten persönlich · Bank-/Postbelege → im Steuerjahr bezahlte Beträge
- **Rechnen:** Σ im Steuerjahr bezahlte, dem Ehegatten persönlich zukommende Unterhaltsbeiträge → Code 254 (Kanton = Bund)
- **Regel:** Für den Ehegatten persönlich bestimmte Unterhaltsbeiträge voll abziehbar; Zahlungsnachweis beilegen. Spiegelbild zu Ziff. 5.1 beim Empfänger. Nicht für Leistungen in Erfüllung anderer familienrechtlicher Pflichten.
- **Beachten:** Gegenstück beim Empfänger: Ziff. 5.1 (Code 160)
- **Beachten:** Nicht abziehbar: Leistungen aus anderen familienrechtlichen Unterhalts-/Unterstützungspflichten (§ 31 StG / Art. 33 DBG)
- **Beachten:** Kinderalimente separat in Ziff. 13.2
- **Bund:** Gleiche Regel (DBG).
- **Quellen:**
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0070.md) `zh-wl-2026-uj__c0070` – «Ehegatten persönlich bestimmt sind, können voll abgezogen werden.»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0007.md) `zh-form-300-2026-uj__c0007` – «13.1 Unterhaltsbeiträge an den geschiedenen oder getrennt lebenden Ehegatten / Partn. 254»
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0051.md) `zh-wl-2026-uj__c0051` – «lebenden Ehegatten persönlich zukommen, sind von diesen als Einkommen anzugeben.»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «5.1 Unterhaltsbeiträge vom geschiedenen / getrennten Ehegatten / Partn.»
  - [StG ZH § 31](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-31-t1.md) `zh-stg-2026__par-31-t1` – «nicht jedoch Leistungen in Erfüllung anderer familienrechtlicher Unterhalts- oder Unterstützungspflichten»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t1.md) `bund-dbg-2026__art-33-t1` – «die Unterhaltsbeiträge an den geschiedenen, gerichtlich oder tatsächlich getrennt lebenden Ehegatten»

<a id="13-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 13.2 – Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit) (Code 255)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Urteil/Konvention; Zahlungsnachweise
- **Rein:** Urteil / Unterhaltsvertrag → Kinderunterhalt (Betrag, Dauer) · Zahlungsbelege → bezahlte Monatsbeträge · Geburtsdatum Kind → Monat des 18. Geburtstags
- **Rechnen:** Σ bezahlte Kinderalimente bis und mit Monat des 18. Geburtstags → Code 255 (Kanton = Bund)
- **Regel:** Kinderalimente abziehbar bis und mit dem Monat, in dem das Kind 18 wird. Danach kein Alimentenabzug – stattdessen steht dem Zahlenden der Kinderabzug zu (Ziff. 24.1). Wer Alimente abzieht, hat keinen (ganzen/halben) Kinderabzug für dasselbe Kind (siehe Ziff. 24.1).
- **Beachten:** Wer Alimente für ein Kind abzieht, hat für dieses Kind keinen (auch keinen halben) Kinderabzug
- **Beachten:** Volljähriges Kind in Erstausbildung: kein Alimentenabzug, aber Kinderabzug bei Unterhalt zur Hauptsache
- **Beachten:** Empfänger: Ziff. 5.2 (inkl. Alimentenbevorschussung)
- **Quellen:**
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0070.md) `zh-wl-2026-uj__c0070` – «Für Kinder bestimmte Unterhaltsbeiträge (Alimente) können bis und mit dem Monat abgezogen werden, in dem das Kind das 18. Altersjahr erreicht.»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0007.md) `zh-form-300-2026-uj__c0007` – «13.2 Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit) 255»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0127.md) `zh-wl-2026-uj__c0127` – «leisten Sie Unterhaltszahlungen für das Kind, so können Sie keinen Kinderabzug geltend machen;»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0127.md) `zh-wl-2026-uj__c0127` – «Sie keine an den anderen Elternteil geleistete»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0127.md) `zh-wl-2026-uj__c0127` – «können Sie den Kinderabzug geltend machen, wenn Sie Unterhaltsbeiträge leisten»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «5.2 Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit)»
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0051.md) `zh-wl-2026-uj__c0051` – «Den Alimenten gleichgestellt sind Alimentenbevorschussungen.»

<a id="13-3-abzug-uebrige"></a>
### Ziff. 13.3 – Rentenleistungen – abzugsfähig: Ertragsanteil (Code 256, Vorkolonne 2561)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ⚠️ strittig
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise/Vertrag; erstmals Kopie Leibrenten-/Verpfründungsvertrag
- **Rein:** Leibrenten-/Verpfründungsvertrag (bei erstmaliger Deklaration Kopie) → Rentenhöhe · Zahlungsnachweise → Σ bezahlte Leibrenten/Verpfründungen (Vorkolonne 2561) · Naturalleistungen (Verpflegung, Unterkunft) → Art und Wert belegen · ESTV-Berechnungssatz der Steuerperiode (estv.admin.ch) → %
- **Rechnen:** WL: 2561 × ESTV-Berechnungssatz (%) → Code 256 (Bund: Ertragsanteil Art. 22 Abs. 3 lit. c DBG); § 31 StG: 40 % × 2561 (strittig)
- **Regel:** Abzugsfähig laut Wegleitung der Ertragsanteil der bezahlten Leibrenten/Verpfründungen (ESTV-Berechnungssatz). Zahlungsnachweise und bei erstmaliger Deklaration Vertragskopie beilegen.
- **Beachten:** strittig: WL (ESTV-Satz) vs. § 31 Abs. 1 lit. b StG (40 % der bezahlten Leibrenten) → Fachperson entscheidet
- **Beachten:** Bund-Satz: Rendite zehnjähriger Bundesobligationen + 0,5 Prozentpunkte (Steuerjahr und neun Vorjahre)
- **Bemerkung:** Gesetz (§ 31 Abs. 1 lit. b StG, Stand 2026): 40 Prozent der bezahlten Leibrenten; Wegleitung: Ertragsanteil nach jährlichem ESTV-Satz. Je nach Satz weichen die Werte ab; Gesetz geht vor, Fachperson entscheidet.
- **Quellen:**
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0071.md) `zh-wl-2026-uj__c0071` – «Abzugsfähig ist der Ertragsanteil der bezahlten Leibrenten und Verpfründungen.»
  - [StG ZH § 31](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-31-t1.md) `zh-stg-2026__par-31-t1` – «die dauernden Lasten sowie 40 Prozent der bezahlten Leibrenten»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t1.md) `bund-dbg-2026__art-33-t1` – «die dauernden Lasten sowie der Ertragsanteil nach Artikel 22 Absatz 3 Buchstabe c»
  - [DBG Art. 22](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-22-t3.md) `bund-dbg-2026__art-22-t3` – «um 0,5 Prozentpunkte erhöhten annualisierten Rendite zehnjähriger Bundesobligationen»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0073.md) `zh-wl-2026-uj__c0073` – «Berechnungsformel: Bezahlte Leibrente / Verpfründung x Berechnungssatz (in %)»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0074.md) `zh-wl-2026-uj__c0074` – «über Art und Wert von ausgerichteten Naturalleistungen (z.B. Verpflegung, Unterkunft) zu»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0074.md) `zh-wl-2026-uj__c0074` – «Bei erstmaliger Deklaration bitten wir Sie zudem, eine Kopie des Leibrenten- bzw.»

<a id="14-1-14-2-abzug-vorsorge-saeule3a"></a>
### Ziff. 14.1 / 14.2 – Beiträge Säule 3a – ordentliche Beiträge, Person 1 (Code 260, effektiv 262) / Person 2 (Code 261, effektiv 263)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → 3a-Bescheinigung der Bank-/Versicherungsstiftung (im Steuerjahr 2026 einbezahlter Betrag)
- **Rein:** 3a-Bescheinigung Bank-/Versicherungsstiftung → im Steuerjahr einbezahlter Betrag (eff. Code 262/263) · Vorsorgeausweis / Lohnausweis → Zugehörigkeit 2. Säule ja/nein · ohne 2. Säule: Erwerbseinkommen → Basis 20 %
- **Rechnen:** je Person min(einbezahlt; mit 2. Säule 7'258 | ohne 2. Säule min(20 % × Erwerbseinkommen; 36'288)) → Code 260/261 (Kanton = Bund)
- **Regel:** Nur im Jahr 2026 tatsächlich bezahlte Beiträge abziehbar, Bescheinigung beilegen. Maximum mit 2. Säule CHF 7'258; ohne 2. Säule 20% des Erwerbseinkommens, max. CHF 36'288. Beide Ehegatten können je für sich abziehen, wenn beide erwerbstätig sind und je einen Vorsorgevertrag haben. Mitarbeit im Betrieb des Ehegatten: nur bei echtem Arbeitsverhältnis mit AHV-Abrechnung. 3a-Guthaben nicht im Wertschriftenverzeichnis/Vermögen aufführen.
- **Beachten:** Nur im Steuerjahr tatsächlich bezahlte Beiträge; Bescheinigung beilegen
- **Beachten:** Mitarbeit im Betrieb des Ehegatten: nur bei echtem, AHV-abgerechnetem Arbeitsverhältnis
- **Beachten:** Einkauf für Beitragslücken separat in Ziff. 14.3
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a mit Zugehörigkeit zur 2. Säule: höchstens Fr. 7'258 (Bemessungsjahr ab 2025).)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug CHF 7'258 pro Jahr für Personen, die einer Vorsorgeeinrichtung der 2. Säule angehören (8 % des oberen Grenzbetrags nach Art. 8 Abs. 1 BVG). Nur im Steuerjahr tatsächlich einbezahlte Beiträge, mit Bescheinigung.)**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a ohne Zugehörigkeit zur 2. Säule: höchstens 20 % des Erwerbseinkommens, maximal Fr. 36'288.)** · Bund **CHF 36'288 (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens CHF 36'288 pro Jahr.)**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. Fr. 36'288).)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (alle Einkünfte aus selbständiger und unselbständiger, haupt- und nebenberuflicher Erwerbstätigkeit), max. CHF 36'288.)**
- **Bund:** Gleiche Höchstbeträge (CHF 7'258 / 20%, max. CHF 36'288) gemäss Formular (Spalte Bund).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «14.1 Person 1 13211 eff. CHF 262 260»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0075.md) `zh-wl-2026-uj__c0075` – «die einer Einrichtung der beruflichen Vorsorge (2. Säule) angehören, höchstens CHF 7’258;»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0076.md) `zh-wl-2026-uj__c0076` – «Es dürfen nur die tatsächlich im Jahr 2026 bezahlten Prämien/Beiträge oder Einlagen ab-»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0076.md) `zh-wl-2026-uj__c0076` – «ein eigentliches Arbeitsverhältnis besteht und demzufolge die Beiträge an die AHV, IV usw.»

<a id="14-3-abzug-vorsorge-saeule3a-einkauf"></a>
### Ziff. 14.3 – Einkauf Säule 3a (neu ab 2026), Person 1 (Code 276) / Person 2 (Code 278), Hauptkolonne Code 264

- **Schlüssel:** `abzug.vorsorge.saeule3a_einkauf` (Einkauf (Nachzahlung) Säule 3a – ab Steuerjahr 2026) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Einkaufsbescheinigung der 3a-Einrichtung (Einkaufsbetrag, Beitragslücken); Nachweis AHV-Beitragsjahre
- **Rein:** Einkaufsbescheinigung 3a-Einrichtung → Einkaufsbetrag je Person (Code 276/278) · 3a-Bescheinigung ordentlicher Beitrag → Nachweis voller Maximalbeitrag im Einkaufsjahr · Nachweis AHV/IV/EO-Beiträge im Lückenjahr
- **Rechnen:** je Person min(Einkauf; Σ Beitragslücken ab 1.1.2025 innert zehn Jahren; 7'258) → Code 276/278; Σ → Code 264 (Kanton = Bund)
- **Regel:** Neu ab Steuerperiode 2026: zusätzlich zu den ordentlichen Beiträgen Einkauf für Beitragslücken, die ab 1.1.2025 entstanden sind. Voraussetzungen: in den Lücken-Jahren AHV/IV/EO-Beiträge geleistet (3a-berechtigt) und im Einkaufsjahr den maximal zulässigen ordentlichen Beitrag (CHF 7'258 bzw. 20%, max. CHF 36'288) vollständig einbezahlt. Einkauf höchstens Summe der Beitragslücken der letzten 10 Jahre (frühestens ab 1.1.2025), maximal CHF 7'258.
- **Beachten:** Voraussetzung: ordentlicher Maximalbeitrag Ziff. 14.1/14.2 im Einkaufsjahr voll einbezahlt
- **Beachten:** Steuerjahr 2026: faktisch nur Lücke 2025 einkaufbar (Lücken frühestens ab 1.1.2025)
- **Limiten:**
  - Säule 3a – Einkauf (Nachzahlung) Regel/Maximum: Kanton **CHF 7'258 (Neu ab Steuerperiode 2026: Einkauf in die Säule 3a für Beitragslücken, die ab 1.1.2025 entstanden sind (innerhalb der zehn Jahre vor dem Einkauf). Voraussetzungen: AHV/IV/EO-Beiträge in den Lückenjahren und im Einkaufsjahr voller ordentlicher Maximalbeitrag einbezahlt. Einkauf höchstens Summe der Lücken, in jedem Fall maximal Fr. 7'258.)** · Bund **CHF 7'258 (Einkauf Säule 3a (ab Steuerperiode 2026, für Beitragslücken ab 1.1.2025): zusätzlich zum vollen ordentlichen Beitrag im Einkaufsjahr; max. Summe der Beitragslücken der letzten 10 Jahre (frühestens ab 2025), pro Steuerjahr höchstens CHF 7'258 (8 % des oberen BVG-Grenzbetrags, unabhängig von Zugehörigkeit zur 2. Säule); eine Jahresbeitragslücke nur durch einen einzigen Einkauf ausgleichbar; kein Einkauf nach Bezug einer Altersleistung der Säule 3a (Bezüge ab 5 Jahren vor Referenzalter zählen als Altersleistung).)**
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «14.3 Einkauf Person 1 276 3211 Person 2 278 3211 264»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0077.md) `zh-wl-2026-uj__c0077` – «in jedem Fall aber maximal CHF 7’258.»
  - [WL ZH 2026 UJ S. 8](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0020.md) `zh-wl-2026-uj__c0020` – «auch Einkäufe getätigt werden für Beitragslücken, die ab dem 1.1.2025 entstanden sind»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0077.md) `zh-wl-2026-uj__c0077` – «im Einkaufsjahr den für sie maximal zulässigen ordentlichen Beitrag (CHF 7’258 bzw. höchs-»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0077.md) `zh-wl-2026-uj__c0077` – «geleistet hat und sie damit zur Leistung von Säule 3a-Beiträgen berechtigt war, und»

<a id="15-abzug-versicherungspraemien"></a>
### Ziff. 15 – Versicherungsprämien, Zinsen von Sparkapitalien (Code 270)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Prämienrechnung/-bescheinigung Krankenkasse (abzüglich Prämienverbilligung), Police Lebens-/Unfallversicherung, Sparzinsen aus Wertschriftenverzeichnis
- **Rein:** Formular Versicherungsprämien (Form. 365) Teil C → Code 270 je Spalte · Form. 365 Teil A (Code 606) → bezahlte Prämien und Sparzinsen netto nach Prämienverbilligung · Seite 1 Kinder / unterstützte Personen → Anzahl Zuschläge in Teil B
- **Rechnen:** min(A Code 606; B) → Code 270 je Spalte; B = Verh. Kanton 5'800 (8'700) / Bund 3'700 (5'550) | übrige 2'900 (4'350) / 1'800 (2'700) + je Kind 1'300 / 700
- **Regel:** Betrag aus dem Formular Versicherungsprämien (Form. 365) Teil C übertragen: der niedrigere der Beträge A (bezahlte Prämien und Sparzinsen, netto nach Prämienverbilligung) und B (Maximalabzug). Maximalabzug Staatssteuer: Verheiratete CHF 5'800 (ohne Beiträge 2. Säule/3a: CHF 8'700), übrige CHF 2'900 (ohne Vorsorgebeiträge: CHF 4'350), zusätzlich pro Kind/unterstützungsbedürftige Person CHF 1'300 (halber Kinderabzug: CHF 650).
- **Beachten:** Klammerwerte nur, wenn weder Steuerpflichtige noch Arbeitgeber Beiträge an 2. Säule oder 3a geleistet haben
- **Beachten:** Halber Kinderabzug: Zuschlag Kanton 650 / Bund 350; unterstützte Person: Kanton 1'300 / Bund 700
- **Beachten:** Verheirateten-Ansatz nur bei rechtlich und tatsächlich ungetrennter Ehe
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'800 (Versicherungsprämien und Sparzinsen (Staatssteuer), in ungetrennter Ehe lebende Steuerpflichtige mit Beiträgen an 2. Säule/Säule 3a: Fr. 5'800.)** · Bund **CHF 3'700 (Versicherungsprämien und Zinsen von Sparkapitalien, Ehepaare in ungetrennter Ehe, mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 3'700.)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 8'700 (Gemeinsam Besteuerte ohne Beiträge an 2. Säule und Säule 3a (weder durch Steuerpflichtige noch Arbeitgeber): Abzug erhöht sich um die Hälfte, höchstens Fr. 8'700.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an 2. Säule und Säule 3a: Höchstabzug CHF 5'550 (Erhöhung um die Hälfte).)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'900 (Versicherungsprämien und Sparzinsen (Staatssteuer), übrige Steuerpflichtige (nicht in ungetrennter Ehe) mit Vorsorgebeiträgen: Fr. 2'900.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 1'800.)**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 4'350 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: Abzug erhöht sich um die Hälfte, höchstens Fr. 4'350.)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: max. CHF 2'700.)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'300 (Zuschlag zum Versicherungsabzug: Fr. 1'300 für jedes Kind oder jede unterstützungsbedürftige Person mit Kinder-/Unterstützungsabzug nach § 34 Abs. 1; bei hälftig aufgeteiltem Kinderabzug Fr. 650.)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**
- **Bund:** Maximalabzug Bund: Verheiratete CHF 3'700 (ohne Vorsorgebeiträge CHF 5'550), übrige CHF 1'800 (ohne Vorsorgebeiträge CHF 2'700), pro Kind/unterstützungsbedürftige Person CHF 700 (halbes Kind: CHF 350).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «15. Versicherungsprämien, Zinsen von Sparkapitalien Versicherungsprämien 270»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0081.md) `zh-wl-2026-uj__c0081` – «CHF 5’800 für verheiratete Personen in rechtlich und tatsächlich ungetrennter Ehe.»
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0084.md) `zh-wl-2026-uj__c0084` – «CHF 2’900 für alle übrigen Steuerpflichtigen.»
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0082.md) `zh-wl-2026-uj__c0082` – «CHF 3’700 für verheiratete Personen in rechtlich und tatsächlich ungetrennter Ehe.»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0079.md) `zh-wl-2026-uj__c0079` – «Total bezahlte Versicherungsprämien und Zinsen von Sparkapitalien (A)»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0080.md) `zh-wl-2026-uj__c0080` – «Total der Abzüge für Versicherungsprämien und Zinsen von Sparkapitalien»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0081.md) `zh-wl-2026-uj__c0081` – «StA Form. 365 (2024) 12.26»
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0087.md) `zh-wl-2026-uj__c0087` – «CHF 350 für jedes Kind, für das der steuerpflichtigen Person ein halber Kinderabzug zusteht.»
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0087.md) `zh-wl-2026-uj__c0087` – «CHF 700 für jedes Kind oder jede unterstützungsbedürftige Person, für die der steuer-»

<a id="16-1-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 16.1 – Beiträge an die AHV, IV und 2. Säule, sofern nicht unter Ziff. 1 und 2 abgezogen (Code 280)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) für selbst einbezahlte Einkäufe; NICHT Lohnausweis Ziff. 10.2
- **Rein:** Bescheinigung Vorsorgeeinrichtung (Formular 21 EDP) → selbst einbezahlte, nicht vom Lohn abgezogene Einkäufe · Bescheinigung Pensionskasse → übrige Beiträge 2. Säule, soweit nicht im Lohnausweis · Lohnausweis Ziff. 10.1/10.2 → nur Kontrolle (bereits im Nettolohn Ziff. 11)
- **Rechnen:** Σ beider Personen: Beiträge/Einkäufe 2. Säule gem. Bescheinigung VE, soweit nicht in LA Ziff. 10 (Nettolohn 11 = 8 − 9 − 10) → Code 280
- **Regel:** Nur Beiträge/Einkäufe eintragen, die nicht schon im Lohnausweis vom Lohn abgezogen sind. Lohnausweis Ziff. 10.2 (Einkauf, im Bruttolohn abgezogen) ist im Nettolohn Ziff. 11 bereits berücksichtigt – nicht nochmals abziehen. Selbst entrichtete (nicht vom Lohn abgezogene) Einkäufe bescheinigt die Vorsorgeeinrichtung separat mit Formular 21 EDP; Bescheinigung beilegen. Einkäufe sind nicht abziehbar, wenn innerhalb von drei Jahren ein Kapitalbezug erfolgt (Sperrfrist). Bei Zweiverdienerabzug sind Einkäufe in die 2. Säule vom Erwerbseinkommen abzuziehen (Ziff. 17).
- **Beachten:** Lohnausweis Ziff. 10.1/10.2 nicht nochmals abziehen – im Nettolohn Ziff. 11 schon gekürzt
- **Beachten:** Kein Abzug, soweit innert drei Jahren Kapitalbezug folgt; WEF-Vorbezug gilt als Kapitalbezug
- **Beachten:** Freiwillige Einkäufe erst nach Rückzahlung früherer WEF-Vorbezüge zulässig
- **Quellen:**
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0088.md) `zh-wl-2026-uj__c0088` – «Einkäufe steuerlich nicht zum Abzug zugelassen werden, soweit innerhalb von drei Jahren ein Kapitalbezug erfolgt.»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «die berufliche Vorsorge, sind nicht durch den Arbeitgeber im Lohnausweis, sondern durch die Vorsorgeeinrichtung separat mit dem Formular 21 EDP zu bescheinigen.»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «Beiträge für den Einkauf von fehlenden Versicherungsjahren oder von fehlendem Spar-»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «16.1 Beiträge an die AHV, IV und 2. Säule, sofern nicht unter Ziff. 1 und 2 abgezogen 280»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «vom Bruttolohn total (Ziffer 8) das Total der Abzüge (Ziffer 9 und 10) abgezogen wird»
  - [KS 17 S. 6](../../chunks/bund/dauernd/bund-ks-17/bund-ks-17__c0012.md) `bund-ks-17__c0012` – «Um einen Kapitalbezug handelt es sich auch bei einem Vorbezug für das Wohneigentum.»
  - [KS 17 S. 6](../../chunks/bund/dauernd/bund-ks-17/bund-ks-17__c0012.md) `bund-ks-17__c0012` – «dürfen freiwillige Einkäufe in die berufliche Vorsorge erst wieder vorgenommen werden, wenn allfällig früher getätigte Vorbezüge»

<a id="16-1-abzug-ahv-nichterwerbstaetige"></a>
### Ziff. 16.1 – AHV/IV-Beiträge, soweit nicht im Lohnausweis gekürzt (z.B. Nichterwerbstätige) (Code 280)

- **Schlüssel:** `abzug.ahv_nichterwerbstaetige` (AHV/IV/EO-Beiträge Nichterwerbstätiger u.ä.) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse) → Beitragsverfügung/Bescheinigung der AHV-Ausgleichskasse
- **Rein:** Beitragsverfügung/Bescheinigung AHV-Ausgleichskasse → bezahlte AHV/IV/EO-Beiträge (Nichterwerbstätige) · Lohnausweis Ziff. 9 → nur Kontrolle (AN-Beiträge AHV/IV/EO/ALV/NBUV bereits im Nettolohn)
- **Rechnen:** Σ AHV/IV-Beiträge gem. Bescheinigung, soweit Einkünfte Ziff. 1–2 nicht bereits darum gekürzt → Code 280 (zusammen mit 2. Säule)
- **Regel:** Beiträge an AHV und IV abziehbar, soweit die unter Ziff. 1 und 2 deklarierten Einkünfte nicht bereits um diese Beiträge gekürzt sind (Lohnausweis Ziff. 9 ist im Nettolohn bereits abgezogen). Bescheinigung beilegen.
- **Beachten:** Lohnausweis Ziff. 9 ist im Nettolohn Ziff. 11 bereits abgezogen – nicht nochmals
- **Beachten:** Bund: Arbeitgeberbeiträge für privates Dienstpersonal nicht abziehbar
- **Beachten:** Bescheinigung beilegen (soweit Beiträge nicht im Lohnausweis enthalten)
- **Quellen:**
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0088.md) `zh-wl-2026-uj__c0088` – «• Beiträge an die AHV und IV, soweit die unter Ziffern 1 und 2 der Steuererklärung deklarierten»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «16.1 Beiträge an die AHV, IV und 2. Säule, sofern nicht unter Ziff. 1 und 2 abgezogen 280»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «vom Bruttolohn total (Ziffer 8) das Total der Abzüge (Ziffer 9 und 10) abgezogen wird»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0055.md) `bund-wl-2a-2026__c0055` – «Nicht zulässig ist der Abzug von Arbeitgeberbeiträgen für das»
  - [WL ZH 2026 UJ S. 31](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0219.md) `zh-wl-2026-uj__c0219` – «Bescheinigung über Beiträge an AHV/IV oder an Pensionskassen (soweit nicht im Lohnaus-»
  - [WL Lohnausweis 2026 S. 14](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0034.md) `bund-wl-lohnausweis-2026__c0034` – «Arbeitnehmeranteil für AHV/IV/EO/ALV/NBUV betragsmässig anzugeben»

<a id="16-2-abzug-weiterbildung"></a>
### Ziff. 16.2 – Berufsorientierte Aus- und Weiterbildungskosten (Code 292)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Kursrechnungen/Zahlungsnachweise; Lohnausweis Ziff. 13.3 (Beiträge des Arbeitgebers); Formular Aus- und Weiterbildungskosten (Form. 367)
- **Rein:** Kursrechnungen/Zahlungsbelege → Total Kosten (Form. 367 Code 2900/2903) · Lohnausweis Ziff. 13.3 → Vergütungen Arbeitgeber (Code 2901/2904) · Bestätigung Bund/Branchenverband → Beiträge Dritter (Code 2901/2904) · Form. 367 → zulässiger Abzug 2920/2921 → Code 292
- **Rechnen:** je Person min(Kosten − Beiträge Dritter; Kanton 12'600 / Bund 13'000); Code 292 = 2920 + 2921
- **Regel:** Selbst getragene Kosten (nach Abzug von Beiträgen Dritter: Arbeitgeber, Bund, Branchenverbände) bis zum Maximalbetrag; Voraussetzung: Abschluss Sekundarstufe II oder 20. Altersjahr vollendet und nicht Ausbildungskosten bis zum ersten Abschluss Sek. II. Zeitpunkt = Fälligkeit/Zahlung, nicht Kursbesuch. Lohnausweis Ziff. 13.3: vom Arbeitgeber dem Arbeitnehmer vergütete Weiterbildungskosten (nicht direkt an Dritte bezahlte) sind in Form. 367 als Beitrag Dritter in Abzug zu bringen; bei Rechnungen auf den Namen des Arbeitnehmers immer bescheinigt. Vollständig ausgefülltes Formular beilegen.
- **Beachten:** Nur bei Abschluss Sek. II oder vollendetem 20. Lebensjahr; nicht Ausbildung bis zum ersten Sek.-II-Abschluss
- **Beachten:** Massgebend ist Fälligkeit bzw. Zahlung, nicht Kursbesuch
- **Beachten:** Vom Arbeitgeber direkt ans Bildungsinstitut bezahlte Kosten: nicht im LA 13.3 – nur selbst getragene Kosten abziehen
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 12'600 (Berufsorientierte Aus- und Weiterbildungskosten inkl. Umschulung: bis Fr. 12'600 (Staatssteuer), sofern erster Abschluss Sekundarstufe II vorliegt oder das 20. Lebensjahr vollendet ist (und es nicht um Kosten bis zum ersten Abschluss Sek. II geht).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildungs- inkl. Umschulungskosten bis CHF 13'000 pro Jahr, sofern erster Abschluss Sek. II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)**
- **Bund:** Höchstbetrag CHF 13'000 (statt CHF 12'600).
- **Quellen:**
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0089.md) `zh-wl-2026-uj__c0089` – «betrag von CHF 12’600 bei der Staatssteuer bzw. CHF 13’000 bei der Bundessteuer, sofern ein»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «die dem Arbeitnehmer vergütet werden. Nicht anzugeben sind Vergütungen, die direkt an Dritte (z. B. Bildungsinstitut) bezahlt werden.»
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0090.md) `zh-wl-2026-uj__c0090` – «Zulässiger Abzug (max. je CHF 12’600) 2920 / 2921»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «16.2 Berufsorientierte Aus- und Weiterbildungskosten Hilfsblatt 292»

<a id="16-3-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. 16.3 – Kosten für die Verwaltung des beweglichen Privatvermögens (Code 283)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Depotgebühren-Ausweis der Bank / Verwaltungsabrechnung (Verwahrung und Verwaltung durch Dritte)
- **Rein:** Bank-/Verwaltungsabrechnung, Depotgebühren-Ausweis → effektive Verwaltungs-/Verwahrungskosten · Steuerauszug/Dividendenabrechnung → nicht rückforderbare, nicht anrechenbare ausländische Quellensteuern
- **Rechnen:** Pauschal min(3‰ × Steuerwert drittverwaltete Wertschriften; 6'000) oder effektiv (voll nachweisen) + nicht rückforderbare ausl. QSt → Code 283
- **Regel:** Abziehbar sind Kosten der Verwaltung und Verwahrung durch Dritte sowie nicht rückforderbare/anrechenbare ausländische Quellensteuern; nicht abziehbar Erwerbs-/Veräusserungskosten und Aufwendungen für Anschaffung/Wertvermehrung. Bei Verwaltung durch Dritte pauschal 3 Promille des Steuerwerts der verwalteten Wertschriften, maximal CHF 6'000, oder effektiv (Bezahlung und Abzugsfähigkeit voll nachweisen).
- **Beachten:** Wertschriften im Depot einer Bank gelten als durch Dritte verwahrt/verwaltet – ein Vermögensverwaltungsmandat ist nicht Voraussetzung der Pauschale
- **Beachten:** Basis Pauschale: nur Wertschriften im Depot (durch Dritte verwahrt/verwaltet) – ohne Darlehen und Bankguthaben aller Art (ZStB 30.1); Pauschale oder effektiv, nicht beides
- **Beachten:** Nicht abziehbar: Kosten für Erwerb/Veräusserung von Wertschriften, Anschaffung/Wertvermehrung
- **Beachten:** Details: Weisung ZStB 30.1 (Kosten Verwaltung Wertschriften Privatvermögen)
- **Beachten:** Bund: Depot- und Safegebühren inkl. Inkasso-/Affidavitspesen; keine Entschädigung für eigene Bemühungen
- **Bund:** Belegt sind nur effektive Verwahrungskosten (Depot-, Safegebühren, Inkassospesen; bund-wl-2a-2026__c0060); eine Bundes-Pauschale ist im Wiki nicht belegt → Bundesspalte effektiv (ohne Gebührenausweis 0) oder Kantonspauschale nur mit Vorbehalt (Fachperson).
- **Quellen:**
  - [WL ZH 2026 UJ S. 15–16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0091.md) `zh-wl-2026-uj__c0091` – «können 3‰ des Steuerwerts dieser durch Dritte verwalteten Wertschriften, maximal»
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0090.md) `zh-wl-2026-uj__c0090` – «Bei beweglichem Privatvermögen können die Kosten der Verwaltung durch Dritte und die weder»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0097.md) `zh-wl-2026-uj__c0097` – «16.3 Kosten für die Verwaltung des beweglichen Privatvermögens 283»
  - [WL ZH 2026 UJ S. 15–16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0091.md) `zh-wl-2026-uj__c0091` – «die Kosten für den Erwerb und die Veräusserung von Wertschriften.»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0092.md) `zh-wl-2026-uj__c0092` – «Weisung finden Sie im Zürcher Steuerbuch Nr. 30.1»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0060.md) `bund-wl-2a-2026__c0060` – «Nicht zulässig ist die Anrechnung einer Entschädigung für ei-»
  - [ZStB 30.1](../../chunks/zh/dauernd/zh-zstb-30-1/zh-zstb-30-1__c0006.md) `zh-zstb-30-1__c0006` – «(ohne Darlehen und Bankguthaben aller Art)»
  - [ZStB 30.1](../../chunks/zh/dauernd/zh-zstb-30-1/zh-zstb-30-1__c0005.md) `zh-zstb-30-1__c0005` – «Eine Kumulation von Pauschalabzug und tatsächlichen Kosten ist innerhalb einer Steuerperiode ausgeschlossen.»

<a id="16-4-abzug-behinderungskosten"></a>
### Ziff. 16.4 – Behinderungsbedingte Kosten (Code 3160)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Aufstellung über behinderungsbedingte Kosten (Codes 3100–3103, 3120, 3130–3133, 3150, 3155); Rechnungen
- **Rein:** Leistungsabrechnung Krankenkasse/Versicherung → 3130; Verfügung Hilflosenentschädigung → 3131 · Heim-/Pensionsrechnung → Anteil Lebenshaltungskosten 3132 (Total B 3150) · Alternativ Pauschale D (Code 3103) gemäss Merkblatt ZStB 32.1 → Ziff. 16.4 Code 3160
- **Rechnen:** 3160 = 3155 (A 3120 − B 3150, kein Selbstbehalt) oder Pauschale 3103: HE leicht 2'500 / mittel 5'000 / schwer 7'500; Gehörlose, Dialyse 2'500
- **Regel:** Formular «Aufstellung über behinderungsbedingte Kosten» (Gemeindesteueramt / zh.ch) ausfüllen: A effektive Aufwendungen, B Vergütungen Dritter (Krankenkasse, Hilflosenentschädigung, Anteil Lebenshaltungskosten), C = A – B (Code 3155) oder D Pauschale gemäss Merkblatt ZStB 32.1; Übertrag in Ziff. 16.4. Nur selbst getragene Kosten; nicht gleichzeitig unter Ziff. 22.1.
- **Beachten:** Kein Selbstbehalt (anders als Krankheitskosten Ziff. 22.1); Pauschalen Kanton = Bund
- **Beachten:** Heim: Pension + Pflege kürzen um Lebenshaltung (ZH: 2'000 pro Monat), KVG-Pflegetaxen und HE
- **Beachten:** Behinderung u.a. bei HE-/IV-Bezügern, Heim/Spitex ab 60 Minuten Pflege/Betreuung täglich
- **Quellen:**
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0093.md) `zh-wl-2026-uj__c0093` – «Wenn Sie einen solchen Abzug beanspruchen, füllen Sie das Formular «Aufstellung über»
  - [StG ZH § 31](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-31-t3.md) `zh-stg-2026__par-31-t3` – «soweit der Steuerpflichtige die Kosten selber trägt»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0016.md) `zh-zstb-32-1__c0016` – «Bezüger einer Hilflosenentschädigung schweren Grades: Fr. 7’500.-»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0016.md) `zh-zstb-32-1__c0016` – «Nierenkranke, die sich einer Dialyse unterziehen müssen.»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0094.md) `zh-wl-2026-uj__c0094` – «rungsbedingten Kosten, Ziffer 3. 3103»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0004.md) `zh-zstb-32-1__c0004` – «Für den Abzug der behinderungsbedingten Kosten besteht kein solcher Selbstbehalt.»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0015.md) `zh-zstb-32-1__c0015` – «Im Kanton Zürich sind dafür monatlich Fr. 2'000.- abzuziehen»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0011.md) `zh-zstb-32-1__c0011` – «bei denen ein täglicher Pflege- und Betreuungsaufwand von 60 Minuten und mehr anfällt.»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «16.4 Behinderungsbedingte Kosten Hilfsblatt 3160»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0017.md) `zh-zstb-32-1__c0017` – «In der Steuererklärung sind die behinderungsbedingten Kosten in Ziffer 16.4 und die Krankheits- und Unfallkosten in Ziffer 22.1 einzutragen.»
  - [KS 11 S. 10](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0025.md) `bund-ks-11__c0025` – «einen jährlichen Pauschalabzug in folgender Höhe geltend machen:»
  - [KS 11 S. 8](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0017.md) `bund-ks-11__c0017` – «oder nach entsprechenden kantonalen Richtlinien»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0014.md) `zh-zstb-32-1__c0014` – «Bei der Berechnung der abzugsfähigen Kosten ist von den gesamten Kosten für Pension (Unterkunft und Verpflegung) und Pflege auszugehen.»

<a id="16-5-parteien-abzug-parteispenden"></a>
### Ziff. 16.5 (Parteien) – Weitere Abzüge – Mitgliederbeiträge und Zuwendungen an politische Parteien (Code 284)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Spendenbestätigung/Beitragsquittung der Partei; Aufstellung
- **Rein:** Spendenbestätigung/Beitragsquittung der Partei → bezahlte Mitgliederbeiträge und Zuwendungen · Aufstellung (Partei, Betrag) → Code 284
- **Rechnen:** Kanton min(Σ; 21'000 verheiratet / 10'500 übrige); Bund min(Σ; 10'600) für alle → Code 284
- **Regel:** Nur Parteien, die im Parteienregister eingetragen, in einem kantonalen Parlament vertreten sind oder bei den letzten Wahlen mind. 3% Wähleranteil erreicht haben. Staatssteuer max. CHF 21'000 für in ungetrennter Ehe Lebende, CHF 10'500 für übrige; Bundessteuer max. CHF 10'600 (gilt für Ehepaare wie Übrige).
- **Beachten:** Nur Parteien im Parteienregister, in einem kant. Parlament vertreten oder mit mind. 3% Stimmen (letzte kant. Wahl)
- **Beachten:** Code 284 sammelt alle «Weiteren Abzüge» (Parteien, Teilbesteuerung, Geldspiel usw.) – Aufstellung beilegen
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'500 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister, Vertretung im kantonalen Parlament oder mind. 3 % Wähleranteil): bis Fr. 10'500 für die übrigen Steuerpflichtigen.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister / kantonales Parlament / mind. 3 % Stimmen): bis Gesamtbetrag CHF 10'600.)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 21'000 (Parteispenden gemeinsam Besteuerte (in ungetrennter Ehe): bis Fr. 21'000.)** · Bund **–**
- **Bund:** Höchstbetrag CHF 10'600 (für Verheiratete und Übrige gleich).
- **Quellen:**
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0097.md) `zh-wl-2026-uj__c0097` – «Höchstbetrag von CHF 21’000 für in ungetrennter Ehe lebende Steuerpflichtige und von»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0098.md) `zh-wl-2026-uj__c0098` – «Der Höchstbetrag für solche Abzüge beträgt CHF 10’600.»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0096.md) `zh-wl-2026-uj__c0096` – «wahlen mindestens 3% der Stimmen erreicht haben.»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «16.5 Weitere Abzüge (z.B. Beiträge an politische Parteien) Aufstellung 284»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0095.md) `zh-wl-2026-uj__c0095` – «Parteienregister nach Artikel 76a des Bundesgesetzes über die politischen Rechte eingetragen,»

<a id="16-5-teilbesteuerung-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 16.5 (Teilbesteuerung) – Weitere Abzüge – Teilbesteuerungsabzug qualifizierte Beteiligungen (Code 284, Aufstellung)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Formular «Qualifizierte Beteiligungen im Privatvermögen» bzw. «…im Geschäftsvermögen»
- **Rein:** Wertschriftenverzeichnis (Code «Q», Bruttobetrag) → Erträge qual. Beteiligungen (Ziff. 4.2 Code 151) · Formular «Qualifizierte Beteiligungen im Privatvermögen» → nicht steuerbarer Teil · Formular «… im Geschäftsvermögen» mit Spartenrechnung → Ertrag abzüglich zurechenbarer Aufwand
- **Rechnen:** PV: Kanton 50% / Bund 30% × Bruttoertrag; GV: Kanton 50% / Bund 30% × (Ertrag − zurechenbarer Aufwand) → Code 284
- **Regel:** Nicht steuerbarer Teil der Erträge aus qualifizierten Beteiligungen (mind. 10%); die Bruttoerträge stehen in Ziff. 4.1/4.2 bzw. 2.1. Staatssteuer: 50% (Privatvermögen und – nach Abzug des zurechenbaren Aufwands – Geschäftsvermögen); Bundessteuer: 30%.
- **Beachten:** Nur Beteiligungen ≥ 10% des Grund- oder Stammkapitals; Ausschüttung brutto im WV mit Code «Q»
- **Beachten:** Gratis abgegebene Mitarbeiteraktien: kein Abzug
- **Bund:** Teilbesteuerung 30% (statt 50% bei der Staatssteuer).
- **Quellen:**
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0100.md) `zh-wl-2026-uj__c0100` – «für qualifizierte Beteiligungen im Privatvermögen beträgt 50%,»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0100.md) `zh-wl-2026-uj__c0100` – «qualifizierte Beteiligungen im Privatvermögen beträgt 30%,»
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0162.md) `zh-wl-2026-uj__c0162` – «Beteiligungen, die mindestens 10% des Grund- oder Stammkapitals einer Kapitalgesellschaft»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «4.2 Davon aus qualifizierten Beteiligungen 13213211 151»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0101.md) `zh-wl-2026-uj__c0101` – «Bei gratis abgegebenen Mitarbeiteraktien kann kein Abzug vorgenommen werden.»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «16.5 Weitere Abzüge (z.B. Beiträge an politische Parteien) Aufstellung 284»

<a id="16-5-brige-abzug-uebrige"></a>
### Ziff. 16.5 (übrige) – Weitere Abzüge – Liquidationsgewinne, Geldspiel-Einsatzkosten u.a. (Code 284)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn), Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsformular «Liquidationsgewinn bei Aufgabe der selbständigen Erwerbstätigkeit»; Aufstellung Einsatzkosten
- **Rein:** Hilfsformular «Liquidationsgewinn bei Aufgabe der selbständigen Erwerbstätigkeit» → Liquidationsgewinn aus Ziff. 2.1/2.2 · Gewinnbestätigung Lotterie/Geldspiel → steuerbarer Gewinn je Einzelgewinn · Auszug Online-Spielerkonto → im Steuerjahr abgebuchte Spieleinsätze · Hilfsblatt STAF (Form. 547) → Patentbox/F&E-Zusatzabzug (Selbständige)
- **Rechnen:** Geldspiel je Gewinn: min(5% × Gewinn; Kanton 5'200 / Bund 5'400); Online-Spielbank je Gewinn: min(abgebuchte Einsätze; 26'200 / 26'800) → Code 284
- **Regel:** Liquidationsgewinne (stille Reserven der letzten zwei Geschäftsjahre bei definitiver Aufgabe nach dem 55. Altersjahr oder wegen Invalidität) werden separat besteuert und von den Einkünften Ziff. 2.1/2.2 abgezogen; Hilfsformular einreichen. Geldspielgewinne (nicht steuerfrei): Einsatzkosten 5% des Gewinns, höchstens CHF 5'200 (Staatssteuer) bzw. CHF 5'400 (Bundessteuer). Weitere Fälle: Patentbox/F&E (Hilfsblatt STAF).
- **Beachten:** Nur nicht steuerfreie Gewinne; Grossspiel-/Online-Spielbankgewinne steuerfrei bis 1'046'400 (Kanton) / 1'071'000 (Bund)
- **Beachten:** Liquidationsgewinn: definitive Aufgabe nach vollendetem 55. Altersjahr oder wegen Invalidität; Hilfsformular
- **Beachten:** Staatssteuer: freizustellenden Teil des Grundstückgewinns hier abziehen
- **Limiten:**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'046'400 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen (BGS) steuerfrei bis Fr. 1'046'400 (Freibetrag: nur der übersteigende Anteil ist steuerbar).)** · Bund **CHF 1'071'000 (Einzelne Gewinne aus nach BGS zugelassenen Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'071'000; darüber steuerbar (abzüglich Einsatzkosten nach Art. 33 Abs. 4 DBG).)**
- **Bund:** Geldspiel-Einsatzkosten max. CHF 5'400 (statt CHF 5'200).
- **Quellen:**
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0099.md) `zh-wl-2026-uj__c0099` – «stille Reserven (Liquidationsgewinne), die in den letzten zwei Geschäftsjahren realisiert worden»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0102.md) `zh-wl-2026-uj__c0102` – «tens CHF 5’200 (Staatssteuer) bzw. CHF 5’400 (Bundessteuer), als Einsatzkosten abgezogen»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0103.md) `zh-wl-2026-uj__c0103` – «die effektiven Einsätze, maximal jedoch CHF 26’200 (Staatssteuer) bzw. CHF 26’800 (Bundes-»
  - [StG ZH § 31](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-31-t4.md) `zh-stg-2026__par-31-t4` – «Von den einzelnen Gewinnen aus der Teilnahme an Geldspielen, die nicht nach § 24 lit. j–m steuerfrei sind»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0104.md) `zh-wl-2026-uj__c0104` – «Erwerbstätigkeit (Form. 547) vollständig ausgefüllt der Steuererklärung beizulegen.»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0101.md) `zh-wl-2026-uj__c0101` – «Für die Staatssteuer ist der bei der Einkommenssteuer freizustellende Teil des Grund»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «16.5 Weitere Abzüge (z.B. Beiträge an politische Parteien) Aufstellung 284»

<a id="16-6-abzug-drittbetreuung"></a>
### Ziff. 16.6 – Abzug für fremdbetreute Kinder (Jahrg. 2012–2026) (Code 376)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Rechnungen Kita/Tagesfamilie/Hort (Aufstellung über Fremdbetreuungskosten) mit Zahlungsnachweis
- **Rein:** Rechnungen Kita/Hort/Spielgruppe/Tagesmutter + Zahlungsnachweis → bezahlte Betreuungskosten je Kind · Aufstellung Fremdbetreuungskosten mit Empfängern → beilegen; bei angestellter Betreuungsperson Kopie Lohnausweis · Seite 1 Kinder → Jahrgang 2012–2026, gleicher Haushalt
- **Rechnen:** Σ je Kind min(nachgewiesene Kosten; Kanton 25'300 / Bund 25'800); Konkubinat/alternierende Obhut: je min(Anteil; 12'650 / 12'900) → Code 376
- **Regel:** Nachgewiesene Kosten, höchstens CHF 25'300 (Staatssteuer) bzw. CHF 25'800 (Bundessteuer) pro Kind. Voraussetzungen: Kind hat das 14. Altersjahr noch nicht vollendet, lebt im gleichen Haushalt wie die steuerpflichtige Person, die für seinen Unterhalt sorgt, und die Kosten stehen in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit. Konkubinat mit gemeinsamer Sorge und Eltern mit alternierender Obhut: je halber Abzug (CHF 12'650 / 12'900 pro Kind), andere Aufteilung nachzuweisen.
- **Beachten:** Verpflegung/Unterhalt der Kinder in der Betreuung = Lebenshaltung, nicht abziehbar (Bund KS 30 Ziff. 8.5, bund-ks-30__c0044); ZH: nur pauschal ausgewiesene Kosten → 20 % als Lebenshaltung kürzen (ZStB 34.1, zh-zstb-34-1__c0022)
- **Beachten:** Nur Kosten während Arbeits-/Ausbildungszeit; Ehepaare: beide gleichzeitig erwerbstätig/in Ausbildung/erwerbsunfähig
- **Beachten:** Nur pauschal ausgewiesene Betreuungskosten: 20% als Lebenshaltungskosten kürzen
- **Beachten:** Nicht abziehbar: Sport, Musik, Vereine, Schulgeld, Nachhilfe; bei Ferienbetreuung Reise/Verpflegung/Übernachtung
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 25'300 (Kinderdrittbetreuungskosten: nachgewiesene Kosten, höchstens Fr. 25'300 pro Kind (Staatssteuer); bei Konkubinat/alternierender Obhut mit gemeinsamer Sorge je halber Abzug (Fr. 12'650).)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind, höchstens CHF 25'800; Kind unter 14 Jahren im gleichen Haushalt; Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 Jahre (Kind hat das 14. Altersjahr noch nicht vollendet, lebt im gleichen Haushalt wie die für den Unterhalt sorgende Person; Kosten im direkten kausalen Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat.)**
- **Bund:** Höchstbetrag CHF 25'800 (statt CHF 25'300); halber Abzug CHF 12'900.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «16.6 Abzug für fremdbetreute Kinder (Jahrg. 2012–2026) max. 25’300 / 25’800 376»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0105.md) `zh-wl-2026-uj__c0105` – «Kinderdrittbetreuungskosten: Der Abzug beträgt höchstens CHF 25’300 (Staatssteuer) bzw.»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0107.md) `zh-wl-2026-uj__c0107` – «Der halbe Abzug beträgt je höchstens CHF 12’650 (Staatssteuer) bzw. CHF 12’900»
  - [ZStB 34.1](../../chunks/zh/dauernd/zh-zstb-34-1/zh-zstb-34-1__c0023.md) `zh-zstb-34-1__c0023` – «Der Steuererklärung ist eine Aufstellung über die bezahlten Kinderdrittbetreuungskosten mit Angabe der Empfänger unaufgefordert beizulegen.»
  - [ZStB 34.1](../../chunks/zh/dauernd/zh-zstb-34-1/zh-zstb-34-1__c0025.md) `zh-zstb-34-1__c0025` – «soweit sie beide gleichzeitig entweder einer Erwerbstätigkeit nachgehen, in Ausbildung stehen oder erwerbsunfähig»
  - [ZStB 34.1](../../chunks/zh/dauernd/zh-zstb-34-1/zh-zstb-34-1__c0022.md) `zh-zstb-34-1__c0022` – «ist ein Anteil von 20% als nicht abzugsfähige Lebenshaltungskosten zu berücksichtigen»
  - [ZStB 34.1](../../chunks/zh/dauernd/zh-zstb-34-1/zh-zstb-34-1__c0023.md) `zh-zstb-34-1__c0023` – «sind generell nicht als Kinderdrittbetreuungskosten abzugsfähig.»
  - [ZStB 34.1](../../chunks/zh/dauernd/zh-zstb-34-1/zh-zstb-34-1__c0021.md) `zh-zstb-34-1__c0021` – «während der tatsächlichen Arbeits- oder Ausbildungszeit»

<a id="17-abzug-zweiverdiener"></a>
### Ziff. 17 – Sonderabzug bei Erwerbstätigkeit beider Ehegatten/Partner (Zweiverdienerabzug) (Code 290)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Berechnung aus den Erwerbseinkommen beider Ehegatten (Ziff. 1–2 abzüglich zugehöriger Berufsauslagen, 3a-Beiträge, PK-Einkäufe, nicht im Lohnausweis berücksichtigte AHV-/PK-Beiträge)
- **Rein:** Lohnausweise beider Ehegatten Ziff. 11 bzw. Jahresrechnung Selbständige → Erwerbseinkommen je Ehegatte · Übertrag Ziff. 11.1/11.2, 14, 16.1 → davon abziehen (Berufsauslagen, 3a, PK-Einkauf, AHV/PK nicht im LA) · Taggelder/Erwerbsausfallentschädigungen zählen zum Erwerbseinkommen; Renten, Vermögensertrag nicht (Bund)
- **Rechnen:** Kanton min(6'200; niedrigeres verbleibendes EK); Bund: EK > 8'600 → min(max(50% × EK; 8'600); 14'100), sonst EK → Code 290; unterjährig × Tage : 360
- **Regel:** Nur einmal beanspruchbar, nur bei rechtlich und tatsächlich ungetrennter Ehe und Erwerbstätigkeit beider. Massgebend ist das verbleibende niedrigere Erwerbseinkommen. Staatssteuer: max. CHF 6'200 (bei niedrigerem Erwerbseinkommen nur dieser Betrag). Bei erheblicher Mitarbeit im Geschäft des anderen Ehegatten wird vom gemeinsamen verbleibenden Erwerbseinkommen abgezogen (Bund: je hälftig aufteilen).
- **Beachten:** Nur einmal; rechtlich und tatsächlich ungetrennte Ehe, beide erwerbstätig
- **Beachten:** Erhebliche Mitarbeit im Geschäft des Ehegatten: Kanton vom gemeinsamen EK; Bund EK in der Regel je hälftig
- **Beachten:** Bund: kein Abzug, wenn aus der Erwerbstätigkeit ein Verlust resultiert
- **Limiten:**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **CHF 6'200 (Zweiverdienerabzug (Ehegatten in ungetrennter Ehe, unabhängig erzielte Erwerbseinkommen oder erhebliche Mitarbeit im Geschäft des Ehegatten): Fr. 6'200, begrenzt auf das niedrigere Erwerbseinkommen.)** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum.)**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **n/a** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum.)**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **n/a** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (Ehepaare in ungetrennter Ehe, beide erwerbstätig).)**
- **Bund:** Bundessteuer: 50% des niedrigeren Erwerbseinkommens, mind. CHF 8'600 und max. CHF 14'100; bei weniger als CHF 8'600 Abzug in Höhe des niedrigeren Erwerbseinkommens.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «17. Sonderabzug bei Erwerbstätigkeit beider Ehegatten/Partn.»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0109.md) `zh-wl-2026-uj__c0109` – «Der Abzug beträgt max. CHF 6’200 und steht wie folgt zu:»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0110.md) `zh-wl-2026-uj__c0110` – «jedoch mind. CHF 8’600 und max. CHF 14’100;»
  - [KS 30 S. 17–18](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0052.md) `bund-ks-30__c0052` – «Dem Erwerbseinkommen gleichgestellt sind Erwerbsausfallsentschädigungen bei vorüber-»
  - [WL 2a 2026 S. 8](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0056.md) `bund-wl-2a-2026__c0056` – «kommt in Betracht, wenn sich aus der Erwerbstätigkeit ein Ver-»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0108.md) `zh-wl-2026-uj__c0108` – «Massgebend für die Berechnung ist das verbleibende niedrigere Erwerbseinkommen,»
  - [WL ZH 2026 UJ S. 37](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0235.md) `zh-wl-2026-uj__c0235` – «6’200 : 360 x 150 = 2’583»

<a id="18-berechnung-total"></a>
### Ziff. 18 – Total der Abzüge, zu übertragen in Ziffer 20 (Code 299)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Summe Ziff. 11–17
- **Rein:** Übertrag Ziff. 11.1–17 (Codes 220–290), je Spalte Staats-/Bundessteuer
- **Rechnen:** 299 = 220 + 240 + 250 + 254 + 255 + 256 + 260 + 261 + 264 + 270 + 280 + 292 + 283 + 3160 + 284 + 376 + 290 (je Spalte)
- **Regel:** Rechenzeile; Staats- und Bundessteuer-Spalte getrennt.
- **Beachten:** Spalten Staats- und Bundessteuer getrennt summieren (Beträge oft verschieden)
- **Beachten:** Nur Abzugscodes: 13.3 → 256 (nicht 2561), 14.1/14.2 → 260/261 (nicht 262/263), 14.3 → 264 (nicht 276/278)
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «18. Total der Abzüge, zu übertragen in Ziffer 20 299»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0007.md) `zh-form-300-2026-uj__c0007` – «13.3 Rentenleistungen CHF 2561 113211 abzugsfähig: Ertragsanteil 256»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0007.md) `zh-form-300-2026-uj__c0007` – «11.1 Person 1 Berufsauslagen 220»

## Hilfsblatt Berufskosten

<a id="form-360-ziff-1-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1.1 – Fahrkosten – Abonnementskosten öffentliche Verkehrsmittel (Code 201)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → ÖV-Abonnement (Rechnung/Beleg); Lohnausweis Feld F
- **Rein:** ÖV-Abo-Rechnung/Quittung → Abokosten Strecke Wohn-/Arbeitsort · Lohnausweis Feld F → angekreuzt = kein Abzug · Lohnausweis Ziff. 2.3 → Wegvergütung bzw. privat genutztes GA (als Lohn versteuert)
- **Rechnen:** notwendige Abokosten Wohn- ↔ Arbeitsstätte → Code 201 (Staat = Bund); Plafond im Zwischentotal Ziff. 1: Kanton 5'200 / Bund 3'300
- **Regel:** Notwendige Abonnementskosten bei ständiger Benützung öffentlicher Verkehrsmittel (Bahn, Schiff, Tram, Bus). Lohnausweis Feld F (unentgeltliche Beförderung Wohn-/Arbeitsort) angekreuzt = dem Arbeitnehmer erwachsen keine Arbeitswegkosten, d.h. kein Fahrkostenabzug (auch kein Abo-Abzug); bei Geschäftsfahrzeug oder vom Arbeitgeber zur Verfügung gestelltem GA aus geschäftlichen Gründen. Vergütete Arbeitswegkosten stehen im LA Ziff. 2.3 (dann Feld F nicht angekreuzt). Halbtaxabo-Vergütung muss nicht bescheinigt werden. Max. Fahrkosten insgesamt: siehe Zwischentotal (Code 205).
- **Beachten:** Feld F (Geschäftsfahrzeug, Sammeltransport, geschäftlich nötiges GA) → keine Arbeitswegkosten
- **Beachten:** Wegvergütung des Arbeitgebers ist Bruttolohn; Abokosten allenfalls als Berufskosten abziehbar
- **Beachten:** Heimkehr bei Wochenaufenthalt (i.d.R. ÖV, z.B. GA) ebenfalls hier erfassen
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrten Wohn-/Arbeitsstätte (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt): Höchstbetrag Fr. 5'200 im Jahr (Staats- und Gemeindesteuer). Bei der direkten Bundessteuer gilt ein anderer Höchstbetrag (Fr. 3'300 laut WL 2026 UJ; siehe Bund-Datei).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes 201 (Person 1, Staat/Bund) / 221 (Person 2)
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0057.md) `zh-wl-2026-uj__c0057` – «bei ständiger Benützung öffentlicher Verkehrsmittel (Bahn, Schiff, Strassenbahn, Autobus) die notwendigen Abonnementskosten»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer keine Kosten für den Arbeitsweg»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0054.md) `zh-wl-2026-uj__c0054` – «Abonnementkosten für öffentliche Verkehrsmittel 201»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0011.md) `bund-wl-lohnausweis-2026__c0011` – «das Zurverfügungstellen eines (aus geschäftlichen Gründen benützten) Generalabon»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «die Beförderung zum Arbeitsort mittels Sammeltransports (v.a. im Baugewerbe);»
  - [WL Lohnausweis 2026 S. 15–16](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0039.md) `bund-wl-lohnausweis-2026__c0039` – «Solche Entschädigungen sind stets zum Bruttolohn zu addieren»
  - [WL Lohnausweis 2026 S. 9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0016.md) `bund-wl-lohnausweis-2026__c0016` – «so wird der Betrag als Berufskostenentschädigung in Ziffer 2.3 deklariert.»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0066.md) `zh-wl-2026-uj__c0066` – «Diese sind unter Ziffer 1 des Berufsauslagenblatts in Abzug zu bringen.»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0002.md) `zh-form-360-2026-uj__c0002` – «1.1 Abonnementkosten für öffentliche Verkehrsmittel 201 3211 201 3211»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0006.md) `zh-form-360-2026-uj__c0006` – «1.1 Abonnementkosten für öffentliche Verkehrsmittel 221 3211 221 3211»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0003.md) `zh-form-360-2026-uj__c0003` – «Zwischentotal 205 3211 205 3211 ▸ max. CHF 5'200 ▸ max. CHF 3'300»

<a id="form-360-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1.2 – Fahrkosten – Fahrrad, Kleinmotorrad (gelbes Kontrollschild) pauschal (Code 202)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → keine Pauschale-Belege nötig; Lohnausweis Feld F prüfen
- **Rein:** keine Belege; Angabe ständige Benützung Fahrrad/Motorfahrrad/Kleinmotorrad (gelbes Kontrollschild) · Lohnausweis Feld F → angekreuzt = kein Abzug
- **Rechnen:** pauschal 700 pro Jahr → Code 202 (Kanton = Bund); zählt ins plafonierte Zwischentotal Ziff. 1
- **Regel:** Pauschal CHF 700 pro Jahr bei ständiger Benützung eines eigenen Fahrrads oder Kleinmotorrads mit gelbem Kontrollschild. Kein Abzug bei Feld F im Lohnausweis.
- **Beachten:** Nur bei ständiger Benützung; Motorfahrrad gleichgestellt (Verfügung LS 631.33 I.1b)
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Fahrrad, Motorfahrrad oder Motorrad mit gelbem Kontrollschild bei ständiger Benützung: Pauschale Fr. 700 im Jahr.)** · Bund **CHF 700 (Fahrrad, Motorfahrrad, Motorrad mit gelbem Kontrollschild: Pauschale CHF 700 pro Jahr; tatsächliche Kosten können nicht zusätzlich geltend gemacht werden.)**
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes 202 (Person 1, Staat/Bund) / 222 (Person 2)
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0055.md) `zh-wl-2026-uj__c0055` – «1.2 Fahrrad, Kleinmotorrad (gelbes Kontrollschild) pauschal CHF 700»
  - [LS 631.33 (ab 2026) S. 1](../../chunks/zh/2026/zh-pauschalierung-berufsauslagen-2026/zh-pauschalierung-berufsauslagen-2026__c0001.md) `zh-pauschalierung-berufsauslagen-2026__c0001` – «bei ständiger Benützung eines Fahrrades, Motorfahrrades oder Motorrades mit»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer keine Kosten für den Arbeitsweg»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0002.md) `zh-form-360-2026-uj__c0002` – «1.2 Fahrrad, Kleinmotorrad (gelbes Kontrollschild) pauschal CHF 700 202 111 202 111»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0006.md) `zh-form-360-2026-uj__c0006` – «1.2 Fahrrad, Kleinmotorrad (gelbes Kontrollschild) pauschal CHF 700 222 111 222 111»

<a id="form-360-ziff-1-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1.3 – Fahrkosten – privates Auto/Motorrad (weisses Kontrollschild), Kilometeransatz (Code 204)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Arbeitstage x Fahrten x km; Begründung (Form. 360 Ziff. 7, Codes 2041–2044); ggf. Arbeitgeberbestätigung/Arztzeugnis
- **Rein:** Arbeitszeitkalender → Anzahl Arbeitstage (i.d.R. max. 240) · Distanz Wohn-/Arbeitsort → km pro Fahrt, Fahrten pro Tag · Begründung Form. 360 Ziff. 7 (Codes 2041–2044) + Arbeitgeberbestätigung bzw. Arztzeugnis · Leasingvertrag → Feld «geleastes Fahrzeug» ankreuzen
- **Rechnen:** Arbeitstage (≤ 240) × Fahrten/Tag × km × 0.75 (Auto) bzw. 0.40 (Motorrad) → Code 204; Gesamt Ziff. 1 ≤ Kanton 5'200 / Bund 3'300
- **Regel:** Nur ausnahmsweise abziehbar (kein öffentliches Verkehrsmittel, Haltestelle mind. 1 km entfernt bzw. keine Verbindung bei Arbeitsbeginn/-ende; Zeitersparnis über 1 Stunde; ständige Benützung während der Arbeitszeit auf Verlangen des Arbeitgebers; Krankheit/Gebrechlichkeit mit Arztzeugnis). Auto CHF 0.75/km (neu 2026, vorher 0.70), Motorrad CHF 0.40/km; in der Regel begrenzt auf 240 Tage. Geleastes Fahrzeug ankreuzen. Mittagsheimfahrt: nur bis zur Höhe des Verpflegungsabzugs, dafür entfällt Verpflegungsabzug Ziff. 2.1. Geschäftsfahrzeug: kein Fahrkostenabzug (LA Feld F).
- **Beachten:** Ohne Begründung (2041–2044) nur Abokosten des ÖV abziehbar (Verfügung LS 631.33 I.1c)
- **Beachten:** Mittagsheimfahrt: Kanton max. 3'200/Jahr, Bund max. 15/Tag; dafür kein Verpflegungsabzug Ziff. 2.1
- **Beachten:** Bund: km-Ansatz nur, wenn ÖV fehlt oder Benützung objektiv nicht zumutbar (BKV Art. 5)
- **Limiten:**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.75 (Privates Auto (nur ausnahmsweise abziehbar): 75 Rp. pro Fahrkilometer (2026; 2025: 70 Rp.).)** · Bund **CHF 0.75 (Privatauto: CHF 0.75 pro Fahrkilometer, nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist; Gesamtmaximum CHF 3'300.)**
  - Fahrkosten Motorrad – Ansatz pro km (CHF): Kanton **CHF 0.40 (Motorrad mit weissem Kontrollschild (nur ausnahmsweise abziehbar): 40 Rp. pro Fahrkilometer.)** · Bund **CHF 0.40 (Motorrad mit weissem Kontrollschild: CHF 0.40 pro Fahrkilometer (nur wenn kein öffentliches Verkehrsmittel zumutbar); Gesamtmaximum CHF 3'300.)**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **240 Tage (Bei Auto/Motorrad (weisses Kontrollschild) ist der Fahrkostenabzug in der Regel auf 240 Arbeitstage begrenzt.)** · Bund **n/a – Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrten Wohn-/Arbeitsstätte (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt): Höchstbetrag Fr. 5'200 im Jahr (Staats- und Gemeindesteuer). Bei der direkten Bundessteuer gilt ein anderer Höchstbetrag (Fr. 3'300 laut WL 2026 UJ; siehe Bund-Datei).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Bemerkung:** Bei der direkten Bundessteuer dieselben Ansätze laut Formular 360 (Spalte Bund). Formular 2026 (UJ): bestaetigt; Codes 204 (Person 1, Staat/Bund) / 224 (Person 2)
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0059.md) `zh-wl-2026-uj__c0059` – «Die Kosten für das private Motorfahrzeug können nur ausnahmsweise geltend gemacht»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0060.md) `zh-wl-2026-uj__c0060` – «für Auto 75 Rp. pro Fahrkilometer.»
  - [WL ZH 2026 UJ S. 8](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0021.md) `zh-wl-2026-uj__c0021` – «der Fahrkostenabzug für Automobile pro Kilometer von CHF 0.70 auf CHF 0.75 angehoben worden»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0055.md) `zh-wl-2026-uj__c0055` – «Motorrad: CHF 0.40 pro km geleastes Fahrzeug»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0058.md) `zh-wl-2026-uj__c0058` – «Fehlen eines öffentlichen Verkehrsmittels (siehe Wegleitung) 2041»
  - [LS 631.33 (ab 2026) S. 1](../../chunks/zh/2026/zh-pauschalierung-berufsauslagen-2026/zh-pauschalierung-berufsauslagen-2026__c0001.md) `zh-pauschalierung-berufsauslagen-2026__c0001` – «bei ständiger Benützung eines Motorrades oder Autos»
  - [LS 631.33 (ab 2026) S. 2](../../chunks/zh/2026/zh-pauschalierung-berufsauslagen-2026/zh-pauschalierung-berufsauslagen-2026__c0003.md) `zh-pauschalierung-berufsauslagen-2026__c0003` – «Für Hin- und Rückfahrt über Mittag sind in diesen Fällen höchstens»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0044.md) `bund-wl-2a-2026__c0044` – «doch zusammen höchstens 15 Fr. im Tag berechnet werden»
  - [BKV Art. 5](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-5.md) `bund-bkv-2026__art-5` – «sofern kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0002.md) `zh-form-360-2026-uj__c0002` – «1.3 Auto, Motorrad (weisses Kontrollschild) in der Regel begrenzt auf 240 Tage»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0002.md) `zh-form-360-2026-uj__c0002` – «Auto: CHF 0.75 pro km Motorrad: CHF 0.40 pro km geleastes Fahrzeug»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0003.md) `zh-form-360-2026-uj__c0003` – «} 204 13211 204 13211 Zwischentotal 205»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0007.md) `zh-form-360-2026-uj__c0007` – «} 224 13211 224 13211 Zwischentotal 225»

<a id="form-360-ziff-1-zwischentotal-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1 (Zwischentotal) – Fahrkosten Zwischentotal mit Plafonierung (Code 205)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg → Summe Ziff. 1.1–1.3; Lohnausweis Feld F
- **Rein:** Übertrag Ziff. 1.1–1.3 (Form. 360) · Lohnausweis Feld F / Geschäftsfahrzeug → Fahrkosten 0
- **Rechnen:** min(Σ Ziff. 1.1–1.3; Kanton 5'200 / Bund 3'300) → Code 205, je Person
- **Regel:** Plafonierung: Staatssteuer max. CHF 5'200, direkte Bundessteuer max. CHF 3'300 (je Person). Lohnausweis Feld F angekreuzt: Fahrkosten auf null setzen. Arbeitnehmende mit Geschäftsfahrzeug können keine Fahrkosten abziehen.
- **Beachten:** Plafond umfasst auch Heimkehr-Fahrkosten bei Wochenaufenthalt (Kanton LS 631.33; Bund BKV Art. 9 Abs. 4)
- **Beachten:** Geschäftsfahrzeug mit pauschaler Fahrkostenberechnung (Bund: 0,9 % Kaufpreis/Monat als Einkommen): kein Abzug
- **Beachten:** Plafond gilt je Person (Ehegatten je eigenes Hilfsblatt)
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrten Wohn-/Arbeitsstätte (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt): Höchstbetrag Fr. 5'200 im Jahr (Staats- und Gemeindesteuer). Bei der direkten Bundessteuer gilt ein anderer Höchstbetrag (Fr. 3'300 laut WL 2026 UJ; siehe Bund-Datei).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Bund:** Fahrkostenabzug max. CHF 3'300 (statt CHF 5'200).
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes 205 (Person 1, Staat/Bund) / 225 (Person 2)
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0060.md) `zh-wl-2026-uj__c0060` – «Bei der Staatssteuer ist der Fahrkostenabzug auf CHF 5’200 beschränkt.»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0060.md) `zh-wl-2026-uj__c0060` – «Bei der direkten Bundessteuer ist der Fahrkostenabzug auf CHF 3’300 beschränkt.»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0060.md) `zh-wl-2026-uj__c0060` – «Arbeitnehmende, die über ein Geschäftsfahrzeug verfügen, können keine Fahrkosten in Ab-»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer keine Kosten für den Arbeitsweg»
  - [LS 631.33 (ab 2026) S. 2](../../chunks/zh/2026/zh-pauschalierung-berufsauslagen-2026/zh-pauschalierung-berufsauslagen-2026__c0003.md) `zh-pauschalierung-berufsauslagen-2026__c0003` – «unter Einbezug der Fahrkosten bei auswärtigem Wochenaufenthalt»
  - [LS 631.33 (ab 2026) S. 2](../../chunks/zh/2026/zh-pauschalierung-berufsauslagen-2026/zh-pauschalierung-berufsauslagen-2026__c0003.md) `zh-pauschalierung-berufsauslagen-2026__c0003` – «kann kein Abzug für Kosten für Fahrten zwischen Wohn- und Arbeitsstätte geltend gemacht werden»
  - [BKV Art. 5a](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-5a.md) `bund-bkv-2026__art-5a` – «gelten 0,9 Prozent des Kaufpreises des Fahrzeugs als monatliches Einkommen aus dieser Nutzung»
  - [BKV Art. 9](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-9.md) `bund-bkv-2026__art-9` – «Sie sind bis zum Maximalbetrag nach Artikel 5 Absatz 1 abziehbar.»
  - [LS 631.33 (ab 2026) S. 3–4](../../chunks/zh/2026/zh-pauschalierung-berufsauslagen-2026/zh-pauschalierung-berufsauslagen-2026__c0007.md) `zh-pauschalierung-berufsauslagen-2026__c0007` – «Sind beide Ehegatten erwerbstätig, werden die Abzüge für Be-»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0054.md) `zh-wl-2026-uj__c0054` – «Person 1 (Berufskosten Person 2 siehe Rückseite)»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0003.md) `zh-form-360-2026-uj__c0003` – «Zwischentotal 205 3211 205 3211 ▸ max. CHF 5'200 ▸ max. CHF 3'300»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0007.md) `zh-form-360-2026-uj__c0007` – «Zwischentotal 225 3211 225 3211 ▸ max. CHF 5'200 ▸ max. CHF 3'300»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0005.md) `zh-form-360-2026-uj__c0005` – «Arbeitnehmende, die über ein Geschäftsfahrzeug verfügen, können keine Fahrkosten in Abzug bringen.»

<a id="form-360-ziff-7-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 7 – Begründung für die Benützung eines privaten Motorfahrzeugs (Codes 2041–2044)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Zutreffendes ankreuzen; Arbeitgeberbestätigung bzw. Arztzeugnis beilegen
- **Rein:** Fahrplan / Distanz zur Haltestelle → 2041 (≥ 1 km oder kein ÖV bei Arbeitsbeginn/-ende) · Zeitvergleich ÖV vs. Motorfahrzeug (Haustür–Arbeitsplatz und zurück) → 2042 (über 1 Stunde) · Arbeitgeberbestätigung → 2043 · Arztzeugnis → 2044
- **Rechnen:** kein Betrag; ≥ 1 Kreuz 2041–2044 = Voraussetzung für km-Abzug Ziff. 1.3, sonst nur ÖV-Abokosten
- **Regel:** Mindestens eine Begründung ankreuzen, sonst wird der Auto-/Motorradabzug nicht gewährt.
- **Beachten:** 2043: auf Verlangen und gegen Entschädigung des AG ständig in der Arbeitszeit benützt, Arbeitsweg unentschädigt
- **Beachten:** Geschäftsfahrzeug: keine Fahrkosten, Begründung entfällt
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes 2041–2044 (Person 1) / 2241–2244 (Person 2)
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0058.md) `zh-wl-2026-uj__c0058` – «Fehlen eines öffentlichen Verkehrsmittels (siehe Wegleitung) 2041»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0059.md) `zh-wl-2026-uj__c0059` – «nächsten Haltestelle mindestens 1 km entfernt ist oder bei Arbeitsbeginn oder -ende kein»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0059.md) `zh-wl-2026-uj__c0059` – «private Motorfahrzeug tatsächlich ständig während der Arbeitszeit benützt und für die Fahr-»
  - [LS 631.33 (ab 2026) S. 1](../../chunks/zh/2026/zh-pauschalierung-berufsauslagen-2026/zh-pauschalierung-berufsauslagen-2026__c0001.md) `zh-pauschalierung-berufsauslagen-2026__c0001` – «bei ständiger Benützung eines Motorrades oder Autos»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0005.md) `zh-form-360-2026-uj__c0005` – «7. Begründung für die Benützung eines privaten Motorfahrzeuges für den Arbeitsweg»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0005.md) `zh-form-360-2026-uj__c0005` – «Fehlen eines öffentlichen Verkehrsmittels (siehe Wegleitung) 2041»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0005.md) `zh-form-360-2026-uj__c0005` – «Zeitersparnis von über 1 Stunde bei Benützung des privaten Motorfahrzeuges 2042»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0005.md) `zh-form-360-2026-uj__c0005` – «Ständige Benützung während der Arbeitszeit auf Verlangen und gegen Entschädigung des Arbeitgebers 2043»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0005.md) `zh-form-360-2026-uj__c0005` – «Unmöglichkeit der Benützung des öffentl. Verkehrsmittels zufolge Krankheit / Gebrechlichkeit (Arztzeugnis beilegen) 2044»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0009.md) `zh-form-360-2026-uj__c0009` – «Fehlen eines öffentlichen Verkehrsmittels (siehe Wegleitung) 2241»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0009.md) `zh-form-360-2026-uj__c0009` – «Unmöglichkeit der Benützung des öffentl. Verkehrsmittels zufolge Krankheit / Gebrechlichkeit (Arztzeugnis beilegen) 2244»

<a id="form-360-ziff-2-1-verbilligt-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 360 Ziff. 2.1 (verbilligt) – Mehrkosten Verpflegung bei verbilligter Verpflegung durch den Arbeitgeber (Code 206)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Feld G (Kantinenverpflegung/Lunch-Checks), Anzahl Arbeitstage
- **Rein:** Lohnausweis Feld G → Kantine/Personalrestaurant, Lunch-Checks, Mittagessensentschädigung bei 40–60 % Aussendienst · Arbeitszeiterfassung → Anzahl Arbeitstage mit auswärtiger Verpflegung
- **Rechnen:** min(Arbeitstage × 7.50; 1'600) → Code 206 (Kanton = Bund)
- **Regel:** Ist im Lohnausweis Feld G angekreuzt (Kantine, Personalrestaurant, Lunch-Checks, Barbeitrag), steht nur der reduzierte Ansatz zu: CHF 7.50 pro Arbeitstag, höchstens CHF 1'600 pro Jahr (nur wenn die Arbeitspause die Heimkehr nicht ermöglicht und Mehrkosten gegenüber zu Hause entstehen). Das Feld G wird auch angekreuzt, wenn die Möglichkeit verbilligter Verpflegung besteht, unabhängig von der tatsächlichen Nutzung. Mittagessen vom Arbeitgeber voll bezahlt (LA Ziff. 15): kein Verpflegungsabzug. Die Abzüge Ziff. 2.1 und 2.2 dürfen nicht kumuliert werden.
- **Beachten:** LA Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt» (über 60 % Aussendienst): kein Abzug
- **Beachten:** Bund: kein Abzug, wenn Verpflegung unter den amtlichen Naturalbezugs-Ansätzen möglich (BKV Art. 6 Abs. 3)
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Verpflegung durch Arbeitgeber verbilligt (Kantine, Personalrestaurant, Barbeitrag, Essensgutscheine) und trotzdem Mehrkosten: Fr. 7.50 pro Arbeitstag.)** · Bund **CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei ständiger auswärtiger Verpflegung mit Verbilligung durch den Arbeitgeber: höchstens Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)**
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes 206 (Person 1, Staat/Bund) / 226 (Person 2)
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0061.md) `zh-wl-2026-uj__c0061` – «– wenn die Verpflegung durch den Arbeitgeber verbilligt wird (Kantine, Personalrestaurant,»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten Buchstabe G»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0056.md) `zh-wl-2026-uj__c0056` – «pro Arbeitstag CHF 7.50 / im Jahr CHF 1’600 206»
  - [LS 631.33 (ab 2026) S. 3–4](../../chunks/zh/2026/zh-pauschalierung-berufsauslagen-2026/zh-pauschalierung-berufsauslagen-2026__c0007.md) `zh-pauschalierung-berufsauslagen-2026__c0007` – «Soweit Berufsauslagen vom Arbeitgeber vergütet werden, steht der steuerpflichtigen Person kein Abzug zu.»
  - [BKV Art. 6](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-6-t1.md) `bund-bkv-2026__art-6-t1` – «Kein Abzug ist mangels Mehrkosten zulässig, wenn der Arbeitgeber bei der Bewertung von Naturalbezügen»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0003.md) `zh-form-360-2026-uj__c0003` – «Mehrkosten entstehen: pro Arbeitstag CHF 7.50 / im Jahr CHF 1’600 206 3211 206 3211»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0007.md) `zh-form-360-2026-uj__c0007` – «Mehrkosten entstehen: pro Arbeitstag CHF 7.50 / im Jahr CHF 1’600 226 3211 226 3211»

<a id="form-360-ziff-2-1-voll-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 360 Ziff. 2.1 (voll) – Mehrkosten Verpflegung bei voller Verpflegung zu Lasten des Arbeitnehmers (Code 208)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Anzahl Arbeitstage mit auswärtiger Verpflegung; Lohnausweis Feld G darf NICHT angekreuzt sein
- **Rein:** Lohnausweis → Feld G leer, Ziff. 15 ohne «Mittagessen durch Arbeitgeber bezahlt» · Arbeitszeiterfassung → Anzahl Arbeitstage mit auswärtigem Mittagessen
- **Rechnen:** min(Arbeitstage × 15; 3'200) → Code 208 (Kanton = Bund)
- **Regel:** CHF 15 pro Arbeitstag, bei ständiger auswärtiger Verpflegung höchstens CHF 3'200 pro Jahr, wenn die Verpflegung in anderen Gaststätten voll zu Lasten des Arbeitnehmers geht. Ist im Lohnausweis Feld G angekreuzt, gilt dagegen Ansatz «verbilligt» (CHF 7.50 / 1'600).
- **Beachten:** Nur wenn Arbeitspause keine Heimkehr erlaubt und Mehrkosten gegenüber Verpflegung zu Hause entstehen
- **Beachten:** Bund: kein Abzug, wenn die Hauptmahlzeit höchstens CHF 10 kostet
- **Beachten:** Mittagsheimfahrt mit privatem Motorfahrzeug ersetzt diesen Abzug
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Auswärtige Verpflegung, wenn voll zulasten des Arbeitnehmers (Dauer der Arbeitspause ermöglicht keine Heimkehr): Fr. 15 pro Arbeitstag.)** · Bund **CHF 15 (Auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (in der Regel nur Mittagessen), nur Pauschale zulässig, wenn Hauptmahlzeit wegen grosser Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann oder bei durchgehender Schicht-/Nachtarbeit.)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei ständiger auswärtiger Verpflegung (voll zulasten Arbeitnehmer): höchstens Fr. 3'200 im Jahr. Nicht kumulierbar mit der Schicht-/Nachtarbeits-Pauschale.)** · Bund **CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)**
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes 208 (Person 1, Staat/Bund) / 228 (Person 2)
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0061.md) `zh-wl-2026-uj__c0061` – «– wenn die Verpflegung in andern Gaststätten voll zu Lasten des Arbeitnehmers geht,»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0056.md) `zh-wl-2026-uj__c0056` – «wenn die Verpflegung voll zu Lasten des Arbeitnehmers geht: pro Arbeitstag CHF 15 / im Jahr CHF 3’200 208»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0046.md) `bund-wl-2a-2026__c0046` – «Kein Abzug ist mangels Mehrkosten zu gewähren, wenn»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0060.md) `zh-wl-2026-uj__c0060` – «Dafür entfällt der Verpflegungsabzug (Ziffer 2.1).»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – ««Mittagessen durch Arbeitgeber bezahlt»»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0003.md) `zh-form-360-2026-uj__c0003` – «wenn die Verpflegung voll zu Lasten des Arbeitnehmers geht: pro Arbeitstag CHF 15 / im Jahr CHF 3’200 208»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0007.md) `zh-form-360-2026-uj__c0007` – «wenn die Verpflegung voll zu Lasten des Arbeitnehmers geht: pro Arbeitstag CHF 15 / im Jahr CHF 3’200 228»

<a id="form-360-ziff-2-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 360 Ziff. 2.2 – Mehrkosten Verpflegung bei Schicht-/Nachtarbeit (Code 210)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 (Anzahl Schichttage im Kalenderjahr); Arbeitgeberbestätigung
- **Rein:** Lohnausweis Ziff. 15 → Anzahl Schichttage (freiwillige Angabe) · Arbeitgeberbestätigung → Tage mit durchgehender Schicht-/Nachtarbeit ≥ 8 Std., Arbeitsort
- **Rechnen:** min(Schichttage × 15; 3'200) → Code 210 (Kanton = Bund)
- **Regel:** Bei durchgehender, mindestens achtstündiger Schicht- oder Nachtarbeit CHF 15 pro ausgewiesenem Schichttag, bei ständiger Schicht-/Nachtarbeit höchstens CHF 3'200 pro Jahr; gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt, sofern beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause eingenommen werden können. Anzahl Schichttage steht – freiwillig – in Lohnausweis Ziff. 15 (Bemerkungen); fehlt sie, Bestätigung des Arbeitgebers einholen. Nicht mit Ziff. 2.1 kumulieren.
- **Beachten:** Nicht mit Ziff. 2.1 kumulieren; gestaffelte Arbeitszeit nur, wenn beide Hauptmahlzeiten nicht zu Hause möglich
- **Beachten:** Bund: bei Verbilligung/Kantine nur halber Abzug (BKV Art. 6 Abs. 2) = CHF 7.50/Tag bzw. 1'600/Jahr (nicht nochmals halbieren); AG bescheinigt Tage auf Verlangen (Abs. 5)
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Durchgehende, mindestens achtstündige Schicht- oder Nachtarbeit: Fr. 15 pro ausgewiesenen Schichttag, bei ständiger Schicht-/Nachtarbeit höchstens Fr. 3'200 im Jahr. Gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt, wenn die Hauptmahlzeiten nicht zur üblichen Zeit zu Hause eingenommen werden können.)** · Bund **CHF 15 (Schicht-/Nachtarbeit: gleiche Pauschale wie auswärtige Verpflegung, CHF 15 pro Tag bzw. max. CHF 3'200 pro Jahr (bei Verbilligung halber Abzug). Gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt (Art. 6 Abs. 4 BKV). Arbeitgeber muss Tage und Arbeitsort auf Verlangen bescheinigen.)**
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes 210 (Person 1, Staat/Bund) / 230 (Person 2)
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0061.md) `zh-wl-2026-uj__c0061` – «2.2 Bei durchgehender, mindestens achtstündiger Schicht- oder Nachtarbeit, pro aus-»
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «die Anzahl im Kalenderjahr geleisteter Schichttage und die Höhe der im»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0056.md) `zh-wl-2026-uj__c0056` – «pro ausgewiesenem Schichttag CHF 15 / im Jahr CHF 3’200 210»
  - [BKV Art. 6](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-6-t1.md) `bund-bkv-2026__art-6-t1` – «Nur der halbe Abzug ist zulässig, wenn die Verpflegung vom Arbeitgeber anders als in bar verbilligt wird»
  - [BKV Art. 6](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-6-t2.md) `bund-bkv-2026__art-6-t2` – «Der Arbeitgeber muss die Anzahl Tage mit Schicht- oder Nachtarbeit sowie den Arbeitsort auf Verlangen bescheinigen.»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0003.md) `zh-form-360-2026-uj__c0003` – «2.2 bei durchgehender, mindestens achtstündiger Schicht- / Nachtarbeit,»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0003.md) `zh-form-360-2026-uj__c0003` – «pro ausgewiesenem Schichttag CHF 15 / im Jahr CHF 3’200 210 3211 210 3211»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0007.md) `zh-form-360-2026-uj__c0007` – «pro ausgewiesenem Schichttag CHF 15 / im Jahr CHF 3’200 230 3211 230 3211»

<a id="form-360-ziff-3-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 360 Ziff. 3 – Übrige Berufskosten – pauschal 3% (Code 212) bzw. effektiv (Code 213)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 Nettolohn; bei effektiven Kosten Aufstellung + Belege
- **Rein:** Lohnausweis Ziff. 11 → Nettolohn (= Ziff. 8 − Ziff. 9 − Ziff. 10) · Effektiv: Belege Berufskleider, Werkzeuge/EDV, Fachliteratur, Arbeitszimmer, Berufsverband + Aufstellung · Lohnausweis Ziff. 13 → vergütete Spesen (bei effektiver Geltendmachung abgrenzen)
- **Rechnen:** pauschal min(max(3 % × Nettolohn LA Ziff. 11; 2'000); 4'000) → Code 212 | effektiv Σ belegte Kosten → Code 213 (Ansätze Kanton = Bund)
- **Regel:** Pauschal 3% des Nettolohns gemäss Lohnausweis, mindestens CHF 2'000, höchstens CHF 4'000 (Berufskleider, Werkzeuge inkl. EDV, Fachliteratur, privates Arbeitszimmer, Berufsverbandsbeiträge). Höhere effektive Kosten: vollständig nachweisen und Aufstellung beilegen. Nettolohn = Bruttolohn nach Abzug AHV/IV/EO/ALV, laufender PK-Beiträge (inkl. aus Lohnerhöhungen) und NBU-Prämien. Vom Arbeitgeber effektiv vergütete Spesen (LA Ziff. 13) sind bei effektiver Geltendmachung zu berücksichtigen.
- **Beachten:** Kein separater Homeoffice-Abzug: Arbeitszimmer in Pauschale enthalten
- **Beachten:** Effektiv: gesamte Kosten und berufliche Notwendigkeit nachweisen; AG-vergütete Kosten nicht abziehbar
- **Beachten:** Bund: Pauschale bei Teilzeit oder unterjähriger Tätigkeit angemessen kürzen (BKV Art. 7 Abs. 2)
- **Limiten:**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **3 % (Übrige Berufskosten (Berufskleider, Berufswerkzeuge inkl. EDV, Fachliteratur, privates Arbeitszimmer, Berufsverbandsbeiträge): 3 % des Nettolohns. Nettolohn = Bruttolohn nach Abzug AHV/IV/EO/ALV, laufender Beiträge an Personalvorsorge und Prämien der obligatorischen NBUV.)** · Bund **3 % (Übrige Berufskosten (Art. 26 Abs. 1 lit. c DBG): Pauschale 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; anstelle der Pauschale ist der Nachweis höherer tatsächlicher übriger Berufskosten möglich. Fahrkosten (lit. a, max. 3'300) und Verpflegung (lit. b) werden zusätzlich abgezogen. Bei Teilzeit/Teiljahr angemessen kürzen.)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **CHF 2'000 (Mindestbetrag der Pauschale für übrige Berufskosten: Fr. 2'000.)** · Bund **CHF 2'000 (Mindestbetrag der Pauschale übrige Berufskosten.)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 4'000 (Höchstbetrag der Pauschale für übrige Berufskosten: Fr. 4'000. Höhere effektive Kosten sind in vollem Umfang nachzuweisen.)** · Bund **CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)**
  - Arbeitszimmer/Homeoffice – Regel: Kanton **Kein separater Homeoffice-/Arbeitszimmerabzug: Das private Arbeitszimmer ist in der Pauschale für übrige Berufskosten (3 % des Nettolohns, min. Fr. 2'000, max. Fr. 4'000) enthalten. Höhere effektive Kosten sind in vollem Umfang nachzuweisen (Aufstellung).** · Bund **Privates Arbeitszimmer: in der Pauschale übrige Berufskosten enthalten. Separater Abzug der Zimmerkosten (Miete, Heizung, Beleuchtung) nur bei Nachweis höherer Kosten und wenn ein Zimmer der Privatwohnung hauptsächlich und regelmässig für die Berufsarbeit benützt werden muss; bloss gelegentliche Arbeit zu Hause gibt keinen Abzug. Keine pauschale Homeoffice-Entschädigung.**
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes 212 pauschal / 213 effektiv (Person 1, Staat/Bund); 232 / 233 (Person 2)
- **Quellen:**
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0062.md) `zh-wl-2026-uj__c0062` – «3% des Nettolohnes gemäss Lohnausweis, mindestens jedoch CHF 2’000»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0064.md) `zh-wl-2026-uj__c0064` – «so sind diese Berufsauslagen in vollem Umfange nachzuweisen.»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «dass vom Bruttolohn total (Ziffer 8) das Total der Abzüge (Ziffer 9 und 10) abgezogen wird»
  - [WL Lohnausweis 2026 S. 15–16](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0039.md) `bund-wl-lohnausweis-2026__c0039` – «Spesenvergütungen (nicht im Bruttolohn enthalten) Ziffer 13»
  - [BKV Art. 7](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-7.md) `bund-bkv-2026__art-7` – «Der Pauschalabzug ist angemessen zu kürzen, wenn die unselbständige Erwerbstätigkeit bloss während eines Teils des Jahres oder als Teilzeitarbeit ausgeübt wird.»
  - [BKV Art. 4](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-4.md) `bund-bkv-2026__art-4` – «so sind die gesamten tatsächlichen Auslagen und deren berufliche Notwendigkeit nachzuweisen.»
  - [LS 631.33 (ab 2026) S. 3–4](../../chunks/zh/2026/zh-pauschalierung-berufsauslagen-2026/zh-pauschalierung-berufsauslagen-2026__c0007.md) `zh-pauschalierung-berufsauslagen-2026__c0007` – «Soweit Berufsauslagen vom Arbeitgeber vergütet werden, steht der steuerpflichtigen Person kein Abzug zu.»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0003.md) `zh-form-360-2026-uj__c0003` – «pauschal 3% des Nettolohnes gem. Lohnausweis, mind. CHF 2’000, höchstens CHF 4’000 2123211 212 3211»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0003.md) `zh-form-360-2026-uj__c0003` – «bzw. effektiv gemäss Aufstellung 213 13211 213 13211»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0007.md) `zh-form-360-2026-uj__c0007` – «höchstens CHF 4’000 2323211 232 3211»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0007.md) `zh-form-360-2026-uj__c0007` – «bzw. effektiv gemäss Aufstellung 233 13211 233 13211»

<a id="form-360-ziff-4-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 360 Ziff. 4 – Zusätzliche Mehrkosten bei auswärtigem Wochenaufenthalt (Code 2860)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag/Beleg Zimmer; Aufstellung; ÖV-Abo für Heimkehr (unter Ziff. 1.1)
- **Rein:** Mietvertrag/Quittungen Zimmer am Arbeitsort → Mietzins (nur Zimmer, nicht Wohnung) · Arbeitszeiterfassung → Arbeitstage mit Übernachtung am Arbeitsort · ÖV-Abo/GA für wöchentliche Heimkehr → unter Ziff. 1 (Fahrkosten) · Aufstellung der Mehrkosten beilegen
- **Rechnen:** Kanton: min(Arbeitstage × 15 (Abendessen); 3'200) + Zimmermiete → Code 2860 · Bund: Verpflegung 30/Tag, max. 6'400 (gekürzt 22.50 / 4'800) + Zimmer
- **Regel:** Abziehbar: Mehrkosten auswärtige Verpflegung (Abendessen CHF 15 pro Arbeitstag, bei ganzjährigem Wochenaufenthalt max. CHF 3'200 pro Jahr), Mietzins für ein Zimmer, Kosten der wöchentlichen Heimkehr (in der Regel nur ÖV, z.B. GA – unter Ziff. 1 des Hilfsblatts).
- **Beachten:** Bund: Wochenaufenthalt-Pauschale nicht zusätzlich zu Ziff. 2.1/2.2 (BKV Art. 6 Abs. 6) – Bund-Spalte abstimmen
- **Beachten:** Bund: höhere Verpflegungskosten nicht nachweisbar; Zimmer zu ortsüblichen Kosten (BKV Art. 9)
- **Beachten:** Heimkehrkosten zählen in den Fahrkosten-Plafond (Kanton 5'200 / Bund 3'300)
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Auswärtiger Wochenaufenthalt: als Mehrkosten für die auswärtige Unterkunft kann der Mietzins für ein Zimmer abgezogen werden (effektive Kosten, gemäss Aufstellung). Kosten der wöchentlichen Heimkehr in der Regel nur ÖV-Aufwendungen (unter Fahrkosten, Ziff. 1 des Berufsauslagenblatts).** · Bund **Wochenaufenthalt: abziehbar sind die ortsüblichen Auslagen für ein Zimmer (nicht eine Wohnung) am Arbeitsort sowie die Fahrkosten der regelmässigen Heimkehr (im Rahmen des Fahrkosten-Maximums).**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 3'200 (Auswärtiger Wochenaufenthalt: Mehrkosten für auswärtige Verpflegung beim Abendessen Fr. 15 pro Arbeitstag bzw. Fr. 3'200 im Jahr bei ganzjährigem Wochenaufenthalt.)** · Bund **CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug CHF 30 pro Tag bzw. CHF 6'400 pro Jahr; gekürzter Abzug (verbilligtes Mittagessen) CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr. Nachweis höherer Kosten ausgeschlossen.)**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrten Wohn-/Arbeitsstätte (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt): Höchstbetrag Fr. 5'200 im Jahr (Staats- und Gemeindesteuer). Bei der direkten Bundessteuer gilt ein anderer Höchstbetrag (Fr. 3'300 laut WL 2026 UJ; siehe Bund-Datei).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Bemerkung:** Code 2860 aus der Formularzeile; im PDF-Layout steht daneben Code 213 (effektive übrige Berufskosten) – Zuordnung am Original prüfen. Hinweis Prüfung: ZH-Wegleitung nennt nur CHF 15/Abendessen bzw. 3'200 pro Jahr; Bundes-Wert laut data/werte/bund/2026.yaml (CHF 30/Tag, 6'400) weicht ab – für die Bundessteuer am Original prüfen. Formular 2026 (UJ): bestaetigt; Codes 2860 (Person 1, Staat/Bund) / 2861 (Person 2)
- **Quellen:**
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0066.md) `zh-wl-2026-uj__c0066` – «Als Mehrkosten für auswärtige Unterkunft kann der Mietzins für ein Zimmer abgezogen werden.»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0066.md) `zh-wl-2026-uj__c0066` – «bei ganzjährigem Wochenaufenthalt CHF 3’200 im Jahr abgezogen werden»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0056.md) `zh-wl-2026-uj__c0056` – «Mehrkosten bei auswärtigem Wochenaufenthalt (gemäss Aufstellung, siehe Wegleitung)»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0044.md) `bund-wl-2a-2026__c0044` – «der Unterkunft nur ein Zimmer (nicht eine Wohnung) als be-»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0044.md) `bund-wl-2a-2026__c0044` – «pro Hauptmahlzeit, somit 30 Fr. im Tag, bei ganzjährigem»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0045.md) `bund-wl-2a-2026__c0045` – «22.50 Fr. im Tag und 4800 Fr. im Jahr;»
  - [BKV Art. 6](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-6-t2.md) `bund-bkv-2026__art-6-t2` – «Der Pauschalabzug nach Absatz 1 oder 2 kann nicht gleichzeitig mit jenem nach Artikel 9 Absatz 2 beansprucht werden.»
  - [BKV Art. 9](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-9.md) `bund-bkv-2026__art-9` – «Der Nachweis höherer Kosten ist ausgeschlossen.»
  - [BKV Art. 9](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-9.md) `bund-bkv-2026__art-9` – «Als notwendige Mehrkosten der Unterkunft sind die ortsüblichen Auslagen für ein Zimmer abziehbar.»
  - [LS 631.33 (ab 2026) S. 2](../../chunks/zh/2026/zh-pauschalierung-berufsauslagen-2026/zh-pauschalierung-berufsauslagen-2026__c0003.md) `zh-pauschalierung-berufsauslagen-2026__c0003` – «unter Einbezug der Fahrkosten bei auswärtigem Wochenaufenthalt»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0004.md) `zh-form-360-2026-uj__c0004` – «4. Mehrkosten bei auswärtigem Wochenaufenthalt (gemäss Aufstellung, siehe Wegleitung) 2860 13211 2860 13211»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0008.md) `zh-form-360-2026-uj__c0008` – «4. Mehrkosten bei auswärtigem Wochenaufenthalt (gemäss Aufstellung, siehe Wegleitung) 2861 13211 2861 13211»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0003.md) `zh-form-360-2026-uj__c0003` – «bzw. effektiv gemäss Aufstellung 213 13211 213 13211»

<a id="form-360-ziff-5-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 360 Ziff. 5 – Auslagen bei Nebenerwerb – pauschal 20% (Code 216) bzw. effektiv (Code 217)

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Einkünfte aus Nebenerwerb (Ziff. 1.2); bei effektiven Auslagen Aufstellung
- **Rein:** Lohnausweis(e) Nebenerwerb → Einkünfte Ziff. 1.2 · Effektiv: Aufstellung + Belege der Auslagen
- **Rechnen:** pauschal min(max(20 % × Σ Einkünfte aller Nebenbeschäftigungen; 800); 2'400) → Code 216 | effektiv → Code 217 (Ansätze Kanton = Bund)
- **Regel:** Pauschal 20% der Einkünfte aus allen Nebenbeschäftigungen, insgesamt mind. CHF 800 und höchstens CHF 2'400; deckt sämtliche Auslagen im Nebenerwerb (inkl. Fahrkosten, Verpflegung). Höhere effektive Auslagen detailliert aufführen und nachweisen.
- **Beachten:** Pauschale deckt alle Nebenerwerbsauslagen inkl. Fahrkosten und Verpflegung
- **Beachten:** Bund: Basis = Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge)
- **Beachten:** Behördenmitglieder (Legislative, Exekutive, Schule, Kirche): Verfügungen ZStB 17.3
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Auslagen bei Nebenbeschäftigung in unselbstständiger Stellung (inkl. Fahrkosten, auswärtige Verpflegung): 20 % der Einkünfte aus der Nebenbeschäftigung.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Mindestbetrag der Nebenerwerbs-Pauschale: Fr. 800.)** · Bund **CHF 800 (Mindestbetrag Pauschale Nebenerwerb.)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Höchstbetrag der Nebenerwerbs-Pauschale: Fr. 2'400. Höhere effektive Kosten sind detailliert aufzuführen und nachzuweisen.)** · Bund **CHF 2'400 (Höchstbetrag Pauschale Nebenerwerb.)**
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes 216 pauschal / 217 effektiv (Person 1, Staat/Bund); 236 / 237 (Person 2)
- **Quellen:**
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0067.md) `zh-wl-2026-uj__c0067` – «20% der Einkünfte aus allen Nebenbeschäftigungen, insgesamt mindestens jedoch CHF 800 und höchstens CHF 2’400»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0004.md) `zh-form-300-2026-uj__c0004` – «1.2 Nebenerwerb Person 1 Lohnausweis 102»
  - [BKV Anhang](../../chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__anhang-1.md) `bund-bkv-2026__anhang-1` – «20 % der Nettoeinkünfte, mindestens im Jahr»
  - [WL 2a 2026 S. 6](../../chunks/bund/2026/bund-wl-2a-2026/bund-wl-2a-2026__c0046.md) `bund-wl-2a-2026__c0046` – «einkommen nach Abzug der Sozialversicherungsbeiträge), min-»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0004.md) `zh-form-360-2026-uj__c0004` – «pauschal 20% der Einkünfte aus Nebenerwerb, mind. CHF 800 und höchstens CHF 2‘400 216 3211 216 3211»
  - [Formular 360 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0004.md) `zh-form-360-2026-uj__c0004` – «bzw. effektiv gemäss Aufstellung 217 13211 217 13211»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0008.md) `zh-form-360-2026-uj__c0008` – «höchstens CHF 2‘400 236 3211 236 3211»
  - [Formular 360 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-360-2026-uj/zh-form-360-2026-uj__c0008.md) `zh-form-360-2026-uj__c0008` – «bzw. effektiv gemäss Aufstellung 237 13211 237 13211»

## Hilfsblatt Versicherungsprämien

<a id="form-365-teil-a-ziff-1-6-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil A (Ziff. 1–6) – Bezahlte Versicherungsprämien und Zinsen von Sparkapitalien (Codes 601–607, Total A 606)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → 1. Private Krankenversicherung (601), 2. private Unfallversicherung (602), 3. Lebens-/Rentenversicherung (603), 4. Sparzinsen (604), 6. abzüglich erhaltene Prämienverbilligungen (605) → Total A (606)
- **Rein:** Krankenkassen-Prämienabrechnung (inkl. Kinder) → Code 601, netto nach verrechneter Prämienverbilligung · Police/Prämienrechnung → Unfall Code 602; Lebens-/Rentenversicherung Code 603 · Wertschriften- und Guthabenverzeichnis → Zinsen von Sparkapitalien Code 604 · Verfügung Prämienverbilligung (nicht verrechnet) → Code 605
- **Rechnen:** Σ 601 + 602 + 603 + 604 = Zwischentotal 607; − 605 (Prämienverbilligung, soweit nicht in 601) = Total A Code 606
- **Regel:** Tatsächlich bezahlte Prämien und Einlagen für Kranken-, Unfall-, Lebens- und Rentenversicherungen sowie Sparzinsen (gemäss Wertschriftenverzeichnis). Individuelle Prämienverbilligung (IPV) abziehen, soweit nicht bereits mit den Prämien des Krankenversicherers verrechnet (dann bereits reduzierte Prämie eintragen). Kinder: Prämien der unterhaltenen Personen einbeziehen.
- **Beachten:** Prämienverbilligung meist mit KK-Prämie verrechnet → reduzierte Prämie in 601, Code 605 dann leer
- **Beachten:** Prämien und Prämienverbilligungen der unterhaltenen Kinder einbeziehen
- **Beachten:** Nur tatsächlich bezahlte Prämien, Einlagen und Beiträge
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes 601, 602, 603, 604, 607 (Zwischentotal), 605, Total A 606
- **Quellen:**
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0079.md) `zh-wl-2026-uj__c0079` – «6. Abzüglich erhaltene Prämienverbilligungen 605»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0078.md) `zh-wl-2026-uj__c0078` – «Der zulässige Abzug für Versicherungsprämien und Sparzinsen ist im Formular Versicherungs-»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0080.md) `zh-wl-2026-uj__c0080` – «Prämienverbilligungen der Krankenversicherer, die für den Steuerpflichtigen und die von»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0079.md) `zh-wl-2026-uj__c0079` – «Tatsächlich bezahlte Einlagen, Prämien und Beiträge für private Kranken-, Unfall-, Lebens- und»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0002.md) `zh-form-365-2026-uj__c0002` – «A. Bezahlte Versicherungsprämien und Zinsen von Sparkapitalien 1. Private Krankenversicherungsprämien 601»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0002.md) `zh-form-365-2026-uj__c0002` – «4. Zinsen von Sparkapitalien 604»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0002.md) `zh-form-365-2026-uj__c0002` – «5. Zwischentotal 607»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0002.md) `zh-form-365-2026-uj__c0002` – «6. Abzüglich erhaltene Prämienverbilligungen 605»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0002.md) `zh-form-365-2026-uj__c0002` – «(soweit nicht schon unter Ziffer 1. berücksichtigt)»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0002.md) `zh-form-365-2026-uj__c0002` – «Total bezahlte Versicherungsprämien und Zinsen von Sparkapitalien (A) 606»

<a id="form-365-teil-b-ziff-1-3-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil B (Ziff. 1–3) – Maximaler Abzug für Versicherungsprämien und Sparzinsen (Codes 611–616)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand/Kinder aus Seite 1; Frage Beiträge 2. Säule/3a (Form. 300 S. 1 und Ziff. 14)
- **Rein:** Seite 1 Personalien → Zivilstand (611 Verheiratete / 612 Übrige) · Lohnausweis Ziff. 10 bzw. 3a-Bescheinigung → Beiträge 2. Säule/3a geleistet? (mit/ohne Vorsorge) · Form. 365 Teil A → Total bezahlte Prämien/Sparzinsen (A) für Teil C
- **Rechnen:** 616 = Grundbetrag 611/612 + Kinder × Kanton 1'300 / Bund 700 (613) + Unterstützte × Kanton 1'300 (614) / Bund 700 (615); 270 = min(A; B 616)
- **Regel:** Verheiratete (611): 5'800 Staat / 3'700 Bund, ohne Beiträge an 2. Säule oder 3a 8'700 / 5'550. Übrige (612): 2'900 / 1'800, ohne Vorsorgebeiträge 4'350 / 2'700. Zusatz je Kind (613) bzw. je unterstützungsbedürftige Person (614/615): 1'300 / 700. Total B = Code 616. Teil C: niedrigerer Betrag von A und B nach Ziff. 15 übertragen (Code 270).
- **Beachten:** Ohne-Vorsorge-Ansatz nur, wenn weder Steuerpflichtige noch Arbeitgeber Beiträge an 2. Säule/3a geleistet haben
- **Beachten:** Halber Kinderabzug: Zusatz nur 650 (Kanton) / 350 (Bund) je Kind
- **Beachten:** Teil A: erhaltene Prämienverbilligung abziehen (Code 605), sofern nicht schon in KK-Prämie verrechnet
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'800 (Versicherungsprämien und Sparzinsen (Staatssteuer), in ungetrennter Ehe lebende Steuerpflichtige mit Beiträgen an 2. Säule/Säule 3a: Fr. 5'800.)** · Bund **CHF 3'700 (Versicherungsprämien und Zinsen von Sparkapitalien, Ehepaare in ungetrennter Ehe, mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 3'700.)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 8'700 (Gemeinsam Besteuerte ohne Beiträge an 2. Säule und Säule 3a (weder durch Steuerpflichtige noch Arbeitgeber): Abzug erhöht sich um die Hälfte, höchstens Fr. 8'700.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an 2. Säule und Säule 3a: Höchstabzug CHF 5'550 (Erhöhung um die Hälfte).)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'900 (Versicherungsprämien und Sparzinsen (Staatssteuer), übrige Steuerpflichtige (nicht in ungetrennter Ehe) mit Vorsorgebeiträgen: Fr. 2'900.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 1'800.)**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 4'350 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: Abzug erhöht sich um die Hälfte, höchstens Fr. 4'350.)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: max. CHF 2'700.)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'300 (Zuschlag zum Versicherungsabzug: Fr. 1'300 für jedes Kind oder jede unterstützungsbedürftige Person mit Kinder-/Unterstützungsabzug nach § 34 Abs. 1; bei hälftig aufgeteiltem Kinderabzug Fr. 650.)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**
- **Bund:** Spalte Bundessteuer: 3'700 / 5'550 (Verheiratete), 1'800 / 2'700 (Übrige), 700 je Kind.
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes 611, 612, 613, 614 (Staat), 615 (Bund), Total B 616; Teil C 270 → Form. 300 Ziff. 15
- **Quellen:**
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0080.md) `zh-wl-2026-uj__c0080` – «oder: sofern weder Beiträge an die 2. noch an die 3. Säule a geleistet wurden 8’700 5’550»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0080.md) `zh-wl-2026-uj__c0080` – «Zusätzlicher Abzug für jedes Kind Anzahl: 1’300 700 613»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0081.md) `zh-wl-2026-uj__c0081` – «Der niedrigere Betrag: (A) oder (B) 270»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0081.md) `zh-wl-2026-uj__c0081` – «Wenn von den Steuerpflichtigen oder ihrem Arbeitgeber keine Beiträge an Einrichtun-»
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0087.md) `zh-wl-2026-uj__c0087` – «CHF 350 für jedes Kind, für das der steuerpflichtigen Person ein halber Kinderabzug zusteht.»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0079.md) `zh-wl-2026-uj__c0079` – «6. Abzüglich erhaltene Prämienverbilligungen 605»
  - [WL Lohnausweis 2026 S. 14](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0035.md) `bund-wl-lohnausweis-2026__c0035` – «Berufliche Vorsorge (2. Säule) Ziffer 10»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0003.md) `zh-form-365-2026-uj__c0003` – «die Beiträge an die 2. oder 3. Säule a geleistet haben 5’800 3’700»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0003.md) `zh-form-365-2026-uj__c0003` – «oder: sofern weder Beiträge an die 2. noch an die 3. Säule a geleistet wurden 8’700 5’550 611»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0003.md) `zh-form-365-2026-uj__c0003` – «die Beiträge an die 2. oder 3. Säule a geleistet haben 2’900 1’800»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0003.md) `zh-form-365-2026-uj__c0003` – «oder: sofern weder Beiträge an die 2. noch an die 3. Säule a geleistet wurden 4’350 2’700 612»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0003.md) `zh-form-365-2026-uj__c0003` – «Zusätzlicher Abzug für jedes Kind Anzahl: 1’300 700 613»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0003.md) `zh-form-365-2026-uj__c0003` – «Zusätzlicher Abzug für jede unterstützungsbed. Person Anzahl: 1’300 614»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0003.md) `zh-form-365-2026-uj__c0003` – «Zusätzlicher Abzug für jede unterstützungsbed. Person Anzahl: 700 615»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0003.md) `zh-form-365-2026-uj__c0003` – «Total der Abzüge für Versicherungsprämien und Zinsen von Sparkapitalien (B) 616»
  - [Formular 365 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-365-2026-uj/zh-form-365-2026-uj__c0003.md) `zh-form-365-2026-uj__c0003` – «Der niedrigere Betrag: (A) oder (B) 270»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «15. Versicherungsprämien, Zinsen von Sparkapitalien Versicherungsprämien 270»

## Hilfsblatt Weiterbildung

<a id="form-367-abzug-weiterbildung"></a>
### Ziff. Form. 367 – Berufsorientierte Aus- und Weiterbildungskosten: Total Kosten (2900/2903), Beitrag Arbeitgeber/Dritte (2901/2904), selbstgetragene Kosten (2902/2905), zulässiger Abzug (2920/2921) → Code 292

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Rechnungen; Lohnausweis Ziff. 13.3; Bestätigung Branchenverband/Bund
- **Rein:** Kursrechnungen/Zahlungsbelege → Total der Kosten 2900 / 2903 · Lohnausweis Ziff. 13.3; Bestätigung Bund/Branchenverband → Beiträge Dritter 2901 / 2904 · Ergebnis: zulässiger Abzug 2920 + 2921 → Ziff. 16.2 Code 292
- **Rechnen:** 2902/2905 = 2900/2903 − 2901/2904; 2920/2921 = min(selbstgetragen; je 12'600 Kanton / 13'000 Bund); 292 = 2920 + 2921
- **Regel:** Total der Kosten minus Beiträge des Arbeitgebers oder weiterer Stellen (Bund, Branchenverbände) = selbstgetragene Kosten; zulässiger Abzug getrennt für Staatssteuer (max. CHF 12'600) und Bundessteuer (max. CHF 13'000) je Person; Übertrag in Ziff. 16.2.
- **Beachten:** Höchstbetrag gilt je Person («max. je»), Zeilen Staats- und Bundessteuer getrennt
- **Beachten:** Voraussetzungen wie Ziff. 16.2: Sek.-II-Abschluss oder 20. Lebensjahr; Zeitpunkt Fälligkeit/Zahlung
- **Beachten:** AG-Vergütungen aus LA 13.3 stets als Beitrag Dritter abziehen (Rechnung auf Name AN immer bescheinigt)
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 12'600 (Berufsorientierte Aus- und Weiterbildungskosten inkl. Umschulung: bis Fr. 12'600 (Staatssteuer), sofern erster Abschluss Sekundarstufe II vorliegt oder das 20. Lebensjahr vollendet ist (und es nicht um Kosten bis zum ersten Abschluss Sek. II geht).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildungs- inkl. Umschulungskosten bis CHF 13'000 pro Jahr, sofern erster Abschluss Sek. II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)**
- **Bund:** Max. CHF 13'000 (Zeile Bundessteuer).
- **Bemerkung:** Personenzuordnung der Codes 2900–2905 (Spaltenfolge) am Original prüfen. Formular 2026 (UJ): bestaetigt; Codes 2900/2903, 2901/2904, 2902/2905, 2920/2921 (Person 1 / Person 2) → 292 (Form. 300 Ziff. 16.2)
- **Quellen:**
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0090.md) `zh-wl-2026-uj__c0090` – «Beitrag Arbeitgeber oder weiterer Stellen (Bund, Branchenverbände etc.) 2901 / 2904»
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0089.md) `zh-wl-2026-uj__c0089` – «Abschluss auf der Sekundarstufe II vorliegt oder das 20. Lebensjahr vollendet ist»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «Immer zu bescheinigen sind jedoch effektive Vergütungen für Rechnungen, die auf den Na»
  - [Formular 367 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-367-2026-uj/zh-form-367-2026-uj__c0001.md) `zh-form-367-2026-uj__c0001` – «Bezeichnung Person 1 Person 2 CHF ohne Rappen CHF ohne Rappen Total der Kosten 2900 / 2903»
  - [Formular 367 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-367-2026-uj/zh-form-367-2026-uj__c0001.md) `zh-form-367-2026-uj__c0001` – «Selbstgetragene Kosten 2902 / 2905»
  - [Formular 367 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-367-2026-uj/zh-form-367-2026-uj__c0001.md) `zh-form-367-2026-uj__c0001` – «Zulässiger Abzug (max. je CHF 12’600) 2920 / 2921»
  - [Formular 367 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-367-2026-uj/zh-form-367-2026-uj__c0001.md) `zh-form-367-2026-uj__c0001` – «Zulässiger Abzug (max. je CHF 13’000) 2920 / 2921»
  - [Formular 367 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-367-2026-uj/zh-form-367-2026-uj__c0001.md) `zh-form-367-2026-uj__c0001` – «Steuererklärung Seite 3 Ziffer 16.2 292»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «16.2 Berufsorientierte Aus- und Weiterbildungskosten Hilfsblatt 292»

## Einkommensberechnung

<a id="19-berechnung-total"></a>
### Ziff. 19 – Total der Einkünfte, Übertrag von Seite 2 Ziffer 7 (Code 199)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Übertrag Ziff. 7
- **Rein:** Seite 2 Ziff. 7 → Total der Einkünfte (Code 199)
- **Rechnen:** Code 199 = Ziff. 7 (Σ Ziff. 1–6, Seite 2) → Spalten Staats- und Bundessteuer
- **Regel:** Rechenzeile.
- **Beachten:** Unterjährige Steuerpflicht: keine eigene Umrechnung auf zwölf Monate – erfolgt für den Satz durch das Steueramt
- **Beachten:** Ziff. 4.2 (Code 151) ist «davon»-Angabe – nicht zusätzlich zu 4.1 addieren
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «19. Total der Einkünfte Übertrag von Seite 2, Ziffer 7 199»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «7. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 19 199»
  - [WL ZH 2026 UJ S. 6](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0011.md) `zh-wl-2026-uj__c0011` – «Die Umrechnung erfolgt durch das Steueramt.»

<a id="20-berechnung-total"></a>
### Ziff. 20 – Total der Abzüge, Übertrag von Ziffer 18 (Code 299)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Übertrag Ziff. 18
- **Rein:** Übertrag Ziff. 18 (Code 299)
- **Rechnen:** Ziff. 20 = Ziff. 18 (Code 299), je Spalte Staats-/Bundessteuer
- **Regel:** Rechenzeile.
- **Beachten:** Staats- und Bundessteuer-Total je in die eigene Spalte übertragen
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «20. Total der Abzüge Übertrag von Ziffer 18 299»

<a id="21-berechnung-total"></a>
### Ziff. 21 – Nettoeinkommen (Code 310)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ziff. 19 minus Ziff. 20
- **Rein:** Ziff. 19 (Code 199) und Ziff. 20 (Code 299)
- **Rechnen:** 310 = 199 − 299 (je Spalte); Basis für Selbstbehalt 5% (Ziff. 22.1) und Obergrenze 20% (Ziff. 22.2)
- **Regel:** Rechenzeile; Basis für den Selbstbehalt der Krankheitskosten (5%) und die Obergrenze der Zuwendungen (20%), je getrennt für Staats- und Bundessteuer.
- **Beachten:** Ziff. 21 kann je Spalte verschieden sein → Selbstbehalt und Spendenlimite je Spalte separat rechnen
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten sind abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen gemäss §§ 26-31 verminderten steuerbaren Einkünfte (laut Wegleitung: Nettoeinkommen, Ziff. 21). Diät-Pauschale Fr. 2'500 bei ärztlich angeordneter, lebensnotwendiger Diät.)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Zuwendungen insgesamt höchstens 20 % der um die Aufwendungen gemäss §§ 26-31 verminderten steuerbaren Einkünfte (Nettoeinkommen).)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «21. Nettoeinkommen 310»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0115.md) `zh-wl-2026-uj__c0115` – «Gesetz erwähnten Selbstbehalt von 5% des Nettoeinkommens (Ziffer 21 der Steuererklärung)»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0120.md) `zh-wl-2026-uj__c0120` – «die Zuwendungen in der Steuerperiode CHF 100 erreichen und soweit sie insgesamt 20%»

<a id="22-1-abzug-krankheitskosten"></a>
### Ziff. 22.1 – Krankheits- und Unfallkosten (Code 320)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Aufstellung über Krankheits- und Unfallkosten (Form. 370) Teil E Abzug; Leistungsabrechnungen der Krankenkasse (Selbstbehalt/Franchise)
- **Rein:** Form. 370 Teil E → Abzug Code 320 je Spalte · Leistungsabrechnungen/Kostenzusammenstellung Krankenkasse → Selbstbehalt/Franchise, Rückvergütungen · Rechnungen Arzt, Medikamente, Zahnarzt, Spital, Therapien, Pflege → Form. 370 Teil A
- **Rechnen:** 320 = Auslagen netto 313 − Selbstbehalt 319 (5% × Ziff. 21, Code 310), nur positiver Rest; Staats- und Bundessteuer getrennt
- **Regel:** Selbst getragene Kosten für sich und unterhaltene Personen, soweit sie 5% des Nettoeinkommens (Ziff. 21) übersteigen (Staats- und Bundessteuer je getrennt). Formular Form. 370 vollständig ausfüllen, Belege geordnet beilegen. Nicht abziehbar: Prävention (Fitness), Fahrkosten zum Arzt, Akupunktur ohne Verordnung, eigene Pflegeleistungen, Schlankheits-/Wellness-/Schönheitsbehandlungen, Psychoanalysen. Ärztlich angeordnete Diät: Mehrkosten oder Pauschale CHF 2'500.
- **Beachten:** Nicht abziehbar: Fitness, Wellness, nicht verordnete Akupunktur; Arztfahrten (Ausn. Ambulanz, auswärtige Kur/Therapie)
- **Beachten:** KK-Prämien gehören ins Hilfsblatt Versicherungsprämien Teil A (Ziff. 15), nicht hierher
- **Beachten:** Heim ohne Behinderung: Pflege-/Medizinkosten hier; mit Behinderung → Ziff. 16.4 (ohne Selbstbehalt)
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten sind abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen gemäss §§ 26-31 verminderten steuerbaren Einkünfte (laut Wegleitung: Nettoeinkommen, Ziff. 21). Diät-Pauschale Fr. 2'500 bei ärztlich angeordneter, lebensnotwendiger Diät.)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
- **Quellen:**
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0115.md) `zh-wl-2026-uj__c0115` – «Gesetz erwähnten Selbstbehalt von 5% des Nettoeinkommens (Ziffer 21 der Steuererklärung)»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0116.md) `zh-wl-2026-uj__c0116` – «wollen, müssen mit der Steuererklärung das vollständig ausgefüllte Formular «Aufstellung über»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0119.md) `zh-wl-2026-uj__c0119` – «CHF 2500 geltend gemacht wer-»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0120.md) `zh-wl-2026-uj__c0120` – «abzüglich Selbstbehalt (5% von Ziffer 21 der»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «21. Nettoeinkommen 310»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0007.md) `zh-zstb-32-1__c0007` – «Auslagen für Ambulanzen oder Fahrten zu auswärtigen Kuren oder Therapien»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0078.md) `zh-wl-2026-uj__c0078` – «1. Private Krankenversicherungsprämien»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0008.md) `zh-zstb-32-1__c0008` – «so können im Rahmen des Abzugs der Krankheits- und Unfallkosten die Kosten für Pflege- und medizinische Leistungen»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0017.md) `zh-zstb-32-1__c0017` – «In der Steuererklärung sind die behinderungsbedingten Kosten in Ziffer 16.4 und die Krankheits- und Unfallkosten in Ziffer 22.1 einzutragen.»

<a id="22-2-abzug-spenden"></a>
### Ziff. 22.2 – Gemeinnützige Zuwendungen (Code 324)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigungen / Aufstellung über gemeinnützige Zuwendungen (Empfänger, Betrag)
- **Rein:** Spendenbestätigungen der Empfänger → Betrag je Zuwendung (Geld oder übrige Vermögenswerte) · Aufstellung über gemeinnützige Zuwendungen (Empfänger, Betrag) → beilegen · Ziff. 21 Nettoeinkommen (Code 310) → Basis 20%-Grenze
- **Rechnen:** wenn Σ Zuwendungen ≥ 100: Abzug = min(Σ; 20% × Ziff. 21), je Spalte Staats-/Bundessteuer → Code 324
- **Regel:** Freiwillige Leistungen an Bund, Kantone, Gemeinden und deren Anstalten sowie an steuerbefreite juristische Personen mit Sitz in der Schweiz mit öffentlichen oder ausschliesslich gemeinnützigen Zwecken; abziehbar, wenn die Zuwendungen in der Steuerperiode mindestens CHF 100 erreichen und insgesamt höchstens 20% des Nettoeinkommens (Ziff. 21) ausmachen. Aufstellung beilegen. Keine Mitgliederbeiträge mit Gegenleistung; Parteispenden gehören zu Ziff. 16.5.
- **Beachten:** Empfänger: Bund/Kantone/Gemeinden + Anstalten; jur. Personen mit Sitz CH, steuerbefreit (öffentl./gemeinnützig)
- **Beachten:** Beiträge an politische Parteien separat unter Ziff. 16.5 (Code 284)
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentliche/gemeinnützige Zwecke): Abzug, wenn die Zuwendungen in der Steuerperiode mindestens Fr. 100 erreichen.)** · Bund **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn im Steuerjahr mindestens CHF 100 erreicht.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Zuwendungen insgesamt höchstens 20 % der um die Aufwendungen gemäss §§ 26-31 verminderten steuerbaren Einkünfte (Nettoeinkommen).)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**
- **Bund:** Gleiche Regel (mind. CHF 100, max. 20% des Nettoeinkommens).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «22.2 Gemeinnützige Zuwendungen Aufstellung 324»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0120.md) `zh-wl-2026-uj__c0120` – «des Nettoeinkommens (Ziffer 21 der Steuererklärung) nicht übersteigen.»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0120.md) `zh-wl-2026-uj__c0120` – «Wir bitten Sie, der Steuererklärung eine Aufstellung über gemeinnützige Zuwendungen bei-»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0119.md) `zh-wl-2026-uj__c0119` – «Abzugsberechtigt sind die freiwilligen Leistungen von Geld und übrigen Vermögenswerten an»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «21. Nettoeinkommen 310»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «16.5 Weitere Abzüge (z.B. Beiträge an politische Parteien) Aufstellung 284»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0120.md) `zh-wl-2026-uj__c0120` – «und an andere juristische Personen mit Sitz in der Schweiz, die im Hinblick auf öffentliche»

<a id="23-berechnung-total"></a>
### Ziff. 23 – Reineinkommen (Ziffer 21 abzüglich Ziffern 22.1 und 22.2) (Code 350)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ziff. 21 minus 22.1 minus 22.2
- **Rein:** Ziff. 21 (Code 310), Ziff. 22.1 (Code 320), Ziff. 22.2 (Code 324)
- **Rechnen:** 350 = 310 − 320 − 324 (je Spalte Staats-/Bundessteuer)
- **Regel:** Rechenzeile; Basis für Sozialabzüge.
- **Beachten:** Je Spalte rechnen: 22.1/22.2 hängen vom spaltenweisen Nettoeinkommen Ziff. 21 ab
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «(Ziffer 21 abzüglich Ziffern 22.1 und 22.2) 350»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0113.md) `zh-wl-2026-uj__c0113` – «22.1 Krankheits- und Unfallkosten Hilfsblatt 320»

<a id="24-1-sozialabzug-kinder"></a>
### Ziff. 24.1 – Abzug für Kinder in Ihrem Haushalt (Code 370) und ausserhalb Ihres Haushaltes (Code 372)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien Kinder Seite 1 (Geburtsjahr, Ausbildung, elterliche Sorge, Alimente)
- **Rein:** Seite 1 Kinderangaben → Jahrgang, Haushalt, elterliche Sorge, Alimente · Ausbildungsbestätigung/Lehrvertrag → volljährige Kinder in beruflicher Erstausbildung · Ziff. 5.2 erhaltene bzw. 13.2 bezahlte Kinderalimente → ganzer, halber oder kein Abzug
- **Rechnen:** Anzahl Kinder × 9'400 Kanton / 6'800 Bund (halb: 4'700 / 3'400) → Code 370 (im Haushalt) / 372 (ausserhalb); unterjährig × Tage : 360
- **Regel:** Staatssteuer CHF 9'400 pro Kind, Bundessteuer CHF 6'800 pro Kind für Kinder, die am 31.12.2026 minderjährig sind (Jahrgänge 2009–2026), oder volljährig in beruflicher Erstausbildung mit Unterhalt zur Hauptsache. Ehepaar/Verwitwete: ganzer Abzug. Alleinerziehend: ganzer Abzug bei alleiniger Sorge oder bei gemeinsamer Sorge mit erhaltenen Alimenten; halber Abzug (CHF 4'700 / 3'400) bei gemeinsamer Sorge ohne erhaltene Alimente. Getrennt lebender Elternteil: halber Abzug bei gemeinsamer Sorge ohne eigene Alimentenzahlung; bei Alimentenabzug oder ohne Sorge kein Kinderabzug. Konkubinat: ganzer Abzug nur bei alleiniger Sorge oder gemeinsamer Sorge mit erhaltenen Alimenten, sonst je halber; volljährige Kinder: Abzug beim Elternteil mit höherem Beitrag. Sozialabzüge nach Verhältnissen am Ende der Steuerperiode bzw. Steuerpflicht; bei unterjähriger Steuerpflicht anteilmässig.
- **Beachten:** Stichtag 31. Dezember 2026 bzw. Ende Steuerpflicht; minderjährig = Jg. 2009–2026; Pflegekinder: kein Kinderabzug
- **Beachten:** Kanton: volljähriges Kind gilt als selbsterhaltend bei Einkommen ≥ 25'000 oder liquidem Vermögen ≥ 100'000
- **Beachten:** Alimente zahlender Elternteil (minderjährige Kinder): kein Kinderabzug, dafür Ziff. 13.2
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 9'400 (Kinderabzug je Kind (minderjährig unter elterlicher Sorge/Obhut oder volljährig in beruflicher Erstausbildung, Unterhalt zur Hauptsache): Fr. 9'400. Bei nicht gemeinsam besteuerten Eltern hälftig aufgeteilt (Fr. 4'700), wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge für das Kind abgezogen werden.)** · Bund **CHF 6'800 (Kinderabzug CHF 6'800 pro minderjähriges oder in beruflicher/schulischer Ausbildung stehendes Kind, für dessen Unterhalt die steuerpflichtige Person sorgt; bei getrennter Besteuerung der Eltern hälftig bei gemeinsamer elterlicher Sorge ohne Unterhaltsbeiträge.)**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 9'400 (Volljährige Kinder in beruflicher Erstausbildung, deren Unterhalt zur Hauptsache bestritten wird: gleicher Kinderabzug Fr. 9'400.)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Abzug CHF 6'800 (kein höherer Ausbildungsabzug beim Bund).)**
- **Bund:** CHF 6'800 pro Kind (halber Abzug CHF 3'400) statt CHF 9'400 (halber Abzug CHF 4'700).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «24.1 Abzug für Kinder in Ihrem Haushalt (gemäss Seite 1) 9’400»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0124.md) `zh-wl-2026-uj__c0124` – «CHF 9’400 pro Kind CHF 6’800 pro Kind»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0125.md) `zh-wl-2026-uj__c0125` – «das am 31. Dezember 2026 minderjährig ist»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0126.md) `zh-wl-2026-uj__c0126` – «pro Kind (CHF 4’700) pro Kind (CHF 3’400)»
  - [StG ZH § 34](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-34.md) `zh-stg-2026__par-34` – «je Fr. 9400»
  - [WL ZH 2026 UJ S. 37](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0237.md) `zh-wl-2026-uj__c0237` – «18’800 : 360 x 150 = 7’833»
  - [ZStB 34.1](../../chunks/zh/dauernd/zh-zstb-34-1/zh-zstb-34-1__c0006.md) `zh-zstb-34-1__c0006` – «Erzielt das Kind ein steuerbares Einkommen von mindestens Fr. 25 000»
  - [ZStB 34.1](../../chunks/zh/dauernd/zh-zstb-34-1/zh-zstb-34-1__c0007.md) `zh-zstb-34-1__c0007` – «Für Pflegekinder kann kein Kinderabzug gewährt werden.»
  - [WL ZH 2026 UJ S. 19](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0127.md) `zh-wl-2026-uj__c0127` – «leisten Sie Unterhaltszahlungen für das Kind, so»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0007.md) `zh-form-300-2026-uj__c0007` – «13.2 Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit)»
  - [StG ZH § 34](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-34.md) `zh-stg-2026__par-34` – «werden nach den Verhältnissen am Ende der Steuerperiode oder der Steuerpflicht festgelegt.»
  - [StG ZH § 34](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-34.md) `zh-stg-2026__par-34` – «Bei teilweiser Steuerpflicht werden die Sozialabzüge gemäss Abs. 1 anteilmässig gewährt.»
  - [KS 30 S. 19](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0057.md) `bund-ks-30__c0057` – «Pflegeeltern wird für ihre Pflegekinder hingegen kein Kinderabzug gewährt.»

<a id="24-2-sozialabzug-unterstuetzung"></a>
### Ziff. 24.2 – Abzug für unterstützte Personen (Code 374)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der Unterstützung; auf Verlangen Zahlungsbelege (bei Auslandzahlungen Post-/Bankbelege)
- **Rein:** Bestätigung der unterstützten Person → Art, Zeitpunkt und Höhe der Unterstützung · Zahlungsbelege auf Verlangen (Ausland: Post-/Bankbelege, Barquittungen grundsätzlich nicht) → Nachweis · Aufstellung über Unterstützungsleistungen → beilegen
- **Rechnen:** je Person: Kanton 2'800 (wenn Unterstützung ≥ 2'800) / Bund 6'800 (wenn ≥ 6'800) → Code 374; unterjährig × Tage : 360
- **Regel:** Für erwerbsunfähige oder beschränkt erwerbsfähige, finanziell unterstützungsbedürftige Personen. Nicht für Leistungen an den Ehegatten, an Kinder mit Kinderabzug, oder wenn für dieselbe Person Alimente abgezogen werden. Staatssteuer CHF 2'800 (Unterstützung mind. in dieser Höhe), Bundessteuer CHF 6'800 (Unterstützung mind. in dieser Höhe).
- **Beachten:** Ausgeschlossen: Ehegatte, Kinder mit Kinderabzug, Person mit Alimentenabzug; Ehepaar nur 1 Abzug je Person
- **Beachten:** Kanton: bedürftig i.d.R. bei Einkommen < 15'000 und Vermögen < 50'000 (verheiratet < 22'000 / < 100'000)
- **Beachten:** Arbeitslosigkeit ≠ Erwerbsunfähigkeit; Zusatz Form. 365: Kanton 1'300 (614) / Bund 700 (615) je Person
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'800 (Unterstützungsabzug für erwerbsunfähige oder beschränkt erwerbsfähige Personen, an deren Unterhalt mindestens in Höhe des Abzugs beigetragen wird: Fr. 2'800 je Person. Nicht für Ehegatten und Kinder mit Kinderabzug oder Unterhaltsbeitragsabzug.)** · Bund **CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)**
- **Bund:** Abzug und Mindestunterstützung CHF 6'800 (statt CHF 2'800).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «24.2 Abzug für unterstützte Personen Bestätigung»
  - [WL ZH 2026 UJ S. 20](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0133.md) `zh-wl-2026-uj__c0133` – «Der Abzug kann nicht gewährt werden:»
  - [WL ZH 2026 UJ S. 20](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0134.md) `zh-wl-2026-uj__c0134` – «des Unterstützungsabzuges von CHF 2’800»
  - [ZStB 34.1](../../chunks/zh/dauernd/zh-zstb-34-1/zh-zstb-34-1__c0016.md) `zh-zstb-34-1__c0016` – «Steuerbares Einkommen von weniger als Fr. 15 000 und steuerbares Vermögen von weniger als Fr. 50 000»
  - [ZStB 34.1](../../chunks/zh/dauernd/zh-zstb-34-1/zh-zstb-34-1__c0016.md) `zh-zstb-34-1__c0016` – «Steuerbares Einkommen von weniger als Fr. 22 000 und steuerbares Vermögen von weniger als Fr. 100 000»
  - [ZStB 34.1](../../chunks/zh/dauernd/zh-zstb-34-1/zh-zstb-34-1__c0015.md) `zh-zstb-34-1__c0015` – «Arbeitslosigkeit oder reduzierte Arbeitstätigkeit ist nicht mit Erwerbsunfähigkeit oder beschränkter Erwerbsfähigkeit gleichzustellen.»
  - [ZStB 34.1](../../chunks/zh/dauernd/zh-zstb-34-1/zh-zstb-34-1__c0018.md) `zh-zstb-34-1__c0018` – «können für die gleiche unterstützungsbedürftige Person nur einen Unterstützungsabzug beanspruchen.»
  - [ZStB 34.1](../../chunks/zh/dauernd/zh-zstb-34-1/zh-zstb-34-1__c0018.md) `zh-zstb-34-1__c0018` – «Quittungen über Barzahlungen an Personen mit Wohnsitz im Ausland können grundsätzlich nicht als Beweismittel»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0080.md) `zh-wl-2026-uj__c0080` – «Zusätzlicher Abzug für jede unterstützungsbed. Person Anzahl: 1’300 614»
  - [WL ZH 2026 UJ S. 37](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0237.md) `zh-wl-2026-uj__c0237` – «18’800 : 360 x 150 = 7’833»
  - [WL ZH 2026 UJ S. 31](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0219.md) `zh-wl-2026-uj__c0219` – «Aufstellung über Unterstützungsleistungen»
  - [WL ZH 2026 UJ S. 20](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0133.md) `zh-wl-2026-uj__c0133` – «für Leistungen an Kinder, für die ein Kinderabzug gewährt wird;»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0080.md) `zh-wl-2026-uj__c0080` – «Anzahl: 700 615 3211»
  - [StG ZH § 34](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-34.md) `zh-stg-2026__par-34` – «Bei teilweiser Steuerpflicht werden die Sozialabzüge gemäss Abs. 1 anteilmässig gewährt.»

<a id="24-3-sozialabzug-verheiratete"></a>
### Ziff. 24.3 – Abzug für Ehegatten/Partner – nur Bundessteuer (Code 365)

- **Schlüssel:** `sozialabzug.verheiratete` (Verheiratetenabzug (Bund)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand (rechtlich und tatsächlich ungetrennte Ehe/Partnerschaft)
- **Rein:** Seite 1 Zivilstand → rechtlich und tatsächlich ungetrennte Ehe/Partnerschaft
- **Rechnen:** Bund 2'800 → Code 365; Kanton: kein Abzug (Staatssteuer-Feld «—»); unterjährig × Tage : 360
- **Regel:** Nur bei der direkten Bundessteuer: Verheiratetenabzug CHF 2'800 für alle in rechtlich und tatsächlich ungetrennter Ehe Lebenden; bei der Staatssteuer keine Zeile (Staatssteuer-Spalte leer).
- **Beachten:** Staatssteuer-Spalte leer lassen
- **Beachten:** Massgebend: Verhältnisse am Ende der Steuerperiode bzw. der Steuerpflicht
- **Limiten:**
  - Verheiratetenabzug (CHF, Bund): Kanton **n/a** · Bund **CHF 2'800 (Verheiratetenabzug CHF 2'800 für Ehepaare in rechtlich und tatsächlich ungetrennter Ehe.)**
- **Bund:** Verheiratetenabzug CHF 2'800 (nur Bund).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «24.3 Abzug für Ehegatten / Partn.»
  - [WL ZH 2026 UJ S. 20](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0134.md) `zh-wl-2026-uj__c0134` – «Steuerpflichtigen einen Verheiratetenabzug von CHF 2’800.»
  - [WL ZH 2026 UJ S. 37](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0237.md) `zh-wl-2026-uj__c0237` – «18’800 : 360 x 150 = 7’833»
  - [DBG Art. 35](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-35.md) `bund-dbg-2026__art-35` – «Die Sozialabzüge werden nach den Verhältnissen am Ende der Steuerperiode (Art. 40) oder der Steuerpflicht festgesetzt.»
  - [DBG Art. 35](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-35.md) `bund-dbg-2026__art-35` – «Bei teilweiser Steuerpflicht werden die Sozialabzüge anteilsmässig gewährt.»

<a id="25-berechnung-total"></a>
### Ziff. 25 – Steuerbares Einkommen gesamt (Ziffer 23 abzüglich Ziff. 24.1 bis 24.3) (Code 390)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ziff. 23 minus Ziff. 24
- **Rein:** Ziff. 23 (Code 350) und Ziff. 24.1–24.3 (Codes 370, 372, 374, 365)
- **Rechnen:** 390 = 350 − (370 + 372 + 374 + 365), je Spalte Staats-/Bundessteuer
- **Regel:** Rechenzeile.
- **Beachten:** Steuerpflicht auch in anderen Kantonen/Ausland: weiter Ziff. 26.1/26.2 (394/396) → Ziff. 27 (398)
- **Beachten:** Steuerausscheidung nimmt das Steueramt vor, sofern nicht mit der Steuererklärung eingereicht
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «25. Steuerbares Einkommen gesamt (Ziffer 23 abz. Ziff. 24.1 bis 24.3) 390»
  - [WL ZH 2026 UJ S. 6](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0011.md) `zh-wl-2026-uj__c0011` – «Das Steueramt nimmt die erforderliche Ausscheidung vor, soweit eine solche nicht mit der»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «(Ziffer 21 abzüglich Ziffern 22.1 und 22.2) 350»

<a id="26-1-26-2-berechnung-total"></a>
### Ziff. 26.1 / 26.2 – Auf steuerbare Einkünfte in anderen Kantonen (Code 394) / im Ausland (Code 396) entfallender Anteil

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ausscheidung aus Liegenschaften/Geschäftsbetrieben/Betriebsstätten ausserhalb ZH
- **Rein:** Übertrag aus Ziff. 25 (Code 390) → aufzuteilender Gesamtbetrag · Eigene Steuerausscheidung (falls eingereicht) → Anteil andere Kantone (394) / Ausland (396) · Liegenschaftenverzeichnis → Erträge ausserkantonaler/ausländischer Liegenschaften
- **Rechnen:** Anteil von Code 390, der gemäss Steuerausscheidung auf Einkünfte in anderen Kantonen (394) bzw. im Ausland (396) entfällt
- **Regel:** Nur bei interkantonaler/internationaler Steuerausscheidung ausfüllen (Staatssteuer); sonst leer.
- **Beachten:** Trotzdem gesamtes in- und ausländisches Einkommen in Ziff. 1–25 deklarieren
- **Beachten:** Ohne eingereichte Ausscheidung nimmt das Steueramt sie vor
- **Beachten:** 26.1 nur Spalte Staatssteuer, 26.2 Staats- und Bundessteuer (Formular S. 3)
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «26.1 Auf steuerbare Einkünfte in anderen Kantonen 394»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «26.2 Auf steuerbare Einkünfte im Ausland 396»
  - [WL ZH 2026 UJ S. 6](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0011.md) `zh-wl-2026-uj__c0011` – «gesamte in- und ausländische Einkommen und Vermögen zu deklarieren.»
  - [WL ZH 2026 UJ S. 6](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0011.md) `zh-wl-2026-uj__c0011` – «Das Steueramt nimmt die erforderliche Ausscheidung vor, soweit eine solche nicht mit der»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0173.md) `zh-wl-2026-uj__c0173` – «Es sind alle Liegenschaften zu deklarieren, auch jene in anderen Kantonen oder»

<a id="27-berechnung-total"></a>
### Ziff. 27 – Steuerbares Einkommen im Kanton Zürich bzw. in der Schweiz (Code 398)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ziff. 25 minus Ziff. 26
- **Rein:** Übertrag aus Ziff. 25 (Code 390) · Übertrag aus Ziff. 26.1 / 26.2 (Codes 394 / 396)
- **Rechnen:** Code 398 = 390 − 394 − 396, je Spalte Staatssteuer und Bundessteuer (Bund ohne 26.1)
- **Regel:** Rechenzeile; Grundlage der Steuerberechnung.
- **Beachten:** Unterjährige Steuerpflicht: Umrechnung regelmässiger Einkünfte auf zwölf Monate (Satz) macht das Steueramt
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «27. Steuerbares Einkommen im Kanton Zürich bzw. in der Schweiz 398»
  - [WL ZH 2026 UJ S. 6](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0011.md) `zh-wl-2026-uj__c0011` – «Für das satzbestimmende Einkommen werden die regelmässig fliessenden Einkünfte auf»

## Hilfsblatt Krankheitskosten

<a id="form-370-teil-a-e-abzug-krankheitskosten"></a>
### Ziff. Form. 370 Teil A–E – Aufstellung über Krankheits- und Unfallkosten: A Aufwendungen (300–307, Total 317), B Vergütungen Dritter (308, 311, 312, Total 318), C Auslagen netto (314), D Pauschale (315), E Berechnung (313, Selbstbehalt 319, Abzug 320)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung, Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung) → Zeilen 1 Selbstbehalt/Franchise lt. Krankenkassenabrechnung (300); 2 Arzt und Medikamente (301); 3 Zahnarzt (302); 4 Pflegepersonal (303); 5 Spital/Heilstätten (304); 6 Therapien/Kuren (305)
- **Rein:** Leistungsabrechnung Krankenkasse → Selbstbehalt/Franchise 300; Versicherungsleistungen 308 (soweit nicht in A gekürzt) · Rechnungen → Arzt/Medikamente 301, Zahnarzt 302, Pflegepersonal 303, Spital 304, Therapien/Kuren 305 · Heim-/Spitalrechnung → Anteil Lebenshaltungskosten 311 · Arztzeugnis andauernde Diät → Pauschale D 315
- **Rechnen:** 317 = Σ 300–305 + 307; 318 = 308 + 311 + 312; 314 = 317 − 318; 313 = 314 und/oder 315; 319 = 5% × Ziff. 21; 320 = 313 − 319 (nur positiv), je Spalte
- **Regel:** Aufwendungen (A) abzüglich Vergütungen Dritter inkl. Anteil Lebenshaltungskosten bei Heim-/Spitalaufenthalt (B) = Auslagen netto (C); bei andauernder lebensnotwendiger Diät statt effektiv Pauschale (D). Davon wird in Teil E der Selbstbehalt (5% des Nettoeinkommens Ziff. 21, Staats- und Bundessteuer getrennt) abgezogen; Ergebnis Code 320 nach Ziff. 22.1. Krankenkassen stellen auf Verlangen Kosten- und Prämienzusammenstellungen aus.
- **Beachten:** Lebensnotwendige Dauerdiät (z.B. Zöliakie): Pauschale CHF 2'500 statt effektiver Mehrkosten
- **Beachten:** Kosten mehrerer Personen addieren; nur eine Aufstellung pro Steuererklärung; Belege geordnet beilegen
- **Beachten:** Abziehbar auch medizinische Apparate und Korrekturgläser
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten sind abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen gemäss §§ 26-31 verminderten steuerbaren Einkünfte (laut Wegleitung: Nettoeinkommen, Ziff. 21). Diät-Pauschale Fr. 2'500 bei ärztlich angeordneter, lebensnotwendiger Diät.)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes 300–305, 307, 317; 308, 311, 312, 318; 314; 315; 313, 319, 320 → Form. 300 UJ 2026 Ziff. 22.1
- **Quellen:**
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0117.md) `zh-wl-2026-uj__c0117` – «1. Selbstbehalt gemäss Abrechnung Krankenkasse und Versicherung 300»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0120.md) `zh-wl-2026-uj__c0120` – «abzüglich Selbstbehalt (5% von Ziffer 21 der»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0118.md) `zh-wl-2026-uj__c0118` – «2. Anteil Lebenshaltungskosten (z. B. Ernährung) 311»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0119.md) `zh-wl-2026-uj__c0119` – «Total der Vergütungen Dritter (B) 318»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0001.md) `zh-form-370__c0001` – «Pro Steuererklärung ist nur eine Aufstellung einzureichen.»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0006.md) `zh-zstb-32-1__c0006` – «Medizinische Apparate, Korrekturgläser etc.»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «22.1 Krankheits- und Unfallkosten Hilfsblatt 32013213211»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «1. Selbstbehalt gemäss Abrechnung Krankenkasse und Versicherung 300»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «Total der Vergütungen Dritter (B) 318»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «Total der Auslagen (C und / oder D) 313»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «Abzug 320 113211 113211»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «Seite 3, Ziffer 22.1»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «StA Form. 370 (2020) 12.20»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben (Code 400)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Wertschriften- und Guthabenverzeichnis (Form. 340) Total Steuerwert per 31.12.2026; eSteuerauszug der Bank (Steuerwert 31.12.)
- **Rein:** Wertschriften- und Guthabenverzeichnis (Form. 340) → Total Steuerwert (Code 400) · eSteuerauszug Bank → Steuerwerte (Import in Online-Steuererklärung) · Konto-/Sparheft-/Salärkontoauszug → Saldo per Stichtag (voller Forderungsbetrag) · Krypto-Auszug → Marktwert per Stichtag
- **Rechnen:** Σ Steuerwerte aller Wertschriften und Guthaben per 31.12.2026 bzw. Ende Steuerpflicht = Code 400; Fremdwährung zum Devisenkurs, Krypto zum Marktwert
- **Regel:** Total Steuerwert aus dem Wertschriftenverzeichnis. Guthaben zum vollen Forderungsbetrag; Fremdwährung zu Devisenkursen; Kryptowährungen zum Marktwert. Nutzniessungsvermögen beim Nutzniesser. Ansprüche an Vorsorgeeinrichtungen (2. Säule, 3a, Freizügigkeit) sind steuerfrei und nicht aufzuführen. Bei Ende der Steuerpflicht Stichtag-Werte.
- **Beachten:** Inkl. Vermögen minderjähriger Kinder Jg. 2009 und jünger und Nutzniessungsvermögen; Jg. 2008 und älter selbst
- **Beachten:** Vorsorgeansprüche 2. Säule und Säule 3a bis Fälligkeit steuerfrei → nicht aufführen
- **Beachten:** Ende Steuerpflicht (Tod/Wegzug): Stichtag Todes-/Wegzugstag, kotierte Titel zum Tageskurs
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0011.md) `zh-form-300-2026-uj__c0011` – «30.1 Wertschriften und Guthaben Wertschriftenverzeichnis 400»
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0158.md) `zh-wl-2026-uj__c0158` – «Kryptowährungen wie Bitcoin sind zum Marktwert zu deklarieren.»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0155.md) `zh-wl-2026-uj__c0155` – «Leistungen steuerfrei und nicht im Wertschriftenverzeichnis aufzuführen.»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0154.md) `zh-wl-2026-uj__c0154` – «minderjährigen Kinder des Jahrgangs 2009 und jüngeren sowie das Vermögen, an dem Sie»
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0158.md) `zh-wl-2026-uj__c0158` – «Guthaben sind mit dem vollen Forderungsbetrag anzugeben.»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0153.md) `zh-wl-2026-uj__c0153` – «Online-Steuererklärung importieren und müssen die darin enthaltenen Angaben nicht mehr ins»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0157.md) `zh-wl-2026-uj__c0157` – «Kotierte Wertpapiere sind zum Tageskurs anzugeben.»
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0159.md) `zh-wl-2026-uj__c0159` – «Für den Wert des Vermögens gilt der Todestag bzw. der Tag des Wegzugs als massgebender»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0152.md) `zh-wl-2026-uj__c0152` – «Wenn Sie Wertschriften oder Guthaben besitzen, wozu unter anderem auch Sparhefte, Salär»
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0158.md) `zh-wl-2026-uj__c0158` – «Auf ausländische Währung lautende Guthaben sind zu»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 404)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bestandesaufstellung per 31.12.; Kurswert (ausländische Noten/Münzen/Edelmetalle zum Tageskurs)
- **Rein:** Eigene Bestandesaufnahme → Bargeld in CHF per Stichtag · Devisen-/Edelmetallkurse → Tageskurs für ausländische Noten, Goldmünzen, Edelmetalle
- **Rechnen:** Σ Bargeld CHF + Σ (Menge × Tageskurs) ausländische Noten/Goldmünzen/Edelmetalle, per 31.12.2026 bzw. Ende Steuerpflicht = Code 404
- **Regel:** Ausländische Banknoten, Goldmünzen und Edelmetalle zum Tageskurs; Bargeld per Stichtag.
- **Beachten:** Bank-, Spar- und Salärkonti nicht hier, sondern im Wertschriftenverzeichnis (Ziff. 30.1)
- **Beachten:** Kryptowährungen zum Marktwert im Wertschriftenverzeichnis, nicht hier
- **Quellen:**
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0137.md) `zh-wl-2026-uj__c0137` – «Ausländische Banknoten, Goldmünzen und Edelmetalle sind zum Tageskurs anzugeben.»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0011.md) `zh-form-300-2026-uj__c0011` – «Steuerwert per 31.12.2026 bzw. per Ende der Steuerpflicht»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0152.md) `zh-wl-2026-uj__c0152` – «Wenn Sie Wertschriften oder Guthaben besitzen, wozu unter anderem auch Sparhefte, Salär»
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0158.md) `zh-wl-2026-uj__c0158` – «Kryptowährungen wie Bitcoin sind zum Marktwert zu deklarieren.»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen (Steuerwert gem. Bescheinigung der Versicherungsgesellschaft) (Code 406)

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Steuerwert-Bescheinigung der Versicherungsgesellschaft (Gesellschaft, Abschlussjahr, Ablaufsjahr, Steuerwert)
- **Rein:** Steuerwertbescheinigung der Versicherungsgesellschaft → Steuerwert (Gesellschaft, Abschluss-, Ablaufsjahr)
- **Rechnen:** Σ bescheinigte Steuerwerte aller rückkaufsfähigen Lebens-/Rentenversicherungen = Code 406; Bescheinigung beilegen
- **Regel:** Rückkaufsfähige Lebens- und Rentenversicherungen: Steuerwert gemäss Bescheinigung (beilegen), auch nach Rentenbeginn bei rückkaufsfähigen Rentenversicherungen. Nicht rückkaufsfähige Renten (nach Rentenbeginn): kein Vermögen. Säule-3a-Policen bis Fälligkeit steuerfrei (nicht aufführen).
- **Beachten:** Säule-3a-Policen bis Fälligkeit steuerfrei → nicht aufführen
- **Beachten:** Rentenversicherung: nach Rentenbeginn nur, wenn rückkaufsfähig (Rückkaufswert)
- **Quellen:**
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0138.md) `zh-wl-2026-uj__c0138` – «Der Vermögenssteuerwert von Lebensversicherungen richtet sich nach dem Steuerwert. Dabei»
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0138.md) `zh-wl-2026-uj__c0138` – «abgeschlossene Vorsorgepolicen sind bis zur Fälligkeit der Versicherungssumme steuerfrei.»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0011.md) `zh-form-300-2026-uj__c0011` – «30.3 Lebens- und Rentenversicherungen (Steuerwert gem. Bescheinigung der Versicherungsges.)»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge (Kaufpreis, Kaufjahr) (Code 412)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Kaufvertrag/Fahrzeugausweis (Kaufpreis und Kaufjahr)
- **Rein:** Kaufvertrag/Rechnung → Kaufpreis und Kaufjahr (im Formular angeben)
- **Rechnen:** aktueller Verkehrswert; Faustregel: Kaufpreis, pro Jahr um 40% des Restwertes vermindert = Code 412
- **Regel:** Privates Motorfahrzeug mit aktuellem Verkehrswert; Wertverminderung in der Regel 40% des Restwertes pro Jahr. Geleaste Fahrzeuge nicht deklarieren (Leasingzinsen/-raten nicht abziehbar, siehe Ziff. 12).
- **Beachten:** Geleaste Fahrzeuge nicht deklarieren
- **Beachten:** Leasingraten (inkl. Zinsanteil) nicht als Schuldzinsen abziehbar (Ziff. 12)
- **Quellen:**
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0139.md) `zh-wl-2026-uj__c0139` – «beträgt die Wertverminderung pro Jahr 40% des Restwertes.»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0011.md) `zh-form-300-2026-uj__c0011` – «30.4 Motorfahrzeuge: Kaufpreis: Kaufjahr: 412»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0068.md) `zh-wl-2026-uj__c0068` – «abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Geschäfts-/Korporationsanteile (Code 414)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung über Kapital und Ertrag; Beteiligungsquote
- **Rein:** Aufstellung über Kapital und Ertrag (Geschäft/Korporation) → anteiliger Wert · Abrechnung Korporation/Geschäft → anteiliger Ertrag für Ziff. 5.3 (Code 162)
- **Rechnen:** Wert der Geschäfts-/Korporationsanteile × Beteiligungsquote = Code 414; Ertrag × Beteiligungsquote → Ziff. 5.3 (Code 162)
- **Regel:** Anteilmässig entsprechend der Beteiligungsquote deklarieren; Aufstellung über Kapital und Ertrag beilegen.
- **Beachten:** Aufstellung über Kapital und Ertrag beilegen
- **Quellen:**
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0139.md) `zh-wl-2026-uj__c0139` – «Geschäfts- und Korporationsanteile sind von den Inhabern anteilmässig entsprechend ihrer»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0011.md) `zh-form-300-2026-uj__c0011` – «30.5 Geschäfts-/Korporationsanteile Aufstellung 414»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «5.3 Ertrag aus Geschäfts- und Korporationsanteilen Aufstellung 162»
  - [WL ZH 2026 UJ S. 31](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0218.md) `zh-wl-2026-uj__c0218` – «Aufstellung über Kapital und Ertrag.»
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0051.md) `zh-wl-2026-uj__c0051` – «Einkünfte aus Geschäfts- und Korporationsanteilen sind von den Inhabern anteilmässig»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte, nähere Bezeichnung (Code 416)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung (Gemälde, Sammlungen, Kunst, Schmuck, Boote, Flugzeuge)
- **Rein:** Eigene Aufstellung/Kaufbelege/Schätzung → Verkehrswert von Sammlungen, Kunst, Schmuck, Booten, Flugzeugen
- **Rechnen:** Σ Verkehrswerte der übrigen Vermögenswerte mit näherer Bezeichnung = Code 416
- **Regel:** Sammlungen, Kunst- und Schmuckgegenstände, Boote, Flugzeuge etc. mit Verkehrswert. Hausrat ist steuerfrei.
- **Beachten:** Hausrat und persönliche Gebrauchsgegenstände steuerfrei → nicht aufführen
- **Quellen:**
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0139.md) `zh-wl-2026-uj__c0139` – «Der Hausrat ist steuerfrei.»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0011.md) `zh-form-300-2026-uj__c0011` – «30.6 Übrige Vermögenswerte; nähere Bezeichnung: 416»
  - [StG ZH § 39](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-39.md) `zh-stg-2026__par-39` – «Das Vermögen wird zum Verkehrswert bewertet.»
  - [StG ZH § 38](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-38.md) `zh-stg-2026__par-38` – «Hausrat und persönliche Gebrauchsgegenstände werden»

<a id="31-1-vermoegen-liegenschaften"></a>
### Ziff. 31.1 – Liegenschaften, zum Verkehrswert besteuert, gemäss Neufestsetzung ab 1.1.2026 (Code 421)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftenverzeichnis (Form. 350) Steuerwert (Verkehrswert); Liegenschaftenbewertung 2026 der Gemeinde
- **Rein:** Liegenschaftenbewertung 2026 der Gemeinde (Neubewertung per 1.1.2026) → Vermögenssteuerwert EFH/STWE · Liegenschaftenverzeichnis (Form. 350) → Total Spalte Verkehrswert (Code 3951) · Mieterspiegel / Hilfsblatt Ertragswert (zh.ch) → massgeblicher Ertrag MFH/Geschäftshäuser
- **Rechnen:** Σ Steuerwerte aller nicht land-/forstw. Liegenschaften inkl. Übertrag 558 = Code 3951 → 421; MFH/Geschäftshaus: Ertrag × 100 / Kapitalisierungssatz Gemeinde
- **Regel:** Vermögenssteuerwert aus der Neubewertung per 1.1.2026 (Weisung 2026) einsetzen; die Neubewertung ist zusammen mit der Steuererklärung 2026 einzureichen. EFH/STWE: Wert gemäss Weisung 2026; MFH/Geschäftshäuser: Ertragswert (Hilfsblatt). Nutzniessung: beim Nutzniesser zu 100%; Wohnrecht: beim Eigentümer. Total Verkehrswerte aller (nicht land-/forstwirtschaftlichen) Liegenschaften in 31.1.
- **Beachten:** Neubewertung 2026 beilegen; fehlt sie → Gemeindesteueramt der Liegenschaftsgemeinde
- **Beachten:** MFH = mehr als zwei Wohneinheiten → Ertragswert; Zweifamilienhaus ohne STWE wie EFH
- **Beachten:** Alle Liegenschaften (auch andere Kantone/Ausland); Nutzniessung 100% beim Nutzniesser, Wohnrecht beim Eigentümer
- **Bemerkung:** Spaltenzuordnung der Codes 553x/554x im Liegenschaftenverzeichnis (Ertragswert/Verkehrswert) am Original prüfen.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «31.1 Zum Verkehrswert besteuert Liegenschaftenverzeichnis 421»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0203.md) `zh-wl-2026-uj__c0203` – «ist der nach der «Weisung des Regierungsrates an die Steuerbehörden über die Bewertung»
  - [WL ZH 2026 UJ S. 30](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0213.md) `zh-wl-2026-uj__c0213` – «Bei Liegenschaften, auf denen ein Wohnrecht lastet, ist der Vermögenssteuerwert zu 100%»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0174.md) `zh-wl-2026-uj__c0174` – «Gestützt auf die Weisung 2026 erstellten die Gemeindesteuerämter für sämtliche Liegenschaften»
  - [WL ZH 2026 UJ S. 30](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0208.md) `zh-wl-2026-uj__c0208` – «Vermögenssteuerwert = Für die Kapitalisierung massgeblicher Ertrag x 100»
  - [WL ZH 2026 UJ S. 30](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0207.md) `zh-wl-2026-uj__c0207` – «Der Kapitalisierungssatz ist je nach Liegenschaftsgemeinde unterschiedlich.»
  - [WL ZH 2026 UJ S. 29–30](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0204.md) `zh-wl-2026-uj__c0204` – «zum Ertragswert zu bewerten. Als Mehrfamilienhäuser im Sinne der Weisung 2026 gelten Liegenschaften mit mehr als zwei Wohneinheiten.»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0173.md) `zh-wl-2026-uj__c0173` – «Es sind alle Liegenschaften zu deklarieren, auch jene in anderen Kantonen oder»
  - [WL ZH 2026 UJ S. 30](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0209.md) `zh-wl-2026-uj__c0209` – «des Ertragswerts von Mehrfamilien- und Geschäftshäusern zur Verfügung.»
  - [WL ZH 2026 UJ S. 30](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0213.md) `zh-wl-2026-uj__c0213` – «Besteht an einer Liegenschaft eine Nutzniessung, ist der Vermögenssteuerwert zu 100% durch»

<a id="31-2-vermoegen-liegenschaften"></a>
### Ziff. 31.2 – Liegenschaften, zum Ertragswert besteuert (Land- oder Forstwirtschaft) (Code 422)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftenverzeichnis (Form. 350) Spalte Ertragswert Land-/Forstwirtschaft
- **Rein:** Liegenschaftenverzeichnis (Form. 350) → Total Spalte Ertragswert Land-/Forstwirtschaft (Code 3952) · Liegenschaftenbewertung 2026 der Gemeinde → Ertragswert
- **Rechnen:** Σ Ertragswerte land-/forstwirtschaftlicher Liegenschaften (inkl. Übertrag Code 557) = Code 3952 → 422
- **Regel:** Total der Vermögenssteuerwerte land- und forstwirtschaftlicher Liegenschaften (Ertragswert) hier, alle übrigen in Ziff. 31.1.
- **Beachten:** Umfasst nötige Gebäude und landwirtschaftlich genutzten erweiterten Umschwung
- **Beachten:** Veräusserung/Entfremdung: ergänzende Vermögenssteuer auf Differenz Ertragswert–Verkehrswert
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «31.2 Zum Ertragswert besteuert (Land- oder Forstwirtschaft) Liegenschaftenverzeichnis 422»
  - [WL ZH 2026 UJ S. 30](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0213.md) `zh-wl-2026-uj__c0213` – «Das Total der Vermögenssteuerwerte aller übrigen Liegenschaften ist auf Seite 4, Ziffer 31.1 der»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0174.md) `zh-wl-2026-uj__c0174` – «Übertrag der Zahlen aus weiteren Liegenschaftenverzeichnissen 557»
  - [WL ZH 2026 UJ S. 30](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0210.md) `zh-wl-2026-uj__c0210` – «bäude, sowie landwirtschaftlich genutzte Flächen des erweiterten Umschwungs von Wohn- und»
  - [WL ZH 2026 UJ S. 30](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0212.md) `zh-wl-2026-uj__c0212` – «ergänzende Vermögenssteuer auf der Differenz zwischen Ertragswert und tatsächlichem Ver-»

<a id="32-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32 – Eigenkapital Selbständigerwerbender ohne Geschäftswertschriften (Code 430)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsblatt A Ziff. 10.4 (kaufmännische Buchführung) bzw. Ziff. 14.4 (vereinfachte Buchführung)
- **Rein:** Hilfsblatt A Ziff. 10.4 (kaufmännische Buchführung) → Eigenkapital · Hilfsblatt A Ziff. 14.4 (vereinfachte Buchführung) → Eigenkapital
- **Rechnen:** Übertrag Eigenkapital laut Hilfsblatt A (Ziff. 10.4 bzw. 14.4), ohne Geschäftswertschriften = Code 430
- **Regel:** Eigenkapital laut Hilfsblatt A übertragen; Geschäftswertschriften im Wertschriftenverzeichnis (Code G).
- **Beachten:** Geschäftswertschriften im Wertschriftenverzeichnis mit Code G erfassen
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «32. Eigenkapital Selbständigerwerbender ohne Geschäftswertschriften Hilfsblatt A 430»
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0140.md) `zh-wl-2026-uj__c0140` – «Selbständigerwerbende mit kaufmännischer Buchführung übertragen das Eigenkapital laut»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0156.md) `zh-wl-2026-uj__c0156` – «mit G das Geschäftsvermögen»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 460)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Summe Ziff. 30–32
- **Rein:** Übertrag Ziff. 31.1/31.2 (Codes 421/422) und Ziff. 32 (Code 430)
- **Regel:** Rechenzeile.
- **Beachten:** Steuerwerte per 31.12.2026 bzw. Ende Steuerpflicht; gesamtes in- und ausländisches Vermögen
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «33. Total der Vermögenswerte 460»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0011.md) `zh-form-300-2026-uj__c0011` – «Steuerwert per 31.12.2026 bzw. per Ende der Steuerpflicht»
  - [WL ZH 2026 UJ S. 6](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0011.md) `zh-wl-2026-uj__c0011` – «gesamte in- und ausländische Einkommen und Vermögen zu deklarieren.»

<a id="34-schulden-privat"></a>
### Ziff. 34 – Schulden (Code 470)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Kreditkartenabrechnung (Monats-/Jahresabrechnung, Karten-Jahresgebühr) → Schuldenverzeichnis (Form. 355) Total Privatschulden (Code 3200) per 31.12.2026; Hypothekarbestätigung / Saldobestätigung der Bank
- **Rein:** Schuldenverzeichnis (Form. 355) → Total Privatschulden (Code 3200) · Hypothekar-/Saldobestätigung Bank → Schuld per 31.12. und Zinsen · Darlehens-/Kreditvertrag, Saldobestätigung → Restschuld, Gläubiger, Zinssatz
- **Rechnen:** Σ Privatschulden inkl. Grundpfandschulden per 31.12.2026 (bzw. Ende Steuerpflicht) = Code 3200 → 470; Σ Zinsen = Code 3201 → Ziff. 12
- **Regel:** Gesamtbetrag der Privatschulden inkl. Grundpfandschulden per 31.12.2026; vollständiges Schuldenverzeichnis mit Gläubiger (genaue Adresse) und Zinssatz beilegen. Zinsen → Ziff. 12 (Code 3201). Leasing: Schuld nicht deklarieren, wenn Fahrzeug nicht deklariert.
- **Beachten:** Schuldzinsabzug (Ziff. 12) max. Bruttoertrag Privatvermögen inkl. EMW + CHF 50'000 (Kanton und Bund)
- **Beachten:** Amortisationen und Leasingraten (inkl. Zinsanteil) nicht als Zinsen abziehbar
- **Beachten:** Unverteilte Erbschaft: Schulden und Schuldzinsen anteilmässig
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «34. Schulden Schuldenverzeichnis 470»
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0140.md) `zh-wl-2026-uj__c0140` – «Werden Schulden deklariert, ist ein vollständiges Schuldenverzeichnis mit der Steuererklärung»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0070.md) `zh-wl-2026-uj__c0070` – «Total Privatschulden / private Schuldzinsen 3200 / 3201»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0068.md) `zh-wl-2026-uj__c0068` – «Schuld per 31.12.2026»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0069.md) `zh-wl-2026-uj__c0069` – «mögen (inkl. Eigenmietwert) und weiterer CHF 50’000 nicht übersteigen.»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0068.md) `zh-wl-2026-uj__c0068` – «abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den»
  - [WL ZH 2026 UJ S. 23](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0150.md) `zh-wl-2026-uj__c0150` – «Die Schulden und Schuldzinsen der unverteilten Erbschaft sind anteilmässig»
  - [DBG Art. 33](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t1.md) `bund-dbg-2026__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken.»
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0140.md) `zh-wl-2026-uj__c0140` – «Unerlässlich ist insbesondere die Angabe des Gläubigers mit genauer Adresse»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Steuerbares Vermögen gesamt (Code 490)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ziff. 33 minus Ziff. 34
- **Rein:** Übertrag Ziff. 33 (Code 460) und Ziff. 34 (Code 470)
- **Rechnen:** Code 490 = 460 − 470
- **Regel:** Rechenzeile; keine Vermögenssteuer bei der direkten Bundessteuer.
- **Beachten:** Nur Staats-/Gemeindesteuer: DBG kennt für natürliche Personen keine Vermögenssteuer (Art. 1 DBG)
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «35. Steuerbares Vermögen gesamt 490»
  - [DBG Art. 1](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-1.md) `bund-dbg-2026__art-1` – «a. eine Einkommenssteuer von den natürlichen Personen;»

<a id="36-1-36-2-berechnung-total"></a>
### Ziff. 36.1 / 36.2 – Auf steuerbare Vermögenswerte in anderen Kantonen (Code 494) / im Ausland (Code 496) entfallender Anteil

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ausscheidung ausserkantonale/ausländische Liegenschaften und Betriebe
- **Rein:** Übertrag aus Ziff. 35 (Code 490) → aufzuteilender Gesamtbetrag · Liegenschaftenverzeichnis → Steuerwerte ausserkantonaler/ausländischer Liegenschaften · Eigene Steuerausscheidung (falls eingereicht) → Anteile andere Kantone (494) / Ausland (496)
- **Rechnen:** Anteil von Code 490, der gemäss Steuerausscheidung auf Vermögenswerte in anderen Kantonen (494) bzw. im Ausland (496) entfällt
- **Regel:** Nur bei Steuerausscheidung ausfüllen.
- **Beachten:** Trotzdem gesamtes in- und ausländisches Vermögen deklarieren (inkl. aller Liegenschaften)
- **Beachten:** Ohne eingereichte Ausscheidung nimmt das Steueramt sie vor
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «36.1 Auf steuerbare Vermögenswerte in anderen Kantonen 494»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «36.2 Auf steuerbare Vermögenswerte im Ausland 496»
  - [WL ZH 2026 UJ S. 6](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0011.md) `zh-wl-2026-uj__c0011` – «gesamte in- und ausländische Einkommen und Vermögen zu deklarieren.»
  - [WL ZH 2026 UJ S. 6](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0011.md) `zh-wl-2026-uj__c0011` – «Das Steueramt nimmt die erforderliche Ausscheidung vor, soweit eine solche nicht mit der»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0173.md) `zh-wl-2026-uj__c0173` – «Es sind alle Liegenschaften zu deklarieren, auch jene in anderen Kantonen oder»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen im Kanton Zürich (Code 498)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ziff. 35 minus Ziff. 36
- **Rein:** Übertrag Ziff. 35 (Code 490) und Ziff. 36.1/36.2 (Codes 494/496)
- **Rechnen:** Code 498 = 490 − 494 − 496; Grundlage für Vermögenstarif § 47 StG
- **Regel:** Rechenzeile; Grundlage der Vermögenssteuer.
- **Beachten:** Unterjährige Steuerpflicht: Vermögenssteuer nach Dauer der Steuerpflicht
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «37. Steuerbares Vermögen im Kanton Zürich 498»
  - [WL ZH 2026 UJ S. 6](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0011.md) `zh-wl-2026-uj__c0011` – «Die Vermögenssteuer wird nach der Dauer der Steuerpflicht erhoben.»
  - [StG ZH § 47](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-47-t1.md) `zh-stg-2026__par-47-t1` – «Die Vermögenssteuer beträgt (Grundtarif):»

<a id="tarif-47-vermoegen-sozialabzug"></a>
### Ziff. (Tarif § 47) – Steuerfreie Vermögensbeträge (kein Formularfeld; im Tarif berücksichtigt)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand/Kinder (Seite 1)
- **Rein:** Übertrag Ziff. 37 (Code 498) → Tarifgrundlage · Seite 1 (Zivilstand, Kinder im Haushalt) → Grund- oder Verheiratetentarif
- **Rechnen:** einfache Steuer § 47: 0‰ bis 81'000 (Grundtarif) / 161'000 (Verheiratetentarif), dann ½‰ … max. 3‰; × (Staatssteuerfuss 95% + Gemeindesteuerfuss)
- **Regel:** Kein Eintrag im Formular. Der Vermögenstarif sieht Nullsätze für die ersten CHF 81'000 (übrige) bzw. CHF 161'000 (Verheiratete und ledige/geschiedene Steuerpflichtige mit Kindern im Haushalt) vor.
- **Beachten:** Verheiratetentarif auch für Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern im Haushalt
- **Beachten:** Tarif nach Verhältnissen am Ende der Steuerperiode bzw. Steuerpflicht (§ 47 Abs. 3)
- **Beachten:** Bund: keine Vermögenssteuer (Art. 1 DBG)
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 81'000 (Vermögenssteuer Grundtarif: 0 ‰ für die ersten Fr. 81'000 (steuerfreies Vermögen im Tarif; kein separater Sozialabzug).)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 161'000 (Vermögenssteuer Verheiratetentarif (ungetrennte Ehe; auch Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern im Haushalt): 0 ‰ für die ersten Fr. 161'000.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
  - Steuerfuss Kanton (%/Einheiten): Kanton **95 % (Staatssteuerfuss 2026: 95 % der einfachen Staatssteuer (für alle Gemeinden gleich; 2025: 98 %). Gemeindesteuerfüsse werden von den Gemeinden festgesetzt.)** · Bund **n/a – Kantonaler Steuerfuss; Bund hat einen eigenen Tarif (Art. 36 DBG) ohne Steuerfuss.**
- **Bund:** Keine Vermögenssteuer beim Bund.
- **Quellen:**
  - [StG ZH § 47](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-47-t1.md) `zh-stg-2026__par-47-t1` – «0‰ für die ersten Fr. 81 000»
  - [StG ZH § 47](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-47-t2.md) `zh-stg-2026__par-47-t2` – «0‰ für die ersten Fr. 161 000»
  - [StG ZH § 47](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-47-t2.md) `zh-stg-2026__par-47-t2` – «Der Tarif wird nach den Verhältnissen am Ende der Steuerperiode oder der Steuerpflicht festgelegt.»
  - [DBG Art. 1](../../chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-1.md) `bund-dbg-2026__art-1` – «a. eine Einkommenssteuer von den natürlichen Personen;»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «37. Steuerbares Vermögen im Kanton Zürich 498»
  - [ZH Steuerfüsse](../../chunks/zh/dauernd/zh-info-steuerfuesse/zh-info-steuerfuesse__c0003.md) `zh-info-steuerfuesse__c0003` – «liegt für die Jahre 2026 und 2027 bei 95 Prozent der einfachen Staatssteuer.»
  - [ZStB 173.1](../../chunks/zh/dauernd/zh-zstb-173-1/zh-zstb-173-1__c0027.md) `zh-zstb-173-1__c0027` – «Die Gemeindesteuern sind zu den von der Gemeinde jährlich beschlossenen Prozentsätzen von der einfachen Staatssteuer zu berechnen»

## Hilfsblatt Wertschriftenverzeichnis

<a id="form-340-kolonnen-a-b-codes-einkommen-wertschriften"></a>
### Ziff. Form. 340 (Kolonnen A/B, Codes) – Wertschriften- und Guthabenverzeichnis mit Verrechnungsantrag: Kolonne A (mit Verrechnungssteuerabzug), Kolonne B (ohne); Codes G, N, E, S, Q

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Steuerauszug/eSteuerauszug; Zins- und Dividendenabrechnungen; Bankbelege Festgeld/Kassenobligationen
- **Rein:** eSteuerauszug/Steuerauszug Bank → Bruttoerträge mit VSt (A) / ohne VSt (B), Steuerwerte · Zins-/Dividendenabrechnungen, Festgeld- und Kassenobligationen-Belege → Bruttoertrag, Laufzeit, Zinssatz · Bescheinigung Lotteriegesellschaft/Bank → Gewinn mit VSt-Abzug (Kolonne A) · Ausländische Dividenden-/Zinsbelege → Ertrag zum Tageskurs (Kolonne B bzw. DA-1)
- **Rechnen:** A: CH-Zinsen/Dividenden, Kundenguthaben mit Bruttozins > CHF 200; B: übrige; Σ Ertrag A + B → Ziff. 4.1 (Code 150), davon Q → 4.2 (151); Σ Steuerwert (400) → 30.1
- **Regel:** Bruttoerträge je nach Verrechnungssteuerabzug in Kolonne A oder B. Kolonne A: schweizerische Zinsen/Dividenden, auch Kundenguthaben mit Bruttozins über CHF 200 pro Jahr. Kennzeichnen: G Geschäftsvermögen, N Nutzniessungsvermögen, E Werte aus Erbschaft 2026, S Schenkung 2026, Q Beteiligung mind. 10%. Ausländische Titel mit ISIN/Valor, Erträge zum Tageskurs. Ausländische Quellensteuern/US-Steuerrückbehalt via Formular DA-1 (Übertrag in Zeile «Übertrag ab Formular DA-1»). Total Ertrag → Ziff. 4.1, Total Steuerwert → Ziff. 30.1.
- **Beachten:** Q-Ausschüttungen ungekürzt (brutto); B u.a. Darlehen, ausländische Wertschriften/Fonds, STWEG-Anteile
- **Beachten:** Grossspiel-/Online-Casino-Gewinne frei bis CHF 1'046'400 (Kanton) / 1'071'000 (Bund); nur Mehrbetrag steuerbar
- **Beachten:** Fonds: thesaurierte Erträge steuerbar; gesondert ausgewiesene Kapitalgewinne (Privatvermögen) frei
- **Limiten:**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'046'400 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen (BGS) steuerfrei bis Fr. 1'046'400 (Freibetrag: nur der übersteigende Anteil ist steuerbar).)** · Bund **CHF 1'071'000 (Einzelne Gewinne aus nach BGS zugelassenen Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'071'000; darüber steuerbar (abzüglich Einsatzkosten nach Art. 33 Abs. 4 DBG).)**
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes Kennbuchstaben G, N, E, S, Q; Total Steuerwert 400 → Ziff. 30.1; Total Bruttoertrag A+B 150 → Ziff. 4.1; qualifizierte Beteiligungen 151 → Ziff. 4.2
- **Quellen:**
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0160.md) `zh-wl-2026-uj__c0160` – «Dies gilt auch für Kundenguthaben mit einem Bruttozins von mehr als»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0156.md) `zh-wl-2026-uj__c0156` – «mit Q Beteiligungen von mindestens 10 Prozent am Aktien-, Grund- oder Stammkapital an»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0155.md) `zh-wl-2026-uj__c0155` – «ob die Verrechnungssteuer abgezogen wurde oder nicht, entweder in der Kolonne A oder Kolonne B einzutragen.»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «4.1 Ertrag aus Wertschriften, Guthaben und Lotterien Wertschriftenverzeichnis 150»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «4.2 Davon aus qualifizierten Beteiligungen»
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0162.md) `zh-wl-2026-uj__c0162` – «Sie sind ungekürzt, d.h. mit dem Bruttobetrag der Ausschüttung,»
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0166.md) `zh-wl-2026-uj__c0166` – «Darlehen und Hypothekarforderungen»
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0164.md) `zh-wl-2026-uj__c0164` – «der Staatssteuer bzw. CHF 1’071’000 bei der Bundessteuer steuerfrei und müssen demzufolge»
  - [WL ZH 2026 UJ S. 25–26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0163.md) `zh-wl-2026-uj__c0163` – «Neben den ausgeschütteten sind auch zurückbehaltene (thesaurierte) Erträge steuerbar.»
  - [WL ZH 2026 UJ S. 34](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0228.md) `zh-wl-2026-uj__c0228` – «A Werte mit Verrechnungssteuerabzug, deren Erträge um 35% eidg. Verrechnungssteuer»
  - [WL ZH 2026 UJ S. 34](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0229.md) `zh-wl-2026-uj__c0229` – «Total Bruttoertrag A + B»
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0164.md) `zh-wl-2026-uj__c0164` – «Diese sind hier aufzuführen, wenn die Verrechnungssteuer abgezogen wurde.»
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0164.md) `zh-wl-2026-uj__c0164` – «ausschliesslich derjenige Anteil des Gewinnes steuerbar, welcher den Betrag von CHF 1’046’400 bzw. CHF 1’071’000 übersteigt.»
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0168.md) `zh-wl-2026-uj__c0168` – «ausgerichteten Erträge solcher Wertschriften sind zum Tageskurs in Schweizer»
  - [WL ZH 2026 UJ S. 34](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0229.md) `zh-wl-2026-uj__c0229` – «Ausländische Wertschriften aller Art»
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0167.md) `zh-wl-2026-uj__c0167` – «aber in Kolonne B zu deklarieren.»
  - [WL ZH 2026 UJ S. 34](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0228.md) `zh-wl-2026-uj__c0228` – «Steuererklärung Seite 4, Ziffer 30.1»
  - [Formular 340 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0003.md) `zh-form-340-2026-uj__c0003` – «A Werte mit Verrechnungssteuerabzug, deren Erträge um 35% eidg. Verrechnungssteuer»
  - [Formular 340 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0003.md) `zh-form-340-2026-uj__c0003` – «B Werte ohne Verrechnungssteuerabzug, deren Erträge nicht um 35% eidg. Verrechnungssteuer»
  - [Formular 340 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0003.md) `zh-form-340-2026-uj__c0003` – «E Wertschriften aus Erbschaften»
  - [Formular 340 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0003.md) `zh-form-340-2026-uj__c0003` – «über CHF 1’046’400 S Schenkung»
  - [Formular 340 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0003.md) `zh-form-340-2026-uj__c0003` – «(Originalbescheinigungen sind beizulegen) Q Qualifizierte Beteiligung»
  - [Formular 340 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0003.md) `zh-form-340-2026-uj__c0003` – «1. Kundenguthaben deren Bruttozins CHF 200.– nicht übersteigt»
  - [Formular 340 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0003.md) `zh-form-340-2026-uj__c0003` – «qualifizierten Beteiligungen 151»
  - [Formular 340 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0004.md) `zh-form-340-2026-uj__c0004` – «Steuerwert per 31.12.2026»
  - [Formular 340 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0004.md) `zh-form-340-2026-uj__c0004` – «bzw. per Ende der Steuerpflicht»
  - [Formular 340 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0005.md) `zh-form-340-2026-uj__c0005` – «Total Steuerwert 400 ▸ Zu übertragen in die Steuererklärung Seite 4, Ziffer 30.1»
  - [Formular 340 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0005.md) `zh-form-340-2026-uj__c0005` – «Total Bruttoertrag A + B 150»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «4.2 Davon aus qualifizierten Beteiligungen 13213211 151»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0011.md) `zh-form-300-2026-uj__c0011` – «30.1 Wertschriften und Guthaben Wertschriftenverzeichnis 400113213211»

<a id="form-340-verrechnungsantrag-da-1-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 340 (Verrechnungsantrag / DA-1) – Verrechnungsantrag (Rückerstattung Verrechnungssteuer, Kolonne A) und Formular DA-1 (ausländische Quellensteuern)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Bankverbindung (IBAN) für Rückerstattung; DA-1 mit Quellensteuerbelegen
- **Rein:** Wertschriftenverzeichnis Kolonne A → Total Bruttoertrag A (Basis VSt-Anspruch) · Bankverbindung (IBAN, Konto lautend auf) → Konto für Rückerstattung · Formular DA-1 + Bankbescheinigungen/Belege ausländische Quellensteuer → Bruttoertrag, nicht rückforderbare Steuer (Kol. 8)
- **Rechnen:** VSt-Anspruch = 35% × Σ Bruttoertrag A (auf 5 Rappen runden); DA-1-Totale → Zeile «Übertrag ab Formular DA-1», Bruttoertrag in Kolonne B
- **Regel:** Mit der Unterschrift wird bestätigt, dass auf allen Erträgen der Kolonne A die Verrechnungssteuer abgezogen wurde. Rückerstattung auf angegebenes Konto. Ausländische Quellensteuern: Antrag DA-1; Anrechnung nur, wenn die nicht rückforderbaren ausländischen Steuern insgesamt CHF 100 übersteigen.
- **Beachten:** Anrechnung nur, wenn nicht rückforderbare ausländische Steuern total > CHF 100; sonst Ertrag gekürzt im Verzeichnis
- **Beachten:** Erträge ohne Quellensteuer oder voll rückforderbar nicht ins DA-1, sondern ins ordentliche Verzeichnis
- **Beachten:** DA-1 auch für US-Erträge mit zusätzlichem Steuerrückbehalt; Verzeichnis unterschreiben (Bestätigung Kolonne A)
- **Bemerkung:** Formular 2026 (UJ): bestaetigt; Codes IBAN 2010, Konto lautend auf 549; Übertrag DA-1 2370 / 2371; VSt-Anspruch 540
- **Quellen:**
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0153.md) `zh-wl-2026-uj__c0153` – «allen unter Kolonne A angegebenen Erträgen die eidg. Verrechnungssteuer zu meinen oder zu Lasten der von mir vertretenen»
  - [WL ZH 2026 UJ S. 26–27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0169.md) `zh-wl-2026-uj__c0169` – «Die Totalbeträge des DA-1 übertragen Sie in die Zeile «Übertrag ab Formular DA-1» im»
  - [WL ZH 2026 UJ S. 34](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0229.md) `zh-wl-2026-uj__c0229` – «35% von Total Bruttoertrag A»
  - [WL ZH 2026 UJ S. 34](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0229.md) `zh-wl-2026-uj__c0229` – «5 Rappen zu runden.»
  - [DA-1 2026 S. 2](../../chunks/bund/2026/bund-form-da1-2026/bund-form-da1-2026__c0007.md) `bund-form-da1-2026__c0007` – «In diesem Fall sind die Erträge zu dem um die nicht rückforderbare ausländische Steuer gekürzten»
  - [DA-1 2026 S. 2](../../chunks/bund/2026/bund-form-da1-2026/bund-form-da1-2026__c0007.md) `bund-form-da1-2026__c0007` – «im Quellenstaat unterliegen oder für die die vollständige Rückerstattung verlangt werden kann, nicht hier, sondern im ordentlichen»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0152.md) `zh-wl-2026-uj__c0152` – «Bankverbindung für Rückerstattungen Ein allfälliges Guthaben ist wie folgt zu überweisen:»
  - [DA-1 2026 S. 2](../../chunks/bund/2026/bund-form-da1-2026/bund-form-da1-2026__c0007.md) `bund-form-da1-2026__c0007` – «Legen Sie dem Antrag Bankbescheinigungen, Belege über den Einbehalt der ausländischen Quellensteuer, usw. bei.»
  - [Formular 340 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0001.md) `zh-form-340-2026-uj__c0001` – «allen unter Kolonne A angegebenen Erträgen die eidg. Verrechnungssteuer zu meinen oder zu Lasten der von mir vertretenen Steuer»
  - [Formular 340 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0001.md) `zh-form-340-2026-uj__c0001` – «Bankverbindung für Rückerstattungen Ein allfälliges Guthaben ist wie folgt zu überweisen:»
  - [Formular 340 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0001.md) `zh-form-340-2026-uj__c0001` – «IBAN-Nr. 2010»
  - [Formular 340 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0001.md) `zh-form-340-2026-uj__c0001` – «Konto lautend auf 549»
  - [Formular 340 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0005.md) `zh-form-340-2026-uj__c0005` – «Übertrag ab Formular DA-1 2370 2371»
  - [Formular 340 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-340-2026-uj/zh-form-340-2026-uj__c0005.md) `zh-form-340-2026-uj__c0005` – «35% von Total Bruttoertrag A 540»
  - [DA-1 2026 S. 2](../../chunks/bund/2026/bund-form-da1-2026/bund-form-da1-2026__c0007.md) `bund-form-da1-2026__c0007` – «insgesamt den Betrag von 100 Franken nicht übersteigen, so wird»

## Hilfsblatt Liegenschaften

<a id="form-350-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 350 – Liegenschaftenverzeichnis: Steuerwert (Codes 5531ff / 5541ff), Eigenmietwert/Mietzinseinnahmen, Unterhalt (pauschal/effektiv), Nettoertrag aus Liegenschaften (Code 3953), Übertrag weitere Verzeichnisse (Code 578)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Liegenschaftenbewertung 2026 der Gemeinde; Mieterspiegel; Unterhaltsrechnungen; Beiblatt zum Liegenschaftenverzeichnis
- **Rein:** Liegenschaftenneubewertung 2026 der Gemeinde → Steuerwert und Eigenmietwert EFH/STWE · Mieterspiegel/Verwaltungsabrechnung (sonst Beiblatt) → Miet- und Pachtzinseinnahmen · Unterhalts-, Versicherungs-, Verwaltungsrechnungen (Aufstellung/Beiblatt) → effektive Kosten · Baurechtsvertrag/Zahlungsbelege → Baurechtszinsen (Aufstellung)
- **Rechnen:** je Liegenschaft: EMW + Miet-/Pachtzinse − Unterhalt (pauschal Kanton 20% / Bund 10% bzw. 20%, oder effektiv); Σ inkl. Übertrag 578 = Code 3953 → Ziff. 6
- **Regel:** Pro Liegenschaft (alle Liegenschaften, auch in anderen Kantonen und im Ausland) Steuerwert, Eigenmietwert bzw. Mieterträge, Unterhalt/Verwaltung (Pauschale oder effektiv) und verbleibenden Ertrag erfassen; Nettoertrag → Ziff. 6, Steuerwerte → Ziff. 31.1/31.2.
- **Beachten:** EMW: Baujahr bis 2025 weiter Weisung 2009; Neubau ab 2026 Weisung 2026 − 10%; MFH-Eigennutzung 70% Drittmietzins
- **Beachten:** Bund-Pauschale 10% bei Gebäude bis 10 Jahre (Beginn Steuerperiode); keine Pauschale bei vorwiegend Geschäftsnutzung
- **Beachten:** Neben Pauschale nur Baurechtszinsen; Bund nicht, wenn EMW auf Zeitbauwert beansprucht
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **20 % (Pauschalabzug für Unterhalts- und Verwaltungskosten von Liegenschaften des Privatvermögens: 20 % des Brutto-Mietertrags bzw. Mietwerts je Liegenschaft; ZH kennt keine Abstufung nach Gebäudealter. Wahl pro Liegenschaft und Steuerperiode; nicht bei ganz oder vorwiegend geschäftlich genutzten Liegenschaften; daneben nur Baurechtszinsen abziehbar.)** · Bund **10 % (Pauschalabzug Liegenschaftskosten (anstelle effektiver Kosten, Wahl pro Periode und Liegenschaft): 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist.)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Gleicher Satz wie für jüngere Gebäude: 20 % des Brutto-Mietertrags bzw. Mietwerts (keine Altersabstufung in ZH).)** · Bund **20 % (Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist.)**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **10 % (Eigenmietwert: Für Liegenschaften bis und mit Baujahr 2025 gelten weiterhin die Eigenmietwerte nach Weisung 2009 (ohne Erhöhung); für Neubauten ab 2026 gilt die Weisung 2026 mit einem pauschalen Abzug von 10 % zum Ausgleich der höheren Eigenmietwerte. Selbstgenutzte Wohnungen in Mehrfamilien-/Geschäftshäusern: 70 % des erzielbaren Mietzinses. Gesetzliche Leitlinie: Eigenmietwert max. 70 % des Marktwerts.)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Bemerkung:** korrigiert durch Prüfung: Zitate durch wörtliche Textstellen (Code 3953; Deklarationspflicht aller Liegenschaften) ersetzt. Detailregeln in c0172/c0173 bei Bedarf direkt prüfen. Formular 2026 (UJ): bestaetigt; Codes Steuerwert 5531ff (Ertragswert) / 5541ff (Verkehrswert), Totale 3952 → Ziff. 31.2 (Code 422) / 3951 → Ziff. 31.1 (Code 421); Übertrag 578; Nettoertrag 3953 → Ziff. 6 (Hauptformular Code 188)
- **Quellen:**
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0177.md) `zh-wl-2026-uj__c0177` – «Nettoertrag aus Liegenschaften 3953»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0173.md) `zh-wl-2026-uj__c0173` – «Es sind alle Liegenschaften zu deklarieren, auch jene in anderen Kantonen oder»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0174.md) `zh-wl-2026-uj__c0174` – «erklärung Seite 4, Ziffer 31.2»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0174.md) `zh-wl-2026-uj__c0174` – «erklärung Seite 4, Ziffer 31.1»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0191.md) `zh-wl-2026-uj__c0191` – «gung, soweit diese die tatsächlichen Aufwendungen nicht übersteigen) und beträgt 20% für»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «a. wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0181.md) `zh-wl-2026-uj__c0181` – «gelten für Zürcher Liegenschaften bis und mit Baujahr 2025 deshalb weiterhin die bisherigen,»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0182.md) `zh-wl-2026-uj__c0182` – «Zum Ausgleich für die höheren Eigenmietwerte für Neubauten ab 2026 wird ein pauschaler»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0182.md) `zh-wl-2026-uj__c0182` – «schäftshäusern sind 70% des Mietzinses einzusetzen, der bei Vermietung dieser Einheiten an»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0201.md) `zh-wl-2026-uj__c0201` – «Der Baurechtszins ist bei der direkten Bundessteuer nicht abzugsberechtigt, wenn für die»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0190.md) `zh-wl-2026-uj__c0190` – «Ein Pauschalabzug ist jedoch nicht zulässig, wenn die Liegen-»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0179.md) `zh-wl-2026-uj__c0179` – «ist auf der Liegenschaftenneubewertung 2026 ausgewiesen.»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0184.md) `zh-wl-2026-uj__c0184` – «Für vermietete Liegenschaften ist eine detaillierte Ertragsaufstellung (Mieterspiegel)»
  - [WL ZH 2026 UJ S. 28–29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0192.md) `zh-wl-2026-uj__c0192` – «ist der Steuererklärung eine detaillierte Aufstellung über diese Aufwendungen (enthaltend»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0191.md) `zh-wl-2026-uj__c0191` – «Wird der Pauschalabzug beansprucht, können (mit Ausnahme der Baurechtszinsen, siehe»
  - [WL ZH 2026 UJ S. 30](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0209.md) `zh-wl-2026-uj__c0209` – «Übertrag der Zahlen aus weiteren Liegenschaftenverzeichnissen 578»
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «6. Nettoertrag aus Liegenschaften Liegenschaftenverzeichnis 188»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «31. Liegenschaften, Verkehrswert gemäss Neufestsetzung ab 1.1. 2026»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «31.1 Zum Verkehrswert besteuert Liegenschaftenverzeichnis 421»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «31.2 Zum Ertragswert besteuert (Land- oder Forstwirtschaft) Liegenschaftenverzeichnis 422»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «Die Liegenschaftenneubewertung per 1.1.2026 ist zusammen mit der Steuererklärung 2026 einzureichen»
  - [Formular 350 ZH S. 1](../../chunks/zh/2025/zh-form-350/zh-form-350__c0001.md) `zh-form-350__c0001` – «Art Fläche in m2 5531 13213211 5541 113213211»
  - [Formular 350 ZH S. 1](../../chunks/zh/2025/zh-form-350/zh-form-350__c0002.md) `zh-form-350__c0002` – «Total 3952 13213211 3951 113213211»
  - [Formular 350 ZH S. 1](../../chunks/zh/2025/zh-form-350/zh-form-350__c0002.md) `zh-form-350__c0002` – «erklärung Seite 4, Ziffer 31.2 erklärung Seite 4, Ziffer 31.1»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0004.md) `zh-form-350__c0004` – «Übertrag der Zahlen aus weiteren Liegenschaftenverzeichnissen 578 13213211 Nettoertrag aus Liegenschaften 3953»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0004.md) `zh-form-350__c0004` – «Nettoertrag aus Liegenschaften 3953 13213211 ▸ Zu übertragen in die Steuer- erklärung Seite 2, Ziffer 6»
