# OpenClaw-Testlauf: blindtest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 14 · Lauf: 2026-11-09 14:46
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## b01

**Frage:** Ehepaar in rechtlich und tatsächlich ungetrennter Ehe, weder Beiträge an die 2. Säule noch an die Säule 3a, Kanton ZH, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Zinsen von Sparkapitalien bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2025: Staatssteuer höchstens CHF 8'700 (Grundabzug CHF 5'800, ohne Beiträge an 2. Säule/3a um die Hälfte erhöht). Direkte Bundessteuer 2025: höchstens CHF 5'550 (Grundabzug CHF 3'700, um die Hälfte erhöht).

**Antwort des Agenten** (28.0 s · Tools: 7 Aufrufe steuerwiki__wert, steuerwiki__zeige, steuerwiki__position):

> **Maximaler Abzug 2025 für Versicherungsprämien und Sparzinsen, Ehepaar in ungetrennter Ehe, ohne Beiträge an 2. Säule und 3a (ohne Kinder):**
> 
> | | Staatssteuer ZH | Direkte Bundessteuer |
> |---|---|---|
> | Maximum | **CHF 8'700** | **CHF 5'550** |
> 
> **Fundstellen**
> - Kanton: `zh-wl-2025__c0086` (WL ZH 2025, Ziff. 15). Der Grundbetrag für Verheiratete ist CHF 5'800. Ohne Beiträge an 2. Säule und 3a erhöht er sich um die Hälfte, höchstens auf CHF 8'700. Status: ☑️ agent-geprüft, Abnahme offen.
> - Bund: `bund-dbg-2025__art-33-t5` (Art. 33 Abs. 1bis lit. a DBG). Der Grundbetrag für Ehepaare ist CHF 3'700 (`bund-dbg-2025__art-33-t2`). Ohne Beiträge an 2. Säule und 3a erhöht er sich um die Hälfte auf CHF 5'550. Status: ☑️ agent-geprüft, Abnahme offen.
> - Formular: Ziff. 15 «Versicherungsprämien und Zinsen von Sparkapitalien» (Code 270) in `zh-form-300-2025__c0008`.
> 
> **Wie der Abzug berechnet wird**
> - Die Limite ist ein Höchstbetrag. Abgezogen wird der tiefere Wert aus den tatsächlich bezahlten Prämien und Sparzinsen und dem Maximum. Im Formular Form. 365 wird dazu Teil A (bezahlte Prämien) mit Teil B (Maximalabzug) verglichen.
> - Bezahlte Prämien sind KK-Prämien (nach Prämienverbilligung), Unfall-, Lebens- und Rentenversicherungsprämien sowie Zinsen von Sparkapitalien. Erhaltene Prämienverbilligung wird abgezogen.
> - Die Bundessteuer-Spalte wird separat mit dem Bundeswert ausgefüllt.
> - Die Höchstbeträge «ohne Vorsorge» gelten nur, wenn weder die steuerpflichtigen Personen noch ihre Arbeitgeber Beiträge an 2. Säule oder 3a geleistet haben. Das trifft hier zu.
> 
> **Hinweis:** Die Werte stammen aus dem Wiki und sind agent-geprüft, die Abnahme ist noch offen. Vor der Einreichung sollten die Limiten mit der amtlichen Wegleitung 2025 abgeglichen werden.

## b02

**Frage:** Wie hoch ist im Steuerjahr 2026 der Maximalabzug für Fahrkosten zwischen Wohn- und Arbeitsort im Kanton St.Gallen (Kantons- und Gemeindesteuern) und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2026: Kantons- und Gemeindesteuern max. Fr. 8'000; direkte Bundessteuer max. Fr. 3'300. Es ist ein Maximalabzug, keine Pauschale (bei Teilzeit/unterjährig nicht gekürzt).

**Antwort des Agenten** (22.0 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Steuerjahr 2026, Maximalabzug für Fahrkosten Wohn–Arbeitsstätte:**
> 
> - **Kanton St.Gallen (Kantons- und Gemeindesteuern): CHF 8'000**
>   Fundstelle: sg-stg-2026__art-39. Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> - **Direkte Bundessteuer: CHF 3'300**
>   Fundstelle: bund-dbg-2026__art-26 (Art. 26 Abs. 1 lit. a DBG). Status ☑️ agent-geprüft.
> 
> Die Abzüge werden getrennt deklariert.
> 
> **Ansätze bei Privatfahrzeug (2026):**
> - **SG:** 75 Rappen pro Fahrkilometer (2025: 70 Rappen), nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung nicht zumutbar ist. Der Maximalabzug von CHF 8'000 gilt weiterhin. Fundstelle: sg-mb-8-2026__c0009.
> - **Bund:** 75 Rappen pro Fahrkilometer, ebenfalls nur ohne zumutbares ÖV, Gesamtmaximum CHF 3'300. Fundstelle: bund-mm-2025-09-11-kalte-progression-2026__c0004.
> 
> **Pauschalen:**
> - Velo, Motorfahrrad: CHF 700 pro Jahr (SG und Bund).
> - Motorrad: SG 75 Rappen pro km; Bund 40 Rappen pro km (weisses Kontrollschild).
> 
> **Offener Punkt zu SG:** Die Weisung StB 39 Nr. 3 nennt für 2026 zusätzlich eine zweite Spalte mit CHF 3'300. Der Chunk erklärt deren Bedeutung nicht, deshalb habe ich sie nicht übernommen. Vor der Deklaration sollte geklärt werden, ob es sich um einen eigenen Abzug oder einen Hinweis zur Bundesregelung handelt. Der Maximalbetrag CHF 8'000 nach Art. 39 StG SG ist durch den Gesetzestext belegt.
> 
> Hinweis: Ob ein öffentliches Verkehrsmittel zumutbar ist, entscheidet sich am Einzelfall; die fachliche Beurteilung liegt bei der Fachperson.

## b03

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Welchen Kinderabzug können Eltern für ein 3-jähriges, ein 10-jähriges und ein 16-jähriges (noch minderjähriges) Kind geltend machen?

**Soll (Referenz):** AR (Kantonssteuer) 2025, indexierte Beträge gemäss Anhang 1 StG (bestätigt durch WL AR 2025 Ziff. 23): 3-jähriges Kind (bis Vollendung des 4. Altersjahrs) Fr. 5'300; 10-jähriges Kind (nach Vollendung des 4. bis Vollendung des 15. Altersjahrs) Fr. 7'400; 16-jähriges Kind (nach Vollendung des 15. Altersjahrs bis Volljährigkeit) Fr. 11'600. Gleiche Beträge für volljährige Kinder in Ausbildung bis zum 26. Altersjahr. (Korrigiert nach Bewertung Lauf A: die ursprüngliche Referenz nannte die nicht indexierten Merkblatt-Beträge 5'000/7'000/11'000.)

**Antwort des Agenten** (29.7 s · Tools: 8 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__position):

> **Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Kinderabzug (Staats- und Gemeindesteuer)**
> 
> | Kind | Alter | Formularziffer | Kantonaler Abzug |
> |---|---|---|---|
> | 3 Jahre | bis Vollendung des 4. Altersjahrs | 23.1 | **CHF 5'300** |
> | 10 Jahre | nach dem 4. bis Vollendung des 15. Altersjahrs | 23.2 | **CHF 7'400** |
> | 16 Jahre (minderjährig) | nach dem 15. Altersjahr bis Volljährigkeit | 23.3 | **CHF 11'600** |
> 
> Das Alter wird per Stichtag 31. Dezember 2025 bestimmt. Bei Kindern in Ausbildung gilt Ziffer 23.3 bis zum 26. Altersjahr.
> 
> **Bund (direkte Bundessteuer):** Hier gibt es keine Altersstaffelung. Für jedes minderjährige Kind wird der Sozialabzug von **CHF 6'800** gewährt, also für alle drei Kinder gleich. Die Steuerverwaltung nimmt die Bundesabweichungen im AR-Formular automatisch vor; eine separate Bundesspalte gibt es nicht.
> 
> **Voraussetzungen, die für alle drei Kinder gelten:**
> - Kein Abzug, wenn das Kind Einkünfte über CHF 18'000 hat (laut Ziffer 23.3 inkl. CHF 6'000 frei verfügbar) oder ein Reinvermögen über CHF 250'000.
> - Kein Kinderabzug bei Unterhaltsbeiträgen nach Ziffer 12.2.
> - Schulgelder und Ausbildungskosten sind mit dem Kinderabzug pauschal abgegolten und nicht zusätzlich abziehbar.
> - Bei getrennt besteuerten Eltern wird der Abzug je hälftig geteilt.
> 
> **Hinweis zu abweichenden Beträgen:** Das Merkblatt MB AR 02 nennt CHF 5'000 / 7'000 / 11'000. Diese Beträge sind nicht indexiert. Massgebend für 2025 sind die indexierten Beträge aus Anhang 1 zum StG (Stand 1.1.2024) und die Wegleitung WL AR 2025, und diese sind hier angegeben. Der StG-Text nennt ebenfalls unindexierte Werte.
> 
> **Quellen und Status:**
> - Ziffern 23.1–23.3 und Beträge: WL AR 2025, `ar-wl-2025__c0005`; Anhang 1 StG, `ar-stg-anhang-kp__c0001` (Art. 38 Abs. 1 lit. a Ziff. 1–3).
> - Formularposition: `position ar 2025 23.1/23.2/23.3`.
> - Bund: `bund-dbg-2025__art-35` (CHF 6'800).
> - Status ☑️: Fundstellen sind geprüft, die fachliche Abnahme steht noch aus. Die Formularcodes 23.1–23.3 sind nicht gegen das Originalformular verifiziert, weil Seite 3 der Steuererklärung in der Wegleitung nicht abgebildet ist.

## b04

**Frage:** Alleinstehende Person ohne Kinder mit Beiträgen an die 2. Säule, Kanton Thurgau, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Staats-/Gemeindesteuern und bei der Bundessteuer?

**Soll (Referenz):** TG 2025: Staat max. Fr. 3'500, Bund max. Fr. 1'800 (ohne Beiträge an Säule 2/3a würde beim Bund Fr. 2'700 gelten). Betrag vor Abzug Prämienverbilligungen Krankenkassen.

**Antwort des Agenten** (23.7 s · Tools: 4 Aufrufe steuerwiki__wert):

> **Alleinstehend, ohne Kinder, mit Beiträgen an die 2. Säule, Kanton TG, Steuerjahr 2025:**
> 
> | | Maximaler Abzug (Versicherungsprämien + Sparzinsen) |
> |---|---|
> | **Staats- und Gemeindesteuern TG** | **CHF 3'500** |
> | **Direkte Bundessteuer** | **CHF 1'800** |
> 
> - **Kanton:** Die Obergrenze von CHF 3'500 gilt für Versicherungsprämien und Sparzinsen zusammen. Quelle: `tg-stg__par-34-t3` („b. Fr. 3'500 für die übrigen Steuerpflichtigen").
> - **Bund:** Die Obergrenze von CHF 1'800 gilt ebenfalls für Versicherungsprämien und Sparkapitalzinsen zusammen. Quelle: `bund-dbg-2025__art-33-t2` („1800 Franken für die übrigen Steuerpflichtigen"). Der Betrag von CHF 2'700 gilt nur ohne Beiträge an die Säulen 2 und 3a und entfällt hier.
> - **Formular TG 2025:** Die Angabe steht in Ziff. 14 („Versicherungsprämien und Zinsen von Sparkapitalien").
> 
> Status beider Werte: ☑️ agent-geprüft. Die Fundstellen sind geprüft, die fachliche Abnahme ist noch offen. Die Beurteilung im Einzelfall bleibt bei der Fachperson.

## b05

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wie hoch ist der Kinderabzug für ein noch nicht schulpflichtiges Kind und für ein Kind in Schule oder Ausbildung bei den Kantons-/Gemeindesteuern?

**Soll (Referenz):** SG 2025: noch nicht schulpflichtiges Kind Fr. 7'600 (Ziff. 23.1); Kind in Schule oder Ausbildung (auch volljährig) Fr. 10'800 (Ziff. 23.2).

**Antwort des Agenten** (24.3 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **St.Gallen, Steuerjahr 2025, Kantons-/Gemeindesteuern: Kinderabzug**
> 
> - **Noch nicht schulpflichtiges Kind (Vorschulalter): CHF 7'600** je Kind (Formular Ziff. 23.1)
> - **Kind in Schule oder Ausbildung: CHF 10'800** je Kind (Formular Ziff. 23.2). Dazu gehören auch volljährige Kinder. SG unterscheidet Schule und Ausbildung nicht, der Betrag ist gleich.
> 
> **Voraussetzungen:**
> - Das Kind steht unter Ihrer elterlichen Sorge oder Obhut, und Sie kommen zur Hauptsache für seinen Unterhalt auf.
> - Der Vorschulbetrag berücksichtigt die Verhältnisse per 31.12.
> - Kein Kinderabzug, wenn Sie Unterhaltsbeiträge nach Art. 45 Abs. 1 lit. c StG geltend machen.
> 
> **Zusätzlich möglich:** Ausbildungskostenabzug für Kinder in Ausbildung (Ziff. 23.3). Er beträgt maximal CHF 13'700, nach Abzug von Stipendien und einem Selbstbehalt von CHF 3'200.
> 
> **Fundstellen:** sg-stg-2025__art-48 (Kinderabzüge), sg-wl-2025__c0104 (Ziff. 23.1–23.2), sg-form-32-2025__c0006 (Unterschiede SG/Bund).
> 
> **Status:** ☑️ agent-geprüft. Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> 
> **Bund (separat deklariert, nicht Teil der Antwort oben):** CHF 6'800 pro minderjährigem oder in Ausbildung stehendem Kind, ohne Altersstaffel. Die Steuerermässigung beträgt CHF 263 je Kind.

## b06

**Frage:** Bis wann ist die Steuererklärung 2025 einer natürlichen Person im Kanton Zürich einzureichen, und wie ist vorzugehen, wenn die Frist nicht eingehalten werden kann?

**Soll (Referenz):** ZH, Steuerperiode 2025: Einreichung bis 31. März 2026 (online oder an das Scan-Center). Gesuch um Fristerstreckung ist vor Ablauf der Frist beim Gemeindesteueramt zu stellen. Mahnfristen sind nicht erstreckbar.

**Antwort des Agenten** (37.4 s · Tools: 8 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Kurz: Die Frist ist abgelaufen.** Die ordentliche Einreichefrist für die Steuererklärung 2025 (natürliche Personen, Kanton Zürich) war **31. März 2026**. Heute ist der 9. November 2026.
> 
> **Die Frist ist ohne Fristerstreckung abgelaufen.** Wurde vor dem 31. März 2026 kein Gesuch gestellt, ist eine Erstreckung nicht mehr möglich. Ein Gesuch nach Fristablauf wird abgewiesen (ZStB 132.1, Kap. G.II, zh-zstb-132-1__c0024). Es bleibt nur die Wiederherstellung der Frist, und dafür gelten die Voraussetzungen von § 15 StV bzw. Art. 119 Abs. 2 und 124 Abs. 4 DBG. Zuständig ist das Gemeindesteueramt. Die genauen Voraussetzungen habe ich nicht geprüft.
> 
> **Vorgehen**
> 
> 1. **Prüfen, ob eine Erstreckung bewilligt wurde.** Wenn ja, gilt die neue Frist. Die späteste Erstreckung für Gesuche, die rechtzeitig eingereicht wurden, ist der **30. November 2026** (zh-zstb-132-1__c0024). Das wäre in knapp drei Wochen.
> 2. **Falls keine Erstreckung beantragt wurde:** Sofort das Gemeindesteueramt kontaktieren und ein Gesuch um Wiederherstellung der Frist stellen, mit Begründung. Die Voraussetzungen nach § 15 StV bzw. Art. 119 Abs. 2 DBG sollten vorab geprüft werden.
> 3. **Bei Ablehnung einer Erstreckung:** Aufsichtsbeschwerde an die Finanzdirektion (§ 39 Abs. 2 StV, zh-stv__par-39).
> 4. **Mahnung abwarten.** Mahnfristen können nicht erstreckt werden (WL ZH 2025, zh-wl-2025__c0017). Reicht man trotz Mahnung nichts ein, wird nach der Weisung ZStB 139.2 eingeschätzt (zh-zstb-132-1__c0032). Die Einschätzung dort habe ich nicht geprüft.
> 
> **Offene Punkte und Unsicherheiten**
> 
> - Der Eckwert-Auszug nennt, dass ein erstes Gesuch ohne gegenteiligen Entscheid stillschweigend bewilligt gilt. Das habe ich im geöffneten Chunk nicht gefunden. Vor einer Entscheidung bitte nachprüfen.
> - Die Kosten einer Erstreckung sind in den Quellen nicht genannt.
> - Der Passus zur Erstreckung «von Amtes wegen bis 30. September» gilt laut Chunk nur für selbstständig Erwerbende und Branchenabteilungen, nicht für Lohnbezüger.
> - Die Zinsen auf verspäteter Zahlung habe ich nicht geprüft.
> - Die Bundessteuer wird laut Tool-Ausgabe nicht separat geregelt, sie folgt der kantonalen Frist.
> 
> Falls du mir sagst, ob bis 31. März 2026 ein Gesuch gestellt wurde, kann ich die Lage genauer einordnen.

## b07

**Frage:** Wir sind eine Treuhandfirma und brauchen für Mandanten im Kanton Thurgau (Steuerperiode 2025, natürliche Personen) eine Fristerstreckung. Bei welcher Stelle ist das Gesuch einzureichen und bis wann kann die Frist längstens erstreckt werden?

**Soll (Referenz):** TG: Gesuch beim Gemeindesteueramt, das darüber entscheidet. Erstmals eingereichte Gesuche werden grundsätzlich bis längstens 30. September des Deklarationsjahres (2026) gutgeheissen; zusätzliche Gesuche in begründeten Fällen bis 30. November. Treuhänder/Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen, können für ihre Mandanten ein Gesuch längstens bis 31. Dezember des Deklarationsjahres beantragen. Arbeitsüberlastung ist kein Grund.

**Antwort des Agenten** (27.0 s · Tools: 4 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurz:** Das Gesuch geht an das **Gemeindesteueramt**, das darüber entscheidet. Für Treuhänder ist die späteste Frist der **31. Dezember 2026**.
> 
> **Stelle:** Gesuche um Fristerstreckung für natürliche Personen sind beim Gemeindesteueramt einzureichen (StP 155 Nr. 2, Ziff. 1). Gemeint ist das Amt der Wohnsitzgemeinde, Stand 31.12.
> 
> **Fristen für Steuerjahr 2025 (Deklarationsjahr 2026):**
> 
> | Gesuch | Längstens bis | Voraussetzung |
> |---|---|---|
> | Erstes Gesuch | 30. September 2026 | grundsätzlich gutgeheissen |
> | Weitere Gesuche | 30. November 2026 | nur in begründeten Fällen |
> | Treuhänder/Steuerberater (gewerbsmässig), für ihre Mandanten | 31. Dezember 2026 | Gesuch für Mandanten |
> | Darüber hinaus | – | abgewiesen, ausser ausserordentliche Gründe sind glaubhaft gemacht |
> 
> **Hinweise für die Praxis:**
> - **Arbeitsüberlastung reicht nicht.** Starke berufliche Inanspruchnahme des Vertreters oder fehlende Unterlagen gelten nicht als Grund. Für Gesuche über den 30. November hinaus braucht es eine substanzierte Sachdarstellung.
> - **Gebühr:** Der Erlass § 39b StV TG regelt Gebühren für Fristerstreckungen. Den Betrag für natürliche Personen habe ich nicht verifiziert. Die Quellen nennen nur die Kanzleigebühr von Fr. 30 für juristische Personen. Bitte vor dem Versand prüfen.
> - **Abgabe:** Die Steuererklärung wird elektronisch mit eFisc übermittelt. Danach muss die unterzeichnete Quittung mit dem Original-Hauptformular (Formular 1) beim Gemeindesteueramt eingereicht werden. Erst dann gilt sie als eingereicht.
> 
> **Quellen:** StP 155 Nr. 2, Chunks `tg-stp-155-2__c0001` (Ziff. 1, natürliche Personen) und `tg-stp-155-2__c0002` (Treuhänder, Abweisung nach 30.11.). § 39b StV TG (`tg-stp-155-2`, Suchtreffer `tg-stp-art-39b`). Status: Fundstelle geprüft, Abnahme offen (☑️).

## b08

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Auf welchem Formular wird der Abzug für Versicherungsprämien und Sparzinsen berechnet und in welche Ziffer der Steuererklärung wird das Ergebnis übertragen?

**Soll (Referenz):** AR 2025: Berechnung auf Formular 6 (A: bezahlte Prämien/Zinsen, B: Maximalabzug, C: Abzug = niedrigerer Betrag von A und B). Der Betrag C wird auf Seite 3 der Steuererklärung in Ziffer 14 übertragen.

**Antwort des Agenten** (24.2 s · Tools: 2 Aufrufe steuerwiki__suche, steuerwiki__position):

> **Kanton Appenzell Ausserrhoden, Steuerjahr 2025:** Der Abzug wird auf **Formular 6** berechnet, das Ergebnis wird in **Ziffer 14** der Steuererklärung übertragen.
> 
> **Berechnung auf Formular 6**
> - **Teil A (Code 600 A):** Bruttoprämien der Krankenversicherung, Unfallprämien (ohne NBUV), Lebens- und Rentenversicherungsprämien und Sparzinsen, abzüglich Prämienverbilligungen. Die Formel lautet: a + b + c + d − e.
> - **Teil B/C (Code 600 B):** Maximalabzug. Dieser beträgt CHF 5'400 für Verheiratete bzw. gemeinsam Steuerpflichtige, sonst CHF 2'700, plus CHF 1'000 je Kind mit Kinderabzug.
> - **Ergebnis (Code 600):** der tiefere Betrag aus 600 A und 600 B.
> 
> **Übertrag:** Code 600 wird in Ziffer 14 („Versicherungsprämien und Zinsen von Sparkapitalien“) übertragen.
> 
> **Hinweise**
> - Sachversicherungen (Mobiliar, Haftpflicht, Motorfahrzeug) sind vom Abzug ausgeschlossen. Bei Familien werden die Prämien und Sparzinsen der ganzen Familie eingetragen.
> - Die Wiki-Angabe, dass die Hauptformular-Ziffer 14 nicht separat verifiziert ist, deckt sich mit der Quelle: Der Code 600 stammt aus dem Hilfsblatt. Ich habe die Ziffer auf dem Hauptformular nicht selbst geprüft.
> - Der Bund hat kein eigenes Feld: Die Steuerverwaltung nimmt die Abweichungen für die direkte Bundessteuer automatisch vor. Die Bundeslimiten (CHF 3'700 bzw. 1'800 mit Säule 2/3a, sonst 5'550 bzw. 2'700) gelten nur für die Bundessteuer und stehen nicht im Formular.
> - Die Belege müssen laut Formular 6 nur auf Verlangen eingereicht werden. Der Rückkaufswert-Nachweis für rückkaufsfähige Lebens-/Rentenversicherungen ist dagegen einzureichen.
> 
> **Quellen:** ar-form-06-2025__c0001, c0002 (Formular 6 Teil A/B/C); ar-wl-2025__c0085 und c0114 (Wegleitung Ziff. 14 bzw. Belege); ar-wl-2025__c0179 (Bund). Der Status ist ☑️ agent-geprüft, die Abnahme steht noch aus.

## b09

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wo und wie ist ein Gesuch um Fristverlängerung für die Steuererklärung einer natürlichen Person zu stellen und bis wann?

**Soll (Referenz):** SG 2025: Das Gesuch ist vor Ablauf der Einreichefrist (Datum auf Seite 1 der Steuererklärung) zu stellen, vorzugsweise elektronisch unter www.steuern.sg.ch (mit Registernummer und Geburtsdatum); sonst schriftlich an das Gemeindesteueramt. Es kann eine angemessene Fristverlängerung gewährt werden.

**Antwort des Agenten** (26.3 s · Tools: 5 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kanton St. Gallen, Steuerjahr 2025: Fristverlängerung für natürliche Personen**
> 
> **Wo und wie:**
> - **Elektronisch (bevorzugt):** über die eFristverlängerung auf www.steuern.sg.ch. Angaben: persönliche **Register-Nr.** und **Geburtsdatum**, beide auf Ihrer Steuererklärung aufgedruckt. Das Gesuch wird interaktiv bewilligt oder abgelehnt. (sg-info-fristverlaengerung__c0002, c0003)
> - **Schriftlich:** nur wenn nicht elektronisch gestellt, an das **Gemeindesteueramt**. (sg-wl-2025__c0018)
> 
> **Bis wann:**
> - Das Gesuch muss **vor Ablauf der Einreichefrist** gestellt werden. Die Verlängerung ist nur auf Gesuch hin und nur für eine angemessene Dauer möglich. (sg-wl-2025__c0018)
> - Das **konkrete Datum** steht nicht im Wiki. Es steht auf **Seite 1 der Steuererklärung 2025**. ☑️ agent-geprüft, Abnahme offen.
> 
> **Bedingung:** Eine Fristverlängerung wird nur gewährt, wenn die **fälligen Steuerrechnungen bezahlt** sind. (sg-info-fristverlaengerung__c0002)
> 
> **Offen:**
> - Heute ist der 9. November 2026. Prüfen Sie zuerst das Datum auf Seite 1. Liegt die Einreichefrist bereits zurück, ist ein Gesuch vor Ablauf nicht mehr möglich. Dann bleibt nur der Kontakt mit dem Gemeindesteueramt.
> - Eine Sonderregel für Treuhänder oder Sammelgesuche habe ich in den Quellen nicht gefunden.
> - Die Dauer der Verlängerung ist nicht beziffert.

## b10

**Frage:** Ehepaar im Kanton St.Gallen, Steuerjahr 2025, zwei Kinder mit Kinderabzug, keine Beiträge an die 2. Säule oder Säule 3a bei beiden Partnern. Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Kantons-/Gemeindesteuern und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2025 Kanton: Fr. 6'800 + zusätzlich ohne 2. Säule/3a bis Fr. 1'100 + 2 x bis Fr. 1'100 für die Kinder = Fr. 10'100. Bund: Fr. 3'700 + zusätzlich bis Fr. 1'850 (= Fr. 5'550) + 2 x Fr. 700 = Fr. 6'950. (Voraussetzung für den Zusatzabzug muss bei beiden Partnern erfüllt sein.)

**Antwort des Agenten** (34.7 s · Tools: 7 Aufrufe steuerwiki__wert, steuerwiki__zeige):

> **Ergebnis (Steuerjahr 2025, Kanton SG, Ehepaar, 2 Kinder mit Kinderabzug, keine Beiträge an Säule 2 oder 3a bei beiden Partnern):**
> 
> | | Kanton/Gemeinde SG | Direkte Bundessteuer |
> |---|---|---|
> | Grundbetrag Ehepaar | 6'800 | 3'700 |
> | Zuschlag ohne Säule-2/3a-Beiträge | +1'100 (→ 7'900) | +50 % (→ 5'550) |
> | Zuschlag pro Kind (2 Kinder) | +2 × 1'100 = 2'200 | +2 × 700 = 1'400 |
> | **Maximaler Abzug** | **10'100** | **6'950** |
> 
> **Rechnung und Fundstellen**
> - **SG:** Art. 45 Abs. 1 lit. g StG SG (`sg-stg-2025__art-45-t2`). Der Grundbetrag 6'800 erhöht sich um 1'100, weil keine Beiträge nach lit. d und e abgezogen werden. Zusätzlich erhöht sich der Betrag um 1'100 für jedes Kind, für das ein Kinderabzug geltend gemacht werden kann.
> - **Bund:** Art. 33 Abs. 1 lit. g DBG (`bund-dbg-2025__art-33-t2`) mit Abs. 1bis (`bund-dbg-2025__art-33-t5`). Die Hälfte-Erhöhung gilt für Ehepaare ohne Beiträge nach Abs. 1 lit. d und e (3'700 + 1'850 = 5'550). Dazu kommen 700 pro Kind nach Art. 35 Abs. 1 lit. a/b.
> 
> **Zu beachten**
> - Die Limite gilt für Versicherungsprämien und Sparkapitalzinsen zusammen. Der Kanton SG rechnet Prämienverbilligungen an.
> - Beim Kanton erhöht der Kinderzuschlag den Betrag unabhängig davon, ob Säule-2/3a-Beiträge abgezogen werden. Die Abnahme dieser Lesart ist noch offen.
> - Die Werte sind im Wiki als „agent-geprüft“ markiert: Fundstelle geprüft, Abnahme durch die Fachperson steht noch aus.
> - Die Ziffer im SG-Formular ist Ziff. 14 (Code 600). Die Bundesspalte und die Regel dazu kann ich mit `position sg 2025 14` nachschlagen, falls du die Eintragung brauchst.

## b11

**Frage:** Arbeitnehmer im Kanton Thurgau, Steuerjahr 2026, Arbeitsweg mit ÖV-Jahresabonnement, effektive Kosten Fr. 6'400. Welcher Fahrkostenabzug ist bei den Staats-/Gemeindesteuern und welcher bei der direkten Bundessteuer zulässig?

**Soll (Referenz):** TG 2026: Kanton gesamthaft max. Fr. 6'000, deshalb Abzug Fr. 6'000 (effektive Kosten Fr. 6'400 werden gekürzt). Bund max. Fr. 3'300, deshalb Abzug Fr. 3'300.

**Antwort des Agenten** (23.4 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Kanton Thurgau (Staats- und Gemeindesteuern), Steuerjahr 2026: Fr. 6'000.** Ihre Kosten von Fr. 6'400 werden auf Fr. 6'000 begrenzt.
> 
> **Direkte Bundessteuer 2026: Fr. 3'300.** Der Bund begrenzt auf Fr. 3'300, also sind davon Fr. 3'300 abziehbar.
> 
> Die beiden Plafonds werden getrennt erfasst. Die tatsächlichen ÖV-Abokosten sind für Kanton und Bund gleich, nur der Höchstbetrag unterscheidet sich. In der Steuererklärung TG 2026 tragen Sie die Abokosten im Hilfsblatt Form. 4.2, Ziff. 2.1 (Code 206) ein. Die Summe kommt in Ziff. 2.5 (Code 213), dort gilt der Plafond: Kanton 6'000, Bund 3'300. Die Spalten für Staat und Bund stehen nebeneinander.
> 
> Zwei Bedingungen sind wichtig:
> - **Lohnausweis Feld F darf nicht angekreuzt sein.** Wenn der Arbeitgeber die Arbeitswegkosten vergütet oder ein Geschäftsfahrzeug bzw. GA aus geschäftlichen Gründen stellt, entfällt der Abzug.
> - **Nur ÖV-Abokosten,** die tatsächlich entstanden und belegt sind. Das Abo ist als Beleg einzureichen (Einreichepflicht laut Wiki unklar).
> 
> Quellen: TG 2026 Fahrkosten-Max. (tg-wl-2026__c0176, ☑️ agent-geprüft, Abnahme offen), Bund Art. 26 Abs. 1 lit. a DBG (bund-dbg-2026__art-26, ☑️ agent-geprüft), Formularposition Form. 4.2/4.3 Ziff. 2.1–2.5 (tg-form-04-2-2026__c0002).

## b12

**Frage:** Ehepaar im Kanton Zürich, Steuerjahr 2026, nachgewiesene Kinderdrittbetreuungskosten: Kind A (5 Jahre) Fr. 30'000, Kind B (8 Jahre) Fr. 12'000. Wie hoch ist der Abzug bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2026: Maximum pro Kind Staat Fr. 25'300, Bund Fr. 25'800 (Kinder unter 14). Staat: 25'300 + 12'000 = Fr. 37'300. Bund: 25'800 + 12'000 = Fr. 37'800. (Zum Vergleich 2025: Staat max. Fr. 25'000.)

**Antwort des Agenten** (25.6 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Ergebnis: Staatssteuer Fr. 37'300, direkte Bundessteuer Fr. 37'800.**
> 
> Der Abzug wird pro Kind berechnet als nachgewiesene Kosten, höchstens der Höchstbetrag.
> 
> | Kind | Alter | Nachgewiesen | Staatssteuer ZH (Max. 25'300) | Bundessteuer (Max. 25'800) |
> |---|---|---|---|---|
> | A | 5 | Fr. 30'000 | Fr. 25'300 (gekappt) | Fr. 25'800 (gekappt) |
> | B | 8 | Fr. 12'000 | Fr. 12'000 | Fr. 12'000 |
> | **Total** | | | **Fr. 37'300** | **Fr. 37'800** |
> 
> **Voraussetzungen**
> - Beide Kinder sind unter 14 Jahre alt und leben im gleichen Haushalt. Die Altersgrenze ist 14 Jahre, im Kanton und beim Bund gleich.
> - Bei Ehepaaren müssen beide gleichzeitig erwerbstätig, in Ausbildung oder erwerbsunfähig sein. Nur Kosten während der Arbeits- oder Ausbildungszeit sind abziehbar.
> - Der Abzug von 20 % für Lebenshaltungskosten entfällt, weil die Kosten nachgewiesen (nicht pauschal) sind. Die Regel gilt nur für pauschal ausgewiesene Kosten.
> - Die hälftige Teilung für Konkubinat oder alternierende Obhut betrifft diesen Fall nicht.
> 
> **Formular:** Im Kanton Zürich steht der Abzug in Ziff. 16.6 (Code 376) mit getrennten Spalten für Staatssteuer und Bundessteuer.
> 
> **Quellen und Status**
> - Kanton: Limite Fr. 25'300, Chunk `zh-stg-2026__par-31-t3`, Wegleitung `zh-wl-2026-uj__c0105`. Status ☑️ agent-geprüft, Abnahme offen.
> - Bund: Limite Fr. 25'800, Chunk `bund-dbg-2026__art-33-t7`. Status ☑️ agent-geprüft, Abnahme offen.
> - Die Formularziffer stammt aus der Fassung für die unterjährige Steuerpflicht. Das reguläre Formular ZH 2026 ist laut Wiki noch nicht publiziert (Stand 09.11.2026). Die Ziffer und den Code daher am regulären Formular prüfen, sobald es vorliegt.

## b13

**Frage:** Ein Mitglied der Milizfeuerwehr erhält für die Erfüllung von Kernaufgaben (Übungen, Pikettdienst, Ernstfalleinsätze) Sold. Bis zu welchem Betrag ist der Feuerwehrsold bei der direkten Bundessteuer steuerfrei, im Steuerjahr 2025 und im Steuerjahr 2026?

**Soll (Referenz):** Bund: 2025 steuerfrei bis maximal Fr. 5'300; 2026 steuerfrei bis maximal Fr. 5'400 (Wert hat sich geändert, nicht übertragen). Der gesamte Sold ist auf dem Lohnausweis zu deklarieren; der steuerfreie Betrag wird auf Formular 9 Berufskosten Ziffer 8 abgezogen.

**Antwort des Agenten** (22.9 s · Tools: 2 Aufrufe steuerwiki__wert):

> Bei der direkten Bundessteuer ist der Feuerwehrsold für Kernaufgaben steuerfrei bis:
> 
> - **Steuerjahr 2025: CHF 5'300** pro Jahr
> - **Steuerjahr 2026: CHF 5'400** pro Jahr (2026 neu, Vorjahr 5'300)
> 
> Quellen: Art. 24 Bst. t² DBG, Chunks `bund-dbg-2025__art-24-t2` und `bund-dbg-2026__art-24-t2`. Status beider Werte: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> Für 2026 gilt zusätzlich: Pauschalzulagen für Kader, Funktionszulagen, administrative Arbeiten und freiwillige Dienstleistungen gehören nicht zum steuerfreien Betrag. Der gesamte Sold wird im Lohnausweis deklariert.
> 
> Ich habe nur den Bundeswert abgefragt. Ob der Kanton abweichende Regeln hat, kann ich bei Bedarf für AR, SG, TG oder ZH prüfen; sagen Sie mir dann bitte den Wohnsitzkanton.

## b14

**Frage:** Ein Mandant wohnt am 31.12.2026 im Kanton Luzern und pendelt mit dem Auto zur Arbeit. Welcher Fahrkostenabzug gilt für die Luzerner Staats- und Gemeindesteuern 2026 und für die direkte Bundessteuer?

**Soll (Referenz):** Luzern ist im Wiki nicht abgedeckt (nur Bund, AR, SG, TG, ZH): kein Wert für die Luzerner Staats-/Gemeindesteuer nennen, auf kantonale Wegleitung verweisen. Für die direkte Bundessteuer 2026 gilt max. Fr. 3'300 (Wegleitung Bund 2026).

**Antwort des Agenten** (23.8 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Direkte Bundessteuer 2026:** Die Fahrkosten für das Auto sind nur abziehbar, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist. Dann gilt CHF 0.75 pro Fahrkilometer (ab 2026; 2025 waren es 0.70). Der Gesamtabzug ist auf CHF 3'300 pro Jahr begrenzt. Bei zumutbarem ÖV gilt der Abzug nach tatsächlichen Kosten, maximal CHF 3'300.
> 
> Quellen: `bund-mm-2025-09-11-kalte-progression-2026__c0004` (0.75 Franken), `bund-dbg-2026__art-26` (3'300 Franken), `bund-rs-2-215__c0004` (Tabelle). Status: ☑️ agent-geprüft, Abnahme offen.
> 
> **Kanton Luzern 2026:** Nicht im Wiki. Das Wiki deckt nur Bund, AR, SG, TG und ZH ab, deshalb kann ich hier keinen Luzerner Fahrkostenabzug nennen. Die Luzerner Regel muss aus der offiziellen Luzerner Steuerverwaltung bzw. dem Luzerner Steuerformular 2026 geprüft werden.
> 
> Hinweis: Die Bundesregel gilt für die direkte Bundessteuer. Die Staats- und Gemeindesteuer richtet sich nach dem Kantonsrecht, das ich hier nicht belegen kann.

