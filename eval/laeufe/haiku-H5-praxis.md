# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 40 · Lauf: 2026-11-09 14:39
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q01

**Frage:** Mandantin (ZH, 2025) bringt: Lohnausweis, Krankenkassen-Prämienrechnung, Handyrechnung, 3a-Bescheinigung, Hausratversicherungspolice, Spendenquittung Rotes Kreuz CHF 80, Kita-Rechnungen. Welche sind relevant, wofür?

**Soll (Referenz):** Relevant: Lohnausweis (Einkünfte 1.1), Krankenkassenprämien (Versicherungsabzug Ziff. 15, Form. 365), 3a-Bescheinigung (Ziff. 14), Kita-Rechnungen (Ziff. 16.6 Drittbetreuung, max. 25'000 Kanton / 25'800 Bund). Spende CHF 80: unter Mindestbetrag 100 → nicht abziehbar (sofern Total < 100). Nicht relevant: Handyrechnung (Lebenshaltung), Hausratversicherung (kein Versicherungsabzug).

**Antwort des Agenten** (40.5 s · Tools: 8 Aufrufe steuerwiki__ablage, read):

> **ZH 2025: Welche Belege sind relevant, wofür?**
> 
> | Dokument | Relevant? | Wofür (ZH 2025) | Kategorie (KATEGORIEN.md) | Eingereicht? |
> |---|---|---|---|---|
> | Lohnausweis | **ja** | Einkünfte aus unselbständiger Erwerbstätigkeit: Ziff. 1.1, 1.2 sowie Form. 360 (Ziff. 2.1, 2.2, 3, 5), Form. 367 | Belege eingereicht | **ja** (immer, Beilage zur Steuererklärung, § 134 Abs. 1 lit. a StG) |
> | Krankenkassen-Prämienrechnung | **ja** | Versicherungsabzug für Prämien: Ziff. 15, Form. 365 Teil A Ziff. 1–4 und 6 | Belege Sonstiges | nein (Formular Versicherungsprämien ist beizulegen; Prämienbeleg nur auf Verlangen) |
> | Handyrechnung | **nein** | Privattelefon ist Lebenshaltung, nicht abziehbar (Art. 34 lit. a DBG) | keine Steuerbeleg-Kategorie | – |
> | 3a-Bescheinigung | **ja** | Abzug Säule 3a: Ziff. 14.1/14.2 | Belege eingereicht | **ja** |
> | Hausratversicherungspolice | **nein** | Hausrat-Prämien sind nicht abziehbar | keine Steuerbeleg-Kategorie | – |
> | Spendenquittung Rotes Kreuz, CHF 80 | **bedingt** | Ziff. 22.2 (Spenden), nur wenn die Zuwendungen im Jahr insgesamt mindestens CHF 100 erreichen | Belege Sonstiges, falls relevant | nein (Liste aller Zuwendungen auf Verlangen) |
> | Kita-Rechnungen | **bedingt** | Kinderbetreuungskosten: Ziff. 16.6, Limite CHF 25'000 pro Kind (ZH StG § 31 Abs. 4) | Belege Sonstiges (Rechnungen) | nein, aber die Aufstellung der bezahlten Kosten mit Empfängern ist unaufgefordert beizulegen |
> 
> **Zu prüfen bzw. zu entscheiden:**
> 
> - **Spende:** Allein CHF 80 liegen unter der Schwelle von CHF 100 (ZH). Abzug nur, wenn die übrigen Zuwendungen 2025 die Schwelle zusammen erreichen. Das Rote Kreuz muss außerdem eine steuerbefreite Institution mit Sitz in der Schweiz sein; das habe ich nicht gegen eine Quelle geprüft.
> - **Kita:** Abzug nur für Kinder unter 14 Jahren im Haushalt, und nur bei Kosten im Zusammenhang mit Erwerbstätigkeit, Ausbildung oder ähnlichem. Ich brauche das Alter der Kinder und die Erwerbssituation der Mandantin, sonst bleibt der Abzug offen.
> - **Hausrat:** Die Fundstelle für den Ausschluss stammt aus dem Kanton AR. Für ZH habe ich sie nicht einzeln belegt, das Ergebnis (kein Abzug) bleibt aber Teil der allgemeinen Regeln.
> - **Status:** Alle Zuordnungen sind agent-geprüft, die Abnahme ist offen. Die Kategorienliste selbst ist laut Datei noch nicht bestätigt.
> 
> Mandantendaten habe ich nicht im Wiki oder im Gedächtnis gespeichert.

## q02

**Frage:** In welche Ziffer und mit welchem Code der ZH-Steuererklärung 2025 gehört der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb)?

**Soll (Referenz):** Ziff. 1.1 Haupterwerb, Code 100 (Person 1) / 101 (Person 2); Nettolohn Lohnausweis Ziff. 11 (zh-form-300-2025).

**Antwort des Agenten** (24.3 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__suche):

> Der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb) gehört ins **Steuerformular ZH 2025 (Form. 300), Ziff. 1.1 «Haupterwerb unselbständig», Code 100**. Person 2 hat Code 101.
> 
> - **Einsetzen:** Den Nettolohn aus Ziff. 11 des Lohnausweises übernehmen. Dieser ist der Bruttolohn (Ziff. 8) abzüglich AHV/IV/EO/ALV (Ziff. 9), laufender BVG-Beiträge (Ziff. 10.1/10.2) und NBUV-Prämien.
> - **Mehrere Haupterwerbe:** Die Ziff. 11 aller Haupterwerbe von Person 1 werden summiert und ergeben Code 100.
> - **Bund:** Die Zeile gilt gleich für Staats- und Bundessteuer. Es gibt keinen Unterschied in der Bundesspalte.
> - **Beleg:** Der Lohnausweis ist für jeden Arbeitgeber einzureichen (§ 134 Abs. 1 lit. a StG ZH; WL S. 31).
> - **Beachten:** BVG-Einkauf (Ziff. 10.2) ist bereits abgezogen und darf nicht nochmals unter Code 280 erscheinen. Erwerbslücken sollen ausdrücklich bezeichnet werden.
> 
> Quellen: zh-form-300-2025__c0004 (Haupterwerb Person 1), zh-wl-2025__c0032. Status: ☑️ agent-geprüft, die Abnahme durch die Fachperson steht noch aus.

## q03

**Frage:** Lohnausweis Feld F ist angekreuzt (Geschäftsauto). Was bedeutet das für den Fahrkostenabzug (SG 2025)?

**Soll (Referenz):** Feld F angekreuzt → kein Fahrkostenabzug für den Arbeitsweg mit Geschäftsfahrzeug (Privatanteil im Lohn, Lohnausweis Ziff. 2.2).

**Antwort des Agenten** (33.5 s · Tools: 5 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__position, steuerwiki__zeige):

> **Kurz:** Ist Feld F angekreuzt, gibt es im Kanton St. Gallen für 2025 keinen Fahrkostenabzug für den Arbeitsweg. Der Grund: Feld F bedeutet, dass dir der Arbeitgeber die Fahrt zwischen Wohn- und Arbeitsort unentgeltlich stellt, etwa per Sammeltransport oder GA aus geschäftlichen Gründen. Dir entstehen dadurch keine Kosten.
> 
> **Was das für deine Steuererklärung heisst (SG 2025):**
> - **Formular 4, Ziff. 1.1–1.3** (ÖV, Fahrrad, Motorfahrzeug): kein Abzug. Das gilt auch für den Maximalabzug von CHF 8'000.
> - **Fahrkosten im Bund:** Die Wiki-Quellen nennen für den Bund den Maximalbetrag von CHF 3'300. Die Regel «Feld F = kein Abzug» ist für den Bund nicht eigens belegt; ich habe sie nicht geprüft.
> 
> **Achtung zur Kombination Feld F + Geschäftsauto:** Normalerweise steht bei einem Geschäftsauto **nicht** Feld F, sondern der Privatanteil in Ziff. 2.2 (0,9 % des Fahrzeugkaufpreises pro Monat). Die Regeln dazu:
> - **Pauschaler Privatanteil:** Mit diesem Privatanteil ist der Arbeitsweg abgegolten. Es gibt keinen Fahrkostenabzug.
> - **Mit Bordbuch (effektive Abrechnung):** Du kannst die effektiven Kosten für den Arbeitsweg bis zum Maximalabzug (SG CHF 8'000 / Bund CHF 3'300) geltend machen. Der Privatanteil bleibt trotzdem im Lohnausweis. Dafür braucht es ein vollständiges Bordbuch.
> 
> **Empfehlung:** Prüfe zuerst den Lohnausweis. Steht Feld F angekreuzt und zusätzlich ein Privatanteil in Ziff. 2.2, ist das widersprüchlich, und Feld F sollte wohl nicht gesetzt sein. Bei einem reinen Geschäftsauto mit Privatanteil ist der Abzug nur mit Bordbuch möglich. Ist Feld F richtig gesetzt, entfällt der Abzug vollständig.
> 
> **Quellen:** WL SG 2025 (`sg-wl-2025__c0075`, `sg-wl-2025__c0076`), Formular 4 Ziff. 1.3 (`sg-form-4-2025__c0002`), StB 39 Nr. 3 Ziff. 4.1 (`sg-stb-39-3__c0013`). Status: agent-geprüft, Abnahme offen.

## q04

**Frage:** Wie hoch ist der maximale Fahrkostenabzug 2025 in TG (Staatssteuer) und beim Bund, und welcher km-Ansatz gilt für das Auto?

**Soll (Referenz):** TG 2025 Staat max. CHF 6'000 (tg-stg__par-29), Bund max. CHF 3'300 (bund-dbg-2025__art-26); Auto TG gestaffelt 0.60/0.50/0.40 je nach Jahres-km, Bund 0.70.

**Antwort des Agenten** (26.7 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Fahrkosten 2025, Kanton Thurgau (Staatssteuer) und Bund**
> 
> | | Kanton TG (Staatssteuer) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | Maximaler Fahrkostenabzug (Wohn–Arbeitsstätte) | CHF 6'000 pro Jahr | CHF 3'300 pro Person und Jahr |
> | Km-Ansatz Privatauto | Gestaffelt (siehe unten) | CHF 0.70 pro Fahrkilometer |
> 
> **Kanton TG:** Der Auto-Ansatz ist gestaffelt, nicht einheitlich:
> - bis 3'000 km: CHF 0.60/km
> - 3'001–5'000 km: CHF 0.50/km
> - über 5'000 km: CHF 0.40/km
> 
> Die Staffel wird stufenweise berechnet. Beispiel aus der Wegleitung: 8'000 km ergeben CHF 4'000. Der Abzug gilt nur, wenn der öffentliche Verkehr nicht zumutbar ist. Im Normalfall sind die Kosten des ÖV-Abonnements abziehbar. Für Privatauto-Berechnungen bei 100 % Tätigkeit gilt in der Regel maximal 225 Arbeitstage pro Jahr. Parkgebühren sind inbegriffen.
> 
> **Bund:** Der Ansatz ist einheitlich CHF 0.70/km, ebenfalls nur ohne zumutbaren ÖV. Eine Arbeitstage-Regel gibt es nicht. Abziehbar sind die tatsächlichen notwendigen Kosten bis zum Maximalbetrag.
> 
> **Quellen und Status:**
> - TG Maximalbetrag: `tg-stg__par-29` (☑️ agent-geprüft, Abnahme offen)
> - TG Km-Staffel: `tg-bkv__par-1` (☑️ agent-geprüft, Abnahme offen)
> - TG 225 Arbeitstage: `tg-wl-2025__c0003`, Angabe aus der Wegleitung, kein Gesetzeswert (☑️)
> - Bund Maximalbetrag: `bund-dbg-2025__art-26` (☑️)
> - Bund Km-Ansatz: `bund-bkv-2025__anhang-1` (☑️)
> 
> **Hinweis zum Bund:** Die Quellen widersprechen sich beim Maximalbetrag. Art. 26 DBG und RS 2-210 nennen CHF 3'300 (Erhöhung von 3'200 wegen kalter Progression). Die ESTV-Wegleitung 2a 2025 (S. 6) nennt noch CHF 3'200. Ich habe CHF 3'300 übernommen, da es die Gesetzesfassung ist. Falls es für eine konkrete Deklaration relevant ist, bitte gegen die Wegleitung prüfen.
> 
> Der Km-Ansatz des Bundes gilt nur für 2025. Ab Steuerjahr 2026 sind es CHF 0.75/km.
> 
> Die Formularziffern für TG 2025 sind Ziff. 10.1 (Person 1) und Ziff. 10.2 (Person 2) bei den Berufsauslagen unselbständiger Erwerbstätigkeit. Soll ich die Rechenregel dazu noch nachschlagen?

## q05

**Frage:** Welcher km-Ansatz für Autos gilt 2026 bei der direkten Bundessteuer?

**Soll (Referenz):** CHF 0.75 pro km (bund-mm-2025-09-11-kalte-progression-2026__c0004; RS 2-215).

**Antwort des Agenten** (25.2 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Bund 2026: CHF 0.75 pro Fahrkilometer** für das Privatauto (Vorjahr 0.70). Der Abzug gilt für Fahrten zwischen Wohn- und Arbeitsstätte.
> 
> - **Voraussetzung:** Ein öffentliches Verkehrsmittel steht nicht zur Verfügung oder ist objektiv nicht zumutbar.
> - **Höchstbetrag:** Die Fahrkosten insgesamt sind auf CHF 3'300 pro Jahr begrenzt.
> - **Fundstellen:** `bund-wl-2a-2026__c0043` und `bund-wl-2a-2026__c0044` (WL 2a 2026, Ziff. 10); Änderung auf 75 Rappen in `bund-mm-2025-09-11-kalte-progression-2026__c0004`.
> - **Status:** ☑️ agent-geprüft. Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> 
> Für Motorrad mit weissem Kontrollschild gilt CHF 0.40/km. Velo oder Mofa ist mit der Pauschale von CHF 700 pro Jahr abgegolten.
> 
> Nicht geprüft habe ich die km-Ansätze für beruflich veranlasste Geschäftsfahrten (Fahrten zwischen Arbeitsorten, Kundenbesuche). Dafür müsste ich eine separate Suche machen. Wenn du das brauchst, sag Bescheid.

## q06

**Frage:** Maximaler Säule-3a-Abzug 2025 für eine Arbeitnehmerin mit Pensionskasse? Und für eine Selbständige ohne 2. Säule?

**Soll (Referenz):** Mit 2. Säule CHF 7'258; ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288 (bund-bsv-masszahlen-2025-2026__c0003).

**Antwort des Agenten** (25.8 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__vergleich):

> **Arbeitnehmerin mit Pensionskasse (2. Säule), Steuerjahr 2025: CHF 7'258**
> 
> Das ist der obere BVG-Grenzbetrag (8 % davon). Ein Abzug über diesen Betrag hinaus ist nicht möglich, ausser über den nachträglichen Einkauf (Lücken aus den 10 Vorjahren, siehe unten). Fundstelle: `bund-bsv-masszahlen-2025-2026__c0003`.
> 
> **Selbständige ohne 2. Säule, Steuerjahr 2025: 20 % des Erwerbseinkommens, maximal CHF 36'288**
> 
> Die 36'288 entsprechen 40 % des oberen Grenzbetrags. Der Prozentsatz bezieht sich auf das Erwerbseinkommen, der Höchstbetrag gilt zusätzlich. Fundstelle: `bund-bvv3__art-7` und `bund-bsv-masszahlen-2025-2026__c0003`.
> 
> **Die Beträge gelten für Bund, ZH, SG, TG und AR gleich.** Die Kantone übernehmen die Bundeswerte, deshalb musst du den Kanton für diese Zahlen nicht kennen.
> 
> Zum nachträglichen Einkauf: Wer in den zehn vorangehenden Jahren nicht alle zulässigen Beiträge einbezahlt hat, kann eine Lücke nachholen (Bund BVV 3 Art. 7a, seit 01.01.2025). Der Einkauf ist zusätzlich zum ordentlichen Beitrag möglich, und pro Beitragslücke gibt es nur einen Einkauf. Im Einkaufsjahr muss der volle ordentliche Beitrag geleistet werden. Für die Obergrenze des Einkaufs nennt das Wiki CHF 7'258 (Art. 7a, BSV-Masszahlen).
> 
> **Status:** Die Werte sind agent-geprüft (Fundstelle geprüft, Abnahme durch die Fachperson offen). Bitte vor der Eingabe in die Steuererklärung gegen die amtlichen Unterlagen abgleichen.

## q07

**Frage:** Kinderabzug 2025 in AR für ein 10-jähriges Kind – und beim Bund?

**Soll (Referenz):** AR 2025: CHF 7'400 (4.–15. Altersjahr; Anhang 1 StG, ar-stg-anhang-kp__c0001); Bund CHF 6'800 (Art. 35 DBG) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (25.1 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kanton AR, Steuerjahr 2025, Kind 10 Jahre:** CHF 7'400 Kinderabzug vom Einkommen. AR staffelt nach Alter, und 10 Jahre fällt in die Stufe «nach Vollendung des 4. bis zur Vollendung des 15. Altersjahres». Fundstelle: ar-stg-anhang-kp__c0001 (Art. 38 Abs. 1 lit. a Ziff. 2). Formular AR 2025: Ziff. 23.2.
> 
> **Bund (direkte Bundessteuer), Steuerjahr 2025:** CHF 6'800 Kinderabzug. Der Bund kennt keine Altersstaffel, der Betrag gilt für jedes minderjährige Kind. Fundstelle: bund-dbg-2025__art-35.
> 
> Zusätzlich beim Bund: Der Steuerbetrag ermässigt sich um CHF 263 pro Kind (Art. 36 Abs. 2bis DBG, bund-dbg-2025__art-36-t4). Das ist eine separate Ermässigung und nicht dasselbe wie der Kinderabzug vom Einkommen.
> 
> Weitere Kinderposten, falls relevant:
> - AR: CHF 1'000 Versicherungszuschlag pro Kind (ar-stg__art-35-t2) und CHF 25'000 Vermögensfreibetrag pro minderjährigem Kind mit Kinderabzug (ar-stg__art-51).
> - Bund: CHF 700 Versicherungszuschlag pro Kind (bund-dbg-2025__art-33-t5). Vermögensfreibetrag gibt es beim Bund nicht.
> 
> Status: Alle Werte sind ☑️ agent-geprüft. Die Fundstellen sind geprüft, die fachliche Abnahme steht aus. Für die Erklärung bitte die Chunks bzw. die Formulargrundlage vor dem Einreichen gegenprüfen.

## q08

**Frage:** Versicherungsabzug ZH 2025 für ein Ehepaar mit 2 Kindern, beide mit Pensionskasse (Staatssteuer und Bund)?

**Soll (Referenz):** ZH Staat: 5'800 + 2 × 1'300 = 8'400; Bund: 3'700 + 2 × 700 = 5'100 (zh-stg-2025__par-31-t2, bund-dbg-2025__art-33).

**Antwort des Agenten** (26.5 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Ergebnis (Steuerjahr 2025, Kanton Zürich, Ehepaar in ungetrennter Ehe, beide mit Pensionskasse):**
> 
> | | Staatssteuer ZH | Direkte Bundessteuer |
> |---|---|---|
> | Ehepaar mit Beiträgen an 2. Säule/3a | CHF 5'800 | CHF 3'700 |
> | Zuschlag 2 Kinder (je Kind separat) | 2 × CHF 1'300 = CHF 2'600 | 2 × CHF 700 = CHF 1'400 |
> | **Total Versicherungsabzug** | **CHF 8'400** | **CHF 5'100** |
> 
> - **Kanton ZH:** Fundstelle zh-stg-2025__par-31-t2 (Ehepaar CHF 5'800, Kinder CHF 1'300 je Kind). Der Zuschlag gilt pro Kind, für das ein Abzug nach § 34 Abs. 1 geltend gemacht werden kann.
> - **Bund:** Fundstelle bund-dbg-2025__art-33-t2 (Ehepaar CHF 3'700) und art-33-t5 (Kinder CHF 700 je Kind).
> - **Formular ZH 2025:** Ziffer 15, Versicherungsprämien und Zinsen von Sparkapitalien (Code 270). Die Bundesspalte wird separat erfasst. Die Regel für die Eintragung kann ich mit `position zh 2025 15` nachschlagen.
> 
> **Status:** Alle Werte sind ☑️ agent-geprüft, die Abnahme ist noch offen. Der Abzug ist nur mit Beiträgen an die 2. Säule oder Säule 3a gedeckt. Ohne Vorsorgebeiträge greifen die höheren Ansätze ohne Vorsorge (ZH CHF 8'700, Bund CHF 5'550 vor Kinderzuschlägen). Da beide Ehegatten in der Pensionskasse versichert sind, trifft das hier nicht zu.

## q09

**Frage:** Wie hoch ist der Kinderdrittbetreuungsabzug 2025 im Kanton ZH, und gilt 2026 ein anderer Wert?

**Soll (Referenz):** ZH 2025 CHF 25'000 (StG Nachtrag 127, zh-stg-2025__par-31-t4); 2026 CHF 25'300 (zh-stg-2026__par-31-t3). Die VKP ab 2024 (10'400) ist überholt.

**Antwort des Agenten** (26.8 s · Tools: 2 Aufrufe steuerwiki__wert):

> **ZH 2025:** Der Kinderdrittbetreuungsabzug (Staatssteuer) beträgt **CHF 25'000 pro Kind**. Voraussetzungen: Kind hat das 14. Altersjahr noch nicht vollendet, lebt im gleichen Haushalt, und die Kosten stehen in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit. Abgezogen werden nur die nachgewiesenen Kosten, höchstens CHF 25'000.
> - Quelle: zh-stg-2025__par-31-t4 (StG, Fassung Nachtrag 127, Stand 1.1.2025) · Status ☑️ agent-geprüft, Abnahme offen
> - Eine alte VKP-Angabe nennt noch CHF 10'400. Das ist laut Wiki überholt, weil Gesetz und Wegleitung 2025 übereinstimmend CHF 25'000 nennen.
> 
> **ZH 2026:** Ja, der Wert ist anders: **CHF 25'300 pro Kind** (Staatssteuer), leicht höher als 2025.
> - Quelle: zh-stg-2026__par-31-t3 (StG Nachtrag 132 und VKP ab 2026) · Status ☑️ agent-geprüft, Abnahme offen
> - Bei Konkubinat oder alternierender Obhut mit gemeinsamer Sorge gilt je der halbe Abzug, also CHF 12'650.
> 
> **Bund (zum Vergleich):** Die direkte Bundessteuer liegt in beiden Jahren bei **CHF 25'800 pro Kind** (bund-dbg-2025__art-33-t7 und bund-dbg-2026__art-33-t7). Die Altersgrenze von 14 Jahren gilt ebenfalls für beide. Kanton und Bund werden getrennt deklariert.
> 
> **Formular:** Im ZH-Formular steht der Abzug für fremdbetreute Kinder unter Ziff. 16.6 (Code 376). Für Rechenregeln: `position zh 2025 16.6` bzw. `position zh 2026 16.6`.
> 
> Alle Werte sind agent-geprüft, die Abnahme steht noch aus. Vor einer Abgabe sollten die Fundstellen im Gesetzestext nochmals gegen die amtliche Fassung gelesen werden.

## q10

**Frage:** Gibt es im Kanton TG einen Zweiverdienerabzug für die Staatssteuer?

**Soll (Referenz):** Nein, TG kennt keinen kantonalen Zweiverdienerabzug (nur Bund: 50 %, 8'600–14'100).

**Antwort des Agenten** (28.7 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Nein.** Im Kanton Thurgau gibt es für die Staats- und Gemeindesteuer keinen Zweiverdienerabzug. Der Abzug existiert nur bei der direkten Bundessteuer.
> 
> - **Gesetz:** Im Gesetz über die Staats- und Gemeindesteuern des Kantons Thurgau ist kein Zweiverdienerabzug vorgesehen (StP 34 Nr. 25, Fundstelle `tg-stp-34-25__c0001`, ☑️ agent-geprüft).
> - **Wegleitung 2025:** «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug» (WL TG 2025, S. 23, Ziffer 18, `tg-wl-2025__c0104`, ☑️ agent-geprüft).
> - **Formular:** Ziffer 18 (Code 356) betrifft nur die direkte Bundessteuer.
> - **Bund (zum Vergleich):** 50 % des niedrigeren Erwerbseinkommens, mindestens CHF 8'600, höchstens CHF 14'100 (Art. 33 Abs. 2 DBG, `bund-dbg-2025__art-33-t6`, ☑️ agent-geprüft). Dieser Abzug wird separat in der Bundesspalte deklariert.
> 
> Ich habe Steuerjahr 2025 verwendet, weil Sie kein Jahr angegeben haben. Das Wiki sagt auch für 2026, dass es keinen kantonalen Abzug gibt (Hinweis in `tg-stp-34-25__c0012`).
> 
> Eine Praxisbeispiel-Rechnung mit «Fr. 10'000» in StP 34 Nr. 25 (Ziffer 7.2) bezieht sich auf die Berechnung des Bundesabzugs und nicht auf die Staatssteuer.

## q11

**Frage:** SG 2025: Pauschale für übrige Berufskosten? Wie wird sie berechnet?

**Soll (Referenz):** SG 2025: CHF 700 + 10 % des Nettolohns, max. CHF 2'400 (Art. 21 StV SG, WL SG 2025).

**Antwort des Agenten** (24.6 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **SG 2025: Pauschale für übrige Berufskosten** (unselbständige Haupterwerbstätigkeit)
> 
> **Berechnung:** Fr. 700 + 10 % der Nettoeinkünfte, höchstens Fr. 2'400.
> - Nettoeinkünfte = Bruttoeinkünfte abzüglich AHV/IV/EO/ALV/UV- und BVG-Beiträge (ohne Einkäufe).
> - Die Pauschale erreicht ihr Maximum bei Nettoeinkünften von Fr. 17'000 (700 + 1'700 = 2'400). Darüber bleibt sie bei Fr. 2'400.
> - Beispiele: Nettoeinkünfte Fr. 10'000 → Fr. 1'700. Fr. 50'000 → Fr. 2'400.
> - SG kennt kein Minimum. Der Bund hat dagegen einen Mindestbetrag (siehe unten).
> 
> **Nachweis:** Höhere tatsächliche Kosten können statt der Pauschale nachgewiesen werden. Das gilt auch für übrige Berufsauslagen einschliesslich Arbeitszimmer: Übersteigen sie zusammen die Pauschale, müssen alle tatsächlichen Aufwendungen belegt werden. Ein Arbeitszimmer ist nicht zusätzlich zur Pauschale abziehbar (StB 39 Nr. 1).
> 
> **Formular SG 2025:** Ziff. 10.1 (Person 1, Code 438) bzw. Ziff. 10.2 (Person 2, Code 488).
> 
> **Bund (zum Vergleich, separat deklarieren):** 3 % des Nettolohns, mindestens Fr. 2'000, höchstens Fr. 4'000.
> 
> **Quellen und Status:**
> - Art. 21 StV SG (sg-stv__art-21), ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen.
> - WL SG 2025, Ziff. 10.3 (sg-wl-2025__c0080), ☑️ agent-geprüft.
> - Bund: bund-bkv-2025__anhang-1, ☑️ agent-geprüft.
> 
> **Nicht verwechseln:** Bei einer Nebenerwerbstätigkeit gilt eine andere Regel (StB 39 Nr. 9, sg-stb-39-9__c0011): 20 % der Nettoeinkünfte, mindestens Fr. 800, höchstens Fr. 2'400.

## q12

**Frage:** Pauschalabzug Liegenschaftsunterhalt in AR für ein 8-jähriges Einfamilienhaus – und wie in ZH?

**Soll (Referenz):** AR: 10 % (Gebäude bis 10 Jahre) bzw. 20 % des Bruttoertrags, nur bis Bruttomietertrag 100'000 (Art. 25 StV AR, MB 03); ZH: einheitlich 20 % ohne Altersstaffel (ZStB 30.2).

**Antwort des Agenten** (33.9 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Antwort (Steuerjahr 2025, da keines angegeben; für 2026 nicht geprüft):**
> 
> Ein 8-jähriges Gebäude liegt bei beiden Kantonen unter der Altersgrenze von 10 Jahren. Die Bundesregel ist für diesen Fall also gleich wie die AR-Regel.
> 
> | | Kanton | Bund (DBSt) |
> |---|---|---|
> | **AR** | **10 %** des Liegenschaftsertrags (Gebäude ≤ 10 Jahre) | 10 % (automatisch durch die Steuerverwaltung) |
> | **ZH** | **20 %** des Brutto-Mietertrags bzw. Mietwerts, unabhängig vom Alter | **10 %** (Gebäude ≤ 10 Jahre bei Periodenbeginn) |
> 
> **Was dabei wichtig ist:**
> 
> - **AR:** Die Pauschale gilt nur, wenn der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes höchstens CHF 100'000 beträgt und die Liegenschaft ganz oder vorwiegend Wohnzwecken dient. Sonst gelten die tatsächlichen Kosten. Je Gebäude und Jahr kann zwischen Pauschale und tatsächlichen Kosten gewählt werden.
> - **ZH:** Die Pauschale wird auf dem Brutto-Mietertrag bzw. **Mietwert** berechnet. Bei Pauschale entfallen weitere Abzüge ausser Baurechtszinsen. Sie gilt nicht für vorwiegend geschäftlich genutzte Liegenschaften. Wählbar pro Liegenschaft und Steuerperiode.
> - **Bund:** Der Satz steht im Formular in der Bundesspalte bzw. wird in AR automatisch korrigiert. Die Bundesregel ist in den Quellen für AR nicht separat belegt; die 10 % stammen aus der Bundesquelle (Art. 5 LKV).
> 
> **Offene Punkte:**
> 
> - **Selbstbewohntes EFH:** Die Angaben beziehen sich auf den Mietertrag. Ob in AR der Eigenmietwert als Bemessungsgrundlage gilt, geht aus den Quellen nicht eindeutig hervor. In ZH ist der Mietwert ausdrücklich erfasst. Bei einem selbstbewohnten Haus sollte man die AR-Frage vor dem Ausfüllen klären.
> - **Status:** Alle Werte sind agent-geprüft (Fundstelle geprüft, Abnahme durch Fachperson offen).
> 
> **Fundstellen:**
> - AR: `ar-mb-03__c0004`, `ar-wl-2025__c0175`, Formular Ziff. 15 (`ar-form-07-2025__c0003`)
> - ZH: `zh-zstb-30-2__c0002`, `zh-form-350__c0007`, `zh-stg-2025__par-30-t1`
> - Bund: `bund-lkv__art-5`
> 
> Falls Sie das Steuerjahr 2026 meinen, sagen Sie Bescheid, dann prüfe ich die Werte für 2026 nach.

## q13

**Frage:** TG: Welcher Einschlag gilt auf dem Eigenmietwert der selbstbewohnten Liegenschaft am Wohnsitz (Kanton vs. Bund)?

**Soll (Referenz):** TG: Abzug 40 % Kanton, 20 % Bund für dauernd selbstbewohntes Eigentum am Wohnsitz (tg-stg__par-23; WL TG 2025).

**Antwort des Agenten** (26.6 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__wert):

> **Bund (direkte Bundessteuer), Steuerjahr 2025:** Beim Bund gibt es keinen prozentualen Einschlag auf den Eigenmietwert selbst. Er wird nach den ortsüblichen Verhältnissen und der tatsächlichen Nutzung festgesetzt (Art. 21 Abs. 2 DBG; Fundstelle: `bund-dbg-2025__art-21`). ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen.
> 
> Was es beim Bund trotzdem gibt, ist ein Pauschalabzug auf den Brutto-Eigenmietwert für die Unterhaltskosten (LKV Art. 5, `bund-lkv__art-5`, ☑️ agent-geprüft). Er hängt vom Gebäudealter zu Beginn der Steuerperiode (1.1.2025) ab:
> - Gebäude bis 10 Jahre alt: 10 %, Wahlrecht je Periode und Liegenschaft
> - Gebäude über 10 Jahre alt: 20 %
> 
> Der Grenzfall beim Baujahr oder Bezug sollte genau geprüft werden.
> 
> **Kanton:** Der kantonale Eigenmietwert-Einschlag (Prozentsatz auf den Mietwert, der je Kanton verschieden ist) lässt sich nur für einen bestimmten Kanton nennen. Ihre Nachricht beginnt mit «TG:». Ist das der Kanton Thurgau? Sonst sagen Sie mir bitte, ob es Appenzell Ausserrhoden, St. Gallen oder Zürich ist. Ich rechne mit Steuerjahr 2025, bis Sie etwas anderes sagen.

## q14

**Frage:** Bis wann kann ein Treuhänder im Kanton TG für seine Mandanten Fristerstreckung erhalten?

**Soll (Referenz):** Gewerbsmässige Treuhänder für Mandanten bis 31.12. des Deklarationsjahres (StP 155 Nr. 2).

**Antwort des Agenten** (26.3 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kanton TG, Steuerjahr 2025 (Deklarationsjahr 2026):** Treuhänder und Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen, können für ihre Mandanten ein Fristerstreckungsgesuch **längstens bis 31. Dezember 2026** beantragen.
> 
> Stand heute (9. November 2026) heisst das: Es sind noch rund 7 Wochen bis zu diesem Endtermin.
> 
> Die Regel im Einzelnen (StP 155 Nr. 2, tg-stp-155-2__c0002 und c0001):
> 
> - **Weitere Gesuche über den 30. November hinaus** werden abgewiesen, ausser es werden ausserordentliche Gründe glaubhaft gemacht. Allgemeine Hinweise wie starke berufliche Belastung des Vertreters oder fehlende Unterlagen reichen dafür nicht aus.
> - **Private (ohne Treuhänder):** Das erste Gesuch geht grundsätzlich bis 30. September des Deklarationsjahres, weitere in begründeten Fällen bis 30. November. Die Gesuche gehen an das Gemeindesteueramt.
> - **Gewerbliche Treuhänder/Steuerberater:** bis 31. Dezember. Dies ist der Endtermin für Mandanten, die sie vertreten.
> 
> Die Praxis gilt für die Steuerjahre 2025, 2026 und 2027. Die Fundstellen sind als «agent-geprüft» markiert, die Abnahme ist also noch offen. Im Wiki nicht geklärt sind die Gebühren für Treuhänder-Gesuche (§ 39b StV TG regelt Fristerstreckungsgebühren allgemein, Details habe ich nicht geprüft).
> 
> Falls Sie ein anderes Steuerjahr meinen, sagen Sie es mir, dann prüfe ich es neu.

## q15

**Frage:** ZH: Bis wann ist die Steuererklärung 2025 einzureichen und wie lange wird höchstens Fristerstreckung gewährt?

**Soll (Referenz):** Einreichung bis 31.03.2026; Fristerstreckung längstens bis 30. November (ZStB 132.1 / WL ZH 2025).

**Antwort des Agenten** (30.6 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Kanton Zürich, Steuerjahr 2025:** Die ordentliche Einreichefrist war **31. März 2026**. Heute ist der 9. November 2026, die Frist ist also abgelaufen.
> 
> **Fristerstreckung:** Rechtzeitig eingereichte Gesuche werden längstens bis **30. November des Folgejahres** bewilligt, also bis **30. November 2026**. Das gilt aber nur für Gesuche, die **vor Ablauf der Frist am 31. März 2026** beim Gemeindesteueramt eingegangen sind. Nach Ablauf der ordentlichen Frist ist eine Erstreckung nicht mehr möglich. Wiederhergestellt werden kann die Frist höchstens, wenn die Voraussetzungen von § 15 StV bzw. Art. 119 Abs. 2 und 124 Abs. 4 DBG erfüllt sind. Zuständig ist das Gemeindesteueramt.
> 
> Ob der 30. November 2026 für Sie noch relevant ist, hängt davon ab, ob Sie vor dem 31. März 2026 ein Gesuch gestellt haben und es bewilligt wurde. Falls ja, gilt der 30. November 2026 als Frist. Falls nein, ist eine Erstreckung nicht mehr möglich, und Sie sollten sich direkt an das Gemeindesteueramt wenden.
> 
> **Zwei Ausnahmen ohne Gesuch:** Das Gemeindesteueramt verlängert die Frist von Amtes wegen bis **30. September des Folgejahres** für im Kanton wohnhafte Selbstständigerwerbende sowie für ausserhalb des Kantons wohnhafte Steuerpflichtige (L- und B-Fälle). Für diese Gruppen wäre der 30. September 2026 massgebend, falls die Erstreckung registriert wurde.
> 
> **Quellen und Status:**
> - Einreichefrist 31.03.2026: `zh-wl-2025__c0017` (Wegleitung ZH 2025), ☑️ agent-geprüft
> - Fristerstreckung bis 30.11. und Gesuchsfrist: `zh-zstb-132-1__c0023`, `__c0024` (ZStB 132.1), ☑️ agent-geprüft
> - Ausnahme von Amtes wegen bis 30.09.: `zh-zstb-132-1__c0023`, ☑️ agent-geprüft
> 
> **Offene Punkte:**
> - Die Regeln in ZStB 132.1 gelten laut Quelle ab 1.1.2026. Die Vorgängerfassung habe ich nicht geprüft, daher kann ich nicht ausschliessen, dass sie für eine frühere Erstreckung abweichende Daten enthielt.
> - Zu den Kosten einer Fristerstreckung enthalten die Quellen keine Angaben.

## q16

**Frage:** AR: Was kostet die zweite Fristverlängerung?

**Soll (Referenz):** CHF 25 (erste Verlängerung kostenlos, jede weitere CHF 25; MB 18 / WL AR 2025).

**Antwort des Agenten** (24.6 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__wert):

> Die zweite Fristverlängerung kostet **CHF 25**. Das gilt für den Kanton Appenzell Ausserrhoden (AR), Steuerjahr 2025, da Sie kein Jahr angegeben haben.
> 
> - Die erste Fristerstreckung ist kostenlos. Jede weitere kostet CHF 25.
> - Quellen: Art. 59a StV AR (Verfahrensgebühren, Art. 161 ff. StG) und Merkblatt 18 (Gebührenansätze KGV ab 1.9.2025), dort «Fristverlängerungen (im Wiederholungsfall): Fr. 25».
> - Der Status ist ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> - Der Bund erhebt keine eigene Gebühr dafür. Die Fristerstreckung ist kantonal geregelt.
> 
> Gesuche müssen vor Ablauf der Einreichefrist bei der Kantonalen Steuerverwaltung eingehen.

## q17

**Frage:** Krankheitskosten SG 2025: Ab welchem Selbstbehalt sind sie abziehbar – und beim Bund?

**Soll (Referenz):** SG: Selbstbehalt 2 % (Art. 46 StG SG); Bund: 5 % (Art. 33 Abs. 1 lit. h DBG, KS 11).

**Antwort des Agenten** (25.4 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kanton St. Gallen 2025:** Krankheits- und Unfallkosten sind abziehbar, soweit sie **2 % der Nettoeinkünfte** übersteigen. Der Selbstbehalt ist also ab dem ersten Franken über 2 % der Nettoeinkünfte (Nettoeinkommen, Formular Ziff. 20) abziehbar. Behinderungsbedingte Kosten haben keinen Selbstbehalt. Die Pauschale für Diät bei Zöliakie beträgt Fr. 2'500.
> - Fundstelle: sg-stg-2025__art-46 (Status ☑️ agent-geprüft, Abnahme offen)
> - Formular: Ziff. 21.1 Krankheits- und Unfallkosten. Die Regel zur Berechnung des Selbstbehalts im Formular habe ich nicht vollständig abgerufen (`position sg 2025 21.1` liefert sie).
> 
> **Bund (direkte Bundessteuer) 2025:** Krankheits- und Unfallkosten sind abziehbar, soweit sie **5 %** übersteigen. Die Bezugsgrösse ist hier anders als im Kanton: die um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte, nicht das Nettoeinkommen des Kantons. Behinderungsbedingte Kosten (BehiG) sind auch hier ohne Selbstbehalt.
> - Fundstelle: bund-dbg-2025__art-33-t3 (☑️ agent-geprüft, Abnahme offen)
> - Praxis 2025/2026: ESTV-KS 11 (2005). Das KS 11a (publiziert 26.05.2026) gilt laut seiner Ziff. 7 erst ab Steuerperiode 2027, ändert 2025 also nichts.
> 
> **Kurz:** SG 2 % der Nettoeinkünfte, Bund 5 % der verminderten steuerbaren Einkünfte. Beide werden separat deklariert.

## q18

**Frage:** PK-Einkauf CHF 20'000 wurde über den Lohn abgezogen (Lohnausweis Ziff. 10.2). Darf er nochmals in der Steuererklärung abgezogen werden?

**Soll (Referenz):** Nein – BVG-Einkauf über Lohnabzug (Lohnausweis Ziff. 10.2) ist bereits im Nettolohn berücksichtigt; nur direkt bezahlte Einkäufe separat abziehen.

**Antwort des Agenten** (34.0 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Kurz: Nein, bei korrekter Erfassung wird der Einkauf nur einmal abgezogen.** Der Lohnausweis liefert die Grundlage, die Abzugszeile in der Steuererklärung ist die andere Stelle, und beide dürfen nicht doppelt gezählt werden.
> 
> **Warum:**
> - Wenn der Arbeitgeber einen Einkauf über den Lohn abzieht, gehört die Einkaufssumme zum massgebenden Bruttolohn. Sie muss im Lohnausweis separat in der Rubrik «Versicherungsbeiträge» ausgewiesen werden, damit Sie sie abziehen können (KS W03-001, Ziff. 3.3, Bund, gilt für 2025–2027; `bund-ks-w03-001__c0009`).
> - Der Abzug erfolgt in der Steuererklärung unter den Abzügen, nicht beim Lohn. Dabei gilt: Der Betrag wird über den Lohnausweis übernommen, und Sie tragen ihn **nicht zusätzlich von Hand** als zweiten Abzug ein.
> 
> **Was Sie prüfen sollten:**
> 1. Steht die CHF 20'000 in der Lohnausweis-Rubrik «Versicherungsbeiträge» bzw. Ziff. 10.2? Dann ist sie erfasst.
> 2. Kontrollieren Sie, dass Sie den Betrag im Formular nur einmal eintragen, entweder über den Lohnausweis oder als Einkaufsabzug, nicht beides.
> 3. Der Abzug ist nur für Einkäufe zulässig, die Sie selbst finanziert haben. Wurde der Betrag nicht vom Lohn, sondern vom Arbeitgeber bezahlt, gilt eine andere Behandlung.
> 
> **Was ich noch brauche, um die Formularposition genau zu nennen:**
> - **Kanton** (Wohnsitz am 31.12.). Die Ziffer 10.2 ist eine Lohnausweis-Ziffer, deren Bedeutung und Eintragungsort im kantonalen Formular unterschiedlich sein können. Ohne Kanton kann ich keine kantonale Position nennen.
> - **Steuerjahr**: Ich habe 2025 verwendet, weil keines angegeben war. Die Bundesregel ist für 2025–2027 gleich.
> 
> Nennen Sie mir den Kanton (ZH, SG, TG oder AR), dann prüfe ich die genaue Position und die kantonalen Limiten.

## q19

**Frage:** Weiterbildungskosten CHF 15'000 (ZH, 2025), Arbeitgeber hat nichts bezahlt. Wie viel ist abziehbar (Kanton/Bund)?

**Soll (Referenz):** ZH Staat max. CHF 12'400 (zh-stg-2025__par-31-t4); Bund max. CHF 13'000 (bund-dbg-2025__art-33-t4).

**Antwort des Agenten** (25.1 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Abziehbar bei CHF 15'000 selbst getragenen Weiterbildungskosten (ZH, Steuerjahr 2025):**
> 
> - **Kanton Zürich (Staatssteuer):** CHF 12'400
> - **Bund (direkte Bundessteuer):** CHF 13'000
> 
> Die Beträge werden in getrennten Blöcken deklariert. Der Bundesabzug ist also höher als der kantonale.
> 
> **Voraussetzungen, die du prüfen musst:**
> - Die Weiterbildung ist nur abziehbar, wenn die Person einen Abschluss auf Sekundarstufe II hat oder das 20. Altersjahr vollendet hat. Eine Ausbildung bis zum ersten Abschluss auf Sek. II zählt nicht. (zh-stg-2025__par-31-t4; bund-dbg-2025__art-33-t4)
> - Massgebend ist der Zeitpunkt der Fälligkeit bzw. Zahlung, nicht der Kursbesuch. (zh-form-300-2025__c0008)
> - Ob der Arbeitgeber tatsächlich nichts bezahlt hat, sollte mit dem Lohnausweis Ziff. 13.3 abgeglichen werden. Direkt an ein Bildungsinstitut bezahlte Arbeitgeberbeiträge stehen nicht im Lohnausweis und müssen beim Arbeitgeber erfragt werden. Wenn es solche Zahlungen gab, reduziert sich der selbst getragene Betrag entsprechend. (zh-form-367-2025__c0001; Lohnausweis-Regeln ZH 2025)
> 
> **Formular:** Ziff. 16.2 (Code 292) mit hilfsblatt Form. 367. Die Berechnung erfolgt pro Person, wobei der Abzug auf den Limiten gekappt wird. Die Belege (Kursrechnungen) und das ausgefüllte Form. 367 sind beizulegen, wobei die Rechnungen nur auf Verlangen einzureichen sind. (zh-wl-2025__c0207)
> 
> **Status:** Die Werte sind agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Limiten sind verlässlich belegt, die Abnahme durch eine Fachperson steht aber noch aus.

## q20

**Frage:** Spenden CHF 50 an eine gemeinnützige Organisation (TG 2025) – abziehbar?

**Soll (Referenz):** Nein – TG: Zuwendungen nur abziehbar, wenn sie CHF 200 übersteigen (StG TG § 34 Abs. 1 Ziff. 11); Bund: ab CHF 100.

**Antwort des Agenten** (30.5 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__position):

> **Nein, für sich allein nicht abziehbar.** Die CHF 50 fallen im Kanton Thurgau unter den Selbstbehalt und beim Bund unter die Mindestgrenze.
> 
> - **Kanton TG (Staats- und Gemeindesteuer):** Abziehbar ist nur der Teil der freiwilligen Zuwendungen, der **gesamthaft CHF 200 übersteigt** (§ 34 Ziff. 11 StG TG, Chunk `tg-stg__par-34-t4`). Bei CHF 50 ergibt das 0.
> - **Bund (direkte Bundessteuer):** Die Grenze ist **CHF 100**, und zwar als Freigrenze: Erreicht das Jahrestotal CHF 100, ist der ganze Betrag abziehbar, sonst nichts (`bund-dbg-2025__art-33a`). Bei CHF 50 ergibt das ebenfalls 0.
> 
> **Was entscheidend ist:** Die Grenzen gelten für das **Jahrestotal aller Zuwendungen 2025**, nicht pro Spende. Liegt die Summe höher, wirkt das so:
> 
> - Beispiel: Total CHF 250 → Kanton: CHF 50 abziehbar (250 − 200); Bund: CHF 250 abziehbar (über 100, aber höchstens 20 % des Nettoeinkommens).
> 
> **Voraussetzungen für den Abzug (Ziff. 23.2, Formular 6, Code 366):**
> 
> - Die Empfängerin muss eine in der Schweiz ansässige, von der Steuer befreite Organisation mit öffentlichem oder gemeinnützigem Zweck sein. Prüfen Sie sie in der Liste der Steuerverwaltung TG.
> - Religiöse, kulturelle, gesellige oder sportliche Zwecke sowie Sitz im Ausland sind nicht abziehbar. Sammelvermerke wie «diverse Organisationen» werden nicht anerkannt.
> - Eine Spendenbescheinigung ist ab CHF 1'000 pro Zuwendung einzureichen; darunter nur auf Verlangen. Bei CHF 50 ist sie also nicht zwingend, sollten Sie sie aber für den Fall einer Nachfrage aufbewahren.
> 
> **Fazit:** Bei dieser einzelnen CHF-50-Spende gibt es keinen Abzug. Stellen Sie die übrigen Zuwendungen 2025 zusammen; erst wenn das Total CHF 200 (TG) bzw. CHF 100 (Bund) übersteigt, lohnt sich der Abzug.
> 
> *Status der Werte: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).*

## q21

**Frage:** Was ändert sich 2026 bei der Säule 3a (Einkauf) und wo wird das im ZH-Formular 2026 eingetragen?

**Soll (Referenz):** Ab 2026 Einkauf (Nachzahlung) Säule 3a für Beitragslücken ab 2025 (max. 7'258 pro Einkaufsjahr, BVV 3 Art. 7a, KS 18a); ZH-Formular 2026: Ziff. 14.3 (Code 264, Detailfelder 276/278).

**Antwort des Agenten** (29.1 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__suche):

> **Neu 2026: Einkauf in die Säule 3a für Beitragslücken**
> 
> Ab Steuerperiode 2026 können Sie zusätzlich zu den ordentlichen 3a-Beiträgen Beitragslücken in der Säule 3a einkaufen. Voraussetzungen und Grenzen:
> 
> - **Lücken ab 1.1.2025**, innerhalb der letzten zehn Jahre vor dem Einkauf.
> - **Voraussetzungen:** In den Lückenjahren wurden AHV/IV/EO-Beiträge geleistet, und im Einkaufsjahr wurde der volle ordentliche Maximalbeitrag einbezahlt.
> - **Höchstbetrag:** CHF 7'258 pro Steuerjahr, für Kanton und Bund gleich.
> - **Praktische Folge für 2026:** Faktisch ist nur die Lücke 2025 einkaufbar, weil frühere Lücken nicht erfasst sind.
> 
> **Ordentliche 3a-Limiten 2026** (unverändert gegenüber 2025):
> - Mit 2. Säule: CHF 7'258
> - Ohne 2. Säule: 20 % des Erwerbseinkommens, max. CHF 36'288
> 
> **Eintrag im Formular ZH 2026**
> - **Ziff. 14.3 «Einkauf Säule 3a»**: Person 1 Code **276**, Person 2 Code **278**. Die Summe geht in die Hauptkolonne Code **264**.
> - Die ordentlichen Beiträge bleiben in **Ziff. 14.1/14.2** (Code 260/261, effektiv 262/263).
> - Berechnung je Person: min(Einkauf; Summe der Lücken ab 1.1.2025 innert zehn Jahren; 7'258).
> - Belege: Einkaufsbescheinigung der 3a-Einrichtung, 3a-Bescheinigung für den ordentlichen Beitrag im Einkaufsjahr als Nachweis des Maximalbetrags, und ein Nachweis der AHV/IV/EO-Beiträge im Lückenjahr.
> 
> **Vorbehalte**
> - Das reguläre Formular und die Wegleitung ZH 2026 sind laut Stand 09.11.2026 noch nicht publiziert. Die Zuordnung stützt sich auf die Fassung für unterjährige Steuerpflicht. Ziffern und Codes bitte am regulären Formular prüfen.
> - Die Werte sind agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Rechtsgrundlage ist nur über die Wegleitung 2026 belegt. Der Artikel in BVV 3 ist nicht aus einem geöffneten Chunk verifiziert.
> - Ich habe den 3a-Einkauf gemeint. Der BVG-Einkauf in die 2. Säule ist davon getrennt und nicht Teil dieser Antwort.
> 
> Fundstellen: `zh-wl-2026-uj__c0077` (Einkauf-Obergrenze), `zh-wl-2026-uj__c0075` (ordentliche Limiten), `zh-form-300-2026-uj__c0008` (Ziff. 14.1–14.3), `bund-wl-2a-2026__c0051` (Bund).

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (36.6 s · Tools: 8 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurz:** Die Verrechnungssteuer (35 %) auf Schweizer Dividenden holen Sie über die **Steuererklärung** zurück, nicht über ein separates Formular. Der Anspruch wird im **Wertschriftenverzeichnis** ausgewiesen. Die Steuerbehörde prüft dabei die Deklaration. Die Kanton-Position im Formular kann ich ohne Kanton noch nicht nennen.
> 
> **Voraussetzungen**
> 
> 1. **Deklarationspflicht (Art. 23 Abs. 1 VStG):** Sie deklarieren die verrechnungssteuerbelasteten Erträge und das Vermögen, aus dem sie fliessen, in der Steuererklärung der Steuerperiode, in der die Leistung fällig wurde. Dann ist die Pflicht erfüllt, und bei Erfüllung der weiteren Voraussetzungen der Art. 21 ff. VStG besteht der Rückerstattungsanspruch. (`bund-ks-vst-48__c0003`, KS VST 48, Ziff. 3.1)
> 2. **Tax-Voucher:** Seit dem neuen System ist ein Tax-Voucher Voraussetzung für die Rückerstattung. Wenn eine ausländische Bank oder Depotstelle eine Ertragsabrechnung oder ein Steuerverzeichnis ausstellt, legen Sie dem Rückerstattungsantrag einen Tax-Voucher bei. Er allein begründet aber keinen Anspruch. (`bund-ks-vst-21__c0007`, KS VST 21, Ziff. 4)
> 3. **Verfahren bei fehlender Deklaration:** Reicht die steuerpflichtige Person keine Steuererklärung ein oder deklariert sie nur teilweise, wird nach pflichtgemässem Ermessen veranlagt (Art. 130 DBG). Eine Steuererklärung mit dem Vermögen als Beweismittel im Einspracheverfahren (Art. 132 Abs. 3 DBG) schliesst die Rückerstattung nicht aus, sofern auf die Einsprache einzutreten ist und die Voraussetzungen erfüllt sind. (`bund-ks-vst-48__c0009`, KS VST 48, Ziff. 4)
> 
> **Wo der Anspruch steht**
> 
> - Im **Wertschriftenverzeichnis** der kantonalen Steuererklärung, mit Steuerwert, Bruttoertrag und Verrechnungssteuer je Titel. Die Kantons-Position und Formularziffer finden sich nur mit Kanton und Jahr.
> - Der **DA-1 2026** (`bund-form-da1-2026__c0002`, `…__c0006`) betrifft nicht die Schweizer Verrechnungssteuer. Er ist der Antrag auf Anrechnung **ausländischer** Quellensteuern (z. B. USA) auf Dividenden und Zinsen. Er wird zusammen mit der Steuererklärung und dem Wertschriftenverzeichnis beim Kanton eingereicht, in dem Sie am 31.12. wohnen. Verwechseln Sie ihn daher nicht mit der Schweizer VSt.
> 
> **Nicht belegt:** Den Formularnamen für den Rückerstattungsantrag an die Eidgenössische Steuerverwaltung (Formular 25 ist mein Vorwissen) habe ich im Wiki nicht gefunden. Das Wiki nennt nur das Formular 102M für den Verrechnungssteuerersatz (KS VST 21, Ziff. 7–8). Den Antragsweg prüfe ich gern gezielt nach, wenn Sie den Kanton nennen.
> 
> Ich habe mit Steuerjahr 2026 gesucht, weil das laufende Jahr 2026 ist. Für die Kantonsposition brauche ich noch den **Wohnsitzkanton (AR, SG, TG oder ZH)**. Dann suche ich die genaue Position im Wertschriftenverzeichnis, z. B. mit `position <kt> 2026 Verrechnungssteuer`.

## q23

**Frage:** Vergleiche den Versicherungsabzug 2025 für Alleinstehende ohne Kinder in AR, SG, TG, ZH und beim Bund.

**Soll (Referenz):** Alleinstehend ohne Kinder 2025 (mit 2. Säule/3a): AR 2'700 · SG 3'400 · TG 3'500 · ZH 2'900 · Bund 1'800.

**Antwort des Agenten** (26.8 s · Tools: 1 Aufrufe steuerwiki__vergleich):

> **Versicherungsabzug 2025, Alleinstehende ohne Kinder (CHF pro Jahr)**
> 
> | Gebiet | Mit Vorsorge (Standard) | Ohne Vorsorge (ohne 2. Säule) | Fundstelle Standard |
> |---|---|---|---|
> | **Bund** | 1'800 | 2'700 | bund-dbg-2025__art-33-t2 |
> | **ZH** | 2'900 | 4'350 | zh-stg-2025__par-31-t2 |
> | **SG** | 3'400 | 3'900 | sg-stg-2025__art-45-t2 |
> | **TG** | 3'500 | nicht anwendbar | tg-stg__par-34-t3 |
> | **AR** | 2'700 | nicht anwendbar | ar-stg__art-35-t2 |
> 
> **Einordnung**
> - **Höchster Standardabzug:** TG (3'500), knapp vor SG (3'400). Der Bund ist mit 1'800 am tiefsten.
> - **Höchster Abzug ohne Vorsorge:** ZH (4'350), dann SG (3'900). Der Bund liegt bei 2'700.
> - **Kantonsvergleich:** ZH hat den tiefsten Standardabzug unter den Kantonen, die einen Wert haben, nämlich 2'900 – AR liegt bei 2'700 und ist damit tiefer. Die Reihenfolge ist also: TG 3'500 > SG 3'400 > ZH 2'900 > AR 2'700.
> - **Gesamtverteilung:** Alle Kantone liegen über dem Bundeswert.
> 
> **Hinweise**
> - Die Schlüssel sind im Wiki mit «mit Vorsorge» und «ohne Vorsorge» benannt. Ob der Abzug «ohne Vorsorge» für eine Person gilt, hängt davon ab, ob sie Beiträge an die berufliche Vorsorge leistet. Das ist die Interpretation der Schlüsselnamen; die genaue Anwendungsregel habe ich nicht im Wortlaut geprüft.
> - TG und AR führen im Wiki keinen separaten Satz ohne Vorsorge. Ob das gesetzlich so ist oder ob dort nur die Lücke im Wiki liegt, habe ich nicht überprüft.
> - Alle Werte haben den Status ☑️ (agent-geprüft: Fundstelle geprüft, Abnahme durch Fachperson offen). Vor einer Verwendung in einer Steuererklärung sollten sie gegen die amtlichen Texte bestätigt werden.

## q24

**Frage:** Steuerfreie Vermögensbeträge (Sozialabzüge) 2025 in SG für ein Ehepaar mit einem minderjährigen Kind?

**Soll (Referenz):** SG 2025: 150'000 (Ehepaar) + 20'000 pro minderjähriges Kind = 170'000 (sg-stg-2025__art-64).

**Antwort des Agenten** (24.2 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> Für ein Ehepaar mit einem minderjährigen Kind beträgt der Vermögens-Sozialabzug im Kanton St. Gallen 2025 insgesamt **CHF 190'000**:
> 
> - **Ehepaar (gemeinsam steuerpflichtig): CHF 150'000** (2 × CHF 75'000)
> - **Kind: CHF 20'000** zusätzlich
> 
> Die Beträge gelten für die Staats- und Gemeindesteuer (Kanton SG).
> 
> **Fundstellen:**
> - Art. 64 Abs. 1 lit. a StG SG (Chunk `sg-stg-2025__art-64`): CHF 75'000 für jeden Steuerpflichtigen. Das ist im Wortlaut geprüft.
> - Art. 64 Abs. 1 lit. b StG SG (Chunk `sg-stg-2025__art-64`): zusätzlich CHF 20'000 für jedes minderjährige Kind unter elterlicher Sorge oder Obhut, für das ein Kinderabzug nach Art. 48 Abs. 1 lit. a StG beansprucht werden kann. Ebenfalls im Wortlaut geprüft.
> - Ehepaar-Betrag CHF 150'000 (Chunk `sg-wl-2025__c0118`, Wegleitung): Das Wiki-Eintrag ist agent-geprüft, die Abnahme ist noch offen.
> 
> **Bund:** Die direkte Bundessteuer kennt keine Vermögenssteuer, daher gibt es dort keinen Vermögens-Sozialabzug.
> 
> **Hinweise:**
> - Die Abzüge richten sich nach den Verhältnissen am Ende der Steuerperiode bzw. der Steuerpflicht (Art. 64 Abs. 2 StG).
> - Die Regel gilt bis 31.12.2025 und wurde durch `sg-stg-2026` ersetzt. Für 2026 müsste man separat nachsehen.
> - Im Formular SG 2025 stehen die Sozialabzüge Vermögen unter Ziff. 36.1–36.3 (alleinstehend / verheiratet / Kind). Die Zeile für das Kind habe ich nicht separat geprüft; das lässt sich mit `position sg 2025 36` nachschlagen.

## q25

**Frage:** Welcher Verzugszins gilt 2026 für die direkte Bundessteuer?

**Soll (Referenz):** 4.00 % (RS 2-215, bund-rs-2-215__c0010/c0011).

**Antwort des Agenten** (23.7 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__zeige):

> Für die direkte Bundessteuer gilt im Steuerjahr 2026 ein **Verzugs- und Rückerstattungszins von 4,00 %** (2025: 4,50 %).
> 
> Quelle: RS 2-215, Abschnitt 3 «Zinssätze … für das Steuerjahr 2026» (Fundstelle `bund-rs-2-215__c0010`). Die Änderung tritt laut Rundschreiben am 1. Januar 2026 in Kraft, und das Rundschreiben gilt bis 31. Dezember 2026. Der Status ist ☑️ agent-geprüft: Fundstelle geprüft, Abnahme durch Fachperson offen.
> 
> Zum Vergleich, ebenfalls aus derselben Quelle:
> - **Vergütungszins für Vorauszahlungen:** 0,00 % (2025: 0,75 %)
> - **Ausgleichszins:** Der Bund kennt keinen Ausgleichszins.
> 
> Der Verzugszins gilt für die verspätete Zahlung der DBSt (Art. 162 Abs. 3 und Art. 164 Abs. 1 DBG). Die konkreten Zahlungstermine werden über die kantonale Bezugsstelle festgelegt.

## q26

**Frage:** Wann wird der Eigenmietwert abgeschafft und gilt das schon für 2026?

**Soll (Referenz):** Abschaffung per 1.1.2029 (Bundesratsbeschluss 01.04.2026); für 2025–2028 gilt bisheriges Recht – 2026 also noch Eigenmietwert.

**Antwort des Agenten** (27.1 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurz:** Der Eigenmietwert wird per **1. Januar 2029** abgeschafft. **Für 2026 gilt er noch**, die Besteuerung läuft also unverändert weiter.
> 
> - **Bund:** Der Bundesrat hat am 1. April 2026 beschlossen, die Reform der Wohneigentumsbesteuerung auf den 1. Januar 2029 in Kraft zu setzen. Danach entfällt auf selbstgenutztem Wohneigentum die Besteuerung des Eigenmietwerts. Quelle: `bund-mm-eigenmietwert-abschaffung__c0002` (Medienmitteilung, Status: 🟡 extrahiert, Abnahme offen).
> - **Kompensation:** Die Kantone können zum Ausgleich eine Objektsteuer auf Zweitliegenschaften einführen (gleiche Quelle).
> - **Liegenschaftsunterhalt:** Laut Medienmitteilung gilt der Abzug der Unterhaltskosten ab 2029 weiterhin (`bund-mm-eigenmietwert-abschaffung__c0004`). Ich habe das nicht im Detail geprüft.
> - **2026 beim Bund:** Der Eigenmietwert ist steuerbar. Die Pauschalen für Liegenschaftskosten bleiben bestehen: 20 % bei Gebäuden über 10 Jahre alt, 10 % bei Gebäuden bis 10 Jahre alt (Stand Gebäudealter am 1.1.2026; `bund-lkv__art-5`, ☑️ agent-geprüft). Auf dem Eigenmietwert selbst gibt es beim Bund keinen prozentualen Abzug.
> 
> **Offen:** Du hast keinen Kanton genannt. Die Eigenmietwert-Bewertung legen die Kantone fest, deshalb hängt der konkrete Betrag für 2026 vom Kanton ab. Wenn du mir sagst, ob es um AR, SG, TG oder ZH geht, schaue ich die kantonalen Werte nach. Für die Abschaffung in den Kantonen selbst habe ich noch keine Angaben geprüft; die Abschaffung gilt jedenfalls für den Bund ab 2029.

## q27

**Frage:** Zitiere die Regel zum Abzug privater Schuldzinsen im DBG (Steuerjahr 2025) mit Artikel.

**Soll (Referenz):** Art. 33 Abs. 1 lit. a DBG (Fassung 2025): private Schuldzinsen im Umfang der steuerbaren Vermögenserträge (Art. 20, 20a, 21) und weiterer CHF 50'000.

**Antwort des Agenten** (23.4 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Art. 33 Abs. 1 lit. a DBG** (Steuerjahr 2025, Fundstelle `bund-dbg-2025__art-33-t1`):
> 
> > «Von den Einkünften werden abgezogen: a. die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken. Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten oder ihr sonst wie nahe stehenden natürlichen Person zu Bedingungen gewährt, die erheblich von den im Geschäftsverkehr unter Dritten üblichen Bedingungen abweichen»
> 
> Die Regel gilt laut Wiki für 2025 (bis 2025-12-31, ersetzt durch 2026). Der Chunk nennt keinen Verifikationsstatus, daher ist das nicht als ✅ markiert.
> 
> Zur Einordnung: Der Abzug ist auf die steuerbaren Vermögenserträge (Art. 20, 20a, 21) plus 50 000 Franken begrenzt. Die Schuldzinsen für Darlehen von Kapitalgesellschaften an beteiligte oder nahestehende Personen zu nicht marktüblichen Bedingungen sind nicht abzugsfähig.

## q28

**Frage:** Ist ein Leasingvertrag für das Privatauto steuerlich relevant? Was ist mit den Leasingraten?

**Soll (Referenz):** Leasingraten sind keine Schuldzinsen und grundsätzlich nicht abziehbar (Lebenshaltung); relevant nur für Fahrkosten-Begründung/Geschäftsauto, Vermögen (kein Eigentum).

**Antwort des Agenten** (30.3 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> **Kurz:** Ein Leasingvertrag für ein rein privat genutztes Auto ist steuerlich nicht abziehbar. Die Leasingraten gehören zu den nicht abzugsfähigen Lebenshaltungskosten. Relevant wird das Auto nur über die Fahrkosten zum Arbeitsweg.
> 
> **Leasingraten (Bund, Steuerjahr 2025)**
> - KS 22a, Ziff. 3.3 (`bund-ks-22a__c0015`, ✅ Fundstelle geprüft): «Leasingraten für privat genutzte Güter enthalten keine abzugsfähigen Zinsanteile.» Ein Zinsabzug über die Leasingrate fällt also weg.
> - Die Raten sind damit für das Privatauto kein Abzug.
> 
> **Fahrkosten zum Arbeitsweg (Bund und ZH, 2025)**
> - Wer das private Auto für den Arbeitsweg benutzt, kann Fahrkosten als Berufsauslagen abziehen. Die Pauschale ist pro km berechnet, nicht über die Leasingrate.
> - Bund (Formular 9–14, `bund-form-9-14-2025__c0002`): Auto CHF –.70/km, Maximum CHF 3'300.–.
> - ZH (`zh-wl-2025__c0063`): Auto 70 Rp./km. Die Begründung für die Autobenützung muss angekreuzt werden (`zh-wl-2025__c0063`).
> - Für die Autobenützung braucht es eine Begründung, etwa fehlende ÖV-Verbindung oder Zeitersparnis über 1 Stunde pro Tag (Formular 9–14, `bund-form-9-14-2025__c0006`).
> - Ob eine Leasingrate beim Berufsauslagen-Abzug in ZH anders behandelt wird, habe ich nicht geprüft.
> 
> **Offen:**
> - **Kanton:** Ich brauche deinen Wohnsitz am 31.12. Die Angaben oben sind Bund plus ZH. Für AR, SG oder TG prüfe ich das gern separat.
> - **Steuerjahr:** Ich habe 2025 verwendet. Sag mir, falls du 2026 meinst.
> - **Geschäftliche Nutzung:** Falls das Auto auch für Geschäftsfahrten genutzt wird (nicht Arbeitsweg), müsste man das Berufsauslagen-Regime prüfen. Dazu habe ich noch keine Fundstelle.

## q29

**Frage:** Wie hoch ist der Kinderabzug im Kanton Bern 2025?

**Soll (Referenz):** Nicht im Wiki (nur Bund, AR, SG, TG, ZH).

**Antwort des Agenten** (23.9 s · Tools: 1 Aufrufe steuerwiki__wert):

> Im Steuer-Wiki ist der Kanton Bern nicht erfasst. Ich kann dir deshalb keinen Kinderabzug für Bern 2025 nennen. Der Wiki deckt nur Bund sowie die Kantone AR, SG, TG und ZH ab.
> 
> Was ich belegen kann, ist der **Bundes-Kinderabzug 2025** (direkte Bundessteuer, Kanton und Bund sind getrennt zu betrachten):
> 
> - **Abzug vom Einkommen:** CHF 6'800 pro minderjährigem oder in Ausbildung stehendem Kind. Der Betrag gilt einheitlich, ohne Altersstaffel und ohne Zuschlag für auswärtige Ausbildung. Fundstelle: Art. 35 DBG, Status ☑️ agent-geprüft (Abnahme offen).
> - **Steuerbetrag-Ermässigung:** CHF 263 pro Kind (Art. 36 Abs. 2bis DBG). Dieser Abzug gilt zusätzlich und darf nicht mit dem Einkommensabzug verwechselt werden.
> - **Versicherungsabzug-Zuschlag:** CHF 700 pro Kind (Art. 33 Abs. 1 lit. a/b DBG).
> 
> Für den Kanton Bern musst du die Werte aus dem Berner Steuergesetz und der kantonalen Wegleitung 2025 entnehmen. Die kantonale Erklärung deckt Kanton und Bund zusammen ab. Wenn du mir Belege oder Unterlagen für Bern gibst, kann ich sie einordnen, aber die Berner Beträge kann ich nicht aus dem Wiki liefern.

## q30

**Frage:** Ehepaar TG 2025, beide angestellt (Nettolohn 80'000 und 30'000), pendelt mit ÖV-Abo (CHF 1'200 bzw. 900). Erstelle die Abzüge Berufskosten (Fahrkosten, Verpflegung ohne Kantine, Pauschale übrige) je Person für Kanton und Bund mit Fundstellen.

**Soll (Referenz):** TG 2025 je Person: Fahrkosten = ÖV-Abo effektiv (1'200 bzw. 900; Max. 6'000 Staat / 3'300 Bund); Verpflegung ohne Kantine 15/Tag, max. 3'200 (beide Ebenen); übrige Pauschale 3 %: P1 80'000 → 2'400, P2 30'000 → 900 → Minimum 2'000 (beide Ebenen, BKV TG § 4a / BKV Bund).

**Antwort des Agenten** (41.0 s · Tools: 9 Aufrufe steuerwiki__position, steuerwiki__wert):

> ## Berufskosten Ehepaar TG 2025 (Kanton und Bund)
> 
> **Annahmen:** Wohnsitz TG am 31.12.2025, beide 100 % angestellt, Nettolohn laut Lohnausweis Ziff. 11 = 80'000 bzw. 30'000. Kein Geschäftsfahrzeug, kein Arbeitgeber-Zuschuss zu den Fahrkosten (Lohnausweis Feld F nicht angekreuzt), Abo selbst bezahlt, Arbeitsweg über ca. 1 km.
> 
> **Kanton TG und Bund ergeben hier dieselben Beträge** (gleiche Pauschalen und Verpflegungsansätze; die Fahrkosten-Maxima 6'000 bzw. 3'300 werden nicht erreicht).
> 
> | Position | Formular | Person 1 (80'000) | Person 2 (30'000) |
> |---|---|---|---|
> | Fahrkosten ÖV-Abo | Ziff. 2.1 (Code 206 / 246) | 1'200 | 900 |
> | Verpflegung ohne Kantine (Fr. 15 pro auswärtiger Hauptmahlzeit) | Ziff. 3.1 (Code 214 / 254) | Tage × 15, max. 3'200 | Tage × 15, max. 3'200 (anteilig bei Teilzeit) |
> | Übrige Berufskosten, Pauschale 3 % Nettolohn | Ziff. 4 (Code 220 / 260) | 2'400 | 2'000 (3 % = 900, daher Minimum) |
> | **Summe ohne Verpflegung** | | **3'600** | **2'900** |
> 
> **Verpflegung:** Die Arbeitstage fehlen. Der Höchstbetrag von 3'200 wird ab 214 Arbeitstagen erreicht. Bei 220 Tagen ergibt sich 3'200, bei 200 Tagen 3'000, bei 100 Tagen 1'500. Der Abzug setzt voraus, dass die Heimkehr am Mittag unzumutbar ist (grosse Entfernung oder sehr kurze Pause). Ist der Lohnausweis in Feld G angekreuzt oder gibt es eine Kantine/Verbilligung, gilt Ziff. 3.2 mit Fr. 7.50 pro Tag, max. 1'600.
> 
> **Vorbehalte:**
> - Die Pauschale nicht zusätzlich zu effektiven Kosten abziehen. Vom Arbeitgeber getragene Kosten sind nicht abziehbar.
> - Die ÖV-Beträge gelten nur ohne Arbeitgeber-Vergütung (Lohnausweis Ziff. 2.3 prüfen).
> - Bei einer Entfernung unter 1 km entfällt der Fahrkostenabzug.
> 
> ## Fundstellen
> 
> - Fahrkosten TG: Form. 4.2 Ziff. 2.1, `tg-form-04-2-2025__c0002`; Wegleitung `tg-wl-2025__c0177`; Maximum 6'000 `tg-stg__par-29`
> - Fahrkosten Bund: Maximum 3'300 `bund-dbg-2025__art-26`; Ansätze `bund-bkv-2025__anhang-1`
> - Verpflegung TG: Ziff. 3.1, `tg-form-04-2-2025__c0003`; `tg-bkv__par-2-t1`; Wegleitung `tg-wl-2025__c0183`
> - Verpflegung verbilligt TG: Ziff. 3.2, `tg-bkv__par-2-t2`, `tg-wl-2025__c0185`
> - Verpflegung Bund: `bund-bkv-2025__anhang-1` (15 Fr. voll, 7.50 Fr. halb, 3'200 Fr. Jahr)
> - Pauschale 3 %: Ziff. 4, `tg-form-04-2-2025__c0004`; `tg-bkv__par-4a`; Wegleitung `tg-wl-2025__c0187`; Bund `bund-bkv-2025__anhang-1` (min. 2'000, max. 4'000)
> - Summe: Ziff. 10.1 (`tg-form-01-2025__c0010`) bzw. 10.2 für Person 2
> 
> **Status:** Alle Fundstellen sind agent-geprüft, die Abnahme steht aus.
> 
> **Offen:** Arbeitstage je Person, Entfernung Wohnort–Arbeitsort, Heimkehr-Möglichkeit am Mittag, Lohnausweis Feld F/G. Mit diesen Angaben lässt sich die Verpflegung exakt berechnen.

## q31

**Frage:** Ehepaar ZH 2026, beide erwerbstätig, Kind 3 Jahre in der Kita (Kosten CHF 30'000). Wie viel Drittbetreuung ist abziehbar (Kanton und Bund)?

**Soll (Referenz):** ZH 2026 Kanton max. CHF 25'300 pro Kind (zh-stg-2026__par-31-t3); Bund 2026 max. CHF 25'800 (bund-dbg-2026__art-33-t7). Abzug je Ebene getrennt.

**Antwort des Agenten** (26.3 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Ergebnis: Kita-Kosten von CHF 30'000 sind im Kanton und beim Bund je auf den Höchstbetrag begrenzt.**
> 
> | | Höchstbetrag pro Kind | Abzug bei CHF 30'000 |
> |---|---|---|
> | Kanton Zürich (Staatssteuer) | CHF 25'300 | **CHF 25'300** |
> | Bund (direkte Bundessteuer) | CHF 25'800 | **CHF 25'800** |
> 
> Die Abzüge werden getrennt deklariert. Der Bund hat den höheren Höchstbetrag, deshalb ist sein Abzug um CHF 500 höher.
> 
> **Voraussetzungen, die hier erfüllt sind:**
> - Das Kind ist unter 14 Jahren (3 Jahre) und lebt im gleichen Haushalt.
> - Beide Eltern sind erwerbstätig, die Kosten hängen also mit der Erwerbstätigkeit zusammen.
> - Es ist ein Ehepaar, deshalb gilt der volle Höchstbetrag und nicht die halbe Regel für Konkubinat oder alternierende Obhut.
> 
> **Zu beachten:**
> - Der Abzug betrifft nur Kosten während der Arbeitszeit. Kosten für Sport, Musik, Vereine oder Nachhilfe sind nicht abziehbar.
> - Der Abzug steht im Formular unter Ziffer 16.6 (Code 376). Belegt wird mit den Kita-Rechnungen und dem Zahlungsnachweis. Bei einer angestellten Betreuungsperson braucht es zusätzlich eine Kopie des Lohnausweises.
> - Wenn die Kosten nur pauschal ausgewiesen sind, werden 20 % als Lebenshaltungskosten gekürzt. Bei den Rechnungen der Kita entfällt das.
> - Das Steuerwiki verwendet für das Steuerjahr 2026 das Formular für die unterjährige Steuerpflicht, weil das reguläre Formular 2026 noch nicht publiziert ist. Die Ziffern und Codes sollten Sie am definitiven Formular prüfen.
> 
> **Quellen (Status ☑️ agent-geprüft, Abnahme offen):**
> - ZH: `zh-form-300-2026-uj__c0008`, `zh-wl-2026-uj__c0105`, Gesetz `zh-stg-2026__par-31-t3`
> - Bund: `bund-dbg-2026__art-33-t7`

## q32

**Frage:** SG 2025: Einfamilienhaus (Baujahr 2010), selbst bewohnt. Pauschalabzug Liegenschaftsunterhalt Kanton und Bund?

**Soll (Referenz):** SG 2025: 20 % des Eigenmietwerts, ohne Altersstaffel (sg-stv__art-29); Bund: Gebäude zu Beginn 2025 über 10 Jahre alt → 20 % (bund-lkv__art-5).

**Antwort des Agenten** (26.2 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Ja, sowohl SG als auch Bund kennen den Pauschalabzug, aber mit unterschiedlichen Sätzen.** Für das Baujahr 2010 ergibt sich:
> 
> | | Satz | Bemessungsgrundlage | Fundstelle |
> |---|---|---|---|
> | **Kanton SG 2025** | **20 %** | Bruttomietertrag ohne Nebenkosten bzw. angerechneter Eigenmietwert | sg-stv__art-29 · ☑️ agent-geprüft |
> | **Bund 2025** | **20 %** | Brutto-Eigenmietwert | bund-lkv__art-5 · ☑️ agent-geprüft |
> 
> - **SG:** Der Satz hängt nicht vom Gebäudealter ab, also gilt 20 % unabhängig vom Baujahr.
> - **Bund:** Massgebend ist das Alter am Beginn der Steuerperiode (1.1.2025). Das Gebäude ist 15 Jahre alt, also gilt der Satz für Gebäude über 10 Jahre (20 %). Der Satz für Gebäude bis 10 Jahre (10 %) entfällt.
> - **Wahlrecht:** Pro Periode und Liegenschaft können Sie zwischen Pauschale und den tatsächlichen Kosten wählen.
> - **Eintrag im SG-Formular:** Ziff. 15, Unterhalts- und Verwaltungskosten für Liegenschaften (Code 716). Die Bundesspalte ist separat zu deklarieren.
> 
> **Offen:**
> - Die Pauschale bezieht sich auf den *angerechneten* Eigenmietwert. Im SG wird der Eigenmietwert zuerst um 30 % herabgesetzt (sg-stg-2025__art-34). Ob die 20 % auf den Wert nach dieser Reduktion zu rechnen sind, habe ich in den Chunks nicht ausdrücklich gefunden. Das prüfe ich noch, bevor Sie einen Betrag festlegen.
> - Beide Sätze sind als agent-geprüft markiert, die Abnahme durch eine Fachperson ist noch offen.

## q33

**Frage:** ZH 2025: Kind 19 Jahre, in Lehre (Ausbildung). Kinderabzug Kanton und Bund?

**Soll (Referenz):** ZH 2025 Kanton CHF 9'300 (volljährig in Erstausbildung, zh-stg-2025__par-34); Bund CHF 6'800 (bund-dbg-2025__art-35) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (27.3 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Kurz:** Ja, für ein 19-jähriges Kind in Lehre gibt es in beiden Steuern einen Kinderabzug. Die Höhe ist im Kanton und beim Bund verschieden.
> 
> | | Kanton ZH 2025 | Bund 2025 |
> |---|---|---|
> | **Kinderabzug** (vom Einkommen) | **CHF 9'300** (§ 34 Abs. 1 lit. a StG) · ☑️ `zh-stg-2025__par-34` | **CHF 6'800** (Art. 35 Abs. 1 lit. a DBG) · ☑️ `bund-dbg-2025__art-35` |
> | **Versicherungsabzug-Zuschlag** | **CHF 1'300** pro Kind · ☑️ `zh-stg-2025__par-31-t2` | **CHF 700** pro Kind · ☑️ `bund-dbg-2025__art-33-t5` |
> | **Abzug vom Steuerbetrag** | keiner | **CHF 263** pro Kind · ☑️ `bund-dbg-2025__art-36-t4` |
> 
> Die Lehre gilt als berufliche Erstausbildung, daher gilt der volle Kinderabzug in beiden Steuern. Beim Bund gibt es keinen höheren Satz für Ausbildung; der Betrag ist derselbe wie für Minderjährige.
> 
> **Voraussetzungen:**
> - Das Kind muss in beruflicher Erstausbildung stehen und volljährig sein.
> - Sie müssen den Unterhalt zur Hauptsache bestreiten, und das Kind muss auf Ihre Unterstützung angewiesen sein (ZH: § 34 StG, ZStB 34.1 Rz 9–12 `zh-zstb-34-1-bis-2025__c0005`/`c0006`). Verdient das Kind selbst so viel, dass es sich selbst unterhalten kann, entfällt der Abzug (Bund: KS 30 Ziff. 10.3 `bund-ks-30__c0062`/`c0063`).
> - Bei getrennt lebenden oder geschiedenen Eltern gelten Sonderregeln, wer den Abzug geltend machen kann (ZStB 34.1 Rz 20–23 `zh-zstb-34-1-bis-2025__c0012`; KS 30 Ziff. 14.10–14.12 `bund-ks-30__c0121`/`c0125`). Das ist hier nicht geklärt.
> 
> **Formular ZH 2025:** Ziff. 24.1 «Abzug für Kinder in Ihrem Haushalt» (Code 370), bzw. Code 372, falls das Kind ausserhalb des Haushalts lebt. Die Versicherungsabzüge stehen in Ziff. 15 (Code 270).
> 
> **Offen / zu prüfen:**
> - Ob das Kind sich selbst unterhalten kann, hängt vom Lehrlingslohn ab. Diesen Betrag bitte mit der Lehrvertrags-Lohnabrechnung prüfen.
> - Die Fundstellen sind agent-geprüft; die Abnahme durch die Fachperson steht noch aus.

## q34

**Frage:** ZH 2025: Lohnausweis Feld G angekreuzt (Kantine). Welche Verpflegungspauschale gilt und in welche Ziffer des Berufsauslagenformulars?

**Soll (Referenz):** Verbilligte Verpflegung: CHF 7.50 pro Arbeitstag, max. CHF 1'600 pro Jahr (LS 631.33, zh-pauschalierung-berufsauslagen-2025__c0004); Form. 360 Ziff. 2.1 (verbilligt); Bund gleich.

**Antwort des Agenten** (24.6 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__suche):

> **Verpflegungspauschale: CHF 7.50 pro Arbeitstag, höchstens CHF 1'600 pro Jahr** (ZH 2025, Staats- und Bundessteuer gleich).
> 
> **Position:** Hilfsblatt Berufskosten, **Form. 360, Ziff. 2.1 (verbilligt)**, **Code 206** für Person 1 (Code 226 für Person 2). Der Betrag gehört in die Spalte Staatssteuer und in die Spalte Bundessteuer.
> 
> **Berechnung:** min(Arbeitstage mit Kantinenverpflegung × 7.50; 1'600). Die Arbeitstage stehen im Arbeitszeitnachweis.
> 
> **Voraussetzungen:**
> - Die Pause erlaubt keine Heimkehr, und es entstehen trotzdem Mehrkosten.
> - Keine Mittagsheimfahrt. Sie schliesst den Verpflegungsabzug aus.
> - Nicht zusammen mit Ziff. 2.1 voll (CHF 15) oder Ziff. 2.2 (Schicht).
> 
> **Bund:** Bei Kantine gilt in der Regel Kanton = Bund. Der Bund gewährt nur den halben Abzug bei Verbilligung; Barbeitrag oder Gutscheine werden beim Bund anders behandelt, die Kantine nicht.
> 
> **Belege:** Lohnausweis (Feld G angekreuzt) und Arbeitszeitnachweis. Der Lohnausweis ist immer einzureichen.
> 
> **Status:** Fundstellen agent-geprüft (☑️), Abnahme offen. Quelle: zh-form-360-2025__c0003 und zh-pauschalierung-berufsauslagen-2025__c0004.

## q35

**Frage:** SG 2025: Kapitalbezug Säule 3a CHF 100'000. Wird das mit dem übrigen Einkommen besteuert? Wo deklarieren?

**Soll (Referenz):** Nein – Kapitalleistungen aus Vorsorge werden getrennt vom übrigen Einkommen (separate Jahressteuer) besteuert; SG Formular 1 Ziff. 40.1 (Säule 3a), Total Ziff. 41.

**Antwort des Agenten** (25.7 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__position):

> **Kurz:** Nein, die CHF 100'000 werden nicht zum übrigen Einkommen gerechnet. Sie werden separat besteuert, und zwar mit einer eigenen Jahressteuer.
> 
> **Besteuerung (SG 2025)**
> - **Kanton:** einfache Steuer von 2,0 % für Ehegatten bzw. 2,2 % für übrige Steuerpflichtige. Bei 100'000 ergibt das 2'000 bzw. 2'200 einfache Steuer, bevor der Steuerfuss angewendet wird. Der Ehegattensatz gilt auch für Alleinstehende, die mit Kindern oder unterstützten Personen zusammenleben.
> - **Bund:** ein Fünftel der Tarife nach Art. 36 DBG. Diesen Betrag habe ich nicht berechnet, weil ich dafür den Bundestarif nicht geprüft habe.
> - **Abzüge:** Für diese separate Steuer gibt es keine allgemeinen und keine Sozialabzüge.
> - **Mehrere Leistungen:** Bei mehreren Kapitalleistungen werden die Beträge des Jahres 2025 zusammengerechnet.
> 
> **Deklaration**
> - Formular 1 SG 2025, **Ziff. 40.1** («Kapitalleistungen aus Vorsorge», Säule 3a).
> - Die Bescheinigung der Bank oder Versicherung über die Kapitalauszahlung 2025 muss beigelegt werden.
> - Der Betrag steht nicht in Ziff. 6.4. Gemäss Wegleitung dient die Angabe der Information. Die Steuer berechnet die Behörde separat.
> - Die Abweichungen für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor. Im Formular gibt es dafür keine eigene Bundesspalte.
> 
> **Quellen:** Formular 1 SG 2025, Chunk sg-form-1-2025__c0014 (Ziff. 40.1); Wegleitung SG 2025, Chunk sg-wl-2025__c0119 (Ziff. 40). Status: agent-geprüft, Abnahme offen.

## q36

**Frage:** ZH 2025: Geschiedener Mandant zahlt Unterhaltsbeiträge an die Ex-Frau (CHF 24'000) und für das minderjährige Kind (CHF 12'000). Was ist abziehbar, in welcher Ziffer?

**Soll (Referenz):** Ex-Ehefrau CHF 24'000 voll abziehbar, Ziff. 13.1 (Code 254); Kinderalimente CHF 12'000 abziehbar bis und mit Monat der Volljährigkeit, Ziff. 13.2 (Code 255); Empfänger versteuert; Bund gleich (Art. 33 Abs. 1 lit. c DBG).

**Antwort des Agenten** (27.8 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__suche):

> **Ergebnis (ZH 2025): beide Beträge sind abziehbar, im Abzugsteil des Formulars.**
> 
> | Zahlung | Ziffer | Code | Betrag | Abzug |
> |---|---|---|---|---|
> | Unterhalt an die Ex-Frau (geschiedene Ehegattin) | **Ziff. 13.1** | 254 | CHF 24'000 | voll abziehbar |
> | Kinderalimente (minderjähriges Kind) | **Ziff. 13.2** | 255 | CHF 12'000 | abziehbar, aber nur bis und mit dem Monat, in dem das Kind 18 wird |
> 
> **Kanton und Bund:** Bei beiden Ziffern ist der Kanton-Abzug gleich wie der Bundes-Abzug (Kanton = Bund), es braucht also keine separate Bundesspalte.
> 
> **Wichtige Einschränkungen:**
> - **Ziff. 13.2:** Die CHF 12'000 müssen auf die Monate bis zum 18. Geburtstag des Kindes aufgeteilt werden. Spätere Zahlungen sind nicht abziehbar. Ist das Kind 2025 noch minderjährig, aber der Geburtstag liegt im Jahr, ist nur der Teil bis zu diesem Monat abziehbar. Die Monatszuordnung fehlt in der Angabe und muss aus den Zahlungsbelegen kommen.
> - **Bund (Ziff. 13.2):** Abziehbar sind nur familienrechtlich geschuldete und effektiv bezahlte Alimente. Freiwillige Zahlungen fallen weg. Ob die Zahlungen auf einem Urteil oder einer Vereinbarung beruhen, muss also belegt sein.
> - **Kinderabzug:** Wer Alimente für ein minderjähriges Kind zahlt, bekommt für dieses Kind keinen Kinderabzug. Prüfen, ob der Mandant für das Kind noch einen Kinderabzug geltend macht.
> - **Nur periodische Zahlungen:** Eine Kapitalabfindung gilt als Schuldentilgung und ist nicht abziehbar. Naturalleistungen (Miete, Krankenkassenprämien, Schuldzinsen) sind gleichgestellt.
> - **Empfänger:** Die Ex-Frau versteuert die CHF 24'000 in Ziff. 5.1 (Code 160). Die Kinderalimente gehen in Ziff. 5.2 (Code 161) und sind nur bis zum Monat der Volljährigkeit einkünftig.
> 
> **Belege:** Scheidungsurteil oder Unterhaltsvereinbarung sowie Zahlungsnachweise. Einreichung nur auf Verlangen, aber im Zweifel beilegen.
> 
> **Fundstellen:** zh-form-300-2025__c0007 (Ziff. 13.1/13.2), zh-wl-2025__c0075 (13.1), zh-wl-2025__c0076 (13.2), zh-wl-2025__c0207 (Belege).
> 
> **Status:** Die Ziffern sind agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Bundes-Einschränkung zu freiwilligen Zahlungen steht unter «Beachten» in Ziff. 13.2 und ist bei der Abnahme zu bestätigen.

## q37

**Frage:** TG 2025: Mandant bringt Steuerberatungsrechnung, Kreditkartenabrechnung, Mietvertrag und Motorfahrzeugversicherung. Was davon ist relevant?

**Soll (Referenz):** Steuerberatungsrechnung: nein; Motorfahrzeugversicherung: nein; Kreditkartenabrechnung: bedingt (nur als Nachweis/Schuld per 31.12.); Mietvertrag: bedingt (Wochenaufenthalt/Arbeitszimmer/Adressnachweis) – laut belege-relevanz.

**Antwort des Agenten** (31.9 s · Tools: 6 Aufrufe steuerwiki__ablage, read, steuerwiki__wert):

> **Kanton TG, Steuerjahr 2025.** Von den vier Dokumenten ist nur der Mietvertrag bedingt relevant, und nur in Sonderfällen. Die Kreditkartenabrechnung ist ebenfalls nur bedingt relevant. Steuerberatung und Motorfahrzeugversicherung sind nicht relevant.
> 
> | Dokument | Steuerrelevant? | Ablage (KATEGORIEN.md) |
> |---|---|---|
> | **Steuerberatungsrechnung** | **Nein.** Kosten für Steuerberatung und Steuererklärung im Privatvermögen sind nicht abziehbar (Bund, Wegleitung 2a, c0057). | Keine Steuerbeleg-Kategorie. Kein Steuerbeleg. |
> | **Kreditkartenabrechnung** | **Bedingt.** Die Abrechnung selbst ist kein Beleg. Sie ist nur Nachweis für einzelne abziehbare Zahlungen (Spenden, Arzt-/Zahnarzt, Weiterbildung, Berufsauslagen, Sollzinsen), wenn die Originalrechnung fehlt. | Nur wenn daraus ein Abzug belegt wird: «Belege Sonstiges» (Einreichung unklar; Zeile «Eingereicht?» = nein, Unsicherheit nennen). Sonst nicht ablegen. |
> | **Mietvertrag** | **Bedingt.** Die Miete der selbstbewohnten Wohnung ist Lebenshaltung und nicht abziehbar (Art. 34 lit. a DBG). Relevant nur bei Untervermietung, Wochenaufenthalt am Arbeitsort oder Vermietung. | Bei Selbstbewohnung: keine Kategorie. Bei Untervermietung: «Mietverträge / Mietzinsabrechnung» (Ziff. 8.1, Form. 7 Mieterträge; Einreichung unklar). |
> | **Motorfahrzeugversicherung** | **Nein.** Versicherungsprämien und Unterhalt des Privatfahrzeugs sind Lebenshaltung. | Keine Steuerbeleg-Kategorie. |
> 
> Zwei Hinweise:
> 
> - **Motorfahrzeugversicherung:** Das Fahrzeug selbst ist steuerrelevant, nicht die Police. Es steht im Vermögen (Ziff. 30.4, Code 422) mit Marke, Kaufpreis und Anschaffungsjahr. Dafür braucht man den Fahrzeugausweis oder den Kaufvertrag, nicht die Versicherungspolice.
> - **Kreditkartenabrechnung:** Wenn Belege zu einzelnen Zahlungen fehlen, muss der Mandant die Originalrechnungen nachreichen.
> 
> Die Zuordnungen sind laut `KATEGORIEN.md` noch nicht von consis bestätigt. Der Wiki-Befund zu den Kategorien ist agent-geprüft, die Abnahme steht aus.

## q38

**Frage:** AR 2026: Wie hoch ist der Kinderabzug für ein 10-jähriges Kind? Ist der Wert gesichert?

**Soll (Referenz):** AR 2026: CHF 7'400 laut Anhang 1 StG (indexiert), aber Status STRITTIG (MB 02 / StG-Text nennen andere Beträge; Wegleitung 2026 fehlt) → Fachperson.

**Antwort des Agenten** (25.7 s · Tools: 2 Aufrufe steuerwiki__wert):

> **AR 2026, Kinderabzug für ein 10-jähriges Kind: CHF 7'400 (Kanton), nicht gesichert.**
> 
> Ein 10-jähriges Kind fällt in die Staffel «nach Vollendung des 4. bis zur Vollendung des 15. Altersjahres».
> 
> - **Kanton AR:** CHF 7'400 · Status ⚠️ strittig. Fundstelle: `ar-stg-anhang-kp__c0001`, Art. 38 Abs. 1 lit. a Ziff. 2. Anhang 1 StG und Wegleitung 2025 nennen 7'400 (indexiert per 1.1.2024). Die Merkblätter MB 02 (Stand 18.08.2026, Ziff. 2) nennen 7'000 und sagen selbst, dass es der nicht indexierte Gesetzestext ist. Die Quellen widersprechen sich, deshalb ist der Betrag nicht gesichert. Die Abnahme durch eine Fachperson steht aus.
> - **Bund (direkte Bundessteuer):** CHF 6'800 pro Kind, unabhängig vom Alter (Art. 35 Abs. 1 lit. a DBG). Status ☑️ agent-geprüft, Abnahme offen. Die Fundstelle ist geprüft, aber noch nicht abgenommen.
> 
> Weitere Kinderwerte, falls relevant (alle ☑️ agent-geprüft, Abnahme offen):
> - AR Versicherungszuschlag pro Kind: CHF 1'000 (Art. 35 t2)
> - AR Vermögensfreibetrag pro Kind: CHF 25'000 (Art. 51)
> - Bund Versicherungszuschlag pro Kind: CHF 700
> - Bund Steuerbetragsermässigung pro Kind: CHF 263
> 
> Im AR-Formular gehört der Abzug zu Ziff. 23.2 (Kind nach Vollendung des 4. bis zur Vollendung des 15. Altersjahres).
> 
> Für die Steuererklärung 2026 würde ich 7'400 mit dem Vermerk «Quellen widersprechen sich» übernehmen und vor Einreichung bei der Fachperson bzw. der Steuerverwaltung AR gegen den Gesetzestext prüfen lassen.

## q39

**Frage:** Welche Vermögenssteuer-Freibeträge (Sozialabzüge) gelten 2025 in ZH für Alleinstehende und Verheiratete?

**Soll (Referenz):** ZH kennt keine Vermögens-Sozialabzüge, sondern Tarifstufen mit 0 ‰: Grundtarif erste CHF 80'000, Verheiratetentarif erste CHF 159'000 (zh-stg-2025__par-47); kein Betrag pro Kind.

**Antwort des Agenten** (26.0 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **ZH 2025, Vermögenssteuer: steuerfreie Beträge**
> 
> Im Kanton Zürich gibt es keinen eigenen Sozialabzug beim Vermögen. Der Freibetrag ist die erste 0‰-Stufe des Vermögenssteuertarifs (§ 47 StG ZH, S. 24–25):
> 
> | Steuerpflichtige | Steuerfrei (0‰) | Fundstelle |
> |---|---|---|
> | Alleinstehend (Grundtarif, Abs. 1) | CHF 80'000 | zh-stg-2025__par-47-t1 |
> | Verheiratet (Verheiratetentarif, Abs. 2) | CHF 159'000 | zh-stg-2025__par-47-t2 |
> 
> - **Verheiratetentarif:** Er gilt für in ungetrennter Ehe lebende Ehegatten. Er gilt auch für Verwitwete, Getrennte, Geschiedene und Ledige, die mit Kindern im Sinn von § 34 Abs. 1 lit. a zusammenleben.
> - **Kinder:** Beim Vermögen gibt es keinen Abzug pro Kind (zh-stg-2025 § 47, keine Fundstelle für einen Kinderabzug).
> - **Bund:** Die direkte Bundessteuer kennt keine Vermögenssteuer, daher gibt es dort keinen Freibetrag.
> 
> **Status:** ☑️ agent-geprüft. Ich habe die Gesetzestexte geöffnet und die Beträge bestätigt, die Abnahme ist aber noch offen. Der Chunk ist als gültig für 2025 markiert und wird durch zh-stg-2026 ersetzt.
> 
> **Formular:** Das steuerbare Vermögen steht in Ziff. 37 (Code 498). Ein eigenes Feld für den steuerfreien Betrag gibt es nicht. Er ergibt sich aus dem Tarif.

## q40

**Frage:** Alleinstehende TG 2026, Nettolohn 90'000, ÖV-Abo 2'400, Säule 3a 7'258, Krankenkasse 5'500. Erstelle die Abzüge (Berufskosten, 3a, Versicherungsabzug) Kanton und Bund mit Fundstellen und Status.

**Soll (Referenz):** TG 2026 (Kanton/Bund): Fahrkosten 2'400 (Max. 6'000 / 3'300); übrige Berufskosten 3 % von 90'000 = 2'700 (Min. 2'000, Max. 4'000, beide Ebenen); Säule 3a 7'258 (TG 🟡 extrahiert, Bund ☑️); Versicherungsabzug TG max. 3'500 → 3'500, Bund max. 1'800 → 1'800 (Prämien 5'500 übersteigen beide Maxima).

**Antwort des Agenten** (50.9 s · Tools: 12 Aufrufe steuerwiki__wert, steuerwiki__suche):

> ## Abzüge Alleinstehende, TG 2026 (Stand 9.11.2026)
> 
> Annahmen: Nettolohn CHF 90'000 laut Lohnausweis Ziff. 11, Wohnsitz TG am 31.12., ÖV-Abo ist die einzige Fahrkostenposition, 7'258 ist der ordentliche 3a-Beitrag (kein Einkauf).
> 
> Alle Werte haben den Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> ### 1. Berufskosten
> 
> | Position | Kanton TG | Bund |
> |---|---|---|
> | Fahrkosten ÖV (tatsächlich) | 2'400 (Max. 6'000) | 2'400 (Max. 3'300) |
> | Pauschale übrige Berufskosten: 3 % von 90'000, min. 2'000, max. 4'000 | 2'700 | 2'700 |
> | **Total Berufskosten** | **5'100** | **5'100** |
> 
> - Fahrkosten TG: `tg-wl-2026__c0176` (Max. 6'000). Bund: `bund-dbg-2026__art-26` (Max. 3'300).
> - Übrige Berufskosten TG: `tg-bkv__par-4a` (3 %, 2'000–4'000). Die Fundstelle ist die Verordnung von 2025, die Formularziffer ist Form. 4.2 Ziff. 4. Bund: `bund-rs-2-215__c0006` und `bund-bkv-2026__anhang-1` (Art. 26 lit. c DBG).
> - Die Pauschale ersetzt nur übrige Berufskosten. Sie wird zusätzlich zu den Fahrkosten abgezogen. Höhere Nachweise sind möglich, dafür fehlen hier Belege.
> - Verpflegung ist nicht angegeben und deshalb nicht berücksichtigt.
> 
> ### 2. Säule 3a
> 
> | Position | Kanton TG | Bund |
> |---|---|---|
> | Beitrag 3a (Beitrag 7'258, Limite mit 2. Säule) | **7'258** | **7'258** |
> 
> - TG: `tg-wl-2026__c0089` (Max. 7'258 mit 2. Säule, 36'288 ohne). Formularziffer Ziff. 13.1/13.2, Code 314/315.
> - Bund: `bund-bsv-masszahlen-2025-2026__c0003` (7'258 mit 2. Säule), `bund-bvv3__art-7` (20 %, max. 36'288).
> - Ohne 2. Säule gilt 20 % des Erwerbseinkommens, also 18'000 bei 90'000. Der Abzug von 7'258 ist deshalb in jedem Fall zulässig.
> 
> ### 3. Versicherungsabzug (Krankenkasse 5'500)
> 
> | Position | Kanton TG | Bund |
> |---|---|---|
> | Limite Alleinstehende | 3'500 | 1'800 (mit 2. Säule oder 3a) |
> | **Abzug** | **3'500** | **1'800** |
> | Nicht abzugsfähig | 2'000 | 3'700 |
> 
> - TG: `tg-stg__par-34-t3` (3'500). Formular 5.2 Teil B: `tg-form-05-2-2026__c0002`. Formularziffer Ziff. 14 (Code 324/328).
> - Bund: `bund-dbg-2026__art-33-t2` (1'800). Der Wert 2'700 ohne Vorsorge (`bund-dbg-2026__art-33-t5`) gilt hier nicht, weil 3a bezahlt wird.
> - Abzugsfähig ist die Nettoprämie nach Prämienverbilligung (`tg-wl-2026__c0206`, `tg-wl-2026__c0207`). Erhält die Person IPV, ist der Betrag tiefer. Liegt die Nettoprämie dann noch über 3'500 bzw. 1'800, bleibt der Abzug auf den Limiten.
> 
> ### Zusammenfassung
> 
> | | Kanton TG | Bund |
> |---|---|---|
> | Berufskosten | 5'100 | 5'100 |
> | 3a | 7'258 | 7'258 |
> | Versicherung | 3'500 | 1'800 |
> | **Total** | **15'858** | **14'158** |
> 
> Offen: Ob die 5'500 Brutto- oder Nettoprämie sind (IPV-Bescheid nötig), ob die 7'258 ordentlicher Beitrag oder Einkauf sind, und ob Verpflegungskosten anfallen.

