# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 40 · Lauf: 2026-11-09 17:23
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q01

**Frage:** Mandantin (ZH, 2025) bringt: Lohnausweis, Krankenkassen-Prämienrechnung, Handyrechnung, 3a-Bescheinigung, Hausratversicherungspolice, Spendenquittung Rotes Kreuz CHF 80, Kita-Rechnungen. Welche sind relevant, wofür?

**Soll (Referenz):** Relevant: Lohnausweis (Einkünfte 1.1), Krankenkassenprämien (Versicherungsabzug Ziff. 15, Form. 365), 3a-Bescheinigung (Ziff. 14), Kita-Rechnungen (Ziff. 16.6 Drittbetreuung, max. 25'000 Kanton / 25'800 Bund). Spende CHF 80: unter Mindestbetrag 100 → nicht abziehbar (sofern Total < 100). Nicht relevant: Handyrechnung (Lebenshaltung), Hausratversicherung (kein Versicherungsabzug).

**Antwort des Agenten** (45.5 s · Tools: 13 Aufrufe read, steuerwiki__ablage, steuerwiki__beleg, steuerwiki__suche):

> Von den 7 Unterlagen sind 4 sicher relevant (Lohnausweis, Prämienrechnung, 3a, Kita), 1 (Spende) ist es mit CHF 80 allein nicht, und 2 sind es nicht (Handy, Hausrat). Alles gilt für ZH, Steuerjahr 2025, Status je ☑️ agent-geprüft (Abnahme offen).
> 
> | Dokument | Wofür (ZH 2025) | Einreichen | Kategorie (KATEGORIEN.md) |
> |---|---|---|---|
> | **Lohnausweis** | Einkünfte, Ziff. 1.1 und Form. 360 (Berufsauslagen). Fundstelle: zh-wl-2025__c0032 | Ja, immer | **Belege eingereicht**. Die Liste nennt ihn ausdrücklich. |
> | **3a-Bescheinigung** | Abzug Säule 3a, Ziff. 14.1/14.2. Fundstelle: zh-wl-2025__c0081 | Ja | **Belege eingereicht**. Die Liste nennt sie ausdrücklich. |
> | **Krankenkassen-Prämienrechnung** | Versicherungsabzug, Ziff. 15 und Form. 365 Teil A. Die Prämien sind nach Abzug der Prämienverbilligung (IPV) einzutragen. Fundstelle: zh-wl-2025__c0207 | Auf Verlangen. Das Formular Versicherungsprämien liegt bei, die Prämienbelege selbst nicht. | **Belege Sonstiges** (Versicherungsprämien, sofern nicht einzureichen) |
> | **Kita-Rechnungen** | Fremdbetreuung, Ziff. 16.6 (Code 376). Fundstelle: zh-stg-2025__par-31-t4 | Auf Verlangen. Die Aufstellung der Kosten mit Empfängern liegt unaufgefordert bei, die Rechnungen nur auf Nachfrage. | **Belege Sonstiges** (Kinderbetreuungskosten, sofern nicht einzureichen) |
> | **Spendenquittung Rotes Kreuz CHF 80** | Ziff. 22.2, Code 324. Fundstelle: zh-info-spenden__c0003 | Auf Verlangen | siehe unten |
> | **Hausratversicherung (Police)** | Kein Wert in der Steuererklärung | – | Keine Steuerbeleg-Kategorie |
> | **Handyrechnung** | Kein Wert in der Steuererklärung | – | Keine Steuerbeleg-Kategorie |
> 
> **Was bei den einzelnen Dokumenten zu beachten ist**
> - **Kita:** Der Abzug gilt nur für Kinder unter 14 im gleichen Haushalt, wenn die Betreuung wegen Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit nötig ist.
>   - Verpflegung ist nicht abziehbar und Subventionen oder Betreuungsgutscheine sind abzuziehen.
>   - Die Obergrenze liegt je Kind bei CHF 25'000 für den Kanton und CHF 25'800 für den Bund.
>   - Ob die Voraussetzungen erfüllt sind (Alter, Erwerbstätigkeit), geht aus den Unterlagen nicht hervor und ist zu klären.
> - **Spende:** Der Abzug gilt erst ab CHF 100 Gesamtspenden pro Jahr (Kanton und Bund). Mit nur CHF 80 gibt es keinen Abzug.
>   - Hat die Mandantin weitere Spenden an steuerbefreite Organisationen in der Schweiz, zählt das Total aller Spenden. Bei mindestens CHF 100 kommt die Quittung unter **Belege Sonstiges**, und die Ziff. 22.2 braucht eine Liste aller Spenden.
>   - Bei insgesamt unter CHF 100 gibt es keinen Wert in der Erklärung und damit keine Steuerbeleg-Kategorie.
> - **Hausrat:** Mobiliar- und Haftpflichtprämien sind nicht abziehbar. Die Fundstelle (ar-wl-2025__c0085) stammt aus AR. Für ZH ist es im Wiki nicht einzeln belegt, es folgt aber aus dem allgemeinen Prinzip, dass Sachversicherungen nicht zählen.
> - **Handy:** Das Wiki erkennt diesen Dokumenttyp nicht, und die Handyrechnung ist wohl eine private Alltagsrechnung. Private Lebenshaltungskosten sind nicht abziehbar (Art. 34 lit. a DBG).
>   - Berufliche Nutzung ist über die Pauschale «übrige Berufskosten» (3 % des Nettolohns, mindestens CHF 2'000, höchstens CHF 4'000) abgedeckt, nicht separat.
>   - Ob die Mandantin effektive Berufskosten geltend machen will, ist offen. Dann bräuchte es eine Aufstellung auf Form. 360, und das liesse sich prüfen.
> 
> **Vorbehalt:** Die Zuordnungen der Liste sind laut KATEGORIEN.md noch nicht bestätigt. Die Einordnung stützt sich auf die Dokumentarten, nicht auf den Inhalt der Dokumente selbst.
> 
> Als Nächstes kann ich mit `steuererklaerung-np` die konkreten Werte je Position erfassen, sobald du die Beträge hast.

## q02

**Frage:** In welche Ziffer und mit welchem Code der ZH-Steuererklärung 2025 gehört der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb)?

**Soll (Referenz):** Ziff. 1.1 Haupterwerb, Code 100 (Person 1) / 101 (Person 2); Nettolohn Lohnausweis Ziff. 11 (zh-form-300-2025).

**Antwort des Agenten** (23.1 s · Tools: 2 Aufrufe steuerwiki__beleg, steuerwiki__position):

> Der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb) gehört in **Ziff. 1.1 «Haupterwerb unselbständig» mit Code 100**. Person 2 hat Code 101.
> 
> - **Betrag:** Eingesetzt wird Ziff. 11 des Lohnausweises. Das ist Bruttolohn (Ziff. 8) minus Abzüge für AHV/IV/EO/ALV/NBUV (Ziff. 9) minus BVG-Beiträge (Ziff. 10.1 und 10.2). Bei mehreren Haupterwerben von Person 1 wird die Summe der Ziff. 11 aller Lohnausweise eingetragen.
> - **Bund:** Es ist dieselbe Zeile für Staats- und Bundessteuer, also kein abweichender Betrag.
> - **Einreichen:** Der Lohnausweis muss der Steuererklärung beigelegt werden, für jeden Arbeitgeber (§ 134 Abs. 1 lit. a StG; zh-wl-2025__c0032).
> - **BVG-Einkauf:** Ein Einkauf, der im Lohnausweis unter Ziff. 10.2 steht, ist im Nettolohn schon abgezogen. Er darf nicht nochmals unter Ziff. 16.1 (Code 280) abgezogen werden.
> - **Berufskosten:** Dieselbe Ziff. 11 dient als Basis für die pauschalen übrigen Berufskosten (Form. 360 Ziff. 3, Code 212, 3 %, mind. CHF 2'000, max. CHF 4'000).
> 
> Status ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme steht aus. Quelle: zh-form-300-2025__c0004 («Haupterwerb Person 1 Lohnausweis»).
> 
> Übrigens: Ich bin hier neu eingerichtet. Wie möchtest du mich nennen?

## q03

**Frage:** Lohnausweis Feld F ist angekreuzt (Geschäftsauto). Was bedeutet das für den Fahrkostenabzug (SG 2025)?

**Soll (Referenz):** Feld F angekreuzt → kein Fahrkostenabzug für den Arbeitsweg mit Geschäftsfahrzeug (Privatanteil im Lohn, Lohnausweis Ziff. 2.2).

**Antwort des Agenten** (27.1 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__beleg):

> **Kurz: Bei angekreuztem Feld F gibt es für SG 2025 keinen Fahrkostenabzug für den Arbeitsweg (Formular 4 Ziff. 1).**
> 
> **Begründung**
> - Feld F bedeutet, dass der Arbeitgeber die Beförderung zwischen Wohn- und Arbeitsort unentgeltlich stellt. Das gilt für Sammeltransporte, ein GA aus geschäftlichen Gründen oder ein Geschäftsfahrzeug. Dem Arbeitnehmer entstehen dann keine Kosten, die er abziehen könnte (sg-wl-2025__c0075: «Ein Abzug für die Fahrt zur Arbeit ist deshalb nicht möglich»).
> - Bei einem Geschäftsauto steht auf dem Lohnausweis meist zusätzlich ein Privatanteil (Ziff. 2.2, 0,9 % pro Monat bzw. 10,8 % pro Jahr). Dieser wird als Einkommen versteuert, ersetzt aber den Fahrkostenabzug nicht, sondern schliesst ihn aus (sg-form-4-2025__c0002).
> - Das gilt für den Kanton und für den Bund. Das SG-Formular hat nur eine Spalte, die Steuerbehörde nimmt die Bundesanpassungen automatisch vor (sg-wl-2025__c0173).
> 
> **Was Sie eintragen**
> - Form. 4 Ziff. 1.1 bis 1.3 (Codes 400 bis 406 bzw. 450 bis 456): leer lassen.
> - Die Maximalabzüge (Kanton Fr. 8'000, Bund Fr. 3'300) kommen nicht zur Anwendung.
> 
> **Ausnahmen und Punkte zu prüfen**
> 1. **Geschäftsauto mit Bordbuch:** Wird nach Bordbuch effektiv abgerechnet statt mit der Privatanteil-Pauschale, sind die effektiven Arbeitswegkosten bis zum Maximalabzug abziehbar (Form. 4 Ziff. 1.3). Dazu braucht es ein Bordbuch und die Angabe auf dem Lohnausweis.
> 2. **GA ohne geschäftliche Notwendigkeit:** Dann dürfte Feld F nicht angekreuzt sein. Der Vorteil gehört in den Lohn, und die Kosten eines Streckenabos wären in Form. 4 abziehbar. Hier lohnt sich eine Rückfrage beim Arbeitgeber, falls das Kreuz fraglich ist.
> 3. **Fahrkostenentschädigung im Bruttolohn (Ziff. 2.3):** Dann ist Feld F nicht angekreuzt, und der Abzug ist bis zum Maximum möglich. Beides zusammen wäre widersprüchlich.
> 4. **Andere Abzüge:** Feld F betrifft nur den Arbeitsweg. Verpflegung (Feld G) und andere Berufskosten sind getrennt zu prüfen.
> 
> **Quellen und Status**
> - Alle Angaben sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> - Zusätzlich: sg-stb-39-3__c0013.
> - Das Lohnausweis-Merkblatt im Wiki (bund-wl-lohnausweis-2026) gilt nur für 2026. Die Regel oben stützt sich auf die SG-Wegleitung 2025.
> - Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Falls ein Bordbuch geführt wird, kann ich die Berechnung nach Ziff. 1.3 durchrechnen (0.70 Fr./km, max. 220 Tage).

## q04

**Frage:** Wie hoch ist der maximale Fahrkostenabzug 2025 in TG (Staatssteuer) und beim Bund, und welcher km-Ansatz gilt für das Auto?

**Soll (Referenz):** TG 2025 Staat max. CHF 6'000 (tg-stg__par-29), Bund max. CHF 3'300 (bund-dbg-2025__art-26); Auto TG gestaffelt 0.60/0.50/0.40 je nach Jahres-km, Bund 0.70.

**Antwort des Agenten** (24.3 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Fahrkostenabzug 2025: TG (Staatssteuer) und Bund**
> 
> | | Thurgau (Staatssteuer) | Bund (dBSt) |
> |---|---|---|
> | **Maximalabzug Wohn-/Arbeitsstätte** | **CHF 6'000** pro Jahr | **CHF 3'300** pro Jahr |
> | **Auto, Ansatz pro km** | gestaffelt, siehe unten | **CHF 0.70/km** |
> 
> Beide Höchstbeträge gelten für alle Fahrkosten zusammen. Im TG-Formular stehen sie unter Ziff. 10.1 (Person 1) und 10.2 (Person 2). Der Bund wird in derselben Erklärung erfasst, es gibt kein eigenes Formular.
> 
> **Auto in TG (Privatauto)**
> - Das Privatauto ist nur in Ausnahmefällen abziehbar, nämlich wenn der öffentliche Verkehr nicht zumutbar ist. Im Normalfall zählen die Kosten des ÖV-Abos.
> - Die Staffelung nach Jahres-km wird stufenweise berechnet und deckt auch die Parkgebühren ab:
>   - bis 3'000 km: CHF 0.60/km
>   - 3'001 bis 5'000 km: CHF 0.50/km
>   - über 5'000 km: CHF 0.40/km
> - Beispiel: 8'000 km ergeben CHF 4'000 (1'800 + 1'000 + 1'200).
> - Bei 100 % Pensum rechnet man in der Regel mit maximal 225 Arbeitstagen.
> 
> **Auto beim Bund**
> - Der Satz von CHF 0.70/km gilt ebenfalls nur, wenn kein öffentliches Verkehrsmittel verfügbar oder zumutbar ist.
> - Ab Steuerjahr 2026 steigt er auf CHF 0.75/km. Für 2025 gilt er nicht.
> - Eine Arbeitstage-Regel gibt es beim Bund nicht.
> 
> **Widerspruch bei den Bundes-Maxima:** DBG Art. 26 Abs. 1 lit. a (Fassung 2025) nennt CHF 3'300. Die ESTV-Wegleitung 2a 2025 (S. 6) nennt noch CHF 3'200. Ich habe das Gesetz verwendet, weil es der Wegleitung vorgeht; die Wegleitung scheint nicht nachgeführt zu sein.
> 
> **Fundstellen (Status ☑️ agent-geprüft, Abnahme offen):**
> - TG Maximum: `tg-stg__par-29`
> - TG km-Staffel: `tg-bkv__par-1`
> - Bund Maximum: `bund-dbg-2025__art-26`
> - Bund km-Satz: `bund-bkv-2025__anhang-1`
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Nebenbei: Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## q05

**Frage:** Welcher km-Ansatz für Autos gilt 2026 bei der direkten Bundessteuer?

**Soll (Referenz):** CHF 0.75 pro km (bund-mm-2025-09-11-kalte-progression-2026__c0004; RS 2-215).

**Antwort des Agenten** (21.4 s · Tools: 1 Aufrufe steuerwiki__wert):

> Bei der direkten Bundessteuer gelten 2026 **CHF 0.75 pro Fahrkilometer** für das Privatauto (☑️ agent-geprüft, Abnahme offen).
> 
> - **Voraussetzung:** Der Ansatz gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist.
> - **Neu ab 2026:** Bisher waren es CHF 0.70. Der Ansatz ist künftig an den TCS-Kilometerpreis gekoppelt und kann nach oben oder unten angepasst werden.
> - **Gesamtmaximum:** Die Fahrkosten zwischen Wohn- und Arbeitsstätte sind auf CHF 3'300 pro Jahr begrenzt (Art. 26 Abs. 1 lit. a DBG, Chunk `bund-dbg-2026__art-26`). Dieser Betrag ist gleich hoch wie 2025.
> - **Andere Fahrzeuge:** Motorrad mit weissem Kontrollschild CHF 0.40 pro km. Velo, Motorfahrrad und Motorrad mit gelbem Kontrollschild CHF 700 pro Jahr als Pauschale.
> 
> Quelle für den Ansatz: `bund-mm-2025-09-11-kalte-progression-2026__c0004`: «Der Abzug wird auf 75 Rappen pro Kilometer erhöht (bisher 70 Rappen).»
> 
> Die kantonalen Ansätze für die Staats- und Gemeindesteuer können abweichen. Wenn du einen Kanton (AR, SG, TG oder ZH) nennst, prüfe ich ihn separat.

## q06

**Frage:** Maximaler Säule-3a-Abzug 2025 für eine Arbeitnehmerin mit Pensionskasse? Und für eine Selbständige ohne 2. Säule?

**Soll (Referenz):** Mit 2. Säule CHF 7'258; ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288 (bund-bsv-masszahlen-2025-2026__c0003).

**Antwort des Agenten** (23.4 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Säule 3a, Steuerjahr 2025.** Die Höchstbeträge gelten für die direkte Bundessteuer. Ein Kanton hast du nicht genannt. Die Beträge stammen aus Bundesrecht (BVV 3), und die Kantone wenden sie in der Regel gleich an. Nicht geprüft habe ich, ob ein Kanton davon abweicht. Nenn mir den Wohnsitzkanton (AR, SG, TG oder ZH), dann prüfe ich das.
> 
> | Situation | Maximaler Abzug 2025 | Status |
> |---|---|---|
> | Arbeitnehmerin mit Pensionskasse (2. Säule) | **CHF 7'258** | ☑️ agent-geprüft |
> | Selbständige ohne 2. Säule | **20 % des Erwerbseinkommens, höchstens CHF 36'288** | ☑️ agent-geprüft |
> 
> - **Mit Pensionskasse:** CHF 7'258 entspricht 8 % des oberen BVG-Grenzbetrags. Quelle: `bund-bsv-masszahlen-2025-2026__c0003`.
> - **Ohne 2. Säule:** Es gilt der tiefere der beiden Beträge. Der Höchstbetrag von CHF 36'288 wird erst ab einem Erwerbseinkommen von CHF 181'440 erreicht (36'288 ÷ 20 %). Das Erwerbseinkommen ist der Nettoerwerb aus der selbständigen Tätigkeit. Quellen: `bund-bsv-masszahlen-2025-2026__c0003` und `bund-bvv3__art-7` («jährlich bis 20 Prozent des Erwerbseinkommens»).
> - **Einkauf von Lücken:** Seit 2025 sind Einkäufe in Lücken möglich, aber nur für Lücken ab dem Beitragsjahr 2025. Frühere Lücken können nicht eingekauft werden. Das gilt nur zusätzlich zum vollen ordentlichen Beitrag im Einkaufsjahr (Art. 7a/7b BVV 3). Die Bedingungen dafür habe ich nicht im Detail geprüft.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## q07

**Frage:** Kinderabzug 2025 in AR für ein 10-jähriges Kind – und beim Bund?

**Soll (Referenz):** AR 2025: CHF 7'400 (4.–15. Altersjahr; Anhang 1 StG, ar-stg-anhang-kp__c0001); Bund CHF 6'800 (Art. 35 DBG) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (25.2 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Kinderabzug 2025, Kind 10 Jahre alt (Stichtag 31.12.2025)**
> 
> | | Abzug | Status / Fundstelle |
> |---|---|---|
> | **AR (Staats- und Gemeindesteuer)** | **CHF 7'400** (Kind nach vollendetem 4. bis vollendetem 15. Altersjahr), Formular Ziff. 23.2 | ☑️ agent-geprüft · `ar-stg-anhang-kp__c0001` (Art. 38 Abs. 1 lit. a Ziff. 2), `ar-wl-2025__c0005` |
> | **Bund (direkte Bundessteuer)** | **CHF 6'800** vom Einkommen, einheitlich ohne Altersstufen (Art. 35 DBG) | ☑️ agent-geprüft · `bund-dbg-2025__art-35` |
> 
> **Zusätzlich beim Bund, nicht beim Kanton:**
> - Abzug vom Steuerbetrag: **CHF 263** pro Kind (Art. 36 Abs. 2^bis DBG). ☑️ `bund-dbg-2025__art-36-t4`
> - Versicherungsabzug: Zuschlag **CHF 700** pro Kind. ☑️ `bund-dbg-2025__art-33-t5`
> 
> **Zusätzlich in AR, nicht beim Bund:**
> - Versicherungsabzug: Zuschlag **CHF 1'000** pro Kind. ☑️ `ar-stg__art-35-t2`
> - Vermögensfreibetrag: **CHF 25'000** pro minderjähriges Kind mit Kinderabzug. ☑️ `ar-stg__art-51` Beim Bund gibt es keine Vermögenssteuer.
> 
> **Im Formular:** Das AR-Formular hat keine Bundesspalte. Man trägt den Kinderabzug nur einmal ein, bei Ziff. 23.2. Die Steuerverwaltung nimmt die Abweichungen für die Bundessteuer automatisch vor (`ar-wl-2025__c0179`).
> 
> **Voraussetzungen und Vorbehalte:**
> - AR kennt keinen Abzug, wenn die Einkünfte des Kindes über CHF 18'000 liegen. Ebenfalls kein Abzug gibt es, wenn Unterhaltsbeiträge nach Ziff. 12.2 abgezogen werden. Der Unterhalt des Kindes muss zur Hauptsache getragen werden.
> - Bei getrennt besteuerten Eltern mit gemeinsamer Sorge und ohne Unterhaltsbeiträge wird der Abzug je zur Hälfte aufgeteilt (CHF 3'700 AR / CHF 3'400 Bund).
> - Das Merkblatt MB 02 nennt teils noch die nicht indexierten Werte (z. B. 7'000). Massgebend sind die indexierten Werte aus Anhang 1 zum StG und der Wegleitung 2025.
> - Die Formularcodes für 23.x sind im Wiki als «nicht verifiziert» vermerkt. Die Ziffern stammen aus der Wegleitung. Das Hauptformular ist nicht online.
> - Der Status «agent-geprüft» bedeutet, dass die Fundstelle geprüft ist, die Abnahme aber noch offen ist. Die fachliche Beurteilung bleibt bei der Fachperson.

## q08

**Frage:** Versicherungsabzug ZH 2025 für ein Ehepaar mit 2 Kindern, beide mit Pensionskasse (Staatssteuer und Bund)?

**Soll (Referenz):** ZH Staat: 5'800 + 2 × 1'300 = 8'400; Bund: 3'700 + 2 × 700 = 5'100 (zh-stg-2025__par-31-t2, bund-dbg-2025__art-33).

**Antwort des Agenten** (26.0 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Maximaler Versicherungsabzug ZH, Steuerjahr 2025: Ehepaar (ungetrennte Ehe), 2 Kinder, beide mit Beiträgen an die 2. Säule (BVG)**
> 
> | | Staatssteuer | Bundessteuer |
> |---|---|---|
> | Ehepaar mit Beiträgen an 2. Säule/3a | CHF 5'800 | CHF 3'700 |
> | Zuschlag je Kind (2 × Kanton 1'300 / Bund 700) | CHF 2'600 | CHF 1'400 |
> | **Maximum total** | **CHF 8'400** | **CHF 5'100** |
> 
> Die Summen sind mit dem Rechentool geprüft. Alle Werte sind ☑️ agent-geprüft, die Abnahme ist noch offen.
> 
> **Hinweise zur Anwendung**
> - **Limite, nicht Pauschale:** Abziehbar ist der tiefere Betrag aus den tatsächlich bezahlten Prämien und dem Maximum. Die Prämien stehen im Form. 365 Teil A (Codes 601–604). Davon abzuziehen ist die Prämienverbilligung (Code 605), die aber nicht doppelt gekürzt werden darf, wenn sie schon in der Krankenkassenprämie verrechnet ist. Das Ergebnis kommt in Ziff. 15 (Code 270). Teil B zeigt die Maxima getrennt für Staat und Bund. Die Bundessteuer-Spalte hat tiefere Limiten.
> - **Beide mit PK:** Es gilt der normale Ansatz. Die höhere Limite «ohne Vorsorge» (Kanton 8'700 / Bund 5'550, plus Kinderzuschläge) gilt nur, wenn weder die Steuerpflichtigen noch deren Arbeitgeber Beiträge an die 2. Säule oder Säule 3a geleistet haben.
> - **Kinderzuschlag:** Er gilt für jedes Kind, für das der Kinderabzug geltend gemacht werden kann. Bei einem halben Kinderabzug (z. B. getrennt lebende Eltern) beträgt der Zuschlag Kanton 650 / Bund 350 je Kind.
> - **Lohnausweis:** Prämien für die Nichtberufsunfallversicherung (NBUV) sind im Nettolohn bereits abgezogen und dürfen nicht nochmals erfasst werden.
> 
> **Fundstellen**
> - Kanton: zh-stg-2025__par-31-t2 (§ 31 StG, CHF 5'800 und 1'300), zh-form-365-2025__c0001, zh-form-300-2025__c0008.
> - Bund: bund-dbg-2025__art-33-t2 und bund-dbg-2025__art-33-t5 (Art. 33 DBG, CHF 3'700 und 700).
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q09

**Frage:** Wie hoch ist der Kinderdrittbetreuungsabzug 2025 im Kanton ZH, und gilt 2026 ein anderer Wert?

**Soll (Referenz):** ZH 2025 CHF 25'000 (StG Nachtrag 127, zh-stg-2025__par-31-t4); 2026 CHF 25'300 (zh-stg-2026__par-31-t3). Die VKP ab 2024 (10'400) ist überholt.

**Antwort des Agenten** (24.3 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Ja, 2026 gilt für den Kanton ZH ein anderer Wert.** Der Abzug ist pro Kind begrenzt.
> 
> | | Kanton ZH (Staatssteuer) | Bund (dBSt) |
> |---|---|---|
> | **2025** | **CHF 25'000** pro Kind | CHF 25'800 |
> | **2026** | **CHF 25'300** pro Kind | CHF 25'800 |
> 
> Der kantonale Höchstbetrag steigt also um CHF 300. Der Bundesabzug bleibt gleich.
> 
> **Voraussetzungen (2025 und 2026 gleich)**
> - Das Kind hat das 14. Altersjahr noch nicht vollendet.
> - Das Kind lebt im gleichen Haushalt wie die Person, die für seinen Unterhalt sorgt.
> - Es sind nachgewiesene Kosten, die in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit stehen.
> 
> **Konkubinat und alternierende Obhut (2026)**
> Bei Konkubinat oder alternierender Obhut mit gemeinsamer Sorge gilt je der halbe Abzug, also CHF 12'650 pro Person. Für 2025 hat das Wiki dazu keine ausdrückliche Aussage geliefert. Ich habe es nicht weiter geprüft.
> 
> **Formular:** Ziff. 16.6 «Abzug für fremdbetreute Kinder», Code 376. Das gilt für 2025 (Jahrgänge 2011–2025) und für 2026 (Jahrgänge 2012–2026).
> 
> **Hinweis zu alten Quellen**
> Die Verwaltungsweisung (VKP) ab 2024 nennt noch CHF 10'400. Dieser Wert ist überholt. Massgebend sind das Steuergesetz in der Fassung Nachtrag 127 (2025) und Nachtrag 132 (2026) sowie die Wegleitung der jeweiligen Jahresfassung.
> 
> **Fundstellen**
> - 2025: `zh-stg-2025__par-31-t4` (Kanton), `bund-dbg-2025__art-33-t7` (Bund).
> - 2026: `zh-stg-2026__par-31-t3` (Kanton), `bund-dbg-2026__art-33-t7` (Bund).
> 
> **Status:** Alle Werte sind ☑️ agent-geprüft. Die Fundstellen sind geprüft, die Abnahme ist noch offen. Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Ich bin dein neuer Assistent und habe noch keinen Namen. Wie möchtest du mich nennen?

## q10

**Frage:** Gibt es im Kanton TG einen Zweiverdienerabzug für die Staatssteuer?

**Soll (Referenz):** Nein, TG kennt keinen kantonalen Zweiverdienerabzug (nur Bund: 50 %, 8'600–14'100).

**Antwort des Agenten** (22.2 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Nein.** Im Kanton Thurgau gibt es für die Staats- und Gemeindesteuern keinen Zweiverdienerabzug (Steuerjahr 2025, da kein Jahr genannt wurde). Die Wegleitung TG sagt dazu: «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.» (Quelle: tg-wl-2025__c0104, ☑️ agent-geprüft, Abnahme offen)
> 
> **Bund (direkte Bundessteuer):** Dort gibt es den Abzug, und zwar in der rechten Spalte des TG-Formulars, Ziff. 18 (Code 356):
> - 50 % des niedrigeren Erwerbseinkommens
> - mindestens Fr. 8'600, höchstens Fr. 14'100 (Quelle: bund-dbg-2025__art-33-t6, ☑️ agent-geprüft)
> - Das Erwerbseinkommen wird nach Berufsauslagen und nach Beiträgen an Säule 2 und 3a gerechnet.
> - Der Abzug gilt nur für gemeinsam besteuerte Ehepaare oder eingetragene Partner, die beide erwerbstätig sind.
> - Löhne, die im vereinfachten Abrechnungsverfahren versteuert werden, zählen nicht mit.
> 
> Im Formular TG steht der Abzug zwar bei den Abzügen (Ziff. 18). Ausgefüllt wird aber nur die Bundesspalte, die Kantonsspalte bleibt leer. (Quelle: tg-form-01-2025__c0011)
> 
> Für ein anderes Steuerjahr (z. B. 2026) prüfe ich das gern separat. Die fachliche Beurteilung im Einzelfall bleibt bei der zuständigen Fachperson.

## q11

**Frage:** SG 2025: Pauschale für übrige Berufskosten? Wie wird sie berechnet?

**Soll (Referenz):** SG 2025: CHF 700 + 10 % des Nettolohns, max. CHF 2'400 (Art. 21 StV SG, WL SG 2025).

**Antwort des Agenten** (26.9 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **SG 2025 – Pauschale für übrige Berufskosten**
> 
> **Kanton (Staats- und Gemeindesteuer)**
> - Formel: **Fr. 700 + 10 % des Nettolohns, höchstens Fr. 2'400**. Es gibt kein Minimum.
> - Der Abzug erfolgt ohne Nachweis auf Formular 4, Ziff. 3.1 (Code 416 Person 1 / 466 Person 2). Das Total geht in die Steuererklärung, Ziff. 10.1 (Code 438) bzw. 10.2 (Code 488).
> - Rechnerisch: `min(700 + 10 % × Nettolohn; 2'400)`. Das Maximum ist ab einem Nettolohn von Fr. 17'000 erreicht.
> - Nettolohn = Ziff. 1.1 der Steuererklärung. Das ist der Bruttolohn abzüglich der Beiträge an AHV/IV/EO/ALV/UV und BVG (ohne Einkäufe). Bei einem Teiljahr wird umgerechnet.
> - Bei ALV-Taggeldern gilt die Pauschale sinngemäss.
> - Quellen: Art. 21 StV SG (sg-stv__art-21), Form. 4 (sg-form-4-2025__c0003), Wegleitung (sg-wl-2025__c0080). Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Bund (direkte Bundessteuer)**
> - Formel: **3 % des Nettolohns, mindestens Fr. 2'000, höchstens Fr. 4'000**. Es gibt keinen fixen Sockelbetrag.
> - Das Formular hat nur eine Spalte. Die Abweichung für den Bund nimmt die Steuerbehörde automatisch vor, Sie tragen nichts separat ein.
> - Quelle: bund-bkv-2025__anhang-1. Status ☑️ agent-geprüft.
> 
> **Beispiel bei Nettolohn Fr. 80'000** (mit `rechne` gerechnet)
> - Kanton: Fr. 2'400 (Maximum)
> - Bund: Fr. 2'400 (3 % entsprechen genau diesem Betrag)
> 
> **Zu beachten**
> - Es gilt entweder die Pauschale (Ziff. 3.1) oder die tatsächlichen Kosten (Ziff. 3.2, Code 418/468). Die tatsächlichen Kosten sind nur sinnvoll, wenn sie die Pauschale übersteigen. Dann müssen alle übrigen Kosten belegt werden, auf einem Beiblatt zu Formular 4.
> - Ein Arbeitszimmer ist mit der Pauschale abgegolten. Es lässt sich nicht zusätzlich abziehen.
> - Zahlt der Arbeitgeber nicht ereignisbezogene Pauschalspesen aus, gibt es keine zusätzliche Pauschale.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.
> 
> Ask me anything; for system things I'll ask OpenClaw.

## q12

**Frage:** Pauschalabzug Liegenschaftsunterhalt in AR für ein 8-jähriges Einfamilienhaus – und wie in ZH?

**Soll (Referenz):** AR: 10 % (Gebäude bis 10 Jahre) bzw. 20 % des Bruttoertrags, nur bis Bruttomietertrag 100'000 (Art. 25 StV AR, MB 03); ZH: einheitlich 20 % ohne Altersstaffel (ZStB 30.2).

**Antwort des Agenten** (31.4 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position):

> Ich habe Steuerjahr 2025 verwendet, weil du keines genannt hast. Für ein 8-jähriges Einfamilienhaus im Privatvermögen gilt:
> 
> | | Kanton (Staatssteuer) | Bund (dBSt) |
> |---|---|---|
> | **AR** | **10 %** (Gebäude bis 10 Jahre) | **10 %** |
> | **ZH** | **20 %** (keine Altersstaffelung) | **10 %** (Gebäude bis 10 Jahre) |
> 
> **AR**
> - Die Pauschale beträgt 10 % bis und mit 10 Jahre Gebäudealter und 20 % darüber (ar-mb-03__c0004, ar-wl-2025__c0175).
> - Du kannst sie nur wählen, wenn der Bruttomietertrag des gesamten Liegenschaftsbesitzes höchstens CHF 100'000 beträgt. Die Liegenschaft muss ganz oder vorwiegend Wohnzwecken dienen.
> - Das Wahlrecht gilt je Gebäude und Jahr: Pauschale (Form. 7 Abschn. C1) oder tatsächliche Kosten (C2). Das Ergebnis kommt in Ziff. 15.
> - Bei Einzelbeträgen ab CHF 5'000 musst du Rechnungskopien beilegen, wenn du die tatsächlichen Kosten wählst.
> - Das AR-Formular hat keine Bundesspalte. Die Steuerverwaltung nimmt die Bundesanpassungen automatisch vor (ar-wl-2025__c0179). Für den Bund gilt 10 % nach bund-lkv__art-5.
> - Beim Eigenheim ist die Basis der Eigenmietwert. Kantonal gilt der Eigenmietwert nach dem 20 %-Selbstnutzungsabzug, beim Bund der Brutto-Eigenmietwert (ar-form-07-2025__c0003).
> 
> **ZH**
> - Die Pauschale beträgt einheitlich 20 % des Brutto-Mietertrags bzw. Brutto-Mietwerts (zh-zstb-30-2__c0002, zh-form-350__c0007).
> - Die Bundessteuer-Spalte hat eigene Sätze: 10 % bei Gebäuden bis 10 Jahre, sonst 20 % (bund-lkv__art-5). Bei deinem 8-jährigen Haus rechnest du also im Form. 350 Staat 20 % und Bund 10 %.
> - Das Wahlrecht gilt je Liegenschaft und Steuerperiode: Pauschale oder effektive Kosten (Form. 350, Codes 5731 ff. bzw. 5741 ff.).
> - Mit der Pauschale sind keine weiteren Abzüge möglich, ausser Baurechtszinsen.
> - Das Ergebnis läuft über den Nettoertrag aus Liegenschaften in Ziff. 6 (Code 188).
> - Belege brauchst du nur auf Verlangen.
> 
> **Wichtigster Unterschied:** AR gewährt für ein junges Haus nur 10 %, ZH 20 %. Beim Bund gelten 10 % in beiden Kantonen.
> 
> **Stand der Werte:** Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Ob die Pauschale oder die tatsächlichen Kosten günstiger sind, hängt von deinen effektiven Unterhaltskosten ab. Das müsste die Fachperson prüfen.
> 
> Nebenbei: Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## q13

**Frage:** TG: Welcher Einschlag gilt auf dem Eigenmietwert der selbstbewohnten Liegenschaft am Wohnsitz (Kanton vs. Bund)?

**Soll (Referenz):** TG: Abzug 40 % Kanton, 20 % Bund für dauernd selbstbewohntes Eigentum am Wohnsitz (tg-stg__par-23; WL TG 2025).

**Antwort des Agenten** (26.3 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **TG 2025: Kanton 40 %, Bund 20 %.** Das Steuerjahr haben Sie nicht genannt, ich habe 2025 verwendet.
> 
> Der Einschlag ist ein Selbstnutzungsabzug auf den Mietwert. Er gilt nur für Wohneigentum, das am Wohnsitz dauernd selbst bewohnt wird.
> 
> | | Abzug auf den (indexierten) Mietwert | Quelle | Status |
> |---|---|---|---|
> | **Kanton (Staats-/Gemeindesteuer)** | **40 %** | tg-stg__par-23: «Abzug von 40 Prozent» | ☑️ agent-geprüft |
> | **Bund (direkte Bundessteuer)** | **20 %** | tg-wl-2025__c0225: «kantonal einen Abzug von 40% und beim Bund von 20% vornehmen» | ☑️ agent-geprüft |
> 
> Das DBG kennt keinen eigenen festen Prozentsatz. Der Bundessatz von 20 % stammt aus der TG-Wegleitung.
> 
> **Im Formular:**
> - Der Mietwert steht in Formular 7 («Mietwert selbstgenutzt»).
> - Der steuerbare Eigenmietwert wird dort für Staat und Bund getrennt gerechnet. Der Nettoerfolg weicht deshalb je Spalte ab.
> - Er geht in Ziff. 8.1 (Code 180), links Staat/Gemeinde, rechts Bund.
> 
> **Rechnung je Spalte:** steuerbarer Eigenmietwert = Mietwert × (1 − 0.40) für den Kanton bzw. × (1 − 0.20) für den Bund. Davon wird der Unterhalt abgezogen.
> 
> **Unterhalt:** Pauschal sind es für Kanton und Bund gleich 10 % bei Gebäuden bis 10 Jahre und 20 % bei älteren. Die Pauschale wird vom steuerbaren Eigenmietwert berechnet. Alternativ können Sie die effektiven Kosten über Formular 8 geltend machen. Die Wahl gilt je Liegenschaft und Jahr.
> 
> **Ausnahmen:** Bei Zweit- oder Ferienwohnungen, landwirtschaftlich geschätzten Liegenschaften und an Nahestehende überlassenen Objekten gibt es keinen Selbstnutzungsabzug. Dort ist der Mietwert zu 100 % steuerbar.
> 
> Konkrete Franken-Beträge kann ich rechnen, sobald der indexierte Mietwert aus der Liegenschaftensteuerrechnung oder dem Schätzungsprotokoll vorliegt. Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Falls Sie mich im Alltag nutzen: Ich bin neu hier. Wie soll ich heissen?

## q14

**Frage:** Bis wann kann ein Treuhänder im Kanton TG für seine Mandanten Fristerstreckung erhalten?

**Soll (Referenz):** Gewerbsmässige Treuhänder für Mandanten bis 31.12. des Deklarationsjahres (StP 155 Nr. 2).

**Antwort des Agenten** (25.5 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Thurgau (Steuerjahr 2025, gilt auch für 2026 und 2027):** Gewerbsmässige Treuhänder und Steuerberater können für ihre Mandanten ein Fristerstreckungsgesuch **längstens bis zum 31. Dezember des Deklarationsjahres** beantragen.
> 
> Das Deklarationsjahr ist das Jahr der Einreichung. Für das Steuerjahr 2025 ist das also der **31. Dezember 2026**.
> 
> - **Normalfall bei Privaten:** Die erste Erstreckung geht grundsätzlich bis 30. September. Weitere Gesuche werden in begründeten Fällen bis 30. November bewilligt. Der Treuhänder hat also gegenüber Privaten rund einen Monat mehr.
> - **Gesuch:** Es ist beim Gemeindesteueramt einzureichen, schriftlich, begründet und rechtzeitig. Dieses entscheidet darüber.
> - **Über den 31. Dezember hinaus:** Das ist nur bei ausserordentlichen Gründen möglich, die glaubhaft gemacht werden. Die Sachdarstellung muss substanziiert sein. Starke berufliche Inanspruchnahme des Vertreters oder fehlende Unterlagen genügen nicht. Arbeitsüberlastung ist generell kein Grund.
> - **Bund:** Die direkte Bundessteuer hat keine eigene Frist. Die kantonale Fristerstreckung gilt auch für sie.
> - **Gebühr:** Für natürliche Personen nennen die Quellen keine Gebühr. Für juristische Personen gibt es eine Kanzleigebühr von Fr. 30. Das gilt nach § 39b StV TG (tg-stv__par-39b), den ich nicht im Wortlaut geöffnet habe.
> 
> **Fundstelle:** StP 155 Nr. 2, Chunks tg-stp-155-2__c0001 und tg-stp-155-2__c0002. Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> Die Frage nannte kein Steuerjahr, deshalb habe ich 2025 verwendet. Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Nebenbei: Ich bin neu hier und noch unbenannt. Wie möchtest du mich nennen?

## q15

**Frage:** ZH: Bis wann ist die Steuererklärung 2025 einzureichen und wie lange wird höchstens Fristerstreckung gewährt?

**Soll (Referenz):** Einreichung bis 31.03.2026; Fristerstreckung längstens bis 30. November (ZStB 132.1 / WL ZH 2025).

**Antwort des Agenten** (25.0 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **ZH, Steuerjahr 2025**
> 
> - **Einreichefrist:** Die Steuererklärung 2025 ist bis **31. März 2026** einzureichen, online oder über das Scan-Center. Das steht in der Wegleitung ZH 2025: «Die Steuererklärung ist bis am 31. März 2026 einzureichen.» (zh-wl-2025__c0017, ☑️ agent-geprüft, Abnahme offen)
> - **Maximale Fristerstreckung:** Eine rechtzeitig gestellte Erstreckung wird längstens bis **30. November 2026** bewilligt, also bis 30. November des Folgejahres. (zh-zstb-132-1__c0024, ☑️ agent-geprüft, Abnahme offen)
> 
> **Weitere Regeln dazu**
> - Das Gesuch muss **vor Fristablauf** beim Gemeindesteueramt eingehen.
> - Das erste Gesuch gilt ohne gegenteiligen Entscheid als stillschweigend bewilligt.
> - Eine Erstreckung über den 30. November hinaus gibt es nur aus ausserordentlichen Gründen. Die berufliche Belastung des Vertreters genügt dafür nicht.
> - Selbständige und Ausserkantonale erhalten von Amtes wegen eine Erstreckung bis 30. September.
> - Mahnfristen sind nicht erstreckbar.
> - Die Kosten einer Fristerstreckung nennen die Quellen nicht. Dazu mache ich keine Aussage.
> 
> **Bund:** Die direkte Bundessteuer hat keine eigene Frist. Die Frist und die Erstreckung des Kantons gelten auch für den Bundesteil der kantonalen Steuererklärung.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.
> 
> Ich bin übrigens dein neuer Assistent. Wie möchtest du mich nennen?

## q16

**Frage:** AR: Was kostet die zweite Fristverlängerung?

**Soll (Referenz):** CHF 25 (erste Verlängerung kostenlos, jede weitere CHF 25; MB 18 / WL AR 2025).

**Antwort des Agenten** (22.6 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **AR, Steuerjahr 2025: Die zweite Fristverlängerung kostet CHF 25.** ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen)
> 
> - Die erste Fristverlängerung ist kostenlos. Jede weitere kostet CHF 25 (`ar-wl-2025__c0012`: «nur die erste Fristverlängerung kostenlos ist»).
> - Die Gebühr steht auch in Art. 59a StV AR (`ar-stv__art-59a`): «Die erstmalige Fristerstreckung ist kostenlos». Das Merkblatt 18 nennt für Fristverlängerungen im Wiederholungsfall Fr. 25 (`ar-mb-18__c0001`, Gebührenansätze ab 1.9.2025).
> - Das Gesuch muss vor Ablauf der Einreichefrist bei der Kantonalen Steuerverwaltung eingehen. Es lässt sich online stellen (esteuern.ar.ch).
> - Beim Bund (direkte Bundessteuer) gibt es keine eigene Regelung. Die Fristerstreckung ist kantonal geregelt, die CHF 25 fallen also nur auf Kantonsebene an.
> 
> Du hast kein Steuerjahr genannt, deshalb habe ich 2025 verwendet. Für 2026 habe ich den Betrag nicht separat geprüft. Das Merkblatt 18 und Art. 59a StV sind aber auch für 2026 ausgewiesen.
> 
> Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## q17

**Frage:** Krankheitskosten SG 2025: Ab welchem Selbstbehalt sind sie abziehbar – und beim Bund?

**Soll (Referenz):** SG: Selbstbehalt 2 % (Art. 46 StG SG); Bund: 5 % (Art. 33 Abs. 1 lit. h DBG, KS 11).

**Antwort des Agenten** (26.1 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__zeige):

> Krankheits- und Unfallkosten sind abziehbar, soweit sie einen Selbstbehalt übersteigen: im Kanton SG 2025 sind das 2 %, bei der direkten Bundessteuer 5 %.
> 
> | | Selbstbehalt | Bemessungsgrundlage | Fundstelle |
> |---|---|---|---|
> | **Kanton SG** | **2 %** | Nettoeinkommen (Ziff. 20) | `sg-stg-2025__art-46`, Art. 46 StG SG ☑️ |
> | **Bund (DBG)** | **5 %** | steuerbare Einkünfte, vermindert um die Aufwendungen nach Art. 26–33 DBG | `bund-dbg-2025__art-33-t3`, Art. 33 Abs. 1 lit. h DBG ☑️ |
> 
> (☑️ = Fundstelle geprüft, Abnahme offen.)
> 
> **Im Formular SG 2025**
> - Es gibt nur eine Spalte. Den Bundesabzug rechnet die Steuerbehörde automatisch um (Merkblatt 32, `sg-wl-2025__c0173`).
> - Ziff. 21.1: Die Vorkolonne (Code 650) ist die Summe aus Bruttokosten minus Beiträgen Dritter. Der Selbstbehalt steht unter Code 238, der Abzug unter Code 240.
> - Der Abzug ist die Vorkolonne minus 2 % × Ziff. 20, mindestens 0.
> 
> **Zu beachten**
> - Abziehbar sind nur die selbst getragenen Kosten, also nach Abzug von Krankenkassen- und Versicherungsleistungen sowie Hilflosenentschädigung (`sg-form-6-2025__c0003`).
> - Die Diät-Pauschale von Fr. 2'500 gilt nur bei dauernder, lebensnotwendiger Diät, zum Beispiel Zöliakie, nicht Diabetes. Beim ersten Mal braucht es eine ärztliche Bescheinigung. Diesen Wert führt das Wiki für SG.
> - Behinderungsbedingte Kosten sind ohne Selbstbehalt abziehbar. In SG gehören sie in Ziff. 21.2, beim Bund unter Art. 33 Abs. 1 lit. h^bis DBG.
> - Krankenkassenprämien gehören nicht hierher, sondern in Ziff. 14.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.
> 
> Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## q18

**Frage:** PK-Einkauf CHF 20'000 wurde über den Lohn abgezogen (Lohnausweis Ziff. 10.2). Darf er nochmals in der Steuererklärung abgezogen werden?

**Soll (Referenz):** Nein – BVG-Einkauf über Lohnabzug (Lohnausweis Ziff. 10.2) ist bereits im Nettolohn berücksichtigt; nur direkt bezahlte Einkäufe separat abziehen.

**Antwort des Agenten** (42.2 s · Tools: 10 Aufrufe steuerwiki__wert, steuerwiki__beleg, steuerwiki__suche, steuerwiki__zeige, steuerwiki__position):

> **Nein, der Einkauf darf nicht nochmals abgezogen werden.** Ein Einkauf, der über den Lohn abgezogen wurde und in Ziff. 10.2 des Lohnausweises steht, ist bereits berücksichtigt. Ein zweiter Abzug in der Steuererklärung wäre ein Doppelabzug.
> 
> Die Frage nennt weder Kanton noch Jahr. Ich habe Steuerjahr 2025 angenommen und die Zeilen am Formular des Kantons Zürich geprüft. Für SG, TG und AR habe ich die Formularpositionen nicht geprüft. Bund und Kanton gelten nach Gesetz gleich (Art. 33 Abs. 1 lit. d DBG, Art. 9 Abs. 2 lit. d StHG).
> 
> **Begründung**
> - **Nettolohn:** Der Lohnausweis weist unter Ziff. 10.2 die im Bruttolohn enthaltenen, vom Lohn abgezogenen Einkaufsbeiträge aus. Der Nettolohn in Ziff. 11 ist Ziff. 8 minus Ziff. 9 und 10 (✅/☑️ Quelle: `bund-wl-lohnausweis-2026__c0036`, ☑️ agent-geprüft). Die CHF 20'000 stecken damit schon im Nettolohn.
> - **Ziff. 11:** Sie übernehmen in der Steuererklärung den Nettolohn aus Ziff. 11 unverändert als Einkommen.
> - **Formular 21 EDP:** Einkäufe, die Sie selbst überwiesen haben (nicht vom Lohn abgezogen), bescheinigt die Pensionskasse mit dem Formular 21 EDP (`bund-wl-lohnausweis-2026__c0037`, `bund-mb-21edp__c0006` Rz 12). Nur diese Einkäufe tragen Sie als Abzug ein. Im Kanton Zürich ist das Ziff. 16.1 (Code 280).
> 
> **Was Sie tun müssen**
> - **Lohnausweis:** Er gehört immer zur Steuererklärung.
> - **Bescheinigung der Pensionskasse:** Legen Sie die Einkaufsbescheinigung bei, wenn Ihr Kanton sie verlangt (Zürich verlangt sie nur bei Abzug unter Ziff. 16.1).
> - **Dreijahressperrfrist:** Ein Einkauf ist steuerlich nicht abziehbar, wenn innerhalb von drei Jahren ein Kapitalbezug erfolgt (`zh-wl-2025`-Zuordnung, KS 17/KS 41).
> 
> **Vorbehalte**
> - **Wegleitung 2026:** Die Wegleitung zum Lohnausweis liegt im Wiki nur in der Fassung 2026 vor. Für 2025 gibt es keine eigene Fassung. Die Regel zu Ziff. 10.2/11 ist qualitativ und hat keine Beträge, ich gehe von derselben Regel aus.
> - **Anderer Kanton:** Wenn Sie in einem anderen Kanton als ZH wohnen, nennen Sie mir Kanton und Jahr. Dann prüfe ich die dortige Formularposition.
> - **Zusätzlicher Einkauf:** Haben Sie neben den CHF 20'000 über den Lohn noch einen Einkauf selbst überwiesen, kommt nur dieser zweite Betrag in den Abzug.
> - **Fachperson:** Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.
> 
> Ich bin Ihr neuer Assistent, und das Einrichten meiner Identität steht noch aus. Wie möchten Sie mich nennen?

## q19

**Frage:** Weiterbildungskosten CHF 15'000 (ZH, 2025), Arbeitgeber hat nichts bezahlt. Wie viel ist abziehbar (Kanton/Bund)?

**Soll (Referenz):** ZH Staat max. CHF 12'400 (zh-stg-2025__par-31-t4); Bund max. CHF 13'000 (bund-dbg-2025__art-33-t4).

**Antwort des Agenten** (26.6 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Weiterbildungskosten CHF 15'000, ZH, Steuerjahr 2025, ohne Arbeitgeberbeitrag**
> 
> | | Selbst getragen | Maximum | **Abziehbar** | Nicht abziehbar |
> |---|---|---|---|---|
> | **Kanton ZH (Staatssteuer)** | 15'000 | 12'400 | **CHF 12'400** | 2'600 |
> | **Bund (dBSt)** | 15'000 | 13'000 | **CHF 13'000** | 2'000 |
> 
> Die Rechnung lautet je Person: Abzug = min(selbst getragene Kosten; Limite). Der Abzug ist also in beiden Fällen auf die Limite gekappt.
> 
> **Formular ZH 2025**
> - Die Eintragung erfolgt in Ziff. 16.2 «Berufsorientierte Aus- und Weiterbildungskosten» (Code 292). Staatssteuer- und Bundessteuer-Spalte füllst du getrennt aus.
> - Das Hilfsblatt Form. 367 ist beizulegen:
>   - Total der Kosten: 2900 = 15'000.
>   - Beitrag Arbeitgeber/Dritte: 2901 = 0.
>   - Selbst getragen: 2902 = 15'000.
>   - Zulässiger Abzug: 2920 = 12'400 im Block Staatssteuer und 13'000 im Block Bundessteuer.
> - Die Limiten gelten je Person. Bei einem Ehepaar hat jede Person ihr eigenes Maximum (Codes 2920 und 2921).
> 
> **Voraussetzungen, die du prüfen musst**
> - Es muss ein Abschluss auf Sek.-II-Stufe vorliegen oder das 20. Altersjahr vollendet sein. Die Ausbildung darf nicht bis zum ersten Sek.-II-Abschluss führen.
> - Die Weiterbildung muss berufsorientiert sein, inklusive Umschulung. Rein private Hobbykurse zählen nicht.
> - Für das Jahr zählt, wann die Rechnung fällig war bzw. bezahlt wurde, nicht wann du den Kurs besucht hast. Nur 2025 bezahlte Beträge gehören in diese Erklärung.
> - Die Angabe «Arbeitgeber hat nichts bezahlt» sollte zum Lohnausweis Ziff. 13.3 passen. Dort darf kein Beitrag stehen. Zahlungen des Arbeitgebers direkt ans Bildungsinstitut fehlen im Lohnausweis und müssten ebenfalls abgezogen werden.
> 
> **Belege:** Kursrechnungen und Zahlungsbelege werden nur auf Verlangen eingereicht. Form. 367 ist dagegen der Erklärung beizulegen.
> 
> **Quellen und Status** (alle ☑️ agent-geprüft, Abnahme offen)
> - Kanton CHF 12'400: `zh-stg-2025__par-31-t4`, `zh-wl-2025__c0093`.
> - Bund CHF 13'000: `bund-dbg-2025__art-33-t4`.
> - Formular: `zh-form-300-2025__c0008`, `zh-form-367-2025__c0001`.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson. Ob der Kurs im Einzelfall als berufsorientiert gilt, lässt sich aus den Angaben nicht entscheiden.

## q20

**Frage:** Spenden CHF 50 an eine gemeinnützige Organisation (TG 2025) – abziehbar?

**Soll (Referenz):** Nein – TG: Zuwendungen nur abziehbar, wenn sie CHF 200 übersteigen (StG TG § 34 Abs. 1 Ziff. 11); Bund: ab CHF 100.

**Antwort des Agenten** (26.4 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Nein, CHF 50 bringen in TG 2025 keinen Abzug**, weder beim Kanton noch beim Bund. Der Betrag liegt unter beiden Mindestgrenzen.
> 
> | | Kanton TG (Staats-/Gemeindesteuer) | Bund (dBSt) |
> |---|---|---|
> | Mindestbetrag | nur der Teil über CHF 200 (Selbstbehalt) ist abziehbar | Abzug erst, wenn die Spenden im Jahr insgesamt CHF 100 erreichen |
> | Abzug bei CHF 50 | max(0; 50 − 200) = **CHF 0** | **CHF 0**, weil unter CHF 100 |
> | Höchstbetrag | CHF 8'000 bei Nettoeinkommen bis CHF 40'000, sonst 20 % des Nettoeinkommens (Ziff. 22) | 20 % des Nettoeinkommens |
> 
> Die Grenzen gelten für alle freiwilligen Zuwendungen eines Jahres zusammen. Bei Spenden an mehrere Organisationen zählt also die Summe. Wenn Ihr Mandant im Jahr 2025 weitere Spenden geleistet hat, kann sich das Bild ändern:
> - **Kanton:** Abziehbar ist nur der Teil der Gesamtsumme über CHF 200. Bei CHF 500 sind das CHF 300.
> - **Bund:** Ab einer Gesamtsumme von CHF 100 ist die ganze Summe abziehbar, ohne Selbstbehalt.
> 
> **Voraussetzungen, falls es doch zum Abzug kommt**
> - Die Organisation muss in der Schweiz sitzen und steuerbefreit sein, mit öffentlichen oder gemeinnützigen Zwecken. Sie wird in der Liste der Steuerverwaltung TG geprüft.
> - Religiöse, kulturelle, gesellige und sportliche Zwecke sind nicht abziehbar. Das gilt auch für Organisationen mit Sitz im Ausland und für ehrenamtliche Arbeit.
> - Die Spende wird im Hilfsblatt Formular 6 einzeln mit Name und Sitz der Organisation eingetragen. Der Übertrag geht in Ziff. 23.2 (Code 366). Sammelvermerke wie «diverse Organisationen» werden nicht anerkannt.
> - Belege müssen erst ab CHF 1'000 pro Zuwendung eingereicht werden. Darunter genügt die Quittung, die nur auf Verlangen vorgelegt wird. Heben Sie sie trotzdem auf.
> 
> **Quellen** (alle ☑️ agent-geprüft, Abnahme offen): tg-stg__par-34-t4, bund-dbg-2025__art-33a, tg-form-06-2025__c0002, tg-form-01-2025__c0012, tg-wl-2025__c0220.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q21

**Frage:** Was ändert sich 2026 bei der Säule 3a (Einkauf) und wo wird das im ZH-Formular 2026 eingetragen?

**Soll (Referenz):** Ab 2026 Einkauf (Nachzahlung) Säule 3a für Beitragslücken ab 2025 (max. 7'258 pro Einkaufsjahr, BVV 3 Art. 7a, KS 18a); ZH-Formular 2026: Ziff. 14.3 (Code 264, Detailfelder 276/278).

**Antwort des Agenten** (30.5 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__vergleich, steuerwiki__zeige):

> **Stand:** Steuerjahr 2026, Kanton Zürich. Das reguläre ZH-Formular und die reguläre Wegleitung 2026 sind noch nicht publiziert (Stand 09.11.2026). Die Zuordnung stützt sich auf Formular und Wegleitung 2026 für unterjährige Steuerpflicht (UJ). Ziffern und Codes bitte am regulären Formular nochmals prüfen.
> 
> ## Was neu ist (Quelle: zh-wl-2026-uj__c0077)
> 
> Ab Steuerperiode 2026 kann man zusätzlich zu den ordentlichen 3a-Beiträgen Beitragslücken nachholen (Einkauf in die Säule 3a). Die Lücken müssen ab dem 1.1.2025 entstanden sein.
> 
> **Voraussetzungen:**
> - In den Lückenjahren wurden AHV/IV/EO-Beiträge geleistet, man war also zu 3a-Beiträgen berechtigt.
> - Im Einkaufsjahr wurde der maximal zulässige ordentliche Beitrag voll einbezahlt. Das sind CHF 7'258 mit 2. Säule, oder 20 % des Erwerbseinkommens, höchstens CHF 36'288, ohne 2. Säule.
> 
> **Limite:**
> - Der Einkauf darf höchstens so hoch sein wie die Summe der Lücken der letzten zehn Jahre, frühestens ab 1.1.2025.
> - In jedem Fall gilt ein Maximum von **CHF 7'258**.
> - Kanton und Bund haben dieselbe Limite (☑️ agent-geprüft; Bund: bund-wl-2a-2026__c0051).
> 
> **Praktisch für 2026:** Einkaufbar ist faktisch nur die Lücke 2025, weil frühere Jahre nicht zählen.
> 
> Die ordentlichen Höchstbeträge sind unverändert:
> - mit 2. Säule: CHF 7'258
> - ohne 2. Säule: 20 %, maximal CHF 36'288
> 
> Die Rechtsgrundlage (BVV 3) ist im Wiki nur über die Wegleitung belegt. Den Artikel habe ich nicht an einem Chunk geprüft.
> 
> ## Wo im ZH-Formular 2026 (Form. 300)
> 
> | Ziffer | Inhalt | Code |
> |---|---|---|
> | 14.1 / 14.2 | Ordentliche 3a-Beiträge | Person 1: 260, Person 2: 261 (effektiv 262/263) |
> | **14.3** | **Einkauf Säule 3a (neu)** | **Person 1: 276, Person 2: 278, Total in 264** |
> 
> Es gibt zwei Spalten, Staatssteuer und Bundessteuer. Die Beträge sind identisch, weil Kanton und Bund dieselbe Limite haben.
> 
> **Rechnung je Person:** min(Einkaufsbetrag; Summe der Beitragslücken; 7'258) → Code 276 bzw. 278.
> 
> **Belege:**
> - Einkaufsbescheinigung der 3a-Einrichtung
> - Bescheinigung über den ordentlichen Beitrag, als Nachweis des vollen Maximalbetrags im Einkaufsjahr
> - Nachweis der AHV/IV/EO-Beiträge im Lückenjahr
> 
> Der Einkauf gehört nicht in 14.1/14.2, sondern separat in 14.3.
> 
> Quellen: zh-form-300-2026-uj__c0008, zh-wl-2026-uj__c0075 und c0077. Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Falls du eigentlich den Einkauf in die Pensionskasse (2. Säule) gemeint hast: Der ist eine andere Position und hat andere Regeln. Sag Bescheid, dann schaue ich das nach.
> 
> ---
> 
> Nebenbei: Ich bin dein neuer Assistent und noch namenlos. Wie möchtest du mich nennen?

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (32.3 s · Tools: 6 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__position):

> **Kurzfassung:** Natürliche Personen müssen keinen separaten Antrag stellen. Die Verrechnungssteuer (35 %) wird mit der **kantonalen Steuererklärung** zurückgefordert. Sie wird im **Wertschriftenverzeichnis** deklariert und dort als «Verrechnungssteueranspruch» ausgewiesen. Es gibt kein eigenes Bundesformular. Die Rückerstattung läuft über den Wohnsitzkanton am 31.12.
> 
> Angaben gelten für das Steuerjahr 2025, weil kein Jahr genannt war. Sie sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Ablauf**
> 1. Alle Dividenden und Erträge ins Wertschriftenverzeichnis eintragen, brutto und vollständig. Der Steuerauszug der Bank dient als Kontrolle.
> 2. Erträge mit abgezogener Verrechnungssteuer stehen in **Kolonne A**. Das sind inländische Dividenden und Zinsen. Erträge ohne Abzug, etwa ausländische, stehen in **Kolonne B**.
> 3. Anspruch = 35 % × Total Bruttoertrag Kolonne A.
> 4. Die Steuerverwaltung verrechnet den Betrag mit der Steuerrechnung oder zahlt ihn aus. Dafür braucht es eine IBAN.
> 5. Das Wertschriftenverzeichnis muss unterschrieben sein.
> 
> **Wo der Anspruch ausgewiesen wird**
> 
> | Kanton | Formular / Position | Fundstelle |
> |---|---|---|
> | ZH | Form. 340, Code **540** (35 % von Total A). Total Steuerwert Code 400, Übertrag in Hauptformular Ziff. 30.1. Total A + B Code 150, Übertrag in Ziff. 4.1. | zh-form-340-2025__c0005 |
> | SG | Form. 2, Code **999** | sg-form-2-2025__c0006 |
> | TG | Form. 2, **Ziff. 10**. Auszahlungskonto auf Form. 1, Seite 1. | tg-form-02-2025__c0006 |
> | AR | Form. 2, Code **999** | ar-form-02-2025__c0007 |
> 
> Bei den Kantonen mit Bundesspalte (ZH, TG) deckt die kantonale Erklärung auch die direkte Bundessteuer ab. SG und AR haben nur eine Spalte. Dort nimmt die Steuerbehörde die Bundesanpassungen automatisch vor.
> 
> **Wichtige Bedingungen**
> - **Frist:** Der Anspruch erlischt, wenn er nicht innert dreier Jahre nach Ablauf des Fälligkeitsjahres beantragt wird (ZH, AR). SG nennt für Fälligkeiten 2025 «bis Ende 2028». Eine Fristerstreckung hemmt die Frist nicht.
> - **Verwirkung:** Wer Erträge oder Vermögen nicht deklariert, verliert den Anspruch. Eine Ausnahme gilt bei Fahrlässigkeit und nachträglicher Angabe (SG).
> - **Wohnsitz:** Die Rückerstattung erfolgt durch den Kanton, in dem man am 31.12. wohnte (TG, AR).
> - **Auszahlung:** TG zahlt unter dem Vorbehalt des Rückforderungsrechts der ESTV.
> - **Belege:** Der Steuerauszug der Bank muss beigelegt werden, wenn das Verzeichnis nur das Total daraus enthält.
> - **Sonderfall Kollektiv- und Kommanditgesellschaften:** Sie beantragen die Rückerstattung mit Formular 25 direkt bei der ESTV (AR, SG). Dasselbe gilt für STWE-Erneuerungsfonds.
> - **Ausländische Dividenden:** Das ist ein anderes Verfahren. Ausländische Quellensteuern werden über Formular **DA-1** zurückgefordert oder angerechnet (ZH: nur, wenn die nicht rückforderbaren Steuern insgesamt über CHF 100 liegen).
> 
> Für andere Kantone sind keine Angaben im Wiki vorhanden.
> 
> Ich bin übrigens dein neuer Assistent. Wie möchtest du mich nennen?

## q23

**Frage:** Vergleiche den Versicherungsabzug 2025 für Alleinstehende ohne Kinder in AR, SG, TG, ZH und beim Bund.

**Soll (Referenz):** Alleinstehend ohne Kinder 2025 (mit 2. Säule/3a): AR 2'700 · SG 3'400 · TG 3'500 · ZH 2'900 · Bund 1'800.

**Antwort des Agenten** (27.4 s · Tools: 3 Aufrufe steuerwiki__vergleich, steuerwiki__wert):

> **Versicherungsabzug 2025, alleinstehend, ohne Kinder (Höchstbeträge)**
> 
> Die Beträge gelten für Versicherungsprämien und Sparzinsen. Bei Kanton und Bund sind das getrennte Abzüge.
> 
> | Rang | Jurisdiktion | Abzug (Standardfall) | Fundstelle | Status |
> |---|---|---|---|---|
> | 1 | **TG** | CHF 3'500 | tg-stg__par-34-t3 | ☑️ |
> | 2 | **SG** | CHF 3'400 | sg-stg-2025__art-45-t2 | ☑️ |
> | 3 | **ZH** | CHF 2'900 | zh-stg-2025__par-31-t2 | ☑️ |
> | 4 | **AR** | CHF 2'700 | ar-stg__art-35-t2 | ☑️ |
> | 5 | **Bund** (direkte Bundessteuer) | CHF 1'800 | bund-dbg-2025__art-33-t2 | ☑️ |
> 
> TG hat den höchsten Abzug und der Bund den tiefsten. Zwischen TG und dem Bund liegen CHF 1'700.
> 
> **Erhöhter Betrag für Personen ohne Beiträge an die 2. Säule und Säule 3a**
> 
> Das gilt nur in ZH, SG und beim Bund. TG und AR kennen keinen separaten Betrag.
> 
> | Jurisdiktion | Abzug ohne Vorsorgebeiträge | Fundstelle |
> |---|---|---|
> | ZH | CHF 4'350 | zh-wl-2025__c0084 |
> | SG | CHF 3'900 | sg-stg-2025__art-45-t2 |
> | Bund | CHF 2'700 | bund-rs-2-210__c0006 |
> | TG | kein separater Betrag | – |
> | AR | kein separater Betrag | – |
> 
> Für den Bund und ZH habe ich den Betrag nur aus dem Vergleichstool übernommen. Den Betrag für den Bund habe ich nicht im Gesetzestext nachgeprüft, nur in der Wegleitung (Rz. 2-210). Für ZH und SG habe ich ihn nicht einzeln geöffnet.
> 
> **Hinweise**
> - **AR:** Vom Betrag von CHF 2'700 ist eine erhaltene Prämienverbilligung abzuziehen (Art. 35 lit. g StG, ar-stg__art-35-t2). Das steht im Werttext zu AR. Ob das auch für ZH, SG, TG und den Bund gilt, habe ich nicht geprüft.
> - **Status:** Alle Werte sind ☑️ agent-geprüft, das heisst die Fundstelle ist geprüft, aber die Abnahme durch eine Fachperson steht noch aus. Verifiziert (✅) ist keiner davon.
> - **Kinder:** Bei Kindern kommt ein Zuschlag pro Kind dazu. Er beträgt beim Bund CHF 700, in AR und TG CHF 1'000, in SG CHF 1'100 und in ZH CHF 1'300. Für Alleinstehende ohne Kinder spielt er keine Rolle.
> 
> Soll ich noch eine der Positionen im Formular (Ziffer, Rechenweg) für einen Kanton nachschlagen?

## q24

**Frage:** Steuerfreie Vermögensbeträge (Sozialabzüge) 2025 in SG für ein Ehepaar mit einem minderjährigen Kind?

**Soll (Referenz):** SG 2025: 150'000 (Ehepaar) + 20'000 pro minderjähriges Kind = 170'000 (sg-stg-2025__art-64).

**Antwort des Agenten** (22.8 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **SG 2025, Ehepaar mit einem minderjährigen Kind: steuerfreier Vermögensbetrag (Sozialabzug) CHF 170'000.**
> 
> | Position | Betrag | Formular SG 2025 |
> |---|---|---|
> | Gemeinsam steuerpflichtige Ehegatten (2 × 75'000) | CHF 150'000 | Ziff. 36.2, Code 332 |
> | Minderjähriges Kind (1 × 20'000) | CHF 20'000 | Ziff. 36.3, Code 334 |
> | **Total** | **CHF 170'000** | |
> 
> Die Summe habe ich mit `rechne` geprüft.
> 
> - **Kanton:** Der Abzug wird vom Reinvermögen abgezogen. Massgebend sind die Verhältnisse am 31.12.2025.
> - **Kind:** Der Abzug gilt nur für minderjährige Kinder unter elterlicher Sorge oder Obhut, für die ein Kinderabzug beansprucht werden kann. Für volljährige Kinder in Ausbildung gibt es keinen Abzug nach Ziff. 36.3.
> - **Bund:** Der Bund erhebt keine Vermögenssteuer. Es gibt deshalb keinen Bundesbetrag.
> - **Formular:** Das Formular hat nur eine Spalte. Abweichungen für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor (sg-wl-2025__c0173).
> 
> Quellen: sg-stg-2025__art-64 (75'000 und zusätzlich 20'000 pro Kind), sg-wl-2025__c0118 (150'000 gemeinsam), sg-form-1-2025__c0013 (Ziff. 36.1 und 36.2).
> Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).

## q25

**Frage:** Welcher Verzugszins gilt 2026 für die direkte Bundessteuer?

**Soll (Referenz):** 4.00 % (RS 2-215, bund-rs-2-215__c0010/c0011).

**Antwort des Agenten** (20.1 s · Tools: 1 Aufrufe steuerwiki__wert):

> Für die direkte Bundessteuer gilt 2026 ein **Verzugszins von 4,00 %** (2025: 4,50 %).
> 
> - Derselbe Satz von 4,00 % gilt auch für den Rückerstattungszins.
> - Der Vergütungszins für Vorauszahlungen beträgt 2026 0,00 % (2025: 0,75 %).
> - Der Bund kennt keinen Ausgleichszins.
> - Fundstelle: `bund-rs-2-215__c0010`. Status: ☑️ agent-geprüft, die Fundstelle ist geprüft, die Abnahme steht noch aus.
> 
> Das gilt nur für die direkte Bundessteuer. Bei Staats- und Gemeindesteuern setzen die Kantone ihre Sätze selbst fest. Nennen Sie mir bei Bedarf den Kanton (AR, SG, TG oder ZH), dann prüfe ich den kantonalen Satz.
> 
> Ich bin übrigens Ihr neuer Assistent. Wie möchten Sie mich nennen?

## q26

**Frage:** Wann wird der Eigenmietwert abgeschafft und gilt das schon für 2026?

**Soll (Referenz):** Abschaffung per 1.1.2029 (Bundesratsbeschluss 01.04.2026); für 2025–2028 gilt bisheriges Recht – 2026 also noch Eigenmietwert.

**Antwort des Agenten** (26.9 s · Tools: 5 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurz: Der Eigenmietwert fällt am 1. Januar 2029 weg. Für 2026 gilt das nicht, er bleibt für das Steuerjahr 2026 voll steuerbar.**
> 
> **Ablauf**
> - Im September 2025 haben Volk und Stände den Bundesbeschluss über die kantonalen Liegenschaftssteuern auf Zweitliegenschaften angenommen. Damit haben sie auch der Abschaffung der Eigenmietwertbesteuerung auf Erst- und Zweitliegenschaften zugestimmt (`bund-mm-eigenmietwert-abschaffung__c0003`).
> - Am 1. April 2026 hat der Bundesrat die Reform auf den **1. Januar 2029** in Kraft gesetzt (`…__c0002`).
> - Den Zeitpunkt hat er nach der Konsultation so gewählt, dass die Kantone ihre Liegenschaftssteuer auf Zweitliegenschaften gleichzeitig einführen können (`…__c0003`).
> 
> **Wirkung ab 2029 (Bund, Kantone und Gemeinden)**
> - Auf selbstgenutztem Wohneigentum wird kein Eigenmietwert mehr besteuert.
> - Der Abzug der Liegenschaftsunterhaltskosten entfällt für selbstgenutztes Wohneigentum. Bei vermietetem oder verpachtetem Wohneigentum bleibt er bestehen.
> - Schuldzinsen sind nur noch im Verhältnis des Werts der vermieteten oder verpachteten Liegenschaften zum gesamten Vermögen abziehbar.
> - Wer erstmals ein Eigenheim in der Schweiz erwirbt, erhält einen zeitlich und betragsmässig begrenzten Ersterwerberabzug für Schuldzinsen.
> - Bei der direkten Bundessteuer entfallen die Abzüge für Energiespar- und Umweltschutzinvestitionen. Die Kantone können sie zeitlich begrenzt beibehalten (`…__c0004`).
> - Die Kantone dürfen eine Sondersteuer auf überwiegend selbstgenutzte Zweitliegenschaften erheben.
> 
> **Für 2026**
> - Der Eigenmietwert gehört weiterhin zu den steuerbaren Einkünften (Formular 2 2026, Ziff. 8).
> - Der Unterhaltsabzug bleibt, pauschal oder effektiv. Die Pauschale beträgt bei der direkten Bundessteuer 10 % bei Gebäuden bis 10 Jahre und 20 % bei älteren Gebäuden, jeweils bezogen auf den Brutto-Eigenmietwert (`bund-lkv__art-5`, ☑️ agent-geprüft).
> 
> **Nicht geprüft:** Die kantonale Umsetzung für AR, SG, TG und ZH, also ob und wie die Zweitliegenschaftssteuer eingeführt wird. Das habe ich nicht abgeklärt. Wenn Sie mir den Kanton nennen, schaue ich das für 2026 gezielt nach.
> 
> Zur Einordnung: Ich bin Ihr neuer Assistent und habe noch keinen Namen. Wie möchten Sie mich nennen?

## q27

**Frage:** Zitiere die Regel zum Abzug privater Schuldzinsen im DBG (Steuerjahr 2025) mit Artikel.

**Soll (Referenz):** Art. 33 Abs. 1 lit. a DBG (Fassung 2025): private Schuldzinsen im Umfang der steuerbaren Vermögenserträge (Art. 20, 20a, 21) und weiterer CHF 50'000.

**Antwort des Agenten** (23.5 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Art. 33 Abs. 1 lit. a DBG** (Fassung Steuerjahr 2025, gültig bis 31.12.2025; Fundstelle `bund-dbg-2025__art-33-t1`):
> 
> > «Von den Einkünften werden abgezogen:
> > a. die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken. Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten oder ihr sonst wie nahe stehenden natürlichen Person zu Bedingungen gewährt, die erheblich von den im Geschäftsverkehr unter Dritten üblichen Bedingungen abweichen;»
> 
> **Kurz erklärt:**
> - Der Abzug ist begrenzt auf die steuerbaren Vermögenserträge (Art. 20, 20a, 21 DBG) plus 50 000 Franken.
> - Schuldzinsen auf Darlehen einer Kapitalgesellschaft an eine massgeblich beteiligte oder nahestehende Person sind nicht abzugsfähig, wenn die Bedingungen erheblich von den marktüblichen abweichen.
> 
> Die Eidgenössische Steuerverwaltung wendet die Regel so an (Bruttovermögensertrag + 50 000 Franken): KS 36, Ziff. 5.2 (`bund-ks-36__c0023`). Die Abgrenzung zu geschäftlichen Schuldzinsen steht in KS 22a, Ziff. 3.2 (`bund-ks-22a__c0014`).
> 
> **Status:** Der Gesetzestext stammt direkt aus dem Chunk im Wiki. Eine Statusmarkierung (✅/☑️) hat das Tool für diesen Chunk nicht ausgegeben. Für die Anwendung auf einen konkreten Fall bleibt die fachliche Beurteilung bei der Fachperson.
> 
> Falls Sie auch die kantonale Regelung brauchen (AR, SG, TG, ZH), nennen Sie mir den Kanton.

## q28

**Frage:** Ist ein Leasingvertrag für das Privatauto steuerlich relevant? Was ist mit den Leasingraten?

**Soll (Referenz):** Leasingraten sind keine Schuldzinsen und grundsätzlich nicht abziehbar (Lebenshaltung); relevant nur für Fahrkosten-Begründung/Geschäftsauto, Vermögen (kein Eigentum).

**Antwort des Agenten** (30.4 s · Tools: 6 Aufrufe steuerwiki__ablage, steuerwiki__beleg, steuerwiki__suche, read, steuerwiki__zeige):

> Kurz: Der Leasingvertrag für ein privat genutztes Auto ist **nicht steuerrelevant**, und die Leasingraten sind **nicht abziehbar**. Ich habe 2025 als Steuerjahr angenommen und keinen Kanton, weil Sie keinen genannt haben. Bei den Raten ist die Rechtslage in Bund, ZH, SG, TG und AR gleich.
> 
> **Leasingraten**
> - Sie zählen zu den privaten Lebenshaltungskosten. Der Zinsanteil in der Rate ist keine abziehbare Schuldzins (Art. 34 DBG).
> - Bund: «Leasingraten für privat genutzte Güter enthalten keine abzugsfähigen Zinsanteile» (KS 22a Ziff. 3.3, `bund-ks-22a__c0015`, Status ☑️ agent-geprüft, Abnahme offen).
> - AR nennt «Leasingraten» persönlicher Gebrauchsgegenstände und privater Fahrzeuge ausdrücklich als nicht abziehbar (`ar-wl-2025__c0081`, Treffer in der Suche, den Wortlaut habe ich nicht geöffnet).
> - ZH führt «Leasingraten» im Hilfsblatt Schuldzinsen als nicht abzugsberechtigt, wie Amortisationen (`zh-wl-2025__c0073`).
> - Die Raten gehören deshalb weder ins Schuldenverzeichnis noch in die Ziffer Schuldzinsen.
> 
> **Vermögen**
> - Ein geleastes Fahrzeug gehört der Leasinggesellschaft und wird nicht als Vermögen deklariert. Ein Fahrzeug im eigenen Eigentum wäre anders zu behandeln.
> 
> **Fahrkosten**
> - Das Leasing ändert nichts am Fahrkostenabzug für den Arbeitsweg. Ein Privatauto ist dafür nur in begründeten Fällen abziehbar, zum Beispiel wenn der öffentliche Verkehr nicht zumutbar ist. Das gilt für gekaufte und geleaste Autos gleich.
> - Die Leasingkosten sind mit der Kilometerpauschale abgegolten und nicht zusätzlich abziehbar.
> 
> **Ausnahmen**
> - Ist der Leasingnehmer ein Selbständigerwerbender oder das Geschäft, kann der geschäftliche Anteil als Geschäftsaufwand in die Jahresrechnung gehören. Das betrifft nicht das reine Privatauto.
> - Bei einem Geschäftsauto des Arbeitgebers ist das Leasing für die Privatanteil-Pauschale relevant. In SG gilt dann der im Vertrag festgehaltene Barkaufpreis ohne MWST (StB 39 Nr. 3 Ziff. 4.2.1, `sg-stb-39-3__c0017`). Diese Aufrechnung geht über die Frage nach dem Privatauto hinaus.
> 
> **Ablage**
> - Der Vertrag ist kein Steuerbeleg und wird nicht eingereicht. Er gehört in keine Kategorie der `KATEGORIEN.md`, weder «Belege eingereicht» noch «Belege Sonstiges», weil er in der Deklaration keinen Wert ergibt.
> - Falls Sie ihn trotzdem aufbewahren wollen, geht er unter «Unterlagen Kunde» oder in die allgemeine Ablage. Das ist meine Einschätzung und steht nicht in der Liste.
> - Wichtig für die Ablage sind nur Leasingnehmer, Vertragsbeginn und Vertragsende sowie die Frage, ob das Auto geschäftlich genutzt wird.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson. Ist das Auto ein Geschäftsfahrzeug oder soll der Fahrkostenabzug für den Arbeitsweg geprüft werden, nennen Sie mir bitte Kanton und Sachverhalt.
> 
> Noch eine Sache zu mir: Ich bin Ihr neuer Assistent. Wie möchten Sie mich nennen?

## q29

**Frage:** Wie hoch ist der Kinderabzug im Kanton Bern 2025?

**Soll (Referenz):** Nicht im Wiki (nur Bund, AR, SG, TG, ZH).

**Antwort des Agenten** (22.1 s · Tools: 1 Aufrufe steuerwiki__wert):

> Den Kinderabzug für den Kanton Bern 2025 kann ich nicht nennen. Das Steuer-Wiki deckt nur den Bund und die Kantone AR, SG, TG und ZH ab. Bern ist nicht im Wiki, und einen Wert schätze oder übernehme ich nicht aus einem anderen Kanton. Massgebend sind das Berner Steuergesetz und die Wegleitung der Steuerverwaltung Bern für 2025.
> 
> Für die **direkte Bundessteuer 2025**, die auch Berner Steuerpflichtige betrifft, liefert das Wiki diese Werte (☑️ agent-geprüft, Abnahme offen):
> - **Kinderabzug vom Einkommen:** CHF 6'800 pro minderjähriges oder in Ausbildung stehendes Kind. Quelle: `bund-dbg-2025__art-35`.
> - **Abzug vom Steuerbetrag:** zusätzlich CHF 263 pro Kind. Quelle: `bund-dbg-2025__art-36-t4`.
> - **Versicherungsabzug:** Zuschlag von CHF 700 pro Kind. Quelle: `bund-dbg-2025__art-33-t5`.
> 
> Diese Zahlen gelten nur für den Bundesanteil. Der Berner Kantons- und Gemeindeabzug kann davon abweichen.
> 
> Falls es für Ihren Fall hilft, kann ich den Kinderabzug für AR, SG, TG oder ZH nachschlagen.

## q30

**Frage:** Ehepaar TG 2025, beide angestellt (Nettolohn 80'000 und 30'000), pendelt mit ÖV-Abo (CHF 1'200 bzw. 900). Erstelle die Abzüge Berufskosten (Fahrkosten, Verpflegung ohne Kantine, Pauschale übrige) je Person für Kanton und Bund mit Fundstellen.

**Soll (Referenz):** TG 2025 je Person: Fahrkosten = ÖV-Abo effektiv (1'200 bzw. 900; Max. 6'000 Staat / 3'300 Bund); Verpflegung ohne Kantine 15/Tag, max. 3'200 (beide Ebenen); übrige Pauschale 3 %: P1 80'000 → 2'400, P2 30'000 → 900 → Minimum 2'000 (beide Ebenen, BKV TG § 4a / BKV Bund).

**Antwort des Agenten** (39.0 s · Tools: 6 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__zeige, steuerwiki__rechne):

> # Berufskosten TG 2025: Ehepaar, beide unselbständig erwerbend
> 
> **Annahmen:** Beide arbeiten 100 %, ganzjährig. Der Arbeitgeber übernimmt keine Fahrkosten (Lohnausweis Feld F nicht angekreuzt), und es steht keine Kantine zur Verfügung (Feld G nicht angekreuzt). Bei der Verpflegung ist die Heimkehr am Mittag unzumutbar. Die Zahlen stehen im Hilfsblatt Form. 4.2 (Person 1) bzw. 4.3 (Person 2). Status aller Werte: ☑️ agent-geprüft, Abnahme offen.
> 
> ## Person 1 (Nettolohn 80'000, ÖV-Abo 1'200), Form. 4.2
> 
> | Ziffer (Code) | Position | Kanton | Bund | Rechnung |
> |---|---|---|---|---|
> | 2.1 (206) / 2.5 (213) | Fahrkosten ÖV-Abo | **1'200** | **1'200** | tatsächliche Kosten; Maximum Kanton 6'000, Bund 3'300 nicht erreicht |
> | 3.1 (214) | Verpflegung ohne Kantine | **3'200** | **3'200** | Fr. 15 pro Tag, Maximum Fr. 3'200 |
> | 4 (220) | Übrige Berufskosten, Pauschale | **2'400** | **2'400** | 3 % × 80'000 = 2'400 (Rahmen 2'000–4'000) |
> | **7 (240)** | **Total Berufsauslagen** | **6'800** | **6'800** | 1'200 + 3'200 + 2'400 |
> 
> ## Person 2 (Nettolohn 30'000, ÖV-Abo 900), Form. 4.3
> 
> | Ziffer (Code) | Position | Kanton | Bund | Rechnung |
> |---|---|---|---|---|
> | 2.1 (246) / 2.5 (253) | Fahrkosten ÖV-Abo | **900** | **900** | tatsächliche Kosten; Maximum nicht erreicht |
> | 3.1 (254) | Verpflegung ohne Kantine | **3'200** | **3'200** | wie Person 1 |
> | 4 (260) | Übrige Berufskosten, Pauschale | **2'000** | **2'000** | 3 % × 30'000 = 900, also Minimum 2'000 |
> | **7 (280)** | **Total Berufsauslagen** | **6'100** | **6'100** | 900 + 3'200 + 2'000 |
> 
> Beide Totale gehen in Formular 1 auf Ziff. 10.1 (Code 240) und 10.2 (Code 280), jeweils in die Spalte Staat und die Spalte Bund. Zusammen sind es **12'900** für Kanton und für Bund.
> 
> ## Fundstellen
> 
> - **Fahrkosten:**
>   - Kanton: `tg-form-04-2-2025__c0002` (Ziff. 2.1) und `tg-wl-2025__c0177`.
>   - Maximum Kanton 6'000 / Bund 3'300 (Ziff. 2.5).
>   - Bund-Maximum 3'300: `bund-dbg-2025__art-26` (Art. 26 Abs. 1 lit. a DBG).
> - **Verpflegung:** `tg-form-04-2-2025__c0003` (Ziff. 3.1) und `tg-wl-2025__c0183`. Die gleichen Ansätze gelten beim Bund (`position`-Ausgabe, Feld «Bund»).
> - **Übrige Berufskosten:** `tg-form-04-2-2025__c0004` (Ziff. 4) und `tg-wl-2025__c0187`. Die Pauschale ist beim Bund gleich: 3 %, min. 2'000, max. 4'000.
> - **Übertrag ins Hauptformular:** `tg-form-01-2025__c0010` (Ziff. 10.1 und 10.2) und `tg-wl-2025__c0196`.
> 
> ## Offene Punkte
> 
> 1. **Verpflegung ist die unsichere Position.** Der Abzug gilt nur, wenn die Heimkehr am Mittag unzumutbar ist, also bei grosser Entfernung oder sehr kurzer Pause (`tg-wl-2025__c0183`). Pendeln mit ÖV allein reicht dafür nicht. Ist die Heimkehr zumutbar, entfallen je 3'200 und die Totale sinken auf 3'600 bzw. 2'900.
> 2. **Pensum:** Bei Teilzeit, besonders bei Person 2 mit dem tieferen Lohn, wird das Verpflegungsmaximum im Verhältnis zum Beschäftigungsgrad gekürzt. Das Pensum wurde nicht genannt. Ich habe 100 % angenommen und nicht geschätzt.
> 3. **Bund-Fahrkostenmaximum:** Die ESTV-Wegleitung 2025 nennt noch 3'200, das Gesetz 3'300. Nach Rangfolge gilt das Gesetz. Das Maximum wird hier nicht erreicht, die Zahlen bleiben also gleich.
> 4. **Lohnausweise prüfen:** Feld F (Geschäftsfahrzeug) und Feld G (Kantine) sind massgebend. Ist Feld G angekreuzt, gilt nur der halbe Verpflegungsabzug (Ziff. 3.2: Fr. 7.50 pro Tag, max. Fr. 1'600).
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q31

**Frage:** Ehepaar ZH 2026, beide erwerbstätig, Kind 3 Jahre in der Kita (Kosten CHF 30'000). Wie viel Drittbetreuung ist abziehbar (Kanton und Bund)?

**Soll (Referenz):** ZH 2026 Kanton max. CHF 25'300 pro Kind (zh-stg-2026__par-31-t3); Bund 2026 max. CHF 25'800 (bund-dbg-2026__art-33-t7). Abzug je Ebene getrennt.

**Antwort des Agenten** (24.5 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **Abziehbar sind beim Kanton CHF 25'300 und beim Bund CHF 25'800** (ZH, Steuerjahr 2026, Ziff. 16.6, Code 376).
> 
> | | Kosten | Höchstbetrag pro Kind | Abzug |
> |---|---|---|---|
> | Kanton (Staats- und Gemeindesteuer) | 30'000 | 25'300 | **25'300** |
> | Bund (direkte Bundessteuer) | 30'000 | 25'800 | **25'800** |
> 
> Der nicht abziehbare Rest beträgt beim Kanton CHF 4'700 und beim Bund CHF 4'200.
> 
> **Voraussetzungen, die bei Ihrem Fall erfüllt sind:**
> - Das Kind ist 3 Jahre alt. Die Altersgrenze liegt bei unter 14 Jahren (Jahrgänge 2012–2026).
> - Das Kind lebt im gleichen Haushalt.
> - Beide Eltern sind gleichzeitig erwerbstätig. Das verlangt die Wegleitung bei Ehepaaren.
> 
> **Was Sie noch prüfen sollten:**
> - **Pauschalrechnung:** Weist die Kita die Kosten nur pauschal aus, also inklusive Verpflegung usw., sind 20 % als Lebenshaltungskosten zu kürzen. Mit CHF 30'000 × 80 % = 24'000 läge der Abzug dann unter dem Höchstbetrag. Ich habe diese Kürzung nicht gerechnet, weil ich nicht weiss, wie die Rechnung aufgebaut ist.
> - **Nur Betreuung zählt:** Abziehbar sind nur Kosten während der Arbeitszeit. Nicht abziehbar sind z. B. Sport, Musik, Schulgeld und Nachhilfe.
> - **Belege:** Beizulegen sind die Kita-Rechnungen mit Zahlungsnachweis und eine Aufstellung der Betreuungskosten mit den Empfängern.
> 
> **Quellen und Status:**
> - Kanton 25'300: `zh-stg-2026__par-31-t3`, ☑️ agent-geprüft. Die alte Limite von 10'400 aus der VKP 2024 ist überholt.
> - Bund 25'800: `bund-dbg-2026__art-33-t7`, ☑️ agent-geprüft.
> - Das reguläre ZH-Formular und die Wegleitung 2026 sind laut Wiki (Stand 09.11.2026) noch nicht publiziert. Die Ziffer 16.6 und der Code 376 stützen sich auf die Fassung für unterjährige Steuerpflicht. Bitte prüfen Sie beides am definitiven Formular.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q32

**Frage:** SG 2025: Einfamilienhaus (Baujahr 2010), selbst bewohnt. Pauschalabzug Liegenschaftsunterhalt Kanton und Bund?

**Soll (Referenz):** SG 2025: 20 % des Eigenmietwerts, ohne Altersstaffel (sg-stv__art-29); Bund: Gebäude zu Beginn 2025 über 10 Jahre alt → 20 % (bund-lkv__art-5).

**Antwort des Agenten** (26.7 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **SG 2025, Einfamilienhaus Baujahr 2010, selbst bewohnt**
> 
> | | Pauschalabzug | Basis |
> |---|---|---|
> | **Kanton SG** (Staats- und Gemeindesteuer) | **20 %** | angerechneter Eigenmietwert |
> | **Bund** (direkte Bundessteuer) | **20 %** | Eigenmietwert, Gebäude älter als 10 Jahre |
> 
> **Kanton:** SG kennt keine Staffelung nach Gebäudealter. Es gilt immer 20 % (☑️ agent-geprüft, Fundstelle sg-stv__art-29).
> 
> **Bund:** Der Satz hängt vom Gebäudealter zu Beginn der Steuerperiode ab. Das Haus ist 2010 gebaut und am 1.1.2025 rund 15 Jahre alt. Damit gilt die Stufe «mehr als zehn Jahre» mit 20 %. Die Stufe «bis zehn Jahre» (10 %) trifft nicht zu (☑️ agent-geprüft, Fundstelle bund-lkv__art-5).
> 
> **Im Formular:**
> - **Basis:** Das ist der Eigenmietwert nach der Herabsetzung um 30 %, also das Total der Erträge in Formular 7, Teil B. Die Herabsetzung steht in sg-stg-2025__art-34.
> - **Ziffer:** Der Abzug kommt in Formular 7, Teil C, und wird von dort nach Ziff. 15 (Code 716) übertragen.
> - **Bund:** Es gibt keine separate Bundesspalte. Die Steuerbehörde nimmt die Bund-Anpassung automatisch vor (sg-wl-2025__c0173).
> - **Beispiel:** Bei einem angerechneten Eigenmietwert von Fr. 20'000 beträgt der Abzug Fr. 4'000, sowohl für den Kanton als auch für den Bund.
> 
> **Beachten:**
> - Pauschale und effektive Kosten können nicht gemischt werden. Sie wählen pro Liegenschaft und Steuerperiode zwischen der Pauschale und den tatsächlichen Kosten (Formular 7, Rückseite).
> - Mit der Pauschale sind alle Unterhalts- und Verwaltungskosten abgegolten, auch Denkmalpflege sowie Energiespar- und Umweltinvestitionen. Belege müssen Sie dafür nicht einreichen.
> - Effektive Kosten lohnen sich nur, wenn sie 2025 über der Pauschale liegen. Dann sind die Belege auf Verlangen einzureichen.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.
> 
> Ich bin übrigens neu hier als Ihr Assistent. Wie möchten Sie mich nennen?

## q33

**Frage:** ZH 2025: Kind 19 Jahre, in Lehre (Ausbildung). Kinderabzug Kanton und Bund?

**Soll (Referenz):** ZH 2025 Kanton CHF 9'300 (volljährig in Erstausbildung, zh-stg-2025__par-34); Bund CHF 6'800 (bund-dbg-2025__art-35) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (30.3 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__wert):

> **Kinderabzug ZH 2025 für ein 19-jähriges Kind in Lehre: Kanton CHF 9'300, Bund CHF 6'800.**
> 
> | | Kanton (Staatssteuer) | Bund (dir. Bundessteuer) |
> |---|---|---|
> | Kinderabzug | **CHF 9'300** | **CHF 6'800** |
> | Zusätzlicher Versicherungsabzug (Form. 365, Code 613) | CHF 1'300 | CHF 700 |
> 
> Beide Abzüge gelten je Kind, ohne Altersstaffel.
> 
> **Voraussetzungen für das volljährige Kind**
> - **Alter:** Das Kind (Jg. 2006) ist am 31.12.2025 volljährig. Als minderjährig gelten nur die Jahrgänge 2008–2025.
> - **Erstausbildung:** Eine Lehre ist eine berufliche Erstausbildung. Das Kind muss in der Ausbildung stehen und die Eltern müssen den Unterhalt zur Hauptsache bestreiten (Kanton: § 34 StG, Bund: Art. 35 DBG).
> - **Kanton:** Das Kind muss auf die Unterstützung angewiesen sein. Der Lehrvertrag muss mindestens ein halbes Jahr laufen.
> - **Beleg:** Der Lehrvertrag oder eine Schulbestätigung belegt die Ausbildung.
> 
> **Wo eintragen**
> - **Kind im eigenen Haushalt:** Ziff. 24.1, Code 370. Das Kind steht auf Seite 1 unter «Kinder in Ihrem Haushalt», mit Geburtsdatum und Lehrfirma.
> - **Kind ausserhalb des Haushalts:** Code 372. Dort müssen Sie den Hauptunterhalt belegen.
> - **Spalten:** Im Formular gibt es zwei Spalten, Staatssteuer 9'300 und Bundessteuer 6'800.
> - **Versicherungsabzug:** Er steht im Hilfsblatt Form. 365, Teil B Ziff. 3.
> 
> **Sonderfälle**
> - **Nicht zusammenlebende Eltern:** Bei gemeinsamem Sorgerecht ohne Unterhaltsbeiträge gibt es den halben Abzug (4'650 Kanton / 3'400 Bund). Wer Kinderalimente abzieht, bekommt keinen Kinderabzug.
> - **Eigener Lehrlingslohn:** Ob der Unterhalt noch «zur Hauptsache» von den Eltern kommt, hängt davon ab, wie viel das Kind selbst verdient. Das Wiki nennt dafür keine feste Einkommensgrenze, deshalb ist dieser Punkt von der Fachperson zu beurteilen.
> 
> **Bund: zusätzliche Ermässigung**
> Bei der direkten Bundessteuer gibt es zusätzlich eine Ermässigung von CHF 263 je Kind direkt auf den Steuerbetrag (Art. 36 DBG). Sie ist kein Abzug vom Einkommen. Wie sie im ZH-Formular erfasst wird, habe ich nicht geprüft.
> 
> **Stand und Quellen**
> Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen):
> - Kinderabzug Kanton: zh-stg-2025__par-34, zh-form-300-2025__c0010, zh-wl-2025__c0126
> - Kinderabzug Bund: bund-dbg-2025__art-35
> - Versicherungsabzug: zh-stg-2025__par-31-t2, bund-dbg-2025__art-33-t5, zh-form-365-2025__c0002
> - Bundes-Ermässigung 263: bund-dbg-2025__art-36-t4
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.
> 
> Ich bin übrigens euer neuer Assistent. Wie möchtet ihr mich nennen?

## q34

**Frage:** ZH 2025: Lohnausweis Feld G angekreuzt (Kantine). Welche Verpflegungspauschale gilt und in welche Ziffer des Berufsauslagenformulars?

**Soll (Referenz):** Verbilligte Verpflegung: CHF 7.50 pro Arbeitstag, max. CHF 1'600 pro Jahr (LS 631.33, zh-pauschalierung-berufsauslagen-2025__c0004); Form. 360 Ziff. 2.1 (verbilligt); Bund gleich.

**Antwort des Agenten** (26.7 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__beleg):

> **ZH 2025, Lohnausweis mit Feld G angekreuzt**
> 
> **Pauschale:** Es gilt der reduzierte Verpflegungsabzug von **CHF 7.50 pro Arbeitstag, höchstens CHF 1'600 pro Jahr**. Die vollen CHF 15 pro Tag bzw. CHF 3'200 pro Jahr gelten nicht. (☑️ agent-geprüft: `zh-form-360-2025__c0003`, `zh-pauschalierung-berufsauslagen-2025__c0004`)
> 
> **Ziffer:** Hilfsblatt Berufskosten, **Form. 360, Ziff. 2.1 «verbilligt»**.
> - Code **206** für Person 1, Code **226** für Person 2.
> - Ohne Kreuz bei Feld G wäre es Code 208 bzw. 228 (voll).
> 
> **Rechnung:** Code 206 = min(Arbeitstage × 7.50; 1'600). Wer an 220 Tagen auswärts isst, kommt auf 220 × 7.50 = 1'650, der Abzug wird also auf 1'600 gekappt.
> 
> **Kanton und Bund:**
> - Beide Spalten (Staats- und Bundessteuer) erhalten denselben Betrag, mit je CHF 7.50 und CHF 1'600.
> - Die 7.50 sind beim Bund bereits der «halbe Abzug». Nicht nochmals halbieren.
> - Beim Bund gibt es keinen halben Abzug, wenn der Arbeitgeber nur einen Barbeitrag zahlt. Hier gilt aber die Kantine bzw. der Lunch-Check, also der halbe Abzug.
> - Beim Bund entfällt der Abzug mangels Mehrkosten, wenn eine Hauptmahlzeit höchstens CHF 10 kostet. Das habe ich nur in der Wegleitung gefunden und nicht gegen das Formular geprüft.
> 
> **Voraussetzungen:**
> - Der Abzug gilt nur, wenn die Heimkehr in der Mittagspause nicht möglich ist und trotzdem Mehrkosten entstehen.
> - Er ist nicht kumulierbar mit dem vollen Abzug, mit dem Schichtarbeitsabzug (Ziff. 2.2) und mit einer Mittagsheimfahrt.
> - Feld G zählt auch, wenn die Kantine tatsächlich selten genutzt wird.
> - Bei Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt» ist die Folge für den Abzug separat zu prüfen.
> 
> **Zur Quelle:** Die Regel zu Feld G stammt aus der ESTV-Wegleitung zum Lohnausweis in der Fassung 2026 (`bund-wl-lohnausweis-2026__c0012`). Eine 2025er Fassung ist im Wiki nicht vorhanden.
> 
> Die Anzahl Arbeitstage mit auswärtiger Verpflegung brauche ich noch, um den Betrag zu berechnen. Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## q35

**Frage:** SG 2025: Kapitalbezug Säule 3a CHF 100'000. Wird das mit dem übrigen Einkommen besteuert? Wo deklarieren?

**Soll (Referenz):** Nein – Kapitalleistungen aus Vorsorge werden getrennt vom übrigen Einkommen (separate Jahressteuer) besteuert; SG Formular 1 Ziff. 40.1 (Säule 3a), Total Ziff. 41.

**Antwort des Agenten** (28.1 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__rechne):

> **Nein, der Bezug wird nicht mit dem übrigen Einkommen versteuert.** Die Kapitalleistung aus der Säule 3a wird gesondert besteuert, mit einer eigenen vollen Jahressteuer (sg-wl-2025__c0119, sg-stg-2025__art-52; ☑️ agent-geprüft, Abnahme offen).
> 
> **Wo deklarieren (SG 2025, Formular 1, «Weitere Angaben»)**
> - Der Bezug gehört in **Ziff. 40.1**, «aus gebundener Vorsorge Säule 3a». Eintragen: CHF 100'000, bei mehreren Bezügen im Jahr 2025 der Gesamtbetrag (sg-form-1-2025__c0014).
> - Die **Bescheinigung** der Bank oder Versicherung ist beizulegen (Einreichepflicht: ja).
> - **Nicht** in Ziff. 6.4 eintragen. Die Angabe in Ziff. 40 dient nur zur Information. Die separate Steuer wird von der Behörde veranlagt und fliesst nicht in das steuerbare Einkommen ein.
> 
> **Steuer auf den Bezug**
> - **Kanton/Gemeinde (Art. 52 StG SG):**
>   - Die einfache Steuer beträgt 2,0 % für gemeinsam steuerpflichtige Ehegatten und 2,2 % für die übrigen Steuerpflichtigen. Bei CHF 100'000 sind das CHF 2'000 bzw. CHF 2'200.
>   - Der Satz 2,0 % gilt auch für Alleinstehende, die mit Kindern oder Unterstützungsbedürftigen im gleichen Haushalt leben.
>   - Darauf kommen noch der kantonale Steuerfuss und der Gemeindesteuerfuss. Beide habe ich nicht abgefragt, daher nenne ich keine Gesamtbelastung.
>   - Es gibt keine allgemeinen Abzüge und keine Sozialabzüge.
> - **Bund (Art. 38 DBG):** Die Steuer beträgt ein Fünftel der Tarife nach Art. 36 DBG, ohne Sozialabzüge (bund-dbg-2025__art-38). Das Formular hat dafür keine eigene Spalte; die kantonale Erklärung deckt Kanton und Bund.
> 
> **Offen**
> - Die Steuer entsteht im Zeitpunkt des Zuflusses, also hier im Steuerjahr 2025. Das Bezugsdatum habe ich nicht geprüft.
> - Der Fall «Auszahlung in mehreren Jahren» ist nicht geprüft.
> - Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## q36

**Frage:** ZH 2025: Geschiedener Mandant zahlt Unterhaltsbeiträge an die Ex-Frau (CHF 24'000) und für das minderjährige Kind (CHF 12'000). Was ist abziehbar, in welcher Ziffer?

**Soll (Referenz):** Ex-Ehefrau CHF 24'000 voll abziehbar, Ziff. 13.1 (Code 254); Kinderalimente CHF 12'000 abziehbar bis und mit Monat der Volljährigkeit, Ziff. 13.2 (Code 255); Empfänger versteuert; Bund gleich (Art. 33 Abs. 1 lit. c DBG).

**Antwort des Agenten** (28.1 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__zeige, steuerwiki__rechne):

> **Beide Beträge sind abziehbar: CHF 36'000 total (ZH 2025, Staats- und Bundessteuer gleich).** Die Fundstellen sind ☑️ agent-geprüft, die Abnahme ist offen.
> 
> | Zahlung | Ziffer / Code | Abzug |
> |---|---|---|
> | Ex-Frau, CHF 24'000 | **Ziff. 13.1** (Code 254) | CHF 24'000, voll |
> | Minderjähriges Kind, CHF 12'000 | **Ziff. 13.2** (Code 255) | CHF 12'000, voll |
> 
> - **Ex-Frau (13.1):** Beiträge, die für den geschiedenen oder getrennt lebenden Ehegatten persönlich bestimmt sind, können voll abgezogen werden (zh-wl-2025__c0075, zh-form-300-2025__c0007).
> - **Kind (13.2):** Abziehbar sind die Beiträge bis und mit dem Monat, in dem das Kind 18 wird (zh-form-300-2025__c0007, zh-wl-2025__c0076).
> - **Kein Kinderabzug:** Wer Alimente für das minderjährige Kind zahlt, erhält für dieses Kind keinen Kinderabzug (Ziff. 24.1). Den Abzug bekommt also nicht beide Male.
> 
> **Zu prüfen:**
> - Es zählt nur, was 2025 effektiv bezahlt wurde, nicht der vereinbarte Betrag. Die CHF 24'000 und CHF 12'000 müssen also den Zahlungen von 2025 entsprechen.
> - Es sind nur periodische Beiträge abziehbar. Eine Kapitalabfindung gilt als Schuldentilgung und ist nicht abziehbar. Naturalleistungen wie Miete, Krankenkassenprämien oder Schuldzinsen sind gleichgestellt.
> - Beim Bund sind nur familienrechtlich geschuldete, effektiv bezahlte Alimente abziehbar, freiwillige nicht. Das Wiki nennt diese Bundesregel nur bei 13.2; ob sie auch für 13.1 gilt, habe ich nicht geprüft.
> - Wird das Kind 2025 volljährig, sind nur die Zahlungen bis und mit Geburtsmonat bei 13.2 abziehbar. Die Zahlungen danach könnten über den Kinderabzug (Ziff. 24.1) laufen.
> - Belege: Scheidungsurteil oder Konvention sowie die Zahlungsnachweise. Einzureichen sind sie nur auf Verlangen, die Wegleitung nennt keine Beilagepflicht (zh-wl-2025__c0207).
> - Die Ex-Frau versteuert ihre CHF 24'000 in Ziff. 5.1 (Code 160), das Kind seine CHF 12'000 in Ziff. 5.2 (Code 161). Das ist für den Mandanten nur relevant, falls die Gegenseite nachfragt.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.
> 
> Ich bin übrigens dein neuer Assistent. Wie möchtest du mich nennen?

## q37

**Frage:** TG 2025: Mandant bringt Steuerberatungsrechnung, Kreditkartenabrechnung, Mietvertrag und Motorfahrzeugversicherung. Was davon ist relevant?

**Soll (Referenz):** Steuerberatungsrechnung: nein; Motorfahrzeugversicherung: nein; Kreditkartenabrechnung: bedingt (nur als Nachweis/Schuld per 31.12.); Mietvertrag: bedingt (Wochenaufenthalt/Arbeitszimmer/Adressnachweis) – laut belege-relevanz.

**Antwort des Agenten** (31.0 s · Tools: 6 Aufrufe read, steuerwiki__ablage):

> **TG 2025 – kurz: Von den vier Dokumenten ist keines ohne Weiteres ein Steuerbeleg. Kreditkartenabrechnung und Mietvertrag sind nur bedingt relevant, Steuerberatungsrechnung und Motorfahrzeugversicherung nicht.**
> 
> | Dokument | Belegtyp | Steuerrelevant | Einreichen (TG 2025) | Kategorie (KATEGORIEN.md) | Unsicherheit |
> |---|---|---|---|---|---|
> | Steuerberatungsrechnung | Rechnung Steuerberatung / Ausfertigung Steuererklärung | **Nein** ☑️. Im Privatvermögen nicht abziehbar. Beim Bund sind Steuerberatungskosten ausdrücklich nicht zulässig (`bund-wl-2a-2025__c0057`). | – | Keine Steuerbeleg-Kategorie | Typerkennung nur «tief» (4 vs. 1 Punkte): Rechnung kurz prüfen. Falls sie zu einer Liegenschaft oder zu Wertschriften gehört, neu beurteilen. |
> | Kreditkartenabrechnung | Kreditkartenabrechnung | **Bedingt** ☑️. Die Abrechnung selbst ist kein Beleg. Sie zählt nur als Nachweisquelle für einzelne abziehbare Zahlungen (z.B. Spenden, Arzt-/Zahnarztkosten, Weiterbildung, Berufsauslagen), wenn die Originalrechnung fehlt, oder für Sollzinsen (Form. 4.1 A). | **Unklar** | **Belege Sonstiges** (unklar wird wie «nicht einreichen» behandelt) | Typ «mittel». Die Einreichepflicht ist im Wiki nicht klar belegt. Nur ablegen, wenn einzelne Posten tatsächlich in die Erklärung einfliessen. |
> | Mietvertrag | Mietvertrag Wohnung | **Bedingt** ☑️. Miete der selbstbewohnten Wohnung ist Lebenshaltungsaufwand und nicht abziehbar (Art. 34 lit. a DBG). Relevant nur bei Untervermietung, Wochenaufenthalt am Arbeitsort oder Geschäftsräumen/Home-Office (siehe Zimmerberechnung `tg-wl-2025__c0189`). | **Unklar** | Wenn relevant: **Belege Sonstiges**. Sonst keine Steuerbeleg-Kategorie. | Bedingung aus der Anfrage nicht prüfbar. Beim Mandanten klären: Untervermietung? Wochenaufenthalt? Home-Office? |
> | Motorfahrzeugversicherung | Motorfahrzeug-Versicherungspolice (Haftpflicht/Kasko) | **Nein** ☑️. Prämien, Verkehrssteuern, Treibstoff und Unterhalt des Privatfahrzeugs sind Lebenshaltungskosten (`tg-wl-2025__c0123`). | – | Keine Steuerbeleg-Kategorie. Eine Krankenkassen-Prämienbescheinigung wäre etwas anderes. | Typ «hoch». |
> 
> **Fazit:**
> - **Relevant:** nur bedingt die Kreditkartenabrechnung und der Mietvertrag. Beide gehören, falls die Bedingung erfüllt ist, nach **Belege Sonstiges**.
> - **Nicht relevant:** Steuerberatungsrechnung und Motorfahrzeugversicherung. Nicht ablegen und nichts erfassen.
> - **Rückfragen an den Mandanten:**
>   - Zur Kreditkarte: Gibt es Posten, die abziehbar sein könnten, und fehlen dazu die Originalbelege?
>   - Zum Mietvertrag: Gibt es Untervermietung, einen Wochenaufenthalt oder Home-Office?
> - **Zu beachten:** Alle Wiki-Aussagen sind «agent-geprüft», die Abnahme steht aus. Die Zuordnungen der Kategorienliste sind laut Datei ebenfalls noch unbestätigt. Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Ich bin übrigens euer neuer Assistent. Wie möchtet ihr mich nennen?

## q38

**Frage:** AR 2026: Wie hoch ist der Kinderabzug für ein 10-jähriges Kind? Ist der Wert gesichert?

**Soll (Referenz):** AR 2026: CHF 7'400 laut Anhang 1 StG (indexiert), aber Status STRITTIG (MB 02 / StG-Text nennen andere Beträge; Wegleitung 2026 fehlt) → Fachperson.

**Antwort des Agenten** (26.3 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__zeige, steuerwiki__position):

> **AR 2026, Kinderabzug für ein 10-jähriges Kind: CHF 7'400 (Staats- und Gemeindesteuer).** Das ist die Stufe «nach Vollendung des 4. bis zur Vollendung des 15. Altersjahrs», Formular-Ziff. 23.2.
> 
> **Gesichert ist der Wert nicht.** Das Wiki führt ihn als ⚠️ strittig, weil sich die Quellen widersprechen:
> 
> | Quelle | Betrag |
> |---|---|
> | Anhang 1 StG, Art. 38 Abs. 1 lit. a Ziff. 2 (indexiert per 1.1.2024), `ar-stg-anhang-kp__c0001` | **CHF 7'400** |
> | Wegleitung AR 2025 (Kurzübersicht Ziff. 23), `ar-wl-2025__c0005` | CHF 7'400 (bestätigt die Anhang-Werte, aber nur für 2025) |
> | Merkblatt MB AR 02 (Stand 18.08.2026, Ziff. 2), `ar-mb-02__c0002` | CHF 7'000 (nicht indexierter Gesetzestext) |
> 
> - **Was für 7'400 spricht:** Der Anhang ist Teil des Gesetzes und nach Art. 39a StG massgeblich. Die Wegleitung 2025 stützt ihn ebenfalls.
> - **Was fehlt:** Die Wegleitung 2026 und das Formular 2026 sind noch nicht publiziert (Stand 09.11.2026). Ob AR 2026 tatsächlich 7'400 oder die 7'000 aus dem Merkblatt anwendet, ist deshalb nicht belegt. Die Zeile Ziff. 23.2 im Wiki ist noch ⬜ offen.
> - **Mein Vorschlag:** Rechne vorläufig mit CHF 7'400. Die Differenz von CHF 400 ist klein. Die endgültige Beurteilung liegt bei der Fachperson, bis die Wegleitung 2026 vorliegt.
> 
> **Weitere Werte für dasselbe Kind:**
> - **Kanton, Vermögensfreibetrag:** CHF 25'000 pro minderjähriges Kind (☑️ agent-geprüft, Art. 51 StG).
> - **Kanton, Versicherungsabzug:** Zuschlag von CHF 1'000 pro Kind (☑️ agent-geprüft, Art. 35 StG).
> - **Bund (direkte Bundessteuer):**
>   - Kinderabzug: einheitlich CHF 6'800, ohne Altersstaffelung (☑️ agent-geprüft, Art. 35 DBG, `bund-dbg-2026__art-35`).
>   - Versicherungsabzug: Zuschlag von CHF 700 pro Kind (☑️ agent-geprüft).
>   - Steuerbetrag: Ermässigung um CHF 263 pro Kind (☑️ agent-geprüft, Art. 36 DBG, `bund-dbg-2026__art-36-t4`).
> 
> Die Bundeswerte sind nicht strittig. Der Status «agent-geprüft» heisst, die Fundstelle ist geprüft und die Abnahme steht noch aus.

## q39

**Frage:** Welche Vermögenssteuer-Freibeträge (Sozialabzüge) gelten 2025 in ZH für Alleinstehende und Verheiratete?

**Soll (Referenz):** ZH kennt keine Vermögens-Sozialabzüge, sondern Tarifstufen mit 0 ‰: Grundtarif erste CHF 80'000, Verheiratetentarif erste CHF 159'000 (zh-stg-2025__par-47); kein Betrag pro Kind.

**Antwort des Agenten** (22.5 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **ZH, Steuerjahr 2025: steuerfreies Vermögen (Staats- und Gemeindesteuer)**
> 
> | Haushalt | Steuerfrei (0 ‰-Stufe) |
> |---|---|
> | Alleinstehend (Grundtarif) | **CHF 80'000** |
> | Verheiratet (Verheiratetentarif) | **CHF 159'000** |
> 
> Quelle: § 47 StG ZH, Stand 1.1.2025 (Nachtrag 127), Chunks `zh-stg-2025__par-47-t1` und `zh-stg-2025__par-47-t2`. Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Was das praktisch heisst**
> - Es ist kein Sozialabzug im eigentlichen Sinn. Das Formular 300 hat dafür keine Zeile.
> - Man trägt das volle Vermögen ein: Ziff. 35 = Ziff. 33 − Ziff. 34. Der Freibetrag wirkt erst bei der Steuerberechnung, als erste Tarifstufe mit 0 ‰.
> - Der Verheiratetentarif gilt auch für Verwitwete, Getrennte, Geschiedene und Ledige, die mit Kindern im Sinn von § 34 Abs. 1 lit. a zusammenleben (§ 47 Abs. 2).
> - Bei Eltern, die nicht gemeinsam besteuert werden und je den halben Kinderabzug erhalten, gilt der Verheiratetentarif nur für den Elternteil, der den Kindesunterhalt hauptsächlich trägt.
> - Massgebend sind die Verhältnisse am Ende der Steuerperiode (§ 47 Abs. 3 StG).
> - Einen zusätzlichen Vermögensfreibetrag pro Kind gibt es in ZH nicht.
> 
> **Bund:** Die direkte Bundessteuer erhebt keine Vermögenssteuer. Es gibt also keinen Bundeswert.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## q40

**Frage:** Alleinstehende TG 2026, Nettolohn 90'000, ÖV-Abo 2'400, Säule 3a 7'258, Krankenkasse 5'500. Erstelle die Abzüge (Berufskosten, 3a, Versicherungsabzug) Kanton und Bund mit Fundstellen und Status.

**Soll (Referenz):** TG 2026 (Kanton/Bund): Fahrkosten 2'400 (Max. 6'000 / 3'300); übrige Berufskosten 3 % von 90'000 = 2'700 (Min. 2'000, Max. 4'000, beide Ebenen); Säule 3a 7'258 (TG 🟡 extrahiert, Bund ☑️); Versicherungsabzug TG max. 3'500 → 3'500, Bund max. 1'800 → 1'800 (Prämien 5'500 übersteigen beide Maxima).

**Antwort des Agenten** (45.2 s · Tools: 10 Aufrufe read, steuerwiki__formular, steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> # Abzüge TG 2026, alleinstehend (Kanton und Bund)
> 
> Die Beträge stehen auf Formular 1 (Ziff. 10.1, 13.1, 14) in der linken Spalte (Staat) und der rechten Spalte (Bund). Alle Werte haben den Status ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen. Gerechnet habe ich mit `rechne`.
> 
> ## Ergebnis
> 
> | Ziff. (Code) | Abzug | Kanton | Bund |
> |---|---|---|---|
> | 10.1 (240) | Berufskosten (Form. 4.2, Ziff. 7) | **5'100** | **5'100** |
> | 13.1 (314) | Säule 3a | **7'258** | **7'258** |
> | 14 (330) | Versicherungsprämien (Form. 5.2) | **3'500** | **1'800** |
> | | **Summe der drei Abzüge** | **15'858** | **14'158** |
> 
> ## Herleitung
> 
> **Berufskosten (Ziff. 10.1, Form. 4.2)**
> - Fahrkosten (Ziff. 2.1 / 2.5): Das ÖV-Abo von 2'400 liegt unter dem Maximum, das im Kanton bei 6'000 und beim Bund bei 3'300 liegt. Damit sind 2'400 abziehbar, in beiden Spalten gleich. Fundstellen: tg-wl-2026__c0177 (tatsächliche Abokosten), tg-wl-2026__c0176 (Kanton max. 6'000), bund-dbg-2026__art-26 (Bund max. 3'300).
> - Übrige Berufskosten (Ziff. 4): 3 % × 90'000 = 2'700. Das liegt zwischen Minimum 2'000 und Maximum 4'000. Der Bundessatz stammt aus dem Positionsergebnis (tg-form-01-2026__c0010). Für die 3 %-Pauschale selbst habe ich keinen Chunk separat geöffnet.
> - Total: 2'400 + 2'700 = 5'100.
> 
> **Säule 3a (Ziff. 13.1)**
> - 7'258 sind in voller Höhe abziehbar, Kanton und Bund gleich. Das ist das Maximum mit Pensionskasse (2. Säule).
> - Fundstellen: tg-wl-2026__c0089 (Kanton), bund-bsv-masszahlen-2025-2026__c0003 (Bund).
> - Mit Pensionskasse liegt der Abzug genau auf dem Maximum. Ohne Pensionskasse wären bis 20 % × 90'000 = 18'000 möglich, höchstens 36'288. Die 7'258 sind in beiden Fällen voll abziehbar.
> - Die Bescheinigung der Säule 3a ist immer einzureichen (tg-wl-2026__c0034).
> 
> **Versicherungsabzug (Ziff. 14, Form. 5.2)**
> - Die Krankenkassenprämie von 5'500 übersteigt beide Maxima. Der Abzug ist daher gedeckelt: Kanton 3'500 (tg-stg__par-34-t3), Bund 1'800 (bund-dbg-2026__art-33-t2).
> - Der erhöhte Bundesabzug von 2'700 gilt nur ohne Beiträge an die 2. Säule oder Säule 3a (bund-dbg-2026__art-33-t5). Mit 3a-Beitrag gilt er nicht.
> - Die 5'500 müssen die Nettoprämie nach Abzug der Prämienverbilligung (IPV) sein. Die Maxima liegen so weit darunter, dass sich am Ergebnis nichts ändert, solange die Nettoprämie über 3'500 liegt.
> 
> ## Offene Punkte
> 1. **Verpflegung (Ziff. 3.1):** Dazu haben Sie nichts angegeben, deshalb ist sie nicht enthalten. Wenn Sie über Mittag nicht nach Hause fahren können und keine Verbilligung erhalten, kommt dazu: 15 × 225 Tage = 3'375, gedeckelt auf **3'200**. Dann betragen die Berufskosten 8'300, die Summe 19'058 im Kanton und 17'358 beim Bund. Bei Kantine oder Verbilligung sind es 7.50 pro Tag, höchstens 1'600. Bitte klären Sie, ob die Verpflegung zutrifft.
> 2. **Lohnausweis Feld F:** Es darf nicht angekreuzt sein. Sonst entfällt der Fahrkostenabzug (tg-form-04-2-2026__c0001). Die 2'400 gelten bei Vollzeit mit 225 Arbeitstagen. Bei Teilzeit oder unterjähriger Tätigkeit wäre die Pauschale zu kürzen.
> 3. **Nettolohn:** Die 90'000 nehme ich als Lohnausweis Ziff. 11. Sie sind die Basis für die 3 %-Pauschale.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Ich bin neu hier. Wie möchten Sie mich nennen?

