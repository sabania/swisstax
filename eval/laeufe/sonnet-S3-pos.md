# OpenClaw-Testlauf: positionstest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 10 · Lauf: 2026-11-09 18:29
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## p01

**Frage:** ZH 2025: Ledige unselbständig erwerbende Person, Nettolohn gemäss Lohnausweis CHF 92'000. Sie fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 23 km einfach, 2 Fahrten pro Tag, 220 Arbeitstage. Übrige Berufskosten werden pauschal geltend gemacht (keine Verpflegungskosten). Welche Positionen/Codes im Formular «Berufsauslagen» und welcher Betrag geht in Ziffer 11.1 – Staatssteuer und Bundessteuer getrennt?

**Soll (Referenz):** Formular 360 «Berufsauslagen» (Person 1), Begründung Privatauto Code 2042 (Zeitersparnis über 1 Stunde) ankreuzen. Ziff. 1.3 Auto (CHF 0.70/km, Staat und Bund gleich): 23 km x 2 Fahrten x 220 Tage = 10'120 km x 0.70 = CHF 7'084 (Code 204). Zwischentotal Fahrkosten Code 205: Staat max. CHF 5'200 -> 5'200; Bund max. CHF 3'300 -> 3'300. Ziff. 3 übrige Berufskosten pauschal Code 212: 3% von 92'000 = CHF 2'760 (innerhalb mind. 2'000 / höchstens 4'000; Staat und Bund gleich, vgl. BKV-Anhang). Total Berufsauslagen Code 220 -> Steuererklärung Seite 3, Ziff. 11.1: Staat 5'200 + 2'760 = CHF 7'960; Bund 3'300 + 2'760 = CHF 6'060.

**Antwort des Agenten** (34.2 s · Tools: 8 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__beleg, steuerwiki__zeige, steuerwiki__rechne):

> **ZH · Steuerjahr 2025 – Ziff. 11.1 (Berufsauslagen Person 1, Code 220)**
> 
> **Ergebnis**
> - **Staatssteuer: CHF 7'960**
> - **Bundessteuer: CHF 6'060**
> 
> Der Betrag kommt aus dem Formular 360 «Berufsauslagen» (Total Ziff. 6, Code 220) und wird in Ziff. 11.1 übertragen (zh-form-300-2025__c0007). Er steht in je einer Spalte für Staats- und Bundessteuer, und die beiden Beträge unterscheiden sich.
> 
> **Positionen im Form. 360 (Person 1)**
> 
> | Ziff. / Code | Eintrag | Staat | Bund |
> |---|---|---|---|
> | 1.3 Auto, Code 204 | 23 km × 2 × 220 Tage = 10'120 km × CHF 0.70 = CHF 7'084 | 7'084 | 7'084 |
> | Zwischentotal Fahrkosten, Code 205 | Plafond Kanton CHF 5'200, Bund CHF 3'300 | **5'200** | **3'300** |
> | 2 Verpflegung (206/208/210) | keine | – | – |
> | 3 Übrige Berufskosten pauschal, Code 212 | 3 % × 92'000 = 2'760 (Min. 2'000, Max. 4'000, also im Rahmen) | 2'760 | 2'760 |
> | **Total Berufsauslagen, Code 220 → Ziff. 11.1** | | **7'960** | **6'060** |
> 
> **Zusätzlich im Form. 360**
> - **Ziff. 7, Code 2042:** «Zeitersparnis von über 1 Stunde bei Benützung des privaten Motorfahrzeuges» ankreuzen (zh-form-360-2025__c0005). Ohne diese Begründung wird das Privatauto nicht akzeptiert.
> - **Code 213 (effektive übrige Kosten):** leer lassen. Die Pauschale (212) und die effektiven Kosten schliessen sich aus.
> 
> **Hinweise**
> - Der km-Abzug ist laut Form. 360 in der Regel auf 240 Arbeitstage begrenzt (zh-wl-2025__c0060). Die 220 Tage liegen darunter, die Begrenzung greift also nicht. Beim Bund gibt es keine solche Tagesregel.
> - Der Plafond greift hier in beiden Spalten, weil CHF 7'084 über 5'200 und über 3'300 liegen.
> - Wenn Feld F im Lohnausweis angekreuzt ist (z. B. Geschäftsfahrzeug oder Autopauschale), ist kein Fahrkostenabzug möglich.
> - Die Pauschale von 2'760 ist ein Jahreswert. Bei unterjähriger Erwerbstätigkeit prüft die Fachperson, ob der Bund eine Kürzung verlangt. Das ist beim Bund unter «Beachten» vermerkt. Die ZH-Position nennt dazu nichts.
> - Eine «ledige» Person ist Person 1, es gibt keine Codes für Person 2.
> 
> **Fundstellen und Status**
> 
> Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen):
> - Plafond Kanton CHF 5'200: zh-stg-2025__par-26
> - Plafond Bund CHF 3'300: bund-dbg-2025__art-26
> - CHF 0.70 pro km: zh-wl-2025__c0064 (Kanton) und bund-bkv-2025__anhang-1 (Bund)
> - Pauschale 3 %, Min. 2'000, Max. 4'000: zh-form-360-2025__c0004
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## p02

**Frage:** ZH 2025: Verheiratetes Paar, beide in einer Pensionskasse (2. Säule) versichert, zwei minderjährige Kinder mit Kinderabzug. Bezahlte Krankenkassenprämien 2025 (bereits netto nach individueller Prämienverbilligung) CHF 15'600, Sparzinsen gemäss Wertschriftenverzeichnis CHF 150. Wie wird das Formular «Versicherungsprämien» ausgefüllt und welcher Abzug kommt in Ziffer 15 (Staat / Bund)?

**Soll (Referenz):** Formular 365 «Versicherungsprämien»: Teil A: Code 601 Krankenversicherungsprämien 15'600 + Code 604 Sparzinsen 150 -> Total (A) Code 606 = CHF 15'750. Teil B (Maximum): Verheiratete mit Beiträgen an 2. Säule/3a Code 611: Staat 5'800 / Bund 3'700; Kinderzuschlag Code 613: Staat 2 x 1'300 = 2'600 / Bund 2 x 700 = 1'400 -> Total (B) Code 616: Staat CHF 8'400 / Bund CHF 5'100. Teil C Code 270 = der niedrigere Betrag von (A) und (B): Staat CHF 8'400, Bund CHF 5'100 -> Steuererklärung Seite 3, Ziff. 15 (Spalten Staatssteuer/Bundessteuer).

**Antwort des Agenten** (30.9 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__beleg, steuerwiki__rechne):

> **ZH · Steuerjahr 2025: Ziffer 15 (Code 270), Formular 365 «Versicherungsprämien»**
> 
> **Abzug in Ziffer 15**
> - **Staatssteuer: CHF 8'400** (Maximalabzug, tiefer als die bezahlten Prämien)
> - **Bundessteuer: CHF 5'100** (Maximalabzug, tiefer als die bezahlten Prämien)
> 
> Die bezahlten Prämien (CHF 15'750) liegen deutlich über beiden Maxima. Der Abzug ist deshalb in beiden Spalten auf das Maximum begrenzt. Der Betrag kommt in Ziffer 15 (Code 270), je eine Spalte für Staat und Bund.
> 
> **Teil A: bezahlte Prämien (gleich für Staat und Bund)**
> 
> | Zeile | Code | Betrag |
> |---|---|---|
> | Krankenkassenprämien, bereits netto nach Prämienverbilligung | 601 | 15'600 |
> | Zinsen von Sparkapitalien (Wertschriftenverzeichnis) | 604 | 150 |
> | Zwischentotal | 607 | 15'750 |
> | Erhaltene Prämienverbilligung (nicht erneut abziehen, da bereits in 601 netto) | 605 | 0 |
> | **Total A** | **606** | **15'750** |
> 
> Wenn die Prämienverbilligung direkt mit der Prämienrechnung verrechnet wurde, ist die um sie gekürzte Prämie einzutragen. Dann darf sie in Code 605 nicht nochmals abgezogen werden. Das gilt auch hier, weil die CHF 15'600 schon netto sind.
> 
> **Teil B: Maximalabzug (Code 616)**
> 
> Beide Ehegatten sind in der 2. Säule versichert. Es gilt also das Maximum «verheiratet, mit Beiträgen an 2. Säule/3a», nicht die höhere Variante «ohne 2./3a» (8'700 Staat / 5'550 Bund). Zusätzlich kommt der Zuschlag für zwei Kinder dazu.
> 
> | | Staat | Bund |
> |---|---|---|
> | Verheiratet, mit 2. Säule | 5'800 | 3'700 |
> | 2 Kinder (je 1'300 / je 700) | 2'600 | 1'400 |
> | **Total B** | **8'400** | **5'100** |
> 
> **Ergebnis:** Der kleinere Betrag aus A und B gilt, je Spalte.
> - Staat: CHF 8'400
> - Bund: CHF 5'100
> 
> **Hinweise**
> - Der Kinderzuschlag gilt für Kinder mit vollem Kinderabzug. Bei halbem Kinderabzug (geteilte Betreuung) wäre er je Kind nur CHF 650 (Staat) bzw. CHF 350 (Bund). Hier ist der volle Abzug angenommen.
> - Einreichung: Das Formular Versicherungsprämien ist der Steuererklärung beizulegen (Wegleitung S. 31). Die Prämienbelege selbst sind nur auf Verlangen einzureichen.
> - Prämien für Hausrat-, Motorfahrzeug- und Haftpflichtversicherungen gehören nicht in Teil A.
> - Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Fachperson nimmt sie ab.
> - Quellen:
>   - Formular: zh-form-300-2025__c0008
>   - Wegleitung: zh-wl-2025__c0082
>   - Staatssteuer-Maxima: zh-stg-2025__par-31-t2
>   - Bundessteuer-Maxima: bund-dbg-2025__art-33-t2 und bund-dbg-2025__art-33-t5

## p03

**Frage:** ZH 2025: Alleinstehende Mandantin unterstützt ihre erwerbsunfähige Mutter (eigener Haushalt, keine Alimente, kein Kinderabzug) nachweislich mit CHF 5'000 im Jahr 2025. In welcher Ziffer wird das geltend gemacht, welcher Abzug gilt bei der Staatssteuer und bei der Bundessteuer, und wirkt sich das auf den Versicherungsprämienabzug aus?

**Soll (Referenz):** Ziff. 24.2 «Abzug für unterstützte Personen» (Code 374); Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der Unterstützung beilegen. Staat: Voraussetzung Unterstützungsleistung mindestens CHF 2'800 -> 5'000 erfüllt -> Abzug CHF 2'800. Bund: Voraussetzung Unterstützungsleistung mindestens CHF 6'800 (Art. 35 Abs. 1 lit. b DBG) -> 5'000 < 6'800 -> kein Unterstützungsabzug (CHF 0). Folge im Formular 365 Teil B.3: Staat zusätzlicher Abzug CHF 1'300 für die unterstützungsbedürftige Person (Code 614); Bund kein Zuschlag von CHF 700 (Code 615), da kein Unterstützungsabzug zusteht.

**Antwort des Agenten** (37.1 s · Tools: 8 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne, steuerwiki__zeige, steuerwiki__suche):

> **ZH · Steuerjahr 2025**
> 
> **Ziffer:** Der Abzug gehört in **Ziff. 24.2 «Abzug für unterstützte Personen» (Code 374)**. Zusätzlich sind auf Seite 1 der Steuererklärung die Angaben zur unterstützten Person einzutragen: Name, Geburtsjahr, Adresse und der Unterstützungsbetrag pro Jahr. Der Mutter-Haushalt ist unerheblich, weil Ziff. 24.2 nur den Ausschluss von Ehegatten, Kindern mit Kinderabzug und Alimenten kennt.
> Quellen: zh-form-300-2025__c0010, zh-stg-2025__par-34, zh-wl-2025__c0134 (alle ☑️ agent-geprüft, Abnahme offen).
> 
> **Abzug Staatssteuer und Bundessteuer** (Rechnung mit dem Rechentool geprüft):
> - **Staatssteuer: CHF 2'800.** Die Unterstützung von CHF 5'000 liegt über dem Mindestbetrag von CHF 2'800. Abgezogen wird der feste Betrag, nicht die effektive Leistung.
> - **Bundessteuer: CHF 0.** Der Bundesabzug beträgt CHF 6'800 (Art. 35 Abs. 1 lit. b DBG, bund-dbg-2025__art-35). Er setzt voraus, dass mindestens in dieser Höhe unterstützt wird. Mit CHF 5'000 fehlen CHF 1'800.
> - Die Bundessteuer-Spalte in Ziff. 24.2 bleibt daher leer. Der Fall ist die Folge der unterschiedlichen Schwellen von Kanton und Bund.
> 
> **Einfluss auf den Versicherungsprämienabzug (Ziff. 15, Code 270):**
> Ja, aber nur beim Maximalabzug, und nur dort, wo der Unterstützungsabzug zusteht.
> - Im Form. 365 Teil B erhöht sich der Maximalabzug für jede unterstützungsbedürftige Person, für die der Unterstützungsabzug zusteht. Der Zuschlag beträgt **Staat CHF 1'300** und **Bund CHF 700** (zh-wl-2025__c0091).
> - Die Bundesspalte ist hier nicht gesichert, nur nach Wortlaut abgeleitet. Die Wegleitung knüpft den Zuschlag an «Unterstützungsabzug zusteht». Weil Ziff. 24.2 beim Bund mangels CHF 6'800 nicht zusteht, ist der Bundeszuschlag von CHF 700 nach dem Wortlaut nicht gegeben. Eine ausdrückliche Aussage dazu habe ich in den Quellen nicht gefunden.
> - Für eine alleinstehende Person mit 2./3a-Vorsorge ergibt sich: Der Maximalabzug (Teil B, Code 616) beträgt in der Staatssteuer CHF 2'900 + 1'300 = **CHF 4'200**. In der Bundessteuer bleibt er bei **CHF 1'800**, ohne Zuschlag. Für den Fall ohne 2./3a gelten CHF 4'350 (Kanton) bzw. CHF 2'700 (Bund) als Basis, jeweils zuzüglich Zuschlag.
> - Abgezogen wird weiterhin der niedrigere Betrag aus den bezahlten Prämien (Teil A) und dem Maximalabzug (Teil B). Der Zuschlag wirkt also nur, wenn die Mandantin mehr Prämien bezahlt hat, als das Basismaximum zulässt.
> 
> **Zu klären bzw. beizulegen:**
> - Die Bestätigung der Mutter über Art, Zeitpunkt und Höhe der Unterstützung ist mit der Steuererklärung einzureichen. Die Zahlungsbelege sind auf Verlangen vorzulegen.
> - Die Mutter muss unterstützungsbedürftig sein. Kantonal gilt dafür: Einkommen < CHF 15'000 und Vermögen < CHF 50'000 (ZStB 34.1). Das ist zu prüfen.
> - Ob die Mandantin 2./3a-Beiträge leistet, bestimmt die Basis beim Versicherungsabzug.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## p04

**Frage:** SG 2025: Nettoeinkommen gemäss Ziffer 20 CHF 80'000. Arzt- und Zahnarztrechnungen 2025 brutto CHF 6'200, davon von der Krankenkasse vergütet CHF 1'700. Wo werden die Kosten deklariert und wie hoch ist der Abzug für die Staats- und Gemeindesteuern bzw. für die direkte Bundessteuer (Annahme: massgebendes Nettoeinkommen Bund ebenfalls CHF 80'000)?

**Soll (Referenz):** Formular 6 (Rückseite «Krankheits-, Unfall- und behinderungsbedingte Kosten»): Bruttobetrag 6'200 abzüglich Beiträge Dritter 1'700 = selbst getragene Kosten CHF 4'500 -> Steuererklärung Seite 3, Vorkolonne Ziff. 21.1 (Code 650). Kanton SG: Selbstbehalt 2% des Nettoeinkommens (Ziff. 20) = 2% x 80'000 = 1'600 (Code 238) -> Abzug Code 240 = CHF 2'900. Bund: Selbstbehalt 5% (Art. 33 Abs. 1 lit. h DBG; Merkblatt 32) = 4'000 -> Abzug CHF 500. Das SG-Formular hat nur eine Spalte; die Abweichung für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor.

**Antwort des Agenten** (28.0 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne, steuerwiki__zeige):

> **SG · Steuerjahr 2025: Krankheits- und Unfallkosten**
> 
> **Wo deklarieren**
> - Die Einzelrechnungen gehören auf die Rückseite von Formular 6 (Hilfsblatt Krankheitskosten). Dort erfassen Sie Rechnungsdatum, Arzt/Zahnarzt, Bruttobetrag, Beiträge Dritter und die selbst getragenen Kosten.
> - Das Total der selbst getragenen Kosten kommt in die Vorkolonne von Ziff. 21.1 (Code 650). Der Selbstbehalt hat Code 238 und der Abzug Code 240.
> - SG hat nur eine Formularspalte. Es gibt keinen separaten Bundesbetrag. Die Steuerbehörde berechnet den Bundesabzug automatisch (Merkblatt 32, sg-wl-2025__c0173).
> - Nur die selbst getragenen Kosten sind abzugsfähig, also brutto abzüglich der Vergütung der Krankenkasse. Krankenkassenprämien gehören nicht hierher, sondern in Ziff. 14.
> - Die Belege müssen Sie nur auf Verlangen einreichen. Verweisen Sie im Formular 6 aber auf einen Krankenkassenzusammenzug, müssen Sie diesen mit der detaillierten Leistungsübersicht beilegen (sg-form-6-2025__c0003).
> 
> **Berechnung**
> 
> | | Staats- und Gemeindesteuer | Direkte Bundessteuer |
> |---|---|---|
> | Brutto Arzt/Zahnarzt | 6'200 | 6'200 |
> | − Vergütung Krankenkasse | −1'700 | −1'700 |
> | = selbst getragen (Vorkolonne Code 650) | 4'500 | 4'500 |
> | Selbstbehalt | 2% × 80'000 = 1'600 | 5% × 80'000 = 4'000 |
> | **Abzug** | **2'900** | **500** |
> 
> **Fundstellen und Status**
> - Kanton: Selbstbehalt 2% des Nettoeinkommens Ziff. 20 (sg-stg-2025__art-46, sg-form-1-2025__c0010). ☑️ agent-geprüft.
> - Bund: Selbstbehalt 5% der um die Aufwendungen (Art. 26–33 DBG) verminderten steuerbaren Einkünfte (Art. 33 Abs. 1 lit. h DBG, bund-dbg-2025__art-33-t3). ☑️ agent-geprüft.
> 
> **Vorbehalte**
> - Der Bundesabzug gilt nur unter Ihrer Annahme, dass das massgebende Nettoeinkommen Bund ebenfalls 80'000 beträgt. Die Behörde setzt das Nettoeinkommen Bund selbst fest. Weicht es ab, ändert sich der Selbstbehalt und damit der Abzug.
> - Die Rechnung geht davon aus, dass in den 6'200 nur Arzt- und Zahnarztrechnungen enthalten sind. Es gibt keine weiteren Vergütungen Dritter, und die Kosten sind nicht behinderungsbedingt. Behinderungsbedingte Kosten würden separat und ohne Selbstbehalt abgezogen (Ziff. 21.2).
> - Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## p05

**Frage:** SG 2025: Mandant gewinnt im Swiss Lotto (interkantonal durchgeführte Lotterie = Grossspiel) einen Einzelgewinn von CHF 1'500'000. Wo wird der Gewinn deklariert, welcher Teil ist steuerbar und welche Einsatzkosten sind abziehbar – Kanton und Bund getrennt?

**Soll (Referenz):** Deklaration im Wertschriften- und Guthabenverzeichnis (Formular 2), Spalte A (Bargewinn aus inländischer Lotterie, verrechnungssteuerpflichtig); Übertrag Ziff. 4.1 (Code 146). Kanton SG: Einzelgewinne aus Grossspielen steuerbar, soweit > Fr. 1'069'800 -> 1'500'000 - 1'069'800 = CHF 430'200 steuerbar; Einsatzkosten unter Ziff. 16.1 (Code 220): 5%, höchstens Fr. 5'400 -> CHF 5'400; netto CHF 424'800. Bund: steuerfrei bis CHF 1'070'400 (Art. 24 lit. ibis DBG) -> steuerbar CHF 429'600; Einsatzkosten 5%, höchstens CHF 5'400 (Art. 33 Abs. 4 DBG) -> CHF 5'400; netto CHF 424'200. (Der Höchstbetrag 5'400 greift unabhängig davon, ob 5% vom Gesamt- oder vom steuerbaren Gewinn gerechnet werden.)

**Antwort des Agenten** (54.7 s · Tools: 21 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__zeige, steuerwiki__suche, steuerwiki__rechne):

> Ich prüfe gerade die Zahlen nach und rechne die Beträge exakt aus. Danach folgt die Antwort.
> 
> **SG · Steuerjahr 2025: Einzelgewinn Swiss Lotto CHF 1'500'000 (Grossspiel nach Geldspielgesetz)**
> 
> Der Gewinn ist nur teilweise steuerbar. Die Freigrenze liegt bei Kanton CHF 1'069'800 und Bund CHF 1'070'400, die Einsatzkosten sind auf CHF 5'400 begrenzt.
> 
> **1. Wo wird der Gewinn deklariert?**
> - **Formular 2 (Wertschriften- und Guthabenverzeichnis):** Lotto-/Totobescheinigung beilegen. Das Formular nennt sie ausdrücklich als Beilage (sg-form-2-2025__c0004).
> - **Übertrag in Formular 1, Ziff. 4.1 (Code 146):** «Einkünfte aus Wertschriften und Guthaben», einschliesslich Gewinne aus Lotterien und anderen Geldspielen (sg-form-1-2025__c0006).
> - **Bund:** Es gibt kein eigenes Bundesformular. Die direkte Bundessteuer wird in derselben kantonalen Steuererklärung erfasst. Die Behörde nimmt die Abweichungen für den Bund automatisch vor (Merkblatt 32, sg-wl-2025__c0173).
> - **Einsatzkosten:** Ziff. 16.1 von Formular 1, «Geldspiele – Einsatzkosten» (sg-wl-2025__c0090).
> 
> **2. Steuerbarer Teil**
> 
> | | Kanton SG | Bund (DBG) |
> |---|---|---|
> | Gewinn | 1'500'000 | 1'500'000 |
> | Steuerfrei bis | 1'069'800 | 1'070'400 |
> | Steuerbar | **430'200** | **429'600** |
> | Rechtsgrundlage | Art. 37 lit. o StG SG (sg-stg-2025__art-37-t3) | Art. 24 lit. ibis DBG (bund-dbg-2025__art-24-t3) |
> 
> Die Freigrenzen sind für 2025 ☑️ agent-geprüft. Für 2026 gelten andere Beträge, die ich hier nicht übernommen habe.
> 
> **3. Abziehbare Einsatzkosten**
> 
> Abzugsfähig sind 5 % des einzelnen steuerbaren Gewinns, höchstens CHF 5'400. Das gilt für Kanton und Bund gleich.
> - Kanton: Art. 45 Abs. 3 StG SG (sg-stg-2025__art-45-t5), Formular 32 (sg-form-32-2025__c0004).
> - Bund: Art. 33 Abs. 4 DBG (bund-dbg-2025__art-33-t7).
> 
> Die Obergrenze greift in jedem Fall. 5 % von 1'500'000 wären 75'000, 5 % vom steuerbaren Teil wären 21'510 (Kanton). Es bleiben deshalb **CHF 5'400**.
> 
> Die höheren Limiten von CHF 26'700 (Kanton) und CHF 26'800 (Bund) gelten nur für abgebuchte Einsätze bei Online-Spielbankenspielen. Bei Swiss Lotto sind sie nicht anwendbar.
> 
> **4. Ergebnis**
> 
> | | Kanton | Bund |
> |---|---|---|
> | Steuerbarer Gewinn | 430'200 | 429'600 |
> | − Einsatzkosten | 5'400 | 5'400 |
> | **Netto zusätzlich im Einkommen** | **424'800** | **424'200** |
> 
> **Vorbehalte**
> - **Freibetrag:** Die Gesetze sagen «Gewinne bis zum Betrag von …» steuerfrei. Die Wegleitung SG formuliert «soweit > Fr. 1'069'800». Ich lese das als Freibetrag, also nur der Teil über der Grenze ist steuerbar. Eine ausdrückliche Berechnungsbeispiel-Stelle habe ich im Wiki nicht gefunden. Ob die Verrechnungssteuer auf den ganzen Gewinn oder nur auf den steuerbaren Teil erhoben wird, habe ich nicht geprüft. Beides sollte die Fachperson bestätigen.
> - **Verrechnungssteuer:** Auf steuerbaren Geldspielgewinnen wird Verrechnungssteuer erhoben (Art. 6 VStG). Sie wird über Formular 2 zurückgefordert, wenn der Gewinn deklariert ist. Die Beträge und die Auszahlungsmodalitäten habe ich nicht geprüft.
> - **Gesamtsteuer:** Die Höhe der Steuer habe ich nicht berechnet. Dazu fehlen das übrige Einkommen und die Tarife.
> - **Beurteilung:** Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## p06

**Frage:** SG 2025: Ehepaar mit zwei Kindern, für deren Unterhalt es zur Hauptsache aufkommt: Kind A ist 2-jährig (noch nicht schulpflichtig), Kind B ist 20 und studiert. Für Kind B selbst getragene Ausbildungskosten (Semestergebühren, Bücher, ÖV zum Studienort) CHF 9'500, erhaltenes Stipendium CHF 1'000. Welche Ziffern/Codes und welche Beträge – Kanton und Bund?

**Soll (Referenz):** Kanton SG (Steuererklärung Seite 3, Ziff. 23): Kind A -> Ziff. 23.1 (Code 252) Fr. 7'600; Kind B -> Ziff. 23.2 (Code 254) Fr. 10'800; Ausbildungskosten Kind B -> Ziff. 23.3 (Code 256, Formular 10): 9'500 - 1'000 Stipendium - 3'200 Selbstbehalt = CHF 5'300 (unter dem Maximum von Fr. 13'700). Total Kinderabzüge Kanton CHF 23'700. Bund: einheitlicher Kinderabzug CHF 6'800 pro Kind (Art. 35 Abs. 1 lit. a DBG), kein Abzug für Ausbildungskosten -> 2 x 6'800 = CHF 13'600 (Anpassung durch die Steuerbehörde, Merkblatt 32).

**Antwort des Agenten** (37.8 s · Tools: 7 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **SG · Steuerjahr 2025** – Ehepaar mit 2 Kindern (A 2-jährig, B 20 und im Studium)
> 
> Das SG-Formular hat nur eine Spalte. Die Bundesbeträge trägt die Steuerbehörde automatisch ein (sg-wl-2025__c0173). Du füllst also nur die Kantonsbeträge aus, die Bundsbeträge unten sind zur Kontrolle.
> 
> | Ziffer / Code | Inhalt | Kanton | Bund |
> |---|---|---|---|
> | **23.1 (Code 252)** | Kind A, noch nicht schulpflichtig | 1 × 7'600 = **7'600** | 6'800 |
> | **23.2 (Code 254)** | Kind B, volljährig in Ausbildung, Unterhalt zur Hauptsache | 1 × 10'800 = **10'800** | 6'800 |
> | **23.3 (Code 256)** | Ausbildungskosten Kind B | **5'300** | **kein Abzug** |
> | **14 (Code 600)** | Kinderzuschlag Versicherungsprämien, je Kind mit Abzug nach 23.1/23.2 | max. 6'800 + 2 × 1'100 = **9'000** | max. 3'700 + 2 × 700 = **5'100** |
> 
> **Rechnung Ziff. 23.3**
> - Berechnungsformel: min(max(0; Kosten − Stipendien − Selbstbehalt 3'200); 13'700).
> - Eingesetzt: 9'500 − 1'000 − 3'200 = **5'300**, deutlich unter dem Maximum von 13'700.
> - Der Ausbildungskostenabzug gilt nur, weil für Kind B der Abzug nach 23.2 geltend gemacht wird.
> - ÖV zum Studienort zählt mit. Fahrkosten sind nur mit öffentlichen Verkehrsmitteln zulässig.
> - Belege laufen über Formular 10. Das Stipendium muss mit der Verfügung deklariert werden.
> 
> **Summe Ziff. 23 Kanton:** 7'600 + 10'800 + 5'300 = **23'700**.
> 
> **Bund (direkte Bundessteuer)**
> - Der Kinderabzug ist einheitlich, ohne Staffelung nach Alter: 2 × 6'800 = **13'600**.
> - Zusätzlich gibt es eine Ermässigung vom Steuerbetrag von 263 je Kind (max.), also 2 × 263 = **526**. Das ist kein Formularabzug, sondern wird im Bundessteuertarif berücksichtigt.
> - Einen Ausbildungskostenabzug nach 23.3 gibt es beim Bund nicht, die 5'300 wirken nur kantonal.
> - Der Kinderzuschlag bei Ziff. 14 ist nur ein Maximalbetrag. Abziehbar ist der tiefere Wert aus den effektiven Prämien und diesem Maximum.
> 
> **Weitere Hinweise**
> - Vermögen (Ziff. 36.3, Code 334): 20'000 je **minderjähriges** Kind, hier nur Kind A. Für das volljährige Kind B gibt es kein 36.3 (sg-form-1-2025__c0013).
> - Ziff. 16.2 (Code 258): Kinderbetreuungskosten bei Drittbetreuung sind bei Kind A nur relevant, wenn Kosten angefallen sind. Dazu hast du nichts angegeben. Grenzen: Kanton max. 26'700, Bund max. 25'800, Altersgrenze 14 Jahre.
> - Ziff. 16.4 (Code 223/224) ist **nicht** für Kind B gedacht. Die Ausbildungskosten der Kinder laufen über 23.3.
> - Ziff. 12.2 ist ausgeschlossen. Mit Abzug von Unterhaltsbeiträgen gäbe es keinen Kinderabzug, was hier nicht zutrifft, weil das Ehepaar zur Hauptsache selbst für den Unterhalt aufkommt.
> 
> Status aller Werte: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Fundstellen: sg-form-1-2025__c0011, sg-wl-2025__c0104/c0105, sg-form-32-2025__c0006, sg-stg-2025__art-48, bund-dbg-2025__art-35 und art-36-t4. Die fachliche Beurteilung bleibt bei der Fachperson.

## p07

**Frage:** TG 2025: Arbeitnehmer fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 22 km einfach, Hin- und Rückfahrt täglich, 225 Arbeitstage, keine weiteren Fahrkosten, kein Geschäftsfahrzeug. Wie wird Formular 4.2 Ziff. 2.3–2.5 für Staats- und Bundessteuer ausgefüllt und was geht in die Steuererklärung?

**Soll (Referenz):** Formular 4.2 Ziff. 2.3: 44 km/Tag x 225 Tage = 9'900 km pro Jahr (Code 211). Staatssteuer, Auto-Ansätze nach Jahreskilometern gestaffelt: 3'000 km x 0.60 = 1'800; 2'000 km x 0.50 = 1'000; 4'900 km x 0.40 = 1'960 -> CHF 4'760. Bundessteuer einheitlich CHF 0.70/km: 9'900 x 0.70 = CHF 6'930. Ziff. 2.4 Total effektive Fahrkosten (Code 212): Staat 4'760 / Bund 6'930. Ziff. 2.5 Total abzugsfähige Fahrkosten (Code 213): Staat max. 6'000 -> CHF 4'760; Bund max. 3'300 -> CHF 3'300. Über Ziff. 7 Total Berufsauslagen (Code 240) in Steuererklärung Seite 3, Ziff. 10.1 (linke Spalte Staat, rechte Spalte Bund).

**Antwort des Agenten** (35.0 s · Tools: 6 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__zeige, steuerwiki__rechne):

> **TG · Steuerjahr 2025 · Formular 4.2, Ziff. 2.3–2.5** (Staat und Bund)
> 
> Das Auto ist hier nur wegen der Zeitersparnis zulässig. Sonst wären nur die ÖV-Abokosten abziehbar (☑️ `tg-wl-2025__c0003`, Regel zu Ziff. 2.3). Ziff. 2.1 und 2.2 bleiben leer. Ein Geschäftsfahrzeug steht nicht zur Verfügung, also Ziff. 1.2 = nein und Lohnausweis Feld F nicht angekreuzt.
> 
> ### Ziff. 2.3 – Kosten für privates Motorfahrzeug (Code 211)
> - Ankreuzen: Auto.
> - Arbeitsweg von Wohnort bis Arbeitsort: 22 km pro Tag, das sind 44 km (Hin- und Rückfahrt).
> - Anzahl Tage: 225. Das ist die übliche Obergrenze bei 100 %-Pensum (☑️ `tg-wl-2025__c0003`).
> - km pro Jahr: 44 × 225 = **9'900 km**. Diese Zahl steht bei «Total Kosten für den Arbeitsweg mit dem Motorfahrzeug», km pro Jahr, Code 211.
> 
> ### Berechnung der Ansätze
> Bei Staat und Bund gelten unterschiedliche Ansätze. Die Parkgebühren sind darin enthalten (☑️ `tg-bkv__par-1`, `bund-bkv-2025__anhang-1`).
> 
> | | Rechnung | Ergebnis |
> |---|---|---|
> | **Staatssteuer** (gestaffelt) | 3'000 × 0.60 + 2'000 × 0.50 + 4'900 × 0.40 | **CHF 4'760** |
> | **Bundessteuer** (einheitlich 0.70/km) | 9'900 × 0.70 | CHF 6'930 |
> 
> ### Ziff. 2.4 – Total effektive Fahrkosten (Ziff. 2.1–2.3, Code 212)
> - Staat: CHF 4'760
> - Bund: CHF 6'930
> 
> ### Ziff. 2.5 – Total abzugsfähige Fahrkosten (Code 213)
> Der Übertrag aus Ziff. 2.4 ist begrenzt auf Staat max. CHF 6'000 und Bund max. CHF 3'300.
> - **Staat: CHF 4'760.** Die Grenze von 6'000 ist nicht erreicht.
> - **Bund: CHF 3'300.** Die effektiven 6'930 werden auf das Maximum gekürzt.
> 
> Die Bundesgrenze von 3'300 stammt aus Art. 26 Abs. 1 lit. a DBG (Fassung 2025). Die ESTV-Wegleitung 2a nennt noch 3'200, das Gesetz geht vor (⚠️ Widerspruch in den Quellen, ☑️ `bund-dbg-2025__art-26`). Der Bundesansatz von 0.70/km gilt für 2025. Ab 2026 sind es 0.75/km.
> 
> ### Was in die Steuererklärung kommt
> - Das Total aus Ziff. 2.5 (4'760 links, 3'300 rechts) geht in die Berufsauslagen von Formular 4.2 (Ziff. 7, Code 240). Von dort wird es in die Hauptformular-Ziffer «Berufsauslagen unselbständige Erwerbstätigkeit» übertragen (Ziff. 10.1 laut Wiki).
> - Das Hauptformular hat zwei Spalten: links Staats- und Gemeindesteuer, rechts direkte Bundessteuer (☑️ `tg-wl-2025__c0196`).
> - Belege: Der Fahrzeugausweis wird als Beleg geführt. Ob er eingereicht werden muss, ist im Wiki als «unklar» vermerkt (`tg-wl-2025__c0179`). Die Zeitersparnis über 1 Stunde pro Arbeitstag (nur Hin- und Rückweg) sollte nachvollziehbar dokumentiert sein.
> - Nicht geprüft: ob die Berufsauslagen-Pauschale (übrige Berufskosten) daneben zusätzlich geltend gemacht werden kann. Das ist eine eigene Position.
> 
> Alle Werte sind ☑️ agent-geprüft, die Abnahme ist offen. Die fachliche Beurteilung bleibt bei der Fachperson.

## p08

**Frage:** TG 2025: Ehepaar bewohnt sein eigenes Einfamilienhaus am Wohnsitz selbst (Baujahr 1995, nicht landwirtschaftlich geschätzt, keine Mieteinnahmen). Indexierter Mietwert aus Selbstnutzung 2025 CHF 21'000; Unterhalt pauschal. Wie werden Eigenmietwert und Nettoerfolg im Formular 7 berechnet und wohin übertragen – Staat und Bund?

**Soll (Referenz):** Formular 7, Zeile «Mietwert selbstgenutzt» 21'000 (beide Spalten). Selbstnutzungsabzug: Staat 40% = 8'400, Bund 20% = 4'200 -> steuerbarer Eigenmietwert (= Bruttoertrag) Staat CHF 12'600, Bund CHF 16'800. Pauschalabzug Unterhalt: Gebäude älter als 10 Jahre -> 20%, berechnet vom steuerbaren Eigenmietwert: Staat 2'520, Bund 3'360. Nettoerfolg: Staat CHF 10'080, Bund CHF 13'440 (bei selbstgenutzter Liegenschaft je Spalte separat ermitteln). Total Nettoerfolge (Code 180) -> Steuererklärung Seite 2, Ziff. 8, Spalte Staat bzw. Bund.

**Antwort des Agenten** (39.9 s · Tools: 11 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne):

> **TG · Steuerjahr 2025: Eigenmietwert und Nettoerfolg in Formular 7 (Staat und Bund)**
> 
> Alle Werte sind ☑️ agent-geprüft, die Abnahme ist offen.
> 
> **Zuerst die Eingaben im Formular 7**
> - Die Checkbox «Am Wohnsitz selbstgenutzt» wird angekreuzt. Das Baujahr 1995 und die Anteile (z. B. 1/1 je Ehegatte oder gemeinsam) werden eingetragen.
> - «Mietwert selbstgenutzt» ist der indexierte Mietwert 2025 von CHF 21'000. Er steht in der Liegenschaftensteuerrechnung bzw. in der Schätzung (tg-form-07-2025__c0002, tg-wl-2025__c0224).
> - Miet- und Pachtzinsen sind keine vorhanden.
> 
> **Berechnung, Staat und Bund getrennt**
> 
> Der Nettoerfolg wird je Spalte einzeln ermittelt, weil der Selbstnutzungsabzug verschieden hoch ist (tg-wl-2025__c0244/c0245).
> 
> | Zeile Formular 7 | Staatssteuer | Bundessteuer |
> |---|---|---|
> | Mietwert selbstgenutzt | 21'000 | 21'000 |
> | Selbstnutzungsabzug (Kanton 40 % / Bund 20 %) | −8'400 | −4'200 |
> | Steuerbarer Eigenmietwert | 12'600 | 16'800 |
> | Miet- und Pachtzinsen | 0 | 0 |
> | **Bruttoertrag** | 12'600 | 16'800 |
> | Unterhalt pauschal 20 % (Checkbox «Pauschal») | −2'520 | −3'360 |
> | **Nettoerfolg** | **10'080** | **13'440** |
> 
> Quellen:
> - Selbstnutzungsabzug: tg-stg__par-23 und tg-wl-2025__c0225 (Kanton 40 %, Bund 20 %).
> - Pauschale 20 %: tg-stv__par-9 und tg-wl-2025__c0238. Das Gebäude ist von 1995 und damit älter als 10 Jahre.
> 
> **Warum die Pauschale 20 % beträgt**
> - Beim Staat zählt das Alter am Ende der Steuerperiode, beim Bund das Alter zu Beginn (Art. 5 LKV). Beide Male ist das Gebäude über 10 Jahre alt.
> - Die Pauschale deckt auch Versicherungsprämien, Verwaltung und energetische Investitionen ab (§ 9 Abs. 3 StV TG).
> - Die Pauschale ist pro Objekt und Jahr wählbar. Effektive Kosten gehen über Formular 8, Einzelbeträge ab CHF 1'000 sind zu belegen.
> 
> **Übertrag in die Steuererklärung (Formular 1)**
> - Im Formular 7 wird das «Total Nettoerfolge» gebildet.
> - Dieses Total wird in Ziff. 8.1 «Einkünfte aus Liegenschaften» (Code 180) übertragen (tg-wl-2025__c0245, tg-form-01-2025__c0009).
> - Die linke Spalte (Staats- und Gemeindesteuern) erhält **CHF 10'080**.
> - Die rechte Spalte (direkte Bundessteuer) erhält **CHF 13'440**.
> - Der Steuerwert aus Formular 7 geht zusätzlich in das Vermögen, Ziff. 31 (Code 430). Das betrifft nur die Staatssteuer und ist hier nicht berechnet.
> 
> **Offener Punkt beim Bund**
> - Art. 5 LKV nennt als Basis der Bundespauschale den «Brutto-Eigenmietwert». Das Wiki sagt nicht eindeutig, ob damit der Wert vor oder nach dem 20 %-Selbstnutzungsabzug gemeint ist.
> - Gerechnet habe ich nach der Formularlogik: Der Bruttoertrag der Bundesspalte ist der steuerbare Eigenmietwert (CHF 16'800) und die Pauschale wird darauf gerechnet.
> - Bei der anderen Lesart (20 % von CHF 21'000 = CHF 4'200) wäre der Bundes-Nettoerfolg CHF 12'600 statt CHF 13'440.
> - Das habe ich nicht abschliessend geprüft. Bitte vor Abgabe mit der Fachperson bzw. dem Steueramt klären.
> 
> Der Mietwert von CHF 21'000 ist der angegebene Wert und stammt nicht aus einem geprüften Dokument. Bitte mit der Liegenschaftensteuerrechnung 2026 oder der Schätzung abgleichen. Die fachliche Beurteilung bleibt bei der Fachperson.

## p09

**Frage:** AR 2025: Ehepaar, beide unabhängig voneinander unselbständig erwerbstätig. Das niedrigere Erwerbseinkommen (Nettolohn der Ehefrau abzüglich Berufskosten, Säule-3a-Beiträge und BVG-Einkäufe) beträgt CHF 38'000. Wie hoch ist der Zweiverdienerabzug in Ziffer 17 für die Staats- und Gemeindesteuer und für die direkte Bundessteuer?

**Soll (Referenz):** Ziff. 17 Zweiverdienerabzug. Kanton AR: 10% des niedrigeren Erwerbseinkommens, mind. Fr. 2'500, max. Fr. 5'200 (Beträge gemäss Anhang 1 StG indexiert per 1.1.2024; Art. 35 Abs. 1 lit. h StG nennt die Basisbeträge 2'400/5'000) -> 10% x 38'000 = CHF 3'800. Bund: Art. 33 Abs. 2 DBG 50% des niedrigeren Erwerbseinkommens, mind. 8'600, max. 14'100 -> 50% x 38'000 = 19'000 -> begrenzt auf CHF 14'100. Die Abweichung für die direkte Bundessteuer wird von der Steuerverwaltung automatisch vorgenommen.

**Antwort des Agenten** (25.3 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **AR · Steuerjahr 2025 · Ziffer 17 Zweiverdienerabzug** (niedrigeres Erwerbseinkommen E = CHF 38'000)
> 
> | | Rechnung | Abzug |
> |---|---|---|
> | **Staats- und Gemeindesteuer (AR)** | 10 % × 38'000 = 3'800 (Grenzen min. 2'500 / max. 5'200 – eingehalten) | **CHF 3'800** |
> | **Direkte Bundessteuer** | 50 % × 38'000 = 19'000 → auf Maximum begrenzt (min. 8'600 / max. 14'100) | **CHF 14'100** |
> 
> **Hinweise**
> - Das AR-Formular hat keine separate Bundesspalte. Du trägst in Ziffer 17 nur den kantonalen Abzug (3'800) ein. Den Bundesabzug von 14'100 setzt die Steuerverwaltung automatisch (WL AR 2025 S. 33, ar-wl-2025__c0179).
> - Der Abzug ist beim Niedrigeren der beiden Erwerbseinkommen berechnet, nachdem Berufskosten, Säule 3a und BVG-Einkäufe bereits abgezogen sind. Das entspricht deinem Wert von 38'000.
> - Der Abzug, die Berufskosten, die 3a-Beiträge und die BVG-Einkäufe zusammen dürfen den massgebenden Nettolohn nicht übersteigen. Bei einem Einkommen von 38'000 ist das hier kein Problem.
> 
> **Fundstellen** (alle ☑️ agent-geprüft, Abnahme offen)
> - Kanton: ar-stg__art-35-t3 (10 %); ar-stg-anhang-kp__c0001 (min. 2'500 / max. 5'200, indexiert per 1.1.2024); ar-wl-2025__c0004
> - Bund: bund-dbg-2025__art-33-t6 (Art. 33 Abs. 2 DBG: 50 %, min. 8'600, max. 14'100)
> 
> Die fachliche Beurteilung liegt bei der Fachperson.

## p10

**Frage:** AR 2025: Mandant bewohnt sein Einfamilienhaus am Wohnsitz dauernd selbst (Baujahr 1995, einzige Liegenschaft, keine Fremdvermietung). Mietwert gemäss Grundstückschätzung CHF 24'500; er wählt den Pauschalabzug für den Unterhalt. Was wird wo im Formular 7 und in der Steuererklärung (Staats- und Gemeindesteuer) eingetragen?

**Soll (Referenz):** Formular 7, Teil B.a: Eigenmietwert 24'500 abzüglich Selbstnutzungsabzug 20% (4'900) = Total anrechenbarer Eigenmietwert CHF 19'600 = Total Erträge a. und b. -> Übertrag Steuererklärung Seite 2, Ziff. 5. Teil C: Pauschalabzug (Gebäude über 10 Jahre; Bruttomietertrag des gesamten Liegenschaftsbesitzes nicht über Fr. 100'000) = 20% vom Total Liegenschaftserträge = 20% x 19'600 = CHF 3'920 -> Übertrag Steuererklärung Seite 3, Ziff. 15 (separater Abzug, nicht mit Ziff. 5 verrechnet). Wirkung auf das Einkommen netto CHF 15'680.

**Antwort des Agenten** (36.3 s · Tools: 7 Aufrufe steuerwiki__position, steuerwiki__formular, steuerwiki__zeige, steuerwiki__rechne):

> **AR · Steuerjahr 2025 · Staats- und Gemeindesteuer.** Die Steuererklärung hat keine Bundesspalte. Die Abweichungen für die direkte Bundessteuer nimmt die Steuerverwaltung automatisch vor (ar-wl-2025__c0179).
> 
> ## Formular 7 (Liegenschaft, pro Liegenschaft ein Formular)
> 
> **Abschn. A, Angaben zur Liegenschaft** (☑️ ar-form-07-2025__c0001)
> - Nutzung: dauernd selbst bewohnt. Anteil: 100 %. Baujahr: 1995.
> - Steuerwert (Verkehrswert gemäss Grundstückschätzung): der Betrag aus der Schätzungseröffnung. Der Wert fehlt in Ihrer Angabe, ich kann ihn nicht ergänzen.
> - Zugang/Wegfall bleibt leer, weil 2025 nichts passiert ist.
> 
> **Abschn. B a, Eigenmietwert** (☑️ ar-wl-2025__c0166)
> 
> | Zeile | CHF |
> |---|---|
> | Mietwert gemäss Grundstückschätzung | 24'500 |
> | Zuschlag für Um-/Anbauten ausserhalb der Schätzung (2.8 % der Aufwendungen) | nur falls vorhanden, sonst 0 |
> | Selbstnutzungsabzug 20 % | −4'900 |
> | **Anrechenbarer Eigenmietwert** | **19'600** |
> 
> Der Abzug von 20 % gilt, weil die Liegenschaft am Wohnsitz dauernd selbst bewohnt wird. Abschn. B b (Fremdnutzung, Leistungen Dritter) bleibt leer, weil keine Vermietung und keine PV-Vergütung vorliegt.
> 
> **Abschn. C, Unterhalts- und Verwaltungskosten** (☑️ ar-form-07-2025__c0003, ar-wl-2025__c0175)
> - Ankreuzen: C1 «Pauschalabzug der Erträge (B)». C2 «Tatsächliche Kosten» und die Rückseite bleiben leer.
> - Satz: 20 %, weil das Gebäude über 10 Jahre alt ist (Baujahr 1995). Das Alter bestimmt sich nach dem Stichtag für die Vermögenssteuer.
> - Basis: Total Liegenschaftserträge (B) = 19'600.
> - Pauschale: 20 % × 19'600 = **CHF 3'920**.
> - Die Pauschale ist zulässig: Die Liegenschaft ist privat und dient Wohnzwecken. Der jährliche Bruttomietertrag liegt bei höchstens CHF 100'000.
> - Die Pauschale deckt alle Unterhalts- und Verwaltungskosten ab. Daneben können keine Einzelrechnungen abgezogen werden.
> - Das Wahlrecht gilt pro Gebäude und Jahr.
> 
> ## Übertrag in die Steuererklärung (Formular 1)
> Es gibt nur eine Liegenschaft. Darum geht der Übertrag direkt ab Formular 7, Formular 7Z entfällt.
> 
> | Ziffer | Position | CHF |
> |---|---|---|
> | **5** (Seite 2, Code 712) | Ertrag aus Liegenschaften: anrechenbarer Eigenmietwert | 19'600 |
> | **15** (Seite 3, Code nicht verifiziert) | Unterhalts- und Verwaltungskosten: Pauschalabzug | 3'920 |
> | **31** (Seite 4, Code 710) | Liegenschaften, Steuerwert aus Form. 7 Abschn. A | gemäss Schätzung |
> 
> Netto wirkt sich die Liegenschaft im Einkommen so aus: 19'600 − 3'920 = **CHF 15'680**.
> 
> Eine allfällige Hypothek und die Schuldzinsen gehören nicht in Formular 7. Die Schuldzinsen kommen über Formular 5 in Ziff. 11, die Schuld in Ziff. 34.1. Beides ist hier nicht geprüft.
> 
> ## Offene Punkte
> - **Bund (direkte Bundessteuer):** Die AR-Quellen belegen nicht, wie Eigenmietwert und Pauschale beim Bund gerechnet werden. Ich mache dazu keine Aussage. Das Wiki nennt nur, der Bund rechne mit dem Brutto-Eigenmietwert, das Alter zu Beginn der Steuerperiode und 10 %/20 %. Die Steuerverwaltung rechnet das automatisch um.
> - **Belege:** Es gibt keine Beilagepflicht. Die Schätzungseröffnung wird nur auf Verlangen eingereicht (ar-wl-2025__c0156).
> - **Fachliche Beurteilung:** Alle Positionen sind ☑️ agent-geprüft, die Abnahme steht aus. Die endgültige Beurteilung liegt bei der zuständigen Fachperson.

