# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 40 · Lauf: 2026-11-09 18:37
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q01

**Frage:** Mandantin (ZH, 2025) bringt: Lohnausweis, Krankenkassen-Prämienrechnung, Handyrechnung, 3a-Bescheinigung, Hausratversicherungspolice, Spendenquittung Rotes Kreuz CHF 80, Kita-Rechnungen. Welche sind relevant, wofür?

**Soll (Referenz):** Relevant: Lohnausweis (Einkünfte 1.1), Krankenkassenprämien (Versicherungsabzug Ziff. 15, Form. 365), 3a-Bescheinigung (Ziff. 14), Kita-Rechnungen (Ziff. 16.6 Drittbetreuung, max. 25'000 Kanton / 25'800 Bund). Spende CHF 80: unter Mindestbetrag 100 → nicht abziehbar (sofern Total < 100). Nicht relevant: Handyrechnung (Lebenshaltung), Hausratversicherung (kein Versicherungsabzug).

**Antwort des Agenten** (35.4 s · Tools: 8 Aufrufe read, steuerwiki__ablage):

> Ich ordne die sieben Dokumente für ZH 2025 ein und lese dazu die Kategorienliste.
> 
> **ZH · 2025**: Relevant sind Lohnausweis, 3a-Bescheinigung und Krankenkassen-Prämien. Die Spende ist nur unter Bedingungen relevant. Hausrat und Alltagsrechnungen sind nicht steuerrelevant.
> 
> | Dokument | Steuerrelevant? | Wofür / Ziffer (ZH 2025) | Einreichen? | Kategorie (KATEGORIEN.md) |
> |---|---|---|---|---|
> | **Lohnausweis** | ja | Einkommen; Ziff. 1.1, 1.2, Form. 360 Ziff. 2–5, Form. 367 | **ja**, immer (§ 134 Abs. 1 lit. a StG) | Belege eingereicht (eingereicht: ja) |
> | **Krankenkassen-Prämienrechnung** | ja | Versicherungsprämien; Ziff. 15, Form. 365 Teil A Ziff. 1–4 und 6 | auf Verlangen (Formular ist beizulegen) | Belege Sonstiges (eingereicht: nein) |
> | **3a-Bescheinigung** | ja | Säule-3a-Abzug; Ziff. 14.1/14.2 (ab 2026 Ziff. 14.3) | **ja** | Belege eingereicht (eingereicht: ja) |
> | **Spendenquittung Rotes Kreuz, CHF 80** | bedingt | Ziff. 22.2 | auf Verlangen (Liste aller Zuwendungen beilegen) | Belege Sonstiges (eingereicht: nein) |
> | **Kita-Rechnungen** | bedingt | Kinderbetreuungskosten; Ziff. 16.6 | auf Verlangen; die Aufstellung der bezahlten Kosten mit Empfängern ist unaufgefordert beizulegen | Belege Sonstiges (eingereicht: nein) |
> | **Hausratversicherungspolice** | nein | keine Position | – | keine Steuerbeleg-Kategorie |
> | **Handyrechnung** | nein (privat) | keine Position | – | keine Steuerbeleg-Kategorie |
> 
> **Erläuterungen**
> 
> - **Lohnausweis:** Pflicht zur Einreichung, auch für Nebenerwerb und VR-Honorare.
> - **Krankenkassen-Prämien:** Die Prämienbelege selbst sind nicht ausdrücklich verlangt; das Formular Versicherungsprämien ist beizulegen. Die Krankenkassen-Leistungsabrechnung ist nur relevant, wenn Krankheits- oder Unfallkosten über dem Selbstbehalt von 5 % des Nettoeinkommens geltend gemacht werden (Ziff. 22.1). Sie gehört dann ebenfalls zu Belege Sonstiges.
> - **Spende CHF 80:** Der Abzug setzt eine Mindestsumme von CHF 100 pro Jahr voraus (zh-info-spenden__c0003). Allein reichen CHF 80 nicht. Relevant wird die Spende nur, wenn die Zuwendungen des Jahres insgesamt mindestens CHF 100 betragen.
> - **Kita:** Abziehbar sind Kosten für Kinder unter 14 Jahren, wenn sie in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder ähnlichem stehen. Der Höchstbetrag laut Wiki ist CHF 25 000 pro Kind für die Drittbetreuung (zh-stg-2025__par-31-t4). Die Rechnungen selbst sind nicht einzureichen; verlangt ist die Kostenaufstellung mit Empfängern.
> - **Hausratpolice:** Prämien für Mobiliar- und Hausratversicherungen sind nicht abziehbar. Der Wiki-Beleg dafür stammt aus Appenzell Ausserrhoden (ar-wl-2025__c0085). Für ZH ist das nicht einzeln belegt, aber es entspricht der allgemeinen Regel.
> - **Handyrechnung:** Eine private Handyrechnung ist ein Lebenshaltungskostenbeleg und nicht abziehbar (Art. 34 lit. a DBG). Nur ein beruflich veranlasster Anteil wäre relevant. Dann bräuchte es eine Angabe zum beruflichen Anteil, etwa Selbstständigkeit oder Homeoffice mit Arbeitgeber-Nachweis.
> 
> **Offene Punkte**
> 
> - Die Kategorien stammen aus der Firmenliste und sind noch nicht bestätigt.
> - Die Zuordnung des Spendenbelegs zu Belege Sonstiges ist die Standardzuordnung für Spendenbescheinigungen; ob ein Beleg überhaupt abgelegt wird, hängt von der Jahressumme ab.
> - Bei der Handyrechnung fehlt die Information, ob ein beruflicher Anteil besteht. Ohne diese Angabe bleibt sie nicht steuerrelevant.

## q02

**Frage:** In welche Ziffer und mit welchem Code der ZH-Steuererklärung 2025 gehört der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb)?

**Soll (Referenz):** Ziff. 1.1 Haupterwerb, Code 100 (Person 1) / 101 (Person 2); Nettolohn Lohnausweis Ziff. 11 (zh-form-300-2025).

**Antwort des Agenten** (23.4 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__beleg):

> **ZH · 2025**
> 
> Der Nettolohn aus Lohnausweis Ziff. 11 gehört für Person 1 (Haupterwerb unselbständig) in **Ziff. 1.1, Code 100**. Person 2 steht in Code 101.
> 
> - **Rechnen:** Summe der Ziff. 11 aller Haupterwerbs-Lohnausweise von Person 1 (Ziff. 11 = Ziff. 8 − Ziff. 9 − Ziff. 10.1 − Ziff. 10.2). Das gilt für jeden Arbeitgeber.
> - **Bund:** Dieselbe Zeile gilt für Staats- und Bundessteuer, es gibt keinen Unterschied.
> - **Beleg:** Lohnausweis beilegen. Einreichen ist Pflicht, für jeden Arbeitgeber inkl. Nebenerwerb (§ 134 Abs. 1 lit. a StG; WL S. 31).
> - **Erwerbslücken:** Falls vorhanden, ausdrücklich bezeichnen.
> 
> Quelle: zh-form-300-2025__c0004 (Haupterwerb Person 1). Status ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen.
> 
> Achtung: Auf der Belegkarte zum Lohnausweis steht bei Ziff. 1.1 der Zusatz «nur Selbständigerwerb/Geschäftsvermögen». Das widerspricht der Positionsangabe und dem Quellchunk. Ich halte die Positionsangabe für richtig, aber bitte am Formular Form. 300 gegenprüfen, bevor du einträgst.

## q03

**Frage:** Lohnausweis Feld F ist angekreuzt (Geschäftsauto). Was bedeutet das für den Fahrkostenabzug (SG 2025)?

**Soll (Referenz):** Feld F angekreuzt → kein Fahrkostenabzug für den Arbeitsweg mit Geschäftsfahrzeug (Privatanteil im Lohn, Lohnausweis Ziff. 2.2).

**Antwort des Agenten** (31.1 s · Tools: 5 Aufrufe steuerwiki__suche, steuerwiki__position, steuerwiki__wert, steuerwiki__zeige):

> **SG · Steuerjahr 2025**
> 
> Wenn Feld F angekreuzt ist, gibt es **keinen Fahrkostenabzug** für den Arbeitsweg (Form. 4 Ziff. 1.1–1.3 bleibt leer). Feld F bedeutet, dass dem Arbeitnehmer keine Kosten entstehen, etwa bei Sammeltransport oder einem vom Arbeitgeber aus geschäftlichen Gründen bezahlten GA (Position Formular 4 / Hilfsblatt Berufskosten, ☑️ agent-geprüft, WL SG 2025 Ziff. 10.1).
> 
> Bei einem Geschäftsauto passt Feld F aber nicht ganz:
> 
> - **Privatanteil:** Bei einem Geschäftsfahrzeug werden 0,9 % des Kaufpreises (exkl. MWST) pro Monat, also 10,8 % pro Jahr, als Gehaltsnebenleistung versteuert. Damit ist auch der Arbeitsweg abgegolten, und es gibt keinen Fahrkostenabzug (WL SG 2025, `sg-wl-2025__c0076`). Der Privatanteil steht in Lohnausweis Ziff. 2.2. Die Beispiele in StB 39 Nr. 3 (Ziff. 4.2.1, `sg-stb-39-3__c0018`) nennen nur Ziff. 2.2, nicht Feld F. Der Treffer `sg-stb-39-3__c0013` enthält den Satz «kein Kreuz im Feld F» in einem anderen Zusammenhang, ich habe den vollständigen Kontext nicht gelesen.
> - **Bordbuch:** Werden die privaten Fahrten anhand eines detaillierten Bordbuchs abgerechnet, können die effektiven Arbeitswegkosten bis zum Maximalabzug geltend gemacht werden: **Kanton CHF 8'000**, **Bund CHF 3'300**. Der Privatanteil muss trotzdem im Lohnausweis stehen.
> 
> **Was zu prüfen ist:** Auf dem Lohnausweis steht Feld F angekreuzt, und Ziff. 2.2 zeigt womöglich keinen Privatanteil. Das passt nicht zusammen. Wenn der Privatanteil in Ziff. 2.2 steht, sollte Feld F leer sein, und der Fahrkostenabzug bleibt in beiden Varianten null (sofern kein Bordbuch geführt wird). Die Lohnausweis-Angaben bitte mit dem Arbeitgeber klären.
> 
> **Offen:** Die Bundesregel für den Privatanteil habe ich nicht separat geprüft. Ich habe nur den Bundes-Maximalabzug von CHF 3'300 bestätigt (`bund-dbg-2025__art-26`). Welche Ziffer des Lohnausweises genau gemeint ist, kann ich bei Bedarf mit `position sg 2025 "Lohnausweis"` nachschlagen.

## q04

**Frage:** Wie hoch ist der maximale Fahrkostenabzug 2025 in TG (Staatssteuer) und beim Bund, und welcher km-Ansatz gilt für das Auto?

**Soll (Referenz):** TG 2025 Staat max. CHF 6'000 (tg-stg__par-29), Bund max. CHF 3'300 (bund-dbg-2025__art-26); Auto TG gestaffelt 0.60/0.50/0.40 je nach Jahres-km, Bund 0.70.

**Antwort des Agenten** (23.8 s · Tools: 3 Aufrufe steuerwiki__wert):

> **TG · Steuerjahr 2025**
> 
> **Maximaler Fahrkostenabzug (Fahrten Wohn–Arbeitsstätte)**
> - **Kanton TG (Staatssteuer): CHF 6'000** pro Jahr. Der Betrag umfasst alle Fahrkosten, auch Wochenaufenthalt und Nebenerwerb. ☑️ tg-stg__par-29
> - **Bund (direkte Bundessteuer): CHF 3'300** pro Person und Jahr. ☑️ bund-dbg-2025__art-26
> 
> Die ESTV-Wegleitung 2025 (S. 6) nennt noch 3'200 Franken. Das Gesetz (Art. 26 DBG, Fassung 2025) und RS 2-210 nennen 3'300. Ich halte 3'300 für richtig, weil das Gesetz vorgeht, aber die Abweichung sollte vor der Abgabe geprüft werden.
> 
> **km-Ansatz für das Auto (Privatauto)**
> - **Kanton TG: kein fester Satz, sondern eine Staffel** nach jährlicher Fahrleistung. Sie wird stufenweise gerechnet (kumulativ):
>   - bis 3'000 km: CHF 0.60/km
>   - 3'001–5'000 km: CHF 0.50/km
>   - über 5'000 km: CHF 0.40/km
>   - Beispiel laut StP 29 Nr. 2: 8'000 km ergibt CHF 4'000.
>   - Parkgebühren sind darin enthalten. ☑️ tg-bkv__par-1
> - **Bund 2025: CHF 0.70/km** einheitlich. ☑️ bund-bkv-2025__anhang-1
> 
> Der Auto-Abzug gilt nur, wenn der öffentliche Verkehr nicht zumutbar ist. Im Normalfall werden die Kosten des ÖV-Abonnements abgezogen. Bei Privatauto-Berechnung bei 100 % Tätigkeit gelten in TG in der Regel höchstens 225 Arbeitstage pro Jahr. ☑️ tg-wl-2025__c0003
> 
> Alle Werte sind von mir gegen die Fundstellen geprüft, die Abnahme durch eine Fachperson steht aber noch aus.

## q05

**Frage:** Welcher km-Ansatz für Autos gilt 2026 bei der direkten Bundessteuer?

**Soll (Referenz):** CHF 0.75 pro km (bund-mm-2025-09-11-kalte-progression-2026__c0004; RS 2-215).

**Antwort des Agenten** (23.8 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Bund · Steuerjahr 2026**
> 
> Für ein Privatauto gilt bei der direkten Bundessteuer **CHF 0.75 pro Fahrkilometer** (Vorjahr 0.70). Der Abzug greift nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist. Der Gesamtabzug für Fahrkosten Wohn-/Arbeitsstätte ist auf **CHF 3'300** pro Jahr begrenzt.
> 
> - **Auto:** CHF 0.75/km, Fundstelle `bund-mm-2025-09-11-kalte-progression-2026__c0004`. Status ☑️ agent-geprüft, Abnahme offen.
> - **Motorrad mit weissem Kontrollschild:** CHF 0.40/km, Fundstelle `bund-rs-2-215__c0004`.
> - **Fahrrad, Motorfahrrad, Motorrad mit gelbem Kontrollschild:** Pauschale CHF 700, keine zusätzlichen Effektivkosten.
> - **Öffentliche Verkehrsmittel:** tatsächliche Kosten bis max. CHF 3'300 (Art. 26 Abs. 1 lit. a DBG, `bund-dbg-2026__art-26`).
> 
> Der Ansatz wird laut Quelle künftig an den TCS-Kilometerpreis gekoppelt und kann sich daher nach oben oder unten anpassen.
> 
> Für die Bundesrechnung brauchte ich keinen Kanton. Kantonale Formulare können eigene Regeln führen, z. B. zur Anzahl Arbeitstage. Nennen Sie den Kanton (ZH, SG, TG oder AR), dann prüfe ich, ob dort beim km-Abzug etwas abweicht.

## q06

**Frage:** Maximaler Säule-3a-Abzug 2025 für eine Arbeitnehmerin mit Pensionskasse? Und für eine Selbständige ohne 2. Säule?

**Soll (Referenz):** Mit 2. Säule CHF 7'258; ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288 (bund-bsv-masszahlen-2025-2026__c0003).

**Antwort des Agenten** (23.6 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Kanton · Steuerjahr:** Kein Kanton genannt, daher nur Bund · 2025
> 
> Die Werte gelten für die direkte Bundessteuer. Die Kantone können für ihre eigene Steuer abweichende Ansätze haben. Sagen Sie mir den Kanton (ZH, SG, TG oder AR), dann prüfe ich den kantonalen Wert.
> 
> **Säule 3a, Höchstabzug 2025 (Bund):**
> 
> - **Arbeitnehmerin mit Pensionskasse (2. Säule): CHF 7'258.** Das ist 8 % des oberen BVG-Grenzbetrags. Quelle: `bund-bsv-masszahlen-2025-2026__c0003`, Status ☑️ agent-geprüft (Abnahme offen).
> - **Selbständige ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens CHF 36'288.** Das ist 40 % des oberen Grenzbetrags. Quellen: `bund-bsv-masszahlen-2025-2026__c0003` und `bund-bvv3__art-7`, Status ☑️ agent-geprüft (Abnahme offen).
> 
> Die Selbständige erreicht den Maximalbetrag von CHF 36'288 erst bei einem Erwerbseinkommen von CHF 181'440 oder mehr. Darunter gilt die 20-%-Grenze.

## q07

**Frage:** Kinderabzug 2025 in AR für ein 10-jähriges Kind – und beim Bund?

**Soll (Referenz):** AR 2025: CHF 7'400 (4.–15. Altersjahr; Anhang 1 StG, ar-stg-anhang-kp__c0001); Bund CHF 6'800 (Art. 35 DBG) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (22.6 s · Tools: 2 Aufrufe steuerwiki__wert):

> **AR · 2025**
> 
> **Kanton AR, Ziff. 23.2 (Kind nach Vollendung des 4. bis zur Vollendung des 15. Altersjahrs): CHF 7'400** ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen)
> Quelle: ar-stg-anhang-kp__c0001, Art. 38 Abs. 1 lit. a Ziff. 2
> 
> **Bund (direkte Bundessteuer 2025):**
> - **Kinderabzug vom Einkommen: CHF 6'800** ☑️ agent-geprüft. Der Bund kennt keine Altersstaffel, der Betrag gilt für jedes minderjährige Kind (Art. 35 DBG, bund-dbg-2025__art-35).
> - **Ermässigung des Steuerbetrags: CHF 263 pro Kind** ☑️ agent-geprüft (Art. 36 Abs. 2bis DBG, bund-dbg-2025__art-36-t4). Das ist ein separater Abzug vom Steuerbetrag, nicht vom Einkommen.
> 
> Beim Bund fällt im Formular ausserdem der Versicherungszuschlag von CHF 700 pro Kind an (Art. 33 Abs. 1 lit. f DBG, bund-dbg-2025__art-33-t5). Das ist kein Kinderabzug im engeren Sinn, wird aber oft zusammen mit ihm erfasst.
> 
> Die kantonale Vermögens-Freibetragsregel für AR (CHF 25'000 pro Kind, Art. 51) gilt nur für das Vermögen. Der Bund erhebt keine Vermögenssteuer.
> 
> Die Werte stammen aus dem Wiki und sind noch nicht abgenommen. Vor dem Ausfüllen bitte die Fundstellen prüfen. Wenn du das Formularfeld wissen willst, kann ich `position ar 2025 23.2` abrufen.

## q08

**Frage:** Versicherungsabzug ZH 2025 für ein Ehepaar mit 2 Kindern, beide mit Pensionskasse (Staatssteuer und Bund)?

**Soll (Referenz):** ZH Staat: 5'800 + 2 × 1'300 = 8'400; Bund: 3'700 + 2 × 700 = 5'100 (zh-stg-2025__par-31-t2, bund-dbg-2025__art-33).

**Antwort des Agenten** (22.8 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__rechne):

> **ZH · Steuerjahr 2025**
> 
> Mit Beiträgen an die 2. Säule bzw. Säule 3a gilt für das Ehepaar mit zwei Kindern:
> 
> - **Kanton (Staatssteuer): CHF 8'400**
>   - Ehepaar: CHF 5'800 (`versicherung.verheiratet`)
>   - 2 Kinder × CHF 1'300 = CHF 2'600 (`versicherung.kind`)
>   - Fundstelle: zh-stg-2025__par-31-t2 (Ehepaar und Kinderzuschlag); Status ☑️ agent-geprüft, Abnahme offen
> - **Bund (direkte Bundessteuer): CHF 5'100**
>   - Ehepaar: CHF 3'700 (`versicherung.verheiratet`)
>   - 2 Kinder × CHF 700 = CHF 1'400 (`versicherung.kind`)
>   - Fundstelle: bund-dbg-2025__art-33-t2 und art-33-t5; Status ☑️ agent-geprüft, Abnahme offen
> 
> Die Beträge sind getrennt zu deklarieren. Die Ziffer im Formular ist Ziff. 15 (Code 270) „Versicherungsprämien und Zinsen von Sparkapitalien“. Für die Regel zum Rechnen dort: `position zh 2025 15`.
> 
> Hinweis: Die Pensionskassenbeiträge selbst sind nicht Teil dieses Versicherungsabzugs. Sie werden über den Abzug für Beiträge an die 2. Säule erfasst. Ob dafür zusätzlich ein Betrag eingesetzt wird, habe ich nicht geprüft. Ich kann das mit `position zh 2025 15` nachschlagen, falls Sie es brauchen.

## q09

**Frage:** Wie hoch ist der Kinderdrittbetreuungsabzug 2025 im Kanton ZH, und gilt 2026 ein anderer Wert?

**Soll (Referenz):** ZH 2025 CHF 25'000 (StG Nachtrag 127, zh-stg-2025__par-31-t4); 2026 CHF 25'300 (zh-stg-2026__par-31-t3). Die VKP ab 2024 (10'400) ist überholt.

**Antwort des Agenten** (23.0 s · Tools: 2 Aufrufe steuerwiki__wert):

> **ZH · Steuerjahr 2025 und 2026**
> 
> **Kanton (Staatssteuer):**
> - **2025:** max. **CHF 25'000** pro Kind
> - **2026:** max. **CHF 25'300** pro Kind, also ein Anstieg um CHF 300.
> 
> Beide Werte gelten für nachgewiesene Kosten, höchstens bis zum Maximum, bei Kindern unter 14 Jahren im gleichen Haushalt. Die Kosten müssen direkt mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit zusammenhängen. Für 2026 gilt laut Wiki bei Konkubinat oder alternierender Obhut mit gemeinsamer Sorge je der halbe Abzug (CHF 12'650).
> 
> **Bund (direkte Bundessteuer), separat zu deklarieren:**
> - **2025:** max. CHF 25'800 pro Kind
> - **2026:** max. CHF 25'800 pro Kind, also unverändert.
> 
> **Quellen und Status:**
> - ZH 2025: `zh-stg-2025__par-31-t4` (☑️ agent-geprüft, Abnahme offen)
> - ZH 2026: `zh-stg-2026__par-31-t3` (☑️ agent-geprüft, Abnahme offen)
> - Bund 2025: `bund-dbg-2025__art-33-t7`; Bund 2026: `bund-dbg-2026__art-33-t7` (beide ☑️)
> 
> **Hinweis zur Abweichung:** Die VKP ab 2024 (`zh-vkp-2024-zstb__c0005`) nennt noch CHF 10'400. Das wiki wertet das als überholt, weil das Gesetz (StG, Nachtrag 127 für 2025) und die Wegleitung 2025 übereinstimmend CHF 25'000 nennen. Die Verordnung würde ich deshalb nicht übernehmen. Ich habe den Wert nicht im Wortlaut der Fundstelle vollständig gegengeprüft, daher ist der Status «Abnahme offen».
> 
> **Formular:** ZH 2025 Ziff. 16.6 (Code 376), ZH 2026 ebenfalls Ziff. 16.6 (Code 376). Für die Rechenregel: `position zh 2025 16.6` bzw. `position zh 2026 16.6`.

## q10

**Frage:** Gibt es im Kanton TG einen Zweiverdienerabzug für die Staatssteuer?

**Soll (Referenz):** Nein, TG kennt keinen kantonalen Zweiverdienerabzug (nur Bund: 50 %, 8'600–14'100).

**Antwort des Agenten** (22.3 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Thurgau · Steuerjahr 2025** (Jahr nicht genannt, daher 2025 angenommen)
> 
> **Nein.** Im Kanton TG gibt es keinen Zweiverdienerabzug für die Staats- und Gemeindesteuern. Die Wegleitung sagt: «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.» (Fundstelle: `tg-wl-2025__c0104`, Status 🟡 extrahiert.)
> 
> **Nur der Bund kennt ihn** (direkte Bundessteuer, separat zu deklarieren):
> - Abzug: 50 % des niedrigeren Erwerbseinkommens
> - Mindestens CHF 8'600, höchstens CHF 14'100
> - Fundstelle: `bund-dbg-2025__art-33-t6`, Status ☑️ agent-geprüft (Abnahme offen)
> - Im TG-Formular 2025 steht er als Ziff. 18 (Code 356), nur für die Bundessteuer.
> 
> Die Zweiverdiener-Regeln der Steuerpraxis StP 34 Nr. 25 (Thurgau) betreffen die Mitarbeit von Ehegatten und gelten nur für den Bund. Ich habe sie nicht als kantonalen Abzug gefunden. Falls Sie den Wortlaut der Wegleitung selbst prüfen möchten, kann ich `tg-wl-2025__c0104` öffnen.

## q11

**Frage:** SG 2025: Pauschale für übrige Berufskosten? Wie wird sie berechnet?

**Soll (Referenz):** SG 2025: CHF 700 + 10 % des Nettolohns, max. CHF 2'400 (Art. 21 StV SG, WL SG 2025).

**Antwort des Agenten** (24.5 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **St. Gallen · Steuerjahr 2025**
> 
> Die Pauschale für übrige Berufskosten beträgt **Fr. 700 zuzüglich 10 % des Nettolohns, höchstens Fr. 2'400**.
> 
> **Berechnung (Kanton):** min(700 + 10 % × Nettolohn; 2'400)
> 
> - Die Obergrenze von Fr. 2'400 greift ab einem Nettolohn von **Fr. 17'000** (700 + 1'700). Darunter ergibt die Formel einen tieferen Betrag.
> - Der **Nettolohn** ist der Bruttoertrag abzüglich AHV/IV/EO/ALV/UV- und BVG-Beiträge, ohne Einkäufe. Er steht im Lohnausweis (Nettolohn gemäss Steuererklärung Ziff. 1.1, Code 100/102).
> - Es gibt kein Minimum im Kanton SG.
> 
> **Formular:** Formular 4 (Hilfsblatt Berufskosten), Ziff. 3.1, Code 416 (Person 1) bzw. 466 (Person 2). Der Betrag wird in Ziff. 10.1 (Code 438) bzw. 10.2 (Code 488) übertragen.
> 
> **Weitere Regeln:**
> - Die Pauschale ist ohne Nachweis abziehbar. Bei Taggeldern der ALV gilt sie sinngemäss.
> - Wenn der Arbeitgeber nicht ereignisbezogene Pauschalspesen ausbezahlt, entfällt die Pauschale.
> - Statt der Pauschale können tatsächliche übrige Berufskosten mit Belegen geltend gemacht werden (Ziff. 3.2, Code 418/468). Das ist nur sinnvoll, wenn diese die Pauschale übersteigen. Entweder Pauschale oder effektive Kosten, nicht beides.
> - Das Arbeitszimmer ist in der Pauschale enthalten und wird nicht zusätzlich abgezogen.
> 
> **Bund (separat):** 3 % des Nettolohns, mindestens Fr. 2'000, höchstens Fr. 4'000. Das Steueramt passt die Bundesabweichung automatisch an.
> 
> **Quellen:**
> - Art. 21 StV SG (`sg-stv__art-21`)
> - Steuerwegleitung 2025 (`sg-wl-2025__c0080`)
> - Formular 4 Ziff. 3.1 (`sg-form-4-2025__c0003`)
> 
> **Status:** ☑️ agent-geprüft. Die Fundstellen sind geprüft, die Abnahme ist noch offen.

## q12

**Frage:** Pauschalabzug Liegenschaftsunterhalt in AR für ein 8-jähriges Einfamilienhaus – und wie in ZH?

**Soll (Referenz):** AR: 10 % (Gebäude bis 10 Jahre) bzw. 20 % des Bruttoertrags, nur bis Bruttomietertrag 100'000 (Art. 25 StV AR, MB 03); ZH: einheitlich 20 % ohne Altersstaffel (ZStB 30.2).

**Antwort des Agenten** (28.9 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__rechne):

> **AR · Steuerjahr 2025** (kein Jahr genannt, daher 2025 angenommen)
> 
> **Appenzell Ausserrhoden: 10 %** des Bruttomietertrags, weil das Gebäude bis 10 Jahre alt ist. Mit 8 Jahren fällt es in diese Stufe.
> - Gilt nur, solange der Bruttomietertrag des gesamten Liegenschaftsbesitzes CHF 100'000 nicht übersteigt.
> - Ältere Gebäude (über 10 Jahre) erhalten 20 %.
> - Fundstelle: `ar-stv__art-25` / `ar-mb-03__c0004` · Status ☑️ agent-geprüft (Abnahme offen).
> 
> **Bund (direkte Bundessteuer): ebenfalls 10 %**, weil das Gebäude zu Beginn der Steuerperiode bis 10 Jahre alt ist. Fundstelle: `bund-lkv__art-5` · ☑️ agent-geprüft. Der Bund wird separat deklariert.
> 
> **Zürich · Steuerjahr 2025: 20 %** des Brutto-Mietertrags bzw. Mietwerts. Es gibt keine Staffelung nach Gebäudealter, der Satz gilt also auch für ein 8-jähriges Haus.
> - Wahl pro Liegenschaft und Steuerperiode zwischen Pauschale und effektiven Kosten.
> - Nicht anwendbar bei vorwiegend geschäftlich genutzten Liegenschaften.
> - Fundstelle: `zh-zstb-30-2__c0002` / `zh-wl-2025__c0185` · ☑️ agent-geprüft (Abnahme offen).
> 
> **Beispiel mit CHF 24'000 Bruttomietertrag:**
> 
> | | Pauschale | Betrag |
> |---|---|---|
> | AR (Kanton) | 10 % | CHF 2'400 |
> | ZH (Kanton) | 20 % | CHF 4'800 |
> 
> Bei AR wäre die Pauschale bei einem Haus über 10 Jahre doppelt so hoch (20 %). In ZH bleibt sie unabhängig vom Alter gleich.
> 
> Zu den Werten: Alle Fundstellen sind agent-geprüft, die Abnahme steht noch aus. Für das Steuerjahr 2026 habe ich nicht nachgeschlagen. Wenn Sie dieses Jahr meinen, sagen Sie Bescheid, dann prüfe ich es.

## q13

**Frage:** TG: Welcher Einschlag gilt auf dem Eigenmietwert der selbstbewohnten Liegenschaft am Wohnsitz (Kanton vs. Bund)?

**Soll (Referenz):** TG: Abzug 40 % Kanton, 20 % Bund für dauernd selbstbewohntes Eigentum am Wohnsitz (tg-stg__par-23; WL TG 2025).

**Antwort des Agenten** (26.8 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Thurgau · Steuerjahr 2025** (Kanton aus dem Kürzel «TG» gelesen, Jahr nicht genannt, daher 2025)
> 
> Der Selbstnutzungsabzug auf dem Eigenmietwert der am Wohnsitz dauernd selbstbewohnten Liegenschaft beträgt:
> 
> - **Staats- und Gemeindesteuern (Kanton): 40 %**, Fundstelle tg-stg__par-23 (§ 23 Abs. 2 StG TG)
> - **Direkte Bundessteuer: 20 %**, Fundstelle tg-wl-2025__c0225 (Wegleitung TG)
> 
> Die beiden Spalten werden getrennt gerechnet. Im Formular TG 2025 steht der Staat links und der Bund rechts, und der Nettoerfolg kann deshalb je Spalte verschieden ausfallen.
> 
> Hinweise:
> - **Bund nicht eindeutig belegt:** Ein Tool-Hinweis sagt, das DBG kenne keinen eigenen festen Prozentsatz und der Bundeswert folge dem kantonalen Verfahren. Die 20 % stammen aus der TG-Wegleitung und dem Formular. Vor einer Abgabe bitte gegen die Wegleitung prüfen.
> - **Voraussetzung:** Der Abzug gilt nur für Wohneigentum am Wohnsitz. Zweit- und Ferienwohnungen, landwirtschaftlich geschätzte Liegenschaften und an Nahestehende überlassene Objekte werden zu 100 % versteuert.
> - **Status:** Die Werte sind agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> Quellen: `wert tg 2025 eigenmietwert`, `position tg 2025 Eigenmietwert` (Ziff. 8.1 und Form. 7).

## q14

**Frage:** Bis wann kann ein Treuhänder im Kanton TG für seine Mandanten Fristerstreckung erhalten?

**Soll (Referenz):** Gewerbsmässige Treuhänder für Mandanten bis 31.12. des Deklarationsjahres (StP 155 Nr. 2).

**Antwort des Agenten** (24.0 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Kanton Thurgau · Steuerjahr 2025** (Sie haben kein Jahr genannt, deshalb 2025 angenommen; Deklarationsjahr ist 2026)
> 
> Ein gewerbsmässiger Treuhänder oder Steuerberater kann für seine Mandanten ein Fristerstreckungsgesuch **längstens bis 31. Dezember 2026** stellen. Das ist die Grenze für das Gesuch, nicht für die Einreichung selbst.
> 
> Die Regel nach StP 155 Nr. 2 (Chunk `tg-stp-155-2__c0002`, Status ☑️ agent-geprüft, Abnahme offen):
> 
> - **Erstes Gesuch** für Privatpersonen: grundsätzlich bis 30. September 2026.
> - **Weitere Gesuche** in begründeten Fällen: bis 30. November 2026.
> - **Treuhänder/Steuerberater** (gewerbsmässig): bis 31. Dezember 2026 für ihre Mandanten.
> - Darüber hinaus werden Gesuche nur bei glaubhaft gemachten **ausserordentlichen Gründen** bewilligt. Arbeitsüberlastung des Vertreters oder fehlende Unterlagen reichen dafür nicht.
> 
> Gesuche gehen schriftlich und begründet an das Gemeindesteueramt der Wohnsitzgemeinde (Stichtag 31.12.). Das konkrete Einreichedatum steht auf der vorgedruckten Steuererklärung. Eine Gebühr für natürliche Personen nennen die Quellen nicht.
> 
> Quellen: `tg-stp-155-2__c0001`, `tg-stp-155-2__c0002`, `tg-wl-2025__c0023`.

## q15

**Frage:** ZH: Bis wann ist die Steuererklärung 2025 einzureichen und wie lange wird höchstens Fristerstreckung gewährt?

**Soll (Referenz):** Einreichung bis 31.03.2026; Fristerstreckung längstens bis 30. November (ZStB 132.1 / WL ZH 2025).

**Antwort des Agenten** (26.2 s · Tools: 4 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kanton ZH · Steuerjahr 2025**
> 
> **Einreichefrist:** Die Steuererklärung 2025 (natürliche Personen) war bis **31. März 2026** einzureichen, online oder beim Scan-Center. Fundstelle: WL ZH 2025, zh-wl-2025__c0017 (☑️ agent-geprüft, Abnahme offen).
> 
> **Fristerstreckung:** Die längste mögliche Erstreckung ist **bis 30. November des Folgejahres**, also bis **30. November 2026**. Das gilt aber nur für Gesuche, die **vor Ablauf der Frist** eingereicht wurden. Fundstellen: zh-zstb-132-1__c0024 (Abschnitt II. Fristerstreckung, § 39 StV, Art. 119 DBG) und zh-stv__par-39 (§ 39 Abs. 1 StV: Gesuche «vor Ablauf der Frist» einreichen).
> 
> **Was das für heute (9. November 2026) heisst:** Die Frist vom 31. März 2026 ist abgelaufen. Ein Erstreckungsgesuch wird nach Fristablauf abgewiesen. Möglich bleibt nur eine **Wiederherstellung der Frist** nach § 15 StV bzw. Art. 119 Abs. 2 DBG, wenn deren Voraussetzungen erfüllt sind. Zuständig ist das **Gemeindesteueramt**. Ob die Wiederherstellung gewährt wird, hängt vom Einzelfall ab; dazu kann ich aus dem Wiki keine Aussage machen.
> 
> Nicht belegt: Kosten einer Fristerstreckung oder einer Wiederherstellung. Die Quellen nennen dazu nichts.

## q16

**Frage:** AR: Was kostet die zweite Fristverlängerung?

**Soll (Referenz):** CHF 25 (erste Verlängerung kostenlos, jede weitere CHF 25; MB 18 / WL AR 2025).

**Antwort des Agenten** (22.8 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **AR · Steuerjahr 2025** (kein Jahr genannt, daher 2025 angenommen)
> 
> Die zweite Fristverlängerung kostet **CHF 25**.
> 
> - Die erste Fristerstreckung ist kostenlos, jede weitere ist kostenpflichtig (Art. 59a Abs. 1 StV AR, Fundstelle `ar-stv__art-59a`).
> - Der Betrag von Fr. 25 steht im Merkblatt 18 unter «Fristverlängerungen (im Wiederholungsfall)» (`ar-mb-18__c0001`, gilt ab 1.9.2025). Die Wegleitung nennt denselben Wert (`ar-wl-2025__c0012`).
> 
> Status: ☑️ agent-geprüft. Die Fundstellen sind geprüft, die Abnahme steht noch aus. Art. 59a Abs. 3 verweist für die Höhe auf die Kanzleigebührenverordnung. Diese habe ich nicht geöffnet. Falls dort ein anderer Betrag steht, würde das Merkblatt davon abweichen.
> 
> Die Angaben gelten für die Staats- und Gemeindesteuer. Der Bund führt die Fristerstreckung nicht separat, daher gibt es dort keinen eigenen Betrag.

## q17

**Frage:** Krankheitskosten SG 2025: Ab welchem Selbstbehalt sind sie abziehbar – und beim Bund?

**Soll (Referenz):** SG: Selbstbehalt 2 % (Art. 46 StG SG); Bund: 5 % (Art. 33 Abs. 1 lit. h DBG, KS 11).

**Antwort des Agenten** (22.1 s · Tools: 2 Aufrufe steuerwiki__wert):

> **SG · Steuerjahr 2025**
> 
> Krankheits- und Unfallkosten sind abziehbar, soweit sie **2 % der Nettoeinkünfte** übersteigen (Nettoeinkommen, Formular Ziff. 20). Behinderungsbedingte Kosten sind ohne Selbstbehalt abziehbar. Pauschale Diätkosten (Zöliakie) betragen Fr. 2'500. Fundstelle: `sg-stg-2025__art-46`. Status ☑️ agent-geprüft, Abnahme offen.
> 
> **Bund · Steuerjahr 2025** (direkte Bundessteuer, separat deklarieren)
> 
> Abziehbar, soweit sie **5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte** übersteigen. Behinderungsbedingte Kosten (BehiG) sind ohne Selbstbehalt abziehbar. Fundstelle: `bund-dbg-2025__art-33-t3`. Status ☑️ agent-geprüft, Abnahme offen.
> 
> Die Praxis 2025/2026 stützt sich auf die ESTV-KS 11 (2005). Das neue KS 11a (publiziert 26.05.2026) gilt laut seiner Ziff. 7 erst ab Steuerperiode 2027 und ändert das Steuerjahr 2025 daher nicht.
> 
> **Wichtig:** Die Basis unterscheidet sich. SG rechnet mit den Nettoeinkünften, der Bund mit den steuerbaren Einkünften nach Abzug der Aufwendungen. Der Selbstbehalt wird deshalb in beiden Erklärungen separat berechnet.
> 
> Offen: Die genaue Formularregel für die SG-Ziff. 21.1 (Code und Berechnung) hat das Tool nur angeschnitten. Wenn du willst, prüfe ich sie mit `position sg 2025 21.1`.

## q18

**Frage:** PK-Einkauf CHF 20'000 wurde über den Lohn abgezogen (Lohnausweis Ziff. 10.2). Darf er nochmals in der Steuererklärung abgezogen werden?

**Soll (Referenz):** Nein – BVG-Einkauf über Lohnabzug (Lohnausweis Ziff. 10.2) ist bereits im Nettolohn berücksichtigt; nur direkt bezahlte Einkäufe separat abziehen.

**Antwort des Agenten** (29.8 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Bund · Steuerjahr 2025 (Kanton fehlt noch)**
> 
> Nein, der Einkauf darf nicht ein zweites Mal abgezogen werden. Es ist ein einziger Abzug, nur die Quelle ist doppelt sichtbar.
> 
> - **Lohnausweis:** Eine Einkaufssumme, die der Arbeitgeber vom Lohn abzieht, gehört zum massgebenden Bruttolohn und ist im Lohnausweis separat unter «Versicherungsbeiträge» (Ziff. 10.2) auszuweisen. Nur so kann der Arbeitnehmer den Einkauf überhaupt geltend machen (KS W03-001, Ziff. 3.3, `bund-ks-w03-001__c0009`, ☑️ Fundstelle geprüft).
> - **Steuererklärung:** Der Betrag aus Ziff. 10.2 wird einmal als Einkaufsabzug in die Abzüge übertragen. Wenn er zusätzlich im Nettolohn oder bei den Versicherungsbeiträgen steht, zählt er doppelt. Das prüfe ich, sobald ich das Formular Ihres Kantons habe.
> 
> **Offene Punkte**
> 
> 1. **Kanton:** Ich brauche den Wohnsitz am 31.12. (ZH, SG, TG oder AR). Die Formularziffer und die Höchstbeträge für den Einkauf unterscheiden sich je nach Kanton. Die Bundesregeln oben gelten unabhängig davon.
> 2. **Sperrfrist:** Laut KS 41 (Ziff. 2.2.4, `bund-ks-41__c0014`) gilt nach einem Einkauf eine dreijährige Sperrfrist für Kapitalbezüge aus der Vorsorge (Art. 79b Abs. 3 BVG). Das betrifft den Abzug nicht, ist aber wichtig, falls Sie später Kapital beziehen.
> 
> Sagen Sie mir den Kanton, dann prüfe ich die kantonale Position und die Limite.

## q19

**Frage:** Weiterbildungskosten CHF 15'000 (ZH, 2025), Arbeitgeber hat nichts bezahlt. Wie viel ist abziehbar (Kanton/Bund)?

**Soll (Referenz):** ZH Staat max. CHF 12'400 (zh-stg-2025__par-31-t4); Bund max. CHF 13'000 (bund-dbg-2025__art-33-t4).

**Antwort des Agenten** (24.8 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **ZH · Steuerjahr 2025**
> 
> - **Kanton (Staatssteuer):** CHF 12'400 abziehbar (von CHF 15'000 selbst getragen).
> - **Bund (direkte Bundessteuer):** CHF 13'000 abziehbar.
> 
> Beide Beträge sind Höchstbeträge. Der Abzug ist die kleinere Zahl aus den selbst getragenen Kosten und dem Limit. Der Arbeitgeber hat nichts bezahlt, also gilt der volle CHF 15'000 als selbst getragen.
> 
> **Voraussetzungen**
> - Die Person hat einen Abschluss auf Sekundarstufe II oder ist 20 Jahre alt oder älter. Die Weiterbildung darf nicht die Ausbildung bis zum ersten Abschluss auf Sekundarstufe II sein.
> - Massgebend ist das Datum der Fälligkeit bzw. der Zahlung, nicht der Kursbesuch.
> 
> **Formular ZH 2025**
> - Ziff. 16.2, Hilfsblatt 292, Code 292. Die Kursrechnungen und Zahlungsbelege gehören in Form. 367 (Codes 2900/2903). Die Bestätigung des Arbeitgebers oder der Lohnausweis Ziff. 13.3 belegt die Beiträge Dritter (Codes 2901/2904), hier null.
> - Staats- und Bundessteuer werden in getrennten Blöcken von Form. 367 erfasst, mit denselben Codes 2920/2921. Der Staatsblock erhält 12'400, der Bundesblock 13'000.
> - Das ausgefüllte Formular 367 liegt der Steuererklärung bei. Die Belege sind auf Verlangen einzureichen.
> 
> Quellen: `zh-stg-2025__par-31-t4` (ZH, ☑️ agent-geprüft), `bund-dbg-2025__art-33-t4` (Bund, ☑️ agent-geprüft), `zh-form-300-2025__c0008`, `zh-wl-2025__c0093`. Die Abnahme der Werte ist noch offen. Ich habe die Fundstellen geprüft, aber nicht die Gesetzestexte selbst.

## q20

**Frage:** Spenden CHF 50 an eine gemeinnützige Organisation (TG 2025) – abziehbar?

**Soll (Referenz):** Nein – TG: Zuwendungen nur abziehbar, wenn sie CHF 200 übersteigen (StG TG § 34 Abs. 1 Ziff. 11); Bund: ab CHF 100.

**Antwort des Agenten** (24.3 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> Kanton Thurgau · Steuerjahr 2025
> 
> **Nein, CHF 50 sind nicht abziehbar** – weder kantonal noch beim Bund.
> 
> - **Kanton (Staats- und Gemeindesteuer):** Abzug erst, soweit die freiwilligen Zuwendungen gesamthaft CHF 200 übersteigen. 50 liegt darunter, also 0 Abzug. Quelle: WL TG 2025, Formular 6, S. 46 (`tg-wl-2025__c0218`); ☑️ agent-geprüft, Abnahme offen.
> - **Bund (direkte Bundessteuer):** Freigrenze CHF 100. Erreichen die Zuwendungen diese nicht, ist nichts abziehbar. Quelle: Art. 33a DBG (`bund-dbg-2025__art-33a`); ☑️ agent-geprüft, Abnahme offen.
> 
> **Wichtig für spätere Spenden:** Die Freigrenze ist keine Freibetrag-Schwelle. Erreicht das Jahrestotal die Grenze, ist der gesamte Betrag abziehbar, nicht nur der Teil darüber. Wer also im Jahr 2025 insgesamt mehr als CHF 200 an abzugsfähige Institutionen gibt, kann ab dem ersten Franken abziehen (Höchstabzug kantonal CHF 8'000 bei Nettoeinkommen bis CHF 40'000, sonst 20 %).
> 
> **Zusätzlich prüfen:** Abzug nur für Institutionen, die die Steuerverwaltung Thurgau als steuerbefreit und gemeinnützig anerkannt hat. Das Verzeichnis dazu führt die Steuerverwaltung (vgl. TG FAQ NP, `tg-info-faq__c0023`). Bei gemischter Zwecksetzung gelten Sonderregeln (StP 34 Nr. 23, Ziff. 4.2). Ob die konkrete Organisation im Verzeichnis steht, habe ich nicht geprüft. Nennen Sie mir den Namen, dann prüfe ich die Anerkennung nicht selbst, sondern weise darauf hin, wo sie nachgeschlagen werden kann.

## q21

**Frage:** Was ändert sich 2026 bei der Säule 3a (Einkauf) und wo wird das im ZH-Formular 2026 eingetragen?

**Soll (Referenz):** Ab 2026 Einkauf (Nachzahlung) Säule 3a für Beitragslücken ab 2025 (max. 7'258 pro Einkaufsjahr, BVV 3 Art. 7a, KS 18a); ZH-Formular 2026: Ziff. 14.3 (Code 264, Detailfelder 276/278).

**Antwort des Agenten** (26.0 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__suche):

> **ZH · Steuerjahr 2026**
> 
> **Was sich ändert:** Neu ab Steuerperiode 2026 kann man in die Säule 3a einkaufen, und zwar für Beitragslücken, die ab 1.1.2025 entstanden sind (innerhalb der letzten zehn Jahre). Der ordentliche Höchstbetrag bleibt gleich.
> 
> - **Voraussetzungen:** In den Lückenjahren wurden AHV/IV/EO-Beiträge bezahlt, und im Einkaufsjahr wurde der volle ordentliche Maximalbeitrag einbezahlt.
> - **Höchstbetrag:** Der Einkauf ist höchstens die Summe der Lücken und in jedem Fall maximal **CHF 7'258**. Dieser Betrag kommt zusätzlich zu den ordentlichen Beiträgen.
> - **Praktische Folge für 2026:** Faktisch ist nur die Lücke 2025 einkaufbar, weil frühere Lücken nicht erfasst sind.
> - **Ordentlicher Maximalbeitrag (unverändert):** CHF 7'258 mit 2. Säule, sonst 20 % des Erwerbseinkommens, maximal CHF 36'288.
> - **Bund:** Die Bundessteuer hat dieselben Beträge (7'258 / 36'288 / 20 %). Die Wegleitung nennt für den Einkauf die gleiche Grenze.
> 
> **Wo eintragen (Formular ZH 2026):**
> 
> | Ziffer | Inhalt | Code Person 1 / 2 | Rechnen |
> |---|---|---|---|
> | **14.1 / 14.2** | Ordentliche Beiträge Säule 3a | 260 (eff. 262) / 261 (eff. 263) | min(einbezahlt; 7'258 bzw. min(20 % × Erwerbseinkommen; 36'288)) |
> | **14.3** | **Einkauf Säule 3a (neu 2026)** | **276 / 278** | min(Einkauf; Σ Lücken ab 1.1.2025; 7'258) → Summe in **Code 264** |
> 
> Kanton und Bund werden jeweils in den Spalten Staatssteuer und Bundessteuer erfasst; die Codes gelten für beide.
> 
> **Belege:**
> - Für 14.1/14.2: Bescheinigung der 3a-Einrichtung. Nur die im Jahr 2026 bezahlten Beiträge sind abziehbar.
> - Für 14.3: Einkaufsbescheinigung der 3a-Einrichtung, ein Nachweis des vollen ordentlichen Beitrags im Einkaufsjahr und ein Nachweis der AHV/IV/EO-Beiträge im Lückenjahr.
> 
> **Vorbehalte:**
> - Das reguläre Formular und die Wegleitung ZH 2026 sind laut Wiki noch nicht publiziert (Stand 09.11.2026). Die Ziffern und Codes stammen aus der Fassung für unterjährige Steuerpflicht. Bitte am endgültigen Formular prüfen.
> - Die Werte sind agent-geprüft (☑️): Fundstelle geprüft, Abnahme offen. Die Rechtsgrundlage ist nur aus der Wegleitung belegt, der Artikel in BVV 3 wurde nicht gegen einen Chunk geprüft.
> 
> **Quellen:** zh-wl-2026-uj__c0075, c0076, c0077; zh-form-300-2026-uj__c0008; bund-wl-2a-2026__c0051; bund-bsv-masszahlen-2025-2026__c0003.

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (27.4 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__wert):

> **Kurzantwort:** Die Verrechnungssteuer (35 % auf Dividenden) fordern natürliche Personen mit der **kantonalen Steuererklärung** zurück. Der Anspruch steht im **Wertschriftenverzeichnis**, nicht in einem separaten Bundesformular.
> 
> **Ablauf laut Steuer-Wiki (Bund, 2025):**
> - Die Bank stellt eine Ertragsabrechnung bzw. Abzugsbescheinigung aus, die den Bruttoertrag und die abgezogene Verrechnungssteuer ausweist.
> - Die Erträge werden im Wertschriftenverzeichnis erfasst. Die Totale (Total Steuerwert, Total Bruttoertrag) übertragen Sie in die entsprechenden Kolonnen der Bundes-Beilage DA-1 (Kapitalanlagen und Erträge, Kolonnen 1–8). Quelle: `bund-form-da1-2025__c0002`.
> - Der Rückerstattungsanspruch beträgt 35 % des Bruttoertrags, also genau der Betrag, der abgezogen wurde.
> 
> **Wo der Anspruch im Kanton steht (Fundstellen, 2025):**
> - **ZH:** Form. 340, Totale: Verrechnungssteueranspruch 35 % (Code 540). `zh-form-340-2025__c0005`
> - **SG:** Form. 2, Code 999: 35 % vom Bruttoertrag Total A. `sg-form-2-2025__c0006`
> - **TG:** Form. 2, Ziff. 10: 35 % von Bruttoertrag Total A (Rückerstattungsantrag). `tg-form-02-2025__c0006`
> - **AR:** Form. 2, Total Verrechnungssteueranspruch (Code 999). `ar-form-02-2025__c0007`
> 
> **Offen:**
> - Ich kenne Ihren Kanton nicht. Nennen Sie ihn (ZH, SG, TG oder AR), dann prüfe ich die genaue Formularposition und die Rückerstattungsregeln für dieses Steuerjahr.
> - Die Bundesrückerstattung selbst (Verfahren, Fristen, Bezug über die Steuerverwaltung) ist im Wiki nur über die Kantonsformulare belegt. Zu den Verfahrensdetails habe ich keine Quelle abgerufen und lasse sie deshalb weg.
> - Die Tool-Ausgabe nennt für diese Fundstellen keinen Verifizierungsstatus. Ich habe die Chunks nicht im Volltext geöffnet.
> - Ich habe Steuerjahr 2025 angenommen, da Sie keines genannt haben.

## q23

**Frage:** Vergleiche den Versicherungsabzug 2025 für Alleinstehende ohne Kinder in AR, SG, TG, ZH und beim Bund.

**Soll (Referenz):** Alleinstehend ohne Kinder 2025 (mit 2. Säule/3a): AR 2'700 · SG 3'400 · TG 3'500 · ZH 2'900 · Bund 1'800.

**Antwort des Agenten** (24.9 s · Tools: 1 Aufrufe steuerwiki__vergleich):

> **Bund, ZH, SG, TG, AR · 2025**
> 
> Versicherungsabzug für Alleinstehende ohne Kinder (Prämien, Versicherungsabzug mit Vorsorge-Standard):
> 
> | Ebene | Betrag | Status | Fundstelle |
> |---|---|---|---|
> | **Bund** (direkte Bundessteuer) | CHF 1'800 | ☑️ | bund-dbg-2025__art-33-t2 |
> | **Thurgau** (Kanton) | CHF 3'500 | ☑️ | tg-stg__par-34-t3 |
> | **St. Gallen** (Kanton) | CHF 3'400 | ☑️ | sg-stg-2025__art-45-t2 |
> | **Zürich** (Kanton) | CHF 2'900 | ☑️ | zh-stg-2025__par-31-t2 |
> | **Appenzell Ausserrhoden** (Kanton) | CHF 2'700 | ☑️ | ar-stg__art-35-t2 |
> 
> **Rangfolge (Kanton):** TG > SG > ZH > AR. Der Bundesabzug ist mit CHF 1'800 der tiefste Wert und liegt unter allen vier Kantonen.
> 
> **Variante ohne Vorsorge** (Alleinstehende, die keine Vorsorgebeiträge geltend machen):
> - Bund CHF 2'700 (bund-rs-2-210__c0006)
> - ZH CHF 4'350 (zh-wl-2025__c0084)
> - SG CHF 3'900 (sg-stg-2025__art-45-t2)
> - TG und AR: kein separater Wert, im Wiki nicht ausgewiesen.
> 
> Alle Werte sind agent-geprüft (☑️): Die Fundstelle ist geprüft, die fachliche Abnahme steht noch aus. Bei der Anwendung auf einen konkreten Fall empfehle ich, die Zahl einmal am Originaltext der Fundstelle gegenzuprüfen.

## q24

**Frage:** Steuerfreie Vermögensbeträge (Sozialabzüge) 2025 in SG für ein Ehepaar mit einem minderjährigen Kind?

**Soll (Referenz):** SG 2025: 150'000 (Ehepaar) + 20'000 pro minderjähriges Kind = 170'000 (sg-stg-2025__art-64).

**Antwort des Agenten** (22.4 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__rechne):

> **St. Gallen · Steuerjahr 2025**
> 
> Für ein Ehepaar mit einem minderjährigen Kind ergibt sich ein steuerfreier Vermögens-Sozialabzug von **CHF 170'000**:
> 
> | Position | Betrag | Fundstelle | Status |
> |---|---|---|---|
> | Gemeinsam Steuerpflichtige (2 × 75'000) | CHF 150'000 | sg-wl-2025__c0118 | ☑️ agent-geprüft |
> | Zusätzlich pro minderjähriges Kind | CHF 20'000 | sg-stg-2025__art-64 | ☑️ agent-geprüft |
> | **Total** | **CHF 170'000** | | |
> 
> Grundlage ist Art. 64 Abs. 1 StG SG (Fr. 75'000 pro Steuerpflichtigen, zusätzlich Fr. 20'000 pro minderjähriges Kind unter elterlicher Sorge bzw. Obhut, für das ein Kinderabzug beansprucht werden kann). Der Status ist «agent-geprüft»: Die Fundstellen sind geprüft, die fachliche Abnahme steht noch aus.
> 
> **Kanton und Bund getrennt:** Der Vermögens-Sozialabzug gilt nur für die Staats- und Gemeindesteuer. Der Bund erhebt keine Vermögenssteuer, daher gibt es dort keinen entsprechenden Abzug.
> 
> **Im Formular SG 2025:** Die Sozialabzüge Vermögen stehen in Ziff. 36.1–36.3. Für die Eintragung der einzelnen Positionen kann ich `position sg 2025 36` abrufen, falls du das brauchst.

## q25

**Frage:** Welcher Verzugszins gilt 2026 für die direkte Bundessteuer?

**Soll (Referenz):** 4.00 % (RS 2-215, bund-rs-2-215__c0010/c0011).

**Antwort des Agenten** (20.9 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Bund · Steuerjahr 2026**
> 
> Der Verzugs- und Rückerstattungszins für die direkte Bundessteuer beträgt **4,00 %** (2025: 4,50 %).
> 
> - Fundstelle: `bund-rs-2-215__c0010`, Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> - Der Bund kennt keinen Ausgleichszins. Der Vergütungszins für Vorauszahlungen liegt 2026 bei 0,00 % (2025: 0,75 %).
> 
> Die Frage bezog sich nur auf den Bund, deshalb habe ich keinen Kanton herangezogen. Für kantonale Verzugszinsen nennen Sie bitte den Kanton (AR, SG, TG oder ZH).

## q26

**Frage:** Wann wird der Eigenmietwert abgeschafft und gilt das schon für 2026?

**Soll (Referenz):** Abschaffung per 1.1.2029 (Bundesratsbeschluss 01.04.2026); für 2025–2028 gilt bisheriges Recht – 2026 also noch Eigenmietwert.

**Antwort des Agenten** (26.5 s · Tools: 4 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Bund · Steuerjahr 2026.** Kein Kanton genannt, deshalb nur die Bundesebene.
> 
> - **Abschaffung:** Der Bundesrat hat am 1. April 2026 beschlossen, die Reform der Wohneigentumsbesteuerung per **1. Januar 2029** in Kraft zu setzen. Ab dann entfällt die Besteuerung des Eigenmietwerts auf selbstgenutztem Wohneigentum. Die Volksabstimmung hat dem bereits zugestimmt (Verfassungsbestimmung). Quelle: Medienmitteilung des Bundesrats, 1. April 2026 (`bund-mm-eigenmietwert-abschaffung__c0001`, `__c0002`).
> - **Gilt 2026 schon?** Nein. Der Eigenmietwert bleibt für 2026 steuerbar. Das Wiki hält dazu fest: «Eigenmietwert bleibt für 2026 steuerbar». Die Formularlogik für 2026 (Formular 2, Ziff. 8: Eigenmietwert, Bruttoertrag, Unterhalt) gilt also unverändert.
> - **Kantone:** Die Kantone können als Ausgleich eine Objektsteuer auf Zweitliegenschaften einführen. Ob und wie das in Ihrem Kanton geschieht, hängt vom Kanton ab.
> 
> Status: Die Angaben stammen aus der Bundesrats-Mitteilung und sind nur als Quelle belegt, nicht gegen den Gesetzestext geprüft. Ich habe den Kanton nicht angenommen. Nennen Sie mir Kanton und Steuerjahr (ZH, SG, TG oder AR), dann prüfe ich die kantonale Umsetzung und die Position in der Steuererklärung.

## q27

**Frage:** Zitiere die Regel zum Abzug privater Schuldzinsen im DBG (Steuerjahr 2025) mit Artikel.

**Soll (Referenz):** Art. 33 Abs. 1 lit. a DBG (Fassung 2025): private Schuldzinsen im Umfang der steuerbaren Vermögenserträge (Art. 20, 20a, 21) und weiterer CHF 50'000.

**Antwort des Agenten** (24.9 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> Ich öffne den Art.-33-Chunk im Wortlaut.
> 
> **Bund · Steuerjahr 2025**
> 
> Art. 33 Abs. 1 lit. a DBG (Schuldzinsen und andere Abzüge), Wortlaut:
> 
> > «Von den Einkünften werden abgezogen: a. die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken. Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten oder ihr sonst wie nahe stehenden natürlichen Person zu Bedingungen gewährt, die erheblich von den im Geschäftsverkehr unter Dritten üblichen Bedingungen abweichen»
> 
> Quelle: `bund-dbg-2025__art-33-t1` (Gesetz DBG, Steuerjahr 2025, gültig bis 31.12.2025), Status ☑️ Fundstelle geprüft, Abnahme offen.
> 
> Zur Einordnung, nur aus den Quellen belegt:
> - Der Abzug ist auf die steuerbaren Vermögenserträge (Art. 20, 20a, 21 DBG) plus 50 000 Franken begrenzt.
> - Die Abgrenzung privater gegenüber geschäftlicher Schuldzinsen (bei Beteiligungen im Geschäftsvermögen) behandelt die KS 22a, Ziff. 3.2 (`bund-ks-22a__c0014`); dort steht auch ein Beispiel (`bund-ks-22a__c0021`). Ich habe diese Chunks nicht im Wortlaut geöffnet.
> 
> Hinweis: Die Schuldzinsen-Regel ist in der Steuererklärung kantonal zu deklarieren. Falls du einen Kanton meinst (ZH, SG, TG, AR), sag mir das Kürzel, dann suche ich die kantonale Position dazu.

## q28

**Frage:** Ist ein Leasingvertrag für das Privatauto steuerlich relevant? Was ist mit den Leasingraten?

**Soll (Referenz):** Leasingraten sind keine Schuldzinsen und grundsätzlich nicht abziehbar (Lebenshaltung); relevant nur für Fahrkosten-Begründung/Geschäftsauto, Vermögen (kein Eigentum).

**Antwort des Agenten** (32.5 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Kanton: nicht angegeben · Steuerjahr: 2025 (angenommen)**
> 
> Die Antwort unten gilt nur für den Bund. Für Staats- und Gemeindesteuer brauche ich den Kanton (ZH, SG, TG oder AR).
> 
> **Ist der Leasingvertrag steuerlich relevant?**
> Der Vertrag selbst ist kein Abzug. Wichtig ist, wozu das Auto genutzt wird:
> 
> - **Rein privat genutzt:** Die Leasingraten sind Lebenshaltungskosten und nicht abzugsfähig. Auch der Zinsanteil ist nicht abzugsfähig, weil Leasingraten für privat genutzte Güter keine abzugsfähigen Zinsanteile enthalten (Bund, KS 22a, Ziff. 3.3).
> - **Für den Arbeitsweg genutzt:** Die Leasingraten werden nicht einzeln abgezogen. Stattdessen gilt die Fahrkostenpauschale: Bund CHF –.70 pro km, maximal CHF 3'300.– (Formular 9–14 2025, Ziff. 2). Damit sind die Autokosten abgegolten. Für ein privates Motorfahrzeug auf dem Arbeitsweg muss zusätzlich begründet werden, warum kein öffentliches Verkehrsmittel genutzt werden kann (Ziff. 9).
> - **Firmenauto vom Arbeitgeber (Leasing über den Arbeitgeber):** Die private Nutzung gilt als Naturallohn. Ein Privatanteil muss als Einkommen deklariert werden (Bund, KS 45, Ziff. 3.2.6; BKV Art. 5a). Ob das Ihren Fall betrifft, hängt davon ab, wer Halter und Vertragspartner ist.
> 
> **Offen:**
> - Ob Sie selbstständig erwerbend sind. Dann könnte ein beruflicher Anteil der Leasingraten als Geschäftsaufwand gelten. Das habe ich nicht geprüft.
> - Die kantonalen Regeln zur Fahrkostenpauschale und zum Arbeitsweg können vom Bund abweichen. Dazu brauche ich den Kanton.
> 
> Wenn Sie mir den Kanton und die Nutzung nennen (nur privat, Arbeitsweg, Firmenwagen oder selbstständig), prüfe ich die kantonalen Werte und die Formularposition.

## q29

**Frage:** Wie hoch ist der Kinderabzug im Kanton Bern 2025?

**Soll (Referenz):** Nicht im Wiki (nur Bund, AR, SG, TG, ZH).

**Antwort des Agenten** (23.3 s · Tools: 1 Aufrufe steuerwiki__wert):

> Im Steuer-Wiki ist der Kanton Bern nicht abgedeckt (erfasst sind Bund sowie AR, SG, TG, ZH). Deshalb kann ich dir für Bern 2025 keinen kantonalen Kinderabzug nennen.
> 
> Was ich belegen kann, ist der **Bund (direkte Bundessteuer) 2025**, der in allen Kantonen gilt:
> 
> - **Kinderabzug vom Einkommen: CHF 6'800** pro minderjähriges oder in Ausbildung stehendes Kind (Art. 35 Abs. 1 lit. a DBG). Status ☑️ agent-geprüft, Abnahme offen. Quelle: `bund-dbg-2025__art-35`.
> - Bei getrennter Besteuerung wird der Abzug hälftig berechnet, wenn gemeinsame elterliche Sorge besteht und keine Unterhaltsbeiträge fliessen.
> - Zusätzlich gibt es eine **Ermässigung des Steuerbetrags von CHF 263 pro Kind** (Art. 36 Abs. 2bis DBG). Das ist ein anderer Abzug und darf nicht damit verwechselt werden.
> 
> Der kantonale Kinderabzug für Bern (Staats- und Gemeindesteuer) lässt sich nur aus einer Quelle ausserhalb des Wiki ermitteln, z.B. dem Berner Steuerrechner oder der Wegleitung der Steuerverwaltung des Kantons Bern. Wenn du mir den Wortlaut oder die Fundstelle schickst, prüfe ich sie gern.

## q30

**Frage:** Ehepaar TG 2025, beide angestellt (Nettolohn 80'000 und 30'000), pendelt mit ÖV-Abo (CHF 1'200 bzw. 900). Erstelle die Abzüge Berufskosten (Fahrkosten, Verpflegung ohne Kantine, Pauschale übrige) je Person für Kanton und Bund mit Fundstellen.

**Soll (Referenz):** TG 2025 je Person: Fahrkosten = ÖV-Abo effektiv (1'200 bzw. 900; Max. 6'000 Staat / 3'300 Bund); Verpflegung ohne Kantine 15/Tag, max. 3'200 (beide Ebenen); übrige Pauschale 3 %: P1 80'000 → 2'400, P2 30'000 → 900 → Minimum 2'000 (beide Ebenen, BKV TG § 4a / BKV Bund).

**Antwort des Agenten** (36.4 s · Tools: 8 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **TG · 2025** · Abzüge Berufskosten je Person, getrennt nach Kanton (Staats- und Gemeindesteuer) und Bund (direkte Bundessteuer). Annahmen: je 100 % Pensum, keine Geschäftsfahrzeuge, keine Fahrkosten vom Arbeitgeber erstattet.
> 
> | Position | Person 1 (Nettolohn 80'000) Kanton | Person 1 Bund | Person 2 (Nettolohn 30'000) Kanton | Person 2 Bund |
> |---|---|---|---|---|
> | **Fahrkosten ÖV-Abo** | 1'200 (Max. 6'000) | 1'200 (Max. 3'300) | 900 (Max. 6'000) | 900 (Max. 3'300) |
> | **Verpflegung** (ohne Kantine, max.) | 3'200 | 3'200 | 3'200 | 3'200 |
> | **Übrige Berufskosten** (3 % Nettolohn, min. 2'000, max. 4'000) | 2'400 | 2'400 | 2'000 (3 % = 900, auf Minimum angehoben) | 2'000 |
> | **Total (Maximalfall)** | **6'800** | **6'800** | **6'100** | **6'100** |
> 
> **Verpflegung ist eine Bedingung.** Der Abzug gilt nur, wenn beide regelmässig auswärts essen, weil die Heimkehr am Mittag unzumutbar ist. Pauschale CHF 15 pro auswärtiger Hauptmahlzeit, Jahresmaximum 3'200; das Maximum ist ab 214 solchen Tagen erreicht. Ohne auswärtige Verpflegung entfällt der Posten (0). Ohne Kantine gibt es keine Halbierung auf CHF 7.50 pro Tag.
> 
> **Fundstellen**
> 
> - Fahrkosten Kanton: `tg-stg__par-29` (Max. CHF 6'000); ÖV-Abo ist der Normalfall (`tg-bkv__par-1`). Zusätzlich Formular-Hinweis `tg-form-01-2025__c0010`.
> - Fahrkosten Bund: `bund-dbg-2025__art-26` (Max. CHF 3'300), `bund-bkv-2025__anhang-1`.
> - Verpflegung Kanton: `tg-bkv__par-2-t1` (CHF 15/Tag, CHF 3'200/Jahr); Halbabzug `tg-bkv__par-2-t2`.
> - Verpflegung Bund: `bund-bkv-2025__anhang-1` (CHF 15/Tag, CHF 3'200/Jahr).
> - Übrige Berufskosten Kanton: `tg-bkv__par-4a` (3 % Nettolohn, min. 2'000, max. 4'000).
> - Übrige Berufskosten Bund: `bund-bkv-2025__anhang-1` (gleiche Ansätze).
> - Formular: Ziff. 10.1 (Person 1) und 10.2 (Person 2), Formular 4.2 Ziff. 2.1 (ÖV), 3 (Verpflegung), 4 (übrige); Nettolohn aus Lohnausweis Ziff. 11.
> 
> **Zu prüfen**
> 
> - Lohnausweis: Feld F angekreuzt heisst keine Fahrkosten; Feld G heisst nur halbe Verpflegung.
> - Der Bund-Fahrkostenmaximum-Wert ist widersprüchlich (Gesetz 3'300, Wegleitung 3'200). Bei 1'200 und 900 ändert das nichts.
> - Alle Werte sind ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen.
> - Übrige Berufskosten: Anstelle der Pauschale kann man höhere, nachgewiesene Kosten geltend machen, aber nicht kumulieren.
> 
> Die Verpflegung braucht Ihre Angabe, ob und an wie vielen Tagen beide auswärts essen; mit dieser Angabe rechne ich den Posten genau.

## q31

**Frage:** Ehepaar ZH 2026, beide erwerbstätig, Kind 3 Jahre in der Kita (Kosten CHF 30'000). Wie viel Drittbetreuung ist abziehbar (Kanton und Bund)?

**Soll (Referenz):** ZH 2026 Kanton max. CHF 25'300 pro Kind (zh-stg-2026__par-31-t3); Bund 2026 max. CHF 25'800 (bund-dbg-2026__art-33-t7). Abzug je Ebene getrennt.

**Antwort des Agenten** (26.1 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Zürich · Steuerjahr 2026**
> 
> Für das Kind (3 Jahre, in Kita, gleicher Haushalt, beide Eltern erwerbstätig) sind die Kosten von CHF 30'000 bis zum Höchstbetrag abziehbar:
> 
> | Steuer | Höchstbetrag pro Kind | Abziehbar |
> |---|---|---|
> | Staatssteuer (Kanton ZH) | CHF 25'300 | **CHF 25'300** |
> | Bundessteuer | CHF 25'800 | **CHF 25'800** |
> 
> Die Kosten übersteigen beide Limiten, daher ist jeweils der Höchstbetrag abziehbar. Die Beträge werden in der Steuererklärung getrennt erfasst (Spalten Staatssteuer und Bundessteuer).
> 
> **Voraussetzungen, die hier erfüllt sind:**
> - Kind hat das 14. Altersjahr noch nicht vollendet (Kanton und Bund: 14 Jahre).
> - Kind lebt im gleichen Haushalt wie die Person, die für seinen Unterhalt sorgt.
> - Die Kosten stehen im direkten Zusammenhang mit Erwerbstätigkeit; bei Ehepaaren müssen beide gleichzeitig erwerbstätig sein.
> 
> **Hinweise:**
> - Abgezogen werden nur Kosten während der Arbeitszeit. Hat die Kita auch Zeiten ohne Erwerbstätigkeit abgedeckt, ist der Anteil zu kürzen.
> - Nicht abziehbar sind z. B. Sport, Musik, Vereine, Schulgeld und Nachhilfe.
> - Sind die Kosten nur pauschal ausgewiesen (nicht per Rechnung), werden 20 % als Lebenshaltungskosten abgezogen. Bei Kita-Rechnungen mit Zahlungsnachweis entfällt das.
> - Belege: Kita-Rechnungen mit Zahlungsnachweis, Aufstellung der Betreuungskosten mit Empfänger; bei angestellter Betreuungsperson eine Kopie des Lohnausweises.
> - Ziffer 16.6 im Formular (Code 376) für fremdbetreute Kinder, Jahrgang 2012–2026.
> 
> **Quellenstatus:** Die Werte sind agent-geprüft (Fundstelle geprüft, Abnahme offen). Quellen: Kanton ZH `zh-stg-2026__par-31-t3`, `zh-wl-2026-uj__c0105`, `zh-form-300-2026-uj__c0008`; Bund `bund-dbg-2026__art-33-t7`. Das reguläre Formular ZH 2026 war zum Stand 09.11.2026 noch nicht publiziert. Die Zuordnung zur Ziffer 16.6 stützt sich auf die Fassung für unterjährige Steuerpflicht. Die Ziffer im regulären Formular sollte vor dem Ausfüllen geprüft werden.

## q32

**Frage:** SG 2025: Einfamilienhaus (Baujahr 2010), selbst bewohnt. Pauschalabzug Liegenschaftsunterhalt Kanton und Bund?

**Soll (Referenz):** SG 2025: 20 % des Eigenmietwerts, ohne Altersstaffel (sg-stv__art-29); Bund: Gebäude zu Beginn 2025 über 10 Jahre alt → 20 % (bund-lkv__art-5).

**Antwort des Agenten** (27.1 s · Tools: 2 Aufrufe steuerwiki__wert):

> **SG · 2025**
> 
> **Ja, für beide.** Der Pauschalabzug für Liegenschaftsunterhalt gilt im Kanton und beim Bund, aber mit unterschiedlichen Sätzen:
> 
> - **Kanton SG: 20 %** des Bruttomietertrags bzw. des angerechneten Eigenmietwerts. SG unterscheidet nicht nach Gebäudealter. Fundstelle: sg-stv__art-29 (`chunks/sg/2025/sg-stv/sg-stv__art-29.md`). Status ☑️ agent-geprüft, Abnahme offen.
> - **Bund (direkte Bundessteuer): 20 %**, weil das Gebäude zu Beginn der Steuerperiode (1.1.2025) mehr als zehn Jahre alt ist. Baujahr 2010 ergibt rund 15 Jahre. Fundstelle: bund-lkv__art-5 (`chunks/bund/2025/bund-lkv/bund-lkv__art-5.md`). Status ☑️ agent-geprüft, Abnahme offen.
> 
> Der Bund rechnet also mit 10 % nur bei Gebäuden bis zehn Jahre alt. Bei Ihrem Baujahr 2010 ist das nicht der Fall.
> 
> **Offen:**
> - Die Pauschale ist eine Wahl pro Periode und Liegenschaft. Die Alternative sind die effektiven Unterhaltskosten.
> - Die Quellen belegen nicht eindeutig, ob die 20 % auf den Eigenmietwert vor oder nach dem 30-%-Selbstnutzungsabzug im Kanton SG angewendet werden. Das sollte vor dem Ausfüllen im Formular geprüft werden. Für den Bund gibt es keinen eigenen Eigenmietwert-Abzug; der Wert wird im kantonalen Verfahren festgesetzt.
> - Für die Platzierung im Formular SG 2025 gilt Ziff. 15 (Code 716). Die Regel dazu prüfe ich bei Bedarf mit `position sg 2025 15`.

## q33

**Frage:** ZH 2025: Kind 19 Jahre, in Lehre (Ausbildung). Kinderabzug Kanton und Bund?

**Soll (Referenz):** ZH 2025 Kanton CHF 9'300 (volljährig in Erstausbildung, zh-stg-2025__par-34); Bund CHF 6'800 (bund-dbg-2025__art-35) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (28.7 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__position, steuerwiki__zeige):

> **ZH · Steuerjahr 2025**
> 
> Ja, für ein volljähriges Kind in beruflicher Erstausbildung (Lehre) gilt der Kinderabzug, wenn Sie den Unterhalt zur Hauptsache bestreiten und das Kind auf Ihre Unterstützung angewiesen ist. Das Alter 19 spielt dabei keine Rolle.
> 
> | | Kanton ZH (Staats-/Gemeindesteuer) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | Kinderabzug vom Einkommen | **CHF 9'300** | **CHF 6'800** |
> | Ermässigung des Steuerbetrags | – | **CHF 263** zusätzlich |
> | Versicherungsabzug je Kind | CHF 1'300 | CHF 700 |
> 
> - **Kanton:** § 34 Abs. 1 lit. a StG, Eckwert `sozialabzug.kind_ausbildung`. ZH kennt keine Altersstaffelung und keinen Zuschlag für auswärtige Ausbildung. Fundstelle: zh-stg-2025__par-34.
> - **Bund:** Art. 35 Abs. 1 lit. a DBG, Eckwert `sozialabzug.kind_ausbildung`. Fundstelle: bund-dbg-2025__art-35. Der Bundesabzug vom Steuerbetrag (263 Franken je Kind, Art. 36 Abs. 2bis DBG) kommt zusätzlich zum Einkommensabzug, nicht statt dessen.
> - **Formular ZH 2025:** Ziff. 24.1, Code 370 («Abzug für Kinder in Ihrem Haushalt»). Das Kind gehört in die Zeile für Kinder im Haushalt. Die Bundessteuer-Spalte trägt 6'800 ein. Wohnt das Kind ausserhalb Ihres Haushalts, gilt Code 372. Der Versicherungsabzug steht unter Ziff. 15 (Code 270).
> 
> **Bedingungen (Stichtag 31.12.2025):**
> - Lehrvertrag oder Schule mit mindestens halbtägigem Besuch und mindestens einem halben Jahr Dauer. Die Lehrbestätigung ist als Beleg einzureichen.
> - Sie tragen den Unterhalt zur Hauptsache, und das Kind ist auf Ihre Unterstützung angewiesen. Wer Kinderalimente zahlt, erhält keinen Kinderabzug (WL ZH 2025, Ziff. 24.1).
> - Bei getrennt lebenden Eltern mit gemeinsamer Sorge ohne Unterhaltsbeiträge wird der Abzug halbiert (CHF 4'650 kantonal / CHF 3'400 Bund).
> 
> **Status:** Die Beträge und Fundstellen sind agent-geprüft (☑️), die Abnahme ist noch offen. Ob das Kind tatsächlich zur Hauptsache von Ihnen unterhalten wird, müssen Sie anhand des Sachverhalts beurteilen. Das Wiki kann das nicht entscheiden.

## q34

**Frage:** ZH 2025: Lohnausweis Feld G angekreuzt (Kantine). Welche Verpflegungspauschale gilt und in welche Ziffer des Berufsauslagenformulars?

**Soll (Referenz):** Verbilligte Verpflegung: CHF 7.50 pro Arbeitstag, max. CHF 1'600 pro Jahr (LS 631.33, zh-pauschalierung-berufsauslagen-2025__c0004); Form. 360 Ziff. 2.1 (verbilligt); Bund gleich.

**Antwort des Agenten** (24.3 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__beleg):

> **ZH · Steuerjahr 2025**
> 
> Mit Feld G im Lohnausweis gilt der **verbilligte Verpflegungsabzug**: CHF 7.50 pro Arbeitstag, höchstens CHF 1'600 pro Jahr. Eingetragen wird er in **Form. 360 (Hilfsblatt Berufskosten), Ziff. 2.1 verbilligt**, Code **206** für Person 1 (Person 2: Code 226).
> 
> - **Berechnung:** min(Arbeitstage × 7.50; 1'600). Die Arbeitstage fehlen mir noch. Sie stehen im Arbeitszeitnachweis.
> - **Bund:** Derselbe Code gilt in der Bundessteuer-Spalte. Kanton und Bund sind hier gleich hoch. Die CHF 7.50 und 1'600 sind bereits der halbe Abzug, also nicht nochmals halbieren.
> - **Voraussetzung:** Der Abzug gilt nur, wenn die Mittagspause die Heimkehr nicht erlaubt und trotzdem Mehrkosten entstehen. Er ist nicht mit Ziff. 2.1 voll (CHF 15/Tag, Code 208) oder Ziff. 2.2 (Schicht) kombinierbar. Ohne Feld G gilt stattdessen Code 208 mit CHF 15/Tag, max. CHF 3'200.
> - **Status:** Fundstelle geprüft (zh-form-360-2025__c0003, Limiten aus zh-pauschalierung-berufsauslagen-2025__c0004), Abnahme offen.
> 
> Falls der Lohnausweis unter Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt» vermerkt, sollten Sie den Abzug nochmals prüfen.

## q35

**Frage:** SG 2025: Kapitalbezug Säule 3a CHF 100'000. Wird das mit dem übrigen Einkommen besteuert? Wo deklarieren?

**Soll (Referenz):** Nein – Kapitalleistungen aus Vorsorge werden getrennt vom übrigen Einkommen (separate Jahressteuer) besteuert; SG Formular 1 Ziff. 40.1 (Säule 3a), Total Ziff. 41.

**Antwort des Agenten** (28.8 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__suche):

> **SG · 2025**
> 
> **Besteuerung:** Nein, die CHF 100'000 werden nicht mit dem übrigen Einkommen zusammengerechnet. Kapitalleistungen aus Vorsorge (Säule 3a, 2. Säule) werden gesondert vom übrigen Einkommen besteuert, mit einer separaten Jahressteuer. Die Steuer wird also nicht durch das übrige Einkommen progressiv erhöht.
> 
> - **Kanton SG:** einfache Steuer 2,0 % (Ehegattensatz, auch für Alleinstehende mit Kindern/Unterstützten im Haushalt) bzw. 2,2 % (übrige). Berechnet ohne allgemeine und Sozialabzüge. Darauf kommen der Steuerfuss von Kanton und Gemeinde.
> - **Bund:** ein Fünftel der Tarife nach Art. 36 DBG, ohne Sozialabzüge.
> 
> **Deklaration:** Formular 1 SG 2025, **Ziff. 40.1** («Kapitalleistungen aus Vorsorge: Säule 3a»). Die Position ist nur informativ. Der Betrag wird nicht in die Einkommenszeile 6.4 eingetragen. Beilegen: die Bescheinigung der Bank bzw. Versicherung über die Kapitalauszahlung 2025. Das Formular verlangt sie ausdrücklich.
> 
> **Offen / zu prüfen:**
> - Die Steuer für die CHF 100'000 habe ich nicht ausgerechnet. Die Sätze sind einfache Steuer, und Steuerfuss sowie Bundesbetrag hängen von Gemeinde und Tarif ab. Ich habe dazu keine verifizierte Rechnung.
> - Die Angaben stammen aus dem Wiki mit Status ☑️ (Fundstelle geprüft, Abnahme offen). Die Fundstellen sind `sg-form-1-2025__c0014` und `sg-wl-2025__c0119`.
> - Falls der Bezug in einem Jahr mit anderen Kapitalleistungen aus Vorsorge zusammenfällt, sind alle 2025 erhaltenen Beträge zu einem Gesamtbetrag zusammenzurechnen.

## q36

**Frage:** ZH 2025: Geschiedener Mandant zahlt Unterhaltsbeiträge an die Ex-Frau (CHF 24'000) und für das minderjährige Kind (CHF 12'000). Was ist abziehbar, in welcher Ziffer?

**Soll (Referenz):** Ex-Ehefrau CHF 24'000 voll abziehbar, Ziff. 13.1 (Code 254); Kinderalimente CHF 12'000 abziehbar bis und mit Monat der Volljährigkeit, Ziff. 13.2 (Code 255); Empfänger versteuert; Bund gleich (Art. 33 Abs. 1 lit. c DBG).

**Antwort des Agenten** (29.8 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **ZH · Steuerjahr 2025**
> 
> | Zahlung | Ziffer | Code | Abziehbar |
> |---|---|---|---|
> | CHF 24'000 an die geschiedene Ehefrau | **13.1** Unterhaltsbeiträge an geschiedenen/getrennt lebenden Ehegatten | 254 | **voll** (CHF 24'000) |
> | CHF 12'000 für das minderjährige Kind | **13.2** Unterhaltsbeiträge für minderjährige Kinder | 255 | **nur bis und mit dem Monat des 18. Geburtstags des Kindes** |
> 
> **Begründung**
> - **Ehefrau (13.1):** Die Wegleitung sagt, Unterhaltsbeiträge, die für den geschiedenen Ehegatten persönlich bestimmt sind, können voll abgezogen werden. Kanton und Bund sind gleich. Gegenstück: Die Ex-Frau versteuert den Betrag in Ziff. 5.1 (Code 160).
> - **Kind (13.2):** Abzug nur für Zahlungen bis und mit dem Monat der Volljährigkeit. Spätere Zahlungen sind nicht abziehbar. Wer Alimente für ein minderjähriges Kind zahlt, erhält für dieses Kind keinen Kinderabzug. Ab dem Folgemonat greift stattdessen der Kinderabzug (Ziff. 24.1), sofern die Voraussetzungen erfüllt sind. Gegenstück: Das Kind-Alimente-Empfänger versteuert in Ziff. 5.2 (Code 161).
> 
> **Offene Punkte**
> 1. **Geburtsdatum des Kindes:** Für 13.2 brauche ich es, um den abziehbaren Betrag zu bestimmen. Liegen alle CHF 12'000 bis zum Monat des 18. Geburtstags, sind sie voll abziehbar. Sonst nur der Teil bis dahin.
> 2. **Bund:** Die Bundessteuer-Spalte hat dieselben Codes. Der Bund lässt nur familienrechtlich geschuldete, effektiv bezahlte Alimente zu, freiwillige Zahlungen nicht. Das ist bei einem Scheidungsurteil oder einer Unterhaltsvereinbarung zu prüfen.
> 3. **Belege:** Die Wegleitung verlangt für 13.1/13.2 keine Beilage der Zahlungsnachweise, sofern nicht ausdrücklich verlangt. Das Wiki markiert die Beilagepflicht trotzdem als strittig. Im Zweifel Scheidungsurteil bzw. Unterhaltsvereinbarung und Bankbelege beilegen.
> 
> Status der Fundstellen: ☑️ agent-geprüft, Abnahme offen. Quellen: zh-form-300-2025__c0007 (13.1/13.2), zh-wl-2025__c0075 und c0076 (Wegleitung ZH 2025, Ziff. 13).

## q37

**Frage:** TG 2025: Mandant bringt Steuerberatungsrechnung, Kreditkartenabrechnung, Mietvertrag und Motorfahrzeugversicherung. Was davon ist relevant?

**Soll (Referenz):** Steuerberatungsrechnung: nein; Motorfahrzeugversicherung: nein; Kreditkartenabrechnung: bedingt (nur als Nachweis/Schuld per 31.12.); Mietvertrag: bedingt (Wochenaufenthalt/Arbeitszimmer/Adressnachweis) – laut belege-relevanz.

**Antwort des Agenten** (34.4 s · Tools: 6 Aufrufe read, steuerwiki__ablage, steuerwiki__zeige):

> **Thurgau · Steuerjahr 2025**
> 
> | Dokument | steuerrelevant? | Kategorie (Ablage) | Eingereicht? |
> |---|---|---|---|
> | Steuerberatungsrechnung | **nein** | keine Steuerbeleg-Kategorie | – |
> | Motorfahrzeugversicherung | **nein** | keine Steuerbeleg-Kategorie | – |
> | Kreditkartenabrechnung | **bedingt** | Belege Sonstiges, falls relevant | nein (Einreichung TG unklar) |
> | Mietvertrag | **bedingt** | Belege Sonstiges, falls relevant | nein (Einreichung TG unklar) |
> 
> **Begründung:**
> 
> - **Steuerberatungsrechnung, nicht relevant:** Kosten für die Steuerberatung und die Ausfertigung der Steuererklärung im Privatvermögen sind nicht abziehbar. Die Fundstelle ist die Bundes-Wegleitung (`bund-wl-2a-2025__c0057`). Eine TG-Stelle habe ich dafür nicht geprüft.
> - **Motorfahrzeugversicherung, nicht relevant:** Die Police selbst hat keinen Steuerwert. Steuerlich relevant ist das Fahrzeug: Private Motorfahrzeuge sind zum Verkehrswert per 31.12. als Vermögen zu deklarieren (WL TG 2025, Ziff. 30.4, `tg-wl-2025__c0123`). Der Wiki-Hinweis, Versicherungsprämien seien nicht abziehbar, stammt aus AR/SG. Für TG habe ich das nicht bestätigt gefunden.
> - **Kreditkartenabrechnung, bedingt:** Die Abrechnung ist kein Beleg. Sie kann aber als Nachweis dienen, wenn ein abziehbarer Betrag (z. B. Spenden, Krankheitskosten, Weiterbildung) belegt werden muss und die Originalrechnung fehlt. Ebenso relevant sind Sollzinsen als Schuldzinsen (Ziff. 34, Form. 4.1 A). Ist eines davon einschlägig, gehört sie zu Belege Sonstiges.
> - **Mietvertrag, bedingt:** Der Mietzins der selbstbewohnten Wohnung ist Lebenshaltung und nicht abziehbar (Art. 34 lit. a DBG). Relevant wird der Vertrag nur bei Untervermietung (steuerbarer Nettoertrag) oder bei einem Wochenaufenthalt am Arbeitsort (Mehrkosten der Unterkunft). Falls einer der Fälle zutrifft, gehört er zu Belege Sonstiges.
> 
> **Offene Punkte:**
> 
> - Die Ablage wurde nur mit den Dokumentarten (Titeln) und nicht mit dem Inhalt der Dokumente durchgeführt. Bitte Dokumente im Original prüfen, besonders auf Sollzinsen, Spenden, Krankheitskosten oder einen Untermietvertrag.
> - Ob die beiden bedingten Belege in TG einzureichen sind, habe ich nicht belegt. Falls doch, wird die Kategorie Belege eingereicht mit «Eingereicht? = ja».
> - Die Kategorien in KATEGORIEN.md sind noch nicht von consis bestätigt.

## q38

**Frage:** AR 2026: Wie hoch ist der Kinderabzug für ein 10-jähriges Kind? Ist der Wert gesichert?

**Soll (Referenz):** AR 2026: CHF 7'400 laut Anhang 1 StG (indexiert), aber Status STRITTIG (MB 02 / StG-Text nennen andere Beträge; Wegleitung 2026 fehlt) → Fachperson.

**Antwort des Agenten** (24.2 s · Tools: 2 Aufrufe steuerwiki__wert):

> **AR · 2026**: Der Kinderabzug für ein 10-jähriges Kind beträgt **CHF 7'400** (Kanton). Der Wert ist **nicht vollständig gesichert**: Status ⚠️ strittig.
> 
> - **Fundstelle:** ar-stg-anhang-kp__c0001, Art. 38 Abs. 1 lit. a Ziff. 2. Der Abzug gilt für Kinder nach Vollendung des 4. bis zur Vollendung des 15. Altersjahres (indexiert per 1.1.2024).
> - **Widerspruch:** Anhang 1 StG und die Wegleitung AR 2025 (ar-wl-2025__c0005) nennen 7'400. Die Merkblatt-Fassung MB 02 (ar-mb-02__c0002) nennt 7'000 und bezeichnet dies als nicht indexierten Gesetzestext.
> - **Lücke:** Eine Wegleitung 2026 fehlt im Wiki. Der Wert 7'400 ist deshalb aus 2025 übernommen. Bitte vor der Abgabe mit der Wegleitung 2026 oder bei einer Fachperson prüfen.
> - **Formular:** Ziff. 23.2 «Kinderabzug: Kind nach Vollendung des 4. bis zur Vollendung des 15. …».
> 
> **Bund · 2026** (getrennt zu deklarieren): CHF 6'800 Kinderabzug vom Einkommen (bund-dbg-2026__art-35), zusätzlich CHF 263 Ermässigung des Steuerbetrags je Kind (bund-dbg-2026__art-36-t4). Beide Werte sind agent-geprüft (Fundstelle geprüft, Abnahme offen).

## q39

**Frage:** Welche Vermögenssteuer-Freibeträge (Sozialabzüge) gelten 2025 in ZH für Alleinstehende und Verheiratete?

**Soll (Referenz):** ZH kennt keine Vermögens-Sozialabzüge, sondern Tarifstufen mit 0 ‰: Grundtarif erste CHF 80'000, Verheiratetentarif erste CHF 159'000 (zh-stg-2025__par-47); kein Betrag pro Kind.

**Antwort des Agenten** (24.0 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **ZH · Steuerjahr 2025**
> 
> Im Kanton Zürich gibt es bei der Vermögenssteuer keinen eigenen Sozialabzug. Der Freibetrag ergibt sich aus der 0‰-Stufe des Tarifs (§ 47 StG ZH):
> 
> | Steuerpflichtige | Steuerfreies Vermögen (0‰-Stufe) | Tarif |
> |---|---|---|
> | **Alleinstehende** | **CHF 80'000** | Grundtarif, § 47 Abs. 1 StG |
> | **Verheiratete** (in ungetrennter Ehe) | **CHF 159'000** | Verheiratetentarif, § 47 Abs. 2 StG |
> 
> Der Verheiratetentarif gilt auch für Verwitwete, Getrennte, Geschiedene und Ledige mit Kindern, die mit diesen zusammenleben.
> 
> Weitere Hinweise:
> - **Kein Abzug im Formular:** Das volle Vermögen wird eingetragen (Ziff. 33 − Ziff. 34 = Ziff. 35). Der Freibetrag wirkt erst bei der Steuerberechnung über den Tarif.
> - **Kein Kinderabzug beim Vermögen:** Pro Kind gibt es keinen Vermögens-Sozialabzug.
> - **Bund:** Der Bund erhebt keine Vermögenssteuer, daher gibt es dort keinen Freibetrag.
> 
> **Status:** Beide Werte sind agent-geprüft (☑️): Die Fundstelle wurde geprüft, die Abnahme durch eine Fachperson steht noch aus.
> 
> **Quellen:**
> - `zh-stg-2025__par-47-t1` (§ 47 Abs. 1 StG ZH, Grundtarif)
> - `zh-vkp-2024-zstb__c0011` (§ 47 Abs. 2 StG ZH, Verheiratetentarif; laut Quelle gilt die VKP für 2024 und 2025)

## q40

**Frage:** Alleinstehende TG 2026, Nettolohn 90'000, ÖV-Abo 2'400, Säule 3a 7'258, Krankenkasse 5'500. Erstelle die Abzüge (Berufskosten, 3a, Versicherungsabzug) Kanton und Bund mit Fundstellen und Status.

**Soll (Referenz):** TG 2026 (Kanton/Bund): Fahrkosten 2'400 (Max. 6'000 / 3'300); übrige Berufskosten 3 % von 90'000 = 2'700 (Min. 2'000, Max. 4'000, beide Ebenen); Säule 3a 7'258 (TG 🟡 extrahiert, Bund ☑️); Versicherungsabzug TG max. 3'500 → 3'500, Bund max. 1'800 → 1'800 (Prämien 5'500 übersteigen beide Maxima).

**Antwort des Agenten** (43.2 s · Tools: 8 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__suche):

> **TG · 2026** · Alleinstehend, Nettolohn 90'000 · Beträge in CHF
> 
> | Abzug | Berechnung | Kanton (Staats-/Gemeindesteuer) | Bund (direkte Bundessteuer) |
> |---|---|---|---|
> | **Berufskosten: Fahrkosten ÖV** | Ist-Kosten 2'400; Limite Kanton 6'000, Bund 3'300 | **2'400** | **2'400** |
> | **Berufskosten: Übrige (3%-Pauschale)** | 3% × 90'000 = 2'700; Min 2'000, Max 4'000 | **2'700** | **2'700** |
> | **Berufskosten gesamt** | | **5'100** | **5'100** |
> | **Säule 3a** | Limite 7'258 (mit 2. Säule). Ohne 2. Säule wäre es 20 % × 90'000 = 18'000, gedeckelt auf 36'288; 7'258 liegt in beiden Fällen darunter | **7'258** | **7'258** |
> | **Versicherungsabzug** (Krankenkasse) | min(Prämie 5'500; Limite) | **3'500** (Limite; 2'000 gehen verloren) | **1'800** (Limite) |
> 
> **Fundstellen und Status**
> 
> - **Fahrkosten ÖV, Kanton:** Limite 6'000 (`tg-wl-2026__c0176`), ☑️ agent-geprüft. Formularposition 10.1, Ziff. 2.5 (`tg-form-01-2026__c0010`).
> - **Fahrkosten ÖV, Bund:** Limite 3'300 (`bund-dbg-2026__art-26`), ☑️ agent-geprüft.
> - **3%-Pauschale, Kanton:** 3% vom Nettolohn, min. 2'000, max. 4'000 (`tg-wl-2026__c0187`), ☑️ agent-geprüft.
> - **3%-Pauschale, Bund:** Der Wert steht nur im TG-Formulareintrag 10.1 (`tg-form-01-2026__c0010`), dort als „Bund: 3 %, 2'000/4'000". Eine eigene Bundesquelle habe ich im Wiki nicht gefunden. Status 🟡 extrahiert; vor Abnahme gegen die Bundes-Wegleitung prüfen.
> - **Säule 3a, Kanton:** Maximum 7'258 mit 2. Säule (`tg-wl-2026__c0089`), ☑️ agent-geprüft. Ohne 2. Säule gilt 20 % des Erwerbseinkommens, max. 36'288 (`tg-wl-2026__c0004`), ☑️.
> - **Säule 3a, Bund:** 7'258 (`bund-bsv-masszahlen-2025-2026__c0003`), ☑️. Ohne 2. Säule 36'288, ☑️.
> - **Versicherungsabzug, Kanton:** Alleinstehend max. 3'500 (`tg-stg__par-34-t3`), ☑️. Formular Ziff. 14 nennt dieselbe Limite und rechnet min(Total; Limite) (`tg-form-01-2026__c0010`).
> - **Versicherungsabzug, Bund:** Alleinstehend 1'800 (`bund-dbg-2026__art-33-t2`), ☑️. Der Wert 2'700 gilt nur ohne Beiträge an Säule 2/3a. Da Sie 3a einzahlen, gilt 1'800 (`tg-wl-2026__c0209`).
> 
> **Hinweise**
> 
> - **Krankenkasse:** Die Ziff. 14 verlangt die **Nettoprämie nach Abzug der IPV** (Prämienverbilligung). Ist 5'500 die Bruttoprämie, sinkt der Betrag, aber über 3'500 liegt er vermutlich trotzdem. Bitte die Jahresbestätigung der Krankenkasse prüfen.
> - **Berufskosten:** Die Fahrkosten werden als Ist-Kosten (ÖV-Abo) angesetzt. Die 225-Tage-Regel gilt nur für Autofahrten und wird hier nicht gebraucht. Verpflegung wurde nicht angegeben und ist deshalb nicht enthalten.
> - **Bund vs. Kanton:** Die Beträge sind getrennt zu deklarieren, Ziff. 14 und Ziff. 10 haben je eine Spalte für Kanton und Bund.

