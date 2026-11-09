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
- **Regel:** Stichtag der Verhältnisse ist der 31.12.2026 bzw. das Ende der Steuerpflicht. Die Frage «Ordentliche Beiträge an die Pensionskasse (2. Säule)?» steuert den höheren Versicherungsabzug (Ziff. 15, Teil B). Bei unterjähriger Steuerpflicht ist die Dauer der Steuerpflicht einzutragen.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0002.md) `zh-form-300-2026-uj__c0002` – «Personalien per 31.12.2026 bzw. per Ende der Steuerpflicht»

<a id="s-1-kinder-personalien"></a>
### Ziff. S. 1 Kinder – Kinder im und ausserhalb des Haushalts (Jahrgänge 2009–2026 oder in beruflicher Erstausbildung)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Geburtsdatum, Ausbildung (Schule/Lehrfirma), Ausbildungsende, ob der andere Elternteil Unterhaltsbeiträge leistet
- **Regel:** Grundlage für Kinderabzug (Ziff. 24.1), Versicherungszuschlag (Ziff. 15 Teil B), Kinderdrittbetreuung (Ziff. 16.6). Angabe «Leistet der andere Elternteil Unterhaltsbeiträge?» ist bei ledigen, geschiedenen oder getrennt lebenden Eltern auszufüllen und entscheidet über ganzen oder halben Kinderabzug.
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 9'400 (Kinderabzug je Kind (minderjährig unter elterlicher Sorge/Obhut oder volljährig in beruflicher Erstausbildung, Unterhalt zur Hauptsache): Fr. 9'400. Bei nicht gemeinsam besteuerten Eltern hälftig aufgeteilt (Fr. 4'700), wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge für das Kind abgezogen werden.)** · Bund **CHF 6'800 (Kinderabzug CHF 6'800 pro minderjähriges oder in beruflicher/schulischer Ausbildung stehendes Kind, für dessen Unterhalt die steuerpflichtige Person sorgt; bei getrennter Besteuerung der Eltern hälftig bei gemeinsamer elterlicher Sorge ohne Unterhaltsbeiträge.)**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 9'400 (Volljährige Kinder in beruflicher Erstausbildung, deren Unterhalt zur Hauptsache bestritten wird: gleicher Kinderabzug Fr. 9'400.)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Abzug CHF 6'800 (kein höherer Ausbildungsabzug beim Bund).)**
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0003.md) `zh-form-300-2026-uj__c0003` – «Kinder der Jahrgänge 2009–2026 oder in beruflicher Erstausbildung stehende Kinder»

<a id="s-1-unterst-tzte-personen-personalien"></a>
### Ziff. S. 1 Unterstützte Personen – Erwerbsunfähige oder beschränkt erwerbsfähige unterstützte Personen (im und ausserhalb des Haushalts)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Name, Geburtsjahr, Adresse, Unterstützungsbetrag pro Jahr; Bestätigung der unterstützten Person
- **Regel:** Voraussetzung Unterstützung von mindestens CHF 2'800 (Staatssteuer) bzw. CHF 6'800 (Bundessteuer) pro Jahr. Abzug erfolgt in Ziff. 24.2.
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'800 (Unterstützungsabzug für erwerbsunfähige oder beschränkt erwerbsfähige Personen, an deren Unterhalt mindestens in Höhe des Abzugs beigetragen wird: Fr. 2'800 je Person. Nicht für Ehegatten und Kinder mit Kinderabzug oder Unterhaltsbeitragsabzug.)** · Bund **CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)**
- **Bund:** Mindestunterstützung CHF 6'800 (Abzug 6'800) statt CHF 2'800.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 1](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0003.md) `zh-form-300-2026-uj__c0003` – «Erwerbsunfähige oder beschränkt erwerbsfähige Personen»
  - [WL ZH 2026 UJ S. 20](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0134.md) `zh-wl-2026-uj__c0134` – «des Unterstützungsabzuges von CHF 2’800»

<a id="40-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. 40 – Kapitalleistungen aus AHV/IV, 2. Säule, Freizügigkeitskonto/-police, Säule 3a, Kapitalzahlungen bei Tod oder bleibenden Nachteilen (Code 510)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung (Form. 563) mit Auszahlungsdatum und Betrag
- **Regel:** Sämtliche im Jahr 2026 ausbezahlten Kapitalleistungen mit Auszahlungsdatum angeben; mehrere Leistungen: Aufstellung und Gesamtbetrag. Zu 100% steuerbar, gesondert vom übrigen Einkommen besteuert: Staatssteuer zum Satz einer jährlichen Leistung von einem Zwanzigstel, einfache Staatssteuer mind. 2%. Steuerfrei: bei Stellenwechsel ausbezahlte 2.-Säule-Kapitalleistungen, soweit innert Jahresfrist in eine andere Vorsorgeeinrichtung eingekauft.
- **Bund:** Steuer zu einem Fünftel der Tarife nach Art. 36 Abs. 1 und 2 DBG.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0013.md) `zh-form-300-2026-uj__c0013` – «40. Kapital- aus AHV / IV aus Einrichtung der beruflichen Vorsorge (2. Säule)»
  - [WL ZH 2026 UJ S. 22](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0144.md) `zh-wl-2026-uj__c0144` – «• Kapitalleistungen aus Vorsorge sind zu 100% steuerbar.»
  - [WL ZH 2026 UJ S. 22](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0145.md) `zh-wl-2026-uj__c0145` – «ausgerichtet würde; die einfache Staatssteuer beträgt jedoch mindestens 2%.»
  - [WL ZH 2026 UJ S. 22](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0145.md) `zh-wl-2026-uj__c0145` – «Die Steuer wird zu einem Fünftel der Tarife nach Artikel 36 Abs. 1 und 2 DBG berechnet.»

<a id="50-1-50-2-info-schenkungen-erbschaften"></a>
### Ziff. 50.1 / 50.2 – Schenkungen, Erbvorbezüge, Erbschaften, Beteiligung an Erbengemeinschaften: erhalten (Code 516) / ausgerichtet (Code 519)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Schenkungsvertrag, Erbteilungsvertrag/Erbbescheinigung (Datum, Name, Adresse, Verwandtschaftsgrad, Wert)
- **Regel:** Alle 2026 erhaltenen bzw. ausgerichteten Schenkungen, Erbvorbezüge und Vermögensanfälle von Todes wegen angeben (auch bei noch nicht erfolgter Erbteilung). Besondere Schenkungssteuererklärung nur nötig, wenn nicht Ehegatte/Partner, Nachkommen oder Gelegenheitsgeschenke bis CHF 5'000 je Geschenk.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0014.md) `zh-form-300-2026-uj__c0014` – «50.1 Am T T M M 2026 erhalten von Wert: 516»
  - [WL ZH 2026 UJ S. 23](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0148.md) `zh-wl-2026-uj__c0148` – «bei Gelegenheitsgeschenken, die den Wert von je CHF 5’000 nicht übersteigen.»

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Unselbständige Erwerbstätigkeit – Haupterwerb, Person 1 / Person 2 (Code 100/101)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis (Form. 11) Ziff. 11 Nettolohn/Rente
- **Regel:** Nettolohn gemäss Lohnausweis Ziff. 11 einsetzen (= Bruttolohn Ziff. 8 abzüglich Ziff. 9 und 10); Lohnausweis beilegen. Was im Lohnausweis unter Ziff. 10.1/10.2 (ordentliche PK-Beiträge, PK-Einkauf) bereits abgezogen ist, NICHT nochmals bei Ziff. 16.1 abziehen. Vom Arbeitgeber erhaltene Weiterbildungsvergütungen (LA Ziff. 13.3) sind bei Ziff. 16.2 zu berücksichtigen. LA Feld F (unentgeltliche Beförderung) und Feld G (Kantine/Lunch-Checks) steuern Ziff. 11/Form. 360. LA Ziff. 15 liefert Schichttage und Zusatzangaben. Zeitliche Lücken in der Erwerbstätigkeit ausdrücklich bezeichnen. Je Arbeitgeber eine Zeile (Haupt-/Nebenerwerb abgrenzen). Quellensteuerpflichtige: Bruttolohn/Quellensteuerabzug LA Ziff. 12 beachten.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0004.md) `zh-form-300-2026-uj__c0004` – «1. Einkünfte aus unselbständiger Erwerbstätigkeit»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0028.md) `zh-wl-2026-uj__c0028` – «In der Steuererklärung ist der Nettolohn (d.h. der Lohn nach Abzug von AHV/IV/EO- und»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «dass vom Bruttolohn total (Ziffer 8) das Total der Abzüge (Ziffer 9 und 10) abgezogen wird.»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Unselbständige Erwerbstätigkeit – Nebenerwerb, Person 1 / Person 2 (Code 102/103)

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nebenerwerb); Bescheinigung für VR-Honorare/Behördenentschädigungen
- **Regel:** Sämtliche Einkünfte aus unselbständigen Nebenerwerbstätigkeiten, auch Dienstleistungsentschädigungen, Amtsvergütungen, Verwaltungsrats-/Vorstandshonorare, Tantiemen, Lizenzen (Formularfussnote 1.2/2.2); in ZH keine eigene Zeile für VR-Honorare. Quellensteuerpflichtige Nebeneinkünfte nach BG gegen Schwarzarbeit nicht aufführen, aber Bescheinigung der AHV-Ausgleichskasse beilegen. Berufsauslagen: Form. 360 Ziff. 5 (Nebenerwerb) statt Ziff. 1–4.
- **Quellen:**
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0029.md) `zh-wl-2026-uj__c0029` – «Hier sind sämtliche Einkünfte aus unselbständigen Nebenerwerbstätigkeiten aufzuführen.»
  - [WL ZH 2026 UJ S. 9](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0030.md) `zh-wl-2026-uj__c0030` – «gegen die Schwarzarbeit bezahlt wurden. Der Steuererklärung ist jedoch die Bescheinigung»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit – Haupterwerb, Person 1 / Person 2 (Code 120/121)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsblatt A (Landwirtschaft: Hilfsblatt B oder G): steuerbarer Reingewinn; unterzeichnete Jahresrechnung
- **Regel:** Ergebnis aus Hilfsblatt A (bzw. B/G) übertragen; unterzeichnete Jahresrechnung (Bilanz, Erfolgsrechnung, Anhang) bzw. bei vereinfachter Buchführung Aufstellungen über Aktiven/Passiven und Einnahmen/Ausgaben beilegen. Enthält auch Erträge aus qualifizierten Beteiligungen im Geschäftsvermögen und Liquidationsgewinne (Abzug siehe Ziff. 16.5). Eigenkapital in Ziff. 32.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0004.md) `zh-form-300-2026-uj__c0004` – «2. Einkünfte aus selbständiger Erwerbstätigkeit in Handel, Gewerbe,»
  - [WL ZH 2026 UJ S. 31](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0217.md) `zh-wl-2026-uj__c0217` – «Unterzeichnete Jahresrechnung (Bilanz, Erfolgsrechnung und Anhang) für Steuerpflichtige»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Selbständige Erwerbstätigkeit – Nebenerwerb, Person 1 / Person 2 (Code 122/123)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsblatt bzw. Aufstellung über Nebenerwerb
- **Regel:** Sämtliche Einkünfte aus selbständigen Nebenerwerbstätigkeiten, einschliesslich Gewinne aus Veräusserung von Wertschriften/Liegenschaften, wenn die Tätigkeit über blosse Vermögensverwaltung hinausgeht.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0004.md) `zh-form-300-2026-uj__c0004` – «2.2 Nebenerwerb Person 1 Hilfsblatt 122»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0042.md) `zh-wl-2026-uj__c0042` – «Hier sind sämtliche Einkünfte aus selbständigen Nebenerwerbstätigkeiten anzugeben.»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV-/IV-Renten (100%), Person 1 / Person 2 (Code 130/131)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung AHV/IV (Form. 11 Rentenbescheinigung) Jahresbetrag
- **Regel:** Zu 100% steuerbar. Ankreuzen AHV oder IV. Ergänzungsleistungen, Hilflosenentschädigungen u.ä. sind nicht steuerbar (nicht eintragen).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0005.md) `zh-form-300-2026-uj__c0005` – «3.1 AHV- / IV-Renten (100%) Person 1 AHV IV 130»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0044.md) `zh-wl-2026-uj__c0044` – «Renten und Pensionen [ Ziffer 3.2]»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen 2. Säule, Säule 3a, Arbeitgeber, UVG/Militärversicherung (Betrag/Prozente Code 960–967, Hauptkolonne 134–137)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Rentenbescheinigung (Lohnausweis/Rentenbescheinigung Form. 11) bzw. Bescheinigung der Vorsorgeeinrichtung
- **Regel:** In die Vorkolonne (Betrag, Prozente) Gesamtbetrag und steuerbaren Prozentsatz, in die Hauptkolonne den steuerbaren Teilbetrag. Je Rentenart eine Zeile: PK-Renten grundsätzlich 100% (80% nur bei Rentenbeginn vor 1.1.1987 bzw. 1987–2001 mit altem Vorsorgeverhältnis und mind. 20% Eigenleistung); Arbeitgeberrenten 100%; Renten Säule 3a 100%; SUVA/UVG-Renten 60/80/100% je nach Unfalldatum und Prämientragung; Militärversicherung 100% (Ausnahmen steuerfrei).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0005.md) `zh-form-300-2026-uj__c0005` – «Person 1 960 113211 961 111 134 3213211»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0044.md) `zh-wl-2026-uj__c0044` – «Von Arbeitgebern (also nicht von einer Pensionskasse) ausgerichtete Renten»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0047.md) `zh-wl-2026-uj__c0047` – «Bei nicht zu 100% steuerbaren Renten ist in den Vorkolonnen der Steuererklärung der»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0045.md) `zh-wl-2026-uj__c0045` – «Folgende Leistungen der Militärversicherung sind jedoch steuerfrei»

<a id="3-2-einkommen-vorsorge-uebrige-renten"></a>
### Ziff. 3.2 – Leibrenten und Verpfründung (Ertragsanteil; Code 960–967 / 134–137)

- **Schlüssel:** `einkommen.vorsorge.uebrige_renten` (Übrige Renten (Leibrenten, ausländische Renten, Militär-/Unfallversicherung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Steuerbescheinigung der Versicherungseinrichtung (Ertragsanteil); bei privaten/ausländischen Leibrenten Zahlungsbelege
- **Regel:** Gesamtbetrag in die Vorkolonne «Betrag», steuerbarer Ertragsanteil in die Hauptkolonne; Kolonne «Prozente» leer lassen. Private und ausländische Leibrenten: Ertragsanteil = Rente x ESTV-Berechnungssatz / 100; schweizerische Leibrentenversicherungen: Satz aus der Steuerbescheinigung.
- **Quellen:**
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0046.md) `zh-wl-2026-uj__c0046` – «Berechnungsformel: Erhaltene Leibrente / Verpfründung x Berechnungssatz (in %)»
  - [WL ZH 2026 UJ S. 10](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0047.md) `zh-wl-2026-uj__c0047` – «Kolonne «Prozente» ist leer zu lassen.»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigungen aus Arbeitslosenversicherung, direkt ausbezahlt, Person 1 / Person 2 (Code 140/141)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Arbeitslosenkasse (Taggelder brutto)
- **Regel:** Nur direkt von der Arbeitslosenkasse ausbezahlte Entschädigungen; vom Arbeitgeber ausbezahlte Leistungen stehen bereits im Lohnausweis. Bescheinigung beilegen.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0005.md) `zh-form-300-2026-uj__c0005` – «3.3 Erwerbsausfallentschädigungen aus Arbeitslosenversicherung»
  - [WL ZH 2026 UJ S. 31](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0218.md) `zh-wl-2026-uj__c0218` – «Bescheinigung der Arbeitslosenkasse über erhaltene Taggelder.»

<a id="3-4-einkommen-ersatz-taggelder"></a>
### Ziff. 3.4 – Taggelder aus Kranken-, Unfall-, Invaliden-, Militärversicherung, EO, Mutterschaftsentschädigungen, Person 1 / Person 2 (Code 142/143)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Versicherung/EO-Ausgleichskasse
- **Regel:** Steuerpflichtiges Einkommen, wenn nicht durch den Arbeitgeber im Lohnausweis bescheinigt und mit dem Lohn übertragen. Bescheinigung der Versicherungseinrichtung einholen und beilegen. Nicht steuerbar: Ergänzungsleistungen, Hilflosenentschädigungen u.ä. (siehe separate Zeile).
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0049.md) `zh-wl-2026-uj__c0049` – «Taggelder aus Kranken-, Unfall- und Invalidenversicherung, aus Militärversicherung sowie die»

<a id="3-4-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.4 – Kinder- und Familienzulagen, direkt von der Ausgleichskasse ausbezahlt (Code 142/143)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Familienausgleichskasse (nicht im Lohnausweis enthaltene Zulagen)
- **Regel:** Nur Zulagen eintragen, die nicht über den Arbeitgeber im Lohnausweis (Ziff. 1) enthalten sind, sondern direkt von der Ausgleichskasse ausgerichtet wurden – sonst Doppelerfassung.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0005.md) `zh-form-300-2026-uj__c0005` – «3.4 Kinder- und Familienzulagen, Mutterschaftsentschädigungen, Taggelder»

<a id="3-hinweis-info-steuerfreie-leistungen"></a>
### Ziff. 3 (Hinweis) – Nicht steuerbare Unterstützungsleistungen (Ergänzungsleistungen, Hilflosenentschädigungen, Pflegebeiträge u.ä.) – nur Angabe, nicht einsetzen

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung/Bescheinigung der EL-Stelle
- **Regel:** Nicht in die Einkünfte aufnehmen; Pflegebeiträge, Hilflosenentschädigungen, Ergänzungsleistungen, Beihilfen, Arbeitslosenhilfen und Gemeindezuschüsse für Bezüger von AHV-, IV- und UVG-Leistungen sind nicht steuerbar. Die Renten und Taggelder selbst (AHV/IV, UVG usw.) bleiben steuerbar (Ziff. 3.1–3.4).
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0048.md) `zh-wl-2026-uj__c0048` – «ausgerichtet werden, sind nicht steuerbar.»

<a id="4-1-einkommen-wertschriften"></a>
### Ziff. 4.1 – Ertrag aus Wertschriften, Guthaben und Lotterien (Code 150)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Wertschriften- und Guthabenverzeichnis (Form. 340) Total Bruttoertrag Kolonne A + B; eSteuerauszug der Bank
- **Regel:** Total aus dem Wertschriftenverzeichnis übertragen (Online: Import eSteuerauszug). Erträge brutto, Auslandserträge zum Tageskurs in CHF. Ertrag aus Nutzniessung zu 100%. Vorsorgeguthaben (2. Säule, Säule 3a) nicht aufführen. Gewinne aus nicht steuerfreien Geldspielen/Lotterien ebenfalls hier (Freibeträge siehe separate Zeile).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «4.1 Ertrag aus Wertschriften, Guthaben und Lotterien Wertschriftenverzeichnis 150»
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0050.md) `zh-wl-2026-uj__c0050` – «Ertrag aus Nutzniessung ist zu 100% einzutragen.»

<a id="4-1-einkommen-lotterie-gewinne"></a>
### Ziff. 4.1 – Lotto-, Grossspiel- und Online-Spielbankengewinne (Teil von Code 150)

- **Schlüssel:** `einkommen.lotterie_gewinne` (Lotterie-/Geldspielgewinne (steuerbarer Teil)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Gewinnbescheinigung der Lotteriegesellschaft/Bank; Verrechnungssteuer-Abzugsabschnitt
- **Regel:** Gewinne aus in der Schweiz zugelassenen Grossspielen und Online-Spielbankenspielen sind bis zum Freibetrag steuerfrei (nur der übersteigende Teil steuerbar). Lotteriegewinne mit Verrechnungssteuerabzug im Wertschriftenverzeichnis aufführen, Bescheinigung beilegen. Einsatzkostenabzug: Ziff. 16.5.
- **Limiten:**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'046'400 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen (BGS) steuerfrei bis Fr. 1'046'400 (Freibetrag: nur der übersteigende Anteil ist steuerbar).)** · Bund **CHF 1'071'000 (Einzelne Gewinne aus nach BGS zugelassenen Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'071'000; darüber steuerbar (abzüglich Einsatzkosten nach Art. 33 Abs. 4 DBG).)**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'000 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei, sofern die Grenze von Fr. 1'000 nicht überschritten wird (Freigrenze: bei Überschreitung ist der gesamte Gewinn steuerbar). Gewinne aus Kleinspielen (BGS) sind steuerfrei.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung (Art. 1 Abs. 2 lit. d und e BGS) steuerfrei, sofern die Grenze von CHF 1'100 nicht überschritten wird. Gewinne aus Kleinspielen (BGS) sind steuerfrei.)**
- **Bund:** Freibetrag Grossspielgewinne CHF 1'071'000 (statt CHF 1'046'400); Kleingewinne Verkaufsförderung CHF 1'100 (statt CHF 1'000).
- **Quellen:**
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0164.md) `zh-wl-2026-uj__c0164` – «etc.) und aus Online-Spielbankenspielen sind bis zu einem Betrag von CHF 1’046’400 bei»
  - [WL ZH 2026 UJ S. 26](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0165.md) `zh-wl-2026-uj__c0165` – «CHF 1’000 (Staatssteuer) bzw. CHF 1’100 (Bundessteuer) steuerfrei»

<a id="4-2-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.2 – Davon aus qualifizierten Beteiligungen (Code 151)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Ausschüttungsabrechnung/Dividendenbeleg; Wertschriftenverzeichnis mit Code Q
- **Regel:** Beteiligungen von mindestens 10% (Code «Q» im Wertschriftenverzeichnis): Ausschüttungen ungekürzt (brutto) in Ziff. 4.1 UND als «davon» in Ziff. 4.2 eintragen; der Teilbesteuerungsabzug erfolgt separat unter Ziff. 16.5 gemäss Formular «Qualifizierte Beteiligungen im Privatvermögen».
- **Bund:** Teilbesteuerungsabzug 30% (Privatvermögen) statt 50% bei der Staatssteuer.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «4.2 Davon aus qualifizierten Beteiligungen»
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0162.md) `zh-wl-2026-uj__c0162` – «Sie sind ungekürzt, d.h. mit dem Bruttobetrag der Ausschüttung,»

<a id="5-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.1 – Erhaltene Unterhaltsbeiträge vom geschiedenen/getrennten Ehegatten/Partner (Code 160)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil, Konvention, Zahlungsnachweise; Name/Adresse des Zahlers
- **Regel:** Alimente für den Ehegatten persönlich sind von diesem als Einkommen anzugeben (Name/Adresse des Alimentenzahlers angeben).
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0051.md) `zh-wl-2026-uj__c0051` – «Unterhaltsbeiträge (Alimente), die den geschiedenen, gerichtlich oder tatsächlich getrennt»

<a id="5-2-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.2 – Erhaltene Unterhaltsbeiträge für minderjährige Kinder (Code 161)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Urteil/Konvention, Zahlungsnachweise; Alimentenbevorschussung
- **Regel:** Kinderalimente bis und mit dem Monat der Volljährigkeit (18. Altersjahr) als Einkommen deklarieren; Alimentenbevorschussungen sind gleichgestellt. Ab dem Folgemonat nicht mehr deklarieren. Wirkt auf den Kinderabzug (Ziff. 24.1: ganzer Abzug bei erhaltenen Alimenten und gemeinsamer Sorge).
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0051.md) `zh-wl-2026-uj__c0051` – «dem das Kind das 18. Altersjahr erreicht, als Einkommen in die Steuererklärung einzutragen.»

<a id="5-3-einkommen-uebrige"></a>
### Ziff. 5.3 – Ertrag aus Geschäfts- und Korporationsanteilen (Code 162)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung über Kapital und Ertrag
- **Regel:** Anteilmässig nach Beteiligungsquote deklarieren; Aufstellung über Kapital und Ertrag beilegen. Vermögenswert: Ziff. 30.5.
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0051.md) `zh-wl-2026-uj__c0051` – «Einkünfte aus Geschäfts- und Korporationsanteilen sind von den Inhabern anteilmässig ent-»

<a id="5-4-einkommen-uebrige"></a>
### Ziff. 5.4 – Weitere Einkünfte, nähere Bezeichnung (Code 163)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung/Bescheinigung je Einkunftsart
- **Regel:** Auffangposition für steuerpflichtige Einkünfte, die unter den übrigen Ziffern nicht aufgeführt sind: im Lohnausweis nicht ausgewiesene Trinkgelder, wiederkehrende Zahlungen bei Tod/bleibenden Nachteilen, Bundesbeiträge an Vorbereitungskurse (soweit sie die geltend gemachten Weiterbildungskosten übersteigen), Förderbeiträge für Energiemassnahmen (im Jahr der Auszahlung, soweit nicht direkt mit den Unterhaltskosten verrechnet). Naturalbezüge jeder Art sind steuerpflichtig.
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0052.md) `zh-wl-2026-uj__c0052` – «Hier sind weitere Einkünfte einzutragen, die der Steuerpflicht unterliegen und unter den übrigen»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0197.md) `zh-wl-2026-uj__c0197` – «Förderbeiträge für Energiespar- und Umweltschutzmassnahmen sind im Jahr der Auszahlung»

<a id="5-5-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 5.5 – Kapitalabfindungen für wiederkehrende Leistungen (Code 164)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung des Leistungserbringers; Anzahl Monate
- **Regel:** Für die Satzbestimmung den Betrag einsetzen, der der jährlichen Leistung entspricht (Anzahl Monate angeben). Kapitalleistungen aus Vorsorge gehören NICHT hierher, sondern auf Seite 4 Ziff. 40.
- **Quellen:**
  - [WL ZH 2026 UJ S. 11](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0053.md) `zh-wl-2026-uj__c0053` – «Diese werden bei der Ermittlung des Steuersatzes zu dem Betrag eingesetzt, welcher der jährlichen Leistung entspricht.»

<a id="6-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. 6 – Nettoertrag aus Liegenschaften – Eigenmietwert selbstbewohnter Liegenschaften (Code 188)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftenverzeichnis (Form. 350) Rückseite: Eigenmietwert/Miet- und Pachtzinseinnahmen; Liegenschaftenbewertung der Gemeinde
- **Regel:** Nettoertrag (Eigenmietwert bzw. Mieteinnahmen abzüglich Unterhalt/Verwaltung) aus Form. 350 Code 3953 übertragen. Liegenschaften bis und mit Baujahr 2025: weiterhin Eigenmietwert nach Weisung 2009 (ohne Erhöhung); Neubauten ab 2026: Weisung 2026 mit pauschalem Abzug von 10%. Selbstgenutzte Wohnung im MFH/Geschäftshaus (ohne STWE): 70% des erzielbaren Mietzinses. Wohnrecht/Nutzniessung: Eigenmietwert beim Berechtigten.
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **10 % (Eigenmietwert: Für Liegenschaften bis und mit Baujahr 2025 gelten weiterhin die Eigenmietwerte nach Weisung 2009 (ohne Erhöhung); für Neubauten ab 2026 gilt die Weisung 2026 mit einem pauschalen Abzug von 10 % zum Ausgleich der höheren Eigenmietwerte. Selbstgenutzte Wohnungen in Mehrfamilien-/Geschäftshäusern: 70 % des erzielbaren Mietzinses. Gesetzliche Leitlinie: Eigenmietwert max. 70 % des Marktwerts.)** · Bund **n/a – Bund: kein prozentualer Einschlag/Abzug auf dem Eigenmietwert; Festsetzung nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG), kantonale Eigenmietwert-Bewertung. Ein im kantonalen Veranlagungsverfahren vorgesehener Abzug für die DBSt (z.B. TG: 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «6. Nettoertrag aus Liegenschaften Liegenschaftenverzeichnis 188»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0181.md) `zh-wl-2026-uj__c0181` – «gelten für Zürcher Liegenschaften bis und mit Baujahr 2025 deshalb weiterhin die bisherigen»
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0182.md) `zh-wl-2026-uj__c0182` – «Abzug von 10% vorgenommen»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0178.md) `zh-wl-2026-uj__c0178` – «(ohne Stockwerkeigentum) sind 70% des Mietzinses einzusetzen, der bei»

<a id="6-h-rtefall-unternutzung-sozialabzug-eigenmietwert"></a>
### Ziff. 6 (Härtefall/Unternutzung) – Einschlag auf dem Eigenmietwert (Unternutzung; Härtefalleinschlag auf Antrag)

- **Schlüssel:** `sozialabzug.eigenmietwert` (Einschlag/Abzug auf dem Eigenmietwert (kantonal)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Antrag/Begründung bei der Gemeinde bzw. im Liegenschaftenverzeichnis
- **Regel:** Unternutzung: In Ausnahmefällen angemessener Einschlag bei verminderten Wohnbedürfnis (z.B. Wegzug der Kinder; keine Unternutzung bei 4–6 Zimmern und 2 Personen). Härtefall: § 21 Abs. 2 lit. d StG (Nachtrag 132, Stand 1.4.2026) sieht auf Antrag eine angemessene Herabsetzung bei übermässiger Belastung vor; die WL 2026 UJ liess offen, ob die zugehörige Weisung bereits per 1.1.2026 gilt – Anwendung (ZStB 21.3) im Einzelfall prüfen.
- **Bemerkung:** Inkrafttreten des Härtefalleinschlags (Weisung) in der WL 2026 UJ offen; StG-Fassung Stand 1.4.2026 enthält § 21 Abs. 2 lit. d.
- **Quellen:**
  - [WL ZH 2026 UJ S. 28](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0186.md) `zh-wl-2026-uj__c0186` – «Auf dem Eigenmietwert kann in Ausnahmefällen ein angemessener Einschlag gewährt wer-»
  - [StG ZH § 21](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-21-t2.md) `zh-stg-2026__par-21-t2` – «ist der Eigenmietwert auf Antrag angemessen herabzusetzen»
  - [WL ZH 2026 UJ S. 8](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0023.md) `zh-wl-2026-uj__c0023` – «die (Wieder-)Einführung eines Härtefalleinschlags auf dem Eigenmietwert beschlossen.»

<a id="6-einkommen-liegenschaften-mietertrag"></a>
### Ziff. 6 – Nettoertrag aus Liegenschaften – Miet- und Pachtzinserträge vermieteter Liegenschaften (Code 188)

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Liegenschaftenverzeichnis (Form. 350) Rückseite; Mieterspiegel oder Verwaltungsabrechnung
- **Regel:** Steuerbar sind sämtliche Miet- und Pachtzinseinnahmen (inkl. Garagen, Abstellplätze, gewerbliche Räume, Reklame) ohne Entschädigungen der Mieter für Heizung, Warmwasser, Treppenhausreinigung, soweit diese die tatsächlichen Aufwendungen nicht übersteigen. Je Liegenschaft Ertragsaufstellung (Mieterspiegel) beilegen; liegt keine vor: Beiblatt zum Liegenschaftenverzeichnis.
- **Quellen:**
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0176.md) `zh-wl-2026-uj__c0176` – «Steuerbar sind sämtliche Miet- und Pachtzinseinnahmen (inkl. Einnahmen z.B. für Gara»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0179.md) `zh-wl-2026-uj__c0179` – «Für jede Liegenschaft ist eine Ertragsaufstellung (Mieterspiegel) mit folgenden Angaben beizulegen:»

<a id="6-abzug-liegenschaft-unterhalt"></a>
### Ziff. 6 – Nettoertrag aus Liegenschaften – Unterhalts- und Verwaltungskosten (Pauschale oder effektiv; im Netto-Code 188 enthalten)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Rechnungen/Verwaltungsabrechnung, Gebäudeversicherungsprämien; Beiblatt zum Liegenschaftenverzeichnis
- **Regel:** Pro Liegenschaft Wahlrecht Pauschale oder effektive Kosten. Pauschale (Staatssteuer) 20% des deklarierten Bruttomietertrags (bei vermieteten Liegenschaften abzüglich Heizungs-/Warmwasser-/Treppenhausentschädigungen); kein Pauschalabzug bei vorwiegend geschäftlicher Nutzung; bei Pauschale keine weiteren Abzüge (ausser Baurechtszinsen). Effektiv: detaillierte Aufstellung (Datum, Art, Empfänger, Betrag) beilegen. Baurechtszinsen zusätzlich abziehbar (Aufstellung beilegen).
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

<a id="6-abzug-liegenschaft-energie-umwelt"></a>
### Ziff. 6 – Nettoertrag aus Liegenschaften – Energiespar-/Umweltschutzinvestitionen und Rückbaukosten (im Netto-Code 188 enthalten)

- **Schlüssel:** `abzug.liegenschaft.energie_umwelt` (Investitionen Energiesparen/Umweltschutz, Rückbaukosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Rechnungen Investitionen; Beiblatt/Aufstellung; Subventionsbescheide
- **Regel:** Den Unterhaltskosten gleichgestellt, soweit nicht subventioniert (ZStB 30.4); Rückbaukosten für Ersatzneubau abziehbar; nicht berücksichtigte Beträge können auf die zwei Folgeperioden übertragen werden. Erhaltene Förderbeiträge: Ziff. 5.4, soweit nicht direkt mit den Kosten verrechnet.
- **Quellen:**
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0193.md) `zh-wl-2026-uj__c0193` – «Den abzugsfähigen Unterhaltskosten gleichgestellt sind Aufwendungen für Massnahmen, wel-»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0194.md) `zh-wl-2026-uj__c0194` – «abzugsfähig sind Rückbaukosten für einen Ersatzneubau.»

<a id="7-berechnung-total"></a>
### Ziff. 7 – Total der Einkünfte, Übertrag auf Seite 3 Ziff. 19 (Code 199)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Summe Ziff. 1–6
- **Regel:** Rechenzeile; Staatssteuer- und Bundessteuer-Spalte getrennt führen.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 2](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0006.md) `zh-form-300-2026-uj__c0006` – «7. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 19 199»

## Abzüge

<a id="11-1-11-2-berechnung-total"></a>
### Ziff. 11.1 / 11.2 – Berufsauslagen bei unselbständiger Erwerbstätigkeit, Person 1 (Code 220) / Person 2 (Code 240)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Formular Berufsauslagen (Form. 360) Ziff. 6 Total Berufsauslagen, je Person
- **Regel:** Total des Hilfsblatts Berufsauslagen übertragen (Staats- und Bundessteuer-Spalte). Pro Person ein Hilfsblatt, vollständig und genau ausgefüllt beilegen. Pauschalen oder effektive Kosten siehe Zeilen Form. 360 Ziff. 1–5.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0007.md) `zh-form-300-2026-uj__c0007` – «11. Berufsauslagen bei unselbständiger Erwerbstätigkeit»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0057.md) `zh-wl-2026-uj__c0057` – «6. Total der Berufsauslagen 220»

<a id="12-abzug-schuldzinsen"></a>
### Ziff. 12 – Schuldzinsen (soweit nicht schon unter Ziff. 2 abgezogen) (Code 250)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen) → Schuldenverzeichnis (Form. 355) Total private Schuldzinsen (Code 3201); Zinsausweis Bank per 31.12.
- **Regel:** Private Schuldzinsen abziehbar bis zum Bruttoertrag aus beweglichem und unbeweglichem Privatvermögen (inkl. Eigenmietwert) plus CHF 50'000. Nicht abziehbar: Amortisationen und Leasingraten (inkl. Zinsanteil). Baurechtszinsen gehören zu den Liegenschaftsunterhaltskosten (Ziff. 6), nicht hierher. Schuldzinsen aus selbständiger Erwerbstätigkeit bereits in Ziff. 2.
- **Bund:** Gleiche Regel (Bruttoertrag plus CHF 50'000).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0007.md) `zh-form-300-2026-uj__c0007` – «12. Schuldzinsen (soweit nicht schon unter Ziff. 2 abgezogen) Schuldenverzeichnis 250»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0069.md) `zh-wl-2026-uj__c0069` – «mögen (inkl. Eigenmietwert) und weiterer CHF 50’000 nicht übersteigen.»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0068.md) `zh-wl-2026-uj__c0068` – «abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den»

<a id="13-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 13.1 – Unterhaltsbeiträge an den geschiedenen oder getrennt lebenden Ehegatten/Partner (Code 254)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungsurteil/Konvention; Zahlungsnachweise
- **Regel:** Für den Ehegatten persönlich bestimmte Unterhaltsbeiträge voll abziehbar; Zahlungsnachweis beilegen. Spiegelbild zu Ziff. 5.1 beim Empfänger. Nicht für Leistungen in Erfüllung anderer familienrechtlicher Pflichten.
- **Bund:** Gleiche Regel (DBG).
- **Quellen:**
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0070.md) `zh-wl-2026-uj__c0070` – «Ehegatten persönlich bestimmt sind, können voll abgezogen werden.»

<a id="13-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 13.2 – Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit) (Code 255)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Urteil/Konvention; Zahlungsnachweise
- **Regel:** Kinderalimente abziehbar bis und mit dem Monat, in dem das Kind 18 wird. Danach kein Alimentenabzug – stattdessen steht dem Zahlenden der Kinderabzug zu (Ziff. 24.1). Wer Alimente abzieht, hat keinen (ganzen/halben) Kinderabzug für dasselbe Kind (siehe Ziff. 24.1).
- **Quellen:**
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0070.md) `zh-wl-2026-uj__c0070` – «Für Kinder bestimmte Unterhaltsbeiträge (Alimente) können bis und mit dem Monat abgezogen werden, in dem das Kind das 18. Altersjahr erreicht.»

<a id="13-3-abzug-uebrige"></a>
### Ziff. 13.3 – Rentenleistungen – abzugsfähig: Ertragsanteil (Code 256, Vorkolonne 2561)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ⚠️ strittig
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Zahlungsnachweise/Vertrag; erstmals Kopie Leibrenten-/Verpfründungsvertrag
- **Regel:** Abzugsfähig laut Wegleitung der Ertragsanteil der bezahlten Leibrenten/Verpfründungen (ESTV-Berechnungssatz). Zahlungsnachweise und bei erstmaliger Deklaration Vertragskopie beilegen.
- **Bemerkung:** Gesetz (§ 31 Abs. 1 lit. b StG, Stand 2026): 40 Prozent der bezahlten Leibrenten; Wegleitung: Ertragsanteil nach jährlichem ESTV-Satz. Je nach Satz weichen die Werte ab; Gesetz geht vor, Fachperson entscheidet.
- **Quellen:**
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0071.md) `zh-wl-2026-uj__c0071` – «Abzugsfähig ist der Ertragsanteil der bezahlten Leibrenten und Verpfründungen.»
  - [StG ZH § 31](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-31-t1.md) `zh-stg-2026__par-31-t1` – «die dauernden Lasten sowie 40 Prozent der bezahlten Leibrenten»

<a id="14-1-14-2-abzug-vorsorge-saeule3a"></a>
### Ziff. 14.1 / 14.2 – Beiträge Säule 3a – ordentliche Beiträge, Person 1 (Code 260, effektiv 262) / Person 2 (Code 261, effektiv 263)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → 3a-Bescheinigung der Bank-/Versicherungsstiftung (im Steuerjahr 2026 einbezahlter Betrag)
- **Regel:** Nur im Jahr 2026 tatsächlich bezahlte Beiträge abziehbar, Bescheinigung beilegen. Maximum mit 2. Säule CHF 7'258; ohne 2. Säule 20% des Erwerbseinkommens, max. CHF 36'288. Beide Ehegatten können je für sich abziehen, wenn beide erwerbstätig sind und je einen Vorsorgevertrag haben. Mitarbeit im Betrieb des Ehegatten: nur bei echtem Arbeitsverhältnis mit AHV-Abrechnung. 3a-Guthaben nicht im Wertschriftenverzeichnis/Vermögen aufführen.
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a mit Zugehörigkeit zur 2. Säule: höchstens Fr. 7'258 (Bemessungsjahr ab 2025).)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug CHF 7'258 pro Jahr für Personen, die einer Vorsorgeeinrichtung der 2. Säule angehören (8 % des oberen Grenzbetrags nach Art. 8 Abs. 1 BVG). Nur im Steuerjahr tatsächlich einbezahlte Beiträge, mit Bescheinigung.)**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a ohne Zugehörigkeit zur 2. Säule: höchstens 20 % des Erwerbseinkommens, maximal Fr. 36'288.)** · Bund **CHF 36'288 (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens CHF 36'288 pro Jahr.)**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. Fr. 36'288).)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (alle Einkünfte aus selbständiger und unselbständiger, haupt- und nebenberuflicher Erwerbstätigkeit), max. CHF 36'288.)**
- **Bund:** Gleiche Höchstbeträge (CHF 7'258 / 20%, max. CHF 36'288) gemäss Formular (Spalte Bund).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «14.1 Person 1 13211 eff. CHF 262 260»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0075.md) `zh-wl-2026-uj__c0075` – «die einer Einrichtung der beruflichen Vorsorge (2. Säule) angehören, höchstens CHF 7’258;»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0076.md) `zh-wl-2026-uj__c0076` – «Es dürfen nur die tatsächlich im Jahr 2026 bezahlten Prämien/Beiträge oder Einlagen ab-»

<a id="14-3-abzug-vorsorge-saeule3a-einkauf"></a>
### Ziff. 14.3 – Einkauf Säule 3a (neu ab 2026), Person 1 (Code 276) / Person 2 (Code 278), Hauptkolonne Code 264

- **Schlüssel:** `abzug.vorsorge.saeule3a_einkauf` (Einkauf (Nachzahlung) Säule 3a – ab Steuerjahr 2026) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Einkaufsbescheinigung der 3a-Einrichtung (Einkaufsbetrag, Beitragslücken); Nachweis AHV-Beitragsjahre
- **Regel:** Neu ab Steuerperiode 2026: zusätzlich zu den ordentlichen Beiträgen Einkauf für Beitragslücken, die ab 1.1.2025 entstanden sind. Voraussetzungen: in den Lücken-Jahren AHV/IV/EO-Beiträge geleistet (3a-berechtigt) und im Einkaufsjahr den maximal zulässigen ordentlichen Beitrag (CHF 7'258 bzw. 20%, max. CHF 36'288) vollständig einbezahlt. Einkauf höchstens Summe der Beitragslücken der letzten 10 Jahre (frühestens ab 1.1.2025), maximal CHF 7'258.
- **Limiten:**
  - Säule 3a – Einkauf (Nachzahlung) Regel/Maximum: Kanton **CHF 7'258 (Neu ab Steuerperiode 2026: Einkauf in die Säule 3a für Beitragslücken, die ab 1.1.2025 entstanden sind (innerhalb der zehn Jahre vor dem Einkauf). Voraussetzungen: AHV/IV/EO-Beiträge in den Lückenjahren und im Einkaufsjahr voller ordentlicher Maximalbeitrag einbezahlt. Einkauf höchstens Summe der Lücken, in jedem Fall maximal Fr. 7'258.)** · Bund **CHF 7'258 (Einkauf Säule 3a (ab Steuerperiode 2026, für Beitragslücken ab 1.1.2025): zusätzlich zum vollen ordentlichen Beitrag im Einkaufsjahr; max. Summe der Beitragslücken der letzten 10 Jahre (frühestens ab 2025), pro Steuerjahr höchstens CHF 7'258 (8 % des oberen BVG-Grenzbetrags, unabhängig von Zugehörigkeit zur 2. Säule); eine Jahresbeitragslücke nur durch einen einzigen Einkauf ausgleichbar; kein Einkauf nach Bezug einer Altersleistung der Säule 3a (Bezüge ab 5 Jahren vor Referenzalter zählen als Altersleistung).)**
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «14.3 Einkauf Person 1 276 3211 Person 2 278 3211 264»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0077.md) `zh-wl-2026-uj__c0077` – «in jedem Fall aber maximal CHF 7’258.»
  - [WL ZH 2026 UJ S. 8](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0020.md) `zh-wl-2026-uj__c0020` – «auch Einkäufe getätigt werden für Beitragslücken, die ab dem 1.1.2025 entstanden sind»

<a id="15-abzug-versicherungspraemien"></a>
### Ziff. 15 – Versicherungsprämien, Zinsen von Sparkapitalien (Code 270)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Prämienrechnung/-bescheinigung Krankenkasse (abzüglich Prämienverbilligung), Police Lebens-/Unfallversicherung, Sparzinsen aus Wertschriftenverzeichnis
- **Regel:** Betrag aus dem Formular Versicherungsprämien (Form. 365) Teil C übertragen: der niedrigere der Beträge A (bezahlte Prämien und Sparzinsen, netto nach Prämienverbilligung) und B (Maximalabzug). Maximalabzug Staatssteuer: Verheiratete CHF 5'800 (ohne Beiträge 2. Säule/3a: CHF 8'700), übrige CHF 2'900 (ohne Vorsorgebeiträge: CHF 4'350), zusätzlich pro Kind/unterstützungsbedürftige Person CHF 1'300 (halber Kinderabzug: CHF 650).
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

<a id="16-1-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 16.1 – Beiträge an die AHV, IV und 2. Säule, sofern nicht unter Ziff. 1 und 2 abgezogen (Code 280)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) für selbst einbezahlte Einkäufe; NICHT Lohnausweis Ziff. 10.2
- **Regel:** Nur Beiträge/Einkäufe eintragen, die nicht schon im Lohnausweis vom Lohn abgezogen sind. Lohnausweis Ziff. 10.2 (Einkauf, im Bruttolohn abgezogen) ist im Nettolohn Ziff. 11 bereits berücksichtigt – nicht nochmals abziehen. Selbst entrichtete (nicht vom Lohn abgezogene) Einkäufe bescheinigt die Vorsorgeeinrichtung separat mit Formular 21 EDP; Bescheinigung beilegen. Einkäufe sind nicht abziehbar, wenn innerhalb von drei Jahren ein Kapitalbezug erfolgt (Sperrfrist). Bei Zweiverdienerabzug sind Einkäufe in die 2. Säule vom Erwerbseinkommen abzuziehen (Ziff. 17).
- **Quellen:**
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0088.md) `zh-wl-2026-uj__c0088` – «Einkäufe steuerlich nicht zum Abzug zugelassen werden, soweit innerhalb von drei Jahren ein Kapitalbezug erfolgt.»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «die berufliche Vorsorge, sind nicht durch den Arbeitgeber im Lohnausweis, sondern durch die Vorsorgeeinrichtung separat mit dem Formular 21 EDP zu bescheinigen.»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «Beiträge für den Einkauf von fehlenden Versicherungsjahren oder von fehlendem Spar-»

<a id="16-1-abzug-ahv-nichterwerbstaetige"></a>
### Ziff. 16.1 – AHV/IV-Beiträge, soweit nicht im Lohnausweis gekürzt (z.B. Nichterwerbstätige) (Code 280)

- **Schlüssel:** `abzug.ahv_nichterwerbstaetige` (AHV/IV/EO-Beiträge Nichterwerbstätiger u.ä.) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse) → Beitragsverfügung/Bescheinigung der AHV-Ausgleichskasse
- **Regel:** Beiträge an AHV und IV abziehbar, soweit die unter Ziff. 1 und 2 deklarierten Einkünfte nicht bereits um diese Beiträge gekürzt sind (Lohnausweis Ziff. 9 ist im Nettolohn bereits abgezogen). Bescheinigung beilegen.
- **Quellen:**
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0088.md) `zh-wl-2026-uj__c0088` – «• Beiträge an die AHV und IV, soweit die unter Ziffern 1 und 2 der Steuererklärung deklarierten»

<a id="16-2-abzug-weiterbildung"></a>
### Ziff. 16.2 – Berufsorientierte Aus- und Weiterbildungskosten (Code 292)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Kursrechnungen/Zahlungsnachweise; Lohnausweis Ziff. 13.3 (Beiträge des Arbeitgebers); Formular Aus- und Weiterbildungskosten (Form. 367)
- **Regel:** Selbst getragene Kosten (nach Abzug von Beiträgen Dritter: Arbeitgeber, Bund, Branchenverbände) bis zum Maximalbetrag; Voraussetzung: Abschluss Sekundarstufe II oder 20. Altersjahr vollendet und nicht Ausbildungskosten bis zum ersten Abschluss Sek. II. Zeitpunkt = Fälligkeit/Zahlung, nicht Kursbesuch. Lohnausweis Ziff. 13.3: vom Arbeitgeber dem Arbeitnehmer vergütete Weiterbildungskosten (nicht direkt an Dritte bezahlte) sind in Form. 367 als Beitrag Dritter in Abzug zu bringen; bei Rechnungen auf den Namen des Arbeitnehmers immer bescheinigt. Vollständig ausgefülltes Formular beilegen.
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 12'600 (Berufsorientierte Aus- und Weiterbildungskosten inkl. Umschulung: bis Fr. 12'600 (Staatssteuer), sofern erster Abschluss Sekundarstufe II vorliegt oder das 20. Lebensjahr vollendet ist (und es nicht um Kosten bis zum ersten Abschluss Sek. II geht).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildungs- inkl. Umschulungskosten bis CHF 13'000 pro Jahr, sofern erster Abschluss Sek. II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)**
- **Bund:** Höchstbetrag CHF 13'000 (statt CHF 12'600).
- **Quellen:**
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0089.md) `zh-wl-2026-uj__c0089` – «betrag von CHF 12’600 bei der Staatssteuer bzw. CHF 13’000 bei der Bundessteuer, sofern ein»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «die dem Arbeitnehmer vergütet werden. Nicht anzugeben sind Vergütungen, die direkt an Dritte (z. B. Bildungsinstitut) bezahlt werden.»

<a id="16-3-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. 16.3 – Kosten für die Verwaltung des beweglichen Privatvermögens (Code 283)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Depotgebühren-Ausweis der Bank / Verwaltungsabrechnung (Verwahrung und Verwaltung durch Dritte)
- **Regel:** Abziehbar sind Kosten der Verwaltung und Verwahrung durch Dritte sowie nicht rückforderbare/anrechenbare ausländische Quellensteuern; nicht abziehbar Erwerbs-/Veräusserungskosten und Aufwendungen für Anschaffung/Wertvermehrung. Bei Verwaltung durch Dritte pauschal 3 Promille des Steuerwerts der verwalteten Wertschriften, maximal CHF 6'000, oder effektiv (Bezahlung und Abzugsfähigkeit voll nachweisen).
- **Quellen:**
  - [WL ZH 2026 UJ S. 15–16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0091.md) `zh-wl-2026-uj__c0091` – «können 3‰ des Steuerwerts dieser durch Dritte verwalteten Wertschriften, maximal»
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0090.md) `zh-wl-2026-uj__c0090` – «Bei beweglichem Privatvermögen können die Kosten der Verwaltung durch Dritte und die weder»

<a id="16-4-abzug-behinderungskosten"></a>
### Ziff. 16.4 – Behinderungsbedingte Kosten (Code 3160)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Aufstellung über behinderungsbedingte Kosten (Codes 3100–3103, 3120, 3130–3133, 3150, 3155); Rechnungen
- **Regel:** Formular «Aufstellung über behinderungsbedingte Kosten» (Gemeindesteueramt / zh.ch) ausfüllen: A effektive Aufwendungen, B Vergütungen Dritter (Krankenkasse, Hilflosenentschädigung, Anteil Lebenshaltungskosten), C = A – B (Code 3155) oder D Pauschale gemäss Merkblatt ZStB 32.1; Übertrag in Ziff. 16.4. Nur selbst getragene Kosten; nicht gleichzeitig unter Ziff. 22.1.
- **Quellen:**
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0093.md) `zh-wl-2026-uj__c0093` – «Wenn Sie einen solchen Abzug beanspruchen, füllen Sie das Formular «Aufstellung über»
  - [StG ZH § 31](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-31-t3.md) `zh-stg-2026__par-31-t3` – «soweit der Steuerpflichtige die Kosten selber trägt»

<a id="16-5-parteien-abzug-parteispenden"></a>
### Ziff. 16.5 (Parteien) – Weitere Abzüge – Mitgliederbeiträge und Zuwendungen an politische Parteien (Code 284)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Spendenbestätigung/Beitragsquittung der Partei; Aufstellung
- **Regel:** Nur Parteien, die im Parteienregister eingetragen, in einem kantonalen Parlament vertreten sind oder bei den letzten Wahlen mind. 3% Wähleranteil erreicht haben. Staatssteuer max. CHF 21'000 für in ungetrennter Ehe Lebende, CHF 10'500 für übrige; Bundessteuer max. CHF 10'600 (gilt für Ehepaare wie Übrige).
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'500 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister, Vertretung im kantonalen Parlament oder mind. 3 % Wähleranteil): bis Fr. 10'500 für die übrigen Steuerpflichtigen.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien (Parteienregister / kantonales Parlament / mind. 3 % Stimmen): bis Gesamtbetrag CHF 10'600.)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 21'000 (Parteispenden gemeinsam Besteuerte (in ungetrennter Ehe): bis Fr. 21'000.)** · Bund **–**
- **Bund:** Höchstbetrag CHF 10'600 (für Verheiratete und Übrige gleich).
- **Quellen:**
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0097.md) `zh-wl-2026-uj__c0097` – «Höchstbetrag von CHF 21’000 für in ungetrennter Ehe lebende Steuerpflichtige und von»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0098.md) `zh-wl-2026-uj__c0098` – «Der Höchstbetrag für solche Abzüge beträgt CHF 10’600.»

<a id="16-5-teilbesteuerung-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 16.5 (Teilbesteuerung) – Weitere Abzüge – Teilbesteuerungsabzug qualifizierte Beteiligungen (Code 284, Aufstellung)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Formular «Qualifizierte Beteiligungen im Privatvermögen» bzw. «…im Geschäftsvermögen»
- **Regel:** Nicht steuerbarer Teil der Erträge aus qualifizierten Beteiligungen (mind. 10%); die Bruttoerträge stehen in Ziff. 4.1/4.2 bzw. 2.1. Staatssteuer: 50% (Privatvermögen und – nach Abzug des zurechenbaren Aufwands – Geschäftsvermögen); Bundessteuer: 30%.
- **Bund:** Teilbesteuerung 30% (statt 50% bei der Staatssteuer).
- **Quellen:**
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0100.md) `zh-wl-2026-uj__c0100` – «für qualifizierte Beteiligungen im Privatvermögen beträgt 50%,»
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0100.md) `zh-wl-2026-uj__c0100` – «qualifizierte Beteiligungen im Privatvermögen beträgt 30%,»

<a id="16-5-brige-abzug-uebrige"></a>
### Ziff. 16.5 (übrige) – Weitere Abzüge – Liquidationsgewinne, Geldspiel-Einsatzkosten u.a. (Code 284)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn), Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsformular «Liquidationsgewinn bei Aufgabe der selbständigen Erwerbstätigkeit»; Aufstellung Einsatzkosten
- **Regel:** Liquidationsgewinne (stille Reserven der letzten zwei Geschäftsjahre bei definitiver Aufgabe nach dem 55. Altersjahr oder wegen Invalidität) werden separat besteuert und von den Einkünften Ziff. 2.1/2.2 abgezogen; Hilfsformular einreichen. Geldspielgewinne (nicht steuerfrei): Einsatzkosten 5% des Gewinns, höchstens CHF 5'200 (Staatssteuer) bzw. CHF 5'400 (Bundessteuer). Weitere Fälle: Patentbox/F&E (Hilfsblatt STAF).
- **Bund:** Geldspiel-Einsatzkosten max. CHF 5'400 (statt CHF 5'200).
- **Quellen:**
  - [WL ZH 2026 UJ S. 16](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0099.md) `zh-wl-2026-uj__c0099` – «stille Reserven (Liquidationsgewinne), die in den letzten zwei Geschäftsjahren realisiert worden»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0102.md) `zh-wl-2026-uj__c0102` – «tens CHF 5’200 (Staatssteuer) bzw. CHF 5’400 (Bundessteuer), als Einsatzkosten abgezogen»

<a id="16-6-abzug-drittbetreuung"></a>
### Ziff. 16.6 – Abzug für fremdbetreute Kinder (Jahrg. 2012–2026) (Code 376)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Rechnungen Kita/Tagesfamilie/Hort (Aufstellung über Fremdbetreuungskosten) mit Zahlungsnachweis
- **Regel:** Nachgewiesene Kosten, höchstens CHF 25'300 (Staatssteuer) bzw. CHF 25'800 (Bundessteuer) pro Kind. Voraussetzungen: Kind hat das 14. Altersjahr noch nicht vollendet, lebt im gleichen Haushalt wie die steuerpflichtige Person, die für seinen Unterhalt sorgt, und die Kosten stehen in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit. Konkubinat mit gemeinsamer Sorge und Eltern mit alternierender Obhut: je halber Abzug (CHF 12'650 / 12'900 pro Kind), andere Aufteilung nachzuweisen.
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 25'300 (Kinderdrittbetreuungskosten: nachgewiesene Kosten, höchstens Fr. 25'300 pro Kind (Staatssteuer); bei Konkubinat/alternierender Obhut mit gemeinsamer Sorge je halber Abzug (Fr. 12'650).)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind, höchstens CHF 25'800; Kind unter 14 Jahren im gleichen Haushalt; Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 (Kind hat das 14. Altersjahr noch nicht vollendet, lebt im gleichen Haushalt wie die für den Unterhalt sorgende Person; Kosten im direkten kausalen Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat.)**
- **Bund:** Höchstbetrag CHF 25'800 (statt CHF 25'300); halber Abzug CHF 12'900.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «16.6 Abzug für fremdbetreute Kinder (Jahrg. 2012–2026) max. 25’300 / 25’800 376»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0105.md) `zh-wl-2026-uj__c0105` – «Kinderdrittbetreuungskosten: Der Abzug beträgt höchstens CHF 25’300 (Staatssteuer) bzw.»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0107.md) `zh-wl-2026-uj__c0107` – «Der halbe Abzug beträgt je höchstens CHF 12’650 (Staatssteuer) bzw. CHF 12’900»

<a id="17-abzug-zweiverdiener"></a>
### Ziff. 17 – Sonderabzug bei Erwerbstätigkeit beider Ehegatten/Partner (Zweiverdienerabzug) (Code 290)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Berechnung aus den Erwerbseinkommen beider Ehegatten (Ziff. 1–2 abzüglich zugehöriger Berufsauslagen, 3a-Beiträge, PK-Einkäufe, nicht im Lohnausweis berücksichtigte AHV-/PK-Beiträge)
- **Regel:** Nur einmal beanspruchbar, nur bei rechtlich und tatsächlich ungetrennter Ehe und Erwerbstätigkeit beider. Massgebend ist das verbleibende niedrigere Erwerbseinkommen. Staatssteuer: max. CHF 6'200 (bei niedrigerem Erwerbseinkommen nur dieser Betrag). Bei erheblicher Mitarbeit im Geschäft des anderen Ehegatten wird vom gemeinsamen verbleibenden Erwerbseinkommen abgezogen (Bund: je hälftig aufteilen).
- **Limiten:**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **CHF 6'200 (Zweiverdienerabzug (Ehegatten in ungetrennter Ehe, unabhängig erzielte Erwerbseinkommen oder erhebliche Mitarbeit im Geschäft des Ehegatten): Fr. 6'200, begrenzt auf das niedrigere Erwerbseinkommen.)** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum.)**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **n/a** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum.)**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **n/a** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (Ehepaare in ungetrennter Ehe, beide erwerbstätig).)**
- **Bund:** Bundessteuer: 50% des niedrigeren Erwerbseinkommens, mind. CHF 8'600 und max. CHF 14'100; bei weniger als CHF 8'600 Abzug in Höhe des niedrigeren Erwerbseinkommens.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «17. Sonderabzug bei Erwerbstätigkeit beider Ehegatten/Partn.»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0109.md) `zh-wl-2026-uj__c0109` – «Der Abzug beträgt max. CHF 6’200 und steht wie folgt zu:»
  - [WL ZH 2026 UJ S. 17](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0110.md) `zh-wl-2026-uj__c0110` – «jedoch mind. CHF 8’600 und max. CHF 14’100;»

<a id="18-berechnung-total"></a>
### Ziff. 18 – Total der Abzüge, zu übertragen in Ziffer 20 (Code 299)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Summe Ziff. 11–17
- **Regel:** Rechenzeile; Staats- und Bundessteuer-Spalte getrennt.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md) `zh-form-300-2026-uj__c0008` – «18. Total der Abzüge, zu übertragen in Ziffer 20 299»

## Hilfsblatt Berufskosten

<a id="form-360-ziff-1-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1.1 – Fahrkosten – Abonnementskosten öffentliche Verkehrsmittel (Code 201)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → ÖV-Abonnement (Rechnung/Beleg); Lohnausweis Feld F
- **Regel:** Notwendige Abonnementskosten bei ständiger Benützung öffentlicher Verkehrsmittel (Bahn, Schiff, Tram, Bus). Lohnausweis Feld F (unentgeltliche Beförderung Wohn-/Arbeitsort) angekreuzt = dem Arbeitnehmer erwachsen keine Arbeitswegkosten, d.h. kein Fahrkostenabzug (auch kein Abo-Abzug); bei Geschäftsfahrzeug oder vom Arbeitgeber zur Verfügung gestelltem GA aus geschäftlichen Gründen. Vergütete Arbeitswegkosten stehen im LA Ziff. 2.3 (dann Feld F nicht angekreuzt). Halbtaxabo-Vergütung muss nicht bescheinigt werden. Max. Fahrkosten insgesamt: siehe Zwischentotal (Code 205).
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrten Wohn-/Arbeitsstätte (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt): Höchstbetrag Fr. 5'200 im Jahr (Staats- und Gemeindesteuer). Bei der direkten Bundessteuer gilt ein anderer Höchstbetrag (Fr. 3'300 laut WL 2026 UJ; siehe Bund-Datei).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0057.md) `zh-wl-2026-uj__c0057` – «bei ständiger Benützung öffentlicher Verkehrsmittel (Bahn, Schiff, Strassenbahn, Autobus) die notwendigen Abonnementskosten»
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer keine Kosten für den Arbeitsweg»

<a id="form-360-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1.2 – Fahrkosten – Fahrrad, Kleinmotorrad (gelbes Kontrollschild) pauschal (Code 202)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → keine Pauschale-Belege nötig; Lohnausweis Feld F prüfen
- **Regel:** Pauschal CHF 700 pro Jahr bei ständiger Benützung eines eigenen Fahrrads oder Kleinmotorrads mit gelbem Kontrollschild. Kein Abzug bei Feld F im Lohnausweis.
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Fahrrad, Motorfahrrad oder Motorrad mit gelbem Kontrollschild bei ständiger Benützung: Pauschale Fr. 700 im Jahr.)** · Bund **CHF 700 (Fahrrad, Motorfahrrad, Motorrad mit gelbem Kontrollschild: Pauschale CHF 700 pro Jahr; tatsächliche Kosten können nicht zusätzlich geltend gemacht werden.)**
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0055.md) `zh-wl-2026-uj__c0055` – «1.2 Fahrrad, Kleinmotorrad (gelbes Kontrollschild) pauschal CHF 700»

<a id="form-360-ziff-1-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1.3 – Fahrkosten – privates Auto/Motorrad (weisses Kontrollschild), Kilometeransatz (Code 204)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Arbeitstage x Fahrten x km; Begründung (Form. 360 Ziff. 7, Codes 2041–2044); ggf. Arbeitgeberbestätigung/Arztzeugnis
- **Regel:** Nur ausnahmsweise abziehbar (kein öffentliches Verkehrsmittel, Haltestelle mind. 1 km entfernt bzw. keine Verbindung bei Arbeitsbeginn/-ende; Zeitersparnis über 1 Stunde; ständige Benützung während der Arbeitszeit auf Verlangen des Arbeitgebers; Krankheit/Gebrechlichkeit mit Arztzeugnis). Auto CHF 0.75/km (neu 2026, vorher 0.70), Motorrad CHF 0.40/km; in der Regel begrenzt auf 240 Tage. Geleastes Fahrzeug ankreuzen. Mittagsheimfahrt: nur bis zur Höhe des Verpflegungsabzugs, dafür entfällt Verpflegungsabzug Ziff. 2.1. Geschäftsfahrzeug: kein Fahrkostenabzug (LA Feld F).
- **Limiten:**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.75 (Privates Auto (nur ausnahmsweise abziehbar): 75 Rp. pro Fahrkilometer (2026; 2025: 70 Rp.).)** · Bund **CHF 0.75 (Privatauto: CHF 0.75 pro Fahrkilometer, nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist; Gesamtmaximum CHF 3'300.)**
  - Fahrkosten Motorrad – Ansatz pro km (CHF): Kanton **CHF 0.40 (Motorrad mit weissem Kontrollschild (nur ausnahmsweise abziehbar): 40 Rp. pro Fahrkilometer.)** · Bund **CHF 0.40 (Motorrad mit weissem Kontrollschild: CHF 0.40 pro Fahrkilometer (nur wenn kein öffentliches Verkehrsmittel zumutbar); Gesamtmaximum CHF 3'300.)**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **240 Tage (Bei Auto/Motorrad (weisses Kontrollschild) ist der Fahrkostenabzug in der Regel auf 240 Arbeitstage begrenzt.)** · Bund **n/a – Bund: keine Arbeitstage-Basis für Fahrkosten; Abzug nach tatsächlichen Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG).**
- **Bemerkung:** Bei der direkten Bundessteuer dieselben Ansätze laut Formular 360 (Spalte Bund).
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0059.md) `zh-wl-2026-uj__c0059` – «Die Kosten für das private Motorfahrzeug können nur ausnahmsweise geltend gemacht»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0060.md) `zh-wl-2026-uj__c0060` – «für Auto 75 Rp. pro Fahrkilometer.»
  - [WL ZH 2026 UJ S. 8](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0021.md) `zh-wl-2026-uj__c0021` – «der Fahrkostenabzug für Automobile pro Kilometer von CHF 0.70 auf CHF 0.75 angehoben worden»

<a id="form-360-ziff-1-zwischentotal-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1 (Zwischentotal) – Fahrkosten Zwischentotal mit Plafonierung (Code 205)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg → Summe Ziff. 1.1–1.3; Lohnausweis Feld F
- **Regel:** Plafonierung: Staatssteuer max. CHF 5'200, direkte Bundessteuer max. CHF 3'300 (je Person). Lohnausweis Feld F angekreuzt: Fahrkosten auf null setzen. Arbeitnehmende mit Geschäftsfahrzeug können keine Fahrkosten abziehen.
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrten Wohn-/Arbeitsstätte (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt): Höchstbetrag Fr. 5'200 im Jahr (Staats- und Gemeindesteuer). Bei der direkten Bundessteuer gilt ein anderer Höchstbetrag (Fr. 3'300 laut WL 2026 UJ; siehe Bund-Datei).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Jahr (öffentliche Verkehrsmittel; Pauschalen bzw. km-Ansätze bei Privatfahrzeug unter den Folgeschlüsseln).)**
- **Bund:** Fahrkostenabzug max. CHF 3'300 (statt CHF 5'200).
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0060.md) `zh-wl-2026-uj__c0060` – «Bei der Staatssteuer ist der Fahrkostenabzug auf CHF 5’200 beschränkt.»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0060.md) `zh-wl-2026-uj__c0060` – «Bei der direkten Bundessteuer ist der Fahrkostenabzug auf CHF 3’300 beschränkt.»
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0060.md) `zh-wl-2026-uj__c0060` – «Arbeitnehmende, die über ein Geschäftsfahrzeug verfügen, können keine Fahrkosten in Ab-»

<a id="form-360-ziff-7-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 7 – Begründung für die Benützung eines privaten Motorfahrzeugs (Codes 2041–2044)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Zutreffendes ankreuzen; Arbeitgeberbestätigung bzw. Arztzeugnis beilegen
- **Regel:** Mindestens eine Begründung ankreuzen, sonst wird der Auto-/Motorradabzug nicht gewährt.
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0058.md) `zh-wl-2026-uj__c0058` – «Fehlen eines öffentlichen Verkehrsmittels (siehe Wegleitung) 2041»

<a id="form-360-ziff-2-1-verbilligt-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 360 Ziff. 2.1 (verbilligt) – Mehrkosten Verpflegung bei verbilligter Verpflegung durch den Arbeitgeber (Code 206)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Feld G (Kantinenverpflegung/Lunch-Checks), Anzahl Arbeitstage
- **Regel:** Ist im Lohnausweis Feld G angekreuzt (Kantine, Personalrestaurant, Lunch-Checks, Barbeitrag), steht nur der reduzierte Ansatz zu: CHF 7.50 pro Arbeitstag, höchstens CHF 1'600 pro Jahr (nur wenn die Arbeitspause die Heimkehr nicht ermöglicht und Mehrkosten gegenüber zu Hause entstehen). Das Feld G wird auch angekreuzt, wenn die Möglichkeit verbilligter Verpflegung besteht, unabhängig von der tatsächlichen Nutzung. Mittagessen vom Arbeitgeber voll bezahlt (LA Ziff. 15): kein Verpflegungsabzug. Die Abzüge Ziff. 2.1 und 2.2 dürfen nicht kumuliert werden.
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Verpflegung durch Arbeitgeber verbilligt (Kantine, Personalrestaurant, Barbeitrag, Essensgutscheine) und trotzdem Mehrkosten: Fr. 7.50 pro Arbeitstag.)** · Bund **CHF 7.50 (Nur halber Abzug (CHF 7.50 pro Tag), wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers benützt werden kann. Kein Abzug, wenn der Arbeitgeber die Naturalbezüge unter den behördlichen Bewertungsansätzen bewertet oder die Verpflegung zu Preisen unter diesen Ansätzen möglich ist (Art. 6 Abs. 3 BKV).)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei ständiger auswärtiger Verpflegung mit Verbilligung durch den Arbeitgeber: höchstens Fr. 1'600 im Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: max. CHF 1'600 pro Jahr.)**
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0061.md) `zh-wl-2026-uj__c0061` – «– wenn die Verpflegung durch den Arbeitgeber verbilligt wird (Kantine, Personalrestaurant,»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten Buchstabe G»

<a id="form-360-ziff-2-1-voll-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 360 Ziff. 2.1 (voll) – Mehrkosten Verpflegung bei voller Verpflegung zu Lasten des Arbeitnehmers (Code 208)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Anzahl Arbeitstage mit auswärtiger Verpflegung; Lohnausweis Feld G darf NICHT angekreuzt sein
- **Regel:** CHF 15 pro Arbeitstag, bei ständiger auswärtiger Verpflegung höchstens CHF 3'200 pro Jahr, wenn die Verpflegung in anderen Gaststätten voll zu Lasten des Arbeitnehmers geht. Ist im Lohnausweis Feld G angekreuzt, gilt dagegen Ansatz «verbilligt» (CHF 7.50 / 1'600).
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Auswärtige Verpflegung, wenn voll zulasten des Arbeitnehmers (Dauer der Arbeitspause ermöglicht keine Heimkehr): Fr. 15 pro Arbeitstag.)** · Bund **CHF 15 (Auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (in der Regel nur Mittagessen), nur Pauschale zulässig, wenn Hauptmahlzeit wegen grosser Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann oder bei durchgehender Schicht-/Nachtarbeit.)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei ständiger auswärtiger Verpflegung (voll zulasten Arbeitnehmer): höchstens Fr. 3'200 im Jahr. Nicht kumulierbar mit der Schicht-/Nachtarbeits-Pauschale.)** · Bund **CHF 3'200 (Auswärtige Verpflegung, voller Abzug: max. CHF 3'200 pro Jahr (bei ständiger auswärtiger Verpflegung).)**
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0061.md) `zh-wl-2026-uj__c0061` – «– wenn die Verpflegung in andern Gaststätten voll zu Lasten des Arbeitnehmers geht,»

<a id="form-360-ziff-2-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 360 Ziff. 2.2 – Mehrkosten Verpflegung bei Schicht-/Nachtarbeit (Code 210)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 (Anzahl Schichttage im Kalenderjahr); Arbeitgeberbestätigung
- **Regel:** Bei durchgehender, mindestens achtstündiger Schicht- oder Nachtarbeit CHF 15 pro ausgewiesenem Schichttag, bei ständiger Schicht-/Nachtarbeit höchstens CHF 3'200 pro Jahr; gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt, sofern beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause eingenommen werden können. Anzahl Schichttage steht – freiwillig – in Lohnausweis Ziff. 15 (Bemerkungen); fehlt sie, Bestätigung des Arbeitgebers einholen. Nicht mit Ziff. 2.1 kumulieren.
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Durchgehende, mindestens achtstündige Schicht- oder Nachtarbeit: Fr. 15 pro ausgewiesenen Schichttag, bei ständiger Schicht-/Nachtarbeit höchstens Fr. 3'200 im Jahr. Gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt, wenn die Hauptmahlzeiten nicht zur üblichen Zeit zu Hause eingenommen werden können.)** · Bund **CHF 15 (Schicht-/Nachtarbeit: gleiche Pauschale wie auswärtige Verpflegung, CHF 15 pro Tag bzw. max. CHF 3'200 pro Jahr (bei Verbilligung halber Abzug). Gestaffelte (unregelmässige) Arbeitszeit ist gleichgestellt (Art. 6 Abs. 4 BKV). Arbeitgeber muss Tage und Arbeitsort auf Verlangen bescheinigen.)**
- **Quellen:**
  - [WL ZH 2026 UJ S. 12](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0061.md) `zh-wl-2026-uj__c0061` – «2.2 Bei durchgehender, mindestens achtstündiger Schicht- oder Nachtarbeit, pro aus-»
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «die Anzahl im Kalenderjahr geleisteter Schichttage und die Höhe der im»

<a id="form-360-ziff-3-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 360 Ziff. 3 – Übrige Berufskosten – pauschal 3% (Code 212) bzw. effektiv (Code 213)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 Nettolohn; bei effektiven Kosten Aufstellung + Belege
- **Regel:** Pauschal 3% des Nettolohns gemäss Lohnausweis, mindestens CHF 2'000, höchstens CHF 4'000 (Berufskleider, Werkzeuge inkl. EDV, Fachliteratur, privates Arbeitszimmer, Berufsverbandsbeiträge). Höhere effektive Kosten: vollständig nachweisen und Aufstellung beilegen. Nettolohn = Bruttolohn nach Abzug AHV/IV/EO/ALV, laufender PK-Beiträge (inkl. aus Lohnerhöhungen) und NBU-Prämien. Vom Arbeitgeber effektiv vergütete Spesen (LA Ziff. 13) sind bei effektiver Geltendmachung zu berücksichtigen.
- **Limiten:**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **3 % (Übrige Berufskosten (Berufskleider, Berufswerkzeuge inkl. EDV, Fachliteratur, privates Arbeitszimmer, Berufsverbandsbeiträge): 3 % des Nettolohns. Nettolohn = Bruttolohn nach Abzug AHV/IV/EO/ALV, laufender Beiträge an Personalvorsorge und Prämien der obligatorischen NBUV.)** · Bund **3 % (Übrige Berufskosten: Pauschale 3 % des Nettolohns, mindestens CHF 2'000, höchstens CHF 4'000 pro Jahr; Nachweis höherer tatsächlicher Kosten möglich. Bei Teilzeit/Teiljahr angemessen zu kürzen.)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **CHF 2'000 (Mindestbetrag der Pauschale für übrige Berufskosten: Fr. 2'000.)** · Bund **CHF 2'000 (Mindestbetrag der Pauschale übrige Berufskosten.)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 4'000 (Höchstbetrag der Pauschale für übrige Berufskosten: Fr. 4'000. Höhere effektive Kosten sind in vollem Umfang nachzuweisen.)** · Bund **CHF 4'000 (Höchstbetrag der Pauschale übrige Berufskosten.)**
  - Arbeitszimmer/Homeoffice – Regel: Kanton **Kein separater Homeoffice-/Arbeitszimmerabzug: Das private Arbeitszimmer ist in der Pauschale für übrige Berufskosten (3 % des Nettolohns, min. Fr. 2'000, max. Fr. 4'000) enthalten. Höhere effektive Kosten sind in vollem Umfang nachzuweisen (Aufstellung).** · Bund **Privates Arbeitszimmer: in der Pauschale übrige Berufskosten enthalten. Separater Abzug der Zimmerkosten (Miete, Heizung, Beleuchtung) nur bei Nachweis höherer Kosten und wenn ein Zimmer der Privatwohnung hauptsächlich und regelmässig für die Berufsarbeit benützt werden muss; bloss gelegentliche Arbeit zu Hause gibt keinen Abzug. Keine pauschale Homeoffice-Entschädigung.**
- **Quellen:**
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0062.md) `zh-wl-2026-uj__c0062` – «3% des Nettolohnes gemäss Lohnausweis, mindestens jedoch CHF 2’000»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0064.md) `zh-wl-2026-uj__c0064` – «so sind diese Berufsauslagen in vollem Umfange nachzuweisen.»

<a id="form-360-ziff-4-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 360 Ziff. 4 – Zusätzliche Mehrkosten bei auswärtigem Wochenaufenthalt (Code 2860)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag/Beleg Zimmer; Aufstellung; ÖV-Abo für Heimkehr (unter Ziff. 1.1)
- **Regel:** Abziehbar: Mehrkosten auswärtige Verpflegung (Abendessen CHF 15 pro Arbeitstag, bei ganzjährigem Wochenaufenthalt max. CHF 3'200 pro Jahr), Mietzins für ein Zimmer, Kosten der wöchentlichen Heimkehr (in der Regel nur ÖV, z.B. GA – unter Ziff. 1 des Hilfsblatts).
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Auswärtiger Wochenaufenthalt: als Mehrkosten für die auswärtige Unterkunft kann der Mietzins für ein Zimmer abgezogen werden (effektive Kosten, gemäss Aufstellung). Kosten der wöchentlichen Heimkehr in der Regel nur ÖV-Aufwendungen (unter Fahrkosten, Ziff. 1 des Berufsauslagenblatts).** · Bund **Wochenaufenthalt: abziehbar sind die ortsüblichen Auslagen für ein Zimmer (nicht eine Wohnung) am Arbeitsort sowie die Fahrkosten der regelmässigen Heimkehr (im Rahmen des Fahrkosten-Maximums).**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 3'200 (Auswärtiger Wochenaufenthalt: Mehrkosten für auswärtige Verpflegung beim Abendessen Fr. 15 pro Arbeitstag bzw. Fr. 3'200 im Jahr bei ganzjährigem Wochenaufenthalt.)** · Bund **CHF 6'400 (Wochenaufenthalt Verpflegung: voller Abzug CHF 30 pro Tag bzw. CHF 6'400 pro Jahr; gekürzter Abzug (verbilligtes Mittagessen) CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr. Nachweis höherer Kosten ausgeschlossen.)**
- **Bemerkung:** Code 2860 aus der Formularzeile; im PDF-Layout steht daneben Code 213 (effektive übrige Berufskosten) – Zuordnung am Original prüfen. Hinweis Prüfung: ZH-Wegleitung nennt nur CHF 15/Abendessen bzw. 3'200 pro Jahr; Bundes-Wert laut data/werte/bund/2026.yaml (CHF 30/Tag, 6'400) weicht ab – für die Bundessteuer am Original prüfen.
- **Quellen:**
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0066.md) `zh-wl-2026-uj__c0066` – «Als Mehrkosten für auswärtige Unterkunft kann der Mietzins für ein Zimmer abgezogen werden.»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0066.md) `zh-wl-2026-uj__c0066` – «bei ganzjährigem Wochenaufenthalt CHF 3’200 im Jahr abgezogen werden»

<a id="form-360-ziff-5-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 360 Ziff. 5 – Auslagen bei Nebenerwerb – pauschal 20% (Code 216) bzw. effektiv (Code 217)

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Einkünfte aus Nebenerwerb (Ziff. 1.2); bei effektiven Auslagen Aufstellung
- **Regel:** Pauschal 20% der Einkünfte aus allen Nebenbeschäftigungen, insgesamt mind. CHF 800 und höchstens CHF 2'400; deckt sämtliche Auslagen im Nebenerwerb (inkl. Fahrkosten, Verpflegung). Höhere effektive Auslagen detailliert aufführen und nachweisen.
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Auslagen bei Nebenbeschäftigung in unselbstständiger Stellung (inkl. Fahrkosten, auswärtige Verpflegung): 20 % der Einkünfte aus der Nebenbeschäftigung.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug Sozialversicherungsbeiträge), mindestens CHF 800, höchstens CHF 2'400; Nachweis höherer Kosten mit separater Aufstellung möglich.)**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Mindestbetrag der Nebenerwerbs-Pauschale: Fr. 800.)** · Bund **CHF 800 (Mindestbetrag Pauschale Nebenerwerb.)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Höchstbetrag der Nebenerwerbs-Pauschale: Fr. 2'400. Höhere effektive Kosten sind detailliert aufzuführen und nachzuweisen.)** · Bund **CHF 2'400 (Höchstbetrag Pauschale Nebenerwerb.)**
- **Quellen:**
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0067.md) `zh-wl-2026-uj__c0067` – «20% der Einkünfte aus allen Nebenbeschäftigungen, insgesamt mindestens jedoch CHF 800 und höchstens CHF 2’400»

## Hilfsblatt Versicherungsprämien

<a id="form-365-teil-a-ziff-1-6-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil A (Ziff. 1–6) – Bezahlte Versicherungsprämien und Zinsen von Sparkapitalien (Codes 601–607, Total A 606)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → 1. Private Krankenversicherung (601), 2. private Unfallversicherung (602), 3. Lebens-/Rentenversicherung (603), 4. Sparzinsen (604), 6. abzüglich erhaltene Prämienverbilligungen (605) → Total A (606)
- **Regel:** Tatsächlich bezahlte Prämien und Einlagen für Kranken-, Unfall-, Lebens- und Rentenversicherungen sowie Sparzinsen (gemäss Wertschriftenverzeichnis). Individuelle Prämienverbilligung (IPV) abziehen, soweit nicht bereits mit den Prämien des Krankenversicherers verrechnet (dann bereits reduzierte Prämie eintragen). Kinder: Prämien der unterhaltenen Personen einbeziehen.
- **Quellen:**
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0079.md) `zh-wl-2026-uj__c0079` – «6. Abzüglich erhaltene Prämienverbilligungen 605»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0078.md) `zh-wl-2026-uj__c0078` – «Der zulässige Abzug für Versicherungsprämien und Sparzinsen ist im Formular Versicherungs-»

<a id="form-365-teil-b-ziff-1-3-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil B (Ziff. 1–3) – Maximaler Abzug für Versicherungsprämien und Sparzinsen (Codes 611–616)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand/Kinder aus Seite 1; Frage Beiträge 2. Säule/3a (Form. 300 S. 1 und Ziff. 14)
- **Regel:** Verheiratete (611): 5'800 Staat / 3'700 Bund, ohne Beiträge an 2. Säule oder 3a 8'700 / 5'550. Übrige (612): 2'900 / 1'800, ohne Vorsorgebeiträge 4'350 / 2'700. Zusatz je Kind (613) bzw. je unterstützungsbedürftige Person (614/615): 1'300 / 700. Total B = Code 616. Teil C: niedrigerer Betrag von A und B nach Ziff. 15 übertragen (Code 270).
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'800 (Versicherungsprämien und Sparzinsen (Staatssteuer), in ungetrennter Ehe lebende Steuerpflichtige mit Beiträgen an 2. Säule/Säule 3a: Fr. 5'800.)** · Bund **CHF 3'700 (Versicherungsprämien und Zinsen von Sparkapitalien, Ehepaare in ungetrennter Ehe, mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 3'700.)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 8'700 (Gemeinsam Besteuerte ohne Beiträge an 2. Säule und Säule 3a (weder durch Steuerpflichtige noch Arbeitgeber): Abzug erhöht sich um die Hälfte, höchstens Fr. 8'700.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an 2. Säule und Säule 3a: Höchstabzug CHF 5'550 (Erhöhung um die Hälfte).)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'900 (Versicherungsprämien und Sparzinsen (Staatssteuer), übrige Steuerpflichtige (nicht in ungetrennter Ehe) mit Vorsorgebeiträgen: Fr. 2'900.)** · Bund **CHF 1'800 (Übrige Steuerpflichtige mit Beiträgen an 2. Säule oder Säule 3a: max. CHF 1'800.)**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 4'350 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: Abzug erhöht sich um die Hälfte, höchstens Fr. 4'350.)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule und Säule 3a: max. CHF 2'700.)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'300 (Zuschlag zum Versicherungsabzug: Fr. 1'300 für jedes Kind oder jede unterstützungsbedürftige Person mit Kinder-/Unterstützungsabzug nach § 34 Abs. 1; bei hälftig aufgeteiltem Kinderabzug Fr. 650.)** · Bund **CHF 700 (Zuschlag CHF 700 pro Kind bzw. unterstützungsbedürftige Person, für die ein Abzug nach Art. 35 Abs. 1 lit. a oder b DBG geltend gemacht werden kann.)**
- **Bund:** Spalte Bundessteuer: 3'700 / 5'550 (Verheiratete), 1'800 / 2'700 (Übrige), 700 je Kind.
- **Quellen:**
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0080.md) `zh-wl-2026-uj__c0080` – «oder: sofern weder Beiträge an die 2. noch an die 3. Säule a geleistet wurden 8’700 5’550»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0080.md) `zh-wl-2026-uj__c0080` – «Zusätzlicher Abzug für jedes Kind Anzahl: 1’300 700 613»
  - [WL ZH 2026 UJ S. 14](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0081.md) `zh-wl-2026-uj__c0081` – «Der niedrigere Betrag: (A) oder (B) 270»

## Hilfsblatt Weiterbildung

<a id="form-367-abzug-weiterbildung"></a>
### Ziff. Form. 367 – Berufsorientierte Aus- und Weiterbildungskosten: Total Kosten (2900/2903), Beitrag Arbeitgeber/Dritte (2901/2904), selbstgetragene Kosten (2902/2905), zulässiger Abzug (2920/2921) → Code 292

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Rechnungen; Lohnausweis Ziff. 13.3; Bestätigung Branchenverband/Bund
- **Regel:** Total der Kosten minus Beiträge des Arbeitgebers oder weiterer Stellen (Bund, Branchenverbände) = selbstgetragene Kosten; zulässiger Abzug getrennt für Staatssteuer (max. CHF 12'600) und Bundessteuer (max. CHF 13'000) je Person; Übertrag in Ziff. 16.2.
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 12'600 (Berufsorientierte Aus- und Weiterbildungskosten inkl. Umschulung: bis Fr. 12'600 (Staatssteuer), sofern erster Abschluss Sekundarstufe II vorliegt oder das 20. Lebensjahr vollendet ist (und es nicht um Kosten bis zum ersten Abschluss Sek. II geht).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildungs- inkl. Umschulungskosten bis CHF 13'000 pro Jahr, sofern erster Abschluss Sek. II vorliegt oder das 20. Lebensjahr vollendet ist (und nicht Ausbildung bis zum ersten Abschluss Sek. II).)**
- **Bund:** Max. CHF 13'000 (Zeile Bundessteuer).
- **Bemerkung:** Personenzuordnung der Codes 2900–2905 (Spaltenfolge) am Original prüfen.
- **Quellen:**
  - [WL ZH 2026 UJ S. 15](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0090.md) `zh-wl-2026-uj__c0090` – «Beitrag Arbeitgeber oder weiterer Stellen (Bund, Branchenverbände etc.) 2901 / 2904»

## Einkommensberechnung

<a id="19-berechnung-total"></a>
### Ziff. 19 – Total der Einkünfte, Übertrag von Seite 2 Ziffer 7 (Code 199)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Übertrag Ziff. 7
- **Regel:** Rechenzeile.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «19. Total der Einkünfte Übertrag von Seite 2, Ziffer 7 199»

<a id="20-berechnung-total"></a>
### Ziff. 20 – Total der Abzüge, Übertrag von Ziffer 18 (Code 299)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Übertrag Ziff. 18
- **Regel:** Rechenzeile.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «20. Total der Abzüge Übertrag von Ziffer 18 299»

<a id="21-berechnung-total"></a>
### Ziff. 21 – Nettoeinkommen (Code 310)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ziff. 19 minus Ziff. 20
- **Regel:** Rechenzeile; Basis für den Selbstbehalt der Krankheitskosten (5%) und die Obergrenze der Zuwendungen (20%), je getrennt für Staats- und Bundessteuer.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «21. Nettoeinkommen 310»

<a id="22-1-abzug-krankheitskosten"></a>
### Ziff. 22.1 – Krankheits- und Unfallkosten (Code 320)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Aufstellung über Krankheits- und Unfallkosten (Form. 370) Teil E Abzug; Leistungsabrechnungen der Krankenkasse (Selbstbehalt/Franchise)
- **Regel:** Selbst getragene Kosten für sich und unterhaltene Personen, soweit sie 5% des Nettoeinkommens (Ziff. 21) übersteigen (Staats- und Bundessteuer je getrennt). Formular Form. 370 vollständig ausfüllen, Belege geordnet beilegen. Nicht abziehbar: Prävention (Fitness), Fahrkosten zum Arzt, Akupunktur ohne Verordnung, eigene Pflegeleistungen, Schlankheits-/Wellness-/Schönheitsbehandlungen, Psychoanalysen. Ärztlich angeordnete Diät: Mehrkosten oder Pauschale CHF 2'500.
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten sind abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen gemäss §§ 26-31 verminderten steuerbaren Einkünfte (laut Wegleitung: Nettoeinkommen, Ziff. 21). Diät-Pauschale Fr. 2'500 bei ärztlich angeordneter, lebensnotwendiger Diät.)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
- **Quellen:**
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0115.md) `zh-wl-2026-uj__c0115` – «Gesetz erwähnten Selbstbehalt von 5% des Nettoeinkommens (Ziffer 21 der Steuererklärung)»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0116.md) `zh-wl-2026-uj__c0116` – «wollen, müssen mit der Steuererklärung das vollständig ausgefüllte Formular «Aufstellung über»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0119.md) `zh-wl-2026-uj__c0119` – «CHF 2500 geltend gemacht wer-»

<a id="22-2-abzug-spenden"></a>
### Ziff. 22.2 – Gemeinnützige Zuwendungen (Code 324)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigungen / Aufstellung über gemeinnützige Zuwendungen (Empfänger, Betrag)
- **Regel:** Freiwillige Leistungen an Bund, Kantone, Gemeinden und deren Anstalten sowie an steuerbefreite juristische Personen mit Sitz in der Schweiz mit öffentlichen oder ausschliesslich gemeinnützigen Zwecken; abziehbar, wenn die Zuwendungen in der Steuerperiode mindestens CHF 100 erreichen und insgesamt höchstens 20% des Nettoeinkommens (Ziff. 21) ausmachen. Aufstellung beilegen. Keine Mitgliederbeiträge mit Gegenleistung; Parteispenden gehören zu Ziff. 16.5.
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentliche/gemeinnützige Zwecke): Abzug, wenn die Zuwendungen in der Steuerperiode mindestens Fr. 100 erreichen.)** · Bund **CHF 100 (Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (und Bund/Kantone/Gemeinden): abziehbar, wenn im Steuerjahr mindestens CHF 100 erreicht.)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Zuwendungen insgesamt höchstens 20 % der um die Aufwendungen gemäss §§ 26-31 verminderten steuerbaren Einkünfte (Nettoeinkommen).)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26-33) verminderten Einkünfte.)**
- **Bund:** Gleiche Regel (mind. CHF 100, max. 20% des Nettoeinkommens).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «22.2 Gemeinnützige Zuwendungen Aufstellung 324»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0120.md) `zh-wl-2026-uj__c0120` – «des Nettoeinkommens (Ziffer 21 der Steuererklärung) nicht übersteigen.»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0120.md) `zh-wl-2026-uj__c0120` – «Wir bitten Sie, der Steuererklärung eine Aufstellung über gemeinnützige Zuwendungen bei-»

<a id="23-berechnung-total"></a>
### Ziff. 23 – Reineinkommen (Ziffer 21 abzüglich Ziffern 22.1 und 22.2) (Code 350)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ziff. 21 minus 22.1 minus 22.2
- **Regel:** Rechenzeile; Basis für Sozialabzüge.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0009.md) `zh-form-300-2026-uj__c0009` – «(Ziffer 21 abzüglich Ziffern 22.1 und 22.2) 350»

<a id="24-1-sozialabzug-kinder"></a>
### Ziff. 24.1 – Abzug für Kinder in Ihrem Haushalt (Code 370) und ausserhalb Ihres Haushaltes (Code 372)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien Kinder Seite 1 (Geburtsjahr, Ausbildung, elterliche Sorge, Alimente)
- **Regel:** Staatssteuer CHF 9'400 pro Kind, Bundessteuer CHF 6'800 pro Kind für Kinder, die am 31.12.2026 minderjährig sind (Jahrgänge 2009–2026), oder volljährig in beruflicher Erstausbildung mit Unterhalt zur Hauptsache. Ehepaar/Verwitwete: ganzer Abzug. Alleinerziehend: ganzer Abzug bei alleiniger Sorge oder bei gemeinsamer Sorge mit erhaltenen Alimenten; halber Abzug (CHF 4'700 / 3'400) bei gemeinsamer Sorge ohne erhaltene Alimente. Getrennt lebender Elternteil: halber Abzug bei gemeinsamer Sorge ohne eigene Alimentenzahlung; bei Alimentenabzug oder ohne Sorge kein Kinderabzug. Konkubinat: ganzer Abzug nur bei alleiniger Sorge oder gemeinsamer Sorge mit erhaltenen Alimenten, sonst je halber; volljährige Kinder: Abzug beim Elternteil mit höherem Beitrag. Sozialabzüge nach Verhältnissen am Ende der Steuerperiode bzw. Steuerpflicht; bei unterjähriger Steuerpflicht anteilmässig.
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

<a id="24-2-sozialabzug-unterstuetzung"></a>
### Ziff. 24.2 – Abzug für unterstützte Personen (Code 374)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der Unterstützung; auf Verlangen Zahlungsbelege (bei Auslandzahlungen Post-/Bankbelege)
- **Regel:** Für erwerbsunfähige oder beschränkt erwerbsfähige, finanziell unterstützungsbedürftige Personen. Nicht für Leistungen an den Ehegatten, an Kinder mit Kinderabzug, oder wenn für dieselbe Person Alimente abgezogen werden. Staatssteuer CHF 2'800 (Unterstützung mind. in dieser Höhe), Bundessteuer CHF 6'800 (Unterstützung mind. in dieser Höhe).
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'800 (Unterstützungsabzug für erwerbsunfähige oder beschränkt erwerbsfähige Personen, an deren Unterhalt mindestens in Höhe des Abzugs beigetragen wird: Fr. 2'800 je Person. Nicht für Ehegatten und Kinder mit Kinderabzug oder Unterhaltsbeitragsabzug.)** · Bund **CHF 6'800 (Unterstützungsabzug CHF 6'800 pro erwerbsunfähige oder beschränkt erwerbsfähige Person, zu deren Unterhalt die steuerpflichtige Person mindestens in der Höhe des Abzugs beiträgt; nicht für Ehegatten und Kinder mit Abzug nach lit. a.)**
- **Bund:** Abzug und Mindestunterstützung CHF 6'800 (statt CHF 2'800).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «24.2 Abzug für unterstützte Personen Bestätigung»
  - [WL ZH 2026 UJ S. 20](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0133.md) `zh-wl-2026-uj__c0133` – «Der Abzug kann nicht gewährt werden:»
  - [WL ZH 2026 UJ S. 20](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0134.md) `zh-wl-2026-uj__c0134` – «des Unterstützungsabzuges von CHF 2’800»

<a id="24-3-sozialabzug-verheiratete"></a>
### Ziff. 24.3 – Abzug für Ehegatten/Partner – nur Bundessteuer (Code 365)

- **Schlüssel:** `sozialabzug.verheiratete` (Verheiratetenabzug (Bund)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand (rechtlich und tatsächlich ungetrennte Ehe/Partnerschaft)
- **Regel:** Nur bei der direkten Bundessteuer: Verheiratetenabzug CHF 2'800 für alle in rechtlich und tatsächlich ungetrennter Ehe Lebenden; bei der Staatssteuer keine Zeile (Staatssteuer-Spalte leer).
- **Limiten:**
  - Verheiratetenabzug (CHF, Bund): Kanton **n/a** · Bund **CHF 2'800 (Verheiratetenabzug CHF 2'800 für Ehepaare in rechtlich und tatsächlich ungetrennter Ehe.)**
- **Bund:** Verheiratetenabzug CHF 2'800 (nur Bund).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «24.3 Abzug für Ehegatten / Partn.»
  - [WL ZH 2026 UJ S. 20](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0134.md) `zh-wl-2026-uj__c0134` – «Steuerpflichtigen einen Verheiratetenabzug von CHF 2’800.»

<a id="25-berechnung-total"></a>
### Ziff. 25 – Steuerbares Einkommen gesamt (Ziffer 23 abzüglich Ziff. 24.1 bis 24.3) (Code 390)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ziff. 23 minus Ziff. 24
- **Regel:** Rechenzeile.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «25. Steuerbares Einkommen gesamt (Ziffer 23 abz. Ziff. 24.1 bis 24.3) 390»

<a id="26-1-26-2-berechnung-total"></a>
### Ziff. 26.1 / 26.2 – Auf steuerbare Einkünfte in anderen Kantonen (Code 394) / im Ausland (Code 396) entfallender Anteil

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ausscheidung aus Liegenschaften/Geschäftsbetrieben/Betriebsstätten ausserhalb ZH
- **Regel:** Nur bei interkantonaler/internationaler Steuerausscheidung ausfüllen (Staatssteuer); sonst leer.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «26.1 Auf steuerbare Einkünfte in anderen Kantonen 394»
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «26.2 Auf steuerbare Einkünfte im Ausland 396»

<a id="27-berechnung-total"></a>
### Ziff. 27 – Steuerbares Einkommen im Kanton Zürich bzw. in der Schweiz (Code 398)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ziff. 25 minus Ziff. 26
- **Regel:** Rechenzeile; Grundlage der Steuerberechnung.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 3](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0010.md) `zh-form-300-2026-uj__c0010` – «27. Steuerbares Einkommen im Kanton Zürich bzw. in der Schweiz 398»

## Hilfsblatt Krankheitskosten

<a id="form-370-teil-a-e-abzug-krankheitskosten"></a>
### Ziff. Form. 370 Teil A–E – Aufstellung über Krankheits- und Unfallkosten: A Aufwendungen (300–307, Total 317), B Vergütungen Dritter (308, 311, 312, Total 318), C Auslagen netto (314), D Pauschale (315), E Berechnung (313, Selbstbehalt 319, Abzug 320)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung, Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung) → Zeilen 1 Selbstbehalt/Franchise lt. Krankenkassenabrechnung (300); 2 Arzt und Medikamente (301); 3 Zahnarzt (302); 4 Pflegepersonal (303); 5 Spital/Heilstätten (304); 6 Therapien/Kuren (305)
- **Regel:** Aufwendungen (A) abzüglich Vergütungen Dritter inkl. Anteil Lebenshaltungskosten bei Heim-/Spitalaufenthalt (B) = Auslagen netto (C); bei andauernder lebensnotwendiger Diät statt effektiv Pauschale (D). Davon wird in Teil E der Selbstbehalt (5% des Nettoeinkommens Ziff. 21, Staats- und Bundessteuer getrennt) abgezogen; Ergebnis Code 320 nach Ziff. 22.1. Krankenkassen stellen auf Verlangen Kosten- und Prämienzusammenstellungen aus.
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten sind abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen gemäss §§ 26-31 verminderten steuerbaren Einkünfte (laut Wegleitung: Nettoeinkommen, Ziff. 21). Diät-Pauschale Fr. 2'500 bei ärztlich angeordneter, lebensnotwendiger Diät.)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit selbst getragen und über 5 % der um die Aufwendungen (Art. 26-33) verminderten steuerbaren Einkünfte. Behinderungsbedingte Kosten (lit. hbis) ohne Selbstbehalt.)**
- **Quellen:**
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0117.md) `zh-wl-2026-uj__c0117` – «1. Selbstbehalt gemäss Abrechnung Krankenkasse und Versicherung 300»
  - [WL ZH 2026 UJ S. 18](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0120.md) `zh-wl-2026-uj__c0120` – «abzüglich Selbstbehalt (5% von Ziffer 21 der»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben (Code 400)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Wertschriften- und Guthabenverzeichnis (Form. 340) Total Steuerwert per 31.12.2026; eSteuerauszug der Bank (Steuerwert 31.12.)
- **Regel:** Total Steuerwert aus dem Wertschriftenverzeichnis. Guthaben zum vollen Forderungsbetrag; Fremdwährung zu Devisenkursen; Kryptowährungen zum Marktwert. Nutzniessungsvermögen beim Nutzniesser. Ansprüche an Vorsorgeeinrichtungen (2. Säule, 3a, Freizügigkeit) sind steuerfrei und nicht aufzuführen. Bei Ende der Steuerpflicht Stichtag-Werte.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0011.md) `zh-form-300-2026-uj__c0011` – «30.1 Wertschriften und Guthaben Wertschriftenverzeichnis 400»
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0158.md) `zh-wl-2026-uj__c0158` – «Kryptowährungen wie Bitcoin sind zum Marktwert zu deklarieren.»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0155.md) `zh-wl-2026-uj__c0155` – «Leistungen steuerfrei und nicht im Wertschriftenverzeichnis aufzuführen.»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 404)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bestandesaufstellung per 31.12.; Kurswert (ausländische Noten/Münzen/Edelmetalle zum Tageskurs)
- **Regel:** Ausländische Banknoten, Goldmünzen und Edelmetalle zum Tageskurs; Bargeld per Stichtag.
- **Quellen:**
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0137.md) `zh-wl-2026-uj__c0137` – «Ausländische Banknoten, Goldmünzen und Edelmetalle sind zum Tageskurs anzugeben.»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen (Steuerwert gem. Bescheinigung der Versicherungsgesellschaft) (Code 406)

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Steuerwert-Bescheinigung der Versicherungsgesellschaft (Gesellschaft, Abschlussjahr, Ablaufsjahr, Steuerwert)
- **Regel:** Rückkaufsfähige Lebens- und Rentenversicherungen: Steuerwert gemäss Bescheinigung (beilegen), auch nach Rentenbeginn bei rückkaufsfähigen Rentenversicherungen. Nicht rückkaufsfähige Renten (nach Rentenbeginn): kein Vermögen. Säule-3a-Policen bis Fälligkeit steuerfrei (nicht aufführen).
- **Quellen:**
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0138.md) `zh-wl-2026-uj__c0138` – «Der Vermögenssteuerwert von Lebensversicherungen richtet sich nach dem Steuerwert. Dabei»
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0138.md) `zh-wl-2026-uj__c0138` – «abgeschlossene Vorsorgepolicen sind bis zur Fälligkeit der Versicherungssumme steuerfrei.»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge (Kaufpreis, Kaufjahr) (Code 412)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Kaufvertrag/Fahrzeugausweis (Kaufpreis und Kaufjahr)
- **Regel:** Privates Motorfahrzeug mit aktuellem Verkehrswert; Wertverminderung in der Regel 40% des Restwertes pro Jahr. Geleaste Fahrzeuge nicht deklarieren (Leasingzinsen/-raten nicht abziehbar, siehe Ziff. 12).
- **Quellen:**
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0139.md) `zh-wl-2026-uj__c0139` – «beträgt die Wertverminderung pro Jahr 40% des Restwertes.»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Geschäfts-/Korporationsanteile (Code 414)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung über Kapital und Ertrag; Beteiligungsquote
- **Regel:** Anteilmässig entsprechend der Beteiligungsquote deklarieren; Aufstellung über Kapital und Ertrag beilegen.
- **Quellen:**
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0139.md) `zh-wl-2026-uj__c0139` – «Geschäfts- und Korporationsanteile sind von den Inhabern anteilmässig entsprechend ihrer»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte, nähere Bezeichnung (Code 416)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung (Gemälde, Sammlungen, Kunst, Schmuck, Boote, Flugzeuge)
- **Regel:** Sammlungen, Kunst- und Schmuckgegenstände, Boote, Flugzeuge etc. mit Verkehrswert. Hausrat ist steuerfrei.
- **Quellen:**
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0139.md) `zh-wl-2026-uj__c0139` – «Der Hausrat ist steuerfrei.»

<a id="31-1-vermoegen-liegenschaften"></a>
### Ziff. 31.1 – Liegenschaften, zum Verkehrswert besteuert, gemäss Neufestsetzung ab 1.1.2026 (Code 421)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftenverzeichnis (Form. 350) Steuerwert (Verkehrswert); Liegenschaftenbewertung 2026 der Gemeinde
- **Regel:** Vermögenssteuerwert aus der Neubewertung per 1.1.2026 (Weisung 2026) einsetzen; die Neubewertung ist zusammen mit der Steuererklärung 2026 einzureichen. EFH/STWE: Wert gemäss Weisung 2026; MFH/Geschäftshäuser: Ertragswert (Hilfsblatt). Nutzniessung: beim Nutzniesser zu 100%; Wohnrecht: beim Eigentümer. Total Verkehrswerte aller (nicht land-/forstwirtschaftlichen) Liegenschaften in 31.1.
- **Bemerkung:** Spaltenzuordnung der Codes 553x/554x im Liegenschaftenverzeichnis (Ertragswert/Verkehrswert) am Original prüfen.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «31.1 Zum Verkehrswert besteuert Liegenschaftenverzeichnis 421»
  - [WL ZH 2026 UJ S. 29](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0203.md) `zh-wl-2026-uj__c0203` – «ist der nach der «Weisung des Regierungsrates an die Steuerbehörden über die Bewertung»
  - [WL ZH 2026 UJ S. 30](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0213.md) `zh-wl-2026-uj__c0213` – «Bei Liegenschaften, auf denen ein Wohnrecht lastet, ist der Vermögenssteuerwert zu 100%»

<a id="31-2-vermoegen-liegenschaften"></a>
### Ziff. 31.2 – Liegenschaften, zum Ertragswert besteuert (Land- oder Forstwirtschaft) (Code 422)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftenverzeichnis (Form. 350) Spalte Ertragswert Land-/Forstwirtschaft
- **Regel:** Total der Vermögenssteuerwerte land- und forstwirtschaftlicher Liegenschaften (Ertragswert) hier, alle übrigen in Ziff. 31.1.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «31.2 Zum Ertragswert besteuert (Land- oder Forstwirtschaft) Liegenschaftenverzeichnis 422»
  - [WL ZH 2026 UJ S. 30](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0213.md) `zh-wl-2026-uj__c0213` – «Das Total der Vermögenssteuerwerte aller übrigen Liegenschaften ist auf Seite 4, Ziffer 31.1 der»

<a id="32-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32 – Eigenkapital Selbständigerwerbender ohne Geschäftswertschriften (Code 430)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsblatt A Ziff. 10.4 (kaufmännische Buchführung) bzw. Ziff. 14.4 (vereinfachte Buchführung)
- **Regel:** Eigenkapital laut Hilfsblatt A übertragen; Geschäftswertschriften im Wertschriftenverzeichnis (Code G).
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «32. Eigenkapital Selbständigerwerbender ohne Geschäftswertschriften Hilfsblatt A 430»
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0140.md) `zh-wl-2026-uj__c0140` – «Selbständigerwerbende mit kaufmännischer Buchführung übertragen das Eigenkapital laut»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 460)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Summe Ziff. 30–32
- **Regel:** Rechenzeile.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «33. Total der Vermögenswerte 460»

<a id="34-schulden-privat"></a>
### Ziff. 34 – Schulden (Code 470)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Kreditkartenabrechnung (Monats-/Jahresabrechnung, Karten-Jahresgebühr) → Schuldenverzeichnis (Form. 355) Total Privatschulden (Code 3200) per 31.12.2026; Hypothekarbestätigung / Saldobestätigung der Bank
- **Regel:** Gesamtbetrag der Privatschulden inkl. Grundpfandschulden per 31.12.2026; vollständiges Schuldenverzeichnis mit Gläubiger (genaue Adresse) und Zinssatz beilegen. Zinsen → Ziff. 12 (Code 3201). Leasing: Schuld nicht deklarieren, wenn Fahrzeug nicht deklariert.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «34. Schulden Schuldenverzeichnis 470»
  - [WL ZH 2026 UJ S. 21](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0140.md) `zh-wl-2026-uj__c0140` – «Werden Schulden deklariert, ist ein vollständiges Schuldenverzeichnis mit der Steuererklärung»
  - [WL ZH 2026 UJ S. 13](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0070.md) `zh-wl-2026-uj__c0070` – «Total Privatschulden / private Schuldzinsen 3200 / 3201»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Steuerbares Vermögen gesamt (Code 490)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ziff. 33 minus Ziff. 34
- **Regel:** Rechenzeile; keine Vermögenssteuer bei der direkten Bundessteuer.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «35. Steuerbares Vermögen gesamt 490»

<a id="36-1-36-2-berechnung-total"></a>
### Ziff. 36.1 / 36.2 – Auf steuerbare Vermögenswerte in anderen Kantonen (Code 494) / im Ausland (Code 496) entfallender Anteil

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ausscheidung ausserkantonale/ausländische Liegenschaften und Betriebe
- **Regel:** Nur bei Steuerausscheidung ausfüllen.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «36.1 Auf steuerbare Vermögenswerte in anderen Kantonen 494»
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «36.2 Auf steuerbare Vermögenswerte im Ausland 496»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen im Kanton Zürich (Code 498)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Ziff. 35 minus Ziff. 36
- **Regel:** Rechenzeile; Grundlage der Vermögenssteuer.
- **Quellen:**
  - [Formular 300 ZH 2026 UJ S. 4](../../chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0012.md) `zh-form-300-2026-uj__c0012` – «37. Steuerbares Vermögen im Kanton Zürich 498»

<a id="tarif-47-vermoegen-sozialabzug"></a>
### Ziff. (Tarif § 47) – Steuerfreie Vermögensbeträge (kein Formularfeld; im Tarif berücksichtigt)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand/Kinder (Seite 1)
- **Regel:** Kein Eintrag im Formular. Der Vermögenstarif sieht Nullsätze für die ersten CHF 81'000 (übrige) bzw. CHF 161'000 (Verheiratete und ledige/geschiedene Steuerpflichtige mit Kindern im Haushalt) vor.
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 81'000 (Vermögenssteuer Grundtarif: 0 ‰ für die ersten Fr. 81'000 (steuerfreies Vermögen im Tarif; kein separater Sozialabzug).)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 161'000 (Vermögenssteuer Verheiratetentarif (ungetrennte Ehe; auch Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern im Haushalt): 0 ‰ für die ersten Fr. 161'000.)** · Bund **n/a – Der Bund erhebt keine Vermögenssteuer (nur Einkommenssteuer, DBG); Vermögenswerte kantonal.**
- **Bund:** Keine Vermögenssteuer beim Bund.
- **Quellen:**
  - [StG ZH § 47](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-47-t1.md) `zh-stg-2026__par-47-t1` – «0‰ für die ersten Fr. 81 000»
  - [StG ZH § 47](../../chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-47-t2.md) `zh-stg-2026__par-47-t2` – «0‰ für die ersten Fr. 161 000»

## Hilfsblatt Wertschriftenverzeichnis

<a id="form-340-kolonnen-a-b-codes-einkommen-wertschriften"></a>
### Ziff. Form. 340 (Kolonnen A/B, Codes) – Wertschriften- und Guthabenverzeichnis mit Verrechnungsantrag: Kolonne A (mit Verrechnungssteuerabzug), Kolonne B (ohne); Codes G, N, E, S, Q

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Steuerauszug/eSteuerauszug; Zins- und Dividendenabrechnungen; Bankbelege Festgeld/Kassenobligationen
- **Regel:** Bruttoerträge je nach Verrechnungssteuerabzug in Kolonne A oder B. Kolonne A: schweizerische Zinsen/Dividenden, auch Kundenguthaben mit Bruttozins über CHF 200 pro Jahr. Kennzeichnen: G Geschäftsvermögen, N Nutzniessungsvermögen, E Werte aus Erbschaft 2026, S Schenkung 2026, Q Beteiligung mind. 10%. Ausländische Titel mit ISIN/Valor, Erträge zum Tageskurs. Ausländische Quellensteuern/US-Steuerrückbehalt via Formular DA-1 (Übertrag in Zeile «Übertrag ab Formular DA-1»). Total Ertrag → Ziff. 4.1, Total Steuerwert → Ziff. 30.1.
- **Quellen:**
  - [WL ZH 2026 UJ S. 25](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0160.md) `zh-wl-2026-uj__c0160` – «Dies gilt auch für Kundenguthaben mit einem Bruttozins von mehr als»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0156.md) `zh-wl-2026-uj__c0156` – «mit Q Beteiligungen von mindestens 10 Prozent am Aktien-, Grund- oder Stammkapital an»
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0155.md) `zh-wl-2026-uj__c0155` – «ob die Verrechnungssteuer abgezogen wurde oder nicht, entweder in der Kolonne A oder Kolonne B einzutragen.»

<a id="form-340-verrechnungsantrag-da-1-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 340 (Verrechnungsantrag / DA-1) – Verrechnungsantrag (Rückerstattung Verrechnungssteuer, Kolonne A) und Formular DA-1 (ausländische Quellensteuern)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Bankverbindung (IBAN) für Rückerstattung; DA-1 mit Quellensteuerbelegen
- **Regel:** Mit der Unterschrift wird bestätigt, dass auf allen Erträgen der Kolonne A die Verrechnungssteuer abgezogen wurde. Rückerstattung auf angegebenes Konto. Ausländische Quellensteuern: Antrag DA-1; Anrechnung nur, wenn die nicht rückforderbaren ausländischen Steuern insgesamt CHF 100 übersteigen.
- **Quellen:**
  - [WL ZH 2026 UJ S. 24](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0153.md) `zh-wl-2026-uj__c0153` – «allen unter Kolonne A angegebenen Erträgen die eidg. Verrechnungssteuer zu meinen oder zu Lasten der von mir vertretenen»
  - [WL ZH 2026 UJ S. 26–27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0169.md) `zh-wl-2026-uj__c0169` – «Die Totalbeträge des DA-1 übertragen Sie in die Zeile «Übertrag ab Formular DA-1» im»

## Hilfsblatt Liegenschaften

<a id="form-350-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 350 – Liegenschaftenverzeichnis: Steuerwert (Codes 5531ff / 5541ff), Eigenmietwert/Mietzinseinnahmen, Unterhalt (pauschal/effektiv), Nettoertrag aus Liegenschaften (Code 3953), Übertrag weitere Verzeichnisse (Code 578)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** 🟡 extrahiert
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Liegenschaftenbewertung 2026 der Gemeinde; Mieterspiegel; Unterhaltsrechnungen; Beiblatt zum Liegenschaftenverzeichnis
- **Regel:** Pro Liegenschaft (alle Liegenschaften, auch in anderen Kantonen und im Ausland) Steuerwert, Eigenmietwert bzw. Mieterträge, Unterhalt/Verwaltung (Pauschale oder effektiv) und verbleibenden Ertrag erfassen; Nettoertrag → Ziff. 6, Steuerwerte → Ziff. 31.1/31.2. Online-Steuererklärung überträgt die Totale automatisch.
- **Bemerkung:** korrigiert durch Prüfung: Zitate durch wörtliche Textstellen (Code 3953; Deklarationspflicht aller Liegenschaften) ersetzt. Detailregeln in c0172/c0173 bei Bedarf direkt prüfen.
- **Quellen:**
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0177.md) `zh-wl-2026-uj__c0177` – «Nettoertrag aus Liegenschaften 3953»
  - [WL ZH 2026 UJ S. 27](../../chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0173.md) `zh-wl-2026-uj__c0173` – «Es sind alle Liegenschaften zu deklarieren, auch jene in anderen Kantonen oder»
