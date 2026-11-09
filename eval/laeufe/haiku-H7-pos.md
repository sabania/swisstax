# OpenClaw-Testlauf: positionstest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 10 · Lauf: 2026-11-09 15:41
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## p01

**Frage:** ZH 2025: Ledige unselbständig erwerbende Person, Nettolohn gemäss Lohnausweis CHF 92'000. Sie fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 23 km einfach, 2 Fahrten pro Tag, 220 Arbeitstage. Übrige Berufskosten werden pauschal geltend gemacht (keine Verpflegungskosten). Welche Positionen/Codes im Formular «Berufsauslagen» und welcher Betrag geht in Ziffer 11.1 – Staatssteuer und Bundessteuer getrennt?

**Soll (Referenz):** Formular 360 «Berufsauslagen» (Person 1), Begründung Privatauto Code 2042 (Zeitersparnis über 1 Stunde) ankreuzen. Ziff. 1.3 Auto (CHF 0.70/km, Staat und Bund gleich): 23 km x 2 Fahrten x 220 Tage = 10'120 km x 0.70 = CHF 7'084 (Code 204). Zwischentotal Fahrkosten Code 205: Staat max. CHF 5'200 -> 5'200; Bund max. CHF 3'300 -> 3'300. Ziff. 3 übrige Berufskosten pauschal Code 212: 3% von 92'000 = CHF 2'760 (innerhalb mind. 2'000 / höchstens 4'000; Staat und Bund gleich, vgl. BKV-Anhang). Total Berufsauslagen Code 220 -> Steuererklärung Seite 3, Ziff. 11.1: Staat 5'200 + 2'760 = CHF 7'960; Bund 3'300 + 2'760 = CHF 6'060.

**Antwort des Agenten** (32.7 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **Ziffer 11.1 (Berufsauslagen Person 1, Code 220):**
> 
> | | Staatssteuer | Bundessteuer |
> |---|---|---|
> | Fahrkosten Auto (Code 204, Zwischentotal 205) | 5'200 | 3'300 |
> | Übrige Berufskosten, Pauschale (Code 212) | 2'760 | 2'760 |
> | **Total → Ziff. 11.1 (Code 220)** | **7'960** | **6'060** |
> 
> **Formular «Berufsauslagen» (Form. 360), Person 1:**
> - **Code 204**: Auto-Fahrkosten. Begründung über 1 Stunde Zeitersparnis, Begründung unter Ziff. 7.
> - **Code 205**: Zwischentotal Fahrkosten (ÖV-Abo 201, Velo 202 und Auto 204 zusammen), gedeckelt.
> - **Code 212**: Übrige Berufskosten pauschal, 3 % des Nettolohns, Minimum 2'000, Maximum 4'000.
> - **Code 220**: Total, übertragen in Ziff. 11.1.
> 
> **Rechnung:**
> - Km: 23 km × 2 Fahrten × 220 Tage = 10'120 km. Das liegt unter der Grenze von 240 Arbeitstagen.
> - Auto: 10'120 km × CHF 0.70 = CHF 7'084. Das ist höher als der Plafond, deshalb wird gekürzt:
>   - Staatssteuer: Plafond CHF 5'200, also 5'200 (CHF 1'884 nicht abziehbar).
>   - Bundessteuer: Plafond CHF 3'300, also 3'300 (CHF 3'784 nicht abziehbar).
> - Übrige Kosten: 3 % von CHF 92'000 = 2'760, liegt zwischen 2'000 und 4'000. Der Betrag ist in beiden Steuern gleich.
> 
> **Hinweise:**
> - Die Pauschale 3 % rechnet mit dem Nettolohn gemäss Lohnausweis (92'000), wie du ihn angegeben hast.
> - Die Auto-Pauschale ist nur ausnahmsweise zulässig, deshalb muss die Begründung (Zeitersparnis über 1 Stunde, kein zumutbarer ÖV) beiliegen.
> - Die Fundstellen sind agent-geprüft (☑️), die fachliche Abnahme steht noch aus.

## p02

**Frage:** ZH 2025: Verheiratetes Paar, beide in einer Pensionskasse (2. Säule) versichert, zwei minderjährige Kinder mit Kinderabzug. Bezahlte Krankenkassenprämien 2025 (bereits netto nach individueller Prämienverbilligung) CHF 15'600, Sparzinsen gemäss Wertschriftenverzeichnis CHF 150. Wie wird das Formular «Versicherungsprämien» ausgefüllt und welcher Abzug kommt in Ziffer 15 (Staat / Bund)?

**Soll (Referenz):** Formular 365 «Versicherungsprämien»: Teil A: Code 601 Krankenversicherungsprämien 15'600 + Code 604 Sparzinsen 150 -> Total (A) Code 606 = CHF 15'750. Teil B (Maximum): Verheiratete mit Beiträgen an 2. Säule/3a Code 611: Staat 5'800 / Bund 3'700; Kinderzuschlag Code 613: Staat 2 x 1'300 = 2'600 / Bund 2 x 700 = 1'400 -> Total (B) Code 616: Staat CHF 8'400 / Bund CHF 5'100. Teil C Code 270 = der niedrigere Betrag von (A) und (B): Staat CHF 8'400, Bund CHF 5'100 -> Steuererklärung Seite 3, Ziff. 15 (Spalten Staatssteuer/Bundessteuer).

**Antwort des Agenten** (31.2 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__formular, steuerwiki__rechne):

> **Ziffer 15 (Code 270, Versicherungsprämien und Zinsen von Sparkapitalien):**
> 
> - **Staatssteuer (Kanton): CHF 8'400**
> - **Bundessteuer: CHF 5'100**
> 
> Die Ziffer nimmt den tieferen Wert aus Teil A (bezahlte Prämien und Sparzinsen) und Teil B (Maximalabzug). Teil A ist hier höher, deshalb gilt Teil B.
> 
> **Ausfüllen von Form. 365 (Hilfsblatt Versicherungsprämien), Teil A**
> 
> | Code | Position | Betrag |
> |---|---|---|
> | 601 | Private Krankenversicherungsprämien, bezahlt, nach IPV-Verrechnung | 15'600 |
> | 602 | Unfallversicherung | – |
> | 603 | Lebens-/Rentenversicherung | – |
> | 604 | Zinsen von Sparkapitalien (aus Wertschriftenverzeichnis) | 150 |
> | 605 | Abzüglich erhaltene Prämienverbilligung | – |
> | 606 | Total (A) = 601–604 − 605 | 15'750 |
> 
> Die IPV ist bereits in den 15'600 verrechnet. Sie darf in 605 nicht noch einmal abgezogen werden (kein Doppelabzug).
> 
> **Teil B (Maximalabzug)**
> 
> - Verheiratet, mit 2. Säule: Kanton 5'800 | Bund 3'700 (Code 611)
> - Zwei Kinder à 1'300 Kanton bzw. 700 Bund (Code 613–615): Kanton 2'600 | Bund 1'400
> - Total B: Kanton 8'400 | Bund 5'100
> 
> Die Pensionskasse ist ein Grund, den Wert «mit 2. Säule» zu wählen. Der höhere Wert «ohne 2./3a» (8'700 / 5'550) gilt nur, wenn weder Sie noch der Arbeitgeber in 2. Säule oder 3a einzahlten.
> 
> **Hinweise**
> 
> - Die Beiträge an die Pensionskasse selbst gehören nicht in Ziffer 15, sondern in Ziffer 16.1 (Code 280).
> - Die Sparzinsen von CHF 150 werden in Ziffer 4.1 als Ertrag versteuert. Der Abzug in Ziffer 15 ist ein separater Posten.
> - Einzureichen: Das Formular «Versicherungsprämien» ist beizulegen, wenn es verlangt wird. Die Krankenkassen-Prämienabrechnung 2025 (mit Verrechnung der IPV) sollten Sie bereithalten.
> 
> Quellen: zh-form-365-2025__c0001 (Codes 601–606), zh-form-300-2025__c0008 (Ziff. 15, Code 270), zh-wl-2025__c0082 und zh-wl-2025__c0084 (Limiten, IPV). Status: agent-geprüft, Abnahme offen. Die Fachbeurteilung liegt bei der Fachperson.

## p03

**Frage:** ZH 2025: Alleinstehende Mandantin unterstützt ihre erwerbsunfähige Mutter (eigener Haushalt, keine Alimente, kein Kinderabzug) nachweislich mit CHF 5'000 im Jahr 2025. In welcher Ziffer wird das geltend gemacht, welcher Abzug gilt bei der Staatssteuer und bei der Bundessteuer, und wirkt sich das auf den Versicherungsprämienabzug aus?

**Soll (Referenz):** Ziff. 24.2 «Abzug für unterstützte Personen» (Code 374); Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der Unterstützung beilegen. Staat: Voraussetzung Unterstützungsleistung mindestens CHF 2'800 -> 5'000 erfüllt -> Abzug CHF 2'800. Bund: Voraussetzung Unterstützungsleistung mindestens CHF 6'800 (Art. 35 Abs. 1 lit. b DBG) -> 5'000 < 6'800 -> kein Unterstützungsabzug (CHF 0). Folge im Formular 365 Teil B.3: Staat zusätzlicher Abzug CHF 1'300 für die unterstützungsbedürftige Person (Code 614); Bund kein Zuschlag von CHF 700 (Code 615), da kein Unterstützungsabzug zusteht.

**Antwort des Agenten** (42.6 s · Tools: 7 Aufrufe steuerwiki__position, steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurz:** Ziffer 24.2 (Code 374), Staatssteuer CHF 2'800, Bundessteuer **CHF 0**. Der Versicherungsabzug steigt nur bei der Staatssteuer, um CHF 1'300.
> 
> **1. Ziffer im Formular ZH 2025**
> - Ziff. 24.2 «Abzug für unterstützte Personen», Code 374 (☑️ agent-geprüft, Abnahme offen).
> - Auf Seite 1 (Personalien) ist zusätzlich pro unterstützte Person der Unterstützungsbetrag pro Jahr anzugeben.
> - Beilegen: Bestätigung der unterstützten Person mit Art, Zeitpunkt und Höhe der Unterstützung. Zahlungsbelege nur auf Verlangen.
> 
> **2. Staatssteuer (ZH)**
> - § 34 Abs. 1 lit. b StG ZH: Unterstützungsabzug **CHF 2'800**, wenn die Unterstützung mindestens in dieser Höhe erfolgt (Fundstelle: zh-stg-2025__par-34).
> - 5'000 ≥ 2'800 → **Abzug CHF 2'800**.
> 
> **3. Bundessteuer**
> - Art. 35 Abs. 1 lit. b DBG: Unterstützungsabzug **CHF 6'800**. Die Leistungen müssen mindestens in dieser Höhe erfolgen.
> - KS 30 Ziff. 11: Wird weniger als der festgelegte Abzug geleistet, **entfällt der Sozialabzug** (bund-ks-30__c0065). Es gibt also keine anteilige Kürzung.
> - 5'000 < 6'800 → **Abzug CHF 0** in der Bundesspalte.
> 
> **4. Auswirkung auf den Versicherungsprämienabzug**
> Der Grundabzug für Versicherungsprämien bleibt gleich. Es kommt nur ein Zuschlag pro unterstützter Person dazu, und dieser hängt am jeweiligen Unterstützungsabzug:
> - **Staat:** +CHF 1'300 (Form. 365, Code 614), weil der Staats-Unterstützungsabzug geltend gemacht werden kann (zh-stg-2025__par-31-t2).
>   - Alleinstehend mit PK-Beiträgen: 2'900 + 1'300 = **4'200**.
>   - Alleinstehend ohne PK-Beiträge: 4'350 + 1'300 = **5'650**.
> - **Bund:** kein Zuschlag, weil der Bundes-Unterstützungsabzug entfällt. Der Zuschlag von CHF 700 (Code 615) setzt einen Bundesabzug nach Art. 35 Abs. 1 lit. a/b DBG voraus (bund-dbg-2025__art-33-t5). Grundbetrag alleinstehend: CHF 1'800 mit / 2'700 ohne Vorsorge.
> 
> **Vor der Abgabe prüfen**
> - **Bedürftigkeit der Mutter** (ZStB 34.1, ZH): Einkommen unter CHF 15'000 und Vermögen unter CHF 50'000. Die Angaben dazu fehlen im Sachverhalt.
> - **Erwerbsunfähigkeit** der Mutter nachweisen (Arztzeugnis oder IV-Verfügung). Ohne Nachweis entfällt der Abzug.
> - Die Ausschlüsse (Ehegatte, Kind mit Kinderabzug, Alimente) treffen hier nicht zu.
> - Die Werte sind agent-geprüft, die Abnahme durch eine Fachperson steht noch aus.

## p04

**Frage:** SG 2025: Nettoeinkommen gemäss Ziffer 20 CHF 80'000. Arzt- und Zahnarztrechnungen 2025 brutto CHF 6'200, davon von der Krankenkasse vergütet CHF 1'700. Wo werden die Kosten deklariert und wie hoch ist der Abzug für die Staats- und Gemeindesteuern bzw. für die direkte Bundessteuer (Annahme: massgebendes Nettoeinkommen Bund ebenfalls CHF 80'000)?

**Soll (Referenz):** Formular 6 (Rückseite «Krankheits-, Unfall- und behinderungsbedingte Kosten»): Bruttobetrag 6'200 abzüglich Beiträge Dritter 1'700 = selbst getragene Kosten CHF 4'500 -> Steuererklärung Seite 3, Vorkolonne Ziff. 21.1 (Code 650). Kanton SG: Selbstbehalt 2% des Nettoeinkommens (Ziff. 20) = 2% x 80'000 = 1'600 (Code 238) -> Abzug Code 240 = CHF 2'900. Bund: Selbstbehalt 5% (Art. 33 Abs. 1 lit. h DBG; Merkblatt 32) = 4'000 -> Abzug CHF 500. Das SG-Formular hat nur eine Spalte; die Abweichung für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor.

**Antwort des Agenten** (29.3 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **Deklaration:** Ziffer 21.1 «Krankheits- und Unfallkosten» der SG-Steuererklärung 2025 (Formular 1). Die Einzelrechnungen trägst du im Hilfsblatt Formular 6 (Rückseite) mit dem Bruttobetrag ein. Die Krankenkassenvergütung wird dort als Beitrag Dritter abgezogen. Bei der direkten Bundessteuer gibt es im Formular keine separate Spalte; die Steuerbehörde nimmt die Anpassung automatisch vor (Merkblatt 32).
> 
> **Berechnung** (Ziff. 21.1, Vorkolonne Code 650, Abzug Code 240):
> 
> | Schritt | Betrag (CHF) |
> |---|---|
> | Arzt- und Zahnarztrechnungen brutto | 6'200 |
> | ./. Vergütung Krankenkasse (Beitrag Dritter) | −1'700 |
> | **Vorkolonne (Nettobetrag selbst getragen)** | **4'500** |
> 
> | | Selbstbehalt (× Nettoeinkommen 80'000) | Abzugsfähig |
> |---|---|---|
> | **Staats- und Gemeindesteuern SG** | 2 % = 1'600 | 4'500 − 1'600 = **2'900** |
> | **Direkte Bundessteuer** | 5 % = 4'000 | 4'500 − 4'000 = **500** |
> 
> Die Formel lautet: Abzug = max(0; Vorkolonne − Selbstbehalt). Die Selbstbehalte gelten nach Ihrer Annahme, dass das massgebende Nettoeinkommen für den Bund ebenfalls 80'000 beträgt. Den Bund-Satz habe ich aus dem Wiki übernommen; die Rechnung selbst habe ich von Hand nachgerechnet, weil das Rechen-Tool die Funktion max() mit benannten Variablen nicht akzeptiert hat.
> 
> **Status der Angaben:** Die Werte für SG (2 %, Ziff. 21.1, Form. 6) sind ☑️ agent-geprüft: Die Fundstellen wurden geprüft, die Abnahme steht aber noch aus. Den Bund-Satz von 5 % habe ich ebenfalls als ☑️ eingestuft.
> 
> **Zu beachten:**
> - Bei einem Verweis auf den Krankenkassen-Zusammenzug musst du eine Detailaufstellung inkl. Leistungsübersicht beilegen (Form. 6).
> - Krankenkassenprämien gehören nicht hierher, sondern in Ziff. 14.
> - Behinderungsbedingte Kosten gehören in Ziff. 21.2 und haben keinen Selbstbehalt.
> - Die Fachbeurteilung und die Abnahme bleiben bei der Fachperson.

## p05

**Frage:** SG 2025: Mandant gewinnt im Swiss Lotto (interkantonal durchgeführte Lotterie = Grossspiel) einen Einzelgewinn von CHF 1'500'000. Wo wird der Gewinn deklariert, welcher Teil ist steuerbar und welche Einsatzkosten sind abziehbar – Kanton und Bund getrennt?

**Soll (Referenz):** Deklaration im Wertschriften- und Guthabenverzeichnis (Formular 2), Spalte A (Bargewinn aus inländischer Lotterie, verrechnungssteuerpflichtig); Übertrag Ziff. 4.1 (Code 146). Kanton SG: Einzelgewinne aus Grossspielen steuerbar, soweit > Fr. 1'069'800 -> 1'500'000 - 1'069'800 = CHF 430'200 steuerbar; Einsatzkosten unter Ziff. 16.1 (Code 220): 5%, höchstens Fr. 5'400 -> CHF 5'400; netto CHF 424'800. Bund: steuerfrei bis CHF 1'070'400 (Art. 24 lit. ibis DBG) -> steuerbar CHF 429'600; Einsatzkosten 5%, höchstens CHF 5'400 (Art. 33 Abs. 4 DBG) -> CHF 5'400; netto CHF 424'200. (Der Höchstbetrag 5'400 greift unabhängig davon, ob 5% vom Gesamt- oder vom steuerbaren Gewinn gerechnet werden.)

**Antwort des Agenten** (54.1 s · Tools: 15 Aufrufe steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne, steuerwiki__position):

> **Ergebnis (Steuerjahr 2025, Wohnsitz SG am 31.12. angenommen; Gewinn im Jahr 2025 erzielt)**
> 
> | | Kanton SG | Bund (direkte Bundessteuer) |
> |---|---|---|
> | Steuerfreie Grenze pro Einzelgewinn | CHF 1'069'800 | CHF 1'070'400 |
> | Steuerbarer Gewinn (1'500'000 − Grenze) | **CHF 430'200** | **CHF 429'600** |
> | Einsatzkosten | 5 % des steuerbaren Gewinns, max. **CHF 5'400** (5 % = 21'510 → gekappt) | 5 % des steuerbaren Gewinns, max. **CHF 5'400** (5 % = 21'480 → gekappt) |
> | Steuerbarer Betrag nach Abzug | **CHF 424'800** | **CHF 424'200** |
> 
> **Kanton SG**
> - **Steuerbefreiung:** Art. 37 Bst. o StG SG, Grossspiele (Lotterien, interkantonal durchgeführt) bis CHF 1'069'800 steuerfrei; nur der Betrag darüber ist steuerbar (WL SG 2025 Ziff. 4, `sg-wl-2025__c0064`, `sg-stg-2025__art-37-t3`).
> - **Einsatzkosten:** Art. 45 Abs. 3 StG SG: 5 %, max. CHF 5'400, auf den steuerbaren Gewinnen (`sg-stg-2025__art-45-t5`, `sg-wl-2025__c0090`, Ziff. 16.1).
> - **Deklaration:** Formular 2 Ziff. 4.1 (Wertschriften- und Guthabenverzeichnis, Code 146), Lotto-Bescheinigung als Beilage. Übertrag auf Hauptformular Seite 4 Ziff. 30.1 (`sg-wl-2025__c0134`, Position-Abfrage). Im Wiki nicht eindeutig belegt: ob der Gesamtgewinn oder nur der steuerbare Teil in die Zeile eingetragen wird. Das bitte bei der Fachperson bzw. im Merkblatt prüfen.
> - **Status:** Fundstellen geprüft, Abnahme offen (☑️).
> 
> **Bund**
> - **Steuerbefreiung:** Art. 24 Bst. ibis DBG, Grossspiele bis CHF 1'070'400 steuerfrei; Überschuss steuerbar (WL 2a 2025 `bund-wl-2a-2025__c0024`, RS 2-211 `bund-rs-2-211__c0019`).
> - **Einsatzkosten:** Art. 33 Abs. 4 DBG (VKP Art. 3 Abs. 6): 5 %, max. CHF 5'400 (`bund-rs-2-211__c0017`). Die Wegleitung nennt für Grossspiele zusätzlich, dass die Einsätze höchstens bis zur Höhe der im selben Jahr erzielten Gewinne abgezogen werden (`bund-wl-2a-2025__c0025`). Diese Obergrenze greift hier nicht.
> - **Deklaration:** Formular 2 Ziff. 4 (Lotterie- und Totogewinne). Im Wiki nicht belegt: die genaue Zeile für den Bund-Einsatzkostenabzug im Hauptformular. Für SG gibt es keinen separaten Bundesbetrag; die Abweichung nimmt die Steuerbehörde automatisch vor (Merkblatt 32, `sg-wl-2025__c0173`).
> 
> **Hinweise**
> - Die Einsatzkosten werden auf die Gesamtsumme oder den steuerbaren Teil berechnet; in beiden Fällen ist das Ergebnis gleich, weil der Deckel von CHF 5'400 greift.
> - Die Online-Spielbank-Regel mit effektiven Einsätzen (SG max. 26'700, Bund max. 26'800) gilt hier nicht, da Swiss Lotto ein interkantonales Grossspiel ist.
> - Die Steuer auf die steuerbaren Beträge (SG 424'800, Bund 424'200) berechnet sich nach dem jeweiligen Tarif und ist hier nicht enthalten; die Wiki-Quellen liefern dafür keine Tarifwerte.

## p06

**Frage:** SG 2025: Ehepaar mit zwei Kindern, für deren Unterhalt es zur Hauptsache aufkommt: Kind A ist 2-jährig (noch nicht schulpflichtig), Kind B ist 20 und studiert. Für Kind B selbst getragene Ausbildungskosten (Semestergebühren, Bücher, ÖV zum Studienort) CHF 9'500, erhaltenes Stipendium CHF 1'000. Welche Ziffern/Codes und welche Beträge – Kanton und Bund?

**Soll (Referenz):** Kanton SG (Steuererklärung Seite 3, Ziff. 23): Kind A -> Ziff. 23.1 (Code 252) Fr. 7'600; Kind B -> Ziff. 23.2 (Code 254) Fr. 10'800; Ausbildungskosten Kind B -> Ziff. 23.3 (Code 256, Formular 10): 9'500 - 1'000 Stipendium - 3'200 Selbstbehalt = CHF 5'300 (unter dem Maximum von Fr. 13'700). Total Kinderabzüge Kanton CHF 23'700. Bund: einheitlicher Kinderabzug CHF 6'800 pro Kind (Art. 35 Abs. 1 lit. a DBG), kein Abzug für Ausbildungskosten -> 2 x 6'800 = CHF 13'600 (Anpassung durch die Steuerbehörde, Merkblatt 32).

**Antwort des Agenten** (37.6 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__formular, steuerwiki__wert, steuerwiki__rechne):

> **Fall:** SG, Steuerjahr 2025, Ehepaar, Kind A (2 J., noch nicht schulpflichtig), Kind B (20 J., in Ausbildung). Beide Kinder werden zur Hauptsache unterhalten, Kind B hat keinen Unterhaltsbeitragsabzug (Ziff. 12.2).
> 
> ## Kanton SG (Formular 1)
> 
> | Ziffer | Code | Position | Betrag |
> |---|---|---|---|
> | 23.1 | 252 | Kinderabzug Kind A (noch nicht schulpflichtig) | CHF 7'600 |
> | 23.2 | 254 | Kinderabzug Kind B (Ausbildung) | CHF 10'800 |
> | 23.3 | 256 | Ausbildungskosten Kind B (Formular 10) | CHF 5'300 |
> | | | **Total Einkommensabzüge Kind** | **CHF 23'700** |
> 
> Ziff. 23.3 rechnet so: 9'500 − Stipendium 1'000 − Selbstbehalt 3'200 = 5'300. Das liegt unter dem Höchstbetrag von 13'700.
> 
> Zusätzlich je Kind ein Zuschlag zu Ziff. 14 (Versicherungen, Code 600): 2 × CHF 1'100 = CHF 2'200.
> 
> ## Bund (direkte Bundessteuer)
> 
> Im Formular gibt es nur eine Spalte. Die Bundesbeträge trägt die Steuerbehörde automatisch ein (Merkblatt 32).
> 
> - **Ziff. 23.1 (Kind A):** CHF 6'800 Kinderabzug
> - **Ziff. 23.2 (Kind B):** CHF 6'800 Kinderabzug
> - **Ziff. 23.3:** kein Bundesabzug. Die Position nennt das Bundesfeld zwar mit CHF 6'800, die Regel sagt aber «nur Kanton/Gemeinde». Der Betrag ist bereits in den beiden Kinderabzügen enthalten. Nicht doppelt ansetzen.
> - **Einkommensabzug Kinder Bund:** CHF 13'600
> - **Steuerbetragsabzug:** 2 × CHF 263 = CHF 526, wird vom Steuerbetrag abgezogen, nicht vom Einkommen. Die Position nennt nur «max. Fr. 263»; die Pro-Kind-Angabe stammt aus dem Wert-Eintrag des Bundes (Elterntarif).
> - **Zuschlag Ziff. 14 Bund:** 2 × CHF 700 = CHF 1'400
> 
> ## Status und Vorbehalte
> 
> - Alle Werte sind ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen.
> - Kind A: die Staffel «noch nicht schulpflichtig» gilt per 31.12.; Alter am 31.12.2025 prüfen.
> - Ziff. 23.3 setzt voraus, dass Formular 10 mit Rechnungen (Semestergebühren, Bücher, ÖV-Abo) und die Stipendienverfügung eingereicht werden bzw. auf Verlangen bereitliegen.
> - Ziff. 23.3 mit Bundesbetrag (6'800) in den Limiten steht im Widerspruch zur Regel «nur Kanton» – ich habe die Regel angewendet.

## p07

**Frage:** TG 2025: Arbeitnehmer fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 22 km einfach, Hin- und Rückfahrt täglich, 225 Arbeitstage, keine weiteren Fahrkosten, kein Geschäftsfahrzeug. Wie wird Formular 4.2 Ziff. 2.3–2.5 für Staats- und Bundessteuer ausgefüllt und was geht in die Steuererklärung?

**Soll (Referenz):** Formular 4.2 Ziff. 2.3: 44 km/Tag x 225 Tage = 9'900 km pro Jahr (Code 211). Staatssteuer, Auto-Ansätze nach Jahreskilometern gestaffelt: 3'000 km x 0.60 = 1'800; 2'000 km x 0.50 = 1'000; 4'900 km x 0.40 = 1'960 -> CHF 4'760. Bundessteuer einheitlich CHF 0.70/km: 9'900 x 0.70 = CHF 6'930. Ziff. 2.4 Total effektive Fahrkosten (Code 212): Staat 4'760 / Bund 6'930. Ziff. 2.5 Total abzugsfähige Fahrkosten (Code 213): Staat max. 6'000 -> CHF 4'760; Bund max. 3'300 -> CHF 3'300. Über Ziff. 7 Total Berufsauslagen (Code 240) in Steuererklärung Seite 3, Ziff. 10.1 (linke Spalte Staat, rechte Spalte Bund).

**Antwort des Agenten** (34.6 s · Tools: 6 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **Ergebnis TG 2025:** Kanton 4'760 Fr. (Staatssteuer), Bund 3'300 Fr. (Bundessteuer, durch den Höchstbetrag begrenzt).
> 
> **Grundlage:** 2 × 22 km × 225 Arbeitstage = **9'900 km/Jahr**. Keine weiteren Fahrkosten, also Ziff. 2.1 und 2.2 = 0.
> 
> | Form. 4.2 | Was | Staat (Kanton) | Bund |
> |---|---|---|---|
> | **Ziff. 2.3** Kosten Privatauto | Kanton: gestaffelt 3'000 km × 0.60 = 1'800 + 2'000 km × 0.50 = 1'000 + 4'900 km × 0.40 = 1'960 → **4'760**. Bund: 9'900 km × 0.70 = **6'930** | 4'760 | 6'930 |
> | **Ziff. 2.4** Total effektive Fahrkosten | Übertrag 2.1 + 2.2 + 2.3 (je Spalte) | 4'760 | 6'930 |
> | **Ziff. 2.5** Total abzugsfähig | Staat: min(2.4; 6'000). Bund: min(2.4; 3'300) | **4'760** | **3'300** |
> 
> Ziff. 2.5 geht nach Form. 4.2 Ziff. 7 (Code 240) und dann auf Seite 3 der Steuererklärung, Ziff. 10.1 (Staat links, Bund rechts). Die Ziffern 2.3 bis 2.5 sind in der Hilfsblatt-Zeile Code 211/212/213 geführt; Person 2 wäre Code 251/252/253.
> 
> **Bedingungen und Hinweise:**
> - **Begründung:** Der Abzug ist nur zulässig, wenn der ÖV unzumutbar ist. Die Wegleitung nennt als Beispiel eine Zeitersparnis von über 1 Stunde pro Arbeitstag (nur Hin- und Rückweg). Diese Begründung sollte belegt werden, etwa mit Fahrplanvergleich oder Reisezeiten.
> - **Keine ÖV-Abokosten** daneben: Bei Privatauto-Nutzung fallen Abo-Kosten weg. Parkgebühren sind in den km-Ansätzen bereits enthalten.
> - **Arbeitstage:** 225 ist der Maximalwert bei 100 %-Pensum. Bei Teilzeit oder einem anderen Pensum sinkt die Tageszahl entsprechend.
> - **Belege:** Fahrzeugausweis (Auto), Distanzangabe Wohnadresse–Arbeitsort, Arbeitszeitangaben (Quelle: tg-wl-2025__c0179, Einreichepflicht unklar).
> - **Status:** Die Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Staffelung stützt sich auf tg-bkv Par. 1 und das StP 29 Nr. 2 Berechnungsbeispiel (kumulative Staffel, 8'000 km = 4'000 Fr.).
> 
> **Fundstellen:** tg-form-04-2-2025__c0002 · tg-wl-2025__c0003 · tg-wl-2025__c0181 · tg-bkv__par-1 · tg-stg__par-29 · bund-dbg-2025__art-26 · bund-bkv-2025__anhang-1 · tg-stp-29-2__c0006

## p08

**Frage:** TG 2025: Ehepaar bewohnt sein eigenes Einfamilienhaus am Wohnsitz selbst (Baujahr 1995, nicht landwirtschaftlich geschätzt, keine Mieteinnahmen). Indexierter Mietwert aus Selbstnutzung 2025 CHF 21'000; Unterhalt pauschal. Wie werden Eigenmietwert und Nettoerfolg im Formular 7 berechnet und wohin übertragen – Staat und Bund?

**Soll (Referenz):** Formular 7, Zeile «Mietwert selbstgenutzt» 21'000 (beide Spalten). Selbstnutzungsabzug: Staat 40% = 8'400, Bund 20% = 4'200 -> steuerbarer Eigenmietwert (= Bruttoertrag) Staat CHF 12'600, Bund CHF 16'800. Pauschalabzug Unterhalt: Gebäude älter als 10 Jahre -> 20%, berechnet vom steuerbaren Eigenmietwert: Staat 2'520, Bund 3'360. Nettoerfolg: Staat CHF 10'080, Bund CHF 13'440 (bei selbstgenutzter Liegenschaft je Spalte separat ermitteln). Total Nettoerfolge (Code 180) -> Steuererklärung Seite 2, Ziff. 8, Spalte Staat bzw. Bund.

**Antwort des Agenten** (43.8 s · Tools: 9 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__zeige, steuerwiki__suche, steuerwiki__rechne):

> **Kanton Thurgau (Staats- und Gemeindesteuer), Steuerjahr 2025**
> 
> Der Eigenmietwert läuft über das Hilfsblatt Liegenschaften (Form. 7) und wird in Ziff. 8.1 übertragen.
> 
> 1. **Steuerbarer Eigenmietwert:** Mietwert 21'000 − Selbstnutzungsabzug 40 % = **CHF 12'600**. Der Abzug gilt, weil das Haus am Wohnsitz selbstbewohnt wird (tg-form-07-2025__c0002, tg-wl-2025__c0225, Quelle: tg-stg__par-23).
> 2. **Unterhalt pauschal:** Das Gebäude ist 1995 gebaut und am Periodenende 30 Jahre alt, also gilt die Pauschale von **20 %** (tg-stv__par-9). Die Wiki-Regel nennt den Mietwert bzw. steuerbaren Eigenmietwert als Basis. Ich rechne deshalb mit 12'600: 20 % = CHF 2'520. Diese Basis ist eine Auslegung; die Abnahme steht noch aus.
> 3. **Nettoerfolg Staat/Kanton:** 12'600 − 2'520 = **CHF 10'080**.
> 4. **Übertrag:** Der Nettoerfolg (Code 180) geht über das Total von Form. 7 in **Ziff. 8.1 Einkünfte aus Liegenschaften**, linke Spalte (Staats- und Gemeindesteuer). Der Bruttoertrag in Ziff. 8.1 ist der steuerbare Eigenmietwert plus allfällige Mieteinnahmen, hier 12'600. Ziff. 31 Vermögen (Code 430) braucht den Steuerwert der Liegenschaft aus der Schätzung; den haben Sie mir nicht genannt.
> 
> **Bund (direkte Bundessteuer): Die Quellen widersprechen sich ⚠️ strittig**
> 
> - tg-wl-2025__c0225 und die Form.-7-Position nennen für den Bund einen Selbstnutzungsabzug von **20 %**. Dann wäre der Bruttoertrag 16'800, die Pauschale 3'360 und der Nettoerfolg **CHF 13'440**.
> - Die Eckwerte-Abfrage (`wert`) und die Form.-7-Limite sagen dagegen «Bund nicht anwendbar», also kein prozentualer Abzug auf den Eigenmietwert. Dann ist der Bruttoertrag 21'000, die Pauschale 4'200 und der Nettoerfolg **CHF 16'800**.
> - Die Bundes-Wegleitung 2a 2025 (bund-wl-2a-2025__c0028) nennt den Abzug im geprüften Ausschnitt nicht.
> 
> Ich kann nicht sicher sagen, welche Variante stimmt. Bitte prüfen Sie den Bund-Abzug in der amtlichen Wegleitung 2025 oder bei der Veranlagungsbehörde, bevor Sie den Bund-Nettoerfolg eintragen. Die Pauschale 20 % für den Bund (Gebäude älter als 10 Jahre, Bemessung nach Gebäudealter zu Periodenbeginn, LKV Art. 5) ist dagegen belegt.
> 
> **Hinweis:** Für Ehepaare gelten Standardabzüge im Formular; die Frage nach Ziff. 8.1 hat damit nichts zu tun. Die Belege (Schätzungsprotokoll, Liegenschaftensteuerrechnung 2026 mit Mietwertindex) sind für das Hilfsblatt nötig.

## p09

**Frage:** AR 2025: Ehepaar, beide unabhängig voneinander unselbständig erwerbstätig. Das niedrigere Erwerbseinkommen (Nettolohn der Ehefrau abzüglich Berufskosten, Säule-3a-Beiträge und BVG-Einkäufe) beträgt CHF 38'000. Wie hoch ist der Zweiverdienerabzug in Ziffer 17 für die Staats- und Gemeindesteuer und für die direkte Bundessteuer?

**Soll (Referenz):** Ziff. 17 Zweiverdienerabzug. Kanton AR: 10% des niedrigeren Erwerbseinkommens, mind. Fr. 2'500, max. Fr. 5'200 (Beträge gemäss Anhang 1 StG indexiert per 1.1.2024; Art. 35 Abs. 1 lit. h StG nennt die Basisbeträge 2'400/5'000) -> 10% x 38'000 = CHF 3'800. Bund: Art. 33 Abs. 2 DBG 50% des niedrigeren Erwerbseinkommens, mind. 8'600, max. 14'100 -> 50% x 38'000 = 19'000 -> begrenzt auf CHF 14'100. Die Abweichung für die direkte Bundessteuer wird von der Steuerverwaltung automatisch vorgenommen.

**Antwort des Agenten** (26.9 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **Ergebnis (AR 2025, Ehepaar, beide erwerbstätig, E = CHF 38'000):**
> 
> | | Satz | Rechnung | Abzug |
> |---|---|---|---|
> | Staats- und Gemeindesteuer (Kanton AR) | 10 % | 10 % × 38'000 = 3'800; Limite 2'500–5'200 | **CHF 3'800** |
> | Direkte Bundessteuer | 50 % | 50 % × 38'000 = 19'000; Limite 8'600–14'100 → gedeckelt | **CHF 14'100** |
> 
> **Zur Herleitung:**
> - Ziffer 17 im AR-Formular hat keine Bundesspalte. Die Steuerverwaltung nimmt die Abweichung für den Bund automatisch vor (WL AR 2025 S. 33, ar-wl-2025__c0179). Der Bundesabzug ist also trotzdem separat zu rechnen, wie oben.
> - Kanton: Art. 35 Abs. 1 lit. h StG AR, Fundstelle ar-stg__art-35-t3 («10 Prozent, jedoch mindestens»), Limiten ar-stg-anhang-kp__c0001 (Min. 2'500, Max. 5'200).
> - Bund: Art. 33 Abs. 2 DBG, Fundstelle bund-dbg-2025__art-33-t6 («50 Prozent, jedoch mindestens 8600 Franken und höchstens 14 100 Franken»).
> 
> **Status:** Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Fachabnahme bleibt bei der Fachperson.
> 
> **Offene Punkte:**
> - Ziffer 17 ist im Formular nicht verifiziert. Seite 3 der Steuererklärung ist in der Wegleitung nicht als Miniatur abgebildet, deshalb steht der Code nicht sicher fest.
> - Die Ausgangsgrösse E ist vorgegeben (CHF 38'000 = Nettolohn abzüglich Berufskosten, 3a und BVG-Einkauf). Sie muss beim Ausfüllen mit dem tatsächlichen Erwerbseinkommen übereinstimmen. Bei Mitarbeit im Geschäft des Partners gilt eine hälftige Aufteilung.

## p10

**Frage:** AR 2025: Mandant bewohnt sein Einfamilienhaus am Wohnsitz dauernd selbst (Baujahr 1995, einzige Liegenschaft, keine Fremdvermietung). Mietwert gemäss Grundstückschätzung CHF 24'500; er wählt den Pauschalabzug für den Unterhalt. Was wird wo im Formular 7 und in der Steuererklärung (Staats- und Gemeindesteuer) eingetragen?

**Soll (Referenz):** Formular 7, Teil B.a: Eigenmietwert 24'500 abzüglich Selbstnutzungsabzug 20% (4'900) = Total anrechenbarer Eigenmietwert CHF 19'600 = Total Erträge a. und b. -> Übertrag Steuererklärung Seite 2, Ziff. 5. Teil C: Pauschalabzug (Gebäude über 10 Jahre; Bruttomietertrag des gesamten Liegenschaftsbesitzes nicht über Fr. 100'000) = 20% vom Total Liegenschaftserträge = 20% x 19'600 = CHF 3'920 -> Übertrag Steuererklärung Seite 3, Ziff. 15 (separater Abzug, nicht mit Ziff. 5 verrechnet). Wirkung auf das Einkommen netto CHF 15'680.

**Antwort des Agenten** (42.0 s · Tools: 9 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne):

> **AR 2025, Staats- und Gemeindesteuer** (Eigenmietwert 24'500, Pauschale 20 %, Einfamilienhaus Baujahr 1995, einzige Liegenschaft)
> 
> **Formular 7, Abschnitt A (Angaben zur Liegenschaft)**
> - Anteil Person 1/2 in %, Baujahr 1995, Nutzung «selbstbewohnt am Wohnsitz», Grundstück-Nr.
> - Steuerwert = Verkehrswert gemäss amtlicher Grundstückschätzung, in den Formularfeldern für Ziffer 31 Liegenschaften (Seite 4). Der Steuerwert fehlt in Ihrer Angabe und muss aus der Schätzung übernommen werden.
> 
> **Formular 7, Abschnitt B a (Eigenmietwert)**
> 
> | Zeile | Betrag |
> |---|---|
> | Eigenmietwert (amtliche Schätzung) | 24'500 |
> | – Selbstnutzungsabzug 20 % | – 4'900 |
> | = Total anrechenbarer Eigenmietwert | 19'600 |
> 
> Die Summe 19'600 wird zu Abschnitt B «Total Erträge a. und b.» übertragen (Fremdnutzung b. ist hier leer) und dann in die Steuererklärung **Seite 2, Ziffer 5** (Ertrag aus Liegenschaften, Code 712 laut Miniatur) gesetzt.
> 
> **Formular 7, Abschnitt C (Unterhalt)**
> - Pauschalabzug C1 statt tatsächlicher Kosten C2. Das Gebäude ist über 10 Jahre alt, daher 20 %.
> - Basis ist laut WL-Muster die Summe «Erträge (B)», also 19'600: 20 % × 19'600 = **3'920**.
> - Übertrag in die Steuererklärung **Seite 3, Ziffer 15** (Unterhalts- und Verwaltungskosten). Der Code für Seite 3 ist laut Wiki nicht verifiziert.
> - Voraussetzung erfüllt: Bruttomietertrag des ganzen Besitzes 24'500 liegt unter 100'000.
> 
> **Nicht nötig:** Formular 7Z, weil nur eine Liegenschaft vorliegt. Die Übertragung erfolgt direkt aus Form. 7.
> 
> **Offene Punkte**
> 1. **Bund weicht ab:** Für die direkte Bundessteuer gibt es keinen 20-%-Selbstnutzungsabzug. Die Pauschale wird laut Wiki beim Bund auf dem Brutto-Eigenmietwert berechnet (20 % × 24'500 = 4'900). Das Formular hat keine Bundesspalte; die Steuerverwaltung nimmt die Abweichung automatisch vor. Die Bundesregel ist nur aus Bundesquellen (bund-lkv art. 5) belegt, nicht aus AR-Quellen.
> 2. **Pauschalbasis prüfen:** Die Wegleitung nennt bei der Pauschale «Erträge (B)». Das Muster stützt die Lesart nach Selbstnutzungsabzug (3'920). Falls die Veranlagung auf dem Brutto-Mietwert rechnet, wären es 4'900. Ich habe das nicht abschliessend geklärt.
> 3. **Belege:** Für die Pauschale sind keine Belege nötig. Eigenmietwert und Steuerwert sind auf Verlangen aus der Grundstückschätzung vorzulegen.
> 
> Status der Angaben: agent-geprüft (Fundstelle geprüft, Abnahme offen). Quellen: ar-form-07-2025__c0001/c0002/c0003, ar-wl-2025__c0158/c0159/c0175, ar-mb-03__c0004, ar-mb-07__c0004.

