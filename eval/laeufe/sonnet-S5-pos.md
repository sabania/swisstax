# OpenClaw-Testlauf: positionstest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 10 · Lauf: 2026-11-09 19:27
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## p01

**Frage:** ZH 2025: Ledige unselbständig erwerbende Person, Nettolohn gemäss Lohnausweis CHF 92'000. Sie fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 23 km einfach, 2 Fahrten pro Tag, 220 Arbeitstage. Übrige Berufskosten werden pauschal geltend gemacht (keine Verpflegungskosten). Welche Positionen/Codes im Formular «Berufsauslagen» und welcher Betrag geht in Ziffer 11.1 – Staatssteuer und Bundessteuer getrennt?

**Soll (Referenz):** Formular 360 «Berufsauslagen» (Person 1), Begründung Privatauto Code 2042 (Zeitersparnis über 1 Stunde) ankreuzen. Ziff. 1.3 Auto (CHF 0.70/km, Staat und Bund gleich): 23 km x 2 Fahrten x 220 Tage = 10'120 km x 0.70 = CHF 7'084 (Code 204). Zwischentotal Fahrkosten Code 205: Staat max. CHF 5'200 -> 5'200; Bund max. CHF 3'300 -> 3'300. Ziff. 3 übrige Berufskosten pauschal Code 212: 3% von 92'000 = CHF 2'760 (innerhalb mind. 2'000 / höchstens 4'000; Staat und Bund gleich, vgl. BKV-Anhang). Total Berufsauslagen Code 220 -> Steuererklärung Seite 3, Ziff. 11.1: Staat 5'200 + 2'760 = CHF 7'960; Bund 3'300 + 2'760 = CHF 6'060.

**Antwort des Agenten** (33.1 s · Tools: 6 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__beleg, steuerwiki__rechne):

> **Kanton Zürich · Steuerjahr 2025** (Annahme: Person 1, also Ziff. 11.1 mit Code 220)
> 
> ## Ziffer 11.1: Betrag
> - **Staatssteuer: CHF 7'960**
> - **Bundessteuer: CHF 6'060**
> 
> Der Unterschied kommt vom Fahrkosten-Plafond. Er liegt bei CHF 5'200 für die Staatssteuer und bei CHF 3'300 für den Bund.
> 
> ## Positionen im Formular 360 «Berufsauslagen» (Person 1)
> 
> | Ziff. Form. 360 | Code | Eintrag | Staatssteuer | Bundessteuer |
> |---|---|---|---|---|
> | 1.3 Auto (weisses Kontrollschild) | **204** | 23 km × 2 × 220 Tage = 10'120 km × CHF 0.70 = 7'084 (vor Plafond) | – | – |
> | Zwischentotal Fahrkosten | **205** | auf den Plafond begrenzt | **5'200** | **3'300** |
> | 3 Übrige Berufskosten, pauschal | **212** | 3 % × 92'000 = 2'760 (innerhalb min. 2'000 / max. 4'000) | **2'760** | **2'760** |
> | 6 Total Berufsauslagen | **220** | Übertrag in Ziff. 11.1 | **7'960** | **6'060** |
> 
> Nicht auszufüllen sind:
> - **201 und 202:** ÖV-Abo bzw. Velo-Pauschale entfallen.
> - **206/208/210:** Verpflegung entfällt, wie von dir angegeben.
> - **213:** die effektiven übrigen Kosten entfallen, weil du die Pauschale (212) wählst.
> - **2860:** Wochenaufenthalt entfällt.
> - **216/217:** Nebenerwerb entfällt.
> 
> Das Total ist die Summe der Zwischentotale 205 und 212, jeweils je Spalte (Hauptformular Code 220; Form. 360 hat in beiden Spalten dieselben Codes).
> 
> ## Zu beachten
> - **Begründung Form. 360 Ziff. 7:** Der Auto-Kilometeransatz ist nur ausnahmsweise zulässig. Hier kreuzt du den Code **2042** (Zeitersparnis über 1 Std.) an. Das ist Voraussetzung für Code 204.
> - **Limite 240 Tage:** Der Kilometerabzug ist «in der Regel» auf 240 Arbeitstage begrenzt. Das Formular gibt das nur so an, im Gesetz steht es nicht. Bei 220 Tagen spielt es keine Rolle.
> - **Bund:** Für die Bundessteuer gilt der Km-Abzug nur ohne verfügbares oder zumutbares ÖV. Das Wiki führt als Bundesvoraussetzung nur diesen Punkt. Die Zeitersparnis von über 1 Std. wird dort als Ausnahmegrund nicht ausdrücklich für den Bund genannt. Die Bundesspalte solltest du deshalb auf diesen Punkt prüfen. Mit dem Plafond von CHF 3'300 fällt ein Abzug in dieser Höhe aber ohnehin an, wenn die Voraussetzung erfüllt ist.
> - **Pauschale 3 %:** Sie wird vom Nettolohn gemäss Lohnausweis berechnet (hier CHF 92'000). Der Kanton und der Bund haben dieselben Mindest- und Höchstwerte.
> - **Beilagen:** Form. 360 und der Lohnausweis sind der Steuererklärung beizulegen.
> 
> **Quellen:**
> - Staatssteuer-Plafond 5'200: zh-stg-2025__par-26
> - Bundes-Plafond 3'300: bund-dbg-2025__art-26
> - Auto 70 Rp./km: zh-wl-2025__c0064, bund-bkv-2025__anhang-1
> - Übrige Berufskosten 3 %: zh-form-360-2025__c0004
> - Ziff. 11.1, Code 220: zh-form-300-2025__c0007
> 
> Status aller Werte: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die fachliche Beurteilung bleibt bei der Fachperson.

## p02

**Frage:** ZH 2025: Verheiratetes Paar, beide in einer Pensionskasse (2. Säule) versichert, zwei minderjährige Kinder mit Kinderabzug. Bezahlte Krankenkassenprämien 2025 (bereits netto nach individueller Prämienverbilligung) CHF 15'600, Sparzinsen gemäss Wertschriftenverzeichnis CHF 150. Wie wird das Formular «Versicherungsprämien» ausgefüllt und welcher Abzug kommt in Ziffer 15 (Staat / Bund)?

**Soll (Referenz):** Formular 365 «Versicherungsprämien»: Teil A: Code 601 Krankenversicherungsprämien 15'600 + Code 604 Sparzinsen 150 -> Total (A) Code 606 = CHF 15'750. Teil B (Maximum): Verheiratete mit Beiträgen an 2. Säule/3a Code 611: Staat 5'800 / Bund 3'700; Kinderzuschlag Code 613: Staat 2 x 1'300 = 2'600 / Bund 2 x 700 = 1'400 -> Total (B) Code 616: Staat CHF 8'400 / Bund CHF 5'100. Teil C Code 270 = der niedrigere Betrag von (A) und (B): Staat CHF 8'400, Bund CHF 5'100 -> Steuererklärung Seite 3, Ziff. 15 (Spalten Staatssteuer/Bundessteuer).

**Antwort des Agenten** (28.6 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__beleg, steuerwiki__wert, steuerwiki__rechne):

> **ZH · Steuerjahr 2025: Ziffer 15 (Code 270), Staat CHF 8'400 / Bund CHF 5'100**
> 
> Der Abzug in Ziffer 15 ist bei beiden Steuern der Maximalbetrag, weil die bezahlten Prämien über der Obergrenze liegen. Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Formular Versicherungsprämien (Form. 365)**
> 
> *Teil A: bezahlte Prämien (eine Spalte für Staat und Bund)*
> 
> | Zeile | Code | Betrag CHF |
> |---|---|---|
> | Krankenkassenprämien, bereits netto nach IPV | 601 | 15'600 |
> | Unfall-, Lebens- und Rentenversicherung | 602/603 | nichts, nach Ihren Angaben |
> | Sparzinsen gemäss Wertschriftenverzeichnis | 604 | 150 |
> | Zwischentotal | 607 | 15'750 |
> | Abzüglich erhaltene Prämienverbilligung | 605 | 0 |
> | **Total (A)** | 606 | **15'750** |
> 
> Die IPV bleibt bei Code 605 auf 0. Die Prämien sind schon netto angegeben, und eine zweite Kürzung wäre ein Doppelabzug (zh-form-365-2025__c0001, zh-wl-2025__c0084).
> 
> *Teil B: Maximalabzug (Staat | Bund)*
> 
> Beide sind in der Pensionskasse versichert, also gilt die Zeile «mit Beiträgen an 2./3. Säule», und die Erhöhung um die Hälfte entfällt.
> 
> | Zeile | Staat | Bund |
> |---|---|---|
> | B.1 Verheiratete mit 2./3a (Code 611) | 5'800 | 3'700 |
> | B.3 Zuschlag je Kind (Codes 613–615), 2 × | 2'600 | 1'400 |
> | **Total (B)** (Code 616) | **8'400** | **5'100** |
> 
> Der Kinderzuschlag beträgt je Kind CHF 1'300 beim Staat und CHF 700 beim Bund (zh-form-365-2025__c0002).
> 
> *Teil C: Abzug ist der niedrigere Betrag von (A) und (B), getrennt je Spalte*
> - Staat: min(15'750; 8'400) = **CHF 8'400**
> - Bund: min(15'750; 5'100) = **CHF 5'100**
> 
> Die Beträge habe ich mit dem Rechentool nachgerechnet.
> 
> **Übernahme ins Hauptformular**
> - In Ziffer 15 (Code 270) steht CHF 8'400 in der Spalte Staatssteuer und CHF 5'100 in der Spalte Bundessteuer.
> - Das Formular 365 ist beizulegen (Wegleitung ZH 2025, S. 31). Die Prämienbelege selbst werden nur auf Verlangen eingereicht.
> 
> **Beachten**
> - Die Erhöhung auf 8'700 / 5'550 (ohne 2./3a) gilt nur, wenn weder die Steuerpflichtigen noch ein Arbeitgeber Beiträge an die 2. Säule oder 3a geleistet haben. Das ist hier nicht der Fall, weil beide in der PK versichert sind.
> - Ich bin davon ausgegangen, dass die Ehe rechtlich und tatsächlich ungetrennt ist und beide Kinder den Kinderabzug erhalten.
> - Prämien für Hausrat-, Haftpflicht- und Motorfahrzeugversicherungen sind nicht abziehbar.
> - Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## p03

**Frage:** ZH 2025: Alleinstehende Mandantin unterstützt ihre erwerbsunfähige Mutter (eigener Haushalt, keine Alimente, kein Kinderabzug) nachweislich mit CHF 5'000 im Jahr 2025. In welcher Ziffer wird das geltend gemacht, welcher Abzug gilt bei der Staatssteuer und bei der Bundessteuer, und wirkt sich das auf den Versicherungsprämienabzug aus?

**Soll (Referenz):** Ziff. 24.2 «Abzug für unterstützte Personen» (Code 374); Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der Unterstützung beilegen. Staat: Voraussetzung Unterstützungsleistung mindestens CHF 2'800 -> 5'000 erfüllt -> Abzug CHF 2'800. Bund: Voraussetzung Unterstützungsleistung mindestens CHF 6'800 (Art. 35 Abs. 1 lit. b DBG) -> 5'000 < 6'800 -> kein Unterstützungsabzug (CHF 0). Folge im Formular 365 Teil B.3: Staat zusätzlicher Abzug CHF 1'300 für die unterstützungsbedürftige Person (Code 614); Bund kein Zuschlag von CHF 700 (Code 615), da kein Unterstützungsabzug zusteht.

**Antwort des Agenten** (38.5 s · Tools: 11 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne):

> **ZH · Steuerjahr 2025**
> 
> Die Staatssteuer lässt 2'800 zu. Bei der Bundessteuer gibt es nichts, weil die CHF 5'000 unter der Bundesschwelle von 6'800 liegen.
> 
> **Ziffer**
> - Der Abzug gehört in Ziff. 24.2 «Abzug für unterstützte Personen» (Code 374) im Hauptformular (Form. 300). Fundstelle: zh-form-300-2025__c0010.
> - Auf Seite 1 der Steuererklärung sind Name, Geburtsjahr, Adresse und der Unterstützungsbetrag der Mutter einzutragen (zh-form-300-2025__c0003).
> - Beizulegen ist die Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der Unterstützung. Zahlungsbelege sind auf Verlangen vorzulegen.
> 
> **Abzug**
> 
> | | Abzug | Voraussetzung | Ergebnis bei CHF 5'000 |
> |---|---|---|---|
> | Staatssteuer | CHF 2'800 | Unterstützung mindestens 2'800 (zh-stg-2025__par-34) | ✅ Abzug 2'800 (fixer Betrag, nicht die effektiven 5'000) |
> | Bundessteuer | CHF 6'800 | Unterstützung mindestens 6'800 (Art. 35 Abs. 1 lit. b DBG, bund-dbg-2025__art-35) | ❌ kein Abzug, 5'000 < 6'800 |
> 
> Beide Beträge haben den Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> Ob die Mutter als unterstützungsbedürftig gilt, ist noch zu prüfen. Die Quelle ist ZStB 34.1 Rz 31–33 (zh-zstb-34-1-bis-2025__c0016).
> - Eine Bedürftigkeit kann grundsätzlich angenommen werden, wenn ein amtlicher Nachweis vorliegt.
> - Sonst gilt sie bei einer alleinstehenden Person mit Wohnsitz in der Schweiz bei einem steuerbaren Einkommen unter CHF 15'000 und einem steuerbaren Vermögen unter CHF 50'000.
> - Die Erwerbsunfähigkeit der Mutter muss belegt werden.
> 
> Die Wegleitung zählt Alimente, Kinderabzug und Ehegatten als Ausschlüsse. Davon trifft hier nichts zu.
> 
> **Auswirkung auf den Versicherungsprämienabzug (Ziff. 15, Form. 365 Teil B Z. 3)**
> Ja, aber nur bei der Staatssteuer. Das Formular 365 erhöht das Maximum für jede unterstützungsbedürftige Person, für die ein Unterstützungsabzug zusteht (zh-form-365-2025__c0002, zh-wl-2025__c0091).
> - **Staatssteuer:** Das Maximum steigt um CHF 1'300 (Code 614).
>   - Mit Beiträgen an die 2. Säule oder 3a: 2'900 + 1'300 = **CHF 4'200**.
>   - Ohne solche Beiträge: 4'350 + 1'300 = **CHF 5'650**.
> - **Bundessteuer:** Es gibt keinen Zuschlag von CHF 700 (Code 615), weil kein Bundes-Unterstützungsabzug zusteht. Das Maximum bleibt bei **CHF 1'800** (mit 2./3a) bzw. **CHF 2'700** (ohne).
>   - Läge die Unterstützung bei 6'800 oder mehr, wären es 1'800 + 700 = 2'500.
> 
> Der Zuschlag ist nur ein höherer Maximalbetrag. Abziehbar bleibt das Minimum aus den bezahlten Prämien (Teil A) und dem Maximum (Teil B). Er hilft also nur, wenn die Prämien das Grundmaximum übersteigen.
> 
> **Offen**
> - Die Erwerbsunfähigkeit und Bedürftigkeit der Mutter müssen belegt sein.
> - Ob die Mandantin 2./3a-Beiträge geleistet hat, bestimmt die Ziff.-15-Variante.
> - Ich habe nicht geprüft, ob der Bundesabzug über andere Wege erreichbar wäre. Falls die Unterstützung auf 6'800 oder mehr erhöht wird, gilt die Bundesregel.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## p04

**Frage:** SG 2025: Nettoeinkommen gemäss Ziffer 20 CHF 80'000. Arzt- und Zahnarztrechnungen 2025 brutto CHF 6'200, davon von der Krankenkasse vergütet CHF 1'700. Wo werden die Kosten deklariert und wie hoch ist der Abzug für die Staats- und Gemeindesteuern bzw. für die direkte Bundessteuer (Annahme: massgebendes Nettoeinkommen Bund ebenfalls CHF 80'000)?

**Soll (Referenz):** Formular 6 (Rückseite «Krankheits-, Unfall- und behinderungsbedingte Kosten»): Bruttobetrag 6'200 abzüglich Beiträge Dritter 1'700 = selbst getragene Kosten CHF 4'500 -> Steuererklärung Seite 3, Vorkolonne Ziff. 21.1 (Code 650). Kanton SG: Selbstbehalt 2% des Nettoeinkommens (Ziff. 20) = 2% x 80'000 = 1'600 (Code 238) -> Abzug Code 240 = CHF 2'900. Bund: Selbstbehalt 5% (Art. 33 Abs. 1 lit. h DBG; Merkblatt 32) = 4'000 -> Abzug CHF 500. Das SG-Formular hat nur eine Spalte; die Abweichung für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor.

**Antwort des Agenten** (26.4 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne, steuerwiki__zeige):

> SG · Steuerjahr 2025
> 
> **Wo deklarieren**
> - Die Einzelrechnungen (Datum, Arzt/Zahnarzt, Bruttobetrag, abzüglich Beiträge Dritter, selbst getragene Kosten) gehören auf die Rückseite von Formular 6 («Krankheits- und Unfallkosten»).
> - Das Total der selbst getragenen Kosten kommt in die Vorkolonne von Ziffer 21.1 «Krankheits- und Unfallkosten» im Hauptformular 1 (Code 650). Der Selbstbehalt hat Code 238, der Abzug Code 240.
> - Das Formular hat nur eine Spalte. Einen separaten Bundesbetrag gibt es nicht. Die Steuerbehörde rechnet den Bundesabzug automatisch (Merkblatt 32, sg-wl-2025__c0173).
> - Krankenkassenprämien gehören nicht hierher, sondern in Ziffer 14.
> 
> **Berechnung**
> Abziehbar sind nur die tatsächlich selbst getragenen Kosten, also brutto minus die Vergütung der Krankenkasse.
> 
> | | Staats-/Gemeindesteuer | Direkte Bundessteuer |
> |---|---|---|
> | Selbst getragene Kosten (6'200 − 1'700) | 4'500 | 4'500 |
> | Selbstbehalt auf CHF 80'000 | 2 % = 1'600 | 5 % = 4'000 |
> | **Abzug** | **CHF 2'900** | **CHF 500** |
> 
> Die Zahlen sind mit dem Rechentool gerechnet.
> 
> **Quellen**
> - Kanton: Art. 46 StG SG, «diese 2 Prozent der Nettoeinkünfte übersteigen» (sg-stg-2025__art-46); Formular 1, Ziffer 21.1 (sg-form-1-2025__c0010); Formular 6 (sg-form-6-2025__c0003). Status ☑️ agent-geprüft (Abnahme offen).
> - Bund: Art. 33 Abs. 1 lit. h DBG, 5 % der um die Aufwendungen nach Art. 26–33 verminderten steuerbaren Einkünfte (bund-dbg-2025__art-33-t3). Status ☑️ agent-geprüft (Abnahme offen).
> 
> **Vorbehalte**
> - Als Basis für den Bund habe ich wie von dir angenommen CHF 80'000 verwendet. Nach dem Gesetzeswortlaut ist die Basis die um die Aufwendungen (Art. 26–33) verminderten Einkünfte. Der tatsächliche Bundesabzug hängt also davon ab, dass dieses Bundes-Nettoeinkommen wirklich bei CHF 80'000 liegt.
> - Arzt- und Zahnarztrechnungen müssen nur auf Verlangen eingereicht werden. Verweist du im Formular 6 aber auf einen Krankenkassenauszug oder dessen Total, musst du die detaillierte Leistungsübersicht beilegen (sg-form-6-2025__c0003).
> - Gehören behinderungsbedingte Kosten oder eine Diätpauschale dazu, werden sie anders behandelt. Behinderungsbedingte Kosten kommen ohne Selbstbehalt in Ziffer 21.2.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## p05

**Frage:** SG 2025: Mandant gewinnt im Swiss Lotto (interkantonal durchgeführte Lotterie = Grossspiel) einen Einzelgewinn von CHF 1'500'000. Wo wird der Gewinn deklariert, welcher Teil ist steuerbar und welche Einsatzkosten sind abziehbar – Kanton und Bund getrennt?

**Soll (Referenz):** Deklaration im Wertschriften- und Guthabenverzeichnis (Formular 2), Spalte A (Bargewinn aus inländischer Lotterie, verrechnungssteuerpflichtig); Übertrag Ziff. 4.1 (Code 146). Kanton SG: Einzelgewinne aus Grossspielen steuerbar, soweit > Fr. 1'069'800 -> 1'500'000 - 1'069'800 = CHF 430'200 steuerbar; Einsatzkosten unter Ziff. 16.1 (Code 220): 5%, höchstens Fr. 5'400 -> CHF 5'400; netto CHF 424'800. Bund: steuerfrei bis CHF 1'070'400 (Art. 24 lit. ibis DBG) -> steuerbar CHF 429'600; Einsatzkosten 5%, höchstens CHF 5'400 (Art. 33 Abs. 4 DBG) -> CHF 5'400; netto CHF 424'200. (Der Höchstbetrag 5'400 greift unabhängig davon, ob 5% vom Gesamt- oder vom steuerbaren Gewinn gerechnet werden.)

**Antwort des Agenten** (45.0 s · Tools: 15 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne):

> **SG · Steuerjahr 2025: Swisslos-Lotto-Gewinn CHF 1'500'000 (Grossspiel)**
> 
> **Wo deklariert**
> - Der Gewinn kommt ins Formular 2 (Wertschriften- und Guthabenverzeichnis), Spalte A (mit Verrechnungssteuer). Er wird dort mit der Lotto-Gewinnbescheinigung belegt (sg-form-2-2025__c0004, ☑️).
> - Das Total geht in Formular 1, Ziff. 4.1 (Code 146), Einkünfte aus Wertschriften und Guthaben inkl. Lotterie-/Geldspielgewinne.
> - Es gibt keine separate Bundesspalte. Die Steuerbehörde nimmt die Anpassungen für die direkte Bundessteuer automatisch vor (sg-wl-2025__c0173, Merkblatt 32).
> - Die Einsatzkosten gehören in Ziff. 16.1 (Code 220).
> 
> **Steuerbarer Teil**
> 
> Einzelne Gewinne aus Grossspielen sind bis zu einer Grenze steuerfrei. Steuerbar ist nur der Teil über der Grenze («soweit > Fr. 1'069'800», sg-wl-2025__c0064 und c0134). Der Gewinn wird also nicht ganz steuerbar, wenn er die Grenze überschreitet. Das Wiki sagt das nur über diese Wegleitungsformulierung, einen ausdrücklichen Freibetrag-Satz habe ich nicht gefunden.
> 
> | | Kanton SG | Bund (DBG) |
> |---|---|---|
> | Gewinn | 1'500'000 | 1'500'000 |
> | Steuerfrei bis | 1'069'800 (Art. 37 lit. o StG SG, sg-stg-2025__art-37-t3, ☑️) | 1'070'400 (Art. 24 lit. ibis DBG, bund-dbg-2025__art-24-t3, ☑️) |
> | **Steuerbarer Gewinn** | **430'200** | **429'600** |
> 
> Die Grenzen sind verschieden, deshalb weichen die steuerbaren Beträge um CHF 600 voneinander ab.
> 
> **Abziehbare Einsatzkosten**
> - Abziehbar sind 5 % der einzelnen steuerbaren Gewinne, höchstens CHF 5'400 (Art. 45 Abs. 3 StG SG, sg-stg-2025__art-45-t5; Art. 33 Abs. 4 DBG, bund-dbg-2025__art-33-t7). Das gilt für Kanton und Bund gleich.
> - 5 % von 430'200 sind 21'510 (Kanton), 5 % von 429'600 sind 21'480 (Bund). Beide Beträge liegen über dem Höchstbetrag. Es gilt deshalb in beiden Fällen die Kappung auf **CHF 5'400**. Das gilt auch, wenn man 5 % vom ganzen Gewinn rechnet.
> - Die höheren Online-Limiten (SG CHF 26'700, Bund CHF 26'800) betreffen nur Online-Spielbankenspiele. Sie gelten hier nicht (Formular 32 SG 2025, sg-form-32-2025__c0004).
> - Die Abzugsfähigkeit hängt nicht davon ab, ob der Mandant tatsächlich Spielkosten hatte. Der Abzug ist eine Pauschale in dieser Höhe.
> 
> **Ergebnis**
> 
> | | Kanton SG | Bund |
> |---|---|---|
> | Steuerbarer Gewinn | 430'200 | 429'600 |
> | − Einsatzkosten | 5'400 | 5'400 |
> | **Netto im Einkommen** | **424'800** | **424'200** |
> 
> Die Zahlen sind mit `rechne` gerechnet. Der Status der Werte ist ☑️ agent-geprüft: Die Fundstellen sind geprüft, die Abnahme ist offen.
> 
> **Offene Punkte**
> - Zur Verrechnungssteuer auf Geldspielgewinne verweist Art. 6 VStG auf die steuerbaren Gewinne. Satz, Bemessungsgrundlage und Rückforderung habe ich nicht geprüft, sie gehören zur Fachperson.
> - Die Gewinnbescheinigung von Swisslos muss vorliegen (SG: Einreichung bedingt, bei deklarierten steuerbaren bzw. VSt-belasteten Gewinnen).
> - Bei mehreren Einzelgewinnen wird die Grenze je Gewinn angewendet, nicht auf die Summe.
> - Die fachliche Beurteilung bleibt bei der Fachperson.

## p06

**Frage:** SG 2025: Ehepaar mit zwei Kindern, für deren Unterhalt es zur Hauptsache aufkommt: Kind A ist 2-jährig (noch nicht schulpflichtig), Kind B ist 20 und studiert. Für Kind B selbst getragene Ausbildungskosten (Semestergebühren, Bücher, ÖV zum Studienort) CHF 9'500, erhaltenes Stipendium CHF 1'000. Welche Ziffern/Codes und welche Beträge – Kanton und Bund?

**Soll (Referenz):** Kanton SG (Steuererklärung Seite 3, Ziff. 23): Kind A -> Ziff. 23.1 (Code 252) Fr. 7'600; Kind B -> Ziff. 23.2 (Code 254) Fr. 10'800; Ausbildungskosten Kind B -> Ziff. 23.3 (Code 256, Formular 10): 9'500 - 1'000 Stipendium - 3'200 Selbstbehalt = CHF 5'300 (unter dem Maximum von Fr. 13'700). Total Kinderabzüge Kanton CHF 23'700. Bund: einheitlicher Kinderabzug CHF 6'800 pro Kind (Art. 35 Abs. 1 lit. a DBG), kein Abzug für Ausbildungskosten -> 2 x 6'800 = CHF 13'600 (Anpassung durch die Steuerbehörde, Merkblatt 32).

**Antwort des Agenten** (34.9 s · Tools: 7 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__zeige, steuerwiki__rechne):

> **SG · Steuerjahr 2025** – Kinderabzüge für Kind A (2-jährig) und Kind B (20, im Studium)
> 
> Im SG-Formular gibt es nur eine Spalte. Die Bundesbeträge setzt die Steuerbehörde automatisch ein (sg-wl-2025__c0173). Deshalb habe ich sie unten separat ausgewiesen.
> 
> | Ziff. / Code | Was | Kanton | Bund |
> |---|---|---|---|
> | **23.1 / Code 252** | Kind A, noch nicht schulpflichtig (1 × 7'600) | **7'600** | 6'800 (einheitlich pro Kind) |
> | **23.2 / Code 254** | Kind B, in Ausbildung und volljährig, Hauptunterhalt (1 × 10'800) | **10'800** | 6'800 (einheitlich pro Kind) |
> | **23.3 / Code 256** | Ausbildungskosten Kind B, mit Formular 10 | **5'300** | **kein Abzug** |
> | | **Total Kinder- und Ausbildungsabzug** | **23'700** | **13'600** |
> 
> Quellen: sg-form-1-2025__c0011, sg-wl-2025__c0104, sg-wl-2025__c0105, sg-form-32-2025__c0006. Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Rechnung Ziff. 23.3 (nur Kanton)**
> - Kosten 9'500 − Stipendium 1'000 − Selbstbehalt 3'200 = **5'300**.
> - Die Obergrenze von 13'700 greift nicht.
> - Das Total von 23'700 ist mit `rechne` gerechnet.
> - Der Abzug gilt nur, weil für Kind B der Abzug nach Ziff. 23.2 geltend gemacht wird.
> - Semestergebühren, Bücher und ÖV zum Studienort sind abzugsfähig. Fahrkosten gelten nur mit öffentlichen Verkehrsmitteln.
> - Beilegen: Formular 10, die Rechnungen und die Stipendienverfügung.
> 
> **Bund**
> - Der Bund kennt 6'800 pro Kind, ohne Unterscheidung nach Vorschul-, Schul- oder Ausbildungsalter. Das ergibt 2 × 6'800 = **13'600**.
> - Die Ausbildungskosten von 9'500 sind beim Bund nicht abziehbar. Das Merkblatt 32 führt für Ziff. 23.3 beim Bund «–».
> - Zusätzlich gibt es einen Abzug vom Steuerbetrag (nicht vom Einkommen): **max. Fr. 263 pro Kind** im gleichen Haushalt, bei 2 Kindern höchstens **526**. Er hängt vom errechneten Steuerbetrag ab (sg-form-32-2025__c0006). Wohnt Kind B am Studienort in einem eigenen Haushalt, entfällt dieser Abzug für Kind B. Das habe ich nicht geklärt.
> - Für das Ehepaar gilt beim Bund ausserdem der Verheiratetenabzug von 2'800 (Ziff. 24).
> 
> **Nicht geprüft:** Kinderbetreuungskosten (Ziff. 16.2) für Kind A, weil dazu keine Angaben vorliegen. Ob das Stipendium für sich steuerfrei ist, habe ich nicht geprüft.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## p07

**Frage:** TG 2025: Arbeitnehmer fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 22 km einfach, Hin- und Rückfahrt täglich, 225 Arbeitstage, keine weiteren Fahrkosten, kein Geschäftsfahrzeug. Wie wird Formular 4.2 Ziff. 2.3–2.5 für Staats- und Bundessteuer ausgefüllt und was geht in die Steuererklärung?

**Soll (Referenz):** Formular 4.2 Ziff. 2.3: 44 km/Tag x 225 Tage = 9'900 km pro Jahr (Code 211). Staatssteuer, Auto-Ansätze nach Jahreskilometern gestaffelt: 3'000 km x 0.60 = 1'800; 2'000 km x 0.50 = 1'000; 4'900 km x 0.40 = 1'960 -> CHF 4'760. Bundessteuer einheitlich CHF 0.70/km: 9'900 x 0.70 = CHF 6'930. Ziff. 2.4 Total effektive Fahrkosten (Code 212): Staat 4'760 / Bund 6'930. Ziff. 2.5 Total abzugsfähige Fahrkosten (Code 213): Staat max. 6'000 -> CHF 4'760; Bund max. 3'300 -> CHF 3'300. Über Ziff. 7 Total Berufsauslagen (Code 240) in Steuererklärung Seite 3, Ziff. 10.1 (linke Spalte Staat, rechte Spalte Bund).

**Antwort des Agenten** (32.7 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne, steuerwiki__zeige):

> **TG · Steuerjahr 2025 – Formular 4.2, Ziff. 2.3–2.5 (Privatauto, Arbeitsweg 22 km einfach, 225 Tage)**
> 
> **Voraussetzung:** Das Privatauto ist nur in begründeten Ausnahmefällen abziehbar, etwa wenn der ÖV unzumutbar ist (Zeitersparnis über 1 Stunde pro Arbeitstag). Sonst wären nur die ÖV-Abokosten abziehbar. Dieser Fall erfüllt die Voraussetzung. Es steht kein Geschäftsfahrzeug zur Verfügung (Ziff. 1.2 = nein, Lohnausweis Feld F nicht angekreuzt). Quellen: tg-wl-2025__c0003, tg-form-04-2-2025__c0001 (☑️ agent-geprüft).
> 
> **Ziff. 2.3 – Kosten für privates Motorfahrzeug**
> - Ankreuzen: «Auto».
> - Arbeitsweg: Wohnadresse bis Arbeitsort eintragen.
> - km pro Tag: 22 × 2 = **44 km**.
> - Anzahl Tage: **225** (bei 100 %-Pensum in der Regel maximal 225).
> - km pro Jahr: 44 × 225 = **9'900 km**. Das gilt für beide Spalten, es ist dieselbe Kilometerzahl (Code 211).
> 
> Der Betrag wird je Spalte mit anderem Ansatz berechnet (Rechnung mit `rechne` geprüft):
> 
> | | Staatssteuer (linke Spalte) | Bundessteuer (rechte Spalte) |
> |---|---|---|
> | Ansatz | gestaffelt: 0.60 / 0.50 / 0.40 | einheitlich 0.70 |
> | Rechnung | 3'000 × 0.60 = 1'800 + 2'000 × 0.50 = 1'000 + 4'900 × 0.40 = 1'960 | 9'900 × 0.70 |
> | **Betrag** | **CHF 4'760** | **CHF 6'930** |
> 
> Die Parkgebühren sind in den Kilometeransätzen enthalten. Quellen: tg-bkv__par-1, bund-bkv-2025__anhang-1.
> 
> **Ziff. 2.4 – Total effektive Fahrkosten (Ziff. 2.1–2.3, Code 212)**
> Es gibt keine weiteren Fahrkosten (kein ÖV-Abo und kein Velo), daher gilt:
> - Staat: **CHF 4'760**
> - Bund: **CHF 6'930**
> 
> **Ziff. 2.5 – Total abzugsfähige Fahrkosten (Code 213)**
> Hier gilt die Begrenzung: Staat höchstens CHF 6'000, Bund höchstens CHF 3'300.
> - Staat: min(4'760; 6'000) = **CHF 4'760** (Maximum nicht erreicht)
> - Bund: min(6'930; 3'300) = **CHF 3'300** (auf das Maximum gekürzt)
> 
> Quelle: tg-form-04-2-2025__c0002, tg-stp-29-2__c0006.
> 
> **Was in die Steuererklärung geht**
> - Die Beträge aus Ziff. 2.5 fliessen in Formular 4.2 Ziff. 7 (Code 240) ein, zusammen mit den übrigen Berufsauslagen: Verpflegung (Ziff. 3), übrige Berufskosten (Ziff. 4, 3 % des Nettolohns, mindestens CHF 2'000 und höchstens CHF 4'000), Wochenaufenthalt (Ziff. 5) und Nebenerwerb (Ziff. 6).
> - Der Übertrag von Ziff. 7 geht in die Steuererklärung, Seite 3, **Ziff. 10.1** (Person 1), Staat links und Bund rechts. Quelle: tg-form-01-2025__c0010.
> - Für Staat und Bund entsteht so je eine eigene Zahl, weil die Ansätze und die Maxima verschieden sind. Das Wiki führt für den Bund keine Arbeitstage-Regel, die 225-Tage-Angabe gilt dort nicht gesondert. Die Kilometerzahl ist hier trotzdem für beide Spalten gleich.
> - Dem Formular ist der Lohnausweis beizulegen. Ob der Fahrzeugausweis bzw. ein Nachweis zur Zeitersparnis eingereicht werden muss, ist im Wiki als «unklar» geführt (tg-wl-2025__c0179). Ich würde die Begründung (Zeitersparnis über 1 Stunde) sicherheitshalber bereithalten.
> 
> **Vorbehalt:** Die Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die fachliche Beurteilung, ob die Zeitersparnis den Ausnahmefall tatsächlich begründet, liegt bei der Fachperson.

## p08

**Frage:** TG 2025: Ehepaar bewohnt sein eigenes Einfamilienhaus am Wohnsitz selbst (Baujahr 1995, nicht landwirtschaftlich geschätzt, keine Mieteinnahmen). Indexierter Mietwert aus Selbstnutzung 2025 CHF 21'000; Unterhalt pauschal. Wie werden Eigenmietwert und Nettoerfolg im Formular 7 berechnet und wohin übertragen – Staat und Bund?

**Soll (Referenz):** Formular 7, Zeile «Mietwert selbstgenutzt» 21'000 (beide Spalten). Selbstnutzungsabzug: Staat 40% = 8'400, Bund 20% = 4'200 -> steuerbarer Eigenmietwert (= Bruttoertrag) Staat CHF 12'600, Bund CHF 16'800. Pauschalabzug Unterhalt: Gebäude älter als 10 Jahre -> 20%, berechnet vom steuerbaren Eigenmietwert: Staat 2'520, Bund 3'360. Nettoerfolg: Staat CHF 10'080, Bund CHF 13'440 (bei selbstgenutzter Liegenschaft je Spalte separat ermitteln). Total Nettoerfolge (Code 180) -> Steuererklärung Seite 2, Ziff. 8, Spalte Staat bzw. Bund.

**Antwort des Agenten** (31.5 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne, steuerwiki__zeige):

> **TG · Steuerjahr 2025: Eigenmietwert und Nettoerfolg im Formular 7**
> 
> **Ausgangslage:** Das Einfamilienhaus wird am Wohnsitz selbst bewohnt. Es gibt keine landwirtschaftliche Schätzung und keine Mieteinnahmen. Der indexierte Mietwert aus Selbstnutzung beträgt CHF 21'000. Das Gebäude ist Baujahr 1995, also älter als 10 Jahre, damit gilt die Unterhaltspauschale von 20 %.
> 
> **Berechnung (rechne-Tool)**
> 
> | Schritt | Staat (linke Spalte) | Bund (rechte Spalte) |
> |---|---|---|
> | Mietwert aus Selbstnutzung (indexiert, Form. 7) | 21'000 | 21'000 |
> | Selbstnutzungsabzug | 40 % = 8'400 | 20 % = 4'200 |
> | **Steuerbarer Eigenmietwert** | **12'600** | **16'800** |
> | Mieterträge | 0 | 0 |
> | Bruttoertrag | 12'600 | 16'800 |
> | Unterhalt pauschal 20 % vom steuerbaren Eigenmietwert | 2'520 | 3'360 |
> | **Nettoerfolg** | **10'080** | **13'440** |
> 
> **Ablauf im Formular**
> 1. **Formular 7, Angaben zur Liegenschaft:** Gemeinde, Baujahr 1995, Steuerwert und Amtsnummer eintragen. Die Checkbox «Am Wohnsitz selbstgenutzt» ankreuzen. Den Mietwert aus Selbstnutzung (21'000) aus der Liegenschaftensteuerrechnung bzw. dem Schätzungsprotokoll übernehmen.
> 2. **Selbstnutzungsabzug:** Staat 40 %, Bund 20 %. Das ergibt den steuerbaren Eigenmietwert je Spalte (12'600 bzw. 16'800).
> 3. **Unterhalt:** Pauschale wählen, kein Formular 8 nötig. Die Wahl gilt pro Liegenschaft und Jahr. Die Pauschale beträgt 20 %, weil das Gebäude über 10 Jahre alt ist. Berechnungsbasis ist der steuerbare Eigenmietwert.
> 4. **Nettoerfolg:** Bruttoertrag minus Unterhalt, für Staat und Bund getrennt rechnen.
> 5. **Übertrag in Formular 1:** Das Total der Nettoerfolge von Formular 7 (Code 180) kommt in Ziff. 8.1 «Einkünfte aus Liegenschaften», links 10'080 (Staat), rechts 13'440 (Bund).
> 6. **Vermögen:** Der Steuerwert aus Formular 7 geht über das Total (Code 430) in Ziff. 31 «Liegenschaften». Das ist nicht Teil der Einkommensberechnung, muss aber mit ausgefüllt werden.
> 
> **Hinweise**
> - **Gebäudealter beim Bund:** Der Bund stellt auf den Beginn der Steuerperiode ab, der Kanton auf das Ende. Bei Baujahr 1995 ändert sich dadurch nichts. Beide Stichtage liegen über 10 Jahren, also 20 % (tg-stv__par-9, bund-lkv__art-5).
> - **Pauschale oder effektive Kosten:** Wer die Pauschale wählt, beziffert den Unterhalt nicht einzeln. Effektive Kosten wären nur dann sinnvoll, wenn sie über 2'520 (Staat) bzw. 3'360 (Bund) lägen. Die Wahl kann nicht nur für Staat oder nur für Bund getroffen werden, das ist aus den Quellen nicht ausdrücklich belegt. Hier gilt die Pauschale in beiden Spalten.
> - **Bund 20 %:** Der Selbstnutzungsabzug von 20 % beim Bund ist in der TG-Wegleitung geregelt. Das DBG selbst kennt keinen festen Prozentsatz, der Eigenmietwert wird im kantonalen Verfahren festgesetzt.
> 
> **Fundstellen (Status ☑️ agent-geprüft, Abnahme offen)**
> - Selbstnutzungsabzug 40 % / 20 %: tg-wl-2025__c0225, tg-stg__par-23
> - Pauschale 10 % / 20 %: tg-stv__par-9, bund-lkv__art-5, tg-wl-2025__c0238
> - Formularfelder: tg-form-07-2025__c0002
> - Übertrag Ziff. 8.1, Code 180: tg-form-01-2025__c0009
> 
> Die 21'000 sind als gegeben angenommen. Nicht geprüft habe ich sie gegen die tatsächliche Liegenschaftensteuerrechnung. Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## p09

**Frage:** AR 2025: Ehepaar, beide unabhängig voneinander unselbständig erwerbstätig. Das niedrigere Erwerbseinkommen (Nettolohn der Ehefrau abzüglich Berufskosten, Säule-3a-Beiträge und BVG-Einkäufe) beträgt CHF 38'000. Wie hoch ist der Zweiverdienerabzug in Ziffer 17 für die Staats- und Gemeindesteuer und für die direkte Bundessteuer?

**Soll (Referenz):** Ziff. 17 Zweiverdienerabzug. Kanton AR: 10% des niedrigeren Erwerbseinkommens, mind. Fr. 2'500, max. Fr. 5'200 (Beträge gemäss Anhang 1 StG indexiert per 1.1.2024; Art. 35 Abs. 1 lit. h StG nennt die Basisbeträge 2'400/5'000) -> 10% x 38'000 = CHF 3'800. Bund: Art. 33 Abs. 2 DBG 50% des niedrigeren Erwerbseinkommens, mind. 8'600, max. 14'100 -> 50% x 38'000 = 19'000 -> begrenzt auf CHF 14'100. Die Abweichung für die direkte Bundessteuer wird von der Steuerverwaltung automatisch vorgenommen.

**Antwort des Agenten** (23.9 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **AR · Steuerjahr 2025 – Ziffer 17 Zweiverdienerabzug** (niedrigeres Erwerbseinkommen E = CHF 38'000)
> 
> | | Regel | Rechnung | Abzug |
> |---|---|---|---|
> | **Staats- und Gemeindesteuer** | 10 % × E, mindestens 2'500, höchstens 5'200 | 10 % × 38'000 = 3'800 (liegt zwischen 2'500 und 5'200) | **CHF 3'800** |
> | **Direkte Bundessteuer** | 50 % × E, mindestens 8'600, höchstens 14'100 | 50 % × 38'000 = 19'000 → auf Maximum begrenzt | **CHF 14'100** |
> 
> **Fundstellen** (Status ☑️ agent-geprüft, Abnahme offen):
> - Kanton: `ar-stg__art-35-t3` (10 %), `ar-stg-anhang-kp__c0001` (Min. 2'500 / Max. 5'200, indexiert per 1.1.2024), `ar-wl-2025__c0004`.
> - Bund: `bund-dbg-2025__art-33-t6` (Art. 33 Abs. 2 DBG: 50 %, mind. 8'600, höchstens 14'100).
> 
> **Hinweise:**
> - Das AR-Formular hat keine eigene Bundesspalte. In Ziffer 17 gehört der kantonale Betrag von CHF 3'800. Der Bundesabzug von CHF 14'100 wird von der Steuerverwaltung automatisch vorgenommen (`ar-wl-2025__c0179`).
> - Die CHF 38'000 müssen das Erwerbseinkommen nach Berufskosten, Säule 3a und BVG-Einkäufen sein. Das haben Sie so angegeben.
> - Der Code für Ziffer 17 ist im Wiki nicht verifiziert, weil Seite 3 der Steuererklärung in der Wegleitung nicht abgebildet ist. Die Ziffer selbst stimmt.
> - Die fachliche Beurteilung bleibt bei der Fachperson.

## p10

**Frage:** AR 2025: Mandant bewohnt sein Einfamilienhaus am Wohnsitz dauernd selbst (Baujahr 1995, einzige Liegenschaft, keine Fremdvermietung). Mietwert gemäss Grundstückschätzung CHF 24'500; er wählt den Pauschalabzug für den Unterhalt. Was wird wo im Formular 7 und in der Steuererklärung (Staats- und Gemeindesteuer) eingetragen?

**Soll (Referenz):** Formular 7, Teil B.a: Eigenmietwert 24'500 abzüglich Selbstnutzungsabzug 20% (4'900) = Total anrechenbarer Eigenmietwert CHF 19'600 = Total Erträge a. und b. -> Übertrag Steuererklärung Seite 2, Ziff. 5. Teil C: Pauschalabzug (Gebäude über 10 Jahre; Bruttomietertrag des gesamten Liegenschaftsbesitzes nicht über Fr. 100'000) = 20% vom Total Liegenschaftserträge = 20% x 19'600 = CHF 3'920 -> Übertrag Steuererklärung Seite 3, Ziff. 15 (separater Abzug, nicht mit Ziff. 5 verrechnet). Wirkung auf das Einkommen netto CHF 15'680.

**Antwort des Agenten** (38.7 s · Tools: 11 Aufrufe steuerwiki__position, steuerwiki__beleg, steuerwiki__zeige, steuerwiki__suche, steuerwiki__rechne):

> **AR · Steuerjahr 2025 (Staats- und Gemeindesteuer)**
> 
> Das AR-Formular hat keine Bundesspalte. Die Steuerverwaltung nimmt die Abweichungen für die direkte Bundessteuer automatisch vor (ar-wl-2025__c0179). Wie der Bund Eigenmietwert und Pauschale behandelt, ist in den AR-Quellen nicht belegt, deshalb sage ich dazu nichts.
> 
> ## Formular 7 (eine Liegenschaft, also kein Formular 7Z)
> 
> **A. Angaben zur Liegenschaft**
> - Baujahr 1995, Nutzung «am Wohnsitz dauernd selbst bewohnt», Anteil 100 %.
> - Steuerwert (Verkehrswert) aus der amtlichen Grundstückschätzung. Diesen Betrag haben Sie nicht genannt, er fehlt noch (ar-form-07-2025__c0001).
> 
> **B. Erträge**
> 
> | Zeile | Betrag CHF |
> |---|---|
> | a. Eigenmietwert (Mietwert gemäss Grundstückschätzung) | 24'500 |
> | abzüglich 20 % Selbstnutzungsabzug | − 4'900 |
> | **Total anrechenbarer Eigenmietwert** | **19'600** |
> | b. Fremdnutzung und Leistungen Dritter | 0 (keine Vermietung) |
> | **Total Erträge a. und b.** | **19'600** |
> 
> - Der 20 %-Abzug gilt nur für die am Wohnsitz dauernd selbst bewohnte Liegenschaft (ar-wl-2025__c0166, ar-form-07-2025__c0002). Das trifft hier zu.
> - Es gibt keine nicht erfassten Um- oder Anbauten. Sonst käme ein Zuschlag von 2.8 % der Aufwendungen zum Mietwert dazu. Falls es solche seit der letzten Schätzung gab, bitte nachprüfen.
> 
> **C. Unterhalts- und Verwaltungskosten**
> - «Pauschalabzug der Erträge (B)» ankreuzen (C1).
> - Das Gebäude ist 30 Jahre alt, also über 10 Jahre. Der Satz beträgt 20 % von Total Erträge (ar-wl-2025__c0175).
> - 20 % × 19'600 = **CHF 3'920**.
> - Als Basis gilt der Eigenmietwert nach dem 20 %-Abzug. Das zeigt das Muster der Wegleitung: 26'000 → 5'200 → 20'800, Pauschale 4'160 = 20 % × 20'800 (ar-wl-2025__c0159, ar-wl-2025__c0160).
> - Die Rückseite (tatsächliche Kosten, C2) bleibt leer.
> - Die Pauschale ist nur zulässig, wenn der Bruttomietertrag des gesamten Liegenschaftsbesitzes höchstens CHF 100'000 beträgt und die Liegenschaft ganz oder vorwiegend Wohnzwecken dient. Beides trifft zu (ar-wl-2025__c0175).
> 
> ## Übertrag in die Steuererklärung (Formular 1)
> 
> Bei nur einer Liegenschaft wird direkt ab Formular 7 übertragen (ar-form-07-2025__c0002, c0003):
> 
> | Ziffer | Seite | Inhalt | CHF |
> |---|---|---|---|
> | **5** (Code 712) | S. 2 | Ertrag aus Liegenschaften: Total Erträge a. und b. | **19'600** |
> | **15** | S. 3 | Unterhalts- und Verwaltungskosten, Pauschalabzug | **3'920** |
> | **31** (Code 710) | S. 4 | Liegenschaften, Steuerwert gemäss Form. 7 Abschn. A | offen |
> 
> - Den Code 712 für Ziffer 5 und den Code 710 für Ziffer 31 geben die Wiki-Daten aus den Formular-Miniaturen der Wegleitung an. Für Ziffer 15 ist der Code nicht verifiziert.
> - Netto wirkt sich die Liegenschaft im Einkommen mit 19'600 − 3'920 = **CHF 15'680** aus.
> 
> ## Belege
> - Es gibt keine Beilagepflicht. Das Schätzungsprotokoll (Steuerwert und Mietwert) wird auf Verlangen vorgelegt (ar-wl-2025__c0156).
> - Handwerkerrechnungen sind bei der Pauschale nicht nötig. Die Pauschale deckt alle Unterhaltskosten ab. Die Rechnungskopien ab CHF 5'000 pro Einzelbetrag brauchen Sie nur bei effektiven Kosten (C2).
> 
> ## Zu beachten
> - Das Wahlrecht Pauschale oder effektive Kosten gilt pro Gebäude und Jahr. Es lohnt sich nur, wenn die tatsächlichen Kosten 2025 über CHF 3'920 liegen. Dann kämen Handwerker- und Versicherungsrechnungen in C2.
> - Alle Status der verwendeten Positionen sind ☑️ agent-geprüft. Die Abnahme durch die Fachperson ist offen.

