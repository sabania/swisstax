# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 40 · Lauf: 2026-11-09 18:12
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q01

**Frage:** Mandantin (ZH, 2025) bringt: Lohnausweis, Krankenkassen-Prämienrechnung, Handyrechnung, 3a-Bescheinigung, Hausratversicherungspolice, Spendenquittung Rotes Kreuz CHF 80, Kita-Rechnungen. Welche sind relevant, wofür?

**Soll (Referenz):** Relevant: Lohnausweis (Einkünfte 1.1), Krankenkassenprämien (Versicherungsabzug Ziff. 15, Form. 365), 3a-Bescheinigung (Ziff. 14), Kita-Rechnungen (Ziff. 16.6 Drittbetreuung, max. 25'000 Kanton / 25'800 Bund). Spende CHF 80: unter Mindestbetrag 100 → nicht abziehbar (sofern Total < 100). Nicht relevant: Handyrechnung (Lebenshaltung), Hausratversicherung (kein Versicherungsabzug).

**Antwort des Agenten** (54.2 s · Tools: 14 Aufrufe read, steuerwiki__ablage, steuerwiki__beleg, steuerwiki__suche):

> Von den sieben Dokumenten sind fünf relevant. Die Handyrechnung und die Hausratpolice sind es nicht, und die Spende (CHF 80) führt für sich allein zu keinem Abzug. Alle Angaben gelten für ZH, Steuerjahr 2025. Die Wiki-Stände sind ☑️ agent-geprüft, die Abnahme steht noch aus.
> 
> | Dokument | Belegtyp | Steuerrelevant? | Wofür (ZH 2025) | Einreichen? | Kategorie (KATEGORIEN.md) |
> |---|---|---|---|---|---|
> | Lohnausweis | `lohnausweis` | ja | Ziff. 1.1 (Haupterwerb); je nach Fall Form. 360 (Berufsauslagen) | ja, immer (§ 134 Abs. 1 lit. a StG; zh-wl-2025__c0032) | **Belege eingereicht** (in der Liste ausdrücklich genannt) |
> | Krankenkassen-Prämienrechnung | `krankenkasse-praemien` | ja | Ziff. 15 Versicherungsabzug, über Form. 365 (Code 601, abzüglich Prämienverbilligung) | auf Verlangen. Das Formular 365 ist beizulegen, die Prämienbelege nicht (zh-wl-2025__c0207). | **Belege Sonstiges** (Zeile «Versicherungsprämien (Prämienbescheinigung), sofern nicht einzureichen») |
> | 3a-Bescheinigung | `bescheinigung-saeule3a` | ja | Ziff. 14.1/14.2 Säule 3a | ja (zh-wl-2025__c0081) | **Belege eingereicht** (ausdrücklich genannt) |
> | Kita-Rechnungen | `kinderbetreuung-rechnungen` | bedingt | Ziff. 16.6, höchstens CHF 25'000 (Kanton) bzw. 25'800 (Bund) je Kind | auf Verlangen. Die Aufstellung der Kosten mit Empfängern ist unaufgefordert beizulegen, die Rechnungen nur auf Verlangen. | **Belege Sonstiges** (Zeile «Kinderbetreuungskosten, sofern nicht einzureichen») |
> | Spendenquittung Rotes Kreuz, CHF 80 | `spendenbestaetigung` | bedingt, Bedingung hier nicht erfüllt | Ziff. 22.2 | auf Verlangen | siehe unten |
> | Hausratversicherungspolice | `hausrat-haftpflicht-police` | nein | – | nein | **keine Steuerbeleg-Kategorie** |
> | Handyrechnung | nicht erkannt, entspricht `privatrechnungen-alltag` | nein | – | nein | **keine Steuerbeleg-Kategorie** |
> 
> **Was bei den einzelnen Dokumenten zu beachten ist**
> - **Krankenkasse:** Der Abzug ist pauschal begrenzt, und eine erhaltene Prämienverbilligung wird abgezogen. Wurde sie schon mit der Prämienrechnung verrechnet, nicht doppelt kürzen. Die Rechnung nur für die tatsächlich im Jahr bezahlten Prämien verwenden. Für Zusatz- und Unfallprämien gelten die Codes 602/603 in Form. 365.
> - **Kita:** Der Abzug gilt nur für Kinder unter 14 Jahren im gleichen Haushalt und nur bei Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit. Die Verpflegung ist nicht abziehbar und muss herausgerechnet werden, wenn sie nicht separat ausgewiesen ist. Erhaltene Subventionen vermindern die Kosten.
> - **Spende:** Abziehbar ist erst ab CHF 100 Gesamttotal aller Spenden im Jahr, höchstens 20 % des Nettoeinkommens (zh-info-spenden__c0003). Mit CHF 80 allein gibt es in ZH und beim Bund keinen Abzug, und die Quittung hat dann keine Steuerbeleg-Kategorie. Gibt es weitere Spenden und liegt das Total bei CHF 100 oder mehr, gehört sie in **Belege Sonstiges**. Die Mandantin sollte das klären.
> - **Handy:** Telefon und Internet sind Lebenshaltungskosten, nicht abziehbar (§ 33 lit. a StG, zh-stg-2025__par-33). Rückfrage: Gibt es eine berufliche Nutzung, die der Arbeitgeber nicht erstattet? Dann sind nur effektive Berufskosten statt der Pauschale von 3 % denkbar (Form. 360, zh-wl-2025__c0067/c0069). Das müsste die Mandantin belegen.
> - **Hausrat:** Prämien für Hausrat- und Mobiliarversicherungen sind nicht abziehbar. Die Fundstelle dafür (ar-wl-2025__c0085) stammt aus AR und ist für ZH nicht einzeln belegt. Vom Typ her gibt es zudem keinen Wert in der Steuererklärung. Gehört das Dokument ausnahmsweise zu einer rückkaufsfähigen Lebensversicherung, wäre es Ziff. 30.3. Das sieht nach einer reinen Hausratpolice nicht danach aus.
> 
> **Unsicherheiten**
> - Die Zuordnungen der Liste sind laut Kopf der Datei noch nicht von consis bestätigt.
> - Bei der Spende ist die Typ-Erkennung nur «tief» und beim Handy fehlt sie. Die Einordnung stützt sich dort auf die Beschreibung in deiner Nachricht.
> - Wie hoch der Versicherungsabzug (Ziff. 15) und das Maximum für 3a (Ziff. 14) bei der Mandantin ausfallen, habe ich nicht geprüft. Das hängt vom Haushalt und von der Vorsorgesituation ab.
> 
> Als Nächstes: Werte erfassen mit `steuererklaerung-np`.

## q02

**Frage:** In welche Ziffer und mit welchem Code der ZH-Steuererklärung 2025 gehört der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb)?

**Soll (Referenz):** Ziff. 1.1 Haupterwerb, Code 100 (Person 1) / 101 (Person 2); Nettolohn Lohnausweis Ziff. 11 (zh-form-300-2025).

**Antwort des Agenten** (25.2 s · Tools: 2 Aufrufe steuerwiki__beleg, steuerwiki__position):

> Der Nettolohn aus Lohnausweis Ziff. 11 gehört in **Ziff. 1.1 «Haupterwerb unselbständig»** der ZH-Steuererklärung 2025 (Hauptformular, Form. 300). Für Person 1 ist das **Code 100**. Person 2 hätte Code 101.
> 
> - **Betrag:** Eingesetzt wird der Nettolohn gemäss Lohnausweis Ziff. 11. Das ist Ziff. 8 (Bruttolohn) minus Ziff. 9 (AHV/IV/EO/ALV/NBUV) minus Ziff. 10.1 und 10.2 (BVG). Bei mehreren Haupterwerben wird die Summe aller Ziff. 11 eingetragen.
> - **Staats- und Bundessteuer:** Es gibt eine Zeile für beide Spalten, der Betrag ist für Kanton und Bund gleich.
> - **Beilage:** Der Lohnausweis muss der Steuererklärung beigelegt werden (§ 134 Abs. 1 lit. a StG).
> - **BVG-Einkauf:** Ein Einkauf in Ziff. 10.2 ist im Nettolohn bereits abgezogen. Er darf deshalb nicht noch einmal unter Ziff. 16.1 (Code 280) abgezogen werden.
> - **Erwerbslücken:** Erwerbslücken (z.B. Arbeitslosigkeit oder Krankheit) müssen ausdrücklich bezeichnet werden.
> 
> Der Wiki-Status dieser Zuordnung ist ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme ist noch offen.
> 
> Fundstellen: zh-form-300-2025__c0004 («Haupterwerb Person 1 Lohnausweis», «Person 2 Lohnausweis 101»), zh-wl-2025__c0032 (Einreichepflicht).

## q03

**Frage:** Lohnausweis Feld F ist angekreuzt (Geschäftsauto). Was bedeutet das für den Fahrkostenabzug (SG 2025)?

**Soll (Referenz):** Feld F angekreuzt → kein Fahrkostenabzug für den Arbeitsweg mit Geschäftsfahrzeug (Privatanteil im Lohn, Lohnausweis Ziff. 2.2).

**Antwort des Agenten** (30.4 s · Tools: 3 Aufrufe steuerwiki__beleg, steuerwiki__wert, steuerwiki__position):

> **Kurzantwort (SG 2025): Wenn Feld F angekreuzt ist, gibt es in der Regel keinen Fahrkostenabzug für den Arbeitsweg (Formular 4 Ziff. 1, Kanton und Bund).**
> 
> **Warum**
> - Feld F bedeutet, dass dem Arbeitnehmer für den Arbeitsweg keine Kosten erwachsen. Das ist der Fall bei einem Sammeltransport, einem vom Arbeitgeber getragenen GA aus geschäftlichen Gründen oder einem Geschäftsfahrzeug, das auch für den Arbeitsweg zur Verfügung steht.
> - Beim Geschäftsauto steht in Ziff. 2.2 des Lohnausweises zusätzlich der Privatanteil von 0,9 % pro Monat (10,8 % pro Jahr). Dieser Privatanteil ist als Lohn aufgerechnet und versteuert. Er deckt den Arbeitsweg mit ab. Ein zusätzlicher Abzug wäre eine Doppelberücksichtigung.
> - Fundstellen: sg-wl-2025__c0075 («Ein Abzug für die Fahrt zur Arbeit ist deshalb nicht möglich»), sg-stb-39-3__c0013, sg-form-4-2025__c0001. Status ☑️ agent-geprüft (Abnahme offen).
> 
> **Was das praktisch heisst**
> - In Formular 4 tragen Sie bei Ziff. 1.1 bis 1.3 (Codes 400/404/406 für Person 1, 450/454/456 für Person 2) nichts ein.
> - Die Maximalabzüge von Fr. 8'000 (Kanton) und Fr. 3'300 (Bund) kommen nicht zur Anwendung, weil gar kein Abzug entsteht.
> 
> **Ausnahmen und Punkte zum Prüfen**
> 1. **Bordbuch:** Wird der Privatanteil nicht pauschal aufgerechnet, sondern effektiv mit Bordbuch abgerechnet, sind die effektiven Arbeitswegkosten bis zum Maximalabzug abziehbar (Form. 4 Ziff. 1.3, Fr. 0.70/km). Das gilt nur in diesem Fall.
> 2. **Fahrkostenentschädigung:** Zahlt der Arbeitgeber eine Entschädigung im Bruttolohn (Lohnausweis Ziff. 2.3), ist Feld F nicht anzukreuzen. Dann ist ein Abzug bis Fr. 8'000 (Kanton) bzw. Fr. 3'300 (Bund) möglich. Ein angekreuztes Feld F zusammen mit einer solchen Entschädigung wäre widersprüchlich und beim Arbeitgeber zu klären.
> 3. **Tatsächlich anderer Arbeitsweg:** Nutzt die Person für einzelne Wege ein anderes, selbst bezahltes Verkehrsmittel, ist das ein Sonderfall. Dazu steht im Wiki nichts Belegtes, ich würde ihn nicht pauschal abziehen. Er braucht eine Einzelfallprüfung.
> 4. **Anderes GA:** Ein vom Arbeitgeber bezahltes GA ohne geschäftliche Notwendigkeit gehört nicht in Feld F, sondern als Vorteil in den Lohn. Dann sind die Streckenabo-Kosten in Formular 4 abziehbar.
> 
> **Zu klären:** Steht in Ziff. 2.2 ein Privatanteil, und gibt es ein Bordbuch? Bei einem pauschalen Privatanteil ohne Bordbuch ist die Antwort eindeutig null. Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q04

**Frage:** Wie hoch ist der maximale Fahrkostenabzug 2025 in TG (Staatssteuer) und beim Bund, und welcher km-Ansatz gilt für das Auto?

**Soll (Referenz):** TG 2025 Staat max. CHF 6'000 (tg-stg__par-29), Bund max. CHF 3'300 (bund-dbg-2025__art-26); Auto TG gestaffelt 0.60/0.50/0.40 je nach Jahres-km, Bund 0.70.

**Antwort des Agenten** (25.0 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Steuerjahr 2025, Fahrkosten Wohn-/Arbeitsstätte**
> 
> | | Maximalbetrag | Auto (Privatfahrzeug) |
> |---|---|---|
> | **TG (Staatssteuer)** | **CHF 6'000** pro Jahr | gestaffelt: bis 3'000 km CHF 0.60/km, 3'001–5'000 km CHF 0.50/km, über 5'000 km CHF 0.40/km |
> | **Bund (dBSt)** | **CHF 3'300** pro Jahr | einheitlich **CHF 0.70/km** |
> 
> **TG**
> - Der Höchstbetrag von CHF 6'000 gilt für alle Fahrkosten zusammen, inklusive Wochenaufenthalt und Nebenerwerb. Bei unterjähriger Steuerpflicht oder Teilzeit wird er nicht gekürzt. (Fundstelle: tg-stg__par-29)
> - Der km-Ansatz fürs Auto gilt nur ausnahmsweise, nämlich wenn der öV nicht zumutbar ist. Im Normalfall werden die Kosten des öV-Abonnements abgezogen. Die Staffel wird stufenweise gerechnet und schliesst Parkgebühren ein (tg-bkv__par-1). Beispiel aus der Wegleitung: 8'000 km ergeben CHF 4'000.
> - Bei 100 % Tätigkeit rechnet man in der Regel mit maximal 225 Arbeitstagen (tg-wl-2025__c0003).
> 
> **Bund**
> - Der Höchstbetrag von CHF 3'300 steht in Art. 26 DBG (bund-dbg-2025__art-26). Der Ansatz von CHF 0.70/km steht in Anhang 1 der Berufskostenverordnung (bund-bkv-2025__anhang-1). Beim Bund gibt es keine Arbeitstage-Regel.
> - Im TG-Formular trägst du Kanton und Bund in derselben Erklärung ein, unter Ziff. 10.1 bzw. 10.2 (Berufsauslagen Person 1 bzw. 2). Der Bundesabzug wird dort separat auf CHF 3'300 begrenzt.
> 
> Alle Werte sind ☑️ agent-geprüft: Die Fundstellen sind geprüft, die Abnahme durch eine Fachperson steht noch aus.

## q05

**Frage:** Welcher km-Ansatz für Autos gilt 2026 bei der direkten Bundessteuer?

**Soll (Referenz):** CHF 0.75 pro km (bund-mm-2025-09-11-kalte-progression-2026__c0004; RS 2-215).

**Antwort des Agenten** (25.0 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Bund (direkte Bundessteuer), Steuerjahr 2026: CHF 0.75 pro Fahrkilometer** für das Privatauto. ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen)
> 
> - **Neu ab 2026:** Der Ansatz war bisher CHF 0.70. Er soll künftig an den TCS-Kilometerpreis gekoppelt werden und kann dann nach oben oder unten angepasst werden.
> - **Bedingung:** Der Abzug gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist.
> - **Gesamtmaximum:** CHF 3'300 pro Jahr für die Fahrten zwischen Wohn- und Arbeitsstätte (Art. 26 Abs. 1 lit. a DBG). Der Betrag ist gleich hoch wie 2025.
> - **Zum Vergleich:**
>   - Motorrad mit weissem Kontrollschild: CHF 0.40 pro km.
>   - Velo, Motorfahrrad und Motorrad mit gelbem Kontrollschild: Pauschale CHF 700 pro Jahr.
> 
> Fundstellen:
> - Auto-Ansatz: `bund-mm-2025-09-11-kalte-progression-2026__c0004`: «Der Abzug wird auf 75 Rappen pro Kilometer erhöht (bisher 70 Rappen).»
> - Maximum: `bund-dbg-2026__art-26`
> - Motorrad und Velo: `bund-rs-2-215__c0004`
> 
> Die kantonalen Ansätze für die Staats- und Gemeindesteuer können abweichen, ebenso die Anzahl anrechenbarer Arbeitstage. Für AR, SG, TG oder ZH kann ich das mit Kanton und Bund getrennt nachschlagen. Sagen Sie mir dafür den Kanton.

## q06

**Frage:** Maximaler Säule-3a-Abzug 2025 für eine Arbeitnehmerin mit Pensionskasse? Und für eine Selbständige ohne 2. Säule?

**Soll (Referenz):** Mit 2. Säule CHF 7'258; ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288 (bund-bsv-masszahlen-2025-2026__c0003).

**Antwort des Agenten** (26.5 s · Tools: 1 Aufrufe steuerwiki__wert):

> Steuerjahr 2025, Bundesrecht (Art. 7 BVV 3). Die Grenzen gelten für Bund und Kantone gleich. Ich habe deshalb keinen Kanton abgefragt.
> 
> | Fall | Maximaler Abzug 2025 | Quelle und Status |
> |---|---|---|
> | Arbeitnehmerin mit Pensionskasse (2. Säule) | **CHF 7'258** | bund-bsv-masszahlen-2025-2026__c0003 · ☑️ agent-geprüft |
> | Selbständige ohne 2. Säule | **20 % des Erwerbseinkommens, höchstens CHF 36'288** | bund-bvv3__art-7 und bund-bsv-masszahlen-2025-2026__c0003 · ☑️ agent-geprüft |
> 
> - **Mit 2. Säule:** Der Betrag ist ein Fixbetrag. Er entspricht 8 % des oberen BVG-Grenzbetrags.
> - **Ohne 2. Säule:** Der Höchstbetrag von CHF 36'288 entspricht 40 % des oberen BVG-Grenzbetrags. Er wird erst erreicht, wenn das Erwerbseinkommen mindestens CHF 181'440 beträgt. Das Erwerbseinkommen ist der Nettoerwerb aus der selbständigen Tätigkeit, also nach Abzug der AHV-Beiträge und der Geschäftsaufwendungen.
> 
> Ob jemand als «ohne 2. Säule» gilt, hängt davon ab, dass sie weder obligatorisch noch freiwillig einer Vorsorgeeinrichtung angeschlossen ist. Bei einer freiwilligen Unterstellung unter die 2. Säule gilt der kleine Betrag von CHF 7'258.
> 
> Die Zahlen sind agent-geprüft, die Abnahme ist noch offen. Die fachliche Beurteilung des Einzelfalls bleibt bei der Fachperson. Ein Einkauf fehlender 3a-Beiträge (Art. 7a BVV 3) ist für 2025 eine separate Frage. Sag Bescheid, falls du dazu etwas brauchst.

## q07

**Frage:** Kinderabzug 2025 in AR für ein 10-jähriges Kind – und beim Bund?

**Soll (Referenz):** AR 2025: CHF 7'400 (4.–15. Altersjahr; Anhang 1 StG, ar-stg-anhang-kp__c0001); Bund CHF 6'800 (Art. 35 DBG) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (30.8 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Kind, 10 Jahre alt, Steuerjahr 2025**
> 
> | | Kanton AR | Bund (dbg) |
> |---|---|---|
> | Kinderabzug vom Einkommen | **CHF 7'400** (4. bis 15. Altersjahr) | **CHF 6'800** (einheitlich, keine Altersstufen) |
> | Zuschlag Versicherungsabzug je Kind | CHF 1'000 | CHF 700 |
> | Abzug vom Steuerbetrag je Kind | nicht anwendbar | CHF 263 |
> | Vermögensfreibetrag je minderjähriges Kind | CHF 25'000 | keine Vermögenssteuer |
> 
> **Kanton AR**
> - Der Abzug steht in Ziff. 23.2 des Formulars.
> - Das Alter gilt per Stichtag 31.12.2025.
> - Das Gesetz nennt unindexiert CHF 7'000. Massgebend sind die indexierten CHF 7'400 (Anhang 1 StG, WL 2025).
> - Quellen: ar-stg-anhang-kp__c0001, ar-wl-2025__c0005 (☑️ agent-geprüft).
> 
> **Bund**
> - Der Abzug beträgt CHF 6'800 je Kind (bund-dbg-2025__art-35). Zusätzlich ermässigt sich der Steuerbetrag um CHF 263 je Kind (bund-dbg-2025__art-36-t4).
> - Der Versicherungsabzug erhöht sich um CHF 700 je Kind (bund-dbg-2025__art-33-t5).
> - Das AR-Formular hat keine Bundesspalte. Die Steuerverwaltung rechnet den Bundesabzug automatisch (ar-wl-2025__c0179). Sie müssen also nichts separat eintragen.
> - Alle Bundeswerte sind ☑️ agent-geprüft, die Abnahme ist offen.
> 
> **Voraussetzungen im Kanton (AR):**
> - Sie bestreiten den Unterhalt des Kindes zur Hauptsache, und das Kind ist darauf angewiesen.
> - Die Einkünfte des Kindes liegen unter CHF 18'000.
> - Sie machen für das Kind keinen Abzug für Unterhaltsbeiträge (Ziff. 12.2) geltend.
> - Sind die Eltern getrennt besteuert, gemeinsame Sorge und keine Unterhaltsbeiträge: Jeder Elternteil erhält je die Hälfte des Abzugs.
> 
> Nicht geprüft: die Bundesvoraussetzungen für den Kinderabzug eines minderjährigen Kindes bei getrennten Eltern. Die fachliche Beurteilung bleibt bei der Fachperson.

## q08

**Frage:** Versicherungsabzug ZH 2025 für ein Ehepaar mit 2 Kindern, beide mit Pensionskasse (Staatssteuer und Bund)?

**Soll (Referenz):** ZH Staat: 5'800 + 2 × 1'300 = 8'400; Bund: 3'700 + 2 × 700 = 5'100 (zh-stg-2025__par-31-t2, bund-dbg-2025__art-33).

**Antwort des Agenten** (29.2 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Versicherungsabzug ZH 2025, Ehepaar mit 2 Kindern, mit Beiträgen an Pensionskasse (2. Säule)**
> 
> | | Staatssteuer | Bundessteuer |
> |---|---|---|
> | Maximalabzug Ehepaar (Form. 365 Teil B, Code 611) | CHF 5'800 | CHF 3'700 |
> | Zuschlag je Kind (Code 613–615) | 2 × CHF 1'300 = 2'600 | 2 × CHF 700 = 1'400 |
> | **Maximaler Abzug total** | **CHF 8'400** | **CHF 5'100** |
> 
> Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Fundstellen**
> - Kanton: zh-stg-2025__par-31-t2 (5'800 Ehepaar, 1'300 je Kind).
> - Bund: bund-dbg-2025__art-33-t2 und art-33-t5 (3'700 Ehepaar, 700 je Kind).
> 
> **Wichtig für das Ausfüllen**
> - Das ist ein Höchstbetrag. Abgezogen wird der tiefere Betrag aus den tatsächlich bezahlten Prämien und dem Maximum, je Spalte getrennt (Ziff. 15, Code 270).
> - Die bezahlten Prämien (Form. 365 Teil A) sind die Summe aus:
>   - Krankenkassenprämien (Code 601),
>   - Unfallversicherung (Code 602),
>   - Lebens- und Rentenversicherung (Code 603),
>   - Zinsen von Sparkapitalien (Code 604).
> 
>   Davon wird die erhaltene Prämienverbilligung (Code 605) abgezogen, soweit sie nicht schon in 601 verrechnet ist. Die Kinderprämien gehören dazu.
> - Bei den Kindern ist der Zuschlag nur für Kinder möglich, für die der Kinderabzug nach § 34 Abs. 1 geltend gemacht werden kann.
> - Im Lohnausweis bereits abgezogene Prämien (NBUV) dürfen nicht nochmals erfasst werden.
> - Bei geteiltem Kinderabzug (z. B. getrennt besteuerte Eltern) beträgt der Zuschlag nur die Hälfte: Kanton 650, Bund 350 je Kind. Das betrifft hier nicht, wenn das Paar gemeinsam veranlagt wird.
> - Die höheren Beträge «ohne 2./3a» (Kanton 8'700, Bund 5'550, jeweils ohne Kinder) gelten nur, wenn weder die Steuerpflichtigen noch ihre Arbeitgeber Beiträge an 2. Säule oder Säule 3a geleistet haben. Sie sind hier nicht anwendbar.
> - Beide Ehegatten haben eine Pensionskasse, es gilt also die Variante «mit Vorsorge».
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q09

**Frage:** Wie hoch ist der Kinderdrittbetreuungsabzug 2025 im Kanton ZH, und gilt 2026 ein anderer Wert?

**Soll (Referenz):** ZH 2025 CHF 25'000 (StG Nachtrag 127, zh-stg-2025__par-31-t4); 2026 CHF 25'300 (zh-stg-2026__par-31-t3). Die VKP ab 2024 (10'400) ist überholt.

**Antwort des Agenten** (25.0 s · Tools: 2 Aufrufe steuerwiki__wert):

> Ja, 2026 gilt in ZH ein anderer Wert für die Staatssteuer: CHF 25'300 statt CHF 25'000. Beim Bund bleibt der Wert gleich.
> 
> | | Kanton ZH (Staatssteuer) | Bund (dBSt) |
> |---|---|---|
> | **2025** | **CHF 25'000** pro Kind | CHF 25'800 pro Kind |
> | **2026** | **CHF 25'300** pro Kind | CHF 25'800 pro Kind |
> 
> **Voraussetzungen** (2025 und 2026 gleich):
> - Das Kind hat das 14. Altersjahr noch nicht vollendet.
> - Das Kind lebt im gleichen Haushalt wie die Person, die für seinen Unterhalt sorgt.
> - Die Kosten sind nachgewiesen und stehen in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.
> - Der Höchstbetrag gilt pro Kind.
> - 2026, bei Konkubinat oder alternierender Obhut mit gemeinsamer Sorge: je halber Abzug, also CHF 12'650 pro Elternteil. Diese Regel steht in der Quelle zu 2026. Ob sie 2025 ebenso gilt, habe ich nicht geprüft.
> 
> **Formular:** Der Abzug gehört in die ZH-Steuererklärung unter Ziff. 16.6 «Abzug für fremdbetreute Kinder» (Code 376). Kanton und Bund werden mit derselben Position erfasst. Für das Ausfüllen kann ich `position zh <jahr> 16.6` aufrufen.
> 
> **Zum alten Wert:** Die Verordnung (VKP) ab 2024 nennt noch CHF 10'400. Das ist überholt. Es gilt das Gesetz in der Fassung der jeweiligen Jahresfassung, also Nachtrag 127 für 2025 und Nachtrag 132 für 2026.
> 
> **Quellen** (alle ☑️ agent-geprüft, Abnahme noch offen):
> - ZH 2025: `zh-stg-2025__par-31-t4`
> - ZH 2026: `zh-stg-2026__par-31-t3`
> - Bund 2025: `bund-dbg-2025__art-33-t7`
> - Bund 2026: `bund-dbg-2026__art-33-t7`
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## q10

**Frage:** Gibt es im Kanton TG einen Zweiverdienerabzug für die Staatssteuer?

**Soll (Referenz):** Nein, TG kennt keinen kantonalen Zweiverdienerabzug (nur Bund: 50 %, 8'600–14'100).

**Antwort des Agenten** (21.7 s · Tools: 1 Aufrufe steuerwiki__wert):

> Nein. Im Kanton TG gibt es für die Staats- und Gemeindesteuern keinen Zweiverdienerabzug (Steuerjahr 2025, da kein Jahr genannt war). Das Wiki zitiert dazu: «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.» (Chunk `tg-wl-2025__c0104`)
> 
> **Direkte Bundessteuer (nur dort)** – ☑️ agent-geprüft, Abnahme offen, Chunk `bund-dbg-2025__art-33-t6`:
> - Abzug: 50 % des niedrigeren Erwerbseinkommens.
> - Mindestens CHF 8'600, höchstens CHF 14'100.
> 
> **Im TG-Formular 2025:** Der Abzug steht unter Ziff. 18 (Code 356) und gilt nur für die direkte Bundessteuer.
> 
> Auf Wunsch rechne ich den Bundesabzug für einen konkreten Fall aus. Die fachliche Beurteilung bleibt bei der Fachperson.

## q11

**Frage:** SG 2025: Pauschale für übrige Berufskosten? Wie wird sie berechnet?

**Soll (Referenz):** SG 2025: CHF 700 + 10 % des Nettolohns, max. CHF 2'400 (Art. 21 StV SG, WL SG 2025).

**Antwort des Agenten** (25.4 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **SG 2025: Pauschale für übrige Berufskosten**
> 
> **Berechnung Kanton (Staats- und Gemeindesteuer):**
> Fr. 700 + 10 % des Nettolohns, höchstens Fr. 2'400. Es gibt kein Minimum.
> Formel: `min(700 + 10 % × Nettolohn; 2'400)`
> 
> - **Nettolohn:** Das ist der Nettolohn gemäss Lohnausweis (Ziff. 1.1 der Steuererklärung, Code 100/102). Gemeint sind die Bruttoeinkünfte abzüglich der Beiträge AHV/IV/EO/ALV/UV und BVG (ohne Einkäufe).
> - **Höchstbetrag:** Er wird ab einem Nettolohn von Fr. 17'000 erreicht.
> - **Teiljahr:** Bei einem Teiljahr wird umgerechnet.
> - **Eintrag im Formular:** Hilfsblatt Formular 4, Ziff. 3.1, Code 416 (Person 1) bzw. 466 (Person 2). Das Total aus Formular 4 kommt in die Steuererklärung, Ziff. 10.1 (Code 438) bzw. 10.2 (Code 488).
> 
> Fundstellen: sg-stv__art-21, sg-form-4-2025__c0003, sg-wl-2025__c0080 (☑️ agent-geprüft, Abnahme offen).
> 
> **Bund (direkte Bundessteuer):**
> 3 % des Nettolohns, mindestens Fr. 2'000, höchstens Fr. 4'000. Das Formular hat nur eine Spalte. Die Steuerbehörde nimmt die Anpassung für den Bund automatisch vor (Fundstellen: bund-bkv-2025__anhang-1, sg-wl-2025__c0173).
> 
> **Zu beachten:**
> - Die Pauschale gilt ohne Nachweis. Sie gilt sinngemäss auch bei Bezug von ALV-Taggeldern.
> - Wer ausbezahlte, nicht ereignisbezogene Pauschalspesen erhält, kann die Pauschale nicht zusätzlich geltend machen.
> - Mit der Pauschale ist auch das Arbeitszimmer abgegolten.
> - Übersteigen die tatsächlichen Kosten die Pauschale, können sie stattdessen belegt werden (Formular 4, Ziff. 3.2, Code 418/468). Dann müssen sämtliche übrigen Berufskosten inkl. Arbeitszimmer mit einem Beiblatt belegt werden. Entweder gilt die Pauschale oder die effektiven Kosten.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der zuständigen Fachperson.

## q12

**Frage:** Pauschalabzug Liegenschaftsunterhalt in AR für ein 8-jähriges Einfamilienhaus – und wie in ZH?

**Soll (Referenz):** AR: 10 % (Gebäude bis 10 Jahre) bzw. 20 % des Bruttoertrags, nur bis Bruttomietertrag 100'000 (Art. 25 StV AR, MB 03); ZH: einheitlich 20 % ohne Altersstaffel (ZStB 30.2).

**Antwort des Agenten** (34.0 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position):

> Annahme: Steuerjahr 2025, da du kein Jahr genannt hast. Die Pauschale ist ein Prozentsatz vom Brutto-Mietertrag bzw. vom Eigenmietwert, wenn du das Haus selbst bewohnst. Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> | | Kanton | Bund |
> |---|---|---|
> | **AR** (Gebäude 8 Jahre, also bis 10 Jahre) | **10 %** | **10 %** |
> | **ZH** | **20 %** | **10 %** |
> 
> **AR (Ziff. 15 der Steuererklärung, Formular 7)**
> - Für Gebäude bis und mit 10 Jahre gilt die Pauschale von 10 %. Ab 11 Jahren sind es 20 %. Die Pauschale gilt für Kanton und Bund gleich (ar-mb-03__c0004, ar-wl-2025__c0175).
> - Die Pauschale gibt es nur, wenn der jährliche Bruttomietertrag deines gesamten Liegenschaftsbesitzes höchstens CHF 100'000 beträgt. Die Liegenschaft muss ganz oder vorwiegend Wohnzwecken dienen.
> - Du kannst pro Gebäude und Jahr zwischen Pauschale und tatsächlichen Kosten wählen. Die Pauschale deckt alle Kosten ab.
> - Bei den tatsächlichen Kosten sind Einzelbeträge ab CHF 5'000 mit Rechnungskopie zu belegen.
> 
> **ZH (Hilfsblatt Form. 350, Übertrag in Ziff. 6, Code 188)**
> - Für die Staatssteuer gilt 20 %, ohne Staffelung nach Gebäudealter (zh-zstb-30-2__c0002).
> - Für die direkte Bundessteuer gilt bei einem Gebäude bis 10 Jahre 10 % (bund-lkv__art-5). Bei einem 8-jährigen Haus liegt die Bundespauschale also tiefer als die kantonale. Beim Bund sind es erst ab mehr als 10 Jahren 20 %.
> - Du kannst pro Liegenschaft und Steuerperiode wählen. Mit der Pauschale sind keine weiteren Abzüge möglich, ausser Baurechtszinsen. Alternativ rechnest du die tatsächlichen Kosten mit Aufstellung ab.
> 
> **Hinweise**
> - **Alter:** Beim Bund zählt das Alter zu Beginn der Steuerperiode. Prüfe, ob das Haus dann noch unter der 10-Jahres-Grenze liegt.
> - **Basis:** Bei Selbstnutzung rechnest du in ZH mit dem Eigenmietwert. In AR sagen die geprüften Quellen zur Basis bei Selbstnutzung nichts Genaueres als «Liegenschaftserträge» (Ziff. B); ob das den Eigenmietwert einschliesst, habe ich nicht geprüft.
> - **AR-Bund:** Das AR-Formular hat keine eigene Bundesspalte. Die Bundesanpassung macht die Steuerverwaltung automatisch.
> - **Abzug lohnt sich nur bei hohen Kosten:** Ob die Pauschale oder die tatsächlichen Kosten günstiger sind, hängt davon ab, ob deine effektiven Unterhaltskosten über dem Pauschalbetrag liegen.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q13

**Frage:** TG: Welcher Einschlag gilt auf dem Eigenmietwert der selbstbewohnten Liegenschaft am Wohnsitz (Kanton vs. Bund)?

**Soll (Referenz):** TG: Abzug 40 % Kanton, 20 % Bund für dauernd selbstbewohntes Eigentum am Wohnsitz (tg-stg__par-23; WL TG 2025).

**Antwort des Agenten** (25.8 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **TG, Steuerjahr 2025** (kein Jahr angegeben, daher 2025 verwendet)
> 
> Für Eigenmietwert-Abzüge bei am Wohnsitz dauernd selbstbewohntem Wohneigentum gilt der Selbstnutzungsabzug vom Mietwert:
> 
> | | Selbstnutzungsabzug auf dem Eigenmietwert |
> |---|---|
> | **Kanton (Staats- und Gemeindesteuer)** | **40 %** (§ 23 StG TG, tg-stg__par-23 «Abzug von 40 Prozent») |
> | **Bund (direkte Bundessteuer)** | **20 %** (tg-wl-2025__c0225 «kantonal einen Abzug von 40% und beim Bund von 20%») |
> 
> Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Praktisch im Formular**
> - Der Mietwert aus Selbstnutzung stammt aus der rechtskräftigen Schätzung und ist mit dem Mietwertindex der Steuerperiode bereinigt (Liegenschaftensteuerrechnung).
> - Der steuerbare Eigenmietwert ist je Spalte unterschiedlich: Staat = Mietwert × (1 − 40 %), Bund = Mietwert × (1 − 20 %). Die Nettoerfolge für Staat und Bund sind daher getrennt zu rechnen (Formular 7, Übertrag in Ziff. 8.1, Code 180).
> - Der Unterhalt wird danach abgezogen, entweder effektiv (Formular 8) oder pauschal mit 10 % (Gebäude bis 10 Jahre) bzw. 20 % (älter). Die Pauschale gilt für Kanton und Bund gleich.
> 
> **Voraussetzungen**
> - Der Abzug gilt nur für am Wohnsitz dauernd selbstbewohntes Eigentum.
> - Zweit- und Ferienwohnungen, landwirtschaftlich geschätzte Liegenschaften und an Nahestehende überlassene Objekte sind zu 100 % des Mietwerts steuerbar.
> - Auf Formular 7 darf bei solchen Objekten die Checkbox «Am Wohnsitz selbstgenutzt» nicht angekreuzt werden.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q14

**Frage:** Bis wann kann ein Treuhänder im Kanton TG für seine Mandanten Fristerstreckung erhalten?

**Soll (Referenz):** Gewerbsmässige Treuhänder für Mandanten bis 31.12. des Deklarationsjahres (StP 155 Nr. 2).

**Antwort des Agenten** (26.8 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Im Kanton Thurgau können gewerbsmässige Treuhänder und Steuerberater für ihre Mandanten längstens bis zum 31. Dezember des Deklarationsjahres eine Fristerstreckung beantragen.** Das Deklarationsjahr ist das Jahr der Einreichung. Für das Steuerjahr 2025 ist das also der 31. Dezember 2026. Ich habe 2025 angenommen, weil Sie kein Steuerjahr genannt haben. Die Praxis StP 155 Nr. 2 gilt ausdrücklich auch für 2026 und 2027.
> 
> - **Privatpersonen:** Das erste Gesuch läuft grundsätzlich bis 30. September des Deklarationsjahres. Weitere Gesuche sind in begründeten Fällen bis 30. November möglich.
> - **Gesuch:** Es geht schriftlich, begründet und rechtzeitig an das Gemeindesteueramt.
> - **Gesuche über die Maximalfrist hinaus:** Sie werden nur bei ausserordentlichen Gründen gutgeheissen, die substanziiert dargelegt werden. Starke berufliche Auslastung des Vertreters oder fehlende Unterlagen genügen nicht. Arbeitsüberlastung ist generell kein Grund (Fundstelle: tg-stp-155-2__c0002 und tg-stp-155-2__c0001).
> - **Gebühr:**
>   - Die erste Fristerstreckung ist gebührenfrei.
>   - Jedes weitere Gesuch kostet eine Kanzleigebühr von Fr. 30 (§ 39b Abs. 2 und 3 StV TG).
>   - Ab der zweiten Mahnung fällt eine Mahngebühr von Fr. 50 an (§ 39b Abs. 4 StV TG).
>   - Das Wiki nennt für natürliche Personen keine abweichende Gebühr. Ob § 39b StV TG auch für Gesuche an das Gemeindesteueramt gilt, habe ich nicht geprüft.
> - **Bund:** Die direkte Bundessteuer regelt die Frist nicht gesondert. Die kantonale Fristerstreckung gilt auch dafür.
> 
> Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die fachliche Beurteilung bleibt bei der Fachperson.

## q15

**Frage:** ZH: Bis wann ist die Steuererklärung 2025 einzureichen und wie lange wird höchstens Fristerstreckung gewährt?

**Soll (Referenz):** Einreichung bis 31.03.2026; Fristerstreckung längstens bis 30. November (ZStB 132.1 / WL ZH 2025).

**Antwort des Agenten** (26.7 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__zeige):

> **ZH, Steuerjahr 2025**
> 
> - **Einreichefrist:** Die Steuererklärung 2025 ist bis **31. März 2026** einzureichen, online oder beim Scan-Center. Quelle: zh-wl-2025__c0017 (☑️ agent-geprüft).
> - **Fristerstreckung:** Rechtzeitig eingereichten Gesuchen ist **längstens bis 30. November 2026** zu entsprechen, also bis 30. November des Folgejahres der Steuerperiode. Quelle: zh-zstb-132-1__c0024 (☑️ agent-geprüft).
> - **Gesuch:** Es muss **vor Fristablauf** beim Gemeindesteueramt gestellt werden. Laut Wiki gilt das erste Gesuch ohne gegenteiligen Entscheid als stillschweigend bewilligt.
> - **Bund:** Die direkte Bundessteuer hat keine eigene Frist. Die kantonale Frist und Fristerstreckung gelten auch für den Bund (Art. 119 DBG).
> 
> **Zu heute (9. November 2026):** Die ordentliche Frist vom 31. März 2026 ist abgelaufen. Eine bereits abgelaufene Frist kann nicht mehr erstreckt werden. Gesuche nach Ablauf werden abgewiesen. Möglich ist dann nur noch die **Wiederherstellung der Frist**, wenn die Voraussetzungen von § 15 StV bzw. Art. 119 Abs. 2 DBG erfüllt sind. Dafür ist bei natürlichen Personen das Gemeindesteueramt zuständig.
> 
> Wurde rechtzeitig eine Erstreckung beantragt oder bewilligt, läuft sie höchstens bis zum 30. November 2026. Das sind noch gut drei Wochen.
> 
> Nicht geprüft: Kosten einer Fristerstreckung (in den Quellen nicht genannt) und ob für einen konkreten Fall eine längere oder kürzere Frist bewilligt wurde. Die fachliche Beurteilung bleibt bei der Fachperson.

## q16

**Frage:** AR: Was kostet die zweite Fristverlängerung?

**Soll (Referenz):** CHF 25 (erste Verlängerung kostenlos, jede weitere CHF 25; MB 18 / WL AR 2025).

**Antwort des Agenten** (25.2 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **AR, Steuerjahr 2025 (kein Jahr genannt, daher 2025 angenommen):** Die zweite Fristverlängerung kostet **CHF 25**.
> 
> - Die erste Fristverlängerung ist kostenlos. Jede weitere kostet CHF 25 (`ar-wl-2025__c0012`, ☑️ agent-geprüft, Abnahme offen).
> - Rechtsgrundlage ist Art. 59a Abs. 1 StV AR (`ar-stv__art-59a`). Er sieht vor, dass die erstmalige Fristerstreckung kostenlos ist und jede weitere kostenpflichtig. Die Höhe richtet sich nach der Kanzleigebührenverordnung (Abs. 3).
> - Das Merkblatt AR 18 nennt für «Fristverlängerungen (im Wiederholungsfall)» ebenfalls Fr. 25. Die Gebührenansätze gelten dort ab 1.9.2025 (`ar-mb-18__c0001`).
> - Das Gesuch muss vor Ablauf der Einreichefrist bei der Kantonalen Steuerverwaltung eingehen. Online geht es über esteuern.ar.ch.
> - Die Gebühr betrifft die Fristerstreckung der kantonalen Steuererklärung. Diese deckt auch die direkte Bundessteuer ab, denn der Bund regelt die Fristerstreckung nicht gesondert.
> 
> Nicht belegt ist, ob die Gebühr bei Treuhänder-Sammelgesuchen anders ausfällt. Dazu habe ich in den Quellen nichts gefunden.

## q17

**Frage:** Krankheitskosten SG 2025: Ab welchem Selbstbehalt sind sie abziehbar – und beim Bund?

**Soll (Referenz):** SG: Selbstbehalt 2 % (Art. 46 StG SG); Bund: 5 % (Art. 33 Abs. 1 lit. h DBG, KS 11).

**Antwort des Agenten** (29.9 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__zeige):

> **Krankheits- und Unfallkosten, Steuerjahr 2025**
> 
> Abziehbar ist nur der Teil der selbst getragenen Kosten, der den Selbstbehalt übersteigt. Der Selbstbehalt beträgt:
> 
> | | Selbstbehalt | Bezugsgrösse | Fundstelle |
> |---|---|---|---|
> | **SG** (Staats- und Gemeindesteuer) | **2 %** | Nettoeinkünfte (= Nettoeinkommen, Ziff. 20 im Formular) | Art. 46 Abs. 1 lit. a StG SG (`sg-stg-2025__art-46`) |
> | **Bund** (direkte Bundessteuer) | **5 %** | Einkünfte, vermindert um die Aufwendungen nach Art. 26–33 DBG | Art. 33 Abs. 1 lit. h DBG (`bund-dbg-2025__art-33-t3`) |
> 
> Beide Werte sind ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme ist offen.
> 
> **Im SG-Formular 2025**
> - Die Kosten gehören in Ziff. 21.1. Die Vorkolonne (Code 650) enthält die Summe aus Rechnungen abzüglich Leistungen Dritter, also Krankenkasse, Versicherung oder Hilflosenentschädigung.
> - Der Selbstbehalt hat Code 238, der Abzug Code 240.
> - Abzug = max(0; Vorkolonne − 2 % × Ziff. 20).
> - Das Formular hat nur eine Spalte. Den abweichenden Bundesabzug (5 %) berechnet die Steuerbehörde automatisch (Merkblatt 32, `sg-wl-2025__c0173`).
> 
> **Weitere Punkte**
> - Nur die tatsächlich selbst getragenen Kosten zählen, auch für unterhaltene Personen. Die Krankenkassenprämien gehören nicht hierher, sie kommen in Ziff. 14.
> - Behinderungsbedingte Kosten sind ohne Selbstbehalt abziehbar. Sie gehören in Ziff. 21.2, beim Bund in Art. 33 Abs. 1 lit. hbis DBG.
> - Die Diät-Pauschale (z. B. Zöliakie) beträgt Fr. 2'500. Sie fällt unter den Selbstbehalt und braucht erstmals eine ärztliche Bescheinigung.
> - Einzelrechnungen werden im Formular 6 aufgeführt, Belege nur auf Verlangen. Verweist man auf den Krankenkassenzusammenzug, muss die detaillierte Leistungsübersicht zwingend beiliegen.
> 
> Die fachliche Beurteilung des Einzelfalls bleibt bei der Fachperson.

## q18

**Frage:** PK-Einkauf CHF 20'000 wurde über den Lohn abgezogen (Lohnausweis Ziff. 10.2). Darf er nochmals in der Steuererklärung abgezogen werden?

**Soll (Referenz):** Nein – BVG-Einkauf über Lohnabzug (Lohnausweis Ziff. 10.2) ist bereits im Nettolohn berücksichtigt; nur direkt bezahlte Einkäufe separat abziehen.

**Antwort des Agenten** (45.8 s · Tools: 8 Aufrufe steuerwiki__beleg, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Nein, nicht nochmals abziehen.** Der Einkauf ist bereits berücksichtigt, wenn Sie den Nettolohn (Ziff. 11) deklarieren. Ein zweiter Abzug in der Steuererklärung wäre ein Doppelabzug. Ich gehe vom Steuerjahr 2025 aus, weil Sie keines genannt haben. Einen Kanton habe ich nicht genannt bekommen.
> 
> **Begründung**
> - Ziff. 11 des Lohnausweises ist der für die Steuererklärung massgebende Nettolohn. Er ergibt sich aus dem Bruttolohn (Ziff. 8) abzüglich der Abzüge nach Ziff. 9 **und 10**. Der Einkauf in Ziff. 10.2 ist also schon abgezogen (`bund-wl-lohnausweis-2026__c0038`, Wegleitung Lohnausweis 2026; für 2025 habe ich keine eigene Fundstelle geöffnet). ☑️
> - Das Merkblatt 21 EDP (Bund) sagt dasselbe. Alle vom Lohn abgezogenen PK-Beiträge stehen im Lohnausweis. Auf der Bescheinigung der Pensionskasse (Formular 21 EDP) stehen nur Beträge, die Sie selbst überwiesen haben und die nicht vom Lohn abgezogen wurden (`bund-mb-21edp__c0006`, Rz 11–12). ☑️
> - Die Wegleitung ZH 2025 (Ziff. 16.1) lässt den Abzug nur zu, «soweit die … deklarierten Einkünfte nicht bereits um diese Beiträge gekürzt worden sind» (`zh-wl-2025__c0092`). ☑️ Das gilt für Zürich. Die Fundstellen für SG, TG und AR habe ich nicht geöffnet.
> 
> **Praktisch**
> - Als Einkommen aus unselbständiger Erwerbstätigkeit gehört der **Nettolohn Ziff. 11** in die Steuererklärung, nicht der Bruttolohn Ziff. 8.
> - Einen separaten Abzug für Einkäufe können Sie nur für Beträge geltend machen, die Sie **zusätzlich selbst** an die Pensionskasse überwiesen haben. Dafür brauchen Sie die Bescheinigung der Pensionskasse. Die CHF 20'000 aus Ziff. 10.2 gehören nicht dazu.
> - Wurde in der Steuererklärung oder in einer Software der Bruttolohn eingesetzt, wäre der Einkauf zusätzlich als Abzug zu erfassen. Das führt zum gleichen Ergebnis wie der Nettolohn. Wichtig ist, dass der Einkauf nur einmal abgezogen wird.
> 
> **Beachten**
> - Der Einkauf ist nur abziehbar, soweit er im Rahmen der Einkaufsmöglichkeit der Pensionskasse liegt.
> - Er ist nicht abziehbar, wenn innerhalb von 3 Jahren ein Kapitalbezug erfolgt. Dasselbe gilt für Einkäufe, solange frühere WEF-Vorbezüge nicht zurückbezahlt sind. Das kann zu einer Aufrechnung führen.
> 
> Wenn Sie mir den Wohnsitzkanton am 31.12. nennen (ZH, SG, TG oder AR), suche ich die genaue Ziffer im Formular und die kantonale Regel heraus.

## q19

**Frage:** Weiterbildungskosten CHF 15'000 (ZH, 2025), Arbeitgeber hat nichts bezahlt. Wie viel ist abziehbar (Kanton/Bund)?

**Soll (Referenz):** ZH Staat max. CHF 12'400 (zh-stg-2025__par-31-t4); Bund max. CHF 13'000 (bund-dbg-2025__art-33-t4).

**Antwort des Agenten** (27.9 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **ZH, Steuerjahr 2025: Weiterbildungskosten CHF 15'000, vom Arbeitgeber nichts übernommen**
> 
> | | Selbst getragen | Limite | Abziehbar | Nicht abziehbar |
> |---|---|---|---|---|
> | **Kanton (Staatssteuer)** | 15'000 | 12'400 | **CHF 12'400** | 2'600 |
> | **Bund (dir. Bundessteuer)** | 15'000 | 13'000 | **CHF 13'000** | 2'000 |
> 
> Die Limiten gelten je Person. Bei Ehepaaren kann jede Person bis zu ihrer eigenen Limite abziehen. Das Wiki führt diese Werte mit Status ☑️ agent-geprüft, die Abnahme ist noch offen.
> 
> **Fundstellen**
> - Kanton: zh-stg-2025__par-31-t4 («bis zum Gesamtbetrag von Fr. 12 400»)
> - Bund: bund-dbg-2025__art-33-t4 («bis zum Gesamtbetrag von 13 000 Franken»)
> - Wegleitung ZH: zh-wl-2025__c0093
> 
> **Eintrag im Formular**
> - Es gilt Ziff. 16.2, Code 292, mit dem Hilfsblatt Form. 367.
> - Im Hilfsblatt kommt unter «Total der Kosten» (2900) 15'000 hinein.
> - Unter «Beitrag Arbeitgeber» (2901) steht 0.
> - Daraus ergeben sich «Selbstgetragene Kosten» (2902) von 15'000.
> - Der zulässige Abzug (2920) beträgt im Block Staatssteuer 12'400 und im Block Bundessteuer 13'000.
> - Im Hauptformular steht 12'400 in der Spalte Staatssteuer und 13'000 in der Spalte Bundessteuer.
> 
> **Voraussetzungen, die ich nicht prüfen kann**
> - Es muss ein Abschluss Sek. II vorliegen oder das 20. Altersjahr vollendet sein.
> - Es darf sich nicht um die Ausbildung bis zum ersten Sek.-II-Abschluss handeln.
> - Die Weiterbildung muss berufsorientiert sein (inkl. Umschulung).
> - Massgebend ist die Zahlung bzw. Fälligkeit im Jahr 2025, nicht der Kursbesuch. Es zählen also nur Rechnungen, die 2025 bezahlt wurden oder fällig waren.
> - Das Form. 367 ist vollständig ausgefüllt beizulegen. Die Rechnungen und Zahlungsbelege müssen nur auf Verlangen eingereicht werden.
> - Ziff. 13.3 im Lohnausweis sollte leer sein. Falls der Arbeitgeber doch Beiträge direkt ans Bildungsinstitut bezahlt hat, stehen diese nicht im Lohnausweis. Sie wären dann von den 15'000 abzuziehen.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q20

**Frage:** Spenden CHF 50 an eine gemeinnützige Organisation (TG 2025) – abziehbar?

**Soll (Referenz):** Nein – TG: Zuwendungen nur abziehbar, wenn sie CHF 200 übersteigen (StG TG § 34 Abs. 1 Ziff. 11); Bund: ab CHF 100.

**Antwort des Agenten** (31.6 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Nein, bei CHF 50 allein ist nichts abziehbar, weder im Kanton noch beim Bund.** Das gilt für TG, Steuerjahr 2025, wenn die Organisation steuerbefreit ist und ihren Sitz in der Schweiz hat.
> 
> | | Regel | Bei CHF 50 |
> |---|---|---|
> | **Kanton TG** (Staats- und Gemeindesteuer) | Nur der Teil über CHF 200 Gesamtbetrag ist abziehbar (Selbstbehalt). Quelle: `tg-form-06-2025__c0002`, `tg-stg__par-34-t4` ☑️ | 50 − 200 < 0, also **CHF 0** |
> | **Bund** (direkte Bundessteuer) | Abziehbar erst, wenn die Spenden im Steuerjahr zusammen mindestens CHF 100 erreichen. Dann gibt es keinen Selbstbehalt. Quelle: `bund-dbg-2025__art-33a` ☑️ | 50 < 100, also **CHF 0** |
> 
> **Zählen Sie Ihre Spenden zusammen.** Die Schwellen gelten für die Summe aller freiwilligen Zuwendungen im Jahr, nicht pro Spende. Dafür gibt es das Formular 6 (Code 366, Ziff. 23.2). Beispiele, jeweils ohne Berücksichtigung der Obergrenze von 20 % des Nettoeinkommens:
> - Bei insgesamt CHF 150 wären beim Bund CHF 150 abziehbar, im Kanton noch CHF 0.
> - Bei insgesamt CHF 350 wären im Kanton CHF 150 abziehbar (350 − 200) und beim Bund CHF 350.
> 
> **Voraussetzungen für den Abzug überhaupt:**
> - Die Organisation muss in der Schweiz ansässig und steuerbefreit sein. Ob sie anerkannt ist, zeigt die Liste der Steuerverwaltung TG.
> - Nicht abziehbar sind Spenden für religiöse, kulturelle, gesellige oder sportliche Zwecke, an ausländische Organisationen sowie ehrenamtliche Arbeit.
> - Im Formular 6 muss jede Institution einzeln mit Name und Sitz stehen. «Diverse Organisationen» wird nicht anerkannt.
> - Eine Quittung müssen Sie nur beilegen, wenn eine einzelne Zuwendung CHF 1'000 oder mehr beträgt. Darunter reicht es, sie aufzubewahren, die Steuerverwaltung kann sie auf Verlangen einfordern.
> - Parteispenden gehören in Ziff. 15.5 und nicht in Ziff. 23.2.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson. Alle Quellen oben haben den Status «☑️ agent-geprüft», die Abnahme ist also noch offen.
> 
> Wenn Sie 2025 weitere Spenden geleistet haben, nennen Sie mir das Total. Dann rechne ich den Abzug für Kanton und Bund durch.

## q21

**Frage:** Was ändert sich 2026 bei der Säule 3a (Einkauf) und wo wird das im ZH-Formular 2026 eingetragen?

**Soll (Referenz):** Ab 2026 Einkauf (Nachzahlung) Säule 3a für Beitragslücken ab 2025 (max. 7'258 pro Einkaufsjahr, BVV 3 Art. 7a, KS 18a); ZH-Formular 2026: Ziff. 14.3 (Code 264, Detailfelder 276/278).

**Antwort des Agenten** (24.3 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Kanton ZH, Steuerjahr 2026**
> 
> ## Was sich 2026 ändert
> Neu ab Steuerperiode 2026 kann man zusätzlich zu den ordentlichen 3a-Beiträgen **Beitragslücken in die Säule 3a einkaufen**. (☑️ agent-geprüft, Quelle: zh-wl-2026-uj__c0077)
> 
> - **Welche Lücken zählen:** Nur Lücken, die ab 1.1.2025 entstanden sind, und zwar innerhalb der zehn Jahre vor dem Einkauf. Für 2026 ist deshalb faktisch nur die Lücke 2025 einkaufbar.
> - **Voraussetzungen:**
>   - In den Lückenjahren wurden AHV/IV/EO-Beiträge geleistet.
>   - Im Einkaufsjahr wurde der ordentliche Maximalbeitrag voll einbezahlt. Das sind CHF 7'258 mit 2. Säule, bzw. 20 % des Erwerbseinkommens, höchstens CHF 36'288, ohne 2. Säule.
> - **Limite:** höchstens die Summe der Lücken, in jedem Fall maximal **CHF 7'258**. Die Limite ist für Kanton und Bund gleich (Bund: bund-wl-2a-2026__c0051).
> - **Unverändert:** Die ordentlichen Maxima bleiben bei CHF 7'258 (mit 2. Säule) bzw. CHF 36'288 (ohne). Sie gelten seit 2025.
> 
> ## Wo im ZH-Formular
> - **Ziff. 14.3 «Einkauf Säule 3a (neu ab 2026)»**
>   - Person 1: Code **276**
>   - Person 2: Code **278**
>   - Summe in Hauptkolonne Code **264**
>   - Kanton und Bund werden gleich behandelt.
> - **Rechnung je Person:** min(Einkauf; Summe der Lücken ab 1.1.2025; 7'258).
> - **Ordentliche Beiträge** stehen separat in **Ziff. 14.1 / 14.2** (Code 260/261, effektiv 262/263). Der Einkauf gehört nicht dorthin.
> - **Belege:**
>   - Einkaufsbescheinigung der 3a-Einrichtung.
>   - 3a-Bescheinigung über den ordentlichen Beitrag, als Nachweis des vollen Maximalbeitrags.
>   - Nachweis der AHV/IV/EO-Beiträge im Lückenjahr.
> 
> ## Vorbehalte
> - Das reguläre ZH-Formular und die Wegleitung 2026 sind per 09.11.2026 noch nicht publiziert. Ziffern und Codes stützen sich auf die Fassung für unterjährige Steuerpflicht (zh-form-300-2026-uj, zh-wl-2026-uj, Chunk c0008). **Sie müssen am regulären Formular geprüft werden.**
> - Die Rechtsgrundlage (Artikel BVV 3) ist nur aus der Wegleitung belegt, nicht aus einem geprüften Gesetzeschunk.
> - Alle Werte haben den Status ☑️ (Abnahme offen). Die fachliche Beurteilung bleibt bei der Fachperson.

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (32.0 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__position):

> **Kurzantwort:** Natürliche Personen fordern die Verrechnungssteuer (VSt) nicht mit einem eigenen Antrag zurück. Sie deklarieren die Dividenden im Wertschriftenverzeichnis ihrer kantonalen Steuererklärung. Der Anspruch ergibt sich dort als 35 % vom Bruttoertrag der Kolonne A. Eine separate Bundesformular-Erklärung gibt es dafür nicht.
> 
> Ich habe das Steuerjahr 2025 angenommen. Die Verrechnungssteuer ist Bundesrecht und gilt für alle Kantone gleich. Die Formularposition hängt aber vom Wohnsitzkanton am 31.12. ab. Unten stehen die vier abgedeckten Kantone. Sagen Sie mir, welcher es ist, dann gehe ich gezielt auf Ihren Fall ein.
> 
> ## Ablauf
> 
> 1. **Dividenden erfassen:** Schweizer Dividenden und Zinsen mit VSt-Abzug gehören ins Wertschriftenverzeichnis in **Kolonne A** (Werte mit Verrechnungssteuerabzug). Der Bruttoertrag ist der Betrag vor Abzug. Werte ohne VSt-Abzug kommen in Kolonne B.
> 2. **Anspruch berechnen:** Der Anspruch beträgt 35 % von Total A. In Zürich wird er auf 5 Rappen gerundet.
> 3. **Beleg bereithalten:** Grundlage ist der Steuerauszug der Bank oder der Post, auch als eSteuerauszug. Er dient zur Kontrolle des VSt-Betrags. Beizulegen ist er nur bedingt, nämlich wenn das Wertschriftenverzeichnis auf das Steuerverzeichnis der Bank verweist, statt die Titel einzeln aufzulisten.
> 4. **Erklärung einreichen:** Die Steuererklärung mit dem Wertschriftenverzeichnis gilt als Rückerstattungsantrag. Das Verzeichnis ist zu unterschreiben, und die Bankverbindung (IBAN) ist anzugeben.
> 5. **Verrechnung oder Auszahlung:** Die VSt wird mit der Steuerrechnung verrechnet. Ein Überschuss wird zurückerstattet.
> 
> ## Wo der Anspruch ausgewiesen wird (2025)
> 
> | Kanton | Position | Fundstelle |
> |---|---|---|
> | **ZH** | Form. 340, Totale: «Verrechnungssteueranspruch 35 %» (Code **540**). Total Steuerwert (Code 400) geht in Hauptformular Ziff. 30.1, Total Bruttoertrag A + B (Code 150) in Ziff. 4.1. | zh-form-340-2025__c0005 |
> | **SG** | Form. 2, Code **999**: «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A)» | sg-form-2-2025__c0006 |
> | **TG** | Form. 2, Ziff. **10**: «Verrechnungssteueranspruch: 35 % von Bruttoertrag Total A» | tg-form-02-2025__c0006 |
> | **AR** | Form. 2, Code **999**: «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A)» | ar-form-02-2025__c0007 |
> 
> Der Status der Fundstellen ist 🟡 extrahiert bzw. ☑️ agent-geprüft, die Abnahme ist noch offen.
> 
> ## Beachten
> 
> - **Frist:** Der Anspruch erlischt, wenn er nicht innert drei Jahren nach Ablauf des Fälligkeitsjahres geltend gemacht wird. Diese Angabe stammt aus dem Zürcher Eintrag (zh-wl-2025__c0173). Ich habe sie nicht für die anderen Kantone oder im Gesetzestext geprüft.
> - **Vollständig deklarieren:** Die Dividenden müssen im Verzeichnis stehen, sonst gibt es keine Rückerstattung. Ich habe die gesetzlichen Folgen bei nicht deklarierten Erträgen nicht geprüft.
> - **Ausländische Dividenden:** Sie unterliegen nicht der Schweizer VSt. Eine ausländische Quellensteuer wird über das Formular DA-1 angerechnet. Das ist ein anderes Verfahren.
> - **Säule 3a und Vorsorge:** Der Vorsorgenehmer hat bei einer Wertschriftenanlage keinen Anspruch auf Rückerstattung der VSt (bund-ks-18a__c0041).
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q23

**Frage:** Vergleiche den Versicherungsabzug 2025 für Alleinstehende ohne Kinder in AR, SG, TG, ZH und beim Bund.

**Soll (Referenz):** Alleinstehend ohne Kinder 2025 (mit 2. Säule/3a): AR 2'700 · SG 3'400 · TG 3'500 · ZH 2'900 · Bund 1'800.

**Antwort des Agenten** (26.7 s · Tools: 3 Aufrufe steuerwiki__vergleich, steuerwiki__wert):

> **Versicherungsabzug 2025, alleinstehend, ohne Kinder** (Prämien und Sparzinsen, Höchstbetrag)
> 
> | | Bund | ZH | SG | TG | AR |
> |---|---|---|---|---|---|
> | **Mit Beiträgen an 2. Säule/3a** | CHF 1'800 | CHF 2'900 | CHF 3'400 | **CHF 3'500** | CHF 2'700 |
> | **Ohne Beiträge an 2. Säule/3a** | CHF 2'700 | CHF 4'350 | CHF 3'900 | kein separater Betrag | kein separater Betrag |
> 
> Alle Werte haben den Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Fundstellen**
> - Bund: bund-dbg-2025__art-33-t2 (CHF 1'800) und bund-rs-2-210__c0006 (CHF 2'700).
> - ZH: zh-stg-2025__par-31-t2 (CHF 2'900) und zh-wl-2025__c0084 (CHF 4'350).
> - SG: sg-stg-2025__art-45-t2 (CHF 3'400 und CHF 3'900).
> - TG: tg-stg__par-34-t3.
> - AR: ar-stg__art-35-t2.
> 
> **Einordnung**
> - **Mit Beiträgen an 2. Säule/3a** hat TG den höchsten Abzug (CHF 3'500). Es folgen SG (3'400), ZH (2'900) und AR (2'700). Der Bund liegt mit CHF 1'800 am tiefsten.
> - **Ohne solche Beiträge** hat ZH den höchsten Abzug (CHF 4'350). Es folgen SG (3'900) und der Bund (2'700).
> - **TG** kennt gemäss Wiki keine Erhöhung für Personen ohne Vorsorgebeiträge. Es gilt CHF 3'500 in beiden Fällen.
> - **AR** kennt ebenfalls keine Unterscheidung. Es gilt CHF 2'700 in beiden Fällen.
> - **AR: Prämienverbilligung.** Der AR-Betrag von CHF 2'700 ist gemäss Fundstelle um die erhaltene Prämienverbilligung zu kürzen. Für die anderen Kantone und den Bund habe ich dazu nichts geprüft.
> - **Kanton und Bund** werden getrennt erfasst. Die Bundesspalte gilt für die direkte Bundessteuer.
> 
> Welche Spalte gilt, hängt davon ab, ob die Person 2025 tatsächlich Beiträge an die 2. Säule oder 3a geleistet hat. Die genaue Voraussetzung (Art. 33 DBG) habe ich nicht im Wortlaut geprüft. Die fachliche Beurteilung bleibt bei der Fachperson.

## q24

**Frage:** Steuerfreie Vermögensbeträge (Sozialabzüge) 2025 in SG für ein Ehepaar mit einem minderjährigen Kind?

**Soll (Referenz):** SG 2025: 150'000 (Ehepaar) + 20'000 pro minderjähriges Kind = 170'000 (sg-stg-2025__art-64).

**Antwort des Agenten** (26.7 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__zeige, steuerwiki__rechne):

> **SG 2025, Ehepaar mit einem minderjährigen Kind: steuerfreies Vermögen (Sozialabzug Vermögen) CHF 170'000.**
> 
> | Teil | Betrag | Grundlage |
> |---|---|---|
> | Gemeinsam steuerpflichtige Ehegatten (2 × Fr. 75'000) | CHF 150'000 | Art. 64 Abs. 1 lit. a StG SG, `sg-stg-2025__art-64`; Betrag für Ehepaare: `sg-wl-2025__c0118` |
> | 1 minderjähriges Kind (zusätzlich) | CHF 20'000 | Art. 64 Abs. 1 lit. b StG SG, `sg-stg-2025__art-64` |
> | **Total** | **CHF 170'000** | |
> 
> Status der Werte: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> - **Kind:** Der Zusatzabzug gilt nur für ein minderjähriges Kind unter der elterlichen Sorge oder Obhut, für das ein Kinderabzug nach Art. 48 Abs. 1 lit. a StG SG beansprucht werden kann.
> - **Stichtag:** Massgebend sind die Verhältnisse am Ende der Steuerperiode (Art. 64 Abs. 2), also am 31.12.2025.
> - **Wirkung:** Der Abzug wird vom Reinvermögen abgezogen. Nur der Rest ist steuerbar. Das Vermögen ist bis CHF 170'000 also steuerfrei.
> - **Formular:** Die Sozialabzüge Vermögen stehen im Formular SG 2025 unter Ziff. 36.1–36.3. Die Zuordnung der drei Ziffern (alleinstehend, gemeinsam, Kinder) konnte ich im Wiki nicht einzeln öffnen: `position` hat «36.2» nicht gefunden. Welche Ziffer für Ehepaar und Kind gilt, ist also nicht geprüft.
> - **Bund:** Die direkte Bundessteuer kennt keine Vermögenssteuer, es gibt daher keinen Bundesabzug.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q25

**Frage:** Welcher Verzugszins gilt 2026 für die direkte Bundessteuer?

**Soll (Referenz):** 4.00 % (RS 2-215, bund-rs-2-215__c0010/c0011).

**Antwort des Agenten** (20.4 s · Tools: 1 Aufrufe steuerwiki__wert):

> Für die direkte Bundessteuer gilt 2026 ein **Verzugszins von 4 %**.
> 
> - **Fundstelle:** bund-rs-2-215__c0010, «Verzugs- und Rückerstattungszins 4,50 4,00». Der Status ist ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> - **Vorjahr:** 2025 lag der Satz bei 4,50 %.
> - **Rückerstattungszins:** Er beträgt 2026 ebenfalls 4,00 %.
> - **Vergütungszins:** Auf Vorauszahlungen gibt es 2026 0,00 % (2025: 0,75 %).
> - **Ausgleichszins:** Den kennt der Bund nicht. Die Kantone regeln ihn für ihre eigenen Steuern selbst.
> 
> Auf welchen Betrag und ab welchem Zeitpunkt der Verzugszins läuft, habe ich nicht geprüft. Für eine konkrete Berechnung brauche ich den Fälligkeitstermin. Den geben die Kantone bekannt.

## q26

**Frage:** Wann wird der Eigenmietwert abgeschafft und gilt das schon für 2026?

**Soll (Referenz):** Abschaffung per 1.1.2029 (Bundesratsbeschluss 01.04.2026); für 2025–2028 gilt bisheriges Recht – 2026 also noch Eigenmietwert.

**Antwort des Agenten** (27.9 s · Tools: 5 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurz: Nein, für 2026 gilt der Eigenmietwert weiterhin. Die Abschaffung tritt am 1. Januar 2029 in Kraft, also erstmals für das Steuerjahr 2029.**
> 
> **Ablauf**
> - Im September 2025 haben Volk und Stände den Bundesbeschluss über die kantonalen Liegenschaftssteuern auf Zweitliegenschaften angenommen. Damit haben sie auch der Abschaffung der Eigenmietwertbesteuerung auf Erst- und Zweitliegenschaften zugestimmt (bund-mm-eigenmietwert-abschaffung__c0003).
> - Der Bundesrat hat am 1. April 2026 das Inkrafttreten auf den **1. Januar 2029** festgelegt (…__c0002).
> - Der Bundesrat hat sich nach der Konsultation für 2029 entschieden, weil die Kantone dann die besondere Liegenschaftssteuer gleichzeitig mit der Abschaffung einführen können (…__c0003).
> 
> **Für 2026 (und bis und mit 2028)**
> - Der Eigenmietwert bleibt bei Bund, Kantonen und Gemeinden steuerbar. Der Unterhaltskostenabzug und die Schuldzinsen bleiben wie bisher abzugsfähig.
> - Bei der direkten Bundessteuer ist ein Pauschalabzug von 10 % (Gebäude bis 10 Jahre) oder 20 % (Gebäude über 10 Jahre) möglich (bund-lkv__art-5, ☑️ agent-geprüft).
> - Wie stark der Eigenmietwert reduziert wird, regelt jeder Kanton selbst. Für 2026 gilt: ZH 10 %, SG 30 %, TG 40 %, AR 20 %. Alle Werte sind ☑️ agent-geprüft; die Abnahme ist offen.
> 
> **Was sich ab 2029 ändert** (…__c0004)
> - Der Eigenmietwert entfällt für selbstgenutztes Wohneigentum. Gleichzeitig entfällt der Abzug der Unterhaltskosten bei Bund, Kantonen und Gemeinden.
> - Bei vermieteten oder verpachteten Liegenschaften bleibt der Unterhaltskostenabzug erhalten.
> - Schuldzinsen sind nur noch im Verhältnis des Werts der vermieteten oder verpachteten Liegenschaften zum gesamten Vermögen abzugsfähig.
> - Wer erstmals in der Schweiz ein Eigenheim erwirbt, erhält einen zeitlich und betragsmässig begrenzten Ersterwerberabzug für Schuldzinsen.
> - Bei der direkten Bundessteuer entfallen die Abzüge für Energiespar- und Umweltschutzinvestitionen. Die Kantone können sie zeitlich begrenzt weiterführen.
> - Die Kantone können auf überwiegend selbstgenutzten Zweitliegenschaften eine Objektsteuer erheben.
> 
> **Nicht geprüft:** Wie die vier Kantone AR, SG, TG und ZH die Reform umsetzen, habe ich nicht abgeklärt. Das betrifft die Objektsteuer auf Zweitliegenschaften und die Übergangsregelungen, zum Beispiel für den Unterhalt in den Jahren 2027 und 2028. Ein Wohnsitzkanton würde ich dafür gezielt nachschlagen.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q27

**Frage:** Zitiere die Regel zum Abzug privater Schuldzinsen im DBG (Steuerjahr 2025) mit Artikel.

**Soll (Referenz):** Art. 33 Abs. 1 lit. a DBG (Fassung 2025): private Schuldzinsen im Umfang der steuerbaren Vermögenserträge (Art. 20, 20a, 21) und weiterer CHF 50'000.

**Antwort des Agenten** (22.1 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Art. 33 Abs. 1 lit. a DBG** (Fassung für das Steuerjahr 2025, gültig bis 31.12.2025; Quelle: `bund-dbg-2025__art-33-t1`):
> 
> > «Von den Einkünften werden abgezogen:
> > a. die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken. Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten oder ihr sonst wie nahe stehenden natürlichen Person zu Bedingungen gewährt, die erheblich von den im Geschäftsverkehr unter Dritten üblichen Bedingungen abweichen;»
> 
> **Kurz eingeordnet:**
> - Der Abzug ist begrenzt auf die steuerbaren Vermögenserträge (Art. 20, 20a, 21 DBG) plus 50 000 Franken.
> - Schuldzinsen auf Darlehen einer Kapitalgesellschaft an eine massgeblich beteiligte oder nahestehende Person sind nicht abzugsfähig, wenn die Bedingungen erheblich von den unter Dritten üblichen abweichen.
> 
> Ich habe nur den Gesetzestext zitiert. Die Anwendung im Einzelfall habe ich nicht geprüft, etwa bei fremdfinanzierten Kapitalversicherungen (KS 22a, Ziff. 3.3). Die Beurteilung bleibt bei der Fachperson.

## q28

**Frage:** Ist ein Leasingvertrag für das Privatauto steuerlich relevant? Was ist mit den Leasingraten?

**Soll (Referenz):** Leasingraten sind keine Schuldzinsen und grundsätzlich nicht abziehbar (Lebenshaltung); relevant nur für Fahrkosten-Begründung/Geschäftsauto, Vermögen (kein Eigentum).

**Antwort des Agenten** (30.7 s · Tools: 5 Aufrufe steuerwiki__beleg, steuerwiki__suche, read, steuerwiki__zeige):

> **Kurz:** Der Leasingvertrag ist für ein Privatauto **nicht steuerrelevant**, und die Leasingraten sind **nicht abziehbar**. Kanton und Jahr haben Sie nicht genannt. Die Antwort gilt unabhängig vom Kanton, ich habe das Steuerjahr 2025 verwendet.
> 
> **Leasingraten**
> - Sie sind private Lebenshaltungskosten. Der Zinsanteil in der Rate ist kein Schuldzins, weil die Raten für privat genutzte Güter keine abzugsfähigen Zinsanteile enthalten. Bund: KS 22a Ziff. 3.3, `bund-ks-22a__c0015` ☑️.
> - Die Rate gehört deshalb weder ins Schuldenverzeichnis noch unter «Schuldzinsen».
> - Auch die Kantone sehen das so. Die ZH-Wegleitung 2025 zu Ziffer 12 sagt: «Nicht abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den darin enthaltenen Zinsanteilen)», `zh-wl-2025__c0073`. Die Belegkarte des Wiki zitiert diesen Satz ohne das «Nicht». Das ist ein Fehler in der Karte, die Quelle sagt das Gegenteil.
> 
> **Vermögen**
> - Ein geleastes Auto gehört dem Leasinggeber. Sie deklarieren es nicht als Fahrzeug im Vermögen, und es gibt dafür auch keine Schuld. ☑️
> 
> **Was Sie stattdessen abziehen können**
> - Der Fahrkostenabzug für den Arbeitsweg ist unabhängig vom Leasing. Er ist nur mit Auto möglich, wenn dessen Benutzung begründet ist, etwa weil kein öffentliches Verkehrsmittel besteht oder die Zeitersparnis über einer Stunde liegt (Bund Formular 9–14 Ziff. 9).
> - Der Ansatz beträgt Auto CHF –.70 pro km, höchstens CHF 3'300 bei der direkten Bundessteuer (Art. 5 BKV, `bund-form-9-14-2025__c0002`). Bei der direkten Bundessteuer sind damit die Leasingkosten abgegolten.
> - Der Maximalbetrag der Kantone kann abweichen. Dafür bräuchte ich den Kanton: `wert <kt> 2025 fahrkosten`.
> 
> **Ausnahmen, in denen der Vertrag doch relevant ist**
> - **Selbständig Erwerbende:** Der Geschäftsanteil des Leasingaufwands gehört in die Jahresrechnung. Dazu brauche ich Angaben zum Anteil.
> - **Geschäftsfahrzeug des Arbeitgebers:** Hier gelten andere Regeln für die private Nutzung (Art. 5a BKV). Das ist ein anderer Fall als ein Privatauto.
> 
> **Ablage:** Eine Steuerbeleg-Kategorie aus `KATEGORIEN.md` ist nicht passend, weil kein Wert in die Steuererklärung kommt. Sie können das Dokument in «Unterlagen Kunde» ablegen oder gar nicht ablegen. Falls der Arbeitsweg per Auto geltend gemacht wird, ist stattdessen der Nachweis dazu relevant. Die jährliche Kilometerleistung aus dem Vertrag kann dafür nützlich sein.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson. Nennen Sie mir Kanton und Sachverhalt (Arbeitsweg, selbständig oder angestellt), dann rechne ich den Fahrkostenabzug konkret durch.

## q29

**Frage:** Wie hoch ist der Kinderabzug im Kanton Bern 2025?

**Soll (Referenz):** Nicht im Wiki (nur Bund, AR, SG, TG, ZH).

**Antwort des Agenten** (23.7 s · Tools: 1 Aufrufe steuerwiki__wert):

> Den Kinderabzug für den Kanton Bern 2025 kann ich nicht nennen: Bern ist im Steuer-Wiki **nicht abgedeckt**. Das Wiki kennt nur den Bund sowie die Kantone AR, SG, TG und ZH. Einen Wert aus einem dieser Kantone setze ich für Bern nicht ein. Eine Schätzung wäre hier unseriös. Den Berner Betrag finden Sie im Steuergesetz des Kantons Bern oder in der Wegleitung der Steuerverwaltung Bern für 2025.
> 
> Die direkte Bundessteuer gilt auch für Bern. Sie wird in der Berner Steuererklärung zusammen mit der Kantonssteuer erfasst. Für 2025 gilt beim Bund (Status ☑️ agent-geprüft, Abnahme offen):
> 
> - **Kinderabzug vom Einkommen:** CHF 6'800 pro minderjähriges oder in Ausbildung stehendes Kind. Beim Bund gibt es keine Altersstaffel. Quelle: `bund-dbg-2025__art-35`
> - **Abzug vom Steuerbetrag:** zusätzlich CHF 263 pro Kind, nach dem Elterntarif. Beide Abzüge gelten nebeneinander. Quelle: `bund-dbg-2025__art-36-t4`
> - **Versicherungsabzug:** Zuschlag von CHF 700 pro Kind. Quelle: `bund-dbg-2025__art-33-t5`
> 
> Diese Bundeswerte sind nicht der Berner Kinderabzug. Der kantonale Abzug ist eine eigene Zahl.

## q30

**Frage:** Ehepaar TG 2025, beide angestellt (Nettolohn 80'000 und 30'000), pendelt mit ÖV-Abo (CHF 1'200 bzw. 900). Erstelle die Abzüge Berufskosten (Fahrkosten, Verpflegung ohne Kantine, Pauschale übrige) je Person für Kanton und Bund mit Fundstellen.

**Soll (Referenz):** TG 2025 je Person: Fahrkosten = ÖV-Abo effektiv (1'200 bzw. 900; Max. 6'000 Staat / 3'300 Bund); Verpflegung ohne Kantine 15/Tag, max. 3'200 (beide Ebenen); übrige Pauschale 3 %: P1 80'000 → 2'400, P2 30'000 → 900 → Minimum 2'000 (beide Ebenen, BKV TG § 4a / BKV Bund).

**Antwort des Agenten** (44.9 s · Tools: 9 Aufrufe read, steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **Mandant: Ehepaar · Kanton: TG · Steuerjahr: 2025 · Formular: Hilfsblatt 4.2 (Person 1) und 4.3 (Person 2), Übertrag in Steuererklärung Ziff. 10.1 und 10.2**
> 
> Annahmen, weil Angaben fehlen:
> - Nettolohn = Lohnausweis Ziff. 11.
> - Kein Geschäftsfahrzeug, Feld F und Feld G im Lohnausweis nicht angekreuzt, keine Fahrkostenvergütung durch den Arbeitgeber.
> - Verpflegung: Mit «ohne Kantine» habe ich den vollen Abzug von Fr. 15 pro Tag angesetzt. Weil Tage und Pensum fehlen, nehme ich den Jahreshöchstbetrag von Fr. 3'200 an (100 %, ständige auswärtige Verpflegung).
> 
> ## Person 1 (Nettolohn 80'000, Formular 4.2)
> 
> | Ziffer / Code | Position | Kanton | Bund | Regel / Limite | Status |
> |---|---|---|---|---|---|
> | 2.1 / 206, Total 2.5 / 213 | Fahrkosten ÖV-Abo | 1'200 | 1'200 | tatsächliche Kosten, begrenzt auf Kanton 6'000, Bund 3'300 (beide nicht erreicht) | ☑️ |
> | 3.1 / 214 | Verpflegung auswärts, ohne Verbilligung | 3'200 | 3'200 | Fr. 15 pro Tag, max. Fr. 3'200 | ☑️ |
> | 4 / 220 | Übrige Berufskosten (Pauschale) | 2'400 | 2'400 | 3 % × 80'000 = 2'400, innerhalb 2'000–4'000 | ☑️ |
> | 7 / 240 | **Total Berufsauslagen** | **6'800** | **6'800** | 1'200 + 3'200 + 2'400 | ☑️ |
> 
> ## Person 2 (Nettolohn 30'000, Formular 4.3, Codes 246–280)
> 
> | Ziffer / Code | Position | Kanton | Bund | Regel / Limite | Status |
> |---|---|---|---|---|---|
> | 2.1 / 246, Total 2.5 / 253 | Fahrkosten ÖV-Abo | 900 | 900 | wie oben | ☑️ |
> | 3.1 / 254 | Verpflegung auswärts, ohne Verbilligung | 3'200 | 3'200 | wie oben | ☑️ |
> | 4 / 260 | Übrige Berufskosten (Pauschale) | 2'000 | 2'000 | 3 % × 30'000 = 900, daher Minimum 2'000 | ☑️ |
> | 7 / 280 | **Total Berufsauslagen** | **6'100** | **6'100** | 900 + 3'200 + 2'000 | ☑️ |
> 
> Total beider Personen: Kanton 12'900, Bund 12'900.
> 
> Kanton und Bund sind hier gleich hoch, weil die Fahrkosten unter beiden Limiten liegen. Das Formular hat zwei Spalten: links Staats- und Gemeindesteuer, rechts direkte Bundessteuer. Die Pauschale für übrige Berufskosten ersetzt nur Ziff. 4. Fahrkosten und Verpflegung kommen dazu.
> 
> ## Fundstellen
> - **Pauschale übrige Berufskosten:**
>   - Kanton: tg-bkv__par-4a «Pauschalabzug 3 Prozent des Nettolohnes, mindestens Fr. 2'000 und höchstens Fr. 4'000»; tg-form-04-2-2025__c0004; tg-wl-2025__c0187.
>   - Bund: bund-bkv-2025__anhang-1 «3 % des Nettolohns, mindestens im Jahr 2000.—», «höchstens 4000.—».
> - **Fahrkosten:**
>   - Kanton: tg-stg__par-29 «Maximalbetrag von Fr. 6'000»; tg-form-04-2-2025__c0002; tg-wl-2025__c0177.
>   - Bund: bund-dbg-2025__art-26 «Maximalbetrag von 3300 Franken».
> - **Verpflegung:**
>   - Kanton: tg-bkv__par-2-t1 «Fr. 15 für jede auswärtige Hauptmahlzeit», «Fr. 3'200 im Jahr»; tg-form-04-2-2025__c0003; tg-wl-2025__c0183.
>   - Bund: bund-bkv-2025__anhang-1 «Voller Abzug 15.—», «im Jahr 3200.—».
> - **Total und Übertrag:** tg-form-01-2025__c0010 (10.1 Code 240, 10.2 Code 280); tg-form-04-2-2025__c0010; tg-wl-2025__c0196.
> 
> Alle Werte haben den Status ☑️ (Fundstelle geprüft, Abnahme offen).
> 
> ## Offene Punkte für die Fachperson
> 1. **Verpflegung, Person 2:** Der Lohn von 30'000 deutet auf ein Teilzeitpensum hin. Der Abzug ist dann gekürzt: min(Arbeitstage × 15; 3'200 × Beschäftigungsgrad). Bei 50 % wären es 1'600, das Total Person 2 sinkt auf 4'500. Pensum und Arbeitstage bitte klären.
> 2. **Verpflegung, beide:** Der Abzug gilt nur, wenn die Heimkehr am Mittag unzumutbar ist (grosse Entfernung oder sehr kurze Pause). Das habe ich angenommen, aber nicht belegt. Ohne diese Voraussetzung entfallen 3'200 pro Person.
> 3. **Lohnausweise prüfen:** Feld F (angekreuzt heisst keine Fahrkosten), Feld G (angekreuzt heisst nur halber Verpflegungsabzug, Fr. 7.50 pro Tag, max. Fr. 1'600) und Lohnausweis Ziff. 2.3 (vom Arbeitgeber vergütete Fahrkosten).
> 4. **Abo-Belege:** Die Abokosten sind nachzuweisen (Rechnung oder Quittung). Ob sie eingereicht werden müssen, ist im Wiki «unklar». Mit Abo-Quittungen bereithalten.
> 5. **Unterjährige Erwerbstätigkeit:** Bei weniger als 12 Monaten werden Verpflegung und Pauschale anteilmässig gekürzt (Tage/360).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q31

**Frage:** Ehepaar ZH 2026, beide erwerbstätig, Kind 3 Jahre in der Kita (Kosten CHF 30'000). Wie viel Drittbetreuung ist abziehbar (Kanton und Bund)?

**Soll (Referenz):** ZH 2026 Kanton max. CHF 25'300 pro Kind (zh-stg-2026__par-31-t3); Bund 2026 max. CHF 25'800 (bund-dbg-2026__art-33-t7). Abzug je Ebene getrennt.

**Antwort des Agenten** (24.9 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **Abziehbare Drittbetreuung ZH 2026 (Ziff. 16.6, Code 376):**
> 
> | | Kosten | Höchstbetrag pro Kind | Abzug |
> |---|---|---|---|
> | **Kanton (Staatssteuer)** | 30'000 | 25'300 | **CHF 25'300** |
> | **Bund (dBSt)** | 30'000 | 25'800 | **CHF 25'800** |
> 
> Die nicht abziehbaren Kosten betragen damit 4'700 (Kanton) bzw. 4'200 (Bund).
> 
> Fundstellen (☑️ agent-geprüft, Abnahme offen):
> - Kanton: zh-stg-2026__par-31-t3
> - Bund: bund-dbg-2026__art-33-t7
> - Formular: zh-form-300-2026-uj__c0008
> 
> **Voraussetzungen, die Sie prüfen sollten:**
> - Das Kind hat das 14. Altersjahr noch nicht vollendet. Das ist bei 3 Jahren erfüllt (Jahrgang 2012–2026).
> - Das Kind lebt im gleichen Haushalt.
> - Beide Ehegatten sind gleichzeitig erwerbstätig, in Ausbildung oder erwerbsunfähig. Das ist hier erfüllt.
> - Die Kosten fallen während der Arbeitszeit an.
> - Zum Nachweis brauchen Sie die Kita-Rechnungen mit Zahlungsnachweis. Dazu kommt eine Aufstellung der Fremdbetreuungskosten.
> - Die CHF 30'000 müssen reine Betreuungskosten sein. Verpflegung gehört dazu, wenn sie in der Kita-Rechnung enthalten ist. Sind nur pauschale Beträge ausgewiesen, werden 20 % als Lebenshaltungskosten gekürzt. Das würde den Abzug nur dann senken, wenn die Kosten nach Kürzung unter die Höchstbeträge fallen. Bei 30'000 × 80 % = 24'000 wäre das der Fall.
> 
> **Hinweis zum Formular:** Das reguläre ZH-Formular und die Wegleitung für 2026 sind noch nicht publiziert (Stand 09.11.2026). Die Ziffer und der Code stützen sich auf die Fassung für unterjährige Steuerpflicht. Bitte prüfen Sie diese am regulären Formular. Die Höchstbeträge selbst stammen aus dem Gesetzestext (StG bzw. DBG) und sind davon nicht betroffen.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q32

**Frage:** SG 2025: Einfamilienhaus (Baujahr 2010), selbst bewohnt. Pauschalabzug Liegenschaftsunterhalt Kanton und Bund?

**Soll (Referenz):** SG 2025: 20 % des Eigenmietwerts, ohne Altersstaffel (sg-stv__art-29); Bund: Gebäude zu Beginn 2025 über 10 Jahre alt → 20 % (bund-lkv__art-5).

**Antwort des Agenten** (25.4 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **SG 2025, selbst bewohntes Einfamilienhaus (Baujahr 2010): Pauschalabzug 20 % im Kanton und 20 % beim Bund**
> 
> | | Satz | Status | Fundstelle |
> |---|---|---|---|
> | **Kanton SG** (Staats- und Gemeindesteuer) | **20 %** | ☑️ agent-geprüft | sg-stv__art-29 |
> | **Bund** (direkte Bundessteuer) | **20 %** | ☑️ agent-geprüft | bund-lkv__art-5 |
> 
> - **Kanton:** SG kennt keine Staffelung nach Gebäudealter. Der Satz beträgt 20 % für Gebäude bis und über 10 Jahre.
> - **Bund:** Das Gebäude ist zu Beginn der Steuerperiode 2025 etwa 15 Jahre alt. Es gilt deshalb die Stufe «mehr als zehn Jahre», also 20 %. Die Stufe von 10 % gilt nur für Gebäude bis zehn Jahre.
> 
> **Bemessungsgrundlage**
> - Die Pauschale beträgt 20 % des angerechneten Eigenmietwerts, also nach der 30-%-Herabsetzung (sg-stg-2025__art-34). Das ist die Summe aus Formular 7 Teil B.
> - Beim Bund nennt die Verordnung den «Brutto-Mietertrag». Im SG-Formular gibt es nur eine Spalte. Die Abweichungen für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor (sg-wl-2025__c0173). Die Bundesbasis für den Eigenmietwert habe ich nicht separat geprüft.
> 
> **Eintrag im Formular**
> - Der Abzug kommt in Formular 7 Teil C und wird nach Ziff. 15 (Code 716) übertragen.
> - Der Eigenmietwert steht unter Ziff. 5 (Code 712).
> 
> **Wahlrecht und Belege**
> - Sie können pro Liegenschaft und Steuerperiode zwischen der Pauschale und den tatsächlichen Kosten wählen.
> - Die Pauschale umfasst auch Denkmalpflege sowie Energiespar- und Umweltinvestitionen.
> - Wertvermehrende Aufwendungen sind nicht abziehbar.
> - Bei der Pauschale sind keine Belege einzureichen. Bei tatsächlichen Kosten werden sie auf Verlangen verlangt.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q33

**Frage:** ZH 2025: Kind 19 Jahre, in Lehre (Ausbildung). Kinderabzug Kanton und Bund?

**Soll (Referenz):** ZH 2025 Kanton CHF 9'300 (volljährig in Erstausbildung, zh-stg-2025__par-34); Bund CHF 6'800 (bund-dbg-2025__art-35) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (30.5 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__zeige):

> **Ja, das Kind hat Anspruch auf den vollen Kinderabzug, im Kanton und beim Bund.** Eine Lehre gilt als berufliche Erstausbildung. Das Kind ist am 31.12.2025 volljährig, deshalb gelten zusätzliche Voraussetzungen (unten).
> 
> **Kinderabzug ZH 2025, Ziff. 24.1** (☑️ agent-geprüft)
> 
> | | Kanton (Staatssteuer) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | Kinderabzug je Kind | **CHF 9'300** | **CHF 6'800** |
> | Zusätzlicher Versicherungsabzug je Kind (Form. 365, Code 613) | CHF 1'300 | CHF 700 |
> 
> - **Kind im eigenen Haushalt:** Code 370.
> - **Kind ausserhalb des Haushalts** (z.B. Wochenaufenthalt oder eigene Wohnung): Code 372.
> - Quellen Kinderabzug: `zh-stg-2025__par-34`, `zh-form-300-2025__c0010`, `bund-dbg-2025__art-35`.
> - Quellen Versicherungsabzug: `zh-form-365-2025__c0002`, `bund-dbg-2025__art-33-t5`.
> 
> **Voraussetzungen für ein volljähriges Kind**
> - Das Kind steht am 31.12.2025 in beruflicher Erstausbildung. Beim Kanton gilt: Lehrvertrag oder Schule mindestens halbtags und mindestens ein halbes Jahr.
> - Sie bestreiten den Unterhalt zur Hauptsache, und das Kind ist auf die Unterstützung angewiesen. Das wird beim Kanton ausdrücklich verlangt (`zh-stg-2025__par-34`). Beim Bund nennt der Wortlaut von Art. 35 diese Bedingung im geprüften Auszug nicht. Ob sie dort gleich streng gilt, habe ich nicht geprüft.
> - Bei einer Lehre kann das Kind einen Lehrlingslohn haben. Ob damit noch der Hauptunterhalt bei Ihnen liegt, hängt vom Einzelfall ab. Eine feste Lohngrenze habe ich im Wiki nicht gefunden.
> - Belege: Lehrvertrag oder Lehrbestätigung. Wohnt das Kind nicht bei Ihnen, zusätzlich ein Nachweis Ihrer Unterhaltszahlungen.
> 
> **Getrennt lebende oder geschiedene Eltern**
> - Bei gemeinsamer Sorge ohne Unterhaltsbeiträge gibt es den halben Abzug: Kanton CHF 4'650, Bund CHF 3'400. Der Versicherungsabzug halbiert sich ebenfalls (CHF 650 Kanton, CHF 350 Bund).
> - Dies steht in der Formularposition 372 für Kinder ausserhalb des Haushalts. Ob es auch beim volljährigen Kind in Erstausbildung gilt, ist dort nicht ausdrücklich gesagt.
> - Wer für das Kind Unterhaltsbeiträge abzieht (Ziff. 13.2), erhält keinen Kinderabzug.
> 
> **Nur Bund: Abzug vom Steuerbetrag, CHF 263 je Kind** (Art. 36 Abs. 2bis DBG, `bund-dbg-2025__art-36-t4`)
> - Der Abzug gilt für Ehepaare und Alleinstehende, die mit dem Kind im gleichen Haushalt leben und dessen Unterhalt zur Hauptsache bestreiten. Er hängt von der Steuerbetragsberechnung ab, nicht von der Einkommensberechnung.
> - Ein Kind in der Lehre wird im Wortlaut nicht ausdrücklich genannt.
> - Das Formular führt diesen Abzug nicht als Position. Das Wiki sagt nicht, wie er dort erfasst wird. Ob er bei Ihrem Fall anwendbar ist, sollte die Fachperson prüfen.
> 
> Die endgültige Beurteilung, insbesondere zum Hauptunterhalt, liegt bei der Fachperson.

## q34

**Frage:** ZH 2025: Lohnausweis Feld G angekreuzt (Kantine). Welche Verpflegungspauschale gilt und in welche Ziffer des Berufsauslagenformulars?

**Soll (Referenz):** Verbilligte Verpflegung: CHF 7.50 pro Arbeitstag, max. CHF 1'600 pro Jahr (LS 631.33, zh-pauschalierung-berufsauslagen-2025__c0004); Form. 360 Ziff. 2.1 (verbilligt); Bund gleich.

**Antwort des Agenten** (27.2 s · Tools: 3 Aufrufe steuerwiki__beleg, steuerwiki__wert, steuerwiki__position):

> **ZH 2025, Lohnausweis Feld G angekreuzt (Kantine / Lunch-Checks)**
> 
> **Pauschale:** Es gilt der reduzierte Verpflegungsabzug von **CHF 7.50 pro Arbeitstag, maximal CHF 1'600 pro Jahr**. Die vollen CHF 15 pro Tag (maximal CHF 3'200) gelten nicht.
> 
> **Ziffer:** Berufsauslagenformular **Form. 360, Ziff. 2.1** («verbilligt»). Die Zeile hat **Code 206** für Person 1 und **Code 226** für Person 2.
> 
> **Rechnen:** Code 206 = min(Arbeitstage × 7.50; 1'600). Ein Beispiel mit 220 Arbeitstagen ergäbe 1'650 und damit 1'600. Der Code 208 (min(Tage × 15; 3'200)) bleibt leer.
> 
> **Kanton und Bund**
> - **Kanton und Bund:** Die Beträge sind gleich: 7.50 pro Tag, maximal 1'600 pro Jahr. Der Code 206 steht in beiden Spalten, Staatssteuer und Bundessteuer. Die 7.50 sind bereits der halbe Abzug. Sie dürfen nicht nochmals halbiert werden.
> - **Quellen Kanton:** zh-pauschalierung-berufsauslagen-2025__c0004 und zh-form-360-2025__c0003.
> - **Quellen Bund:** bund-bkv-2025__anhang-1 und bund-wl-2a-2025__c0045.
> - **Status:** ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Zu beachten**
> - **Feld G:** Es wird auch bei Lunch-Checks oder einem verbilligten Personalrestaurant angekreuzt, unabhängig von der tatsächlichen Nutzung.
> - **Barbeitrag:** Im Kanton gilt ein Barbeitrag als Verbilligung. Beim Bund gibt es den halben Abzug nur bei Gutscheinen oder Kantine/Personalrestaurant.
> - **Keine Mehrkosten beim Bund:** Kosten die Hauptmahlzeiten höchstens CHF 10, entfällt der Abzug beim Bund mangels Mehrkosten.
> - **Ziff. 15 im Lohnausweis:** Steht dort «Mittagessen durch Arbeitgeber bezahlt», muss der Abzug zusätzlich geprüft werden.
> - **Schichtarbeit (Ziff. 2.2, Code 210):** Dieser Abzug ist mit dem Verpflegungsabzug nicht kumulierbar.
> - **Nicht geprüft:** Die Bundes-Ausnahmen nach BKV Art. 6 Abs. 2/3 habe ich nicht im Detail angeschaut.
> - **Quelle Lohnausweis-Regeln:** Die Wegleitung zum Lohnausweis liegt im Wiki nur in der Fassung 2026 vor. Die Regeln zu Feld G sind qualitativ und enthalten keine Beträge.
> - **Fachliche Beurteilung:** Sie bleibt bei der zuständigen Fachperson.

## q35

**Frage:** SG 2025: Kapitalbezug Säule 3a CHF 100'000. Wird das mit dem übrigen Einkommen besteuert? Wo deklarieren?

**Soll (Referenz):** Nein – Kapitalleistungen aus Vorsorge werden getrennt vom übrigen Einkommen (separate Jahressteuer) besteuert; SG Formular 1 Ziff. 40.1 (Säule 3a), Total Ziff. 41.

**Antwort des Agenten** (28.8 s · Tools: 4 Aufrufe steuerwiki__beleg, steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Nein, der Bezug wird nicht mit dem übrigen Einkommen zusammengerechnet.** Er wird in SG 2025 separat besteuert.
> 
> **Besteuerung (SG 2025, Steuerstatus ☑️ agent-geprüft)**
> - **Kanton:** Kapitalleistungen werden gesondert vom übrigen Einkommen besteuert (sg-wl-2025__c0119). Es gilt eine volle Jahressteuer, und der Steueranspruch entsteht im Zeitpunkt des Zuflusses.
> - **Einfache Steuer (Art. 52 StG SG, sg-stg-2025__art-52):**
>   - 2,0 % für gemeinsam steuerpflichtige Ehegatten. Das gilt auch für Alleinstehende, die mit Kindern oder Unterstützungsbedürftigen im gleichen Haushalt leben.
>   - 2,2 % für die übrigen Steuerpflichtigen.
> - **Beispiel bei CHF 100'000:** Die einfache Steuer beträgt CHF 2'200 (2,2 %) bzw. CHF 2'000 (2,0 %). Dazu kommt der Steuerfuss von Kanton und Gemeinde. Die Gesamtbelastung habe ich nicht berechnet, weil der Steuerfuss fehlt.
> - **Abzüge:** Allgemeine Abzüge und Sozialabzüge werden auf den Kapitalbezug nicht gewährt.
> - **Bund (direkte Bundessteuer):** Der Bezug wird separat zu einem Fünftel der Tarife nach Art. 36 DBG besteuert, ohne Sozialabzüge (bund-dbg-2025__art-38). Den Bundesbetrag habe ich nicht berechnet, den Tarif nicht geöffnet.
> 
> **Wo deklarieren (Formular 1, SG 2025)**
> - **Ziff. 40.1** «Kapitalleistungen aus gebundener Vorsorge Säule 3a». Eintragen: Kapitalauszahlung 2025, brutto, ohne Rappen. Bei mehreren Auszahlungen ist es der Gesamtbetrag.
> - **Nicht in die Einkünfte**, namentlich nicht in Ziff. 6.4. Die Ziff. 40 ist ein separater Block («Weitere Angaben»), und die Deklaration dient nur der Information. Die Steuer wird trotzdem separat erhoben.
> - **Beilage:** Die Bescheinigung der 3a-Stiftung (Bank oder Versicherung) mit Auszahlungsdatum und Bruttobetrag ist einzureichen (sg-form-1-2025__c0014).
> - **Bund:** Das Formular hat dafür keine eigene Spalte. Die Behörde nimmt die Anpassung für die Bundessteuer automatisch vor (sg-wl-2025__c0173).
> 
> **Zu beachten**
> - Massgebend ist das Auszahlungsjahr. Der Bezug gehört in die Steuererklärung 2025, wenn er 2025 zugeflossen ist.
> - Bezüge aus mehreren Vorsorgequellen im selben Jahr (3a, 2. Säule, Freizügigkeit) werden nach meiner Lesart nicht quellenweise getrennt besteuert. Sie werden für die separate Jahressteuer zusammengerechnet. Das habe ich aber nicht gesondert geprüft; Ziff. 40.1 bis 40.3 sind jedenfalls getrennte Zeilen.
> - Die fachliche Beurteilung bleibt bei der Fachperson.

## q36

**Frage:** ZH 2025: Geschiedener Mandant zahlt Unterhaltsbeiträge an die Ex-Frau (CHF 24'000) und für das minderjährige Kind (CHF 12'000). Was ist abziehbar, in welcher Ziffer?

**Soll (Referenz):** Ex-Ehefrau CHF 24'000 voll abziehbar, Ziff. 13.1 (Code 254); Kinderalimente CHF 12'000 abziehbar bis und mit Monat der Volljährigkeit, Ziff. 13.2 (Code 255); Empfänger versteuert; Bund gleich (Art. 33 Abs. 1 lit. c DBG).

**Antwort des Agenten** (27.6 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **ZH 2025: Unterhaltsbeiträge des geschiedenen Mandanten**
> 
> Beide Beträge sind voll abziehbar, insgesamt CHF 36'000. Sie gehören aber in zwei verschiedene Ziffern des Hauptformulars (StA Form. 300):
> 
> | Empfänger | Betrag | Ziffer / Code | Abzug |
> |---|---|---|---|
> | Ex-Frau (für sie persönlich) | CHF 24'000 | **13.1, Code 254** | voll |
> | Minderjähriges Kind | CHF 12'000 | **13.2, Code 255** | voll, bis und mit Monat des 18. Geburtstags |
> | **Total** | **CHF 36'000** | | |
> 
> Kanton und Bund sind gleich. In beiden Spalten (Staats- und Bundessteuer) wird derselbe Betrag eingetragen.
> 
> **Zu Ziff. 13.1 (Ex-Frau)**
> - Abziehbar sind nur periodische Beiträge, die für den Ehegatten persönlich bestimmt sind. Eine Kapitalabfindung gilt als Schuldentilgung und ist nicht abziehbar.
> - Naturalleistungen wie Miete, Krankenkassenprämien oder Schuldzinsen sind gleichgestellt.
> - Die Ex-Frau muss die CHF 24'000 in ihrer Erklärung bei Ziff. 5.1 (Code 160) als Einkommen versteuern.
> - Quelle: zh-form-300-2025__c0007, zh-wl-2025__c0075.
> 
> **Zu Ziff. 13.2 (Kind)**
> - Abziehbar sind die bezahlten Beiträge bis und mit dem Monat, in dem das Kind 18 wird. Spätere Zahlungen sind nicht mehr abziehbar. Dann kommt stattdessen allenfalls der Kinderabzug (Ziff. 24.1) in Frage.
> - Wer Alimente für das minderjährige Kind abzieht, erhält für dieses Kind keinen Kinderabzug. Beides zusammen geht nicht.
> - Beim Bund zählen nur familienrechtlich geschuldete und effektiv bezahlte Alimente, freiwillige Zahlungen nicht.
> - Der empfangende Elternteil versteuert die Kinderalimente bei Ziff. 5.2 (Code 161).
> - Quelle: zh-form-300-2025__c0007, zh-wl-2025__c0076.
> 
> **Offene Punkte**
> - Bitte prüfen, ob das Kind 2025 volljährig wird. Wenn ja, ist nur der Teil bis zum Geburtstagsmonat bei Ziff. 13.2 abziehbar.
> - Bezahlt sein müssen die Beträge effektiv im Jahr 2025. Die Bank- bzw. Zahlungsbelege sind dafür nötig.
> - Ob die Zahlungsnachweise mit der Erklärung eingereicht werden müssen, ist im Wiki strittig (Entscheidungsvorlage Nr. 11, zh-wl-2025__c0207). Bis die Fachperson entschieden hat, empfehle ich, Scheidungsurteil bzw. Unterhaltsvereinbarung und Zahlungsnachweise beizulegen.
> - Alle Fundstellen haben den Status ☑️ agent-geprüft, die Abnahme ist noch offen. Die fachliche Beurteilung bleibt bei der Fachperson.

## q37

**Frage:** TG 2025: Mandant bringt Steuerberatungsrechnung, Kreditkartenabrechnung, Mietvertrag und Motorfahrzeugversicherung. Was davon ist relevant?

**Soll (Referenz):** Steuerberatungsrechnung: nein; Motorfahrzeugversicherung: nein; Kreditkartenabrechnung: bedingt (nur als Nachweis/Schuld per 31.12.); Mietvertrag: bedingt (Wochenaufenthalt/Arbeitszimmer/Adressnachweis) – laut belege-relevanz.

**Antwort des Agenten** (37.7 s · Tools: 10 Aufrufe read, steuerwiki__ablage, steuerwiki__beleg):

> Nach dem Wiki ist keines der vier Dokumente sicher ein Beleg für die TG-Erklärung 2025. Zwei sind nicht steuerrelevant, zwei nur unter einer Bedingung, die ich mangels Dokumentinhalt nicht prüfen kann.
> 
> | Dokument | Belegtyp | steuerrelevant | Steuerjahr | einreichen (TG 2025) | Kategorie (KATEGORIEN.md) |
> |---|---|---|---|---|---|
> | Steuerberatungsrechnung | `steuerberatungskosten` | **nein** (☑️, `bund-wl-2a-2025__c0057`) | 2025 | nein | keine Steuerbeleg-Kategorie |
> | Kreditkartenabrechnung | `kreditkartenabrechnung` | **bedingt** (☑️, `bund-dbg-2025__art-34`) | 2025 | unklar | falls relevant: **Belege Sonstiges** |
> | Mietvertrag | `mietvertrag-wohnung` | **bedingt** (☑️, `tg-wl-2025__c0189`) | 2025 | unklar | falls relevant: **Belege Sonstiges** |
> | Motorfahrzeugversicherung | `motorfahrzeug-versicherung` | **nein** (☑️, `tg-wl-2025__c0123`) | 2025 | nein | keine Steuerbeleg-Kategorie |
> 
> Der Status ☑️ heisst: Fundstelle geprüft, Abnahme offen.
> 
> **Nicht relevant**
> - **Steuerberatungsrechnung:** Die Kosten für Steuerberatung und das Ausfüllen der Steuererklärung sind im Privatvermögen nicht abziehbar. Der Bund schliesst sie ausdrücklich aus. Eine TG-Fundstelle dazu gibt es im Wiki nicht (Suche «Steuerberatung» ohne Treffer). Nur wenn das Honorar teilweise geschäftlich veranlasst ist (Selbständigerwerbende), gehört dieser Teil in die Jahresrechnung. Bei einer Einsprache ist die Abzugsfähigkeit im Wiki nicht verifiziert, im Zweifel nicht abziehen.
> - **Motorfahrzeugversicherung:** Prämien und Verkehrssteuern des Privatfahrzeugs sind Lebenshaltungskosten, kein Abzug. Das Fahrzeug selbst gehört aber ins Vermögen: Verkehrswert per 31.12.2025 deklarieren, ein geleastes Fahrzeug nicht. Dafür braucht es Fahrzeugtyp, Kaufpreis und Anschaffungsjahr aus dem Fahrzeugausweis oder Kaufvertrag, nicht aus der Police.
> 
> **Nur bedingt relevant**
> - **Kreditkartenabrechnung:** Die Abrechnung selbst ist kein Beleg. Sie zählt nur in diesen Fällen:
>   - Es besteht ein Saldovortrag mit Sollzinsen. Dann kommen Saldo per 31.12.2025 und Zinsen in Form. 4.1 A (Privatschulden, Codes 455 und 286). Private Schuldzinsen sind abziehbar bis Vermögensertrag plus Fr. 50'000, für Kanton und Bund.
>   - Sie dient als Ersatznachweis für eine abziehbare Zahlung, zum Beispiel Spende, Arzt, Weiterbildung oder Berufsauslagen, wenn die Originalrechnung fehlt. Die Originalrechnung ist vorzuziehen.
>   - Kartengebühren und Alltagsumsätze sind nicht abziehbar.
> - **Mietvertrag:** Der Mietzins der selbstbewohnten Wohnung ist Lebenshaltungsaufwand und nicht abziehbar. Relevant wird er nur in diesen Fällen:
>   - Untervermietung: Der Nettoertrag ist steuerbar (Ziff. 5.4).
>   - Wochenaufenthalt am Arbeitsort: Die Unterkunftskosten berechnen sich nach der Formel Jahresmietzins : (Zimmer + 1) bei Wohnungen bis 3½ Zimmer.
>   - Mietzinsreduktion als Entgelt, zum Beispiel für eine Hauswart-Tätigkeit: Die Differenz ist Einkommen.
>   - Für TG 2025 ist keine Formularposition mit diesem Beleg erfasst.
> 
> **Kurzfazit**
> - Nicht relevant: Steuerberatungsrechnung und Motorfahrzeugversicherung. Beide sind keine Steuerbelege und kommen in keine Steuerbeleg-Kategorie.
> - Bedingt relevant: Kreditkartenabrechnung und Mietvertrag. Sie sind nur dann Belege, wenn eine der oben genannten Bedingungen zutrifft, und kommen dann in «Belege Sonstiges».
> 
> **Unsicherheiten**
> - Die Einreichepflicht ist für Kreditkartenabrechnung und Mietvertrag in den TG-Quellen 2025 nicht geregelt. Ich habe sie deshalb wie «nicht einzureichen» behandelt (Belege Sonstiges). Das ist eine Annahme, keine belegte Aussage.
> - Keine der beiden Listenzeilen ist bestätigt. KATEGORIEN.md nennt diese Dokumentarten nicht ausdrücklich, die Kategorie folgt deshalb aus der Einreichepflicht.
> - Welche Bedingung zutrifft, hängt vom Inhalt ab. Beim Mandanten wäre zu klären, ob ein Kreditkarten-Saldovortrag besteht oder Belege fehlen, und ob untervermietet wird, ein Wochenaufenthalt vorliegt oder eine Mietzinsreduktion gewährt wird. Die fachliche Beurteilung bleibt bei der Fachperson.

## q38

**Frage:** AR 2026: Wie hoch ist der Kinderabzug für ein 10-jähriges Kind? Ist der Wert gesichert?

**Soll (Referenz):** AR 2026: CHF 7'400 laut Anhang 1 StG (indexiert), aber Status STRITTIG (MB 02 / StG-Text nennen andere Beträge; Wegleitung 2026 fehlt) → Fachperson.

**Antwort des Agenten** (25.1 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__zeige):

> **Kinderabzug AR 2026, Kind 10 Jahre (Kategorie «nach 4. bis 15. Altersjahr»): CHF 7'400. Der Wert ist nicht gesichert.**
> 
> **Status: ⚠️ strittig.** Die Quellen widersprechen sich:
> 
> | Quelle | Betrag |
> |---|---|
> | Anhang 1 StG (indexierter Betrag per 1.1.2024, Art. 38 Abs. 1 lit. a Ziff. 2; `ar-stg-anhang-kp__c0001`) | **CHF 7'400** |
> | WL AR 2025, Kurzübersicht Ziff. 23 (bestätigt die Anhang-Werte für 2025; `ar-wl-2025__c0005`) | CHF 7'400 |
> | MB AR 02, Ziff. 2 (Stand 18.08.2026, gilt für 2025–2027; `ar-mb-02__c0002`) | CHF 7'000 (entspricht dem nicht indexierten Gesetzestext) |
> 
> **Einschätzung:** Nach Art. 39a StG ist Anhang 1 massgeblich. Die Indexierung spricht deshalb für 7'400. Das Merkblatt nennt aber die nicht indexierten 7'000. Ich habe keine Wegleitung oder Formular AR 2026 gefunden, die den Widerspruch auflösen würde. Das Gerüst im Wiki stammt aus 2025 und ist für 2026 noch nicht publiziert (Stand 09.11.2026). Ich nehme 7'400 als Arbeitswert, bis die Fachperson oder das Steueramt AR den Betrag bestätigt.
> 
> **Weitere Abzüge für dasselbe Kind (nicht strittig):**
> - Versicherungsabzug: Zuschlag von CHF 1'000 pro Kind (☑️ agent-geprüft, `ar-stg__art-35-t2`).
> - Vermögensfreibetrag: CHF 25'000 pro minderjähriges Kind (☑️ agent-geprüft, `ar-stg__art-51`).
> 
> **Bund (direkte Bundessteuer 2026):**
> - Es gibt einen einheitlichen Kinderabzug von CHF 6'800, ohne Staffelung nach Alter (☑️, `bund-dbg-2026__art-35`).
> - Dazu kommt ein Versicherungszuschlag von CHF 700 pro Kind (☑️).
> - Die Steuerermässigung beträgt CHF 263 pro Kind (☑️, `bund-dbg-2026__art-36-t4`).
> 
> Im Formular gehört der Abzug auf Ziff. 23.2. Die fachliche Beurteilung bleibt bei der Fachperson.

## q39

**Frage:** Welche Vermögenssteuer-Freibeträge (Sozialabzüge) gelten 2025 in ZH für Alleinstehende und Verheiratete?

**Soll (Referenz):** ZH kennt keine Vermögens-Sozialabzüge, sondern Tarifstufen mit 0 ‰: Grundtarif erste CHF 80'000, Verheiratetentarif erste CHF 159'000 (zh-stg-2025__par-47); kein Betrag pro Kind.

**Antwort des Agenten** (20.6 s · Tools: 1 Aufrufe steuerwiki__wert):

> **ZH, Steuerjahr 2025 – Vermögenssteuer (Staats-/Gemeindesteuer)**
> 
> Zürich kennt keinen separaten Sozialabzug beim Vermögen. Der Freibetrag steckt als 0‰-Stufe im Vermögenssteuertarif (§ 47 StG ZH):
> 
> | Zivilstand | Steuerfreies Vermögen (0‰-Stufe) | Fundstelle | Status |
> |---|---|---|---|
> | Alleinstehende | CHF 80'000 | zh-stg-2025__par-47-t1 | ☑️ agent-geprüft |
> | Verheiratete (Grundtarif für Ehepaare; gilt auch für Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern) | CHF 159'000 | zh-stg-2025__par-47-t2 | ☑️ agent-geprüft |
> 
> - **Kinder:** Es gibt keinen Vermögensabzug pro Kind (nur Tarifstufen, keine Kinderabzüge beim Vermögen).
> - **Im Formular:** Der Freibetrag ist kein Abzug. In Ziff. 35 «Steuerbares Vermögen gesamt» (= Ziff. 33 − Ziff. 34) wird das volle Vermögen eingetragen. Der Freibetrag wirkt erst bei der Steuerberechnung.
> - **Bund:** Die direkte Bundessteuer kennt keine Vermögenssteuer, daher gibt es dort keinen Freibetrag.
> 
> Status ☑️ heisst: Die Fundstelle ist geprüft, die Abnahme ist noch offen. Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q40

**Frage:** Alleinstehende TG 2026, Nettolohn 90'000, ÖV-Abo 2'400, Säule 3a 7'258, Krankenkasse 5'500. Erstelle die Abzüge (Berufskosten, 3a, Versicherungsabzug) Kanton und Bund mit Fundstellen und Status.

**Soll (Referenz):** TG 2026 (Kanton/Bund): Fahrkosten 2'400 (Max. 6'000 / 3'300); übrige Berufskosten 3 % von 90'000 = 2'700 (Min. 2'000, Max. 4'000, beide Ebenen); Säule 3a 7'258 (TG 🟡 extrahiert, Bund ☑️); Versicherungsabzug TG max. 3'500 → 3'500, Bund max. 1'800 → 1'800 (Prämien 5'500 übersteigen beide Maxima).

**Antwort des Agenten** (41.8 s · Tools: 11 Aufrufe read, steuerwiki__formular, steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Mandant:** alleinstehend, Nettolohn 90'000 · **Kanton:** TG · **Steuerjahr:** 2026 · **Formular:** Steuererklärung 2026 TG (Formular 1 + Hilfsblatt 4.2). Die linke Spalte gilt für die Staats- und Gemeindesteuern, die rechte für die direkte Bundessteuer (tg-wl-2026__c0195).
> 
> | Ziffer / Code | Position | Kanton | Bund | Regel / Limite | Fundstelle | Status |
> |---|---|---|---|---|---|---|
> | Form. 4.2 Ziff. 2.1 (Code 206) | ÖV-Abo | 2'400 | 2'400 | Effektive Kosten. Maximum Kanton 6'000, Bund 3'300 (Ziff. 2.5, Code 213). | tg-wl-2026__c0177, c0176; bund-dbg-2026__art-26 | ☑️ |
> | Form. 4.2 Ziff. 4 | Übrige Berufskosten (Pauschale) | 2'700 | 2'700 | 3 % × 90'000 = 2'700, innerhalb min 2'000 / max 4'000. | tg-bkv__par-4a; bund-bkv-2026__anhang-1; bund-rs-2-215__c0006 | ☑️ |
> | Form. 4.2 Ziff. 7 → Ziff. 10.1 (Code 240) | **Berufsauslagen total** | **5'100** | **5'100** | 2'400 + 2'700 | – | ☑️ |
> | Ziff. 13.1 (Code 314) | Säule 3a | 7'258 | 7'258 | Mit Anschluss an die 2. Säule gilt das Maximum 7'258. Die Einzahlung liegt genau darauf. Kanton und Bund sind gleich. | tg-wl-2026__c0089; bund-bsv-masszahlen-2025-2026__c0003 | ☑️ |
> | Ziff. 14 (Form. 5.2, Code 330) | Versicherungsabzug | 3'500 | 1'800 | Kanton min(5'500; 3'500), Bund min(5'500; 1'800). Das Maximum ist ausgeschöpft. | tg-stg__par-34-t3; bund-dbg-2026__art-33-t2; tg-wl-2026__c0209 | ☑️ |
> | | **Summe der drei Abzüge** | **15'858** | **14'158** | Kanton 5'100 + 7'258 + 3'500; Bund 5'100 + 7'258 + 1'800 | – | – |
> 
> Alle Beträge sind mit `rechne` berechnet. ☑️ bedeutet agent-geprüft: Die Fundstelle ist geprüft, die Abnahme ist offen.
> 
> **Annahmen und offene Punkte (für die Fachperson):**
> - **Verpflegung (Ziff. 3.1/3.2) fehlt.** Dazu habe ich keine Angaben. Wer an Arbeitstagen auswärts isst, hat zusätzlich Anspruch auf die Pauschale: Fr. 15 pro Arbeitstag, maximal 3'200 im Jahr, bei Verbilligung durch den Arbeitgeber Fr. 7.50 pro Tag. Bei Teilzeit wird sie nach Beschäftigungsgrad gekürzt. Die Verpflegung käme zu den 5'100 dazu, Kanton und Bund gleich. Rückfrage: Isst die Person an den Arbeitstagen auswärts (225 Tage bei 100 %)?
> - **Fahrkosten:** Die 2'400 gelten, wenn Feld F im Lohnausweis nicht angekreuzt ist. Ist es angekreuzt, entfällt der Fahrkostenabzug (tg-wl-2026__c0175). Die Berufsauslagen sänken dann auf 2'700. Das ÖV-Abo-Beleg ist als Beleg «unklar», ob einzureichen (tg-wl-2026__c0177). Aufbewahren und auf Verlangen vorlegen.
> - **Übrige Berufskosten:** Die Pauschale ist die Standardvariante. Höhere effektive Kosten wären mit Nachweis möglich, dann aber ohne Kumulation mit der Pauschale. Für Homeoffice/Arbeitszimmer ist im Kanton TG nichts verifizierbar (⬜ offen, StP 29 Nr. 8 nicht im Wiki).
> - **Säule 3a:** Ich gehe davon aus, dass eine Pensionskasse besteht. Dann das Kästchen «Anschluss 2. Säule (PK)» ankreuzen. Ohne PK-Anschluss wäre das Maximum 20 % des Erwerbseinkommens bis 36'288, die 7'258 blieben also voll abziehbar. Die 3a-Bescheinigung ist immer einzureichen (tg-wl-2026__c0034).
> - **Versicherungsabzug:** Die Prämie 5'500 setze ich als Nettoprämie nach Abzug der Prämienverbilligung (IPV) an. Liegt die Jahresbestätigung höher oder tiefer, ist das zu prüfen. Ergibt sich dadurch ein Betrag unter den Maxima, ändert sich der Abzug. Sparzinsen und weitere Policen kämen in Form. 5.2 dazu, ändern aber nichts, solange das Maximum erreicht ist. Die erhöhte Bundeslimite «ohne Vorsorgebeiträge» (2'700) greift hier nicht, weil Säule 3a bezahlt wurde (Bund 1'800, Kanton ohne Erhöhung).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

