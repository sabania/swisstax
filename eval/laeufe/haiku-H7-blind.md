# OpenClaw-Testlauf: blindtest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 14 · Lauf: 2026-11-09 15:47
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## b01

**Frage:** Ehepaar in rechtlich und tatsächlich ungetrennter Ehe, weder Beiträge an die 2. Säule noch an die Säule 3a, Kanton ZH, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Zinsen von Sparkapitalien bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2025: Staatssteuer höchstens CHF 8'700 (Grundabzug CHF 5'800, ohne Beiträge an 2. Säule/3a um die Hälfte erhöht). Direkte Bundessteuer 2025: höchstens CHF 5'550 (Grundabzug CHF 3'700, um die Hälfte erhöht).

**Antwort des Agenten** (27.1 s · Tools: 6 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne):

> **Ergebnis: Ehepaar in ungetrennter Ehe, ohne Beiträge an Säule 2 und 3a, ZH 2025**
> 
> | | Staatssteuer ZH | Direkte Bundessteuer |
> |---|---|---|
> | Maximaler Abzug | **CHF 8'700** | **CHF 5'550** |
> 
> - **Staatssteuer:** Der Grundbetrag für Verheiratete in ungetrennter Ehe ist CHF 5'800. Ohne Beiträge an 2. Säule und 3a erhöht er sich um die Hälfte, max. CHF 8'700 (5'800 × 1.5). Fundstelle: `zh-wl-2025__c0086`, Status ☑️ agent-geprüft (Abnahme offen).
> - **Bundessteuer:** Der Grundbetrag ist CHF 3'700. Ohne Beiträge an Säule 2 und 3a erhöht er sich um die Hälfte, max. CHF 5'550 (3'700 × 1.5). Fundstelle: `bund-dbg-2025__art-33-t5` (Art. 33 Abs. 1bis lit. a DBG), Status ☑️ agent-geprüft (Abnahme offen).
> 
> Die Beträge sind Obergrenzen. Abziehbar ist der tatsächlich bezahlte Betrag bis zu diesem Maximum. Die Erfassung erfolgt im ZH-Formular Ziff. 15, Code 270 («Versicherungsprämien und Zinsen von Sparkapitalien»), mit getrennter Deklaration für Kanton und Bund.
> 
> Ein Kinderzuschlag (ZH CHF 1'300, Bund CHF 700 pro Kind) kommt nur hinzu, wenn Kinder oder unterstützungsbedürftige Personen vorhanden sind. Das ist in der Frage nicht angegeben.

## b02

**Frage:** Wie hoch ist im Steuerjahr 2026 der Maximalabzug für Fahrkosten zwischen Wohn- und Arbeitsort im Kanton St.Gallen (Kantons- und Gemeindesteuern) und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2026: Kantons- und Gemeindesteuern max. Fr. 8'000; direkte Bundessteuer max. Fr. 3'300. Es ist ein Maximalabzug, keine Pauschale (bei Teilzeit/unterjährig nicht gekürzt).

**Antwort des Agenten** (22.4 s · Tools: 2 Aufrufe steuerwiki__wert):

> Im Steuerjahr 2026 gilt für Fahrkosten zwischen Wohn- und Arbeitsort:
> 
> - **Kanton und Gemeinden St.Gallen:** maximal **CHF 8'000** pro Jahr (`sg-stg-2026__art-39`). Das ist ein Höchstbetrag, keine Pauschale.
> - **Direkte Bundessteuer:** maximal **CHF 3'300** pro Jahr (`bund-dbg-2026__art-26`).
> 
> Die beiden Abzüge werden separat deklariert. Beim Kanton gilt der höhere Betrag, beim Bund der tiefere.
> 
> Bei Privatfahrzeugen gelten im Kanton SG wie im Bund 75 Rappen pro Fahrkilometer (2025 waren es 70 Rappen). Im Kanton ist das nur zulässig, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung nicht zumutbar ist, und der Abzug bleibt im Rahmen von CHF 8'000. Im Bund gilt dasselbe, die Obergrenze ist CHF 3'300.
> 
> Hinweis zu einer Unklarheit: Die Weisung StB 39 Nr. 3 nennt für 2026 zusätzlich eine zweite Spalte mit CHF 3'300. Der Chunk erklärt deren Bedeutung nicht, deshalb habe ich sie nicht übernommen. Bitte vor der Deklaration in der Weisung prüfen.
> 
> Status der Werte: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).

## b03

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Welchen Kinderabzug können Eltern für ein 3-jähriges, ein 10-jähriges und ein 16-jähriges (noch minderjähriges) Kind geltend machen?

**Soll (Referenz):** AR (Kantonssteuer) 2025, indexierte Beträge gemäss Anhang 1 StG (bestätigt durch WL AR 2025 Ziff. 23): 3-jähriges Kind (bis Vollendung des 4. Altersjahrs) Fr. 5'300; 10-jähriges Kind (nach Vollendung des 4. bis Vollendung des 15. Altersjahrs) Fr. 7'400; 16-jähriges Kind (nach Vollendung des 15. Altersjahrs bis Volljährigkeit) Fr. 11'600. Gleiche Beträge für volljährige Kinder in Ausbildung bis zum 26. Altersjahr. (Korrigiert nach Bewertung Lauf A: die ursprüngliche Referenz nannte die nicht indexierten Merkblatt-Beträge 5'000/7'000/11'000.)

**Antwort des Agenten** (30.2 s · Tools: 5 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__position):

> **Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Kinderabzug (Staats- und Gemeindesteuer)**
> 
> | Kind | Alter am 31.12.2025 | Kinderabzug | Formularziffer |
> |---|---|---|---|
> | 3 Jahre | bis zur Vollendung des 4. Altersjahrs | **CHF 5'300** | Ziff. 23.1 |
> | 10 Jahre | nach dem 4. bis zur Vollendung des 15. Altersjahrs | **CHF 7'400** | Ziff. 23.2 |
> | 16 Jahre (minderjährig) | nach dem 15. Altersjahr bis zur Volljährigkeit | **CHF 11'600** | Ziff. 23.3 |
> 
> **Quellen:** Anhang 1 StG AR, Art. 38 Abs. 1 lit. a Ziff. 1–3 (`ar-stg-anhang-kp__c0001`), bestätigt durch WL AR 2025 (`ar-wl-2025__c0005`). Status ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen.
> 
> **Voraussetzungen** (WL AR 2025, Ziff. 23):
> - Das Kind steht unter der elterlichen Sorge oder Obhut der steuerpflichtigen Person und wird von ihr hauptsächlich unterhalten.
> - Keine Einkünfte des Kindes über CHF 18'000 (Steuererklärung des Kindes bei eigenen Einkünften beachten).
> - Kein Kinderabzug, wenn für dasselbe Kind Unterhaltsbeiträge nach Ziff. 12.2 abgezogen werden.
> - Bei getrennt besteuerten Eltern wird der Abzug je hälftig geteilt.
> 
> **Widerspruch in den Quellen:** Das Merkblatt MB AR 02 (gültig für 2025–2027) nennt noch CHF 5'000 / 7'000 / 11'000. Das sind die nicht indexierten Gesetzesbeträge. Die WL AR 2025 und Anhang 1 StG verwenden die indexierten Beträge, und die Wiki-Auswertung hält diese für massgebend. Ich habe den Widerspruch nicht abschliessend geklärt. Wenn es auf den genauen Betrag ankommt, sollte die Steuerverwaltung AR bestätigen, welche Beträge für 2025 gelten.
> 
> **Bund (zum Vergleich, separat zu deklarieren):** CHF 6'800 pro minderjähriges Kind, ohne Altersstaffel. Zusätzlich gibt es eine Reduktion des Steuerbetrags um CHF 263 pro Kind. Die Steuerverwaltung nimmt die Bundesabweichungen laut Formular automatisch vor.

## b04

**Frage:** Alleinstehende Person ohne Kinder mit Beiträgen an die 2. Säule, Kanton Thurgau, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Staats-/Gemeindesteuern und bei der Bundessteuer?

**Soll (Referenz):** TG 2025: Staat max. Fr. 3'500, Bund max. Fr. 1'800 (ohne Beiträge an Säule 2/3a würde beim Bund Fr. 2'700 gelten). Betrag vor Abzug Prämienverbilligungen Krankenkassen.

**Antwort des Agenten** (22.6 s · Tools: 4 Aufrufe steuerwiki__wert):

> **Antwort (Kanton TG, Steuerjahr 2025, alleinstehend ohne Kinder, mit Beiträgen an die 2. Säule):**
> 
> | | Maximaler Abzug für Versicherungsprämien und Sparzinsen |
> |---|---|
> | Staats- und Gemeindesteuern TG | **CHF 3'500** |
> | Direkte Bundessteuer | **CHF 1'800** |
> 
> - **Kanton:** Die Obergrenze für übrige Steuerpflichtige steht in § 34 Abs. 3 lit. b StG TG (Fundstelle `tg-stg__par-34-t3`). Status ☑️ agent-geprüft; die Abnahme ist noch offen.
> - **Bund:** Der Ansatz für übrige Steuerpflichtige mit Beiträgen an Säule 2/3a steht in Art. 33 Abs. 2 DBG (Fundstelle `bund-dbg-2025__art-33-t2`). Status ☑️ agent-geprüft; die Abnahme ist noch offen.
> - Die Bundes-Obergrenze von CHF 2'700 gilt nur ohne Beiträge an die Säulen 2 und 3a. Da die Person Beiträge an die 2. Säule leistet, ist sie nicht anwendbar.
> - Kinderzuschläge und die Ehepaar-Beträge (TG CHF 7'000, Bund CHF 3'700) entfallen hier.
> 
> Die Beträge gelten als Obergrenze. Der tatsächlich abziehbare Betrag hängt von den Belegen zu Prämien und Sparzinsen ab. Im Formular TG 2025 steht die Position unter Ziff. 14 (Versicherungsprämien und Zinsen von Sparkapitalien); für die Bundesspalte gilt dieselbe Ziffer, sofern das Formular sie vorsieht. Die genaue Erfassung kann ich mit `position tg 2025 14` nachprüfen.

## b05

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wie hoch ist der Kinderabzug für ein noch nicht schulpflichtiges Kind und für ein Kind in Schule oder Ausbildung bei den Kantons-/Gemeindesteuern?

**Soll (Referenz):** SG 2025: noch nicht schulpflichtiges Kind Fr. 7'600 (Ziff. 23.1); Kind in Schule oder Ausbildung (auch volljährig) Fr. 10'800 (Ziff. 23.2).

**Antwort des Agenten** (24.8 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, message):

> **Kanton St.Gallen, Steuerjahr 2025: Kinderabzug bei den Kantons- und Gemeindesteuern**
> 
> - **Noch nicht schulpflichtiges Kind:** **CHF 7'600** je Kind (Formular Ziff. 23.1, Code 252)
> - **Kind in Schule oder Ausbildung:** **CHF 10'800** je Kind (Formular Ziff. 23.2, Code 254). Das gilt auch für volljährige Kinder in Ausbildung.
> 
> **Zusätzlich, Ausbildungskosten (nur Kanton/Gemeinde):** Für ein Kind mit Abzug nach Ziff. 23.2 können selbst getragene Ausbildungskosten abgezogen werden. Davon werden erhaltene Stipendien und ein Selbstbehalt von **CHF 3'200** abgezogen. Der Abzug ist höchstens **CHF 13'700** (Ziff. 23.3, Code 256).
> 
> **Bedingungen:**
> - Der Abzug gilt nur, wenn zur Hauptsache für den Unterhalt des Kindes aufgekommen wird.
> - Ein Kind, für das Unterhaltsbeiträge nach Ziff. 12.2 abgezogen werden, erhält keinen Kinderabzug.
> - Für das Vorschulkind zählen die Verhältnisse am 31.12.2025 bzw. am Ende der Steuerpflicht; bei unterjähriger Steuerpflicht wird anteilig gerechnet. Der Kindergarten zählt zur Schulpflicht, also gilt dafür Ziff. 23.2.
> 
> **Bund (nur zur Abgrenzung):** einheitlich CHF 6'800 pro Kind, unabhängig vom Alter, plus Abzug vom Steuerbetrag von CHF 263 je Kind.
> 
> **Quellen:** sg-form-1-2025__c0011 (Ziff. 23.1–23.3), sg-wl-2025__c0104 und c0105, sg-form-32-2025__c0006, sg-stg-2025 Art. 48.
> **Status:** ☑️ agent-geprüft. Die Fundstelle ist geprüft, die Abnahme durch die Fachperson steht noch aus.

## b06

**Frage:** Bis wann ist die Steuererklärung 2025 einer natürlichen Person im Kanton Zürich einzureichen, und wie ist vorzugehen, wenn die Frist nicht eingehalten werden kann?

**Soll (Referenz):** ZH, Steuerperiode 2025: Einreichung bis 31. März 2026 (online oder an das Scan-Center). Gesuch um Fristerstreckung ist vor Ablauf der Frist beim Gemeindesteueramt zu stellen. Mahnfristen sind nicht erstreckbar.

**Antwort des Agenten** (30.0 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Kurzantwort:** Die ordentliche Frist für die Steuererklärung 2025 im Kanton Zürich war **31. März 2026**. Heute ist der 9. November 2026, die Frist ist also abgelaufen. Die späteste mögliche Erstreckung endet am **30. November 2026**, also in 3 Wochen.
> 
> **Was jetzt zu tun ist**
> 
> 1. **Prüfen, ob bereits eine Fristerstreckung bewilligt wurde.** Ein rechtzeitiges Gesuch vor dem 31. März 2026 wird höchstens bis 30. November 2026 bewilligt. Das erste Gesuch gilt ohne gegenteiligen Entscheid als stillschweigend bewilligt. Die neue Frist steht im Bewilligungsschreiben oder ist beim Gemeindesteueramt erfragbar.
> 2. **Falls keine Erstreckung besteht oder die bewilligte Frist abgelaufen ist:** Die Erklärung so schnell wie möglich einreichen, online oder beim Scan-Center. Papierform ist ebenfalls zulässig.
> 3. **Falls kein rechtzeitiges Gesuch vorlag:** Ein nachträgliches Gesuch beim Gemeindesteueramt ist nur aus **ausserordentlichen Gründen** möglich. Berufliche Belastung des Vertreters reicht nicht. Die Gründe sollten dokumentiert werden.
> 4. **Mahnungen beachten:** Mahnfristen können nicht erstreckt werden. Wer trotz Mahnung keine Erklärung einreicht, wird nach dem Verfahren für Nichtabgabe eingeschätzt (§ 42 Abs. 3 StV, ZStB 139.2). Dann erfolgt die Einschätzung ohne Erklärung.
> 
> **Besonderheit für Selbstständige:** Die automatische Erstreckung von Amtes wegen gilt nur bis **30. September** des Folgejahres (also 30.09.2026) und ist damit ebenfalls abgelaufen. Hier gilt dasselbe wie oben: Gesuch bzw. Einreichung jetzt, spätestens bis 30.11.2026.
> 
> **Quellen und Status**
> - Frist 31.3.2026: `zh-wl-2025__c0017` (Wegleitung ZH 2025), ☑️ agent-geprüft, Abnahme offen
> - Erstreckung bis 30.11., stillschweigende Bewilligung des ersten Gesuchs, Gemeindesteueramt, Automatik bis 30.9. für Selbständige: `zh-zstb-132-1__c0023` (ZStB 132.1, § 39 StV), ☑️ agent-geprüft, Abnahme offen
> - Nichtabgabe und Mahnung: `zh-zstb-132-1__c0032`, ☑️ agent-geprüft
> - **Offen:** Die Quellen nennen keine Kosten für eine Fristerstreckung. Auch zu den Anforderungen an «ausserordentliche Gründe» steht nichts Konkretes darin. Wie das Gemeindesteueramt nachträgliche Gesuche handhabt, sollte direkt dort erfragt werden.
> 
> Diese Angaben ersetzen keine Beratung durch eine Fachperson. Bei einem komplizierten Fall oder bereits eingetroffener Mahnung empfehle ich, zeitnah das Gemeindesteueramt zu kontaktieren.

## b07

**Frage:** Wir sind eine Treuhandfirma und brauchen für Mandanten im Kanton Thurgau (Steuerperiode 2025, natürliche Personen) eine Fristerstreckung. Bei welcher Stelle ist das Gesuch einzureichen und bis wann kann die Frist längstens erstreckt werden?

**Soll (Referenz):** TG: Gesuch beim Gemeindesteueramt, das darüber entscheidet. Erstmals eingereichte Gesuche werden grundsätzlich bis längstens 30. September des Deklarationsjahres (2026) gutgeheissen; zusätzliche Gesuche in begründeten Fällen bis 30. November. Treuhänder/Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen, können für ihre Mandanten ein Gesuch längstens bis 31. Dezember des Deklarationsjahres beantragen. Arbeitsüberlastung ist kein Grund.

**Antwort des Agenten** (27.6 s · Tools: 4 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kurzantwort:** Das Gesuch geht an das **Gemeindesteueramt** der Wohnsitzgemeinde des Mandanten, nicht an die kantonale Steuerverwaltung. Für Treuhänder und Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen, ist die Frist **längstens bis 31. Dezember 2026**.
> 
> **Steuerjahr 2025, Deklarationsjahr 2026:**
> 
> | Gesuch | Längste Frist | Voraussetzung |
> |---|---|---|
> | Erstes Gesuch | 30. September 2026 | wird grundsätzlich gutgeheissen |
> | Weitere Gesuche (Private) | 30. November 2026 | nur in begründeten Fällen |
> | Gewerbsmässige Treuhänder/Steuerberater für ihre Mandanten | 31. Dezember 2026 | Gesuch durch den Treuhänder |
> | Darüber hinaus | keine | nur bei ausserordentlichen, glaubhaft gemachten Gründen |
> 
> **Weitere Punkte:**
> - Arbeitsüberlastung des Vertreters ist kein Grund. Glaubhaft machen muss man ausserordentliche Gründe mit einer konkreten Sachdarstellung; allgemeine Hinweise wie berufliche Inanspruchnahme oder fehlende Unterlagen reichen nicht.
> - Das Gesuch ist schriftlich und begründet einzureichen. Die Bewilligung oder Ablehnung ergeht schriftlich.
> - Es gibt eine Gebühr für Fristerstreckungen (§ 39b StV TG). Den Betrag für natürliche Personen habe ich nicht verifiziert; die Quellen nennen nur die Kanzleigebühr von Fr. 30 für juristische Personen.
> 
> **Quellen:** StP 155 Nr. 2 (`tg-stp-155-2__c0001`, `c0002`), § 39b StV TG (`tg-stp-155-2`-Suchtreffer, Volltext nicht geöffnet). Status: agent-geprüft, Abnahme offen. Die Praxis-Aussage zum 31. Dezember steht im Chunk unmittelbar nach der 30.-November-Regel; ich habe sie wörtlich geprüft, aber die fachliche Abnahme steht noch aus.

## b08

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Auf welchem Formular wird der Abzug für Versicherungsprämien und Sparzinsen berechnet und in welche Ziffer der Steuererklärung wird das Ergebnis übertragen?

**Soll (Referenz):** AR 2025: Berechnung auf Formular 6 (A: bezahlte Prämien/Zinsen, B: Maximalabzug, C: Abzug = niedrigerer Betrag von A und B). Der Betrag C wird auf Seite 3 der Steuererklärung in Ziffer 14 übertragen.

**Antwort des Agenten** (22.2 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__suche):

> **Kanton Appenzell Ausserrhoden, Steuerjahr 2025:**
> 
> Die Berechnung erfolgt im **Formular 6** (Hilfsblatt Versicherungsprämien/Krankheitskosten). Das Ergebnis wird in **Ziffer 14** des Hauptformulars übertragen, Code **600**.
> 
> **Ablauf im Formular 6:**
> - **Teil A, Code 600 A:** Summe aus Krankenversicherung (brutto), Unfallversicherung (ohne NBUV), Lebens- und Rentenversicherungen und Sparzinsen, abzüglich Prämienverbilligungen.
> - **Teil B, Code 600 B:** Maximalabzug. Fr. 5'400 bei gemeinsam Steuerpflichtigen, Fr. 2'700 für übrige, plus Fr. 1'000 je Kind mit Kinderabzug (Ziff. 23.1–23.3).
> - **Teil C, Code 600:** Der niedrigere Betrag aus A und B, also min(600 A; 600 B). Dieser Wert geht in Ziffer 14.
> 
> **Hinweise:**
> - Nicht abzugsfähig sind NBUV, Mobiliar-, Motorfahrzeug-, Haftpflicht- und andere Sachversicherungen.
> - Familien tragen die Prämien und Sparzinsen der ganzen Familie im selben Formular ein.
> - Der Bund hat keine eigene Spalte. Die Steuerverwaltung nimmt die Abweichungen für die direkte Bundessteuer automatisch vor (WL AR 2025, ar-wl-2025__c0179).
> 
> **Fundstellen und Status:**
> - Formular 6, Teil A/B/C: ar-form-06-2025__c0001 und c0002 (☑️ agent-geprüft, Abnahme offen)
> - Ziffer 14: ar-wl-2025__c0085 und Abschnitt «Abzüge» (☑️ agent-geprüft, Abnahme offen)
> 
> **Offen:** Das Hauptformular selbst ist nicht online. Der Code 600 für Ziffer 14 ist im Wiki nicht separat verifiziert, er stammt aus dem Hilfsblatt. Vor dem Ausfüllen empfiehlt sich ein Blick auf das amtliche Formular.

## b09

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wo und wie ist ein Gesuch um Fristverlängerung für die Steuererklärung einer natürlichen Person zu stellen und bis wann?

**Soll (Referenz):** SG 2025: Das Gesuch ist vor Ablauf der Einreichefrist (Datum auf Seite 1 der Steuererklärung) zu stellen, vorzugsweise elektronisch unter www.steuern.sg.ch (mit Registernummer und Geburtsdatum); sonst schriftlich an das Gemeindesteueramt. Es kann eine angemessene Fristverlängerung gewährt werden.

**Antwort des Agenten** (24.7 s · Tools: 6 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Kanton St. Gallen, Steuerjahr 2025: Fristverlängerung für eine natürliche Person**
> 
> **Wo und wie:**
> - **Elektronisch (bevorzugt):** über die eFristverlängerung auf www.steuern.sg.ch. Dafür brauchen Sie die **Register-Nummer** und das **Geburtsdatum**, beide stehen auf Ihrer persönlichen Steuererklärung. Das Gesuch wird interaktiv bewilligt oder abgelehnt. (WL SG 2025, S. 8, `sg-wl-2025__c0018`; SG Fristverlängerung Privatpersonen, `sg-info-fristverlaengerung__c0002`/`c0003`)
> - **Schriftlich:** wenn nicht elektronisch gestellt, an das **Gemeindesteueramt** Ihrer Wohngemeinde (`sg-wl-2025__c0018`).
> 
> **Bis wann:**
> - Das Gesuch muss **vor Ablauf der Einreichefrist** gestellt werden. Die Verlängerung wird nur auf Gesuch hin und nur als «angemessene» Frist gewährt (`sg-wl-2025__c0018`).
> - Das **konkrete Datum** der Einreichefrist steht im Wiki nicht. Es ist auf **Seite 1 Ihrer Steuererklärung 2025** aufgedruckt (`sg-wl-2025__c0018`). Die Dauer der Verlängerung ist in den Quellen nicht beziffert.
> 
> **Bedingung:** Eine Fristverlängerung wird nur gewährt, wenn **fällige Steuerrechnungen bezahlt** sind (`sg-info-fristverlaengerung__c0002`).
> 
> **Offen / nicht geprüft:**
> - Ob für Treuhänder oder Vertreter eine eigene Fristregel gilt (Sammelgesuch o. Ä.), ist in den Quellen nicht gefunden.
> - Der Bund hat keine eigene Fristverlängerung; sie wird kantonal geregelt (Wiki-Eintrag Bund).
> 
> **Status:** Die Fundstellen sind agent-geprüft, die Abnahme durch die Fachperson steht noch aus. Für das genaue Datum bitte die Seite 1 der Steuererklärung 2025 prüfen.

## b10

**Frage:** Ehepaar im Kanton St.Gallen, Steuerjahr 2025, zwei Kinder mit Kinderabzug, keine Beiträge an die 2. Säule oder Säule 3a bei beiden Partnern. Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Kantons-/Gemeindesteuern und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2025 Kanton: Fr. 6'800 + zusätzlich ohne 2. Säule/3a bis Fr. 1'100 + 2 x bis Fr. 1'100 für die Kinder = Fr. 10'100. Bund: Fr. 3'700 + zusätzlich bis Fr. 1'850 (= Fr. 5'550) + 2 x Fr. 700 = Fr. 6'950. (Voraussetzung für den Zusatzabzug muss bei beiden Partnern erfüllt sein.)

**Antwort des Agenten** (35.3 s · Tools: 9 Aufrufe steuerwiki__wert, steuerwiki__zeige, steuerwiki__position, steuerwiki__rechne, message):

> **SG, Steuerjahr 2025, Ehepaar (gemeinsam steuerpflichtig), 2 Kinder mit Kinderabzug, keine Beiträge an Säule 2 / 3a bei beiden Partnern**
> 
> **Kanton/Gemeinde (SG): max. CHF 10'100**
> - Grundbetrag Ehepaar: 6'800
> - Zuschlag ohne 2. Säule/3a (Ehegatten): +1'100
> - Kinderzuschlag: 2 × 1'100 = +2'200
> 
> **Direkte Bundessteuer: max. CHF 6'950**
> - Grundbetrag Ehepaar: 3'700
> - Zuschlag ohne 2. Säule/3a: +1'850
> - Kinderzuschlag: 2 × 700 = +1'400
> 
> Der tatsächlich abziehbare Betrag ist der tiefere Wert von (Prämien + Sparzinsen − Prämienverbilligungen) und dem Maximum. Der Zuschlag ohne Vorsorge gilt nur, wenn bei beiden Partnern keine Beiträge abgezogen werden, was hier zutrifft.
> 
> **Fundstellen und Status**
> - SG: StG SG Art. 45 (`sg-stg-2025__art-45-t2`), Formular Ziff. 14 / Code 600 (`sg-form-1-2025__c0009`). Status ☑️ agent-geprüft, Abnahme offen.
> - Bund: DBG Art. 33 (`bund-dbg-2025__art-33-t2`, `art-33-t5`), RS 2-210 (`bund-rs-2-210__c0006`). Status ☑️ agent-geprüft, Abnahme offen.
> - Die Summen habe ich mit dem Rechentool geprüft.
> 
> **Zu beachten**
> - Die Werte sind agent-geprüft; die fachliche Abnahme steht noch aus.
> - Prämienbelege sind laut Formular teils nur auf Verlangen einzureichen. Bei Zinsen mit Verrechnungssteuer (Bruttozins > Fr. 200) gehört der Bankbeleg bei.
> - Nicht abziehbar sind Mobiliar-, Motorfahrzeug-, Haftpflicht- und andere Sachversicherungen.

## b11

**Frage:** Arbeitnehmer im Kanton Thurgau, Steuerjahr 2026, Arbeitsweg mit ÖV-Jahresabonnement, effektive Kosten Fr. 6'400. Welcher Fahrkostenabzug ist bei den Staats-/Gemeindesteuern und welcher bei der direkten Bundessteuer zulässig?

**Soll (Referenz):** TG 2026: Kanton gesamthaft max. Fr. 6'000, deshalb Abzug Fr. 6'000 (effektive Kosten Fr. 6'400 werden gekürzt). Bund max. Fr. 3'300, deshalb Abzug Fr. 3'300.

**Antwort des Agenten** (26.5 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Ergebnis TG, Steuerjahr 2026, ÖV-Jahresabonnement, effektive Kosten Fr. 6'400:**
> 
> | | Staats- und Gemeindesteuern TG | Direkte Bundessteuer |
> |---|---|---|
> | Höchstbetrag Fahrkosten | Fr. 6'000 | Fr. 3'300 |
> | **Zulässiger Abzug** | **Fr. 6'000** | **Fr. 3'300** |
> 
> Die nachgewiesenen Abokosten von Fr. 6'400 werden für den Kanton auf Fr. 6'000 und für den Bund auf Fr. 3'300 begrenzt. Die Differenz von Fr. 400 bzw. Fr. 3'100 ist nicht abziehbar.
> 
> **Hinweise zur Erfassung im Formular TG 2026:**
> - **Form. 4.2 (bzw. 4.3 für Person 2), Ziff. 2.1** (Code 206): Abonnementskosten Fr. 6'400 eintragen. Voraussetzung ist, dass im Lohnausweis Feld F **nicht** angekreuzt ist. Ist der Arbeitsweg vom Arbeitgeber vergütet oder gratis, entfällt der Abzug.
> - **Ziff. 2.5** (Code 213): Plafond Kanton Fr. 6'000, Bund Fr. 3'300. Die Spalten Staat und Bund sind getrennt zu führen.
> - **Belege:** Das ÖV-Abonnement sollte beigelegt werden. Die Einreichepflicht ist laut Wiki unklar, daher vorsorglich einreichen.
> - Ein Auto-Abzug kommt nur bei unzumutbarer ÖV-Nutzung in Frage und ist hier nicht einschlägig.
> 
> **Quellen:** TG-Wegleitung 2026 (tg-wl-2026__c0176, c0177), Form. 4.2 Ziff. 2.1/2.5 (tg-form-04-2-2026__c0002); Bund: DBG Art. 26 Abs. 1 lit. a (bund-dbg-2026__art-26). Status: agent-geprüft, Abnahme durch Fachperson noch offen.

## b12

**Frage:** Ehepaar im Kanton Zürich, Steuerjahr 2026, nachgewiesene Kinderdrittbetreuungskosten: Kind A (5 Jahre) Fr. 30'000, Kind B (8 Jahre) Fr. 12'000. Wie hoch ist der Abzug bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2026: Maximum pro Kind Staat Fr. 25'300, Bund Fr. 25'800 (Kinder unter 14). Staat: 25'300 + 12'000 = Fr. 37'300. Bund: 25'800 + 12'000 = Fr. 37'800. (Zum Vergleich 2025: Staat max. Fr. 25'000.)

**Antwort des Agenten** (27.5 s · Tools: 4 Aufrufe steuerwiki__wert, steuerwiki__rechne, steuerwiki__position):

> **Ergebnis (Kanton Zürich, Steuerjahr 2026, Ehepaar, beide Kinder unter 14 Jahren):**
> 
> | | Kind A (5 J.) | Kind B (8 J.) | Total |
> |---|---|---|---|
> | Nachgewiesen | 30'000 | 12'000 | |
> | **Staatssteuer** (Max. 25'300 pro Kind) | 25'300 | 12'000 | **Fr. 37'300** |
> | **Bundessteuer** (Max. 25'800 pro Kind) | 25'800 | 12'000 | **Fr. 37'800** |
> 
> - **Staatssteuer:** Kind A ist auf den Höchstbetrag von Fr. 25'300 gekürzt, Kind B wird voll mit Fr. 12'000 abgezogen.
> - **Bundessteuer:** Kind A ist auf Fr. 25'800 gekürzt, Kind B wie oben. Der Bund hat einen eigenen Höchstbetrag und wird separat deklariert.
> 
> **Formular:** ZH Ziff. 16.6, «Abzug für fremdbetreute Kinder», Code 376. Die Spalten «Staatssteuer» und «Bundessteuer» sind getrennt auszufüllen.
> 
> **Zu beachten:**
> - Der Abzug gilt nur für Kosten während der Erwerbs-, Ausbildungs- oder Erwerbsunfähigkeitszeit. Bei einem Ehepaar müssen beide gleichzeitig erwerbstätig bzw. in Ausbildung sein.
> - Die 20%-Kürzung für Lebenshaltungskosten gilt nur bei pauschal ausgewiesenen Kosten. Hier sind die Kosten nachgewiesen, daher entfällt sie. Das setzt voraus, dass Rechnungen und Zahlungsnachweise vorliegen.
> - Nicht abziehbar sind z.B. Sport, Musik, Vereine, Schulgeld und Nachhilfe.
> 
> **Status der Werte:** Die Höchstbeträge (ZH 25'300 / Bund 25'800) und das Höchstalter 14 Jahre sind ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen. Die reguläre Formular-/Wegleitung 2026 ist laut Wiki noch nicht publiziert. Die Ziffer 16.6 stützt sich auf die Fassung für unterjährige Steuerpflicht, daher sollte sie am regulären Formular nochmals geprüft werden.
> 
> Quellen: `zh-stg-2026__par-31-t3` (ZH-Limite), `bund-dbg-2026__art-33-t7` (Bund), `zh-form-300-2026-uj__c0008`, `zh-wl-2026-uj__c0105`.

## b13

**Frage:** Ein Mitglied der Milizfeuerwehr erhält für die Erfüllung von Kernaufgaben (Übungen, Pikettdienst, Ernstfalleinsätze) Sold. Bis zu welchem Betrag ist der Feuerwehrsold bei der direkten Bundessteuer steuerfrei, im Steuerjahr 2025 und im Steuerjahr 2026?

**Soll (Referenz):** Bund: 2025 steuerfrei bis maximal Fr. 5'300; 2026 steuerfrei bis maximal Fr. 5'400 (Wert hat sich geändert, nicht übertragen). Der gesamte Sold ist auf dem Lohnausweis zu deklarieren; der steuerfreie Betrag wird auf Formular 9 Berufskosten Ziffer 8 abgezogen.

**Antwort des Agenten** (21.8 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Direkte Bundessteuer, Sold der Milizfeuerwehr (Kernaufgaben):**
> 
> - **Steuerjahr 2025:** bis **CHF 5'300** pro Jahr steuerfrei.
> - **Steuerjahr 2026:** bis **CHF 5'400** pro Jahr steuerfrei. Der Betrag steigt gegenüber 2025 um CHF 100.
> 
> Quellen: Chunk `bund-dbg-2025__art-24-t2` (2025) und `bund-dbg-2026__art-24-t2` (2026). Beide Werte sind agent-geprüft (☑️): Fundstelle geprüft, Abnahme noch offen.
> 
> Hinweise zu 2026 aus dem Chunk:
> - Pauschalzulagen für Kader, Funktionszulagen, administrative Arbeiten und freiwillige Dienstleistungen gehören nicht zum befreiten Sold.
> - Der gesamte Sold wird im Lohnausweis deklariert.
> 
> Der Wert gilt für den Bund. Für die Kantonssteuer brauche ich den Kanton (AR, SG, TG oder ZH), weil kantonale Ansätze abweichen können.

## b14

**Frage:** Ein Mandant wohnt am 31.12.2026 im Kanton Luzern und pendelt mit dem Auto zur Arbeit. Welcher Fahrkostenabzug gilt für die Luzerner Staats- und Gemeindesteuern 2026 und für die direkte Bundessteuer?

**Soll (Referenz):** Luzern ist im Wiki nicht abgedeckt (nur Bund, AR, SG, TG, ZH): kein Wert für die Luzerner Staats-/Gemeindesteuer nennen, auf kantonale Wegleitung verweisen. Für die direkte Bundessteuer 2026 gilt max. Fr. 3'300 (Wegleitung Bund 2026).

**Antwort des Agenten** (25.0 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Luzern (LU) ist im Steuer-Wiki nicht abgedeckt.** Ich kann Ihnen dafür keinen kantonalen Fahrkostenabzug nennen. Das Wiki deckt nur Bund, AR, SG, TG und ZH ab. Die Luzerner Staats- und Gemeindesteuern 2026 müssen Sie daher anhand der kantonalen Quellen prüfen.
> 
> **Direkte Bundessteuer 2026** (Wohnsitz 31.12.2026 in LU, Steuerjahr 2026):
> 
> - **Maximalabzug:** CHF 3'300 pro Jahr für die Fahrten zwischen Wohn- und Arbeitsstätte (Art. 26 Abs. 1 lit. a DBG; Fundstelle `bund-dbg-2026__art-26`).
> - **Privatauto:** CHF 0.75 pro Fahrkilometer (neu ab 2026, Vorjahr 0.70). Der Abzug gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist. Das Gesamtmaximum bleibt CHF 3'300 (`bund-mm-2025-09-11-kalte-progression-2026__c0004`; RS 2-215).
> - **Status:** ☑️ agent-geprüft. Die Fundstellen sind geprüft, die Abnahme steht noch aus.
> 
> **Offene Punkte für den Fall:**
> 
> 1. Ob für den Mandanten ein öffentliches Verkehrsmittel zumutbar ist, entscheidet, ob er den Autoabzug überhaupt geltend machen darf. Dazu brauchen wir die Angaben zum Arbeitsweg, z. B. Fahrzeit und Verbindung mit dem ÖV.
> 2. Mit 0.75 CHF/km erreicht der Abzug den Höchstbetrag von CHF 3'300 bei rund 4'400 einfachen Fahrkilometern pro Jahr. Die tatsächliche Kilometerzahl ist also entscheidend.
> 3. Für Luzern brauchen wir den kantonalen Abzug aus den LU-Quellen, bevor Sie die Staats- und Gemeindesteuer ausfüllen.

