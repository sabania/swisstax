# OpenClaw-Testlauf: positionstest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuermem` · Fragen: 10 · Lauf: 2026-11-09 08:17
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## p01

**Frage:** ZH 2025: Ledige unselbständig erwerbende Person, Nettolohn gemäss Lohnausweis CHF 92'000. Sie fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 23 km einfach, 2 Fahrten pro Tag, 220 Arbeitstage. Übrige Berufskosten werden pauschal geltend gemacht (keine Verpflegungskosten). Welche Positionen/Codes im Formular «Berufsauslagen» und welcher Betrag geht in Ziffer 11.1 – Staatssteuer und Bundessteuer getrennt?

**Soll (Referenz):** Formular 360 «Berufsauslagen» (Person 1), Begründung Privatauto Code 2042 (Zeitersparnis über 1 Stunde) ankreuzen. Ziff. 1.3 Auto (CHF 0.70/km, Staat und Bund gleich): 23 km x 2 Fahrten x 220 Tage = 10'120 km x 0.70 = CHF 7'084 (Code 204). Zwischentotal Fahrkosten Code 205: Staat max. CHF 5'200 -> 5'200; Bund max. CHF 3'300 -> 3'300. Ziff. 3 übrige Berufskosten pauschal Code 212: 3% von 92'000 = CHF 2'760 (innerhalb mind. 2'000 / höchstens 4'000; Staat und Bund gleich, vgl. BKV-Anhang). Total Berufsauslagen Code 220 -> Steuererklärung Seite 3, Ziff. 11.1: Staat 5'200 + 2'760 = CHF 7'960; Bund 3'300 + 2'760 = CHF 6'060.

**Antwort des Agenten** (44.9 s · Tools: 16 Aufrufe read, read):

> Jetzt noch die Übrige-Berufskosten-Zeile (Ziff. 3/4, Codes 212/213) und die Pauschal-Verfügung.
> 
> **ZH 2025, Formular 360 «Berufsauslagen» (Person 1)**
> 
> Staatssteuer: **CHF 7'960** in Ziff. 11.1. Bundessteuer: **CHF 6'060** in Ziff. 11.1. Beide Beträge kommen aus Code 220 des Formulars 360.
> 
> | Form. 360 | Code | Staatssteuer | Bundessteuer |
> |---|---|---|---|
> | **Ziff. 1.3** Auto (weisses Schild), 220 Tage × 2 Fahrten × 23 km = 10'120 km × CHF 0.70 | 204 | 7'084 | 7'084 |
> | **Zwischentotal Fahrkosten** (Kappung) | 205 | **5'200** | **3'300** |
> | **Ziff. 3** Übrige Berufskosten pauschal: 3 % × 92'000 = 2'760 (innerhalb Min. 2'000 / Max. 4'000) | 212 | **2'760** | **2'760** |
> | **Ziff. 7** Begründung: «Zeitersparnis von über 1 Stunde» ankreuzen | 2042 | – | – |
> | **Ziff. 6 Total Berufsauslagen** | **220** | **7'960** | **6'060** |
> 
> Nicht auszufüllen sind Ziff. 1.1 (ÖV-Abo, Code 201), Ziff. 1.2 (Velo, Code 202), Ziff. 2 (Verpflegung, Codes 206/208/210), Ziff. 4 (Wochenaufenthalt, Code 2860) und Ziff. 5 (Nebenerwerb, Codes 216/217). Ziff. 3 pauschal ist Code 212. Code 213 ist die effektive Variante und bleibt leer.
> 
> **Quellen (Steuerjahr 2025, Status ☑️ agent-geprüft):**
> - Auto 70 Rp./km und Begründung Zeitersparnis > 1 Std.: [WL ZH 2025 S. 13](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0064.md) und [LS 631.33 Ziff. I/1](steuerwiki/chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0003.md).
> - Formularzeilen Ziff. 1.3, 3 und 6–7: [Form. 360 ZH 2025](steuerwiki/chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0002.md), [c0004](steuerwiki/chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0004.md) und [c0005](steuerwiki/chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md).
> - Höchstbeträge: [WL ZH 2025 S. 13](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md), Staatssteuer CHF 5'200 und direkte Bundessteuer CHF 3'300. Die Staatssteuer-Grenze steht zusätzlich in § 26 StG ZH.
> - Pauschale Ziff. 3: [LS 631.33 Ziff. I/3](steuerwiki/chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0005.md).
> 
> **Hinweise für die Fachperson:**
> - Die 220 Arbeitstage liegen unter der Formularlimite «in der Regel begrenzt auf 240 Tage» ([Form. 360, Ziff. 1.3](steuerwiki/chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0002.md)). Es braucht keine Kürzung.
> - Die Kilometerrechnung (CHF 7'084) übersteigt beide Maxima. Die Begründung und die Arbeitstage sollten trotzdem sauber dokumentiert sein. Bei fehlender Begründung in Ziff. 7 wird der Abzug nicht gewährt (WL ZH 2026 UJ, [Fahrkosten-Thema](steuerwiki/wiki/themen/fahrkosten.md)).
> - Die Zeitersparnis von über 1 Stunde wird von der Haustür zum Arbeitsplatz und zurück gemessen ([WL ZH 2025 S. 13](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0064.md)). Eine Arbeitgeberbestätigung ist dafür nicht vorgesehen, die ÖV-Fahrzeit sollte aber belegbar sein.
> - Der Nettolohn für die 3 %-Pauschale ist der Betrag gemäss Lohnausweis (Ziff. 11). Hier wurden CHF 92'000 angenommen.
> - Das Lohnausweis-Feld F darf nicht angekreuzt sein. Mit Geschäftsfahrzeug gibt es keine Fahrkosten.
> - Die fachliche Beurteilung bleibt bei SB/ML.

## p02

**Frage:** ZH 2025: Verheiratetes Paar, beide in einer Pensionskasse (2. Säule) versichert, zwei minderjährige Kinder mit Kinderabzug. Bezahlte Krankenkassenprämien 2025 (bereits netto nach individueller Prämienverbilligung) CHF 15'600, Sparzinsen gemäss Wertschriftenverzeichnis CHF 150. Wie wird das Formular «Versicherungsprämien» ausgefüllt und welcher Abzug kommt in Ziffer 15 (Staat / Bund)?

**Soll (Referenz):** Formular 365 «Versicherungsprämien»: Teil A: Code 601 Krankenversicherungsprämien 15'600 + Code 604 Sparzinsen 150 -> Total (A) Code 606 = CHF 15'750. Teil B (Maximum): Verheiratete mit Beiträgen an 2. Säule/3a Code 611: Staat 5'800 / Bund 3'700; Kinderzuschlag Code 613: Staat 2 x 1'300 = 2'600 / Bund 2 x 700 = 1'400 -> Total (B) Code 616: Staat CHF 8'400 / Bund CHF 5'100. Teil C Code 270 = der niedrigere Betrag von (A) und (B): Staat CHF 8'400, Bund CHF 5'100 -> Steuererklärung Seite 3, Ziff. 15 (Spalten Staatssteuer/Bundessteuer).

**Antwort des Agenten** (43.8 s · Tools: 5 Aufrufe read, exec):

> **Ziffer 15 (Code 270): Staat CHF 8'400, Bund CHF 5'100.** Die bezahlten Prämien und Zinsen von CHF 15'750 liegen über dem Maximum, deshalb gilt in beiden Spalten das Maximum.
> 
> ## Formular 365 «Versicherungsprämien 2025» (ZH)
> 
> **Teil A, bezahlte Prämien** ([Form. 365 ZH 2025 S. 1](steuerwiki/chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md))
> 
> | Zeile | Code | CHF |
> |---|---|---|
> | 1. Private Krankenversicherungsprämien (netto nach IPV) | 601 | 15'600 |
> | 2. Unfall (nicht NBUV) | 602 | 0 |
> | 3. Lebens-/Rentenversicherung | 603 | 0 |
> | 4. Zinsen von Sparkapitalien (gemäss Wertschriftenverzeichnis) | 604 | 150 |
> | 5. Zwischentotal | 607 | 15'750 |
> | 6. Abzüglich erhaltene Prämienverbilligungen | 605 | **leer** |
> | **Total (A)** | 606 | **15'750** |
> 
> - **Zeile 6 bleibt leer.** Die Prämienverbilligung ist in Ihren CHF 15'600 schon abgezogen. Das Formular sagt dazu, dass in diesem Fall die um die Verbilligung reduzierten Prämien einzutragen sind. Sonst würde sie doppelt abgezogen ([WL ZH 2025 S. 15](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0083.md)).
> - **Zeile 1:** Falls die CHF 15'600 auch Zusatzversicherungen enthalten, gehören sie hierhin. Prämien, die schon im Lohnausweis abgezogen sind (NBUV), und Hausrat-, Haftpflicht- und Motorfahrzeugversicherung gehören nicht ins Formular.
> 
> **Teil B, Maximalabzug** ([Form. 365 ZH 2025 S. 1](steuerwiki/chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md); [§ 31 Abs. 1 lit. g StG ZH](steuerwiki/chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t2.md); [Art. 33 Abs. 1 lit. g und Abs. 1bis DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t2.md))
> 
> | | Staat | Bund |
> |---|---|---|
> | Verheiratete, **mit** Beiträgen an die 2. Säule oder 3a (Code 611) | 5'800 | 3'700 |
> | Zuschlag je Kind, 2 × (Code 613) | 2'600 (2 × 1'300) | 1'400 (2 × 700) |
> | **Total (B), Code 616** | **8'400** | **5'100** |
> 
> - **Verheiratete mit 2. Säule:** Verwendet wird die Zeile «Beiträge an die 2. oder 3. Säule a geleistet». Die erhöhte Zeile (8'700 / 5'550) gilt nur, wenn weder Sie noch Ihre Arbeitgeber Beiträge an die 2. oder 3. Säule geleistet haben. Das ist bei Ihnen nicht der Fall ([WL ZH 2025 S. 15](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0086.md)).
> - **Kinderzuschlag:** In «Anzahl» tragen Sie 2 ein. Der Zuschlag setzt den Kinderabzug nach § 34 StG ZH bzw. Art. 35 DBG voraus. Er halbiert sich nur bei hälftig aufgeteiltem Kinderabzug getrennter Eltern. Das trifft hier nicht zu.
> 
> **Teil C, Abzug** ([Form. 365 ZH 2025 S. 1](steuerwiki/chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0003.md)): Der niedrigere Betrag aus A und B wird nach Seite 3, Ziffer 15 übertragen.
> 
> | | Staatssteuer | Bundessteuer |
> |---|---|---|
> | (A) | 15'750 | 15'750 |
> | (B) | 8'400 | 5'100 |
> | **Abzug Ziff. 15 (Code 270)** | **CHF 8'400** | **CHF 5'100** |
> 
> ## Hinweise
> 
> - Die Sparzinsen von CHF 150 ändern das Ergebnis nicht, weil A auch ohne sie weit über B liegt. Sie gehören trotzdem in Zeile 4. Als Einkommen sind sie separat im Wertschriftenverzeichnis zu deklarieren (Ziff. 4.1).
> - Die Summen 8'400 und 5'100 sind meine Rechnung aus den Formularwerten, kein Beispiel der Wegleitung.
> - Die Werte und Zuordnungen stehen im Wiki mit Status ☑️ (agent-geprüft), nicht ✅ verifiziert. Die fachliche Beurteilung bleibt bei SB/ML.
> 
> Quellen: Formular 365 ZH 2025 (c0001–c0003), WL ZH 2025 S. 15 (c0083–c0086), § 31 StG ZH (2025), Art. 33 DBG (2025). Zusammenfassung: `quick/wegleitung-zh-2025.md` Ziff. 15.

## p03

**Frage:** ZH 2025: Alleinstehende Mandantin unterstützt ihre erwerbsunfähige Mutter (eigener Haushalt, keine Alimente, kein Kinderabzug) nachweislich mit CHF 5'000 im Jahr 2025. In welcher Ziffer wird das geltend gemacht, welcher Abzug gilt bei der Staatssteuer und bei der Bundessteuer, und wirkt sich das auf den Versicherungsprämienabzug aus?

**Soll (Referenz):** Ziff. 24.2 «Abzug für unterstützte Personen» (Code 374); Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der Unterstützung beilegen. Staat: Voraussetzung Unterstützungsleistung mindestens CHF 2'800 -> 5'000 erfüllt -> Abzug CHF 2'800. Bund: Voraussetzung Unterstützungsleistung mindestens CHF 6'800 (Art. 35 Abs. 1 lit. b DBG) -> 5'000 < 6'800 -> kein Unterstützungsabzug (CHF 0). Folge im Formular 365 Teil B.3: Staat zusätzlicher Abzug CHF 1'300 für die unterstützungsbedürftige Person (Code 614); Bund kein Zuschlag von CHF 700 (Code 615), da kein Unterstützungsabzug zusteht.

**Antwort des Agenten** (48.5 s · Tools: 8 Aufrufe read, exec):

> Kurzer Stand: Ich habe Wegleitung, Eckwerte und die Originalchunks (§ 34 StG ZH, Art. 35 und 33 DBG, WL ZH 2025, Form. 365) geprüft. Hier das Ergebnis.
> 
> ## ZH 2025: Unterstützung der erwerbsunfähigen Mutter (CHF 5'000)
> 
> **Ziffer:** 24.2 «Abzug für unterstützte Personen» (Code 374). Die Mutter wird zusätzlich auf Seite 1 der Steuererklärung erfasst (Name, Geburtsjahr, Adresse, Unterstützungsbetrag pro Jahr).
> 
> | | Staats-/Gemeindesteuer | Direkte Bundessteuer |
> |---|---|---|
> | Abzug | **CHF 2'800** | **CHF 0** |
> | Grund | Fixbetrag. Die Leistung von CHF 5'000 erreicht die Mindestschwelle von CHF 2'800. | Die Leistung muss mindestens CHF 6'800 betragen. CHF 5'000 reichen nicht. |
> | Fundstelle | [§ 34 Abs. 1 lit. b StG ZH](steuerwiki/chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-34.md); [WL ZH 2025 S. 21](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0135.md) | [Art. 35 Abs. 1 lit. b DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md); [WL ZH 2025 S. 21](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0135.md) |
> 
> - **Kein Teilabzug:** Es gibt den Fixbetrag oder nichts. Die effektiven CHF 5'000 sind nicht abziehbar, weder beim Staat noch beim Bund.
> - **Bund:** Unterstützung von CHF 5'000 liegt unter der Schwelle von CHF 6'800, deshalb gibt es bei der Bundessteuer keinen Abzug.
> 
> ## Wirkung auf den Versicherungsabzug (Ziff. 15, Form. 365)
> 
> Ja, aber nur beim Staat.
> 
> - **Staat:** Der Maximalabzug steigt um **CHF 1'300** für die unterstützte Person (Form. 365 Teil B Ziff. 3, Code 614; [Form. 365 S. 1](steuerwiki/chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md), § 31 StG).
>   - Maximalabzug für Alleinstehende: CHF 2'900 (mit 2./3a-Beiträgen) bzw. CHF 4'350 (ohne).
>   - Mit Zuschlag ergibt das CHF 4'200 bzw. CHF 5'650 (von mir addiert).
> - **Bund:** Der Zuschlag von CHF 700 setzt einen Abzug nach Art. 35 Abs. 1 lit. a/b DBG voraus ([Art. 33 Abs. 1bis lit. b DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t5.md)). Ohne Unterstützungsabzug entfällt er. Es bleiben CHF 1'800 bzw. CHF 2'700.
> - **Praktisch:** Der Zuschlag hebt nur die Obergrenze an. Abgezogen wird das Minimum aus den bezahlten Prämien und dieser Grenze (Ziff. 15, min(A; B)). Er wirkt nur, wenn die Prämien der Mandantin über CHF 2'900 bzw. CHF 4'350 liegen.
> 
> ## Voraussetzungen und Belege
> 
> - Die Mutter muss erwerbsunfähig oder beschränkt erwerbsfähig **und** unterstützungsbedürftig sein ([WL ZH 2025 S. 21](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0134.md)).
> - Mit der Steuererklärung ist eine Bestätigung der Mutter über Art, Zeitpunkt und Höhe der Unterstützung einzureichen. Zahlungsbelege nur auf Verlangen.
> - Kein Abzug bei Alimenten an dieselbe Person. Das ist hier erfüllt.
> - Richtwerte für die Bedürftigkeit nach [ZStB 34.1 Rz 33](steuerwiki/chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0016.md): steuerbares Einkommen unter CHF 15'000 und steuerbares Vermögen unter CHF 50'000, wenn die Mutter alleinstehend ist. Das ist anhand ihrer Verhältnisse zu prüfen. Es ist ein Richtwert («grundsätzlich»), kein harter Grenzwert. Falls die Mutter im Ausland wohnt, gilt dieser Richtwert nicht (er nennt nur Wohnsitz in der Schweiz).
> 
> Alle genannten Werte sind im Wiki als ☑️ agent-geprüft geführt. Nicht abgeklärt habe ich, ob bei der Bundessteuer eigene Bedürftigkeitsgrenzen gelten. Die fachliche Beurteilung bleibt bei SB/ML.

## p04

**Frage:** SG 2025: Nettoeinkommen gemäss Ziffer 20 CHF 80'000. Arzt- und Zahnarztrechnungen 2025 brutto CHF 6'200, davon von der Krankenkasse vergütet CHF 1'700. Wo werden die Kosten deklariert und wie hoch ist der Abzug für die Staats- und Gemeindesteuern bzw. für die direkte Bundessteuer (Annahme: massgebendes Nettoeinkommen Bund ebenfalls CHF 80'000)?

**Soll (Referenz):** Formular 6 (Rückseite «Krankheits-, Unfall- und behinderungsbedingte Kosten»): Bruttobetrag 6'200 abzüglich Beiträge Dritter 1'700 = selbst getragene Kosten CHF 4'500 -> Steuererklärung Seite 3, Vorkolonne Ziff. 21.1 (Code 650). Kanton SG: Selbstbehalt 2% des Nettoeinkommens (Ziff. 20) = 2% x 80'000 = 1'600 (Code 238) -> Abzug Code 240 = CHF 2'900. Bund: Selbstbehalt 5% (Art. 33 Abs. 1 lit. h DBG; Merkblatt 32) = 4'000 -> Abzug CHF 500. Das SG-Formular hat nur eine Spalte; die Abweichung für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor.

**Antwort des Agenten** (36.8 s · Tools: 6 Aufrufe read, exec):

> **Kurzantwort (SG, Steuerjahr 2025):** Abzug Staats- und Gemeindesteuer **CHF 2'900**, direkte Bundessteuer **CHF 500**.
> 
> **Wo deklarieren**
> - Auf **Formular 6** (Krankheits-, Unfall- und behinderungsbedingte Kosten), Rückseite «Krankheits- und Unfallkosten». Pro Rechnung kommen Datum, Arzt/Zahnarzt, Bruttobetrag, Beiträge Dritter und die selbst getragenen Kosten in die Tabelle. Quelle: [Formular 6 SG 2025 S. 2](steuerwiki/chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0003.md).
> - Das Total gehört ins **Hauptformular 1, Seite 3, Ziff. 21.1, Vorkolonne (Code 650)**. Selbstbehalt (Code 238) und Abzug (Code 240) stehen im selben Block. Quelle: [Formular 1 SG 2025 S. 3](steuerwiki/chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0010.md).
> - Das SG-Formular 1 gilt für Kantons-, Gemeinde- und Bundessteuer. Es hat keine eigene Bundesspalte. Der Bundesabzug mit 5 % Selbstbehalt wird von der Veranlagungsbehörde berechnet (Wegleitung SG 2025 Ziff. 21.1, [WL SG 2025 S. 29](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0098.md)).
> - Die Krankenkasse hat CHF 1'700 vergütet. Diese sind abzuziehen. Wenn Sie nur den Kassenzusammenzug angeben, müssen Sie die detaillierte Kostenaufstellung mit Leistungsübersicht beilegen (WL SG 2025 S. 29; Formular 6 S. 2).
> 
> **Berechnung**
> 
> Selbst getragene Kosten: 6'200 − 1'700 = **CHF 4'500**. Das ist der Betrag für die Vorkolonne (Code 650).
> 
> | | Staat/Gemeinde (SG) | Direkte Bundessteuer |
> |---|---|---|
> | Selbstbehalt in % von Ziff. 20 | 2 % | 5 % |
> | Selbstbehalt (× CHF 80'000) | CHF 1'600 | CHF 4'000 |
> | **Abzug** (4'500 − Selbstbehalt) | **CHF 2'900** | **CHF 500** |
> | Fundstelle | Art. 46 Abs. 1 lit. a StG SG 2025 ([Chunk](steuerwiki/chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-46.md)); [WL SG 2025 S. 29](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0098.md) | Art. 33 Abs. 1 lit. h DBG 2025 ([Chunk](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t3.md)); KS 11 Ziff. 5.3 ([Chunk](steuerwiki/chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0030.md)) |
> 
> **Hinweise**
> - Die Basis für den Selbstbehalt ist das Nettoeinkommen Ziff. 20, also vor den Abzügen Ziff. 21. Das Gesetz spricht von den «Nettoeinkünften» nach Art. 39–45 StG SG.
> - Beim Bund gilt: 5 % der um die Aufwendungen nach Art. 26–33 DBG verminderten Einkünfte. Ihre Annahme von CHF 80'000 setze ich so voraus. Weicht das Bundes-Nettoeinkommen ab, ändert sich der Selbstbehalt entsprechend.
> - Krankenkassenprämien gehören nicht in diesen Abzug, sondern in den Versicherungsabzug.
> - Die Abzugsfähigkeit der einzelnen Rechnungen habe ich nicht geprüft, etwa Zahnarztkosten für Ästhetik oder nicht verordnete Behandlungen.
> - Status der Zuordnung SG 2025: ☑️ agent-geprüft, noch nicht von einer Fachperson verifiziert.

## p05

**Frage:** SG 2025: Mandant gewinnt im Swiss Lotto (interkantonal durchgeführte Lotterie = Grossspiel) einen Einzelgewinn von CHF 1'500'000. Wo wird der Gewinn deklariert, welcher Teil ist steuerbar und welche Einsatzkosten sind abziehbar – Kanton und Bund getrennt?

**Soll (Referenz):** Deklaration im Wertschriften- und Guthabenverzeichnis (Formular 2), Spalte A (Bargewinn aus inländischer Lotterie, verrechnungssteuerpflichtig); Übertrag Ziff. 4.1 (Code 146). Kanton SG: Einzelgewinne aus Grossspielen steuerbar, soweit > Fr. 1'069'800 -> 1'500'000 - 1'069'800 = CHF 430'200 steuerbar; Einsatzkosten unter Ziff. 16.1 (Code 220): 5%, höchstens Fr. 5'400 -> CHF 5'400; netto CHF 424'800. Bund: steuerfrei bis CHF 1'070'400 (Art. 24 lit. ibis DBG) -> steuerbar CHF 429'600; Einsatzkosten 5%, höchstens CHF 5'400 (Art. 33 Abs. 4 DBG) -> CHF 5'400; netto CHF 424'200. (Der Höchstbetrag 5'400 greift unabhängig davon, ob 5% vom Gesamt- oder vom steuerbaren Gewinn gerechnet werden.)

**Antwort des Agenten** (57.2 s · Tools: 16 Aufrufe read, memory_search, exec):

> Ich prüfe noch die Einsatzkosten-Quellen (WL SG S. 27, Formular 32) und die Bundesregelung, dann antworte ich.
> 
> **SG 2025, Swiss-Lotto-Einzelgewinn CHF 1'500'000:** Steuerbar ist nur der Teil über dem Freibetrag, bei Kanton CHF 430'200 und beim Bund CHF 429'600. Die Einsatzkosten sind auf CHF 5'400 begrenzt. Der Gewinn zählt als Grossspiel (interkantonal durchgeführte Lotterie), nicht als Verkaufsförderungs-Lotterie.
> 
> ## Wo deklarieren
> - **Einkünfte, Ziff. 4.1 (Code 146):** Der steuerbare Teil geht in Formular 1, Ziff. 4.1. Der Code 146 umfasst «Wertschriften und Guthaben inkl. Lotterie-/Geldspielgewinne». ^[sg-form-1-2025__c0006]
> - **Formular 2, Wertschriften- und Guthabenverzeichnis:** Die Gewinnbescheinigung der Lotteriegesellschaft bzw. der Bank gehört dazu. Die Wegleitung führt Geldspielgewinne dort unter «j)». ^[sg-wl-2025__c0134, S. 38]
> - **Einsatzkosten, Ziff. 16.1 (Code 220):** Sie werden separat als Abzug geltend gemacht, nicht im Verzeichnis. ^[sg-wl-2025__c0090, S. 27]
> - **Kanton und Bund:** Es gibt nur eine Steuererklärung. Abweichende Bundesabzüge passt die Steuerbehörde automatisch an (Merkblatt Formular 32). ^[sg-form-32-2025__c0004]
> 
> ## Steuerbarer Teil
> Bei Grossspielen ist nur der Betrag über dem Freibetrag steuerbar (Freibetrag, nicht Freigrenze). Der Ansatz «ganzer Gewinn steuerbar» gilt nur für Verkaufsförderungs-Lotterien über CHF 1'100.
> 
> | | Freibetrag Einzelgewinn | Steuerbar bei CHF 1'500'000 | Fundstelle |
> |---|---|---|---|
> | **Kanton SG (Staats-/Gemeindesteuer)** | CHF 1'069'800 | **CHF 430'200** | WL SG 2025 S. 20/38: `sg-wl-2025__c0064`, `__c0134` |
> | **Bund (DBG)** | CHF 1'070'400 | **CHF 429'600** | Art. 24 lit. ibis DBG: `bund-dbg-2025__art-24-t3` |
> 
> ## Abziehbare Einsatzkosten
> - **Kanton:** 5 % der einzelnen steuerbaren Gewinne, höchstens CHF 5'400, unter Ziff. 16.1. ^[sg-wl-2025__c0090]
> - **Bund:** 5 %, höchstens CHF 5'400 (Art. 3 Abs. 6 VKP zu Art. 33 Abs. 4 DBG). ^[bund-vkp-2025__art-3-t4; sg-form-32-2025__c0004]
> - **Im Fall:** Bei 5 % greift in beiden Fällen die Obergrenze. Ob die 5 % auf den steuerbaren Teil (CHF 21'510) oder auf den ganzen Gewinn (CHF 75'000) gerechnet werden, ist unerheblich. Der Abzug beträgt je CHF 5'400.
> - **Online-Spiele:** Für Online-Spiele gelten die effektiven Einsätze, höchstens CHF 26'700 (Kanton) bzw. CHF 26'800 (Bund). Das ist hier nicht einschlägig.
> - **Pauschale:** Es ist eine Pauschale. Effektive Einsatzkosten bei Lotterien/Geldspielen sind nach dem Wortlaut nicht vorgesehen.
> - **Zusammenhang:** Einsatzkosten nicht steuerbarer Gewinne sind nicht abziehbar (Belegkarte Lotteriegewinn). Hier ist der Gewinn steuerbar, der Abzug also zulässig.
> 
> ## Rechnung im Überblick
> 
> | | Kanton | Bund |
> |---|---|---|
> | Gewinn | 1'500'000 | 1'500'000 |
> | – Freibetrag | 1'069'800 | 1'070'400 |
> | = steuerbarer Gewinn (Ziff. 4.1) | **430'200** | **429'600** |
> | – Einsatzkosten (Ziff. 16.1) | **5'400** | **5'400** |
> | = netto zusätzlich im Einkommen | 424'800 | 424'200 |
> 
> ## Hinweise und offene Punkte
> - **Status:** Die Werte sind ☑️ agent-geprüft (nicht ✅ verifiziert). Die Fachperson sollte die Freibeträge am Original (WL SG 2025 S. 20 und 38) bestätigen.
> - **Verrechnungssteuer:** Lottogewinne mit Verrechnungssteuerabzug brauchen die Bescheinigung der Lotteriegesellschaft bzw. den Auszahlungsabschnitt. Die Rückforderung läuft über das Wertschriftenverzeichnis (Belegkarte Lotteriegewinn). Zu Höhe und Verbuchung im SG-Formular 2 habe ich im Wiki keine eigene Fundstelle gelesen. Das bitte am Formular 2 prüfen.
> - **Schuldzinsenabzug:** Der Gewinn zählt nicht als Wertschriftenertrag für die Schuldzinsen-Limite Ziff. 11. Die Wegleitung rechnet Lotterie-/Totogewinne dort heraus.
> - **Einmalgewinn und Steuerjahr:** Für das Steuerjahr 2025 ist das Jahr des Zuflusses massgebend. Die Wiki-Seiten sagen dazu nichts Eigenes. Die Zuordnung zum Jahr 2025 gilt also nur, wenn der Gewinn 2025 ausbezahlt wurde.
> 
> Dies ist keine abschliessende Beurteilung. Die fachliche Würdigung bleibt bei SB/ML.

## p06

**Frage:** SG 2025: Ehepaar mit zwei Kindern, für deren Unterhalt es zur Hauptsache aufkommt: Kind A ist 2-jährig (noch nicht schulpflichtig), Kind B ist 20 und studiert. Für Kind B selbst getragene Ausbildungskosten (Semestergebühren, Bücher, ÖV zum Studienort) CHF 9'500, erhaltenes Stipendium CHF 1'000. Welche Ziffern/Codes und welche Beträge – Kanton und Bund?

**Soll (Referenz):** Kanton SG (Steuererklärung Seite 3, Ziff. 23): Kind A -> Ziff. 23.1 (Code 252) Fr. 7'600; Kind B -> Ziff. 23.2 (Code 254) Fr. 10'800; Ausbildungskosten Kind B -> Ziff. 23.3 (Code 256, Formular 10): 9'500 - 1'000 Stipendium - 3'200 Selbstbehalt = CHF 5'300 (unter dem Maximum von Fr. 13'700). Total Kinderabzüge Kanton CHF 23'700. Bund: einheitlicher Kinderabzug CHF 6'800 pro Kind (Art. 35 Abs. 1 lit. a DBG), kein Abzug für Ausbildungskosten -> 2 x 6'800 = CHF 13'600 (Anpassung durch die Steuerbehörde, Merkblatt 32).

**Antwort des Agenten** (54.6 s · Tools: 13 Aufrufe read, exec, memory_search):

> Ich prüfe gerade den Wortlaut zu Ziff. 23.3 (Selbstbehalt, Stipendien, Höchstbetrag) im Originalchunk und in Art. 48 StG SG. Danach rechne ich den Fall.
> 
> **SG 2025, Ehepaar mit Kind A (2, nicht schulpflichtig) und Kind B (20, Studium)**
> 
> Alle Werte sind ☑️ agent-geprüft. Quellen: Art. 48 StG SG 2025 (`sg-stg-2025__art-48`), WL SG 2025 S. 31 (`sg-wl-2025__c0104`, `__c0105`) und Formular 1 SG 2025 S. 3 (`sg-form-1-2025__c0011`). Das Formular hat keine separate Bundesspalte. Die Bundesabzüge entnimmt die Steuerbehörde derselben Erklärung (Merkblatt 32).
> 
> ### Kanton (Staats- und Gemeindesteuer)
> 
> | Ziff. (Code) | Position | Rechnung | Betrag |
> |---|---|---|---|
> | 23.1 (252) | Kind A, noch nicht schulpflichtig | 1 × 7'600 | **CHF 7'600** |
> | 23.2 (254) | Kind B, in Ausbildung (auch volljährig) | 1 × 10'800 | **CHF 10'800** |
> | 23.3 (256) | Ausbildungskosten Kind B, via Formular 10 | 9'500 − 1'000 Stipendium − 3'200 Selbstbehalt | **CHF 5'300** |
> 
> - **Ziff. 23.3:** Der Höchstbetrag von CHF 13'700 ist nicht erreicht. Abzugsfähig sind Semestergebühren, Bücher und Skripte sowie ÖV-Fahrkosten zum Ausbildungsort. Fahrkosten gelten nur mit öffentlichen Verkehrsmitteln. Der Abzug setzt den Abzug nach Ziff. 23.2 voraus.
> - **Total Sozialabzüge Kinder (Kanton):** CHF 23'700, abgezogen von Ziff. 22 (Reineinkommen) auf dem Weg zu Ziff. 24 (Code 268).
> - **Voraussetzung:** Das Ehepaar kommt für beide Kinder zur Hauptsache auf. Es macht für sie keine Unterhaltsbeiträge nach Ziff. 12.2 geltend.
> 
> ### Bund (direkte Bundessteuer)
> 
> | Position | Rechnung | Betrag | Quelle |
> |---|---|---|---|
> | Kinderabzug (kein Alters- oder Ausbildungsstufen-Unterschied) | 2 × 6'800 | **CHF 13'600** | Art. 35 Abs. 1 lit. a DBG 2025 |
> | Abzug vom Steuerbetrag je Kind (Elterntarif) | 2 × 263 | **CHF 526** | Art. 36 Abs. 2bis DBG 2025 |
> | Ausbildungskosten Kind B (Ziff. 23.3) | – | **kein Abzug** | Ziff. 23.3 gilt nur für Kanton/Gemeinde |
> 
> - **Abzug vom Steuerbetrag:** Er ist kein Einkommensabzug und gilt neben dem Kinderabzug. Die Wegleitung nennt ihn für Kinder im gleichen Haushalt. Bei Kind B ist zu klären, ob es noch im Haushalt der Eltern wohnt. Kind B hat auswärtige Kosten (ÖV zum Studienort), das spricht für das Elternhaus, ist aber nicht belegt.
> - **Nicht kinderbezogen:** Der Verheiratetenabzug von CHF 2'800 gilt beim Bund ebenfalls (Art. 35 Abs. 1 lit. c DBG).
> - **Ziff. 23.4 (Code 264):** Der Unterstützungsabzug ist nicht einschlägig. Kinder mit Kinderabzug sind ausgeschlossen.
> 
> ### Nebenpunkte (Wirkung nur, wenn die Obergrenze erreicht wird)
> 
> - **Ziff. 14, Versicherungsprämien:** Die Obergrenze steigt um CHF 1'100 je Kind mit Abzug nach 23.1/23.2 (Kanton, total 2'200) bzw. um CHF 700 je Kind (Bund, total 1'400). Abgezogen wird nur, was die Prämien und Sparzinsen tatsächlich ausmachen.
> - **Vermögen:** Ich habe CHF 20'000 je Kind aus Art. 64 StG SG gesehen, die Anwendbarkeit aber nicht im Detail geprüft. Bitte vor der Verwendung nachlesen.
> 
> ### Offen
> 
> - Ich habe nichts gefunden, das Einkünfte von Kind B (z.B. Nebenverdienst) mit dem Kinderabzug SG 2025 verknüpft. Eine solche Regel gibt es für AR (über Fr. 18'000), nicht für SG im Wiki. Ob das Stipendium bei Kind B Auswirkungen auf «Unterhalt zur Hauptsache» hat, ist ebenfalls nicht erfasst.
> - Die fachliche Beurteilung bleibt bei SB/ML.

## p07

**Frage:** TG 2025: Arbeitnehmer fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 22 km einfach, Hin- und Rückfahrt täglich, 225 Arbeitstage, keine weiteren Fahrkosten, kein Geschäftsfahrzeug. Wie wird Formular 4.2 Ziff. 2.3–2.5 für Staats- und Bundessteuer ausgefüllt und was geht in die Steuererklärung?

**Soll (Referenz):** Formular 4.2 Ziff. 2.3: 44 km/Tag x 225 Tage = 9'900 km pro Jahr (Code 211). Staatssteuer, Auto-Ansätze nach Jahreskilometern gestaffelt: 3'000 km x 0.60 = 1'800; 2'000 km x 0.50 = 1'000; 4'900 km x 0.40 = 1'960 -> CHF 4'760. Bundessteuer einheitlich CHF 0.70/km: 9'900 x 0.70 = CHF 6'930. Ziff. 2.4 Total effektive Fahrkosten (Code 212): Staat 4'760 / Bund 6'930. Ziff. 2.5 Total abzugsfähige Fahrkosten (Code 213): Staat max. 6'000 -> CHF 4'760; Bund max. 3'300 -> CHF 3'300. Über Ziff. 7 Total Berufsauslagen (Code 240) in Steuererklärung Seite 3, Ziff. 10.1 (linke Spalte Staat, rechte Spalte Bund).

**Antwort des Agenten** (50.2 s · Tools: 13 Aufrufe read, exec, exec):

> Ich prüfe noch die WL-Stellen zur Zeitersparnis und zur «km pro Tag»-Zählweise (Hin- und Rückweg), dann rechne ich das Beispiel durch.
> 
> **Ergebnis TG 2025, Formular 4.2 (Person 1)**
> 
> | Ziff. | Eintrag |
> |---|---|
> | 1.2 Geschäftsfahrzeug | Nein. Das Lohnausweis-Feld F darf nicht angekreuzt sein, sonst gibt es keinen Fahrkostenabzug. |
> | 2.1 ÖV-Abo (Code 206) | leer |
> | 2.2 Velo/Kleinmotorrad (Code 210) | leer |
> | 2.3 Privatauto | «Auto» ankreuzen. Arbeitsweg von Wohnort bis Arbeitsort, **44 km pro Tag** (Hin und zurück) × **225 Tage** = **9'900 km/Jahr**. Dieses Total gehört in die Zeile «km pro Jahr» (Code 211). |
> | 2.4 Total effektive Fahrkosten (Code 212) | **Staat Fr. 4'760 / Bund Fr. 6'930** |
> | 2.5 Total abzugsfähig (Code 213) | **Staat Fr. 4'760 / Bund Fr. 3'300** |
> 
> **Rechnung**
> 
> - **Staatssteuer:** Der Ansatz ist gestaffelt und kumulativ (§ 1 Abs. 1 Ziff. 3 BKV TG, WL TG 2025 S. 38).
>   - 3'000 km × 0.60 = 1'800
>   - 2'000 km × 0.50 = 1'000
>   - 4'900 km × 0.40 = 1'960
>   - Total 4'760. Das liegt unter dem Maximum von Fr. 6'000, es wird also nichts gekürzt.
> - **Bundessteuer:** Der Ansatz ist einheitlich Fr. 0.70/km. 9'900 × 0.70 = 6'930. Das Maximum nach Art. 26 DBG beträgt 3'300 (Formular 4.2 Ziff. 2.5, StP 29 Nr. 2 Ziff. 3.1). Abziehbar sind daher nur 3'300.
> - **Spalten:** Staat und Bund müssen separat gerechnet und in die zwei Spalten eingetragen werden. Der Staats-km-Ansatz darf nicht auf den Bund übertragen werden.
> 
> **Was in die Steuererklärung geht**
> 
> - Formular 4.2 Ziff. 2.5 wird in Ziff. 7 übertragen (nicht Ziff. 2.4). Die Summe aus Ziff. 7 geht in Formular 1 Ziff. 10.1 (Code 240), getrennt nach Staat und Bund.
> - Der Fahrkostenanteil in Ziff. 10.1 beträgt damit **Staat 4'760 / Bund 3'300**.
> - Das Total von Ziff. 10.1 kann ich nicht nennen. Dafür fehlen die Verpflegungsmehrkosten (Ziff. 3), der Nettolohn für die 3%-Pauschale (Ziff. 4), Wochenaufenthalt (Ziff. 5) und Nebenerwerbskosten (Ziff. 6).
> - Beizulegen ist die Begründung: Zeitersparnis über 1 Stunde pro Arbeitstag. Für diese Berechnung zählen nur die morgendliche Hinfahrt und die abendliche Rückkehr (WL TG 2025 S. 38, `tg-wl-2025__c0178`). Zusätzlich braucht es die Fahrtenaufstellung und den Fahrzeugausweis. Den Nachweis der Zeitersparnis, etwa einen Fahrplanvergleich ÖV gegen Auto, sollten Sie bereithalten.
> 
> **Offene Punkte**
> 
> - **Zählweise «km pro Tag»:** Ich habe sie als Hin- und Rückweg verstanden (44 km). Das Beispiel der WL rechnet mit 54 km pro Tag × 225 Tage = 12'150 km (`tg-wl-2025__c0182`) und deckt sich damit, nennt die Zählweise aber nicht ausdrücklich.
> - **225 Tage:** Das gilt bei 100%-Pensum als Regelwert (WL TG 2025 S. 3 und 38). Der Bund kennt keine feste Tageszahl, die 225 Tage wurden nur für den Kanton so festgelegt. Bei der Bundessteuer spielt es hier keine Rolle, weil das Maximum greift.
> - **Mittagsheimkehr:** Sie ist im Sachverhalt nicht erwähnt. Falls es sie gibt, sind die Fahrkosten dafür auf die Höhe des Verpflegungsabzugs begrenzt, und der Verpflegungsabzug in Ziff. 3 entfällt (WL TG 2025 S. 38).
> 
> **Fundstellen und Status:** Alle Angaben gelten für TG, Steuerjahr 2025. Quellen sind Formular 4.2 TG 2025 (`tg-form-04-2-2025__c0002`), § 1 BKV TG (`tg-bkv__par-1`), WL TG 2025 S. 38/39 (`tg-wl-2025__c0178`, `__c0180`, `__c0182`) und StP 29 Nr. 2 Ziff. 3.1 (`tg-stp-29-2__c0006`). Status: ☑️ agent-geprüft, nicht ✅ verifiziert. Die fachliche Beurteilung bleibt bei SB/ML.

## p08

**Frage:** TG 2025: Ehepaar bewohnt sein eigenes Einfamilienhaus am Wohnsitz selbst (Baujahr 1995, nicht landwirtschaftlich geschätzt, keine Mieteinnahmen). Indexierter Mietwert aus Selbstnutzung 2025 CHF 21'000; Unterhalt pauschal. Wie werden Eigenmietwert und Nettoerfolg im Formular 7 berechnet und wohin übertragen – Staat und Bund?

**Soll (Referenz):** Formular 7, Zeile «Mietwert selbstgenutzt» 21'000 (beide Spalten). Selbstnutzungsabzug: Staat 40% = 8'400, Bund 20% = 4'200 -> steuerbarer Eigenmietwert (= Bruttoertrag) Staat CHF 12'600, Bund CHF 16'800. Pauschalabzug Unterhalt: Gebäude älter als 10 Jahre -> 20%, berechnet vom steuerbaren Eigenmietwert: Staat 2'520, Bund 3'360. Nettoerfolg: Staat CHF 10'080, Bund CHF 13'440 (bei selbstgenutzter Liegenschaft je Spalte separat ermitteln). Total Nettoerfolge (Code 180) -> Steuererklärung Seite 2, Ziff. 8, Spalte Staat bzw. Bund.

**Antwort des Agenten** (49.5 s · Tools: 12 Aufrufe read, exec, exec):

> **Ergebnis TG, Steuerjahr 2025:** Der Nettoerfolg aus dem Eigenheim beträgt beim Staat CHF 10'080 und beim Bund CHF 13'440. Die beiden Beträge unterscheiden sich, weil der Selbstnutzungsabzug in den Spalten verschieden hoch ist.
> 
> ## Rechnung in Formular 7 (Spalten Staat / Bund getrennt)
> 
> | Zeile Form. 7 | Staat (Kanton/Gemeinde) | Bund (DBSt) |
> |---|---|---|
> | Mietwert selbstgenutzt (indexiert, Angabe) | 21'000 | 21'000 |
> | Selbstnutzungsabzug | 40 % = −8'400 | 20 % = −4'200 |
> | **Steuerbarer Eigenmietwert** | **12'600** | **16'800** |
> | Miet- und Pachtzinsen | 0 | 0 |
> | Bruttoertrag | 12'600 | 16'800 |
> | Unterhalts-/Betriebskosten, «Pauschal» angekreuzt, 20 % | −2'520 | −3'360 |
> | **Nettoerfolg** | **10'080** | **13'440** |
> 
> **Gründe für die Parameter**
> - **Selbstnutzungsabzug:** Er gilt nur für am Wohnsitz dauernd selbstbewohntes Eigentum. Das trifft bei Ihnen zu und wird in Form. 7 mit «ja» markiert. Der Abzug beträgt Staat 40 % und Bund 20 % (§ 23 Abs. 3 StG TG, `tg-stg__par-23`; StP 23 Nr. 1 Ziff. 3.4, `tg-stp-23-1__c0005`; WL TG 2025 S. 47, `tg-wl-2025__c0225`).
> - **Pauschale 20 %:** Das Gebäude ist Baujahr 1995 und damit am Ende der Steuerperiode 2025 über 10 Jahre alt. Die 20 % werden vom steuerbaren Eigenmietwert berechnet (WL TG 2025 S. 50, `tg-wl-2025__c0238`; § 9 Abs. 2 StV TG). Das Wahlrecht zwischen Pauschale und effektiven Kosten besteht pro Liegenschaft und Jahr. Wer pauschal wählt, braucht kein Formular 8.
> 
> ## Übertrag ins Formular 1 (`tg-form-01-2025__c0009`, S. 2)
> 1. Der Nettoerfolg (Staat 10'080 / Bund 13'440) gehört in **Ziff. 8.1, Code 180**, in die jeweilige Spalte.
> 2. In **Ziff. 9** (Code 198) gilt: Ziff. 7 + Ziff. 8.1, getrennt nach Staat und Bund. Dieser Betrag geht auf **Seite 3, Ziff. 20**. Ziff. 7 entspricht dem Total der Ziff. 6 (WL TG 2025, Kompakt-Wegleitung Ziff. 7 und 9).
> 3. Der Steuerwert des Hauses (Form. 7, Total Steuerwerte) kommt nicht in die Einkünfte. Er gehört zum Vermögen in **Ziff. 31, Code 430**. Die Quelle ist die Liegenschaftensteuerrechnung.
> 
> ## Hinweise für die Fachperson
> - **Mietwert 2025:** Der indexierte Mietwert für die Steuerperiode 2025 steht in der Regel in der Liegenschaftensteuerrechnung (WL TG 2025 S. 47, `tg-wl-2025__c0224`). Prüfen Sie, dass die CHF 21'000 aus der Fassung für 2025 stammen und nicht aus der Rechnung für 2026.
> - **Basis der Bundespauschale (⚠ offen):** Das Wiki führt für den Bund «20 % des Brutto-Eigenmietwerts» (DBG/LKV-Daten). Die TG-Wegleitung nennt als Basis allgemein den «steuerbaren Eigenmietwert», ohne zwischen den Spalten zu unterscheiden. Ich habe die Bundesspalte nach der Form.-7-Logik gerechnet (20 % von 16'800 = 3'360). Läge die Basis bei 21'000, wären es 4'200 und ein Nettoerfolg Bund von 12'600. Das konnte ich im Wiki nicht abschliessend klären, die Entscheidung liegt bei SB/ML.
> - **Sonderfälle:** Ohne Selbstnutzungsabzug und damit zu 100 % steuerbar sind Zweit- und Ferienwohnungen, landwirtschaftlich geschätzte Liegenschaften und an Nahestehende überlassene Objekte. Das ist hier nicht einschlägig.
> - **Status:** Alle Werte (40 %/20 %, Pauschale 10 %/20 %) sind ☑️ agent-geprüft, nicht ✅ von der Fachperson verifiziert. Die Eigenmietwert-Abschaffung gilt erst ab 1.1.2029 und ist für 2025 irrelevant.
> 
> Fundstellen: `tg-form-07-2025__c0002` (Form. 7), `tg-form-01-2025__c0009`, `tg-wl-2025__c0225` und `__c0238`, `tg-stg__par-23`, `tg-stp-23-1__c0005`. Die Übersicht dazu steht in `quick/wegleitung-tg-2025.md`, Ziff. 8.1.

## p09

**Frage:** AR 2025: Ehepaar, beide unabhängig voneinander unselbständig erwerbstätig. Das niedrigere Erwerbseinkommen (Nettolohn der Ehefrau abzüglich Berufskosten, Säule-3a-Beiträge und BVG-Einkäufe) beträgt CHF 38'000. Wie hoch ist der Zweiverdienerabzug in Ziffer 17 für die Staats- und Gemeindesteuer und für die direkte Bundessteuer?

**Soll (Referenz):** Ziff. 17 Zweiverdienerabzug. Kanton AR: 10% des niedrigeren Erwerbseinkommens, mind. Fr. 2'500, max. Fr. 5'200 (Beträge gemäss Anhang 1 StG indexiert per 1.1.2024; Art. 35 Abs. 1 lit. h StG nennt die Basisbeträge 2'400/5'000) -> 10% x 38'000 = CHF 3'800. Bund: Art. 33 Abs. 2 DBG 50% des niedrigeren Erwerbseinkommens, mind. 8'600, max. 14'100 -> 50% x 38'000 = 19'000 -> begrenzt auf CHF 14'100. Die Abweichung für die direkte Bundessteuer wird von der Steuerverwaltung automatisch vorgenommen.

**Antwort des Agenten** (32.0 s · Tools: 6 Aufrufe read, exec):

> **Zweiverdienerabzug AR 2025, Ziff. 17 (niedrigeres Erwerbseinkommen CHF 38'000)**
> 
> | Ebene | Regel | Rechnung | Abzug |
> |---|---|---|---|
> | **Staats- und Gemeindesteuer AR** | 10 % des niedrigeren Erwerbseinkommens, mindestens CHF 2'500, höchstens CHF 5'200 | 10 % × 38'000 = 3'800 (liegt zwischen Min. und Max.) | **CHF 3'800** |
> | **Direkte Bundessteuer** | 50 % des niedrigeren Erwerbseinkommens, mindestens CHF 8'600, höchstens CHF 14'100 | 50 % × 38'000 = 19'000, begrenzt auf das Maximum | **CHF 14'100** |
> 
> **Fundstellen (Steuerjahr 2025)**
> - **AR:**
>   - WL AR 2025 S. 2, Kurzübersicht Ziff. 17: «max. Fr. 5'200, 10 %, mindestens Fr. 2'500» (`ar-wl-2025__c0004`).
>   - Die Beträge stammen aus Anhang 1 zum StG AR, der die indexierten Beträge per 1.1.2024 nennt: Art. 35 Abs. 1 lit. h Minimum 2'500, Maximum 5'200 (`ar-stg-anhang-kp__c0001`).
>   - Der Gesetzestext selbst nennt noch die nicht indexierten 2'400 und 5'000. Massgebend ist Anhang 1.
> - **Bund:**
>   - Art. 33 Abs. 2 DBG: 50 % des niedrigeren Erwerbseinkommens, mindestens 8'600, höchstens 14'100 (`bund-dbg-2025__art-33-t6`).
>   - Die Beträge für 2025 bestätigt das Rundschreiben RS 2-210: Min. 8'600, Max. 14'100 (`bund-rs-2-210__c0007`).
> - **Status:** Die Kompakt-Wegleitung AR 2025 zu Ziff. 17 ist ☑️ agent-geprüft, nicht ✅ verifiziert. Die Beurteilung bleibt bei SB/ML.
> 
> **Hinweis zum Formular**
> Das AR-Formular hat keine separate Bundesspalte. In Ziff. 17 trägst du den kantonalen Betrag ein (3'800). Den Bundesabzug von 14'100 setzt die Steuerverwaltung automatisch an (WL AR 2025 S. 33, `ar-wl-2025__c0179`).
> 
> **Annahme**
> Ich bin davon ausgegangen, dass die CHF 38'000 dem verbleibenden Erwerbseinkommen entsprechen. Die Wegleitung rechnet dafür Nettolohn minus Berufskosten, Säule 3a und BVG-Einkäufe. Beim Bund gilt die gleiche Basis, dort allerdings über die Aufwendungen nach Art. 26–31 DBG und die Abzüge nach Art. 33 Abs. 1 lit. d–f. Wenn ein tieferer Betrag herauskommt, ändert sich nur das Ergebnis des Kantonsabzugs: Bei einem Erwerbseinkommen unter CHF 2'500 wird dieses voll abgezogen.

## p10

**Frage:** AR 2025: Mandant bewohnt sein Einfamilienhaus am Wohnsitz dauernd selbst (Baujahr 1995, einzige Liegenschaft, keine Fremdvermietung). Mietwert gemäss Grundstückschätzung CHF 24'500; er wählt den Pauschalabzug für den Unterhalt. Was wird wo im Formular 7 und in der Steuererklärung (Staats- und Gemeindesteuer) eingetragen?

**Soll (Referenz):** Formular 7, Teil B.a: Eigenmietwert 24'500 abzüglich Selbstnutzungsabzug 20% (4'900) = Total anrechenbarer Eigenmietwert CHF 19'600 = Total Erträge a. und b. -> Übertrag Steuererklärung Seite 2, Ziff. 5. Teil C: Pauschalabzug (Gebäude über 10 Jahre; Bruttomietertrag des gesamten Liegenschaftsbesitzes nicht über Fr. 100'000) = 20% vom Total Liegenschaftserträge = 20% x 19'600 = CHF 3'920 -> Übertrag Steuererklärung Seite 3, Ziff. 15 (separater Abzug, nicht mit Ziff. 5 verrechnet). Wirkung auf das Einkommen netto CHF 15'680.

**Antwort des Agenten** (79.2 s · Tools: 18 Aufrufe read, exec, message):

> **AR 2025, selbstbewohntes Einfamilienhaus mit Pauschalabzug: Kanton Ziff. 5 = CHF 19'600, Ziff. 15 = CHF 3'920.**
> 
> Der Mietwert ist brutto und gilt vor dem Selbstnutzungsabzug von 20 %. Der Pauschalabzug von 20 % wird in AR auf dem Eigenmietwert nach diesem Abzug gerechnet.
> 
> ## Formular 7 (eine Liegenschaft, daher kein Form. 7Z)
> 
> | Abschnitt | Eintrag | CHF |
> |---|---|---|
> | **A** Angaben | Art: Einfamilienhaus · Nutzung: selbst genutzt · Baujahr 1995 · Anteil 100 % | – |
> | **A** Steuerwert | Verkehrswert gemäss Grundstückschätzung (Betrag fehlt in deiner Angabe) → Übertrag StE **S. 4 Ziff. 31** (Code 710) | offen |
> | **B a** Eigenmietwert | Mietwert gemäss Grundstückschätzung | 24'500 |
> | | abzüglich 20 % | −4'900 |
> | | Total anrechenbarer Eigenmietwert | **19'600** |
> | **B b** Fremdnutzung | leer, keine Vermietung | 0 |
> | **B** Total a + b | Übertrag StE **S. 2 Ziff. 5** (Code 712) | **19'600** |
> | **C** Unterhalt | Pauschalabzug (C1): 20 % × 19'600 → StE **S. 3 Ziff. 15** | **3'920** |
> | | Tatsächliche Kosten (C2, Rückseite) | leer |
> 
> ## Steuererklärung Staats- und Gemeindesteuer
> 
> - **Ziff. 5** (Ertrag aus Liegenschaften, Code 712): 19'600. Dieser Betrag fliesst in Ziff. 7 (Total der Einkünfte).
> - **Ziff. 15** (Unterhalts- und Verwaltungskosten, Code nicht verifiziert): 3'920. Er fliesst in Ziff. 18 (Total der Abzüge).
> - **Ziff. 31** (Liegenschaften, Code 710): Steuerwert aus Form. 7 Abschnitt A. Er gehört ins Vermögen und beeinflusst Ziff. 5 nicht.
> - **Netto Kanton:** 19'600 − 3'920 = CHF 15'680.
> 
> ## Voraussetzungen für die Pauschale (alle erfüllt)
> 
> - **Alter:** Das Gebäude ist über 10 Jahre alt (Stichtag Vermögenssteuer, 31.12.2025, ergibt 30 Jahre), also gilt 20 %.
> - **Limite:** Der Bruttomietertrag des gesamten Liegenschaftsbesitzes liegt unter CHF 100'000.
> - **Nutzung:** Es handelt sich um eine Privatliegenschaft mit Wohnnutzung.
> - **Wahlrecht:** Die Wahl gilt je Gebäude und Jahr. Mit der Pauschale sind alle Unterhaltskosten abgegolten, auch Denkmalpflege.
> - **Kein 20 %-Abzug bei Zweit- oder Ferienwohnung.** Hier wird er zu Recht gewährt, weil der Wohnsitz dauernd selbst bewohnt wird.
> 
> ## Bund (direkte Bundessteuer)
> 
> Das AR-Formular hat keine Bundesspalte. Die Steuerverwaltung nimmt die Abweichungen automatisch vor, du trägst dafür nichts separat ein.
> 
> - **Eigenmietwert:** Der Selbstnutzungsabzug von 20 % ist für den Bund nicht belegt (n/a). Der Mietwert wird dort brutto mit CHF 24'500 angesetzt.
> - **Pauschale:** 20 % des Brutto-Eigenmietwerts (Alter am 1.1.2025), also CHF 4'900.
> - **Netto Bund:** 24'500 − 4'900 = CHF 19'600.
> - **Vorbehalt:** Die Behandlung der Bundessteuer ist in den AR-Quellen des Wiki nicht ausdrücklich belegt (⚠, Status «na»). Die Aussage stützt sich auf Art. 5 LKV und den Wegleitungstext.
> 
> ## Fundstellen
> 
> - **Form. 7 Abschn. B:** `ar-form-07-2025__c0002`, Formular 7 AR 2025 S. 1. Eigenmietwert, 20 %-Abzug und Übertrag Ziff. 5. ☑️
> - **Form. 7 Abschn. C:** `ar-form-07-2025__c0003`. Pauschalabzug «der Erträge (B)», Übertrag Ziff. 15. ☑️
> - **Form. 7 Abschn. A:** `ar-form-07-2025__c0001`. Steuerwert, Übertrag Ziff. 31. ☑️
> - **Eigenmietwert nach Wegleitung:** WL AR 2025 S. 30, `ar-wl-2025__c0166`. Mietwert abzüglich 20 % bei dauernder Selbstbewohnung am Wohnsitz. ☑️
> - **Pauschale nach Wegleitung:** WL AR 2025 S. 32, `ar-wl-2025__c0175` und `__c0174`. 20 % bei über 10 Jahren, Limite CHF 100'000, Wahlrecht je Gebäude. ☑️
> - **Rechtsgrundlage Pauschale:** Art. 25 StV AR (`ar-stv__art-25`), MB AR 03 (`ar-mb-03__c0004`). Der Eigenmietwert ist massgebend, und er wird netto angerechnet (Kompakt-Wegleitung AR 2025, Form. 7 Abschn. C). ☑️
> - **Bund:** Art. 5 LKV (`bund-lkv__art-5`). 20 % des Brutto-Eigenmietwerts, Alter zu Beginn der Steuerperiode.
> 
> Status aller genannten Positionen: ☑️ agent-geprüft, nicht ✅ verifiziert. Die fachliche Beurteilung bleibt bei SB/ML.
> 
> ## Offene Punkte
> 
> 1. **Steuerwert:** Der Betrag für Form. 7 Abschn. A fehlt.
> 2. **Um- oder Anbauten seit der letzten Schätzung:** Dafür kommt ein Zuschlag von 2,8 % der Aufwendungen zum Mietwert (WL S. 30). Sonst bleibt es bei 24'500.
> 3. **Hypothek:** Bei einer Hypothek gehören die Zinsen in Ziff. 11 und die Schuld in Ziff. 34.1, beides über Form. 5 Teil A. Die Abzugslimite ist Ertrag Ziff. 4 + Ziff. 5 + CHF 50'000. Hier geht Ziff. 5 mit dem Wert aus diesem Fall ein.
> 4. **Pauschale oder effektiv:** Ob die Pauschale für 2025 günstiger ist als die tatsächlichen Kosten, kann die Fachperson mit den Unterhaltsrechnungen prüfen.

