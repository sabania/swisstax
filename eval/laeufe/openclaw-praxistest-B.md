# OpenClaw-Testlauf: fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuermem` · Fragen: 40 · Lauf: 2026-11-09 08:34
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## q01

**Frage:** Mandantin (ZH, 2025) bringt: Lohnausweis, Krankenkassen-Prämienrechnung, Handyrechnung, 3a-Bescheinigung, Hausratversicherungspolice, Spendenquittung Rotes Kreuz CHF 80, Kita-Rechnungen. Welche sind relevant, wofür?

**Soll (Referenz):** Relevant: Lohnausweis (Einkünfte 1.1), Krankenkassenprämien (Versicherungsabzug Ziff. 15, Form. 365), 3a-Bescheinigung (Ziff. 14), Kita-Rechnungen (Ziff. 16.6 Drittbetreuung, max. 25'000 Kanton / 25'800 Bund). Spende CHF 80: unter Mindestbetrag 100 → nicht abziehbar (sofern Total < 100). Nicht relevant: Handyrechnung (Lebenshaltung), Hausratversicherung (kein Versicherungsabzug).

**Antwort des Agenten** (59.5 s · Tools: 21 Aufrufe read, read, exec, message):

> Für ZH, Steuerjahr 2025 sind vier Dokumente relevant, eines nur bedingt, und Handy und Hausrat sind es nicht. Alle Angaben stammen aus dem Steuer-Wiki mit Status ☑️ agent-geprüft. Die Beurteilung bleibt bei SB/ML.
> 
> ## Relevant
> 
> | Dokument | Wofür (ZH 2025) | Kanton / Bund | Fundstelle |
> |---|---|---|---|
> | **Lohnausweis** | **Ziff. 1.1**: Nettolohn aus Ziff. 11. Zusätzlich Berufskosten (Form. 360), dafür Felder F und G, Ziff. 10.2, 13 und 15 prüfen. | Eine Zeile für Staat und Bund. Berufskosten-Pauschale 3 % des Nettolohns, mind. CHF 2'000, max. CHF 4'000, bei Staat und Bund gleich. | `zh-wl-2025__c0032`, `beleg-lohnausweis` |
> | **Krankenkassen-Prämienrechnung** | **Ziff. 15** (Form. 365 Teil A): Prämien nach Abzug der Prämienverbilligung, ohne Doppelkürzung. | Kanton: CHF 5'800 verheiratet / CHF 2'900 übrige, plus CHF 1'300 je Kind. Bund: CHF 3'700 / CHF 1'800, plus CHF 700 je Kind. Die höheren Ansätze «ohne 2. Säule/3a» gelten nur, wenn weder die Person noch der Arbeitgeber in die 2. Säule oder 3a einzahlen. | `zh-wl-2025__c0084`, `__c0086`, `bund-dbg-2025__art-33-t2` |
> | **3a-Bescheinigung** | **Ziff. 14.1 / 14.2**: nur 2025 tatsächlich einbezahlte Beträge. Bescheinigung beilegen. | Mit 2. Säule max. CHF 7'258, ohne 2. Säule max. CHF 36'288 bzw. 20 % des Erwerbseinkommens. Staat und Bund gleich. | `zh-wl-2025__c0081` |
> 
> ## Bedingt relevant
> 
> **Kita-Rechnungen** gehören in **Ziff. 16.6** (Abzug für fremdbetreute Kinder).
> - **Limite:** Kanton CHF 25'000, Bund CHF 25'800, je Kind (`zh-stg-2025__par-31-t4`, `bund-dbg-2025__art-33-t7`).
> - **Bedingungen:**
>   - Das Kind ist unter 14 (Jahrgang 2011–2025) und lebt im gleichen Haushalt.
>   - Die Betreuung hängt mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit zusammen. Bei Ehepaaren müssen beide erwerbstätig sein.
> - **Rechnen:** Subventionen abziehen. Wird die Verpflegung separat ausgewiesen, rechnet man sie heraus, denn sie ist Lebenshaltung (`beleg-kinderbetreuung-rechnungen`). Eine ZH-spezifische Pauschale dafür fand ich im Wiki nicht.
> - **Folgeabzüge:** Mit Kindern kommen der Kinderabzug in Ziff. 24.1 (Kanton CHF 9'300 / Bund CHF 6'800) und der Kinder-Zuschlag bei Ziff. 15 dazu. Beides sind Sozialabzüge, kein Beleg.
> 
> ## Spendenquittung Rotes Kreuz, CHF 80
> 
> Der Betrag ist **allein nicht abziehbar**. Ziff. 22.2 verlangt gesamthaft mindestens CHF 100 pro Jahr, bei Staat und Bund (`bund-dbg-2025__art-33a`, `zh-info-spenden__c0003`).
> 
> Die Schwelle gilt für das Jahrestotal. Bitte die Mandantin nach weiteren Spenden 2025 fragen. Erreicht das Total CHF 100, ist es abziehbar bis max. 20 % des Nettoeinkommens (Ziff. 21). Der Empfänger muss ein steuerbefreiter Verein oder eine Stiftung mit Sitz in der Schweiz sein.
> 
> ## Nicht relevant
> 
> - **Handyrechnung:** Das ist Lebenshaltung und nicht abziehbar (Art. 34 lit. a DBG, `bund-dbg-2025__art-34`, `beleg-privatrechnungen-alltag`). Eine ZH-Sonderregel für beruflich genutzte Handys fand ich im Wiki nicht. Berufliche Auslagen sind in der Berufskosten-Pauschale mit enthalten.
> - **Hausrat-Police:** Die Belegkarte stuft sie als «nein» ein. Ein ausdrücklicher Ausschluss ist nur für AR und SG belegt. Für ZH und Bund fand ich in den hinterlegten Wegleitungen keinen ausdrücklichen Ausschluss, der Abzug ist aber auf die gesetzlichen Positionen beschränkt. Sachversicherungen gehören nicht zu den Versicherungsprämien in Ziff. 15, der Hausrat ist auch kein Vermögen (`beleg-hausrat-haftpflicht-police`). Im Zweifel entscheidet SB/ML.
> 
> ## Offene Punkte
> 
> 1. **Zivilstand, Kinder und Erwerbstätigkeit:** Daran hängen Kita-Abzug, Zweiverdienerabzug und die Limite in Ziff. 15.
> 2. **Pensionskasse:** Zahlt sie oder der Arbeitgeber in die 2. Säule (Lohnausweis Ziff. 10.1)? Das entscheidet über die 3a-Limite und die Stufe in Ziff. 15.
> 3. **Weitere Belege:** Fehlen Bank-Steuerauszug oder Kontoauszüge (Ziff. 4.1 und 30.1), ÖV-Abo oder Fahrkosten (Form. 360), Krankheitskosten und Schuldenbelege?

## q02

**Frage:** In welche Ziffer und mit welchem Code der ZH-Steuererklärung 2025 gehört der Nettolohn aus Lohnausweis Ziff. 11 (Person 1, Haupterwerb)?

**Soll (Referenz):** Ziff. 1.1 Haupterwerb, Code 100 (Person 1) / 101 (Person 2); Nettolohn Lohnausweis Ziff. 11 (zh-form-300-2025).

**Antwort des Agenten** (27.1 s · Tools: 5 Aufrufe read):

> **Ziffer 1.1, Code 100** (Einkünfte aus unselbständiger Erwerbstätigkeit, Haupterwerb, Person 1). Für Person 2 wäre es Code 101.
> 
> - **Betrag:** Der Nettolohn aus Lohnausweis Ziff. 11 kommt unverändert in Code 100. Hat Person 1 mehrere Haupterwerbe, ist es die Summe aller Ziff. 11.
> - **Kanton und Bund:** Es gibt nur eine Zeile. Staats- und Bundessteuer verwenden dieselbe Ziffer und denselben Code.
> - **Kontrolle:** Ziff. 11 muss Ziff. 8 − Ziff. 9 − Ziff. 10.1 − Ziff. 10.2 entsprechen.
> - **Erwerbslücken:** Sie sind ausdrücklich zu bezeichnen.
> - **PK-Einkauf aus Ziff. 10.2:** Er ist im Nettolohn schon abgezogen. In Ziff. 16.1 (Code 280) darf er nicht nochmals erscheinen.
> - **Nicht im Lohnausweis Ziff. 11 enthalten:** Spesen ohne entsprechende Ausgaben, Naturalbezüge und Mitarbeiterbeteiligungen gehören ebenfalls zum Lohn.
> - **Berufsauslagen:** Ziff. 11 dient auch als Basis für die 3 %-Pauschale für übrige Berufskosten im Form. 360 (Ziff. 11.1, Code 220).
> 
> **Fundstellen (Steuerjahr 2025):**
> - Formular 300 ZH 2025, S. 2 (Chunk `zh-form-300-2025__c0004`). Das Formular zeigt Ziff. 1.1 «Haupterwerb – Person 1 – Lohnausweis – 100» und «Person 2 – 101».
> - `quick/wegleitung-zh-2025.md` und `quick/zuordnung-zh-2025.md`, Zeile 1.1. Das Detail steht in `wiki/zh/zuordnung-zh-2025-detail.md#1-1-einkommen-unselbstaendig-haupterwerb`.
> 
> **Status:** ☑️ agent-geprüft, nicht von der Fachperson verifiziert. Ob Ziff. 11 weiter in der Wegleitung ZH 2025 steht, habe ich nicht im Wegleitungs-Chunk nachgeprüft. Ich habe nur das Formular-Chunk und die Zuordnungsseiten gelesen.

## q03

**Frage:** Lohnausweis Feld F ist angekreuzt (Geschäftsauto). Was bedeutet das für den Fahrkostenabzug (SG 2025)?

**Soll (Referenz):** Feld F angekreuzt → kein Fahrkostenabzug für den Arbeitsweg mit Geschäftsfahrzeug (Privatanteil im Lohn, Lohnausweis Ziff. 2.2).

**Antwort des Agenten** (44.2 s · Tools: 7 Aufrufe read, exec):

> Kurzer Zwischenstand: Ich habe die SG-Wegleitung 2025, StB 39 Nr. 3, Art. 18a StV und die Lohnausweis-Wegleitung geprüft. Jetzt folgt die Antwort.
> 
> ## Feld F angekreuzt: SG 2025
> 
> **Kurz: Kein Abzug für Fahrkosten Wohn–Arbeitsort.** Die Ziffern 1.1–1.3 in Formular 4 (ÖV, Velo, Motorfahrzeug) bleiben leer.
> 
> ### Begründung
> - **Wegleitung SG 2025, Ziff. 10.1, S. 23:** Wenn dem Arbeitnehmer keine Kosten erwachsen, muss auf dem Lohnausweis Feld F angekreuzt sein. «Ein Abzug für die Fahrt zur Arbeit ist deshalb nicht möglich.» Der Text nennt Sammeltransport und ein vom Arbeitgeber getragenes GA, das aus geschäftlichen Gründen benutzt wird. ^[sg-wl-2025__c0075]
> - **Lohnausweis-Wegleitung, Rz 9:** Feld F ist anzukreuzen, wenn dem Arbeitnehmer keine Arbeitswegkosten entstehen. Das Geschäftsfahrzeug wird dort ausdrücklich genannt, sofern der Arbeitnehmer nicht mindestens die Kilometerentschädigung oder die Selbstkosten zahlt. Dieser Chunk ist die Fassung **2026** (Steuerjahr 2026). Eine 2025er Fassung liegt im Wiki nicht vor. Die SG-WL 2025 stützt aber dieselbe Logik. ^[bund-wl-lohnausweis-2026__c0010]
> - **Art. 18a StV SG (2025/2026):** Für ein Geschäftsfahrzeug mit unentgeltlicher Privatnutzung gilt die Pauschale von 0,9 % des Kaufpreises pro Monat. Sie **ersetzt** den Fahrkostenabzug nach Art. 18 StV. ^[sg-stv__art-18a]
> 
> ### Praktisch für die Erklärung
> - **Kanton (Staats-/Gemeindesteuer):** Fahrkosten = 0. Der Maximalabzug von Fr. 8'000 ist irrelevant.
> - **Bund (DBG):** Der Wegleitungstext ist für die Kantonssteuer formuliert. Die Logik «keine Kosten, kein Abzug» gilt für beide Ebenen. Eine ausdrückliche SG-Fundstelle für den Bund habe ich nicht gefunden.
> - **Nicht betroffen:** Die übrigen Berufskosten bleiben abziehbar, also die Pauschale Fr. 700 + 10 % des Nettolohns (max. Fr. 2'400) bzw. effektiv. ^[Kompakt-Wegleitung SG 2025, Ziff. 10.1]
> - **Verpflegung:** Das ist ein eigener Prüfpunkt. Er hängt an Arbeitspause und Heimkehrmöglichkeit, nicht an Feld F. Bei Feld G (Kantine/Verbilligung) gilt der halbe Ansatz Fr. 7.50/Tag, max. Fr. 1'600, siehe Form. 4 Ziff. 2.2. ^[sg-form-4-2025__c0003]
> 
> ### Zu prüfen
> 1. **Ziff. 2.2 des Lohnausweises:** Steht dort der Privatanteil (0,9 %/Monat)? Dann ist alles stimmig, und der Arbeitsweg ist darin enthalten.
> 2. **Feld F und Ziff. 2.3:** Ist trotz angekreuztem Feld F eine Arbeitswegvergütung in Ziff. 2.3 ausgewiesen, widersprechen sich die Angaben. Die Regel besagt, dass bei vergüteten Arbeitswegkosten Feld F leer bleibt (StB 39 Nr. 3 Ziff. 4.1). Dann beim Arbeitgeber nachfragen. ^[sg-stb-39-3__c0013]
> 3. **Privatfahrzeug daneben:** Nutzt die Person zusätzlich ein eigenes Fahrzeug für den Arbeitsweg, ist das mit Geschäftsauto plus Feld F nicht vereinbar.
> 
> **Status:** Die Zuordnung ist ☑️ agent-geprüft (Kompakt-Wegleitung SG 2025, Ziff. 10.1). Die fachliche Beurteilung bleibt bei SB/ML.

## q04

**Frage:** Wie hoch ist der maximale Fahrkostenabzug 2025 in TG (Staatssteuer) und beim Bund, und welcher km-Ansatz gilt für das Auto?

**Soll (Referenz):** TG 2025 Staat max. CHF 6'000 (tg-stg__par-29), Bund max. CHF 3'300 (bund-dbg-2025__art-26); Auto TG gestaffelt 0.60/0.50/0.40 je nach Jahres-km, Bund 0.70.

**Antwort des Agenten** (32.8 s · Tools: 10 Aufrufe read):

> **Steuerjahr 2025, Kanton TG und Bund (Stand Wiki, Status je ☑️ agent-geprüft):**
> 
> | Ebene | Max. Fahrkostenabzug pro Person | Fundstelle |
> |---|---|---|
> | **TG Staats-/Gemeindesteuer** | **CHF 6'000** | § 29 Abs. 1 Ziff. 1 StG TG (`tg-stg__par-29`) |
> | **Direkte Bundessteuer** | **CHF 3'300** | Art. 26 Abs. 1 lit. a DBG, Fassung 2025 (`bund-dbg-2025__art-26`); ebenso RS 2-210 Ziff. 1.1 |
> 
> **km-Ansatz Auto (nur Privatauto, wenn ÖV nicht zumutbar oder nicht vorhanden):**
> 
> - **TG (Staat):** Der Ansatz ist gestaffelt und hängt von der jährlichen Kilometerleistung ab (§ 1 Abs. 1 Ziff. 3 BKV TG, `tg-bkv__par-1`):
>   - bis 3'000 km: CHF 0.60
>   - 3'001 bis 5'000 km: CHF 0.50
>   - über 5'000 km: CHF 0.40
>   - Die Staffel ist laut dem Wiki kumulativ, wie im Berechnungsbeispiel in StP 29 Nr. 2: 8'000 km ergeben Fr. 4'000.
> - **Bund:** Einheitlich CHF 0.70 pro km (Anhang Ziff. 2 BKV 2025, `bund-bkv-2025__anhang-1`).
> 
> Bei TG müssen Staat und Bund also getrennt gerechnet werden. Im Formular 4.2 gibt es dafür zwei Spalten. Den Bundesansatz von CHF 0.70 darf man nicht auf die Staatssteuer übertragen.
> 
> **Hinweise:**
> - ⚠️ **Widerspruch beim Bund-Maximum:** Die ESTV-Wegleitung 2a 2025 (S. 6, `bund-wl-2a-2025__c0042`) nennt noch «maximal 3200 Franken». Das Gesetz für 2025 und RS 2-210 nennen 3'300. Nach der Quellenhierarchie (Gesetz vor Wegleitung) gilt 3'300. Ich würde das Original-PDF prüfen und die Fachperson entscheiden lassen.
> - **Ab 2026** gilt beim Bund CHF 0.75 pro km. Für 2025 ist dieser Wert nicht anwendbar.
> - **Auto nur ausnahmsweise:** Normalfall ist das ÖV-Abo mit den tatsächlichen Kosten. Das Privatauto ist nur zulässig, wenn der ÖV fehlt oder unzumutbar ist. Der Abzug entfällt, wenn im Lohnausweis Feld F angekreuzt ist (unentgeltliche Beförderung, z.B. Geschäftsfahrzeug).
> - **Bei Auto-km:** Das Wiki nennt 225 Arbeitstage (TG, WL 2025 S. 4).
> 
> Quellen: `steuerwiki/quick/werte-tg-2025.md`, `steuerwiki/quick/werte-bund-2025.md`, `steuerwiki/wiki/themen/fahrkosten.md`. Die Chunk-Texte habe ich direkt geprüft. Die fachliche Beurteilung bleibt bei SB/ML.

## q05

**Frage:** Welcher km-Ansatz für Autos gilt 2026 bei der direkten Bundessteuer?

**Soll (Referenz):** CHF 0.75 pro km (bund-mm-2025-09-11-kalte-progression-2026__c0004; RS 2-215).

**Antwort des Agenten** (33.3 s · Tools: 6 Aufrufe read, memory_search):

> **Für die direkte Bundessteuer gelten im Steuerjahr 2026 CHF 0.75 pro km für das Privatauto.** Im Vorjahr 2025 waren es CHF 0.70.
> 
> Der Ansatz gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist. Der Fahrkostenabzug bleibt auf CHF 3'300 pro Person und Jahr begrenzt (Art. 26 Abs. 1 lit. a DBG).
> 
> | Position Bund 2026 | Wert | Vorjahr 2025 |
> |---|---|---|
> | Auto, pro km | **CHF 0.75** | 0.70 |
> | Motorrad (weisses Kontrollschild), pro km | CHF 0.40 | 0.40 |
> | Velo / Motorfahrrad (Pauschale) | CHF 700 | 700 |
> | Maximalabzug Fahrkosten | CHF 3'300 | 3'300 |
> 
> **Fundstellen:**
> - Das ESTV-Rundschreiben RS 2-215 (S. 1, Abzugstabelle 2025/2026) nennt «Fahrkosten für Automobile pro Kilometer: 0.70 (2025) / 0.75 (2026)». Quelle: `bund-rs-2-215__c0004`.
> - Die ESTV-Mitteilung vom 11.09.2025 begründet die Erhöhung. Der Autoabzug richtet sich erstmals nach dem jährlich publizierten TCS-Kilometerpreis für das Musterauto. Er kann künftig auch sinken. Quelle: `bund-mm-2025-09-11-kalte-progression-2026__c0004`.
> - Rechtsgrundlage laut Wiki: Art. 5 Abs. 2 lit. b BKV, Anhang Ziff. 2. Diesen Artikel habe ich nicht selbst im Chunk geprüft.
> - Wiki-Status: ☑️ agent-geprüft, nicht von der Fachperson verifiziert. Die Seite [Eckwerte Bund 2026](steuerwiki/quick/werte-bund-2026.md) führt den Wert unter `berufskosten.fahrkosten.auto_km`.
> 
> **Kanton separat:**
> - Die kantonalen Ansätze sind nicht automatisch identisch mit dem Bundesansatz.
> - AR (Wiki: Kanton ebenfalls 0.75; Fundstelle nur über die Zuordnungsseite AR 2026 gesehen), SG (Wiki: 0.75 ab 2026, bisher 0.70) und ZH (Wegleitung ZH 2026 UJ: Auto 0.75/km) weisen für 2026 ebenfalls 0.75 aus.
> - Den TG-Ansatz habe ich nicht geprüft. Den genauen Wortlaut je Kanton müsste ich bei Bedarf in der jeweiligen Wegleitung nachschlagen.

## q06

**Frage:** Maximaler Säule-3a-Abzug 2025 für eine Arbeitnehmerin mit Pensionskasse? Und für eine Selbständige ohne 2. Säule?

**Soll (Referenz):** Mit 2. Säule CHF 7'258; ohne 2. Säule 20 % des Erwerbseinkommens, max. CHF 36'288 (bund-bsv-masszahlen-2025-2026__c0003).

**Antwort des Agenten** (33.0 s · Tools: 4 Aufrufe read, memory_search, exec):

> **Steuerjahr 2025, Säule 3a.** Die Limiten sind bundesrechtlich geregelt (BVV 3). Sie gelten für Staats-/Gemeindesteuer und direkte Bundessteuer gleich. In den Wegleitungen AR, SG, TG und ZH 2025 stehen dieselben Beträge. Den Kanton brauche ich nur für die Ziffer und den Code im Formular.
> 
> | Fall | Maximalabzug 2025 | Fundstelle |
> |---|---|---|
> | **Arbeitnehmerin mit Pensionskasse** (2. Säule) | **CHF 7'258** | BVV 3 Art. 7 Abs. 1 lit. a (8 % des oberen BVG-Grenzbetrags). BSV-Masszahlen 2025/26 S. 1 (`bund-bsv-masszahlen-2025-2026__c0003`). WL 2a 2025 S. 7 (`bund-wl-2a-2025__c0048`). |
> | **Selbständige ohne 2. Säule** | **20 % des Erwerbseinkommens, höchstens CHF 36'288** | BVV 3 Art. 7 Abs. 1 lit. b (`bund-bvv3__art-7`). BSV-Masszahlen 2025/26 S. 1 (`bund-bsv-masszahlen-2025-2026__c0003`). WL 2a 2025 S. 7 (`bund-wl-2a-2025__c0048`). |
> 
> Status im Wiki: ☑️ agent-geprüft. Die Fachperson hat die Werte noch nicht als ✅ verifiziert.
> 
> **Rechenregel, je Person:**
> - Mit 2. Säule gilt min(Einzahlung; 7'258).
> - Ohne 2. Säule gilt min(Einzahlung; 20 % × Erwerbseinkommen; 36'288).
> - Der Höchstbetrag von CHF 36'288 wird bei einem Erwerbseinkommen ab CHF 181'440 erreicht (36'288 ÷ 0.2, eigene Rechnung).
> 
> **Beachten:**
> - Abziehbar sind nur Beiträge, die 2025 tatsächlich einbezahlt wurden. Die Bescheinigung der Vorsorgeeinrichtung muss beiliegen.
> - Die Beträge sind zugleich die absoluten Einzahlungslimiten. Eine Überzahlung ist vom Vorsorgeträger zurückzahlen zu lassen (so in der WL TG 2026 festgehalten; für 2025 nicht separat geprüft).
> - Als Erwerbseinkommen zählen alle Einkünfte aus selbständiger und unselbständiger, haupt- und nebenberuflicher Erwerbstätigkeit. Bei Selbständigen sind die 3a-Beiträge Privataufwand und gehören nicht in die Erfolgsrechnung (WL SG 2025).
> - Der nachträgliche Einkauf in die Säule 3a nach BVV 3 Art. 7a/7b gilt seit 01.01.2025. Er betrifft nur Lücken ab Beitragsjahr 2025 und ist damit praktisch erst ab 2026 nutzbar (Seed-Angabe, nicht aus der Quelle bestätigt). Im Maximum 2025 ist er nicht enthalten.
> 
> Die Beurteilung im Einzelfall bleibt bei der Fachperson. Wenn du mir den Kanton nennst, gebe ich dir die Ziffer und den Code im Formular.

## q07

**Frage:** Kinderabzug 2025 in AR für ein 10-jähriges Kind – und beim Bund?

**Soll (Referenz):** AR 2025: CHF 7'400 (4.–15. Altersjahr; Anhang 1 StG, ar-stg-anhang-kp__c0001); Bund CHF 6'800 (Art. 35 DBG) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (35.5 s · Tools: 8 Aufrufe read):

> **Steuerjahr 2025, Kind 10 Jahre alt.** Massgebend ist das Alter am 31.12.2025. Ich gehe davon aus, dass der Wohnsitz am 31.12. in AR liegt und das Kind keine eigenen Einkünfte hat.
> 
> | | Betrag | Fundstelle | Status |
> |---|---|---|---|
> | **AR (Staats-/Gemeindesteuer)** | **CHF 7'400** (Schulalter, nach dem 4. bis zum 15. Altersjahr), Ziff. 23.2 | StG AR Art. 38 Abs. 1 lit. a Ziff. 2, indexiert in Anhang 1 (`ar-stg-anhang-kp__c0001`); WL AR 2025 S. 2 | ☑️ |
> | **Bund (DBG)** | **CHF 6'800** vom Einkommen, einheitlich für alle Altersstufen | Art. 35 Abs. 1 lit. a DBG (`bund-dbg-2025__art-35`) | ☑️ |
> | **Bund, zusätzlich** | **CHF 263** direkt vom Steuerbetrag, wenn die Person mit dem Kind im gleichen Haushalt lebt und dessen Unterhalt zur Hauptsache bestreitet | Art. 36 Abs. 2bis DBG (`bund-dbg-2025__art-36-t4`) | ☑️ |
> 
> **Zum Ausfüllen in AR**
> - Das AR-Formular hat keine eigene Bundesspalte. Den Bundesabzug nimmt die Steuerverwaltung automatisch vor (WL AR 2025 S. 33, `ar-wl-2025__c0179`). Du trägst nur Ziff. 23.2 ein.
> - Der Gesetzestext nennt noch CHF 7'000. Massgebend sind CHF 7'400 aus Anhang 1 per 1.1.2024, bestätigt durch die WL 2025.
> 
> **Bedingungen und Stolpersteine**
> - Kein Kinderabzug, wenn für das Kind Unterhaltsbeiträge nach Ziff. 12.2 abgezogen werden. Das gilt für Kanton und Bund.
> - AR: Kein Abzug, wenn die Einkünfte des Kindes über CHF 18'000 liegen. Diese Grenze ist bei Ziff. 23.1 und 23.2 belegt. Die Vermögensgrenze von CHF 250'000 steht nur bei Ziff. 23.3 (Kind ab dem 15. Altersjahr).
> - Getrennt besteuerte Eltern mit gemeinsamer Sorge und ohne Alimente: je die Hälfte.
> 
> **Weitere kindbezogene Positionen (nicht der Kinderabzug)**
> 
> | | AR | Bund |
> |---|---|---|
> | Versicherungsabzug, Zuschlag pro Kind | CHF 1'000 | CHF 700 |
> | Vermögens-Sozialabzug pro Kind | CHF 25'000 | n/a (Bund erhebt keine Vermögenssteuer) |
> | Drittbetreuungskosten, Maximum pro Kind (bis 14 Jahre) | CHF 25'000 | CHF 25'800 |
> 
> Für diese Positionen ist nur die Quelle des Kinderabzugs gelesen. Die Detailregeln habe ich nicht geprüft.
> 
> Die Werte sind agent-geprüft (☑️), nicht von der Fachperson verifiziert. Die fachliche Beurteilung bleibt bei SB/ML.

## q08

**Frage:** Versicherungsabzug ZH 2025 für ein Ehepaar mit 2 Kindern, beide mit Pensionskasse (Staatssteuer und Bund)?

**Soll (Referenz):** ZH Staat: 5'800 + 2 × 1'300 = 8'400; Bund: 3'700 + 2 × 700 = 5'100 (zh-stg-2025__par-31-t2, bund-dbg-2025__art-33).

**Antwort des Agenten** (32.9 s · Tools: 7 Aufrufe read):

> **Versicherungsabzug ZH, Steuerjahr 2025 – Ehepaar, 2 Kinder mit Kinderabzug, beide mit Pensionskasse**
> 
> | | Staats-/Gemeindesteuer | Direkte Bundessteuer |
> |---|---|---|
> | Grundbetrag Ehepaar (mit Beiträgen an 2. Säule/3a) | CHF 5'800 | CHF 3'700 |
> | Zuschlag je Kind (2 × CHF 1'300 bzw. 2 × CHF 700) | CHF 2'600 | CHF 1'400 |
> | **Maximalabzug** | **CHF 8'400** | **CHF 5'100** |
> 
> Die Zuschläge sind meine Rechnung aus den Tabellenwerten. Sie steht nicht als Beispiel in der Wegleitung.
> 
> **So wirkt der Maximalabzug**
> - Abgezogen wird der niedrigere Betrag aus den bezahlten Prämien und Sparzinsen (A) und dem Maximalabzug (B). Das läuft über Form. 365 Teil C und geht in Ziff. 15 (Code 270) des Formulars 300. Staat und Bund haben je eine eigene Spalte.
> - Zu A gehören Krankenkasse, Unfall (ohne die im Lohnausweis abgezogene NBUV), Lebens- und Rentenversicherung sowie Sparzinsen aus dem Wertschriftenverzeichnis.
> - Die Prämienverbilligung muss abgezogen werden. Sie ist meist schon in der Krankenkassenbescheinigung verrechnet; dann nicht nochmals abziehen.
> - Mobiliar-, Haftpflicht- und Motorfahrzeugversicherungen gehören nicht in A.
> 
> **Zu beachten**
> - Der Zuschlag von CHF 1'300 bzw. CHF 700 gilt nur für Kinder, für die ein Kinderabzug nach § 34 StG geltend gemacht werden kann. Bei hälftigem Kinderabzug halbiert er sich auf CHF 650 bzw. CHF 350.
> - Die erhöhten Beträge ohne Vorsorge (Staat CHF 8'700, Bund CHF 5'550, jeweils ohne Kinderzuschlag) gelten nur, wenn weder Beiträge an die 2. noch an die 3. Säule geleistet wurden. Hier zahlen beide in die Pensionskasse ein, also gilt der Grundbetrag.
> - Ob die Pensionskasse oder der Arbeitgeber Beiträge leistet, beantwortet sich über Seite 1 des Formulars und Lohnausweis Ziff. 10.1.
> 
> **Fundstellen (Steuerjahr 2025)**
> - Staat und Bund: [Formular 365 ZH 2025, Teil B](steuerwiki/chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md), Codes 611 und 613, Formularwerte wörtlich geprüft.
> - Staat: [§ 31 Abs. 1 lit. g StG ZH](steuerwiki/chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t2.md) (Gesetzestext: CHF 5'800 und Zuschlag CHF 1'300).
> - Bund: Art. 33 DBG, [bund-dbg-2025__art-33-t2](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t2.md) und [t5](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t5.md). Die Bundeswerte habe ich nur über die Wiki-Seite und das Formular 365 bestätigt, nicht im DBG-Chunk selbst.
> - Wegleitung: [WL ZH 2025 S. 15](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0086.md).
> - Status: ☑️ agent-geprüft, nicht ✅ von der Fachperson verifiziert. Die fachliche Beurteilung bleibt bei SB/ML.

## q09

**Frage:** Wie hoch ist der Kinderdrittbetreuungsabzug 2025 im Kanton ZH, und gilt 2026 ein anderer Wert?

**Soll (Referenz):** ZH 2025 CHF 25'000 (StG Nachtrag 127, zh-stg-2025__par-31-t4); 2026 CHF 25'300 (zh-stg-2026__par-31-t3). Die VKP ab 2024 (10'400) ist überholt.

**Antwort des Agenten** (36.4 s · Tools: 6 Aufrufe read, exec):

> **Kanton ZH, Kinderdrittbetreuungsabzug (Ziff. 16.6, Code 376), pro Kind:**
> 
> | | 2025 | 2026 |
> |---|---|---|
> | **Staats-/Gemeindesteuer (ZH)** | **CHF 25'000** | **CHF 25'300** |
> | Direkte Bundessteuer (zur Abgrenzung) | CHF 25'800 | CHF 25'800 |
> 
> **Ja, 2026 gilt für die Staatssteuer ein anderer Wert: CHF 25'300 statt CHF 25'000.** Beim Bund bleibt es bei CHF 25'800.
> 
> **Voraussetzungen (2025 und 2026 gleich):**
> - Das Kind hat das 14. Altersjahr noch nicht vollendet.
> - Es lebt im gleichen Haushalt wie die Person, die für seinen Unterhalt sorgt.
> - Die Kosten stehen in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.
> - Abziehbar sind nur die nachgewiesenen Kosten, höchstens der Maximalbetrag.
> 
> **Sonderfall Konkubinat oder alternierende Obhut mit gemeinsamer Sorge:** Jeder Elternteil erhält den halben Abzug.
> - 2025: höchstens CHF 12'500 Staat / CHF 12'900 Bund.
> - 2026: höchstens CHF 12'650 Staat / CHF 12'900 Bund.
> - Diese Halbbeträge stehen nicht in den beiden Gesetzesabschnitten, die ich im Original geprüft habe. Sie stammen aus der Themenseite des Wikis, die sich auf die Wegleitung beruft (WL 2025 `c0109`, WL 2026 UJ `c0107`). Ich habe sie nicht im Wegleitungs-Chunk nachgelesen.
> 
> **Fundstellen** (Status ☑️ agent-geprüft, nicht von der Fachperson verifiziert):
> - 2025: § 31 Abs. 1 lit. j StG ZH, Chunk `zh-stg-2025__par-31-t4`: «höchstens Fr. 25 000». Bestätigt durch WL ZH 2025, Ziff. 16.6 (`zh-wl-2025__c0106`).
> - 2026: § 31 Abs. 1 lit. j StG ZH, Chunk `zh-stg-2026__par-31-t3`: «höchstens Fr. 25 300». Bestätigt durch WL ZH 2026 UJ, Ziff. 16.6 (`zh-wl-2026-uj__c0105`).
> 
> **Zwei Stolpersteine:**
> - **Alter Wert Fr. 10'400:** Die Verordnung ab 2024 (VKP) nennt noch diesen Betrag. Er ist durch das Gesetz überholt. Für 2025 gilt der Wert im StG (Fassung Nachtrag 127), für 2026 der im StG (Fassung Nachtrag 132).
> - **Stand der Wegleitung 2026:** Die reguläre Wegleitung und das reguläre Formular ZH 2026 sind im Wiki noch nicht abgelegt (Stand 09.11.2026). Die Bestätigung stützt sich auf die Fassung für unterjährige Steuerpflicht (UJ). Für die Ziffer und den Code 376 ist am regulären Formular 2026 gegenzuprüfen.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## q10

**Frage:** Gibt es im Kanton TG einen Zweiverdienerabzug für die Staatssteuer?

**Soll (Referenz):** Nein, TG kennt keinen kantonalen Zweiverdienerabzug (nur Bund: 50 %, 8'600–14'100).

**Antwort des Agenten** (37.0 s · Tools: 5 Aufrufe read, exec):

> Ich prüfe noch die Belegstellen im Original-Chunk.
> 
> **Nein.** Im Kanton Thurgau gibt es für die Staats- und Gemeindesteuer keinen Zweiverdienerabzug. Das gilt für die Steuerjahre 2025 und 2026. Den Abzug gibt es nur bei der direkten Bundessteuer.
> 
> **Staats- und Gemeindesteuer TG (2025 und 2026)**
> - Die Steuerpraxis TG hält fest: «Im Gesetz über die Staats- und Gemeindesteuern des Kantons Thurgau ist kein Zweiverdienerabzug vorgesehen.» (StP 34 Nr. 25, Ziff. 1, `tg-stp-34-25__c0001`)
> - Die Wegleitung bestätigt das für beide Jahre: «Bei den Staats- und Gemeindesteuern besteht keinen solcher Abzug.» (WL TG 2025 S. 23, `tg-wl-2025__c0104`; WL TG 2026 S. 23, `tg-wl-2026__c0103`)
> 
> **Direkte Bundessteuer (Art. 33 Abs. 2 DBG)**
> - Der Abzug beträgt 50 % des niedrigeren Erwerbseinkommens der beiden gemeinsam besteuerten Personen.
> - Er beträgt mindestens CHF 8'600 und höchstens CHF 14'100. Diese Beträge gelten für 2025 und 2026 gleich.
> - Liegt das niedrigere Erwerbseinkommen unter CHF 8'600, ist nur dieser Teilbetrag abziehbar.
> - Als Erwerbseinkommen gilt die Einkunft aus unselbständiger oder selbständiger Tätigkeit nach Abzug der Berufsauslagen, der Beiträge an die 2. Säule und der Säule 3a.
> - Voraussetzung ist eine rechtlich und tatsächlich ungetrennte Ehe oder eingetragene Partnerschaft, bei der beide ein Erwerbseinkommen erzielen. (WL TG 2025/2026 S. 23; StP 34 Nr. 25)
> 
> **Im Formular**
> - Der Abzug steht in Ziff. 18 (Code 356) und nur in der Bundesspalte. In der Kantonsspalte bleibt die Zeile leer.
> - Die Wegleitung nennt als typischen Fehler, den Abzug im Kantonsteil anzusetzen.
> - Taggelder und andere Erwerbsersatzeinkünfte zählen beim Bund als Erwerbseinkommen. Im vereinfachten Verfahren versteuerte Löhne zählen nicht. (StP 34 Nr. 27; WL TG 2025 S. 23)
> 
> **Status:** ☑️ agent-geprüft. Ich habe die Chunks `tg-stp-34-25__c0001`, `tg-wl-2025__c0104` und `tg-wl-2026__c0103` im Wortlaut gelesen. Das Original-PDF habe ich nicht eingesehen. Die fachliche Beurteilung bleibt bei SB/ML.
> 
> **Ausblick:** Der Bundesrat hat die Individualbesteuerung auf den 1. Januar 2032 festgelegt. Der Zweiverdienerabzug in dieser Form dürfte dann entfallen. Details dazu sind im Wiki nicht erfasst.
> 
> Weitere Hinweise: [Thema Zweiverdienerabzug](steuerwiki/wiki/themen/zweiverdienerabzug.md), [Wegleitung TG 2025](steuerwiki/quick/wegleitung-tg-2025.md), [Wegleitung TG 2026](steuerwiki/quick/wegleitung-tg-2026.md).

## q11

**Frage:** SG 2025: Pauschale für übrige Berufskosten? Wie wird sie berechnet?

**Soll (Referenz):** SG 2025: CHF 700 + 10 % des Nettolohns, max. CHF 2'400 (Art. 21 StV SG, WL SG 2025).

**Antwort des Agenten** (42.2 s · Tools: 5 Aufrufe read, exec):

> **SG, Steuerjahr 2025: Pauschale für übrige Berufskosten (Formular 4, Ziff. 3.1; Code 416 für Person 1, 466 für Person 2)**
> 
> **Staats- und Gemeindesteuer**
> - **Formel:** Fr. 700 + 10 % des Nettolohns, höchstens Fr. 2'400. Es gibt kein Minimum. ^[sg-stv__art-21] ^[sg-wl-2025__c0080]
> - **Nettolohn:** Gemeint sind die Nettoeinkünfte (Art. 21 Abs. 2 StV SG). Das sind die Bruttoeinkünfte abzüglich der Beiträge nach Art. 45 Abs. 1 lit. d und f StG, ohne Einkäufe in die 2. Säule. Als Basis dient der Nettolohn gemäss Lohnausweis (Ziff. 1.1 der Steuererklärung bzw. Lohnausweis Ziff. 11).
> - **Berechnung:** `min(700 + 10 % × Nettolohn; 2'400)`. Das Maximum ist ab einem Nettolohn von Fr. 17'000 erreicht (rechnerisch: (2'400 − 700) / 10 %).
> - **Effektive Kosten:** Wer höhere Kosten nachweist, kann sie anstelle der Pauschale abziehen (Ziff. 3.2; Code 418 bzw. 468). Die Kosten gehören auf ein Beiblatt zu Formular 4. Die Pauschale entfällt dann vollständig. Ein Arbeitszimmer muss dann ebenfalls effektiv belegt werden. ^[sg-stv__art-21 Abs. 3]
> - **Pauschalspesen:** Bei ausbezahlten nicht ereignisbezogenen Pauschalspesen kann die Pauschale nicht zusätzlich geltend gemacht werden. ^[sg-wl-2025__c0080]
> - **Arbeitslosentaggelder:** Die Pauschale ist bei ALV-Taggeldern sinngemäss abziehbar. ^[sg-wl-2025__c0080]
> - **Arbeitszimmer:** Es ist mit der Pauschale abgegolten, eine Kumulation ist nicht möglich. Der Quick-Layer stützt sich dafür auf StB 39 Nr. 1. Dieses Steuerbuch-Kapitel habe ich nicht im Original geöffnet.
> - **Unterjährige Steuerpflicht:** Jahrespauschalen werden nach der Dauer umgerechnet. Das gilt laut Quick-Layer für Ziff. 3 und 5 des Formulars 4.
> 
> **Direkte Bundessteuer (im SG-Formular automatisch durch das Steueramt umgesetzt)**
> - Der Bund rechnet anders: 3 % des Nettolohns, mindestens Fr. 2'000 und höchstens Fr. 4'000. Das steht im Anhang BKV (`bund-bkv-2025__anhang-1`).
> - Berechnung: `min(max(3 % × Nettolohn; 2'000); 4'000)`.
> 
> **Rechenbeispiel (Kanton):** Bei einem Nettolohn von Fr. 60'000 ergeben 700 + 6'000 = 6'700 Franken. Gedeckelt sind das Fr. 2'400. Bei Fr. 10'000 sind es 700 + 1'000 = Fr. 1'700. Beide Beträge habe ich selbst nach der Formel gerechnet. Sie stehen nicht so im Wiki.
> 
> **Status:** ☑️ agent-geprüft. Die Werte stützen sich auf Art. 21 StV SG und die WL SG 2025 S. 24. Die fachliche Beurteilung bleibt bei SB/ML.
> 
> Quellen:
> - `steuerwiki/chunks/sg/2025/sg-stv/sg-stv__art-21.md`
> - `steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0080.md`
> - `steuerwiki/quick/wegleitung-sg-2025.md` (Form. 4 Ziff. 3.1/3.2)
> - `steuerwiki/quick/werte-sg-2025.md`
> - `steuerwiki/quick/werte-bund-2025.md`

## q12

**Frage:** Pauschalabzug Liegenschaftsunterhalt in AR für ein 8-jähriges Einfamilienhaus – und wie in ZH?

**Soll (Referenz):** AR: 10 % (Gebäude bis 10 Jahre) bzw. 20 % des Bruttoertrags, nur bis Bruttomietertrag 100'000 (Art. 25 StV AR, MB 03); ZH: einheitlich 20 % ohne Altersstaffel (ZStB 30.2).

**Antwort des Agenten** (44.7 s · Tools: 5 Aufrufe read, exec):

> Bei einem 8-jährigen Einfamilienhaus gilt in AR 10 % und in ZH 20 %. Die Steuerjahre 2025 und 2026 sind in beiden Kantonen identisch. Alle Angaben haben den Status ☑️ agent-geprüft und sind noch nicht von einer Fachperson verifiziert.
> 
> ## Pauschalabzug
> 
> Basis ist der Eigenmietwert (bzw. Brutto-Mietertrag).
> 
> | | Satz bei 8 Jahren | Bedingungen | Fundstelle |
> |---|---|---|---|
> | **AR** (Staats-/Gemeindesteuer) | **10 %** (20 % erst bei Gebäuden über 10 Jahren) | Der jährliche Bruttomietertrag des gesamten Liegenschaftsbesitzes darf höchstens CHF 100'000 betragen. Bei Eigennutzung gilt der Eigenmietwert. Das Alter bestimmt sich nach dem Stichtag der Vermögenssteuer. | Art. 25 StV AR: `ar-stv__art-25`, `ar-mb-03__c0004` |
> | **ZH** (Staats-/Gemeindesteuer) | **20 %**, einheitlich ohne Altersstaffelung | Das Haus darf nicht ganz oder vorwiegend geschäftlich genutzt sein. | § 30 Abs. 5 StG, ZStB 30.2 Ziff. II–IV: `zh-zstb-30-2__c0002` |
> | **Bund** (DBG, in beiden Kantonen) | **10 %** (Alter zu Beginn der Steuerperiode, bis 10 Jahre) | Das Haus darf nicht von Dritten vorwiegend geschäftlich genutzt werden. | Art. 5 Abs. 2 LKV: `bund-lkv__art-5` |
> 
> ## Was das für die Praxis heisst
> 
> - **ZH:** Kanton und Bund haben verschiedene Sätze, nämlich 20 % beim Kanton und 10 % beim Bund. Beide Ebenen sind getrennt zu rechnen. Das Wiki hält ausdrücklich fest, dass beim Bund 10 %/20 % auch dann gelten, wenn der Kanton einheitlich 20 % gewährt (WL ZH 2026 UJ, `zh-wl-2026-uj__c0192`).
> - **AR:** Das AR-Formular hat keine separate Bundesspalte. Die Pauschale gilt dort auf beiden Ebenen mit 10 %.
> - **Wahlrecht:** In beiden Kantonen kann man je Liegenschaft und Steuerperiode zwischen Pauschale und effektiven Kosten wählen (AR zusätzlich je Gebäude). Bei der Pauschale kommen keine weiteren Abzüge dazu. In ZH sind nur Baurechtszinsen zusätzlich abziehbar.
> - **Energiesparinvestitionen:** Sie sind nur bei effektiven Kosten separat abziehbar. In ZH sind sie von der Pauschale mit abgegolten (ZStB 30.2 Ziff. II).
> - **Formular:** In AR gehört der Abzug auf Ziff. 15 / Form. 7 Abschn. C1 (Pauschale). In ZH steht er im Liegenschaftenverzeichnis, bei der Pauschale als Code 5731 ff. auf Form. 350 (2025).
> 
> ## Offene Punkte
> 
> - **Steuerjahr:** Sie haben keines genannt. Für 2025 sind die Werte aus der Wegleitung belegt.
> - **AR 2026:** Das AR-Formular und die Wegleitung 2026 sind noch nicht publiziert. Der Satz stützt sich auf Art. 25 StV AR, dessen Quelle für 2025 und 2026 gilt.
> - **Eigenmietwert-Reform:** Die Abschaffung ist auf den 1.1.2029 angesetzt. Für 2025 und 2026 gilt das bisherige Recht.
> 
> Ob effektive Kosten über der Pauschale liegen, hängt von den Rechnungen ab. Die Entscheidung bleibt bei der Fachperson.

## q13

**Frage:** TG: Welcher Einschlag gilt auf dem Eigenmietwert der selbstbewohnten Liegenschaft am Wohnsitz (Kanton vs. Bund)?

**Soll (Referenz):** TG: Abzug 40 % Kanton, 20 % Bund für dauernd selbstbewohntes Eigentum am Wohnsitz (tg-stg__par-23; WL TG 2025).

**Antwort des Agenten** (51.1 s · Tools: 9 Aufrufe read, exec, memory_search):

> Für Thurgau gilt beim Selbstnutzungsabzug (dem «Einschlag») auf dem Eigenmietwert:
> 
> | Ebene | Abzug auf dem Mietwert | Steuerjahr |
> |---|---|---|
> | Staats- und Gemeindesteuer TG | **40 %** | 2025 und 2026 |
> | Direkte Bundessteuer | **20 %** | 2025 und 2026 |
> 
> Die Wegleitung 2025 und 2026 nennt für beide Jahre dieselben Sätze. Du hast kein Steuerjahr genannt, deshalb habe ich beide geprüft.
> 
> **Voraussetzung:** Die Liegenschaft muss am Wohnsitz selbstgenutzt sein. Der Abzug gilt nicht für landwirtschaftlich geschätzte Liegenschaften, Zweit- und Ferienwohnungen und unentgeltlich oder unterpreislich an Nahestehende überlassene Objekte. Diese Mietwerte sind zu 100 % steuerbar.
> 
> **Ausfüllen:** Formular 7 führt Staats- und Bundessteuer in getrennten Spalten. Der Nettoerfolg kommt in Ziff. 8.1 (Code 180).
> 
> **Fundstellen:**
> - Kanton: § 23 Abs. 3 StG TG. Der Mietwert wird nach Abs. 2 «aufgrund der ortsüblichen Verhältnisse und tatsächlichen Nutzung» festgelegt, davon werden 40 % abgezogen. (`tg-stg__par-23`)
> - Kanton und Bund: StP 23 Nr. 1, Ziff. 3.4: «40% bei den Staats- und Gemeindesteuern … Bei der direkten Bundessteuer beträgt der Abzug hingegen nur 20%». (`tg-stp-23-1__c0005`)
> - WL TG 2025, S. 47: «kantonal einen Abzug von 40% und beim Bund von 20%». (`tg-wl-2025__c0225`)
> - WL TG 2026, S. 47: gleicher Wortlaut. (`tg-wl-2026__c0222`)
> 
> **Status:** Gesetz, Praxis und Wegleitung habe ich im Wortlaut gelesen. Der Datenwert `liegenschaft.eigenmietwert_abzug` ist laut Themenseite agent-geprüft (☑️), nicht von einer Fachperson verifiziert (✅). Ich habe den Status des Einzeleintrags nicht separat geöffnet.
> 
> **Ausblick:** Der Eigenmietwert soll per 1.1.2029 entfallen (Medienmitteilung Bundesrat vom 01.04.2026). Für 2025 und 2026 ändert das nichts.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## q14

**Frage:** Bis wann kann ein Treuhänder im Kanton TG für seine Mandanten Fristerstreckung erhalten?

**Soll (Referenz):** Gewerbsmässige Treuhänder für Mandanten bis 31.12. des Deklarationsjahres (StP 155 Nr. 2).

**Antwort des Agenten** (48.5 s · Tools: 9 Aufrufe read, read, memory_search):

> **Antwort:** Im Kanton Thurgau kann ein gewerbsmässig tätiger Treuhänder oder Steuerberater für seine Mandanten **längstens bis zum 31. Dezember des Deklarationsjahres** Fristerstreckung beantragen. Das gilt für die kantonale Steuererklärung, die auch die direkte Bundessteuer abdeckt (Staats-/Gemeindesteuer und Bund laufen über dieselbe Erklärung).
> 
> **Fundstelle:** Thurgauer Steuerpraxis StP 155 Nr. 2 («Fristerstreckung zur Einreichung der Steuererklärung»), [`tg-stp-155-2__c0002`](steuerwiki/chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0002.md). Der Chunk ist für die Steuerjahre 2025, 2026 und 2027 ausgewiesen. Status im Wiki: ☑️ agent-geprüft.
> 
> **Heute (09.11.2026):** Für das Steuerjahr 2025 ist das Deklarationsjahr 2026, die Frist also der **31. Dezember 2026**. Das ist rund sieben Wochen entfernt. Die Zuordnung «Deklarationsjahr = Einreichejahr» ist eine Auslegung des Wikis aus der Wortwahl der Praxis (⚠ prüfen).
> 
> **Zum Vergleich: Private ohne Vertreter** (StP 155 Nr. 2, [c0001](steuerwiki/chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md))
> - Das erste Gesuch wird grundsätzlich bewilligt, längstens bis 30. September.
> - Weitere Gesuche werden in begründeten Fällen bis 30. November gewährt.
> 
> **Weitere Punkte**
> - **Nach dem 31.12.:** Weitere Gesuche werden abgewiesen, ausser es werden ausserordentliche Gründe glaubhaft gemacht. Dafür braucht es in der Regel eine substanziierte Sachdarstellung. Starke berufliche Inanspruchnahme des Vertreters oder fehlende Unterlagen genügen nicht (c0002).
> - **Arbeitsüberlastung:** Sie ist kein Grund für eine Fristverlängerung (c0001).
> - **Zeitpunkt und Form:** Das Gesuch muss schriftlich, begründet und rechtzeitig (also vor Ablauf der Frist) beim Gemeindesteueramt eingehen ([WL TG 2026 S. 7–8](steuerwiki/chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0022.md)). Abgelaufene Fristen lassen sich nicht mehr erstrecken.
> - **Entscheid:** Er ergeht schriftlich an den Vertreter, wenn dieser das Gesuch gestellt hat. Eine verweigerte Fristverlängerung ist ein Zwischenentscheid und nicht selbständig anfechtbar (StP 155 Nr. 2, c0005, laut Wiki-Überblick `tg-ueberblick.md`).
> - **Vollmacht:** Eine schriftliche Vollmacht ist nötig (§ 151 StG TG; [WL TG 2025 S. 5](steuerwiki/chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0012.md)). Die Unterschrift auf der Steuererklärung bleibt trotz Vollmacht persönlich.
> - **Gebühr:** Nach § 39b StV TG ist die erstmalige Fristerstreckung gebührenfrei, jedes weitere Gesuch kostet CHF 30 Kanzleigebühr. ⚠ Ob das auch bei natürlichen Personen angewendet wird, ist offen. StP 155 Nr. 2 nennt die Gebühr nur für juristische Personen (c0003).
> - **Bei Fristversäumnis:** Es folgen Mahnung mit Nachfrist, danach Ermessensveranlagung und Busse (§§ 155 Abs. 3, 162 StG TG).
> 
> Die fachliche Beurteilung bleibt bei Ihnen. Den Wortlaut von c0002 habe ich im Chunk selbst geprüft.

## q15

**Frage:** ZH: Bis wann ist die Steuererklärung 2025 einzureichen und wie lange wird höchstens Fristerstreckung gewährt?

**Soll (Referenz):** Einreichung bis 31.03.2026; Fristerstreckung längstens bis 30. November (ZStB 132.1 / WL ZH 2025).

**Antwort des Agenten** (50.3 s · Tools: 10 Aufrufe read, read):

> **Kanton Zürich, Steuerjahr 2025 (Einreichung 2026)**
> 
> - **Einreichefrist:** 31. März 2026. Die Steuererklärung ist zusammen mit dem Wertschriftenverzeichnis online oder beim Scan-Center einzureichen. Quellen: [WL ZH 2025 S. 7](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0017.md) und [ZStB 132.1 Ziff. G.I](steuerwiki/chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0022.md).
> - **Maximale Fristerstreckung:** bis 30. November 2026. Rechtzeitig eingereichten Gesuchen ist «längstens bis 30. November des der Steuerperiode folgenden Kalenderjahres» zu entsprechen. Quelle: [ZStB 132.1 Ziff. G.II.2.b](steuerwiki/chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0024.md). In der Fassung bis 2025 steht dasselbe ([ZStB 132.1 bis 2025, c0023](steuerwiki/chunks/zh/2025/zh-zstb-132-1-bis-2025/zh-zstb-132-1-bis-2025__c0023.md)). Ich habe diese Fassung nicht selbst geöffnet, die Angabe stammt aus dem Themenblatt [Fristen & Verfahren](steuerwiki/wiki/themen/fristen-verfahren.md).
> 
> **Weitere Regeln**
> - Das Gesuch muss **vor Fristablauf** beim Gemeindesteueramt eingehen. Ein verspätetes Gesuch ist abzuweisen. Eine abgelaufene Frist kann nicht erstreckt, höchstens wiederhergestellt werden ([ZStB 132.1, c0024](steuerwiki/chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0024.md)). Mahnfristen sind nicht erstreckbar ([WL ZH 2025 S. 7](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0017.md)).
> - Das Gemeindesteueramt erstreckt von Amtes wegen bis 30. September 2026. Das gilt für im Kanton wohnhafte Selbständigerwerbende, für übrige einer Branchenabteilung zugewiesene natürliche Personen und für ausserkantonal Wohnhafte (L-/B-Fälle) ([ZStB 132.1, c0023](steuerwiki/chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0023.md)).
> - Zur Direkten Bundessteuer: Die Steuererklärung deckt Kanton und Bund ab. Die Frist bestimmt der Kanton ([Art. 124 Abs. 2 DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-124.md)). Die Fristerstreckung stützt sich zusätzlich auf Art. 119 DBG.
> 
> **Heute ist der 9. November 2026.** Die Frist vom 31. März 2026 ist abgelaufen. Falls für den Fall noch keine Erstreckung bewilligt wurde, kann sie nicht mehr erstreckt werden. Dann bleibt nur die Wiederherstellung nach § 15 StV bzw. Art. 119 Abs. 2 und 124 Abs. 4 DBG, und über sie entscheidet das Gemeindesteueramt. Läuft eine Erstreckung, endet sie spätestens am 30. November 2026, also in gut drei Wochen.
> 
> **Status:** Der Status der Quellen ist nicht im Wiki-Frontmatter geprüft. Das Themenblatt ist ein `entwurf` (Agent, 2026-11-09). Die fachliche Beurteilung bleibt bei SB/ML.
> 
> Gilt nur für ZH. Falls der Wohnsitz am 31.12.2025 in einem anderen Kanton lag (AR, SG, TG), gelten dort andere Regeln.

## q16

**Frage:** AR: Was kostet die zweite Fristverlängerung?

**Soll (Referenz):** CHF 25 (erste Verlängerung kostenlos, jede weitere CHF 25; MB 18 / WL AR 2025).

**Antwort des Agenten** (38.4 s · Tools: 5 Aufrufe read, memory_search):

> **Kanton AR, Steuerjahr 2025 (Einreichung 2026): Fr. 25.– für die zweite Fristverlängerung.** Die erste ist kostenlos. Das gilt für die Staats- und Gemeindesteuer. Für die direkte Bundessteuer habe ich keine eigene Gebühr gefunden, die kantonale Steuererklärung deckt beide Ebenen ab.
> 
> **Fundstellen**
> - Die WL AR 2025, S. 4, sagt: «nur die erste Fristverlängerung kostenlos ist. Jede weitere Fristverlängerung kostet Fr. 25.–» (`ar-wl-2025__c0012`).
> - Das Merkblatt 18 (gültig ab 1.9.2025, S. 1) nennt «Fristverlängerungen (im Wiederholungsfall): Fr. 25» als Gebührenansatz nach der kantonalen Kanzleigebührenverordnung (`ar-mb-18__c0001`).
> - Das Merkblatt gilt für die Steuerjahre 2025–2027. Verfahrensgebühren richten sich nach dem Zeitpunkt der Handlung, hier 2026, also gilt es.
> 
> **Status:** ☑️ agent-geprüft, nicht von einer Fachperson verifiziert (`verfahren.fristerstreckung`).
> 
> **Offen**
> - Die Quellen sagen nicht, ob die Gebühr pro weitere Verlängerung anfällt (dritte, vierte …) oder nur einmal. Der Wortlaut «jede weitere» spricht für pro Verlängerung.
> - Das Merkblatt 18 sagt zudem, im ordentlichen Veranlagungsverfahren dürften Gebühren nur bei schuldhafter Verletzung von Mitwirkungspflichten erhoben werden. Das Merkblatt nennt die Fristverlängerung aber ausdrücklich als Gebührentatbestand. Ich habe dazu keine weitere Auslegung gefunden.
> - Die Aussage «erste kostenlos» steht nur in der WL 2025. Für 2026 ist sie nicht belegt, und ein Wert für 2026 ist im Wiki nicht bestätigt.
> 
> Ich bin von Appenzell Ausserrhoden und Steuerjahr 2025 ausgegangen. Falls du Innerrhoden (AI) oder ein anderes Jahr meinst, sag Bescheid. AI ist im Wiki nicht abgedeckt.

## q17

**Frage:** Krankheitskosten SG 2025: Ab welchem Selbstbehalt sind sie abziehbar – und beim Bund?

**Soll (Referenz):** SG: Selbstbehalt 2 % (Art. 46 StG SG); Bund: 5 % (Art. 33 Abs. 1 lit. h DBG, KS 11).

**Antwort des Agenten** (42.5 s · Tools: 4 Aufrufe read, exec):

> **Krankheits- und Unfallkosten, Steuerjahr 2025**
> 
> | Ebene | Selbstbehalt | Abziehbar sind … | Fundstelle | Status |
> |---|---|---|---|---|
> | **SG (Staats- und Gemeindesteuer)** | **2 %** | selbst getragene Kosten, die 2 % der Nettoeinkünfte übersteigen | Art. 46 Abs. 1 lit. a StG SG ([Chunk](steuerwiki/chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-46.md)); Wegleitung SG 2025 Ziff. 21.1 | ☑️ |
> | **Bund (DBSt)** | **5 %** | selbst getragene Kosten, die 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen | Art. 33 Abs. 1 lit. h DBG ([Chunk](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t3.md)); ESTV-KS 11 Ziff. 5.3 | ☑️ |
> 
> **Berechnung im SG-Formular**
> - Basis ist das Nettoeinkommen Ziff. 20.
> - Abzug (Code 240) = Summe der Kosten nach Abzug von Leistungen Dritter, minus 2 % von Ziff. 20 (Kanton) bzw. 5 % (Bund). Er ist nur gültig, wenn das Ergebnis positiv ist.
> - Das SG-Formular weist den Bundes-Selbstbehalt von 5 % in der Wegleitung aus (Wegleitung SG 2025, Ziff. 21.1).
> - Der Bundesabzug wird also anders berechnet als der kantonale.
> 
> **Zusätzlich beachten**
> - Es zählen nur selbst getragene Kosten. Vergütungen der Krankenkasse oder anderer Dritter sind abzuziehen.
> - Behinderungsbedingte Kosten (Ziff. 21.2) gehören nicht hierher. Sie werden ohne Selbstbehalt abgezogen, sowohl im Kanton (Art. 46 Abs. 1 lit. abis StG SG) als auch beim Bund (Art. 33 Abs. 1 lit. hbis DBG).
> - Krankenkassenprämien sind keine Krankheitskosten. Sie gehören in den Versicherungsabzug.
> - Das KS 11a der ESTV gilt erst ab Steuerperiode 2027. Für 2025 gilt das KS 11 vom 31.08.2005.
> 
> Details zur Abgrenzung (Heim, Diät, Pauschalen) stehen in [Krankheits-, Unfall- und Behinderungskosten](steuerwiki/wiki/themen/krankheits-behinderungskosten.md). Die fachliche Beurteilung im Einzelfall bleibt bei der Fachperson.

## q18

**Frage:** PK-Einkauf CHF 20'000 wurde über den Lohn abgezogen (Lohnausweis Ziff. 10.2). Darf er nochmals in der Steuererklärung abgezogen werden?

**Soll (Referenz):** Nein – BVG-Einkauf über Lohnabzug (Lohnausweis Ziff. 10.2) ist bereits im Nettolohn berücksichtigt; nur direkt bezahlte Einkäufe separat abziehen.

**Antwort des Agenten** (45.4 s · Tools: 7 Aufrufe read):

> **Nein, nicht nochmals.** Der Einkauf von CHF 20'000, der im Lohnausweis unter Ziff. 10.2 steht, wirkt bereits über den Nettolohn.
> 
> **Begründung**
> - Die ESTV-Wegleitung zum Lohnausweis sagt, Ziff. 11 sei der «für die Steuererklärung massgebende Nettolohn». Er ergibt sich aus dem Bruttolohn (Ziff. 8) abzüglich der Abzüge nach Ziff. 9 und 10. Ziff. 10.2 ist also schon abgezogen. (Bund, WL Lohnausweis 2026, Rz 47, S. 15, `bund-wl-lohnausweis-2026__c0038`; Status 🟡 extrahiert.) Eine Wegleitung für 2025 liegt im Wiki nicht vor. Für 2025 wird gleicher Aufbau angenommen, was nicht bestätigt ist.
> - Rz 46 unterscheidet davon die Einkäufe, die Sie selbst bezahlt haben und die nicht vom Lohn abgezogen wurden. Diese bescheinigt die Pensionskasse mit Formular 21 EDP, und nur sie kommen als eigener Abzug in die Steuererklärung (`bund-wl-lohnausweis-2026__c0037`).
> - Kantonal ist es gleich:
>   - ZH: Ziff. 16.1 ist abziehbar, soweit die Einkünfte «nicht bereits um diese Beiträge gekürzt worden sind» (WL ZH 2026 UJ S. 15, `zh-wl-2026-uj__c0088`).
>   - SG: nochmaliger Abzug unter Ziff. 13.2 ausgeschlossen (WL SG 2025, `sg-wl-2025__c0086`).
>   - TG: ordentliche Beiträge sind in der Regel schon vom Bruttolohn abgezogen (WL TG 2025, `tg-wl-2025__c0093`).
>   - AR: Ziff. 13.2 gilt nur für nicht vom Lohn abgezogene Einkäufe. Der Eintrag in den Daten ist ⚠️ strittig, die Bund-Regel ist nicht aus AR-Quellen belegt.
> 
> **Praktisch**
> - Als Einkommen setzen Sie den Nettolohn (Ziff. 11) ein, nicht den Bruttolohn.
> - Tragen Sie die CHF 20'000 nicht zusätzlich unter Einkauf 2. Säule ein: ZH 16.1 / Code 280, SG 13.2 / Code 218 bzw. 219, TG 15.2 / Code 343 bzw. 344, AR 13.2. Das wäre der typische Doppelabzug.
> - Dass der Betrag im Lohnausweis steht, ersetzt nicht die Prüfung der Sperrfrist. Wer innert 3 Jahren nach dem Einkauf Kapital bezieht (auch WEF-Vorbezug), verliert den Abzug bzw. er wird nachträglich korrigiert (Art. 79b Abs. 3 BVG, KS 17 Ziff. II.2.3, `bund-ks-17__c0012`).
> - Den Einkaufsbetrag und die Einkaufslimite bestätigt die Pensionskasse, nicht das Steuerrecht. Prüfen Sie CHF 20'000 gegen die Einkaufsbescheinigung.
> 
> Kanton und Steuerjahr habe ich nicht, die Antwort gilt deshalb für Bund, ZH, SG, TG und AR. Nennen Sie mir Wohnsitzkanton (Stand 31.12.) und Steuerjahr, dann prüfe ich die Ziffer im passenden Formular konkret. Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## q19

**Frage:** Weiterbildungskosten CHF 15'000 (ZH, 2025), Arbeitgeber hat nichts bezahlt. Wie viel ist abziehbar (Kanton/Bund)?

**Soll (Referenz):** ZH Staat max. CHF 12'400 (zh-stg-2025__par-31-t4); Bund max. CHF 13'000 (bund-dbg-2025__art-33-t4).

**Antwort des Agenten** (35.4 s · Tools: 8 Aufrufe read):

> **Abziehbar sind bei der Staatssteuer ZH CHF 12'400 und bei der direkten Bundessteuer CHF 13'000.** Die Werte gelten für Steuerjahr 2025, pro Person.
> 
> | Ebene | Kosten | Höchstbetrag 2025 | Abzug | Nicht abziehbar |
> |---|---|---|---|---|
> | Staats-/Gemeindesteuer ZH | 15'000 | 12'400 | **CHF 12'400** | CHF 2'600 |
> | Direkte Bundessteuer | 15'000 | 13'000 | **CHF 13'000** | CHF 2'000 |
> 
> Der Arbeitgeber hat nichts bezahlt. Es fällt also kein Beitrag Dritter weg, und die vollen CHF 15'000 zählen als selbst getragene Kosten. Beide Beträge sind daher gekappt.
> 
> **Fundstellen (Steuerjahr 2025)**
> - Kanton: § 31 Abs. 1 lit. k StG ZH, «bis zum Gesamtbetrag von Fr. 12 400» (`zh-stg-2025__par-31-t4`).
> - Bund: Art. 33 Abs. 1 lit. j DBG, «13 000 Franken» (`bund-dbg-2025__art-33-t4`).
> - Die Wegleitung ZH 2025, S. 16, nennt beide Beträge nebeneinander (`zh-wl-2025__c0093`). Der Status der Werte im Wiki ist ☑️ agent-geprüft, nicht ✅ verifiziert.
> 
> **Zu prüfen, bevor du die Beträge einträgst**
> - Die Voraussetzung muss erfüllt sein: ein erster Abschluss auf der Sekundarstufe II liegt vor, oder die Person ist über 20 und es geht nicht um Kosten bis zu diesem ersten Abschluss. Umschulungskosten sind im Höchstbetrag enthalten.
> - Die Kosten müssen berufsorientiert sein. Hobby oder Liebhaberei ist nicht abziehbar.
> - Notwendige Nebenkosten zählen in den Höchstbetrag hinein, zum Beispiel Fahrten zum Kursort (KS 42 Ziff. 4.3). Die CHF 15'000 sind hier schon über beiden Limiten, das ändert also nichts mehr.
> - Für den Zeitpunkt gilt die Fälligkeit bzw. Zahlung, nicht der Kursbesuch. Nur 2025 fällige oder bezahlte Beträge zählen für 2025.
> - Bei Ehepaaren steht der Höchstbetrag jedem Ehegatten einzeln zu (KS 42 Ziff. 4.3). Hat der Ehegatte oder die Ehegattin ebenfalls Kosten, gilt für diese Person ein eigenes Maximum.
> - Dem Arbeitgeber könnte direkt bezahlt worden sein, ohne dass es im Lohnausweis steht. Das sollte man bei der Person nochmals bestätigen (Lohnausweis Ziff. 13.3, WL Lohnausweis 2026 S. 18).
> 
> **Ausfüllen:** Ziff. 16.2, Code 292, mit dem vollständig ausgefüllten Formular 367 «Berufsorientierte Aus- und Weiterbildungskosten». Das Formular trennt Staats- und Bundessteuer (WL ZH 2025 S. 16). Kursrechnungen und Zahlungsnachweise gehören dazu.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## q20

**Frage:** Spenden CHF 50 an eine gemeinnützige Organisation (TG 2025) – abziehbar?

**Soll (Referenz):** Nein – TG: Zuwendungen nur abziehbar, wenn sie CHF 200 übersteigen (StG TG § 34 Abs. 1 Ziff. 11); Bund: ab CHF 100.

**Antwort des Agenten** (43.2 s · Tools: 5 Aufrufe read, exec):

> **Nein, CHF 50 sind im TG-Steuerjahr 2025 weder bei der Staats-/Gemeindesteuer noch bei der direkten Bundessteuer abziehbar.** Das gilt, wenn es die einzige Spende des Jahres ist. Mehrere Spenden zählen zusammen.
> 
> | Ebene | Regel 2025 | Ergebnis bei CHF 50 | Fundstelle |
> |---|---|---|---|
> | **Kanton TG** (Staats- und Gemeindesteuer) | Abziehbar ist nur der Betrag, der gesamthaft CHF 200 übersteigt (Selbstbehalt). Obergrenze: bei Nettoeinkommen bis CHF 40'000 maximal CHF 8'000, darüber maximal 20 % des Nettoeinkommens. | 50 − 200 < 0, also **CHF 0** | § 34 Ziff. 11 StG TG (`tg-stg__par-34-t4`); StP 34 Nr. 23 Ziff. 2.2 (`tg-stp-34-23__c0003`); Formular 6 TG 2025 S. 1 (`tg-form-06-2025__c0002`) |
> | **Bund** (DBG) | Die Leistungen müssen im Steuerjahr mindestens CHF 100 erreichen. Obergrenze: 20 % der um die Aufwendungen verminderten Einkünfte. | 50 < 100, also **CHF 0** | Art. 33a DBG 2025 (`bund-dbg-2025__art-33a`); StP 34 Nr. 23 Ziff. 2.3 |
> 
> Der Betrag ist also kein Abzug, aber auch kein Fehler: Die Spende liegt unter beiden Mindestgrenzen.
> 
> **Was sich ändert, wenn es mehr Spenden gibt:**
> - **Bund:** Ab CHF 100 gesamthaft im Jahr ist der volle Betrag abziehbar, ohne Selbstbehalt.
> - **Kanton:** Erst der Teil über CHF 200 zählt. Bei gesamthaft CHF 500 wären das CHF 300.
> - **Bund:** Bei CHF 500 wären es voll CHF 500.
> 
> **Voraussetzungen, die bei grösseren Beträgen gelten:**
> - Die Organisation muss ihren Sitz in der Schweiz haben und wegen öffentlicher oder gemeinnütziger Zwecke steuerbefreit sein. Die Liste führt die Steuerverwaltung. Mitgliederbeiträge sind nicht abziehbar.
> - Erfasst werden die Spenden im Formular 6 («Zuwendungen für gemeinnützige oder öffentliche Zwecke», Code 366), übertragen auf Ziff. 23.2 des Hauptformulars.
> - Jede Zuwendung wird einzeln mit Name und Sitz der Institution aufgeführt. Sammelvermerke wie «Spenden an diverse Organisationen» werden nicht anerkannt.
> - Quittungen sind erst ab CHF 1'000 pro Zuwendung beizulegen. Die Steuerverwaltung kann sie bei Bedarf auch für kleinere Beträge nachfordern (WL TG 2025 S. 46, `tg-wl-2025__c0220`).
> 
> **Zur Verlässlichkeit:** Die Mindestgrenzen (CHF 200 Kanton, CHF 100 Bund) stimmen in Gesetz, Praxis und Formular überein. Die TG-Quellen sind in dieser Wissensbasis als «agent-geprüft» geführt und nicht von einer Fachperson verifiziert. Die Beurteilung des Einzelfalls bleibt bei Ihnen.

## q21

**Frage:** Was ändert sich 2026 bei der Säule 3a (Einkauf) und wo wird das im ZH-Formular 2026 eingetragen?

**Soll (Referenz):** Ab 2026 Einkauf (Nachzahlung) Säule 3a für Beitragslücken ab 2025 (max. 7'258 pro Einkaufsjahr, BVV 3 Art. 7a, KS 18a); ZH-Formular 2026: Ziff. 14.3 (Code 264, Detailfelder 276/278).

**Antwort des Agenten** (36.0 s · Tools: 6 Aufrufe read, exec):

> Kanton und Steuerjahr sind hier ZH 2026. Die Werte stammen aus der Fassung für unterjährige Steuerpflicht (UJ). Das reguläre ZH-Formular und die reguläre Wegleitung 2026 sind laut Wiki (Stand 09.11.2026) noch nicht publiziert. Ziffern und Codes müssen Sie deshalb am regulären Formular nochmals prüfen.
> 
> ## Was sich 2026 ändert
> 
> **Neu 2026: nachträglicher Einkauf in die Säule 3a.** Die Höchstbeträge für den ordentlichen Beitrag bleiben bei Bund und ZH unverändert (Kanton und Bund identisch, 2025 = 2026):
> - mit 2. Säule: CHF 7'258
> - ohne 2. Säule: 20 % des Erwerbseinkommens, höchstens CHF 36'288
> 
> Quelle: BSV-Masszahlen 25/26 S. 1, WL ZH 2026 UJ S. 14 (`zh-wl-2026-uj__c0075`).
> 
> Voraussetzungen für den Einkauf (BVV 3 Art. 7a, `bund-bvv3__art-7a-t1`; WL ZH 2026 UJ S. 14, `zh-wl-2026-uj__c0077`):
> 1. Der Einkauf ist nur **zusätzlich** zum ordentlichen Beitrag möglich. Im Einkaufsjahr muss der für die Person maximal zulässige ordentliche Beitrag **vollständig** einbezahlt sein (CHF 7'258 bzw. 20 %, höchstens CHF 36'288).
> 2. In den Jahren der Beitragslücke müssen AHV/IV/EO-Beiträge geleistet worden sein. Die Person war damit zu 3a-Beiträgen berechtigt.
> 3. Eingekauft werden können nur Beitragslücken **ab 1.1.2025**, innerhalb der zehn Jahre vor dem Einkauf. Der Einkauf darf höchstens der Summe der Lücken entsprechen, in jedem Fall höchstens **CHF 7'258 pro Steuerjahr**. Das entspricht 8 % des oberen BVG-Grenzbetrags (BVV 3 Art. 7a Abs. 2).
> 4. Praktisch ist 2026 also nur die Lücke 2025 einkaufbar. Für das Steuerjahr 2025 selbst ist kein Einkauf abziehbar.
> 5. Nach Bund (KS 18a S. 6, `bund-ks-18a__c0017`) kann jede Jahreslücke nur durch einen einzigen Einkauf ausgeglichen werden. Nach dem Bezug einer Altersleistung aus Säule 3a ist kein Einkauf mehr möglich.
> 6. Beilegen müssen Sie die Einkaufsbestätigung der 3a-Einrichtung.
> 
> ## Wo im ZH-Formular 2026 (Form. 300, Steuererklärung ZH)
> 
> Der Einkauf steht auf **Seite 3, Ziff. 14.3** und ist eine eigene Zeile unter den ordentlichen Beiträgen (Formular 300 ZH 2026 UJ S. 3, `zh-form-300-2026-uj__c0008`):
> 
> | Ziffer | Position | Code |
> |---|---|---|
> | 14.1 / 14.2 | Ordentliche 3a-Beiträge, Person 1 / Person 2 | 260 / 261 (effektiv 262 / 263) |
> | **14.3** | **Einkauf Säule 3a, Person 1 / Person 2** | **276 / 278**, Summe in der Hauptkolonne **Code 264** |
> 
> Staat und Bund haben dieselbe Zeile. Die Kolonnen Staats- und Bundessteuer sind getrennt, die Limiten sind aber gleich.
> 
> Rechenweg laut Wiki (Zuordnung ZH 2026): Pro Person gilt min(Einkauf; Summe der Beitragslücken ab 1.1.2025; 7'258). Das ergibt Code 276 bzw. 278, die Summe kommt in Code 264.
> 
> Zwei Abgrenzungen:
> - 3a-Guthaben gehört nicht ins Wertschriftenverzeichnis. Auszahlungen aus 3a stehen auf Seite 4, Ziff. 40.
> - Ein PK-Einkauf in die 2. Säule ist etwas anderes. Er gehört in Ziff. 16.1 (Code 280), sofern er nicht schon im Lohnausweis abgezogen ist.
> 
> ## Offene Punkte
> 
> - **Status:** ☑️ agent-geprüft, nicht von der Fachperson verifiziert.
> - **Rechtsgrundlage ZH:** Für ZH ist der Einkauf nur über die Wegleitung UJ und das Formular belegt, nicht über eine kantonale Norm. Die Bundesgrundlage ist BVV 3 Art. 7a/7b (in Kraft 1.1.2025).
> - **Nicht geklärt:** Das Wiki hat kein Zahlenbeispiel der Wegleitung. Ebenso fehlen Angaben zu unterjährigem PK-Eintritt oder -Austritt, Grenzgängern und Teilzeit-PK-Anschluss. Das ist laut Wiki ⚠ zu prüfen.
> - **Reguläres Formular 2026:** Sobald es publiziert ist, die Ziffer 14.3 und die Codes 276/278/264 dort abgleichen.
> 
> Details: `steuerwiki/wiki/themen/saeule-3a.md`, `quick/zuordnung-zh-2026.md`, `wiki/zh/zuordnung-zh-2026-detail.md` (Abschnitt 14.3). Die fachliche Beurteilung bleibt bei SB/ML.

## q22

**Frage:** Wie wird die Verrechnungssteuer auf Schweizer Dividenden zurückgefordert und wo wird der Anspruch ausgewiesen?

**Soll (Referenz):** Verrechnungssteuer (35 %) via Wertschriftenverzeichnis (Kolonne A) zurückfordern; Anspruch im Wertschriftenverzeichnis ausgewiesen (z.B. ZH Code 540) und mit der Steuer verrechnet/ausbezahlt.

**Antwort des Agenten** (56.7 s · Tools: 9 Aufrufe read, memory_search, exec, ls):

> Ich habe das Steuer-Wiki durchgesehen und die Gesetzesartikel geöffnet. Hier die Antwort. Kanton und Steuerjahr haben Sie nicht genannt, deshalb gilt der Ablauf allgemein, mit den Abweichungen für AR, SG, TG und ZH.
> 
> ## So wird zurückgefordert
> 
> Es gibt keine separate Rückforderung: Der Antrag läuft über die ordentliche Steuererklärung.
> 
> 1. **Dividende brutto im Wertschriftenverzeichnis deklarieren.** Schweizer Dividenden kommen in Kolonne A (Erträge mit Verrechnungssteuerabzug). Das Verzeichnis ist ZH Form. 340 bzw. AR/SG/TG Form. 2. Die Bank liefert die Zahlen im Steuerauszug oder E-Steuerauszug.
> 2. **Anspruch berechnen.** Er beträgt 35 % vom Total Kolonne A (Art. 13 Abs. 1 lit. a VStG). Das Formular rechnet ihn aus (AR/SG: Code 999, TG: Ziff. 10).
> 3. **Antrag stellen.** Das geschieht mit der Unterschrift unter dem Verzeichnis. Die Person bestätigt damit, dass auf allen Erträgen in Kolonne A die Verrechnungssteuer abgezogen wurde (WL ZH 2026 UJ S. 24). Dazu kommt das Auszahlungskonto (TG: Formular 1, S. 1).
> 4. **Zuständig ist der Wohnsitzkanton.** Massgebend ist der Wohnsitz am Ende des Kalenderjahres der Fälligkeit (Art. 30 Abs. 1 VStG, ebenso Art. 22 Abs. 1). TG bestätigt das für die Fälligkeiten 2026 und verlangt Wohnsitz am 31.12. (WL TG 2026 S. 35).
> 
> ## Wo wird der Anspruch ausgewiesen?
> 
> | | Ertrag (Kolonne A) | Anspruch 35 % | Übertrag in die Steuererklärung |
> |---|---|---|---|
> | **AR 2025** | Form. 2, Spalte A | «Verrechnungssteueranspruch: 35 % vom Bruttoertrag (Total A)», Code 999 (Formular 2 AR 2025 S. 2) | Ertrag Ziff. 4.1 (Beteiligungen ≥ 10 %: 4.2/4.3), Steuerwert Ziff. 30.1 |
> | **SG 2025** | Form. 2, Spalte A | Code 999 (Formular 2 SG 2025 S. 2) | Ertrag Ziff. 4.1, Steuerwert Ziff. 30.1 |
> | **TG 2025/2026** | Form. 2, Spalte 8 | Form. 2 Ziff. 10, 35 % vom Total I (WL TG 2026 S. 35) | Ertrag Ziff. 4, Steuerwert Ziff. 30.1 |
> | **ZH 2025** | Form. 340, Kolonne A | 35 % von Kolonne A (WL ZH 2025 S. 25) | Total Bruttoertrag A+B in Ziff. 4.1 (Code 150) |
> 
> Der Anspruch steht also nicht in der Steuererklärung (Form. 1/300) selbst. Er steht im Wertschriftenverzeichnis, also Form. 340 oder Form. 2. Dort gibt es keine eigene Bundesspalte.
> 
> ## Bedingungen und Fallen
> 
> - **Verwirkung bei Nichtdeklaration:** Wer verrechnungssteuerbelastete Einkünfte oder das zugrunde liegende Vermögen nicht angibt, verliert den Anspruch (Art. 23 Abs. 1 VStG). Ausnahme: Wurde fahrlässig nicht angegeben und wird im noch offenen Veranlagungs-, Revisions- oder Nachsteuerverfahren nachdeklariert, tritt keine Verwirkung ein (Abs. 2).
> - **Nutzungsberechtigung:** Anspruch hat, wer bei Fälligkeit zur Nutzung des Vermögenswerts berechtigt war (Art. 21 Abs. 1 lit. a VStG). Bei Steuerumgehung ist die Rückerstattung unzulässig (Abs. 2).
> - **Frist:** Der Anspruch erlischt, wenn der Antrag nicht innert drei Jahren nach Ablauf des Fälligkeitsjahrs gestellt wird (Art. 32 Abs. 1 VStG). Frühestens ist der Antrag nach Ablauf des Fälligkeitsjahrs möglich (Art. 29 Abs. 2).
> - **Qualifizierte Beteiligungen (≥ 10 %):** Die Bruttoausschüttung wird ungekürzt deklariert (Code BP/BG). Die Teilbesteuerung läuft über einen separaten Abzug und ändert die 35 % nicht (WL ZH 2026 UJ S. 25, WL AR 2025 S. 11).
> - **Konten bis Fr. 200 Bruttozins** gehören in Kolonne B, weil dort keine Verrechnungssteuer abgezogen wird. Sie sind trotzdem zu deklarieren (AR/SG/ZH).
> - **Ausländische Dividenden** sind ein anderer Fall: Die ausländische Quellensteuer wird über das Formular DA-1 zurückgefordert bzw. angerechnet, nicht über die 35 %.
> 
> ## Fundstellen und Status
> 
> - **Gesetzestext:** VStG (Fassung ab 01.01.2025, gilt laut Wiki für 2025–2027). Gelesen habe ich Art. 13, 21, 22, 23, 29, 30 und 32 unter `chunks/bund/2025/bund-vstg/…`.
> - **Kantonale Angaben:** `wiki/themen/wertschriften-verrechnungssteuer.md` mit den Chunks der Wegleitungen und Formulare. Die Chunks WL ZH 2026 UJ S. 24, WL TG 2026 S. 35 und Formular 2 AR 2025 S. 2 habe ich selbst geöffnet.
> - **Nicht geöffnet:** die ZH-2025-Chunks und das SG-Formular, die Zitate dazu stammen aus der Themenseite.
> - **Status:** Bei den gesehenen SG- und TG-Zeilen steht ☑️ agent-geprüft. Eine Verifikation durch die Fachperson (✅) habe ich nirgends gesehen. Die fachliche Beurteilung bleibt bei SB/ML.
> - **Lücken:** Für AR und ZH 2026 liegt noch kein reguläres Formular bzw. keine Wegleitung vor (Stand 09.11.2026). Ziffern und Codes 2026 sind dort vorbehalten. Zahlen aus 2025 habe ich nicht übertragen.
> 
> Sagen Sie mir Kanton und Steuerjahr, dann gebe ich Ihnen die genauen Ziffern und Codes dazu.

## q23

**Frage:** Vergleiche den Versicherungsabzug 2025 für Alleinstehende ohne Kinder in AR, SG, TG, ZH und beim Bund.

**Soll (Referenz):** Alleinstehend ohne Kinder 2025 (mit 2. Säule/3a): AR 2'700 · SG 3'400 · TG 3'500 · ZH 2'900 · Bund 1'800.

**Antwort des Agenten** (37.8 s · Tools: 5 Aufrufe read):

> # Versicherungsabzug 2025 – Alleinstehende ohne Kinder
> 
> **Annahme:** «Alleinstehend» heisst hier «übrige Steuerpflichtige» (nicht in ungetrennter Ehe), ohne Kinder und ohne unterstützte Personen. Der Kinderzuschlag entfällt damit. Alle Werte gelten für Steuerjahr 2025 und sind CHF-Maximalbeträge.
> 
> | | Mit Beiträgen an 2. Säule/3a | Ohne Beiträge an 2. Säule/3a |
> |---|---|---|
> | **Bund (DBG)** | 1'800 | 2'700 |
> | **AR** | 2'700 | 2'700 (keine Erhöhung) |
> | **SG** | 3'400 | 3'900 |
> | **TG** (Kanton) | 3'500 | 3'500 (keine Erhöhung) |
> | **TG** (Bund, im gleichen Formular) | 1'800 | 2'700 |
> | **ZH** | 2'900 | 4'350 |
> 
> Der Abzug ist immer der **niedrigere** Betrag aus den bezahlten Prämien und Sparzinsen (nach Abzug der Prämienverbilligung) und dem Maximalbetrag.
> 
> ## Fundstellen und Status
> 
> Alle Werte haben den Status ☑️ agent-geprüft. Keiner ist ✅ von der Fachperson verifiziert.
> 
> - **Bund:** 1'800 aus [Art. 33 DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t2.md). Die Erhöhung ohne Vorsorge steht in [Art. 33 DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t5.md). Den Betrag 2'700 nennt [RS 2-210 S. 2](steuerwiki/chunks/bund/2025/bund-rs-2-210/bund-rs-2-210__c0006.md).
> - **AR:** [Art. 35 StG AR](steuerwiki/chunks/ar/2025/ar-stg/ar-stg__art-35-t2.md) kennt nur einen einheitlichen Betrag. Beiträge an 2. Säule/3a werden separat nach Art. 35 lit. d/e abgezogen. Das AR-Formular hat keine Bundesspalte. Die Verwaltung wendet die Bundesbeträge automatisch an (WL AR 2025 S. 33, laut `quick/index.md`).
> - **SG:** [Art. 45 StG SG](steuerwiki/chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t2.md) und [WL SG 2025 S. 4](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0003.md). Die Erhöhung für übrige beträgt +500. Die 3'900 sind daher eine Summe (3'400 + 500), die das Wiki selbst berechnet hat.
> - **TG:** [§ 34 StG TG](steuerwiki/chunks/tg/2025/tg-stg/tg-stg__par-34-t3.md). Die kantonale Limite wird ohne Vorsorgebeiträge nicht erhöht. Den Hinweis dazu nennt das Wiki aus [WL TG 2026 S. 44](steuerwiki/chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0209.md), also aus dem Jahr 2026. Für 2025 gilt der Gesetzeswortlaut. Die Bundesbeträge stehen in [Formular 5.2 TG 2025](steuerwiki/chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0002.md). Der erhöhte Bundesabzug von 2'700 lässt sich nicht mit dem ordentlichen Abzug kombinieren.
> - **ZH:** [§ 31 StG ZH](steuerwiki/chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t2.md), [WL ZH 2025 S. 15](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0084.md) und [Formular 365 ZH 2025](steuerwiki/chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md). Ohne Vorsorgebeiträge ist der Betrag «um die Hälfte erhöht» (2'900 → 4'350).
> 
> ## Zum Vergleich
> 
> - **Höhe der Kantone:** TG (3'500) ist am höchsten, dann SG (3'400), ZH (2'900) und AR (2'700). Der Bund liegt mit 1'800 klar darunter.
> - **Erhöhung ohne Vorsorge:** Sie gilt nur bei Bund, SG und ZH. In AR und im Kanton TG gibt es sie nicht, in TG nur beim Bund.
> - **Kantonslimiten nicht auf den Bund übertragen:** Das ist laut Wiki ein typischer Fehler. Die Bundesbeträge sind eigenständig.
> - **Wo die Spalten getrennt sind:** ZH (Formular 365) und TG (Formular 5.2) weisen Staat und Bund in zwei Spalten aus. Bei AR gilt nur die Staatsspalte, bei SG nennt die Wegleitung die Bundeslimiten.
> 
> Die Bundesbeträge zu 2025 stammen aus dem Gesetz und dem Rundschreiben des Jahres. Das ältere KS 30 (Stand 2014) habe ich bewusst nicht herangezogen, weil das Wiki davor warnt.

## q24

**Frage:** Steuerfreie Vermögensbeträge (Sozialabzüge) 2025 in SG für ein Ehepaar mit einem minderjährigen Kind?

**Soll (Referenz):** SG 2025: 150'000 (Ehepaar) + 20'000 pro minderjähriges Kind = 170'000 (sg-stg-2025__art-64).

**Antwort des Agenten** (32.6 s · Tools: 6 Aufrufe read, exec):

> **Steuerfreie Vermögensbeträge (Sozialabzüge Vermögen) 2025, SG, Ehepaar mit einem minderjährigen Kind: CHF 170'000**
> 
> | Position | Betrag | Ziff./Code |
> |---|---|---|
> | Gemeinsam Steuerpflichtige | CHF 150'000 | 36.2 / Code 332 |
> | Zuschlag für 1 minderjähriges Kind | CHF 20'000 | 36.3 / Code 334 |
> | **Total** | **CHF 170'000** | |
> 
> Das Total ist meine Addition der beiden Beträge. Das Wiki nennt es nicht als eigenen Wert.
> 
> **Fundstellen (Staats- und Gemeindesteuer, Steuerjahr 2025)**
> - Der Betrag von CHF 150'000 für gemeinsam Steuerpflichtige steht in WL SG 2025 S. 34, Ziff. 36 (`sg-wl-2025__c0118`). Der Betrag von CHF 20'000 je Kind steht an derselben Stelle.
> - Das Gesetz nennt CHF 75'000 «für jeden Steuerpflichtigen» und CHF 20'000 je Kind (Art. 64 Abs. 1 StG SG, `sg-stg-2025__art-64`). Bei einem Ehepaar entspricht das den CHF 150'000 der Wegleitung.
> - Status im Wiki: ☑️ agent-geprüft. Als verifiziert (✅) ist nichts markiert.
> 
> **Voraussetzungen und Beachten**
> - **Stichtag:** Massgebend sind die Verhältnisse am Ende der Steuerperiode, in der Regel der 31.12.2025 (Art. 64 Abs. 2 StG; WL Ziff. 36). Zivilstand und Kind werden also per 31.12.2025 beurteilt.
> - **Kind:** Der Zuschlag gilt nur für ein minderjähriges Kind unter der elterlichen Sorge oder Obhut, für das ein Kinderabzug nach Art. 48 Abs. 1 lit. a StG möglich ist. Für volljährige Kinder in Ausbildung gibt es Ziff. 36.3 nicht.
> - **Anwendung:** Die Beträge werden vom Reinvermögen (Ziff. 35, Code 326) abgezogen. Das ergibt das steuerbare Vermögen (Ziff. 37, Code 338).
> - **Bund:** Die direkte Bundessteuer kennt keine Vermögenssteuer. Es gibt keinen Bundeswert.
> 
> Meinen Sie mit «Sozialabzüge» auch die Einkommensseite (Kinderabzug, Versicherungsabzug)? Das habe ich hier nicht aufgeführt. Die Werte liegen in `quick/werte-sg-2025.md`: Kinderabzug nach Altersstufe in Art. 48 StG, Versicherungsabzug gemeinsam Besteuerte CHF 6'800 plus CHF 1'100 je Kind.

## q25

**Frage:** Welcher Verzugszins gilt 2026 für die direkte Bundessteuer?

**Soll (Referenz):** 4.00 % (RS 2-215, bund-rs-2-215__c0010/c0011).

**Antwort des Agenten** (34.3 s · Tools: 8 Aufrufe read, memory_search, exec):

> Der Beleg-Chunk fehlt noch im Wortlaut; ich lese ihn.
> 
> **Der Verzugszins bei der direkten Bundessteuer beträgt 2026 4,00 % (Bund, DBG).** Der Satz gilt für Steuerjahr 2026. Er sinkt damit gegenüber 2025, wo er 4,50 % betrug.
> 
> **Fundstelle**
> - Das ESTV-Rundschreiben RS 2-215, Ziff. 3 (S. 3), nennt in der Tabelle «Verzugs- und Rückerstattungszins 4,50 (2025) / 4,00 (2026)». Es verweist auf Art. 164 Abs. 1 DBG und die Zinssatzverordnung EFD (SR 631.014): [RS 2-215 S. 3](steuerwiki/chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0010.md).
> - Das EFD hat die Verordnung am 9. September 2025 angepasst, die Änderung tritt am 1. Januar 2026 in Kraft (gleiche Quelle).
> - Art. 164 Abs. 1 DBG legt den Satz nicht selbst fest. Er sagt nur, dass das EFD ihn festsetzt: [Art. 164 DBG](steuerwiki/chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-164.md).
> - Status im Wiki: ☑️ agent-geprüft. Eine Verifizierung durch die Fachperson fehlt noch.
> 
> **Nebenbefunde**
> - Der Rückerstattungszins hat denselben Satz (4,00 %).
> - Der Vergütungszins für Vorauszahlungen beträgt 2026 0,00 % (2025: 0,75 %).
> - Für 2027 bleiben die Sätze laut RS 2-220, Ziff. 3 unverändert: [RS 2-220 S. 3](steuerwiki/chunks/bund/2027/bund-rs-2-220/bund-rs-2-220__c0010.md). Das habe ich nur im Suchtreffer gesehen, den Chunk nicht vollständig gelesen.
> 
> **Zeitbezug:** Zinsen richten sich nach dem Kalenderjahr der Zahlung (Wiki-Regel 2a). Für die Verzugszins-Berechnung bei Zahlungsverzug 2026 gilt also 4,00 %, unabhängig davon, welche Steuerperiode bezahlt wird. Der Zeitraum ab Fälligkeit der Rechnung (Art. 164 Abs. 2 DBG: 30 Tage nach Zustellung, falls bis zur Fälligkeit keine Rechnung eintraf) ist davon getrennt.
> 
> Der kantonale Verzugszins ist ein anderer Satz. Beispiel AR: 5 % bei der Staats- und Gemeindesteuer, bei der DBSt ab 2026 4,0 %. Andere Kantone habe ich nicht geprüft, du hast auch keinen genannt.

## q26

**Frage:** Wann wird der Eigenmietwert abgeschafft und gilt das schon für 2026?

**Soll (Referenz):** Abschaffung per 1.1.2029 (Bundesratsbeschluss 01.04.2026); für 2025–2028 gilt bisheriges Recht – 2026 also noch Eigenmietwert.

**Antwort des Agenten** (35.0 s · Tools: 8 Aufrufe read, memory_search):

> **Der Eigenmietwert fällt per 1. Januar 2029 weg. Für 2026 gilt er noch unverändert.**
> 
> **Zeitplan**
> - Volk und Stände haben im September 2025 den Bundesbeschluss über die kantonalen Liegenschaftssteuern auf Zweitliegenschaften angenommen. Damit haben sie auch der Abschaffung der Eigenmietwertbesteuerung zugestimmt (Quelle: [MM Bundesrat, c0003](steuerwiki/chunks/bund/dauernd/bund-mm-eigenmietwert-abschaffung/bund-mm-eigenmietwert-abschaffung__c0003.md)).
> - Der Bundesrat hat am 1. April 2026 beschlossen, die Reform per 1. Januar 2029 in Kraft zu setzen (Quelle: [MM Bundesrat, c0002](steuerwiki/chunks/bund/dauernd/bund-mm-eigenmietwert-abschaffung/bund-mm-eigenmietwert-abschaffung__c0002.md)).
> - Die Kantone können dann zeitgleich eine Objektsteuer auf Zweitliegenschaften einführen (Quelle: c0002).
> 
> **Was das für 2026 heisst**
> - Der Eigenmietwert bleibt für Steuerjahr 2026 steuerbar, bei Bund und Kantonen. Das Wiki führt ihn bis und mit 2028 unverändert (Quelle: [Rechtsänderungen](steuerwiki/wiki/themen/rechtsaenderungen.md)). Die neuen Regeln darf man nicht vorzeitig anwenden.
> - Der Unterhaltskostenabzug bleibt bis dahin ebenfalls bestehen.
> - ZH bestätigt das für 2026. Der Regierungsrat hat die Eigenmietwerte wegen des beschlossenen Systemwechsels nicht vorübergehend erhöht (Quelle: [ZH Neubewertung 2026, c0024](steuerwiki/chunks/zh/2026/zh-info-neubewertung-2026/zh-info-neubewertung-2026__c0024.md)). Für ZH gilt 2026 weiter die Liegenschaftenneubewertung.
> 
> **Was ab 2029 gilt** (Quelle: [c0004](steuerwiki/chunks/bund/dauernd/bund-mm-eigenmietwert-abschaffung/bund-mm-eigenmietwert-abschaffung__c0004.md))
> - Der Eigenmietwert ist auf selbstgenutztem Wohneigentum nicht mehr steuerbar.
> - Der Abzug der Liegenschaftsunterhaltskosten entfällt bei Bund, Kantonen und Gemeinden. Bei vermieteten oder verpachteten Liegenschaften bleibt er.
> - Schuldzinsen sind nur noch im Verhältnis des Werts der vermieteten Liegenschaften zum Gesamtvermögen abziehbar.
> - Wer erstmals in der Schweiz ein Eigenheim erwirbt, erhält einen zeitlich und betragsmässig begrenzten Ersterwerberabzug für Schuldzinsen. Die Parameter nennen die erfassten Quellen nicht.
> - Bei der direkten Bundessteuer fallen die Abzüge für Energiespar- und Umweltschutzinvestitionen weg. Die Kantone können sie zeitlich begrenzt beibehalten.
> 
> **Offen**
> - Die kantonale Umsetzung (Objektsteuer, Übergangsregeln) ist im Wiki für AR, SG, TG und ZH nicht erfasst. Dort fehlen auch konkrete Beträge.
> - Status der Quellen: die Medienmitteilung ist amtlich, aber noch nicht von der Fachperson verifiziert.
> - Das Wiki ist seit dem 9.11.2026 auf Stand. Falls das Parlament oder der Bundesrat den Termin seither geändert haben, wäre das nicht erfasst.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## q27

**Frage:** Zitiere die Regel zum Abzug privater Schuldzinsen im DBG (Steuerjahr 2025) mit Artikel.

**Soll (Referenz):** Art. 33 Abs. 1 lit. a DBG (Fassung 2025): private Schuldzinsen im Umfang der steuerbaren Vermögenserträge (Art. 20, 20a, 21) und weiterer CHF 50'000.

**Antwort des Agenten** (32.8 s · Tools: 8 Aufrufe read, memory_search, ls, exec):

> Der Gesetzesartikel liegt als Chunk vor. Ich öffne ihn und prüfe die Aufteilung in Teile.
> 
> **Art. 33 Abs. 1 lit. a DBG** (Bund, direkte Bundessteuer, Steuerjahr 2025):
> 
> > «Von den Einkünften werden abgezogen:
> > a. die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken. Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten oder ihr sonst wie nahe stehenden natürlichen Person zu Bedingungen gewährt, die erheblich von den im Geschäftsverkehr unter Dritten üblichen Bedingungen abweichen;»
> 
> **Fundstelle:** `bund-dbg-2025__art-33-t1` (Chunk `steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md`). Quelle ist das DBG, SR 642.11, Fassung gültig ab 01.01.2025 (Fedlex, laut `registry/sources.yaml`).
> 
> **Einordnung:**
> - Der Abzug ist begrenzt auf die steuerbaren Vermögenserträge nach Art. 20, 20a und 21 DBG plus CHF 50 000.
> - Nach KS 22a Ziff. 3.1 (`bund-ks-22a__c0010`) ist der Betrag von 50 000 ein Grundbetrag. Bei Ehepaaren und Kindern unter elterlicher Sorge gilt er gesamthaft. Massgebend ist der Brutto-Ertrag (KS 22a S. 4, `bund-ks-22a__c0012`).
> - Das ist die Bundesebene. Die Staats- und Gemeindesteuer richtet sich nach dem kantonalen Gesetz. Es gilt dort die gleiche Grenze, jeweils mit den Erträgen nach kantonalem Recht: Art. 35 StG AR, Art. 45 StG SG, § 34 StG TG, § 31 StG ZH.
> 
> **Status:** Das ist Gesetzestext, der maschinell aus Fedlex eingelesen wurde. Eine Prüfung durch die Fachperson (✅ verifiziert) ist nicht vermerkt. Die Zitate in `wiki/themen/schuldzinsen-schulden.md` (Status «entwurf») habe ich nicht gegen das Original-PDF oder -XML in `raw/` abgeglichen. Den Wortlaut habe ich direkt aus dem Chunk übernommen.

## q28

**Frage:** Ist ein Leasingvertrag für das Privatauto steuerlich relevant? Was ist mit den Leasingraten?

**Soll (Referenz):** Leasingraten sind keine Schuldzinsen und grundsätzlich nicht abziehbar (Lebenshaltung); relevant nur für Fahrkosten-Begründung/Geschäftsauto, Vermögen (kein Eigentum).

**Antwort des Agenten** (31.4 s · Tools: 5 Aufrufe read, memory_search, memory_get):

> **Kurz: Der Vertrag ist nicht als Beleg relevant, und die Leasingraten sind bei einem Privatauto nicht abziehbar.**
> 
> Ich habe den Kanton und das Steuerjahr nicht erfragt. Die Quellen unten sind die Wegleitungen 2025 von ZH, SG, AR und TG. Sie sagen alle dasselbe. Der Beleg ist als «Relevanz: nein» eingestuft (Status ☑️ agent-geprüft).
> 
> **Leasingraten**
> - Die Raten sind Lebenshaltungskosten (Art. 34 DBG). Auch der darin enthaltene Zinsanteil ist keine abziehbare Schuldzinse.
> - Die Rate gehört deshalb weder in die Ziffer Schuldzinsen noch ins Schuldenverzeichnis.
> - Fundstellen, alle Wegleitung 2025:
>   - ZH: «Nicht abzugsberechtigt sind Amortisationen … sowie Leasingraten (mit den darin enthaltenen Zinsanteilen)» (WL ZH 2025 S. 14, `zh-wl-2025__c0073`).
>   - SG: Leasinggebühren privater Fahrzeuge sind nicht abzugsfähig (WL SG 2025 S. 25, `sg-wl-2025__c0083`).
>   - AR: Leasingraten privater Fahrzeuge sind nicht abziehbar (WL AR 2025 S. 14, `ar-wl-2025__c0081`).
>   - TG: «Leasingzinsen sind grundsätzlich nicht abzugsfähig» (WL TG 2025 S. 36, `tg-wl-2025__c0173`).
> 
> **Vermögen**
> - Ein geleastes Fahrzeug muss nicht deklariert werden. Das steht ausdrücklich in der ZH-Wegleitung: «Nicht deklariert werden müssen geleaste Fahrzeuge» (WL ZH 2025 S. 22, `zh-wl-2025__c0140`).
> - Ein Auto im Eigentum wäre dagegen zu deklarieren.
> 
> **Wann der Vertrag trotzdem eine Rolle spielt**
> - **Fahrkostenabzug (Arbeitsweg):** Das Privatauto kann nur in begründeten Fällen geltend gemacht werden, mit Kilometeransatz. Dann braucht man vom Vertrag nur die Kilometerleistung. Der Kilometeransatz soll die Leasingkosten mit abgelten. Das ist in den zitierten Chunks nicht belegt (Praxis, nachprüfen).
> - **Selbständigerwerbende:** Bei geschäftlicher Nutzung gehört der Leasingaufwand (Geschäftsanteil) in die Jahresrechnung.
> - **Geschäftsfahrzeug des Arbeitgebers:** Dann ist der Arbeitgeber Leasingnehmer. Fahrkosten sind nicht abziehbar (ZH WL 2025 Ziff. 11). Der Privatanteil steht im Lohnausweis.
> 
> Fachlich sollte SB/ML das abschliessend beurteilen.
> 
> Wenn du mir Kanton (Wohnsitz am 31.12.) und Steuerjahr nennst, prüfe ich die kantonale Ziffer und den Fahrkostenabzug genauer. Für ZH 2025/2026 hat der Beleg keine eigene Zuordnungsseite, für SG und TG sind es Ziff. 34.1 bzw. 34.

## q29

**Frage:** Wie hoch ist der Kinderabzug im Kanton Bern 2025?

**Soll (Referenz):** Nicht im Wiki (nur Bund, AR, SG, TG, ZH).

**Antwort des Agenten** (26.0 s · Tools: 2 Aufrufe memory_search, read):

> Dazu kann ich keine Zahl nennen: Der Kanton Bern ist im Steuer-Wiki nicht abgedeckt. Es enthält nur Bund, AR, SG, TG und ZH (Steuerjahre 2025/2026). Die Suche nach «Bern 2025 Kinderabzug» hat nur Treffer zum Ort Bern geliefert, etwa Zimmermieten und Quellensteuer-Beispiele. Einen Berner Kinderabzug fand sie nicht. Aus dem Gedächtnis nenne ich keinen Betrag, weil das Wiki dafür keine Fundstelle hat.
> 
> Für Bern brauchst du die amtliche Quelle. Das sind die Wegleitung zur Steuererklärung 2025 der Steuerverwaltung Bern (Ziffer «Kinderabzug») oder das Steuergesetz des Kantons Bern (BSG 661.11, Art. 40 Abs. 1 Bst. a StG BE).
> 
> Aus dem Wiki kann ich dir diese Werte nennen:
> - **Bund (direkte Bundessteuer), 2025:** Der Kinderabzug ist einheitlich CHF 6'800 pro Kind. Er ist nicht nach Alter gestaffelt (Fundstelle: `wiki/ar/zuordnung-ar-2025-detail.md`, Limiten-Zeile).
> - **AR, Staats- und Gemeindesteuer, 2025:** CHF 5'300 bis zum vollendeten 4. Altersjahr und CHF 7'400 vom 4. bis zum vollendeten 15. Altersjahr (gleiche Fundstelle).
> 
> Der Bundesabzug gilt auch für Berner Steuerpflichtige. Den Berner Kantonsabzug muss ich offen lassen. Wenn du die Berner Wegleitung 2025 als PDF hast, kann ich sie nach `steuerwiki-pflege` ins Wiki einlesen.

## q30

**Frage:** Ehepaar TG 2025, beide angestellt (Nettolohn 80'000 und 30'000), pendelt mit ÖV-Abo (CHF 1'200 bzw. 900). Erstelle die Abzüge Berufskosten (Fahrkosten, Verpflegung ohne Kantine, Pauschale übrige) je Person für Kanton und Bund mit Fundstellen.

**Soll (Referenz):** TG 2025 je Person: Fahrkosten = ÖV-Abo effektiv (1'200 bzw. 900; Max. 6'000 Staat / 3'300 Bund); Verpflegung ohne Kantine 15/Tag, max. 3'200 (beide Ebenen); übrige Pauschale 3 %: P1 80'000 → 2'400, P2 30'000 → 900 → Minimum 2'000 (beide Ebenen, BKV TG § 4a / BKV Bund).

**Antwort des Agenten** (62.2 s · Tools: 12 Aufrufe read, exec):

> Ich habe die TG-2025-Wegleitung, die Eckwerte TG und Bund und die Originalchunks geprüft. Hier das Ergebnis.
> 
> # Berufskosten TG 2025: Ehepaar, beide unselbständig
> 
> Der Kanton ist TG und das Steuerjahr 2025. Die Berechnung steht in Formular 4.2, Person 2 auf der Rückseite (im Formular «4.3» genannt). Das Total geht in Formular 1 Ziff. 10.1 (Code 240) bzw. Ziff. 10.2 (Code 280) mit je einer Spalte Staat und Bund.
> 
> | Position | Person 1 (Netto 80'000) | Person 2 (Netto 30'000) |
> |---|---|---|
> | Fahrkosten ÖV-Abo, Kanton | 1'200 | 900 |
> | Fahrkosten ÖV-Abo, Bund | 1'200 | 900 |
> | Verpflegung ohne Kantine, Kanton | 3'200 | 3'200 (Annahme, siehe unten) |
> | Verpflegung ohne Kantine, Bund | 3'200 | 3'200 (Annahme, siehe unten) |
> | Übrige Berufskosten, Kanton | 2'400 | 2'000 |
> | Übrige Berufskosten, Bund | 2'400 | 2'000 |
> | **Total Kanton** | **6'800** | **6'100** |
> | **Total Bund** | **6'800** | **6'100** |
> 
> ## Herleitung und Fundstellen
> 
> **Fahrkosten (Form. 4.2 Ziff. 2.1):**
> - Beim ÖV-Abo gelten die tatsächlichen Kosten.
>   - Fundstelle: § 1 Abs. 1 Ziff. 1 BKV TG (`tg-bkv__par-1`).
> - Das Maximum beträgt Kanton 6'000 und Bund 3'300 (Form. 4.2 Ziff. 2.5).
>   - Fundstellen: `tg-form-04-2-2025__c0002`, `tg-wl-2025__c0181` (WL TG 2025 S. 38 f.), für den Bund Art. 26 Abs. 1 lit. a DBG (`bund-dbg-2025__art-26`).
> - Beide Abos liegen unter den Maxima, es gibt also keine Kürzung.
> 
> **Verpflegung ohne Kantine (Form. 4.2 Ziff. 3.1):**
> - Die Pauschale beträgt CHF 15 je auswärtige Hauptmahlzeit und bei ständiger auswärtiger Verpflegung höchstens CHF 3'200 im Jahr.
>   - Fundstellen Kanton: § 2 Abs. 2 BKV TG (`tg-bkv__par-2-t1`), `tg-wl-2025__c0183` (S. 39), `tg-form-04-2-2025__c0003`.
>   - Fundstelle Bund: Anhang Ziff. 1 BKV (`bund-bkv-2025__anhang-1`).
> - Der halbe Abzug (7.50 pro Tag, 1'600 im Jahr) gilt nur mit Kantine oder Verbilligung und entfällt hier.
> 
> **Übrige Berufskosten (Pauschale, Form. 4.2 Ziff. 4):**
> - Die Pauschale beträgt 3 % vom Nettolohn (Lohnausweis Ziff. 11), mindestens 2'000 und höchstens 4'000, für Kanton und Bund gleich.
>   - Fundstellen: § 4a BKV TG (`tg-bkv__par-4a`), `tg-wl-2025__c0187` (S. 40), Anhang BKV (`bund-bkv-2025__anhang-1`).
> - Person 1 hat 3 % × 80'000 = 2'400.
> - Person 2 hat 3 % × 30'000 = 900, angehoben auf das Minimum von 2'000.
> 
> Alle Werte haben den Status ☑️ agent-geprüft. Fachlich beurteilt noch niemand.
> 
> ## Offene Punkte
> 
> 1. **Verpflegung Person 2 und Pensum.**
>    - Ich habe für beide 3'200 gerechnet, also 100 % Pensum und ständige auswärtige Verpflegung. Bei 30'000 Nettolohn ist ein Teilzeitpensum gut möglich.
>    - Bei Teilzeit wird die Pauschale nach Beschäftigungsgrad gekürzt, z.B. 80 % = 2'560 (`tg-wl-2025__c0183`).
>    - Zudem braucht es die Voraussetzung «Heimkehr am Mittag unzumutbar»: grosse Entfernung oder sehr kurze Essenspause (§ 2 Abs. 1 BKV TG).
>    - Bitte Pensum und Arbeitstage von Person 2 klären. Das Total von Person 2 verringert sich entsprechend, beim Bund gleich wie beim Kanton.
> 2. **Lohnausweis Feld F.** Ist es angekreuzt oder liegt ein Geschäftsfahrzeug vor, entfällt der Fahrkostenabzug (`tg-wl-2025__c0176`). Das ÖV-Abo muss belegt sein und darf nicht vom Arbeitgeber getragen werden (`tg-wl-2025__c0175`).
> 3. **Bund-Maximum Fahrkosten.**
>    - Gesetz und RS 2-210 nennen 3'300 (`bund-rs-2-210__c0002`). Die ESTV-Wegleitung 2a 2025 S. 6 nennt noch 3'200 (`bund-wl-2a-2025__c0042`).
>    - Das Gesetz geht vor. Auf dieses Ergebnis hat der Widerspruch keinen Einfluss, da beide Abos weit darunter liegen.
> 4. **Unterjährige Tätigkeit.** Die Pauschalen werden anteilig gekürzt, z.B. 3'200 × 270/360 = 2'400 (`tg-wl-2025__c0176`). Das ist nur relevant, falls jemand nicht das ganze Jahr gearbeitet hat.
> 5. **Teilzeit bei der Pauschale übrige Berufskosten.** Die TG-Wegleitung kürzt hier nur bei unterjähriger Tätigkeit (`tg-wl-2025__c0187`). Die Wiki-Detailseite nennt für den Bund auch eine Kürzung bei Teilzeit. Diesen Bund-Chunk habe ich nicht selbst geöffnet. Bei Teilzeit von Person 2 bitte prüfen, ob die 2'000 beim Bund angemessen zu kürzen sind.
> 
> Soll ich die Verpflegung von Person 2 mit Pensum und Arbeitstagen neu rechnen, sobald du sie hast?

## q31

**Frage:** Ehepaar ZH 2026, beide erwerbstätig, Kind 3 Jahre in der Kita (Kosten CHF 30'000). Wie viel Drittbetreuung ist abziehbar (Kanton und Bund)?

**Soll (Referenz):** ZH 2026 Kanton max. CHF 25'300 pro Kind (zh-stg-2026__par-31-t3); Bund 2026 max. CHF 25'800 (bund-dbg-2026__art-33-t7). Abzug je Ebene getrennt.

**Antwort des Agenten** (32.8 s · Tools: 6 Aufrufe read, memory_search, exec):

> **Steuerjahr 2026, Kanton ZH.** Bei CHF 30'000 Kita-Kosten für ein Kind sind abziehbar:
> 
> | Ebene | Höchstbetrag pro Kind | Abziehbar bei CHF 30'000 |
> |---|---|---|
> | Staats-/Gemeindesteuer | CHF 25'300 | **CHF 25'300** |
> | Direkte Bundessteuer | CHF 25'800 | **CHF 25'800** |
> 
> Die Differenz von CHF 4'700 (Staat) bzw. CHF 4'200 (Bund) ist nicht abziehbar.
> 
> **Fundstellen**
> - Kanton: § 31 Abs. 1 lit. j StG ZH, Fassung 2026: «die nachgewiesenen Kosten, jedoch höchstens Fr. 25 300, für die Drittbetreuung jedes Kindes» ^[zh-stg-2026__par-31-t3]. Dasselbe steht im Formular 300 ZH 2026 UJ, Ziff. 16.6, Code 376 ^[zh-form-300-2026-uj__c0008]. Status ☑️ agent-geprüft.
> - Bund: Art. 33 Abs. 3 DBG, 2026: «höchstens 25 800 Franken» ^[bund-dbg-2026__art-33-t7]. Status ☑️ agent-geprüft.
> 
> **Voraussetzungen**
> - **Kind:** Es hat das 14. Altersjahr noch nicht vollendet und lebt im gleichen Haushalt. Das ist beim 3-jährigen Kind erfüllt.
> - **Erwerbstätigkeit:** Die Kosten müssen in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit stehen. Bei Ehepaaren müssen laut Wegleitung beide gleichzeitig erwerbstätig, in Ausbildung oder erwerbsunfähig sein (Wegleitung/Quick-Seite ZH 2026). Das ist hier gegeben.
> - **Kosten:** Es zählen nur Betreuungskosten. Verpflegung, Sport, Musik oder Ähnliches sind nicht abziehbar. Weist die Kita die Kosten nur pauschal aus, ist laut Wegleitung 20 % als Lebenshaltungskosten zu kürzen. Dann wären bei CHF 30'000 noch CHF 24'000 anrechenbar. Das liegt unter den beiden Maxima.
> - **Belege:** Rechnungen mit Empfänger und Zahlungsnachweis, dazu eine Aufstellung der Fremdbetreuungskosten.
> 
> **Wichtig bei der 20 %-Kürzung:** Das Wiki nennt sie nur für «nur pauschal ausgewiesene Betreuungskosten». Weist die Kita die Verpflegung separat aus oder rechnet reine Betreuung ab, entfällt die Kürzung. Die Kita-Rechnung sollte also geprüft werden. Wäre sie anzuwenden, ergäben sich CHF 24'000 für Kanton und Bund (statt 25'300 / 25'800).
> 
> **Offene Punkte**
> - Das reguläre Formular und die Wegleitung ZH 2026 sind noch nicht publiziert (Stand 09.11.2026). Das Wiki stützt sich auf die Fassung für unterjährige Steuerpflicht (UJ). Ziffer 16.6 und Code 376 sollten am regulären Formular geprüft werden.
> - Der Zweiverdienerabzug (Ziff. 17) ist ein separater Abzug und hat mit der Drittbetreuung nichts zu tun.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## q32

**Frage:** SG 2025: Einfamilienhaus (Baujahr 2010), selbst bewohnt. Pauschalabzug Liegenschaftsunterhalt Kanton und Bund?

**Soll (Referenz):** SG 2025: 20 % des Eigenmietwerts, ohne Altersstaffel (sg-stv__art-29); Bund: Gebäude zu Beginn 2025 über 10 Jahre alt → 20 % (bund-lkv__art-5).

**Antwort des Agenten** (40.0 s · Tools: 10 Aufrufe read, exec):

> **SG 2025, Einfamilienhaus (Baujahr 2010, selbst bewohnt): Pauschale 20 % für Kanton und Bund.** Der Satz ist gleich, die Berechnungsbasis ist verschieden. Status in beiden Fällen ☑️ (agent-geprüft).
> 
> | | Satz 2025 | Basis | Fundstelle |
> |---|---|---|---|
> | **Kanton SG** (Staats-/Gemeindesteuer) | **20 %**, unabhängig vom Gebäudealter | angerechneter Eigenmietwert, d.h. nach dem 30 %-Einschlag (Form. 7, Teil B → «20 % der Erträge (B)») | [Art. 29 StV SG](../steuerwiki/chunks/sg/2025/sg-stv/sg-stv__art-29.md); [WL SG 2025 S. 45](../steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0161.md); [Form. 7 SG 2025 S. 1](../steuerwiki/chunks/sg/2025/sg-form-7-2025/sg-form-7-2025__c0004.md) |
> | **Bund** (DBG) | **20 %**, weil das Gebäude mehr als 10 Jahre alt ist | Brutto-Eigenmietwert, ohne 30 %-Einschlag | [Art. 5 Abs. 2 lit. b LKV](../steuerwiki/chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) |
> 
> **Gebäudealter beim Bund:** Massgebend ist der Beginn der Steuerperiode, also der 1.1.2025. Bei Baujahr 2010 ist das Gebäude dann 14 bis 15 Jahre alt, die 10-%-Stufe (bis 10 Jahre) greift nicht. Gemäss Quick-Seiten gilt für SG keine Altersstaffelung ([Eckwerte SG 2025](../steuerwiki/quick/werte-sg-2025.md), [Eckwerte Bund 2025](../steuerwiki/quick/werte-bund-2025.md)).
> 
> **Rechenbeispiel:** Bei einem Brutto-EMW von 24'000 ergibt sich:
> - Kanton: 24'000 − 30 % = 16'800 angerechneter EMW, davon 20 % = 3'360.
> - Bund: 20 % × 24'000 = 4'800.
> 
> Der Bundesabzug kann also höher ausfallen als der kantonale. Die SG-Steuerbehörde passt die Bundeswerte von Amtes wegen an (Form. 7Z, [Kompakt-Wegleitung SG 2025](../steuerwiki/quick/wegleitung-sg-2025.md)). Der Betrag ist erfunden und dient nur der Illustration.
> 
> **Zu beachten**
> - **Wahlrecht:** Pauschale oder effektive Kosten gelten je Liegenschaft und Steuerperiode. Es ist also nicht nötig, sich für Kanton und Bund auf dieselbe Variante festzulegen. Rechnen Sie beide Varianten und nehmen Sie die höhere.
> - **Wirkung der Pauschale:** Sie deckt alle Unterhalts- und Verwaltungskosten ab, auch Denkmalpflege sowie Energiespar- und Umweltschutzinvestitionen. Daneben gibt es keine Zusatzabzüge (WL SG 2025 S. 45). Beim Bund sind Energiespar- und Umweltinvestitionen nach dem Wiki-Stand nur bei effektiven Kosten separat abziehbar (Thema Liegenschaftsunterhalt).
> - **Voraussetzung:** Die Liegenschaft muss ganz oder vorwiegend Wohnzwecken dienen. Das ist bei Selbstnutzung erfüllt.
> - **Formular:** Form. 7 Teil C. Die Pauschale (C1) geht in Ziff. 15 (Code 716) der Steuererklärung. Bei mehreren Liegenschaften läuft der Übertrag über Form. 7Z.
> 
> **Offen:** Die SG-Weisung StB 44 Nr. 8 (Pauschalabzug) wurde auf den 1.1.2026 überarbeitet. Ihr Inhalt ist im Wiki nicht erfasst. Für 2025 ist das nicht relevant, nur falls Sie später 2026 prüfen.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## q33

**Frage:** ZH 2025: Kind 19 Jahre, in Lehre (Ausbildung). Kinderabzug Kanton und Bund?

**Soll (Referenz):** ZH 2025 Kanton CHF 9'300 (volljährig in Erstausbildung, zh-stg-2025__par-34); Bund CHF 6'800 (bund-dbg-2025__art-35) + CHF 263 Abzug vom Steuerbetrag.

**Antwort des Agenten** (54.9 s · Tools: 13 Aufrufe read, exec):

> Ich habe die Kinderabzüge ZH 2025 (Kanton und Bund) gefunden. Jetzt prüfe ich noch die Voraussetzungen für volljährige Kinder in der Lehre in der Zürcher Steuerbuch-Weisung ZStB 34.1.
> 
> Die 2025er Fassung der Weisung (ZStB 34.1 bis 2025) liegt vor. Ich lese die Randziffern zu volljährigen Kindern in Erstausbildung nach.
> 
> **ZH 2025, Kind 19 Jahre in Lehre: Der volle Kinderabzug ist möglich, unter den unten genannten Bedingungen.**
> 
> | Ebene | Abzug vom Einkommen | Fundstelle (Steuerjahr 2025) | Status |
> |---|---|---|---|
> | **Kanton** (Staats-/Gemeindesteuer) | **CHF 9'300** | § 34 Abs. 1 lit. a StG ZH `^[zh-stg-2025__par-34]` | ☑️ |
> | **Bund** (DBG) | **CHF 6'800** | Art. 35 Abs. 1 lit. a DBG `^[bund-dbg-2025__art-35]` | ☑️ |
> | **Bund**, zusätzlich | **CHF 263** Ermässigung vom Steuerbetrag | Art. 36 Abs. 2bis DBG `^[bund-dbg-2025__art-36-t4]` | ☑️ |
> 
> Der Steuerbetrags-Abzug von CHF 263 gilt nur, wenn das Kind im gleichen Haushalt lebt und Sie seinen Unterhalt zur Hauptsache bestreiten. Er kommt zusätzlich zum Einkommensabzug von CHF 6'800, ersetzt ihn also nicht.
> 
> Das Formular trägt den Abzug in Ziff. 24.1 ein: Code 370 für Kinder im Haushalt, Code 372 für Kinder ausserhalb des Haushalts. Die Wegleitung zeigt dort Kanton 9'300 und Bund 6'800 ([WL ZH 2025 S. 20](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0127.md)). ZH staffelt den Abzug nicht nach Alter, und es gibt keinen Zuschlag für Ausbildung.
> 
> **Bedingungen für ein volljähriges Kind** (Stichtag 31.12.2025, ZStB 34.1 bis 2025, Rz 7–15, [c0004](../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0004.md), [c0005](../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0005.md), [c0007](../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0007.md)):
> - **Berufliche Erstausbildung:** Eine Berufslehre zählt. Die Anstellung zur Ausbildung wird nur mit abgeschlossenem Lehrvertrag anerkannt (Rz 8–9).
> - **Hauptunterhalt:** Sie müssen den Unterhalt zur Hauptsache bestreiten. Das wird angenommen, wenn Ihre Leistungen auf Jahresbasis mindestens dem Kinderabzug entsprechen (Rz 15).
> - **Angewiesen auf Unterstützung:** Das Kind darf seinen Unterhalt nicht aus eigenem Arbeitserwerb oder zumutbar verwertbarem Vermögen selbst bestreiten (Rz 12). Das Lehrlingseinkommen ist daher zu prüfen.
> - **Bund:** Art. 35 DBG verlangt «in beruflicher oder schulischer Ausbildung stehend» und dass Sie für den Unterhalt sorgen. Eine Hauptunterhalts-Schwelle ist dort nicht ausdrücklich genannt.
> 
> **Offene Punkte:**
> - **Einkommensgrenzen:** Die Weisung 2025 nennt keine Zahlen für die Frage, ob das Kind sich selbst erhält. Die Grenzen von CHF 25'000 steuerbarem Einkommen und CHF 100'000 liquidem Vermögen stehen erst in der Fassung ab 2026 (ZStB 34.1, Rz 12). Für 2025 sind sie nicht belegt und dürfen nicht übertragen werden. Bei einem hohen Lehrlingslohn ist das Selbstunterhalts-Kriterium sorgfältig zu prüfen.
> - **Getrennt lebende, geschiedene oder ledige Eltern:** Bei Alimenten für das volljährige Kind geht der Kinderabzug an den zahlenden Elternteil. Die Alimente sind dann nicht mehr abziehbar bzw. nicht mehr steuerbar (Rz 20–23, [c0010](../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0010.md) bis [c0012](../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0012.md)). Bei gemeinsamer Sorge und ohne Alimentenabzug wird der Abzug hälftig geteilt: Kanton CHF 4'650, Bund CHF 3'400.
> 
> **Belege:** Lehrvertrag oder Schulbestätigung, Angaben auf Seite 1 des Formulars (Schule bzw. Lehrfirma, voraussichtlich bis) und bei Bedarf der Nachweis des Hauptunterhalts.
> 
> **Randnotiz:** Der Versicherungsabzug (Ziff. 15) hat einen Zuschlag je Kind von Kanton CHF 1'300 und Bund CHF 700. Das Wiki nennt dort «Kind/unterstützte Person», klärt aber nicht ausdrücklich, ob er für volljährige Kinder in Ausbildung gilt. Das sollten SB/ML prüfen.
> 
> Die fachliche Beurteilung liegt bei SB/ML.

## q34

**Frage:** ZH 2025: Lohnausweis Feld G angekreuzt (Kantine). Welche Verpflegungspauschale gilt und in welche Ziffer des Berufsauslagenformulars?

**Soll (Referenz):** Verbilligte Verpflegung: CHF 7.50 pro Arbeitstag, max. CHF 1'600 pro Jahr (LS 631.33, zh-pauschalierung-berufsauslagen-2025__c0004); Form. 360 Ziff. 2.1 (verbilligt); Bund gleich.

**Antwort des Agenten** (38.4 s · Tools: 11 Aufrufe read, exec):

> Ich habe die ZH-2025-Wegleitung, die Eckwerte und die Chunks geprüft. Hier das Ergebnis.
> 
> **Antwort (ZH, Steuerjahr 2025)**
> 
> Bei Kreuz in Feld G gilt nur der reduzierte Ansatz:
> - **CHF 7.50 pro Arbeitstag, höchstens CHF 1'600 pro Jahr** statt CHF 15 und CHF 3'200.
> - Das gilt auch, wenn die Kantine tatsächlich nicht benützt wird.
> 
> **Ziffer im Berufsauslagenformular**
> - **Formular 360, Ziff. 2.1** («Verpflegung durch den Arbeitgeber verbilligt»), **Code 206** (Folgecode 3211).
> - Ohne Kreuz und bei voller Verpflegung zu Lasten des Arbeitnehmers wäre es Code 208.
> - Rechnung: Code 206 = min(Arbeitstage mit auswärtiger Hauptmahlzeit × 7.50; 1'600).
> - Das Total aus Formular 360 (Ziff. 6) geht in die Steuererklärung in Ziff. 11.1 (Person 1, Code 220) bzw. 11.2 (Person 2, Code 240).
> 
> **Zu beachten**
> - Der Abzug gilt nur, wenn die Arbeitspause die Heimkehr nicht ermöglicht und trotz Verbilligung Mehrkosten entstehen.
> - Er ist nicht kumulierbar mit Ziff. 2.1 «voll» (Code 208), Ziff. 2.2 «Schicht/Nacht» (Code 210) oder einer Mittagsheimfahrt.
> - Kanton und Bund haben dieselben Beträge. Beim Bund gilt zusätzlich: kein Abzug, wenn die Hauptmahlzeiten höchstens CHF 10 kosten (Art. 6 Abs. 3 BKV).
> 
> **Fundstellen und Status (alle ☑️ agent-geprüft)**
> - Beträge 7.50 / 1'600 (Kanton): [WL ZH 2025 S. 13, Ziff. 11/2.1](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0066.md) und [LS 631.33 (bis 2025) Ziff. I/2a](steuerwiki/chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0004.md).
> - Code 206 und Ziff. 2.1: [Formular 360 ZH 2025 S. 1](steuerwiki/chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md).
> - Feld G als Auslöser: [WL Lohnausweis 2026 S. 8–9](steuerwiki/chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md).
> 
> **Offener Punkt**
> Die Feld-G-Regel stammt aus der Lohnausweis-Wegleitung 2026 (Bund/SSK), nicht aus der WL ZH 2025. Letztere nennt nur «Kantine, Personalrestaurant, Barbeitrag, Essensgutscheine». Eine Lohnausweis-Wegleitung für 2025 liegt im Wiki nicht vor. Inhaltlich passt es zusammen, aber das ist die Fachperson zu bestätigen.

## q35

**Frage:** SG 2025: Kapitalbezug Säule 3a CHF 100'000. Wird das mit dem übrigen Einkommen besteuert? Wo deklarieren?

**Soll (Referenz):** Nein – Kapitalleistungen aus Vorsorge werden getrennt vom übrigen Einkommen (separate Jahressteuer) besteuert; SG Formular 1 Ziff. 40.1 (Säule 3a), Total Ziff. 41.

**Antwort des Agenten** (39.4 s · Tools: 11 Aufrufe read, exec):

> **Kurzantwort:** Nein, der Bezug wird nicht mit dem übrigen Einkommen zusammengerechnet. Er wird separat als Kapitalleistung aus Vorsorge besteuert und in der SG-Steuererklärung 2025 unter **Ziff. 40.1 (Säule 3a)** angegeben.
> 
> **Besteuerung (SG 2025)**
> 
> - **Kanton und Gemeinde:** Kapitalleistungen werden gesondert besteuert und unterliegen einer vollen Jahressteuer (Art. 52 Abs. 1 StG SG, `sg-stg-2025__art-52`).
>   - Die einfache Steuer beträgt **2,0 %** für gemeinsam steuerpflichtige Ehegatten und **2,2 %** für die übrigen Steuerpflichtigen (Abs. 2).
>   - Der Ehegattensatz gilt auch für Verwitwete, Getrennte, Geschiedene und Ledige, die mit Kindern oder unterstützungsbedürftigen Personen zusammenleben und deren Unterhalt zur Hauptsache bestreiten (Abs. 3).
>   - Allgemeine Abzüge und Sozialabzüge werden nicht gewährt (Abs. 4).
>   - Der Steueranspruch entsteht im Zeitpunkt des Zuflusses (Abs. 5). Massgebend ist also das Auszahlungsjahr 2025.
> - **Direkte Bundessteuer:** Die Steuer ist ebenfalls gesondert und eine volle Jahressteuer. Sie beträgt **ein Fünftel der Tarife** nach Art. 36 Abs. 1, 2 und 2bis DBG, Sozialabzüge werden nicht gewährt (Art. 38 DBG, `bund-dbg-2025__art-38`).
> 
> **Wo deklarieren**
> 
> - Auf Seite 4 des Formulars 1, **Ziff. 40.1** (Säule 3a), mit der Bescheinigung der Bank bzw. Versicherung über die Auszahlung 2025. Bei mehreren Bezügen im Jahr trägst du den zusammengerechneten Gesamtbetrag ein. Das Total steht in **Ziff. 41 (Code 950)** (WL SG 2025 S. 35, `sg-wl-2025__c0119`; Formular 1 SG 2025 S. 4, `sg-form-1-2025__c0014`).
> - Die Wegleitung bezeichnet die Deklaration als «zu Informationszwecken», sie hat «keine weiteren Steuerfolgen». Die separate Jahressteuer wird trotzdem darauf veranlagt, du musst den Betrag also angeben.
> - **Nicht** in Ziff. 3.2 (Renten) und nicht in Ziff. 6.4 (Kapitalabfindung für wiederkehrende Leistungen) eintragen. Der Betrag fliesst auch nicht ins Total der Einkünfte (Ziff. 7).
> - Die 3a-Guthaben gehören nicht ins Wertschriftenverzeichnis. Das Guthaben per 31.12.2025 ist nach der Auszahlung ohnehin weg.
> 
> **Orientierung (Beispiel, kein Veranlagungsergebnis):** Beim Satz für übrige Steuerpflichtige ergeben sich 100'000 × 2,2 % = CHF 2'200 einfache Steuer. Mit dem Kantonssteuerfuss 2025 von 105 % (`sg-steuerfuesse-2025`) sind das CHF 2'310 Kantonssteuer. Die Gemeindesteuer kommt mit dem Steuerfuss der Wohngemeinde dazu. Dieser ist hier nicht gerechnet, weil die Gemeinde fehlt. Den Bundesanteil habe ich nicht gerechnet. Der Bundestarif ist in `quick/werte-bund-2025.md` zu prüfen.
> 
> **Offen und zu prüfen**
> 
> - Für die Gemeindesteuer brauche ich Wohngemeinde und Zivilstand (2,0 % oder 2,2 %).
> - Die Quellen enthalten nichts zur Zusammenrechnung mehrerer Bezüge aus verschiedenen Jahren. Für den Bezug 2025 spielt das keine Rolle.
> - Der Status der Zuordnung ist ☑️ agent-geprüft, nicht verifiziert durch eine Fachperson. Die fachliche Beurteilung liegt bei SB/ML.

## q36

**Frage:** ZH 2025: Geschiedener Mandant zahlt Unterhaltsbeiträge an die Ex-Frau (CHF 24'000) und für das minderjährige Kind (CHF 12'000). Was ist abziehbar, in welcher Ziffer?

**Soll (Referenz):** Ex-Ehefrau CHF 24'000 voll abziehbar, Ziff. 13.1 (Code 254); Kinderalimente CHF 12'000 abziehbar bis und mit Monat der Volljährigkeit, Ziff. 13.2 (Code 255); Empfänger versteuert; Bund gleich (Art. 33 Abs. 1 lit. c DBG).

**Antwort des Agenten** (34.6 s · Tools: 8 Aufrufe read):

> **ZH 2025: beide Beträge sind voll abziehbar, insgesamt CHF 36'000.** Kanton und Bund behandeln sie gleich, es gibt keine Betragslimite.
> 
> | Betrag | Ziffer / Code | Abzug | Quelle |
> |---|---|---|---|
> | CHF 24'000 an die Ex-Frau | **Ziff. 13.1, Code 254** | CHF 24'000, Staat = Bund | [WL ZH 2025 S. 14](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0075.md): «Für den geschiedenen … Ehegatten persönlich bestimmt … voll abgezogen» |
> | CHF 12'000 für das minderjährige Kind | **Ziff. 13.2, Code 255** | CHF 12'000, Staat = Bund | [WL ZH 2025 S. 15](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0076.md): abziehbar bis und mit dem Monat des 18. Geburtstags |
> 
> Die beiden Beträge gehören in getrennte Zeilen. Das sind Ziff. 13.1 und 13.2 im Formular 2025, Seite 3.
> 
> **Was vor dem Eintrag zu prüfen ist**
> - **Bezahlt und geschuldet:** Abziehbar sind nur die 2025 effektiv bezahlten, familienrechtlich geschuldeten Beträge (Bund: [KS 30 S. 32](steuerwiki/chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0100.md)). Freiwillige Zahlungen sind nicht abziehbar. Die Zahlungsnachweise sind mit der Steuererklärung einzureichen (WL ZH 2025 S. 15).
> - **Zahlungen für die Ex-Frau:** Es zählen nur Beiträge, die für sie persönlich bestimmt sind. Sind in den CHF 24'000 Anteile für das Kind enthalten, gehören diese in Ziff. 13.2.
> - **Alter des Kindes:** Die CHF 12'000 sind nur bis und mit dem Monat abziehbar, in dem das Kind 18 wird. Wird das Kind 2025 volljährig, gilt der Abzug nur für die Monate bis dahin. Ab dem Folgemonat steht stattdessen der Kinderabzug zu (Ziff. 24.1, WL ZH 2025 S. 15).
> - **Kein Kinderabzug daneben:** Wer Kinderalimente abzieht, bekommt für dasselbe Kind keinen Kinderabzug (Kinderabzug Ziff. 24.1; Quick-Seite zur Wegleitung ZH 2025, Ziff. 13.2). Das gilt auch für den halben Abzug. Der Kinderabzug steht dem Elternteil mit alleiniger Sorge oder Obhut zu (ZStB 34.1 Rz 16, [S. 3–4](steuerwiki/chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0008.md)). Hat der Mandant das Kind in der Obhut und zahlt trotzdem Alimente, ist das ein Einzelfall für die Fachperson.
> - **Gegenseite:** Die Ex-Frau versteuert die Beträge in Ziff. 5.1 (Code 160) und 5.2 (Code 161). Name und Adresse der Empfängerin sind anzugeben.
> - **Nicht hierher:** Kapitalabfindungen und Leibrenten gehören nicht in 13.1/13.2 (Ziff. 13.3, Code 256).
> 
> **Status:** Die Zuordnung ist ☑️ agent-geprüft, nicht ✅ von der Fachperson verifiziert. Die Beurteilung des Einzelfalls bleibt bei SB/ML. Gelesen habe ich die Kompakt-Wegleitung ZH 2025, das Themenblatt Unterhaltsbeiträge und die oben verlinkten Chunks. Das Original-PDF habe ich nicht geöffnet.

## q37

**Frage:** TG 2025: Mandant bringt Steuerberatungsrechnung, Kreditkartenabrechnung, Mietvertrag und Motorfahrzeugversicherung. Was davon ist relevant?

**Soll (Referenz):** Steuerberatungsrechnung: nein; Motorfahrzeugversicherung: nein; Kreditkartenabrechnung: bedingt (nur als Nachweis/Schuld per 31.12.); Mietvertrag: bedingt (Wochenaufenthalt/Arbeitszimmer/Adressnachweis) – laut belege-relevanz.

**Antwort des Agenten** (43.2 s · Tools: 14 Aufrufe read, exec, exec):

> Pfad liegt unter `steuerwiki/`.
> 
> **TG 2025: Relevanz der vier Unterlagen**
> 
> Nur die Kreditkartenabrechnung ist bedingt relevant, die anderen drei sind es in der Regel nicht. Stand: ☑️ agent-geprüft, fachliche Beurteilung bei SB/ML. Die Fundstellen sind in den Belegkarten hinterlegt; die TG-Wegleitung enthält zur Steuerberatung keine eigene Aussage (s. u.).
> 
> | Dokument | Relevanz | Begründung / Fundstelle |
> |---|---|---|
> | **Steuerberatungsrechnung** | ❌ nein | Im Privatvermögen sind Steuerberatung und Ausfertigung der Steuererklärung Lebenshaltungskosten (Art. 34 lit. a DBG, `bund-dbg-2025__art-34`). Bund: als Vermögensverwaltungskosten ausdrücklich nicht zulässig (WL 2a 2025 S. 8, `bund-wl-2a-2025__c0057`). Der TG-Pauschalabzug (Form. 2 Code 148) deckt sie nicht. |
> | **Kreditkartenabrechnung** | 🟡 bedingt | Die Abrechnung ist kein Beleg. Sie dient nur als Nachweis, wenn Originalrechnungen fehlen, z. B. für Spenden, Arzt- oder Weiterbildungskosten. Dazu kommt ein Saldovortrag per 31.12.2025 mit Sollzinsen, den Sie in Form. 4.1 A eintragen. Dort gehören Gläubiger mit Adresse, Zinssatz, Saldo per 31.12. und die 2025 belasteten Zinsen hinein (WL TG 2025, Zuordnung Form. 4.1 A). Die Zinsen werden über Form. 4.1 C in Ziff. 11 (Code 290) und der Saldo in Ziff. 34 (Code 466) übernommen. Schuldzinsen sind begrenzt auf Vermögensertrag + Fr. 50'000 (Kanton und Bund). Jahresgebühr und Alltagsumsätze sind nicht abziehbar. |
> | **Mietvertrag** | ❌ nein (Normalfall) | Der Mietzins der selbstbewohnten Wohnung ist nicht abziehbar (Art. 34 lit. a DBG). Relevant wird er nur bei Wochenaufenthalt, Untervermietung oder Mietzinsreduktion als Entgelt (Hauswart). Bei Wochenaufenthalt gilt Form. 4.2 Ziff. 5.1: Zimmer ortsüblich, bei Wohnungen bis 3½ Zimmer Jahresmietzins : (Zimmer + 1) (`tg-wl-2025__c0189`). Bei Untervermietung wird der Nettoertrag unter Ziff. 5.4 steuerbar (`tg-wl-2025__c0083`). Ein Mietvertrag fürs Eigenheim ist nicht relevant. |
> | **Motorfahrzeugversicherung** | ❌ nein (als Police) | Prämien und Verkehrssteuer sind Lebenshaltungskosten. Ein Arbeitsweg mit dem Privatauto wird nur pauschal pro km abgezogen (Form. 4.2 Ziff. 2.3), nicht anhand der Police. Die Police zeigt aber, ob ein Fahrzeug vorhanden ist. Das Fahrzeug muss in Ziff. 30.4 (Code 422) deklariert werden, sofern es nicht geleast ist. Verkehrswert per 31.12.2025: Kaufpreis minus 20 % pro Jahr seit Erwerb, und vor mehr als 5 Jahren gekauft = Fr. 1.– (`tg-wl-2025__c0123`). Dafür brauchen Sie Fahrzeugausweis oder Kaufvertrag. |
> 
> **Rückfragen an den Mandanten**
> - Hat er Saldovortrag oder Sollzinsen auf der Kreditkarte, und welche Spenden oder Arztkosten sollen über die Karte belegt werden?
> - Wohnt er in der Mietwohnung selbst, oder gibt es Wochenaufenthalt oder Untervermietung?
> - Besitzt oder least er das Fahrzeug, und seit wann? Fährt er damit zur Arbeit?
> 
> **Offen / Hinweis**
> - In den TG-Quellen des Wikis steht zur Steuerberatung nichts. Die Aussage stützt sich auf Bund (DBG, WL 2a 2025) und SG/AR, die Beurteilung für TG ist ein Analogieschluss. Fachperson prüfen.
> - Bei Selbständigerwerbenden kann ein geschäftlicher Teil der Beratung Geschäftsaufwand sein. Die Quelle dazu ist im Wiki nicht verifiziert.

## q38

**Frage:** AR 2026: Wie hoch ist der Kinderabzug für ein 10-jähriges Kind? Ist der Wert gesichert?

**Soll (Referenz):** AR 2026: CHF 7'400 laut Anhang 1 StG (indexiert), aber Status STRITTIG (MB 02 / StG-Text nennen andere Beträge; Wegleitung 2026 fehlt) → Fachperson.

**Antwort des Agenten** (44.0 s · Tools: 7 Aufrufe read, exec, exec):

> Ich habe das AR-Wiki zu 2026 durchgesehen. Der Wert ist nicht gesichert.
> 
> **Kinderabzug AR 2026, Kind 10 Jahre (Staats- und Gemeindesteuer)**
> 
> Ein 10-jähriges Kind fällt in die Stufe «nach Vollendung des 4. bis zur Vollendung des 15. Altersjahrs» (Ziff. 23.2). Massgebend ist der Stand am 31.12. (Art. 38 Abs. 2 StG AR).
> 
> Im Wiki stehen zwei Werte, die sich widersprechen:
> 
> | Wert | Quelle |
> |---|---|
> | **CHF 7'400** | StG AR Anhang 1 (indexierte Beträge per 1.1.2024): «Art. 38 Abs. 1 lit. a Ziff. 2 – 7'400» (`ar-stg-anhang-kp__c0001`) |
> | **CHF 7'000** | Gesetzestext StG AR Art. 38 Abs. 1 lit. a Ziff. 2 (`ar-stg__art-38-t1`) und MB AR 02 Ziff. 2, Stand 18.08.2026 (`ar-mb-02__c0002`) |
> 
> - **Status: ⚠️ strittig.** Das Wiki führt den Wert nicht als verifiziert, und die Fachperson muss entscheiden.
> - **Was für 7'400 spricht:** Art. 39a StG verlangt, die Abzüge in Art. 38 Abs. 1 für die kalte Progression anzupassen, und Anhang 1 weist die angepassten Beträge aus. Die WL AR 2025 (Kurzübersicht Ziff. 23.2, `ar-wl-2025__c0005`) nennt für 2025 ebenfalls 7'400. Das Wiki hält 7'400 deshalb für «wahrscheinlich».
> - **Was dagegen spricht:** Das Merkblatt von August 2026 nennt 7'000. Das sind die nicht indexierten Gesetzeszahlen, also vermutlich nur eine Wiederholung des Gesetzestexts. Das ist meine Einschätzung und nicht belegt.
> - **Es fehlen** die Wegleitung und das Formular AR 2026. Sie sind laut Wiki noch nicht publiziert (Stand 09.11.2026). Ich habe auch keine Quelle gefunden, die eine weitere Indexierung für 2026 bestätigt oder ausschliesst.
> - **7'400 ist deshalb mein Arbeitswert unter Vorbehalt, kein bestätigter.** Das Wiki bezieht den 2025er Wert für 2026 nur über den Anhang und nicht über eine 2026er Quelle.
> 
> **Direkte Bundessteuer (getrennt)**
> 
> - Der Kinderabzug beträgt einheitlich **CHF 6'800** ohne Altersstaffelung (Art. 35 Abs. 1 lit. a DBG, `bund-dbg-2026__art-35`, 2026, ☑️ agent-geprüft).
> - Dazu kommt ein Abzug vom Steuerbetrag von **CHF 263** pro Kind (Art. 36 Abs. 2bis DBG, `bund-dbg-2026__art-36-t4`, ☑️).
> 
> Die Fachbeurteilung (SB/ML) bleibt bei Ihnen. Sinnvoll wäre, bei der AR-Steuerverwaltung nachzufragen oder die Wegleitung 2026 abzuwarten, bevor der Wert fest verwendet wird.

## q39

**Frage:** Welche Vermögenssteuer-Freibeträge (Sozialabzüge) gelten 2025 in ZH für Alleinstehende und Verheiratete?

**Soll (Referenz):** ZH kennt keine Vermögens-Sozialabzüge, sondern Tarifstufen mit 0 ‰: Grundtarif erste CHF 80'000, Verheiratetentarif erste CHF 159'000 (zh-stg-2025__par-47); kein Betrag pro Kind.

**Antwort des Agenten** (32.2 s · Tools: 7 Aufrufe read, exec):

> **ZH, Steuerjahr 2025, Staats- und Gemeindesteuer.** ZH kennt bei der Vermögenssteuer keinen Sozialabzug im eigentlichen Sinn. Der Freibetrag steckt in der 0‰-Stufe des Tarifs (§ 47 StG ZH).
> 
> | Tarif | Steuerfreies Vermögen | Fundstelle |
> |---|---|---|
> | Grundtarif (Alleinstehende) | **CHF 80'000** (0‰ für die ersten Fr. 80 000) | § 47 Abs. 1 StG ZH, `zh-stg-2025__par-47-t1` (S. 24–25) |
> | Verheiratetentarif | **CHF 159'000** (0‰ für die ersten Fr. 159 000) | § 47 Abs. 2 StG ZH, `zh-stg-2025__par-47-t2` (S. 24–25) |
> 
> Beide Werte sind ☑️ agent-geprüft, also noch nicht von der Fachperson verifiziert. Die Stufe 0‰ wird auch von ZStB 48.1 (VKP ab 2024) bestätigt (`zh-vkp-2024-zstb__c0010` und `__c0011`).
> 
> **Wer den Verheiratetentarif bekommt** (§ 47 Abs. 2 StG):
> - Ehegatten in rechtlich und tatsächlich ungetrennter Ehe.
> - Verwitwete, getrennt lebende, geschiedene und ledige Steuerpflichtige, die mit Kindern im Sinn von § 34 Abs. 1 lit. a zusammenleben.
> - Nicht gemeinsam besteuerte Eltern mit gemeinsamer elterlicher Sorge, denen der Kinderabzug je zur Hälfte zusteht: Den Verheiratetentarif erhält der Elternteil, der den Unterhalt des Kindes aus seinen versteuerten Einkünften zur Hauptsache bestreitet (Abs. 2bis).
> - Massgebend sind die Verhältnisse am Ende der Steuerperiode oder der Steuerpflicht (Abs. 3).
> 
> **Weitere Punkte:**
> - **Kein Kinderabzug beim Vermögen:** Das Wiki hat dazu keinen Wert, § 47 enthält nur Tarifstufen (Status: n/a).
> - **Bund:** Die direkte Bundessteuer erhebt keine Vermögenssteuer, es gibt also keine Bundesspalte.
> - **Weitere Stufen:** Diese gehören zum Tarif und sind keine Freibeträge. Grundtarif: ½‰ für die weiteren Fr. 238 000, danach 1‰ für die weiteren Fr. 399 000 usw. bis 3‰ ab Fr. 3 262 000. Verheiratetentarif: ½‰ für die weiteren Fr. 239 000 bis 3‰ ab Fr. 3 342 000.
> - **Steuerfuss:** Die Beträge sind einfache Staatssteuer. Der Steuerfuss Kanton (98 %, § 2 StG) und der Gemeindesteuerfuss kommen noch dazu.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## q40

**Frage:** Alleinstehende TG 2026, Nettolohn 90'000, ÖV-Abo 2'400, Säule 3a 7'258, Krankenkasse 5'500. Erstelle die Abzüge (Berufskosten, 3a, Versicherungsabzug) Kanton und Bund mit Fundstellen und Status.

**Soll (Referenz):** TG 2026 (Kanton/Bund): Fahrkosten 2'400 (Max. 6'000 / 3'300); übrige Berufskosten 3 % von 90'000 = 2'700 (Min. 2'000, Max. 4'000, beide Ebenen); Säule 3a 7'258 (TG 🟡 extrahiert, Bund ☑️); Versicherungsabzug TG max. 3'500 → 3'500, Bund max. 1'800 → 1'800 (Prämien 5'500 übersteigen beide Maxima).

**Antwort des Agenten** (55.7 s · Tools: 12 Aufrufe read, exec):

> Ich habe die TG-2026-Eckwerte und die Bundeswerte gelesen. Jetzt prüfe ich noch die Ziffer 2.1 (ÖV-Abo) im Formular 4.2, dann rechne ich alles zusammen.
> 
> **Fall:** Alleinstehend, Kanton TG, Steuerjahr 2026. Basis: Nettolohn CHF 90'000 (angenommen als Lohnausweis Ziff. 11), ÖV-Abo CHF 2'400, Säule 3a CHF 7'258, Krankenkasse CHF 5'500.
> 
> ## Abzüge
> 
> | Position | Ziffer / Form. | Kanton (Staat/Gde.) | Bund (DBG) | Rechnung |
> |---|---|---|---|---|
> | Fahrkosten ÖV-Abo | 4.2 Ziff. 2.1 → 2.5 (Code 206) | **2'400** | **2'400** | 2'400 liegt unter den Maxima von 6'000 (Kanton) und 3'300 (Bund) |
> | Übrige Berufskosten, Pauschale | 4.2 Ziff. 4 | **2'700** | **2'700** | 3 % × 90'000 = 2'700, innerhalb Min. 2'000 / Max. 4'000 |
> | **Berufskosten total** | 4.2 Ziff. 7 → Hauptformular Ziff. 10.1 (Code 240) | **5'100** | **5'100** | 2'400 + 2'700 |
> | Säule 3a | Ziff. 13.1 | **7'258** | **7'258** | Einzahlung entspricht dem Maximum mit 2. Säule |
> | Versicherungsabzug | Form. 5.2 → Ziff. 14 (Code 330) | **3'500** | **1'800** | Kanton min(5'500; 3'500), Bund min(5'500; 1'800) |
> 
> Beim Versicherungsabzug fallen 2'000 (Kanton) bzw. 3'700 (Bund) der Prämien über das Maximum und bleiben ohne Wirkung.
> 
> ## Fundstellen und Status
> 
> | Wert | Fundstelle | Status |
> |---|---|---|
> | Fahrkosten-Plafond Kanton 6'000 / Bund 3'300 | [WL TG 2026 S. 37–38](steuerwiki/chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0176.md); Bund: [DBG Art. 26 Abs. 1 lit. a](steuerwiki/chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-26.md) | ☑️ |
> | Übrige Berufskosten 3 %, min. 2'000, max. 4'000 (Kanton) | [BKV TG § 4a](steuerwiki/chunks/tg/2025/tg-bkv/tg-bkv__par-4a.md) (gilt 2025/2026) | ☑️ |
> | Übrige Berufskosten (Bund) | [RS 2-215 S. 2](steuerwiki/chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0006.md); [BKV Anhang](steuerwiki/chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__anhang-1.md); [DBG Art. 26 Abs. 2](steuerwiki/chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-26.md) | ☑️ |
> | 3a mit 2. Säule 7'258 (Kanton) | [WL TG 2026 S. 20](steuerwiki/chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0089.md) | ☑️ |
> | 3a mit 2. Säule 7'258 (Bund) | [BSV Masszahlen 25/26](steuerwiki/chunks/bund/2025/bund-bsv-masszahlen-2025-2026/bund-bsv-masszahlen-2025-2026__c0003.md) | ☑️ |
> | Versicherungsabzug Kanton 3'500 | [WL TG 2026 S. 44](steuerwiki/chunks/tg/2026/tg-wl-2026/tg-wl-2026__c0209.md); [StG TG § 34 Ziff. 9](steuerwiki/chunks/tg/2025/tg-stg/tg-stg__par-34-t3.md) | ☑️ |
> | Versicherungsabzug Bund 1'800 | [DBG Art. 33 Abs. 1 lit. g](steuerwiki/chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t2.md); [RS 2-215 S. 2](steuerwiki/chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0006.md) | ☑️ |
> 
> Alle Werte sind agent-geprüft (☑️). Keiner ist von der Fachperson verifiziert (✅). Der Status ☑️ habe ich aus den Eckwert-Seiten übernommen und die Chunks stichprobenartig gegengelesen. Die Chunks für Berufskosten Bund und für 3a Bund habe ich nicht alle einzeln geöffnet. Die Wegleitung TG 2026 ist laut Quick-Index publiziert (Formular-Ziffern, Stand 09.11.2026), das Hauptformular selbst habe ich nicht gegen das Original-PDF geprüft.
> 
> ## Annahmen und offene Punkte
> 
> 1. **Pensionskasse:** Ich gehe von einem Anschluss an die 2. Säule aus. Das Maximum 7'258 und der Versicherungsabzug 1'800 bzw. 3'500 gelten so (WL TG 2026 S. 20). Ohne PK-Anschluss wären 3a bis 20 % des Erwerbseinkommens (max. 36'288) möglich. Das wäre mehr als die geleisteten 7'258. Der Bundesabzug würde dann 2'700 statt 1'800 betragen, wenn überhaupt keine 3a-Beiträge geleistet würden. Bei bezahltem 3a gilt aber weiterhin 1'800.
> 2. **Krankenkasse 5'500:** Gemeint ist die Nettoprämie nach Abzug der Prämienverbilligung (IPV). Die KK-Jahresbestätigung kommt in Form. 5.2 A Ziff. 1. Weitere Versicherungsprämien oder Sparzinsen ändern nichts, da das Maximum schon überschritten ist.
> 3. **Nettolohn 90'000:** Ich habe ihn als Lohnausweis Ziff. 11 angenommen. Ist er anders definiert, ändert sich die 3 %-Pauschale.
> 4. **ÖV-Abo:** Das Abo wird nur anerkannt, wenn im Lohnausweis Feld F nicht angekreuzt ist (kein Geschäftsfahrzeug), und bei einer Distanz ab ca. 1 km. Die Abo-Quittung ist beizulegen.
> 5. **Nicht gerechnet, mangels Angaben:** Verpflegungsmehrkosten (CHF 15 pro Arbeitstag, max. 3'200), effektive übrige Berufskosten statt Pauschale, Weiterbildung und Spenden. Verpflegung wäre bei einem Arbeitsweg mit Kantine oder auswärts Essen relevant.
> 6. **Offene Wiki-Punkte, die diesen Fall nicht betreffen:** Das Wiki führt einen Streit zum Bund-Autoansatz (0.70 vs. 0.75 pro km), und der Homeoffice-Abzug ist offen. Beides spielt hier keine Rolle, da ÖV statt Auto.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson (SB/ML).

