# OpenClaw-Testlauf: blindtest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuermem` · Fragen: 14 · Lauf: 2026-11-09 08:09
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## b01

**Frage:** Ehepaar in rechtlich und tatsächlich ungetrennter Ehe, weder Beiträge an die 2. Säule noch an die Säule 3a, Kanton ZH, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Zinsen von Sparkapitalien bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2025: Staatssteuer höchstens CHF 8'700 (Grundabzug CHF 5'800, ohne Beiträge an 2. Säule/3a um die Hälfte erhöht). Direkte Bundessteuer 2025: höchstens CHF 5'550 (Grundabzug CHF 3'700, um die Hälfte erhöht).

**Antwort des Agenten** (34.1 s · Tools: 8 Aufrufe read):

> **Steuerjahr 2025, Kanton ZH, Ehepaar in rechtlich und tatsächlich ungetrennter Ehe, ohne Beiträge an die 2. Säule und die Säule 3a (weder durch die Steuerpflichtigen noch durch den Arbeitgeber):**
> 
> | Ebene | Maximaler Abzug (Ziff. 15, Code 270) | Fundstelle |
> |---|---|---|
> | **Staats-/Gemeindesteuer ZH** | **CHF 8'700** (Grundbetrag CHF 5'800, um die Hälfte erhöht) | [Formular 365 ZH 2025, Teil B Ziff. 1 (Code 611)](../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md); [WL ZH 2025 S. 15](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0086.md); § 31 Abs. 1 lit. g StG ZH |
> | **Direkte Bundessteuer** | **CHF 5'550** (Grundbetrag CHF 3'700, um die Hälfte erhöht) | [Formular 365 ZH 2025, Teil B Ziff. 1](../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md); [Art. 33 Abs. 1bis lit. a DBG](../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t5.md); [WL ZH 2025 S. 15](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0086.md) |
> 
> Status: ☑️ agent-geprüft. Die Werte stimmen in Gesetz, Formular 365 und Wegleitung überein. Die Fachperson hat sie noch nicht verifiziert.
> 
> **Hinweise zur Anwendung**
> - Der Abzug ist der **niedrigere** Betrag aus (A) den tatsächlich bezahlten Prämien und Sparzinsen, netto nach Prämienverbilligung, und (B) dem Maximalbetrag. Die CHF 8'700 bzw. 5'550 sind also nur eine Obergrenze (Formular 365 Teil C).
> - Für jedes Kind oder jede unterstützungsbedürftige Person mit Kinder- bzw. Unterstützungsabzug kommt ein Zuschlag dazu: CHF 1'300 bei der Staatssteuer und CHF 700 bei der Bundessteuer. Bei halbem Kinderabzug wird der Zuschlag halbiert (CHF 650 bzw. 350). In Ihrem Fall ohne Kinder entfällt er.
> - Die erhöhte Limite gilt nur, wenn **keine** Beiträge an die 2. Säule oder die Säule 3a geleistet wurden. Das schliesst auch Arbeitgeberbeiträge an die Pensionskasse ein (WL ZH 2025 S. 15). Das Wiki enthält dazu keinen Hinweis, wie es bei Ehepaaren zu behandeln ist, bei denen nur ein Partner Beiträge geleistet hat. Das habe ich nicht weiter geprüft. Wenn bei einem der beiden Beiträge anfallen, gelten die Grundbeträge CHF 5'800 und CHF 3'700.
> - NBUV-Prämien, die schon im Lohnausweis abgezogen sind, sowie Mobiliar-, Haftpflicht- und Motorfahrzeugversicherungen gehören nicht in die Aufstellung.

## b02

**Frage:** Wie hoch ist im Steuerjahr 2026 der Maximalabzug für Fahrkosten zwischen Wohn- und Arbeitsort im Kanton St.Gallen (Kantons- und Gemeindesteuern) und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2026: Kantons- und Gemeindesteuern max. Fr. 8'000; direkte Bundessteuer max. Fr. 3'300. Es ist ein Maximalabzug, keine Pauschale (bei Teilzeit/unterjährig nicht gekürzt).

**Antwort des Agenten** (40.8 s · Tools: 9 Aufrufe read, exec):

> Für das Steuerjahr 2026 gilt für die Fahrkosten zwischen Wohn- und Arbeitsstätte:
> 
> | Ebene | Maximalabzug pro Person | Fundstelle | Status |
> |---|---|---|---|
> | **Kantons- und Gemeindesteuern SG** | **CHF 8'000** | Art. 39 Abs. 1 lit. a StG SG (Fassung 2026): «bis zum Betrag von Fr. 8000.–» (`sg-stg-2026__art-39`) | ☑️ agent-geprüft |
> | **Direkte Bundessteuer** | **CHF 3'300** | Art. 26 Abs. 1 lit. a DBG (Fassung 2026): «Maximalbetrag von 3300 Franken» (`bund-dbg-2026__art-26`) | ☑️ agent-geprüft |
> 
> Die SG-Steuerverwaltung bestätigt beide Beträge in ihrer Tabelle der Maximalabzüge: Für 2026 stehen dort «Fr. 8'000.--» (Kantons- und Gemeindesteuern) und «Fr. 3'300.--» (direkte Bundessteuer) (StB 39 Nr. 3 Ziff. 3, S. 3–4, `sg-stb-39-3__c0011`).
> 
> **Wichtig bei der Anwendung (StB 39 Nr. 3 Ziff. 3):**
> - Es ist ein Maximalabzug, keine Pauschale. Bei unterjähriger Steuerpflicht, Aufnahme oder Aufgabe der Erwerbstätigkeit im Jahr und bei Teilzeit wird er nicht gekürzt.
> - Bei Haupt- und Nebenerwerb gilt die Begrenzung insgesamt.
> - Abziehbar sind nur die tatsächlich notwendigen Kosten, und zwar nur bis zu diesem Betrag. Bei Auto und Motorrad sind das CHF 0.75/km (SG: 220 Arbeitstage, `sg-stb-39-3__c0010`). Die Velo-Pauschale beträgt CHF 700. Ein ÖV-Abo wird mit den effektiven Kosten angesetzt.
> - Ein SG-Formular 4 setzt Kanton (8'000) und Bund (3'300) getrennt an. Der Kantonsbetrag ist also nicht automatisch der Bundesbetrag.
> 
> **Offener Punkt:** Die SG-Wegleitung 2026 ist noch nicht publiziert (Stand 09.11.2026). Die Beträge stützen sich auf das Gesetz 2026 und die Weisung StB 39 Nr. 3, nicht auf die Wegleitung. Die fachliche Beurteilung bleibt bei der Fachperson.

## b03

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Welchen Kinderabzug können Eltern für ein 3-jähriges, ein 10-jähriges und ein 16-jähriges (noch minderjähriges) Kind geltend machen?

**Soll (Referenz):** AR (Kantonssteuer) 2025, indexierte Beträge gemäss Anhang 1 StG (bestätigt durch WL AR 2025 Ziff. 23): 3-jähriges Kind (bis Vollendung des 4. Altersjahrs) Fr. 5'300; 10-jähriges Kind (nach Vollendung des 4. bis Vollendung des 15. Altersjahrs) Fr. 7'400; 16-jähriges Kind (nach Vollendung des 15. Altersjahrs bis Volljährigkeit) Fr. 11'600. Gleiche Beträge für volljährige Kinder in Ausbildung bis zum 26. Altersjahr. (Korrigiert nach Bewertung Lauf A: die ursprüngliche Referenz nannte die nicht indexierten Merkblatt-Beträge 5'000/7'000/11'000.)

**Antwort des Agenten** (48.4 s · Tools: 7 Aufrufe read, memory_search):

> **Kanton AR, Steuerjahr 2025:** Der Kinderabzug beträgt für die drei Kinder zusammen **CHF 24'300** bei Staats- und Gemeindesteuer und **CHF 20'400** bei der direkten Bundessteuer. Der Kinderabzug ist in AR nach Alter gestaffelt. Massgebend ist das Alter am 31.12.2025. Status der Werte: ☑️ agent-geprüft.
> 
> | Kind | Ziffer (Formular AR) | Kanton (Staats-/Gemeindesteuer) | Bund (DBG) |
> |---|---|---|---|
> | 3-jährig | 23.1 (bis zur Vollendung des 4. Altersjahrs) | CHF 5'300 | CHF 6'800 |
> | 10-jährig | 23.2 (nach Vollendung des 4. bis zur Vollendung des 15. Altersjahrs) | CHF 7'400 | CHF 6'800 |
> | 16-jährig, minderjährig | 23.3 (nach Vollendung des 15. Altersjahrs bis zur Volljährigkeit) | CHF 11'600 | CHF 6'800 |
> | **Total** | | **CHF 24'300** | **CHF 20'400** |
> 
> **Fundstellen**
> - **Kanton:** WL AR 2025 S. 2, Ziff. 23.1–23.3 (`ar-wl-2025__c0005`) und StG AR Anhang 1 (`ar-stg-anhang-kp__c0001`). Der Gesetzestext nennt unindexiert 5'000 und 7'000. Massgebend sind die indexierten Beträge per 1.1.2024 gemäss Anhang 1 und Wegleitung 2025.
> - **Bund:** Art. 35 Abs. 1 lit. a DBG 2025 (`bund-dbg-2025__art-35`): 6'800 für jedes minderjährige oder in Ausbildung stehende Kind, ohne Altersstaffelung.
> - Das AR-Formular hat keine separate Bundesspalte. Die Steuerverwaltung nimmt die Bundesabweichungen automatisch vor (WL AR 2025 S. 33, `ar-wl-2025__c0179`).
> 
> **Voraussetzungen**
> - Die Eltern müssen für den Unterhalt der Kinder aufkommen.
> - Hat ein Kind Einkünfte von mehr als CHF 18'000, gibt es keinen Abzug.
> - Wer für ein Kind Unterhaltsbeiträge nach Ziff. 12.2 abzieht, erhält dafür keinen Kinderabzug.
> - Bei getrennt besteuerten Eltern mit gemeinsamer Sorge und ohne Unterhaltsbeiträge wird der Abzug je zur Hälfte aufgeteilt.
> - Bei Kind 3 (16-jährig) kommen die Ausbildungsgrenzen der Ziff. 23.3 (Reinvermögen über CHF 250'000) erst bei Volljährigkeit zum Tragen. Die Quelle nennt sie in der Wegleitung (Detailkarte Ziff. 23.3), und ich habe sie nicht am Originaltext nachgeprüft.
> - Das Alter am 31.12.2025 bestimmt die Stufe. Ein Kind, das 2025 den 4. oder 15. Geburtstag feiert, rutscht deshalb je nach Geburtsdatum in die nächste Stufe. Für die Kinder in Ihrer Frage (3, 10 und 16 Jahre) ist die Zuordnung eindeutig, sofern diese Alter am 31.12.2025 gelten.
> 
> **Nicht Teil des Kinderabzugs, aber für diese Familie relevant**
> - **Vermögen (Ziff. 36.3):** zusätzlich CHF 25'000 je minderjähriges Kind, hier CHF 75'000 (WL AR 2025 S. 2, StG AR Art. 51).
> - **Versicherungsabzug:** Zuschlag von CHF 1'000 je Kind (StG AR Art. 35).
> - **Kinderdrittbetreuung (Kita, Tagesmutter):** bis CHF 25'000 je Kind, aber nur bis zum 14. Altersjahr. Das betrifft die beiden jüngeren Kinder, nicht das 16-jährige (StG AR Art. 35).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## b04

**Frage:** Alleinstehende Person ohne Kinder mit Beiträgen an die 2. Säule, Kanton Thurgau, Steuerjahr 2025: Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Staats-/Gemeindesteuern und bei der Bundessteuer?

**Soll (Referenz):** TG 2025: Staat max. Fr. 3'500, Bund max. Fr. 1'800 (ohne Beiträge an Säule 2/3a würde beim Bund Fr. 2'700 gelten). Betrag vor Abzug Prämienverbilligungen Krankenkassen.

**Antwort des Agenten** (40.6 s · Tools: 9 Aufrufe read):

> Für eine alleinstehende Person ohne Kinder, die Beiträge an die 2. Säule leistet, beträgt der maximale Abzug im Kanton Thurgau, Steuerjahr 2025:
> 
> | Ebene | Maximaler Abzug | Fundstelle |
> |---|---|---|
> | **Staats-/Gemeindesteuer TG** | **CHF 3'500** | § 34 Abs. 1 Ziff. 9 lit. b StG TG (`tg-stg__par-34-t3`); Formular 5.2 TG 2025, Teil B Ziff. 2 (`tg-form-05-2-2025__c0002`) |
> | **Direkte Bundessteuer** | **CHF 1'800** | Art. 33 Abs. 1 lit. g Ziff. 2 DBG (`bund-dbg-2025__art-33-t2`); Formular 5.2 TG 2025, Teil B Ziff. 2 |
> 
> Der Abzug ist der tiefere Betrag aus den tatsächlich bezahlten Prämien und Sparzinsen und diesem Maximum. Das Formular 5.2 rechnet Staat und Bund in getrennten Spalten (Teil C, Code 330, Übertrag in Ziff. 14 der Steuererklärung).
> 
> **Erhöhung ohne Vorsorgebeiträge:** Sie gilt hier nicht, weil Beiträge an die 2. Säule geleistet werden. Die höhere Limite von CHF 2'700 beim Bund gilt nur, wenn weder Beiträge an die Säule 2 noch an die Säule 3a geleistet wurden (Art. 33 Abs. 1bis lit. a DBG, `bund-dbg-2025__art-33-t5`). Im Kanton Thurgau gibt es diese Erhöhung nicht.
> 
> **Kinderzuschlag:** Er entfällt, weil keine Kinder oder unterstützungsbedürftigen Personen vorhanden sind. Sonst wären es +CHF 1'000 (Kanton) bzw. +CHF 700 (Bund) je Kind.
> 
> **Netto-Prämien:** Die Krankenkassenprämie ist netto nach Prämienverbilligung (IPV) einzusetzen. Zusätzlich sind die Krankentaggeldbeiträge gemäss Lohnausweis zu erfassen (Formular 5.2 TG 2025 S. 1, `tg-form-05-2-2025__c0001`). Prämien, die im Lohnausweis bereits abgezogen sind (NBUV), gehören nicht hierher.
> 
> **Status:** Die TG-Zeile in der Kompakt-Wegleitung (`quick/wegleitung-tg-2025.md`, Ziff. 14) ist ☑️ agent-geprüft. Die Beträge habe ich zusätzlich direkt in den zitierten Gesetzes- und Formular-Chunks nachgelesen, sie stimmen überein. Von einer Fachperson verifiziert (✅) ist der Eintrag nicht. Die fachliche Beurteilung bleibt bei SB/ML.

## b05

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wie hoch ist der Kinderabzug für ein noch nicht schulpflichtiges Kind und für ein Kind in Schule oder Ausbildung bei den Kantons-/Gemeindesteuern?

**Soll (Referenz):** SG 2025: noch nicht schulpflichtiges Kind Fr. 7'600 (Ziff. 23.1); Kind in Schule oder Ausbildung (auch volljährig) Fr. 10'800 (Ziff. 23.2).

**Antwort des Agenten** (44.2 s · Tools: 7 Aufrufe read, read, exec):

> **Kanton St. Gallen, Steuerjahr 2025 (Staats- und Gemeindesteuer)**
> 
> | Kind | Kinderabzug | Ziff. / Code (Formular 1) |
> |---|---|---|
> | Noch nicht schulpflichtig | **Fr. 7'600** je Kind | 23.1 / Code 252 |
> | In schulischer oder beruflicher Ausbildung | **Fr. 10'800** je Kind | 23.2 / Code 254 |
> 
> **Voraussetzungen** (Art. 48 Abs. 1 lit. a StG SG):
> - Du kommst für den Unterhalt zur Hauptsache auf.
> - Du machst für das Kind keinen Abzug für Unterhaltsbeiträge nach Art. 45 Abs. 1 lit. c geltend (Ziff. 12.2).
> - Der Abzug nach 23.1 gilt für Kinder unter deiner elterlichen Sorge oder Obhut.
> - Der Abzug nach 23.2 gilt für Kinder unter deiner Sorge oder Obhut und für volljährige Kinder in Ausbildung.
> - Es zählen die Verhältnisse am Ende der Steuerperiode, also am 31.12.2025. Bei nur teilweiser Steuerpflicht wird der Abzug anteilmässig gewährt (Abs. 2 und 3).
> - Der Kindergarten gehört zur Schulpflicht. Ein Kindergartenkind fällt deshalb unter 23.2 (Fr. 10'800).
> 
> **Zusätzlich für Kinder in Ausbildung (Ziff. 23.3, Code 256):** Es gibt bis zu weitere Fr. 13'700 für Ausbildungskosten, die du selbst trägst und die Fr. 3'200 übersteigen. Voraussetzung ist der Abzug nach 23.2. Die Berechnung lautet min(max(0; Kosten − Stipendien − 3'200); 13'700). Dieser Abzug gilt nur für den Kanton, nicht für den Bund.
> 
> **Abgrenzung zum Bund (DBG, nicht gefragt, zur Orientierung):** Die direkte Bundessteuer kennt keine Altersstufen. Sie gewährt Fr. 6'800 je Kind vom Einkommen und zusätzlich einen Abzug vom Steuerbetrag von max. Fr. 263 je Kind im gleichen Haushalt. Quelle: Wegleitung SG 2025, Ziff. 23.1/23.2, Eckwerte SG 2025.
> 
> **Fundstellen:**
> - [StG SG Art. 48 (Fassung 2025)](steuerwiki/chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-48.md)
> - Formular 1 SG 2025, S. 3 (`sg-form-1-2025__c0011`)
> - [Kompakt-Wegleitung SG 2025, Ziff. 23.1–23.3](steuerwiki/quick/wegleitung-sg-2025.md)
> - [Eckwerte SG 2025](steuerwiki/quick/werte-sg-2025.md)
> 
> **Status:** ☑️ agent-geprüft. Der Gesetzeswortlaut stimmt mit den Wiki-Werten überein. Eine Verifizierung durch die Fachperson (✅) steht noch aus.

## b06

**Frage:** Bis wann ist die Steuererklärung 2025 einer natürlichen Person im Kanton Zürich einzureichen, und wie ist vorzugehen, wenn die Frist nicht eingehalten werden kann?

**Soll (Referenz):** ZH, Steuerperiode 2025: Einreichung bis 31. März 2026 (online oder an das Scan-Center). Gesuch um Fristerstreckung ist vor Ablauf der Frist beim Gemeindesteueramt zu stellen. Mahnfristen sind nicht erstreckbar.

**Antwort des Agenten** (51.6 s · Tools: 6 Aufrufe read, exec):

> **Kanton Zürich, Steuerjahr 2025** (Staats-/Gemeindesteuer; die direkte Bundessteuer läuft über dieselbe Erklärung mit)
> 
> ## Einreichefrist
> - Die Steuererklärung 2025 ist **bis 31. März 2026** einzureichen. Quelle: [WL ZH 2025 S. 7](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0017.md). Die Praxis bestätigt dies: Frist ist der 31. März des der Steuerperiode folgenden Jahres, online oder beim Scan-Center ([ZStB 132.1 Ziff. G.I](steuerwiki/chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0022.md)).
> - Bund: Das Datum bestimmt der Kanton ([Art. 124 Abs. 2 DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-124.md)). Eine separate Bundessteuererklärung gibt es nicht.
> 
> ## Wenn die Frist nicht reicht
> 1. **Gesuch vor Fristablauf** (also bis 31. März 2026) beim **Gemeindesteueramt** stellen ([WL ZH 2025 S. 7](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0017.md); [ZStB 132.1 Ziff. G.II](steuerwiki/chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0023.md)). Der Bund verlangt zureichende Gründe und ein Gesuch innerhalb der Frist ([Art. 119 Abs. 2 DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-119.md)).
> 2. **Dauer:** Rechtzeitige Gesuche werden längstens **bis 30. November 2026** bewilligt. Ein erstes, rechtzeitiges Gesuch gilt ohne gegenteiligen schriftlichen Entscheid als stillschweigend bewilligt. Einen schriftlichen Entscheid gibt es nur bei verspäteten Gesuchen oder bei Erstreckung über den 30. November hinaus ([ZStB 132.1 c0024](steuerwiki/chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0024.md), [c0026](steuerwiki/chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0026.md)).
> 3. **Von Amtes wegen bis 30. September 2026:** Das gilt für im Kanton wohnhafte Selbständigerwerbende, für übrige einer Branchenabteilung zugewiesene natürliche Personen und für ausserkantonal Wohnhafte (L-/B-Fälle). Ein Gesuch ist dort nicht nötig ([ZStB 132.1 c0023](steuerwiki/chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0023.md)).
> 4. **Mahnfristen** sind nicht erstreckbar ([WL ZH 2025 S. 7](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0017.md)).
> 5. **Wohnsitz in einem anderen Kanton:** Dessen Fristerstreckungsentscheid gilt auch für Zürich, wenn er vor Fristablauf dem zuständigen Gemeindesteueramt mitgeteilt wird (ebenda).
> 
> ## Wenn die Frist schon abgelaufen ist
> - Gesuche nach Fristablauf sind **abzuweisen**, weil eine abgelaufene Frist nicht mehr erstreckt werden kann. Möglich ist nur die **Wiederherstellung**. Dafür ist bei natürlichen Personen das Gemeindesteueramt zuständig ([ZStB 132.1 c0024](steuerwiki/chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0024.md)).
> - Voraussetzung (Bund): Man war durch Militär-/Zivildienst, Landesabwesenheit, Krankheit oder andere erhebliche Gründe verhindert und hat das Versäumte **innert 30 Tagen nach Wegfall** des Hindernisses nachgeholt ([Art. 124 Abs. 4 DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-124.md)). Die Praxis verweist dafür auch auf § 15 StV ZH.
> - Bei Nichteinreichung trotz Mahnung droht eine Busse. Die Bundesvorschrift dazu ist Art. 174 DBG, mit bis CHF 1 000 und in schweren Fällen oder bei Rückfall bis CHF 10 000. Den Betrag entnehme ich der Themenseite [Fristen & Verfahren](steuerwiki/wiki/themen/fristen-verfahren.md). Den Chunk selbst habe ich nur bis Abs. 1 gelesen, die Beträge also nicht am Gesetzestext nachgeprüft. Die kantonale Busse nach StG ZH habe ich nicht geprüft.
> 
> ## Zum heutigen Stand (9. November 2026)
> Die ordentliche Frist (31. März 2026) ist längst abgelaufen. Hat der Mandant rechtzeitig ein Gesuch gestellt oder gilt die Fristerstreckung von Amtes wegen, läuft die Frist **spätestens am 30. November 2026** ab, bei Amtserstreckung teils schon am 30. September 2026. Ohne rechtzeitiges Gesuch bleibt nur Wiederherstellung (30-Tage-Regel), sonst droht das Mahnverfahren.
> 
> Zeitbezug: Die Frist für Steuerjahr 2025 und das Verfahren richten sich nach der Fassung im Zeitpunkt der Handlung, also 2026. Die Fassung ab 1.1.2026 von ZStB 132.1 ist hier massgebend ([Gültigkeit 2025](steuerwiki/quick/gueltigkeit-2025.md)). Der Status der Wiki-Seite «Fristen & Verfahren» ist «Entwurf». Die Beurteilung im Einzelfall liegt bei SB/ML.

## b07

**Frage:** Wir sind eine Treuhandfirma und brauchen für Mandanten im Kanton Thurgau (Steuerperiode 2025, natürliche Personen) eine Fristerstreckung. Bei welcher Stelle ist das Gesuch einzureichen und bis wann kann die Frist längstens erstreckt werden?

**Soll (Referenz):** TG: Gesuch beim Gemeindesteueramt, das darüber entscheidet. Erstmals eingereichte Gesuche werden grundsätzlich bis längstens 30. September des Deklarationsjahres (2026) gutgeheissen; zusätzliche Gesuche in begründeten Fällen bis 30. November. Treuhänder/Steuerberater, die gewerbsmässig Steuererklärungen ausfüllen, können für ihre Mandanten ein Gesuch längstens bis 31. Dezember des Deklarationsjahres beantragen. Arbeitsüberlastung ist kein Grund.

**Antwort des Agenten** (58.0 s · Tools: 15 Aufrufe read, exec):

> Ich habe die Thurgauer Steuerpraxis (StP 155 Nr. 2) und die Wegleitung nachgeschlagen. Hier das Ergebnis.
> 
> **Einreichestelle**
> - Das Gesuch geht an das **Gemeindesteueramt**, und dieses entscheidet auch darüber. Die Quelle sagt: «Gesuche um Fristerstreckung … natürlicher Personen sind dem Gemeindesteueramt einzureichen, das darüber zu entscheiden hat» (^[tg-stp-155-2__c0001]).
> - Die Wegleitung verlangt ein rechtzeitiges, schriftliches und begründetes Gesuch beim zuständigen Gemeindesteueramt (WL TG 2025 S. 7, ^[tg-wl-2025__c0023]).
> - Die Wegleitung nennt das Gemeindesteueramt der Wohnsitzgemeinde. Bei ausserkantonalen Steuerpflichtigen ist es das Amt der Liegenschafts- bzw. Betriebsstättengemeinde.
> - Die Steuerverwaltung des Kantons ist nur für juristische Personen zuständig (^[tg-stp-155-2__c0003]).
> 
> **Längste Erstreckung für Treuhänder**
> - Gewerbsmässige Treuhänder und Steuerberater können für ihre Mandanten ein Gesuch «längstens bis zum **31. Dezember des Deklarationsjahres**» beantragen (^[tg-stp-155-2__c0002]).
> - Das Deklarationsjahr ist für die Steuerperiode 2025 das Jahr **2026**. Die Frist läuft damit bis **31. Dezember 2026**.
> - Zum Vergleich gilt für Private ohne Vertreter: Das erste Gesuch wird bis längstens 30. September bewilligt. Weitere Gesuche werden in begründeten Fällen bis längstens 30. November gewährt (^[tg-stp-155-2__c0001]).
> - Gesuche über den 30. November hinaus werden abgewiesen, ausser es werden ausserordentliche Gründe glaubhaft gemacht (^[tg-stp-155-2__c0002]).
> 
> **Zu beachten**
> - Die Quelle definiert «Deklarationsjahr» nicht. Dass es das Einreichejahr (hier 2026) ist, steht nur als Bemerkung im Wiki-Datensatz `data/werte/tg/2025.yaml` (Status ☑️ agent-geprüft, nicht ✅ verifiziert). Ich halte das für sicher, würde es aber vor der Mandantenkommunikation bei der Steuerverwaltung oder auf der Mahnung bestätigen lassen.
> - Arbeitsüberlastung gilt nicht als Grund. Auch «starke berufliche Inanspruchnahme des Vertreters» oder fehlende Unterlagen reichen nicht aus (^[tg-stp-155-2__c0001], ^[tg-stp-155-2__c0002]).
> - Das Gesuch muss **rechtzeitig**, also vor Ablauf der laufenden Frist, gestellt werden. Heute ist der 09.11.2026, die 30.-September-Frist ist also schon vorbei. Wo eine ältere Frist bereits abgelaufen ist, hilft die Treuhänder-Regel nach dem Wortlaut der Quelle nicht mehr. Dass abgelaufene Fristen nicht mehr erstreckt werden können, steht im Wiki nur für ZH (ZStB 132.1). Für TG ist es nicht ausdrücklich belegt.
> - Der Entscheid wird schriftlich eröffnet und dem Vertreter zugestellt. Eine verweigerte Erstreckung ist ein Zwischenentscheid und nicht selbständig anfechtbar (^[tg-stp-155-2__c0005]).
> - Eine Gebühr für natürliche Personen nennen die Quellen nicht. Die Kanzleigebühr von Fr. 30 betrifft nur juristische Personen.
> - Fehlt die Steuererklärung trotz Mahnung, droht eine Ermessensveranlagung und eine Busse (^[tg-stp-155-2__c0006]).
> - Natürliche Personen reichen nur die kantonale Steuererklärung ein, sie deckt die direkte Bundessteuer mit ab (Art. 124 DBG). Eine separate Bundes-Erstreckung ist deshalb nicht vorgesehen, soweit die Quellen das hergeben.
> 
> **Fundstelle und Steuerjahr:** StP 155 Nr. 2 Ziff. 1 gilt laut Wiki für die Steuerjahre 2025 bis 2027 (Stand 05.01.2026). Für Verfahrensfragen massgebend ist die Fassung zum Zeitpunkt der Handlung, hier 2026. Die fachliche Beurteilung bleibt bei Ihnen.

## b08

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Auf welchem Formular wird der Abzug für Versicherungsprämien und Sparzinsen berechnet und in welche Ziffer der Steuererklärung wird das Ergebnis übertragen?

**Soll (Referenz):** AR 2025: Berechnung auf Formular 6 (A: bezahlte Prämien/Zinsen, B: Maximalabzug, C: Abzug = niedrigerer Betrag von A und B). Der Betrag C wird auf Seite 3 der Steuererklärung in Ziffer 14 übertragen.

**Antwort des Agenten** (42.3 s · Tools: 6 Aufrufe read, exec, exec):

> **Kanton AR, Steuerjahr 2025**
> 
> Der Abzug wird auf **Formular 6** ermittelt. Das Ergebnis gehört in **Ziffer 14** der Steuererklärung (Seite 3).
> 
> **Ablauf auf Formular 6**
> - **Teil A:** Hier tragen Sie die tatsächlich bezahlten Prämien und Sparzinsen ein:
>   - Krankenversicherung (brutto)
>   - Unfallversicherung (ohne NBUV)
>   - Lebens- und Rentenversicherung
>   - Sparzinsen gemäss Wertschriftenverzeichnis (Formular 2)
>   
>   Davon ziehen Sie die individuellen Prämienverbilligungen ab.
> - **Teil B:** Hier steht der Maximalabzug:
>   - CHF 5'400 für gemeinsam Steuerpflichtige
>   - CHF 2'700 für Alleinstehende
>   - dazu CHF 1'000 je Kind, für das ein Kinderabzug nach Ziff. 23.1–23.3 beansprucht werden kann
> - **Teil C:** Der Abzug ist der **niedrigere Betrag** aus A und B (Code 600). Das Formular nennt dazu: «zu übertragen in die Steuererklärung Seite 3 Ziffer 14».
> 
> **Nicht abziehbar:** Prämien für Mobiliar-, Motorfahrzeug-, Haftpflicht- und andere Sachversicherungen.
> 
> **Kanton und Bund:** Das AR-Formular rechnet nur den kantonalen Betrag. Es hat keine separate Bundesspalte, und die Steuerverwaltung nimmt die Bundesabweichungen automatisch vor. Beim Bund gelten andere Beträge:
> - CHF 3'700 für Ehepaare und CHF 1'800 für übrige Steuerpflichtige
> - ohne Beiträge an 2. Säule oder Säule 3a: CHF 5'550 bzw. CHF 2'700
> - zusätzlich CHF 700 je Kind
> 
> **Fundstellen**
> - Formular 6 AR 2025, S. 1, Schritte 2–3: `ar-form-06-2025__c0002`
> - Wegleitung AR 2025, Ziff. 14, S. 15: `ar-wl-2025__c0085`
> - `quick/wegleitung-ar-2025.md`, Ziff. 14
> 
> **Status:** ☑️ agent-geprüft. Die Fachperson hat die Angaben noch nicht verifiziert.

## b09

**Frage:** Kanton St.Gallen, Steuerjahr 2025: Wo und wie ist ein Gesuch um Fristverlängerung für die Steuererklärung einer natürlichen Person zu stellen und bis wann?

**Soll (Referenz):** SG 2025: Das Gesuch ist vor Ablauf der Einreichefrist (Datum auf Seite 1 der Steuererklärung) zu stellen, vorzugsweise elektronisch unter www.steuern.sg.ch (mit Registernummer und Geburtsdatum); sonst schriftlich an das Gemeindesteueramt. Es kann eine angemessene Fristverlängerung gewährt werden.

**Antwort des Agenten** (63.0 s · Tools: 13 Aufrufe read, ls, memory_search, exec, exec):

> Ich suche noch nach einem konkreten SG-Einreichedatum in den Quellen.
> 
> **Kanton St. Gallen, Steuerjahr 2025: Gesuch um Fristverlängerung**
> 
> **Wo und wie**
> - **Elektronisch (bevorzugt):** über die eFristverlängerung auf www.steuern.sg.ch. Dafür braucht man die **Register-Nr.** und das **Geburtsdatum**, beide stehen auf der persönlichen Steuererklärung. Das Gesuch wird interaktiv bewilligt oder abgelehnt. Quellen: [WL SG 2025 S. 8](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0018.md), [SG Fristverlängerung c0002](steuerwiki/chunks/sg/dauernd/sg-info-fristverlaengerung/sg-info-fristverlaengerung__c0002.md).
> - **Sonst schriftlich** an das **Gemeindesteueramt**, das auch die Steuererklärung entgegennimmt ([WL SG 2025 S. 8](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0018.md)).
> - **Bedingung:** Die Fristverlängerung gibt es nur, wenn die fälligen Steuerrechnungen bezahlt sind ([c0002](steuerwiki/chunks/sg/dauernd/sg-info-fristverlaengerung/sg-info-fristverlaengerung__c0002.md)).
> 
> **Bis wann**
> - Das Gesuch muss **vor Ablauf der Einreichefrist** gestellt werden. Die WL SG 2025 S. 8 sagt, dass «auf Gesuch hin … vor Ablauf der Einreichefrist» eine angemessene Verlängerung gewährt werden kann.
> - Die Einreichefrist selbst ist der **Einreichetermin gemäss Seite 1 der Steuererklärung** ([WL SG 2025 S. 8](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0018.md)). Ein festes Kalenderdatum steht in den Wiki-Quellen nicht. Ich nenne deshalb keins. Bitte das Datum auf Seite 1 der Steuererklärung des Mandanten ablesen.
> - Das Gesuch gehört also vor dieses aufgedruckte Datum. Nach Ablauf lässt sich die Frist nach dem Wiki-Stand nicht mehr verlängern. Das ist im Wiki nur für Bund und Zürich belegt ([Art. 119 DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-119.md), [ZStB 132.1](steuerwiki/chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0024.md)). Für SG ist es nicht belegt, sicher ist nur: Das Gesuch muss vor Ablauf kommen.
> 
> **Nicht im Wiki, bitte beim Original prüfen**
> - Die Dauer der Verlängerung.
> - Mögliche Gebühren.
> - Eine Sammelgesuch- oder Sonderregel für Treuhänder.
> 
> Zu diesen Punkten nennen die SG-Quellen nichts, ich habe nichts ergänzt.
> 
> **Stand und Hinweise**
> - Status: ☑️ agent-geprüft, nicht von der Fachperson verifiziert.
> - Das Gesuch ist ein Verfahrensschritt und wird deshalb im Jahr 2026 gestellt. Die Infoseite gilt laut Wiki für 2025 und 2026 ([c0002](steuerwiki/chunks/sg/dauernd/sg-info-fristverlaengerung/sg-info-fristverlaengerung__c0002.md)).
> - Die Fristverlängerung gilt für die gesamte Steuererklärung, also Staats- und Gemeindesteuer sowie direkte Bundessteuer. Es gibt keine separate Bundessteuererklärung ([Art. 124 DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-124.md), [Art. 168 StG SG](steuerwiki/chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-168.md)).
> - Die Wiki-Seiten zum Thema sind [Fristen & Verfahren](steuerwiki/wiki/themen/fristen-verfahren.md) und [SG-Überblick, Abschnitt 5](steuerwiki/wiki/sg/sg-ueberblick.md).

## b10

**Frage:** Ehepaar im Kanton St.Gallen, Steuerjahr 2025, zwei Kinder mit Kinderabzug, keine Beiträge an die 2. Säule oder Säule 3a bei beiden Partnern. Wie hoch ist der maximale Abzug für Versicherungsprämien und Sparzinsen bei den Kantons-/Gemeindesteuern und bei der direkten Bundessteuer?

**Soll (Referenz):** SG 2025 Kanton: Fr. 6'800 + zusätzlich ohne 2. Säule/3a bis Fr. 1'100 + 2 x bis Fr. 1'100 für die Kinder = Fr. 10'100. Bund: Fr. 3'700 + zusätzlich bis Fr. 1'850 (= Fr. 5'550) + 2 x Fr. 700 = Fr. 6'950. (Voraussetzung für den Zusatzabzug muss bei beiden Partnern erfüllt sein.)

**Antwort des Agenten** (41.8 s · Tools: 11 Aufrufe read):

> **Ergebnis (Steuerjahr 2025, Ehepaar in ungetrennter Ehe, 2 Kinder mit Kinderabzug, keine Beiträge an 2. Säule oder Säule 3a bei beiden Partnern)**
> 
> | Ebene | Berechnung | Maximaler Abzug |
> |---|---|---|
> | **Kanton SG (Staats- und Gemeindesteuer)** | 6'800 + 1'100 (ohne 2. Säule/3a) + 2 × 1'100 (Kinder) | **CHF 10'100** |
> | **Direkte Bundessteuer (DBG)** | 5'550 (3'700 + die Hälfte, ohne 2. Säule/3a) + 2 × 700 (Kinder) | **CHF 6'950** |
> 
> Der Abzug ist der tiefere Betrag aus den effektiv bezahlten Prämien und Sparzinsen und diesen Maximalbeträgen. Die Prämien und Sparzinsen sind dabei netto nach Prämienverbilligung (IPV).
> 
> **Fundstellen**
> 
> - **SG:**
>   - Art. 45 Abs. 1 lit. g StG SG nennt 6'800 für gemeinsam steuerpflichtige Ehegatten. Dazu kommen 1'100, wenn keine Beiträge nach lit. d und e abgezogen werden, und 1'100 je Kind mit Kinderabzug (`sg-stg-2025__art-45-t2`).
>   - WL SG 2025 S. 4 (`sg-wl-2025__c0003`) und Formular 6 SG 2025 (`sg-form-6-2025__c0002`) bestätigen dasselbe.
>   - Das Formular verlangt ausdrücklich, dass die Voraussetzung für den Zuschlag von 1'100 bei beiden Personen erfüllt ist. Das trifft hier zu.
>   - Der Kinderzuschlag setzt voraus, dass der Kinderabzug nach Ziff. 23.1 oder 23.2 beansprucht werden kann. Das trifft hier zu.
> - **Bund:**
>   - Art. 33 Abs. 1 lit. g DBG nennt 3'700 für Ehepaare (`bund-dbg-2025__art-33-t2`).
>   - Art. 33 Abs. 1bis DBG erhöht diesen Betrag um die Hälfte ohne Beiträge nach Abs. 1 lit. d und e, und um 700 je Kind mit Abzug nach Art. 35 Abs. 1 lit. a oder b (`bund-dbg-2025__art-33-t5`).
>   - RS 2-210 S. 2 (`bund-rs-2-210__c0006`) nennt für 2025 ohne Beiträge an Säule 2 und 3a: 5'550 für Verheiratete, plus 700 je Kind.
>   - WL 2a 2025 S. 7 (`bund-wl-2a-2025__c0050`) bestätigt die 5'550.
> 
> **Hinweise**
> 
> - Die Summen 10'100 und 6'950 habe ich selbst aus den Einzelbeträgen gerechnet. Das Wiki nennt sie nicht als fertige Zahl.
> - Die Bundeszahlen gelten nicht für den Kanton. Die Bundesbeträge (3'700, 5'550, 700) gehören nur in die Bundesspalte.
> - In der SG-Steuererklärung gibt es nur eine Ziffer 14 (Code 600, aus Formular 6). Die Bundeslimiten nennt die SG-Wegleitung zwar, im Formular 6 SG werden sie aber nicht gerechnet. Die Bundeskürzung wird nach den vorliegenden Quellen von der Verwaltung vorgenommen. Das ist im Wiki für SG nicht ausdrücklich belegt. Beim Kanton AR steht es dagegen ausdrücklich, und für SG ist es eine Annahme.
> - Status der SG-Zuordnung: ☑️ agent-geprüft, nicht ✅ von der Fachperson verifiziert. Die fachliche Beurteilung bleibt bei SB/ML.

## b11

**Frage:** Arbeitnehmer im Kanton Thurgau, Steuerjahr 2026, Arbeitsweg mit ÖV-Jahresabonnement, effektive Kosten Fr. 6'400. Welcher Fahrkostenabzug ist bei den Staats-/Gemeindesteuern und welcher bei der direkten Bundessteuer zulässig?

**Soll (Referenz):** TG 2026: Kanton gesamthaft max. Fr. 6'000, deshalb Abzug Fr. 6'000 (effektive Kosten Fr. 6'400 werden gekürzt). Bund max. Fr. 3'300, deshalb Abzug Fr. 3'300.

**Antwort des Agenten** (38.8 s · Tools: 9 Aufrufe read):

> **Kanton Thurgau, Steuerjahr 2026, ÖV-Jahresabo mit effektiven Kosten von Fr. 6'400**
> 
> | Ebene | Zulässiger Fahrkostenabzug | Gekürzt um |
> |---|---|---|
> | Staats-/Gemeindesteuern TG | **Fr. 6'000** | Fr. 400 |
> | Direkte Bundessteuer (DBG) | **Fr. 3'300** | Fr. 3'100 |
> 
> Beide Beträge sind Höchstbeträge pro Person. Die Fr. 6'400 übersteigen beide Limiten, daher greift jeweils der Deckel.
> 
> **Fundstellen**
> - **Kanton:** Das Maximum von Fr. 6'000 steht in § 29 Abs. 1 Ziff. 1 StG TG (`tg-stg__par-29`). Die Wegleitung TG 2026 bestätigt es: «Staats- und Gemeindesteuern … gesamthaft maximal Fr. 6 000» (WL TG 2026 S. 37–38, `tg-wl-2026__c0176`).
> - **Bund:** Das Maximum von Fr. 3'300 steht in Art. 26 Abs. 1 lit. a DBG in der Fassung 2026 (`bund-dbg-2026__art-26`). Dieselbe Wegleitungsstelle nennt es ebenfalls: «beim Bund … maximal Fr. 3'300».
> - **Status:** Beide Werte sind ☑️ agent-geprüft, nicht ✅ von der Fachperson verifiziert.
> 
> **Für die Steuererklärung**
> - **Formular 4.2 (Person 1) bzw. 4.3 (Person 2):** Das Abo kommt in Ziff. 2.1 (Codes 206 / 246). Das Total in Ziff. 2.5 (Codes 213 / 253) wird in der Spalte Staat auf Fr. 6'000 und in der Spalte Bund auf Fr. 3'300 begrenzt. Die Kappung erfolgt also im Formular, nicht in der Eingabe.
> - **Lohnausweis Feld F:** Ist dort «unentgeltliche Beförderung» angekreuzt, gibt es keinen Fahrkostenabzug, und Ziff. 2.1 bleibt leer (WL TG 2026, `tg-wl-2026__c0175`). Das ist vor dem Abzug zu prüfen. Das gilt auch, wenn der Arbeitgeber das Abo bezahlt hat.
> - **Beleg:** Das Abo ist mit dem Beleg nachzuweisen. Fr. 6'400 sind höher als die kantonale Limite, die Kürzung auf Fr. 6'000 ist aber keine Ablehnung.
> - **Teilzeit und unterjährige Tätigkeit:** Die Höchstbeträge werden nicht anteilig gekürzt (Themenseite `fahrkosten.md`, zu WL TG 2026).
> - **Weitere Fahrkosten:** Wochenaufenthalt und Ähnliches fallen unter dasselbe Maximum. Die Fr. 6'400 sind dann zusammen mit diesen Kosten zu betrachten.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## b12

**Frage:** Ehepaar im Kanton Zürich, Steuerjahr 2026, nachgewiesene Kinderdrittbetreuungskosten: Kind A (5 Jahre) Fr. 30'000, Kind B (8 Jahre) Fr. 12'000. Wie hoch ist der Abzug bei der Staatssteuer und bei der direkten Bundessteuer?

**Soll (Referenz):** ZH 2026: Maximum pro Kind Staat Fr. 25'300, Bund Fr. 25'800 (Kinder unter 14). Staat: 25'300 + 12'000 = Fr. 37'300. Bund: 25'800 + 12'000 = Fr. 37'800. (Zum Vergleich 2025: Staat max. Fr. 25'000.)

**Antwort des Agenten** (32.6 s · Tools: 6 Aufrufe read, exec):

> **Kanton Zürich, Steuerjahr 2026, Ehepaar mit zwei Kindern unter 14**
> 
> Die Höchstbeträge gelten pro Kind, nicht pro Haushalt. Beide Kinder sind unter 14, das Maximum wird also je Kind geprüft.
> 
> | | Kind A (5 J.) | Kind B (8 J.) | **Abzug total** |
> |---|---|---|---|
> | Nachgewiesene Kosten | 30'000 | 12'000 | 42'000 |
> | **Staats-/Gemeindesteuer** (Max. 25'300 je Kind) | 25'300 (gekappt) | 12'000 | **Fr. 37'300** |
> | **Direkte Bundessteuer** (Max. 25'800 je Kind) | 25'800 (gekappt) | 12'000 | **Fr. 37'800** |
> 
> Die Differenz von Fr. 500 ergibt sich allein aus den unterschiedlichen Höchstbeträgen. Bei Kind A werden Fr. 4'700 (Staat) bzw. Fr. 4'200 (Bund) nicht anerkannt. Bei Kind B wirkt keine Kappung.
> 
> **Fundstellen**
> - Staatssteuer: § 31 Abs. 1 lit. j StG ZH, Fassung 2026: «höchstens Fr. 25 300» je Kind ^[zh-stg-2026__par-31-t3]. Status ☑️ agent-geprüft.
> - Bundessteuer: Art. 33 Abs. 3 DBG, Fassung 2026: «höchstens 25 800 Franken» je Kind ^[bund-dbg-2026__art-33-t7]. Status ☑️ agent-geprüft.
> - Beide Chunks habe ich im Wortlaut geprüft. Zusätzlich bestätigt die Wegleitung ZH 2026 UJ die Maxima (zh-wl-2026-uj__c0105).
> 
> **Voraussetzungen, die ich nicht prüfen konnte** (aus dem Gesetzestext):
> - Die Kinder haben das 14. Altersjahr noch nicht vollendet und leben im gleichen Haushalt wie die unterhaltspflichtigen Eltern.
> - Die Kosten stehen im direkten Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit. Bei einem Ehepaar heisst das in der Regel, dass beide erwerbstätig bzw. in Ausbildung sind.
> - Verpflegungsanteile (z. B. Mittagstisch) sind keine Betreuungskosten und müssen ausgeschieden werden. Auch Subventionen sind abzuziehen. Beides ist im Fall noch zu prüfen.
> - Im Formular steht der Abzug unter Ziff. 16.6, Code 376 (Zuordnung ZH 2026). Diese Zuordnung stützt sich auf die UJ-Fassung des Formulars, weil das reguläre Formular ZH 2026 noch nicht publiziert ist. Ziffer und Code sind am regulären Formular zu prüfen.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

## b13

**Frage:** Ein Mitglied der Milizfeuerwehr erhält für die Erfüllung von Kernaufgaben (Übungen, Pikettdienst, Ernstfalleinsätze) Sold. Bis zu welchem Betrag ist der Feuerwehrsold bei der direkten Bundessteuer steuerfrei, im Steuerjahr 2025 und im Steuerjahr 2026?

**Soll (Referenz):** Bund: 2025 steuerfrei bis maximal Fr. 5'300; 2026 steuerfrei bis maximal Fr. 5'400 (Wert hat sich geändert, nicht übertragen). Der gesamte Sold ist auf dem Lohnausweis zu deklarieren; der steuerfreie Betrag wird auf Formular 9 Berufskosten Ziffer 8 abgezogen.

**Antwort des Agenten** (28.8 s · Tools: 6 Aufrufe read, read, exec):

> Ich prüfe die Zitate in den Chunks.
> 
> Bei der direkten Bundessteuer ist der Sold der Milizfeuerwehrleute für Kernaufgaben (Übungen, Pikettdienste, Kurse, Inspektionen, Ernstfalleinsätze) pro Jahr bis zu diesen Beträgen steuerfrei:
> 
> | Steuerjahr | Steuerfrei bis | Fundstelle |
> |---|---|---|
> | **2025** | **CHF 5'300** | Art. 24 lit. fbis DBG (Fassung 2025), ^[bund-dbg-2025__art-24-t2]; bestätigt in ESTV-Tabelle RS 2-210 S. 2 («Feuerwehrsold … 5'300») |
> | **2026** | **CHF 5'400** | Art. 24 lit. fbis DBG (Fassung 2026), ^[bund-dbg-2026__art-24-t2]; Art. 4 VKP, ^[bund-vkp-2026__art-4]; RS 2-215 S. 1 («Feuerwehrsold … 5'300 → 5'400») |
> 
> Die Erhöhung auf CHF 5'400 gehört zur Anpassung für die kalte Progression 2026 (ESTV-Medienmitteilung vom 11.09.2025, `bund-mm-2025-09-11-kalte-progression-2026__c0003`).
> 
> Was nicht unter die Befreiung fällt (Art. 24 lit. fbis DBG):
> - Pauschalzulagen für Kader
> - Funktionszulagen
> - Entschädigungen für administrative Arbeiten
> - Entschädigungen für Dienstleistungen, welche die Feuerwehr freiwillig erbringt
> 
> Der Betrag gilt nur für die direkte Bundessteuer. Die Staats- und Gemeindesteuer richtet sich nach dem kantonalen Recht und ist je Kanton verschieden. Zum Vergleich:
> 
> | Kanton | 2025 | 2026 |
> |---|---|---|
> | ZH | CHF 8'300 | CHF 8'400 |
> | SG | CHF 5'300 | CHF 5'300 |
> | AR | CHF 5'000 | CHF 5'000 |
> | TG | CHF 5'000 | CHF 5'000 |
> 
> Fundstellen dafür: `quick/vergleich-2025.md` und `quick/vergleich-2026.md`.
> 
> Status im Wiki: ☑️ agent-geprüft, also noch nicht von der Fachperson verifiziert. Den gesamten Sold muss man im Lohnausweis deklarieren. Steuerfrei ist nur der Teil bis zur Limite.

## b14

**Frage:** Ein Mandant wohnt am 31.12.2026 im Kanton Luzern und pendelt mit dem Auto zur Arbeit. Welcher Fahrkostenabzug gilt für die Luzerner Staats- und Gemeindesteuern 2026 und für die direkte Bundessteuer?

**Soll (Referenz):** Luzern ist im Wiki nicht abgedeckt (nur Bund, AR, SG, TG, ZH): kein Wert für die Luzerner Staats-/Gemeindesteuer nennen, auf kantonale Wegleitung verweisen. Für die direkte Bundessteuer 2026 gilt max. Fr. 3'300 (Wegleitung Bund 2026).

**Antwort des Agenten** (37.2 s · Tools: 5 Aufrufe read, exec):

> LU ist nicht abgedeckt. Für den Bund hole ich die Werte 2026.
> 
> **Direkte Bundessteuer 2026: Maximalabzug CHF 3'300. Luzern ist im Wiki nicht erfasst, daher kann ich keinen Wert für die Staats- und Gemeindesteuern nennen.**
> 
> ## Direkte Bundessteuer 2026 (Bund, DBG)
> 
> | Punkt | Wert 2026 | Fundstelle | Status |
> |---|---|---|---|
> | Maximalabzug Fahrten Wohn-/Arbeitsstätte | **CHF 3'300** pro Person | Art. 26 Abs. 1 lit. a DBG ([bund-dbg-2026__art-26](steuerwiki/chunks/bund/2026/bund-dbg-2026/bund-dbg-2026__art-26.md)); ESTV RS 2-215 Ziff. 1 ([bund-rs-2-215__c0004](steuerwiki/chunks/bund/2026/bund-rs-2-215/bund-rs-2-215__c0004.md)) | ☑️ agent-geprüft |
> | Privatauto, pro Kilometer | **CHF 0.75** (2025: 0.70) | RS 2-215 Ziff. 1; ESTV-Medienmitteilung 11.09.2025 ([bund-mm-2025-09-11-kalte-progression-2026__c0004](steuerwiki/chunks/bund/2026/bund-mm-2025-09-11-kalte-progression-2026/bund-mm-2025-09-11-kalte-progression-2026__c0004.md)) | ☑️ |
> 
> - **Abzugsvoraussetzung:** Das Privatfahrzeug ist nur abziehbar, wenn kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist. Sonst gelten die ÖV-Kosten (Art. 5 Abs. 2 BKV, [bund-bkv-2026__art-5](steuerwiki/chunks/bund/2026/bund-bkv-2026/bund-bkv-2026__art-5.md)).
> - **Plafond:** Der Maximalabzug gilt für alle Fahrkosten zusammen. Die Begrenzung auf 3'300 bleibt auch dann bestehen, wenn die Kilometerrechnung mehr ergibt.
> - **Künftiger Ansatz:** Der Kilometeransatz richtet sich neu nach dem TCS-Kilometerpreis. Er kann künftig auch sinken.
> - **Wichtig für die Bundessteuer:** Die Bundesregel gilt unabhängig vom kantonalen Höchstbetrag.
> 
> ## Kanton Luzern 2026 (Staats- und Gemeindesteuern)
> 
> Luzern gehört nicht zu den vom Wiki abgedeckten Kantonen (AR, SG, TG, ZH). Ich habe auch in den Quick-Seiten nach LU gesucht und nichts gefunden. Den Luzerner Höchstbetrag und den Kilometeransatz nenne ich deshalb nicht. Die Werte anderer Kantone auf LU zu übertragen wäre falsch, denn die Höchstbeträge unterscheiden sich stark (AR/TG 6'000, SG 8'000, ZH 5'200).
> 
> Für LU wären nötig:
> - das Luzerner Steuergesetz (§ 29 StG LU, Berufskosten, nach meiner Erinnerung nicht verifiziert),
> - die Wegleitung zur Steuererklärung 2026 der Dienststelle Steuern LU.
> 
> Beides ist bei der Dienststelle Steuern Luzern (steuern.lu.ch) zu prüfen. Wenn die Luzerner Quellen ins Wiki aufgenommen werden sollen, geht das über den Skill `steuerwiki-pflege`.
> 
> **Praktischer Hinweis zur Steuererklärung:** Das Luzerner Formular führt Kanton und Bund beim Fahrkostenabzug getrennt. Der Bundesbetrag ist also separat zu begrenzen, auch wenn der Kanton einen höheren Maximalbetrag zulässt. Das gilt generell. Für LU habe ich es nicht geprüft.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

