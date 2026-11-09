# OpenClaw-Testlauf: positionstest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 10 · Lauf: 2026-11-09 15:11
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## p01

**Frage:** ZH 2025: Ledige unselbständig erwerbende Person, Nettolohn gemäss Lohnausweis CHF 92'000. Sie fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 23 km einfach, 2 Fahrten pro Tag, 220 Arbeitstage. Übrige Berufskosten werden pauschal geltend gemacht (keine Verpflegungskosten). Welche Positionen/Codes im Formular «Berufsauslagen» und welcher Betrag geht in Ziffer 11.1 – Staatssteuer und Bundessteuer getrennt?

**Soll (Referenz):** Formular 360 «Berufsauslagen» (Person 1), Begründung Privatauto Code 2042 (Zeitersparnis über 1 Stunde) ankreuzen. Ziff. 1.3 Auto (CHF 0.70/km, Staat und Bund gleich): 23 km x 2 Fahrten x 220 Tage = 10'120 km x 0.70 = CHF 7'084 (Code 204). Zwischentotal Fahrkosten Code 205: Staat max. CHF 5'200 -> 5'200; Bund max. CHF 3'300 -> 3'300. Ziff. 3 übrige Berufskosten pauschal Code 212: 3% von 92'000 = CHF 2'760 (innerhalb mind. 2'000 / höchstens 4'000; Staat und Bund gleich, vgl. BKV-Anhang). Total Berufsauslagen Code 220 -> Steuererklärung Seite 3, Ziff. 11.1: Staat 5'200 + 2'760 = CHF 7'960; Bund 3'300 + 2'760 = CHF 6'060.

**Antwort des Agenten** (30.4 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert):

> **Ergebnis ZH 2025, Ziff. 11.1:** Staatssteuer **CHF 7'960**, Bundessteuer **CHF 6'060**. Die beiden Spalten weichen wegen des Fahrkostenplafonds ab (Kanton 5'200, Bund 3'300).
> 
> **Formular «Berufsauslagen» (Form. 360), Person 1**
> 
> | Code | Position | Staatssteuer | Bundessteuer |
> |---|---|---|---|
> | 204 | Auto: 23 km × 2 × 220 Tage = 10'120 km × CHF 0.70 = 7'084 | 7'084 | 7'084 |
> | 205 | Zwischentotal Fahrkosten (gedeckelt) | 5'200 | 3'300 |
> | 212 | Übrige Berufskosten, Pauschale 3 % von 92'000 = 2'760 (im Rahmen min. 2'000 / max. 4'000) | 2'760 | 2'760 |
> | 206/208/210 | Verpflegung | 0 | 0 |
> | 220 | Total → **Ziff. 11.1** | **7'960** | **6'060** |
> 
> **Hinweise**
> 
> - **Auto-Begründung:** Im Kanton ist das Privatauto nur bei fehlendem ÖV, mehr als 1 Stunde Zeitersparnis, Verlangen des Arbeitgebers oder Krankheit zulässig. Die Begründung (Zeitersparnis über 1 Stunde) muss in Ziff. 7 stehen. Ich habe keine Quelle für den Bund gefunden, die genau diese Voraussetzung nennt. Der Bund verlangt laut Wiki nur, dass kein öffentliches Verkehrsmittel verfügbar oder zumutbar ist. Die Begründung sollte deshalb auch den fehlenden ÖV-Vergleich abdecken. Das ist nicht geprüft.
> - **Arbeitstage:** 220 Tage liegen unter der kantonalen Grenze von 240 Tagen für den Kilometerabzug. Beim Bund gibt es keine Arbeitstage-Regel.
> - **Pauschale:** Die Pauschale ist beim Bund gleich hoch wie beim Kanton. Sie gilt, solange keine effektiven Kosten mit vollem Nachweis geltend gemacht werden.
> - **Status:** Die Werte sind agent-geprüft (Fundstellen geprüft), die Abnahme ist noch offen.
> 
> Quellen: zh-form-300-2025__c0007, zh-form-360-2025__c0004, zh-wl-2025__c0060, zh-wl-2025__c0064, zh-stg-2025__par-26, bund-dbg-2025__art-26, bund-bkv-2025__anhang-1.

## p02

**Frage:** ZH 2025: Verheiratetes Paar, beide in einer Pensionskasse (2. Säule) versichert, zwei minderjährige Kinder mit Kinderabzug. Bezahlte Krankenkassenprämien 2025 (bereits netto nach individueller Prämienverbilligung) CHF 15'600, Sparzinsen gemäss Wertschriftenverzeichnis CHF 150. Wie wird das Formular «Versicherungsprämien» ausgefüllt und welcher Abzug kommt in Ziffer 15 (Staat / Bund)?

**Soll (Referenz):** Formular 365 «Versicherungsprämien»: Teil A: Code 601 Krankenversicherungsprämien 15'600 + Code 604 Sparzinsen 150 -> Total (A) Code 606 = CHF 15'750. Teil B (Maximum): Verheiratete mit Beiträgen an 2. Säule/3a Code 611: Staat 5'800 / Bund 3'700; Kinderzuschlag Code 613: Staat 2 x 1'300 = 2'600 / Bund 2 x 700 = 1'400 -> Total (B) Code 616: Staat CHF 8'400 / Bund CHF 5'100. Teil C Code 270 = der niedrigere Betrag von (A) und (B): Staat CHF 8'400, Bund CHF 5'100 -> Steuererklärung Seite 3, Ziff. 15 (Spalten Staatssteuer/Bundessteuer).

**Antwort des Agenten** (28.3 s · Tools: 2 Aufrufe steuerwiki__position):

> **Ergebnis Ziffer 15 (ZH 2025, Staat/Bund): Staat CHF 8'400, Bund CHF 5'100.** Die Prämien (CHF 15'750) liegen über den Maxima, deshalb greift der Höchstbetrag.
> 
> **1. Hilfsblatt Versicherungsprämien (Form. 365, Teil A)**
> 
> | Code | Position | Eintrag |
> |---|---|---|
> | 601 | Bezahlte Krankenversicherungsprämien (nach IPV-Verrechnung) | 15'600 |
> | 602 | Unfallversicherung (privat) | 0 |
> | 603 | Lebens-/Rentenversicherung | 0 |
> | 604 | Zinsen von Sparkapitalien (Wertschriftenverzeichnis) | 150 |
> | 605 | Abzüglich erhaltene Prämienverbilligung | leer |
> | 607 | Zwischentotal (601–604) | 15'750 |
> | 606 | Total (A) = 607 − 605 | 15'750 |
> 
> Die IPV ist bereits in den 15'600 verrechnet. Sie darf nicht zusätzlich unter 605 abgezogen werden (kein Doppelabzug).
> 
> **2. Maximalabzug (Form. 365, Teil B, Code 616)**
> 
> | | Staat | Bund |
> |---|---|---|
> | Verheiratet, mit 2. Säule (Code 611) | 5'800 | 3'700 |
> | Zwei Kinder à 1'300 / 700 (Code 613–615) | 2'600 | 1'400 |
> | **Maximum B** | **8'400** | **5'100** |
> 
> Der Ohne-2./3a-Betrag (8'700 / 5'550) gilt nicht, weil beide Ehegatten in der 2. Säule versichert sind.
> 
> **3. Ziffer 15 (Abzüge, Code 270)**
> 
> Abzug = min(A; B) je Spalte:
> - **Staat:** min(15'750; 8'400) = **8'400**
> - **Bund:** min(15'750; 5'100) = **5'100**
> 
> Die Bundesspalte wird separat eingetragen, weil der Bund tiefere Maxima hat.
> 
> **Hinweise**
> - Die Angaben stammen aus dem Wiki (Quellen: zh-form-365-2025__c0001, zh-form-300-2025__c0008, zh-wl-2025__c0082). Sie sind als ☑️ agent-geprüft markiert: Die Fundstellen sind geprüft, die fachliche Abnahme steht aber noch aus.
> - Die 150 Franken gehören nur dann in 604, wenn sie aus Sparkapital stammen (Sparkonto, Festgeld, Kassenobligation mit Zins). Bei anderen Wertpapier-Erträgen ist das nicht der richtige Code.
> - Belege: Die Prämienrechnung bzw. Jahresbescheinigung der Krankenkasse sollte bereitliegen. Eingereicht werden muss sie nur auf Verlangen, das Formular Versicherungsprämien ist aber immer beizulegen.

## p03

**Frage:** ZH 2025: Alleinstehende Mandantin unterstützt ihre erwerbsunfähige Mutter (eigener Haushalt, keine Alimente, kein Kinderabzug) nachweislich mit CHF 5'000 im Jahr 2025. In welcher Ziffer wird das geltend gemacht, welcher Abzug gilt bei der Staatssteuer und bei der Bundessteuer, und wirkt sich das auf den Versicherungsprämienabzug aus?

**Soll (Referenz):** Ziff. 24.2 «Abzug für unterstützte Personen» (Code 374); Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der Unterstützung beilegen. Staat: Voraussetzung Unterstützungsleistung mindestens CHF 2'800 -> 5'000 erfüllt -> Abzug CHF 2'800. Bund: Voraussetzung Unterstützungsleistung mindestens CHF 6'800 (Art. 35 Abs. 1 lit. b DBG) -> 5'000 < 6'800 -> kein Unterstützungsabzug (CHF 0). Folge im Formular 365 Teil B.3: Staat zusätzlicher Abzug CHF 1'300 für die unterstützungsbedürftige Person (Code 614); Bund kein Zuschlag von CHF 700 (Code 615), da kein Unterstützungsabzug zusteht.

**Antwort des Agenten** (35.5 s · Tools: 6 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__suche):

> **Kanton ZH, Steuerjahr 2025.** Die Mutter ist erwerbsunfähig, und die Mandantin unterstützt sie mit CHF 5'000. Daraus ergibt sich:
> 
> **1. Formularziffer**
> - Ziff. **24.2** «Abzug für unterstützte Personen» (Code **374**), Teil Einkommensberechnung. ☑️ agent-geprüft, Abnahme offen. (zh-form-300-2025__c0010)
> - Ziff. **Seite 1** (Personalien): Name, Geburtsjahr, Adresse und Unterstützungsbetrag pro Jahr der Mutter eintragen. Dazu die Bestätigung der Mutter über Art, Zeitpunkt und Höhe der Unterstützung beilegen. (zh-form-300-2025__c0002)
> 
> **2. Staatssteuer (Kanton ZH)**
> - Limite CHF **2'800**. Die Unterstützung von CHF 5'000 erreicht diese Schwelle, also gilt der **fixe Abzug von CHF 2'800**, nicht die effektiven CHF 5'000.
> - Bedingung für den Abzug: Die Mutter muss bedürftig sein (Einkommen < 15'000 und Vermögen < 50'000, ZStB 34.1). Diese Werte sind nicht bekannt und müssen geprüft werden.
> 
> **3. Bundessteuer**
> - Limite CHF **6'800**. Die Unterstützung von CHF 5'000 liegt darunter. Es gilt daher **kein Unterstützungsabzug im Bund (CHF 0)**. Der Abzug wird nicht anteilig gewährt. (bund-dbg-2025__art-35)
> - Die Staats- und Bundeswerte werden getrennt deklariert.
> 
> **4. Auswirkung auf den Versicherungsprämienabzug (Ziff. 15, Code 270)**
> - **Ja, aber nur auf die Obergrenze.** Pro unterstützte Person, für die ein Unterstützungsabzug geltend gemacht werden kann, erhöht sich das Maximum um:
>   - **Staat: +CHF 1'300**
>   - **Bund: +CHF 700**
>   (zh-stg-2025__par-31-t2; Form. 365 Code 616)
> - Die Mutter zählt für den Staat, weil dort der Abzug von CHF 2'800 gilt. Für den Bund ist das nicht gesichert: Mit CHF 5'000 gibt es dort keinen Unterstützungsabzug, daher ist der Zuschlag von CHF 700 im Bund wahrscheinlich **nicht anwendbar**. Das ist meine Ableitung aus dem Wortlaut, nicht ausdrücklich belegt. Bitte bei der Abnahme prüfen.
> - Der Zuschlag erhöht nur die Obergrenze. Der tatsächliche Abzug ist **min(bezahlte Prämien und Sparzinsen; Maximum)**.
> - Obergrenzen für Alleinstehende mit Zuschlag (Staat, Vorsorgebeiträge vorhanden): 2'900 + 1'300 = **4'200**. Ohne Vorsorgebeiträge: 4'350 + 1'300 = **5'650**.
> - Für den Bund: 1'800 (ohne Zuschlag, da keine Unterstützung ≥ 6'800). Die Pensionskassen-Angabe auf Seite 1 bestimmt, welche Obergrenze gilt.
> 
> **Offen zu prüfen:** Bedürftigkeit der Mutter (Einkommen und Vermögen), Erwerbsunfähigkeit, und der Nachweis der CHF 5'000 durch die Bestätigung der Mutter.
> 
> Quellen: Chunks zh-form-300-2025__c0002, c0010, c0008; zh-stg-2025__par-34, par-31-t2; bund-dbg-2025__art-35, art-33-t2, art-33-t5.

## p04

**Frage:** SG 2025: Nettoeinkommen gemäss Ziffer 20 CHF 80'000. Arzt- und Zahnarztrechnungen 2025 brutto CHF 6'200, davon von der Krankenkasse vergütet CHF 1'700. Wo werden die Kosten deklariert und wie hoch ist der Abzug für die Staats- und Gemeindesteuern bzw. für die direkte Bundessteuer (Annahme: massgebendes Nettoeinkommen Bund ebenfalls CHF 80'000)?

**Soll (Referenz):** Formular 6 (Rückseite «Krankheits-, Unfall- und behinderungsbedingte Kosten»): Bruttobetrag 6'200 abzüglich Beiträge Dritter 1'700 = selbst getragene Kosten CHF 4'500 -> Steuererklärung Seite 3, Vorkolonne Ziff. 21.1 (Code 650). Kanton SG: Selbstbehalt 2% des Nettoeinkommens (Ziff. 20) = 2% x 80'000 = 1'600 (Code 238) -> Abzug Code 240 = CHF 2'900. Bund: Selbstbehalt 5% (Art. 33 Abs. 1 lit. h DBG; Merkblatt 32) = 4'000 -> Abzug CHF 500. Das SG-Formular hat nur eine Spalte; die Abweichung für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor.

**Antwort des Agenten** (24.9 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert):

> **Deklaration (SG 2025):** Ziff. 21.1 «Krankheits- und Unfallkosten». Die Arzt- und Zahnarztrechnungen gehen mit dem Bruttobetrag ins Hilfsblatt Krankheitskosten (Formular 6, Rückseite). Die Vorkolonne (Code 650) enthält den Nettobetrag nach Abzug der Krankenkassenvergütung, der Abzug kommt in Code 240. Die Krankenkassenprämien gehören nicht hierher, sondern in Ziff. 14. Im Formular gibt es nur eine Spalte für den Bund, die Abweichungen nimmt die Steuerbehörde automatisch vor.
> 
> **Berechnung**
> 
> | | Kanton SG / Gemeinde | Bund |
> |---|---|---|
> | Arzt-/Zahnarztkosten brutto | 6'200 | 6'200 |
> | ./. Krankenkassenvergütung | −1'700 | −1'700 |
> | Nettobetrag (Vorkolonne 650) | 4'500 | 4'500 |
> | Selbstbehalt | 2 % × 80'000 = −1'600 | 5 % × 80'000 = −4'000 |
> | **Abzug** | **2'900** (Code 240) | **500** |
> 
> - Kanton: Abzug = 4'500 − 2'000 … korrekt: 4'500 − 1'600 = **CHF 2'900**
> - Bund: Abzug = 4'500 − 4'000 = **CHF 500**
> 
> **Quellen und Status**
> - Kanton, 2 % Selbstbehalt: sg-stg-2025__art-46 (☑️ agent-geprüft, Abnahme offen); Formular: sg-form-1-2025__c0010 und sg-form-6-2025__c0003.
> - Bund, 5 % Selbstbehalt: bund-dbg-2025__art-33-t3 (☑️ agent-geprüft, Abnahme offen). Der Bund-Selbstbehalt bezieht sich nach Gesetz auf die um die Aufwendungen verminderten steuerbaren Einkünfte. Ich habe Ihre Annahme von CHF 80'000 übernommen, wie Sie es verlangt haben.
> 
> **Belege**
> - Arzt-/Zahnarztrechnungen: auf Verlangen vorzulegen, die Einzelrechnungen sind im Formular 6 aufzuführen.
> - Krankenkassen-Leistungsabrechnung: einzureichen, wenn im Formular 6 auf einen Kassenauszug bzw. das Total gemäss Zusammenzug verwiesen wird. In diesem Fall die Detailaufstellung mit Leistungsübersicht beilegen.
> 
> Offen bleibt die Abnahme der Fundstellen; die fachliche Beurteilung liegt bei der Fachperson.

## p05

**Frage:** SG 2025: Mandant gewinnt im Swiss Lotto (interkantonal durchgeführte Lotterie = Grossspiel) einen Einzelgewinn von CHF 1'500'000. Wo wird der Gewinn deklariert, welcher Teil ist steuerbar und welche Einsatzkosten sind abziehbar – Kanton und Bund getrennt?

**Soll (Referenz):** Deklaration im Wertschriften- und Guthabenverzeichnis (Formular 2), Spalte A (Bargewinn aus inländischer Lotterie, verrechnungssteuerpflichtig); Übertrag Ziff. 4.1 (Code 146). Kanton SG: Einzelgewinne aus Grossspielen steuerbar, soweit > Fr. 1'069'800 -> 1'500'000 - 1'069'800 = CHF 430'200 steuerbar; Einsatzkosten unter Ziff. 16.1 (Code 220): 5%, höchstens Fr. 5'400 -> CHF 5'400; netto CHF 424'800. Bund: steuerfrei bis CHF 1'070'400 (Art. 24 lit. ibis DBG) -> steuerbar CHF 429'600; Einsatzkosten 5%, höchstens CHF 5'400 (Art. 33 Abs. 4 DBG) -> CHF 5'400; netto CHF 424'200. (Der Höchstbetrag 5'400 greift unabhängig davon, ob 5% vom Gesamt- oder vom steuerbaren Gewinn gerechnet werden.)

**Antwort des Agenten** (43.1 s · Tools: 11 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__position, steuerwiki__zeige):

> **Ergebnis SG 2025 / Bund 2025: Gewinn CHF 1'500'000 aus Swiss Lotto (Grossspiel)**
> 
> | | Kanton SG (Staats- und Gemeindesteuer) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | Steuerfrei bis | CHF 1'069'800 | CHF 1'070'400 |
> | Steuerbarer Gewinn | CHF 430'200 | CHF 429'600 |
> | Einsatzkosten (5 %, max.) | CHF 5'400 (5 % von 430'200 = 21'510, gedeckelt) | CHF 5'400 (5 % von 429'600 = 21'480, gedeckelt) |
> | Abzug netto zusätzlich | Einsatzkosten als Abzug, neben Verwaltungskosten | Einsatzkosten als Abzug, Art. 33 Abs. 4 DBG |
> 
> **Kanton SG**
> - **Steuerfreiheit:** Einzelgewinne aus Grossspielen nach dem Geldspielgesetz sind bis CHF 1'069'800 steuerfrei (Art. 37 lit. o StG SG, `sg-stg-2025__art-37-t3`). Den Betrag über CHF 1'069'800 (CHF 430'200) versteuern Sie als Einkommen.
> - **Deklaration:** Ziff. 4.1 Formular 1 (Code 146) «Einkünfte aus Wertschriften und Guthaben inkl. Lotterie-/Geldspielgewinne», Übertrag aus Formular 2 (Abschnitt j Geldspielgewinne, `sg-wl-2025__c0134`). Gewinnbescheinigung (Lotto) als Beilage einreichen.
> - **Einsatzkosten:** Ziff. 16.1 (Code 220). 5 % des steuerbaren Gewinns, höchstens CHF 5'400. Sie sind zusätzlich zu den Verwaltungskosten abziehbar. Der Gewinn selbst (CHF 1'500'000) ist kein Abzug.
> - **Ergebnis:** Die CHF 5'400 mindern das steuerbare Einkommen. Die Basis für die Rechnung ist also CHF 430'200 − CHF 5'400 = CHF 424'800 (vor weiteren Abzügen).
> 
> **Bund**
> - **Steuerfreiheit:** Einzelne Gewinne aus Grossspielen sind bis CHF 1'070'400 steuerfrei (Art. 24 lit. ibis DBG, `bund-dbg-2025__art-24-t3`). Steuerbar sind CHF 429'600.
> - **Deklaration:** Das Formular SG 2025 hat nur eine Spalte. Die Bundesabweichungen (Freibetrag 1'070'400 statt 1'069'800) nimmt die Steuerbehörde automatisch vor (Merkblatt 32, `sg-wl-2025__c0173`). Sie müssen den Bund also nicht separat eintragen.
> - **Einsatzkosten:** 5 % des nicht steuerfreien Gewinns, höchstens CHF 5'400 (RS 2-211, Beilage 1 VKP Art. 3 Abs. 6, `bund-rs-2-211__c0017`).
> 
> **Hinweise**
> - Die Freibeträge gelten für das Steuerjahr 2025. Für 2026 steigt der Kantonsbetrag laut Wiki; das ist hier nicht relevant.
> - Die Schwellen unterscheiden sich um CHF 600 zwischen Kanton und Bund. Die Gewinn-Beträge deshalb nicht gleichsetzen.
> - Kanton-Werte (Freibetrag, Einsatzkosten-Satz) sind agent-geprüft (☑️). Die Abnahme durch eine Fachperson steht noch aus.
> - Nicht geprüft: ob bei der Auszahlung Verrechnungssteuer abgezogen wurde. Das Formular verlangt die Lotto-Bescheinigung in Spalte A, wenn VSt abgezogen wurde; prüfen Sie das auf der Bescheinigung.
> - Annahme: Der Gewinn ist im Steuerjahr 2025 zugeflossen und der Wohnsitz war am 31.12.2025 im Kanton SG.

## p06

**Frage:** SG 2025: Ehepaar mit zwei Kindern, für deren Unterhalt es zur Hauptsache aufkommt: Kind A ist 2-jährig (noch nicht schulpflichtig), Kind B ist 20 und studiert. Für Kind B selbst getragene Ausbildungskosten (Semestergebühren, Bücher, ÖV zum Studienort) CHF 9'500, erhaltenes Stipendium CHF 1'000. Welche Ziffern/Codes und welche Beträge – Kanton und Bund?

**Soll (Referenz):** Kanton SG (Steuererklärung Seite 3, Ziff. 23): Kind A -> Ziff. 23.1 (Code 252) Fr. 7'600; Kind B -> Ziff. 23.2 (Code 254) Fr. 10'800; Ausbildungskosten Kind B -> Ziff. 23.3 (Code 256, Formular 10): 9'500 - 1'000 Stipendium - 3'200 Selbstbehalt = CHF 5'300 (unter dem Maximum von Fr. 13'700). Total Kinderabzüge Kanton CHF 23'700. Bund: einheitlicher Kinderabzug CHF 6'800 pro Kind (Art. 35 Abs. 1 lit. a DBG), kein Abzug für Ausbildungskosten -> 2 x 6'800 = CHF 13'600 (Anpassung durch die Steuerbehörde, Merkblatt 32).

**Antwort des Agenten** (32.0 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__suche):

> **Ergebnis SG 2025 (Ehepaar, Kind A 2 J., Kind B 20 J. in Ausbildung, Hauptsache Unterhalt durch Sie)**
> 
> **Kanton St. Gallen** (Formular 1, Ziff. 23 Sozialabzüge)
> 
> | Ziff. | Code | Position | Berechnung | Betrag |
> |---|---|---|---|---|
> | 23.1 | 252 | Kinderabzug noch nicht schulpflichtiges Kind (Kind A) | 1 × 7'600 | 7'600 |
> | 23.2 | 254 | Kinderabzug Kind in Ausbildung (Kind B) | 1 × 10'800 | 10'800 |
> | 23.3 | 256 | Ausbildungskosten Kind B | 9'500 − Stipendium 1'000 − Selbstbehalt 3'200 = 5'300 (Limite 13'700 nicht erreicht) | 5'300 |
> 
> Kanton total aus Ziff. 23: **Fr. 23'700**.
> 
> **Bund (direkte Bundessteuer)**
> 
> Das Formular hat keine separate Bundesspalte; die Steuerbehörde nimmt die Bundesabweichungen automatisch vor (Merkblatt 32).
> 
> - Ziff. 23.1 (Kind A): Bund Fr. 6'800 als Abzug vom Einkommen.
> - Ziff. 23.2 (Kind B): Bund Fr. 6'800 als Abzug vom Einkommen.
> - Ziff. 23.3 (Ausbildungskosten): **kein Bundesabzug**. Die 9'500 CHF und das Stipendium gehen nur in den Kantonsabzug.
> - Steuerbetrag-Abzug: Ziff. 23.1 und 23.2 nennen je Kind max. Fr. 263 Abzug vom Steuerbetrag (Bund). Das ergibt bei zwei Kindern höchstens 526. Ob der Betrag für Kind B ebenfalls gilt, ist im Wiki nicht eindeutig belegt; ich habe es nicht abschliessend geprüft.
> 
> Bund total: Einkommensabzug **Fr. 13'600**, plus Steuerbetragsabzug bis **Fr. 526** (Kind B noch offen, s. oben).
> 
> **Hinweise**
> - Die Ausbildungskosten des Kindes gehören nicht in Ziff. 16.4 (das ist für die eigenen Kosten der steuerpflichtigen Person). Belege (Semestergebühren, Bücher, ÖV-Abo, Stipendienverfügung) sind im Formular 10 bzw. auf Verlangen einzureichen.
> - Ziff. 23.3 gilt nur, wenn für das Kind ein Abzug nach 23.2 gewährt wird. Hier ist das der Fall.
> - Status der Fundstellen: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Quellen: sg-form-1-2025__c0011, sg-wl-2025__c0104/c0105, sg-form-32-2025__c0006.

## p07

**Frage:** TG 2025: Arbeitnehmer fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 22 km einfach, Hin- und Rückfahrt täglich, 225 Arbeitstage, keine weiteren Fahrkosten, kein Geschäftsfahrzeug. Wie wird Formular 4.2 Ziff. 2.3–2.5 für Staats- und Bundessteuer ausgefüllt und was geht in die Steuererklärung?

**Soll (Referenz):** Formular 4.2 Ziff. 2.3: 44 km/Tag x 225 Tage = 9'900 km pro Jahr (Code 211). Staatssteuer, Auto-Ansätze nach Jahreskilometern gestaffelt: 3'000 km x 0.60 = 1'800; 2'000 km x 0.50 = 1'000; 4'900 km x 0.40 = 1'960 -> CHF 4'760. Bundessteuer einheitlich CHF 0.70/km: 9'900 x 0.70 = CHF 6'930. Ziff. 2.4 Total effektive Fahrkosten (Code 212): Staat 4'760 / Bund 6'930. Ziff. 2.5 Total abzugsfähige Fahrkosten (Code 213): Staat max. 6'000 -> CHF 4'760; Bund max. 3'300 -> CHF 3'300. Über Ziff. 7 Total Berufsauslagen (Code 240) in Steuererklärung Seite 3, Ziff. 10.1 (linke Spalte Staat, rechte Spalte Bund).

**Antwort des Agenten** (30.0 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert):

> **TG 2025, Form. 4.2 Ziff. 2.3–2.5 (Person 1, Staat und Bund getrennt)**
> 
> **Berechnung**
> 
> - Km pro Jahr: 22 km × 2 = 44 km/Tag × 225 Tage = **9'900 km**
> - Ziff. 2.1 und 2.2 bleiben leer, weil keine weiteren Fahrkosten anfallen.
> 
> | Ziffer | Inhalt | Staat (TG) | Bund |
> |---|---|---|---|
> | 2.3 | Privatauto, km × Tage | 1'800 + 1'000 + 1'960 = **4'760** | 9'900 × 0.70 = **6'930** |
> | 2.4 | Total effektive Fahrkosten (2.1–2.3) | **4'760** | **6'930** |
> | 2.5 | Abzugsfähig, Maximum | min(4'760; 6'000) = **4'760** | min(6'930; 3'300) = **3'300** |
> 
> - **Kanton:** Der Ansatz ist gestaffelt: 3'000 km × 0.60, 2'000 km × 0.50, Rest (4'900 km) × 0.40. Das Maximum von Fr. 6'000 wird nicht erreicht.
> - **Bund:** Einheitlich Fr. 0.70/km. Der Bundeshöchstbetrag von Fr. 3'300 greift, daher kürzt er auf 3'300.
> 
> **Was in die Steuererklärung geht**
> 
> - Ziff. 2.5 wird als Übertrag in Form. 4.2 Ziff. 7 (Code 240) übernommen. Danach folgt Steuererklärung Seite 3 Ziff. 10.1: **Staat links 4'760, Bund rechts 3'300.**
> - Die Position gilt nur für Person 1. Person 2 hätte eigene Codes (252/253, Form. 4.3).
> 
> **Voraussetzung und Belege**
> 
> - Der Abzug gilt nur, wenn der ÖV nicht zumutbar ist. Die Zeitersparnis von über 1 Stunde pro Arbeitstag ist in den Hinweisen der Wegleitung als Beispiel genannt. Sie sollten sie in den Unterlagen nachweisen können.
> - Bei Abzug des Privatautos entfällt der Abzug für ÖV-Abos.
> - Belege: Fahrzeugausweis (Fahrzeugart Auto), Distanzangabe Wohnadresse–Arbeitsort, Arbeitszeitangaben (225 Tage). Ob sie einzureichen sind, ist in der Quelle unklar (tg-wl-2025__c0179).
> 
> **Offene Punkte**
> 
> - Alle Werte sind im Wiki als «agent-geprüft» markiert; die Abnahme steht noch aus.
> - Ich habe die Bundes-Voraussetzung («Ausnahmefall») nicht separat in den Quellen belegt gefunden. Die Berechnung oben folgt der Kantonsregel, die für die Bundesspalte in der Wegleitung ebenfalls gilt. Ob der Bund die Begründung gleich streng prüft, habe ich nicht bestätigt.
> - Die Angabe von 225 Arbeitstagen stammt aus der Wegleitung-Kurzübersicht, nicht aus dem Gesetz.

## p08

**Frage:** TG 2025: Ehepaar bewohnt sein eigenes Einfamilienhaus am Wohnsitz selbst (Baujahr 1995, nicht landwirtschaftlich geschätzt, keine Mieteinnahmen). Indexierter Mietwert aus Selbstnutzung 2025 CHF 21'000; Unterhalt pauschal. Wie werden Eigenmietwert und Nettoerfolg im Formular 7 berechnet und wohin übertragen – Staat und Bund?

**Soll (Referenz):** Formular 7, Zeile «Mietwert selbstgenutzt» 21'000 (beide Spalten). Selbstnutzungsabzug: Staat 40% = 8'400, Bund 20% = 4'200 -> steuerbarer Eigenmietwert (= Bruttoertrag) Staat CHF 12'600, Bund CHF 16'800. Pauschalabzug Unterhalt: Gebäude älter als 10 Jahre -> 20%, berechnet vom steuerbaren Eigenmietwert: Staat 2'520, Bund 3'360. Nettoerfolg: Staat CHF 10'080, Bund CHF 13'440 (bei selbstgenutzter Liegenschaft je Spalte separat ermitteln). Total Nettoerfolge (Code 180) -> Steuererklärung Seite 2, Ziff. 8, Spalte Staat bzw. Bund.

**Antwort des Agenten** (46.7 s · Tools: 11 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__zeige, steuerwiki__suche):

> **Kurzantwort:** Für Kanton TG ergibt sich ein Nettoerfolg von **CHF 10'080**, für den Bund **CHF 13'440**. Der Bund-Selbstnutzungsabzug ist im Wiki widersprüchlich belegt (siehe unten), daher die Bundszahl vor dem Einreichen prüfen.
> 
> **Berechnung (Formular 7, Hilfsblatt Liegenschaften, Zeile je Liegenschaft)**
> 
> | Schritt | Staat/Gemeinde (Kanton) | Direkte Bundessteuer |
> |---|---|---|
> | Mietwert selbstgenutzt (indexiert 2025) | 21'000 | 21'000 |
> | Selbstnutzungsabzug | − 8'400 (40 %) | − 4'200 (20 %) |
> | Steuerbarer Eigenmietwert = Bruttoertrag (keine Mieten) | 12'600 | 16'800 |
> | Unterhalt pauschal: 20 % (Gebäude > 10 Jahre, Baujahr 1995) | − 2'520 | − 3'360 |
> | **Nettoerfolg** | **10'080** | **13'440** |
> 
> **Eintrag im Formular**
> - Formular 7: Am Wohnsitz selbstgenutzt = «ja», Mietwert 21'000, Selbstnutzungsabzug und Unterhalt «Pauschal» ankreuzen, Nettoerfolg je Spalte (links Staat, rechts Bund).
> - Die Summe der Nettoerfolge aus Formular 7 geht in **Ziff. 8.1 «Einkünfte aus Liegenschaften», Code 180**: links 10'080 (Staat/Gemeinde), rechts 13'440 (direkte Bundessteuer).
> - Der Steuerwert (amtlicher Verkehrswert, Ziff. 31, Code 430) ist eine separate Angabe und nicht Teil dieser Rechnung.
> 
> **Rechtsgrundlagen**
> - Kanton: § 23 Abs. 3 StG TG, 40 % Abzug auf den Mietwert bei am Wohnsitz selbstbewohntem Wohneigentum (Fundstelle tg-stg__par-23).
> - Pauschale: 20 % für Gebäude älter als 10 Jahre (tg-stv__par-9). Das Gebäudealter wird beim Kanton am Ende der Steuerperiode, beim Bund zu Beginn gemessen. Bei Baujahr 1995 ist beides über 10 Jahre.
> - Die Pauschale ist für selbstgenutzte Liegenschaften auf den steuerbaren Eigenmietwert zu berechnen (tg-wl-2025__c0238 und Formular-Regel).
> 
> **Offen: Bund-Selbstnutzungsabzug**
> - Die Wegleitung TG 2025 (tg-wl-2025__c0225) und die Formularposition nennen einen Bund-Abzug von 20 %. Die Rechnung oben folgt dieser Quelle.
> - Eine Wiki-Eckwertabfrage für Bund führt den Abzug dagegen als «nicht gesondert» auf (kein prozentualer Abzug auf den Eigenmietwert beim Bund). Die beiden Aussagen widersprechen sich. Ohne Bund-Abzug läge der Bund-Eigenmietwert bei 21'000 und der Bund-Nettoerfolg bei 17'640 (Pauschale 20 % auf 21'000 = 4'200). Ich habe diese Variante nicht als belegt übernommen.
> - Die Pauschale für den Bund ist im LKV Art. 5 auf den «Brutto-Mietertrag» bezogen. Ob dabei der Eigenmietwert nach Abzug oder der volle Mietwert gilt, ist im Wiki nicht eindeutig belegt. Ich habe den steuerbaren Eigenmietwert verwendet.
> 
> Bitte prüfen Sie den Bund-Abzug anhand der amtlichen Bundesunterlagen für 2025 oder fragen Sie die Steuerverwaltung TG. Die fachliche Beurteilung bleibt bei der Fachperson.

## p09

**Frage:** AR 2025: Ehepaar, beide unabhängig voneinander unselbständig erwerbstätig. Das niedrigere Erwerbseinkommen (Nettolohn der Ehefrau abzüglich Berufskosten, Säule-3a-Beiträge und BVG-Einkäufe) beträgt CHF 38'000. Wie hoch ist der Zweiverdienerabzug in Ziffer 17 für die Staats- und Gemeindesteuer und für die direkte Bundessteuer?

**Soll (Referenz):** Ziff. 17 Zweiverdienerabzug. Kanton AR: 10% des niedrigeren Erwerbseinkommens, mind. Fr. 2'500, max. Fr. 5'200 (Beträge gemäss Anhang 1 StG indexiert per 1.1.2024; Art. 35 Abs. 1 lit. h StG nennt die Basisbeträge 2'400/5'000) -> 10% x 38'000 = CHF 3'800. Bund: Art. 33 Abs. 2 DBG 50% des niedrigeren Erwerbseinkommens, mind. 8'600, max. 14'100 -> 50% x 38'000 = 19'000 -> begrenzt auf CHF 14'100. Die Abweichung für die direkte Bundessteuer wird von der Steuerverwaltung automatisch vorgenommen.

**Antwort des Agenten** (24.6 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert):

> **Ergebnis (AR 2025, Ehepaar, beide erwerbstätig, E = CHF 38'000):**
> 
> | Steuer | Satz | Rechnung | Abzug |
> |---|---|---|---|
> | Staats- und Gemeindesteuer (Kanton AR) | 10 % | 10 % × 38'000 = 3'800; im Rahmen von min. 2'500 / max. 5'200 | **CHF 3'800** |
> | Direkte Bundessteuer | 50 % | 50 % × 38'000 = 19'000; auf max. 14'100 begrenzt (min. 8'600) | **CHF 14'100** |
> 
> **Quellen:**
> - Kanton: `ar-stg__art-35-t3` (10 %, min./max.) und `ar-stg-anhang-kp__c0001` (Min. 2'500, Max. 5'200, indexiert per 1.1.2024). Position: `ar-wl-2025__c0004`.
> - Bund: `bund-dbg-2025__art-33-t6` (Art. 33 Abs. 2 DBG: 50 %, min. 8'600, max. 14'100).
> 
> **Hinweise:**
> - **Ziffer 17 ist nicht verifiziert.** Der Status im Wiki ist ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme steht aber aus. Die Nummer 17 stammt aus der Wegleitung; die Seite 3 des Formulars ist dort nicht als Miniatur abgebildet. Bitte vor dem Ausfüllen gegen das Originalformular prüfen.
> - **Kein separates Bundesfeld im AR-Formular.** Laut Wegleitung (`ar-wl-2025__c0179`) nimmt die Steuerverwaltung die Abweichungen für den Bund automatisch vor. Der Bundesabzug von 14'100 ist daher nach meiner Lesart nicht in Ziffer 17 einzutragen, sondern wird von der Verwaltung berechnet. Das sollte bei der Abnahme bestätigt werden.
> - Der Betrag E muss bereits nach Berufskosten, Säule-3a und BVG-Einkäufen ermittelt sein, wie in der Angabe vorgegeben.

## p10

**Frage:** AR 2025: Mandant bewohnt sein Einfamilienhaus am Wohnsitz dauernd selbst (Baujahr 1995, einzige Liegenschaft, keine Fremdvermietung). Mietwert gemäss Grundstückschätzung CHF 24'500; er wählt den Pauschalabzug für den Unterhalt. Was wird wo im Formular 7 und in der Steuererklärung (Staats- und Gemeindesteuer) eingetragen?

**Soll (Referenz):** Formular 7, Teil B.a: Eigenmietwert 24'500 abzüglich Selbstnutzungsabzug 20% (4'900) = Total anrechenbarer Eigenmietwert CHF 19'600 = Total Erträge a. und b. -> Übertrag Steuererklärung Seite 2, Ziff. 5. Teil C: Pauschalabzug (Gebäude über 10 Jahre; Bruttomietertrag des gesamten Liegenschaftsbesitzes nicht über Fr. 100'000) = 20% vom Total Liegenschaftserträge = 20% x 19'600 = CHF 3'920 -> Übertrag Steuererklärung Seite 3, Ziff. 15 (separater Abzug, nicht mit Ziff. 5 verrechnet). Wirkung auf das Einkommen netto CHF 15'680.

**Antwort des Agenten** (36.1 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert):

> **Ergebnis (AR 2025, Staats- und Gemeindesteuer):** Der Eigenmietwert wird um 20 % Selbstnutzungsabzug gekürzt, der Pauschalabzug beträgt 20 % auf dem Eigenmietwert nach Abzug, und für den Bund ist keine zusätzliche Eingabe nötig.
> 
> **Ausgangslage:** Mietwert CHF 24'500, Baujahr 1995, Selbstnutzung am Wohnsitz.
> 
> | Position | Betrag | Eintrag | Quelle / Status |
> |---|---|---|---|
> | Form. 7 Abschn. A: Steuerwert (Verkehrswert gemäss Grundstückschätzung) | gemäss Schätzung (Betrag nicht angegeben) | Ziff. 31, Seite 4 (Code 710) | ar-form-07-2025__c0001 · ☑️ |
> | Form. 7 Abschn. B a: Mietwert 24'500 − 20 % (4'900) | **CHF 19'600** | Ziff. 5, Seite 2 (Code 712) | ar-form-07-2025__c0002 · ☑️ · Limite 20 % (`liegenschaft.eigenmietwert_abzug`) |
> | Form. 7 Abschn. C1: Pauschale 20 % auf 19'600 | **CHF 3'920** | Ziff. 15, Seite 3 | ar-form-07-2025__c0003 · ☑️ · Limite `liegenschaft.pauschale_alt` = 20 % |
> 
> **Begründung:**
> - **Eigenmietwert:** Der 20 %-Abzug gilt nur für die dauernd selbst bewohnte Wohnsitzliegenschaft. Das trifft zu.
> - **Pauschale 20 %:** Gebäude älter als 10 Jahre (1995). Die Pauschale ist zulässig, weil der Bruttomietertrag des gesamten Besitzes CHF 100'000 nicht übersteigt und die Liegenschaft Wohnzwecken dient. Er ist also keine Einzelbetragsrechnung nötig.
> - **Bemessungsgrundlage Kanton:** Laut Beachten-Feld gilt für den Kanton der **netto** Eigenmietwert (nach 20 %-Abzug), also 19'600.
> - **Bund:** Der AR-Formular hat keine Bundesspalte. Die Steuerverwaltung nimmt die Abweichungen für die direkte Bundessteuer automatisch vor (ar-wl-2025__c0179). Laut Bund-Quelle (bund-lkv art. 5) ist die Pauschale beim Bund 20 % des **Brutto**-Mietertrags, also 4'900 statt 3'920. Der Eigenmietwert wird beim Bund ohne prozentualen Abzug angesetzt, also 24'500.
> 
> **Offene Punkte zur Abnahme:**
> 1. **Bemessungsgrundlage der Pauschale:** Die Wiki-Quellen widersprechen sich leicht. Der Wortlaut zu Ziff. 15 nennt „Liegenschaftserträge (Ziff. B)“, das Beachten-Feld nennt für den Kanton netto und für den Bund brutto. Bitte gegen die Wegleitung AR 2025 (ar-wl-2025__c0175) prüfen, bevor die 3'920 eingetragen werden.
> 2. **Code Ziff. 15** ist laut Wiki nicht verifiziert, weil Seite 3 in der Wegleitung nicht als Miniatur abgebildet ist.
> 3. **Bund** ist im Wiki nur als „agent-geprüft“ markiert, und für den Eigenmietwert steht ausdrücklich „nicht aus AR-Quellen belegt“.
> 
> **Belege:** Für Eigenmietwert und Steuerwert genügt die Grundstückschätzung, und sie ist nur auf Verlangen einzureichen. Für die Pauschale braucht es keine Rechnungen. Diese wären nur bei Abzug der tatsächlichen Kosten (C2) nötig.

