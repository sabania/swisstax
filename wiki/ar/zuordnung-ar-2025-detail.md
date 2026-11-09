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

> **Hinweis:** Das AR-Formular hat keine separate Bundesspalte: Die Steuererklärung dient zugleich für die direkte Bundessteuer; Abweichungen (z.B. Zweiverdiener-, Versicherungs-, Kinderabzug Bund) werden von der Steuerverwaltung automatisch vorgenommen (WL AR 2025 S. 33, ar-wl-2025__c0179: «Anpassungen durch die Steuerverwaltung automatisch vorgenommen»).

## Personalien

<a id="seite-1-personalien"></a>
### Ziff. Seite 1 – Personalien, Berufs- und Familienverhältnisse, Dauer der Steuerpflicht, Kinder (Formular 1 Seite 1)

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 1 Seite 1 (Stammdaten, Erwerbsart, Kinder in Ihrem Haushalt, Unterhaltsbeiträge)
- **Rein:** Eingedruckte Stammdaten (Stand Ende Dezember) → nur Korrekturen eintragen · Beruf + überwiegende Erwerbsart; unselbständiger Hauptberuf → Arbeitgeber · Kinder, für deren Unterhalt zur Hauptsache aufgekommen wird (Vorname, Name, Geburtsjahr; Ausbildung: Schule/Lehrfirma + Dauer) → nur mit Abzug 23.1–23.3
- **Rechnen:** Alter am 31. Dezember → Kanton 23.1 (bis 4) 5'300 / 23.2 (4–15) 7'400 / 23.3 (ab 15, Ausbildung bis 26) 11'600; Bund 6'800 je Kind; minderjährig → 36.3 +25'000
- **Regel:** Personalien sind bei der Steuerverwaltung gespeichert (Stand Ende Dezember) und bereits eingedruckt; Korrekturen auf der Steuererklärung vornehmen. Beruf und überwiegende Erwerbsart immer angeben; bei unselbständigem Hauptberuf Arbeitgeber. Kinder nur aufführen, wenn Abzug 23.1-23.3 beansprucht wird (Geburtsjahr/Jahrgang bestimmt Abzugsstufe und Vermögensabzug 36.3); bei Kindern in beruflicher Ausbildung Schule/Lehrfirma und voraussichtliche Dauer.
- **Beachten:** Änderungen auch dem Einwohneramt melden – Vermerk auf der Steuererklärung ersetzt die Meldung nicht
- **Beachten:** Zuzug aus anderem Kanton 2025: ganzes Jahr AR (auch DBSt); Zuzug aus Ausland: Einkommen erst ab Zuzug
- **Beachten:** Wer für ein Kind Unterhaltsbeiträge nach Ziff. 12.2 abzieht, erhält dafür keinen Kinderabzug
- **Limiten:**
  - Kinderabzug Vorschulalter (CHF): Kanton **CHF 5'300 (Kinderabzug bis Vollendung des 4. Altersjahres: CHF 5'300 (indexiert per 1.1.2024).)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (sozialabzug.kind); Staffelung nach Alter nur kantonal.**
  - Kinderabzug Schulalter (CHF): Kanton **CHF 7'400 (Kinderabzug nach Vollendung des 4. bis Vollendung des 15. Altersjahres: CHF 7'400 (indexiert).)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (sozialabzug.kind).**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 11'600 (Kinderabzug nach 15. Altersjahr bis Volljährigkeit sowie volljährige Kinder in Ausbildung bis 26. Altersjahr: CHF 11'600 (indexiert).)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Kinderabzug CHF 6'800 wie für Minderjährige (kein höherer Ausbildungsabzug))**
  - Kinderabzug Grundbetrag (CHF): Kanton **n/a – AR staffelt den Kinderabzug nach Alter (sozialabzug.kind_vorschule/_schule/_ausbildung); kein einheitlicher Grundbetrag.** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 25'000 (Zusätzlich pro minderjähriges Kind mit Kinderabzug CHF 25'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Bemerkung:** Keine Codes im Formularraster Seite 1 verifiziert.
- **Quellen:**
  - [WL AR 2025 S. 6](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0024.md) `ar-wl-2025__c0024` – «Die Angaben zu den Berufsverhältnissen (Beruf und überwiegende Erwerbsart)»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0025.md) `ar-wl-2025__c0025` – «Es sind nur diejenigen Kinder aufzuführen, für die Sie einen Abzug in den Ziffern 23.1, 23.2 oder 23.3 geltend machen»
  - [WL AR 2025 S. 6](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0024.md) `ar-wl-2025__c0024` – «Ende Dezember gespeicherten Daten»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0025.md) `ar-wl-2025__c0025` – «Aufgrund des Jahrgangs der Kinder können die für minderjährige Kinder»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «Für jedes Kind bis zur Vollendung des 4. Altersjahrs»
  - [WL AR 2025 S. 6](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0024.md) `ar-wl-2025__c0024` – «Ein Vermerk auf der Steuer»
  - [WL AR 2025 S. 5](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0017.md) `ar-wl-2025__c0017` – «wohnten, sind Sie für das ganze Jahr in»
  - [WL AR 2025 S. 5–6](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0018.md) `ar-wl-2025__c0018` – «ist das tatsächliche, ab Zuzugsdatum bis Ende 2025 erzielte Einkommen»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0105.md) `ar-wl-2025__c0105` – «Der Kinderabzug entfällt für»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0025.md) `ar-wl-2025__c0025` – «Kinder, für deren Unterhalt Sie zur Hauptsache aufkommen»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «bis zur Vollendung des 26. Altersjahrs»

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Haupterwerb unselbständig, Person 1 (Code 100) / Person 2 (Code 102)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn/Rente)
- **Rein:** Lohnausweis (Formular 11) je Arbeitgeber → Nettolohn · Bescheinigung Vorsorgeeinrichtung (Formular 21) → nicht vom Lohn abgezogene BVG-Einkäufe (nicht hier, Ziff. 13.2)
- **Rechnen:** Σ Nettolohn Haupterwerb je Person = Bruttolohn − AHV/IV/EO/ALV/NBUV − BVG-Beiträge (gemäss Lohnausweisen)
- **Regel:** Nettolohn gemäss Lohnausweis einsetzen (Brutto abzüglich AHV/IV/EO/ALV/NBUV und BVG-Beiträge, WL AR c0035; im Lohnausweis Ziff. 11 = Brutto abzüglich Ziff. 9 und 10, Ziff. 10.2 = vom Lohn abgezogene Einkäufe). Lohnausweise lückenlos belegen (Ziffern 1-10 des Lohnausweises); pro Arbeitgeber grundsätzlich ein Lohnausweis. Spesenpauschalen müssen im Lohnausweis stehen. Vom Arbeitgeber getragene berufsorientierte Aus-/Weiterbildung ist nicht steuerbar (im Lohnausweis Ziff. 13.3). Nicht im Nettolohn abgezogene NBUV-/BVG-Beiträge: Ziff. 16.6. Berufskosten: Ziff. 10 (Form. 4). Ein BVG-Einkauf in Ziff. 10.2 des Lohnausweises ist bereits im Nettolohn abgezogen; selbst bezahlte (nicht vom Lohn abgezogene) Einkäufe bescheinigt die Vorsorgeeinrichtung separat mit Formular 21 EDP.
- **Beachten:** Je Arbeitgeber ein Lohnausweis (Ziff. 1–10 lückenlos); sonst Vermerk Ziff. 15 «Einer von xx Lohnausweisen»
- **Beachten:** Im Nettolohn nicht abgezogene NBUV-/BVG-Beiträge → Ziff. 16.6; Berufskosten → Ziff. 10 (Form. 4)
- **Beachten:** Pauschalspesen immer im Lohnausweis; vom Arbeitgeber getragene berufsorientierte Weiterbildung nicht steuerbar
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
  - [WL AR 2025 S. 3](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0008.md) `ar-wl-2025__c0008` – «(Formular 11) ist durch den»
  - [MB 21 EDP S. 2–3](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0006.md) `bund-mb-21edp__c0006` – «Lohn abgezogenen Beiträge nur im Formular 21 angegeben werden dürfen, nicht aber im»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0084.md) `ar-wl-2025__c0084` – «erbrachten Leistungen sowie Einkaufsbeiträge abziehbar»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0033.md) `ar-wl-2025__c0033` – «möglich, muss unter Ziffer 15»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0034.md) `ar-wl-2025__c0034` – «Insbesondere sind pauschale Spesenver»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Nebenerwerb unselbständig, Person 1 (Code 104) / Person 2 (Code 106), mit Art der Tätigkeit

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn) des Nebenarbeitgebers
- **Rein:** Lohnausweis Nebenarbeitgeber → Nettolohn · Hauswartung o.ä. mit Mietzinsreduktion → Differenz normaler − reduzierter Mietzins · Art der Nebenerwerbstätigkeit → Textfeld Ziff. 1.2
- **Rechnen:** Σ Nettolohn Nebenerwerb je Person; Form. 4 Ziff. 5.1: Nettolohn ≤ 800 → Auslagen bis Nettolohn, sonst min(max(20 % × Nettolohn; 800); 2'400); alternativ effektiv 5.2
- **Regel:** Nettolohn des zweiten Arbeitgebers; als Nebenerwerb gilt nur eine Tätigkeit neben einem Hauptberuf mit voller zeitlicher Beanspruchung für einen anderen Arbeitgeber. Berufskosten pauschal 20 % der Nettoeinkünfte (min. 800, max. 2'400) in Form. 4 Ziff. 5.1, alternativ tatsächliche Kosten (5.2). Mietzinsreduktion (z.B. Hauswart): Differenz zwischen normalem und reduziertem Mietzins als Einkommen deklarieren.
- **Beachten:** Nur neben vollem Hauptberuf bei anderem Arbeitgeber; ohne Haupterwerb bei Dritten (z.B. Pensionierte) kein Abzug
- **Beachten:** Pauschale Kanton = Bund (Art. 19 StV AR verweist auf die DBG-Pauschalansätze)
- **Beachten:** Alle Nebeneinkünfte angeben: Provisionen, Gutachten, Lehrtätigkeit, Buchhaltung, Hauswartung usw.
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
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0080.md) `ar-wl-2025__c0080` – «können bis zur Höhe des erzielten Nettolohns abgezogen werden, soweit die»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0080.md) `ar-wl-2025__c0080` – «Nebeneinkünfte netto Fr. 800.– nicht übersteigen. Übersteigt der Nettolohn»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0080.md) `ar-wl-2025__c0080` – «Steuerpflichtige Personen, die keine Haupterwerbstätigkeit bei Dritten»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0004.md) `ar-form-04-2025__c0004` – «5.2 Anstelle des Pauschalabzuges: tatsächliche Kosten»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0036.md) `ar-wl-2025__c0036` – «Anzugeben sind alle Einkünfte aus Nebenerwerbstätigkeit wie Vermittlungs»

<a id="1-3-einkommen-unselbstaendig-vr-honorare"></a>
### Ziff. 1.3 – Sitzungsgelder, VR-Honorare, Behördenentschädigungen, Person 1 (Code 108) / Person 2 (Code 110)

- **Schlüssel:** `einkommen.unselbstaendig.vr_honorare` (VR-Honorare, Sitzungsgelder, Tantiemen (wo separat ausgewiesen, z.B. SG/AR Ziff. 1.3)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 6 (Verwaltungsratsentschädigungen) bzw. Bescheinigung der Behörde/Gesellschaft
- **Rein:** Bescheinigung Behörde/Gemeinde → Sitzungs-, Taggelder, Pauschalspesen · Lohnausweis bzw. Bescheinigung der Gesellschaft → VR-Honorare, Tantièmen
- **Rechnen:** Σ Entschädigungen (soweit nicht in 1.1/1.2); Kanton: Nebenerwerbspauschale + Behördenabzug ≤ 2'600 (Beispiele MB 15); Bund: nur Pauschale 20 % (800–2'400)
- **Regel:** Nur soweit nicht bereits im Lohnausweis/Haupterwerb deklariert. Nebenamtliche Behördenmitglieder: zusätzlich zu den pauschalen Berufskosten bis max. Fr. 2'600 abziehbar (MB AR 15 Ziff. 3). Mit der Pauschale sind sämtliche Unkosten der Tätigkeit abgegolten; der Nachweis höherer effektiver Kosten bleibt vorbehalten.
- **Beachten:** Behördenabzug nur bei Behördenentschädigung ≤ 54'000 inkl. Pauschalspesen; darüber gilt Haupterwerb
- **Beachten:** Kein Abzug: Verwaltungsangestellte, Einsitz von Amtes wegen, Verbände/Vereine; ausserkantonale Behörde: Abzug möglich
- **Beachten:** VR-Tätigkeit: Nebenerwerbsabzug i.d.R. nicht zulässig (Unkosten meist zusätzlich vergütet)
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Nebenerwerb: Pauschalabzug 20 % der Nettoeinkünfte (WL: Nettolohn), mind. CHF 800, max. CHF 2'400 (DBG-Ansatz).)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge))**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Nebenerwerb Pauschale Minimum CHF 800.)** · Bund **CHF 800 (Minimum Pauschale Nebenerwerb)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Nebenerwerb Pauschale Maximum CHF 2'400.)** · Bund **CHF 2'400 (Maximum Pauschale Nebenerwerb)**
- **Bund:** Zusatzabzug Fr. 2'600 für nebenamtliche Behördenmitglieder gilt nicht für die direkte Bundessteuer.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Lohnausweis Ziff. 6 (VR-Entschädigungen) aus WL Lohnausweis 2026 (jahr_ok, Feldstruktur nicht für 2025 verifiziert); Behörden: Bescheinigung der Behörde.
- **Quellen:**
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0037.md) `ar-wl-2025__c0037` – «zusätzlich bis max. Fr. 2’600.– abgezogen werden (gilt nicht für die direkte Bundessteuer)»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0026.md) `ar-wl-2025__c0026` – «108 13213211»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0026.md) `ar-wl-2025__c0026` – «Bescheinigung 110 13213211»
  - [MB AR 15 S. 1](../../chunks/ar/dauernd/ar-mb-15/ar-mb-15__c0003.md) `ar-mb-15__c0003` – «Mit dem Abzug der Pauschale sind sämtliche Unkosten im Zusammenhang mit den erwähnten Tätigkeiten abgegolten.»
  - [WL Lohnausweis 2026 S. 13](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0030.md) `bund-wl-lohnausweis-2026__c0030` – «In diesem Feld sind alle Entschädigungen anzugeben, die einer Person in ihrer Eigenschaft»
  - [MB AR 15 S. 1](../../chunks/ar/dauernd/ar-mb-15/ar-mb-15__c0002.md) `ar-mb-15__c0002` – «Für die direkte Bundessteuer kann ein Pauschalabzug für gelegentlichen Nebenerwerb von 20% der»
  - [MB AR 15 S. 2](../../chunks/ar/dauernd/ar-mb-15/ar-mb-15__c0006.md) `ar-mb-15__c0006` – «Bei einer Behördenentschädigung von höchstens Fr. 54‘000 (inkl. Pauschalspesen) liegt ein»
  - [MB AR 15 S. 1](../../chunks/ar/dauernd/ar-mb-15/ar-mb-15__c0004.md) `ar-mb-15__c0004` – «die von Amtes wegen in solchen Behörden Einsitz nehmen»
  - [MB AR 15 S. 2](../../chunks/ar/dauernd/ar-mb-15/ar-mb-15__c0005.md) `ar-mb-15__c0005` – «Tätigkeiten bei Berufs- und Fachverbänden, gemeinnützigen Institutionen und Freizeitvereinen»
  - [MB AR 15 S. 3](../../chunks/ar/dauernd/ar-mb-15/ar-mb-15__c0009.md) `ar-mb-15__c0009` – «Das Merkblatt gilt auch für eine ausserkantonale nebenamtliche Behördentätigkeit.»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0080.md) `ar-wl-2025__c0080` – «Regel auch nicht zulässig für Einkünfte aus Verwaltungsratstätigkeit»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit (Industrie, Handel, Gewerbe, Landwirtschaft, freie Berufe, Internet-Plattformen), Person 1 (Code 112) / Person 2 (Code 114)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Jahresrechnung (Bilanz, Erfolgsrechnung, Eigenkapitalnachweis, Abschreibungstabelle) bzw. Einnahmen-Ausgaben-Rechnung
- **Rein:** Jahresrechnung (Bilanz, Erfolgsrechnung) der 2025 abgeschlossenen Geschäftsjahre → Reingewinn · Eigenkapitalkonti (Privatkonti) + Abschreibungstabellen → beilegen · Ohne Buchhaltung: Einnahmen-Ausgaben-Rechnung + Vermögensübersicht; Landwirte: Formular 12 oder 14
- **Rechnen:** Reingewinn ER (inkl. Privatanteile, Naturalbezüge) − darin enthaltene Familienzulagen AK (→ 3.5) − Erträge BG-Beteiligungen (→ 4.3)
- **Regel:** Reine Einkünfte nach Abzug der Gewinnungskosten, ermittelt nach den im Steuerjahr 2025 abgeschlossenen Bilanzen und Erfolgsrechnungen (Layout der WL teilweise verzerrt, c0039). Aufstellung über Aktiven und Passiven, Einnahmen und Ausgaben sowie Privatentnahmen/-einlagen beilegen (Jahresrechnung, Eigenkapitalkonti, Abschreibungstabellen). Privatanteil an Vorsorgebeiträgen (2. Säule, 3a) nicht in der Erfolgsrechnung, sondern ausschliesslich in Ziff. 13.2 bzw. 13.1; Kinderzulagen der Ausgleichskasse in Ziff. 3.5 (Reingewinn entsprechend kürzen).
- **Beachten:** Eigene BVG nur «Arbeitgeberanteil» in ER (ohne Personal: Hälfte); Rest + Säule 3a → 13.2/13.1; Einkäufe 100 % in 13.2
- **Beachten:** Privatanteil Heizung/Strom/Telefon u.a. (dem Betrieb belastet): 3'540/Jahr + 900 je weiteren Erwachsenen + 600 je Kind
- **Beachten:** EO Militär/Zivilschutz in der Jahresrechnung (nicht Ziff. 3.3); Geschäftsbelege zehn Jahre aufbewahren
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
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0039.md) `ar-wl-2025__c0039` – «eine Einnahmen-Ausgaben-Rechnung sowie»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0040.md) `ar-wl-2025__c0040` – «12 oder 14 ausgefüllt einzureichen.»
  - [WL AR 2025 S. 9](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0047.md) `ar-wl-2025__c0047` – «Ist kein solches Personal vorhanden, so gilt die Hälfte der Beiträge als»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0084.md) `ar-wl-2025__c0084` – «sind hier immer 100 % der Einkaufsbeiträge zu deklarieren»
  - [WL AR 2025 S. 9](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0044.md) `ar-wl-2025__c0044` – «Für Heizung, elektrischen Strom, Gas, Putzmaterial, Wäschereinigung, private»
  - [WL AR 2025 S. 9](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0045.md) `ar-wl-2025__c0045` – «Im Jahr   3’540.–   900.–   600.–»
  - [WL AR 2025 S. 9](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0046.md) `ar-wl-2025__c0046` – «da AHV-pflichtig, in der Jahresrechnung erfolgswirksam zu verbuchen und nicht»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0040.md) `ar-wl-2025__c0040` – «der selbständigen Tätigkeit in Zusammenhang stehen, sind während zehn Jahren»
  - [WL AR 2025 S. 11](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0057.md) `ar-wl-2025__c0057` – «(Code «BG» im Wertschriftenverzeichnis) ist der ausgewiesene Reingewinn um»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0054.md) `ar-wl-2025__c0054` – «Sind diese im Reingewinn aus selbständiger Er»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Kollektiv-, Kommanditgesellschaften und einfache Gesellschaften, Person 1 (Code 120) / Person 2 (Code 122)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Angaben/Bescheinigung der Gesellschaft (inkl. Kapitalerträge)
- **Rein:** Angaben der Firma (Kollektiv-/Kommanditgesellschaft) → Einkommensanteil inkl. Kapitalerträge · Abrechnung einfache Gesellschaft (z.B. Konsortium) → Anteil am Ergebnis · Formular 2 Seite 1 → Frage Beteiligung an Kollektiv-/Kommanditgesellschaft (Firma)
- **Rechnen:** Σ Einkommensanteile je Gesellschaft gemäss Angaben der Firma (inkl. Kapitalerträge), je Person
- **Regel:** Einkünfte aus Beteiligungen an Kollektiv-/Kommanditgesellschaften und einfachen Gesellschaften (Konsortium) hier angeben. Verrechnungssteueransprüche auf Kapitalerträgen von Kollektiv-/Kommanditgesellschaften nicht in den persönlichen Rückerstattungsantrag aufnehmen; Rückerstattung mit Formular 25 direkt bei der Eidg. Steuerverwaltung (die Gesellschaft macht den Anspruch selber geltend).
- **Beachten:** VSt auf Gesellschafts-Kapitalerträgen nicht im eigenen Form. 2 zurückfordern; Gesellschaft beantragt mit Form. 25 (ESTV)
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Die WL nennt für die Gesellschaftsangaben «Formular 10», in 2025 ist Formular 10 jedoch Kinderbetreuungskosten – Beleg sind die Angaben der Firma.
- **Quellen:**
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0038.md) `ar-wl-2025__c0038` – «sind ebenfalls unter Ziffer 2.2 aufzuführen»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0027.md) `ar-wl-2025__c0027` – «120 13213211»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0027.md) `ar-wl-2025__c0027` – «Kommandit- 122»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0004.md) `ar-form-02-2025__c0004` – «Rückerstattung der Verrechnungssteuer mit Formular 25 direkt bei der Eidg. Steuerverwaltung»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0131.md) `ar-wl-2025__c0131` – «hat die Gesellschaft selber den Rückerstattungsanspruch mit dem Antrags»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0038.md) `ar-wl-2025__c0038` – «Einkünfte aus einer Beteiligung an einer einfachen Gesellschaft (z.B.»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0004.md) `ar-form-02-2025__c0004` – «Sind Sie an einer Kollektiv- oder Kommanditgesellschaft beteiligt?»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0131.md) `ar-wl-2025__c0131` – «dürfen nicht in die persönlichen Rück»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV-/IV-Renten (zu 100 %), Person 1 (Code 126) / Person 2 (Code 128)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung der Ausgleichskasse (Jahresbetrag)
- **Rein:** Bescheinigung der Ausgleichskasse (AHV-/IV-Rente) → Jahresbetrag 2025 je Person
- **Rechnen:** 100 % × Σ ordentliche + ausserordentliche AHV-/IV-Renten je Person (Kanton = Bund, Art. 22 Abs. 1 DBG)
- **Regel:** Ordentliche und ausserordentliche AHV-/IV-Renten voll deklarieren. Ergänzungsleistungen sind nicht steuerbar (Unterstützungscharakter); Ziff. 8.3: Ergänzungsleistungen und Hilflosenentschädigungen sind steuerfrei, anzurechnen sind aber jene Ergänzungsleistungen, die zur Vergütung von Krankheits- und Behinderungskosten ausgerichtet werden.
- **Beachten:** Ergänzungsleistungen und Hilflosenentschädigung nicht hier: steuerfrei, nur Information Ziff. 8.2/8.3
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0049.md) `ar-wl-2025__c0049` – «Die ordentlichen und ausserordentlichen AHV- und IV-Renten sind in vollem Um»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0049.md) `ar-wl-2025__c0049` – «nicht aber die ordentlichen und ausserordentlichen Ergänzungsleistungen»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0027.md) `ar-wl-2025__c0027` – «Versic herungen 126 32132111»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Ergänzungsleistungen und Hilflosenentschädigungen sind steuerfrei.»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Anzurechnen sind aber jene Ergänzungsleistungen, die zur Ver»
  - [DBG Art. 22](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-22-t1.md) `bund-dbg-2025__art-22-t1` – «Steuerbar sind alle Einkünfte aus der Alters-, Hinterlassenen- und Invalidenversicherung»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Auch diese Angaben dienen Informationszwecken.»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten/Pensionen (2. Säule, Säule 3a, Unfall-/Haftpflichtversicherung, Leibrenten) mit steuerbarem Prozentsatz, Person 1 (Code 130) / Person 2 (Code 132)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Rentenbescheinigung der Vorsorgeeinrichtung/Versicherung (Rentenbescheinigung Formular 11 gemäss WL Lohnausweis/Rentenbescheinigung)
- **Rein:** Rentenbescheinigung Pensionskasse/früherer Arbeitgeber → Jahresrente 2. Säule · Bescheinigung Versicherung → Renten Säule 3a, Unfall-, Haftpflichtversicherung · Bescheinigung Versicherung (Leibrente 3b, VVG) → steuerbarer Ertragsanteil · Militärversicherung → Verfügung/Abrechnung beilegen
- **Rechnen:** Vorkolonne Betrag × steuerbarer % → Hauptkolonne; 2. Säule 80 %, wenn Beginn vor 31. Dezember 2001 + Vorsorge vor 1. Januar 1985 + ≥ 20 % Eigenbeiträge, sonst 100 %
- **Regel:** In der Vorkolonne vollen Betrag und Prozentsatz des steuerbaren Umfangs einsetzen (100 % in allen anderen Fällen; 80 % nur wenn die Rentenzahlung vor dem 31.12.2001 zu laufen begann, das Vorsorgeverhältnis vor dem 1.1.1985 bestand und der Versicherte mind. 20 % der Beiträge erbracht hat), Nettobetrag in die Hauptkolonne. Säule-3a-Renten 100 % steuerbar. Bei mehreren Renten Aufstellung beilegen. Leibrenten Säule 3b nach VVG: Ertragsanteil wird von der Versicherung bescheinigt; für privatrechtliche und ausländische Leibrenten siehe Ziff. 12.3.
- **Beachten:** 3a/Risikovers. 100 %; obl. Unfallvers. (NBU vor 1. Januar 1987): 80 % bei ≥ 20 % Eigenbeiträgen / 60 % alle selbst
- **Beachten:** Bund abweichend: Vorsorgeverhältnis per 31. Dezember 1986 + Beginn vor 1. Januar 2002 → drei/vier Fünftel (Art. 204 DBG)
- **Beachten:** Privatrechtliche/ausländische Leibrenten → Ertragsanteil Ziff. 12.3; mehrere Renten: Aufstellung beilegen
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Zuordnung 130/132 je Person aus Reihenfolge; Prozentfelder separat. «Formular 11» als Rentenbescheinigung: Bezeichnung aus WL Lohnausweis 2026 (jahr_ok), für 2025 nicht separat bestätigt.
- **Quellen:**
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0051.md) `ar-wl-2025__c0051` – «100 % in allen andern Fällen»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0050.md) `ar-wl-2025__c0050` – «Renten aus anerkannten Vorsorgeformen der Säule 3a 100 % steuerbar»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0027.md) `ar-wl-2025__c0027` – «130 gen. % sind beizule»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0051.md) `ar-wl-2025__c0051` – «des steuerbaren Ertragsanteils jährlich von der Versicherung bescheinigt.»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0052.md) `ar-wl-2025__c0052` – «ländischen Leibrenten wird auf Ziffer 12.3 verwiesen.»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «Wegleitung zum Ausfüllen des Lohnausweises bzw. der Rentenbescheinigung»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0050.md) `ar-wl-2025__c0050` – «wenn die Rentenzahlung vor dem 31. Dezember 2001 zu laufen»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0050.md) `ar-wl-2025__c0050` – «das Vorsorgeverhältnis vor dem 1. Januar 1985 bestanden hat»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0050.md) `ar-wl-2025__c0050` – «und der Versicherte mindestens 20 % der Beitragsleistungen erbracht»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0050.md) `ar-wl-2025__c0050` – «in der Vorkolonne mit dem»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0051.md) `ar-wl-2025__c0051` – «berufsunfalles ausgerichtet wird und die versicherte Person die»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0052.md) `ar-wl-2025__c0052` – «Renten aus reinen Risikoversicherungen (u.a. Erwerbsausfallversicherungen)»
  - [DBG Art. 204](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-204.md) `bund-dbg-2025__art-204` – «Vorsorgeverhältnis beruhen, das am 31. Dezember 1986 bereits bestand, sind wie folgt steuerbar»
  - [DBG Art. 204](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-204.md) `bund-dbg-2025__art-204` – «die vor dem 1. Januar 2002 zu laufen beginnen oder fällig werden»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0049.md) `ar-wl-2025__c0049` – «einschliesslich der vom früheren Arbeitgeber ausgerichteten»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0051.md) `ar-wl-2025__c0051` – «tens 20 % der Beitragsleistungen erbracht hat;»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigungen, Taggelder aus Kranken-, Unfall-, Invalidenversicherung, Mutterschaftsentschädigung (nicht im Lohnausweis), Person 1 (Code 134) / Person 2 (Code 136)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Taggeldabrechnung/Bescheinigung der Versicherung bzw. Ausgleichskasse
- **Rein:** Taggeldabrechnung Kranken-/Unfall-/IV-Versicherung → Taggelder 2025 (soweit nicht im Lohnausweis) · EO-Abrechnung Militär/Zivilschutz, Mutterschaftsentschädigung → soweit nicht im Lohnausweis
- **Rechnen:** Σ Taggelder + EO + Mutterschaftsentschädigung − bereits im Lohnausweis enthaltene; je Person
- **Regel:** Nur soweit nicht im Lohnausweis enthalten. IV-Taggelder sind steuerbar. Damit zusammenhängende selbst getragene Krankheits-/Behinderungskosten über Formular 6 (Ziff. 21.1/21.2).
- **Beachten:** Selbständige: EO Militär/Zivilschutz in der Jahresrechnung verbuchen, nicht hier
- **Beachten:** Nicht anzugeben: Unterstützungen bei Bedürftigkeit, IV-Kostenbeiträge (Eingliederung, Hilfsmittel, Sonderschulung)
- **Beachten:** Selbst getragene Krankheits-/Behinderungskosten → Form. 6, Ziff. 21.1/21.2
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Codes 134/136 durch Reihenfolge (Miniatur stark verzerrt); Quelle für Code ist nur die Reihenfolge der Codes 126-146.
- **Quellen:**
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0053.md) `ar-wl-2025__c0053` – «IV-Taggelder gehören zum steuerbaren Einkommen und sind unter Ziffer 3.3»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0053.md) `ar-wl-2025__c0053` – «wie Mutterschaftsentschädigung sind unter Ziffer 3.3 insoweit anzugeben, als sie»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0028.md) `ar-wl-2025__c0028` – «211 134 321321 1»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0028.md) `ar-wl-2025__c0028` – «136 Aufstellung»
  - [WL AR 2025 S. 9](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0046.md) `ar-wl-2025__c0046` – «separat unter Ziffer 3.3 zu deklarieren.»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0053.md) `ar-wl-2025__c0053` – «Nicht anzugeben sind»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0053.md) `ar-wl-2025__c0053` – «für Hilfsmittel, für Sonder»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0053.md) `ar-wl-2025__c0053` – «ten können im Formular 6 deklariert und unter Ziffer 21.1 bzw. 21.2 in Abzug»

<a id="3-4-einkommen-ersatz-taggelder"></a>
### Ziff. 3.4 – Arbeitslosentaggelder (nicht im Lohnausweis), Person 1 (Code 138) / Person 2 (Code 140)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Arbeitslosenkasse
- **Rein:** Bescheinigung der Arbeitslosenkasse → ausbezahlte ALV-Taggelder 2025 (nicht im Lohnausweis)
- **Rechnen:** Σ ALV-Taggelder − vom Arbeitgeber im Lohnausweis bescheinigte; je Person
- **Regel:** Nur Taggelder, die nicht vom Arbeitgeber im Lohnausweis bescheinigt sind; Bescheinigung der Arbeitslosenkasse beilegen.
- **Beachten:** Über nicht im Lohnausweis aufgeführte Bezüge Bescheinigung der Arbeitslosenkasse beilegen
- **Beachten:** Überbrückungsleistungen für ältere Arbeitslose ≠ ALV-Taggeld: steuerfrei, nur Information Ziff. 8.4
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Codes 138/140 durch Reihenfolge abgeleitet.
- **Quellen:**
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0053.md) `ar-wl-2025__c0053` – «Taggelder aus Arbeitslosenversicherung sind insoweit anzugeben, als sie nicht»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0028.md) `ar-wl-2025__c0028` – «2 138 321321 1»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0053.md) `ar-wl-2025__c0053` – «Über nicht im Lohnausweis aufgeführte Bezüge ist eine»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Steuerfrei sind Einkünfte aus Überbrückungsleistungen für ältere Arbeitslose»

<a id="3-5-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.5 – Von Ausgleichskassen direkt ausbezahlte Kinder- und Familienzulagen (Code 142)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Familienausgleichskasse
- **Rein:** Bescheinigung der Familienausgleichskasse → direkt ausbezahlte Kinder-/Familienzulagen 2025
- **Rechnen:** Σ direkt von Ausgleichskassen ausbezahlte Kinder-/Familienzulagen (nicht über den Arbeitgeber)
- **Regel:** Nur direkt von der Ausgleichskasse ausbezahlte Zulagen; im Lohnausweis bereits enthaltene Zulagen nicht doppelt erfassen; bei Selbständigen Reingewinn entsprechend kürzen.
- **Beachten:** Über den Arbeitgeber ausbezahlte Zulagen sind Lohnbestandteil (Lohnausweis, Ziff. 1.1) – nicht doppelt erfassen
- **Beachten:** Selbständige: Zulagen (nicht AHV-pflichtig) hier deklarieren, Reingewinn Ziff. 2 entsprechend kürzen
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Code 142 durch Reihenfolge abgeleitet.
- **Quellen:**
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0054.md) `ar-wl-2025__c0054` – «Kinder- und Familienzulagen, die von Ausgleichskassen direkt ausbezahlt wurden,»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0028.md) `ar-wl-2025__c0028` – «Taggelder n-Taggelde 142»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0032.md) `ar-wl-2025__c0032` – «wie Familien- und Kinderzulagen, Provisionen, Zulagen und Entschädigungen»
  - [WL AR 2025 S. 9](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0046.md) `ar-wl-2025__c0046` – «(Haushaltungs- und Kinderzulagen) sind, da nicht AHV-pflichtig, unter Ziffer 3.5»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0035.md) `ar-wl-2025__c0035` – «Die Einkünfte aus der Haupt»

<a id="4-1-einkommen-wertschriften"></a>
### Ziff. 4.1 – Erträge aus Wertschriften und Guthaben inkl. Lotterie-/Geldspielgewinne (Code 146), Übertrag Formular 2

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 Total Bruttoertrag A+B abzüglich Geschäftswertschriften (G) und Beteiligungserträge (BP, BG); Steuerauszug (eCH-0196)/Bankbescheinigungen
- **Rein:** Steuerauszug/Bankbescheinigungen → Bruttoerträge 2025 Spalte A (mit VSt) bzw. B (ohne VSt), Form. 2 · Zins-/Saldomeldungen Konten → Bruttozins (Kundenguthaben ≤ 200 Zins: Spalte B) · Ausländische Titel: Bankabrechnungen → Bruttoertrag in CHF vor Quellensteuer (Form. 2 bzw. DA-1) · Lotto-/Totobescheinigungen, Kryptowährungen → Form. 2
- **Rechnen:** Form. 2: (Total A + B) − G − BP (→ 4.2) − BG (→ 4.3) = Ziff. 4.1; VSt-Anspruch = 35 % × Total A
- **Regel:** Bruttoerträge 2025 nach Fälligkeit (Dividenden: Fälligkeitsdatum) im Wertschriftenverzeichnis; Total A+B abzüglich G, BP (-> Ziff. 4.2) und BG (-> Ziff. 4.3) in Ziff. 4.1. Kundenguthaben bis Fr. 200 Bruttozins je Kalenderjahr: Spalte B (ohne Verrechnungssteuer). Kryptowährungen sind im Wertschriften- und Guthabenverzeichnis anzugeben (inkl. Bitcoin, Ether etc.). Spielgewinne: einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen erst soweit > Fr. 1 Mio. steuerbar, aus Verkaufsförderungs-Lotterien erst wenn > Fr. 1'000; Gewinne aus Spielen mit ausschliesslicher Gratisteilnahme und aus ausländischen Spielen sind vollumfänglich steuerbar.
- **Beachten:** Gross-/Online-Spiele: steuerbar soweit > Kanton 1 Mio. / Bund 1'070'400; Verkaufsförderung ganz, wenn > 1'000 / 1'100
- **Beachten:** Dividenden nach Fälligkeitsdatum; Thesaurierungsfonds: auch zurückbehaltene Erträge; keine selbst errechneten Zinsen
- **Beachten:** DA-1: Erträge mit Anrechnung ausl. Quellensteuern; Gewinne aus Gratis- bzw. ausländischen Spielen voll steuerbar
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
  - [WL AR 2025 S. 24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0138.md) `ar-wl-2025__c0138` – «Für Dividenden ist das Fälligkeitsdatum und nicht das Geschäftsjahr»
  - [WL AR 2025 S. 24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0139.md) `ar-wl-2025__c0139` – «als auch die zurückbehaltenen Erträge von Wertzuwachs- bzw. Thesaurie»
  - [WL AR 2025 S. 23–24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0136.md) `ar-wl-2025__c0136` – «Selbst errechnete Zinsen dürfen nicht eingetragen werden.»
  - [WL AR 2025 S. 25](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0144.md) `ar-wl-2025__c0144` – «ertrag in Schweizer Franken, vor Abzug von Quellensteuern und Kommissionen.»
  - [WL AR 2025 S. 25](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0144.md) `ar-wl-2025__c0144` – «geltend gemacht werden kann, sind im Formular DA-1 aufzuführen.»
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A)»
  - [DBG Art. 24](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-24-t3.md) `bund-dbg-2025__art-24-t3` – «die einzelnen Gewinne bis zum Betrag von 1 070 400 Franken aus der Teilnahme an Grossspielen»
  - [DBG Art. 24](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-24-t3.md) `bund-dbg-2025__art-24-t3` – «sofern die Grenze von 1100 Franken nicht überschritten wird»
  - [WL AR 2025 S. 24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0138.md) `ar-wl-2025__c0138` – «Gewinne aus ausländischen Spielen sind ebenfalls vollum»

<a id="4-2-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.2 – Erträge aus Beteiligungen ab 10 % (Privatvermögen, Code BP) (Code 147)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2: Erträge mit Code BP (Übertrag ohne Vorzeichen)
- **Rein:** Form. 2: Erträge Code BP (Privatbeteiligung mind. 10 %) → Übertrag ohne Vorzeichen · Steuerauszug/Dividendenabrechnung → Bruttoausschüttung der Beteiligung
- **Rechnen:** Ziff. 4.2 = Σ Bruttoerträge Code BP (voll); Teilbesteuerung über Abzug Ziff. 16.7: steuerbar Kanton 60 % / Bund 70 %
- **Regel:** Ausschüttungen von Schweizer Kapitalgesellschaften/Genossenschaften bei Beteiligung von mind. 10 % werden nur zu 60 % besteuert; der Teilbesteuerungsabzug (40 %) steht in Ziff. 16.7. Brutto-Ertrag hier ohne Vorzeichen eintragen.
- **Beachten:** Voraussetzung: ≥ 10 % am Grund-/Stammkapital (Art. 23 Abs. 1bis StG AR / Art. 20 Abs. 1bis DBG)
- **Beachten:** Bund-Abweichung (70 %) passt die Steuerverwaltung bei der DBSt automatisch an
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 11](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0057.md) `ar-wl-2025__c0057` – «Sitz in der Schweiz werden nur zu 60 Prozent besteuert, wenn die steuerpflich»
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «Abzüglich Erträge aus Privatbeteiligung (BP) Übertrag in Steuererkl. Ziff. 4.2 (ohne Vorzeichen)»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0029.md) `ar-wl-2025__c0029` – «147 13213211»
  - [StG AR Art. 23](../../chunks/ar/2025/ar-stg/ar-stg__art-23-t3.md) `ar-stg__art-23-t3` – «sind im Umfang von 60 Prozent steuerbar, wenn diese Beteiligungsrechte mindestens 10 Prozent des Grund- oder Stammkapitals»
  - [DBG Art. 20](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-20-t3.md) `bund-dbg-2025__art-20-t3` – «sind im Umfang von 70 Prozent steuerbar, wenn diese Beteiligungsrechte mindestens 10 Prozent des Grund- oder Stammkapitals»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0095.md) `ar-wl-2025__c0095` – «Teilbesteuerungsverfahren kann auf der Seite 3, Ziffer 16.7, in Abzug gebracht»
  - [WL AR 2025 S. 33](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0179.md) `ar-wl-2025__c0179` – «Anpassungen durch die Steuerverwaltung automatisch vorgenommen.»

<a id="4-3-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.3 – Erträge aus Beteiligungen ab 10 % (Geschäftsvermögen, Code BG) (Code 149)

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 2: Erträge mit Code BG; Jahresrechnung
- **Rein:** Form. 2: Erträge Code BG (Geschäftsbeteiligung mind. 10 %) → Übertrag ohne Vorzeichen · Jahresrechnung → im Reingewinn verbuchter Beteiligungsertrag (Kürzung Ziff. 2)
- **Rechnen:** Reingewinn Ziff. 2 − BG-Ertrag; Ziff. 4.3 = BG-Ertrag; steuerbar nach zurechenbarem Aufwand Kanton 60 % / Bund 70 % (Art. 21b StG / Art. 18b DBG)
- **Regel:** Beteiligung gehört zum Geschäftsvermögen: ausgewiesenen Reingewinn (Ziff. 2) um diesen Betrag kürzen und hier deklarieren (sonst Doppelbesteuerung); kein Abzug Teilbesteuerung 16.7.
- **Beachten:** Ohne Kürzung + Deklaration in 4.3: Doppelbesteuerung, keine Berücksichtigung beim Teilbesteuerungsabzug 16.7
- **Beachten:** Teilbesteuerung auch auf Veräusserungsgewinnen, wenn Beteiligung mindestens ein Jahr im Eigentum
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 11](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0057.md) `ar-wl-2025__c0057` – «Gehört eine solche Beteiligung zum Geschäftsvermögen selbständig Erwerbender»
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «Abzüglich Erträge aus Geschäftsbeteiligung Übertrag in Steuererkl. Ziff. 4.3 (ohne Vorzeichen)»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0029.md) `ar-wl-2025__c0029` – «n) 149 13213211»
  - [StG AR Art. 21b](../../chunks/ar/2025/ar-stg/ar-stg__art-21b.md) `ar-stg__art-21b` – «nach Abzug des zurechenbaren Aufwandes im Umfang von 60 Prozent steuerbar»
  - [DBG Art. 18b](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-18b.md) `bund-dbg-2025__art-18b` – «nach Abzug des zurechenbaren Aufwandes im Umfang von 70 Prozent steuerbar»
  - [StG AR Art. 21b](../../chunks/ar/2025/ar-stg/ar-stg__art-21b.md) `ar-stg__art-21b` – «wenn die veräusserten Beteiligungsrechte mindestens ein Jahr im Eigentum»
  - [WL AR 2025 S. 11](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0057.md) `ar-wl-2025__c0057` – «ansonsten eine doppelte Besteuerung resultiert und nicht für den Abzug Teil»

<a id="5-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. 5 – Ertrag aus Liegenschaften: Eigenmietwert (abzüglich 20 % Selbstnutzungsabzug) und Mietertrag (Code 712), Übertrag Formular 7/7Z

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Formular 7 Abschn. B (Total Erträge a. und b.) bzw. Formular 7Z Spalte B
- **Rein:** Amtliche Grundstückschätzung → Mietwert (Eigenmietwert), Form. 7 B a. · Mietverträge/Aufstellung → Miet-/Pachtzinsen ohne Nebenkosten, Form. 7 B b. · PV-Abrechnung → Einspeisevergütung − Eigenverbrauch (Leistungen Dritter) · Mehrere Liegenschaften → je Form. 7, Total Form. 7Z Spalte B
- **Rechnen:** Σ je Form. 7: Mietwert (− 20 % bei dauernd selbst bewohnter Wohnsitzliegenschaft) + Netto-Mietzinsen + Leistungen Dritter → Ziff. 5
- **Regel:** Eigenmietwert = Mietwert gemäss amtlicher Grundstückschätzung; Selbstnutzungsabzug 20 % nur auf der am Wohnsitz dauernd selbst bewohnten Liegenschaft (nicht Zweit-/Ferienwohnung, nicht Landwirtschaft). Fremdnutzung: Mietzinsen ohne Nebenkosten (Netto-Mietzins), Leistungen Dritter und PV-Einspeisevergütung (netto nach Eigenverbrauch). Mehrere Liegenschaften: je Form. 7, Zusammenzug in Form. 7Z.
- **Beachten:** Kein 20 %-Abzug: Zweit-/Ferienwohnung, Landwirtschaft; Vorzugsmiete an Nahestehende: voller Mietwert
- **Beachten:** Nicht erfasste Um-/Anbauten: Zuschlag 2.8 % der Aufwendungen; nur Privatvermögen (Geschäft → Ziff. 2)
- **Beachten:** Bund: Eigenmietwert nach ortsüblichen Verhältnissen (Art. 21 Abs. 2 DBG); DBSt-Abweichungen passt die StV automatisch an
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **20 % (Selbstnutzungsabzug 20 % auf dem Eigenmietwert; nur auf der am Wohnsitz dauernd selbst bewohnten Liegenschaft.)** · Bund **n/a – Eigenmietwert wird nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt (Art. 21 Abs. 2 DBG); Abschaffung per 01.01.2029 beschlossen, 2025–2028 gilt bisheriges Recht. Der Eigenmietwert für die direkte Bundessteuer wird im kantonalen Veranlagungsverfahren festgesetzt; ein dort vorgesehener Abzug für die DBSt (z.B. TG 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Bund:** Eigenmietwert/Selbstnutzungsabzug: Behandlung bei der direkten Bundessteuer nicht aus AR-Quellen belegt - Bund-Wegleitung/ESTV-Quellen prüfen.
- **Bemerkung:** Code 712 laut Miniatur (Zeile Ertrag aus Liegenschaften).
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0002.md) `ar-form-07-2025__c0002` – «Übertrag in die Steuererklärung Seite 2 Ziffer 5»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0166.md) `ar-wl-2025__c0166` – «entspricht dem massgeblichen Mietwert abzüglich 20 Prozent»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0167.md) `ar-wl-2025__c0167` – «Miet- und Pachtzinsen bei Fremd- nutzung ohne Nebenkosten (Netto-Mietzins)»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0166.md) `ar-wl-2025__c0166` – «wie Zweit- und Ferienwohnungen entfällt der Abzug.»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0166.md) `ar-wl-2025__c0166` – «nahestehenden Person überlassen wird (Vorzugsmiete).»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0166.md) `ar-wl-2025__c0166` – «2.8 Prozent der Aufwendungen berücksichtigt.»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0167.md) `ar-wl-2025__c0167` – «Einspeisevergütungen für Photovoltaikanlagen sind steuerbar.»
  - [Formular 7Z AR 2025 S. 1](../../chunks/ar/2025/ar-form-07z-2025/ar-form-07z-2025__c0001.md) `ar-form-07z-2025__c0001` – «Bei Besitz von mehr als einer Liegenschaft sind die einzelnen Ergebnisse je Liegenschaft»
  - [WL AR 2025 S. 11](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0058.md) `ar-wl-2025__c0058` – «Anzugeben sind die Einkünfte aus Liegenschaften des Privatvermögens.»
  - [DBG Art. 21](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-21.md) `bund-dbg-2025__art-21` – «Die Festsetzung des Eigenmietwertes erfolgt unter Berücksichtigung der ortsüblichen Verhältnisse»
  - [WL AR 2025 S. 33](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0179.md) `ar-wl-2025__c0179` – «Anpassungen durch die Steuerverwaltung automatisch vorgenommen.»

<a id="6-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 6.1 – Erhaltene Unterhaltsbeiträge: für geschiedene/getrennt lebende Person (Code 154); für minderjährige Kinder (Code 156)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil bzw. Vereinbarung und Zahlungsnachweise
- **Rein:** Scheidungsurteil/Trennungsvereinbarung → periodische Alimente für sich (Code 154) · Scheidungsurteil/Unterhaltsvereinbarung → Kinderalimente für minderjährige Kinder unter Sorge/Obhut (Code 156) · Zahlungsnachweise → 2025 erhaltene Beträge
- **Rechnen:** Σ erhaltene periodische Unterhaltsbeiträge für sich + Σ für minderjährige Kinder (Kanton = Bund, Art. 23 lit. f DBG)
- **Regel:** Periodische Alimente für sich und Kinderalimente für unter Sorge/Obhut stehende minderjährige Kinder sind beim Empfänger steuerbar (Gegenstück beim Zahlenden: Ziff. 12.1/12.2). Wer Kinderalimente erhält, macht für dieses Kind keinen Kinderabzug geltend, wenn der Zahlende den Abzug nach Ziff. 12.2 beansprucht.
- **Beachten:** Unterhalt an volljährige Kinder: beim Empfänger unbesteuert (Zahlender ohne Abzug)
- **Beachten:** Gegenstück beim Zahlenden: Ziff. 12.1/12.2; wer 12.2 abzieht, verliert für dieses Kind die Kinderabzüge 23.1–23.3
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Zuordnung 154 = geschiedene/getrennte Person, 156 = minderjährige Kinder aus Reihenfolge abgeleitet.
- **Quellen:**
  - [WL AR 2025 S. 11–12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0060.md) `ar-wl-2025__c0060` – «sind bei der empfangenden Person steuerbar und daher»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0029.md) `ar-wl-2025__c0029` – «154 32132111»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0030.md) `ar-wl-2025__c0030` – «nfte iedene oder 156»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «Unterhaltsbeiträge, die an ein volljähriges Kind bezahlt werden»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «sie beim Empfänger unbesteuert.»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «Unterhaltsbeiträge an die geschiedene, gerichtlich oder tatsächlich»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «entfallen die Kinderabzüge»
  - [DBG Art. 23](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-23.md) `bund-dbg-2025__art-23` – «Unterhaltsbeiträge, die ein Elternteil für die unter seiner elterlichen Sorge stehenden Kinder erhält»

<a id="6-2-einkommen-erbschaften-unverteilt"></a>
### Ziff. 6.2 – Ertrag aus unverteilten Erbschaften (Code 158)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung des Erbenvertreters/Erbteilung, Inventar und Erbenverzeichnis
- **Rein:** Aufstellung Erbenvertreter → detaillierte Erträge der Erbschaft 2025, eigener Anteil · Kopie Inventar + Erbenverzeichnis → beilegen; Form. 2 S. 1 Code 961 (Erbanteil ohne Liegenschaften) · Zins-/Dividendenabrechnungen → anteilige Bruttoerträge im persönlichen Form. 2 (VSt-Rückforderung)
- **Rechnen:** Ziff. 6.2 = Erbanteil × Erträge der unverteilten Erbschaft (Fälligkeiten Todestag bis Erbteilung); Vermögensanteil → Ziff. 30.5
- **Regel:** Einkünfte unverteilter Erbschaften werden anteilig bei den Erben besteuert; detaillierte Aufstellung beilegen; Beteiligung zusätzlich im Wertschriftenverzeichnis (Form. 2 S. 1, Code 961) und Vermögensanteil in Ziff. 30.5. Zwischen Todestag und Erbteilung fällige Erträge anteilig hier.
- **Beachten:** Anteilige Besteuerung bei den Erben gilt auch für unverteilte ausserkantonale Vermögensmassen
- **Beachten:** Liegenschaften der Erbschaft nicht im Form. 2, sondern im Form. 7 deklarieren
- **Beachten:** Nach Erbteilung: Titel im Form. 2 Spalte 1 mit «E» bezeichnen; Kopie der Erbteilung zwingend beilegen
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0061.md) `ar-wl-2025__c0061` – «6.2 Einkünfte aus unverteilten Erbschaften und andern Vermögensmassen werden»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0030.md) `ar-wl-2025__c0030` – «158 321321 1»
  - [WL AR 2025 S. 25](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0143.md) `ar-wl-2025__c0143` – «beim Einkommen unter Ziffer 6.2, Ertrag aus unverteilter Erbschaft»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «(Kopie Inventar und Erbenverzeichnis beilegen)»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «sind im Liegenschaftsformular 7 zu deklarieren.»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0132.md) `ar-wl-2025__c0132` – «Dazu sind die anteiligen Bruttoerträge nach Massgabe seines Anteils an der»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0132.md) `ar-wl-2025__c0132` – «Der Anteil der unverteilten»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0061.md) `ar-wl-2025__c0061` – «gilt auch für unverteilte ausserkantonale Vermögensmassen.»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0130.md) `ar-wl-2025__c0130` – «Bei einer verteilten Erbschaft ist uns zwingend eine Kopie»
  - [WL AR 2025 S. 25](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0143.md) `ar-wl-2025__c0143` – «Spalte 1 mit «E» bzw. «S» zu»

<a id="6-3-einkommen-uebrige"></a>
### Ziff. 6.3 – Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen, nicht verrechnete Förderbeiträge) mit Art (Code 162)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Mitarbeiterbeteiligung (Mitarbeiteraktien, Optionen, Anwartschaften/RSU, Beiblatt zum Lohnausweis), Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Aufstellung der Einkünfte; Mitarbeiterbeteiligungs-Bescheinigung
- **Rein:** Abrechnungen/Aufstellung → Provisionen, Trinkgelder (soweit nicht im Lohnausweis) · Bescheinigung Arbeitgeber → Einkünfte aus Mitarbeiterbeteiligungen · Abrechnungen Urheberrechte, Patente, Lizenzen, Konzessionen → Erträge · Förderbeitrag-Abrechnung (Energie/Umwelt) → im Vorjahr nicht mit Unterhalt verrechneter Beitrag
- **Rechnen:** Σ übrige Einkünfte mit Art, soweit nicht bereits in Ziff. 1 bis 6.2 enthalten
- **Regel:** Nur soweit nicht bereits in Ziff. 1-6.2 enthalten. Förderbeiträge/Subventionen, die im Vorjahr nicht mit dem Liegenschaftsunterhalt verrechnet werden konnten, sind hier anzugeben.
- **Beachten:** Förderbeiträge, die erst in der Folgeperiode vergütet werden → hier; sonst Aufwandminderung im Form. 7
- **Beachten:** Mitarbeiteraktien/-optionen: Bescheinigung des Arbeitgebers beilegen
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0061.md) `ar-wl-2025__c0061` – «6.3 Zu den übrigen Einkünften gehören beispielsweise Provisionen, Trinkgelder, Ein»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0030.md) `ar-wl-2025__c0030` – «162 321321 1»
  - [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0172.md) `ar-wl-2025__c0172` – «sind die Leistungen unter übrige Einkünfte (Ziffer 6.3) zu deklarieren.»
  - [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0172.md) `ar-wl-2025__c0172` – «Die erhaltenen Förderbeiträge sind als Aufwandminderung im»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0130.md) `ar-wl-2025__c0130` – «Bei Mitarbeiteraktien und -optionen muss die vom Arbeitgeber ausgestellte»

<a id="6-4-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 6.4 – Kapitalabfindungen für wiederkehrende Leistungen mit Anzahl Jahre (Code 164)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der auszahlenden Stelle
- **Rein:** Bescheinigung der auszahlenden Stelle → Auszahlungsbetrag + Anzahl Jahre, für die die Leistung ausgerichtet wird
- **Rechnen:** Betrag voll in 6.4 (+ Anzahl Jahre); Satz = Satz einer entsprechenden jährlichen Leistung zusammen mit übrigen Einkünften; Kanton = Bund (Art. 37 DBG)
- **Regel:** Auszahlungsbetrag und Anzahl Jahre einsetzen; Besteuerung zusammen mit den übrigen Einkünften zum Satz, der sich bei einer entsprechenden jährlichen Leistung ergäbe. Kapitalleistungen aus Vorsorge gehören nicht hierher, sondern auf Seite 4 (Ziff. 40/41).
- **Beachten:** Kapitalleistungen aus Vorsorge nicht hier → Seite 4 der Steuererklärung
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0062.md) `ar-wl-2025__c0062` – «6.4 Die Kapitalabfindungen für wiederkehrende Leistungen sind mit dem Auszah»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0030.md) `ar-wl-2025__c0030` – «Jahre 164 321321»
  - [DBG Art. 37](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-37.md) `bund-dbg-2025__art-37` – «zu dem Steuersatz berechnet, der sich ergäbe, wenn anstelle der einmaligen Leistung eine entsprechende jährliche Leistung ausgerichtet würde»

## Einkommensberechnung

<a id="7-berechnung-total"></a>
### Ziff. 7 – Total der Einkünfte (Code 168)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 1-6)
- **Rein:** Übertrag Hauptkolonne Ziff. 1 bis 6.4 (Person 1 und 2)
- **Rechnen:** Σ Ziff. 1 bis 6.4 (Hauptkolonne); ohne Ergänzende Angaben Ziff. 8 und ohne Kapitalleistungen aus Vorsorge (Seite 4)
- **Regel:** Summe der Einkünfte Ziff. 1.1-6.4; nicht enthalten sind Ergänzende Angaben (Ziff. 8) und Kapitalleistungen aus Vorsorge (Ziff. 40/41).
- **Beachten:** Ziff. 8 dient nur Informationszwecken – nicht addieren
- **Beachten:** Gesamtes in-/ausländisches Einkommen inkl. minderjährige Kinder unter Sorge/Obhut, ausser deren Erwerbseinkommen
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Textliche Bezeichnung «Total der Einkünfte» im Raster stark zerlegt (nur Code und Raster-Kontext belegt).
- **Quellen:**
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0030.md) `ar-wl-2025__c0030` – «168 e Einkünfte»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0061.md) `ar-wl-2025__c0061` – «soweit sie nicht bereits in den Ziffern 1 bis»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0063.md) `ar-wl-2025__c0063` – «Diese Angabe dient Informationszwecken.»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0062.md) `ar-wl-2025__c0062` – «sind auf Seite 4 der Steuer»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0028.md) `ar-wl-2025__c0028` – «Der Steuerpflicht unterliegt das gesamte in- und ausländische Einkommen der»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0031.md) `ar-wl-2025__c0031` – «Minderjährige Kinder werden für Einkommen aus Erwerbs-»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0029.md) `ar-wl-2025__c0029` – «und der unter elterlicher Sorge oder Obhut stehenden minderjährigen Kinder.»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0031.md) `ar-wl-2025__c0031` – «tätigkeit selbständig besteuert.»

<a id="18-berechnung-total"></a>
### Ziff. 18 – Total der Abzüge (Zeile nach Ziff. 17)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeile
- **Rein:** Übertrag Abzüge Ziff. 10.1 bis 17 (Seite 3)
- **Rechnen:** Σ Abzüge Ziff. 10.1 bis 17
- **Regel:** Summe der Abzüge Ziff. 10-17.
- **Beachten:** Abzüge Ziff. 21 (Krankheit, Behinderung, Zuwendungen) erst vom Nettoeinkommen Ziff. 20
- **Bemerkung:** Ziffer/Code in den AR-Quellen nicht belegt (konkordanz-CSV nennt 18/Code unverifiziert); Rechenlogik: Art. 28 StG (Einkünfte abzüglich Abzüge Art. 29-36). Geprüft: weiterhin offen; im Formular/in der WL ist Ziff. 18 nicht belegt, nur die Rechenlogik (Art. 28 Abs. 1 StG).
- **Quellen:**
  - [StG AR Art. 28](../../chunks/ar/2025/ar-stg/ar-stg__art-28.md) `ar-stg__art-28` – «werden von den gesamten steuerbaren Einkünften die Aufwendungen und allgemeinen Abzüge gemäss Art. 29–36 abgezogen»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0004.md) `ar-form-04-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 10.1»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) `ar-wl-2025__c0004` – «17. Zweiverdiener Bei gemeinsamer Steuerpflicht»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0098.md) `ar-wl-2025__c0098` – «Abzüge vom Nettoeinkommen»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0099.md) `ar-wl-2025__c0099` – «5 Prozent des Nettoeinkommens gemäss Ziffer 20 übersteigen»

<a id="20-berechnung-total"></a>
### Ziff. 20 – Nettoeinkommen (Basis für Selbstbehalt Krankheitskosten und Limite Zuwendungen)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Nettoeinkommen (Herleitung aus Einkünften und Abzügen im Formular Seite 3 in den vorliegenden Quellen nicht belegt – am Originalformular prüfen)
- **Rein:** Rechenzeile: Total Einkünfte − Total Abzüge Ziff. 10–17
- **Rechnen:** Σ steuerbare Einkünfte − Σ Abzüge Ziff. 10–17 (= Einkünfte − Aufwendungen Art. 28–35 StG; Bund: Art. 26–33 DBG)
- **Regel:** Massgebende Grösse für Selbstbehalt 5 % (Ziff. 21.1) und für das 20 %-Maximum der Zuwendungen (Ziff. 21.3).
- **Beachten:** Basis für Selbstbehalt Krankheitskosten 5 % (Ziff. 21.1) und Maximum Zuwendungen 20 % (Ziff. 21.3)
- **Bemerkung:** Code nicht verifiziert. Schlüssel berechnung.total wird mehrfach verwendet (Taxonomie kennt nur diesen Schlüssel für Totalzeilen); Zeile Ziff. 20 ist durch den Verweis «Nettoeinkommen gemäss Ziffer 20» belegt, die Rechenregel nicht.
- **Quellen:**
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0099.md) `ar-wl-2025__c0099` – «5 Prozent des Nettoeinkommens gemäss Ziffer 20 übersteigen»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0103.md) `ar-wl-2025__c0103` – «tens Fr. 100.– beträgt; maximal jedoch 20 Prozent des Nettoeinkommens»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0065.md) `ar-wl-2025__c0065` – «Berufskosten bei unselbständiger Erwerbstätigkeit»
  - [StG AR Art. 36](../../chunks/ar/2025/ar-stg/ar-stg__art-36.md) `ar-stg__art-36` – «5 Prozent der um die Aufwendungen gemäss Art. 28–35 verminderten steuerbaren Einkünfte übersteigen»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t3.md) `bund-dbg-2025__art-33-t3` – «5 Prozent der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen»

<a id="21-1-abzug-krankheitskosten"></a>
### Ziff. 21.1 – Krankheits- und Unfallkosten nach Selbstbehalt (Vorkolonne: Total Formular 6; Hauptkolonne: über 5 % des Nettoeinkommens)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 6 Seite 2 Total Krankheits- und Unfallkosten (selbst getragen)
- **Rein:** Arzt-, Zahnarzt-, Spital-, Therapie-, Medikamentenrechnungen 2025 → Form. 6 S. 2 Bruttobetrag · Leistungsabrechnungen KK/UV → Beiträge Dritter (abziehen) · Ärztliches Zeugnis → Medikamente/Heilmittel, Diät
- **Rechnen:** Vorkolonne = Σ (Brutto − Beiträge Dritter); Abzug = Vorkolonne − 5 % × Nettoeinkommen Ziff. 20 (nur übersteigender Teil); Kanton = Bund 5 %
- **Regel:** Pro Rechnung Bruttobetrag abzüglich Beiträge Dritter (KK, UV, Hilflosenentschädigung) = selbst getragene Kosten; ärztliches Zeugnis bei Medikamenten/Diät. Abzugsfähig ist nur der Teil über 5 % des Nettoeinkommens (Ziff. 20). Anstelle effektiver Diätmehrkosten Pauschale Fr. 2'500 bei dauernder lebensnotwendiger Diät (Zöliakie, nicht Diabetes). Pensionskosten ohne Pflegebedarf sind nicht abzugsfähig.
- **Beachten:** Dauernde lebensnotwendige Diät (Zöliakie, nicht Diabetes): Pauschale 2'500 statt Effektivkosten
- **Beachten:** Altersresidenz mit Pflege < 60 Min./Tag (Pflegestufe 1–3) hier; Pensionskosten ohne Pflegebedarf nicht abziehbar
- **Beachten:** Dauerhaftes Pflegeheim ab Pflegestufe 4 → Ziff. 21.2 (ohne Selbstbehalt)
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
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0100.md) `ar-wl-2025__c0100` – «erkannt, wenn die dauernde Pflegebedürftigkeit (ab Pflegestufe 4 bzw. ab 61»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t3.md) `bund-dbg-2025__art-33-t3` – «5 Prozent der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen»

<a id="21-2-abzug-behinderungskosten"></a>
### Ziff. 21.2 – Behinderungsbedingte Kosten (Übertrag Formular 6 Seite 2; Pflegeheim-Pauschale 2/3, Pauschalen 2'500/5'000/7'500)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 6 Seite 2 Behinderungsbedingte Kosten Total; Verfügung Hilflosenentschädigung; Bewohnerkonto Pflegeheim
- **Rein:** Form. 6 S. 2 «Behinderungsbedingte Kosten» → Total selbst getragen · Bewohnerkonto Pflegeheim 2025 → selbst getragene Heimkosten · Verfügung Hilflosenentschädigung (HE) AHV/IV → Grad (Pauschale) bzw. Anrechnung
- **Rechnen:** Σ selbst getragene Kosten − Vergütungen Dritter; Heim ab Pflegestufe 4: 2/3 × Heimkosten − HE; statt dessen Pauschale HE leicht 2'500 / mittel 5'000 / schwer 7'500
- **Regel:** Ohne Selbstbehalt abziehbar. Dauerhafter Pflegeheimaufenthalt (ab Pflegestufe 4 bzw. ab 61 Min. Pflege-/Betreuungsaufwand): pauschal 2/3 der selbst getragenen Heimkosten, Hilflosenentschädigung AHV/IV abziehen, Bewohnerkonto beilegen. Statt effektiver Kosten Pauschale nach Hilflosenentschädigung: leicht Fr. 2'500, mittel Fr. 5'000, schwer Fr. 7'500 (Verfügung einreichen); Gehörlose und Dialyse-Patienten Fr. 2'500.
- **Beachten:** Gehörlose und Dialysepatienten: Pauschale 2'500 unabhängig von HE
- **Beachten:** Pauschale: HE-Verfügung einreichen; Pflegeheim: Bewohnerkonto beilegen
- **Beachten:** Kanton und Bund: behinderungsbedingte Kosten ohne Selbstbehalt
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
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t3.md) `bund-dbg-2025__art-33-t3` – «die behinderungsbedingten Kosten des Steuerpflichtigen oder der von ihm unterhaltenen Personen mit Behinderungen»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0101.md) `ar-wl-2025__c0101` – «Wird eine solche Pauschale geltend gemacht, ist die Verfügung der Hilflosenent»

<a id="21-3-abzug-spenden"></a>
### Ziff. 21.3 – Freiwillige Zuwendungen an steuerbefreite juristische Personen (Code 550), Übertrag Formular 5 Teil A

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Formular 5 Teil A Total der Zuwendungen (Spendenbestätigungen auf Verlangen)
- **Rein:** Spendenbestätigungen → Form. 5 Teil A (Institution, Datum, Betrag), Total Code 550
- **Rechnen:** Σ Zuwendungen ≥ 100 → min(Σ; 20 % × Nettoeinkommen Ziff. 20); Σ < 100 → kein Abzug; Kanton = Bund
- **Regel:** Nur Geldleistungen/Vermögenswerte an in der Schweiz steuerbefreite gemeinnützige/öffentliche Institutionen, uneigennützig (Mitgliederbeiträge nicht abziehbar); Gesamtbetrag nur abzugsfähig, wenn Total mind. Fr. 100; Maximum 20 % des Nettoeinkommens (Ziff. 20). Religiöse Institutionen nur bei ausschliesslich gemeinnütziger Zweckbestimmung.
- **Beachten:** Nur an CH-steuerbefreite Institutionen (öffentl./gemeinnützig) bzw. Bund, Kantone, Gemeinden; keine Mitgliederbeiträge
- **Beachten:** Religiöse Institutionen nur bei ausschliesslich gemeinnütziger Verwendung
- **Beachten:** Belege auf Verlangen einreichen
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
  - [StG AR Art. 36](../../chunks/ar/2025/ar-stg/ar-stg__art-36.md) `ar-stg__art-36` – «sowie an Bund, Kantone, Gemeinden und deren Anstalten, wenn die Zuwendungen in der Steuerperiode Fr. 100.– erreichen»
  - [DBG Art. 33a](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33a.md) `bund-dbg-2025__art-33a` – «wenn diese Leistungen im Steuerjahr 100 Franken erreichen und insgesamt 20 Prozent»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0102.md) `ar-wl-2025__c0102` – «Freiwillige Zuwendungen an religiöse Vereine und Institutionen mit Sitz in der»

<a id="22-berechnung-total"></a>
### Ziff. 22 – Reineinkommen

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ⬜ offen
- **Beleg → Feld:** – → Rechenzeile (Nettoeinkommen abzüglich Abzüge Ziff. 21)
- **Rein:** Übertrag Ziff. 20 (Nettoeinkommen) und Ziff. 21.1–21.3
- **Rechnen:** Nettoeinkommen Ziff. 20 − (21.1 + 21.2 + 21.3)
- **Regel:** Nettoeinkommen abzüglich zusätzliche Abzüge 21.1-21.3; Sozialabzüge (Ziff. 23) werden vom Reineinkommen abgezogen.
- **Beachten:** Sozialabzüge Ziff. 23 werden erst vom Reineinkommen abgezogen
- **Bemerkung:** Ziffer/Code 22 in den AR-Quellen nicht belegt; Reineinkommen/Sozialabzüge laut Art. 28 und Art. 38 StG (ar-stg__art-28, ar-stg__art-38-t1). Geprüft: weiterhin offen; Ziffer/Code 22 nicht in WL/Formularraster belegt, nur die Rechenlogik (Art. 28, Art. 38 Abs. 1 StG).
- **Quellen:**
  - [StG AR Art. 28](../../chunks/ar/2025/ar-stg/ar-stg__art-28.md) `ar-stg__art-28` – «werden von den gesamten steuerbaren Einkünften die Aufwendungen und allgemeinen Abzüge gemäss Art. 29–36 abgezogen»
  - [StG AR Art. 38](../../chunks/ar/2025/ar-stg/ar-stg__art-38-t1.md) `ar-stg__art-38-t1` – «Vom Reineinkommen werden für die Steuerberechnung abgezogen»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) `ar-wl-2025__c0004` – «21. Zusätzliche 21.1 Krankheits- und Unfallkosten, Selbstbehalt vom Nettoeinkommen»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0099.md) `ar-wl-2025__c0099` – «5 Prozent des Nettoeinkommens gemäss Ziffer 20 übersteigen»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «23. Sozialabzüge 23.1 Für jedes Kind bis zur Vollendung des 4. Altersjahrs»

<a id="23-1-sozialabzug-kinder"></a>
### Ziff. 23.1 – Kinderabzug: Kind bis zur Vollendung des 4. Altersjahrs

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Seite 1 der Steuererklärung (Kinder, Geburtsdatum) - Stichtag 31.12.2025
- **Rein:** StE Seite 1 → Kinderangaben (Geburtsdatum), Stichtag 31. Dezember 2025 · Steuererklärung des Kindes (falls Einkünfte) → Total Einkünfte (Grenze 18'000)
- **Rechnen:** Kanton: 5'300 je Kind bis vollendetes 4. Altersjahr (Stand 31. Dezember 2025); getrennt besteuerte Eltern (gemeinsame Sorge, keine Alimente): je ½ / Bund: 6'800 je Kind
- **Regel:** Fr. 5'300 pro Kind bis zur Vollendung des 4. Altersjahrs, wenn Unterhalt zur Hauptsache bestritten, Kind auf Unterhalt angewiesen und kein Abzug Unterhaltsbeiträge (12.2) geltend gemacht. Kein Abzug, wenn Einkünfte des Kindes Fr. 18'000 übersteigen. Getrennte Eltern: hälftig bei gemeinsamer elterlicher Sorge und ohne Unterhaltsbeiträge.
- **Beachten:** Kein Abzug bei Einkünften des Kindes > 18'000 oder wenn Unterhaltsbeiträge Ziff. 12.2 abgezogen werden
- **Beachten:** Steuerpflicht nur Teil des Jahres: anteilig (für Satz voll)
- **Beachten:** StG-Text nennt 5'000 (nicht indexiert) → massgebend 5'300 (Anhang 1, WL 2025)
- **Limiten:**
  - Kinderabzug Vorschulalter (CHF): Kanton **CHF 5'300 (Kinderabzug bis Vollendung des 4. Altersjahres: CHF 5'300 (indexiert per 1.1.2024).)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (sozialabzug.kind); Staffelung nach Alter nur kantonal.**
  - Kinderabzug Grundbetrag (CHF): Kanton **n/a – AR staffelt den Kinderabzug nach Alter (sozialabzug.kind_vorschule/_schule/_ausbildung); kein einheitlicher Grundbetrag.** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
- **Bund:** Bund: Kinderabzug eigener Betrag (nicht nach Altersstufen; data/werte/bund/2025.yaml).
- **Bemerkung:** Der StG-Text nennt Fr. 5'000 (nicht indexiert); massgebend Anhang 1 StG (per 1.1.2024) und WL 2025: Fr. 5'300. MB 02 (Fassung 25.9.2025) nennt noch Fr. 5'000/7'000/11'000 - MB-Werte nicht indexiert, im Widerspruch zu Anhang 1/WL (Rangfolge: Gesetz-Anhang und WL gelten). Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «23.1 Für jedes Kind bis zur Vollendung des 4. Altersjahrs Fr. 5’300»
  - [StG AR Anhang 1 S. 1](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0001.md) `ar-stg-anhang-kp__c0001` – «Art. 38 Abs. 1 lit. a Ziff. 1 5'300»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Für die Festsetzung der Sozialabzüge sind die Verhältnisse am 31. Dezember 2025»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Fr. 18‘000 kann kein Kinderabzug geltend gemacht werden»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Werden die Eltern getrennt besteuert, kann der Kinderabzug hälftig aufgeteilt»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «6800 Franken für jedes minderjährige oder in der beruflichen oder schulischen Ausbildung stehende Kind»
  - [StG AR Art. 38](../../chunks/ar/2025/ar-stg/ar-stg__art-38-t1.md) `ar-stg__art-38-t1` – «bis zur Vollendung des 4. Altersjahres Fr. 5 000.–»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0105.md) `ar-wl-2025__c0105` – «Der Kinderabzug entfällt für»

<a id="23-2-sozialabzug-kinder"></a>
### Ziff. 23.2 – Kinderabzug: Kind nach Vollendung des 4. bis zur Vollendung des 15. Altersjahrs

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Seite 1 der Steuererklärung (Kinder, Geburtsdatum)
- **Rein:** StE Seite 1 → Kinderangaben (Geburtsdatum), Stichtag 31. Dezember 2025 · Steuererklärung des Kindes (falls Einkünfte) → Total Einkünfte (Grenze 18'000)
- **Rechnen:** Kanton: 7'400 je Kind nach vollendetem 4. bis vollendetes 15. Altersjahr (Stand 31. Dezember 2025); getrennte Eltern: je ½ / Bund: 6'800 je Kind
- **Regel:** Fr. 7'400 pro Kind (4.-15. Altersjahr), Voraussetzungen wie 23.1.
- **Beachten:** Kein Abzug bei Einkünften des Kindes > 18'000 oder wenn Unterhaltsbeiträge Ziff. 12.2 abgezogen werden
- **Beachten:** StG-Text nennt 7'000 (nicht indexiert) → massgebend 7'400 (Anhang 1, WL 2025)
- **Limiten:**
  - Kinderabzug Schulalter (CHF): Kanton **CHF 7'400 (Kinderabzug nach Vollendung des 4. bis Vollendung des 15. Altersjahres: CHF 7'400 (indexiert).)** · Bund **n/a – Bund: einheitlicher Kinderabzug CHF 6'800 (sozialabzug.kind).**
  - Kinderabzug Grundbetrag (CHF): Kanton **n/a – AR staffelt den Kinderabzug nach Alter (sozialabzug.kind_vorschule/_schule/_ausbildung); kein einheitlicher Grundbetrag.** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
- **Bund:** Bund: Kinderabzug eigener Betrag.
- **Bemerkung:** MB 02 nennt Fr. 7'000 (nicht indexiert) - siehe 23.1. Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «des 15. Altersjahrs Fr. 7’400»
  - [StG AR Anhang 1 S. 1](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0001.md) `ar-stg-anhang-kp__c0001` – «Art. 38 Abs. 1 lit. a Ziff. 2 7'400»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Für die Festsetzung der Sozialabzüge sind die Verhältnisse am 31. Dezember 2025»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Fr. 18‘000 kann kein Kinderabzug geltend gemacht werden»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Werden die Eltern getrennt besteuert, kann der Kinderabzug hälftig aufgeteilt»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0105.md) `ar-wl-2025__c0105` – «Der Kinderabzug entfällt für»
  - [StG AR Art. 38](../../chunks/ar/2025/ar-stg/ar-stg__art-38-t1.md) `ar-stg__art-38-t1` – «bis zur Vollendung des 15. Altersjahres Fr. 7 000.–»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «6800 Franken für jedes minderjährige oder in der beruflichen oder schulischen Ausbildung stehende Kind»

<a id="23-3-sozialabzug-kinder"></a>
### Ziff. 23.3 – Kinderabzug: Kind nach Vollendung des 15. Altersjahrs bis Volljährigkeit sowie volljährig in beruflicher/schulischer Ausbildung bis 26. Altersjahr

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Seite 1 der Steuererklärung (Kinder, Schule/Lehrfirma, Dauer der Ausbildung)
- **Rein:** Seite 1 Steuererklärung → Kind (Name, Geburtsjahr), Schule/Lehrfirma + voraussichtliche Ausbildungsdauer · Steuererklärung des Kindes → Total Einkünfte (Ziff. 168 + vereinfacht abgerechnete Bruttolöhne Ziff. 290; bei Ausbildungsbeginn erst ab Eintritt), Reinvermögen
- **Rechnen:** Kanton: 11'600 je Kind / Bund: 6'800 je Kind; Eltern getrennt besteuert, gemeinsame Sorge, keine Unterhaltsbeiträge: je ½; Stichtag 31. Dezember 2025
- **Regel:** Fr. 11'600 pro Kind; für volljährige Kinder in Erstausbildung bis zur Vollendung des 26. Altersjahrs (Ausbildung angeben: Schule oder Lehrfirma und voraussichtliche Dauer). Unterhaltsbeiträge an volljährige Kinder sind nicht abziehbar (beim Empfänger unbesteuert, WL Ziff. 12.2).
- **Beachten:** Kanton: kein Abzug bei Einkünften des Kindes > 18'000 (inkl. 6'000 frei verfügbar) oder Reinvermögen > 250'000
- **Beachten:** Kein Kinderabzug für Kind mit Unterhaltsbeiträgen Ziff. 12.2; Schulgelder/Ausbildungskosten nicht zusätzlich abziehbar
- **Beachten:** Bund volljährig: Beiträge ≥ Abzug; zahlen beide Eltern, erhält die höhere Leistung den Kinderabzug
- **Limiten:**
  - Kinderabzug/Ausbildungsabzug in Ausbildung (CHF): Kanton **CHF 11'600 (Kinderabzug nach 15. Altersjahr bis Volljährigkeit sowie volljährige Kinder in Ausbildung bis 26. Altersjahr: CHF 11'600 (indexiert).)** · Bund **CHF 6'800 (Kinder in beruflicher oder schulischer Ausbildung: gleicher Kinderabzug CHF 6'800 wie für Minderjährige (kein höherer Ausbildungsabzug))**
  - Kinderabzug Grundbetrag (CHF): Kanton **n/a – AR staffelt den Kinderabzug nach Alter (sozialabzug.kind_vorschule/_schule/_ausbildung); kein einheitlicher Grundbetrag.** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
- **Bund:** Bund: Kinderabzug eigener Betrag.
- **Bemerkung:** MB 02 nennt Fr. 11'000 (nicht indexiert) - siehe 23.1. Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «bis zur Vollendung des 26. Altersjahrs Fr. 11’600»
  - [StG AR Anhang 1 S. 1](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0001.md) `ar-stg-anhang-kp__c0001` – «Art. 38 Abs. 1 lit. a Ziff. 3 11'600»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «Unterhaltsbeiträge, die an ein volljähriges Kind bezahlt werden,»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0025.md) `ar-wl-2025__c0025` – «Bei Kindern in beruflicher Ausbildung ist zudem die Schule oder Lehrfirma und»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Übersteigt das Total der Einkünfte des Kindes gemäss seiner Steuererklärung»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Fr. 18‘000 kann kein Kinderabzug geltend gemacht werden»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Bei Ausbildungsbeginn ist auf das Einkommen des Kindes während den Monaten»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Werden die Eltern getrennt besteuert, kann der Kinderabzug hälftig aufgeteilt»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Für die Festsetzung der Sozialabzüge sind die Verhältnisse am 31. Dezember 2025»
  - [MB AR 02 S. 1–2](../../chunks/ar/dauernd/ar-mb-02/ar-mb-02__c0003.md) `ar-mb-02__c0003` – «Übersteigt das Total der Einkünfte (Ziffer 168 sowie allfällige vereinfachte abgerechnete Bruttolöhne, Ziffer 290»
  - [MB AR 02 S. 1–2](../../chunks/ar/dauernd/ar-mb-02/ar-mb-02__c0003.md) `ar-mb-02__c0003` – «Reinvermögen mehr als Fr. 250'000 ist der Kinderabzug nicht mehr zulässig»
  - [MB AR 02 S. 2](../../chunks/ar/dauernd/ar-mb-02/ar-mb-02__c0004.md) `ar-mb-02__c0004` – «Somit können weder Schulgelder noch andere Ausbildungskosten der Kinder vom Einkommen abgezogen»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0105.md) `ar-wl-2025__c0105` – «Der Kinderabzug entfällt für»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «6800 Franken für jedes minderjährige oder in der beruflichen oder schulischen Ausbildung stehende Kind»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «werden die Eltern getrennt besteuert, so wird der Kinderabzug hälftig aufgeteilt»
  - [KS 30 S. 20](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0062.md) `bund-ks-30__c0062` – «Person für den Unterhalt des Kindes sorgt, ist erfüllt, wenn sie Beiträge mindestens in der»
  - [KS 30 S. 21–22](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0068.md) `bund-ks-30__c0068` – «Leisten beide Elternteile Unterhaltszahlungen, kann der El»

<a id="23-4-sozialabzug-unterstuetzung"></a>
### Ziff. 23.4 – Unterstützungsabzug für unterstützte Person (nur direkte Bundessteuer)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Bescheinigung der unterstützten Person/Zahlungsnachweise (Name, Adresse, Betrag)
- **Rein:** Zahlungsbelege der Unterstützungsleistungen 2025 → geleisteter Betrag je Person · Bescheinigung → unterstützte Person kann Lebensunterhalt nicht aus eigenen Mitteln bestreiten · Angaben zur unterstützten Person → Name, Vorname, Adresse
- **Rechnen:** Bund: 6'800 je unterstützte Person, sofern Σ Beiträge in der Steuerperiode ≥ 6'800 / Kanton: kein Unterstützungsabzug
- **Regel:** Fr. 6'800 nur bei der DBSt; Voraussetzung: Beiträge mind. in Höhe des Abzugs an eine erwerbsunfähige/beschränkt erwerbsfähige Person; nicht für Ehegatten/eingetragene Partner und nicht für Kinder mit Kinderabzug. Für Staats-/Gemeindesteuer kein Unterstützungsabzug.
- **Beachten:** Nicht für Ehegatten/eingetragene Partner und nicht für Kinder, für die ein Kinderabzug gewährt wird
- **Beachten:** Bedürftigkeit objektiv (erwerbsunfähig/beschränkt erwerbsfähig); Leistung unentgeltlich, ohne Gegenleistung
- **Beachten:** Beide Eltern zahlen an volljähriges Kind: höhere Leistung → Kinderabzug, anderer Elternteil 23.4, wenn Leistung ≥ 6'800
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **n/a – Unterstützungsabzug (CHF 6'800) gilt gemäss WL 2025 Ziff. 23.4 nur für die direkte Bundessteuer; kantonal nicht vorgesehen (Art. 38 Abs. 1 lit. b StG aufgehoben).** · Bund **CHF 6'800 (Unterstützungsabzug pro erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mindestens in Höhe des Abzugs unterstützt; nicht für Ehegatten und Kinder mit Kinderabzug)**
- **Bund:** Nur DBSt: Fr. 6'800 (AR-Quelle WL).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «23.4 Abzug für jede unterstützte Person (gilt nur für die direkte Bundessteuer) Fr. 6’800»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0105.md) `ar-wl-2025__c0105` – «Dieser Abzug gilt nur für die»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0105.md) `ar-wl-2025__c0105` – «Anzugeben sind der geleistete Betrag»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0105.md) `ar-wl-2025__c0105` – «nicht aus eigenen Mitteln bestreiten kann»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0105.md) `ar-wl-2025__c0105` – «werden für den Ehegatten bzw. eingetragenen Partner sowie für Kinder, für die»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «6800 Franken für jede erwerbsunfähige oder beschränkt erwerbsfähige Person»
  - [KS 30 S. 21](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0066.md) `bund-ks-30__c0066` – «haltsleistungen müssen zudem unentgeltlich sein bzw. ohne Gegenleistung erfolgen»
  - [KS 30 S. 21–22](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0068.md) `bund-ks-30__c0068` – «ternteil mit den höheren finanziellen Leistungen, d.h. in der Regel derjenige mit dem höheren»
  - [KS 30 S. 21–22](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0068.md) `bund-ks-30__c0068` – «zungsabzug geltend machen, sofern seine Leistungen mindestens in der Höhe des Abzuges»

<a id="24-berechnung-total"></a>
### Ziff. 24 – Steuerbares Einkommen

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Reineinkommen abzüglich Sozialabzüge)
- **Rein:** Übertrag Sozialabzüge Ziff. 23.1–23.4 (Spalten Kanton / Bund)
- **Rechnen:** Je Spalte: Reineinkommen − Sozialabzüge; Kanton: Σ 23.1–23.3 / Bund: 6'800 je Kind + 23.4 + 2'800 für Ehepaare in ungetrennter Ehe (Art. 35 DBG)
- **Regel:** Steuersatz bestimmt sich auf dem steuerbaren Einkommen (Ziff. 24); vereinfacht abgerechnete Löhne (8.1) werden nicht berücksichtigt.
- **Beachten:** Vereinfacht abgerechnete Löhne (Ziff. 8.1) zählen nicht für den Steuersatz
- **Beachten:** Unterjährige Steuerpflicht: Sozialabzüge anteilig, für die Satzbestimmung voll
- **Beachten:** Stichtag: Verhältnisse am 31. Dezember 2025 bzw. Ende der Steuerpflicht
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **n/a – AR staffelt den Kinderabzug nach Alter (sozialabzug.kind_vorschule/_schule/_ausbildung); kein einheitlicher Grundbetrag.** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
  - Verheiratetenabzug (CHF, Bund): Kanton **n/a – Verheiratetenabzug existiert nur bei der direkten Bundessteuer (data/werte/bund).** · Bund **CHF 2'800 (Verheiratetenabzug für Ehepaare in rechtlich und tatsächlich ungetrennter Ehe)**
- **Bemerkung:** Code nicht verifiziert.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0063.md) `ar-wl-2025__c0063` – «stimmung des Steuersatzes auf dem steuerbaren Einkommen (Ziff. 24)»
  - [StG AR Art. 38](../../chunks/ar/2025/ar-stg/ar-stg__art-38-t1.md) `ar-stg__art-38-t1` – «Vom Reineinkommen werden für die Steuerberechnung abgezogen»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «Abzug für jede unterstützte Person (gilt nur für die direkte Bundessteuer)»
  - [StG AR Art. 38](../../chunks/ar/2025/ar-stg/ar-stg__art-38-t2.md) `ar-stg__art-38-t2` – «werden die Sozialabzüge anteilmässig gewährt; für die Satzbestimmung werden sie voll angerechnet»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0104.md) `ar-wl-2025__c0104` – «Für die Festsetzung der Sozialabzüge sind die Verhältnisse am 31. Dezember 2025»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «6800 Franken für jedes minderjährige oder in der beruflichen oder schulischen Ausbildung stehende Kind»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «2800 Franken für Ehepaare, die in rechtlich und tatsächlich ungetrennter Ehe leben»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «Bei teilweiser Steuerpflicht werden die Sozialabzüge anteilsmässig gewährt»

## Weitere Angaben

<a id="8-1-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 8.1 – Im vereinfachten Abrechnungsverfahren (BGSA) abgerechneter Bruttolohn - nur Information (Code 290)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Abrechnung/Bescheinigung der AHV-Ausgleichskasse
- **Rein:** Aufstellung/Bestätigung der AHV-Ausgleichskasse über den Steuerabzug → Bruttolohn (vereinfacht abgerechnet)
- **Rechnen:** Bruttolohn eintragen; nur Information: nicht in Ziff. 7, nicht satzbestimmend (Ziff. 24)
- **Regel:** Bruttolohn einsetzen, nur zur Information (nicht im Total der Einkünfte Ziff. 7); mit 5 % Quellensteuerabzug sind DBSt und Kantons-/Gemeindesteuern abgegolten; keine Abzüge im ordentlichen Verfahren dafür.
- **Beachten:** Quellensteuer 5 % gilt für Kanton/Gemeinde und Bund als abgegolten (DBSt-Satz 0,5 %, Art. 37a DBG)
- **Beachten:** Für diesen Lohn keinerlei Abzüge (z.B. Berufskosten) im ordentlichen Verfahren
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Korrigiert durch Prüfung: Beleg lohnausweis entfernt; beim vereinfachten Verfahren (BGSA) wird kein Lohnausweis ausgestellt, Beleg ist die Abrechnung der AHV-Ausgleichskasse (kein passender Belegtyp in der Taxonomie).
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0063.md) `ar-wl-2025__c0063` – «In Ziff. 8.1 ist der Bruttolohn einzusetzen.»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0063.md) `ar-wl-2025__c0063` – «8.1 Gemäss Bundesgesetz gegen die Schwarzarbeit (BGSA) können Arbeitgeber klei»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0030.md) `ar-wl-2025__c0030` – «290 213211»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0063.md) `ar-wl-2025__c0063` – «des Steuersatzes auf dem steuerbaren Einkommen (Ziff. 24) berücksichtigt»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0063.md) `ar-wl-2025__c0063` – «nerlei Abzüge im ordentlichen Veranlagungsverfahren geltend gemacht werden»
  - [DBG Art. 37a](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-37a.md) `bund-dbg-2025__art-37a` – «zu einem Satz von 0,5 Prozent zu erheben»
  - [DBG Art. 37a](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-37a.md) `bund-dbg-2025__art-37a` – «Die AHV-Ausgleichskasse stellt dem Steuerpflichtigen eine Aufstellung oder eine Bestätigung über den Steuerabzug aus.»

<a id="8-2-info-steuerfreie-leistungen"></a>
### Ziff. 8.2 – Ergänzungsleistungen (nur Information) (Code 291)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung/Bescheinigung der Ausgleichskasse
- **Rein:** EL-Verfügung/Bescheinigung der Ausgleichskasse → ausbezahlte Ergänzungsleistungen 2025
- **Rechnen:** Nur Information (steuerfrei); EL zur Vergütung von Krankheits-/Behinderungskosten an diese Kosten (Form. 6) anrechnen (Kanton = Bund)
- **Regel:** Nur Angabe; Ergänzungsleistungen sind steuerfrei. Anzurechnen sind die zur Vergütung von Krankheits-/Behinderungskosten ausgerichteten Beträge (mindern Ziff. 21.1/21.2).
- **Beachten:** Auch DBSt steuerfrei (Art. 24 lit. h DBG); EL nicht unter Ziff. 3.1 erfassen
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Ergänzungsleistungen und Hilflosenentschädigungen sind steuerfrei.»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0031.md) `ar-wl-2025__c0031` – «291 tragen»
  - [DBG Art. 24](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-24-t2.md) `bund-dbg-2025__art-24-t2` – «die Einkünfte aufgrund der Bundesgesetzgebung über Ergänzungsleistungen zur Alters-, Hinterlassenen- und Invalidenversicherung»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0049.md) `ar-wl-2025__c0049` – «nicht aber die ordentlichen und ausserordentlichen»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0049.md) `ar-wl-2025__c0049` – «Ergänzungsleistungen, da diesen Leistungen Unterstützungscharakter zukommt.»
  - [KS 11 S. 10–11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0026.md) `bund-ks-11__c0026` – «hingegen diejenigen Ergänzungsleistungen, welche zur Vergütung von Krankheits- und Be»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Anzurechnen sind aber jene Ergänzungsleistungen, die zur Ver»

<a id="8-3-info-steuerfreie-leistungen"></a>
### Ziff. 8.3 – Hilflosenentschädigungen (nur Information) (Code 292)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung der Hilflosenentschädigung
- **Rein:** Verfügung der Hilflosenentschädigung → Jahresbetrag und Grad (leicht/mittel/schwer)
- **Rechnen:** Nur Information (steuerfrei); an behinderungsbedingte Kosten (Form. 6) anrechnen oder Pauschale 21.2: leicht 2'500 / mittel 5'000 / schwer 7'500 (Kanton = Bund)
- **Regel:** Nur Angabe; steuerfrei, aber an die behinderungsbedingten Kosten (Form. 6, Ziff. 21.2) anzurechnen, für die sie bestimmt sind. Verfügung auch bei Pauschalabzug 21.2 einreichen.
- **Beachten:** Pauschale ersetzt den Abzug der effektiven selbst getragenen behinderungsbedingten Kosten
- **Beachten:** Bei Pauschale die Verfügung der Hilflosenentschädigung einreichen
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Ergänzungsleistungen und Hilflosenentschädigungen sind steuerfrei.»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0031.md) `ar-wl-2025__c0031` – «292 213211»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0101.md) `ar-wl-2025__c0101` – «Bezüger einer Hilflosenentschädigung leichten Grades:»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0101.md) `ar-wl-2025__c0101` – «Bezüger einer Hilflosenentschädigung mittleren Grades:»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0101.md) `ar-wl-2025__c0101` – «Bezüger einer Hilflosenentschädigung schweren Grades:»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0101.md) `ar-wl-2025__c0101` – «Wird eine solche Pauschale geltend gemacht, ist die Verfügung der Hilflosenent-»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0101.md) `ar-wl-2025__c0101` – «21.2 zu übertragen.»
  - [KS 11 S. 10](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0025.md) `bund-ks-11__c0025` – «Bezüger einer Hilflosenentschädigung schweren Grades:   CHF 7'500.--»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «für die sie bestimmt sind (Formular 6).»
  - [KS 11 S. 10–11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0026.md) `bund-ks-11__c0026` – «hinderungskosten gemäss Art. 3d ELG ausgerichtet werden. Gleiches gilt für Hilflosenent»

<a id="8-4-info-steuerfreie-leistungen"></a>
### Ziff. 8.4 – Überbrückungsleistungen für ältere Arbeitslose (nur Information) (Code 293)

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung über Überbrückungsleistungen
- **Rein:** Verfügung/Abrechnung Überbrückungsleistungen (vom Kanton ausgerichtet) → Jahresbetrag 2025
- **Rechnen:** Nur Information; steuerfrei (Kanton und Bund, Art. 24 lit. k DBG)
- **Regel:** Nur Angabe; steuerfrei (Bundesgesetz vom 19. Juni 2020).
- **Beachten:** Anspruch: nach dem 60. Geburtstag von der ALV ausgesteuert, bis zur Pensionierung
- **Beachten:** Abgrenzung: ALV-Taggelder bleiben steuerbar (Ziff. 3.4)
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Steuerfrei sind Einkünfte aus Überbrückungsleistungen für ältere Arbeitslose ge»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0031.md) `ar-wl-2025__c0031` – «293 213211»
  - [DBG Art. 24](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-24-t3.md) `bund-dbg-2025__art-24-t3` – «Einkünfte aufgrund des Bundesgesetzes vom 19. Juni 2020 über Überbrückungsleistungen für ältere Arbeitslose»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0064.md) `ar-wl-2025__c0064` – «Arbeitslose, die nach dem 60. Geburtstag von der Arbeitslosenversicherung aus-»
  - [WL AR 2025 S. 10](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0053.md) `ar-wl-2025__c0053` – «Taggelder aus Arbeitslosenversicherung sind insoweit anzugeben»

<a id="40-41-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. 40-41 – Ausbezahlte Kapitalleistungen aus Vorsorge: 40.1 Säule 3a, 40.2 berufliche Vorsorge, 40.3 übrige; Total Ziff. 41 (Code 950)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Bescheinigung der Vorsorgeeinrichtung/Bank
- **Rein:** Bescheinigung Bank/Versicherung → Kapitalbezug Säule 3a (40.1) · Bescheinigung Pensionskasse → Kapitalleistung 2. Säule, auch Vorbezug Wohneigentum (40.2) · Bescheinigung → übrige Kapitalleistungen aus Vorsorge (40.3)
- **Rechnen:** 41 = Σ 40.1–40.3. Kanton (einf. Steuer): Verheiratetentarif 0,7500 % bis 417'200, darüber 1,0000 %; übrige 1,0000 % bzw. 1,3333 % / Bund: ⅕ der Tarife Art. 36 DBG
- **Regel:** Gesondert besteuert (volle Jahressteuer), Sozialabzüge werden nicht gewährt; nicht in Ziff. 6.4/7. Tarif: Satz der einfachen Steuer nach Art. 41 StG (Tarifgrenze indexiert gem. Anhang 1: 417'200). Bescheinigung beilegen. Einkauf-Sperrfrist/WEF siehe MB 08/09/19.
- **Beachten:** Gesonderte volle Jahressteuer ohne Sozialabzüge; Steuerjahr des Zuflusses (Kanton und Bund)
- **Beachten:** Kanton (MB 08): Einkauf 2. Säule innert 3 Jahren vor Kapitalbezug → nicht abziehbar, von Kapitalleistung abgezogen
- **Beachten:** Kapitalabfindungen für wiederkehrende Leistungen nicht hier → Ziff. 6.4 (Rentensatz)
- **Bund:** Besteuerung der Kapitalleistungen bei der DBSt: nicht aus AR-Quellen belegt (Bund-Quellen prüfen).
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Einzelcodes 40.1-40.3 nicht erkennbar; nur Total-Code 950. 417'200 gilt als indexierter Anhang-Wert; StG-Text nennt 400'000 (nicht indexiert).
- **Quellen:**
  - [StG AR Art. 41](../../chunks/ar/2025/ar-stg/ar-stg__art-41.md) `ar-stg__art-41` – «Kapitalleistungen gemäss Art. 25 sowie Zahlungen bei Tod und für bleibende körperliche oder gesundheitliche Nachteile werden gesondert besteuert»
  - [StG AR Art. 41](../../chunks/ar/2025/ar-stg/ar-stg__art-41.md) `ar-stg__art-41` – «Die Sozialabzüge werden nicht gewährt.»
  - [StG AR Anhang 1 S. 1–2](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0002.md) `ar-stg-anhang-kp__c0002` – «Art. 41 Abs. 1 lit. a Ziff. 1 417'200»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0109.md) `ar-wl-2025__c0109` – «aus Vorso Bescheinigung»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0109.md) `ar-wl-2025__c0109` – «950»
  - [StG AR Art. 41](../../chunks/ar/2025/ar-stg/ar-stg__art-41.md) `ar-stg__art-41` – «Der Satz der einfachen Steuer berechnet sich wie folgt»
  - [StG AR Art. 41](../../chunks/ar/2025/ar-stg/ar-stg__art-41.md) `ar-stg__art-41` – «Der Steueranspruch entsteht zum Zeitpunkt des Zuflusses der Leistung.»
  - [DBG Art. 38](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-38.md) `bund-dbg-2025__art-38` – «Sie wird zu einem Fünftel der Tarife nach Artikel 36 Absätze 1, 2 und 2bis erster Satz berechnet.»
  - [DBG Art. 38](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-38.md) `bund-dbg-2025__art-38` – «Die Steuer wird für das Steuerjahr festgesetzt, in dem die entsprechenden Einkünfte zugeflossen sind.»
  - [DBG Art. 38](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-38.md) `bund-dbg-2025__art-38` – «Die Sozialabzüge werden nicht gewährt.»
  - [StG AR Anhang 1 S. 1–2](../../chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0002.md) `ar-stg-anhang-kp__c0002` – «Art. 41 Abs. 1 lit. b Ziff. 1   417'200»
  - [MB AR 08 S. 1–2](../../chunks/ar/dauernd/ar-mb-08/ar-mb-08__c0006.md) `ar-mb-08__c0006` – «die steuerpflichtigen Personen Einkaufsleistungen innerhalb der letzten 3 Jahre vor dem Bezug einer»
  - [MB AR 08 S. 1–2](../../chunks/ar/dauernd/ar-mb-08/ar-mb-08__c0006.md) `ar-mb-08__c0006` – «Kapitalleistung (Altersleistung, Vorbezug für Wohneigentum, Aufnahme selbständige Erwerbstätigkeit)»
  - [MB AR 08 S. 2](../../chunks/ar/dauernd/ar-mb-08/ar-mb-08__c0007.md) `ar-mb-08__c0007` – «die Beiträge für den Einkauf von Beitragsjahren können nicht vom steuerbaren Einkommen in Abzug»
  - [MB AR 08 S. 2](../../chunks/ar/dauernd/ar-mb-08/ar-mb-08__c0007.md) `ar-mb-08__c0007` – «die steuerliche nicht akzeptierte Einkaufssumme muss für die Besteuerung der Kapitalleistung in Abzug»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0062.md) `ar-wl-2025__c0062` – «Die Kapitalabfindungen für wiederkehrende Leistungen sind mit dem Auszah»

## Abzüge

<a id="10-1-abzug-berufskosten-uebrige"></a>
### Ziff. 10.1 – Berufskosten unselbständig Erwerbende, Person 1 (Total Formular 4, Code 438); Person 2 unter Ziff. 10.2 (Code 488)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Formular 4 Ziff. 6 Total der Berufskosten (Person 1 Vorderseite, Person 2 Rückseite)
- **Rein:** Formular 4 → Ziff. 6 Total: Person 1 Code 438 (Vorderseite) → 10.1; Person 2 Code 488 (Rückseite) → 10.2 · ÖV-Abo/Billette → Form. 4 Ziff. 1.1 tatsächliche Kosten (Code 400) · Lohnausweis → Nettolohn (= Ziff. 1.1 StE, Basis Pauschale); Kreuz Feld F/G · Spesenreglement/Lohnausweis → nicht ereignisbezogene Pauschalspesen?
- **Rechnen:** Σ Form. 4: Fahrkosten (Kt. max. 6'000 / Bund 3'300) + Verpflegung + übrige (Kt. 700 + 10 % Nettolohn, max. 2'400 / Bund 3 %, 2'000–4'000) + Wochenaufenthalt + Nebenerwerb
- **Regel:** Total aus Form. 4 (Fahrkosten max. 6'000, Verpflegung, übrige Kosten Pauschale oder effektiv, Wochenaufenthalt, Nebenerwerb) übertragen. Pauschale übrige Kosten (Fr. 700 + 10 % des Nettolohns, max. Fr. 2'400) kann jede unselbständig erwerbstätige Person beanspruchen. Hinweis: Nach Form. 4 nimmt Ziff. 10.1 das Total Person 1, Ziff. 10.2 das Total Person 2 auf (nicht Fahrkosten/Verpflegung wie in den Titeln der WL-Chunks).
- **Beachten:** LA Feld F (Sammeltransport, GA vom AG) → kein Fahrkostenabzug; Feld G → halber Verpflegungsabzug 7.50/Tag, max. 1'600
- **Beachten:** Auto nur begründet (kein öV, > 60 Min./Tag Einsparung, AG-Verlangen, Arztzeugnis): 0.70/km, i.d.R. max. 220 Tage
- **Beachten:** Nicht ereignisbezogene Pauschalspesen → keine Pauschale übrige Kosten; vom AG übernommene Kosten nicht abziehbar
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 (Pendlerabzug).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Übrige Berufskosten Pauschale: CHF 700 zuzüglich 10 % des Nettolohnes, max. CHF 2'400.)** · Bund **3 % (Übrige Berufskosten: 3 % des Nettolohns (Pauschale; Nachweis höherer Kosten möglich); bei Teilzeit/unterjährig angemessen kürzen)**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockelbetrag der Pauschale (zuzüglich 10 % des Nettolohnes).)** · Bund **n/a – Bund: 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; kein 'fix + %'-Modell.**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Maximum der Pauschale für übrige Berufskosten: CHF 2'400.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **n/a – Formel «700 + 10 %» ohne separates Minimum; der fixe Sockelbetrag von CHF 700 ist das faktische Minimum (siehe berufskosten.uebrige.fix).** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.70 (Privates Motorfahrzeug in begründeten Fällen: CHF 0.70 pro km.)** · Bund **CHF 0.70 (Privatauto: Abzug pro Fahrkilometer CHF 0.70, nur wenn kein öffentliches Verkehrsmittel verfügbar/zumutbar (Steuerjahr 2025))**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **220 Tage (In der Regel höchstens 220 Arbeitstage für Fahrkosten.)** · Bund **n/a – Bund kennt keine Festlegung massgebender Arbeitstage; abziehbar sind die tatsächlichen notwendigen Kosten bis zum Maximalbetrag (Art. 26 Abs. 1 lit. a DBG).**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Bei Kantinenverpflegung oder Arbeitgeberbeitrag CHF 7.50 pro Tag.)** · Bund **CHF 7.50 (Halber Abzug CHF 7.50 pro Hauptmahlzeit, wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei Kantinenverpflegung oder Arbeitgeberbeitrag höchstens CHF 1'600 pro Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: CHF 1'600 pro Jahr)**
- **Bund:** Direkte Bundessteuer hat eigene Maxima/Pauschalen (Fahrkosten, übrige Berufskosten): siehe data/werte/bund/2025.yaml; AR-Fr. 6'000 gilt nur für Staats-/Gemeindesteuer.
- **Bemerkung:** Hauptformular-Code für Ziff. 10.1/10.2: nicht verifiziert (438/488 sind die Codes der Total-Zeile in Form. 4). Gleichzeitig Zweiverdienerabzug: Berufskosten mindern Basis (Ziff. 17).
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0004.md) `ar-form-04-2025__c0004` – «Total der Berufskosten 438 13211 zu übertragen in die Steuererklärung Seite 3 Ziffer 10.1»
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0008.md) `ar-form-04-2025__c0008` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 10.2»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0065.md) `ar-wl-2025__c0065` – «10. Berufskosten bei unselbständiger Erwerbstätigkeit 4»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «muss auf dem Lohnausweis Feld F»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «Ein Abzug für die Fahrt zur Arbeit ist deshalb nicht möglich»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «Es sind die max. Fahrkosten abzüge für Kanton und Bund zu beachten»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0076.md) `ar-wl-2025__c0076` – «der halbe Abzug (Fr. 7.50 pro Tag, Fr. 1’600.– im Jahr) zulässig. In diesem Fall ist auf dem Lohnausweis Feld G angekreuzt»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0002.md) `ar-form-04-2025__c0002` – «Einsparung über 60 Minuten/Tag durch Benützung Privatfahrzeug»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0001.md) `ar-wl-2025__c0001` – «in begründeten Fällen pro Km Fr. 0.70»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0001.md) `ar-wl-2025__c0001` – «in der Regel höchstens 220 Tage»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0078.md) `ar-wl-2025__c0078` – «Bei Auszahlung nicht ereignis»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0073.md) `ar-wl-2025__c0073` – «Kein Abzug ist zulässig für Kosten, die der Arbeitgeber»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0071.md) `ar-wl-2025__c0071` – «Ausgangsbasis ist der in Ziffer 1.1 der Steuererklärung deklarierte Nettolohn»
  - [DBG Art. 26](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-26.md) `bund-dbg-2025__art-26` – «die notwendigen Kosten bis zu einem Maximalbetrag von 3300 Franken für die Fahrten zwischen Wohn- und Arbeitsstätte»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «3 % des Nettolohns, mindestens im Jahr»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0001.md) `ar-form-04-2025__c0001` – «1.1 Öffentliche Verkehrsmittel»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0074.md) `ar-wl-2025__c0074` – «Autobus usw.) die tatsächlichen Kosten;»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0002.md) `ar-form-04-2025__c0002` – «Ständige Benützung des Motorfahrzeugs auf Verlangen des Arbeitgebers»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0002.md) `ar-form-04-2025__c0002` – «Benützung öV wegen Krankheit oder Gebrechlichkeit unzumutbar (Arztzeugnis)»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «höchstens im Jahr | 4000.—»

<a id="11-abzug-schuldzinsen"></a>
### Ziff. 11 – Schuldzinsen (privat), Übertrag Formular 5 Teil A (Code nicht verifiziert)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 5 Teil A Total private Schuldzinsen (Spalte rechts)
- **Rein:** Formular 5 Teil A → Total private Schuldzinsen 2025 (Schulden → Ziff. 34.1) · Hypothekar-/Kreditgeber → Zinsausweis 2025 (bezahlte Zinsen) · Steuerauszug Bank → Schuldzinsen Konti/Kredite
- **Rechnen:** Kanton: min(Σ 2025 bezahlte private Schuldzinsen; Erträge Ziff. 4 (ohne Lotterie-/Lottogewinne) + Ziff. 5 + 50'000) / Bund: steuerbare Vermögenserträge + 50'000
- **Regel:** Tatsächlich bezahlte Zinsen 2025 auf anerkannten Schulden; nicht abzugsfähig: Amortisationen, Anlagekosten-Zinsen (ausser Baukreditzinsen), Baurechtszinsen selbstgenutzter Eigenheime, Leasingraten. Private Schuldzinsen nur bis Wertschriften-/Guthabenerträge (Ziff. 4, ohne Lotteriegewinne) plus Liegenschaftserträge (Ziff. 5) zuzüglich Fr. 50'000.
- **Beachten:** Nicht abziehbar: Amortisationen, Baurechtszinsen Eigenheim, Leasingraten, Anlagekosten-Zinsen (Baukreditzinsen schon)
- **Beachten:** Schuld muss steuerlich anerkannt sein (Ziff. 34)
- **Beachten:** Geschäftliche Schuldzinsen in der Jahresrechnung, nicht hier (Form. 5 Teil B)
- **Bund:** Schuldzinsen-Abzugsgrenze bei der DBSt nicht aus AR-Quellen belegt; Bundesregeln separat prüfen.
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0001.md) `ar-form-05-2025__c0001` – «Total private Schulden und private Schuldzinsen 213213211 13213211»
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0001.md) `ar-form-05-2025__c0001` – «Seite 3 Ziffer 11»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0081.md) `ar-wl-2025__c0081` – «zuzüglich Fr. 50’000.–»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0081.md) `ar-wl-2025__c0081` – «sind im Teil A des Formulars 5 zu deklarieren»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken»
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0002.md) `ar-form-05-2025__c0002` – «und deshalb hier nicht»

<a id="12-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.1 – Unterhaltsbeiträge an geschiedene/getrennt lebende Person

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungsurteil/Trennungsvereinbarung, Zahlungsnachweise
- **Rein:** Scheidungsurteil/Trennungsvereinbarung → Unterhaltsbeitrag an Ehegatten · Bank-/Zahlungsbelege → Σ 2025 bezahlt
- **Rechnen:** Σ 2025 bezahlte Unterhaltsbeiträge an geschiedene, gerichtlich oder tatsächlich getrennt lebende Person (Kinderalimente → Ziff. 12.2); Kanton = Bund
- **Regel:** Beiträge an die geschiedene, gerichtlich oder tatsächlich getrennt lebende Person; bei erstmaliger Zahlung Urteilsauszug und Zahlungsnachweis beilegen.
- **Beachten:** Erstmalige Zahlung: Auszug Urteil/Vereinbarung + Zahlungsnachweis beilegen
- **Beachten:** Andere familienrechtliche Unterhalts-/Unterstützungsleistungen nicht abziehbar
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «12.2 Die Unterhaltsbeiträge an einen Elternteil für die unter dessen elterlicher Sorge»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «Bei erstmaliger Zahlung von Unterhaltsbeiträgen»
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t1.md) `ar-stg__art-35-t1` – «nicht jedoch Leistungen in Erfüllung anderer familienrechtlicher Unterhalts- oder Unterstützungspflichten»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «die Unterhaltsbeiträge an den geschiedenen, gerichtlich oder tatsächlich getrennt lebenden Ehegatten»

<a id="12-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.2 – Unterhaltsbeiträge für minderjährige Kinder (an den Elternteil mit Sorge/Obhut)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungsurteil/Vereinbarung, Zahlungsnachweise
- **Rein:** Scheidungsurteil/Unterhaltsvertrag → Kinderunterhaltsbeiträge · Zahlungsbelege → Σ 2025 bezahlt je Kind
- **Rechnen:** Σ 2025 bezahlte Unterhaltsbeiträge an den anderen Elternteil für minderjährige Kinder unter dessen Sorge/Obhut; Kanton = Bund
- **Regel:** Abziehbar nur für minderjährige Kinder unter der Sorge/Obhut des anderen Elternteils; dann entfällt der Kinderabzug 23.1-23.3. Beiträge an volljährige Kinder: nicht abziehbar (beim Empfänger unbesteuert).
- **Beachten:** Abzug 12.2 → Kinderabzüge 23.1–23.3 für dieses Kind entfallen
- **Beachten:** Zahlungen an volljährige Kinder: nicht abziehbar (beim Empfänger unbesteuert)
- **Beachten:** Erstmalige Zahlung: Urteils-/Vereinbarungsauszug + Zahlungsnachweis beilegen
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet).
- **Quellen:**
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «12.2 Die Unterhaltsbeiträge an einen Elternteil für die unter dessen elterlicher Sorge»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «Unterhaltsbeiträge, die an ein volljähriges Kind bezahlt werden»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «sowie die Unterhaltsbeiträge an einen Elternteil für die unter dessen elterlichen Sorge stehenden Kinder»

<a id="12-3-abzug-unterhaltsbeitraege"></a>
### Ziff. 12.3 – Rentenleistungen (Leibrenten nach OR, Ertragsanteil)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Vertrag/Bescheinigung der Rentenzahlung
- **Rein:** Leibrentenvertrag (OR) / Zahlungsbescheinigung → 2025 bezahlte Rentenleistungen · ESTV-Publikation → massgebender Prozentsatz Ertragsanteil 2025
- **Rechnen:** abziehbarer Ertragsanteil = bezahlte Leibrente × ESTV-Satz (Ø-Rendite zehnjährige Bundesobligationen + 0.5 %)
- **Regel:** Abziehbar ist der Ertragsanteil, berechnet aus der Durchschnittsrendite zehnjähriger Bundesobligationen plus 0,5 %; der massgebende Prozentsatz wird jährlich von der ESTV veröffentlicht.
- **Beachten:** Satz 2025 nicht in AR-Quellen → ESTV-Publikation konsultieren
- **Beachten:** Auch dauernde Lasten abziehbar (Art. 35 Abs. 1 lit. b StG; Bund: Art. 33 Abs. 1 lit. b DBG)
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Prozentsatz 2025 nicht in den AR-Quellen: bei ESTV prüfen.
- **Quellen:**
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «Bei der Finanzierung von Leibrenten nach Obligationenrecht berechnet sich der»
  - [StG AR Art. 35](../../chunks/ar/2025/ar-stg/ar-stg__art-35-t1.md) `ar-stg__art-35-t1` – «die dauernden Lasten sowie der Ertragsanteil im Sinne von Art. 7 Abs. 2 lit. c StHG der Leistungen aus Leibrenten- und aus Verpfründungsverträgen»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «die dauernden Lasten sowie der Ertragsanteil nach Artikel 22 Absatz 3 Buchstabe c»

<a id="13-1-abzug-vorsorge-saeule3a"></a>
### Ziff. 13.1 – Beiträge Säule 3a (gebundene Selbstvorsorge)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Bescheinigung der Bank-/Versicherungsstiftung (Formular 21 EDP)
- **Rein:** 3a-Bescheinigung Bank-/Versicherungsstiftung (Form. 21 EDP) → einbezahlte Beiträge 2025 je Person · Lohnausweis/Vorsorgeausweis → Anschluss 2. Säule ja/nein (bestimmt Maximum) · ohne 2. Säule: Lohnausweis/Jahresrechnung → Erwerbseinkommen (Basis 20 %)
- **Rechnen:** je Person min(bezahlte Beiträge 2025; mit 2. Säule 7'258 / ohne 2. Säule 20 % Erwerbseinkommen, max. 36'288); Kanton = Bund
- **Regel:** Nur 2025 tatsächlich bezahlte Beiträge, Bescheinigung beilegen. Max. Fr. 7'258 mit 2. Säule; ohne 2. Säule 20 % des Erwerbseinkommens, max. Fr. 36'288. Beide Partner können je den Abzug beanspruchen. Selbständige: Beiträge nicht in der Erfolgsrechnung, sondern hier.
- **Beachten:** Nur 2025 tatsächlich bezahlte Beiträge; Bescheinigung in jedem Fall beilegen
- **Beachten:** Beide Partner erwerbstätig mit Beiträgen → je eigener Abzug
- **Beachten:** Selbständige: Beiträge nicht der Erfolgsrechnung belasten
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
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0083.md) `ar-wl-2025__c0083` – «Es dürfen nur die im Jahre»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0083.md) `ar-wl-2025__c0083` – «21 EDP dfi) beizulegen»

<a id="13-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 13.2 – Beiträge/Einkäufe in die 2. Säule (soweit nicht im Lohnausweis abgezogen)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ⚠️ strittig
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) mit Einkaufsberechnung; Lohnausweis Ziff. 10.1/10.2
- **Rein:** Bescheinigung Vorsorgeeinrichtung + Einkaufsberechnung → selbst bezahlte Beiträge/Einkäufe 2025 · Lohnausweis → Ziff. 10.1/10.2 (vom Lohn abgezogen = im Nettolohn, nicht hier) · Selbständige: Einkaufsbeiträge → hier statt Erfolgsrechnung
- **Rechnen:** Σ 2025 Beiträge/Einkäufe 2. Säule, soweit nicht bereits im Nettolohn (Lohnausweis) abgezogen; Selbständige: 100 % der Einkaufsbeiträge
- **Regel:** Nur Beiträge, die nicht schon vom Lohn abgezogen und damit im Nettolohn (Lohnausweis Ziff. 11) berücksichtigt sind. Lohnausweis Ziff. 10.2 (Einkauf, vom Lohn abgezogen) ist bereits abgezogen -> nicht doppelt hier. Selbst bezahlte Einkäufe: Bescheinigung der Pensionskasse mit Formular 21 EDP plus Einkaufsberechnung; bei Selbständigen 100 % der Einkaufsbeiträge hier. Einkauf: 3-Jahres-Sperre für Kapitalbezug (MB 08) beachten.
- **Beachten:** WL widersprüchlich: nicht im Nettolohn abgerechnete BVG-Beiträge auch unter Ziff. 16.6 genannt → nur einmal abziehen
- **Beachten:** Bescheinigung + Einkaufsberechnung in jedem Fall beilegen
- **Beachten:** Einkauf: Kapitalbezug (inkl. WEF) innert drei Jahren gesperrt; neuer Einkauf erst nach Rückzahlung WEF-Vorbezüge
- **Bund:** Einkauf in die 2. Säule bei der DBSt: Regeln nicht aus AR-Quellen belegt (Bund-Quellen prüfen).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). WL-intern widersprüchlich: Ziff. 13.2 (c0089, c0051, Hilfsformular) nimmt BVG-Beiträge/Einkäufe auf, Ziff. 1.1 (c0038) verweist für nicht im Nettolohn abgerechnete BVG-/NBUV-Beiträge auf Ziff. 16.6. Fachperson entscheidet; hier als Hauptzeile 13.2 geführt. Lohnausweis-Wegleitung gilt 2026 (jahr_ok).
- **Quellen:**
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0084.md) `ar-wl-2025__c0084` – «sind hier immer 100 % der Einkaufsbeiträge zu deklarieren»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0084.md) `ar-wl-2025__c0084` – «zulegen, zusammen mit der entsprechenden Einkaufsberechnung»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «nicht vom Lohn abgezogene Einkaufsbeiträge»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «Beiträge für den Einkauf von fehlenden Versicherungsjahren»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0035.md) `ar-wl-2025__c0035` – «bzw. im Lohnausweis nicht bereits abgerechnet sind, können unter der Ziffer 16.6 abgezogen werden»
  - [MB AR 08 S. 1](../../chunks/ar/dauernd/ar-mb-08/ar-mb-08__c0002.md) `ar-mb-08__c0002` – «innerhalb der nächsten drei Jahre nicht in Kapitalform bezogen werden»
  - [MB AR 08 S. 1](../../chunks/ar/dauernd/ar-mb-08/ar-mb-08__c0002.md) `ar-mb-08__c0002` – «erst wieder vorgenommen werden, wenn die gesamten Vorbezüge für Wohneigentum zurückbezahlt sind»

<a id="14-abzug-versicherungspraemien"></a>
### Ziff. 14 – Versicherungsprämien und Zinsen von Sparkapitalien (Übertrag Formular 6 Teil C, Code 600)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 6 Teil C: niedrigerer Betrag aus A (bezahlte Prämien/Sparzinsen abzüglich Prämienverbilligung) und B (Maximum)
- **Rein:** Krankenkassen-Prämienabrechnung 2025 → Form. 6 A a (brutto) · Verfügung Prämienverbilligung → Form. 6 A e (Abzug) · Police/Bescheinigung Lebens-, Renten-, Unfallversicherung → Form. 6 A b/c · Form. 2 Wertschriftenverzeichnis → Sparzinsen (Form. 6 A d)
- **Rechnen:** min(A = KK brutto + UV ohne NBUV + Leben/Rente + Sparzinsen − Prämienverbilligung; B = Kt. 5'400 gemeinsam / 2'700 übrige + 1'000 je Kind) → Code 600
- **Regel:** A = Krankenversicherung (brutto), Unfall (ohne NBUV), Lebens-/Rentenversicherung, Sparzinsen gemäss Wertschriftenverzeichnis, abzüglich Prämienverbilligungen; B = Max. Fr. 5'400 gemeinsam / Fr. 2'700 übrige plus Fr. 1'000 je Kind mit Kinderabzug 23.1-23.3. Abzug = niedrigerer Betrag von A und B. Ausgeschlossen: Mobiliar-, Motorfahrzeug-, Haftpflicht- und Sachversicherungen.
- **Beachten:** Bund: 3'700 gemeinsam / 1'800 übrige (ohne Beiträge 2. Säule/3a: 5'550 / 2'700) + 700 je Kind
- **Beachten:** Kinderzuschlag nur für Kinder mit Kinderabzug 23.1–23.3
- **Beachten:** Ausgeschlossen: Mobiliar-, Motorfahrzeug-, Haftpflicht- und andere Sachversicherungen
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'400 (Versicherungsprämien und Sparzinsen: in ungetrennter Ehe lebende Personen max. CHF 5'400 (abzüglich Prämienverbilligung).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'700 (Versicherungsprämien und Sparzinsen: übrige Steuerpflichtige max. CHF 2'700 (abzüglich Prämienverbilligung).)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag pro Kind (bzw. unterstützte Person mit Abzug nach Art. 38) CHF 1'000.)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – AR kennt keine Unterscheidung nach Beiträgen 2. Säule/3a beim Versicherungsabzug; einheitlicher Betrag (Art. 35 lit. g StG).** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an Säule 2/3a (Erhöhung um die Hälfte))**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – AR kennt keine Unterscheidung nach Beiträgen 2. Säule/3a beim Versicherungsabzug.** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an Säule 2/3a)**
- **Bund:** Versicherungsabzug beim Bund mit anderen Beträgen (data/werte/bund/2025.yaml); eine Berechnung im AR-Formular 6 nur für Staats-/Gemeindesteuer.
- **Bemerkung:** Code 600 (Hilfsblatt Form. 6, Hauptformular-Code für Ziff. 14 nicht separat verifiziert). Korrigiert durch Prüfung: Beleg hausrat-haftpflicht-police entfernt, da Mobiliar-/Haftpflicht-/Sachversicherungen vom Abzug ausgeschlossen sind.
- **Quellen:**
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Fr. 5’400 für gemeinsam Steuerpflichtige»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Fr. 2’700 für alleinstehende Steuerpflichtige»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Fr. 1’000 zusätzlich für jedes Kind»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Der niedrigere Betrag von (A) und (B) 600 13211 zu übertragen in die Steuererklärung Seite 3 Ziffer 14»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0085.md) `ar-wl-2025__c0085` – «Vom Abzug ausgeschlossen sind die Prämien für Mobiliar-, Motorfahrzeug- und»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0001.md) `ar-form-06-2025__c0001` – «Total bezahlte Versicherungsprämien und Sparzinsen 600 A»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t2.md) `bund-dbg-2025__art-33-t2` – «3700 Franken für Ehepaare, die in rechtlich und tatsächlich ungetrennter Ehe leben»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t5.md) `bund-dbg-2025__art-33-t5` – «um die Hälfte für Steuerpflichtige ohne Beiträge nach Absatz 1 Buchstaben d und e»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t5.md) `bund-dbg-2025__art-33-t5` – «um 700 Franken für jedes Kind»

<a id="15-abzug-liegenschaft-unterhalt"></a>
### Ziff. 15 – Unterhalts- und Verwaltungskosten Liegenschaften: Pauschalabzug (C1) oder tatsächliche Kosten (C2), Übertrag Formular 7/7Z

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Formular 7 Abschn. C bzw. Formular 7Z Spalte C1/C2
- **Rein:** Form. 7 Abschn. C je Liegenschaft (mehrere: Form. 7Z Total Spalte C1/C2) → Ziff. 15 · Handwerker-/Unterhaltsrechnungen → Form. 7 Rückseite (Anteil Unterhalt/Verwaltung, ohne Anlagekosten) · Prämien Brand-/Wasserschaden-/Glas-/Gebäudehaftpflichtversicherung, Wartung, Verwaltung → tatsächliche Kosten (C2) · Förderbeiträge/Versicherungsleistungen Dritter → Abzug von den Kosten
- **Rechnen:** je Gebäude wahlweise: Pauschale 10 % (≤ 10 J.) / 20 % (> 10 J.) × Erträge B; oder C2 = Σ Unterhalt/Verwaltung − Leistungen Dritter; Kanton = Bund 10/20 %
- **Regel:** Wahlrecht je Gebäude und Jahr: Pauschale 10 % (Gebäude bis und mit 10 Jahre) bzw. 20 % (über 10 Jahre) der Liegenschaftserträge (Ziff. B), nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes höchstens Fr. 100'000 beträgt und die Liegenschaft ganz/vorwiegend Wohnzwecken dient; sonst tatsächliche Kosten (Einzelbeträge ab Fr. 5'000 mit Rechnungskopien; Förderbeiträge Dritter abziehen). Pauschale umfasst alle Kosten inkl. Denkmalpflege.
- **Beachten:** Pauschale (Kanton) nur wenn Bruttomietertrag gesamter Besitz ≤ 100'000 und vorwiegend Wohnzwecke; deckt alle Kosten
- **Beachten:** Einzelbeträge ab 5'000: Rechnungskopien; wertvermehrende Aufwendungen nicht abziehbar
- **Beachten:** Eigengebrauch: Verbrauchs-, Heiz-, Abwasser-, Kehrichtkosten nicht abziehbar (Lebenshaltung)
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
  - [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0169.md) `ar-wl-2025__c0169` – «Nicht abzugsberechtigt sind Ausgaben, die eine Wertvermehrung der»
  - [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0170.md) `ar-wl-2025__c0170` – «Diese Kosten gelten als nicht abzugsfähige Lebenshaltungskosten»
  - [Formular 7 AR 2025 S. 2](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0005.md) `ar-form-07-2025__c0005` – «Abzugsfähig sind nur die selbst bezahlten Kosten. Versicherungsleistungen, Beiträge der öffentlichen Hand»
  - [Formular 7Z AR 2025 S. 1](../../chunks/ar/2025/ar-form-07z-2025/ar-form-07z-2025__c0003.md) `ar-form-07z-2025__c0003` – «Seite 2 Ziffer 5 Seite 3 Ziffer 15»

<a id="16-1-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. 16.1 – Verwaltungskosten Wertschriften/Kapitalanlagen (tatsächlich oder Pauschale)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Depotgebührenausweis der Bank / Steuerauszug (Bestand per 31.12. fremdverwalteter Titel)
- **Rein:** Bank: Gebühren-/Spesenausweis bzw. Steuerauszug → Depot-, Safegebühren, Inkassospesen (effektiv) · Form. 2 Wertschriftenverzeichnis → Total Steuerwerte drittverwaltet (Basis Pauschale)
- **Rechnen:** effektiv: Σ Depot-/Safegebühren + Inkassospesen; oder Kanton-Pauschale auf Antrag: Bestand ≤ 2 Mio. 3 ‰, max. 6'000; > 2 Mio. 1 ‰, max. 15'000
- **Regel:** Tatsächliche Depot-/Safegebühren, Inkassospesen oder auf Antrag Pauschale auf dem drittverwalteten Wertschriftenbestand (Total Steuerwerte, ohne eigene Unternehmensaktien, private Darlehen, Geschäftskonti): 3 Promille, max. Fr. 6'000 (bis 2 Mio.); über 2 Mio. 1 Promille, max. Fr. 15'000. Nicht abziehbar: Courtagen, Emissionsabgaben, Anlage-/Steuerberatung, Karten-Gebühren.
- **Beachten:** Basis ohne Aktien/GmbH-Anteile eigener Unternehmen, privat gewährte Darlehen, Geschäftskonti
- **Beachten:** Nicht abziehbar: Courtagen, Ausgabe-/Rücknahmekommissionen, Emissionsabgabe, Beratung, Bancomat-/Kreditkartengebühren
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Die Textstelle zur 2-Mio.-Grenze ist über die Chunks c0092-c0094 verteilt (Spalten-Layout), Originalseite 15 prüfen.
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «Fremdverwaltete Wertschriften und Kapitalanlagen 3 ‰, max. jedoch Fr. 6’000»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0089.md) `ar-wl-2025__c0089` – «jedoch Fr. 15’000.–»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0088.md) `ar-wl-2025__c0088` – «vermögen: 1 Promille des drittverwalteten Wertschrif»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0088.md) `ar-wl-2025__c0088` – «die Finanz-, Anlage-, Erbschafts-, Vorsorge- und Steuerberatung»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0087.md) `ar-wl-2025__c0087` – «bzw. GmbH-Stammanteile, privat gewährter Darlehen»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0087.md) `ar-wl-2025__c0087` – «Wertschriftenbestand kann auf Antrag folgender»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0087.md) `ar-wl-2025__c0087` – «den Erwerb und das Anlegen von Vermögenswerten»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0088.md) `ar-wl-2025__c0088` – «Gebühren für Bancomat- und Kreditkarten»

<a id="16-2-abzug-drittbetreuung"></a>
### Ziff. 16.2 – Kinderbetreuungskosten durch Drittpersonen (Übertrag Formular 10)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Formular 10 Total Kinderbetreuungskosten (Rechnungen Krippe/Tagesfamilie, Empfänger muss ersichtlich sein)
- **Rein:** Rechnungen/Quittungen Krippe, Hort, Tagesfamilie → Form. 10 je Kind (Empfänger ersichtlich) · Abrechnung Betreuungsbeiträge (Kinderbetreuungsgesetz) → Form. 10 «Abzüglich erhaltene Beiträge»
- **Rechnen:** je Kind < 14 J. im gleichen Haushalt: min(tatsächliche Kosten − Verpflegung − erhaltene Beiträge; Kanton 25'000 / Bund 25'800)
- **Regel:** Nachgewiesene Kosten bis max. Fr. 25'000 pro Kind unter 14 Jahren im gleichen Haushalt, in direktem Zusammenhang mit Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit; Ehepaare in ungetrennter Ehe nur, wenn beide gleichzeitig erwerbstätig bzw. in Ausbildung sind oder erwerbsunfähig und zugleich betreuungsunfähig; Konkubinatspaare analog. Ohne Verpflegung (Lebenshaltungskosten); Betreuungsbeiträge nach Kinderbetreuungsgesetz abziehen. Fahrkosten zur Betreuungsstätte zählen mit.
- **Beachten:** Ehepaare/Konkubinat: beide gleichzeitig erwerbstätig/in Ausbildung oder erwerbs- und betreuungsunfähig
- **Beachten:** Fahrkosten zur Betreuungsstätte zählen mit; Mittagstisch/Verpflegung nicht
- **Beachten:** Kosten nur bei direktem Zusammenhang mit Erwerb, Ausbildung oder Erwerbsunfähigkeit
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
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t7.md) `bund-dbg-2025__art-33-t7` – «jedoch höchstens 25 800 Franken, für die Drittbetreuung jedes Kindes»

<a id="16-3-abzug-parteispenden"></a>
### Ziff. 16.3 – Mitgliederbeiträge und Zuwendungen an politische Parteien (Code 555), Übertrag Formular 5 Teil B

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Formular 5 Teil B Total der Parteispenden
- **Rein:** Beitrags-/Spendenquittungen der Partei → Form. 5 Teil B, Total Code 555
- **Rechnen:** min(Σ 2025 Mitgliederbeiträge + Zuwendungen an Parteien; Kanton 10'000 pro Steuererklärung / Bund 10'600)
- **Regel:** Bis Fr. 10'000 pro Steuererklärung (gemeinsam Veranlagte zusammen) an im Parteienregister eingetragene bzw. im Kantonsparlament vertretene Parteien oder solche mit mind. 3 % Wähleranteil; nicht abziehbar: persönliche Wahlkampfkosten, Komitees, Beiträge direkt an Kandidaten.
- **Beachten:** Partei im Parteienregister, in einem kantonalen Parlament vertreten oder ≥ 3 % Stimmen (letzte Wahlen); Kanton = Bund
- **Beachten:** Nicht: persönliche Wahlkampfkosten, Komitees, Volksinitiativen, Beiträge direkt an Kandidaten
- **Beachten:** Kanton: Maximum gilt pro Steuererklärung, Ehepaare zusammen
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'000 (pro Steuererklärung).)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 10'000 (Gesamtbetrag CHF 10'000 gilt pro Steuererklärung, d.h. auch für gemeinsam Besteuerte (keine Verdoppelung).)** · Bund **n/a – Bund kennt nur einen Gesamtbetrag von CHF 10'600 (Art. 33 Abs. 1 lit. i DBG); keine Verdoppelung für Ehepaare in der Quelle.**
- **Bund:** Bundesmaximum abweichend (data/werte/bund/2025.yaml).
- **Bemerkung:** Code 555 aus Hilfsblatt Form. 5.
- **Quellen:**
  - [Formular 5 AR 2025 S. 2](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0004.md) `ar-form-05-2025__c0004` – «Total der Parteispenden 555 3213211 zu übertragen in die Steuererklärung Seite 3 Ziffer 16.3»
  - [WL AR 2025 S. 16–17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0092.md) `ar-wl-2025__c0092` – «Gesamtbetrag von Fr. 10’000.– (pro Steuererklärung) an politische Parteien»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t3.md) `bund-dbg-2025__art-33-t3` – «die Mitgliederbeiträge und Zuwendungen bis zum Gesamtbetrag von 10 600 Franken an politische Parteien»

<a id="16-4-abzug-weiterbildung"></a>
### Ziff. 16.4 – Berufsorientierte Aus- und Weiterbildungskosten inkl. Umschulung, Person 1 / Person 2 (Hauptformular, kein eigenes Hilfsblatt)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Kursrechnungen/Zahlungsbelege der steuerpflichtigen Person; Lohnausweis Ziff. 13.3 (Vergütungen des Arbeitgebers)
- **Rein:** Kurs-/Schulrechnungen + Zahlungsbelege → selbst getragene Kosten je Person · Lohnausweis → Ziff. 13.3 Vergütungen AG für Weiterbildung (Abgrenzung)
- **Rechnen:** je Person min(selbst getragene Kosten 2025; Kanton 12'000 / Bund 13'000); keine Pauschale
- **Regel:** Bis Fr. 12'000 pro Person nur nach erstem Abschluss Sek. II oder ab 20. Altersjahr (ohne Ausbildung bis zum ersten Abschluss); keine Pauschale; vom Arbeitgeber getragene Kosten sind nicht steuerbar und nicht zusätzlich als eigene Kosten abziehbar; dem Arbeitnehmer vergütete Beträge erscheinen im Lohnausweis Ziff. 13.3 (direkt an Dritte bezahlte nicht). Informatikmittel nur bei zwingendem Zusammenhang, bei privater Nutzung 50 %.
- **Beachten:** Nur nach erstem Abschluss Sek. II oder ab vollendetem 20. Lebensjahr (nicht Kosten bis zum ersten Abschluss)
- **Beachten:** Vom AG getragene Kosten: nicht steuerbar → nur selbst getragene Kosten abziehen
- **Beachten:** Informatikmittel nur bei zwingendem Bezug zur Weiterbildung; bei Privatnutzung 50 %
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 12'000 (Berufsorientierte Aus- und Weiterbildungskosten (inkl. Umschulung) bis CHF 12'000 pro steuerpflichtige Person.)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Bund:** Bundesmaximum abweichend (data/werte/bund/2025.yaml).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Lohnausweis-Wegleitung gilt für 2026 (jahr_ok), Ziff. 13.3 nur als Feldbeschreibung.
- **Quellen:**
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0003.md) `ar-wl-2025__c0003` – «Berufsorientierte Aus-/Weiterbildungskosten Person 1 max. Fr. 12’000»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «Nicht anzugeben sind Vergütungen, die direkt an Dritte (z. B. Bildungsinstitut) bezahlt werden»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0034.md) `ar-wl-2025__c0034` – «Nicht steuerbar sind die vom Arbeitgeber getragenen Kosten der berufs»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0093.md) `ar-wl-2025__c0093` – «Es werden keine pauschalen»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0093.md) `ar-wl-2025__c0093` – «das 20. Lebensjahr vollendet ist und es sich nicht um die Ausbildungskosten»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0093.md) `ar-wl-2025__c0093` – «werden, können nur 50 % der Aufwendungen bei den Aus- oder Weiterbildungs»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t4.md) `bund-dbg-2025__art-33-t4` – «bis zum Gesamtbetrag von 13 000 Franken»

<a id="16-6-abzug-uebrige"></a>
### Ziff. 16.6 – Übrige Abzüge (AHV-Beiträge Nichterwerbstätiger, Einsatzkosten Geldspiele, nicht im Nettolohn berücksichtigte NBUV-/BVG-Beiträge)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → AHV-Beitragsverfügung; Lohnausweis (NBUV/BVG-Abzüge Ziff. 9/10)
- **Rein:** AHV-Beitragsverfügung Nichterwerbstätige → bezahlte Beiträge 2025 · Gewinnbestätigung Geldspiele / Online-Spielerkonto → Einsatzkosten · Lohnausweis → NBUV-/BVG-Beiträge, die nicht im Nettolohn abgezogen sind
- **Rechnen:** Σ AHV-Beiträge Nichterwerbstätige + Einsatzkosten (5 % je steuerbarer Gewinn, max. 5'400; online Einsätze max. 26'800; Kanton = Bund) + NBUV/BVG nicht im Nettolohn
- **Regel:** AHV-Beiträge Nichterwerbstätiger; Einsatzkosten bei steuerbaren Geldspielgewinnen 5 %, max. Fr. 5'400 (Online-Spiele: Spieleinsätze max. Fr. 26'800); NBUV-Beiträge (und gemäss Ziff. 1.1 der WL auch BVG-Beiträge) nur, wenn nicht schon im Nettolohn bzw. Lohnausweis berücksichtigt (Regelfall: schon berücksichtigt -> kein nochmaliger Abzug). Abgrenzung zu Ziff. 13.2 siehe dort (WL widersprüchlich).
- **Beachten:** NBUV/BVG i.d.R. schon im Nettolohn (Ziff. 1.1/1.2) → kein nochmaliger Abzug
- **Beachten:** Ordentliche AHV-Beiträge Erwerbstätiger schon in Ziff. 1/2 berücksichtigt
- **Beachten:** Abgrenzung BVG zu Ziff. 13.2 in WL widersprüchlich → nur einmal abziehen
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). Ziff. 16.5 im Formular nicht beschrieben.
- **Quellen:**
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0094.md) `ar-wl-2025__c0094` – «Beiträge von nichterwerbstätigen steuerpflichtigen Personen (ordentliche»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0094.md) `ar-wl-2025__c0094` – «können 5 Prozent, jedoch höchstens Fr. 5’400.–, als Einsatzkosten»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0094.md) `ar-wl-2025__c0094` – «unter dieser Ziffer abgezogen werden»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0035.md) `ar-wl-2025__c0035` – «bzw. im Lohnausweis nicht bereits abgerechnet sind, können unter der Ziffer 16.6 abgezogen werden»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t7.md) `bund-dbg-2025__art-33-t7` – «werden 5 Prozent, jedoch höchstens 5400 Franken, als Einsatzkosten abgezogen»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t7.md) `bund-dbg-2025__art-33-t7` – «jedoch höchstens 26 800 Franken abgezogen»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0084.md) `ar-wl-2025__c0084` – «13.2 Als Beiträge an die Einrichtung der beruflichen Vorsorge (2. Säule) sind die von»

<a id="16-7-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 16.7 – Abzug Teilbesteuerung Beteiligungserträge (40 % der Erträge Ziff. 4.2)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Berechnung aus Ziff. 4.2 (Privatbeteiligungen ab 10 %)
- **Rein:** Form. 2 Wertschriftenverzeichnis → Erträge Code BP (Privatbeteiligung mind. 10 %) = Ziff. 4.2 · Dividendenbelege/Steuerauszug → Bruttoertrag der Beteiligung
- **Rechnen:** Kanton: Abzug = Ertrag Ziff. 4.2 (bzw. 4.3 Geschäftsbeteiligung) − 60 % davon (steuerbar bleiben 60 %) / Bund: steuerbar 70 % (Art. 20 Abs. 1bis, Art. 18b DBG)
- **Regel:** Erträge aus Beteiligungen ab 10 % sind nur zu 60 % steuerbar: Abzug = 40 % des in Ziff. 4.2 deklarierten Bruttoertrags (Abzug steht in Ziff. 16.7).
- **Beachten:** Nur Beteiligung ≥ 10 % am Grund-/Stammkapital; Kanton: Gesellschaft mit Sitz in der Schweiz
- **Beachten:** Geschäftsbeteiligung (Code BG): Reingewinn kürzen, Ertrag in Ziff. 4.3 → sonst kein Teilbesteuerungsabzug
- **Bund:** Teilbesteuerungsquote DBSt: eigene Regelung (nicht aus AR-Quellen).
- **Bemerkung:** Code nicht verifiziert (Seite 3 der Steuererklärung ist in der WL nicht als Miniatur abgebildet). 40 %-Satz ist die Ergänzung zu den belegten 60 % steuerbar.
- **Quellen:**
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0095.md) `ar-wl-2025__c0095` – «Der entsprechende Abzug für das Teilbesteuerungsverfahren kann auf der Seite 3, Ziffer 16.7, in Abzug gebracht»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0095.md) `ar-wl-2025__c0095` – «sind im Umfang von 60 Prozent steuerbar, wenn diese Beteili»
  - [WL AR 2025 S. 11](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0057.md) `ar-wl-2025__c0057` – «Sitz in der Schweiz werden nur zu 60 Prozent besteuert»
  - [WL AR 2025 S. 11](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0057.md) `ar-wl-2025__c0057` – «Gehört eine solche Beteiligung zum Geschäftsvermögen selbständig Erwerbender»
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «Abzüglich Erträge aus Privatbeteiligung (BP) Übertrag in Steuererkl. Ziff. 4.2»
  - [DBG Art. 20](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-20-t3.md) `bund-dbg-2025__art-20-t3` – «sind im Umfang von 70 Prozent steuerbar, wenn diese Beteiligungsrechte mindestens 10 Prozent»
  - [StG AR Art. 21b](../../chunks/ar/2025/ar-stg/ar-stg__art-21b.md) `ar-stg__art-21b` – «sind nach Abzug des zurechenbaren Aufwandes im Umfang von 60 Prozent steuerbar»
  - [DBG Art. 18b](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-18b.md) `bund-dbg-2025__art-18b` – «sind nach Abzug des zurechenbaren Aufwandes im Umfang von 70 Prozent steuerbar»

<a id="17-abzug-zweiverdiener"></a>
### Ziff. 17 – Zweiverdienerabzug (gemeinsam veranlagte, beide erwerbstätig)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechnung aus den beiden Nettoerwerbseinkommen
- **Rein:** Lohnausweise beider Partner → Nettolohn (Ziff. 1.1/1.2 StE); Selbständige: Reingewinn (Ziff. 2) · Form. 4 Total, 3a-Bescheinigung, BVG-Einkauf je Partner → Abzüge vom Erwerbseinkommen
- **Rechnen:** E = niedrigeres Erwerbseinkommen (Nettolohn/Reingewinn − Berufskosten − 3a − BVG-Einkauf); Kanton: E > 2'500 → 10 % × E, min. 2'500, max. 5'200; E < 2'500 → E
- **Regel:** 10 % des niedrigeren Erwerbseinkommens (nach allen damit zusammenhängenden Abzügen: Berufskosten, 3a, BVG-Einkauf), mind. Fr. 2'500, max. Fr. 5'200; unter Fr. 2'500: Abzug in Höhe des niedrigeren Einkommens; bei Fr. 0 kein Abzug. Bei Mitarbeit im Geschäft des Partners Einkommen hälftig aufteilen.
- **Beachten:** Bund: 50 % × E, min. 8'600, max. 14'100 (Art. 33 Abs. 2 DBG)
- **Beachten:** Abzug + Berufskosten + 3a + BVG-Einkauf ≤ massgebender Nettolohn bzw. Reingewinn
- **Beachten:** Erhebliche Mitarbeit im Geschäft des Partners: Erwerbseinkommen i.d.R. je hälftig aufteilen
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
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t6.md) `bund-dbg-2025__art-33-t6` – «vom niedrigeren Erwerbseinkommen 50 Prozent, jedoch mindestens 8600 Franken und höchstens 14 100 Franken abgezogen»
  - [WL AR 2025 S. 17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0096.md) `ar-wl-2025__c0096` – «Der Abzug darf zusammen»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben inkl. Kryptowährungen (Code 300), Übertrag Formular 2

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Formular 2 Total Steuerwert per 31.12.2025 (Spalte 'Steuerwert am 31. Dezember 2025'); Steuerauszug (eCH-0196)
- **Rein:** Steuerauszug/Depotverzeichnis Bank per 31.12.2025 → Steuerwert (Auszug vollständig beilegen) · Zins- und Saldomeldungen Bankkonti → Guthaben 31.12.2025 · Krypto-Auszug (Bitcoin, Ether) → Bestand 31.12.2025 · Kauf-/Verkaufsbelege; Darlehensvertrag ab 50'000; Arbeitgeberbescheinigung Mitarbeiteraktien/-optionen
- **Rechnen:** Form. 2: Σ Steuerwerte Ende 2025 − «G»-Titel → 30.1 (Code 300; Erträge → 4.1); kotiert: ESTV-Kursliste, nichtkotiert: innerer Wert, Fremdwährung: Devisenkurs
- **Regel:** Stand per 31.12.2025; kotierte Wertpapiere: offizieller Steuerwert am Ende des Jahres 2025 gemäss Kursliste der ESTV; Kryptowährungen mit erfassen; Bestandesveränderungen (Erwerb, Veräusserung, Rückzahlung, Konversion) mit Datum des Zu- oder Abganges und Bankbelegen.
- **Beachten:** Nicht deklarieren: Ansprüche 2. Säule und Säule 3a (bis Fälligkeit steuerfrei)
- **Beachten:** Inkl. Vermögen minderjähriger Kinder + Nutzniessungsvermögen; Bestandesänderung: Datum Spalte 5/6 + Bankbelege
- **Beachten:** Nichtkotiert, Steuerwert unbekannt: Anzahl, Titel gemäss HR, Nennwert, letztbekannter Steuerwert angeben
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 30.1 Seite 2 Ziffer 4.1»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0113.md) `ar-wl-2025__c0113` – «gen Kapitalanlagen sind im Wertschriften- und Guthabenverzeichnis (Formular 2)»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «300 213213211»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0128.md) `ar-wl-2025__c0128` – «rungen wie Bitcoin, Ether etc.).»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0128.md) `ar-wl-2025__c0128` – «oder Abganges anzugeben und die Bankbelege beizulegen.»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0128.md) `ar-wl-2025__c0128` – «Massgebend ist in der Regel»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0134.md) `ar-wl-2025__c0134` – «Dieser kann der Kursliste der Eidg. Steuerverwaltung entnommen werden.»
  - [WL AR 2025 S. 4](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0010.md) `ar-wl-2025__c0010` – «die Steuerauszüge und Depotverzeichnisse der Banken;»
  - [WL AR 2025 S. 4](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0010.md) `ar-wl-2025__c0010` – «die Zins- und Saldomeldungen der Bankguthaben;»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0129.md) `ar-wl-2025__c0129` – «dem Formular 2 vollständig beizulegen»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0130.md) `ar-wl-2025__c0130` – «sind die betreffenden Kaufs- bzw. Verkaufsbelege oder allenfalls die entspre»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0130.md) `ar-wl-2025__c0130` – «Bei Darlehen ab Fr. 50’000.– ist eine Kopie des Darlehensvertrags beizulegen.»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0130.md) `ar-wl-2025__c0130` – «Bei Mitarbeiteraktien und -optionen muss die vom Arbeitgeber ausgestellte Be»
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «Abzüglich Geschäftswertschriften bzw. -erträge (G)»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0134.md) `ar-wl-2025__c0134` – «Der Verkehrswert nichtkotierter Wertpapiere wird nach dem inneren Wert»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0134.md) `ar-wl-2025__c0134` – «Nennwertes und – soweit möglich – des letztbekannten Steuerwertes»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0135.md) `ar-wl-2025__c0135` – «Die Umrechnung von Kursen aus fremden Währungen in Franken erfolgt zum»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0111.md) `ar-wl-2025__c0111` – «gebundener Selbstvorsorge (Säule 3a) stellen bis zu ihrer Fälligkeit steuerfreies»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0128.md) `ar-wl-2025__c0128` – «Kinder einschliesslich Nutzniessungsvermögen anzugeben»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 302)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Aufstellung/Bewertung zum Verkehrswert per 31.12.
- **Rein:** Bargeldbestand CHF und Fremdwährungen → Betrag per 31.12.2025 · Gold/Edelmetalle (Bestand) → Verkehrswert gemäss ESTV-Kursliste
- **Rechnen:** Σ (inländisches + ausländisches Bargeld + Gold/Edelmetalle) zum Verkehrswert per 31. Dezember 2025 (Werte: ESTV-Kursliste) → 30.2 (Code 302)
- **Regel:** Inländisches und ausländisches Bargeld sowie Gold/Edelmetalle zum Verkehrswert (ESTV-Kursliste).
- **Beachten:** Bank-/Postguthaben nicht hier, sondern im Form. 2 (Ziff. 30.1)
- **Beachten:** Schmuck = steuerfreier Gebrauchsgegenstand; Wert deutlich über dem Üblichen → Ziff. 30.6
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0113.md) `ar-wl-2025__c0113` – «30.2 Unter dieser Ziffer sind nebst dem inländischen Bargeld auch das ausländische»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «302»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0113.md) `ar-wl-2025__c0113` – «Bargeld, Gold und andere Edelmetalle mit dem Verkehrswert einzusetzen»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0113.md) `ar-wl-2025__c0113` – «amtliche Kursliste der Eidgenössischen Steuerverwaltung enthält die massgeben»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0113.md) `ar-wl-2025__c0113` – «Die Wertschriften und Guthaben des Privatvermögens einschliesslich aller sonsti»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0111.md) `ar-wl-2025__c0111` – «Massgebend ist in der Regel»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0112.md) `ar-wl-2025__c0112` – «Kleider, Schmuck, Sportgeräte, Foto- und Filmapparate»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0112.md) `ar-wl-2025__c0112` – «das gemeinhin Übliche deutlich übersteigt oder mit denen erhebliche Wertzu»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen mit Rückkaufswert (Code 304) mit Versicherungsgesellschaft, Abschluss-/Ablaufjahr, Versicherungssumme

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Steuerwertbescheinigung der Versicherungsgesellschaft (Rückkaufswert + Überschussguthaben)
- **Rein:** Steuerwertbescheinigung Versicherer per 31.12.2025 → Rückkaufswert + Überschussguthaben · Police → Versicherungsgesellschaft, Abschluss-/Ablaufjahr, Versicherungssumme
- **Rechnen:** Σ je Police: Rückkaufswert + Überschussguthaben/Gewinnbeteiligung → 30.3 (Code 304)
- **Regel:** Steuerwert = Rückkaufswert + Überschussguthaben/Gewinnbeteiligung; Rentenversicherungen mit aufgeschobener Rente ebenfalls; Rückkaufswert laufender Renten wird als Vermögen besteuert; Bescheinigung beilegen. Ansprüche gegenüber Einrichtungen der beruflichen Vorsorge (2. Säule) und aus gebundener Selbstvorsorge (Säule 3a) sind bis zur Fälligkeit steuerfreies Vermögen.
- **Beachten:** Nur rückkaufsfähige Lebens- und Rentenversicherungen mit Rückgewähr; aufgeschobene und laufende Renten ebenfalls
- **Beachten:** Säule 3a und 2. Säule nicht deklarieren (bis Fälligkeit steuerfrei)
- **Beachten:** Berechnung/Bescheinigung der Versicherungsgesellschaft beilegen
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0114.md) `ar-wl-2025__c0114` – «wert (= Rückkaufswert + Überschussguthaben/Gewinnbeteiligung)»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «304 213213211 306»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0111.md) `ar-wl-2025__c0111` – «gebundener Selbstvorsorge (Säule 3a) stellen bis zu ihrer Fälligkeit steuerfreies»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0114.md) `ar-wl-2025__c0114` – «Rückkaufsfähige Lebensversicherungen und Rentenversicherungen mit Rückge»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0114.md) `ar-wl-2025__c0114` – «Der Rückkaufswert laufender Renten»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0114.md) `ar-wl-2025__c0114` – «Steuererklärung beizulegen. Rentenversicherungen mit aufgeschobenen Renten»
  - [WL AR 2025 S. 4](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0010.md) `ar-wl-2025__c0010` – «die Bescheinigungen der Versicherungsgesellschaften über den Steuerwert (Rück-»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge mit Art, Kaufpreis, Erwerbsjahr (Code 306)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg, Motorfahrzeug-Versicherungspolice (Haftpflicht/Kasko) und Verkehrssteuer-Rechnung → Kaufbeleg/Fahrzeugausweis (Anschaffungswert, Erwerbsjahr)
- **Rein:** Kaufvertrag/Rechnung → Kaufpreis (Anschaffungswert), Erwerbsjahr · Fahrzeugausweis → Art des Fahrzeugs
- **Rechnen:** Anschaffungswert − 20 % des Anschaffungswerts × Jahre seit Erwerb (inkl. Steuerjahr 2025) → 30.4 (Code 306)
- **Regel:** Steuerwert = Anschaffungswert abzüglich 20 % pro Jahr seit Erwerb (inkl. Steuerjahr).
- **Beachten:** Motorfahrzeuge sind kein steuerfreier Gebrauchsgegenstand → deklarieren
- **Beachten:** Fahrzeuge des Geschäftsvermögens → Betriebsvermögen Ziff. 32, nicht hier
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0114.md) `ar-wl-2025__c0114` – «Wertverminderung von 20 Prozent vom Anschaf»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «304 213213211 306»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0112.md) `ar-wl-2025__c0112` – «Nicht dazu zählen Motorfahrzeuge, Boote, Reitpferde und»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0117.md) `ar-wl-2025__c0117` – «mente, Mobilien, Fahrzeuge sowie entgeltlich erworbene immaterielle Güter.»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Anteil an unverteilter Erbschaft (Code 308), mit Aufstellung

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Inventar und Erbenverzeichnis (Kopie beilegen)
- **Rein:** Inventar + Erbenverzeichnis (Kopie) → Erbanteil · Form. 2 Seite 1 → Frage unverteilte Erbschaft, Erbanteil ohne Liegenschaften (Code 961) · Aufstellung der Nachlassaktiven → Anteil je Vermögensart
- **Rechnen:** Erbanteil (inkl. Nutzniessungsvermögen) bewertet nach Ziff. 30/31, soweit nicht schon in anderen Ziffern → 30.5 (Code 308)
- **Regel:** Sämtliche Ansprüche eines Erben/Vermächtnisnehmers an einem ungeteilten Nachlass (auch Nutzniessung Dritter); auch bei noch nicht feststehenden Anteilen; Bewertung nach Ziff. 30/31; Liegenschaftsanteile im Formular 7; zusätzlich Form. 2 Seite 1 (Code 961).
- **Beachten:** Auch anzugeben, wenn Anteile zahlenmässig noch nicht feststehen; auch bei Nutzniessung zugunsten Dritter
- **Beachten:** Liegenschaften des Nachlasses im Form. 7 (→ Ziff. 31)
- **Beachten:** Erträge des Nachlasses anteilig in Ziff. 6.2 mit detaillierter Aufstellung
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0115.md) `ar-wl-2025__c0115` – «Der Anteil an einer unverteilten Erbschaft umfasst sämtliche Ansprüche»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «308 213213»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «Sind Sie an einer unverteilten Erbschaft beteiligt?»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «13213211 961»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «Diese sind im Liegenschaftsformular 7 zu deklarieren.»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0115.md) `ar-wl-2025__c0115` – «Erbschaft ist auch dann anzugeben, wenn die Anteile zahlenmässig noch nicht»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0115.md) `ar-wl-2025__c0115` – «und 31. Eine Deklaration hat in Ziffer 30.5 zu erfolgen, sofern die Anteile nicht»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0061.md) `ar-wl-2025__c0061` – «Einkünfte aus unverteilten Erbschaften und andern Vermögensmassen werden»
  - [WL AR 2025 S. 12](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0061.md) `ar-wl-2025__c0061` – «künfte sind daher unter Beilage einer detaillierten Aufstellung anzugeben.»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte (Boote, Reitpferde, Kunstsammlungen u.a.) (Code 310)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Private Alltagsrechnungen (Lebensmittel, Kleider, Telefon/Internet, Strom privat, Freizeit, Ferien) → Aufstellung der Vermögenswerte mit Verkehrswert
- **Rein:** Aufstellung der Vermögenswerte → Art und Verkehrswert (Boote, Reitpferde, Kunst-/wertvolle Sammlungen) · Kaufbelege/Bewertungen → mutmasslicher Verkehrswert per 31.12.2025
- **Rechnen:** Σ mutmasslicher Verkehrswert je Objekt per 31. Dezember 2025 → 30.6 (Code 310)
- **Regel:** Mutmasslicher Verkehrswert; Hausrat und persönliche Gebrauchsgegenstände sind steuerfrei, nicht deklarieren.
- **Beachten:** Hausrat und persönliche Gebrauchsgegenstände (Möbel, Kleider, Schmuck, Sportgeräte) steuerfrei – nicht deklarieren
- **Beachten:** Aber: Gegenstände/Sammlungen deutlich über dem Üblichen oder mit erheblichem Wertzuwachspotenzial → hier
- **Beachten:** Motorfahrzeuge in eigener Ziff. 30.4
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0116.md) `ar-wl-2025__c0116` – «Für die Bewertung der übrigen Vermögenswerte ist in der Regel der mutmassli»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «310 213213»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0111.md) `ar-wl-2025__c0111` – «Nicht anzugeben sind der Hausrat und die persönlichen Gebrauchsgegen»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0112.md) `ar-wl-2025__c0112` – «Kleider, Schmuck, Sportgeräte, Foto- und Filmapparate»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0111.md) `ar-wl-2025__c0111` – «Möbel, Teppiche, Bilder, Küchen- und Gartengeräte, Geschirr, Bücher sowie Gerä»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0116.md) `ar-wl-2025__c0116` – «Wertzuwachsgewinne erzielt werden können»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0111.md) `ar-wl-2025__c0111` – «Massgebend ist in der Regel»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0114.md) `ar-wl-2025__c0114` – «Für die Ermittlung des Steuerwertes von Motorfahrzeugen»

<a id="31-vermoegen-liegenschaften"></a>
### Ziff. 31 – Liegenschaften, Steuerwert (Code 710), Übertrag Formular 7 Abschn. A / 7Z

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Formular 7 Abschn. A Steuerwert; amtliche Schätzung (vom Grundbuchamt eröffnet)
- **Rein:** Formular 7 Abschn. A → Steuerwert je Liegenschaft (bei mehreren: Total Form. 7Z) · Amtliche Schätzung (vom Grundbuchamt eröffnet) → Verkehrs-/Ertragswert, Grundstücknummer · Ausserkantonal/Ausland → dortiger Steuerwert bzw. mutmasslicher Verkehrswert
- **Rechnen:** Σ Steuerwerte (Form. 7 bzw. 7Z) → 31 (Code 710); AR: amtl. Verkehrs-/Ertragswert, ausserkantonal: dortiger Steuerwert, Ausland: mutmasslicher Verkehrswert
- **Regel:** AR: amtlicher Verkehrs-/Ertragswert gemäss Schätzung; andere Kantone: dortiger Steuerwert; Ausland: mutmasslicher Verkehrswert. Neu-/Anbauten ohne Schätzung: Zuschlag 80 % der Baukosten. Pro Liegenschaft ein Formular 7, bei mehreren Zusammenzug Form. 7Z.
- **Beachten:** Neu-/Anbau ohne Schätzung: i.d.R. amtl. Wert + 80 % der Baukosten (landwirtschaftlich: Ertragswert + 20 %)
- **Beachten:** Geschäftsliegenschaften ebenfalls hier zum amtlichen Wert; deren Buchwert in Ziff. 32.2 abziehen
- **Beachten:** Zugang/Wegfall 2025 mit Datum + Grund im Form. 7; auch Baurechte/Dienstbarkeiten im Grundbuch
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0001.md) `ar-form-07-2025__c0001` – «Übertrag in die Steuererklärung Seite 4 Ziffer 31»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0117.md) `ar-wl-2025__c0117` – «mitteln und gesamthaft in Ziffer 31 der Steuererklärung zu übertragen»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0165.md) `ar-wl-2025__c0165` – «im Ausland gelegene Grundstücke mit dem mutmasslichen»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0165.md) `ar-wl-2025__c0165` – «im Ausmass von 80 Prozent der Neu- oder An»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «710 213213»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0164.md) `ar-wl-2025__c0164` – «sich nach der amtlichen Verkehrs- oder Ertragswertschätzung»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0165.md) `ar-wl-2025__c0165` – «Der massgebliche Steuerwert wird vom Grundbuchamt eröffnet.»
  - [StG AR Art. 48](../../chunks/ar/2025/ar-stg/ar-stg__art-48.md) `ar-stg__art-48` – «Zuschlag zum geltenden amtlichen Ertragswert von 20 Prozent der Aufwendungen»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0120.md) `ar-wl-2025__c0120` – «jedem Fall zum amtlichen Verkehrswert erfasst werden und unter Ziffer 31 anzu»
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0001.md) `ar-form-07-2025__c0001` – «Zugang bzw. Wegfall der Liegenschaft im Jahr 2025»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0117.md) `ar-wl-2025__c0117` – «und die im Grundbuch eingetragenen selbständigen und dauernden Rechte»
  - [WL AR 2025 S. 29](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0161.md) `ar-wl-2025__c0161` – «Pro Liegenschaft ist je ein Formular 7 auszufüllen.»

<a id="32-1-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.1 – Geschäftskapital in Kollektiv-, Kommandit- und einfachen Gesellschaften (Code 314), mit Aufstellung

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Angaben/Bilanz der Gesellschaft (Anteil am Vermögen)
- **Rein:** Abschluss/Angaben der Kollektiv- oder Kommanditgesellschaft → Anteil am Gesellschaftsvermögen · Abrechnung einfache Gesellschaft → Anteil am Geschäftsvermögen · Form. 2 Seite 1 → Frage Beteiligung an Kollektiv-/Kommanditgesellschaft (Firma)
- **Rechnen:** Anteil am Vermögen der Gesellschaft, bewertet wie Ziff. 32 (Anschaffungswert − Entwertung = i.d.R. Buchwert) → 32.1 (Code 314)
- **Regel:** Anteil am Vermögen der Gesellschaft; Bewertung wie Ziff. 32 (Einkommenssteuerwert/Buchwert).
- **Beachten:** Waren/Vorräte: Anschaffungs-/Herstellungskosten, tieferer Marktwert massgebend
- **Beachten:** Debitoren: Delkredere nach Verlustwahrscheinlichkeit zulässig
- **Beachten:** Liegenschaften sinngemäss nicht hier: Form. 7 → Ziff. 31 (amtlicher Wert)
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Taxonomie hat keinen eigenen Schlüssel für Geschäftsvermögen; Zuordnung zu vermoegen.erbschaften_beteiligungen (Geschäftsvermögen).
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0119.md) `ar-wl-2025__c0119` – «32.1 Für das Geschäftsvermögen in Kollektiv-, Kommandit- oder einfachen Gesell»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0106.md) `ar-wl-2025__c0106` – «314 213213211»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0117.md) `ar-wl-2025__c0117` – «Massgebend ist der Anschaffungswert, vermindert um die eingetretene»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0118.md) `ar-wl-2025__c0118` – «schaffungs- oder Herstellungskosten bewertet. Ist der Marktwert niedriger, so»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0119.md) `ar-wl-2025__c0119` – «Für unsichere oder bestrittene Forderungen»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0117.md) `ar-wl-2025__c0117` – «Die massgebenden Liegenschaftswerte sind im Formular 7 pro Liegenschaft zu er»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0004.md) `ar-form-02-2025__c0004` – «Sind Sie an einer Kollektiv- oder Kommanditgesellschaft beteiligt?»

<a id="32-2-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.2 – Geschäftsaktiven gemäss Schlussbilanz (ohne Liegenschaften) (Code 316)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Schlussbilanz/Zusammenstellung Betriebsvermögen
- **Rein:** Schlussbilanz der 2025 abgeschlossenen Geschäftsjahre (oder Zusammenstellung Betriebsvermögen) → Total Aktiven · Schlussbilanz → Buchwert Geschäftsliegenschaften (abziehen) · Form. 2 → Geschäftswertschriften mit Vermerk «G»
- **Rechnen:** Total Aktiven Schlussbilanz − Buchwert Liegenschaften → 32.2 (Code 316)
- **Regel:** Aktiven gemäss letzter Schlussbilanz; Buchwert der Liegenschaften abziehen (Ziff. 31 zum amtlichen Wert); Betriebsschulden im Formular 5 B -> Ziff. 34.2; Wertschriften des Geschäftsvermögens im Formular 2 mit Code G.
- **Beachten:** Liegenschaften zum amtlichen Verkehrswert in Ziff. 31 (Form. 7)
- **Beachten:** Betriebsschulden im Form. 5 Teil B → Ziff. 34.2
- **Beachten:** Geschäftswertschriften im Form. 2 mit «G»; dort vom Übertrag Ziff. 30.1 abgezogen
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0120.md) `ar-wl-2025__c0120` – «32.2 Die Geschäftsaktiven sind der letzten Schlussbilanz oder der erfolgten Zusam»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0107.md) `ar-wl-2025__c0107` – «andit- und 316»
  - [WL AR 2025 S. 4](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0010.md) `ar-wl-2025__c0010` – «periode abgeschlossenen Geschäftsjahre;»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0117.md) `ar-wl-2025__c0117` – «Die massgebenden Liegenschaftswerte sind im Formular 7 pro Liegenschaft zu er»
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0002.md) `ar-form-05-2025__c0002` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 34.2»
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «Abzüglich Geschäftswertschriften bzw. -erträge (G)»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0119.md) `ar-wl-2025__c0119` – «Geschäftsvermögens sind im Wertschriften- und Guthabenverzeichnis (Formu»

<a id="32-3-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 32.3 – Vermögen im landwirtschaftlichen Betrieb (Code 318)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Spezielle Landwirte-Formulare (12/14)
- **Rein:** Landwirte-Formulare 12 bzw. 14 → Vermögen im landwirtschaftlichen Betrieb
- **Rechnen:** Wert gemäss Landwirte-Formularen 12/14 und deren speziellen Erläuterungen → 32.3
- **Regel:** Besondere Erläuterungen zu den Landwirte-Formularen beachten.
- **Beachten:** Landwirtschaftliche Grundstücke (bäuerliches Bodenrecht) nicht hier: Form. 7 → Ziff. 31, zum Ertragswert
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0120.md) `ar-wl-2025__c0120` – «32.3 Für die Angaben zum Vermögen im landwirtschaftlichen Betrieb sind die spezi»
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0001.md) `ar-form-07-2025__c0001` – «Landwirtschaft mit Bauten»
  - [StG AR Art. 48](../../chunks/ar/2025/ar-stg/ar-stg__art-48.md) `ar-stg__art-48` – «sind zum Ertragswert zu bewerten»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 322)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 30-32)
- **Rein:** Übertrag Ziff. 30.1–30.6, 31, 32.1–32.3
- **Rechnen:** Σ Ziff. 30.1–30.6 + 31 + 32.1–32.3 → 33 (Code 322)
- **Regel:** Summe Ziff. 30.1-32.3.
- **Beachten:** Stichtag: Stand 31. Dezember 2025
- **Beachten:** Inkl. Vermögen minderjähriger Kinder unter elterlicher Sorge/Obhut und Nutzniessungsvermögen
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0107.md) `ar-wl-2025__c0107` – «gemäss b 322»
  - [WL AR 2025 S. 20](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0113.md) `ar-wl-2025__c0113` – «Die Wertschriften und Guthaben des Privatvermögens einschliesslich aller sonsti»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0111.md) `ar-wl-2025__c0111` – «Massgebend ist in der Regel»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0107.md) `ar-wl-2025__c0107` – «mögen der steuerpflichtigen Person und der unter elterlicher Sorge oder Obhut»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «dem die steuerpflichtige Person Nutzniessungsrechte hat»

<a id="34-1-schulden-privat"></a>
### Ziff. 34.1 – Privatschulden (Code 504), Übertrag Formular 5 Teil A

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 5 Teil A Schuld am 31.12.2025 (Total); Hypothekar-/Kreditbestätigung
- **Rein:** Formular 5 Teil A → Schuld am 31.12.2025 je Gläubiger (Total) · Hypothekar-/Kreditbestätigung, Darlehensvertrag → Saldo 31.12.2025 + Zinsen 2025 · Steuerauszug Bank → Hypotheken/Kredite
- **Rechnen:** Σ private Schulden je Gläubiger am 31. Dezember 2025 (Form. 5 A Total) → 34.1 (Code 504); Schuldzinsen 2025 → Ziff. 11
- **Regel:** Schuldbestand per 31.12.2025 je Gläubiger; Solidar-/Bürgschaftsschulden nur soweit selbst zu tragen; Steuerverwaltung kann nähere Angaben verlangen. Zinsen gleiches Formular -> Ziff. 11.
- **Beachten:** Nur ausgewiesene Verpflichtungen; Solidar-/Bürgschaftsschulden nur soweit selbst zu tragen
- **Beachten:** Geschäftsschulden nicht hier → Form. 5 Teil B / Ziff. 34.2
- **Beachten:** Belege auf Verlangen; Steuerverwaltung kann nähere Angaben zum Schuldverhältnis verlangen
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0001.md) `ar-form-05-2025__c0001` – «Total private Schulden und private Schuldzinsen 213213211 13213211»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0121.md) `ar-wl-2025__c0121` – «Als Schulden, die vom Vermögen in Abzug gebracht werden können, werden alle»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0107.md) `ar-wl-2025__c0107` – «504 –»
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0001.md) `ar-form-05-2025__c0001` – «Seite 3 Ziffer 11»
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0002.md) `ar-form-05-2025__c0002` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 34.2»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0121.md) `ar-wl-2025__c0121` – «Schuld (Solidar- oder Bürgschaftsschuld), so wird der Abzug nur insoweit ge»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0121.md) `ar-wl-2025__c0121` – «nähere Angaben über das Schuldverhältnis verlangen»

<a id="34-2-schulden-privat"></a>
### Ziff. 34.2 – Geschäftsschulden (Code 506), Übertrag Formular 5 Teil B

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Formular 5 Teil B Total Geschäftsschulden (per Bilanzstichtag)
- **Rein:** Formular 5 Teil B → Schuld am 31.12.2025 bzw. Bilanzstichtag je Gläubiger (Total) · Schlussbilanz → Betriebsschulden (Fremdkapital)
- **Rechnen:** Σ Geschäftsschulden am 31. Dezember 2025 bzw. Bilanzstichtag (Form. 5 B Total) → 34.2 (Code 506)
- **Regel:** Betriebsschulden per 31.12. bzw. Bilanzstichtag; geschäftliche Schuldzinsen gehören in die Jahresrechnung, nicht in Ziff. 11.
- **Beachten:** Geschäftliche Schuldzinsen gehören in die Jahresrechnung, nicht ins Schuldenverzeichnis
- **Beachten:** Solidar-/Bürgschaftsschulden nur soweit selbst zu tragen
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0002.md) `ar-form-05-2025__c0002` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 34.2»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0107.md) `ar-wl-2025__c0107` – «506 –»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0120.md) `ar-wl-2025__c0120` – «Die Betriebsschulden sind im Schuldenverzeichnis (Formular 5) einzu»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0121.md) `ar-wl-2025__c0121` – «Schuld (Solidar- oder Bürgschaftsschuld), so wird der Abzug nur insoweit ge»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Reinvermögen (Code 326)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 33 abzüglich 34)
- **Rein:** Übertrag Ziff. 33 (Total Vermögenswerte) · Übertrag Ziff. 34.1 + 34.2 (Schulden)
- **Rechnen:** Ziff. 33 − (34.1 + 34.2) → 35 (Code 326)
- **Regel:** Total Vermögenswerte abzüglich Schulden.
- **Beachten:** Vermögenswerte auch deklarieren, wenn nach Abzug der Schulden kein steuerbares Vermögen bleibt
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «326»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0109.md) `ar-wl-2025__c0109` – «der Regel mit dem Verkehrswert anzugeben. Einzusetzen sind auch die Vermö»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0110.md) `ar-wl-2025__c0110` – «genswerte, aus denen sich nach Abzug der Schulden und/oder der Sozialabzüge»

<a id="36-1-vermoegen-sozialabzug"></a>
### Ziff. 36.1 – Sozialabzug alleinstehende Steuerpflichtige (Code 330)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien (Zivilstand 31.12.2025)
- **Rein:** Personalien → Zivilstand am 31.12.2025 (nicht in ungetrennter Ehe)
- **Rechnen:** Kanton: 75'000 (Verhältnisse am Ende der Steuerperiode, i.d.R. 31. Dezember 2025) / Bund: keine Vermögenssteuer
- **Regel:** Fr. 75'000 für alleinstehende Steuerpflichtige.
- **Beachten:** Gilt für alle Steuerpflichtigen ausser Ehegatten in rechtlich und tatsächlich ungetrennter Ehe (36.2)
- **Beachten:** Zusätzlich 25'000 je minderjähriges Kind mit Kinderabzug (Ziff. 36.3)
- **Beachten:** Internationales Verhältnis: nur bei unbeschränkter Steuerpflicht
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 75'000 (Steuerfreier Betrag auf dem Reinvermögen: übrige Steuerpflichtige CHF 75'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 25'000 (Zusätzlich pro minderjähriges Kind mit Kinderabzug CHF 25'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Bund:** Keine Vermögenssteuer beim Bund.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0122.md) `ar-wl-2025__c0122` – «36.1 für alleinstehende Steuerpflichtige»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0122.md) `ar-wl-2025__c0122` – «Fr. 75’000.– sen am Ende der Steuerperi»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «36.1 Für alleinstehende Personen Fr. 75’000»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «(Ziffer 33 330»
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «für alle übrigen steuerpflichtigen Personen Fr. 75 000.–»
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «Im internationalen Verhältnis werden die steuerfreien Beträge nur unbeschränkt steuerpflichtigen Personen gewährt»

<a id="36-2-vermoegen-sozialabzug"></a>
### Ziff. 36.2 – Sozialabzug gemeinsam steuerpflichtige Ehegatten (Code 332)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Personalien (Zivilstand 31.12.2025)
- **Rein:** Personalien → Zivilstand am 31.12.2025 (verheiratet, gemeinsam steuerpflichtig)
- **Rechnen:** Kanton: 150'000 je Ehepaar in ungetrennter Ehe (Verhältnisse am 31. Dezember 2025) / Bund: keine Vermögenssteuer
- **Regel:** Fr. 150'000 für Ehegatten in rechtlich und tatsächlich ungetrennter Ehe (gemeinsam steuerpflichtig); alle übrigen Steuerpflichtigen Fr. 75'000 (Ziff. 36.1).
- **Beachten:** Entweder 36.1 (75'000) oder 36.2 (150'000), nicht beide; nicht in ungetrennter Ehe → 36.1
- **Beachten:** Zusätzlich 25'000 je minderjähriges Kind (Ziff. 36.3)
- **Beachten:** Unterjährige Steuerpflicht: Verhältnisse am Ende der Steuerpflicht
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 150'000 (Steuerfreier Betrag auf dem Reinvermögen: Ehegatten in ungetrennter Ehe CHF 150'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 75'000 (Steuerfreier Betrag auf dem Reinvermögen: übrige Steuerpflichtige CHF 75'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 25'000 (Zusätzlich pro minderjähriges Kind mit Kinderabzug CHF 25'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Bund:** Keine Vermögenssteuer beim Bund.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0122.md) `ar-wl-2025__c0122` – «Fr. 150’000.– also per 31. Dezember 2025»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «36.2 Für gemeinsam steuerpflichtige Personen Fr. 150’000»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «332 –»
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «für Ehegatten, die in rechtlich und tatsächlich ungetrennter Ehe leben, Fr. 150 000.–»
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «Die steuerfreien Beträge werden nach den Verhältnissen am Ende der Steuerperiode oder der Steuerpflicht festgelegt»
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «für alle übrigen steuerpflichtigen Personen Fr. 75 000.–»

<a id="36-3-vermoegen-sozialabzug"></a>
### Ziff. 36.3 – Sozialabzug je minderjähriges Kind (Code 334)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Seite 1 der Steuererklärung (Kinder, Jahrgang)
- **Rein:** Seite 1 Steuererklärung → Kinder mit Geburtsjahr (minderjährig am 31.12.2025) · Kinderabzug Ziff. 23.1–23.3 → Voraussetzung
- **Rechnen:** Kanton: 25'000 × minderjährige Kinder unter elterlicher Sorge/Obhut mit Kinderabzug (23.1–23.3), Stand Ende Steuerperiode / Bund: keine Vermögenssteuer
- **Regel:** Fr. 25'000 für jedes minderjährige Kind unter der elterlichen Sorge oder Obhut der steuerpflichtigen Person, für das ein Kinderabzug nach Art. 38 StG (Ziff. 23.1-23.3) geltend gemacht werden kann (Jahrgang auf Seite 1 massgebend).
- **Beachten:** Volljährige Kinder in Ausbildung: nur Kinderabzug 23.3, kein Vermögensabzug
- **Beachten:** Kein 36.3 ohne Kinderabzug (z.B. Unterhaltsbeiträge Ziff. 12.2 abgezogen)
- **Beachten:** Vermögen minderjähriger Kinder wird bei den Eltern deklariert
- **Limiten:**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 25'000 (Zusätzlich pro minderjähriges Kind mit Kinderabzug CHF 25'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Bund:** Keine Vermögenssteuer beim Bund.
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0122.md) `ar-wl-2025__c0122` – «36.3 für jedes minderjährige Kind»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0005.md) `ar-wl-2025__c0005` – «36.3 Zusätzlich für jedes minderjährige Kind Fr. 25’000»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «334 –»
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «zusätzlich für jedes minderjährige Kind, das unter der elterlichen Sorge oder Obhut der steuerpflichtigen Person steht»
  - [WL AR 2025 S. 7](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0025.md) `ar-wl-2025__c0025` – «Aufgrund des Jahrgangs der Kinder können die für minderjährige Kinder unter»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0107.md) `ar-wl-2025__c0107` – «mögen der steuerpflichtigen Person und der unter elterlicher Sorge oder Obhut»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0082.md) `ar-wl-2025__c0082` – «entfallen die Kinderabzüge»
  - [StG AR Art. 51](../../chunks/ar/2025/ar-stg/ar-stg__art-51.md) `ar-stg__art-51` – «Die steuerfreien Beträge werden nach den Verhältnissen am Ende der Steuerperiode oder der Steuerpflicht festgelegt»

<a id="36-5-vermoegen-sozialabzug"></a>
### Ziff. 36.5 – Ermässigung auf ausserrhodischen Beteiligungen (Code 335)

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Beteiligungsbewertung
- **Rein:** Steuerwertmitteilung der Steuerverwaltung (innerer Wert der AR-Gesellschaft) → Steuerwert der Beteiligung (Form. 2)
- **Rechnen:** Ermässigung = 20 % × innerer Wert der Beteiligung an stark personenbezogener Gesellschaft mit Sitz in AR; ermässigter Wert ≥ ⅓ Substanzwert
- **Regel:** Ermässigung nach Art. 31 StV für ausserrhodische Beteiligungen.
- **Beachten:** Keine Ermässigung, wenn die Personenbezogenheit schon im inneren Wert berücksichtigt ist
- **Beachten:** Innerer Wert nach KS 28 (SSK), von der Steuerverwaltung der Gesellschaft mitgeteilt
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen. Höhe nicht in den geprüften Quellen.
- **Quellen:**
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0122.md) `ar-wl-2025__c0122` – «36.5 Ermässigung auf ausserrhodischen Beteiligungen (vgl. Art. 31 StV)»
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «335 –»
  - [StV AR Art. 31](../../chunks/ar/2025/ar-stv/ar-stv__art-31.md) `ar-stv__art-31` – «Bei stark personenbezogenen Gesellschaften mit Sitz in Appenzell Ausserrhoden wird der Wert gemäss Abs. 1 um 20 Prozent ermässigt»
  - [StV AR Art. 31](../../chunks/ar/2025/ar-stv/ar-stv__art-31.md) `ar-stv__art-31` – «Der Wert beträgt in jedem Fall mindestens einen Drittel des Substanzwertes.»
  - [StV AR Art. 31](../../chunks/ar/2025/ar-stv/ar-stv__art-31.md) `ar-stv__art-31` – «Keine Ermässigung wird gewährt, wenn die starke Personenbezogenheit des Unternehmens bereits bei der Bewertung des inneren Wertes berücksichtigt wurde.»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0134.md) `ar-wl-2025__c0134` – «rischen Steuerkonferenz vom 28. August 2008 festgelegt und von der Steuer»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen gesamt (Code 338)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 35 abzüglich 36.1-36.5)
- **Rein:** Übertrag Ziff. 35 (Reinvermögen) · Übertrag Sozialabzüge Ziff. 36.1–36.5
- **Rechnen:** Ziff. 35 − (36.1 bzw. 36.2) − 36.3 − 36.5 → 37 (Code 338)
- **Regel:** Reinvermögen abzüglich Sozialabzüge.
- **Beachten:** Bund: keine Vermögenssteuer – steuerbares Vermögen nur für Staats-/Gemeindesteuer
- **Beachten:** Steuerfreie Beträge nach den Verhältnissen am Ende der Steuerperiode
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 75'000 (Steuerfreier Betrag auf dem Reinvermögen: übrige Steuerpflichtige CHF 75'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 150'000 (Steuerfreier Betrag auf dem Reinvermögen: Ehegatten in ungetrennter Ehe CHF 150'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Vermögens-Sozialabzug pro Kind (CHF): Kanton **CHF 25'000 (Zusätzlich pro minderjähriges Kind mit Kinderabzug CHF 25'000.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Bemerkung:** Code aus der Formular-Miniatur der WL AR 2025 (Raster verzerrt, Zuordnung Zeile-Code nach Reihenfolge); am Originalformular prüfen.
- **Quellen:**
  - [WL AR 2025 S. 19](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0108.md) `ar-wl-2025__c0108` – «338»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0122.md) `ar-wl-2025__c0122` – «Vom Reinvermögen gemäss Ziffer 35 werden für die Berechnung des steuerbaren»

## Hilfsblatt Berufskosten (Form. 4)

<a id="form-4-ziff-1-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.1 – Fahrkosten öffentliche Verkehrsmittel (Code 400 Person 1 / 450 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg, Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → ÖV-Abo/Fahrausweise (tatsächliche Kosten); Lohnausweis Feld F
- **Rein:** ÖV-Abo/Fahrausweise → tatsächliche Kosten 2025 (Strecke, Datum von–bis) · Lohnausweis → Feld F (unentgeltliche Beförderung) prüfen · Angaben Arbeitsverhältnis → Arbeitgeber, Arbeitsort, Pensum, Erwerbsdauer (Form. 4 Allgemeine Angaben)
- **Rechnen:** Σ tatsächliche ÖV-Kosten → Code 400 (Person 1) / 450 (Person 2); mit 1.2–1.3 begrenzt (Code 405/455): Kanton max. 6'000 / Bund max. 3'300
- **Regel:** Tatsächliche ÖV-Kosten (Abo-Preis). Lohnausweis Feld F (unentgeltliche Beförderung/Sammeltransport/vom Arbeitgeber bezahltes GA) angekreuzt -> kein Fahrkostenabzug. Zusammen mit 1.2 und 1.3 begrenzt auf max. Fr. 6'000 (Pendlerabzug, nur Staats-/Gemeindesteuer). Fahrt über Mittag: Fahrkostenabzug höchstens Fr. 3'200 bzw. Fr. 1'600 (entspricht Verpflegung). Bei Geschäftsfahrzeug mit Privatanteil 0,9 %/Monat keine effektiven Fahrkosten.
- **Beachten:** Lohnausweis Feld F angekreuzt (Sammeltransport, GA vom Arbeitgeber) → kein Fahrkostenabzug
- **Beachten:** Geschäftsfahrzeug (Privatanteil 0,9 % pro Monat) → keine effektiven Fahrkosten
- **Beachten:** Fahrt über Mittag: Fahrkosten max. 3'200 / 1'600 (= Verpflegungsabzug); Maxima Kanton und Bund beachten
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 (Pendlerabzug).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **220 Tage (In der Regel höchstens 220 Arbeitstage für Fahrkosten.)** · Bund **n/a – Bund kennt keine Festlegung massgebender Arbeitstage; abziehbar sind die tatsächlichen notwendigen Kosten bis zum Maximalbetrag (Art. 26 Abs. 1 lit. a DBG).**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Mehrkosten auswärtige Verpflegung höchstens CHF 3'200 pro Jahr.)** · Bund **CHF 3'200 (Bei ständiger auswärtiger Verpflegung CHF 3'200 pro Jahr (voller Abzug))**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei Kantinenverpflegung oder Arbeitgeberbeitrag höchstens CHF 1'600 pro Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: CHF 1'600 pro Jahr)**
- **Bund:** DBSt: Fahrkosten-Maximum Fr. 3'300 (Art. 26 Abs. 1 lit. a DBG, vgl. data/werte/bund/2025.yaml, Status agent-geprüft; die ESTV-Wegleitung 2a 2025 nennt abweichend 3'200); die Fr. 6'000 gelten nur für Staats-/Gemeindesteuer. Lohnausweis-Feld F: nach ESTV-Wegleitung Lohnausweis 2026 (Folgejahr, für 2025 nicht bestätigt).
- **Bemerkung:** Codes 400/450 aus Form. 4. Lohnausweis-Wegleitung gilt 2026 (jahr_ok), Regel Feld F in AR-WL 2025 bestätigt.
- **Quellen:**
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0074.md) `ar-wl-2025__c0074` – «Bei Benützung eines öffentlichen Verkehrsmittels (Bahn, Tram, Trolley- oder»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «muss auf dem Lohnausweis Feld F»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «Ein Abzug für die Fahrt zur Arbeit ist deshalb nicht möglich»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0074.md) `ar-wl-2025__c0074` – «zur Arbeit bei den Staats- und Gemeindesteuern auf max. Fr. 6’000.–»
  - [WL Lohnausweis 2026 S. 9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0016.md) `bund-wl-lohnausweis-2026__c0016` – «In die sem Fall ist kein Kreuz im Feld F zu setzen»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0001.md) `ar-form-04-2025__c0001` – «1.1 Öffentliche Verkehrsmittel Datum von bis Weg von nach 400»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0002.md) `ar-form-04-2025__c0002` – «Zwischentotal Ziffern 1.1 – 1.3»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0002.md) `ar-form-04-2025__c0002` – «max. Fr. 6'000 405»
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0005.md) `ar-form-04-2025__c0005` – «1.1 Öffentliche Verkehrsmittel»
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0006.md) `ar-form-04-2025__c0006` – «max. Fr. 6'000 455»
  - [DBG Art. 26](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-26.md) `bund-dbg-2025__art-26` – «die notwendigen Kosten bis zu einem Maximalbetrag von 3300 Franken für die Fahrten zwischen Wohn- und Arbeitsstätte»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «Besitzer eines Geschäftsfahrzeuges versteuern einen Privatanteil von 0,9 %»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0001.md) `ar-form-04-2025__c0001` – «Arbeitgeber, Arbeitsort, Arbeitspensum, Erwerbsdauer»

<a id="form-4-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.2 – Fahrrad/Kleinmotorrad bis 50 cm3 (gelbes Kontrollschild) (Code 402 / 452)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Pauschale (keine Belege)
- **Rein:** Keine Belege – Pauschale (Code 402 Person 1 / 452 Person 2) · Form. 4 Kopf → Arbeitgeber, Arbeitsort, Pensum, Erwerbsdauer
- **Regel:** Pauschal bis Fr. 700 pro Jahr; zählt zur Gesamtlimite Fr. 6'000.
- **Beachten:** Kanton (Pendlerabzug): Velo, ÖV und Motorrad/Auto zusammen max. Fr. 6'000
- **Beachten:** Bund: Pauschale gilt für Fahrrad, Motorfahrrad, Motorrad mit gelbem Kontrollschild
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Benützung eines Fahrrades oder Kleinmotorrades: Pauschale bis CHF 700.)** · Bund **CHF 700 (Pauschale pro Jahr für Fahrrad, Motorfahrrad und Motorrad mit gelbem Kontrollschild; tatsächliche Kosten zusätzlich nicht abziehbar)**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 (Pendlerabzug).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Bund:** Bund: gleiche Pauschale Fr. 700 (BKV Anhang 2); Gesamtlimite Fr. 6'000 gilt nur kantonal (Bund 3'300).
- **Bemerkung:** Code 402 (Person 1); Person 2 Code 452 aus Form. 4 Rückseite.
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0001.md) `ar-form-04-2025__c0001` – «1.2 Fahrrad, Kleinmotorrad bis 50 cm3 (Kontrollschild mit gelbem Grund) 402»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0074.md) `ar-wl-2025__c0074` – «bis zu Fr. 700.– im Jahr»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «Motorräder mit gelbem Kontrollschild | im Jahr | 700.—»
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0005.md) `ar-form-04-2025__c0005` – «1.2 Fahrrad, Kleinmotorrad bis 50 cm3 (Kontrollschild mit gelbem Grund) 452»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0002.md) `ar-form-04-2025__c0002` – «max. Fr. 6'000 405»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0074.md) `ar-wl-2025__c0074` – «Unter diese Maximale fallen Velo, ÖV und Kosten für das Motorrad bzw. Auto.»

<a id="form-4-ziff-1-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 4 Ziff. 1.3 – Privates Motorfahrzeug in begründeten Fällen (Code 404/454); Zwischentotal 1.1-1.3 max. Fr. 6'000 (Code 405/455)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg, Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Fahrtenaufstellung (km, Tage), Begründung (Formular 4 Ankreuzfelder)
- **Rein:** Begründung ankreuzen: kein ÖV, Zeitersparnis, Verlangen AG, Krankheit (Arztzeugnis) · Lohnausweis → Feld F (Gratistransport/GA durch AG) prüfen
- **Regel:** Nur wenn kein ÖV vorhanden oder unzumutbar (Fussweg Haltestelle >15 Min., Krankheit/Gebrechlichkeit, Zeitaufwand ab 60 Min./Tag, Fahrzeugpflicht des Arbeitgebers): Auto Fr. 0.70/km, Motorrad Fr. 0.40/km (2025), in der Regel höchstens 220 Arbeitstage; Zwischentotal 1.1-1.3 max. Fr. 6'000. Ab 2026 Auto Fr. 0.75/km (News 2026; gilt auch für Staats-/Gemeindesteuer).
- **Beachten:** Nur wenn ÖV fehlt/unzumutbar: > 15 Min. Fussweg zur Haltestelle je Weg, Mehraufwand ÖV ≥ 60 Min./Tag, Krankheit, Fahrzeugpflicht AG
- **Beachten:** Geschäftsfahrzeug (Privatanteil 0,9 %/Monat) oder Lohnausweis Feld F angekreuzt → kein Fahrkostenabzug
- **Beachten:** > 220 Arbeitstage nachweisen; Park and Ride nur bis nächste Haltestelle; Heimfahrt über Mittag max. Fr. 3'200 / 1'600
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
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0006.md) `ar-form-04-2025__c0006` – «max. Fr. 6'000 455»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «Besitzer eines Geschäftsfahrzeuges versteuern einen Privatanteil von 0,9 %»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «Es können keine effektiven Fahrtkosten»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «getragenes Generalabonnement), muss auf dem Lohnausweis Feld F»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «Ein Abzug für die Fahrt zur Arbeit ist deshalb nicht möglich.»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «Arbeitstage ist nachzuweisen.»
  - [MB AR 01 S. 1](../../chunks/ar/dauernd/ar-mb-01/ar-mb-01__c0001.md) `ar-mb-01__c0001` – «Entfernung von der nächsten Haltestelle der öffentlichen Verkehrsmittel von mehr als 15 Minuten»
  - [MB AR 01 S. 1](../../chunks/ar/dauernd/ar-mb-01/ar-mb-01__c0001.md) `ar-mb-01__c0001` – «werden die Auslagen für das private Verkehrsmittel nur bis zur nächsten»
  - [MB AR 01 S. 1](../../chunks/ar/dauernd/ar-mb-01/ar-mb-01__c0001.md) `ar-mb-01__c0001` – «Verpflichtung zur Mitnahme des Fahrzeuges für Dienstfahrten an den Arbeitsort.»

<a id="form-4-ziff-2-1-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.1 – Mehrkosten auswärtige Verpflegung: Fr. 15 pro Arbeitstag, max. Fr. 3'200 (Code 408 / 458)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis (Felder F/G, Ziff. 15); Arbeitstage
- **Rein:** Lohnausweis → Feld G nicht angekreuzt (sonst Ziff. 2.2) · Arbeitstage mit auswärtiger Hauptmahlzeit
- **Regel:** Nur wenn die Heimkehr zum Mittagessen nicht möglich ist (grosse Entfernung): Fr. 15 pro Hauptmahlzeit, bei regelmässiger auswärtiger Verpflegung max. Fr. 3'200 pro Jahr. Lohnausweis Feld G angekreuzt -> nur Zeile 2.2 (halber Abzug). Nicht kombinierbar mit Schichtarbeit (2.3).
- **Beachten:** Nur wenn Hauptmahlzeit zu Hause wegen Entfernung oder kurzer Essenspause (AG) nicht zumutbar
- **Beachten:** Bei täglicher Heimkehr nur, soweit Mehrkosten ggü. Verpflegung zu Hause entstehen
- **Beachten:** Nicht zusammen mit Schicht-/Nachtarbeit (Ziff. 2.3)
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
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0007.md) `ar-form-04-2025__c0007` – «Pro Arbeitstag Fr. 15 / im Jahr Fr. 3'200 458»

<a id="form-4-ziff-2-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.2 – Verpflegung durch Arbeitgeber verbilligt (Kantine, Lunch-Checks, Beitrag): Fr. 7.50 pro Tag, max. Fr. 1'600 (Code 410 / 460)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (Kantinenverpflegung/Lunch-Checks/Bezahlung von Mahlzeiten)
- **Rein:** Lohnausweis → Feld G angekreuzt (Kantine, AG-Beitrag, Gutscheine) · Arbeitstage mit verbilligter Hauptmahlzeit
- **Regel:** Lohnausweis Feld G angekreuzt (Kantine, Lunch-Checks, Arbeitgeberbeitrag) -> in der Regel nur halber Abzug Fr. 7.50 pro Tag, max. Fr. 1'600 pro Jahr; bei so weit gehender Verbilligung, dass keine Mehrkosten gegenüber Zuhause entstehen: kein Abzug.
- **Beachten:** Halber Abzug schon, wenn ein Personalrestaurant benutzt werden kann (Art. 16 Abs. 2 StV)
- **Beachten:** Verbilligung so weit, dass keine Mehrkosten ggü. Zuhause entstehen → kein Abzug
- **Beachten:** Nicht kumulierbar mit Ziff. 2.1 oder 2.3
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
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0007.md) `ar-form-04-2025__c0007` – «Pro Arbeitstag Fr. 7.50 / im Jahr Fr. 1'600 460»

<a id="form-4-ziff-2-3-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 4 Ziff. 2.3 – Schicht-/Nachtarbeit (durchgehend mind. 8 Std.): Fr. 15 pro Schichttag, max. Fr. 3'200 (Code 412 / 462)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 (Bemerkungen: Anzahl Schichttage)
- **Rein:** Arbeitgeberbescheinigung (Lohnausweis, Bemerkungen) → Anzahl geleisteter Schichttage
- **Regel:** Nur bei durchgehender, mindestens achtstündiger Schicht-/Nachtarbeit; Anzahl Schichttage vom Arbeitgeber bescheinigt (Lohnausweis Ziff. 15); nicht zusätzlich zum Abzug 2.1/2.2.
- **Beachten:** Nur bei durchgehender, mind. achtstündiger Schicht-/Nachtarbeit
- **Beachten:** Gestaffelte/unregelmässige Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zu Hause möglich
- **Beachten:** Nicht zusätzlich zu Ziff. 2.1/2.2
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
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0007.md) `ar-form-04-2025__c0007` – «Pro ausgewiesenen Schichttag Fr. 15 / im Jahr Fr. 3'200 462»
  - [StV AR Art. 16](../../chunks/ar/2025/ar-stv/ar-stv__art-16.md) `ar-stv__art-16` – «Die gestaffelte oder unregelmässige Arbeitszeit wird der Schichtarbeit gleichgestellt»

<a id="form-4-ziff-3-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 4 Ziff. 3 – Übrige Berufskosten: Pauschale Fr. 700 + 10 % des Nettolohns, max. Fr. 2'400 (Code 416 / 466) oder tatsächliche Kosten mit Aufstellung (Code 418 / 468)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Ziff. 11 (Nettolohn) für die Pauschale; Kostenaufstellung/Belege bei effektiv
- **Rein:** Lohnausweis → Nettolohn (= Ziff. 1.1 Steuererklärung) als Basis der Pauschale · Lohnausweis → Pauschalspesen des Arbeitgebers prüfen
- **Regel:** Pauschale für jede unselbständig erwerbstätige Person; auch bei Taggeldern der ALV sinngemäss. Höhere effektive Kosten nur gegen Nachweis (Beiblatt). Bei nicht ereignisbezogenen Pauschalspesen des Arbeitgebers keine zusätzliche Pauschale. Nebenamtliche Behörden: MB 15. Arbeitszimmer in der Privatwohnung nur, wenn spezifisch eingerichteter Arbeitsplatz ausgeschieden und mindestens 40 % der Tätigkeit (bezogen auf Vollzeit) zu Hause erledigt werden müssen (Art. 18 Abs. 3 StV AR).
- **Beachten:** Nicht ereignisbezogene Pauschalspesen des AG → keine zusätzliche Pauschale; bei ALV-Taggeldern sinngemäss
- **Beachten:** Arbeitszimmer (Kanton) nur mit ausgeschiedenem Arbeitsplatz und ≥ 40 % Heimarbeit (Vollzeitbasis)
- **Beachten:** Bund: Pauschale bei Teilzeit oder unterjähriger Tätigkeit angemessen kürzen
- **Limiten:**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Übrige Berufskosten Pauschale: CHF 700 zuzüglich 10 % des Nettolohnes, max. CHF 2'400.)** · Bund **3 % (Übrige Berufskosten: 3 % des Nettolohns (Pauschale; Nachweis höherer Kosten möglich); bei Teilzeit/unterjährig angemessen kürzen)**
  - Übrige Berufskosten – fixer Pauschalbetrag (CHF), falls Formel «fix + %»: Kanton **CHF 700 (Fixer Sockelbetrag der Pauschale (zuzüglich 10 % des Nettolohnes).)** · Bund **n/a – Bund: 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; kein 'fix + %'-Modell.**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Maximum der Pauschale für übrige Berufskosten: CHF 2'400.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
  - Arbeitszimmer/Homeoffice – Regel: Kanton **Kosten eines Arbeitszimmers in der Privatwohnung sind abziehbar, wenn ein spezifisch eingerichteter Arbeitsplatz benötigt und tatsächlich ausgeschieden wird und mindestens 40 % der Tätigkeit (bezogen auf Vollzeit) zu Hause erledigt werden müssen; sonst nur Pauschale übrige Berufskosten bzw. Nachweis höherer Kosten.** · Bund **Privates Arbeitszimmer: nur als Teil der Pauschale 'übrige Berufskosten' bzw. bei Nachweis höherer Kosten abziehbar; Kosten (Miete, Heizung, Beleuchtung) nur, wenn das Zimmer für die Berufsarbeit benützt werden muss. Gelegentliche Arbeit in der Privatwohnung gibt keinen Abzug**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **n/a – Formel «700 + 10 %» ohne separates Minimum; der fixe Sockelbetrag von CHF 700 ist das faktische Minimum (siehe berufskosten.uebrige.fix).** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
- **Bund:** DBSt: eigene Pauschale 3 % (min./max.) statt Fr. 700 + 10 % (data/werte/bund/2025.yaml).
- **Bemerkung:** Codes 416/418 Person 1, 466/468 Person 2. Pauschale ist kantonal (Art. 18 StV AR, kein Verweis auf DBG-Ansatz); Bund hat 3 %.
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0003.md) `ar-form-04-2025__c0003` – «Pauschalabzug: Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2'400 416»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0003.md) `ar-form-04-2025__c0003` – «Anstelle des Pauschalabzuges: tatsächliche Berufskosten»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0078.md) `ar-wl-2025__c0078` – «Bei Auszahlung nicht ereignis»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0078.md) `ar-wl-2025__c0078` – «3.1 Für diese Aufwendungen kann die steuerpflichtige Person von ihren Einkünf»
  - [StV AR Art. 18](../../chunks/ar/2025/ar-stv/ar-stv__art-18.md) `ar-stv__art-18` – «Fr. 700.– zuzüglich 10 Prozent der Nettoeinkünfte, höchstens aber Fr. 2400.–»
  - [StV AR Art. 18](../../chunks/ar/2025/ar-stv/ar-stv__art-18.md) `ar-stv__art-18` – «mindestens 40 Prozent der Tätigkeit, gemessen an einer Vollzeitbeschäftigung, zu Hause erledigt werden müssen»
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0007.md) `ar-form-04-2025__c0007` – «Pauschalabzug: Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2'400 466»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0071.md) `ar-wl-2025__c0071` – «Ausgangsbasis ist der in Ziffer 1.1 der Steuererklärung deklarierte Nettolohn»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «3 % des Nettolohns, mindestens im Jahr | 2000.—»
  - [BKV Anhang](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) `bund-bkv-2025__anhang-1` – «höchstens im Jahr | 4000.—»
  - [BKV Art. 7](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-7.md) `bund-bkv-2025__art-7` – «Der Pauschalabzug ist angemessen zu kürzen, wenn die unselbständige Erwerbstätigkeit bloss während eines Teils des Jahres oder als Teilzeitarbeit ausgeübt wird.»

<a id="form-4-ziff-4-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 4 Ziff. 4 – Wochenaufenthalt: Zimmer (Code 426 / 476), Verpflegung Fr. 30/Tag, max. Fr. 6'400 bzw. Fr. 22.50/Tag, max. Fr. 4'800 (Code 428 / 478)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag/Quittungen des Zimmers; Lohnausweis (verbilligte Mahlzeiten)
- **Rein:** Heimfahrten an den Wohnsitz → Ziff. 1 Fahrkosten
- **Rechnen:** Code 426 = Monate × min(Zimmermiete/Monat; 800) (Kanton) + Code 428 = min(Tage × 30; 6'400), verbilligt min(Tage × 22.50; 4'800); Verpflegung Kanton = Bund
- **Regel:** Nur wenn tägliche Rückkehr nicht zumutbar; Zimmer (keine Wohnung) tatsächliche Kosten max. Fr. 800 pro Monat; Verpflegung Fr. 30 pro Tag/max. Fr. 6'400, bei verbilligtem Mittagessen Fr. 22.50/max. Fr. 4'800; Heimkehr-Fahrkosten unter Ziff. 1 (unter Fahrkostenlimite).
- **Beachten:** Nur wenn tägliche Rückkehr (zeitlich/finanziell) unzumutbar und regelmässige Heimkehr übers Wochenende
- **Beachten:** Nur Zimmer (keine Wohnung), ortsübliche Kosten; Heimfahrten unterliegen der Fahrkostenlimite
- **Beachten:** Bund: Nachweis höherer Verpflegungskosten ausgeschlossen; Zimmer nur ortsübliche Auslagen
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
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0008.md) `ar-form-04-2025__c0008` – «Unterkunft: Ortsübliche Kosten für ein Zimmer Monate à Fr. 476»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0076.md) `ar-wl-2025__c0076` – «In diesem Fall ist auf dem Lohnausweis Feld G angekreuzt.»
  - [BKV Art. 9](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-9.md) `bund-bkv-2025__art-9` – «Der Nachweis höherer Kosten ist ausgeschlossen.»
  - [BKV Art. 9](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-9.md) `bund-bkv-2025__art-9` – «Als notwendige Mehrkosten der Unterkunft sind die ortsüblichen Auslagen für ein Zimmer abziehbar.»

<a id="form-4-ziff-5-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 4 Ziff. 5 – Unselbständiger Nebenerwerb: Pauschale 20 % der Nettoeinkünfte, mind. Fr. 800, max. Fr. 2'400 (Code 432 / 482) oder tatsächliche Kosten (Code 434 / 484)

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 des Nebenarbeitgebers
- **Rein:** Lohnausweis Nebenarbeitgeber → Nettolohn Nebenerwerb (Ziff. 1.2 Steuererklärung)
- **Regel:** Nur bei echtem Nebenerwerb neben vollem Hauptberuf für einen anderen Arbeitgeber; bis Nettolohn Fr. 800: Auslagen bis zur Höhe des Nettolohns; darüber 20 %, mind. Fr. 800, max. Fr. 2'400. Kein Abzug für Pensionierte/Hausfrauen ohne Haupterwerb; in der Regel nicht für VR-Honorare.
- **Beachten:** Nur Nebenerwerb neben vollem Hauptberuf bei anderem AG; Pensionierte/Hausfrauen ohne Haupterwerb → nur Ziff. 1–3
- **Beachten:** VR-Honorare i.d.R. kein Abzug (Unkosten meist zusätzlich vergütet)
- **Beachten:** Nebenamtliche Behördenmitglieder: Kanton zusätzlich bis Fr. 2'600 (gilt nicht für DBSt)
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
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0008.md) `ar-form-04-2025__c0008` – «Pauschalabzug: 20% der Nettoeinkünfte, mindestens Fr. 800,»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0035.md) `ar-wl-2025__c0035` – «Als Nebenerwerb gilt eine Tätigkeit, die gleichzeitig neben einem Hauptberuf»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0080.md) `ar-wl-2025__c0080` – «Ihnen stehen die Abzüge gemäss Ziffern 1 bis 3 zu.»
  - [WL AR 2025 S. 8](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0037.md) `ar-wl-2025__c0037` – «(gilt nicht für die direkte Bundessteuer)»
  - [MB AR 15 S. 1](../../chunks/ar/dauernd/ar-mb-15/ar-mb-15__c0003.md) `ar-mb-15__c0003` – «werden für die Berufskosten von nebenamtlichen Behördenmitgliedern zusätzlich pauschal bis Fr. 2‘600.- abgezogen (Behördenabzug)»

<a id="form-4-ziff-6-berechnung-total"></a>
### Ziff. Form. 4 Ziff. 6 – Total der Berufskosten (Code 438 Person 1 -> Ziff. 10.1; Code 488 Person 2 -> Ziff. 10.2)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 4 Rechenzeile
- **Rein:** Übertrag Form. 4 Ziff. 1–5 je Person (Codes 405, 408/410/412, 416/418, 426, 428, 432/434)
- **Rechnen:** Code 438 = 405 + 408 bzw. 410 bzw. 412 + 416 bzw. 418 + 426 + 428 + 432 bzw. 434 → Ziff. 10.1; Person 2: Code 488 → Ziff. 10.2
- **Regel:** Summe Ziff. 1-5; Übertrag in Seite 3 Ziffer 10.1 (Person 1) bzw. 10.2 (Person 2).
- **Beachten:** Vorderseite Person 1 bzw. Alleinstehende, Rückseite Person 2; Abzüge stehen jedem Ehegatten individuell zu
- **Beachten:** Kein Abzug für Kosten, die der Arbeitgeber übernommen hat
- **Beachten:** Bund abweichend: Fahrkosten max. 3'300; übrige Berufskosten 3 %, min. 2'000, max. 4'000
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 6'000 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, kantonal höchstens CHF 6'000 (Pendlerabzug).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **10 % (Übrige Berufskosten Pauschale: CHF 700 zuzüglich 10 % des Nettolohnes, max. CHF 2'400.)** · Bund **3 % (Übrige Berufskosten: 3 % des Nettolohns (Pauschale; Nachweis höherer Kosten möglich); bei Teilzeit/unterjährig angemessen kürzen)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **n/a – Formel «700 + 10 %» ohne separates Minimum; der fixe Sockelbetrag von CHF 700 ist das faktische Minimum (siehe berufskosten.uebrige.fix).** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Maximum der Pauschale für übrige Berufskosten: CHF 2'400.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
- **Bemerkung:** Code 488 aus Form. 4 Rückseite (Person 2).
- **Quellen:**
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0004.md) `ar-form-04-2025__c0004` – «Total der Berufskosten 438 13211 zu übertragen in die Steuererklärung Seite 3 Ziffer 10.1»
  - [Formular 4 AR 2025 S. 2](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0008.md) `ar-form-04-2025__c0008` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 10.2»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0002.md) `ar-form-04-2025__c0002` – «max. Fr. 6'000 405»
  - [Formular 4 AR 2025 S. 1](../../chunks/ar/2025/ar-form-04-2025/ar-form-04-2025__c0003.md) `ar-form-04-2025__c0003` – «Pauschalabzug: Fr. 700 zuzüglich 10% des Nettolohnes, höchstens Fr. 2'400 416»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0073.md) `ar-wl-2025__c0073` – «Kein Abzug ist zulässig für Kosten, die der Arbeitgeber»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0073.md) `ar-wl-2025__c0073` – «Person 2 auf der Rückseite.»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0072.md) `ar-wl-2025__c0072` – «jedem Ehegatten/Partner individuell zu»
  - [WL AR 2025 S. 13](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0075.md) `ar-wl-2025__c0075` – «Es sind die max. Fahrkosten»

## Hilfsblatt Wertschriftenverzeichnis (Form. 2)

<a id="form-2-spalten-a-b-vermoegen-wertschriften-guthaben"></a>
### Ziff. Form. 2 Spalten A/B – Verzeichnis der Vermögenswerte: Steuerwert per 31.12.2025 und Bruttoertrag 2025, Spalte A (mit Verrechnungssteuerabzug) / Spalte B (ohne)

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Steuerauszug (eCH-0196)/Bankbescheinigung: Valoren-Nr., Stückzahl, Steuerwert per 31.12.2025, Bruttoertrag 2025
- **Rein:** Steuerauszug Bank → je Titel/Konto Steuerwert am 31. Dezember 2025 + Bruttoertrag 2025 (Auszug vollständig beilegen) · Kursliste ESTV → Steuerwert kotierter Titel; nichtkotierte: innerer Wert (Kreisschreiben Nr. 28) · Kauf-/Verkaufsbelege, Bankbelege → Datum Zugang/Abgang (Spalte 5/6) · Formular DA-1 → Hertrag ausländische Titel mit anrechenbarer Quellensteuer
- **Rechnen:** Ertrag je Titel → Spalte A (VSt-pflichtig) oder B; Ziff. 4.1 = Total A+B − G − BP − BG (BP → Ziff. 4.2, BG → 4.3); Σ Steuerwert − G → Ziff. 30.1
- **Regel:** Spalte A: Titel/Guthaben mit 35 % Verrechnungssteuerabzug (u.a. Guthaben mit Bruttozins >Fr. 200, inländische Aktien/Obligationen/Fonds); Spalte B: ohne Verrechnungssteuer (u.a. Kundenguthaben bis Fr. 200 Bruttozins pro Jahr). Code-Abkürzungen: G Geschäftsvermögen, N Nutzniessung, E neuer Titel aus Erbschaft, S aus Schenkung, BP/BG Beteiligung mind. 10 % (Privat-/Geschäftsvermögen). Bisher nicht deklarierte Titel (Selbstanzeige) ausdrücklich als solche bezeichnen.
- **Beachten:** Spalte B: Kundenguthaben mit Bruttozins ≤ Fr. 200, ausländische Titel; selbst errechnete Zinsen nicht eintragen
- **Beachten:** Krypto mitdeklarieren; Codes: G Geschäftsvermögen, N Nutzniessung, E/S neu aus Erbschaft/Schenkung, BP/BG Beteiligung ≥ 10 %
- **Beachten:** Darlehen ab Fr. 50'000: Vertrag beilegen; Selbstanzeige-Titel ausdrücklich als solche bezeichnen
- **Bemerkung:** Spaltenüberschriften Form. 2 (Seite 2) nicht mit Zeilencodes versehen.
- **Quellen:**
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0005.md) `ar-form-02-2025__c0005` – «Steuerwert am 31. Dezember 2025 Bruttoertrag 2025»
  - [WL AR 2025 S. 26](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0147.md) `ar-wl-2025__c0147` – «In Spalte A sind die Vermögenswerte aufzuführen, deren Erträge der»
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «Total A und B Bruttoertrag»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0128.md) `ar-wl-2025__c0128` – «rungen wie Bitcoin, Ether etc.»
  - [WL AR 2025 S. 27](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0151.md) `ar-wl-2025__c0151` – «Kundenguthaben, deren Bruttozins Fr. 200.– nicht übersteigt;»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0129.md) `ar-wl-2025__c0129` – «sind die Auszüge für Steuerzwecke dem Formular 2 vollständig beizulegen»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0134.md) `ar-wl-2025__c0134` – «Kursliste der Eidg. Steuerverwaltung entnommen werden»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0134.md) `ar-wl-2025__c0134` – «Kreisschreiben Nr. 28»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0130.md) `ar-wl-2025__c0130` – «sind die betreffenden Kaufs- bzw. Verkaufsbelege oder allenfalls»
  - [WL AR 2025 S. 25](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0144.md) `ar-wl-2025__c0144` – «geltend gemacht werden kann, sind im Formular DA-1 aufzuführen»
  - [WL AR 2025 S. 25](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0145.md) `ar-wl-2025__c0145` – «Wertschriftenverzeichnis zu übertragen (Zeile «Hertrag von DA-1»)»
  - [WL AR 2025 S. 23–24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0136.md) `ar-wl-2025__c0136` – «Selbst errechnete Zinsen dürfen nicht eingetragen werden.»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0130.md) `ar-wl-2025__c0130` – «Bei Darlehen ab Fr. 50’000.– ist eine Kopie des Darlehensvertrags beizulegen.»
  - [WL AR 2025 S. 27](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0151.md) `ar-wl-2025__c0151` – «ausländische Aktien, Obligationen, Anteile an GmbH, Genossenschaften»

<a id="form-2-total-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 2 Total – Verrechnungssteueranspruch 35 % vom Bruttoertrag (Total A) (Code 999)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular 2 Total A (Rückerstattungsantrag Verrechnungssteuer)
- **Rein:** Übertrag Form. 2 → Total Bruttoertrag Spalte A (Erträge mit 35 % VSt-Abzug)
- **Rechnen:** Code 999 = 35 % × Total Bruttoertrag Spalte A
- **Regel:** 35 % des Bruttoertrags Total A (nur Erträge mit abgezogener Verrechnungssteuer); Kollektiv-/Kommanditgesellschaften: Formular 25 direkt bei ESTV.
- **Beachten:** Rückerstattung nur bei Wohnsitz AR am 31. Dezember 2025; sonst Antrag beim Steueramt des früheren Wohnortes
- **Beachten:** Kollektiv-/Kommanditgesellschaft: Formular 25 durch die Gesellschaft; STWE-Erneuerungsfonds: Formular 25 durch die STWE-Verwaltung (direkt ESTV)
- **Beachten:** Anspruch erlischt, wenn nicht innert drei Jahren nach Ablauf des Fälligkeitsjahres beantragt
- **Bemerkung:** Code 999 aus Form. 2.
- **Quellen:**
  - [Formular 2 AR 2025 S. 2](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0007.md) `ar-form-02-2025__c0007` – «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A) Fr./Rp. 999»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0004.md) `ar-form-02-2025__c0004` – «Rückerstattung der Verrechnungssteuer mit Formular 25 direkt bei der Eidg. Steuerverwaltung»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0131.md) `ar-wl-2025__c0131` – «Der Verrechnungssteuersatz beträgt 35 Prozent.»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0132.md) `ar-wl-2025__c0132` – «Steueramt des früheren»
  - [WL AR 2025 S. 23–24](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0137.md) `ar-wl-2025__c0137` – «durch die Stockwerkeigentums-Verwaltung mit dem Antragsfor»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0133.md) `ar-wl-2025__c0133` – «Der Anspruch auf Rückerstattung der Verrechnungssteuer erlischt»

<a id="form-2-s-1-960-961-info-schenkungen-erbschaften"></a>
### Ziff. Form. 2 S. 1 (960/961) – Fragen Erbschaften: erhaltene Erbschaft/Vermächtnis (Code 960); Beteiligung an unverteilter Erbschaft mit Erbanteil (Code 961)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Erbteilungsvertrag/Erbteilungsakt (Kopie), Inventar und Erbenverzeichnis
- **Rein:** Erbteilungsvertrag/Erbteilakt (Kopie) → Erblasser, Todestag, Betrag, Teilungsdatum (Code 960) · Inventar + Erbenverzeichnis (Kopie) → Erbanteil ohne Liegenschaften (Code 961) · Zins-/Dividendenabrechnungen der Erbschaft → anteilige Bruttoerträge
- **Rechnen:** Unverteilt: Anteil Erträge ab Todestag → Ziff. 6.2, Anteil Vermögen → Ziff. 30.5, Liegenschaften → Form. 7; verteilt: Titel mit «E» im Wertschriftenverzeichnis (Erträge seit Erbteilung)
- **Regel:** Fragen sind immer zu beantworten; bei Erbschaft im Jahr 2025 Erblasser, Todestag, Betrag, Teilungsdatum (Erbteilakt beilegen); unverteilte Erbschaft: Erbanteil ohne Liegenschaften (diese in Form. 7), Inventar/Erbenverzeichnis beilegen; Ertrag -> Ziff. 6.2, Vermögen -> Ziff. 30.5.
- **Beachten:** Fragen auf Seite 1 immer beantworten
- **Beachten:** Erbschaft ab Fr. 100'000: Vermögenszuwachs wird von Amtes wegen zeitlich gewichtet
- **Beachten:** VSt auf Erträgen nach dem Todestag beantragen die Erben anteilig im eigenen Verzeichnis (mit Belegen)
- **Bemerkung:** Codes 960/961 aus Form. 2. Schlüssel info.schenkungen_erbschaften kommt in dieser Datei zweimal vor (zwei Fragen-Blöcke).
- **Quellen:**
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «Haben Sie im Jahr 2025 eine Erbschaft oder ein Vermächtnis erhalten?»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «Sind Sie an einer unverteilten Erbschaft beteiligt?»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0002.md) `ar-form-02-2025__c0002` – «(Kopie des Erbteilaktes beilegen)»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0132.md) `ar-wl-2025__c0132` – «in der Steuererklärung Ziffer 6.2 (Erträge) bzw. in Ziffer 30.5 (Vermö»
  - [WL AR 2025 S. 22](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0127.md) `ar-wl-2025__c0127` – «Die Fragen auf Seite 1 des Wertschriften- und Guthabenverzeichnisses sind zu»
  - [WL AR 2025 S. 5](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0016.md) `ar-wl-2025__c0016` – «Bei einer Erbschaft ab Fr. 100’000.– wird»
  - [WL AR 2025 S. 5](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0016.md) `ar-wl-2025__c0016` – «der Vermögenszuwachs von Amtes wegen zeitlich gewichtet»
  - [WL AR 2025 S. 25](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0143.md) `ar-wl-2025__c0143` – «Spalte 1 mit «E» bzw. «S» zu»
  - [WL AR 2025 S. 23](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0132.md) `ar-wl-2025__c0132` – «Dazu sind die anteiligen Bruttoerträge nach Massgabe seines Anteils an der»

<a id="form-2-s-1-962-963-info-schenkungen-erbschaften"></a>
### Ziff. Form. 2 S. 1 (962/963) – Fragen Schenkungen: Vermögen aus Schenkung/Erbvorbezug erworben (Code 962); Vermögen verschenkt (Code 963)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Schenkungsvertrag/Aufstellung
- **Rein:** Schenkungsvertrag/Aufstellung → Schenker/in bzw. Beschenkte/r, Datum, Betrag, Verwandtschaftsgrad
- **Rechnen:** Erhalten (inkl. Erbvorbezug) → Code 962; verschenkt → Code 963; Erträge ab Erhalt bis Ende Steuerperiode, Vermögen per 31. Dezember
- **Regel:** Betrag, Datum, Schenker/Beschenkter und Verwandtschaftsgrad angeben; Aufstellung beilegen. Erträge aus geschenkten Titeln: Code S im Verzeichnis.
- **Beachten:** Geschenkte Titel im Wertschriftenverzeichnis (Spalte 1) mit «S» bezeichnen; nur Erträge seit Erwerb
- **Beachten:** Zusammensetzung (Aufstellung) beilegen
- **Bemerkung:** Codes 962/963 aus Form. 2.
- **Quellen:**
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0003.md) `ar-form-02-2025__c0003` – «Haben Sie im Jahr 2025 Vermögen aus Schenkung oder Erbvorbezug erworben?»
  - [Formular 2 AR 2025 S. 1](../../chunks/ar/2025/ar-form-02-2025/ar-form-02-2025__c0003.md) `ar-form-02-2025__c0003` – «(Zusammensetzung: Aufstellung beilegen)»
  - [WL AR 2025 S. 5](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0016.md) `ar-wl-2025__c0016` – «deklarieren Sie die Erträge, die Sie ab Erhalt bis Ende der»
  - [WL AR 2025 S. 5](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0016.md) `ar-wl-2025__c0016` – «sich aus dem Stand per 31. Dezember.»
  - [WL AR 2025 S. 25](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0143.md) `ar-wl-2025__c0143` – «Spalte 1 mit «E» bzw. «S» zu»

## Hilfsblatt Schulden/Zuwendungen (Form. 5)

<a id="form-5-teil-a-schulden-privat"></a>
### Ziff. Form. 5 Teil A – Private Schulden (Schuldbestand 31.12.2025) und Schuldzinsen 2025

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Hypothekar-/Kreditbestätigung der Bank: Gläubiger, Schuld per 31.12.2025, Zinsen 2025
- **Rein:** Hypothekar-/Kreditbestätigung → Gläubiger, Schuld am 31. Dezember 2025 · Zinsausweis/Bankbestätigung → bezahlte Schuldzinsen 2025 · Private Darlehensverträge → Gläubiger, Saldo, Zins
- **Rechnen:** Σ Schulden → Ziff. 34.1; Σ Schuldzinsen → Ziff. 11, abziehbar max. Ertrag Ziff. 4 + Ziff. 5 + Fr. 50'000 (Bund: Vermögenserträge + 50'000)
- **Regel:** Je Gläubiger Schuld am 31.12.2025 und bezahlte Zinsen 2025; Total Schulden -> Ziff. 34.1, Total Zinsen -> Ziff. 11. Belege nur auf Verlangen einzureichen.
- **Beachten:** Nicht abziehbar: Amortisationen, Baurechtszinsen selbstgenutztes Eigenheim, Leasingraten; Baukreditzinsen ja
- **Beachten:** Solidar-/Bürgschaftsschuld nur soweit selbst zu tragen
- **Beachten:** Ertrag Ziff. 4 ohne Lotterie-/Lotto-/Totogewinne; Belege nur auf Verlangen
- **Bemerkung:** Beide Totale ohne eigene Codes.
- **Quellen:**
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0001.md) `ar-form-05-2025__c0001` – «Total private Schulden und private Schuldzinsen 213213211 13213211»
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0001.md) `ar-form-05-2025__c0001` – «Seite 3 Ziffer 11»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0081.md) `ar-wl-2025__c0081` – «der Einkünfte aus Liegenschaften gemäss Ziffer 5 zuzüglich Fr. 50’000.–»
  - [WL AR 2025 S. 14](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0081.md) `ar-wl-2025__c0081` – «Leasingraten persönlicher Gebrauchsgegenstände und privater Fahrzeuge.»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0121.md) `ar-wl-2025__c0121` – «Schuld (Solidar- oder Bürgschaftsschuld), so wird der Abzug nur insoweit ge»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken»

<a id="form-5-teil-b-schulden-privat"></a>
### Ziff. Form. 5 Teil B – Geschäftsschulden (Schuld am 31.12. bzw. Bilanzstichtag)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Bilanz/Schuldenbestätigung
- **Rein:** Bilanz/Jahresrechnung → Geschäftsschulden per 31. Dezember 2025 bzw. Bilanzstichtag
- **Rechnen:** Σ Geschäftsschulden je Gläubiger → Ziff. 34.2
- **Regel:** Nur Schuldbestand; geschäftliche Zinsen sind in der Jahresrechnung enthalten und hier nicht aufzuführen. Total -> Ziff. 34.2.
- **Beachten:** Geschäftliche Schuldzinsen nicht hier (in der Jahresrechnung enthalten)
- **Beachten:** Solidar-/Bürgschaftsschuld nur soweit selbst zu tragen
- **Quellen:**
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0002.md) `ar-form-05-2025__c0002` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 34.2»
  - [Formular 5 AR 2025 S. 1](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0002.md) `ar-form-05-2025__c0002` – «Total Geschäftsschulden 213213211»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0120.md) `ar-wl-2025__c0120` – «Die Betriebsschulden sind im Schuldenverzeichnis (Formular 5)»
  - [WL AR 2025 S. 21](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0121.md) `ar-wl-2025__c0121` – «Schuld (Solidar- oder Bürgschaftsschuld), so wird der Abzug nur insoweit ge»

<a id="form-5-s-2-teil-a-abzug-spenden"></a>
### Ziff. Form. 5 S. 2 Teil A – Freiwillige Zuwendungen: Institution, Datum, Betrag; Total (Code 550) -> Ziff. 21.3

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigung der steuerbefreiten Institution (auf Verlangen)
- **Rein:** Spendenbestätigung der steuerbefreiten Institution → Name, Datum, Betrag 2025 (auf Verlangen)
- **Rechnen:** Σ Zuwendungen = Code 550 → Ziff. 21.3 Vorkolonne; Abzug nur wenn Σ ≥ 100: min(Σ; 20 % × Nettoeinkommen Ziff. 20); Kanton = Bund
- **Regel:** Je Zuwendung Datum und Betrag; Total -> Ziff. 21.3 (Vorkolonne).
- **Beachten:** Nur an steuerbefreite juristische Personen mit Sitz in der Schweiz, völlig uneigennützig
- **Beachten:** Mitgliederbeiträge nicht abziehbar; religiöse Institutionen nur für ausschliesslich gemeinnützige Zwecke
- **Beachten:** Parteispenden separat in Teil B (Ziff. 16.3)
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Zuwendungen nur abziehbar, wenn sie in der Steuerperiode CHF 100 erreichen.)** · Bund **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen (CH) bzw. Gemeinwesen: mindestens CHF 100 im Steuerjahr)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen max. 20 % der um die Aufwendungen gemäss Art. 28-35 verminderten steuerbaren Einkünfte.)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Bemerkung:** Code 550.
- **Quellen:**
  - [Formular 5 AR 2025 S. 2](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0003.md) `ar-form-05-2025__c0003` – «Total der Zuwendungen 550 3213211»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0103.md) `ar-wl-2025__c0103` – «Abzugsfähig ist der gesamte Betrag, sofern das Total der Zuwendungen mindes»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0103.md) `ar-wl-2025__c0103` – «maximal jedoch 20 Prozent des Nettoeinkommens gemäss Ziffer 20»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0102.md) `ar-wl-2025__c0102` – «an juristische Personen mit Sitz in der Schweiz»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0102.md) `ar-wl-2025__c0102` – «(Mitgliederbeiträge sind nicht abzugsfähig)»
  - [Formular 5 AR 2025 S. 2](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0004.md) `ar-form-05-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 16.3»

<a id="form-5-s-2-teil-b-abzug-parteispenden"></a>
### Ziff. Form. 5 S. 2 Teil B – Parteispenden: Partei, Datum, Betrag; Total (Code 555) -> Ziff. 16.3

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Bestätigung der Partei (auf Verlangen)
- **Rein:** Bestätigung der Partei → Partei, Datum, Betrag (Mitglieder-, Wahlkampf-, Mandatsbeiträge)
- **Rechnen:** Σ Parteispenden = Code 555 → Ziff. 16.3; Abzug Kanton min(Σ; 10'000 je Steuererklärung) / Bund min(Σ; 10'600)
- **Regel:** Max. Fr. 10'000 pro Steuererklärung; Total -> Ziff. 16.3.
- **Beachten:** Kanton = Bund: nur Parteien im Parteienregister, in einem Kantonsparlament vertreten oder ≥ 3 % Stimmen bei den letzten kantonalen Parlamentswahlen
- **Beachten:** Nicht: persönliche Wahlkampfkosten, Komitees, Volksinitiativen, Beiträge direkt an Kandidierende
- **Beachten:** Kanton: Fr. 10'000 gilt pro Steuererklärung, auch für Ehepaare (keine Verdoppelung)
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'000 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'000 (pro Steuererklärung).)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 10'000 (Gesamtbetrag CHF 10'000 gilt pro Steuererklärung, d.h. auch für gemeinsam Besteuerte (keine Verdoppelung).)** · Bund **n/a – Bund kennt nur einen Gesamtbetrag von CHF 10'600 (Art. 33 Abs. 1 lit. i DBG); keine Verdoppelung für Ehepaare in der Quelle.**
- **Bemerkung:** Code 555.
- **Quellen:**
  - [Formular 5 AR 2025 S. 2](../../chunks/ar/2025/ar-form-05-2025/ar-form-05-2025__c0004.md) `ar-form-05-2025__c0004` – «Total der Parteispenden 555 3213211»
  - [WL AR 2025 S. 16–17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0092.md) `ar-wl-2025__c0092` – «Gesamtbetrag von Fr. 10’000.– (pro Steuererklärung)»
  - [WL AR 2025 S. 16–17](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0092.md) `ar-wl-2025__c0092` – «in einem Kanton bei den letzten Wahlen des kantonalen Parlaments mindes»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t3.md) `bund-dbg-2025__art-33-t3` – «in einem Kanton bei den letzten Wahlen des kantonalen Parlaments mindestens 3 Prozent der Stimmen erreicht haben»

## Hilfsblatt Versicherungsprämien/Krankheitskosten (Form. 6)

<a id="form-6-teil-a-abzug-versicherungspraemien"></a>
### Ziff. Form. 6 Teil A – Bezahlte Versicherungsprämien und Sparzinsen: a. Krankenversicherung (brutto), b. Unfallversicherung (ohne NBUV), c. Lebens-/Rentenversicherungen, d. Sparzinsen, e. abzüglich Prämienverbilligungen (Code 600 A)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Prämienrechnung/Jahresbescheinigung Krankenversicherung (brutto), Prämienverbilligungs-Verfügung, Zinsausweis (Sparzinsen gemäss Wertschriftenverzeichnis)
- **Rein:** Prämienbescheinigung Krankenkasse → Bruttoprämien (a) · Policen/Prämienrechnungen → Unfall- (ohne NBUV), Lebens-, Rentenversicherung (b, c) · Form. 2 → Sparzinsen (d) · Verfügung Prämienverbilligung → Betrag (e, abziehen)
- **Rechnen:** Code 600 A = a + b + c + d − e (Prämienverbilligung)
- **Regel:** Familien tragen Prämien/Sparzinsen der ganzen Familie hier ein; Prämienverbilligung (IPV) abziehen; NBUV, Mobiliar-, Haftpflicht-, Motorfahrzeugversicherungen nicht aufführen.
- **Beachten:** Familien: Prämien und Sparzinsen der ganzen Familie (inkl. unterhaltene Kinder) eintragen
- **Beachten:** Nicht: NBUV, Mobiliar-, Motorfahrzeug-, Haftpflicht- und andere Sachversicherungen
- **Beachten:** Nur tatsächlich bezahlte Prämien
- **Bemerkung:** Code 600 A.
- **Quellen:**
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0001.md) `ar-form-06-2025__c0001` – «Private Krankenversicherung (brutto)»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0001.md) `ar-form-06-2025__c0001` – «abzüglich Prämienverbilligungen»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0001.md) `ar-form-06-2025__c0001` – «Total bezahlte Versicherungsprämien und Sparzinsen 600 A»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0085.md) `ar-wl-2025__c0085` – «Vom Abzug ausgeschlossen sind die Prämien für Mobiliar-, Motorfahrzeug- und»
  - [WL AR 2025 S. 15](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0085.md) `ar-wl-2025__c0085` – «Dabei sind die individuellen Prämienverbilligungen»

<a id="form-6-teil-b-c-abzug-versicherungspraemien"></a>
### Ziff. Form. 6 Teil B/C – Maximaler Abzug (Code 600 B): Fr. 5'400 gemeinsam / Fr. 2'700 übrige + Fr. 1'000 je Kind; Abzug = niedrigerer Betrag aus A und B (Code 600) -> Ziff. 14

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeilen
- **Rein:** Übertrag Code 600 A (Teil A) · Zivilstand (gemeinsam/alleinstehend) + Kinder mit Kinderabzug Ziff. 23.1–23.3
- **Rechnen:** Code 600 = min(600 A; 600 B) → Ziff. 14; 600 B Kanton: 5'400 gemeinsam bzw. 2'700 + 1'000 je Kind / Bund (mit Säule 2/3a): 3'700 bzw. 1'800 + 700 je Kind
- **Regel:** Siehe Ziff. 14.
- **Beachten:** Kinderzuschlag nur für Kinder mit Kinderabzug nach Ziff. 23.1, 23.2 oder 23.3
- **Beachten:** Bund ohne Beiträge an Säule 2/3a: 5'550 gemeinsam / 2'700 übrige
- **Beachten:** Prämienverbilligung ist bereits in 600 A abgezogen
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'400 (Versicherungsprämien und Sparzinsen: in ungetrennter Ehe lebende Personen max. CHF 5'400 (abzüglich Prämienverbilligung).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'700 (Versicherungsprämien und Sparzinsen: übrige Steuerpflichtige max. CHF 2'700 (abzüglich Prämienverbilligung).)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'000 (Zuschlag pro Kind (bzw. unterstützte Person mit Abzug nach Art. 38) CHF 1'000.)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – AR kennt keine Unterscheidung nach Beiträgen 2. Säule/3a beim Versicherungsabzug; einheitlicher Betrag (Art. 35 lit. g StG).** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an Säule 2/3a (Erhöhung um die Hälfte))**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **n/a – AR kennt keine Unterscheidung nach Beiträgen 2. Säule/3a beim Versicherungsabzug.** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an Säule 2/3a)**
- **Bemerkung:** Code 600 B / 600.
- **Quellen:**
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Fr. 5’400 für gemeinsam Steuerpflichtige»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Total der Abzüge für Versicherungsprämien und Sparzinsen 600 B»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «Der niedrigere Betrag von (A) und (B) 600»
  - [Formular 6 AR 2025 S. 1](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md) `ar-form-06-2025__c0002` – «zusätzlich für jedes Kind, für das der Kinderabzug gemäss Ziffer»

<a id="form-6-s-2-abzug-krankheitskosten"></a>
### Ziff. Form. 6 S. 2 – Krankheits- und Unfallkosten: Rechnungsdatum, Arzt/Zahnarzt/Spital, Bruttobetrag abzüglich Beiträge Dritter = selbst getragene Kosten; Total -> Ziff. 21.1 (Vorkolonne)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Arzt-/Zahnarztrechnungen und KK-Leistungsabrechnung (Vergütungen Dritter)
- **Rein:** Arzt-/Zahnarzt-/Spitalrechnungen → Rechnungsdatum, Bruttobetrag · Leistungsabrechnung Krankenkasse/Versicherung → Beiträge Dritter (abziehen) · Ärztliches Zeugnis → Medikamente/Heilmittel; ärztliche Anordnung → Diät
- **Rechnen:** Σ (Brutto − Beiträge Dritter) → Ziff. 21.1 Vorkolonne; Abzug = Σ − 5 % × Nettoeinkommen Ziff. 20 (nur Überschuss); Kanton = Bund
- **Regel:** Nur selbst getragene Kosten; Selbstbehalt 5 % des Nettoeinkommens wird in der Steuererklärung (Ziff. 21.1) berechnet.
- **Beachten:** Lebensnotwendige Diät (z.B. Zöliakie): Pauschale Fr. 2'500 statt Mehrkosten, Kanton = Bund; Diabetes nur effektiv
- **Beachten:** Altersresidenz mit Pflege < 60 Min./Tag (Pflegestufe 1 bis 3): Pflegekosten hier; reine Pension = Lebenshaltung
- **Beachten:** Dauerhaft Pflegeheim ab Pflegestufe 4 → behinderungsbedingte Kosten Ziff. 21.2
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten: abziehbar, soweit sie 5 % der um die Aufwendungen gemäss Art. 28-35 verminderten steuerbaren Einkünfte übersteigen.)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Quellen:**
  - [Formular 6 AR 2025 S. 2](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0003.md) `ar-form-06-2025__c0003` – «Hinweis: Abzugsfähig sind die tatsächlich selbst getragenen Kosten»
  - [Formular 6 AR 2025 S. 2](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0003.md) `ar-form-06-2025__c0003` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.1 (Vorkolonne)»
  - [WL AR 2025 S. 2](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) `ar-wl-2025__c0004` – «Krankheits- und Unfallkosten, Selbstbehalt vom Nettoeinkommen 5%»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0098.md) `ar-wl-2025__c0098` – «(ärztliches Zeugnis beilegen)»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0098.md) `ar-wl-2025__c0098` – «von weniger als 60 Minuten (Pflegestufe 1 bis 3) pro Tag anfällt»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0099.md) `ar-wl-2025__c0099` – «5 Prozent des Nettoeinkommens gemäss Ziffer 20 übersteigen»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0099.md) `ar-wl-2025__c0099` – «bei Zöliakie, nicht jedoch bei Diabetes»
  - [KS 11 S. 5–6](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0009.md) `bund-ks-11__c0009` – «eine Pauschale von CHF 2'500.-- geltend gemacht werden»
  - [KS 11 S. 5–6](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0009.md) `bund-ks-11__c0009` – «sonen können jedoch nur die effektiven Mehrkosten zum Abzug bringen.»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0100.md) `ar-wl-2025__c0100` – «(ab Pflegestufe 4 bzw. ab 61»

<a id="form-6-s-2-behinderungsbedingt-abzug-behinderungskosten"></a>
### Ziff. Form. 6 S. 2 (behinderungsbedingt) – Behinderungsbedingte Kosten (Einzelleistungen); Total -> Ziff. 21.2

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Rechnungen/Verfügungen (Hinweise in der Wegleitung)
- **Rein:** Rechnungen behinderungsbedingter Leistungen → Bruttobetrag, Vergütungen Dritter · Pflegeheim: Bewohnerkonto des Jahres (beilegen) · Verfügung Hilflosenentschädigung (HE) bei Pauschale
- **Rechnen:** Σ (Brutto − Vergütungen Dritter) → Ziff. 21.2 Hauptkolonne, ohne Selbstbehalt (Kanton = Bund); Kanton Pflegeheim ab Pflegestufe 4: 2/3 × selbstgetragene Heimkosten − HE AHV/IV
- **Regel:** Selbst getragene Kosten ohne steuerlichen Selbstbehalt abziehbar (Vergütungen Dritter sind abzuziehen); Details siehe Ziff. 21.2.
- **Beachten:** Statt effektiv: Pauschale HE leicht 2'500 / mittel 5'000 / schwer 7'500 (Verfügung beilegen); Kanton = Bund
- **Beachten:** Gehörlose und Nierenkranke mit Dialyse: Pauschale Fr. 2'500 pro Jahr; Kanton = Bund
- **Beachten:** Pflegeheim: Weisung und Berechnungsformular auf www.ar.ch/steuerverwaltung (FAQ)
- **Quellen:**
  - [Formular 6 AR 2025 S. 2](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0004.md) `ar-form-06-2025__c0004` – «Behinderungsbedingte Kosten (siehe Hinweise in der Wegleitung)»
  - [Formular 6 AR 2025 S. 2](../../chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0004.md) `ar-form-06-2025__c0004` – «zu übertragen in die Steuererklärung Seite 3 Ziffer 21.2»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0100.md) `ar-wl-2025__c0100` – «können ohne steuerlichen»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0100.md) `ar-wl-2025__c0100` – «Selbstbehalt in Abzug gebracht»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0100.md) `ar-wl-2025__c0100` – «vom entsprechenden Jahr des Pflegeheims ist beizulegen»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0100.md) `ar-wl-2025__c0100` – «Die Hilflosenentschädigung AHV/IV und weitere Vergütungen Dritter sind davon»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0101.md) `ar-wl-2025__c0101` – «Bezüger einer Hilflosenentschädigung schweren Grades:»
  - [WL AR 2025 S. 18](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0101.md) `ar-wl-2025__c0101` – «Nierenkranken, die sich einer Dialyse unterziehen müssen»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t3.md) `bund-dbg-2025__art-33-t3` – «die behinderungsbedingten Kosten des Steuerpflichtigen oder der von ihm unterhaltenen Personen mit Behinderungen»
  - [KS 11 S. 10](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0025.md) `bund-ks-11__c0025` – «Bezüger einer Hilflosenentschädigung schweren Grades: CHF 7'500.--»
  - [KS 11 S. 10](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0025.md) `bund-ks-11__c0025` – «Nierenkranke, die sich einer Dialyse unterziehen müssen»

## Hilfsblatt Liegenschaften (Form. 7/7Z)

<a id="form-7-abschn-a-vermoegen-liegenschaften"></a>
### Ziff. Form. 7 Abschn. A – Angaben zur Liegenschaft, Anteil Person 1/2, Nutzung, Baujahr, Steuerwert (Verkehrswert gemäss Grundstückschätzung)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Amtliche Grundstückschätzung (Steuerwert, Grundstücknummer, Baujahr)
- **Rein:** Amtliche Schätzung (Steuerwert vom Grundbuchamt eröffnet) → Steuerwert (Verkehrswert), Grundstück-Nr. · Grundbuch/Kaufvertrag → Anteil Person 1/2 in %, Baujahr, Datum Zugang/Wegfall · Ausserkantonal: dortiger Steuerwert; Ausland: mutmasslicher Verkehrswert
- **Rechnen:** Steuerwert = amtliche Schätzung (Neu-/Anbau ohne Schätzung: i.d.R. + 80 % der Baukosten) → Ziff. 31 bzw. Form. 7Z Spalte A
- **Regel:** Pro Liegenschaft ein Formular; Baujahr bestimmt Alter (10-Jahres-Grenze Pauschale) am Stichtag der Vermögenssteuer; Zugang/Wegfall im Jahr 2025 mit Datum/Grund; Steuerwert -> Ziff. 31 (bzw. Form. 7Z).
- **Beachten:** Pro Liegenschaft ein Formular 7; bei mehr als einer Liegenschaft Zusammenzug in Form. 7Z
- **Beachten:** Gebäudealter (Kanton: Stichtag Vermögenssteuer; Bund: Beginn Steuerperiode) bestimmt Pauschale: bis 10 J. 10 %, älter 20 %
- **Beachten:** Zugang/Wegfall nur ausfüllen, wenn Ereignis in der Steuerperiode 2025
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Pauschalabzug Liegenschaftsunterhalt: 10 % des Bruttomietertrags bei Gebäuden bis 10 Jahre (Wahlrecht je Gebäude und Periode zwischen Pauschale und effektiven Kosten); nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt: 20 % des Bruttomietertrags für ältere Gebäude (über 10 Jahre); nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0001.md) `ar-form-07-2025__c0001` – «Steuerwert in Fr. (Verkehrswert gemäss Grundstückschätzung)»
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0001.md) `ar-form-07-2025__c0001` – «Pro Liegenschaft ist ein separates Formular zu verwenden»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0164.md) `ar-wl-2025__c0164` – «Diese kann der amtlichen Schätzung entnommen werden.»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0165.md) `ar-wl-2025__c0165` – «Der massgebliche Steuerwert wird vom Grundbuchamt eröffnet.»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0165.md) `ar-wl-2025__c0165` – «amtlichen Verkehrswertschätzung im Ausmass von 80 Prozent der Neu- oder An»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0165.md) `ar-wl-2025__c0165` – «im Ausland gelegene Grundstücke mit dem mutmasslichen»
  - [WL AR 2025 S. 32](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0175.md) `ar-wl-2025__c0175` – «bis und mit 10 Jahre 10 % vom Total Liegenschaftserträge»
  - [Formular 7Z AR 2025 S. 1](../../chunks/ar/2025/ar-form-07z-2025/ar-form-07z-2025__c0001.md) `ar-form-07z-2025__c0001` – «Bei Besitz von mehr als einer Liegenschaft sind die einzelnen Ergebnisse je Liegenschaft»

<a id="form-7-abschn-b-a-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 7 Abschn. B a – Eigenmietwert abzüglich 20 % = anrechenbarer Eigenmietwert

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Amtliche Grundstückschätzung (Mietwert)
- **Rein:** Amtliche Grundstückschätzung → Mietwert · Belege wertvermehrender Um-/Anbauten seit der letzten Schätzung
- **Rechnen:** Kanton: (Mietwert letzte Schätzung + 2.8 % × nicht erfasste wertvermehrende Investitionen) − 20 % Selbstnutzungsabzug = anrechenbarer Eigenmietwert
- **Regel:** Mietwert der letzten amtlichen Schätzung; nicht erfasste Um-/Anbauten +2,8 % der Aufwendungen; Selbstnutzungsabzug 20 % nur am Wohnsitz dauernd selbst bewohnt (nicht Zweit-/Ferienwohnung/Landwirtschaft).
- **Beachten:** 20 %-Abzug nur am Wohnsitz dauernd selbst bewohnt; nicht bei Zweit-/Ferienwohnung und Landwirtschaft
- **Beachten:** Auch Nutzniessungs-/Wohnrechtsberechtigte; Vorzugsmiete an Nahestehende: voller Mietwert steuerbar
- **Beachten:** Ohne amtliche Schätzung: Mietwert gemäss Merkblatt der Steuerverwaltung
- **Limiten:**
  - Eigenmietwert – Einschlag/Abzug für selbstbewohnte Liegenschaft (%): Kanton **20 % (Selbstnutzungsabzug 20 % auf dem Eigenmietwert; nur auf der am Wohnsitz dauernd selbst bewohnten Liegenschaft.)** · Bund **n/a – Eigenmietwert wird nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt (Art. 21 Abs. 2 DBG); Abschaffung per 01.01.2029 beschlossen, 2025–2028 gilt bisheriges Recht. Der Eigenmietwert für die direkte Bundessteuer wird im kantonalen Veranlagungsverfahren festgesetzt; ein dort vorgesehener Abzug für die DBSt (z.B. TG 20 %, siehe werte-tg) ist kantonale Vollzugspraxis, kein Widerspruch.**
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0002.md) `ar-form-07-2025__c0002` – «Total anrechenbarer Eigenmietwert»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0166.md) `ar-wl-2025__c0166` – «entspricht dem massgeblichen Mietwert abzüglich 20 Prozent»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0166.md) `ar-wl-2025__c0166` – «2.8 Prozent der Aufwendungen berücksichtigt»
  - [MB AR 07 S. 1–2](../../chunks/ar/dauernd/ar-mb-07/ar-mb-07__c0003.md) `ar-mb-07__c0003` – «sowie von Nutzniessungs- und Wohnrechtsberechtigten in Abzug gebracht wer»
  - [MB AR 07 S. 1](../../chunks/ar/dauernd/ar-mb-07/ar-mb-07__c0002.md) `ar-mb-07__c0002` – «Die Kantonale Steuerverwaltung erlässt ein Merkblatt, wie der massgebliche Mietwert erhoben wird, wenn keine amtliche Schätzung vorliegt.»

<a id="form-7-abschn-b-b-einkommen-liegenschaften-mietertrag"></a>
### Ziff. Form. 7 Abschn. B b – Erträge Fremdnutzung und Leistungen Dritter (Miet-/Pachtzinsen abzüglich Nebenkosten), inkl. PV-Einspeisevergütung

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Mietverträge/Mietzinsabrechnung, Abrechnung Netzbetreiber
- **Rein:** Mietverträge/Mietzinsabrechnung → Miet-/Pachtzinsen netto (ohne Nebenkosten) · Abrechnung Netzbetreiber → PV-Einspeisevergütung und Kosten Eigenverbrauch · Aufstellung Leistungen Dritter; Geschäfts-/Büroräume separat
- **Rechnen:** Miet-/Pachtzinsen + Leistungen Dritter + Geschäfts-/Büroräume − Nebenkosten = Total Fremdnutzung (b); a + b → Ziff. 5 bzw. Form. 7Z Spalte B
- **Regel:** Netto-Mietzins ohne Nebenkosten; Einspeisevergütung PV steuerbar abzüglich Eigenverbrauch (Netto); Total Erträge a.+b. -> Ziff. 5.
- **Beachten:** PV (Eigenbedarfsdeckung): Einspeisevergütung − Eigenverbrauch (ohne Gebühren), unter Leistungen Dritter
- **Beachten:** Kanton: Unterhaltspauschale 10 %/20 % nur, wenn Bruttomietertrag aller Liegenschaften ≤ Fr. 100'000
- **Beachten:** Nur Privatvermögen; Geschäftsliegenschaften bei selbständiger Erwerbstätigkeit
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Pauschalabzug Liegenschaftsunterhalt: 10 % des Bruttomietertrags bei Gebäuden bis 10 Jahre (Wahlrecht je Gebäude und Periode zwischen Pauschale und effektiven Kosten); nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt: 20 % des Bruttomietertrags für ältere Gebäude (über 10 Jahre); nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0002.md) `ar-form-07-2025__c0002` – «Total steuerbare Erträge Fremdnutzung und Leistungen Dritter»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0167.md) `ar-wl-2025__c0167` – «Miet- und Pachtzinsen bei Fremd- nutzung ohne Nebenkosten (Netto-Mietzins)»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0167.md) `ar-wl-2025__c0167` – «d.h. Gesamtvergütung abzüglich»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0167.md) `ar-wl-2025__c0167` – «deklarieren unter Leistungen»
  - [WL AR 2025 S. 32](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0175.md) `ar-wl-2025__c0175` – «Bruttomietertrag des gesamten Liegenschaftsbesitzes Fr. 100’000.– nicht über»
  - [WL AR 2025 S. 11](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0058.md) `ar-wl-2025__c0058` – «Anzugeben sind die Einkünfte aus Liegenschaften des Privatvermögens.»

<a id="form-7-abschn-c-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 7 Abschn. C – Unterhalts- und Verwaltungskosten: Pauschalabzug (C1) oder tatsächliche Kosten (C2, Rückseite)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Rechnungen (Datum, Rechnungssteller, Beschreibung, Unterhalt/Anlagekosten/Verwaltung)
- **Rein:** Handwerker-/Unterhaltsrechnungen → Form. 7 Rückseite: Datum, Rechnungssteller, Total netto, davon Anlagekosten bzw. Unterhalt/Verwaltung · Prämienrechnungen Gebäudeversicherungen (Brand, Wasserschaden, Glas, Gebäudehaftpflicht), Wartung Heizung → C2 · STWE-Abrechnung → eigener Anteil inkl. Einlage Erneuerungsfonds, ohne Heiz-/Warmwasser-/Stromkosten; Liegenschaftenrechnung → Total in C2, beilegen · Abrechnungen Versicherungsleistungen, Förderbeiträge Energie → in C2 abziehen (Förderbeitrag erst in Folgeperiode: Ziff. 6.3)
- **Rechnen:** je Gebäude: C1 = Erträge (B) × 10 % (≤ 10 J.) bzw. 20 % (> 10 J.) oder C2 = Σ Anteil Unterhalt/Verwaltung − Leistungen Dritter → Ziff. 15 bzw. 7Z
- **Regel:** Pauschale nur für private, ganz/vorwiegend Wohnzwecken dienende Liegenschaften; tatsächlich: nur selbst bezahlte Kosten (Versicherungsleistungen, Förderbeiträge abziehen), Einzelbeträge ab Fr. 5'000 mit Rechnungskopie; wertvermehrende Anlagekosten nicht abziehbar.
- **Beachten:** Kanton: Pauschale nur bei Bruttomietertrag gesamter Liegenschaftsbesitz ≤ Fr. 100'000; Wahl C1/C2 je Gebäude und Jahr
- **Beachten:** Kanton: Alter per Stichtag Vermögenssteuer, EMW netto / Bund: Alter zu Beginn Steuerperiode, Brutto-Eigenmietwert
- **Beachten:** Nicht abziehbar: Wertvermehrung; bei Eigengebrauch Verbrauch/Heizung/Kehricht; ab Fr. 5'000 Rechnungskopie beilegen
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **10 % (Pauschalabzug Liegenschaftsunterhalt: 10 % des Bruttomietertrags bei Gebäuden bis 10 Jahre (Wahlrecht je Gebäude und Periode zwischen Pauschale und effektiven Kosten); nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Pauschalabzug Liegenschaftsunterhalt: 20 % des Bruttomietertrags für ältere Gebäude (über 10 Jahre); nur wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Quellen:**
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0003.md) `ar-form-07-2025__c0003` – «Der Pauschalabzug kann nur»
  - [Formular 7 AR 2025 S. 2](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0004.md) `ar-form-07-2025__c0004` – «Bitte fügen Sie für Einzelbeträge ab Fr. 5’000 die Rechnungskopien»
  - [Formular 7 AR 2025 S. 2](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0005.md) `ar-form-07-2025__c0005` – «Total Unterhalts- und Verwaltungskosten (C2)»
  - [WL AR 2025 S. 32](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0175.md) `ar-wl-2025__c0175` – «Bruttomietertrag des gesamten Liegenschaftsbesitzes Fr. 100’000.–»
  - [WL AR 2025 S. 32](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0175.md) `ar-wl-2025__c0175` – «Steuerperiode massgebenden Stichtag für die Vermögens»
  - [WL AR 2025 S. 32](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0175.md) `ar-wl-2025__c0175` – «Das Wahlrecht ist für jedes einzelne Gebäude gegeben»
  - [MB AR 03 S. 6](../../chunks/ar/dauernd/ar-mb-03/ar-mb-03__c0017.md) `ar-mb-03__c0017` – «Bei der Anrechnung eines Eigenmietwertes ist dieser massgebend (Nettobetrag).»
  - [WL 2a 2025 S. 5–6](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0036.md) `bund-wl-2a-2025__c0036` – «das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags beziehungsweise des Brutto-Eigenmiet-werts»
  - [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0170.md) `ar-wl-2025__c0170` – «die Prämien für die Brand-, Wasserschaden-, Glas- und Gebäudehaftpflicht»
  - [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0170.md) `ar-wl-2025__c0170` – «die Wartungsarbeiten an liegenschaftlichen Einrichtungen (z.B. Heizung);»
  - [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0170.md) `ar-wl-2025__c0170` – «Nicht abziehbar sind die periodisch anfallenden Grundgebühren für Wasser-,»
  - [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0170.md) `ar-wl-2025__c0170` – «Kosten gelten als nicht abzugsfähige Lebenshaltungskosten»
  - [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0169.md) `ar-wl-2025__c0169` – «Nicht abzugsberechtigt sind Ausgaben, die eine Wertvermehrung der»
  - [WL AR 2025 S. 32](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0174.md) `ar-wl-2025__c0174` – «der Regel auch die Einlagen in den Reparatur- und Erneuerungsfonds als Unter-»
  - [WL AR 2025 S. 32](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0174.md) `ar-wl-2025__c0174` – «Heiz-, Warmwasser- und Stromkosten) abgezogen werden»
  - [WL AR 2025 S. 32](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0174.md) `ar-wl-2025__c0174` – «kann das Total der tatsächlichen Unterhalts- und Verwaltungskosten beim Feld»
  - [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0172.md) `ar-wl-2025__c0172` – «Die erhaltenen Förderbeiträge sind als Aufwandminderung im»
  - [WL AR 2025 S. 31](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0172.md) `ar-wl-2025__c0172` – «sind die Leistungen unter übrige Einkünfte (Ziffer 6.3) zu deklarieren»

<a id="form-7z-vermoegen-liegenschaften"></a>
### Ziff. Form. 7Z – Zusammenzug aller Liegenschaften: Spalten Steuerwert (A) -> Ziff. 31, Erträge (B) -> Ziff. 5, Pauschalabzug (C1) / tatsächliche Kosten (C2) -> Ziff. 15

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Ergebnisse der einzelnen Formulare 7
- **Rein:** Formulare 7 je Liegenschaft → Steuerwert (A), Erträge (B), Pauschalabzug (C1) bzw. tatsächliche Kosten (C2) · Steuerwert-Eröffnung Grundbuchamt → Spalte A
- **Rechnen:** Σ A → Ziff. 31 (Seite 4); Σ B → Ziff. 5 (Seite 2); Σ C1 + Σ C2 → Ziff. 15 (Seite 3)
- **Regel:** Nur bei mehr als einer Liegenschaft; einzelne Totale in die Steuererklärung übertragen.
- **Beachten:** Nur bei mehr als einer Liegenschaft, je Liegenschaft C1 oder C2; bei einer: Übertrag direkt ab Form. 7
- **Beachten:** Steuerwert per 31. Dezember 2025 bzw. Ende Steuerpflicht; anderer Kanton: dortiger Wert; Ausland: mutm. Verkehrswert
- **Beachten:** Neu-/Anbau ohne amtliche Schätzung: i.d.R. Zuschlag 80 % der Neu-/Anbaukosten zur geltenden Schätzung
- **Quellen:**
  - [Formular 7Z AR 2025 S. 1](../../chunks/ar/2025/ar-form-07z-2025/ar-form-07z-2025__c0003.md) `ar-form-07z-2025__c0003` – «zu übertragen in die Steuererklärung Seite 4 Ziffer 31 Seite 2 Ziffer 5 Seite 3 Ziffer 15»
  - [Formular 7Z AR 2025 S. 1](../../chunks/ar/2025/ar-form-07z-2025/ar-form-07z-2025__c0001.md) `ar-form-07z-2025__c0001` – «Bei Besitz von mehr als einer Liegenschaft sind die einzelnen Ergebnisse je Liegenschaft von den Formularen 7 in»
  - [Formular 7 AR 2025 S. 1](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0003.md) `ar-form-07-2025__c0003` – «Übertrag in die Steuererklärung Seite 3 Ziffer 15»
  - [Formular 7 AR 2025 S. 2](../../chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0004.md) `ar-form-07-2025__c0004` – «halts- und Verwaltungskosten anstelle des Pauschalabzugs geltend gemacht werden»
  - [Formular 7Z AR 2025 S. 1](../../chunks/ar/2025/ar-form-07z-2025/ar-form-07z-2025__c0001.md) `ar-form-07z-2025__c0001` – «31. Dezember 2025»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0165.md) `ar-wl-2025__c0165` – «Der massgebliche Steuerwert wird vom Grundbuchamt eröffnet»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0165.md) `ar-wl-2025__c0165` – «tonen gelegene Grundstücke sind mit dem entsprechenden Steuerwert (Verkehrs-»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0165.md) `ar-wl-2025__c0165` – «bzw. Ertragswert), im Ausland gelegene Grundstücke mit dem mutmasslichen»
  - [WL AR 2025 S. 30](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0165.md) `ar-wl-2025__c0165` – «Zuschlag zur geltenden amtlichen Verkehrswertschätzung im Ausmass von 80 Prozent der Neu- oder An-»

## Hilfsblatt Kinderbetreuung (Form. 10)

<a id="form-10-abzug-drittbetreuung"></a>
### Ziff. Form. 10 – Kinderbetreuungskosten: Rechnungsdatum, Name des Kindes, Empfänger, Kosten; tatsächliche Kosten abzüglich erhaltene Beiträge; Total -> Ziff. 16.2

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Rechnungen Krippe/Tagesfamilie (Empfänger ersichtlich)
- **Rein:** Rechnungen/Quittungen Kinderkrippe, Kinderhort, Tagesfamilie → Rechnungsdatum, Name Kind, Empfänger, Kosten 2025 · Lohnabrechnungen Betreuungsperson (z.B. Tagesmutter) → Kosten · Belege Fahrkosten zur Betreuungsstätte → Kosten · Verfügung/Abrechnung Betreuungsbeiträge (Kinderbetreuungsgesetz) → «Abzüglich erhaltene Beiträge»
- **Rechnen:** Σ je Kind min(Kosten exkl. Verpflegung − erhaltene Beiträge; Kanton Fr. 25'000 / Bund Fr. 25'800) → Ziff. 16.2
- **Regel:** Max. Fr. 25'000 pro Kind unter 14 Jahren; ohne Verpflegung; erhaltene Betreuungsbeiträge abziehen.
- **Beachten:** Nur Kind < 14 (bis 14. Geburtstag), gleicher Haushalt, Kosten kausal zu Erwerb/Ausbildung/Erwerbsunfähigkeit
- **Beachten:** Paare/Konkubinat: beide erwerbstätig, in Ausbildung oder erwerbs- + betreuungsunfähig; Bund: nicht ausser Arbeitszeit
- **Beachten:** Verpflegung/Mittagstisch nicht abziehbar (Bund: auch Unterkunft); Belege auf Verlangen, Empfänger muss ersichtlich sein
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 25'000 (Kinderdrittbetreuungskosten: nachgewiesene Kosten max. CHF 25'000 pro Kind.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind bis max. CHF 25'800 (Kind unter 14, im gleichen Haushalt, Zusammenhang mit Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit))**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat (bis zum 14. Geburtstag), im gleichen Haushalt.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat)**
- **Quellen:**
  - [Formular 10 AR 2025 S. 1](../../chunks/ar/2025/ar-form-10-2025/ar-form-10-2025__c0001.md) `ar-form-10-2025__c0001` – «Abzüglich erhaltene Beiträge»
  - [Formular 10 AR 2025 S. 1](../../chunks/ar/2025/ar-form-10-2025/ar-form-10-2025__c0002.md) `ar-form-10-2025__c0002` – «Total Kinderbetreuungskosten»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0090.md) `ar-wl-2025__c0090` – «Kinderkrippen oder Kinderhorte. Als abziehbare»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0090.md) `ar-wl-2025__c0090` – «wie etwa Tagesmütter oder Tagesfamilien»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0090.md) `ar-wl-2025__c0090` – «Fahrkosten zur Betreuungsstätte gehören ebenfalls zu den Betreuungs-»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0090.md) `ar-wl-2025__c0090` – «nachzuweisen. Der Empfänger der Leistungen muss aus den»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0090.md) `ar-wl-2025__c0090` – «Drittbetreuungskosten geltend machen, wenn die Ehegatten gleichzeitig einer»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0090.md) `ar-wl-2025__c0090` – «Die Regelungen sind analog bei den Konkubi-»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0091.md) `ar-wl-2025__c0091` – «Die in den Drittbetreuungskosten enthaltenen Lebenshaltungskosten, z.B. Mit-»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0091.md) `ar-wl-2025__c0091` – «gen gemäss des Kinderbetreuungsgesetz erfüllt sind, mit Beiträgen unterstützt»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0091.md) `ar-wl-2025__c0091` – «tatsächlichen Betreuungskosten sind um die erhaltenen Beiträge zu reduzieren»
  - [WL AR 2025 S. 16](../../chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0089.md) `ar-wl-2025__c0089` – «d.h. bis zum 14. Geburtstag»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0054.md) `bund-wl-2a-2025__c0054` – «25 800 Fr., für die Drittbetreuung jedes Kindes (bis 14 Jahre),»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0055.md) `bund-wl-2a-2025__c0055` – «betreuungskosten ausserhalb der Arbeits- oder Ausbildungszeit»
  - [WL 2a 2025 S. 8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0055.md) `bund-wl-2a-2025__c0055` – «Gleiches gilt für die Kosten für Verpflegung und Unterkunft der»
