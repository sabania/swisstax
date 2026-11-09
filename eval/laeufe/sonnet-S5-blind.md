# OpenClaw-Testlauf: blindtest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 14 · Lauf: 2026-11-09 19:33
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## b01

**Frage:** Ehepaar in rechtlich und tatsächlich ungetrennter Ehe, weder Beiträge an die 2. Säule noch an die Säule 3a, Kanton ZH, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Zinsen von Sparkapitalien bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2025: Staatssteuer höchstens CHF 8'700 (Grundabzug CHF 5'800, ohne Beiträge an 2. Säule/3a um die Hälfte erhöht). Direkte Bundessteuer 2025: höchstens CHF 5'550 (Grundabzug CHF 3'700, um die Hälfte erhöht).

**Antwort des Agenten** (24.7 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__wert):

> **Kanton ZH · Steuerjahr 2025**
> 
> Ehepaar in rechtlich und tatsächlich ungetrennter Ehe, ohne Beiträge an die 2. Säule und die Säule 3a. Gemeint ist der Abzug für Versicherungsprämien und Zinsen von Sparkapitalien (Formular Ziff. 15, Code 270).
> 
> | | Maximalabzug |
> |---|---|
> | **Staatssteuer** | **CHF 8'700** |
> | **Direkte Bundessteuer** | **CHF 5'550** |
> 
> - **Staatssteuer:** Der Normalabzug für Verheiratete beträgt CHF 5'800. Ohne Beiträge an die 2. Säule und Säule 3a erhöht er sich um die Hälfte auf CHF 8'700. Quelle: zh-stg-2025__par-31-t2, zh-wl-2025__c0086 (☑️ agent-geprüft).
> - **Bundessteuer:** Der Normalabzug beträgt CHF 3'700. Ohne Beiträge nach Art. 33 Abs. 1 Bst. d und e DBG erhöht er sich um die Hälfte auf CHF 5'550. Quelle: bund-dbg-2025__art-33-t2, bund-dbg-2025__art-33-t5 (☑️ agent-geprüft).
> 
> **Zu beachten**
> - Das sind Höchstbeträge. Abziehbar ist je Spalte der tiefere Betrag aus Teil A (tatsächlich bezahlte Prämien und Sparzinsen, abzüglich Prämienverbilligung) und Teil B (Maximalabzug). Das steht im Form. 365 und führt zu Code 270. Quelle: zh-form-300-2025__c0008.
> - Kinder oder unterstützungsbedürftige Personen sind in den Beträgen nicht enthalten. Pro Kind oder unterstützte Person kommen CHF 1'300 (Staat) bzw. CHF 700 (Bund) dazu. Für Ihren Fall gilt das nur, wenn solche Personen vorhanden sind.
> - Die erhöhten Beträge gelten nur, wenn weder die Steuerpflichtigen noch deren Arbeitgeber Beiträge an die 2. Säule oder die Säule 3a geleistet haben. Dasselbe gilt für beide Ehegatten.
> 
> Status: ☑️ agent-geprüft, Fundstelle geprüft, Abnahme durch eine Fachperson offen.

## b02

**Frage:** Wie hoch ist im Steuerjahr 2026 der Maximalabzug für Fahrkosten zwischen Wohn- und Arbeitsort im Kanton St.Gallen (Kantons- und Gemeindesteuern) und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2026: Kantons- und Gemeindesteuern max. Fr. 8'000; direkte Bundessteuer max. Fr. 3'300. Es ist ein Maximalabzug, keine Pauschale (bei Teilzeit/unterjährig nicht gekürzt).

**Antwort des Agenten** (24.8 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **SG · Steuerjahr 2026: Maximalabzug Fahrkosten Wohn-/Arbeitsort**
> 
> | | Maximalabzug | Fundstelle | Status |
> |---|---|---|---|
> | **Kanton SG** (Staats- und Gemeindesteuern) | **CHF 8'000** | `sg-stg-2026__art-39` (Art. 39 StG SG): «bis zum Betrag von Fr. 8000.–» | ☑️ agent-geprüft |
> | **Direkte Bundessteuer** | **CHF 3'300** | `bund-dbg-2026__art-26` (Art. 26 Abs. 1 lit. a DBG): «bis zu einem Maximalbetrag von 3300 Franken» | ☑️ agent-geprüft |
> 
> **Hinweise**
> - Die Maximalbeträge sind Obergrenzen, keine Pauschalen. Abziehbar sind die tatsächlichen Kosten, begrenzt auf diese Beträge.
> - Im Kanton SG wird das Maximum bei unterjähriger Steuerpflicht oder Teilzeit nicht gekürzt. Es gilt für Haupt- und Nebenerwerb zusammen (StB 39 Nr. 3).
> - Im Formular 1 SG 2026 steht der Abzug unter Ziff. 10.1 bzw. 10.2 (Code 438). Er wird über Formular 4 berechnet, mit Kanton und Bund in getrennten Spalten.
> - Zusätzlich zu den Maxima gelten:
>   - Privates Auto oder Motorrad: CHF 0.75 pro km, nur wenn kein zumutbarer öffentlicher Verkehr besteht. Das gilt für Kanton und Bund. Beim Auto sind es neu 75 Rappen (2025: 70 Rappen).
>   - Velo, Motorfahrrad oder Kleinmotorrad: CHF 700 pauschal.
>   - Der Kanton rechnet mit 220 Arbeitstagen (StB 39 Nr. 3 Ziff. 2.7).
>   - Beim Bund gelten für Motorräder CHF 0.40 pro km (`bund-rs-2-215__c0004`).
> - Die Wegleitung und die Hilfsblätter SG 2026 sind laut Wiki noch nicht publiziert (Stand 09.11.2026). Die Zuordnung stützt sich auf Formular 1 UJ und die Rechtsgrundlagen 2026.
> - Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## b03

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Welchen Kinderabzug können Eltern für ein 3-jähriges, ein 10-jähriges und ein 16-jähriges (noch minderjähriges) Kind geltend machen?

**Soll (Referenz):** AR (Kantonssteuer) 2025, indexierte Beträge gemäss Anhang 1 StG (bestätigt durch WL AR 2025 Ziff. 23): 3-jähriges Kind (bis Vollendung des 4. Altersjahrs) Fr. 5'300; 10-jähriges Kind (nach Vollendung des 4. bis Vollendung des 15. Altersjahrs) Fr. 7'400; 16-jähriges Kind (nach Vollendung des 15. Altersjahrs bis Volljährigkeit) Fr. 11'600. Gleiche Beträge für volljährige Kinder in Ausbildung bis zum 26. Altersjahr. (Korrigiert nach Bewertung Lauf A: die ursprüngliche Referenz nannte die nicht indexierten Merkblatt-Beträge 5'000/7'000/11'000.)

**Antwort des Agenten** (28.4 s · Tools: 3 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> **Appenzell Ausserrhoden · Steuerjahr 2025**
> 
> **Kanton (Staats- und Gemeindesteuer):** Der Kinderabzug ist nach Alter gestaffelt. Massgebend ist das Alter am 31.12.2025.
> 
> | Kind | Ziff. | Abzug | Quelle |
> |---|---|---|---|
> | 3-jährig (bis Vollendung des 4. Altersjahrs) | 23.1 | CHF 5'300 | ar-stg-anhang-kp__c0001, ar-wl-2025__c0005 |
> | 10-jährig (nach dem 4. bis zur Vollendung des 15. Altersjahrs) | 23.2 | CHF 7'400 | ar-stg-anhang-kp__c0001, ar-wl-2025__c0005 |
> | 16-jährig (nach dem 15. Altersjahr bis Volljährigkeit) | 23.3 | CHF 11'600 | ar-stg-anhang-kp__c0001, ar-wl-2025__c0005 |
> | **Total** | | **CHF 24'300** | |
> 
> **Bund (direkte Bundessteuer):** Der Bund kennt keine Altersstaffel. Es gilt ein einheitlicher Kinderabzug von CHF 6'800 pro Kind, also **CHF 20'400** für die drei Kinder (bund-dbg-2025__art-35). Das AR-Formular hat keine separate Bundesspalte. Die Steuerverwaltung nimmt die Bundesabweichungen automatisch vor.
> 
> Alle Werte sind ☑️ agent-geprüft: Die Fundstellen sind geprüft, die Abnahme steht noch aus.
> 
> **Voraussetzungen und Stolpersteine (Kanton):**
> - Das Kind muss auf Unterhalt angewiesen sein, und die Eltern bestreiten diesen zur Hauptsache.
> - Der Abzug entfällt, wenn die Einkünfte des Kindes CHF 18'000 übersteigen. Bei der Ausbildungsstufe entfällt er auch, wenn das Reinvermögen des Kindes CHF 250'000 übersteigt.
> - Er entfällt ebenfalls, wenn für das Kind Unterhaltsbeiträge nach Ziff. 12.2 abgezogen werden.
> - Getrennt besteuerte Eltern mit gemeinsamer Sorge und ohne Unterhaltsbeiträge: Der Abzug wird je zur Hälfte aufgeteilt.
> - Der Gesetzestext nennt noch die unindexierten Beträge (5'000 / 7'000 / 11'000). Massgebend sind die indexierten Werte aus Anhang 1 StG und der Wegleitung 2025, wie oben.
> 
> **Zusätzlich pro Kind (nicht Teil des Kinderabzugs):**
> - Kanton: Zuschlag zum Versicherungsabzug von CHF 1'000 pro Kind (ar-stg__art-35-t2). Beim Bund sind es CHF 700 (bund-dbg-2025__art-33-t5).
> - Kanton: Vermögensfreibetrag von CHF 25'000 pro minderjähriges Kind mit Kinderabzug (ar-stg__art-51).
> - Bund: Abzug vom Steuerbetrag von CHF 263 pro Kind, also CHF 789 bei drei Kindern (bund-dbg-2025__art-36-t4).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## b04

**Frage:** Alleinstehende Person ohne Kinder mit Beiträgen an die 2. Säule, Kanton Thurgau, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Staats-/Gemeindesteuern und bei der Bundessteuer?

**Soll (Referenz):** TG 2025: Staat max. Fr. 3'500, Bund max. Fr. 1'800 (ohne Beiträge an Säule 2/3a würde beim Bund Fr. 2'700 gelten). Betrag vor Abzug Prämienverbilligungen Krankenkassen.

**Antwort des Agenten** (23.1 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Thurgau · Steuerjahr 2025** – alleinstehend, keine Kinder, mit Beiträgen an die 2. Säule
> 
> | | Maximaler Abzug Versicherungsprämien und Sparzinsen |
> |---|---|
> | **Staats-/Gemeindesteuern** | **CHF 3'500** |
> | **Direkte Bundessteuer** | **CHF 1'800** |
> 
> **Fundstellen**
> - **Kanton:** CHF 3'500 für «die übrigen Steuerpflichtigen» (tg-stg__par-34-t3). Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> - **Bund:** CHF 1'800 für «die übrigen Steuerpflichtigen» (bund-dbg-2025__art-33-t2). Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Warum nicht der höhere Bundesbetrag**
> - Der erhöhte Bundesabzug von CHF 2'700 gilt nur für Personen ohne Beiträge an die Säulen 2 und 3a.
> - Weil hier Beiträge an die 2. Säule geleistet wurden, gilt der ordentliche Betrag von CHF 1'800.
> - Die beiden Ansätze lassen sich nicht kumulieren.
> 
> **Hinweise zur Anwendung**
> - Abgezogen wird der niedrigere Betrag aus den tatsächlichen Prämien und Sparzinsen und dem Maximum. Das Formular rechnet je Spalte: Staat min(«A5»; «B4 Staat»), Bund min(«A5»; «B4 Bund»).
> - Der Eintrag erfolgt in Ziff. 14 der Steuererklärung (Code 330), mit Hilfsblatt Formular 5.2. Die linke Spalte gilt für Staat/Gemeinde, die rechte für den Bund.
> - Krankenkassenprämien werden netto nach Abzug der erhaltenen Prämienverbilligung (IPV) eingesetzt. Die Krankenkassenprämien müssen deklariert sein, sonst entfällt der Abzug unter Umständen ganz.
> - Prämien der Nichtberufsunfallversicherung (NBUV) gehören nicht hierher, sondern in Ziff. 15.4.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## b05

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wie hoch ist der Kinderabzug für ein noch nicht schulpflichtiges Kind und für ein Kind in Schule oder Ausbildung bei den Kantons-/Gemeindesteuern?

**Soll (Referenz):** SG 2025: noch nicht schulpflichtiges Kind Fr. 7'600 (Ziff. 23.1); Kind in Schule oder Ausbildung (auch volljährig) Fr. 10'800 (Ziff. 23.2).

**Antwort des Agenten** (23.9 s · Tools: 2 Aufrufe steuerwiki__wert, steuerwiki__position):

> **Kanton St. Gallen · Steuerjahr 2025 (Staats- und Gemeindesteuern)**
> 
> | Kind | Abzug | Formular SG 2025 |
> |---|---|---|
> | Noch nicht schulpflichtig | **CHF 7'600** | Ziff. 23.1 (Code 252) |
> | In Schule oder Ausbildung | **CHF 10'800** | Ziff. 23.2 (Code 254) |
> 
> Beide Beträge sind ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme steht noch aus.
> - Fundstelle: Art. 48 StG SG (sg-stg-2025__art-48) und Formular 1 SG 2025 (sg-form-1-2025__c0011).
> - Wo die Wegleitung sie ergänzt, steht sie in sg-wl-2025__c0104.
> 
> **Voraussetzungen**
> - **Stichtag:** Massgebend sind die Verhältnisse am 31.12.2025. Bei unterjähriger Steuerpflicht wird der Abzug anteilig gewährt.
> - **Unterhalt:** Das Kind steht unter Ihrer Sorge oder Obhut, und Sie kommen zur Hauptsache für den Unterhalt auf. Für Kinder, für die Sie Unterhaltsbeiträge nach Ziff. 12.2 abziehen, gibt es keinen Kinderabzug.
> - **Kindergarten:** Er zählt bereits zur Schulpflicht, es gilt also Ziff. 23.2 (CHF 10'800).
> - **Volljährige Kinder:** Der Abzug von CHF 10'800 gilt auch für volljährige Kinder in schulischer oder beruflicher Ausbildung, wenn Sie zur Hauptsache für den Unterhalt aufkommen.
> 
> **Zusätzlich bei Kindern in Ausbildung (nur Kanton und Gemeinde)**
> - Ziff. 23.3 (Code 256) sind die Ausbildungskosten, die Sie selbst tragen. Der Abzug beträgt höchstens CHF 13'700.
> - Davon geht ein Selbstbehalt von CHF 3'200 ab. Erhaltene Stipendien werden ebenfalls abgezogen.
> - Der Abzug setzt voraus, dass für das Kind der Abzug nach Ziff. 23.2 gilt.
> 
> **Direkte Bundessteuer**
> Der Bund kennt keine Altersstaffel. Er gewährt CHF 6'800 pro Kind, dazu CHF 263 Abzug vom Steuerbetrag pro Kind. Im SG-Formular gibt es nur eine Spalte, die Anpassungen für den Bund nimmt die Steuerbehörde automatisch vor. Die Bundesbeträge sind ebenfalls ☑️ agent-geprüft.
> 
> Die fachliche Beurteilung des Einzelfalls bleibt bei der Fachperson.

## b06

**Frage:** Bis wann ist die Steuererklärung 2025 einer natürlichen Person im Kanton Zürich einzureichen, und wie ist vorzugehen, wenn die Frist nicht eingehalten werden kann?

**Soll (Referenz):** ZH, Steuerperiode 2025: Einreichung bis 31. März 2026 (online oder an das Scan-Center). Gesuch um Fristerstreckung ist vor Ablauf der Frist beim Gemeindesteueramt zu stellen. Mahnfristen sind nicht erstreckbar.

**Antwort des Agenten** (32.4 s · Tools: 8 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Kanton Zürich · Steuerjahr 2025** (Staats- und Gemeindesteuer; der Bund folgt der kantonalen Regelung, es gibt keine gesonderte Bundesfrist)
> 
> ## Einreichefrist
> Die Steuererklärung 2025 ist **bis 31. März 2026** einzureichen (online oder beim Scan-Center). Quelle: `zh-wl-2025__c0017`, Status ☑️ agent-geprüft.
> 
> Heute ist der 9. November 2026, die ordentliche Frist ist also abgelaufen. Hat die Person nie ein Gesuch gestellt, geht es nur noch um den Fall «Frist verpasst» (siehe unten).
> 
> ## Wenn die Frist nicht eingehalten werden kann
> 1. **Gesuch um Fristerstreckung vor Ablauf der Frist** beim Gemeindesteueramt stellen (`zh-wl-2025__c0017`, § 39 Abs. 1 StV ZH, `zh-stv__par-39`).
> 2. **Dauer:** Rechtzeitige Gesuche werden längstens bis **30. November 2026** bewilligt (`zh-zstb-132-1__c0024`).
> 3. **Über den 30. November hinaus:** Solche Gesuche werden abgewiesen, ausser es werden ausserordentliche Gründe glaubhaft gemacht. Dafür braucht es in der Regel eine substanziierte Sachdarstellung. Starke berufliche Belastung der Vertretung oder fehlende Unterlagen genügen nicht (`zh-zstb-132-1__c0025`).
> 4. **Ablehnung:** Wird keine Erstreckung gewährt, folgt die Aufforderung, innert 30 Tagen einzureichen. Dagegen ist eine Beschwerde bei der Finanzdirektion möglich (`zh-zstb-132-1__c0025`; § 39 Abs. 2 StV: Aufsichtsbeschwerde).
> 5. **Von Amtes wegen bis 30. September 2026:** Das Gemeindesteueramt erstreckt die Frist automatisch für im Kanton wohnhafte Selbständigerwerbende, für übrige einer Branchenabteilung zugewiesene natürliche Personen und für ausserkantonal Wohnhafte (L- und B-Fälle) (`zh-zstb-132-1__c0023`).
> 6. **Wohnsitz in einem anderen Kanton:** Dessen Erstreckungsentscheid gilt auch für Zürich, wenn er dem Gemeindesteueramt vor Fristablauf mitgeteilt wird (`zh-wl-2025__c0017`).
> 
> ## Wenn die Frist bereits verpasst ist
> - Ein **nach Fristablauf gestelltes Gesuch wird abgewiesen**. Eine abgelaufene Frist kann nicht mehr erstreckt werden, höchstens **wiederhergestellt** werden (§ 15 StV, Art. 119 Abs. 2 und 124 Abs. 4 DBG). Zuständig ist das Gemeindesteueramt (`zh-zstb-132-1__c0024`).
> - **Mahnverfahren:** Es beginnt unmittelbar nach Fristablauf. Möglich ist vorher eine Aufforderung per Post mit 20 Tagen Frist (`zh-zstb-132-1__c0029`). Die Mahnfrist beträgt **10 Tage** und ist **nicht erstreckbar**. Angedroht werden Einschätzung nach pflichtgemässem Ermessen und eine Ordnungsbusse nach § 234 StG bzw. Art. 174 DBG (`zh-zstb-132-1__c0029`, `zh-wl-2025__c0017`).
> 
> ## Nicht geprüft
> - Ob ein erstes Gesuch ohne Gegenentscheid als stillschweigend bewilligt gilt: Das steht in der Wiki-Zusammenfassung von `wert`, ich habe es im Volltext nicht geöffnet.
> - Die Kosten einer Fristerstreckung: In den Quellen nicht genannt.
> - Die Fristen zählen nach der Verfahrensfassung ZStB 132.1, die ab 1.1.2026 gilt. Die Vorgängerfassung ist gleichlautend.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei der zuständigen Fachperson.

## b07

**Frage:** Wir sind eine Treuhandfirma und brauchen für Mandanten im Kanton Thurgau (Steuerperiode 2025, natürliche Personen) eine Fristerstreckung. Bei welcher Stelle ist das Gesuch einzureichen und bis wann kann die Frist längstens erstreckt werden?

**Soll (Referenz):** TG: Gesuch beim Gemeindesteueramt, das darüber entscheidet. Erstmals eingereichte Gesuche werden grundsätzlich bis längstens 30. September des Deklarationsjahres (2026) gutgeheissen; zusätzliche Gesuche in begründeten Fällen bis 30. November. Treuhänder/Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen, können für ihre Mandanten ein Gesuch längstens bis 31. Dezember des Deklarationsjahres beantragen. Arbeitsüberlastung ist kein Grund.

**Antwort des Agenten** (30.0 s · Tools: 6 Aufrufe steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **Kanton Thurgau · Steuerperiode 2025 (natürliche Personen)**
> 
> **Zuständige Stelle:** Das Gesuch geht an das **Gemeindesteueramt**, das auch darüber entscheidet. Die kantonale Steuerverwaltung ist für natürliche Personen nicht zuständig, nur für juristische Personen. Bei der direkten Bundessteuer gibt es keine eigene Regelung, die kantonale Fristerstreckung gilt auch dafür. (StP 155 Nr. 2, Ziff. 1, `tg-stp-155-2__c0001`, ☑️ agent-geprüft)
> 
> **Längste Frist:**
> - **Für Ihre Mandanten: bis 31. Dezember des Deklarationsjahres.** Gewerbsmässig tätige Treuhänder und Steuerberater können das für ihre Mandanten beantragen (`tg-stp-155-2__c0002`). Deklarationsjahr ist das Jahr der Einreichung. Für die Steuerperiode 2025 ist das **2026**, also längstens **bis 31.12.2026**.
> - Zum Vergleich gilt für Private ohne Vertreter: Das erste Gesuch wird in der Regel bis höchstens 30. September gutgeheissen. Weitere Gesuche gibt es in begründeten Fällen bis höchstens 30. November.
> - Über den 30. November bzw. 31. Dezember hinaus werden Gesuche abgewiesen, ausser Sie machen ausserordentliche Gründe glaubhaft. Das setzt in der Regel eine substanziierte Sachdarstellung voraus. Starke berufliche Inanspruchnahme des Vertreters oder fehlende Unterlagen genügen nicht (`tg-stp-155-2__c0002`).
> - Arbeitsüberlastung ist grundsätzlich kein Grund für eine Fristerstreckung.
> 
> **Formales und Gebühren:**
> - Das Gesuch ist schriftlich, begründet und rechtzeitig einzureichen, also vor Ablauf der angesetzten Frist (☑️ `wert tg 2025 fristerstreckung`).
> - Die erstmalige Fristerstreckung ist gebührenfrei. Für jedes weitere Gesuch wird eine Kanzleigebühr von Fr. 30 erhoben (§ 39b Abs. 2 und 3 StV TG, `tg-stv__par-39b`). Der Wortlaut von § 39b unterscheidet nicht nach natürlichen und juristischen Personen. Eine Bestätigung für natürliche Personen habe ich in der Praxis nicht gefunden, daher nur mit diesem Vorbehalt.
> - Den Entscheid erhält der Vertreter, wenn er das Gesuch gestellt hat. Eine verweigerte Fristerstreckung ist ein Zwischenentscheid und kann nicht selbständig angefochten werden (`tg-stp-155-2__c0005`).
> - Läuft eine erstreckte Frist unbenutzt ab, folgt eine Mahnung mit neuer Fristansetzung. Ab der zweiten Mahnung kostet das Fr. 50 (§ 39b Abs. 4 StV TG). Bei Fristversäumnis droht zudem eine Ermessensveranlagung (StP 155 Nr. 2, Ziff. 4, `tg-stp-155-2__c0006`, nicht im Wortlaut geöffnet).
> 
> **Offen:**
> - Heute ist der 9.11.2026. Wenn die ursprüngliche oder bereits erstreckte Frist schon abgelaufen ist, muss das Gesuch umgehend gestellt werden.
> - Ob Ihre Treuhandfirma als «gewerbsmässig» im Sinne der Praxis gilt und ob die Gemeinden zusätzliche formelle Anforderungen stellen, wie Sammelgesuche oder Mandantenlisten, steht in den Quellen nicht. Das ist bei den zuständigen Gemeindesteuerämtern zu klären.

## b08

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Auf welchem Formular wird der Abzug für Versicherungsprämien und Sparzinsen berechnet und in welche Ziffer der Steuererklärung wird das Ergebnis übertragen?

**Soll (Referenz):** AR 2025: Berechnung auf Formular 6 (A: bezahlte Prämien/Zinsen, B: Maximalabzug, C: Abzug = niedrigerer Betrag von A und B). Der Betrag C wird auf Seite 3 der Steuererklärung in Ziffer 14 übertragen.

**Antwort des Agenten** (24.7 s · Tools: 2 Aufrufe steuerwiki__position, steuerwiki__suche):

> **Kanton Appenzell Ausserrhoden · Steuerjahr 2025**
> 
> **Formular:** Der Abzug wird auf dem **Formular 6** berechnet. Das Formular heisst «Krankheits- und Unfallkosten, behinderungsbedingte Kosten». Seine Vorderseite enthält den Teil «Versicherungsprämien und Sparzinsen». Fundstellen: ar-wl-2025__c0085, ar-wl-2025__c0065 (Übersicht: Ziff. 14 → Formular 6), ar-form-06-2025__c0001. Status: ☑️ agent-geprüft.
> 
> **Ziffer:** Das Ergebnis, der Code **600**, wird in **Ziffer 14** «Versicherungsprämien und Sparzinsen» der Steuererklärung übertragen (ar-form-06-2025__c0002).
> 
> **Berechnung auf Formular 6**
> - **A (Code 600 A):** Krankenversicherung brutto + Unfallversicherung (ohne NBUV) + Lebens-/Rentenversicherung + Sparzinsen (gemäss Formular 2, Wertschriftenverzeichnis) − Prämienverbilligungen.
> - **B (Code 600 B), maximaler Abzug Kanton:** CHF 5'400 für gemeinsam Steuerpflichtige oder CHF 2'700 für übrige Steuerpflichtige. Dazu kommen CHF 1'000 je Kind mit Kinderabzug nach Ziff. 23.1–23.3.
> - **Abzug (Code 600):** Es gilt der niedrigere Betrag aus A und B.
> - Nicht aufführen: Mobiliar-, Motorfahrzeug-, Haftpflicht- und andere Sachversicherungen sowie die NBUV. Familien tragen die Prämien und Sparzinsen der ganzen Familie ein.
> 
> **Bund:** Das AR-Formular hat keine eigene Bundesspalte. Der Bundesabzug weicht ab: CHF 3'700 gemeinsam, CHF 1'800 übrige und CHF 700 je Kind. Ohne Beiträge an Säule 2/3a sind es CHF 5'550 bzw. CHF 2'700. Die Steuerverwaltung nimmt diese Anpassung automatisch vor (ar-wl-2025__c0179).
> 
> **Vorbehalt:** Die Zuordnung zu Ziff. 14 stammt aus der Wegleitung und den Formular-Miniaturen. Das Hauptformular 1 ist nicht online verfügbar. Der Code der Hauptformular-Zeile für Ziff. 14 ist deshalb nicht separat am Originalformular geprüft. Die fachliche Beurteilung bleibt bei der Fachperson.

## b09

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wo und wie ist ein Gesuch um Fristverlängerung für die Steuererklärung einer natürlichen Person zu stellen und bis wann?

**Soll (Referenz):** SG 2025: Das Gesuch ist vor Ablauf der Einreichefrist (Datum auf Seite 1 der Steuererklärung) zu stellen, vorzugsweise elektronisch unter www.steuern.sg.ch (mit Registernummer und Geburtsdatum); sonst schriftlich an das Gemeindesteueramt. Es kann eine angemessene Fristverlängerung gewährt werden.

**Antwort des Agenten** (26.1 s · Tools: 8 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige):

> **St. Gallen · Steuerjahr 2025**
> 
> **Wo und wie**
> - **Elektronisch (empfohlen):** über die eFristverlängerung auf www.steuern.sg.ch. Dafür braucht es die **Register-Nr.** und das **Geburtsdatum**, beide stehen auf der persönlichen Steuererklärung. Das Gesuch wird interaktiv bewilligt oder abgelehnt. (sg-wl-2025__c0018, sg-info-fristverlaengerung__c0002 · ☑️ agent-geprüft)
> - **Schriftlich:** Wer es nicht elektronisch stellt, richtet das Gesuch schriftlich an das **Gemeindesteueramt**. Dieses ist auch die Einreichestelle der Steuererklärung. (sg-wl-2025__c0018 · ☑️)
> 
> **Bis wann**
> - Das Gesuch muss **vor Ablauf der Einreichefrist** gestellt werden. Danach ist keine Verlängerung mehr möglich.
> - Die Einreichefrist ist der **Einreichetermin auf Seite 1 der Steuererklärung 2025**. Das konkrete Datum steht nicht im Wiki, deshalb nenne ich keines. Bitte auf dem Formular ablesen.
> 
> **Voraussetzung**
> - Die Verlängerung wird nur gewährt, wenn die **fälligen Steuerrechnungen bezahlt** sind. (sg-info-fristverlaengerung__c0002)
> 
> **Bund**
> - Die direkte Bundessteuer hat keine eigene Fristerstreckung. Die kantonale Regelung gilt auch für die Bundessteuer, weil dieselbe Steuererklärung eingereicht wird.
> 
> **Nicht belegt, daher offen**
> - Die Dauer der Verlängerung: Die Wegleitung spricht nur von einer «angemessenen Fristverlängerung».
> - Eine Sonderregel für Treuhänder, etwa Sammelgesuche: Dazu habe ich in den Quellen nichts gefunden.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## b10

**Frage:** Ehepaar im Kanton St.Gallen, Steuerjahr 2025, zwei Kinder mit Kinderabzug, keine Beiträge an die 2. Säule oder Säule 3a bei beiden Partnern. Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Kantons-/Gemeindesteuern und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2025 Kanton: Fr. 6'800 + zusätzlich ohne 2. Säule/3a bis Fr. 1'100 + 2 x bis Fr. 1'100 für die Kinder = Fr. 10'100. Bund: Fr. 3'700 + zusätzlich bis Fr. 1'850 (= Fr. 5'550) + 2 x Fr. 700 = Fr. 6'950. (Voraussetzung für den Zusatzabzug muss bei beiden Partnern erfüllt sein.)

**Antwort des Agenten** (26.1 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Kanton St. Gallen · Steuerjahr 2025** (Ehepaar, 2 Kinder mit Kinderabzug, weder 2. Säule noch Säule 3a bei beiden Partnern)
> 
> Der Abzug für Versicherungsprämien und Sparzinsen steht in Ziff. 14 (Code 600) und wird im Hilfsblatt Formular 6 berechnet. Abziehbar ist der niedrigere Betrag aus den effektiv bezahlten Prämien und Sparzinsen (A) und dem Maximalabzug (B).
> 
> **Kantons- und Gemeindesteuern: maximal CHF 10'100**
> 
> | Teil | Betrag (CHF) |
> |---|---|
> | Grundabzug gemeinsam steuerpflichtige Ehegatten | 6'800 |
> | Zuschlag ohne Beiträge an 2. Säule und Säule 3a (bei beiden Partnern) | 1'100 |
> | Kinderzuschlag, 2 × 1'100 | 2'200 |
> | **Maximalabzug (B)** | **10'100** |
> 
> Quelle: sg-stg-2025__art-45-t2 und sg-form-6-2025__c0002. Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Direkte Bundessteuer: maximal CHF 6'950**
> 
> | Teil | Betrag (CHF) |
> |---|---|
> | Grundabzug Ehepaar | 3'700 |
> | Zuschlag ohne Beiträge an 2. Säule und Säule 3a (+50 %) | 1'850 |
> | Zwischensumme ohne Vorsorge | 5'550 |
> | Kinderzuschlag, 2 × 700 | 1'400 |
> | **Maximalabzug (B)** | **6'950** |
> 
> Quelle: bund-dbg-2025__art-33-t2 und bund-dbg-2025__art-33-t5. Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> **Hinweise**
> - Die Beträge sind Höchstgrenzen. Abziehbar ist der niedrigere Betrag aus den effektiv bezahlten Prämien und Sparzinsen (A) und dem Maximum (B). Dabei zählen Krankenkasse brutto, Unfall ohne NBU, Lebens- und Rentenversicherung sowie Sparzinsen. Die Prämienverbilligungen (IPV) werden abgezogen.
> - Die Zuschläge ohne Vorsorge gelten bei Ehepaaren nur, wenn beide Partner weder BVG- noch Säule-3a-Beiträge abziehen.
> - Der Kinderzuschlag gilt nur für Kinder, für die der Kinderabzug nach Ziff. 23.1 oder 23.2 geltend gemacht wird.
> - Der Zuschlag von CHF 1'100 ohne Vorsorge ist im Gesetz als «bis zu»-Betrag formuliert. Das Wiki leitet die CHF 7'900 daher als Summe ab.
> - Im SG-Formular gibt es nur eine Spalte. Die Bundesbeträge setzt die Steuerbehörde automatisch um, es ist keine separate Deklaration nötig.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## b11

**Frage:** Arbeitnehmer im Kanton Thurgau, Steuerjahr 2026, Arbeitsweg mit ÖV-Jahresabonnement, effektive Kosten Fr. 6'400. Welcher Fahrkostenabzug ist bei den Staats-/Gemeindesteuern und welcher bei der direkten Bundessteuer zulässig?

**Soll (Referenz):** TG 2026: Kanton gesamthaft max. Fr. 6'000, deshalb Abzug Fr. 6'000 (effektive Kosten Fr. 6'400 werden gekürzt). Bund max. Fr. 3'300, deshalb Abzug Fr. 3'300.

**Antwort des Agenten** (23.7 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__rechne):

> **Thurgau · Steuerjahr 2026**
> 
> Bei effektiven Kosten von Fr. 6'400 für das ÖV-Jahresabonnement gelten folgende Abzüge:
> 
> | | Effektive Kosten | Höchstbetrag | Zulässiger Abzug | Nicht abziehbar |
> |---|---|---|---|---|
> | **Staats-/Gemeindesteuern TG** | Fr. 6'400 | Fr. 6'000 | **Fr. 6'000** | Fr. 400 |
> | **Direkte Bundessteuer** | Fr. 6'400 | Fr. 3'300 | **Fr. 3'300** | Fr. 3'100 |
> 
> **Kanton und Gemeinde:** Der Abzug für Fahrten zwischen Wohn- und Arbeitsstätte ist auf maximal Fr. 6'000 pro Person begrenzt. Das gilt gesamthaft, also inklusive Wochenaufenthalt und Nebenerwerb. Die Begrenzung wird auch bei unterjähriger Steuerpflicht oder Teilzeit nicht gekürzt. (Fundstelle: tg-wl-2026__c0176, Status ☑️ agent-geprüft, Abnahme offen)
> 
> **Direkte Bundessteuer:** Abziehbar sind die notwendigen Kosten bis höchstens Fr. 3'300 (Art. 26 Abs. 1 lit. a DBG). Für den Bund spielt die Anzahl Arbeitstage bei Fahrkosten keine Rolle. (Fundstelle: bund-dbg-2026__art-26, Status ☑️ agent-geprüft, Abnahme offen)
> 
> **Im Formular:** Die Fahrkosten gehören in die Berufsauslagen bei unselbständiger Erwerbstätigkeit (TG 2026, Ziff. 10.1 bzw. 10.2). Die Bundesbegrenzung wird im Thurgauer Formular nicht separat erfasst, sie wird bei der Veranlagung auf Bundesebene angewendet. Wie genau das Formular die Bundesspalte behandelt, habe ich hier nicht mit `position` geprüft.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## b12

**Frage:** Ehepaar im Kanton Zürich, Steuerjahr 2026, nachgewiesene Kinderdrittbetreuungskosten: Kind A (5 Jahre) Fr. 30'000, Kind B (8 Jahre) Fr. 12'000. Wie hoch ist der Abzug bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2026: Maximum pro Kind Staat Fr. 25'300, Bund Fr. 25'800 (Kinder unter 14). Staat: 25'300 + 12'000 = Fr. 37'300. Bund: 25'800 + 12'000 = Fr. 37'800. (Zum Vergleich 2025: Staat max. Fr. 25'000.)

**Antwort des Agenten** (24.5 s · Tools: 3 Aufrufe steuerwiki__wert, steuerwiki__position, steuerwiki__rechne):

> **Kanton Zürich · Steuerjahr 2026 · Kinderdrittbetreuung (Ziff. 16.6, Code 376)**
> 
> Der Höchstbetrag gilt pro Kind. Die Kosten werden daher je Kind begrenzt und danach addiert.
> 
> | | Kind A (5 J.) | Kind B (8 J.) | **Total Abzug** |
> |---|---|---|---|
> | Nachgewiesene Kosten | 30'000 | 12'000 | 42'000 |
> | **Staatssteuer** (max. 25'300 je Kind) | 25'300 (gekürzt) | 12'000 | **Fr. 37'300** |
> | **Direkte Bundessteuer** (max. 25'800 je Kind) | 25'800 (gekürzt) | 12'000 | **Fr. 37'800** |
> 
> - Kind B bleibt unter dem Höchstbetrag und wird voll abgezogen.
> - Bei Kind A fallen 4'700 (Staat) bzw. 4'200 (Bund) weg.
> - Die Berechnung ist mit dem Rechentool geprüft.
> 
> **Voraussetzungen** (aus der Tool-Ausgabe, nicht für den konkreten Fall geprüft):
> - Beide Kinder sind unter 14 Jahren.
> - Beide Kinder leben im Haushalt der Eltern.
> - Die Betreuung steht im direkten Zusammenhang mit der Erwerbstätigkeit oder Ausbildung. Bei einem Ehepaar müssen beide gleichzeitig erwerbstätig, in Ausbildung oder erwerbsunfähig sein.
> - Verpflegung, Sport, Musik, Schulgeld und Nachhilfe sind nicht abziehbar. Das gilt auch für Reise-, Verpflegungs- und Übernachtungskosten bei Ferienbetreuung.
> - Sind die Kosten nur pauschal ausgewiesen, sind 20 % als Lebenshaltungskosten zu kürzen.
> - Einzureichen sind die Rechnungen mit Zahlungsnachweis und eine Aufstellung mit den Empfängern.
> 
> **Fundstellen und Status:**
> - Staatssteuer: zh-stg-2026__par-31-t3, ☑️ agent-geprüft.
> - Bundessteuer: bund-dbg-2026__art-33-t7, ☑️ agent-geprüft.
> - Formular: zh-form-300-2026-uj__c0008 und zh-wl-2026-uj__c0105, ☑️ agent-geprüft.
> 
> **Vorbehalt Formular:** Das reguläre Formular und die Wegleitung ZH 2026 sind noch nicht publiziert (Stand 09.11.2026). Die Ziffer 16.6 und der Code 376 stammen aus der Fassung für unterjährige Steuerpflicht. Sie sollten am regulären Formular nochmals geprüft werden. Die fachliche Beurteilung bleibt bei der Fachperson.

## b13

**Frage:** Ein Mitglied der Milizfeuerwehr erhält für die Erfüllung von Kernaufgaben (Übungen, Pikettdienst, Ernstfalleinsätze) Sold. Bis zu welchem Betrag ist der Feuerwehrsold bei der direkten Bundessteuer steuerfrei, im Steuerjahr 2025 und im Steuerjahr 2026?

**Soll (Referenz):** Bund: 2025 steuerfrei bis maximal Fr. 5'300; 2026 steuerfrei bis maximal Fr. 5'400 (Wert hat sich geändert, nicht übertragen). Der gesamte Sold ist auf dem Lohnausweis zu deklarieren; der steuerfreie Betrag wird auf Formular 9 Berufskosten Ziffer 8 abgezogen.

**Antwort des Agenten** (21.1 s · Tools: 2 Aufrufe steuerwiki__wert):

> Bund (direkte Bundessteuer) · Steuerjahr 2025 und 2026. Die Frage nennt keinen Kanton, deshalb gelten die Bundeswerte.
> 
> | Steuerjahr | Steuerfreier Feuerwehrsold (pro Jahr) | Fundstelle | Status |
> |---|---|---|---|
> | 2025 | **CHF 5'300** | bund-dbg-2025__art-24-t2 (Art. 24 lit. fbis DBG) | ☑️ agent-geprüft |
> | 2026 | **CHF 5'400** | bund-dbg-2026__art-24-t2 (Art. 24 lit. fbis DBG) | ☑️ agent-geprüft |
> 
> Der Betrag erhöht sich 2026 gegenüber dem Vorjahr um CHF 100.
> 
> - Die Befreiung gilt nur für den Sold für Kernaufgaben, also Übungen, Pikettdienst und Ernstfalleinsätze.
> - Der Betrag ist ein Höchstbetrag pro Jahr. Was darüber hinausgeht, ist steuerbar.
> - Nicht unter die Befreiung fallen laut Wiki (Text 2026) Pauschalzulagen für Kader, Funktionszulagen, administrative Arbeiten und freiwillige Dienstleistungen.
> - Den gesamten Sold muss man im Lohnausweis deklarieren (Hinweis im Text 2026). Das Wiki hat dazu keinen Text für 2025. Ich kann daher nicht sagen, ob das auch für 2025 gilt.
> 
> Die Abnahme der beiden Werte ist noch offen. Die fachliche Beurteilung bleibt bei der Fachperson.

## b14

**Frage:** Ein Mandant wohnt am 31.12.2026 im Kanton Luzern und pendelt mit dem Auto zur Arbeit. Welcher Fahrkostenabzug gilt für die Luzerner Staats- und Gemeindesteuern 2026 und für die direkte Bundessteuer?

**Soll (Referenz):** Luzern ist im Wiki nicht abgedeckt (nur Bund, AR, SG, TG, ZH): kein Wert für die Luzerner Staats-/Gemeindesteuer nennen, auf kantonale Wegleitung verweisen. Für die direkte Bundessteuer 2026 gilt max. Fr. 3'300 (Wegleitung Bund 2026).

**Antwort des Agenten** (23.4 s · Tools: 1 Aufrufe steuerwiki__wert):

> **Luzern · Steuerjahr 2026**
> 
> **Kanton Luzern (Staats- und Gemeindesteuern): nicht im Wiki.** Das Wiki deckt nur Bund, AR, SG, TG und ZH ab. Zum Luzerner Fahrkostenabzug nenne ich deshalb keine Zahl, weder Maximum noch Kilometeransatz oder Arbeitstage. Das müsste anhand der Luzerner Quellen geprüft werden, etwa Steuergesetz und Wegleitung der Dienststelle Steuern Luzern. Werte aus anderen Kantonen sind nicht übertragbar.
> 
> **Direkte Bundessteuer 2026**
> 
> Der Bundesabzug gilt für alle Kantone gleich. Die Quelle für das Maximum ist Art. 26 DBG (`bund-dbg-2026__art-26`). Alle Werte haben den Status ☑️ agent-geprüft: Die Fundstelle ist geprüft, die Abnahme ist offen.
> 
> | Position | Wert |
> |---|---|
> | Maximalabzug Fahrten Wohn-/Arbeitsstätte | **CHF 3'300** pro Jahr |
> | Privatauto | **CHF 0.75 pro Fahrkilometer** (2025: 0.70), Gesamtmaximum CHF 3'300 |
> 
> - **Voraussetzung Auto:** Der Kilometeransatz gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist. Sonst werden nur die Kosten des öffentlichen Verkehrs anerkannt (RS 2-215).
> - **Quelle 0.75:** `bund-mm-2025-09-11-kalte-progression-2026__c0004`. Der Ansatz ist neu ab 2026 und künftig an den TCS-Kilometerpreis gekoppelt.
> - **Arbeitstage:** Der Bund kennt keine Arbeitstage-Basis. Abgezogen werden die tatsächlichen Kosten bis höchstens CHF 3'300.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson. Wenn Sie wollen, kann ich den Bundesabzug mit den konkreten Kilometern des Mandanten durchrechnen.

