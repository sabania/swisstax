# OpenClaw-Testlauf: ablage-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 8 · Lauf: 2026-11-09 18:57
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## a01

**Frage:** Per E-Mail kommt der «Lohnausweis 2025» der Muster AG für Hans Muster (Kanton Zürich). Ist das steuerrelevant? Welches Steuerjahr, muss er eingereicht werden, wie wird er abgelegt und in welche Position der Steuererklärung gehört der Nettolohn?

**Soll (Referenz):** Steuerrelevant ja. Steuerjahr 2025 (Bescheinigungsjahr). Einzureichen (ZH: Lohnausweise beilegen, zh-wl-2025__c0032; § 134 StG). → consis: Klasse StE, Kategorie «Belege eingereicht». Bezeichnung z.B. «Lohnausweis Muster AG». Nettolohn (Lohnausweis Ziff. 11) → ZH 2025 Ziff. 1.1 Haupterwerb, Code 100 (Person 1).

**Antwort des Agenten** (29.7 s · Tools: 6 Aufrufe ablage, beleg, read, steuerwiki__ablage, steuerwiki__beleg, steuerwiki__position):

> **Kanton Zürich · Steuerjahr 2025 – Lohnausweis Muster AG (Hans Muster)**
> 
> **Steuerrelevant:** Ja. Der Lohnausweis (Formular 11) belegt das unselbständige Einkommen. Status: ☑️ agent-geprüft, Abnahme offen. Die Erkennung des Dokumenttyps hat nur «mittel» Sicherheit, bitte das Dokument selbst kurz prüfen.
> 
> **Steuerjahr:** 2025. Massgebend ist das Bescheinigungsjahr. Das Jahr stammt aus dem Titel und ist nur die häufigste Jahreszahl im Text, bitte auf dem Dokument bestätigen.
> 
> **Einreichen:** Ja, immer, für jeden Arbeitgeber (auch Nebenerwerb), inkl. Beilagen. Quelle: § 134 Abs. 1 lit. a StG; Wegleitung ZH 2025 S. 31, Chunk `zh-wl-2025__c0032`: «Bitte vergessen Sie nicht, Ihre Lohnausweise der Steuererklärung beizulegen.»
> 
> **Ablage:** Kategorie **«Belege eingereicht»** (Eingereicht? = ja). Die Kategorienliste nennt den Lohnausweis ausdrücklich («Direkt beim Ablegen; eingereicht: ja»). Beachten: Alle Zuordnungen der Liste sind laut Liste noch nicht bestätigt. Nach den consis-Ablageregeln (Prozessbeschrieb, selbst auch noch zu bestätigen):
> - Beschreibung: «Lohnausweis Muster AG»
> - Steuerjahr: 2025
> - Ein Beleg = eine Datei
> 
> **Position für den Nettolohn:** **Ziff. 1.1 «Haupterwerb unselbständig», Code 100** (Person 1; Person 2 wäre Code 101).
> - Einzusetzen ist **Ziff. 11 des Lohnausweises (Nettolohn)**. Das ist Bruttolohn (Ziff. 8) minus AHV/IV/EO/ALV/NBUV (Ziff. 9) minus BVG-Beiträge (Ziff. 10.1 und 10.2).
> - Bei mehreren Haupterwerben ist die Summe der Ziff. 11 einzusetzen.
> - **Bund:** Es gilt dieselbe Zeile für Staats- und Bundessteuer, kein Unterschied. Quelle: `zh-form-300-2025__c0004` (☑️).
> - Wenn Hans Muster nur einen Lohnausweis hat und der Beleg ein Nebenerwerb ist, gehört der Betrag stattdessen in Ziff. 1.2. Das gilt nicht für die Muster AG als Haupterwerb.
> 
> **Weitere Felder im Lohnausweis, die Folgen haben:**
> - **Ziff. 10.2** (BVG-Einkauf, bereits vom Lohn abgezogen): nicht nochmals unter Ziff. 16.1 abziehen.
> - **Feld F** (Kreuz, unentgeltliche Beförderung oder Geschäftsfahrzeug): kein Fahrkostenabzug in Form. 360 Ziff. 1.
> - **Feld G** (Kantine/Lunch-Checks): Verpflegungsabzug Form. 360 Ziff. 2.1 verbilligt, Code 206, max. CHF 1'600 (CHF 7.50/Tag). Ohne Kreuz gilt Code 208, max. CHF 3'200 (CHF 15/Tag).
> - **Ziff. 13.3** (Arbeitgeberbeitrag Weiterbildung): in Form. 367 als «Beitrag Arbeitgeber» (Codes 2901/2904) eintragen.
> - **Ziff. 15** (Bemerkungen): Anzahl Schichttage → Form. 360 Ziff. 2.2, Code 210.
> - **Übrige Berufskosten:** Form. 360 Ziff. 3 berechnet sich als 3 % des Nettolohns (Ziff. 11), mind. CHF 2'000, max. CHF 4'000 (Code 212).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

## a02

**Frage:** Ein Kunde lädt eine Migros-Kassenquittung und eine Swisscom-Handyrechnung hoch. Wie werden sie behandelt?

**Soll (Referenz):** Nicht steuerrelevant (private Alltagsrechnungen, kein Wert in der Steuererklärung). Nicht als Steuerbeleg ablegen; Grund nennen (z.B. zur Prüfung markieren oder dem Mandanten zurückmelden). Handyrechnung nur bei nachgewiesener beruflicher Nutzung allenfalls Berufskosten – als Rückfrage.

**Antwort des Agenten** (25.0 s · Tools: 3 Aufrufe read, steuerwiki__ablage):

> **Kanton: nicht angegeben und für die Einordnung nicht nötig. Steuerjahr: aus den Dokumenten (Quittungs- bzw. Rechnungsjahr), in der Anfrage nicht genannt.**
> 
> | Dokument | Typ | Steuerrelevant? | Kategorie |
> |---|---|---|---|
> | Migros-Kassenquittung | Private Alltagsrechnung (Lebensmittel) | Nein | Keine Steuerbeleg-Kategorie |
> | Swisscom-Handyrechnung | Private Alltagsrechnung (Telefon) | Nein | Keine Steuerbeleg-Kategorie |
> 
> **Begründung (beide Dokumente):**
> - Lebenshaltungskosten sind nicht abziehbar. Es gibt dafür keine Position in der Steuererklärung.
> - Fundstelle: Art. 34 lit. a DBG, «die Aufwendungen für den Unterhalt des Steuerpflichtigen und seiner Familie» (`bund-dbg-2025__art-34`), Status ☑️ agent-geprüft, Abnahme offen.
> - Das Wiki erkennt den Typ mit mittlerer Sicherheit (Punkte 9 bzw. 8 gegen 0). Ich habe nur Titel und Stichwort geprüft, nicht die Dokumente selbst.
> 
> **Ablage:**
> - Die Liste `KATEGORIEN.md` nennt beide Dokumentarten nicht.
> - «Belege eingereicht» und «Belege Sonstiges» gelten nur für Belege mit einem Wert in der Steuerdeklaration. Das trifft hier nicht zu, auch wenn Beispiele wie «Kinderbetreuungskosten» oder «Krankheitskosten» ähnlich klingen.
> - Beide Dokumente also nicht als Steuerbeleg ablegen. Wenn der Kunde sie trotzdem geschickt hat, kann man sie unter «Unterlagen Kunde» dokumentieren. Das ist aber nur meine Überlegung, die Liste sieht das nicht ausdrücklich vor.
> 
> **Vorbehalt bei der Handyrechnung:** Falls der Kunde selbständig erwerbend ist und das Handy teils geschäftlich nutzt, könnte ein Geschäftsanteil in die Jahresrechnung der Einzelfirma gehören. Das ist im Wiki nicht geprüft. Bitte beim Kunden nachfragen, ob das zutrifft.
> 
> Die Beurteilung bleibt bei der Fachperson.

## a03

**Frage:** Ein Kunde schickt ein Sammel-PDF mit Lohnausweis 2025, Bescheinigung Säule 3a 2025, Prämienübersicht Krankenkasse 2025 und Kita-Rechnungen 2025 (Kanton St. Gallen). Wie werden die Dokumente abgelegt?

**Soll (Referenz):** Sammel-PDF trennen: ein Beleg = eine Datei. Steuerjahr 2025. Lohnausweis → einzureichen (consis: Belege eingereicht). Säule 3a → einzureichen (consis: Belege eingereicht). Krankenkassenprämien → SG 2025 nur auf Verlangen (sg-wl-2025__c0073) → nicht einzureichen (consis: Belege Sonstiges). Kita-Rechnungen → SG 2025 nicht einzureichen bzw. auf Verlangen → Belege Sonstiges; steuerrelevant bedingt (nur bei Erwerbstätigkeit/Ausbildung, Kind unter 14).

**Antwort des Agenten** (25.9 s · Tools: 5 Aufrufe read, steuerwiki__ablage):

> **SG · Steuerjahr 2025**
> 
> Das Sammel-PDF wird zuerst getrennt (ein Beleg = eine Datei, gemäss Ablageregel consis, noch nicht bestätigt). Danach wird jede Datei einzeln abgelegt:
> 
> | Dokument | Steuerrelevant | Einreichen in SG 2025 | Kategorie | Beschreibung |
> |---|---|---|---|---|
> | **Lohnausweis 2025** | ja ☑️ | ja, immer; pro Arbeitgeber ein Lohnausweis (`sg-stg-2025__art-169`) | **Belege eingereicht** | «Lohnausweis [Arbeitgeber]»; die Liste nennt ihn ausdrücklich |
> | **Bescheinigung Säule 3a 2025** | ja ☑️ | ja, bei Abzug Ziff. 13.1 (`sg-form-1-2025__c0008`) | **Belege eingereicht** | «Bescheinigung Säule 3a [Stiftung]»; die Liste nennt sie ausdrücklich |
> | **Prämienübersicht Krankenkasse 2025** | ja ☑️ | nur auf Verlangen: Prämien in Form. 6 Teil A deklarieren (`sg-wl-2025__c0073`) | **Belege Sonstiges** | «Prämienbescheinigung [Krankenkasse]»; die Liste führt «Versicherungsprämien (Prämienbescheinigung) (Sofern nicht einzureichen)» |
> | **Kita-Rechnungen 2025** | bedingt ☑️ | nur auf Verlangen: Form. 10 ausfüllen, Belege bei Bedarf nachreichen (`sg-wl-2025__c0092`, `c0073`) | **Belege Sonstiges** | «Kinderbetreuungskosten [Kita]»; die Liste führt «Kinderbetreuungskosten (Sofern nicht einzureichen)» |
> 
> **Hinweise**
> - **Kita:** Der Abzug (Ziff. 16.2, max. Fr. 26'700 pro Kind) gilt nur für Kinder unter 14 im gleichen Haushalt. Die Kosten müssen in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Ähnlichem stehen. Das ist bei der Ablage zu prüfen. Trifft es nicht zu, ist die Rechnung kein Abzugsbeleg.
> - **Krankenkasse:** Individuelle Prämienverbilligungen werden von den Prämien abgezogen (`sg-wl-2025__c0087`). Enthält das PDF zusätzlich Leistungsabrechnungen, ist das ein eigener Typ. Er ist nur relevant, wenn Krankheitskosten über dem Selbbehalt geltend gemacht werden. Einzureichen ist er, wenn Form. 6 darauf verweist.
> - **Steuerjahr:** Das Jahr 2025 wurde von der Erkennung aus der Häufigkeit der Jahreszahl im Titel ermittelt. Es sollte auf den Dokumenten selbst geprüft werden.
> - **Vorbehalt:** Die Zuordnungen in `KATEGORIEN.md` sind von consis noch nicht bestätigt. Die Wiki-Stellen sind ☑️ agent-geprüft, die Abnahme steht aus. Die fachliche Beurteilung bleibt bei der Fachperson.

## a04

**Frage:** Wie werden (a) eine Bestätigung der Fristerstreckung für die Steuererklärung 2025 und (b) die E-Mail-Antwort eines Kunden auf Rückfragen abgelegt?

**Soll (Referenz):** (a) → consis: Klasse StE, Kategorie «Fristenliste NP». (b) Korrespondenz des Mandanten → consis: Klasse StE, Kategorie «Unterlagen Kunde». Beide werden nicht eingereicht.

**Antwort des Agenten** (25.1 s · Tools: 3 Aufrufe read, steuerwiki__ablage):

> **Kein Kanton angegeben.** Das ist für die Ablage nicht nötig, denn Typ und Kategorie hängen nicht vom Kanton ab. Beide Dokumente sind keine Steuerbelege.
> 
> ## (a) Bestätigung der Fristerstreckung, Steuerjahr 2025
> 
> - **Kategorie: «Fristenliste NP».** Die Liste nennt dieses Dokument ausdrücklich: «Fristerstreckungsgesuch / Bestätigung Fristerstreckung NP (Einzel- oder Sammelgesuch, Bestätigung des Steueramts)».
> - **Eingereicht?** Nein.
> - **Steuerrelevant als Beleg?** Nein. Es ist ein Dokument des Steuerverfahrens und hat keinen Wert in der Steuererklärung. Es gehört deshalb nicht in «Belege eingereicht» oder «Belege Sonstiges».
> - **Steuerjahr:** 2025. Das Tool hat das Jahr aus dem Text abgeleitet, bitte am Dokument prüfen.
> - **Nicht verwechseln:** «Fristenliste JP» gilt nur für juristische Personen.
> 
> ## (b) E-Mail-Antwort eines Kunden auf Rückfragen
> 
> - **Kategorie: «Unterlagen Kunde».** Die Liste nennt ausdrücklich «Antworten des Kunden auf Fragen / Pendenzen (z. B. per E-Mail)».
> - **Eingereicht?** Nein.
> - **Steuerrelevant als Beleg?** Nein. Die Antwort enthält Angaben des Kunden ohne eigentlichen Beleg. Der Inhalt wird für die Erfassung in der Steuererklärung verwendet.
> - **Steuerjahr:** Aus der Anfrage nicht ersichtlich. Es gilt das Steuerjahr der Steuererklärung, zu der die Rückfragen gehören.
> - **Falls die E-Mail einen Beleg als Anhang enthält** (z. B. Lohnausweis oder Spendenbescheinigung): Ein Beleg ergibt eine Datei. Den Anhang trennen und separat nach seinem Belegtyp ablegen.
> - **Falls die E-Mail die Freigabe zur Einreichung ist:** Das ist auch «Unterlagen Kunde», mit der Beschreibung «Freigabe Kunde».
> 
> ## Vorbehalte
> 
> - Alle Zuordnungen der Liste sind laut KATEGORIEN.md noch nicht von consis bestätigt (Spalte «Bestätigt» leer). Die beiden hier verwendeten Zeilen stehen aber ausdrücklich in der Liste.
> - Das Tool stuft die Erkennung des Dokumenttyps bei beiden Dokumenten als «mittel» ein. Die Typen passen aber klar zur Beschreibung in der Liste.

## a05

**Frage:** Kanton Zürich, Steuerjahr 2025: Kita-Rechnungen von CHF 14'000 für ein 5-jähriges Kind, beide Eltern erwerbstätig. In welche Position (Ziffer/Code) gehört das, welcher Höchstbetrag gilt beim Kanton und beim Bund, und wie werden die Rechnungen abgelegt?

**Soll (Referenz):** ZH 2025 Ziff. 16.6 «Abzug für fremdbetreute Kinder» (Code 376): je Kind unter 14 Jahren nachgewiesene Kosten, höchstens Kanton CHF 25'000 / Bund CHF 25'800 → CHF 14'000 in beiden Spalten (Verpflegung nicht abziehbar). Ablage: ZH 2025 Kinderdrittbetreuungskosten nur auf Verlangen nachzuweisen (zh-zstb-34-1-bis-2025__c0023) → → consis: Belege Sonstiges.

**Antwort des Agenten** (30.7 s · Tools: 5 Aufrufe steuerwiki__position, steuerwiki__wert, steuerwiki__beleg, read, steuerwiki__rechne):

> **Kanton Zürich · Steuerjahr 2025**
> 
> **Position**
> - Die Kita-Kosten gehören in **Ziff. 16.6 «Abzug für fremdbetreute Kinder (Jahrg. 2011–2025)», Code 376**. Das ist im Hauptformular Form. 300 (Fundstelle zh-form-300-2025__c0008). Status: ☑️ agent-geprüft, Abnahme offen.
> - Ein 5-jähriges Kind hat Jahrgang 2020 und liegt damit im Bereich 2011–2025.
> - Die Spalten «Staatssteuer» und «Bundessteuer» deckt dieselbe Zeile ab. Weicht der Bundesbetrag ab, wird er in der Bundessteuer-Spalte separat eingetragen. Hier ist das nicht nötig, siehe unten.
> 
> **Höchstbetrag pro Kind**
> | | Höchstbetrag | Fundstelle |
> |---|---|---|
> | Kanton (Staatssteuer) | CHF 25'000 | § 31 Abs. 1 lit. j StG ZH, Stand 1.1.2025 (zh-stg-2025__par-31-t4) |
> | Bund (dBSt) | CHF 25'800 | Art. 33 Abs. 3 DBG (bund-dbg-2025__art-33-t7) |
> 
> - Beide Limiten gelten, solange das Kind das 14. Altersjahr noch nicht vollendet hat und im gleichen Haushalt lebt. Status: ☑️ agent-geprüft.
> - Die Verordnung VKP ZH ab 2024 nennt noch Fr. 10'400. Dieser Wert ist für 2025 überholt: Gesetz, Wegleitung (WL) und Formular nennen übereinstimmend CHF 25'000.
> 
> **Rechnung**
> - Kanton: min(14'000; 25'000) = **CHF 14'000**
> - Bund: min(14'000; 25'800) = **CHF 14'000**
> - Beide Limiten greifen nicht. Es wird der volle Betrag abgezogen, aber nur die reinen Betreuungskosten.
> - **Nicht abziehbar ist die Verpflegung.** Weist die Kita sie in der Rechnung aus, ist sie von den CHF 14'000 abzuziehen. Dann sinkt der Abzug entsprechend, im Kanton wie beim Bund.
> - Erhaltene Subventionen oder Betreuungsgutscheine mindern ebenfalls die abziehbaren Kosten.
> 
> **Voraussetzungen**
> - Die Kosten müssen in direktem Zusammenhang mit der Erwerbstätigkeit stehen. Das ist bei beiden erwerbstätigen Eltern erfüllt. Die Betreuungszeiten sollten zu den Arbeitszeiten passen.
> - Leben die Eltern im Konkubinat mit gemeinsamer Sorge, gilt die Limite je halb: Kanton CHF 12'500, Bund CHF 12'900 pro Elternteil. Sie wird dann pro Person auf den von ihr getragenen Anteil angewendet. Bei Ehepaaren trifft das nicht zu.
> 
> **Ablage (KATEGORIEN.md)**
> - Die Kategorienliste nennt «Kinderbetreuungskosten (Sofern nicht einzureichen)» ausdrücklich unter **«Belege Sonstiges»** (Eingereicht? = nein).
> - Begründung: Im Kanton Zürich werden die Kosten nur **auf Verlangen** nachgewiesen. Die Wegleitung sagt dazu: «auf Verlangen der Steuerbehörden hinreichend nachzuweisen» (zh-zstb-34-1-bis-2025__c0023).
> - Die Rechnungen samt Zahlungsnachweisen kommen also in «Belege Sonstiges» und nicht in «Belege eingereicht».
> - Laut Wiki ist zu Ziff. 16.6 zusätzlich eine Aufstellung der bezahlten Kosten mit Empfängern unaufgefordert beizulegen. Diese Aufstellung wird bei der Einreichung mitgegeben; sie ersetzt die Rechnungen nicht, die bei «Belege Sonstiges» bleiben.
> - Steuerjahr der Ablage ist 2025. Pro Beleg eine Datei, Beschreibung nach dem Muster «Kita-Rechnung [Kita-Name], [Kind]».
> - Die Zuordnungen in KATEGORIEN.md sind laut Liste noch nicht bestätigt (Spalte «Bestätigt» leer). Das gilt auch für diese Ablage.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson. Der Status der Fundstellen ist durchgehend «agent-geprüft, Abnahme offen», nicht «verifiziert».

## a06

**Frage:** Kanton Thurgau, Steuerjahr 2025: Es liegt ein Steuerauszug der Bank vor. Welche Formularpositionen füllt er, und wird er eingereicht (Ablage)?

**Soll (Referenz):** TG 2025: Formular 2 (Wertschriftenverzeichnis) → Ziff. 4 Wertschriften- und Zinserträge (Code 150), Ziff. 30.1 Wertschriften und Guthaben (Code 410), Verrechnungssteueranspruch 35 % von Total A. Einreichen bedingt: wenn die Titel nicht einzeln im Formular 2, sondern mit dem Steuerauszug deklariert werden (tg-wl-2025__c0168) → dann «einzureichen» (consis: Belege eingereicht), sonst «nicht einzureichen» (Belege Sonstiges).

**Antwort des Agenten** (28.0 s · Tools: 3 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read):

> **Thurgau · Steuerjahr 2025 · Steuerauszug der Bank (Typ `steuerauszug-bank`, inkl. eSteuerauszug)**
> 
> Der Steuerauszug ist steuerrelevant (☑️ agent-geprüft, Abnahme offen). Er liefert Werte für Einkommen und Vermögen.
> 
> ## Formularpositionen (TG 2025)
> 
> | Position | Inhalt | Wert aus dem Steuerauszug |
> |---|---|---|
> | **Form. 2, Spalten 7–9** | Detailverzeichnis Wertschriften und Guthaben | Sp. 7 = Steuerwert 31.12.2025; Sp. 8 = Bruttoertrag mit Verrechnungssteuer (A); Sp. 9 = Bruttoertrag ohne Verrechnungssteuer (B) |
> | **Ziff. 4** (Form. 1, Code 150) | Wertschriften- und Zinserträge | Übertrag aus Form. 2. Form. 2 Ziff. 9 = Ziff. 15 (Bruttoertrag A+B) − Ziff. 16 Geschäftserträge − Ziff. 17 Verwaltungskosten (2 Promille, max. CHF 6'000) − Ziff. 18 Einsatzkosten |
> | **Ziff. 30.1** (Form. 1, Code 410) | Wertschriften und Guthaben (Vermögen) | Übertrag aus Form. 2. Steuerwerte per 31.12.2025 abzüglich Geschäftswertschriften = Form. 2 Ziff. 9 (Total Steuerwert Privatvermögen) |
> | **Form. 2 Ziff. 10** | Verrechnungssteueranspruch | 35 % × Σ Bruttoerträge Sp. 8 (Kolonne A) |
> | **Ziff. 15.6** (Form. 1, Code 341) | Teilbesteuerungsabzug, nur bei qualifizierten Beteiligungen (≥ 10 %) | Beteiligungsertrag × Kanton 40 % / Bund 30 % |
> | **Form. 2 Hilfsblatt qualifizierte Beteiligungen** | Nur bei Beteiligungen ≥ 10 % | Σ Erträge = Ziff. 2; Abzug Ziff. 3 wird nach Ziff. 15.6 übertragen |
> 
> - Ziff. 15.6 und das Hilfsblatt kommen nur zum Zug, wenn eine Beteiligung von mindestens 10 % vorliegt.
> - Die Kantonsformulare decken Kanton und Bund ab. Die Bundesspalte steht in den Rechenwegen oben (z. B. 30 % bei Ziff. 15.6).
> - Soweit der Auszug Depotgebühren oder Verwaltungskosten ausweist, fliessen sie in Ziff. 17 ein (Pauschale 2 Promille, max. CHF 6'000).
> - Ausländische Quellensteuern sind ein eigener Beleg (`dividenden-ausland-quellensteuer`) und hier nicht abgedeckt.
> 
> ## Einreichen: bedingt (Fundstelle tg-wl-2025__c0036, tg-wl-2025__c0168)
> 
> - **Ja**, wenn die Titel im Wertschriftenverzeichnis nicht einzeln, sondern als Total gemäss Steuerauszug deklariert werden. Der Auszug ist dann Bestandteil des Verrechnungssteuerantrags (WL TG 2025 S. 10 und S. 35).
> - **Nein**, wenn alle Titel einzeln im Form. 2 deklariert sind.
> 
> ## Ablage (KATEGORIEN.md)
> 
> Die Liste nennt «Bank-/Depotauszüge, Steuerverzeichnis» ausdrücklich: «gemäss Wegleitung Kanton/Gemeinde einzureichen → Belege eingereicht, sonst Belege Sonstiges».
> 
> - Titel nur als Total deklariert (Auszug wird eingereicht): **«Belege eingereicht»** (Eingereicht = ja).
> - Titel einzeln im Form. 2 erfasst (Auszug wird nicht eingereicht): **«Belege Sonstiges»** (Eingereicht = nein). Der Auszug hat trotzdem einen Wert in der Deklaration.
> 
> Es gibt keine pauschale Antwort. Massgebend ist, wie der Mandant die Wertschriften deklariert, und das lässt sich nur am konkreten Fall prüfen. Die Zuordnungen in KATEGORIEN.md sind von consis noch nicht bestätigt. Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Beschreibung bei der Ablage: «Steuerauszug [Bank]», Steuerjahr 2025. Wenn Sie mir sagen, ob die Titel einzeln oder als Total deklariert werden, lege ich die Kategorie verbindlich fest.

## a07

**Frage:** Kanton Appenzell Ausserrhoden, Steuerjahr 2025: Hypothekarzinsbescheinigung der Bank. Welche Ziffern betrifft sie und wie wird sie abgelegt?

**Soll (Referenz):** AR 2025: Formular 5 Teil A (private Schulden 31.12.2025 und Schuldzinsen 2025) → Ziff. 11 Schuldzinsen privat und Ziff. 34.1 Privatschulden (Code 504). Belege zum Schuldenverzeichnis nur auf Verlangen (ar-form-05-2025__c0001) → → consis: Belege Sonstiges.

**Antwort des Agenten** (30.2 s · Tools: 7 Aufrufe steuerwiki__beleg, steuerwiki__ablage, read, steuerwiki__position):

> **Appenzell Ausserrhoden · Steuerjahr 2025: Hypothekarzinsbescheinigung der Bank**
> 
> **Steuerrelevant:** ja (Zweck: Abzug und Vermögen). Status ☑️ agent-geprüft, Abnahme offen.
> 
> **Betroffene Ziffern**
> 
> | Ziffer | Inhalt | Wert aus der Bescheinigung |
> |---|---|---|
> | **Ziff. 11** (Seite 3) | Schuldzinsen privat, Übertrag aus Formular 5 Teil A | 2025 bezahlte Zinsen, ohne Amortisationen |
> | **Ziff. 34.1** (Code 504) | Privatschulden, Übertrag aus Formular 5 Teil A | Schuldsaldo per 31.12.2025 je Gläubiger |
> | **Formular 5 Teil A** | Schuldenverzeichnis | Gläubiger, Schuld per 31.12.2025, Zinsen 2025 |
> 
> - **Ziff. 34.2** (Geschäftsschulden, Code 506, Form. 5 Teil B) betrifft nur Selbständigerwerbende oder Geschäftsvermögen. Eine private Hypothek gehört dort nicht hin.
> - **Abzugsgrenze Ziff. 11, Kanton:** Der Abzug ist auf Erträge Ziff. 4 (ohne Lotteriegewinne) plus Ziff. 5, zuzüglich CHF 50'000, begrenzt. Die Summe rechnet man mit `rechne`.
> - **Abzugsgrenze Ziff. 11, Bund:** Das AR-Formular hat keine Bundesspalte. Die Abweichungen für die direkte Bundessteuer nimmt die Steuerverwaltung automatisch vor (ar-wl-2025__c0179). Für die Bundes-Abzugsgrenze der Schuldzinsen gilt nach Wiki-Stand: nicht aus AR-Quellen belegt, separat prüfen.
> - **Baukreditzinsen:** Sie sind in AR abzugsfähig (WL AR 2025 Ziff. 11).
> - **Amortisationen:** Sie sind nicht abziehbar und müssen vom Zinsbetrag getrennt werden.
> - **Code Ziff. 11:** Der Code ist nicht verifiziert, weil Seite 3 der Steuererklärung in der Wegleitung nicht als Miniatur abgebildet ist. Bitte am Originalformular prüfen.
> - **Code Ziff. 34.1:** Der Code 504 stammt aus der Formular-Miniatur der Wegleitung (Raster verzerrt) und ist am Originalformular zu prüfen.
> 
> **Einreichepflicht AR 2025:** nur auf Verlangen. Im Schuldenverzeichnis Formular 5 heisst es: «Die Belege sind auf Verlangen einzureichen» (ar-form-05-2025__c0001). Der Chunk ist durch Formularfelder unterbrochen, der Wortlaut ist daher nur teilweise belegt. Das Formular 5 selbst gehört zur Steuererklärung.
> 
> **Ablage (KATEGORIEN.md)**
> - Die Liste nennt die Hypothekarzinsbescheinigung ausdrücklich. Die Regel lautet: gemäss Wegleitung des Kantons «Belege eingereicht», sonst «Belege Sonstiges».
> - Für AR 2025 ist die Bescheinigung nur auf Verlangen einzureichen, also **«Belege Sonstiges»** («Eingereicht?» = nein).
> - Vorbehalt: Die Zuordnungen der Liste sind laut Datei noch nicht bestätigt.
> - Ablageregeln:
>   - Ein Beleg ist eine Datei.
>   - Die Beschreibung lautet «Hypothekarzinsbescheinigung <Bank>».
>   - Das Steuerjahr ist das Bescheinigungsjahr 2025.
> - Enthält ein Sammel-PDF auch andere Dokumente, etwa einen Steuerauszug, sind diese zu trennen. Ein Steuerauszug der Bank wird nur dann eingereicht, wenn sein Gesamtbetrag ins Formular 2 übertragen wird.
> 
> **Zu prüfen**
> - Die Bescheinigung muss Saldo per 31.12.2025, bezahlte Zinsen, Gläubigerin, Zinssatz und Objekt ausweisen.
> - Hat die Bank mehrere Tranchen, braucht es den Saldo je Tranche.

## a08

**Frage:** Es kommt ein Kontoauszug des Steueramts St. Gallen zum Steuerkonto (Zahlungen und Saldo der Staats- und Gemeindesteuern). Wie wird er abgelegt?

**Soll (Referenz):** Kein Steuerbeleg und kein Bank-Kontoauszug: → consis: Klasse «Kontoauszug» (nicht Klasse StE). Kein Wert in der Steuererklärung.

**Antwort des Agenten** (23.4 s · Tools: 2 Aufrufe read, steuerwiki__ablage):

> **SG · Steuerjahr 2025** (in der Frage kein Jahr genannt, daher 2025 angenommen; bei Auszügen ist es die Steuerperiode, auf die sich der Auszug bezieht)
> 
> **Ablage: Klasse «Kontoauszug»** (Kontoauszug des Steueramts / Steuerkonto, nicht Bank-Kontoauszug)
> 
> - **Typ:** Kontoauszug des Steueramts mit Zahlungen und Saldo. Die Erkennung ist sicher (hoch).
> - **Steuerrelevant als Beleg:** nein. Es ist ein Dokument des Steuerverfahrens und hat keinen Wert in der Steuererklärung.
> - **Einreichen:** nein.
> - **Keine Steuerbeleg-Kategorie:**
>   - «Belege eingereicht» und «Belege Sonstiges» passen nicht, weil der Auszug kein Beleg ist.
>   - «Unterlagen Kunde» passt nicht, weil es keine Information des Kunden ist.
>   - «Deklaration» passt nicht, weil es keine Steuererklärung ist.
> - **Beschreibung:** «Kontoauszug Steueramt St. Gallen», gemäss Ablageregel Dokumentart plus Aussteller. Bei mehreren Gemeinden oder Steuerarten ist das Datum des Auszugs sinnvoll.
> - **Eine Datei pro Auszug.** Sammel-PDFs trennen.
> 
> **Vorbehalt:** «Kontoauszug» steht in `KATEGORIEN.md` nur im Abschnitt «Weitere Klassen im Bereich Steuern». Diese Zuordnung stammt nicht aus der Zuordnungsliste, sondern aus dem Prozessbeschrieb vom 27.10.2026 und ist von consis noch zu bestätigen. Es ist eine Klasse, keine Kategorie mit M-Files-Eintrag.
> 
> Für Auszüge zur direkten Bundessteuer, falls einer dabei ist, hat das Wiki keine eigene Regel geliefert. Das habe ich nicht geprüft.

