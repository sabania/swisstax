# OpenClaw-Testlauf: blindtest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 14 · Lauf: 2026-11-09 17:05
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## b01

**Frage:** Ehepaar in rechtlich und tatsächlich ungetrennter Ehe, weder Beiträge an die 2. Säule noch an die Säule 3a, Kanton ZH, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Zinsen von Sparkapitalien bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2025: Staatssteuer höchstens CHF 8'700 (Grundabzug CHF 5'800, ohne Beiträge an 2. Säule/3a um die Hälfte erhöht). Direkte Bundessteuer 2025: höchstens CHF 5'550 (Grundabzug CHF 3'700, um die Hälfte erhöht).

**Antwort des Agenten** (23.9 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **ZH, Steuerjahr 2025: Ehepaar in rechtlich und tatsächlich ungetrennter Ehe, ohne Beiträge an die 2. Säule und die Säule 3a**
> 
> Höchstabzug für Versicherungsprämien und Zinsen von Sparkapitalien (Ziff. 15, Code 270):
> 
> | | Maximaler Abzug | Fundstelle |
> |---|---|---|
> | **Staatssteuer (ZH)** | **CHF 8'700** | zh-wl-2025__c0086 |
> | **Direkte Bundessteuer** | **CHF 5'550** | bund-dbg-2025__art-33-t5 |
> 
> Alle Werte sind ☑️ agent-geprüft. Die Fundstelle ist geprüft, die Abnahme ist offen.
> 
> **Herleitung**
> - Mit Vorsorgebeiträgen betragen die Höchstbeträge für Verheiratete CHF 5'800 (Staat) und CHF 3'700 (Bund).
> - Ohne Beiträge an die 2. Säule und die Säule 3a erhöhen sie sich um die Hälfte.
>   - Staat: 5'800 + 2'900 = CHF 8'700.
>   - Bund: 3'700 + 1'850 = CHF 5'550.
> - Die beiden Beträge für Staat und Bund kommen aus dem Wiki. Die Rechnung dient nur der Nachvollziehbarkeit und ist nicht separat mit dem Tool geprüft.
> 
> **Wichtig zur Anwendung**
> - Die Beträge sind Höchstbeträge. Abziehbar ist der tiefere Betrag aus den tatsächlich bezahlten Prämien und Sparzinsen (Form. 365, Total A, Code 606) und dem Maximalabzug (Teil B). Das gilt je Spalte, also getrennt für Staat und Bund. Nach der Prämienverbilligung bleibt dabei nur der tatsächlich bezahlte Teil.
> - «Ohne 2./3a» gilt nur, wenn weder die Steuerpflichtigen noch ein Arbeitgeber Beiträge an die 2. Säule oder die Säule 3a geleistet haben. Leistet eine der beiden Personen Beiträge, gelten CHF 5'800 (Staat) und CHF 3'700 (Bund).
> - Für jedes Kind und jede unterstützungsbedürftige Person kommt ein Zuschlag dazu: CHF 1'300 (Staat) und CHF 700 (Bund). Er ist in den Beträgen oben nicht enthalten.

## b02

**Frage:** Wie hoch ist im Steuerjahr 2026 der Maximalabzug für Fahrkosten zwischen Wohn- und Arbeitsort im Kanton St.Gallen (Kantons- und Gemeindesteuern) und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2026: Kantons- und Gemeindesteuern max. Fr. 8'000; direkte Bundessteuer max. Fr. 3'300. Es ist ein Maximalabzug, keine Pauschale (bei Teilzeit/unterjährig nicht gekürzt).

**Antwort des Agenten** (22.6 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Steuerjahr 2026, Fahrkosten Wohn-/Arbeitsort (Maximalabzug)**
> 
> | | Maximalabzug | Fundstelle |
> |---|---|---|
> | **Kanton St.Gallen** (Staats- und Gemeindesteuern) | **CHF 8'000** | `sg-stg-2026__art-39`: «die notwendigen Kosten für Fahrten zwischen Wohn- und Arbeitsstätte bis zum Betrag von Fr. 8000.–» |
> | **Direkte Bundessteuer** | **CHF 3'300** | `bund-dbg-2026__art-26`: «bis zu einem Maximalbetrag von 3300 Franken für die Fahrten zwischen Wohn- und Arbeitsstätte» (Art. 26 Abs. 1 lit. a DBG) |
> 
> Status beider Werte: ☑️ agent-geprüft. Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> 
> **Zur Anwendung:**
> - Der SG-Maximalabzug von CHF 8'000 ist eine Obergrenze und keine Pauschale. Er wird bei unterjähriger Steuerpflicht oder Teilzeit nicht gekürzt. Er gilt für Haupt- und Nebenerwerb zusammen.
> - Beim Privatauto gilt 2026 neu ein Ansatz von CHF 0.75 pro Kilometer. 2025 waren es CHF 0.70. Das gilt bei Kanton und Bund und nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder zumutbar ist. Der jeweilige Maximalbetrag bleibt dabei die Obergrenze.
> - Die Velo-Pauschale beträgt bei Kanton und Bund CHF 700.
> - Im SG-Formular gehören die Fahrkosten unter Ziff. 10.1 (Person 1) bzw. 10.2 (Person 2), Berufskosten bei unselbständiger Erwerbstätigkeit.
> 
> **Nicht geprüft:** Die Weisung StB 39 Nr. 3 führt für 2026 neben den CHF 8'000 eine zweite Spalte mit Fr. 3'300. Der Chunk erklärt deren Bedeutung nicht, ich habe sie deshalb nicht übernommen. Vermutlich ist es der Bundesbetrag, das ist aber nicht belegt. Für den Maximalabzug im Kanton gilt nach dem Gesetzestext CHF 8'000.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## b03

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Welchen Kinderabzug können Eltern für ein 3-jähriges, ein 10-jähriges und ein 16-jähriges (noch minderjähriges) Kind geltend machen?

**Soll (Referenz):** AR (Kantonssteuer) 2025, indexierte Beträge gemäss Anhang 1 StG (bestätigt durch WL AR 2025 Ziff. 23): 3-jähriges Kind (bis Vollendung des 4. Altersjahrs) Fr. 5'300; 10-jähriges Kind (nach Vollendung des 4. bis Vollendung des 15. Altersjahrs) Fr. 7'400; 16-jähriges Kind (nach Vollendung des 15. Altersjahrs bis Volljährigkeit) Fr. 11'600. Gleiche Beträge für volljährige Kinder in Ausbildung bis zum 26. Altersjahr. (Korrigiert nach Bewertung Lauf A: die ursprüngliche Referenz nannte die nicht indexierten Merkblatt-Beträge 5'000/7'000/11'000.)

**Antwort des Agenten** (28.0 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **AR, Steuerjahr 2025: Kinderabzug für drei Kinder (3, 10 und 16 Jahre)**
> 
> Der Kanton staffelt den Abzug nach Alter. Der Bund kennt keine Altersstufen. Stichtag für das Alter ist der 31.12.2025.
> 
> | Kind | Formular-Ziffer | Kanton (Staats-/Gemeindesteuer) | Bund (dBSt) |
> |---|---|---|---|
> | 3-jährig (bis Vollendung 4. Altersjahr) | 23.1 | CHF 5'300 | CHF 6'800 |
> | 10-jährig (nach 4. bis Vollendung 15. Altersjahr) | 23.2 | CHF 7'400 | CHF 6'800 |
> | 16-jährig, minderjährig (nach 15. Altersjahr bis Volljährigkeit) | 23.3 | CHF 11'600 | CHF 6'800 |
> | **Total** | | **CHF 24'300** | **CHF 20'400** |
> 
> Im AR-Formular gibt es keine Bundesspalte. Die Bundesabzüge setzt die Steuerverwaltung automatisch.
> 
> **Fundstellen** (Status ☑️ agent-geprüft, Abnahme offen):
> - Kanton: `ar-stg-anhang-kp__c0001` (Art. 38 Abs. 1 lit. a Ziff. 1–3) und `ar-wl-2025__c0005`.
> - Bund: `bund-dbg-2025__art-35`.
> - Das Gesetz nennt für 2025 noch die nicht indexierten Beträge (5'000 / 7'000). Massgebend sind die indexierten Beträge laut Anhang 1 und Wegleitung 2025. Das Merkblatt 02 (Fassung 25.9.2025) nennt ebenfalls noch die alten Beträge.
> 
> **Voraussetzungen und Vorbehalte:**
> - **Kein Abzug im Kanton:** wenn das Kind Einkünfte von über CHF 18'000 hat oder ein Reinvermögen von über CHF 250'000. Das gilt auch, wenn Sie Unterhaltsbeiträge nach Ziff. 12.2 abziehen.
> - **Unterhalt:** Sie müssen den Unterhalt des Kindes zur Hauptsache bestreiten.
> - **Getrennte Eltern** mit gemeinsamer Sorge und ohne Unterhaltsbeiträge: Der Abzug wird je zur Hälfte aufgeteilt.
> - **Alter:** Das «3-jährige» Kind bekommt CHF 5'300 nur, wenn es am 31.12.2025 noch nicht vier ist. Wird es im Lauf von 2025 vier, gilt CHF 7'400. Entsprechend gilt der Abzug von CHF 7'400 für das 10-jährige Kind nur, solange es am Stichtag das 15. Altersjahr nicht vollendet hat.
> 
> **Zusätzlich, aber nicht Teil des Kinderabzugs** (pro Kind):
> - Versicherungsabzug: Zuschlag von CHF 1'000 im Kanton (Art. 35) und CHF 700 beim Bund. Bei drei Kindern sind das CHF 3'000 bzw. CHF 2'100.
> - Vermögen: Freibetrag von CHF 25'000 pro minderjähriges Kind im Kanton (Art. 51). Bei drei Kindern sind das CHF 75'000.
> - Bund: Abzug vom Steuerbetrag von CHF 263 pro Kind.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.
> 
> Ich bin Ihr neuer Assistent. Wie möchten Sie mich nennen?

## b04

**Frage:** Alleinstehende Person ohne Kinder mit Beiträgen an die 2. Säule, Kanton Thurgau, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Staats-/Gemeindesteuern und bei der Bundessteuer?

**Soll (Referenz):** TG 2025: Staat max. Fr. 3'500, Bund max. Fr. 1'800 (ohne Beiträge an Säule 2/3a würde beim Bund Fr. 2'700 gelten). Betrag vor Abzug Prämienverbilligungen Krankenkassen.

**Antwort des Agenten** (23.4 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Thurgau, Steuerjahr 2025, alleinstehend, keine Kinder, mit Beiträgen an die 2. Säule**
> 
> | | Maximalabzug |
> |---|---|
> | **Staats-/Gemeindesteuern TG** | **CHF 3'500** |
> | **Direkte Bundessteuer** | **CHF 1'800** |
> 
> **Quellen**
> - Kanton: «Fr. 3'500 für die übrigen Steuerpflichtigen», `tg-stg__par-34-t3`. Status: ☑️ agent-geprüft.
> - Bund: «1800 Franken für die übrigen Steuerpflichtigen», `bund-dbg-2025__art-33-t2`. Status: ☑️ agent-geprüft.
> 
> **Zur Anwendung**
> - Der Abzug ist der niedrigere Betrag aus den tatsächlichen Prämien und Sparzinsen und dem Maximum. Die Maxima sind also Obergrenzen, keine Pauschalen. Im Formular steht der Abzug in Ziff. 14 (Code 330), berechnet über das Hilfsblatt Formular 5.2. Kanton und Bund werden dort in zwei Spalten getrennt ermittelt.
> - Zu den abzugsfähigen Posten gehören:
>   - die Krankenkassenprämien, netto nach Abzug der Prämienverbilligung,
>   - private Unfall-, Lebens- und Rentenversicherungen,
>   - erhaltene Sparzinsen,
>   - Krankentaggeld-Beiträge laut Lohnausweis.
> - Die Krankenkassenprämien müssen deklariert werden. Sonst gibt es unter Umständen gar keinen Versicherungsabzug.
> - Die erhöhten Bundesansätze von CHF 2'700 (alleinstehend) bzw. CHF 5'550 (verheiratet) gelten nur für Personen **ohne** Beiträge an die Säulen 2/3a. Bei Beiträgen an die 2. Säule gilt hier CHF 1'800. Die beiden Ansätze sind nicht kumulierbar.
> - Beim Kanton gibt es keine solche Erhöhung. Dort gilt unabhängig von der Vorsorge CHF 3'500.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson. Die Abnahme der beiden Werte ist laut Wiki noch offen.
> 
> Falls du magst: Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## b05

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wie hoch ist der Kinderabzug für ein noch nicht schulpflichtiges Kind und für ein Kind in Schule oder Ausbildung bei den Kantons-/Gemeindesteuern?

**Soll (Referenz):** SG 2025: noch nicht schulpflichtiges Kind Fr. 7'600 (Ziff. 23.1); Kind in Schule oder Ausbildung (auch volljährig) Fr. 10'800 (Ziff. 23.2).

**Antwort des Agenten** (23.4 s · Tools: 1 Aufrufe steuerwiki__wert):

> **St. Gallen, Steuerjahr 2025, Kantons- und Gemeindesteuern**
> 
> | Kind | Kinderabzug | Formular-Ziffer | Status |
> |---|---|---|---|
> | Noch nicht schulpflichtig | **CHF 7'600** | 23.1 | ☑️ agent-geprüft |
> | In Schule oder Ausbildung (auch volljährig) | **CHF 10'800** | 23.2 | ☑️ agent-geprüft |
> 
> Fundstelle für beide Beträge: `sg-stg-2025__art-48` (Art. 48 StG SG).
> 
> **Bedingungen**
> - Vorschulkind: Das Kind steht unter Ihrer elterlichen Sorge oder Obhut. Massgebend sind die Verhältnisse am 31.12. Sie kommen zur Hauptsache für den Unterhalt auf und machen keinen Unterhaltsabzug geltend.
> - Schule oder Ausbildung: Der Abzug gilt für Kinder unter Ihrer Sorge oder Obhut sowie für volljährige Kinder in schulischer oder beruflicher Ausbildung.
> - Kein Kinderabzug, wenn Sie Unterhaltsbeiträge nach Art. 45 Abs. 1 lit. c StG abziehen.
> 
> **Weitere Abzüge pro Kind (Kanton), falls relevant**
> - Ausbildungskostenabzug (Ziff. 23.3, Code 256): effektive, selbst getragene Kosten nach Abzug von Stipendien, soweit sie den Selbstbehalt von CHF 3'200 übersteigen, höchstens CHF 13'700. Er ist nicht auf auswärtige Ausbildung beschränkt (`sg-stg-2025__art-48`).
> - Versicherungsabzug: Zuschlag von CHF 1'100 pro Kind (`sg-stg-2025__art-45-t2`).
> - Vermögen: zusätzlich CHF 20'000 pro minderjähriges Kind, für das ein Kinderabzug beansprucht werden kann (`sg-stg-2025__art-64`).
> 
> **Zum Vergleich: direkte Bundessteuer**
> Der Bund kennt keine Altersstaffel. Es gilt ein einheitlicher Kinderabzug von CHF 6'800 pro Kind (`bund-dbg-2025__art-35`). Zusätzlich ermässigt sich der Steuerbetrag um CHF 263 pro Kind (`bund-dbg-2025__art-36-t4`).
> 
> Die Beträge sind agent-geprüft, die Abnahme durch eine Fachperson steht noch aus.
> 
> Übrigens: Ich bin neu hier und der Assistent dieses Steuer-Wikis. Wie möchten Sie mich nennen?

## b06

**Frage:** Bis wann ist die Steuererklärung 2025 einer natürlichen Person im Kanton Zürich einzureichen, und wie ist vorzugehen, wenn die Frist nicht eingehalten werden kann?

**Soll (Referenz):** ZH, Steuerperiode 2025: Einreichung bis 31. März 2026 (online oder an das Scan-Center). Gesuch um Fristerstreckung ist vor Ablauf der Frist beim Gemeindesteueramt zu stellen. Mahnfristen sind nicht erstreckbar.

**Antwort des Agenten** (29.8 s · Tools: 6 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Steuerjahr 2025, Kanton Zürich (natürliche Personen)**
> 
> **Ordentliche Frist: 31. März 2026.** Die Steuererklärung 2025 ist bis dahin online oder über das Scan-Center einzureichen. Die Frist wird vom Kanton bestimmt und gilt auch für die direkte Bundessteuer. (✅ ☑️ agent-geprüft; zh-wl-2025__c0017)
> 
> **Wenn die Frist nicht eingehalten werden kann:**
> 
> 1. **Fristerstreckungsgesuch vor Fristablauf** beim Gemeindesteueramt stellen. Auch die Vertretung (z. B. Treuhand) kann es stellen. (§ 39 Abs. 1 StV ZH; zh-zstb-132-1__c0023)
> 2. **Dauer:** Rechtzeitige Gesuche werden gemäss Gesuch bewilligt, längstens bis 30. November 2026. Ein erstes, rechtzeitiges Gesuch gilt ohne gegenteiligen schriftlichen Entscheid als stillschweigend bewilligt. (zh-zstb-132-1__c0024, c0026)
> 3. **Ein schriftlicher Entscheid** ergeht nur bei verspäteten Gesuchen und bei Begehren über den 30. November hinaus. Eine Verlängerung darüber hinaus gibt es nur aus ausserordentlichen Gründen. Die berufliche Belastung der Vertretung genügt dafür nicht.
> 4. **Von Amtes wegen bis 30. September 2026** erstreckt das Gemeindesteueramt die Frist für im Kanton wohnhafte Selbständigerwerbende und für ausserkantonal Wohnhafte. Ein Gesuch ist dann nicht nötig. (zh-zstb-132-1__c0023)
> 5. **Bei Ablehnung** steht eine Aufsichtsbeschwerde an die Finanzdirektion offen. (§ 39 Abs. 2 StV ZH)
> 
> **Wenn auch die erstreckte Frist verpasst wird:**
> - Es folgt eine **Mahnung** mit A-Post Plus, ohne Gebühr. Davor kann eine Aufforderung mit gewöhnlicher Post mit 20 Tagen Frist kommen.
> - Die **Mahnfrist beträgt 10 Tage und ist nicht erstreckbar** (§ 41 Abs. 2 StV).
> - Die Mahnung droht eine **Einschätzung nach pflichtgemässem Ermessen** und eine **Ordnungsbusse** (§ 234 StG bzw. Art. 174 DBG) an. (zh-zstb-132-1__c0029)
> 
> **Zum heutigen Datum (9.11.2026):**
> - Die ordentliche Frist ist abgelaufen. Falls kein Gesuch gestellt wurde und noch keine Mahnung vorliegt, sofort beim Gemeindesteueramt um Erstreckung bis 30.11.2026 ersuchen. Ein verspätetes Gesuch wird schriftlich entschieden, ein stillschweigender Bewilligungsautomatismus gilt dafür nicht.
> - Ist ein Gesuch bereits bewilligt, läuft die Frist am 30.11.2026 ab. Danach droht die Mahnung.
> 
> **Nicht belegt bzw. nicht geprüft:**
> - Die Kosten einer Fristerstreckung stehen in den Quellen nicht.
> - Die Quellen enthalten keine Angaben zur Höhe der Ordnungsbusse.
> - Der Status ☑️ heisst: Fundstelle geprüft, Abnahme durch die Fachperson offen. Die fachliche Beurteilung bleibt dort.
> 
> Übrigens: Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## b07

**Frage:** Wir sind eine Treuhandfirma und brauchen für Mandanten im Kanton Thurgau (Steuerperiode 2025, natürliche Personen) eine Fristerstreckung. Bei welcher Stelle ist das Gesuch einzureichen und bis wann kann die Frist längstens erstreckt werden?

**Soll (Referenz):** TG: Gesuch beim Gemeindesteueramt, das darüber entscheidet. Erstmals eingereichte Gesuche werden grundsätzlich bis längstens 30. September des Deklarationsjahres (2026) gutgeheissen; zusätzliche Gesuche in begründeten Fällen bis 30. November. Treuhänder/Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen, können für ihre Mandanten ein Gesuch längstens bis 31. Dezember des Deklarationsjahres beantragen. Arbeitsüberlastung ist kein Grund.

**Antwort des Agenten** (32.6 s · Tools: 6 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **TG, Steuerperiode 2025, natürliche Personen**
> 
> **Zuständige Stelle:** Das Gesuch geht an das **Gemeindesteueramt** (Wohnsitzgemeinde der steuerpflichtigen Person), nicht an die kantonale Steuerverwaltung. Das Gemeindesteueramt entscheidet auch darüber. Die Steuerverwaltung Thurgau ist nur für juristische Personen zuständig. Bei Ausserkantonalen gilt die Liegenschafts- bzw. Betriebsstättengemeinde. Das Gesuch ist schriftlich, begründet und rechtzeitig vor Fristablauf einzureichen. Beim Entscheid wird er dem Vertreter zugestellt, wenn dieser das Gesuch gestellt hat.
> Quelle: tg-stp-155-2__c0001, tg-stp-155-2__c0005, tg-wl-2025__c0023 (☑️ agent-geprüft).
> 
> **Längste Erstreckung:**
> 
> | Gesuchsteller | Längstens bis |
> |---|---|
> | Treuhänder und Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen (für ihre Mandanten) | **31. Dezember 2026** |
> | Private, erstes Gesuch | 30. September 2026 |
> | Private, weitere Gesuche (nur in begründeten Fällen) | 30. November 2026 |
> 
> Quelle: tg-stp-155-2__c0002 (☑️ agent-geprüft).
> 
> - **Deklarationsjahr:** Das ist das Jahr der Einreichung, für die Steuerperiode 2025 also 2026. Die Treuhänder-Frist läuft damit bis 31.12.2026. Heute ist der 09.11.2026, die Frist ist noch erreichbar.
> - **Über den 31. Dezember hinaus:** Dafür gibt es in den geprüften Quellen keine Regel. Die allgemeine Praxis nennt für weitere Gesuche über den 30. November hinaus nur «ausserordentliche Gründe». Das gilt für Private. Ob ein Gesuch über den 31.12. hinaus für Treuhänder möglich ist, habe ich nicht geprüft.
> - **Gründe:** Arbeitsüberlastung gilt nicht als Grund. Auch «starke berufliche Inanspruchnahme des Vertreters» oder «fehlende Unterlagen» reichen nicht, wenn man ausserordentliche Gründe geltend machen will. Verlangt wird eine substanziierte Sachdarstellung (tg-stp-155-2__c0002).
> - **Gebühr:** Die erstmalige Fristerstreckung ist gebührenfrei. Für jedes weitere Gesuch fällt eine Kanzleigebühr von Fr. 30 an (§ 39b Abs. 2–3 StV TG, tg-stv__par-39b). Ab der zweiten Mahnung kostet die Mahnung Fr. 50 (Abs. 4). Die Wiki-Übersicht (`wert`) hält fest, die Gebühr für natürliche Personen sei in den Quellen nicht genannt. Dort steht nur die Fr. 30 für juristische Personen. Der Verordnungstext selbst unterscheidet aber nicht nach Personenart. Ich würde mich auf § 39b stützen.
> - **Rechtsmittel:** Eine verweigerte Fristverlängerung ist ein Zwischenentscheid und kann nicht selbständig angefochten werden (tg-stp-155-2__c0005).
> - **Bund:** Die direkte Bundessteuer hat keine eigene Fristerstreckung. Das Gesuch beim Gemeindesteueramt deckt die kantonale Steuererklärung und damit auch den Bund.
> - **Nicht geprüft:** Ob ein Sammelgesuch für mehrere Mandanten oder ein bestimmtes Formular bzw. ein Online-Weg möglich ist, habe ich nicht geprüft. Das sollte man vorab beim Gemeindesteueramt klären. Die Fachbeurteilung bleibt bei euch.
> 
> Ask me anything; for system things I'll ask OpenClaw.

## b08

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Auf welchem Formular wird der Abzug für Versicherungsprämien und Sparzinsen berechnet und in welche Ziffer der Steuererklärung wird das Ergebnis übertragen?

**Soll (Referenz):** AR 2025: Berechnung auf Formular 6 (A: bezahlte Prämien/Zinsen, B: Maximalabzug, C: Abzug = niedrigerer Betrag von A und B). Der Betrag C wird auf Seite 3 der Steuererklärung in Ziffer 14 übertragen.

**Antwort des Agenten** (25.4 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__suche):

> **AR, Steuerjahr 2025:** Der Abzug wird auf **Formular 6** berechnet und in **Ziffer 14** der Steuererklärung übertragen. Das ist das Hilfsblatt «Krankheits- und Unfallkosten / Versicherungsprämien und Sparzinsen». Die Wegleitung nennt «Versicherungsprämien» und «Sparzinsen» unter Ziff. 14 mit Verweis auf Formular 6 (ar-wl-2025__c0085, ar-wl-2025__c0065).
> 
> **Ablauf auf Formular 6 (Code 600):**
> - **A, bezahlte Prämien und Zinsen:** Code 600 A = Krankenversicherung (brutto) + Unfallversicherung (ohne NBUV) + Lebens-/Rentenversicherung + Sparzinsen (aus Formular 2) − Prämienverbilligung (ar-form-06-2025__c0001).
> - **B, Maximalabzug:** Code 600 B = CHF 5'400 für gemeinsam Steuerpflichtige oder CHF 2'700 für übrige Steuerpflichtige. Dazu kommen CHF 1'000 je Kind mit Kinderabzug nach Ziff. 23.1–23.3 (ar-form-06-2025__c0002).
> - **C, Abzug:** Code 600 = der niedrigere der beiden Beträge A und B. Dieser Betrag kommt in **Ziff. 14**.
> 
> **Bund:** Das AR-Formular hat keine eigene Bundesspalte. Der abweichende Versicherungsabzug der direkten Bundessteuer wird von der Steuerverwaltung automatisch vorgenommen (ar-wl-2025__c0179). Die Bundeslimiten sind CHF 3'700 bzw. CHF 1'800 plus CHF 700 je Kind, ohne Beiträge an Säule 2/3a CHF 5'550 bzw. CHF 2'700.
> 
> **Nicht aufführen:** NBUV, Mobiliar-, Haftpflicht-, Motorfahrzeug- und andere Sachversicherungen.
> 
> **Status:** ☑️ agent-geprüft, die Abnahme steht noch aus. Der Code 600 stammt aus dem Hilfsblatt Formular 6. Der Hauptformular-Code für Ziff. 14 ist im Wiki nicht separat verifiziert, weil das Hauptformular nicht online verfügbar ist. Die Ziffer 14 selbst ist durch die Wegleitung belegt. Die fachliche Beurteilung bleibt bei der Fachperson.

## b09

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wo und wie ist ein Gesuch um Fristverlängerung für die Steuererklärung einer natürlichen Person zu stellen und bis wann?

**Soll (Referenz):** SG 2025: Das Gesuch ist vor Ablauf der Einreichefrist (Datum auf Seite 1 der Steuererklärung) zu stellen, vorzugsweise elektronisch unter www.steuern.sg.ch (mit Registernummer und Geburtsdatum); sonst schriftlich an das Gemeindesteueramt. Es kann eine angemessene Fristverlängerung gewährt werden.

**Antwort des Agenten** (27.5 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Kurzantwort:** Das Gesuch geht an das Gemeindesteueramt und muss **vor Ablauf der Einreichefrist** eingehen. Diese Frist steht auf Seite 1 der Steuererklärung 2025. Am besten stellen Sie es elektronisch.
> 
> **Wo und wie (SG, Steuerjahr 2025)**
> - **Elektronisch (bevorzugt):** auf www.steuern.sg.ch, als «eFristverlängerung». Sie brauchen die **Register-Nr.** und das **Geburtsdatum**, beide stehen auf der persönlichen Steuererklärung. Das System bewilligt oder lehnt das Gesuch interaktiv ab. (WL SG 2025 S. 8, `sg-wl-2025__c0018`; `sg-info-fristverlaengerung__c0002`)
> - **Schriftlich:** Wenn Sie das Gesuch nicht elektronisch stellen, richten Sie es schriftlich an das **Gemeindesteueramt**. (`sg-wl-2025__c0018`)
> 
> **Bis wann**
> - Das Gesuch muss «vor Ablauf der Einreichefrist» gestellt werden. Die Frist ist der Einreichetermin gemäss Seite 1 der Steuererklärung. (`sg-wl-2025__c0018`)
> - Das konkrete Datum steht nicht in den Quellen des Wikis. Bitte auf der Steuererklärung 2025 nachsehen. Nicht geprüft ist, ob für Ihren Fall noch eine Frist läuft.
> 
> **Voraussetzung**
> - Die Fristverlängerung wird nur gewährt, wenn die **fälligen Steuerrechnungen bezahlt** sind. (`sg-info-fristverlaengerung__c0002`)
> 
> **Offen**
> - Die Wegleitung spricht von einer «angemessenen» Fristverlängerung. Die Dauer ist in den Quellen nicht beziffert.
> - Eine Sonderregel für Treuhänder oder Sammelgesuche habe ich nicht gefunden.
> 
> **Bund:** Die direkte Bundessteuer hat keine eigene Regelung. Die Erklärung wird über die kantonale Steuererklärung abgegeben, die Fristerstreckung ist kantonal geregelt.
> 
> **Status:** ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Hinweis zum Datum:** Heute ist der 9.11.2026. Falls die Einreichefrist 2025 bereits abgelaufen ist, kommt das Gesuch zu spät. Ob und wie in diesem Fall eine verspätete Einreichung (Busse) oder Nachfrist greift, habe ich nicht geprüft. Die Strafbestimmung dazu liegt unter `sg-wl-2025__c0170`.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## b10

**Frage:** Ehepaar im Kanton St.Gallen, Steuerjahr 2025, zwei Kinder mit Kinderabzug, keine Beiträge an die 2. Säule oder Säule 3a bei beiden Partnern. Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Kantons-/Gemeindesteuern und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2025 Kanton: Fr. 6'800 + zusätzlich ohne 2. Säule/3a bis Fr. 1'100 + 2 x bis Fr. 1'100 für die Kinder = Fr. 10'100. Bund: Fr. 3'700 + zusätzlich bis Fr. 1'850 (= Fr. 5'550) + 2 x Fr. 700 = Fr. 6'950. (Voraussetzung für den Zusatzabzug muss bei beiden Partnern erfüllt sein.)

**Antwort des Agenten** (37.7 s · Tools: 6 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__zeige, steuerwiki__rechne):

> **Maximaler Abzug für Versicherungsprämien und Sparzinsen (Ehepaar, 2 Kinder mit Kinderabzug, ohne 2. Säule und Säule 3a bei beiden Partnern, Steuerjahr 2025):**
> 
> | | Kanton und Gemeinde SG | Direkte Bundessteuer |
> |---|---|---|
> | Grundbetrag, gemeinsam steuerpflichtige Ehegatten | CHF 6'800 | CHF 3'700 |
> | Zuschlag, weil bei beiden keine 2. Säule und keine Säule 3a abgezogen wird | + CHF 1'100 | + CHF 1'850 (die Hälfte von 3'700) |
> | Zuschlag für 2 Kinder | + 2 × CHF 1'100 = CHF 2'200 | + 2 × CHF 700 = CHF 1'400 |
> | **Maximaler Abzug** | **CHF 10'100** | **CHF 6'950** |
> 
> Die Summen habe ich mit `rechne` geprüft.
> 
> **Fundstellen** (Status ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen):
> - **Kanton SG:** Art. 45 Abs. 1 Bst. g StG SG (`sg-stg-2025__art-45-t2`). Die Zuschläge stehen im selben Artikel. Auch das Formular 6 Teil B/C nennt sie (`sg-form-6-2025__c0002`).
> - **Bund:** Art. 33 Abs. 1 Bst. g und Abs. 1bis DBG (`bund-dbg-2025__art-33-t5`). Die Beträge für 2025 (3'700, 5'550 ohne 2. Säule/3a, 700 je Kind) stehen im Rundschreiben RS 2-210 (`bund-rs-2-210__c0006`).
> 
> **Hinweise:**
> - **Abgeleitete Zahlen:** Die Gesamtbeträge 10'100 und 6'950 stehen nirgends als fertige Zahl, ich habe sie aus den Einzelbeträgen zusammengesetzt. Beim Bund ergibt «um die Hälfte» auf 3'700 die 5'550 laut RS 2-210. Der Kinderzuschlag von 700 kommt flach dazu. Das ist meine Lesart von Art. 33 Abs. 1bis DBG, ein Gesamtbetrag mit Kindern steht in den Quellen nicht.
> - **Zuschlag nur bei beiden Partnern:** Er gilt nur, wenn bei beiden weder 2. Säule noch Säule 3a abgezogen wird. Das trifft hier zu.
> - **Maximalbeträge, kein Pauschalabzug:** Abziehbar ist der niedrigere Betrag aus den effektiv bezahlten Prämien und Sparzinsen und diesem Maximum. Die Prämienverbilligung (IPV) wird zuerst abgezogen.
> - **Eintrag im Formular:** In St. Gallen deklarieren Sie nur einmal, in Ziff. 14 (Code 600) mit Formular 6. Die Bundesbeträge setzt das Steueramt automatisch um (Merkblatt 32).
> - **Nicht abziehbar:** Sachversicherungen wie Mobiliar, Motorfahrzeug und Haftpflicht.
> - **Fachliche Beurteilung:** Sie bleibt bei der zuständigen Fachperson.
> 
> Ask me anything; for system things I'll ask OpenClaw.

## b11

**Frage:** Arbeitnehmer im Kanton Thurgau, Steuerjahr 2026, Arbeitsweg mit ÖV-Jahresabonnement, effektive Kosten Fr. 6'400. Welcher Fahrkostenabzug ist bei den Staats-/Gemeindesteuern und welcher bei der direkten Bundessteuer zulässig?

**Soll (Referenz):** TG 2026: Kanton gesamthaft max. Fr. 6'000, deshalb Abzug Fr. 6'000 (effektive Kosten Fr. 6'400 werden gekürzt). Bund max. Fr. 3'300, deshalb Abzug Fr. 3'300.

**Antwort des Agenten** (24.1 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__rechne):

> Bei effektiven Fahrkosten von Fr. 6'400 (Thurgau, Steuerjahr 2026) darf die Person abziehen:
> 
> | | Zulässiger Abzug | Begrenzung |
> |---|---|---|
> | **Staats-/Gemeindesteuern TG** | **Fr. 6'000** | Maximum Fr. 6'000 pro Person |
> | **Direkte Bundessteuer** | **Fr. 3'300** | Maximum Fr. 3'300 (Art. 26 Abs. 1 lit. a DBG) |
> 
> Das ist jeweils der tiefere Wert aus den effektiven Kosten und dem Maximum. Beim Kanton fallen Fr. 400 weg, beim Bund Fr. 3'100.
> 
> **Kanton TG:** Der Höchstbetrag von Fr. 6'000 gilt gesamthaft pro Person, inklusive Wochenaufenthalt und Nebenerwerb. Er wird nicht gekürzt, wenn die Steuerpflicht nur während eines Teils des Jahres besteht oder bei Teilzeit. Quelle: tg-wl-2026__c0176. Status: ☑️ agent-geprüft, Abnahme offen.
> 
> **Bund:** Der Höchstbetrag von Fr. 3'300 gilt für die Fahrten zwischen Wohn- und Arbeitsstätte und ist gleich hoch wie 2025. Quelle: bund-dbg-2026__art-26. Status: ☑️ agent-geprüft, Abnahme offen.
> 
> **Formular:** Im TG-Formular gibt es keine separate Bundeserklärung. Die Fahrkosten stehen unter Ziff. 10.1 bzw. 10.2 (Berufsauslagen bei unselbständiger Erwerbstätigkeit). Die Bundeslimite wird dort über die Bundesspalte berücksichtigt. Ich habe die Formularposition hier nicht einzeln aufgerufen, die genaue Eintragung steht in `position tg 2026 10.1`.
> 
> Die Berufsbezeichnung des Abonnements ist nicht entscheidend: Die Abzüge folgen den tatsächlichen Kosten des ÖV-Jahresabonnements, begrenzt durch die Maxima. Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## b12

**Frage:** Ehepaar im Kanton Zürich, Steuerjahr 2026, nachgewiesene Kinderdrittbetreuungskosten: Kind A (5 Jahre) Fr. 30'000, Kind B (8 Jahre) Fr. 12'000. Wie hoch ist der Abzug bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2026: Maximum pro Kind Staat Fr. 25'300, Bund Fr. 25'800 (Kinder unter 14). Staat: 25'300 + 12'000 = Fr. 37'300. Bund: 25'800 + 12'000 = Fr. 37'800. (Zum Vergleich 2025: Staat max. Fr. 25'000.)

**Antwort des Agenten** (27.4 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **Abzug für Kinderdrittbetreuung, Kanton Zürich, Steuerjahr 2026** (Ziff. 16.6, Code 376)
> 
> Der Abzug wird für jedes Kind einzeln auf den Höchstbetrag begrenzt.
> 
> | | Kind A (5 J.) | Kind B (8 J.) | Total |
> |---|---|---|---|
> | Nachgewiesene Kosten | 30'000 | 12'000 | 42'000 |
> | **Staatssteuer** (Max. 25'300 je Kind) | 25'300 (gekürzt) | 12'000 | **Fr. 37'300** |
> | **Direkte Bundessteuer** (Max. 25'800 je Kind) | 25'800 (gekürzt) | 12'000 | **Fr. 37'800** |
> 
> - Beide Kinder sind unter 14 Jahren, die Altersgrenze ist also eingehalten (Kanton und Bund).
> - Fr. 4'700 (Staat) bzw. Fr. 4'200 (Bund) von Kind A sind nicht abziehbar. Der Höchstbetrag gilt je Kind, nicht gesamthaft. Die 12'000 von Kind B werden nicht gegen die gekappten Beträge von Kind A verrechnet.
> - Beide Beträge sind als ☑️ agent-geprüft eingestuft (Fundstelle geprüft, Abnahme offen).
> - Das reguläre ZH-Formular und die Wegleitung 2026 sind noch nicht publiziert (Stand 09.11.2026). Die Ziffer 16.6 und der Code 376 stammen aus der Fassung für unterjährige Steuerpflicht. Sie sind am regulären Formular zu prüfen.
> 
> **Voraussetzungen, die zu prüfen sind:**
> - Die Kinder leben im gleichen Haushalt wie das Ehepaar.
> - Die Kosten stehen im direkten Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit. Bei Ehepaaren müssen beide gleichzeitig erwerbstätig, in Ausbildung oder erwerbsunfähig sein.
> - Nur die Betreuung während der Arbeits- oder Ausbildungszeit zählt. Sport, Musik, Vereine, Schulgeld und Nachhilfe sind nicht abziehbar.
> - Wenn nur pauschale Beträge ausgewiesen sind, werden 20 % als Lebenshaltungskosten gekürzt. Bei Fr. 30'000 und Fr. 12'000 ist zu klären, ob es sich um Rechnungen für reine Betreuung handelt.
> 
> **Belege:** Rechnungen und Zahlungsnachweise (Kita, Hort, Tagesmutter) sowie eine Aufstellung mit den Empfängern. Bei angestellter Betreuungsperson kommt eine Kopie des Lohnausweises dazu.
> 
> **Quellen:** zh-stg-2026__par-31-t3 (Staatssteuer, 25'300), bund-dbg-2026__art-33-t7 (Bund, 25'800), zh-form-300-2026-uj__c0008 (Ziff. 16.6).
> 
> Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## b13

**Frage:** Ein Mitglied der Milizfeuerwehr erhält für die Erfüllung von Kernaufgaben (Übungen, Pikettdienst, Ernstfalleinsätze) Sold. Bis zu welchem Betrag ist der Feuerwehrsold bei der direkten Bundessteuer steuerfrei, im Steuerjahr 2025 und im Steuerjahr 2026?

**Soll (Referenz):** Bund: 2025 steuerfrei bis maximal Fr. 5'300; 2026 steuerfrei bis maximal Fr. 5'400 (Wert hat sich geändert, nicht übertragen). Der gesamte Sold ist auf dem Lohnausweis zu deklarieren; der steuerfreie Betrag wird auf Formular 9 Berufskosten Ziffer 8 abgezogen.

**Antwort des Agenten** (22.6 s · Tools: 2 Aufrufe steuerwiki__wert):

> Bei der direkten Bundessteuer ist der Sold der Milizfeuerwehrleute für Kernaufgaben pro Jahr bis zu diesen Beträgen steuerfrei:
> 
> | Steuerjahr | Steuerfrei bis | Fundstelle (Art. 24 DBG) | Status |
> |---|---|---|---|
> | **2025** | **CHF 5'300** | `bund-dbg-2025__art-24-t2` | ☑️ agent-geprüft (Abnahme offen) |
> | **2026** | **CHF 5'400** | `bund-dbg-2026__art-24-t2` | ☑️ agent-geprüft (Abnahme offen) |
> 
> Der Betrag ist 2026 neu um CHF 100 höher als im Vorjahr.
> 
> - **Was zählt:** Steuerfrei ist nur der Sold für Kernaufgaben, also Übungen, Pikettdienst und Ernstfalleinsätze. Das trifft auf Ihren Fall zu. Pauschalzulagen für Kader, Funktionszulagen, administrative Arbeiten und freiwillige Dienstleistungen sind davon ausgenommen. Diese Ausnahmen stehen nur in der Fundstelle für 2026. Die Fundstelle für 2025 nennt sie nicht.
> - **Deklaration:** Der gesamte Sold gehört in den Lohnausweis. Das steht in der Fundstelle für 2026. Nur der Betrag über der Limite wird besteuert.
> - **Kantone:** Diese Antwort gilt nur für den Bund. Für die Staats- und Gemeindesteuer eines Kantons (AR, SG, TG, ZH) habe ich nichts geprüft. Die kantonalen Limiten können abweichen. Nennen Sie mir den Kanton, dann schaue ich nach.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## b14

**Frage:** Ein Mandant wohnt am 31.12.2026 im Kanton Luzern und pendelt mit dem Auto zur Arbeit. Welcher Fahrkostenabzug gilt für die Luzerner Staats- und Gemeindesteuern 2026 und für die direkte Bundessteuer?

**Soll (Referenz):** Luzern ist im Wiki nicht abgedeckt (nur Bund, AR, SG, TG, ZH): kein Wert für die Luzerner Staats-/Gemeindesteuer nennen, auf kantonale Wegleitung verweisen. Für die direkte Bundessteuer 2026 gilt max. Fr. 3'300 (Wegleitung Bund 2026).

**Antwort des Agenten** (24.4 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Kanton Luzern (Staats- und Gemeindesteuern 2026): nicht im Wiki.**
> Das Steuer-Wiki deckt nur Bund, AR, SG, TG und ZH ab. Zum Luzerner Fahrkostenabzug nenne ich deshalb keinen Wert. Er ist weder belegt noch aus einem anderen Kanton übertragbar. Massgebend sind das Luzerner Steuergesetz und die Wegleitung zur Steuererklärung 2026 des Kantons Luzern, die ausserhalb des Wiki nachzuschlagen sind. Das Bundesrecht gilt für Luzern nicht automatisch: Kantone können eigene Höchstbeträge und Ansätze haben.
> 
> **Direkte Bundessteuer 2026 (Art. 26 Abs. 1 lit. a DBG):**
> 
> | Position | Wert | Status |
> |---|---|---|
> | Maximalabzug Fahrten Wohn-/Arbeitsstätte | CHF 3'300 pro Jahr | ☑️ agent-geprüft |
> | Privatauto | CHF 0.75 pro Fahrkilometer | ☑️ agent-geprüft |
> 
> - **Bedingung Privatauto:** Der km-Ansatz gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist. Das Gesamtmaximum von CHF 3'300 bleibt bestehen.
> - **Neu 2026:** Der Ansatz steigt von 0.70 auf 0.75. Er ist künftig an den TCS-Kilometerpreis gekoppelt und kann nach oben oder unten angepasst werden.
> - **Maximum:** CHF 3'300, gleich wie 2025.
> - **Zumutbarer ÖV:** Ist der öffentliche Verkehr zumutbar, wird in der Regel nur dessen Preis abgezogen und nicht der km-Ansatz fürs Auto. Das habe ich hier nicht im Einzelnen geprüft.
> 
> Fundstellen:
> - Maximum: `bund-dbg-2026__art-26`
> - 0.75 pro km: `bund-mm-2025-09-11-kalte-progression-2026__c0004`
> - Rundschreiben: `bund-rs-2-215`
> 
> **Praktisch:** Für die Luzerner Erklärung ist die kantonale Regelung separat zu klären. Der Bundesabzug gehört in die Spalte «Bund» derselben kantonalen Erklärung. Ob Luzern dort einen abweichenden Betrag verlangt, ist nicht geprüft. Die fachliche Beurteilung bleibt bei der Fachperson.

