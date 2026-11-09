# OpenClaw-Testlauf: positionstest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 10 · Lauf: 2026-11-09 16:59
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## p01

**Frage:** ZH 2025: Ledige unselbständig erwerbende Person, Nettolohn gemäss Lohnausweis CHF 92'000. Sie fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 23 km einfach, 2 Fahrten pro Tag, 220 Arbeitstage. Übrige Berufskosten werden pauschal geltend gemacht (keine Verpflegungskosten). Welche Positionen/Codes im Formular «Berufsauslagen» und welcher Betrag geht in Ziffer 11.1 – Staatssteuer und Bundessteuer getrennt?

**Soll (Referenz):** Formular 360 «Berufsauslagen» (Person 1), Begründung Privatauto Code 2042 (Zeitersparnis über 1 Stunde) ankreuzen. Ziff. 1.3 Auto (CHF 0.70/km, Staat und Bund gleich): 23 km x 2 Fahrten x 220 Tage = 10'120 km x 0.70 = CHF 7'084 (Code 204). Zwischentotal Fahrkosten Code 205: Staat max. CHF 5'200 -> 5'200; Bund max. CHF 3'300 -> 3'300. Ziff. 3 übrige Berufskosten pauschal Code 212: 3% von 92'000 = CHF 2'760 (innerhalb mind. 2'000 / höchstens 4'000; Staat und Bund gleich, vgl. BKV-Anhang). Total Berufsauslagen Code 220 -> Steuererklärung Seite 3, Ziff. 11.1: Staat 5'200 + 2'760 = CHF 7'960; Bund 3'300 + 2'760 = CHF 6'060.

**Antwort des Agenten** (32.1 s · Tools: 7 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__beleg, steuerwiki__rechne):

> **Ziffer 11.1 (Code 220): Staatssteuer CHF 7'960, Bundessteuer CHF 6'060.** Der Unterschied kommt nur vom Fahrkosten-Plafond. Dieser liegt bei der Staatssteuer bei CHF 5'200 und bei der Bundessteuer bei CHF 3'300.
> 
> Stand der Angaben: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Formular 360 «Berufsauslagen» (Person 1)**
> 
> | Position / Code | Inhalt | Staatssteuer | Bundessteuer |
> |---|---|---|---|
> | Ziff. 7, Code **2042** | Begründung ankreuzen: Zeitersparnis über 1 Std. bei Benützung des Privatautos | ankreuzen | ankreuzen |
> | Ziff. 1.3, Code **204** | Auto weisses Kontrollschild: 23 km × 2 Fahrten × 220 Tage = 10'120 km × CHF 0.70 = CHF 7'084 | 7'084 | 7'084 |
> | Code **205** (Zwischentotal Fahrkosten) | Plafond: Kanton max. 5'200, Bund max. 3'300 | **5'200** | **3'300** |
> | Ziff. 2 (Codes 206/208/210) | Verpflegung: keine | – | – |
> | Ziff. 3, Code **212** | Übrige Berufskosten pauschal: 3 % × 92'000 = CHF 2'760 (innerhalb Min. 2'000 / Max. 4'000) | **2'760** | **2'760** |
> | Ziff. 6, Code **220** (Total) | 205 + 212 | **7'960** | **6'060** |
> 
> Ins Hauptformular geht das Total aus Code 220 als **Ziffer 11.1**.
> 
> **Hinweise**
> - **Codes 201 und 202:** Die Zeilen für ÖV-Abo und Velo bleiben leer.
> - **Code 213:** Er bleibt leer. Er gilt nur für effektive übrige Kosten, nicht für die Pauschale.
> - **240-Tage-Grenze:** Sie gilt für den Kilometerabzug beim Auto (Kanton). 220 Tage liegen darunter, es gibt keine Kürzung. Beim Bund gibt es diese Regel nicht.
> - **Begründung des Autos:** Der Abzug mit dem Privatauto ist nur ausnahmsweise zulässig. Hier ist das die Zeitersparnis über 1 Stunde (Haustür–Arbeitsplatz retour), und sie ist in Ziff. 7 anzukreuzen. Ein Geschäftsfahrzeug oder Lohnausweis Feld F würde den Fahrkostenabzug ausschliessen. Davon ist hier nicht auszugehen.
> - **Nettolohn:** Die Pauschale von 3 % bezieht sich auf den Nettolohn gemäss Lohnausweis (Ziff. 11), hier CHF 92'000.
> - **Lohnausweis:** Er ist immer einzureichen.
> 
> **Fundstellen**
> - Pauschale 3 % / Min. 2'000 / Max. 4'000: zh-form-360-2025__c0004
> - Auto-Ansatz und Ausnahmen: zh-form-360-2025__c0002, zh-wl-2025__c0064
> - Begründungscode 2042: zh-form-360-2025__c0005
> - Plafond Kanton CHF 5'200: zh-stg-2025__par-26
> - Plafond Bund CHF 3'300: bund-dbg-2025__art-26
> - Ziff. 11.1 / Code 220: zh-form-300-2025__c0007
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Zur Einrichtung: Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## p02

**Frage:** ZH 2025: Verheiratetes Paar, beide in einer Pensionskasse (2. Säule) versichert, zwei minderjährige Kinder mit Kinderabzug. Bezahlte Krankenkassenprämien 2025 (bereits netto nach individueller Prämienverbilligung) CHF 15'600, Sparzinsen gemäss Wertschriftenverzeichnis CHF 150. Wie wird das Formular «Versicherungsprämien» ausgefüllt und welcher Abzug kommt in Ziffer 15 (Staat / Bund)?

**Soll (Referenz):** Formular 365 «Versicherungsprämien»: Teil A: Code 601 Krankenversicherungsprämien 15'600 + Code 604 Sparzinsen 150 -> Total (A) Code 606 = CHF 15'750. Teil B (Maximum): Verheiratete mit Beiträgen an 2. Säule/3a Code 611: Staat 5'800 / Bund 3'700; Kinderzuschlag Code 613: Staat 2 x 1'300 = 2'600 / Bund 2 x 700 = 1'400 -> Total (B) Code 616: Staat CHF 8'400 / Bund CHF 5'100. Teil C Code 270 = der niedrigere Betrag von (A) und (B): Staat CHF 8'400, Bund CHF 5'100 -> Steuererklärung Seite 3, Ziff. 15 (Spalten Staatssteuer/Bundessteuer).

**Antwort des Agenten** (31.5 s · Tools: 5 Aufrufe read, steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **ZH 2025, Ziffer 15 (Code 270): Staat CHF 8'400, Bund CHF 5'100.** Das tatsächlich bezahlte Total von CHF 15'750 liegt über beiden Höchstbeträgen, deshalb gilt jeweils der Maximalabzug.
> 
> ## Formular 365 «Versicherungsprämien»
> 
> **Teil A – bezahlte Prämien (einspaltig)**
> 
> | Code | Position | CHF |
> |---|---|---|
> | 601 | Private Krankenversicherungsprämien (bereits netto nach individueller Prämienverbilligung) | 15'600 |
> | 602 / 603 | Unfall / Leben / Rente | 0, laut Angaben keine |
> | 604 | Zinsen von Sparkapitalien (gemäss Wertschriftenverzeichnis) | 150 |
> | 607 | Zwischentotal | 15'750 |
> | 605 | Abzüglich erhaltene Prämienverbilligung | 0 |
> | **606** | **Total (A)** | **15'750** |
> 
> - In Code 605 trägst du nichts ein. Die Prämienverbilligung ist mit den Prämien verrechnet und steckt schon in den 15'600. Ein zweiter Abzug wäre ein Doppelabzug (Quelle: zh-form-365-2025__c0001, zh-wl-2025__c0084).
> - Das gilt auch für die Verbilligung der Kinder.
> 
> **Teil B – Maximalabzug (Staat | Bund)**
> 
> Beide Ehegatten haben Beiträge an die 2. Säule. Damit gelten die normalen Höchstbeträge. Die erhöhten Beträge «ohne 2./3a» (Staat 8'700, Bund 5'550) gelten nur, wenn weder die Steuerpflichtigen noch der Arbeitgeber Beiträge an die 2. Säule oder Säule 3a leisteten.
> 
> | | Staat | Bund |
> |---|---|---|
> | Verheiratete (Code 611) | 5'800 | 3'700 |
> | Zuschlag 2 Kinder (Codes 613–615) | 2 × 1'300 = 2'600 | 2 × 700 = 1'400 |
> | **Total (B) (Code 616)** | **8'400** | **5'100** |
> 
> **Übertrag in die Steuererklärung (Form. 300)**
> 
> Ziffer 15 (Code 270) ist der kleinere Betrag aus A und B, je Spalte:
> 
> | | Staatssteuer | Bundessteuer |
> |---|---|---|
> | min(A; B) | min(15'750; 8'400) = **8'400** | min(15'750; 5'100) = **5'100** |
> 
> ## Hinweise
> - **Zahlungsnachweis:** Das Formular 365 ist der Steuererklärung beizulegen. Die Prämienbelege selbst sind laut Wegleitung nicht ausdrücklich verlangt, aber auf Verlangen bereitzuhalten (zh-wl-2025__c0207).
> - **Sparzinsen:** Die CHF 150 müssen mit dem Wertschriftenverzeichnis (Form. 340) übereinstimmen. Sie wirken sich hier wegen der Kappung nicht aus.
> - **Kinder:** Der Zuschlag setzt voraus, dass der Kinderabzug nach § 34 Abs. 1 StG zusteht. Das ist bei zwei minderjährigen Kindern mit Kinderabzug gegeben.
> - **Annahme:** Ich gehe davon aus, dass beide Ehegatten tatsächlich Beiträge an die Pensionskasse leisten. Das ist bei Erwerbstätigen mit PK-Versicherung der Normalfall, ein Blick auf den Lohnausweis (Ziff. 10) bestätigt es.
> - **Status der Werte:** Alle Limiten sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Fundstellen: Staat zh-stg-2025__par-31-t2, Bund bund-dbg-2025__art-33-t2 und -t5, Formularzeilen zh-form-300-2025__c0008 und zh-form-365-2025__c0001.
> 
> Zum Start: Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## p03

**Frage:** ZH 2025: Alleinstehende Mandantin unterstützt ihre erwerbsunfähige Mutter (eigener Haushalt, keine Alimente, kein Kinderabzug) nachweislich mit CHF 5'000 im Jahr 2025. In welcher Ziffer wird das geltend gemacht, welcher Abzug gilt bei der Staatssteuer und bei der Bundessteuer, und wirkt sich das auf den Versicherungsprämienabzug aus?

**Soll (Referenz):** Ziff. 24.2 «Abzug für unterstützte Personen» (Code 374); Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der Unterstützung beilegen. Staat: Voraussetzung Unterstützungsleistung mindestens CHF 2'800 -> 5'000 erfüllt -> Abzug CHF 2'800. Bund: Voraussetzung Unterstützungsleistung mindestens CHF 6'800 (Art. 35 Abs. 1 lit. b DBG) -> 5'000 < 6'800 -> kein Unterstützungsabzug (CHF 0). Folge im Formular 365 Teil B.3: Staat zusätzlicher Abzug CHF 1'300 für die unterstützungsbedürftige Person (Code 614); Bund kein Zuschlag von CHF 700 (Code 615), da kein Unterstützungsabzug zusteht.

**Antwort des Agenten** (36.1 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **ZH 2025: Unterstützung der erwerbsunfähigen Mutter (CHF 5'000)**
> 
> **Ziffer:** Ziff. 24.2 «Abzug für unterstützte Personen» (Code 374), Steuererklärung ZH 2025, Form. 300. Auf Seite 1 sind Name, Geburtsjahr, Adresse und Unterstützungsbetrag pro Jahr anzugeben. Die Bestätigung der unterstützten Person (Art, Zeitpunkt, Höhe der Unterstützung) ist beizulegen. Zahlungsbelege nur auf Verlangen (zh-form-300-2025__c0010; ☑️ agent-geprüft).
> 
> **Abzug (fixer Betrag, nicht die effektiven CHF 5'000):**
> 
> | | Mindestunterstützung | Abzug |
> |---|---|---|
> | Staatssteuer | ≥ CHF 2'800 | **CHF 2'800** (§ 34 StG ZH, zh-stg-2025__par-34) |
> | Bundessteuer | ≥ CHF 6'800 | **CHF 0** |
> 
> - **Staatssteuer:** Die CHF 5'000 liegen über CHF 2'800, die Bedingung ist erfüllt.
> - **Bundessteuer:** Der Abzug beträgt CHF 6'800 (Art. 35 Abs. 1 lit. b DBG, bund-dbg-2025__art-35). Er setzt eine Unterstützung von mindestens CHF 6'800 voraus. Die CHF 5'000 erreichen das nicht, deshalb gibt es bei der Bundessteuer **keinen** Abzug.
> - Die Mindestunterstützung für den Bund ist aus der Position 24.2 abgeleitet («Unterstützung ≥ Bund 6'800»). Das ist keine wörtliche Gesetzesstelle. Die Formulierung in Art. 35 DBG lautet «Abzug von 6800 Franken für jede erwerbsunfähige oder beschränkt erwerbsfähige Person, an deren Unterhalt der Steuerpflichtige mindestens in dieser Höhe beiträgt».
> 
> **Voraussetzungen, die erfüllt sein müssen:**
> - Die Mutter ist erwerbsunfähig oder beschränkt erwerbsfähig und unterstützungsbedürftig. Das ist hier angegeben.
> - Es werden keine Alimente für sie abgezogen. Das trifft zu.
> - Sie ist weder Ehegattin noch Kind mit Kinderabzug. Das trifft zu.
> - Die Leistungen müssen hinreichend nachgewiesen sein. Das ist hier angegeben.
> - **Nicht aus dem Sachverhalt ersichtlich:** Für die Staatssteuer nennt die Position die Bedürftigkeitsgrenze der Mutter (ZStB 34.1, Wohnsitz CH). Ihr Einkommen muss unter CHF 15'000 liegen und ihr Vermögen unter CHF 50'000. Das ist bei der Mutter zu klären und bleibt ⬜ ungeprüft. Ich habe den Chunk nicht im Wortlaut geöffnet.
> 
> **Wirkung auf den Versicherungsprämienabzug (Ziff. 15, Code 270):** Ja. Für jede unterstützungsbedürftige Person, für die ein Abzug nach § 34 Abs. 1 StG geltend gemacht werden kann, erhöht sich das Maximum der Versicherungsprämien (zh-stg-2025__par-31-t2):
> 
> | | Basis Alleinstehende mit 2. Säule/3a | Zuschlag | Maximum |
> |---|---|---|---|
> | Staat | 2'900 | +1'300 | **4'200** |
> | Bund | 1'800 | +700 | **2'500** |
> 
> Ohne Beiträge an 2. Säule/3a sind es 4'350 + 1'300 = **5'650** (Staat) und 2'700 + 700 = **3'400** (Bund). Im Form. 365 steht der Zuschlag im Teil B (Code 616, Staat 1'300 / Bund 700). Abziehbar ist der tiefere Betrag aus bezahlten Prämien (Teil A) und diesem Maximum.
> 
> **Wichtige Einschränkung bei der Bundessteuer:** Der Zuschlag knüpft an die Berechtigung zum Abzug nach Art. 35 Abs. 1 lit. b DBG an (analog zur ZH-Formulierung). Da der Bundesabzug hier mangels CHF 6'800 entfällt, **dürfte auch der Bundeszuschlag von CHF 700 entfallen**. Das ist meine Ableitung und nicht wörtlich belegt. Das Wiki führt den Bundeszuschlag nur als «je Kind/unterstützungsbedürftige Person». Bei den Bundeswerten ist der Zuschlag als 700 angegeben (bund-dbg-2025__art-33-t5), ohne Ausführung zur Bedingung. Ich würde diesen Punkt vor der Eingabe prüfen (`suche … --jur bund`), sonst gilt für die Bundessteuer das Basismaximum von 1'800 bzw. 2'700.
> 
> **Zusammenfassung zur Eingabe:** Ziff. 24.2 Staat 2'800 / Bund 0. Ziff. 15 Maximum Staat 4'200 (bzw. 5'650 ohne Vorsorge) / Bund voraussichtlich 1'800 (bzw. 2'700 ohne Vorsorge).
> 
> Alle Werte sind ☑️ agent-geprüft (Abnahme offen). Die fachliche Beurteilung bleibt bei der Fachperson.

## p04

**Frage:** SG 2025: Nettoeinkommen gemäss Ziffer 20 CHF 80'000. Arzt- und Zahnarztrechnungen 2025 brutto CHF 6'200, davon von der Krankenkasse vergütet CHF 1'700. Wo werden die Kosten deklariert und wie hoch ist der Abzug für die Staats- und Gemeindesteuern bzw. für die direkte Bundessteuer (Annahme: massgebendes Nettoeinkommen Bund ebenfalls CHF 80'000)?

**Soll (Referenz):** Formular 6 (Rückseite «Krankheits-, Unfall- und behinderungsbedingte Kosten»): Bruttobetrag 6'200 abzüglich Beiträge Dritter 1'700 = selbst getragene Kosten CHF 4'500 -> Steuererklärung Seite 3, Vorkolonne Ziff. 21.1 (Code 650). Kanton SG: Selbstbehalt 2% des Nettoeinkommens (Ziff. 20) = 2% x 80'000 = 1'600 (Code 238) -> Abzug Code 240 = CHF 2'900. Bund: Selbstbehalt 5% (Art. 33 Abs. 1 lit. h DBG; Merkblatt 32) = 4'000 -> Abzug CHF 500. Das SG-Formular hat nur eine Spalte; die Abweichung für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor.

**Antwort des Agenten** (28.3 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne, steuerwiki__zeige):

> **SG 2025, Krankheitskosten**
> 
> **Wo deklariert**
> - Die Einzelrechnungen (Arzt, Zahnarzt) kommen auf die Rückseite von Formular 6, dem Hilfsblatt Krankheitskosten. Dort stehen Rechnungsdatum, Leistungserbringer, Bruttobetrag, abzüglich Beiträge Dritter (hier Krankenkasse) und die selbst getragenen Kosten.
> - Das Total der selbst getragenen Kosten geht in Formular 1 in die Vorkolonne von Ziff. 21.1 (Code 650). Der Selbstbehalt steht unter Code 238 und der Abzug unter Code 240.
> - Das Formular hat nur eine Spalte. Die Abweichungen für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor (sg-wl-2025__c0173).
> - Die Belege sind auf Verlangen einzureichen. Verweist ihr in Formular 6 aber auf einen Krankenkassenauszug oder das Total laut Zusammenzug, müsst ihr die detaillierte Leistungsübersicht beilegen (sg-form-6-2025__c0003).
> 
> **Berechnung**
> 
> Selbst getragene Kosten: 6'200 − 1'700 = **CHF 4'500**. Die Rückvergütung der Krankenkasse wird abgezogen, weil nur die tatsächlich selbst getragenen Kosten abzugsfähig sind.
> 
> | | Selbstbehalt | Selbstbehalt in CHF | Abzug |
> |---|---|---|---|
> | Staats- und Gemeindesteuern SG | 2 % von Ziff. 20 | 1'600 | 4'500 − 1'600 = **CHF 2'900** |
> | Direkte Bundessteuer | 5 % vom Nettoeinkommen | 4'000 | 4'500 − 4'000 = **CHF 500** |
> 
> **Fundstellen und Status**
> - Kanton: sg-stg-2025__art-46 und sg-form-1-2025__c0010 (☑️ agent-geprüft, Abnahme offen).
> - Bund: Art. 33 Abs. 1 lit. h DBG, bund-dbg-2025__art-33-t3 (☑️ agent-geprüft, Abnahme offen).
> 
> **Zur Bundesbasis**
> - Beim Bund beträgt der Selbstbehalt 5 % der um die Aufwendungen nach Art. 26–33 DBG verminderten Einkünfte.
> - Ich habe die Annahme von CHF 80'000 unverändert übernommen. Weicht das tatsächliche Bundesnettoeinkommen ab, ändern sich der Selbstbehalt und damit der Abzug.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Ich bin übrigens euer neuer Assistent. Wie möchtet ihr mich nennen?

## p05

**Frage:** SG 2025: Mandant gewinnt im Swiss Lotto (interkantonal durchgeführte Lotterie = Grossspiel) einen Einzelgewinn von CHF 1'500'000. Wo wird der Gewinn deklariert, welcher Teil ist steuerbar und welche Einsatzkosten sind abziehbar – Kanton und Bund getrennt?

**Soll (Referenz):** Deklaration im Wertschriften- und Guthabenverzeichnis (Formular 2), Spalte A (Bargewinn aus inländischer Lotterie, verrechnungssteuerpflichtig); Übertrag Ziff. 4.1 (Code 146). Kanton SG: Einzelgewinne aus Grossspielen steuerbar, soweit > Fr. 1'069'800 -> 1'500'000 - 1'069'800 = CHF 430'200 steuerbar; Einsatzkosten unter Ziff. 16.1 (Code 220): 5%, höchstens Fr. 5'400 -> CHF 5'400; netto CHF 424'800. Bund: steuerfrei bis CHF 1'070'400 (Art. 24 lit. ibis DBG) -> steuerbar CHF 429'600; Einsatzkosten 5%, höchstens CHF 5'400 (Art. 33 Abs. 4 DBG) -> CHF 5'400; netto CHF 424'200. (Der Höchstbetrag 5'400 greift unabhängig davon, ob 5% vom Gesamt- oder vom steuerbaren Gewinn gerechnet werden.)

**Antwort des Agenten** (69.4 s · Tools: 29 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne):

> **SG 2025: Swiss-Lotto-Gewinn CHF 1'500'000 (Grossspiel)**
> 
> Steuerbar ist nur der Teil über der Freigrenze, also rund CHF 430'000. Der Einsatzabzug beträgt bei Kanton und Bund je CHF 5'400. Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **1. Wo wird deklariert?**
> - **Kanton und Bund:** Es gibt nur eine Steuererklärung. SG hat kein separates Bundesformular, und die Steuerbehörde nimmt die Bundesabweichungen automatisch vor (sg-wl-2025__c0173).
> - **Gewinn:** Er kommt ins Wertschriften- und Guthabenverzeichnis (Formular 2) und wird in Ziff. 4.1 (Code 146) der Steuererklärung übertragen (sg-form-1-2025__c0006).
> - **Spalte A:** «Bargewinne aus inländischen Lotterien und anderen Geldspielen» gehören in Spalte A, weil Verrechnungssteuer anfällt (sg-wl-2025__c0135).
> - **Beilage:** Die Lotto-/Totobescheinigung ist beizulegen (sg-form-2-2025__c0004).
> - **Einsatzkosten:** Sie werden separat in Ziff. 16.1 abgezogen (sg-wl-2025__c0090).
> 
> **2. Steuerbarer Teil (Freibetrag je Einzelgewinn)**
> 
> | | Kanton SG | Bund (DBG) |
> |---|---|---|
> | Gewinn | 1'500'000 | 1'500'000 |
> | Steuerfrei bis | 1'069'800 | 1'070'400 |
> | **Steuerbar vor Abzug** | **430'200** | **429'600** |
> | Quelle | Art. 37 lit. o StG SG (sg-stg-2025__art-37-t3) | Art. 24 lit. ibis DBG, VKP Art. 6 (bund-dbg-2025__art-24-t3) |
> 
> - **Freibetrag, nicht Freigrenze:** Der Wortlaut lautet «Gewinne bis zum Betrag von …». Das spricht für einen Freibetrag, bei dem nur der Mehrbetrag steuerbar ist.
> - **Anders bei Kleingewinnen:** Bei Verkaufsförderungs-Lotterien über CHF 1'100 ist dagegen der ganze Gewinn steuerbar.
> - **Vorbehalt:** Die SG-Wegleitung formuliert nur «soweit > Fr. 1'069'800» (sg-wl-2025__c0064). Ausdrücklich bestätigt «nur der übersteigende Anteil» sind die Wiki-Quellen von TG (tg-wl-2025__c0148) und ZH (zh-wl-2025__c0167). Für SG ist das aus dem Gesetzestext abgeleitet.
> 
> **3. Abziehbare Einsatzkosten**
> - **Regel:** 5 % des einzelnen steuerbaren Gewinns, höchstens CHF 5'400.
>   - Kanton: Art. 45 Abs. 3 StG SG (sg-stg-2025__art-45-t5).
>   - Bund: Art. 33 Abs. 4 DBG (bund-dbg-2025__art-33-t7).
> - **Hier:** 5 % ergeben CHF 21'510 (vom steuerbaren Teil) oder CHF 75'000 (vom Gesamtgewinn). In beiden Fällen greift der Deckel, der Abzug beträgt also **CHF 5'400**.
> - **Bund:** Die Bundeswegleitung sagt zusätzlich, der Abzug ist höchstens so hoch wie die im gleichen Jahr im selben Wettbewerb erzielten Gewinne (bund-wl-2a-2025__c0025). Das ist hier unproblematisch.
> - **Nicht anwendbar:** Der höhere Abzug von CHF 26'700 (Kanton) bzw. CHF 26'800 (Bund) für abgebuchte Spieleinsätze gilt nur für Online-Spielbankenspiele (sg-form-32-2025__c0004). Lotto-Tippscheine fallen nicht darunter.
> 
> **4. Ergebnis (gerechnet mit `rechne`)**
> - **Kanton:** 1'500'000 − 1'069'800 − 5'400 = **CHF 424'800** zusätzliches steuerbares Einkommen.
> - **Bund:** 1'500'000 − 1'070'400 − 5'400 = **CHF 424'200** zusätzliches steuerbares Einkommen.
> 
> **Offene Punkte**
> - **Verrechnungssteuer (35 %):** Sie fällt auf den bundessteuerlich steuerbaren Teil an. Das wären rechnerisch CHF 150'360 (35 % von 429'600). Der Wert ist nicht aus einer SG-Quelle geprüft, die Bescheinigung der Swisslos ist massgebend. Wie der Zwölf-Franken-Unterschied von CHF 600 zwischen Kanton und Bund in Spalte A/B aufzuteilen ist, zeigt die SG-Wegleitung nicht. TG sieht für den nur kantonal steuerbaren Anteil Spalte B vor (tg-wl-2025__c0149). Das bitte vor der Eingabe fachlich klären.
> - **Fachliche Beurteilung:** Sie liegt bei der Fachperson.
> 
> Nebenbei: Ich bin neu hier. Wie möchtest du mich nennen?

## p06

**Frage:** SG 2025: Ehepaar mit zwei Kindern, für deren Unterhalt es zur Hauptsache aufkommt: Kind A ist 2-jährig (noch nicht schulpflichtig), Kind B ist 20 und studiert. Für Kind B selbst getragene Ausbildungskosten (Semestergebühren, Bücher, ÖV zum Studienort) CHF 9'500, erhaltenes Stipendium CHF 1'000. Welche Ziffern/Codes und welche Beträge – Kanton und Bund?

**Soll (Referenz):** Kanton SG (Steuererklärung Seite 3, Ziff. 23): Kind A -> Ziff. 23.1 (Code 252) Fr. 7'600; Kind B -> Ziff. 23.2 (Code 254) Fr. 10'800; Ausbildungskosten Kind B -> Ziff. 23.3 (Code 256, Formular 10): 9'500 - 1'000 Stipendium - 3'200 Selbstbehalt = CHF 5'300 (unter dem Maximum von Fr. 13'700). Total Kinderabzüge Kanton CHF 23'700. Bund: einheitlicher Kinderabzug CHF 6'800 pro Kind (Art. 35 Abs. 1 lit. a DBG), kein Abzug für Ausbildungskosten -> 2 x 6'800 = CHF 13'600 (Anpassung durch die Steuerbehörde, Merkblatt 32).

**Antwort des Agenten** (39.1 s · Tools: 9 Aufrufe steuerwiki__formular, steuerwiki__wert, steuerwiki__position, steuerwiki__zeige, steuerwiki__rechne):

> **SG 2025, Ehepaar mit Kind A (2 Jahre, nicht schulpflichtig) und Kind B (20 Jahre, Studium)**
> 
> Das St. Galler Formular hat nur eine Spalte. Die Bundesbeträge setzt die Steuerbehörde automatisch (sg-wl-2025__c0173). Die Bundeswerte unten sind daher zur Kontrolle ausgewiesen und nicht separat einzutragen.
> 
> | Ziff. / Code | Position | Kanton | Bund |
> |---|---|---|---|
> | **23.1 / 252** | Kinderabzug, nicht schulpflichtig (Kind A) | 7'600 | 6'800 |
> | **23.2 / 254** | Kinderabzug, Schule/Ausbildung (Kind B, volljährig, Unterhalt zur Hauptsache) | 10'800 | 6'800 |
> | **23.3 / 256** | Ausbildungskosten Kind B (Formular 10) | **5'300** | kein Abzug |
> | **14 / 600** | Versicherungsprämien, nur Maximalbetrag (Kinderzuschlag je Kind mit Abzug) | 6'800 + 2 × 1'100 = 9'000 | 3'700 + 2 × 700 = 5'100 |
> | Nur Bund | Abzug vom Steuerbetrag | – | 2 × 263 = 526 |
> | **36.1–36.3 / 330** | Vermögen, Zusatzfreibetrag minderjähriges Kind (nur Kind A) | 20'000 | keine Vermögenssteuer |
> 
> **Kinderabzüge (Ziff. 23.1 und 23.2)**
> - Kanton: 7'600 + 10'800 = 18'400.
> - Bund: 2 × 6'800 = 13'600. Er kennt keine Altersstaffel.
> - Quellen: sg-wl-2025__c0104, sg-form-1-2025__c0011, bund-dbg-2025__art-35.
> 
> **Ausbildungskosten Kind B (Ziff. 23.3)**
> - Gerechnet wird mit der Formel der Position: min(max(0; Kosten − Stipendium − 3'200); 13'700). Das ergibt 9'500 − 1'000 − 3'200 = 5'300.
> - Die 9'500 (Semestergebühren, Bücher, ÖV zum Studienort) sind laut Wegleitung abzugsfähig (sg-wl-2025__c0105).
> - Voraussetzung ist, dass der Abzug nach Ziff. 23.2 gilt. Das ist hier der Fall.
> - Stipendienverfügung und Belege sind für Formular 10 bereitzuhalten.
> - Beim Bund gibt es keinen Ausbildungskostenabzug. Dort bleibt es bei den 6'800 für Kind B.
> 
> **Versicherungsprämien (Ziff. 14)**
> - Die 9'000 bzw. 5'100 sind nur die Obergrenze. Abziehbar ist der tiefere Betrag aus den tatsächlichen Prämien plus Sparzinsen (abzüglich Prämienverbilligung) und diesem Maximum.
> - Der Kinderzuschlag gilt nur für Kinder mit Abzug nach Ziff. 23.1 oder 23.2. Das trifft auf beide zu (sg-wl-2025__c0094-Umfeld: Position 14, sg-stg-2025__art-45-t2).
> 
> **Nicht anwendbar oder nicht geprüft**
> - Ziff. 16.4 (berufsorientierte Weiterbildung) gilt nicht für Kind B. Die Studienkosten gehören in Ziff. 23.3.
> - Kinderbetreuungskosten (Ziff. 16.2) für Kind A: Es wurden keine Kosten genannt. Falls Drittbetreuung anfällt, sind max. 26'700 (Kanton) bzw. 25'800 (Bund) möglich.
> - Ob das Stipendium bei Kind B selbst steuerbar ist, habe ich nicht geprüft.
> 
> Status der Werte: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Ich bin übrigens neu hier. Wie möchtest du mich nennen?

## p07

**Frage:** TG 2025: Arbeitnehmer fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 22 km einfach, Hin- und Rückfahrt täglich, 225 Arbeitstage, keine weiteren Fahrkosten, kein Geschäftsfahrzeug. Wie wird Formular 4.2 Ziff. 2.3–2.5 für Staats- und Bundessteuer ausgefüllt und was geht in die Steuererklärung?

**Soll (Referenz):** Formular 4.2 Ziff. 2.3: 44 km/Tag x 225 Tage = 9'900 km pro Jahr (Code 211). Staatssteuer, Auto-Ansätze nach Jahreskilometern gestaffelt: 3'000 km x 0.60 = 1'800; 2'000 km x 0.50 = 1'000; 4'900 km x 0.40 = 1'960 -> CHF 4'760. Bundessteuer einheitlich CHF 0.70/km: 9'900 x 0.70 = CHF 6'930. Ziff. 2.4 Total effektive Fahrkosten (Code 212): Staat 4'760 / Bund 6'930. Ziff. 2.5 Total abzugsfähige Fahrkosten (Code 213): Staat max. 6'000 -> CHF 4'760; Bund max. 3'300 -> CHF 3'300. Über Ziff. 7 Total Berufsauslagen (Code 240) in Steuererklärung Seite 3, Ziff. 10.1 (linke Spalte Staat, rechte Spalte Bund).

**Antwort des Agenten** (34.4 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne, steuerwiki__zeige):

> **TG 2025: Arbeitsweg 22 km einfach, Privatauto, 225 Arbeitstage**
> 
> Für Staat und Bund ergibt das Fr. 4'760 bzw. Fr. 3'300 (nach Kürzung auf das Bundesmaximum). Beide Beträge gehen über Form. 4.2 Ziff. 7 in Ziff. 10.1 der Steuererklärung. Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Voraussetzungen**
> - Das Privatauto ist nur in begründeten Ausnahmefällen abziehbar, z.B. bei einer Zeitersparnis von über 1 Stunde pro Arbeitstag. Das ist hier gegeben. Sonst wären nur die ÖV-Abokosten abziehbar (tg-wl-2025__c0003).
> - Ziff. 1.2 (Geschäftsfahrzeug zur Verfügung?): **Nein** ankreuzen. Bei «Ja» gäbe es keinen Fahrkostenabzug.
> - Lohnausweis Feld F darf nicht angekreuzt sein, und der Arbeitgeber darf keine Fahrkosten vergüten.
> - Ziff. 2.1 (ÖV-Abo) und Ziff. 2.2 (Velo) bleiben leer.
> 
> **Form. 4.2 Ziff. 2.3** (Quelle: tg-form-04-2-2025__c0002)
> - Ankreuzen: **Auto**.
> - Arbeitsweg von Wohnort bis Arbeitsort eintragen.
> - km pro Tag: 22 × 2 = **44**.
> - Anzahl Tage: **225**.
> - km pro Jahr: 44 × 225 = **9'900 km**.
> - Total Kosten für den Arbeitsweg mit dem Motorfahrzeug (Code 211), je Spalte in Franken:
> 
> | | Rechnung | Betrag |
> |---|---|---|
> | **Staatssteuer** (gestaffelt, inkl. Parkgebühren) | 3'000 km × 0.60 = 1'800<br>2'000 km × 0.50 = 1'000<br>4'900 km × 0.40 = 1'960 | **Fr. 4'760** |
> | **Bundessteuer** (einheitlich 0.70 pro km) | 9'900 km × 0.70 | **Fr. 6'930** |
> 
> **Ziff. 2.4** (Total effektive Fahrkosten, Code 212)
> - Es gibt keine weiteren Fahrkosten, daher Staat Fr. 4'760 und Bund Fr. 6'930.
> 
> **Ziff. 2.5** (Total abzugsfähige Fahrkosten, Code 213; Quelle: tg-form-04-2-2025__c0002, tg-stp-29-2__c0006)
> - Staat: min(4'760; 6'000) = **Fr. 4'760**.
> - Bund: min(6'930; 3'300) = **Fr. 3'300**.
> 
> **Übertrag in die Steuererklärung**
> - Ziff. 2.5 geht in Form. 4.2 **Ziff. 7** (Total Berufsauslagen, Code 240). Dort kommen noch Verpflegung (Ziff. 3), übrige Berufskosten (Ziff. 4, 3 % vom Nettolohn, min. Fr. 2'000, max. Fr. 4'000) und gegebenenfalls Ziff. 5 und 6 dazu.
> - Das Total wandert auf Seite 3 der Steuererklärung in **Ziff. 10.1** (Staat links, Bund rechts). Die Spalten bleiben getrennt (tg-form-01-2025__c0010, tg-wl-2025__c0196).
> 
> **Hinweise**
> - Das Maximum von Fr. 6'000 bzw. Fr. 3'300 wird bei Teilzeit oder unterjähriger Erwerbstätigkeit nicht gekürzt.
> - Der Bundesabzug ist also um Fr. 3'630 gekappt (6'930 − 3'300), der Staatsabzug nicht.
> - Als Beleg empfiehlt sich der Fahrzeugausweis. Ob er eingereicht werden muss, ist laut Wiki unklar.
> - Die fachliche Beurteilung der Zeitersparnis liegt bei der Fachperson bzw. der Steuerbehörde.
> 
> Ich bin übrigens dein neuer Assistent. Wie möchtest du mich nennen?

## p08

**Frage:** TG 2025: Ehepaar bewohnt sein eigenes Einfamilienhaus am Wohnsitz selbst (Baujahr 1995, nicht landwirtschaftlich geschätzt, keine Mieteinnahmen). Indexierter Mietwert aus Selbstnutzung 2025 CHF 21'000; Unterhalt pauschal. Wie werden Eigenmietwert und Nettoerfolg im Formular 7 berechnet und wohin übertragen – Staat und Bund?

**Soll (Referenz):** Formular 7, Zeile «Mietwert selbstgenutzt» 21'000 (beide Spalten). Selbstnutzungsabzug: Staat 40% = 8'400, Bund 20% = 4'200 -> steuerbarer Eigenmietwert (= Bruttoertrag) Staat CHF 12'600, Bund CHF 16'800. Pauschalabzug Unterhalt: Gebäude älter als 10 Jahre -> 20%, berechnet vom steuerbaren Eigenmietwert: Staat 2'520, Bund 3'360. Nettoerfolg: Staat CHF 10'080, Bund CHF 13'440 (bei selbstgenutzter Liegenschaft je Spalte separat ermitteln). Total Nettoerfolge (Code 180) -> Steuererklärung Seite 2, Ziff. 8, Spalte Staat bzw. Bund.

**Antwort des Agenten** (35.6 s · Tools: 7 Aufrufe steuerwiki__position, steuerwiki__beleg, steuerwiki__wert, steuerwiki__zeige, steuerwiki__rechne):

> **TG 2025, selbstgenutztes Einfamilienhaus: Eigenmietwert und Nettoerfolg in Formular 7**
> 
> Staat und Bund werden in Formular 7 getrennt gerechnet, weil der Selbstnutzungsabzug verschieden hoch ist. Die Zahlen sind ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen.
> 
> **Rechnung je Spalte** (indexierter Mietwert CHF 21'000, Baujahr 1995, am Wohnsitz selbstgenutzt = «ja»)
> 
> | Zeile Formular 7 | Staat (Kanton/Gemeinde) | Bund |
> |---|---|---|
> | Mietwert selbstgenutzt (indexiert) | 21'000 | 21'000 |
> | Selbstnutzungsabzug | −40 % = −8'400 | −20 % = −4'200 |
> | **Steuerbarer Eigenmietwert** (= Bruttoertrag, da keine Mieten) | **12'600** | **16'800** |
> | Unterhalt pauschal | −20 % = −2'520 | −20 % = −3'360 |
> | **Nettoerfolg** | **10'080** | **13'440** |
> 
> Die Beträge sind mit dem Rechentool gerechnet.
> 
> **Begründung**
> - **Selbstnutzungsabzug:** Er gilt für dauernd am Wohnsitz selbstbewohntes Eigentum, im Kanton 40 % und beim Bund 20 %. Quelle: tg-wl-2025__c0225, § 23 Abs. 3 StG TG (tg-stg__par-23).
> - **Pauschale:** Das Gebäude ist älter als zehn Jahre (Baujahr 1995), daher 20 % (§ 9 Abs. 2 StV TG, tg-stv__par-9). Beim Bund gilt ebenfalls 20 % (Art. 5 LKV, bund-lkv__art-5).
> - **Wahl der Pauschale:** Sie kann pro Liegenschaft und Jahr statt der effektiven Kosten gewählt werden (§ 9 Abs. 1 StV TG). Dann kommt kein Formular 8 und keine Rechnungskopie dazu.
> 
> **Übertragen in die Steuererklärung (Formular 1)**
> - **Ziff. 8.1 «Einkünfte aus Liegenschaften», Code 180:** Total Nettoerfolge aus Formular 7 eintragen.
>   - Linke Spalte (Staats- und Gemeindesteuern): **CHF 10'080**
>   - Rechte Spalte (direkte Bundessteuer): **CHF 13'440**
>   - Quelle: tg-form-01-2025__c0009, tg-wl-2025__c0196.
> - **Vermögen:** Der Steuerwert der Liegenschaft gehört nicht zum Einkommen. Er kommt in Ziff. 31 «Liegenschaften», Code 430, aus Formular 7. Er gilt nur für Staat und Gemeinde, nicht für den Bund.
> 
> **Offene Punkte**
> - **Indexierter Mietwert:** Er muss mit der rechtskräftigen Schätzung bzw. der Liegenschaftensteuerrechnung (Versand Januar 2026) übereinstimmen. Bei den CHF 21'000 habe ich nur Ihre Angabe übernommen.
> - **Basis der Pauschale:** § 9 StV spricht von «Mietwert oder Eigenmietwert». Ich habe die Pauschale auf dem steuerbaren Eigenmietwert, also nach Selbstnutzungsabzug, gerechnet. Das entspricht dem Aufbau von Formular 7 und der Wiki-Regel. Falls die Veranlagungsbehörde die Pauschale auf dem ungekürzten Mietwert rechnen würde, kämen höhere Abzüge heraus. Dafür habe ich keinen Beleg gefunden. Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Nebenbei: Ich bin Ihr neuer Assistent. Wie möchten Sie mich nennen?

## p09

**Frage:** AR 2025: Ehepaar, beide unabhängig voneinander unselbständig erwerbstätig. Das niedrigere Erwerbseinkommen (Nettolohn der Ehefrau abzüglich Berufskosten, Säule-3a-Beiträge und BVG-Einkäufe) beträgt CHF 38'000. Wie hoch ist der Zweiverdienerabzug in Ziffer 17 für die Staats- und Gemeindesteuer und für die direkte Bundessteuer?

**Soll (Referenz):** Ziff. 17 Zweiverdienerabzug. Kanton AR: 10% des niedrigeren Erwerbseinkommens, mind. Fr. 2'500, max. Fr. 5'200 (Beträge gemäss Anhang 1 StG indexiert per 1.1.2024; Art. 35 Abs. 1 lit. h StG nennt die Basisbeträge 2'400/5'000) -> 10% x 38'000 = CHF 3'800. Bund: Art. 33 Abs. 2 DBG 50% des niedrigeren Erwerbseinkommens, mind. 8'600, max. 14'100 -> 50% x 38'000 = 19'000 -> begrenzt auf CHF 14'100. Die Abweichung für die direkte Bundessteuer wird von der Steuerverwaltung automatisch vorgenommen.

**Antwort des Agenten** (25.3 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **AR 2025, Ziffer 17 (Zweiverdienerabzug), niedrigeres Erwerbseinkommen E = CHF 38'000**
> 
> | | Rechnung | Abzug |
> |---|---|---|
> | **Staats- und Gemeindesteuer (AR)** | 10 % × 38'000 = 3'800. Das liegt zwischen dem Minimum von 2'500 und dem Maximum von 5'200. | **CHF 3'800** |
> | **Direkte Bundessteuer** | 50 % × 38'000 = 19'000. Das übersteigt das Maximum von 14'100, der Abzug wird also gekappt. | **CHF 14'100** |
> 
> **Quellen (☑️ agent-geprüft, Abnahme offen)**
> - **Kanton:** 10 %, mindestens 2'500, höchstens 5'200 gemäss Art. 35 Abs. 1 lit. h StG AR. Fundstellen: `ar-stg__art-35-t3` und `ar-stg-anhang-kp__c0001`. Die Beträge sind indexiert per 1.1.2024 und werden durch die Wegleitung 2025 bestätigt (`ar-wl-2025__c0004`).
> - **Bund:** 50 %, mindestens 8'600, höchstens 14'100 gemäss Art. 33 Abs. 2 DBG. Fundstelle: `bund-dbg-2025__art-33-t6`.
> 
> **Hinweise**
> - Das AR-Formular hat keine eigene Bundesspalte. Den Bundesabzug von 14'100 nimmt die Steuerverwaltung automatisch vor (`ar-wl-2025__c0179`). In Ziffer 17 trägst du nur den kantonalen Betrag von 3'800 ein.
> - Dein E von 38'000 ist bereits nach Berufskosten, Säule 3a und BVG-Einkauf berechnet. Das ist die richtige Basis. Der Abzug darf zusammen mit diesen Abzügen den massgebenden Nettolohn nicht übersteigen. Das ist hier nicht kritisch.
> - Das setzt voraus, dass beide Ehegatten selbständig voneinander erwerbstätig sind und niemand im Geschäft des Partners mitarbeitet. Bei Mitarbeit würde das Einkommen in der Regel hälftig aufgeteilt.
> - Die Ziffer-Nummer 17 ist laut Wiki nicht abschliessend verifiziert, weil Seite 3 des Formulars in der Wegleitung nicht abgebildet ist. Bitte beim Ausfüllen am amtlichen Formular kurz gegenprüfen. Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## p10

**Frage:** AR 2025: Mandant bewohnt sein Einfamilienhaus am Wohnsitz dauernd selbst (Baujahr 1995, einzige Liegenschaft, keine Fremdvermietung). Mietwert gemäss Grundstückschätzung CHF 24'500; er wählt den Pauschalabzug für den Unterhalt. Was wird wo im Formular 7 und in der Steuererklärung (Staats- und Gemeindesteuer) eingetragen?

**Soll (Referenz):** Formular 7, Teil B.a: Eigenmietwert 24'500 abzüglich Selbstnutzungsabzug 20% (4'900) = Total anrechenbarer Eigenmietwert CHF 19'600 = Total Erträge a. und b. -> Übertrag Steuererklärung Seite 2, Ziff. 5. Teil C: Pauschalabzug (Gebäude über 10 Jahre; Bruttomietertrag des gesamten Liegenschaftsbesitzes nicht über Fr. 100'000) = 20% vom Total Liegenschaftserträge = 20% x 19'600 = CHF 3'920 -> Übertrag Steuererklärung Seite 3, Ziff. 15 (separater Abzug, nicht mit Ziff. 5 verrechnet). Wirkung auf das Einkommen netto CHF 15'680.

**Antwort des Agenten** (39.2 s · Tools: 9 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__zeige, steuerwiki__rechne):

> **AR 2025, Staats- und Gemeindesteuer: selbstbewohntes Einfamilienhaus mit Pauschalabzug**
> 
> Der Mandant hat nur diese eine Liegenschaft. Er füllt deshalb ein einziges Formular 7 aus, ein Formular 7Z braucht es nicht. Die Beträge gehen direkt ins Hauptformular.
> 
> **Formular 7**
> 
> | Abschnitt | Eintrag | Betrag CHF |
> |---|---|---|
> | A. Angaben zur Liegenschaft | Nutzung: dauernd selbstbewohnt. Baujahr 1995. Anteil 100 %. Steuerwert gemäss Grundstückschätzung: Betrag fehlt in Ihrer Angabe. | – |
> | B a. Eigenmietwert | Mietwert gemäss Grundstückschätzung | 24'500 |
> | B a. Selbstnutzungsabzug | 20 % von 24'500 | – 4'900 |
> | B a. Total anrechenbarer Eigenmietwert | | **19'600** |
> | B b. Fremdnutzung | keine Fremdvermietung, leer lassen | – |
> | B. Total Erträge a. und b. | | **19'600** |
> | C. Pauschalabzug (C1) | 20 % × 19'600 | **3'920** |
> | C. Tatsächliche Kosten (C2) | leer lassen, Pauschale und tatsächliche Kosten sind alternativ | – |
> 
> **Steuererklärung (Formular 1)**
> 
> | Ziffer | Eintrag | Betrag CHF |
> |---|---|---|
> | Ziff. 5, Ertrag aus Liegenschaften (Code 712) | Total Erträge aus Formular 7 B | 19'600 |
> | Ziff. 15, Unterhalts- und Verwaltungskosten (Abzüge) | Pauschalabzug C1 | 3'920 |
> | Ziff. 31, Liegenschaften (Code 710) | Steuerwert aus Formular 7 A | offen |
> 
> Per Saldo ergibt das eine steuerbare Nettoposition von CHF 15'680 (19'600 – 3'920).
> 
> **Begründung**
> - **Selbstnutzungsabzug 20 %:** Er gilt nur für die am Wohnsitz dauernd selbstbewohnte Liegenschaft, und die trifft hier zu. Zweit- und Ferienwohnungen und Landwirtschaft sind ausgenommen. Fundstellen: ar-wl-2025__c0166 und ar-form-07-2025__c0002.
> - **Pauschale 20 %:** Das Gebäude ist über 10 Jahre alt. Es ist von 1995, also rund 30 Jahre alt. Das Alter wird per Stichtag der Vermögenssteuer bestimmt. Ihre Angaben erfüllen die Voraussetzungen: private Wohnliegenschaft, Bruttomietertrag unter CHF 100'000, Wahl der Pauschale für dieses Gebäude und dieses Jahr. Fundstellen: ar-wl-2025__c0175 und ar-form-07-2025__c0003.
> - **Bemessungsgrundlage der Pauschale:** Das Formular sagt «Pauschalabzug der Erträge (B)». Das ist hier das Total aus B a. und b., also der Eigenmietwert nach Abzug der 20 %. Die Pauschale beträgt daher CHF 3'920 und nicht 20 % von 24'500. Zu dieser Auslegung habe ich keine ausdrückliche Wegleitungsstelle gefunden. Sie stützt sich auf den Wortlaut des Formulars und auf den Hinweis im Wiki «Kanton: EMW netto». Bitte prüfen Sie das noch einmal.
> 
> **Beachten**
> - **Belege:** Es gibt keine Beilagepflicht. Die Grundstückschätzung wird nur auf Verlangen eingereicht (ar-wl-2025__c0156). Bei der Pauschale entfallen Rechnungen, Einzelbeträge ab CHF 5'000 betreffen nur die tatsächlichen Kosten.
> - **Direkte Bundessteuer:** Das AR-Formular hat keine separate Bundesspalte. Abweichungen für den Bund nimmt die Steuerverwaltung automatisch vor (ar-wl-2025__c0179). Für den Bund ist laut Wiki das Alter zu Beginn der Steuerperiode massgebend, und die Pauschale wird auf dem Brutto-Eigenmietwert berechnet. Beides ist aus den AR-Quellen nicht gesichert und deshalb nicht geprüft. Ich habe es nicht ins Formular eingerechnet.
> - **Status der Werte:** Die Werte sind ☑️ agent-geprüft: die Fundstellen sind geprüft, die Abnahme ist offen. Der Code 710 stammt aus einer verzerrten Formular-Miniatur und ist am Originalformular zu kontrollieren. Der Code für Ziff. 15 ist nicht verifiziert, er ist deshalb oben nicht aufgeführt. Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.
> 
> **Offen:** Welcher Steuerwert steht in der Grundstückschätzung für Ziff. 31?
> 
> Ich bin neu hier. Wie möchten Sie mich nennen?

