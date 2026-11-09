# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 40 · Lauf: 2026-11-09 18:54
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q01

**Frage:** Mandantin (ZH, 2025) bringt: Lohnausweis, Krankenkassen-Prämienrechnung, Handyrechnung, 3a-Bescheinigung, Hausratversicherungspolice, Spendenquittung Rotes Kreuz CHF 80, Kita-Rechnungen. Welche sind relevant, wofür?

**Soll (Referenz):** Relevant: Lohnausweis (Einkünfte 1.1), Krankenkassenprämien (Versicherungsabzug Ziff. 15, Form. 365), 3a-Bescheinigung (Ziff. 14), Kita-Rechnungen (Ziff. 16.6 Drittbetreuung, max. 25'000 Kanton / 25'800 Bund). Spende CHF 80: unter Mindestbetrag 100 → nicht abziehbar (sofern Total < 100). Nicht relevant: Handyrechnung (Lebenshaltung), Hausratversicherung (kein Versicherungsabzug).

**Antwort des Agenten** (43.2 s · Tools: 14 Aufrufe read, steuerwiki__ablage, steuerwiki__beleg):

> **ZH · Steuerjahr 2025**
> 
> Fünf der sieben Dokumente sind relevant, zwei nicht. Alle Wiki-Angaben sind ☑️ agent-geprüft (Abnahme offen). Die Kategorienliste ist noch nicht von consis bestätigt.
> 
> | Dokument | Relevant? | Wofür (ZH 2025) | Einreichen? | Kategorie |
> |---|---|---|---|---|
> | **Lohnausweis** | ja | Ziff. 1.1 / 1.2 (Einkünfte), Grundlage für Berufsauslagen | **ja**, immer, für jeden Arbeitgeber (zh-wl-2025__c0032) | **Belege eingereicht** |
> | **3a-Bescheinigung** | ja | Ziff. 14.1 / 14.2. Mit 2. Säule gilt max. CHF 7'258 (Kanton und Bund gleich). Massgebend ist der im Jahr 2025 einbezahlte Betrag (zh-wl-2025__c0081) | **ja**, bei Abzug | **Belege eingereicht** |
> | **Krankenkassen-Prämienrechnung** | ja | Ziff. 15 Versicherungsabzug, über Form. 365 Teil A (Code 601) | auf Verlangen. Form. 365 liegt bei, die Prämienbelege selbst nicht (zh-wl-2025__c0207) | **Belege Sonstiges** |
> | **Kita-Rechnungen** | bedingt | Ziff. 16.6 Fremdbetreuung, je Kind max. CHF 25'000 Kanton / CHF 25'800 Bund | Aufstellung mit Empfängern unaufgefordert beilegen. Rechnungen auf Verlangen (zh-zstb-34-1-bis-2025__c0023) | **Belege Sonstiges** (die Rechnungen) |
> | **Spendenquittung Rotes Kreuz CHF 80** | bedingt | Ziff. 22.2, aber nur wenn die Spenden im Jahr zusammen **mindestens CHF 100** betragen | auf Verlangen. Liste aller Zuwendungen beilegen (zh-info-spenden__c0006) | **Belege Sonstiges** |
> | **Handyrechnung** | nein | Privater Lebensunterhalt, nicht abziehbar (§ 33 lit. a StG, zh-stg-2025__par-33) | – | keine Steuerbeleg-Kategorie |
> | **Hausratversicherungspolice** | nein | Nur Prämien für Lebens-, Kranken- und Unfallversicherung sind abziehbar (§ 31 Abs. 1 lit. g StG, zh-stg-2025__par-31-t2) | – | keine Steuerbeleg-Kategorie |
> 
> **Offene Punkte für die Mandantin**
> - **Kita:**
>   - Nur Kinder unter 14, die im gleichen Haushalt leben. Die Betreuung muss mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit zusammenhängen.
>   - Verpflegung ist nicht abziehbar. Sie muss getrennt ausgewiesen sein, sonst ist der Betrag zu kürzen.
>   - Subventionen und Betreuungsgutscheine mindern die Kosten.
>   - Pro Kind braucht es die bezahlten Beträge, Name und Geburtsdatum des Kindes und den Empfänger.
> - **Spende:** CHF 80 allein ergeben keinen Abzug (Schwelle CHF 100). Gibt es weitere Spenden an steuerbefreite Organisationen mit Sitz in der Schweiz, zählt das Total (Obergrenze 20 % des Nettoeinkommens).
> - **Krankenkasse:**
>   - Eine erhaltene Prämienverbilligung (IPV) muss berücksichtigt werden, aber nicht doppelt gekürzt. Ist sie bereits in der Prämie verrechnet, die reduzierte Prämie eintragen.
>   - Der Abzug ist pauschal begrenzt (Ziff. 15, je nach Zivilstand und Kindern).
>   - Die Zusatzversicherung zählt mit.
>   - Allfällige Selbstbehalte und Arztrechnungen sind ein separates Thema (Ziff. 22.1). Dafür fehlen bisher Belege.
> - **Handy:** Wird es beruflich genutzt, ohne dass der Arbeitgeber es erstattet, kurz nachfragen. Sonst nicht erfassen.
> - **Hausrat:** Prüfen, ob die Police eine Gebäudeversicherung (Eigentümer) mit separat ausgewiesener Prämie enthält. Bei einer Mieterin ist das nicht der Fall.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q02

**Frage:** In welche Ziffer und mit welchem Code der ZH-Steuererklärung 2025 gehört der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb)?

**Soll (Referenz):** Ziff. 1.1 Haupterwerb, Code 100 (Person 1) / 101 (Person 2); Nettolohn Lohnausweis Ziff. 11 (zh-form-300-2025).

**Antwort des Agenten** (22.4 s · Tools: 2 Aufrufe steuerwiki__beleg, steuerwiki__position):

> **ZH · Steuerjahr 2025**
> 
> Der Nettolohn aus dem Lohnausweis Ziff. 11 (Person 1, Haupterwerb) gehört in die **Ziffer 1.1** (Einkünfte, unselbständige Erwerbstätigkeit, Haupterwerb) mit **Code 100**. Für Person 2 gilt Code 101.
> 
> - **Betrag:** Eingesetzt wird der Nettolohn gemäss Lohnausweis Ziff. 11. Das ist der Bruttolohn (Ziff. 8) minus AHV/IV/EO/ALV/NBUV (Ziff. 9) und minus BVG-Beiträge (Ziff. 10.1 und 10.2). Hat Person 1 mehrere Haupterwerbe, ist die Summe aller Ziff. 11 einzutragen.
> - **Bund:** Es gibt dieselbe Zeile für Staats- und Bundessteuer, und der Betrag ist in beiden Spalten gleich.
> - **Beilage:** Der Lohnausweis muss mitgeschickt werden (§ 134 Abs. 1 lit. a StG; zh-wl-2025__c0032).
> - **Einkauf in die 2. Säule:** Ein Einkauf, der laut Lohnausweis Ziff. 10.2 schon vom Lohn abgezogen wurde, steckt bereits im Nettolohn. Er darf nicht noch einmal unter Ziff. 16.1 (Code 280) abgezogen werden.
> - **Erwerbslücken:** Sie müssen ausdrücklich bezeichnet werden.
> 
> Fundstelle: zh-form-300-2025__c0004. Status: ☑️ agent-geprüft, die Abnahme ist noch offen.

## q03

**Frage:** Lohnausweis Feld F ist angekreuzt (Geschäftsauto). Was bedeutet das für den Fahrkostenabzug (SG 2025)?

**Soll (Referenz):** Feld F angekreuzt → kein Fahrkostenabzug für den Arbeitsweg mit Geschäftsfahrzeug (Privatanteil im Lohn, Lohnausweis Ziff. 2.2).

**Antwort des Agenten** (30.2 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__beleg, steuerwiki__position, steuerwiki__zeige):

> **SG · Steuerjahr 2025 – Lohnausweis Feld F angekreuzt (Geschäftsauto)**
> 
> **Kurzantwort:** Mit angekreuztem Feld F ist in der Regel **kein Fahrkostenabzug** möglich. Sie tragen also nichts in Formular 4 Ziff. 1 ein (Codes 400/404 bzw. 450/454). Das gilt für Kanton und Bund. Es gibt eine Ausnahme, die unten steht.
> 
> **Begründung**
> - Die Wegleitung SG 2025 verlangt das Kreuz in Feld F, wenn dem Arbeitnehmer keine Fahrkosten erwachsen. Genannt werden Sammeltransport und ein vom Arbeitgeber getragenes GA. Sie folgert daraus: «Ein Abzug für die Fahrt zur Arbeit ist deshalb nicht möglich.» (`sg-wl-2025__c0075`, ☑️ agent-geprüft)
> - Zum Geschäftsfahrzeug sagt das Wiki: Feld F wird auch angekreuzt, wenn der Arbeitgeber ein Geschäftsfahrzeug zur Verfügung stellt, zusammen mit dem Privatanteil.
> - Beim Geschäftsfahrzeug mit Privatanteil von 0,9 % pro Monat (10,8 % pro Jahr) gibt es keinen Fahrkostenabzug (Form. 4 Ziff. 1.3, Wiki-Zuordnung SG 2025).
> - Der Privatanteil wird im Lohnausweis als Gehaltsnebenleistung aufgeführt (Ziff. 2.2) und ist bereits im Lohn versteuert. Ein zusätzlicher Abzug würde den Arbeitsweg doppelt berücksichtigen.
> 
> **Ausnahme: effektive Abrechnung mit Bordbuch**
> Führen Sie ein Bordbuch statt der Privatanteil-Pauschale, sind die effektiven Arbeitswegkosten bis zum Maximalabzug abziehbar. Die Maximalbeträge sind:
> - Kanton **CHF 8'000**
> - Bund **CHF 3'300**
> 
> Das stützt sich auf die Wiki-Zuordnung zu Form. 4 Ziff. 1.3 («Beachten»). Ich habe dazu keine eigene Fundstelle im Wortlaut geöffnet. Ob die Voraussetzungen im konkreten Fall erfüllt sind, sollte die Fachperson prüfen.
> 
> **Was Sie prüfen sollten**
> 1. Ob der Privatanteil in Lohnausweis Ziff. 2.2 ausgewiesen ist (Pauschale 0,9 % pro Monat) oder ob stattdessen ein Bordbuch geführt wird.
> 2. Ob zusätzlich eine Fahrkostenentschädigung in Ziff. 2.3 steht. Dann dürfte Feld F nicht angekreuzt sein (StB 39 Nr. 3, `sg-stb-39-3__c0013`). Sie wäre Einkommen, und die Kosten wären bis zum Maximum abziehbar. Ein gleichzeitiges Kreuz in Feld F und ein Eintrag in Ziff. 2.3 wäre widersprüchlich. Dann sollte der Arbeitgeber den Lohnausweis korrigieren.
> 3. Ob Sie das Geschäftsauto an einzelnen Tagen nicht nutzen und dort privat zur Arbeit fahren, etwa mit dem ÖV. Das Wiki nennt dazu keine Regel, daher kann ich dazu nichts Belegtes sagen. Bitte mit der Fachperson klären.
> 
> **Limiten 2025 zur Einordnung**
> 
> | | Kanton SG | Bund |
> |---|---|---|
> | Maximalabzug Fahrkosten | CHF 8'000 | CHF 3'300 |
> | Auto, pro km (nur in begründeten Fällen) | CHF 0.70 | CHF 0.70 |
> 
> Der Ansatz von 75 Rp. pro km gilt erst ab 2026.
> 
> Alle Werte sind ☑️ agent-geprüft, die Abnahme ist noch offen. Die fachliche Beurteilung bleibt bei der Fachperson.

## q04

**Frage:** Wie hoch ist der maximale Fahrkostenabzug 2025 in TG (Staatssteuer) und beim Bund, und welcher km-Ansatz gilt für das Auto?

**Soll (Referenz):** TG 2025 Staat max. CHF 6'000 (tg-stg__par-29), Bund max. CHF 3'300 (bund-dbg-2025__art-26); Auto TG gestaffelt 0.60/0.50/0.40 je nach Jahres-km, Bund 0.70.

**Antwort des Agenten** (22.6 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **TG · Steuerjahr 2025: Fahrkostenabzug**
> 
> **Maximalbetrag**
> | | Max. pro Jahr | Fundstelle |
> |---|---|---|
> | Kanton TG (Staats- und Gemeindesteuer) | **CHF 6'000** | tg-stg__par-29 (☑️ agent-geprüft) |
> | Bund (direkte Bundessteuer) | **CHF 3'300** | bund-dbg-2025__art-26 (☑️ agent-geprüft) |
> 
> Die Grenze gilt für alle Fahrkosten zusammen, inklusive Wochenaufenthalt und Nebenerwerb. Im Formular 4.2 steht sie in Ziff. 2.5 (Code 213, bei Person 2: 253), getrennt für Staat und Bund.
> 
> **km-Ansatz für das Auto**
> Das Auto gilt nur in Ausnahmefällen, nämlich wenn der ÖV nicht zumutbar ist. Ein Beispiel ist eine Zeitersparnis von über 1 Stunde pro Arbeitstag. Im Normalfall ist nur das ÖV-Abo abziehbar.
> 
> - **TG (Staatssteuer):** Der Ansatz ist gestaffelt und wird stufenweise berechnet (tg-bkv__par-1, tg-wl-2025__c0003):
>   - bis 3'000 km: CHF 0.60/km
>   - 3'001 bis 5'000 km: CHF 0.50/km
>   - über 5'000 km: CHF 0.40/km
>   - Parkgebühren sind darin enthalten.
> - **Bund:** Der Ansatz ist einheitlich **CHF 0.70/km** (bund-bkv-2025__anhang-1).
> 
> **Weitere Regeln**
> - Bei 100 % Pensum werden in der Regel höchstens 225 Arbeitstage gerechnet (tg-wl-2025__c0003). Beim Bund gibt es keine solche Regel.
> - Beispiel TG mit 8'000 km: 3'000 × 0.60 + 2'000 × 0.50 + 3'000 × 0.40 = CHF 4'000. Das entspricht dem Rechenbeispiel in StP 29 Nr. 2.
> - Steht ein Geschäftsfahrzeug für den Arbeitsweg zur Verfügung (Lohnausweis Feld F), ist kein Fahrkostenabzug möglich.
> 
> Die Fundstellen sind agent-geprüft, die Abnahme ist noch offen. Die fachliche Beurteilung bleibt bei der Fachperson.

## q05

**Frage:** Welcher km-Ansatz für Autos gilt 2026 bei der direkten Bundessteuer?

**Soll (Referenz):** CHF 0.75 pro km (bund-mm-2025-09-11-kalte-progression-2026__c0004; RS 2-215).

**Antwort des Agenten** (22.2 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Bund (direkte Bundessteuer) · Steuerjahr 2026**
> 
> Für das Privatauto gilt **CHF 0.75 pro Fahrkilometer**. Im Vorjahr waren es CHF 0.70. ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme ist noch offen.
> 
> - **Bedingung:** Der km-Ansatz gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist.
> - **Gesamtmaximum:** Der Fahrkostenabzug ist auf CHF 3'300 pro Jahr begrenzt (Art. 26 Abs. 1 lit. a DBG, `bund-dbg-2026__art-26`). Dieser Betrag ist gleich hoch wie 2025.
> - **Künftige Anpassung:** Der Ansatz ist neu an den TCS-Kilometerpreis gekoppelt. Er kann daher künftig nach oben und nach unten angepasst werden.
> - **Zum Vergleich:** Für Motorräder mit weissem Kontrollschild gelten CHF 0.40 pro km. Für Velo, Motorfahrrad und Motorrad mit gelbem Kontrollschild gilt eine Pauschale von CHF 700 pro Jahr (`bund-rs-2-215__c0004`).
> 
> Quelle für die CHF 0.75: `bund-mm-2025-09-11-kalte-progression-2026__c0004`: «Der Abzug wird auf 75 Rappen pro Kilometer erhöht (bisher 70 Rappen).»
> 
> Ich habe keinen Kanton angenommen. Die Anzahl Arbeitstage und damit der kantonale Abzug sind kantonal geregelt. Wenn du mir den Kanton nennst (AR, SG, TG oder ZH), prüfe ich auch dessen Werte und Ansätze.

## q06

**Frage:** Maximaler Säule-3a-Abzug 2025 für eine Arbeitnehmerin mit Pensionskasse? Und für eine Selbständige ohne 2. Säule?

**Soll (Referenz):** Mit 2. Säule CHF 7'258; ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288 (bund-bsv-masszahlen-2025-2026__c0003).

**Antwort des Agenten** (26.0 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Bund · Steuerjahr 2025** (du hast keinen Kanton genannt. Die Säule-3a-Limiten kommen aus dem Bundesrecht, BVV 3, und gelten für Bund und Kantone gleich. Wenn du einen Kanton nennst, prüfe ich, ob dort etwas Abweichendes im Formular steht.)
> 
> | Situation | Maximaler 3a-Abzug 2025 | Status |
> |---|---|---|
> | Arbeitnehmerin **mit Pensionskasse** (2. Säule) | **CHF 7'258** | ☑️ agent-geprüft |
> | Selbständige **ohne 2. Säule** | **20 % des Erwerbseinkommens, höchstens CHF 36'288** | ☑️ agent-geprüft |
> 
> **Mit 2. Säule:** Der Höchstbetrag ist 8 % des oberen BVG-Grenzbetrags, also CHF 7'258.
> Quelle: `bund-bsv-masszahlen-2025-2026__c0003`.
> 
> **Ohne 2. Säule:**
> - Der Abzug beträgt 20 % des Erwerbseinkommens, begrenzt auf 40 % des oberen BVG-Grenzbetrags, also CHF 36'288.
> - Die Obergrenze erreichst du erst ab einem Erwerbseinkommen von CHF 181'440 (36'288 / 0.2). Bei tieferem Einkommen gilt der 20-%-Anteil.
> - Quellen: `bund-bvv3__art-7` (20 %) und `bund-bsv-masszahlen-2025-2026__c0003` (CHF 36'288).
> - Das Erwerbseinkommen bedeutet hier das Nettoeinkommen aus der selbständigen Tätigkeit. Welche Grösse die Fachperson im Einzelfall genau ansetzt, habe ich nicht geprüft.
> 
> **Einkauf von Lücken:** Für Steuerjahr 2025 ist ein nachträglicher Einkauf von Beitragslücken möglich, nach Art. 7a/7b BVV 3, seit 1.1.2025 in Kraft.
> - Lücken, die vor dem 1.1.2025 entstanden sind, können nicht eingekauft werden.
> - Der Einkauf kommt zusätzlich zum vollen ordentlichen Beitrag im selben Jahr.
> - Pro Jahreslücke ist nur ein Einkauf möglich.
> - Quelle: `bund-bvv3__art-7a-t1`.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## q07

**Frage:** Kinderabzug 2025 in AR für ein 10-jähriges Kind – und beim Bund?

**Soll (Referenz):** AR 2025: CHF 7'400 (4.–15. Altersjahr; Anhang 1 StG, ar-stg-anhang-kp__c0001); Bund CHF 6'800 (Art. 35 DBG) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (27.2 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **AR · Steuerjahr 2025**
> 
> Kind, 10 Jahre alt, Stichtag 31.12.2025
> 
> | | Kanton AR (Staats-/Gemeindesteuer) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | **Kinderabzug vom Einkommen** | **CHF 7'400** (Alter 4 bis 15, Formular Ziff. 23.2) | **CHF 6'800** (einheitlich, keine Altersstaffel) |
> | Quelle | ar-stg-anhang-kp__c0001, ar-wl-2025__c0005 | bund-dbg-2025__art-35 |
> | Status | ☑️ agent-geprüft | ☑️ agent-geprüft |
> 
> **Hinweise zum Kanton**
> - Der Gesetzestext nennt 7'000 (nicht indexiert). Massgebend sind 7'400 (Anhang 1 StG und Wegleitung 2025).
> - Kein Abzug, wenn die Einkünfte des Kindes über CHF 18'000 liegen oder für das Kind Unterhaltsbeiträge nach Ziff. 12.2 abgezogen werden.
> - Bei getrennt besteuerten Eltern mit gemeinsamer elterlicher Sorge und ohne Unterhaltsbeiträge erhält jeder Elternteil die Hälfte.
> 
> **Zusätzlich beim Bund**
> - Der Steuerbetrag ermässigt sich um **CHF 263** pro Kind (bund-dbg-2025__art-36-t4, ☑️). Das ist ein Abzug direkt vom berechneten Steuerbetrag und kein Abzug vom Einkommen.
> 
> **Verwandte Abzüge (nicht der Kinderabzug)**
> - Versicherungsabzug: Zuschlag pro Kind CHF 1'000 im Kanton (ar-stg__art-35-t2) und CHF 700 beim Bund (bund-dbg-2025__art-33-t5).
> - Vermögen: Freibetrag CHF 25'000 pro minderjähriges Kind mit Kinderabzug, nur im Kanton (ar-stg__art-51). Beim Bund gibt es keine Vermögenssteuer.
> 
> **Formular**
> - Das AR-Formular hat keine separate Bundesspalte. Die Steuerverwaltung nimmt die Bundesabweichungen, also auch den Kinderabzug Bund, automatisch vor (ar-wl-2025__c0179). Im Formular trägst du das Kind nur einmal ein.
> - Der Formular-Code für Ziff. 23.2 ist laut Wiki nicht verifiziert.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q08

**Frage:** Versicherungsabzug ZH 2025 für ein Ehepaar mit 2 Kindern, beide mit Pensionskasse (Staatssteuer und Bund)?

**Soll (Referenz):** ZH Staat: 5'800 + 2 × 1'300 = 8'400; Bund: 3'700 + 2 × 700 = 5'100 (zh-stg-2025__par-31-t2, bund-dbg-2025__art-33).

**Antwort des Agenten** (25.5 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **ZH · Steuerjahr 2025: Versicherungsabzug, Ehepaar mit 2 Kindern, beide mit Pensionskasse (2. Säule)**
> 
> Das ist der **Höchstbetrag**. Abziehbar ist der tiefere Betrag aus den tatsächlich bezahlten Prämien und Sparzinsen (Form. 365 Teil A) und diesem Maximum (Form. 365 Teil B).
> 
> | | Staatssteuer | Bundessteuer |
> |---|---|---|
> | Ehepaar, ungetrennte Ehe, mit Beiträgen an 2. Säule/3a | CHF 5'800 | CHF 3'700 |
> | Zuschlag je Kind (1'300 bzw. 700), 2 Kinder | CHF 2'600 | CHF 1'400 |
> | **Maximalabzug total** | **CHF 8'400** | **CHF 5'100** |
> 
> Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Fundstellen**
> - Staat: § 31 StG ZH (zh-stg-2025__par-31-t2): 5'800 für in ungetrennter Ehe Lebende, plus 1'300 je Kind.
> - Bund: Art. 33 DBG (bund-dbg-2025__art-33-t2 und art-33-t5): 3'700 für Ehepaare, plus 700 je Kind.
> 
> **Eintrag im Formular**
> - Ziff. 15 «Versicherungsprämien und Zinsen von Sparkapitalien», Code 270 (zh-form-300-2025__c0008). Es gibt zwei Spalten, Staatssteuer und Bundessteuer.
> - Der Betrag ist je Spalte min(A; B). A ist Form. 365 Teil A (Code 606), also die Summe der Codes 601 bis 604 minus die Prämienverbilligung (605). B ist Teil B (Code 616). Die Maxima stehen in Teil B bei den Codes 611 bis 615.
> 
> **Bedingungen und Hinweise**
> - Die höheren Maxima ohne Vorsorge (8'700 Staat / 5'550 Bund) gelten nur, wenn weder die steuerpflichtigen Personen noch ihre Arbeitgeber Beiträge an die 2. Säule oder Säule 3a leisteten. Hier haben beide eine Pensionskasse, also gelten die oben genannten Beträge.
> - Der Zuschlag gilt für Kinder, für die der Kinderabzug (§ 34 Abs. 1 StG) geltend gemacht werden kann. Bei geteiltem Kinderabzug (halber Abzug) beträgt der Zuschlag je Kind 650 (Staat) bzw. 350 (Bund).
> - Erhaltene individuelle Prämienverbilligung (IPV) ist abzuziehen. Sie darf nicht doppelt berücksichtigt werden: Entweder sind die Krankenkassenprämien in Code 601 schon netto erfasst, oder die IPV wird in Code 605 abgezogen.
> - Prämien, die schon im Lohnausweis abgezogen sind (NBUV), nicht nochmals erfassen.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q09

**Frage:** Wie hoch ist der Kinderdrittbetreuungsabzug 2025 im Kanton ZH, und gilt 2026 ein anderer Wert?

**Soll (Referenz):** ZH 2025 CHF 25'000 (StG Nachtrag 127, zh-stg-2025__par-31-t4); 2026 CHF 25'300 (zh-stg-2026__par-31-t3). Die VKP ab 2024 (10'400) ist überholt.

**Antwort des Agenten** (22.1 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kanton ZH · Steuerjahr 2025 und 2026**
> 
> Ja, 2026 gilt ein anderer Wert für die Staatssteuer. Der Bundeswert bleibt gleich.
> 
> | | 2025 | 2026 |
> |---|---|---|
> | **Kanton ZH (Staatssteuer)**, max. pro Kind | **CHF 25'000** | **CHF 25'300** |
> | **Bund (dBSt)**, max. pro Kind | CHF 25'800 | CHF 25'800 |
> 
> Der Abzug steht im ZH-Formular unter Ziff. 16.6 «Abzug für fremdbetreute Kinder» (Code 376).
> 
> **Voraussetzungen** (2025 und 2026 gleich):
> - Das Kind hat das 14. Altersjahr noch nicht vollendet.
> - Das Kind lebt im gleichen Haushalt.
> - Die Kosten stehen in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.
> - Die Kosten sind nachgewiesen. Abgezogen werden die tatsächlichen Kosten bis zur Höchstgrenze.
> 
> **Besonderheit 2026:** Bei Konkubinat oder alternierender Obhut mit gemeinsamer Sorge gilt je der halbe Abzug, also CHF 12'650 pro Person.
> 
> **Hinweis zur alten Zahl:** Die Verwaltungspraxis (VKP) ab 2024 nennt noch CHF 10'400. Dieser Wert ist überholt. Massgebend sind das StG in der Fassung Nachtrag 127 (Stand 1.1.2025) für 2025 und Nachtrag 132 für 2026.
> 
> **Quellen** (Status ☑️ agent-geprüft, Abnahme offen):
> - ZH 2025: `zh-stg-2025__par-31-t4`
> - ZH 2026: `zh-stg-2026__par-31-t3`
> - Bund 2025: `bund-dbg-2025__art-33-t7`
> - Bund 2026: `bund-dbg-2026__art-33-t7`
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## q10

**Frage:** Gibt es im Kanton TG einen Zweiverdienerabzug für die Staatssteuer?

**Soll (Referenz):** Nein, TG kennt keinen kantonalen Zweiverdienerabzug (nur Bund: 50 %, 8'600–14'100).

**Antwort des Agenten** (21.4 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **TG · Steuerjahr 2025** (du hast kein Jahr genannt, deshalb 2025)
> 
> **Nein.** Im Kanton Thurgau gibt es bei den Staats- und Gemeindesteuern keinen Zweiverdienerabzug. Die Wegleitung sagt: «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.» (tg-wl-2025__c0104, Status: Quelle geprüft, Abnahme offen).
> 
> **Bund (direkte Bundessteuer):** Dort gibt es den Abzug, und er steht im TG-Formular unter Ziff. 18 (Code 356), nur in der rechten Spalte (Bund) (tg-form-01-2025__c0011). Er beträgt 50 % des niedrigeren Erwerbseinkommens, mindestens Fr. 8'600 und höchstens Fr. 14'100 (bund-dbg-2025__art-33-t6, ☑️ agent-geprüft).
> 
> - **Wer ihn bekommt:** nur Ehepaare und eingetragene Partner in gemeinsamer Veranlagung, bei denen beide erwerbstätig sind.
> - **Niedrigeres Erwerbseinkommen:** Das ist die Summe der Erwerbseinkünfte nach Berufsauslagen und nach Beiträgen an Säule 2 und 3a. Liegt es unter Fr. 8'600, kann nur dieser Betrag abgezogen werden.
> - **Nicht angerechnet:** Löhne, die im vereinfachten Abrechnungsverfahren versteuert wurden.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## q11

**Frage:** SG 2025: Pauschale für übrige Berufskosten? Wie wird sie berechnet?

**Soll (Referenz):** SG 2025: CHF 700 + 10 % des Nettolohns, max. CHF 2'400 (Art. 21 StV SG, WL SG 2025).

**Antwort des Agenten** (23.7 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **SG · Steuerjahr 2025: Pauschale für übrige Berufskosten**
> 
> **Kanton (Staats- und Gemeindesteuer)**
> - Die Pauschale beträgt **Fr. 700 plus 10 % des Nettolohns, höchstens Fr. 2'400**. Ein Minimum gibt es nicht.
> - Rechnung: `min(700 + 10 % × Nettolohn; 2'400)`
> - Der Höchstbetrag ist ab einem Nettolohn von Fr. 17'000 erreicht (700 + 1'700 = 2'400).
> - Nettolohn ist der Betrag aus Ziff. 1.1 der Steuererklärung (Code 100/102). Das sind die Bruttoeinkünfte abzüglich der Beiträge an AHV/IV/EO/ALV/UV und BVG, ohne BVG-Einkäufe.
> - Bei einem Teiljahr rechnet man um.
> - Quellen:
>   - Art. 21 StV SG (sg-stv__art-21)
>   - Formular 4 Ziff. 3.1 (sg-form-4-2025__c0003)
>   - Wegleitung (sg-wl-2025__c0080)
> - Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Bund (direkte Bundessteuer)**
> - Die Pauschale beträgt **3 % des Nettolohns, mindestens Fr. 2'000 und höchstens Fr. 4'000**.
> - Rechnung: `min(max(3 % × Nettolohn; 2'000); 4'000)`
> - Quelle: bund-bkv-2025__anhang-1. Status: ☑️ agent-geprüft.
> - Im SG-Formular gibt es nur eine Spalte. Die Bundesabweichung nimmt die Steuerbehörde automatisch vor (sg-wl-2025__c0173).
> 
> **Wo im Formular**
> - Hilfsblatt Formular 4, Ziff. 3.1: Code **416** (Person 1) bzw. **466** (Person 2).
> - Das Total der Berufskosten aus Formular 4 kommt in Ziff. 10.1 (Code 438) bzw. 10.2 (Code 488).
> 
> **Beachten**
> - Die Pauschale gilt ohne Nachweis. Man kann stattdessen die tatsächlichen Kosten geltend machen (Form. 4 Ziff. 3.2, Code 418/468). Das lohnt sich nur, wenn sie die Pauschale übersteigen. Dann müssen alle übrigen Kosten belegt werden (Beiblatt).
> - Das Arbeitszimmer ist mit der Pauschale abgegolten. Es zählt nur bei der Variante mit tatsächlichen Kosten und nur unter den dort genannten Voraussetzungen, nämlich ca. 40 % der Arbeitszeit zu Hause, kein Arbeitsplatz beim Arbeitgeber und ein ausgeschiedener Raum.
> - Zahlt der Arbeitgeber nicht ereignisbezogene Pauschalspesen aus, darf man die Pauschale nicht zusätzlich abziehen.
> - Bei Bezug von ALV-Taggeldern gilt die Pauschale sinngemäss.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q12

**Frage:** Pauschalabzug Liegenschaftsunterhalt in AR für ein 8-jähriges Einfamilienhaus – und wie in ZH?

**Soll (Referenz):** AR: 10 % (Gebäude bis 10 Jahre) bzw. 20 % des Bruttoertrags, nur bis Bruttomietertrag 100'000 (Art. 25 StV AR, MB 03); ZH: einheitlich 20 % ohne Altersstaffel (ZStB 30.2).

**Antwort des Agenten** (31.3 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position):

> **AR und ZH · Steuerjahr 2025** (du hast kein Jahr genannt, deshalb 2025). Annahme: selbstbewohntes EFH, Privatvermögen, Gebäudealter 8 Jahre.
> 
> | | Kanton (Staats-/Gemeindesteuer) | Bund (dBSt) |
> |---|---|---|
> | **AR** | **10 %** (Gebäude bis 10 Jahre) | **10 %** |
> | **ZH** | **20 %** (keine Altersstaffelung) | **10 %** (Gebäude bis 10 Jahre) |
> 
> Alle Werte sind ☑️ agent-geprüft, die Abnahme ist offen.
> 
> **AR**
> - Die Pauschale beträgt 10 % bei Gebäuden bis 10 Jahre und 20 % bei älteren (ar-mb-03__c0004, ar-wl-2025__c0175).
> - Sie gilt nur, wenn der Bruttomietertrag des gesamten Liegenschaftsbesitzes höchstens CHF 100'000 beträgt und die Liegenschaft ganz oder vorwiegend Wohnzwecken dient (ar-form-07-2025__c0003).
> - Du wählst je Gebäude und Jahr zwischen Pauschale (Form. 7 C1) und effektiven Kosten (C2). Das Total kommt in Ziff. 15.
> - Das AR-Formular hat keine Bundesspalte. Der Bund wendet ebenfalls 10 % an (bund-lkv__art-5), die Steuerverwaltung nimmt das automatisch vor.
> - Das Alter wird für den Kanton per Stichtag der Vermögenssteuer bestimmt, für den Bund zu Beginn der Steuerperiode. Bei 8 Jahren bleibst du in beiden Fällen unter der 10-Jahres-Grenze.
> 
> **ZH**
> - Die Pauschale beträgt einheitlich 20 % des Brutto-Mietertrags bzw. Mietwerts. Das Alter spielt für den Kanton keine Rolle (zh-zstb-30-2__c0002, zh-form-350__c0007).
> - Beim Bund gelten 10 %, weil das Gebäude höchstens 10 Jahre alt ist (bund-lkv__art-5). Das Formular hat deshalb zwei Spalten, Staatssteuer 20 % und Bundessteuer 10 % (Form. 350, Code 5731 ff.).
> - Du wählst pro Liegenschaft und Steuerperiode zwischen Pauschale und effektiven Kosten. Mit der Pauschale sind keine weiteren Abzüge möglich, ausser Baurechtszinsen. Bei vorwiegend geschäftlicher Nutzung gibt es keine Pauschale.
> - Der Betrag wird im Form. 350 mit dem Eigenmietwert verrechnet. Nur der Nettobetrag kommt in Ziff. 6 (Code 188). Ein separater Abzug in Ziff. 16 wäre ein Doppelabzug.
> 
> **Fazit:** Bei gleichem Eigenmietwert ist die Pauschale in ZH für den Kanton doppelt so hoch wie in AR. Beim Bund sind es in beiden Kantonen 10 %. Bei einem neuen Gebäude lohnt sich ein Vergleich mit den effektiven Kosten selten. Gerade bei Energiespar- oder Rückbaukosten kann die Wahl der effektiven Kosten trotzdem sinnvoll sein, weil diese nur dann abziehbar sind (ZH: Form. 350 / Ziff. 16).
> 
> **Nicht geprüft:** die Berechnungsbasis (Eigenmietwert) in beiden Kantonen im Detail. In AR gilt der Eigenmietwert nach 20 % Selbstnutzungsabzug (ar-wl-2025__c0001), in ZH der Wert nach Weisung 2009. Die Pauschale wird auf dieser Basis berechnet.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q13

**Frage:** TG: Welcher Einschlag gilt auf dem Eigenmietwert der selbstbewohnten Liegenschaft am Wohnsitz (Kanton vs. Bund)?

**Soll (Referenz):** TG: Abzug 40 % Kanton, 20 % Bund für dauernd selbstbewohntes Eigentum am Wohnsitz (tg-stg__par-23; WL TG 2025).

**Antwort des Agenten** (24.9 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **TG · Steuerjahr 2025** (kein Jahr genannt, daher 2025)
> 
> Auf dem Eigenmietwert einer am Wohnsitz dauernd selbstbewohnten Liegenschaft gilt in Thurgau ein Selbstnutzungsabzug. Er beträgt:
> 
> | | Abzug auf dem Mietwert | Steuerbar bleiben |
> |---|---|---|
> | **Kanton** (Staats- und Gemeindesteuer) | **40 %** | 60 % |
> | **Bund** (direkte Bundessteuer) | **20 %** | 80 % |
> 
> - **Kanton:** 40 % ist der Abzug nach § 23 StG TG. Quelle: tg-stg__par-23 «von dem gemäss Abs. 2 festgelegten Mietwert ein Abzug von 40 Prozent vorgenommen». Status ☑️ agent-geprüft, Abnahme offen.
> - **Bund:** 20 % steht in der Wegleitung TG 2025. Quelle: tg-wl-2025__c0225 «nutzung kantonal einen Abzug von 40% und beim Bund von 20% vornehmen». Status ☑️ agent-geprüft, Abnahme offen.
> - Das DBG kennt keinen eigenen festen Prozentsatz. Der Bundesabzug wird im kantonalen Verfahren angewendet, im Thurgau also mit 20 %. Die Bundesspalte weicht deshalb von der Kantonsspalte ab.
> 
> **Praktisch im Formular:**
> - Ziff. 8.1 (Formular 7, Code 180) wird für Staat und Bund getrennt gerechnet.
> - Rechnung je Spalte: Mietwert selbstgenutzt (indexiert, aus der Liegenschaftensteuerrechnung/Schätzung) × (1 − 40 % bzw. 20 %).
> - Davon geht der Unterhalt ab, entweder effektiv (Formular 8) oder pauschal. Die Pauschale beträgt 10 % bei Gebäuden bis 10 Jahre und 20 % bei älteren Gebäuden. Sie gilt für Kanton und Bund gleich und wird vom steuerbaren Eigenmietwert berechnet.
> 
> **Der Abzug gilt nicht für:**
> - Zweit- und Ferienwohnungen,
> - landwirtschaftlich geschätzte Liegenschaften,
> - Objekte, die an Nahestehende überlassen sind.
> 
> In diesen Fällen sind 100 % des Mietwerts steuerbar. Beim Formular-7-Feld «Am Wohnsitz selbstgenutzt» ist bei einer Zweitwohnung das Häkchen leer zu lassen.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der zuständigen Fachperson.

## q14

**Frage:** Bis wann kann ein Treuhänder im Kanton TG für seine Mandanten Fristerstreckung erhalten?

**Soll (Referenz):** Gewerbsmässige Treuhänder für Mandanten bis 31.12. des Deklarationsjahres (StP 155 Nr. 2).

**Antwort des Agenten** (26.0 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **TG · Steuerjahr 2025** (kein Jahr genannt, daher 2025; Kanton Thurgau, Staats- und Gemeindesteuer)
> 
> **Gewerbsmässige Treuhänder und Steuerberater können für ihre Mandanten Fristerstreckung bis längstens 31. Dezember des Deklarationsjahres beantragen.** Das Deklarationsjahr ist das Jahr der Einreichung. Für das Steuerjahr 2025 ist es also der **31. Dezember 2026**.
> Quelle: StP 155 Nr. 2, Chunk `tg-stp-155-2__c0002` (☑️ agent-geprüft, Abnahme offen).
> 
> Zum Vergleich und für die Praxis:
> - **Private ohne Vertretung:** Das erste Gesuch wird grundsätzlich bis 30. September bewilligt, weitere in begründeten Fällen bis 30. November (`tg-stp-155-2__c0001`). Darüber hinaus gibt es eine Erstreckung nur bei ausserordentlichen Gründen. Diese müssen mit einer substanziierten Sachdarstellung glaubhaft gemacht werden. Starke berufliche Belastung des Vertreters oder fehlende Unterlagen genügen nicht (`tg-stp-155-2__c0002`).
> - **Gesuch:** Es geht schriftlich, begründet und rechtzeitig an das Gemeindesteueramt (`tg-stp-155-2__c0001`).
> - **Gebühr:** Nach § 39b StV TG (`tg-stv__par-39b`) ist die erste Erstreckung gebührenfrei. Jedes weitere Gesuch kostet Fr. 30 Kanzleigebühr. Das Wiki-Eckwert-Blatt hält zugleich fest, dass die Gebühr für natürliche Personen in den Quellen nicht ausdrücklich genannt sei. Der Wortlaut von § 39b Abs. 3 unterscheidet aber nicht nach Personenart. Das ist ein Widerspruch zwischen Wiki-Hinweis und Verordnungstext, und ich habe ihn nicht abschliessend geklärt.
> - **Bund:** Die direkte Bundessteuer regelt die Fristerstreckung nicht gesondert. Sie läuft über die kantonale Steuererklärung und die kantonale Regelung.
> 
> Ob die Frist im Einzelfall gewährt wird und wie die Eingabe sauber begründet wird, beurteilt die zuständige Fachperson beim Gemeindesteueramt. Das Gesuch ist rechtzeitig vor Ablauf der laufenden Frist zu stellen.

## q15

**Frage:** ZH: Bis wann ist die Steuererklärung 2025 einzureichen und wie lange wird höchstens Fristerstreckung gewährt?

**Soll (Referenz):** Einreichung bis 31.03.2026; Fristerstreckung längstens bis 30. November (ZStB 132.1 / WL ZH 2025).

**Antwort des Agenten** (25.0 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **ZH · Steuerjahr 2025**
> 
> **Einreichefrist:** Die Steuererklärung 2025 ist bis **31. März 2026** einzureichen, online oder über das Scan-Center. (☑️ agent-geprüft, zh-wl-2025__c0017; ZStB 132.1, zh-zstb-132-1__c0022)
> 
> **Maximale Fristerstreckung:** Rechtzeitig gestellten Gesuchen ist längstens bis **30. November 2026** zu entsprechen, also bis zum 30. November des Folgejahres der Steuerperiode. (☑️ agent-geprüft, zh-zstb-132-1__c0024)
> 
> - **Gesuch rechtzeitig stellen:** Das Gesuch muss vor Fristablauf beim Gemeindesteueramt eingehen. Nach Ablauf der ordentlichen oder erstreckten Frist wird es abgewiesen. Dann ist nur noch eine Wiederherstellung der Frist nach § 15 StV bzw. Art. 119 Abs. 2 DBG möglich (c0024).
> - **Über den 30. November hinaus:** Solche Gesuche werden abgewiesen, ausser es werden ausserordentliche Gründe glaubhaft gemacht. Dafür braucht es in der Regel eine substanziierte Sachdarstellung. Starke berufliche Auslastung der Vertretung oder fehlende Unterlagen genügen nicht (zh-zstb-132-1__c0025).
> - **Erstes Gesuch:** Es gilt ohne gegenteiligen Entscheid als stillschweigend bewilligt (Wiki-Eintrag `verfahren.fristerstreckung`). Den Wortlaut dazu habe ich nicht im Chunk geöffnet.
> - **Bund:** Die direkte Bundessteuer hat keine eigene Frist. Einreichung und Erstreckung richten sich nach der kantonalen Regelung (Art. 119 DBG).
> - **Nicht geprüft:** Kosten einer Fristerstreckung sind in den Quellen nicht genannt.
> 
> **Zu Ihrem Stichtag (heute 9.11.2026):** Der 30. November 2026 ist der letzte mögliche Termin. Ein Gesuch um Erstreckung darüber hinaus wäre nur mit ausserordentlichen Gründen aussichtsreich. Wurde bis heute weder eingereicht noch erstreckt, ist die ordentliche Frist bereits abgelaufen. Dann kann nur noch eine Wiederherstellung beantragt werden, oder es folgt das Mahnverfahren (ZStB 132.1, IV; zh-zstb-132-1__c0029).
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## q16

**Frage:** AR: Was kostet die zweite Fristverlängerung?

**Soll (Referenz):** CHF 25 (erste Verlängerung kostenlos, jede weitere CHF 25; MB 18 / WL AR 2025).

**Antwort des Agenten** (21.0 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **AR · Steuerjahr 2025** (kein Jahr angegeben, daher 2025)
> 
> Die zweite Fristverlängerung kostet **CHF 25**. Nur die erste Fristverlängerung ist gebührenfrei. Jede weitere kostet CHF 25.
> 
> - Das Gesuch muss vor Ablauf der Einreichefrist bei der Kantonalen Steuerverwaltung eingehen. Online geht das über esteuern.ar.ch.
> - Quellen:
>   - Wert `verfahren.fristerstreckung`: ar-wl-2025__c0012 («nur die erste Fristverlängerung kostenlos ist»), Status ☑️ agent-geprüft (Abnahme offen).
>   - Art. 59a StV AR (ar-stv__art-59a): «Die erstmalige Fristerstreckung ist kostenlos.»
>   - Merkblatt 18 (ar-mb-18__c0001, Gebührenansätze ab 1.9.2025): «Fristverlängerungen (im Wiederholungsfall): Fr. 25».
> - **Bund:** Die direkte Bundessteuer regelt die Fristerstreckung nicht gesondert. Sie ist kantonal geregelt, und die Gebühr fällt nur nach kantonalem Recht an.
> - **Nicht geprüft:** Die Quelle ar-wl-2025__c0012 belegt Treuhänder-Sammelgesuche nicht. Dazu mache ich keine Aussage.
> - Den Wortlaut von Art. 59a StV AR habe ich nur im Suchausschnitt gesehen und nicht als ganzen Chunk geöffnet.

## q17

**Frage:** Krankheitskosten SG 2025: Ab welchem Selbstbehalt sind sie abziehbar – und beim Bund?

**Soll (Referenz):** SG: Selbstbehalt 2 % (Art. 46 StG SG); Bund: 5 % (Art. 33 Abs. 1 lit. h DBG, KS 11).

**Antwort des Agenten** (26.1 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__zeige):

> **SG · Steuerjahr 2025: Krankheits- und Unfallkosten**
> 
> **Kanton SG (Staats- und Gemeindesteuer): Selbstbehalt 2 %**
> - Abziehbar ist, was 2 % der Nettoeinkünfte (Nettoeinkommen, Ziff. 20 im Formular) übersteigt. Es zählen nur die selbst getragenen Kosten, also nach Abzug von Beiträgen Dritter wie Krankenkasse oder Hilflosenentschädigung.
> - Formular SG 2025: Ziff. 21.1. Die Vorkolonne (Code 650) enthält die Summe der selbst getragenen Kosten, der Selbstbehalt steht unter Code 238 und der Abzug unter Code 240.
> - Rechnung: Abzug = max(0; Vorkolonne − 2 % × Ziff. 20).
> - Fundstellen: sg-stg-2025__art-46, sg-form-1-2025__c0010, sg-wl-2025__c0098. Status ☑️ agent-geprüft.
> 
> **Bund (direkte Bundessteuer): Selbstbehalt 5 %**
> - Abziehbar sind die Kosten, soweit sie 5 % der um die Aufwendungen nach Art. 26–33 DBG verminderten steuerbaren Einkünfte übersteigen (Art. 33 Abs. 1 lit. h DBG).
> - Im SG-Formular gibt es dafür keine eigene Spalte. Die Steuerbehörde nimmt die Abweichung für den Bund automatisch vor (sg-wl-2025__c0173).
> - Fundstelle: bund-dbg-2025__art-33-t3, im Wortlaut geprüft. Status ☑️ agent-geprüft.
> 
> **Ergänzungen**
> - Behinderungsbedingte Kosten gelten ohne Selbstbehalt. Beim Kanton gehören sie in Ziff. 21.2, beim Bund unter Art. 33 Abs. 1 lit. hbis DBG.
> - Die Diät-Pauschale (z. B. bei Zöliakie, nicht bei Diabetes) beträgt Fr. 2'500 und wird beim Kanton in der Vorkolonne mitgerechnet. Beim erstmaligen Geltendmachen braucht es eine ärztliche Bescheinigung.
> - Krankenkassenprämien gehören nicht hierher, sondern in Ziff. 14.
> - Die Belege sind im Formular 6 aufzuführen und auf Verlangen einzureichen. Wenn dort auf einen Krankenkassenauszug verwiesen wird, muss die detaillierte Leistungsübersicht beiliegen.
> 
> **Nicht geprüft:** Die Selbstbehalt-Basis beim Bund (Einkünfte nach Art. 26–33 DBG) weicht im Wortlaut von «Nettoeinkommen Ziff. 20» ab. Bei einem konkreten Fall habe ich den Bundesbetrag nicht gerechnet. Die fachliche Beurteilung bleibt bei der Fachperson.

## q18

**Frage:** PK-Einkauf CHF 20'000 wurde über den Lohn abgezogen (Lohnausweis Ziff. 10.2). Darf er nochmals in der Steuererklärung abgezogen werden?

**Soll (Referenz):** Nein – BVG-Einkauf über Lohnabzug (Lohnausweis Ziff. 10.2) ist bereits im Nettolohn berücksichtigt; nur direkt bezahlte Einkäufe separat abziehen.

**Antwort des Agenten** (51.0 s · Tools: 11 Aufrufe steuerwiki__beleg, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__position):

> **Nein, nicht nochmals abziehen.** Der Abzug ist schon erfolgt. Das gilt in allen vier Kantonen des Wikis (ZH, SG, TG, AR) und beim Bund. Ein zweiter Abzug wäre ein Doppelabzug. Der Kanton fehlt in Ihrer Frage, deshalb nenne ich unten alle vier Formularstellen. Ich verwende Steuerjahr 2025, weil keines genannt ist.
> 
> **Begründung**
> - Ziff. 10.2 des Lohnausweises weist Einkaufsbeiträge aus, die der Arbeitgeber vom Lohn abgezogen hat. Der Nettolohn in Ziff. 11 ist Bruttolohn (Ziff. 8) minus Ziff. 9 und 10. Dieser Nettolohn kommt in die Steuererklärung (`bund-wl-lohnausweis-2026__c0036`, `__c0038`).
> - Die CHF 20'000 sind also im Nettolohn schon abgezogen, für Kanton und Bund.
> - In der Steuererklärung abziehen können Sie nur Einkäufe, die Sie selbst direkt an die Pensionskasse überwiesen haben. Dafür gibt es die Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP). Das sagt Rz 46 der Wegleitung (`bund-wl-lohnausweis-2026__c0037`).
> 
> **Wo der Abzug im Formular steht, falls zusätzlich selbst bezahlte Einkäufe vorliegen**
> 
> | Kanton | Position | Hinweis |
> |---|---|---|
> | ZH | Ziff. 16.1, Code 280 | Ziff. 10.2 ist bereits im Nettolohn und darf nicht nochmals in Ziff. 16.1 stehen. |
> | SG | Ziff. 13.2, Code 218 (Person 1) / 219 (Person 2) | Einkauf über den Lohnausweis abgerechnet: nicht doppelt abziehen. Bescheinigung und Einkaufsberechnung beilegen. |
> | TG | Ziff. 15.2, Code 343 / 344 | Ziff. 10.1 und 10.2 dienen nur zur Kontrolle. Sie sind bereits in Ziff. 1 der Steuererklärung berücksichtigt. |
> | AR | Ziff. 13.2 | Ziff. 10.2 nicht doppelt eintragen. Der Code ist nicht verifiziert (siehe unten). |
> 
> Status aller vier Positionen: ☑️ agent-geprüft, Abnahme offen.
> 
> **Vorbehalte**
> - Die Lohnausweis-Wegleitung liegt im Wiki nur in der Fassung 2026 vor, nicht für 2025. Die Regel zu Ziff. 10.2 und 11 ist inhaltlich dieselbe, geprüft habe ich sie für 2025 aber nicht.
> - AR ist als ⚠️ strittig markiert: Die Wegleitung nennt neben Ziff. 13.2 teilweise auch Ziff. 16.6. Am Ergebnis ändert das nichts, die Beiträge dürfen nur einmal abgezogen werden.
> - Unabhängig vom Doppelabzug gilt für alle Einkäufe: Wird innert drei Jahren Kapital bezogen, ist der Einkauf nicht abziehbar. Das steht bei ZH, SG und AR (Sperrfrist).
> - Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Nennen Sie mir den Wohnkanton am 31.12., dann gebe ich die Angaben für diesen Kanton genau an. Das gilt auch für weitere Einkäufe, die Sie direkt bezahlt haben.

## q19

**Frage:** Weiterbildungskosten CHF 15'000 (ZH, 2025), Arbeitgeber hat nichts bezahlt. Wie viel ist abziehbar (Kanton/Bund)?

**Soll (Referenz):** ZH Staat max. CHF 12'400 (zh-stg-2025__par-31-t4); Bund max. CHF 13'000 (bund-dbg-2025__art-33-t4).

**Antwort des Agenten** (24.4 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **ZH · Steuerjahr 2025: Weiterbildungskosten CHF 15'000, selbst getragen**
> 
> | | Abziehbar | Nicht abziehbar | Limite |
> |---|---|---|---|
> | **Kanton (Staatssteuer)** | **CHF 12'400** | CHF 2'600 | CHF 12'400 (☑️, zh-stg-2025__par-31-t4) |
> | **Bund (direkte Bundessteuer)** | **CHF 13'000** | CHF 2'000 | CHF 13'000 (☑️, bund-dbg-2025__art-33-t4) |
> 
> **Rechnung:** Selbst getragene Kosten = 15'000 − 0 (Arbeitgeberbeitrag) = 15'000. Der Abzug ist der kleinere Wert aus den selbst getragenen Kosten und der Limite.
> 
> **Formular:** Ziff. 16.2, Code 292. Dort steht in der Spalte Staatssteuer 12'400 und in der Spalte Bundessteuer 13'000. Das Hilfsblatt Form. 367 ist beizulegen. Dort gehören hin:
> - Total der Kosten: 15'000 (Code 2900)
> - Beitrag Arbeitgeber/Dritte: 0 (Code 2901)
> - Selbst getragen: 15'000 (Code 2902)
> - Zulässiger Abzug: 12'400 im Block Staatssteuer, 13'000 im Block Bundessteuer (Code 2920)
> 
> **Voraussetzungen:**
> - Die Limite gilt je Person. Bei Ehepaaren hat jede Person ihr eigenes Maximum.
> - Es braucht einen Abschluss auf Sekundarstufe II oder das vollendete 20. Altersjahr. Eine Ausbildung bis zum ersten Sek.-II-Abschluss ist nicht abziehbar.
> - Die Weiterbildung muss berufsorientiert sein. Das schliesst Umschulung ein.
> - Massgebend ist das Jahr der Zahlung oder Fälligkeit, nicht der Kursbesuch. Die 15'000 müssen also 2025 bezahlt oder fällig geworden sein.
> - Belege (Rechnungen und Zahlungsnachweise) werden auf Verlangen eingereicht. Das Form. 367 ist der Steuererklärung beizulegen.
> - Dass der Arbeitgeber nichts bezahlt hat, sollte zum Lohnausweis passen: Ziff. 13.3 muss leer sein.
> 
> Alle Werte haben den Status ☑️ agent-geprüft, das heisst Fundstelle geprüft, Abnahme offen. Die fachliche Beurteilung bleibt bei der Fachperson.

## q20

**Frage:** Spenden CHF 50 an eine gemeinnützige Organisation (TG 2025) – abziehbar?

**Soll (Referenz):** Nein – TG: Zuwendungen nur abziehbar, wenn sie CHF 200 übersteigen (StG TG § 34 Abs. 1 Ziff. 11); Bund: ab CHF 100.

**Antwort des Agenten** (25.1 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **TG · Steuerjahr 2025**
> 
> **Nein, die CHF 50 sind bei der Staats- und Gemeindesteuer wie auch bei der direkten Bundessteuer nicht abziehbar.**
> 
> **Kanton TG (Staats- und Gemeindesteuer)**
> - Freiwillige Zuwendungen sind nur abziehbar, soweit sie gesamthaft CHF 200 übersteigen (Selbstbehalt).
> - Berechnung: max(50 − 200; 0) = **CHF 0**.
> - Quelle: tg-stg__par-34-t4 «soweit sie gesamthaft Fr. 200 übersteigen» · Status ☑️ agent-geprüft.
> 
> **Bund (direkte Bundessteuer)**
> - Der Abzug gilt erst, wenn die Zuwendungen im Steuerjahr CHF 100 erreichen. CHF 50 liegen darunter, also **CHF 0**.
> - Quelle: bund-dbg-2025__art-33a «wenn diese Leistungen im Steuerjahr 100 Franken erreichen» · Status ☑️ agent-geprüft.
> 
> **Wichtig: Die Schwellen gelten für die Summe aller Spenden des Jahres.**
> - Hat die Person im Jahr 2025 noch weitere abziehbare Spenden, werden diese zusammengerechnet.
> - Beispiel: Bei total CHF 500 wären kantonal CHF 300 abziehbar (500 − 200), beim Bund CHF 500. Beides gilt innerhalb der Maximalgrenzen von 20 % des Nettoeinkommens.
> - Die CHF 50 sind dann Teil der Gesamtsumme.
> 
> **Formular**
> - Erfasst werden die Spenden in Formular 6, Spalte «gemeinnützige oder öffentliche Zwecke». Dort sind sie einzeln mit Name und Sitz der Institution aufzuführen. Das Ergebnis kommt in Ziff. 23.2 (Code 366).
> - Quittungen sind nur ab CHF 1'000 pro Zuwendung beizulegen, darunter nur auf Verlangen.
> 
> **Voraussetzung für die Abzugsfähigkeit**
> - Die Organisation muss steuerbefreit sein und ihren Sitz in der Schweiz haben, oder es muss sich um ein Gemeinwesen handeln.
> - Religiöse, kulturelle und sportliche Zwecke sind nicht abziehbar. Das gilt auch für Organisationen mit Sitz im Ausland.
> - Ob die konkrete Organisation steuerbefreit ist, lässt sich in der Liste der Steuerverwaltung TG prüfen. Das habe ich nicht geprüft.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q21

**Frage:** Was ändert sich 2026 bei der Säule 3a (Einkauf) und wo wird das im ZH-Formular 2026 eingetragen?

**Soll (Referenz):** Ab 2026 Einkauf (Nachzahlung) Säule 3a für Beitragslücken ab 2025 (max. 7'258 pro Einkaufsjahr, BVV 3 Art. 7a, KS 18a); ZH-Formular 2026: Ziff. 14.3 (Code 264, Detailfelder 276/278).

**Antwort des Agenten** (24.4 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **ZH · Steuerjahr 2026**
> 
> ## Was sich ändert
> Ab der Steuerperiode 2026 können Sie zusätzlich zu den ordentlichen 3a-Beiträgen **Beitragslücken nachträglich einkaufen** (☑️ agent-geprüft, Abnahme offen; zh-wl-2026-uj__c0077).
> 
> - **Lücken:** Es zählen nur Lücken, die ab 1.1.2025 entstanden sind, innerhalb der zehn Jahre vor dem Einkauf. Für 2026 ist faktisch nur die Lücke 2025 einkaufbar.
> - **Voraussetzungen:**
>   - In den Lückenjahren wurden AHV/IV/EO-Beiträge geleistet.
>   - Im Einkaufsjahr wurde der ordentliche Maximalbeitrag voll einbezahlt. Das sind CHF 7'258 mit 2. Säule bzw. 20 % des Erwerbseinkommens, max. CHF 36'288, ohne 2. Säule.
> - **Limite Einkauf:** höchstens die Summe der Lücken, in jedem Fall maximal **CHF 7'258**. Das gilt für Kanton und Bund (Bund: bund-wl-2a-2026__c0051).
> - **Ordentliche Beiträge:** Die Maxima bleiben bei CHF 7'258 und CHF 36'288 (Bund gleich; bund-bsv-masszahlen-2025-2026__c0003).
> 
> ## Wo im ZH-Formular 2026
> Der Einkauf steht in **Ziff. 14.3 «Einkauf Säule 3a (neu ab 2026)»** (zh-form-300-2026-uj__c0008):
> - **Person 1:** Code **276**
> - **Person 2:** Code **278**
> - **Summe:** Hauptkolonne Code **264**
> 
> Das Formular hat die Spalten Staatssteuer und Bundessteuer. Der Betrag gilt für beide gleich.
> 
> Die ordentlichen Beiträge gehören separat in **Ziff. 14.1 / 14.2** (Code 260 bzw. 261). Der Einkauf darf nicht dort stehen.
> 
> **Rechnen je Person:** min(Einkauf; Summe der Lücken ab 1.1.2025 innert 10 Jahren; 7'258)
> 
> **Belege:**
> - Einkaufsbescheinigung der 3a-Einrichtung
> - 3a-Bescheinigung für den ordentlichen Beitrag, als Nachweis des vollen Maximalbeitrags im Einkaufsjahr
> - Nachweis der AHV/IV/EO-Beiträge im Lückenjahr
> 
> ## Vorbehalte
> - Das reguläre ZH-Formular und die Wegleitung 2026 sind per 09.11.2026 noch nicht publiziert. Die Ziffern und Codes stützen sich auf die Fassung für unterjährige Steuerpflicht. **Bitte am regulären Formular prüfen.**
> - Die Rechtsgrundlage (Artikel BVV 3) ist nur aus der Wegleitung belegt, nicht aus einem geprüften Gesetzeschunk.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (34.6 s · Tools: 6 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__position):

> **Steuerjahr 2025.** Du hast keinen Kanton genannt. Das Verfahren ist bundesrechtlich einheitlich. Die Formularstelle hängt aber vom Wohnsitzkanton am 31.12. ab. Deshalb nenne ich sie für alle vier abgedeckten Kantone (ZH, SG, TG, AR). Alle Positionen sind ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen.
> 
> ## Wie wird zurückgefordert?
> Natürliche Personen mit Wohnsitz in der Schweiz stellen keinen separaten Antrag. Sie deklarieren die Dividende in der kantonalen Steuererklärung und fordern die Verrechnungssteuer dort zurück.
> 
> 1. Die Dividende wird mit dem **Bruttoertrag** im Wertschriftenverzeichnis aufgeführt. Erträge mit abgezogener Verrechnungssteuer stehen in **Kolonne A**, Erträge ohne Abzug in Kolonne B. Der Steuerauszug der Bank dient als Beleg.
> 2. Der Anspruch beträgt **35 % von Total A**.
> 3. Der Betrag wird mit der Steuerrechnung verrechnet oder ausbezahlt. Dafür muss die Bankverbindung (IBAN) angegeben sein.
> 4. Das Wertschriftenverzeichnis muss unterschrieben werden.
> 
> **Wichtige Voraussetzungen**
> - Der Ertrag muss **vollständig deklariert** sein. Bei nicht deklarierten Erträgen verwirkt der Anspruch. In SG gilt eine Ausnahme: Er besteht weiter, wenn die Nichtdeklaration fahrlässig war und die Erträge nachträglich angegeben werden.
> - Der Anspruch erlischt, wenn er nicht **innert drei Jahren nach Ablauf des Fälligkeitsjahres** geltend gemacht wird. Das gilt laut Quellen für ZH und AR. In SG verwirkt der Anspruch für Fälligkeiten 2025 ohne Antrag bis Ende 2028. Fristerstreckung hemmt die Frist nicht.
> - Die Auszahlung erfolgt nur durch den Kanton, in dem du am **31.12. wohnst**. TG zahlt zudem unter Vorbehalt des Rückforderungsrechts der ESTV.
> - Kollektiv- und Kommanditgesellschaften sowie Erneuerungsfonds von Stockwerkeigentümergemeinschaften stellen **Formular 25 direkt an die ESTV**.
> 
> ## Wo wird der Anspruch ausgewiesen?
> 
> | Kanton | Stelle im Formular | Fundstelle |
> |---|---|---|
> | **ZH** | Form. 340 (Hilfsblatt Wertschriftenverzeichnis), Totale, **Code 540**: 35 % × Total Bruttoertrag A, auf 5 Rappen gerundet. Total A+B gehen in Ziff. 4.1 des Hauptformulars. | zh-form-340-2025__c0005 |
> | **SG** | Form. 2, **Code 999**: 35 % von Total A | sg-form-2-2025__c0006 |
> | **TG** | Form. 2, **Ziff. 10**: 35 % von Total A, Übertrag aus Ziff. 3, Zwischentotal I, Spalte 8 | tg-form-02-2025__c0006 |
> | **AR** | Form. 2, **Code 999**: 35 % von Total A | ar-form-02-2025__c0007 |
> 
> Eine eigene Bundesspalte gibt es für die Verrechnungssteuer nicht. Die Rückerstattung ist Bundesrecht und läuft über die kantonale Steuererklärung.
> 
> ## Ausländische Titel
> Bei ausländischen Dividenden gilt etwas anderes. Eine ausländische Quellensteuer wird über Formular **DA-1** angerechnet, nicht als Verrechnungssteuer. Das Total wird ins Wertschriftenverzeichnis übertragen (ZH: Zeile «Übertrag ab Formular DA-1», Code 2370/2371).
> 
> ## Nicht geprüft
> Die Rückerstattungsvoraussetzungen im Bundesgesetz (VStG) habe ich hier nicht einzeln aufgerufen, zum Beispiel den Nachweis der Berechtigung am Ertrag. Die Angaben stützen sich auf die kantonalen Wegleitungen. Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Nenn mir deinen Wohnsitzkanton, falls du den Fall mit Beträgen durchrechnen willst.

## q23

**Frage:** Vergleiche den Versicherungsabzug 2025 für Alleinstehende ohne Kinder in AR, SG, TG, ZH und beim Bund.

**Soll (Referenz):** Alleinstehend ohne Kinder 2025 (mit 2. Säule/3a): AR 2'700 · SG 3'400 · TG 3'500 · ZH 2'900 · Bund 1'800.

**Antwort des Agenten** (26.4 s · Tools: 1 Aufrufe steuerwiki__vergleich):

> **Versicherungsabzug 2025, alleinstehend ohne Kinder** (Kanton = Staats-/Gemeindesteuer, Bund = direkte Bundessteuer)
> 
> | Rang | Jurisdiktion | Abzug mit Vorsorgebeiträgen (2. und 3. Säule) | Abzug ohne Vorsorgebeiträge | Fundstelle (Chunk-ID) |
> |---|---|---|---|---|
> | 1 | **TG** | CHF 3'500 ☑️ | nicht anwendbar | tg-stg__par-34-t3 |
> | 2 | **SG** | CHF 3'400 ☑️ | CHF 3'900 ☑️ | sg-stg-2025__art-45-t2 |
> | 3 | **ZH** | CHF 2'900 ☑️ | CHF 4'350 ☑️ | zh-stg-2025__par-31-t2, zh-wl-2025__c0084 |
> | 4 | **AR** | CHF 2'700 ☑️ | nicht anwendbar | ar-stg__art-35-t2 |
> | 5 | **Bund** | CHF 1'800 ☑️ | CHF 2'700 ☑️ | bund-dbg-2025__art-33-t2, bund-rs-2-210__c0006 |
> 
> - **Höchster Abzug:** Im Normalfall (Spalte «mit Vorsorgebeiträgen») hat TG mit CHF 3'500 den höchsten Abzug. Danach folgen SG mit CHF 3'400 und ZH mit CHF 2'900.
> - **Tiefste Abzüge:** AR liegt mit CHF 2'700 am tiefsten bei den Kantonen. Der Bund ist mit CHF 1'800 deutlich tiefer als alle Kantone.
> - **Ohne Vorsorgebeiträge:** Bei ZH, SG und beim Bund gibt es einen höheren Ansatz, wenn keine Beiträge an die 2. oder 3. Säule geleistet werden. ZH liegt dann mit CHF 4'350 vor SG mit CHF 3'900. Für TG und AR weist das Wiki keinen solchen Ansatz aus («nicht anwendbar»). Ich habe diese Einträge nicht im Wortlaut geöffnet.
> - **Status:** Alle Werte sind ☑️ agent-geprüft: Die Fundstelle ist geprüft, die fachliche Abnahme steht noch aus.
> - **Gesetzliche Grundlage der Spalte «mit Vorsorgebeiträgen»:** Bund Art. 33 DBG, ZH § 31 StG, SG Art. 45 StG, TG § 34 StG, AR Art. 35 StG.
> 
> Ich habe die Abzüge für Kinder und für Verheiratete bewusst weggelassen. Sie gehören nicht zu Ihrer Frage.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q24

**Frage:** Steuerfreie Vermögensbeträge (Sozialabzüge) 2025 in SG für ein Ehepaar mit einem minderjährigen Kind?

**Soll (Referenz):** SG 2025: 150'000 (Ehepaar) + 20'000 pro minderjähriges Kind = 170'000 (sg-stg-2025__art-64).

**Antwort des Agenten** (23.1 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **SG · Steuerjahr 2025: steuerfreie Vermögensbeträge (Sozialabzüge Vermögen)**
> 
> Für ein Ehepaar mit einem minderjährigen Kind sind **CHF 170'000** vom Reinvermögen steuerfrei (Kanton und Gemeinde).
> 
> | Formularziffer (Code) | Abzug | Betrag |
> |---|---|---|
> | 36.2 (Code 332) | gemeinsam steuerpflichtige Ehegatten (2 × 75'000) | CHF 150'000 |
> | 36.3 (Code 334) | 1 minderjähriges Kind | CHF 20'000 |
> | **Total** | 150'000 + 20'000 (mit `rechne` geprüft) | **CHF 170'000** |
> 
> - **Voraussetzungen:** Massgebend sind die Verhältnisse am 31.12.2025. Das Kind muss minderjährig sein und unter der elterlichen Sorge bzw. Obhut stehen. Für volljährige Kinder in Ausbildung gibt es den Abzug 36.3 nicht.
> - **Bund:** Die direkte Bundessteuer kennt keine Vermögenssteuer, deshalb gibt es hier keinen Bundesbetrag. Das SG-Formular hat dafür nur eine Spalte.
> - **Status:** ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> - **Fundstellen:**
>   - 75'000 und 20'000: `sg-stg-2025__art-64` (Art. 64 StG SG)
>   - 150'000: `sg-wl-2025__c0118`
>   - Formularziffern: `sg-form-1-2025__c0013`
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q25

**Frage:** Welcher Verzugszins gilt 2026 für die direkte Bundessteuer?

**Soll (Referenz):** 4.00 % (RS 2-215, bund-rs-2-215__c0010/c0011).

**Antwort des Agenten** (20.1 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Bund · Steuerjahr 2026**
> 
> Der Verzugszins für die direkte Bundessteuer beträgt **4,00 %** im Jahr 2026. Im Jahr 2025 waren es 4,50 %. Der Rückerstattungszins beträgt ebenfalls 4,00 %. Status: ☑️ agent-geprüft, Abnahme offen. Quelle: `bund-rs-2-215__c0010` («Verzugs- und Rückerstattungszins 4,50 → 4,00»).
> 
> Zum Vergütungszins für Vorauszahlungen steht in derselben Quelle 0,00 % (2025: 0,75 %). Einen Ausgleichszins kennt der Bund nicht.
> 
> Die Fachperson sollte die Zahlen vor der Verwendung prüfen. Der Wert gilt nur für den Bund. Kantons- und Gemeindesteuern haben eigene Zinsregeln.

## q26

**Frage:** Wann wird der Eigenmietwert abgeschafft und gilt das schon für 2026?

**Soll (Referenz):** Abschaffung per 1.1.2029 (Bundesratsbeschluss 01.04.2026); für 2025–2028 gilt bisheriges Recht – 2026 also noch Eigenmietwert.

**Antwort des Agenten** (27.9 s · Tools: 5 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Bund (direkte Bundessteuer) · Steuerjahr 2026.** Einen Kanton nennst du nicht. Die Antwort gilt aber überall, weil die Reform Bundesrecht ist und Bund und Kantone gleichzeitig betrifft.
> 
> **Wann wird der Eigenmietwert abgeschafft?**
> Per **1. Januar 2029**. Das hat der Bundesrat am 1. April 2026 beschlossen (bund-mm-eigenmietwert-abschaffung__c0002). Im September 2025 hatten Volk und Stände den Bundesbeschluss über die kantonalen Liegenschaftssteuern auf Zweitliegenschaften angenommen. Damit stimmten sie auch der Abschaffung der Eigenmietwertbesteuerung zu (c0003). Den Zeitpunkt des Inkrafttretens bestimmt der Bundesrat. Die Kantone sollten Zeit für die Gesetzesanpassung haben und die neue Objektsteuer auf Zweitliegenschaften gleichzeitig einführen können (c0003).
> 
> **Gilt das schon für 2026?**
> **Nein.** Der Eigenmietwert bleibt für 2026 steuerbar, ebenso für 2027 und 2028. Die Abschaffung wirkt erst ab dem Steuerjahr 2029. Das ergibt sich aus dem Inkrafttreten per 1.1.2029. Das Wiki führt für 2026 den Eigenmietwert weiterhin als Einkunft (Formular 2 2026, Ziff. 8, bund-form-2-2026__c0007).
> 
> **Was ändert sich ab 2029?** (c0004)
> - Der Eigenmietwert entfällt auf selbstgenutztem Wohneigentum.
> - Der Abzug der Unterhaltskosten entfällt für selbstgenutztes Wohneigentum bei Bund, Kantonen und Gemeinden. Bei vermietetem oder verpachtetem Wohneigentum bleibt er erhalten.
> - Schuldzinsen sind nur noch im Verhältnis des Werts der vermieteten oder verpachteten Liegenschaften zum gesamten Vermögen abzugsfähig. Wer erstmals in der Schweiz ein Eigenheim kauft, bekommt einen zeitlich und betragsmässig begrenzten Ersterwerberabzug.
> - Bei der direkten Bundessteuer entfallen die Abzüge für Energiespar- und Umweltschutzinvestitionen. Die Kantone können sie, zeitlich begrenzt, weiterführen.
> - Die Kantone dürfen eine Objektsteuer auf überwiegend selbstgenutzten Zweitliegenschaften erheben.
> 
> **Für die Steuererklärung 2026:** Eigenmietwert und Unterhaltskostenabzug (Pauschale oder effektiv) wie bisher deklarieren. Wenn du mir den Kanton nennst, rechne ich dir die 2026er-Werte durch. Der kantonale Abzug auf dem Eigenmietwert ist sehr unterschiedlich, zum Beispiel ZH 10 %, AR 20 %, SG 30 %, TG 40 %.
> 
> Die Quelle ist eine Medienmitteilung. Die kantonalen Umsetzungsgesetze habe ich nicht geprüft. Die fachliche Beurteilung bleibt bei der Fachperson.

## q27

**Frage:** Zitiere die Regel zum Abzug privater Schuldzinsen im DBG (Steuerjahr 2025) mit Artikel.

**Soll (Referenz):** Art. 33 Abs. 1 lit. a DBG (Fassung 2025): private Schuldzinsen im Umfang der steuerbaren Vermögenserträge (Art. 20, 20a, 21) und weiterer CHF 50'000.

**Antwort des Agenten** (24.4 s · Tools: 4 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Bund (DBG) · Steuerjahr 2025**
> 
> **Art. 33 Abs. 1 Bst. a DBG** (Chunk `bund-dbg-2025__art-33-t1`, Fassung gültig bis 31.12.2025):
> 
> > «Von den Einkünften werden abgezogen: a. die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken. Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten oder ihr sonst wie nahe stehenden natürlichen Person zu Bedingungen gewährt, die erheblich von den im Geschäftsverkehr unter Dritten üblichen Bedingungen abweichen;»
> 
> **Bestätigung durch die ESTV:** Das Kreisschreiben 22a, Ziff. 1 (Chunk `bund-ks-22a__c0002`) fasst die Regel so zusammen: Private Schuldzinsen sind «im Umfang des Ertrages aus beweglichem und unbeweglichem Vermögen (Art. 20 und 21 DBG) und weiterer 50'000 Franken abziehbar». Zinsen auf Geschäftsschulden sind weiterhin vollumfänglich abziehbar (Art. 27 Abs. 2 Bst. d DBG).
> 
> **Praktisch:** Der Abzug ist begrenzt auf die steuerbaren Vermögenserträge (Art. 20, 20a, 21 DBG) plus 50'000 Franken.
> 
> **Status und Vorbehalte:**
> - Der Wortlaut stammt direkt aus dem geöffneten Gesetzes-Chunk.
> - Das Wiki weist für die Fassung 2026 einen eigenen Chunk aus (`bund-dbg-2026`). Diesen habe ich nicht geprüft.
> - Die Anwendung auf einen konkreten Fall, etwa die Frage, was zu den Vermögenserträgen zählt, habe ich nicht geprüft. Dafür gehört die Beurteilung zur Fachperson.

## q28

**Frage:** Ist ein Leasingvertrag für das Privatauto steuerlich relevant? Was ist mit den Leasingraten?

**Soll (Referenz):** Leasingraten sind keine Schuldzinsen und grundsätzlich nicht abziehbar (Lebenshaltung); relevant nur für Fahrkosten-Begründung/Geschäftsauto, Vermögen (kein Eigentum).

**Antwort des Agenten** (28.8 s · Tools: 3 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read):

> **Kanton: nicht angegeben · Steuerjahr 2025 (angenommen, da keine Jahreszahl genannt)**
> 
> **Kurz: Nein.** Ein Leasingvertrag für ein Privatauto ist steuerlich nicht relevant. Die Leasingraten sind nicht abziehbar.
> 
> - **Leasingraten:** Sie zählen zu den privaten Lebenshaltungskosten (Art. 34 DBG, Fundstelle zh-wl-2025__c0073, ☑️ agent-geprüft). Das gilt auch für den Zinsanteil in der Rate.
> - **Schuldzinsen:** Die Rate gehört nicht in die Ziffer «Schuldzinsen» und nicht ins Schuldenverzeichnis.
> - **Vermögen:** Ein geleastes Auto gehört dem Leasinggeber und wird nicht deklariert. Anders ist es bei einem Auto im eigenen Eigentum.
> - **Fahrkosten:** Der Arbeitsweg-Abzug hängt nicht vom Leasing ab. Er richtet sich nach dem Arbeitsweg und dem Verkehrsmittel. Beim Privatauto ist er nur in begründeten Fällen mit der Kilometerpauschale möglich. Die Leasingkosten sind damit abgegolten und werden nicht zusätzlich abgezogen.
> - **Ausnahme:** Bei Selbständigerwerbenden ist der geschäftliche Anteil der Leasingraten Aufwand in der Jahresrechnung. Das gilt nicht für ein reines Privatauto. Zu klären wäre, ob der Mandant oder der Arbeitgeber/das Geschäft Leasingnehmer ist.
> 
> **Ablage:** Der Vertrag ist kein Steuerbeleg und gehört deshalb in keine Steuerbeleg-Kategorie der `KATEGORIEN.md`. Weder «Belege eingereicht» noch «Belege Sonstiges» passt, da er keinen Wert in der Steuererklärung hat. Wenn die Kilometerleistung für einen Fahrkostenabzug gebraucht wird, kann diese Angabe zu den Unterlagen Kunde.
> 
> **Nicht geprüft:** Die Fundstelle stammt aus dem ZH-Wiki. Für AR, SG und TG habe ich die Regel nicht einzeln nachgeschlagen, weil kein Kanton genannt war. Nach dem Bundesrecht (Art. 34 DBG) gilt dasselbe. Sagen Sie mir den Kanton, dann prüfe ich die Fahrkosten-Limiten für Kanton und Bund konkret nach.

## q29

**Frage:** Wie hoch ist der Kinderabzug im Kanton Bern 2025?

**Soll (Referenz):** Nicht im Wiki (nur Bund, AR, SG, TG, ZH).

**Antwort des Agenten** (25.3 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__wert):

> **Kanton Bern · Steuerjahr 2025: nicht im Wiki.**
> 
> Das Steuer-Wiki deckt nur Bund, AR, SG, TG und ZH ab. Zu Bern gibt es keine Quellen, und die Suche mit `jur=be` hat keine Treffer geliefert. Einen Berner Betrag nenne ich nicht, weil ich ihn nicht belegen kann. Aus einem anderen Kanton übernehme ich auch nichts.
> 
> Den Wert finden Sie in der Wegleitung zur Berner Steuererklärung 2025 oder im Steuergesetz des Kantons Bern (BE) auf der Seite der Steuerverwaltung Bern. Dort steht der Kinderabzug nach den Berner Regeln.
> 
> **Bund (direkte Bundessteuer) · 2025**
> Das gilt unabhängig vom Wohnkanton und damit auch für Bern. Die Werte sind ☑️ agent-geprüft, die Abnahme ist noch offen.
> - **Kinderabzug vom Einkommen:** CHF 6'800 je minderjähriges Kind oder Kind in Ausbildung. Es gibt keine Altersstaffel. Quelle: `bund-dbg-2025__art-35`.
> - **Zusätzlich Abzug vom Steuerbetrag:** CHF 263 je Kind. Quelle: `bund-dbg-2025__art-36-t4`.
> - **Versicherungsabzug:** Zuschlag von CHF 700 je Kind. Quelle: `bund-dbg-2025__art-33-t5`.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q30

**Frage:** Ehepaar TG 2025, beide angestellt (Nettolohn 80'000 und 30'000), pendelt mit ÖV-Abo (CHF 1'200 bzw. 900). Erstelle die Abzüge Berufskosten (Fahrkosten, Verpflegung ohne Kantine, Pauschale übrige) je Person für Kanton und Bund mit Fundstellen.

**Soll (Referenz):** TG 2025 je Person: Fahrkosten = ÖV-Abo effektiv (1'200 bzw. 900; Max. 6'000 Staat / 3'300 Bund); Verpflegung ohne Kantine 15/Tag, max. 3'200 (beide Ebenen); übrige Pauschale 3 %: P1 80'000 → 2'400, P2 30'000 → 900 → Minimum 2'000 (beide Ebenen, BKV TG § 4a / BKV Bund).

**Antwort des Agenten** (40.7 s · Tools: 10 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne, steuerwiki__zeige):

> **TG · Steuerjahr 2025 · Berufskosten Ehepaar (Hilfsblatt Formular 4.2 für Person 1, 4.3 für Person 2)**
> 
> Die Beträge sind für Kanton (Staats- und Gemeindesteuer) und Bund (direkte Bundessteuer) gleich. Das Formular hat dafür zwei Spalten, links Staat und rechts Bund (tg-wl-2025__c0196). Alle Fundstellen sind ☑️ agent-geprüft, die Abnahme ist offen.
> 
> | Position | Person 1 (Netto 80'000, Abo 1'200) | Person 2 (Netto 30'000, Abo 900) |
> |---|---|---|
> | Fahrkosten, ÖV-Abo (Ziff. 2.1, Code 206 / 246) | Kanton 1'200 · Bund 1'200 | Kanton 900 · Bund 900 |
> | Verpflegung ohne Kantine (Ziff. 3.1, Code 214 / 254) | 3'200 | 3'200 |
> | Übrige Berufskosten, Pauschale (Ziff. 4, Code 220 / 260) | 2'400 (3 % von 80'000) | 2'000 (3 % von 30'000 = 900, Minimum greift) |
> | **Total Berufsauslagen (Ziff. 7, Code 240 / 280)** | **6'800** (Kanton und Bund) | **6'100** (Kanton und Bund) |
> 
> Die Berufsauslagen von Person 1 gehören in Ziff. 10.1 des Hauptformulars (Code 240), die von Person 2 in Ziff. 10.2 (Code 280). Das Total beider Personen beträgt 12'900, jeweils für Kanton und Bund.
> 
> **Fundstellen**
> - **Fahrkosten:**
>   - Es zählen die tatsächlich bezahlten Abokosten, bei Kanton und Bund gleich: tg-form-04-2-2025__c0002 und tg-wl-2025__c0177.
>   - Die Limiten (Kanton max. 6'000, Bund max. 3'300) sind nicht erreicht: tg-stg__par-29 und bund-dbg-2025__art-26.
>   - Die Begrenzung steht in Ziff. 2.5, Code 213 / 253.
> - **Verpflegung:**
>   - 15 Franken pro Hauptmahlzeit, maximal 3'200 im Jahr: tg-bkv__par-2-t1, tg-form-04-2-2025__c0003 und tg-wl-2025__c0183.
>   - Bund: bund-bkv-2025__anhang-1 (15 Franken pro Tag, 3'200 im Jahr).
>   - Rechnung: 15 × 225 Tage = 3'375, gedeckelt auf 3'200 (Tagesansatz × Tage aus der Rechnung in Ziff. 3.1, 225 Tage als Regelwert bei 100 %-Pensum aus tg-wl-2025__c0003).
> - **Übrige Berufskosten:** 3 % des Nettolohns gemäss Lohnausweis Ziff. 11, mindestens 2'000 und höchstens 4'000, für Kanton und Bund: tg-bkv__par-4a, tg-form-04-2-2025__c0004, tg-wl-2025__c0187 und bund-bkv-2025__anhang-1.
> 
> **Vorbehalte**
> 1. **Verpflegung:**
>    - Die 3'200 sind der Höchstbetrag und setzen voraus, dass beide 100 % arbeiten.
>    - Der Abzug gilt nur, wenn die Heimkehr am Mittag unzumutbar ist, wegen grosser Entfernung oder einer sehr kurzen Essenspause (tg-wl-2025__c0183). Ein ÖV-Pendeln allein genügt dafür nicht.
>    - Bei Teilzeit wird der Betrag nach Beschäftigungsgrad gekürzt, zum Beispiel 2'560 bei 80 %. Ohne Angaben dazu ist der Abzug nicht belegt.
>    - Ist die Heimkehr zumutbar, entfällt er. Dann betragen die Totale 3'600 (Person 1) und 2'900 (Person 2), zusammen 6'500.
> 2. **Lohnausweis prüfen:** Feld F (Geschäftsfahrzeug) bedeutet keine Fahrkosten. Feld G (Kantine oder Verbilligung) bedeutet nur den halben Verpflegungsabzug (7.50 pro Tag, maximal 1'600; tg-wl-2025__c0185). Übernimmt der Arbeitgeber das Abo, ist es nicht abziehbar.
> 3. **Übrige Berufskosten:** Die Pauschale ersetzt die effektiven Kosten; beides zusammen ist nicht möglich. Bei unterjähriger Erwerbstätigkeit wird sie anteilmässig gekürzt.
> 4. **Belege:** Die Lohnausweise sind einzureichen (tg-wl-2025__c0035). Beim ÖV-Abo ist «einreichen» im Wiki als unklar vermerkt; die Belege sollten bereitliegen.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q31

**Frage:** Ehepaar ZH 2026, beide erwerbstätig, Kind 3 Jahre in der Kita (Kosten CHF 30'000). Wie viel Drittbetreuung ist abziehbar (Kanton und Bund)?

**Soll (Referenz):** ZH 2026 Kanton max. CHF 25'300 pro Kind (zh-stg-2026__par-31-t3); Bund 2026 max. CHF 25'800 (bund-dbg-2026__art-33-t7). Abzug je Ebene getrennt.

**Antwort des Agenten** (30.1 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **ZH · Steuerjahr 2026**
> 
> Abziehbar sind bei Kita-Kosten von CHF 30'000:
> 
> | | Abzug | Nicht abziehbar |
> |---|---|---|
> | **Kanton (Staatssteuer)** | **CHF 25'300** | CHF 4'700 |
> | **Bund (direkte Bundessteuer)** | **CHF 25'800** | CHF 4'200 |
> 
> **Berechnung:** Es gelten die nachgewiesenen Kosten, höchstens CHF 25'300 (Kanton) bzw. CHF 25'800 (Bund) pro Kind. Die Kosten von CHF 30'000 liegen über beiden Limiten, deshalb greift die Limite.
> 
> **Formular:** Ziff. 16.6 «Abzug für fremdbetreute Kinder (Jahrg. 2012–2026)», Code 376. Die Spalten Staatssteuer und Bundessteuer werden getrennt ausgefüllt.
> 
> **Voraussetzungen, die hier erfüllt sind:**
> - Das Kind ist 3 Jahre alt (Grenze: das 14. Altersjahr noch nicht vollendet).
> - Es lebt im gleichen Haushalt.
> - Beide Eltern sind gleichzeitig erwerbstätig. Bei Ehepaaren ist das Pflicht.
> 
> **Zu beachten:**
> - **Pauschalrechnung:** Weist die Kita nur einen Pauschalbetrag aus, der auch Verpflegung oder Ähnliches enthält, sind 20 % als Lebenshaltungskosten zu kürzen. Bei 30'000 wären das 24'000, also unter beiden Limiten. Das gilt nur bei Pauschalen. Rechnet die Kita die reine Betreuung separat ab, entfällt die Kürzung.
> - **Belege:** Kita-Rechnungen mit Zahlungsnachweis und eine Aufstellung der Empfänger sind beizulegen.
> - **Nicht abziehbar:** Sport, Musik, Nachhilfe, Schulgeld und Ähnliches.
> - **Alternierende Obhut / Konkubinat:** Hier wäre es je der halbe Höchstbetrag (12'650 Kanton, 12'900 Bund). Das trifft bei einem Ehepaar im gleichen Haushalt nicht zu.
> 
> **Quellen:**
> - Kanton: zh-stg-2026__par-31-t3.
> - Bund: bund-dbg-2026__art-33-t7.
> - Formular: zh-form-300-2026-uj__c0008 und Wegleitung zh-wl-2026-uj__c0105.
> 
> **Status:** Alle Werte sind ☑️ agent-geprüft, die Abnahme ist offen. Das reguläre Formular und die Wegleitung ZH 2026 sind noch nicht publiziert (Stand 09.11.2026). Die Ziffer stützt sich auf die Fassung für unterjährige Steuerpflicht und ist am regulären Formular zu prüfen. Die fachliche Beurteilung bleibt bei der Fachperson.

## q32

**Frage:** SG 2025: Einfamilienhaus (Baujahr 2010), selbst bewohnt. Pauschalabzug Liegenschaftsunterhalt Kanton und Bund?

**Soll (Referenz):** SG 2025: 20 % des Eigenmietwerts, ohne Altersstaffel (sg-stv__art-29); Bund: Gebäude zu Beginn 2025 über 10 Jahre alt → 20 % (bund-lkv__art-5).

**Antwort des Agenten** (26.3 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **SG · Steuerjahr 2025**
> 
> Für ein Einfamilienhaus mit Baujahr 2010, das Sie selbst bewohnen, beträgt der Pauschalabzug sowohl im Kanton als auch beim Bund **20 %**.
> 
> | | Satz | Fundstelle | Status |
> |---|---|---|---|
> | **Kanton (Staats- und Gemeindesteuer)** | **20 %** des angerechneten Eigenmietwerts. SG kennt keine Staffelung nach Gebäudealter. | sg-stv__art-29 | ☑️ agent-geprüft |
> | **Bund (direkte Bundessteuer)** | **20 %**, weil das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist. | bund-lkv__art-5 | ☑️ agent-geprüft |
> 
> - **Bund:** Das Haus ist Baujahr 2010 und am 1.1.2025 rund 15 Jahre alt. Der tiefere Satz von 10 % gilt nur für Gebäude bis 10 Jahre.
> - **Basis der Pauschale:** Es ist der angerechnete Eigenmietwert aus Formular 7 Teil B. Dieser ist bereits um 30 % herabgesetzt (sg-stg-2025__art-34).
> - **Formular:** Die Pauschale wird in Formular 7 Teil C berechnet und nach **Ziff. 15 (Code 716)** übertragen. Das Formular hat nur eine Spalte. Abweichungen für die Bundessteuer nimmt die Steuerbehörde automatisch vor (sg-wl-2025__c0173). Der Bund-Satz muss daher nicht separat erfasst werden.
> - **Wahlrecht:** Sie können pro Steuerperiode und Liegenschaft entweder die Pauschale oder die tatsächlichen Kosten abziehen. Die Pauschale deckt alle Unterhalts- und Verwaltungskosten, auch Denkmalpflege sowie Energiespar- und Umweltinvestitionen (sg-wl-2025__c0161). Belege müssen Sie nur bei den tatsächlichen Kosten und nur auf Verlangen vorlegen.
> - **Miteigentum:** Falls das Haus mehreren Personen gehört, gilt die Pauschale nur im Umfang Ihres Eigentumsanteils.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q33

**Frage:** ZH 2025: Kind 19 Jahre, in Lehre (Ausbildung). Kinderabzug Kanton und Bund?

**Soll (Referenz):** ZH 2025 Kanton CHF 9'300 (volljährig in Erstausbildung, zh-stg-2025__par-34); Bund CHF 6'800 (bund-dbg-2025__art-35) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (31.2 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__wert):

> **ZH · Steuerjahr 2025: Kinderabzug für ein 19-jähriges Kind in der Lehre**
> 
> Das Kind ist am 31.12.2025 volljährig (Jahrgang 2006). Der Abzug steht trotzdem zu, wenn es in beruflicher Erstausbildung ist und Sie seinen Unterhalt zur Hauptsache bestreiten.
> 
> | | Kanton (Staatssteuer) | Bund (dBSt) |
> |---|---|---|
> | Kinderabzug (Ziff. 24.1, Code 370 im Haushalt / 372 ausserhalb) | **CHF 9'300** | **CHF 6'800** |
> | Zusätzlicher Versicherungsabzug je Kind (Form. 365, Code 613) | CHF 1'300 | CHF 700 |
> 
> Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Fundstellen**
> - Kanton: zh-stg-2025__par-34 (§ 34 StG) und zh-form-300-2025__c0010.
> - Bund: bund-dbg-2025__art-35 (Art. 35 DBG).
> - Versicherungsabzug: zh-stg-2025__par-31-t2 und bund-dbg-2025__art-33-t5.
> 
> **Voraussetzungen**
> - Das Kind steht am 31.12.2025 in beruflicher Erstausbildung. Der Lehrvertrag oder die Lehrbestätigung ist der Beleg. Kantonal gelten ein Lehrvertrag oder Schule mindestens halbtags und mindestens ein halbes Jahr (ZStB 34.1).
> - Sie bestreiten den Unterhalt zur Hauptsache, und das Kind ist auf die Unterstützung angewiesen.
> - Für ein volljähriges Kind in Erstausbildung gilt der volle Abzug. Es gibt keine Alterstaffel und keinen Zuschlag für auswärtige Ausbildung.
> 
> **Wo eintragen**
> - Wohnt das Kind bei Ihnen, tragen Sie es auf Seite 1 unter «Kinder in Ihrem Haushalt» ein und setzen den Abzug in Code 370 ein (Kanton 9'300, Bund 6'800).
> - Wohnt es auswärts, tragen Sie es unter «Kinder ausserhalb Ihres Haushaltes» ein, mit Code 372 und Nachweis der Unterhaltszahlungen.
> - Der Zusatzabzug für die Versicherungsprämien kommt zusätzlich in Form. 365 (Code 613).
> 
> **Getrennt lebende Eltern**
> Bei gemeinsamer Sorge ohne Unterhaltsbeiträge gilt der halbe Abzug (4'650 Kanton / 3'400 Bund, Zusatzabzug 650 / 350). Wer Unterhaltsbeiträge für das Kind abzieht, erhält keinen Kinderabzug.
> 
> **Nur Bund: Ermässigung auf dem Steuerbetrag**
> Der Steuerbetrag der Bundessteuer ermässigt sich um CHF 263 je Kind (bund-dbg-2025__art-36-t4, ☑️). Das ist kein Abzug im Formular, sondern wird bei der Steuerberechnung berücksichtigt. Ob die Ermässigung bei einem volljährigen Kind in Ausbildung gleich greift, habe ich nicht separat geprüft. Die Quelle nennt «Kind oder unterstützungsbedürftige Person».
> 
> **Offen**
> Ob «zur Hauptsache» erfüllt ist, hängt von Lehrlohn und Ihren Zahlungen ab. Die Quellen nennen dafür keine feste Betragsgrenze, ich schätze das nicht. Die Beurteilung liegt bei der Fachperson.

## q34

**Frage:** ZH 2025: Lohnausweis Feld G angekreuzt (Kantine). Welche Verpflegungspauschale gilt und in welche Ziffer des Berufsauslagenformulars?

**Soll (Referenz):** Verbilligte Verpflegung: CHF 7.50 pro Arbeitstag, max. CHF 1'600 pro Jahr (LS 631.33, zh-pauschalierung-berufsauslagen-2025__c0004); Form. 360 Ziff. 2.1 (verbilligt); Bund gleich.

**Antwort des Agenten** (25.0 s · Tools: 3 Aufrufe steuerwiki__beleg, steuerwiki__wert, steuerwiki__position):

> **ZH · Steuerjahr 2025**
> 
> **Pauschale:** Bei angekreuztem Feld G gilt nur der reduzierte Verpflegungsabzug von **CHF 7.50 pro Arbeitstag, höchstens CHF 1'600 pro Jahr**. Der volle Satz von CHF 15 pro Tag (max. CHF 3'200) gilt hier nicht. Status ☑️ agent-geprüft (Quelle: zh-pauschalierung-berufsauslagen-2025__c0004, zh-form-360-2025__c0003).
> 
> **Eintrag im Formular:** Form. 360 (Hilfsblatt Berufsauslagen), **Ziffer 2.1 «verbilligt»**.
> - Person 1: **Code 206**
> - Person 2: **Code 226**
> - Der Code ist in beiden Spalten (Staatssteuer und Bundessteuer) derselbe.
> 
> **Rechnung:** `min(Arbeitstage × 7.50; 1'600)`. Der Betrag gilt für Kanton und Bund gleich. Die CHF 7.50 sind bereits der halbe Abzug und werden nicht nochmals halbiert.
> 
> **Bund:** Der halbe Abzug gilt nur bei Kantine, Personalrestaurant oder Gutscheinen. Bei einem Barbeitrag gibt es beim Bund keinen halben Abzug. Zudem entfällt der Abzug mangels Mehrkosten, wenn die Hauptmahlzeiten höchstens CHF 10 kosten. Das passt zu Feld G «Kantine», sollte aber anhand der Art der Verpflegung kurz geprüft werden.
> 
> **Zu beachten:**
> - Der Abzug gilt nur, wenn die Heimkehr in der Mittagspause nicht möglich ist und trotzdem Mehrkosten entstehen. Die Arbeitstage mit auswärtiger Verpflegung sind aus einem Arbeitszeitnachweis zu entnehmen.
> - Er ist nicht kumulierbar mit Ziff. 2.1 voll (Code 208/228), dem Schichtarbeitsabzug Ziff. 2.2 (Code 210) oder der Mittagsheimfahrt.
> - Feld G wird auch angekreuzt, wenn die Nutzung unbekannt ist (Lunch-Checks, verbilligtes Personalrestaurant). Die Regel dazu stützt sich auf die ESTV-Wegleitung zum Lohnausweis in der Fassung 2026 (bund-wl-lohnausweis-2026__c0012). Eine 2025er Fassung ist im Wiki nicht vorhanden.
> - Steht im Lohnausweis Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt», sind die Folgen für den Abzug separat zu prüfen.
> - Der Lohnausweis ist der Steuererklärung beizulegen (zh-wl-2025__c0032).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q35

**Frage:** SG 2025: Kapitalbezug Säule 3a CHF 100'000. Wird das mit dem übrigen Einkommen besteuert? Wo deklarieren?

**Soll (Referenz):** Nein – Kapitalleistungen aus Vorsorge werden getrennt vom übrigen Einkommen (separate Jahressteuer) besteuert; SG Formular 1 Ziff. 40.1 (Säule 3a), Total Ziff. 41.

**Antwort des Agenten** (26.3 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **SG · Steuerjahr 2025**
> 
> **Nein, der Bezug wird nicht mit dem übrigen Einkommen besteuert.** Kapitalleistungen aus der Säule 3a werden gesondert vom übrigen Einkommen besteuert, mit einer separaten vollen Jahressteuer. Der Bezug erhöht also den Steuersatz auf dem übrigen Einkommen nicht (sg-wl-2025__c0119, ☑️ agent-geprüft).
> 
> **Wo deklarieren:** Formular 1, **Ziff. 40.1** («aus gebundener Vorsorge Säule 3a»), Abschnitt «Weitere Angaben» (sg-form-1-2025__c0014).
> - Die Bescheinigung der Bank oder Versicherung ist beizulegen (Einreichepflicht: ja).
> - Der Betrag gehört nicht in Ziff. 6.4.
> - Die Deklaration erfolgt nur zu Informationszwecken. Die Steuer wird separat veranlagt.
> - Bei mehreren Bezügen im Jahr 2025 ist der Gesamtbetrag anzugeben.
> 
> **Besteuerung Kanton/Gemeinde:**
> - Die einfache Steuer beträgt 2,2 % für die übrigen Steuerpflichtigen und 2,0 % für gemeinsam steuerpflichtige Ehegatten (sg-stg-2025__art-52).
> - Der 2,0 %-Satz gilt auch für Verwitwete, Getrennte, Geschiedene und Ledige, die mit Kindern oder Unterstützungsbedürftigen im gleichen Haushalt leben.
> - Allgemeine Abzüge und Sozialabzüge werden nicht gewährt.
> - Bei CHF 100'000 ergibt das eine einfache Steuer von CHF 2'200 (übrige) bzw. CHF 2'000 (Ehegatten).
> - Darauf kommen noch die Steuerfüsse von Kanton und Gemeinde. Die Gesamtbelastung habe ich nicht berechnet, weil mir der Steuerfuss fehlt.
> 
> **Bund (direkte Bundessteuer):**
> - Die Steuer wird zu einem Fünftel der Tarife nach Art. 36 DBG berechnet, ohne Sozialabzüge (bund-dbg-2025__art-38).
> - Das Formular hat dafür keine eigene Spalte. Dieselbe Angabe in Ziff. 40.1 genügt, die Behörde nimmt die Bundesberechnung automatisch vor.
> - Den Bundesbetrag in CHF habe ich nicht ausgerechnet, weil ich den Tarif nicht geprüft habe.
> 
> **Status:** Alle Angaben sind ☑️ agent-geprüft, die Abnahme ist offen. Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> **Zeitpunkt:** Massgebend ist das Jahr, in dem das Geld zugeflossen ist, hier 2025. Die Steuer entsteht im Zuflusszeitpunkt.

## q36

**Frage:** ZH 2025: Geschiedener Mandant zahlt Unterhaltsbeiträge an die Ex-Frau (CHF 24'000) und für das minderjährige Kind (CHF 12'000). Was ist abziehbar, in welcher Ziffer?

**Soll (Referenz):** Ex-Ehefrau CHF 24'000 voll abziehbar, Ziff. 13.1 (Code 254); Kinderalimente CHF 12'000 abziehbar bis und mit Monat der Volljährigkeit, Ziff. 13.2 (Code 255); Empfänger versteuert; Bund gleich (Art. 33 Abs. 1 lit. c DBG).

**Antwort des Agenten** (26.6 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **ZH · Steuerjahr 2025: Unterhaltsbeiträge des geschiedenen Mandanten**
> 
> Beide Beträge sind voll abziehbar, insgesamt CHF 36'000 (24'000 + 12'000). Sie gehören in zwei verschiedene Ziffern:
> 
> | Zahlung | Ziffer / Code | Abzug |
> |---|---|---|
> | Unterhalt an die Ex-Frau (persönlich) | **Ziff. 13.1 · Code 254** | CHF 24'000 |
> | Unterhalt für das minderjährige Kind | **Ziff. 13.2 · Code 255** | CHF 12'000 |
> 
> Beide Abzüge sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Fundstellen: Ziff. 13.1 zh-form-300-2025__c0007 und zh-wl-2025__c0075, Ziff. 13.2 zh-form-300-2025__c0007 und zh-wl-2025__c0076.
> 
> **Kanton und Bund**
> - Beide Ziffern haben eine Regel für Kanton und Bund. Die Quelle sagt «Kanton = Bund». Im Formular steht ein Code je Zeile für beide Spalten (Staatssteuer und Bundessteuer).
> 
> **Bedingungen**
> - **Ziff. 13.1 (Ex-Frau):**
>   - Abziehbar sind nur die periodischen Beiträge, die 2025 effektiv bezahlt wurden.
>   - Eine Kapitalabfindung gilt als Schuldentilgung und ist nicht abziehbar.
>   - Naturalleistungen (Miete, KK-Prämien, Schuldzinsen) sind gleichgestellt.
> - **Ziff. 13.2 (Kind):**
>   - Abziehbar sind die Zahlungen bis und mit dem Monat, in dem das Kind 18 wird. Spätere Zahlungen sind nicht mehr abziehbar. Dann gilt stattdessen der Kinderabzug nach Ziff. 24.1, sofern dessen Voraussetzungen erfüllt sind.
>   - Für das Kind, für das Alimente bezahlt werden, gibt es keinen Kinderabzug.
>   - Beim Bund zählen nur familienrechtlich geschuldete, effektiv bezahlte Alimente. Freiwillige Zahlungen zählen nicht.
> 
> **Gegenstück bei der Empfängerin**
> - Sie versteuert den Unterhalt für sich in Ziff. 5.1 (Code 160) und den Kinderunterhalt in Ziff. 5.2 (Code 161).
> 
> **Belege**
> - Nötig sind das Scheidungsurteil oder die Unterhaltsvereinbarung und die Zahlungsnachweise mit Monatszuordnung.
> - Ob die Zahlungsnachweise mit der Steuererklärung eingereicht werden müssen, ist in den Quellen strittig. Die Wegleitung nennt für 13.1 und 13.2 keine Beilagepflicht. Der Formularhinweis «sämtliche Zahlungsnachweise» steht unter Ziff. 13.3 und lässt sich nicht eindeutig auf 13.1 und 13.2 beziehen. Empfehlung: bis zum Entscheid der Fachperson die Zahlungsnachweise beilegen.
> 
> **Nicht geprüft**
> - Ob die CHF 12'000 nur die Zeit bis zum 18. Geburtstag betreffen, ist aus den Angaben nicht ersichtlich. Das Alter des Kindes ist offen. Der Betrag setzt voraus, dass alle Zahlungen vor dem Monat der Volljährigkeit erfolgten.
> - Die Beurteilung bleibt bei der Fachperson.

## q37

**Frage:** TG 2025: Mandant bringt Steuerberatungsrechnung, Kreditkartenabrechnung, Mietvertrag und Motorfahrzeugversicherung. Was davon ist relevant?

**Soll (Referenz):** Steuerberatungsrechnung: nein; Motorfahrzeugversicherung: nein; Kreditkartenabrechnung: bedingt (nur als Nachweis/Schuld per 31.12.); Mietvertrag: bedingt (Wochenaufenthalt/Arbeitszimmer/Adressnachweis) – laut belege-relevanz.

**Antwort des Agenten** (32.7 s · Tools: 7 Aufrufe read, steuerwiki__ablage, steuerwiki__beleg):

> **TG · Steuerjahr 2025 (aus Ihrer Anfrage)**
> 
> Es gibt nur zwei Dokumente mit möglichem Steuerwert, und beide nur unter einer Bedingung. Die Typerkennung beruht hier nur auf den Dokumentbezeichnungen. Ich habe keine Inhalte gesehen. Alle Einstufungen sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> | Dokument | Steuerrelevant? | Kategorie (KATEGORIEN.md) |
> |---|---|---|
> | **Steuerberatungsrechnung** | **Nein** | Keine Steuerbeleg-Kategorie |
> | **Kreditkartenabrechnung** | **Bedingt** | «Belege Sonstiges», falls ein Wert deklariert wird |
> | **Mietvertrag** | **Bedingt** | «Belege Sonstiges», falls ein Wert deklariert wird |
> | **Motorfahrzeugversicherung** | **Nein** | Keine Steuerbeleg-Kategorie |
> 
> **Nicht relevant**
> - **Steuerberatungsrechnung:** Kosten für Steuerberatung und das Ausfüllen der Steuererklärung im Privatvermögen sind nicht abziehbar. Beim Bund sind sie ausdrücklich nicht zulässig (bund-wl-2a-2025__c0057). Die Abgrenzung zu den Vermögensverwaltungskosten steht dort nur verkürzt. Ich habe sie nicht im Wortlaut geprüft.
> - **Motorfahrzeugversicherung:** Prämien, Verkehrssteuer, Treibstoff und Unterhalt des Privatfahrzeugs sind Lebenshaltungskosten. Sie sind nicht abziehbar (tg-wl-2025__c0123). Ausnahme: Fahrzeug als Geschäftsfahrzeug einer selbständigen Tätigkeit. Das ist nicht geprüft und ergibt sich auch nicht aus der Anfrage.
> - Die Steuerberatungsrechnung und die Motorfahrzeugversicherung gehören zu keiner Zeile von `KATEGORIEN.md`. Sie gelten weder als «Belege eingereicht» noch als «Belege Sonstiges». Wer sie trotzdem ablegen will, braucht dafür eine Regel von consis. Das ist offen.
> 
> **Bedingt relevant**
> - **Kreditkartenabrechnung:** Die Abrechnung selbst ist kein Steuerbeleg. Relevant wird sie in zwei Fällen:
>   - Bei Saldovortrag zählen der Saldo per 31.12.2025 und die Sollzinsen als Privatschulden. Sie gehören in Form. 4.1 A (Codes 455 und 286). Die Schuldzinsen sind privat nur bis Vermögensertrag + Fr. 50'000 abziehbar (Kanton und Bund).
>   - Als Zahlungsnachweis für einzelne abziehbare Posten, wenn die Originalrechnung fehlt (z.B. Spenden, Arzt-/Zahnarztkosten, Weiterbildung). Die Originalrechnung ist vorzuziehen.
>   - Kartengebühren und Alltagsumsätze sind nicht abziehbar.
>   - Wer eine Zusammenfassung ohne Saldovortrag und ohne Einzelbelege-Bedarf bringt, bei dem entfällt das Dokument.
> - **Mietvertrag:** Der Mietzins der selbstbewohnten Wohnung ist nicht abziehbar (Art. 34 lit. a DBG). Relevant ist der Vertrag nur in diesen Fällen:
>   - Untervermietung: Der Nettoertrag ist steuerbar (TG Ziff. 5.4).
>   - Wochenaufenthalt am Arbeitsort: Mehrkosten der Unterkunft sind abziehbar. Bei Wohnungen bis 3½ Zimmer gilt Mietzins : (Zimmer + 1) (tg-wl-2025__c0189).
>   - Mietzinsreduktion als Entgelt, z.B. Hauswart: Die Differenz ist Einkommen.
>   - Für den Mietvertrag ist im Wiki keine TG-Formularposition erfasst.
> 
> **Zur Einreichung in TG 2025:** Für beide bedingten Dokumente ist das in den TG-Quellen nicht konkret geregelt (unklar). Deshalb «Belege Sonstiges» (Eingereicht = nein), mit diesem Vorbehalt. Die Zuordnungen in der Liste sind laut Datei noch nicht von consis bestätigt.
> 
> **Nachfragen beim Mandanten**
> 1. Bleibt auf der Kreditkarte ein Saldo oder fallen Sollzinsen an?
> 2. Gibt es Untervermietung, einen Wochenaufenthalt oder eine Hauswart-Funktion?
> 
> Ohne ein Ja bei diesen Fragen sind alle vier Dokumente für die Steuererklärung nicht relevant. Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q38

**Frage:** AR 2026: Wie hoch ist der Kinderabzug für ein 10-jähriges Kind? Ist der Wert gesichert?

**Soll (Referenz):** AR 2026: CHF 7'400 laut Anhang 1 StG (indexiert), aber Status STRITTIG (MB 02 / StG-Text nennen andere Beträge; Wegleitung 2026 fehlt) → Fachperson.

**Antwort des Agenten** (26.2 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__zeige):

> **AR · Steuerjahr 2026: Kinderabzug für ein 10-jähriges Kind**
> 
> Das Kind ist nach dem 4. und vor dem 15. Geburtstag. Es gilt Ziff. 23.2 im Formular, Art. 38 Abs. 1 lit. a Ziff. 2 StG.
> 
> **Kanton (Staats- und Gemeindesteuer): CHF 7'400** nach dem Wiki-Wert. Dieser Wert ist ⚠️ **nicht gesichert**, denn die Quellen widersprechen sich:
> - **Anhang 1 StG** (indexierte Beträge per 1.1.2024) nennt CHF 7'400 (`ar-stg-anhang-kp__c0001`). Das ist der Wert, den das Wiki führt.
> - **Merkblatt MB AR 02** (Ziff. 2, gilt für 2025/2026/2027) nennt CHF 7'000 (`ar-mb-02__c0002`). Das entspricht dem nicht indexierten Gesetzestext.
> - **Wegleitung 2025** bestätigt für 2025 die Anhang-Werte 7'400, 5'300 und 11'600 (`ar-wl-2025__c0005`). Das ist ein anderes Steuerjahr und gilt für 2026 nicht automatisch.
> - **Wegleitung und Formular AR 2026** sind noch nicht publiziert (Stand 09.11.2026). Ziffern und Beträge sind deshalb vorbehalten, und die Position 23.2 ist im Wiki ⬜ offen.
> 
> Welcher Wert für 2026 gilt, kann ich nicht entscheiden. Die Abweichung beträgt CHF 400 (7'400 gegenüber 7'000). Das Merkblatt widerspricht also dem Wert im Wiki. Für die Fachperson bleibt zu klären, ob Anhang 1 StG (indexiert) oder das Merkblatt massgebend ist. Das Wiki verweist auf Art. 39a StG als Grundlage für den Anhang, das habe ich nicht im Wortlaut geprüft.
> 
> **Bund (direkte Bundessteuer): CHF 6'800** Kinderabzug, einheitlich ohne Altersstaffelung (Art. 35 Abs. 1 lit. a DBG, `bund-dbg-2026__art-35`). ☑️ agent-geprüft, Abnahme offen. Zusätzlich ermässigt sich der Steuerbetrag um CHF 263 pro Kind (Art. 36 Abs. 2^bis DBG, `bund-dbg-2026__art-36-t4`, ☑️).
> 
> **Weitere kinderbezogene Positionen AR 2026** (☑️ agent-geprüft, Abnahme offen):
> - Versicherungsabzug: Zuschlag von CHF 1'000 pro Kind (Kanton, `ar-stg__art-35-t2`) bzw. CHF 700 (Bund).
> - Vermögen: zusätzlicher Freibetrag von CHF 25'000 pro minderjähriges Kind (`ar-stg__art-51`).
> 
> **Fazit:** Der Kanton-Wert (7'400 oder 7'000) ist nicht gesichert, der Bundeswert von 6'800 ist agent-geprüft. Bis die Wegleitung 2026 vorliegt, würde ich den Wert als Arbeitsstand mit Vorbehalt behandeln und die Fachperson entscheiden lassen.

## q39

**Frage:** Welche Vermögenssteuer-Freibeträge (Sozialabzüge) gelten 2025 in ZH für Alleinstehende und Verheiratete?

**Soll (Referenz):** ZH kennt keine Vermögens-Sozialabzüge, sondern Tarifstufen mit 0 ‰: Grundtarif erste CHF 80'000, Verheiratetentarif erste CHF 159'000 (zh-stg-2025__par-47); kein Betrag pro Kind.

**Antwort des Agenten** (23.1 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **ZH · Steuerjahr 2025 – Vermögenssteuer: steuerfreie Beträge**
> 
> In Zürich gibt es beim Vermögen keinen eigentlichen Sozialabzug. Der Freibetrag ergibt sich aus der ersten Tarifstufe (0 ‰) von § 47 StG.
> 
> | Tarif | Steuerfreies Vermögen (Staats-/Gemeindesteuer) | Fundstelle | Status |
> |---|---|---|---|
> | Alleinstehende (Grundtarif) | **CHF 80'000** | zh-stg-2025__par-47-t1 | ☑️ agent-geprüft |
> | Verheiratete (Verheiratetentarif) | **CHF 159'000** | zh-stg-2025__par-47-t2 | ☑️ agent-geprüft |
> 
> **Wer den Verheiratetentarif erhält:**
> - Verheiratete.
> - Verwitwete, Getrennte und Geschiedene.
> - Ledige, die mit Kindern im Sinn von § 34 Abs. 1 lit. a zusammenleben (§ 47 Abs. 2).
> - Bei nicht gemeinsam besteuerten Eltern mit je ½ Kinderabzug erhält ihn nur, wer den Kindesunterhalt hauptsächlich trägt.
> - Massgebend sind die Verhältnisse am Ende der Steuerperiode (§ 47 Abs. 3 StG).
> 
> **Im Formular:**
> - Es gibt kein Formularfeld für diesen Betrag. Ziff. 35 «Steuerbares Vermögen gesamt» ist Ziff. 33 minus Ziff. 34. Das volle Vermögen wird eingetragen, und der Freibetrag wirkt erst bei der Steuerberechnung.
> - Pro Kind gibt es beim Vermögen keinen zusätzlichen Abzug.
> 
> **Bund (direkte Bundessteuer):** Der Bund erhebt keine Vermögenssteuer, es gibt also keinen Freibetrag.
> 
> Hinweis: Der Status «agent-geprüft» heisst, dass die Fundstelle geprüft ist, die fachliche Abnahme aber noch offen ist. Die Beträge stimmen mit § 47 StG (Stand 1.1.2025) und der Quelle VKP 2024 überein. Die abschliessende Beurteilung bleibt bei der Fachperson.

## q40

**Frage:** Alleinstehende TG 2026, Nettolohn 90'000, ÖV-Abo 2'400, Säule 3a 7'258, Krankenkasse 5'500. Erstelle die Abzüge (Berufskosten, 3a, Versicherungsabzug) Kanton und Bund mit Fundstellen und Status.

**Soll (Referenz):** TG 2026 (Kanton/Bund): Fahrkosten 2'400 (Max. 6'000 / 3'300); übrige Berufskosten 3 % von 90'000 = 2'700 (Min. 2'000, Max. 4'000, beide Ebenen); Säule 3a 7'258 (TG und Bund ☑️ agent-geprüft); Versicherungsabzug TG max. 3'500 → 3'500, Bund max. 1'800 → 1'800 (Prämien 5'500 übersteigen beide Maxima).

**Antwort des Agenten** (37.5 s · Tools: 10 Aufrufe steuerwiki__formular, steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Thurgau · Steuerjahr 2026 · alleinstehend** (Nettolohn Fr. 90'000)
> 
> Status überall: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> | Formular | Position | Kanton | Bund | Fundstelle |
> |---|---|---|---|---|
> | Ziff. 10.1 / Form. 4.2 Ziff. 2.1 (Code 206) | ÖV-Abo, effektive Kosten | 2'400 | 2'400 | tg-wl-2026__c0177, tg-form-04-2-2026__c0002 |
> | Form. 4.2 Ziff. 2.5 | Fahrkostenmaximum (nicht erreicht) | max. 6'000 | max. 3'300 | tg-wl-2026__c0176, bund-dbg-2026__art-26 |
> | Form. 4.2 Ziff. 4 | Übrige Berufskosten: 3 % × 90'000 = 2'700 (Min. 2'000, Max. 4'000) | 2'700 | 2'700 | tg-bkv__par-4a, bund-bkv-2026__anhang-1 |
> | **Ziff. 10.1 (Code 240)** | **Total Berufsauslagen** (2'400 + 2'700) | **5'100** | **5'100** | |
> | **Ziff. 13.1 (Code 314)** | **Säule 3a**: min(7'258; 7'258) | **7'258** | **7'258** | tg-wl-2026__c0089, bund-bsv-masszahlen-2025-2026__c0003 |
> | Form. 5.2 A.1 (Code 324) | Krankenkasse netto | 5'500 | 5'500 | tg-form-05-2-2026__c0001 |
> | Form. 5.2 B.4 (Code 328) | Maximalabzug alleinstehend | 3'500 | 1'800 | tg-stg__par-34-t3, bund-dbg-2026__art-33-t2 |
> | **Ziff. 14 (Code 330)** | **Versicherungsabzug** = min(A; B) | **3'500** | **1'800** | tg-form-05-2-2026__c0003 |
> | | **Total dieser drei Abzüge** | **15'858** | **14'158** | |
> 
> Alle Summen und Limiten sind mit `rechne` berechnet.
> 
> **Zu den einzelnen Abzügen**
> - **Berufskosten:** Die 3-%-Pauschale beruht auf dem Nettolohn nach Lohnausweis Ziff. 11. Sie schliesst sich mit dem Abzug effektiver Kosten gegenseitig aus. Das ÖV-Abo ist nur abziehbar, wenn im Lohnausweis Feld F nicht angekreuzt ist (tg-wl-2026__c0175).
> - **Säule 3a:** Die Einzahlung entspricht genau der Limite mit 2. Säule (Fr. 7'258). Das setzt voraus, dass du einer Pensionskasse angeschlossen bist. Ohne PK würde die 20-%-Regel gelten (Fr. 18'000 bei Fr. 90'000, Maximum Fr. 36'288), und es wäre mehr Abzug möglich. Die 3a-Bescheinigung ist immer einzureichen (tg-wl-2026__c0034).
> - **Versicherungsabzug:** Die Krankenkassenprämie übersteigt die Limiten (Kanton 3'500, Bund 1'800). Der Abzug ist daher gedeckelt. Der erhöhte Bundesabzug von Fr. 2'700 gilt nur ohne Beiträge an die Säule 2/3a (tg-wl-2026__c0209). Du zahlst in die 3a ein, deshalb gilt Fr. 1'800.
> 
> **Offene Punkte**
> - Als Krankenkassenprämie ist die Nettoprämie nach Abzug der Prämienverbilligung (IPV) einzusetzen. Sind Fr. 5'500 die Bruttoprämie, ändert sich der Abzug nicht, solange der Nettobetrag über Fr. 3'500 liegt.
> - Verpflegung auswärts (Form. 4.2 Ziff. 3.1/3.2), weitere Prämien (Unfall, Leben, Sparzinsen) und Weiterbildung hast du nicht genannt. Ich habe sie nicht berücksichtigt. Die Verpflegung wäre ein zusätzlicher Berufskostenabzug (Pauschale max. Fr. 3'200, ✅ nur wenn die Voraussetzungen erfüllt sind). Das habe ich nicht geprüft.
> - Die Abzüge auf Basis des Nettoeinkommens (Krankheitskosten, Spenden), die Sozialabzüge und das steuerbare Einkommen habe ich nicht berechnet.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

