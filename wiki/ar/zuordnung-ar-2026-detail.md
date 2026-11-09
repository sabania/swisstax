---
typ: zuordnung-detail
titel: Zuordnung AR 2026 – Detail
jur: ar
jahre:
- 2026
generiert: tools/build_quick.py aus data/zuordnung/ar/2026.yaml (2026-11-09)
---

# AR 2026: Zuordnung Beleg → Ziffer – Detail

> Kompaktansicht: [quick/zuordnung-ar-2026.md](../../quick/zuordnung-ar-2026.md) · Formular: Steuererklärung 2025 Appenzell Ausserrhoden (Formular 1 Seiten 1-4, Hauptformular nicht online; Ziffern/Codes aus den Formular-Miniaturen der Wegleitung WL AR 2025) + Hilfsformulare 2 (Wertschriften), 4 (Berufskosten), 5 (Schulden, Zuwendungen, Parteispenden), 6 (Versicherungsprämien, Krankheits-/Behinderungskosten), 7/7Z (Liegenschaften), 10 (Kinderbetreuung) · Quelle der Wahrheit: `data/zuordnung/ar/2026.yaml`

> **Hinweis:** Gerüst aus 2025 (tools/new_year.py) – Formular und Wegleitung AR 2026 noch nicht publiziert (Stand 09.11.2026). Ziffern/Codes vorbehaltlich Änderungen; alle Positionen offen. Neu ab 2026 bundesrechtlich: Einkauf Säule 3a (Ziffer offen).

## Personalien

<a id="seite-1-personalien"></a>
### Ziff. Seite 1 – Personalien, Berufs- und Familienverhältnisse, Dauer der Steuerpflicht, Kinder (Formular 1 Seite 1)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Formular 1 Seite 1 (Stammdaten, Erwerbsart, Kinder in Ihrem Haushalt, Unterhaltsbeiträge)

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Haupterwerb unselbständig, Person 1 (Code 100) / Person 2 (Code 102)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** ⬜ offen
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn/Rente)

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Nebenerwerb unselbständig, Person 1 (Code 104) / Person 2 (Code 106), mit Art der Tätigkeit

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ⬜ offen
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn) des Nebenarbeitgebers
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Unselbständiger Nebenerwerb: Pauschale nach DBG-Pauschalansätzen: 20 % der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400. Nachweis höherer Kosten vorbehalten. Nebenamtliche Behördenmitglieder zusätzlich pauschal bis Fr. 2'600 (Behördenabzug).)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Minimum der Nebenerwerbspauschale (Verweis auf DBG).)** · Bund **CHF 800 (Mindestbetrag Pauschale Nebenerwerb.)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Maximum der Nebenerwerbspauschale (Verweis auf DBG). Zusätzlich Behördenabzug bis Fr. 2'600 für nebenamtliche Behördenmitglieder.)** · Bund **CHF 2'400 (Höchstbetrag Pauschale Nebenerwerb.)**

<a id="1-3-einkommen-unselbstaendig-vr-honorare"></a>
### Ziff. 1.3 – Sitzungsgelder, VR-Honorare, Behördenentschädigungen, Person 1 (Code 108) / Person 2 (Code 110)

- **Schlüssel:** `einkommen.unselbstaendig.vr_honorare` (VR-Honorare, Sitzungsgelder, Tantiemen (wo separat ausgewiesen, z.B. SG/AR Ziff. 1.3)) · **Status:** ⬜ offen
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 6 bzw. Bescheinigung der Behörde/Gesellschaft

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit (Industrie, Handel, Gewerbe, Landwirtschaft, freie Berufe, Internet-Plattformen), Person 1 (Code 112) / Person 2 (Code 114)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ⬜ offen
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Jahresrechnung (Bilanz, Erfolgsrechnung, Eigenkapitalnachweis, Abschreibungstabelle) bzw. Einnahmen-Ausgaben-Rechnung

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Kollektiv-, Kommanditgesellschaften und einfache Gesellschaften, Person 1 (Code 120) / Person 2 (Code 122)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ⬜ offen
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Angaben/Bescheinigung der Gesellschaft (inkl. Kapitalerträge)

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV-/IV-Renten (zu 100 %), Person 1 (Code 126) / Person 2 (Code 128)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ⬜ offen
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung der Ausgleichskasse (Jahresbetrag)

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen (2. Säule, Säule 3a, Unfall-/Haftpflichtversicherung, Leibrenten) mit steuerbarem Prozentsatz, Person 1 (Code 130) / Person 2 (Code 132)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ⬜ offen
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Rentenbescheinigung der Vorsorgeeinrichtung/Versicherung (Lohnausweis/Rentenbescheinigung Formular 11)

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigungen, Taggelder aus Kranken-, Unfall-, Invalidenversicherung, Mutterschaftsentschädigung (nicht im Lohnausweis), Person 1 (Code 134) / Person 2 (Code 136)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ⬜ offen
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Taggeldabrechnung/Bescheinigung der Versicherung bzw. Ausgleichskasse

<a id="3-4-einkommen-ersatz-taggelder"></a>
### Ziff. 3.4 – Arbeitslosentaggelder (nicht im Lohnausweis), Person 1 (Code 138) / Person 2 (Code 140)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ⬜ offen
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Arbeitslosenkasse

<a id="3-5-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.5 – Von Ausgleichskassen direkt ausbezahlte Kinder- und Familienzulagen (Code 142)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ⬜ offen
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Familienausgleichskasse

<a id="4-1-einkommen-wertschriften"></a>
### Ziff. 4.1 – Erträge aus Wertschriften und Guthaben inkl. Lotterie-/Geldspielgewinne (Code 146), Übertrag Formular 2

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ⬜ offen
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 Total Bruttoertrag A+B abzüglich Geschäftswertschriften (G) und Beteiligungserträge (BP, BG); Steuerauszug (eCH-0196)/Bankbescheinigungen
- **Limiten:**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'000'000 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen (nach BGS zugelassen) steuerfrei bis 1 Million Franken; Spielbankengewinne (Art. 27 lit. k) unbeschränkt steuerfrei, sofern nicht aus selbständiger Erwerbstätigkeit.)** · Bund **CHF 1'071'000 (Einzelne Gewinne aus nach BGS zugelassenen Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'071'000; darüber steuerbar (abzüglich Einsatzkosten nach Art. 33 Abs. 4 DBG).)**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'000 (Einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei, sofern Fr. 1'000 nicht überschritten werden; Gewinne aus Kleinspielen (nach BGS zugelassen) steuerfrei.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (Art. 1 Abs. 2 lit. d und e BGS) steuerfrei, sofern die Grenze von CHF 1'100 nicht überschritten wird. Gewinne aus Kleinspielen (BGS) sind steuerfrei.)**

<a id="4-2-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.2 – Erträge aus Beteiligungen ab 10 % (Privatvermögen, Code BP) (Code 147)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ⬜ offen
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2: Erträge mit Code BP (Übertrag ohne Vorzeichen)

<a id="4-3-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.3 – Erträge aus Beteiligungen ab 10 % (Geschäftsvermögen, Code BG) (Code 149)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ⬜ offen
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 2: Erträge mit Code BG; Jahresrechnung

<a id="5-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. 5 – Ertrag aus Liegenschaften: Eigenmietwert (abzüglich 20 % Selbstnutzungsabzug) und Mietertrag (Code 712), Übertrag Formular 7/7Z

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ⬜ offen
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Formular 7 Abschn. B (Total Erträge a. und b.) bzw. Formular 7Z Spalte B
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **20 % (Eigenmietwert dauernd selbstbewohnter Liegenschaften am Wohnsitz: massgeblicher Mietwert abzüglich 20 %; kein Abzug bei landwirtschaftlichen Liegenschaften sowie Zweit- und Ferienwohnungen. Bei Berechnung in % des Verkehrswertes zusätzlich -10 % (Schätzungsunsicherheit) und -10 % bei Selbstbewohnung am Wohnsitz.)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**

<a id="6-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 6.1 – Erhaltene Unterhaltsbeiträge: für geschiedene/getrennt lebende Person (Code 154); für minderjährige Kinder (Code 156)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ⬜ offen
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil bzw. Vereinbarung und Zahlungsnachweise

<a id="6-2-einkommen-erbschaften-unverteilt"></a>
### Ziff. 6.2 – Ertrag aus unverteilten Erbschaften (Code 158)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ⬜ offen
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung des Erbenvertreters/Erbteilung, Inventar und Erbenverzeichnis

<a id="6-3-einkommen-uebrige"></a>
### Ziff. 6.3 – Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen, nicht verrechnete Förderbeiträge) mit Art (Code 162)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ⬜ offen
- **Beleg → Feld:** Bescheinigung Mitarbeiterbeteiligung (Mitarbeiteraktien, Optionen, Anwartschaften/RSU, Beiblatt zum Lohnausweis), Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Aufstellung der Einkünfte; Mitarbeiterbeteiligungs-Bescheinigung

<a id="6-4-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 6.4 – Kapitalabfindungen für wiederkehrende Leistungen mit Anzahl Jahre (Code 164)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ⬜ offen
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der auszahlenden Stelle

## Einkommensberechnung

<a id="7-berechnung-total"></a>
### Ziff. 7 – Total der Einkünfte (Code 168)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 1-6)

<a id="18-berechnung-total"></a>
### Ziff. 18 – Total der Abzüge (Zeile nach Ziff. 17)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeile

<a id="20-berechnung-total"></a>
### Ziff. 20 – Nettoeinkommen (Basis für Selbstbehalt Krankheitskosten und Limite Zuwendungen)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeile (Total Einkünfte Ziff. 7 abzüglich Abzüge Ziff. 10-17)

<a id="21-1-abzug-krankheitskosten"></a>
### Ziff. 21.1 – Krankheits- und Unfallkosten nach Selbstbehalt (Vorkolonne: Total Formular 6; Hauptkolonne: über 5 % des Nettoeinkommens)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ⬜ offen
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 6 Seite 2 Total Krankheits- und Unfallkosten (selbst getragen)
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen nach Art. 28–35 verminderten steuerbaren Einkünfte.)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**

<a id="21-2-abzug-behinderungskosten"></a>
### Ziff. 21.2 – Behinderungsbedingte Kosten (Übertrag Formular 6 Seite 2; Pflegeheim-Pauschale 2/3, Pauschalen 2'500/5'000/7'500)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ⬜ offen
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 6 Seite 2 Behinderungsbedingte Kosten Total; Verfügung Hilflosenentschädigung; Bewohnerkonto Pflegeheim

<a id="21-3-abzug-spenden"></a>
### Ziff. 21.3 – Freiwillige Zuwendungen an steuerbefreite juristische Personen (Code 550), Übertrag Formular 5 Teil A

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ⬜ offen
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Formular 5 Teil A Total der Zuwendungen (Spendenbestätigungen auf Verlangen)
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz sowie Bund/Kantone/Gemeinden: ab Fr. 100 pro Steuerperiode.)** · Bund **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn im Steuerjahr mindestens CHF 100 erreicht.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Maximum 20 % der um die Aufwendungen nach Art. 28–35 verminderten steuerbaren Einkünfte.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**

<a id="22-berechnung-total"></a>
### Ziff. 22 – Reineinkommen

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeile (Nettoeinkommen abzüglich Abzüge Ziff. 21)

<a id="23-1-sozialabzug-kinder"></a>
### Ziff. 23.1 – Kinderabzug: Kind bis zur Vollendung des 4. Altersjahrs

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ⬜ offen
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Seite 1 der Steuererklärung (Kinder, Geburtsdatum) - Stichtag 31.12.2025
- **Limiten:**
  - Kinderabzug Vorschulalter (CHF): Kanton **CHF 5'300 (Kinderabzug bis zur Vollendung des 4. Altersjahres (indexiert per 1.1.2024). Voraussetzungen: Unterhalt zur Hauptsache, Kind unter elterlicher Sorge/Obhut, keine Unterhaltsbeiträge nach Art. 35 lit. c.)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (Art. 35 Abs. 1 lit. a DBG), keine Staffelung nach Alter; siehe sozialabzug.kind.**

<a id="23-2-sozialabzug-kinder"></a>
### Ziff. 23.2 – Kinderabzug: Kind nach Vollendung des 4. bis zur Vollendung des 15. Altersjahrs

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ⬜ offen
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Seite 1 der Steuererklärung (Kinder, Geburtsdatum)
- **Limiten:**
  - Kinderabzug Schulalter (CHF): Kanton **CHF 7'400 (Kinderabzug nach Vollendung des 4. bis zur Vollendung des 15. Altersjahres (indexiert per 1.1.2024).)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800, keine Staffelung nach Alter; siehe sozialabzug.kind.**

<a id="23-3-sozialabzug-kinder"></a>
### Ziff. 23.3 – Kinderabzug: Kind nach Vollendung des 15. Altersjahrs bis Volljährigkeit sowie volljährig in beruflicher/schulischer Ausbildung bis 26. Altersjahr

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ⬜ offen
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Seite 1 der Steuererklärung (Kinder, Schule/Lehrfirma, Dauer der Ausbildung)
- **Limiten:**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 11'600 (Kinderabzug nach Vollendung des 15. Altersjahres bis zur Volljährigkeit sowie für volljährige Kinder in beruflicher/schulischer Ausbildung bis zum 26. Altersjahr (indexiert per 1.1.2024). Bei volljährigen Kindern entfällt der Abzug, wenn Einkünfte des Kindes über Fr. 18'000 oder Reinvermögen über Fr. 250'000 (MB 02).)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Abzug CHF 6'800 (kein höherer Ausbildungsabzug beim Bund).)**

<a id="23-4-sozialabzug-unterstuetzung"></a>
### Ziff. 23.4 – Unterstützungsabzug für unterstützte Person (nur direkte Bundessteuer)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ⬜ offen
- **Beleg → Feld:** Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Bescheinigung der unterstützten Person/Zahlungsnachweise (Name, Adresse, Betrag)
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **n/a – Abzug nur DBSt (siehe data/werte/bund/); Beleg: ar-wl-2025__c0005 (Ziff. 23.4 «gilt nur für die direkte Bundessteuer»), Steuerjahr 2025.** · Bund **CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)**

<a id="24-berechnung-total"></a>
### Ziff. 24 – Steuerbares Einkommen

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeile (Reineinkommen abzüglich Sozialabzüge)

## Weitere Angaben

<a id="8-1-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 8.1 – Im vereinfachten Abrechnungsverfahren (BGSA) abgerechneter Bruttolohn - nur Information (Code 290)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Abrechnung/Bescheinigung der AHV-Ausgleichskasse

<a id="8-2-info-steuerfreie-leistungen"></a>
### Ziff. 8.2 – Ergänzungsleistungen (nur Information) (Code 291)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ⬜ offen
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung/Bescheinigung der Ausgleichskasse

<a id="8-3-info-steuerfreie-leistungen"></a>
### Ziff. 8.3 – Hilflosenentschädigungen (nur Information) (Code 292)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ⬜ offen
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung der Hilflosenentschädigung

<a id="8-4-info-steuerfreie-leistungen"></a>
### Ziff. 8.4 – Überbrückungsleistungen für ältere Arbeitslose (nur Information) (Code 293)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ⬜ offen
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung über Überbrückungsleistungen

<a id="40-41-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. 40-41 – Ausbezahlte Kapitalleistungen aus Vorsorge: 40.1 Säule 3a, 40.2 berufliche Vorsorge, 40.3 übrige; Total Ziff. 41 (Code 950)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ⬜ offen
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung/Bank

## Abzüge

<a id="10-1-abzug-berufskosten-uebrige"></a>
### Ziff. 10.1 – Berufskosten unselbständig Erwerbende, Person 1 (Total Formular 4, Code 438); Person 2 unter Ziff. 10.2 (Code 488)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ⬜ offen
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Formular 4 Ziff. 6 Total der Berufskosten (Person 1 Vorderseite, Person 2 Rückseite)
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte (ÖV oder privates Fahrzeug, wenn ÖV nicht zur Verfügung steht/unzumutbar): Höchstbetrag Fr. 6'000 pro Person.)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Übrige Berufskosten: Fr. 700 zuzüglich 10 % der Nettoeinkünfte, höchstens Fr. 2'400. Nachweis höherer Kosten vorbehalten.)** · Bund **3 % (Übrige Berufskosten: Pauschale 3 % des Nettolohns, mindestens CHF 2'000, höchstens CHF 4'000 pro Jahr; Nachweis höherer tatsächlicher Kosten möglich. Bei Teilzeit/Teiljahr angemessen zu kürzen.)**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockelbetrag der Pauschale für übrige Berufskosten.)** · Bund **n/a – Formel ohne fixen Anteil (3 % des Nettolohns, min. 2'000, max. 4'000).**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Höchstbetrag der Pauschale für übrige Berufskosten.)** · Bund **CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)**

<a id="11-abzug-schuldzinsen"></a>
### Ziff. 11 – Schuldzinsen (privat), Übertrag Formular 5 Teil A (Code nicht verifiziert)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ⬜ offen
- **Beleg → Feld:** Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 5 Teil A Total private Schuldzinsen (Spalte rechts)

<a id="12-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.1 – Unterhaltsbeiträge an geschiedene/getrennt lebende Person

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ⬜ offen
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungsurteil/Trennungsvereinbarung, Zahlungsnachweise

<a id="12-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.2 – Unterhaltsbeiträge für minderjährige Kinder (an den Elternteil mit Sorge/Obhut)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ⬜ offen
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungsurteil/Vereinbarung, Zahlungsnachweise

<a id="12-3-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.3 – Rentenleistungen (Leibrenten nach OR, Ertragsanteil)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Vertrag/Bescheinigung der Rentenzahlung

<a id="13-1-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.1 – Beiträge Säule 3a (gebundene Selbstvorsorge)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ⬜ offen
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Bescheinigung der Bank-/Versicherungsstiftung (Formular 21 EDP)
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a mit Zugehörigkeit zur 2. Säule: Abzug im Sinn und im Umfang von Art. 82 BVG, max. Fr. 7'258 pro Jahr (8 % des oberen Grenzbetrags, BVV 3 Art. 7).)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug CHF 7'258 pro Jahr für Personen, die einer Vorsorgeeinrichtung der 2. Säule angehören (8 % des oberen Grenzbetrags nach Art. 8 Abs. 1 BVG). Nur im Steuerjahr tatsächlich einbezahlte Beiträge, mit Bescheinigung.)**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens Fr. 36'288 pro Jahr (Art. 82 BVG / BVV 3 Art. 7).)** · Bund **CHF 36'288 (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens CHF 36'288 pro Jahr.)**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. Fr. 36'288).)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (alle Einkünfte aus selbständiger und unselbständiger, haupt- und nebenberuflicher Erwerbstätigkeit), max. CHF 36'288.)**

<a id="13-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 13.2 – Beiträge/Einkäufe in die 2. Säule (soweit nicht im Lohnausweis abgezogen)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ⬜ offen
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) mit Einkaufsberechnung; Lohnausweis Ziff. 10.1/10.2

<a id="14-abzug-versicherungspraemien"></a>
### Ziff. 14 – Versicherungsprämien und Zinsen von Sparkapitalien (Übertrag Formular 6 Teil C, Code 600)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ⬜ offen
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 6 Teil C: niedrigerer Betrag aus A (bezahlte Prämien/Sparzinsen abzüglich Prämienverbilligung) und B (Maximum)
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'400 (Versicherungsprämien/Sparzinsen: Fr. 5'400 für in ungetrennter Ehe lebende Personen.)** · Bund **CHF 3'700 (Versicherungsprämien und Zinsen von Sparkapitalien, Ehepaare in ungetrennter Ehe, mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 3'700.)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'700 (Versicherungsprämien/Sparzinsen: Fr. 2'700 für die übrigen steuerpflichtigen Personen.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 1'800.)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag pro Kind, für das ein Kinderabzug nach Art. 38 geltend gemacht werden kann.)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**

<a id="15-abzug-liegenschaft-unterhalt"></a>
### Ziff. 15 – Unterhalts- und Verwaltungskosten Liegenschaften: Pauschalabzug (C1) oder tatsächliche Kosten (C2), Übertrag Formular 7/7Z

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ⬜ offen
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Formular 7 Abschn. C bzw. Formular 7Z Spalte C1/C2
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Pauschalabzug Unterhalt/Verwaltung: 10 % des Bruttomietertrags bei Gebäuden bis 10 Jahre; nur wenn jährlicher Bruttomietertrag des gesamten Liegenschaftsbesitzes höchstens Fr. 100'000; Wahlrecht je Gebäude und Veranlagungsperiode; bei Eigenmietwert ist dieser massgebend.)** · Bund **10 % (Pauschalabzug Liegenschaftskosten (anstelle effektiver Kosten, Wahl pro Periode und Liegenschaft): 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist.)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Pauschalabzug: 20 % des Bruttomietertrags für ältere Gebäude (über 10 Jahre); Voraussetzungen wie liegenschaft.pauschale_neu.)** · Bund **20 % (Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist.)**

<a id="16-1-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. 16.1 – Verwaltungskosten Wertschriften/Kapitalanlagen (tatsächlich oder Pauschale)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ⬜ offen
- **Beleg → Feld:** Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Depotgebührenausweis der Bank / Steuerauszug (Bestand per 31.12. fremdverwalteter Titel)

<a id="16-2-abzug-drittbetreuung"></a>
### Ziff. 16.2 – Kinderbetreuungskosten durch Drittpersonen (Übertrag Formular 10)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ⬜ offen
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Formular 10 Total Kinderbetreuungskosten (Rechnungen Krippe/Tagesfamilie, Empfänger muss ersichtlich sein)
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 25'000 (Nachgewiesene Kinderdrittbetreuungskosten, max. Fr. 25'000 pro Kind (Kind im gleichen Haushalt, kausaler Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit).)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind, höchstens CHF 25'800; Kind unter 14 Jahren im gleichen Haushalt; Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 (Kind hat das 14. Altersjahr noch nicht vollendet.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat.)**

<a id="16-3-abzug-parteispenden"></a>
### Ziff. 16.3 – Mitgliederbeiträge und Zuwendungen an politische Parteien (Code 555), Übertrag Formular 5 Teil B

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ⬜ offen
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Formular 5 Teil B Total der Parteispenden
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister, im kantonalen Parlament vertreten oder mind. 3 % Stimmen): bis Fr. 10'000 gesamt.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister / kantonales Parlament / mind. 3 % Stimmen): bis Gesamtbetrag CHF 10'600.)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **n/a** · Bund **–**

<a id="16-4-abzug-weiterbildung"></a>
### Ziff. 16.4 – Berufsorientierte Aus- und Weiterbildungskosten inkl. Umschulung, Person 1 / Person 2 (Hauptformular, kein eigenes Hilfsblatt)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ⬜ offen
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Kursrechnungen/Zahlungsbelege der steuerpflichtigen Person; Lohnausweis Ziff. 13.3 (Vergütungen des Arbeitgebers)
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 12'000 (Berufsorientierte Aus- und Weiterbildungskosten inkl. Umschulung: max. Fr. 12'000 pro steuerpflichtige Person, sofern erster Abschluss Sekundarstufe II oder 20. Lebensjahr vollendet (nicht Ausbildung bis erster Abschluss Sek. II).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildungs- inkl. Umschulungskosten bis CHF 13'000 pro Jahr, sofern erster Abschluss Sek. II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)**

<a id="16-6-abzug-uebrige"></a>
### Ziff. 16.6 – Übrige Abzüge (AHV-Beiträge Nichterwerbstätiger, Einsatzkosten Geldspiele, nicht im Nettolohn berücksichtigte NBUV-/BVG-Beiträge)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ⬜ offen
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → AHV-Beitragsverfügung; Lohnausweis (NBUV/BVG-Abzüge Ziff. 9/10)

<a id="16-7-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 16.7 – Abzug Teilbesteuerung Beteiligungserträge (40 % der Erträge Ziff. 4.2)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ⬜ offen
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Berechnung aus Ziff. 4.2 (Privatbeteiligungen ab 10 %)

<a id="17-abzug-zweiverdiener"></a>
### Ziff. 17 – Zweiverdienerabzug (gemeinsam veranlagte, beide erwerbstätig)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechnung aus den beiden Nettoerwerbseinkommen
- **Limiten:**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **10 % (Zweiverdienerabzug: 10 % des niedrigeren Erwerbseinkommens (Ehegatten in rechtlich und tatsächlich ungetrennter Ehe), mindestens Fr. 2'500, höchstens Fr. 5'200 (indexiert per 1.1.2024).)** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (Ehepaare in ungetrennter Ehe, beide erwerbstätig).)**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **CHF 2'500 (Minimum Zweiverdienerabzug (indexierter Betrag per 1.1.2024; Gesetzestext nennt noch Fr. 2'400).)** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum.)**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **CHF 5'200 (Maximum Zweiverdienerabzug (indexierter Betrag per 1.1.2024; Gesetzestext nennt noch Fr. 5'000).)** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum.)**

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben inkl. Kryptowährungen (Code 300), Übertrag Formular 2

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ⬜ offen
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 Total Steuerwert per 31.12.2025 (Spalte 'Steuerwert am 31. Dezember 2025'); Steuerauszug (eCH-0196)

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 302)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ⬜ offen
- **Beleg → Feld:** Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Aufstellung/Bewertung zum Verkehrswert per 31.12.

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen mit Rückkaufswert (Code 304) mit Versicherungsgesellschaft, Abschluss-/Ablaufjahr, Versicherungssumme

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ⬜ offen
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Steuerwertbescheinigung der Versicherungsgesellschaft (Rückkaufswert + Überschussguthaben)

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge mit Art, Kaufpreis, Erwerbsjahr (Code 306)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ⬜ offen
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg, Motorfahrzeug-Versicherungspolice (Haftpflicht/Kasko) und Verkehrssteuer-Rechnung → Kaufbeleg/Fahrzeugausweis (Anschaffungswert, Erwerbsjahr)

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Anteil an unverteilter Erbschaft (Code 308), mit Aufstellung

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ⬜ offen
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Inventar und Erbenverzeichnis (Kopie beilegen)

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte (Boote, Reitpferde, Kunstsammlungen u.a.) (Code 310)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ⬜ offen
- **Beleg → Feld:** Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Aufstellung der Vermögenswerte mit Verkehrswert

<a id="31-vermoegen-liegenschaften"></a>
### Ziff. 31 – Liegenschaften, Steuerwert (Code 710), Übertrag Formular 7 Abschn. A / 7Z

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ⬜ offen
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Formular 7 Abschn. A Steuerwert; amtliche Schätzung (vom Grundbuchamt eröffnet)

<a id="32-1-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.1 – Geschäftskapital in Kollektiv-, Kommandit- und einfachen Gesellschaften (Code 314), mit Aufstellung

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ⬜ offen
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Angaben/Bilanz der Gesellschaft (Anteil am Vermögen)

<a id="32-2-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.2 – Geschäftsaktiven gemäss Schlussbilanz (ohne Liegenschaften) (Code 316)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ⬜ offen
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Schlussbilanz/Zusammenstellung Betriebsvermögen

<a id="32-3-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.3 – Vermögen im landwirtschaftlichen Betrieb (Code 318)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ⬜ offen
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Spezielle Landwirte-Formulare (12/14)

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 322)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeile (Ziff. 30-32)

<a id="34-1-schulden-privat"></a>
### Ziff. 34.1 – Privatschulden (Code 504), Übertrag Formular 5 Teil A

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ⬜ offen
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 5 Teil A Schuld am 31.12.2025 (Total); Hypothekar-/Kreditbestätigung

<a id="34-2-schulden-privat"></a>
### Ziff. 34.2 – Geschäftsschulden (Code 506), Übertrag Formular 5 Teil B

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ⬜ offen
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 5 Teil B Total Geschäftsschulden (per Bilanzstichtag)

<a id="35-berechnung-total"></a>
### Ziff. 35 – Reinvermögen (Code 326)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeile (Ziff. 33 abzüglich 34)

<a id="36-1-vermoegen-sozialabzug"></a>
### Ziff. 36.1 – Sozialabzug alleinstehende Steuerpflichtige (Code 330)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Personalien (Zivilstand 31.12.2025)
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 75'000 (Steuerfreier Betrag vom Reinvermögen für alle übrigen steuerpflichtigen Personen.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**

<a id="36-2-vermoegen-sozialabzug"></a>
### Ziff. 36.2 – Sozialabzug gemeinsam steuerpflichtige Ehegatten (Code 332)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Personalien (Zivilstand 31.12.2025)
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 150'000 (Steuerfreier Betrag für Ehegatten in rechtlich und tatsächlich ungetrennter Ehe.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**

<a id="36-3-vermoegen-sozialabzug"></a>
### Ziff. 36.3 – Sozialabzug je minderjähriges Kind (Code 334)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ⬜ offen
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Seite 1 der Steuererklärung (Kinder, Jahrgang)
- **Limiten:**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 25'000 (Zusätzlich pro minderjähriges Kind unter elterlicher Sorge/Obhut, für das ein Kinderabzug nach Art. 38 Abs. 1 geltend gemacht werden kann.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**

<a id="36-5-vermoegen-sozialabzug"></a>
### Ziff. 36.5 – Ermässigung auf ausserrhodischen Beteiligungen (Code 335)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Beteiligungsbewertung

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen gesamt (Code 338)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeile (Ziff. 35 abzüglich 36.1-36.5)

## Hilfsblatt Berufskosten (Form. 4)

<a id="form-4-ziff-1-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.1 – Fahrkosten öffentliche Verkehrsmittel (Code 400 Person 1 / 450 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ⬜ offen
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → ÖV-Abo/Fahrausweise (tatsächliche Kosten); Lohnausweis Feld F
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte (ÖV oder privates Fahrzeug, wenn ÖV nicht zur Verfügung steht/unzumutbar): Höchstbetrag Fr. 6'000 pro Person.)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **Keine AR-Quelle für 2026 zur Anzahl Arbeitstage.** · Bund **n/a – Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).**

<a id="form-4-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.2 – Fahrrad/Kleinmotorrad bis 50 cm3 (gelbes Kontrollschild) (Code 402 / 452)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Pauschale (keine Belege)
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Pauschale Fahrrad/Motorfahrrad (und Motorrad mit gelbem Kontrollschild) Fr. 700 pro Jahr; AR übernimmt per Verweis (Art. 15 Abs. 3 StV) die DBG-Pauschalansätze.)** · Bund **CHF 700 (Fahrrad, Motorfahrrad, Motorrad mit gelbem Kontrollschild: Pauschale CHF 700 pro Jahr; tatsächliche Kosten können nicht zusätzlich geltend gemacht werden.)**

<a id="form-4-ziff-1-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.3 – Privates Motorfahrzeug in begründeten Fällen (Code 404/454); Zwischentotal 1.1-1.3 max. Fr. 6'000 (Code 405/455)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ⬜ offen
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg, Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Fahrtenaufstellung (km, Tage), Begründung (Formular 4 Ankreuzfelder)
- **Limiten:**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.75 (Kilometeransatz Auto 75 Rappen/km (2026, neu; 2025: 70 Rappen). Gilt auch für Staats- und Gemeindesteuern AR.)** · Bund **CHF 0.75 (Privatauto: CHF 0.75 pro Fahrkilometer, nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist; Gesamtmaximum CHF 3'300.)**
  - Fahrkosten Motorrad – Ansatz pro km (CHF): Kanton **CHF 0.40 (Kilometeransatz Motorrad (weisses Kontrollschild) 40 Rappen/km; AR übernimmt per Verweis (Art. 15 Abs. 3 StV) die DBG-Pauschalansätze. Nur wenn kein ÖV zur Verfügung steht/zumutbar; Gesamtmaximum AR Fr. 6'000.)** · Bund **CHF 0.40 (Motorrad mit weissem Kontrollschild: CHF 0.40 pro Fahrkilometer (nur wenn kein öffentliches Verkehrsmittel zumutbar); Gesamtmaximum CHF 3'300.)**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte (ÖV oder privates Fahrzeug, wenn ÖV nicht zur Verfügung steht/unzumutbar): Höchstbetrag Fr. 6'000 pro Person.)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **Keine AR-Quelle für 2026 zur Anzahl Arbeitstage.** · Bund **n/a – Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).**

<a id="form-4-ziff-2-1-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.1 – Mehrkosten auswärtige Verpflegung: Fr. 15 pro Arbeitstag, max. Fr. 3'200 (Code 408 / 458)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ⬜ offen
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis (Felder F/G, Ziff. 15); Arbeitstage
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswärtige Verpflegung Fr. 15 pro Tag (voller Abzug) nach den für die direkte Bundessteuer massgebenden Pauschalansätzen; Voraussetzung: Hauptmahlzeit zu Hause nicht zumutbar (Entfernung oder kurze Essenspause) oder durchgehende Schichtarbeit.)** · Bund **CHF 15 (Auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (in der Regel nur Mittagessen), nur Pauschale zulässig, wenn Hauptmahlzeit wegen grosser Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann oder bei durchgehender Schicht-/Nachtarbeit.)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Mehrkosten auswärtige Verpflegung, voller Abzug max. Fr. 3'200 pro Jahr (DBG-Pauschalansatz, per Verweis in Art. 16 Abs. 1 StV).)** · Bund **CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)**

<a id="form-4-ziff-2-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.2 – Verpflegung durch Arbeitgeber verbilligt (Kantine, Lunch-Checks, Beitrag): Fr. 7.50 pro Tag, max. Fr. 1'600 (Code 410 / 460)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ⬜ offen
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten)
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Halber Abzug Fr. 7.50 pro Tag, wenn die Verpflegung in einem Personalrestaurant eingenommen werden kann oder eine wesentliche Verbilligung durch Beiträge des Arbeitgebers erfolgt (Art. 16 Abs. 2 StV; Betrag = halber DBG-Ansatz).)** · Bund **CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Halber Jahresabzug max. Fr. 1'600 (Art. 16 Abs. 2 StV; DBG-Pauschalansatz).)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)**

<a id="form-4-ziff-2-3-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.3 – Schicht-/Nachtarbeit (durchgehend mind. 8 Std.): Fr. 15 pro Schichttag, max. Fr. 3'200 (Code 412 / 462)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ⬜ offen
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 (Bemerkungen: Anzahl Schichttage)
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Schichtarbeit (inkl. gestaffelte/unregelmässige Arbeitszeit): Pauschale Fr. 15 pro Tag nach DBG-Pauschalansätzen (max. Fr. 3'200 pro Jahr); nicht zusätzlich zum Verpflegungsabzug (Art. 16 Abs. 1, 3, 4 StV).)** · Bund **CHF 15 (Schicht-/Nachtarbeit: gleiche Pauschale wie auswärtige Verpflegung, CHF 15 pro Tag bzw. max. CHF 3'200 pro Jahr (bei Verbilligung halber Abzug). Gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt (Art. 6 Abs. 4 BKV). Arbeitgeber muss Tage und Arbeitsort auf Verlangen bescheinigen.)**

<a id="form-4-ziff-3-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4 Ziff. 3 – Übrige Berufskosten: Pauschale Fr. 700 + 10 % des Nettolohns, max. Fr. 2'400 (Code 416 / 466) oder tatsächliche Kosten mit Aufstellung (Code 418 / 468)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ⬜ offen
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Ziff. 11 (Nettolohn) für die Pauschale; Kostenaufstellung/Belege bei effektiv
- **Limiten:**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Übrige Berufskosten: Fr. 700 zuzüglich 10 % der Nettoeinkünfte, höchstens Fr. 2'400. Nachweis höherer Kosten vorbehalten.)** · Bund **3 % (Übrige Berufskosten: Pauschale 3 % des Nettolohns, mindestens CHF 2'000, höchstens CHF 4'000 pro Jahr; Nachweis höherer tatsächlicher Kosten möglich. Bei Teilzeit/Teiljahr angemessen zu kürzen.)**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockelbetrag der Pauschale für übrige Berufskosten.)** · Bund **n/a – Formel ohne fixen Anteil (3 % des Nettolohns, min. 2'000, max. 4'000).**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Höchstbetrag der Pauschale für übrige Berufskosten.)** · Bund **CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)**
  - Arbeitszimmer/Homeoffice – Regel: Kanton **Arbeitszimmer in der Privatwohnung nur bei spezifisch eingerichtetem, tatsächlich ausgeschiedenem Arbeitsplatz und wenn mindestens 40 % der Tätigkeit (gemessen an einer Vollzeitbeschäftigung) zu Hause erledigt werden müssen.** · Bund **Privates Arbeitszimmer: in der Pauschale übrige Berufskosten enthalten. Separater Abzug der Zimmerkosten (Miete, Heizung, Beleuchtung) nur bei Nachweis höherer Kosten und wenn ein Zimmer der Privatwohnung hauptsächlich und regelmässig für die Berufsarbeit benützt werden muss; bloss gelegentliche Arbeit zu Hause gibt keinen Abzug. Keine pauschale Homeoffice-Entschädigung.**

<a id="form-4-ziff-4-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4 Ziff. 4 – Wochenaufenthalt: Zimmer (Code 426 / 476), Verpflegung Fr. 30/Tag, max. Fr. 6'400 bzw. Fr. 22.50/Tag, max. Fr. 4'800 (Code 428 / 478)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ⬜ offen
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag/Quittungen des Zimmers; Lohnausweis (verbilligte Mahlzeiten)
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Auswärtige Unterkunft: höchstens die ortsüblichen Mietkosten für ein Zimmer; Fahrt zur auswärtigen Unterkunft sinngemäss nach Art. 15 StV. Voraussetzung: tägliche Rückkehr an den Wohnsitz nicht zumutbar.** · Bund **Wochenaufenthalt: abziehbar sind die ortsüblichen Auslagen für ein Zimmer (nicht eine Wohnung) am Arbeitsort sowie die Fahrkosten der regelmässigen Heimkehr (im Rahmen des Fahrkosten-Maximums).**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 6'400 (Verpflegung bei auswärtigem Wochenaufenthalt: nach DBG-Pauschalansätzen voller Abzug Fr. 6'400 pro Jahr (Fr. 30/Tag).)** · Bund **CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug CHF 30 pro Tag bzw. CHF 6'400 pro Jahr; gekürzter Abzug (verbilligtes Mittagessen) CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr. Nachweis höherer Kosten ausgeschlossen.)**

<a id="form-4-ziff-5-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 4 Ziff. 5 – Unselbständiger Nebenerwerb: Pauschale 20 % der Nettoeinkünfte, mind. Fr. 800, max. Fr. 2'400 (Code 432 / 482) oder tatsächliche Kosten (Code 434 / 484)

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ⬜ offen
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 des Nebenarbeitgebers
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Unselbständiger Nebenerwerb: Pauschale nach DBG-Pauschalansätzen: 20 % der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400. Nachweis höherer Kosten vorbehalten. Nebenamtliche Behördenmitglieder zusätzlich pauschal bis Fr. 2'600 (Behördenabzug).)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Minimum der Nebenerwerbspauschale (Verweis auf DBG).)** · Bund **CHF 800 (Mindestbetrag Pauschale Nebenerwerb.)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Maximum der Nebenerwerbspauschale (Verweis auf DBG). Zusätzlich Behördenabzug bis Fr. 2'600 für nebenamtliche Behördenmitglieder.)** · Bund **CHF 2'400 (Höchstbetrag Pauschale Nebenerwerb.)**

<a id="form-4-ziff-6-berechnung-total"></a>
### Ziff. Form. 4 Ziff. 6 – Total der Berufskosten (Code 438 Person 1 -> Ziff. 10.1; Code 488 Person 2 -> Ziff. 10.2)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Formular 4 Rechenzeile

## Hilfsblatt Wertschriftenverzeichnis (Form. 2)

<a id="form-2-spalten-a-b-vermoegen-wertschriften-guthaben"></a>
### Ziff. Form. 2 Spalten A/B – Verzeichnis der Vermögenswerte: Steuerwert per 31.12.2025 und Bruttoertrag 2025, Spalte A (mit Verrechnungssteuerabzug) / Spalte B (ohne)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ⬜ offen
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Steuerauszug (eCH-0196)/Bankbescheinigung: Valoren-Nr., Stückzahl, Steuerwert per 31.12.2025, Bruttoertrag 2025

<a id="form-2-total-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 2 Total – Verrechnungssteueranspruch 35 % vom Bruttoertrag (Total A) (Code 999)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ⬜ offen
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2 Total A (Rückerstattungsantrag Verrechnungssteuer)

<a id="form-2-s-1-960-961-info-schenkungen-erbschaften"></a>
### Ziff. Form. 2 S. 1 (960/961) – Fragen Erbschaften: erhaltene Erbschaft/Vermächtnis (Code 960); Beteiligung an unverteilter Erbschaft mit Erbanteil (Code 961)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ⬜ offen
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Erbteilungsvertrag/Erbteilungsakt (Kopie), Inventar und Erbenverzeichnis

<a id="form-2-s-1-962-963-info-schenkungen-erbschaften"></a>
### Ziff. Form. 2 S. 1 (962/963) – Fragen Schenkungen: Vermögen aus Schenkung/Erbvorbezug erworben (Code 962); Vermögen verschenkt (Code 963)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ⬜ offen
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Schenkungsvertrag/Aufstellung

## Hilfsblatt Schulden/Zuwendungen (Form. 5)

<a id="form-5-teil-a-schulden-privat"></a>
### Ziff. Form. 5 Teil A – Private Schulden (Schuldbestand 31.12.2025) und Schuldzinsen 2025

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ⬜ offen
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Hypothekar-/Kreditbestätigung der Bank: Gläubiger, Schuld per 31.12.2025, Zinsen 2025

<a id="form-5-teil-b-schulden-privat"></a>
### Ziff. Form. 5 Teil B – Geschäftsschulden (Schuld am 31.12. bzw. Bilanzstichtag)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ⬜ offen
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz/Schuldenbestätigung

<a id="form-5-s-2-teil-a-abzug-spenden"></a>
### Ziff. Form. 5 S. 2 Teil A – Freiwillige Zuwendungen: Institution, Datum, Betrag; Total (Code 550) -> Ziff. 21.3

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ⬜ offen
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigung der steuerbefreiten Institution (auf Verlangen)
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz sowie Bund/Kantone/Gemeinden: ab Fr. 100 pro Steuerperiode.)** · Bund **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn im Steuerjahr mindestens CHF 100 erreicht.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Maximum 20 % der um die Aufwendungen nach Art. 28–35 verminderten steuerbaren Einkünfte.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**

<a id="form-5-s-2-teil-b-abzug-parteispenden"></a>
### Ziff. Form. 5 S. 2 Teil B – Parteispenden: Partei, Datum, Betrag; Total (Code 555) -> Ziff. 16.3

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ⬜ offen
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Bestätigung der Partei (auf Verlangen)
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister, im kantonalen Parlament vertreten oder mind. 3 % Stimmen): bis Fr. 10'000 gesamt.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister / kantonales Parlament / mind. 3 % Stimmen): bis Gesamtbetrag CHF 10'600.)**

## Hilfsblatt Versicherungsprämien/Krankheitskosten (Form. 6)

<a id="form-6-teil-a-abzug-versicherungspraemien"></a>
### Ziff. Form. 6 Teil A – Bezahlte Versicherungsprämien und Sparzinsen: a. Krankenversicherung (brutto), b. Unfallversicherung (ohne NBUV), c. Lebens-/Rentenversicherungen, d. Sparzinsen, e. abzüglich Prämienverbilligungen (Code 600 A)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ⬜ offen
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Prämienrechnung/Jahresbescheinigung Krankenversicherung (brutto), Prämienverbilligungs-Verfügung, Zinsausweis (Sparzinsen gemäss Wertschriftenverzeichnis)

<a id="form-6-teil-b-c-abzug-versicherungspraemien"></a>
### Ziff. Form. 6 Teil B/C – Maximaler Abzug (Code 600 B): Fr. 5'400 gemeinsam / Fr. 2'700 übrige + Fr. 1'000 je Kind; Abzug = niedrigerer Betrag aus A und B (Code 600) -> Ziff. 14

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeilen
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'400 (Versicherungsprämien/Sparzinsen: Fr. 5'400 für in ungetrennter Ehe lebende Personen.)** · Bund **CHF 3'700 (Versicherungsprämien und Zinsen von Sparkapitalien, Ehepaare in ungetrennter Ehe, mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 3'700.)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'700 (Versicherungsprämien/Sparzinsen: Fr. 2'700 für die übrigen steuerpflichtigen Personen.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 1'800.)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag pro Kind, für das ein Kinderabzug nach Art. 38 geltend gemacht werden kann.)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**

<a id="form-6-s-2-abzug-krankheitskosten"></a>
### Ziff. Form. 6 S. 2 – Krankheits- und Unfallkosten: Rechnungsdatum, Arzt/Zahnarzt/Spital, Bruttobetrag abzüglich Beiträge Dritter = selbst getragene Kosten; Total -> Ziff. 21.1 (Vorkolonne)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ⬜ offen
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Arzt-/Zahnarztrechnungen und KK-Leistungsabrechnung (Vergütungen Dritter)

<a id="form-6-s-2-behinderungsbedingt-abzug-behinderungskosten"></a>
### Ziff. Form. 6 S. 2 (behinderungsbedingt) – Behinderungsbedingte Kosten (Einzelleistungen); Total -> Ziff. 21.2

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ⬜ offen
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Rechnungen/Verfügungen (Hinweise in der Wegleitung)

## Hilfsblatt Liegenschaften (Form. 7/7Z)

<a id="form-7-abschn-a-vermoegen-liegenschaften"></a>
### Ziff. Form. 7 Abschn. A – Angaben zur Liegenschaft, Anteil Person 1/2, Nutzung, Baujahr, Steuerwert (Verkehrswert gemäss Grundstückschätzung)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ⬜ offen
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Amtliche Grundstückschätzung (Steuerwert, Grundstücknummer, Baujahr)

<a id="form-7-abschn-b-a-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 7 Abschn. B a – Eigenmietwert abzüglich 20 % = anrechenbarer Eigenmietwert

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ⬜ offen
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Amtliche Grundstückschätzung (Mietwert)
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **20 % (Eigenmietwert dauernd selbstbewohnter Liegenschaften am Wohnsitz: massgeblicher Mietwert abzüglich 20 %; kein Abzug bei landwirtschaftlichen Liegenschaften sowie Zweit- und Ferienwohnungen. Bei Berechnung in % des Verkehrswertes zusätzlich -10 % (Schätzungsunsicherheit) und -10 % bei Selbstbewohnung am Wohnsitz.)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**

<a id="form-7-abschn-b-b-einkommen-liegenschaften-mietertrag"></a>
### Ziff. Form. 7 Abschn. B b – Erträge Fremdnutzung und Leistungen Dritter (Miet-/Pachtzinsen abzüglich Nebenkosten), inkl. PV-Einspeisevergütung

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ⬜ offen
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Mietverträge/Mietzinsabrechnung, Abrechnung Netzbetreiber

<a id="form-7-abschn-c-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 7 Abschn. C – Unterhalts- und Verwaltungskosten: Pauschalabzug (C1) oder tatsächliche Kosten (C2, Rückseite)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ⬜ offen
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Rechnungen (Datum, Rechnungssteller, Beschreibung, Unterhalt/Anlagekosten/Verwaltung)
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Pauschalabzug Unterhalt/Verwaltung: 10 % des Bruttomietertrags bei Gebäuden bis 10 Jahre; nur wenn jährlicher Bruttomietertrag des gesamten Liegenschaftsbesitzes höchstens Fr. 100'000; Wahlrecht je Gebäude und Veranlagungsperiode; bei Eigenmietwert ist dieser massgebend.)** · Bund **10 % (Pauschalabzug Liegenschaftskosten (anstelle effektiver Kosten, Wahl pro Periode und Liegenschaft): 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist.)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Pauschalabzug: 20 % des Bruttomietertrags für ältere Gebäude (über 10 Jahre); Voraussetzungen wie liegenschaft.pauschale_neu.)** · Bund **20 % (Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist.)**

<a id="form-7z-vermoegen-liegenschaften"></a>
### Ziff. Form. 7Z – Zusammenzug aller Liegenschaften: Spalten Steuerwert (A) -> Ziff. 31, Erträge (B) -> Ziff. 5, Pauschalabzug (C1) / tatsächliche Kosten (C2) -> Ziff. 15

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ⬜ offen
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Ergebnisse der einzelnen Formulare 7

## Hilfsblatt Kinderbetreuung (Form. 10)

<a id="form-10-abzug-drittbetreuung"></a>
### Ziff. Form. 10 – Kinderbetreuungskosten: Rechnungsdatum, Name des Kindes, Empfänger, Kosten; tatsächliche Kosten abzüglich erhaltene Beiträge; Total -> Ziff. 16.2

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ⬜ offen
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Rechnungen Krippe/Tagesfamilie (Empfänger ersichtlich)
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 25'000 (Nachgewiesene Kinderdrittbetreuungskosten, max. Fr. 25'000 pro Kind (Kind im gleichen Haushalt, kausaler Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit).)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind, höchstens CHF 25'800; Kind unter 14 Jahren im gleichen Haushalt; Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)**
