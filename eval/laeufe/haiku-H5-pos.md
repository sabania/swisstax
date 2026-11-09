# OpenClaw-Testlauf: positionstest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 10 · Lauf: 2026-11-09 14:26
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## p01

**Frage:** ZH 2025: Ledige unselbständig erwerbende Person, Nettolohn gemäss Lohnausweis CHF 92'000. Sie fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 23 km einfach, 2 Fahrten pro Tag, 220 Arbeitstage. Übrige Berufskosten werden pauschal geltend gemacht (keine Verpflegungskosten). Welche Positionen/Codes im Formular «Berufsauslagen» und welcher Betrag geht in Ziffer 11.1 – Staatssteuer und Bundessteuer getrennt?

**Soll (Referenz):** Formular 360 «Berufsauslagen» (Person 1), Begründung Privatauto Code 2042 (Zeitersparnis über 1 Stunde) ankreuzen. Ziff. 1.3 Auto (CHF 0.70/km, Staat und Bund gleich): 23 km x 2 Fahrten x 220 Tage = 10'120 km x 0.70 = CHF 7'084 (Code 204). Zwischentotal Fahrkosten Code 205: Staat max. CHF 5'200 -> 5'200; Bund max. CHF 3'300 -> 3'300. Ziff. 3 übrige Berufskosten pauschal Code 212: 3% von 92'000 = CHF 2'760 (innerhalb mind. 2'000 / höchstens 4'000; Staat und Bund gleich, vgl. BKV-Anhang). Total Berufsauslagen Code 220 -> Steuererklärung Seite 3, Ziff. 11.1: Staat 5'200 + 2'760 = CHF 7'960; Bund 3'300 + 2'760 = CHF 6'060.

**Antwort des Agenten** (33.8 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert):

> **Ergebnis ZH 2025, Ziffer 11.1 (Person 1, Code 220):**
> 
> | Position | Code (Form. 360) | Staatssteuer | Bundessteuer |
> |---|---|---|---|
> | Fahrkosten Auto: 46 km/Tag × 220 Tage = 10'120 km × CHF 0.70 = CHF 7'084 (Brutto) | 204 | 7'084 | 7'084 |
> | Zwischentotal Fahrkosten (Plafond) | 205 | **5'200** | **3'300** |
> | Übrige Berufskosten, Pauschale 3 % von CHF 92'000 = CHF 2'760 (im Rahmen 2'000–4'000) | 212 | 2'760 | 2'760 |
> | Verpflegung | 206/208/210 | 0 | 0 |
> | **Total → Ziffer 11.1** | **220** | **CHF 7'960** | **CHF 6'060** |
> 
> **Begründung der Werte:**
> - **Fahrkosten Auto:** Die Ausnahme ist begründet (Zeitersparnis über 1 Stunde). Der Km-Satz ist CHF 0.70 (ZH und Bund). Die Begründung gehört nach Ziffer 7 des Formulars.
> - **Arbeitstage:** Kantonal werden Km-Abzüge in der Regel auf 240 Tage begrenzt. Mit 220 Tagen greift das nicht. Der Bund kennt keine Arbeitstage-Regel.
> - **Plafond:** Die Fahrkosten werden gekürzt auf CHF 5'200 (Staat) bzw. CHF 3'300 (Bund). Die Staats- und Bundessteuer-Spalte weichen deshalb ab.
> - **Übrige Berufskosten:** Pauschal 3 % des Nettolohns, Minimum CHF 2'000, Maximum CHF 4'000. Beide Steuerarten haben dieselben Werte. Die Pauschale gilt nur, wenn keine effektiven Kosten mit vollem Nachweis geltend gemacht werden.
> 
> **Zu prüfen:**
> - Der Bund kürzt die Pauschale bei Teilzeit oder unterjähriger Erwerbstätigkeit. Ich gehe von einer vollen Erwerbstätigkeit übers ganze Jahr aus. Bitte bestätigen.
> - Ich habe die Werte so gerechnet, wie die Formularzeilen im Wiki beschrieben sind: Auto-Brutto auf Zeile 204, gekappter Betrag auf Zwischentotal 205. Die Kürzung wird also auf Zeile 205 vorgenommen.
> - Die Fundstellen sind als «agent-geprüft» markiert. Die fachliche Abnahme steht noch aus.
> 
> Quellen: `position zh 2025 11.1` (zh-form-300-2025__c0007), `position zh 2025 Berufsauslagen` (zh-form-360-2025__c0004), `wert zh/bund 2025 fahrkosten` (zh-stg-2025__par-26, bund-dbg-2025__art-26, bund-bkv-2025__anhang-1).

## p02

**Frage:** ZH 2025: Verheiratetes Paar, beide in einer Pensionskasse (2. Säule) versichert, zwei minderjährige Kinder mit Kinderabzug. Bezahlte Krankenkassenprämien 2025 (bereits netto nach individueller Prämienverbilligung) CHF 15'600, Sparzinsen gemäss Wertschriftenverzeichnis CHF 150. Wie wird das Formular «Versicherungsprämien» ausgefüllt und welcher Abzug kommt in Ziffer 15 (Staat / Bund)?

**Soll (Referenz):** Formular 365 «Versicherungsprämien»: Teil A: Code 601 Krankenversicherungsprämien 15'600 + Code 604 Sparzinsen 150 -> Total (A) Code 606 = CHF 15'750. Teil B (Maximum): Verheiratete mit Beiträgen an 2. Säule/3a Code 611: Staat 5'800 / Bund 3'700; Kinderzuschlag Code 613: Staat 2 x 1'300 = 2'600 / Bund 2 x 700 = 1'400 -> Total (B) Code 616: Staat CHF 8'400 / Bund CHF 5'100. Teil C Code 270 = der niedrigere Betrag von (A) und (B): Staat CHF 8'400, Bund CHF 5'100 -> Steuererklärung Seite 3, Ziff. 15 (Spalten Staatssteuer/Bundessteuer).

**Antwort des Agenten** (34.9 s · Tools: 4 Aufrufe steuerwiki__position, steuerwiki__wert):

> **Kanton Zürich 2025, verheiratetes Paar mit zwei Kindern, beide in der 2. Säule**
> 
> **Formular «Versicherungsprämien» (Form. 365)**
> 
> | Zeile | Code | Eintrag | Betrag |
> |---|---|---|---|
> | Teil A, Ziff. 1: bezahlte KK-Prämien (nach IPV-Verrechnung) | 601 | Prämie netto | 15'600 |
> | Teil A, Ziff. 4: Zinsen von Sparkapitalien (Wertschriftenverzeichnis) | 604 | Sparzinsen | 150 |
> | Zwischentotal | 607 | 601–604 | 15'750 |
> | Teil A, Ziff. 6: IPV nicht verrechnet | 605 | 0, weil die IPV bereits in 601 gekürzt ist | 0 |
> | Total (A) | 606 | 607 − 605 | 15'750 |
> 
> Die Prämienverbilligung ist hier nicht nochmals abzuziehen. Die Krankenkasse hat sie bereits verrechnet, deshalb steht in 601 nur der Nettobetrag. Ein Doppelabzug würde den Abzug zu tief ausweisen.
> 
> **Teil B (Maximalabzug, Form. 365)**
> 
> | Zeile | Code | Staat | Bund |
> |---|---|---|---|
> | Verheiratete mit Beiträgen an 2. Säule/3a | 611 | 5'800 | 3'700 |
> | Zusatz je Kind (2 × 1'300 / 2 × 700) | 613–615 | 2'600 | 1'400 |
> | Maximalabzug B (Code 616) | | 8'400 | 5'100 |
> 
> Die Limite «ohne Vorsorge» (8'700 / 5'550) gilt nicht, weil beide Ehegatten Beiträge an die 2. Säule leisten. Die Limite ist sonst nur dann höher, wenn weder Steuerpflichtige noch Arbeitgeber Beiträge an 2. Säule oder 3a geleistet haben.
> 
> **Ziffer 15 (Hauptformular, Code 270)**
> 
> Ziffer 15 nimmt pro Spalte den kleineren Wert aus A (606) und B (616):
> 
> - **Staatssteuer:** min(15'750; 8'400) = **CHF 8'400**
> - **Bundessteuer:** min(15'750; 5'100) = **CHF 5'100**
> 
> Bei der Bundessteuer wird der Abzug also auf CHF 5'100 begrenzt. Die Prämien und Sparzinsen übersteigen die Limite deutlich, deshalb wirkt die Limite in beiden Spalten.
> 
> **Quellen und Status**
> - Formular: `zh-form-365-2025__c0001` (Codes 601–607), `zh-form-300-2025__c0008` (Ziff. 15, Code 270)
> - Limiten Kanton: `zh-stg-2025__par-31-t2`, `zh-wl-2025__c0084`
> - Limiten Bund: `bund-dbg-2025__art-33-t2`, `bund-dbg-2025__art-33-t5`
> - Kinderzuschläge: `zh-stg-2025__par-31-t2` (Kanton), `bund-dbg-2025__art-33-t5` (Bund)
> - Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Werte sind durch die Quellen belegt, die fachliche Abnahme steht noch aus.
> 
> **Belege, die Sie beilegen sollten:** Die Krankenkassen-Prämienabrechnung mit der verrechneten IPV und die Zins- und Saldobescheinigung für die Sparzinsen. Das Formular Versicherungsprämien selbst ist laut Wegleitung (S. 31) beizulegen, wenn es verlangt wird.

## p03

**Frage:** ZH 2025: Alleinstehende Mandantin unterstützt ihre erwerbsunfähige Mutter (eigener Haushalt, keine Alimente, kein Kinderabzug) nachweislich mit CHF 5'000 im Jahr 2025. In welcher Ziffer wird das geltend gemacht, welcher Abzug gilt bei der Staatssteuer und bei der Bundessteuer, und wirkt sich das auf den Versicherungsprämienabzug aus?

**Soll (Referenz):** Ziff. 24.2 «Abzug für unterstützte Personen» (Code 374); Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der Unterstützung beilegen. Staat: Voraussetzung Unterstützungsleistung mindestens CHF 2'800 -> 5'000 erfüllt -> Abzug CHF 2'800. Bund: Voraussetzung Unterstützungsleistung mindestens CHF 6'800 (Art. 35 Abs. 1 lit. b DBG) -> 5'000 < 6'800 -> kein Unterstützungsabzug (CHF 0). Folge im Formular 365 Teil B.3: Staat zusätzlicher Abzug CHF 1'300 für die unterstützungsbedürftige Person (Code 614); Bund kein Zuschlag von CHF 700 (Code 615), da kein Unterstützungsabzug zusteht.

**Antwort des Agenten** (48.2 s · Tools: 7 Aufrufe steuerwiki__position, steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurzantwort (ZH 2025):** Der Abzug gehört in **Ziff. 24.2** (Code 374, «Abzug für unterstützte Personen»). Beim Kanton gilt er mit **CHF 2'800**, beim Bund entfällt er, weil die Unterstützung von CHF 5'000 unter der Bundesschwelle von **CHF 6'800** liegt. Der Versicherungsprämienabzug steigt im Kanton, im Bund nicht.
> 
> **Ziff. 24.2 (Kanton ZH, Form. 300)**
> - Die Mutter muss erwerbsunfähig oder beschränkt erwerbsfähig sein. Ehegatten, Kinder mit Kinderabzug und Personen, für die Alimente abgezogen werden, sind ausgeschlossen. Hier trifft nichts davon zu.
> - Staat: Der Abzug ist fix **CHF 2'800**, wenn die Unterstützung mindestens diesen Betrag erreicht. Mit CHF 5'000 ist das erfüllt.
> - Bund: Der Abzug beträgt **CHF 6'800** und wird nur gewährt, wenn die Leistung mindestens 6'800 erreicht (Art. 35 Abs. 1 lit. b DBG; KS 30 Ziff. 11: «Wird … weniger als der festgelegte Abzug geleistet, entfällt dieser Sozialabzug»). Bei CHF 5'000 entfällt er ganz, auch nicht anteilig.
> - Bedürftigkeit der Mutter (Kanton, ZStB 34.1): Einkommen unter CHF 15'000 und Vermögen unter CHF 50'000. Das muss geprüft werden.
> - Belege: Bestätigung der Mutter mit Art, Zeitpunkt und Höhe der Unterstützung. Zahlungsbelege auf Verlangen. Für die Erwerbsunfähigkeit verlangt ZStB 34.1 Rz 27–30 eine faktische Erwerbsunfähigkeit; ich würde dafür eine IV-Verfügung beilegen, auch wenn das Wiki sie nicht als Pflichtbeleg nennt.
> - Auf Seite 1 des Formulars die unterstützte Person mit Name, Geburtsjahr, Adresse und Betrag von CHF 5'000 eintragen.
> 
> **Versicherungsprämienabzug (Ziff. 15)**
> Der Abzug ist das Minimum aus den tatsächlich bezahlten Prämien und einem Maximalbetrag. Der Maximalbetrag steigt pro unterstützter Person, nur wenn dort auch ein Unterstützungsabzug gewährt wird.
> 
> | | Staat ZH | Bund |
> |---|---|---|
> | Maximum alleinstehend mit 2./3a | 2'900 | 1'800 |
> | Maximum alleinstehend ohne 2./3a | 4'350 | 2'700 |
> | Zuschlag für die unterstützte Person | +1'300 (gewährt) | +700 (nicht gewährt) |
> | **Maximum mit Zuschlag, mit 2./3a** | **4'200** | **1'800** |
> | **Maximum mit Zuschlag, ohne 2./3a** | **5'650** | **2'700** |
> 
> Im Kanton erhöht der Zuschlag den Maximalbetrag auf 4'200 bzw. 5'650. Im Bund bleibt er bei 1'800 bzw. 2'700, weil dort kein Abzug nach Art. 35 gewährt wird. Ob sich das konkret auswirkt, hängt davon ab, ob die tatsächlichen Prämien über dem bisherigen Maximum liegen. Die Angabe «ordentliche Beiträge an die Pensionskasse ja/nein» auf Seite 1 bestimmt, welcher Maximalbetrag gilt.
> 
> **Status:** Die Fundstellen (Ziff. 24.2, Ziff. 15, KS 30 Ziff. 11) sind agent-geprüft, die Abnahme ist offen. Die Zuschlagsregel im Bund (Art. 33 Abs. 5 DBG) stammt aus dem Wiki-Eckwert, nicht aus einem geöffneten Gesetzestext. Den Fall «ohne 2./3a» habe ich nicht eigens nachgeprüft.

## p04

**Frage:** SG 2025: Nettoeinkommen gemäss Ziffer 20 CHF 80'000. Arzt- und Zahnarztrechnungen 2025 brutto CHF 6'200, davon von der Krankenkasse vergütet CHF 1'700. Wo werden die Kosten deklariert und wie hoch ist der Abzug für die Staats- und Gemeindesteuern bzw. für die direkte Bundessteuer (Annahme: massgebendes Nettoeinkommen Bund ebenfalls CHF 80'000)?

**Soll (Referenz):** Formular 6 (Rückseite «Krankheits-, Unfall- und behinderungsbedingte Kosten»): Bruttobetrag 6'200 abzüglich Beiträge Dritter 1'700 = selbst getragene Kosten CHF 4'500 -> Steuererklärung Seite 3, Vorkolonne Ziff. 21.1 (Code 650). Kanton SG: Selbstbehalt 2% des Nettoeinkommens (Ziff. 20) = 2% x 80'000 = 1'600 (Code 238) -> Abzug Code 240 = CHF 2'900. Bund: Selbstbehalt 5% (Art. 33 Abs. 1 lit. h DBG; Merkblatt 32) = 4'000 -> Abzug CHF 500. Das SG-Formular hat nur eine Spalte; die Abweichung für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor.

**Antwort des Agenten** (28.2 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert):

> **Deklaration:** SG 2025 Formular 1, **Ziff. 21.1** («Krankheits- und Unfallkosten»). Die Arzt- und Zahnarztrechnungen gehen mit dem Bruttobetrag über das Hilfsblatt Formular 6 (Rückseite) in die Vorkolonne (Code 650). Die Vergütung der Krankenkasse wird davon abgezogen. Der Selbstbehalt (Code 238) wird von dieser Vorkolonne abgezogen, der Abzug steht in Code 240.
> 
> **Berechnung**
> 
> | | Kanton SG (Staats- und Gemeindesteuern) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | Brutto-Arzt-/Zahnarztkosten | 6'200 | 6'200 |
> | ./. Vergütung Krankenkasse | −1'700 | −1'700 |
> | **Vorkolonne (Code 650)** | **4'500** | **4'500** |
> | Selbstbehalt | 2 % × 80'000 = −1'600 | 5 % × 80'000 = −4'000 |
> | **Abzug** | **2'900** | **500** |
> 
> **Hinweise**
> 
> - **Kanton:** Der Selbstbehalt beträgt 2 % des Nettoeinkommens gemäss Ziff. 20. Quelle: sg-stg-2025 Art. 46 (☑️ agent-geprüft, Abnahme offen).
> - **Bund:** Der Selbstbehalt beträgt 5 %, Quelle: bund-dbg-2025 Art. 33 Abs. 3 (☑️ agent-geprüft, Abnahme offen). Ich habe Ihre Annahme von CHF 80'000 als Basis übernommen. Nach Art. 33 DBG ist die Basis aber die um die Aufwendungen verminderten steuerbaren Einkünfte. Diese können vom Nettoeinkommen abweichen, weshalb die 500 nur gelten, wenn Ihre Annahme zutrifft.
> - **Formular:** Das SG-Formular hat für den Bund keine eigene Spalte. Die Abweichung für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor (Merkblatt 32). Den Bundesabzug müssen Sie also nicht separat eintragen.
> - **Belege:** Die Einzelrechnungen sind im Formular 6 aufzuführen und auf Verlangen einzureichen. Wenn Sie im Formular 6 auf einen Krankenkassen-Zusammenzug verweisen, müssen Sie diesen mit der detaillierten Leistungsübersicht einreichen.
> - **Nicht hier:** Krankenkassenprämien gehören nicht in Ziff. 21.1, sondern in Ziff. 14.

## p05

**Frage:** SG 2025: Mandant gewinnt im Swiss Lotto (interkantonal durchgeführte Lotterie = Grossspiel) einen Einzelgewinn von CHF 1'500'000. Wo wird der Gewinn deklariert, welcher Teil ist steuerbar und welche Einsatzkosten sind abziehbar – Kanton und Bund getrennt?

**Soll (Referenz):** Deklaration im Wertschriften- und Guthabenverzeichnis (Formular 2), Spalte A (Bargewinn aus inländischer Lotterie, verrechnungssteuerpflichtig); Übertrag Ziff. 4.1 (Code 146). Kanton SG: Einzelgewinne aus Grossspielen steuerbar, soweit > Fr. 1'069'800 -> 1'500'000 - 1'069'800 = CHF 430'200 steuerbar; Einsatzkosten unter Ziff. 16.1 (Code 220): 5%, höchstens Fr. 5'400 -> CHF 5'400; netto CHF 424'800. Bund: steuerfrei bis CHF 1'070'400 (Art. 24 lit. ibis DBG) -> steuerbar CHF 429'600; Einsatzkosten 5%, höchstens CHF 5'400 (Art. 33 Abs. 4 DBG) -> CHF 5'400; netto CHF 424'200. (Der Höchstbetrag 5'400 greift unabhängig davon, ob 5% vom Gesamt- oder vom steuerbaren Gewinn gerechnet werden.)

**Antwort des Agenten** (51.6 s · Tools: 17 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__position, steuerwiki__zeige):

> ## Ergebnis: SG 2025, Lotto-Einzelgewinn CHF 1'500'000 (Grossspiel)
> 
> Die interkantonale Lotterie ist ein Grossspiel. Steuerbar ist nur der Teil über der Freigrenze je Einzelgewinn. Der Betrag bis zur Grenze bleibt steuerfrei.
> 
> | | Kanton SG (Staats-/Gemeindesteuer) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | Einzelgewinn | 1'500'000 | 1'500'000 |
> | Steuerfrei bis | 1'069'800 | 1'070'400 |
> | **Steuerbarer Teil** | **430'200** | **429'600** |
> | Einsatzkosten-Pauschale 5 %, max. 5'400 | −5'400 | −5'400 |
> | **Netto steuerbar** | **424'800** | **424'200** |
> 
> Die 5 % gelten auf den steuerbaren Teil (5 % von 430'200 = 21'510, also greift der Höchstbetrag). Beim Bund entsprechend (21'480 → 5'400).
> 
> **Deklaration (Kanton SG)**
> - Formular 1, Ziff. 4.1 «Einkünfte aus Wertschriften und Guthaben inkl. Lotterie-/Geldspielgewinne» (Code 146). Die Werte kommen aus Formular 2.
> - Formular 2, Abschnitt j) «Geldspielgewinne»: Der steuerbare Teil wird hier erfasst.
> - Beleg: Lotto-/Lottogewinn-Bescheinigung, Beilage zu Formular 2. Das Formular verlangt Lotto-/Totobescheinigungen als Beilage.
> - Die Einsatzkosten-Pauschale wird unter Ziff. 16.1 «Weitere Abzüge» geltend gemacht.
> 
> **Bund**
> - Im SG-Formular gibt es keine separate Bundesspalte. Abweichungen für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor (Merkblatt 32).
> - Für die Bundessteuer gilt dieselbe Systematik: Freigrenze 1'070'400, Pauschale 5 % bis 5'400 je Gewinn. Der Bund führt Lotteriegewinne in Formular 2, Ziff. 4 «Wertschriftenertrag … Lotterie- und Totogewinnen».
> 
> **Einsatzkosten**
> - Bei Grossspielen (Lotto) gilt nur die Pauschale von 5 % des steuerbaren Gewinns, höchstens CHF 5'400. Die effektiv bezahlten Lotto-Einsätze sind nicht abziehbar.
> - Der Abzug der tatsächlichen Einsätze gilt nur für Online-Spielbankenspiele (SG: max. 26'700, Bund: max. 26'800). Das trifft hier nicht zu.
> 
> **Vorbehalte**
> - Die Freigrenzen (SG ☑️ agent-geprüft, Bund ☑️ agent-geprüft) und die Pauschale (Quelle WL SG 2025 Ziff. 16.1 und VKP Art. 3) sind belegt. Die Bundes-Pauschale ist nur 🟡 extrahiert und nicht abgenommen.
> - Ob die Pauschale nur auf den steuerbaren Teil oder auf den ganzen Gewinn zu rechnen ist, ändert das Ergebnis hier nicht, weil der Höchstbetrag greift.
> - Die Grenzen gelten für 2025. Für 2026 steigen sie (SG laut Merkblatt 8/2026); nicht übernehmen.
> - Ob die Bank-VSt-Spalte A für Lotteriegewinne gilt, habe ich nur aus der Formularbeschreibung gelesen. Der Lotto-Beleg sollte dies bestätigen.
> - Die Auszahlung als Bargewinn ist beim Lotto einkommenssteuerpflichtig nur im steuerbaren Teil. Wie der Gewinn in der Vermögenssteuer behandelt wird, habe ich nicht geprüft.

## p06

**Frage:** SG 2025: Ehepaar mit zwei Kindern, für deren Unterhalt es zur Hauptsache aufkommt: Kind A ist 2-jährig (noch nicht schulpflichtig), Kind B ist 20 und studiert. Für Kind B selbst getragene Ausbildungskosten (Semestergebühren, Bücher, ÖV zum Studienort) CHF 9'500, erhaltenes Stipendium CHF 1'000. Welche Ziffern/Codes und welche Beträge – Kanton und Bund?

**Soll (Referenz):** Kanton SG (Steuererklärung Seite 3, Ziff. 23): Kind A -> Ziff. 23.1 (Code 252) Fr. 7'600; Kind B -> Ziff. 23.2 (Code 254) Fr. 10'800; Ausbildungskosten Kind B -> Ziff. 23.3 (Code 256, Formular 10): 9'500 - 1'000 Stipendium - 3'200 Selbstbehalt = CHF 5'300 (unter dem Maximum von Fr. 13'700). Total Kinderabzüge Kanton CHF 23'700. Bund: einheitlicher Kinderabzug CHF 6'800 pro Kind (Art. 35 Abs. 1 lit. a DBG), kein Abzug für Ausbildungskosten -> 2 x 6'800 = CHF 13'600 (Anpassung durch die Steuerbehörde, Merkblatt 32).

**Antwort des Agenten** (36.6 s · Tools: 7 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Steuerjahr 2025, Kanton St. Gallen (Staats- und Gemeindesteuer) und direkte Bundessteuer**
> 
> | Ziff. (Code) | Sachverhalt | Kanton SG | Bund |
> |---|---|---|---|
> | **23.1** (Code 252) | Kind A, 2 Jahre, noch nicht schulpflichtig | **CHF 7'600** | **CHF 6'800** |
> | **23.2** (Code 254) | Kind B, 20 Jahre, in Ausbildung | **CHF 10'800** | **CHF 6'800** |
> | **23.3** (Code 256) | Ausbildungskosten Kind B | **CHF 5'300** | **kein Abzug** |
> | Ziff. 14 (Code 600), Zuschlag je Kind | Kind A und Kind B | 2 × CHF 1'100 = **CHF 2'200** | 2 × CHF 700 = **CHF 1'400** |
> 
> **Rechnung Ziff. 23.3 (Kanton):**
> 9'500 (Ausbildungskosten) − 1'000 (Stipendium) − 3'200 (Selbstbehalt) = 5'300. Das liegt unter dem Maximum von CHF 13'700.
> 
> **Bund:**
> - Bund-Steuerbetrag: Ermässigung von CHF 263 je Kind, also 2 × 263 = **CHF 526** vom Steuerbetrag. Diesen Abzug nimmt die Steuerbehörde laut Merkblatt 32 automatisch vor. Er steht nicht als eigene Zeile im Formular.
> - Der Bund kennt keinen Ausbildungskostenabzug. Die 23.3-Position ist ausdrücklich «nur Kanton/Gemeinde».
> 
> **Summen:**
> - Kanton: Ziff. 23.1 + 23.2 + 23.3 = 7'600 + 10'800 + 5'300 = **CHF 23'700** (Einkommensabzüge), dazu Ziff. 14 mit CHF 2'200.
> - Bund: Ziff. 23.1 + 23.2 = 6'800 + 6'800 = **CHF 13'600** (Einkommensabzüge), dazu Ziff. 14 mit CHF 1'400 und der Steuerbetrag-Ermässigung von CHF 526.
> 
> **Hinweise:**
> - Die Kinderabzüge gelten nur, wenn für die Kinder zur Hauptsache Unterhalt geleistet wird. Für Kind B gilt der 23.2-Abzug, weil es volljährig ist und sich in Ausbildung befindet. Ausbildungskosten (23.3) werden nur gewährt, wenn für das Kind ein 23.2-Abzug geltend gemacht werden kann.
> - Der Stichtag für die Verhältnisse ist der 31.12.2025.
> - Ziff. 23.3 verlangt die Belege im Formular 10. Dazu gehören Rechnungen für Semestergebühren, Bücher und Skripte sowie ÖV-Abo zum Studienort. Die Stipendienverfügung ist ebenfalls einzureichen.
> - Die Ziff. 14-Zuschläge sind meine Ergänzung. Sie hängen an den Kinderabzügen, sind aber nicht Teil der Frage.
> - Der Status der Werte und Positionen ist ☑️ agent-geprüft. Die Fundstellen sind sg-form-1-2025__c0011 (Ziff. 23.1–23.3), sg-wl-2025__c0105 (Ziff. 23.3, Selbstbehalt 3'200 und Maximum 13'700), sg-stg-2025__art-48 (Beträge 7'600/10'800/13'700) und bund-dbg-2025__art-35 und art-36-t4 (Bund 6'800 und 263). Die Abnahme ist noch offen.

## p07

**Frage:** TG 2025: Arbeitnehmer fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 22 km einfach, Hin- und Rückfahrt täglich, 225 Arbeitstage, keine weiteren Fahrkosten, kein Geschäftsfahrzeug. Wie wird Formular 4.2 Ziff. 2.3–2.5 für Staats- und Bundessteuer ausgefüllt und was geht in die Steuererklärung?

**Soll (Referenz):** Formular 4.2 Ziff. 2.3: 44 km/Tag x 225 Tage = 9'900 km pro Jahr (Code 211). Staatssteuer, Auto-Ansätze nach Jahreskilometern gestaffelt: 3'000 km x 0.60 = 1'800; 2'000 km x 0.50 = 1'000; 4'900 km x 0.40 = 1'960 -> CHF 4'760. Bundessteuer einheitlich CHF 0.70/km: 9'900 x 0.70 = CHF 6'930. Ziff. 2.4 Total effektive Fahrkosten (Code 212): Staat 4'760 / Bund 6'930. Ziff. 2.5 Total abzugsfähige Fahrkosten (Code 213): Staat max. 6'000 -> CHF 4'760; Bund max. 3'300 -> CHF 3'300. Über Ziff. 7 Total Berufsauslagen (Code 240) in Steuererklärung Seite 3, Ziff. 10.1 (linke Spalte Staat, rechte Spalte Bund).

**Antwort des Agenten** (33.4 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__wert):

> **Ergebnis TG 2025 (Staats- und Bundessteuer)**
> 
> **Berechnung:** 22 km × 2 = 44 km pro Tag × 225 Tage = **9'900 km pro Jahr**
> 
> | Form. 4.2 | Position | Staat (TG) | Bund |
> |---|---|---|---|
> | Ziff. 2.3 | Privatauto, km/Tag × Tage (Code 211 = km pro Jahr: 9'900) | **Fr. 4'760.–** | **Fr. 6'930.–** |
> | Ziff. 2.4 | Total effektive Fahrkosten (Code 212) | **Fr. 4'760.–** | **Fr. 6'930.–** |
> | Ziff. 2.5 | Abzugsfähig: Staat min(2.4; 6'000), Bund min(2.4; 3'300) (Code 213) | **Fr. 4'760.–** | **Fr. 3'300.–** |
> 
> **Rechnung dahinter:**
> - **Kanton:** gestaffelt, 3'000 km × 0.60 = 1'800 + 2'000 km × 0.50 = 1'000 + 4'900 km × 0.40 = 1'960 → 4'760
> - **Bund:** 9'900 km × 0.70 = 6'930, begrenzt auf den Maximalabzug von 3'300
> 
> **Was in die Steuererklärung kommt:**
> - Form. 4.2 Ziff. 2.5 → Ziff. 7 (Code 240) → Steuererklärung Seite 3, **Ziff. 10.1**: Staat links **Fr. 4'760**, Bund rechts **Fr. 3'300**.
> - Keine Fahrkosten in Ziff. 2.1/2.2 angegeben. Falls es welche gibt (z.B. ÖV-Abo, Wochenaufenthalt), kommen sie in die Summe und die Maxima gelten für alle Fahrkosten zusammen.
> 
> **Zu beachten:**
> - **Ausnahmegrund dokumentieren:** Der Privatauto-Abzug gilt nur, wenn der ÖV nicht zumutbar ist (hier Zeitersparnis über 1 Stunde pro Arbeitstag). Die Begründung sollte belegt werden, z.B. mit Fahrplan-Vergleich. Ob sie einzureichen ist, ist im Wiki unklar.
> - **Belege:** Fahrzeugausweis (Auto), Distanzangabe Wohnadresse–Arbeitsort, Arbeitszeitangaben.
> - **225 Tage:** Das ist der Regelwert bei 100%-Pensum («in der Regel max.»). Bei einem anderen Pensum oder einer anderen Tageszahl ändert sich die Rechnung.
> - **Bund-Maximum:** DBG Art. 26 und RS 2-210 nennen 3'300 Fr. Die ESTV-Wegleitung 2a 2025 (S. 6) nennt noch 3'200 Fr. Ich habe mit 3'300 gerechnet, weil das die Gesetzesfassung ist. Die Abweichung ist im Wiki als Widerspruch markiert.
> - **Status:** Die Fundstellen sind agent-geprüft (Abnahme offen). Die Zahlen sind aus dem Wiki übernommen, nicht selbst aus dem amtlichen Formular abgeglichen.

## p08

**Frage:** TG 2025: Ehepaar bewohnt sein eigenes Einfamilienhaus am Wohnsitz selbst (Baujahr 1995, nicht landwirtschaftlich geschätzt, keine Mieteinnahmen). Indexierter Mietwert aus Selbstnutzung 2025 CHF 21'000; Unterhalt pauschal. Wie werden Eigenmietwert und Nettoerfolg im Formular 7 berechnet und wohin übertragen – Staat und Bund?

**Soll (Referenz):** Formular 7, Zeile «Mietwert selbstgenutzt» 21'000 (beide Spalten). Selbstnutzungsabzug: Staat 40% = 8'400, Bund 20% = 4'200 -> steuerbarer Eigenmietwert (= Bruttoertrag) Staat CHF 12'600, Bund CHF 16'800. Pauschalabzug Unterhalt: Gebäude älter als 10 Jahre -> 20%, berechnet vom steuerbaren Eigenmietwert: Staat 2'520, Bund 3'360. Nettoerfolg: Staat CHF 10'080, Bund CHF 13'440 (bei selbstgenutzter Liegenschaft je Spalte separat ermitteln). Total Nettoerfolge (Code 180) -> Steuererklärung Seite 2, Ziff. 8, Spalte Staat bzw. Bund.

**Antwort des Agenten** (33.2 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__suche, steuerwiki__zeige):

> **Ergebnis TG 2025 (Ehepaar, eigenes Einfamilienhaus am Wohnsitz, Baujahr 1995, Mietwert 21'000, Unterhalt pauschal)**
> 
> | Schritt | Staat/Gemeinde (links) | Direkte Bundessteuer (rechts) |
> |---|---|---|
> | Mietwert selbstgenutzt (indexiert) | 21'000 | 21'000 |
> | Selbstnutzungsabzug | −8'400 (40 %) | −4'200 (20 %) |
> | Steuerbarer Eigenmietwert | 12'600 | 16'800 |
> | Bruttoertrag (keine Mieten) | 12'600 | 16'800 |
> | Unterhalt pauschal (20 %, Baujahr 1995 > 10 Jahre) | −2'520 | −3'360 |
> | **Nettoerfolg** | **10'080** | **13'440** |
> 
> **Berechnung**
> - Der Selbstnutzungsabzug ist für Staat und Bund unterschiedlich. Deshalb sind auch die Nettoerfolge je Spalte verschieden.
> - Die Pauschale wird vom steuerbaren Eigenmietwert berechnet, also je Spalte von 12'600 (Staat) bzw. 16'800 (Bund). Ich habe das aus dem Wortlaut der WL TG 2025 abgeleitet (S. 50, tg-wl-2025__c0238). Die Bund-Basis ist damit eine Auslegung, nicht ausdrücklich so formuliert.
> 
> **Wo es hingeht**
> 1. **Formular 7** (Hilfsblatt Liegenschaften): Mietwert, Selbstnutzungsabzug und steuerbarer Eigenmietwert getrennt für Staat und Bund. Haken bei «Am Wohnsitz selbstgenutzt» setzen. Pauschal ankreuzen. Nettoerfolg je Spalte, Summe über alle Liegenschaften.
> 2. **Ziff. 8.1** der Steuererklärung (Einkünfte aus Liegenschaften, Code 180): Das Total der Nettoerfolge aus Formular 7 wird übertragen. Links 10'080 (Staat/Gemeinde), rechts 13'440 (direkte Bundessteuer).
> 3. **Nicht vergessen:** Der Steuerwert der Liegenschaft gehört separat in **Ziff. 31** (Vermögen, Code 430). Das ist der rechtskräftige amtliche Verkehrswert Ende 2025, nicht der Eigenmietwert.
> 
> **Belege und offene Punkte**
> - Liegenschaftensteuerrechnung 2026 (indexierter Mietwert 2025) und Schätzungsprotokoll bzw. Steuerwert (liegenschaft-schaetzung-eigenmietwert). Die Einreichepflicht ist laut Wiki unklar.
> - Bei Pauschale sind keine Unterhaltsrechnungen nötig. Effektive Kosten würden Formular 8 und Rechnungskopien ab Fr. 1'000 erfordern.
> - Ob der Mietwert 2025 wirklich 21'000 ist, prüfe ich nicht selbst. Das ist Ihre Angabe und muss mit der Liegenschaftensteuerrechnung übereinstimmen.
> 
> **Quellen und Status**
> - Formularposition: tg-form-07-2025__c0002 · Ziff. 8.1 (Code 180): tg-form-01-2025__c0009 · Ziff. 31: tg-form-01-2025__c0015
> - Selbstnutzungsabzug 40 % Kanton / 20 % Bund und Abzug nur bei Wohnsitz: tg-wl-2025__c0225 (S. 47)
> - Pauschale 10 %/20 % (Alter des Gebäudes): tg-wl-2025__c0238 (S. 50)
> - Status: agent-geprüft, Abnahme offen. Die fachliche Beurteilung bleibt bei der Fachperson.

## p09

**Frage:** AR 2025: Ehepaar, beide unabhängig voneinander unselbständig erwerbstätig. Das niedrigere Erwerbseinkommen (Nettolohn der Ehefrau abzüglich Berufskosten, Säule-3a-Beiträge und BVG-Einkäufe) beträgt CHF 38'000. Wie hoch ist der Zweiverdienerabzug in Ziffer 17 für die Staats- und Gemeindesteuer und für die direkte Bundessteuer?

**Soll (Referenz):** Ziff. 17 Zweiverdienerabzug. Kanton AR: 10% des niedrigeren Erwerbseinkommens, mind. Fr. 2'500, max. Fr. 5'200 (Beträge gemäss Anhang 1 StG indexiert per 1.1.2024; Art. 35 Abs. 1 lit. h StG nennt die Basisbeträge 2'400/5'000) -> 10% x 38'000 = CHF 3'800. Bund: Art. 33 Abs. 2 DBG 50% des niedrigeren Erwerbseinkommens, mind. 8'600, max. 14'100 -> 50% x 38'000 = 19'000 -> begrenzt auf CHF 14'100. Die Abweichung für die direkte Bundessteuer wird von der Steuerverwaltung automatisch vorgenommen.

**Antwort des Agenten** (25.9 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert):

> **Ergebnis (E = CHF 38'000, Steuerjahr 2025, Kanton AR):**
> 
> - **Staats- und Gemeindesteuer (AR): CHF 3'800.** 10 % von 38'000 = 3'800. Das liegt zwischen Minimum 2'500 und Maximum 5'200.
> - **Direkte Bundessteuer: CHF 14'100.** 50 % von 38'000 = 19'000, begrenzt auf das Maximum 14'100 (Minimum 8'600).
> 
> **Zur Ziffer 17:** Das AR-Formular hat keine Bundesspalte. Die Steuerverwaltung nimmt die Bundesabweichung automatisch vor (WL AR 2025, S. 33). Die Bundesrechnung läuft also separat über Art. 33 Abs. 2 DBG.
> 
> **Offene Punkte:**
> - Der Code «17» ist laut Wiki noch nicht verifiziert, weil Seite 3 der Steuererklärung in der Wegleitung nicht als Miniatur abgebildet ist. Bitte auf dem Original-Formular prüfen.
> - Die Werte sind als «agent-geprüft» markiert: Fundstelle geprüft, Abnahme durch die Fachperson steht noch aus.
> - Der Abzug darf zusammen mit Berufskosten, 3a und BVG-Einkauf den massgebenden Nettolohn nicht übersteigen. Bei Ihren Angaben ist das nicht der Fall, sofern der Nettolohn mindestens 38'000 plus diese Abzüge beträgt.
> 
> Quellen: ar-wl-2025__c0004 (Kanton), bund-dbg-2025__art-33-t6 (Bund), ar-stg-anhang-kp__c0001 (Limiten AR).

## p10

**Frage:** AR 2025: Mandant bewohnt sein Einfamilienhaus am Wohnsitz dauernd selbst (Baujahr 1995, einzige Liegenschaft, keine Fremdvermietung). Mietwert gemäss Grundstückschätzung CHF 24'500; er wählt den Pauschalabzug für den Unterhalt. Was wird wo im Formular 7 und in der Steuererklärung (Staats- und Gemeindesteuer) eingetragen?

**Soll (Referenz):** Formular 7, Teil B.a: Eigenmietwert 24'500 abzüglich Selbstnutzungsabzug 20% (4'900) = Total anrechenbarer Eigenmietwert CHF 19'600 = Total Erträge a. und b. -> Übertrag Steuererklärung Seite 2, Ziff. 5. Teil C: Pauschalabzug (Gebäude über 10 Jahre; Bruttomietertrag des gesamten Liegenschaftsbesitzes nicht über Fr. 100'000) = 20% vom Total Liegenschaftserträge = 20% x 19'600 = CHF 3'920 -> Übertrag Steuererklärung Seite 3, Ziff. 15 (separater Abzug, nicht mit Ziff. 5 verrechnet). Wirkung auf das Einkommen netto CHF 15'680.

**Antwort des Agenten** (34.9 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__formular):

> **Kanton Appenzell Ausserrhoden, Steuerjahr 2025.** Ich habe den Stand der Steuerwiki-Quellen geprüft. Der Eigenmietwert und der Pauschalabzug sind mit ☑️ agent-geprüft markiert (Abnahme offen).
> 
> ## Formular 7 (Hilfsblatt Liegenschaften)
> 
> Da nur eine Liegenschaft vorhanden ist, entfällt das Formular 7Z. Die Werte werden direkt aus Formular 7 übertragen.
> 
> | Abschnitt | Eintrag | Betrag | Status |
> |---|---|---|---|
> | **A** | Steuerwert (Verkehrswert gemäss Grundstückschätzung), Baujahr 1995, Anteil 100 % | **noch offen** (siehe unten) | ☑️ |
> | **B a** | Mietwert CHF 24'500 − 20 % Selbstnutzungsabzug = **anrechenbarer Eigenmietwert CHF 19'600** | 19'600 | ☑️ |
> | **B b** | Miet-/Pachtzinsen, Fremdnutzung | 0 (keine Fremdvermietung) | — |
> | **C** | Unterhalt: **Pauschalabzug C1** (Wahl ankreuzen, keine Belege nötig) | 3'920 (siehe Rechnung) | ☑️ |
> 
> **Pauschalabzug-Rechnung (Kanton):**
> - Baujahr 1995 → Alter am Stichtag der Vermögenssteuer (31.12.2025) = 30 Jahre, also über 10 Jahre → **20 %**.
> - Voraussetzungen erfüllt: Bruttomietertrag des gesamten Besitzes 0 (≤ CHF 100'000), ganz zu Wohnzwecken genutzt.
> - Berechnung: 20 % × 19'600 = **CHF 3'920**. Ich habe die Pauschale auf den Betrag nach dem 20-%-Abzug gerechnet, weil Formular 7 die Erträge (Ziff. B) als Bemessungsgrundlage nennt. Bitte mit der Wegleitung bestätigen, falls die Bemessung eine andere sein sollte.
> 
> ## Steuererklärung (Staats- und Gemeindesteuer)
> 
> | Ziffer | Seite | Inhalt | Betrag |
> |---|---|---|---|
> | **5** | 2 | Ertrag aus Liegenschaften: Eigenmietwert nach 20-%-Abzug (aus Form. 7 B a) | CHF 19'600 |
> | **15** | 3 | Unterhalts- und Verwaltungskosten: Pauschalabzug (aus Form. 7 C1) | CHF 3'920 |
> | **31** | 4 | Liegenschaften, Steuerwert (Code 710), aus Form. 7 A | **offen** |
> 
> Hinweis zu Ziff. 15: Der Code ist laut Quelle nicht verifiziert, weil Seite 3 der Steuererklärung in der Wegleitung nicht als Miniatur abgebildet ist.
> 
> ## Offene Punkte
> 
> 1. **Steuerwert fehlt.** Für Ziff. 31 / Form. 7 A brauche ich den amtlichen Verkehrswert aus der Grundstückschätzung. Der Mietwert CHF 24'500 ist nicht dasselbe. Bitte den Wert aus dem Schätzungsprotokoll nennen.
> 2. **Bund ist nicht belegt.** Das AR-Formular hat keine Bundesspalte. Die Steuerverwaltung nimmt die Abweichungen für die direkte Bundessteuer automatisch vor. Für den Bund sind der 20-%-Selbstnutzungsabzug und der Pauschalabzug in den AR-Quellen nicht geprüft. Dazu müsste die ESTV-Wegleitung geprüft werden.
> 3. **Belege:** Für den Eigenmietwert genügt das Schätzungsprotokoll auf Verlangen. Für die Pauschale sind keine Unterhaltsbelege nötig.
> 
> Quellen: `ar-form-07-2025__c0001`, `__c0002`, `__c0003`, `ar-wl-2025__c0166`, `__c0175`, `ar-form-07z-2025__c0003`.

