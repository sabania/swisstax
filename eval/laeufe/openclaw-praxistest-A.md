# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuermem` · Fragen: 40 · Lauf: 2026-11-09 06:26
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q01

**Frage:** Mandantin (ZH, 2025) bringt: Lohnausweis, Krankenkassen-Prämienrechnung, Handyrechnung, 3a-Bescheinigung, Hausratversicherungspolice, Spendenquittung Rotes Kreuz CHF 80, Kita-Rechnungen. Welche sind relevant, wofür?

**Soll (Referenz):** Relevant: Lohnausweis (Einkünfte 1.1), Krankenkassenprämien (Versicherungsabzug Ziff. 15, Form. 365), 3a-Bescheinigung (Ziff. 14), Kita-Rechnungen (Ziff. 16.6 Drittbetreuung, max. 25'000 Kanton / 25'800 Bund). Spende CHF 80: unter Mindestbetrag 100 → nicht abziehbar (sofern Total < 100). Nicht relevant: Handyrechnung (Lebenshaltung), Hausratversicherung (kein Versicherungsabzug).

**Antwort des Agenten** (52.9 s · Tools: 17 Aufrufe read, read):

> **Kurzfassung (ZH, Steuerjahr 2025):** Vier der sieben Belege sind relevant: Lohnausweis, 3a-Bescheinigung, Krankenkassen-Prämien und Kita-Rechnungen (letztere bedingt). Die Spende von CHF 80 zählt nur, wenn die Spenden im Jahr zusammen mindestens CHF 100 betragen. Handyrechnung und Hausratpolice sind nicht relevant.
> 
> Quelle: `quick/belege-relevanz.md`, `quick/zuordnung-zh-2025.md`, `quick/werte-zh-2025.md` und die Belegkarten. Alle Zeilen haben den Status ☑️ agent-geprüft. Die verlinkten Chunks habe ich nicht einzeln geöffnet, die Chunk-IDs stammen aus den Wiki-Seiten.
> 
> | Beleg | Relevanz | Ziffer ZH 2025 | Was zu prüfen ist |
> |---|---|---|---|
> | **Lohnausweis** | ja | 1.1 (Haupterwerb), 1.2 (Nebenerwerb) | Nettolohn aus Ziff. 11 übertragen. Dazu kommen Feld F (Gratis-Arbeitsweg, dann kein Fahrkostenabzug), Feld G (Kantine/Lunch-Checks) und Ziff. 10.2 (PK-Einkauf, steckt schon im Nettolohn). Ziff. 13.3 (Weiterbildung) ist für Form. 367 relevant. Berufskosten (Ziff. 11.1, Form. 360) laufen pauschal: 3 % des Nettolohns, mind. CHF 2'000, max. CHF 4'000 (`zh-pauschalierung-berufsauslagen-2025__c0005`). Der Lohnausweis muss der Steuererklärung beiliegen (`zh-wl-2025__c0032`). |
> | **3a-Bescheinigung** | ja | 14.1 / 14.2 | Nur 2025 tatsächlich einbezahlte Beträge zählen. Das Maximum mit 2. Säule ist CHF 7'258 für Kanton und Bund. Ohne 2. Säule sind es 20 % des Erwerbseinkommens, max. CHF 36'288 (`zh-wl-2025__c0081`). Die Bescheinigung gehört zur Steuererklärung. Bei Einzahlungen in mehrere Verträge ist das Total zu begrenzen. |
> | **Krankenkassen-Prämien** | ja | 15 über Form. 365 Teil A (Ziff. 1–4, 6) | Massgebend sind die tatsächlich bezahlten Prämien abzüglich Prämienverbilligung. Wurde die Verbilligung schon mit der Rechnung verrechnet, nicht doppelt kürzen. Der Abzug ist gedeckelt. Mit 3a-Beiträgen gilt für Alleinstehende CHF 2'900 (Staat) bzw. CHF 1'800 (Bund), für Verheiratete CHF 5'800 bzw. CHF 3'700. Pro Kind kommen CHF 1'300 bzw. CHF 700 dazu (`zh-stg-2025__par-31-t2`). Die Werte ohne Vorsorgebeiträge (CHF 4'350 / 8'700) gelten für sie nicht, da sie 3a einzahlt. |
> | **Kita-Rechnungen** | bedingt | 16.6 | Das Kind muss unter 14 Jahre alt sein und im gleichen Haushalt leben. Die Betreuung muss durch Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit veranlasst sein. Bei Ehepaaren müssen beide gleichzeitig erwerbstätig sein. Das Maximum pro Kind ist CHF 25'000 (Staat, `zh-stg-2025__par-31-t4`) bzw. CHF 25'800 (Bund, Art. 33 Abs. 3 DBG). Verpflegung ist nicht abziehbar und muss separat ausgewiesen oder gekürzt werden. Subventionen sind abzuziehen. Es braucht Name und Geburtsdatum des Kindes sowie Name und Adresse der Kita. |
> | **Spende Rotes Kreuz CHF 80** | bedingt, allein nicht abziehbar | 22.2 | Die Mindestschwelle ist CHF 100 für das Jahrestotal aller Zuwendungen (Kanton und Bund, `zh-info-spenden__c0003`, Art. 33a DBG). Das Maximum sind 20 % des Nettoeinkommens. Das Rote Kreuz muss steuerbefreit sein und seinen Sitz in der Schweiz haben. Gibt es weitere Spenden, die zusammen CHF 100 erreichen, alle mit Empfänger auflisten. Belege sind in ZH erst auf Verlangen nötig. |
> | **Handyrechnung** | nein | – | Telefon ist Lebenshaltungskosten (Art. 34 lit. a DBG, Belegkarte `privatrechnungen-alltag`). Eine berufliche Nutzung wäre unter «Berufskosten» zu prüfen. Die Wiki-Quellen enthalten dazu keine eigene ZH-Regel. Die übrigen Berufskosten sind in ZH pauschaliert (siehe Lohnausweis). Ob ein effektiver Abzug möglich ist, entscheidet die Fachperson. |
> | **Hausratpolice** | nein | – | Sachversicherungen gehören nicht zu den Prämien in Form. 365 (Krankenkasse, Unfall, Leben/Rente, Sparzinsen). Der Hausrat selbst ist kein Vermögen. Für ZH und den Bund fand ich in den Wegleitungen keinen ausdrücklichen Ausschluss. AR und SG haben einen, daher bleibt die Einordnung bei der Fachperson. |
> 
> **Offene Punkte, die ich für die Ziffern und Limiten brauche:**
> 1. Zivilstand und Kinder per 31.12.2025 (Versicherungsabzug, kein Kinderabzug ohne Angabe) sowie das Alter der Kita-Kinder.
> 2. Ob sie in einer Pensionskasse ist (Lohnausweis Ziff. 10.1). Das bestimmt, welches 3a-Maximum gilt.
> 3. Ob die Prämienverbilligung schon in der Prämienrechnung verrechnet ist.
> 4. Ob weitere Spenden bezahlt wurden.
> 5. Ob in der Kita-Rechnung der Verpflegungsanteil separat ausgewiesen ist.
> 
> Nicht verfügbar im Wiki: betragsmässige Belegpflicht-Schwellen für ZH (`verfahren.beilagen_schwellen` ist offen). Die fachliche Beurteilung bleibt bei SB/ML.

## q02

**Frage:** In welche Ziffer und mit welchem Code der ZH-Steuererklärung 2025 gehört der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb)?

**Soll (Referenz):** Ziff. 1.1 Haupterwerb, Code 100 (Person 1) / 101 (Person 2); Nettolohn Lohnausweis Ziff. 11 (zh-form-300-2025).

**Antwort des Agenten** (24.5 s · Tools: 4 Aufrufe read, exec, exec):

> **Ziffer 1.1, Code 100** (Steuererklärung ZH 2025, Einkünfte: «Haupterwerb unselbständig», Person 1). Person 2 wäre Code 101.
> 
> - **Betrag:** Der Nettolohn aus Lohnausweis Ziff. 11 kommt hier hinein. Das ist der Lohn nach Abzug von AHV/IV/EO/ALV, laufenden BVG-Beiträgen und NBUV-Prämien. Den Lohnausweis legen Sie bei. Erwerbslücken sind ausdrücklich zu bezeichnen.
> - **Bund:** Es gilt dieselbe Zeile für Staats- und Bundessteuer, es gibt keine separate Bundesspalte.
> - **Nebenerwerb:** Ein Nebenerwerb gehört nicht hierhin, sondern in Ziff. 1.2 (Code 102/103).
> - **Fundstellen:** Formular 300 ZH 2025, S. 2 (`zh-form-300-2025__c0004`) und Wegleitung ZH 2025, S. 10 (`zh-wl-2025__c0032`).
> - **Status:** ☑️ agent-geprüft, nicht durch eine Fachperson verifiziert.
> 
> Ich habe nur die Zuordnungsseite und die Detailseite geprüft, nicht die Chunks oder das Original-PDF.

## q03

**Frage:** Lohnausweis Feld F ist angekreuzt (Geschäftsauto). Was bedeutet das für den Fahrkostenabzug (SG 2025)?

**Soll (Referenz):** Feld F angekreuzt → kein Fahrkostenabzug für den Arbeitsweg mit Geschäftsfahrzeug (Privatanteil im Lohn, Lohnausweis Ziff. 2.2).

**Antwort des Agenten** (40.9 s · Tools: 11 Aufrufe read, read, exec):

> Ich lese noch die Stellen zum Geschäftsfahrzeug (WL SG 2025 c0076, Art. 18a StV SG) nach, dann antworte ich.
> 
> **Kurzantwort (SG, Steuerjahr 2025):** Wenn im Lohnausweis Feld F angekreuzt ist, ist **kein Fahrkostenabzug** für den Arbeitsweg möglich. Form. 4 Ziff. 1.1–1.3 (Codes 400–406) bleiben leer. Das gilt für Kanton und Bund, weil Feld F bescheinigt, dass dem Arbeitnehmer gar keine Kosten entstehen.
> 
> **Fundstellen**
> - **WL SG 2025, S. 23 (Ziff. 10.1)** `sg-wl-2025__c0075`: «Wenn dem Arbeitnehmer keine Kosten erwachsen (Sammeltransport, vom Arbeitgeber getragenes Generalabonnement, das aus geschäftlichen Gründen benutzt wird), muss auf dem Lohnausweis Feld F angekreuzt sein. Ein Abzug für die Fahrt zur Arbeit ist deshalb nicht möglich.» Status ☑️ agent-geprüft.
> - **Geschäftsauto mit Privatanteil:** WL SG 2025, S. 23 `sg-wl-2025__c0076`. Wird für die private Nutzung 0,9 % des Kaufpreises pro Monat (10,8 % pro Jahr) versteuert, «kann kein Fahrkostenabzug geltend gemacht werden». Der Privatanteil gilt den Arbeitsweg ab. Er muss im Lohnausweis als Gehaltsnebenleistung stehen.
> - **Rechtsgrundlage:** Art. 18a StV SG `sg-stv__art-18a` (pauschale Fahrkostenberechnung, 0,9 % des Kaufpreises als monatliches Einkommen). Sie ersetzt den Fahrkostenabzug nach Art. 18 StV.
> 
> **Ausnahme: Bordbuch**
> Wenn die privaten Fahrten samt Arbeitsweg nicht pauschal (0,9 %), sondern effektiv per Bordbuch abgerechnet werden, können die effektiven Arbeitswegkosten bis zum Maximalabzug geltend gemacht werden (WL SG 2025, `sg-wl-2025__c0076`). Dann braucht es ein detailliertes, vollständiges Bordbuch, und der Privatanteil muss trotzdem im Lohnausweis als Gehaltsnebenleistung erfasst sein. Ob das Feld F in diesem Fall angekreuzt sein darf, sagen die Quellen im Wiki nicht ausdrücklich. Das müssten Sie am Lohnausweis klären.
> 
> **Was Sie prüfen sollten**
> 1. **Privatanteil im Lohnausweis:** Er sollte als Gehaltsnebenleistung unter Ziff. 2.2 stehen. Steht er dort nicht, passt Feld F zum Geschäftsauto nicht zusammen. Das würde ich beim Arbeitgeber nachfragen, bevor Sie etwas abziehen.
> 2. **Kein Doppelabzug:** Privatanteil 0,9 % und gleichzeitig Fahrkostenabzug ist ein typischer Fehler.
> 3. **Verpflegung ist getrennt zu beurteilen** (Form. 4 Ziff. 2). Feld F sagt dazu nichts. Dort zählt Feld G.
> 
> **Gegenprobe (nur zur Abgrenzung)**
> Bezahlt der Arbeitgeber ein GA ohne geschäftliche Notwendigkeit, bleibt Feld F leer. Der Wert steht in Ziff. 2.3, und die Kosten sind in Form. 4 bis zum Maximalabzug abziehbar (StB 39 Nr. 3 Ziff. 4.1, `sg-stb-39-3__c0013`/`c0014`).
> 
> **Zum Maximalabzug**
> Er beträgt 2025 für Kanton und Gemeinde CHF 8'000 und für den Bund CHF 3'300 (StB 39 Nr. 3 Ziff. 3, `sg-stb-39-3__c0011`). Bei angekreuztem Feld F kommt er nicht zur Anwendung.
> 
> **Offen**
> Das Wiki enthält für SG 2025 keinen Beispielfall «Geschäftsauto + Feld F». Die Antwort stützt sich auf die Wegleitung und Art. 18a StV. Die fachliche Beurteilung bleibt bei Ihnen (SB/ML).

## q04

**Frage:** Wie hoch ist der maximale Fahrkostenabzug 2025 in TG (Staatssteuer) und beim Bund, und welcher km-Ansatz gilt für das Auto?

**Soll (Referenz):** TG 2025 Staat max. CHF 6'000 (tg-stg__par-29), Bund max. CHF 3'300 (bund-dbg-2025__art-26); Auto TG gestaffelt 0.60/0.50/0.40 je nach Jahres-km, Bund 0.70.

**Antwort des Agenten** (33.5 s · Tools: 7 Aufrufe read, exec):

> Die Quick-Seiten nennen beim Bund einen Widerspruch und beim TG-Auto-Ansatz eine Staffelung. Ich schaue deshalb in die Detailseiten und Chunks.
> 
> **Steuerjahr 2025, Fahrkosten Wohn-/Arbeitsstätte. Die Fachperson sollte die Punkte unter «Vorbehalte» prüfen.**
> 
> | | Maximalabzug pro Person | Auto (Privatauto) |
> |---|---|---|
> | **TG Staats- und Gemeindesteuer** | **CHF 6'000** pro Jahr | **Gestaffelt:** bis 3'000 km CHF 0.60 · 3'001–5'000 km CHF 0.50 · über 5'000 km CHF 0.40 |
> | **Direkte Bundessteuer** | **CHF 3'300** pro Jahr | **CHF 0.70/km**, einheitlich |
> 
> **Fundstellen**
> - TG Maximum: «bis zu einem Maximalbetrag von Fr. 6'000», § 29 Abs. 1 Ziff. 1 StG TG (`tg-stg__par-29`). Die Weisung StP 29 Nr. 2 und die Wegleitung TG 2025 S. 37–38 bestätigen dies. Das Maximum gilt für alle Fahrkosten zusammen, inklusive Wochenaufenthalt und Nebenerwerb. Es wird auch bei unterjähriger Steuerpflicht oder Teilzeit nicht gekürzt. Status ☑️ agent-geprüft.
> - TG km-Ansatz: § 1 Abs. 1 Ziff. 3 BKV TG (`tg-bkv__par-1`). Die Staffel ist kumulativ. 8'000 km ergeben CHF 4'000 (StP 29 Nr. 2). Die km-Ansätze enthalten die Parkgebühren. Status ☑️.
> - Bund Maximum: Art. 26 Abs. 1 lit. a DBG, Fassung 2025 (`bund-dbg-2025__art-26`). Dazu kommt ESTV-Rundschreiben RS 2-210 Ziff. 1.1 (`bund-rs-2-210__c0002`). Status ☑️.
> - Bund km-Ansatz: Anhang Ziff. 2 BKV, «Autos | pro Fahrkilometer | –.70» (`bund-bkv-2025__anhang-1`). Status ☑️.
> 
> **Vorbehalte**
> - **Auto nur ausnahmsweise:** Beide Auto-Ansätze gelten nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung nicht zumutbar ist. Sonst wird nur der ÖV-Betrag anerkannt. Beim Bund sind es die tatsächlichen Kosten bis maximal CHF 3'300.
> - **Widerspruch beim Bund-Maximum:** Die ESTV-Wegleitung 2a 2025 (S. 6, `bund-wl-2a-2025__c0042`) nennt noch «3200 Franken». Das Gesetz und das RS 2-210 sagen CHF 3'300. Das Wiki wendet nach der Rangfolge 3'300 an und geht davon aus, dass die Wegleitung nicht nachgeführt wurde. Die Fachperson sollte das zur Kenntnis nehmen.
> - **Lücke im Chunk:** In `tg-bkv__par-1` endet die Staffel mit «d. …». Ob dort noch eine weitere Stufe steht, sollte man im Original-PDF unter `raw/tg/2025/` prüfen. Die Berechnungsbeispiele in StP 29 Nr. 2 stützen die drei genannten Stufen.
> - **Nicht übertragbar:** Der Bund-Ansatz von CHF 0.75/km gilt erst ab 2026 und darf für 2025 nicht verwendet werden.
> 
> Die Werte stammen aus den Wiki-Quellen und sind nicht von einer Fachperson verifiziert (✅).

## q05

**Frage:** Welcher km-Ansatz für Autos gilt 2026 bei der direkten Bundessteuer?

**Soll (Referenz):** CHF 0.75 pro km (bund-mm-2025-09-11-kalte-progression-2026__c0004; RS 2-215).

**Antwort des Agenten** (31.7 s · Tools: 8 Aufrufe read, read, memory_search, memory_get):

> **Direkte Bundessteuer, Steuerjahr 2026: CHF 0.75 pro Fahrkilometer** für das Privatauto. Im Vorjahr 2025 waren es CHF 0.70.
> 
> - **Bedingung:** Der Abzug gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist.
> - **Maximum:** Die Fahrkosten zwischen Wohn- und Arbeitsstätte sind insgesamt auf CHF 3'300 pro Jahr begrenzt (Art. 26 Abs. 1 lit. a DBG).
> - **Künftige Anpassung:** Der Ansatz ist neu an den jährlichen TCS-Kilometerpreis gekoppelt. Er kann in Zukunft auch sinken.
> - **Fundstellen:**
>   - ESTV-Mitteilung vom 11.09.2025: «Der Abzug wird auf 75 Rappen pro Kilometer erhöht (bisher 70 Rappen).» (`bund-mm-2025-09-11-kalte-progression-2026__c0004`)
>   - RS 2-215, S. 1: «Fahrkosten für Automobile pro Kilometer 0.70 0.75» (`bund-rs-2-215__c0004`)
>   - Rechtsgrundlage: Art. 5 Abs. 2 lit. b BKV, Anhang Ziff. 2
> - **Status:** ☑️ agent-geprüft, also noch nicht von der Fachperson verifiziert.
> 
> Für Motorräder mit weissem Kontrollschild gelten 2026 unverändert CHF 0.40 pro km. Für Velo, Motorfahrrad und Motorrad mit gelbem Kontrollschild gilt eine Pauschale von CHF 700.
> 
> Die Kantone sind getrennt zu prüfen. AR, ZH und SG nennen für 2026 ebenfalls CHF 0.75 pro km. TG habe ich nicht geprüft.

## q06

**Frage:** Maximaler Säule-3a-Abzug 2025 für eine Arbeitnehmerin mit Pensionskasse? Und für eine Selbständige ohne 2. Säule?

**Soll (Referenz):** Mit 2. Säule CHF 7'258; ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288 (bund-bsv-masszahlen-2025-2026__c0003).

**Antwort des Agenten** (29.8 s · Tools: 3 Aufrufe read, exec):

> **Säule 3a, Steuerjahr 2025**
> 
> | Fall | Maximaler Abzug 2025 |
> |---|---|
> | Arbeitnehmerin mit Pensionskasse | **CHF 7'258** |
> | Selbständige ohne 2. Säule | **20 % des Erwerbseinkommens, höchstens CHF 36'288** |
> 
> Die Beträge sind beim Bund (DBG) und in AR, SG, TG und ZH identisch. Der Kanton ändert den Höchstabzug also nicht. Alle Kantone verweisen auf Art. 82 BVG und Art. 7 BVV 3.
> 
> **Herleitung**
> - **Mit Pensionskasse:** Das sind 8 % des oberen BVG-Grenzbetrags von CHF 90'720 (Art. 7 Abs. 1 lit. a BVV 3).
> - **Ohne 2. Säule:** Es gelten 20 % des Erwerbseinkommens, aber höchstens 40 % des oberen BVG-Grenzbetrags (Art. 7 Abs. 1 lit. b BVV 3). Die Obergrenze von CHF 36'288 erreichst du ab einem Erwerbseinkommen von CHF 181'440. Bei einem Einkommen von CHF 100'000 wären es zum Beispiel nur CHF 20'000.
> - **Selbständige:** «Erwerbseinkommen» ist das Einkommen aus der selbständigen Erwerbstätigkeit nach Abzug der AHV-Beiträge. Diese Definition steht nicht in den Fundstellen unten. Sie ist mein Hintergrundwissen und im Wiki nicht belegt; bitte vor der Anwendung prüfen. Die Beiträge werden nicht der Erfolgsrechnung belastet, sondern separat abgezogen (WL SG 2025 S. 26).
> - **Ehepaare:** Sind beide erwerbstätig, hat jede Person ihren eigenen Abzug mit eigenem Vorsorgevertrag (Art. 7 Abs. 2 BVV 3).
> 
> **Zu beachten**
> - Es zählt nur, was bis zum 31.12.2025 tatsächlich einbezahlt wurde.
> - Ein nachträglicher Einkauf in die Säule 3a ist für 2025 nicht abziehbar. Er ist erst ab Steuerjahr 2026 möglich, für Beitragslücken ab 2025.
> - Wer nur teilweise einer Vorsorgeeinrichtung angeschlossen ist, braucht eine Einzelfallprüfung. Das habe ich im Wiki nicht gesondert geprüft.
> 
> **Fundstellen und Status**
> - Beträge: BSV Masszahlen 25/26 S. 1, Ziff. 9 (`bund-bsv-masszahlen-2025-2026__c0003`), Status ☑️ agent-geprüft.
> - Regel: Art. 7 BVV 3 (`bund-bvv3__art-7`). Weitere Fundstellen sind `quick/vergleich-2025.md` und `wiki/themen/saeule-3a.md`.
> - Kantone: ZH und SG sind ☑️ (WL ZH 2025 S. 15, WL SG 2025 S. 26). AR (Art. 35 StG AR) und TG (WL TG 2025 S. 20) sind erst 🟡 extrahiert.
> - Nichts davon ist durch eine Fachperson verifiziert. Die fachliche Beurteilung bleibt bei SB/ML.

## q07

**Frage:** Kinderabzug 2025 in AR für ein 10-jähriges Kind – und beim Bund?

**Soll (Referenz):** AR 2025: CHF 7'400 (4.–15. Altersjahr; Anhang 1 StG, ar-stg-anhang-kp__c0001); Bund CHF 6'800 (Art. 35 DBG) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (45.6 s · Tools: 10 Aufrufe read, memory_search, exec):

> Ich habe die Werte für AR und Bund 2025 im Wiki nachgeschlagen und die Altersstufen im AR-Detail geprüft. Hier das Ergebnis.
> 
> **Kinderabzug 2025 für ein 10-jähriges Kind**
> 
> | | Betrag | Fundstelle | Status |
> |---|---|---|---|
> | **AR** (Staats- und Gemeindesteuer) | **CHF 7'400** (Schulalter) | Art. 38 Abs. 1 lit. a Ziff. 2 StG AR i.V.m. Anhang 1 (Beträge per 1.1.2024) – `ar-stg-anhang-kp__c0001`; WL AR 2025 S. 2 – `ar-wl-2025__c0005` | ☑️ agent-geprüft |
> | **Bund** (direkte Bundessteuer) | **CHF 6'800** | Art. 35 Abs. 1 lit. a DBG (Fassung 2025) – `bund-dbg-2025__art-35` | ☑️ agent-geprüft |
> 
> **AR-Staffelung nach Alter (2025):**
> - bis Vollendung des 4. Altersjahrs: CHF 5'300
> - ab 4. bis Vollendung des 15. Altersjahrs: **CHF 7'400** (hier einschlägig)
> - ab 15. Altersjahr bis Volljährigkeit sowie Ausbildung bis 26: CHF 11'600
> 
> Ein 10-jähriges Kind liegt eindeutig in der mittleren Stufe. Der Gesetzestext nennt die unindexierten Beträge, massgebend sind Anhang 1 und die Wegleitung 2025.
> 
> **Beim Bund** gibt es keine Altersstaffelung. Der Abzug von CHF 6'800 gilt für jedes minderjährige oder in Ausbildung stehende Kind, für dessen Unterhalt die steuerpflichtige Person sorgt.
> 
> **Weitere kinderbezogene Positionen 2025 (nicht Teil des Kinderabzugs):**
> - **Bund:** Zusätzlich gibt es einen Abzug vom Steuerbetrag von CHF 263 pro Kind (Art. 36 DBG, `bund-dbg-2025__art-36-t4`, ☑️). Ich habe nur den Wert aus den Eckwerten gelesen, nicht den Chunk selbst.
> - **Versicherungsabzug-Zuschlag pro Kind:** AR CHF 1'000, Bund CHF 700.
> - **AR Vermögen:** Sozialabzug von CHF 25'000 pro Kind (Art. 51 StG AR).
> 
> **Annahmen und Vorbehalte:**
> - Ich bin von Wohnsitz in AR am 31.12.2025 ausgegangen. Das Kind ist minderjährig, und die steuerpflichtige Person sorgt für seinen Unterhalt.
> - Bei getrennt besteuerten Eltern mit gemeinsamer Sorge wird der Bundesabzug hälftig aufgeteilt, wenn keine Unterhaltsbeiträge für das Kind abgezogen werden (Art. 35 Abs. 1 lit. a DBG). Für AR habe ich die Voraussetzungen bei getrennt besteuerten Eltern nicht geprüft.
> - Die Beträge gelten nur für 2025. Im AR-Detail zu 2026 steht der Wert «Vorschulalter» als ⚠️ strittig, also nichts von 2025 auf 2026 übertragen. Die fachliche Beurteilung bleibt bei der Fachperson.

## q08

**Frage:** Versicherungsabzug ZH 2025 für ein Ehepaar mit 2 Kindern, beide mit Pensionskasse (Staatssteuer und Bund)?

**Soll (Referenz):** ZH Staat: 5'800 + 2 × 1'300 = 8'400; Bund: 3'700 + 2 × 700 = 5'100 (zh-stg-2025__par-31-t2, bund-dbg-2025__art-33).

**Antwort des Agenten** (33.2 s · Tools: 7 Aufrufe read):

> **Versicherungsabzug ZH 2025, Ehepaar mit 2 Kindern, beide mit Pensionskasse (gemeinsame Veranlagung, beide Kinder mit vollem Kinderabzug)**
> 
> | | Staatssteuer ZH | Direkte Bundessteuer |
> |---|---|---|
> | Grundbetrag Ehepaar (mit Beiträgen an 2. Säule/3a) | CHF 5'800 | CHF 3'700 |
> | Zuschlag je Kind | 2 × CHF 1'300 = CHF 2'600 | 2 × CHF 700 = CHF 1'400 |
> | **Maximalabzug** | **CHF 8'400** | **CHF 5'100** |
> 
> Die Pensionskassenbeiträge zählen als Beiträge an die 2. Säule. Deshalb gilt der Grundbetrag und nicht die um die Hälfte erhöhte Limite von CHF 8'700 (Staat) bzw. CHF 5'550 (Bund). Diese erhöhte Limite gilt nur, wenn weder Pensionskasse noch Säule 3a bezahlt wurde. Das Wiki nennt dafür keine Einzelfallregel für Ehepaare mit nur einem Vorsorgeverhältnis. Bei einem Ehepaar, bei dem nur ein Partner in der Pensionskasse ist, wäre das also separat zu klären.
> 
> **Was tatsächlich abgezogen wird**
> - Der Abzug ist der niedrigere Betrag aus den bezahlten Prämien und Sparzinsen (Teil A) und dem Maximalabzug (Teil B). Das geschieht im Formular 365 Teil C, der Übertrag geht in Ziff. 15 (Code 270).
> - Die bezahlten Prämien und Sparzinsen sind netto, also nach Abzug der erhaltenen Prämienverbilligung. In ZH ist die Verbilligung meist schon mit den Krankenkassenprämien verrechnet. Sie darf dann nicht nochmals abgezogen werden.
> - Nicht aufzuführen sind Prämien, die schon im Lohnausweis abgezogen sind (NBUV), sowie Mobiliar-, Haftpflicht- und Motorfahrzeugversicherungen.
> - Der Kinderzuschlag setzt voraus, dass für das Kind der Kinderabzug nach § 34 StG geltend gemacht werden kann. Bei getrennt besteuerten Eltern mit hälftigem Kinderabzug wird er halbiert, also auf CHF 650 (Staat) bzw. CHF 350 (Bund).
> - Der Bund rechnet auf demselben Formular 365 in einer eigenen Spalte.
> 
> **Fundstellen (Steuerjahr 2025, Status ☑️ agent-geprüft)**
> - Staat: § 31 Abs. 1 lit. g StG ZH, `zh-stg-2025__par-31-t2`. Das ist der Gesetzestext mit Fr. 5800, der Erhöhung um die Hälfte und Fr. 1300 je Kind.
> - Staat und Bund: Formular 365 ZH 2025, Teil B Ziff. 1 und 3, `zh-form-365-2025__c0002`. Dort stehen auch die Bundesbeträge CHF 3'700 und CHF 700. Das Formular habe ich im Chunk gegengelesen.
> - Bund: Art. 33 DBG, Fassung 2025 (`bund-dbg-2025__art-33-t2` und `__art-33-t5`). Die Beträge nach der Anpassung an die kalte Progression stehen in RS 2-210 S. 2 (`bund-rs-2-210__c0006`).
> - Wegleitung ZH 2025 Ziff. 15, S. 15 (`zh-wl-2025__c0084` bis `__c0086`).
> 
> Die Rechnung (5'800 + 2 × 1'300 und 3'700 + 2 × 700) ist meine eigene Addition der Tabellenwerte. Sie steht so nicht als Beispiel in der Wegleitung. Die fachliche Beurteilung bleibt bei SB/ML.

## q09

**Frage:** Wie hoch ist der Kinderdrittbetreuungsabzug 2025 im Kanton ZH, und gilt 2026 ein anderer Wert?

**Soll (Referenz):** ZH 2025 CHF 25'000 (StG Nachtrag 127, zh-stg-2025__par-31-t4); 2026 CHF 25'300 (zh-stg-2026__par-31-t3). Die VKP ab 2024 (10'400) ist überholt.

**Antwort des Agenten** (30.4 s · Tools: 7 Aufrufe read, exec, exec):

> Ja, 2026 gilt ein anderer Wert für die Staats- und Gemeindesteuer. Bei der direkten Bundessteuer bleibt der Betrag gleich.
> 
> **Kinderdrittbetreuungsabzug im Kanton ZH, pro Kind (§ 31 Abs. 1 lit. j StG ZH)**
> 
> | | Steuerjahr 2025 | Steuerjahr 2026 |
> |---|---|---|
> | Staats-/Gemeindesteuer | **CHF 25'000** | **CHF 25'300** |
> | Direkte Bundessteuer (Art. 33 Abs. 3 DBG) | CHF 25'800 | CHF 25'800 |
> 
> Die Fundstellen für Staats- und Gemeindesteuer sind `zh-stg-2025__par-31-t4` für 2025 und `zh-stg-2026__par-31-t3` für 2026. Beide Wortlaute habe ich direkt im Chunk geprüft. Der Status im Wiki ist ☑️ (agent-geprüft), nicht ✅ verifiziert.
> 
> Für den Bundesbetrag stütze ich mich auf das Themenblatt `wiki/themen/kinderdrittbetreuung.md`. Diese Chunks habe ich nicht selbst geöffnet.
> 
> **Bedingungen (2025 und 2026 gleich)**
> - Das Kind hat das 14. Altersjahr noch nicht vollendet.
> - Das Kind lebt im gleichen Haushalt wie die Person, die für seinen Unterhalt sorgt.
> - Die Kosten müssen nachgewiesen sein.
> - Die Kosten stehen im direkten kausalen Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.
> - Im Formular steht der Abzug unter Ziff. 16.6, Code 376. Bei der Zuordnung stütze ich mich auf das Themenblatt, nicht auf die Zuordnungsseiten.
> 
> **Halber Abzug bei Konkubinat oder alternierender Obhut mit gemeinsamer Sorge**
> - 2025: Staat CHF 12'500, Bund CHF 12'900 (WL ZH 2025, `zh-wl-2025__c0109`).
> - 2026: Staat CHF 12'650, Bund CHF 12'900 (WL ZH 2026 UJ, `zh-wl-2026-uj__c0107`).
> 
> **Vorbehalte**
> - Die alte Verordnung (VKP ab 2024, `zh-vkp-2024-zstb__c0005`) nennt noch CHF 10'400. Sie ist durch das Gesetz überholt, denn Gesetz und Wegleitung gehen vor.
> - Für 2026 gibt es im Wiki erst die Wegleitung für unterjährige Steuerpflicht (WL 2026 UJ). Das reguläre ZH-Formular und die reguläre Wegleitung 2026 sind noch nicht publiziert (Stand 09.11.2026). Der Gesetzeswert von CHF 25'300 ist davon nicht berührt. Ziffer und Code im regulären Formular sollten Sie aber prüfen.
> 
> Die fachliche Beurteilung bleibt bei Ihnen (SB/ML).

## q10

**Frage:** Gibt es im Kanton TG einen Zweiverdienerabzug für die Staatssteuer?

**Soll (Referenz):** Nein, TG kennt keinen kantonalen Zweiverdienerabzug (nur Bund: 50 %, 8'600–14'100).

**Antwort des Agenten** (31.9 s · Tools: 10 Aufrufe read, read):

> **Nein.** Im Kanton Thurgau gibt es für die Staats- und Gemeindesteuer keinen Zweiverdienerabzug. Das gilt für die Steuerjahre 2025 und 2026. Den Abzug gibt es nur bei der direkten Bundessteuer.
> 
> **Staats- und Gemeindesteuer TG (2025 und 2026):**
> - Die Steuerpraxis des Kantons hält fest: «Im Gesetz über die Staats- und Gemeindesteuern des Kantons Thurgau ist kein Zweiverdienerabzug vorgesehen.» Fundstelle: `tg-stp-34-25__c0001` (StP 34 Nr. 25, gilt für 2025 und 2026).
> - Die Wegleitung sagt es gleich: «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.» (sic, Wortlaut so in der Quelle.) Fundstellen: WL TG 2025 S. 23, Ziff. 18 (`tg-wl-2025__c0104`) und WL TG 2026 S. 23, Ziff. 18 (`tg-wl-2026__c0103`).
> 
> **Direkte Bundessteuer (Art. 33 Abs. 2 DBG), für beide Jahre unverändert:**
> - Der Abzug beträgt 50 % des niedrigeren Erwerbseinkommens, mindestens Fr. 8'600 und höchstens Fr. 14'100 (WL TG 2025 und 2026, je S. 23, Ziff. 18).
> - Als Erwerbseinkommen zählt das Einkommen nach Berufsauslagen sowie nach Abzug der Beiträge an die 2. Säule und die Säule 3a.
> - Liegt das so berechnete niedrigere Einkommen unter Fr. 8'600, ist nur dieser Teilbetrag abziehbar.
> - Voraussetzung ist eine rechtlich und tatsächlich ungetrennte Ehe oder eingetragene Partnerschaft, in der beide ein Erwerbseinkommen erzielen.
> - Im Formular 1 steht der Abzug unter Ziff. 18 (Code 356), und zwar nur in der Bundesspalte. Ich habe die Ziffer und den Code der Themenseite entnommen und nicht am Formular geprüft.
> 
> **Praxishinweis:** Im Kantonsteil bleibt Ziff. 18 leer. Ein Abzug dort ist ein typischer Fehler.
> 
> Status: Die Werte stehen im Wiki als ☑️ agent-geprüft, nicht als ✅ verifiziert. Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Quellen im Wiki: `steuerwiki/wiki/themen/zweiverdienerabzug.md`, `steuerwiki/quick/werte-tg-2025.md`, `steuerwiki/quick/werte-tg-2026.md`.

## q11

**Frage:** SG 2025: Pauschale für übrige Berufskosten? Wie wird sie berechnet?

**Soll (Referenz):** SG 2025: CHF 700 + 10 % des Nettolohns, max. CHF 2'400 (Art. 21 StV SG, WL SG 2025).

**Antwort des Agenten** (33.0 s · Tools: 6 Aufrufe read):

> **SG 2025, Staats- und Gemeindesteuer: Pauschale für übrige Berufskosten**
> 
> **Formel:** Fr. 700 + 10 % der Nettoeinkünfte, höchstens Fr. 2'400.
> - Rechtsgrundlage ist [Art. 21 Abs. 1 StV SG](steuerwiki/chunks/sg/2025/sg-stv/sg-stv__art-21.md). Die Wegleitung bestätigt die Formel in Ziff. 10.3 (Formular 4 Ziff. 3.1, [WL SG 2025 S. 24](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0080.md)).
> - Ein Minimum gibt es nicht. Die Quellen nennen nur den Fixbetrag, den Prozentsatz und das Maximum.
> 
> **Basis «Nettoeinkünfte»:**
> - Das sind die Bruttoeinkünfte abzüglich der Prämien und Beiträge nach Art. 45 Abs. 1 Bst. d und f StG, ausgenommen Einkäufe von Beitragsjahren (Art. 21 Abs. 2 StV SG).
> - Laut Wiki-Zusammenfassung der Wegleitung sind das AHV/IV/EO/ALV, UV und BVG, ohne Einkäufe. Den Wortlaut dieser Aufzählung habe ich nicht im Original geprüft.
> - Auf dem Formular nimmst du den Nettolohn aus Lohnausweis Ziff. 11 bzw. Ziff. 1.1.
> 
> **Rechenbeispiele** (meine Berechnung, nicht aus der Wegleitung):
> - Nettolohn 10'000: 700 + 1'000 = **1'700**.
> - Nettolohn 17'000: 700 + 1'700 = **2'400**, die Kappung wird erreicht.
> - Nettolohn 80'000: 700 + 8'000 = 8'700, begrenzt auf **2'400**.
> 
> Ab einem Nettolohn von Fr. 17'000 gilt also immer das Maximum von Fr. 2'400.
> 
> **Weitere Regeln:**
> - **Pauschale oder effektiv:** Beides zusammen geht nicht. Höhere tatsächliche Kosten sind gegen Nachweis abziehbar (Art. 21 Abs. 3 StV SG). Dafür gehören sie auf ein Beiblatt zu Formular 4 (Ziff. 3.2) und ersetzen die Pauschale vollständig.
> - **Codes:** Pauschale Code 416 (Person 1) bzw. 466 (Person 2). Effektive Kosten Code 418 bzw. 468.
> - **Arbeitslosentaggelder:** Die Pauschale kann bei Bezug von ALV-Leistungen sinngemäss abgezogen werden.
> - **Pauschalspesen des Arbeitgebers:** Bei nicht ereignisbezogenen Pauschalspesen kann die Pauschale nicht zusätzlich geltend gemacht werden.
> - **Arbeitszimmer/Homeoffice:** Das ist grundsätzlich mit der Pauschale abgegolten, es gibt keine Homeoffice-Pauschale. Effektive Kosten sind nur bei beruflicher Notwendigkeit möglich ([StB 39 Nr. 1](steuerwiki/chunks/sg/dauernd/sg-stb-39-1/sg-stb-39-1__c0005.md)).
> - **Nebenerwerb:** Das ist eine separate Pauschale (Formular 4 Ziff. 5): 20 %, mindestens Fr. 800, höchstens Fr. 2'400 ([StB 39 Nr. 9](steuerwiki/chunks/sg/dauernd/sg-stb-39-9/sg-stb-39-9__c0002.md)).
> 
> **Direkte Bundessteuer, andere Regel:** Beim Bund gilt 3 % des Nettolohns, mindestens Fr. 2'000 und höchstens Fr. 4'000 (Anhang BKV 2025, [bund-bkv-2025__anhang-1](steuerwiki/chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md)). Die SG-Formel «700 + 10 %» gilt dort nicht. Wie die Bundespauschale in der SG-Steuererklärung ausgewiesen wird, habe ich nicht geprüft.
> 
> **Offener Punkt:** Eine Kürzung bei Teilzeit oder unterjähriger Tätigkeit nennt das Wiki für SG nur im MB 8/2026 für unterjährige Steuerpflicht. Für 2025 habe ich dazu keine Regel geprüft.
> 
> **Status:** ☑️ agent-geprüft (nicht von der Fachperson verifiziert). Steuerjahr 2025, Quellen jeweils verlinkt.

## q12

**Frage:** Pauschalabzug Liegenschaftsunterhalt in AR für ein 8-jähriges Einfamilienhaus – und wie in ZH?

**Soll (Referenz):** AR: 10 % (Gebäude bis 10 Jahre) bzw. 20 % des Bruttoertrags, nur bis Bruttomietertrag 100'000 (Art. 25 StV AR, MB 03); ZH: einheitlich 20 % ohne Altersstaffel (ZStB 30.2).

**Antwort des Agenten** (39.7 s · Tools: 7 Aufrufe read, read, exec):

> Für ein 8-jähriges Einfamilienhaus gilt in AR ein Pauschalabzug von **10 %**, in ZH von **20 %**. Die Prozentsätze sind für 2025 und 2026 gleich. Rechnungsbasis ist bei Selbstnutzung der Brutto-Eigenmietwert, bei Vermietung der Brutto-Mietertrag.
> 
> | | Satz | Basis | Fundstelle (2025/2026) | Status |
> |---|---|---|---|---|
> | **AR** (Staats-/Gemeindesteuer) | **10 %** (Gebäude bis 10 Jahre) | Eigenmietwert bzw. Bruttomietertrag | Art. 25 Abs. 1 StV AR, MB AR 03 Ziff. 1 (`ar-mb-03__c0004`, `ar-stv__art-25`) | ☑️ |
> | **ZH** (Staats-/Gemeindesteuer) | **20 %** (einheitlich, keine Altersstaffelung) | Brutto-Mietertrag bzw. -Mietwert | ZStB 30.2 Ziff. II (`zh-zstb-30-2__c0002`) | ☑️ |
> | **Bund** (DBG, in beiden Kantonen) | **10 %** (Gebäude bis 10 Jahre) | Brutto-Mietertrag bzw. Brutto-Eigenmietwert | Art. 5 Abs. 2 lit. a LKV (`bund-lkv__art-5`) | ☑️ |
> 
> **Was in AR zu beachten ist**
> - Der Pauschalabzug ist nur zulässig, wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes höchstens CHF 100'000 beträgt. Sonst bleibt nur der Abzug der effektiven Kosten.
> - Das Alter des Gebäudes richtet sich nach dem Stichtag für die Vermögenssteuer der Steuerperiode. Bei 8 Jahren gilt die Stufe «bis 10 Jahre». Ab dem 11. Jahr sind es 20 %.
> - Das Wahlrecht zwischen Pauschale und effektiven Kosten besteht jedes Jahr und je Gebäude.
> - Formular: Ziff. 15 / Form. 7 Abschn. C (C1 Pauschale, C2 tatsächliche Kosten).
> 
> **Was in ZH zu beachten ist**
> - Das Wahlrecht besteht je Steuerperiode und Liegenschaft. Bei Pauschale ist nur der Baurechtszins zusätzlich abziehbar.
> - Bei vorwiegend geschäftlicher Nutzung ist keine Pauschale möglich.
> - Formular 2025: Form. 350 S. 2, Spalte Unterhalt, Codes 5731–57310. Formular 2026: Ziff. 6 / Liegenschaftenverzeichnis, Code 188 (Netto).
> 
> **Kanton und Bund getrennt rechnen:** In ZH gibt es kantonal 20 %, bei der direkten Bundessteuer aber nur 10 %. Der Abzug fällt in ZH also je nach Ebene unterschiedlich aus (WL ZH 2026 UJ, `zh-wl-2026-uj__c0192`). Die effektiven Kosten sind in beiden Kantonen die Alternative. Energiespar- und Umweltinvestitionen sind nur bei den effektiven Kosten abziehbar. In der Pauschale sind sie bereits enthalten.
> 
> **Offene Punkte**
> - **Steuerjahr:** Du hast keines genannt. Die Antwort gilt für 2025 und 2026. Eine abweichende Altersgrenze oder Regeländerung ist für beide Jahre in den Quellen nicht vermerkt.
> - **AR 2026:** Formular und Wegleitung AR 2026 sind noch nicht publiziert (Stand 09.11.2026). Der Wert stützt sich auf Verordnung und Merkblatt, die für 2025 und 2026 gelten.
> - **ZH 2026:** Das reguläre Formular 2026 liegt ebenfalls noch nicht vor. Die Ziffern oder Codes basieren auf der Fassung für unterjährige Steuerpflicht und sind am regulären Formular zu prüfen.
> - **Ab 2029:** Der Bundesrat will den Eigenmietwert auf 1. Januar 2029 abschaffen. Ob der Unterhaltsabzug bei Selbstnutzung dann bestehen bleibt, ist in den Wiki-Quellen nicht geklärt. Für 2025 und 2026 gilt das bisherige Recht.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson. Wenn du mir den ungefähren Eigenmietwert nennst, rechne ich dir die Pauschale für AR, ZH und Bund durch und vergleiche sie mit den effektiven Kosten.

## q13

**Frage:** TG: Welcher Einschlag gilt auf dem Eigenmietwert der selbstbewohnten Liegenschaft am Wohnsitz (Kanton vs. Bund)?

**Soll (Referenz):** TG: Abzug 40 % Kanton, 20 % Bund für dauernd selbstbewohntes Eigentum am Wohnsitz (tg-stg__par-23; WL TG 2025).

**Antwort des Agenten** (34.7 s · Tools: 7 Aufrufe read, read, exec):

> In Thurgau beträgt der Einschlag (Selbstnutzungsabzug) auf dem Mietwert bei der Staats- und Gemeindesteuer 40 % und bei der direkten Bundessteuer 20 %. Das gilt für 2025 und 2026 gleich.
> 
> | Ebene | Abzug auf dem Mietwert | Fundstelle |
> |---|---|---|
> | Staats- und Gemeindesteuer TG | **40 %** | § 23 Abs. 3 StG TG (`tg-stg__par-23`); StP 23 Nr. 1, Ziff. 3.4 (`tg-stp-23-1__c0005`) |
> | Direkte Bundessteuer | **20 %** | StP 23 Nr. 1, Ziff. 3.4 (`tg-stp-23-1__c0005`); WL TG 2025 S. 47 (`tg-wl-2025__c0225`); WL TG 2026 S. 47 (`tg-wl-2026__c0222`) |
> 
> Status: ☑️ agent-geprüft. Die Zitate habe ich in den Chunks gelesen.
> 
> Die Wegleitung formuliert es so: «kantonal einen Abzug von 40 % und beim Bund von 20 %. Dies ergibt den steuerbaren Eigenmietwert.»
> 
> **Voraussetzungen:**
> - Die Liegenschaft muss am Wohnsitz selbstgenutzt sein.
> - Keinen Abzug gibt es bei landwirtschaftlich geschätzten Liegenschaften, bei Zweit- und Ferienwohnungen und bei unentgeltlich oder unterpreislich an Nahestehende überlassenen Liegenschaften. Diese Mietwerte sind zu 100 % steuerbar.
> 
> **Praktisch:** Formular 7 TG weist darum zwei Nettoerfolge aus, einen für den Kanton und einen für den Bund. Dieser Nettoerfolg kommt in Ziff. 8.1 (Code 180) der Steuererklärung, jeweils getrennt nach Ebene.
> 
> **Hinweis zum Wiki:** Das Wiki hat zwei Stellen, die nicht zusammenpassen:
> - Die Eckwert-Seiten `quick/werte-bund-2025.md` und `quick/werte-bund-2026.md` führen für den Bund «n/a» und nennen keinen allgemeinen Prozentabzug. Das ist die bundesrechtliche Sicht nach Art. 21 DBG, wonach der Mietwert nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt wird.
> - Die TG-Quellen nennen für die DBSt ausdrücklich 20 %. Für Thurgau gilt deshalb 20 %.
> 
> Der Eigenmietwert bleibt bis und mit 2028 steuerbar. Die Abschaffung ist für den 01.01.2029 vorgesehen (Medienmitteilung des Bundesrats, `bund-mm-eigenmietwert-abschaffung__c0002`). Die fachliche Beurteilung bleibt bei SB/ML.

## q14

**Frage:** Bis wann kann ein Treuhänder im Kanton TG für seine Mandanten Fristerstreckung erhalten?

**Soll (Referenz):** Gewerbsmässige Treuhänder für Mandanten bis 31.12. des Deklarationsjahres (StP 155 Nr. 2).

**Antwort des Agenten** (31.4 s · Tools: 6 Aufrufe read, memory_search):

> **Antwort: bis längstens 31. Dezember des Deklarationsjahres.**
> 
> Das gilt für Treuhänder und Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen. Sie können im Kanton Thurgau für ihre Mandanten ein Fristerstreckungsgesuch längstens bis zum 31. Dezember des Deklarationsjahres beantragen. Quelle: [StP 155 Nr. 2, Chunk c0002](steuerwiki/chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0002.md). Die Regel gilt für die Steuerjahre 2025 und 2026. Die Quelle gilt für beide Jahre, und das Wiki führt sie für 2026 als unverändert (Stand 05.01.2026).
> 
> **Zum Vergleich: Private ohne Treuhänder** (gleiche Quelle, [c0001](steuerwiki/chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md)):
> - Das Gesuch geht an das Gemeindesteueramt.
> - Ein erstes Gesuch wird grundsätzlich bewilligt, längstens bis 30. September des Deklarationsjahres.
> - Weitere Gesuche werden in begründeten Fällen längstens bis 30. November des Deklarationsjahres gewährt.
> - Arbeitsüberlastung ist kein Grund.
> 
> **Praxishinweise:**
> - Über den 30. November hinaus werden weitere Gesuche abgewiesen, ausser es werden ausserordentliche Gründe glaubhaft gemacht. Dafür braucht es in der Regel eine substanziierte Sachdarstellung. Allgemeine Hinweise wie starke berufliche Inanspruchnahme des Vertreters oder fehlende Unterlagen genügen nicht ([c0002](steuerwiki/chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0002.md)).
> - Das Gesuch muss rechtzeitig, schriftlich und begründet gestellt werden, also vor Fristablauf ([WL TG 2026 S. 7–8](steuerwiki/chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0022.md)).
> - «Deklarationsjahr» bedeutet das Jahr der Einreichung. Für die Steuerperiode 2025 ist das 2026, für die Steuerperiode 2026 ist es 2027. Daraus ergibt sich als Frist der 31.12.2026 bzw. der 31.12.2027. Diese Ableitung steht nicht wörtlich in der Quelle.
> 
> **Nicht belegt:** Ob für Treuhänder-Sammelgesuche ein bestimmtes Verfahren oder eine Gebühr gilt, steht in den Wiki-Quellen nicht. Für natürliche Personen ist dort keine Gebühr genannt.
> 
> **Status:** Der Wert stammt aus der amtlichen Steuerpraxis des Kantons TG und ist im Wiki als Chunk abgelegt. Die Prüfung durch die Fachperson (✅ verifiziert) steht noch aus.

## q15

**Frage:** ZH: Bis wann ist die Steuererklärung 2025 einzureichen und wie lange wird höchstens Fristerstreckung gewährt?

**Soll (Referenz):** Einreichung bis 31.03.2026; Fristerstreckung längstens bis 30. November (ZStB 132.1 / WL ZH 2025).

**Antwort des Agenten** (37.5 s · Tools: 9 Aufrufe read):

> **Kanton Zürich, Steuerjahr 2025 (Staats-/Gemeindesteuer und direkte Bundessteuer in einer gemeinsamen Erklärung)**
> 
> **Einreichefrist:** 31. März 2026. Die Wegleitung sagt: «Die Steuererklärung ist bis am 31. März 2026 einzureichen.» (`zh-wl-2025__c0017`, WL ZH 2025 S. 7; Status ☑️ agent-geprüft). Die Bundessteuer hat keine eigene Erklärung. Der Kanton setzt die Frist (Art. 124 Abs. 2 DBG).
> 
> **Fristerstreckung:** Längstens bis 30. November 2026. Rechtzeitig eingereichten Gesuchen ist «längstens bis 30. November des der Steuerperiode folgenden Kalenderjahres» zu entsprechen (`zh-zstb-132-1-bis-2025__c0021`, ZStB 132.1 bis 2025, S. 8, G.II.2 b). Die ab 2026 gültige Fassung hat denselben Wortlaut (`zh-zstb-132-1__c0024`).
> 
> Weitere Punkte aus den Quellen:
> - **Gesuch:** Es muss vor Fristablauf beim Gemeindesteueramt eintreffen. Mahnfristen sind nicht erstreckbar (WL ZH 2025 S. 7).
> - **Erstes Gesuch:** Ein rechtzeitiges erstes Gesuch gilt ohne gegenteiligen schriftlichen Entscheid als stillschweigend bewilligt (`…c0023`).
> - **Über den 30. November hinaus:** Solche Gesuche werden abgewiesen, ausser es werden ausserordentliche Gründe glaubhaft gemacht. «Starke berufliche Inanspruchnahme» der Vertretung oder fehlende Unterlagen genügen nicht (`…c0021`).
> - **Von Amtes wegen bis 30. September:** Das gilt für im Kanton wohnhafte Selbständigerwerbende und für Steuerpflichtige mit Wohnsitz ausserhalb des Kantons (`zh-zstb-132-1__c0023`, Fassung 2026).
> 
> **Zur heutigen Lage (9. November 2026):**
> - Die ordentliche Frist vom 31. März 2026 ist abgelaufen. Eine abgelaufene Frist kann nicht mehr erstreckt werden, höchstens wiederhergestellt werden. Das setzt die Voraussetzungen von § 15 StV bzw. Art. 119 Abs. 2 und Art. 124 Abs. 4 DBG voraus (`zh-zstb-132-1__c0024`).
> - Ein früher gestelltes Gesuch deckt bis maximal 30. November 2026, also noch gut drei Wochen. Wer bis dahin nichts eingereicht hat, hat ein Mahnungs- und Bussenrisiko (Art. 174 DBG: Busse bis CHF 1'000).
> 
> **Offen und nicht belegt:**
> - Kosten der Fristerstreckung nennen die Quellen nicht.
> - Ob für die Fassung ZStB 132.1 ab 2026 auf das Steuerjahr 2025 noch die «bis 2025»-Fassung massgebend ist, habe ich nicht abschliessend geklärt. Der Wortlaut zur 30.-November-Grenze ist in beiden Fassungen identisch.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## q16

**Frage:** AR: Was kostet die zweite Fristverlängerung?

**Soll (Referenz):** CHF 25 (erste Verlängerung kostenlos, jede weitere CHF 25; MB 18 / WL AR 2025).

**Antwort des Agenten** (37.4 s · Tools: 4 Aufrufe read, exec):

> Das hängt vom Kanton ab. Kanton und Steuerjahr haben Sie nicht genannt, deshalb hier die Übersicht für die abgedeckten Kantone:
> 
> | Kanton | Kosten 2. Fristverlängerung | Fundstelle |
> |---|---|---|
> | **AR** (2025/2026) | **Fr. 25.–** Die erste Verlängerung ist kostenlos, jede weitere kostet Fr. 25.–. | WL AR 2025 S. 4 `^[ar-wl-2025__c0012]`; MB AR 18 (gültig ab 1.9.2025, «im Wiederholungsfall») `^[ar-mb-18__c0001]`. Status ☑️ |
> | **TG** (2025/2026) | **Fr. 30.–** Die erste Verlängerung ist gebührenfrei, für jedes weitere Gesuch wird eine Kanzleigebühr von Fr. 30 erhoben. | § 39b Abs. 2–3 StV TG `^[tg-stv__par-39b]`. Mit Mahngebühren ab der zweiten Mahnung (Fr. 50) hat das nichts zu tun. |
> | **SG** | Im Wiki nicht genannt. | Die Infoseite zur Fristverlängerung nennt keine Kosten. Bedingung ist, dass die fälligen Steuerrechnungen bezahlt sind `^[sg-info-fristverlaengerung__c0002]`. |
> | **ZH** | Im Wiki nicht genannt. | ZStB 132.1 regelt nur die Dauer: rechtzeitige Gesuche werden längstens bis 30. November des Folgejahres bewilligt `^[zh-zstb-132-1__c0024]`. |
> 
> - **TG, Zuständigkeit:** Bei natürlichen Personen entscheidet das Gemeindesteueramt `^[tg-stp-155-2__c0001]`. § 39b StV spricht von der «Steuerverwaltung». Ob die Fr. 30 bei natürlichen Personen genau so erhoben werden, habe ich nicht weiter geprüft. Bitte kurz bestätigen. Zusätzliche Gesuche werden in TG nur in begründeten Fällen und längstens bis 30. November bewilligt, Arbeitsüberlastung gilt nicht als Grund.
> - **Eigene Gebühren in TG:** Die Praxis zu juristischen Personen (monatliche Gesuche à Fr. 30) gilt nicht für natürliche Personen.
> 
> Für welchen Kanton und welches Steuerjahr brauchen Sie es? Bei SG und ZH müsste ich sonst «nicht im Wiki» sagen, und die fachliche Beurteilung liegt bei SB/ML.

## q17

**Frage:** Krankheitskosten SG 2025: Ab welchem Selbstbehalt sind sie abziehbar – und beim Bund?

**Soll (Referenz):** SG: Selbstbehalt 2 % (Art. 46 StG SG); Bund: 5 % (Art. 33 Abs. 1 lit. h DBG, KS 11).

**Antwort des Agenten** (31.5 s · Tools: 8 Aufrufe read):

> **SG 2025 (Staats- und Gemeindesteuer):** Krankheits- und Unfallkosten sind abziehbar, soweit Sie sie selbst tragen und sie **2 %** der Nettoeinkünfte übersteigen. Nettoeinkünfte sind die um die Abzüge nach Art. 39–45 StG verminderten steuerbaren Einkünfte (Ziff. 20 der Steuererklärung). Quelle: [Art. 46 Abs. 1 lit. a StG SG](steuerwiki/chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-46.md), bestätigt durch [WL SG 2025 S. 29, Ziff. 21.1](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0098.md). Status ☑️ agent-geprüft.
> 
> **Bund (direkte Bundessteuer 2025):** Der Selbstbehalt beträgt **5 %** der um die Aufwendungen nach Art. 26–33 DBG verminderten steuerbaren Einkünfte. Quelle: [Art. 33 Abs. 1 lit. h DBG (Fassung 2025)](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t3.md). Status ☑️ agent-geprüft.
> 
> Das KS 11a der ESTV gilt laut seiner Ziff. 7 erst ab Steuerperiode 2027. Für 2025 gilt weiterhin das KS 11 von 2005.
> 
> **Wichtig bei der Anwendung:**
> - Der Selbstbehalt gilt nur für Krankheits- und Unfallkosten. Behinderungsbedingte Kosten (Art. 46 Abs. 1 lit. abis StG SG, Art. 33 Abs. 1 lit. hbis DBG) sind **ohne Selbstbehalt** abziehbar. Sie gehören in Ziff. 21.2, Code 235.
> - Abziehbar ist nur der Nettobetrag nach Vergütungen von Krankenkasse und anderen Dritten. Krankenkassenprämien gehören nicht hierher, sondern in den Versicherungsabzug.
> - Die Kosten kommen im Kanton in Ziff. 21.1 (Formular 6, Codes 650/238/240). Sie gelten für Staats-/Gemeindesteuer und Bund, aber mit unterschiedlichem Selbstbehalt (2 % bzw. 5 %). Die beiden Beträge fallen daher verschieden aus.
> - Die Diätpauschale von CHF 2'500 zählt bei SG zu den Krankheitskosten und unterliegt dem Selbstbehalt. Sie gilt nicht bei Diabetes.
> 
> Die Beurteilung im Einzelfall bleibt bei der Fachperson.

## q18

**Frage:** PK-Einkauf CHF 20'000 wurde über den Lohn abgezogen (Lohnausweis Ziff. 10.2). Darf er nochmals in der Steuererklärung abgezogen werden?

**Soll (Referenz):** Nein – BVG-Einkauf über Lohnabzug (Lohnausweis Ziff. 10.2) ist bereits im Nettolohn berücksichtigt; nur direkt bezahlte Einkäufe separat abziehen.

**Antwort des Agenten** (38.3 s · Tools: 8 Aufrufe read):

> **Nein, nicht nochmals abziehen.** Die CHF 20'000 sind über den Lohn bereits steuerlich berücksichtigt.
> 
> **Warum:**
> - Der Nettolohn in Ziff. 11 des Lohnausweises ist der Bruttolohn (Ziff. 8) minus die Abzüge in Ziff. 9 und 10 (Ziff. 10.2 ist der vom Lohn abgezogene Einkauf). Dieser Nettolohn ist der «für die Steuererklärung massgebende» Betrag ([WL Lohnausweis 2026 Rz 47, Chunk `bund-wl-lohnausweis-2026__c0038`](steuerwiki/chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md)). Der Einkauf wirkt also schon über den tieferen Nettolohn. Ein zweiter Abzug wäre ein Doppelabzug.
> - Nur Einkäufe, die der Arbeitnehmer selbst bezahlt hat (nicht vom Lohn abgezogen), werden separat abgezogen. Dafür stellt die Vorsorgeeinrichtung eine Bescheinigung (Formular 21 EDP) aus ([Rz 46, Chunk `…__c0037`](steuerwiki/chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md)).
> 
> **Kantonale Bestätigung (nur die Kantone, deren Wegleitungstext ich geprüft habe):**
> - **SG 2025:** Sind die Beiträge im Nettolohn berücksichtigt, ist «ein nochmaliger Abzug unter Ziffer 13.2 ausgeschlossen» ([WL SG 2025 S. 26](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0086.md)).
> - **TG 2025:** Die ordentlichen Beiträge sind in der Regel schon vom Bruttolohn abgezogen und in Ziff. 1 berücksichtigt (Ziff. 15.2, [WL TG 2025 S. 21](steuerwiki/chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0093.md)). Dieser Text spricht von den *ordentlichen* Beiträgen. Er sagt nicht ausdrücklich etwas zum Einkauf in Ziff. 10.2. Die Aussage zum Einkauf stützt sich hier auf die Bundes-Wegleitung oben.
> - **ZH und AR:** Das Wiki führt die Regel im Themenbeitrag als Checkliste. Den Wortlaut der ZH- und AR-Wegleitung habe ich nicht separat geöffnet.
> 
> **Wo die CHF 20'000 trotzdem hingehören:**
> - Nichts in der Abzugsziffer für Einkäufe eintragen. Die Ziffern sind ZH 16.1, SG 13.2, TG 15.2, AR 13.2. Wenn nichts selbst bezahlt wurde, bleibt das Feld leer.
> - Hat die Person zusätzlich selbst Einkäufe bezahlt, kommen nur diese in die Ziffer, belegt mit der Bescheinigung der Vorsorgeeinrichtung.
> - Die CHF 20'000 dienen als Plausibilitätskontrolle: Ziff. 10.2 muss zur Einkaufsbescheinigung und zur Einkaufsberechnung der PK passen.
> 
> **Offene Punkte, die Sie klären sollten:**
> - **Kanton und Steuerjahr:** Sie haben beides nicht genannt (Wohnsitz am 31.12.). Die Grundregel ist bei Bund und den vier Kantonen gleich. Für die Ziffer und die Fundstelle brauche ich beides.
> - **Sperrfrist:** Der Abzug gilt nur, wenn innert 3 Jahren nach dem Einkauf kein Kapitalbezug folgt. Auch ein WEF-Vorbezug zählt als Kapitalbezug ([KS 17 Ziff. II.2.3](steuerwiki/chunks/bund/dauernd/bund-ks-17/bund-ks-17__c0012.md)). Gab es Einkauf und Kapitalbezug nahe beieinander, würde der Abzug nachträglich verweigert.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson. Der Status der Wiki-Seite ist «entwurf», die zitierten Wegleitungstexte habe ich im Original-Chunk gegengelesen.

## q19

**Frage:** Weiterbildungskosten CHF 15'000 (ZH, 2025), Arbeitgeber hat nichts bezahlt. Wie viel ist abziehbar (Kanton/Bund)?

**Soll (Referenz):** ZH Staat max. CHF 12'400 (zh-stg-2025__par-31-t4); Bund max. CHF 13'000 (bund-dbg-2025__art-33-t4).

**Antwort des Agenten** (35.9 s · Tools: 8 Aufrufe read):

> **Abziehbar bei CHF 15'000 Weiterbildungskosten, ZH, Steuerjahr 2025:**
> 
> | Ebene | Abzug | Maximum | Nicht abziehbar |
> |---|---|---|---|
> | **Staats-/Gemeindesteuer ZH** | **CHF 12'400** | CHF 12'400 | CHF 2'600 |
> | **Direkte Bundessteuer** | **CHF 13'000** | CHF 13'000 | CHF 2'000 |
> 
> Die Höchstbeträge gelten pro Person und Steuerjahr, einschliesslich Umschulungskosten. Bei der Staatssteuer ist der Maximalbetrag tiefer als beim Bund. Der Abzug wird für beide Steuerarten getrennt berechnet. Dass der Arbeitgeber nichts bezahlt hat, ist hier günstig: Beiträge Dritter müssten sonst von den Kosten abgezogen werden, bevor das Maximum greift.
> 
> **Fundstellen (alle Steuerjahr 2025):**
> - ZH Staat: § 31 Abs. 1 lit. k StG ZH, «bis zum Gesamtbetrag von Fr. 12 400» (`zh-stg-2025__par-31-t4`). Status ☑️ agent-geprüft.
> - Bund: Art. 33 Abs. 1 lit. j DBG, «13 000 Franken» (`bund-dbg-2025__art-33-t4`). Status ☑️ agent-geprüft.
> - Die Wegleitung ZH 2025, Ziff. 16.2, S. 16, nennt beide Beträge nebeneinander (`zh-wl-2025__c0093`).
> 
> **Voraussetzungen, die ich nicht prüfen kann:**
> 1. Es muss ein erster Abschluss auf Sekundarstufe II vorliegen. Alternativ muss das 20. Lebensjahr vollendet sein, und es darf nicht um Kosten bis zum ersten Sek.-II-Abschluss gehen.
> 2. Die Weiterbildung muss berufsorientiert sein. Hobby oder Liebhaberei ist nicht abziehbar.
> 3. Die CHF 15'000 müssen **selbst getragene** Kosten sein. Zahlungen von Dritten wie Bund oder Branchenverbänden sind abzuziehen. Beim Lohnausweis Ziff. 13.3 prüfen, ob der Arbeitgeber trotzdem etwas vergütet oder direkt ans Institut bezahlt hat. Direktzahlungen stehen dort nicht, mindern aber Ihre Kosten.
> 4. Mit der Weiterbildung zusammenhängende notwendige Kosten, etwa Fahrten zum Kursort, zählen in den Höchstbetrag hinein (KS 42 Ziff. 4.3).
> 5. Massgebend ist die Fälligkeit bzw. Zahlung im Jahr 2025, nicht der Kursbesuch (WL ZH 2025 S. 16). Die CHF 15'000 sollten also 2025 fällig oder bezahlt worden sein.
> 
> **Formular:** Die Eintragung erfolgt in Ziff. 16.2, Code 292. Dazu gehört das vollständig ausgefüllte Formular 367 «Berufsorientierte Aus- und Weiterbildungskosten», mit Staat und Bund getrennt je Person. Kursrechnungen und Zahlungsnachweise beilegen (Zuordnung ZH 2025, Formular 367 S. 1: `zh-form-367-2025__c0001`).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson. Das gilt besonders für Punkt 1 (Sek.-II-Abschluss bzw. Alter).

## q20

**Frage:** Spenden CHF 50 an eine gemeinnützige Organisation (TG 2025) – abziehbar?

**Soll (Referenz):** Nein – TG: Zuwendungen nur abziehbar, wenn sie CHF 200 übersteigen (StG TG § 34 Abs. 1 Ziff. 11); Bund: ab CHF 100.

**Antwort des Agenten** (38.4 s · Tools: 11 Aufrufe read, read):

> **Nein, nicht für sich allein.** Die 50 Franken liegen unter beiden Mindestschwellen. Die Schwellen gelten für alle Spenden des Jahres zusammen. Das gilt für Thurgau, Steuerjahr 2025, bei einer Organisation, die in der Schweiz wegen gemeinnütziger oder öffentlicher Zwecke steuerbefreit ist.
> 
> | Ebene | Regel 2025 | CHF 50 allein |
> |---|---|---|
> | **Staats-/Gemeindesteuer TG** | Abziehbar ist nur, was gesamthaft über CHF 200 liegt (Selbstbehalt), höchstens CHF 8'000 oder 20 % des Nettoeinkommens. | nicht abziehbar |
> | **Direkte Bundessteuer** | Abziehbar sind Spenden, wenn sie im Jahr gesamthaft mindestens CHF 100 erreichen, höchstens 20 % des Nettoeinkommens. Ohne Selbstbehalt. | nicht abziehbar |
> 
> Fundstellen:
> - Kanton: § 34 Abs. 1 Ziff. 11 StG TG, `tg-stg__par-34-t4`; StP 34 Nr. 23 Ziff. 2.2, `tg-stp-34-23__c0003`; Formular 6 TG 2025 S. 1, `tg-form-06-2025__c0002` (Zeile «abzüglich Selbstbehalt – 200.–»).
> - Bund: Art. 33a DBG, `bund-dbg-2025__art-33a`; StP 34 Nr. 23 Ziff. 2.3, `tg-stp-34-23__c0003`.
> - Status der Zuordnung zu Ziff. 23.2 in `quick/zuordnung-tg-2025.md`: ☑️ agent-geprüft.
> 
> **Falls es 2025 weitere Spenden gab:**
> - **Kanton:** Zählen Sie alle Spenden zusammen. Abziehbar ist nur der Teil über CHF 200. Mit 50 + 400 = 450 wären das CHF 250.
> - **Bund:** Erreicht das Total CHF 100, ist der volle Betrag abziehbar (50 + 400 = 450), bis zum 20-%-Deckel.
> - **Belege:** Quittungen sind erst ab CHF 1'000 pro Zuwendung einzureichen. Einzeln aufführen müssen Sie die Spenden im Formular 6 trotzdem, mit Name und Sitz der Organisation (`tg-form-06-2025__c0002`).
> 
> Mitgliederbeiträge sind keine abziehbaren Spenden. Die fachliche Beurteilung bleibt bei SB/ML.

## q21

**Frage:** Was ändert sich 2026 bei der Säule 3a (Einkauf) und wo wird das im ZH-Formular 2026 eingetragen?

**Soll (Referenz):** Ab 2026 Einkauf (Nachzahlung) Säule 3a für Beitragslücken ab 2025 (max. 7'258 pro Einkaufsjahr, BVV 3 Art. 7a, KS 18a); ZH-Formular 2026: Ziff. 14.3 (Code 264, Detailfelder 276/278).

**Antwort des Agenten** (39.1 s · Tools: 6 Aufrufe read, exec):

> **Kurzfassung:** Neu ist ab Steuerjahr 2026 der nachträgliche Einkauf in die Säule 3a. Im ZH-Formular gehört er in **Ziff. 14.3**, getrennt von den ordentlichen Beiträgen in Ziff. 14.1/14.2. Die Höchstbeträge der ordentlichen Beiträge bleiben gleich.
> 
> **Wichtig zur Datenlage:** Das reguläre ZH-Formular und die Wegleitung 2026 sind laut Wiki noch nicht publiziert (Stand 09.11.2026). Die Angaben stützen sich auf die Fassung für unterjährige Steuerpflicht (Formular 300 ZH 2026 UJ und Wegleitung 2026 UJ). Ziffern und Codes bitte am regulären Formular prüfen.
> 
> ## Was ändert sich 2026
> 
> **Unverändert (ordentliche Beiträge, Bund und ZH):**
> - Mit 2. Säule: CHF 7'258.
> - Ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens CHF 36'288.
> - Quellen: [BSV Masszahlen 25/26 S. 1](steuerwiki/chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md), [WL ZH 2026 UJ S. 14](steuerwiki/chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0075.md). Status ☑️ agent-geprüft.
> 
> **Neu: Einkauf für Beitragslücken** (Art. 7a/7b BVV 3, [Art. 7a](steuerwiki/chunks/bund/2025/bund-bvv3/bund-bvv3__art-7a-t1.md); ZH: [WL ZH 2026 UJ S. 14, Ziff. 14.3](steuerwiki/chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0077.md)):
> - **Ab wann:** Einkäufe sind ab der Steuerperiode 2026 möglich. Für 2025 ist kein Einkauf abziehbar.
> - **Welche Lücken:** nur Lücken, die ab dem 1.1.2025 entstanden sind. Ältere Lücken sind nicht einkaufbar.
> - **Voraussetzung 1:** In den Lückenjahren wurden AHV/IV/EO-Beiträge geleistet, die Person war also zu 3a-Beiträgen berechtigt.
> - **Voraussetzung 2:** Im Einkaufsjahr (2026) wurde der volle ordentliche Maximalbeitrag einbezahlt (CHF 7'258 bzw. 20 %, höchstens CHF 36'288).
> - **Obergrenze:** höchstens die Summe der Lücken der letzten zehn Jahre (frühestens ab 2025), pro Jahr aber maximal CHF 7'258.
> - **Beleg:** Bestätigung des Vorsorgeanbieters. Das Wiki führt dazu den Einkaufsnachweis und den Nachweis der AHV-Beitragsjahre.
> - **Zusätzlich beim Bund** (KS 18a, [S. 6](steuerwiki/chunks/bund/dauernd/bund-ks-18a/bund-ks-18a__c0017.md)):
>   - Eine Jahreslücke kann nur durch einen einzigen Einkauf ausgeglichen werden.
>   - Nach dem Bezug einer Altersleistung aus der Säule 3a ist kein Einkauf mehr möglich.
> 
> ## Eintrag im ZH-Formular 2026
> 
> Quelle: [Formular 300 ZH 2026 UJ S. 3](steuerwiki/chunks/zh/2026/zh-form-300-2026-uj/zh-form-300-2026-uj__c0008.md). Eine Zeile gilt für Staats- und Bundessteuer, es gibt je eine Spalte.
> 
> | Ziffer | Position | Code |
> |---|---|---|
> | 14.1 | Ordentliche 3a-Beiträge Person 1 | 260 (eff. 262) |
> | 14.2 | Ordentliche 3a-Beiträge Person 2 | 261 (eff. 263) |
> | **14.3** | **Einkauf Säule 3a** | **Person 1: 276 · Person 2: 278 · Hauptkolonne 264** |
> 
> - Den Einkauf nicht in Ziff. 14.1/14.2 miteinbeziehen, sondern separat in 14.3 eintragen.
> - Das 3a-Guthaben selbst gehört nicht ins Wertschriftenverzeichnis.
> 
> ## Offen / Vorbehalte
> - Zu Ziff. 14.3 gibt es kein Zahlenbeispiel der Wegleitung.
> - Die Rechtsgrundlage (BVV 3) ist für ZH nur über die Wegleitung belegt.
> - Unterjähriger Ein- oder Austritt, Grenzgänger und Teilzeit-PK-Anschluss sind in den erfassten Quellen nicht geklärt.
> - Für 2027 liegen keine Werte vor.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson (SB/ML).

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (47.8 s · Tools: 14 Aufrufe read, memory_search):

> Das Wiki beantwortet das für Bund, AR, SG, TG und ZH, Steuerjahre 2025 und 2026. Sie haben keinen Kanton genannt. Ich zeige deshalb das gemeinsame Prinzip und die kantonalen Unterschiede. Die Seite ist als Entwurf markiert und nicht von einer Fachperson verifiziert.
> 
> ## So funktioniert die Rückforderung
> 
> 1. **Satz:** Die Verrechnungssteuer auf Kapitalerträgen beträgt 35 % der steuerbaren Leistung (Art. 13 Abs. 1 lit. a VStG, `bund-vstg__art-13`, Bund 2025/2026).
> 2. **Berechtigter:** Anspruch hat, wer bei Fälligkeit der Leistung das Recht zur Nutzung des Vermögenswerts besass (Art. 21 Abs. 1 lit. a VStG, `bund-vstg__art-21`). Eine Rückerstattung ist unzulässig, wenn sie zu einer Steuerumgehung führen würde (Abs. 2).
> 3. **Verfahren:** Es gibt keinen separaten Antrag an die ESTV. Der Antrag läuft über die kantonale Steuererklärung (Wertschriftenverzeichnis, unterschrieben, mit Auszahlungskonto). Die Rückerstattung kommt also von der Kantonssteuerverwaltung, nicht vom Bund. Das Wiki zeigt das für ZH (`zh-wl-2026-uj__c0153`) und TG (`tg-wl-2026__c0166`).
> 4. **Verwirkung:** Wer mit Verrechnungssteuer belastete Einkünfte oder das zugehörige Vermögen nicht angibt, verliert den Anspruch (Art. 23 Abs. 1 VStG, `bund-vstg__art-23`). Das gilt nicht, wenn die Angabe fahrlässig unterblieb und die Einkünfte in einem noch nicht rechtskräftigen Veranlagungs-, Revisions- oder Nachsteuerverfahren nachgemeldet oder von der Behörde aufgerechnet werden (Abs. 2).
> 
> ## Wo der Anspruch ausgewiesen wird
> 
> Der Anspruch steht im Wertschriften- und Guthabenverzeichnis. Dort gehören die Bruttoerträge mit Verrechnungssteuerabzug (Dividenden Schweizer Gesellschaften) in Kolonne bzw. Spalte A. Der Anspruch ist 35 % vom Total A.
> 
> | Kanton | Formular | Anspruch | Fundstelle |
> |---|---|---|---|
> | AR (2025) | Formular 2 | «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A)», Code 999. Total A und B geht in Ziff. 4.1, Steuerwerte in Ziff. 30.1. | `ar-form-02-2025__c0007` |
> | SG (2025) | Formular 2 | Code 999, gleiche Logik, Übertrag in Ziff. 4.1 und 30.1. | `sg-form-2-2025__c0006` |
> | TG (2026) | Formular 2 | 35 % vom Total I der Spalte 8, zu übertragen in Ziff. 10 auf Seite 2. Das Auszahlungskonto steht auf Seite 1 von Formular 1. | `tg-wl-2026__c0166` |
> | ZH (2025/2026) | Form. 340 | Kolonne A, Verrechnungssteueranspruch Code 540. Mit der Unterschrift bestätigen Sie, dass auf allen Erträgen der Kolonne A Verrechnungssteuer abgezogen wurde. | `zh-wl-2026-uj__c0153`, Zuordnung ZH 2025 |
> 
> Der Ertrag selbst wird brutto in der Steuererklärung deklariert (Ziff. 4.1, ZH Code 150, AR/SG Code 146). Die Steuer auf diesen Bruttoerträgen wird dann mit der Verrechnungssteuer verrechnet.
> 
> ## Kantonale Besonderheiten
> 
> - **TG:** Rückerstattung nur, wenn Sie am 31.12. in TG wohnten und die Erträge deklariert haben (`tg-wl-2026__c0166`). Sonst gilt der Kanton des Wohnsitzes am 31.12.
> - **Kundenguthaben:** Bei einem Bruttozins bis Fr. 200 pro Jahr und Bank gehört der Ertrag in Kolonne B, weil keine Verrechnungssteuer abgezogen wird. Darüber gehört er in Kolonne A. Das gilt für AR, SG und ZH (`zh-wl-2025__c0162`). Für TG ist es im Wiki nicht in der Zuordnung erfasst (⚠ prüfen).
> - **Bankbelege:** Ein eSteuerauszug der Bank lässt sich in die Online-Steuererklärung importieren (ZH, `zh-wl-2026-uj__c0153`).
> - **Erben:** Bei Erträgen, die nach dem Tod fällig wurden, beantragen die Erben die Rückerstattung selbst. Der Antrag geht an das Steueramt des früheren Wohnorts (AR, `ar-wl-2025__c0132`).
> - **Kollektiv- und Kommanditgesellschaften:** Sie fordern über Formular 25 direkt bei der ESTV zurück (laut Zuordnung AR/SG 2025).
> 
> ## Lücken im Wiki
> 
> - **AR 2026:** Es gibt kein Formular und keine Wegleitung. Ich habe nichts aus 2025 übernommen.
> - **SG und ZH 2026:** Es liegt nur die Fassung für unterjährige Steuerpflicht vor. Die Ziffern müssen am regulären Formular geprüft werden.
> - **Dividenden aus dem Ausland:** Die ausländische Quellensteuer wird nicht über das Verrechnungssteuerverfahren zurückgefordert. Dafür gibt es das Formular DA-1.
> 
> Für welchen Kanton und welches Steuerjahr brauchen Sie es? Dann kann ich die genaue Ziffer und Fundstelle nennen.

## q23

**Frage:** Vergleiche den Versicherungsabzug 2025 für Alleinstehende ohne Kinder in AR, SG, TG, ZH und beim Bund.

**Soll (Referenz):** Alleinstehend ohne Kinder 2025 (mit 2. Säule/3a): AR 2'700 · SG 3'400 · TG 3'500 · ZH 2'900 · Bund 1'800.

**Antwort des Agenten** (38.8 s · Tools: 8 Aufrufe read, read):

> # Versicherungsabzug 2025, alleinstehend ohne Kinder
> 
> Die Beträge gelten für die Steuerperiode 2025 und sind in CHF. «Übrige Steuerpflichtige» sind Personen, die nicht in ungetrennter Ehe leben. Ein Kinderzuschlag entfällt, weil keine Kinder da sind.
> 
> | Jurisdiktion | Mit Beiträgen an 2. Säule oder 3a | Ohne Beiträge an 2. Säule oder 3a | Fundstelle (Status ☑️ agent-geprüft) |
> |---|---|---|---|
> | **Bund (DBG)** | 1'800 | 2'700 | Art. 33 DBG (`bund-dbg-2025__art-33-t2`); 2'700 laut RS 2-210 S. 2 (`bund-rs-2-210__c0006`) |
> | **AR** | 2'700 | 2'700 (keine Erhöhung) | Art. 35 StG AR (`ar-stg__art-35-t2`) |
> | **SG** | 3'400 | 3'900 (+500) | Art. 45 StG SG (`sg-stg-2025__art-45-t2`) |
> | **TG** | 3'500 | 3'500 (keine kantonale Erhöhung) | § 34 StG TG (`tg-stg__par-34-t3`) |
> | **ZH** | 2'900 | 4'350 (+50 %) | § 31 StG ZH (`zh-stg-2025__par-31-t2`); 4'350 laut WL ZH 2025 S. 15 (`zh-wl-2025__c0084`) |
> 
> Die Tabelle gilt für die Staats- und Gemeindesteuer der Kantone bzw. für die direkte Bundessteuer. Die kantonalen Werte stehen in `quick/vergleich-2025.md`, das Thema in `wiki/themen/versicherungspraemien.md`.
> 
> ## Auffälligkeiten
> 
> - **Rangfolge:** TG (3'500) und SG (3'400) haben die höchsten Grundbeträge. Es folgen ZH (2'900), AR (2'700) und der Bund (1'800).
> - **Erhöhung ohne Vorsorgebeiträge:** Sie gibt es nur beim Bund, in SG und in ZH. AR und TG kennen sie kantonal nicht. Der TG-Steuerpflichtige kann sie aber beim Bund geltend machen (Formular 5.2, Spalte Bund).
> - **SG:** Die 3'900 sind eine Summe aus 3'400 und 500. Sie steht so nicht als Einzelzahl im Gesetz. Laut WL SG 2025 S. 4 muss die Voraussetzung bei Verheirateten bei beiden Partnern erfüllt sein, bei Alleinstehenden ist das nicht relevant.
> - **TG:** Der erhöhte Bundesabzug (2'700) kann nicht zusammen mit dem ordentlichen Abzug beansprucht werden (WL TG 2025 S. 44).
> - **ZH:** Die 4'350 ergeben sich aus «um die Hälfte erhöht» (2'900 × 1,5).
> 
> ## Rechenregel
> 
> Der Abzug ist der niedrigere Betrag aus A und B:
> 
> - **A:** die bezahlten Prämien und Sparzinsen, abzüglich erhaltener Prämienverbilligung (IPV).
> - **B:** die Maximalbeträge aus der Tabelle.
> 
> Das Vorgehen je Kanton:
> 
> - **ZH:** Formular 365, Ziff. 15 (Code 270). Die Beträge für Staat und Bund stehen in zwei Spalten.
> - **TG:** Formular 5.2 in zwei Spalten (Staat/Bund), Übertrag in Ziff. 14.
> - **AR und SG:** Formular 6, Ziff. 14. Dort rechnet AR nur die Staats- und Gemeindesteuer, der Bundesabzug hat andere Beträge. SG nennt die Bundeslimiten in der Wegleitung.
> 
> ## Offen
> 
> Die Rangfolge und die Zahlen stammen aus dem Wiki. Eine fachliche Verifikation (✅) durch SB/ML liegt für diese Werte nicht vor. Für AR 2026 gibt es noch keine Wegleitung. Das betrifft diese Frage aber nicht, weil sie das Jahr 2025 betrifft.
> 
> Soll ich das Ganze mit einem Rechenbeispiel durchspielen, etwa mit Prämien von CHF 4'500?

## q24

**Frage:** Steuerfreie Vermögensbeträge (Sozialabzüge) 2025 in SG für ein Ehepaar mit einem minderjährigen Kind?

**Soll (Referenz):** SG 2025: 150'000 (Ehepaar) + 20'000 pro minderjähriges Kind = 170'000 (sg-stg-2025__art-64).

**Antwort des Agenten** (29.0 s · Tools: 5 Aufrufe read):

> **Steuerfreie Vermögensbeträge (Sozialabzüge) SG 2025, Ehepaar mit einem minderjährigen Kind: CHF 170'000.**
> 
> | Position | Betrag |
> |---|---|
> | Gemeinsam Steuerpflichtige (Ehepaar) | CHF 150'000 |
> | Zuschlag für ein minderjähriges Kind | CHF 20'000 |
> | **Total vom Reinvermögen abziehbar** | **CHF 170'000** |
> 
> **Fundstellen (Steuerjahr 2025, Kantons- und Gemeindesteuer)**
> - Das Wiki führt diese Werte als ☑️ agent-geprüft, also noch nicht von einer Fachperson verifiziert.
> - Die CHF 150'000 für gemeinsam Steuerpflichtige stehen in der Wegleitung SG 2025, Ziff. 36, S. 34 (`sg-wl-2025__c0118`).
> - Das Gesetz nennt für Ehepaare keinen eigenen Betrag. Art. 64 Abs. 1 lit. a StG SG nennt nur CHF 75'000 «für jeden Steuerpflichtigen» (`sg-stg-2025__art-64`).
> - Die CHF 20'000 je Kind stehen in Art. 64 Abs. 1 lit. b StG SG und in der Wegleitung Ziff. 36.
> 
> **Voraussetzungen und Abgrenzung**
> - Das Kind muss minderjährig sein und unter der elterlichen Sorge oder Obhut der Steuerpflichtigen stehen. Sie müssen dafür den Kinderabzug nach Art. 48 Abs. 1 lit. a StG beanspruchen können.
> - Massgebend sind die Verhältnisse am 31.12.2025 (Art. 64 Abs. 2 StG; WL Ziff. 36).
> - Die Beträge gelten nur für Kanton und Gemeinde. Für die direkte Bundessteuer wird kein Vermögen besteuert.
> - Die Abzüge werden vom Reinvermögen abgezogen, nur der Rest wird besteuert.
> 
> Die Kinderabzüge beim Einkommen (SG 2025: CHF 7'600 im Vorschulalter, CHF 10'800 im Schulalter) sind ein separater Abzug, nicht Teil dieser Vermögensfreibeträge.

## q25

**Frage:** Welcher Verzugszins gilt 2026 für die direkte Bundessteuer?

**Soll (Referenz):** 4.00 % (RS 2-215, bund-rs-2-215__c0010/c0011).

**Antwort des Agenten** (29.1 s · Tools: 5 Aufrufe read):

> **Der Verzugszins auf der direkten Bundessteuer beträgt für das Steuerjahr 2026 4,00 %.** Das ist eine Senkung gegenüber 2025, als er 4,50 % betrug. Die Änderung tritt am 1.1.2026 in Kraft. Der Status im Wiki ist ☑️ agent-geprüft, also noch nicht durch eine Fachperson verifiziert.
> 
> - **Quelle:** ESTV-Rundschreiben RS 2-215, Ziff. 3 «Zinssätze DBSt 2026», S. 3 (Chunk `bund-rs-2-215__c0010`). Rechtsgrundlage ist Art. 164 Abs. 1 DBG, geregelt in der Zinssatzverordnung EFD (SR 631.014), die das EFD am 9.9.2025 angepasst hat.
> - **Rückerstattungszins:** Er beträgt ebenfalls 4,00 % (2025: 4,50 %), Art. 162 Abs. 3 DBG.
> - **Vergütungszins für Vorauszahlungen:** Er liegt 2026 bei 0,00 % (2025: 0,75 %), Art. 163 Abs. 2 DBG. Vorauszahlungen bringen bei der DBSt 2026 also keinen Zins.
> - **Ausgleichszins:** Die DBSt kennt keinen.
> - **Kanton getrennt:** Der Zins auf der Staats- und Gemeindesteuer ist davon unabhängig. Für ZH und AR enthält das Wiki 2026 kantonale Sätze (ZH 4,5 %, AR 5 %). Für SG und TG fehlt der Verzugszins im Wiki.
> 
> Der Verzugszins läuft erst nach Ablauf der 30-tägigen Zahlungsfrist der Schlussrechnung (Art. 162/164 DBG; Termine über die kantonale Bezugsstelle).
> 
> Fundstellen im Wiki: `steuerwiki/quick/werte-bund-2026.md` (`bezug.verzugszins`) und `steuerwiki/wiki/themen/bezug-zinsen.md`.

## q26

**Frage:** Wann wird der Eigenmietwert abgeschafft und gilt das schon für 2026?

**Soll (Referenz):** Abschaffung per 1.1.2029 (Bundesratsbeschluss 01.04.2026); für 2025–2028 gilt bisheriges Recht – 2026 also noch Eigenmietwert.

**Antwort des Agenten** (40.8 s · Tools: 7 Aufrufe read, memory_search, exec):

> **Kurz: Der Eigenmietwert fällt per 1. Januar 2029 weg. Für 2026 gilt das noch nicht.** Für das Steuerjahr 2026 wird der Eigenmietwert wie bisher besteuert, bei Bund und Kantonen.
> 
> **Zeitplan**
> - Das Volk hat am 28. September 2025 den Bundesbeschluss über die kantonalen Liegenschaftssteuern auf Zweitliegenschaften angenommen. Damit wurde auch die Abschaffung der Eigenmietwertbesteuerung bestätigt.
> - Der Bundesrat hat am 1. April 2026 beschlossen, die Reform auf den 1. Januar 2029 in Kraft zu setzen. Er folgte damit der Mehrheit der Kantone. Sie wollten Zeit, um die Objektsteuer auf Zweitliegenschaften gleichzeitig einzuführen. (Quelle: [Medienmitteilung Bundesrat, 1.4.2026](steuerwiki/chunks/bund/dauernd/bund-mm-eigenmietwert-abschaffung/bund-mm-eigenmietwert-abschaffung__c0001.md), Wiki-Notiz zu c0002/c0003)
> - Der Kanton Zürich bestätigt das ausdrücklich. Ab Inkrafttreten gehören die Eigenmietwerte von Einfamilienhäusern und Stockwerkeigentum nicht mehr zum steuerbaren Einkommen. (Quelle: [^zh-info-neubewertung-2026__c0024](steuerwiki/chunks/zh/2026/zh-info-neubewertung-2026/zh-info-neubewertung-2026__c0024.md))
> 
> **Folgen für 2026 (Wiki-Stand)**
> - Der Eigenmietwert und der Unterhaltskostenabzug gelten bis und mit 2028 unverändert. Die neuen Regeln dürfen nicht vorzeitig angewendet werden (Wiki-Seite [rechtsaenderungen](steuerwiki/wiki/themen/rechtsaenderungen.md), Status: Entwurf).
> - ZH hat für 2026 eine Übergangsregelung ([^zh-info-neubewertung-2026__c0024](steuerwiki/chunks/zh/2026/zh-info-neubewertung-2026/zh-info-neubewertung-2026__c0024.md) und [c0025](steuerwiki/chunks/zh/2026/zh-info-neubewertung-2026/zh-info-neubewertung-2026__c0025.md)):
>   - Für Liegenschaften mit Erstellungsjahr vor dem 31.12.2025 gelten weiterhin die bisherigen Eigenmietwerte nach Weisung 2009.
>   - Für Liegenschaften ab Erstellungsjahr 2026 werden die Werte nach Weisung 2026 ermittelt, mit einem Pauschalabzug von 10 %.
> 
> **Was ab 1.1.2029 ändert**
> - Bei selbstgenutztem Wohneigentum entfallen die Eigenmietwertbesteuerung und der Abzug der Unterhaltskosten, bei Bund, Kantonen und Gemeinden. Bei vermieteten oder verpachteten Liegenschaften bleibt der Unterhaltskostenabzug.
> - Schuldzinsen sind nur noch im Verhältnis des Werts der vermieteten Liegenschaften zum gesamten Vermögen abzugsfähig. Für Ersterwerber gibt es einen zeitlich und betragsmässig begrenzten Schuldzinsenabzug.
> - Bei der direkten Bundessteuer entfallen die Abzüge für Energiespar- und Umweltschutzinvestitionen. Die Kantone dürfen sie beibehalten, aber nur befristet.
> - Die Kantone dürfen eine Objektsteuer auf überwiegend selbstgenutzten Zweitliegenschaften erheben.
> 
> **Offen**
> - Die Parameter des Ersterwerberabzugs (Dauer, Höchstbetrag) stehen in den erfassten Quellen nicht. Ich nenne dazu keine Zahlen.
> - Wie AR, SG und TG die Reform kantonal umsetzen, ist im Wiki nicht erfasst.
> - Die Quellen sind Medienmitteilungen und eine Kantonsinformation, also Ausblick und kein Gesetzestext. Die Wiki-Seite ist erst ein Entwurf. Die fachliche Beurteilung liegt bei SB/ML.
> 
> Falls Sie einen konkreten Fall für 2026 haben, sagen Sie mir den Kanton. Dann suche ich die passende Ziffer und den Wert heraus.

## q27

**Frage:** Zitiere die Regel zum Abzug privater Schuldzinsen im DBG (Steuerjahr 2025) mit Artikel.

**Soll (Referenz):** Art. 33 Abs. 1 lit. a DBG (Fassung 2025): private Schuldzinsen im Umfang der steuerbaren Vermögenserträge (Art. 20, 20a, 21) und weiterer CHF 50'000.

**Antwort des Agenten** (38.4 s · Tools: 8 Aufrufe read, read, exec):

> **Bund (DBG), Steuerjahr 2025 – Art. 33 Abs. 1 lit. a DBG**
> 
> > «Von den Einkünften werden abgezogen:
> > a. die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken. Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten oder ihr sonst wie nahe stehenden natürlichen Person zu Bedingungen gewährt, die erheblich von den im Geschäftsverkehr unter Dritten üblichen Bedingungen abweichen;»
> 
> Fundstelle: `^[bund-dbg-2025__art-33-t1]`. Das ist Art. 33 DBG, Teil 1 von 7, Bund, Steuerjahr 2025. Der Chunk liegt unter `steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md`.
> 
> **Praxis der ESTV (Kreisschreiben 22a, Ziff. 3.1, S. 4, gilt 2025/2026):**
> - Der maximale Abzug entspricht den steuerbaren Erträgen aus Privatvermögen plus einem Grundbetrag von CHF 50 000.
> - Der Grundbetrag gilt für Ehepaare in ungetrennter Ehe, eingetragene Partner und Kinder unter elterlicher Sorge gesamthaft.
> - Schuldzinsen sind auch ohne Vermögenserträge bis CHF 50 000 abziehbar.
> - Quelle: `^[bund-ks-22a__c0010]`.
> 
> **Abgrenzung:** Das gilt nur für die direkte Bundessteuer. Die Staats- und Gemeindesteuer richtet sich nach dem kantonalen Gesetz, und die Kantone folgen Art. 9 Abs. 2 lit. a StHG. Zu AR, SG, TG und ZH nenne ich auf Wunsch die Artikel. Laut `wiki/themen/schuldzinsen-schulden.md` ist die Grenze dort 2025 gleich.
> 
> **Status:** Die Seite `schuldzinsen-schulden.md` hat den Status «entwurf». Der Gesetzestext ist wörtlich aus dem Chunk übernommen. Eine Verifizierung durch die Fachperson (SB/ML) liegt nicht vor. Das Original-PDF habe ich nicht geprüft.

## q28

**Frage:** Ist ein Leasingvertrag für das Privatauto steuerlich relevant? Was ist mit den Leasingraten?

**Soll (Referenz):** Leasingraten sind keine Schuldzinsen und grundsätzlich nicht abziehbar (Lebenshaltung); relevant nur für Fahrkosten-Begründung/Geschäftsauto, Vermögen (kein Eigentum).

**Antwort des Agenten** (60.6 s · Tools: 13 Aufrufe read, exec, memory_search):

> Ich lese die Detailkarte und die zitierten Chunks, damit die Fundstellen stimmen.
> 
> **Kurz:** Bei einem privat genutzten Leasingauto ist der Vertrag steuerlich praktisch nicht relevant. Die Leasingraten sind nicht abziehbar, und das Fahrzeug muss nicht im Vermögen deklariert werden. Die Erfassung der Leasingschuld ist je Kanton nicht einheitlich geregelt (siehe unten).
> 
> Ich habe nicht nach Kanton und Steuerjahr gefragt. Die Antwort gilt für Bund, AR, SG, TG und ZH, Steuerjahre 2025/2026. Für andere Kantone ist das Wiki nicht abgedeckt, dort würde ich keine Werte übertragen.
> 
> **Leasingraten**
> - **Bund (DBG):** Leasingraten für privat genutzte Güter enthalten keine abzugsfähigen Zinsanteile. Die Raten gehören zu den nicht abziehbaren Lebenshaltungskosten (Art. 34 DBG). Fundstelle: KS 22a Ziff. 3.3, S. 5 (`bund-ks-22a__c0015`), 2025/2026, Status 🟡 extrahiert.
> - **ZH:** Leasingraten sind samt Zinsanteil nicht abzugsberechtigt (WL ZH 2025 Ziff. 12, S. 14, `zh-wl-2025__c0073`; Satzanfang im PDF-Layout verschoben, Original prüfen). Dasselbe gilt für 2026 (WL ZH 2026 UJ S. 13).
> - **SG:** Leasinggebühren privater Fahrzeuge sind nicht abziehbar (WL SG 2025 Ziff. 11, S. 25, `sg-wl-2025__c0083`).
> - **AR:** «Leasingraten persönlicher Gebrauchsgegenstände und privater Fahrzeuge» sind nicht abziehbar (WL AR 2025 Ziff. 11, S. 14, `ar-wl-2025__c0081`).
> - **TG:** Leasingzinsen sind grundsätzlich nicht abziehbar (WL TG 2025 S. 36, `tg-wl-2025__c0173`).
> - Die Raten gehören auch nicht in die Schuldzinsen. Dort sind nur echte Zinsen abziehbar, höchstens bis zum Vermögensertrag plus CHF 50'000. Die Rate also nicht in Schuldzinsen oder Schuldenverzeichnis übernehmen.
> 
> **Vermögen (Fahrzeug)**
> - Geleaste Fahrzeuge müssen nicht deklariert werden, weil die Leasinggesellschaft Eigentümerin ist.
> - TG 2025: WL TG 2025 Ziff. 30.4, S. 26 (`tg-wl-2025__c0123`). TG 2026 sagt dasselbe (`tg-wl-2026__c0122`).
> - ZH 2025: WL ZH 2025 Ziff. 30.4, S. 22 (`zh-wl-2025__c0140`). ZH 2026: WL ZH 2026 UJ S. 21 (`zh-wl-2026-uj__c0139`).
> - Für AR und SG ist die Aussage zum Leasingfahrzeug nicht direkt in einem zitierten Chunk belegt, nur über die Detailkarte. Die Karte nennt dort den Hinweis «Leasing nicht deklarieren (TG)», also nur für TG.
> 
> **Eigener Kanton-Widerspruch, den ich nicht auflösen kann**
> - Die Zuordnungstabellen von SG und TG (2025/2026) führen den Leasingvertrag als möglichen Beleg für die Schulden (SG Ziff. 34.1, TG Ziff. 34).
> - Die Detailkarte sagt dagegen, die Rate gehöre nicht ins Schuldenverzeichnis. Für ZH 2026 steht im Wiki sinngemäss: Schuld nicht deklarieren, wenn das Fahrzeug nicht deklariert wird. Dieser Satz steht in einer Wiki-Zusammenfassung (`schuldzinsen-schulden.md`). Den Originalwortlaut habe ich in den gelesenen Chunks nicht gefunden.
> - Ob die Leasingverpflichtung als Schuld erfasst wird, sollte die Fachperson klären.
> 
> **Wann der Vertrag doch eine Rolle spielt**
> - **Fahrkostenabzug:** Wer das Auto für den Arbeitsweg nutzt, kann im begründeten Fall den Fahrkostenabzug für das Privatauto geltend machen. Leasing ändert daran nichts. Bei ZH ist «Leasingfahrzeug» im Formular anzukreuzen (Wiki-Thema Fahrkosten).
> - **Selbständige:** Bei geschäftlicher Nutzung gehört der Leasingaufwand in die Jahresrechnung, nicht in die private Steuererklärung.
> - **Geschäftsfahrzeug vom Arbeitgeber:** Dann besteht kein Fahrkostenabzug. Für die Privatnutzung ist der Lohnausweis massgebend (Kästchen F bzw. Ziff. 2.2).
> 
> **Nicht belegt:** Die Aussage «Leasingkosten sind mit der Kilometerpauschale abgegolten» steht im Wiki ausdrücklich als Praxis ohne Chunk-Beleg («nachprüfen»). Ich würde sie nicht als gesichert weitergeben.
> 
> Fachliche Beurteilung bleibt bei SB/ML. Sag mir Kanton und Steuerjahr, dann prüfe ich die Ziffern und die Schuldenfrage für diesen Fall.

## q29

**Frage:** Wie hoch ist der Kinderabzug im Kanton Bern 2025?

**Soll (Referenz):** Nicht im Wiki (nur Bund, AR, SG, TG, ZH).

**Antwort des Agenten** (35.5 s · Tools: 2 Aufrufe exec, memory_search):

> Den Kinderabzug im Kanton Bern für 2025 kann ich nicht angeben, weil das Steuer-Wiki den Kanton Bern nicht abdeckt. Es enthält nur Bund, AR, SG, TG und ZH. Die Suche nach «Bern 2025 Kinderabzug» lieferte nur Treffer aus diesen Kantonen. Einen Wert für Bern zu schätzen oder aus einem anderen Kanton zu übernehmen, wäre falsch.
> 
> Für den Vergleich enthält das Wiki folgende Kinderabzüge für 2025:
> 
> | Jurisdiktion | Kinderabzug 2025 (CHF) | Fundstelle |
> |---|---|---|
> | Bund (DBG) | 6'800 pro Kind | `wiki/bund/werte-bund-2025-detail.md#L460-L487` |
> | TG (Kanton) | 7'400 Grundbetrag | `wiki/tg/werte-tg-2025-detail.md#L474-L496` |
> | SG (Kanton) | 7'600 im Vorschulalter, weitere Altersstufen nicht abgefragt | `wiki/sg/zuordnung-sg-2025-detail.md#L539-L551` |
> | AR (Kanton) | 5'300 im Vorschulalter, nach Alter gestaffelt | `wiki/ar/werte-ar-2025-detail.md#L464-L489` |
> 
> Der Bundesabzug von CHF 6'800 gilt unabhängig vom Wohnkanton auch für Bern, also für die direkte Bundessteuer. Für die bernische Staats- und Gemeindesteuer brauchen Sie die offizielle Quelle: die Wegleitung zur Steuererklärung 2025 der Steuerverwaltung Bern (Ziffer Sozialabzüge) oder das Steuergesetz des Kantons Bern (StG BE). Auf Wunsch rufe ich die Seite der Steuerverwaltung Bern ab. Das wäre dann aber eine Quelle ausserhalb des Wiki, ohne Wiki-Status oder Fundstelle.

## q30

**Frage:** Ehepaar TG 2025, beide angestellt (Nettolohn 80'000 und 30'000), pendelt mit ÖV-Abo (CHF 1'200 bzw. 900). Erstelle die Abzüge Berufskosten (Fahrkosten, Verpflegung ohne Kantine, Pauschale übrige) je Person für Kanton und Bund mit Fundstellen.

**Soll (Referenz):** TG 2025 je Person: Fahrkosten = ÖV-Abo effektiv (1'200 bzw. 900; Max. 6'000 Staat / 3'300 Bund); Verpflegung ohne Kantine 15/Tag, max. 3'200 (beide Ebenen); übrige Pauschale 3 %: P1 80'000 → 2'400, P2 30'000 → 900 → Minimum 2'000 (beide Ebenen, BKV TG § 4a / BKV Bund).

**Antwort des Agenten** (90.3 s · Tools: 25 Aufrufe read, read):

> Ich prüfe noch die letzten Fundstellen (Bund-Widerspruch 3'200/3'300, TG-Wegleitung zu Verpflegung/Arbeitstagen, Nettolohn-Basis), dann folgt die Berechnung.
> 
> # Berufskosten Ehepaar TG, Steuerjahr 2025
> 
> Kanton (Staats-/Gemeindesteuer) und Bund (DBG) ergeben für beide Personen dieselben Beträge. Keine Limite greift, und die Pauschalen sind in beiden Ebenen gleich.
> 
> ## Person 1 (Nettolohn CHF 80'000, ÖV-Abo CHF 1'200), Formular 4.2 → Ziff. 10.1 (Code 240)
> 
> | Form. 4.2 | Code | Position | Kanton | Bund | Regel / Rechnung | Fundstelle | Status |
> |---|---|---|---|---|---|---|---|
> | Ziff. 2.1 / 2.5 | 206 / 213 | Fahrkosten (ÖV-Abo) | 1'200 | 1'200 | Effektive Kosten, Maximum Kanton 6'000 / Bund 3'300; nicht erreicht | [StG TG § 29](../chunks/tg/2025/tg-stg/tg-stg__par-29.md) · [Form. 4.2 TG 2025 S. 1](../chunks/tg/2025/tg-form-04-2-2025/tg-form-04-2-2025__c0002.md) · [WL TG 2025 S. 4](../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0003.md) · [Art. 26 DBG](../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-26.md) | ☑️ |
> | Ziff. 3.1 | 214 | Verpflegung ohne Verbilligung | 3'200 | 3'200 | Fr. 15 pro Hauptmahlzeit, bei ständiger auswärtiger Verpflegung max. Fr. 3'200 | [§ 2 BKV TG](../chunks/tg/2025/tg-bkv/tg-bkv__par-2-t1.md) · [WL TG 2025 S. 39](../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0183.md) · [BKV Anhang 1](../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) · [Art. 6 BKV](../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-6-t1.md) | ☑️ (Zuordnung Form. 🟡) |
> | Ziff. 4 | 220 | Übrige Berufskosten | 2'400 | 2'400 | 3 % × 80'000 = 2'400, innerhalb Min. 2'000 / Max. 4'000 | [§ 4a BKV TG](../chunks/tg/2025/tg-bkv/tg-bkv__par-4a.md) · [WL TG 2025 S. 40](../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0187.md) · [BKV Anhang 1](../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) | ☑️ |
> | Ziff. 7 | 240 | **Total Berufsauslagen** | **6'800** | **6'800** | Summe Ziff. 2.5 bis 6 | [Zuordnung TG 2025](../quick/zuordnung-tg-2025.md) | ☑️ |
> 
> ## Person 2 (Nettolohn CHF 30'000, ÖV-Abo CHF 900), Formular 4.2, Rückseite → Ziff. 10.2 (Code 280)
> 
> | Form. 4.2 | Code | Position | Kanton | Bund | Regel / Rechnung | Fundstelle | Status |
> |---|---|---|---|---|---|---|---|
> | Ziff. 2.1 / 2.5 | 246 / 253 | Fahrkosten (ÖV-Abo) | 900 | 900 | Effektive Kosten; Maximum nicht erreicht | wie oben | ☑️ |
> | Ziff. 3.1 | 254 | Verpflegung ohne Verbilligung | 3'200 | 3'200 | wie Person 1 (Vollzeit unterstellt) | wie oben | ☑️ (Zuordnung Form. 🟡) |
> | Ziff. 4 | 260 | Übrige Berufskosten | 2'000 | 2'000 | 3 % × 30'000 = 900, **Minimum 2'000 greift** | [§ 4a BKV TG](../chunks/tg/2025/tg-bkv/tg-bkv__par-4a.md) · [BKV Anhang 1](../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) | ☑️ |
> | Ziff. 7 | 280 | **Total Berufsauslagen** | **6'100** | **6'100** | | | ☑️ |
> 
> ## Offene Punkte für die Fachperson
> 
> 1. **Verpflegung (3'200 je Person) beruht auf Annahmen.**
>    - Ich habe unterstellt, dass die Voraussetzung erfüllt ist: grosse Entfernung oder sehr kurze Essenspause, sodass die Hauptmahlzeit nicht zu Hause möglich ist ([§ 2 Abs. 1 BKV TG](../chunks/tg/2025/tg-bkv/tg-bkv__par-2-t1.md), [Art. 6 Abs. 1 BKV](../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-6-t1.md)). Bitte mit dem Mandanten klären.
>    - «Ohne Kantine» heisst im Lohnausweis Feld G nicht angekreuzt. Sonst gilt nur der halbe Abzug von Fr. 7.50 pro Tag, max. Fr. 1'600 ([§ 2 BKV TG, Teil 2](../chunks/tg/2025/tg-bkv/tg-bkv__par-2-t2.md)).
>    - Kein Abzug, wenn die Mahlzeit weniger als Fr. 10 kostet (gleiche Fundstelle).
>    - Die Arbeitstage sind nicht angegeben. Bei 225 Tagen × 15 = 3'375 würde das Maximum von 3'200 greifen, bei weniger Tagen entsprechend weniger (Tage × 15).
> 2. **Person 2 mit CHF 30'000 Nettolohn ist vermutlich teilzeitbeschäftigt.** Bei Teilzeit wird der Maximalbetrag nach Beschäftigungsgrad gekürzt, z.B. 80 % ergeben 2'560 ([WL TG 2025 S. 39](../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0183.md), [StP 29 Nr. 4](../chunks/tg/dauernd/tg-stp-29-4/tg-stp-29-4__c0005.md)). Beschäftigungsgrad und Verpflegungstage fehlen noch.
> 3. **Übrige Berufskosten: Basis ist der Nettolohn gemäss Lohnausweis Ziff. 11.** Die Nettolöhne habe ich so übernommen, wie Sie sie genannt haben. Bei weniger als 12 Monaten Erwerbstätigkeit wird die Pauschale anteilmässig gekürzt ([WL TG 2025 S. 40](../chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0187.md)).
> 4. **Bund-Fahrkostenmaximum:** Die ESTV-Wegleitung 2a 2025 S. 6 nennt noch «3200» ([Chunk](../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0042.md)). Gesetz und Rundschreiben nennen 3'300 ([Art. 26 DBG 2025](../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-26.md), [RS 2-210 Ziff. 1.1](../chunks/bund/2025/bund-rs-2-210/bund-rs-2-210__c0002.md)). Das Gesetz geht vor. Für diesen Fall ist es ohne Wirkung, da beide Abos unter 3'200 liegen.
> 5. **Belege:** ÖV-Abos und Lohnausweise beider Personen anfordern. Feld F (unentgeltliche Beförderung) muss leer sein, sonst entfällt der Fahrkostenabzug.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson (SB/ML).

## q31

**Frage:** Ehepaar ZH 2026, beide erwerbstätig, Kind 3 Jahre in der Kita (Kosten CHF 30'000). Wie viel Drittbetreuung ist abziehbar (Kanton und Bund)?

**Soll (Referenz):** ZH 2026 Kanton max. CHF 25'300 pro Kind (zh-stg-2026__par-31-t3); Bund 2026 max. CHF 25'800 (bund-dbg-2026__art-33-t7). Abzug je Ebene getrennt.

**Antwort des Agenten** (43.6 s · Tools: 10 Aufrufe read, exec, exec):

> Ich habe die Werte und Chunks geprüft und fasse zusammen.
> 
> **ZH, Steuerjahr 2026, Ehepaar, ein Kind (3 Jahre), Kita CHF 30'000**
> 
> | Ebene | Höchstbetrag pro Kind | Abziehbar bei CHF 30'000 | Fundstelle |
> |---|---|---|---|
> | **Staats-/Gemeindesteuer ZH** | CHF 25'300 | **CHF 25'300** | [§ 31 Abs. 1 lit. j StG ZH](steuerwiki/chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-31-t3.md), [WL ZH 2026 UJ S. 17, Ziff. 16.6](steuerwiki/chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0105.md) |
> | **Direkte Bundessteuer** | CHF 25'800 | **CHF 25'800** | [Art. 33 Abs. 3 DBG](steuerwiki/chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t7.md), WL ZH 2026 UJ S. 17 |
> 
> Die CHF 30'000 liegen über beiden Höchstbeträgen. Der Abzug ist deshalb gekappt, und die übersteigenden CHF 4'700 (Kanton) bzw. CHF 4'200 (Bund) fallen weg. Der Status im Wiki ist ☑️ agent-geprüft, nicht ✅ verifiziert.
> 
> **Voraussetzungen**
> - Das Kind ist unter 14 Jahren und lebt im gleichen Haushalt wie die Eltern.
> - Die Kosten stehen in direktem Zusammenhang mit der Erwerbstätigkeit der Eltern. Bei Ehepaaren sollten beide erwerbstätig sein. Das ist hier gegeben.
> - Formular: ZH-Ziffer 16.6, Code 376. Die beiden Maxima stehen im Formularkopf.
> 
> **Offene Punkte**
> 1. **Verpflegung:** Lebenshaltungskosten wie der Mittagstisch sind nicht abziehbar. Das Wiki nennt das für AR, SG und TG. Für ZH habe ich keine ausdrückliche Aussage in den gelesenen Quellen gefunden. Prüfen Sie, ob die Kita-Rechnung Verpflegung enthält. Liegt der Betrag ohne Verpflegung unter CHF 25'300, ist die Kappung nicht mehr massgebend.
> 2. **Subventionen:** Erhaltene Beiträge der Gemeinde oder der Kita wären von den Kosten abzuziehen. Dies ist für AR belegt, für ZH habe ich es nicht geprüft.
> 3. **Formular 2026:** Das reguläre Formular und die Wegleitung ZH 2026 sind noch nicht publiziert (Stand 09.11.2026). Die Werte stammen aus der Fassung für unterjährige Steuerpflicht (UJ) und aus dem Gesetz. Ziffer und Code sind am regulären Formular zu prüfen.
> 4. **Vorjahr:** Der Kantonswert 2025 war CHF 25'000 (Bund unverändert CHF 25'800). Die alte Verordnungsgrenze von CHF 10'400 ist überholt.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## q32

**Frage:** SG 2025: Einfamilienhaus (Baujahr 2010), selbst bewohnt. Pauschalabzug Liegenschaftsunterhalt Kanton und Bund?

**Soll (Referenz):** SG 2025: 20 % des Eigenmietwerts, ohne Altersstaffel (sg-stv__art-29); Bund: Gebäude zu Beginn 2025 über 10 Jahre alt → 20 % (bund-lkv__art-5).

**Antwort des Agenten** (36.2 s · Tools: 8 Aufrufe read):

> **Einfamilienhaus (Baujahr 2010, selbst bewohnt), Steuerjahr 2025: Pauschale 20 % im Kanton SG und 20 % bei der direkten Bundessteuer.** Die Pauschale gilt jeweils auf den Eigenmietwert.
> 
> | Ebene | Pauschale | Bemessungsgrundlage | Fundstelle | Status |
> |---|---|---|---|---|
> | **Kanton SG (Staats- und Gemeindesteuer)** | **20 %** | angerechneter Eigenmietwert | [Art. 29 Abs. 1 StV SG](steuerwiki/chunks/sg/2025/sg-stv/sg-stv__art-29.md) (zu Art. 44 Abs. 4 StG) · [WL SG 2025 S. 45](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0161.md) | ☑️ |
> | **Bund (DBG)** | **20 %** | Brutto-Eigenmietwert | [Art. 5 Abs. 2 lit. b LKV](steuerwiki/chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) (zu Art. 32 Abs. 4 DBG) | ☑️ |
> 
> **Begründung**
> - **SG:** Der Satz ist einheitlich 20 %, unabhängig vom Gebäudealter. Voraussetzung ist, dass die Liegenschaft ganz oder vorwiegend Wohnzwecken dient. Das trifft bei einem selbst bewohnten Einfamilienhaus zu.
> - **Bund:** Der Satz hängt vom Gebäudealter zu Beginn der Steuerperiode ab. Bei Baujahr 2010 ist das Haus am 1.1.2025 rund 15 Jahre alt, also mehr als 10 Jahre. Es gilt der Satz von 20 %. Bei einem Gebäude bis 10 Jahre wären es 10 %.
> - **Wahlrecht:** Die Wahl zwischen Pauschale und effektiven Kosten gilt pro Liegenschaft und Steuerperiode (Art. 29 Abs. 2 StV SG, Art. 5 Abs. 4 LKV). Bei der Pauschale sind keine weiteren Unterhaltsabzüge möglich.
> - **Energiespar- und Umweltinvestitionen:** In SG sind sie in der Pauschale inbegriffen (WL SG 2025 S. 45). Beim Bund gilt dasselbe (Art. 5 Abs. 1 lit. d LKV). Ein Abzug dieser Kosten ist nur bei effektiven Kosten möglich.
> - **Formular:** Es ist Ziff. 15 bzw. Formular 7 Abschnitt C (Code 716). Das steht in der Wiki-Zuordnung SG 2025 ([Liegenschaftsunterhalt](steuerwiki/wiki/themen/liegenschaftsunterhalt.md)). Ich habe die Zuordnung nicht in den Chunks nachgeprüft.
> 
> **Offene Punkte**
> - Bund und Kanton rechnen im Ergebnis gleich (20 %). Die Herleitung ist aber getrennt, weil der Bundessatz vom Alter abhängt. Wenn das Haus vor dem Steuerjahr 2020 gebaut oder fertiggestellt wurde, bleibt es beim Bund bei 20 %. Das ist hier der Fall.
> - Der Eigenmietwert für 2025 steht nicht in dieser Antwort. Er kommt aus der Einschätzung bzw. dem Formular. Die Pauschale ist 20 % von diesem Wert.
> - Das Wiki hat keine Verfügung SG 2025 zur Frage, ob Nebenkosten im Eigenmietwert enthalten sind. Bei der Mietertrags-Variante sind sie ausgenommen (Art. 29 Abs. 1 StV SG: «ohne Nebenkosten»).
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## q33

**Frage:** ZH 2025: Kind 19 Jahre, in Lehre (Ausbildung). Kinderabzug Kanton und Bund?

**Soll (Referenz):** ZH 2025 Kanton CHF 9'300 (volljährig in Erstausbildung, zh-stg-2025__par-34); Bund CHF 6'800 (bund-dbg-2025__art-35) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (49.8 s · Tools: 9 Aufrufe read, exec):

> Ich habe die ZH-2025-Werte und die Gesetzestexte gelesen. Jetzt prüfe ich noch kurz, ob der Bundesabzug vom Steuerbetrag (Art. 36 DBG) auch für ein volljähriges Kind in Ausbildung gilt.
> 
> **ZH 2025, Kind 19 Jahre in Lehre: ja, es gibt den vollen Kinderabzug, auf Kantons- und auf Bundesebene.** Das gilt, wenn Sie das Kind zur Hauptsache unterhalten. Das 19-jährige Kind ist am 31.12.2025 volljährig und in beruflicher Erstausbildung.
> 
> | Ebene | Abzug 2025 | Fundstelle | Status |
> |---|---|---|---|
> | Staats-/Gemeindesteuer ZH | **CHF 9'300** | § 34 Abs. 1 lit. a StG ZH ([`zh-stg-2025__par-34`](steuerwiki/chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-34.md)); WL ZH 2025 S. 20 ([`zh-wl-2025__c0126`](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0126.md)) | ☑️ agent-geprüft |
> | Direkte Bundessteuer | **CHF 6'800** | Art. 35 Abs. 1 lit. a DBG ([`bund-dbg-2025__art-35`](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md)) | ☑️ agent-geprüft |
> 
> **Formular (Steuererklärung 2025, Seite 3):**
> - Der Abzug kommt in Ziff. 24.1, «Abzug für Kinder in Ihrem Haushalt», Code 370. Die Spalten sind Staat 9'300 und Bund 6'800.
> - Lebt das Kind nicht in Ihrem Haushalt, gehört der Abzug in die Zeile «ausserhalb Ihres Haushaltes», Code 372 ([`zh-wl-2025__c0127`](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0127.md)).
> - Auf Seite 1 müssen Sie das Kind mit Geburtsdatum und Ausbildung (Lehrfirma, Dauer) angeben.
> 
> **Voraussetzungen:**
> - **Erstausbildung:** Das Kind ist am 31.12.2025 volljährig und steht in der beruflichen Erstausbildung. Eine Lehre erfüllt das. Bei ZH ist es ausdrücklich eine Voraussetzung (§ 34 Abs. 1 lit. a StG).
> - **Unterhalt zur Hauptsache:** Sie müssen überwiegend für das Kind aufkommen. Im Wiki steht dazu keine Franken-Grenze. Der Lehrlingslohn kann den Abzug also gefährden, wenn das Kind sich im Wesentlichen selbst finanziert. Das müssen Sie im Einzelfall beurteilen.
> - **Stichtag:** Massgebend sind die Verhältnisse am 31.12.2025 (§ 34 Abs. 2 StG, Art. 35 Abs. 2 DBG).
> - **Getrennt besteuerte Eltern:** Der Abzug wird hälftig geteilt (Staat 4'650 / Bund 3'400), wenn gemeinsame elterliche Sorge besteht und keine Alimente abgezogen werden. Bei einem volljährigen Kind in Erstausbildung gilt gemäss Wegleitung der ganze Abzug, wenn der andere Elternteil keine Unterhaltsbeiträge leistet oder Sie trotzdem zur Hauptsache für den Unterhalt aufkommen ([`zh-wl-2025__c0128`](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0128.md)).
> - **Alimente:** Zahlen Sie für das Kind Unterhaltsbeiträge (Ziff. 13.2), gibt es keinen Kinderabzug.
> 
> **Weitere kinderbezogene Positionen:**
> - **Versicherungsabzug, Zuschlag je Kind:** CHF 1'300 für den Staat und CHF 700 für den Bund (Form. 365, Teil B Ziff. 3). Dieser Zuschlag hängt am Anspruch auf den Kinderabzug.
> - **Bund, Abzug vom Steuerbetrag:** CHF 263 je Kind (Art. 36 Abs. 2bis DBG, [`bund-dbg-2025__art-36-t4`](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-36-t4.md)). Er gilt für Personen, die «mit Kindern … im gleichen Haushalt zusammenleben» und deren Unterhalt zur Hauptsache bestreiten. Er betrifft nur die Bundessteuer, nicht den Kanton. Der Gesetzestext nennt keine Altersgrenze. Ob das Kind dafür minderjährig oder in Ausbildung sein muss, habe ich in den Quellen nicht gesondert bestätigt.
> - **Ausbildungskosten und Fahrkosten des Kindes:** Die Lehrlingsfahrkosten, die das Kind selbst trägt, sind bei Ihnen kein Abzug. ZH kennt keinen zusätzlichen Ausbildungsabzug für Kinder (§ 34 StG, Eckwerte ZH 2025: «n/a»).
> 
> Das Kind versteuert seinen Lehrlingslohn selbst. Das ist hier nicht Teil Ihrer Steuererklärung.
> 
> Die fachliche Beurteilung, insbesondere zum «Unterhalt zur Hauptsache», bleibt bei SB/ML.

## q34

**Frage:** ZH 2025: Lohnausweis Feld G angekreuzt (Kantine). Welche Verpflegungspauschale gilt und in welche Ziffer des Berufsauslagenformulars?

**Soll (Referenz):** Verbilligte Verpflegung: CHF 7.50 pro Arbeitstag, max. CHF 1'600 pro Jahr (LS 631.33, zh-pauschalierung-berufsauslagen-2025__c0004); Form. 360 Ziff. 2.1 (verbilligt); Bund gleich.

**Antwort des Agenten** (48.7 s · Tools: 7 Aufrufe read, exec, exec):

> Ich habe die Fundstellen im Wiki gefunden und fasse sie jetzt zusammen.
> 
> **ZH 2025, Lohnausweis Feld G angekreuzt (Kantine / Lunch-Checks)**
> 
> **Pauschale:** Es gilt die reduzierte Verpflegungspauschale für verbilligte Verpflegung, nicht die volle.
> - Kanton: **CHF 7.50 pro Arbeitstag**, bei ständiger auswärtiger Verpflegung **max. CHF 1'600 pro Jahr**.
> - Bund (DBG): gleiche Beträge, CHF 7.50 pro Tag und max. CHF 1'600 pro Jahr. Die Spalten im Formular führt man getrennt.
> - Nicht anwendbar sind CHF 15 pro Tag und max. CHF 3'200 pro Jahr. Das ist die Pauschale, wenn die Verpflegung voll zulasten des Arbeitnehmers geht.
> 
> **Ziffer:** Formular 360 «Berufsauslagen», **Ziff. 2.1, erste Zeile** («Verpflegung durch den Arbeitgeber verbilligt»), **Code 206** für Person 1 (Person 2: 226).
> - Das Formular-360-Total (Code 220 bzw. 240) wird in die Steuererklärung nach **Ziff. 11.1** (Person 1) bzw. **11.2** (Person 2) übertragen.
> 
> **Voraussetzungen und Abgrenzungen:**
> - Die Heimkehr in der Mittagspause darf nicht möglich sein. Die Abzugsberechtigung gilt nur für die Arbeitstage am Arbeitsort.
> - Ziff. 2.1 verbilligt, Ziff. 2.1 voll und Ziff. 2.2 (Schicht-/Nachtarbeit) lassen sich nicht kumulieren.
> - Ist in Lohnausweis Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt» vermerkt, gibt es keinen Verpflegungsabzug.
> 
> **Fundstellen:**
> - [Formular 360 ZH 2025 S. 1](steuerwiki/chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md), `zh-form-360-2025__c0003`: Ziff. 2.1 mit Code 206.
> - [WL ZH 2025 S. 13](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0066.md), `zh-wl-2025__c0066`: Ziff. 11/2.1.
> - [LS 631.33 (bis 2025) S. 2–3](steuerwiki/chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0004.md), `zh-pauschalierung-berufsauslagen-2025__c0004`: Ziff. I/2.
> 
> **Status:**
> - Die Pauschalen und die Ziffer 2.1 (verbilligt) sind ☑️ agent-geprüft.
> - Die Aussage zu Feld G selbst, dass ein Kreuz nur den reduzierten Abzug erlaubt (auch wenn die Nutzung unbekannt ist), ist nur 🟡 extrahiert. Sie stützt sich auf `bund-wl-lohnausweis-2026__c0012`, also die ESTV-Wegleitung zum Lohnausweis in der Fassung **2026**. Eine 2025er Fassung ist im Wiki nicht vorhanden. Ob die Regel 2025 identisch war, muss die Fachperson prüfen.

## q35

**Frage:** SG 2025: Kapitalbezug Säule 3a CHF 100'000. Wird das mit dem übrigen Einkommen besteuert? Wo deklarieren?

**Soll (Referenz):** Nein – Kapitalleistungen aus Vorsorge werden getrennt vom übrigen Einkommen (separate Jahressteuer) besteuert; SG Formular 1 Ziff. 40.1 (Säule 3a), Total Ziff. 41.

**Antwort des Agenten** (57.2 s · Tools: 12 Aufrufe read, memory_search, exec, exec):

> Ich habe die SG-Quellen zu Kapitalleistungen aus Vorsorge gelesen und fasse jetzt zusammen.
> 
> ## Antwort (SG, Steuerjahr 2025)
> 
> **Nein, der Bezug wird nicht mit dem übrigen Einkommen versteuert.** Er wird gesondert und zu einem reduzierten Satz besteuert.
> 
> ### Kanton und Gemeinde
> - Der 3a-Kapitalbezug fällt unter Art. 52 StG SG («Kapitalabfindungen mit Vorsorgecharakter»). Er wird gesondert besteuert und unterliegt einer vollen Jahressteuer (Abs. 1).
> - Die einfache Steuer beträgt **2,0 %** für gemeinsam steuerpflichtige Ehegatten und **2,2 %** für die übrigen Steuerpflichtigen (Abs. 2).
> - Den Ehegattensatz erhalten auch Verwitwete, Getrennte, Geschiedene und Ledige, die mit Kindern oder unterstützungsbedürftigen Personen zusammenleben und deren Unterhalt zur Hauptsache bestreiten (Abs. 3).
> - Allgemeine Abzüge und Sozialabzüge werden nicht gewährt (Abs. 4).
> - Die Steuer entsteht, wenn die Leistung zufliesst (Abs. 5). Massgebend ist also das Auszahlungsjahr.
> - Fundstelle: `sg-stg-2025__art-52` (☑️ agent-geprüft).
> 
> **Rechenbeispiel für CHF 100'000:**
> 
> | Zivilstand | Einfache Steuer |
> |---|---|
> | Übrige Steuerpflichtige (2,2 %) | CHF 2'200 |
> | Gemeinsam Steuerpflichtige (2,0 %) | CHF 2'000 |
> 
> - Die einfache Steuer wird mit dem Steuerfuss multipliziert. Der Kantonssteuerfuss 2025 beträgt 105 % (`sg-steuerfuesse-2025__c0001`). Das ergibt CHF 2'310 bzw. CHF 2'100 Kantonssteuer.
> - Der Gemeindesteuerfuss ist im Wiki nicht erfasst, und die Kirchensteuer lasse ich hier unberücksichtigt. Dafür brauche ich die Gemeinde.
> 
> ### Direkte Bundessteuer
> - Der Bezug wird gesondert besteuert, mit voller Jahressteuer, zu **einem Fünftel der Tarife** nach Art. 36 DBG. Sozialabzüge werden nicht gewährt (Art. 38 DBG, `bund-dbg-2025__art-38`).
> - Einen CHF-Betrag nenne ich nicht. Das Wiki führt für den Bund keinen Prozentsatz, und die Tarifstufen müssten aus der Tabelle in WL 2a 2025 S. 10 gerechnet werden.
> 
> ### Wo deklarieren
> - Die Deklaration erfolgt in **Formular 1 SG 2025, Ziff. 40.1 «Säule 3a»**. Ziff. 40.2 ist für die 2. Säule und 40.3 für übrige Leistungen. Das Total steht in Ziff. 41 (Code 950).
> - Es ist **nicht** Ziff. 3.2 (Renten) und **nicht** Ziff. 6.4 (Kapitalabfindung für wiederkehrende Leistungen).
> - Bei mehreren Kapitalleistungen im Jahr trägt man den zusammengerechneten Gesamtbetrag ein.
> - Die Wegleitung bezeichnet die Eintragung in Ziff. 40 als «Ergänzende Angaben zu Informationszwecken». Sie hat keine weiteren Steuerfolgen und fliesst nicht in das steuerbare Einkommen ein. Die separate Besteuerung erfolgt trotzdem, sie ist nicht von der Deklaration abhängig (WL SG 2025 S. 35, `sg-wl-2025__c0119`).
> - Als Beleg dient die Auszahlungsbescheinigung der 3a-Stiftung (Bank oder Versicherung). Auszahlungsdatum und Bruttobetrag sollten darauf stehen.
> 
> ### Offen / zu beachten
> - **Gemeindesteuerfuss:** nicht im Wiki, siehe oben.
> - **Bundesbetrag:** nicht berechnet, siehe oben.
> - **Auszahlungsjahr:** Die Regeln oben gelten für einen Zufluss 2025. Fliesst der Betrag erst 2026 zu, gehört er in die Steuererklärung 2026. Die SG-Sätze 2026 sind laut Wiki gleich (Art. 52 StG SG 2026), aber das ist ein separates Steuerjahr.
> - **Weitere Bezüge:** Mehrere Kapitalleistungen im selben Jahr (z. B. Pensionskasse und 3a) unterliegen jeweils der gesonderten Jahressteuer. Das Wiki prüft nicht, ob sie zusammengerechnet werden, bevor der Satz angewendet wird. Bei einem solchen Fall ist das vor der Berechnung zu klären.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## q36

**Frage:** ZH 2025: Geschiedener Mandant zahlt Unterhaltsbeiträge an die Ex-Frau (CHF 24'000) und für das minderjährige Kind (CHF 12'000). Was ist abziehbar, in welcher Ziffer?

**Soll (Referenz):** Ex-Ehefrau CHF 24'000 voll abziehbar, Ziff. 13.1 (Code 254); Kinderalimente CHF 12'000 abziehbar bis und mit Monat der Volljährigkeit, Ziff. 13.2 (Code 255); Empfänger versteuert; Bund gleich (Art. 33 Abs. 1 lit. c DBG).

**Antwort des Agenten** (43.0 s · Tools: 9 Aufrufe read, exec):

> **ZH 2025, geschiedener Mandant: beide Beträge sind voll abziehbar, CHF 36'000 insgesamt. Sie gehören in zwei getrennte Ziffern.**
> 
> | Ziffer | Position (Code) | Betrag |
> |---|---|---|
> | **13.1** | Unterhaltsbeiträge an den geschiedenen oder getrennt lebenden Ehegatten / Partner (Code 254) | CHF 24'000 |
> | **13.2** | Unterhaltsbeiträge für minderjährige Kinder, bis zum Monat der Volljährigkeit (Code 255) | CHF 12'000 |
> 
> - **Ex-Frau (13.1):** Beiträge, die für den Ehegatten persönlich bestimmt sind, sind voll abziehbar. ^[zh-wl-2025__c0075] (WL ZH 2025 S. 14)
> - **Kind (13.2):** Kinderalimente sind bis und mit dem Monat abziehbar, in dem das Kind 18 wird. ^[zh-wl-2025__c0076] (WL ZH 2025 S. 15)
> - **Bund:** Das Formular hat je eine Spalte für Staats- und Bundessteuer. Der Abzug gilt auch für die direkte Bundessteuer nach Art. 33 Abs. 1 lit. c DBG. ^[bund-ks-30__c0100] (KS 30 S. 32) Der Betrag ist in beiden Spalten derselbe, es gibt keine Limite.
> - **Status:** Ziff. 13.1 und 13.2 sind ☑️ agent-geprüft. Quick-Seite: `quick/zuordnung-zh-2025.md`.
> 
> **Zu prüfen**
> 1. **Kein Kinderabzug für dieses Kind.** Wer Kinderalimente nach Ziff. 13.2 abzieht, erhält für dasselbe Kind keinen Kinderabzug (Ziff. 24.1, Code 372). Das ist in der Zuordnung festgehalten (`zuordnung-zh-2025-detail.md`, Abschnitt 24.1, gestützt auf WL ZH 2025 S. 20, `zh-wl-2025__c0129`). Der Kinderabzug kommt erst nach Erreichen des 18. Altersjahrs, statt des Alimentenabzugs. ^[zh-wl-2025__c0076]
> 2. **Volljährigkeit im Jahr 2025.** Wird das Kind 2025 18, ist nur der Betrag bis und mit Geburtsmonat in 13.2 abziehbar. Die Zahlungen ab dem Folgemonat gehören nicht in 13.2. Dann ist der Kinderabzug für den Zahlenden zu prüfen.
> 3. **Nur effektiv bezahlt und familienrechtlich geschuldet.** Freiwillige Beiträge sind nicht abziehbar. ^[bund-ks-30__c0100] Mit der Steuererklärung sind sämtliche Zahlungsnachweise einzureichen. ^[zh-wl-2025__c0076] Bei erstmaliger Deklaration kommt das Urteil bzw. die Konvention dazu. Name und Adresse der empfangenden Person sind anzugeben.
> 4. **Beträge aufteilen.** Wenn die Konvention einen Gesamtbetrag nennt, braucht es die Aufteilung auf Ex-Frau und Kind. Nur der Teil für die Ex-Frau persönlich gehört in 13.1.
> 5. **Gegenseite.** Die Ex-Frau muss dieselben Beträge versteuern (Ziff. 5.1 und 5.2).
> 
> Offen bleibt die Frage, wer das Kind betreut und ob das Sorgerecht gemeinsam ist. Davon hängt der Kinderabzug ab (ZStB 34.1 Rz 16–19, `zh-zstb-34-1-bis-2025__c0008`, nur Teil 1 gelesen). Die fachliche Beurteilung bleibt bei SB/ML.

## q37

**Frage:** TG 2025: Mandant bringt Steuerberatungsrechnung, Kreditkartenabrechnung, Mietvertrag und Motorfahrzeugversicherung. Was davon ist relevant?

**Soll (Referenz):** Steuerberatungsrechnung: nein; Motorfahrzeugversicherung: nein; Kreditkartenabrechnung: bedingt (nur als Nachweis/Schuld per 31.12.); Mietvertrag: bedingt (Wochenaufenthalt/Arbeitszimmer/Adressnachweis) – laut belege-relevanz.

**Antwort des Agenten** (62.3 s · Tools: 12 Aufrufe read, memory_search, exec):

> Ich habe die Belegkarten und die TG-Quellen für 2025 geprüft. Hier das Ergebnis.
> 
> **TG, Steuerjahr 2025 (Staat und Bund getrennt, wo es zählt). Status aller Karten: ☑️ agent-geprüft.**
> 
> | Dokument | Relevanz | Kurzbegründung |
> |---|---|---|
> | Steuerberatungsrechnung | **nein** | Privat nicht abziehbar. |
> | Kreditkartenabrechnung | **bedingt** | Kein Beleg an sich, nur bei Sollzinsen/Saldovortrag oder als Nachweisquelle. |
> | Mietvertrag | **bedingt** (meist nein) | Der Mietzins der selbstbewohnten Wohnung ist nicht abziehbar. Nur drei Sonderfälle, siehe unten. |
> | Motorfahrzeugversicherung | **nein** (Police) | Die Prämie ist nicht abziehbar. Das Fahrzeug selbst ist aber Vermögen. |
> 
> **1. Steuerberatungsrechnung: nicht relevant**
> - Bund: Steuerberatung und Ausfertigung der Steuererklärung sind keine zulässigen Vermögensverwaltungskosten (`bund-wl-2a-2025__c0057`, S. 8). Sie sind Lebenshaltungskosten nach Art. 34 lit. a DBG (`bund-dbg-2025__art-34`).
> - TG: Die Wegleitung TG 2025 (S. 33–34, `tg-wl-2025__c0160`) lässt nur notwendige Verwaltung des Privatvermögens zu, z.B. Depotgebühren. Anlageberater und Kontoführung sind ausgeschlossen. Steuerberatung wird dort nicht ausdrücklich genannt. Ein TG-Treffer dazu fehlt im Wiki, die ausdrückliche Nennung stammt aus Bund, SG und AR.
> - Ausnahme: Ist der Mandant selbständig, kann der geschäftliche Teil Geschäftsaufwand sein. Die Aufteilung ist im Wiki nicht verifiziert, das entscheidet die Fachperson.
> 
> **2. Kreditkartenabrechnung: bedingt**
> - Übernehmen nur, wenn Sollzinsen oder ein Saldovortrag bestehen.
>   - Das gehört in Formular 4.1 A (Schuldenverzeichnis).
>   - Dazu braucht es Gläubiger mit Adresse, Zinssatz, Schuld per 31.12.2025 und die fälligen Zinsen.
>   - Die Summen gehen nach Ziff. 34 (Schulden, Code 466) und Ziff. 11 (Schuldzinsen, Code 290).
> - Ausserdem kann sie als Nachweisquelle für abziehbare Zahlungen dienen, wenn die Originalrechnung fehlt (Spenden, Arzt, Weiterbildung).
> - Jahresgebühr und Alltagsumsätze sind nicht abziehbar.
> 
> **3. Mietvertrag: nur in drei Fällen relevant**
> - **Untervermietung:** Der Nettoertrag ist steuerbar, nach Abzug des anteiligen Mietzinses und der Nebenkosten (WL TG 2025 S. 19, `tg-wl-2025__c0083`).
> - **Wochenaufenthalt am Arbeitsort:** Der Abzug läuft über Formular 4.2 Ziff. 5.1 (Code 226).
>   - Es gilt nur ein Zimmer als notwendig.
>   - Bei Wohnungen bis 3½ Zimmer rechnet man Jahresmietzins : (Zimmer + 1) (WL TG 2025 S. 40, `tg-wl-2025__c0189`).
> - **Mietzinsreduktion als Entgelt** (z.B. Hauswart): Die Differenz ist Einkommen.
> - Ein Mietkautionskonto (Sperrkonto) gehört nur als Guthaben ins Vermögen, falls es verzinst ist.
> 
> **4. Motorfahrzeugversicherung: Police nicht relevant, Fahrzeug schon**
> - Prämien und Verkehrssteuer sind Lebenshaltungskosten. Im Wiki sind sie für AR und SG ausdrücklich ausgeschlossen. Für TG stütze ich mich auf Art. 34 DBG, eine TG-spezifische Stelle habe ich nicht gefunden.
> - Das Fahrzeug ist aber Vermögen (Ziff. 30.4, Code 422, WL TG 2025 S. 26, `tg-wl-2025__c0123`).
>   - Anzusetzen ist der Verkehrswert per 31.12.2025: Kaufpreis abzüglich 20 % pro Jahr seit Erwerb.
>   - Ein Fahrzeug, das vor mehr als 5 Jahren gekauft wurde, steht pro memoria mit Fr. 1.– drin.
>   - Geleaste Fahrzeuge werden nicht deklariert.
>   - Dafür brauche ich den **Fahrzeugausweis** (Typ, Kaufpreis, Anschaffungsjahr), nicht die Police.
> - Fahrkosten mit dem Privatauto sind nur in begründeten Ausnahmefällen abziehbar, und zwar mit Kilometerpauschale (Formular 4.2 Ziff. 2.3). Die Police belegt das nicht.
> 
> **Rückfragen an den Mandanten**
> 1. Ist er Mieter oder Eigentümer? Gibt es Untervermietung oder einen Wochenaufenthalt?
> 2. Hat die Kreditkarte einen Saldovortrag oder Sollzinsen? Wurden darüber Spenden, Arzt- oder Weiterbildungskosten bezahlt, deren Rechnung fehlt?
> 3. Wird das Auto privat gehalten oder geleast? Kaufpreis und Jahr, plus Fahrzeugausweis.
> 4. Ist er selbständig? Das betrifft einen möglichen geschäftlichen Teil der Steuerberatung.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## q38

**Frage:** AR 2026: Wie hoch ist der Kinderabzug für ein 10-jähriges Kind? Ist der Wert gesichert?

**Soll (Referenz):** AR 2026: CHF 7'400 laut Anhang 1 StG (indexiert), aber Status STRITTIG (MB 02 / StG-Text nennen andere Beträge; Wegleitung 2026 fehlt) → Fachperson.

**Antwort des Agenten** (37.0 s · Tools: 5 Aufrufe read, exec):

> **Kurz: Nein, der Wert ist nicht gesichert.** Für AR 2026 gibt es zwei Zahlen. Das Wiki führt den Eintrag als ⚠️ strittig, und die Fachperson muss entscheiden.
> 
> **Einordnung:** 10-jähriges Kind, also Schulalter (nach Vollendung des 4. bis zur Vollendung des 15. Altersjahrs). Stichtag ist der 31.12. Das gilt für die Staats- und Gemeindesteuer AR.
> 
> | Quelle | Betrag |
> |---|---|
> | Anhang 1 StG AR, Art. 38 Abs. 1 lit. a Ziff. 2, indexiert per 1.1.2024 (`ar-stg-anhang-kp__c0001`) | **CHF 7'400** |
> | MB AR 02 Ziff. 2, Stand 18.08.2026 (`ar-mb-02__c0002`) | **CHF 7'000** |
> 
> - **Gesetzestext:** Der Text von Art. 38 StG und das MB 02 nennen 7'000. Das ist der nicht indexierte Gesetzesbetrag.
> - **Anhang 1:** Er gehört zum Gesetz und gilt nach Art. 39a StG als massgeblich. Er nennt 7'400.
> - **2025 als Vergleich:** Die Wegleitung AR 2025 bestätigt für 2025 die 7'400 (Kurzübersicht Ziff. 23.2, `ar-wl-2025__c0005`). Dieser Wert gilt nicht automatisch für 2026.
> - **Wegleitung 2026:** Sie ist noch nicht publiziert (Stand 09.11.2026). Es gibt also keine amtliche Praxis des Jahres, die den Widerspruch auflöst.
> 
> **Wahrscheinliche Lesart:** Es gilt Anhang 1 mit CHF 7'400, weil das Wiki dem Anhang als Teil des Gesetzes den Vorrang gibt. Das ist aber keine bestätigte Aussage. Ich würde 7'400 als Arbeitswert nehmen und den Widerspruch im Dossier vermerken. Danach den Betrag an der Steuererklärung oder Wegleitung AR 2026 prüfen, sobald sie erscheint.
> 
> **Nicht verwechseln:**
> - Bund (DBG): Der Kinderabzug ist dort anders aufgebaut, nämlich als Abzug vom Steuerbetrag.
> - Zusätzliche AR-Positionen, die nicht der Kinderabzug sind:
>   - Versicherungsabzug CHF 1'000 pro Kind (☑️)
>   - Vermögensfreibetrag CHF 25'000 pro Kind (☑️)
> 
> Quellen: `steuerwiki/quick/werte-ar-2026.md` (Sozialabzüge), `data/werte/ar/2026.yaml` (`sozialabzug.kind_schule`, Status `strittig`).

## q39

**Frage:** Welche Vermögenssteuer-Freibeträge (Sozialabzüge) gelten 2025 in ZH für Alleinstehende und Verheiratete?

**Soll (Referenz):** ZH kennt keine Vermögens-Sozialabzüge, sondern Tarifstufen mit 0 ‰: Grundtarif erste CHF 80'000, Verheiratetentarif erste CHF 159'000 (zh-stg-2025__par-47); kein Betrag pro Kind.

**Antwort des Agenten** (34.7 s · Tools: 5 Aufrufe read):

> **ZH, Steuerjahr 2025 (Staats- und Gemeindesteuer):** Die Vermögenssteuer kennt in ZH keinen Abzug. Der Freibetrag ist die 0‰-Stufe im Tarif von § 47 StG ZH.
> 
> | Tarif | Steuerfrei (0‰-Stufe) | Quelle |
> |---|---|---|
> | Grundtarif (Alleinstehende) | **CHF 80'000** | § 47 Abs. 1 StG ZH ^[zh-stg-2025__par-47-t1] |
> | Verheiratetentarif (gemeinsam besteuerte Ehepaare) | **CHF 159'000** | § 47 Abs. 2 StG ZH ^[zh-stg-2025__par-47-t2] |
> 
> Status im Wiki: ☑️ agent-geprüft, nicht von der Fachperson verifiziert. Ich habe beide Beträge im Gesetzeswortlaut der Chunks nachgelesen.
> 
> - **Verheiratetentarif auch ohne Ehe:** Er gilt auch für Verwitwete, gerichtlich oder tatsächlich Getrennte, Geschiedene und Ledige, die mit Kindern im Sinn von § 34 Abs. 1 lit. a zusammenleben. Dasselbe gilt für nicht gemeinsam besteuerte Eltern mit gemeinsamer elterlicher Sorge, wenn der Kinderabzug je zur Hälfte zusteht. Dann hat der Elternteil Anspruch, der den Unterhalt des Kindes zur Hauptsache bestreitet (§ 47 Abs. 2 und 2bis).
> - **Stichtag:** Der Tarif richtet sich nach den Verhältnissen am Ende der Steuerperiode bzw. der Steuerpflicht (§ 47 Abs. 3).
> - **Kein Kinderabzug beim Vermögen:** ZH kennt keinen Vermögens-Sozialabzug pro Kind. Das steht als «n/a» in den Eckwerten (`vermoegen.freibetrag_kind`).
> - **Darüber:** Auf die weiteren Vermögensteile gilt eine progressive Staffel von ½‰ bis 3‰, die im Grundtarif ab CHF 3'262'000 und im Verheiratetentarif ab CHF 3'342'000 greift. Die Gemeindesteuer kommt über den Steuerfuss hinzu.
> - **Bund:** Die direkte Bundessteuer erhebt keine Vermögenssteuer, daher gibt es dort keine entsprechenden Freibeträge.
> 
> Fundstelle der Eckwerte: `steuerwiki/quick/werte-zh-2025.md`, Abschnitt «Vermögen».

## q40

**Frage:** Alleinstehende TG 2026, Nettolohn 90'000, ÖV-Abo 2'400, Säule 3a 7'258, Krankenkasse 5'500. Erstelle die Abzüge (Berufskosten, 3a, Versicherungsabzug) Kanton und Bund mit Fundstellen und Status.

**Soll (Referenz):** TG 2026 (Kanton/Bund): Fahrkosten 2'400 (Max. 6'000 / 3'300); übrige Berufskosten 3 % von 90'000 = 2'700 (Min. 2'000, Max. 4'000, beide Ebenen); Säule 3a 7'258 (TG 🟡 extrahiert, Bund ☑️); Versicherungsabzug TG max. 3'500 → 3'500, Bund max. 1'800 → 1'800 (Prämien 5'500 übersteigen beide Maxima).

**Antwort des Agenten** (84.5 s · Tools: 22 Aufrufe read, read, exec, message):

> **Fall:** TG, alleinstehend, Steuerjahr 2026. Wohnsitz am 31.12.2026 in TG und keine Kinder habe ich vorausgesetzt. Quellen sind das Steuer-Wiki (Quick-Layer, Detailseiten und die Chunks selbst).
> 
> ## Ergebnis
> 
> | Abzug | Ziffer TG-Formular | Kanton (Staat/Gemeinde) | Bund (DBG) | Status |
> |---|---|---|---|---|
> | Fahrkosten ÖV-Abo | Form. 4.2 Ziff. 2.1 / 2.5 | **CHF 2'400** | **CHF 2'400** | ☑️ |
> | Übrige Berufskosten (3 % von 90'000) | Form. 4.2 Ziff. 4 | **CHF 2'700** | **CHF 2'700** | ☑️ |
> | **Berufsauslagen total** | Form. 4.2 Ziff. 7 → Form. 1 Ziff. 10.1 | **CHF 5'100** | **CHF 5'100** | ☑️ |
> | Säule 3a | Form. 1 Ziff. 13.1 | **CHF 7'258** | **CHF 7'258** | ☑️ (Kanton: Eckwert 🟡, siehe unten) |
> | Versicherungsabzug | Form. 5.2 → Form. 1 Ziff. 14 | **CHF 3'500** | **CHF 1'800** | ☑️ |
> | **Total dieser drei Abzüge** | | **CHF 15'858** | **CHF 14'158** | |
> 
> ## Herleitung und Fundstellen
> 
> **Fahrkosten**
> - Der Kanton begrenzt auf CHF 6'000, der Bund auf CHF 3'300. Die CHF 2'400 liegen unter beiden Grenzen und werden voll abgezogen.
> - Kanton: Formular 4.2 TG 2026, Ziff. 2.5 (`tg-form-04-2-2026__c0002`: «aber Staat max. Fr. 6000.– / Bund max. Fr. 3300.–»). Kanton: WL TG 2026 S. 38 (`tg-wl-2026__c0177`).
> - Bund: Art. 26 Abs. 1 lit. a DBG (`bund-dbg-2026__art-26`): «bis zu einem Maximalbetrag von 3300 Franken».
> - Voraussetzung: Im Lohnausweis darf Feld F (Gratis-Arbeitsweg, Geschäftsfahrzeug) nicht angekreuzt sein.
> 
> **Übrige Berufskosten**
> - 3 % von 90'000 = 2'700. Das liegt zwischen dem Minimum von CHF 2'000 und dem Maximum von CHF 4'000, es gilt also die Pauschale.
> - Kanton: WL TG 2026 S. 40 (`tg-wl-2026__c0187`: «3% vom Nettolohn gemäss Ziffer 11 des Lohnausweises … mindestens Fr. 2'000 und höchstens Fr. 4'000 (kantonal und direkte Bundessteuer)»). Kanton: Formular 4.2 (`tg-form-04-2-2026__c0004`). Kanton: § 4a BKV TG (`tg-bkv__par-4a`, gültig für 2025 und 2026).
> - Bund: Eckwerte Bund 2026 (BKV-Anhang `bund-bkv-2026__anhang-1`, RS 2-215 S. 2 `bund-rs-2-215__c0006`).
> 
> **Säule 3a**
> - Die Obergrenze mit Anschluss an die 2. Säule beträgt CHF 7'258. Der Betrag ist erreicht, nicht überschritten.
> - Kanton: WL TG 2026 S. 20 (`tg-wl-2026__c0089`). Kanton: Formular 1 Ziff. 13.1 (`tg-form-01-2026__c0010`).
> - Bund: Eckwerte Bund 2026 mit BSV-Masszahlen 25/26 (`bund-bsv-masszahlen-2025-2026__c0003`).
> - Dasselbe Feld (Ziff. 13.1) gilt für Staat und Bund. Das Kästchen «Anschluss 2. Säule (PK)» ist anzukreuzen, wenn eine Pensionskasse besteht. Gäbe es keine, lägen die Grenzen bei 20 % des Erwerbseinkommens, höchstens CHF 36'288. Der Abzug von 7'258 bliebe gleich.
> 
> **Versicherungsabzug**
> - Die Prämie von 5'500 übersteigt beide Maxima. Der Abzug ist daher der Maximalbetrag.
> - Kanton: min(5'500; 3'500) = 3'500. Fundstellen: Formular 5.2 Teil B (`tg-form-05-2-2026__c0002`: alleinstehend «3500 / 1800»), WL TG 2026 S. 44 (`tg-wl-2026__c0209`) und § 34 Ziff. 9 lit. b StG TG (`tg-stg__par-34-t3`, gültig für 2025 und 2026).
> - Bund: min(5'500; 1'800) = 1'800. Fundstelle: Art. 33 Abs. 1 lit. g Ziff. 2 DBG (`bund-dbg-2026__art-33-t2`: «1800 Franken für die übrigen Steuerpflichtigen»).
> - Der erhöhte Bundesabzug von CHF 2'700 gilt nur ohne Beiträge an die 2. Säule und Säule 3a. Wegen der 3a-Einzahlung greift er hier nicht (WL c0209).
> 
> ## Offene Punkte und Vorbehalte
> 
> 1. **Prämie 5'500:** Das Formular verlangt die Nettoprämie nach Abzug der erhaltenen Prämienverbilligung (IPV). Der Abzug sinkt nur dann unter das Kantonsmaximum, wenn die Nettoprämie unter CHF 3'500 fällt, also bei einer IPV über rund CHF 2'000. Bitte prüfen, ob 5'500 brutto oder netto ist.
> 2. **Status 3a Kanton:** Die Position (Zuordnung) ist ☑️. Der Eckwert `saeule3a.max_mit_2saeule` in `quick/werte-tg-2026.md` ist erst 🟡 (extrahiert).
> 3. **Nettolohn:** Ich habe 90'000 als Lohnausweis Ziff. 11 angenommen. Die 3 %-Pauschale richtet sich nach genau diesem Betrag.
> 4. **Nicht enthalten, da keine Angaben:** Verpflegung, Wochenaufenthalt, weitere Versicherungs- und Sparzinsen (ändern am Maximum nichts), Krankheitskosten, Spenden und Weiterbildung.
> 5. **Fachliche Beurteilung:** Sie bleibt bei der zuständigen Fachperson. Keiner der Werte ist ✅ verifiziert.

