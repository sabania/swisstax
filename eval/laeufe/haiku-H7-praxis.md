# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 40 · Lauf: 2026-11-09 15:54
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q01

**Frage:** Mandantin (ZH, 2025) bringt: Lohnausweis, Krankenkassen-Prämienrechnung, Handyrechnung, 3a-Bescheinigung, Hausratversicherungspolice, Spendenquittung Rotes Kreuz CHF 80, Kita-Rechnungen. Welche sind relevant, wofür?

**Soll (Referenz):** Relevant: Lohnausweis (Einkünfte 1.1), Krankenkassenprämien (Versicherungsabzug Ziff. 15, Form. 365), 3a-Bescheinigung (Ziff. 14), Kita-Rechnungen (Ziff. 16.6 Drittbetreuung, max. 25'000 Kanton / 25'800 Bund). Spende CHF 80: unter Mindestbetrag 100 → nicht abziehbar (sofern Total < 100). Nicht relevant: Handyrechnung (Lebenshaltung), Hausratversicherung (kein Versicherungsabzug).

**Antwort des Agenten** (43.7 s · Tools: 10 Aufrufe steuerwiki__ablage, read, steuerwiki__suche):

> **Mandantin, ZH 2025: Relevanz und Ablage der 7 Dokumente**
> 
> | Dokument | Steuerrelevant? | Wofür (ZH 2025) | Einreichen? | Kategorie (KATEGORIEN.md) |
> |---|---|---|---|---|
> | **Lohnausweis** | ✅ ja | Einkommen, Ziff. 1.1/1.2; Form. 360 (Ziff. 2–5), Form. 367 | ja (immer, inkl. Beilagen, § 134 Abs. 1 lit. a StG) | Belege eingereicht, «Eingereicht?» = ja |
> | **3a-Bescheinigung** | ✅ ja | Abzug Säule 3a, Ziff. 14.1/14.2 (Form. 21 EDP) | ja | Belege eingereicht, «Eingereicht?» = ja |
> | **Krankenkassen-Prämienrechnung** | ✅ ja | Abzug Versicherungsprämien, Ziff. 15 / Form. 365 Teil A Ziff. 1–4 | auf Verlangen (Formular Versicherungsprämien beilegen) | Belege Sonstiges, «Eingereicht?» = nein |
> | **Kita-Rechnungen** | ✅ bedingt | Kinderbetreuungsabzug, Ziff. 16.6 (max. CHF 25'000 je Kind für Drittbetreuung) | Aufstellung der Kosten mit Empfängern beilegen; Rechnungen auf Verlangen | Belege Sonstiges, «Eingereicht?» = nein (siehe Hinweis 1) |
> | **Spendenquittung Rotes Kreuz, CHF 80** | ⚠️ bedingt | Ziff. 22.2 (gemeinnützige Zuwendungen), nur wenn das Jahrestotal ≥ CHF 100 | auf Verlangen (Zuwendungsliste beilegen) | Belege Sonstiges, nur wenn der Abzug zählt (Hinweis 2) |
> | **Handyrechnung** | ❌ nein | Privates Telefon ist Lebenshaltung, nicht abziehbar (Art. 34 lit. a DBG) | – | keine Steuerbeleg-Kategorie |
> | **Hausratversicherungspolice** | ❌ nein | Hausrat-/Haftpflichtprämien gehören nicht zu den abziehbaren Prämien; Form. 365 nennt nur Kranken-, Unfall-, Lebens- und Sparzinsprämien | – | keine Steuerbeleg-Kategorie (Grund: nicht abziehbar) |
> 
> **Hinweise und offene Punkte**
> 
> 1. **Kita:** Die Wegleitung verlangt eine Kostenaufstellung beizulegen. Die Rechnungen selbst müssen nur auf Verlangen vorgelegt werden. Ich habe die Rechnungen als «Belege Sonstiges» eingeordnet. Die Aufstellung fällt nach der Listenregel unter «Belege eingereicht». Bitte bestätigen, welche Variante Ihre Kanzlei will. Abzugsfähig sind nur Kinder unter 14 Jahren im Haushalt, und die Kosten müssen mit Erwerbstätigkeit, Ausbildung oder Krankheit zusammenhängen. Bitte prüfen, ob das zutrifft.
> 2. **Spende CHF 80:** Der Abzug gilt erst ab CHF 100 Zuwendungen pro Jahr. Ohne weitere Spenden 2025 ist die Quittung nicht abziehbar. Bitte fragen, ob die Mandantin 2025 noch weitere Spenden gemacht hat.
> 3. **Handy:** Nur der beruflich bedingte Anteil könnte relevant sein, und das nur bei effektiven Berufskosten. Bei der Pauschale (3 % des Nettolohns, mindestens CHF 2'000, Ziff. 11) ist kein Einzelbeleg nötig. Dies habe ich nur aus der Berufskostenregel abgeleitet und nicht im Chunk geöffnet.
> 4. **Hausrat:** Die Nicht-Abziehbarkeit ist im ZH-Wiki nicht ausdrücklich belegt. Die Quelle, die der Ablage-Vorschlag zitiert, betrifft den Kanton AR. Die Einordnung stützt sich auf die Liste der abziehbaren Prämien in Form. 365.
> 5. **Kategorien:** Die Zuordnungsliste der Firma ist noch nicht bestätigt («Bestätigt» leer). Die Kategorien sind deshalb vorläufig.

## q02

**Frage:** In welche Ziffer und mit welchem Code der ZH-Steuererklärung 2025 gehört der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb)?

**Soll (Referenz):** Ziff. 1.1 Haupterwerb, Code 100 (Person 1) / 101 (Person 2); Nettolohn Lohnausweis Ziff. 11 (zh-form-300-2025).

**Antwort des Agenten** (25.3 s · Tools: 2 Aufrufe steuerwiki__beleg, steuerwiki__position):

> Der Nettolohn aus Ziff. 11 des Lohnausweises von Person 1 gehört in **Ziff. 1.1 «Haupterwerb unselbständig», Code 100** (Hauptformular Form. 300, ZH 2025).
> 
> - **Bund:** Dieselbe Zeile gilt für Staats- und Bundessteuer. Es gibt keinen Unterschied zwischen den Spalten.
> - **Berechnung:** Einzusetzen ist die Summe der Ziff. 11 aller Haupterwerbe von Person 1. Ziff. 11 ergibt sich aus Bruttolohn (Ziff. 8) minus AHV/IV/EO/ALV (Ziff. 9) minus BVG (Ziff. 10.1/10.2).
> - **Lohnausweis-Ziff. 10.2:** Ein vom Lohn abgezogener BVG-Einkauf ist bereits im Nettolohn enthalten. Er darf nicht nochmals unter Ziff. 16.1 (Code 280) abgezogen werden.
> - **Beilage:** Der Lohnausweis muss der Steuererklärung beigelegt werden.
> 
> Quelle: Chunk `zh-form-300-2025__c0004`. Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> Hinweis: Die Beleg-Auskunft markiert Ziff. 1.1 zusätzlich mit «nur Selbständigerwerb/Geschäftsvermögen». Das widerspricht der Positionsauskunft und dem Formular-Chunk, die Ziff. 1.1 für unselbständige Haupterwerbe ausweisen. Das würde ich vor dem Ausfüllen am Formular (`zh-form-300-2025.pdf`) gegenprüfen.

## q03

**Frage:** Lohnausweis Feld F ist angekreuzt (Geschäftsauto). Was bedeutet das für den Fahrkostenabzug (SG 2025)?

**Soll (Referenz):** Feld F angekreuzt → kein Fahrkostenabzug für den Arbeitsweg mit Geschäftsfahrzeug (Privatanteil im Lohn, Lohnausweis Ziff. 2.2).

**Antwort des Agenten** (31.7 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__suche, steuerwiki__wert):

> **Kurz:** Mit angekreuztem Feld F gibt es für den Arbeitsweg keinen Fahrkostenabzug. Die Kombination mit «Geschäftsauto» passt aber nicht zusammen, und das sollten Sie vor dem Ausfüllen klären.
> 
> **Was Feld F bedeutet (SG 2025)**
> - Feld F steht für unentgeltliche Beförderung zwischen Wohn- und Arbeitsort, z.B. Sammeltransport oder ein vom Arbeitgeber getragenes GA aus geschäftlichen Gründen.
> - Wenn Feld F angekreuzt ist, sind dem Arbeitnehmer keine Kosten entstanden. Deshalb gibt es in Formular 4 Ziff. 1.1 (ÖV) und Ziff. 1.3 (Motorfahrzeug) keinen Abzug. (sg-wl-2025__c0075; sg-form-4-2025__c0001/c0002)
> 
> **Warum «Geschäftsauto» und Feld F nicht zusammenpassen**
> - Ein Geschäftsauto mit Privatnutzung wird im Lohnausweis über Ziff. 2.2 als Privatanteil erfasst. Der Privatanteil ist mit 0,9 % pro Monat (10,8 % pro Jahr) zu versteuern.
> - Für diesen Fall gilt laut StB 39 Nr. 3 ausdrücklich: «kein Kreuz im Feld F». (sg-stb-39-3__c0013)
> - Kreuze ich Feld F bei einem Geschäftsauto, passt die Angabe also nicht zur Privatnutzung. Entweder ist Feld F falsch gesetzt, oder der Arbeitgeber meint etwas anderes (z.B. ein GA oder eine Sammelfahrt).
> 
> **Was das für den Fahrkostenabzug heisst**
> - **Feld F angekreuzt:** kein Fahrkostenabzug.
> - **Privatanteil 0,9 % pro Monat, Feld F leer:** ebenfalls kein Abzug (Form. 4 Ziff. 1.3). Die einzige Ausnahme ist eine effektive Abrechnung mit Bordbuch. Dann können die tatsächlichen Arbeitswegkosten bis zum Maximum von Fr. 8'000 abgezogen werden. (sg-wl-2025__c0076; sg-stb-39-3__c0018)
> - **Fahrkostenentschädigung im Bruttolohn (Ziff. 2.3):** Hier ist der Abzug bis Fr. 8'000 möglich, aber dann darf Feld F nicht angekreuzt sein.
> 
> **Empfehlung**
> 1. Den Lohnausweis mit dem Arbeitgeber klären: Ist das Auto privat nutzbar (dann Ziff. 2.2 ausfüllen und Feld F leer lassen)? Oder gibt es tatsächlich ein GA oder eine Sammelfahrt (dann bleibt Feld F, aber ohne Auto-Abzug)?
> 2. Falls Bordbuch geführt wird, lohnt sich die effektive Abrechnung nur, wenn die tatsächlichen Arbeitswegkosten über dem Privatanteil liegen. Das prüfe ich gern mit konkreten Zahlen.
> 
> **Offen / Einschränkungen**
> - Die Angaben zu Feld F und Bordbuch sind laut Wiki «agent-geprüft» (Fundstelle geprüft, Abnahme offen).
> - Ich habe nur die SG-Regel geprüft. Für die direkte Bundessteuer habe ich die Feld-F-Regel nicht separat belegt. Der Bund-Maximalabzug liegt bei Fr. 3'300.
> - Das Lohnausweis-Merkblatt im Wiki gilt nur für 2026. Die Regel oben stammt aus WL SG 2025.

## q04

**Frage:** Wie hoch ist der maximale Fahrkostenabzug 2025 in TG (Staatssteuer) und beim Bund, und welcher km-Ansatz gilt für das Auto?

**Soll (Referenz):** TG 2025 Staat max. CHF 6'000 (tg-stg__par-29), Bund max. CHF 3'300 (bund-dbg-2025__art-26); Auto TG gestaffelt 0.60/0.50/0.40 je nach Jahres-km, Bund 0.70.

**Antwort des Agenten** (26.7 s · Tools: 3 Aufrufe steuerwiki__wert):

> **Kanton Thurgau (Staatssteuer) 2025**
> - **Fahrkosten Wohn-/Arbeitsstätte: max. CHF 6'000** pro Jahr. Quelle: tg-stg__par-29. Status ☑️ agent-geprüft (Abnahme offen).
> - **km-Ansatz Privatauto: gestaffelt**, nur wenn der ÖV nicht zumutbar ist:
>   - bis 3'000 km: CHF 0.60/km
>   - 3'001–5'000 km: CHF 0.50/km
>   - über 5'000 km: CHF 0.40/km
> 
>   Die Stufen werden kumuliert berechnet. Die Wegleitung nennt 8'000 km = CHF 4'000 (3'000×0.60 + 2'000×0.50 + 3'000×0.40). Quelle: tg-bkv__par-1 und StP 29 Nr. 2. Status ☑️.
> - Bei Privatauto-Berechnung bei 100 % Tätigkeit gelten in der Regel **höchstens 225 Arbeitstage** pro Jahr (Wegleitung, tg-wl-2025__c0003).
> 
> **Bund (direkte Bundessteuer) 2025**
> - **Fahrkosten: max. CHF 3'300** pro Person und Jahr (DBG Art. 26 Abs. 1 lit. a).
> - **km-Ansatz Auto: CHF 0.70/km** einheitlich, nur ohne zumutbaren ÖV (Anhang 1 BKV). Ab 2026 gilt CHF 0.75/km, für 2025 nicht anwendbar.
> - Der Bund kennt keine Arbeitstage-Regel.
> 
> **Offen:** Die ESTV-Wegleitung 2025 (S. 6) nennt beim Bund noch «maximal 3200 Franken». Das Gesetz nennt 3'300, und ich halte mich ans Gesetz. Die Wegleitung dürfte nicht nachgeführt sein. Vor einer Abgabe lohnt sich eine Prüfung.
> 
> Beim TG-Abzug sind alle Fahrkosten zusammen zu rechnen, inklusive Wochenaufenthalt und Nebenerwerb. Der Bund wird im TG-Formular separat deklariert.

## q05

**Frage:** Welcher km-Ansatz für Autos gilt 2026 bei der direkten Bundessteuer?

**Soll (Referenz):** CHF 0.75 pro km (bund-mm-2025-09-11-kalte-progression-2026__c0004; RS 2-215).

**Antwort des Agenten** (26.8 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Bund 2026: CHF 0.75 pro Fahrkilometer** für den Arbeitsweg mit dem Privatauto (bisher CHF 0.70).
> 
> - **Bedingung:** Der Ansatz gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist.
> - **Maximum:** Die Fahrkosten Wohn-/Arbeitsstätte sind insgesamt auf **CHF 3'300** pro Jahr begrenzt.
> - **Grundlage:** Der Abzug richtet sich neu nach dem TCS-Kilometerpreis für das Musterauto. Anpassungen können künftig nach oben und unten erfolgen.
> 
> Fundstellen:
> - Wert: `bund-mm-2025-09-11-kalte-progression-2026__c0004` (ESTV-Mitteilung 11.09.2025), Status ☑️ agent-geprüft, Abnahme offen
> - Maximum 3'300: `bund-dbg-2026__art-26` (Art. 26 DBG), Status ☑️
> - Ansatz und Maximum werden außerdem in der Wegleitung zum Lohnausweis 2026 (`bund-wl-2a-2026__c0043`) genannt.
> 
> Zur Einordnung: Für Velo und Mofa gilt eine Pauschale von CHF 700 pro Jahr, für Motorräder mit weissem Kontrollschild CHF 0.40 pro Kilometer.
> 
> Die Frage war ohne Kanton gestellt; die obigen Werte sind die Bundeswerte. Kantonale Formulare können für die Kantonssteuer eigene Ansätze führen. Nennen Sie den Kanton (AR, SG, TG oder ZH), dann prüfe ich die kantonale Angabe.

## q06

**Frage:** Maximaler Säule-3a-Abzug 2025 für eine Arbeitnehmerin mit Pensionskasse? Und für eine Selbständige ohne 2. Säule?

**Soll (Referenz):** Mit 2. Säule CHF 7'258; ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288 (bund-bsv-masszahlen-2025-2026__c0003).

**Antwort des Agenten** (24.7 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Bund 2025 (direkte Bundessteuer):**
> 
> - **Arbeitnehmerin mit Pensionskasse (2. Säule): CHF 7'258**
> - **Selbständige ohne 2. Säule: 20 % des Erwerbseinkommens, maximal CHF 36'288**
> 
> Die Werte stammen aus dem Steuer-Wiki: Höchstbetrag mit 2. Säule `bund-bsv-masszahlen-2025-2026__c0003`, Höchstbetrag ohne 2. Säule ebenfalls `bund-bsv-masszahlen-2025-2026__c0003`, 20 %-Regel `bund-bvv3__art-7`. Status ☑️ agent-geprüft, die Abnahme ist noch offen.
> 
> Für die kantonale Staats- und Gemeindesteuer kann der Ansatz abweichen. Welcher Kanton gilt (Wohnsitz am 31.12.2025: AR, SG, TG oder ZH)? Dann prüfe ich die kantonalen Werte.

## q07

**Frage:** Kinderabzug 2025 in AR für ein 10-jähriges Kind – und beim Bund?

**Soll (Referenz):** AR 2025: CHF 7'400 (4.–15. Altersjahr; Anhang 1 StG, ar-stg-anhang-kp__c0001); Bund CHF 6'800 (Art. 35 DBG) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (24.8 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kanton Appenzell Ausserrhoden (AR), Steuerjahr 2025, Kind 10 Jahre:** CHF 7'400 Sozialabzug (Form. Ziff. 23.2, Kinderabzug nach dem 4. bis zum 15. Altersjahr).
> 
> **Bund (direkte Bundessteuer), Steuerjahr 2025:**
> - Sozialabzug: CHF 6'800. Beim Bund gibt es keine Altersstaffelung.
> - Zusätzlich ein Abzug vom Steuerbetrag von CHF 263 pro Kind (Art. 36 Abs. 2bis DBG). Dieser ist eine Ermässigung der Steuer, kein Abzug vom Einkommen, und gilt nur für den Bund.
> 
> **Quellen (Fundstellen):**
> - AR: `ar-stg-anhang-kp__c0001`, Art. 38 Abs. 1 lit. a Ziff. 2 (7'400)
> - Bund: `bund-dbg-2025__art-35` (6'800) und `bund-dbg-2025__art-36-t4` (263)
> 
> **Status:** Alle Werte sind ☑️ agent-geprüft: Die Fundstellen sind geprüft, die Abnahme durch die Fachperson steht noch aus.
> 
> Die Vermögens- und Versicherungszuschläge (AR: CHF 1'000 Versicherungszuschlag pro Kind; Bund: CHF 700) habe ich nicht eingerechnet, weil Sie danach nicht gefragt haben.

## q08

**Frage:** Versicherungsabzug ZH 2025 für ein Ehepaar mit 2 Kindern, beide mit Pensionskasse (Staatssteuer und Bund)?

**Soll (Referenz):** ZH Staat: 5'800 + 2 × 1'300 = 8'400; Bund: 3'700 + 2 × 700 = 5'100 (zh-stg-2025__par-31-t2, bund-dbg-2025__art-33).

**Antwort des Agenten** (26.3 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Kurzantwort: ZH 2025 maximal CHF 8'400 (Staatssteuer) und CHF 5'100 (Bundessteuer).** Das ist eine Obergrenze. Abgezogen wird der kleinere Wert aus Ihren tatsächlich bezahlten Prämien und diesem Maximum.
> 
> **Berechnung für Ehepaar mit 2 Kindern, beide mit Pensionskasse (Stand 2025)**
> 
> | | Staatssteuer ZH | Bundessteuer |
> |---|---|---|
> | Grundabzug verheiratet (mit 2./3a-Beiträgen) | 5'800 | 3'700 |
> | Zuschlag 2 × Kind | 2 × 1'300 = 2'600 | 2 × 700 = 1'400 |
> | **Maximum** | **8'400** | **5'100** |
> 
> **Quellen und Status**
> - Staat: `zh-stg-2025__par-31-t2` (versicherung.verheiratet 5'800; versicherung.kind 1'300) · ☑️ agent-geprüft, Abnahme offen
> - Bund: `bund-dbg-2025__art-33-t2` (3'700) und `bund-dbg-2025__art-33-t5` (700 je Kind) · ☑️ agent-geprüft, Abnahme offen
> - Formular: Ziff. 15 (Code 270), Hilfsblatt Form. 365 Teil B, Ziff. 1 und 3 (Codes 611, 613–615). Beide Spalten (Staat und Bund) sind getrennt auszufüllen.
> 
> **Hinweise**
> - Die Grenze «ohne Vorsorge» (8'700 bzw. 5'550) gilt nicht, weil beide Ehegatten Pensionskassenbeiträge leisten.
> - Den tatsächlichen Abzug bestimmen die bezahlten Prämien (Krankenkasse, Unfall, Leben/Rente, Sparzinsen, abzüglich Prämienverbilligung). Ist der Betrag tiefer als das Maximum, gilt er.
> - Die Obergrenzen gelten nur für Beiträge in die Versicherungsprämien; die Pensionskassenbeiträge selbst sind in der Position «Berufliche Vorsorge» zu erfassen, nicht hier. Das habe ich im Wiki nicht gesondert geprüft.

## q09

**Frage:** Wie hoch ist der Kinderdrittbetreuungsabzug 2025 im Kanton ZH, und gilt 2026 ein anderer Wert?

**Soll (Referenz):** ZH 2025 CHF 25'000 (StG Nachtrag 127, zh-stg-2025__par-31-t4); 2026 CHF 25'300 (zh-stg-2026__par-31-t3). Die VKP ab 2024 (10'400) ist überholt.

**Antwort des Agenten** (27.1 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kanton ZH, Staatssteuer:**
> 
> - **2025:** max. **CHF 25'000** pro Kind
> - **2026:** max. **CHF 25'300** pro Kind, also um CHF 300 höher
> 
> Der Abzug gilt nur für nachgewiesene Kosten, höchstens bis zum Maximum. Das Kind muss im Steuerjahr das 14. Altersjahr noch nicht vollendet haben und im gleichen Haushalt leben. Die Kosten müssen im direkten Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit stehen.
> 
> **Für 2026 kommt eine Regel dazu:** Bei Konkubinat oder alternierender Obhut mit gemeinsamer elterlicher Sorge gibt es je die Hälfte des Abzugs, also CHF 12'650. Die Regel steht nur für 2026 im Wiki. Für 2025 habe ich sie nicht gefunden, deshalb nenne ich sie nicht als gesichert für 2025.
> 
> **Bund (direkte Bundessteuer), getrennt zu deklarieren:** 2025 CHF 25'800, 2026 ebenfalls CHF 25'800.
> 
> **Quellen:**
> - ZH 2025: `zh-stg-2025__par-31-t4`
> - ZH 2026: `zh-stg-2026__par-31-t3`
> - Bund 2025: `bund-dbg-2025__art-33-t7`
> - Bund 2026: `bund-dbg-2026__art-33-t7`
> 
> Alle vier Werte sind ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> 
> **Hinweis zu 2025:** Die alte Verordnung (VKP ab 2024) nennt noch CHF 10'400. Das Gesetz (StG Nachtrag 127) und die Wegleitung 2025 nennen CHF 25'000. Ich habe mich an das Gesetz gehalten, weil es für das Steuerjahr gilt. Der VKP-Wert ist überholt.
> 
> Im Formular ZH ist der Abzug Ziffer 16.6 (Code 376). Soll ich die Rechenregel dazu mit `position` nachschlagen?

## q10

**Frage:** Gibt es im Kanton TG einen Zweiverdienerabzug für die Staatssteuer?

**Soll (Referenz):** Nein, TG kennt keinen kantonalen Zweiverdienerabzug (nur Bund: 50 %, 8'600–14'100).

**Antwort des Agenten** (26.7 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> Nein. Im Kanton Thurgau gibt es für die Staats- und Gemeindesteuer keinen Zweiverdienerabzug.
> 
> **Staatssteuer TG (Steuerjahr 2025):** kein Abzug.
> - Wegleitung TG 2025, S. 23 (Ziffer 18): «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.» (Fundstelle `tg-wl-2025__c0104`, Status ✅ verifiziert)
> - Praxis StP 34 Nr. 25, 1. Allgemeines: «Im Gesetz über die Staats- und Gemeindesteuern des Kantons Thurgau ist kein Zweiverdienerabzug vorgesehen.» (Fundstelle `tg-stp-34-25__c0001`, Status ☑️ agent-geprüft)
> 
> Die Praxis gilt laut Wiki auch für 2026 und 2027. Die Wegleitung 2026 enthält dieselbe Aussage (`tg-wl-2026` c0103).
> 
> **Direkte Bundessteuer (zum Vergleich, separat deklarieren):** Der Zweiverdienerabzug gilt nur hier.
> - 50 % des niedrigeren Erwerbseinkommens, mindestens CHF 8'600, höchstens CHF 14'100 (Art. 33 Abs. 2 DBG, `bund-dbg-2025__art-33-t6`, ☑️ agent-geprüft).
> - Im TG-Formular 2025 steht er in Ziffer 18 (Code 356) und ist nur für die Bundessteuer auszufüllen.
> 
> Die Suchtreffer zu «Zweiverdienerabzug» in der StP 34 betreffen die Bundessteuer oder die Berechnung bei Mitarbeit im Betrieb des Ehegatten. Sie begründen keinen kantonalen Abzug.

## q11

**Frage:** SG 2025: Pauschale für übrige Berufskosten? Wie wird sie berechnet?

**Soll (Referenz):** SG 2025: CHF 700 + 10 % des Nettolohns, max. CHF 2'400 (Art. 21 StV SG, WL SG 2025).

**Antwort des Agenten** (24.2 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **SG 2025, Pauschale für übrige Berufskosten** (unselbständige Erwerbstätigkeit, Art. 21 StV SG)
> 
> **Berechnung:** Fr. 700 + 10 % der Nettoeinkünfte, höchstens Fr. 2'400.
> 
> - **Nettoeinkünfte** = Bruttoeinkünfte abzüglich AHV/IV/EO/ALV/UV- und BVG-Beiträge (ohne Einkäufe).
> - SG kennt kein Minimum. Die Formel nennt nur Fixbetrag, Satz und Maximum.
> - Höhere nachgewiesene Kosten sind vorbehalten. Dann gilt der tatsächliche Aufwand, nicht die Pauschale.
> 
> **Beispiel:** Nettoeinkünfte Fr. 50'000 → 700 + 5'000 = Fr. 5'700, durch den Höchstbetrag auf Fr. 2'400 begrenzt. Der Höchstbetrag wird bei Nettoeinkünften ab Fr. 17'000 erreicht (700 + 10 % = 2'400 ⇒ 17'000).
> 
> Hinweis: Das Beispiel rechne ich nicht per Tool nach. Wenn Sie einen konkreten Nettolohn haben, rechne ich ihn gern exakt.
> 
> **Formular SG 2025:** Ziff. 10.1 (Person 1, Code 438) bzw. Ziff. 10.2 (Person 2, Code 488).
> 
> **Bund (zum Vergleich, separat deklarieren):** 3 % des Nettolohns, mindestens Fr. 2'000, höchstens Fr. 4'000.
> 
> **Quellen und Status:**
> - Art. 21 StV SG, Chunk `sg-stv__art-21`: ☑️ agent-geprüft (Abnahme offen)
> - WL SG 2025, Ziff. 10.3, Chunk `sg-wl-2025__c0080`: ☑️ agent-geprüft (Abnahme offen)
> - Bund: `bund-bkv-2025__anhang-1`: ☑️ agent-geprüft (Abnahme offen)
> 
> Die Suche fand außerdem StB 39 Nr. 9 (`sg-stb-39-9__c0011`) mit einer Pauschale von 20 %, min. Fr. 800, max. Fr. 2'400. Das betrifft die unselbständige **Nebenerwerbstätigkeit** und nicht die Haupterwerbspauschale. Ich habe diesen Chunk nicht geöffnet und nicht geprüft, deshalb übernehme ich ihn nicht.

## q12

**Frage:** Pauschalabzug Liegenschaftsunterhalt in AR für ein 8-jähriges Einfamilienhaus – und wie in ZH?

**Soll (Referenz):** AR: 10 % (Gebäude bis 10 Jahre) bzw. 20 % des Bruttoertrags, nur bis Bruttomietertrag 100'000 (Art. 25 StV AR, MB 03); ZH: einheitlich 20 % ohne Altersstaffel (ZStB 30.2).

**Antwort des Agenten** (30.6 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__vergleich):

> **Annahme:** Steuerjahr 2025, weil Sie kein Jahr genannt haben. Bei 2026 könnten die Werte abweichen; sagen Sie mir das Jahr, dann prüfe ich es nach.
> 
> **AR (Staats- und Gemeindesteuer), 2025: 10 %**
> - Gebäude bis 10 Jahre alt: 10 % des Bruttomietertrags. Ein 8-jähriges Haus fällt darunter.
> - Die Pauschale gilt nur, wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.
> - Wahlrecht je Gebäude und Steuerperiode zwischen Pauschale und effektiven Kosten.
> - Fundstelle: ar-mb-03__c0004 (☑️ agent-geprüft, Abnahme offen).
> 
> **ZH (Staats- und Gemeindesteuer), 2025: 20 %**
> - Einheitlich 20 % des Brutto-Mietertrags bzw. Mietwerts, unabhängig vom Gebäudealter. Das Alter spielt in ZH keine Rolle.
> - Wahl pro Liegenschaft und Steuerperiode. Nicht bei vorwiegend geschäftlich genutzten Liegenschaften.
> - Fundstelle: zh-zstb-30-2__c0002 (☑️ agent-geprüft, Abnahme offen).
> 
> **Bund (direkte Bundessteuer), 2025: 10 %** bei Gebäuden bis 10 Jahre, sonst 20 %. Der Bund wird separat deklariert (bund-lkv__art-5).
> 
> **Vergleich mit Ihrem Fall**
> 
> | | Satz | Bedingung |
> |---|---|---|
> | AR | 10 % | Gesamt-Bruttomietertrag ≤ CHF 100'000 |
> | ZH | 20 % | keine Altersstaffelung |
> | Bund | 10 % | Gebäude bis 10 Jahre |
> 
> **Offen bleibt eine Frage, die die Antwort wesentlich ändert:** Ist das Haus vermietet oder selbst bewohnt? Die Pauschale knüpft an den Bruttomietertrag an. Bei einem selbst bewohnten Haus gibt es keinen Mietertrag, und in ZH gilt die Pauschale laut Quelle auch auf den Mietwert. Für AR habe ich keine belegte Aussage, ob die Pauschale auf den Eigenmietwert anwendbar ist. Ich habe das nicht geprüft und nehme es hier nicht an. Der Eigenmietwert selbst wird in AR mit einem Selbstnutzungsabzug von 20 % gekürzt (ar-wl-2025__c0001), in ZH nicht pauschal, sondern über die Weisung 2009 (zh-weisung-liegenschaften-2009__c0033).

## q13

**Frage:** TG: Welcher Einschlag gilt auf dem Eigenmietwert der selbstbewohnten Liegenschaft am Wohnsitz (Kanton vs. Bund)?

**Soll (Referenz):** TG: Abzug 40 % Kanton, 20 % Bund für dauernd selbstbewohntes Eigentum am Wohnsitz (tg-stg__par-23; WL TG 2025).

**Antwort des Agenten** (28.5 s · Tools: 4 Aufrufe steuerwiki__vergleich, steuerwiki__wert, steuerwiki__suche):

> Kurz: Auf den Eigenmietwert selbst gibt es **beim Bund keinen Einschlag**. Ob ein kantonaler Einschlag gilt, hängt vom Kanton ab. Ich habe für das Steuerjahr 2025 geprüft (Jahr nicht genannt, daher 2025; Kanton nicht genannt, daher alle Wiki-Kantone).
> 
> **Bund (direkte Bundessteuer)**
> - Kein prozentualer Einschlag. Der Eigenmietwert wird nach ortsüblichen Verhältnissen und tatsächlicher Nutzung festgesetzt (Art. 21 Abs. 2 DBG). Festgesetzt wird er im kantonalen Veranlagungsverfahren.
> - Abschaffung des Eigenmietwerts per 01.01.2029 beschlossen; 2025–2028 gilt bisheriges Recht. Status: ☑️ agent-geprüft, Quelle für den Eigenmietwert-Satz nicht erfasst (`bund-mm-eigenmietwert-abschaffung__c0002`).
> 
> **Kantone (Eigenmietwert-Abzug / Einschlag)**
> 
> | Kanton | Einschlag auf Eigenmietwert | Fundstelle |
> |---|---|---|
> | ZH | kein Pauschal-Einschlag. Formelwert auf 60–70 % der Marktmiete begrenzt; Einschlag nur bei tatsächlicher Unternutzung (ZStB 21.2) | zh-weisung-liegenschaften-2009__c0033 ☑️ |
> | SG | 30 % | sg-stg-2025__art-34 ☑️ |
> | TG | 40 % | tg-stg__par-23 ☑️ |
> | AR | 20 % | ar-wl-2025__c0001 ☑️ |
> 
> Alle Angaben sind ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> 
> **Nicht verwechseln:** Die Pauschalen 10 %/20 % (Bund, Kanton) betreffen den Brutto-Mietertrag bzw. Mietwert für Unterhaltskosten. Sie sind kein Einschlag auf den Eigenmietwert. Beim Bund hängt der Satz vom Gebäudealter ab (bis 10 Jahre 10 %, über 10 Jahre 20 %).
> 
> Sag mir den Kanton und das Steuerjahr, dann prüfe ich den Fall konkret. Für ZH 2026 gilt eine neue Weisung, die noch nicht im Wiki liegt. Ich habe dafür keine Werte.

## q14

**Frage:** Bis wann kann ein Treuhänder im Kanton TG für seine Mandanten Fristerstreckung erhalten?

**Soll (Referenz):** Gewerbsmässige Treuhänder für Mandanten bis 31.12. des Deklarationsjahres (StP 155 Nr. 2).

**Antwort des Agenten** (27.8 s · Tools: 4 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurz:** Gewerbsmässige Treuhänder und Steuerberater können für ihre Mandanten längstens bis **31. Dezember des Deklarationsjahres** ein Fristerstreckungsgesuch stellen.
> 
> Ich habe Steuerjahr 2025 angenommen, da Sie keines genannt haben. Das Deklarationsjahr ist dann 2026, die Frist also **31. Dezember 2026**. Heute ist der 9. November 2026, es bleiben also rund sieben Wochen. Für Steuerjahr 2026 gilt dieselbe Regel mit Frist 31. Dezember 2027.
> 
> Zum Vergleich mit Privatpersonen:
> - Das erste Gesuch geht grundsätzlich bis **30. September** des Deklarationsjahres, weitere in begründeten Fällen bis **30. November**.
> - Gesuche nach dem 30. November werden abgewiesen, ausser es liegen ausserordentliche Gründe vor. Starke berufliche Beanspruchung des Vertreters oder fehlende Unterlagen genügen dafür nicht.
> 
> Gesuche natürlicher Personen gehen an das Gemeindesteueramt. Das Gesuch muss schriftlich, begründet und rechtzeitig gestellt werden.
> 
> Quelle: StP 155 Nr. 2, Chunk `tg-stp-155-2__c0002` (Gültigkeit Steuerjahre 2025–2027). Status: agent-geprüft, Abnahme offen. Die Gebühren für Fristerstreckungen regelt § 39b StV TG (`tg-stv__par-39b`); ich habe sie hier nicht geprüft.

## q15

**Frage:** ZH: Bis wann ist die Steuererklärung 2025 einzureichen und wie lange wird höchstens Fristerstreckung gewährt?

**Soll (Referenz):** Einreichung bis 31.03.2026; Fristerstreckung längstens bis 30. November (ZStB 132.1 / WL ZH 2025).

**Antwort des Agenten** (26.4 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Kanton Zürich, Steuerjahr 2025 (natürliche Personen):**
> 
> - **Ordentliche Einreichefrist: 31. März 2026.** Quelle: WL ZH 2025, `zh-wl-2025__c0017`.
> - **Höchstens Fristerstreckung: bis 30. November 2026** (längstens bis 30. November des Folgejahres). Quelle: ZStB 132.1, `zh-zstb-132-1__c0024`.
> - **Selbständige und Ausserkantonale:** Von Amtes wegen gilt Frist bis 30. September 2026. Quelle: ZStB 132.1, `zh-zstb-132-1__c0024`.
> 
> **Wichtig für heute (9. November 2026):** Die ordentliche Frist ist abgelaufen. Das Ende der maximalen Erstreckung (30. November 2026) ist in 21 Tagen.
> 
> - Ein Erstreckungsgesuch muss vor Ablauf der Frist eingereicht werden (§ 39 StV, `zh-stv__par-39`). Wenn bis 31. März 2026 keine Erstreckung bewilligt wurde, ist ein neues Gesuch nach dem Datum voraussichtlich verspätet.
> - Darüber hinaus wird eine Erstreckung nur aus ausserordentlichen Gründen gewährt. Berufliche Belastung des Vertreters genügt nicht (ZStB 132.1, `zh-zstb-132-1__c0024`).
> - Mahnfristen sind nicht erstreckbar (ZStB 132.1, `zh-zstb-132-1__c0024`).
> - Wer trotz Mahnung nicht einreicht, wird nach § 42 Abs. 3 StV behandelt (ZStB 132.1, `zh-zstb-132-1__c0032`).
> 
> **Status:** Die Fristen sind agent-geprüft (☑️). Die Fundstellen sind geprüft, die Abnahme durch die Fachperson ist offen. Bitte vor einer Eingabe mit der zuständigen Gemeinde bzw. dem Steueramt abgleichen, ob bereits eine Erstreckung besteht und ob ein Gesuch noch als rechtzeitig gilt.

## q16

**Frage:** AR: Was kostet die zweite Fristverlängerung?

**Soll (Referenz):** CHF 25 (erste Verlängerung kostenlos, jede weitere CHF 25; MB 18 / WL AR 2025).

**Antwort des Agenten** (21.5 s · Tools: 0 Aufrufe ):

> Welcher Kanton ist gemeint: AR, SG, TG oder ZH? Die Gebühr für eine Fristverlängerung wird kantonal geregelt, deshalb nenne ich ohne Kanton keinen Betrag. Ich gehe für das Steuerjahr von 2025 aus, sofern du kein anderes nennst.

## q17

**Frage:** Krankheitskosten SG 2025: Ab welchem Selbstbehalt sind sie abziehbar – und beim Bund?

**Soll (Referenz):** SG: Selbstbehalt 2 % (Art. 46 StG SG); Bund: 5 % (Art. 33 Abs. 1 lit. h DBG, KS 11).

**Antwort des Agenten** (25.1 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kurz:** Im Kanton St. Gallen sind Krankheits- und Unfallkosten 2025 ab **2 %** Selbstbehalt abziehbar, beim Bund ab **5 %**. Die Basis ist jeweils eine andere.
> 
> **Kanton SG 2025**
> - Abziehbar ist der Betrag, der **2 % der Nettoeinkünfte** übersteigt (Nettoeinkommen, Ziff. 20 im Formular).
> - Behinderungsbedingte Kosten sind ohne Selbstbehalt abziehbar.
> - Für Zöliakie gilt eine Pauschale von Fr. 2'500.
> - Formular: Ziff. 21.1 Krankheits- und Unfallkosten.
> - Fundstelle: `sg-stg-2025__art-46`. Status ☑️ agent-geprüft, die Abnahme ist offen.
> 
> **Bund (direkte Bundessteuer) 2025**
> - Abziehbar ist der Betrag, der **5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte** übersteigt.
> - Behinderungsbedingte Kosten (BehiG) sind auch hier ohne Selbstbehalt abziehbar.
> - Der Bund wird separat deklariert, auch wenn er im kantonalen Formular steht.
> - Fundstelle: `bund-dbg-2025__art-33-t3`. Status ☑️ agent-geprüft, die Abnahme ist offen.
> - Praxis 2025/2026 ist die ESTV-KS 11 (31.08.2005). Die KS 11a (publiziert 26.05.2026) gilt laut ihrer Ziff. 7 erst ab Steuerperiode 2027, sie ist für 2025 also nicht massgebend.
> 
> Die beiden Basen sind nicht identisch, deshalb ergibt derselbe Betrag im Kanton und beim Bund meist unterschiedlich hohe Abzüge. Die Basis für den Bund ist dabei nicht das kantonale Nettoeinkommen. Wenn du mir Zahlen zum Fall nennst (Nettoeinkünfte, Krankheitskosten, ob behinderungsbedingt), rechne ich die Abzüge für beide Ebenen durch.

## q18

**Frage:** PK-Einkauf CHF 20'000 wurde über den Lohn abgezogen (Lohnausweis Ziff. 10.2). Darf er nochmals in der Steuererklärung abgezogen werden?

**Soll (Referenz):** Nein – BVG-Einkauf über Lohnabzug (Lohnausweis Ziff. 10.2) ist bereits im Nettolohn berücksichtigt; nur direkt bezahlte Einkäufe separat abziehen.

**Antwort des Agenten** (30.9 s · Tools: 6 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Nein, nicht nochmals.** Ein Einkauf, der über den Lohn abgezogen wurde, darf in der Steuererklärung nicht ein zweites Mal als Abzug geltend gemacht werden.
> 
> **Warum:** Die Lohnausweis-Ziffern 10.x (Beiträge an die 2. Säule, inkl. Ziff. 10.2 «Beiträge für den Einkauf») werden vor dem Nettolohn (Ziff. 11) abgezogen. Der Nettolohn wird dann in die Steuererklärung übertragen. Der Einkauf ist damit schon in den Einkünften gekürzt. Die Wegleitung ZH 2025 formuliert den Abzug in Ziff. 16.1 entsprechend: Zahlungen an Pensionskassen sind abziehbar, *«soweit die unter Ziffern 1 und 2 deklarierten Einkünfte nicht bereits um diese Beiträge gekürzt worden sind»* (`zh-wl-2025__c0092`, `zh-wl-2025__c0035`).
> 
> **Konsequenz für Sie:**
> - Die CHF 20'000 nicht in Ziff. 16.1 eintragen. Der Lohnausweis-Nettolohn enthält den Einkauf bereits als Abzug.
> - Wenn der Einkauf über den Lohn läuft, ist er im Lohnausweis separat auszuweisen (Rubrik «Versicherungsbeiträge»), sonst ist er steuerlich nicht geltend zu machen (`bund-ks-w03-001__c0009`).
> 
> **Was ich nicht geprüft habe:**
> - **Kanton:** Ich habe mit der Wegleitung Zürich gerechnet, weil der Lohnausweis-Aufbau (Ziff. 10.2) dorthin passt. Sagen Sie mir den Wohnsitzkanton am 31.12. (AR, SG, TG oder ZH), dann prüfe ich das gegen dessen Regeln.
> - **Bund:** Ich habe die Bundesregel nicht eigens als Textstelle geprüft. Die Fundstelle KS W03-001 bestätigt nur die separate Ausweisung im Lohnausweis.
> - **Jahr:** Ich bin vom Steuerjahr 2025 ausgegangen.
> - **Höhe und Sperrfrist:** Ob CHF 20'000 im Rahmen des Höchstbetrags liegen, prüfe ich gern, wenn Sie mir Lohnausweis-Angaben und Kanton nennen. Ebenso gilt: Ein Kapitalbezug innert drei Jahren nach dem Einkauf hebt den Abzug auf (ZH Ziff. 16.1).

## q19

**Frage:** Weiterbildungskosten CHF 15'000 (ZH, 2025), Arbeitgeber hat nichts bezahlt. Wie viel ist abziehbar (Kanton/Bund)?

**Soll (Referenz):** ZH Staat max. CHF 12'400 (zh-stg-2025__par-31-t4); Bund max. CHF 13'000 (bund-dbg-2025__art-33-t4).

**Antwort des Agenten** (23.9 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> Bei CHF 15'000 selbst getragenen Weiterbildungskosten (ZH, Steuerjahr 2025, Arbeitgeber zahlt nichts):
> 
> - **Kanton Zürich (Staatssteuer): CHF 12'400 abziehbar.** Limite Ziff. 16.2, Code 292 (Hilfsblatt Form. 367, Block Staatssteuer). Fundstelle: zh-stg-2025__par-31-t4 («bis zum Gesamtbetrag von Fr. 12 400»). Status ☑️ agent-geprüft, Abnahme offen.
> - **Bund (direkte Bundessteuer): CHF 13'000 abziehbar.** Separat in der Bundessteuer-Spalte. Fundstelle: bund-dbg-2025__art-33-t4 («bis zum Gesamtbetrag von 13 000 Franken»). Status ☑️ agent-geprüft, Abnahme offen.
> 
> Die Differenz zu den Kosten (2'600 Kanton, 2'000 Bund) ist nicht abziehbar.
> 
> **Voraussetzung, die Sie prüfen müssen:** Der Abzug gilt nur, wenn Sie einen Abschluss auf Sekundarstufe II haben oder im Steuerjahr das 20. Altersjahr vollendet haben, und die Ausbildung nicht die erste Sek.-II-Ausbildung ist. Ist das nicht erfüllt, entfällt der Abzug.
> 
> **Weitere Punkte:**
> - Massgebend ist das Datum der Fälligkeit bzw. Zahlung, nicht der Kursbesuch.
> - Die Kosten sind vollständig selbst getragen, daher kein Abzug von Beiträgen Dritter.
> - Einzureichen sind die Kursrechnungen und Zahlungsbelege sowie das Formular «Berufsorientierte Aus- und Weiterbildungskosten» (Ziff. 16.2). Das Formular ist bei ZH nur auf Verlangen beizulegen, sollten Sie es also trotzdem bereithalten.

## q20

**Frage:** Spenden CHF 50 an eine gemeinnützige Organisation (TG 2025) – abziehbar?

**Soll (Referenz):** Nein – TG: Zuwendungen nur abziehbar, wenn sie CHF 200 übersteigen (StG TG § 34 Abs. 1 Ziff. 11); Bund: ab CHF 100.

**Antwort des Agenten** (25.5 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Kurz: Nein, nicht bei CHF 50 allein.** Der Betrag ist in TG 2025 nicht abziehbar, sofern die Spenden des Jahres insgesamt nicht über CHF 200 liegen.
> 
> **Kanton Thurgau 2025**
> - Freiwillige Zuwendungen sind nur abziehbar, soweit sie gesamthaft CHF 200 übersteigen (Freibetrag). Bei CHF 50 ist der Abzug also 0.
> - Beispiel: Gesamtspenden CHF 260 → abziehbar CHF 60.
> - Höchstabzug: 20 % des Nettoeinkommens, bei Nettoeinkommen bis CHF 40'000 maximal CHF 8'000.
> - Fundstelle: `tg-stg__par-34-t4` (StG TG § 34 Abs. 4). Status ☑️ agent-geprüft, Abnahme offen.
> - Formular: TG 2025 Ziff. 23.2 «Freiwillige Zuwendungen» (Formular 6, Code 366). Belege ab CHF 1'000 pro Zuwendung einreichen (WL 2025 Ziff. 23.2).
> 
> **Bund 2025 (separat deklarieren)**
> - Freigrenze CHF 100: Erreichen die Spenden im Jahr CHF 100, ist der ganze Betrag abziehbar, nicht nur der Teil darüber. Bei CHF 50 also ebenfalls 0.
> - Höchstabzug: 20 % der um die Aufwendungen verminderten Einkünfte.
> - Fundstelle: `bund-dbg-2025__art-33a`. Status ☑️ agent-geprüft, Abnahme offen.
> 
> **Zusätzlich zu prüfen**
> - Empfänger: Abziehbar sind nur Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentliche oder gemeinnützige Zwecke) sowie an Bund, Kantone und Gemeinden. Die Steuerverwaltung TG führt ein Verzeichnis der abzugsfähigen Institutionen (WL TG 2025, Formular 6). Ob die Organisation dort steht, sollten Sie vor dem Abzug prüfen.
> - Gemischte Zwecksetzung (Kultur und Gemeinnützigkeit) und Zuwendungen mit Gegenleistung (z. B. Eintritt, Auktionserlös) werden nicht pauschal abgezogen. Nennen Sie mir die Organisation, dann prüfe ich den Einzelfall.
> 
> **Fazit für Ihren Fall:** Die CHF 50 bringen Ihnen in TG und beim Bund keinen Abzug. Relevant wird die Spende erst, wenn die Jahressumme aller Zuwendungen die Schwellen überschreitet. Die Summe sollten Sie in Formular 6 erfassen.

## q21

**Frage:** Was ändert sich 2026 bei der Säule 3a (Einkauf) und wo wird das im ZH-Formular 2026 eingetragen?

**Soll (Referenz):** Ab 2026 Einkauf (Nachzahlung) Säule 3a für Beitragslücken ab 2025 (max. 7'258 pro Einkaufsjahr, BVV 3 Art. 7a, KS 18a); ZH-Formular 2026: Ziff. 14.3 (Code 264, Detailfelder 276/278).

**Antwort des Agenten** (25.2 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__suche):

> **Kurz:** Neu ab Steuerperiode 2026 gibt es in der Säule 3a einen **Einkauf für Beitragslücken**. Er kommt zusätzlich zu den ordentlichen Beiträgen und wird im ZH-Formular 2026 in **Ziff. 14.3** eingetragen.
> 
> **Was sich ändert (ZH und Bund, gleiche Regel)**
> - Einkauf ist für Lücken möglich, die **ab 1.1.2025** entstanden sind, und zwar innerhalb der letzten zehn Jahre vor dem Einkauf.
> - Voraussetzungen: In den Lückenjahren wurden AHV/IV/EO-Beiträge geleistet, und im Einkaufsjahr wurde der volle ordentliche Maximalbeitrag einbezahlt.
> - Höchstbetrag: der Einkauf ist höchstens die Summe der Lücken und in jedem Fall **CHF 7'258** (ZH: Wegleitung 2026 UJ, Ziff. 14; Bund: Wegleitung 2a 2026).
> - Für Steuerjahr 2026 ist faktisch nur die Lücke 2025 einkaufbar.
> 
> **Eintrag im ZH-Formular 2026 (Ziff. 14.3)**
> - **Code 276** für Person 1, **Code 278** für Person 2, Summe in die Hauptkolonne **Code 264**.
> - Rechnen je Person: min(Einkauf; Summe der Beitragslücken ab 1.1.2025; 7'258).
> - Belege: Einkaufsbescheinigung der 3a-Einrichtung; die 3a-Bescheinigung für den ordentlichen Beitrag als Nachweis des vollen Maximalbetrags im Einkaufsjahr; Nachweis der AHV/IV/EO-Beiträge im Lückenjahr.
> - Kanton und Bund stehen in derselben Spalte (gleicher Betrag).
> 
> **Dazu gehört die ordentliche Position (Ziff. 14.1/14.2, unverändert)**
> - Codes 260/261 (eff. 262/263) für die im Jahr 2026 tatsächlich bezahlten Beiträge.
> - Höchstbetrag mit 2. Säule CHF 7'258; ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288.
> 
> **Vorbehalte**
> - Das reguläre ZH-Formular 2026 ist laut Steuerwiki-Stand 09.11.2026 noch nicht publiziert. Die Zuordnung stützt sich auf das Formular für die unterjährige Steuerpflicht (Form. 300 UJ). Ziffern und Codes bitte am regulären Formular prüfen, sobald es vorliegt.
> - Die Angaben sind agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Rechtsgrundlage ist nur aus der Wegleitung belegt, der Artikel in BVV 3 wurde nicht aus einem Chunk bestätigt.
> 
> Quellen: `zh-wl-2026-uj__c0075`, `zh-wl-2026-uj__c0077`, `zh-form-300-2026-uj__c0008`, `bund-wl-2a-2026__c0051`.

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (37.6 s · Tools: 10 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurzantwort:** Die 35 % Verrechnungssteuer auf Dividenden schweizerischer Gesellschaften werden nicht über ein separates Rückforderungsformular zurückgefordert. Sie gehört in die **Steuererklärung** des Steuerjahrs, in dem die Dividende fällig wurde. Der Anspruch wird im **Wertschriftenverzeichnis** ausgewiesen. Ich habe Steuerjahr 2025 angenommen, weil keines genannt war.
> 
> **1. Voraussetzung: Deklaration**
> - Wer die mit Verrechnungssteuer belasteten Erträge und das Vermögen, aus dem sie fliessen, in der Steuererklärung deklariert, erfüllt die Deklarationspflicht nach Art. 23 Abs. 1 VStG. Dann besteht der Anspruch auf Rückerstattung, sofern die weiteren Voraussetzungen der Art. 21 ff. VStG erfüllt sind. (KS VST 48, Ziff. 3.1.1, `bund-ks-vst-48__c0003`)
> - Die Steuerbehörde des Kantons, bei dem Sie die Steuererklärung einreichen, ist für die Rückerstattung zuständig. (WL ZH 2025, `zh-wl-2025__c0161`)
> 
> **2. Ausweis im Wertschriftenverzeichnis (Kanton Zürich, 2025)**
> - Erträge mit abgezogener Verrechnungssteuer stehen in **Kolonne A**, Erträge ohne Abzug in **Kolonne B** (WL ZH 2025, `zh-wl-2025__c0155`).
> - Der Anspruch beträgt 35 % des Total Bruttoertrag A. Er wird auf 5 Rappen gerundet, zum Beispiel CHF 30.224 → CHF 30.20 (WL ZH 2025, `zh-wl-2025__c0220`).
> - Qualifizierte Beteiligungen (mindestens 10 % am Kapital) kennzeichnen Sie mit **Q** (WL ZH 2025, `zh-wl-2025__c0155`).
> - Die Totale für Bruttoertrag (Zeile 150) und Verrechnungssteueranspruch stehen im Formular 340 ZH 2025, Seite 3 (`zh-form-340-2025__c0005`).
> - Die genauen Zeilennummern des Anspruchs habe ich nicht im Volltext bestätigt. Die OCR-Texte sind dort lückenhaft. Ich prüfe sie gern mit `position zh 2025 Verrechnungssteuer`.
> 
> **3. Nicht verwechseln**
> - Die **DA-1** betrifft nur die Anrechnung **ausländischer** Quellensteuern (Kolonnen Steuerwert, Bruttoertrag, nicht rückforderbare ausländische Steuern). Die schweizerische Verrechnungssteuer wird damit nicht zurückgefordert (DA-1 2025, `bund-form-da1-2025__c0002`).
> 
> **Offen:** Für eine Angabe, welche Zeile und welcher Betrag im Kanton Ihres Wohnsitzes am 31.12. gilt, brauche ich den **Kanton** (AR, SG, TG oder ZH). Das Wertschriftenverzeichnis ist kantonal. Die Grundregel von 35 % und der Ablauf über die Deklaration gelten bundesweit.

## q23

**Frage:** Vergleiche den Versicherungsabzug 2025 für Alleinstehende ohne Kinder in AR, SG, TG, ZH und beim Bund.

**Soll (Referenz):** Alleinstehend ohne Kinder 2025 (mit 2. Säule/3a): AR 2'700 · SG 3'400 · TG 3'500 · ZH 2'900 · Bund 1'800.

**Antwort des Agenten** (25.3 s · Tools: 1 Aufrufe steuerwiki__vergleich):

> **Versicherungsabzug 2025, alleinstehend, ohne Kinder** (Stand Wiki, Status ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen)
> 
> | Kanton / Bund | Abzug mit Vorsorgebeiträgen (2./3. Säule) | Abzug ohne Vorsorgebeiträge | Fundstelle (mit Vorsorge) |
> |---|---|---|---|
> | **Bund** | CHF 1'800 | CHF 2'700 | bund-dbg-2025__art-33-t2 |
> | **ZH** | CHF 2'900 | CHF 4'350 | zh-stg-2025__par-31-t2 |
> | **SG** | CHF 3'400 | CHF 3'900 | sg-stg-2025__art-45-t2 |
> | **TG** | CHF 3'500 | nicht vorgesehen | tg-stg__par-34-t3 |
> | **AR** | CHF 2'700 | nicht vorgesehen | ar-stg__art-35-t2 |
> 
> **Einordnung:**
> - **Höchster Abzug mit Vorsorge:** TG (CHF 3'500), knapp vor SG (CHF 3'400). **Tiefster:** Bund (CHF 1'800).
> - **Ohne Vorsorgebeiträge** sind nur Bund, ZH und SG als eigener Satz ausgewiesen. Ob dieser Fall für Sie zutrifft, hängt davon ab, ob Beiträge an die 2. oder 3. Säule geleistet werden.
> - Der **Bund** erfasst den Abzug gemäss Formular in der kantonalen Erklärung. Die Bundesspalte gilt für die direkte Bundessteuer, getrennt vom Kanton.
> 
> **Offene Punkte:**
> - Die Werte sind agent-geprüft, aber noch nicht abgenommen. Vor einer Abgabe bitte gegen die Fundstellen (Chunk-IDs oben) prüfen.
> - Ich habe die Zeile «ohne Vorsorge» für TG und AR nicht gefunden. Ob es dort tatsächlich keinen eigenen Satz gibt oder ob der Wert im Wiki fehlt, kann ich nicht sicher sagen. Eine Nachprüfung mit `wert tg 2025 versicherung.alleinstehend_ohne_vorsorge` bzw. `wert ar …` würde das klären.

## q24

**Frage:** Steuerfreie Vermögensbeträge (Sozialabzüge) 2025 in SG für ein Ehepaar mit einem minderjährigen Kind?

**Soll (Referenz):** SG 2025: 150'000 (Ehepaar) + 20'000 pro minderjähriges Kind = 170'000 (sg-stg-2025__art-64).

**Antwort des Agenten** (26.9 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kanton St. Gallen, Steuerjahr 2025, Ehepaar mit einem minderjährigen Kind: Sozialabzüge auf dem Reinvermögen von insgesamt Fr. 170'000.**
> 
> - **Ehepaar (gemeinsam steuerpflichtig): Fr. 150'000** (2 × Fr. 75'000)
> - **Minderjähriges Kind: Fr. 20'000** zusätzlich
> 
> Der Kinderabzug setzt voraus, dass das Kind minderjährig ist, unter der elterlichen Sorge oder Obhut steht und für es ein Kinderabzug nach Art. 48 Abs. 1 lit. a StG SG beansprucht werden kann.
> 
> Quellen:
> - Art. 64 Abs. 1 StG SG (`sg-stg-2025__art-64`): Fr. 75'000 pro Steuerpflichtigen, Fr. 20'000 pro berechtigtem Kind. Abs. 2: Die Abzüge richten sich nach den Verhältnissen am Ende der Steuerperiode.
> - Wiki-Wert `vermoegen.freibetrag_verheiratet` = Fr. 150'000 (`sg-wl-2025__c0118`).
> 
> Status: Die Werte sind agent-geprüft (☑️), die Abnahme steht noch aus. Der Gesetzestext für 2025 ist durch 2026 ersetzt, deshalb habe ich die 2025-Fassung zitiert.
> 
> Die Sozialabzüge gelten nur für die Kantonssteuer (Vermögenssteuer). Beim Bund gibt es keine Vermögenssteuer, also keinen entsprechenden Abzug.

## q25

**Frage:** Welcher Verzugszins gilt 2026 für die direkte Bundessteuer?

**Soll (Referenz):** 4.00 % (RS 2-215, bund-rs-2-215__c0010/c0011).

**Antwort des Agenten** (21.9 s · Tools: 1 Aufrufe steuerwiki__wert):

> Für 2026 beträgt der Verzugs- und Rückerstattungszins der direkten Bundessteuer **4,00 %** (2025: 4,50 %).
> 
> Quelle: `bund-rs-2-215__c0010`, Verzugs- und Rückerstattungszins. Der Status ist ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> 
> Die Frage bezog sich auf den Bund, daher habe ich keinen Kanton angegeben. Für einen kantonalen Wert nennen Sie bitte den Kanton (AR, SG, TG oder ZH).

## q26

**Frage:** Wann wird der Eigenmietwert abgeschafft und gilt das schon für 2026?

**Soll (Referenz):** Abschaffung per 1.1.2029 (Bundesratsbeschluss 01.04.2026); für 2025–2028 gilt bisheriges Recht – 2026 also noch Eigenmietwert.

**Antwort des Agenten** (28.2 s · Tools: 4 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurz: Nein, für 2026 gilt die Abschaffung noch nicht. Der Eigenmietwert bleibt im Steuerjahr 2026 steuerbar.**
> 
> **Wann kommt die Abschaffung?**
> - Der Bundesrat hat am 1. April 2026 beschlossen, die Reform der Wohneigentumsbesteuerung auf den **1. Januar 2029** in Kraft zu setzen. Ab dann entfällt auf selbstgenutztem Wohneigentum die Besteuerung des Eigenmietwerts.
> - Gleichzeitig können die Kantone zur finanziellen Kompensation eine Objektsteuer auf Zweitliegenschaften einführen.
> - Quelle: Medienmitteilung Bundesrat, `bund-mm-eigenmietwert-abschaffung__c0002` (Status: ☑️ agent-geprüft, Abnahme offen).
> 
> **Was heisst das für 2026?**
> - Der Eigenmietwert ist für 2026 noch steuerbar. Der Bund behandelt die Liegenschaft also weiterhin wie bisher.
> - Für Liegenschaftskosten gilt beim Bund 2026 weiterhin die Pauschale nach Gebäudealter (Stand 1.1.2026):
>   - bis 10 Jahre alt: 10 % des Brutto-Eigenmietwerts
>   - älter als 10 Jahre: 20 % (Quelle: `bund-lkv__art-5`)
> - Bei Grenzfällen beim Baujahr oder Bezug sollte das Alter genau geprüft werden.
> 
> **Kantone:** Die Eigenmietwert-Bewertung und die kantonale Veranlagung legt der Kanton fest, und die Kantone müssen die Abschaffung in ihr Recht übernehmen. Für eine verlässliche Antwort für 2026 brauche ich den Kanton des Wohnsitzes am 31.12. Sag mir, welcher es ist (AR, SG, TG oder ZH), dann prüfe ich die kantonalen Werte.

## q27

**Frage:** Zitiere die Regel zum Abzug privater Schuldzinsen im DBG (Steuerjahr 2025) mit Artikel.

**Soll (Referenz):** Art. 33 Abs. 1 lit. a DBG (Fassung 2025): private Schuldzinsen im Umfang der steuerbaren Vermögenserträge (Art. 20, 20a, 21) und weiterer CHF 50'000.

**Antwort des Agenten** (25.8 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Art. 33 Abs. 1 lit. a DBG** (Steuerjahr 2025, Bund):
> 
> > «Von den Einkünften werden abgezogen: a. die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken. Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten oder ihr sonst wie nahe stehenden natürlichen Person zu Bedingungen gewährt, die erheblich von den im Geschäftsverkehr unter Dritten üblichen Bedingungen abweichen»
> 
> Fundstelle: `bund-dbg-2025__art-33-t1`. Die Chunk-Angabe nennt Gesetz, Steuerjahr 2025 und Gültigkeit bis 31.12.2025; einen Prüfstatus trägt er nicht.
> 
> Für die Praxis: Der Abzug ist auf die steuerbaren Vermögenserträge plus 50 000 Franken begrenzt. Der Ausschluss für Darlehen von Kapitalgesellschaften an nahe stehende Personen zu nicht marktüblichen Bedingungen gilt daneben. Die Verwaltungspraxis dazu steht in der KS W95-024 (Ziff. II.4–5, Chunk `bund-ks-w95-024__c0014`), die Fremdfinanzierung bei Darlehen aus Gesellschaften in der KS 22a (Ziff. 3.3, `bund-ks-22a__c0016`). Diese Chunks habe ich nur über die Suchtreffer gesehen, nicht im Wortlaut geöffnet.

## q28

**Frage:** Ist ein Leasingvertrag für das Privatauto steuerlich relevant? Was ist mit den Leasingraten?

**Soll (Referenz):** Leasingraten sind keine Schuldzinsen und grundsätzlich nicht abziehbar (Lebenshaltung); relevant nur für Fahrkosten-Begründung/Geschäftsauto, Vermögen (kein Eigentum).

**Antwort des Agenten** (31.5 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Kurz:** Ja, der Leasingvertrag ist steuerlich relevant, aber nur über die Zinsen und den beruflichen Anteil. Die Leasingraten selbst sind für ein privat genutzes Auto nicht abziehbar.
> 
> **Leasingraten bei privater Nutzung (Bund, Steuerjahr 2025)**
> - Leasingraten für privat genutzte Güter enthalten keine abzugsfähigen Zinsanteile. Die Kosten gelten als nicht abzugsfähige Lebenshaltungskosten (Art. 34 DBG).
> - Quelle: KS 22a, Ziff. 3.3 (`bund-ks-22a__c0015`), gilt für 2025, 2026 und 2027. Status: Fundstelle geprüft, Abnahme offen.
> 
> **Berufliche Nutzung**
> - Fährt die Person das Auto für den Arbeitsweg, zählen nur die Fahrkosten zwischen Wohn- und Arbeitsort. Die Abzugslimite steht in Art. 26 DBG und im Formular 9–14 (2025). Den genauen Betrag habe ich nicht geprüft; ich nenne ihn erst nach einer Abfrage mit dem Kanton.
> - Ob und wie viel Leasing für eine berufliche Nutzung abziehbar ist, konnte ich nicht belegen. Dafür bräuchte ich die Nutzungsanteile und den Kanton.
> 
> **Offene Punkte**
> - **Kanton:** Ich brauche den Wohnsitz am 31.12. (AR, SG, TG oder ZH), damit ich die kantonalen Limiten und das Formular prüfen kann.
> - **Steuerjahr:** Ich habe 2025 angenommen. Falls es 2026 sein soll, sag Bescheid.
> - **Leasingvertrag:** Ist das Auto vom Arbeitgeber geleast und privat mitbenutzt, gelten andere Regeln (Eigenverbrauch). Dann bräuchte ich die Angaben dazu.

## q29

**Frage:** Wie hoch ist der Kinderabzug im Kanton Bern 2025?

**Soll (Referenz):** Nicht im Wiki (nur Bund, AR, SG, TG, ZH).

**Antwort des Agenten** (20.0 s · Tools: 0 Aufrufe ):

> Im Steuer-Wiki ist der Kanton Bern nicht abgedeckt. Ich kann Ihnen deshalb keinen Kinderabzug für Bern 2025 nennen, und ich habe dafür keinen Wert aus einem anderen Kanton übernommen.
> 
> Abgedeckt sind der Bund sowie die Kantone Appenzell Ausserrhoden (AR), St. Gallen (SG), Thurgau (TG) und Zürich (ZH), jeweils für 2025 und 2026. Für einen dieser Kantone kann ich den Kinderabzug mit Fundstelle und Status nennen. Für den Berner Wert finden Sie die Angabe in der kantonalen Steuerverwaltung Bern oder im bernischen Steuergesetz.

## q30

**Frage:** Ehepaar TG 2025, beide angestellt (Nettolohn 80'000 und 30'000), pendelt mit ÖV-Abo (CHF 1'200 bzw. 900). Erstelle die Abzüge Berufskosten (Fahrkosten, Verpflegung ohne Kantine, Pauschale übrige) je Person für Kanton und Bund mit Fundstellen.

**Soll (Referenz):** TG 2025 je Person: Fahrkosten = ÖV-Abo effektiv (1'200 bzw. 900; Max. 6'000 Staat / 3'300 Bund); Verpflegung ohne Kantine 15/Tag, max. 3'200 (beide Ebenen); übrige Pauschale 3 %: P1 80'000 → 2'400, P2 30'000 → 900 → Minimum 2'000 (beide Ebenen, BKV TG § 4a / BKV Bund).

**Antwort des Agenten** (35.9 s · Tools: 9 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **TG 2025, Ehepaar, beide unselbständig.** Beträge in CHF pro Jahr. Kanton und Bund sind hier gleich, weil keine Obergrenze greift (Fahrkosten-Max. Kanton 6'000 / Bund 3'300; Pauschale-Sätze identisch).
> 
> | Position | Person 1 (Netto 80'000) | Person 2 (Netto 30'000) |
> |---|---|---|
> | Fahrkosten ÖV-Abo | 1'200 | 900 |
> | Verpflegung (ohne Kantine) | max. 3'200 (siehe Hinweis) | max. 3'200 (siehe Hinweis) |
> | Pauschale übrige Berufskosten | 2'400 | 2'000 (Minimum) |
> | **Summe** | **6'800** | **6'100** |
> | Formularziffer | 10.1 (Form. 4.2, Code 240) | 10.2 (Form. 4.3, Code 280) |
> 
> **Rechnung**
> - Fahrkosten: Kanton `min(Ziff. 2.4; 6'000)`, Bund `min(…; 3'300)`. Beide Fälle liegen unter dem Max.
> - Pauschale: 3 % des Nettolohns, min. 2'000, max. 4'000. P1: 3 % × 80'000 = 2'400. P2: 3 % × 30'000 = 900, daher auf 2'000 angehoben.
> - Verpflegung: 15 CHF pro auswärtige Hauptmahlzeit, max. 3'200 pro Jahr. Die Obergrenze erreichen Sie ab 214 Mahlzeiten (3'200 / 15 = 213,3). Ohne Kantine und ohne Verbilligung ist der volle Satz anzusetzen, nicht der halbe (7.50/Tag).
> 
> **Offene Punkte**
> 1. **Verpflegung:** Ich kenne die Arbeitstage nicht. Die Summen oben setzen je Person den Höchstbetrag 3'200 voraus. Bei weniger Mahlzeiten gilt 15 × Anzahl Hauptmahlzeiten, z.B. 200 Tage × 15 = 3'000. Bitte die Tage je Person angeben, dann rechne ich genau nach.
> 2. **Nettolohn:** Ich setze voraus, dass die Werte 80'000 und 30'000 der Lohnausweis-Ziffer 11 entsprechen.
> 3. **Pensum:** Ich setze 100 % voraus. Bei Teilzeit kürzt die Verpflegung nach Beschäftigungsgrad, die Pauschale nach Dauer.
> 4. **Arbeitgeber-Kosten:** Ist das ÖV-Abo vom Arbeitgeber bezahlt, entfällt der Fahrkostenabzug (Lohnausweis Feld F). Ein Verpflegungs-Zuschuss halbiert die Verpflegung.
> 
> **Fundstellen**
> - Fahrkosten TG: `tg-stg__par-29` «bis zu einem Maximalbetrag von Fr. 6'000», ÖV-Abo als Normalfall in `tg-bkv__par-1`. Status ☑️ agent-geprüft.
> - Fahrkosten Bund: `bund-dbg-2025__art-26` (3'300) und `bund-bkv-2025__anhang-1`. Die ESTV-Wegleitung 2a nennt noch 3'200. Der Widerspruch ist hier nicht entscheidend, weil die Abzüge darunter liegen.
> - Verpflegung TG: `tg-bkv__par-2-t1` (15 pro Hauptmahlzeit, 3'200 pro Jahr), `tg-bkv__par-2-t2` (halber Abzug 7.50/1'600 bei Kantine oder Verbilligung). Bund: `bund-bkv-2025__anhang-1`.
> - Pauschale übrige TG: `tg-bkv__par-4a` (3 %, min. 2'000, max. 4'000). Bund: `bund-bkv-2025__anhang-1`.
> - Formular: `tg-form-01-2025__c0010` (Ziff. 10.1 und 10.2), `tg-wl-2025__c0196`.
> 
> Alle Ansätze sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Abnahme bleibt bei der Fachperson.

## q31

**Frage:** Ehepaar ZH 2026, beide erwerbstätig, Kind 3 Jahre in der Kita (Kosten CHF 30'000). Wie viel Drittbetreuung ist abziehbar (Kanton und Bund)?

**Soll (Referenz):** ZH 2026 Kanton max. CHF 25'300 pro Kind (zh-stg-2026__par-31-t3); Bund 2026 max. CHF 25'800 (bund-dbg-2026__art-33-t7). Abzug je Ebene getrennt.

**Antwort des Agenten** (25.8 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Ergebnis für ZH 2026, Ehepaar, beide erwerbstätig, Kind 3 Jahre, Kita CHF 30'000:**
> 
> | | Höchstbetrag pro Kind | Abzug bei CHF 30'000 Kosten |
> |---|---|---|
> | **Kanton ZH (Staatssteuer)** | CHF 25'300 | **CHF 25'300** |
> | **Bund (direkte Bundessteuer)** | CHF 25'800 | **CHF 25'800** |
> 
> Der Abzug ist auf den Höchstbetrag begrenzt, die CHF 4'700 (Kanton) bzw. CHF 4'200 (Bund) darüber sind nicht abziehbar.
> 
> **Voraussetzungen, die erfüllt sind:**
> - Kind unter 14 Jahren (Altersgrenze 14, Kanton und Bund).
> - Kind lebt im gleichen Haushalt wie die für den Unterhalt sorgende Person.
> - Die Kosten hängen mit der Erwerbstätigkeit zusammen; beide Ehegatten sind erwerbstätig.
> 
> **Zu beachten:**
> - **Nachweis:** Kita-Rechnungen und Zahlungsnachweise beilegen. Bei angestellter Betreuungsperson zusätzlich eine Aufstellung mit den Empfängern und ggf. Lohnausweis. Hier ist die Kita der Empfänger, eine Aufstellung reicht also in der Regel.
> - **Nur Arbeitszeit:** Abziehbar sind nur Kosten während der Arbeits- bzw. Ausbildungszeit. Kosten für Ferien- oder Zusatzbetreuung, die nicht der Erwerbstätigkeit dienen, sind nicht abziehbar.
> - **20%-Kürzung:** Nur bei pauschal ausgewiesenen Betreuungskosten werden 20 % als Lebenshaltungskosten gekürzt. Bei Kita-Rechnungen mit Einzelnachweis entfällt das.
> - **Formularziffer ZH:** Ziff. 16.6 «Abzug für fremdbetreute Kinder» (Code 376). Das Formular ist für 2026 noch nicht vollständig publiziert; die Zuordnung stützt sich auf die Fassung für unterjährige Steuerpflicht. Ziffer und Code am regulären Formular vor dem Ausfüllen prüfen.
> - **Kind-Ziffer:** Das Kind muss auf Seite 1 (Ziff. S. 1) erfasst sein, sonst greift der Abzug nicht.
> 
> **Quellen und Status:** Kanton CHF 25'300 (zh-stg-2026__par-31-t3; zh-wl-2026-uj__c0105) und Bund CHF 25'800 (bund-dbg-2026__art-33-t7). Beide Werte sind agent-geprüft (☑️), die Abnahme durch die Fachperson ist noch offen.

## q32

**Frage:** SG 2025: Einfamilienhaus (Baujahr 2010), selbst bewohnt. Pauschalabzug Liegenschaftsunterhalt Kanton und Bund?

**Soll (Referenz):** SG 2025: 20 % des Eigenmietwerts, ohne Altersstaffel (sg-stv__art-29); Bund: Gebäude zu Beginn 2025 über 10 Jahre alt → 20 % (bund-lkv__art-5).

**Antwort des Agenten** (25.7 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kurz:** Ja, beide haben einen Pauschalabzug, aber die Sätze unterscheiden sich.
> 
> **Kanton St. Gallen 2025: 20 %**
> - Der Satz ist 20 % unabhängig vom Gebäudealter. Ein Baujahr 2010 spielt im Kanton keine Rolle.
> - Bemessungsgrundlage ist der angerechnete Eigenmietwert bzw. der Bruttomietertrag ohne Nebenkosten. Beim Eigenmietwert ist also der nach der 30-%-Herabsetzung angerechnete Betrag gemeint (Art. 34 StG SG). Das ist aus der Fundstelle nicht ganz eindeutig; vor der Abgabe prüfen.
> - Die Pauschale ist eine Wahl pro Periode und Liegenschaft: Entweder Pauschale oder effektive Kosten.
> - Quelle: sg-stv__art-29 (Fundstelle geprüft, Abnahme offen ☑️).
> 
> **Bund 2025: 20 %**
> - Massgebend ist das Gebäudealter am 1.1.2025. Bei Baujahr 2010 ist das Gebäude etwa 15 Jahre alt, also über zehn Jahre. Es gilt daher der Satz von 20 % (bis zehn Jahre wären 10 %).
> - Bemessungsgrundlage ist der Brutto-Eigenmietwert. Beim Bund gibt es keine 30-%-Herabsetzung.
> - Quelle: bund-lkv__art-5 (☑️ agent-geprüft, Abnahme offen).
> 
> **Ergebnis für dieses Haus:** Kanton 20 % und Bund 20 %, jeweils auf den eigenen Bemessungsgrundlagen, separat deklariert. Die Pauschale ersetzt die effektiven Unterhaltskosten. Wenn diese höher sind, kann sich der Einzelnachweis lohnen.
> 
> **Offen:** Die Eigenmietwerte für Kanton und Bund brauche ich für eine Betragsrechnung. Die Werte stammen aus dem kantonalen Eigenmietwert-Verfahren und sind nicht im Wiki enthalten. Wenn du sie mir gibst, rechne ich die Abzüge aus. Das Formular ist SG 2025 Ziff. 15, Code 716 (Unterhalts- und Verwaltungskosten für Liegenschaften).

## q33

**Frage:** ZH 2025: Kind 19 Jahre, in Lehre (Ausbildung). Kinderabzug Kanton und Bund?

**Soll (Referenz):** ZH 2025 Kanton CHF 9'300 (volljährig in Erstausbildung, zh-stg-2025__par-34); Bund CHF 6'800 (bund-dbg-2025__art-35) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (27.6 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Kinderabzug für das 19-jährige Kind in Lehre, Steuerjahr 2025**
> 
> | | Kanton ZH (Staats-/Gemeindesteuer) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | Kinderabzug vom Einkommen | **CHF 9'300** | **CHF 6'800** |
> | Zusätzlicher Versicherungsabzug | CHF 1'300 | CHF 700 |
> | Ermässigung des Steuerbetrags | nicht anwendbar | **CHF 263** |
> 
> - **ZH:** § 34 Abs. 1 lit. a StG, Chunk `zh-stg-2025__par-34` (☑️ agent-geprüft, Abnahme offen). Versicherungsabzug: `zh-stg-2025__par-31-t2`.
> - **Bund:** Art. 35 Abs. 1 lit. a DBG, Chunk `bund-dbg-2025__art-35` (☑️). Steuerbetrag-Ermässigung: Art. 36 Abs. 2bis DBG, Chunk `bund-dbg-2025__art-36-t4` (☑️). Versicherungszuschlag: `bund-dbg-2025__art-33-t5`.
> 
> **Voraussetzungen für den Abzug bei einem volljährigen Kind in Lehre (ZH, ZStB 34.1, Rz 9–12):**
> 1. **Berufliche Erstausbildung mit Lehrvertrag.** Eine Anstellung gilt nur dann als Ausbildung, wenn ein Lehrvertrag besteht.
> 2. **Unterhalt zur Hauptsache durch Sie.** Die Eltern müssen den Unterhalt überwiegend tragen.
> 3. **Angewiesenheit.** Das Kind muss auf die Unterstützung angewiesen sein. Das ist nicht der Fall, wenn es selbst für seinen Unterhalt aufkommen kann, etwa durch den Lehrlingslohn.
> 4. **Unterbrüche** sind nur in engen Grenzen unschädlich (Militär-/Zivildienst, ergänzende halbtägige Schule, konsequente Prüfungsvorbereitung).
> 
> Der Bund kennt keine Unterscheidung nach Alter oder Ausbildungsart. Für das volljährige Kind in Ausbildung gilt dort derselbe Betrag wie für Minderjährige.
> 
> **Offene Punkte:**
> - Ob die Angewiesenheit gegeben ist, hängt vom Lehrlingslohn und den übrigen Einkünften des Kindes ab. Das muss im Einzelfall beurteilt werden und ist nicht allein mit dem Wiki zu klären.
> - Ob der Kinderabzug in Ihrem Fall tatsächlich zusteht, ist die Entscheidung der Fachperson.
> - Die Zeile im ZH-Formular ist Ziff. 24.1 (Code 370 für Kinder im Haushalt, Code 372 für Kinder ausserhalb). Die genaue Regel dazu liefert `position zh 2025 24.1`, falls Sie das Ausfüllen brauchen.

## q34

**Frage:** ZH 2025: Lohnausweis Feld G angekreuzt (Kantine). Welche Verpflegungspauschale gilt und in welche Ziffer des Berufsauslagenformulars?

**Soll (Referenz):** Verbilligte Verpflegung: CHF 7.50 pro Arbeitstag, max. CHF 1'600 pro Jahr (LS 631.33, zh-pauschalierung-berufsauslagen-2025__c0004); Form. 360 Ziff. 2.1 (verbilligt); Bund gleich.

**Antwort des Agenten** (25.4 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__beleg, steuerwiki__wert):

> **Verpflegungspauschale: CHF 7.50 pro Arbeitstag, höchstens CHF 1'600 pro Jahr** (verbilligte Verpflegung, Lohnausweis Feld G). Eintragen unter **Form. 360 (Hilfsblatt Berufskosten), Ziff. 2.1 verbilligt, Code 206** (Person 2: Code 226).
> 
> - **Berechnung:** min(Arbeitstage × 7.50; 1'600). Beispiel: 220 Arbeitstage ergeben 1'650, gedeckelt auf 1'600. Der Deckel greift ab 214 Arbeitstagen.
> - **Arbeitstage:** aus dem Arbeitszeitnachweis, bei ständiger auswärtiger Verpflegung.
> - **Bedingung:** Der Abzug gilt nur, wenn die Arbeitspause die Heimkehr nicht erlaubt und trotzdem Mehrkosten entstehen. Nicht kombinierbar mit Ziff. 2.1 voll, Ziff. 2.2 (Schicht) oder Mittagsheimfahrt; bei Mittagsheimfahrt entfällt der Verpflegungsabzug.
> - **Kanton und Bund:** Beide Spalten (Staats- und Bundessteuer) tragen 7.50 bzw. 1'600 ein. Der Bund halbiert den Abzug bei Verbilligung; die Kantine ist kein Sonderfall, der davon abweicht.
> - **Ohne Feld G** (Verpflegung voll zulasten der Arbeitnehmenden) gilt stattdessen Ziff. 2.1 voll, Code 208: CHF 15 pro Tag, max. CHF 3'200.
> 
> **Quellen:** Form. 360 Ziff. 2.1 (zh-form-360-2025__c0003), Pauschalierung Berufsauslagen ZH 2025 (zh-pauschalierung-berufsauslagen-2025__c0004), Bund BKV 2025 Anhang 1. Status: agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Fachabnahme bleibt bei der Fachperson.

## q35

**Frage:** SG 2025: Kapitalbezug Säule 3a CHF 100'000. Wird das mit dem übrigen Einkommen besteuert? Wo deklarieren?

**Soll (Referenz):** Nein – Kapitalleistungen aus Vorsorge werden getrennt vom übrigen Einkommen (separate Jahressteuer) besteuert; SG Formular 1 Ziff. 40.1 (Säule 3a), Total Ziff. 41.

**Antwort des Agenten** (27.5 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__position):

> **Kurz:** Nein, die CHF 100'000 werden nicht mit dem übrigen Einkommen versteuert. Kapitalleistungen aus Säule 3a werden gesondert besteuert, mit einer separaten Jahressteuer. Sie erhöhen also nicht den Satz auf Ihr übriges Einkommen. Der Betrag muss aber in der Steuererklärung 2025 angegeben werden.
> 
> **Wo deklarieren (SG 2025, Formular 1):**
> - **Ziff. 40.1**, Kapitalleistungen aus Vorsorge, «aus gebundener Vorsorge Säule 3a». Der Betrag ist die 2025 erhaltene Kapitalauszahlung. Bei mehreren Auszahlungen wird der Gesamtbetrag eingetragen.
> - **Beilage:** Bescheinigung der Bank oder Versicherung über die Kapitalleistung.
> - Die Angabe ist nur zu Informationszwecken. Sie gehört **nicht** in Ziff. 6.4.
> 
> **Steuerbetrag (Richtwert, nicht abschliessend geprüft):**
> - **Kanton:** einfache Steuer von 2,0 % (Ehegatten) bzw. 2,2 % (übrige). Bei CHF 100'000 ergibt das CHF 2'000 bzw. CHF 2'200, jeweils vor Steuerfuss und ohne allgemeine oder Sozialabzüge.
> - **Bund:** ein Fünftel der Tarife nach Art. 36 DBG, ebenfalls ohne Sozialabzüge. Den genauen Betrag habe ich nicht berechnet, weil ich die Bundestarifwerte nicht abgefragt habe. Im Formular gibt es für den Bund keine eigene Spalte, die Steuerbehörde nimmt die Anpassung automatisch vor.
> 
> **Offene Punkte:**
> - Ob Sie verheiratet sind, entscheidet über den Satz (2,0 % oder 2,2 %). Das wirkt sich auf den Kantonsbetrag aus.
> - Die Zahlen sind agent-geprüft (Fundstelle geprüft, Abnahme offen). Vor dem Einreichen bitte mit der Fachperson abgleichen.
> 
> Quellen: `sg-form-1-2025__c0014` (Ziff. 40.1), `sg-wl-2025__c0119` (gesonderte Besteuerung), Position «Kapitalleistungen Säule 3a» SG 2025.

## q36

**Frage:** ZH 2025: Geschiedener Mandant zahlt Unterhaltsbeiträge an die Ex-Frau (CHF 24'000) und für das minderjährige Kind (CHF 12'000). Was ist abziehbar, in welcher Ziffer?

**Soll (Referenz):** Ex-Ehefrau CHF 24'000 voll abziehbar, Ziff. 13.1 (Code 254); Kinderalimente CHF 12'000 abziehbar bis und mit Monat der Volljährigkeit, Ziff. 13.2 (Code 255); Empfänger versteuert; Bund gleich (Art. 33 Abs. 1 lit. c DBG).

**Antwort des Agenten** (27.5 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__suche):

> **Ergebnis (ZH 2025, Kanton und Bund gleich):**
> 
> | Betrag | Ziffer | Code | Abzug |
> |---|---|---|---|
> | CHF 24'000 an die geschiedene Ehefrau | **13.1** Unterhaltsbeiträge an geschiedenen/getrennt lebenden Ehegatten | 254 | voll abziehbar, CHF 24'000 |
> | CHF 12'000 für das minderjährige Kind | **13.2** Unterhaltsbeiträge für minderjährige Kinder | 255 | abziehbar, CHF 12'000 |
> 
> Total Abzug: CHF 36'000 (Kanton = Bund).
> 
> **Bedingungen und Hinweise:**
> - **Ziff. 13.1:** Abziehbar sind die für die Ehefrau persönlich bestimmten periodischen Beiträge, die 2025 effektiv bezahlt wurden. Kapitalabfindungen sind nicht abziehbar, Naturalleistungen wie Miete oder Krankenkassenprämien dagegen gleichgestellt. Die Ehefrau versteuert die Beiträge in Ziff. 5.1 (Korrespondenzprinzip).
> - **Ziff. 13.2:** Abziehbar sind die effektiv bezahlten Kinderalimente bis und mit dem Monat, in dem das Kind 18 wird. Spätere Zahlungen sind nicht abziehbar. Ist das Kind 2025 durchgehend minderjährig, ist der volle Betrag abziehbar. Das Geburtsdatum des Kindes sollte trotzdem geprüft werden.
> - **Kinderabzug:** Wer Alimente für ein minderjähriges Kind leistet, erhält für dieses Kind keinen Kinderabzug (Ziff. 24.1).
> - **Bund:** Abziehbar sind nur familienrechtlich geschuldete, effektiv bezahlte Alimente; freiwillige Zahlungen fallen nicht darunter. Sind die 12'000 gerichtlich oder vertraglich festgelegt, ist das gegeben.
> - **Belege:** Die Wegleitung verlangt keine Beilage. Einzureichen sind Zahlungsnachweise und das Scheidungsurteil bzw. die Konvention nur auf Verlangen. Im Zweifel beilegen.
> 
> **Fundstellen:** Ziff. 13.1 zh-form-300-2025__c0007 / zh-wl-2025__c0075; Ziff. 13.2 zh-form-300-2025__c0007 / zh-wl-2025__c0076.
> 
> **Status:** ☑️ agent-geprüft: Fundstelle geprüft, Abnahme durch Fachperson offen. Die fachliche Beurteilung bleibt bei der Fachperson.

## q37

**Frage:** TG 2025: Mandant bringt Steuerberatungsrechnung, Kreditkartenabrechnung, Mietvertrag und Motorfahrzeugversicherung. Was davon ist relevant?

**Soll (Referenz):** Steuerberatungsrechnung: nein; Motorfahrzeugversicherung: nein; Kreditkartenabrechnung: bedingt (nur als Nachweis/Schuld per 31.12.); Mietvertrag: bedingt (Wochenaufenthalt/Arbeitszimmer/Adressnachweis) – laut belege-relevanz.

**Antwort des Agenten** (35.6 s · Tools: 7 Aufrufe steuerwiki__ablage, read, steuerwiki__zeige):

> **TG 2025: Relevanz der vier Dokumente**
> 
> | Dokument | Steuerrelevant? | Ablage (Kategorie) |
> |---|---|---|
> | Steuerberatungsrechnung | **Nein** | Keine Steuerbeleg-Kategorie |
> | Kreditkartenabrechnung | **Bedingt** | Belege Sonstiges oder Belege eingereicht, je nach Abzug |
> | Mietvertrag | **Bedingt** | Nur bei Ausnahme relevant (s. unten) |
> | Motorfahrzeugversicherung | **Nein** (als Dokument) | Keine Steuerbeleg-Kategorie |
> 
> **1. Steuerberatungsrechnung: nicht relevant.** Kosten für Steuerberatung und das Ausfüllen der Steuererklärung im Privatvermögen sind nicht abziehbar. Quelle: `bund-wl-2a-2025__c0057` (Bundesrecht, Wegleitung). Ich habe nur die Bundesfundstelle geprüft, nicht die TG-Wegleitung. Ablage: kein Steuerbeleg, Grund nennen.
> 
> **2. Kreditkartenabrechnung: bedingt.** Die Abrechnung selbst ist kein Abzugsbeleg. Sie ist nur Nachweis für einzelne abziehbare Zahlungen, etwa Spenden, Krankheitskosten, Weiterbildung oder Berufsauslagen, falls die Originalrechnung fehlt. Die Position ist TG 2025 Form. 4.1 A.
> - Wenn sie einen Abzug belegt, gehört sie zu **Belege Sonstiges** (Eingereicht = nein), sofern die TG-Wegleitung sie nicht zur Einreichung verlangt.
> - Die Einreichpflicht im Kanton ist nicht eindeutig geklärt. Prüfen Sie diesen Punkt vor der Ablage.
> 
> **3. Mietvertrag: bedingt.** Der Mietzins einer selbstbewohnten Wohnung ist Lebenshaltungsaufwand und nicht abziehbar (Art. 34 lit. a DBG). Relevant wird er nur in diesen Fällen:
> - **Untervermietung:** Der Nettoertrag ist steuerbar.
> - **Wochenaufenthalt am Arbeitsort:** Die Mehrkosten sind nach TG-Wegleitung Form. 4.2 abziehbar (`tg-wl-2025__c0189`). Dabei wird der Jahresmietzins durch (Zimmerzahl + 1) geteilt, bei Wohnungen bis 3½ Zimmer.
> - Ohne einen dieser Fälle ist das Dokument nicht relevant. Mit einem solchen Fall gehört es zu Belege Sonstiges oder Belege eingereicht, je nach Einreichepflicht im Kanton. Die ist hier ebenfalls unklar.
> 
> **4. Motorfahrzeugversicherung: nicht relevant als Dokument.** Das Auto ist im Vermögen zum Verkehrswert per 31.12.2025 zu deklarieren (`tg-wl-2025__c0123`, Ziffer 30.4). Den Wert setzen Sie selbst an, Versicherungsprämien gehen nicht ein. Laut Wiki sind Prämien, Verkehrssteuern und Unterhalt privater Fahrzeuge nicht abziehbar. Diese Aussage stammt aus der Bundes-Fundstelle des Wiki-Tools, die TG-Fundstelle habe ich nicht gesondert geprüft. Die Police kann als Nachweis für Fahrzeugtyp und Kaufjahr dienen, muss aber nicht abgelegt werden.
> 
> **Hinweis zur Kategorienliste:** Die Zuordnungen in `KATEGORIEN.md` sind laut Datei noch nicht vom Hersteller bestätigt. Das gilt auch für die Regeln zu «bedingt» und zum Mietvertrag, die die Liste nicht ausdrücklich nennt.

## q38

**Frage:** AR 2026: Wie hoch ist der Kinderabzug für ein 10-jähriges Kind? Ist der Wert gesichert?

**Soll (Referenz):** AR 2026: CHF 7'400 laut Anhang 1 StG (indexiert), aber Status STRITTIG (MB 02 / StG-Text nennen andere Beträge; Wegleitung 2026 fehlt) → Fachperson.

**Antwort des Agenten** (26.0 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Kinderabzug AR 2026 für ein 10-jähriges Kind: CHF 7'400** (Kanton Appenzell Ausserrhoden, Sozialabzug, Formular Ziff. 23.2).
> 
> **Wert ist nicht gesichert.** Er ist als ⚠️ strittig markiert, weil die Quellen widersprechen:
> 
> - **Anhang 1 StG AR** und **Wegleitung 2025** nennen 7'400 (indexiert per 1.1.2024). Die Wegleitung 2025 bestätigt den Wert für 2025 (`ar-wl-2025__c0005`).
> - **Gesetzestext Art. 38 und Merkblatt MB 02** nennen 7'000. Das ist der nicht indexierte Gesetzestext.
> - **Wegleitung und Formular AR 2026** sind noch nicht publiziert (Stand 09.11.2026). Der Wert 7'400 für 2026 ist also aus dem Anhang übernommen, nicht in einer Quelle für 2026 bestätigt.
> 
> Für die Abnahme sollte die Fachperson die AR-Wegleitung 2026 abwarten oder bei der Steuerverwaltung AR nachfragen.
> 
> **Zum Vergleich, Bund 2026** (getrennt zu deklarieren): CHF 6'800 Sozialabzug für jedes minderjährige Kind (Art. 35 Abs. 1 lit. a DBG, Status ☑️ agent-geprüft). Beim Bund gibt es keine Staffelung nach Alter. Zusätzlich gibt es einen Steuerbetrag-Abzug von CHF 263 pro Kind (Art. 36 DBG).
> 
> **Weitere kindbezogene AR-Werte** (zur Orientierung, ebenfalls ☑️ agent-geprüft):
> - Versicherungsabzug-Zuschlag: CHF 1'000 pro Kind (Art. 35 StG).
> - Vermögensfreibetrag: CHF 25'000 pro minderjähriges Kind (Art. 51 StG).
> 
> Die Altersstaffelung für AR lautet: 5'300 bis zum 4. Altersjahr, 7'400 vom 4. bis zum 15. Altersjahr, 11'600 ab dem 15. Altersjahr bis zur Volljährigkeit (und in Ausbildung bis 26).

## q39

**Frage:** Welche Vermögenssteuer-Freibeträge (Sozialabzüge) gelten 2025 in ZH für Alleinstehende und Verheiratete?

**Soll (Referenz):** ZH kennt keine Vermögens-Sozialabzüge, sondern Tarifstufen mit 0 ‰: Grundtarif erste CHF 80'000, Verheiratetentarif erste CHF 159'000 (zh-stg-2025__par-47); kein Betrag pro Kind.

**Antwort des Agenten** (23.9 s · Tools: 4 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> Im Kanton Zürich gibt es für die Vermögenssteuer 2025 keinen eigenen Sozialabzug. Der steuerfreie Betrag ergibt sich aus der 0‰-Stufe des Tarifs in § 47 StG ZH:
> 
> **Kanton Zürich, Steuerjahr 2025 (Staats- und Gemeindesteuer)**
> 
> | Steuerpflichtige | Steuerfrei (0‰-Stufe) | Tarif |
> |---|---|---|
> | Alleinstehend (Grundtarif) | **CHF 80'000** | § 47 Abs. 1 StG ZH |
> | Verheiratet (Verheiratetentarif) | **CHF 159'000** | § 47 Abs. 2 StG ZH |
> 
> - **Verheiratetentarif** gilt für in ungetrennter Ehe lebende Ehegatten sowie für Verwitwete, getrennt lebende, Geschiedene und Ledige, die mit Kindern zusammenleben.
> - **Kinder:** Beim Vermögen gibt es keinen Abzug pro Kind. Kinder wirken nur über die Wahl des Verheiratetentarifs.
> 
> **Bund:** Die direkte Bundessteuer kennt keine Vermögenssteuer, daher gibt es dort keinen entsprechenden Freibetrag.
> 
> **Status:** Die Beträge stammen aus den Chunks `zh-stg-2025__par-47-t1` und `zh-stg-2025__par-47-t2` und sind im Wiki als ☑️ agent-geprüft markiert (Fundstelle geprüft, Abnahme offen). Ich habe den Gesetzestext direkt gegen die Werte gelesen, sie stimmen überein. Die Fachperson sollte die Abnahme noch bestätigen.

## q40

**Frage:** Alleinstehende TG 2026, Nettolohn 90'000, ÖV-Abo 2'400, Säule 3a 7'258, Krankenkasse 5'500. Erstelle die Abzüge (Berufskosten, 3a, Versicherungsabzug) Kanton und Bund mit Fundstellen und Status.

**Soll (Referenz):** TG 2026 (Kanton/Bund): Fahrkosten 2'400 (Max. 6'000 / 3'300); übrige Berufskosten 3 % von 90'000 = 2'700 (Min. 2'000, Max. 4'000, beide Ebenen); Säule 3a 7'258 (TG 🟡 extrahiert, Bund ☑️); Versicherungsabzug TG max. 3'500 → 3'500, Bund max. 1'800 → 1'800 (Prämien 5'500 übersteigen beide Maxima).

**Antwort des Agenten** (39.8 s · Tools: 11 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Abzüge Alleinstehende, TG 2026, Nettolohn CHF 90'000**
> 
> Kanton (Staats- und Gemeindesteuer) und Bund (direkte Bundessteuer) werden getrennt berechnet.
> 
> | Abzug | Eingabe | Kanton TG | Bund |
> |---|---|---|---|
> | **Berufskosten: Fahrkosten ÖV** (Ziff. 2.5) | 2'400 | **2'400** (Max. 6'000) | **2'400** (Max. 3'300) |
> | **Berufskosten: Pauschale übrige** (Ziff. 4, 3 % Nettolohn, min. 2'000 / max. 4'000) | 3 % × 90'000 = 2'700 | **2'700** | **2'700** |
> | **Berufskosten total** (Ziff. 7 bzw. Form. 4.2 Code 240) | | **5'100** | **5'100** |
> | **Säule 3a** (Ziff. 13.1, Code 314) | 7'258 | **7'258** (Max. 7'258) | **7'258** (Max. 7'258) |
> | **Versicherungsprämien** (Ziff. 14, Code 330) | 5'500 | **3'500** (Max. Alleinstehend) | **1'800** (Max. Alleinstehend mit 2./3a-Beiträgen) |
> 
> **Fundstellen und Status**
> 
> - **Fahrkosten TG:** Max. CHF 6'000, `tg-wl-2026__c0176`, ☑️ agent-geprüft (Abnahme offen).
> - **Fahrkosten Bund:** Max. CHF 3'300, `bund-dbg-2026__art-26`, ☑️ agent-geprüft (Abnahme offen).
> - **Pauschale übrige Berufskosten TG:** 3 % des Nettolohns, min. 2'000, max. 4'000, `tg-bkv__par-4a`, ☑️ agent-geprüft (Abnahme offen).
> - **Pauschale übrige Berufskosten Bund:** 3 % des Nettolohns, min. 2'000, max. 4'000, `bund-rs-2-215__c0006` und `bund-bkv-2026__anhang-1`, ☑️ agent-geprüft (Abnahme offen).
> - **Säule 3a TG:** Max. 7'258 für Erwerbstätige mit 2. Säule, `tg-wl-2026__c0089`, ☑️ agent-geprüft (Abnahme offen).
> - **Säule 3a Bund:** Max. 7'258, `bund-bsv-masszahlen-2025-2026__c0003`, ☑️ agent-geprüft (Abnahme offen).
> - **Versicherung TG:** Alleinstehend max. 3'500, `tg-stg__par-34-t3`, ☑️ agent-geprüft (Abnahme offen).
> - **Versicherung Bund:** Alleinstehend mit Beiträgen an 2. Säule oder 3a max. 1'800, `bund-dbg-2026__art-33-t2`, ☑️ agent-geprüft (Abnahme offen).
> 
> **Hinweise**
> 
> - **Versicherung:** Die 5'500 Krankenkasse übersteigen beide Maxima. Die Limite gilt für Prämien und Sparzinsen zusammen. Die Kasse wird nur netto (nach Prämienverbilligung) abgezogen, also bitte die Nettoprämie aus der Jahresbestätigung prüfen. Falls Sie Prämienverbilligung erhalten, sinkt der Betrag, der Abzug bleibt aber am Maximum, solange die Nettoprämie darüber liegt.
> - **Säule 3a:** Der Maximalbetrag gilt ohne Rücksicht auf eine 2. Säule. Ohne 2. Säule wären 20 % von 90'000 = 18'000, gedeckelt auf 36'288, also bleibt 7'258 zulässig. Bitte die Einzahlung mit Bescheinigung belegen.
> - **Fahrkosten:** Der ÖV-Abzug liegt unter beiden Maxima. Ein Privatauto wäre nur bei unzumutbarem ÖV abziehbar, wird hier nicht angesetzt.
> - **Verpflegung:** Nicht angesetzt, da keine Angabe dazu vorliegt.
> - **Einkauf 3a:** Nicht angesetzt, da keine Angabe dazu vorliegt.
> - **Gesamtstatus:** Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme durch die Fachperson offen). Es sind keine ⚠️ strittigen Werte dabei.

