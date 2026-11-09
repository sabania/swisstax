# OpenClaw-Testlauf: ablage-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 8 · Lauf: 2026-11-09 17:27
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## a01

**Frage:** Per E-Mail kommt der «Lohnausweis 2025» der Muster AG für Hans Muster (Kanton Zürich). Ist das steuerrelevant? Welches Steuerjahr, muss er eingereicht werden, wie wird er abgelegt und in welche Position der Steuererklärung gehört der Nettolohn?

**Soll (Referenz):** Steuerrelevant ja. Steuerjahr 2025 (Bescheinigungsjahr). Einzureichen (ZH: Lohnausweise beilegen, zh-wl-2025__c0032; § 134 StG). → consis: Klasse StE, Kategorie «Belege eingereicht». Bezeichnung z.B. «Lohnausweis Muster AG». Nettolohn (Lohnausweis Ziff. 11) → ZH 2025 Ziff. 1.1 Haupterwerb, Code 100 (Person 1).

**Antwort des Agenten** (29.6 s · Tools: 4 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read, steuerwiki__position):

> **Lohnausweis 2025, Muster AG, Hans Muster (Kanton ZH)**
> 
> **Steuerrelevant: ja.** Der Lohnausweis (Formular 11) ist die Einkommensbescheinigung für das unselbständige Einkommen. Status ☑️ agent-geprüft, Abnahme durch die Fachperson offen.
> 
> **Steuerjahr: 2025.** Es gilt das Bescheinigungsjahr. «2025» im Titel stimmt mit der häufigsten Jahreszahl im Text überein, ich habe das Jahr aber nicht am Dokument selbst geprüft. Bitte kurz kontrollieren.
> 
> **Einreichen: ja.**
> - Der Lohnausweis ist der Steuererklärung immer beizulegen, für jeden Arbeitgeber, auch bei Nebenerwerb.
> - Fundstelle: § 134 Abs. 1 lit. a StG, Wegleitung ZH 2025 S. 31, Chunk `zh-wl-2025__c0032`. Dort steht: «Bitte vergessen Sie nicht, Ihre Lohnausweise der Steuererklärung beizulegen.»
> 
> **Ablage: Kategorie «Belege eingereicht»** (Zeile «Eingereicht?» = ja).
> - KATEGORIEN.md nennt «Lohnausweis (Direkt beim Ablegen; eingereicht: ja)» ausdrücklich.
> - Vorbehalt: Die Zuordnungen der Liste sind laut Datei noch nicht bestätigt.
> - Beschreibung nach Ablageregel: «Lohnausweis Muster AG», Steuerjahr 2025.
> - Ein Beleg entspricht einer Datei. Die E-Mail-Anhänge also trennen und nur den Lohnausweis hier ablegen.
> 
> **Position für den Nettolohn: Ziff. 1.1 «Haupterwerb unselbständig», Code 100 (Person 1).**
> - Ins Feld kommt Ziff. 11 des Lohnausweises, der Nettolohn. Der Nettolohn ist Ziff. 8 (Bruttolohn) minus Ziff. 9 und 10.
> - Kanton und Bund stehen in derselben Zeile (Staats- und Bundessteuer ohne Unterschied).
> - Ist die Muster AG nicht der Haupterwerb, sondern ein Nebenerwerb, gehört der Betrag in Ziff. 1.2.
> - Quelle: `zh-form-300-2025__c0004` (Haupterwerb Person 1, Lohnausweis, Code 100).
> 
> **Auf dem Lohnausweis zusätzlich prüfen:**
> - **Ziff. 10.2 (BVG-Einkauf):** Er ist im Nettolohn schon abgezogen. Er darf nicht nochmals unter Ziff. 16.1 (Code 280) abgezogen werden.
> - **Feld F angekreuzt** (unentgeltliche Beförderung oder Geschäftsfahrzeug): Dann gibt es keinen Fahrkostenabzug in Form. 360 Ziff. 1.
> - **Feld G angekreuzt** (Kantine oder Lunch-Checks): Dann gilt der Verpflegungsabzug «verbilligt», Form. 360 Ziff. 2.1, Code 206. Das sind CHF 7.50 pro Tag, maximal CHF 1'600 pro Jahr. Ohne Kreuz gilt Code 208 mit CHF 15 pro Tag, maximal CHF 3'200.
> - **Ziff. 13.3** (Arbeitgeberbeitrag an Weiterbildung): gehört in Form. 367 als «Beitrag Arbeitgeber».
> - **Ziff. 15** (Bemerkungen, z. B. Schichttage): Grundlage für Form. 360 Ziff. 2.2.
> - **Übrige Berufskosten (Form. 360 Ziff. 3):** Der Pauschalabzug beträgt 3 % des Nettolohns, mindestens CHF 2'000 und höchstens CHF 4'000 (Code 212). Der konkrete Betrag hängt vom Wert in Ziff. 11 ab. Den rechne ich, sobald ich die Zahl habe.
> - **Erwerbslücken** (z. B. Arbeitslosigkeit, Krankheit) müssen in der Steuererklärung ausdrücklich bezeichnet werden.
> 
> Schicken Sie mir die Beträge aus dem Lohnausweis (Ziff. 8–11, Felder F und G, Ziff. 13 und 15), dann rechne ich die Abzüge durch.

## a02

**Frage:** Ein Kunde lädt eine Migros-Kassenquittung und eine Swisscom-Handyrechnung hoch. Wie werden sie behandelt?

**Soll (Referenz):** Nicht steuerrelevant (private Alltagsrechnungen, kein Wert in der Steuererklärung). Nicht als Steuerbeleg ablegen; Grund nennen (z.B. zur Prüfung markieren oder dem Mandanten zurückmelden). Handyrechnung nur bei nachgewiesener beruflicher Nutzung allenfalls Berufskosten – als Rückfrage.

**Antwort des Agenten** (26.0 s · Tools: 3 Aufrufe steuerwiki__ablage, read):

> Beide Dokumente werden gleich behandelt: **nicht steuerrelevant, nicht ablegen.**
> 
> | | Migros-Kassenquittung | Swisscom-Handyrechnung |
> |---|---|---|
> | Dokumenttyp | Private Alltagsrechnung (Lebensmittel, Detailhandel) | Private Alltagsrechnung (Telefon/Internet) |
> | Steuerrelevant? | **Nein** | **Nein** |
> | Wert in der Steuererklärung | Keiner | Keiner |
> | Einreichen? | Nein | Nein |
> | Kategorie in `KATEGORIEN.md` | **Keine.** Weder «Belege eingereicht» noch «Belege Sonstiges». | **Keine.** Weder «Belege eingereicht» noch «Belege Sonstiges». |
> 
> **Grund:** Lebenshaltungskosten sind nicht abziehbar. Art. 34 lit. a DBG schliesst «die Aufwendungen für den Unterhalt des Steuerpflichtigen und seiner Familie» vom Abzug aus (Fundstelle: `bund-dbg-2025__art-34`, Status ☑️ agent-geprüft, Abnahme offen). Das gilt für Lebensmittel und für das private Handy gleichermassen.
> 
> **Wichtig bei der Ablage:** Beide Beispiele klingen ähnlich wie Einträge unter «Belege Sonstiges», etwa «Andere Nachweise zu Werten in der Deklaration». Diese Zeile greift hier nicht. Sie gilt nur für Belege, die in der Deklaration einen Wert haben. Die beiden Dokumente nicht dort einsortieren.
> 
> **Praktisch:**
> - Dem Kunden kurz mitteilen, dass die Dokumente für die Steuererklärung nicht benötigt werden.
> - Wenn sie nicht ausnahmsweise für etwas anderes gebraucht werden, nicht in der Klasse StE ablegen.
> 
> **Vorbehalte:**
> - Die Einstufung beruht auf den Dokumenttiteln. Die Erkennungssicherheit des Tools ist «mittel», und ich habe die Dokumente selbst nicht gesehen.
> - Kanton und Steuerjahr sind nicht angegeben. Das ändert hier nichts, weil die Nichtabziehbarkeit Bundesrecht ist und für alle Kantone gilt.
> - **Ausnahme Handy:** Nutzt der Kunde das Handy **geschäftlich**, etwa als Selbständigerwerbender oder mit einem Anteil für den Beruf, kann der berufliche Teil relevant sein. Dann müsste man nach Kanton und Jahr prüfen. Bei einer reinen Privatrechnung gilt das nicht.
> - Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> ---
> 
> Nebenbei: Ich bin neu hier als dein Assistent. Wie möchtest du mich nennen?

## a03

**Frage:** Ein Kunde schickt ein Sammel-PDF mit Lohnausweis 2025, Bescheinigung Säule 3a 2025, Prämienübersicht Krankenkasse 2025 und Kita-Rechnungen 2025 (Kanton St. Gallen). Wie werden die Dokumente abgelegt?

**Soll (Referenz):** Sammel-PDF trennen: ein Beleg = eine Datei. Steuerjahr 2025. Lohnausweis → einzureichen (consis: Belege eingereicht). Säule 3a → einzureichen (consis: Belege eingereicht). Krankenkassenprämien → SG 2025 nur auf Verlangen (sg-wl-2025__c0073) → nicht einzureichen (consis: Belege Sonstiges). Kita-Rechnungen → SG 2025 nicht einzureichen bzw. auf Verlangen → Belege Sonstiges; steuerrelevant bedingt (nur bei Erwerbstätigkeit/Ausbildung, Kind unter 14).

**Antwort des Agenten** (32.7 s · Tools: 5 Aufrufe read, steuerwiki__ablage):

> Das Sammel-PDF wird in vier Dokumente getrennt (ein Beleg = eine Datei). Steuerjahr ist bei allen 2025, Kanton SG. Die Kategorien stammen aus `KATEGORIEN.md` und sind dort noch nicht bestätigt.
> 
> | Dokument | Kategorie | Beschreibung | Einreichen in SG 2025 |
> |---|---|---|---|
> | Lohnausweis 2025 | **Belege eingereicht** | «Lohnausweis <Arbeitgeber>» | Ja, immer. Pro Arbeitgeber ein Lohnausweis (`sg-stg-2025__art-169`). Formular 1, Ziff. 1.1/1.2. |
> | Bescheinigung Säule 3a 2025 | **Belege eingereicht** | «Bescheinigung Säule 3a <Stiftung/Bank>» | Ja, bei Abzug Säule 3a (`sg-form-1-2025__c0008`). Formular 1, Ziff. 13.1. |
> | Prämienübersicht Krankenkasse 2025 | **Belege Sonstiges** | «Prämienbescheinigung <Krankenkasse>» | Nur auf Verlangen (`sg-wl-2025__c0073`). Ziff. 14, Formular 6 Teil A. |
> | Kita-Rechnungen 2025 | **Belege Sonstiges** | «Kita-Rechnung <Kita>» | Nur auf Verlangen (`sg-wl-2025__c0073`). Ziff. 16.2, Formular 10. |
> 
> Die Wiki-Einstufung der Dokumenttypen hat bei allen vier Status ☑️ (Fundstelle geprüft, Abnahme offen). Bei Lohnausweis, 3a und Krankenkasse ist die Erkennung «mittel» sicher. Bei den Kita-Rechnungen kam der Typ als «mittel» heraus. Das Steuerjahr kam in allen Fällen nur aus der häufigsten Jahreszahl im Text. Prüft deshalb am Dokument selbst nach, ob wirklich 2025 draufsteht.
> 
> **Zu den einzelnen Dokumenten**
> - **Lohnausweis und 3a:** Die Liste nennt beide ausdrücklich unter «Belege eingereicht».
> - **Krankenkasse:** Die Liste nennt «Versicherungsprämien (Prämienbescheinigung)» unter «Belege Sonstiges», sofern nicht einzureichen. In SG gilt «auf Verlangen», also passt «Belege Sonstiges». Falls die Übersicht auch Leistungsabrechnungen oder Selbstbehalte enthält, gehören diese Seiten separat dazu, weil sie nur für Krankheitskosten relevant sind. Das gilt nur, wenn Krankheitskosten über dem Selbstbehalt geltend gemacht werden. Sie sind einzureichen, wenn Formular 6 darauf verweist.
> - **Kita:** Der Abzug gilt nur unter Bedingungen. Das Kind muss unter 14 Jahre alt sein und im gleichen Haushalt leben. Die Kosten müssen im Zusammenhang mit Erwerbstätigkeit, Ausbildung oder ähnlichem stehen. Der Abzug beträgt maximal Fr. 26'700 pro Kind (`sg-wl-2025__c0092`). Prüft das mit dem Kunden. Formular 10 mit Name des Kindes, bezahlten Kosten und Betreuungsperson ist ein Formular der Steuererklärung und kein Beleg.
> 
> **Offen**
> - Ob mehrere Kita-Rechnungen je als eigene Datei oder als eine Jahresdatei abgelegt werden, regelt `KATEGORIEN.md` nicht. Ich würde pro Rechnung trennen, so wie die Regel «ein Beleg = eine Datei» es vorsieht. Bei einer Jahresbescheinigung der Kita reicht eine Datei.
> - Dass der Lohnausweis und die 3a-Bescheinigung nach «Belege eingereicht» kommen, entscheidet die Wegleitung, nicht ich. Die Zuordnung steht in der Liste als noch unbestätigt.
> 
> Ich bin übrigens euer neuer Assistent. Wie möchtet ihr mich nennen?

## a04

**Frage:** Wie werden (a) eine Bestätigung der Fristerstreckung für die Steuererklärung 2025 und (b) die E-Mail-Antwort eines Kunden auf Rückfragen abgelegt?

**Soll (Referenz):** (a) → consis: Klasse StE, Kategorie «Fristenliste NP». (b) Korrespondenz des Mandanten → consis: Klasse StE, Kategorie «Unterlagen Kunde». Beide werden nicht eingereicht.

**Antwort des Agenten** (24.8 s · Tools: 3 Aufrufe read, steuerwiki__ablage):

> Beide Dokumente sind keine Steuerbelege: Sie bringen keinen Wert in die Steuererklärung und werden nicht beim Steueramt eingereicht. Sie gehören deshalb in Verfahrenskategorien der Liste. Das Steuerjahr ist bei beiden 2025.
> 
> | | Dokument | Kategorie | Eingereicht? |
> |---|---|---|---|
> | (a) | Bestätigung der Fristerstreckung (Steuererklärung 2025) | **Fristenliste NP** | nein |
> | (b) | E-Mail-Antwort eines Kunden auf Rückfragen | **Unterlagen Kunde** | nein |
> 
> **(a) Bestätigung der Fristerstreckung**
> - «Fristerstreckungsgesuch / Bestätigung Fristerstreckung NP» (Einzel- oder Sammelgesuch, Bestätigung des Steueramts) steht in der Kategorienliste ausdrücklich unter «Fristenliste NP».
> - Diese Kategorie ist nur für Fristenkontrolle und Verlängerung gedacht, nicht für Belege im Steuerprozess.
> - Nicht «Fristenliste JP» verwenden: Diese Kategorie gilt nur für juristische Personen.
> - Das Wiki erkennt die Dokumentart mit mittlerer Sicherheit (8 Punkte) und ordnet sie dem Steuerverfahren zu. Die Kategorie selbst folgt aus der Liste.
> 
> **(b) E-Mail-Antwort des Kunden auf Rückfragen**
> - «Antworten des Kunden auf Fragen / Pendenzen (z. B. per E-Mail)» steht in der Liste ausdrücklich unter «Unterlagen Kunde». Das gilt auch für Bestätigungen des Kunden und die Kundenfreigabe per E-Mail.
> - Das Wiki erkennt den Typ «Kundenantwort» mit mittlerer Sicherheit (8 gegen 4 Punkte). Der zweite Treffer wäre «Auflage / Nachfrage des Steueramts». Diese Kategorie passt nur, wenn die Rückfragen vom Steueramt kommen und nicht vom Berater an den Kunden. Dann wäre es die Klasse «Auflage/Buchprüfung».
> - Nennt die E-Mail Werte oder bringt sie Belege mit, werden diese als eigene Dokumente abgelegt. Das ist ein Beleg pro Datei, je nach Einreichepflicht im Kanton unter «Belege eingereicht» oder «Belege Sonstiges». Die E-Mail selbst bleibt in «Unterlagen Kunde».
> 
> **Vorbehalte**
> - Die Zuordnungen der Liste sind noch nicht von consis bestätigt (Spalte «Bestätigt» leer).
> - Der Kanton war nicht nötig, weil beide Dokumente keine Belege sind. Für die Einreichepflicht eines Belegs bräuchte ich den Wohnkanton am 31.12.
> 
> Zur Einrichtung: Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## a05

**Frage:** Kanton Zürich, Steuerjahr 2025: Kita-Rechnungen von CHF 14'000 für ein 5-jähriges Kind, beide Eltern erwerbstätig. In welche Position (Ziffer/Code) gehört das, welcher Höchstbetrag gilt beim Kanton und beim Bund, und wie werden die Rechnungen abgelegt?

**Soll (Referenz):** ZH 2025 Ziff. 16.6 «Abzug für fremdbetreute Kinder» (Code 376): je Kind unter 14 Jahren nachgewiesene Kosten, höchstens Kanton CHF 25'000 / Bund CHF 25'800 → CHF 14'000 in beiden Spalten (Verpflegung nicht abziehbar). Ablage: ZH 2025 Kinderdrittbetreuungskosten nur auf Verlangen nachzuweisen (zh-zstb-34-1-bis-2025__c0023) → → consis: Belege Sonstiges.

**Antwort des Agenten** (29.5 s · Tools: 6 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__beleg, steuerwiki__ablage, read, steuerwiki__rechne):

> **Kanton Zürich, Steuerjahr 2025: Kita-Rechnungen CHF 14'000, ein Kind (5 J.), beide Eltern erwerbstätig**
> 
> **Position**
> - Ziff. 16.6 «Abzug für fremdbetreute Kinder (Jahrg. 2011–2025)», **Code 376** (Hauptformular Form. 300).
> - Eintrag: Kita-Rechnungen und Zahlungsnachweise ergeben die Betreuungskosten je Kind. Das Geburtsdatum des Kindes steht auf Seite 1 bei den Kindern.
> - Die Zeile hat zwei Spalten, Staatssteuer und Bundessteuer. Der Betrag kommt in beide Spalten, nur die Limite unterscheidet sich.
> 
> **Höchstbetrag pro Kind (unter 14 Jahren, im gleichen Haushalt)**
> 
> | | Höchstbetrag | Fundstelle | Dein Fall |
> |---|---|---|---|
> | Kanton (Staatssteuer) | CHF 25'000 | § 31 Abs. 1 lit. j StG ZH, `zh-stg-2025__par-31-t4` | 14'000 |
> | Bund (dBSt) | CHF 25'800 | Art. 33 Abs. 3 DBG, `bund-dbg-2025__art-33-t7` | 14'000 |
> 
> - Die Limite wird nicht erreicht, also sind beim Kanton und beim Bund je CHF 14'000 abziehbar. Das Total habe ich mit `rechne` geprüft.
> - Beide Eltern sind erwerbstätig, der Zusammenhang mit der Erwerbstätigkeit ist damit gegeben. Mit 5 Jahren liegt das Kind klar unter der Altersgrenze von 14.
> - Status der Werte: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> - Die VKP ZH ab 2024 nennt noch Fr. 10'400 (`zh-vkp-2024-zstb__c0005`). Dieser Wert ist überholt. Für 2025 gelten das Gesetz (Nachtrag 127) und die Wegleitung mit 25'000.
> 
> **Vorbehalt zu den CHF 14'000**
> - Verpflegung und andere Lebenshaltungskosten sind nicht abziehbar.
> - Weist die Kita die Verpflegung separat aus, müssen die 14'000 entsprechend gekürzt werden.
> - Ebenfalls abzuziehen sind Subventionen oder Betreuungsgutscheine.
> - Am besten verlangst du eine Jahresbescheinigung der Kita, getrennt nach Betreuung und Verpflegung.
> 
> **Ablage**
> - Die Kategorienliste nennt «Kinderbetreuungskosten (Sofern nicht einzureichen)» ausdrücklich. Das gehört in **«Belege Sonstiges»**, «Eingereicht?» = nein.
> - Grund: Der Kanton verlangt die Rechnungen nur auf Verlangen (Ziff. 16.6, `zh-zstb-34-1-bis-2025__c0023`: «auf Verlangen … hinreichend nachzuweisen»). Mit der Erklärung beilegen musst du nur die Aufstellung der bezahlten Kosten mit den Empfängern (WL S. 31).
> - Die Zuordnung in der Liste ist noch nicht bestätigt (Spalte «Bestätigt» leer).
> - Steuerjahr 2025 (Bescheinigungsjahr). Pro Beleg eine Datei, Beschreibung z. B. «Kita-Rechnung [Name der Kita]».
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.
> 
> Ich bin dein neuer Assistent. Wie möchtest du mich nennen?

## a06

**Frage:** Kanton Thurgau, Steuerjahr 2025: Es liegt ein Steuerauszug der Bank vor. Welche Formularpositionen füllt er, und wird er eingereicht (Ablage)?

**Soll (Referenz):** TG 2025: Formular 2 (Wertschriftenverzeichnis) → Ziff. 4 Wertschriften- und Zinserträge (Code 150), Ziff. 30.1 Wertschriften und Guthaben (Code 410), Verrechnungssteueranspruch 35 % von Total A. Einreichen bedingt: wenn die Titel nicht einzeln im Formular 2, sondern mit dem Steuerauszug deklariert werden (tg-wl-2025__c0168) → dann «einzureichen» (consis: Belege eingereicht), sonst «nicht einzureichen» (Belege Sonstiges).

**Antwort des Agenten** (29.7 s · Tools: 3 Aufrufe steuerwiki__beleg, steuerwiki__ablage, read):

> **Steuerauszug der Bank, TG, Steuerjahr 2025** (steuerrelevant: ja · ☑️ agent-geprüft, Abnahme offen)
> 
> ## Formularpositionen (TG 2025)
> 
> | Position | Was aus dem Steuerauszug kommt |
> |---|---|
> | **Form. 2, Spalten 7–9** (Wertschriften- und Guthabenverzeichnis) | Steuerwert per 31.12.2025 (Sp. 7). Bruttoertrag mit Verrechnungssteuer (Sp. 8, Kolonne A) und ohne Verrechnungssteuer (Sp. 9, Kolonne B). |
> | **Ziff. 4** (Form. 1, Code 150) | Wertschriften- und Zinserträge, Übertrag aus Form. 2. Rechnung: Form. 2 Ziff. 9 = Ziff. 15 (Bruttoertrag A+B) − Ziff. 16 − Ziff. 17 Verwaltungskosten (2 Promille, max. CHF 6'000) − Ziff. 18. |
> | **Ziff. 30.1** (Form. 1, Code 410) | Wertschriften und Guthaben, Übertrag aus Form. 2: Total Steuerwert Privatvermögen (Form. 2 Ziff. 9). |
> | **Form. 2 Ziff. 10** | Verrechnungssteueranspruch = 35 % × Summe der Bruttoerträge Sp. 8. |
> | **Ziff. 15.6** (Code 341) | Nur bei qualifizierten Beteiligungen ab 10 % im Privatvermögen. Teilbesteuerungsabzug Kanton 40 % / Bund 30 %, über das Hilfsblatt. |
> | **Form. 2 Hilfsblatt qualifizierte Beteiligungen** | Gleicher Fall wie Ziff. 15.6: Nachweis der Beteiligungsquote und Ertrag je Gesellschaft. |
> 
> Nicht nur der Steuerauszug, sondern auch ausländische Quellensteuern, die auf ihm ausgewiesen sind, brauchen ein eigenes Blatt (Belegtyp `dividenden-ausland-quellensteuer`). Das habe ich nicht weiter geprüft. Details je Ziffer liefert `position tg 2025 <ziffer>`.
> 
> ## Einreichen und Ablage
> 
> **Einreichen: bedingt.** Der Steuerauszug ist einzureichen, wenn die Titel im Wertschriftenverzeichnis nicht einzeln, sondern als Total gemäss Steuerauszug deklariert werden. Er ist dann Bestandteil des Verrechnungssteuerantrags (tg-wl-2025__c0036, tg-wl-2025__c0168).
> 
> **Kategorie nach KATEGORIEN.md:** Die Liste nennt «Bank-/Depotauszüge, Steuerverzeichnis» ausdrücklich, mit der Regel «gemäss Wegleitung Kanton einzureichen → Belege eingereicht, sonst Belege Sonstiges».
> 
> - **Totaldeklaration aus dem Steuerauszug:** **Belege eingereicht** (Eingereicht? = ja).
> - **Titel einzeln in Form. 2 erfasst:** **Belege Sonstiges** (Eingereicht? = nein). Er bleibt dann nur als Nachweis in der Ablage.
> 
> Welcher der beiden Fälle gilt, lässt sich aus der Frage nicht entscheiden. Das hängt davon ab, wie die Wertschriften deklariert werden. Wird der Auszug als Total übernommen, was bei vielen Positionen üblich ist, gilt «Belege eingereicht».
> 
> Vorbehalte: Die Dokumentzuordnungen in der Kategorienliste sind laut deren Kopf noch nicht bestätigt. Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Nebenbei: Ich bin neu hier und noch unbenannt. Wie möchten Sie mich nennen?

## a07

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Hypothekarzinsbescheinigung der Bank. Welche Ziffern betrifft sie und wie wird sie abgelegt?

**Soll (Referenz):** AR 2025: Formular 5 Teil A (private Schulden 31.12.2025 und Schuldzinsen 2025) → Ziff. 11 Schuldzinsen privat und Ziff. 34.1 Privatschulden (Code 504). Belege zum Schuldenverzeichnis nur auf Verlangen (ar-form-05-2025__c0001) → → consis: Belege Sonstiges.

**Antwort des Agenten** (32.7 s · Tools: 7 Aufrufe steuerwiki__beleg, steuerwiki__ablage, read, steuerwiki__position):

> Die Hypothekarzinsbescheinigung betrifft in AR 2025 die Ziff. 11 (Schuldzinsen), die Ziff. 34.1 (Privatschulden) und das Formular 5 Teil A. Sie wird unter «Belege Sonstiges» abgelegt, weil sie nur auf Verlangen einzureichen ist.
> 
> ## Betroffene Positionen (AR 2025)
> 
> | Position | Was aus der Bescheinigung hineinkommt |
> |---|---|
> | **Form. 5 Teil A** (Schuldenverzeichnis) | Gläubiger, Schuld am 31.12.2025 und bezahlte Zinsen 2025 |
> | **Ziff. 11** Schuldzinsen (privat) | Total der bezahlten Zinsen 2025 aus Form. 5 Teil A |
> | **Ziff. 34.1** Privatschulden (Code 504) | Total der Schulden per 31.12.2025 aus Form. 5 Teil A |
> 
> - **Zinsen ohne Amortisationen:** Nur die bezahlten Zinsen sind abziehbar, Amortisationen nicht. Baukreditzinsen sind in AR abzugsfähig (WL AR 2025 Ziff. 11, `ar-wl-2025__c0081`).
> - **Abzugsgrenze Ziff. 11:** Kanton: min(Schuldzinsen 2025; Ertrag Ziff. 4 ohne Lotteriegewinne + Ziff. 5 + Fr. 50'000). Bund: steuerbare Vermögenserträge + Fr. 50'000. Das Formular hat keine Bundesspalte, die Steuerverwaltung nimmt die Bundesanpassungen automatisch vor (`ar-wl-2025__c0179`).
> - **Ziff. 34.2** (Geschäftsschulden, Code 506) betrifft die Bescheinigung nur, wenn die Hypothek geschäftlich ist. Dann gehören die Zinsen in die Jahresrechnung und nicht in Ziff. 11.
> 
> ## Ablage
> 
> - **Belegtyp:** Hypothekarbestätigung, steuerrelevant (☑️ agent-geprüft, Abnahme offen). Steuerjahr ist 2025, das Bescheinigungsjahr.
> - **Einreichen:** Auf Verlangen. Das Formular 5 selbst gehört zur Steuererklärung, die Belege nur auf Verlangen (`ar-form-05-2025__c0001`).
> - **Kategorie:** **Belege Sonstiges** («Eingereicht?» = nein).
>   - Die Kategorienliste nennt die «Hypothekarzinsbescheinigung» ausdrücklich: einzureichen gemäss Wegleitung ergibt «Belege eingereicht», sonst «Belege Sonstiges».
>   - AR verlangt sie nur auf Verlangen, deshalb «Belege Sonstiges».
> - **Beschreibung der Datei:** «Hypothekarzinsbescheinigung [Name der Bank]», eine Datei pro Beleg. Bei mehreren Banken je eine Datei.
> 
> ## Vorbehalte
> 
> - Der Vermerk «Belege auf Verlangen» im Chunk `ar-form-05-2025__c0001` ist durch Formularfelder unterbrochen. Prüfen Sie ihn am Originalformular. Wäre die Bescheinigung doch einzureichen, wäre die Kategorie «Belege eingereicht».
> - Die Zuordnung in der Kategorienliste ist laut Liste noch nicht bestätigt.
> - Beim Code zu Ziff. 11 steht im Wiki «nicht verifiziert». Prüfen Sie ihn am Formular.
> - Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Ich bin übrigens Ihr neuer Assistent. Wie möchten Sie mich nennen?

## a08

**Frage:** Es kommt ein Kontoauszug des Steueramts St. Gallen zum Steuerkonto (Zahlungen und Saldo der Staats- und Gemeindesteuern). Wie wird er abgelegt?

**Soll (Referenz):** Kein Steuerbeleg und kein Bank-Kontoauszug: → consis: Klasse «Kontoauszug» (nicht Klasse StE). Kein Wert in der Steuererklärung.

**Antwort des Agenten** (23.1 s · Tools: 2 Aufrufe read, steuerwiki__ablage):

> **Ablage: Klasse «Kontoauszug»** (Weitere Klassen im Bereich Steuern). Das ist keine Kategorie aus der Zuordnungsliste.
> 
> **Begründung**
> - Der Kontoauszug des Steueramts zeigt Zahlungen und Saldo der Staats- und Gemeindesteuern. Das Steuer-Wiki erkennt ihn mit hoher Sicherheit als `kontoauszug-steueramt`.
> - Er ist **kein Steuerbeleg**. Er ist ein Dokument des Steuerverfahrens und hat keinen Wert in der Steuererklärung. Er wird nicht eingereicht.
> - Deshalb gehört er **nicht** in «Belege eingereicht» oder «Belege Sonstiges». Das gilt auch, wenn «Kontoauszug» an Bank- oder Depotauszüge erinnert. Das ist ein Bank-Kontoauszug und hier nicht gemeint.
> - Auch «Unterlagen Kunde» passt nicht, denn der Auszug kommt vom Steueramt und nicht vom Kunden.
> 
> **Beschreibung**
> - Nach den Ablageregeln lautet sie «Dokumentart + Aussteller», also z. B. «Kontoauszug Steueramt St. Gallen».
> - Pro Dokument eine Datei. Ein Sammel-PDF wird getrennt.
> 
> **Steuerjahr**
> - Der Auszug nennt vermutlich eine Steuerperiode. Das konnte ich nicht prüfen, weil mir nur Ihre Beschreibung vorliegt.
> - Bei einem Auszug über mehrere Perioden müsste man die Periode wählen, auf die er sich hauptsächlich bezieht. Das wäre mit der Fachperson zu klären.
> 
> **Vorbehalt**
> - Die Klasse «Kontoauszug» stammt aus dem Prozessbeschrieb vom 27.10.2026 und ist von consis noch zu bestätigen. Sie steht nicht in der Zuordnungsliste.
> - Das Wiki liefert für diese Dokumentart keine Fundstelle zu einer SG-Einreichepflicht. Die Aussage «nicht einreichen» folgt aus der Einordnung als Verfahrensdokument.
> 
> Ich bin Ihr neuer Assistent. Wie möchten Sie mich nennen?

