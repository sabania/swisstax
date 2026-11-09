# OpenClaw-Testlauf: blindtest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuermem` · Fragen: 14 · Lauf: 2026-11-09 06:12
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## b01

**Frage:** Ehepaar in rechtlich und tatsächlich ungetrennter Ehe, weder Beiträge an die 2. Säule noch an die Säule 3a, Kanton ZH, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Zinsen von Sparkapitalien bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2025: Staatssteuer höchstens CHF 8'700 (Grundabzug CHF 5'800, ohne Beiträge an 2. Säule/3a um die Hälfte erhöht). Direkte Bundessteuer 2025: höchstens CHF 5'550 (Grundabzug CHF 3'700, um die Hälfte erhöht).

**Antwort des Agenten** (30.6 s · Tools: 5 Aufrufe read, exec):

> **Ehepaar in ungetrennter Ehe, ZH, Steuerjahr 2025, weder 2. Säule noch Säule 3a, ohne Kinder oder unterstützte Personen:**
> 
> | Ebene | Maximaler Abzug (Ziff. 15, Code 270) | Fundstelle |
> |---|---|---|
> | **Staatssteuer ZH** | **CHF 8'700** (Grundbetrag 5'800, um die Hälfte erhöht) | [Formular 365 ZH 2025 S. 1, Teil B Ziff. 1](steuerwiki/chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md); [WL ZH 2025 S. 15](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0086.md); [§ 31 Abs. 1 lit. g StG ZH](steuerwiki/chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t2.md) |
> | **Direkte Bundessteuer** | **CHF 5'550** (Grundbetrag 3'700, um die Hälfte erhöht) | [Formular 365 ZH 2025 S. 1](steuerwiki/chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md); [Art. 33 Abs. 1bis lit. a DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t5.md); [RS 2-210 S. 2](steuerwiki/chunks/bund/2025/bund-rs-2-210/bund-rs-2-210__c0006.md) |
> 
> Status: ☑️ agent-geprüft. Ich habe die Chunks selbst gelesen und die Werte stimmen überein. Die Fachperson hat sie noch nicht als ✅ verifiziert.
> 
> **Hinweise**
> - **Kinder und unterstützte Personen:** Pro Kind oder unterstützungsbedürftiger Person mit Kinder- bzw. Unterstützungsabzug kommen CHF 1'300 (Staat) und CHF 700 (Bund) dazu. Bei halbem Kinderabzug gilt der halbe Zuschlag.
> - **Bedingung für den erhöhten Betrag:** Weder die Steuerpflichtigen noch ihr Arbeitgeber dürfen Beiträge an die 2. Säule oder die Säule 3a geleistet haben. Pensionskassenbeiträge, die der Arbeitgeber vom Lohn abzieht oder für sie zahlt, schliessen die Erhöhung also aus. Das ist wohl der häufigste Stolperstein. Die Wegleitung nennt «von den Steuerpflichtigen oder ihrem Arbeitgeber» ausdrücklich. Bei Ehepaaren ist die Frage für beide Partner zu prüfen; die Formulierung der Wegleitung ZH dazu habe ich nicht gesondert nachgeprüft.
> - **Höchstbetrag, nicht Pauschale:** Abziehbar ist der niedrigere Betrag aus (A) den effektiv bezahlten Prämien und Sparzinsen, netto nach Prämienverbilligung, und (B) dem Maximalbetrag. Das Formular 365 Teil C rechnet das aus.
> - **Berechnung:** Die Erhöhung um die Hälfte ergibt 5'800 × 1.5 = 8'700 und 3'700 × 1.5 = 5'550. Beide Werte stehen so im Formular 365.

## b02

**Frage:** Wie hoch ist im Steuerjahr 2026 der Maximalabzug für Fahrkosten zwischen Wohn- und Arbeitsort im Kanton St.Gallen (Kantons- und Gemeindesteuern) und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2026: Kantons- und Gemeindesteuern max. Fr. 8'000; direkte Bundessteuer max. Fr. 3'300. Es ist ein Maximalabzug, keine Pauschale (bei Teilzeit/unterjährig nicht gekürzt).

**Antwort des Agenten** (31.9 s · Tools: 7 Aufrufe read, exec):

> **Steuerjahr 2026, Maximalabzug für Fahrkosten zwischen Wohn- und Arbeitsstätte:**
> 
> | Ebene | Maximalabzug | Fundstelle | Status |
> |---|---|---|---|
> | **SG Kantons- und Gemeindesteuern** | **CHF 8'000** | Art. 39 Abs. 1 lit. a StG SG (Fassung 2026): «bis zum Betrag von Fr. 8000.–» ([`sg-stg-2026__art-39`](steuerwiki/chunks/sg/2026/sg-stg-2026/sg-stg-2026__art-39.md)). Bestätigt durch StB 39 Nr. 3 Ziff. 3, Tabelle: «2026 Fr. 8'000.--» ([`sg-stb-39-3__c0011`](steuerwiki/chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0011.md), S. 3–4). | ☑️ agent-geprüft |
> | **Direkte Bundessteuer** | **CHF 3'300** | Art. 26 Abs. 1 lit. a DBG (Fassung 2026): «bis zu einem Maximalbetrag von 3300 Franken» ([`bund-dbg-2026__art-26`](steuerwiki/chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-26.md)). Dieselbe SG-Tabelle weist die Spalte «Direkte Bundessteuer» mit «2026 Fr. 3'300.--» aus. | ☑️ agent-geprüft |
> 
> **Hinweise zur Anwendung** (StB 39 Nr. 3 Ziff. 3, `sg-stb-39-3__c0011`):
> - Es ist ein Maximalabzug, keine Pauschale. Er wird bei unterjähriger Steuerpflicht, Aufnahme oder Aufgabe der Erwerbstätigkeit im Jahr und bei Teilzeit nicht gekürzt.
> - Bei unselbständiger Haupt- und Nebenerwerbstätigkeit gilt die Begrenzung insgesamt, nicht je Tätigkeit.
> - Abgezogen werden die tatsächlich notwendigen Kosten bis zu diesem Betrag. Die Ansätze pro km für Auto und Motorrad sowie die Velo-Pauschale stehen in `quick/werte-sg-2026.md` und `quick/werte-bund-2026.md`.
> 
> **Korrektur an der Wiki-Seite:** Die Detailseite `wiki/sg/werte-sg-2026-detail.md` sagt, die zweite Spalte (Fr. 3'300) sei im Chunk nicht erklärt. Das stimmt nicht. Die Spaltenüberschrift im Original lautet «Direkte Bundessteuer». Die Zahl deckt sich mit Art. 26 DBG, ich habe sie daher oben dem Bund zugeordnet. Die Wiki-Seite habe ich nicht geändert.
> 
> Beide Werte stehen im Gesetzestext der Fassung 2026, die Fachperson hat sie noch nicht verifiziert (✅).

## b03

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Welchen Kinderabzug können Eltern für ein 3-jähriges, ein 10-jähriges und ein 16-jähriges (noch minderjähriges) Kind geltend machen?

**Soll (Referenz):** AR (Kantonssteuer) 2025: 3-jähriges Kind (bis Vollendung des 4. Altersjahrs) Fr. 5'000; 10-jähriges Kind (nach Vollendung des 4. bis Vollendung des 15. Altersjahrs) Fr. 7'000; 16-jähriges Kind (nach Vollendung des 15. Altersjahrs bis Volljährigkeit) Fr. 11'000. Gleiche Beträge gelten für volljährige Kinder in Ausbildung bis zum 26. Altersjahr.

**Antwort des Agenten** (38.2 s · Tools: 6 Aufrufe read, exec):

> **Kanton AR, Steuerjahr 2025 (Staats- und Gemeindesteuer), pro Kind:**
> 
> | Kind | Stufe (Ziff. Steuererklärung) | Abzug |
> |---|---|---|
> | 3-jährig | 23.1: bis zur Vollendung des 4. Altersjahrs | **CHF 5'300** |
> | 10-jährig | 23.2: nach Vollendung des 4. bis zur Vollendung des 15. Altersjahrs | **CHF 7'400** |
> | 16-jährig, minderjährig | 23.3: nach Vollendung des 15. Altersjahrs bis Volljährigkeit | **CHF 11'600** |
> | **Total** | | **CHF 24'300** |
> 
> Fundstellen: StG AR Anhang 1, Art. 38 Abs. 1 lit. a Ziff. 1–3 (`ar-stg-anhang-kp__c0001`) und WL AR 2025 S. 2 (`ar-wl-2025__c0005`). Der Status im Wiki ist 🟡 extrahiert für die Zuordnung zu den Ziffern und ☑️ agent-geprüft für die Beträge.
> 
> **Direkte Bundessteuer (separat):**
> - Der Bund kennt keine Altersstufen. Der Kinderabzug beträgt **CHF 6'800 pro minderjähriges Kind**, bei drei Kindern also **CHF 20'400** (Art. 35 Abs. 1 lit. a DBG, `bund-dbg-2025__art-35`; Status ☑️).
> - Zusätzlich gibt es eine Ermässigung des Steuerbetrags von CHF 263 pro Kind (Art. 36 Abs. 2bis DBG, `bund-dbg-2025__art-36-t4`). Das ist ein Abzug vom Steuerbetrag und kein Abzug vom Einkommen.
> 
> **Voraussetzungen und Hinweise:**
> - **Stichtag:** Massgebend ist das Alter am **31.12.2025** (WL AR 2025 S. 19, `ar-wl-2025__c0104`). Das Wiki legt nicht fest, ab welchem Tag ein Altersjahr als «vollendet» gilt. Ich bin davon ausgegangen, dass die genannten Alter am Stichtag gelten. Bei Kindern nahe an einer Altersgrenze (4./15. Geburtstag) das Geburtsdatum prüfen.
> - **Bedingungen:** Der Abzug gilt, wenn die Eltern den Unterhalt zur Hauptsache bestreiten und das Kind auf Unterhalt angewiesen ist. Wenn die Einkünfte des Kindes CHF 18'000 übersteigen, entfällt er.
> - **Getrennte Eltern:** Der Abzug wird hälftig geteilt, wenn gemeinsame elterliche Sorge besteht und keine Unterhaltsbeiträge geltend gemacht werden. Wer für ein Kind Unterhaltsbeiträge nach Ziff. 12.2 abzieht, kann dafür keinen Kinderabzug geltend machen.
> - **Merkblatt 02:** Es nennt noch CHF 5'000, 7'000 und 11'000. Das sind die nicht indexierten Werte. Massgebend sind Anhang 1 und die Wegleitung 2025 mit CHF 5'300, 7'400 und 11'600.
> - **Ziffern-Codes:** Die Codes für Seite 3 der Steuererklärung sind im Wiki nicht verifiziert, weil die Wegleitung sie nicht als Miniatur zeigt.
> - **Weitere kindbezogene Positionen:** Der Versicherungsabzug erhöht sich um CHF 1'000 pro Kind (Kanton). Beim Vermögen gibt es einen Sozialabzug von CHF 25'000 pro minderjähriges Kind. Kinderdrittbetreuung ist bis CHF 25'000 pro Kind unter 14 Jahren abziehbar, also für das 3- und das 10-jährige Kind.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## b04

**Frage:** Alleinstehende Person ohne Kinder mit Beiträgen an die 2. Säule, Kanton Thurgau, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Staats-/Gemeindesteuern und bei der Bundessteuer?

**Soll (Referenz):** TG 2025: Staat max. Fr. 3'500, Bund max. Fr. 1'800 (ohne Beiträge an Säule 2/3a würde beim Bund Fr. 2'700 gelten). Betrag vor Abzug Prämienverbilligungen Krankenkassen.

**Antwort des Agenten** (32.6 s · Tools: 7 Aufrufe read):

> **Kanton Thurgau, Steuerjahr 2025, alleinstehend ohne Kinder, mit Beiträgen an die 2. Säule**
> 
> | Ebene | Maximalabzug (Ziff. 14, Formular 5.2) | Fundstelle | Status |
> |---|---|---|---|
> | **Staats-/Gemeindesteuer TG** | **CHF 3'500** | § 34 Abs. 1 Ziff. 9 StG TG ([tg-stg__par-34-t3](steuerwiki/chunks/tg/2025/tg-stg/tg-stg__par-34-t3.md)); Formular 5.2 TG 2025, Teil B Zeile 2 ([tg-form-05-2-2025__c0002](steuerwiki/chunks/tg/2025/tg-form-05-2-2025/tg-form-05-2-2025__c0002.md)) | ☑️ agent-geprüft |
> | **Direkte Bundessteuer** | **CHF 1'800** | Art. 33 Abs. 1 lit. g DBG ([bund-dbg-2025__art-33-t2](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t2.md)); Formular 5.2 TG 2025, Teil B Zeile 2 | ☑️ agent-geprüft |
> 
> - **Kinderzuschlag:** Er entfällt, weil die Person keine Kinder hat. Er beträgt sonst CHF 1'000 (Staat) bzw. CHF 700 (Bund) pro Kind oder unterstützte Person mit Kinder- bzw. Unterstützungsabzug (Art. 33 Abs. 1bis lit. b DBG, [art-33-t5](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t5.md)).
> - **Erhöhte Bundeslimite:** Die erhöhte Bundeslimite von CHF 2'700 gilt nur ohne Beiträge an die Säule 2 oder 3a (Art. 33 Abs. 1bis lit. a DBG). Hier gilt sie nicht, weil die Person in die 2. Säule einzahlt. Kantonal gibt es keine erhöhte Limite.
> - **Tatsächlicher Abzug:** Der tatsächliche Abzug ist der niedrigere Betrag aus den bezahlten Prämien und Sparzinsen und dem Maximum, getrennt für Staat und Bund. Die Krankenkassenprämie zählt netto nach Prämienverbilligung. Bei Prämien und Zinsen von z. B. CHF 4'000 ergeben sich CHF 3'500 (Staat) und CHF 1'800 (Bund). Das Beispiel ist von mir gerechnet, nicht aus einer Quelle.
> - **Übertrag:** Die Berechnung läuft über Formular 5.2 (Code 330) in Ziff. 14 der Steuererklärung.
> 
> Die Werte stammen aus den ☑️-Einträgen des Wikis. Die Fachperson hat sie noch nicht verifiziert (✅).

## b05

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wie hoch ist der Kinderabzug für ein noch nicht schulpflichtiges Kind und für ein Kind in Schule oder Ausbildung bei den Kantons-/Gemeindesteuern?

**Soll (Referenz):** SG 2025: noch nicht schulpflichtiges Kind Fr. 7'600 (Ziff. 23.1); Kind in Schule oder Ausbildung (auch volljährig) Fr. 10'800 (Ziff. 23.2).

**Antwort des Agenten** (30.0 s · Tools: 6 Aufrufe read, read):

> **Kanton St. Gallen, Steuerjahr 2025, Staats- und Gemeindesteuern (nicht direkte Bundessteuer)**
> 
> | Kind | Kinderabzug | Fundstelle |
> |---|---|---|
> | Noch nicht schulpflichtig | **CHF 7'600** | Art. 48 Abs. 1 lit. a Ziff. 1 StG SG, `sg-stg-2025__art-48` |
> | In schulischer oder beruflicher Ausbildung | **CHF 10'800** | Art. 48 Abs. 1 lit. a Ziff. 2 StG SG, `sg-stg-2025__art-48` |
> 
> Der Status ist bei beiden Werten ☑️ agent-geprüft (nicht von einer Fachperson verifiziert). Die Beträge stimmen mit dem Gesetzeswortlaut im Chunk überein.
> 
> **Voraussetzungen**
> - Die steuerpflichtige Person muss zur Hauptsache für den Unterhalt des Kindes aufkommen.
> - Sie darf keinen Abzug für Unterhaltsbeiträge nach Art. 45 Abs. 1 lit. c StG geltend machen. Sonst entfällt der Kinderabzug.
> - Der Abzug gilt für ein Kind unter ihrer elterlichen Sorge oder Obhut. Beim Abzug von 10'800 gilt er auch für ein volljähriges Kind in Ausbildung.
> - Massgebend sind die Verhältnisse am Ende der Steuerperiode oder der Steuerpflicht (Abs. 2). Bei nur teilweiser Steuerpflicht wird der Abzug anteilmässig gewährt. Für den Steuersatz zählt er voll (Abs. 3).
> 
> **Zusätzlich bei Ausbildung (Art. 48 Abs. 1 lit. a Ziff. 3)**
> - Es können höchstens weitere CHF 13'700 für Ausbildungskosten abgezogen werden.
> - Das gilt nur für Kosten, die die steuerpflichtige Person selbst trägt und die CHF 3'200 übersteigen.
> 
> **Nicht verwechseln**
> - Für ein Kind im Schulalter nennt das Wiki denselben Betrag von CHF 10'800 (`kind_schule`). SG unterscheidet also nicht zwischen Schule und Ausbildung.
> - Die Bundessteuer hat eigene Kinderabzüge. Sie sind hier nicht beantwortet, stehen aber in `quick/werte-bund-2025.md`.
> - Zusätzlich gibt es im Versicherungsabzug einen Zuschlag von CHF 1'100 pro Kind (Art. 45 StG, Kategorie `versicherung.kind`). Das ist ein separater Abzug.
> - Zum Vermögen gibt es einen Sozialabzug von CHF 20'000 pro Kind (Art. 64 StG, Kategorie `vermoegen.freibetrag_kind`).
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## b06

**Frage:** Bis wann ist die Steuererklärung 2025 einer natürlichen Person im Kanton Zürich einzureichen, und wie ist vorzugehen, wenn die Frist nicht eingehalten werden kann?

**Soll (Referenz):** ZH, Steuerperiode 2025: Einreichung bis 31. März 2026 (online oder an das Scan-Center). Gesuch um Fristerstreckung ist vor Ablauf der Frist beim Gemeindesteueramt zu stellen. Mahnfristen sind nicht erstreckbar.

**Antwort des Agenten** (39.4 s · Tools: 8 Aufrufe read):

> **Stichtag (Kanton ZH, Steuerjahr 2025):** Die Steuererklärung 2025 ist bis zum **31. März 2026** einzureichen (WL ZH 2025 S. 7, `zh-wl-2025__c0017`). Das gilt für die Staats- und Gemeindesteuer und die direkte Bundessteuer zusammen, weil es nur eine kantonale Steuererklärung gibt (Art. 124 DBG). Für Steuerjahr 2025 ist die Wegleitung die Fundstelle. Status ☑️ agent-geprüft.
> 
> Heute ist der 9. November 2026, die ordentliche Frist ist also schon abgelaufen. Was jetzt noch möglich ist, hängt davon ab, ob rechtzeitig ein Gesuch gestellt wurde (siehe unten).
> 
> ## Wenn die Frist nicht eingehalten werden kann
> 
> 1. **Gesuch vor Fristablauf stellen.** Es geht an das Gemeindesteueramt (WL ZH 2025 S. 7, `zh-wl-2025__c0017`). Eine abgelaufene Frist kann nicht mehr erstreckt werden. Verspätete Gesuche sind abzuweisen und können höchstens zu einer Wiederherstellung der Frist führen (ZStB 132.1 Ziff. G.II, `zh-zstb-132-1__c0024`, Fassung ab 2026).
> 2. **Erstreckung bis längstens 30. November 2026.** Rechtzeitige Gesuche sind entsprechend dem Gesuch zu bewilligen, längstens bis 30. November des Folgejahres (ZStB 132.1 bis 2025, G.II.2 b), `zh-zstb-132-1-bis-2025__c0021`; gleich in der Fassung ab 2026, `zh-zstb-132-1__c0024`). Das erste rechtzeitige Gesuch gilt ohne gegenteiligen schriftlichen Entscheid als stillschweigend bewilligt (`…__c0023`). Einen schriftlichen Entscheid gibt es nur auf ausdrückliches Begehren, bei verspäteten Gesuchen und bei Gesuchen über den 30. November hinaus.
> 3. **Über den 30. November hinaus** werden Gesuche abgewiesen, ausser es werden ausserordentliche Gründe glaubhaft gemacht. Das braucht in der Regel eine substanziierte Sachdarstellung. Starke berufliche Beanspruchung der Vertretung oder fehlende Unterlagen genügen nicht (`…__c0021`). Bei Abweisung wird eine Frist von 30 Tagen zur Einreichung angesetzt, und der Entscheid ist mit einem Hinweis auf die Beschwerde nach § 111 StG zu versehen.
> 4. **Mahnfristen** sind nicht erstreckbar (WL ZH 2025 S. 7).
> 5. **Wohnsitz in einem anderen Kanton:** Der Fristerstreckungsentscheid des Wohnsitzkantons gilt auch für ZH. Er muss dem Gemeindesteueramt aber vor Ablauf der Zürcher Frist mitgeteilt werden (WL ZH 2025 S. 7; ZStB `…__c0023`).
> 
> ## Hinweise für heute
> - **Gesuch rechtzeitig gestellt:** Die Erstreckung läuft bis längstens 30. November 2026. Das sind noch rund drei Wochen. Wer mehr Zeit braucht, muss ausserordentliche Gründe glaubhaft machen.
> - **Kein Gesuch gestellt:** Eine Erstreckung ist nicht mehr möglich. Möglich bleiben die Wiederherstellung der Frist (Zuständigkeit: Gemeindesteueramt) und eine Mahnung. Die Wiederherstellung setzt voraus, dass der Steuerpflichtige einen erheblichen Verhinderungsgrund nachweist, zum Beispiel Krankheit oder Landesabwesenheit. Er muss die Steuererklärung innert 30 Tagen nach Wegfall des Hindernisses nachholen (Art. 124 Abs. 4 DBG; § 15 StV laut ZStB 132.1).
> - **Folgen bei Nichteinreichung trotz Mahnung:** Beim Bund droht eine Busse bis CHF 1 000, in schweren Fällen oder bei Rückfall bis CHF 10 000 (Art. 174 DBG). Die kantonale Busse (StG ZH) ist im Wiki nicht erfasst.
> 
> ## Offene Punkte
> - Die Kosten einer Fristerstreckung nennen die Quellen nicht.
> - Für ZH 2025 nicht geprüft: Die Sonderregel «von Amtes wegen bis 30. September» für im Kanton wohnhafte Selbständigerwerbende und Ausserkantonale steht in ZStB 132.1 (`zh-zstb-132-1__c0023`).
> - Bei unterjähriger Steuerpflicht (Wegzug ins Ausland, Tod) gilt eine andere Frist: 30 Tage ab Zustellung der Formulare.
> 
> Die fachliche Beurteilung im Einzelfall bleibt bei SB/ML.

## b07

**Frage:** Wir sind eine Treuhandfirma und brauchen für Mandanten im Kanton Thurgau (Steuerperiode 2025, natürliche Personen) eine Fristerstreckung. Bei welcher Stelle ist das Gesuch einzureichen und bis wann kann die Frist längstens erstreckt werden?

**Soll (Referenz):** TG: Gesuch beim Gemeindesteueramt, das darüber entscheidet. Erstmals eingereichte Gesuche werden grundsätzlich bis längstens 30. September des Deklarationsjahres (2026) gutgeheissen; zusätzliche Gesuche in begründeten Fällen bis 30. November. Treuhänder/Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen, können für ihre Mandanten ein Gesuch längstens bis 31. Dezember des Deklarationsjahres beantragen. Arbeitsüberlastung ist kein Grund.

**Antwort des Agenten** (46.6 s · Tools: 12 Aufrufe read, read, memory_search):

> Ich habe die TG-Praxis StP 155 Nr. 2 und § 39b StV gelesen. Jetzt prüfe ich noch kurz die Wegleitung TG 2025 zur Zuständigkeit, dann antworte ich.
> 
> **Kurzantwort:** Das Gesuch geht an das **Gemeindesteueramt** der Wohnsitzgemeinde. Als gewerbsmässiger Treuhänder können Sie die Frist für Ihre Mandanten **längstens bis zum 31. Dezember 2026** erstrecken lassen.
> 
> Die Steuerperiode 2025 wird im Jahr 2026 deklariert, daher ist das «Deklarationsjahr» 2026.
> 
> **Zuständige Stelle**
> - Das Gesuch ist dem Gemeindesteueramt einzureichen, und dieses entscheidet auch darüber ([StP 155 Nr. 2, Ziff. 1](steuerwiki/chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md)).
> - Bei ausserkantonalen Steuerpflichtigen ist es die Liegenschafts- bzw. Betriebsstättengemeinde.
> - Die Wegleitung TG 2025 verlangt ein rechtzeitiges, schriftliches und begründetes Gesuch ([WL TG 2025 S. 7](steuerwiki/chunks/tg/2025/tg-wl-2025/tg-wl-2025__c0023.md)).
> - Die Steuerverwaltung Thurgau ist nur für juristische Personen zuständig.
> - Der Entscheid geht schriftlich an den Vertreter, wenn dieser das Gesuch gestellt hat ([StP 155 Nr. 2, Ziff. 3](steuerwiki/sources/tg/dauernd/tg-stp-155-2.md)).
> 
> **Wie lange**
> 
> | Gesuch | Längstens bis | Quelle |
> |---|---|---|
> | Erstgesuch, natürliche Personen | 30. September 2026 | [c0001](steuerwiki/chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md) |
> | Weitere Gesuche, nur in begründeten Fällen | 30. November 2026 | [c0001](steuerwiki/chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0001.md) |
> | Treuhänder/Steuerberater für ihre Mandanten | **31. Dezember 2026** | [c0002](steuerwiki/chunks/tg/dauernd/tg-stp-155-2/tg-stp-155-2__c0002.md) |
> 
> - **Treuhänder:** Die Regel gilt für Treuhänder und Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen.
> - **Über den 31. Dezember hinaus:** Für natürliche Personen nennt die Praxis keinen weiteren Spielraum. Über den 30. November hinausgehende Gesuche werden abgewiesen, ausser es werden ausserordentliche Gründe glaubhaft gemacht.
> - **Kein Grund:** Arbeitsüberlastung sowie starke berufliche Inanspruchnahme des Vertreters oder fehlende Unterlagen genügen nicht.
> 
> **Kosten:** Die erstmalige Fristerstreckung ist gebührenfrei. Für jedes weitere Gesuch erhebt die Steuerverwaltung eine Kanzleigebühr von Fr. 30 ([§ 39b Abs. 2–3 StV TG](steuerwiki/chunks/tg/2025/tg-stv/tg-stv__par-39b.md)). Ab der zweiten Mahnung kommen Fr. 50 Mahngebühr dazu (Abs. 4). Die Themenseite im Wiki sagt zur Gebühr bei natürlichen Personen «nicht genannt». Das ist überholt, denn § 39b StV regelt sie.
> 
> **Zum Vorgehen**
> - Bis heute (9. November 2026) bleiben nur noch rund sieben Wochen.
> - Reichen Sie das Gesuch vor Ablauf der laufenden Frist ein. Abgelaufene Fristen lassen sich nicht mehr erstrecken.
> - Wird die Frist ungenutzt überschritten, folgt eine Mahnung mit neuer Frist. Danach droht eine Ermessensveranlagung und eine Busse ([StP 155 Nr. 2, Ziff. 4](steuerwiki/sources/tg/dauernd/tg-stp-155-2.md)).
> - Ein verweigertes Gesuch lässt sich nicht selbständig anfechten.
> 
> **Offen und Status**
> - Die Praxis ist seit 05.01.2026 unverändert. Sie gilt laut Wiki für die Steuerjahre 2025 und 2026 und ist als Praxisquelle (Steuerpraxis TG) ein amtlicher Text. Die Wiki-Themenseite hat den Status «Entwurf».
> - Ob einzelne Gemeindesteuerämter bei Sammelgesuchen eigene Formulare oder Portale verlangen, steht nicht in den Quellen. Das müssten Sie beim jeweiligen Amt klären.
> - Die fachliche Beurteilung bleibt bei Ihnen.

## b08

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Auf welchem Formular wird der Abzug für Versicherungsprämien und Sparzinsen berechnet und in welche Ziffer der Steuererklärung wird das Ergebnis übertragen?

**Soll (Referenz):** AR 2025: Berechnung auf Formular 6 (A: bezahlte Prämien/Zinsen, B: Maximalabzug, C: Abzug = niedrigerer Betrag von A und B). Der Betrag C wird auf Seite 3 der Steuererklärung in Ziffer 14 übertragen.

**Antwort des Agenten** (35.2 s · Tools: 6 Aufrufe read):

> **Kanton AR, Steuerjahr 2025**
> 
> - **Formular:** Der Abzug wird auf dem **Formular 6 «Versicherungsprämien und Sparzinsen»** berechnet.
> - **Zielziffer:** Das Ergebnis kommt in **Ziffer 14** der Steuererklärung (Seite 3). Das ist im Formular als Code 600 geführt.
> 
> **Berechnung auf Formular 6**
> - **Teil A:** Total der bezahlten Prämien und Sparzinsen. Dazu zählen Kranken- (brutto), Unfall- (ohne NBUV), Lebens- und Rentenversicherung sowie die Sparzinsen aus dem Wertschriftenverzeichnis (Formular 2). Erhaltene Prämienverbilligungen (IPV) werden abgezogen. Mobiliar-, Motorfahrzeug-, Haftpflicht- und andere Sachversicherungen gehören nicht hinein.
> - **Teil B:** Maximalabzug. Er beträgt Fr. 5'400 für gemeinsam Steuerpflichtige oder Fr. 2'700 für Alleinstehende. Dazu kommen Fr. 1'000 je Kind, für das der Kinderabzug nach Ziff. 23.1, 23.2 oder 23.3 beansprucht werden kann.
> - **Teil C:** Zulässiger Abzug ist der **niedrigere Betrag aus A und B**. Er wird nach Ziff. 14 übertragen.
> 
> **Kanton und Bund**
> - Formular 6 AR rechnet nur den Maximalabzug für die Staats- und Gemeindesteuer.
> - Die direkte Bundessteuer hat tiefere Limiten: Fr. 3'700 für Ehepaare, Fr. 1'800 für übrige Steuerpflichtige und Fr. 700 je Kind. Sie stehen in Art. 33 DBG.
> - Auf Formular 6 AR ist keine eigene Bundesspalte vorhanden. Die Bundeslimiten kommen aus dem DBG, nicht aus einer AR-Quelle.
> 
> **Fundstellen**
> - Formular 6 AR 2025, S. 1, Teile B und C: `chunks/ar/2025/ar-form-06-2025/ar-form-06-2025__c0002.md`. Teil A steht in `…__c0001.md`.
> - Wegleitung AR 2025, Ziff. 14, S. 15: `chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0085.md`.
> - Betragsrahmen: Art. 35 lit. g StG AR, `chunks/ar/2025/ar-stg/ar-stg__art-35-t2.md`.
> - Bundeslimiten: `chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t2.md`.
> 
> **Status:** 🟡 extrahiert. Das Hauptformular 1 AR ist nicht online. Die Ziffer 14 stützt sich auf die Formularverweise in Formular 6 und in der Wegleitung. Die Zuordnungsseite stützt sich für Ziffern und Codes auf die Formular-Miniaturen der Wegleitung. Die fachliche Beurteilung bleibt bei der Fachperson.

## b09

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wo und wie ist ein Gesuch um Fristverlängerung für die Steuererklärung einer natürlichen Person zu stellen und bis wann?

**Soll (Referenz):** SG 2025: Das Gesuch ist vor Ablauf der Einreichefrist (Datum auf Seite 1 der Steuererklärung) zu stellen, vorzugsweise elektronisch unter www.steuern.sg.ch (mit Registernummer und Geburtsdatum); sonst schriftlich an das Gemeindesteueramt. Es kann eine angemessene Fristverlängerung gewährt werden.

**Antwort des Agenten** (37.9 s · Tools: 10 Aufrufe read, ls):

> Ich lese die Belegstellen im Original-Chunk nach.
> 
> **Kurzantwort (SG, Steuerjahr 2025):** Das Gesuch geht an das Gemeindesteueramt. Am einfachsten stellen Sie es elektronisch unter www.steuern.sg.ch, sonst schriftlich. Es muss vor Ablauf der Einreichefrist gestellt werden. Das konkrete Datum steht nicht im Wiki, sondern auf Seite 1 der Steuererklärung.
> 
> **Wo und wie**
> - **Elektronisch (empfohlen):** über die eFristverlängerung auf steuern.sg.ch. Sie brauchen die **Register-Nr.** und das **Geburtsdatum**, beide stehen auf der persönlichen Steuererklärung. Das Gesuch wird interaktiv bewilligt oder abgelehnt. ([WL SG 2025 S. 8](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0018.md); [SG Fristverlängerung, Privatpersonen](steuerwiki/chunks/sg/dauernd/sg-info-fristverlaengerung/sg-info-fristverlaengerung__c0002.md); [eFristverlängerung](steuerwiki/chunks/sg/dauernd/sg-info-fristverlaengerung/sg-info-fristverlaengerung__c0003.md))
> - **Nicht elektronisch:** schriftlich an das Gemeindesteueramt ([WL SG 2025 S. 8](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0018.md)).
> 
> **Bis wann**
> - Die Wegleitung verlangt das Gesuch «vor Ablauf der Einreichefrist». Dann kann «eine angemessene Fristverlängerung» gewährt werden ([WL SG 2025 S. 8](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0018.md)).
> - Der Einreichetermin selbst steht «gemäss Seite 1 der Steuererklärung». Ein generelles Datum nennen die Quellen im Wiki nicht.
> - Art. 168 Abs. 2 StG SG verlangt nur «fristgemäss» einzureichen ([Art. 168 StG SG](steuerwiki/chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-168.md)).
> - Heute ist der 09.11.2026. Ist der Termin auf der Steuererklärung 2025 bereits verstrichen, geht ein Gesuch nach den Quellen nicht mehr. Dann bleibt nur die Wiederherstellung wegen entschuldbaren Versäumnisses. Das Wiki belegt dafür nur Art. 124 Abs. 4 DBG, also die Bundesebene. Eine SG-Regel dazu habe ich nicht geprüft.
> 
> **Bedingung**
> - Die Fristverlängerung wird nur gewährt, wenn die fälligen Steuerrechnungen bezahlt sind ([SG Fristverlängerung, Privatpersonen](steuerwiki/chunks/sg/dauernd/sg-info-fristverlaengerung/sg-info-fristverlaengerung__c0002.md)).
> 
> **Nicht im Wiki, bitte beim Mandat prüfen**
> - Wie lange die Verlängerung dauert.
> - Ob sie etwas kostet.
> - Ob es für Treuhänder eine Sonderregel gibt, etwa Sammelgesuche oder eine Maximalfrist. Die Quellen nennen keine.
> - Der konkrete Einreichetermin 2025.
> 
> Die Quellen gelten für Kantons- und Gemeindesteuern wie für die direkte Bundessteuer, weil die kantonale Steuererklärung beide abdeckt ([Art. 124 DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-124.md)). Das Gesuch läuft also nur über den Kanton. Beim Bund gilt nach Art. 119 Abs. 2 DBG sinngemäss dasselbe: behördlich angesetzte Fristen werden bei zureichenden Gründen und rechtzeitigem Gesuch erstreckt.
> 
> Status: Der Wert `verfahren.fristerstreckung` ist ☑️ agent-geprüft, nicht von einer Fachperson verifiziert. Die fachliche Beurteilung liegt bei SB/ML.

## b10

**Frage:** Ehepaar im Kanton St.Gallen, Steuerjahr 2025, zwei Kinder mit Kinderabzug, keine Beiträge an die 2. Säule oder Säule 3a bei beiden Partnern. Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Kantons-/Gemeindesteuern und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2025 Kanton: Fr. 6'800 + zusätzlich ohne 2. Säule/3a bis Fr. 1'100 + 2 x bis Fr. 1'100 für die Kinder = Fr. 10'100. Bund: Fr. 3'700 + zusätzlich bis Fr. 1'850 (= Fr. 5'550) + 2 x Fr. 700 = Fr. 6'950. (Voraussetzung für den Zusatzabzug muss bei beiden Partnern erfüllt sein.)

**Antwort des Agenten** (43.9 s · Tools: 9 Aufrufe read):

> **Ergebnis (Steuerjahr 2025, Ehepaar in ungetrennter Ehe, 2 Kinder mit Kinderabzug, bei beiden Partnern keine Beiträge an die 2. Säule oder Säule 3a):**
> 
> | Ebene | Grundbetrag Ehepaar | Erhöhung ohne 2. Säule/3a | 2 Kinder | **Maximum** |
> |---|---|---|---|---|
> | **SG Staats-/Gemeindesteuer** | CHF 6'800 | + CHF 1'100 | 2 × CHF 1'100 = 2'200 | **CHF 10'100** |
> | **Direkte Bundessteuer** | CHF 3'700 | + die Hälfte (= CHF 1'850), also 5'550 | 2 × CHF 700 = 1'400 | **CHF 6'950** |
> 
> Das sind Höchstbeträge. Abziehbar ist der niedrigere Betrag aus den effektiv bezahlten Prämien und Sparzinsen und dem Maximum. Bei den Prämien ist die Prämienverbilligung bereits abgezogen. Auf dem SG-Formular 6 ist das «der niedrigere Betrag von (A) und (B)».
> 
> **Kanton SG**
> - Der Grundbetrag von CHF 6'800 und die Erhöhung um CHF 1'100 stehen in Art. 45 Abs. 1 lit. g StG SG. Der Kinderzuschlag von CHF 1'100 gilt «für jedes Kind, für das der Steuerpflichtige einen Kinderabzug geltend machen kann» (^[sg-stg-2025__art-45-t2]).
> - Die Erhöhung um CHF 1'100 gibt es nur, wenn «keine Beiträge nach Bst. d und e» abgezogen werden. Bei gemeinsam Besteuerten müssen die Voraussetzungen bei beiden Personen erfüllt sein (Formular 6 SG 2025 S. 1, ^[sg-form-6-2025__c0002]; WL SG 2025 S. 4, ^[sg-wl-2025__c0003]). Das ist hier der Fall.
> - Der Wert 7'900 für das Ehepaar ohne Vorsorge ist im Wiki als Summe 6'800 + 1'100 berechnet. Das Gesetz nennt ihn nicht als eigene Zahl.
> - Die Wegleitung formuliert Erhöhung und Kinderzuschlag als «bis Fr. 1'100». Das sind Obergrenzen, und die 10'100 sind ein Maximum.
> - Status ☑️ agent-geprüft.
> 
> **Direkte Bundessteuer**
> - Der Grundbetrag beträgt CHF 3'700 (Art. 33 Abs. 1 lit. g DBG, ^[bund-dbg-2025__art-33-t2]).
> - Art. 33 Abs. 1bis DBG: Der Abzug erhöht sich «um die Hälfte für Steuerpflichtige ohne Beiträge nach Absatz 1 Buchstaben d und e». Dazu kommen «700 Franken für jedes Kind … [mit] Abzug nach Artikel 35 Absatz 1 Buchstabe a oder b» (^[bund-dbg-2025__art-33-t5]). Die Hälfte von 3'700 ergibt 5'550. Das stimmt mit dem Wiki-Wert «Ehepaar ohne 2. Säule/3a CHF 5'550» überein (Eckwerte Bund 2025).
> - Die Kinderzuschläge von 700 werden nicht um die Hälfte erhöht. Die Erhöhung betrifft nur den Grundbetrag. Das ist meine Lesart des Gesetzeswortlauts. Ein Beispiel dazu fand ich im Wiki nicht.
> - Status ☑️ agent-geprüft.
> 
> **Hinweise**
> - Den Bundesabzug auf dem SG-Formular zu ermitteln ist Sache der Veranlagungsbehörde. Das SG-Formular 6 rechnet nur den Maximalbetrag für Staats- und Gemeindesteuer. Die Bundeslimiten stehen in der Wegleitung, die die Bundesbeträge nennt (Verweis im Wiki-Thema auf WL SG 2025 S. 4).
> - Der Kinderzuschlag setzt voraus, dass für das Kind tatsächlich der Kinderabzug beansprucht wird (SG Ziff. 23.1/23.2, Bund Art. 35 Abs. 1 lit. a DBG). Bei getrennten Eltern mit halbem Kinderabzug fällt er entsprechend tiefer aus. Das trifft bei einem Ehepaar mit gemeinsamen Kindern nicht zu.
> - Die fachliche Beurteilung bleibt bei SB/ML.
> 
> Weitere Details: `steuerwiki/wiki/themen/versicherungspraemien.md`.

## b11

**Frage:** Arbeitnehmer im Kanton Thurgau, Steuerjahr 2026, Arbeitsweg mit ÖV-Jahresabonnement, effektive Kosten Fr. 6'400. Welcher Fahrkostenabzug ist bei den Staats-/Gemeindesteuern und welcher bei der direkten Bundessteuer zulässig?

**Soll (Referenz):** TG 2026: Kanton gesamthaft max. Fr. 6'000, deshalb Abzug Fr. 6'000 (effektive Kosten Fr. 6'400 werden gekürzt). Bund max. Fr. 3'300, deshalb Abzug Fr. 3'300.

**Antwort des Agenten** (34.4 s · Tools: 9 Aufrufe read, read):

> **Steuerjahr 2026, Thurgau, ÖV-Jahresabo mit effektiven Kosten von Fr. 6'400**
> 
> | Ebene | Maximum | Zulässiger Abzug |
> |---|---|---|
> | Staats- und Gemeindesteuer TG | Fr. 6'000 | **Fr. 6'000** (die Fr. 400 über dem Maximum sind nicht abziehbar) |
> | Direkte Bundessteuer | Fr. 3'300 | **Fr. 3'300** (Fr. 3'100 nicht abziehbar) |
> 
> **Fundstellen**
> - **Kanton:** Die Wegleitung TG 2026, S. 37–38, nennt für die Staats- und Gemeindesteuern «gesamthaft maximal Fr. 6 000» und für den Bund «gesamthaft maximal Fr. 3'300» (`tg-wl-2026__c0176`). Das Wiki führt den Wert als ☑️ agent-geprüft (`berufskosten.fahrkosten.max`).
> - **Bund:** Art. 26 Abs. 1 lit. a DBG (Fassung 2026) erlaubt «die notwendigen Kosten bis zu einem Maximalbetrag von 3300 Franken» (`bund-dbg-2026__art-26`, ☑️).
> 
> **Praktische Hinweise**
> - Im Formular 4.2 stehen die Beträge in zwei Spalten (Staat/Bund). Das ÖV-Abo gehört in Ziff. 2.1 (Code 206 für den Staat, 246 für den Bund). Das Total in Ziff. 2.5 trägt die Codes 213 und 253 und wird je Ebene auf Fr. 6'000 bzw. Fr. 3'300 begrenzt (Quelle: `wiki/themen/fahrkosten.md`, Formularzuordnung TG 2025/2026).
> - Voraussetzung ist, dass im Lohnausweis Feld F nicht angekreuzt ist. Ist es angekreuzt (unentgeltliche Beförderung), entfällt der Abzug ganz (WL TG 2026, `c0175`).
> - Die Maxima gelten pro Person und für alle Fahrkosten zusammen, auch für Wochenaufenthalt und Nebenerwerb. Bei Teilzeit oder unterjähriger Tätigkeit werden sie nicht gekürzt (WL TG 2026, `c0176`; Wiki-Thema Fahrkosten).
> - Ich habe die Fr. 400 / Fr. 3'100 selbst aus den Maxima und Ihren Fr. 6'400 gerechnet. Sie stehen nicht so in einer Quelle.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson (SB/ML).

## b12

**Frage:** Ehepaar im Kanton Zürich, Steuerjahr 2026, nachgewiesene Kinderdrittbetreuungskosten: Kind A (5 Jahre) Fr. 30'000, Kind B (8 Jahre) Fr. 12'000. Wie hoch ist der Abzug bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2026: Maximum pro Kind Staat Fr. 25'300, Bund Fr. 25'800 (Kinder unter 14). Staat: 25'300 + 12'000 = Fr. 37'300. Bund: 25'800 + 12'000 = Fr. 37'800. (Zum Vergleich 2025: Staat max. Fr. 25'000.)

**Antwort des Agenten** (36.7 s · Tools: 9 Aufrufe read):

> **Abzug für Kinderdrittbetreuung, Kanton ZH, Steuerjahr 2026**
> 
> | | Kind A (5 J.) | Kind B (8 J.) | Total |
> |---|---|---|---|
> | Nachgewiesene Kosten | 30'000 | 12'000 | 42'000 |
> | **Staats-/Gemeindesteuer** (Höchstbetrag 25'300 pro Kind) | 25'300 (gekürzt) | 12'000 | **37'300** |
> | **Direkte Bundessteuer** (Höchstbetrag 25'800 pro Kind) | 25'800 (gekürzt) | 12'000 | **37'800** |
> 
> Die Höchstbeträge gelten pro Kind und werden nicht über die Kinder hinweg zusammengezählt. Bei Kind A greift deshalb die Kürzung (Staat –4'700, Bund –4'200). Kind B liegt unter beiden Höchstbeträgen und wird voll abgezogen.
> 
> **Fundstellen (alle Steuerjahr 2026)**
> - **Staatssteuer:** § 31 Abs. 1 lit. j StG ZH nennt «höchstens Fr. 25 300» pro Kind unter 14 Jahren ([zh-stg-2026__par-31-t3](steuerwiki/chunks/zh/2026/zh-stg-2026/zh-stg-2026__par-31-t3.md)). Das Wegleitungs-Chunk bestätigt den Wert ([WL ZH 2026 UJ S. 17, Ziff. 16.6](steuerwiki/chunks/zh/2026/zh-wl-2026-uj/zh-wl-2026-uj__c0105.md)).
> - **Bundessteuer:** Art. 33 Abs. 3 DBG nennt «höchstens 25 800 Franken» ([bund-dbg-2026__art-33-t7](steuerwiki/chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-33-t7.md)). Das Rundschreiben bestätigt den Wert ([RS 2-215 S. 2](steuerwiki/chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0007.md)).
> - **Status:** ☑️ agent-geprüft. Die Fachperson hat die Werte noch nicht verifiziert.
> 
> **Formular:** Ziff. 16.6, Code 376. Dort stehen beide Höchstbeträge im Formularkopf, die Eingabe erfolgt nur einmal. Der Abzug wird im Formular ZH 2026 pro Kind auf die jeweilige Limite gekürzt. Der Betrag der Kita-Rechnungen ist ohne Verpflegung einzutragen.
> 
> **Vorbehalte**
> - **Voraussetzungen:** Der Abzug gilt nur, wenn die Kosten in direktem kausalem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit stehen. Zudem müssen die Kinder im gleichen Haushalt leben. Bei einem Ehepaar sollten beide erwerbstätig oder in Ausbildung sein (bzw. erwerbsunfähig). Das wurde hier angenommen und nicht geprüft.
> - **Verpflegung:** Lebenshaltungskosten wie der Mittagstisch sind nicht abziehbar. Falls die 30'000 und 12'000 darin enthaltene Verpflegung einschliessen, sind sie entsprechend zu bereinigen.
> - **Wegleitung:** Die reguläre Wegleitung ZH 2026 ist noch nicht publiziert (Stand 09.11.2026). Das Wiki stützt sich auf die Fassung für unterjährige Steuerpflicht (UJ). Die Beträge selbst sind durch Gesetz und Rundschreiben belegt.
> - **Alter der Kinder:** Beide Kinder sind unter 14 Jahren und damit abzugsberechtigt.

## b13

**Frage:** Ein Mitglied der Milizfeuerwehr erhält für die Erfüllung von Kernaufgaben (Übungen, Pikettdienst, Ernstfalleinsätze) Sold. Bis zu welchem Betrag ist der Feuerwehrsold bei der direkten Bundessteuer steuerfrei, im Steuerjahr 2025 und im Steuerjahr 2026?

**Soll (Referenz):** Bund: 2025 steuerfrei bis maximal Fr. 5'300; 2026 steuerfrei bis maximal Fr. 5'400 (Wert hat sich geändert, nicht übertragen). Der gesamte Sold ist auf dem Lohnausweis zu deklarieren; der steuerfreie Betrag wird auf Formular 9 Berufskosten Ziffer 8 abgezogen.

**Antwort des Agenten** (32.6 s · Tools: 4 Aufrufe read, exec):

> Ich prüfe die Chunks im Original.
> 
> Bei der direkten Bundessteuer ist der Sold der Milizfeuerwehrleute für Kernaufgaben jährlich bis zu diesen Beträgen steuerfrei:
> 
> | Steuerjahr | Steuerfrei bis (pro Jahr) | Fundstelle |
> |---|---|---|
> | **2025** | **CHF 5'300** | Art. 24 lit. fbis DBG (Fassung 2025), Chunk `bund-dbg-2025__art-24-t2`. Wörtlich: «bis zum Betrag von jährlich 5300 Franken». Gleicher Wert in RS 2-210 S. 2, Chunk `bund-rs-2-210__c0006`. |
> | **2026** | **CHF 5'400** | Art. 24 lit. fbis DBG (Fassung 2026), Chunk `bund-dbg-2026__art-24-t2`. Wörtlich: «bis zum Betrag von jährlich 5400 Franken». Zusätzlich Art. 4 VKP. |
> 
> **Umfang:** Steuerfrei ist der Sold für die Kernaufgaben der Feuerwehr: Übungen, Pikettdienste, Kurse, Inspektionen und Ernstfalleinsätze (Rettung, Brandbekämpfung, allgemeine Schadenwehr, Elementarschadenbewältigung und dergleichen). Nicht steuerfrei sind:
> - Pauschalzulagen für Kader
> - Funktionszulagen
> - Entschädigungen für administrative Arbeiten
> - Entschädigungen für Dienstleistungen, welche die Feuerwehr freiwillig erbringt
> 
> Das Wiki hält für 2026 fest, dass der gesamte Sold im Lohnausweis zu deklarieren ist.
> 
> **Status:** Beide Werte sind ☑️ agent-geprüft, nicht von einer Fachperson verifiziert. Der Gesetzeswortlaut stimmt aber mit dem Wiki-Wert überein.
> 
> **Hinweis:** Das gilt nur für den Bund (DBG). Die Staats- und Gemeindesteuer richtet sich nach dem Kanton und weicht teils deutlich ab. Im Wiki steht für 2025 AR 5'000, SG 5'300, TG 5'000 und ZH 8'300. Für 2026 steht dort SG 5'300 und ZH 8'400. AR und TG sind für 2026 mit dem Wert von 2025 geführt. Soll ich das für einen bestimmten Kanton genauer prüfen?

## b14

**Frage:** Ein Mandant wohnt am 31.12.2026 im Kanton Luzern und pendelt mit dem Auto zur Arbeit. Welcher Fahrkostenabzug gilt für die Luzerner Staats- und Gemeindesteuern 2026 und für die direkte Bundessteuer?

**Soll (Referenz):** Luzern ist im Wiki nicht abgedeckt (nur Bund, AR, SG, TG, ZH): kein Wert für die Luzerner Staats-/Gemeindesteuer nennen, auf kantonale Wegleitung verweisen. Für die direkte Bundessteuer 2026 gilt max. Fr. 3'300 (Wegleitung Bund 2026).

**Antwort des Agenten** (34.9 s · Tools: 8 Aufrufe read, read, memory_search):

> Luzern ist nicht abgedeckt. Für den Bund schaue ich in die Eckwerte 2026.
> 
> **Kanton Luzern: nicht im Wiki, daher keine Antwort.**
> Das Steuer-Wiki deckt nur Bund, AR, SG, TG und ZH ab (`quick/index.md`). Ich nenne keinen Luzerner Wert für die Staats- und Gemeindesteuern 2026 und übertrage auch keinen aus einem anderen Kanton. Die Regel dafür müssen Sie direkt im Luzerner Steuergesetz (StG LU) und in der Wegleitung zur Steuererklärung 2026 der Dienststelle Steuern LU nachschlagen. Ob LU wie andere Kantone eine eigene Obergrenze oder Autopauschale kennt, kann ich aus dem Wiki nicht sagen.
> 
> **Direkte Bundessteuer 2026 (Wiki-Stand: ☑️ agent-geprüft)**
> 
> | Punkt | Regel | Fundstelle |
> |---|---|---|
> | Maximalabzug Fahrkosten Wohn-/Arbeitsstätte | CHF 3'300 pro Jahr und Person. Abziehbar sind die «notwendigen Kosten bis zu einem Maximalbetrag von 3300 Franken». | DBG Art. 26 Abs. 1 lit. a, `bund-dbg-2026__art-26`; Eckwerte Bund 2026, `berufskosten.fahrkosten.max` |
> | Privatauto | CHF 0.75 pro Fahrkilometer, neu ab 2026 (2025: CHF 0.70). Das gilt nur, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist. Der Gesamtabzug bleibt auf CHF 3'300 begrenzt. | Art. 5 Abs. 2 lit. b BKV und Anhang Ziff. 2; RS 2-215 S. 1 (`bund-rs-2-215__c0004`); ESTV-MM 11.09.2025 (`bund-mm-2025-09-11-kalte-progression-2026__c0004`) |
> | Arbeitstage | Der Bund kennt keine Arbeitstage-Basis. Es gelten die tatsächlichen Kosten bis CHF 3'300. | Eckwerte Bund 2026 |
> 
> **Was Sie klären sollten**
> - Ob für den Mandanten ein öffentliches Verkehrsmittel zumutbar wäre. Wenn ja, wären nur dessen Kosten abziehbar (z. B. ein ÖV-Abo), nicht die Autokilometer.
> - Bei Autokosten über CHF 3'300 gilt für die direkte Bundessteuer trotzdem nur CHF 3'300. Der kantonale Abzug kann höher oder tiefer sein und muss separat aus den Luzerner Quellen ermittelt werden. In der Steuererklärung werden Kanton und Bund meist unterschiedlich gedeckelt.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson. Den Luzerner Wert sollten Sie aus den Primärquellen belegen, bevor Sie ihn ausfüllen.

