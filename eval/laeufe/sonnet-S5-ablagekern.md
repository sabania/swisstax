# OpenClaw-Testlauf: ablage-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 8 · Lauf: 2026-11-09 19:55
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## a01

**Frage:** Per E-Mail kommt der «Lohnausweis 2025» der Muster AG für Hans Muster (Kanton Zürich). Ist das steuerrelevant? Welches Steuerjahr, muss er eingereicht werden, wie wird er abgelegt und in welche Position der Steuererklärung gehört der Nettolohn?

**Soll (Referenz):** Steuerrelevant ja. Steuerjahr 2025 (Bescheinigungsjahr). Einzureichen (ZH: Lohnausweise beilegen, zh-wl-2025__c0032; § 134 StG). → consis: Klasse StE, Kategorie «Belege eingereicht». Bezeichnung z.B. «Lohnausweis Muster AG». Nettolohn (Lohnausweis Ziff. 11) → ZH 2025 Ziff. 1.1 Haupterwerb, Code 100 (Person 1).

**Antwort des Agenten** (29.8 s · Tools: 4 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read, steuerwiki__position):

> **Kanton Zürich · Steuerjahr 2025**
> 
> **Steuerrelevant?** Ja. Der Lohnausweis (Formular 11) ist die Grundlage für das Haupteinkommen. Status im Wiki: ☑️ agent-geprüft, Abnahme offen. Das Wiki erkennt den Typ mit mittlerer Sicherheit. Prüfen Sie deshalb kurz, ob es wirklich ein Formular 11 ist und nicht z. B. eine Rentenbescheinigung.
> 
> **Steuerjahr:** 2025. Es gilt das Bescheinigungsjahr. Die Jahreszahl 2025 stammt aus Ihrer Angabe und aus der Dokumenterkennung. Prüfen Sie sie im Dokument selbst.
> 
> **Einreichen?** Ja, immer. Der Lohnausweis ist der Steuererklärung beizulegen, für jeden Arbeitgeber, auch bei Nebenerwerb (§ 134 Abs. 1 lit. a StG; Wegleitung ZH 2025 S. 31). Die Wegleitung sagt: «Bitte vergessen Sie nicht, Ihre Lohnausweise der Steuererklärung beizulegen.» (zh-wl-2025__c0032, ☑️).
> 
> **Ablage:** Kategorie **«Belege eingereicht»** (Spalte «Eingereicht?» = ja). Die Kategorienliste nennt «Lohnausweis» dort ausdrücklich («Direkt beim Ablegen; eingereicht: ja»).
> - Vorbehalt: Die Zuordnungen der Liste sind noch nicht bestätigt (Spalte «Bestätigt» leer).
> - Ablageregeln consis, ebenfalls zu bestätigen: Ein Beleg ist eine Datei. Beschreibung: «Lohnausweis Muster AG». Steuerjahr: 2025.
> 
> **Position für den Nettolohn:**
> - **Ziff. 1.1 «Haupterwerb unselbständig»** im Hauptformular (Form. 300), **Code 100** für Person 1 (Code 101 für Person 2).
> - **Wert:** Lohnausweis **Ziff. 11 Nettolohn**. Das ist Brutto (Ziff. 8) minus AHV/IV/EO/ALV/NBUV (Ziff. 9) minus BVG-Beiträge (Ziff. 10.1 und 10.2).
> - **Mehrere Haupterwerbe:** Die Ziff. 11 aller Haupterwerbe werden pro Person summiert.
> - **Bund:** Es gibt kein eigenes Bundesformular. Die Zeile gilt für Staats- und Bundessteuer, ohne Unterschied (zh-form-300-2025__c0004, ☑️).
> - Wenn Hans Muster neben der Muster AG weitere Arbeitgeber hat, gehören Nebenerwerbe in Ziff. 1.2.
> 
> **Zusätzlich aus dem Lohnausweis zu beachten:**
> - **Feld F** (unentgeltliche Beförderung oder Geschäftsfahrzeug): kein Fahrkostenabzug in Form. 360 Ziff. 1.
> - **Feld G** (Kantine oder Lunch-Checks): verbilligter Verpflegungsabzug, Code 206 (min(Arbeitstage × 7.50; 1'600)). Ohne Kreuz in Feld G gilt Code 208 (min(Arbeitstage × 15; 3'200)).
> - **Ziff. 10.2** (BVG-Einkauf): ist schon im Nettolohn abgezogen. Nicht nochmals in Ziff. 16.1 (Code 280) abziehen.
> - **Ziff. 13.3** (Weiterbildung durch den Arbeitgeber): gehört in Form. 367 unter «Beitrag Arbeitgeber».
> - **Ziff. 15** (Bemerkungen): Hier stehen z. B. Schichttage.
> - **Übrige Berufskosten** (Form. 360 Ziff. 3): pauschal 3 % des Nettolohns, mindestens CHF 2'000, höchstens CHF 4'000. Die Basis ist Ziff. 11.
> - **Erwerbslücken** (z. B. Arbeitslosigkeit oder Krankheit): in der Steuererklärung bezeichnen und belegen.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## a02

**Frage:** Ein Kunde lädt eine Migros-Kassenquittung und eine Swisscom-Handyrechnung hoch. Wie werden sie behandelt?

**Soll (Referenz):** Nicht steuerrelevant (private Alltagsrechnungen, kein Wert in der Steuererklärung). Nicht als Steuerbeleg ablegen; Grund nennen (z.B. zur Prüfung markieren oder dem Mandanten zurückmelden). Handyrechnung nur bei nachgewiesener beruflicher Nutzung allenfalls Berufskosten – als Rückfrage.

**Antwort des Agenten** (26.6 s · Tools: 3 Aufrufe read, steuerwiki__ablage):

> **Ohne Kanton · Steuerjahr 2025 (nicht angegeben, Standardjahr; bei Quittungen gilt eigentlich das Belegjahr)**
> 
> Beide Belege werden gleich behandelt: Sie sind nicht steuerrelevant und kommen in keine Steuerbeleg-Kategorie.
> 
> | Dokument | Typ (Erkennung) | Steuerrelevant? | Ablage |
> |---|---|---|---|
> | Migros-Kassenquittung | Private Alltagsrechnung (Lebensmittel), Sicherheit mittel | nein | keine Kategorie aus `KATEGORIEN.md` |
> | Swisscom-Handyrechnung | Private Alltagsrechnung (Telefon/Internet), Sicherheit mittel | nein | keine Kategorie aus `KATEGORIEN.md` |
> 
> **Begründung:**
> - Lebenshaltungskosten sind nicht abziehbar. Grundlage ist Art. 34 lit. a DBG: «die Aufwendungen für den Unterhalt des Steuerpflichtigen und seiner Familie».
> - Fundstelle: `bund-dbg-2025__art-34` (☑️ agent-geprüft, Abnahme offen).
> - Die Belege haben keinen Wert in der Steuererklärung. Deshalb passen weder «Belege eingereicht» noch «Belege Sonstiges». Die Liste nennt sie nicht, und eine Ähnlichkeit zu einem Listenbeispiel reicht nicht.
> - Ein Kanton ist für diese Einordnung nicht nötig. Die Beurteilung ist bei Bund und Kantonen dieselbe, und eine Einreichepflicht entfällt.
> 
> **Zur Swisscom-Rechnung:** Das Tool hat zusätzlich schwach das ÖV-Abonnement als Möglichkeit genannt (1 Punkt gegen 8). Das ist nur eine Erkennungsunsicherheit, die Rechnung ist keine ÖV-Rechnung. Ob ein Teil der Rechnung beruflich bedingt ist, habe ich nicht geprüft. Das lässt sich nur mit Angaben zum Kunden und seinem Wohnsitzkanton am 31.12. beurteilen. Falls der Kunde dazu etwas sagt, kläre ich es nach.
> 
> **Praktisch:** Beide Belege dem Kunden zurückgeben oder als «kein Steuerbeleg» markieren und nicht in die Steuerakte legen. Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## a03

**Frage:** Ein Kunde schickt ein Sammel-PDF mit Lohnausweis 2025, Bescheinigung Säule 3a 2025, Prämienübersicht Krankenkasse 2025 und Kita-Rechnungen 2025 (Kanton St. Gallen). Wie werden die Dokumente abgelegt?

**Soll (Referenz):** Sammel-PDF trennen: ein Beleg = eine Datei. Steuerjahr 2025. Lohnausweis → einzureichen (consis: Belege eingereicht). Säule 3a → einzureichen (consis: Belege eingereicht). Krankenkassenprämien → SG 2025 nur auf Verlangen (sg-wl-2025__c0073) → nicht einzureichen (consis: Belege Sonstiges). Kita-Rechnungen → SG 2025 nicht einzureichen bzw. auf Verlangen → Belege Sonstiges; steuerrelevant bedingt (nur bei Erwerbstätigkeit/Ausbildung, Kind unter 14).

**Antwort des Agenten** (29.8 s · Tools: 5 Aufrufe read, steuerwiki__ablage):

> **Kanton St. Gallen · Steuerjahr 2025**
> 
> Zuerst das Sammel-PDF trennen, denn nach den Ablageregeln gilt: ein Beleg = eine Datei. Beschreibung jeweils «Dokumentart + Aussteller». Die Einordnung beruht nur auf den Titeln, nicht auf dem Inhalt der Dokumente.
> 
> | Dokument | Steuerrelevant | Einreichen (SG 2025) | Kategorie |
> |---|---|---|---|
> | **Lohnausweis 2025** | ja | ja, immer, pro Arbeitgeber einer (`sg-stg-2025__art-169`) | **Belege eingereicht** (die Liste nennt den Lohnausweis ausdrücklich) |
> | **Bescheinigung Säule 3a 2025** (Form. 21 EDP) | ja | ja, bei Abzug Ziff. 13.1 (`sg-form-1-2025__c0008`) | **Belege eingereicht** (die Liste nennt sie ausdrücklich) |
> | **Prämienübersicht Krankenkasse 2025** | ja (Ziff. 14, Form. 6 Teil A) | nur auf Verlangen (`sg-wl-2025__c0073`) | **Belege Sonstiges** (Liste: «Versicherungsprämien, sofern nicht einzureichen») |
> | **Kita-Rechnungen 2025** | bedingt (Ziff. 16.2) | nur auf Verlangen. Formular 10 wird ausgefüllt, die Rechnungen nur auf Anfrage (`sg-wl-2025__c0092`) | **Belege Sonstiges** (Liste: «Kinderbetreuungskosten, sofern nicht einzureichen») |
> 
> **Zu den Kita-Rechnungen:**
> - Der Abzug gilt nur für Kinder unter 14 Jahren im gleichen Haushalt. Die Kosten müssen mit Erwerbstätigkeit, Ausbildung oder Ähnlichem zusammenhängen. Das ist beim Kunden zu prüfen.
> - Der Höchstabzug beträgt Fr. 26'700 pro Kind (`sg-wl-2025__c0092`).
> - Falls die Prämienübersicht zusätzlich Leistungsabrechnungen oder Selbstbehalte enthält, ist das ein eigener Belegtyp (Krankheitskosten, Ziff. 21.1). Er ist nur relevant, wenn Krankheitskosten geltend gemacht werden. Dann wäre er bei Verweis im Formular 6 einzureichen (**Belege eingereicht**), sonst **Belege Sonstiges**.
> 
> **Vorbehalte:**
> - Alle Zuordnungen der Liste sind laut `KATEGORIEN.md` noch nicht von consis bestätigt. Auch die Wiki-Einstufungen sind erst agent-geprüft, die Abnahme steht aus.
> - Die Typerkennung ist nur «mittel» sicher. Prüfen Sie Typ und Bescheinigungsjahr am Dokument selbst.
> - Bei mehreren Kita-Rechnungen sagt die Ablageregel nicht, ob jede Rechnung eine eigene Datei bekommt. Ich würde pro Rechnung oder pro Kita-Jahresübersicht trennen. Das ist nicht belegt und sollte mit consis geklärt werden.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## a04

**Frage:** Wie werden (a) eine Bestätigung der Fristerstreckung für die Steuererklärung 2025 und (b) die E-Mail-Antwort eines Kunden auf Rückfragen abgelegt?

**Soll (Referenz):** (a) → consis: Klasse StE, Kategorie «Fristenliste NP». (b) Korrespondenz des Mandanten → consis: Klasse StE, Kategorie «Unterlagen Kunde». Beide werden nicht eingereicht.

**Antwort des Agenten** (24.8 s · Tools: 3 Aufrufe read, steuerwiki__ablage):

> Kanton: nicht angegeben, für die Ablage aber nicht nötig. Steuerjahr: 2025, so von Ihnen genannt. Die Kategorien stammen aus `KATEGORIEN.md` (consis, Stand 05.11.2026).
> 
> **(a) Bestätigung der Fristerstreckung für die Steuererklärung 2025**
> - **Kategorie:** «Fristenliste NP». Die Liste nennt die Dokumentart ausdrücklich: «Fristerstreckungsgesuch / Bestätigung Fristerstreckung NP (Einzel- oder Sammelgesuch, Bestätigung des Steueramts)».
> - **Steuerrelevant als Beleg:** nein. Es ist ein Dokument des Steuerverfahrens und hat keinen Wert in der Steuererklärung.
> - **Eingereicht:** nein.
> - **Steuerjahr:** 2025. Die Erkennung nimmt die Jahreszahl aus Ihrer Anfrage.
> - **Nicht ablegen unter:** «Belege eingereicht» oder «Belege Sonstiges». Die Kategorie «Fristenliste NP» ist nur für Fristenkontrolle und Fristerstreckung gedacht, nicht für Belege.
> - **Vorbehalt:** Die Zuordnung in der Liste ist noch nicht von consis bestätigt (Spalte «Bestätigt» leer). Die Erkennung des Dokumenttyps ist «mittel» sicher.
> 
> **(b) E-Mail-Antwort eines Kunden auf Rückfragen**
> - **Kategorie:** «Unterlagen Kunde». Die Liste nennt ausdrücklich «Antworten des Kunden auf Fragen / Pendenzen (z. B. per E-Mail)».
> - **Steuerrelevant als Beleg:** nein. Es ist kein Steuerbeleg. Der Inhalt dient der Erfassung der Steuererklärung.
> - **Eingereicht:** nein.
> - **Steuerjahr:** 2025. Die Erkennung nimmt die Jahreszahl aus Ihrer Anfrage.
> - **Beilagen zur E-Mail:** Hängt der Kunde echte Belege an, etwa einen Lohnausweis oder eine Bescheinigung Säule 3a, legen Sie jeden Beleg als eigene Datei in seiner eigenen Kategorie ab. Das folgt der Regel «ein Beleg = eine Datei». Welche Kategorie das ist, hängt von der Einreichepflicht ab. Die E-Mail selbst bleibt unter «Unterlagen Kunde».
> - **Abgrenzung:** Ein Schreiben des Steueramts mit Nachfragen oder Auflagen gehört nicht hierher. Dafür gibt es die Klasse «Auflage/Buchprüfung». Sie steht in `KATEGORIEN.md` unter «Weitere Klassen» und ist von consis noch zu bestätigen.
> - **Vorbehalt:** Die Zuordnung ist ebenfalls noch nicht von consis bestätigt.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## a05

**Frage:** Kanton Zürich, Steuerjahr 2025: Kita-Rechnungen von CHF 14'000 für ein 5-jähriges Kind, beide Eltern erwerbstätig. In welche Position (Ziffer/Code) gehört das, welcher Höchstbetrag gilt beim Kanton und beim Bund, und wie werden die Rechnungen abgelegt?

**Soll (Referenz):** ZH 2025 Ziff. 16.6 «Abzug für fremdbetreute Kinder» (Code 376): je Kind unter 14 Jahren nachgewiesene Kosten, höchstens Kanton CHF 25'000 / Bund CHF 25'800 → CHF 14'000 in beiden Spalten (Verpflegung nicht abziehbar). Ablage: ZH 2025 Kinderdrittbetreuungskosten nur auf Verlangen nachzuweisen (zh-zstb-34-1-bis-2025__c0023) → → consis: Belege Sonstiges.

**Antwort des Agenten** (30.2 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__beleg, steuerwiki__wert, read, steuerwiki__rechne):

> **Kanton Zürich · Steuerjahr 2025**
> 
> **Position:** Ziff. 16.6 «Abzug für fremdbetreute Kinder (Jahrg. 2011–2025)», **Code 376**. Dieselbe Zeile gilt für Staats- und Bundessteuer. Die Beträge stehen in den Spalten «Staatssteuer» und «Bundessteuer». (Fundstelle: zh-form-300-2025__c0008; ☑️ agent-geprüft, Abnahme offen)
> 
> **Höchstbetrag je Kind:**
> - **Kanton:** CHF 25'000 (§ 31 Abs. 1 lit. j StG ZH, zh-stg-2025__par-31-t4; ☑️).
> - **Bund:** CHF 25'800 (Art. 33 Abs. 3 DBG, bund-dbg-2025__art-33-t7; ☑️).
> - Die Altersgrenze liegt bei beiden unter 14 Jahren. Ein 5-jähriges Kind (Jahrgang 2020) fällt darunter.
> 
> **Ihr Fall:** Die CHF 14'000 liegen unter beiden Limiten. Es gilt also `min(14'000; 25'000)` = 14'000 beim Kanton und `min(14'000; 25'800)` = 14'000 beim Bund. Die Rechnung wurde mit dem Rechentool geprüft. In beiden Spalten wird der volle Betrag eingetragen, vorausgesetzt:
> - **Haushalt:** Das Kind lebt im gleichen Haushalt wie die Eltern.
> - **Erwerbstätigkeit:** Die Betreuung steht im direkten Zusammenhang mit der Erwerbstätigkeit. Bei zwei erwerbstätigen Eltern ist das erfüllt.
> - **Verpflegung:** Sie ist Lebenshaltung und nicht abziehbar (Bund KS 30 Ziff. 8.5, bund-ks-30__c0044). Die CHF 14'000 müssen deshalb reine Betreuungskosten sein. Weisen die Kita-Rechnungen Verpflegung separat aus, ist der Betrag entsprechend zu kürzen. Das gilt ebenso für Beträge, die Ihnen die Kita als Subvention oder Betreuungsgutschein vergütet hat.
> - **Verheiratete Eltern:** Es gilt der Abzug je Kind in voller Höhe. Die hälftige Regel (Kanton 12'500 / Bund 12'900 je Elternteil) betrifft nur Konkubinatspaare mit gemeinsamer Sorge. Ob das Paar verheiratet ist oder im Konkubinat lebt, geht aus der Frage nicht hervor. Bitte klären.
> 
> **Ablage (KATEGORIEN.md):** Kategorie **«Belege Sonstiges»** (Eingereicht? = nein).
> - Die Liste nennt «Kinderbetreuungskosten (Sofern nicht einzureichen)» ausdrücklich.
> - In ZH sind die Rechnungen nur **auf Verlangen** nachzuweisen (zh-zstb-34-1-bis-2025__c0023: «auf Verlangen der Steuerbehörden hinreichend nachzuweisen»).
> - Das Wiki verweist zusätzlich auf Ziff. 16.6, WL S. 31, wonach die Aufstellung der bezahlten Kosten mit Empfängern unaufgefordert beizulegen ist. Diese Aufstellung geht mit der Steuererklärung ein, die Rechnungen selbst bleiben in der Ablage.
> - Die Zuordnung in der Kategorienliste ist laut deren Kopf noch nicht von der Firma bestätigt.
> - Ablageregeln: Ein Beleg = eine Datei. Beschreibung: «Kita-Rechnung [Name der Kita]». Steuerjahr: 2025. Zahlungsnachweise und die Jahresbescheinigung der Kita (Betreuung und Verpflegung getrennt) dazulegen.
> 
> **Hinweis:** Die ZH-Verordnung VKP ab 2024 nennt noch CHF 10'400. Dieser Wert ist für 2025 überholt. Gesetz und Wegleitung der Jahresfassung nennen CHF 25'000 (zh-vkp-2024-zstb__c0005 vs. zh-stg-2025__par-31-t4). Die abschliessende fachliche Beurteilung bleibt bei der Fachperson.

## a06

**Frage:** Kanton Thurgau, Steuerjahr 2025: Es liegt ein Steuerauszug der Bank vor. Welche Formularpositionen füllt er, und wird er eingereicht (Ablage)?

**Soll (Referenz):** TG 2025: Formular 2 (Wertschriftenverzeichnis) → Ziff. 4 Wertschriften- und Zinserträge (Code 150), Ziff. 30.1 Wertschriften und Guthaben (Code 410), Verrechnungssteueranspruch 35 % von Total A. Einreichen bedingt: wenn die Titel nicht einzeln im Formular 2, sondern mit dem Steuerauszug deklariert werden (tg-wl-2025__c0168) → dann «einzureichen» (consis: Belege eingereicht), sonst «nicht einzureichen» (Belege Sonstiges).

**Antwort des Agenten** (26.9 s · Tools: 3 Aufrufe steuerwiki__beleg, steuerwiki__ablage, read):

> **Thurgau · Steuerjahr 2025 · Steuerauszug der Bank (eSteuerauszug eingeschlossen)**
> 
> Der Steuerauszug ist steuerrelevant (☑️ agent-geprüft, Abnahme offen).
> 
> ## Formularpositionen (TG 2025)
> | Position | Inhalt | Aus dem Steuerauszug |
> |---|---|---|
> | **Form. 2, Spalten 7–9** | Detailverzeichnis Wertschriften und Guthaben | Steuerwert 31.12.2025 (Sp. 7), Bruttoertrag mit Verrechnungssteuer (Sp. 8, Kolonne A), ohne Verrechnungssteuer (Sp. 9, Kolonne B) |
> | **Ziff. 4** (Form. 1, Code 150) | Wertschriften- und Zinserträge | Übertrag aus Form. 2. Rechnung: Ziff. 15 (Bruttoertrag A+B) − Ziff. 16 Geschäftserträge − Ziff. 17 Verwaltungskosten (2 Promille, max. CHF 6'000) − Ziff. 18 Einsatzkosten |
> | **Ziff. 30.1** (Form. 1, Code 410) | Wertschriften und Guthaben (Vermögen) | Übertrag aus Form. 2. Rechnung: Zwischentotal Steuerwerte − Geschäftswertschriften = Total Steuerwert Privatvermögen (Ziff. 9) |
> | **Form. 2, Ziff. 10** | Verrechnungssteueranspruch | 35 % × Summe Bruttoerträge Sp. 8 (Rückerstattungsantrag) |
> | **Ziff. 15.6** (Code 341) und **Hilfsblatt qualifizierte Beteiligungen** | Teilbesteuerungsabzug | Nur bei Beteiligungen ab 10 % im Privatvermögen. Abzug: Kanton 40 % / Bund 30 % der Beteiligungserträge |
> 
> Limiten und Hinweise zu Ziff. 4:
> - Steuerfreier Kleingewinn: Kanton CHF 1'000, Bund CHF 1'100.
> - Steuerfreier Grossspielgewinn: Kanton CHF 1'000'000, Bund CHF 1'070'400.
> - Die kantonale Erklärung deckt Kanton und Bund ab. Es gibt kein separates Bundesformular.
> 
> Details je Ziffer (Regeln, Beachten, Fundstelle) liefert `position tg 2025 <ziffer>`. Ausser dem Zitat zu Ziff. 4 habe ich keine Chunks im Wortlaut geöffnet.
> 
> ## Einreichen
> **Bedingt.** Der Steuerauszug muss eingereicht werden, wenn die Titel im Wertschriften- und Guthabenverzeichnis nicht einzeln, sondern als Total gemäss Steuerauszug deklariert werden. Er ist dann Bestandteil des Verrechnungssteuerantrags.
> - Fundstellen: tg-wl-2025__c0036 und tg-wl-2025__c0168.
> - Werden die Titel einzeln in Form. 2 erfasst, besteht keine Einreichepflicht.
> 
> ## Ablage (KATEGORIEN.md)
> Die Liste nennt «Bank-/Depotauszüge, Steuerverzeichnis» ausdrücklich. Die Zuordnung hängt vom Kanton ab:
> - **Totale aus dem Steuerauszug deklariert → «Belege eingereicht»** (Eingereicht? = ja).
> - **Titel einzeln erfasst, Auszug nur Nachweis → «Belege Sonstiges»** (Eingereicht? = nein).
> 
> Welcher Fall vorliegt, kann ich aus der Anfrage nicht ablesen. Das hängt davon ab, wie das Wertschriftenverzeichnis ausgefüllt wird. Wenn Ziff. 4 und Ziff. 30.1 als Totale aus dem Auszug kommen, gilt «Belege eingereicht».
> 
> Die Zuordnungen in KATEGORIEN.md sind von consis noch nicht bestätigt. Die fachliche Beurteilung bleibt bei der Fachperson.

## a07

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Hypothekarzinsbescheinigung der Bank. Welche Ziffern betrifft sie und wie wird sie abgelegt?

**Soll (Referenz):** AR 2025: Formular 5 Teil A (private Schulden 31.12.2025 und Schuldzinsen 2025) → Ziff. 11 Schuldzinsen privat und Ziff. 34.1 Privatschulden (Code 504). Belege zum Schuldenverzeichnis nur auf Verlangen (ar-form-05-2025__c0001) → → consis: Belege Sonstiges.

**Antwort des Agenten** (29.7 s · Tools: 7 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read, steuerwiki__position):

> **AR · Steuerjahr 2025: Hypothekarzinsbescheinigung der Bank**
> 
> Die Bescheinigung ist steuerrelevant (Belegtyp `hypothekarbestaetigung`). Der Status ist ☑️ agent-geprüft, die Abnahme ist noch offen. Die Erkennung des Typs ist nur mittelsicher, weil auch ein Steuerauszug der Bank in Frage käme. Prüfen Sie am Dokument, ob Zinsen und Schuldsaldo aufgeführt sind.
> 
> **Betroffene Ziffern**
> 
> | Ziffer | Inhalt | Was aus dem Beleg übertragen wird |
> |---|---|---|
> | **Ziff. 11** (Abzüge, Seite 3) | Private Schuldzinsen | Die 2025 bezahlten Zinsen, ohne Amortisationen. Der Code ist nicht verifiziert (ar-form-05-2025__c0001). |
> | **Ziff. 34.1** (Vermögen, Code 504) | Privatschulden | Der Saldo per 31.12.2025 je Gläubiger (ar-form-05-2025__c0001, ar-wl-2025__c0121). |
> | **Formular 5 Teil A** | Schuldenverzeichnis | Gläubiger, Schuld per 31.12.2025 und Zinsen 2025. Die Summen gehen in Ziff. 34.1 und Ziff. 11 (ar-form-05-2025__c0001). |
> 
> - **Ziff. 34.2 (Geschäftsschulden, Code 506, Formular 5 Teil B):** Sie betrifft die Bescheinigung nur bei Selbständigerwerb oder Geschäftsvermögen. Geschäftliche Schuldzinsen gehören in die Jahresrechnung und nicht in Ziff. 11 (ar-form-05-2025__c0002).
> - **Rechenregel Ziff. 11, Kanton:** Abziehbar ist das Minimum aus den bezahlten Schuldzinsen und den Erträgen aus Ziff. 4 (ohne Lotteriegewinne) plus Ziff. 5 plus CHF 50'000.
> - **Bund:** Das AR-Formular hat keine Bundesspalte. Die Steuerverwaltung nimmt die Abweichungen für die direkte Bundessteuer automatisch vor (ar-wl-2025__c0179). Die Grenze (Vermögenserträge plus CHF 50'000) steht nur im Kantonsformular. Sie ist aus den AR-Quellen nicht belegt, also nicht geprüft.
> - **Baukreditzinsen:** Sie sind in AR im Gegensatz zu SG abzugsfähig (WL AR 2025 Ziff. 11, ar-wl-2025__c0081).
> - **Amortisationen:** Sie sind nicht abziehbar. Trennen Sie sie auf der Bescheinigung vom Zinsbetrag.
> 
> **Einreichen**
> 
> Die Belege zum Schuldenverzeichnis sind in AR **auf Verlangen** einzureichen (ar-form-05-2025__c0001). Der Chunk ist durch Formularfelder unterbrochen. Ich lese «auf Verlangen» daraus, weil der Vermerk nicht ganz zusammenhängend steht.
> 
> **Ablage nach KATEGORIEN.md**
> 
> - **Kategorie: «Belege Sonstiges»** (Eingereicht? = nein).
> - Die Liste nennt die «Hypothekarzinsbescheinigung» ausdrücklich. Sie gehört gemäss Wegleitung des Kantons in «Belege eingereicht», wenn sie einzureichen ist, sonst in «Belege Sonstiges». Da AR die Belege nur auf Verlangen verlangt, ist es «Belege Sonstiges».
> - Die Zuordnung in der Liste ist noch nicht von consis bestätigt.
> - **Beschreibung:** Dokumentart plus Aussteller, zum Beispiel «Hypothekarzinsbescheinigung Muster Bank».
> - **Steuerjahr:** 2025, das Bescheinigungsjahr. Ein Beleg ergibt eine Datei. Sammel-PDFs sind zu trennen.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## a08

**Frage:** Es kommt ein Kontoauszug des Steueramts St. Gallen zum Steuerkonto (Zahlungen und Saldo der Staats- und Gemeindesteuern). Wie wird er abgelegt?

**Soll (Referenz):** Kein Steuerbeleg und kein Bank-Kontoauszug: → consis: Klasse «Kontoauszug» (nicht Klasse StE). Kein Wert in der Steuererklärung.

**Antwort des Agenten** (22.7 s · Tools: 2 Aufrufe read, steuerwiki__ablage):

> **SG · Steuerjahr 2025** (kein Jahr genannt, daher 2025 angenommen; bitte das Jahr auf dem Auszug prüfen)
> 
> **Ablage: Klasse «Kontoauszug»** (Bereich Steuern, Klasse «Kontoauszug des Steueramts (Steuerkonto) – nicht Bank-Kontoauszug»).
> 
> - **Keine Steuerbeleg-Kategorie.** Weder «Belege eingereicht» noch «Belege Sonstiges» passt. Der Auszug ist ein Dokument des Steuerverfahrens (Zahlungen, Saldo, Zinsen des Steuerkontos) und hat keinen Wert in der Steuererklärung. Er ist daher nicht steuerrelevant als Beleg.
> - **Nicht einreichen.** Der Auszug geht nicht mit der Deklaration an das Steueramt.
> - **Beschreibung:** «Kontoauszug Steueramt St. Gallen» (Dokumentart + Aussteller, wie in den Ablageregeln).
> - **Steuerjahr:** Das ist die Steuerperiode, auf die sich der Auszug bezieht. Deckt er mehrere Perioden ab, bitte nach Jahr trennen oder dem Hauptjahr zuordnen. Ein Beleg entspricht einer Datei.
> 
> **Vorbehalte:**
> - «Kontoauszug» steht nicht in der Kategorienliste der Firma (Tabelle). Die Zuordnung stammt aus dem Prozessbeschrieb vom 27.10.2026 und ist von consis noch zu bestätigen.
> - Das Wiki liefert für diesen Typ keine Fundstelle. Die Einordnung beruht auf der Typerkennung (Sicherheit hoch).

