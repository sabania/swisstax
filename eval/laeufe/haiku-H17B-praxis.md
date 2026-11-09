# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 40 · Lauf: 2026-11-09 18:36
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q01

**Frage:** Mandantin (ZH, 2025) bringt: Lohnausweis, Krankenkassen-Prämienrechnung, Handyrechnung, 3a-Bescheinigung, Hausratversicherungspolice, Spendenquittung Rotes Kreuz CHF 80, Kita-Rechnungen. Welche sind relevant, wofür?

**Soll (Referenz):** Relevant: Lohnausweis (Einkünfte 1.1), Krankenkassenprämien (Versicherungsabzug Ziff. 15, Form. 365), 3a-Bescheinigung (Ziff. 14), Kita-Rechnungen (Ziff. 16.6 Drittbetreuung, max. 25'000 Kanton / 25'800 Bund). Spende CHF 80: unter Mindestbetrag 100 → nicht abziehbar (sofern Total < 100). Nicht relevant: Handyrechnung (Lebenshaltung), Hausratversicherung (kein Versicherungsabzug).

**Antwort des Agenten** (36.6 s · Tools: 10 Aufrufe read, steuerwiki__ablage, steuerwiki__suche, steuerwiki__wert):

> Ich ordne die sieben Dokumente für Zürich 2025 ein und lese dazu die Kategorienliste.
> 
> Die Handyrechnung wurde nicht erkannt, und bei der Spende ist die Schwelle wichtig. Ich prüfe beides nach.
> 
> **ZH · 2025**
> 
> | Dokument | Steuerrelevant? | Wofür | Kategorie (KATEGORIEN.md) | Eingereicht? |
> |---|---|---|---|---|
> | **Lohnausweis** | ja | Einkommen (Ziff. 1.1/1.2, Form. 360, Form. 367) | Belege eingereicht | ja |
> | **3a-Bescheinigung** | ja | Säule-3a-Abzug (Ziff. 14.1/14.2) | Belege eingereicht | ja |
> | **Krankenkassen-Prämienrechnung** | ja | Abzug Versicherungsprämien (Ziff. 15, Form. 365 Teil A Ziff. 1–4 und 6) | Belege Sonstiges | nein (Prämienbescheinigung nur auf Verlangen) |
> | **Kita-Rechnungen** | bedingt | Kinderbetreuungskosten (Ziff. 16.6), max. CHF 25'000 pro Kind (§ 31 StG) | Belege Sonstiges | nein (Rechnungen auf Verlangen) |
> | **Spendenquittung Rotes Kreuz CHF 80** | bedingt | Gemeinnützige Zuwendungen (Ziff. 22.2) | Belege Sonstiges, falls das Jahrestotal reicht | nein |
> | **Handyrechnung** | nein | Private Telefonkosten sind Lebenshaltungskosten, nicht abziehbar | keine Steuerbeleg-Kategorie | – |
> | **Hausratversicherungspolice** | nein | Mobiliar- und Haftpflichtprämien sind nicht abziehbar | keine Steuerbeleg-Kategorie | – |
> 
> **Wichtige Punkte:**
> 
> - **Spende:** Zuwendungen an gemeinnützige Organisationen sind erst ab CHF 100 pro Steuerperiode abziehbar (§ 32 StG, Fundstelle zh-stg-2025__par-32). Die CHF 80 allein reichen nicht. Der Abzug gilt nur, wenn alle Spenden 2025 zusammen mindestens CHF 100 ergeben. Bitte die übrigen Spenden des Jahres prüfen.
> - **Kita:** Die Wegleitung verlangt die Aufstellung der bezahlten Kosten mit Empfängern unaufgefordert beizulegen (Ziff. 16.6). Die Rechnungen selbst bleiben bei «auf Verlangen». Die Aufstellung ist dann einzureichen. Das sollte mit dem Steueramt bzw. der Wegleitung S. 31 abgeglichen werden.
> - **Spende und Ziff. 22.2:** Auch hier ist laut Wegleitung eine Aufstellung aller Zuwendungen beizulegen, falls der Abzug geltend gemacht wird.
> - **Hausrat:** Der Ausschluss ist im Wiki aus AR belegt (ar-wl-2025__c0085). Für ZH habe ich keine eigene Fundstelle gefunden. Die Einordnung bleibt deshalb offen, bis ZH-Wegleitung und Formular geprüft sind.
> - **Handy:** Die Fundstelle (zh-zstb-30-3__c0018) betrifft selbstgenutzte Liegenschaften. Der Grundsatz (Art. 34 lit. a DBG) gilt aber allgemein. Nur bei beruflicher Nutzung (z. B. Homeoffice) käme etwas in Betracht. Dann bitte die Berufsauslagen prüfen.
> - **Krankenkassen-Leistungsabrechnung** (nicht vorhanden, aber relevant): Nur bei Krankheits- oder Unfallkosten über dem Selbstbehalt einreichen (Ziff. 22.1).
> 
> Die Kategorien stammen aus der Liste, die noch nicht bestätigt ist (Spalte «Bestätigt» leer). Die Einreichepflicht ist mit Wegleitung ZH 2025 belegt.

## q02

**Frage:** In welche Ziffer und mit welchem Code der ZH-Steuererklärung 2025 gehört der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb)?

**Soll (Referenz):** Ziff. 1.1 Haupterwerb, Code 100 (Person 1) / 101 (Person 2); Nettolohn Lohnausweis Ziff. 11 (zh-form-300-2025).

**Antwort des Agenten** (21.9 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__suche):

> **Zürich · Steuerjahr 2025**
> 
> Der Nettolohn aus Lohnausweis Ziff. 11 gehört in **Ziff. 1.1 «Haupterwerb unselbständig», Code 100** (Person 1). Die Zeile gilt für Staats- und Bundessteuer gleich, es gibt keinen Spaltenunterschied.
> 
> - **Rechnen:** Summe der Ziff. 11 aller Haupterwerbs-Lohnausweise von Person 1. Ziff. 11 ist Ziff. 8 (Bruttolohn) minus Ziff. 9 (AHV/IV/EO/ALV/NBUV) minus Ziff. 10.1 und 10.2 (BVG).
> - **Beilegen:** Den Lohnausweis legen Sie bei, für jeden Arbeitgeber, auch bei Nebenerwerb (§ 134 Abs. 1 lit. a StG).
> - **Beachten:** BVG-Einkäufe (Ziff. 10.2) sind schon abgezogen und dürfen nicht nochmals in Ziff. 16.1 (Code 280) erscheinen. Erwerbslücken müssen Sie ausdrücklich angeben.
> 
> Person 2 steht in derselben Ziffer mit Code 101.
> 
> Status: ☑️ agent-geprüft. Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> Quellen: zh-form-300-2025__c0004 (Formular 300, Ziff. 1.1) und zh-wl-2025__c0032 (Wegleitung ZH 2025, Ziff. 1.1).

## q03

**Frage:** Lohnausweis Feld F ist angekreuzt (Geschäftsauto). Was bedeutet das für den Fahrkostenabzug (SG 2025)?

**Soll (Referenz):** Feld F angekreuzt → kein Fahrkostenabzug für den Arbeitsweg mit Geschäftsfahrzeug (Privatanteil im Lohn, Lohnausweis Ziff. 2.2).

**Antwort des Agenten** (30.4 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__beleg, steuerwiki__suche, steuerwiki__zeige):

> **SG · Steuerjahr 2025**
> 
> Wenn im Lohnausweis Feld F angekreuzt ist und ein Geschäftsauto privat genutzt wird, gibt es **keinen Fahrkostenabzug** für den Arbeitsweg (WL SG 2025 Ziff. 10.1, sg-wl-2025__c0076; Form. 4 Ziff. 1; ☑️ agent-geprüft, Abnahme offen).
> 
> **Begründung:** Der Privatanteil von 0,9 % des Fahrzeugkaufpreises (exkl. MWST) pro Monat, also 10,8 % pro Jahr, deckt den Arbeitsweg ab. Der Privatanteil muss in Ziff. 2.2 des Lohnausweises stehen. Die pauschale Berechnung ist in Art. 18a^bis StV SG geregelt.
> 
> **Ausnahme mit Bordbuch:** Werden die privaten Fahrten inklusive Arbeitsweg nach der effektiven Nutzung abgerechnet, können die effektiven Arbeitswegkosten bis zum Maximalabzug geltend gemacht werden:
> - Kanton: max. CHF 8'000
> - Bund: max. CHF 3'300
> - Der Privatanteil muss in beiden Fällen im Lohnausweis als Gehaltsnebenleistung stehen.
> - Das Bordbuch muss die einzelnen Fahrten und Kilometer vollständig belegen.
> - Der Kilometersatz für 2025 beträgt CHF 0.70 (der Satz von CHF 0.75 gilt erst ab 2026).
> 
> **Was zu prüfen ist:**
> 1. Steht bei Feld F auch der Privatanteil in Ziff. 2.2? Falls nicht, ist der Lohnausweis unvollständig.
> 2. Wurde mit Bordbuch oder pauschal gerechnet? Nur mit Bordbuch lässt sich ein Abzug geltend machen.
> 3. Der Bund wird im Formular nicht separat erfasst. Die Behandlung folgt dem Kanton, und ich habe die Bundsregel für 2025 nicht eigenständig gegengeprüft. Die Bundes-Wegleitung zum Lohnausweis im Wiki gilt nur für 2026.
> 
> Quellen: sg-wl-2025__c0075, sg-wl-2025__c0076, sg-stv__art-18a, sg-stb-39-3__c0015.

## q04

**Frage:** Wie hoch ist der maximale Fahrkostenabzug 2025 in TG (Staatssteuer) und beim Bund, und welcher km-Ansatz gilt für das Auto?

**Soll (Referenz):** TG 2025 Staat max. CHF 6'000 (tg-stg__par-29), Bund max. CHF 3'300 (bund-dbg-2025__art-26); Auto TG gestaffelt 0.60/0.50/0.40 je nach Jahres-km, Bund 0.70.

**Antwort des Agenten** (25.1 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Thurgau · Steuerjahr 2025**
> 
> **Maximaler Fahrkostenabzug (Wohn-/Arbeitsstätte)**
> - **Kanton TG (Staatssteuer): CHF 6'000** pro Jahr. Der Betrag umfasst alle Fahrkosten zusammen, auch Wochenaufenthalt und Nebenerwerb. Fundstelle: tg-stg__par-29. Status ☑️ agent-geprüft, Abnahme offen.
> - **Bund (direkte Bundessteuer): CHF 3'300** pro Person und Jahr. Fundstelle: bund-dbg-2025__art-26. Status ☑️ agent-geprüft.
> - Die ESTV-Wegleitung 2025 (S. 6) nennt noch 3'200 Franken. Das Gesetz (3'300) geht nach der Rangfolge vor, aber der Widerspruch ist nicht geklärt.
> 
> **km-Ansatz für das Privatauto**
> - **Kanton TG: gestaffelt**, kumulativ berechnet (Fundstelle tg-bkv__par-1):
>   - bis 3'000 km: CHF 0.60/km
>   - 3'001–5'000 km: CHF 0.50/km
>   - über 5'000 km: CHF 0.40/km
>   - Beispiel laut StP 29 Nr. 2: 8'000 km ergeben CHF 4'000.
>   - Der Ansatz gilt nur, wenn der öffentliche Verkehr nicht zumutbar ist. Im Normalfall werden die Kosten des ÖV-Abos abgezogen.
>   - Bei 100%-Tätigkeit gelten in der Regel höchstens 225 Arbeitstage (tg-wl-2025__c0003).
> - **Bund: CHF 0.70/km** einheitlich, ebenfalls nur ohne zumutbare ÖV-Alternative (bund-bkv-2025__anhang-1).
> 
> Die Werte sind agent-geprüft; die fachliche Abnahme steht noch aus.

## q05

**Frage:** Welcher km-Ansatz für Autos gilt 2026 bei der direkten Bundessteuer?

**Soll (Referenz):** CHF 0.75 pro km (bund-mm-2025-09-11-kalte-progression-2026__c0004; RS 2-215).

**Antwort des Agenten** (21.8 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Bund · Steuerjahr 2026:** Für Privatautos gilt ein Ansatz von **CHF 0.75 pro Fahrkilometer**, neu ab 2026 (Vorjahr CHF 0.70). Quelle: Mitteilung zur kalten Progression 2026, `bund-mm-2025-09-11-kalte-progression-2026__c0004`. Status ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen.
> 
> Einschränkungen:
> - Der Ansatz gilt nur, wenn für den Arbeitsweg kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist.
> - Der Gesamtabzug für Fahrkosten Wohn-/Arbeitsstätte ist auf **CHF 3'300** pro Jahr begrenzt (Art. 26 Abs. 1 lit. a DBG, `bund-dbg-2026__art-26`).
> - Laut Wiki wird der Ansatz künftig an den TCS-Kilometerpreis gekoppelt und kann sich nach oben oder unten anpassen.
> 
> Zum Vergleich: Motorrad mit weissem Kontrollschild CHF 0.40/km, Velo, Motorfahrrad oder Motorrad mit gelbem Kontrollschild CHF 700 Pauschale.
> 
> Die Kantone haben eigene Arbeitstage-Regeln (ZH 240, SG 220, TG 225), die das Bundesergebnis beeinflussen können. Nennen Sie den Kanton, dann prüfe ich den kantonalen Wert mit dem Bundesteil.

## q06

**Frage:** Maximaler Säule-3a-Abzug 2025 für eine Arbeitnehmerin mit Pensionskasse? Und für eine Selbständige ohne 2. Säule?

**Soll (Referenz):** Mit 2. Säule CHF 7'258; ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288 (bund-bsv-masszahlen-2025-2026__c0003).

**Antwort des Agenten** (23.0 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Bund · Steuerjahr 2025** (Kanton nicht genannt, daher nur der Bundeswert)
> 
> **Arbeitnehmerin mit Pensionskasse (2. Säule):** maximal **CHF 7'258**
> - Fundstelle: `bund-bsv-masszahlen-2025-2026__c0003` (oberer BVG-Grenzbetrag 7'258, 8 %-Regel)
> - Status: ☑️ agent-geprüft, Abnahme offen
> 
> **Selbständige ohne 2. Säule:** maximal **CHF 36'288**, und zwar 20 % des Erwerbseinkommens, höchstens dieser Betrag
> - Fundstellen: `bund-bsv-masszahlen-2025-2026__c0003` (40 %-Regel, Grenzbetrag 36'288) und `bund-bvv3__art-7` (20 %-Regel)
> - Status: ☑️ agent-geprüft, Abnahme offen
> - Entscheidend ist das Erwerbseinkommen: Liegt es unter CHF 181'440, ist der Abzug auf 20 % davon begrenzt. Bei Selbständigen gilt das Nettoeinkommen aus der Tätigkeit.
> 
> **Hinweise:**
> - Die Pensionskasse-Frage hängt an der Unterstellung unter die 2. Säule. Eine Arbeitnehmerin mit PK-Beiträgen gilt als unterstellt, auch wenn sie nur Teilzeit arbeitet.
> - Die Kantone können eigene Ansätze führen. Für die kantonale Steuer brauche ich den Kanton (AR, SG, TG oder ZH). Schreib z. B. «TG 2025: …», dann prüfe ich den kantonalen Wert.
> - Wenn du das Erwerbseinkommen der Selbständigen nennst, rechne ich den 20-%-Abzug konkret aus.

## q07

**Frage:** Kinderabzug 2025 in AR für ein 10-jähriges Kind – und beim Bund?

**Soll (Referenz):** AR 2025: CHF 7'400 (4.–15. Altersjahr; Anhang 1 StG, ar-stg-anhang-kp__c0001); Bund CHF 6'800 (Art. 35 DBG) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (22.9 s · Tools: 2 Aufrufe steuerwiki__wert):

> **AR · Steuerjahr 2025**
> 
> Ein 10-jähriges Kind fällt in die Altersstufe «nach Vollendung des 4. bis Vollendung des 15. Altersjahres». Der Kinderabzug beträgt **CHF 7'400** (indexiert). Quelle: `ar-stg-anhang-kp__c0001`, Art. 38 Abs. 1 lit. a Ziff. 2. Formular: Ziff. 23.2. Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Bund (direkte Bundessteuer) 2025**
> 
> - **Kinderabzug vom Einkommen: CHF 6'800.** Der Bund kennt keine Altersstaffelung, der Betrag gilt für jedes minderjährige Kind. Quelle: `bund-dbg-2025__art-35`, Status ☑️ agent-geprüft.
> - **Abzug vom Steuerbetrag: CHF 263** pro Kind (Elterntarif). Quelle: `bund-dbg-2025__art-36-t4`. Das ist eine Ermässigung der Steuer, kein Einkommensabzug, und gilt zusätzlich zum Kinderabzug von CHF 6'800.
> - **Versicherungsabzug-Zuschlag: CHF 700** pro Kind. Quelle: `bund-dbg-2025__art-33-t5`. Auch dies ist ein Zuschlag zum Versicherungsabzug, nicht der Kinderabzug selbst.
> 
> **Kurz:** Kanton AR CHF 7'400 · Bund CHF 6'800 (Einkommen) plus CHF 263 (Steuerbetrag). Die beiden Ebenen sind getrennt zu deklarieren.
> 
> Wenn du die Ziffern im Formular brauchst, kann ich die Position `position ar 2025 23.2` abrufen.

## q08

**Frage:** Versicherungsabzug ZH 2025 für ein Ehepaar mit 2 Kindern, beide mit Pensionskasse (Staatssteuer und Bund)?

**Soll (Referenz):** ZH Staat: 5'800 + 2 × 1'300 = 8'400; Bund: 3'700 + 2 × 700 = 5'100 (zh-stg-2025__par-31-t2, bund-dbg-2025__art-33).

**Antwort des Agenten** (25.7 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__rechne):

> **ZH · 2025**
> 
> Versicherungsabzug für Ehepaar mit 2 Kindern, beide mit Beiträgen an Pensionskasse (2. Säule):
> 
> | | Basis Ehepaar | Zuschlag 2 Kinder | Total |
> |---|---|---|---|
> | **Kanton ZH (Staatssteuer)** | CHF 5'800 | 2 × CHF 1'300 = 2'600 | **CHF 8'400** |
> | **Bund (direkte Bundessteuer)** | CHF 3'700 | 2 × CHF 700 = 1'400 | **CHF 5'100** |
> 
> - **Kanton:** versicherung.verheiratet, Fundstelle zh-stg-2025__par-31-t2 (§ 31 Abs. 2 StG ZH), Status ☑️ agent-geprüft, Abnahme offen. Zuschlag je Kind: versicherung.kind, gleiche Fundstelle.
> - **Bund:** versicherung.verheiratet, Fundstelle bund-dbg-2025__art-33-t2; Zuschlag je Kind: bund-dbg-2025__art-33-t5, Status ☑️ agent-geprüft.
> 
> **Zu beachten:**
> - Der Zuschlag gilt nur für Kinder, für die ein Kinderabzug nach § 34 Abs. 1 (ZH) bzw. Art. 35 Abs. 1 lit. a/b DBG geltend gemacht werden kann.
> - Der Versicherungsabzug ist eine Pauschale. Die tatsächlichen Pensionskassenbeiträge (Lohnausweis Ziff. 10.1) werden separat unter den Abzügen für Vorsorge (ZH Ziff. 16.1) erfasst. Sie ersetzen den Versicherungsabzug nicht.
> - Ohne Beiträge an 2. Säule/3a gelten höhere Ansätze (ZH Ehepaar: CHF 8'700 + Kinderzuschlag). Das trifft hier nicht zu, da beide Beiträge leisten.
> - Die Formularziffer für die Eingabe ist ZH Ziff. 15 (Code 270). Falls du die Felder ausfüllen willst, sag Bescheid.

## q09

**Frage:** Wie hoch ist der Kinderdrittbetreuungsabzug 2025 im Kanton ZH, und gilt 2026 ein anderer Wert?

**Soll (Referenz):** ZH 2025 CHF 25'000 (StG Nachtrag 127, zh-stg-2025__par-31-t4); 2026 CHF 25'300 (zh-stg-2026__par-31-t3). Die VKP ab 2024 (10'400) ist überholt.

**Antwort des Agenten** (22.0 s · Tools: 2 Aufrufe steuerwiki__wert):

> **ZH · Steuerjahr 2025 und 2026**
> 
> **Kinderdrittbetreuungsabzug (Staatssteuer, Kanton ZH):**
> - **2025: max. CHF 25'000** pro Kind. Voraussetzungen: Kind hat das 14. Altersjahr noch nicht vollendet, lebt im gleichen Haushalt, und die Kosten hängen direkt mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit zusammen. Fundstelle: zh-stg-2025__par-31-t4. Status ☑️ agent-geprüft, Abnahme offen.
> - **2026: max. CHF 25'300** pro Kind. Fundstelle: zh-stg-2026__par-31-t3. Status ☑️ agent-geprüft, Abnahme offen. Laut Wiki gilt bei Konkubinat oder alternierender Obhut mit gemeinsamer Sorge je der halbe Abzug (CHF 12'650).
> 
> Der Wert steigt also um CHF 300. Die Altersgrenze (14 Jahre) bleibt gleich.
> 
> **Bund (direkte Bundessteuer), getrennt zu deklarieren:** CHF 25'800 für 2025 und 2026, Altersgrenze ebenfalls 14 Jahre (bund-dbg-2025__art-33-t7 bzw. bund-dbg-2026__art-33-t7, ☑️ agent-geprüft).
> 
> **Formular:** Ziffer 16.6 «Abzug für fremdbetreute Kinder» (Code 376) in beiden Jahren. Die Rechenregel erhältst du mit `position zh 2025 16.6` bzw. `position zh 2026 16.6`.
> 
> **Hinweis:** Die alte VKP ab 2024 nennt noch CHF 10'400. Das Wiki stuft diesen Wert als überholt ein, weil das StG (Nachtrag 127 für 2025, Nachtrag 132 für 2026) die höheren Beträge festlegt. Die Werte sind agent-geprüft, die Abnahme durch eine Fachperson steht noch aus.

## q10

**Frage:** Gibt es im Kanton TG einen Zweiverdienerabzug für die Staatssteuer?

**Soll (Referenz):** Nein, TG kennt keinen kantonalen Zweiverdienerabzug (nur Bund: 50 %, 8'600–14'100).

**Antwort des Agenten** (21.6 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Thurgau · Steuerjahr 2025** (Jahr aus Ihrer Frage nicht angegeben, daher 2025 angenommen)
> 
> **Nein.** Die Staats- und Gemeindesteuer im Kanton TG kennt keinen Zweiverdienerabzug.
> 
> - **Kanton (Staats- und Gemeindesteuer):** Im Gesetz ist kein Zweiverdienerabzug vorgesehen. Die Wegleitung TG 2025 sagt dazu: «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.» (`tg-wl-2025__c0104`, Formular Ziff. 18). Die Praxis StP 34 Nr. 25 bestätigt das für 2025–2027 (`tg-stp-34-25__c0001`). Status: ✅ verifiziert (Fundstelle geprüft).
> - **Bund (direkte Bundessteuer):** Dort gibt es den Abzug, und er wird separat deklariert. Er beträgt 50 % des niedrigeren Erwerbseinkommens, mindestens CHF 8'600 und höchstens CHF 14'100 (Art. 33 Abs. 2 DBG, `bund-dbg-2025__art-33-t6`). Status: ☑️ agent-geprüft, Abnahme offen.
> 
> Die Praxis-Texte in StP 34 Nr. 25 zur Aufteilung von Erwerbseinkommen beziehen sich auf den Bundesabzug, nicht auf die kantonale Steuer.

## q11

**Frage:** SG 2025: Pauschale für übrige Berufskosten? Wie wird sie berechnet?

**Soll (Referenz):** SG 2025: CHF 700 + 10 % des Nettolohns, max. CHF 2'400 (Art. 21 StV SG, WL SG 2025).

**Antwort des Agenten** (23.0 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **SG · 2025**: Die Pauschale für übrige Berufskosten beträgt **Fr. 700 zuzüglich 10 % der Nettoeinkünfte**, höchstens **Fr. 2'400**.
> 
> - **Nettoeinkünfte** (Nettolohn) = Bruttoeinkünfte abzüglich AHV/IV/EO/ALV/UV- und BVG-Beiträge, ohne Einkäufe.
> - **Minimum:** keines im SG-Recht.
> - **Nachweis:** Höhere Kosten können nachgewiesen werden; die Pauschale ist widerlegbar.
> 
> **Beispiel:** Nettoeinkünfte Fr. 30'000 → 700 + 10 % × 30'000 = 3'700, gedeckelt auf **Fr. 2'400**. Die Obergrenze greift ab Nettoeinkünften von Fr. 17'000 (700 + 1'700 = 2'400).
> 
> **Bund (direkte Bundessteuer), separat deklarieren:** 3 % des Nettolohns, mindestens Fr. 2'000, höchstens Fr. 4'000.
> 
> **Formular SG 2025:** Ziff. 10.1 (Person 1, Code 438) bzw. Ziff. 10.2 (Person 2, Code 488) für Berufskosten bei unselbständiger Erwerbstätigkeit.
> 
> **Quellen:**
> - Art. 21 StV SG (`sg-stv__art-21`), Status ☑️ agent-geprüft, Abnahme offen
> - WL SG 2025, Ziff. 10.3 (`sg-wl-2025__c0080`), Status ☑️ agent-geprüft, Abnahme offen
> 
> Nicht verwechseln: Bei der Nebenerwerbstätigkeit gilt eine andere Regelung (20 %, min. Fr. 800, max. Fr. 2'400, StB 39 Nr. 9).

## q12

**Frage:** Pauschalabzug Liegenschaftsunterhalt in AR für ein 8-jähriges Einfamilienhaus – und wie in ZH?

**Soll (Referenz):** AR: 10 % (Gebäude bis 10 Jahre) bzw. 20 % des Bruttoertrags, nur bis Bruttomietertrag 100'000 (Art. 25 StV AR, MB 03); ZH: einheitlich 20 % ohne Altersstaffel (ZStB 30.2).

**Antwort des Agenten** (24.5 s · Tools: 2 Aufrufe steuerwiki__wert):

> **AR · Steuerjahr 2025** (Jahr nicht genannt, daher 2025 angenommen)
> 
> **Pauschalabzug Liegenschaftsunterhalt für ein 8-jähriges Einfamilienhaus: 10 % des Bruttomietertrags**
> 
> - **Kanton AR:** 10 % bei Gebäuden bis 10 Jahre, 20 % bei älteren Gebäuden. Fundstelle: ar-mb-03__c0004. Status: ☑️ agent-geprüft, Abnahme offen.
> - **Bund:** ebenfalls 10 % bis 10 Jahre (bund-lkv__art-5, Status ☑️). Der Bund wird separat deklariert. Das Alter wird dort zu Beginn der Steuerperiode gemessen.
> - **Bedingung in AR:** Der Pauschalabzug gilt nur, wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.
> - **Wahlrecht:** Pro Gebäude und Periode kann man zwischen Pauschale und effektiven Kosten wählen.
> 
> **Zum Vergleich ZH 2025:** 20 %, unabhängig vom Gebäudealter. Es gibt keine Staffelung nach 10 Jahren. Fundstelle: zh-zstb-30-2__c0002, Status ☑️ agent-geprüft, Abnahme offen. Der Bund bleibt bei 10 % bis 10 Jahre.
> 
> **Wichtig bei einem Einfamilienhaus:**
> - Die Pauschale bezieht sich auf den **Bruttomietertrag**. Wird das Haus selbst bewohnt, gibt es keinen Mietertrag. In ZH gilt die Pauschale laut Wiki auch für den **Mietwert** (Brutto-Mietertrag bzw. Mietwert). Für AR fehlt eine entsprechende Fundstelle. Ob ein selbst bewohntes Haus in AR überhaupt eine Pauschale bekommt, habe ich nicht belegt. Dort gilt der Selbstnutzungsabzug von 20 % auf dem Eigenmietwert (ar-wl-2025__c0001).
> - Ob Pauschale oder effektive Kosten günstiger ist, hängt von den tatsächlichen Unterhaltskosten ab. Das prüfe ich gern, wenn du mir die Beträge und die Eigennutzung/Vermietung nennst.
> 
> Falls du ein anderes Steuerjahr meinst (z. B. 2026), sag Bescheid, dann schaue ich nach.

## q13

**Frage:** TG: Welcher Einschlag gilt auf dem Eigenmietwert der selbstbewohnten Liegenschaft am Wohnsitz (Kanton vs. Bund)?

**Soll (Referenz):** TG: Abzug 40 % Kanton, 20 % Bund für dauernd selbstbewohntes Eigentum am Wohnsitz (tg-stg__par-23; WL TG 2025).

**Antwort des Agenten** (24.1 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **TG · Steuerjahr 2025** (Jahr nicht genannt, daher 2025 verwendet)
> 
> - **Kanton (Staats- und Gemeindesteuer): 40 %** Selbstnutzungsabzug auf dem Eigenmietwert. Quelle: tg-stg__par-23 (§ 23 StG TG); tg-stp-23-1__c0005. Status: ☑️ agent-geprüft, Abnahme offen.
> - **Bund (direkte Bundessteuer): 20 %.** Quelle: tg-wl-2025__c0002 (Kurzübersicht: „40 % Kanton / 20 % Bund“) und tg-wl-2025__c0225. Status: ☑️ agent-geprüft, Abnahme offen.
> 
> Der Abzug gilt nur für die am Wohnsitz dauernd selbstbewohnte Liegenschaft. Zweit- und Ferienwohnungen sowie an Nahestehende überlassene Objekte sind ausgenommen.
> 
> Im DBG gibt es keinen festen Prozentsatz für den Eigenmietwert; die 20 % für den Bund sind der Wert, den das TG-Verfahren und der Wiki-Eintrag ausweisen. Das Wiki führt den Bundessatz nicht mit einer eigenen Fundstelle aus dem DBG. Die Angabe ist deshalb nicht vollständig belegt. Die Fachperson sollte sie bestätigen.
> 
> Im TG-Formular 2025 steht der Eigenmietwert bei Ziffer 8.1 (Formular 7, Code 180). Der Selbstnutzungsabzug ist dort in der Spalte „Selbstnutzungsabzug“ mit Kanton- und Bundeswert zu erfassen.

## q14

**Frage:** Bis wann kann ein Treuhänder im Kanton TG für seine Mandanten Fristerstreckung erhalten?

**Soll (Referenz):** Gewerbsmässige Treuhänder für Mandanten bis 31.12. des Deklarationsjahres (StP 155 Nr. 2).

**Antwort des Agenten** (27.6 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Thurgau · Steuerjahr 2025** (Sie haben kein Jahr genannt, daher 2025 angenommen; Deklarationsjahr 2026)
> 
> Ein gewerbsmässiger Treuhänder oder Steuerberater kann für seine Mandanten ein Fristerstreckungsgesuch **längstens bis 31. Dezember des Deklarationsjahres** stellen. Für Steuerjahr 2025 ist das **31. Dezember 2026**. Heute ist der 9. November 2026, also bleiben noch rund sieben Wochen.
> 
> Weitere Gesuche über den 30. November hinaus werden nur bei ausserordentlichen Gründen behandelt, und allgemeine Gründe wie starke berufliche Belastung des Vertreters reichen dafür nicht. Für Private gilt das erste Gesuch grundsätzlich bis 30. September, weitere in begründeten Fällen bis 30. November.
> 
> Gesuche gehen schriftlich an das Gemeindesteueramt, das über die Bewilligung schriftlich entscheidet. Die Gebühren für Fristerstreckungen regelt § 39b StV TG. Die Höhe habe ich nicht geprüft.
> 
> Quellen: `tg-stp-155-2__c0002` (Treuhänder-Frist, Status ☑️ agent-geprüft), `tg-stp-155-2__c0001` (Gesuch und Frist 30.09./30.11.), `tg-stp-155-2__c0005` (Entscheid).
> 
> Falls Sie Steuerjahr 2026 meinen, verschiebt sich die Frist auf den 31. Dezember 2027.

## q15

**Frage:** ZH: Bis wann ist die Steuererklärung 2025 einzureichen und wie lange wird höchstens Fristerstreckung gewährt?

**Soll (Referenz):** Einreichung bis 31.03.2026; Fristerstreckung längstens bis 30. November (ZStB 132.1 / WL ZH 2025).

**Antwort des Agenten** (27.1 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **ZH · Steuerjahr 2025**
> 
> - **Ordentliche Einreichungsfrist:** 31. März 2026 (WL ZH 2025, `zh-wl-2025__c0017`).
> - **Höchstens mögliche Fristerstreckung:** Rechtzeitig eingereichte Gesuche werden bis längstens **30. November 2026** bewilligt (ZStB 132.1, `zh-zstb-132-1__c0024`).
> 
> Für Ihre Situation heisst das: Heute ist der 9. November 2026, also liegt der Endtermin noch vor uns. Die Erstreckung gilt aber nur, wenn das Gesuch **vor dem 31. März 2026** beim Gemeindesteueramt eingereicht wurde. Ein Gesuch, das nach Fristablauf gestellt wird, ist abzuweisen. Dann bleibt nur die Wiederherstellung der Frist nach § 15 StV bzw. Art. 119 Abs. 2 DBG, und das Gemeindesteueramt entscheidet darüber.
> 
> Wenn bisher kein Gesuch gestellt wurde, ist die Frist bereits abgelaufen und die Wiederherstellung ist der einzige Weg. Ob sie gewährt wird, hängt von den Voraussetzungen ab, die ich hier nicht beurteilen kann.
> 
> **Offene Punkte:**
> - Die Kosten einer Fristerstreckung nennen die Quellen nicht.
> - Die Fundstellen sind agent-geprüft (☑️), die fachliche Abnahme steht noch aus.
> - Die Regel stammt aus ZStB 132.1 in der Fassung ab 1.1.2026. Das ist die Fassung, die für die 2025er-Erklärung im Jahr 2026 gilt.

## q16

**Frage:** AR: Was kostet die zweite Fristverlängerung?

**Soll (Referenz):** CHF 25 (erste Verlängerung kostenlos, jede weitere CHF 25; MB 18 / WL AR 2025).

**Antwort des Agenten** (23.2 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__wert):

> **AR · Steuerjahr 2025:** Die zweite Fristverlängerung kostet **CHF 25**.
> 
> Die erste Fristerstreckung ist kostenlos, jede weitere kostet CHF 25 (Art. 59a StV AR; Merkblatt 18 nennt für Wiederholungsfälle ebenfalls Fr. 25). Das Gesuch muss vor Ablauf der Einreichefrist bei der Kantonalen Steuerverwaltung gestellt werden.
> 
> Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Quellen: `ar-stv__art-59a`, `ar-mb-18__c0001`, `ar-wl-2025__c0012`.
> 
> Die Bundessteuer kennt keine eigene Fristerstreckung. Sie läuft über die kantonale Erklärung.
> 
> Du hast kein Steuerjahr angegeben, deshalb habe ich 2025 verwendet. Für 2026 kann ich das separat prüfen.

## q17

**Frage:** Krankheitskosten SG 2025: Ab welchem Selbstbehalt sind sie abziehbar – und beim Bund?

**Soll (Referenz):** SG: Selbstbehalt 2 % (Art. 46 StG SG); Bund: 5 % (Art. 33 Abs. 1 lit. h DBG, KS 11).

**Antwort des Agenten** (24.4 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__position):

> **SG · Steuerjahr 2025**
> 
> **Kanton St. Gallen:** Krankheits- und Unfallkosten sind abziehbar, soweit sie **2 % des Nettoeinkommens** (Ziff. 20) übersteigen. Der Abzug ist also erst ab dem Betrag über dem Selbstbehalt wirksam: Abzug = max(0; Σ Kosten − 2 % × Ziff. 20). Behinderungsbedingte Kosten haben keinen Selbstbehalt; sie gehören in Ziff. 21.2.
> - Formular SG 2025: Ziff. 21.1, Vorkolonne Code 650, Selbstbehalt Code 238, Abzug Code 240.
> - Pauschale für lebensnotwendige Diät (z. B. Zöliakie): Fr. 2'500, zusätzlich zur Vorkolonne. Nicht bei Diabetes; bei erstmaliger Deklaration ärztliche Bescheinigung nötig.
> - Quellen: sg-form-1-2025__c0010, sg-wl-2025__c0098, Limite ☑️ agent-geprüft (Abnahme offen).
> 
> **Bund (direkte Bundessteuer) 2025:** Abziehbar, soweit die Kosten **5 %** der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen. Die Basis ist also nicht dieselbe wie im Kanton. Das Formular SG 2025 hat keine separate Bundesspalte; die Steuerbehörde nimmt die Abweichung automatisch vor (Merkblatt 32).
> - Quelle: bund-dbg-2025__art-33-t3, Praxis ESTV-KS 11 (2005). Das KS 11a (publiziert 26.05.2026) gilt laut seiner Ziff. 7 erst ab Steuerperiode 2027, nicht für 2025.
> 
> **Zusammengefasst:** Kanton SG 2 % der Nettoeinkünfte (Ziff. 20), Bund 5 % der Einkünfte nach Art. 26–33. Die Selbstbehalte sind unterschiedlich hoch und haben unterschiedliche Basen, deshalb in der Erklärung getrennt rechnen.
> 
> Offen: Die Fundstellen sind agent-geprüft, die fachliche Abnahme steht noch aus. Die Bundesbasis (Art. 26–33) sollte bei einem konkreten Fall anhand des Nettoeinkommens nachgerechnet werden.

## q18

**Frage:** PK-Einkauf CHF 20'000 wurde über den Lohn abgezogen (Lohnausweis Ziff. 10.2). Darf er nochmals in der Steuererklärung abgezogen werden?

**Soll (Referenz):** Nein – BVG-Einkauf über Lohnabzug (Lohnausweis Ziff. 10.2) ist bereits im Nettolohn berücksichtigt; nur direkt bezahlte Einkäufe separat abziehen.

**Antwort des Agenten** (32.4 s · Tools: 4 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Bund · Steuerjahr 2025 (angenommen, Kanton offen)**
> 
> Nein, nicht doppelt. Der Betrag wird nur einmal abgezogen, aber er muss in der Steuererklärung geltend gemacht werden, damit er überhaupt wirkt.
> 
> - **Lohnabzug gehört in den Lohnausweis, nicht aufs Formular 21.** Bei Arbeitnehmern sind alle vom Lohn abgezogenen Beiträge an die berufliche Vorsorge im Lohnausweis aufzuführen und dürfen nicht mit Formular 21 bescheinigt werden (MB 21 EDP, Ziff. 1, Rz 12, `bund-mb-21edp__c0006`).
> - **Einkauf für den Abzug muss separat ausgewiesen sein.** Damit der Arbeitnehmer den Einkauf geltend machen kann, muss die Einkaufssumme im Lohnausweis separat in der Rubrik «Versicherungsbeiträge» stehen (KS W03-001, Ziff. 3.3, `bund-ks-w03-001__c0009`). Ihre 20'000 CHF in Ziff. 10.2 erfüllen das, sofern die Summe dort so ausgewiesen ist.
> - **Keine zweite Erfassung.** Den Betrag nicht zusätzlich auf Formular 21 oder als eigenen Einkauf nochmals eintragen. Der Lohnausweis ist die Quelle, die Steuererklärung nimmt ihn einmal auf.
> 
> Ob 20'000 CHF im Einzelfall voll abzugsfähig sind, hängt von Ihrer persönlichen Situation ab. Eine Kapitalbezug-Sperrfrist nach Art. 79b BVG ist dabei zu beachten (KS 41, Ziff. 2.2.4, `bund-ks-41__c0014`). Den Abzug habe ich dazu nicht geprüft.
> 
> Damit ich die kantonale Ziffer und die Limite nennen kann, brauche ich noch den **Kanton** (ZH, SG, TG oder AR). Dann suche ich die Position im kantonalen Formular und prüfe, ob der Betrag dort anders behandelt wird.

## q19

**Frage:** Weiterbildungskosten CHF 15'000 (ZH, 2025), Arbeitgeber hat nichts bezahlt. Wie viel ist abziehbar (Kanton/Bund)?

**Soll (Referenz):** ZH Staat max. CHF 12'400 (zh-stg-2025__par-31-t4); Bund max. CHF 13'000 (bund-dbg-2025__art-33-t4).

**Antwort des Agenten** (22.2 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position):

> **ZH · 2025**
> 
> Da der Arbeitgeber nichts bezahlt hat, sind die vollen CHF 15'000 selbst getragen. Abziehbar ist davon höchstens:
> 
> - **Kanton (Staats-/Gemeindesteuer): CHF 12'400**. Das ist der Höchstbetrag, die übrigen CHF 2'600 sind nicht abziehbar.
> - **Bund (direkte Bundessteuer): CHF 13'000**. Der Bund hat einen höheren Höchstbetrag, also werden hier CHF 13'000 abgezogen, die übrigen CHF 2'000 nicht.
> 
> Die Beträge sind getrennt zu deklarieren. Im Formular ZH 2025 gehört der Abzug in Ziff. 16.2 (Code 292) über hilfsblatt Form. 367, mit separatem Block für die Bundessteuer.
> 
> **Bedingungen, die ich nicht prüfen kann:**
> - Der Abzug gilt nur, wenn ein Abschluss auf Sekundarstufe II vorliegt oder die Person das 20. Altersjahr vollendet hat, und nicht, wenn sie noch eine Ausbildung bis zum ersten Sek.-II-Abschluss macht. Das ist hier nicht angegeben.
> - Massgebend ist das Jahr der Fälligkeit bzw. Zahlung, nicht der Kursbesuch.
> - Die Kursrechnungen müssen belegt werden. Auf Verlangen ist das Formular «Berufsorientierte Aus- und Weiterbildungskosten» beizulegen.
> 
> **Status:** Die Beträge sind agent-geprüft (Fundstelle geprüft, Abnahme durch Fachperson offen).
> - Kanton: zh-stg-2025__par-31-t4 (Form. 300, Ziff. 16.2; zh-form-367-2025__c0001)
> - Bund: bund-dbg-2025__art-33-t4

## q20

**Frage:** Spenden CHF 50 an eine gemeinnützige Organisation (TG 2025) – abziehbar?

**Soll (Referenz):** Nein – TG: Zuwendungen nur abziehbar, wenn sie CHF 200 übersteigen (StG TG § 34 Abs. 1 Ziff. 11); Bund: ab CHF 100.

**Antwort des Agenten** (25.6 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Thurgau · Steuerjahr 2025**
> 
> **Nein, eine einzelne Spende von CHF 50 ist nicht abziehbar**, weder im Kanton noch beim Bund. Massgebend ist die Summe aller freiwilligen Zuwendungen des Jahres, nicht der einzelne Betrag.
> 
> - **Kanton TG:** Es gilt ein Selbstbehalt von CHF 200. Abziehbar ist nur, was die Gesamtsumme übersteigt: min(Σ − 200; …). Bei Σ = 50 ergibt das 0.
> - **Bund:** Es gilt eine Freigrenze von CHF 100. Erreicht die Gesamtsumme CHF 100, ist der ganze Betrag abziehbar, sonst nichts. Bei Σ = 50 ergibt das 0.
> 
> **Was sich ändert:** Hat die Person 2025 weitere Zuwendungen an gemeinnützige Institutionen, zählt die Gesamtsumme.
> - Summe über CHF 200: Kanton abziehbar ist Σ − 200 (höchstens 8'000, bei Nettoeinkommen bis 40'000, sonst 20 % des Nettoeinkommens).
> - Summe ab CHF 100: Bund abziehbar ist die ganze Summe (höchstens 20 % des Nettoeinkommens).
> 
> **Voraussetzungen für den Abzug:**
> - Die Empfängerin muss eine steuerbefreite juristische Person mit Sitz in der Schweiz sein, mit öffentlichem oder gemeinnützigem Zweck. Prüfen über die Liste der Steuerverwaltung TG.
> - Religiöse, kulturelle, gesellige oder sportliche Zwecke sind nicht abziehbar. Ebenso wenig Empfänger im Ausland oder Sammelvermerke wie «diverse Organisationen».
> - Die Zuwendung wird in Formular 6 (Code 366) mit Name und Sitz der Institution eingetragen und fliesst über Ziffer 23.2 in die Steuererklärung.
> - Belege (Spendenbestätigung) sind ab CHF 1'000 pro Zuwendung einzureichen. Bei CHF 50 nur auf Verlangen.
> 
> **Status:** Die Werte sind agent-geprüft (Fundstelle geprüft, Abnahme offen). Quellen: tg-stg__par-34-t4 (Kanton), bund-dbg-2025__art-33a (Bund), tg-form-06-2025__c0002 und tg-wl-2025__c0220 (Formular und Wegleitung).

## q21

**Frage:** Was ändert sich 2026 bei der Säule 3a (Einkauf) und wo wird das im ZH-Formular 2026 eingetragen?

**Soll (Referenz):** Ab 2026 Einkauf (Nachzahlung) Säule 3a für Beitragslücken ab 2025 (max. 7'258 pro Einkaufsjahr, BVV 3 Art. 7a, KS 18a); ZH-Formular 2026: Ziff. 14.3 (Code 264, Detailfelder 276/278).

**Antwort des Agenten** (30.2 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__position, steuerwiki__zeige):

> **ZH · Steuerjahr 2026**
> 
> **Was sich 2026 ändert:** Ab Steuerperiode 2026 können Erwerbstätige zusätzlich zu den ordentlichen 3a-Beiträgen Einkäufe für Beitragslücken in der Säule 3a leisten. Es geht um Lücken, die ab 1.1.2025 entstanden sind, und zwar innerhalb der zehn Jahre vor dem Einkauf. Das ist nicht der 2.-Säule-Einkauf in die Pensionskasse. (WL ZH 2026 UJ, Ziff. 14, S. 14, `zh-wl-2026-uj__c0077`)
> 
> Voraussetzungen:
> - In den Jahren der Lücke wurden AHV/IV/EO-Beiträge geleistet, sodass die Person 3a-berechtigt war.
> - Im Einkaufsjahr wurde der volle ordentliche Maximalbeitrag einbezahlt.
> - Der Einkauf ist höchstens so hoch wie die Summe der Lücken und in jedem Fall maximal **CHF 7'258**.
> 
> Weil die Lücken frühestens ab 1.1.2025 entstanden sein können, ist für Steuerjahr 2026 praktisch nur die Lücke 2025 einkaufbar.
> 
> **Wo im Formular:** Ziff. **14.3 «Einkauf»** im Abzugsteil (Formular 300 ZH 2026 UJ, S. 3, `zh-form-300-2026-uj__c0008`):
> - Person 1: **Code 276**
> - Person 2: **Code 278**
> - Hauptkolonne: **Code 264**
> 
> Die Rechnung pro Person ist min(Einkauf; Summe der Lücken ab 1.1.2025; 7'258). Die Summe der Personen geht in Code 264.
> 
> **Bund:** Die Höchstbeträge sind dieselben (CHF 7'258). Kanton und Bund werden im Formular in den beiden Spalten erfasst, und die Codes gelten für beide.
> 
> **Zu beachten:**
> - Der ordentliche Beitrag steht weiterhin in Ziff. 14.1/14.2 (Codes 260/261). Der Einkauf setzt voraus, dass dieser Maximalbetrag im Einkaufsjahr voll bezahlt wurde.
> - Die Bescheinigungen (3a-Einkaufsbescheinigung, Nachweis des ordentlichen Beitrags, AHV-Nachweis für die Lücke) gehören zu den Belegen.
> - Die Quelle ist die Fassung für unterjährige Steuerpflicht (UJ). Das reguläre Formular und die Wegleitung 2026 sind laut Wiki-Stand (09.11.2026) noch nicht publiziert. Ziffern und Codes müssen am regulären Formular geprüft werden, sobald es vorliegt.
> - Die Rechtsgrundlage ist im Wiki nur aus der Wegleitung belegt. Den Artikel in der BVV 3 habe ich nicht geprüft.
> - Die Werte sind agent-geprüft (Fundstelle geprüft, Abnahme offen).

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (25.0 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> Welcher Kanton ist es? Die Rückforderung selbst ist Bundesrecht, aber die Deklaration (Wertschriftenverzeichnis, Ziffern) steht in der kantonalen Steuererklärung der natürlichen Person. Ohne Kanton kann ich die Position nicht nennen.
> 
> Was ich bisher belegt habe:
> 
> - **Bund, Steuerjahr 2025:** Die Bundessuche liefert zur Verrechnungssteuer-Rückerstattung nur Kreisschreiben (KS VST 21, KS 18) und Formulare für Bankstiftungen und Depots. Das Formular DA-1 (`bund-form-da1-2025__c0002`) ist dagegen für die **Anrechnung ausländischer Quellensteuern** gedacht, nicht für die 35 % Schweizer Verrechnungssteuer. Es ist für diese Frage also nicht die richtige Fundstelle.
> - **Nicht belegt:** Die konkrete Rückforderungsmechanik für natürliche Personen (Antrag, Formularnummer, Nachweis über die Gutschrift) habe ich bisher nicht in den Quellen gefunden. Ich nenne sie deshalb nicht.
> 
> Sobald Sie den Kanton (ZH, SG, TG oder AR) nennen, suche ich mit `position <kt> 2025 Verrechnungssteuer` bzw. `suche … --jur <kt>` nach dem Wertschriftenverzeichnis und der Rückerstattung. Falls Sie ein anderes Steuerjahr meinen, sagen Sie es bitte; sonst nehme ich 2025.

## q23

**Frage:** Vergleiche den Versicherungsabzug 2025 für Alleinstehende ohne Kinder in AR, SG, TG, ZH und beim Bund.

**Soll (Referenz):** Alleinstehend ohne Kinder 2025 (mit 2. Säule/3a): AR 2'700 · SG 3'400 · TG 3'500 · ZH 2'900 · Bund 1'800.

**Antwort des Agenten** (23.2 s · Tools: 1 Aufrufe steuerwiki__vergleich):

> **Versicherungsabzug 2025, alleinstehend ohne Kinder** (Steuerjahr 2025; Kanton = Staats-/Gemeindesteuer, Bund = direkte Bundessteuer)
> 
> | Steuerebene | Abzug (CHF) | Status | Fundstelle |
> |---|---|---|---|
> | **TG** | 3'500 | ☑️ | tg-stg__par-34-t3 |
> | **SG** | 3'400 | ☑️ | sg-stg-2025__art-45-t2 |
> | **ZH** | 2'900 | ☑️ | zh-stg-2025__par-31-t2 |
> | **AR** | 2'700 | ☑️ | ar-stg__art-35-t2 |
> | **Bund** | 1'800 | ☑️ | bund-dbg-2025__art-33-t2 |
> 
> - **Höchster Kantonsabzug:** Thurgau, 3'500 CHF. **Tiefster:** Appenzell Ausserrhoden, 2'700 CHF.
> - **Bund:** 1'800 CHF, deutlich tiefer als alle vier Kantone.
> - **Ohne Vorsorge:** Für Alleinstehende ohne Vorsorgebeiträge (3a/BVG) gibt es einen höheren Satz in ZH (4'350 CHF, zh-wl-2025__c0084) und SG (3'900 CHF, sg-stg-2025__art-45-t2). TG und AR kennen diese Unterscheidung in der Vergleichstabelle nicht. Bund: 2'700 CHF (bund-rs-2-210__c0006).
> 
> Alle Werte sind agent-geprüft (☑️): Die Fundstelle ist geprüft, die fachliche Abnahme steht noch aus. Vor einer Verwendung in einer Steuererklärung sollten die Chunks einzeln gegengelesen werden (`zeige <chunk-id>`).

## q24

**Frage:** Steuerfreie Vermögensbeträge (Sozialabzüge) 2025 in SG für ein Ehepaar mit einem minderjährigen Kind?

**Soll (Referenz):** SG 2025: 150'000 (Ehepaar) + 20'000 pro minderjähriges Kind = 170'000 (sg-stg-2025__art-64).

**Antwort des Agenten** (25.7 s · Tools: 5 Aufrufe steuerwiki__suche, steuerwiki__formular, steuerwiki__wert, steuerwiki__zeige):

> **SG · Steuerjahr 2025**
> 
> Für ein Ehepaar mit einem minderjährigen Kind ergeben sich **CHF 170'000** steuerfreie Vermögens-Sozialabzüge:
> 
> - **CHF 150'000** für gemeinsam Steuerpflichtige (2 × 75'000)
> - **+ CHF 20'000** für das minderjährige Kind unter elterlicher Sorge/Obhut, für das ein Kinderabzug beansprucht werden kann
> 
> Der Kinderzusatz gilt nur, wenn für das Kind tatsächlich ein Kinderabzug geltend gemacht werden kann. Das Kind muss also minderjährig sein und unter elterlicher Sorge bzw. Obhut stehen.
> 
> Die Abzüge werden auf dem Reinvermögen (Vermögenswerte minus Schulden) berücksichtigt. Im Formular stehen sie in Ziff. 36.1–36.3 (Formular 1, Kanton SG). Ob der Abzug für das Kind das Vermögen in jedem Fall in der Formularzeile gleich aufführt, habe ich nicht geprüft.
> 
> **Bund:** Die direkte Bundessteuer kennt keine Vermögenssteuer. Die Vermögensfreibeträge gelten daher nur für den Kanton.
> 
> **Fundstellen und Status:**
> - Kind: `vermoegen.freibetrag_kind` = 20'000, Fundstelle sg-stg-2025__art-64 (StG SG) · ☑️ agent-geprüft, Abnahme offen
> - Ehepaar: `vermoegen.freibetrag_verheiratet` = 150'000, Fundstelle sg-wl-2025__c0118 (Wegleitung) · ☑️ agent-geprüft, Abnahme offen
> - Alleinstehend (zum Vergleich): 75'000, sg-stg-2025__art-64 · ☑️
> 
> Hinweis: Den Art. 64 StG SG habe ich über die Wert-Abfrage belegt, nicht im Volltext geöffnet. Die Werte stehen noch unter Abnahme.

## q25

**Frage:** Welcher Verzugszins gilt 2026 für die direkte Bundessteuer?

**Soll (Referenz):** 4.00 % (RS 2-215, bund-rs-2-215__c0010/c0011).

**Antwort des Agenten** (21.5 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Bund · Steuerjahr 2026**
> 
> Der Verzugs- und Rückerstattungszins für die direkte Bundessteuer beträgt **4,00 %** (2025: 4,50 %).
> 
> - Fundstelle: `bund-rs-2-215__c0010` („Verzugs- und Rückerstattungszins 4,50 4,00“)
> - Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen)
> 
> Ergänzend für den Bund 2026:
> - Vergütungszins für Vorauszahlungen: 0,00 % (2025: 0,75 %), Fundstelle `bund-rs-2-215__c0010`, ☑️
> - Einen Ausgleichszins kennt der Bund nicht.
> 
> Die Zinssätze sind nur für den Bund angegeben. Falls Sie einen Kanton meinen, nennen Sie ihn bitte (z. B. «TG: …»); die kantonalen Ausgleichszinse weichen ab.

## q26

**Frage:** Wann wird der Eigenmietwert abgeschafft und gilt das schon für 2026?

**Soll (Referenz):** Abschaffung per 1.1.2029 (Bundesratsbeschluss 01.04.2026); für 2025–2028 gilt bisheriges Recht – 2026 also noch Eigenmietwert.

**Antwort des Agenten** (25.4 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__wert):

> **Bund · Steuerjahr 2026** (kein Kanton genannt)
> 
> **Wann:** Der Bundesrat hat die Abschaffung des Eigenmietwerts auf **1. Januar 2029** in Kraft gesetzt. Die Medienmitteilung stammt vom 1. April 2026 (`bund-mm-eigenmietwert-abschaffung__c0001`, `__c0002`; Status ☑️ agent-geprüft, Abnahme offen).
> 
> **Gilt schon 2026?** Nein. Der Eigenmietwert bleibt für 2026 steuerbar. Massgebend ist die Rechtslage 2026, die Abschaffung gilt erst ab Steuerperiode 2029.
> 
> **Was 2026 trotzdem gilt (Bund):**
> - Der Eigenmietwert wird als Einkommen im Formular erfasst (Formular 2, 2026, Ziff. 6–9, `bund-form-2-2026__c0007`).
> - Der Pauschalabzug für Liegenschaftskosten beträgt 20 % des Brutto-Eigenmietwerts, wenn das Gebäude zu Beginn der Steuerperiode mehr als 10 Jahre alt ist, sonst 10 % (`bund-lkv__art-5`). Pauschal oder effektiv wählbar pro Periode und Liegenschaft.
> 
> **Kantonal:** Der Eigenmietwert wird für die direkte Bundessteuer im kantonalen Verfahren festgesetzt, und die Kantone wenden darauf unterschiedliche Abzüge an. Für 2026 (☑️ agent-geprüft) gilt laut Wiki:
> - ZH: 10 % Abzug (Liegenschaften bis Baujahr 2025 nach Weisung 2009)
> - SG: 30 % Herabsetzung
> - TG: 40 % Selbstnutzungsabzug (Bund: 20 %)
> - AR: 20 % Abzug
> 
> Nenn mir den Kanton, dann prüfe ich die genaue Regelung und die Bundesspalte für dein Steuerjahr. Der Kanton ist auch nötig, falls du wissen willst, was für dich konkret gilt.

## q27

**Frage:** Zitiere die Regel zum Abzug privater Schuldzinsen im DBG (Steuerjahr 2025) mit Artikel.

**Soll (Referenz):** Art. 33 Abs. 1 lit. a DBG (Fassung 2025): private Schuldzinsen im Umfang der steuerbaren Vermögenserträge (Art. 20, 20a, 21) und weiterer CHF 50'000.

**Antwort des Agenten** (23.9 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Bund · Steuerjahr 2025**
> 
> **Art. 33 Abs. 1 lit. a DBG** (Fundstelle: `bund-dbg-2025__art-33-t1`):
> 
> > «Von den Einkünften werden abgezogen: a. die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken. Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten oder ihr sonst wie nahe stehenden natürlichen Person zu Bedingungen gewährt, die erheblich von den im Geschäftsverkehr unter Dritten üblichen Bedingungen abweichen»
> 
> Kurz: Private Schuldzinsen sind bis zur Höhe der steuerbaren Vermögenserträge (Art. 20, 20a, 21 DBG) plus 50 000 Franken abziehbar. Ausgenommen sind Schuldzinsen für Darlehen einer Kapitalgesellschaft an eine ihr nahestehende natürliche Person, wenn die Konditionen deutlich von Drittüblichem abweichen.
> 
> Der Text stammt aus dem Wiki-Chunk zum DBG 2025 und ist als gültig bis 31.12.2025 markiert. Ich habe ihn nicht gegen die Fedlex-Originalfassung abgeglichen.

## q28

**Frage:** Ist ein Leasingvertrag für das Privatauto steuerlich relevant? Was ist mit den Leasingraten?

**Soll (Referenz):** Leasingraten sind keine Schuldzinsen und grundsätzlich nicht abziehbar (Lebenshaltung); relevant nur für Fahrkosten-Begründung/Geschäftsauto, Vermögen (kein Eigentum).

**Antwort des Agenten** (24.4 s · Tools: 0 Aufrufe ):

> Dafür brauche ich den Kanton. Die Antwort hängt davon ab, welche Fahrkosten-Regeln dort gelten, und ich nehme keinen Kanton an. Bitte schreib z. B. «ZH: …», «SG: …», «TG: …» oder «AR: …». Das Steuerjahr nehme ich, falls du nichts angibst, als 2025 an und nenne es dann in der Antwort.
> 
> Dann prüfe ich:
> 
> - **Leasingvertrag selbst:** Ob und wo er in der kantonalen Steuererklärung relevant ist, etwa bei Vermögen oder Schulden. Ein geleastes Fahrzeug gehört dir nicht, deshalb steht es normalerweise nicht im Fahrzeugvermögen.
> - **Leasingraten für ein Privatauto:** Ob sie als Gewinnungskosten abziehbar sind. Ich erwarte, dass Privatfahrzeugkosten grundsätzlich nicht abziehbar sind, aber das prüfe ich mit dem Wiki und nenne die Fundstelle. Ausnahme ist der Arbeitsweg: Dafür gibt es die Fahrkosten-Regel mit kantonalen Limiten, und die hängt vom Kanton ab.
> 
> Was ist außerdem im Spiel: Wird das Auto auch geschäftlich genutzt, oder nur privat?

## q29

**Frage:** Wie hoch ist der Kinderabzug im Kanton Bern 2025?

**Soll (Referenz):** Nicht im Wiki (nur Bund, AR, SG, TG, ZH).

**Antwort des Agenten** (20.4 s · Tools: 0 Aufrufe ):

> Der Kanton Bern ist nicht im Steuer-Wiki. Abgedeckt sind nur der Bund sowie die Kantone AR, SG, TG und ZH, deshalb kann ich den Kinderabzug für Bern 2025 nicht angeben. Ich habe dafür auch keinen Wert geschätzt oder aus einem anderen Kanton übernommen.
> 
> Falls du den Kinderabzug in einem der abgedeckten Kantone brauchst, sag mir den Kanton (AR, SG, TG oder ZH), dann schlage ich ihn für 2025 nach. Für den Bund kann ich den Wert ebenfalls nachschlagen.

## q30

**Frage:** Ehepaar TG 2025, beide angestellt (Nettolohn 80'000 und 30'000), pendelt mit ÖV-Abo (CHF 1'200 bzw. 900). Erstelle die Abzüge Berufskosten (Fahrkosten, Verpflegung ohne Kantine, Pauschale übrige) je Person für Kanton und Bund mit Fundstellen.

**Soll (Referenz):** TG 2025 je Person: Fahrkosten = ÖV-Abo effektiv (1'200 bzw. 900; Max. 6'000 Staat / 3'300 Bund); Verpflegung ohne Kantine 15/Tag, max. 3'200 (beide Ebenen); übrige Pauschale 3 %: P1 80'000 → 2'400, P2 30'000 → 900 → Minimum 2'000 (beide Ebenen, BKV TG § 4a / BKV Bund).

**Antwort des Agenten** (36.1 s · Tools: 9 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **TG · Steuerjahr 2025**: Berufskosten Ehepaar, Kanton und Bund
> 
> Beide Pauschalen und Fahrkosten liegen unter den Maximalbeträgen, deshalb sind Kanton und Bund hier identisch. Die Verpflegung kann ich noch nicht beziffern (Angaben fehlen, siehe unten).
> 
> | Position | Person 1 (Nettolohn 80'000) | Person 2 (Nettolohn 30'000) | Form. / Fundstelle |
> |---|---|---|---|
> | Fahrkosten ÖV-Abo | 1'200 | 900 | TG Form. 4.2 Ziff. 2.1 (Code 206 / 246); `tg-form-04-2-2025__c0002` |
> | Verpflegung ohne Kantine | offen | offen | TG Form. 4.2 Ziff. 3.1 (Code 214 / 254); `tg-form-04-2-2025__c0003`, `tg-bkv__par-2-t1` |
> | Pauschale übrige Berufskosten | 2'400 | 2'000 (Minimum) | TG Form. 4.2 Ziff. 4 (Code 220 / 260); `tg-form-04-2-2025__c0004`, `tg-bkv__par-4a` |
> | **Summe ohne Verpflegung** | **3'600** | **2'900** | Ziff. 10.1 (Code 240) / Ziff. 10.2 (Code 280) |
> 
> **Kanton und Bund** (identische Beträge):
> - **Fahrkosten:** Max. Kanton CHF 6'000, Bund CHF 3'300 pro Person (`tg-stg__par-29`, `bund-dbg-2025__art-26`). Beide nicht erreicht.
> - **Pauschale:** 3 % vom Nettolohn (Lohnausweis Ziff. 11), min. CHF 2'000, max. CHF 4'000. Bund identisch (`bund-bkv-2025__anhang-1`). Ich habe den Nettolohn als Ziff. 11 des Lohnausweises angenommen.
> 
> **Verpflegung (offen):**
> - Ohne Kantine/Verbilligung: CHF 15 pro auswärtiger Hauptmahlzeit, max. CHF 3'200 pro Person und Jahr (`tg-bkv__par-2-t1`, `bund-bkv-2025__anhang-1`). Voraussetzung: Heimkehr mittags unzumutbar. Abzug = 15 × Arbeitstage.
> - Mit Verbilligung durch Arbeitgeber oder Kantine: CHF 7.50 pro Tag, max. CHF 1'600 (`tg-bkv__par-2-t2`, `bund-wl-2a-2025__c0045`).
> - Sicher ist nur die Obergrenze: 3'200 bzw. 1'600. Welcher Fall gilt, hängt von den Lohnausweisen ab (Feld G) und davon, ob Mittagessen vergütet wird.
> 
> **Was ich noch brauche:**
> 1. Arbeitstage und Pensum je Person (Teilzeit wird gekürzt).
> 2. Lohnausweis Feld G (verbilligte Verpflegung) und Feld F (Geschäftsfahrzeug; hier nicht angenommen).
> 3. Ob Heimkehr am Mittag zumutbar ist.
> 4. Ob der Arbeitgeber das ÖV-Abo ganz oder teilweise vergütet. Dann entfällt der Abzug für diesen Teil.
> 
> **Hinweise:**
> - Alle Werte sind laut Wiki «agent-geprüft», die Abnahme steht noch aus.
> - Belege: ÖV-Abo-Quittungen und Lohnausweise einreichen. Ob die Abo-Belege einzureichen sind, ist im Wiki als «unklar» markiert.
> - Die Wegleitung nennt für den Bund noch 3'200 als Fahrkostenmaximum, das Gesetz 3'300. Das ist hier ohne Auswirkung, da die Abzüge darunter liegen.

## q31

**Frage:** Ehepaar ZH 2026, beide erwerbstätig, Kind 3 Jahre in der Kita (Kosten CHF 30'000). Wie viel Drittbetreuung ist abziehbar (Kanton und Bund)?

**Soll (Referenz):** ZH 2026 Kanton max. CHF 25'300 pro Kind (zh-stg-2026__par-31-t3); Bund 2026 max. CHF 25'800 (bund-dbg-2026__art-33-t7). Abzug je Ebene getrennt.

**Antwort des Agenten** (24.6 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **ZH · Steuerjahr 2026**
> 
> Bei nachgewiesenen Kosten von CHF 30'000 für ein Kind (3 Jahre) sind abziehbar:
> 
> - **Kanton Zürich (Staatssteuer): CHF 25'300**, also der Höchstbetrag, weil min(30'000; 25'300) = 25'300.
> - **Bund (direkte Bundessteuer): CHF 25'800**, also der Höchstbetrag, weil min(30'000; 25'800) = 25'800.
> 
> Die beiden Beträge werden separat deklariert. Die Differenz von CHF 4'200 bzw. 4'700 zu den CHF 30'000 ist nicht abziehbar.
> 
> **Voraussetzungen, die hier erfüllt sind**
> - Kind unter 14 Jahren im gleichen Haushalt (Kanton und Bund: 14. Altersjahr noch nicht vollendet).
> - Beide Eltern sind erwerbstätig und die Kosten stehen im direkten Zusammenhang mit der Erwerbstätigkeit.
> - Nur Kosten während der Arbeitszeit zählen. Falls die Kita-Rechnungen auch Ferien- oder andere nicht arbeitsbedingte Betreuung enthalten, muss der Anteil herausgerechnet werden.
> 
> **Formular und Belege**
> - Kanton: Ziff. 16.6 «Abzug für fremdbetreute Kinder», Code 376, Bundesspalte separat.
> - Belege: Kita-Rechnungen mit Zahlungsnachweis und eine Aufstellung der Fremdbetreuungskosten mit Empfängern. Bei angestellter Betreuungsperson zusätzlich eine Kopie des Lohnausweises.
> - Die 20%-Kürzung als Lebenshaltungskosten gilt nur für pauschal ausgewiesene Betreuungskosten. Bei Kita-Rechnungen fällt sie weg.
> 
> **Quellen und Status**
> - ZH: zh-stg-2026__par-31-t3 (Limite 25'300), zh-form-300-2026-uj__c0008 und zh-wl-2026-uj__c0105 (Formular/Wegleitung). Status ☑️ agent-geprüft, Abnahme offen.
> - Bund: bund-dbg-2026__art-33-t7 (Limite 25'800). Status ☑️ agent-geprüft, Abnahme offen.
> - Die reguläre Formular-Fassung ZH 2026 ist laut Wiki noch nicht publiziert. Die Ziffer 16.6 stützt sich auf die Fassung für unterjährige Steuerpflicht. Die Ziffer und den Code bitte am definitiven Formular prüfen.

## q32

**Frage:** SG 2025: Einfamilienhaus (Baujahr 2010), selbst bewohnt. Pauschalabzug Liegenschaftsunterhalt Kanton und Bund?

**Soll (Referenz):** SG 2025: 20 % des Eigenmietwerts, ohne Altersstaffel (sg-stv__art-29); Bund: Gebäude zu Beginn 2025 über 10 Jahre alt → 20 % (bund-lkv__art-5).

**Antwort des Agenten** (26.2 s · Tools: 2 Aufrufe steuerwiki__wert):

> **SG · 2025**
> 
> **Kanton (St. Gallen):** Pauschale **20 %**, unabhängig vom Gebäudealter. Die Basis ist der Eigenmietwert, weil die Liegenschaft selbst bewohnt wird. Fundstelle: `sg-stv__art-29`. Status: ☑️ agent-geprüft (Abnahme offen).
> 
> **Bund (direkte Bundessteuer):** Pauschale **20 %**. Massgebend ist das Gebäudealter zu Beginn der Steuerperiode (1.1.2025). Ein Gebäude mit Baujahr 2010 ist 15 Jahre alt und liegt damit über der 10-Jahres-Grenze. Der Satz von 10 % gilt nur bis zehn Jahre. Fundstelle: `bund-lkv__art-5`. Status: ☑️ agent-geprüft (Abnahme offen).
> 
> **Offene Punkte:**
> - **Bemessungsgrundlage im Kanton:** Das Tool nennt «angerechneter Eigenmietwert», sagt aber nicht, ob die 30-%-Reduktion für selbstbewohntes Wohneigentum (`sg-stg-2025__art-34`) vor oder nach der Pauschale abgezogen wird. Ob die 20 % auf den reduzierten oder den unreduzierten Eigenmietwert angewendet werden, ist im Chunk nicht belegt. Bitte vor dem Ausfüllen prüfen. Beim Bund gibt es keine eigene 30-%-Reduktion; dort ist die Basis der Brutto-Eigenmietwert.
> - **Wahlrecht:** Pauschale oder effektive Kosten können je Steuerperiode und Liegenschaft gewählt werden. Bei tatsächlich hohen Unterhaltskosten kann sich der Einzelnachweis lohnen.

## q33

**Frage:** ZH 2025: Kind 19 Jahre, in Lehre (Ausbildung). Kinderabzug Kanton und Bund?

**Soll (Referenz):** ZH 2025 Kanton CHF 9'300 (volljährig in Erstausbildung, zh-stg-2025__par-34); Bund CHF 6'800 (bund-dbg-2025__art-35) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (27.9 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **ZH · Steuerjahr 2025**
> 
> Ja, für ein volljähriges Kind in Lehre (berufliche Erstausbildung) gilt der Kinderabzug, in beiden Steuern gleich wie für Minderjährige.
> 
> - **Kanton ZH:** CHF 9'300 Abzug vom Einkommen (§ 34 Abs. 1 lit. a StG). ☑️ agent-geprüft, Abnahme offen. Fundstelle: zh-stg-2025__par-34.
> - **Bund:** CHF 6'800 Abzug vom Einkommen (Art. 35 Abs. 1 lit. a DBG). ☑️ agent-geprüft, Abnahme offen. Fundstelle: bund-dbg-2025__art-35.
> - **Bund, zusätzlich:** Ermässigung des Steuerbetrags um CHF 263 pro Kind (Art. 36 Abs. 2bis DBG). Das gilt im Elterntarif, also bei Ehepaaren und Alleinstehenden mit Kindern im gleichen Haushalt. ☑️ agent-geprüft, Abnahme offen. Fundstelle: bund-dbg-2025__art-36-t4.
> 
> Der Kinderabzug vom Einkommen und die Steuerbetrag-Ermässigung gelten beide, sie sind nicht dasselbe.
> 
> **Voraussetzungen (ZStB 34.1, bis 2025):**
> - Die Ausbildung ist nur dann berufliche Ausbildung, wenn ein Lehrvertrag besteht (Rz. 9).
> - Das Kind muss auf die Unterstützung der Eltern angewiesen sein (Rz. 12). Der Chunk ist an dieser Stelle abgeschnitten. Ob ein Lehrlohn die Angewiesenheit ausschliesst, habe ich nicht geprüft.
> - Die Unterhaltszahlung muss zur Hauptsache beim Steuerpflichtigen liegen. Bei getrennten oder geschiedenen Eltern gelten besondere Regeln (ZStB 34.1 Rz. 20–23).
> 
> **Weitere Abzüge pro Kind, falls Sie sie brauchen:** Versicherungsabzug ZH CHF 1'300, Bund CHF 700.
> 
> Zum Ausfüllen: Ziff. 24.1 im Formular ZH 2025 (Code 370 für Kinder im Haushalt, Code 372 für Kinder ausserhalb). Für die Angewiesenheit bei Lehrlohn kann ich die Fundstelle als Nächstes genauer prüfen.

## q34

**Frage:** ZH 2025: Lohnausweis Feld G angekreuzt (Kantine). Welche Verpflegungspauschale gilt und in welche Ziffer des Berufsauslagenformulars?

**Soll (Referenz):** Verbilligte Verpflegung: CHF 7.50 pro Arbeitstag, max. CHF 1'600 pro Jahr (LS 631.33, zh-pauschalierung-berufsauslagen-2025__c0004); Form. 360 Ziff. 2.1 (verbilligt); Bund gleich.

**Antwort des Agenten** (25.8 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__beleg):

> **ZH · 2025**
> 
> **Verpflegungspauschale: CHF 7.50 pro Arbeitstag, höchstens CHF 1'600 pro Jahr.** Das ist der verbilligte Abzug, der bei Kantine, Personalrestaurant, Barbeitrag oder Essensgutscheinen gilt, wenn trotzdem Mehrkosten entstehen. Feld G ist angekreuzt, also greift dieser Satz und nicht der volle Abzug (CHF 15/Tag, max. CHF 3'200).
> 
> **Ziffer im Formular:** Form. 360 (Hilfsblatt Berufskosten), **Ziff. 2.1 verbilligt**, **Code 206** für Person 1 (Code 226 für Person 2). Der Betrag steht in der Spalte Staatssteuer und in der Spalte Bundessteuer.
> 
> **Rechnung:** min(Arbeitstage × 7.50; 1'600). Die Arbeitstage mit auswärtiger Verpflegung stehen im Arbeitszeitnachweis. Ich kenne sie nicht, deshalb kann ich den Betrag nicht beziffern.
> 
> **Bund:** Für den Regelfall Kantine/Lunch-Checks ist der Bundesbetrag gleich (CHF 7.50/Tag, CHF 1'600/Jahr). Die 7.50 und die 1'600 sind bereits der halbe Abzug, also nicht nochmals halbieren. Beim Barbeitrag gilt beim Bund kein halber Abzug. Dafür ist die Ausnahme nach BKV Art. 6 Abs. 2/3 zu prüfen.
> 
> **Zu beachten:**
> - Der Abzug gilt nur, wenn die Pause keine Heimkehr erlaubt. Bei Mittagsheimfahrt entfällt der Verpflegungsabzug.
> - Ziff. 2.1 verbilligt ist nicht kumulierbar mit Ziff. 2.1 voll oder Ziff. 2.2 (Schicht).
> - Im Lohnausweis Ziff. 15 steht vielleicht «Mittagessen durch Arbeitgeber bezahlt». Das ist ein Hinweis, den Abzug zu prüfen, aber kein eigenes Feld.
> 
> **Status:** Fundstelle geprüft (zh-form-360-2025__c0003, zh-pauschalierung-berufsauslagen-2025__c0004), Abnahme noch offen (☑️).

## q35

**Frage:** SG 2025: Kapitalbezug Säule 3a CHF 100'000. Wird das mit dem übrigen Einkommen besteuert? Wo deklarieren?

**Soll (Referenz):** Nein – Kapitalleistungen aus Vorsorge werden getrennt vom übrigen Einkommen (separate Jahressteuer) besteuert; SG Formular 1 Ziff. 40.1 (Säule 3a), Total Ziff. 41.

**Antwort des Agenten** (28.4 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__suche):

> **SG · 2025**
> 
> **Nein, die CHF 100'000 werden nicht mit dem übrigen Einkommen besteuert.** Kapitalleistungen aus Säule 3a werden gesondert vom übrigen Einkommen besteuert, mit einer separaten Jahressteuer. Das steht in der Weisung SG 2025, Ziff. 40 (`sg-wl-2025__c0119`). ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen.
> 
> **Tarife (separate Steuer):**
> - **Kanton SG:** einfache Steuer 2,2 % für Alleinstehende bzw. 2,0 % für Ehegatten. Der Ehegattensatz gilt auch für Alleinstehende, die mit Kindern oder unterstützten Personen zusammenleben. Ohne allgemeine und Sozialabzüge (`sg-form-1-2025__c0014`, Limite tarif.kapitalleistung_vorsorge).
> - **Bund:** ein Fünftel der ordentlichen Tarife nach Art. 36 DBG, ohne Sozialabzüge (`bund-ks-30__c0071`, `bund-dbg-2025__art-38`).
> 
> Ich habe keinen Steuerbetrag berechnet. Der Kantonssatz ist eine Stufe vor dem Steuerfuss der Gemeinde, und die Bundestarife habe ich nicht aus der Quelle gelesen. Eine Zahl kann ich nachreichen, wenn du Wohnsitz am 31.12. und Zivilstand angibst.
> 
> **Wo deklarieren (Formular 1 SG 2025):**
> - **Ziff. 40.1** «aus gebundener Vorsorge Säule 3a», im Abschnitt «Weitere Angaben». Dort wird der Betrag der 2025 erhaltenen Kapitalleistung eingetragen.
> - **Nicht** in Ziff. 6.4 (Einkommen). Die Angabe dient nur der Information, die Steuer rechnet die Steuerbehörde separat.
> - **Beleg:** Bescheinigung der Bank oder Versicherung über die Kapitalauszahlung 2025 (`sg-form-1-2025__c0014`). Die Bescheinigung ist einzureichen.
> - **Bund:** Das Formular hat nur eine Spalte. Abweichungen für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor (Merkblatt 32, `sg-wl-2025__c0173`).
> 
> Hinweis: Bei mehreren Auszahlungen 2025 wird der Gesamtbetrag angegeben.

## q36

**Frage:** ZH 2025: Geschiedener Mandant zahlt Unterhaltsbeiträge an die Ex-Frau (CHF 24'000) und für das minderjährige Kind (CHF 12'000). Was ist abziehbar, in welcher Ziffer?

**Soll (Referenz):** Ex-Ehefrau CHF 24'000 voll abziehbar, Ziff. 13.1 (Code 254); Kinderalimente CHF 12'000 abziehbar bis und mit Monat der Volljährigkeit, Ziff. 13.2 (Code 255); Empfänger versteuert; Bund gleich (Art. 33 Abs. 1 lit. c DBG).

**Antwort des Agenten** (31.5 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__suche, steuerwiki__zeige):

> **ZH · Steuerjahr 2025**
> 
> Beide Beträge sind abziehbar, aber in zwei verschiedenen Ziffern:
> 
> | Zahlung | Ziffer | Code | Abzug |
> |---|---|---|---|
> | CHF 24'000 an die Ex-Frau | 13.1 Unterhaltsbeiträge an den geschiedenen Ehegatten | 254 | voll abziehbar |
> | CHF 12'000 für das minderjährige Kind | 13.2 Unterhaltsbeiträge für minderjährige Kinder | 255 | abziehbar bis und mit dem Monat, in dem das Kind 18 wird |
> 
> **Ziff. 13.1 (Code 254):** Für den Ehegatten persönlich bestimmte periodische Beiträge sind voll abziehbar. Kanton und Bund sind gleich (Rechnen-Regel laut Formular: «Kanton = Bund»). Die Ex-Frau versteuert die Beiträge in Ziff. 5.1 (Code 160), Korrespondenzprinzip.
> 
> **Ziff. 13.2 (Code 255):** Kinderalimente sind nur bis und mit dem Monat abziehbar, in dem das Kind das 18. Altersjahr erreicht. Spätere Zahlungen sind nicht mehr abziehbar. Stattdessen steht dem Zahlenden ab dem Folgemonat der Kinderabzug zu (Ziff. 24.1). Für die Bundessteuer gilt zusätzlich: nur familienrechtlich geschuldete und effektiv bezahlte Alimente; freiwillige Zahlungen fallen weg.
> 
> **Offene Punkte:**
> - **Geburtsdatum des Kindes:** Ob der ganze Betrag von CHF 12'000 abziehbar ist, hängt davon ab, wie viele Monate des Jahres 2025 das Kind noch minderjährig bis zum Monat des 18. Geburtstags war. Ich brauche das Geburtsdatum, um den abziehbaren Teil zu bestimmen.
> - **Zahlungsnachweise:** Die Belegpflicht für 13.1/13.2 ist strittig (Entscheidungsvorlage Nr. 11). Lege die Bank- bzw. Zahlungsbelege bei, dann ist man auf der sicheren Seite. Die Entscheidung liegt bei der Fachperson.
> - **Vereinbarung:** Der Abzug setzt ein Scheidungsurteil oder eine Unterhaltsvereinbarung voraus. Dieses Dokument sollte vorliegen.
> 
> Quellen: Formular ZH 2025 Ziff. 13.1/13.2 (zh-form-300-2025__c0007), WL ZH 2025 Ziff. 13 (zh-wl-2025__c0076). Status beider Ziffern: ☑️ agent-geprüft, Abnahme offen.

## q37

**Frage:** TG 2025: Mandant bringt Steuerberatungsrechnung, Kreditkartenabrechnung, Mietvertrag und Motorfahrzeugversicherung. Was davon ist relevant?

**Soll (Referenz):** Steuerberatungsrechnung: nein; Motorfahrzeugversicherung: nein; Kreditkartenabrechnung: bedingt (nur als Nachweis/Schuld per 31.12.); Mietvertrag: bedingt (Wochenaufenthalt/Arbeitszimmer/Adressnachweis) – laut belege-relevanz.

**Antwort des Agenten** (30.7 s · Tools: 5 Aufrufe steuerwiki__ablage, read):

> **Thurgau · Steuerjahr 2025**
> 
> | Dokument | Steuerrelevant? | Kategorie | Eingereicht? |
> |---|---|---|---|
> | Steuerberatungsrechnung | **Nein** | Keine Steuerbeleg-Kategorie | – |
> | Kreditkartenabrechnung | **Bedingt** | Belege Sonstiges, falls ein Abzug darauf beruht | Nein (Einreichepflicht TG unklar) |
> | Mietvertrag | **Bedingt** | Belege Sonstiges, nur bei Abzug/Ertrag | Nein (Einreichepflicht TG unklar) |
> | Motorfahrzeugversicherung | **Nein** | Keine Steuerbeleg-Kategorie | – |
> 
> **Steuerberatungsrechnung – nicht relevant.** Kosten für Steuerberatung und Erstellung der Steuererklärung im Privatvermögen sind nicht abziehbar. Die Fundstelle (`bund-wl-2a-2025__c0057`) ist Bundesrecht. Eine TG-Fundstelle habe ich nicht separat geprüft.
> 
> **Kreditkartenabrechnung – bedingt.** Die Abrechnung selbst ist kein Steuerbeleg. Sie ist nur Nachweis für einzelne abziehbare Zahlungen, etwa Spenden, Krankheitskosten, Weiterbildung oder Berufsauslagen, wenn die Originalbelege fehlen. Relevant sind auch Schuldzinsen (`tg-wl-2025__c0171`, Form. 4.1 A). Die Passage zu Sollzinsen war im Wiki-Ergebnis abgeschnitten; ich habe sie nicht geöffnet.
> - Falls eine Position abgezogen wird: Belege Sonstiges, Eingereicht = nein.
> - Falls nichts daraus abgezogen wird: keine Ablage.
> 
> **Mietvertrag – bedingt.** Der Mietzins der selbstbewohnten Wohnung ist Lebenshaltung und nicht abziehbar. Relevant wird er nur bei Untervermietung (Nettoertrag ist steuerbar) oder bei einem Wochenaufenthalt am Arbeitsort (Mehrkosten der Unterkunft). Dann: Belege Sonstiges. Die Einreichepflicht für TG 2025 konnte ich nicht klären. Ich würde den Mietvertrag vorerst als «Eingereicht = nein, Einreichepflicht offen» ablegen.
> 
> **Motorfahrzeugversicherung – nicht relevant.** Prämien sowie Verkehrssteuern, Treibstoff und Unterhalt des Privatfahrzeugs sind Lebenshaltungskosten. Das Wiki stuft das mit hoher Sicherheit ein. Die TG-Fundstelle (`tg-wl-2025__c0123`) ist im Ergebnis nur ausschnittsweise sichtbar, deshalb habe ich sie nicht vollständig geprüft.
> 
> **Offen:**
> - Die Einreichepflicht der Kreditkarten- und Mietunterlagen im Kanton TG 2025 muss anhand der Wegleitung geprüft werden.
> - Die Kategorieliste ist von consis noch nicht bestätigt. Die Zuordnung «Belege Sonstiges» beruht auf dieser Liste.
> - Alle Einordnungen sind agent-geprüft, die Abnahme durch die Fachperson steht aus.

## q38

**Frage:** AR 2026: Wie hoch ist der Kinderabzug für ein 10-jähriges Kind? Ist der Wert gesichert?

**Soll (Referenz):** AR 2026: CHF 7'400 laut Anhang 1 StG (indexiert), aber Status STRITTIG (MB 02 / StG-Text nennen andere Beträge; Wegleitung 2026 fehlt) → Fachperson.

**Antwort des Agenten** (23.5 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **AR · Steuerjahr 2026**
> 
> Ein 10-jähriges Kind fällt in die Staffel «nach Vollendung des 4. bis zur Vollendung des 15. Altersjahres». Dafür gibt es zwei unterschiedliche Werte, und der Wert ist deshalb **nicht gesichert**:
> 
> - **CHF 7'400** nach Anhang 1 StG (Art. 38 Abs. 1 lit. a Ziff. 2, indexiert per 1.1.2024). Die Wegleitung AR 2025 bestätigt denselben Wert. Quelle: `ar-stg-anhang-kp__c0001`, `ar-wl-2025__c0005`.
> - **CHF 7'000** nach Merkblatt AR 02 Ziff. 2 (Fassung 25.9.2025, Stand 18.08.2026). Das ist der nicht indexierte Gesetzestext. Quelle: `ar-mb-02__c0002`.
> 
> Der Widerspruch ist im Wiki als ⚠️ strittig markiert. Für 2026 fehlt eine Wegleitung, die entscheiden könnte. Ich habe den Wert deshalb nicht als verifiziert übernommen.
> 
> **Bund (zum Vergleich, separat deklarieren):** CHF 6'800 für jedes minderjährige Kind (Art. 35 Abs. 1 lit. a DBG 2026, ☑️ agent-geprüft). Der Bund staffelt nicht nach Alter.
> 
> **Praxisrat:** Für die Steuererklärung 2026 würde ich **CHF 7'400** als Arbeitswert einsetzen, weil es die indexierte Fassung des Gesetzes ist. Bestätigen sollte das die Fachperson oder die kantonale Steuerverwaltung, bevor die Zahl endgültig übernommen wird.
> 
> Formular: Ziff. 23.2 «Kinderabzug: Kind nach Vollendung des 4. bis zur Vollendung des 15. …» (`position ar 2026 23.2` für Details).

## q39

**Frage:** Welche Vermögenssteuer-Freibeträge (Sozialabzüge) gelten 2025 in ZH für Alleinstehende und Verheiratete?

**Soll (Referenz):** ZH kennt keine Vermögens-Sozialabzüge, sondern Tarifstufen mit 0 ‰: Grundtarif erste CHF 80'000, Verheiratetentarif erste CHF 159'000 (zh-stg-2025__par-47); kein Betrag pro Kind.

**Antwort des Agenten** (23.1 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **ZH · 2025**
> 
> Im Kanton Zürich gibt es keinen eigenen Sozialabzug auf dem Vermögen. Der Freibetrag steckt in der 0‰-Stufe des Vermögenssteuertarifs (§ 47 StG ZH):
> 
> - **Alleinstehende (Grundtarif):** 0‰ auf den ersten **CHF 80'000** steuerbaren Vermögens, also steuerfrei. Quelle: `zh-stg-2025__par-47-t1`
> - **Verheiratete (Verheiratetentarif):** 0‰ auf den ersten **CHF 159'000**. Quelle: `zh-stg-2025__par-47-t2`
>   - Der Verheiratetentarif gilt laut Wiki auch für Verwitwete, gerichtlich oder tatsächlich Getrennte, Geschiedene und Ledige mit Kindern. Chunk `zh-zstb-34-1-bis-2025__c0032` (ZStB 34.1, Rz 60–62) stellt das zusammen mit der Kinderregel dar. Ich habe die Fundstellen nicht im Volltext geöffnet.
> 
> **Für das Ausfüllen:** Es gibt kein Abzugsfeld. Ziff. 35 «Steuerbares Vermögen gesamt» = Ziff. 33 − Ziff. 34, und das volle Vermögen wird eingetragen. Der Freibetrag wirkt erst bei der Steuerberechnung.
> 
> **Kinder:** Einen Vermögens-Sozialabzug pro Kind gibt es in ZH nicht. Die Kinderabzüge (WL ZH 2025, Ziff. 24.1) betreffen das Einkommen, nicht das Vermögen.
> 
> **Status:** ☑️ agent-geprüft. Die Fundstelle ist geprüft, die Abnahme durch eine Fachperson steht noch aus. Bund erhebt keine Vermögenssteuer, daher gilt das nur für den Kanton.

## q40

**Frage:** Alleinstehende TG 2026, Nettolohn 90'000, ÖV-Abo 2'400, Säule 3a 7'258, Krankenkasse 5'500. Erstelle die Abzüge (Berufskosten, 3a, Versicherungsabzug) Kanton und Bund mit Fundstellen und Status.

**Soll (Referenz):** TG 2026 (Kanton/Bund): Fahrkosten 2'400 (Max. 6'000 / 3'300); übrige Berufskosten 3 % von 90'000 = 2'700 (Min. 2'000, Max. 4'000, beide Ebenen); Säule 3a 7'258 (TG 🟡 extrahiert, Bund ☑️); Versicherungsabzug TG max. 3'500 → 3'500, Bund max. 1'800 → 1'800 (Prämien 5'500 übersteigen beide Maxima).

**Antwort des Agenten** (46.4 s · Tools: 13 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne):

> **TG · Steuerjahr 2026** (Alleinstehend, Nettolohn CHF 90'000)
> 
> | Abzug | Kanton TG (Staats- und Gemeindesteuer) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | **Fahrkosten ÖV-Abo** | **2'400** (Limite 6'000) | **2'400** (Limite 3'300) |
> | **Übrige Berufskosten** (Pauschale 3 % Nettolohn, Min. 2'000, Max. 4'000) | **2'700** | **2'700** |
> | **Säule 3a** (Limite 7'258 mit 2. Säule) | **7'258** | **7'258** |
> | **Versicherungsprämien** (Krankenkasse 5'500 gekürzt) | **3'500** (Limite Alleinstehend) | **1'800** (Limite Alleinstehend mit 3a-/2.-Säule-Beiträgen) |
> | **Summe** | **15'858** | **14'158** |
> 
> Die Summen habe ich mit `rechne` geprüft.
> 
> **Fundstellen und Status**
> 
> - **Fahrkosten TG:** Max. 6'000, `tg-wl-2026__c0176`. Status ☑️ agent-geprüft, Abnahme offen.
> - **Fahrkosten Bund:** Max. 3'300, `bund-dbg-2026__art-26`. Status ☑️ agent-geprüft, Abnahme offen.
> - **Übrige Berufskosten TG:** 3 % vom Nettolohn (gemäss Lohnausweis Ziff. 11), min. 2'000, max. 4'000, `tg-wl-2026__c0187` (WL TG 2026, Ziff. 4, S. 40). Die Wegleitung gilt für Kanton und Bund gleich. Status nicht im Tool-Output ausgewiesen; der Wert ist aus dem Chunk übernommen.
> - **Übrige Berufskosten Bund:** 3 %, min. 2'000, max. 4'000, `bund-wl-2a-2026__c0041` (WL 2a 2026, Ziff. 10). Status nicht im Tool-Output ausgewiesen.
> - **Säule 3a TG:** 7'258 mit 2. Säule, `tg-wl-2026__c0089`. Ohne 2. Säule gilt 20 % des Erwerbseinkommens, max. 36'288, `tg-wl-2026__c0004`. Status ☑️ agent-geprüft, Abnahme offen.
> - **Säule 3a Bund:** 7'258 mit 2. Säule, `bund-bsv-masszahlen-2025-2026__c0003`. Ohne 2. Säule gilt 20 %, max. 36'288, `bund-bvv3__art-7`. Status ☑️ agent-geprüft, Abnahme offen.
> - **Versicherung TG:** 3'500 für Alleinstehende, `tg-stg__par-34-t3` (StG § 34 Abs. 3). Status ☑️ agent-geprüft, Abnahme offen.
> - **Versicherung Bund:** 1'800 für Alleinstehende mit Beiträgen an 2. Säule oder 3a, `bund-dbg-2026__art-33-t2`. Status ☑️ agent-geprüft, Abnahme offen.
> 
> **Hinweise**
> 
> - **Säule 3a:** Die 20 %-Grenze ergibt 18'000 und liegt damit über 7'258. Der Abzug bleibt also 7'258, ob sie in einer Pensionskasse ist oder nicht.
> - **Versicherung:** Die Krankenkasse von 5'500 übersteigt beide Limiten. Im Kanton fallen 2'000 weg, im Bund 3'700. Bei den Kantonsbeträgen sind keine Sparzinsen enthalten, daher bleibt das Limit bindend. Der Bund-Wert gilt, weil sie 3a-Beiträge leistet.
> - **ÖV-Abo:** Die Fahrkosten sind tatsächliche Kosten (2'400, unter beiden Limiten) und gehen zusätzlich zur Pauschale.
> - **Übrige Berufskosten:** Die 3 %-Pauschale ersetzt die tatsächlichen Berufsauslagen. Man kann stattdessen nachweisen, Pauschale und Nachweis zusammen gehen aber nicht.
> - **Annahme:** 90'000 wird als Nettolohn gemäss Lohnausweis Ziff. 11 gelesen.
> - **Offen:** Wohnsitz am 31.12. ist mit TG angenommen. Ob sie Beiträge an eine 2. Säule zahlt, ist nicht angegeben. Es ändert die Bund-Versicherung nicht, da die 3a-Zahlung allein bereits den Bund-Wert 1'800 ergibt.

