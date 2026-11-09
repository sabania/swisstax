# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 40 · Lauf: 2026-11-09 19:52
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q01

**Frage:** Mandantin (ZH, 2025) bringt: Lohnausweis, Krankenkassen-Prämienrechnung, Handyrechnung, 3a-Bescheinigung, Hausratversicherungspolice, Spendenquittung Rotes Kreuz CHF 80, Kita-Rechnungen. Welche sind relevant, wofür?

**Soll (Referenz):** Relevant: Lohnausweis (Einkünfte 1.1), Krankenkassenprämien (Versicherungsabzug Ziff. 15, Form. 365), 3a-Bescheinigung (Ziff. 14), Kita-Rechnungen (Ziff. 16.6 Drittbetreuung, max. 25'000 Kanton / 25'800 Bund). Spende CHF 80: unter Mindestbetrag 100 → nicht abziehbar (sofern Total < 100). Nicht relevant: Handyrechnung (Lebenshaltung), Hausratversicherung (kein Versicherungsabzug).

**Antwort des Agenten** (40.9 s · Tools: 15 Aufrufe read, steuerwiki__ablage, steuerwiki__beleg, steuerwiki__suche, steuerwiki__zeige):

> **ZH · Steuerjahr 2025** (Wiki-Status der Karten: ☑️ agent-geprüft, Abnahme offen)
> 
> | Dokument | Relevant? | Wofür (ZH-Formular) | Einreichen? | Ablage-Kategorie |
> |---|---|---|---|---|
> | **Lohnausweis** | **Ja** | Ziff. 1.1/1.2 (Einkommen), Berufsauslagen-Angaben, Form. 360 | **Ja**, immer (zh-wl-2025__c0032) | **Belege eingereicht** (in der Liste ausdrücklich genannt) |
> | **3a-Bescheinigung** | **Ja** | Ziff. 14.1/14.2, Code 260/262. Abzug = min(einbezahlt; 7'258) mit 2. Säule. Ohne 2. Säule gilt min(einbezahlt; 20 % × Erwerbseinkommen; 36'288). Kanton und Bund gleich. | **Ja** (zh-wl-2025__c0081) | **Belege eingereicht** (in der Liste ausdrücklich genannt) |
> | **Krankenkassen-Prämienrechnung** | **Ja** | Ziff. 15 mit Form. 365 Teil A (Code 601). Prämien nach Abzug der Prämienverbilligung (IPV) eintragen und nicht doppelt kürzen. Der Abzug ist gedeckelt (Form. 365 Teil B). Beispiel-Limiten: Alleinstehend Kanton 2'900 / Bund 1'800, Verheiratet Kanton 5'800 / Bund 3'700 (jeweils mit Zuschlag je Kind). | Nur auf Verlangen, das Formular 365 liegt bei (zh-wl-2025__c0207) | **Belege Sonstiges** (Versicherungsprämien) |
> | **Kita-Rechnungen** | **Ja, bedingt** | Ziff. 16.6 (Code 376). Abzug je Kind unter 14 Jahren: min(Betreuungskosten; Kanton 25'000 / Bund 25'800). Verpflegung ist nicht abziehbar. Voraussetzung ist, dass die Betreuung wegen Erwerbstätigkeit oder Ausbildung nötig ist. Erhaltene Subventionen sind abzuziehen. | Aufstellung mit Empfängern beilegen, Rechnungen nur auf Verlangen (zh-zstb-34-1-bis-2025__c0023) | **Belege Sonstiges** (Kinderbetreuungskosten) |
> | **Spendenquittung Rotes Kreuz CHF 80** | **Nein, voraussichtlich nicht** | Ziff. 22.2. Abziehbar sind Spenden erst ab **CHF 100 pro Jahr** insgesamt (zh-info-spenden__c0003). | Nur auf Verlangen | **Belege Sonstiges**, nur falls Zuwendungen in der Summe CHF 100 erreichen. |
> | **Handyrechnung** | **Nein** | Privater Aufwand ist nicht abziehbar (Art. 34 lit. a DBG). Die Pauschale 3 % für übrige Berufskosten (mind. 2'000, max. 4'000) deckt berufliche Nutzung ab (zh-wl-2025__c0067). | – | Keine Steuerbeleg-Kategorie |
> | **Hausratversicherungspolice** | **Nein** | Prämien für Hausrat/Mobiliar sind nicht abziehbar und zählen nicht zum Versicherungsabzug in Ziff. 15. | – | Keine Steuerbeleg-Kategorie |
> 
> **Vorbehalte**
> - **Spenden:** Bei CHF 80 ist die Schwelle nur erreicht, wenn weitere Spenden dazukommen. Dann ist die Summe aller gemeinnützigen Zuwendungen massgebend, mit Grenze 20 % des Nettoeinkommens. Die Mandantin sollte nach weiteren Quittungen gefragt werden.
> - **Hausrat:** Die Fundstelle für den Ausschluss stammt aus AR/SG (ar-wl-2025__c0085). Für ZH ist das nicht einzeln belegt. Das Ergebnis passt zur ZH-Systematik von Form. 365, wo nur Kranken-, Unfall-, Lebens- und Rentenversicherung und Sparzinsen aufgeführt sind. Das ist aber ein Schluss und kein ausdrücklicher ZH-Satz.
> - **Handy:** Dazu hat das Wiki keine eigene Belegkarte, die Einordnung stützt sich auf die allgemeine Regel.
> - **Kategorien:** Alle Zuordnungen in `KATEGORIEN.md` sind noch von der Firma unbestätigt.
> 
> **Noch zu klären**
> - **Kita:** Beträge je Kind, Geburtsjahr, Erwerbspensum und Subventionen. Verpflegung muss getrennt ausgewiesen sein oder gekürzt werden.
> - **Krankenkasse:** Prämienverbilligung erhalten? Wenn ja, wurde sie bereits verrechnet?
> - **3a:** Hat die Mandantin eine Pensionskasse? Das entscheidet über die Limite 7'258 oder 20 %.

## q02

**Frage:** In welche Ziffer und mit welchem Code der ZH-Steuererklärung 2025 gehört der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb)?

**Soll (Referenz):** Ziff. 1.1 Haupterwerb, Code 100 (Person 1) / 101 (Person 2); Nettolohn Lohnausweis Ziff. 11 (zh-form-300-2025).

**Antwort des Agenten** (22.9 s · Tools: 2 Aufrufe steuerwiki__beleg, steuerwiki__position):

> **ZH · Steuerjahr 2025**
> 
> Der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb) gehört in **Ziff. 1.1** des Hauptformulars (Form. 300), «Haupterwerb unselbständig», mit **Code 100**. Code 101 gilt für Person 2.
> 
> - **Betrag:** Du setzt Ziff. 11 des Lohnausweises ein. Das ist der Bruttolohn (Ziff. 8) minus Ziff. 9 (AHV/IV/EO/ALV/NBUV) und minus Ziff. 10.1/10.2 (BVG). Bei mehreren Haupterwerben von Person 1 gilt die Summe aller Ziff. 11.
> - **Bund:** Es ist dieselbe Zeile für Staats- und Bundessteuer, ohne abweichende Regel. Kanton und Bund haben denselben Betrag.
> - **Einreichen:** Der Lohnausweis muss der Steuererklärung beigelegt werden, für jeden Arbeitgeber (§ 134 Abs. 1 lit. a StG, zh-wl-2025__c0032).
> - **BVG-Einkauf:** Ein Einkauf in Ziff. 10.2 ist schon im Nettolohn abgezogen. Er darf nicht nochmals in Ziff. 16.1 (Code 280) abgezogen werden.
> - **Erwerbslücken:** Sie müssen in der Steuererklärung ausdrücklich bezeichnet werden.
> - **Übrige Berufskosten:** Dieselbe Ziff. 11 dient auch als Basis für die Pauschale von 3 % (mindestens CHF 2'000, höchstens CHF 4'000) in Form. 360 Ziff. 3, Code 212.
> 
> Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Quelle: zh-form-300-2025__c0004.

## q03

**Frage:** Lohnausweis Feld F ist angekreuzt (Geschäftsauto). Was bedeutet das für den Fahrkostenabzug (SG 2025)?

**Soll (Referenz):** Feld F angekreuzt → kein Fahrkostenabzug für den Arbeitsweg mit Geschäftsfahrzeug (Privatanteil im Lohn, Lohnausweis Ziff. 2.2).

**Antwort des Agenten** (29.3 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__beleg, steuerwiki__wert, steuerwiki__zeige):

> **SG · Steuerjahr 2025**
> 
> **Kurzantwort:** Feld F angekreuzt heisst: **kein Fahrkostenabzug** für den Arbeitsweg (Formular 4 Ziff. 1, Codes 400–406 bzw. 450–456). Beim Kanton und beim Bund sind es CHF 0. Das Feld sagt, dass dem Arbeitnehmer für die Fahrt Wohnort–Arbeitsort keine Kosten entstehen.
> 
> **Begründung**
> - Die WL SG 2025 sagt: Erwachsen dem Arbeitnehmer keine Kosten (Sammeltransport, vom Arbeitgeber getragenes GA aus geschäftlichen Gründen), muss Feld F angekreuzt sein. «Ein Abzug für die Fahrt zur Arbeit ist deshalb nicht möglich.» (sg-wl-2025__c0075, ☑️ agent-geprüft)
> - Bei einem Geschäftsfahrzeug mit Privatanteil von 0,9 % pro Monat (10,8 % pro Jahr) gilt dasselbe: kein Fahrkostenabzug. Das ergibt sich aus der Position Form. 4 Ziff. 1.3 (☑️).
> - Das Lohnausweis-Merkblatt in den Wiki-Quellen (bund-wl-lohnausweis-2026) gilt nur für 2026. Ich stütze mich deshalb auf die WL SG 2025. Wiki-Hinweis zum Lohnausweis: Feld F wird auch angekreuzt, wenn der Arbeitgeber ein Geschäftsfahrzeug zur Verfügung stellt, zusammen mit dem Privatanteil (Ziff. 2.2). Diese Formulierung ist im Tool-Auszug abgeschnitten und stammt nicht aus einem von mir geöffneten Chunk.
> 
> **Zu prüfen:**
> 1. **Privatanteil in Ziff. 2.2 des Lohnausweises:** Er sollte aufgeführt sein. Er ist steuerbares Einkommen und im Nettolohn (Ziff. 11) enthalten. Es ist kein separater Eintrag nötig.
> 2. **Ausnahme Bordbuch:** Rechnet man mit Bordbuch effektiv ab statt mit der Privatanteil-Pauschale, sind die effektiven Arbeitswegkosten bis zum Maximalabzug abziehbar. Das Wiki nennt diese Ausnahme (Form. 4 Ziff. 1.3, Limite Kanton CHF 8'000 | Bund CHF 3'300). Wie sich das mit dem Kreuz in Feld F verträgt, geht aus den geöffneten Quellen nicht klar hervor. Das müsste die Fachperson klären.
> 3. **Fahrkostenentschädigung in Ziff. 2.3:** Wäre sie im Bruttolohn enthalten, dürfte Feld F nicht angekreuzt sein (sg-stb-39-3__c0013). Der Abzug wäre dann bis CHF 8'000 (Kanton) bzw. CHF 3'300 (Bund) möglich.
> 4. **Teilweise Privatfahrten ohne Geschäftsauto:** Fährt die Person zusätzlich an einzelnen Tagen anders zur Arbeit, ist das im Wiki nicht geregelt (nicht geprüft). Es braucht dann Rückfrage oder Beurteilung durch die Fachperson.
> 
> **Limiten zur Einordnung (nur relevant bei Abzug):** Maximalabzug Kanton CHF 8'000 (sg-stg-2025__art-39), Bund CHF 3'300 (bund-dbg-2025__art-26); Auto Fr. 0.70/km (2025; die 0.75 gelten erst ab 2026).
> 
> Die abschliessende fachliche Beurteilung bleibt bei der Fachperson.

## q04

**Frage:** Wie hoch ist der maximale Fahrkostenabzug 2025 in TG (Staatssteuer) und beim Bund, und welcher km-Ansatz gilt für das Auto?

**Soll (Referenz):** TG 2025 Staat max. CHF 6'000 (tg-stg__par-29), Bund max. CHF 3'300 (bund-dbg-2025__art-26); Auto TG gestaffelt 0.60/0.50/0.40 je nach Jahres-km, Bund 0.70.

**Antwort des Agenten** (22.4 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **TG · Steuerjahr 2025**
> 
> **Maximaler Fahrkostenabzug (alle Fahrkosten zusammen, Form. 4.2 Ziff. 2.5)**
> - **Staats- und Gemeindesteuer TG:** max. **CHF 6'000** ☑️ (tg-stg__par-29)
> - **Direkte Bundessteuer:** max. **CHF 3'300** ☑️ (bund-dbg-2025__art-26)
> 
> Die Limite gilt für alle Fahrkosten zusammen, inklusive Wochenaufenthalt und Nebenerwerb. Im Formular steht links die Spalte für Staat/Gemeinde und rechts jene für den Bund.
> 
> **km-Ansatz für das Privatauto**
> 
> Das Privatauto ist nur in begründeten Ausnahmefällen abziehbar, zum Beispiel wenn der ÖV unzumutbar ist, etwa bei einer Zeitersparnis von über 1 Stunde pro Arbeitstag. Im Normalfall werden nur die Kosten des ÖV-Abonnements abgezogen.
> 
> - **Kanton TG:** gestaffelt, stufenweise gerechnet ☑️ (tg-bkv__par-1, tg-wl-2025__c0003)
>   - bis 3'000 km: CHF 0.60/km
>   - 3'001 bis 5'000 km: CHF 0.50/km
>   - über 5'000 km: CHF 0.40/km
>   - Parkgebühren sind in diesen Ansätzen enthalten.
>   - Beispiel: 8'000 km ergeben CHF 1'800 + 1'000 + 1'200 = CHF 4'000.
> - **Bund:** einheitlich **CHF 0.70/km** ☑️ (bund-bkv-2025__anhang-1)
> 
> Bei einem 100%-Pensum werden in der Regel höchstens 225 Arbeitstage angerechnet (nur Kanton, beim Bund gibt es diese Regel nicht).
> 
> Alle Werte sind «agent-geprüft» (☑️): Die Fundstelle ist geprüft, die Abnahme steht noch aus. Die fachliche Beurteilung des Einzelfalls bleibt bei der Fachperson.

## q05

**Frage:** Welcher km-Ansatz für Autos gilt 2026 bei der direkten Bundessteuer?

**Soll (Referenz):** CHF 0.75 pro km (bund-mm-2025-09-11-kalte-progression-2026__c0004; RS 2-215).

**Antwort des Agenten** (22.7 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Bund (direkte Bundessteuer) · Steuerjahr 2026**
> 
> Für das Privatauto gilt **CHF 0.75 pro Fahrkilometer** (☑️ agent-geprüft, Abnahme offen). Im Vorjahr waren es CHF 0.70.
> 
> - **Bedingung:** Der Ansatz gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist.
> - **Obergrenze:** Der Abzug für Fahrten zwischen Wohn- und Arbeitsstätte ist insgesamt auf **CHF 3'300** pro Jahr begrenzt (Art. 26 Abs. 1 lit. a DBG, Chunk `bund-dbg-2026__art-26`). Der Betrag ist gleich hoch wie 2025.
> - **Künftige Anpassung:** Der Ansatz wird neu an den TCS-Kilometerpreis gekoppelt. Er kann künftig nach oben oder unten angepasst werden.
> - **Quelle:** `bund-mm-2025-09-11-kalte-progression-2026__c0004`: «Der Abzug wird auf 75 Rappen pro Kilometer erhöht (bisher 70 Rappen).»
> 
> Zum Vergleich gelten 2026 beim Bund auch diese Ansätze (Quelle `bund-rs-2-215__c0004`):
> - Motorrad mit weissem Kontrollschild: CHF 0.40 pro km.
> - Fahrrad, Motorfahrrad und Motorrad mit gelbem Kontrollschild: Pauschale CHF 700 pro Jahr.
> 
> Die Anzahl Arbeitstage für die Fahrkostenberechnung ist beim Bund nicht geregelt. Die Kantone legen sie unterschiedlich fest (ZH 240, SG 220, TG 225). Für AR habe ich dazu keine Quelle für 2026. Ein kantonales Formular kann für den Bundesteil eigene Ansätze führen. Wenn Sie einen Kanton nennen, prüfe ich das gezielt.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q06

**Frage:** Maximaler Säule-3a-Abzug 2025 für eine Arbeitnehmerin mit Pensionskasse? Und für eine Selbständige ohne 2. Säule?

**Soll (Referenz):** Mit 2. Säule CHF 7'258; ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288 (bund-bsv-masszahlen-2025-2026__c0003).

**Antwort des Agenten** (23.7 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Säule 3a · Steuerjahr 2025** (Bundesrecht BVV 3; gilt für alle Kantone gleich. Du hast keinen Kanton genannt, deshalb nenne ich keine kantonalen Formularziffern.)
> 
> | Fall | Maximaler Abzug 2025 |
> |---|---|
> | Arbeitnehmerin mit Pensionskasse (2. Säule) | **CHF 7'258** |
> | Selbständige ohne 2. Säule | **bis 20 % des Erwerbseinkommens, höchstens CHF 36'288** |
> 
> - **Mit Pensionskasse:** CHF 7'258 entsprechen 8 % des oberen BVG-Grenzbetrags. Quelle: bund-bsv-masszahlen-2025-2026__c0003. Status ☑️ agent-geprüft.
> - **Ohne 2. Säule:** Der Abzug beträgt 20 % des Erwerbseinkommens und ist bei CHF 36'288 gedeckelt (40 % des oberen BVG-Grenzbetrags). Quellen: bund-bvv3__art-7 und bund-bsv-masszahlen-2025-2026__c0003. Status ☑️ agent-geprüft.
>   - Das Einkommen, ab dem das Maximum erreicht wird, ergibt sich rechnerisch: 36'288 ÷ 0.20 = CHF 181'440.
>   - Unter diesem Einkommen gilt nur der 20-%-Anteil.
>   - Der Satz bezieht sich auf das Erwerbseinkommen. Welches Einkommen bei Selbständigen genau massgebend ist (Reineinkommen nach AHV-Beiträgen), habe ich hier nicht geprüft. Bitte im konkreten Fall klären.
> 
> **Hinweis zu 3a-Einkäufen:** Im Steuerjahr 2025 ist noch kein Einkauf möglich. Er ist frühestens 2026 möglich, und zwar für Lücken ab 2025. Für 2025 bleiben also die Höchstbeträge oben. Quelle: bund-ks-18a__c0016 und BVV 3 Art. 7a/7b.
> 
> Die fachliche Beurteilung des Einzelfalls bleibt bei der Fachperson. Nenne mir den Wohnsitzkanton (AR, SG, TG oder ZH), dann prüfe ich zusätzlich die Position im kantonalen Formular.

## q07

**Frage:** Kinderabzug 2025 in AR für ein 10-jähriges Kind – und beim Bund?

**Soll (Referenz):** AR 2025: CHF 7'400 (4.–15. Altersjahr; Anhang 1 StG, ar-stg-anhang-kp__c0001); Bund CHF 6'800 (Art. 35 DBG) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (29.6 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **AR · Steuerjahr 2025: Kinderabzug für ein 10-jähriges Kind**
> 
> Das Alter zählt per Stichtag 31.12.2025. Ein 10-jähriges Kind liegt in der Stufe «nach Vollendung des 4. bis zur Vollendung des 15. Altersjahrs».
> 
> | | Kanton AR | Bund (dBSt) |
> |---|---|---|
> | Kinderabzug vom Einkommen | **CHF 7'400** (Formular Ziff. 23.2) | **CHF 6'800** |
> | Quelle | ar-stg-anhang-kp__c0001, ar-wl-2025__c0005 | bund-dbg-2025__art-35 |
> | Zusätzlich | Versicherungsabzug +CHF 1'000 pro Kind | Versicherungsabzug +CHF 700 pro Kind |
> | Quelle | ar-stg__art-35-t2 | bund-dbg-2025__art-33-t5 |
> | Abzug vom Steuerbetrag | keiner | **CHF 263** pro Kind |
> | Quelle | – | bund-dbg-2025__art-36-t4 |
> 
> Alle genannten Werte haben den Status ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme steht aus.
> 
> **Besonderheiten Kanton**
> - AR staffelt den Kinderabzug nach Alter: CHF 5'300 bis zum 4. Altersjahr, CHF 7'400 vom 4. bis zum 15. und CHF 11'600 danach.
> - Das Gesetz nennt CHF 7'000, das ist die nicht indexierte Fassung. Massgebend sind CHF 7'400 nach Anhang 1 und Wegleitung 2025.
> - Der Abzug entfällt, wenn die Einkünfte des Kindes CHF 18'000 übersteigen.
> - Er entfällt auch, wenn für das Kind Unterhaltsbeiträge nach Ziff. 12.2 abgezogen werden.
> - Getrennt besteuerte Eltern mit gemeinsamer Sorge und ohne Unterhaltsbeiträge teilen den Abzug je zur Hälfte.
> - Für Vermögen gilt zusätzlich ein Freibetrag von CHF 25'000 pro minderjähriges Kind (ar-stg__art-51).
> 
> **Besonderheiten Bund**
> - Der Bund kennt keine Altersstaffel. Der Abzug gilt einheitlich für das minderjährige Kind.
> - Die CHF 263 werden direkt vom berechneten Steuerbetrag abgezogen. Sie kommen zum Abzug von CHF 6'800 hinzu.
> - Im AR-Formular gibt es keine separate Bundesspalte. Die Steuerverwaltung setzt die Bundesbeträge automatisch ein (ar-wl-2025__c0179). Du trägst nur das Kind auf Seite 1 und in Ziff. 23.2 ein.
> 
> **Nicht geprüft:** die Aufteilung bei getrennten Eltern auf Bundesebene.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## q08

**Frage:** Versicherungsabzug ZH 2025 für ein Ehepaar mit 2 Kindern, beide mit Pensionskasse (Staatssteuer und Bund)?

**Soll (Referenz):** ZH Staat: 5'800 + 2 × 1'300 = 8'400; Bund: 3'700 + 2 × 700 = 5'100 (zh-stg-2025__par-31-t2, bund-dbg-2025__art-33).

**Antwort des Agenten** (26.0 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **ZH · Steuerjahr 2025: Versicherungsabzug, Ehepaar mit 2 Kindern, beide mit Pensionskasse**
> 
> Das Ehepaar lebt in ungetrennter Ehe und leistet Beiträge an die 2. Säule. Es gilt daher der Maximalabzug «mit Vorsorge».
> 
> | | Staatssteuer | Bundessteuer |
> |---|---|---|
> | Ehepaar (mit 2. Säule/3a) | CHF 5'800 | CHF 3'700 |
> | Zuschlag je Kind (2 × Kanton 1'300 / Bund 700) | CHF 2'600 | CHF 1'400 |
> | **Maximalabzug** | **CHF 8'400** | **CHF 5'100** |
> 
> Status der Werte: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Fundstellen**
> - Kanton: Ehepaar 5'800 und Kinderzuschlag 1'300 stehen in `zh-stg-2025__par-31-t2`.
> - Bund: Ehepaar 3'700 in `bund-dbg-2025__art-33-t2`, Kinderzuschlag 700 in `bund-dbg-2025__art-33-t5`.
> - Formular: Form. 365 Teil B (Codes 611, 613–615), Übertrag in Ziff. 15 (Code 270) des Hauptformulars `zh-form-300-2025__c0008`.
> 
> **Wie der Abzug im Formular entsteht**
> - Abgezogen werden nicht die Maximalbeträge, sondern der tiefere Wert aus A und B, je Spalte getrennt (Staat/Bund).
> - A (Code 606) sind die tatsächlich bezahlten Prämien für Kranken-, Unfall-, Lebens- und Rentenversicherung plus die Zinsen von Sparkapitalien. Davon ab geht die Prämienverbilligung (IPV), soweit sie nicht schon in den Prämien gekürzt ist.
> - B (Code 616) sind die Maximalbeträge aus der Tabelle.
> - Abzug = min(A; B). Der Bund hat tiefere Maxima, deshalb kann die Bundesspalte früher begrenzt sein als die Staatsspalte.
> 
> **Zu beachten**
> - Die Variante «ohne Vorsorge» (Kanton 8'700 / Bund 5'550 für Ehepaare) gilt nur, wenn weder die Steuerpflichtigen noch ihre Arbeitgeber Beiträge an die 2. Säule oder 3a geleistet haben. Das trifft hier nicht zu.
> - Prämien, die im Lohnausweis bereits abgezogen sind (NBUV), nicht nochmals erfassen.
> - Die Kinderzuschläge gelten für Kinder, für die ein Kinderabzug geltend gemacht werden kann. Bei geteiltem Kinderabzug halbiert sich der Zuschlag auf Kanton 650 / Bund 350 je Kind.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q09

**Frage:** Wie hoch ist der Kinderdrittbetreuungsabzug 2025 im Kanton ZH, und gilt 2026 ein anderer Wert?

**Soll (Referenz):** ZH 2025 CHF 25'000 (StG Nachtrag 127, zh-stg-2025__par-31-t4); 2026 CHF 25'300 (zh-stg-2026__par-31-t3). Die VKP ab 2024 (10'400) ist überholt.

**Antwort des Agenten** (23.5 s · Tools: 2 Aufrufe steuerwiki__wert):

> **ZH · Steuerjahr 2025 und 2026: Kinderdrittbetreuungsabzug**
> 
> Ja, 2026 gilt für die Staatssteuer ein anderer Wert als 2025. Der Bundeswert bleibt gleich.
> 
> | | 2025 | 2026 |
> |---|---|---|
> | **Kanton ZH (Staats-/Gemeindesteuer)** | max. **CHF 25'000** pro Kind | max. **CHF 25'300** pro Kind |
> | **Bund (direkte Bundessteuer)** | max. **CHF 25'800** pro Kind | max. **CHF 25'800** pro Kind |
> 
> **Voraussetzungen (2025 und 2026 gleich)**
> - Das Kind hat das 14. Altersjahr noch nicht vollendet.
> - Die Kosten sind nachgewiesen und stehen in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.
> - Das Kind lebt im gleichen Haushalt wie die für den Unterhalt sorgende Person.
> 
> **Besonderheit 2026:** Bei Konkubinat oder alternierender Obhut mit gemeinsamer Sorge gilt je der halbe Abzug, also CHF 12'650 pro Person. Diesen Hinweis nennt das Wiki nur für 2026. Für 2025 ist er in der Tool-Ausgabe nicht aufgeführt, also nicht geprüft.
> 
> **Formular:** Der Abzug gehört in Ziff. 16.6 «Abzug für fremdbetreute Kinder» (Code 376). Das gilt für beide Jahre. Das Formular deckt Kanton und Bund. Der Bund wird dort mit seiner eigenen Limite angewendet.
> 
> **Quellen und Status** (alle ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen)
> - ZH 2025: `zh-stg-2025__par-31-t4` (§ 31 StG, Fassung Nachtrag 127).
> - ZH 2026: `zh-stg-2026__par-31-t3` (§ 31 StG, Fassung Nachtrag 132).
> - Bund 2025: `bund-dbg-2025__art-33-t7`.
> - Bund 2026: `bund-dbg-2026__art-33-t7`.
> 
> **Stolperstein:** Die ältere Wegleitung (VKP ab 2024, `zh-vkp-2024-zstb__c0005`) nennt noch CHF 10'400. Dieser Wert ist überholt. Massgebend ist das Gesetz in der jeweiligen Jahresfassung.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## q10

**Frage:** Gibt es im Kanton TG einen Zweiverdienerabzug für die Staatssteuer?

**Soll (Referenz):** Nein, TG kennt keinen kantonalen Zweiverdienerabzug (nur Bund: 50 %, 8'600–14'100).

**Antwort des Agenten** (21.5 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **TG · Steuerjahr 2025** (in der Frage kein Jahr genannt, daher 2025)
> 
> **Nein.** Im Kanton Thurgau gibt es bei den Staats- und Gemeindesteuern keinen Zweiverdienerabzug. Die Wegleitung sagt: «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.» (tg-wl-2025__c0104, ☑️ agent-geprüft)
> 
> **Bund (direkte Bundessteuer):** Dort gibt es den Abzug. Er gilt für gemeinsam besteuerte Ehepaare und eingetragene Partner, wenn beide erwerbstätig sind.
> - Abzug: 50 % des niedrigeren Erwerbseinkommens.
> - Mindestens Fr. 8'600, höchstens Fr. 14'100.
> - Ist das niedrigere Erwerbseinkommen kleiner als Fr. 8'600, kann nur dieser Betrag abgezogen werden.
> - Quelle: bund-dbg-2025__art-33-t6, ☑️ agent-geprüft.
> 
> **Im Formular:** Ziff. 18, Zweiverdienerabzug (Code 356), nur in der rechten Spalte (Bund) ausfüllen. Die linke Spalte (Staats- und Gemeindesteuern) bleibt leer. Quelle: tg-form-01-2025__c0011.
> 
> **Berechnung für den Bund:**
> - Erwerbseinkommen je Person = Erwerbseinkünfte − Berufsauslagen − Beiträge Säule 2/3a.
> - Abzug = min(max(50 % × tieferes Erwerbseinkommen; 8'600); 14'100; tieferes Erwerbseinkommen).
> - Löhne, die im vereinfachten Abrechnungsverfahren versteuert werden, zählen nicht mit.
> 
> Die fachliche Beurteilung des Einzelfalls bleibt bei der Fachperson.

## q11

**Frage:** SG 2025: Pauschale für übrige Berufskosten? Wie wird sie berechnet?

**Soll (Referenz):** SG 2025: CHF 700 + 10 % des Nettolohns, max. CHF 2'400 (Art. 21 StV SG, WL SG 2025).

**Antwort des Agenten** (24.6 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **SG · Steuerjahr 2025: Pauschale übrige Berufskosten**
> 
> **Kanton (Staats- und Gemeindesteuer)**
> - Formel: **Fr. 700 + 10 % der Nettoeinkünfte (Nettolohn), höchstens Fr. 2'400**.
> - Rechnung: `min(700 + 10 % × Nettolohn; 2'400)`. Die 2'400-Grenze ist ab einem Nettolohn von Fr. 17'000 erreicht.
> - Ein Minimum gibt es im Kanton nicht.
> - Nettolohn = Bruttoeinkünfte abzüglich AHV/IV/EO/ALV/UV und BVG (ohne Einkäufe). Im Formular ist das der Nettolohn aus Ziff. 1.1 (Code 100/102).
> - Quellen: sg-stv__art-21, sg-wl-2025__c0080, sg-form-4-2025__c0003. Status ☑️ agent-geprüft, Abnahme offen.
> 
> **Bund (direkte Bundessteuer)**
> - Formel: **3 % des Nettolohns, mindestens Fr. 2'000, höchstens Fr. 4'000**. Es gibt keinen fixen Sockelbetrag.
> - Rechnung: `min(max(3 % × Nettolohn; 2'000); 4'000)`.
> - Quelle: bund-bkv-2025__anhang-1. Status ☑️ agent-geprüft.
> - Im SG-Formular gibt es nur eine Spalte. Die Bundesabweichung nimmt die Steuerbehörde automatisch vor (Merkblatt 32, sg-wl-2025__c0173).
> 
> **Wo im Formular**
> - Hilfsblatt Formular 4, Ziff. 3.1: Code 416 (Person 1) bzw. 466 (Person 2).
> - Das Total der Berufskosten aus Formular 4 kommt in Hauptformular Ziff. 10.1 (Code 438) bzw. 10.2 (Code 488).
> 
> **Zu beachten**
> - Die Pauschale gilt ohne Nachweis. Bei Teiljahr ist umzurechnen.
> - Sie gilt sinngemäss auch bei ALV-Taggeldern.
> - Sie kann nicht zusätzlich geltend gemacht werden, wenn der Arbeitgeber nicht ereignisbezogene Pauschalspesen ausbezahlt.
> - Statt der Pauschale können die tatsächlichen Kosten abgezogen werden (Form. 4 Ziff. 3.2, Code 418 bzw. 468). Das lohnt sich nur, wenn sie die Pauschale übersteigen. Dann müssen alle übrigen Kosten belegt werden, auch ein allfälliges Arbeitszimmer (Beiblatt zu Formular 4).
> - Das Arbeitszimmer ist mit der Pauschale abgegolten. Eine Kumulation ist nicht möglich.
> 
> **Beispiel (Kanton):** Bei Nettolohn Fr. 80'000 ergibt 700 + 8'000 = 8'700, begrenzt auf **Fr. 2'400**. Beim Bund ergibt 3 % = 2'400, also ebenfalls **Fr. 2'400** (innerhalb 2'000–4'000).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q12

**Frage:** Pauschalabzug Liegenschaftsunterhalt in AR für ein 8-jähriges Einfamilienhaus – und wie in ZH?

**Soll (Referenz):** AR: 10 % (Gebäude bis 10 Jahre) bzw. 20 % des Bruttoertrags, nur bis Bruttomietertrag 100'000 (Art. 25 StV AR, MB 03); ZH: einheitlich 20 % ohne Altersstaffel (ZStB 30.2).

**Antwort des Agenten** (33.9 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position):

> **AR und ZH · Steuerjahr 2025** (du hast kein Jahr genannt, deshalb 2025). Status bei allen Zahlen: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> ## Pauschalabzug für ein 8-jähriges EFH
> 
> | | Kanton | Bund (DBSt) |
> |---|---|---|
> | **AR** | **10 %** (Gebäude bis und mit 10 Jahre) | **10 %** |
> | **ZH** | **20 %** (keine Staffelung nach Gebäudealter) | **10 %** (Gebäude bis 10 Jahre) |
> 
> Basis ist in beiden Kantonen der Bruttoertrag, bei Selbstnutzung also der Eigenmietwert.
> 
> ### AR
> - Der Kanton staffelt nach Gebäudealter: 10 % bis 10 Jahre, 20 % darüber. Dein EFH liegt mit 8 Jahren im 10-%-Bereich.
> - Beim Bund gilt dasselbe (Art. 5 LKV, bund-lkv__art-5, mit Stichtag Gebäudealter zu Beginn der Steuerperiode). Das AR-Formular hat keine separate Bundesspalte. Die Steuerverwaltung nimmt die Bundesanpassungen automatisch vor.
> - Die Pauschale gilt nur, wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes höchstens CHF 100'000 beträgt und die Liegenschaft ganz oder vorwiegend Wohnzwecken dient. Sonst sind nur die tatsächlichen Kosten abziehbar.
> - Du kannst je Gebäude und Jahr zwischen Pauschale und effektiven Kosten wählen.
> - Die Pauschale deckt alle Unterhalts- und Verwaltungskosten ab.
> - Eintrag: Form. 7 Abschn. C (C1 = Pauschale) → Ziff. 15 der Steuererklärung.
> - Fundstellen: ar-mb-03__c0004, ar-wl-2025__c0175, ar-form-07-2025__c0003.
> 
> ### ZH
> - Der Kanton rechnet einheitlich 20 % vom Brutto-Mietertrag bzw. Mietwert (zh-zstb-30-2__c0002).
> - Der Bund staffelt: 10 % bei Gebäuden bis 10 Jahre. Das EFH fällt mit 8 Jahren in diesen Bereich. Im ZH-Formular entstehen dadurch zwei unterschiedliche Prozentsätze für Staat und Bund. Das Hilfsblatt Form. 350 nennt dazu «Kanton 20 % / Bund 10 %».
> - Die Wahl zwischen Pauschale und effektiven Kosten gilt je Liegenschaft und Steuerperiode. Bei der Pauschale sind keine weiteren Abzüge möglich, ausser Baurechtszinsen. Bei vorwiegend geschäftlich genutzten Liegenschaften gibt es keine Pauschale.
> - Eintrag: Form. 350, Seite 2, Codes 5731 ff. (Pauschale). Der Nettoertrag geht über Code 3953 in Ziff. 6 (Code 188) der Steuererklärung. Du ziehst den Unterhalt also direkt im Hilfsblatt ab und nicht nochmals separat.
> - Fundstellen: zh-form-350__c0007, zh-zstb-30-2__c0002.
> 
> ## Nicht geprüft / Vorbehalte
> - In AR habe ich nicht geprüft, ob die 10 % vom Eigenmietwert vor oder nach dem 20-%-Selbstnutzungsabzug (Ziff. 5) berechnet werden. Das kann ich bei Bedarf nachschlagen.
> - Zum genauen Stichtag des Gebäudealters in AR und ZH (Baujahr oder Bezugsfertigkeit) liegt mir nichts Belegtes vor. Beim Bund steht «zu Beginn der Steuerperiode». Bei einem Gebäude nahe der 10-Jahres-Grenze solltest du das prüfen.
> - Die Positionsausgabe für AR vermerkt, dass der Bund nicht aus AR-Quellen belegt ist. Die 10 % beim Bund stammen aus Art. 5 LKV.
> - Die fachliche Beurteilung bleibt bei der Fachperson.

## q13

**Frage:** TG: Welcher Einschlag gilt auf dem Eigenmietwert der selbstbewohnten Liegenschaft am Wohnsitz (Kanton vs. Bund)?

**Soll (Referenz):** TG: Abzug 40 % Kanton, 20 % Bund für dauernd selbstbewohntes Eigentum am Wohnsitz (tg-stg__par-23; WL TG 2025).

**Antwort des Agenten** (25.2 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **TG · Steuerjahr 2025** (in der Frage kein Jahr genannt, deshalb 2025)
> 
> Auf dem Eigenmietwert der am Wohnsitz dauernd selbstbewohnten Liegenschaft gilt ein Selbstnutzungsabzug. Er beträgt im Kanton 40 % und beim Bund 20 %.
> 
> | | Abzug auf dem Eigenmietwert | Steuerbar | Status |
> |---|---|---|---|
> | **Kanton** (Staats- und Gemeindesteuer) | **40 %** | 60 % des Mietwerts | ☑️ agent-geprüft |
> | **Bund** (direkte Bundessteuer) | **20 %** | 80 % des Mietwerts | ☑️ agent-geprüft |
> 
> - **Kanton:** § 23 StG TG (tg-stg__par-23): «von dem gemäss Abs. 2 festgelegten Mietwert ein Abzug von 40 Prozent».
> - **Bund:** Der Wert 20 % stammt aus der Wegleitung (tg-wl-2025__c0225): «… nutzung kantonal einen Abzug von 40% und beim Bund von 20% vornehmen». Das DBG kennt keinen eigenen festen Prozentsatz. Der Bundesabzug wird im kantonalen Verfahren festgesetzt, hier also bei der Veranlagung im Kanton TG.
> - **Im Formular:** Ziff. 8.1 «Einkünfte aus Liegenschaften» (Formular 7, Code 180), Kanton in der linken, Bund in der rechten Spalte. Auf Formular 7 geben Sie den indexierten Mietwert nach rechtskräftiger Schätzung an (tg-form-07-2025__c0002, tg-wl-2025__c0224). Der Nettoerfolg wird für Staat und Bund getrennt gerechnet, weil die Abzüge verschieden sind.
> 
> **Rechenbeispiel:** Bei einem indexierten Mietwert von 20'000 ergibt sich:
> - Kanton: 20'000 × (1 − 40 %) = 12'000
> - Bund: 20'000 × (1 − 20 %) = 16'000
> 
> Das Beispiel ist nur zur Illustration. Ihre tatsächlichen Werte stehen in der Liegenschaftensteuerrechnung und der Schätzung.
> 
> **Voraussetzung und Ausnahmen:**
> - Der Abzug gilt nur für Wohneigentum, das am Wohnsitz dauernd selbst bewohnt wird.
> - Bei Zweit- oder Ferienwohnungen, landwirtschaftlich geschätzten Liegenschaften und an Nahestehende überlassenen Objekten ist der Mietwert zu 100 % steuerbar.
> 
> **Unterhalt:** Die Unterhaltspauschale ist in Kanton und Bund gleich hoch, 10 % bei Gebäuden bis 10 Jahre und 20 % bei älteren. Sie wird vom steuerbaren Eigenmietwert gerechnet, also nach dem Selbstnutzungsabzug. Alternativ können Sie die effektiven Kosten abziehen (Formular 8). Die Wahl gilt je Objekt und Jahr.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson. Die Fundstellen sind agent-geprüft, die Abnahme steht noch aus.

## q14

**Frage:** Bis wann kann ein Treuhänder im Kanton TG für seine Mandanten Fristerstreckung erhalten?

**Soll (Referenz):** Gewerbsmässige Treuhänder für Mandanten bis 31.12. des Deklarationsjahres (StP 155 Nr. 2).

**Antwort des Agenten** (25.1 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **TG · Steuerjahr 2025** (kein Jahr genannt, daher 2025; die Regel gilt laut Quelle auch für 2026 und 2027)
> 
> **Gewerbsmässige Treuhänder und Steuerberater können für ihre Mandanten Fristerstreckung längstens bis zum 31. Dezember des Deklarationsjahres beantragen.**
> 
> - Das Deklarationsjahr ist das Jahr der Einreichung. Für das Steuerjahr 2025 ist das **2026**, die Frist reicht also bis zum **31.12.2026**.
> - Zum Vergleich: Private erhalten das erste Gesuch grundsätzlich bis 30. September des Deklarationsjahres, weitere Gesuche in begründeten Fällen bis 30. November.
> - Über den 30. November hinaus (Private) bzw. den 31. Dezember (Treuhänder) werden weitere Gesuche abgewiesen, ausser es werden ausserordentliche Gründe glaubhaft gemacht. Dazu braucht es in der Regel eine substanziierte Sachdarstellung. Starke berufliche Beanspruchung des Vertreters oder fehlende Unterlagen reichen nicht.
> - Das Gesuch geht an das Gemeindesteueramt. Es muss schriftlich, begründet und rechtzeitig gestellt werden. Der Entscheid wird dem Vertreter zugestellt.
> - Eine verweigerte Fristverlängerung ist ein Zwischenentscheid und kann nicht selbständig angefochten werden.
> - Beim Bund gibt es keine eigene Regelung. Die Fristerstreckung ist kantonal geregelt und deckt die direkte Bundessteuer mit ab.
> - Nicht geprüft habe ich, ob das Gesuch pro Mandant oder als Sammelgesuch gestellt werden kann. Die Gebühr für natürliche Personen nennen die Quellen nicht.
> 
> **Fundstellen:** `tg-stp-155-2__c0002` (Treuhänder bis 31. Dezember), `tg-stp-155-2__c0001` (30. September), `tg-stp-155-2__c0005` (Entscheid). Status: ☑️ agent-geprüft, Abnahme offen. Die fachliche Beurteilung bleibt bei der Fachperson.

## q15

**Frage:** ZH: Bis wann ist die Steuererklärung 2025 einzureichen und wie lange wird höchstens Fristerstreckung gewährt?

**Soll (Referenz):** Einreichung bis 31.03.2026; Fristerstreckung längstens bis 30. November (ZStB 132.1 / WL ZH 2025).

**Antwort des Agenten** (25.5 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__zeige):

> **ZH · Steuerjahr 2025**
> 
> - **Ordentliche Einreichefrist:** 31. März 2026 (☑️ agent-geprüft; zh-wl-2025__c0017: «Die Steuererklärung ist bis am 31. März 2026 einzureichen.»).
> - **Maximale Fristerstreckung:** Rechtzeitig gestellten Gesuchen ist längstens bis 30. November des Folgejahres zu entsprechen. Für das Steuerjahr 2025 ist das der **30. November 2026** (☑️ agent-geprüft; zh-zstb-132-1__c0024). Das sind rund 8 Monate über die ordentliche Frist hinaus.
> - **Gesuch:** Es muss vor Fristablauf beim Gemeindesteueramt eingehen. Das erste Gesuch gilt ohne gegenteiligen Entscheid als stillschweigend bewilligt.
> - **Bund:** Die direkte Bundessteuer hat keine eigene Frist. Einreichefrist und Fristerstreckung richten sich nach dem Kanton.
> 
> **Zur heutigen Lage (9. November 2026):** Die ordentliche Frist ist abgelaufen. Eine Fristerstreckung ist nur möglich, wenn sie vor Ablauf der Frist beantragt wurde. Gesuche nach Fristablauf, ob ordentlich oder bereits erstreckt, werden abgewiesen. Dann bleibt nur noch die Wiederherstellung der Frist (§ 15 StV, Art. 119 Abs. 2 DBG). Dafür muss ein Wiederherstellungsgrund vorliegen, und das Gemeindesteueramt entscheidet darüber.
> 
> Falls die Erklärung 2025 bis zum 30. November 2026 eingereicht werden muss, ist das nur sicher, wenn zuvor eine Erstreckung bewilligt oder beantragt wurde. Ob das hier der Fall war, ist nicht geprüft.
> 
> Die Quelle nennt keine Kosten für die Fristerstreckung. Die fachliche Beurteilung bleibt bei der Fachperson.

## q16

**Frage:** AR: Was kostet die zweite Fristverlängerung?

**Soll (Referenz):** CHF 25 (erste Verlängerung kostenlos, jede weitere CHF 25; MB 18 / WL AR 2025).

**Antwort des Agenten** (21.5 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **AR · Steuerjahr 2025** (kein Jahr genannt, daher 2025 angenommen)
> 
> Die zweite Fristverlängerung kostet **CHF 25**. Das gilt auch für jede weitere. Nur die erste Fristverlängerung ist kostenlos.
> 
> - Der Betrag steht in der Wegleitung AR 2025 (Chunk `ar-wl-2025__c0012`) und im Merkblatt 18, Gebührenansätze KGV ab 1.9.2025: «Fristverlängerungen (im Wiederholungsfall): Fr. 25» (Chunk `ar-mb-18__c0001`). Status: ☑️ agent-geprüft, Abnahme offen.
> - Die Rechtsgrundlage ist Art. 59a StV AR (Chunk `ar-stv__art-59a`): Die Kantonale Steuerverwaltung erhebt eine Gebühr für die Fristerstreckung, die erstmalige ist kostenlos.
> - Das Gesuch muss vor Ablauf der Einreichefrist bei der Kantonalen Steuerverwaltung eingehen. Es kann online gestellt werden (esteuern.ar.ch).
> - **Bund:** Die Fristerstreckung ist kantonal geregelt, die direkte Bundessteuer hat keine eigene Gebühr.
> 
> Die Angabe aus dem Seed, dass Treuhänder-Sammelgesuche anders behandelt würden, ist in den Quellen nicht belegt. Dazu mache ich keine Aussage.

## q17

**Frage:** Krankheitskosten SG 2025: Ab welchem Selbstbehalt sind sie abziehbar – und beim Bund?

**Soll (Referenz):** SG: Selbstbehalt 2 % (Art. 46 StG SG); Bund: 5 % (Art. 33 Abs. 1 lit. h DBG, KS 11).

**Antwort des Agenten** (25.9 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__zeige):

> **SG · Steuerjahr 2025**
> 
> **Kanton St. Gallen: Selbstbehalt 2 %**
> - Abziehbar sind Krankheits- und Unfallkosten, soweit du sie selbst trägst und sie 2 % der Nettoeinkünfte übersteigen.
> - Die Nettoeinkünfte sind das Nettoeinkommen nach Ziff. 20 im Formular. Sie sind bereits um die Aufwendungen und die Abzüge nach Art. 39–45 StG SG vermindert.
> - Quelle: Art. 46 Abs. 1 lit. a StG SG («diese 2 Prozent der Nettoeinkünfte übersteigen»), Chunk `sg-stg-2025__art-46`. Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Bund (direkte Bundessteuer): Selbstbehalt 5 %**
> - Abziehbar sind die selbst getragenen Kosten, soweit sie 5 % der um die Aufwendungen (Art. 26–33 DBG) verminderten steuerbaren Einkünfte übersteigen.
> - Die Bezugsgrösse ist beim Bund also eine andere als im Kanton. Sie wird nach Art. 26–33 DBG berechnet, nicht nach Ziff. 20 des Formulars.
> - Quelle: Art. 33 Abs. 1 lit. h DBG, Chunk `bund-dbg-2025__art-33-t3`. Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Im Formular SG 2025**
> - Es gibt nur eine Spalte. Die Steuerbehörde setzt den abweichenden Bundesselbstbehalt automatisch an (Merkblatt 32, `sg-wl-2025__c0173`).
> - Ziff. 21.1 enthält drei Codes: Vorkolonne Code 650 (Kosten nach Abzug von Beiträgen Dritter), Selbstbehalt Code 238 und Abzug Code 240.
> - Der Abzug rechnet sich so: max(0; Vorkolonne − 2 % × Ziff. 20) (Quellen `sg-form-1-2025__c0010`, `sg-wl-2025__c0098`).
> - Die Einzelrechnungen trägst du im Formular 6 ein.
> 
> **Weitere Punkte**
> - Behinderungsbedingte Kosten werden ohne Selbstbehalt abgezogen (Ziff. 21.2, Art. 46 Abs. 1 lit. abis StG SG und Art. 33 Abs. 1 lit. hbis DBG).
> - Die Diät-Pauschale (z. B. Zöliakie) beträgt Fr. 2'500 und zählt zu den Krankheitskosten mit Selbstbehalt. Beim ersten Mal braucht es eine ärztliche Bescheinigung. Bei Diabetes gilt sie nicht.
> - Krankenkassenprämien gehören nicht hierher, sondern in Ziff. 14.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q18

**Frage:** PK-Einkauf CHF 20'000 wurde über den Lohn abgezogen (Lohnausweis Ziff. 10.2). Darf er nochmals in der Steuererklärung abgezogen werden?

**Soll (Referenz):** Nein – BVG-Einkauf über Lohnabzug (Lohnausweis Ziff. 10.2) ist bereits im Nettolohn berücksichtigt; nur direkt bezahlte Einkäufe separat abziehen.

**Antwort des Agenten** (47.8 s · Tools: 10 Aufrufe steuerwiki__wert, steuerwiki__beleg, steuerwiki__suche, steuerwiki__zeige):

> Ich habe die Lohnausweis-Wegleitung geprüft und gebe jetzt die Antwort.
> 
> **Kanton: nicht genannt · Steuerjahr 2025 (angenommen).** Die Antwort stützt sich auf Bundesrecht und die Lohnausweis-Wegleitung. Für die Formularziffer bräuchte ich den Wohnkanton am 31.12.
> 
> **Kurz: Nein, nicht nochmals abziehen, sofern Ziff. 11 (Nettolohn) tatsächlich um die CHF 20'000 gekürzt ist.**
> 
> **Begründung**
> - Ziff. 10.2 enthält die im Bruttolohn enthaltenen, vom Lohn abgezogenen Einkaufsbeiträge (WL Lohnausweis Rz 45, `bund-wl-lohnausweis-2026__c0036`).
> - Der Nettolohn (Ziff. 11) ergibt sich aus Bruttolohn (Ziff. 8) minus Total der Abzüge (Ziff. 9 und 10) (Rz 47, `bund-wl-lohnausweis-2026__c0038`).
> - Dieser Nettolohn ist der für die Steuererklärung massgebende Betrag und gehört in die Einkünfte aus unselbständiger Erwerbstätigkeit. Der Einkauf ist damit bereits einmal berücksichtigt.
> - Ziehen Sie ihn zusätzlich in der Steuererklärung ab, entsteht ein Doppelabzug.
> 
> **Gegenprobe vor dem Ausfüllen**
> - Rechnen Sie Ziff. 8 − Ziff. 9 − Ziff. 10 (10.1 + 10.2) nach. Das Ergebnis muss Ziff. 11 sein.
> - Ist Ziff. 11 nicht um Ziff. 10.2 gekürzt, ist der Lohnausweis falsch. Dann muss der Arbeitgeber ihn berichtigen, oder Sie müssen den Einkauf ausnahmsweise in der Steuererklärung geltend machen. Das ist mit der Fachperson zu klären.
> 
> **Gegenfall: selbst einbezahlter Einkauf**
> - Einen Einkauf, den Sie direkt an die Pensionskasse überwiesen haben (nicht vom Lohn abgezogen), bescheinigt die Vorsorgeeinrichtung mit Formular 21 EDP und nicht der Arbeitgeber (Rz 46, `bund-wl-lohnausweis-2026__c0037`; MB 21 EDP). Nur diesen Einkauf machen Sie in der Steuererklärung als Abzug geltend.
> - Im Fall mit Abzug vom Lohn betrifft das nur zusätzliche Direkteinzahlungen.
> 
> **Vorbehalte**
> - Die Wegleitung ist als Version 2026 im Wiki hinterlegt. Eine 2025er-Fassung habe ich nicht gefunden. Ich gehe davon aus, dass sich die Ziffernlogik nicht geändert hat, aber das ist nicht geprüft.
> - Die Fundstellen sind ☑️ agent-geprüft (Abnahme offen).
> - Ob Ihr Kanton den Einkauf bei der Staats- und Gemeindesteuer anders behandelt oder Höchstgrenzen (Einkaufspotenzial, Sperrfrist von 3 Jahren für Kapitalbezüge) vorsieht, habe ich nicht geprüft, weil der Kanton fehlt. Nennen Sie ihn (AR, SG, TG oder ZH), dann nenne ich die Formularposition.

## q19

**Frage:** Weiterbildungskosten CHF 15'000 (ZH, 2025), Arbeitgeber hat nichts bezahlt. Wie viel ist abziehbar (Kanton/Bund)?

**Soll (Referenz):** ZH Staat max. CHF 12'400 (zh-stg-2025__par-31-t4); Bund max. CHF 13'000 (bund-dbg-2025__art-33-t4).

**Antwort des Agenten** (26.0 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **ZH · Steuerjahr 2025: Weiterbildungskosten CHF 15'000, selbst getragen**
> 
> | | Abziehbar | Nicht abziehbar |
> |---|---|---|
> | **Kanton (Staatssteuer)** | **CHF 12'400** | CHF 2'600 |
> | **Bund (direkte Bundessteuer)** | **CHF 13'000** | CHF 2'000 |
> 
> **Rechnung**
> - Der Arbeitgeber hat nichts bezahlt. Die selbst getragenen Kosten sind damit CHF 15'000. Beiträge Dritter in Form. 367, Code 2901, sind CHF 0.
> - Kanton: min(15'000; 12'400) = 12'400.
> - Bund: min(15'000; 13'000) = 13'000.
> 
> **Eintrag im Formular**
> - Der Abzug kommt in Ziff. 16.2, Code 292, «Berufsorientierte Aus- und Weiterbildungskosten».
> - Dafür füllst du Form. 367 aus. In der Spalte Staatssteuer trägst du 12'400 ein, in der Spalte Bundessteuer 13'000. Die Codes sind 2900 (Total der Kosten) und 2920 (zulässiger Abzug).
> - Bei einem Ehepaar gilt die Limite pro Person (Codes 2900 bis 2920 für Person 1, 2903 bis 2921 für Person 2).
> 
> **Voraussetzungen**
> - Du hast einen Abschluss Sek. II oder das 20. Altersjahr vollendet. Es darf nicht die Ausbildung bis zum ersten Sek.-II-Abschluss sein.
> - Die Kosten müssen berufsorientiert sein (Aus- oder Weiterbildung, inkl. Umschulung).
> - Massgebend ist das Jahr der Zahlung bzw. Fälligkeit, nicht der Kursbesuch. Nur 2025 bezahlte Beträge zählen.
> - Form. 367 muss vollständig ausgefüllt beiliegen. Die Rechnungen und Zahlungsbelege reichst du nur auf Verlangen ein.
> - Prüfe, dass im Lohnausweis Ziff. 13.3 kein Arbeitgeberbeitrag steht. Auch direkt ans Bildungsinstitut bezahlte Beiträge des Arbeitgebers wären abzuziehen.
> 
> **Fundstellen (Status ☑️ agent-geprüft, Abnahme offen)**
> - Kanton: zh-stg-2025__par-31-t4, «bis zum Gesamtbetrag von Fr. 12 400».
> - Bund: bund-dbg-2025__art-33-t4, «bis zum Gesamtbetrag von 13 000 Franken».
> - Formular und Wegleitung: zh-form-367-2025__c0001, zh-form-300-2025__c0008, zh-wl-2025__c0093.
> 
> Ob die Kosten berufsorientiert sind und die Voraussetzungen erfüllt sind, beurteilt die Fachperson anhand der Kursunterlagen. Das habe ich nicht geprüft.

## q20

**Frage:** Spenden CHF 50 an eine gemeinnützige Organisation (TG 2025) – abziehbar?

**Soll (Referenz):** Nein – TG: Zuwendungen nur abziehbar, wenn sie CHF 200 übersteigen (StG TG § 34 Abs. 1 Ziff. 11); Bund: ab CHF 100.

**Antwort des Agenten** (25.8 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **TG · Steuerjahr 2025: Eine Spende von CHF 50 ist nicht abziehbar.** Weder bei der Staats- und Gemeindesteuer noch bei der direkten Bundessteuer wirkt sie sich aus.
> 
> | | Kanton (Staats-/Gemeindesteuer) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | Mindestbetrag | Selbstbehalt CHF 200. Abziehbar ist nur der Teil, der die CHF 200 übersteigt. | Der Gesamtbetrag der Spenden muss mindestens CHF 100 erreichen. Dann gibt es keinen Selbstbehalt. |
> | Rechnung bei CHF 50 | 50 − 200 → **CHF 0 abziehbar** | 50 < 100 → **kein Abzug** |
> 
> Quellen: tg-stg__par-34-t4 («soweit sie gesamthaft Fr. 200 übersteigen»), bund-dbg-2025__art-33a («wenn diese Leistungen im Steuerjahr 100 Franken erreichen»), tg-form-06-2025__c0002. Status: ☑️ agent-geprüft, Abnahme offen.
> 
> **Die Schwellen gelten für alle Spenden zusammen.** Gemeint ist die Summe aller freiwilligen Zuwendungen des Jahres an gemeinnützige oder öffentliche Zwecke, nicht jede Spende einzeln.
> - Beim **Bund** wird der Abzug möglich, sobald die Summe CHF 100 erreicht. Dann ist der ganze Betrag abziehbar.
> - Beim **Kanton** zählt nur der Teil über CHF 200.
> 
> **Wenn die Summe die Schwellen überschreitet**, gilt Folgendes:
> - Eingetragen wird in Ziff. 23.2 (Formular 6, Code 366). Jede Institution wird einzeln mit Name und Sitz aufgeführt. Sammelvermerke wie «diverse Organisationen» werden nicht anerkannt.
> - Die Empfängerin muss eine steuerbefreite juristische Person mit Sitz in der Schweiz sein. Religiöse, kulturelle, gesellige und sportliche Zwecke sowie Empfänger im Ausland sind nicht abziehbar.
> - Das Maximum liegt beim Kanton bei 20 % des Nettoeinkommens (Ziff. 22), bei Nettoeinkommen bis CHF 40'000 bei CHF 8'000. Beim Bund liegt es bei 20 % des Nettoeinkommens.
> - Belege sind erst ab CHF 1'000 pro Zuwendung einzureichen. Darunter genügt die Quittung auf Verlangen (tg-wl-2025__c0220).
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q21

**Frage:** Was ändert sich 2026 bei der Säule 3a (Einkauf) und wo wird das im ZH-Formular 2026 eingetragen?

**Soll (Referenz):** Ab 2026 Einkauf (Nachzahlung) Säule 3a für Beitragslücken ab 2025 (max. 7'258 pro Einkaufsjahr, BVV 3 Art. 7a, KS 18a); ZH-Formular 2026: Ziff. 14.3 (Code 264, Detailfelder 276/278).

**Antwort des Agenten** (29.6 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position):

> **ZH · Steuerjahr 2026**
> 
> ## Was neu ist: Einkauf in die Säule 3a
> Ab der Steuerperiode 2026 können Sie zusätzlich zum ordentlichen 3a-Beitrag Beitragslücken nachträglich einkaufen. Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> - **Welche Lücken:** Nur Lücken, die ab 1.1.2025 entstanden sind, und zwar innerhalb der zehn Jahre vor dem Einkauf. Für 2026 ist deshalb faktisch nur die Lücke 2025 einkaufbar.
> - **Voraussetzungen:**
>   - In den Lückenjahren wurden AHV/IV/EO-Beiträge geleistet.
>   - Im Einkaufsjahr wurde der volle ordentliche Maximalbeitrag einbezahlt.
> - **Limite:** Höchstens die Summe der Lücken, in jedem Fall aber maximal **CHF 7'258**. Das gilt für Kanton und Bund gleich.
>   - Quellen: zh-wl-2026-uj__c0077 (Kanton) und bund-wl-2a-2026__c0051 (Bund).
>   - Zur Rechtsgrundlage: Sie ist nur aus der Wegleitung belegt. Den Artikel in der BVV 3 habe ich nicht geprüft.
> - **Ordentliche Beiträge bleiben unverändert** (zh-wl-2026-uj__c0075, Bund bund-bsv-masszahlen-2025-2026__c0003):
>   - Mit 2. Säule: max. CHF 7'258.
>   - Ohne 2. Säule: 20 % des Erwerbseinkommens, max. CHF 36'288.
> 
> ## Wo im ZH-Formular 2026
> - **Ziff. 14.3 «Einkauf Säule 3a»**: Person 1 Code **276**, Person 2 Code **278**, Summe in der Hauptkolonne Code **264** (zh-form-300-2026-uj__c0008).
>   - Rechnen: je Person min(Einkauf; Summe der Lücken ab 1.1.2025; 7'258).
>   - Der Abzug gilt für Kanton und Bund (Spalten Staatssteuer und Bundessteuer).
>   - Belege: Einkaufsbescheinigung der 3a-Einrichtung, Bescheinigung über den ordentlichen Maximalbeitrag im selben Jahr und Nachweis der AHV/IV/EO-Beiträge im Lückenjahr.
> - **Ziff. 14.1 / 14.2** ist für die ordentlichen 3a-Beiträge (Code 260/261, effektiv 262/263). Der Einkauf gehört nicht dorthin.
> 
> **Falls Sie einen Pensionskasseneinkauf (2. Säule) meinten:** Der steht nicht unter 14.3, sondern in **Ziff. 16.1, Code 280**. Eingetragen wird nur, was nicht schon im Lohnausweis Ziff. 10 abgezogen ist. Beizulegen ist die Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP). Kein Abzug gibt es, wenn innert drei Jahren ein Kapitalbezug folgt (zh-wl-2026-uj__c0088).
> 
> ## Vorbehalte
> - Das reguläre ZH-Formular und die Wegleitung 2026 sind laut Wiki (Stand 09.11.2026) noch nicht publiziert. Die Ziffern und Codes stützen sich auf die Fassung für unterjährige Steuerpflicht und sind am regulären Formular zu prüfen.
> - Eine Quelle zu den Maximalbeträgen nennt «ab 2025» ohne neues Datum für 2026. Die Wegleitung 2026 bestätigt CHF 7'258.
> - Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (30.6 s · Tools: 4 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Bund · Steuerjahr 2025.** Die Frage nennt keinen Kanton und kein Jahr, daher gilt hier Bundesrecht und 2025. Die genaue Formularziffer hängt vom Wohnsitzkanton am 31.12. ab. Das Wiki deckt ZH, SG, TG und AR ab.
> 
> **Wie wird zurückgefordert?**
> - Auf Dividenden und anderen Kapitalerträgen behält die ausschüttende Gesellschaft 35 % Verrechnungssteuer ab (☑️ `bund-vstg__art-13`).
> - Natürliche Personen stellen **keinen separaten Rückerstattungsantrag**. Sie fordern die Steuer zurück, indem sie die Erträge im **Wertschriftenverzeichnis** der kantonalen Steuererklärung deklarieren (☑️ `wert bund 2025 verrechnungssteuer`).
> - Das Wertschriftenverzeichnis führt die Titel mit Steuerwert am 31.12. und Bruttoertrag auf.
> - Die Steuerverwaltung verrechnet die 35 % mit der Steuerschuld. Ein Überschuss wird ausbezahlt.
> - Es gibt kein eigenes Bundesformular. Die kantonale Erklärung deckt Kanton und Bund ab.
> 
> **Wo wird der Anspruch ausgewiesen?**
> - Der Anspruch ergibt sich aus dem deklarierten Bruttoertrag im Wertschriftenverzeichnis, wo die Verrechnungssteuer ausgewiesen wird.
> - Der Betrag beträgt 35 % der Erträge, bei denen Verrechnungssteuer abgezogen wurde.
> - Die genaue Ziffer und Kolonne habe ich nicht geprüft, weil der Kanton fehlt. Mit Kanton kann ich sie über `position <kt> 2025 …` nachschlagen.
> - Das Bundesformular DA-1 gilt nicht für die Verrechnungssteuer. Es betrifft nur die Anrechnung ausländischer Quellensteuern (☑️ `bund-form-da1-2025__c0002`).
> 
> **Wichtig (Verwirkung, Art. 23 VStG, ☑️ `bund-vstg__art-23`):**
> - Wer Erträge oder das zugrunde liegende Vermögen nicht deklariert, **verwirkt den Rückerstattungsanspruch** (Abs. 1). Deshalb müssen alle Titel und Erträge im Verzeichnis stehen.
> - Die Verwirkung tritt nicht ein, wenn die Angabe nur **fahrlässig** fehlte und im noch offenen Verfahren nachgeholt wird. Das gilt auch, wenn die Behörde die Erträge selbst aufrechnet (Abs. 2).
> - Die Verwirkung gilt für die gleichen Voraussetzungen im Bund und in allen Kantonen.
> 
> **Offen:**
> - Je nach Fall gibt es Sonderregeln, zum Beispiel die Vorsorgenehmer-Fälle in KS 18/18a oder die Tax-Voucher-Regeln in KS VST 21. Sie sind hier nicht geprüft.
> - Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Für die konkrete Ziffer im Formular brauche ich den Kanton (ZH, SG, TG oder AR).

## q23

**Frage:** Vergleiche den Versicherungsabzug 2025 für Alleinstehende ohne Kinder in AR, SG, TG, ZH und beim Bund.

**Soll (Referenz):** Alleinstehend ohne Kinder 2025 (mit 2. Säule/3a): AR 2'700 · SG 3'400 · TG 3'500 · ZH 2'900 · Bund 1'800.

**Antwort des Agenten** (29.5 s · Tools: 2 Aufrufe steuerwiki__vergleich, steuerwiki__wert):

> **Versicherungsabzug 2025, alleinstehend ohne Kinder**
> 
> Die Frage nennt mehrere Kantone, deshalb habe ich sie nebeneinander verglichen (Steuerjahr 2025).
> 
> | Jurisdiktion | Mit Beiträgen an Säule 2/3a | Ohne Beiträge an Säule 2/3a | Fundstelle (Standardfall) |
> |---|---|---|---|
> | **Bund** (dBSt) | CHF 1'800 | CHF 2'700 | bund-dbg-2025__art-33-t2 |
> | **ZH** | CHF 2'900 | CHF 4'350 | zh-stg-2025__par-31-t2 |
> | **SG** | CHF 3'400 | CHF 3'900 | sg-stg-2025__art-45-t2 |
> | **TG** | CHF 3'500 | kein separater Ansatz | tg-stg__par-34-t3 |
> | **AR** | CHF 2'700 | kein separater Ansatz | ar-stg__art-35-t2 |
> 
> Alle Werte haben den Status ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme ist offen.
> 
> **Rangfolge** (Standardfall, mit Beiträgen an Säule 2/3a):
> 1. TG CHF 3'500
> 2. SG CHF 3'400
> 3. ZH CHF 2'900
> 4. AR CHF 2'700
> 5. Bund CHF 1'800
> 
> **Hinweise**
> - **Standardfall:** Die Spalte «Mit Beiträgen» gilt für Alleinstehende, die Beiträge an die Säule 2 oder 3a leisten. Das ist der übliche Fall bei Erwerbstätigen. Der Bund nennt diese Bedingung ausdrücklich (bund-dbg-2025__art-33-t2).
> - **Erhöhter Ansatz:** Ohne solche Beiträge gilt in ZH, SG und beim Bund ein höherer Abzug. Beim Bund stammen die CHF 2'700 aus der Wegleitung bund-rs-2-210__c0006.
> - **TG und AR:** Das Wiki führt für den Fall ohne Beiträge keinen eigenen Ansatz (Eintrag «nicht anwendbar»). Ich habe dazu nichts angenommen.
> - **Kinder:** Sie sind hier ausgeklammert. Pro Kind kommt ein Zuschlag dazu: Bund CHF 700, ZH CHF 1'300, SG CHF 1'100, TG CHF 1'000, AR CHF 1'000.
> - **Bundesabzug im Formular:** Die kantonale Steuererklärung deckt Kanton und Bund ab. Der Bundesabzug wird dort mit dem Bundesansatz berücksichtigt. Zu den Ziffern und zur genauen Erfassung kann ich `position <kt> 2025 Versicherungsprämien` aufrufen.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der zuständigen Fachperson.

## q24

**Frage:** Steuerfreie Vermögensbeträge (Sozialabzüge) 2025 in SG für ein Ehepaar mit einem minderjährigen Kind?

**Soll (Referenz):** SG 2025: 150'000 (Ehepaar) + 20'000 pro minderjähriges Kind = 170'000 (sg-stg-2025__art-64).

**Antwort des Agenten** (23.6 s · Tools: 4 Aufrufe steuerwiki__formular, steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **SG · Steuerjahr 2025: Sozialabzüge auf dem Vermögen, Ehepaar mit 1 minderjährigem Kind**
> 
> Der steuerfreie Vermögensbetrag beträgt **CHF 170'000**. Er gilt nur für den Kanton und die Gemeinde. Die direkte Bundessteuer kennt keine Vermögenssteuer.
> 
> | Ziffer (Formular 1) | Abzug | Betrag Kanton SG |
> |---|---|---|
> | 36.2 (Code 332) | Gemeinsam steuerpflichtige Ehegatten (2 × 75'000) | CHF 150'000 |
> | 36.3 (Code 334) | 1 minderjähriges Kind unter elterlicher Sorge/Obhut | CHF 20'000 |
> | **Total** | | **CHF 170'000** |
> 
> Die Summe habe ich mit `rechne` gebildet.
> 
> - **Zivilstand und Kind:** Massgebend sind die Verhältnisse am 31.12.2025. Der Kinderabzug gilt nur für minderjährige Kinder unter elterlicher Sorge/Obhut. Für volljährige Kinder in Ausbildung gibt es kein 36.3.
> - **Eintrag im Formular:** Die Sozialabzüge stehen in voller Höhe in ihrer eigenen Ziffer, auch wenn das Reinvermögen kleiner ist. Erst das steuerbare Vermögen ist mindestens 0.
> - **Bund:** Beim Bund gibt es keinen Vermögensabzug.
> 
> **Fundstellen:**
> - sg-stg-2025__art-64 (75'000 pro Steuerpflichtigen und zusätzlich 20'000 pro Kind)
> - sg-wl-2025__c0118 (150'000 gemeinsam)
> - sg-form-1-2025__c0013 (Ziff. 36.1 und 36.2)
> 
> **Status:** ☑️ agent-geprüft. Die Fundstelle ist geprüft, die Abnahme ist offen. Die fachliche Beurteilung bleibt bei der Fachperson.

## q25

**Frage:** Welcher Verzugszins gilt 2026 für die direkte Bundessteuer?

**Soll (Referenz):** 4.00 % (RS 2-215, bund-rs-2-215__c0010/c0011).

**Antwort des Agenten** (21.2 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Bund · Steuerjahr 2026:** Der Verzugszins auf der direkten Bundessteuer beträgt **4 %** pro Jahr. Der Rückerstattungszins liegt ebenfalls bei 4 %. Zum Vergleich: 2025 waren es 4,5 %.
> 
> - Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> - Fundstelle: `bund-rs-2-215__c0010` («Verzugs- und Rückerstattungszins 4,50 → 4,00»).
> 
> Verwandte Zinssätze Bund 2026:
> - **Vergütungszins** auf Vorauszahlungen: 0 % (2025: 0,75 %).
> - **Ausgleichszins:** Den kennt der Bund nicht. Ausgleichszinsen gibt es nur auf kantonaler Ebene.
> 
> Die Fachperson sollte den Wert vor der Verwendung bestätigen, weil die Abnahme noch offen ist.

## q26

**Frage:** Wann wird der Eigenmietwert abgeschafft und gilt das schon für 2026?

**Soll (Referenz):** Abschaffung per 1.1.2029 (Bundesratsbeschluss 01.04.2026); für 2025–2028 gilt bisheriges Recht – 2026 also noch Eigenmietwert.

**Antwort des Agenten** (27.0 s · Tools: 5 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> Let me read the press release itself for details.
> 
> **Bund · Steuerjahr 2026** (die Frage nennt keinen Kanton, die Antwort gilt für das Bundesrecht und damit grundsätzlich für alle Kantone)
> 
> **Wann?** Der Bundesrat hat am 1. April 2026 beschlossen, die Reform der Wohneigentumsbesteuerung **auf den 1. Januar 2029** in Kraft zu setzen. Ab diesem Datum entfällt die Besteuerung des Eigenmietwerts auf selbstgenutztem Wohneigentum (Quelle: `bund-mm-eigenmietwert-abschaffung__c0002`). Im September 2025 haben Volk und Stände zugestimmt (`…__c0003`).
> 
> **Gilt das schon für 2026?** Nein. Für 2026 bleibt der Eigenmietwert steuerbar, das gilt auch für 2027 und 2028. Die Steuererklärung 2026 wird noch wie bisher ausgefüllt. Der Eigenmietwert wird als Einkommen aufgerechnet, und die Liegenschaftsunterhaltskosten können abgezogen werden. Beim Unterhalt gibt es die Pauschale von 10 % (Gebäude bis 10 Jahre) oder 20 % (Gebäude über 10 Jahre) oder die effektiven Kosten (`bund-lkv__art-5`, ☑️ agent-geprüft).
> 
> **Was ändert sich ab 2029?** Laut Medienmitteilung (`…__c0004`):
> - Der Eigenmietwert entfällt bei Bund, Kantonen und Gemeinden.
> - Der Abzug der Unterhaltskosten entfällt für selbstgenutztes Wohneigentum. Bei vermieteten oder verpachteten Liegenschaften bleibt er.
> - Schuldzinsen sind nur noch im Verhältnis des Werts der vermieteten oder verpachteten Liegenschaften zum gesamten Vermögen abziehbar. Wer erstmals in der Schweiz ein Eigenheim erwirbt, erhält einen zeitlich und betragsmässig begrenzten Ersterwerberabzug für Schuldzinsen.
> - Bei der direkten Bundessteuer entfallen die Abzüge für Energiespar- und Umweltschutzinvestitionen. Die Kantone können sie zeitlich begrenzt beibehalten.
> - Die Kantone können eine Objektsteuer auf überwiegend selbstgenutzten Zweitliegenschaften einführen.
> 
> **Vorbehalt:** Der Stand ist die Medienmitteilung vom 1.4.2026, deren Fundstellen im Wiki nicht mit einem Status geführt sind. Die kantonale Umsetzung (Gesetzesanpassungen, Objektsteuer) habe ich nicht geprüft. Wenn Sie einen Kanton nennen (AR, SG, TG, ZH), schaue ich dort nach.

## q27

**Frage:** Zitiere die Regel zum Abzug privater Schuldzinsen im DBG (Steuerjahr 2025) mit Artikel.

**Soll (Referenz):** Art. 33 Abs. 1 lit. a DBG (Fassung 2025): private Schuldzinsen im Umfang der steuerbaren Vermögenserträge (Art. 20, 20a, 21) und weiterer CHF 50'000.

**Antwort des Agenten** (23.5 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Bund (direkte Bundessteuer) · Steuerjahr 2025**
> 
> **Art. 33 Abs. 1 lit. a DBG** (Chunk `bund-dbg-2025__art-33-t1`, Fassung gültig bis 31.12.2025):
> 
> > «Von den Einkünften werden abgezogen:
> > a. die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken. Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten oder ihr sonst wie nahe stehenden natürlichen Person zu Bedingungen gewährt, die erheblich von den im Geschäftsverkehr unter Dritten üblichen Bedingungen abweichen;»
> 
> **Kurz erklärt**
> - Der Abzug ist begrenzt auf die steuerbaren Vermögenserträge nach Art. 20, 20a und 21 DBG, plus 50 000 Franken.
> - Darlehen einer Kapitalgesellschaft an eine massgeblich beteiligte oder nahestehende Person zu nicht marktüblichen Bedingungen sind vom Abzug ausgeschlossen.
> 
> **Nicht geprüft:** Ob die 50 000 Franken pro Person oder pro Ehepaar gelten, steht nicht im zitierten Artikeltext. Ich habe das hier nicht nachgeschlagen. Die Kreisschreiben KS 22a (z. B. `bund-ks-22a__c0002`, `bund-ks-22a__c0014`) behandeln die Abgrenzung zwischen privaten und geschäftlichen Schuldzinsen sowie die Auslegung des Abzugs. Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## q28

**Frage:** Ist ein Leasingvertrag für das Privatauto steuerlich relevant? Was ist mit den Leasingraten?

**Soll (Referenz):** Leasingraten sind keine Schuldzinsen und grundsätzlich nicht abziehbar (Lebenshaltung); relevant nur für Fahrkosten-Begründung/Geschäftsauto, Vermögen (kein Eigentum).

**Antwort des Agenten** (30.1 s · Tools: 4 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read, steuerwiki__zeige):

> **Kurz: Nein.** Bei einem privat geleasten Auto sind weder der Leasingvertrag noch die Leasingraten ein Wert in der Steuererklärung. Das gilt für 2025 (kein Jahr genannt) und ist ein Querschnitt über die Kantone, weil Sie keinen Kanton genannt haben. Falls der Wohnsitz am 31.12. relevant wird, nennen Sie ihn bitte. Die Einordnung als Beleg hängt nicht davon ab.
> 
> **Leasingraten**
> - Sie sind nicht abziehbar. Es sind Lebenshaltungskosten (Art. 34 DBG, laut Tool-Karte; diese Norm habe ich nicht separat geöffnet).
> - Der Zinsanteil in der Rate ist keine Schuldzinsen-Position. Die Rate gehört deshalb weder in Ziff. «Schuldzinsen» noch ins Schuldenverzeichnis.
> - Fundstelle (Beispiel ZH): WL ZH 2025, Ziff. 12 Schuldzinsen, Chunk `zh-wl-2025__c0073`. Dort steht: «Nicht abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den darin enthaltenen Zinsanteilen).» Das Wort «Nicht» steht im Chunk noch vor einem Seitenumbruch, der Sinn ist aber eindeutig.
> - Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Vermögen**
> - Ein geleastes Fahrzeug gehört Ihnen nicht und wird nicht deklariert. Ein Auto im Eigentum würde dagegen im Vermögen erscheinen.
> 
> **Fahrkosten (Arbeitsweg)**
> - Das Leasing ändert daran nichts. Ein Abzug für das Privatauto ist nur in begründeten Fällen mit Kilometerpauschale möglich.
> - Die Leasingkosten sind mit dieser Pauschale abgegolten. Sie können sie nicht zusätzlich geltend machen.
> - Die Höhe der Pauschale ist kantonsabhängig. Ich habe sie hier nicht geprüft.
> 
> **Ausnahmen**
> - Wenn die Leasingnehmerin oder der Leasingnehmer eine selbständig erwerbende Person ist und das Auto geschäftlich genutzt wird, ist der geschäftliche Anteil Aufwand der Jahresrechnung. Das ist aber nicht das Privatauto.
> - Wenn der Arbeitgeber least, gehört der Vertrag nicht in Ihre Steuererklärung. Der Privatanteil läuft dann über den Lohnausweis.
> 
> **Ablage**
> - Der Vertrag ist kein Steuerbeleg. Er bekommt keine Steuerbeleg-Kategorie, weder «Belege eingereicht» noch «Belege Sonstiges». Es gibt keinen Wert in der Deklaration, der damit belegt werden müsste.
> - Die Einreichepflicht entfällt damit ebenfalls.
> - Behalten Sie den Vertrag allenfalls als Information. Nützlich ist er nur, um zu klären, wer Leasingnehmer ist, und um die Kilometerleistung zu kennen, falls Fahrkosten geltend gemacht werden.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der zuständigen Fachperson.

## q29

**Frage:** Wie hoch ist der Kinderabzug im Kanton Bern 2025?

**Soll (Referenz):** Nicht im Wiki (nur Bund, AR, SG, TG, ZH).

**Antwort des Agenten** (19.2 s · Tools: 0 Aufrufe ):

> Kanton Bern ist im Wiki nicht abgedeckt (nur Bund, AR, SG, TG, ZH). Ich gebe deshalb keinen Wert für Bern an, auch keine geschätzte oder aus einem anderen Kanton übernommene Zahl.
> 
> **Bern · Steuerjahr 2025: nicht im Wiki.**
> 
> Wenn Sie den Bundesteil brauchen: Der Kinderabzug bei der direkten Bundessteuer gilt unabhängig vom Wohnkanton. Ich kann ihn für 2025 nachschlagen. Alternativ kann ich den Wert für AR, SG, TG oder ZH liefern. Für Bern verweise ich auf die amtliche Wegleitung der Steuerverwaltung des Kantons Bern (Steuererklärung 2025) oder auf die Fachperson.
> 
> Soll ich den Bundeswert nachschlagen?

## q30

**Frage:** Ehepaar TG 2025, beide angestellt (Nettolohn 80'000 und 30'000), pendelt mit ÖV-Abo (CHF 1'200 bzw. 900). Erstelle die Abzüge Berufskosten (Fahrkosten, Verpflegung ohne Kantine, Pauschale übrige) je Person für Kanton und Bund mit Fundstellen.

**Soll (Referenz):** TG 2025 je Person: Fahrkosten = ÖV-Abo effektiv (1'200 bzw. 900; Max. 6'000 Staat / 3'300 Bund); Verpflegung ohne Kantine 15/Tag, max. 3'200 (beide Ebenen); übrige Pauschale 3 %: P1 80'000 → 2'400, P2 30'000 → 900 → Minimum 2'000 (beide Ebenen, BKV TG § 4a / BKV Bund).

**Antwort des Agenten** (39.6 s · Tools: 10 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__zeige, steuerwiki__rechne):

> **TG · Steuerjahr 2025 – Berufskosten Ehepaar (Formular 4.2 für Person 1, Formular 4.3 für Person 2)**
> 
> Der Verpflegungsabzug ist ein Höchstbetrag und hängt von Annahmen ab, die ich nicht kenne (siehe «Offen»). Fahrkosten und übrige Berufskosten sind fix.
> 
> | Position | Person 1 (Netto 80'000, Abo 1'200) | Person 2 (Netto 30'000, Abo 900) |
> |---|---|---|
> | **Fahrkosten** (Ziff. 2.1, Code 206 / 246) | Kanton 1'200 · Bund 1'200 | Kanton 900 · Bund 900 |
> | **Verpflegung ohne Kantine** (Ziff. 3.1, Code 214 / 254) | Kanton max. 3'200 · Bund max. 3'200 | Kanton max. 3'200 · Bund max. 3'200 |
> | **Übrige Berufskosten** (Ziff. 4, Code 220 / 260) | Kanton 2'400 · Bund 2'400 | Kanton 2'000 · Bund 2'000 |
> | **Total** (Ziff. 7, Code 240 / 280) | **6'800** (Kanton und Bund) | **6'100** (Kanton und Bund) |
> 
> Die Summe beider Personen beträgt 12'900 in jeder Spalte. Übertragen wird in Formular 1 Ziff. 10.1 (Person 1) und Ziff. 10.2 (Person 2), links Staat/Gemeinde, rechts Bund.
> 
> **Berechnung und Fundstellen**
> - **Fahrkosten:** Es gilt der tatsächlich bezahlte ÖV-Abopreis. Das Maximum ist beim Kanton 6'000 (tg-stg__par-29) und beim Bund 3'300 (bund-dbg-2025__art-26). Beide Abos liegen darunter, deshalb sind Kanton und Bund gleich. Die Regel steht in tg-form-04-2-2025__c0002 und tg-wl-2025__c0177 (☑️ agent-geprüft).
> - **Verpflegung:** Der Ansatz ist Fr. 15 pro Tag, maximal Fr. 3'200 pro Jahr, bei Kanton und Bund gleich (tg-form-04-2-2025__c0003, tg-wl-2025__c0183, bund-bkv-2025__anhang-1; ☑️). Der Höchstbetrag wird ab 214 Tagen erreicht (3'200 / 15 = 213.3). Bei 225 Arbeitstagen und 100 % Pensum sind es 3'200.
> - **Übrige Berufskosten:** Die Pauschale ist 3 % des Nettolohns, mindestens 2'000 und höchstens 4'000, bei Kanton und Bund gleich (tg-form-04-2-2025__c0004, tg-wl-2025__c0187, bund-bkv-2025__anhang-1; ☑️).
>   - Person 1: 3 % × 80'000 = 2'400.
>   - Person 2: 3 % × 30'000 = 900, angehoben auf das Minimum von 2'000.
> 
> **Offen**
> 1. **Verpflegung:** Der Abzug gilt nur, wenn die Heimkehr am Mittag unzumutbar ist, also bei grosser Entfernung oder sehr kurzer Essenspause. Ein ÖV-Abo allein genügt nicht (tg-wl-2025__c0183). Sonst ist der Abzug 0. Bei Teilzeit wird er nach Beschäftigungsgrad gekürzt, bei weniger als 12 Monaten Erwerb anteilig. Ich habe 100 % Pensum und durchgehende auswärtige Verpflegung angenommen und die tatsächlichen Tage nicht erfragt.
> 2. **Lohnausweis:** Als «Nettolohn» habe ich Ziff. 11 angenommen. Zu prüfen sind ausserdem Feld F (Geschäftsfahrzeug, dann kein Fahrkostenabzug), Feld G (Kantine, dann nur halber Verpflegungsabzug Fr. 7.50/Tag, max. 1'600) und ob der Arbeitgeber Fahrkosten vergütet. Ist das der Fall, ändern sich die Zahlen.
> 3. **Bund, Fahrkostenmaximum:** Die Quellen widersprechen sich (3'300 laut DBG, 3'200 laut WL 2a 2025, ⚠️ strittig). Das spielt hier keine Rolle, weil beide Abos weit darunter liegen.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q31

**Frage:** Ehepaar ZH 2026, beide erwerbstätig, Kind 3 Jahre in der Kita (Kosten CHF 30'000). Wie viel Drittbetreuung ist abziehbar (Kanton und Bund)?

**Soll (Referenz):** ZH 2026 Kanton max. CHF 25'300 pro Kind (zh-stg-2026__par-31-t3); Bund 2026 max. CHF 25'800 (bund-dbg-2026__art-33-t7). Abzug je Ebene getrennt.

**Antwort des Agenten** (26.1 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **ZH · Steuerjahr 2026**
> 
> Abziehbar sind beim Kanton CHF 25'300 und beim Bund CHF 25'800. Der Abzug steht auf Ziff. 16.6 (Code 376) der Steuererklärung.
> 
> | | Kanton (Staatssteuer) | Bund (dBSt) |
> |---|---|---|
> | Nachgewiesene Kosten | 30'000 | 30'000 |
> | Höchstbetrag pro Kind | 25'300 | 25'800 |
> | **Abziehbar** | **25'300** | **25'800** |
> | Nicht abziehbar (über der Limite) | 4'700 | 4'200 |
> 
> **Quellen**
> - Kanton: zh-stg-2026__par-31-t3 und zh-form-300-2026-uj__c0008.
> - Bund: bund-dbg-2026__art-33-t7.
> - Status: ☑️ agent-geprüft, Fundstelle geprüft, Abnahme offen.
> 
> **Voraussetzungen (alle erfüllt, soweit aus Ihren Angaben ersichtlich)**
> - Das Kind ist 3 Jahre alt (Jahrgang 2012–2026, unter 14) und lebt im gleichen Haushalt.
> - Beide Eltern sind gleichzeitig erwerbstätig. Das ist bei Ehepaaren Pflicht.
> - Die Kosten stehen im direkten Zusammenhang mit der Erwerbstätigkeit.
> 
> **Zu beachten**
> - **Verpflegung:** Verpflegung und Unterhalt des Kindes in der Kita gelten als Lebenshaltungskosten und sind nicht abziehbar (Bund KS 30 Ziff. 8.5, bund-ks-30__c0044). Enthalten die CHF 30'000 solche Anteile, sind sie auszuscheiden.
> - **Pauschale Rechnung:** Weist die Kita nur pauschale Kosten aus, werden diese um 20 % gekürzt. Dann wären es 24'000, also unter beiden Limiten. Abziehbar wären dann 24'000 bei Kanton und Bund.
> - **Belege:** Beizulegen ist die Aufstellung der Fremdbetreuungskosten mit den Empfängern. Rechnungen und Zahlungsnachweise der Kita halten Sie bereit.
> - **Formular:** Das reguläre ZH-Formular und die Wegleitung 2026 sind noch nicht publiziert (Stand 09.11.2026). Die Ziffer stützt sich auf die Fassung für unterjährige Steuerpflicht. Bitte Ziffer und Code am regulären Formular prüfen.
> - **Fachliche Beurteilung:** Sie bleibt bei der Fachperson.

## q32

**Frage:** SG 2025: Einfamilienhaus (Baujahr 2010), selbst bewohnt. Pauschalabzug Liegenschaftsunterhalt Kanton und Bund?

**Soll (Referenz):** SG 2025: 20 % des Eigenmietwerts, ohne Altersstaffel (sg-stv__art-29); Bund: Gebäude zu Beginn 2025 über 10 Jahre alt → 20 % (bund-lkv__art-5).

**Antwort des Agenten** (25.0 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **SG · Steuerjahr 2025: Pauschalabzug Liegenschaftsunterhalt, selbst bewohntes Einfamilienhaus (Baujahr 2010)**
> 
> **Kanton (Staats- und Gemeindesteuer): 20 %**
> - Die Basis ist der angerechnete Eigenmietwert (Formular 7, Teil B). Der Eigenmietwert ist in SG vorher um 30 % herabgesetzt worden (Art. 34 StG SG).
> - SG staffelt nicht nach Gebäudealter. Es gilt immer 20 %.
> - Quelle: sg-stv__art-29, sg-wl-2025__c0161. Status ☑️ agent-geprüft.
> 
> **Bund (direkte Bundessteuer): 20 %**
> - Das Gebäude ist zu Beginn der Steuerperiode 2025 rund 15 Jahre alt. Es ist damit über 10 Jahre alt, deshalb gilt der Satz von 20 %.
> - Der Satz von 10 % gilt nur für Gebäude bis 10 Jahre.
> - Quelle: bund-lkv__art-5. Status ☑️ agent-geprüft.
> 
> **Im Formular**
> - Sie füllen Formular 7, Teil C (Pauschalabzug) aus und übertragen den Betrag in Ziff. 15 (Code 716).
> - Das Formular hat nur eine Spalte. Der Bund wird dort nicht separat erfasst. Abweichungen für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor (Merkblatt 32, sg-wl-2025__c0173).
> - Hier ergibt sich ohnehin kein Unterschied, weil beide Sätze 20 % betragen. Die Basis für den Bund habe ich nicht separat geprüft.
> 
> **Zu beachten**
> - Sie wählen pro Liegenschaft und Steuerperiode zwischen der Pauschale und den tatsächlichen Kosten (Formular 7, Rückseite, C2).
> - Die Pauschale deckt alle Unterhalts- und Verwaltungskosten ab. Das gilt auch für Denkmalpflege sowie Energiespar- und Umweltinvestitionen (sg-wl-2025__c0161). Bei der Pauschale reichen Sie keine Belege ein. Belege brauchen Sie nur bei tatsächlichen Kosten, und dann auf Verlangen.
> - Bei Miteigentum gilt die Pauschale nur im Umfang Ihres Anteils.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q33

**Frage:** ZH 2025: Kind 19 Jahre, in Lehre (Ausbildung). Kinderabzug Kanton und Bund?

**Soll (Referenz):** ZH 2025 Kanton CHF 9'300 (volljährig in Erstausbildung, zh-stg-2025__par-34); Bund CHF 6'800 (bund-dbg-2025__art-35) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (27.9 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **ZH · Steuerjahr 2025: Kinderabzug für ein 19-jähriges Kind in der Lehre**
> 
> Das Kind hat Anspruch auf den vollen Kinderabzug, wenn es am 31.12.2025 in beruflicher Erstausbildung ist und Sie seinen Unterhalt zur Hauptsache tragen. Das Kind muss auf Ihre Unterstützung angewiesen sein. Eine Lehre ist berufliche Erstausbildung.
> 
> | | Kanton (Staatssteuer) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | Kinderabzug, Ziff. 24.1 | CHF 9'300 (Code 370) | CHF 6'800 |
> | Zusätzlicher Versicherungsabzug je Kind, Form. 365 Teil B Ziff. 3 (Code 613) | CHF 1'300 | CHF 700 |
> | **Total** | **CHF 10'600** | **CHF 7'500** |
> 
> Status: alle Werte ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> - **Kinderabzug Kanton:** zh-form-300-2025__c0010, zh-stg-2025__par-34 (§ 34 StG).
> - **Kinderabzug Bund:** bund-dbg-2025__art-35 (Art. 35 DBG).
> - **Versicherungsabzug:** zh-form-365-2025__c0002, zh-stg-2025__par-31-t2 (Kanton), bund-dbg-2025__art-33-t5 (Bund).
> 
> **Zusätzlich beim Bund:** Der Steuerbetrag ermässigt sich um CHF 263 pro Kind (bund-dbg-2025__art-36-t4, ☑️). Das ist kein Abzug im Formular, die Steuerverwaltung berücksichtigt ihn bei der Berechnung.
> 
> **Wo eintragen:**
> - Auf Seite 1 des Formulars führen Sie das Kind unter «Kinder in Ihrem Haushalt» auf, mit Geburtsdatum und Lehrfirma. Wohnt es nicht bei Ihnen, gehört es unter «Kinder ausserhalb Ihres Haushaltes» (Code 372).
> - Der Lehrvertrag gilt als Nachweis. Beim Kanton muss die Ausbildung mindestens ein halbes Jahr dauern.
> - Das Formular hat zwei Spalten, Staatssteuer und Bundessteuer. Der Bundesbetrag steht in der Bundesspalte.
> 
> **Vorbehalte:**
> - **Stichtag und Haushalt:** Die Verhältnisse am 31.12.2025 zählen. Der volle Abzug gilt für Verheiratete. Bei Alleinerziehenden gilt er bei alleinigem Sorgerecht oder bei gemeinsamem Sorgerecht mit erhaltenen Unterhaltsbeiträgen. Sonst gilt der halbe Abzug (Kanton 4'650 / Bund 3'400, Versicherungsabzug 650 / 350). Für getrennte Eltern ohne Haushaltsgemeinschaft müsste ich die Konstellation kennen.
> - **Eigenes Einkommen:** Wie viel Lehrlingslohn das Kind verdienen darf, ohne dass der «Hauptunterhalt» entfällt, habe ich hier nicht geprüft. Das liesse sich mit `suche` klären.
> - **Kinderalimente:** Wer für das Kind Unterhaltszahlungen abzieht (Ziff. 13.2), erhält keinen Kinderabzug.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q34

**Frage:** ZH 2025: Lohnausweis Feld G angekreuzt (Kantine). Welche Verpflegungspauschale gilt und in welche Ziffer des Berufsauslagenformulars?

**Soll (Referenz):** Verbilligte Verpflegung: CHF 7.50 pro Arbeitstag, max. CHF 1'600 pro Jahr (LS 631.33, zh-pauschalierung-berufsauslagen-2025__c0004); Form. 360 Ziff. 2.1 (verbilligt); Bund gleich.

**Antwort des Agenten** (27.1 s · Tools: 3 Aufrufe steuerwiki__beleg, steuerwiki__wert, steuerwiki__position):

> **ZH · Steuerjahr 2025**
> 
> **Pauschale bei angekreuztem Feld G (Kantine / Lunch-Checks):**
> - CHF 7.50 pro Arbeitstag, höchstens CHF 1'600 pro Jahr. Das ist der reduzierte Verpflegungsabzug (verbilligt), nicht der volle Satz von CHF 15 pro Tag und CHF 3'200 pro Jahr.
> - Berechnung: min(Arbeitstage × 7.50; 1'600). Mit `rechne` geprüft, z. B. 220 Tage × 7.50 = 1'650, begrenzt auf 1'600.
> - Quelle: zh-form-360-2025__c0003 und zh-pauschalierung-berufsauslagen-2025__c0004. Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Wo im Formular:**
> - Hilfsblatt Berufsauslagen Form. 360, **Ziff. 2.1** (Mehrkosten Verpflegung, verbilligte Variante), **Code 206** für Person 1 und Code 226 für Person 2.
> - Den Betrag trägst du in der Spalte Staatssteuer und in der Spalte Bundessteuer ein.
> - Ohne Kreuz bei Feld G und mit Verpflegung voll zulasten der Arbeitnehmerin oder des Arbeitnehmers gilt stattdessen Code 208 (Person 2: 228) mit CHF 15 pro Tag und höchstens CHF 3'200 pro Jahr.
> 
> **Bund (direkte Bundessteuer):**
> - Die Werte sind gleich: CHF 7.50 pro Tag, höchstens CHF 1'600 pro Jahr (bund-bkv-2025__anhang-1, bund-wl-2a-2025__c0045).
> - Das ist bereits der halbe Abzug, also nicht nochmals halbieren.
> - Beim Bund gibt es kein halbes Abzugsrecht, wenn der Arbeitgeber nur einen Barbeitrag leistet. Es gilt nur bei Gutscheinen oder bei Kantine bzw. Personalrestaurant.
> - Beim Bund entfällt der Abzug, wenn die Hauptmahlzeiten höchstens CHF 10 kosten.
> 
> **Zu beachten:**
> - Die Pauschale gilt nur, wenn die Arbeitspause die Heimkehr zum Mittagessen nicht erlaubt und trotzdem Mehrkosten entstehen.
> - Sie ist nicht kumulierbar mit dem vollen Verpflegungsabzug (Code 208), dem Schichtarbeitsabzug (Ziff. 2.2, Code 210) und dem Abzug für die Heimfahrt über Mittag. In der Praxis ist nur einer dieser Abzüge möglich.
> - Feld G wird auch bei Lunch-Checks oder einem verbilligten Personalrestaurant angekreuzt, unabhängig davon, ob die Person es nutzt.
> 
> **Nicht geprüft:** Die Wegleitung zum Lohnausweis (Regeln zu Feld G) liegt im Wiki nur in der Fassung 2026 vor, nicht für 2025. Die Beträge und die Ziffer stammen aber aus den 2025er Quellen (Form. 360 und Merkblatt Pauschalierung). Die Anzahl Arbeitstage musst du anhand des Arbeitszeitnachweises bestimmen.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q35

**Frage:** SG 2025: Kapitalbezug Säule 3a CHF 100'000. Wird das mit dem übrigen Einkommen besteuert? Wo deklarieren?

**Soll (Referenz):** Nein – Kapitalleistungen aus Vorsorge werden getrennt vom übrigen Einkommen (separate Jahressteuer) besteuert; SG Formular 1 Ziff. 40.1 (Säule 3a), Total Ziff. 41.

**Antwort des Agenten** (24.3 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__wert):

> **SG · Steuerjahr 2025**
> 
> **Besteuerung:** Nein, der Bezug wird nicht mit dem übrigen Einkommen zusammengerechnet. Kapitalleistungen werden gesondert vom übrigen Einkommen besteuert, mit einer separaten Jahressteuer (sg-wl-2025__c0119, ☑️ agent-geprüft).
> 
> - **Kanton/Gemeinde:** einfache Steuer von 2,2 % (übrige Steuerpflichtige) bzw. 2,0 % (gemeinsam steuerpflichtige Ehegatten). Der 2,0%-Satz gilt auch für Verwitwete, Getrennte, Geschiedene und Ledige, die mit Kindern oder Unterstützungsbedürftigen im gleichen Haushalt leben. Auf die einfache Steuer kommt der Steuerfuss von Kanton und Gemeinde (sg-stg-2025__art-52, ☑️). Allgemeine Abzüge und Sozialabzüge werden nicht gewährt.
> - **Bund:** ein Fünftel der Tarife nach Art. 36 DBG, ohne Sozialabzüge (bund-dbg-2025__art-38, ☑️).
> 
> **Wo deklarieren:** Formular 1 (Hauptformular), **Ziff. 40.1** «Kapitalleistungen aus gebundener Vorsorge Säule 3a» (sg-form-1-2025__c0014).
> 
> - Betrag: CHF 100'000, die im Jahr 2025 erhaltene Kapitalauszahlung. Bei mehreren Leistungen den Gesamtbetrag angeben.
> - Beleg: Die Bescheinigung der Bank oder Versicherung ist einzureichen (Formular 1 verlangt sie).
> - Die Deklaration dient nur zur Information. Der Betrag gehört nicht in Ziff. 6.4 und fliesst nicht in das steuerbare Einkommen ein. Die Steuerbehörde veranlagt die separate Steuer selbst.
> - Die Bundessteuer wird im Formular nicht separat erfasst. Es gibt eine Spalte, die Behörde nimmt die Abweichungen für die direkte Bundessteuer automatisch vor (sg-wl-2025__c0173).
> 
> **Orientierung (nicht berechnet):** Die einfache Steuer beträgt bei 2,2 % CHF 2'200 (bzw. CHF 2'000 bei 2,0 %). Die Gesamtbelastung ergibt sich erst mit dem Steuerfuss von Kanton und Gemeinde. Dazu kommt die Bundessteuer. Einen Steuerfuss habe ich nicht abgefragt, daher gebe ich keine Gesamtzahl an.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q36

**Frage:** ZH 2025: Geschiedener Mandant zahlt Unterhaltsbeiträge an die Ex-Frau (CHF 24'000) und für das minderjährige Kind (CHF 12'000). Was ist abziehbar, in welcher Ziffer?

**Soll (Referenz):** Ex-Ehefrau CHF 24'000 voll abziehbar, Ziff. 13.1 (Code 254); Kinderalimente CHF 12'000 abziehbar bis und mit Monat der Volljährigkeit, Ziff. 13.2 (Code 255); Empfänger versteuert; Bund gleich (Art. 33 Abs. 1 lit. c DBG).

**Antwort des Agenten** (27.9 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **ZH · Steuerjahr 2025: Unterhaltsbeiträge des geschiedenen Mandanten**
> 
> Beide Beträge sind voll abziehbar, CHF 36'000 insgesamt. Sie gehören in zwei verschiedene Ziffern:
> 
> | Zahlung | Betrag | Ziffer / Code | Abzug |
> |---|---|---|---|
> | An die Ex-Frau (für sie persönlich) | CHF 24'000 | **Ziff. 13.1, Code 254** | voll |
> | Für das minderjährige Kind | CHF 12'000 | **Ziff. 13.2, Code 255** | voll |
> | **Total** | **CHF 36'000** | | |
> 
> **Kanton und Bund:** Beide Ziffern gelten für Staats- und Bundessteuer in gleicher Höhe (Kanton = Bund). Die Beträge sind in beiden Spalten einzutragen.
> 
> **Fundstellen:** Ziff. 13.1: zh-form-300-2025__c0007, zh-wl-2025__c0075. Ziff. 13.2: zh-form-300-2025__c0007, zh-wl-2025__c0076. Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Bedingungen und Hinweise:**
> - **Nur effektiv bezahlte Beträge:** Abziehbar ist, was 2025 tatsächlich bezahlt wurde, nicht der bloss vereinbarte oder geschuldete Betrag. Beim Bund sind nur familienrechtlich geschuldete Alimente abziehbar, freiwillige nicht.
> - **Nur periodische Beiträge (13.1):** Eine Kapitalabfindung gilt als Schuldentilgung und ist nicht abziehbar. Naturalleistungen (Miete, Krankenkassenprämien, Schuldzinsen) werden den Geldzahlungen gleichgestellt.
> - **Kinderalimente (13.2):** Abziehbar sind sie bis und mit dem Monat, in dem das Kind 18 wird. Danach entfällt der Abzug, und stattdessen kommt der Kinderabzug in Ziff. 24.1 zum Zug.
> - **Kein Kinderabzug daneben:** Wer Alimente für das minderjährige Kind abzieht, erhält für dieses Kind keinen Kinderabzug.
> - **Gegenstück bei der Ex-Frau:** Sie versteuert die 24'000 in Ziff. 5.1 (Code 160) und die 12'000 in Ziff. 5.2 (Code 161). Das ist das Korrespondenzprinzip.
> - **Belege:** Nötig sind Scheidungsurteil bzw. Unterhaltsvereinbarung und Zahlungsnachweise. Ob diese mit der Steuererklärung einzureichen sind, ist im Wiki als strittig markiert (reports/entscheidungsvorlage-strittig.md Nr. 11, zh-wl-2025__c0207). Bis die Fachperson entschieden hat, empfehle ich, die Nachweise zu 13.1 und 13.2 beizulegen.
> 
> Offen ist, ob die CHF 12'000 nur die Zeit bis zur Volljährigkeit betreffen. Das ist nur relevant, wenn das Kind 2025 18 wird. Die fachliche Beurteilung bleibt bei der Fachperson.

## q37

**Frage:** TG 2025: Mandant bringt Steuerberatungsrechnung, Kreditkartenabrechnung, Mietvertrag und Motorfahrzeugversicherung. Was davon ist relevant?

**Soll (Referenz):** Steuerberatungsrechnung: nein; Motorfahrzeugversicherung: nein; Kreditkartenabrechnung: bedingt (nur als Nachweis/Schuld per 31.12.); Mietvertrag: bedingt (Wochenaufenthalt/Arbeitszimmer/Adressnachweis) – laut belege-relevanz.

**Antwort des Agenten** (41.8 s · Tools: 9 Aufrufe read, steuerwiki__ablage, steuerwiki__beleg, steuerwiki__suche):

> **TG · Steuerjahr 2025**
> 
> Von den vier Dokumenten ist keines ohne Weiteres ein Steuerbeleg. Die Kreditkartenabrechnung und der Mietvertrag sind nur unter einer Bedingung relevant. Alles stammt aus den `ablage`/`beleg`-Karten, die den Status ☑️ agent-geprüft haben (Abnahme offen).
> 
> | Dokument | Steuerrelevant? | Ablage (KATEGORIEN.md) |
> |---|---|---|
> | **Steuerberatungsrechnung** | **Nein** | Keine Steuerbeleg-Kategorie |
> | **Kreditkartenabrechnung** | **Bedingt** | Nur wenn relevant: **Belege Sonstiges** |
> | **Mietvertrag** | **Bedingt** (selbstbewohnt: nein) | Nur wenn relevant: **Belege Sonstiges** |
> | **Motorfahrzeugversicherung** | **Nein** | Keine Steuerbeleg-Kategorie |
> 
> **1. Steuerberatungsrechnung: nicht relevant**
> - Kosten für Steuerberatung und das Ausfertigen der Steuererklärung im Privatvermögen sind nicht abziehbar. Der Bund lässt sie ausdrücklich nicht als Vermögensverwaltungskosten zu (`bund-wl-2a-2025__c0057`).
> - Die Liste hat dafür keine Zeile, die Rechnung gilt deshalb nicht als Steuerbeleg. Sie gehört in die Buchhaltung bzw. Honorarabrechnung der Firma.
> - Die Dokumenterkennung ist hier unsicher (Sicherheit «tief»). Bitte die Rechnung kurz ansehen: Ist es eine Beratung für Selbständigerwerbende oder Liegenschaften, könnte das anders sein.
> - Eine TG-spezifische Fundstelle habe ich nicht gefunden. Die Aussage stützt sich nur auf die Bundesquelle.
> 
> **2. Kreditkartenabrechnung: bedingt relevant**
> - Die Abrechnung selbst ist kein Beleg. Alltagsumsätze und Kartengebühren sind nicht abziehbar.
> - Sie wird relevant in zwei Fällen:
>   - **Saldovortrag per 31.12.2025:** Der Saldo kommt als Schuld, die Sollzinsen als Schuldzinsen in **Form. 4.1 A** (Codes 455 und 286). Private Schuldzinsen sind begrenzt auf den Vermögensertrag plus Fr. 50'000 (Kanton und Bund).
>   - **Nachweisquelle:** für einzelne abziehbare Zahlungen (Spenden, Arzt-/Zahnarztkosten, Weiterbildung, Berufsauslagen), wenn die Originalrechnung fehlt. Die Originalrechnung ist vorzuziehen.
> - **Einreichen:** In den TG-Quellen 2025 nicht konkret geregelt (unklar).
> - **Ablage:** Die Liste nennt Kreditkartenabrechnungen nicht ausdrücklich. Wegen «unklar» gilt «Eingereicht?» = nein, also **Belege Sonstiges**. Die nächstliegende Listenzeile ist «Schuldzinsen (ohne Hypothek)», aber das ist eine Ähnlichkeit, keine ausdrückliche Zuordnung. Ohne Saldovortrag und ohne Nachweisfunktion nicht ablegen.
> 
> **3. Mietvertrag: bedingt relevant**
> - Der Mietzins der selbstbewohnten Wohnung ist Lebenshaltungsaufwand und nicht abziehbar (Art. 34 lit. a DBG). Dafür gibt es keine Formularposition.
> - Relevant ist er nur in folgenden Fällen:
>   - **Untervermietung:** Der Nettoertrag ist steuerbar (TG Ziff. 5.4).
>   - **Wochenaufenthalt am Arbeitsort:** Die Mehrkosten der Unterkunft sind abziehbar. Bei Wohnungen bis 3½ Zimmer gilt Jahresmietzins : (Zimmer + 1) (`tg-wl-2025__c0189`).
>   - **Mietzinsreduktion als Entgelt**, z. B. für Hauswartstätigkeit: Die Differenz ist Einkommen.
> - **Einreichen:** unklar. Dann **Belege Sonstiges**. Trifft keiner der drei Fälle zu, ist der Mietvertrag kein Steuerbeleg und wird nicht abgelegt.
> - Bitte beim Mandanten klären, ob einer der drei Fälle vorliegt.
> 
> **4. Motorfahrzeugversicherung: nicht relevant**
> - Prämien, Verkehrssteuern, Treibstoff und Unterhalt des Privatfahrzeugs sind Lebenshaltungskosten und nicht abziehbar. Das Dokument hat keinen Wert in der Steuererklärung, also keine Steuerbeleg-Kategorie.
> - Die TG-Fundstelle der Karte (`tg-wl-2025__c0123`) betrifft nur geleaste Fahrzeuge und stützt diese Aussage nicht direkt. Die Nicht-Abziehbarkeit steht in der Karte mit Bezug auf AR/SG. Für TG ist sie nicht separat belegt.
> - Gehört in die Police auch eine Lebens- oder Rentenversicherung mit Rückkaufswert, wäre die Bescheinigung per 31.12.2025 einzureichen (Ziff. 30.3, `tg-wl-2025__c0122`). Das ist bei einer reinen Fahrzeugpolice nicht der Fall.
> 
> Das Wiki liefert nur die Einordnung. Die fachliche Beurteilung bleibt bei der Fachperson.

## q38

**Frage:** AR 2026: Wie hoch ist der Kinderabzug für ein 10-jähriges Kind? Ist der Wert gesichert?

**Soll (Referenz):** AR 2026: CHF 7'400 laut Anhang 1 StG (indexiert), aber Status STRITTIG (MB 02 / StG-Text nennen andere Beträge; Wegleitung 2026 fehlt) → Fachperson.

**Antwort des Agenten** (25.2 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__zeige):

> **AR · Steuerjahr 2026: Kinderabzug für ein 10-jähriges Kind**
> 
> Das Kind ist über 4 und unter 15 Jahre alt. Es fällt daher in die Stufe Ziff. 23.2 des Formulars. Der Wert, der sich aus dem Wiki ergibt, ist **CHF 7'400** (Staats- und Gemeindesteuer).
> 
> **Der Wert ist nicht gesichert (⚠️ strittig).** Zwei Quellen widersprechen sich:
> 
> | Quelle | Betrag (4.–15. Altersjahr) |
> |---|---|
> | Anhang 1 StG (indexiert per 1.1.2024), `ar-stg-anhang-kp__c0001` | **CHF 7'400** |
> | Merkblatt MB AR 02, Ziff. 2 (gilt 2025/2026/2027), `ar-mb-02__c0002` | **CHF 7'000** |
> 
> - **Warum der Widerspruch:** Das Merkblatt nennt die nicht indexierten Gesetzestext-Beträge. Das sind 5'000, 7'000 und 11'000 statt 5'300, 7'400 und 11'600.
> - **Was für 7'400 spricht:** Anhang 1 StG ist Teil des Gesetzes. Die Wegleitung AR 2025 bestätigt für 2025 die Anhang-Werte 7'400/5'300/11'600 (`ar-wl-2025__c0005`).
> - **Was fehlt:** Formular und Wegleitung AR 2026 sind noch nicht publiziert (Stand 09.11.2026). Eine amtliche Bestätigung für 2026 gibt es im Wiki also nicht. Die Position 23.2 ist deshalb mit ⬜ offen markiert.
> 
> Ich würde mit 7'400 rechnen, den Wert aber als provisorisch kennzeichnen. Die Fachperson sollte ihn gegen die Wegleitung 2026 prüfen, sobald sie erscheint.
> 
> **Weitere Beträge für das Kind (2026):**
> - **Bund (direkte Bundessteuer):** Einheitlicher Kinderabzug von CHF 6'800, ohne Altersstaffelung (Art. 35 Abs. 1 lit. a DBG, `bund-dbg-2026__art-35`, ☑️ agent-geprüft). Zusätzlich ermässigt sich der Steuerbetrag um CHF 263 pro Kind (Art. 36 Abs. 2bis DBG, `bund-dbg-2026__art-36-t4`, ☑️).
> - **Versicherungsabzug:** Kanton Zuschlag von CHF 1'000 pro Kind (`ar-stg__art-35-t2`, ☑️). Bund Zuschlag von CHF 700 pro Kind (`bund-dbg-2026__art-33-t5`, ☑️).
> - **Vermögen:** Zusätzlicher Freibetrag von CHF 25'000 pro minderjähriges Kind mit Kinderabzug (`ar-stg__art-51`, ☑️).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q39

**Frage:** Welche Vermögenssteuer-Freibeträge (Sozialabzüge) gelten 2025 in ZH für Alleinstehende und Verheiratete?

**Soll (Referenz):** ZH kennt keine Vermögens-Sozialabzüge, sondern Tarifstufen mit 0 ‰: Grundtarif erste CHF 80'000, Verheiratetentarif erste CHF 159'000 (zh-stg-2025__par-47); kein Betrag pro Kind.

**Antwort des Agenten** (21.6 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **ZH · Steuerjahr 2025: Vermögenssteuer-Freibeträge**
> 
> In ZH gibt es beim Vermögen keinen eigentlichen Sozialabzug. Das Formular 300 hat dafür keine Zeile. Der steuerfreie Betrag ist die 0‰-Stufe des Vermögenssteuertarifs (§ 47 StG). Das Vermögen tragen Sie voll ein, der Freibetrag wirkt erst bei der Steuerberechnung.
> 
> | Tarif | Steuerfrei (0 ‰) | Fundstelle |
> |---|---|---|
> | Grundtarif (Alleinstehende) | **CHF 80'000** | zh-stg-2025__par-47-t1 |
> | Verheiratetentarif | **CHF 159'000** | zh-stg-2025__par-47-t2 |
> 
> Beide Werte haben den Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Beträge entsprechen § 47 StG in der Fassung Nachtrag 127, Stand 1.1.2025. Die VKP 2024 nennt dieselben Werte.
> 
> **Wer den Verheiratetentarif erhält:**
> - Verheiratete.
> - Verwitwete, Getrennte, Geschiedene und Ledige, die mit Kindern zusammenleben (§ 47 Abs. 2 StG).
> - Bei nicht gemeinsam besteuerten Eltern mit je ½ Kinderabzug nur, wer den Kindesunterhalt hauptsächlich trägt.
> - Massgebend sind die Verhältnisse am Ende der Steuerperiode (§ 47 Abs. 3 StG).
> 
> **Weitere Punkte:**
> - Es gibt keinen zusätzlichen Vermögensfreibetrag pro Kind.
> - **Bund:** keine Vermögenssteuer, daher auch kein Freibetrag.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## q40

**Frage:** Alleinstehende TG 2026, Nettolohn 90'000, ÖV-Abo 2'400, Säule 3a 7'258, Krankenkasse 5'500. Erstelle die Abzüge (Berufskosten, 3a, Versicherungsabzug) Kanton und Bund mit Fundstellen und Status.

**Soll (Referenz):** TG 2026 (Kanton/Bund): Fahrkosten 2'400 (Max. 6'000 / 3'300); übrige Berufskosten 3 % von 90'000 = 2'700 (Min. 2'000, Max. 4'000, beide Ebenen); Säule 3a 7'258 (TG und Bund ☑️ agent-geprüft); Versicherungsabzug TG max. 3'500 → 3'500, Bund max. 1'800 → 1'800 (Prämien 5'500 übersteigen beide Maxima).

**Antwort des Agenten** (43.0 s · Tools: 11 Aufrufe steuerwiki__formular, steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **TG · Steuerjahr 2026 · alleinstehend** (Kanton = Staats-/Gemeindesteuer, Bund = direkte Bundessteuer; beide Spalten im selben Formular)
> 
> Alle Werte haben den Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> | Ziff. (Code) | Position | Kanton | Bund | Rechnung |
> |---|---|---|---|---|
> | Form. 4.2 Ziff. 2.1 (206) → 2.5 (213) | ÖV-Abo, Fahrkosten | **2'400** | **2'400** | tatsächliche Kosten, kleiner als Plafond Kanton 6'000 / Bund 3'300 |
> | Form. 4.2 Ziff. 4 | Übrige Berufskosten (Pauschale) | **2'700** | **2'700** | 3 % × 90'000, innerhalb min. 2'000 / max. 4'000 |
> | Form. 4.2 Ziff. 7 (240) → **Ziff. 10.1** | **Berufskosten total** | **5'100** | **5'100** | 2'400 + 2'700 |
> | **Ziff. 13.1** (314) | **Säule 3a** | **7'258** | **7'258** | min(7'258; 7'258) |
> | **Ziff. 14** (330) | **Versicherungsabzug** | **3'500** | **1'800** | KK 5'500 ist höher als beide Limiten, daher gedeckelt |
> | | **Total dieser drei Abzüge** | **15'858** | **14'158** | 5'100 + 7'258 + 3'500 bzw. 1'800 |
> 
> Die Summen habe ich mit `rechne` gerechnet.
> 
> ## Fundstellen
> - **Fahrkosten:**
>   - ÖV-Abo wird mit den tatsächlichen Kosten angesetzt: `tg-wl-2026__c0177`.
>   - Plafond Kanton 6'000: `tg-wl-2026__c0176`.
>   - Plafond Bund 3'300: `bund-dbg-2026__art-26`.
> - **Übrige Berufskosten:**
>   - Kanton: `tg-bkv__par-4a`.
>   - Bund: `bund-bkv-2026__anhang-1` und `bund-rs-2-215__c0006`.
> - **Säule 3a:**
>   - Kanton: `tg-wl-2026__c0089`.
>   - Bund: `bund-bsv-masszahlen-2025-2026__c0003`.
>   - Die Zeile ist für Kanton und Bund gleich.
> - **Versicherungsabzug:**
>   - Kanton alleinstehend 3'500: `tg-stg__par-34-t3`.
>   - Bund alleinstehend 1'800: `bund-dbg-2026__art-33-t2`.
>   - Formularzeile und Limiten: `tg-wl-2026__c0209`.
> 
> ## Annahmen und offene Punkte
> - **Nettolohn:** Ich habe 90'000 als Lohnausweis Ziff. 11 genommen. Die 3-%-Pauschale und der Plafond für die übrigen Berufskosten hängen daran.
> - **Fahrkosten:** Der Abzug gilt nur, wenn im Lohnausweis Feld F nicht angekreuzt ist (kein Geschäftsfahrzeug, kein vom Arbeitgeber bezahltes GA). Sonst entfällt er.
> - **Verpflegung:** Nicht erfasst, weil in der Anfrage nichts dazu steht (Form. 4.2 Ziff. 3.1/3.2). Bei auswärtiger Verpflegung kommt Fr. 15 pro Arbeitstag, max. Fr. 3'200 pro Jahr, noch dazu, falls nicht verbilligt. Das war nur die Kurzangabe im Wiki; die Detailposition habe ich nicht geöffnet.
> - **Säule 3a:**
>   - Ich bin von einem Anschluss an die 2. Säule (PK) ausgegangen und habe das Kästchen «Anschluss 2. Säule» so angenommen. Das Maximum ist dann 7'258, die Einzahlung ist voll abzugsfähig.
>   - Die 3a-Bescheinigung ist immer einzureichen (`tg-wl-2026__c0034`).
> - **Versicherungsabzug, Bund:**
>   - Wegen der 3a-Beiträge gilt der normale Ansatz 1'800. Die Erhöhung auf 2'700 gilt nur ohne Beiträge an 2. Säule oder 3a.
>   - Der Kanton kennt keine solche Erhöhung (`wert tg 2026 versicherungsabzug`).
> - **Krankenkasse:** Als Prämie zählt die Nettoprämie nach Abzug der individuellen Prämienverbilligung (IPV), die Sie bei Form. 5.2 angeben. Ist die Prämie nach IPV tiefer, bleibt der Abzug trotzdem gedeckelt, solange Prämien plus Sparzinsen über der Limite liegen (Kanton 3'500, Bund 1'800). Weitere Versicherungsprämien (Unfall, Leben) und Sparzinsen gehen ebenfalls in Form. 5.2 und erhöhen den Betrag nicht über die Limite.
> - **Einreichen:** Für den ÖV-Abo-Beleg ist im Wiki «einreichen: unklar» (`tg-wl-2026__c0177`). Für die Krankenkassenbescheinigung ebenso (`tg-wl-2026__c0207`). Beide Belege bereithalten.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

