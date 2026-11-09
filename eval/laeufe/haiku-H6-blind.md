# OpenClaw-Testlauf: blindtest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 14 · Lauf: 2026-11-09 15:17
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## b01

**Frage:** Ehepaar in rechtlich und tatsächlich ungetrennter Ehe, weder Beiträge an die 2. Säule noch an die Säule 3a, Kanton ZH, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Zinsen von Sparkapitalien bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2025: Staatssteuer höchstens CHF 8'700 (Grundabzug CHF 5'800, ohne Beiträge an 2. Säule/3a um die Hälfte erhöht). Direkte Bundessteuer 2025: höchstens CHF 5'550 (Grundabzug CHF 3'700, um die Hälfte erhöht).

**Antwort des Agenten** (28.7 s · Tools: 6 Aufrufe steuerwiki__wert, steuerwiki__zeige, steuerwiki__position):

> **Maximalabzug für Versicherungsprämien und Sparzinsen, Ehepaar in ungetrennter Ehe, ohne Beiträge an 2. Säule und 3a, Steuerjahr 2025**
> 
> | | Kanton ZH (Staatssteuer) | Bund (direkte Bundessteuer) |
> |---|---|---|
> | Maximalabzug | **CHF 8'700** | **CHF 5'550** |
> | Formularzeile | Ziff. 15, Code 270 | Bundesspalte derselben Ziffer |
> 
> - **Grundlage:** Der Regelabzug für Ehepaare beträgt CHF 5'800 (Kanton) bzw. CHF 3'700 (Bund). Wenn weder die Steuerpflichtigen noch ihr Arbeitgeber Beiträge an die 2. Säule oder 3a geleistet haben, erhöht sich der Abzug um die Hälfte. Die Obergrenzen sind dann CHF 8'700 bzw. CHF 5'550.
> - **Quelle:** WL ZH 2025, Abzüge Ziff. 15 (S. 15), Chunk `zh-wl-2025__c0086`. Der Bundeswert ist in derselben Passage genannt und stimmt mit `bund-dbg-2025__art-33-t5` überein.
> - **Zinsen:** Sparzinsen teilen sich den Betrag mit den Prämien und haben keinen eigenen Höchstbetrag.
> - **Tatsächlich bezahlte Beträge:** Der abziehbare Betrag ist der tiefere Wert aus den tatsächlich bezahlten Prämien und Sparzinsen einerseits und dem Maximum andererseits. Die Prämien sind nach Prämienverbilligung anzugeben. Die Bundesspalte wird separat ausgefüllt.
> - **Kinder:** Kein Zuschlag, sofern keine Kinder oder unterstützungsbedürftigen Personen geltend gemacht werden. Sonst gilt je Kind CHF 1'300 (Kanton) bzw. CHF 700 (Bund).
> 
> **Status:** ☑️ agent-geprüft. Die Fundstellen sind geprüft, die fachliche Abnahme steht noch aus.

## b02

**Frage:** Wie hoch ist im Steuerjahr 2026 der Maximalabzug für Fahrkosten zwischen Wohn- und Arbeitsort im Kanton St.Gallen (Kantons- und Gemeindesteuern) und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2026: Kantons- und Gemeindesteuern max. Fr. 8'000; direkte Bundessteuer max. Fr. 3'300. Es ist ein Maximalabzug, keine Pauschale (bei Teilzeit/unterjährig nicht gekürzt).

**Antwort des Agenten** (24.3 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Steuerjahr 2026, Maximalabzug Fahrkosten Wohn- und Arbeitsstätte:**
> 
> **Kanton St.Gallen (Kantons- und Gemeindesteuern): CHF 8'000**
> - Maximalabzug für die notwendigen Fahrkosten bis Fr. 8'000 (Art. 39 StG SG). Er gilt für Haupt- und Nebenerwerb insgesamt.
> - Privatauto: 75 Rappen pro Fahrkilometer (2025: 70 Rappen), nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung nicht zumutbar ist. Der Betrag liegt im Rahmen der Fr. 8'000.
> - Velo, Motorfahrrad, Kleinmotorrad: Pauschale Fr. 700.
> - Quelle: `sg-stg-2026__art-39`; km-Ansatz `sg-mb-8-2026__c0009`.
> - Offener Punkt: Die Weisung StB 39 Nr. 3 nennt für 2026 zusätzlich eine zweite Spalte mit Fr. 3'300. Der Chunk erklärt deren Bedeutung nicht, deshalb übernehme ich sie nicht. Das sollte vor einer Abgabe geklärt werden.
> 
> **Direkte Bundessteuer: CHF 3'300**
> - Maximalabzug für die notwendigen Fahrkosten bis Fr. 3'300 pro Jahr (Art. 26 Abs. 1 lit. a DBG). Gleicher Betrag wie 2025.
> - Privatauto: 75 Rappen pro Fahrkilometer, nur wenn kein öffentliches Verkehrsmittel zur Verfügung steht. Gesamtmaximum Fr. 3'300.
> - Motorrad mit weissem Kontrollschild: 40 Rappen pro km; Velo, Motorfahrrad und Motorrad mit gelbem Kontrollschild: Pauschale Fr. 700.
> - Quelle: `bund-dbg-2026__art-26`, `bund-rs-2-215__c0004`.
> 
> **Vergleich:** Der kantonale Maximalabzug in SG (Fr. 8'000) liegt deutlich über dem Bundesbetrag (Fr. 3'300). Kanton und Bund werden getrennt deklariert.
> 
> Alle Werte sind von der Quelle geprüft, die Abnahme durch eine Fachperson steht aber noch aus.

## b03

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Welchen Kinderabzug können Eltern für ein 3-jähriges, ein 10-jähriges und ein 16-jähriges (noch minderjähriges) Kind geltend machen?

**Soll (Referenz):** AR (Kantonssteuer) 2025, indexierte Beträge gemäss Anhang 1 StG (bestätigt durch WL AR 2025 Ziff. 23): 3-jähriges Kind (bis Vollendung des 4. Altersjahrs) Fr. 5'300; 10-jähriges Kind (nach Vollendung des 4. bis Vollendung des 15. Altersjahrs) Fr. 7'400; 16-jähriges Kind (nach Vollendung des 15. Altersjahrs bis Volljährigkeit) Fr. 11'600. Gleiche Beträge für volljährige Kinder in Ausbildung bis zum 26. Altersjahr. (Korrigiert nach Bewertung Lauf A: die ursprüngliche Referenz nannte die nicht indexierten Merkblatt-Beträge 5'000/7'000/11'000.)

**Antwort des Agenten** (26.0 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Kinderabzug vom Einkommen**
> 
> | Kind | Alter | AR-Kinderabzug (kantonal) | Bund (DBG) |
> |---|---|---|---|
> | 3-jährig | bis Vollendung des 4. Altersjahres | **CHF 5'300** | CHF 6'800 |
> | 10-jährig | nach Vollendung des 4. bis Vollendung des 15. Altersjahres | **CHF 7'400** | CHF 6'800 |
> | 16-jährig (minderjährig) | nach Vollendung des 15. Altersjahres bis Volljährigkeit | **CHF 11'600** | CHF 6'800 |
> 
> Die drei Beträge sind die Kinderabzüge vom Einkommen nach Art. 38 Abs. 1 lit. a Ziff. 1–3 des AR-Steuergesetzes (Fundstelle `ar-stg-anhang-kp__c0001`). Der Bund kennt keine Altersstaffelung; für jedes minderjährige Kind gilt CHF 6'800 (Art. 35 DBG, `bund-dbg-2025__art-35`).
> 
> **Hinweise:**
> - **Vorschulbetrag:** Die Wiki-Eckwerte nennen CHF 5'300 (indexiert per 1.1.2024). Der unindexierte Gesetzestext nennt CHF 5'000. Massgebend ist der indexierte Betrag aus Anhang 1 bzw. der Wegleitung 2025. Ich habe den Betrag nicht gegen die Wegleitung selbst geprüft.
> - **Weitere Kinderabzüge:** Die AR-Abzüge für Versicherungen (CHF 1'000 pro Kind, `ar-stg__art-35-t2`) und das Vermögensfreibetrag-Zuschlag (CHF 25'000 pro minderjähriges Kind mit Kinderabzug, `ar-stg__art-51`) sind hier nicht eingerechnet. Im Bund gilt außerdem eine Steuerbetragsermässigung von CHF 263 pro Kind (`bund-dbg-2025__art-36-t4`).
> - **Status:** Alle Werte sind ☑️ agent-geprüft: Die Fundstelle ist geprüft, die fachliche Abnahme steht noch aus.
> - **Formular:** Die Kinderabzüge stehen im AR-Formular unter Ziff. 23.1 (Kind bis 4. Altersjahr) und Ziff. 23.2 (Kind nach 4. bis 15. Altersjahr). Für das 16-jährige Kind ist die Angabe im Formular noch zu prüfen. Die genaue Position lässt sich mit `position ar 2025 <Ziffer>` nachschlagen.

## b04

**Frage:** Alleinstehende Person ohne Kinder mit Beiträgen an die 2. Säule, Kanton Thurgau, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Staats-/Gemeindesteuern und bei der Bundessteuer?

**Soll (Referenz):** TG 2025: Staat max. Fr. 3'500, Bund max. Fr. 1'800 (ohne Beiträge an Säule 2/3a würde beim Bund Fr. 2'700 gelten). Betrag vor Abzug Prämienverbilligungen Krankenkassen.

**Antwort des Agenten** (25.9 s · Tools: 4 Aufrufe steuerwiki__wert):

> **Antwort (Steuerjahr 2025, alleinstehend, ohne Kinder, mit Beiträgen an die 2. Säule, Kanton TG):**
> 
> | Steuer | Max. Abzug (Versicherungsprämien + Sparzinsen) | Fundstelle | Status |
> |---|---|---|---|
> | Staats- und Gemeindesteuern TG | **CHF 3'500** | tg-stg__par-34-t3 | ☑️ agent-geprüft |
> | Direkte Bundessteuer | **CHF 1'800** | bund-dbg-2025__art-33-t2 | ☑️ agent-geprüft |
> 
> - **Kanton:** Der Betrag von CHF 3'500 gilt für übrige Steuerpflichtige. TG kennt keinen separaten, höheren Betrag für Personen ohne Vorsorgebeiträge.
> - **Bund:** Der höhere Satz von CHF 2'700 gilt nur ohne Beiträge an Säule 2 und 3a (bund-rs-2-210__c0006). Mit Säule-2-Beiträgen gilt der Satz von CHF 1'800.
> - Bei den Sparzinsen gibt es keinen eigenen Betrag: Beide Steuern fassen Prämien und Sparzinsen in einem gemeinsamen Höchstbetrag zusammen.
> 
> Die Beträge sind im Wiki als «agent-geprüft» markiert, die Abnahme durch eine Fachperson steht noch aus. Vor der Deklaration bitte im Formular TG 2025 unter Ziff. 14 («Versicherungsprämien und Zinsen von Sparkapitalien») gegenprüfen (`position tg 2025 14`).

## b05

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wie hoch ist der Kinderabzug für ein noch nicht schulpflichtiges Kind und für ein Kind in Schule oder Ausbildung bei den Kantons-/Gemeindesteuern?

**Soll (Referenz):** SG 2025: noch nicht schulpflichtiges Kind Fr. 7'600 (Ziff. 23.1); Kind in Schule oder Ausbildung (auch volljährig) Fr. 10'800 (Ziff. 23.2).

**Antwort des Agenten** (23.6 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Kanton St.Gallen, Steuerjahr 2025, Kantons- und Gemeindesteuern:**
> 
> - **Noch nicht schulpflichtiges Kind (Ziff. 23.1): CHF 7'600**
> - **Kind in Schule oder Ausbildung (Ziff. 23.2): CHF 10'800**
> 
> Die Beträge gelten je Kind. Der Abzug für das Vorschulkind wird nach den Verhältnissen am 31.12. berechnet. Voraussetzung ist, dass das Kind unter elterlicher Sorge bzw. Obhut steht und der Steuerpflichtige hauptsächlich für den Unterhalt aufkommt und keinen Unterhaltsabzug beansprucht. Der Abzug für Schule/Ausbildung gilt für Kinder unter Sorge/Obhut oder volljährige Kinder in Ausbildung.
> 
> Zusätzlich kann für ein Kind in Ausbildung der Ausbildungskostenabzug (Ziff. 23.3) geltend gemacht werden: die selbst getragenen Kosten nach Abzug von Stipendien, soweit sie den Selbstbehalt von CHF 3'200 übersteigen, höchstens CHF 13'700.
> 
> **Fundstellen:** StG SG Art. 48 (Sozialabzüge), Formular 1 SG 2025 Ziff. 23.1–23.3 (`sg-form-1-2025__c0011`), WL SG 2025 Ziff. 23 (`sg-wl-2025__c0104`). Alle Werte sind als ☑️ agent-geprüft markiert: Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> 
> **Bund (zur Abgrenzung, nicht Kanton/Gemeinde):** Die direkte Bundessteuer kennt keine Altersstaffel. Sie gewährt CHF 6'800 pro minderjähriges oder in Ausbildung stehendes Kind (Art. 35 DBG 2025).

## b06

**Frage:** Bis wann ist die Steuererklärung 2025 einer natürlichen Person im Kanton Zürich einzureichen, und wie ist vorzugehen, wenn die Frist nicht eingehalten werden kann?

**Soll (Referenz):** ZH, Steuerperiode 2025: Einreichung bis 31. März 2026 (online oder an das Scan-Center). Gesuch um Fristerstreckung ist vor Ablauf der Frist beim Gemeindesteueramt zu stellen. Mahnfristen sind nicht erstreckbar.

**Antwort des Agenten** (29.8 s · Tools: 6 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Frist:** Die Steuererklärung 2025 natürlicher Personen im Kanton Zürich musste **bis 31. März 2026** eingereicht werden, zusammen mit dem Wertschriftenverzeichnis, online oder beim Scan-Center (ZStB 132.1, Kap. G.I; WL ZH 2025). Heute ist der 9. November 2026, die ordentliche Frist ist also seit rund sieben Monaten abgelaufen.
> 
> **Was jetzt noch möglich ist:**
> 
> 1. **Fristerstreckung gibt es nur, wenn sie vor Fristablauf beantragt wurde.** Nach Ablauf der ordentlichen oder erstreckten Frist gestellte Gesuche werden abgewiesen, weil eine abgelaufene Frist nicht mehr erstreckt werden kann (ZStB 132.1, Kap. G.II.a). Hat jemand rechtzeitig ein Gesuch gestellt, gilt die Erstreckung längstens bis **30. November 2026**. Heute ist also noch Zeit bis zu diesem Datum, aber nur für eine bereits bewilligte oder rechtzeitig beantragte Erstreckung.
> 
> 2. **Wiederherstellung der Frist:** Wer nichts beantragt hat, kann beim **Gemeindesteueramt** eine Wiederherstellung der Frist verlangen. Sie wird nur bei Vorliegen der Voraussetzungen nach § 15 StV bzw. Art. 119 Abs. 2 und Art. 124 Abs. 4 DBG gewährt, also bei ausserordentlichen Gründen, die glaubhaft gemacht werden müssen. Die Voraussetzungen im Einzelnen habe ich nicht im Wortlaut geprüft.
> 
> 3. **Sofort einreichen:** Die Steuererklärung nachreichen, möglichst zusammen mit einem Wiederherstellungsgesuch, das die Gründe für die Verspätung darlegt.
> 
> 4. **Mahnung abwarten bzw. beachten:** Wer trotz Mahnung nicht einreicht, wird nach der Weisung ZStB 139.2 veranlagt (Kap. J). Mahnfristen sind nicht erstreckbar. Was das im Einzelfall heisst (z. B. Veranlagung nach Ermessen, Busse), ist in den Quellen nicht abschliessend beschrieben. Die Kosten einer Fristerstreckung sind in den Quellen ebenfalls nicht genannt.
> 
> **Hinweis:** Die Verfahrensregeln (ZStB 132.1, gültig ab 1.1.2026) und das Datum 31.3.2026 sind agent-geprüft, die Abnahme durch die Fachperson steht noch aus. Wer die Frist verpasst hat, sollte sich deshalb vor einem Wiederherstellungsgesuch oder der Einreichung beim Gemeindesteueramt Zürich bestätigen lassen, ob bereits eine Erstreckung besteht.

## b07

**Frage:** Wir sind eine Treuhandfirma und brauchen für Mandanten im Kanton Thurgau (Steuerperiode 2025, natürliche Personen) eine Fristerstreckung. Bei welcher Stelle ist das Gesuch einzureichen und bis wann kann die Frist längstens erstreckt werden?

**Soll (Referenz):** TG: Gesuch beim Gemeindesteueramt, das darüber entscheidet. Erstmals eingereichte Gesuche werden grundsätzlich bis längstens 30. September des Deklarationsjahres (2026) gutgeheissen; zusätzliche Gesuche in begründeten Fällen bis 30. November. Treuhänder/Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen, können für ihre Mandanten ein Gesuch längstens bis 31. Dezember des Deklarationsjahres beantragen. Arbeitsüberlastung ist kein Grund.

**Antwort des Agenten** (27.8 s · Tools: 3 Aufrufe steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> **Stelle:** Das Gesuch geht an das **Gemeindesteueramt**, also an die Gemeinde, die für die Steuererklärung zuständig ist (in der Regel die Wohnsitzgemeinde am 31.12.). Das Gemeindesteueramt entscheidet darüber und teilt den Entscheid schriftlich mit. Das Gesuch muss schriftlich, begründet und rechtzeitig eingereicht werden.
> 
> **Längstmögliche Frist:** Als gewerbsmässige Treuhänder und Steuerberater können Sie für Ihre Mandanten **längstens bis 31. Dezember 2026** eine Fristerstreckung beantragen. Für die Steuerperiode 2025 ist das Deklarationsjahr 2026.
> 
> **Ablauf der Fristen für Steuerjahr 2025 (natürliche Personen):**
> - Erstes Gesuch grundsätzlich bis 30. September 2026. Diese Frist ist bereits abgelaufen.
> - Weitere Gesuche in begründeten Fällen bis 30. November 2026.
> - Für Treuhänder bis 31. Dezember 2026 (die Regel für Ihre Mandanten).
> - Darüber hinaus werden Gesuche nur bei ausserordentlichen Gründen behandelt. Starke berufliche Beanspruchung des Vertreters oder fehlende Unterlagen gelten ausdrücklich nicht als solche Gründe.
> 
> Die Frist 30. November wird in der Praxis nur in der Form genannt, dass Gesuche danach abgewiesen werden, ausser für Treuhänder bis 31. Dezember. Das ist im Wortlaut nicht ganz eindeutig; prüfen Sie vor dem Einreichen, ob Ihr Gemeindesteueramt die Treuhänder-Regel so anwendet.
> 
> **Gebühr:** § 39b StV TG regelt Gebühren für Fristerstreckungen. Der Betrag für natürliche Personen ist in meinen Quellen nicht genannt, daher bitte beim Gemeindesteueramt erfragen.
> 
> **Hinweis:** Die Angaben stammen aus StP 155 Nr. 2 (Fundstelle `tg-stp-155-2__c0001` und `c0002`) und sind agent-geprüft (Abnahme offen). Die Frist 31. Dezember habe ich im Chunk-Wortlaut bestätigt.

## b08

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Auf welchem Formular wird der Abzug für Versicherungsprämien und Sparzinsen berechnet und in welche Ziffer der Steuererklärung wird das Ergebnis übertragen?

**Soll (Referenz):** AR 2025: Berechnung auf Formular 6 (A: bezahlte Prämien/Zinsen, B: Maximalabzug, C: Abzug = niedrigerer Betrag von A und B). Der Betrag C wird auf Seite 3 der Steuererklärung in Ziffer 14 übertragen.

**Antwort des Agenten** (24.4 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__suche):

> **Kanton Appenzell Ausserrhoden, Steuerjahr 2025:**
> 
> **Berechnung:** Formular 6 («Krankheits- und Unfallkosten, behinderungsbedingte Kosten»), Hilfsblatt Versicherungsprämien/Krankheitskosten.
> - **Teil A (Code 600 A):** Bruttoprämien Krankenversicherung, Unfallversicherung (ohne NBUV), Lebens-/Rentenversicherung und Sparzinsen, abzüglich Prämienverbilligung. Rechnung: a + b + c + d − e.
> - **Teil B (Code 600 B):** Höchstabzug. Kanton: Fr. 5'400 gemeinsam steuerpflichtige Personen, sonst Fr. 2'700, plus Fr. 1'000 je Kind mit Kinderabzug (Ziff. 23.1–23.3).
> - **Ergebnis (Code 600):** der niedrigere Betrag aus 600 A und 600 B.
> 
> **Übertrag:** Ziff. 14 der Steuererklärung («Versicherungsprämien und Zinsen von Sparkapitalien»), Code 600.
> 
> **Bund:** Das AR-Formular hat keine Bundesspalte. Die Steuerverwaltung nimmt die Abweichungen für die direkte Bundessteuer automatisch vor. Die Bundeslimiten sind andere (Fr. 3'700 gemeinsam, Fr. 1'800 übrige, Fr. 700 je Kind; ohne Säule 2/3a Fr. 5'550 bzw. Fr. 2'700).
> 
> **Ausgeschlossen:** NBUV, Mobiliar-, Motorfahrzeug-, Haftpflicht- und andere Sachversicherungen.
> 
> **Status:** ☑️ agent-geprüft (Fundstellen geprüft, Abnahme offen). Die Code-Nummer 600 ist aus dem Hilfsblatt belegt. Der Hauptformular-Code für Ziff. 14 ist nicht separat verifiziert.
> 
> **Fundstellen:** ar-form-06-2025__c0001, ar-form-06-2025__c0002, ar-wl-2025__c0085, ar-wl-2025__c0179.

## b09

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wo und wie ist ein Gesuch um Fristverlängerung für die Steuererklärung einer natürlichen Person zu stellen und bis wann?

**Soll (Referenz):** SG 2025: Das Gesuch ist vor Ablauf der Einreichefrist (Datum auf Seite 1 der Steuererklärung) zu stellen, vorzugsweise elektronisch unter www.steuern.sg.ch (mit Registernummer und Geburtsdatum); sonst schriftlich an das Gemeindesteueramt. Es kann eine angemessene Fristverlängerung gewährt werden.

**Antwort des Agenten** (28.9 s · Tools: 7 Aufrufe steuerwiki__suche, steuerwiki__zeige):

> Die wichtigsten Treffer sind die SG-Informationsseite und die Wegleitung. Ich öffne die Chunks, um Fristen und Verfahren wörtlich zu prüfen.
> 
> Für die Steuererklärung 2025 im Kanton St. Gallen stellst du das Gesuch um Fristverlängerung **elektronisch über www.steuern.sg.ch (eFristverlängerung)**. Eine schriftliche Eingabe ist nur der Ausweg, wenn du nicht elektronisch stellst.
> 
> **Wo und wie**
> - Online unter **www.steuern.sg.ch**, Dienst «eFristverlängerung». Du brauchst die **Registernummer** und das **Geburtsdatum**, beide stehen auf deiner Steuererklärung.
> - Das Gesuch wird interaktiv bewilligt oder abgelehnt.
> - Wird das Gesuch nicht elektronisch gestellt, ist es **schriftlich an das Gemeindesteueramt** zu richten.
> - Eine Fristverlängerung gibt es nur, **bevor** die Einreichefrist abläuft.
> - Sind fällige Steuerrechnungen noch nicht bezahlt, kann die Fristverlängerung nicht gewährt werden.
> 
> **Bis wann**
> - Die Einreichefrist (inkl. Beilagen) steht auf **Seite 1 der Steuererklärung** als Termin. Das Gesuch muss vor diesem Termin gestellt werden.
> - Das konkrete Datum für Steuerjahr 2025 ist im Wiki nicht hinterlegt. Ich habe es deshalb nicht übernommen. Bitte nimm es von Seite 1 deiner Steuererklärung.
> - Auf der Informationsseite steht ein Hinweis: Am **Freitag, 6. November 2026, zwischen 19:00 und 24:00 Uhr** kann die eFristverlängerung gestört sein. Wenn du das Gesuch online stellen willst, wähle ein anderes Zeitfenster.
> 
> **Quellen**
> - SG Informationsseite «Fristverlängerung Privatpersonen» (sg-info-fristverlaengerung__c0001–c0003, gilt für 2025 und 2026). Status: 🟡 extrahiert.
> - Wegleitung SG 2025, Fristen, S. 8 (sg-wl-2025__c0018). Status: 🟡 extrahiert.
> 
> Die Angaben gelten für die Staats- und Gemeindesteuer. Zur direkten Bundessteuer habe ich nichts Eigenes geprüft. Die Erklärung ist kantonal, und die Fristverlängerung läuft über das Gemeindesteueramt.

## b10

**Frage:** Ehepaar im Kanton St.Gallen, Steuerjahr 2025, zwei Kinder mit Kinderabzug, keine Beiträge an die 2. Säule oder Säule 3a bei beiden Partnern. Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Kantons-/Gemeindesteuern und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2025 Kanton: Fr. 6'800 + zusätzlich ohne 2. Säule/3a bis Fr. 1'100 + 2 x bis Fr. 1'100 für die Kinder = Fr. 10'100. Bund: Fr. 3'700 + zusätzlich bis Fr. 1'850 (= Fr. 5'550) + 2 x Fr. 700 = Fr. 6'950. (Voraussetzung für den Zusatzabzug muss bei beiden Partnern erfüllt sein.)

**Antwort des Agenten** (34.8 s · Tools: 6 Aufrufe steuerwiki__wert, steuerwiki__zeige):

> **Ergebnis (Steuerjahr 2025, Ehepaar, zwei Kinder mit Kinderabzug, keine Beiträge an Säule 2 oder 3a bei beiden Partnern):**
> 
> | | Kanton/Gemeinde SG | Direkte Bundessteuer |
> |---|---|---|
> | Grundbetrag Ehepaar (Prämien und Sparzinsen) | 6'800 | 3'700 |
> | Zuschlag ohne Säule 2/3a bei beiden | +1'100 | +50 % = +1'850 (ergibt 5'550) |
> | Zuschlag je Kind (2 Kinder) | +2 × 1'100 = +2'200 | +2 × 700 = +1'400 |
> | **Maximaler Abzug** | **10'200** | **6'950** |
> 
> **Quellen und Einordnung:**
> 
> - **SG:** Art. 45 Abs. 1 lit. g StG SG (Chunk `sg-stg-2025__art-45-t2`). Der Gesamtbetrag von 6'800 gilt für Ehegatten und umfasst Krankenversicherung, Lebens- und Unfallversicherung sowie Sparkapitalzinsen. Die Zuschläge von 1'100 (ohne 2./3a) und 1'100 je Kind stehen im selben Absatz und addieren sich. Die 10'200 ist meine Addition aus den Einzelwerten, im Wiki steht diese Summe nicht. Das Wiki führt die Zahl 7'900 für «ohne Vorsorge» ohne die Kinder auf. Die Voraussetzung «keine Beiträge» muss bei beiden Partnern erfüllt sein.
> - **Bund:** Art. 33 Abs. 1 lit. g und Abs. 1bis DBG (Chunk `bund-dbg-2025__art-33-t5`). Die Hälfte-Erhöhung für Verzicht auf 2./3a und die 700 Franken je Kind sind im Gesetz aufgeführt. Die 5'550 steht im Wiki als Eckwert, die Summe 6'950 ist abgeleitet.
> - **Abnahme:** Alle Werte sind im Wiki als ☑️ agent-geprüft markiert (Fundstelle geprüft, Abnahme offen).
> - **Prämienverbilligungen** der Krankenversicherung mindern den Abzug (laut SG-Text).
> 
> Der Kanton-Abzug 10'200 gilt nur für die Staats- und Gemeindesteuer SG. Die Berechnung der tatsächlich abziehbaren Beträge aus Ihren Belegen (Prämien, Zinsen) klären wir separat, sobald die Belege vorliegen.

## b11

**Frage:** Arbeitnehmer im Kanton Thurgau, Steuerjahr 2026, Arbeitsweg mit ÖV-Jahresabonnement, effektive Kosten Fr. 6'400. Welcher Fahrkostenabzug ist bei den Staats-/Gemeindesteuern und welcher bei der direkten Bundessteuer zulässig?

**Soll (Referenz):** TG 2026: Kanton gesamthaft max. Fr. 6'000, deshalb Abzug Fr. 6'000 (effektive Kosten Fr. 6'400 werden gekürzt). Bund max. Fr. 3'300, deshalb Abzug Fr. 3'300.

**Antwort des Agenten** (23.5 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kanton Thurgau, Steuerjahr 2026, ÖV-Jahresabonnement, effektive Kosten Fr. 6'400:**
> 
> **Staats- und Gemeindesteuern TG: maximal Fr. 6'000** → abziehbar **Fr. 6'000** (Kürzung von 6'400 um 400).
> - Fundstelle: tg-wl-2026__c0176 («Fahrkosten von gesamthaft maximal Fr. 6 000»). Status ☑️ agent-geprüft, Abnahme offen.
> - Der Höchstbetrag umfasst Fahrkosten Wochenaufenthalt und Nebenerwerb insgesamt pro Person.
> 
> **Direkte Bundessteuer: maximal Fr. 3'300** → abziehbar **Fr. 3'300** (Kürzung von 6'400 um 3'100).
> - Fundstelle: bund-dbg-2026__art-26 (Art. 26 Abs. 1 lit. a DBG: «bis zu einem Maximalbetrag von 3300 Franken für die Fahrten zwischen Wohn- und Arbeitsstätte»). Status ☑️ agent-geprüft, Abnahme offen.
> - Die Bundesspalte wird separat deklariert.
> 
> **Ergebnis:** Kanton/Gemeinde Fr. 6'000, Bund Fr. 3'300. Die tatsächlichen Kosten von Fr. 6'400 werden in beiden Fällen nicht vollständig abgezogen.
> 
> Hinweis: Die Eckwerte sind agent-geprüft, die Abnahme durch eine Fachperson steht noch aus. Die Formularziffer im TG-Formular 2026 (Ziff. 10.1/10.2, Berufsauslagen unselbständig Erwerbstätiger) kann ich mit `position tg 2026 10.1` nachschlagen, falls Sie die Eintragung benötigen.

## b12

**Frage:** Ehepaar im Kanton Zürich, Steuerjahr 2026, nachgewiesene Kinderdrittbetreuungskosten: Kind A (5 Jahre) Fr. 30'000, Kind B (8 Jahre) Fr. 12'000. Wie hoch ist der Abzug bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2026: Maximum pro Kind Staat Fr. 25'300, Bund Fr. 25'800 (Kinder unter 14). Staat: 25'300 + 12'000 = Fr. 37'300. Bund: 25'800 + 12'000 = Fr. 37'800. (Zum Vergleich 2025: Staat max. Fr. 25'000.)

**Antwort des Agenten** (24.3 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Kanton Zürich (Staatssteuer), Steuerjahr 2026:** Fr. 37'300
> 
> - Kind A (5 Jahre): Kosten Fr. 30'000, gedeckelt auf **Fr. 25'300**
> - Kind B (8 Jahre): Kosten Fr. 12'000, unter dem Höchstbetrag, also **Fr. 12'000**
> 
> **Direkte Bundessteuer, Steuerjahr 2026:** Fr. 37'800
> 
> - Kind A (5 Jahre): Kosten Fr. 30'000, gedeckelt auf **Fr. 25'800**
> - Kind B (8 Jahre): **Fr. 12'000**
> 
> Die Höchstbeträge gelten pro Kind. Beide Kinder sind unter 14 Jahre alt, und als Ehepaar im gemeinsamen Haushalt greift der volle Abzug, nicht der halbe Betrag für Konkubinat oder alternierende Obhut.
> 
> Quellen:
> - ZH: Höchstbetrag Fr. 25'300 (StG § 31 Abs. 3 ZH, zh-stg-2026__par-31-t3), Altersgrenze 14 Jahre
> - Bund: Höchstbetrag Fr. 25'800 (DBG Art. 33 Abs. 1 lit. f, bund-dbg-2026__art-33-t7), Altersgrenze 14 Jahre
> 
> Status: beide Werte sind agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Zahlen stimmen mit den Fundstellen überein, sind aber noch nicht abgenommen.

## b13

**Frage:** Ein Mitglied der Milizfeuerwehr erhält für die Erfüllung von Kernaufgaben (Übungen, Pikettdienst, Ernstfalleinsätze) Sold. Bis zu welchem Betrag ist der Feuerwehrsold bei der direkten Bundessteuer steuerfrei, im Steuerjahr 2025 und im Steuerjahr 2026?

**Soll (Referenz):** Bund: 2025 steuerfrei bis maximal Fr. 5'300; 2026 steuerfrei bis maximal Fr. 5'400 (Wert hat sich geändert, nicht übertragen). Der gesamte Sold ist auf dem Lohnausweis zu deklarieren; der steuerfreie Betrag wird auf Formular 9 Berufskosten Ziffer 8 abgezogen.

**Antwort des Agenten** (24.1 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__suche):

> **Direkte Bundessteuer (Art. 24 DBG):**
> 
> - **Steuerjahr 2025: CHF 5'300** pro Jahr. Der Sold der Milizfeuerwehrleute für Dienstleistungen zur Erfüllung der Kernaufgaben ist bis zu diesem Betrag steuerfrei. Fundstelle: bund-dbg-2025__art-24-t2 · ☑️ agent-geprüft (Abnahme offen).
> - **Steuerjahr 2026: CHF 5'400** pro Jahr. Der Betrag wurde gegenüber 2025 um CHF 100 erhöht. Fundstelle: bund-dbg-2026__art-24-t2 · ☑️ agent-geprüft (Abnahme offen).
> 
> Für 2026 gilt laut Wiki zusätzlich:
> - Die Befreiung betrifft nur den Sold für Kernaufgaben. Pauschalzulagen für Kader, Funktionszulagen, administrative Arbeiten und freiwillige Dienstleistungen sind davon ausgenommen.
> - Im Lohnausweis wird der gesamte Sold deklariert. Die Steuerbefreiung wird also nicht im Lohnausweis, sondern bei der Steuererklärung berücksichtigt.
> 
> Die Wegleitung 2a (2025) bestätigt ebenfalls den Betrag von CHF 5'300 und verweist für den Nachweis auf die Aufstellung mit Belegen (Beleg 7 «Feuerwehrsold»).
> 
> Die Antwort gilt nur für den Bund. Kantonale Regeln können abweichen. Wenn du mir den Kanton nennst, prüfe ich die kantonalen Werte ebenfalls.

## b14

**Frage:** Ein Mandant wohnt am 31.12.2026 im Kanton Luzern und pendelt mit dem Auto zur Arbeit. Welcher Fahrkostenabzug gilt für die Luzerner Staats- und Gemeindesteuern 2026 und für die direkte Bundessteuer?

**Soll (Referenz):** Luzern ist im Wiki nicht abgedeckt (nur Bund, AR, SG, TG, ZH): kein Wert für die Luzerner Staats-/Gemeindesteuer nennen, auf kantonale Wegleitung verweisen. Für die direkte Bundessteuer 2026 gilt max. Fr. 3'300 (Wegleitung Bund 2026).

**Antwort des Agenten** (25.6 s · Tools: 2 Aufrufe steuerwiki__wert):

> **Direkte Bundessteuer 2026:** Pendlerabzug mit dem Auto nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist.
> 
> - **Ansatz:** CHF 0.75 pro Fahrkilometer (2025: 0.70). Status ☑️ agent-geprüft, Abnahme offen.
> - **Fundstelle:** `bund-mm-2025-09-11-kalte-progression-2026__c0004` (Medienmitteilung zur kalten Progression 2026).
> - **Maximum:** CHF 3'300 pro Jahr. Dieser Höchstbetrag gilt für alle Fahrkosten Wohn-/Arbeitsstätte zusammen, also auch für das Auto (`bund-dbg-2026__art-26`).
> - **Vergleich:** Öffentliche Verkehrsmittel werden nach den tatsächlichen Kosten bis CHF 3'300 abgezogen. Ein Velo oder Motorfahrrad mit gelbem Kontrollschild ergibt die Pauschale von CHF 700.
> 
> **Kanton Luzern 2026:** Das Steuer-Wiki deckt Luzern nicht ab (nur Bund, AR, SG, TG, ZH). Ich kann deshalb keinen luzernischen Fahrkostenabzug nennen. Für Luzern bitte die Wegleitung der Dienststelle Steuern Luzern bzw. das Luzerner Steuergesetz für 2026 prüfen.
> 
> Die Abklärung zu Luzern hängt davon ab, ob für den Mandanten ein öV-Anschluss zumutbar ist. Das bestimmt sich nach dem Bundesrecht und ist im Wiki nicht als eigene Regel erfasst. Es gibt hier also zwei offene Punkte: den Luzerner Ansatz und die Zumutbarkeit des öV.

