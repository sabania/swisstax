# OpenClaw-Testlauf: ablage-agent-fragen.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 40 · Lauf: 2026-11-09 14:51
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## d01

**Frage:** Neuer Eingang (Kanton ZH, Steuererklärung 2025): «E-Mail von Muster Hans: «Grüezi, anbei wie gewünscht mein Lohnausweis 2025 von der Beispiel AG in Zürich. Die Spesenpauschale ist ja auf dem Formular drauf.» Anhang: LA_2025_Muster.pdf (Formular 11, Lohnausweis zur Steuererklärung)» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: lohnausweis. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen ZH 2025: ja (zh-wl-2025__c0032). Kategorie gemäss Liste consis: Belege eingereicht (Beispiel in der Liste: wird eingereicht).

**Antwort des Agenten** (27.4 s · Tools: 3 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read):

> **Ergebnis: Lohnausweis (Formular 11), steuerrelevant, Steuerjahr 2025, einreichen, Kategorie «Belege eingereicht».**
> 
> - **Dokumenttyp:** Lohnausweis (Formular 11) der Beispiel AG, Zürich. Sicherheit hoch. Die E-Mail und der Anhang-Titel stimmen überein; geprüft ist aber nur anhand des Textes, nicht des PDF-Inhalts.
> - **Steuerrelevant:** Ja. Der Lohnausweis liefert das Einkommen (Ziff. 8 Bruttolohn, Ziff. 11 Nettolohn) und die Spesen (Ziff. 13).
> - **Steuerjahr:** 2025 (Bescheinigungsjahr).
> - **Einreichen:** Ja. Im Kanton ZH 2025 sind Lohnausweise immer beizulegen, auch bei Nebenerwerb (§ 134 Abs. 1 lit. a StG; Wegleitung S. 31; Fundstelle zh-wl-2025__c0032).
> - **Kategorie:** «Belege eingereicht» (Eingereicht? = ja). Die Liste nennt den Lohnausweis ausdrücklich in dieser Kategorie, ohne «prüfen»-Vorbehalt. Beschreibung nach Ablageregel: «Lohnausweis Beispiel AG», Steuerjahr 2025.
> 
> **Zur Spesenpauschale:** Sie steht in Ziff. 13. Ob sie als steuerfrei ausgewiesen ist, entscheidet, ob für dieselben Auslagen ein zusätzlicher Berufskostenabzug entfällt. Das Spesenreglement des Arbeitgebers ist nur bedingt relevant und muss nicht eingereicht werden. Ob ein Abzug zulässig ist, prüfe ich, sobald die Ziff. 13 mit Betrag vorliegt.
> 
> **Offen vor der Abnahme:**
> 1. Das PDF öffnen und Ziff. 8, 9, 10, 11, 13 sowie die Felder F und G (Geschäftsfahrzeug, Kantinenverpflegung) gegen die Fundstellen prüfen.
> 2. Die Kategorieliste ist von consis noch nicht bestätigt.
> 3. Die E-Mail nennt keinen Nebenerwerb. Falls der Lohn als Nebenerwerb gilt, ändern sich die Positionen (Form. 360 Ziff. 5).

## d02

**Frage:** Neuer Eingang (Kanton SG, Steuererklärung 2025): «Portal-Upload von Muster Anna (Rorschach): Bescheinigung über Vorsorgebeiträge 2025, Beispiel Vorsorgestiftung 3a der Musterbank, gebundene Selbstvorsorge, einbezahlte Beiträge CHF 5'000.00, Formular 21 EDP.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: bescheinigung-saeule3a. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen SG 2025: ja (sg-form-1-2025__c0008). Kategorie gemäss Liste consis: Belege eingereicht (Beispiel in der Liste: wird eingereicht).

**Antwort des Agenten** (24.9 s · Tools: 2 Aufrufe steuerwiki__ablage, read):

> **Dokumenttyp:** Bescheinigung Säule 3a (Formular 21 EDP) der Bank- bzw. Versicherungsstiftung. Die Erkennung ist eindeutig, mit Punkten 2 gegenüber 1 für die nächstbeste Option (AHV-Beitragsverfügung).
> 
> **Steuerrelevant:** Ja. Die Bescheinigung belegt den Abzug der Säule-3a-Beiträge (SG 2025, Ziff. 13.1; Ziff. 3.2 ebenfalls genannt).
> 
> **Steuerjahr:** 2025, das Bescheinigungsjahr.
> 
> **Einreichen:** Ja. Im Kanton SG 2025 ist die Bescheinigung bei einem Abzug der Säule 3a immer einzureichen (Fundstelle sg-form-1-2025__c0008).
> 
> **Kategorie:** «Belege eingereicht», Zeile «Eingereicht?» = **ja**. Die Liste nennt «Bescheinigung Säule 3a» ausdrücklich mit «eingereicht: ja».
> 
> **Vorbehalte:**
> - Die Zuordnung ist als agent-geprüft markiert. Die Abnahme durch eine Fachperson steht noch aus, und die Kategorieliste ist von consis noch nicht bestätigt.
> - Die Beschreibung im Upload enthält das Wort «Beispiel» («Beispiel Vorsorgestiftung 3a der Musterbank»). Bitte prüfen, ob es sich um eine echte Bescheinigung handelt oder um ein Muster. Bei einem Muster wäre die Ablage nicht verbindlich.
> - Ich habe den Höchstbetrag für die Säule 3a 2025 nicht geprüft. Die CHF 5'000.00 sind damit nicht gegen die Limite abgeglichen.
> 
> **Vorschlag für die Beschreibung:** «Bescheinigung Säule 3a 2025 – Vorsorgestiftung Musterbank» (Mandant: Muster Anna, Rorschach).

## d03

**Frage:** Neuer Eingang (Kanton TG, Steuererklärung 2025): «Upload Mandantenportal, Muster Hans, Frauenfeld: «eSteuerauszug 2025 Beispielbank Thurgau» – Verzeichnis der Konten und Wertschriften per 31.12.2025 mit Barcode, Zusammenfassung Verrechnungssteuer A/B, 14 Seiten.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: steuerauszug-bank. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen TG 2025: bedingt (tg-wl-2025__c0168). Kategorie gemäss Liste consis: Belege eingereicht, falls Pflicht, wenn Titel nicht einzeln im Wertschriftenverzeichnis, sondern als Total gemäss Steuerauszug deklariert (WL c0036); dann Bestandteil des VSt-Antrags – sonst Belege Sonstiges.

**Antwort des Agenten** (29.4 s · Tools: 5 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg, steuerwiki__zeige):

> **Kurzantwort:** Steuerauszug der Bank (eSteuerauszug), steuerrelevant, Steuerjahr 2025. Einreichen ist **bedingt**. Kategorie: **Belege eingereicht**, wenn der Auszug eingereicht wird, sonst **Belege Sonstiges**.
> 
> **Dokumenttyp:** Steuerauszug der Bank / Post (inkl. eSteuerauszug). Erkennbar am Titel «eSteuerauszug» und am Barcode. Die Erkennung ist sicher (10 zu 0 Punkte), der Typ ist agent-geprüft, die Abnahme ist offen.
> 
> **Steuerrelevant:** ja. Der Auszug liefert Werte für das Vermögen (Steuerwerte per 31.12.2025), für die Erträge (Bruttoerträge mit und ohne Verrechnungssteuer) und für den Verrechnungssteueranspruch.
> 
> **Steuerjahr:** 2025 (Bescheinigungsjahr, eindeutig angegeben).
> 
> **Einreichepflicht (TG 2025, bedingt):** Einzureichen ist der Auszug nur, wenn die Titel im Wertschriften- und Guthabenverzeichnis (Formular 2) nicht einzeln, sondern als Total unter Erträge und Steuerwert deklariert werden. Fundstellen: WL TG 2025 S. 10 (`tg-wl-2025__c0036`) und S. 35 (`tg-wl-2025__c0168`). In diesem Fall bildet er Bestandteil des Verrechnungssteuer-Rückerstattungsantrags.
> 
> **Kategorie (KATEGORIEN.md):** Bank- und Depotauszüge gehören laut Liste zu «Belege eingereicht», sofern die Wegleitung des Kantons die Einreichung verlangt. Sonst gehören sie zu «Belege Sonstiges».
> - Werden die Totale übernommen: Kategorie **Belege eingereicht**, Zeile «Eingereicht?» = **ja**.
> - Werden die Titel einzeln deklariert: Kategorie **Belege Sonstiges**, «Eingereicht?» = **nein**.
> 
> **Offen:** Ob Hans' Steuererklärung die Titel einzeln oder als Total deklariert, entscheidet die Einreichung. Das bitte mit dem Mandanten bzw. der Fachperson klären. Bis dahin würde ich das Dokument unter «Belege eingereicht» mit dem Vermerk «bedingt» ablegen.

## d04

**Frage:** Neuer Eingang (Kanton AR, Steuererklärung 2025): «E-Mail Muster Anna, Herisau: «Hier noch das Schreiben der Bank zu unserem Haus, das Sie letztes Jahr auch hatten.» Anhang: Zinsbestätigung 2025, Festhypothek Nr. 1234.56, Saldo per 31.12.2025, belastete Hypothekarzinsen 01.01.–31.12.2025.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: hypothekarbestaetigung. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen AR 2025: auf verlangen (ar-form-05-2025__c0001). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (28.5 s · Tools: 3 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read):

> **Ergebnis: Hypothekarbestätigung (Zins- und Saldobestätigung), Steuerjahr 2025, nicht von sich aus einzureichen, Kategorie «Belege Sonstiges».**
> 
> - **Dokumenttyp:** Hypothekarbestätigung der Bank. Festhypothek Nr. 1234.56, Saldo per 31.12.2025 und bezahlte Hypothekarzinsen 01.01.–31.12.2025. Der Typ ist eindeutig erkannt (Punkte 16 gegenüber 1 für den nächsten Kandidaten).
> - **Steuerrelevant:** Ja. Der Saldo gehört in die Vermögens-/Schuldenangaben, die Zinsen in den Schuldzinsenabzug. Der Beleg ist agent-geprüft, die Abnahme durch Sie steht noch aus.
> - **Steuerjahr:** 2025, laut Bescheinigungsjahr.
> - **Einreichen im Kanton AR:** Nur auf Verlangen. Das Schuldenverzeichnis (Formular 5) verlangt die Belege «auf Verlangen», also nicht ungefragt.
> - **Kategorie:** Die Kategorienliste nennt die Hypothekarzinsbescheinigung ausdrücklich. Die Regel lautet: einzureichen → «Belege eingereicht», sonst «Belege Sonstiges». Da AR nur auf Verlangen einreichen lässt, gilt **«Belege Sonstiges», Eingereicht? = nein**. Sobald das Steueramt die Belege verlangt, wird der Beleg nach «Belege eingereicht» verschoben.
> 
> **Zu prüfen, bevor Sie ablegen:**
> 1. **Widerspruch in den Quellen:** Das Wiki sagt beim Beleg, das Schuldenverzeichnis sei der Steuererklärung «beizulegen». Formular 5 sagt dagegen «auf Verlangen». Ich habe die Formularquelle übernommen, weil sie wörtlich ist. Vor der Ablage bitte mit `position ar 2025 34.1` bestätigen, da der Wortlaut im Chunk durch Formularfelder unterbrochen ist.
> 2. **Zuordnung unbestätigt:** Die Kategorienliste ist laut ihrer Quellenangabe noch nicht bestätigt.
> 3. **Übertrag in die Erklärung:** Saldo 31.12.2025 → Ziff. 34.1 (Code 504, Form. 5 Teil A). Zinsen 2025 → Ziff. 11, abziehbar nur bis zu den steuerbaren Vermögenserträgen plus Fr. 50'000. Der Code für Ziff. 11 ist im Wiki nicht verifiziert.
> 4. **Amortisationen** sind nicht abziehbar; die Zinsen müssen vom Tilgungsbetrag getrennt werden.
> 
> Der Dateiname sollte nach Consis-Regel «Hypothekarbestätigung Muster Anna 2025» lauten. Die Kategorie ist ein Vorschlag. Die Entscheidung liegt bei Ihnen.

## d05

**Frage:** Neuer Eingang (Kanton TG, Steuererklärung 2025): «Portal-Upload Familie Muster, Weinfelden: Beispiel Krankenversicherung AG – Prämienbestätigung 2025 für Steuerzwecke, Grundversicherung KVG und Zusatzversicherungen VVG, abzüglich Prämienverbilligung, je versicherte Person.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: krankenkasse-praemien. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen TG 2025: unklar (tg-wl-2025__c0209). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (30.2 s · Tools: 4 Aufrufe steuerwiki__ablage, read, steuerwiki__zeige, steuerwiki__beleg):

> **Ergebnis: Krankenkassen-Prämienbescheinigung, steuerrelevant, Steuerjahr 2025, Kategorie «Belege Sonstiges» mit «Eingereicht?» = nein. Die Einreichepflicht im Kanton TG ist nicht eindeutig.**
> 
> **1. Dokumenttyp:** Krankenkassen-Prämienrechnung bzw. Jahresbescheinigung (Grund- und Zusatzversicherung), Wiki-Kürzel `krankenkasse-praemien`. Erkennung hoch (Punkte 12 vs. 0).
> 
> **2. Steuerrelevant:** Ja, zum Abzug. Die Prämien werden je versicherte Person in der TG-Erklärung 2025 eingetragen:
> - Kanton und Bund: Ziff. 14 (Form. 5.2, Code 330). Der Abzug ist begrenzt: Kanton CHF 7'000 (verheiratet), CHF 3'500 (alleinstehend) und CHF 1'000 je Kind; Bund CHF 3'700, CHF 1'800 und CHF 700 je Kind, jeweils nach Abzug von Säule 2/3a bzw. mit den dort genannten Erhöhungen.
> - Form. 5.2 A.1: selbst getragene Krankenversicherungsprämie, also netto nach erhaltener Prämienverbilligung (IPV). Die Prämienverbilligung wird abgezogen und nicht doppelt gekürzt.
> - Quelle: WL TG 2025, S. 44 (tg-wl-2025__c0209, c0210). Die Deklaration der Krankenversicherungsprämien wird vorausgesetzt.
> 
> **3. Steuerjahr:** 2025 (Bescheinigungsjahr, Angabe im Dokument).
> 
> **4. Einreichen:** Unklar, und die Wiki-Quellen widersprechen sich:
> - Chunk tg-wl-2025__c0209 sagt, dass die Deklaration vorausgesetzt wird. Eine Beilage der Prämienbescheinigung wird dort nicht ausdrücklich verlangt.
> - Die Wiki-Karte `beleg-krankenkasse-praemien` schreibt dagegen «Jahresbestätigung der Krankenkasse beilegen (WL TG 2025 S. 44)». Diesen Satz habe ich im geöffneten Chunk nicht gefunden.
> 
> Ich habe deshalb «nein» gewählt, weil die Ablageregel bei «unklar» so vorgibt. Das ist eine Annahme. Bitte die Wegleitung TG 2025, S. 44, im Original prüfen. Wenn die Beilage verlangt wird, wechselt die Kategorie zu «Belege eingereicht» mit «Eingereicht?» = ja.
> 
> **5. Kategorie (KATEGORIEN.md):** «Belege Sonstiges». Die Liste nennt «Versicherungsprämien (Prämienbescheinigung) (Sofern nicht einzureichen)» ausdrücklich. Die Zeile «Eingereicht?» steht auf nein, solange die Einreichepflicht nicht bestätigt ist.
> 
> **Offene Punkte:**
> - Einreichepflicht TG klären (siehe oben). Das ist der einzige Punkt, der die Kategorie ändern kann.
> - Die Prämien zählen nur, wenn die Deklaration der Prämien auf Formular 5 erfolgt.
> - Wenn das Dokument mehrere Personen betrifft, bitte je Person eine Zeile anlegen, weil die Abzugslimiten je Haushaltssituation gelten.

## d06

**Frage:** Neuer Eingang (Kanton SG, Steuererklärung 2025): «Foto per Handy hochgeladen von Muster Hans (Wil SG): Rechnung Zahnarztpraxis Dr. Beispiel, Behandlung März–Mai 2025, Wurzelbehandlung und Krone Zahn 36, Total CHF 2'480.–, Vermerk «nicht kassenpflichtig».» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: arzt-zahnarzt-rechnungen. Steuerrelevant: bedingt (Bedingung: Nur die selbst bezahlten Kosten (nach Abzug der Kassenleistungen), und nur soweit sie 5 % des Nettoeinkommens übersteigen; allgemeine Gesundheitsvorsorge (z. B. …). Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen SG 2025: auf verlangen (sg-wl-2025__c0073). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (36.3 s · Tools: 3 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read):

> **Dokumenttyp:** Arzt-/Zahnarztrechnung (Krankheitskosten), hier eine Zahnbehandlung. Die Erkennung ist eindeutig (13 Treffer gegen 1 für den nächsten Typ).
> 
> **Steuerrelevant: bedingt.** Die Rechnung ist relevant, aber nur für den Teil, den die Person selbst bezahlt hat:
> - **Selbst getragene Kosten:** Brutto abzüglich Leistungen Dritter (Krankenkasse, Unfallversicherung). Der Vermerk «nicht kassenpflichtig» spricht dafür, dass keine Kassenleistung fliesst, also Vorkolonne = CHF 2'480.–. Das ist mit einer Kassenabrechnung oder dem Zahlungsbeleg zu bestätigen.
> - **Selbstbehalt:** Abziehbar ist nur der Betrag über dem Selbstbehalt. Kanton SG: 2 % des Nettoeinkommens (Ziff. 20). Bund: 5 %. Ohne Nettoeinkommen kann ich den Abzug nicht beziffern.
> - **Zahlungsjahr:** Krankheitskosten sind im Jahr der Zahlung abziehbar. Die Behandlung war März–Mai 2025, das Rechnungsdatum fehlt aber. Ob die Zahlung 2025 erfolgte, ist offen.
> - **Empfänger:** Kosten für unterhaltene Personen sind nur abziehbar, wenn die Person tatsächlich unterstützt wird. Die Rechnung nennt den Patienten nicht; das ist zu prüfen.
> 
> **Steuerjahr:** 2025 (Bescheinigungsjahr laut Dokument), sofern die Zahlung 2025 erfolgte.
> 
> **Einreichen: nein, nur auf Verlangen.** Für SG 2025 gilt: Die Einzelrechnung in Formular 6 (Rückseite, Krankheitskosten) aufführen; Ziff. 21.1 (Vorkolonne Code 650, Abzug Code 240). Den Beleg selbst aufbewahren und auf Verlangen des Steueramts vorlegen.
> 
> **Kategorie: «Belege Sonstiges»** (Zeile «Krankheitskosten, sofern nicht einzureichen»). «Eingereicht?» = **nein**. Verlangt das Steueramt den Beleg, wird er zu «Belege eingereicht» (Eingereicht = ja).
> 
> **Offen, bevor die Werte übernommen werden:**
> 1. Zahlungsdatum und Zahlungsnachweis 2025.
> 2. Bestätigung, dass keine Kassenleistungen oder Dritten-Beiträge fliessen.
> 3. Nettoeinkommen (Ziff. 20) für die Berechnung des Selbstbehalts.
> 4. Patient bzw. Empfänger der Behandlung.
> 5. Das Foto ist für die Ablage kein Ersatz: Originalbeleg oder lesbare Kopie aufbewahren.
> 
> Die Angaben zur Person (Mandant) habe ich nicht im Wiki oder in MEMORY.md gespeichert.

## d07

**Frage:** Neuer Eingang (Kanton TG, Steuererklärung 2025): «E-Mail Muster Anna, Kreuzlingen: «Die Kita-Rechnungen fürs ganze Jahr habe ich zusammengefasst.» Anhang: Jahresübersicht 2025 Kita Sonnenschein Beispiel GmbH, Betreuung Muster Lea, 3 Tage/Woche, Elternbeitrag total CHF 14'600.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: kinderbetreuung-rechnungen. Steuerrelevant: bedingt (Bedingung: Nur für Kinder unter 14 Jahren, die im gleichen Haushalt leben wie die steuerpflichtige Person, die für den Unterhalt sorgt, und nur wenn die Kosten in …). Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen TG 2025: unklar (tg-wl-2025__c0096). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (39.2 s · Tools: 4 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg, steuerwiki__wert):

> **Dokumenttyp:** Jahresabrechnung einer Kita (Rechnungen Kinderbetreuung: Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule). Die Erkennung ist nur mittel sicher, weil die E-Mail auch andere Lesarten zulässt. Der Anhang selbst sollte bestätigt werden.
> 
> **Steuerrelevant:** bedingt. Die Kosten sind als Drittbetreuungsabzug relevant (TG 2025, Ziff. 15.3, Code 345). Voraussetzungen:
> - Das Kind ist unter 14 Jahre alt und lebt im gleichen Haushalt wie die steuerpflichtige Person. Das Alter von Lea ist in der E-Mail nicht angegeben und muss geprüft werden.
> - Die Betreuung hängt mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit zusammen. Bei 3 Tagen pro Woche braucht es einen Nachweis der Erwerbs- oder Ausbildungszeiten.
> - Verpflegung und andere Lebenshaltungskosten sind nicht abziehbar. Die Übersicht muss Betreuung und Verpflegung getrennt ausweisen. Ist das nicht der Fall, wird der Betrag gekürzt.
> - Subventionen oder Betreuungsgutscheine mindern den Abzug.
> 
> **Steuerjahr:** 2025. Die Übersicht ist als Jahresübersicht 2025 bezeichnet, und Steuerjahr ist das Bescheinigungsjahr.
> 
> **Einreichpflicht:** unklar. Der Abzug gilt für nachgewiesene Kosten. Ob die Rechnungen beizulegen sind, regelt die TG-Wegleitung 2025 nicht ausdrücklich (tg-wl-2025__c0096). Ich setze «Eingereicht?» auf **nein**, mit diesem Vorbehalt. Die Übersicht sollte trotzdem aufbewahrt werden, damit sie auf Verlangen vorliegt.
> 
> **Kategorie:** **Belege Sonstiges**. Die Kategorienliste nennt «Kinderbetreuungskosten (Sofern nicht einzureichen)» ausdrücklich unter dieser Kategorie. Eine Zuordnung nach Eingereicht-Status ist daher nicht nötig. Die Dokumentbeschreibung würde «Kita Sonnenschein, Jahresübersicht 2025» lauten, je nach Konvention.
> 
> **Mögliche Abzugshöhe TG 2025 (nur Richtwert, nicht geprüft):**
> - Kanton: In der Regel werden 75 % der nachgewiesenen Kosten anerkannt, höchstens CHF 10'100 pro Kind. Bei 14'600 CHF ergeben 75 % = 10'950 CHF, also greift die Kappe bei 10'100 CHF. Dies gilt nur, wenn der gesamte Betrag Betreuung ist. Ist ein Verpflegungsanteil enthalten, sinkt die Basis entsprechend.
> - Bund: Höchstbetrag CHF 25'800 pro Kind (Art. 33 Abs. 3 DBG 2025). Die 75-%-Regel habe ich für den Bund nicht bestätigt. Kanton und Bund sind getrennt zu deklarieren.
> 
> **Offene Punkte für die Sachbearbeitung:**
> 1. Alter von Lea (unter 14 am Stichtag?) und Wohnsitz im gleichen Haushalt.
> 2. Aufteilung Betreuung/Verpflegung in der Jahresübersicht.
> 3. Nachweis der Erwerbs- oder Ausbildungszeiten für 3 Tage pro Woche.
> 4. Erhaltene Subventionen.
> 5. Ob die TG-Steuerverwaltung die Rechnungen einfordert. Ist das der Fall, wechselt die Einreichpflicht auf «ja».
> 
> Die Fundstellen sind tg-stv__par-11c, tg-stg__par-34-t5 und bund-dbg-2025__art-33-t7. Sie sind agent-geprüft, die Abnahme ist offen.

## d08

**Frage:** Neuer Eingang (Kanton AR, Steuererklärung 2025): «Portal-Upload Muster Hans, Teufen AR: Spendenbestätigung 2025 der Stiftung Beispielhilfe Schweiz (gemeinnützig, steuerbefreit) – «Wir danken Ihnen für Ihre Zuwendungen von total CHF 600 im Jahr 2025.»» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: spendenbestaetigung. Steuerrelevant: bedingt (Bedingung: Nur Zuwendungen in Geld oder Vermögenswerten an steuerbefreite juristische Personen mit Sitz in der Schweiz (öffentliche/gemeinnützige Zwecke); …). Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen AR 2025: auf verlangen (ar-form-05-2025__c0003). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (28.4 s · Tools: 3 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg):

> **Ergebnis: Spendenbescheinigung, Steuerjahr 2025, steuerrelevant (bedingt), nicht einreichen, Kategorie «Belege Sonstiges»** (Kanton AR, Steuerjahr 2025)
> 
> - **Dokumenttyp:** Spendenbescheinigung einer gemeinnützigen Organisation (Jahresübersicht). Die Erkennung ist eindeutig (Sicherheit hoch).
> - **Steuerjahr:** 2025. Die Bescheinigung ist für 2025 ausgestellt.
> - **Steuerrelevant: bedingt.** Abzugsfähig ist es nur, wenn zwei Bedingungen erfüllt sind:
>   1. Die Empfängerin ist eine steuerbefreite juristische Person mit Sitz in der Schweiz. Die Bescheinigung nennt die Steuerbefreiung, aber nicht den Sitz. Beides ist vor dem Abzug zu prüfen, z. B. im Verzeichnis der steuerbefreiten Institutionen der kantonalen Steuerverwaltung AR.
>   2. Das Total aller Zuwendungen im Jahr erreicht die Mindestschwelle von CHF 100. Mit CHF 600 ist sie erfüllt. Der Abzug ist auf 20 % des Nettoeinkommens begrenzt.
> - **Einreichen: nein, nur auf Verlangen.** Im AR-Formular 5 (Rückseite, freiwillige Zuwendungen) heisst es, die Belege seien auf Verlangen einzureichen. Die Bescheinigung muss also nicht mit der Steuererklärung eingereicht werden, sondern ist bereitzuhalten.
> - **Kategorie:** «Belege Sonstiges». Die Kategorienliste nennt «Spendenbescheinigungen (Sofern nicht einzureichen)» ausdrücklich dort.
> - **Steuererklärung AR 2025:** Ziff. 21.3 (Code 550), übertragen aus Formular 5 Teil A (Institution, Datum, Betrag). Die Werte stammen aus dem Wiki-Eintrag und sind agent-geprüft, die Abnahme steht noch aus.
> 
> Vorbehalt: Die Kategorienliste ist laut ihrer Quelle noch nicht bestätigt. Die Zuordnung «Belege Sonstiges» gilt deshalb vorläufig.

## d09

**Frage:** Neuer Eingang (Kanton ZH, Steuererklärung 2025): «E-Mail Muster Anna, Uster: «Ich habe mir das Freizügigkeitsgeld auszahlen lassen, weil wir eine Wohnung gekauft haben.» Anhang: Beispiel Freizügigkeitsstiftung – Auszahlungsbestätigung Vorbezug WEF, Kapitalleistung CHF 80'000, Meldung an die ESTV erfolgt.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: kapitalleistung-vorsorge. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen ZH 2025: auf verlangen (zh-stg-2025__par-135). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (34.4 s · Tools: 3 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read):

> **Kurz:** Kapitalbezug aus der Vorsorge (WEF-Vorbezug). Steuerrelevant, Steuerjahr 2025 (sofern die Auszahlung 2025 erfolgte), nicht von sich aus einzureichen, Kategorie «Belege Sonstiges».
> 
> **Dokumenttyp:** Bescheinigung über eine Kapitalleistung aus Vorsorge (Freizügigkeitsstiftung, Vorbezug WEF). Erkennung: hoch.
> 
> **Steuerrelevant: ja.** Der Vorbezug für Wohneigentum ist keine steuerfreie Auszahlung. Er wird als Kapitalleistung im Jahr des Zuflusses besteuert. Die Meldung an die ESTV ist ein Verfahrensvorgang und ersetzt die Deklaration nicht.
> 
> **Steuerjahr: 2025**, massgebend ist das Auszahlungsdatum. Das Dokument im Eingang zeigt kein Datum. Bitte prüfen, ob die Auszahlung 2025 erfolgte. Falls nicht, ist das Steuerjahr 2026.
> 
> **Einreichen: nein, nur auf Verlangen.** Im ZH-Formular (Ziff. 40, Code 510) ist keine Bescheinigung als Beilage verlangt. Bei mehreren Kapitalleistungen ist eine Aufstellung mit Datum und Betrag je Leistung einzureichen (zh-stg-2025__par-135, WL Ziff. 40). Die Steuerbehörde kann die Bescheinigung jederzeit verlangen, daher aufbewahren.
> 
> **Kategorie: «Belege Sonstiges»**, Eingereicht? = nein.
> - Die Liste nennt Kapitalleistungen nicht ausdrücklich. Die Regel der Liste greift: Der Beleg hat einen Wert in der Deklaration, muss aber nicht eingereicht werden.
> - Die Zuordnung ist laut Liste noch nicht von consis bestätigt.
> 
> **Für die Erklärung ZH 2025:**
> - Betrag der Kapitalleistung (hier CHF 80'000) unter Ziff. 40 erfassen. Sie wird gesondert besteuert, nicht über die Einkünfte.
> - Kanton: Satz für einen Zwanzigstel der Leistung, einfache Staatssteuer mindestens 2 %, keine Sozialabzüge (zh-stg-2025__par-37, § 37 StG ZH).
> - Bund: ein Fünftel der Tarife nach Art. 36 DBG, keine Sozialabzüge (Art. 38 DBG).
> - Ich habe die Steuerbeträge nicht berechnet. Dafür fehlen Angaben wie Zivilstand und übrige Einkünfte.
> 
> **Offene Punkte:**
> - Auszahlungsdatum im Dokument prüfen (Steuerjahr).
> - Falls das WEF-Geld später zurückbezahlt wird, ist das relevant. Die Rückzahlung muss dann separat geprüft werden.
> - Die Ablage-Zuordnung ist mit consis zu bestätigen.
> 
> Quelle: `beleg kapitalleistung-vorsorge` (ZH 2025), Status ☑️ agent-geprüft, Abnahme durch die Fachperson offen.

## d10

**Frage:** Neuer Eingang (Kanton SG, Steuererklärung 2025): «Weitergeleitet von Muster Hans, Gossau SG: «Heute im Briefkasten, können Sie das bitte kontrollieren?» Anhang: Kantonales Steueramt St. Gallen, Veranlagungsverfügung Steuerperiode 2025, Staats- und Gemeindesteuer sowie direkte Bundessteuer, mit Rechtsmittelbelehrung.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: veranlagung (Veranlagungsverfügung / Einschätzungsentscheid / definitive Steuerrechnung (Bund, Kanton/Gemeinde, Kapitalleistung)). Kein Steuerbeleg. Kategorie gemäss Liste consis: Klasse «Veranlagung + def. Steuerrechnung» (weitere Klassen, nicht aus der Liste).

**Antwort des Agenten** (26.0 s · Tools: 2 Aufrufe steuerwiki__ablage, read):

> **Ergebnis: Veranlagungsverfügung SG 2025, kein Steuerbeleg, nicht einzureichen.**
> 
> - **Dokumenttyp:** Veranlagungsverfügung (Verfügung des Steueramts über die Veranlagung), Staats- und Gemeindesteuer sowie direkte Bundessteuer. Die Erkennung ist mit hoher Sicherheit.
> - **Steuerrelevant?** Als Beleg nein. Es ist ein Dokument des Steuerverfahrens und trägt keinen Wert für die Steuererklärung. Es ist aber verfahrensrelevant: Es zeigt, wie die Behörde die eingereichte Erklärung veranlagt hat.
> - **Steuerjahr:** 2025. Gemeint ist die veranlagte Steuerperiode, nicht das Ausstellungsjahr.
> - **Einreichen?** Nein. Es ist kein Beleg, der an das Steueramt geht.
> - **Kategorie:** Keine Belegkategorie. Die Liste `KATEGORIEN.md` enthält keine Zeile für Veranlagungen. Die Ablage erfolgt in die Klasse **«Veranlagung + def. Steuerrechnung»**. Diese Klasse steht im Ablageschema von consis (Prozessbeschrieb vom 27.10.2026) und ist noch nicht bestätigt.
> 
> **Zu prüfen:**
> - Die **Rechtsmittelfrist** steht in der beiliegenden Rechtsmittelbelehrung. Ich habe sie nicht nachgeschlagen. Wenn die Frist für eine Einsprache läuft, sollte sie heute notiert werden. Ich kann die Frist im Steuer-Wiki für SG 2025 suchen, falls gewünscht.
> - Die Verfügung sollte mit der eingereichten Steuererklärung 2025 von Herrn Muster verglichen werden. Weichen die Beträge ab, ist das ein Fall für Einsprache oder Rückfrage.
> - Falls das Steueramt zusätzlich eine Auflage oder Nachfrage geschickt hat, gehört diese in die Klasse «Auflage/Buchprüfung» und nicht in diese Veranlagung.

## d11

**Frage:** Neuer Eingang (Kanton ZH, Steuererklärung 2025): «E-Mail Gemeindesteueramt Beispielhausen ZH an die Treuhand: Bestätigung Ihres Gesuchs – die Frist zur Einreichung der Steuererklärung 2025 für Muster Hans und Anna wird bis 30.09.2026 erstreckt.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: fristerstreckung (Fristerstreckungsgesuch / Bestätigung Fristerstreckung). Kein Steuerbeleg. Kategorie gemäss Liste consis: Fristenliste NP.

**Antwort des Agenten** (25.2 s · Tools: 2 Aufrufe steuerwiki__ablage, read):

> **Ergebnis: Fristerstreckung-Bestätigung, kein Steuerbeleg. Kategorie «Fristenliste NP», nicht einreichen.**
> 
> - **Dokumenttyp:** Bestätigung einer Fristerstreckung (Gesuchsbestätigung des Gemeindesteueramts Beispielhausen) für die Steuererklärung natürlicher Personen.
> - **Steuerrelevant:** Nein. Es ist ein Dokument des Steuerverfahrens, kein Beleg. Es hat keinen Wert in der Steuererklärung.
> - **Steuerjahr:** 2025 (Steuererklärung 2025).
> - **Einreichen:** Nein. Die Bestätigung wird nicht als Beleg eingereicht.
> - **Kategorie:** «Fristenliste NP». Die Kategorienliste nennt «Fristerstreckungsgesuch / Bestätigung Fristerstreckung NP» ausdrücklich bei dieser Kategorie. Sie dient nur der Fristenkontrolle und Verlängerung und ist nicht für Belege bestimmt. «Eingereicht?» = nein.
> 
> **Zu prüfen:**
> 
> 1. **Frist ist abgelaufen.** Die verlängerte Frist war der 30.09.2026. Heute ist der 09.11.2026. Bitte klären, ob die Steuererklärung 2025 für Muster Hans und Anna inzwischen eingereicht wurde. Falls nicht, ist die Frist verpasst und das Gemeindeamt sollte kontaktiert werden.
> 2. **Kategorie ist noch nicht bestätigt.** Die Kategorienliste ist laut Quelle von consis noch nicht bestätigt. Die Zuordnung «Fristenliste NP» ist aber eindeutig, weil die Liste den Dokumenttyp ausdrücklich nennt.
> 3. **Gesuchsart unklar.** Ob es ein Einzel- oder Sammelgesuch war, geht aus der E-Mail nicht hervor. Das betrifft nur die Fristenliste, nicht die Einreichepflicht.

## d12

**Frage:** Neuer Eingang (Kanton AR, Steuererklärung 2025): «Scan vom Mandanten hochgeladen, Muster Anna (Speicher): Kantonale Steuerverwaltung Appenzell Ausserrhoden – Auflage zur Steuererklärung 2025. Bitte reichen Sie innert 30 Tagen Belege zu den geltend gemachten Weiterbildungskosten und den Fahrkosten ein.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: auflage-nachfrage (Auflage / Nachfrage / Buchprüfung des Steueramts). Kein Steuerbeleg. Kategorie gemäss Liste consis: Klasse «Auflage/Buchprüfung».

**Antwort des Agenten** (35.3 s · Tools: 4 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg):

> **Dokumenttyp:** Auflage bzw. Nachfrage der Steuerbehörde (Verfahrensdokument), kein Beleg. Die Erkennung ist sicher.
> 
> **Ist es steuerrelevant?**
> - **Das Schreiben selbst:** nein. Es ist kein Steuerbeleg und enthält keinen Wert für die Steuererklärung.
> - **Die verlangten Unterlagen:** ja, aber nur wenn sie tatsächlich deklariert wurden.
>   - *Weiterbildungskosten* (AR 2025, Ziff. 16.4): nur berufsorientierte Aus- und Weiterbildung abziehbar, Maximum Fr. 12'000 pro Person. Hobbykurse und vom Arbeitgeber bezahlte Kosten fallen weg.
>   - *Fahrkosten* (Form. 4, Ziff. 1.1): relevant vor allem als ÖV-Abo für den Arbeitsweg, begrenzt auf Fr. 6'000. Nicht abziehbar, wenn der Arbeitgeber die Fahrt unentgeltlich stellt (Lohnausweis Feld F).
> 
> **Steuerjahr:** 2025.
> 
> **Muss es eingereicht werden?**
> - **Das Schreiben:** nein. Es ist die Aufforderung und wird nicht eingereicht.
> - **Die Belege:** ja. Nach der AR-Wegleitung 2025 sind Abzugsbelege grundsätzlich bereitzuhalten und auf Verlangen einzureichen. Mit dieser Auflage ist das Verlangen gestellt, also innert 30 Tagen.
> - **Frist:** Das Schreiben nennt 30 Tage, ab dem Datum der Zustellung. Ich habe kein Datum des Schreibens; ab heute (09.11.2026) wären es etwa 09.12.2026. Bitte das Datum auf dem Schreiben prüfen.
> 
> **Kategorie** (Kategorienliste `KATEGORIEN.md`; die Liste ist laut Datei noch nicht bestätigt):
> 1. **Das Auflage-Schreiben:** Klasse «Auflage/Buchprüfung». Diese Klasse steht im consis-Prozessbeschrieb, nicht in der Kategorienliste. Sie ist keine Steuerbeleg-Kategorie.
> 2. **Die Belege zu Weiterbildung und Fahrkosten:** «Belege eingereicht», Zeile «Eingereicht?» = ja, Beschreibung nach Dokumentart und Aussteller, Steuerjahr 2025. Die Liste ordnet Weiterbildungsnachweise sonst unter «Belege Sonstiges» ein. Sobald sie verlangt und eingereicht werden, wechseln sie nach «Belege eingereicht».
> 
> **Offen:**
> - Bitte prüfen, welche Belege Anna in der Erklärung 2025 tatsächlich geltend gemacht hat. Nur diese werden verlangt.
> - Die Kategorienzuordnung ist laut `KATEGORIEN.md` noch nicht von consis bestätigt.

## d13

**Frage:** Neuer Eingang (Kanton SG, Steuererklärung 2025): «E-Mail Muster Anna, Buchs SG: «Zu Ihren Fragen: Wir haben 2025 nichts geerbt, kein Auto gekauft, und unser Sohn macht seit August die Lehre bei der Beispiel AG. Die 3a-Bescheinigung reiche ich noch nach. Liebe Grüsse»» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: kundenantwort (Antworten, Bestätigungen und Checklisten des Kunden, Kundenfreigabe per E-Mail). Kein Steuerbeleg. Kategorie gemäss Liste consis: Unterlagen Kunde.

**Antwort des Agenten** (30.1 s · Tools: 2 Aufrufe steuerwiki__ablage, read):

> **Kurzfassung:** Das ist keine Steuerbeleg-Bescheinigung, sondern eine **Kundenantwort per E-Mail** auf Pendenzen. Es gehört in «Unterlagen Kunde», nicht in «Belege eingereicht». Das Tool hat es als Säule-3a-Bescheinigung erkannt, das ist falsch: die Bescheinigung wird nur angekündigt, ist nicht im Text.
> 
> **1. Dokumenttyp:** Kundenmail mit Antworten auf Fragen/Pendenzen (Erbschaft, Autokauf, Lehre des Sohnes, angekündigte 3a-Bescheinigung). Kein Beleg im engeren Sinn.
> 
> **2. Steuerrelevant?** Der Mail selbst: nicht als Steuerbeleg, aber für die Erklärung inhaltlich wichtig.
> - Erbschaft 2025 verneint: keine Erbschaftssteuer- bzw. Erbschaftsposition für 2025.
> - Autokauf verneint: kein Fahrzeug-Beleg nötig.
> - Sohn in Lehre seit August: Hinweis auf Lehrlingslohn und Ausbildungsabzug. Dafür braucht es einen Lohnausweis der Beispiel AG. Ob und wie der Sohn dadurch steuerlich wirkt, prüfe ich nicht weiter, weil das nicht Teil deiner Frage war; sag Bescheid, wenn ich das mit `position sg 2025 …` nachschlagen soll.
> - 3a-Bescheinigung: steuerrelevant und einzureichen (SG 2025, Ziff. 13.1, Form. 21 EDP), sobald sie eintrifft. Das Tool meldete «☑️ agent-geprüft, Abnahme offen».
> 
> **3. Steuerjahr:** 2025 (Steuererklärung 2025, SG). Das Mail-Datum ist 09.11.2026. Das ist später als die übliche Abgabefrist, daher ggf. Fristerstreckung prüfen.
> 
> **4. Einreichen und Kategorie:**
> - **Kategorie: «Unterlagen Kunde»** (Antworten des Kunden auf Fragen/Pendenzen per E-Mail; Liste-Beispiel «Kundenfreigabe per E-Mail» bzw. «Antworten des Kunden auf Fragen»).
> - **Eingereicht?** nein. Die Mail wird nicht beim Steueramt eingereicht.
> - Die künftige **3a-Bescheinigung** kommt später in «Belege eingereicht» (Eingereicht? ja), Beschreibung z. B. «Bescheinigung Säule 3a Anna, Buchs» (Steuerjahr 2025).
> 
> **Offen:**
> - Lohnausweis bzw. Lehrvertrag des Sohnes: noch nicht angefordert; im Mail nicht enthalten. Vorschlag: nachfordern.
> - Die Liste selbst ist laut Kopf noch nicht bestätigt; die Zuordnung «Unterlagen Kunde» ist daher mit Vorbehalt.

## d14

**Frage:** Neuer Eingang (Kanton ZH, Steuererklärung 2025): «Portal-Upload Muster Hans, Winterthur: Freigabequittung zur elektronisch eingereichten Steuererklärung 2025, Kanton Zürich, unterschrieben von beiden Ehegatten, mit Freigabecode und Datum.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: freigabequittung (Freigabe-/Unterschriftsquittung zur (elektronisch eingereichten) Steuererklärung). Kein Steuerbeleg. Kategorie gemäss Liste consis: Deklaration (vorläufig, zu bestätigen).

**Antwort des Agenten** (31.7 s · Tools: 4 Aufrufe steuerwiki__ablage, read, steuerwiki__suche, steuerwiki__zeige):

> **Ergebnis: Verfahrensdokument, nicht steuerrelevant als Beleg, Steuerjahr 2025, nicht als Beleg einzureichen. Kategorie «Deklaration» (mit Vorbehalt).**
> 
> **1. Dokumenttyp:** Freigabequittung zur elektronisch eingereichten Steuererklärung (Erkennung: mittel, Sicherheit 8.5 gegenüber 0 Punkten). Die gemeinsame Unterschrift beider Ehegatten bestätigt, dass die Steuererklärung wahrheitsgemäss und vollständig ist. Der Freigabecode ist die elektronische Bestätigung.
> 
> **2. Steuerrelevant?** Nein, nicht als Beleg. Das Dokument enthält keinen Wert für die Deklaration. Es ist ein Dokument des Steuerverfahrens.
> 
> **3. Steuerjahr:** 2025 (Bescheinigungsjahr laut Dokument).
> 
> **4. Einreichen?** Nicht als Beleg.
> - Nach § 8 Abs. 1 und 2 der V elektr. Einreichung ZH gilt die Steuererklärung als eingereicht, sobald die Ehegatten sie gemeinsam elektronisch bestätigt und übermittelt haben (Fundstelle `zh-v-einreichung__par-8`, Status ☑️ agent-geprüft).
> - Nach § 8 Abs. 4 sind nur die erforderlichen Beilagen elektronisch einzureichen. Die Quittung selbst wird dort nicht als Beilage genannt.
> - Offen: Ich habe keine Einreichungsregel für ZH gefunden, die eine Papierquittung zusätzlich verlangt. Diese Prüfung habe ich nicht vollständig gemacht. Ob die Gemeinde (Winterthur) die unterschriebene Quittung trotzdem auf Papier will, müsste man in der Wegleitung ZH nachsehen.
> 
> **5. Kategorie: «Deklaration»** (Zeile «Unterzeichnete Freigabequittung (DeepSign oder Papier)»).
> - Die Liste nennt diese Dokumentart ausdrücklich. Die Zuordnung ist aber nur als «Vorschlag, zu prüfen» markiert. Die Liste selbst vermerkt zudem «Offen: Deklaration oder Unterlagen Kunde?».
> - Die Liste gibt für diese Zeile «eingereicht: ja (Post)» an. Das passt nicht zu meiner Prüfung oben. Ich würde «Eingereicht?» deshalb auf **nein** setzen und den Konflikt bei consis klären.
> - Alternative, falls consis die Quittung als Kundenunterlage führt: «Unterlagen Kunde». Die Zeile «Kundenfreigabe per E-Mail» betrifft aber eine andere Dokumentart.
> 
> **Ablage-Hinweis:** Beschreibung nach Liste «Freigabequittung», Steuerjahr 2025, Mandant Hans (Winterthur).

## d15

**Frage:** Neuer Eingang (Kanton TG, Steuererklärung 2025): «Systemmeldung Steuersoftware: Übermittlungsbestätigung – Die Steuererklärung 2025 von Muster Hans, Arbon TG, wurde erfolgreich an die Steuerverwaltung des Kantons Thurgau übermittelt. Eingangsnummer TG-2026-0815, Zeitstempel 14.03.2026 10:42.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: uebermittlungsquittung (Übermittlungs-/Eingangsquittung der eingereichten Steuererklärung). Kein Steuerbeleg. Kategorie gemäss Liste consis: Übermittlungsbestätigung.

**Antwort des Agenten** (27.3 s · Tools: 2 Aufrufe steuerwiki__ablage, read):

> **Dokumenttyp:** Übermittlungsquittung (Übermittlungsbestätigung) der Steuersoftware. Sie bestätigt, dass die Steuererklärung 2025 an die Steuerverwaltung TG übermittelt wurde. Die Erkennung ist mittel sicher, weil das Dokument auch Merkmale eines Steuerformulars nennt.
> 
> **Steuerrelevant?** Nein. Es ist kein Steuerbeleg und enthält keinen Wert für die Steuererklärung. Es belegt nur den Einreichungsvorgang.
> 
> **Steuerjahr:** 2025, weil die Quittung die Steuererklärung 2025 betrifft. Der Zeitstempel 14.03.2026 ist das Übermittlungsdatum und nicht das Steuerjahr. Nach der Ablageregel ist das Steuerjahr das Bescheinigungsjahr. Ob das hier 2025 oder 2026 ist, sollte kurz geprüft werden.
> 
> **Einreichen?** Nein. Die Quittung wird nicht an die Steuerverwaltung geschickt, sie ist die Bestätigung, dass dort eingereicht wurde.
> 
> **Kategorie:** «Übermittlungsbestätigung» aus `KATEGORIEN.md`, Spalte «Eingereicht?» = nein. Die Liste nennt diese Dokumentart ausdrücklich («Übermittlungsquittung Online-Übermittlung»). Der Eintrag ist nicht als «prüfen» markiert.
> 
> Hinweis: Diese Kategorie gehört nicht zu den Steuerbelegen. Die Zuordnung ist laut Liste noch nicht von consis bestätigt.

## d16

**Frage:** Neuer Eingang (Kanton AR, Steuererklärung 2025): «E-Mail Muster Hans, Heiden: «Ich hab noch etwas Bitcoin und Ether, hier der Export.» Anhang: Beispiel Exchange AG – Annual Statement 2025, Bestand per 31.12.2025: 0.42 BTC, 3.1 ETH, Wallet-Adresse, Transaktionsliste.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: krypto-auszug. Steuerrelevant: bedingt (Bedingung: Nur wenn Kryptowährungen gehalten werden (Bestand per 31.12. und Erträge wie Staking/Lending deklarieren).). Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen AR 2025: unklar. Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (39.6 s · Tools: 5 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg, steuerwiki__suche, steuerwiki__zeige):

> **Ablage: Krypto-Auszug, AR, Steuerjahr 2025**
> 
> - **Dokumenttyp:** Krypto-Auszug (Exchange-/Wallet-Auszug mit Jahresendbestand). Die Erkennung ist eindeutig (14 gegen 0 Punkte), die Dokumentart steht im Wiki unter `krypto-auszug`.
> - **Steuerrelevant: ja, bedingt erfüllt.** Die Bedingung ist «Kryptowährungen gehalten» (Bestand per 31.12.). Mit 0.42 BTC und 3.1 ETH per 31.12.2025 ist sie erfüllt. Die Bestände sind Vermögen (Ziff. 30.1, Code 300). Erträge aus Staking, Lending, Airdrops oder Mining, die in der Transaktionsliste stehen, sind Einkommen (Ziff. 4.1 / Form. 2).
> - **Steuerjahr:** 2025, Stichtag 31.12.2025 (Bescheinigungsjahr).
> - **Einreichen: nicht eindeutig.** Die AR-Wegleitung (WL AR 2025, S. 22, `ar-wl-2025__c0129`) verlangt Beilagen in zwei Fällen:
>   - Bankauszüge (Steuerauszüge) sind vollständig beizulegen, wenn ihr Gesamtbetrag ins Verzeichnis übertragen wird.
>   - Ein selbst erstelltes Verzeichnis ist zusammen mit Formular 2 einzureichen.
> 
>   Ein Exchange-/Wallet-Export wird nicht ausdrücklich genannt. Wenn Sie die Werte direkt aus dem Export ins Formular übernehmen, gibt es keine Beilagepflicht. Wenn Sie daraus ein eigenes Verzeichnis erstellen, muss dieses mit Formular 2 eingereicht werden.
> - **Kategorie: Belege Sonstiges.** Die Liste nennt «Nachweis Kryptowährungen (z. B. Bitcoin)» ausdrücklich in dieser Kategorie. «Eingereicht?» = **nein**, mit dem Vorbehalt aus dem Punkt oben: Wird ein eigenes Verzeichnis gebildet, ist es einzureichen und gehört in die Kategorie «Belege eingereicht».
> 
> **Offen für die Erfassung:**
> 1. CHF-Werte fehlen. Bestand zum ESTV-Jahresendkurs per 31.12.2025 umrechnen, Ziff. 30.1 und Form. 2 (Spalte A/B) befüllen.
> 2. Transaktionsliste auf Staking-, Lending- oder Zinserträge prüfen (Ziff. 4.1).
> 3. Der Titel lautet «Beispiel Exchange AG». Bitte bestätigen, dass es sich um den echten Export des Mandanten handelt.
> 4. Die Einreichungsfrage (Beilage ja/nein) sollte das AR-Steueramt oder die Fachperson bestätigen. Das Wiki kann das nicht abschliessend klären.
> 
> Ich habe keine Mandantendaten im Wiki oder im Gedächtnis gespeichert.

## d17

**Frage:** Neuer Eingang (Kanton TG, Steuererklärung 2025): «Portal-Upload Muster Anna, Amriswil: Verfügung der Schätzungsbehörde – Neuschätzung Einfamilienhaus Parzelle Nr. 1234, neuer Steuerwert und Eigenmietwert, gültig ab Steuerperiode 2026, mit Rekursmöglichkeit.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: liegenschaft-schaetzung-eigenmietwert. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen TG 2025: unklar (tg-wl-2025__c0239). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (30.6 s · Tools: 5 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg, steuerwiki__zeige):

> **Ergebnis: Schätzungsverfügung (Steuerwert und Eigenmietwert, TG). Steuerrelevant, Steuerjahr 2026, nicht als Beleg einzureichen (unsicher), Kategorie «Belege Sonstiges».**
> 
> **Dokumenttyp:** Verfügung der Schätzungsbehörde zur Liegenschaftenschätzung, also Steuerwert und Eigenmietwert (Karte `liegenschaft-schaetzung-eigenmietwert`, ☑️ agent-geprüft, Abnahme offen). Die Rekursmöglichkeit ist typisch für diese Verfügung und macht sie nicht zu einem Verfahrensdokument.
> 
> **Steuerrelevant: ja.**
> - Steuerwert: Vermögen, kantonal. Massgebend ist der rechtskräftige amtliche Verkehrswert am Ende der Steuerperiode (`tg-wl-2026__c0221`, Formular 7).
> - Eigenmietwert: Einkommen, Kanton und Bund (`tg-stp-23-1__c0004`, StP 23 Nr. 1 Ziff. 3.3).
> 
> **Steuerjahr: 2026.** Das Dokument gilt ab Steuerperiode 2026, daher gehört es in die Erklärung 2026, nicht 2025. ⚠️ Ihre Anfrage nennt die Steuererklärung 2025. Prüfen Sie, ob die Verfügung vor dem 31.12.2025 rechtskräftig eröffnet wurde. Falls ja, wäre sie für 2025 relevant; das Wiki sagt dazu nichts Belastbares.
> 
> **Einzureichen: nicht geklärt, daher «Eingereicht?» = nein.** Die TG-Wegleitung 2026 nennt keine Beilagepflicht für amtliche Schätzungswerte. Die Einreichepflicht ist im Wiki als «unklar» markiert, nicht als «nein». Bei Unsicherheit bitte die Wegleitung 2026 direkt prüfen.
> 
> **Kategorie:** Die Dokumentart steht nicht ausdrücklich in `KATEGORIEN.md`. Nach der Regel «nicht eingereicht, aber wertrelevant» gehört sie in **Belege Sonstiges** (Eingereicht? = nein). Die Klasse «Einsprache/Rekurs» passt nur, wenn tatsächlich Rekurs eingelegt wird. Die Liste ist laut Kopfzeile noch nicht bestätigt.
> 
> **Wo die Werte in der Erklärung TG 2026 stehen:**
> - Ziff. 8.1 (Formular 7, Code 180): Mietwert selbstgenutzt, abzüglich Selbstnutzungsabzug.
> - Ziff. 31 (Formular 7, Code 430): Steuerwert der Liegenschaft.
> - Der Mietwert ist indexiert. Den indexierten Wert 2026 finden Sie in der Liegenschaftensteuerrechnung 2027 (Januar 2027).
> 
> ⚠️ Das Wiki ist uneinheitlich beim Bund-Selbstnutzungsabzug: Die Rechenregel nennt Bund 20 %, die Limite-Angabe «Bund nicht anwendbar». Bitte mit `position tg 2026 8.1` gegenprüfen, bevor Sie rechnen.

## d18

**Frage:** Neuer Eingang (Kanton AR, Steuererklärung 2025): «E-Mail Muster Hans, Herisau: «Weiss nicht ob ihr das braucht, schicke mal alles.» Anhang: Beispiel Telecom AG, Rechnung Oktober 2025, Mobile-Abo und Internet privat, CHF 89.90.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: privatrechnungen-alltag. Steuerrelevant: nein. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen AR 2025: nein (ar-stg__art-37). Kategorie gemäss Liste consis: keine Steuerbeleg-Kategorie (nicht steuerrelevant).

**Antwort des Agenten** (25.7 s · Tools: 3 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read):

> **Ergebnis: nicht steuerrelevant, keine Einreichung, keine Steuerbeleg-Kategorie.**
> 
> - **Dokumenttyp:** Private Alltagsrechnung (Telekom/Internet), Kategorie „Private Alltagsrechnungen“ im Wiki. Aussteller: Beispiel Telecom AG, Rechnung Oktober 2025, Mobile-Abo und Internet privat, CHF 89.90.
> - **Steuerrelevant:** Nein. Telefon- und Internetkosten für den Privatgebrauch sind Lebenshaltungskosten und nach Art. 34 lit. a DBG bzw. Art. 37 Abs. 1 lit. a StG AR nicht abziehbar (ar-wl-2025__c0170). Sie gehen nicht in eine Position der Steuererklärung AR 2025. Status: ☑️ agent-geprüft, Abnahme offen.
> - **Steuerjahr:** 2025 (Bescheinigungsjahr der Rechnung vom Oktober 2025).
> - **Einreichen:** Nein.
> - **Kategorie:** Keine Steuerbeleg-Kategorie, weil das Dokument nicht steuerrelevant ist. Die Rechnung selbst gehört damit nicht in „Belege Sonstiges“ oder „Belege eingereicht“.
> - **Begleit-E-Mail von Hans:** Die E-Mail ist eine Kundenmitteilung ohne Steuerwert. Sie passt zur Kategorie **Unterlagen Kunde** (Eingereicht: nein). Das ist eine Zuordnung nach der Liste, die ich nicht selbst bestätigen kann.
> 
> **Offen:** Die Rechnung wäre nur dann relevant, wenn Hans Mobile oder Internet beruflich nutzt (z. B. Homeoffice). Das wäre mit Hans zu klären. Die Gemeinde ist Herisau, also Wohnsitz im Kanton AR; das ist für diese Einordnung unkritisch.

## d19

**Frage:** Neuer Eingang (Kanton ZH, Steuererklärung 2025): «Portal-Upload Muster Anna, Dietikon: Beispiel Versicherungen AG – Police Hausrat- und Privathaftpflichtversicherung, Versicherungssumme Hausrat CHF 100'000, Jahresprämie 2026 CHF 412.–, Vertragsbeginn 01.01.2026.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: hausrat-haftpflicht-police. Steuerrelevant: nein. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen ZH 2025: nein (zh-stg-2025__par-31-t2). Kategorie gemäss Liste consis: keine Steuerbeleg-Kategorie (nicht steuerrelevant).

**Antwort des Agenten** (26.0 s · Tools: 3 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg):

> **Ergebnis: kein Steuerbeleg, daher keine Kategorie.**
> 
> - **Dokumenttyp:** Police Hausrat- und Privathaftpflichtversicherung (Wiki-Beleg `hausrat-haftpflicht-police`).
> - **Steuerrelevant:** nein. Im Kanton ZH sind nur Prämien für Lebens-, Kranken- und Unfallversicherungen abziehbar (§ 31 Abs. 1 lit. g StG ZH, Quelle `zh-stg-2025__par-31-t2`). Hausrat- und Privathaftpflichtprämien gehören nicht dazu. Der Hausrat ist zudem steuerfrei und wird nicht deklariert, der Versicherungswert ist keine Vermögensposition. Die Einschätzung ist agent-geprüft, die Abnahme durch die Fachperson steht aus.
> - **Steuerjahr:** 2026. Das Dokument nennt Jahresprämie 2026 und Vertragsbeginn 01.01.2026, also ist 2026 das Bescheinigungsjahr. Das Tool hat 2025 vorgeschlagen, weil es die häufigste Jahreszahl im Text ist. Für die Steuererklärung 2025 ist das Dokument ohnehin nicht relevant.
> - **Einreichen:** nein. Es muss nicht eingereicht werden und hat keine Formularposition in ZH 2025.
> - **Kategorie:** keine Steuerbeleg-Kategorie. Die Liste hat «Versicherungsprämien (Prämienbescheinigung)» nur unter «Belege Sonstiges» und nur für abziehbare Prämien. Diese Police trifft das nicht, also wird sie nicht dort abgelegt. Falls die Kanzlei sie trotzdem archivieren will, wäre das außerhalb der Steuerbeleg-Kategorien zu entscheiden.
> 
> Hinweis: Die Liste «KATEGORIEN.md» ist laut Kopfzeile noch nicht bestätigt. Die Zuordnung zu «keine Kategorie» beruht auf der Regel für nicht steuerrelevante Dokumente.

## d20

**Frage:** Neuer Eingang (Kanton SG, Steuererklärung 2025): «E-Mail Muster Hans, Rapperswil-Jona: «Noch die Autoversicherung, falls nötig.» Anhang: Beispiel Assurance AG – Prämienrechnung 2026, Motorfahrzeug-Haftpflicht und Teilkasko, Kontrollschild SG 12345, Fälligkeit 01.01.2026.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: motorfahrzeug-versicherung. Steuerrelevant: nein. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen SG 2025: nein (sg-wl-2025__c0088). Kategorie gemäss Liste consis: keine Steuerbeleg-Kategorie (nicht steuerrelevant).

**Antwort des Agenten** (32.9 s · Tools: 5 Aufrufe steuerwiki__ablage, read, steuerwiki__zeige, steuerwiki__suche):

> **Ergebnis: Motorfahrzeugversicherung, nicht steuerrelevant, keine Steuerbeleg-Kategorie.**
> 
> - **Dokumenttyp:** Prämienrechnung Motorfahrzeug-Haftpflicht und Teilkasko (Assurance AG, Kontrollschild SG 12345). Der Wiki-Vorschlag «Motorfahrzeug-Versicherungspolice» passt.
> - **Steuerrelevant?** Nein. In SG ist die Motorfahrzeugversicherung nicht abziehbar. Ziff. 14 der WL SG 2025 (`sg-wl-2025__c0087`) zählt die abzugsfähigen Versicherungsprämien auf: private Kranken-, Unfall-, Lebens- und Rentenversicherungen sowie Sparzinsen. Motorfahrzeugversicherungen gehören nicht dazu. Das Wiki ordnet Fahrzeugkosten als Lebenshaltungskosten ein. Die Aussage «nicht abziehbar» beruht damit auf der Aufzählung, nicht auf einem ausdrücklichen Satz. Der Status ist agent-geprüft, die Abnahme durch die Fachperson steht aus.
> - **Steuerjahr:** Das Tool schlägt 2025 vor und markiert den Konflikt selbst. Das Dokument ist aber eine Prämienrechnung 2026 mit Fälligkeit 01.01.2026. Nach der Regel «Steuerjahr = Bescheinigungsjahr» ist das 2026. Für die Steuererklärung 2025 spielt es in beiden Fällen keine Rolle.
> - **Einreichen?** Entfällt, da nicht steuerrelevant. Die Einreichepflicht betrifft nur Belege mit Abzug.
> - **Kategorie:** Keine Steuerbeleg-Kategorie. Die Liste nennt «Versicherungsprämien (Prämienbescheinigung)» unter «Belege Sonstiges», aber nur für abzugsfähige Prämien. Die Ähnlichkeit zu diesem Beispiel genügt nicht. Die Rechnung gehört damit in keine Kategorie der Steuerablage.
> - **Die E-Mail von Hans** («Noch die Autoversicherung, falls nötig.») ist eine Kundenmitteilung. Sie passt zu «Unterlagen Kunde» (Eingereicht: nein), falls sie dokumentiert werden soll.
> 
> Offen: Die Kategorieliste ist noch nicht durch consis bestätigt. Ob die Rechnung überhaupt abgelegt werden soll, entscheidet die Kanzlei.

## d21

**Frage:** Neuer Eingang (Kanton ZH, Steuererklärung 2025): «Kantonales Steueramt Zürich, 8090 Zürich | Herr und Frau Muster Hans und Anna, Musterweg 5, 8000 Zürich | Einschätzungsentscheid Staats- und Gemeindesteuern 2025 / Veranlagungsverfügung direkte Bundessteuer 2025: steuerbares Einkommen Kanton CHF 98'400, Bund CHF 101'200. Abweichungen von der Deklaration siehe Beilage. Einsprache innert 30 Tagen.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: veranlagung (Veranlagungsverfügung / Einschätzungsentscheid / definitive Steuerrechnung (Bund, Kanton/Gemeinde, Kapitalleistung)). Kein Steuerbeleg. Kategorie gemäss Liste consis: Klasse «Veranlagung + def. Steuerrechnung» (weitere Klassen, nicht aus der Liste).

**Antwort des Agenten** (27.9 s · Tools: 2 Aufrufe steuerwiki__ablage, read):

> **Ergebnis: Verfahrensdokument (Veranlagung), kein Steuerbeleg. Nicht einreichen. Steuerjahr 2025.**
> 
> - **Dokumenttyp:** Veranlagungsverfügung bzw. Einschätzungsentscheid. Das Schreiben enthält zwei Entscheide: Staats- und Gemeindesteuern ZH 2025 und direkte Bundessteuer 2025. Die Einsprache-Hinweise gehören zur Rechtsmittelbelehrung. Das Wiki erkennt den Typ mit hoher Sicherheit.
> - **Steuerrelevant (als Beleg):** Nein. Es ist ein Dokument des Steuerverfahrens und hat keinen Wert, den man in die Steuererklärung übernimmt. Die Werte dienen aber dem Abgleich mit der eingereichten Deklaration.
> - **Steuerjahr:** 2025. Das ist die veranlagte Steuerperiode, nicht das Ausstellungsjahr.
> - **Einreichen:** Nein. Die Einsprache richtet sich an das Steueramt, nicht an die Belegablage.
> - **Kategorie:** Die Liste `KATEGORIEN.md` hat dafür keine eigene Zeile. Die passende Klasse ist **«Veranlagung + def. Steuerrechnung»** (Ablageschema consis, noch nicht bestätigt). Keine Steuerbeleg-Kategorie wie «Belege eingereicht» oder «Belege Sonstiges». Die Zuordnung zu dieser Klasse ist vorläufig, bis consis sie bestätigt.
> 
> **Zu prüfen:**
> 1. **Einsprache-Frist:** 30 Tage ab Zustellung. Bei Zustellung heute läuft sie bis 9. Dezember 2026. War das Schreiben früher zugestellt, endet die Frist früher. Das Zustelldatum auf dem Umschlag oder im Eingangsstempel bestimmt die Frist. Die Rechtsmittelbelehrung im Schreiben ist maßgeblich.
> 2. **Abweichungen:** Die Beilage mit den Abweichungen von der Deklaration liegt nicht im Text vor. Ohne sie lässt sich nicht sagen, ob Einsprache nötig ist. Ich habe die Beträge (Kanton CHF 98'400, Bund CHF 101'200) deshalb nicht gegen eine Deklaration geprüft.
> 3. **Kanton und Bund** sind getrennte Entscheide mit getrennten Beträgen. Bei einer Einsprache müssen beide Positionen einzeln geprüft werden.
> 
> Die Entscheidung über eine Einsprache liegt bei der Fachperson. Ich habe keine Mandantendaten gespeichert.

## d22

**Frage:** Neuer Eingang (Kanton SG, Steuererklärung 2025): «Stadt St. Gallen, Steueramt | Herr Muster Hans, Dorfstrasse 12, 9000 St. Gallen | Provisorische Rechnung Staats- und Gemeindesteuern 2026, berechnet auf Basis der letzten Veranlagung: Total CHF 7'850.00, fällig 30.09.2026. Die definitive Abrechnung folgt nach der Veranlagung 2026.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: provisorische-rechnung (Provisorische Steuerrechnung (Bund, Kanton/Gemeinde)). Kein Steuerbeleg. Kategorie gemäss Liste consis: Klasse «Prov. Steuerrechnung».

**Antwort des Agenten** (26.7 s · Tools: 2 Aufrufe steuerwiki__ablage, read):

> **Dokumenttyp:** Provisorische Steuerrechnung (Staats- und Gemeindesteuern, Kanton SG). Die Erkennung ist mittel sicher, weil das Dokument nur wenige Merkmale nennt. Die Rechnung enthält keinen Bundessteuer-Betrag.
> 
> **Steuerrelevant?** Nein, nicht als Beleg. Es ist ein Dokument des Steuerverfahrens, kein Nachweis für einen Abzug oder Wert in der Steuererklärung. Der Betrag von CHF 7'850.00 wird nicht in die Deklaration übertragen.
> 
> **Steuerjahr:** 2026, laut Titel «Provisorische Rechnung … 2026». Sie basiert auf der letzten Veranlagung und ist nicht die Veranlagung 2025 selbst.
> 
> **Einreichen?** Nein. Auch die Wegleitung SG 2026 verlangt dafür keinen Beleg.
> 
> **Kategorie:** Die Kategorienliste (`KATEGORIEN.md`) hat keine eigene Zeile für provisorische Rechnungen. Im consis-Ablageschema gibt es dafür die Klasse «Prov. Steuerrechnung». Ich empfehle, das Dokument dort abzulegen und «Eingereicht?» = nein zu setzen. Die Klasse ist im Schema noch nicht von consis bestätigt.
> 
> **Auffällig:** Die Fälligkeit war am 30.09.2026, heute ist der 09.11.2026. Falls die Rechnung noch nicht bezahlt ist, ist sie überfällig und sollte kurzfristig geprüft werden. Ob die Zahlung eingegangen ist, lässt sich aus dem Dokument nicht ablesen.

## d23

**Frage:** Neuer Eingang (Kanton TG, Steuererklärung 2025): «Kantonale Steuerverwaltung Thurgau, Frauenfeld | Frau Muster Anna, Seeweg 3, 8590 Romanshorn | Steuererklärung 2025 – Auflage: Zur Prüfung Ihrer Deklaration reichen Sie uns bis 15.12.2026 die Belege zu den Liegenschaftsunterhaltskosten sowie den Nachweis der Weiterbildungskosten ein. Ohne Antwort erfolgt eine Ermessensveranlagung.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: auflage-nachfrage (Auflage / Nachfrage / Buchprüfung des Steueramts). Kein Steuerbeleg. Kategorie gemäss Liste consis: Klasse «Auflage/Buchprüfung».

**Antwort des Agenten** (34.7 s · Tools: 4 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg):

> **Kurz:** Das Schreiben ist eine **Auflage des Steueramts** (Aufforderung, Belege nachzureichen). Es ist selbst kein Steuerbeleg. Die verlangten Belege sind steuerrelevant und müssen bis **15.12.2026** eingereicht werden.
> 
> **1. Dokumenttyp:** Auflage/Nachfrage der Steuerbehörde (Verfahrensdokument).
> 
> **2. Steuerrelevant?**
> - Das Schreiben selbst: **nein**, es hat keinen Wert in der Steuererklärung.
> - Die verlangten Belege:
>   - **Weiterbildungskosten:** steuerrelevant (Abzug Ziff. 16.1/16.2, Code 348/349).
>   - **Liegenschaftsunterhalt:** **bedingt**. Relevant nur, wenn statt der Pauschale die tatsächlichen Kosten gewählt werden (Form. 7/8, Ziff. 8.1).
> 
> **3. Steuerjahr:** **2025**, also die Steuerperiode der Auflage. Die Belege selbst folgen dem Bescheinigungsjahr. Das Zahlungsdatum ist für die Periodenzuordnung massgebend.
> 
> **4. Einreichen?**
> - **Auflage:** nicht als Beleg einzureichen. Sie verlangt die Belege, und die Antwort ist die Einreichung.
> - **Weiterbildung: ja.** Bei Abzug Ziff. 16 ist eine Aufstellung mit Belegen beizulegen (tg-wl-2025__c0102).
> - **Liegenschaftsunterhalt: ja, sofern effektive Kosten gewählt wurden.** Die Auflage ist das ausdrückliche Verlangen, also auch Einzelbeträge unter Fr. 1'000 einreichen (tg-wl-2025__c0234). Bei Pauschalabzug entfällt die Einreichung, dann sollte die Auflage mit dem Steueramt geklärt werden.
> 
> **5. Kategorie (KATEGORIEN.md):**
> - **Auflage selbst:** Die Kategorienliste hat keine Zeile für Verfahrensdokumente. Vorgesehen ist die Klasse **«Auflage/Buchprüfung»** aus dem consis-Prozessbeschrieb. Diese Klasse ist noch nicht bestätigt, daher bitte mit consis abstimmen.
> - **Weiterbildungsbelege: «Belege eingereicht»** (Eingereicht? = ja). Die Liste nennt Weiterbildung unter «Belege Sonstiges», aber nur für Fälle ohne Einreichpflicht. Hier ist die Einreichung vorgeschrieben.
> - **Liegenschaftsunterhaltsbelege: «Belege eingereicht»**, falls effektive Kosten gewählt wurden (Liste: «Liegenschaftsunterhalt (Rechnungen, Aufstellung)», je nach Wegleitung). Bei Pauschale: «Belege Sonstiges».
> 
> **Hinweise:**
> - Die Einordnung ist agent-geprüft, die Abnahme steht noch aus. Die Erkennung des Dokumenttyps hat mittlere Sicherheit.
> - Frist: 15.12.2026, rund fünf Wochen ab heute. Ohne Antwort droht eine Ermessensveranlagung.
> - Vor dem Einreichen sollte geklärt werden, ob bei Frau Muster effektive Liegenschaftskosten oder die Pauschale gewählt wurden.

## d24

**Frage:** Neuer Eingang (Kanton AR, Steuererklärung 2025): «Kantonale Steuerverwaltung Appenzell Ausserrhoden, Herisau | Herr Muster Hans, Hauptgasse 7, 9100 Herisau | Kontoauszug Steuerkonto per 31.10.2026 – Steuerperiode 2025, Staats- und Gemeindesteuern: Soll CHF 9'210.00, Zahlungen CHF 8'000.00, Vergütungszins CHF 12.40, offener Saldo CHF 1'197.60.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: kontoauszug-steueramt (Kontoauszug des Steueramts (Steuerkonto, Zahlungen, Saldo) – nicht Bank-Kontoauszug). Kein Steuerbeleg. Kategorie gemäss Liste consis: Klasse «Kontoauszug».

**Antwort des Agenten** (25.4 s · Tools: 2 Aufrufe steuerwiki__ablage, read):

> **Dokumenttyp:** Kontoauszug des Steueramts (Steuerkonto, Staats- und Gemeindesteuern AR). Es ist kein Bank-Kontoauszug.
> 
> **Steuerrelevant?** Nein. Es ist ein Dokument des Steuerverfahrens und kein Steuerbeleg. Die Werte (Soll, Zahlungen, Zinsen, Saldo) gehen nicht als Abzug oder Einkommen in die Steuererklärung ein.
> 
> **Steuerjahr:** 2025. Das Dokument ist am 31.10.2026 ausgestellt, bezieht sich aber auf die Steuerperiode 2025. Die Ablageregel nimmt das Bescheinigungsjahr, also 2025.
> 
> **Einreichen?** Nein.
> 
> **Kategorie:** Keine Steuerbeleg-Kategorie. Die Kategorienliste (`KATEGORIEN.md`) enthält für dieses Dokument keine Zeile. Die Klasse **«Kontoauszug»** (Kontoauszug des Steueramts, Steuerkonto, nicht Bank-Kontoauszug) steht im consis-Ablageschema außerhalb der Liste und ist noch nicht bestätigt. Ablage dort, Beschreibung z. B. «Kontoauszug Steueramt AR 2025», Eingereicht = nein.
> 
> **Hinweis:** Die Kategorienliste ist noch nicht bestätigt (Spalte «Bestätigt» leer). Der Saldo von CHF 1'197.60 ist für die Kontrolle relevant, z. B. ob die Zahlung der Steuerrechnung 2025 vollständig ist. Er gehört aber nicht in die Steuererklärung.

## d25

**Frage:** Neuer Eingang (Kanton ZH, Steuererklärung 2025): «Beispiel Bank AG, Musterstrasse 10, 8001 Zürich | Herr Muster Hans | Steuerauszug 2025 (eSteuerauszug mit Barcode): Wertschriften- und Guthabenverzeichnis per 31.12.2025, Steuerwert total CHF 186'300.00, Bruttoerträge mit Verrechnungssteuer CHF 1'240.00, VSt-Anspruch CHF 434.00. Bitte der Steuererklärung beilegen.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: steuerauszug-bank. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen ZH 2025: bedingt (zh-wl-2025__c0173). Kategorie gemäss Liste consis: Belege eingereicht, falls beizulegen, wenn im Wertschriften- und Guthabenverzeichnis auf das Steuerverzeichnis der Bank verwiesen wird (statt Einzelauflistung); eSteuerauszug kann online importiert werden (WL c0153); Wertschriftenverzeichnis selbst ist Pflichtbeilage – sonst Belege Sonstiges.

**Antwort des Agenten** (29.2 s · Tools: 4 Aufrufe steuerwiki__ablage, read, steuerwiki__zeige):

> **Ablage-Vorschlag: Steuerauszug der Bank (eSteuerauszug), ZH, Steuerjahr 2025**
> 
> - **Dokumenttyp:** Steuerauszug der Bank mit Wertschriften- und Guthabenverzeichnis per 31.12.2025. Die Erkennung ist eindeutig (Punkte 13 gegenüber 1).
> - **Steuerrelevant:** ja. Das Dokument hat Werte in der Steuererklärung: Ziff. 4.1, 4.2, 16.3, 16.5, 30.1 sowie Form. 340 Kolonnen A und B und Totale (Wiki-Fundstelle zh-wl-2025__c0153).
> - **Steuerjahr:** 2025 (Bescheinigungsjahr).
> - **Einreichen:** bedingt. Laut WL ZH 2025 (zh-wl-2025__c0173) sind die detaillierten Steuerverzeichnisse beizulegen, wenn das Wertschriftenverzeichnis darauf verweist, statt die Werte einzeln aufzulisten. Der eSteuerauszug ist genau dafür gedacht: Die Werte lassen sich damit importieren, eine Einzelauflistung entfällt. Ob im Verzeichnis tatsächlich auf den Steuerauszug verwiesen wird, sehe ich aus der Notiz nicht. Der Auftrag, ihn «beizulegen», spricht dafür.
> - **Kategorie:** **Belege eingereicht**. Die Liste ordnet Bank-/Depotauszüge und Steuerverzeichnisse so ein: einzureichen gemäss Wegleitung → «Belege eingereicht», sonst «Belege Sonstiges». Bei Verweis im Verzeichnis lautet die Zeile «Belege eingereicht» (Eingereicht? = ja). Ohne Verweis wäre es «Belege Sonstiges» (Eingereicht? = nein).
> 
> **Offene Punkte:**
> - Prüfen, ob das Wertschriftenverzeichnis auf den Steuerauszug verweist. Falls ja: einreichen, Kategorie «Belege eingereicht». Falls nein: beide Werte sind in der Erklärung einzeln zu erfassen, Kategorie «Belege Sonstiges».
> - Zur Plausibilität: VSt-Anspruch CHF 434.00 entspricht 35 % von Bruttoerträgen CHF 1'240.00. Das stimmt.
> - Die Kategorieliste ist laut Quelle noch nicht durch consis bestätigt. Die Abnahme durch den Fachbearbeiter steht aus.
> 
> Ich habe nichts in Dateien oder Memory gespeichert. Die Mandantendaten (Name, Adresse) stehen nur in dieser Antwort.

## d26

**Frage:** Neuer Eingang (Kanton SG, Steuererklärung 2025): «Banque Exemple SA, Genève | Monsieur Muster Hans, 9000 St-Gall | Relevé de dépôt au 31.12.2025 – positions: 120 actions nom. Beispiel AG, 50 parts fonds obligataire CHF; valeur de marché totale CHF 64'380.00. Ce relevé ne remplace pas le relevé fiscal.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: depotauszug. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen SG 2025: bedingt (sg-wl-2025__c0121). Kategorie gemäss Liste consis: Belege eingereicht, falls bei Bestandesänderungen (Erwerb, Veräusserung, Rückzahlung, Konversion) Bankbelege beilegen; selbst erstelltes Verzeichnis mit Formular 2 einreichen; nichtkotierte Titel: Kauf-/Verkaufsverträge beilegen – sonst Belege Sonstiges.

**Antwort des Agenten** (32.0 s · Tools: 4 Aufrufe steuerwiki__ablage, read, steuerwiki__zeige):

> **Dokumenttyp:** Depotauszug (Wertschriftenbestand per 31.12.2025) der Bank, also kein Steuerauszug. Der Vermerk «ne remplace pas le relevé fiscal» bestätigt das: Für die Steuererklärung fehlt noch der Steuerauszug der Bank. Die Erkennung ist mittel sicher (9 zu 5 Punkte gegen Steuerauszug).
> 
> **Steuerrelevant:** Ja. Die Werte gehen ins Wertschriften- und Guthabenverzeichnis (Stand 31. Dezember). Dort landen die 120 Aktien und die 50 Fondsanteile mit dem Marktwert von CHF 64'380.00. Positionen SG 2025: Ziff. 4.1, 4.2, 16.1, 30.1 sowie Form. 2 Spalte A/B.
> 
> **Steuerjahr:** 2025, weil das Dokument den Stand am 31.12.2025 ausweist.
> 
> **Einreichung (SG 2025): bedingt.** Ein reiner Stichtagsauszug muss nicht eingereicht werden. Anders ist es bei Bestandesänderungen während 2025 (Erwerb, Veräusserung, Rückzahlung, Konversion): Dann sind die Bankbelege dazu beizulegen (WL SG 2025, S. 35–36). Das Dokument selbst zeigt keine Bewegungen. Bitte die Kundin bzw. den Kunden oder die Bank-Unterlagen dazu prüfen.
> 
> **Kategorie: Belege Sonstiges**, mit Eingereicht? = nein. Das gilt, solange keine Bestandesänderungen 2025 vorliegen. Bei Änderungen würden die Bankbelege zu den Veränderungen in «Belege eingereicht» (Eingereicht? = ja) abgelegt. Die Begründung stützt sich auf die Zeile «Belege Sonstiges» in KATEGORIEN.md (Wertschriftenverzeichnis).
> 
> **Offene Punkte:**
> - KATEGORIEN.md ist von consis noch nicht bestätigt. Die Liste selbst vermerkt zudem offen, ob das Wertschriftenverzeichnis in SG einzureichen ist. Der Wiki-Befund (bedingt) stützt die Zuordnung zu «Belege Sonstiges», die Klärung durch consis bleibt aber offen.
> - Der Steuerauszug der Bank wird separat benötigt. Er ist in SG bei Papiereinreichung immer dem Formular 2 beizulegen (WL SG 2025, S. 36).
> - Die Angaben im Wiki sind agent-geprüft, die fachliche Abnahme steht noch aus.

## d27

**Frage:** Neuer Eingang (Kanton TG, Steuererklärung 2025): «Musterbank Genossenschaft, 8500 Frauenfeld | Herr und Frau Muster Hans und Anna | Zinsbestätigung 2025 Festhypothek Nr. 4711, Objekt Rebenweg 4, Weinfelden: Schuld per 31.12.2025 CHF 520'000.00, belastete Hypothekarzinsen 01.01.–31.12.2025 CHF 7'540.00. Zur Vorlage bei der Steuerbehörde.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: hypothekarbestaetigung. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen TG 2025: unklar (tg-wl-2025__c0026). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (34.4 s · Tools: 7 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg, steuerwiki__zeige, steuerwiki__suche, steuerwiki__position):

> **Dokumenttyp:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen). Erkennung hoch (10 zu 0 Punkten).
> 
> **Steuerrelevant:** ja. Das Dokument gehört in drei Positionen der TG-Steuererklärung 2025:
> - **Ziff. 34** (Schulden, Formular 4.1, Code 466): Schuld per 31.12.2025 von CHF 520'000.00 mit Gläubiger, Zinssatz und Adresse im Schuldenverzeichnis. Die Bankbestätigung liefert die Schuld und den Zinssatz.
> - **Ziff. 11** (Schuldzinsen, Code 290): belastete Hypothekarzinsen 2025 von CHF 7'540.00. Nur im Jahr 2025 fällige Zinsen, keine Ratenzinsen.
> - Gläubiger-Angabe mit genauer Adresse: Die Wegleitung nennt sie als unerlässlich (WL TG 2025, S. 36, tg-wl-2025__c0171).
> 
> **Steuerjahr:** 2025 (Bescheinigungsjahr). Quelle: Zinsbestätigung «Schuld per 31.12.2025».
> 
> **Einreichen:** unklar. Das Wiki kann für die Bankbestätigung keine eindeutige TG-Einreichepflicht belegen. Die Wegleitung verlangt, dass das Schuldenverzeichnis (Formular 4.1) mit der Steuererklärung eingereicht wird (tg-wl-2025__c0171). Ob die Bankbestätigung selbst einzureichen ist, geht daraus nicht hervor. Ich habe deshalb nicht geraten. Falls die Behörde die Bestätigung verlangt, wäre das bei Einreichung ein «ja». Das musst du mit der Wegleitung bzw. dem Steueramt klären. Vorläufig: «Eingereicht?» = nein, mit diesem Vorbehalt.
> 
> **Kategorie:** **Belege Sonstiges** (Eingereicht? = nein, vorläufig). Die Liste nennt «Hypothekarzinsbescheinigung» ausdrücklich. Sie ordnet sie unter «Belege eingereicht», wenn die Wegleitung des Kantons die Einreichung verlangt, sonst unter «Belege Sonstiges». Da die Einreichepflicht für TG unklar ist, ist «Belege Sonstiges» die vorläufige Zuordnung. Sobald klar ist, dass die Bestätigung einzureichen ist, wechselt sie zu «Belege eingereicht» (Eingereicht? = ja).
> 
> **Hinweise:**
> - Der Status der Fundstellen ist «agent-geprüft, Abnahme offen». Die fachliche Abnahme steht noch aus.
> - Die Liegenschaft Rebenweg 4 in Weinfelden kann zusätzlich relevant sein (Eigenmietwert, Liegenschaftsunterhalt). Das ist hier nicht geprüft.

## d28

**Frage:** Neuer Eingang (Kanton AR, Steuererklärung 2025): «Vorsorgestiftung Sparen 3 der Beispiel Bank AG | Frau Muster Anna, 9100 Herisau | Bescheinigung über Vorsorgebeiträge 2025 (gebundene Vorsorge Säule 3a, Form. 21 EDP): einbezahlte Beiträge vom 01.01.–31.12.2025 CHF 6'000.00.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: bescheinigung-saeule3a. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen AR 2025: ja (ar-wl-2025__c0083). Kategorie gemäss Liste consis: Belege eingereicht (Beispiel in der Liste: wird eingereicht).

**Antwort des Agenten** (27.1 s · Tools: 3 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg):

> **Dokumenttyp:** Bescheinigung über Vorsorgebeiträge, Formular 21 EDP für die gebundene Selbstvorsorge (Säule 3a), ausgestellt von einer Bankstiftung. ☑️ agent-geprüft: Fundstelle geprüft, Abnahme offen.
> 
> **Steuerrelevant:** Ja. Die Bescheinigung belegt den Abzug Säule 3a in Ziffer 13.1.
> 
> **Steuerjahr:** 2025 (Bescheinigungsjahr, Beiträge 01.01.–31.12.2025).
> 
> **Einreichen:** Ja, in jedem Fall. Die Wegleitung AR 2025 (Ziff. 13.1) verlangt die Bescheinigung bei diesem Abzug.
> 
> **Kategorie:** «Belege eingereicht», mit «Eingereicht?» = ja. KATEGORIEN.md nennt «Bescheinigung Säule 3a (eingereicht: ja)» ausdrücklich. Die Zuordnungsliste ist von consis noch nicht bestätigt.
> 
> **Berechnung für Ziff. 13.1 (AR 2025, Kanton = Bund):**
> - Mit 2. Säule: Abzug = min(6'000.00; 7'258) = **CHF 6'000.00**.
> - Ohne 2. Säule: Abzug = min(6'000.00; 20 % des Erwerbseinkommens, max. 36'288). Dafür braucht es das Erwerbseinkommen.
> - Ob eine 2. Säule besteht, steht im Lohnausweis oder Vorsorgeausweis. Das muss ich noch prüfen, bevor ich den Abzug festlege.
> 
> Der Abzug gilt nur für Beiträge, die im Steuerjahr tatsächlich bezahlt wurden, und nur bei AHV-pflichtiger Erwerbstätigkeit. Die Bescheinigung nennt den Gesamtbetrag. Die Begrenzung wendet der Bearbeiter an.
> 
> **Offen:** Ob Frau Muster eine 2. Säule hat und ob sie erwerbstätig ist.

## d29

**Frage:** Neuer Eingang (Kanton ZH, Steuererklärung 2025): «Banca Esempio SA, Lugano | Signor Muster Hans, 8400 Winterthur | Conteggio dividendo del 14.05.2025 – 200 az. Example Corp. (USA): dividendo lordo USD 180.00, ritenuta alla fonte USA 15% USD 27.00, accredito netto USD 153.00. Modulo DA-1 disponibile su richiesta.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: dividenden-ausland-quellensteuer. Steuerrelevant: bedingt (Bedingung: Nur bei Erträgen aus dem Ausland mit abgezogener ausländischer Quellensteuer; die Rückerstattung bzw. Anrechnung wird über Formular DA-1 (und ggf. …). Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen ZH 2025: bedingt (zh-wl-da1-2025__c0007). Kategorie gemäss Liste consis: Belege eingereicht, falls nur wenn Anrechnung ausländischer Quellensteuern bzw. Rückerstattung Steuerrückbehalt USA beantragt: Formular DA-1 inkl. sämtlicher Ertragsabrechnungen mit der Steuererklärung (USA-Positionen ohne Belege werden abgelehnt, WL DA-1 c0013) – sonst Belege Sonstiges.

**Antwort des Agenten** (34.9 s · Tools: 3 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg):

> **Dokumenttyp:** Dividenden-Ertragsabrechnung aus dem Ausland mit Quellensteuer (Gutschrift einer Depotbank für US-Aktien, 200 Aktien Example Corp., Bruttodividende USD 180.00, US-Quellensteuer 15 % = USD 27.00, Netto USD 153.00). Die Typerkennung ist mittel sicher. Das Dokument sollte kurz von dir selbst geprüft werden.
> 
> **Steuerrelevant:** Ja. Die Dividende ist steuerbarer Ertrag aus Wertschriften und gehört in Ziff. 4.1 (Code 150) der ZH-Steuererklärung 2025, über das Wertschriftenverzeichnis. Die USD-Beträge müssen zum Kurs in CHF umgerechnet werden. Den massgebenden Stichtag und Kurs habe ich nicht belegt. Das Dokument nennt nur das Datum 14.05.2025, keine separate Valuta.
> 
> **Steuerjahr:** 2025, weil die Ausschüttung am 14.05.2025 erfolgte.
> 
> **Einreichpflicht: bedingt.** Die Pflicht entsteht nur, wenn die Anrechnung der ausländischen Quellensteuer bzw. die Rückerstattung des US-Steuerrückbehalts beantragt wird. Dann muss das DA-1-Formular vollständig mit allen Ertragsabrechnungen eingereicht werden (Form. 340 DA-1, Codes 2370/2371; Wegleitung DA-1/DA-3 2025). Die Anrechnung erfolgt nur, wenn die nicht rückforderbare ausländische Quellensteuer über CHF 100 liegt. Die Bank schreibt, das DA-1 sei „auf Anfrage“ erhältlich. Wenn der Kunde die Anrechnung will, muss es bei Banca Esempio angefordert werden.
> 
> **Kategorie:** Die Liste nennt diese Dokumentart nicht ausdrücklich. Am nächsten liegt die Zeile „Bank-/Depotauszüge“, die je nach Wegleitung entweder unter „Belege eingereicht“ oder unter „Belege Sonstiges“ landet.
> - **Empfehlung: „Belege eingereicht“ (Eingereicht? = ja)**, wenn die Anrechnung der Quellensteuer beantragt wird. Die Ertragsabrechnung gehört dann zum eingereichten DA-1.
> - **Sonst: „Belege Sonstiges“ (Eingereicht? = nein)**, wenn keine Anrechnung beantragt wird. Der Wert steht trotzdem im Wertschriftenverzeichnis.
> 
> Die Zuordnung der Liste ist noch nicht bestätigt; das sollte mit consis geklärt werden.
> 
> Der Mandant ist laut Dokument Hans Muster, Winterthur. Ich habe seinen Namen nicht im Wiki oder im Gedächtnis gespeichert.

## d30

**Frage:** Neuer Eingang (Kanton SG, Steuererklärung 2025): «Beispiel Kredit AG, 9001 St. Gallen | Herr Muster Hans, Rosenbergstrasse 9, 9000 St. Gallen | Privatkredit Vertrag Nr. PK-2210 – Zinsbescheinigung 2025: Restschuld per 31.12.2025 CHF 18'400.00, bezahlte Schuldzinsen 2025 CHF 1'322.50.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: kredit-darlehen-schuldzinsen. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen SG 2025: auf verlangen (sg-wl-2025__c0073). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (29.0 s · Tools: 3 Aufrufe steuerwiki__ablage, read, steuerwiki__zeige):

> **Ablage-Ergebnis: Privatkredit-Zinsbescheinigung, SG 2025**
> 
> | Frage | Antwort |
> |---|---|
> | **Dokumenttyp** | Kredit-/Darlehensvertrag bzw. Zinsbescheinigung zu einem Privatkredit (Konsum-/Privatdarlehen, kein Hypothekarkredit) |
> | **Steuerrelevant?** | **Ja.** Schuldzinsen sind abzugsfähig, sofern die Kapitalforderung steuerlich anerkannt ist (Fundstelle sg-wl-2025__c0083). |
> | **Steuerjahr** | **2025** (Bescheinigungsjahr; Restschuld per 31.12.2025, Zinsen 2025) |
> | **Einreichen?** | **Nein, nur auf Verlangen.** Belege zu Abzügen sind aufzubewahren und erst auf Verlangen einzureichen (WL SG 2025, S. 22, sg-wl-2025__c0073). |
> | **Kategorie** | **Belege Sonstiges** («Schuldzinsen (ohne Hypothek) – Sofern nicht einzureichen», aus KATEGORIEN.md). Zeile «Eingereicht?» = **nein**. |
> 
> **Wo es in der Steuererklärung SG 2025 landet**
> - Schuldzinsen: Ziff. 11 (Formular 5, Teil A)
> - Schulden per 31.12.: ebenfalls Formular 5, Teil A. Dort Gläubiger («Beispiel Kredit AG»), Restschuld CHF 18'400.00 und Zinsen CHF 1'322.50 eintragen.
> - Ziff. 34.1 ist laut Wiki ebenfalls betroffen. Ich habe den Inhalt dieser Position nicht separat geprüft.
> 
> **Offene Punkte**
> - Die Kategorieliste ist laut Quelle noch nicht von consis bestätigt. Die Zuordnung «Schuldzinsen (ohne Hypothek) → Belege Sonstiges» steht aber wörtlich in der Liste.
> - Die Angaben im Dokument (Restschuld, Zinsen, Vertragsnummer PK-2210) habe ich nicht gegen einen Vertrag geprüft. Für die Deklaration sollte man sie gegen die Bescheinigung abgleichen.
> - Ob die Kapitalforderung steuerlich anerkannt ist (Bedingung für den Schuldzinsabzug), kann ich aus dem Dokument allein nicht beurteilen. Das bleibt bei der Fachperson.

## d31

**Frage:** Neuer Eingang (Kanton TG, Steuererklärung 2025): «Regionalbank Beispiel, 8280 Kreuzlingen | Frau Muster Anna | Zins- und Saldobestätigung Sparkonto per 31.12.2025: Saldo CHF 42'115.30, Bruttozins 2025 CHF 210.00, Verrechnungssteuer 35% CHF 73.50. Jahresabschluss Privatkonto beiliegend.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: kontoauszug-zinsausweis. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen TG 2025: unklar (tg-wl-2025__c0026). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (31.4 s · Tools: 4 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg, steuerwiki__zeige):

> **Dokumenttyp:** Kontoauszug / Zins- und Saldobescheinigung (Sparkonto). Die Erkennung ist mittel sicher (Punkte 8 gegenüber 1 für den Steuerauszug), weil nur der Text vorlag.
> 
> **Steuerrelevant:** ja. Saldo per 31.12., Bruttozins und Verrechnungssteuer gehören in die Steuererklärung. Die Fundstelle ist geprüft, die fachliche Abnahme steht noch aus.
> 
> **Steuerjahr:** 2025 (Bescheinigungsjahr, Stichtag 31.12.2025).
> 
> **Einreichen (TG 2025):** Unklar. Die Wegleitung nennt Zins- und Kapitalbescheinigungen unter «Benötigte Unterlagen» mit dem Zusatz «insbesondere», sie sagt aber nicht ausdrücklich, dass sie einzureichen sind. Deshalb setze ich «Eingereicht?» auf **nein**, bis das Steueramt oder die Wegleitung das klärt.
> 
> **Kategorie:** **Belege Sonstiges**, Zeile «Eingereicht?» = nein. Die Liste ordnet Bank- und Depotauszüge je nach Wegleitung entweder unter «Belege eingereicht» oder unter «Belege Sonstiges» ein. Hier gilt die zweite Option, solange die Einreichepflicht unklar ist. Falls das Steueramt den Ausweis doch verlangt, wechselt die Ablage zu «Belege eingereicht» (Eingereicht? = ja).
> 
> **Für die Erfassung in TG 2025:**
> - Bruttozins CHF 210.00 liegt über CHF 200. Die Verrechnungssteuer ist deshalb abzuziehen und der Betrag gehört in Spalte 8 (mit VSt), nicht in Spalte 9. Die VSt von CHF 73.50 entspricht genau 35 % von CHF 210.00.
> - Saldo CHF 42'115.30 → Form. 2 Spalten 7–9 (Steuerwert 31.12.) und Ziff. 30.1 (Wertschriften und Guthaben, Code 410).
> - Bruttozins → Ziff. 4 (Erträge, Form. 2 Ziff. 9).
> 
> **Offen:**
> - Der beiliegende «Jahresabschluss Privatkonto» liegt mir nicht vor. Falls es sich dabei um einen Steuerauszug der Bank handelt, ist er separat abzulegen. Dieser Typ kann je nach Einreichepflicht eine andere Kategorie bekommen.
> - Die Kategorie wurde aus der Liste mit dem Vorbehalt abgeleitet, dass die Zuordnung der Liste noch nicht von consis bestätigt ist.

## d32

**Frage:** Neuer Eingang (Kanton AR, Steuererklärung 2025): «Ausgleichskasse Appenzell Ausserrhoden, Herisau | Herr Muster Hans, 9053 Teufen | Rentenbescheinigung für die Steuererklärung 2025: ordentliche Altersrente AHV, ausbezahlt 01.01.–31.12.2025 total CHF 29'400.00 (monatlich CHF 2'450.00).» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: rentenbescheinigung-ahv-iv. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen AR 2025: auf verlangen (ar-wl-2025__c0009). Kategorie gemäss Liste consis: Belege eingereicht (Beispiel in der Liste: wird eingereicht).

**Antwort des Agenten** (28.2 s · Tools: 3 Aufrufe steuerwiki__ablage, read, steuerwiki__zeige):

> **Dokumenttyp:** Rentenbescheinigung AHV (ordentliche Altersrente, Jahresbescheinigung der Ausgleichskasse). Die Erkennung ist eindeutig, die Trennschärfe der Erkennung ist aber nur mittelhoch.
> 
> **Steuerrelevant:** Ja. Die AHV-Rente ist im Kanton AR vollständig zu deklarieren (WL AR 2025, Ziff. 3.1, S. 10, Fundstelle `ar-wl-2025__c0049`, geprüft). Bei der Deklaration gehören die Rentenbeträge zu den Einkünften aus Sozialversicherungen. Die Ergänzungsleistungen sind nicht steuerbar.
> 
> **Steuerjahr:** 2025 (Bescheinigungsjahr, Zeitraum 01.01.–31.12.2025).
> 
> **Einreichen:** Die Kategorieliste und das Wiki sind hier nicht deckungsgleich:
> - **Kategorieliste (KATEGORIEN.md):** Die Liste nennt «Renten-/Pensionsbescheinigung (AHV, PK)» ausdrücklich unter «Belege eingereicht» mit «eingereicht: ja». Diese Zuordnung stammt aus «Anhang F (02.11.2026), prüfen» und ist noch nicht bestätigt.
> - **Wiki (AR 2025):** Die WL nennt keine ausdrückliche Beilagepflicht für AHV-Renten. Das Wiki führt den Fall als «auf Verlangen» (Ziff. 3.1, c0049; Formular 1 siehe `ar-wl-2025__c0009`, nicht im Detail geprüft).
> 
> Ich folge hier der Listenregel, weil die Liste die Dokumentart ausdrücklich nennt: **Eingereicht? = ja**. Der Vorbehalt ist, dass die Einreichepflicht im Kanton AR laut Wiki nicht ausdrücklich geregelt ist. Falls die Fachperson strikt nach Wegleitung ablegt, wäre es «auf Verlangen». Das Dokument sollte in jedem Fall aufbewahrt werden.
> 
> **Kategorie:** **Belege eingereicht**, Beschreibung «Rentenbescheinigung AHV, Ausgleichskasse Appenzell Ausserrhoden».
> 
> **Offene Punkte:**
> - Bestätigung der Einreichungsregel für AR (Formular 1, `ar-wl-2025__c0009`).
> - Die Kategoriezuordnung ist laut Liste noch nicht bestätigt («Anhang F, prüfen»).
> - Abnahme durch die Fachperson ausstehend.
> 
> Der Name des Mandanten wird nicht im Wiki gespeichert.

## d33

**Frage:** Neuer Eingang (Kanton ZH, Steuererklärung 2025): «SVA Zürich, Ausgleichskasse | Frau Muster Anna, 8700 Küsnacht | Beitragsverfügung 2025 für Nichterwerbstätige: massgebendes Vermögen CHF 1'250'000 und Renteneinkommen; AHV/IV/EO-Jahresbeitrag CHF 3'180.00 zuzüglich Verwaltungskosten, zahlbar in vier Akontoraten.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: ahv-beitragsverfuegung-nichterwerbstaetige. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen ZH 2025: ja (zh-wl-2025__c0092). Kategorie gemäss Liste consis: Belege eingereicht.

**Antwort des Agenten** (31.7 s · Tools: 2 Aufrufe steuerwiki__ablage, read):

> **Ergebnis: AHV-Beitragsverfügung für Nichterwerbstätige, steuerrelevant, Steuerjahr 2025, Einreichung bedingt, Kategorie «Belege eingereicht» (vorläufig).**
> 
> **1. Dokumenttyp:** AHV-Beitragsverfügung bzw. Rechnung für Nichterwerbstätige der Ausgleichskasse (Erkennung hoch sicher). Die Verfügung legt den AHV/IV/EO-Jahresbeitrag fest. Sie ist keine Rentenbescheinigung.
> 
> **2. Steuerrelevant: ja.** Die Beiträge an AHV, IV und EO sind abzugsfähig (ZH Ziff. 16.1, Fundstelle zh-wl-2025__c0077).
> 
> **3. Steuerjahr: 2025.** Das ist das Bescheinigungsjahr.
> 
> **4. Einreichung: bedingt.** Laut Wiki (zh-wl-2025__c0092) muss der Beleg eingereicht werden, wenn der Abzug unter Ziff. 16.1 geltend gemacht wird, soweit die Einkünfte nicht schon darum gekürzt wurden. Zu prüfen:
> - Wird Ziff. 16.1 bei dieser Person angewendet? Das ist der Normalfall, wenn die Beiträge tatsächlich bezahlt wurden.
> - Welcher Betrag wurde 2025 tatsächlich bezahlt? Die Beiträge sind in vier Akontoraten zahlbar, und die Verwaltungskosten sind im Abzug unklar. Die Verfügung allein belegt nicht die Zahlung. Zahlungsnachweise sind deshalb sinnvoll.
> 
> **5. Kategorie: «Belege eingereicht» (Eingereicht? = ja), wenn der Abzug unter Ziff. 16.1 geltend gemacht wird.** Sonst «Belege Sonstiges» (Eingereicht? = nein).
> - Die Kategorienliste nennt die Beitragsverfügung nicht ausdrücklich. Die Regel der Liste lautet: einzureichen → «Belege eingereicht», sonst «Belege Sonstiges».
> - Die Liste ordnet Renten-/Pensionsbescheinigungen (AHV) unter «Belege eingereicht» zu. Das ist ein anderes Dokument und nur ein Anhaltspunkt.
> - Die Zuordnung ist laut KATEGORIEN.md noch nicht von consis bestätigt.
> 
> Der Beleg enthält personenbezogene Daten (Frau Muster Anna, Küsnacht). Ich habe nichts ins Wiki oder ins Gedächtnis geschrieben.

## d34

**Frage:** Neuer Eingang (Kanton SG, Steuererklärung 2025): «Sozialversicherungsanstalt des Kantons St. Gallen, EL-Stelle | Frau Muster Anna, 9500 Wil | Verfügung Ergänzungsleistungen zur AHV ab 01.01.2025: jährliche EL CHF 14'220.00, monatlich CHF 1'185.00; Vergütung von Krankheitskosten separat. Berechnungsblatt beiliegend.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: ergaenzungsleistungen. Steuerrelevant: bedingt (Bedingung: Die EL selbst sind steuerfrei und NICHT als Einkommen zu deklarieren. Relevant nur für (a) den Krankheits-/Behinderungskostenabzug (vergütete Kosten sind …). Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen SG 2025: auf verlangen (sg-wl-2025__c0013). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (27.3 s · Tools: 2 Aufrufe read, steuerwiki__ablage):

> **Dokumenttyp:** Verfügung Ergänzungsleistungen (EL) zur AHV, mit Berechnungsblatt. Die Erkennung ist sicher (13 Punkte gegen 0).
> 
> **Steuerrelevant:** bedingt.
> - Die EL selbst sind steuerfrei und werden nicht als Einkommen deklariert.
> - Relevant ist das Dokument für den Abzug der Krankheits- bzw. Behinderungskosten. Vergütete Kosten sind davon abzuziehen. Die separat vergüteten Krankheitskosten sind deshalb wichtig.
> - Relevant ist es auch für die Prämienverbilligung in der Nettoprämie.
> - Fundstelle: sg-wl-2025__c0072 («Anzurechnen sind»). Formularpositionen SG 2025: Ziff. 8.2–8.3. Die Vergütung von Krankheitskosten steht im Formular 6 (sg-wl-2025__c0013).
> 
> **Steuerjahr:** 2025. Die Verfügung gilt ab 01.01.2025.
> 
> **Einreichen:** nicht von sich aus. Laut Wiki ist die Verfügung nur auf Verlangen vorzulegen. Sie dient im Formular 8.2 zu Informationszwecken.
> 
> **Kategorie:** **Belege Sonstiges**, Zeile «Eingereicht?» = **nein**.
> - Die Liste nennt die EL-Verfügung nicht ausdrücklich.
> - Nach der Einreichepflicht passt «Belege Sonstiges». Sie umfasst Belege mit Wert in der Deklaration, die nicht eingereicht werden müssen, etwa Krankheitskosten.
> - Die Kategorie «Belege eingereicht» passt nicht, weil die Verfügung nicht von sich aus einzureichen ist.
> 
> **Unsicherheit:** Der Ablagevorschlag ist ☑️ agent-geprüft, die Abnahme ist offen. Die Liste ist noch nicht von consis bestätigt. Falls die Abnahme die Verfügung anders einordnet, etwa als reines Verfahrensdokument, bitte dort klären. Ich habe die Zuordnung nicht geraten, sondern aus der Einreichepflicht abgeleitet.
> 
> **Hinweis zum Beleg:** Der Name und die Adresse der Mandantin stehen nur in der Dokumentbeschreibung. Ich habe sie nicht in das Wiki oder in MEMORY.md übernommen.

## d35

**Frage:** Neuer Eingang (Kanton TG, Steuererklärung 2025): «Kanton Thurgau, Liegenschaftenschätzung | Herr und Frau Muster, Rebenweg 4, 8570 Weinfelden | Mitteilung Neuschätzung Einfamilienhaus Parz. 1234: Steuerwert CHF 640'000, Eigenmietwert CHF 21'300 ab Steuerperiode 2026. Einsprachefrist 30 Tage ab Zustellung.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: liegenschaft-schaetzung-eigenmietwert. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen TG 2025: unklar (tg-wl-2025__c0239). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (33.1 s · Tools: 4 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg, steuerwiki__zeige):

> **Dokumenttyp:** Schätzungsmitteilung der Liegenschaft, also Steuerwert- und Eigenmietwert-Verfügung (amtliche Schätzung, Kanton TG). Sie enthält einen Einsprachehinweis. Die Ablage-Erkennung ist mittel sicher (Top 1, 5 Punkte); die Einsprache-Kategorie (2.5 Punkte) passt nicht, weil das Dokument keine Einsprache ist.
> 
> **Steuerrelevant:** Ja. Der Eigenmietwert ist Einkommen, der Steuerwert ist Vermögen (Kanton). Fundstelle: Wiki-Beleg `liegenschaft-schaetzung-eigenmietwert`, ☑️ agent-geprüft, Abnahme offen.
> 
> **Steuerjahr:** Das Dokument gilt ab Steuerperiode 2026, das Bescheinigungsjahr ist also 2026, nicht 2025. Für die Steuererklärung 2025 ist die Neuschätzung nach TG-Praxis (StP 23 Nr. 1, Ziff. 3.3) nicht massgebend, weil massgebend der am Ende der Steuerperiode rechtskräftige Mietwert ist. Die Mitteilung kam am 09.11.2026, also nach Jahresende 2025. Die 2025er Erklärung braucht deshalb den bisherigen rechtskräftigen Wert. Bitte bestätigen, ob die Schätzung vor dem 31.12.2025 rechtskräftig eröffnet wurde, falls das anders ist.
> 
> **Einreichen:** Unklar. Die TG-Wegleitung regelt die Beilage nicht eindeutig (2025 und 2026). Nach der Regel der Kategorienliste heisst «unklar» → «Eingereicht?» = nein, mit diesem Vorbehalt.
> 
> **Kategorie:** **Belege Sonstiges**, «Eingereicht?» = nein. Die Liste nennt die Schätzungsmitteilung nicht ausdrücklich. Sie hat aber einen Wert in der Deklaration (Steuerwert, Eigenmietwert) und ist nicht klar einzureichen. Beschreibung nach Ablageregel: «Schätzung Liegenschaft Steuerwert/Eigenmietwert, Aussteller kantonale Steuerverwaltung TG», Steuerjahr 2026.
> 
> **Frist:** Die Einsprachefrist beträgt 30 Tage ab Zustellung. Bei Zustellung am 09.11.2026 wäre das etwa der 09.12.2026. Das Zustelldatum steht nicht im Dokument, bitte prüfen. Die Einsprache wäre eine eigene Ablage (Klasse «Einsprache/Rekurs»), falls sie eingelegt wird.

## d36

**Frage:** Neuer Eingang (Kanton ZH, Steuererklärung 2025): «Arbeitslosenkasse des Kantons Zürich | Herr Muster Hans, 8050 Zürich | Bescheinigung für die Steuererklärung 2025: ausbezahlte Arbeitslosenentschädigung 01.03.–30.09.2025 brutto CHF 31'560.40, abzüglich AHV/IV/EO-Beiträge und NBU-Prämie.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: taggeldbescheinigung. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen ZH 2025: ja (zh-wl-2025__c0055). Kategorie gemäss Liste consis: Belege eingereicht.

**Antwort des Agenten** (29.7 s · Tools: 4 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg, steuerwiki__zeige):

> **Kurzantwort:** Taggeldbescheinigung der Arbeitslosenkasse, steuerrelevant, Steuerjahr 2025, muss mit der Steuererklärung eingereicht werden, Kategorie «Belege eingereicht».
> 
> - **Dokumenttyp:** Taggeldbescheinigung (ALV-Taggelder, Arbeitslosenkasse). Sicherheit der Erkennung hoch.
> - **Steuerrelevant:** Ja. Die Arbeitslosenentschädigung ist Einkommen.
> - **Steuerjahr:** 2025. Das Bescheinigungsjahr ist 2025, der Zeitraum 01.03.–30.09.2025 liegt im Jahr 2025.
> - **Einreichen:** Ja. Die Bescheinigung ist laut WL ZH 2025 (Ziff. 3.3, Fundstelle zh-wl-2025__c0055) «mit der Steuererklärung einzureichen», wenn die Taggelder direkt von der Kasse ausbezahlt wurden und nicht im Lohnausweis stehen.
> - **Kategorie:** «Belege eingereicht», Zeile «Eingereicht?» = ja. Die Taggeldbescheinigung hat in KATEGORIEN.md keine eigene Zeile. Die Ablageregel der Liste ordnet einzureichende Belege dieser Kategorie zu.
> 
> **Erfassung in der Steuererklärung ZH 2025:**
> - Ziff. 3.3 (Code 140 für Person 1, 141 für Person 2): Erwerbsausfallentschädigungen der ALV, direkt ausbezahlt. Kanton und Bund sind gleich.
> - Den Bruttobetrag aus dem Dokument übernehmen. Vorher prüfen, ob derselbe Betrag im Lohnausweis steht, damit nichts doppelt deklariert wird.
> 
> **Offen:**
> - Die Abzüge (AHV/IV/EO-Beiträge und NBU-Prämie) habe ich nicht gegen die Wegleitung geprüft. Für die AHV-Beiträge gilt Ziff. 16.1, für die NBU-Prämie habe ich keine Fundstelle abgefragt. Ob und wie diese Abzüge in die Erklärung gehören, sollte die Fachperson noch klären.
> - Die Erkennung ist agent-geprüft, die Abnahme durch eine Fachperson steht noch aus.

## d37

**Frage:** Neuer Eingang (Kanton AR, Steuererklärung 2025): «Muster Krankenversicherung AG | Familie Muster Hans und Anna, 9100 Herisau | Prämienbestätigung 2025: Grundversicherung KVG CHF 8'964.00, Zusatzversicherungen VVG CHF 1'296.00, abzüglich Prämienverbilligung CHF 1'200.00; bezahlte Prämien total CHF 9'060.00.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: krankenkasse-praemien. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen AR 2025: auf verlangen (ar-form-06-2025__c0001). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (29.8 s · Tools: 3 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read):

> **Ergebnis: Prämienbescheinigung der Krankenversicherung, steuerrelevant, Steuerjahr 2025, nicht einzureichen (nur auf Verlangen), Kategorie «Belege Sonstiges».**
> 
> - **Dokumenttyp:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung). Erkennung: hoch. Status im Wiki: agent-geprüft, Abnahme offen.
> - **Steuerrelevant:** Ja. Die Prämien sind im Versicherungsabzug abziehbar (AR 2025, Ziff. 14, Form. 6 Teil A).
> - **Steuerjahr:** 2025. Das Bescheinigungsjahr ist 2025.
> - **Einreichen:** Nein, nur auf Verlangen. Form. 6 Teil A: «Die Belege sind auf Verlangen einzureichen.» Die Kategorie «Eingereicht?» ist daher **nein**.
> - **Kategorie:** **Belege Sonstiges**. Die Liste nennt dort ausdrücklich «Versicherungsprämien (Prämienbescheinigung) (Sofern nicht einzureichen)». Die Zeile «Belege eingereicht» passt nicht, weil die Pflicht nicht besteht.
> 
> **Zu prüfen beim Ausfüllen:**
> 1. **Zivilstand:** Der Höchstbetrag für den Versicherungsabzug hängt davon ab. Ehepaar: Kanton CHF 5'400 / Bund CHF 3'700. Alleinstehend: CHF 2'700 / CHF 1'800. Die Bescheinigung nennt Hans und Anna, Zivilstand steht nicht drin.
> 2. **Prämienverbilligung nicht doppelt kürzen:** Die Bescheinigung weist CHF 9'060 als bezahlte Prämien aus, also bereits nach Abzug der Prämienverbilligung von CHF 1'200. Laut Wiki ist in diesem Fall der reduzierte Betrag einzutragen, nicht der Bruttobetrag minus IPV.
> 3. **Gedeckelt:** CHF 9'060 liegt über den Höchstbeträgen. Der Abzug wird also auf den Höchstbetrag begrenzt.
> 
> Ich habe nichts gespeichert. Die Mandantendaten bleiben aus dem Wiki und aus der MEMORY.md heraus.

## d38

**Frage:** Neuer Eingang (Kanton SG, Steuererklärung 2025): «Exemple SA, Lausanne | Certificat de salaire 2025 (formulaire 11) – Monsieur Muster Hans, 9000 St-Gall, période 01.01.–31.12.2025: salaire brut CHF 96'500, cotisations AVS/AI/APG/AC CHF 6'128, prévoyance professionnelle CHF 5'820, salaire net CHF 84'552.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: lohnausweis. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen SG 2025: ja (sg-stg-2025__art-169). Kategorie gemäss Liste consis: Belege eingereicht (Beispiel in der Liste: wird eingereicht).

**Antwort des Agenten** (26.7 s · Tools: 2 Aufrufe steuerwiki__ablage, read):

> **Dokumenttyp:** Lohnausweis (Formular 11, in französischer Fassung «Certificat de salaire»). Erkennungssicherheit hoch.
> 
> **Steuerrelevant:** Ja. Der Nettolohn aus dem Lohnausweis ist für die Steuererklärung massgebend. Die Fundstelle ist bund-wl-lohnausweis-2026__c0038 (agent-geprüft, Abnahme offen).
> 
> **Steuerjahr:** 2025, laut Bescheinigungsjahr eindeutig.
> 
> **Einreichen:** Ja. Im Kanton SG ist der Lohnausweis für 2025 immer einzureichen, und zwar einer pro Arbeitgeber, auch bei Nebenerwerb (sg-stg-2025__art-169; Formular 1 Ziff. 1.1/1.2).
> 
> **Kategorie:** «Belege eingereicht», Zeile «Eingereicht?» = ja. Die Liste nennt den Lohnausweis ausdrücklich in dieser Kategorie. Die Kategorienliste ist laut Datei noch nicht von consis bestätigt.
> 
> **Positionen SG 2025:** Ziff. 1.1, 1.2, 1.3, Form. 4 Ziff. 2.2, 2.3, 4.2 und 5, sowie Feld F des Lohnausweises.
> 
> **Plausibilität:** 96'500 − 6'128 − 5'820 = 84'552. Die Werte im Dokument sind rechnerisch konsistent.
> 
> Ich habe nichts abgelegt oder gespeichert, weil das Ablegen von der Ablage-Zuständigkeit abhängt.

## d39

**Frage:** Neuer Eingang (Kanton TG, Steuererklärung 2025): «Pensionskasse Beispiel AG | Herr Muster Hans, 8590 Romanshorn | Abrechnung Kapitalauszahlung infolge Pensionierung per 31.08.2025: ausbezahltes Altersguthaben CHF 412'000.00, Valuta 02.09.2025. Die Meldung an die Eidg. Steuerverwaltung erfolgt durch uns.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: kapitalleistung-vorsorge. Steuerrelevant: ja. Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen TG 2025: unklar (tg-form-01-2025__c0018). Kategorie gemäss Liste consis: Belege Sonstiges.

**Antwort des Agenten** (38.4 s · Tools: 5 Aufrufe steuerwiki__ablage, read, steuerwiki__beleg, steuerwiki__zeige):

> **Dokumenttyp:** Bescheinigung/Abrechnung einer Kapitalleistung aus Vorsorge (Pensionskasse, 2. Säule), Wiki-Kürzel `kapitalleistung-vorsorge`. Die Erkennung ist mittel sicher, aber eindeutig genug: Es ist eine Auszahlung, keine Einkaufsbescheinigung.
> 
> **Steuerrelevant: ja.** Kapitalleistungen aus Vorsorge sind immer zu 100 % steuerbar und werden gesondert besteuert (WL TG 2025, S. 28, `tg-wl-2025__c0131`).
> - **Kanton TG:** einfache Steuer auf der Kapitalleistung von CHF 412'000 zu 2,4 % (alleinstehend) bzw. 2 % (gemeinsam besteuert), danach × Gesamtsteuerfuss. Ob Herr Muster alleinstehend ist, geht aus dem Dokument nicht hervor. Die Berechnung ist daher noch offen.
> - **Bund:** 1/5 des ordentlichen Tarifs (Art. 36 DBG), keine Sozialabzüge. Den Bundesbetrag habe ich nicht berechnet.
> 
> **Steuerjahr: 2025.** Massgebend ist der Zufluss; die Valuta ist der 02.09.2025.
> 
> **Einreichen: nicht eindeutig belegt.** Der Wiki-Status ist «unklar». Formular 1 TG 2025, S. 4, verlangt eine Aufstellung nur bei mehreren Kapitalleistungen. Eine Beilage der Bescheinigung wird dort nicht ausdrücklich verlangt (`tg-form-01-2025__c0018`). Hier liegt eine einzige Leistung vor. Die Deklaration auf S. 4 ist trotzdem Pflicht, unabhängig davon, ob die PK meldet.
> 
> **Kategorie: Belege Sonstiges, «Eingereicht?» = nein.**
> - Die KATEGORIEN.md nennt die Kapitalleistung nicht als eigene Zeile. Es gilt daher die Regel für Belege mit Wert in der Deklaration, die nicht eingereicht werden müssen.
> - Ablagebeschreibung nach consis-Regel: «Kapitalleistung Pensionskasse Beispiel AG», Steuerjahr 2025.
> - Vorbehalt: Verlangt das Steueramt die Bescheinigung doch, ist die Kategorie auf «Belege eingereicht» zu ändern. Diesen Punkt kann nur die Ausschreibung des Steueramts klären, das Wiki liefert hier keine Gewissheit.

## d40

**Frage:** Neuer Eingang (Kanton AR, Steuererklärung 2025): «Lotteriegesellschaft Beispiel AG | Frau Muster Anna, 9043 Trogen | Gewinnbestätigung Lotto, Ziehung vom 18.10.2025: Gewinn Rang 3, Betrag CHF 48'000.00, ausbezahlt am 05.11.2025 auf Ihr Konto. Bitte für Ihre Unterlagen aufbewahren.» – Welcher Dokumenttyp ist das, ist es steuerrelevant, welches Steuerjahr, muss es eingereicht werden, und in welche Kategorie gehört es?

**Soll (Referenz):** Dokumenttyp: lotteriegewinn. Steuerrelevant: bedingt (Bedingung: Nur steuerbar, wenn der EINZELGEWINN die Freigrenze/den Freibetrag übersteigt (Lotterien/Verkaufsförderung: Freigrenze, dann voller Gewinn; …). Steuerjahr 2025 (bzw. Jahr des Dokuments). Einreichen AR 2025: bedingt (ar-form-02-2025__c0004). Kategorie gemäss Liste consis: Belege eingereicht, falls bei deklarierten Lotterie-/Geldspielgewinnen: Lotto-/Totobescheinigung im Beilagen-Raster von Formular 2 vorgesehen; ausdrückliche Pflichtformulierung fehlt (grep WL/Formulare ohne weitere Regel) – Formular-1-Zeile 4 verweist nur auf «Formular 2» – sonst Belege Sonstiges.

**Antwort des Agenten** (31.1 s · Tools: 3 Aufrufe steuerwiki__ablage, steuerwiki__beleg, read):

> **Ergebnis: nicht steuerbar, daher kein Einreichen und keine Steuerbeleg-Kategorie.**
> 
> **1. Dokumenttyp:** Lotto-Gewinnbestätigung (Lotteriegesellschaft, Rang 3, CHF 48'000.00, Ziehung 18.10.2025, Auszahlung 05.11.2025).
> 
> **2. Steuerrelevant?** Nein, nicht steuerbar. Die Gewinnbestätigung ist ein Beleg für einen Lotteriegewinn, der nur steuerbar ist, wenn der **Einzelgewinn** die Freigrenze bzw. den Freibetrag übersteigt. Der Lotto-Gewinn ist ein Grossspiel, und dafür gilt der Freibetrag:
> - AR (Kanton): CHF 1'000'000 (`steuerfrei.grossspielgewinn`)
> - Bund: CHF 1'070'400 (Art. 24 lit. ibis DBG)
> 
> CHF 48'000 liegt weit darunter. Der Gewinn bleibt steuerfrei, und ein Eintrag in der Steuererklärung (Ziff. 4.1) entfällt.
> Quelle: `ar-wl-2025__c0138`, Karte `beleg-lotteriegewinn`. Status: ☑️ agent-geprüft (Abnahme offen).
> 
> **3. Steuerjahr:** 2025. Ziehung und Auszahlung liegen beide im Jahr 2025, und die Bescheinigung gehört zum Steuerjahr 2025.
> 
> **4. Einreichen?** Nein. Das Wiki sagt «bedingt»: Die Lotto-Bescheinigung wird nur eingereicht, wenn der Lotteriegewinn deklariert ist. Da der Gewinn steuerfrei ist, entfällt das.
> 
> **5. Kategorie:** Keine Steuerbeleg-Kategorie. Die Liste nennt den Lotteriegewinn nicht ausdrücklich. Nach der Einreichepflicht gilt «Eingereicht? = nein». «Belege Sonstiges» wäre nur richtig, wenn der Beleg in der Deklaration einen Wert hat, und das ist hier nicht der Fall. Den Grund für die fehlende Kategorie habe ich oben genannt.
> 
> **Unsicherheit:** Die Einordnung als Grossspiel beruht auf dem Produktnamen «Lotto». Wenn es sich um eine Verkaufsförderungs-Lotterie handelt, gilt die Freigrenze von CHF 1'000 und der volle Gewinn wäre steuerbar (Ziff. 4.1, einzureichen, Kategorie «Belege eingereicht»). Bitte die Spielart kurz bestätigen. Der Name im Dokument wird nicht im Wiki gespeichert.

