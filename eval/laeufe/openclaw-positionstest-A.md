# OpenClaw-Testlauf: positionstest-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuermem` · Fragen: 10 · Lauf: 2026-11-09 07:28
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## p01

**Frage:** ZH 2025: Ledige unselbständig erwerbende Person, Nettolohn gemäss Lohnausweis CHF 92'000. Sie fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 23 km einfach, 2 Fahrten pro Tag, 220 Arbeitstage. Übrige Berufskosten werden pauschal geltend gemacht (keine Verpflegungskosten). Welche Positionen/Codes im Formular «Berufsauslagen» und welcher Betrag geht in Ziffer 11.1 – Staatssteuer und Bundessteuer getrennt?

**Soll (Referenz):** Formular 360 «Berufsauslagen» (Person 1), Begründung Privatauto Code 2042 (Zeitersparnis über 1 Stunde) ankreuzen. Ziff. 1.3 Auto (CHF 0.70/km, Staat und Bund gleich): 23 km x 2 Fahrten x 220 Tage = 10'120 km x 0.70 = CHF 7'084 (Code 204). Zwischentotal Fahrkosten Code 205: Staat max. CHF 5'200 -> 5'200; Bund max. CHF 3'300 -> 3'300. Ziff. 3 übrige Berufskosten pauschal Code 212: 3% von 92'000 = CHF 2'760 (innerhalb mind. 2'000 / höchstens 4'000; Staat und Bund gleich, vgl. BKV-Anhang). Total Berufsauslagen Code 220 -> Steuererklärung Seite 3, Ziff. 11.1: Staat 5'200 + 2'760 = CHF 7'960; Bund 3'300 + 2'760 = CHF 6'060.

**Antwort des Agenten** (47.1 s · Tools: 12 Aufrufe read, exec, exec):

> Ich habe alles Nötige im Wiki gefunden und rechne jetzt ab.
> 
> ## ZH 2025: Berufsauslagen (Form. 360) und Ziffer 11.1
> 
> **Annahme:** «2 Fahrten pro Tag» heisst Hin- und Rückfahrt, also 46 km pro Tag. Zählen die 2 Fahrten als zwei Hin- und Rückfahrten (Mittagsheimfahrt), kommt ein anderer Wert heraus (siehe «Offen»).
> 
> ### Fahrkosten (Form. 360 Ziff. 1.3, Code 204, Zwischentotal 205)
> 
> - **Rechnung:** 46 km × 220 Tage = 10'120 km × CHF 0.70 = **CHF 7'084**. Die Quelle nennt CHF 0.70/km (WL ZH 2025 S. 13, `zh-wl-2025__c0064`).
> - **Staatssteuer:** begrenzt auf **CHF 5'200** (`zh-wl-2025__c0065`; Form. 360, `zh-form-360-2025__c0002`).
> - **Bundessteuer:** begrenzt auf **CHF 3'300** (gleiche Quellen).
> - **Zeitersparnis:** Form. 360 Ziff. 7 ankreuzen, Code **2042** «Zeitersparnis von über 1 Stunde». Ohne diese Begründung wird der Abzug nicht gewährt (`zh-form-360-2025__c0005`).
> - **Arbeitstage:** Das Formular begrenzt «in der Regel» auf 240 Tage. Die 220 Tage liegen darunter und sind einzusetzen (`zh-form-360-2025__c0002`).
> - **Ergebnis:** Der Deckel greift, der Abzug ist also auch bei 240 Tagen derselbe. Das Feld F im Lohnausweis muss leer sein, sonst entfällt der Fahrkostenabzug.
> 
> ### Übrige Berufskosten (Form. 360 Ziff. 3, Code 212, pauschal)
> 
> - **Rechnung:** 3 % von CHF 92'000 = **CHF 2'760**. Das liegt zwischen Minimum CHF 2'000 und Maximum CHF 4'000 (LS 631.33 Ziff. I/3, `zh-pauschalierung-berufsauslagen-2025__c0005`; Form. 360, `zh-form-360-2025__c0004`).
> - **Gilt für beide Ebenen:** Pauschale, Minimum und Maximum sind bei Kanton und Bund identisch.
> - **Nettolohn:** Gemeint ist der Nettolohn gemäss Lohnausweis. Er entspricht dem Bruttolohn nach Abzug von AHV/IV/EO/ALV, laufenden BVG-Beiträgen und NBUV-Prämien.
> 
> ### Nicht auszufüllen
> 
> - Ziff. 1.1 (ÖV-Abo, Code 201) und Ziff. 1.2 (Velo, Code 202)
> - Ziff. 2 (Verpflegung, Codes 206/208/210): keine Verpflegungskosten, und Verpflegungsabzug und Mittagsheimfahrt schliessen sich ohnehin aus
> - Ziff. 4 (Wochenaufenthalt, Code 2860)
> - Ziff. 5 (Nebenerwerb, Codes 216/217)
> 
> ### Ergebnis Ziffer 11.1 (Code 220, Total aus Form. 360 Ziff. 6)
> 
> | | Staatssteuer | Bundessteuer |
> |---|---|---|
> | Fahrkosten (Code 205) | CHF 5'200 | CHF 3'300 |
> | Übrige Berufskosten pauschal (Code 212) | CHF 2'760 | CHF 2'760 |
> | **Ziff. 11.1 (Code 220)** | **CHF 7'960** | **CHF 6'060** |
> 
> ### Status und offene Punkte
> 
> - **Status:** Alle verwendeten Werte sind ☑️ agent-geprüft. Der Wert «240 Arbeitstage» ist nur 🟡 extrahiert und für das Ergebnis nicht relevant.
> - **Bund-Widerspruch:** Die ESTV-Wegleitung 2a 2025 S. 6 nennt noch «maximal 3200». DBG Art. 26 Abs. 1 lit. a und RS 2-210 nennen CHF 3'300, und das Gesetz geht vor. Das Formular ZH 2025 nennt ebenfalls CHF 3'300. Die Fachperson sollte das bestätigen.
> - **Anderes Verständnis der Fahrten:** Würden die 23 km nur einmal pro Tag gefahren (46 km Tagestotal wäre falsch), läge der Fahrkostenabzug bei CHF 3'542. Das wären CHF 3'300 beim Bund und CHF 3'542 beim Staat. Die Ziff. 11.1 wäre dann CHF 6'302 (Staat) bzw. CHF 6'060 (Bund). Bitte die Fahrtenzahl bestätigen.
> - **Belege:** Fahrzeugausweis, Fahrtenaufstellung (Arbeitsort, Arbeitstage, km pro Tag) und Lohnausweis (Feld F leer) mit dem Form. 360 einreichen.
> - **Nicht geprüft:** Ob die Zeitersparnis von über einer Stunde tatsächlich gegeben ist. Die Wegleitung misst sie «von der Haustür zum Arbeitsplatz und zurück» (`zh-wl-2025__c0064`). Das ist Sache der Fachperson.

## p02

**Frage:** ZH 2025: Verheiratetes Paar, beide in einer Pensionskasse (2. Säule) versichert, zwei minderjährige Kinder mit Kinderabzug. Bezahlte Krankenkassenprämien 2025 (bereits netto nach individueller Prämienverbilligung) CHF 15'600, Sparzinsen gemäss Wertschriftenverzeichnis CHF 150. Wie wird das Formular «Versicherungsprämien» ausgefüllt und welcher Abzug kommt in Ziffer 15 (Staat / Bund)?

**Soll (Referenz):** Formular 365 «Versicherungsprämien»: Teil A: Code 601 Krankenversicherungsprämien 15'600 + Code 604 Sparzinsen 150 -> Total (A) Code 606 = CHF 15'750. Teil B (Maximum): Verheiratete mit Beiträgen an 2. Säule/3a Code 611: Staat 5'800 / Bund 3'700; Kinderzuschlag Code 613: Staat 2 x 1'300 = 2'600 / Bund 2 x 700 = 1'400 -> Total (B) Code 616: Staat CHF 8'400 / Bund CHF 5'100. Teil C Code 270 = der niedrigere Betrag von (A) und (B): Staat CHF 8'400, Bund CHF 5'100 -> Steuererklärung Seite 3, Ziff. 15 (Spalten Staatssteuer/Bundessteuer).

**Antwort des Agenten** (46.1 s · Tools: 19 Aufrufe read, grep):

> Ich habe das Form. 365 ZH 2025, die Wegleitung ZH 2025 (Ziff. 15), § 31 StG ZH und Art. 33 DBG im Wiki geprüft und rechne jetzt den Fall durch.
> 
> ## Ergebnis (ZH, Steuerjahr 2025)
> 
> Ziffer 15 (Code 270): Staatssteuer CHF 8'400, direkte Bundessteuer CHF 5'100. Der Abzug ist bei beiden gekappt, weil die bezahlten Prämien und Zinsen über dem Maximum liegen.
> 
> ## So wird das Form. 365 ausgefüllt
> 
> **Teil A – bezahlte Prämien** (eine Spalte, gilt für Staat und Bund)
> 
> | Zeile | Code | Betrag CHF |
> |---|---|---|
> | 1. Private Krankenversicherungsprämien | 601 | 15'600 |
> | 2. Private Unfallversicherungsprämien | 602 | leer |
> | 3. Private Lebens- und Rentenversicherungsprämien | 603 | leer |
> | 4. Zinsen von Sparkapitalien (gemäss Wertschriftenverzeichnis) | 604 | 150 |
> | 5. Zwischentotal | 607 | 15'750 |
> | 6. Abzüglich erhaltene Prämienverbilligungen | 605 | **leer** |
> | **Total (A)** | 606 | **15'750** |
> 
> - **Zeile 6 leer lassen:** Die CHF 15'600 sind bereits netto nach individueller Prämienverbilligung. Das Formular sagt dazu: «Die individuelle Prämienverbilligung wird in der Regel mit den Prämien Ihres Krankenversicherers verrechnet. In diesem Fall tragen Sie die um die Prämienverbilligung reduzierten Krankenversicherungsprämien ein» (Formular 365 ZH 2025 S. 1, `zh-form-365-2025__c0001`; WL ZH 2025 S. 15, `zh-wl-2025__c0083`/`c0084`). Ein zweiter Abzug wäre ein Doppelabzug.
> - **Nicht aufführen:** Nichtberufsunfallversicherung (NBUV), die schon im Lohnausweis abgezogen ist, sowie Mobiliar-, Haftpflicht- und Motorfahrzeugversicherungen.
> 
> **Teil B – Maximalabzug** (Spalte Staatssteuer / Bundessteuer)
> 
> Beide sind in der Pensionskasse versichert, also gilt die Zeile «Verheiratete, die Beiträge an die 2. oder 3. Säule a geleistet haben». Die um die Hälfte erhöhten Beträge (8'700 / 5'550) gelten nur, wenn weder die Steuerpflichtigen noch ihr Arbeitgeber Beiträge geleistet haben (WL ZH 2025 S. 15, `zh-wl-2025__c0086`).
> 
> | Zeile | Code | Staat CHF | Bund CHF |
> |---|---|---|---|
> | 1. Verheiratete mit 2./3.-Säule-Beiträgen | 611 | 5'800 | 3'700 |
> | 3. Zusatz je Kind, Anzahl 2 | 613 | 2 × 1'300 = 2'600 | 2 × 700 = 1'400 |
> | **Total (B)** | 616 | **8'400** | **5'100** |
> 
> Der Kinderzuschlag setzt voraus, dass für das Kind ein Kinderabzug nach § 34 StG ZH bzw. Art. 35 DBG geltend gemacht wird. Das ist bei Ihnen der Fall (Quellen: Formular 365 ZH 2025 S. 1, `zh-form-365-2025__c0002`; § 31 Abs. 1 lit. g StG ZH, `zh-stg-2025__par-31-t2`; Art. 33 Abs. 1 lit. g und Abs. 1bis DBG, `bund-dbg-2025__art-33-t2` und `__art-33-t5`).
> 
> **Teil C – Abzug** (Code 270): der niedrigere Betrag von A und B, getrennt für Staat und Bund.
> 
> | | A | B | Abzug in Ziffer 15 |
> |---|---|---|---|
> | Staatssteuer | 15'750 | 8'400 | **CHF 8'400** |
> | Bundessteuer | 15'750 | 5'100 | **CHF 5'100** |
> 
> Die Beträge werden auf Seite 3, Ziffer 15 der Steuererklärung übertragen, in der Spalte Staatssteuer bzw. Bundessteuer.
> 
> ## Hinweise
> 
> - **Kürzung:** CHF 7'350 (Staat) bzw. CHF 10'650 (Bund) der bezahlten Prämien sind nicht abziehbar. Das ist die gesetzliche Begrenzung, kein Fehler. Prämien über der Limite lassen sich nicht in ein anderes Jahr oder eine andere Ziffer verschieben.
> - **Prämien nicht in Ziffer 22.1:** Krankenkassenprämien zählen nicht zu den Krankheitskosten, dort gehören nur Franchise, Selbstbehalt und Arztkosten hin.
> - **Eigene Rechnung:** Die Rechnung stammt aus den Tabellenwerten des Wikis. Das Wiki enthält kein Beispiel der Wegleitung für diese Konstellation.
> - **Status:** Alle Beträge sind ☑️ agent-geprüft, nicht ✅ verifiziert. Die fachliche Freigabe liegt bei SB/ML.

## p03

**Frage:** ZH 2025: Alleinstehende Mandantin unterstützt ihre erwerbsunfähige Mutter (eigener Haushalt, keine Alimente, kein Kinderabzug) nachweislich mit CHF 5'000 im Jahr 2025. In welcher Ziffer wird das geltend gemacht, welcher Abzug gilt bei der Staatssteuer und bei der Bundessteuer, und wirkt sich das auf den Versicherungsprämienabzug aus?

**Soll (Referenz):** Ziff. 24.2 «Abzug für unterstützte Personen» (Code 374); Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der Unterstützung beilegen. Staat: Voraussetzung Unterstützungsleistung mindestens CHF 2'800 -> 5'000 erfüllt -> Abzug CHF 2'800. Bund: Voraussetzung Unterstützungsleistung mindestens CHF 6'800 (Art. 35 Abs. 1 lit. b DBG) -> 5'000 < 6'800 -> kein Unterstützungsabzug (CHF 0). Folge im Formular 365 Teil B.3: Staat zusätzlicher Abzug CHF 1'300 für die unterstützungsbedürftige Person (Code 614); Bund kein Zuschlag von CHF 700 (Code 615), da kein Unterstützungsabzug zusteht.

**Antwort des Agenten** (54.9 s · Tools: 11 Aufrufe read, exec, exec):

> Ich habe das Wiki zu ZH 2025 geprüft (Zuordnung, Gesetzesartikel, Wegleitung, Formular 365). Hier das Ergebnis.
> 
> ## Ziffer
> **Ziff. 24.2, «Abzug für unterstützte Personen» (Code 374)**, im Hauptformular unter den Sozialabzügen. Auf Seite 1 sind Name, Adresse und Betrag der unterstützten Person anzugeben. Als Beleg dient die Bestätigung zur Unterstützung (Art, Zeitpunkt, Höhe) und auf Verlangen die Zahlungsnachweise. Ein Alimentenabzug (Ziff. 13) kommt nicht in Frage.
> Status ☑️ agent-geprüft. Quellen: [Formular 300 ZH 2025 S. 3](steuerwiki/chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md), [§ 34 StG ZH](steuerwiki/chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-34.md).
> 
> ## Abzug Staats- und Bundessteuer
> Der Abzug ist ein fester Betrag. Er ist nicht an die gezahlten CHF 5'000 gekoppelt. Die Unterstützung muss aber mindestens so hoch sein wie der Abzug.
> 
> | | Abzug | Mindestunterstützung | Bei CHF 5'000 |
> |---|---|---|---|
> | Staats-/Gemeindesteuer | CHF 2'800 (§ 34 Abs. 1 lit. b StG ZH) | CHF 2'800 | ✅ erfüllt, **Abzug CHF 2'800** |
> | Direkte Bundessteuer | CHF 6'800 (Art. 35 Abs. 1 lit. b DBG) | CHF 6'800 | ❌ nicht erfüllt, **kein Abzug** |
> 
> Quellen: [WL ZH 2025 S. 21](steuerwiki/chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0135.md), [Art. 35 DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md).
> 
> Beim Bund fehlen CHF 1'800 an der Schwelle. Eine Teilkürzung gibt es nicht. Die Voraussetzungen sind erfüllt, weil die Mutter erwerbsunfähig oder beschränkt erwerbsfähig ist, nicht Ehegattin ist, keinen Kinderabzug auslöst und keine Alimente fliessen.
> 
> ## Auswirkung auf den Versicherungsabzug (Ziff. 15, Form. 365)
> Ja, aber nur bei der Staatssteuer. Der Zuschlag gilt je unterstützungsbedürftige Person, für die ein Abzug nach § 34 Abs. 1 bzw. Art. 35 Abs. 1 lit. a/b möglich ist (Form. 365 Teil B Ziff. 3).
> 
> - **Staat:** Der Maximalabzug steigt um CHF 1'300 (§ 31 Abs. 1 lit. g StG ZH, [Chunk](steuerwiki/chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t2.md)). Für eine Alleinstehende ergibt das:
>   - mit Beiträgen an 2. Säule/3a: CHF 2'900 + 1'300 = **CHF 4'200**
>   - ohne solche Beiträge: CHF 4'350 + 1'300 = **CHF 5'650** (eigene Addition aus den Einzelwerten im Form. 365)
> - **Bund:** Der Zuschlag von CHF 700 setzt einen Abzug nach Art. 35 Abs. 1 lit. a/b voraus ([Art. 33 Abs. 1bis lit. b DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t5.md)). Er entfällt, weil dort kein Unterstützungsabzug gewährt wird. Es gelten weiter CHF 1'800 bzw. CHF 2'700 ohne 2. Säule/3a.
> 
> Der Abzug ist immer der tiefere Betrag aus bezahlten Prämien/Sparzinsen (Teil A) und dem Maximum (Teil B), getrennt für Staat und Bund. Der höhere Staatsmaximalbetrag wirkt sich also nur aus, wenn die effektiven Prämien über CHF 2'900 liegen (bzw. CHF 4'350 ohne 2. Säule/3a). Das ist bei Krankenkassenprämien in der Regel so.
> 
> ## Offene Punkte für SB/ML
> - Das Wiki sagt nicht, ob und wie eigene Einkünfte der Mutter (z. B. IV-Rente, Ergänzungsleistungen) die Unterstützungsbedürftigkeit oder den Nachweis beeinflussen. Dazu habe ich keine Fundstelle. Die Beurteilung liegt bei der Fachperson.
> - Nicht geprüft habe ich, ob die Ermässigung vom Steuerbetrag (CHF 263, Art. 36 Abs. 2bis DBG) hier eine Rolle spielt. Sie ist als Elterntarif ausgestaltet und dürfte bei getrennten Haushalten ohnehin nicht greifen.

## p04

**Frage:** SG 2025: Nettoeinkommen gemäss Ziffer 20 CHF 80'000. Arzt- und Zahnarztrechnungen 2025 brutto CHF 6'200, davon von der Krankenkasse vergütet CHF 1'700. Wo werden die Kosten deklariert und wie hoch ist der Abzug für die Staats- und Gemeindesteuern bzw. für die direkte Bundessteuer (Annahme: massgebendes Nettoeinkommen Bund ebenfalls CHF 80'000)?

**Soll (Referenz):** Formular 6 (Rückseite «Krankheits-, Unfall- und behinderungsbedingte Kosten»): Bruttobetrag 6'200 abzüglich Beiträge Dritter 1'700 = selbst getragene Kosten CHF 4'500 -> Steuererklärung Seite 3, Vorkolonne Ziff. 21.1 (Code 650). Kanton SG: Selbstbehalt 2% des Nettoeinkommens (Ziff. 20) = 2% x 80'000 = 1'600 (Code 238) -> Abzug Code 240 = CHF 2'900. Bund: Selbstbehalt 5% (Art. 33 Abs. 1 lit. h DBG; Merkblatt 32) = 4'000 -> Abzug CHF 500. Das SG-Formular hat nur eine Spalte; die Abweichung für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor.

**Antwort des Agenten** (37.1 s · Tools: 13 Aufrufe read, read):

> **Ergebnis SG 2025:** Die Kosten gehören in Ziffer 21.1. Der Abzug beträgt für Staats- und Gemeindesteuern CHF 2'900 und für die direkte Bundessteuer CHF 500.
> 
> ## Wo deklarieren
> 
> - Die Kosten werden in **Formular 6** (Krankheits-, Unfall- und behinderungsbedingte Kosten, Rückseite) aufgelistet.
> - Pro Rechnung gehören Datum, Arzt bzw. Zahnarzt, Bruttobetrag, Beiträge Dritter (Krankenkasse) und die selbst getragenen Kosten in das Formular.
> - Das **Total der selbst getragenen Kosten** kommt in die **Vorkolonne von Ziffer 21.1** der Steuererklärung (Code 650). Selbstbehalt und Abzug werden in derselben Zeile eingetragen (Codes 238 und 240).
> - Verweist man nur auf den Auszug der Krankenkasse, muss die detaillierte Aufstellung mit Leistungsübersicht zwingend beiliegen.
> - Fundstellen: [Formular 6 SG 2025 S. 2](../steuerwiki/chunks/sg/2025/sg-form-6-2025/sg-form-6-2025__c0003.md), [WL SG 2025 S. 29](../steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0098.md) und [Zuordnung SG 2025](../steuerwiki/quick/zuordnung-sg-2025.md) (Ziff. 21.1).
> 
> ## Berechnung
> 
> Die Vergütungen Dritter werden abgezogen, es zählen nur die selbst getragenen Kosten: 6'200 − 1'700 = **CHF 4'500** (Betrag für die Vorkolonne).
> 
> | | Staats-/Gemeindesteuer SG | Direkte Bundessteuer |
> |---|---|---|
> | Selbst getragene Kosten | 4'500 | 4'500 |
> | Selbstbehalt | 2 % × 80'000 = **1'600** | 5 % × 80'000 = **4'000** |
> | **Abzug** | **CHF 2'900** | **CHF 500** |
> 
> ## Fundstellen
> 
> - **Kanton:** Der Selbstbehalt beträgt 2 % der Nettoeinkünfte (Art. 46 Abs. 1 lit. a StG SG, [sg-stg-2025__art-46](../steuerwiki/chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-46.md)). Die Wegleitung nennt als Basis das Nettoeinkommen nach Ziffer 20 (WL SG 2025 S. 29).
> - **Bund:** Der Selbstbehalt beträgt 5 % der um die Aufwendungen (Art. 26–33 DBG) verminderten steuerbaren Einkünfte (Art. 33 Abs. 1 lit. h DBG, [bund-dbg-2025__art-33-t3](../steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t3.md)). Dasselbe steht im ESTV-Kreisschreiben 11 Ziff. 5.3 ([bund-ks-11__c0030](../steuerwiki/chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0030.md)). Das neue KS 11a gilt erst ab Steuerperiode 2027.
> - Status: ☑️ agent-geprüft (nicht von der Fachperson verifiziert).
> 
> ## Hinweise
> 
> - **Bundesabzug:** Er wird nicht separat im SG-Formular gerechnet. Es gibt eine Erklärung für beide Ebenen, und die Behörde berechnet den Bundesabzug mit dem Bund-Satz. Das Wiki sagt dazu nur, dass bei Ziffer 24 die Bundesabzüge von der Behörde angepasst werden.
> - **Annahme Bund:** Die 80'000 sind Ihre Annahme. Beim Bund ist die Basis formal das Nettoeinkommen nach Art. 26–33 DBG, es kann also vom SG-Wert abweichen.
> - **Nicht in Ziffer 21.1:** Krankenkassenprämien gehören nur in den Versicherungsabzug (Ziffer 14). Prävention, Fitness, Wellness und Fahrkosten zum Arzt sind nicht abziehbar.
> - **Zahnarztrechnungen:** Das Wiki unterscheidet nicht nach Behandlungsart. Kosmetische Behandlungen wären sinngemäss nicht abziehbar, ärztlich nötige Behandlungen schon.
> - **Behinderungsbedingte Kosten:** Falls welche dabei sind, gehören sie ohne Selbstbehalt in Ziffer 21.2 (Code 235).

## p05

**Frage:** SG 2025: Mandant gewinnt im Swiss Lotto (interkantonal durchgeführte Lotterie = Grossspiel) einen Einzelgewinn von CHF 1'500'000. Wo wird der Gewinn deklariert, welcher Teil ist steuerbar und welche Einsatzkosten sind abziehbar – Kanton und Bund getrennt?

**Soll (Referenz):** Deklaration im Wertschriften- und Guthabenverzeichnis (Formular 2), Spalte A (Bargewinn aus inländischer Lotterie, verrechnungssteuerpflichtig); Übertrag Ziff. 4.1 (Code 146). Kanton SG: Einzelgewinne aus Grossspielen steuerbar, soweit > Fr. 1'069'800 -> 1'500'000 - 1'069'800 = CHF 430'200 steuerbar; Einsatzkosten unter Ziff. 16.1 (Code 220): 5%, höchstens Fr. 5'400 -> CHF 5'400; netto CHF 424'800. Bund: steuerfrei bis CHF 1'070'400 (Art. 24 lit. ibis DBG) -> steuerbar CHF 429'600; Einsatzkosten 5%, höchstens CHF 5'400 (Art. 33 Abs. 4 DBG) -> CHF 5'400; netto CHF 424'200. (Der Höchstbetrag 5'400 greift unabhängig davon, ob 5% vom Gesamt- oder vom steuerbaren Gewinn gerechnet werden.)

**Antwort des Agenten** (49.7 s · Tools: 10 Aufrufe read, exec, memory_search):

> Ich habe die Fundstellen für SG und Bund beisammen und prüfe noch kurz die Wegleitung zu Ziff. 4.1, bevor ich antworte.
> 
> **SG 2025, Swiss Lotto (Grossspiel), Einzelgewinn CHF 1'500'000: Ergebnis (Status ☑️ agent-geprüft)**
> 
> Ein Grossspiel-Gewinn ist nur im Betrag über dem Freibetrag steuerbar (Freibetrag, keine Freigrenze). Der Freibetrag ist beim Kanton und beim Bund fast gleich hoch, aber nicht identisch. Daher ergeben sich zwei leicht verschiedene steuerbare Beträge.
> 
> **1. Wo deklarieren?**
> - Der Gewinn gehört ins Wertschriften- und Guthabenverzeichnis (Formular 2 SG 2025, Deklaration der Erträge j). Er wird in die Steuererklärung, Ziff. 4.1 (Code 146), übertragen. ^[sg-wl-2025__c0134] ^[sg-wl-2025__c0064] ^[sg-form-1-2025__c0006]
> - Die Einsatzkosten werden separat in Ziff. 16.1 (Code 220) abgezogen. ^[sg-wl-2025__c0090] ^[sg-form-1-2025__c0009]
> - Die kantonale Steuererklärung deckt beide Ebenen ab (Staats-/Gemeindesteuer und DBG). Die Bundessteuer-Korrektur ergibt sich über die Unterschiede in den Beträgen (siehe Formular 32 SG 2025, Ziff. 16.1). ^[sg-form-32-2025__c0004]
> - Die Bescheinigung der Lotteriegesellschaft bzw. der Auszahlungsabschnitt ist beizulegen. Falls Verrechnungssteuer abgezogen wurde, ist sie im Wertschriftenverzeichnis zu führen (Wiki: [beleg-lotteriegewinn.md](steuerwiki/wiki/belege/beleg-lotteriegewinn.md)).
> 
> **2. Steuerbarer Teil**
> 
> | | Kanton SG (Staats-/Gemeindesteuer) | Bund (DBG) |
> |---|---|---|
> | Gewinn | 1'500'000 | 1'500'000 |
> | Steuerfrei (Freibetrag) | 1'069'800 | 1'070'400 |
> | **Steuerbar** | **430'200** | **429'600** |
> | Rechtsgrundlage | Art. 37 lit. o StG SG ^[sg-stg-2025__art-37-t3] | Art. 24 lit. ibis DBG ^[bund-dbg-2025__art-24-t3] |
> 
> Swiss Lotto fällt als interkantonal durchgeführtes Grossspiel unter diese Regel. Die Wegleitung nennt Grossspiele ausdrücklich: «Lotterien, Sportwetten und Geschicklichkeitsspiele, die je automatisiert oder interkantonal oder online durchgeführt werden». Steuerbar ist nur der Teil über CHF 1'069'800. ^[sg-wl-2025__c0064]
> 
> **3. Abziehbare Einsatzkosten**
> - **Kanton:** 5 % des einzelnen steuerbaren Gewinns, höchstens CHF 5'400 (Art. 45 Abs. 3 StG SG; WL SG 2025 S. 27, Ziff. 16.1). ^[sg-stg-2025__art-45-t5] ^[sg-wl-2025__c0090]
> - **Bund:** 5 %, höchstens CHF 5'400 (Art. 33 Abs. 4 DBG; Art. 3 Abs. 6 VKP). ^[bund-dbg-2025__art-33-t7] ^[bund-vkp-2025__art-3-t4]
> - **Rechnung:** 5 % von 430'200 sind 21'510, 5 % von 1'500'000 sind 75'000. Beide Werte liegen über dem Deckel. Der Abzug beträgt daher auf beiden Ebenen **CHF 5'400**, unabhängig davon, ob man vom steuerbaren oder vom ganzen Gewinn ausgeht.
> - Die höheren Maxima (Kanton CHF 26'700, Bund CHF 26'800) gelten nur für Online-Spielbankenspiele mit effektiv abgebuchten Einsätzen, nicht für Swiss Lotto. ^[sg-form-32-2025__c0004]
> 
> **4. Nettoergebnis**
> 
> | | Kanton | Bund |
> |---|---|---|
> | Steuerbarer Gewinn | 430'200 | 429'600 |
> | – Einsatzkosten | 5'400 | 5'400 |
> | **Netto im Einkommen** | **424'800** | **424'200** |
> 
> Dieser Betrag kommt zum übrigen Einkommen hinzu und wird zum jeweiligen Tarif besteuert. Die Tarifwirkung habe ich nicht berechnet.
> 
> **Offene Punkte**
> - Die Dreiecksfrage «5 % vom steuerbaren oder vom gesamten Gewinn» spielt hier keine Rolle. Das Wiki nennt dazu keine abweichende Praxis.
> - Das Wiki enthält keine eigene Seite zur Verrechnungssteuer auf Lottogewinnen. Ob und in welcher Höhe sie abgezogen wurde, steht auf der Gewinnbestätigung. Das müssen SB/ML am Beleg prüfen.
> - Die Werte gelten nur für 2025. Für 2026 sind die Freibeträge anders (z.B. SG CHF 1'070'900), nicht übertragen.
> - Die fachliche Beurteilung bleibt bei SB/ML.

## p06

**Frage:** SG 2025: Ehepaar mit zwei Kindern, für deren Unterhalt es zur Hauptsache aufkommt: Kind A ist 2-jährig (noch nicht schulpflichtig), Kind B ist 20 und studiert. Für Kind B selbst getragene Ausbildungskosten (Semestergebühren, Bücher, ÖV zum Studienort) CHF 9'500, erhaltenes Stipendium CHF 1'000. Welche Ziffern/Codes und welche Beträge – Kanton und Bund?

**Soll (Referenz):** Kanton SG (Steuererklärung Seite 3, Ziff. 23): Kind A -> Ziff. 23.1 (Code 252) Fr. 7'600; Kind B -> Ziff. 23.2 (Code 254) Fr. 10'800; Ausbildungskosten Kind B -> Ziff. 23.3 (Code 256, Formular 10): 9'500 - 1'000 Stipendium - 3'200 Selbstbehalt = CHF 5'300 (unter dem Maximum von Fr. 13'700). Total Kinderabzüge Kanton CHF 23'700. Bund: einheitlicher Kinderabzug CHF 6'800 pro Kind (Art. 35 Abs. 1 lit. a DBG), kein Abzug für Ausbildungskosten -> 2 x 6'800 = CHF 13'600 (Anpassung durch die Steuerbehörde, Merkblatt 32).

**Antwort des Agenten** (48.1 s · Tools: 10 Aufrufe read, exec):

> Ich habe die Quellen zu SG 2025 gelesen und stelle jetzt die Antwort zusammen.
> 
> # SG 2025: Kinderabzüge und Ausbildungskosten
> 
> **Grundlage:** Kanton SG, Steuerjahr 2025, Formular 1 SG 2025 mit Formular 10. Die Beträge sind ☑️ agent-geprüft; die fachliche Beurteilung bleibt bei SB/ML.
> 
> ## Kanton (Staats- und Gemeindesteuer)
> 
> | Ziffer (Code) | Position | Betrag | Fundstelle |
> |---|---|---|---|
> | **23.1** (252) | Kind A: noch nicht schulpflichtig | **CHF 7'600** | Art. 48 Abs. 1 lit. a Ziff. 1 StG SG (`sg-stg-2025__art-48`); Formular 1 S. 3 (`sg-form-1-2025__c0011`) |
> | **23.2** (254) | Kind B: volljährig, in Ausbildung, Unterhalt zur Hauptsache | **CHF 10'800** | Art. 48 Abs. 1 lit. a Ziff. 2 StG SG; Formular 1 S. 3 |
> | **23.3** (256) | Kind B: Ausbildungskosten, Formular 10 | **CHF 5'300** | Art. 48 Abs. 1 lit. a Ziff. 3 StG SG; WL SG 2025 S. 31 (`sg-wl-2025__c0105`) |
> 
> **Rechnung Ziff. 23.3:**
> - CHF 9'500 selbst getragene Kosten, minus CHF 1'000 Stipendium, ergibt CHF 8'500.
> - CHF 8'500 minus Selbstbehalt CHF 3'200 ergibt **CHF 5'300**.
> - Das liegt unter dem Maximum von CHF 13'700.
> - Die Wegleitung zählt Semestergebühren, Bücher/Skripte und ÖV-Fahrkosten zum Ausbildungsort ausdrücklich zu den abzugsfähigen Kosten.
> - Der Abzug setzt voraus, dass für das Kind der Abzug nach Ziff. 23.2 gilt. Das ist hier erfüllt.
> 
> **Total Sozialabzüge Kanton (Ziff. 23.1–23.3): CHF 7'600 + 10'800 + 5'300 = CHF 23'700.** Ziff. 24 zieht Ziff. 23.1 bis 23.3 vom Reineinkommen ab.
> 
> ## Bund (direkte Bundessteuer)
> 
> | Position | Betrag | Fundstelle |
> |---|---|---|
> | Kinderabzug Kind A | **CHF 6'800** | Art. 35 Abs. 1 lit. a DBG (`bund-dbg-2025__art-35`) |
> | Kinderabzug Kind B (in Ausbildung) | **CHF 6'800** | Art. 35 Abs. 1 lit. a DBG |
> | Ausbildungskosten Kind B | **kein Abzug** | Formular 1 SG nennt den Abzug «nur Kanton/Gemeinde» (`sg-wl-2025__c0105`) |
> | Abzug vom Steuerbetrag | **CHF 263 je Kind**, also CHF 526 | Art. 36 Abs. 2bis DBG (`bund-dbg-2025__art-36-t4`); RS 2-210 S. 2 |
> 
> - Der Bund kennt weder eine Altersstaffelung noch einen Ausbildungsabzug. Total Kinderabzüge Bund: CHF 13'600.
> - Die CHF 263 je Kind sind kein Einkommensabzug. Das Formular hat dafür keine eigene Ziffer.
> - Ziff. 23.4 (Unterstützungsabzug) entfällt. Sie ist nur für Personen ohne Kinderabzug gedacht (Art. 35 Abs. 1 lit. b DBG).
> 
> ## Weitere Wirkungen
> 
> - **Ziff. 14 / Formular 6 (Versicherungsabzug):** Der Maximalabzug erhöht sich je Kind mit Kinderabzug. Das sind beim Kanton CHF 1'100 und beim Bund CHF 700, bei zwei Kindern also CHF 2'200 bzw. CHF 1'400 (`sg-form-6-2025__c0002`). Wie viel davon tatsächlich abgezogen wird, hängt von den bezahlten Prämien ab.
> - **Vermögen, Ziff. 36.3 (Code 334):** Die CHF 20'000 gibt es nur für **minderjährige** Kinder. Das gilt also nur für Kind A, nicht für Kind B (Art. 64 Abs. 1 lit. b StG SG). Beim Bund gibt es keine Vermögenssteuer.
> - **Ziff. 16.2 (Drittbetreuung):** Nur falls für Kind A Kosten anfallen (z.B. Kita). Das Maximum beträgt CHF 26'700 beim Kanton und CHF 25'800 beim Bund. Das ist in dieser Frage nicht enthalten.
> 
> ## Offene Punkte
> 
> - **Stipendium:** Ich habe es nur als Abzugsposten bei den Ausbildungskosten behandelt. Ob es steuerlich anderswo zu erfassen ist, habe ich nicht geprüft.
> - **«Selbst getragen»:** Ich habe angenommen, dass die CHF 9'500 vollständig von den Eltern bezahlt wurden. Zahlt Kind B einen Teil selbst, ist der Betrag entsprechend zu kürzen.
> - **Belege:** Die Rechnungen gehören zu Formular 10. Dort ist auch die ÖV-Fahrkostenposition zu belegen.
> - **Alter von Kind B:** SG kennt dafür keine Altersgrenze. Entscheidend sind Ausbildung und überwiegender Unterhalt. Prüfen Sie, ob die Ausbildung eine Erstausbildung ist und ob Kind B eigene Einkünfte hat.

## p07

**Frage:** TG 2025: Arbeitnehmer fährt begründet (Zeitersparnis über 1 Stunde) mit dem Privatauto zur Arbeit: Arbeitsweg 22 km einfach, Hin- und Rückfahrt täglich, 225 Arbeitstage, keine weiteren Fahrkosten, kein Geschäftsfahrzeug. Wie wird Formular 4.2 Ziff. 2.3–2.5 für Staats- und Bundessteuer ausgefüllt und was geht in die Steuererklärung?

**Soll (Referenz):** Formular 4.2 Ziff. 2.3: 44 km/Tag x 225 Tage = 9'900 km pro Jahr (Code 211). Staatssteuer, Auto-Ansätze nach Jahreskilometern gestaffelt: 3'000 km x 0.60 = 1'800; 2'000 km x 0.50 = 1'000; 4'900 km x 0.40 = 1'960 -> CHF 4'760. Bundessteuer einheitlich CHF 0.70/km: 9'900 x 0.70 = CHF 6'930. Ziff. 2.4 Total effektive Fahrkosten (Code 212): Staat 4'760 / Bund 6'930. Ziff. 2.5 Total abzugsfähige Fahrkosten (Code 213): Staat max. 6'000 -> CHF 4'760; Bund max. 3'300 -> CHF 3'300. Über Ziff. 7 Total Berufsauslagen (Code 240) in Steuererklärung Seite 3, Ziff. 10.1 (linke Spalte Staat, rechte Spalte Bund).

**Antwort des Agenten** (44.6 s · Tools: 13 Aufrufe read, exec):

> Ich prüfe noch die Wegleitungsstelle zur «Zeitersparnis über 1 Stunde», dann kommt die Antwort.
> 
> **TG 2025: Formular 4.2 Ziff. 2.3–2.5, Privatauto mit Zeitersparnis über 1 Std.**
> 
> Staatssteuer und Bundessteuer rechnen unterschiedlich, deshalb gibt es zwei Spalten. Der Abzug beträgt beim Staat CHF 4'760 und beim Bund CHF 3'300.
> 
> **1. Ausnahmefall, Voraussetzung erfüllt**
> - Das Privatauto ist nur in Ausnahmefällen abziehbar. Die Benützung des ÖV ist unter anderem dann unzumutbar, wenn die Zeitersparnis mit dem Privatauto über 1 Stunde pro Arbeitstag beträgt. Massgebend sind nur die morgendliche Hinfahrt und die abendliche Rückkehr. ^[tg-wl-2025__c0178]
> - Die genaue Distanz zwischen Wohnadresse und Fahrzeugstandort am Arbeitsort (oder P+Rail) ist anzugeben. ^[tg-wl-2025__c0179]
> - Bei Zeitersparnis ist die Begründung beizulegen, am besten mit Vergleich der ÖV-Verbindung. Die Beilage-Pflicht ist im Wiki nicht gesondert belegt.
> - Voraussetzungen: kein Geschäftsfahrzeug und Feld F im Lohnausweis leer. Beides ist hier gegeben.
> 
> **2. Kilometer pro Jahr (Ziff. 2.3, Code 211, Person 2: 251)**
> - 22 km × 2 = 44 km pro Tag
> - 44 km × 225 Tage = **9'900 km pro Jahr**
> - Die 225 Tage sind der Regelwert bei 100%-Pensum. ^[tg-wl-2025__c0003]
> - Im Formular trägst du ein: Auto ankreuzen, Arbeitsweg von/bis, 44 km pro Tag, 225 Tage, 9'900 km pro Jahr.
> 
> **3. Betrag je Spalte**
> 
> | | Staatssteuer | Bundessteuer |
> |---|---|---|
> | Ansatz | gestaffelt, kumulativ, inkl. Parkgebühren | einheitlich Fr. 0.70/km |
> | Rechnung | 3'000 km × 0.60 = 1'800<br>2'000 km × 0.50 = 1'000<br>4'900 km × 0.40 = 1'960 | 9'900 km × 0.70 = 6'930 |
> | Ziff. 2.3 / 2.4 (Codes 211 / 212) | **CHF 4'760** | **CHF 6'930** |
> | Ziff. 2.5 (Code 213) Maximum | Fr. 6'000 → nicht erreicht | Fr. 3'300 → gekappt |
> | **Ziff. 2.5 abzugsfähig** | **CHF 4'760** | **CHF 3'300** |
> 
> - Quellen Staffel: § 1 Abs. 1 Ziff. 3 BKV TG ^[tg-bkv__par-1], StP 29 Nr. 2 Ziff. 2.3 ^[tg-stp-29-2__c0004]
> - Quellen Bund-Ansatz 0.70: WL TG 2025 S. 38 ^[tg-wl-2025__c0180], Anhang BKV 2025 ^[bund-bkv-2025__anhang-1]
> - Quellen Maxima: Formular 4.2 ^[tg-form-04-2-2025__c0002], StP 29 Nr. 2 Ziff. 3.1 (Bund 2025: Fr. 3'300) ^[tg-stp-29-2__c0006]
> - Das Maximum wird bei Teilzeit oder unterjähriger Tätigkeit nicht gekürzt. Es umfasst alle Fahrkosten zusammen.
> - Ziff. 2.1 (ÖV-Abo) und 2.2 (Velo) bleiben leer, es gibt keine weiteren Fahrkosten.
> 
> **4. Was in die Steuererklärung geht**
> - Form. 4.2 Ziff. 7 (Code 240) summiert Ziff. 2.5 bis 6 und wird in der Steuererklärung nach Ziff. 10.1 übertragen. Die Spalten Staat und Bund bleiben getrennt.
> - Staatssteuer: Fahrkosten CHF 4'760 plus übrige Berufskosten.
> - Bundessteuer: Fahrkosten CHF 3'300 plus übrige Berufskosten.
> - Die übrigen Berufskosten (Ziff. 4) sind eine separate Pauschale von 3 % des Nettolohns (Lohnausweis Ziff. 11), mindestens Fr. 2'000 und höchstens Fr. 4'000, für Staat und Bund gleich. Sie ist nicht Teil der Fahrkosten und geht zusätzlich in Ziff. 7. Den Betrag kann ich ohne den Nettolohn nicht beziffern.
> - Verpflegung (Ziff. 3) ist nur abziehbar, wenn die Voraussetzungen vorliegen. Bei Heimfahrt über Mittag gilt eine Deckelung, und der Verpflegungsabzug entfällt dann. Das ist hier nicht angegeben. ^[tg-wl-2025__c0179]
> 
> **Status und Vorbehalte**
> - Alle Werte sind ☑️ agent-geprüft, gestützt auf Gesetz, Verordnung, Wegleitung und Formular 2025.
> - Die Fachperson entscheidet, ob die Begründung «Zeitersparnis über 1 Std.» im Einzelfall genügt.

## p08

**Frage:** TG 2025: Ehepaar bewohnt sein eigenes Einfamilienhaus am Wohnsitz selbst (Baujahr 1995, nicht landwirtschaftlich geschätzt, keine Mieteinnahmen). Indexierter Mietwert aus Selbstnutzung 2025 CHF 21'000; Unterhalt pauschal. Wie werden Eigenmietwert und Nettoerfolg im Formular 7 berechnet und wohin übertragen – Staat und Bund?

**Soll (Referenz):** Formular 7, Zeile «Mietwert selbstgenutzt» 21'000 (beide Spalten). Selbstnutzungsabzug: Staat 40% = 8'400, Bund 20% = 4'200 -> steuerbarer Eigenmietwert (= Bruttoertrag) Staat CHF 12'600, Bund CHF 16'800. Pauschalabzug Unterhalt: Gebäude älter als 10 Jahre -> 20%, berechnet vom steuerbaren Eigenmietwert: Staat 2'520, Bund 3'360. Nettoerfolg: Staat CHF 10'080, Bund CHF 13'440 (bei selbstgenutzter Liegenschaft je Spalte separat ermitteln). Total Nettoerfolge (Code 180) -> Steuererklärung Seite 2, Ziff. 8, Spalte Staat bzw. Bund.

**Antwort des Agenten** (46.6 s · Tools: 9 Aufrufe read, read, exec):

> Kurzer Zwischenstand: Ich habe die Fundstellen zu TG 2025 (Formular 7, Wegleitung, StG/StV, StP) gelesen und rechne jetzt das Ergebnis aus.
> 
> ## Ergebnis TG 2025, Formular 7 (Eigenheim, 1 Liegenschaft)
> 
> Annahme: Die CHF 21'000 sind der indexierte Mietwert aus Selbstnutzung vor Selbstnutzungsabzug. Er gilt für Staat und Bund gleich.
> 
> | Schritt | Staatssteuer | Bundessteuer |
> |---|---|---|
> | Mietwert selbstgenutzt (indexiert) | 21'000 | 21'000 |
> | Selbstnutzungsabzug | −40 % = −8'400 | −20 % = −4'200 |
> | **Steuerbarer Eigenmietwert** | **12'600** | **16'800** |
> | Unterhaltspauschale, Gebäude über 10 Jahre: 20 % vom steuerbaren Eigenmietwert | −2'520 | −3'360 |
> | **Nettoerfolg** | **10'080** | **13'440** |
> 
> ## Begründung
> 
> - **Selbstnutzungsabzug:** Er beträgt 40 % beim Kanton und 20 % beim Bund. Er gilt nur für Eigentum, das am Wohnsitz dauernd selbst bewohnt wird. Dein Fall (Wohnsitz, keine Landwirtschaft, keine Vermietung) erfüllt das.
>   - Quellen: § 23 Abs. 3 StG TG (`tg-stg__par-23`, nur 40 % Kanton), StP 23 Nr. 1 Ziff. 3.4 (`tg-stp-23-1__c0005`, Bund 20 %), WL TG 2025 S. 47 (`tg-wl-2025__c0225`).
> - **Pauschale:** Das Gebäude ist Baujahr 1995, also am Ende der Steuerperiode 2025 über 10 Jahre alt. Damit gelten 20 %.
>   - Quellen: § 9 Abs. 2 StV TG (`tg-stv__par-9`), WL TG 2025 S. 50 (`tg-wl-2025__c0238`).
>   - Die Pauschale wird beim selbstbewohnten Eigenheim «vom steuerbaren Eigenmietwert» berechnet, also nach dem Selbstnutzungsabzug. Deshalb unterscheidet sie sich zwischen Staat und Bund.
>   - Sie schliesst Unterhalt, Verwaltung, Versicherungsprämien, Energiespar-/Umweltinvestitionen und Liegenschaftensteuer ein (§ 9 Abs. 3 StV). Daneben darf nichts zusätzlich abgezogen werden.
>   - Die Wahl zwischen Pauschale und effektiven Kosten (dann Formular 8) gilt pro Periode und pro Liegenschaft.
> - **Indexierter Mietwert:** Der Mietwert wird jährlich indexiert. Den Wert für 2025 findest du in der Regel auf der Liegenschaftensteuerrechnung vom Januar 2026 (`tg-wl-2025__c0224`).
> 
> ## Wohin übertragen
> 
> 1. **Formular 7:** Pro Liegenschaft erfasst du in den Spalten «Staatssteuer» und «Bundessteuer» den Mietwert selbstgenutzt, den Selbstnutzungsabzug und den steuerbaren Eigenmietwert. Dazu kreuzt du «Am Wohnsitz selbstgenutzt: ja» und «Pauschal» an und trägst den Nettoerfolg ein (Form. 7 TG 2025 S. 1, `tg-form-07-2025__c0002`).
> 2. **Total Nettoerfolge (Code 180):** Der Übertrag geht in die Steuererklärung Seite 2, Ziff. 8, getrennt nach Staat und Bund (`tg-form-07-2025__c0003`).
>    - Staat: 10'080
>    - Bund: 13'440
> 3. **Ziff. 8.1 (Code 180):** Das ist die Zeile im Formular 1 (`tg-form-01-2025__c0009`). Danach gilt Ziff. 9 = Ziff. 7 plus Ziff. 8.1, je Spalte. Das Total geht in Ziff. 20 und von dort in die Einkommensberechnung.
> 4. **Steuerwert:** Das Total Steuerwerte (Code 430) geht ins Vermögen, Seite 4, Ziff. 31. Das betrifft nur die Staats- und Gemeindesteuer, da der Bund kein Vermögen besteuert.
> 
> Status der Zuordnung Ziff. 8.1: ☑️ agent-geprüft (Steuerjahr 2025).
> 
> ## Offen und zu prüfen
> 
> - Ich bin davon ausgegangen, dass die 21'000 vor dem Selbstnutzungsabzug stehen. Bitte vor dem Ausfüllen mit der Liegenschaftensteuerrechnung abgleichen.
> - Das Baujahr 1995 stammt aus deinen Angaben. Massgebend ist das Alter laut Schätzung.
> - Rundungsregeln für Formular 7 habe ich im Wiki nicht gefunden.
> - Der Eigenmietwert bleibt bis und mit 2028 steuerbar. Die Abschaffung per 01.01.2029 betrifft 2025 nicht.
> - Die fachliche Beurteilung bleibt bei SB/ML.

## p09

**Frage:** AR 2025: Ehepaar, beide unabhängig voneinander unselbständig erwerbstätig. Das niedrigere Erwerbseinkommen (Nettolohn der Ehefrau abzüglich Berufskosten, Säule-3a-Beiträge und BVG-Einkäufe) beträgt CHF 38'000. Wie hoch ist der Zweiverdienerabzug in Ziffer 17 für die Staats- und Gemeindesteuer und für die direkte Bundessteuer?

**Soll (Referenz):** Ziff. 17 Zweiverdienerabzug. Kanton AR: 10% des niedrigeren Erwerbseinkommens, mind. Fr. 2'500, max. Fr. 5'200 (Beträge gemäss Anhang 1 StG indexiert per 1.1.2024; Art. 35 Abs. 1 lit. h StG nennt die Basisbeträge 2'400/5'000) -> 10% x 38'000 = CHF 3'800. Bund: Art. 33 Abs. 2 DBG 50% des niedrigeren Erwerbseinkommens, mind. 8'600, max. 14'100 -> 50% x 38'000 = 19'000 -> begrenzt auf CHF 14'100. Die Abweichung für die direkte Bundessteuer wird von der Steuerverwaltung automatisch vorgenommen.

**Antwort des Agenten** (30.2 s · Tools: 9 Aufrufe read):

> **AR 2025, Ziffer 17 (Zweiverdienerabzug), niedrigeres Erwerbseinkommen CHF 38'000:**
> 
> | Ebene | Regel | Rechnung | Abzug |
> |---|---|---|---|
> | **Staats-/Gemeindesteuer AR** | 10 % des niedrigeren Erwerbseinkommens, mindestens CHF 2'500, höchstens CHF 5'200 | 10 % × 38'000 = 3'800, liegt zwischen Minimum und Maximum | **CHF 3'800** |
> | **Direkte Bundessteuer** | 50 % des niedrigeren Erwerbseinkommens, mindestens CHF 8'600, höchstens CHF 14'100 | 50 % × 38'000 = 19'000, begrenzt auf das Maximum | **CHF 14'100** |
> 
> **Fundstellen (Steuerjahr 2025)**
> - AR: [WL AR 2025 S. 2, Kurzübersicht Ziff. 17](steuerwiki/chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md) nennt «10 %, mindestens Fr. 2'500, max. Fr. 5'200». [StG AR Anhang 1 S. 1](steuerwiki/chunks/ar/2025/ar-stg-anhang-kp/ar-stg-anhang-kp__c0001.md) nennt die indexierten Beträge 2'500 und 5'200 (Art. 35 Abs. 1 lit. h). Der Gesetzestext selbst nennt noch die unindexierten 2'400 und 5'000, massgebend ist Anhang 1. Status ☑️ agent-geprüft.
> - Bund: [Art. 33 Abs. 2 DBG (Fassung 2025)](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t6.md) nennt «50 Prozent, jedoch mindestens 8600 Franken und höchstens 14 100 Franken». Status ☑️ agent-geprüft.
> 
> **Hinweise**
> - Die Basis von CHF 38'000 stimmt mit der AR-Regel überein. Sie ist der Nettolohn nach Berufskosten, Säule 3a und BVG-Einkäufen ([WL AR 2025 S. 2](steuerwiki/chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0004.md); [Art. 33 Abs. 2 DBG](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t6.md)).
> - Beim Bund fliessen zusätzlich die allgemeinen Abzüge nach Art. 33 Abs. 1 lit. d–f DBG ins Erwerbseinkommen ein. Wenn Kanton und Bund unterschiedliche Berufskosten haben (Fahrkosten 6'000 bzw. 3'300, Pauschale 10 % bzw. 3 %), kann das niedrigere Erwerbseinkommen beim Bund abweichen. Die CHF 38'000 gelten dann nur für die AR-Rechnung. Das Ergebnis beim Bund (14'100) bleibt aber stabil, solange das bundesrechtliche Erwerbseinkommen mindestens CHF 28'200 beträgt.
> - Beide Beträge werden in derselben Ziffer 17 der AR-Steuererklärung erfasst: der Kantonsbetrag in der Kantonsspalte, der Bundesbetrag in der Bundesspalte ([Zuordnung AR 2025](steuerwiki/quick/zuordnung-ar-2025.md), Ziff. 17).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## p10

**Frage:** AR 2025: Mandant bewohnt sein Einfamilienhaus am Wohnsitz dauernd selbst (Baujahr 1995, einzige Liegenschaft, keine Fremdvermietung). Mietwert gemäss Grundstückschätzung CHF 24'500; er wählt den Pauschalabzug für den Unterhalt. Was wird wo im Formular 7 und in der Steuererklärung (Staats- und Gemeindesteuer) eingetragen?

**Soll (Referenz):** Formular 7, Teil B.a: Eigenmietwert 24'500 abzüglich Selbstnutzungsabzug 20% (4'900) = Total anrechenbarer Eigenmietwert CHF 19'600 = Total Erträge a. und b. -> Übertrag Steuererklärung Seite 2, Ziff. 5. Teil C: Pauschalabzug (Gebäude über 10 Jahre; Bruttomietertrag des gesamten Liegenschaftsbesitzes nicht über Fr. 100'000) = 20% vom Total Liegenschaftserträge = 20% x 19'600 = CHF 3'920 -> Übertrag Steuererklärung Seite 3, Ziff. 15 (separater Abzug, nicht mit Ziff. 5 verrechnet). Wirkung auf das Einkommen netto CHF 15'680.

**Antwort des Agenten** (59.5 s · Tools: 10 Aufrufe read, exec):

> The WL-Muster zu Form. 7 B/C und MB 03 c0006 könnten ein Rechenbeispiel enthalten – ich prüfe beide.
> 
> **Ergebnis (AR, Steuerjahr 2025, Formular 7 mit Übertrag in die Steuererklärung):** In Ziff. 5 kommen CHF 19'600, in Ziff. 15 CHF 3'920 und in Ziff. 31 der Steuerwert aus der Grundstückschätzung. Die Pauschale von 3'920 rechne ich vom Wert nach Selbstnutzungsabzug (siehe «Annahmen»).
> 
> **Formular 7 (eine Liegenschaft, daher kein Formular 7Z)**
> 
> | Abschnitt | Feld | Betrag | Fundstelle |
> |---|---|---|---|
> | A | Baujahr 1995, Nutzung «selbst genutzt», Steuerwert (Verkehrswert gemäss Grundstückschätzung) | Steuerwert: Wert aus der Schätzung, er ist nicht in Ihrer Angabe | [Form. 7 S. 1](steuerwiki/chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0001.md) |
> | B a. | Eigenmietwert (Mietwert gemäss Grundstückschätzung) | 24'500 | [Form. 7 S. 1](steuerwiki/chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0002.md) |
> | B a. | abzüglich 20 % Selbstnutzungsabzug | − 4'900 | [Art. 11 Abs. 2 StV AR](steuerwiki/chunks/ar/2025/ar-stv/ar-stv__art-11.md), [MB 07](steuerwiki/chunks/ar/dauernd/ar-mb-07/ar-mb-07__c0003.md) |
> | B a. | Total anrechenbarer Eigenmietwert | 19'600 | wie oben |
> | B b. | Erträge Fremdnutzung | keine | – |
> | B | Total Erträge a. und b. | 19'600 | – |
> | C | Pauschalabzug (C1) ankreuzen: 20 % von 19'600 | 3'920 | [WL AR 2025 S. 32](steuerwiki/chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0175.md), [Art. 25 StV AR](steuerwiki/chunks/ar/2025/ar-stv/ar-stv__art-25.md) |
> | C | Tatsächliche Kosten und Rückseite (C2) | leer lassen | [Form. 7 S. 1–2](steuerwiki/chunks/ar/2025/ar-form-07-2025/ar-form-07-2025__c0003.md) |
> 
> Der Pauschalsatz ist 20 %, weil das Gebäude älter als 10 Jahre ist (1995). Das Alter bestimmt sich nach dem Vermögenssteuerstichtag. Die Bedingung «Bruttomietertrag des gesamten Liegenschaftsbesitzes höchstens CHF 100'000» ist erfüllt.
> 
> **Steuererklärung (eine Erklärung für Staats- und Gemeindesteuer)**
> 
> | Ziff. | Position | Betrag | Quelle des Übertrags |
> |---|---|---|---|
> | 5 (Seite 2, Code 712) | Ertrag aus Liegenschaften | 19'600 | Form. 7, Total Erträge a. und b. |
> | 15 (Seite 3) | Unterhalts- und Verwaltungskosten, Pauschalabzug | 3'920 | Form. 7, Abschn. C1 |
> | 31 (Seite 4, Code 710) | Liegenschaften, Steuerwert | Steuerwert aus Form. 7 Abschn. A | Form. 7, Abschn. A |
> 
> Netto wirkt die Liegenschaft damit mit 15'680 (19'600 − 3'920) im Einkommen. Ziff. 5 und 15 werden getrennt deklariert und nicht verrechnet.
> 
> **Annahmen und Prüfpunkte**
> - **Basis der Pauschale:** Die Wegleitung sagt «20 % vom Total Liegenschaftserträge», und das Formular rechnet «Pauschalabzug der Erträge (B)». Das Muster der Wegleitung bestätigt es: Mietwert 26'000, Abzug 5'200, Total 20'800, Pauschale 4'160, also 20 % von 20'800 ([WL AR 2025 S. 28](steuerwiki/chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0159.md), [c0160](steuerwiki/chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0160.md)). Ich habe das Muster so gelesen. Bei 24'500 als Basis wären es 4'900.
> - **Zuschlag 2,8 %:** Ich bin davon ausgegangen, dass 24'500 der Mietwert der Schätzung ist, vor dem 20-%-Abzug. Seit der Schätzung ausgeführte wertvermehrende Um- oder Anbauten erhöhen den Mietwert um 2,8 % der Aufwendungen ([Art. 11 Abs. 1 StV AR](steuerwiki/chunks/ar/2025/ar-stv/ar-stv__art-11.md)). Das wäre bei der Schätzung zu klären.
> - **Pauschale statt tatsächlicher Kosten:** Mit der Pauschale sind alle Kosten abgegolten, auch denkmalpflegerische ([WL AR 2025 S. 32](steuerwiki/chunks/ar/2025/ar-wl-2025/ar-wl-2025__c0175.md)). Das Wahlrecht gilt pro Gebäude und Jahr.
> - **Ziff. 15:** Den Code habe ich nicht verifiziert. Die Wiki-Daten sind für Ziff. 5 und 15 als 🟡 extrahiert geführt, die Sätze 20 % und 20 % als ☑️ agent-geprüft.
> - **Direkte Bundessteuer:** Das Wiki hat keine AR-Quelle zur Behandlung des Eigenmietwerts und der Pauschale bei der DBSt. Auf Bundesebene gilt gemäss Wiki ebenfalls 20 % für Gebäude über 10 Jahre ([Art. 5 LKV](steuerwiki/chunks/bund/2025/bund-lkv/bund-lkv__art-5.md)). Ob der Selbstnutzungsabzug beim Bund gleich wirkt, ist offen. Das habe ich nicht gerechnet.
> 
> Die fachliche Beurteilung bleibt bei SB/ML.

