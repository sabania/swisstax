---
typ: zuordnung-detail
titel: Zuordnung ZH 2025 – Detail
jur: zh
jahre:
- 2025
generiert: tools/build_quick.py aus data/zuordnung/zh/2025.yaml (2026-11-09)
---

# ZH 2025: Zuordnung Beleg → Ziffer – Detail

> Kompaktansicht: [quick/zuordnung-zh-2025.md](../../quick/zuordnung-zh-2025.md) · Formular: Steuererklärung 2025 Kanton Zürich (StA Form. 300, Hauptformular) + Hilfsblätter Form. 340 (Wertschriften- und Guthabenverzeichnis), 350 (Liegenschaftenverzeichnis), 355 (Schuldenverzeichnis), 360 (Berufsauslagen), 365 (Versicherungsprämien), 367 (Aus- und Weiterbildungskosten), 370 (Krankheits-/Unfallkosten, behinderungsbedingte Kosten) · Quelle der Wahrheit: `data/zuordnung/zh/2025.yaml`

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Haupterwerb unselbständig, Person 1 / Person 2 (Code 100/101)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn / Rente)
- **Regel:** Nettolohn gemäss Lohnausweis Ziff. 11 einsetzen (nach Abzug AHV/IV/EO/ALV, laufender BVG-Beiträge und NBUV-Prämien); Lohnausweis beilegen; Erwerbslücken ausdrücklich bezeichnen. Je Person eine Zeile (P1 = 100, P2 = 101). Lohnausweis-Felder F, G, 10.2, 13.3, 15 beachten (siehe Abschnitt Lohnausweis-Regeln).
- **Bund:** Gleiche Zeile für Staats- und Bundessteuer (eine Spalte, kein Unterschied).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Haupterwerb Person 1 Lohnausweis»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Person 2 Lohnausweis 101»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0032.md) `zh-wl-2025__c0032` – «In der Steuererklärung ist der Nettolohn (d.h. der Lohn nach Abzug von AHV/IV/EO- und»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Nebenerwerb unselbständig inkl. Behörden-/VR-Entschädigungen, Person 1 / Person 2 (Code 102/103)

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn / Rente) des Nebenerwerbs-Lohnausweises
- **Regel:** Sämtliche Einkünfte aus unselbständigen Nebenerwerbstätigkeiten (Dienstleistungen jeder Art, Amtstätigkeit, Verwaltungsrats-/Vorstandshonorare, Tantiemen, Lizenzen, Autorenrechte) einsetzen. Berufsauslagen dazu: Pauschale 20 % (Form. 360 Ziff. 5, Code 216/217) oder effektiv.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Nebenerwerb Person 1 Lohnausweis 102»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Vergütungen für Amtstätigkeit, Verwaltungsrats- und Vorstands»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0033.md) `zh-wl-2025__c0033` – «Hier sind sämtliche Einkünfte aus unselbständigen Nebenerwerbstätigkeiten aufzuführen»

<a id="1-2-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 1.2 – Im vereinfachten Verfahren abgerechnete Einkünfte (Bescheinigung AHV-Ausgleichskasse)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der AHV-Ausgleichskasse (kein Lohnausweis)
- **Regel:** Einkünfte, für die im vereinfachten Verfahren (Bundesgesetz gegen die Schwarzarbeit) abgerechnet wurde, nicht als Lohn aufführen; die Bescheinigung der AHV-Ausgleichskasse ist der Steuererklärung beizulegen.
- **Quellen:**
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0033.md) `zh-wl-2025__c0033` – «gegen die Schwarzarbeit bezahlt wurden. Der Steuererklärung ist jedoch die Bescheinigung»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit Haupterwerb, Person 1 / Person 2 (Code 120/121)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsblatt A (Reingewinn nach Steuerkorrekturen) bzw. Hilfsblatt B/G (Landwirtschaft)
- **Regel:** Ergebnis aus Hilfsblatt A einsetzen (inkl. qualifizierte Beteiligungen im Geschäftsvermögen und Liquidationsgewinne). Bei kaufmännischer Buchführung unterzeichnete Jahresrechnung (Bilanz, Erfolgsrechnung, Anhang) einreichen. Liquidationsgewinne (ab 55 / Invalidität) werden gesondert besteuert und unter Ziff. 16.5 wieder abgezogen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Haupterwerb Person 1 Hilfsblatt»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0039.md) `zh-wl-2025__c0039` – «reichen Sie eine unterzeichnete Jahresrechnung (Einzelabschluss»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0043.md) `zh-wl-2025__c0043` – «Solche Liquidationsgewinne können unter Ziffer 16.5 wieder von den Einkünften abgezogen werden»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Selbständige Erwerbstätigkeit Nebenerwerb, Person 1 / Person 2 (Code 122/123)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsblatt bzw. Aufstellung des Nebenerwerbs
- **Regel:** Sämtliche Einkünfte aus selbständigen Nebenerwerbstätigkeiten angeben (Hilfsblatt bzw. Aufstellung); Gewinne aus Wertschriften-/Liegenschaftsverkäufen nur, soweit über die schlichte Vermögensverwaltung hinaus (siehe WL).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Nebenerwerb Person 1 Hilfsblatt»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0047.md) `zh-wl-2025__c0047` – «Hier sind sämtliche Einkünfte aus selbständigen Nebenerwerbstätigkeiten anzugeben»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV-/IV-Renten (100 %), Person 1 / Person 2 (Code 130/131)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung AHV/IV (Jahresbetrag)
- **Regel:** AHV-/IV-Renten sind zu 100 % steuerbar; Jahresbetrag einsetzen, Haken AHV oder IV setzen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «AHV- / IV-Renten (100%) Person 1»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0050.md) `zh-wl-2025__c0050` – «AHV- und IV-Renten [ Ziffer 3.1]»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten / Pensionen (2. Säule, 3a, Arbeitgeber, UVG, Militärversicherung), Person 1 / 2 (Code 134/135 bzw. 136/137; Vorkolonnen 960–967)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Rentenbescheinigung Pensionskasse / Versicherer: Bruttorente (Betrag) und steuerbarer Anteil (Prozente)
- **Regel:** Vorkolonne «Betrag» = Gesamtrente, Hauptkolonne = steuerbarer Teil. 2. Säule i.d.R. 100 % (80 % nur bei Rentenbeginn vor 1.1.1987 bzw. 1987–2001 mit Eigenbeitrag ≥ 20 %); Renten aus Säule 3a, vom Arbeitgeber und Militärversicherung 100 %; UVG-Renten 100 % (60 %/80 % nur Altfälle vor 1986).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «3.2 Renten / Pensionen»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0050.md) `zh-wl-2025__c0050` – «in allen übrigen Fällen:»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0051.md) `zh-wl-2025__c0051` – «Renten aus anerkannten Formen der gebundenen Selbstvorsorge (3. Säule a)»

<a id="3-2-leibrenten-einkommen-vorsorge-uebrige-renten"></a>
### Ziff. 3.2 (Leibrenten) – Leibrenten / Verpfründung (private, Versicherer, ausländisch) – Code 134–137

- **Schlüssel:** `einkommen.vorsorge.uebrige_renten` (Übrige Renten (Leibrenten, ausländische Renten, Militär-/Unfallversicherung)) · **Status:** ⚠️ strittig
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Steuerbescheinigung des Versicherers (steuerbarer Ertragsanteil) bzw. Leibrentenvertrag + ESTV-Berechnungssatz
- **Regel:** Gesamtbetrag in Vorkolonne «Betrag», steuerbarer Ertragsanteil in die Hauptkolonne; Kolonne «Prozente» leer lassen. Ertragsanteil: Bescheinigung des Versicherers bzw. Rente x ESTV-Berechnungssatz / 100. STRITTIG: StG § 22 Abs. 3 (Fassung 2025) nennt 40 %, WL 2025 den flexiblen Ertragsanteil – Fachperson entscheidet.
- **Bund:** Bund: Ertragsanteil nach Art. 22 Abs. 3 DBG (lit. a/b Leibrentenversicherungen mit Versichererbescheinigung; lit. c ausländische Leibrentenversicherungen sowie Leibrenten- und Verpfründungsverträge, Satz r + 0,5 Prozentpunkte).
- **Bemerkung:** Widerspruch Gesetz vs. Wegleitung: StG ZH § 22 Abs. 3 (zh-stg-2025, Nachtrag 127) = 40 Prozent; WL ZH 2025 (c0025, c0052) = flexibler Ertragsanteil seit 1.1.2025 (bisher pauschal 40 %). Rangfolge Gesetz > Wegleitung, aber StG-Fassung im Wiki möglicherweise nicht auf Stand. Praxis der Wegleitung (Bescheinigung des Versicherers) anwenden und Fachperson informieren. Gegenprobe Prüfung: StHG Art. 7 Abs. 2 (Fassung 2025) kennt den flexiblen Ertragsanteil; nach Art. 72 Abs. 2 StHG gilt Bundesrecht direkt, wenn das kantonale Recht widerspricht – das spricht für die Wegleitung (Versichererbescheinigung/ESTV-Satz). Endentscheid bleibt bei der Fachperson (status strittig).
- **Quellen:**
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0052.md) `zh-wl-2025__c0052` – «Leibrenten sowie Einkünfte aus Verpfründung»
  - [WL ZH 2025 S. 9](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0025.md) `zh-wl-2025__c0025` – «Ab dem 1.1.2025 wird der steuerbare Ertragsanteil flexibel an die Anlagebedingungen angepasst»
  - [StG ZH § 22](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-22.md) `zh-stg-2025__par-22` – «Leibrenten sowie Einkünfte aus Verpfründung sind zu 40 Prozent steuerbar.»
  - [StHG Art. 7](../../chunks/bund/2025/bund-sthg/bund-sthg__art-7-t3.md) `bund-sthg__art-7-t3` – «Leibrentenversicherungen sowie Leibrenten- und Verpfründungsverträge sind im Umfang ihres Ertragsanteils steuerbar»
  - [StHG Art. 72](../../chunks/bund/2025/bund-sthg/bund-sthg__art-72.md) `bund-sthg__art-72` – «Nach ihrem Inkrafttreten finden die Bestimmungen dieses Gesetzes direkt Anwendung, wenn ihnen das kantonale Steuerrecht widerspricht»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigungen aus Arbeitslosenversicherung, direkt ausbezahlt (Code 140/141)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Arbeitslosenkasse (Jahresbetrag)
- **Regel:** Nur direkt von der Arbeitslosenkasse ausbezahlte Entschädigungen hier; vom Arbeitgeber ausbezahlte Taggelder stehen bereits im Lohnausweis. Bescheinigungen beilegen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «3.3 Erwerbsausfallentschädigungen aus Arbeitslosenversicherung»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0054.md) `zh-wl-2025__c0054` – «Die entsprechenden Bescheinigungen sind beizulegen.»

<a id="3-4-einkommen-ersatz-taggelder"></a>
### Ziff. 3.4 – Taggelder KV/UV/IV/MV, EO und Mutterschaftsentschädigung, direkt ausbezahlt (Code 142/143)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Versicherung / Ausgleichskasse (Jahresbetrag)
- **Regel:** Taggelder aus Kranken-, Unfall-, Invaliden- und Militärversicherung sowie EO/Mutterschaftsentschädigung sind steuerbar. Hier nur eintragen, wenn nicht im Lohnausweis enthalten; Bescheinigung verlangen und beilegen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «3.4 Kinder- und Familienzulagen, Mutterschaftsentschädigungen, Taggelder»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0055.md) `zh-wl-2025__c0055` – «Taggelder aus Kranken-, Unfall- und Invalidenversicherung, aus Militärversicherung sowie die»

<a id="3-4-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.4 – Kinder- und Familienzulagen, direkt von der Ausgleichskasse ausbezahlt (Code 142/143)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Familienausgleichskasse (nicht im Lohnausweis enthalten)
- **Regel:** Nur Zulagen eintragen, die nicht über den Lohnausweis abgerechnet wurden, sondern direkt von der Ausgleichskasse kamen.
- **Quellen:**
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0055.md) `zh-wl-2025__c0055` – «von Ausgleichskassen direkt ausbezahlten Kinder- und Familienzulagen und Mutterschafts-»

<a id="3-steuerfrei-info-steuerfreie-leistungen"></a>
### Ziff. 3 (steuerfrei) – Steuerfreie Unterstützungsleistungen (EL, Hilflosenentschädigung, Pflegebeiträge) – nicht deklarieren

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung / Bescheid der Ausgleichskasse (nur zur Abgrenzung)
- **Regel:** Ergänzungsleistungen, Hilflosenentschädigungen, Pflegebeiträge, Beihilfen, Arbeitslosenhilfen und Gemeindezuschüsse für Bezüger von AHV/IV/UVG-Leistungen sind nicht steuerbar und werden nicht als Einkommen eingesetzt.
- **Quellen:**
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0053.md) `zh-wl-2025__c0053` – «Beihilfen, Arbeitslosenhilfen und Gemeindezuschüsse, welche Bezügern von AHV-, IV- und»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0053.md) `zh-wl-2025__c0053` – «ausgerichtet werden, sind nicht steuerbar.»

<a id="4-1-einkommen-wertschriften"></a>
### Ziff. 4.1 – Ertrag aus Wertschriften, Guthaben und Lotterien (Code 150) – Total Bruttoertrag A + B laut Wertschriftenverzeichnis

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Wertschriftenverzeichnis (Form. 340) Total Bruttoertrag A + B (Code 150); Basis: Steuerauszug / Zinsausweise
- **Regel:** Brutto-Erträge aller Konti, Wertschriften, Fonds, Dividenden (inkl. thesaurierte Erträge, Gratisaktien) im WV erfassen; Total A + B nach Ziff. 4.1 übertragen. Ertrag aus Nutzniessung zu 100 %. Vermögen und Ertrag der Kinder (Jg. 2008 und jünger) gehören in dieses Verzeichnis.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «Ertrag aus Wertschriften, Guthaben und Lotterien Wertschriftenverzeichnis 150»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Total Bruttoertrag A + B 150»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0056.md) `zh-wl-2025__c0056` – «ist zu 100% einzutragen.»

<a id="4-1-lotterie-einkommen-lotterie-gewinne"></a>
### Ziff. 4.1 (Lotterie) – Lotterie-/Grossspiel-/Sportwettengewinne (im Wertschriftenverzeichnis, Kolonne A/B)

- **Schlüssel:** `einkommen.lotterie_gewinne` (Lotterie-/Geldspielgewinne (steuerbarer Teil)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Gewinnbescheinigung Lotteriegesellschaft / Bank / Auszahlungsabschnitt Post
- **Regel:** Gewinne aus Grossspielen und Online-Spielbankenspielen sind bis CHF 1’033’000 (Staat) bzw. CHF 1’070’400 (Bund) steuerfrei; Gewinne aus Verkaufsförderungs-Lotterien bis CHF 1’000 (Staat) bzw. CHF 1’100 (Bund) steuerfrei, bei Überschreitung ganzer Gewinn steuerbar (Freigrenze). Einsatzkosten: siehe Ziff. 16.5.
- **Bund:** Bund: Freibetrag Grossspiele CHF 1’070’400, Freigrenze Verkaufsförderung CHF 1’100.
- **Quellen:**
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0167.md) `zh-wl-2025__c0167` – «sind bis zu einem Betrag von CHF 1’033’000 bei»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0167.md) `zh-wl-2025__c0167` – «zu einem Betrag von CHF 1’000 (Staatssteuer) bzw. CHF 1’100 (Bundessteuer) steuerfrei»

<a id="4-2-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.2 – Davon aus qualifizierten Beteiligungen (Code 151) – Erträge aus Beteiligungen ≥ 10 %

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Wertschriftenverzeichnis: Ertrag-Total aus qualifizierten Beteiligungen (Code Q) – Bruttobetrag der Ausschüttung
- **Regel:** Beteiligungen von mindestens 10 % mit Code Q kennzeichnen, Bruttoausschüttung ungekürzt in Kolonne A oder B erfassen und das Total nochmals in Ziff. 4.2 (Code 151) angeben (Teilbesteuerungsabzug siehe Ziff. 16.5).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «4.2 Davon aus qualifizierten Beteiligungen»
  - [Formular 340 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0003.md) `zh-form-340-2025__c0003` – «qualifizierten Beteiligungen 151»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0165.md) `zh-wl-2025__c0165` – «Sie sind ungekürzt, d.h. mit dem Bruttobetrag der Ausschüttung,»

<a id="5-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.1 – Unterhaltsbeiträge vom geschiedenen / getrennten Ehegatten (Code 160)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil bzw. Vereinbarung; Jahressumme der erhaltenen Zahlungen
- **Regel:** Erhaltene Unterhaltsbeiträge für die Person selbst sind voll als Einkommen anzugeben (Name/Adresse des Zahlers eintragen).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «Unterhaltsbeiträge vom geschiedenen / getrennten Ehegatten / Partn.»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0057.md) `zh-wl-2025__c0057` – «Unterhaltsbeiträge (Alimente), die den geschiedenen, gerichtlich oder tatsächlich getrennt»

<a id="5-2-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.2 – Unterhaltsbeiträge für minderjährige Kinder (bis Monat der Volljährigkeit) (Code 161)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil, Alimenten-Bevorschussung; Zahlungen bis und mit Monat des 18. Geburtstags
- **Regel:** Kinderalimente nur bis und mit dem Monat der Volljährigkeit deklarieren; Alimentenbevorschussungen gleichgestellt. Spätere Zahlungen nicht mehr als Einkommen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «5.2 Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit)»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0057.md) `zh-wl-2025__c0057` – «Den Alimenten gleichgestellt sind Alimentenbevorschussungen.»

<a id="5-3-einkommen-erbschaften-unverteilt"></a>
### Ziff. 5.3 – Ertrag aus Geschäfts- und Korporationsanteilen / unverteilten Erbschaften (Code 162)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung (Erbengemeinschaft / Gesellschaftsanteil); Quote des Steuerpflichtigen
- **Regel:** Einkünfte aus Geschäfts- und Korporationsanteilen anteilmässig nach Beteiligungsquote. Unverteilte Erbschaften: Einkommen ab dem auf den Todestag folgenden Tag anteilmässig; Wertschriften-/Liegenschaftserträge gehören ins WV bzw. Liegenschaftenverzeichnis.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «Ertrag aus Geschäfts- und Korporationsanteilen Aufstellung 162»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0058.md) `zh-wl-2025__c0058` – «Einkünfte aus Geschäfts- und Korporationsanteilen sind von den Inhabern anteilmässig ent-»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0149.md) `zh-wl-2025__c0149` – «Das Einkommen aus unverteilten Erb-»

<a id="5-4-einkommen-uebrige"></a>
### Ziff. 5.4 – Weitere Einkünfte, nähere Bezeichnung (Code 163)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung (z. B. im Lohnausweis nicht ausgewiesene Trinkgelder, Renten bei Tod/Nachteilen, Bundesbeiträge Prüfungskurse)
- **Regel:** Auffangzeile für alle weiteren steuerbaren Einkünfte inkl. Naturalbezüge; Bundesbeiträge an Prüfungsvorbereitungskurse nur soweit sie die effektiven Weiterbildungskosten übersteigen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «Weitere Einkünfte, nähere Bezeichnung:»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0058.md) `zh-wl-2025__c0058` – «Bitte beachten Sie, dass grundsätzlich alle wiederkehrenden und einmaligen Einkünfte, mit»

<a id="5-5-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 5.5 – Kapitalabfindungen für wiederkehrende Leistungen (Code 164)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der auszahlenden Stelle (Betrag und Anzahl Monate)
- **Regel:** Die Abfindung wird zur Satzbestimmung auf den Betrag der jährlichen Leistung umgerechnet; Anzahl Monate in der Vorkolonne angeben. Kapitalleistungen aus Vorsorge gehören NICHT hierher, sondern in Ziff. 40.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «Kapitalabfindungen für wiederkehrende Leistungen»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0059.md) `zh-wl-2025__c0059` – «Diese werden bei der Ermittlung des Steuersatzes zu dem Betrag eingesetzt, welcher der»

<a id="6-einkommen-liegenschaften-mietertrag"></a>
### Ziff. 6 – Nettoertrag aus Liegenschaften (Code 188) – Übertrag aus Liegenschaftenverzeichnis

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Liegenschaftenverzeichnis (Form. 350) Seite 2: Nettoertrag aus Liegenschaften (Code 3953)
- **Regel:** Erträge (Eigenmietwert, Mietzinsen) abzüglich Unterhalts- und Verwaltungskosten (pauschal oder effektiv) je Liegenschaft im Form. 350 berechnen; nur der Nettobetrag kommt in Ziff. 6. Unterhaltskosten sind hier bereits abgezogen (kein Doppelabzug in Ziff. 16).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «6. Nettoertrag aus Liegenschaften Liegenschaftenverzeichnis 188»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0004.md) `zh-form-350__c0004` – «Nettoertrag aus Liegenschaften 3953»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0059.md) `zh-wl-2025__c0059` – «Erträge aus Liegenschaften sowie die Unterhaltskosten sind im Formular»

<a id="7-berechnung-total"></a>
### Ziff. 7 – Total der Einkünfte (Code 199)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 1–6)
- **Regel:** Rechenzeile: Übertrag auf Seite 3, Ziffer 19.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «7. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 19»

## Abzüge

<a id="11-1-11-2-berechnung-total"></a>
### Ziff. 11.1 / 11.2 – Berufsauslagen bei unselbständiger Erwerbstätigkeit, Person 1 (Code 220) / Person 2 (Code 240)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 360 Ziff. 6 «Total der Berufsauslagen» (Staats- und Bundessteuer getrennte Spalten)
- **Regel:** Pro Person Formular «Berufsauslagen» (Form. 360) ausfüllen und beilegen; Total in Ziff. 11.1/11.2 übertragen. Staats- und Bundessteuer-Spalte können abweichen (Fahrkosten-Plafond). Vom Arbeitgeber vergütete Berufsauslagen sind nicht abziehbar.
- **Bund:** Bundessteuer-Spalte separat (Fahrkostenplafond CHF 3’300 statt CHF 5’200).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «11.1 Person 1 Berufsauslagen 220»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0060.md) `zh-wl-2025__c0060` – «Formular «Berufsauslagen» beizulegen und können ihre Berufsauslagen, soweit sie nicht vom»
  - [LS 631.33 (bis 2025) S. 3–4](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0007.md) `zh-pauschalierung-berufsauslagen-2025__c0007` – «Soweit Berufsauslagen vom Arbeitgeber vergütet werden, steht»

<a id="12-abzug-schuldzinsen"></a>
### Ziff. 12 – Schuldzinsen (Code 250)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen) → Schuldenverzeichnis (Form. 355) Total private Schuldzinsen (Code 3201); Zinsausweis/Hypothekarbestätigung per 31.12.
- **Regel:** Private Schuldzinsen sind abziehbar bis zur Höhe der steuerbaren Vermögenserträge (inkl. Eigenmietwert) plus CHF 50’000. Amortisationen und Leasingraten sind nicht abziehbar. Baurechtszinsen gehören zu den Liegenschaftskosten (Form. 350), nicht hierher.
- **Bund:** Gleich: Art. 33 Abs. 1 lit. a DBG (Vermögenserträge + CHF 50’000).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «12. Schuldzinsen (soweit nicht schon unter Ziff. 2 abgezogen) Schuldenverzeichnis 250»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0074.md) `zh-wl-2025__c0074` – «mögen (inkl. Eigenmietwert) und weiterer CHF 50’000 nicht übersteigen.»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0073.md) `zh-wl-2025__c0073` – «abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t1.md) `zh-stg-2025__par-31-t1` – «die privaten Schuldzinsen im Umfang der nach den §§ 20, 20 a und 21 steuerbaren Vermögenserträge und weiterer Fr. 50 000»

<a id="13-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 13.1 – Unterhaltsbeiträge an geschiedenen / getrennt lebenden Ehegatten (Code 254)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil + Zahlungsnachweise (Jahressumme)
- **Regel:** Für den Ehegatten persönlich bestimmte Beiträge voll abziehbar; sämtliche Zahlungsnachweise einreichen. Der Empfänger deklariert sie in Ziff. 5.1.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «13.1 Unterhaltsbeiträge an den geschiedenen oder getrennt lebenden Ehegatten / Partn. 254»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0075.md) `zh-wl-2025__c0075` – «Ehegatten persönlich bestimmt sind, können voll abgezogen werden.»

<a id="13-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 13.2 – Unterhaltsbeiträge für minderjährige Kinder (Code 255)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Urteil/Vereinbarung + Zahlungsnachweise bis und mit Monat des 18. Geburtstags
- **Regel:** Abziehbar bis und mit dem Monat der Volljährigkeit; danach steht dem Zahlenden stattdessen der Kinderabzug zu (Ziff. 24.1). Spätere Zahlungen nicht mehr abziehbar.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «13.2 Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit)»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0076.md) `zh-wl-2025__c0076` – «werden, in dem das Kind das 18. Altersjahr erreicht.»

<a id="13-3-abzug-uebrige"></a>
### Ziff. 13.3 – Rentenleistungen / dauernde Lasten, abzugsfähig: Ertragsanteil (Code 256)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ⚠️ strittig
- **Beleg → Feld:** – → Leibrentenvertrag / Verpfründungsvertrag; Zahlungsnachweise
- **Regel:** Bezahlte Leibrenten und Verpfründungen: abziehbar ist der Ertragsanteil = bezahlte Rente x ESTV-Berechnungssatz / 100; Betrag der Leistung in Vorkolonne, abzugsfähiger Ertragsanteil in Hauptkolonne. STRITTIG für die Staatssteuer: StG § 31 Abs. 1 lit. b nennt 40 % der bezahlten Leibrenten.
- **Bund:** Bund: Art. 33 Abs. 1 lit. b DBG – Ertragsanteil nach Art. 22 Abs. 3 lit. c DBG.
- **Bemerkung:** Wie Ziff. 3.2 (Leibrenten): StG ZH § 31 Abs. 1 lit. b (zh-stg-2025) = 40 Prozent der bezahlten Leibrenten; WL 2025 (c0078) = Ertragsanteil nach ESTV-Satz. Bund (bund-dbg-2025__art-33-t1): «der Ertragsanteil nach Artikel 22 Absatz 3 Buchstabe c». Fachperson entscheidet für die Staatssteuer. Gegenprobe Prüfung: Bundesrecht (Art. 33 Abs. 1 lit. b DBG) und StHG gelten nach Art. 72 Abs. 2 StHG direkt, falls kantonales Recht widerspricht; Fachperson entscheidet.
- **Quellen:**
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0078.md) `zh-wl-2025__c0078` – «Abzugsfähig ist der Ertragsanteil der bezahlten Leibrenten und Verpfründungen.»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t1.md) `zh-stg-2025__par-31-t1` – «die dauernden Lasten sowie 40 Prozent der bezahlten Leibrenten»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «der Ertragsanteil nach Artikel 22 Absatz 3 Buchstabe c der Leistungen aus Leibrenten- und aus Verpfründungsverträgen»

<a id="14-1-14-2-abzug-vorsorge-saeule3a"></a>
### Ziff. 14.1 / 14.2 – Beiträge Säule 3a, Person 1 (Code 260, eff. 262) / Person 2 (Code 261, eff. 263)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Bescheinigung der Bankstiftung / Versicherung (im Jahr 2025 tatsächlich einbezahlter Betrag)
- **Regel:** Nur im Jahr 2025 tatsächlich einbezahlte Beiträge. Mit 2. Säule: max. CHF 7’258; ohne 2. Säule: 20 % des Erwerbseinkommens, max. CHF 36’288. Beide erwerbstätigen Ehegatten je einzeln (eigener Vorsorgevertrag). Mitarbeit im Betrag des Ehegatten nur bei echtem Arbeitsverhältnis. Bescheinigung beilegen.
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a: Erwerbstätige mit Pensionskasse (2. Säule): max. CHF 7'258 (Bemessungsjahr 2025).)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug mit Zugehörigkeit zur 2. Säule (8 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a: Erwerbstätige ohne 2. Säule: 20 % des Erwerbseinkommens, max. CHF 36'288.)** · Bund **CHF 36'288 (Säule 3a: Höchstabzug ohne 2. Säule (max. 36'288, 40 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. CHF 36'288).)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. CHF 36'288))**
- **Bund:** Gleiche Höchstbeträge (BVV 3); gleiche Zeile für Staat und Bund.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «14. Beiträge an anerkannte Formen der geb. Selbstvorsorge (3. Säule a)»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0081.md) `zh-wl-2025__c0081` – «für Steuerpflichtige, die einer Einrichtung der beruflichen Vorsorge (2. Säule) angehören,»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0081.md) `zh-wl-2025__c0081` – «höchstens 20% des Erwerbseinkommens, maximal aber CHF 36’288.»
  - [ZStB 31.1 (bis 2026) S. 1](../../chunks/zh/2025/zh-zstb-31-1-bis-2026/zh-zstb-31-1-bis-2026__c0002.md) `zh-zstb-31-1-bis-2026__c0002` – «ab 2025 7 258 36 288»

<a id="14-3-ab-2026-abzug-vorsorge-saeule3a-einkauf"></a>
### Ziff. 14.3 (ab 2026) – Einkauf (Nachzahlung) Säule 3a – im Formular 2025 nicht vorhanden

- **Schlüssel:** `abzug.vorsorge.saeule3a_einkauf` (Einkauf (Nachzahlung) Säule 3a – ab Steuerjahr 2026) · **Status:** – na
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → –
- **Regel:** Das Formular 300 für 2025 hat keine Zeile 14.3 (Ziff. 14 nur Person 1/2). 3a-Einkäufe sind erst ab dem Steuerjahr 2026 (Beitragslücken ab 2025) abziehbar – für Steuerjahr 2025 nicht deklarieren.
- **Bemerkung:** Formular 300 ZH 2025 (zh-form-300-2025__c0008) enthält nur Ziff. 14.1/14.2; Einkauf 3a wird in der Zuordnung ZH 2026 behandelt.

<a id="15-abzug-versicherungspraemien"></a>
### Ziff. 15 – Versicherungsprämien und Zinsen von Sparkapitalien (Code 270)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 365 Teil C (Code 270): niedrigerer Betrag von (A) bezahlte Prämien und (B) Maximalabzug
- **Regel:** Im Form. 365 Teil A bezahlte Prämien (KK, Unfall, Leben/Rente, Sparzinsen, abzüglich Prämienverbilligung) mit Teil B (Maximalabzug) vergleichen; der niedrigere Betrag nach Ziff. 15. Erhaltene Prämienverbilligung ist abzuziehen, soweit nicht schon in den Prämien berücksichtigt.
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'800 (Versicherungsprämien und Sparzinsen, in ungetrennter Ehe Lebende, MIT Beiträgen an 2. Säule/Säule 3a: max. CHF 5'800 (Staatssteuer).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 8'700 (Gemeinsam Besteuerte ohne Beiträge an 2. Säule und Säule 3a: Abzug erhöht sich um die Hälfte, max. CHF 8'700.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an Säule 2/3a (Erhöhung um die Hälfte))**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'900 (Übrige Steuerpflichtige MIT Beiträgen an 2. Säule/Säule 3a: max. CHF 2'900 (Staatssteuer).)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 4'350 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule/3a: max. CHF 4'350 (2'900 + die Hälfte).)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'300 (Zusätzlicher Versicherungsabzug von CHF 1'300 für jedes Kind oder jede unterstützungsbedürftige Person, für die ein Abzug nach § 34 Abs. 1 geltend gemacht werden kann (Bund: CHF 700).)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
- **Bund:** Bundessteuer-Spalte mit tieferen Maxima (Form. 365 Teil B).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «15. Versicherungsprämien, Zinsen von Sparkapitalien Versich.prämien 270»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0082.md) `zh-wl-2025__c0082` – «Der zulässige Abzug für Versicherungsprämien und Sparzinsen ist im Formular Versicherungs-»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0003.md) `zh-form-365-2025__c0003` – «Der niedrigere Betrag: (A) oder (B) 270»

<a id="16-1-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 16.1 – Beiträge an 2. Säule inkl. Einkäufe, soweit nicht im Lohnausweis abgezogen (Code 280)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) – nur selbst bezahlte, nicht vom Lohn abgezogene Beiträge/Einkäufe
- **Regel:** Nur Einkäufe/Beiträge eintragen, die NICHT bereits im Lohnausweis (Ziff. 10.1/10.2) vom Lohn abgezogen sind. Einkäufe sind nicht abziehbar, soweit innert drei Jahren ein Kapitalbezug erfolgt (Sperrfrist). Bescheinigung beilegen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.1 Beiträge an die AHV, IV und 2. Säule, sofern nicht unter Ziff. 1 und 2 abgezogen 280»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0092.md) `zh-wl-2025__c0092` – «Weiter ist zu beachten, dass Einkäufe steuerlich nicht zum Abzug zugelassen»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0092.md) `zh-wl-2025__c0092` – «werden, soweit innerhalb von drei Jahren ein Kapitalbezug erfolgt.»

<a id="16-1-abzug-ahv-nichterwerbstaetige"></a>
### Ziff. 16.1 – Beiträge an AHV/IV (z. B. Nichterwerbstätige, Selbständige ohne Abzug im Hilfsblatt) (Code 280)

- **Schlüssel:** `abzug.ahv_nichterwerbstaetige` (AHV/IV/EO-Beiträge Nichterwerbstätiger u.ä.) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse) → AHV-Beitragsverfügung / Bescheinigung der Ausgleichskasse
- **Regel:** AHV-/IV-Beiträge nur abziehen, soweit die unter Ziff. 1 und 2 deklarierten Einkünfte nicht schon um diese Beiträge gekürzt wurden. Bescheinigung beilegen.
- **Quellen:**
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0092.md) `zh-wl-2025__c0092` – «Beiträge an die AHV und IV, soweit die unter Ziffern 1 und 2 der Steuererklärung deklarierten»

<a id="16-2-abzug-weiterbildung"></a>
### Ziff. 16.2 – Berufsorientierte Aus- und Weiterbildungskosten (Code 292)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Formular 367 (selbstgetragene Kosten nach Abzug Arbeitgeberbeitrag) + Kursrechnungen / Zahlungsnachweise
- **Regel:** Selbst getragene Kosten (nach Abzug Beiträge Dritter, z. B. Arbeitgeber/Bund) bis max. CHF 12’400 (Staat) bzw. CHF 13’000 (Bund), sofern Abschluss Sek. II vorliegt oder 20. Altersjahr vollendet und nicht Ausbildung bis zum ersten Sek.-II-Abschluss. Massgebend ist Fälligkeit/Zahlung, nicht der Kursbesuch. Lohnausweis Ziff. 13.3 beachten.
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 12'400 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung, selbst getragene Kosten: max. CHF 12'400 (Staatssteuer), sofern Abschluss Sek. II vorliegt oder 20. Lebensjahr vollendet (und nicht Ausbildung bis zum ersten Sek.-II-Abschluss).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Bund:** Bund: max. CHF 13’000 (Bundessteuer-Spalte, Form. 367 Code 2921/292).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.2 Berufsorientierte Aus- und Weiterbildungskosten Hilfsblatt 292»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0093.md) `zh-wl-2025__c0093` – «betrag von CHF 12’400 bei der Staatssteuer bzw. CHF 13’000 bei der Bundessteuer, sofern ein»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t4.md) `zh-stg-2025__par-31-t4` – «die Kosten der berufsorientierten Aus- und Weiterbildung, einschliesslich Umschulungskosten, bis zum Gesamtbetrag von Fr. 12 400»

<a id="16-3-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. 16.3 – Kosten für die Verwaltung des beweglichen Privatvermögens (Code 283)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.) → Depotgebührenausweis / Steuerauszug (Verwaltungs- und Verwahrungskosten Dritter)
- **Regel:** Verwaltungs-/Verwahrungskosten durch Dritte abziehbar, nicht aber Erwerbs-/Veräusserungskosten (Courtagen, Stempel). Pauschal 3 ‰ des Steuerwerts der durch Dritte verwalteten Wertschriften, max. CHF 6’000, oder höhere effektive Kosten mit Nachweis.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.3 Kosten für die Verwaltung des beweglichen Privatvermögens 283»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0095.md) `zh-wl-2025__c0095` – «können 3‰ des Steuerwerts dieser durch Dritte verwalteten Wertschriften, maximal»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0095.md) `zh-wl-2025__c0095` – «jedoch CHF 6’000, abgezogen werden.»

<a id="16-4-abzug-behinderungskosten"></a>
### Ziff. 16.4 – Behinderungsbedingte Kosten (Code 3160)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Formular 370 Seite 2 «Aufstellung über behinderungsbedingte Kosten» (Total abzugsberechtigte Kosten, Code 3155 / Pauschale 3103)
- **Regel:** Behinderungsbedingte Kosten (Behindertengleichstellungsgesetz), soweit selbst getragen; Vergütungen Dritter (Krankenkasse, Hilflosenentschädigung, Anteil Lebenshaltungskosten) abziehen. Formular 370 Rückseite einreichen. Kein Selbstbehalt, zu unterscheiden von Krankheitskosten Ziff. 22.1.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.4 Behinderungsbedingte Kosten Hilfsblatt 3160»
  - [Formular 370 ZH S. 2](../../chunks/zh/2025/zh-form-370/zh-form-370__c0006.md) `zh-form-370__c0006` – «Total der abzugsberechtigten Kosten 3155»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t3.md) `zh-stg-2025__par-31-t3` – «die behinderungsbedingten Kosten des Steuerpflichtigen»

<a id="16-5-abzug-parteispenden"></a>
### Ziff. 16.5 – Beiträge und Zuwendungen an politische Parteien (Code 284, Aufstellung)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Spendenbestätigung der Partei (Parteienregister / Kantonsparlament / ≥ 3 % Wähleranteil)
- **Regel:** Staatssteuer max. CHF 20’600 (in ungetrennter Ehe) bzw. CHF 10’300 (übrige); Bundessteuer max. CHF 10’600 (für alle). Nur Parteien im Parteienregister, mit Sitz im kantonalen Parlament oder mit mind. 3 % Stimmen.
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'300 (Mitgliederbeiträge und Zuwendungen an politische Parteien (im Parteienregister eingetragen, im kantonalen Parlament vertreten oder mind. 3 % Wähleranteil): max. CHF 10'300 für übrige Steuerpflichtige.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 20'600 (Parteispenden gemeinsam Besteuerte (ungetrennte Ehe): max. CHF 20'600.)** · Bund **n/a – Bund kennt nur einen Gesamtbetrag von CHF 10'600 (Art. 33 Abs. 1 lit. i DBG); keine Verdoppelung für Ehepaare in der Quelle.**
- **Bund:** Bund: max. CHF 10’600 für Verheiratete und Übrige (Art. 33 Abs. 1 lit. i DBG).
- **Quellen:**
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0100.md) `zh-wl-2025__c0100` – «Höchstbetrag von CHF 20’600 für in ungetrennter Ehe lebende Steuerpflichtige und von»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0100.md) `zh-wl-2025__c0100` – «Der Höchstbetrag für solche Abzüge beträgt CHF 10’600.»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t3.md) `zh-stg-2025__par-31-t3` – «bis zum Gesamtbetrag von Fr. 20 600 für in ungetrennter Ehe lebende Steuerpflichtige und von Fr. 10 300 für die übrigen Steuerpflichtigen»

<a id="16-5-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 16.5 – Weitere Abzüge: Teilbesteuerung qualifizierte Beteiligungen (Abzug 50 % Staat / 30 % Bund)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular «Qualifizierte Beteiligungen im Privatvermögen / Geschäftsvermögen» + Dividendenbeleg
- **Regel:** Nicht steuerbarer Teil der in Ziff. 4.2 deklarierten Erträge aus qualifizierten Beteiligungen: Privatvermögen 50 % (Staat) bzw. 30 % (Bund); gratis abgegebene Mitarbeiteraktien: kein Abzug. Betrag in Ziff. 16.5 (Staats-/Bundessteuer-Spalte unterschiedlich).
- **Bund:** Bund: 30 % statt 50 %.
- **Quellen:**
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md) `zh-wl-2025__c0104` – «Privatvermögen beträgt 50%, für qualifizierte Beteiligungen»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md) `zh-wl-2025__c0104` – «Privatvermögen beträgt 30%, für qualifizierte Beteiligungen»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md) `zh-wl-2025__c0104` – «Bei gratis abgegebenen Mitarbeiteraktien kann kein Abzug vorgenommen werden.»

<a id="16-5-abzug-uebrige"></a>
### Ziff. 16.5 – Weitere Abzüge (Freitext, Code 284): Liquidationsgewinne, Grundstückgewinn-Freistellung, Einsatzkosten Geldspiele

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung / Hilfsformular (z. B. Liquidationsgewinn-Formular, Spielgewinn-Abrechnung)
- **Regel:** Liquidationsgewinne aus Ziff. 2.1 (gesonderte Besteuerung), freizustellender Teil des Grundstückgewinns (Staatssteuer), 5 % Einsatzkosten bei Geldspielgewinnen (max. CHF 5’200 Staat / CHF 5’400 Bund), Patentbox/F&E-Zusatzabzug (Form. 547).
- **Quellen:**
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0105.md) `zh-wl-2025__c0105` – «Für die Staatssteuer ist der bei der Einkommenssteuer freizustellende Teil des Grund»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0105.md) `zh-wl-2025__c0105` – «Selbständig Erwerbende, welche die Patentbox oder den Zusatzabzug für Forschungs- und»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0043.md) `zh-wl-2025__c0043` – «Solche Liquidationsgewinne können unter Ziffer 16.5 wieder von den Einkünften abgezogen werden»

<a id="16-6-abzug-drittbetreuung"></a>
### Ziff. 16.6 – Abzug für fremdbetreute Kinder (Jahrg. 2011–2025) (Code 376)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Rechnungen/Quittungen Kita, Tagesfamilie, Hort etc. mit Zahlungsnachweis (Name Kind, Zeitraum)
- **Regel:** Nachgewiesene Kosten für jedes Kind unter 14 Jahren im gleichen Haushalt, max. CHF 25’000 (Staat) bzw. CHF 25’800 (Bund) pro Kind; Kosten müssen in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit stehen. Konkubinat mit gemeinsamer Sorge: je halber Abzug (max. CHF 12’500 Staat / CHF 12’900 Bund). Verpflegung/Schulgeld nicht betreuungsbedingt.
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 25'000 (Nachgewiesene Kinderdrittbetreuungskosten: max. CHF 25'000 pro Kind (Staatssteuer), wenn Kind unter 14, im gleichen Haushalt, und Kosten in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind bis max. CHF 25'800 (Kind unter 14, im gleichen Haushalt, Zusammenhang mit Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit))**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 Jahre (Kind darf das 14. Altersjahr noch nicht vollendet haben.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat)**
- **Bund:** Bund: max. CHF 25’800 pro Kind (Art. 33 Abs. 3 DBG).
- **Bemerkung:** Hinweis: Die VKP ZH ab 2024 (zh-vkp-2024-zstb__c0005) nennt noch Fr. 10 400 für § 31 Abs. 1 lit. j; für 2025 gilt gemäss StG ZH Nachtrag 127 (zh-stg-2025__par-31-t4), Formular und WL der Betrag CHF 25’000 – die Verordnung 10’400 ist überholt und nicht anzuwenden.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.6 Abzug für fremdbetreute Kinder (Jahrg. 2011-2025) max. 25’000 / 25’800 376»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t4.md) `zh-stg-2025__par-31-t4` – «die nachgewiesenen Kosten, jedoch höchstens Fr. 25 000, für die Drittbetreuung jedes Kindes»
  - [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0107.md) `zh-wl-2025__c0107` – «CHF 25’800 (Bundessteuer) pro Kind. Für jedes Kind, welches das 14. Altersjahr noch nicht»
  - [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0109.md) `zh-wl-2025__c0109` – «machen. Der halbe Abzug beträgt je höchstens CHF 12’500 (Staatssteuer) bzw. CHF 12’900»

<a id="17-abzug-zweiverdiener"></a>
### Ziff. 17 – Sonderabzug bei Erwerbstätigkeit beider Ehegatten / Partner (Code 290)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Berechnung aus verbleibendem niedrigerem Erwerbseinkommen (Ziff. 1–2 abzüglich Berufsauslagen, 3a, 2.-Säule-Einkäufe, nicht über Lohnausweis berücksichtigte AHV/BVG)
- **Regel:** Nur für in ungetrennter Ehe lebende, beide erwerbstätige Ehegatten, einmal pro Paar. Staatssteuer: max. CHF 6’100 (vom niedrigeren verbleibenden Erwerbseinkommen, bei Mitarbeit vom gemeinsamen). Bundessteuer: 50 % des niedrigeren Erwerbseinkommens, mind. CHF 8’600, max. CHF 14’100; unter CHF 8’600 Abzug in Höhe des Einkommens.
- **Limiten:**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **n/a – ZH: kein Minimum; liegt das tiefere Erwerbseinkommen unter CHF 6'100, wird nur dieser tiefere Betrag abgezogen (WL ZH 2025 Ziff. 17).** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum)**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **CHF 6'100 (Zweiverdienerabzug bei ungetrennter Ehe: CHF 6'100 vom (niedrigeren) Erwerbseinkommen; bei erheblicher Mitarbeit im Geschäft des Ehegatten vom gemeinsamen Erwerbseinkommen; ist dieses tiefer, nur der tiefere Betrag.)** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum)**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **n/a – ZH: fixer Abzug von CHF 6'100 (bzw. tieferes Erwerbseinkommen), kein Prozentsatz (§ 31 Abs. 2 StG). Der Prozentsatz-Mechanismus gilt nur beim Bund.** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (bei Ehegatten in ungetrennter Ehe mit beidseitigem Erwerbseinkommen))**
- **Bund:** Bund: 50 % des niedrigeren Erwerbseinkommens, mind. CHF 8’600, max. CHF 14’100 (Art. 33 Abs. 2 DBG).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «17. Sonderabzug bei Erwerbstätigkeit beider Ehegatten/Partn.»
  - [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0112.md) `zh-wl-2025__c0112` – «Der Abzug beträgt max. CHF 6’100 und steht wie folgt zu:»
  - [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0113.md) `zh-wl-2025__c0113` – «mens, jedoch mind. CHF 8’600 und max. CHF 14’100;»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t5.md) `zh-stg-2025__par-31-t5` – «Fr. 6100 abgezogen»

<a id="18-berechnung-total"></a>
### Ziff. 18 – Total der Abzüge (Code 299)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 11–17)
- **Regel:** Rechenzeile; Übertrag in Ziffer 20.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «18. Total der Abzüge, zu übertragen in Ziffer 20»

## Einkommensberechnung

<a id="19-berechnung-total"></a>
### Ziff. 19 – Total der Einkünfte (Code 199)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Übertrag Seite 2, Ziffer 7
- **Regel:** Rechenzeile: Übertrag von Ziff. 7.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «19. Total der Einkünfte Übertrag von Seite 2, Ziffer 7»

<a id="20-berechnung-total"></a>
### Ziff. 20 – Total der Abzüge (Code 299)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Übertrag Ziffer 18
- **Regel:** Rechenzeile: Übertrag von Ziff. 18; Subtraktion von Ziff. 19.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «20. Total der Abzüge Übertrag von Ziffer 18»

<a id="21-berechnung-total"></a>
### Ziff. 21 – Nettoeinkommen (Code 310)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 19 – Ziff. 20)
- **Regel:** Rechenzeile; Basis für den Selbstbehalt Krankheitskosten (5 %) und die Obergrenze gemeinnütziger Zuwendungen (20 %).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «21. Nettoeinkommen 310»

<a id="22-1-abzug-krankheitskosten"></a>
### Ziff. 22.1 – Krankheits- und Unfallkosten (Code 320) – über Selbstbehalt 5 % des Nettoeinkommens

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 370 Seite 1, Teil E: Abzug (Code 320) nach Selbstbehalt
- **Regel:** Selbst getragene Kosten (Franchise/Selbstbehalt, Arzt, Zahnarzt, Pflege, Spital, Therapien) abzüglich Vergütungen Dritter, soweit sie 5 % des Nettoeinkommens (Ziff. 21) übersteigen; Staats- und Bundessteuer je mit eigenem Netto. Nicht abziehbar: Prävention, Fahrkosten, Wellness etc. Diät-Pauschale CHF 2500 bei dauernder lebensnotwendiger Diät. Formular 370 und Belege beilegen.
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen nach §§ 26–31 verminderten steuerbaren Einkünfte (Nettoeinkommen, Ziff. 21) übersteigen. Behinderungsbedingte Kosten ohne Selbstbehalt (§ 31 lit. i).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Bund:** Bund: Selbstbehalt 5 % des Nettoeinkommens nach Bundessteuer-Spalte (Art. 33 Abs. 1 lit. h DBG).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «22.1 Krankheits- und Unfallkosten Hilfsblatt 320»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «abzüglich Selbstbehalt (5% von Ziffer 21 der»
  - [StG ZH § 32](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-32.md) `zh-stg-2025__par-32` – «diese 5 Prozent der um die Aufwendungen gemäss §§ 26–31 verminderten steuerbaren Einkünfte übersteigen»

<a id="22-2-abzug-spenden"></a>
### Ziff. 22.2 – Gemeinnützige Zuwendungen (Code 324)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigung (Empfänger im Verzeichnis steuerbefreiter Institutionen) + Aufstellung
- **Regel:** Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz bzw. Bund/Kantone/Gemeinden: mind. CHF 100 pro Jahr (gesamthaft), max. 20 % des Nettoeinkommens (Ziff. 21). Aufstellung beilegen; Belege auf Verlangen.
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz / öffentliche Hand: abzugsfähig, wenn sie in der Steuerperiode insgesamt mind. CHF 100 erreichen.)** · Bund **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen (CH) bzw. Gemeinwesen: mindestens CHF 100 im Steuerjahr)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen insgesamt max. 20 % der um die Aufwendungen nach §§ 26–31 verminderten steuerbaren Einkünfte (Nettoeinkommen).)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Bund:** Bund: Art. 33a DBG – ebenfalls mind. CHF 100 und max. 20 % der um die Aufwendungen verminderten Einkünfte.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «22.2 Gemeinnützige Zuwendungen Aufstellung 324»
  - [WL ZH 2025 S. 19](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0122.md) `zh-wl-2025__c0122` – «die Zuwendungen in der Steuerperiode CHF 100 erreichen und soweit sie insgesamt 20%»
  - [WL ZH 2025 S. 19](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0122.md) `zh-wl-2025__c0122` – «des Nettoeinkommens (Ziffer 21 der Steuererklärung) nicht übersteigen.»
  - [ZH Spenden](../../chunks/zh/dauernd/zh-info-spenden/zh-info-spenden__c0003.md) `zh-info-spenden__c0003` – «Die Zuwendungen in einem Jahr gesamthaft mindestens CHF 100 betragen.»

<a id="23-berechnung-total"></a>
### Ziff. 23 – Reineinkommen (Code 350)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 21 – 22.1 – 22.2)
- **Regel:** Rechenzeile.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «23. Reineinkommen (Ziffer 21 abzüglich Ziffern 22.1 und 22.2) 350»

<a id="24-1-sozialabzug-kinder"></a>
### Ziff. 24.1 – Abzug für Kinder in Ihrem Haushalt (Code 370)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Kinder Jg. 2008–2025 oder in beruflicher Erstausbildung); Stand 31.12.2025
- **Regel:** Staatssteuer CHF 9’300 pro Kind, Bundessteuer CHF 6’800 pro Kind (Verhältnisse am Ende der Steuerperiode). Verheiratete/verwitwete: voll; Alleinerziehende: voll bei alleinigem Sorgerecht bzw. bei gemeinsamem Sorgerecht mit erhaltenen Unterhaltsbeiträgen, sonst halb (CHF 4’650 / 3’400). Volljährige Kinder nur in beruflicher Erstausbildung mit überwiegendem Unterhalt.
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 9'300 (Kinderabzug je Kind: CHF 9'300 (minderjährige Kinder unter elterlicher Sorge/Obhut; volljährige in beruflicher Erstausbildung, deren Unterhalt zur Hauptsache bestritten wird). Bei nicht gemeinsam besteuerten Eltern mit gemeinsamer Sorge hälftig.)** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
- **Bund:** Bund: CHF 6’800 pro Kind (Art. 35 Abs. 1 lit. a DBG).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «Abzug für Kinder in Ihrem Haushalt (gemäss Seite 1) 9’300»
  - [WL ZH 2025 S. 20](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0126.md) `zh-wl-2025__c0126` – «CHF 9’300 pro Kind CHF 6’800 pro Kind»
  - [StG ZH § 34](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-34.md) `zh-stg-2025__par-34` – «a. als Kinderabzug: für minderjährige Kinder unter elterlicher Sorge oder Obhut des Steuerpflichtigen sowie»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «6800 Franken für jedes minderjährige oder in der beruflichen oder schulischen Ausbildung stehende Kind»

<a id="24-1-sozialabzug-kinder-2"></a>
### Ziff. 24.1 – Abzug für Kinder ausserhalb Ihres Haushaltes (Code 372)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Kinder ausserhalb des Haushalts, Adresse); Nachweis Unterhalt
- **Regel:** Nicht zusammenlebende Eltern: halber Kinderabzug (CHF 4’650 / 3’400) bei gemeinsamem Sorgerecht ohne abgezogene Unterhaltsbeiträge; wer Kinderalimente bezahlt (Ziff. 13.2) oder kein Sorgerecht hat: kein Kinderabzug. Volljährige Kinder in Erstausbildung: ganzer Abzug, wenn Unterhaltsbeiträge den Hauptunterhalt decken.
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 9'300 (Kinderabzug je Kind: CHF 9'300 (minderjährige Kinder unter elterlicher Sorge/Obhut; volljährige in beruflicher Erstausbildung, deren Unterhalt zur Hauptsache bestritten wird). Bei nicht gemeinsam besteuerten Eltern mit gemeinsamer Sorge hälftig.)** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
- **Bund:** Bund: CHF 6’800 bzw. halb CHF 3’400.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «Abzug für Kinder ausserhalb Ihres Haushaltes (gem. S. 1) 9’300»
  - [WL ZH 2025 S. 20](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0129.md) `zh-wl-2025__c0129` – «können Sie die Hälfte des Kinderabzugs geltend»

<a id="24-2-sozialabzug-unterstuetzung"></a>
### Ziff. 24.2 – Abzug für unterstützte Personen (Code 374)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bestätigung der unterstützten Person (Art, Zeitpunkt, Höhe der Unterstützung) + Zahlungsbelege auf Verlangen
- **Regel:** Für erwerbsunfähige / beschränkt erwerbsfähige Personen, wenn mindestens in der Höhe des Abzugs unterstützt wird: Staat CHF 2’800, Bund CHF 6’800. Nicht für Ehegatten, nicht für Kinder mit Kinderabzug, nicht bei gleichzeitigem Abzug von Alimenten.
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'800 (Unterstützungsabzug je erwerbsunfähige/beschränkt erwerbsfähige Person, an deren Unterhalt mindestens in Höhe des Abzugs beigetragen wird (nicht für Ehegatten und Kinder mit Abzug nach lit. a oder § 31 lit. c).)** · Bund **CHF 6'800 (Unterstützungsabzug pro erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mindestens in Höhe des Abzugs unterstützt; nicht für Ehegatten und Kinder mit Kinderabzug)**
- **Bund:** Bund: CHF 6’800 (Art. 35 Abs. 1 lit. b DBG).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «24.2 Abzug für unterstützte Personen Bestätigung»
  - [StG ZH § 34](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-34.md) `zh-stg-2025__par-34` – «b. als Unterstützungsabzug: für erwerbsunfähige oder beschränkt erwerbsfähige Personen, an deren Unterhalt der»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0135.md) `zh-wl-2025__c0135` – «leistung mindestens in der Höhe des Unterstützungsabzuges von CHF 2’800.»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0135.md) `zh-wl-2025__c0135` – «leistung mindestens in der Höhe des Unterstützungsabzuges von CHF 6’800.»

<a id="24-3-sozialabzug-verheiratete"></a>
### Ziff. 24.3 – Abzug für Ehegatten / Partner – nur Bundessteuer (Code 365)

- **Schlüssel:** `sozialabzug.verheiratete` (Verheiratetenabzug (Bund)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand am 31.12.2025 (Seite 1)
- **Regel:** Nur bei der direkten Bundessteuer: CHF 2’800 für in rechtlich und tatsächlich ungetrennter Ehe lebende Steuerpflichtige. Die Staatssteuer kennt keinen Verheiratetenabzug (Tarifsplitting über Verheiratetentarif).
- **Limiten:**
  - Verheiratetenabzug (CHF, Bund): Kanton **n/a – Verheiratetenabzug existiert nur bei der direkten Bundessteuer (Bund-Datei); ZH Staatssteuer kennt Verheiratetentarif statt Abzug.** · Bund **CHF 2'800 (Verheiratetenabzug für Ehepaare in rechtlich und tatsächlich ungetrennter Ehe)**
- **Bund:** Nur Bund: CHF 2’800 (Art. 35 Abs. 1 lit. c DBG).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «24.3 Abzug für Ehegatten / Partn.»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0135.md) `zh-wl-2025__c0135` – «Bei der Bundessteuer gibt es für alle in rechtlich und tatsächlich ungetrennter Ehe lebenden»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «2800 Franken für Ehepaare, die in rechtlich und tatsächlich ungetrennter Ehe leben.»

<a id="25-berechnung-total"></a>
### Ziff. 25 – Steuerbares Einkommen gesamt (Code 390)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 23 – 24.1 bis 24.3)
- **Regel:** Rechenzeile.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «25. Steuerbares Einkommen gesamt (Ziffer 23 abz. Ziff. 24.1 bis 24.3) 390»

<a id="26-1-26-2-berechnung-total"></a>
### Ziff. 26.1 / 26.2 – Davon auf steuerbare Einkünfte in anderen Kantonen (Code 394) bzw. im Ausland (Code 396)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Steuerausscheidung / Ausscheidungsberechnung (nur bei interkantonalem / internationalem Sachverhalt)
- **Regel:** Nur bei Einkünften in anderen Kantonen oder im Ausland (Liegenschaften, Betriebsstätten) ausfüllen; sonst leer lassen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «26.1 Auf steuerbare Einkünfte in anderen Kantonen 394»

<a id="27-berechnung-total"></a>
### Ziff. 27 – Steuerbares Einkommen im Kanton Zürich bzw. in der Schweiz (Code 398)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 25 – 26)
- **Regel:** Rechenzeile: massgebend für Staats- und Bundessteuertarif.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «27. Steuerbares Einkommen im Kanton Zürich bzw. in der Schweiz 398»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben (Code 400) – Total Steuerwert laut Wertschriftenverzeichnis

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Wertschriftenverzeichnis (Form. 340) Total Steuerwert (Code 400); Steuerauszug per 31.12.2025
- **Regel:** Steuerwert per 31.12.2025 (Schlusskurs letzter Handelstag Dezember, ESTV-Kursliste), Guthaben zum vollen Forderungsbetrag, Kryptowährungen zum ESTV-Jahresendkurs. PK-/Vorsorgeguthaben der 2. Säule und 3a sind steuerfrei und nicht aufzuführen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.1 Wertschriften und Guthaben Wertschriftenverzeichnis 400»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Total Steuerwert 400»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0156.md) `zh-wl-2025__c0156` – «Für den Steuerwert per Ende des Kalenderjahres ist der Schlusskurs des letzten Börsenhan-»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0159.md) `zh-wl-2025__c0159` – «Guthaben sind mit dem vollen Forderungsbetrag anzugeben.»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0154.md) `zh-wl-2025__c0154` – «sind bis zur Fälligkeit der Leistungen steuerfrei und nicht im Wertschriftenverzeichnis aufzuführen»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 404)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Eigene Aufstellung / Bestandsnachweis per 31.12.
- **Regel:** Bargeld und Edelmetalle zum Steuerwert; ausländische Banknoten, Goldmünzen und Edelmetalle zum Tageskurs.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.2 Bargeld, Gold und andere Edelmetalle»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0138.md) `zh-wl-2025__c0138` – «Ausländische Banknoten, Goldmünzen und Edelmetalle sind zum Tageskurs anzugeben.»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen, Steuerwert (Code 406)

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Steuerwertbescheinigung der Versicherungsgesellschaft per 31.12.2025 (Total)
- **Regel:** Nur rückkaufsfähige Lebens-/Rentenversicherungen: bescheinigter Steuerwert (Rückkaufswert) einsetzen; Bescheinigung beilegen. Policen der gebundenen Selbstvorsorge (3a) bis zur Fälligkeit steuerfrei.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.3 Lebens- und Rentenversicherungen (Steuerwert gem. Bescheinigung der Versicherungsges.)»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0139.md) `zh-wl-2025__c0139` – «Rückkaufsfähige Lebens- und Rentenversicherungen unterliegen der Vermögenssteuer. Aus-»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0139.md) `zh-wl-2025__c0139` – «bescheinigten Wert abzustellen.»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge (Code 412)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Kaufvertrag / Fahrzeugausweis (Kaufpreis, Kaufjahr)
- **Regel:** Aktueller Verkehrswert; in der Regel Wertverminderung 40 % des Restwertes pro Jahr. Geleaste Fahrzeuge nicht deklarieren.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.4 Motorfahrzeuge: Kaufpreis: Kaufjahr: 412»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0140.md) `zh-wl-2025__c0140` – «beträgt die Wertverminderung pro Jahr 40% des Restwertes. Nicht deklariert werden müssen»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Geschäfts- und Korporationsanteile (Code 414)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung (Beteiligungsquote, Steuerwert)
- **Regel:** Anteilmässig nach Beteiligungsquote; Anteile an unverteilten Erbschaften: Vermögen mit Steuerwert per 31.12. anteilmässig, Belege beilegen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.5 Geschäfts-/Korporationsanteile Aufstellung 414»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0140.md) `zh-wl-2025__c0140` – «Geschäfts- und Korporationsanteile sind von den Inhabern anteilmässig entsprechend ihrer»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0150.md) `zh-wl-2025__c0150` – «Das Vermögen aus unverteilten Erbschaften ist mit dem per 31.12. gültigen Steuerwert an-»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte (Code 416)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Eigene Aufstellung (Schätzwert / Versicherungswert)
- **Regel:** z. B. Gemälde, Sammlungen, Kunst- und Schmuckgegenstände, Boote, Flugzeuge; nähere Bezeichnung angeben. Hausrat ist steuerfrei.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.6 Übrige Vermögenswerte; nähere Bezeichnung: 416»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0140.md) `zh-wl-2025__c0140` – «Übrige Vermögenswerte sind zum Beispiel Gemälde- und andere Sammlungen, Kunst- und»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0140.md) `zh-wl-2025__c0140` – «Der Hausrat ist steuerfrei.»

<a id="31-1-vermoegen-liegenschaften"></a>
### Ziff. 31.1 – Liegenschaften zum Verkehrswert besteuert (Code 421) – Total Liegenschaftenverzeichnis

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftenverzeichnis (Form. 350) Seite 1: Total Steuerwert Verkehrswert (Code 3951) – Bewertung des Gemeindesteueramts
- **Regel:** Steuerwert Einfamilienhaus/Stockwerkeigentum gemäss zugestellter Bewertung des Gemeindesteueramts (Weisung ZStB 21.1); Mehrfamilien-/Geschäftshaus = Ertragswert (Bruttojahresertrag x 100 / 7,05). Nutzniessung/Wohnrecht: voller Wert beim Berechtigten bzw. Eigentümer.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «31.1 Zum Verkehrswert besteuert Liegenschaftenverzeichnis 421»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0196.md) `zh-wl-2025__c0196` – «tenbewertung wird Ihnen vom Gemeindesteueramt der Liegenschaftengemeinde zugestellt.»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0198.md) `zh-wl-2025__c0198` – «Vermögenssteuerwert = Bruttojahresertrag x 100 / 7,05»

<a id="31-2-vermoegen-liegenschaften"></a>
### Ziff. 31.2 – Liegenschaften zum Ertragswert besteuert – Land- oder Forstwirtschaft (Code 422)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Liegenschaftenverzeichnis (Form. 350) Seite 1: Total Ertragswert (Code 3952)
- **Regel:** Land- und forstwirtschaftliche Liegenschaften zum Ertragswert; Total aus dem Liegenschaftenverzeichnis übertragen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «31.2 Zum Ertragswert besteuert (Land- oder Forstwirtschaft) Liegenschaftenverzeichnis 422»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0200.md) `zh-wl-2025__c0200` – «Das Total der Vermögenssteuerwerte von land- und forstwirtschaftlichen Liegen-»

<a id="32-vermoegen-uebrige"></a>
### Ziff. 32 – Eigenkapital Selbständigerwerbender ohne Geschäftswertschriften (Code 430)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsblatt A (Eigenkapital Ziff. 10.4 bzw. 14.4)
- **Regel:** Eigenkapital laut Hilfsblatt A (kaufmännische Buchführung Ziff. 10.4, vereinfachte Ziff. 14.4) ohne Geschäftswertschriften (diese im WV mit Code G).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «32. Eigenkapital Selbständigerwerbender ohne Geschäftswertschriften Hilfsblatt A 430»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0141.md) `zh-wl-2025__c0141` – «Selbständigerwerbende mit kaufmännischer Buchführung übertragen das Eigenkapital laut»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 460)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 30–32)
- **Regel:** Rechenzeile.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «33. Total der Vermögenswerte 460»

<a id="34-schulden-privat"></a>
### Ziff. 34 – Schulden (Code 470)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung) → Schuldenverzeichnis (Form. 355) Total Privatschulden (Code 3200); Saldobestätigung Bank per 31.12.2025
- **Regel:** Alle Privatschulden inkl. Grundpfandschulden per 31.12.2025 mit Gläubiger (genaue Adresse), Betrag und Zinssatz im Schuldenverzeichnis aufführen und Total übertragen; Verzeichnis beilegen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «34. Schulden Schuldenverzeichnis 470»
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0002.md) `zh-form-355__c0002` – «Total Privatschulden / private Schuldzinsen 3200 / 3201»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0141.md) `zh-wl-2025__c0141` – «einzureichen. Unerlässlich ist insbesondere die Angabe des Gläubigers mit genauer Adresse»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Steuerbares Vermögen gesamt (Code 490)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 33 – 34)
- **Regel:** Rechenzeile.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «35. Steuerbares Vermögen gesamt 490»

<a id="36-1-36-2-berechnung-total"></a>
### Ziff. 36.1 / 36.2 – Davon auf steuerbare Vermögenswerte in anderen Kantonen (Code 494) bzw. im Ausland (Code 496)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Steuerausscheidung (nur bei interkantonalem / internationalem Sachverhalt)
- **Regel:** Nur bei Vermögen in anderen Kantonen oder im Ausland ausfüllen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «36.1 Auf steuerbare Vermögenswerte in anderen Kantonen 494»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen im Kanton Zürich (Code 498)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 35 – 36)
- **Regel:** Rechenzeile: massgebend für den Vermögenssteuertarif.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «37. Steuerbares Vermögen im Kanton Zürich 498»

<a id="tarif-vermoegen-sozialabzug"></a>
### Ziff. — (Tarif) – Steuerfreies Vermögen: kein Formularfeld, ergibt sich aus der 0‰-Stufe des Vermögenssteuertarifs

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → –
- **Regel:** Das Formular 300 enthält keine Zeile für einen Vermögens-Sozialabzug. Der steuerfreie Betrag ergibt sich aus der ersten Tarifstufe (0‰): Grundtarif Fr. 80 000, Verheiratetentarif Fr. 159 000. Es ist nichts einzutragen. Der Verheiratetentarif gilt auch für Alleinstehende, die mit Kindern im Sinn von § 34 Abs. 1 lit. a zusammenleben (§ 47 Abs. 2).
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 80'000 (Vermögenssteuer Grundtarif: 0 ‰ für die ersten CHF 80'000 steuerbares Vermögen (steuerfrei; kein separater Sozialabzug).)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 159'000 (Verheiratetentarif (auch Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern): 0 ‰ für die ersten CHF 159'000 steuerbares Vermögen.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Bund:** Bund: keine Vermögenssteuer.
- **Bemerkung:** Beträge aus § 47 StG (Fassung Nachtrag 127, Stand 1.1.2025); VKP 2024 (zh-vkp-2024-zstb) nennt dieselben Werte.
- **Quellen:**
  - [StG ZH § 47](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-47-t1.md) `zh-stg-2025__par-47-t1` – «0‰ für die ersten Fr. 80 000»
  - [StG ZH § 47](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-47-t2.md) `zh-stg-2025__par-47-t2` – «0‰ für die ersten Fr. 159 000»

## Weitere Angaben

<a id="40-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. 40 – Kapitalleistungen aus Vorsorge (Code 510)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Auszahlungsbescheinigung der Vorsorgeeinrichtung (Datum, Betrag, Art)
- **Regel:** Sämtliche 2025 ausgerichteten Kapitalleistungen aus AHV/IV, 2. Säule, Freizügigkeit, Säule 3a sowie Arbeitgeberleistungen mit Vorsorgecharakter und Kapitalzahlungen bei Tod/bleibenden Nachteilen angeben (bei mehreren Gesamtbetrag + Aufstellung). 100 % steuerbar, gesondert besteuert (Staat: Satz einer Jahresleistung von 1/20, mind. 2 %; Bund: 1/5 der Tarife). Steuerfrei: Stellenwechsel-Leistungen, die innert Jahresfrist in eine andere Vorsorgeeinrichtung eingekauft werden.
- **Bund:** Bund: Steuer zu einem Fünftel der Tarife (Art. 36 Abs. 1 und 2 DBG).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0013.md) `zh-form-300-2025__c0013` – «aus Einrichtung der beruflichen Vorsorge (2. Säule)»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0144.md) `zh-wl-2025__c0144` – «Kapitalleistungen aus Vorsorge sind zu 100% steuerbar.»
  - [WL ZH 2025 S. 22–23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0145.md) `zh-wl-2025__c0145` – «Die Steuer wird zu einem Fünftel der Tarife nach Artikel 36 Abs. 1 und 2 DBG berechnet.»

<a id="50-1-50-2-info-schenkungen-erbschaften"></a>
### Ziff. 50.1 / 50.2 – Schenkungen, Erbvorbezug, Erbschaften, Beteiligung an Erbengemeinschaften: erhalten (Code 516) / ausgerichtet (Code 519)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Schenkungsvertrag / Erbbescheinigung / Teilungsvertrag (Datum, Wert, Name, Verwandtschaftsgrad)
- **Regel:** Alle 2025 erhaltenen bzw. ausgerichteten Schenkungen, Erbvorbezüge und Vermögensanfälle von Todes wegen angeben (auch bei nicht erfolgter Erbteilung). Besondere Schenkungssteuererklärung nicht nötig bei Zuwendungen an Ehegatten/Partner, Nachkommen und Gelegenheitsgeschenken bis CHF 5’000.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0014.md) `zh-form-300-2025__c0014` – «2025 erhalten von Wert: 516»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0146.md) `zh-wl-2025__c0146` – «Hier sind alle Schenkungen, Erbvorbezüge und Vermögensanfälle von Todes wegen (auch»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0148.md) `zh-wl-2025__c0148` – «bei Gelegenheitsgeschenken, die den Wert von je CHF 5’000 nicht übersteigen.»

<a id="seite-1-personalien"></a>
### Ziff. Seite 1 – Personalien, Kinder (Jg. 2008–2025 / in Erstausbildung), unterstützte Personen, Pensionskassenbeiträge ja/nein

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Vorjahresveranlagung, Zivilstandsdaten, Schul-/Lehrbestätigungen
- **Regel:** Verhältnisse per 31.12.2025 (Zivilstand, Konfession, Kinder inkl. Ausbildung und ob der andere Elternteil Unterhalt leistet, unterstützte Personen mit Unterstützungsbetrag). Die Angabe «ordentliche Beiträge an die Pensionskasse ja/nein» bestimmt Maximalabzug Versicherungsprämien (Ziff. 15) und 3a-Berechtigung.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0002.md) `zh-form-300-2025__c0002` – «Personalien, Berufs- und Familienverhältnisse am 31. Dezember 2025»
  - [Formular 300 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0003.md) `zh-form-300-2025__c0003` – «Kinder der Jahrgänge 2008-2025 oder in beruflicher Erstausbildung stehende Kinder, deren Unterhalt Sie bestreiten:»

<a id="seite-1-4-verfahren-einreichung"></a>
### Ziff. Seite 1 / 4 – Einreichung, Frist, Unterschrift, Beilagen

- **Schlüssel:** `verfahren.einreichung` (Einreichung, Unterschrift, Beilagen, Fristen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerrechnung / Akontorechnung / Schlussrechnung (Staats-, Gemeinde- und Bundessteuer) → Aufforderung / Steuererklärung (Frist), Beilagen gemäss Checkliste
- **Regel:** Steuererklärung 2025 bis 31. März 2026 einreichen (Fristerstreckung vor Ablauf beim Gemeindesteueramt beantragen; Mahnfristen nicht erstreckbar). Belege zu den Aufstellungen/Formularen nur beilegen, wenn ausdrücklich verlangt (insb. Liegenschaftskosten und Spenden erst auf Verlangen). Unterschrift Person 1 und 2.
- **Quellen:**
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0017.md) `zh-wl-2025__c0017` – «Die Steuererklärung ist bis am 31. März 2026 einzureichen.»
  - [WL ZH 2025 S. 32](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0207.md) `zh-wl-2025__c0207` – «Die Belege zu den Aufstellungen und Formularen sind nur dann zusammen mit der»

## Hilfsblatt Berufskosten (Form. 360)

<a id="form-360-ziff-1-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1.1 – Abonnementkosten öffentliche Verkehrsmittel (Code 201 / Person 2: 221)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg → ÖV-Abo-Beleg (Jahreskosten, Wohn- und Arbeitsort); Lohnausweis Feld F
- **Regel:** Notwendige Abonnementskosten bei ständiger ÖV-Benützung. Zusammen mit Ziff. 1.2/1.3 Plafond CHF 5’200 (Staat) / CHF 3’300 (Bund). Kein Abzug bei Lohnausweis Feld F (unentgeltliche Beförderung).
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, bei der Staatssteuer höchstens CHF 5'200 pro Jahr (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Bund:** Bund: Plafond CHF 3’300.
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0001.md) `zh-form-360-2025__c0001` – «1.1 Abonnementkosten für öffentliche Verkehrsmittel 201»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0062.md) `zh-wl-2025__c0062` – «die notwendigen Abonnementskosten»

<a id="form-360-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1.2 – Fahrrad, Kleinmotorrad (gelbes Kontrollschild) pauschal CHF 700 (Code 202 / 222)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → –
- **Regel:** Pauschal CHF 700 pro Jahr bei ständiger Benützung eigenes Fahrrad/Kleinmotorrad mit gelbem Kontrollschild; kein Belegnachweis nötig.
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Ständige Benützung eines Fahrrads, Motorfahrrads oder Kleinmotorrads (gelbes Kontrollschild): Pauschale CHF 700 pro Jahr.)** · Bund **CHF 700 (Pauschale pro Jahr für Fahrrad, Motorfahrrad und Motorrad mit gelbem Kontrollschild; tatsächliche Kosten zusätzlich nicht abziehbar)**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0001.md) `zh-form-360-2025__c0001` – «1.2 Fahrrad, Kleinmotorrad (gelbes Kontrollschild) pauschal CHF 700»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0063.md) `zh-wl-2025__c0063` – «Kontrollschild im Jahr CHF 700»

<a id="form-360-ziff-1-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1.3 – Auto / Motorrad (weisses Kontrollschild), CHF –.70 bzw. –.40 pro km (Code 204 / 224; Zwischentotal 205 / 225)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Fahrzeugausweis, Arbeitsort, Arbeitstage, km pro Fahrt; Begründung Ziff. 7 (Code 2041–2044)
- **Regel:** Nur ausnahmsweise (kein ÖV-Anschluss ≥ 1 km, Zeitersparnis > 1 Std., ständige dienstliche Benützung gegen Entschädigung, Krankheit/Gebrechlichkeit mit Arztzeugnis): Auto 70 Rp./km, Motorrad weiss 40 Rp./km, in der Regel max. 240 Tage; sonst nur ÖV-Abo. Mittagsheimfahrt max. soviel wie Verpflegungsabzug (dafür entfällt dieser). Geschäftsfahrzeug: kein Fahrkostenabzug. Zwischentotal auf CHF 5’200 (Staat) / CHF 3’300 (Bund) begrenzt.
- **Limiten:**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.70 (Privatauto nur ausnahmsweise (kein öV, Zeitersparnis über 1 Std., Einsatz auf Verlangen des Arbeitgebers, Krankheit/Gebrechlichkeit): CHF 0.70 pro Fahrkilometer.)** · Bund **CHF 0.70 (Privatauto: Abzug pro Fahrkilometer CHF 0.70, nur wenn kein öffentliches Verkehrsmittel verfügbar/zumutbar (Steuerjahr 2025))**
  - Fahrkosten Motorrad – Ansatz pro km (CHF): Kanton **CHF 0.40 (Motorrad mit weissem Kontrollschild, nur in den gleichen Ausnahmefällen wie beim Auto: CHF 0.40 pro Fahrkilometer.)** · Bund **CHF 0.40 (Motorrad mit weissem Kontrollschild: CHF 0.40 pro Fahrkilometer (Steuerjahr 2025))**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **240 Tage (Kilometerabrechnung (Auto/Motorrad, weisses Kontrollschild) in der Regel auf 240 Arbeitstage begrenzt (gemäss Formular Berufsauslagen).)** · Bund **n/a – Bund kennt keine Festlegung massgebender Arbeitstage; abziehbar sind die tatsächlichen notwendigen Kosten bis zum Maximalbetrag (Art. 26 Abs. 1 lit. a DBG).**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, bei der Staatssteuer höchstens CHF 5'200 pro Jahr (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Bund:** Bund: Plafond CHF 3’300 (eigene Spalte, Zwischentotal Code 205).
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0002.md) `zh-form-360-2025__c0002` – «Auto: CHF -.70 pro km Motorrad: CHF -.40 pro km»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0064.md) `zh-wl-2025__c0064` – «für Auto 70 Rp. pro Fahrkilometer.»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «Bei der Staatssteuer ist der Fahrkostenabzug auf CHF 5’200 beschränkt.»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «Bei der direkten Bundessteuer ist der Fahrkostenabzug auf CHF 3’300 beschränkt.»
  - [StG ZH § 26](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-26.md) `zh-stg-2025__par-26` – «a. die notwendigen Kosten bis zu einem Höchstbetrag von Fr. 5200 für Fahrten zwischen Wohn- und Arbeitsstätte»

<a id="form-360-ziff-7-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 7 – Begründung für Benützung eines privaten Motorfahrzeugs (Code 2041–2044 / 2241–2244); Geschäftsfahrzeug

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Arbeitgeberbestätigung / Arztzeugnis; Lohnausweis Feld F bei Geschäftsfahrzeug
- **Regel:** Zutreffende Begründung ankreuzen (fehlender ÖV, > 1 Std. Zeitersparnis, ständige Benützung auf Verlangen und gegen Entschädigung des Arbeitgebers, Krankheit/Gebrechlichkeit mit Arztzeugnis). Wer ein Geschäftsfahrzeug hat, kann keine Fahrkosten abziehen.
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «Fehlen eines öffentlichen Verkehrsmittels (siehe Wegleitung) 2041»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «Arbeitnehmende, die über ein Geschäftsfahrzeug verfügen, können keine Fahrkosten in Abzug bringen.»

<a id="form-360-ziff-2-1-verbilligt-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 360 Ziff. 2.1 (verbilligt) – Mehrkosten Verpflegung bei verbilligter Verpflegung (Kantine, Lunch-Checks): CHF 7.50/Tag, max. CHF 1’600/Jahr (Code 206 / 226)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Feld G (Kantine/Lunch-Checks); Arbeitstage am Arbeitsort
- **Regel:** Wenn die Verpflegung vom Arbeitgeber verbilligt wird (Kantine, Personalrestaurant, Barbeitrag, Essensgutscheine) und trotzdem Mehrkosten entstehen: CHF 7.50 pro Arbeitstag, bei ständiger auswärtiger Verpflegung max. CHF 1’600 pro Jahr. Nur wenn die Heimkehr in der Mittagspause nicht möglich ist. Nicht kumulierbar mit 2.1 voll und 2.2 Schicht.
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Verpflegung durch Arbeitgeber verbilligt (Kantine, Personalrestaurant, Barbeitrag, Essensgutscheine) und trotzdem Mehrkosten: CHF 7.50 pro Arbeitstag.)** · Bund **CHF 7.50 (Halber Abzug CHF 7.50 pro Hauptmahlzeit, wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei ständiger auswärtiger Verpflegung mit Verbilligung: CHF 1'600 pro Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: CHF 1'600 pro Jahr)**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md) `zh-form-360-2025__c0003` – «wenn die Verpflegung durch den Arbeitgeber verbilligt wird und dem Arbeitnehmer trotzdem»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0066.md) `zh-wl-2025__c0066` – «– wenn die Verpflegung durch den Arbeitgeber verbilligt wird (Kantine, Personalrestaurant,»
  - [LS 631.33 (bis 2025) S. 2–3](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0004.md) `zh-pauschalierung-berufsauslagen-2025__c0004` – «Die vorstehenden Abzüge dürfen nicht kumuliert werden.»

<a id="form-360-ziff-2-1-voll-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 360 Ziff. 2.1 (voll) – Mehrkosten Verpflegung, Verpflegung voll zu Lasten Arbeitnehmer: CHF 15/Tag, max. CHF 3’200/Jahr (Code 208 / 228)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis (kein Feld G); Arbeitstage am Arbeitsort
- **Regel:** Wenn die Verpflegung in anderen Gaststätten voll zu Lasten des Arbeitnehmers geht: CHF 15 pro Arbeitstag, bei ständiger auswärtiger Verpflegung max. CHF 3’200 pro Jahr. Voraussetzung: Arbeitspause lässt Heimkehr nicht zu.
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswärtige Verpflegung, wenn voll zulasten der steuerpflichtigen Person: CHF 15 pro Arbeitstag (nicht kumulierbar mit Fahrkosten über Mittag).)** · Bund **CHF 15 (Mehrkosten auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (i.d.R. Mittagessen); ausschliesslich Pauschale, wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei ständiger auswärtiger Verpflegung (voll zulasten): CHF 3'200 pro Jahr.)** · Bund **CHF 3'200 (Bei ständiger auswärtiger Verpflegung CHF 3'200 pro Jahr (voller Abzug))**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md) `zh-form-360-2025__c0003` – «pro Arbeitstag CHF 15 / im Jahr CHF 3’200»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0066.md) `zh-wl-2025__c0066` – «pro Arbeitstag CHF 15, bei ständiger»

<a id="form-360-ziff-2-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 360 Ziff. 2.2 – Mehrkosten bei durchgehender, mind. achtstündiger Schicht- / Nachtarbeit: CHF 15/Schichttag, max. CHF 3’200/Jahr (Code 210 / 230)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 (Anzahl Schichttage); Dienstplan
- **Regel:** Pro ausgewiesenem Schichttag CHF 15, bei ständiger Schicht-/Nachtarbeit max. CHF 3’200 pro Jahr; gestaffelte Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause eingenommen werden können. Anzahl Tage eintragen. Nicht kumulierbar mit Ziff. 2.1.
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Durchgehende, mindestens achtstündige Schicht-/Nachtarbeit: CHF 15 pro ausgewiesenem Schichttag, bei ständiger Schicht-/Nachtarbeit CHF 3'200 pro Jahr. Gestaffelte (unregelmässige) Arbeitszeit gleichgestellt, wenn Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich.)** · Bund **CHF 15 (Durchgehende Schicht-/Nachtarbeit (gestaffelte Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich): CHF 15 pro ausgewiesenem Tag, bei ganzjähriger Schicht-/Nachtarbeit CHF 3'200 pro Jahr)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei ständiger auswärtiger Verpflegung (voll zulasten): CHF 3'200 pro Jahr.)** · Bund **CHF 3'200 (Bei ständiger auswärtiger Verpflegung CHF 3'200 pro Jahr (voller Abzug))**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md) `zh-form-360-2025__c0003` – «pro ausgewiesenem Schichttag CHF 15 / im Jahr CHF 3’200»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0066.md) `zh-wl-2025__c0066` – «gewiesenen Schichttag CHF 15, bei ständiger Schicht- oder Nachtarbeit im Jahr»

<a id="form-360-ziff-3-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 360 Ziff. 3 – Übrige Berufskosten: pauschal 3 % des Nettolohns, mind. CHF 2’000, max. CHF 4’000 (Code 212) bzw. effektiv (Code 213) (Person 2: 232 / 233)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn als Basis); bei effektiv: Aufstellung + Belege
- **Regel:** Berufskleider, Berufswerkzeuge (inkl. EDV), Fachliteratur, privates Arbeitszimmer, Berufsverbandsbeiträge. Pauschale 3 % des Nettolohns gemäss Lohnausweis (mind. CHF 2’000 / max. CHF 4’000); höhere effektive Kosten nur mit Aufstellung und vollem Nachweis (dann Pauschale entfällt).
- **Limiten:**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **3 % (Übrige Berufsauslagen (Berufskleider, Werkzeuge inkl. EDV, Fachliteratur, privates Arbeitszimmer, Berufsverbandsbeiträge): 3 % des Nettolohns, mind. CHF 2'000, höchstens CHF 4'000. Nachweis höherer Kosten möglich (volle Belegpflicht).)** · Bund **3 % (Übrige Berufskosten: 3 % des Nettolohns (Pauschale; Nachweis höherer Kosten möglich); bei Teilzeit/unterjährig angemessen kürzen)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **CHF 2'000 (Minimum der Pauschale für übrige Berufsauslagen: CHF 2'000.)** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 4'000 (Maximum der Pauschale für übrige Berufsauslagen: CHF 4'000.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
  - Arbeitszimmer/Homeoffice – Regel: Kanton **Keine separate Homeoffice-/Arbeitszimmer-Pauschale: Kosten eines privaten Arbeitszimmers sind in der Pauschale für übrige Berufsauslagen (3 % des Nettolohns, CHF 2'000–4'000) enthalten; höhere effektive Kosten nur bei vollem Nachweis.** · Bund **Privates Arbeitszimmer: nur als Teil der Pauschale 'übrige Berufskosten' bzw. bei Nachweis höherer Kosten abziehbar; Kosten (Miete, Heizung, Beleuchtung) nur, wenn das Zimmer für die Berufsarbeit benützt werden muss. Gelegentliche Arbeit in der Privatwohnung gibt keinen Abzug**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0004.md) `zh-form-360-2025__c0004` – «3% des Nettolohnes gem. Lohnausweis, mind. CHF 2’000, höchstens CHF 4’000»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0069.md) `zh-wl-2025__c0069` – «so sind diese Berufsauslagen in vollem Umfange nachzuweisen.»
  - [LS 631.33 (bis 2025) S. 3](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0005.md) `zh-pauschalierung-berufsauslagen-2025__c0005` – «Der Nettolohn entspricht dem Bruttolohn nach»

<a id="form-360-ziff-4-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 360 Ziff. 4 – Mehrkosten bei auswärtigem Wochenaufenthalt (Code 2860 / 2861)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag Zimmer am Arbeitsort; Aufstellung
- **Regel:** Zusätzlich: Mehrkosten Abendessen CHF 15 pro Arbeitstag bzw. max. CHF 3’200 im Jahr bei ganzjährigem Wochenaufenthalt, Zimmermiete, Kosten der wöchentlichen Heimkehr (i.d.R. nur ÖV-Abo, unter Ziff. 1 abziehen).
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Auswärtiger Wochenaufenthalt: Mehrkosten Unterkunft = Mietzins für ein Zimmer; Heimkehr in der Regel nur Kosten öffentlicher Verkehrsmittel (z. B. GA), unter Fahrkosten (Ziff. 1) abzuziehen; Abendessen CHF 15 pro Arbeitstag.** · Bund **Mehrkosten Unterkunft: ortsübliche Auslagen für ein Zimmer (nicht eine Wohnung) abziehbar; Fahrkosten der regelmässigen Heimkehr bis zum Maximalbetrag nach Art. 5 Abs. 1 BKV**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 3'200 (Mehrkosten Verpflegung (Abendessen) bei ganzjährigem Wochenaufenthalt: CHF 15 pro Arbeitstag, max. CHF 3'200 pro Jahr.)** · Bund **CHF 6'400 (Auswärtiger Wochenaufenthalt: Verpflegung CHF 30 pro Tag, max. CHF 6'400 pro Jahr; bei Verbilligung CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr; Nachweis höherer Kosten ausgeschlossen)**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0004.md) `zh-form-360-2025__c0004` – «Mehrkosten bei auswärtigem Wochenaufenthalt (gemäss Aufstellung, siehe Wegleitung) 2860»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0071.md) `zh-wl-2025__c0071` – «Arbeitstag oder bei ganzjährigem Wochenaufenthalt CHF 3’200 im Jahr abgezogen werden.»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0071.md) `zh-wl-2025__c0071` – «Als Mehrkosten für auswärtige Unterkunft kann der Mietzins für ein Zimmer abgezogen»

<a id="form-360-ziff-5-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 360 Ziff. 5 – Auslagen bei Nebenerwerb: pauschal 20 %, mind. CHF 800, max. CHF 2’400 (Code 216) bzw. effektiv (Code 217) (Person 2: 236 / 237)

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis des Nebenerwerbs; bei effektiv: Aufstellung
- **Regel:** Gilt für sämtliche Auslagen bei unselbständigem Nebenerwerb (inkl. Fahrkosten, Verpflegung): 20 % der Einkünfte aus allen Nebenbeschäftigungen, insgesamt mind. CHF 800 und max. CHF 2’400; höhere effektive Auslagen mit detaillierter Aufstellung und Nachweis.
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Auslagen bei Nebenbeschäftigung in unselbständiger Stellung (inkl. Fahrkosten, Verpflegung): 20 % der Einkünfte aus allen Nebenbeschäftigungen, mind. CHF 800, höchstens CHF 2'400.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge))**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Minimum Nebenerwerbspauschale: CHF 800.)** · Bund **CHF 800 (Minimum Pauschale Nebenerwerb)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Maximum Nebenerwerbspauschale: CHF 2'400.)** · Bund **CHF 2'400 (Maximum Pauschale Nebenerwerb)**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0004.md) `zh-form-360-2025__c0004` – «bzw. effektiv gemäss Aufstellung 217»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0072.md) `zh-wl-2025__c0072` – «20% der Einkünfte aus allen Nebenbeschäftigungen, insgesamt mindestens»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0072.md) `zh-wl-2025__c0072` – «jedoch CHF 800 und höchstens CHF 2’400.»

<a id="form-360-ziff-6-berechnung-total"></a>
### Ziff. Form. 360 Ziff. 6 – Total der Berufsauslagen (Code 220 / 240) → Steuererklärung Ziff. 11.1 / 11.2

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Formular 360
- **Regel:** Total übertragen nach Hauptformular Seite 3, Ziff. 11.1 (Person 1) bzw. 11.2 (Person 2).
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «6. Total der Berufsauslagen 220»

## Hilfsblatt Versicherungsprämien (Form. 365)

<a id="form-365-teil-a-ziff-1-4-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil A Ziff. 1–4 – Bezahlte Prämien: private Krankenversicherung (601), Unfall (602), Lebens-/Rentenversicherung (603), Zinsen von Sparkapitalien (604)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Jahresprämienrechnung/Prämienbescheinigung KK (Grundversicherung + Zusatz), Prämien Unfall (nicht NBUV via Lohnausweis), Lebens-/Rentenversicherung; Sparzinsen aus Steuerauszug/WV
- **Regel:** Tatsächlich im Jahr 2025 bezahlte Prämien für Kranken-, Unfall-, Lebens- und Rentenversicherung sowie Zinsen von Sparkapitalien (gemäss WV). Im Lohnausweis bereits abgezogene Prämien (NBUV) nicht nochmals.
- **Quellen:**
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md) `zh-form-365-2025__c0001` – «1. Private Krankenversicherungsprämien 601»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md) `zh-form-365-2025__c0001` – «4. Zinsen von Sparkapitalien 604»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0083.md) `zh-wl-2025__c0083` – «Tatsächlich bezahlte Einlagen, Prämien und Beiträge für private Kranken-, Unfall-, Lebens- und»

<a id="form-365-teil-a-ziff-6-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil A Ziff. 6 – Abzüglich erhaltene Prämienverbilligungen (Code 605); Total (A) (Code 606)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung) → Prämienrechnung/Bescheinigung Krankenversicherer (Verrechnung IPV), IPV-Verfügung
- **Regel:** Individuelle Prämienverbilligung wird meist mit den KK-Prämien verrechnet: dann die um die Verbilligung reduzierten Prämien in Ziffer 1 eintragen; sonst hier abziehen (kein Doppelabzug).
- **Quellen:**
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md) `zh-form-365-2025__c0001` – «6. Abzüglich erhaltene Prämienverbilligungen 605»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0084.md) `zh-wl-2025__c0084` – «Prämienverbilligungen der Krankenversicherer, die für den Steuerpflichtigen und die von»

<a id="form-365-teil-b-ziff-1-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil B Ziff. 1 – Maximalabzug Verheiratete: CHF 5’800 / 8’700 (Staat), CHF 3’700 / 5’550 (Bund) (Code 611)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Pensionskasse ja/nein, Säule 3a bezahlt)
- **Regel:** Verheiratete in ungetrennter Ehe: CHF 5’800 (Staat) / CHF 3’700 (Bund) mit Beiträgen an 2. Säule oder 3a; ohne solche Beiträge um die Hälfte erhöht (CHF 8’700 / CHF 5’550).
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'800 (Versicherungsprämien und Sparzinsen, in ungetrennter Ehe Lebende, MIT Beiträgen an 2. Säule/Säule 3a: max. CHF 5'800 (Staatssteuer).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 8'700 (Gemeinsam Besteuerte ohne Beiträge an 2. Säule und Säule 3a: Abzug erhöht sich um die Hälfte, max. CHF 8'700.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an Säule 2/3a (Erhöhung um die Hälfte))**
- **Bund:** Bund: CHF 3’700 / 5’550.
- **Quellen:**
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «die Beiträge an die 2. oder 3. Säule a geleistet haben 5’800 3’700»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «oder: sofern weder Beiträge an die 2. noch an die 3. Säule a geleistet wurden 8’700 5’550»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t2.md) `zh-stg-2025__par-31-t2` – «bis zum Gesamtbetrag von Fr. 5800 für in ungetrennter Ehe lebende Steuerpflichtige und von Fr. 2900 für die übrigen Steuerpflichtigen»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t2.md) `bund-dbg-2025__art-33-t2` – «3700 Franken für Ehepaare, die in rechtlich und tatsächlich ungetrennter Ehe leben,»

<a id="form-365-teil-b-ziff-2-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil B Ziff. 2 – Maximalabzug übrige Steuerpflichtige: CHF 2’900 / 4’350 (Staat), CHF 1’800 / 2’700 (Bund) (Code 612)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Pensionskasse ja/nein, Säule 3a bezahlt)
- **Regel:** Alle übrigen Steuerpflichtigen (nicht in ungetrennter Ehe): CHF 2’900 (Staat) / CHF 1’800 (Bund), ohne Beiträge an 2. Säule/3a um die Hälfte erhöht (CHF 4’350 / CHF 2’700).
- **Limiten:**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'900 (Übrige Steuerpflichtige MIT Beiträgen an 2. Säule/Säule 3a: max. CHF 2'900 (Staatssteuer).)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 4'350 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule/3a: max. CHF 4'350 (2'900 + die Hälfte).)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an Säule 2/3a)**
- **Bund:** Bund: CHF 1’800 / 2’700.
- **Quellen:**
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «die Beiträge an die 2. oder 3. Säule a geleistet haben 2’900 1’800»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «oder: sofern weder Beiträge an die 2. noch an die 3. Säule a geleistet wurden 4’350 2’700»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t2.md) `bund-dbg-2025__art-33-t2` – «1800 Franken für die übrigen Steuerpflichtigen;»

<a id="form-365-teil-b-ziff-3-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil B Ziff. 3 – Zusätzlicher Abzug je Kind / unterstützungsbedürftige Person: CHF 1’300 Staat, CHF 700 Bund (Code 613–615)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Kinder, unterstützte Personen mit Kinder-/Unterstützungsabzug)
- **Regel:** Für jedes Kind oder jede unterstützungsbedürftige Person mit Anspruch auf Kinder-/Unterstützungsabzug: CHF 1’300 (Staat) / CHF 700 (Bund); bei halbem Kinderabzug CHF 650 / CHF 350. Anzahl eintragen; Total (B) = Code 616.
- **Limiten:**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'300 (Zusätzlicher Versicherungsabzug von CHF 1'300 für jedes Kind oder jede unterstützungsbedürftige Person, für die ein Abzug nach § 34 Abs. 1 geltend gemacht werden kann (Bund: CHF 700).)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
- **Bund:** Bund: CHF 700 bzw. 350.
- **Quellen:**
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «Zusätzlicher Abzug für jedes Kind Anzahl: 1’300 700 613»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0091.md) `zh-wl-2025__c0091` – «CHF 650 für jedes Kind, für das der steuerpflichtigen Person ein halber Kinderabzug-»

<a id="form-365-teil-c-berechnung-total"></a>
### Ziff. Form. 365 Teil C – Abzug = niedrigerer Betrag von (A) und (B) (Code 270) → Steuererklärung Ziff. 15

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Formular 365
- **Regel:** Der niedrigere der Beträge (A) bezahlte Prämien / (B) Maximalabzug; Staat und Bund getrennt rechnen; Übertrag in Ziff. 15.
- **Quellen:**
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0003.md) `zh-form-365-2025__c0003` – «Der niedrigere Betrag: (A) oder (B) 270»

## Hilfsblatt Wertschriftenverzeichnis (Form. 340)

<a id="form-340-kolonne-a-einkommen-wertschriften"></a>
### Ziff. Form. 340 Kolonne A – Werte mit Verrechnungssteuerabzug – Bruttoertrag A (Code 2309-xx; Zwischentotal 539)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.) → Steuerauszug / Zinsausweis / Dividendenabrechnung (Bruttoertrag, 35 % VSt abgezogen)
- **Regel:** Konti, Kassenobligationen, inländische Aktien/Fonds/Obligationen mit Verrechnungssteuerabzug (auch Kundenguthaben mit Bruttozins über CHF 200). Bruttoertrag in Kolonne A; Steuerwert per 31.12. in Kolonne Steuerwert. Anspruch Verrechnungssteuer = 35 % von Total Bruttoertrag A (Code 540).
- **Quellen:**
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Zwischentotal Bruttoerträge 539 542»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0162.md) `zh-wl-2025__c0162` – «Die Zinsen und Dividenden schweizerischer Wertpapiere sind der schweizerischen Verrech-»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0162.md) `zh-wl-2025__c0162` – «nungssteuer unterworfen. Dies gilt auch für Kundenguthaben mit einem Bruttozins von mehr als»

<a id="form-340-kolonne-b-einkommen-wertschriften"></a>
### Ziff. Form. 340 Kolonne B – Werte ohne Verrechnungssteuerabzug – Bruttoertrag B (Code 542)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Steuerauszug / ausländische Abrechnungen / Zinsbescheinigungen
- **Regel:** Erträge ohne Verrechnungssteuerabzug: Kundenguthaben bis CHF 200 Zins, Darlehen, ausländische Wertschriften (Umrechnung zu Kursliste-Devisenkursen), Stockwerkeigentümer-Anteile, Vergütungszinsen, ausländische Spielbanken/Lotterien/Sportwetten. Total A + B = Code 150.
- **Quellen:**
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0168.md) `zh-wl-2025__c0168` – «Kundenguthaben, wenn der Zins nicht um die eidg. Verrechnungssteuer gekürzt wurde»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Total Bruttoertrag A + B 150»

<a id="form-340-totale-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 340 Totale – Total Steuerwert (Code 400) und Verrechnungssteueranspruch 35 % (Code 540)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Steuerauszug (Verrechnungssteuer-Betrag)
- **Regel:** Total Steuerwert → Ziff. 30.1 (Seite 4); Total Bruttoertrag A + B → Ziff. 4.1 (Seite 2). Die 35 % Verrechnungssteuer auf Kolonne A werden mit der Steuerrechnung verrechnet bzw. zurückerstattet (Bankverbindung angeben).
- **Quellen:**
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «35% von Total Bruttoertrag A 540»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Total Steuerwert 400»

<a id="form-340-da-1-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 340 DA-1 – Anrechnung ausländischer Quellensteuern / Übertrag ab Formular DA-1 (Code 2370/2371)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Formular DA-1 (Antrag Anrechnung ausländischer Quellensteuern) + Dividendenabrechnung
- **Regel:** Ausländische Dividenden/Zinsen mit Quellensteuer-Anrechnung im DA-1 aufführen; Totalbeträge in die Zeile «Übertrag ab Formular DA-1» (Bruttoertrag unter Kolonne B). Keine Anrechnung, wenn die nicht rückforderbaren ausländischen Steuern insgesamt CHF 100 nicht übersteigen.
- **Quellen:**
  - [WL ZH 2025 S. 27](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0171.md) `zh-wl-2025__c0171` – «ren. Die Totalbeträge des DA-1 übertragen Sie in die Zeile «Übertrag ab Formular DA-1» im»
  - [WL ZH 2025 S. 27](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0171.md) `zh-wl-2025__c0171` – «insgesamt den Betrag von CHF 100 nicht übersteigen, wird keine Anrechnung ausländischer»

<a id="form-340-code-q-g-n-e-s-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. Form. 340 Code Q/G/N/E/S – Kennzeichnung: G Geschäftsvermögen, N Nutzniessung, E Erbschaft, S Schenkung, Q qualifizierte Beteiligung ≥ 10 %

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Steuerauszug / Erb- und Schenkungsunterlagen
- **Regel:** Besondere Vermögenswerte mit Code kennzeichnen (Q → Ziff. 4.2 und Teilbesteuerungsabzug Ziff. 16.5; E/S → Ziff. 50). Vermögen/Ertrag Kinder Jg. 2008 und jünger sind im Verzeichnis der Eltern, Jg. 2007 und älter selbst zu deklarieren.
- **Quellen:**
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0155.md) `zh-wl-2025__c0155` – «mit Q Beteiligungen von mindestens 10 Prozent am Aktien-, Grund- oder Stammkapital an»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0154.md) `zh-wl-2025__c0154` – «minderjährigen Kinder des Jahrgangs 2008 und jüngeren sowie das Vermögen, an dem Sie»

## Hilfsblatt Schulden (Form. 355)

<a id="form-355-spalte-schuld-schulden-privat"></a>
### Ziff. Form. 355 Spalte Schuld – Privatschulden inkl. Grundpfandschulden am 31. Dezember – Total (Code 3200) → Ziff. 34

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung) → Bankbestätigung/Hypothekarbestätigung per 31.12.2025 (Gläubiger, Saldo, Zinssatz)
- **Regel:** Pro Gläubiger Name/Adresse, Schuldbetrag per 31.12. in CHF ohne Rappen eintragen; Total nach Seite 4, Ziff. 34.
- **Quellen:**
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0001.md) `zh-form-355__c0001` – «Privatschulden inkl. Grundpfandschulden Schuld am 31. Dezember Schuldzinsen»
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0002.md) `zh-form-355__c0002` – «Total Privatschulden / private Schuldzinsen 3200 / 3201»

<a id="form-355-spalte-schuldzinsen-abzug-schuldzinsen"></a>
### Ziff. Form. 355 Spalte Schuldzinsen – Schuldzinsen des Jahres – Total (Code 3201) → Ziff. 12

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen) → Zinsabrechnung der Bank für 2025
- **Regel:** Bezahlte Schuldzinsen 2025 pro Gläubiger; Total nach Seite 3, Ziff. 12 (Begrenzung Vermögensertrag + CHF 50’000 beachten, Baurechtszinsen separat im Liegenschaftenverzeichnis).
- **Quellen:**
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0002.md) `zh-form-355__c0002` – «Total Privatschulden / private Schuldzinsen 3200 / 3201»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0074.md) `zh-wl-2025__c0074` – «mögen (inkl. Eigenmietwert) und weiterer CHF 50’000 nicht übersteigen.»

## Hilfsblatt Liegenschaften (Form. 350)

<a id="form-350-seite-1-vermoegen-liegenschaften"></a>
### Ziff. Form. 350 Seite 1 – Steuerwert: Verkehrswert (Codes 5541–55410; Total 3951 → Ziff. 31.1) / Ertragswert Land- und Forstwirtschaft (Codes 5531–55310; Total 3952 → Ziff. 31.2)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftsbewertung des Gemeindesteueramts / Steuerwert-Mitteilung
- **Regel:** Pro Liegenschaft Ort, Art, Fläche und Steuerwert eintragen. EFH/StWE zu Wohnzwecken: Wert gemäss Bewertung des Gemeindesteueramts (ZStB 21.1); MFH/Geschäftshäuser: Ertragswert = Bruttojahresertrag 2025 x 100 / 7,05; Anteile an unverteilten Erbschaften anteilmässig.
- **Quellen:**
  - [Formular 350 ZH S. 1](../../chunks/zh/2025/zh-form-350/zh-form-350__c0002.md) `zh-form-350__c0002` – «Total 3952 13213211 3951 113213211»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0197.md) `zh-wl-2025__c0197` – «folgt: Vermögenssteuerwert = Ertragswert.»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0198.md) `zh-wl-2025__c0198` – «Vermögenssteuerwert = Bruttojahresertrag x 100 / 7,05»

<a id="form-350-seite-2-spalte-eigenmietwert-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 350 Seite 2 Spalte Eigenmietwert – Eigenmietwert / Miet- und Pachtzinseinnahmen (Codes 5701–57010 Wohnungen/Zimmer/Garagen; 5711–57110 gewerblich; Total 5721–57210)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Mieterspiegel / Ertragsaufstellung; Eigenmietwert-Verfügung des Gemeindesteueramts
- **Regel:** Eigenmietwert selbstgenutzter Räume (EFH 3,50 % bzw. StWE 4,25 % des Land- und Zeitbauwerts gemäss Weisung; selbstbewohnte Wohnung im eigenen MFH/Geschäftshaus 70 % des erzielbaren Mietzinses) plus sämtliche Miet-/Pachtzinseinnahmen (Garagen, Abstellplätze, Reklame) ohne Heizungs-/Warmwasser-/Treppenhaus-Entschädigungen bis zu den tatsächlichen Aufwendungen. Mieterspiegel je vermietete Liegenschaft beilegen. Wohnrecht/Nutzniessung: 100 % beim Berechtigten.
- **Bemerkung:** Eigenmietwert-Berechnungssätze EFH/StWE hier aus WL 2025; die Weisung 2009 (zh-weisung-liegenschaften-2009, ZStB 21.1) ist die massgebende Grundlage – bei Zweifel dort prüfen.
- **Quellen:**
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0006.md) `zh-form-350__c0006` – «Als Eigenmietwert der selbst genutzten Wohnung im Mehrfamilien- und Geschäftshaus (ohne Stockwerkeigentum) sind 70% des Mietzinses einzusetzen»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0176.md) `zh-wl-2025__c0176` – «Geschäftshaus (ohne Stockwerkeigentum) sind 70% des Mietzinses einzusetzen, der bei»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0178.md) `zh-wl-2025__c0178` – «Für Einfamilienhäuser: 3,50% des Land- und Zeitbauwertes»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0179.md) `zh-wl-2025__c0179` – «Für Stockwerkeigentum: 4,25% des Land- und Zeitbauwertanteils»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0183.md) `zh-wl-2025__c0183` – «Besteht ein Wohnrecht oder eine Nutzniessung, ist der Eigenmietwert zu 100% durch die»

<a id="form-350-seite-2-spalte-unterhalts-und-verwaltungskosten-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 350 Seite 2 Spalte Unterhalts- und Verwaltungskosten – Unterhalts- und Verwaltungskosten: pauschal (Codes 5731–57310) oder effektiv (Codes 5741–57410)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Unterhaltsrechnungen, Versicherungsprämien Gebäude, Verwaltungsabrechnung (bei effektiv: detaillierte Aufstellung)
- **Regel:** Wahl pro Liegenschaft und Steuerperiode: Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Mietwerts (abzüglich Heizungs-/Warmwasser-Entschädigungen) – dann keine weiteren Abzüge ausser Baurechtszinsen – oder tatsächliche Kosten mit Aufstellung (Datum, Art, Empfänger, Betrag). Pauschale nicht bei vorwiegend geschäftlich genutzten Liegenschaften. Resultat: Verbleibender Ertrag (Code 5751–57510), Total Nettoertrag Code 3953 → Ziff. 6.
- **Bemerkung:** Pauschale 20 % gilt in ZH unabhängig vom Gebäudealter (keine Staffelung nach Gebäudealter, keine Werte-Schlüssel liegenschaft.pauschale_neu/alt belegt).
- **Quellen:**
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0007.md) `zh-form-350__c0007` – «Die Abzüge für die Unterhalts- und Verwaltungskosten können für jede Liegenschaft entweder auf Grund einer Pauschale»
  - [ZStB 30.2](../../chunks/zh/dauernd/zh-zstb-30-2/zh-zstb-30-2__c0002.md) `zh-zstb-30-2__c0002` – «Dieser Pauschalabzug beträgt 20 % vom Brutto-Mietertrag bzw. -Mietwert.»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0184.md) `zh-wl-2025__c0184` – «pflichtigen können für jede Liegenschaft zwischen dem Abzug der tatsächlichen Kosten und»
  - [StG ZH § 30](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-30-t2.md) `zh-stg-2025__par-30-t2` – «Der Steuerpflichtige kann für Liegenschaften des Privatvermögens anstelle der tatsächlichen Kosten und Prämien einen Pauschalabzug geltend machen.»

<a id="form-350-ziff-16-unterhalt-abzug-liegenschaft-energie-umwelt"></a>
### Ziff. Form. 350 / Ziff. 16 Unterhalt – Investitionen Energiesparen / Umweltschutz, Rückbaukosten Ersatzneubau, Denkmalpflege, Baurechtszinsen

- **Schlüssel:** `abzug.liegenschaft.energie_umwelt` (Investitionen Energiesparen/Umweltschutz, Rückbaukosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Rechnungen, Subventionsbescheide (Abzug nur nicht subventionierter Teil)
- **Regel:** Den Unterhaltskosten gleichgestellt: Investitionen für Energiesparen/Umweltschutz und Rückbaukosten im Hinblick auf den Ersatzneubau, soweit nicht subventioniert und bei der direkten Bundessteuer abzugsfähig; nicht berücksichtigter Teil in den zwei folgenden Steuerperioden abziehbar. Denkmalpflegerische Arbeiten und Baurechtszinsen abziehbar. Bei Pauschale nicht zusätzlich (ausser Baurechtszinsen).
- **Bund:** Bund: Art. 32 Abs. 2 DBG (Energiespar-/Umweltschutzinvestitionen, Rückbaukosten) – Abzug auch bei Staatssteuer nur soweit bei Bund abzugsfähig.
- **Quellen:**
  - [StG ZH § 30](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-30-t1.md) `zh-stg-2025__par-30-t1` – «Den Unterhaltskosten sind Investitionen, die dem Energiesparen und dem Umweltschutz dienen, und die Rückbaukosten im Hinblick auf den Ersatzneubau gleichgestellt»
  - [StG ZH § 30](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-30-t1.md) `zh-stg-2025__par-30-t1` – «sind in den zwei nachfolgenden Steuerperioden abziehbar»
  - [StG ZH § 30](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-30-t2.md) `zh-stg-2025__par-30-t2` – «Die den Erträgen aus Liegenschaften gegenüberstehenden Baurechtszinsen können abgezogen werden.»

<a id="form-350-wl-eigenmietwert-sozialabzug-eigenmietwert"></a>
### Ziff. Form. 350 / WL Eigenmietwert – Einschlag auf dem Eigenmietwert bei tatsächlicher Unternutzung (Unternutzungsabzug)

- **Schlüssel:** `sozialabzug.eigenmietwert` (Einschlag/Abzug auf dem Eigenmietwert (kantonal)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Antrag an Gemeindesteueramt; ZStB 21.2
- **Regel:** Nur in Ausnahmefällen bei Verminderung des Wohnbedürfnisses (z. B. Wegzug der Kinder); bei vier bis sechs Zimmern liegt keine Unternutzung vor, wenn zwei oder mehr Personen darin wohnen. Wird von der Behörde beim Eigenmietwert berücksichtigt (keine eigene Zeile im Formular).
- **Quellen:**
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0183.md) `zh-wl-2025__c0183` – «Auf den errechneten Eigenmietwerten kann in Ausnahmefällen ein Einschlag gewährt werden,»

## Hilfsblatt Krankheitskosten (Form. 370)

<a id="form-370-s-1-teil-a-ziff-1-abzug-krankheitskosten"></a>
### Ziff. Form. 370 S.1 Teil A Ziff. 1 – Selbstbehalt gemäss Abrechnung Krankenkasse und Versicherung (Code 300)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Leistungsabrechnung/Jahresübersicht Krankenkasse (Franchise + Selbstbehalt)
- **Regel:** Franchise und Selbstbehalt gemäss Krankenkassenabrechnung; Prämien selbst sind NICHT Krankheitskosten (siehe Ziff. 15).
- **Quellen:**
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «1. Selbstbehalt gemäss Abrechnung Krankenkasse und Versicherung 300»

<a id="form-370-s-1-teil-a-ziff-2-3-abzug-krankheitskosten"></a>
### Ziff. Form. 370 S.1 Teil A Ziff. 2–3 – Arzt und verordnete Medikamente (Code 301), Zahnarztkosten (Code 302)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Arzt-/Zahnarztrechnungen, Apothekenbelege (nur nicht von KK/Versicherung vergütete Beträge)
- **Regel:** Nur die vom Steuerpflichtigen selbst getragenen Kosten; bereits unter Ziffer 1 erfasste Beträge nicht nochmals. Nicht abzugsfähig: Präventivmassnahmen, Fahrkosten zum Arzt, nicht verordnete Akupunktur, eigene Pflegeleistungen, Schlankheitskuren, Wellness, Schönheitsbehandlungen, Psychoanalysen.
- **Quellen:**
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «2. Arzt und vom Arzt verordnete Medikamente 301»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «3. Zahnarztkosten 302»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «Nicht abzugsfähig sind A. Aufwendungen Auslagen für: – Präventivmassnahmen»

<a id="form-370-s-1-teil-a-ziff-4-7-abzug-krankheitskosten"></a>
### Ziff. Form. 370 S.1 Teil A Ziff. 4–7 – Pflegepersonal (Code 303), Spital/Heilstätten (Code 304), verordnete Therapien/Kuraufenthalte (Code 305), Übrige (Code 307); Total (A) Code 317

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Rechnungen Spital, Spitex, Therapie, Kuraufenthalt (ärztlich verordnet)
- **Regel:** Entgeltliche Leistungen Dritter (nicht Pflege durch Angehörige), Spitalaufenthalte, ärztlich verordnete Therapien und Kuren; Belege geordnet beilegen.
- **Quellen:**
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «4. Pflegepersonal (entgeltliche Leistungen von Drittpersonen) 303»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «5. Kosten für Aufenthalt in Spitälern und Heilstätten usw. 304»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «6. Ärztlich verordnete Therapien, Kuraufenthalte usw. 305»

<a id="form-370-s-1-teil-b-abzug-krankheitskosten"></a>
### Ziff. Form. 370 S.1 Teil B – Vergütungen Dritter und Anteil Lebenshaltungskosten: Krankenkasse/Versicherungen (Code 308), Lebenshaltungskosten (Code 311), Übrige (Code 312); Total (B) Code 318

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Vergütungsabrechnungen Krankenkasse/Zusatzversicherung/Unfallversicherung
- **Regel:** Abzuziehen sind Leistungen der Kranken-/Unfallversicherung und Dritter sowie der Anteil Lebenshaltungskosten bei Heim-/Spitalaufenthalt (z. B. Ernährung), soweit nicht bereits unter A abgezogen.
- **Quellen:**
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «1. Krankenkasse / Versicherungen 308»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «2. Anteil Lebenshaltungskosten (z. B. Ernährung) 311»

<a id="form-370-s-1-teil-c-d-abzug-krankheitskosten"></a>
### Ziff. Form. 370 S.1 Teil C/D – Auslagen netto (C, Code 314) bzw. Pauschale Diät CHF 2500 (D, Code 315)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Ärztliche Bestätigung dauernde lebensnotwendige Diät (z. B. Zöliakie)
- **Regel:** Auslagen netto = Total Aufwendungen (A) – Vergütungen Dritter (B). Bei ärztlich angeordneter Diät/Spezialnahrung Mehrkosten abziehbar; anstelle der tatsächlichen Kosten bei andauernder lebensnotwendiger Diät Pauschale CHF 2500.
- **Quellen:**
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «Total der Auslagen (C) 314»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «CHF 2500 geltend gemacht wer-»

<a id="form-370-s-1-teil-e-abzug-krankheitskosten"></a>
### Ziff. Form. 370 S.1 Teil E – Berechnung: Total Auslagen (313) abzüglich Selbstbehalt 5 % des Nettoeinkommens (319) = Abzug (320) → Ziff. 22.1

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Formular 370 (Staats- und Bundessteuer getrennt)
- **Regel:** Selbstbehalt 5 % von Ziffer 21 der Steuererklärung (Nettoeinkommen) getrennt für Staats- und Bundessteuer abziehen; Resultat nach Seite 3, Ziff. 22.1.
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen nach §§ 26–31 verminderten steuerbaren Einkünfte (Nettoeinkommen, Ziff. 21) übersteigen. Behinderungsbedingte Kosten ohne Selbstbehalt (§ 31 lit. i).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Quellen:**
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «abzüglich Selbstbehalt (5% von Ziffer 21 der»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «Abzug 320»

<a id="form-370-s-2-teil-a-b-abzug-behinderungskosten"></a>
### Ziff. Form. 370 S.2 Teil A/B – Behinderungsbedingte Kosten: effektive Aufwendungen (Codes 3100–3120) und Vergütungen Dritter (Codes 3130–3150)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → IV-/Hilflosenentschädigungs-Bescheide, Rechnungen Heim-/Entlastungsaufenthalt, Hilfsmittel
- **Regel:** Effektive Kosten bei Empfängern von IV-Leistungen etc. (3100) und bei Heim-/Entlastungsaufenthalten (3101); abzuziehen: Krankenkasse/Versicherungen (3130), Hilflosenentschädigungen (3131), Anteil Lebenshaltungskosten (3132). Pro Steuererklärung nur eine Aufstellung.
- **Quellen:**
  - [Formular 370 ZH S. 2](../../chunks/zh/2025/zh-form-370/zh-form-370__c0005.md) `zh-form-370__c0005` – «1. behinderungsbedingte Kosten bei Empfängern von IV-Leistungen etc. 3100»
  - [Formular 370 ZH S. 2](../../chunks/zh/2025/zh-form-370/zh-form-370__c0005.md) `zh-form-370__c0005` – «2. Hilflosenentschädigungen 3131»

<a id="form-370-s-2-teil-c-d-abzug-behinderungskosten"></a>
### Ziff. Form. 370 S.2 Teil C/D – Total abzugsberechtigte Kosten (Code 3155) bzw. Pauschale (Code 3103) → Ziff. 16.4

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Formular 370 Seite 2
- **Regel:** Entweder Total der abzugsberechtigten Kosten (A – B) oder Pauschale (Art angeben; Pauschalen siehe Merkblatt des kantonalen Steueramtes zu Krankheits-, Unfall- und behinderungsbedingten Kosten, Ziff. 3, ZStB 32.1); Übertrag nach Seite 3, Ziff. 16.4.
- **Quellen:**
  - [Formular 370 ZH S. 2](../../chunks/zh/2025/zh-form-370/zh-form-370__c0006.md) `zh-form-370__c0006` – «Total der abzugsberechtigten Kosten 3155»

## Hilfsblatt Weiterbildung (Form. 367)

<a id="form-367-abzug-weiterbildung"></a>
### Ziff. Form. 367 – Total der Kosten (Code 2900/2903), Beitrag Arbeitgeber/Dritte (2901/2904), Selbstgetragene Kosten (2902/2905), Zulässiger Abzug (2920/2921 → Code 292)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Kursrechnungen, Zahlungsnachweise; Lohnausweis Ziff. 13.3 (Arbeitgeberbeitrag an den Arbeitnehmer)
- **Regel:** Je Person: Total Kosten – Beiträge Arbeitgeber/Bund/Branchenverbände = selbstgetragene Kosten; zulässiger Abzug max. CHF 12’400 (Staatssteuer) bzw. CHF 13’000 (Bundessteuer) → Ziff. 16.2. Im Lohnausweis Ziff. 13.3 ausgewiesene Arbeitgeberbeiträge sind als Beitrag Dritter anzugeben.
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 12'400 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung, selbst getragene Kosten: max. CHF 12'400 (Staatssteuer), sofern Abschluss Sek. II vorliegt oder 20. Lebensjahr vollendet (und nicht Ausbildung bis zum ersten Sek.-II-Abschluss).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Bund:** Bund: max. CHF 13’000.
- **Quellen:**
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Beitrag Arbeitgeber oder weiterer Stellen (Bund, Branchenverbände etc.)»
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Zulässiger Abzug (max. je CHF 12’400)»
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Zulässiger Abzug (max. je CHF 13’000)»

## Lohnausweis-Regeln

<a id="lohnausweis-feld-f-abzug-berufskosten-fahrkosten"></a>
### Ziff. Lohnausweis Feld F – Unentgeltliche Beförderung zwischen Wohn- und Arbeitsort → kein Fahrkostenabzug (Form. 360 Ziff. 1)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld F (Kreuz) / Ziff. 2.2 Privatanteil Geschäftsfahrzeug
- **Regel:** Ist Feld F angekreuzt (Geschäftsfahrzeug, Sammeltransport, Autokilometervergütung an Aussendienst, Autopauschale, geschäftlich notwendiges GA), entstehen dem Arbeitnehmer keine Arbeitswegkosten: kein Fahrkostenabzug in Form. 360 Ziff. 1. Wer ein Geschäftsfahrzeug hat, kann keine Fahrkosten abziehen. Ein GA ohne geschäftliche Notwendigkeit ist zum Marktwert in Lohnausweis Ziff. 2.3 zu deklarieren; Feld F ist dann nicht anzukreuzen.
- **Bemerkung:** Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen.
- **Quellen:**
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «das zur Verfügung stellen eines Geschäftsfahrzeugs durch den Arbeitgeber»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «Arbeitnehmende, die über ein Geschäftsfahrzeug verfügen, können keine Fahrkosten in Abzug bringen.»
  - [LS 631.33 (bis 2025) S. 2](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0003.md) `zh-pauschalierung-berufsauslagen-2025__c0003` – «zwischen Wohn- und Arbeitsstätte geltend gemacht werden.»

<a id="lohnausweis-feld-g-abzug-berufskosten-verpflegung"></a>
### Ziff. Lohnausweis Feld G – Kantinenverpflegung / Lunch-Checks → reduzierter Verpflegungsabzug (Form. 360 Ziff. 2.1 verbilligt, Code 206)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (Kreuz) / Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt»
- **Regel:** Feld G angekreuzt (Lunch-Checks, verbilligtes Personalrestaurant, auch wenn Nutzung unbekannt) → nur der reduzierte Verpflegungsabzug CHF 7.50/Tag (max. CHF 1’600/Jahr), nicht CHF 15/3’200. Bei > 60 % auswärtiger Tätigkeit mit Mittagessensentschädigung ist im Lohnausweis ausschliesslich unter Ziff. 15 der Hinweis «Mittagessen durch Arbeitgeber bezahlt» anzubringen (WL Lohnausweis 2026); die Folge für den Verpflegungsabzug ist in den vorliegenden Quellen nicht ausdrücklich belegt – nicht belegt, Fachperson prüfen.
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Verpflegung durch Arbeitgeber verbilligt (Kantine, Personalrestaurant, Barbeitrag, Essensgutscheine) und trotzdem Mehrkosten: CHF 7.50 pro Arbeitstag.)** · Bund **CHF 7.50 (Halber Abzug CHF 7.50 pro Hauptmahlzeit, wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei ständiger auswärtiger Verpflegung mit Verbilligung: CHF 1'600 pro Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: CHF 1'600 pro Jahr)**
- **Bemerkung:** Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen.
- **Quellen:**
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer Lunch-Checks (vgl. Rz 18) abgege»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – ««Mittagessen durch Arbeitgeber bezahlt»»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0066.md) `zh-wl-2025__c0066` – «– wenn die Verpflegung durch den Arbeitgeber verbilligt wird (Kantine, Personalrestaurant,»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Bei Arbeitnehmern, die mehr als 60 % der Arbeitszeit ausserhalb ihrer üblichen»

<a id="lohnausweis-ziff-10-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. Lohnausweis Ziff. 10.2 – Beiträge für den Einkauf in die berufliche Vorsorge – bereits vom Lohn abgezogen → nicht nochmals unter Ziff. 16.1 abziehen

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Lohnausweis Ziff. 10.2 (Einkauf, im Nettolohn Ziff. 11 bereits berücksichtigt); separat bezahlte Einkäufe: Formular 21 EDP der Vorsorgeeinrichtung
- **Regel:** Ziff. 10.2 ist vom Bruttolohn schon abgezogen (Nettolohn = Brutto – Ziff. 9 und 10); NICHT zusätzlich in Ziff. 16.1 abziehen. Nur vom Arbeitnehmer selbst bezahlte (nicht vom Lohn abgezogene) Einkäufe werden von der Vorsorgeeinrichtung mit Formular 21 EDP bescheinigt und in Ziff. 16.1 deklariert. Sperrfrist 3 Jahre bei Kapitalbezug beachten.
- **Bemerkung:** Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen.
- **Quellen:**
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «In diesem Feld sind die im Bruttolohn enthaltenen, dem Arbeitnehmer vom Lohn abgezoge»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «Vom Arbeitnehmer selber entrichtete, d. h. nicht vom Lohn abgezogene Einkaufsbeiträge an»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «vom Bruttolohn total (Ziffer 8) das Total der Abzüge (Ziffer 9 und 10) abgezogen wird.»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0092.md) `zh-wl-2025__c0092` – «werden, soweit innerhalb von drei Jahren ein Kapitalbezug erfolgt.»

<a id="lohnausweis-ziff-13-3-abzug-weiterbildung"></a>
### Ziff. Lohnausweis Ziff. 13.3 – Beiträge des Arbeitgebers an berufsorientierte Aus- und Weiterbildung → Form. 367 «Beitrag Arbeitgeber»

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Lohnausweis Ziff. 13.3 (Vergütungen an den Arbeitnehmer; direkt an Bildungsinstitut bezahlte Beträge werden nicht bescheinigt)
- **Regel:** Ziff. 13.3 als «Beitrag Arbeitgeber oder weiterer Stellen» im Form. 367 von den Gesamtkosten abziehen; nur die selbst getragenen Kosten sind abziehbar. Direkt an Dritte (Bildungsinstitut) bezahlte Arbeitgeberbeiträge stehen nicht im Lohnausweis – beim Arbeitgeber nachfragen und ebenfalls abziehen.
- **Bemerkung:** Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen.
- **Quellen:**
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «In diesem Feld sind alle effektiven Vergütungen des Arbeitgebers für berufsorientierte Aus-»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «Nicht anzugeben sind Vergütungen, die direkt an»
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Beitrag Arbeitgeber oder weiterer Stellen (Bund, Branchenverbände etc.)»

<a id="lohnausweis-ziff-15-abzug-berufskosten-verpflegung"></a>
### Ziff. Lohnausweis Ziff. 15 – Bemerkungen: Anzahl Schichttage u. a. → Grundlage für Schichtarbeitsabzug (Form. 360 Ziff. 2.2, Code 210)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 «Bemerkungen» (Anzahl im Kalenderjahr geleisteter Schichttage)
- **Regel:** Der Arbeitgeber kann die Anzahl geleisteter Schichttage in Ziff. 15 (Bemerkungen) bescheinigen (freiwillige Angabe); Schichtarbeitsabzug CHF 15 pro ausgewiesenem Schichttag (max. CHF 3’200/Jahr), mind. achtstündige durchgehende Schicht-/Nachtarbeit. Ziff. 15 kann zudem freiwillig die Höhe der im Bruttolohn enthaltenen Kinderzulagen und Krankenkassenbeiträge nennen.
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Durchgehende, mindestens achtstündige Schicht-/Nachtarbeit: CHF 15 pro ausgewiesenem Schichttag, bei ständiger Schicht-/Nachtarbeit CHF 3'200 pro Jahr. Gestaffelte (unregelmässige) Arbeitszeit gleichgestellt, wenn Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich.)** · Bund **CHF 15 (Durchgehende Schicht-/Nachtarbeit (gestaffelte Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich): CHF 15 pro ausgewiesenem Tag, bei ganzjähriger Schicht-/Nachtarbeit CHF 3'200 pro Jahr)**
- **Bemerkung:** Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen.
- **Quellen:**
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «nen Kinderzulagen, die Anzahl im Kalenderjahr geleisteter Schichttage und die Höhe der im»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0066.md) `zh-wl-2025__c0066` – «gewiesenen Schichttag CHF 15, bei ständiger Schicht- oder Nachtarbeit im Jahr»
