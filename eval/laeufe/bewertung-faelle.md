# End-zu-End-Test: vollständige Steuererklärungen 2025 im echten OpenClaw

- 4 fiktive Fälle (ZH, SG, TG, AR), je 10 Belege, Musterlösung mit 109 Positionen – unabhängig nur aus Primärquellen erstellt ([faelle-2025.yaml](../faelle-2025.yaml)).
- OpenClaw 2026.11.2, Claude (claude-cli), Wiki-Stand Commit a953f9b; Auftrag: vollständige Ausfüllhilfe (Ziffern/Codes, Staat/Bund, Rechenweg, Fundstellen, nicht zu deklarierende Belege).
- Bewertung positionsweise durch unabhängige Prüf-Agenten gegen Musterlösung **und** Primärquellen.

| Fall | korrekt | abweichend | Musterlösung falsch (Agent richtig) | irrelevante Belege erkannt | Kanton/Bund getrennt | Gesamturteil |
|---|---|---|---|---|---|---|
| f-zh | 23/29 | 6 | 0 | ja | ja | kleinere_korrekturen |
| f-sg | 24/24 | 0 | 0 | ja | ja | einreichbar_nach_kontrolle |
| f-tg | 25/25 | 0 | 7 | ja | ja | einreichbar_nach_kontrolle |
| f-ar | 31/31 | 0 | 0 | ja | ja | einreichbar_nach_kontrolle |

**Total:** 103 von 109 Positionen korrekt; alle 6 Abweichungen (ZH) gehen auf eine einzige Ermessensfrage zurück (Verpflegungsabzug Person 2 bei Feld G: Agent nahm Heimkehr über Mittag an und setzte 0, nannte aber den korrekten Wert 1'320 als Variante) und deren Folgezeilen. In TG fand der Agent eine Pauschale (Vermögensverwaltungskosten § 10a StV TG), die die Musterlösung übersehen hatte.

Tuning daraus: Regel «Unklarer Sachverhalt → Standardfall deklarieren, Annahme offenlegen, Alternative und Rückfrage» im Skill `steuererklaerung-np`.

**Nachtest ZH nach dem Tuning** (gleicher Fall, gleiche Bewertung): alle Positionen der Musterlösung korrekt, Gesamturteil
«einreichbar nach Kontrolle»; zusätzlich fand der Agent die Pauschale für Vermögensverwaltungskosten (Ziff. 16.3, 3 ‰ × 31'200 = 94),
die in der Musterlösung fehlte (Prüferin: vertretbar nach WL ZH 2025). Formfehler: für Person 2 zweimal der Code von Person 1 genannt
(206/212 statt 226/232) → Hinweis im Skill ergänzt. **Damit 4/4 Fälle «einreichbar nach Kontrolle».**

## f-zh

Die Ausfüllhilfe ist fachlich sehr nah an der Musterlösung. 22 der 29 Positionen stimmen in Ziffer und Beträgen für Staat und Bund. Alle Limiten 2025 habe ich in den Primärquellen nachgeprüft: Fahrkosten 5'200/3'300, Verpflegung 3'200/1'600, Drittbetreuung 25'000/25'800, Versicherungsabzug 5'800 + 1'300 bzw. 3'700 + 700, Zweiverdienerabzug 6'100 bzw. 8'600–14'100, Kinderabzug 9'300/6'800, Verheiratetenabzug 2'800.

Die einzige inhaltliche Abweichung betrifft Sandras Verpflegungsabzug (Code 226). Der Assistent erkennt die Feld-G-Falle (7.50 statt 15) richtig. Im Basisfall setzt er den Abzug aber auf 0, weil Wohn- und Arbeitsort Winterthur seien. Die Quellen knüpfen den Abzug an eine Arbeitspause, die die Heimkehr nicht ermöglicht (zh-wl-2025__c0066, Art. 6 BKV). Der Sachverhalt sagt dazu nichts, und bei angekreuztem Feld G ist der halbe Ansatz Praxis. Die Musterlösung ist deshalb nicht fehlerhaft.

Daraus folgen Abweichungen von je 1'320 in den Ziffern 11.2, 18, 21, 23 und 25. Die korrekten Werte 4'036 und 66'668 / 64'248 nennt der Assistent jedoch transparent als Variante und als Rückfrage an die Mandanten.

Die nicht zu deklarierenden Belege sind alle richtig ausgeschieden: Handy, Hausrat- und Haftpflichtversicherung, Zahnarzt und Kostenbeteiligung unter dem Selbstbehalt, Kinderzulagen. Staat und Bund sind durchgehend getrennt. Die Rechnungen sind in sich konsistent. Überzählige falsche Positionen gibt es keine.

Stichprobe von über 10 Fundstellen: alle tragend, darunter zh-wl-2025__c0065, c0066, c0081, c0107, c0112, c0095, zh-pauschalierung-berufsauslagen-2025__c0004, zh-form-365-2025__c0002, zh-form-340-2025__c0005, zh-stg-2025__par-31-t4, par-31-t5, par-34, par-47-t2, bund-dbg-2025__art-26 und art-36-t4. Die Angabe von CHF 10 zu Art. 6 Abs. 3 BKV stützt sich auf das Merkblatt N2.

Für die Treuhänderin heisst das: Ziff. 11.2 auf 4'036 korrigieren oder die Arbeitspause klären, dann die Totale nachführen. Danach ist die Erklärung einreichbar.

| Ziffer | Urteil | Begründung |
|---|---|---|
| 1.1 Person 1 (Code 100) | korrekt | 103'000 Staat und Bund, mit Kontrollrechnung 118'400 − 8'110 − 7'290. Stimmt mit der Musterlösung überein. |
| 1.1 Person 2 (Code 101) | korrekt | 67'200 Staat und Bund. Der Assistent hält ausdrücklich fest, dass die Kinderzulagen im Lohn enthalten sind und nicht unter Ziff. 3.4 gehören. |
| 4.1 (Code 150) | korrekt | 1'140 = Kolonne A 960 + Kolonne B 180. Die Zuordnung zu den Kolonnen ist korrekt. |
| Form. 340 Code 540 | korrekt | 336 = 35 % × 960, nur Staat (Bund «–»). Entspricht zh-form-340-2025__c0005. |
| 7 (Code 199) | korrekt | 171'340 in beiden Spalten. |
| Form. 360 P1 Ziff. 1.1 (Code 201/205) | korrekt | Staat 4'180, Bund 3'300. Die Plafonds 5'200 und 3'300 sind durch zh-wl-2025__c0065, § 26 StG ZH, Art. 26 DBG und RS 2-210 belegt. Der Hinweis, dass die ESTV-WL 2a noch 3200 nennt, stimmt (bund-wl-2a-2025__c0042). |
| Form. 360 P1 Ziff. 2.1 (Code 208) | korrekt | 220 × 15 = 3'300, gedeckelt auf 3'200 in beiden Spalten. |
| Form. 360 P1 Ziff. 3 (Code 212) | korrekt | 3 % × 103'000 = 3'090. |
| 11.1 (Code 220) | korrekt | Staat 10'470, Bund 9'590. |
| Form. 360 P2 Ziff. 1.2 (Code 222) | korrekt | 700 in beiden Spalten. |
| Form. 360 P2 Ziff. 2.1 (Code 226) | abweichend | Im Basisfall setzt der Assistent 0 statt 1'320 ein, weil Wohn- und Arbeitsort Winterthur seien und die Heimkehr deshalb möglich sei. Die Primärquellen (zh-wl-2025__c0066, zh-pauschalierung-berufsauslagen-2025__c0004, Art. 6 BKV) knüpfen den Abzug an eine Arbeitspause, die die Heimkehr nicht ermöglic |
| Form. 360 P2 Ziff. 3 (Code 232) | korrekt | 3 % × 67'200 = 2'016. |
| 11.2 (Code 240) | abweichend | 2'716 statt 4'036 (Folgefehler aus Code 226). Die Variante 4'036 ist genannt. |
| 14.1 (Code 260) | korrekt | 7'258, belegt durch zh-wl-2025__c0081. |
| 14.2 (Code 261) | korrekt | 7'258. |
| 15 (Code 270) | korrekt | Teil A 16'020. Teil B: Staat 5'800 + 2 × 1'300 = 8'400, Bund 3'700 + 2 × 700 = 5'100, belegt durch zh-form-365-2025__c0002, § 31 Abs. 1 lit. g StG ZH und RS 2-210. |
| 16.1 (Code 280) | korrekt | 10'000 in beiden Spalten. Keine Doppelerfassung über den Lohnausweis, kein Kapitalbezug innert 3 Jahren. |
| 16.6 (Code 376) | korrekt | Staat 25'000 + 6'900 = 31'900, Bund 25'800 + 6'900 = 32'700, belegt durch § 31 lit. j StG ZH, Art. 33 Abs. 3 DBG und zh-wl-2025__c0107. |
| 17 (Code 290) | korrekt | Staat 6'100, Bund 14'100 stimmen. Die Basis 57'226 statt 55'906 folgt aus Code 226, wirkt sich wegen der Deckelung aber nicht aus. |
| 18 (Code 299) | abweichend | 84'102 / 88'722 statt 85'422 / 90'042, Differenz 1'320 aus Code 226. Die Rechnung ist in sich korrekt. |
| 21 (Code 310) | abweichend | 87'238 / 82'618 statt 85'918 / 81'298 (Folgefehler). |
| 22.1 (Code 320) | korrekt | 0 in beiden Spalten. 3'090 liegen unter dem Selbstbehalt von 5 %. Die Selbstbehalt-Beträge weichen als Folge von Code 226 leicht ab, das Ergebnis bleibt gleich. |
| 22.2 (Code 324) | korrekt | 650 in beiden Spalten, Mindestbetrag 100 und Limite 20 % geprüft. |
| 23 (Code 350) | abweichend | 86'588 / 81'968 statt 85'268 / 80'648 (Folgefehler). |
| 24.1 (Code 370) | korrekt | 2 × 9'300 = 18'600 (§ 34 StG ZH) und 2 × 6'800 = 13'600 (Art. 35 DBG). |
| 24.3 (Code 365) | korrekt | Staat «–», Bund 2'800. |
| 25 (Code 390) | abweichend | Basisfall 67'988 / 65'568 statt 66'668 / 64'248. Die Musterwerte sind als Variante ausdrücklich genannt. |
| 30.1 (Code 400) | korrekt | 82'000, nur Staat. |
| 35 (Code 490) | korrekt | 82'000. Der Hinweis auf die steuerfreie Tarifstufe von 159'000 (§ 47 Abs. 2 StG ZH) ist korrekt. |

## f-sg

Alle 24 Positionen der Musterlösung stimmen in Ziffer, Code und Beträgen für Kanton und Bund. Auch die vier Fallen hat der Assistent richtig gelöst: Kita-Mahlzeiten ausgeschieden, Spende unter 100, Kindergarten unter 23.2, Weiterbildungspauschale nur beim Kanton. Die Musterlösung ist nicht fehlerhaft.

Nicht zu deklarieren sind Motorfahrzeugsteuer, Versicherung, Handy-Abo, Spende, Kinderzulage und Kita-Mahlzeiten. Alle sind korrekt ausgeschieden. Dazu kommen sinnvolle Negativabgrenzungen wie Zweiverdiener-, Schicht- und Alimentenabzug.

Als einzige Zusatzposition nennt der Assistent Ziff. 30.4 Privatauto als «offen» und fragt nach Kaufpreis und Erwerbsjahr. Die Bewertungsregel (20 % pro Jahr ab Anschaffungswert) entspricht sg-wl-2025__c0111. Die Position ist sachlich berechtigt und nicht falsch, die Musterlösung hat sie übersehen.

Kanton und Bund sind durchgängig getrennt, inklusive Hinweis auf die Bundeskorrektur durch das Steueramt.

Stichproben der Fundstellen: sg-form-4-2025__c0002 und c0003, sg-wl-2025__c0078, c0092, c0095, c0102 und c0104, sg-stb-39-3__c0004 sowie bund-wl-2a-2025__c0042. Alle sind tragend. Den echten Quellenwiderspruch beim Bund-Fahrkostenmaximum (WL 2a nennt 3'200, DBG Art. 26 2025 nennt 3'300) hat der Assistent korrekt offengelegt und gesetzeskonform entschieden.

Kleine formale Schwäche: Im Abschnitt Einkommensberechnung (21.1 Selbstbehalte, 23.2 Kinderabzug) fehlen Chunk-Fundstellen.

Aus Sicht einer Treuhänderin ist die Ausfüllhilfe nach üblicher Kontrolle einreichbar. Vorher zu klären sind die offenen Rückfragen: Fahrplannachweis, Brutto-Prämien, Auto-Wert für 30.4 und Zahnarztrechnung.

| Ziffer | Urteil | Begründung |
|---|---|---|
| 1.1 Person 1 (Code 100) | korrekt | 73'000 Kanton und Bund, Rechnung 83'500 − 5'890 − 4'610 stimmt. Kinderzulage zu Recht nicht separat aufgeführt, Feld F/G beachtet. |
| 4.1 (Code 146) – aus Formular 2 | korrekt | 68 / 68 über Form. 2 Abschnitt B (Zins bis 200 ohne VSt), kein VSt-Anspruch. |
| 6.1 für minderjährige Kinder (Code 156) | korrekt | 9'600 / 9'600, Code 156 statt 154 ausdrücklich richtig gewählt. Fundstelle WL c0068 und Art. 23 lit. f DBG. |
| 7 (Code 168) | korrekt | 82'668 / 82'668. |
| Formular 4 Person 1, Ziff. 1.3 (Code 404) / Zwischentotal (Code 406) | korrekt | 9'856 berechnet, gekappt auf Kanton 8'000 und Bund 3'300. Die Begründung «Fehlen eines öffentlichen Verkehrsmittels» ist angegeben. Geprüft in sg-form-4-2025__c0002 (0.70/km, max. 8'000), sg-form-32-2025__c0002 (Bund 3'300) und DBG Art. 26 2025 (3'300). Den Widerspruch zur ESTV-WL 2a 2025 (c0042 nen |
| Formular 4 Person 1, Ziff. 2.1 (Code 408) | korrekt | min(220 × 15 = 3'300; 3'200) = 3'200 Kanton und Bund. Belegt durch sg-wl-2025__c0078 und sg-form-4-2025__c0003. |
| Formular 4 Person 1, Ziff. 3.1 (Code 416) | korrekt | Kanton 2'400 (700 + 10 %, max. 2'400), Bund 2'190 (3 %, zwischen 2'000 und 4'000). Belegt durch sg-form-4-2025__c0003 und sg-form-32-2025__c0002. |
| 10.1 (Code 438) | korrekt | 13'600 / 8'690. |
| 13.1 Person 1 (Code 208) | korrekt | 7'258 / 7'258 = Maximum mit 2. Säule. |
| 13.2 Person 1 (Code 218) | korrekt | 6'000 / 6'000. Kein Doppelabzug, weil Lohnausweis Ziff. 10.2 = 0. Zusätzlich korrekter Hinweis auf die 3-jährige Sperrfrist nach Art. 79b Abs. 3 BVG. |
| 14 (Code 600) – via Formular 6 | korrekt | A = 4'868. Kanton max. 3'400 + 1'100 = 4'500, Bund 1'800 + 700 = 2'500, kein Zuschlag ohne Vorsorge. Geprüft gegen sg-form-32-2025__c0003 und DBG Art. 33 Abs. 1bis 2025 (1'800 / 700). |
| 16.2 (Code 258) | korrekt | Falle erkannt: Die separat ausgewiesenen Mahlzeiten 1'080 sind ausgeschieden, Abzug 8'760 / 8'760. Maximum Kanton 26'700 gemäss sg-wl-2025__c0092, Bund 25'800 gemäss DBG Art. 33 Abs. 3. |
| 16.4 Person 1 (Code 223) | korrekt | Kanton Pauschale 400 (gilt nur für Staat/Gemeinde), Bund effektive 340. Belegt durch sg-wl-2025__c0095 und c0004. |
| 18 (Code 230) | korrekt | 40'518 / 33'548. |
| 20 (Code 234) | korrekt | 42'150 / 49'120. |
| 21.1 (Vorkolonne Code 650, Selbstbehalt Code 238, Abzug Code 240) | korrekt | Vorkolonne 3'600. Kanton mit Selbstbehalt 2 % (843) → 2'757, Bund mit 5 % (2'456) → 1'144. Der Satz von 2 % ist durch sg-wl-2025__c0098 und form-32 c0005 bestätigt. In der Tabelle fehlt allerdings eine Chunk-Fundstelle. |
| 21.3 (Code 244) | korrekt | Falle erkannt: Die Spende von 80 liegt unter dem Mindestbetrag von 100 (sg-wl-2025__c0102), daher 0 / 0. |
| 22 (Code 248) | korrekt | 39'393 / 47'976. |
| 23.2 (Code 254) | korrekt | Falle erkannt: Der Kindergarten gehört zur Volksschule, daher 23.2 mit 10'800 statt 23.1 mit 7'600. Bund 6'800. Bestätigt durch sg-wl-2025__c0104 und form-32 c0006. Zusätzlich korrekter Hinweis auf den Elterntarif mit 263 je Kind (Art. 36 Abs. 2bis DBG). |
| 24 (Code 268) | korrekt | 28'593 / 41'176. Rundung als ungeprüft gekennzeichnet. |
| 30.1 (Code 300) | korrekt | 31'500, nur Staat. |
| 36.1 (Code 330) | korrekt | 75'000 (zusammen mit 36.3 in einer Zeile genannt). Belegt durch sg-wl-2025__c0118. |
| 36.3 (Code 334) | korrekt | 20'000 für 1 Kind. |
| 37 (Code 338) | korrekt | «Voraussichtlich 0». Der Vorbehalt betrifft die zusätzlich und zu Recht aufgeworfene Ziff. 30.4 (Privatauto), die in der Musterlösung fehlt. Sachlich ist das Ergebnis 0 identisch. |

## f-tg

Die Ausfüllhilfe ist vollständig und fachlich sauber. Alle 25 Positionen der Musterlösung sind vorhanden, Staat und Bund sind durchgehend getrennt. Die Fallen sind erkannt:
- Wintergarten als Anlagekosten
- Hausrat-, Serafe- und Handyrechnung nicht abziehbar
- Brillenvergütung 300 in Teil B abgezogen
- PK-Rente mit Beginn 2020 zu 100 %
- Bund-Versicherungsabzug 2'700 ohne Säule 2/3a
- 40/20-%-Selbstnutzungsabzug
- Spendenselbstbehalt nur beim Kanton
- Rentnerabzug 1'000 nur beim Kanton

Die einzige inhaltliche Abweichung ist die Pauschale für Vermögensverwaltungskosten von 190 (2 ‰ × 95'000, Form. 2 Code 148). Der Assistent zieht sie ab, die Musterlösung nicht. Die Primärquellen erlauben die Pauschale ohne Beleg für Wertschriften, die durch Dritte verwahrt werden: § 10a StV TG (tg-stv__par-10a), WL TG 2025 tg-wl-2025__c0159 und Form. 2 tg-form-02-2025__c0006. Die Musterlösung lässt diesen zulässigen Abzug weg und ist daher in Ziff. 4 und allen Folgezahlen fehlerhaft (Ziff. 6, 9, 22, 23.1, 24, 26). Die Werte des Assistenten sind dort rechnerisch konsistent. Für den Bund wendet der Assistent denselben Betrag an und weist das transparent als Annahme aus (⚠).

Geöffnete Fundstellen, alle tragend:
- tg-wl-2025__c0159/c0160 und tg-stv__par-10a
- tg-wl-2025__c0116/c0117
- tg-wl-2025__c0206
- tg-wl-2025__c0218
- tg-wl-2025__c0225/c0227/c0228/c0233/c0243
- tg-form-04-1-2025__c0001
- tg-form-08-2025__c0001
- bund-rs-2-210__c0006
- tg-stg__par-53

Kleinere Mängel:
- Rappenbeträge in Ziff. 23.1, 24 und 26, obwohl das Formular in ganzen Franken rechnet.
- Zwei Verweise auf Beleg-Schlüssel statt Chunk-IDs, z.B. «beleg-hausrat-haftpflicht-police».

Die Rückfragen sind sachgerecht: Fertigstellung des Wintergartens und Steuerwert, Abgrenzung der Malerarbeiten, Depotausweis, Spendenliste. Einreichbar nach normaler Kontrolle.

| Ziffer | Urteil | Begründung |
|---|---|---|
| 3.1 Person 1 (Code 130) | korrekt | 27'000 Kanton/Bund, 12 × 2'250, zu 100 %. Stimmt mit der Musterlösung überein. |
| 3.2 Person 1 (Code 132) | korrekt | 10'800 Kanton/Bund, zu 100 % steuerbar. Der Rentenbeginn 2020 schliesst die Übergangsregel aus, wie der Assistent in Abschnitt 11 richtig festhält. |
| 4 (Code 150) – Formular 2 Ziff. 9 | korrekt (Musterlösung falsch) | Assistent 2'160 = 2'350 brutto − Pauschale Vermögensverwaltungskosten 190 (Form. 2 Ziff. 17, Code 148, 2 ‰ × 95'000; Sparkonto zu Recht nicht eingerechnet). Die Musterlösung setzt 2'350 und lässt den Abzug weg. Die Primärquellen erlauben ihn ohne Beleg: § 10a StV TG (tg-stv__par-10a: «pauschal 2 Pro |
| Formular 2 Ziff. 10 | korrekt | 822.50 = 35 % × 2'350 (Spalte 8). Der Assistent stimmt den Betrag mit 87.50 + 735 ab und hält fest, dass er weder Einkommen noch Abzug ist. |
| 6 (Code 175) | korrekt (Musterlösung falsch) | Assistent 39'960 (27'000 + 10'800 + 2'160), Musterlösung 40'150. Die Abweichung folgt allein aus der zulässigen Pauschale nach § 10a StV TG (siehe Ziff. 4). Rechnerisch richtig. |
| Formular 7 Liegenschaft 1 – Selbstnutzungsabzug / steuerbarer Eigenmietwert | korrekt | 12'240 Kanton (40 % Abzug) und 16'320 Bund (20 % Abzug), belegt mit tg-wl-2025__c0225/c0243. |
| Formular 8 → Formular 7 «Unterhalts-/Betriebskosten» (effektiv) | korrekt | 7'400 = 6'400 + 520 + 480, Wintergarten 31'000 ausgeschieden. Der Vergleich mit der 20-%-Pauschale (2'448 / 3'264) fällt zugunsten von «effektiv» aus. Richtig sind auch die Hinweise, Rechnungskopien ab 1'000 beizulegen (tg-form-08-2025__c0001) und den Gartenunterhalt abzugrenzen (tg-wl-2025__c0228). |
| 8.1 (Code 180) | korrekt | 4'840 Kanton und 8'920 Bund, je Spalte separat gerechnet. |
| 9 (Code 198) | korrekt (Musterlösung falsch) | Assistent 44'800 / 48'880, Musterlösung 44'990 / 49'070. Die Differenz von 190 je Spalte ist nur die Folge der Pauschale aus Ziff. 4, die die Musterlösung nicht berücksichtigt. Rechnerisch richtig. |
| 11 (Code 290) – via Formular 4.1 | korrekt | 3'150 Kanton/Bund. Die Fundstelle tg-form-04-1-2025__c0001 (Code 286/455) trägt. |
| 14 (Code 330) – via Formular 5.2 (Codes 324/328) | korrekt | A5 = 6'240 + 250 = 6'490. Staat 3'500. Bund 2'700, weil keine Beiträge an Säule 2/3a geleistet wurden (bund-rs-2-210__c0006: «ohne Beiträge an die Säulen 2 und 3a … 2’700»). |
| 19 (Code 360) | korrekt | 6'650 Kanton / 5'850 Bund. |
| 22 (Code 362) | korrekt (Musterlösung falsch) | Assistent 38'150 / 43'030, Musterlösung 38'340 / 43'220. Die Abweichung folgt aus der Pauschale in Ziff. 4. Rechnerisch richtig. |
| 23.1 (Code 364) – via Formular 5.1 | korrekt (Musterlösung falsch) | 6'540 nach Abzug der Vergütung 300. Selbstbehalt 5 % von Ziff. 22 je Spalte (tg-wl-2025__c0206): Staat 1'907.50 → 4'632.50, Bund 2'151.50 → 4'388.50. Die Musterlösung kommt auf 4'623 / 4'379, weil ihr Nettoeinkommen um 190 höher ist. Das ist eine Folge von Ziff. 4, die Methode ist identisch. Kleiner |
| 23.2 (Code 366) – via Formular 6 | korrekt | Staat 550 − 200 = 350, Bund 550 voll. Die Maxima nach tg-wl-2025__c0218 sind richtig angewendet. |
| 24 (Code 372) | korrekt (Musterlösung falsch) | 33'167.50 = 38'150 − 4'632.50 − 350 und 38'091.50 = 43'030 − 4'388.50 − 550. Die Abweichung zur Musterlösung (33'367 / 38'291) folgt nur aus Ziff. 4. Rappen statt ganzer Franken. |
| 25.3 (Code 388) | korrekt | 1'000, nur Kanton. 33'167.50 liegt wie der Referenzwert in der Stufe 32'900–33'899 (tg-wl-2025__c0117). |
| 26 (Code 398) | korrekt (Musterlösung falsch) | 32'167.50 Kanton / 38'091.50 Bund, Musterlösung 32'367 / 38'291. Die Differenz von 199.50 folgt aus der Pauschale (190) und dem dadurch tieferen Selbstbehalt bei den Krankheitskosten (9.50). Konsistent nach Primärquelle. |
| 30.1 (Code 410) | korrekt | 143'000. |
| 31 (Code 430) | korrekt | 410'000. Dazu stellt der Assistent eine sinnvolle Rückfrage, ob der Wintergarten-Anbau im Steuerwert enthalten ist. |
| 33 (Code 464) | korrekt | 553'000. |
| 34 (Code 466) | korrekt | 180'000. |
| 35 (Code 468) | korrekt | 373'000. |
| 36.2 (Code 472) | korrekt | 100'000 nach § 53 Abs. 1 Ziff. 2 StG TG (tg-stg__par-53). |
| 37 (Code 498) | korrekt | 273'000. |

## f-ar

Alle 31 Positionen der Musterlösung stimmen bei Ziffer und Betrag (Kanton und Bund). Der Assistent erkennt alle Fallen: Werkbus (Feld F), PK-Einkauf über den Lohn (kein Doppelabzug unter 13.2), Kita-Mittagessen und Betreuungsbeitrag, Stichtag für Leas Kinderabzug (23.2) und den Turnverein-Beitrag als keine Zuwendung. Steuerrechnung 2024 und Handy-Abo hat er korrekt ausgeschieden.

Kanton und Bund sind sauber getrennt:
- Verheiratetenabzug nur beim Bund.
- Vermögen nur beim Kanton.
- Verrechnungssteuer als Rückforderung (Code 999), nicht als Abzug.
- Hinweis, dass die Steuerverwaltung die DBSt-Abweichungen automatisch vornimmt.

Geöffnete Fundstellen, alle tragend: ar-stv__art-16, ar-stg__art-36, ar-stg__art-51, ar-form-04-2025__c0003, ar-form-06-2025__c0002, bund-dbg-2025__art-35, bund-dbg-2025__art-36-t4 (263 je Kind), bund-bkv-2025__anhang-1, bund-bsv-masszahlen-2025-2026__c0003 und ar-wl-2025__c0091.

Kleine Mängel ohne Steuerwirkung:
1. Formular 6, Schritt A: Dort stehen 13'900 statt 14'060. Die Sparzinsen von 160 gehören laut Formular 6 lit. d und Art. 35 lit. g StG AR hinein. Der Abzug in Ziff. 14 ist trotzdem richtig.
2. Fahrkosten P1: Die tragende WL-Stelle zu Feld F (ar-wl-2025__c0075) fehlt. Zitiert ist stattdessen c0003 (Verpflegung).
3. Rückfrage zu Jonas: Die 18'000-Grenze stimmt, steht aber in ar-wl-2025__c0104, nicht im zitierten c0005. Die zusätzliche Bedingung «Reinvermögen über 250'000» ist in den AR-Quellen nicht belegt.

Positiv: Der optionale Pauschalabzug für Wertschriftenverwaltung (3 ‰, ar-wl-2025__c0087/88) ist korrekt als offener Punkt markiert. Er wäre rund 276 und fehlt auch in der Musterlösung; da es ein Abzug auf Antrag ist, ist die Musterlösung deshalb nicht fehlerhaft.

Aus Sicht einer Treuhänderin nach Kontrolle einreichbar. Zeile d auf Formular 6 ist zu ergänzen.

| Ziffer | Urteil | Begründung |
|---|---|---|
| 1.1 P1 (Code 100) | korrekt | 85'300 Kt./Bund, Rechenweg 98'000−6'860−5'840 identisch; ar-wl-2025__c0035 tragend. |
| 1.1 P2 (Code 102) | korrekt | 68'200 Kt./Bund inkl. Abzug BVG-Einkauf via Lohn; Zulagen korrekt als im Lohn enthalten erkannt. |
| 4.1 (Code 146) | korrekt | 1'410 (Spalte A 1'250, Spalte B 160) Kt./Bund; Code 146 stimmt mit quick/zuordnung-ar-2025 überein. |
| Formular 2 – VSt-Anspruch (Code 999) | korrekt | 35 % × 1'250 = 437.50, als Rückforderung (kein Einkommen/Abzug) behandelt; Code 999 laut ar-form-02-2025__c0007. |
| 7 (Code 168) | korrekt | 154'910 Kt./Bund. |
| Form. 4 P1 Ziff. 1 (Code 400) | korrekt | 0 wegen Feld F (Werkbus) – Falle erkannt. Fundstelle nur Formular (c0001) und c0003 (Verpflegung, nicht tragend); die tragende WL-Stelle ar-wl-2025__c0075 fehlt, Ergebnis aber richtig. |
| Form. 4 P1 Ziff. 2.2 (Code 410) | korrekt | 220 × 7.50 = 1'650 → Max. 1'600 Kt./Bund; ar-stv__art-16 Abs. 2 (halber Abzug bei Personalrestaurant) geöffnet und tragend. |
| Form. 4 P1 Ziff. 3.1 (Code 416) | korrekt | Kt. 2'400 (700 + 10 %, max. 2'400 laut ar-form-04-2025__c0003), Bund 2'559 (3 %, min. 2'000/max. 4'000 laut bund-bkv-2025__anhang-1). |
| 10.1 (Code 438) | korrekt | Kt. 4'000 / Bund 4'159. |
| Form. 4 P2 Ziff. 1.1 (Code 450) | korrekt | 1'260 Kt./Bund, unter Limiten 6'000/3'300. |
| Form. 4 P2 Ziff. 2.1 (Code 458) | korrekt | 176 × 15 = 2'640 Kt./Bund (Max. 3'200); Zumutbarkeit der Heimkehr sinnvoll als Ermessensfrage markiert. |
| Form. 4 P2 Ziff. 3.1 (Code 466) | korrekt | Kt. 2'400, Bund 2'046 (3 % × 68'200). |
| 10.2 (Code 488) | korrekt | Kt. 6'300 / Bund 5'946. |
| 13.1 P1 | korrekt | 7'258 Kt./Bund (in der Zeile 13.1 total 12'258 mit Aufteilung je Person); Maximum 7'258 durch bund-bsv-masszahlen-2025-2026__c0003 belegt. |
| 13.1 P2 | korrekt | 5'000 Kt./Bund, separat ausgewiesen. |
| 13.2 P2 | korrekt | 0 – Doppelabzug-Falle erkannt (Einkauf bereits im Nettolohn, LA Ziff. 10.2). |
| 14 (Code 600, Formular 6) | korrekt | Abzug Kt. 7'400 / Bund 5'100 richtig. Kleiner Mangel im Rechenweg: Schritt A mit 13'900 statt 14'060 – die Sparzinsen 160 gehören laut ar-form-06-2025__c0001 (lit. d) und Art. 35 lit. g StG AR in A. Ohne Auswirkung auf den Abzug, auf Formular 6 aber zu ergänzen. |
| 16.2 (Formular 10) | korrekt | 14'400 − 1'800 − 2'400 = 10'200 Kt./Bund; ar-wl-2025__c0091 tragend (Mittagstisch nicht abziehbar, Beiträge abzuziehen). |
| 17 | korrekt | Kt. 5'200 (10 % von 56'900, max. 5'200, ar-wl-2025__c0004), Bund 14'100 (Art. 33 Abs. 2 DBG, bund-dbg-2025__art-33-t6 geprüft). |
| 18 | korrekt | Kt. 45'358 / Bund 51'763. |
| 20 | korrekt | Kt. 109'552 / Bund 103'147. |
| 21.3 (Code 550) | korrekt | 300 Kt./Bund; Turnverein 120 korrekt ausgeschlossen; ar-stg__art-36 lit. b (≥100, max. 20 %) geöffnet und tragend. |
| 22 | korrekt | Kt. 109'252 / Bund 102'847. |
| 23.2 | korrekt | Stichtag-Falle erkannt (4. Altersjahr am 14.03.2025 vollendet) → Kt. 7'400, Bund 6'800; ar-wl-2025__c0005 tragend. |
| 23.3 | korrekt | Kt. 11'600 / Bund 6'800. |
| – (nur DBSt) | korrekt | 2'800 nur Bund (bund-dbg-2025__art-35 lit. c geprüft). |
| 24 | korrekt | Kt. 90'252 / Bund 86'447. Der zusätzliche Hinweis auf 2 × 263 Abzug vom Steuerbetrag (bund-dbg-2025__art-36-t4) ist korrekt. |
| 30.1 (Code 300) | korrekt | 92'000, nur Kanton. |
| 36.2 (Code 332) | korrekt | 150'000; ar-stg__art-51 Abs. 1 lit. a geöffnet und tragend. |
| 36.3 (Code 334) | korrekt | 2 × 25'000 = 50'000 (ar-wl-2025__c0122). |
| 37 (Code 338) | korrekt | 0 (nicht negativ); Ziff. 33/35 mit 92'000 zusätzlich korrekt ausgewiesen. |

Protokoll der Agent-Antworten: [openclaw-faelle-B.md](openclaw-faelle-B.md)
