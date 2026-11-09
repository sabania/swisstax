# OpenClaw-Testlauf: blindtest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 14 · Lauf: 2026-11-09 18:35
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## b01

**Frage:** Ehepaar in rechtlich und tatsächlich ungetrennter Ehe, weder Beiträge an die 2. Säule noch an die Säule 3a, Kanton ZH, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Zinsen von Sparkapitalien bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2025: Staatssteuer höchstens CHF 8'700 (Grundabzug CHF 5'800, ohne Beiträge an 2. Säule/3a um die Hälfte erhöht). Direkte Bundessteuer 2025: höchstens CHF 5'550 (Grundabzug CHF 3'700, um die Hälfte erhöht).

**Antwort des Agenten** (26.4 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__wert):

> **ZH · Steuerjahr 2025: Versicherungsprämien und Zinsen von Sparkapitalien (Ziff. 15, Code 270)**
> 
> Das Ehepaar lebt in ungetrennter Ehe und leistet weder Beiträge an die 2. Säule noch an die Säule 3a. Deshalb gilt der erhöhte Maximalabzug («ohne 2./3a»): Der Abzug erhöht sich um die Hälfte.
> 
> | | Maximalabzug (Ehepaar, ohne 2./3a) | Grundbetrag mit 2./3a |
> |---|---|---|
> | **Staatssteuer ZH** | **CHF 8'700** | CHF 5'800 |
> | **Direkte Bundessteuer** | **CHF 5'550** | CHF 3'700 |
> 
> - **Staatssteuer:** CHF 8'700, die Fundstelle ist zh-wl-2025__c0086. Der Grundbetrag von CHF 5'800 steht in § 31 StG (zh-stg-2025__par-31-t2).
> - **Bund:** CHF 5'550, die Fundstelle ist bund-dbg-2025__art-33-t5 (Art. 33 DBG).
> - Alle Werte sind ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> 
> **Zur Anwendung im Formular**
> - Der Abzug ist ein Maximalbetrag. Abgezogen wird der tiefere Betrag von A und B, je Spalte (Staat und Bund).
> - A ist die Summe der tatsächlich bezahlten Prämien und Sparzinsen nach Form. 365 (Codes 601–604), abzüglich erhaltener Prämienverbilligung (605). B ist der Maximalabzug aus der Tabelle.
> - Der Maximalbetrag wird nur gewährt, wenn kein Ehegatte und kein Arbeitgeber Beiträge an die 2. Säule oder die Säule 3a geleistet hat. Sonst gelten CHF 5'800 (Staat) und CHF 3'700 (Bund).
> - Kinder sind in der Frage nicht erwähnt und in den Beträgen oben nicht enthalten. Je Kind oder unterstützungsbedürftiger Person kommen CHF 1'300 (Staat) bzw. CHF 700 (Bund) dazu.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## b02

**Frage:** Wie hoch ist im Steuerjahr 2026 der Maximalabzug für Fahrkosten zwischen Wohn- und Arbeitsort im Kanton St.Gallen (Kantons- und Gemeindesteuern) und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2026: Kantons- und Gemeindesteuern max. Fr. 8'000; direkte Bundessteuer max. Fr. 3'300. Es ist ein Maximalabzug, keine Pauschale (bei Teilzeit/unterjährig nicht gekürzt).

**Antwort des Agenten** (26.9 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__zeige):

> **St. Gallen · Steuerjahr 2026 – Maximalabzug Fahrkosten Wohn-/Arbeitsort**
> 
> | | Maximalabzug | Fundstelle | Status |
> |---|---|---|---|
> | **Kanton SG** (Staats- und Gemeindesteuer) | **CHF 8'000** | Art. 39 Abs. 1 lit. a StG SG (`sg-stg-2026__art-39`): «bis zum Betrag von Fr. 8000.–» | ☑️ agent-geprüft (Abnahme offen) |
> | **Direkte Bundessteuer** | **CHF 3'300** | Art. 26 Abs. 1 lit. a DBG (`bund-dbg-2026__art-26`): «bis zu einem Maximalbetrag von 3300 Franken» | ☑️ agent-geprüft (Abnahme offen) |
> 
> Im SG-Formular 2026 gehört der Abzug zu Ziff. 10.1 (Person 1) bzw. 10.2 (Person 2), Berufskosten bei unselbständiger Erwerbstätigkeit.
> 
> **Zum Rechnen**
> - Es ist ein Maximalabzug und keine Pauschale. Abgezogen werden die tatsächlichen, notwendigen Kosten bis zur Obergrenze.
> - Beim Kanton gilt die Grenze von CHF 8'000 für Haupt- und Nebenerwerb zusammen. Sie wird bei unterjähriger Steuerpflicht oder Teilzeit nicht gekürzt (`sg-stb-39-3`).
> - Beim Bund gilt die Grenze von CHF 3'300 pro Person. Die Kosten über CHF 3'300 sind beim Bund nicht abzugsfähig. Dieser Punkt ist belegt, aber nicht weiter vertieft.
> - Ansätze 2026 für das private Auto: 75 Rappen pro km (2025: 70 Rappen), sofern kein öffentliches Verkehrsmittel zur Verfügung steht oder zumutbar ist (Kanton und Bund). Die Velo-Pauschale beträgt in beiden Fällen CHF 700. Bei Motorrädern gelten im Kanton 75 Rappen pro km, beim Bund 40 Rappen pro km.
> 
> **Offener Punkt:** Die kantonale Weisung StB 39 Nr. 3 nennt für 2026 neben den CHF 8'000 eine zweite Spalte mit CHF 3'300. Der Quellentext erklärt nicht, was diese bedeutet. Ich habe sie nicht als kantonalen Wert übernommen. Sie entspricht aber dem Betrag der direkten Bundessteuer. Für die Kantons- und Gemeindesteuer gilt nach Gesetzestext CHF 8'000.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## b03

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Welchen Kinderabzug können Eltern für ein 3-jähriges, ein 10-jähriges und ein 16-jähriges (noch minderjähriges) Kind geltend machen?

**Soll (Referenz):** AR (Kantonssteuer) 2025, indexierte Beträge gemäss Anhang 1 StG (bestätigt durch WL AR 2025 Ziff. 23): 3-jähriges Kind (bis Vollendung des 4. Altersjahrs) Fr. 5'300; 10-jähriges Kind (nach Vollendung des 4. bis Vollendung des 15. Altersjahrs) Fr. 7'400; 16-jähriges Kind (nach Vollendung des 15. Altersjahrs bis Volljährigkeit) Fr. 11'600. Gleiche Beträge für volljährige Kinder in Ausbildung bis zum 26. Altersjahr. (Korrigiert nach Bewertung Lauf A: die ursprüngliche Referenz nannte die nicht indexierten Merkblatt-Beträge 5'000/7'000/11'000.)

**Antwort des Agenten** (31.2 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Appenzell Ausserrhoden · Steuerjahr 2025**
> 
> Der Kinderabzug in AR hängt vom Alter am Stichtag 31. Dezember 2025 ab (Art. 38 Abs. 1 lit. a StG AR). Alle Werte sind ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> 
> | Kind | Stufe | Formularziffer | Kanton (Staats- und Gemeindesteuer) |
> |---|---|---|---|
> | 3-jährig | bis zur Vollendung des 4. Altersjahrs | 23.1 | **CHF 5'300** |
> | 10-jährig | nach Vollendung des 4. bis zur Vollendung des 15. Altersjahrs | 23.2 | **CHF 7'400** |
> | 16-jährig (minderjährig) | nach Vollendung des 15. Altersjahrs bis zur Volljährigkeit | 23.3 | **CHF 11'600** |
> | **Total Kanton** | | | **CHF 24'300** |
> 
> Fundstellen: `ar-wl-2025__c0005`, `ar-stg-anhang-kp__c0001`.
> 
> **Bund (direkte Bundessteuer)**
> - Der Bund staffelt nicht nach Alter. Er gewährt CHF 6'800 pro Kind, bei drei Kindern also **CHF 20'400** (`bund-dbg-2025__art-35`).
> - Zusätzlich ermässigt sich der Steuerbetrag um CHF 263 pro Kind, also um **CHF 789** (`bund-dbg-2025__art-36-t4`).
> - Das AR-Formular hat keine eigene Bundesspalte. Die Steuerverwaltung nimmt die Bundesabweichungen automatisch vor (`ar-wl-2025__c0179`).
> 
> **Voraussetzungen und Hinweise**
> - Die Eltern müssen den Unterhalt des Kindes zur Hauptsache bestreiten. Das Kind muss auf diesen Unterhalt angewiesen sein.
> - Es dürfen keine Unterhaltsbeiträge nach Ziff. 12.2 für dieses Kind abgezogen werden.
> - Kein Kinderabzug gibt es, wenn die Einkünfte des Kindes CHF 18'000 übersteigen (inkl. CHF 6'000 frei verfügbar) oder sein Reinvermögen über CHF 250'000 liegt. Die Einkünfte-Grenze steht ausdrücklich bei 23.1/23.2, die Vermögensgrenze bei 23.3. Ob beide Grenzen auch für die 23.1/23.2-Stufen gelten, habe ich nicht geprüft.
> - Getrennt besteuerte Eltern mit gemeinsamer Sorge und ohne Unterhaltsbeiträge erhalten den Abzug je zur Hälfte.
> - Die Gesetzestexte nennen noch die nicht indexierten Beträge (5'000, 7'000 und 11'000). Massgebend sind die indexierten Beträge nach Anhang 1 zum StG und der Wegleitung 2025, wie in der Tabelle.
> 
> **Weitere kinderbezogene Positionen, die Sie ebenfalls prüfen sollten** (nicht Teil der Frage)
> - Der Versicherungsabzug erhöht sich um CHF 1'000 pro Kind (Kanton) bzw. CHF 700 (Bund).
> - Beim Vermögen gibt es einen zusätzlichen Freibetrag von CHF 25'000 pro minderjähriges Kind mit Kinderabzug (`ar-stg__art-51`).
> - Die Kinderbetreuungskosten sind separat zu beurteilen. Das habe ich hier nicht geprüft.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## b04

**Frage:** Alleinstehende Person ohne Kinder mit Beiträgen an die 2. Säule, Kanton Thurgau, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Staats-/Gemeindesteuern und bei der Bundessteuer?

**Soll (Referenz):** TG 2025: Staat max. Fr. 3'500, Bund max. Fr. 1'800 (ohne Beiträge an Säule 2/3a würde beim Bund Fr. 2'700 gelten). Betrag vor Abzug Prämienverbilligungen Krankenkassen.

**Antwort des Agenten** (25.0 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Thurgau · Steuerjahr 2025** (alleinstehend, keine Kinder, mit Beiträgen an die 2. Säule)
> 
> | | Maximaler Abzug | Fundstelle |
> |---|---|---|
> | **Staats-/Gemeindesteuern** | **CHF 3'500** | tg-stg__par-34-t3, «b. Fr. 3'500 für die übrigen Steuerpflichtigen» |
> | **Direkte Bundessteuer** | **CHF 1'800** | bund-dbg-2025__art-33-t2, «1800 Franken für die übrigen Steuerpflichtigen» |
> 
> Beide Werte sind ☑️ agent-geprüft: die Fundstelle ist geprüft, die Abnahme steht noch aus.
> 
> - **Erhöhter Bundesansatz:** Der höhere Bundesbetrag von CHF 2'700 gilt nur für Personen ohne Beiträge an die Säule 2 oder 3a. Weil hier Beiträge an die 2. Säule geleistet werden, gilt der ordentliche Ansatz von CHF 1'800. Die beiden Ansätze lassen sich nicht kombinieren.
> - **Kinderzuschläge:** Sie entfallen, weil es keine Kinder gibt (sonst Kanton +CHF 1'000, Bund +CHF 700 je Kind).
> - **Berechnung:** Abgezogen wird der niedrigere Betrag aus den effektiven Prämien und Sparzinsen und dem Maximum. Im Formular steht das Ergebnis in Ziff. 14 (Code 330), mit der Berechnung im Hilfsblatt Formular 5.2. Der Kanton nutzt die linke, der Bund die rechte Spalte.
> - **Krankenkassenprämien:** Sie zählen netto, also nach Abzug der erhaltenen Prämienverbilligung. Ohne Deklaration der Krankenkassenprämien kann der Abzug ganz entfallen.
> - **Unfallversicherung:** Prämien für die Nichtberufsunfallversicherung (NBUV) gehören nicht hierher, sondern in Ziff. 15.4.

## b05

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wie hoch ist der Kinderabzug für ein noch nicht schulpflichtiges Kind und für ein Kind in Schule oder Ausbildung bei den Kantons-/Gemeindesteuern?

**Soll (Referenz):** SG 2025: noch nicht schulpflichtiges Kind Fr. 7'600 (Ziff. 23.1); Kind in Schule oder Ausbildung (auch volljährig) Fr. 10'800 (Ziff. 23.2).

**Antwort des Agenten** (25.9 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Kanton St. Gallen · Steuerjahr 2025 – Kinderabzug bei den Kantons- und Gemeindesteuern**
> 
> | Kind | Formular-Ziffer (Code) | Abzug |
> |---|---|---|
> | Noch nicht schulpflichtig | Ziff. 23.1 (Code 252) | **Fr. 7'600** |
> | In Schule oder Ausbildung | Ziff. 23.2 (Code 254) | **Fr. 10'800** |
> 
> Beide Beträge gelten pro Kind. Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Quellen**
> - Gesetz: sg-stg-2025__art-48
> - Formular 1: sg-form-1-2025__c0011
> - Wegleitung: sg-wl-2025__c0104 (Ziff. 23.1)
> 
> **Voraussetzungen und Hinweise**
> - **Vorschulkind (23.1):**
>   - Das Kind steht unter der elterlichen Sorge oder Obhut.
>   - Massgebend sind die Verhältnisse am 31.12.2025. Bei unterjähriger Steuerpflicht wird der Abzug anteilig gewährt.
>   - Der Kindergarten zählt bereits zur Schulpflicht, dann gilt Ziff. 23.2.
> - **Kind in Schule oder Ausbildung (23.2):**
>   - Der Abzug gilt ab Kindergarten.
>   - Er gilt auch für volljährige Kinder in schulischer oder beruflicher Ausbildung.
>   - Voraussetzung ist, dass Sie zur Hauptsache für den Unterhalt aufkommen.
> - **Kein Abzug**, wenn für das Kind Unterhaltsbeiträge nach Ziff. 12.2 abgezogen werden.
> - **Zusätzlich bei Kindern in Ausbildung (Ziff. 23.3, Code 256):**
>   - Sie können die effektiven, selbst getragenen Ausbildungskosten abziehen, soweit sie nach Abzug von Stipendien den Selbstbehalt von Fr. 3'200 übersteigen.
>   - Höchstens Fr. 13'700 je Kind, nur Kanton und Gemeinde.
>   - Voraussetzung ist, dass der Abzug nach Ziff. 23.2 gilt.
> 
> **Zum Vergleich: Bund (direkte Bundessteuer)**
> - Der Bund kennt keine Altersstaffel. Es gilt ein einheitlicher Kinderabzug von Fr. 6'800 pro Kind (bund-dbg-2025__art-35).
> - Zusätzlich ermässigt sich der Steuerbetrag um Fr. 263 pro Kind (bund-dbg-2025__art-36-t4).
> - Im SG-Formular gibt es nur eine Spalte. Die Behörde nimmt die Anpassung für den Bund automatisch vor.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## b06

**Frage:** Bis wann ist die Steuererklärung 2025 einer natürlichen Person im Kanton Zürich einzureichen, und wie ist vorzugehen, wenn die Frist nicht eingehalten werden kann?

**Soll (Referenz):** ZH, Steuerperiode 2025: Einreichung bis 31. März 2026 (online oder an das Scan-Center). Gesuch um Fristerstreckung ist vor Ablauf der Frist beim Gemeindesteueramt zu stellen. Mahnfristen sind nicht erstreckbar.

**Antwort des Agenten** (31.0 s · Tools: 7 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Zürich · Steuerjahr 2025**
> 
> **Frist**
> - Die Steuererklärung 2025 ist bis **31. März 2026** einzureichen, online oder beim Scan-Center. Das gilt für Staats- und Gemeindesteuer sowie für die direkte Bundessteuer. Der Bund hat keine eigene Frist, der Kanton bestimmt sie. ☑️ (zh-wl-2025__c0017)
> - Heute ist der 9. November 2026. Die ordentliche Frist ist also abgelaufen. Eine erstreckte Frist läuft längstens bis 30. November 2026 (siehe unten).
> 
> **Wenn die Frist nicht eingehalten werden kann**
> 1. **Gesuch um Fristerstreckung vor Fristablauf** beim Gemeindesteueramt stellen (zh-wl-2025__c0017, § 39 Abs. 1 StV ZH).
> 2. Rechtzeitige Gesuche werden längstens bis **30. November 2026** bewilligt (zh-zstb-132-1__c0024). Es braucht keinen besonderen Grund. Nach der Wegleitung genügen «irgendwelche Gründe».
> 3. Von Amtes wegen wird die Frist bis **30. September 2026** erstreckt für im Kanton wohnhafte Selbständigerwerbende, für Personen, die einer Branchenabteilung zugewiesen sind, und für Steuerpflichtige mit Wohnsitz ausserhalb des Kantons (zh-zstb-132-1__c0023). Ein Gesuch ist dann nicht nötig. Entscheide des Wohnsitzkantons gelten auch für ZH, wenn sie dem zuständigen Gemeindesteueramt vor Fristablauf mitgeteilt werden (zh-wl-2025__c0017).
> 4. Bei Verweigerung der Erstreckung kann man Aufsichtsbeschwerde an die Finanzdirektion erheben (§ 39 Abs. 2 StV ZH).
> 
> **Wenn die Frist bereits abgelaufen ist**
> - **Fristerstreckungsgesuche nach Fristablauf werden abgewiesen**. Eine abgelaufene Frist kann nicht mehr erstreckt werden. Möglich ist nur die **Wiederherstellung der Frist** nach § 15 StV bzw. Art. 119 Abs. 2 und 124 Abs. 4 DBG, wenn deren Voraussetzungen erfüllt sind. Zuständig ist das Gemeindesteueramt (zh-zstb-132-1__c0024). Die Voraussetzungen habe ich nicht geprüft.
> - **Mahnung:** Wer die Steuererklärung nicht innert der ordentlichen oder erstreckten Frist einreicht, wird gemahnt (zh-zstb-132-1__c0029).
>   - Die Mahnfrist beträgt **10 Tage** und ist **nicht erstreckbar**.
>   - Bei Nichtabgabe droht eine **Einschätzung nach pflichtgemässem Ermessen** und eine **Ordnungsbusse** (§ 234 StG bzw. Art. 174 DBG).
>   - Die Mahnung ist gebührenfrei.
> 
> **Offene Punkte**
> - Ob eine Fristerstreckung etwas kostet, steht in den Quellen nicht.
> - Im Wiki-Eckwert ist vermerkt, dass das erste Gesuch ohne gegenteiligen Entscheid als stillschweigend bewilligt gilt. Die Fundstelle dazu habe ich nicht im Wortlaut geöffnet. Verlassen Sie sich deshalb nicht darauf und holen Sie die Bewilligung ein.
> - Der Status aller Angaben ist ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen. Die fachliche Beurteilung bleibt bei der Fachperson.

## b07

**Frage:** Wir sind eine Treuhandfirma und brauchen für Mandanten im Kanton Thurgau (Steuerperiode 2025, natürliche Personen) eine Fristerstreckung. Bei welcher Stelle ist das Gesuch einzureichen und bis wann kann die Frist längstens erstreckt werden?

**Soll (Referenz):** TG: Gesuch beim Gemeindesteueramt, das darüber entscheidet. Erstmals eingereichte Gesuche werden grundsätzlich bis längstens 30. September des Deklarationsjahres (2026) gutgeheissen; zusätzliche Gesuche in begründeten Fällen bis 30. November. Treuhänder/Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen, können für ihre Mandanten ein Gesuch längstens bis 31. Dezember des Deklarationsjahres beantragen. Arbeitsüberlastung ist kein Grund.

**Antwort des Agenten** (32.0 s · Tools: 7 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Kanton Thurgau · Steuerjahr 2025 · natürliche Personen**
> 
> **Zuständige Stelle:** Das Gesuch geht an das **Gemeindesteueramt** und nicht an die kantonale Steuerverwaltung. Gemeint ist das Steueramt der Wohnsitzgemeinde, bei Ausserkantonalen die Liegenschafts- oder Betriebsstättengemeinde. Das Gemeindesteueramt entscheidet auch darüber. Das Gesuch ist schriftlich, begründet und rechtzeitig vor Ablauf der angesetzten Frist zu stellen. (StP 155 Nr. 2, Ziff. 1, `tg-stp-155-2__c0001`; WL TG 2025, `tg-wl-2025__c0023`)
> 
> **Längste Erstreckung:**
> - **Treuhänder und Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen,** können für ihre Mandanten die Erstreckung **längstens bis zum 31. Dezember des Deklarationsjahres** beantragen. (`tg-stp-155-2__c0002`)
> - Für die Steuerperiode 2025 ist das Deklarationsjahr 2026. Die Frist läuft also **längstens bis 31. Dezember 2026**.
> - Private ohne Vertretung erhalten nur kürzere Fristen:
>   - Erstgesuch grundsätzlich bis 30. September 2026.
>   - Weitere Gesuche in begründeten Fällen bis 30. November 2026.
> - Über den 30. November hinaus werden Gesuche abgewiesen, ausser es werden ausserordentliche Gründe glaubhaft gemacht. Dafür braucht es eine substanziierte Sachdarstellung. Allgemeine Hinweise wie starke berufliche Inanspruchnahme oder fehlende Unterlagen genügen nicht. (`tg-stp-155-2__c0002`)
> - Arbeitsüberlastung ist kein Grund für eine Fristverlängerung. (`tg-stp-155-2__c0001`)
> 
> **Weitere Punkte:**
> - **Entscheid:** Er wird schriftlich eröffnet. Wenn Sie als Vertreter das Gesuch stellen, geht er an Sie. Eine verweigerte Fristverlängerung ist ein Zwischenentscheid und kann nicht selbständig angefochten werden. (`tg-stp-155-2__c0005`)
> - **Gebühren (§ 39b StV TG, `tg-stv__par-39b`):**
>   - Die erstmalige Erstreckung ist gebührenfrei.
>   - Jedes weitere Gesuch kostet eine Kanzleigebühr von Fr. 30.
>   - Die Fr. 30 stehen im Verordnungstext ohne Beschränkung auf juristische Personen. Die Einordnung in unserem Wiki-Eckwert, wonach die Gebühr nur für juristische Personen gelte, würde ich deshalb nicht übernehmen.
> - **Bund:** Die direkte Bundessteuer hat keine eigene Regelung. Die Einreichefrist bestimmt der Kanton, und die Fristerstreckung ist kantonal geregelt. Ein Gesuch beim Gemeindesteueramt deckt also Staats-, Gemeinde- und Bundessteuer.
> 
> **Status:** Die Quellen sind ☑️ agent-geprüft, die Abnahme ist offen. Das Datum 31. Dezember bezieht sich auf das Deklarationsjahr, also das Jahr der Einreichung. Ob es im Einzelfall Sammelgesuche oder eine bestimmte elektronische Eingabe gibt, geht aus den geprüften Quellen nicht hervor. Das habe ich nicht geprüft. Dazu sollten Sie beim jeweiligen Gemeindesteueramt nachfragen. Die fachliche Beurteilung bleibt bei Ihnen.

## b08

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Auf welchem Formular wird der Abzug für Versicherungsprämien und Sparzinsen berechnet und in welche Ziffer der Steuererklärung wird das Ergebnis übertragen?

**Soll (Referenz):** AR 2025: Berechnung auf Formular 6 (A: bezahlte Prämien/Zinsen, B: Maximalabzug, C: Abzug = niedrigerer Betrag von A und B). Der Betrag C wird auf Seite 3 der Steuererklärung in Ziffer 14 übertragen.

**Antwort des Agenten** (26.2 s · Tools: 1 Aufrufe steuerwiki__position):

> **Appenzell Ausserrhoden · Steuerjahr 2025**
> 
> **Formular:** Der Abzug wird auf dem **Hilfsblatt Formular 6** («Versicherungsprämien / Krankheitskosten») berechnet. Das ist Teil A bis C, Code 600. (Fundstelle: ar-form-06-2025__c0001, ar-form-06-2025__c0002; Status ☑️ agent-geprüft)
> 
> **Berechnung:**
> - **Teil A (Code 600 A):** Krankenversicherung (brutto) + Unfallversicherung (ohne NBUV) + Lebens-/Rentenversicherung + Sparzinsen (aus Formular 2) − Prämienverbilligungen.
> - **Teil B (Code 600 B):** Höchstbetrag. Er liegt bei CHF 5'400 für gemeinsam Steuerpflichtige und bei CHF 2'700 für übrige. Dazu kommen CHF 1'000 je Kind mit Kinderabzug nach Ziff. 23.1–23.3.
> - **Code 600:** Abzug = der tiefere Betrag aus 600 A und 600 B.
> 
> **Übertrag:** Das Ergebnis (Code 600) kommt in die **Ziffer 14** der Steuererklärung (Formular 1), «Versicherungsprämien und Zinsen von Sparkapitalien».
> 
> **Bund:** Das AR-Formular hat keine eigene Bundesspalte. Die Steuerverwaltung rechnet die Abweichungen für die direkte Bundessteuer automatisch. Die Berechnung auf Formular 6 gilt nur für die Staats- und Gemeindesteuer. Der Bund hat andere Höchstbeträge (ar-wl-2025__c0179):
> - gemeinsam CHF 3'700, übrige CHF 1'800, je Kind CHF 700;
> - ohne Beiträge an die 2. Säule oder Säule 3a: CHF 5'550 gemeinsam und CHF 2'700 übrige.
> 
> **Nicht abzugsfähig:** NBUV sowie Mobiliar-, Motorfahrzeug-, Haftpflicht- und andere Sachversicherungen.
> 
> **Belege:** Sie sind auf Verlangen einzureichen (Formular 6 Teil A).
> 
> **Einschränkung:** Das Hauptformular 1 ist nicht online verfügbar. Die Ziffer 14 stammt aus den Formular-Miniaturen der Wegleitung. Den Hauptformular-Code für Ziff. 14 habe ich nicht separat verifiziert. Die fachliche Beurteilung bleibt bei der Fachperson.

## b09

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wo und wie ist ein Gesuch um Fristverlängerung für die Steuererklärung einer natürlichen Person zu stellen und bis wann?

**Soll (Referenz):** SG 2025: Das Gesuch ist vor Ablauf der Einreichefrist (Datum auf Seite 1 der Steuererklärung) zu stellen, vorzugsweise elektronisch unter www.steuern.sg.ch (mit Registernummer und Geburtsdatum); sonst schriftlich an das Gemeindesteueramt. Es kann eine angemessene Fristverlängerung gewährt werden.

**Antwort des Agenten** (27.7 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **SG · Steuerjahr 2025: Gesuch um Fristverlängerung (natürliche Person)**
> 
> **Wo und wie**
> - **Elektronisch (bevorzugt):** auf www.steuern.sg.ch als eFristverlängerung. Dafür brauchen Sie die **Register-Nr.** und das **Geburtsdatum**, beide stehen auf der persönlichen Steuererklärung. Das Gesuch wird interaktiv bewilligt oder abgelehnt. (WL SG 2025 S. 8, `sg-wl-2025__c0018`; Infoseite `sg-info-fristverlaengerung__c0002`) ☑️ agent-geprüft
> - **Sonst schriftlich** an das **Gemeindesteueramt**. (`sg-wl-2025__c0018`) ☑️
> 
> **Bis wann**
> - Das Gesuch muss **vor Ablauf der Einreichefrist** gestellt werden. Die Wegleitung nennt dafür den «Einreichetermin gemäss Seite 1 der Steuererklärung». (`sg-wl-2025__c0018`) ☑️
> - Das konkrete Datum steht nicht im Wiki. Bitte auf Seite 1 der Steuererklärung 2025 nachsehen.
> 
> **Zu beachten**
> - Die Fristverlängerung wird nur gewährt, wenn die **fälligen Steuerrechnungen bezahlt** sind. (`sg-info-fristverlaengerung__c0002`) ☑️
> - Gewährt wird eine «angemessene» Verlängerung. Die Dauer ist in den Quellen nicht beziffert. Sie ist deshalb offen, und ich schätze sie nicht.
> - Bund: Es gibt kein eigenes Verfahren. Einreichefrist und Fristerstreckung regelt der Kanton, und die direkte Bundessteuer läuft über dieselbe kantonale Steuererklärung.
> - Eine Sonderregel für Treuhänder, etwa ein Sammelgesuch, habe ich in den Quellen nicht gefunden. Für Vertreter ist sie offen und nicht geprüft.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## b10

**Frage:** Ehepaar im Kanton St.Gallen, Steuerjahr 2025, zwei Kinder mit Kinderabzug, keine Beiträge an die 2. Säule oder Säule 3a bei beiden Partnern. Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Kantons-/Gemeindesteuern und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2025 Kanton: Fr. 6'800 + zusätzlich ohne 2. Säule/3a bis Fr. 1'100 + 2 x bis Fr. 1'100 für die Kinder = Fr. 10'100. Bund: Fr. 3'700 + zusätzlich bis Fr. 1'850 (= Fr. 5'550) + 2 x Fr. 700 = Fr. 6'950. (Voraussetzung für den Zusatzabzug muss bei beiden Partnern erfüllt sein.)

**Antwort des Agenten** (27.4 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **SG · Steuerjahr 2025: Ehepaar, 2 Kinder mit Kinderabzug, weder 2. Säule noch Säule 3a bei beiden Partnern**
> 
> Gezeigt ist der Höchstbetrag (B) für Versicherungsprämien und Sparzinsen (Ziff. 14, Code 600, Formular 6). Abgezogen wird der niedrigere Betrag aus den tatsächlich bezahlten Prämien und Sparzinsen (A) und diesem Höchstbetrag (B).
> 
> | | Kanton/Gemeinde (SG) | Direkte Bundessteuer |
> |---|---|---|
> | Grundbetrag Ehepaar | 6'800 | 3'700 |
> | Zuschlag ohne 2. Säule/3a (bei beiden Partnern) | +1'100 | +1'850 |
> | Kinder (2 × Kinderzuschlag) | +2'200 (2 × 1'100) | +1'400 (2 × 700) |
> | **Maximaler Abzug** | **CHF 10'100** | **CHF 6'950** |
> 
> Die Summen habe ich mit dem Rechentool geprüft.
> 
> **Fundstellen** (Status ☑️ agent-geprüft, Abnahme offen):
> - Kanton: sg-stg-2025__art-45-t2 (Art. 45 StG SG) und sg-form-6-2025__c0002. Der Wert 7'900 für Ehepaare ohne Vorsorge ist abgeleitet (6'800 + 1'100).
> - Bund: bund-dbg-2025__art-33-t2 und art-33-t5 (Art. 33 DBG).
> - Zuschlag Bund ohne Vorsorge: Die Quelle nennt «um die Hälfte», also 3'700 / 2 = 1'850. Das ergibt 5'550 für Ehepaare ohne Vorsorge.
> 
> **Hinweise:**
> - **Bund im Formular:** Es gibt nur eine Spalte. Die Bundeswerte setzt die Steuerbehörde automatisch um, Sie deklarieren nur einmal.
> - **Zuschlag ohne Vorsorge:** Er gilt nur, wenn bei beiden Partnern weder BVG- noch 3a-Beiträge abgezogen werden.
> - **Kinderzuschlag:** Er gilt nur für Kinder mit Kinderabzug (Ziff. 23.1/23.2). Beim Bund gilt er auch für unterstützungsbedürftige Personen.
> - **Berechnung von A:** A = Krankenkasse brutto + Unfall (ohne NBU) + Lebens-/Rentenversicherung + Sparzinsen − Prämienverbilligungen (IPV). Es zählen die Beträge der ganzen Familie.
> - **Nicht abziehbar:** Sachversicherungen wie Mobiliar, Motorfahrzeug und Haftpflicht.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## b11

**Frage:** Arbeitnehmer im Kanton Thurgau, Steuerjahr 2026, Arbeitsweg mit ÖV-Jahresabonnement, effektive Kosten Fr. 6'400. Welcher Fahrkostenabzug ist bei den Staats-/Gemeindesteuern und welcher bei der direkten Bundessteuer zulässig?

**Soll (Referenz):** TG 2026: Kanton gesamthaft max. Fr. 6'000, deshalb Abzug Fr. 6'000 (effektive Kosten Fr. 6'400 werden gekürzt). Bund max. Fr. 3'300, deshalb Abzug Fr. 3'300.

**Antwort des Agenten** (27.4 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Thurgau · Steuerjahr 2026**
> 
> Bei effektiven ÖV-Jahresabokosten von Fr. 6'400 gilt:
> 
> | | Abzug | Begründung |
> |---|---|---|
> | **Staats-/Gemeindesteuern TG** | **Fr. 6'000** | Plafond Fr. 6'000 pro Person (tg-wl-2026__c0176) ☑️ |
> | **Direkte Bundessteuer** | **Fr. 3'300** | Plafond Fr. 3'300 nach Art. 26 Abs. 1 lit. a DBG (bund-dbg-2026__art-26) ☑️ |
> 
> Die tatsächlichen Abokosten sind für Kanton und Bund gleich abziehbar. Der Unterschied entsteht erst beim Höchstbetrag. Beim Kanton sind Fr. 400 nicht abziehbar, beim Bund Fr. 3'100.
> 
> **Formular TG 2026:**
> - Hilfsblatt Form. 4.2 (Person 1) bzw. 4.3 (Person 2), Ziff. 2.1 «Abonnementskosten öffentliche Verkehrsmittel» (Code 206 bzw. 246): Fr. 6'400 einsetzen (tg-form-04-2-2026__c0002).
> - Ziff. 2.5 «Total abzugsfähige Fahrkosten» (Code 213 bzw. 253): links Staat Fr. 6'000, rechts Bund Fr. 3'300.
> - Das Total wird in die Berufsauslagen Ziff. 10.1 bzw. 10.2 übertragen, ebenfalls in beiden Spalten.
> 
> **Voraussetzungen:**
> - Im Lohnausweis darf Feld F («unentgeltliche Beförderung Wohn-/Arbeitsort») nicht angekreuzt sein. Sonst gibt es keinen Fahrkostenabzug.
> - Der Arbeitsweg muss eine beachtenswerte Entfernung haben (ab ca. 1 km).
> - Das Abo muss nachgewiesen sein. Ob der Beleg eingereicht werden muss, ist im Wiki als «unklar» vermerkt. Aufbewahren und auf Verlangen vorlegen.
> 
> Der Maximalbetrag Fr. 6'000 ist gesamthaft pro Person und umfasst auch Wochenaufenthalt und Nebenerwerb. Er wird bei Teilzeit oder unterjähriger Steuerpflicht nicht gekürzt.
> 
> Alle Fundstellen sind ☑️ agent-geprüft (Abnahme offen). Die fachliche Beurteilung bleibt bei der Fachperson.

## b12

**Frage:** Ehepaar im Kanton Zürich, Steuerjahr 2026, nachgewiesene Kinderdrittbetreuungskosten: Kind A (5 Jahre) Fr. 30'000, Kind B (8 Jahre) Fr. 12'000. Wie hoch ist der Abzug bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2026: Maximum pro Kind Staat Fr. 25'300, Bund Fr. 25'800 (Kinder unter 14). Staat: 25'300 + 12'000 = Fr. 37'300. Bund: 25'800 + 12'000 = Fr. 37'800. (Zum Vergleich 2025: Staat max. Fr. 25'000.)

**Antwort des Agenten** (27.7 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Kanton Zürich · Steuerjahr 2026: Abzug für Kinderdrittbetreuung (Ziff. 16.6, Code 376)**
> 
> Die Höchstgrenze gilt pro Kind. Beide Kinder sind unter 14 Jahren, daher erfüllen sie die Altersvoraussetzung.
> 
> | | Kind A (Fr. 30'000) | Kind B (Fr. 12'000) | **Total** |
> |---|---|---|---|
> | **Staatssteuer** (max. Fr. 25'300 pro Kind) | 25'300 (gekappt) | 12'000 | **Fr. 37'300** |
> | **Direkte Bundessteuer** (max. Fr. 25'800 pro Kind) | 25'800 (gekappt) | 12'000 | **Fr. 37'800** |
> 
> Bei Kind A sind Fr. 4'700 (Staatssteuer) bzw. Fr. 4'200 (Bund) über der Limite und nicht abziehbar. Die Zahlen stammen aus dem `rechne`-Tool.
> 
> **Fundstellen** (Status ☑️ agent-geprüft, Abnahme offen):
> - Staatssteuer: `zh-stg-2026__par-31-t3` (höchstens Fr. 25'300 pro Kind) und `zh-wl-2026-uj__c0105`.
> - Bund: `bund-dbg-2026__art-33-t7` (höchstens Fr. 25'800 pro Kind).
> - Formular: `zh-form-300-2026-uj__c0008`. Das reguläre ZH-Formular 2026 ist laut Wiki (Stand 09.11.2026) noch nicht publiziert. Die Ziffer und der Code 376 stützen sich auf die Fassung für unterjährige Steuerpflicht und sind am regulären Formular zu prüfen.
> 
> **Voraussetzungen, die ich nicht prüfen konnte:**
> - Die Kinder leben im gleichen Haushalt wie die Eltern.
> - Beide Ehegatten sind gleichzeitig erwerbstätig, in Ausbildung oder erwerbsunfähig, und die Kosten stehen in direktem Zusammenhang damit.
> - Es handelt sich um reine Betreuungskosten. Sport, Musik, Vereine, Schulgeld und Nachhilfe sind nicht abziehbar.
> - Sind die Kosten nur pauschal ausgewiesen, sind 20 % als Lebenshaltungskosten zu kürzen. Das gälte dann für die Beträge vor der Kappung.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## b13

**Frage:** Ein Mitglied der Milizfeuerwehr erhält für die Erfüllung von Kernaufgaben (Übungen, Pikettdienst, Ernstfalleinsätze) Sold. Bis zu welchem Betrag ist der Feuerwehrsold bei der direkten Bundessteuer steuerfrei, im Steuerjahr 2025 und im Steuerjahr 2026?

**Soll (Referenz):** Bund: 2025 steuerfrei bis maximal Fr. 5'300; 2026 steuerfrei bis maximal Fr. 5'400 (Wert hat sich geändert, nicht übertragen). Der gesamte Sold ist auf dem Lohnausweis zu deklarieren; der steuerfreie Betrag wird auf Formular 9 Berufskosten Ziffer 8 abgezogen.

**Antwort des Agenten** (23.4 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Bund (direkte Bundessteuer)**
> 
> Der Sold der Milizfeuerwehr für Kernaufgaben ist pro Jahr bis zu diesen Beträgen steuerfrei (Art. 24 Bst. fbis DBG):
> 
> | Steuerjahr | Steuerfrei bis | Fundstelle | Status |
> |---|---|---|---|
> | 2025 | **CHF 5'300** | bund-dbg-2025__art-24-t2 | ☑️ agent-geprüft (Abnahme offen) |
> | 2026 | **CHF 5'400** | bund-dbg-2026__art-24-t2 | ☑️ agent-geprüft (Abnahme offen) |
> 
> Die Grenze steigt 2026 gegenüber dem Vorjahr um CHF 100.
> 
> - **Kernaufgaben:** Die Steuerbefreiung gilt für Übungen, Pikettdienst und Ernstfalleinsätze.
> - **Nicht befreit:** Pauschalzulagen für Kader, Funktionszulagen, administrative Arbeiten und freiwillige Dienstleistungen. Diese Ausnahmen sind im Wiki nur für 2026 vermerkt, für 2025 nicht geprüft.
> - **Lohnausweis:** Den gesamten Sold im Lohnausweis deklarieren (Angabe aus dem Wiki zu 2026).
> - **Kanton:** Ich habe keinen Kanton geprüft. Die kantonalen Grenzen können abweichen. Für die Staats- und Gemeindesteuer müsste ich den Kanton kennen.

## b14

**Frage:** Ein Mandant wohnt am 31.12.2026 im Kanton Luzern und pendelt mit dem Auto zur Arbeit. Welcher Fahrkostenabzug gilt für die Luzerner Staats- und Gemeindesteuern 2026 und für die direkte Bundessteuer?

**Soll (Referenz):** Luzern ist im Wiki nicht abgedeckt (nur Bund, AR, SG, TG, ZH): kein Wert für die Luzerner Staats-/Gemeindesteuer nennen, auf kantonale Wegleitung verweisen. Für die direkte Bundessteuer 2026 gilt max. Fr. 3'300 (Wegleitung Bund 2026).

**Antwort des Agenten** (25.0 s · Tools: 1 Aufrufe steuerwiki__wert):

> Luzern ist im Wiki nicht abgedeckt. Den Bundesteil prüfe ich im Wiki.
> 
> **Kanton Luzern · Steuerjahr 2026**
> 
> **Luzerner Staats- und Gemeindesteuern:** Dazu kann ich nichts sagen. Das Wiki deckt nur Bund, AR, SG, TG und ZH ab, Luzern ist nicht im Wiki. Ich nenne deshalb keinen Wert und übertrage auch keinen Wert aus einem anderen Kanton. Massgebend sind das Luzerner Steuergesetz und die Wegleitung der Dienststelle Steuern Luzern für 2026. Dort musst du Maximalabzug, Kilometeransatz und Arbeitstage nachschlagen.
> 
> **Direkte Bundessteuer 2026** (Art. 26 Abs. 1 lit. a DBG, Wohnsitzkanton ändert daran nichts):
> 
> | Punkt | Wert | Fundstelle | Status |
> |---|---|---|---|
> | Maximalabzug Fahrten Wohn-/Arbeitsstätte | CHF 3'300 pro Jahr | `bund-dbg-2026__art-26` | ☑️ agent-geprüft |
> | Privatauto | CHF 0.75 pro km (2025: 0.70) | `bund-mm-2025-09-11-kalte-progression-2026__c0004` | ☑️ agent-geprüft |
> 
> - **Voraussetzung für das Auto:** Der Abzug nach km-Ansatz gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist. Sonst wird nur der Preis für das öffentliche Verkehrsmittel anerkannt.
> - **Deckel:** Der Gesamtabzug ist auf CHF 3'300 begrenzt, auch beim Auto.
> - **Arbeitstage:** Der Bund kennt keine feste Arbeitstage-Basis. Der Abzug richtet sich nach den tatsächlichen Kosten bis zum Maximum.
> - **Status:** ☑️ heisst, die Fundstelle ist geprüft, die Abnahme ist noch offen.
> 
> **Offen:**
> - Bei Luzern ist unklar, ob der Kanton für die Fahrkosten gleich rechnet wie der Bund. Das kann ich ohne Quelle nicht beurteilen.
> - Wie die Bundesspalte im Luzerner Formular erfasst wird, kann ich nicht sagen. Das steht im Wiki nur für die abgedeckten Kantone.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

