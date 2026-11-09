# OpenClaw-Testlauf: ablage-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 8 · Lauf: 2026-11-09 14:30
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## a01

**Frage:** Per E-Mail kommt der «Lohnausweis 2025» der Muster AG für Hans Muster (Kanton Zürich). Ist das steuerrelevant? Welches Steuerjahr, muss er eingereicht werden, wie wird er abgelegt und in welche Position der Steuererklärung gehört der Nettolohn?

**Soll (Referenz):** Steuerrelevant ja. Steuerjahr 2025 (Bescheinigungsjahr). Einzureichen (ZH: Lohnausweise beilegen, zh-wl-2025__c0032; § 134 StG). → consis: Klasse StE, Kategorie «Belege eingereicht». Bezeichnung z.B. «Lohnausweis Muster AG». Nettolohn (Lohnausweis Ziff. 11) → ZH 2025 Ziff. 1.1 Haupterwerb, Code 100 (Person 1).

**Antwort des Agenten** (30.9 s · Tools: 4 Aufrufe steuerwiki__ablage, steuerwiki__beleg, steuerwiki__position, read):

> **Kurz:** Ja, steuerrelevant. Steuerjahr 2025, einreichen, Ablage unter «Belege eingereicht», Nettolohn in Position 100 (Person 1) bzw. 101 (Person 2).
> 
> **Steuerrelevant?** Ja. Es ist ein Lohnausweis (Formular 11) für den Haupterwerb. Ich habe nur den Titel und Ihre Beschreibung gesehen, nicht das Dokument selbst. Die Einordnung ist deshalb «agent-geprüft, Abnahme offen».
> 
> **Steuerjahr:** 2025, als Bescheinigungsjahr. Bitte auf dem Dokument prüfen, dass «2025» dort tatsächlich steht.
> 
> **Einreichen?** Ja. Im Kanton Zürich ist der Lohnausweis für jeden Arbeitgeber mit der Steuererklärung einzureichen (§ 134 Abs. 1 lit. a StG; Wegleitung S. 31).
> 
> **Ablage:** Kategorie **«Belege eingereicht»** (Zeile «Eingereicht?» = ja). Die Liste nennt den Lohnausweis ausdrücklich. Die Kategorienliste ist laut Datei noch nicht von consis bestätigt.
> 
> **Position Nettolohn (Formular 300, ZH 2025):**
> - Ziffer **1.1 Haupterwerb unselbständig**, Code **100** für Person 1 bzw. **101** für Person 2.
> - Eingetragen wird **Ziffer 11 «Nettolohn»** des Lohnausweises (Bruttolohn minus AHV/IV/EO/ALV, laufende BVG-Beiträge und NBUV-Prämien).
> - Staats- und Bundessteuer tragen dieselbe Zeile ein.
> - Den Lohnausweis unbedingt beilegen. Erwerbslücken müssen Sie ausdrücklich bezeichnen.
> 
> **Weitere Lohnausweis-Felder, die ich beim Ausfüllen prüfen würde:**
> - **Ziffer 11 ist zugleich Basis für die pauschalen übrigen Berufskosten** (Form. 360 Ziff. 3: 3 % des Nettolohns, mindestens CHF 2'000, höchstens CHF 4'000).
> - **Feld G (Kantine/Lunch-Checks):** bestimmt den Verpflegungsabzug (Form. 360 Ziff. 2.1).
> - **Feld F (Geschäftsfahrzeug zu Wohn-/Arbeitsort):** schliesst den Fahrkostenabzug aus.
> - **Ziffer 10.2 (BVG-Einkauf):** bereits im Nettolohn abgezogen, nicht nochmals unter Ziff. 16.1 abziehen.
> 
> Soll ich die Verpflegungs- oder Berufskostenpositionen anhand des konkreten Dokuments durchrechnen? Dafür bräuchte ich die Werte aus dem Lohnausweis.

## a02

**Frage:** Ein Kunde lädt eine Migros-Kassenquittung und eine Swisscom-Handyrechnung hoch. Wie werden sie behandelt?

**Soll (Referenz):** Nicht steuerrelevant (private Alltagsrechnungen, kein Wert in der Steuererklärung). Nicht als Steuerbeleg ablegen; Grund nennen (z.B. zur Prüfung markieren oder dem Mandanten zurückmelden). Handyrechnung nur bei nachgewiesener beruflicher Nutzung allenfalls Berufskosten – als Rückfrage.

**Antwort des Agenten** (29.0 s · Tools: 4 Aufrufe read, steuerwiki__ablage):

> **Kurz:** Beide Dokumente sind nicht steuerrelevant und landen in keiner Steuerbeleg-Kategorie. Ich habe nur die Titel-Beschreibungen geprüft, nicht den Inhalt der PDFs.
> 
> | Dokument | Belegtyp | steuerrelevant | Steuerjahr | einreichen | Kategorie | Unsicherheit |
> |---|---|---|---|---|---|---|
> | Migros-Kassenquittung | Private Alltagsrechnung (Lebensmittel) | nein. Lebenshaltungskosten sind nicht abziehbar (Art. 34 lit. a DBG) | unbekannt, Datum fehlt | nein | keine. Grund: nicht steuerrelevant | keine |
> | Swisscom-Handyrechnung | Private Alltagsrechnung (Telefon/Internet) | nein, wenn rein privat | unbekannt, Datum fehlt | nein | keine. Grund: nicht steuerrelevant | Siehe unten |
> 
> **Swisscom:** Falls das Handy teilweise beruflich genutzt wird, kann der berufliche Anteil relevant sein. Das habe ich nicht geprüft. Ich würde den Kunden fragen, ob das Abo beruflich genutzt wird. Dann prüfe ich das mit `steuerwiki__ablage` bzw. `beleg`, sobald Kanton und Steuerjahr feststehen.
> 
> **Offen:** Für die Ablage selbst fehlt nur das Steuerjahr, und dafür brauche ich das Rechnungs- bzw. Quittungsdatum. Der Wohnsitzkanton am 31.12. ist für diese beiden Belege nicht nötig.

## a03

**Frage:** Ein Kunde schickt ein Sammel-PDF mit Lohnausweis 2025, Bescheinigung Säule 3a 2025, Prämienübersicht Krankenkasse 2025 und Kita-Rechnungen 2025 (Kanton St. Gallen). Wie werden die Dokumente abgelegt?

**Soll (Referenz):** Sammel-PDF trennen: ein Beleg = eine Datei. Steuerjahr 2025. Lohnausweis → einzureichen (consis: Belege eingereicht). Säule 3a → einzureichen (consis: Belege eingereicht). Krankenkassenprämien → SG 2025 nur auf Verlangen (sg-wl-2025__c0073) → nicht einzureichen (consis: Belege Sonstiges). Kita-Rechnungen → SG 2025 nicht einzureichen bzw. auf Verlangen → Belege Sonstiges; steuerrelevant bedingt (nur bei Erwerbstätigkeit/Ausbildung, Kind unter 14).

**Antwort des Agenten** (33.4 s · Tools: 5 Aufrufe steuerwiki__ablage, read):

> ## Ablage: Sammel-PDF in vier Einzeldateien, Kanton St. Gallen, Steuerjahr 2025
> 
> Ein Beleg = eine Datei. Das Sammel-PDF muss also nach Seiten getrennt werden. Die Zuordnung unten beruht auf den Dokumentbeschreibungen, nicht auf dem PDF selbst. Vor dem Ablegen Aussteller, Betrag und Seitenzahl im PDF prüfen.
> 
> | Dokument | Kategorie (KATEGORIEN.md) | Eingereicht? | Begründung |
> |---|---|---|---|
> | Lohnausweis 2025 | **Belege eingereicht** | **ja** | Die Liste nennt den Lohnausweis ausdrücklich. SG verlangt pro Arbeitgeber einen Lohnausweis (Form. 1 Ziff. 1.1/1.2, sg-stg-2025__art-169). |
> | Bescheinigung Säule 3a 2025 | **Belege eingereicht** | **ja** | Die Liste nennt die Bescheinigung ausdrücklich. SG verlangt sie bei Abzug Säule 3a (Ziff. 13.1, Form. 21 EDP). |
> | Prämienübersicht Krankenkasse 2025 | **Belege Sonstiges** | nein | Die Liste führt «Versicherungsprämien (Prämienbescheinigung)» unter Sonstiges. In SG ist sie nur auf Verlangen einzureichen (Form. 6, Teil A). |
> | Kita-Rechnungen 2025 | **Belege Sonstiges** | nein | Die Liste führt «Kinderbetreuungskosten» unter Sonstiges. In SG ist die Rechnung nur auf Verlangen einzureichen (Ziff. 16.2, Form. 10). |
> 
> **Dateinamen und Beschreibung** (Regel consis: Dokumentart + Aussteller):
> - `2025_Lohnausweis_<Arbeitgeber>.pdf`
> - `2025_Bescheinigung_Saeule3a_<Institut>.pdf`
> - `2025_Praemienuebersicht_KK_<Krankenkasse>.pdf`
> - `2025_Kita-Rechnungen_<Kita>.pdf` (eine Datei pro Kita, falls mehrere)
> 
> ## Offene Punkte
> 
> 1. **Kita-Rechnungen:** Der Abzug gilt nur für Kinder unter 14 Jahren im gleichen Haushalt und nur bei Erwerbstätigkeit, Ausbildung o. Ä. Das ist vor dem Abzug zu prüfen. Der Höchstbetrag für SG 2025 lautet laut Wiki (sg-wl-2025__c0092) Fr. 26'700 pro Kind. Ein Vorjahresvergleich ist nicht erfolgt.
> 2. **Krankenkasse:** Die Prämien gehören in Form. 6 Teil A, abzüglich der Prämienverbilligung. Falls im Formular auf einen Kassenauszug verwiesen wird, wäre die Leistungsabrechnung einzureichen (Form. 6 Rückseite).
> 3. **Kategorienliste:** Laut Liste sind alle Zuordnungen noch nicht bestätigt (Spalte «Bestätigt» leer). Die Zuordnung der Sonstiges-Belege beruht auf der Regel «sofern nicht einzureichen».

## a04

**Frage:** Wie werden (a) eine Bestätigung der Fristerstreckung für die Steuererklärung 2025 und (b) die E-Mail-Antwort eines Kunden auf Rückfragen abgelegt?

**Soll (Referenz):** (a) → consis: Klasse StE, Kategorie «Fristenliste NP». (b) Korrespondenz des Mandanten → consis: Klasse StE, Kategorie «Unterlagen Kunde». Beide werden nicht eingereicht.

**Antwort des Agenten** (30.1 s · Tools: 2 Aufrufe read):

> **(a) Bestätigung der Fristerstreckung 2025**
> 
> - **Kategorie:** Fristenliste NP
> - **Eingereicht?:** nein
> - **Steuerjahr:** 2025
> 
> Die Liste nennt dieses Dokument ausdrücklich („Bestätigung Fristerstreckung NP“), deshalb gilt diese Zeile. Sie dient nur der Fristenkontrolle und Verlängerung und ist kein Beleg für den Steuerprozess, daher wird das Dokument nicht eingereicht.
> 
> **(b) E-Mail-Antwort des Kunden auf Rückfragen**
> 
> - **Kategorie:** Unterlagen Kunde
> - **Eingereicht?:** nein
> - **Steuerjahr:** 2025, sofern die Rückfragen das Steuerjahr 2025 betreffen (Ablageregel: Bescheinigungsjahr bzw. Steuerperiode, auf die sich das Dokument bezieht)
> 
> Die Liste nennt „Antworten des Kunden auf Fragen / Pendenzen (z. B. per E-Mail)“ ausdrücklich. Falls die E-Mail eine Freigabe zur Einreichung enthält, gehört sie in dieselbe Kategorie („Kundenfreigabe per E-Mail“, Beschreibung «Freigabe Kunde»).
> 
> **Zu beachten:**
> 
> - **Anhänge separat ablegen.** Ein Beleg entspricht einer Datei. Liegen Belege wie ein Lohnausweis oder eine Säule-3a-Bescheinigung als Anhang bei, werden sie einzeln nach ihrer eigenen Kategorie abgelegt, nicht unter „Unterlagen Kunde“.
> - **Beschreibung:** Dokumentart und Absender, z. B. „Antworten Kunde auf Rückfragen“ mit Datum.
> - **Unbestätigte Liste:** Die Spalte „Bestätigt“ in `KATEGORIEN.md` ist leer, und die Ablageregeln stammen aus dem Prozessbeschrieb von consis (27.10.2026). Beides sollte consis bestätigen.
> 
> Ich habe die Zuordnung aus der Kategorienliste abgeleitet und keinen Beleg mit dem Werkzeug `ablage` geprüft. Wenn du mir den Text der Bestätigung oder der E-Mail gibst, prüfe ich Typ, Relevanz und Steuerjahr mit `ablage` ab.

## a05

**Frage:** Kanton Zürich, Steuerjahr 2025: Kita-Rechnungen von CHF 14'000 für ein 5-jähriges Kind, beide Eltern erwerbstätig. In welche Position (Ziffer/Code) gehört das, welcher Höchstbetrag gilt beim Kanton und beim Bund, und wie werden die Rechnungen abgelegt?

**Soll (Referenz):** ZH 2025 Ziff. 16.6 «Abzug für fremdbetreute Kinder» (Code 376): je Kind unter 14 Jahren nachgewiesene Kosten, höchstens Kanton CHF 25'000 / Bund CHF 25'800 → CHF 14'000 in beiden Spalten (Verpflegung nicht abziehbar). Ablage: ZH 2025 Kinderdrittbetreuungskosten nur auf Verlangen nachzuweisen (zh-zstb-34-1-bis-2025__c0023) → → consis: Belege Sonstiges.

**Antwort des Agenten** (37.1 s · Tools: 6 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__beleg, read, steuerwiki__ablage):

> **Kanton Zürich, Steuerjahr 2025: Kita-Rechnungen für ein 5-jähriges Kind**
> 
> **Position:** Ziff. 16.6 «Abzug für fremdbetreute Kinder (Jahrg. 2011–2025)», Code **376** (Form. 300). Das Kind ist 5 Jahre alt und fällt damit unter den Jahrgang. ☑️ agent-geprüft, Abnahme offen.
> 
> **Höchstbeträge** (je Kind unter 14 Jahren, im gleichen Haushalt):
> - **Kanton (Staatssteuer):** CHF 25'000, § 31 Abs. 1 lit. j StG ZH, Nachtrag 127. Eine ältere VKP-Angabe von CHF 10'400 ist für 2025 überholt.
> - **Bund:** CHF 25'800, Art. 33 Abs. 3 DBG.
> - Die Kosten müssen im direkten Zusammenhang mit der Erwerbstätigkeit stehen. Das ist hier mit zwei erwerbstätigen Eltern gegeben.
> 
> **Abzug:** CHF 14'000 liegen unter beiden Limiten, also ist der volle Betrag abziehbar, sofern:
> - die Rechnungen nur Betreuungskosten enthalten. Verpflegungsanteile sind nicht abziehbar; sind sie nicht separat ausgewiesen, ist der Betrag zu kürzen.
> - Subventionen oder Betreuungsgutscheine abgezogen sind (sie mindern die Kosten).
> - Die Zahlungen im Steuerjahr 2025 geleistet wurden.
> - Bei einem Konkubinat mit gemeinsamer Sorge gilt je Elternteil ein Maximum von CHF 12'500 (Kanton) bzw. CHF 12'900 (Bund). Bei hälftiger Aufteilung wären das je CHF 7'000, also unter dem Limit. Eine andere Aufteilung muss nachgewiesen werden.
> - Die Bund-Spalte separat ausgefüllt wird. Der Betrag ist unter beiden Regeln gleich hoch. Ob im Formular für den Bund denselben Betrag braucht, habe ich nicht im Detail geprüft; `position zh 2025 16.6` zeigt die Spaltenregel.
> 
> **Ablage:**
> - **Die Rechnungen selbst:** Kategorie **«Belege Sonstiges»** (Liste: «Kinderbetreuungskosten (Sofern nicht einzureichen)»). «Eingereicht?» = **nein**. Der Wiki-Eintrag sagt, dass die Belege nur auf Verlangen der Steuerbehörde einzureichen sind.
> - **Zusätzlich:** Eine **Aufstellung der bezahlten Kosten mit Empfängern** muss unaufgefordert beigelegt werden (Ziff. 16.6, Wegleitung S. 31). Diese Aufstellung gehört zu **«Belege eingereicht»**, «Eingereicht?» = **ja**.
> - Beschreibung nach Konvention: z.B. «Kita-Rechnungen [Name Kita] 2025». Bescheinigungsjahr ist 2025.
> 
> Die Kategorienliste ist laut Datei noch nicht vollständig bestätigt. Die Zuordnung zu «Belege Sonstiges» ist eindeutig, die Aufstellung als Beilage sollte aber mit consis abgestimmt werden.

## a06

**Frage:** Kanton Thurgau, Steuerjahr 2025: Es liegt ein Steuerauszug der Bank vor. Welche Formularpositionen füllt er, und wird er eingereicht (Ablage)?

**Soll (Referenz):** TG 2025: Formular 2 (Wertschriftenverzeichnis) → Ziff. 4 Wertschriften- und Zinserträge (Code 150), Ziff. 30.1 Wertschriften und Guthaben (Code 410), Verrechnungssteueranspruch 35 % von Total A. Einreichen bedingt: wenn die Titel nicht einzeln im Formular 2, sondern mit dem Steuerauszug deklariert werden (tg-wl-2025__c0168) → dann «einzureichen» (consis: Belege eingereicht), sonst «nicht einzureichen» (Belege Sonstiges).

**Antwort des Agenten** (31.4 s · Tools: 4 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read, steuerwiki__zeige):

> **Steuerauszug der Bank, TG, Steuerjahr 2025**
> 
> **Formularpositionen** (Fundstelle WL TG 2025; Status ☑️ agent-geprüft, Abnahme offen):
> 
> - **Ziff. 4** Wertschriften- und Zinserträge (Form. 1 Code 150, Übertrag aus Form. 2): Bruttoerträge mit VSt (Sp. 8) und ohne VSt (Sp. 9) aus dem Auszug übernehmen.
> - **Ziff. 15.6** Teilbesteuerungsabzug Beteiligungen (Form. 1 Code 341): nur falls qualifizierte Beteiligungen (≥ 10 %) vorliegen. Kanton 40 %, Bund 30 %, über das Hilfsblatt.
> - **Ziff. 30.1** Wertschriften und Guthaben (Form. 1 Code 410): Steuerwert per 31.12.2025 je Konto/Titel bzw. Total.
> - **Form. 2, Spalten 7–9**: Steuerwert 31.12. (Sp. 7), Bruttoertrag mit VSt (Sp. 8), ohne VSt (Sp. 9).
> - **Form. 2, Ziff. 10**: Verrechnungssteueranspruch, 35 % der Bruttoerträge mit VSt (Sp. 8).
> - **Hilfsblatt qualifizierte Beteiligungen**: nur bei Beteiligungen ≥ 10 %.
> 
> **Einreichung: bedingt.** Der Steuerauszug muss eingereicht werden, wenn die Titel nicht einzeln im Wertschriftenverzeichnis stehen, sondern als Total gemäss Auszug deklariert werden. Er wird dann Bestandteil des Verrechnungssteuer-Antrags und bleibt bei den Akten (WL TG 2025 S. 35, tg-wl-2025__c0168; S. 10, c0036).
> 
> **Ablage** (KATEGORIEN.md, Zeile «Bank-/Depotauszüge»):
> 
> - **Werden die Titel als Total aus dem Steuerauszug deklariert:** Kategorie **Belege eingereicht**, «Eingereicht?» = **ja**.
> - **Werden sie einzeln im Wertschriftenverzeichnis deklariert:** Kategorie **Belege Sonstiges**, «Eingereicht?» = **nein**.
> 
> Ich kann die Entscheidung nicht aus dem Dokument allein treffen, weil sie davon abhängt, wie die Titel deklariert werden. Die Kategorieliste ist außerdem noch nicht von consis bestätigt.
> 
> **Hinweis:** Das Tool ordnet den Steuerauszug in der Ablage-Prüfung als «ja» ein, die Liste verweist aber auf die Wegleitung und damit auf die Bedingung oben. Ich habe mich an die Bedingung gehalten.

## a07

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Hypothekarzinsbescheinigung der Bank. Welche Ziffern betrifft sie und wie wird sie abgelegt?

**Soll (Referenz):** AR 2025: Formular 5 Teil A (private Schulden 31.12.2025 und Schuldzinsen 2025) → Ziff. 11 Schuldzinsen privat und Ziff. 34.1 Privatschulden (Code 504). Belege zum Schuldenverzeichnis nur auf Verlangen (ar-form-05-2025__c0001) → → consis: Belege Sonstiges.

**Antwort des Agenten** (32.8 s · Tools: 7 Aufrufe steuerwiki__ablage, steuerwiki__beleg, steuerwiki__position, read):

> **Kanton AR, Steuerjahr 2025: Hypothekarzinsbescheinigung**
> 
> **Ziffern im Formular (AR 2025)**
> 
> - **Ziff. 11, Schuldzinsen (privat):** Die bezahlten Hypothekarzinsen 2025 gehören hierher, übertragen über Formular 5 Teil A. Nur Zinsen sind abziehbar, nicht Amortisationen. Der Abzug ist begrenzt auf Wertschriften- und Guthabenerträge (Ziff. 4, ohne Lotteriegewinne) plus Liegenschaftserträge (Ziff. 5) plus Fr. 50'000. Baukreditzinsen sind in AR abziehbar.
> - **Ziff. 34.1, Privatschulden (Code 504):** Der Schuldsaldo per 31.12.2025 je Gläubiger, übertragen über Formular 5 Teil A.
> - **Ziff. 34.2, Geschäftsschulden (Code 506):** Nur relevant bei Selbständigerwerb. Geschäftliche Schuldzinsen gehören in die Jahresrechnung, nicht hierher.
> - **Bund:** Das AR-Formular hat keine Bundesspalte. Die Steuerverwaltung nimmt die Abweichungen für die direkte Bundessteuer automatisch vor. Die Abzugsgrenze für Schuldzinsen beim Bund ist aus den AR-Quellen nicht belegt und separat zu prüfen.
> 
> Die Codes 504 und 506 stammen aus der Formular-Miniatur der Wegleitung und sind laut Wiki nicht verifiziert. Ziff. 11 hat laut Wiki keinen verifizierten Code. Bitte am Originalformular prüfen.
> 
> **Einreichung:** Laut Wiki ist die Bescheinigung in AR nur **auf Verlangen** einzureichen. Sie wird im Schuldenverzeichnis (Formular 5) erfasst, und die Steuerverwaltung kann die Belege nachfordern. Sie muss also nicht von sich aus eingereicht werden, sollte aber griffbereit sein.
> 
> **Ablage nach KATEGORIEN.md**
> 
> - **Kategorie:** Belege Sonstiges
> - **Eingereicht?:** nein
> 
> Die Liste ordnet die Hypothekarzinsbescheinigung der Kategorie «Belege eingereicht» zu, wenn die Wegleitung des Kantons sie einzureichen verlangt. Das ist in AR nicht der Fall, deshalb gilt «Belege Sonstiges». Die Kategorie ist noch nicht durch consis bestätigt.
> 
> Falls du die Bescheinigung doch einreichen willst, oder eine Prüfung ansteht, lege sie in «Belege eingereicht» ab.
> 
> Quellen: `hypothekarbestaetigung` (Wiki-Beleg, Fundstellen ar-form-05-2025__c0001 und ar-wl-2025__c0081), Positionen Ziff. 11, 34.1, 34.2 (AR 2025), `KATEGORIEN.md`.

## a08

**Frage:** Es kommt ein Kontoauszug des Steueramts St. Gallen zum Steuerkonto (Zahlungen und Saldo der Staats- und Gemeindesteuern). Wie wird er abgelegt?

**Soll (Referenz):** Kein Steuerbeleg und kein Bank-Kontoauszug: → consis: Klasse «Kontoauszug» (nicht Klasse StE). Kein Wert in der Steuererklärung.

**Antwort des Agenten** (24.9 s · Tools: 2 Aufrufe steuerwiki__ablage, read):

> **Ablage: Klasse «Kontoauszug»**, nicht als Steuerbeleg.
> 
> - **Art:** Kontoauszug des Steueramts (Steuerkonto, Zahlungen und Saldo). Das ist kein Bank-Kontoauszug und kein Beleg für die Steuererklärung. Es enthält keinen Wert, der in die Deklaration gehört.
> - **Kategorie:** Keine Zeile der Kategorienliste passt. Die Klasse «Kontoauszug» steht im consis-Ablageschema für Verfahrensdokumente des Steueramts, und zwar unter «Weitere Klassen im Bereich Steuern». Die Liste selbst kennt diese Klasse nicht. Die Zuordnung ist von consis noch zu bestätigen.
> - **Eingereicht?** Nein. Es muss nicht eingereicht werden.
> - **Steuerjahr:** 2026, weil das Dokument aus 2026 stammt. Steht im Schreiben ein anderes Bezugsjahr, etwa 2025, gilt dieses.
> - **Beschreibung:** «Kontoauszug Steueramt St. Gallen (Steuerkonto, Staats- und Gemeindesteuern)».
> 
> Nicht in «Belege eingereicht» oder «Belege Sonstiges» ablegen, weil es kein Beleg ist.
> 
> Falls das Schreiben zusätzlich eine Auflage oder Nachfrage des Steueramts enthält, gehört dieser Teil in die Klasse «Auflage/Buchprüfung». Die verlangten Unterlagen sind dann eigene Belege. Bei Auflagen sind außerdem die Fristen zu beachten.

