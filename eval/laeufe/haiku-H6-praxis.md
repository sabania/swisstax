# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 40 · Lauf: 2026-11-09 15:24
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q01

**Frage:** Mandantin (ZH, 2025) bringt: Lohnausweis, Krankenkassen-Prämienrechnung, Handyrechnung, 3a-Bescheinigung, Hausratversicherungspolice, Spendenquittung Rotes Kreuz CHF 80, Kita-Rechnungen. Welche sind relevant, wofür?

**Soll (Referenz):** Relevant: Lohnausweis (Einkünfte 1.1), Krankenkassenprämien (Versicherungsabzug Ziff. 15, Form. 365), 3a-Bescheinigung (Ziff. 14), Kita-Rechnungen (Ziff. 16.6 Drittbetreuung, max. 25'000 Kanton / 25'800 Bund). Spende CHF 80: unter Mindestbetrag 100 → nicht abziehbar (sofern Total < 100). Nicht relevant: Handyrechnung (Lebenshaltung), Hausratversicherung (kein Versicherungsabzug).

**Antwort des Agenten** (33.4 s · Tools: 7 Aufrufe steuerwiki__ablage):

> **Relevant (ZH 2025):**
> 
> | Dokument | Relevant? | Wofür | Beilegen? |
> |---|---|---|---|
> | **Lohnausweis** | Ja | Einkünfte aus unselbständiger Arbeit: Ziff. 1.1, 1.2; Form. 360 Ziff. 2.1, 2.2, 3, 5; Form. 367 | Ja, immer |
> | **3a-Bescheinigung** | Ja | Säule-3a-Abzug: Ziff. 14.1/14.2 (Form. 21 EDP) | Ja, bei Abzug |
> | **Krankenkassen-Prämienrechnung** | Ja | Versicherungsprämien: Ziff. 15, Form. 365 Teil A Ziff. 1–4 und 6 | Auf Verlangen. Die Formularangabe der Prämien ist beizulegen, der Beleg selbst nicht ausdrücklich verlangt |
> | **Kita-Rechnungen** | Bedingt | Kinderbetreuungskosten: Ziff. 16.6. Abzug nur für Kinder unter 14 Jahren, wenn die Kosten mit Erwerbstätigkeit oder Ausbildung zusammenhängen. ZH-Höchstbetrag laut Fundstelle CHF 25'000 pro Kind | Auf Verlangen. Eine Aufstellung der Kosten mit Empfängern ist unaufgefordert beizulegen |
> | **Spendenquittung Rotes Kreuz (CHF 80)** | Bedingt | Ziff. 22.2. Abzug nur, wenn die Zuwendungen des Jahres insgesamt mindestens CHF 100 betragen | Auf Verlangen. Eine Liste aller Zuwendungen ist beizulegen |
> 
> **Nicht relevant:**
> - **Handyrechnung:** Private Telefon- und Internetkosten sind nicht abziehbar (Lebenshaltung, Art. 34 lit. a DBG). Nur bei einem beruflich genutzten Anteil ergäbe sich ein Thema, dazu ist im Fall nichts belegt.
> - **Hausratversicherungspolice:** Prämien für Mobiliar und Hausrat sind nicht abziehbar. Die Fundstelle stammt aus dem Kanton AR; für ZH habe ich diesen Punkt nicht separat belegt.
> 
> **Offen für die Spende:** CHF 80 erreichen allein die Schwelle von CHF 100 nicht. Ein Abzug kommt nur in Betracht, wenn weitere Zuwendungen im Jahr 2025 dazukommen. Das sollte mit der Mandantin geklärt werden.
> 
> **Hinweise:**
> - Alle Einordnungen sind agent-geprüft (☑️). Die Fundstellen sind geprüft, die fachliche Abnahme steht aus.
> - Die Kita-Limite stammt aus dem ZH-Steuergesetz. Den Bundeswert habe ich in dieser Abfrage nicht geprüft.
> - Die Kategorien aus `KATEGORIEN.md` habe ich noch nicht bestimmt. Soll ich das als Nächstes machen?

## q02

**Frage:** In welche Ziffer und mit welchem Code der ZH-Steuererklärung 2025 gehört der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb)?

**Soll (Referenz):** Ziff. 1.1 Haupterwerb, Code 100 (Person 1) / 101 (Person 2); Nettolohn Lohnausweis Ziff. 11 (zh-form-300-2025).

**Antwort des Agenten** (21.5 s · Tools: 2 Aufrufe steuerwiki__position):

> Der Nettolohn aus Ziff. 11 des Lohnausweises gehört in **Ziff. 1.1 des Hauptformulars Steuererklärung 2025 Kanton Zürich (Form. 300), Code 100** (Person 1, Haupterwerb).
> 
> - **Eintrag:** Summe der Ziff. 11 aller Lohnausweise der Person 1 im Haupterwerb. Ziff. 11 ist Bruttolohn (Ziff. 8) minus AHV/IV/EO/ALV (Ziff. 9) minus BVG (Ziff. 10.1 und 10.2).
> - **Bund:** Dieselbe Zeile gilt für Staats- und Bundessteuer, es gibt keinen Unterschied.
> - **Beleg:** Den Lohnausweis für jeden Arbeitgeber beilegen (§ 134 Abs. 1 lit. a StG; Wegleitung S. 31).
> - **Beachten:** Erwerbslücken ausdrücklich bezeichnen. Der BVG-Einkauf aus Ziff. 10.2 ist schon abgezogen und darf nicht nochmals in Ziff. 16.1 (Code 280) erscheinen.
> 
> Quelle: `zh-form-300-2025__c0004`. Status ☑️: Fundstelle agent-geprüft, Abnahme noch offen.

## q03

**Frage:** Lohnausweis Feld F ist angekreuzt (Geschäftsauto). Was bedeutet das für den Fahrkostenabzug (SG 2025)?

**Soll (Referenz):** Feld F angekreuzt → kein Fahrkostenabzug für den Arbeitsweg mit Geschäftsfahrzeug (Privatanteil im Lohn, Lohnausweis Ziff. 2.2).

**Antwort des Agenten** (28.6 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__suche, steuerwiki__wert):

> **Kurz:** Ist Feld F angekreuzt, gibt es in SG 2025 **keinen Fahrkostenabzug** für den Arbeitsweg. Das gilt in Form. 4 Ziff. 1.1 (ÖV), 1.2 (Velo) und 1.3 (Auto/Motorrad).
> 
> **Warum:** Feld F bedeutet, dass die Beförderung zwischen Wohn- und Arbeitsort unentgeltlich ist, etwa durch Sammeltransport oder ein vom Arbeitgeber aus geschäftlichen Gründen bezahltes GA. Dem Arbeitnehmer entstehen dann keine Kosten, die man abziehen könnte. Der Maximalabzug von CHF 8'000 (Bund CHF 3'300) ändert daran nichts. (WL SG 2025, sg-wl-2025__c0075; Form. 4 Ziff. 1.1 und 1.3)
> 
> **Der Geschäftswagen ist der Knackpunkt.** Bei einem Geschäftsauto wird der private Nutzen normalerweise als Privatanteil in Lohnausweis Ziff. 2.2 erfasst (0,9 % des Listenpreises pro Monat). Feld F gehört dort eigentlich nicht angekreuzt. Der Abzug ist in beiden Fällen gesperrt, aber die Kombination ist widersprüchlich:
> 
> - **Feld F und Ziff. 2.2 gleichzeitig:** Prüfen Sie den Lohnausweis. Vermutlich ist Feld F falsch gesetzt, und die Arbeitgeberin oder der Arbeitgeber sollte den Ausweis korrigieren. Sonst entsteht eine Frage, die bei einer Veranlagung auffällt.
> - **Nur Ziff. 2.2 (Privatanteil):** Kein Fahrkostenabzug in Form. 4 Ziff. 1.3, die Fahrt ist durch den Privatanteil abgegolten.
> 
> **Einzige Ausnahme:** Wird statt der 0,9-%-Pauschale ein Bordbuch geführt, lassen sich die effektiven Kosten des Arbeitswegs bis zum Maximum abziehen. Dann muss der Privatanteil nach den tatsächlichen Fahrten berechnet werden. Das Bordbuch ist der Beleg dafür.
> 
> **Empfehlung:** Lohnausweis anschauen und die Angaben in Feld F und Ziff. 2.2 abgleichen. Bei einem Widerspruch die Arbeitgeberin oder den Arbeitgeber um eine Korrektur bitten, bevor Sie die Steuererklärung 2025 einreichen.
> 
> **Quellen:** WL SG 2025 (sg-wl-2025__c0075, sg-wl-2025__c0076), StB 39 Nr. 3 (sg-stb-39-3__c0013, sg-stb-39-3__c0018), Form. 4 SG 2025 Ziff. 1.1–1.3. Alle Stellen sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Regel zum Bordbuch ist im Wiki nicht in allen Details belegt. Vor einer verbindlichen Aussage sollte die Fachperson sie gegen StB 39 Nr. 3 prüfen.

## q04

**Frage:** Wie hoch ist der maximale Fahrkostenabzug 2025 in TG (Staatssteuer) und beim Bund, und welcher km-Ansatz gilt für das Auto?

**Soll (Referenz):** TG 2025 Staat max. CHF 6'000 (tg-stg__par-29), Bund max. CHF 3'300 (bund-dbg-2025__art-26); Auto TG gestaffelt 0.60/0.50/0.40 je nach Jahres-km, Bund 0.70.

**Antwort des Agenten** (23.7 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kanton Thurgau (Staatssteuer) 2025**
> 
> - **Maximalbetrag Fahrkosten Wohn-/Arbeitsstätte: CHF 6'000** pro Jahr (StP 29; ☑️ agent-geprüft, Abnahme offen; Quelle: `tg-stg__par-29`).
> - **Km-Ansatz Privatauto: gestaffelt** (`tg-bkv__par-1`; ☑️):
>   - bis 3'000 km: CHF 0.60/km
>   - 3'001–5'000 km: CHF 0.50/km
>   - über 5'000 km: CHF 0.40/km
> 
>   Die Staffel wird stufenweise berechnet, inkl. Parkgebühren. Beispiel laut StP 29: 8'000 km ergeben CHF 4'000.
> - Das Auto ist nur abziehbar, wenn kein öffentliches Verkehrsmittel zumutbar ist. Normalfall ist der ÖV-Abo-Abzug.
> - Bei Privatauto-Berechnung bei 100%-Tätigkeit gelten in der Regel höchstens **225 Arbeitstage** (Wegleitung, `tg-wl-2025__c0003`).
> 
> **Bund (direkte Bundessteuer) 2025**
> 
> - **Maximalbetrag: CHF 3'300** pro Person und Jahr (DBG Art. 26 Abs. 1 lit. a; ☑️).
> - **Km-Ansatz Auto: CHF 0.70/km** einheitlich (BKV Anhang 1), nur ohne zumutbares ÖV. Ab Steuerjahr 2026 gilt CHF 0.75/km, für 2025 nicht.
> - Beim Bund gibt es keine Arbeitstage-Regel.
> 
> **Hinweis zum Bund:** Die ESTV-Wegleitung 2025 (S. 6) nennt noch «maximal 3200 Franken». Das Gesetz (Art. 26 DBG, Fassung 2025) und RS 2-210 nennen 3'300. Nach Rangfolge gilt das Gesetz, also CHF 3'300. Ich habe den Widerspruch nicht abschliessend geklärt. Vor der Abgabe lohnt sich ein Blick in die aktuelle Wegleitung.
> 
> Beim Kanton TG und beim Bund gelten die Limiten getrennt und müssen separat deklariert werden.

## q05

**Frage:** Welcher km-Ansatz für Autos gilt 2026 bei der direkten Bundessteuer?

**Soll (Referenz):** CHF 0.75 pro km (bund-mm-2025-09-11-kalte-progression-2026__c0004; RS 2-215).

**Antwort des Agenten** (21.3 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> Für 2026 gilt bei der direkten Bundessteuer für ein Privatauto **CHF 0.75 pro Fahrkilometer** (2025: 70 Rappen).
> 
> - **Voraussetzung:** Der Ansatz gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist.
> - **Höchstbetrag:** Die Fahrkosten Wohn-/Arbeitsstätte sind insgesamt auf **CHF 3'300** pro Jahr begrenzt. Dieser Betrag gilt unverändert seit 2025.
> - **Grundlage:** Art. 26 DBG und die ESTV-Medienmitteilung vom 11.09.2025 (Quelle: `bund-mm-2025-09-11-kalte-progression-2026__c0004`). Die Mitteilung nennt den Anstieg auf 75 Rappen ausdrücklich.
> - **Künftige Anpassung:** Der Ansatz soll an den TCS-Kilometerpreis gekoppelt werden, kann also nach oben und unten angepasst werden.
> 
> Status: ☑️ agent-geprüft. Die Fundstelle ist geprüft, die fachliche Abnahme steht noch aus.
> 
> Wenn Sie den Kanton nennen, kann ich den kantonalen Ansatz ebenfalls prüfen, da kantonale Formulare eigene Werte führen können.

## q06

**Frage:** Maximaler Säule-3a-Abzug 2025 für eine Arbeitnehmerin mit Pensionskasse? Und für eine Selbständige ohne 2. Säule?

**Soll (Referenz):** Mit 2. Säule CHF 7'258; ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288 (bund-bsv-masszahlen-2025-2026__c0003).

**Antwort des Agenten** (22.8 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Säule 3a 2025 (Bund):**
> 
> - **Arbeitnehmerin mit Pensionskasse:** maximal **CHF 7'258**. Das ist der Höchstabzug bei Zugehörigkeit zur 2. Säule (8 % des oberen BVG-Grenzbetrags). Quelle: `bund-bsv-masszahlen-2025-2026__c0003`.
> - **Selbständige ohne 2. Säule:** **20 % des Erwerbseinkommens, maximal CHF 36'288** (40 % des oberen BVG-Grenzbetrags). Quelle: `bund-bsv-masszahlen-2025-2026__c0003` und `bund-bvv3__art-7`.
> 
> Beide Werte sind agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> Ich habe nur den Bund abgefragt, weil du keinen Kanton genannt hast. Die kantonalen Formulare können für den Abzug eigene Ansätze führen. Sag mir den Kanton und das Steuerjahr, dann prüfe ich ihn.

## q07

**Frage:** Kinderabzug 2025 in AR für ein 10-jähriges Kind – und beim Bund?

**Soll (Referenz):** AR 2025: CHF 7'400 (4.–15. Altersjahr; Anhang 1 StG, ar-stg-anhang-kp__c0001); Bund CHF 6'800 (Art. 35 DBG) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (23.6 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kinderabzug 2025, 10-jähriges Kind**
> 
> | | Kanton AR (Sozialabzug) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | Betrag | **CHF 7'400** | **CHF 6'800** |
> | Grundlage | Art. 38 Abs. 1 lit. a Ziff. 2 (Anhang KP) · `ar-stg-anhang-kp__c0001` | Art. 35 Abs. 1 lit. a DBG · `bund-dbg-2025__art-35` |
> | Status | ☑️ agent-geprüft, Abnahme offen | ☑️ agent-geprüft, Abnahme offen |
> 
> - **AR:** Die Staffelung gilt nach Alter. Ein Kind zwischen Vollendung des 4. und des 15. Altersjahres fällt in die Stufe CHF 7'400. Ab dem 15. Altersjahr bis zur Volljährigkeit (bzw. Ausbildung bis 26) gilt CHF 11'600. Im Formular ist das Ziff. 23.2.
> - **Bund:** Keine Altersstaffel. Der Abzug beträgt CHF 6'800 pro minderjähriges oder in Ausbildung stehendes Kind, unabhängig vom Alter.
> 
> **Zusätzlich beim Bund:** Die Ermässigung des Steuerbetrags um **CHF 263** pro Kind (Art. 36 Abs. 2bis DBG) ist ein eigener Abzug und kommt zum Kinderabzug vom Einkommen hinzu. Die Versicherungsabzug-Zuschläge pro Kind (AR CHF 1'000, Bund CHF 700) sind ebenfalls separat zu betrachten.
> 
> **Offen:** Alle Werte sind agent-geprüft; die Abnahme steht noch aus. Die Formularpositionen für AR habe ich nicht im Detail mit `position` geprüft. Ob eine hälftige Aufteilung bei getrennter Besteuerung zutrifft, hängt vom Sachverhalt ab und habe ich hier nicht geprüft.

## q08

**Frage:** Versicherungsabzug ZH 2025 für ein Ehepaar mit 2 Kindern, beide mit Pensionskasse (Staatssteuer und Bund)?

**Soll (Referenz):** ZH Staat: 5'800 + 2 × 1'300 = 8'400; Bund: 3'700 + 2 × 700 = 5'100 (zh-stg-2025__par-31-t2, bund-dbg-2025__art-33).

**Antwort des Agenten** (26.0 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Kanton ZH 2025: max. CHF 8'400 · Bund 2025: max. CHF 5'100**, jeweils als Höchstbetrag. Der Abzug wird nur bis zur Höhe der tatsächlich bezahlten Prämien gewährt.
> 
> **Berechnung (verheiratet, Beiträge an 2. Säule/3a, 2 Kinder):**
> 
> | | Staatssteuer ZH | Bundessteuer |
> |---|---|---|
> | Ehepaar (mit Vorsorge) | 5'800 | 3'700 |
> | + Kind 1 | 1'300 | 700 |
> | + Kind 2 | 1'300 | 700 |
> | **Maximum** | **8'400** | **5'100** |
> 
> - **Beide mit Pensionskasse** bedeutet, dass der Satz «mit Beiträgen an 2. Säule/3a» gilt, nicht der höhere «ohne Vorsorge»-Satz (8'700 / 5'550).
> - **Pro Kind** kommt ein Zuschlag dazu: kantonal 1'300, bundesweit 700. Diese Zuschläge stehen in Form. 365 Teil B Ziff. 3 (Codes 613–615).
> - **Im Formular:** Ziff. 15 (Code 270) nimmt den kleineren Wert aus den tatsächlich bezahlten Prämien (Form. 365 Teil A) und dem Maximalabzug (Teil B). Staat und Bund werden in getrennten Spalten erfasst.
> 
> **Zu prüfen:**
> - Die Maxima sind alle ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> - Ich habe nicht geprüft, wie die Pensionskassenbeiträge selbst abgezogen werden. Dafür gibt es eine eigene Formularposition, die nicht Teil dieses Versicherungsabzugs ist.
> - Bezahlte Krankenkassen-, Unfall-, Lebens- und Sparzinsen werden zuerst gegen die Maxima gerechnet. Liegen die tatsächlichen Prämien darunter, gilt der tiefere Betrag.
> 
> Quellen: `zh-stg-2025__par-31-t2`, `bund-dbg-2025__art-33-t2`, `bund-dbg-2025__art-33-t5`, `zh-form-300-2025__c0008`, `zh-form-365-2025__c0001`.

## q09

**Frage:** Wie hoch ist der Kinderdrittbetreuungsabzug 2025 im Kanton ZH, und gilt 2026 ein anderer Wert?

**Soll (Referenz):** ZH 2025 CHF 25'000 (StG Nachtrag 127, zh-stg-2025__par-31-t4); 2026 CHF 25'300 (zh-stg-2026__par-31-t3). Die VKP ab 2024 (10'400) ist überholt.

**Antwort des Agenten** (25.3 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Zürich (Staatssteuer), Kinderdrittbetreuungsabzug:**
> 
> - **2025: CHF 25'000 pro Kind**, wenn das Kind das 14. Altersjahr noch nicht vollendet hat, im gleichen Haushalt lebt und die Kosten im direkten Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit stehen. Abzug nur bis zur Höhe der nachgewiesenen Kosten.
> - **2026: CHF 25'300 pro Kind**, sonst gleiche Voraussetzungen. Bei Konkubinat oder alternierender Obhut mit gemeinsamer Sorge gibt es je die Hälfte (2026: CHF 12'650).
> 
> Der Wert steigt also um CHF 300.
> 
> **Bund (direkte Bundessteuer)** ist separat zu deklarieren: CHF 25'800 pro Kind in beiden Jahren, Altersgrenze ebenfalls 14 Jahre.
> 
> **Quellen und Status:**
> - ZH 2025: `zh-stg-2025__par-31-t4` (☑️ agent-geprüft, Abnahme offen)
> - ZH 2026: `zh-stg-2026__par-31-t3` (☑️ agent-geprüft, Abnahme offen)
> - Bund 2025/2026: `bund-dbg-2025__art-33-t7` / `bund-dbg-2026__art-33-t7`
> 
> **Hinweis zu 2025:** Eine ältere VKP-Fassung (ab 2024) nennt noch CHF 10'400. Das Gesetz (StG Nachtrag 127, Stand 1.1.2025) und die Wegleitung 2025 nennen übereinstimmend CHF 25'000. Ich habe den VKP-Wert deshalb als überholt behandelt. Für 2026 erwähnt das Tool ebenfalls die alte 10'400 als überholt.
> 
> Die Formularposition für ZH ist Ziff. 16.6 (Code 376) in beiden Jahren. Soll ich die Rechenregel dazu noch nachschlagen?

## q10

**Frage:** Gibt es im Kanton TG einen Zweiverdienerabzug für die Staatssteuer?

**Soll (Referenz):** Nein, TG kennt keinen kantonalen Zweiverdienerabzug (nur Bund: 50 %, 8'600–14'100).

**Antwort des Agenten** (26.2 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Nein.** Im Kanton Thurgau gibt es für die Staats- und Gemeindesteuer keinen Zweiverdienerabzug. Den Abzug gibt es nur bei der direkten Bundessteuer.
> 
> Ich habe das Steuerjahr 2025 geprüft, da keines angegeben war. Die Praxis StP 34 Nr. 25 gilt für 2025, 2026 und 2027 und sagt ebenfalls, dass das Gesetz über die Staats- und Gemeindesteuern keinen Zweiverdienerabzug vorsieht.
> 
> - **Kanton TG (Staats- und Gemeindesteuer):** kein Abzug. Quelle: WL TG 2025, S. 23, Ziff. 18 (`tg-wl-2025__c0104`), und StP 34 Nr. 25 (`tg-stp-34-25__c0001`).
> - **Bund (direkte Bundessteuer, Art. 33 Abs. 2 DBG):** 50 % des niedrigeren Erwerbseinkommens, mindestens CHF 8'600, höchstens CHF 14'100 (2025). Das ist ☑️ agent-geprüft, die Abnahme steht noch aus. Quelle: `bund-dbg-2025__art-33-t6`.
> 
> Im Formular TG 2025 steht der Zweiverdienerabzug unter Ziff. 18 (Code 356) und wird nur für den Bund geltend gemacht. Den Staatssteuerwert setzt du dort nicht ein. Falls du eine Position für die Erklärung brauchst, kann ich `position tg 2025 18` abrufen.

## q11

**Frage:** SG 2025: Pauschale für übrige Berufskosten? Wie wird sie berechnet?

**Soll (Referenz):** SG 2025: CHF 700 + 10 % des Nettolohns, max. CHF 2'400 (Art. 21 StV SG, WL SG 2025).

**Antwort des Agenten** (23.8 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Pauschale für übrige Berufskosten, SG 2025 (Kanton St. Gallen)**
> 
> **Berechnung:** Fr. 700 + 10 % der Nettoeinkünfte (Nettolohn), höchstens Fr. 2'400. Ein Minimum gibt es im Kanton SG nicht.
> 
> - **Nettoeinkünfte** = Bruttoeinkünfte abzüglich AHV/IV/EO/ALV/UV- und BVG-Beiträge, ohne Einkäufe.
> - **Beispiel:** Nettolohn Fr. 50'000 → 700 + 5'000 = **Fr. 5'700**, gedeckelt auf Fr. 2'400. Der Höchstbetrag wird also bei einem Nettolohn ab ca. Fr. 17'000 erreicht.
> - **Nachweis:** Höhere tatsächliche Kosten können nachgewiesen werden (Art. 21 StV SG). Dann gilt aber: Werden «übrige» Berufsauslagen inkl. Arbeitszimmer geltend gemacht und übersteigen die Pauschale, müssen alle tatsächlichen Aufwendungen belegt werden (StB 39 Nr. 1).
> 
> **Im Formular SG 2025:** Ziff. 10.1 (Person 1, Code 438) bzw. Ziff. 10.2 (Person 2, Code 488) für Berufskosten bei unselbständiger Erwerbstätigkeit.
> 
> **Bund (direkte Bundessteuer), separat zu deklarieren:** 3 % des Nettolohns, mindestens Fr. 2'000, höchstens Fr. 4'000. Es gibt keinen fixen Sockelbetrag.
> 
> **Status:** Die SG-Werte (Satz 10 %, Fix Fr. 700, Max. Fr. 2'400) sind agent-geprüft: Fundstelle geprüft, Abnahme offen. Quelle: Art. 21 StV SG und Wegleitung SG 2025 Ziff. 10.3 (Chunk `sg-wl-2025__c0080`).
> 
> **Nicht verwechseln:** Bei einer *Nebenerwerbstätigkeit* gilt laut StB 39 Nr. 9 eine andere Regel: Pauschale 20 %, mindestens Fr. 800, höchstens Fr. 2'400. Ich habe diese Regel nur aus den Suchtreffern, nicht aus dem vollen Chunk geprüft.
> 
> Wenn du mir den Nettolohn des Mandanten nennst, rechne ich den konkreten Betrag aus.

## q12

**Frage:** Pauschalabzug Liegenschaftsunterhalt in AR für ein 8-jähriges Einfamilienhaus – und wie in ZH?

**Soll (Referenz):** AR: 10 % (Gebäude bis 10 Jahre) bzw. 20 % des Bruttoertrags, nur bis Bruttomietertrag 100'000 (Art. 25 StV AR, MB 03); ZH: einheitlich 20 % ohne Altersstaffel (ZStB 30.2).

**Antwort des Agenten** (30.6 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Annahme:** Steuerjahr 2025, da keines angegeben war. Wohnsitz vermutlich AR bzw. ZH; die Frage nennt keinen Kanton, daher beide.
> 
> **AR (Staats- und Gemeindesteuer)**
> - **10 %** des Bruttomietertrags bei Gebäuden bis 10 Jahre alt, 20 % bei älteren Gebäuden. Ihr 8-jähriges Haus fällt also unter 10 %. (ar-mb-03__c0004, Art. 25 StV AR · ☑️ agent-geprüft, Abnahme offen)
> - Voraussetzung: Der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes darf CHF 100'000 nicht übersteigen.
> - Das Alter bestimmt sich nach dem Stichtag für die Vermögenssteuer. Die Quelle nennt den Stichtag nicht genauer.
> - Wahlrecht zwischen Pauschale und effektiven Kosten in jeder Periode, je Gebäude.
> - Bei einem selbstbewohnten Haus ist der Eigenmietwert die Bemessungsgrundlage (Art. 25 Abs. 1 StV). Für den Eigenmietwert gilt zusätzlich der Selbstnutzungsabzug von 20 % (ar-wl-2025__c0001).
> 
> **ZH (Staats- und Gemeindesteuer)**
> - **20 %** des Brutto-Mietertrags bzw. Mietwerts. Es gibt keine Altersstaffelung, Ihr Haus wird also mit 20 % abgezogen. (zh-zstb-30-2__c0002 · ☑️ agent-geprüft, Abnahme offen)
> - Wahl pro Liegenschaft und Steuerperiode. Nicht anwendbar bei vorwiegend geschäftlich genutzten Liegenschaften.
> - Beim Eigenmietwert gibt es keinen prozentualen Pauschal-Einschlag. Er richtet sich nach der Weisung 2009, die für 2025 gilt (zh-weisung-liegenschaften-2009__c0033).
> 
> **Bund (zum Vergleich)**
> - Gilt gleich wie AR: **10 %** bei Gebäuden bis 10 Jahre alt zu Beginn der Steuerperiode (bund-lkv__art-5). Der Bund wird separat deklariert.
> 
> **Ergebnis für Ihr 8-jähriges Haus**
> 
> | | Kanton | Bund |
> |---|---|---|
> | AR | 10 % (Mietertrag-Limite CHF 100'000 beachten) | 10 % |
> | ZH | 20 % | 10 % |
> 
> Die Sätze sind aus den Merkblättern und Wegleitungen übernommen und als «agent-geprüft» markiert. Vor einer Abgabe sollte die Abnahme durch die Fachperson erfolgen. Falls Sie mir Kanton, Steuerjahr und Wohnsitz-Stichtag nennen, prüfe ich die Ziffer im Formular (`position ar 2025 15` bzw. `position zh 2025 <ziffer>`).

## q13

**Frage:** TG: Welcher Einschlag gilt auf dem Eigenmietwert der selbstbewohnten Liegenschaft am Wohnsitz (Kanton vs. Bund)?

**Soll (Referenz):** TG: Abzug 40 % Kanton, 20 % Bund für dauernd selbstbewohntes Eigentum am Wohnsitz (tg-stg__par-23; WL TG 2025).

**Antwort des Agenten** (30.9 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> Die Antwort hängt am Kanton, den ich noch nicht kenne. Welcher ist es: AR, SG, TG oder ZH? Und soll ich 2025 oder 2026 nehmen?
> 
> **Bund (direkte Bundessteuer):** Der Eigenmietwert ist steuerbar nach Art. 21 Abs. 1 lit. b DBG. Abs. 2 sagt, seine Festsetzung erfolge «unter Berücksichtigung der ortsüblichen Verhältnisse und der tatsächlichen Nutzung der am Wohnsitz selbstbewohnten Liegenschaft» (Fundstelle: `bund-dbg-2025__art-21`). Das Wiki enthält keinen eigenen Bundes-Prozentsatz für den Eigenmietwert, den ich als «Einschlag» nennen könnte. Ich habe das aber nicht abschliessend geprüft, deshalb keine Zahl von mir.
> 
> **Kanton:** Die Bewertung wird kantonal vorgenommen und hängt vom Kanton ab. Ohne Kanton kann ich dazu keinen Wert nennen. Sobald Sie den Kanton und das Jahr angeben, suche ich den kantonalen Ansatz gezielt nach.
> 
> **Hinweis zur Reform:** Der Bundesrat hat am 1. April 2026 beschlossen, die Abschaffung der Eigenmietwertbesteuerung auf den 1. Januar 2029 in Kraft zu setzen. Für 2026 bleibt der Eigenmietwert steuerbar (`bund-mm-eigenmietwert-abschaffung__c0002`). Die Kantone können dann eine Objektsteuer auf Zweitliegenschaften einführen.

## q14

**Frage:** Bis wann kann ein Treuhänder im Kanton TG für seine Mandanten Fristerstreckung erhalten?

**Soll (Referenz):** Gewerbsmässige Treuhänder für Mandanten bis 31.12. des Deklarationsjahres (StP 155 Nr. 2).

**Antwort des Agenten** (28.3 s · Tools: 5 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> Ein gewerbsmässiger Treuhänder oder Steuerberater kann im Kanton Thurgau für seine Mandanten **längstens bis 31. Dezember des Deklarationsjahres** eine Fristerstreckung beantragen.
> 
> Da Sie kein Steuerjahr genannt haben, habe ich 2025 verwendet. Für das Steuerjahr 2025 ist das Deklarationsjahr 2026, die Frist also der **31. Dezember 2026**. Heute ist der 9. November 2026, für Ihre Mandanten bleiben also noch rund sieben Wochen.
> 
> **Einordnung (Quelle: StP 155 Nr. 2, Chunks `tg-stp-155-2__c0002` und `c0001`, Status ☑️ agent-geprüft, Abnahme offen):**
> - **Gesuch an:** das Gemeindesteueramt, das darüber entscheidet.
> - **Private (Standardfall):** Das erste Gesuch wird grundsätzlich bis 30. September des Deklarationsjahres gutgeheissen. Weitere Gesuche gibt es nur in begründeten Fällen bis 30. November.
> - **Über 30. November hinaus:** Weitere Gesuche werden nur bei glaubhaft gemachten ausserordentlichen Gründen gewährt. Allgemeine Hinweise wie berufliche Überlastung oder fehlende Unterlagen reichen nicht aus.
> - **Gebühren:** Für natürliche Personen nennen die Quellen keine Gebühr. Für juristische Personen gilt eine Kanzleigebühr von Fr. 30 je weiterem Gesuch.
> 
> Das Wiki enthält keine Angaben zur Gebühr für das Treuhänder-Gesuch bei natürlichen Personen. Ob das Gemeindesteueramt eine Gebühr erhebt, kann ich daher nicht bestätigen.
> 
> Wenn Sie für 2026 fragen, sagen Sie mir das Steuerjahr, dann prüfe ich die Frist für dieses Jahr separat.

## q15

**Frage:** ZH: Bis wann ist die Steuererklärung 2025 einzureichen und wie lange wird höchstens Fristerstreckung gewährt?

**Soll (Referenz):** Einreichung bis 31.03.2026; Fristerstreckung längstens bis 30. November (ZStB 132.1 / WL ZH 2025).

**Antwort des Agenten** (25.7 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Kanton Zürich, Steuerjahr 2025 (natürliche Personen):**
> 
> - **Ordentliche Einreichefrist: 31. März 2026.** Die Steuererklärung 2025 musste bis dahin eingereicht werden (online oder Scan-Center). Quelle: WL ZH 2025, `zh-wl-2025__c0017` · ☑️ agent-geprüft, Abnahme offen.
> - **Höchstens bis 30. November 2026** wird eine Fristerstreckung gewährt. Gesuche müssen vor Ablauf der Frist (31.3.2026) beim Gemeindesteueramt eingereicht werden. Rechtzeitige Gesuche werden entsprechend dem Gesuch bewilligt, längstens bis 30. November des Folgejahres. Ein erstes Gesuch gilt ohne gegenteiligen Entscheid als stillschweigend bewilligt. Darüber hinaus gibt es nur ausserordentliche Gründe; berufliche Belastung des Vertreters genügt nicht. Quelle: ZStB 132.1, `zh-zstb-132-1__c0024` · ☑️ agent-geprüft, Abnahme offen.
> - **Selbständige und Ausserkantonale:** Die Frist wird von Amtes wegen bis 30. September erstreckt (laut selber Quelle).
> - **Mahnfristen** sind nicht erstreckbar.
> 
> **Was das für heute (9. November 2026) heisst:** Die Frist 31.3.2026 ist abgelaufen. Eine Erstreckung bis 30.11.2026 ist nur möglich, wenn vor dem 31.3.2026 ein Gesuch eingereicht wurde. Ohne Gesuch gilt die Erklärung als verspätet; es folgt das Mahnverfahren bei Nichtabgabe (ZStB 132.1, `zh-zstb-132-1__c0032`). Prüfen Sie daher zuerst, ob ein Gesuch oder eine Bewilligung vorliegt. Falls ja, ist 30.11.2026 die späteste Frist, also in gut drei Wochen.
> 
> **Hinweis:** Die Kosten einer Fristerstreckung sind in den Quellen nicht genannt. Die Fassung ZStB 132.1 gilt laut Wiki bis 31.12.2025 und ab 2026 in neuer Fassung; die Fristregeln für 2025 sind dort gleichlautend. Bei einem konkreten Fall lohnt sich eine Rückfrage beim Gemeindesteueramt.

## q16

**Frage:** AR: Was kostet die zweite Fristverlängerung?

**Soll (Referenz):** CHF 25 (erste Verlängerung kostenlos, jede weitere CHF 25; MB 18 / WL AR 2025).

**Antwort des Agenten** (24.4 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__wert):

> **Die zweite Fristverlängerung kostet im Kanton Appenzell Ausserrhoden CHF 25.** Die erste ist kostenlos.
> 
> - **Steuerjahr:** Du hast kein Jahr genannt, also habe ich 2025 verwendet. Die Quellen decken auch 2026 ab, dort gilt der Betrag laut Fundstelle ebenfalls, aber ich habe das nicht separat geprüft.
> - **Quellen:** Die Wegleitung AR 2025 (`ar-wl-2025__c0012`) sagt, dass nur die erste Fristverlängerung kostenlos ist und jede weitere CHF 25 kostet. Das Merkblatt 18 (`ar-mb-18__c0001`) nennt für Fristverlängerungen im Wiederholungsfall ebenfalls Fr. 25. Die Verfahrensgebühren in Art. 59a StV AR stimmen damit überein.
> - **Status:** ☑️ agent-geprüft. Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> - **Bund:** Die direkte Bundessteuer hat keine eigene Fristerstreckung. Sie läuft über die kantonale Erklärung.
> 
> Wenn du mir sagst, ob es um 2025 oder 2026 geht, prüfe ich das Jahr gezielt nach.

## q17

**Frage:** Krankheitskosten SG 2025: Ab welchem Selbstbehalt sind sie abziehbar – und beim Bund?

**Soll (Referenz):** SG: Selbstbehalt 2 % (Art. 46 StG SG); Bund: 5 % (Art. 33 Abs. 1 lit. h DBG, KS 11).

**Antwort des Agenten** (23.3 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Krankheitskosten 2025: Selbstbehalt in SG und beim Bund**
> 
> **Kanton St. Gallen (2025): 2 % der Nettoeinkünfte**
> - Abziehbar ist der Teil der Krankheits- und Unfallkosten, der 2 % der Nettoeinkünfte übersteigt. Massgebend ist das Nettoeinkommen aus Ziff. 20.
> - Behinderungsbedingte Kosten sind ohne Selbstbehalt abziehbar.
> - Eine pauschale Diät (Zöliakie) wird mit Fr. 2'500 angesetzt.
> - Quelle: sg-stg-2025__art-46. Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> - Im Formular steht dies in Ziff. 21.1 (Krankheits- und Unfallkosten). Die genaue Rechenregel bei Code 650 habe ich nicht vollständig gesehen. Für die Zeile mit dem Selbstbehalt-Code prüfe ich sie mit `position sg 2025 21.1`, falls du es brauchst.
> 
> **Bund (direkte Bundessteuer 2025): 5 %**
> - Abziehbar ist der Teil, der 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigt.
> - Behinderungsbedingte Kosten (BehiG) sind ohne Selbstbehalt abziehbar.
> - Quelle: bund-dbg-2025__art-33-t3. Status: ☑️ agent-geprüft (Abnahme offen).
> - Praxis 2025/2026 ist die ESTV-KS 11 vom 31.08.2005. Das KS 11a (publiziert 26.05.2026) gilt laut seiner Ziff. 7 erst ab Steuerperiode 2027, also nicht für 2025.
> 
> **Wichtig:** Die Basis unterscheidet sich. SG rechnet mit 2 % des Nettoeinkommens, der Bund mit 5 % der um Aufwendungen verminderten Einkünfte. Der Selbstbehalt ist deshalb je Steuer separat zu berechnen, die Beträge sind nicht identisch.

## q18

**Frage:** PK-Einkauf CHF 20'000 wurde über den Lohn abgezogen (Lohnausweis Ziff. 10.2). Darf er nochmals in der Steuererklärung abgezogen werden?

**Soll (Referenz):** Nein – BVG-Einkauf über Lohnabzug (Lohnausweis Ziff. 10.2) ist bereits im Nettolohn berücksichtigt; nur direkt bezahlte Einkäufe separat abziehen.

**Antwort des Agenten** (34.6 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Kurz: nein, nicht doppelt.** Wenn der Einkauf vom Lohn abgezogen und über den Lohnausweis gemeldet wurde, wird er in der Steuererklärung über die Lohnausweis-Werte berücksichtigt und darf kein zweites Mal als Einkauf eingetragen werden.
> 
> Grundlage (Bund, Steuerjahre 2025–2027):
> - **KS W03-001, Ziff. 3.3** (`bund-ks-w03-001__c0009`, ✅ Fundstelle geprüft): Übernimmt der Arbeitgeber Arbeitnehmer-Einlagen für den Einkauf, gehören sie zum massgebenden Bruttolohn und sind im Lohnausweis separat aufzuführen. Nur so kann der Arbeitnehmer den Einkauf steuerlich geltend machen.
> - **MB 21 EDP, Ziff. 1, Rz 12** (`bund-mb-21edp__c0006`): Alle vom Lohn abgezogenen Beiträge an die 2. Säule stehen im Lohnausweis. Nur Einkäufe, die der Versicherte selbst an die Vorsorgeeinrichtung überweist, gehören ins Formular 21.
> 
> Der Einkauf ist also schon im Lohnausweis erfasst. Wenn Sie ihn zusätzlich von Hand als Einkauf eintragen, wäre das der Doppelabzug, den Sie befürchten.
> 
> **Offen bleibt der genaue Abzug:** Die Position im kantonalen Formular und die Höchstbeträge für Einkäufe unterscheiden sich je Kanton. Dafür brauche ich:
> 1. **Kanton** (Wohnsitz am 31.12.): AR, SG, TG oder ZH?
> 2. **Steuerjahr**: 2025 (Annahme, falls Sie nichts sagen)?
> 
> Danach prüfe ich die Formularposition und die kantonale Limite mit Fundstelle.

## q19

**Frage:** Weiterbildungskosten CHF 15'000 (ZH, 2025), Arbeitgeber hat nichts bezahlt. Wie viel ist abziehbar (Kanton/Bund)?

**Soll (Referenz):** ZH Staat max. CHF 12'400 (zh-stg-2025__par-31-t4); Bund max. CHF 13'000 (bund-dbg-2025__art-33-t4).

**Antwort des Agenten** (25.0 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Zürich 2025: CHF 12'400 abziehbar (Staatssteuer). Bund: CHF 13'000 (direkte Bundessteuer).**
> 
> Da der Arbeitgeber nichts bezahlt hat, sind die gesamten CHF 15'000 selbst getragen. Die Obergrenze greift also in beiden Blöcken:
> 
> | | Staatssteuer ZH | Bundessteuer |
> |---|---|---|
> | Selbst getragene Kosten | 15'000 | 15'000 |
> | Höchstbetrag | 12'400 | 13'000 |
> | **Abzug** | **12'400** | **13'000** |
> 
> **Bedingungen:**
> - Die Person hat einen Abschluss auf Sekundarstufe II oder hat das 20. Altersjahr vollendet, und die Ausbildung ist nicht die erste Ausbildung bis zum Sek.-II-Abschluss.
> - Massgebend ist das Jahr der Fälligkeit bzw. Zahlung, nicht der Kursbesuch.
> 
> **Formular:** Ziff. 16.2 «Berufsorientierte Aus- und Weiterbildungskosten» (Code 292), Hilfsblatt Form. 367 (Codes 2900/2901 bzw. 2920 für Person 1). Die Beträge gehen je in die Spalte Staatssteuer bzw. Bundessteuer. Auf Verlangen beilegen.
> 
> **Status:** Die Beträge sind agent-geprüft (Fundstelle geprüft, Abnahme offen).
> - ZH: Form. 300 Ziff. 16.2 / Wegleitung ZH 2025, `zh-stg-2025__par-31-t4` und `zh-wl-2025__c0093`
> - Bund: `bund-dbg-2025__art-33-t4`

## q20

**Frage:** Spenden CHF 50 an eine gemeinnützige Organisation (TG 2025) – abziehbar?

**Soll (Referenz):** Nein – TG: Zuwendungen nur abziehbar, wenn sie CHF 200 übersteigen (StG TG § 34 Abs. 1 Ziff. 11); Bund: ab CHF 100.

**Antwort des Agenten** (27.7 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__position):

> **Nein, mit CHF 50 allein ist nichts abziehbar.** Für 2025 gelten im Kanton Thurgau und beim Bund Mindestbeträge für freiwillige Zuwendungen:
> 
> - **Kanton TG:** Es wird nur der Betrag abgezogen, der die Summe aller Zuwendungen des Jahres um CHF 200 übersteigt. Bei CHF 50 ergibt das 0.
> - **Bund:** Erst ab einer Jahressumme von CHF 100 wird abgezogen, dann aber der volle Betrag ohne Selbstbehalt. Bei CHF 50 ergibt das ebenfalls 0.
> 
> Die CHF 50 zählen aber zur Jahressumme. Hätten Sie 2025 weitere Zuwendungen an steuerbefreite Institutionen, wären sie mitzurechnen. Beispiel: Bei Zuwendungen von insgesamt CHF 250 an Institutionen mit öffentlichem oder gemeinnützigem Zweck ergäbe sich kantonal ein Abzug von CHF 50 (250 − 200).
> 
> **Weitere Voraussetzungen**, falls die Summe später relevant wird:
> - Die Empfängerin muss in der Schweiz ansässig und von der Steuer befreit sein. Die Liste der Steuerverwaltung TG prüfen Sie, bevor Sie etwas abziehen.
> - Sammelvermerke wie «Spenden an diverse Organisationen» werden nicht anerkannt. Die Zuwendung muss einzeln und mit Name und Sitz der Institution im Formular 6, Spalte «gemeinnützige oder öffentliche Zwecke», stehen.
> - Belege braucht es ab CHF 1'000 pro Zuwendung. Darunter nur auf Verlangen.
> - Keine Abzüge für religiöse, wohltätige, kulturelle, gesellige oder sportliche Zwecke.
> 
> **Formularposition:** TG 2025, Ziffer 23.2, Formular 6, Code 366. Der Kanton führt den Betrag in der linken Spalte, der Bund in der rechten.
> 
> **Quellen:** TG StP 34 Nr. 23 (tg-stp-34-23), Wegleitung TG 2025 Ziff. 23.2 (tg-wl-2025__c0220), Formular 6 (tg-form-06-2025__c0002). Die Werte sind agent-geprüft, die Abnahme durch eine Fachperson steht noch aus.

## q21

**Frage:** Was ändert sich 2026 bei der Säule 3a (Einkauf) und wo wird das im ZH-Formular 2026 eingetragen?

**Soll (Referenz):** Ab 2026 Einkauf (Nachzahlung) Säule 3a für Beitragslücken ab 2025 (max. 7'258 pro Einkaufsjahr, BVV 3 Art. 7a, KS 18a); ZH-Formular 2026: Ziff. 14.3 (Code 264, Detailfelder 276/278).

**Antwort des Agenten** (27.8 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__suche):

> **Neu 2026: Einkauf in die Säule 3a für Beitragslücken**
> 
> - **Was:** Ab Steuerperiode 2026 können Sie zusätzlich zu den ordentlichen 3a-Beiträgen Beitragslücken in der 3a-Vorsorge einkaufen. Berechtigt sind Lücken, die **ab 1.1.2025** entstanden sind, innerhalb der letzten zehn Jahre.
> - **Voraussetzungen:** In den Lückenjahren wurden AHV/IV/EO-Beiträge geleistet, und im Einkaufsjahr wurde der volle ordentliche Maximalbeitrag einbezahlt.
> - **Höchstbetrag:** Der Einkauf ist auf die Summe der Lücken begrenzt und in jedem Fall auf **CHF 7'258** pro Person beschränkt.
> - **Praktische Folge für 2026:** Faktisch ist nur die Lücke 2025 einkaufbar, da frühere Lücken ausgeschlossen sind.
> - **Bund:** Der Höchstbetrag ist gleich (CHF 7'258). Der Einkauf wird in der Bundessteuer-Spalte separat erfasst.
> 
> **Eintrag im ZH-Formular 2026**
> 
> - **Ziff. 14.3 «Einkauf Säule 3a»** (neu ab 2026):
>   - Person 1: Code **276**
>   - Person 2: Code **278**
>   - Hauptkolonne: Code **264**
>   - Der Betrag wird je Person als Minimum aus Einkauf, Summe der Lücken und CHF 7'258 berechnet.
> - **Ziff. 14.1 / 14.2** bleiben für die ordentlichen Beiträge (Codes 260/261, effektiv 262/263). Der Einkauf wird nicht dort eingetragen.
> - **Belege:** Einkaufsbescheinigung der 3a-Einrichtung, Nachweis des vollen ordentlichen Maximalbeitrags im Einkaufsjahr und Nachweis der AHV/IV/EO-Beiträge in der Lücke.
> 
> **Einschränkungen**
> 
> - Das reguläre Formular und die Wegleitung ZH 2026 sind laut Wiki-Stand (09.11.2026) noch nicht publiziert. Die Zuordnung stützt sich auf die Fassung für unterjährige Steuerpflicht (Form. 300 UJ). Ziffern und Codes sollten am definitiven Formular geprüft werden.
> - Der Status der Werte ist ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen. Die Rechtsgrundlage ist nur aus der Wegleitung belegt; der Artikel in BVV 3 wurde nicht selbst geprüft.
> 
> Quellen: `zh-form-300-2026-uj__c0008` (Ziff. 14.1–14.3), `zh-wl-2026-uj__c0077` (Einkauf, max. CHF 7'258), `bund-wl-2a-2026__c0051` (Bund).

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (34.5 s · Tools: 7 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurz:** Die Verrechnungssteuer auf inländischen Dividenden wird **nicht** über die Steuererklärung zurückgefordert. Die Rückerstattung läuft separat über die Eidgenössische Steuerverwaltung (ESTV) mit **Formular 25**. In der Steuererklärung erscheinen die Kapitalanlagen im **Wertschriftenverzeichnis**.
> 
> **Rückforderung (Bund)**
> - Die Rückerstattung ist mit Formular 25 direkt bei der ESTV, Abteilung Rückerstattung, 3003 Bern, zu beantragen. Das steht im Formular 13 2025 (`bund-form-13-2025__c0001`).
> - Ein Anspruch besteht nur, wenn die Verrechnungssteuer auf dem Ertrag tatsächlich abgezogen wurde. Zusätzlich gilt: Wer nicht Empfänger der Dividende ist, etwa bei Short-Positionen, hat keinen Anspruch. Dazu KS VST 21 Ziff. 3 (`bund-ks-vst-21__c0006`).
> 
> **Wo der Anspruch ausgewiesen wird**
> - Die Kapitalanlagen mit Verrechnungssteuer stehen im Wertschriftenverzeichnis, Teil I (Formular 13, Abschnitt «Kapitalanlagen, deren Ertrag der Verrechnungssteuer unterliegt», `bund-form-13-2025__c0001`). Das Formular 13 ist allerdings das Verzeichnis für juristische Personen. Für natürliche Personen gilt das kantonale Wertschriftenverzeichnis, und dort fehlt mir noch die Position.
> - Die Verrechnungssteuer wird dort nicht als Forderung ausgewiesen, die Sie in der Steuererklärung geltend machen. Ob und wie der Abzug in der kantonalen Erklärung verbucht wird, habe ich nicht belegt.
> 
> **Nicht verwechseln**
> - Die **DA-1** (`bund-form-da1-2025__c0006`) betrifft ausländische Quellensteuern, nicht die Schweizer Verrechnungssteuer. Sie ist hier nicht einschlägig.
> 
> **Offen**
> - Für die Position im kantonalen Wertschriftenverzeichnis brauche ich den **Kanton** (AR, SG, TG oder ZH) und das **Steuerjahr**. Ich nehme 2025 an, wenn Sie nichts anderes sagen. Sagen Sie mir Kanton und Jahr, dann suche ich die Position und die Ziffern.

## q23

**Frage:** Vergleiche den Versicherungsabzug 2025 für Alleinstehende ohne Kinder in AR, SG, TG, ZH und beim Bund.

**Soll (Referenz):** Alleinstehend ohne Kinder 2025 (mit 2. Säule/3a): AR 2'700 · SG 3'400 · TG 3'500 · ZH 2'900 · Bund 1'800.

**Antwort des Agenten** (30.2 s · Tools: 6 Aufrufe steuerwiki__vergleich, steuerwiki__zeige):

> **Versicherungsabzug 2025, alleinstehend, ohne Kinder** (Steuerjahr 2025, Abzug für Versicherungsprämien und Sparzinsen)
> 
> | Kanton / Bund | Mit Beiträge an 2. oder 3a-Säule | Ohne Beiträge an 2. oder 3a-Säule | Fundstelle |
> |---|---|---|---|
> | **Bund** | CHF 1'800 | CHF 2'700 | Art. 33 Abs. 1 lit. g DBG (bund-dbg-2025__art-33-t2) |
> | **ZH** (Staatssteuer) | CHF 2'900 | CHF 4'350 | WL ZH 2025, Ziff. 15 (zh-wl-2025__c0084) |
> | **SG** | CHF 3'400 | CHF 3'900 | Art. 45 StG SG (sg-stg-2025__art-45-t2) |
> | **TG** | CHF 3'500 | CHF 3'500 | § 34 Ziff. 9 StG TG (tg-stg__par-34-t3) |
> | **AR** | CHF 2'700 | CHF 2'700 | Art. 35 lit. g StG AR (ar-stg__art-35-t2) |
> 
> **Einordnung**
> 
> - **Höchster Abzug:** Kanton ZH (CHF 4'350 ohne 2./3a-Säule). **Tiefster:** Bund (CHF 1'800 mit Beiträgen).
> - **Zwei Varianten:** Die Abzugshöhe hängt davon ab, ob Beiträge an die 2. Säule oder die Säule 3a geleistet wurden. Im Bund, in ZH und in SG gibt es zwei Beträge. Im Bund und in ZH steigt der Abzug ohne diese Beiträge deutlich. In SG greift der Zuschlag von CHF 500 nur, wenn keine Beiträge nach lit. d und e abgezogen werden.
> - **TG und AR:** Hier gibt es nur einen festen Betrag, unabhängig von Vorsorgebeiträgen.
> - **Kanton vs. Bund:** Die Kantone rechnen mit eigenen Beträgen. Der Bundesabzug gilt nur für die direkte Bundessteuer.
> 
> **Status:** Alle Werte sind agent-geprüft (☑️). Die Fundstellen für TG, AR und SG sowie der Bund-Gesetzestext und die ZH-Wegleitung habe ich im Wortlaut geöffnet. Die Bund-Variante ohne Vorsorge (CHF 2'700) stammt aus der Vergleichstabelle (bund-rs-2-210__c0006), den Chunk habe ich nicht separat geöffnet.

## q24

**Frage:** Steuerfreie Vermögensbeträge (Sozialabzüge) 2025 in SG für ein Ehepaar mit einem minderjährigen Kind?

**Soll (Referenz):** SG 2025: 150'000 (Ehepaar) + 20'000 pro minderjähriges Kind = 170'000 (sg-stg-2025__art-64).

**Antwort des Agenten** (24.3 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Antwort: CHF 170'000** (SG, Steuerjahr 2025)
> 
> | Position | Betrag | Fundstelle | Status |
> |---|---|---|---|
> | Ehepaar (gemeinsam steuerpflichtig) | CHF 150'000 (2 × 75'000) | sg-wl-2025__c0118 | ☑️ |
> | Pro minderjähriges Kind | CHF 20'000 | sg-stg-2025__art-64 (Abs. 1 a) | ☑️ |
> 
> - Die Sozialabzüge stehen im Formular SG 2025 unter Ziff. 36 (Vermögen). Das Kind muss unter elterlicher Sorge bzw. Obhut stehen und für einen Kinderabzug berücksichtigt werden können.
> - Die Beträge stammen aus dem Steuergesetz (Art. 64 StG SG) und der Wegleitung. Sie sind agent-geprüft, die Abnahme durch eine Fachperson steht noch aus.
> - Die 20'000 pro Kind sind kantonale Sozialabzüge. Beim Bund gibt es keine Vermögenssteuer und daher keinen entsprechenden Abzug.

## q25

**Frage:** Welcher Verzugszins gilt 2026 für die direkte Bundessteuer?

**Soll (Referenz):** 4.00 % (RS 2-215, bund-rs-2-215__c0010/c0011).

**Antwort des Agenten** (22.7 s · Tools: 1 Aufrufe steuerwiki__wert):

> Für die direkte Bundessteuer gilt 2026 ein **Verzugs- und Rückerstattungszins von 4,00 %** (2025: 4,50 %).
> 
> Quelle: `bund-rs-2-215__c0010` (Verordnung-Tabelle „Verzugs- und Rückerstattungszins 4,50 → 4,00“). Status: ☑️ agent-geprüft, Abnahme offen.
> 
> Zum Vergleich, ebenfalls aus derselben Fundstelle:
> - **Vergütungszins** für Vorauszahlungen: 0,00 % (2025: 0,75 %)
> 
> Der Verzugszins gilt unabhängig vom Kanton. Wenn du mir sagst, in welchem Kanton (AR, SG, TG oder ZH) die Person wohnt, kann ich zusätzlich den kantonalen Wert prüfen, weil die Kantone eigene Ansätze führen können.

## q26

**Frage:** Wann wird der Eigenmietwert abgeschafft und gilt das schon für 2026?

**Soll (Referenz):** Abschaffung per 1.1.2029 (Bundesratsbeschluss 01.04.2026); für 2025–2028 gilt bisheriges Recht – 2026 also noch Eigenmietwert.

**Antwort des Agenten** (26.8 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurz:** Der Eigenmietwert wird per **1. Januar 2029** abgeschafft. **2026 gilt er noch**, also wird er für das Steuerjahr 2026 wie bisher besteuert.
> 
> - **Bund:** Der Bundesrat hat am 1. April 2026 beschlossen, die Reform der Wohneigentumsbesteuerung auf den 1.1.2029 in Kraft zu setzen. Ab dann entfällt auf selbstgenutztem Wohneigentum die Besteuerung des Eigenmietwerts. (Fundstelle: `bund-mm-eigenmietwert-abschaffung__c0002`, Medienmitteilung Bundesrat · Status ☑️ agent-geprüft, Abnahme offen)
> - **Kompensation:** Die Kantone können zur finanziellen Kompensation eine Objektsteuer auf Zweitliegenschaften einführen. Ob und wie das geschieht, ist kantonal unterschiedlich.
> - **Für 2026:** Der Eigenmietwert bleibt steuerbar. Bei der Liegenschaftspauschale gilt das Gebäudealter am Anfang der Steuerperiode (1.1.2026): bis 10 Jahre alt → 10 %, mehr als 10 Jahre → 20 % (Fundstelle: `bund-lkv__art-5`, ☑️). Im Grenzfall das Baujahr bzw. den Bezug genau prüfen.
> 
> Die kantonalen Eigenmietwert-Regeln und Bewertungen für 2026 kann ich nur für AR, SG, TG oder ZH nennen. Sag mir, für welchen Kanton du fragst, dann prüfe ich das für 2026 gezielt.

## q27

**Frage:** Zitiere die Regel zum Abzug privater Schuldzinsen im DBG (Steuerjahr 2025) mit Artikel.

**Soll (Referenz):** Art. 33 Abs. 1 lit. a DBG (Fassung 2025): private Schuldzinsen im Umfang der steuerbaren Vermögenserträge (Art. 20, 20a, 21) und weiterer CHF 50'000.

**Antwort des Agenten** (24.2 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Art. 33 Abs. 1 lit. a DBG** (Steuerjahr 2025, Bund):
> 
> > «Von den Einkünften werden abgezogen: a. die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken. Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten oder ihr sonst wie nahe stehenden natürlichen Person zu Bedingungen gewährt, die erheblich von den im Geschäftsverkehr unter Dritten üblichen Bedingungen abweichen;»
> 
> Quelle: `bund-dbg-2025__art-33-t1`. Der Chunk gilt für 2025 und ist durch `bund-dbg-2026` ersetzt. Der Status des Chunks ist in der Tool-Ausgabe nicht angegeben, daher kann ich keinen Status-Kennzeichen wie ✅ oder ☑️ nennen.
> 
> Die Regel gilt für den Bund. Kantonale Regeln prüfe ich nur auf Anfrage, für AR, SG, TG oder ZH mit Kanton und Jahr.

## q28

**Frage:** Ist ein Leasingvertrag für das Privatauto steuerlich relevant? Was ist mit den Leasingraten?

**Soll (Referenz):** Leasingraten sind keine Schuldzinsen und grundsätzlich nicht abziehbar (Lebenshaltung); relevant nur für Fahrkosten-Begründung/Geschäftsauto, Vermögen (kein Eigentum).

**Antwort des Agenten** (35.7 s · Tools: 4 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Kurz:** Der Leasingvertrag selbst ist kein Abzugsposten. Die Leasingraten sind für ein rein privat genutztes Auto **nicht abzugsfähig**. Ein beruflicher Anteil kann nur über die Fahrkosten geltend gemacht werden. Die kantonalen Werte habe ich noch nicht geprüft, weil mir der Kanton fehlt.
> 
> **Annahme:** Steuerjahr 2025, weil keine Jahreszahl angegeben war. Da heute November 2026 ist, könnte 2026 gemeint sein. Dann prüfe ich neu.
> 
> **1. Leasingraten für das Privatauto (Bund, 2025)**
> - Leasingraten für privat genutzte Güter enthalten keine abzugsfähigen Zinsanteile. Das gilt für die Schuldzinsen. Die Raten lassen sich also auch nicht über den Schuldzinsabzug geltend machen. (KS 22a, Ziff. 3.3, `bund-ks-22a__c0015`, ☑️ Fundstelle geprüft)
> - Ob die Raten als Lebenshaltungskosten nicht abziehbar sind, steht nicht ausdrücklich in dem Abschnitt. Ich habe das nicht im Wiki belegt, sondern aus dem Zusammenhang geschlossen.
> 
> **2. Berufliche Nutzung (Arbeitsweg)**
> - Der Arbeitsweg wird über eine Kilometerpauschale abgezogen: Auto CHF –.70/km, maximal CHF 3300.– (Formular 9–14, 2025, Ziff. 2, `bund-form-9-14-2025__c0002`, 🟡 extrahiert). Die Leasingraten werden dafür nicht zusätzlich geltend gemacht. Das habe ich im Wiki nicht gefunden.
> - Für die Benützung eines privaten Autos für den Arbeitsweg braucht es eine Begründung, zum Beispiel fehlendes öffentliches Verkehrsmittel oder erhebliche Zeitersparnis (Formular 9–14 2025, Ziff. 9, `bund-form-9-14-2025__c0006`, 🟡 extrahiert).
> 
> **3. Der Leasingvertrag als Beleg**
> - Er ist vor allem dann nützlich, wenn Sie das Auto beruflich nutzen, denn er belegt Fahrzeug und Laufzeit. Ob er als Beleg einzureichen ist, kann ich mit dem `ablage`-Werkzeug prüfen, wenn Sie mir den Text oder den Titel geben.
> 
> **Was ich noch brauche:**
> - **Kanton** (Wohnsitz am 31.12.). Die kantonalen Abzüge und Limiten können vom Bund abweichen.
> - **Steuerjahr**: 2025 oder 2026?
> - **Beruflicher Anteil**: Fahren Sie mit dem Auto zur Arbeit, und gibt es dafür einen Grund wie fehlende öV-Verbindung?

## q29

**Frage:** Wie hoch ist der Kinderabzug im Kanton Bern 2025?

**Soll (Referenz):** Nicht im Wiki (nur Bund, AR, SG, TG, ZH).

**Antwort des Agenten** (20.2 s · Tools: 0 Aufrufe ):

> Der Kanton Bern ist im Steuer-Wiki nicht abgedeckt. Das Wiki enthält nur den Bund sowie die Kantone Zürich, St. Gallen, Thurgau und Appenzell Ausserrhoden. Einen Kinderabzug für Bern kann ich daher nicht nennen, und ich schätze ihn nicht.
> 
> Für die Kinderabzüge in Bern 2025 empfehle ich die Steuerverwaltung des Kantons Bern bzw. die Wegleitung zur Steuererklärung 2025 des Kantons Bern.
> 
> Falls du stattdessen einen der abgedeckten Kantone meinst, sag mir welchen (ZH, SG, TG oder AR), dann suche ich den Kinderabzug 2025 dort nach.

## q30

**Frage:** Ehepaar TG 2025, beide angestellt (Nettolohn 80'000 und 30'000), pendelt mit ÖV-Abo (CHF 1'200 bzw. 900). Erstelle die Abzüge Berufskosten (Fahrkosten, Verpflegung ohne Kantine, Pauschale übrige) je Person für Kanton und Bund mit Fundstellen.

**Soll (Referenz):** TG 2025 je Person: Fahrkosten = ÖV-Abo effektiv (1'200 bzw. 900; Max. 6'000 Staat / 3'300 Bund); Verpflegung ohne Kantine 15/Tag, max. 3'200 (beide Ebenen); übrige Pauschale 3 %: P1 80'000 → 2'400, P2 30'000 → 900 → Minimum 2'000 (beide Ebenen, BKV TG § 4a / BKV Bund).

**Antwort des Agenten** (38.3 s · Tools: 7 Aufrufe steuerwiki__position, steuerwiki__wert):

> ## Berufskosten TG 2025, Ehepaar (Wohnsitz TG am 31.12.)
> 
> Die Werte sind für Kanton und Bund identisch, weil die Beträge unter allen Maxima liegen. Die Berechnung setzt Vollzeit (100 %) bei beiden Personen und keine Kantine voraus.
> 
> **Person 1 (Nettolohn CHF 80'000), Formular 4.2, Code 240**
> 
> | Position | Form. Ziff. | Kanton TG | Bund | Fundstelle |
> |---|---|---|---|---|
> | Fahrkosten ÖV-Abo | 2.1 | 1'200 | 1'200 | Kanton: `tg-stg__par-29` (Max. 6'000), `tg-form-01-2025__c0010`. Bund: `bund-dbg-2025__art-26` lit. a (Max. 3'300) |
> | Verpflegung | 3 | 3'200 | 3'200 | Kanton: `tg-bkv__par-2-t1` (CHF 15/Tag, max. 3'200/Jahr). Bund: `bund-bkv-2025__anhang-1` |
> | Übrige Berufskosten (Pauschale) | 4 | 2'400 | 2'400 | Kanton: `tg-bkv__par-4a`, `tg-form-04-2-2025__c0004`. Bund: `bund-bkv-2025__anhang-1`, `bund-dbg-2025__art-26` lit. c |
> | **Total** | 7 | **6'800** | **6'800** | |
> 
> **Person 2 (Nettolohn CHF 30'000), Formular 4.3, Code 280**
> 
> | Position | Form. Ziff. | Kanton TG | Bund | Fundstelle |
> |---|---|---|---|---|
> | Fahrkosten ÖV-Abo | 2.1 (Code 246) | 900 | 900 | wie Person 1 |
> | Verpflegung | 3 | 3'200 | 3'200 | wie Person 1 |
> | Übrige Berufskosten (Pauschale) | 4 | 2'000 | 2'000 | wie Person 1 |
> | **Total** | 7 (Code 280) | **6'100** | **6'100** | |
> 
> **Herleitung**
> 
> - **Fahrkosten:** Der ÖV-Abo-Betrag ist abziehbar, solange er unter dem Maximum liegt (TG 6'000, Bund 3'300). Die Belege nach `tg-stp-29-2__c0002` aufbewahren.
> - **Verpflegung:** Ohne Kantine gilt der volle Abzug von CHF 15 pro Arbeitstag. Der Halbabzug (CHF 7.50/Tag, max. 1'600) greift nur bei verbilligter Verpflegung oder Kantine (`tg-bkv__par-2-t2`). Bei 225 Arbeitstagen ergibt das 3'375, gedeckelt auf 3'200. Der Deckel wird ab 214 Arbeitstagen erreicht.
> - **Pauschale übrige Berufskosten:** 3 % des Nettolohns, min. 2'000, max. 4'000. Person 1: 3 % von 80'000 = 2'400. Person 2: 3 % von 30'000 = 900, auf das Minimum von 2'000 angehoben.
> 
> **Offene Punkte**
> 
> 1. **Pensum und Arbeitstage fehlen.** Bei Teilzeit werden Verpflegung und Pauschale anteilig gekürzt (`tg-bkv__par-2-t1`). Person 2 hat mit 30'000 netto eventuell ein tieferes Pensum. Pensum und Arbeitstage bitte bestätigen.
> 2. **Lohnausweis prüfen:** Feld F angekreuzt heisst keine Fahrkosten. Feld G heisst nur halbe Verpflegung. Beides würde die Zahlen oben ändern.
> 3. **Abnahme:** Alle Fundstellen sind ☑️ agent-geprüft, die Abnahme ist offen.
> 4. **Hinweis zum Bund:** Die Wegleitung 2a 2025 nennt für die Fahrkosten noch 3'200, das Gesetz (Art. 26 DBG) 3'300. Hier ohne Auswirkung, da die Fahrkosten unter beiden Werten liegen.

## q31

**Frage:** Ehepaar ZH 2026, beide erwerbstätig, Kind 3 Jahre in der Kita (Kosten CHF 30'000). Wie viel Drittbetreuung ist abziehbar (Kanton und Bund)?

**Soll (Referenz):** ZH 2026 Kanton max. CHF 25'300 pro Kind (zh-stg-2026__par-31-t3); Bund 2026 max. CHF 25'800 (bund-dbg-2026__art-33-t7). Abzug je Ebene getrennt.

**Antwort des Agenten** (25.3 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Kanton Zürich und Bund: Abzug je CHF 30'000 Kosten ist auf den Höchstbetrag begrenzt.**
> 
> | | Höchstbetrag pro Kind | Abzug bei CHF 30'000 |
> |---|---|---|
> | Kanton ZH (Staatssteuer) | CHF 25'300 | **CHF 25'300** |
> | Bund (direkte Bundessteuer) | CHF 25'800 | **CHF 25'800** |
> 
> Die Differenz von CHF 4'700 (Kanton) bzw. CHF 4'200 (Bund) ist nicht abziehbar. Die Beträge werden getrennt in der Staatssteuer- und der Bundessteuer-Spalte deklariert.
> 
> **Voraussetzungen, die hier erfüllt sind:**
> - Das Kind ist 3 Jahre alt, also unter 14 Jahren. Die Altersgrenze gilt im Kanton und im Bund gleich.
> - Das Kind lebt im gleichen Haushalt wie die steuerpflichtigen Eltern.
> - Beide Ehepartner sind erwerbstätig, die Kosten stehen also im Zusammenhang mit der Erwerbstätigkeit.
> 
> **Weitere Punkte:**
> - **Formular:** Ziffer 16.6 «Abzug für fremdbetreute Kinder» (Code 376). Belegt wird mit Kita-Rechnungen, Zahlungsnachweisen und einer Aufstellung der Betreuungskosten mit Empfängern. Bei angestellter Betreuungsperson ist zusätzlich eine Kopie des Lohnausweises beizulegen.
> - **Kürzung um 20 %:** Sie gilt nur für pauschal ausgewiesene Betreuungskosten. Bei Kita-Rechnungen entfällt sie.
> - **Nur Betreuungszeit:** Abziehbar sind nur die Kosten während der Arbeitszeit. Kosten für Sport, Musik, Vereine oder Nachhilfe sind nicht abziehbar.
> - **Halbierung:** Sie betrifft nur Konkubinat oder alternierende Obhut und gilt hier nicht.
> 
> **Vorbehalte:**
> - Die Werte stammen aus den Tool-Quellen mit Status ☑️ (Fundstelle geprüft, Abnahme offen). Die Fachabnahme steht noch aus.
> - Das reguläre Formular ZH 2026 ist laut Wiki noch nicht publiziert. Die Zuordnung stützt sich auf die Fassung für die unterjährige Steuerpflicht. Die Ziffer 16.6 und der Code 376 sind am definitiven Formular zu prüfen.
> - Ältere Quellen nennen für den Kanton noch CHF 10'400 (VKP ab 2024). Dieser Wert ist laut Wiki für 2026 überholt.
> 
> Quellen: zh-form-300-2026-uj__c0008, zh-wl-2026-uj__c0105, bund-dbg-2026__art-33-t7.

## q32

**Frage:** SG 2025: Einfamilienhaus (Baujahr 2010), selbst bewohnt. Pauschalabzug Liegenschaftsunterhalt Kanton und Bund?

**Soll (Referenz):** SG 2025: 20 % des Eigenmietwerts, ohne Altersstaffel (sg-stv__art-29); Bund: Gebäude zu Beginn 2025 über 10 Jahre alt → 20 % (bund-lkv__art-5).

**Antwort des Agenten** (23.4 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Ja, Pauschalabzug möglich, und zwar in beiden Fällen 20 %.** Bei einem Baujahr 2010 ist das Gebäude zu Beginn der Steuerperiode (1.1.2025) über 10 Jahre alt, also gilt der höhere Satz.
> 
> **Kanton SG 2025**
> - 20 % der Erträge (B), also des anrechenbaren Eigenmietwerts nach 30 %-Reduktion plus allfälliger Mieterträge ohne Nebenkosten.
> - SG kennt keine Staffelung nach Gebäudealter.
> - Eintrag: Ziff. 15, Code 716 (Form. 7, Abschnitt C1).
> - Fundstellen: sg-stv__art-29, sg-wl-2025__c0161.
> 
> **Direkte Bundessteuer 2025**
> - 20 % des Brutto-Eigenmietwerts, weil das Gebäude über 10 Jahre alt ist. Die 10 %-Stufe gilt nur bis 10 Jahre.
> - Die Bundesspalte wird nicht separat im Formular erfasst; die Steuerbehörde nimmt die Abweichungen automatisch vor.
> - Fundstelle: bund-lkv__art-5.
> 
> **Wichtig:**
> - Die Pauschale wird pro Liegenschaft und Steuerperiode gewählt. Alternativ können die tatsächlich selbst bezahlten Unterhaltskosten abgezogen werden (Form. 7, Rückseite C2). Dann müssen die Belege bereitgehalten werden, sie sind aber nur auf Verlangen einzureichen.
> - Die Pauschale gilt nur für ganz oder vorwiegend Wohnzwecken dienende Privatliegenschaften. Ein selbst bewohntes Einfamilienhaus erfüllt das.
> - Nicht über die Pauschale abziehbar sind wertvermehrende Investitionen (Anlagekosten).
> 
> Status der Angaben: agent-geprüft (Fundstellen geprüft, Abnahme durch die Fachperson offen). Die fachliche Beurteilung bleibt bei Ihnen bzw. der zuständigen Fachperson.

## q33

**Frage:** ZH 2025: Kind 19 Jahre, in Lehre (Ausbildung). Kinderabzug Kanton und Bund?

**Soll (Referenz):** ZH 2025 Kanton CHF 9'300 (volljährig in Erstausbildung, zh-stg-2025__par-34); Bund CHF 6'800 (bund-dbg-2025__art-35) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (24.6 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Kanton ZH, Steuerjahr 2025, Kind 19 in beruflicher Erstausbildung (Lehre):**
> 
> | | Kinderabzug (Einkommen) | Versicherungsabzug pro Kind | Abzug vom Steuerbetrag |
> |---|---|---|---|
> | **ZH (Staatssteuer)** | CHF 9'300 | CHF 1'300 | – |
> | **Bund (direkte Bundessteuer)** | CHF 6'800 | CHF 700 | CHF 263 |
> 
> Die Beträge gelten, weil das Kind volljährig ist und sich in beruflicher Erstausbildung befindet. Ein Kind bis zum Abschluss der Erstausbildung zählt also gleich wie ein minderjähriges Kind. Der Bund kennt keinen höheren Ausbildungsabzug.
> 
> **Voraussetzungen für den Abzug bei volljährigen Kindern in Ausbildung:**
> - Der Unterhalt wird zur Hauptsache von Ihnen bestritten.
> - Das Kind ist auf diese Unterstützung angewiesen.
> 
> Wenn diese Voraussetzungen nicht erfüllt sind, fällt der Abzug weg. Ob sie hier zutreffen, hängt vom Sachverhalt ab, zum Beispiel von eigenem Lehrlingslohn und davon, wer die Kosten trägt. Das Wiki liefert dazu keine Schwelle, die ich Ihnen nennen könnte.
> 
> **Formular ZH 2025:** Ziff. 24.1, Code 370 (Kind im Haushalt) bzw. Code 372 (Kind ausserhalb Ihres Haushalts). Der Versicherungsabzug steht in Ziff. 15 (Code 270).
> 
> **Quellen:** ZH § 34 StG (`zh-stg-2025__par-34`), ZH Versicherungsabzug (`zh-stg-2025__par-31-t2`), Bund Art. 35 DBG (`bund-dbg-2025__art-35`), Bund Art. 36 Abs. 2bis DBG (`bund-dbg-2025__art-36-t4`), ZStB 34.1 Rz 6–12 zu Ausbildung und Angewiesenheit (`zh-zstb-34-1-bis-2025__c0004`/`c0005`).
> 
> **Status:** Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme durch die Fachperson offen).

## q34

**Frage:** ZH 2025: Lohnausweis Feld G angekreuzt (Kantine). Welche Verpflegungspauschale gilt und in welche Ziffer des Berufsauslagenformulars?

**Soll (Referenz):** Verbilligte Verpflegung: CHF 7.50 pro Arbeitstag, max. CHF 1'600 pro Jahr (LS 631.33, zh-pauschalierung-berufsauslagen-2025__c0004); Form. 360 Ziff. 2.1 (verbilligt); Bund gleich.

**Antwort des Agenten** (25.1 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__suche):

> **Verpflegungspauschale: CHF 7.50 pro Arbeitstag, höchstens CHF 1'600 pro Jahr** (verbilligte Verpflegung, Kanton Zürich 2025).
> 
> **Formularziffer:** Hilfsblatt Berufskosten (Form. 360), **Ziff. 2.1 (verbilligt)**, **Code 206** für Person 1 (Code 226 für Person 2). Der Betrag steht in der Spalte Staatssteuer und in der Spalte Bundessteuer.
> 
> **Berechnung:** min(Arbeitstage × 7.50; 1'600). Die Arbeitstage mit auswärtiger Verpflegung stehen im Arbeitszeitnachweis.
> 
> **Voraussetzungen:**
> - Die Arbeitspause lässt die Heimkehr nicht zu, und trotzdem entstehen Mehrkosten.
> - Nicht kumulierbar mit Ziff. 2.1 voll, Ziff. 2.2 (Schicht) oder Mittagsheimfahrt. Bei Mittagsheimfahrt entfällt der Verpflegungsabzug.
> 
> **Bund:** Die Limiten sind gleich (CHF 7.50 / CHF 1'600). Die Beachten-Notiz zum Bund erwähnt einen halben Abzug bei Verbilligung, die anders als in bar (Gutscheine) oder über eine AG-Kantine erfolgt. Ob dieser Fall für Ihre Kantine zutrifft, habe ich nicht abschliessend geklärt. Ich würde die Bundesspalte deshalb vor dem Eintragen nochmals prüfen.
> 
> **Status:** ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Quellen: zh-form-360-2025__c0003, zh-pauschalierung-berufsauslagen-2025__c0004, zh-wl-2025__c0066.
> 
> **Belege:** Der Lohnausweis (Feld G) muss eingereicht werden. Das Spesenreglement des Arbeitgebers ist laut Wiki nicht eindeutig einreichungspflichtig.

## q35

**Frage:** SG 2025: Kapitalbezug Säule 3a CHF 100'000. Wird das mit dem übrigen Einkommen besteuert? Wo deklarieren?

**Soll (Referenz):** Nein – Kapitalleistungen aus Vorsorge werden getrennt vom übrigen Einkommen (separate Jahressteuer) besteuert; SG Formular 1 Ziff. 40.1 (Säule 3a), Total Ziff. 41.

**Antwort des Agenten** (26.4 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__position, steuerwiki__zeige):

> **Kurz:** Ja, das Kapital wird nicht zum übrigen Einkommen dazugerechnet. Es wird separat mit einer eigenen Jahressteuer besteuert. In der Steuererklärung 2025 deklarierst du es in Ziffer 40.1 (Säule 3a) des Formulars 1.
> 
> **Besteuerung (SG, Steuerjahr 2025)**
> - Die Kapitalleistung wird gesondert vom übrigen Einkommen besteuert. Die Angabe dient laut Wegleitung nur Informationszwecken und hat keine weiteren Steuerfolgen. (WL SG 2025, Ziff. 40, S. 35 · `sg-wl-2025__c0119`)
> - **Kanton (Staats- und Gemeindesteuer):** einfache Steuer zu 2,0 % für Ehegatten bzw. 2,2 % für übrige. Allgemeine und Sozialabzüge fallen dabei weg. Der Ehegattensatz gilt auch für Alleinstehende, die mit Kindern oder Unterstützten zusammenleben.
> - **Bund (direkte Bundessteuer):** ein Fünftel der Tarife nach Art. 36 DBG, ohne Sozialabzüge. Die Abweichungen für den Bund nimmt die Steuerbehörde automatisch vor.
> - Mehrere Kapitalleistungen aus Vorsorge werden zu einem Gesamtbetrag zusammengerechnet.
> 
> **Wo deklarieren**
> - **Ziffer 40.1** (Formular 1 SG 2025): Kapitalleistungen aus gebundener Vorsorge Säule 3a, Betrag 2025 (Gesamtbetrag bei mehreren Auszahlungen).
> - **Beleg:** Bescheinigung der Bank oder Versicherung über die Kapitalauszahlung 2025. Diese ist einzureichen.
> - Nicht in Ziffer 6.4 (Kapitalabfindungen für wiederkehrende Leistungen) eintragen.
> 
> **Nicht verwechseln:** Ziffer 13.1 betrifft die Einzahlungen in die Säule 3a (Max. CHF 7'258 mit 2. Säule bzw. 20 % des Erwerbseinkommens, max. CHF 36'288 ohne), nicht den Bezug.
> 
> **Offen:** Den genauen Steuerbetrag kann ich aus den Quellen nicht berechnen. Dafür fehlen der Steuerfuss der Gemeinde und die Tarifstufen nach Art. 36 DBG für den Bund. Die Quellen zu den Sätzen sind geprüft, die Abnahme durch die Fachperson steht aber noch aus. Wenn du mir die Gemeinde und den Familienstand nennst, kann ich die Rechnung genauer eingrenzen.

## q36

**Frage:** ZH 2025: Geschiedener Mandant zahlt Unterhaltsbeiträge an die Ex-Frau (CHF 24'000) und für das minderjährige Kind (CHF 12'000). Was ist abziehbar, in welcher Ziffer?

**Soll (Referenz):** Ex-Ehefrau CHF 24'000 voll abziehbar, Ziff. 13.1 (Code 254); Kinderalimente CHF 12'000 abziehbar bis und mit Monat der Volljährigkeit, Ziff. 13.2 (Code 255); Empfänger versteuert; Bund gleich (Art. 33 Abs. 1 lit. c DBG).

**Antwort des Agenten** (25.2 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__suche, steuerwiki__wert):

> Beide Beträge sind abziehbar, in zwei verschiedenen Ziffern des Abzugsteils (Kanton und Bund identisch):
> 
> | Zahlung | Ziffer | Code | Betrag | Abzug |
> |---|---|---|---|---|
> | CHF 24'000 an die geschiedene Ehefrau | 13.1 | 254 | 24'000 | voll |
> | CHF 12'000 für das minderjährige Kind | 13.2 | 255 | 12'000 | voll, aber nur bis und mit dem Monat des 18. Geburtstags |
> 
> **Ziff. 13.1 (Code 254):** Periodische Unterhaltsbeiträge an den geschiedenen Ehegatten, die für ihn persönlich bestimmt sind, sind voll abziehbar. Summe der 2025 effektiv bezahlten Beiträge eintragen. Kapitalabfindungen sind nicht abziehbar.
> 
> **Ziff. 13.2 (Code 255):** Kinderalimente sind abziehbar, aber nur für Zahlungen bis und mit dem Monat, in dem das Kind 18 wird. Die 12'000 gelten nur, wenn sie diesen Zeitraum betreffen; ist das Kind 2025 noch minderjährig, bleibt der volle Betrag abziehbar. Danach entfällt der Abzug, und der Zahlende hat stattdessen Anspruch auf den Kinderabzug nach Ziff. 24.1. Für dieses Kind gibt es dann keinen Kinderabzug zusätzlich zu den Alimenten.
> 
> **Korrespondenz:** Die Ex-Frau versteuert die 24'000 als Einkommen in Ziff. 5.1 (Code 160). Kinderalimente, die jemand anderes erhält, stehen in Ziff. 5.2 (Code 161).
> 
> **Offene Punkte:**
> - Die Summen müssen Zahlungen des Jahres 2025 sein. Bei 13.2 brauchen Sie die Monatszuordnung der Zahlungen, damit klar ist, ob sie vor dem 18. Geburtstag des Kindes liegen.
> - Bank- und Zahlungsbelege sowie Scheidungsurteil bzw. Unterhaltsvereinbarung sollten bereitliegen. Das Wiki sagt, sie müssten nur auf Verlangen eingereicht werden, und im Zweifel empfiehlt es, sie beizulegen.
> - Die Fundstellen sind agent-geprüft (☑️, Abnahme offen): Ziff. 13.1 belegt durch zh-form-300-2025__c0007 und zh-wl-2025__c0075; Ziff. 13.2 durch zh-form-300-2025__c0007 und zh-wl-2025__c0076.

## q37

**Frage:** TG 2025: Mandant bringt Steuerberatungsrechnung, Kreditkartenabrechnung, Mietvertrag und Motorfahrzeugversicherung. Was davon ist relevant?

**Soll (Referenz):** Steuerberatungsrechnung: nein; Motorfahrzeugversicherung: nein; Kreditkartenabrechnung: bedingt (nur als Nachweis/Schuld per 31.12.); Mietvertrag: bedingt (Wochenaufenthalt/Arbeitszimmer/Adressnachweis) – laut belege-relevanz.

**Antwort des Agenten** (32.6 s · Tools: 5 Aufrufe steuerwiki__ablage, read):

> **Kanton TG, Steuerjahr 2025.** Relevant ist nur der Mietvertrag, und auch nur unter Bedingungen. Die anderen drei Dokumente sind nicht steuerrelevant, bzw. die Kreditkartenabrechnung nur als Nachweis.
> 
> | Dokument | Steuerrelevant? | Kategorie (KATEGORIEN.md) | Eingereicht? |
> |---|---|---|---|
> | Steuerberatungsrechnung | **Nein** | Keine Steuerbeleg-Kategorie | – |
> | Kreditkartenabrechnung | **Bedingt** | Belege Sonstiges | nein (unklar) |
> | Mietvertrag | **Bedingt** | Belege Sonstiges, nur bei Ausnahme (sonst keine) | nein (unklar) |
> | Motorfahrzeugversicherung | **Nein** | Keine Steuerbeleg-Kategorie | – |
> 
> **Begründung je Dokument**
> 
> 1. **Steuerberatungsrechnung – nicht relevant.** Kosten für Steuerberatung und Steuererklärung im Privatvermögen sind nicht abziehbar. Die Fundstelle ist die Bundeswegleitung (`bund-wl-2a-2025__c0057`). Ich habe nicht separat geprüft, ob die TG-Wegleitung dazu etwas anderes sagt. Kein Wert in der Steuererklärung.
> 
> 2. **Kreditkartenabrechnung – bedingt.** Die Abrechnung selbst ist kein steuerlicher Beleg. Sie ist nur Nachweis für einzelne abziehbare Zahlungen, etwa Spenden, Arzt- oder Zahnarztkosten, Weiterbildung oder Berufsauslagen, wenn die Originalrechnung fehlt. Ebenso kann sie Nachweis für Sollzinsen sein. Die Liste nennt die Kreditkartenabrechnung nicht ausdrücklich. Deshalb wähle ich «Belege Sonstiges» (dort stehen Spenden-, Weiterbildungs- und Schuldzinsbelege, sofern nicht einzureichen). Die Einreichepflicht ist für TG unklar. Prüfe die Abrechnung auf die Positionen und lege sie nur ab, wenn ein solcher Abzug vorkommt.
> 
> 3. **Mietvertrag – bedingt.** Die Miete einer selbstbewohnten Wohnung ist Lebenshaltung und nicht abziehbar. Relevant wird der Vertrag nur bei Untervermietung, weil dann der Nettoertrag steuerbar ist, oder bei einem Wochenaufenthalt am Arbeitsort, weil dann Mehrkosten für die Unterkunft abziehbar sein können. Ob einer dieser Fälle vorliegt, muss der Mandant bestätigen. Trifft keiner zu, gehört der Vertrag nicht in eine Steuerbeleg-Kategorie.
> 
> 4. **Motorfahrzeugversicherung – nicht relevant.** Prämien für ein Privatfahrzeug sind Lebenshaltungskosten und nicht abziehbar. Das Wiki bestätigt das für AR und SG. Die Fundstelle für TG (`tg-wl-2025__c0123`) passt inhaltlich schlecht, weil sie von geleasten Fahrzeugen handelt. Für die TG-Aussage fehlt also ein sauber belegter Nachweis. Kein Wert in der Steuererklärung.
> 
> **Offen:** Für den Mietvertrag brauche ich eine Antwort des Mandanten: Gibt es Untervermietung oder einen Wochenaufenthalt am Arbeitsort? Die Kategorien sind noch nicht von consis bestätigt, und die Einreichepflicht für TG ist bei Kreditkarte und Mietvertrag nicht eindeutig.

## q38

**Frage:** AR 2026: Wie hoch ist der Kinderabzug für ein 10-jähriges Kind? Ist der Wert gesichert?

**Soll (Referenz):** AR 2026: CHF 7'400 laut Anhang 1 StG (indexiert), aber Status STRITTIG (MB 02 / StG-Text nennen andere Beträge; Wegleitung 2026 fehlt) → Fachperson.

**Antwort des Agenten** (25.8 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kurz:** Für ein 10-jähriges Kind im Kanton AR 2026 sind es **CHF 7'400** Kinderabzug. Der Wert ist **nicht gesichert**: Die Quellen widersprechen sich.
> 
> **AR 2026, Kind im Alter 4 bis 15 (Ziff. 23.2 des Formulars)**
> - **CHF 7'400** nach Anhang 1 StG (Art. 38 Abs. 1 lit. a Ziff. 2, indexiert per 1.1.2024), Fundstelle `ar-stg-anhang-kp__c0001`.
> - Die Wegleitung AR 2025 (`ar-wl-2025__c0005`) bestätigt ebenfalls 7'400.
> - Die Materialblätter MB 02 (Stand 18.08.2026, `ar-mb-02__c0002`) nennen dagegen **CHF 7'000**. Das ist laut Wiki der nicht indexierte Gesetzestext.
> - Status: ⚠️ strittig. Eine Fachperson muss entscheiden.
> - Die Wegleitung 2026 fehlt im Wiki, daher kann ich den Wert nicht aus einer Wegleitung für 2026 belegen.
> 
> **Bund 2026 (direkte Bundessteuer), separat zu deklarieren**
> - **CHF 6'800** Kinderabzug vom Einkommen (Art. 35 Abs. 1 lit. a DBG, `bund-dbg-2026__art-35`). Keine Staffelung nach Alter.
> - Zusätzlich **CHF 263** Ermässigung des Steuerbetrags pro Kind (Art. 36 Abs. 2bis DBG, `bund-dbg-2026__art-36-t4`). Die beiden Abzüge gelten nebeneinander.
> - Status: ☑️ agent-geprüft. Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> 
> **Zur Sicherheit des Werts:** Für AR ist der Betrag strittig (7'400 gegen 7'000). Für den Bund ist er gut belegt, aber noch nicht abgenommen. Ich empfehle, den AR-Wert vor der Einreichung mit der Veranlagungsbehörde oder einer Fachperson abzugleichen.

## q39

**Frage:** Welche Vermögenssteuer-Freibeträge (Sozialabzüge) gelten 2025 in ZH für Alleinstehende und Verheiratete?

**Soll (Referenz):** ZH kennt keine Vermögens-Sozialabzüge, sondern Tarifstufen mit 0 ‰: Grundtarif erste CHF 80'000, Verheiratetentarif erste CHF 159'000 (zh-stg-2025__par-47); kein Betrag pro Kind.

**Antwort des Agenten** (24.0 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__position):

> In Zürich gibt es für 2025 keinen eigenen Vermögens-Sozialabzug. Der steuerfreie Betrag ergibt sich aus der ersten Stufe des Vermögenssteuertarifs (§ 47 StG), die mit 0 ‰ besteuert wird:
> 
> | Steuerpflichtige | Steuerfrei (0 ‰) bis |
> |---|---|
> | Alleinstehende (Grundtarif) | CHF 80'000 |
> | Verheiratete (Verheiratetentarif) | CHF 159'000 |
> 
> - **Kanton Zürich:** Die Werte stammen aus § 47 Abs. 1 und 2 StG (Stand 1.1.2025). Fundstellen: `zh-stg-2025__par-47-t1` und `zh-stg-2025__par-47-t2`. Status: ☑️ agent-geprüft, Abnahme offen.
> - **Bund:** Die direkte Bundessteuer kennt keine Vermögenssteuer, also gibt es dort keinen Freibetrag.
> - **Kinder:** Beim Vermögen gibt es in ZH keinen Abzug pro Kind.
> - **Verheiratetentarif:** Er gilt auch für Verwitwete, Getrennte, Geschiedene und Ledige, die mit Kindern zusammenleben (§ 47 Abs. 2 StG). Nicht gemeinsam besteuerte Eltern: Den Verheiratetentarif erhält nur, wer hauptsächlich den Kindesunterhalt trägt. Massgebend sind die Verhältnisse am Ende der Steuerperiode (§ 47 Abs. 3 StG).
> 
> **Formular:** Im Formular 300 (ZH 2025) gibt es keine Zeile für den Freibetrag. Eingetragen wird nur das steuerbare Vermögen in Ziff. 37 (Code 498). Die 0 ‰-Stufe wird beim Rechnen automatisch berücksichtigt.
> 
> Die Werte stimmen mit der VKP 2024 überein (`zh-vkp-2024-zstb`).

## q40

**Frage:** Alleinstehende TG 2026, Nettolohn 90'000, ÖV-Abo 2'400, Säule 3a 7'258, Krankenkasse 5'500. Erstelle die Abzüge (Berufskosten, 3a, Versicherungsabzug) Kanton und Bund mit Fundstellen und Status.

**Soll (Referenz):** TG 2026 (Kanton/Bund): Fahrkosten 2'400 (Max. 6'000 / 3'300); übrige Berufskosten 3 % von 90'000 = 2'700 (Min. 2'000, Max. 4'000, beide Ebenen); Säule 3a 7'258 (TG 🟡 extrahiert, Bund ☑️); Versicherungsabzug TG max. 3'500 → 3'500, Bund max. 1'800 → 1'800 (Prämien 5'500 übersteigen beide Maxima).

**Antwort des Agenten** (48.4 s · Tools: 10 Aufrufe steuerwiki__wert, steuerwiki__position):

> ## Abzüge TG 2026, alleinstehend, Nettolohn CHF 90'000
> 
> Die Angaben sind Ihre; die Limiten und Fundstellen stammen aus dem Steuer-Wiki. Der Bund steht getrennt, weil Kanton und Bund bei Fahrkosten und Versicherungen unterschiedliche Maxima haben.
> 
> | Position (Formular TG 2026) | Ihr Betrag | Kanton TG (Staat/Gemeinde) | Bund (direkte Bundessteuer) |
> |---|---|---|---|
> | **Berufskosten, ÖV-Abo** (Form. 4.2/4.3 Ziff. 2.1, Ziff. 2.5) | 2'400 | **2'400** (Max. 6'000) | **2'400** (Max. 3'300) |
> | **Berufskosten, übrige Pauschale** (Form. 4.2/4.3 Ziff. 4) | 3 % × 90'000 | **2'700** (min. 2'000, max. 4'000) | **2'700** (min. 2'000, max. 4'000) |
> | **Berufskosten total** (Ziff. 10.1) | | **5'100** | **5'100** |
> | **Säule 3a** (Ziff. 13.1) | 7'258 | **7'258** | **7'258** |
> | **Versicherungsprämien** (Ziff. 14) | 5'500 | **3'500** (Max. alleinstehend) | **1'800** (Max. alleinstehend mit 2. Säule/3a) |
> 
> **Summe:** Kanton CHF 15'858 · Bund CHF 14'158
> 
> ### Fundstellen und Status
> 
> | Position | Kanton TG | Bund |
> |---|---|---|
> | ÖV-Abo | Limite 6'000: `tg-wl-2026__c0176`; Ziff. 2.1: `tg-form-04-2-2026__c0002` / `tg-wl-2026__c0177` · ☑️ | Limite 3'300: `bund-dbg-2026__art-26` · ☑️ |
> | Pauschale 3 % | `tg-form-04-2-2026__c0004`; `tg-wl-2026__c0187` · ☑️ | Gleiche Regel laut Wiki; keine eigene Bund-Fundstelle erfasst · ☑️ |
> | Säule 3a 7'258 | Ziff. 13.1: `tg-form-01-2026__c0010`; Limite `tg-wl-2026__c0089` · ☑️ | `bund-bsv-masszahlen-2025-2026__c0003` · ☑️ |
> | Versicherung 3'500 / 1'800 | `tg-stg__par-34-t3` (Max. 3'500); Ziff. 14: `tg-form-01-2026__c0010`, `tg-wl-2026__c0209` · ☑️ | `bund-dbg-2026__art-33-t2` (1'800) · ☑️ |
> 
> Alle Werte sind agent-geprüft (Fundstelle geprüft, Abnahme offen). Keiner ist von einer Fachperson abgenommen.
> 
> ### Annahmen, die Sie bestätigen sollten
> 
> 1. **Nettolohn 90'000** ist der Wert aus dem Lohnausweis Ziff. 11. Die 3 %-Pauschale basiert darauf.
> 2. **ÖV-Abo nur abziehbar, wenn der Arbeitgeber es nicht bezahlt hat.** Im Lohnausweis darf Feld F nicht angekreuzt sein. Sonst entfällt der Abzug.
> 3. **3a 7'258 ist der volle Jahresbeitrag.** Mit Anschluss an die 2. Säule ist 7'258 das Limit. Ohne 2. Säule wäre das Limit 20 % × 90'000 = 18'000 (gedeckelt bei 36'288), der Abzug bleibt also gleich.
> 4. **5'500 ist die Nettoprämie nach Abzug der Prämienverbilligung (IPV).** Der Abzug ist auf Kanton 3'500 und Bund 1'800 begrenzt. Die Krankenkasse übersteigt beides; der Mehrbetrag ist nicht abziehbar.
> 5. **Keine weiteren Berufskosten.** Verpflegung, Weiterbildung, Mehrkosten Auswärtsverpflegung usw. sind nicht enthalten. Die Pauschale 3 % ist nur mit einem Ansatz gewählt, effektive Kosten schliessen sie aus.
> 
> ### Offene Punkte
> - Bei den Belegen ist «einreichen» für ÖV-Abo und Krankenkassenprämien im Wiki als «unklar» markiert. Am sichersten: Abo-Quittung und Prämienrechnung beilegen.
> - Ob Sie tatsächlich einer 2. Säule angeschlossen sind, bestimmt die Kästchen-Angabe bei Ziff. 13.1. Der Abzugsbetrag ändert sich dadurch nicht.

