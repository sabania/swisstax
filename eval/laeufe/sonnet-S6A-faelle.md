# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 20:20
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## f-zh

**Frage:** Steuerjahr 2025, Kanton ZH. Mandant/Haushalt: Ehepaar, wohnhaft in Winterthur ZH (Mieter, keine Liegenschaft), beide unselbständig erwerbstätig und Pensionskasse angeschlossen. Person 1 (Marco, 41, Projektleiter, 100 %, Arbeitsort Zug), Person 2 (Sandra, 39, kaufmännische Angestellte, 80 %, Arbeitsort Winterthur). Zwei Kinder im Haushalt: Lena (geb. 2021, 4 Jahre, Kita) und Noah (geb. 2016, 9 Jahre, Primarschule und Hort). Keine Kapitalbezüge aus Vorsorge in den letzten drei Jahren.

Belege:
- Lohnausweis 2025 Person 1: Ziff. 8 Bruttolohn 118'400; Ziff. 9 AHV/IV/EO/ALV/NBUV 8'110; Ziff. 10.1 BVG ordentlich 7'290; Ziff. 10.2 BVG Einkauf 0; Ziff. 11 Nettolohn 103'000. Feld F nicht angekreuzt, Feld G nicht angekreuzt. 100 %, 220 Arbeitstage; Mittagessen auswärts im Restaurant (keine Kantine, keine Lunch-Checks).
- Lohnausweis 2025 Person 2: Ziff. 8 Bruttolohn 76'800 (inkl. Kinderzulagen 4'800); Ziff. 9 AHV/IV/EO/ALV/NBUV 5'260; Ziff. 10.1 BVG ordentlich 4'340; Ziff. 10.2 0; Ziff. 11 Nettolohn 67'200. Feld F nicht angekreuzt, Feld G ANGEKREUZT (Personalrestaurant). 80 %, 176 Arbeitstage; Arbeitsweg mit eigenem Velo.
- Jahresabonnement öffentlicher Verkehr Winterthur–Zug (2. Klasse) Person 1, bezahlt 4'180.
- Krankenkassen-Prämienbescheinigung 2025 (ganze Familie, Grund- und Zusatzversicherung): Prämien 15'840; keine individuelle Prämienverbilligung.
- Säule-3a-Bescheinigungen (Form. 21 EDP): Person 1 7'258; Person 2 7'258.
- Pensionskasse Person 1: Bescheinigung freiwilliger Einkauf, direkt überwiesen am 14.11.2025: 10'000.
- Kita-Jahresrechnung Lena (4 Tage/Woche, reine Betreuung, Verpflegung von den Eltern mitgegeben): 27'300. Hort-/Tagesstrukturrechnung Noah: 6'900.
- Bank-Steuerauszug ZKB per 31.12.2025: Sparkonto 42'500 (Bruttozins 180, ohne VSt-Abzug); Privatkonto 8'300 (Zins 0); Depot Schweizer Aktien Steuerwert 31'200, Bruttodividenden 960 (VSt 336 abgezogen).
- Spendenquittungen: Schweizerisches Rotes Kreuz 400; UNICEF Schweiz und Liechtenstein 250 (beide steuerbefreit, Sitz CH). Zahnarztrechnung 1'850 (selbst bezahlt) und Krankenkassen-Leistungsabrechnung mit Kostenbeteiligung (Franchise/Selbstbehalt) Familie 1'240.
- Weitere Belege im Couvert: Swisscom-Handyrechnungen 2025 (privat) total 1'080; Hausrat- und Privathaftpflichtversicherung 465.

Auftrag: Erstelle die Ausfüllhilfe (alle relevanten Positionen mit Ziffer/Code, Beträge Staat und Bund, Rechenweg, Fundstellen) und nenne, was nicht zu deklarieren ist.

**Soll (Referenz):** nicht_deklarieren:
- 'Handyrechnungen 1''080: private Lebenshaltung (zh-stg-2025__par-33, bund-dbg-2025__art-34).'
- 'Hausrat-/Privathaftpflichtversicherung 465: keine Lebens-, Kranken- oder Unfallversicherung, gehört nicht in Form. 365 (zh-stg-2025__par-31-t2, zh-form-365-2025__c0001).'
- 'Zahnarzt 1''850 und Kostenbeteiligung 1''240: unter Selbstbehalt 5 % – Ziff. 22.1 bleibt 0 (zh-wl-2025__c0117).'
- Kinderzulagen 4'800 nicht separat unter Ziff. 3.4 – bereits im Lohnausweis Person 2 enthalten (zh-wl-2025__c0055).
- Fahrkosten Person 1 über 3'300 (Bund) bzw. Verpflegung über 3'200 sind nicht abziehbar (Maxima).
positionen:
- bezeichnung: Haupterwerb Person 1 – Nettolohn
  bund: 103000
  fundstellen:
  - zh-form-300-2025__c0004
  - zh-wl-2025__c0032
  kanton: 103000
  rechnung: 'Nettolohn gem. Lohnausweis Ziff. 11: 118''400 − 8''110 − 7''290 = 103''000.'
  ziffer: 1.1 Person 1 (Code 100)
- bezeichnung: Haupterwerb Person 2 – Nettolohn
  bund: 67200
  fundstellen:
  - zh-form-300-2025__c0004
  - zh-wl-2025__c0032
  - zh-wl-2025__c0055
  kanton: 67200
  rechnung: 76'800 − 5'260 − 4'340 = 67'200. Kinderzulagen sind im Lohnausweis enthalten, daher nicht zusätzlich unter Ziff. 3.4.
  ziffer: 1.1 Person 2 (Code 101)
- bezeichnung: Ertrag aus Wertschriften und Guthaben
  bund: 1140
  fundstellen:
  - zh-form-340-2025__c0003
  - zh-form-340-2025__c0005
  - zh-wl-2025__c0162
  - zh-wl-2025__c0168
  - bund-vstg__art-5-t1
  kanton: 1140
  rechnung: 'Kolonne A (mit VSt): Dividenden 960; Kolonne B (ohne VSt): Sparzins 180 (Bruttozins bis 200, kein VSt-Abzug); Total 960 + 180 = 1''140.'
  ziffer: 4.1 (Code 150) – aus Wertschriftenverzeichnis Form. 340
- bezeichnung: Verrechnungssteueranspruch (Rückerstattung, kein Einkommen/Abzug)
  bund: null
  fundstellen:
  - zh-form-340-2025__c0005
  - bund-vstg__art-13
  kanton: 336
  rechnung: 35 % von Bruttoertrag Kolonne A 960 = 336 (eidg. VSt, einmaliger Anspruch).
  ziffer: Form. 340 Code 540
- bezeichnung: Total der Einkünfte
  bund: 171340
  fundstellen:
  - zh-form-300-2025__c0006
  kanton: 171340
  rechnung: 103'000 + 67'200 + 1'140 = 171'340.
  ziffer: 7 (Code 199)
- bezeichnung: Fahrkosten öV Person 1
  bund: 3300
  fundstellen:
  - zh-form-360-2025__c0001
  - zh-form-360-2025__c0002
  - zh-wl-2025__c0065
  - zh-pauschalierung-berufsauslagen-2025__c0003
  - zh-stg-2025__par-26
  - bund-dbg-2025__art-26
  - bund-rs-2-210__c0002
  kanton: 4180
  rechnung: 'Abo 4''180 in beiden Spalten (Code 201); Zwischentotal 205: Staat 4''180 (unter Max. 5''200), Bund begrenzt auf Max. 3''300.'
  ziffer: Form. 360 Person 1, Ziff. 1.1 (Code 201) / Zwischentotal (Code 205)
- bezeichnung: Mehrkosten Verpflegung voll (keine Verbilligung)
  bund: 3200
  fundstellen:
  - zh-form-360-2025__c0003
  - zh-wl-2025__c0066
  - zh-pauschalierung-berufsauslagen-2025__c0004
  - bund-bkv-2025__anhang-1
  kanton: 3200
  rechnung: 220 Tage × 15 = 3'300 → Jahresmaximum 3'200.
  ziffer: Form. 360 Person 1, Ziff. 2.1 (Code 208)
- bezeichnung: Übrige Berufskosten pauschal
  bund: 3090
  fundstellen:
  - zh-form-360-2025__c0004
  - zh-wl-2025__c0067
  - zh-pauschalierung-berufsauslagen-2025__c0005
  - bund-bkv-2025__anhang-1
  kanton: 3090
  rechnung: 3 % × Nettolohn 103'000 = 3'090 (zwischen Min. 2'000 und Max. 4'000).
  ziffer: Form. 360 Person 1, Ziff. 3 (Code 212)
- bezeichnung: Berufsauslagen Person 1 total
  bund: 9590
  fundstellen:
  - zh-form-360-2025__c0005
  - zh-form-300-2025__c0007
  kanton: 10470
  rechnung: Staat 4'180 + 3'200 + 3'090 = 10'470; Bund 3'300 + 3'200 + 3'090 = 9'590.
  ziffer: 11.1 (Code 220)
- bezeichnung: Fahrkosten Velo pauschal
  bund: 700
  fundstellen:
  - zh-form-360-2025__c0006
  - zh-wl-2025__c0063
  - zh-pauschalierung-berufsauslagen-2025__c0001
  - bund-bkv-2025__anhang-1
  kanton: 700
  rechnung: Pauschal 700 pro Jahr (Staat und Bund).
  ziffer: Form. 360 Person 2, Ziff. 1.2 (Code 222)
- bezeichnung: Mehrkosten Verpflegung verbilligt (Feld G)
  bund: 1320
  fundstellen:
  - zh-form-360-2025__c0008
  - zh-wl-2025__c0066
  - zh-pauschalierung-berufsauslagen-2025__c0004
  - bund-bkv-2025__art-6-t1
  - bund-bkv-2025__anhang-1
  kanton: 1320
  rechnung: 'FALLE Feld G angekreuzt → nur halber Ansatz: 176 Tage × 7.50 = 1''320 (unter Max. 1''600); nicht 15.–/Tag.'
  ziffer: Form. 360 Person 2, Ziff. 2.1 (Code 226)
- bezeichnung: Übrige Berufskosten pauschal
  bund: 2016
  fundstellen:
  - zh-form-360-2025__c0009
  - zh-wl-2025__c0067
  - zh-pauschalierung-berufsauslagen-2025__c0005
  - bund-bkv-2025__anhang-1
  kanton: 2016
  rechnung: 3 % × 67'200 = 2'016 (über Min. 2'000).
  ziffer: Form. 360 Person 2, Ziff. 3 (Code 232)
- bezeichnung: Berufsauslagen Person 2 total
  bund: 4036
  fundstellen:
  - zh-form-360-2025__c0010
  - zh-form-300-2025__c0007
  kanton: 4036
  rechnung: 700 + 1'320 + 2'016 = 4'036.
  ziffer: 11.2 (Code 240)
- bezeichnung: Säule 3a Person 1
  bund: 7258
  fundstellen:
  - zh-form-300-2025__c0008
  - zh-wl-2025__c0081
  - bund-bvv3__art-7
  - bund-bsv-masszahlen-2025-2026__c0003
  kanton: 7258
  rechnung: Mit 2. Säule max. 7'258; bezahlt 7'258.
  ziffer: 14.1 (Code 260; eff. bezahlt Code 262)
- bezeichnung: Säule 3a Person 2
  bund: 7258
  fundstellen:
  - zh-form-300-2025__c0008
  - zh-wl-2025__c0081
  - bund-bvv3__art-7
  - bund-bsv-masszahlen-2025-2026__c0003
  kanton: 7258
  rechnung: Mit 2. Säule max. 7'258; bezahlt 7'258.
  ziffer: 14.2 (Code 261; eff. bezahlt Code 263)
- bezeichnung: Versicherungsprämien und Zinsen von Sparkapitalien
  bund: 5100
  fundstellen:
  - zh-form-365-2025__c0001
  - zh-form-365-2025__c0002
  - zh-form-365-2025__c0003
  - zh-wl-2025__c0086
  - zh-wl-2025__c0091
  - zh-stg-2025__par-31-t2
  - bund-dbg-2025__art-33-t2
  - bund-dbg-2025__art-33-t5
  - bund-rs-2-210__c0006
  kanton: 8400
  rechnung: 'Teil A (606): Prämien 15''840 + Sparzinsen 180 = 16''020. Teil B (616) Staat: 5''800 + 2 × 1''300 = 8''400; Bund: 3''700 + 2 × 700 = 5''100 (Verheiratete
    mit 2./3a-Beiträgen). Abzug = niedrigerer Betrag.'
  ziffer: 15 (Code 270) – via Form. 365 (Codes 606/616)
- bezeichnung: Einkauf 2. Säule Person 1 (direkt bezahlt)
  bund: 10000
  fundstellen:
  - zh-form-300-2025__c0008
  - zh-wl-2025__c0092
  - zh-stg-2025__par-31-t1
  - bund-dbg-2025__art-33-t2
  kanton: 10000
  rechnung: Einkauf 10'000 gem. PK-Bescheinigung; nicht über Lohnausweis abgezogen; kein Kapitalbezug innert 3 Jahren.
  ziffer: 16.1 (Code 280)
- bezeichnung: Kosten für die Verwaltung des beweglichen Privatvermögens (Pauschale)
  bund: 0
  fundstellen:
  - zh-form-300-2025__c0008
  - zh-wl-2025__c0095
  - zh-zstb-30-1__c0006
  - bund-wl-2a-2025__c0056
  kanton: 94
  rechnung: 'Depot ZKB (drittverwahrt) 31''200 × 3 ‰ = 93.60 → 94 (93 ebenfalls korrekt); Spar-/Privatkonto zählen nicht (ohne Bankguthaben, ZStB 30.1). Bund: belegt
    sind nur effektive Depot-/Safegebühren (bund-wl-2a-2025__c0056) → 0; 94 nur mit ausdrücklichem Vorbehalt ebenfalls zulässig (dann Bund-Totale je −94).'
  ziffer: 16.3 (Code 283)
- bezeichnung: Abzug für fremdbetreute Kinder
  bund: 32700
  fundstellen:
  - zh-form-300-2025__c0008
  - zh-wl-2025__c0106
  - zh-wl-2025__c0107
  - zh-wl-2025__c0108
  - zh-stg-2025__par-31-t4
  - bund-dbg-2025__art-33-t7
  - bund-rs-2-210__c0007
  kanton: 31900
  rechnung: Lena 27'300 → Staat max. 25'000 / Bund max. 25'800; Noah 6'900 (unter Max.). Staat 25'000 + 6'900 = 31'900; Bund 25'800 + 6'900 = 32'700.
  ziffer: 16.6 (Code 376)
- bezeichnung: Sonderabzug bei Erwerbstätigkeit beider Ehegatten
  bund: 14100
  fundstellen:
  - zh-wl-2025__c0111
  - zh-wl-2025__c0112
  - zh-wl-2025__c0113
  - zh-stg-2025__par-31-t5
  - bund-dbg-2025__art-33-t6
  - bund-rs-2-210__c0007
  kanton: 6100
  rechnung: 'Niedrigeres verbleibendes Erwerbseinkommen = Person 2: 67''200 − Berufsauslagen 4''036 − 3a 7''258 = 55''906 (Person 1: Staat 75''272 / Bund 76''152).
    Staat: fix max. 6''100. Bund: 50 % × 55''906 = 27''953 → Max. 14''100.'
  ziffer: 17 (Code 290)
- bezeichnung: Total der Abzüge
  bund: 90042
  fundstellen:
  - zh-form-300-2025__c0008
  kanton: 85516
  rechnung: Staat 10'470 + 4'036 + 7'258 + 7'258 + 8'400 + 10'000 + 94 + 31'900 + 6'100 = 85'516; Bund 9'590 + 4'036 + 7'258 + 7'258 + 5'100 + 10'000 + 32'700 + 14'100
    = 90'042.
  ziffer: 18 (Code 299)
- bezeichnung: Nettoeinkommen
  bund: 81298
  fundstellen:
  - zh-form-300-2025__c0009
  kanton: 85824
  rechnung: 171'340 − 85'516 = 85'824; 171'340 − 90'042 = 81'298.
  ziffer: 21 (Code 310)
- bezeichnung: Krankheits- und Unfallkosten
  bund: 0
  fundstellen:
  - zh-wl-2025__c0117
  - zh-wl-2025__c0122
  - zh-stg-2025__par-32
  - bund-dbg-2025__art-33-t3
  kanton: 0
  rechnung: 'FALLE: Kosten 1''850 + 1''240 = 3''090 < Selbstbehalt 5 % von Ziff. 21 (Staat 4''291.20, Bund 4''064.90) → kein Abzug.'
  ziffer: 22.1 (Code 320)
- bezeichnung: Gemeinnützige Zuwendungen
  bund: 650
  fundstellen:
  - zh-wl-2025__c0121
  - zh-wl-2025__c0122
  - zh-stg-2025__par-32
  - bund-dbg-2025__art-33a
  kanton: 650
  rechnung: 400 + 250 = 650; ≥ 100 und unter 20 % von Ziff. 21 (Staat 17'165 / Bund 16'259).
  ziffer: 22.2 (Code 324)
- bezeichnung: Reineinkommen
  bund: 80648
  fundstellen:
  - zh-form-300-2025__c0009
  kanton: 85174
  rechnung: 85'824 − 0 − 650 = 85'174; 81'298 − 0 − 650 = 80'648.
  ziffer: 23 (Code 350)
- bezeichnung: Abzug für Kinder im Haushalt
  bund: 13600
  fundstellen:
  - zh-form-300-2025__c0010
  - zh-wl-2025__c0126
  - zh-stg-2025__par-34
  - bund-dbg-2025__art-35
  - bund-rs-2-210__c0007
  kanton: 18600
  rechnung: 2 Kinder × 9'300 (Staat) = 18'600; 2 × 6'800 (Bund) = 13'600.
  ziffer: 24.1 (Code 370)
- bezeichnung: Abzug für Ehegatten (nur Bund)
  bund: 2800
  fundstellen:
  - zh-form-300-2025__c0010
  - zh-wl-2025__c0135
  - bund-dbg-2025__art-35
  kanton: null
  rechnung: Verheiratetenabzug nur direkte Bundessteuer 2'800; Staatssteuer kein Abzug (Formular «—»).
  ziffer: 24.3 (Code 365)
- bezeichnung: Steuerbares Einkommen gesamt
  bund: 64248
  fundstellen:
  - zh-form-300-2025__c0010
  kanton: 66574
  rechnung: 85'174 − 18'600 = 66'574; 80'648 − 13'600 − 2'800 = 64'248.
  ziffer: 25 (Code 390)
- bezeichnung: Wertschriften und Guthaben (Steuerwert 31.12.2025)
  bund: null
  fundstellen:
  - zh-form-300-2025__c0011
  - zh-form-340-2025__c0005
  kanton: 82000
  rechnung: 42'500 + 8'300 + 31'200 = 82'000 (Form. 340 Total Steuerwert); keine Vermögenssteuer beim Bund.
  ziffer: 30.1 (Code 400)
- bezeichnung: Steuerbares Vermögen gesamt
  bund: null
  fundstellen:
  - zh-form-300-2025__c0012
  kanton: 82000
  rechnung: 82'000 − Schulden 0 = 82'000.
  ziffer: 35 (Code 490)


**Antwort des Agenten** (136.9 s · Tools: 30 Aufrufe read, steuerwiki__formular, read, steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__beleg, steuerwiki__rechne):

> Ich habe die Positionen, Limiten und Fundstellen geholt. Jetzt rechne ich alle Beträge exakt durch.
> 
> **Kanton ZH · Steuerjahr 2025**
> Mandant: Ehepaar M. und S., Winterthur. Formular: StA Form. 300 mit Hilfsblättern 340, 360, 365 und 370. Beträge in ganzen Franken; Staat und Bund stehen in getrennten Spalten.
> 
> Status aller Werte: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | Staat | Bund | Beleg / Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb Marco | 103'000 | 103'000 | LA Ziff. 11. Kontrolle: 118'400 − 8'110 − 7'290 − 0 = 103'000 | zh-form-300-2025__c0004 |
> | 1.1 | 101 | Haupterwerb Sandra | 67'200 | 67'200 | LA Ziff. 11, inkl. Kinderzulagen 4'800 aus Ziff. 8. Kontrolle: 76'800 − 5'260 − 4'340 = 67'200 | zh-form-300-2025__c0004 |
> | 4.1 | 150 | Ertrag Wertschriften und Guthaben (Total A + B) | 1'140 | 1'140 | A: Dividenden 960 mit VSt (Code 539). B: Sparkonto-Zins 180, da ≤ 200 und ohne VSt (Code 542). Privatkonto 0 | zh-form-340-2025__c0005, zh-wl-2025__c0168 |
> | 7 | 199 | Total der Einkünfte | 171'340 | 171'340 | 103'000 + 67'200 + 1'140 | – |
> 
> - **Verrechnungssteueranspruch (Form. 340, Code 540):** 35 % × 960 = CHF 336.00. Das passt zum Steuerauszug (336 abgezogen). Es ist eine Rückerstattung, weder Einkommen noch Abzug. Dazu die IBAN angeben und das Wertschriftenverzeichnis unterschreiben.
> - **Kinderzulagen:** Sie stehen schon im Lohnausweis. Ziff. 3.4 (Code 142/143) bleibt leer, nur bei direkter Auszahlung durch die Ausgleichskasse.
> 
> ## 2. Abzüge
> 
> **Berufsauslagen Form. 360 → Ziff. 11.1 Marco (Code 220) und Ziff. 11.2 Sandra (Code 240)**
> 
> | Form. 360 | Code M / S | Staat M | Bund M | Staat S | Bund S | Rechenweg |
> |---|---|---|---|---|---|---|
> | 1.1 ÖV-Abo | 201 / 221 | 4'180 | 3'300 | – | – | Plafond Staat 5'200, Bund 3'300 |
> | 1.2 Velo | 202 / 222 | – | – | 700 | 700 | Pauschale bei ständiger Benützung |
> | 2.1 Verpflegung | 208 / 228 (M voll) | 3'200 | 3'200 | – | – | M: 15 × 220 = 3'300, gekappt auf 3'200 |
> | 2.1 Verpflegung | 206 / 226 (S verbilligt, Feld G) | – | – | 1'320 | 1'320 | S: 7.50 × 176 = 1'320, Maximum 1'600 |
> | 3 Übrige Berufskosten | 212 / 232 | 3'090 | 3'090 | 2'016 | 2'016 | 3 % × 103'000 bzw. 3 % × 67'200, Minimum 2'000, Maximum 4'000 |
> | 6 Total | 220 / 240 | **10'470** | **9'590** | **4'036** | **4'036** | |
> 
> Fundstellen: zh-form-360-2025__c0001, zh-form-360-2025__c0003, zh-form-360-2025__c0004.
> 
> **Hauptformular**
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Regel | Fundstelle |
> |---|---|---|---|---|---|---|
> | 11.1 | 220 | Berufsauslagen Marco | 10'470 | 9'590 | siehe Form. 360 | s. o. |
> | 11.2 | 240 | Berufsauslagen Sandra | 4'036 | 4'036 | siehe Form. 360 | s. o. |
> | 14.1 | 260 (eff. 262) | Säule 3a Marco | 7'258 | 7'258 | Limite mit 2. Säule; Bescheinigung beilegen | zh-wl-2025__c0081 |
> | 14.2 | 261 (eff. 263) | Säule 3a Sandra | 7'258 | 7'258 | wie oben | zh-wl-2025__c0081 |
> | 15 | 270 | Versicherungsprämien und Sparzinsen | 8'400 | 5'100 | Form. 365: 601 = 15'840, 604 = 180, Total A (606) = 16'020. Maximum B: Staat 5'800 + 2 × 1'300 = 8'400, Bund 3'700 + 2 × 700 = 5'100. Abzug = der kleinere Betrag von A und B | zh-form-365-2025__c0001, zh-form-365-2025__c0002 |
> | 16.1 | 280 | PK-Einkauf Marco | 10'000 | 10'000 | selbst überwiesen am 14.11.2025. LA Ziff. 10.2 = 0, also keine Doppelerfassung. Keine Kapitalbezüge in den letzten 3 Jahren (Sperrfrist unkritisch) | zh-form-300-2025__c0008, zh-wl-2025__c0092 |
> | 16.3 | 283 | Vermögensverwaltungskosten | 94 | 0 | Staat: 3 ‰ × 31'200 = 93.60. Bund: im Wiki keine Pauschale belegt (siehe Hinweise) | zh-wl-2025__c0095 |
> | 16.6 | 376 | Fremdbetreute Kinder | 31'900 | 32'700 | Lena: Staat min(27'300; 25'000) = 25'000, Bund min(27'300; 25'800) = 25'800. Noah: 6'900 | zh-form-300-2025__c0008, zh-stg-2025__par-31-t4 |
> | 17 | 290 | Zweiverdienerabzug | 6'100 | 14'100 | Basis = niedrigeres Erwerbseinkommen (Sandra) = 67'200 − 4'036 − 7'258 = 55'906. Staat: min(55'906; 6'100). Bund: min(max(50 % × 55'906; 8'600); 14'100) | zh-wl-2025__c0112 |
> | 18 | 299 | **Total der Abzüge** | **85'516** | **90'042** | Summe der Zeilen oben | – |
> 
> ## 3. Einkommensberechnung
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 19 | 199 | Total Einkünfte | 171'340 | 171'340 | |
> | 20 | 299 | Total Abzüge | 85'516 | 90'042 | |
> | 21 | 310 | **Nettoeinkommen** | **85'824** | **81'298** | 171'340 − Abzüge |
> | 22.1 | 320 | Krankheits- und Unfallkosten | 0 | 0 | Kosten 1'850 + 1'240 = 3'090. Selbstbehalt 5 %: Staat 4'291.20, Bund 4'064.90. Die Kosten liegen darunter, also kein Abzug |
> | 22.2 | 324 | Gemeinnützige Zuwendungen | 650 | 650 | 400 + 250 = 650. Mindestens 100 erreicht, Maximum 20 % × Netto (Staat 17'164.80), also voll abziehbar |
> | 23 | 350 | **Reineinkommen** | **85'174** | **80'648** | Netto − 0 − 650 |
> | 24.1 | 370 | Kinder im Haushalt (2) | 18'600 | 13'600 | 2 × 9'300 bzw. 2 × 6'800 (Lena und Noah) |
> | 24.3 | 365 | Verheiratetenabzug | – | 2'800 | nur Bundessteuer |
> | 25 | 390 | **Steuerbares Einkommen gesamt** | **66'574** | **64'248** | 85'174 − 18'600 bzw. 80'648 − 13'600 − 2'800 |
> | 26.1 / 26.2 | 394 / 396 | Anteile andere Kantone / Ausland | 0 | 0 | |
> | 27 | 398 | **Steuerbares Einkommen ZH / Schweiz** | **66'574** | **64'248** | |
> 
> - **Krankheitskosten:** Form. 370 ist nicht nötig, weil kein Abzug entsteht. Die Belege trotzdem aufbewahren.
> - **Plausibilität:** Staat liegt 2'326 über Bund. Das ist erklärbar durch den Bund-Zweiverdienerabzug (14'100 statt 6'100) und den Verheiratetenabzug (2'800), die höheren Bund-Kinderbetreuungskosten, den kleineren Bund-Versicherungsabzug und den kleineren Bund-Kinderabzug.
> - **Bund, ausserhalb des Formulars:** Auf den Steuerbetrag kommt eine Ermässigung von CHF 263 je Kind (2 × 263 = 526). Das ist eine Tarifwirkung, es gibt kein Formularfeld (bund-dbg-2025__art-36-t4).
> 
> ## 4. Vermögen (Staat, Bund hat keine Vermögenssteuer)
> 
> | Ziff. | Code | Position | Betrag | Rechenweg |
> |---|---|---|---|---|
> | 30.1 | 400 | Wertschriften und Guthaben (Form. 340 Total Steuerwert) | 82'000 | Sparkonto 42'500 + Privatkonto 8'300 + Depot 31'200 |
> | 33 | 460 | Total Vermögenswerte | 82'000 | keine weiteren Positionen belegt |
> | 34 | 470 | Schulden | 0 | Mieter, keine Schulden belegt |
> | 35 | 490 | Steuerbares Vermögen gesamt | 82'000 | |
> | 37 | 498 | Steuerbares Vermögen im Kanton ZH | 82'000 | |
> 
> Das steuerfreie Vermögen ergibt sich nur aus dem Tarif, nichts abziehen. PK-Guthaben und Säule 3a sind kein steuerbares Vermögen und werden nicht deklariert. Ziff. 40 (Kapitalleistungen aus Vorsorge): keine.
> 
> ## 5. Nicht zu deklarieren oder nicht abziehbar
> 
> - **Swisscom-Handyrechnungen (1'080):** private Lebenshaltungskosten, kein Abzug. Ein Berufsanteil ist mit der Pauschale Form. 360 Ziff. 3 abgegolten (zh-zstb-30-3__c0018 nennt das Telefonabonnement ausdrücklich als Lebenshaltungskosten, dort zu Liegenschaften). Kein Beleg beilegen.
> - **Hausrat- und Privathaftpflichtversicherung (465):** Sachversicherungen, nicht im Versicherungsabzug (Form. 365 kennt nur Kranken-, Unfall-, Leben-/Rente und Sparzinsen). Das Wiki hat dazu keinen eigenen Ausschlusssatz, die Aussage folgt aus dem Aufbau von Form. 365. Selbst wirkungslos, weil das Maximum ohnehin ausgeschöpft ist.
> - **Kinderzulagen 4'800:** nicht nochmals erfassen, sie sind schon in Ziff. 11 des Lohnausweises.
> - **PK-Beiträge 7'290 / 4'340 und AHV/ALV/NBUV:** schon im Nettolohn abgezogen, nicht nochmals abziehen.
> - **Krankenkassenprämien als Krankheitskosten:** nicht abziehbar. Sie gehören nur in Ziff. 15 (Form. 365, Code 601).
> - **Kita- und Mittagsverpflegung:** Die Eltern geben das Essen mit, daher kein Verpflegungsanteil in 16.6. Verpflegung wäre sonst nicht abziehbar.
> - **Verrechnungssteuer 336:** weder Einkommen noch Abzug, nur Rückerstattung im Wertschriftenverzeichnis.
> - **Fahrkosten Sandra:** nur die Velopauschale, keine Abo- oder Autokosten.
> - **Keine Liegenschaft:** keine Mietzinsen deklarieren, kein Eigenmietwert. Keine Schuldzinsen.
> 
> ## 6. Annahmen, offene Punkte, Rückfragen
> 
> 1. **Verpflegung Sandra (1'320, Code 226):** Der Abzug setzt voraus, dass eine Heimkehr in der Mittagspause nicht möglich ist. Sandra wohnt und arbeitet in Winterthur. Ich habe den Standardfall mit Personalrestaurant (Feld G) erfasst. **Rückfrage:** Isst sie wirklich täglich im Personalrestaurant, ohne nach Hause zu fahren? Falls ihr Mittag eine Heimkehr zulässt, entfallen 1'320. Dann sinkt ihre Berufsauslagen-Summe auf 2'716 und die Basis für den Zweiverdienerabzug steigt auf 57'226. Die Abzüge bleiben am Maximum (Staat 6'100, Bund 14'100).
> 2. **Verpflegung Marco (3'200):** Annahme: Mittagessen im Restaurant, Heimkehr wegen Arbeitsort Zug nicht möglich. Bund: kein Abzug, wenn die Hauptmahlzeit höchstens 10 Fr. kostet; hier nicht gegeben angenommen.
> 3. **Hort Noah (6'900):** Falls die Rechnung Mittagstisch oder Verpflegung enthält, ist dieser Anteil herauszurechnen. Nur die reine Betreuung ist abziehbar. **Rückfrage:** Hort-Rechnung nach Betreuung und Verpflegung aufgeschlüsselt? Die Kita-Rechnung (27'300) überschreitet die Staatslimite ohnehin, dort wirkt eine Korrektur nur beim Bund (Limite 25'800).
> 4. **Vermögensverwaltungskosten Bund (Code 283):** Im Wiki ist für den Bund nur der effektive Depotgebührenausweis belegt (bund-wl-2a-2025__c0056), keine Pauschale. Ich habe Bund 0 gesetzt. Falls die Fachperson die kantonale Pauschale auch für den Bund anwendet, wären es 94. Das ist ein Vorbehalt (Fachperson). Die Wirkung ist minimal.
> 5. **PK-Einkauf (10'000):** Der Abzug ist nur im Rahmen des Einkaufspotenzials zulässig. Das ergibt sich aus der Bescheinigung der PK (Form. 21 EDP), die beizulegen ist.
> 6. **Spenden:** Annahme: Sowohl das SRK als auch UNICEF Schweiz sind steuerbefreit mit Sitz in der Schweiz, wie angegeben. Im ZH-Verzeichnis der steuerbefreiten Institutionen nicht geprüft. Liste beilegen, Quittungen nur auf Verlangen.
> 7. **Fahrkosten und Arbeitsort Zug:** Wohnsitz am 31.12. ist ZH, es gibt keine Steuerausscheidung. Das GA/Streckenabo steht Marco nur zu, wenn Feld F wie angegeben leer ist.
> 
> ## 7. Beilagen (Einreichung, ZH)
> 
> - **Immer:** beide Lohnausweise.
> - **Hilfsblätter:** Form. 360 (Marco und Sandra), Form. 365 und Form. 340 (Wertschriftenverzeichnis, bzw. Verweis auf den ZKB-Steuerauszug).
> - **Bei Abzug:** Säule-3a-Bescheinigungen (beide), PK-Einkaufsbescheinigung (Marco) und Aufstellung der Betreuungskosten mit Empfängern (Ziff. 16.6).
> - **Auf Verlangen:** Spendenquittungen, Kita- und Hort-Rechnungen, Krankenkassenbelege.

## f-sg

**Frage:** Steuerjahr 2025, Kanton SG. Mandant/Haushalt: Alleinerziehende, geschiedene Mutter (Nadine, 38) mit Wohnsitz im Toggenburg SG (Mieterin), Sachbearbeiterin Logistik in St. Gallen (100 %, Arbeitsbeginn 06:00), Pensionskasse angeschlossen. Sohn Elias (geb. 2020, 5 Jahre) lebt bei ihr, besucht seit August 2025 den Kindergarten und ausserhalb davon Kita/Tagesstruktur. Der Ex-Ehemann zahlt Kinderalimente.

Belege:
- Lohnausweis 2025: Ziff. 8 Bruttolohn 83'500 (inkl. Kinderzulage 2'400); Ziff. 9 AHV/IV/EO/ALV/NBUV 5'890; Ziff. 10.1 BVG ordentlich 4'610; Ziff. 10.2 0; Ziff. 11 Nettolohn 73'000. Feld F und Feld G nicht angekreuzt. 100 %, 220 Arbeitstage.
- Arbeitsweg mit Privatauto Wohnort–St. Gallen 32 km (einfach), 220 Tage; Begründung: Arbeitsbeginn 06:00, erste öV-Verbindung ab Wohnort erst 06:40 (Fehlen eines öffentlichen Verkehrsmittels). Mittagessen im Restaurant, keine Kantine.
- Kontoauszüge Kinderalimente vom Ex-Ehemann für Elias: 12 × 800 = 9'600.
- Krankenkasse 2025: Prämien Nadine 5'280, Elias 1'320; individuelle Prämienverbilligung 1'800 (direkt an KK); Leistungsabrechnung Kostenbeteiligung (Franchise/Selbstbehalt) 850.
- Säule-3a-Bescheinigung 7'258; Pensionskasse: Bescheinigung freiwilliger Einkauf, direkt bezahlt am 20.10.2025: 6'000.
- Kita/Tagesstruktur Elias: Rechnungen 2025 total 9'840, davon separat ausgewiesene Mahlzeiten 1'080.
- Zahnarztrechnung Nadine 2'750 (nicht von der Krankenkasse übernommen).
- Bank-Steuerauszug Raiffeisen per 31.12.2025: Sparkonto 31'500, Bruttozins 68 (ohne VSt-Abzug).
- Quittungen: Excel-Kurs Klubschule (beruflich bedingt, selbst bezahlt) 340; Spende Caritas St. Gallen-Appenzell 80.
- Weitere Belege: Motorfahrzeugsteuer 2025 410; Auto-Haftpflicht-/Kaskoversicherung 1'020; Handy-Abo 720.

Auftrag: Erstelle die Ausfüllhilfe (alle relevanten Positionen mit Ziffer/Code, Beträge Staat und Bund, Rechenweg, Fundstellen) und nenne, was nicht zu deklarieren ist.

**Soll (Referenz):** nicht_deklarieren:
- 'Spende Caritas 80: unter Mindestbetrag 100 (sg-wl-2025__c0102, bund-dbg-2025__art-33a).'
- 'Motorfahrzeugsteuer 410 und Auto-Haftpflicht/Kasko 1''020: mit Kilometeransatz abgegolten bzw. Motorfahrzeugversicherungen vom Versicherungsabzug ausgeschlossen
  (sg-wl-2025__c0077, sg-wl-2025__c0088, sg-stg-2025__art-47).'
- 'Handy-Abo 720: private Lebenshaltung (sg-stg-2025__art-47, bund-dbg-2025__art-34).'
- 'Kita-Mahlzeiten 1''080: keine Betreuungskosten (sg-wl-2025__c0092).'
- Kinderzulage 2'400 nicht separat unter Ziff. 3.5 – bereits im Lohnausweis (sg-wl-2025__c0061).
positionen:
- bezeichnung: Haupterwerb – Nettolohn
  bund: 73000
  fundstellen:
  - sg-form-1-2025__c0004
  - sg-wl-2025__c0042
  - sg-form-32-2025__c0001
  kanton: 73000
  rechnung: '83''500 − 5''890 − 4''610 = 73''000 (Lohnausweis Ziff. 11). Hinweis: Formular 1 SG hat nur eine Spalte; Bundeswerte setzt die Veranlagungsbehörde gemäss
    Merkblatt 32.'
  ziffer: 1.1 Person 1 (Code 100)
- bezeichnung: Einkünfte aus Wertschriften und Guthaben
  bund: 68
  fundstellen:
  - sg-form-1-2025__c0006
  - sg-form-2-2025__c0006
  - sg-wl-2025__c0130
  - bund-vstg__art-5-t1
  kanton: 68
  rechnung: Sparzins 68 brutto, bis 200 verrechnungssteuerfrei → Abschnitt B; kein VSt-Anspruch.
  ziffer: 4.1 (Code 146) – aus Formular 2
- bezeichnung: Erhaltene Unterhaltsbeiträge für Elias
  bund: 9600
  fundstellen:
  - sg-form-1-2025__c0006
  - sg-wl-2025__c0068
  - bund-dbg-2025__art-23
  kanton: 9600
  rechnung: 12 × 800 = 9'600; beim empfangenden Elternteil steuerbar.
  ziffer: 6.1 für minderjährige Kinder (Code 156)
- bezeichnung: Total der Einkünfte
  bund: 82668
  fundstellen:
  - sg-form-1-2025__c0006
  kanton: 82668
  rechnung: 73'000 + 68 + 9'600 = 82'668.
  ziffer: 7 (Code 168)
- bezeichnung: Fahrkosten Motorfahrzeug
  bund: 3300
  fundstellen:
  - sg-form-4-2025__c0002
  - sg-wl-2025__c0075
  - sg-wl-2025__c0077
  - sg-stg-2025__art-39
  - sg-form-32-2025__c0002
  - bund-dbg-2025__art-26
  - bund-bkv-2025__art-5
  - bund-bkv-2025__anhang-1
  kanton: 8000
  rechnung: 32 km × 2 × 220 Tage = 14'080 km × 0.70 = 9'856 (Begründung «Fehlen eines öffentlichen Verkehrsmittels» ankreuzen). Kanton Max. 8'000; Bund Max. 3'300.
  ziffer: Formular 4 Person 1, Ziff. 1.3 (Code 404) / Zwischentotal (Code 406)
- bezeichnung: Mehrkosten auswärtige Verpflegung
  bund: 3200
  fundstellen:
  - sg-form-4-2025__c0003
  - sg-wl-2025__c0078
  - bund-bkv-2025__anhang-1
  kanton: 3200
  rechnung: 220 × 15 = 3'300 → Max. 3'200.
  ziffer: Formular 4 Person 1, Ziff. 2.1 (Code 408)
- bezeichnung: Übrige Berufskosten pauschal
  bund: 2190
  fundstellen:
  - sg-form-4-2025__c0003
  - sg-wl-2025__c0080
  - sg-stv__art-21
  - sg-form-32-2025__c0002
  - bund-bkv-2025__anhang-1
  kanton: 2400
  rechnung: 'Kanton: 700 + 10 % × 73''000 = 8''000 → Max. 2''400. Bund: 3 % × 73''000 = 2''190 (zwischen 2''000 und 4''000).'
  ziffer: Formular 4 Person 1, Ziff. 3.1 (Code 416)
- bezeichnung: Berufskosten Person 1 total
  bund: 8690
  fundstellen:
  - sg-form-4-2025__c0004
  - sg-form-1-2025__c0008
  - sg-form-32-2025__c0002
  kanton: 13600
  rechnung: Kanton 8'000 + 3'200 + 2'400 = 13'600; Bund 3'300 + 3'200 + 2'190 = 8'690.
  ziffer: 10.1 (Code 438)
- bezeichnung: Säule 3a
  bund: 7258
  fundstellen:
  - sg-form-1-2025__c0008
  - sg-wl-2025__c0085
  - bund-bvv3__art-7
  - bund-bsv-masszahlen-2025-2026__c0003
  kanton: 7258
  rechnung: Mit 2. Säule max. 7'258; bezahlt 7'258.
  ziffer: 13.1 Person 1 (Code 208)
- bezeichnung: Säule 2 – Einkaufsbeitrag direkt bezahlt
  bund: 6000
  fundstellen:
  - sg-form-1-2025__c0008
  - sg-wl-2025__c0086
  - sg-stg-2025__art-45-t1
  - bund-dbg-2025__art-33-t2
  kanton: 6000
  rechnung: Einkauf 6'000 gem. PK-Bescheinigung; nicht im Lohnausweis (Ziff. 10.2 = 0), daher hier abziehbar.
  ziffer: 13.2 Person 1 (Code 218)
- bezeichnung: Versicherungsprämien und Sparzinsen
  bund: 2500
  fundstellen:
  - sg-form-6-2025__c0001
  - sg-form-6-2025__c0002
  - sg-wl-2025__c0087
  - sg-wl-2025__c0088
  - sg-stg-2025__art-45-t2
  - sg-form-32-2025__c0003
  - bund-dbg-2025__art-33-t2
  - bund-dbg-2025__art-33-t5
  kanton: 4500
  rechnung: 'A: 5''280 + 1''320 − Prämienverbilligung 1''800 + Sparzins 68 = 4''868. B Kanton (alleinstehend): 3''400 + 1''100 für 1 Kind = 4''500. Bund: 1''800 +
    700 = 2''500 (mit 2./3a-Beiträgen). Abzug = niedrigerer Betrag.'
  ziffer: 14 (Code 600) – via Formular 6
- bezeichnung: Kinderbetreuungskosten bei Drittbetreuung
  bund: 8760
  fundstellen:
  - sg-form-1-2025__c0009
  - sg-wl-2025__c0092
  - sg-stg-2025__art-45-t3
  - bund-dbg-2025__art-33-t7
  - bund-dbg-2025__art-34
  kanton: 8760
  rechnung: 'FALLE: 9''840 − separat ausgewiesene Mahlzeiten 1''080 (Verpflegung ist keine Betreuung) = 8''760; unter Max. Kanton 26''700 / Bund 25''800.'
  ziffer: 16.2 (Code 258)
- bezeichnung: Berufsorientierte Aus- und Weiterbildung
  bund: 340
  fundstellen:
  - sg-form-1-2025__c0009
  - sg-wl-2025__c0095
  - sg-wl-2025__c0004
  - sg-stg-2025__art-45-t4
  - bund-dbg-2025__art-33-t4
  kanton: 400
  rechnung: 'Kanton: Pauschale 400 ohne Nachweis für hauptberuflich Unselbständige (höher als effektive 340). Bund: nur effektive Kosten 340.'
  ziffer: 16.4 Person 1 (Code 223)
- bezeichnung: Total der Abzüge
  bund: 33548
  fundstellen:
  - sg-form-1-2025__c0009
  kanton: 40518
  rechnung: Kanton 13'600 + 7'258 + 6'000 + 4'500 + 8'760 + 400 = 40'518; Bund 8'690 + 7'258 + 6'000 + 2'500 + 8'760 + 340 = 33'548.
  ziffer: 18 (Code 230)
- bezeichnung: Nettoeinkommen
  bund: 49120
  fundstellen:
  - sg-form-1-2025__c0010
  kanton: 42150
  rechnung: 82'668 − 40'518 = 42'150; 82'668 − 33'548 = 49'120.
  ziffer: 20 (Code 234)
- bezeichnung: Krankheits- und Unfallkosten
  bund: 1144
  fundstellen:
  - sg-form-1-2025__c0010
  - sg-form-6-2025__c0003
  - sg-wl-2025__c0098
  - sg-stg-2025__art-46
  - sg-form-32-2025__c0005
  - bund-dbg-2025__art-33-t3
  kanton: 2757
  rechnung: 'Selbst getragen 2''750 + 850 = 3''600. Kanton: Selbstbehalt 2 % × 42''150 = 843 → 2''757. Bund: Selbstbehalt 5 % × 49''120 = 2''456 → 1''144.'
  ziffer: 21.1 (Vorkolonne Code 650, Selbstbehalt Code 238, Abzug Code 240)
- bezeichnung: Freiwillige Zuwendungen
  bund: 0
  fundstellen:
  - sg-form-1-2025__c0010
  - sg-wl-2025__c0102
  - sg-stg-2025__art-46
  - bund-dbg-2025__art-33a
  kanton: 0
  rechnung: 'FALLE: Spende 80 erreicht den Mindestbetrag von 100 nicht → kein Abzug (Kanton und Bund).'
  ziffer: 21.3 (Code 244)
- bezeichnung: Reineinkommen
  bund: 47976
  fundstellen:
  - sg-form-1-2025__c0010
  kanton: 39393
  rechnung: 42'150 − 2'757 = 39'393; 49'120 − 1'144 = 47'976.
  ziffer: 22 (Code 248)
- bezeichnung: Kinderabzug Kind in Schule/Ausbildung
  bund: 6800
  fundstellen:
  - sg-form-1-2025__c0011
  - sg-wl-2025__c0104
  - sg-stg-2025__art-48
  - sg-form-32-2025__c0006
  - bund-dbg-2025__art-35
  kanton: 10800
  rechnung: 'FALLE: Elias besucht am 31.12.2025 den Kindergarten = Volksschule → 23.2 mit 10''800 (nicht 23.1 Vorschulalter 7''600). Bund einheitlich 6''800.'
  ziffer: 23.2 (Code 254)
- bezeichnung: Steuerbares Einkommen gesamt
  bund: 41176
  fundstellen:
  - sg-form-1-2025__c0011
  kanton: 28593
  rechnung: 39'393 − 10'800 = 28'593; 47'976 − 6'800 = 41'176.
  ziffer: 24 (Code 268)
- bezeichnung: Wertschriften und Guthaben
  bund: null
  fundstellen:
  - sg-form-1-2025__c0012
  - sg-form-2-2025__c0006
  kanton: 31500
  rechnung: Sparkonto 31'500 (Formular 2); keine Vermögenssteuer beim Bund.
  ziffer: 30.1 (Code 300)
- bezeichnung: Sozialabzug Vermögen alleinstehend
  bund: null
  fundstellen:
  - sg-form-1-2025__c0013
  - sg-wl-2025__c0118
  kanton: 75000
  rechnung: Fix 75'000.
  ziffer: 36.1 (Code 330)
- bezeichnung: Sozialabzug Vermögen je minderjähriges Kind
  bund: null
  fundstellen:
  - sg-form-1-2025__c0013
  - sg-wl-2025__c0118
  kanton: 20000
  rechnung: 1 Kind × 20'000.
  ziffer: 36.3 (Code 334)
- bezeichnung: Steuerbares Vermögen gesamt
  bund: null
  fundstellen:
  - sg-form-1-2025__c0013
  kanton: 0
  rechnung: 31'500 − 75'000 − 20'000 < 0 → 0.
  ziffer: 37 (Code 338)


**Antwort des Agenten** (154.3 s · Tools: 32 Aufrufe read, steuerwiki__formular, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, message, steuerwiki__rechne):

> **SG · Steuerjahr 2025 – Ausfüllhilfe Nadine (alleinerziehend, 1 Kind)**
> 
> Das Formular hat eine Spalte, und die Behörde setzt die Bundeswerte automatisch um (sg-wl-2025__c0173). Die Bundesbeträge unten sind deshalb Vergleichswerte und keine separaten Eingaben. Alle Werte haben den Status ☑️ agent-geprüft (Abnahme offen).
> 
> ## Einkünfte
> 
> | Ziff. / Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 1.1 / 100 | Haupterwerb | 73'000 | 73'000 | Nettolohn Lohnausweis Ziff. 11, nicht Ziff. 8. Die Kinderzulage 2'400 ist darin enthalten. c0042 |
> | 6.1 / 156 | Unterhaltsbeiträge für minderjährige Kinder | 9'600 | 9'600 | 12 × 800. Beim Empfänger steuerbar. c0068 |
> | 4.1 / 146 | Wertschriften und Guthaben | 68 | 68 | Form. 2 Spalte B. Bruttozins ≤ 200 und ohne Verrechnungssteuer. Code 999 bleibt leer. c0135 |
> | 7 / 168 | Total Einkünfte | **82'668** | **82'668** | 73'000 + 9'600 + 68 |
> 
> ## Abzüge
> 
> **Form. 4 Berufskosten (Übertrag in Ziff. 10.1, Code 438)**
> 
> | Form. 4 | Staat | Bund | Rechenweg |
> |---|---|---|---|
> | Ziff. 1.3 / Code 404 Auto | 9'856 | 9'856 | 2 × 32 km × 220 Tage × 0.70 |
> | Zwischentotal Fahrkosten / Code 406 | 8'000 | 3'300 | Maximum Kanton 8'000, Bund 3'300 |
> | Ziff. 2.1 / Code 408 Verpflegung | 3'200 | 3'200 | 15 × 220 = 3'300, begrenzt auf 3'200. Feld G nicht angekreuzt |
> | Ziff. 3.1 / Code 416 übrige Berufskosten | 2'400 | 2'190 | Kanton: min(700 + 10 % × 73'000; 2'400). Bund: min(max(3 % × 73'000; 2'000); 4'000) |
> | **Ziff. 10.1 / 438 Total** | **13'600** | **8'690** | |
> 
> Fundstellen: sg-form-4-2025__c0002/c0003, sg-wl-2025__c0077/c0078/c0080.
> 
> | Ziff. / Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 13.1 / 208 | Säule 3a | 7'258 | 7'258 | Bescheinigung 7'258 = Maximum mit 2. Säule. c0085 |
> | 13.2 / 218 | PK-Einkauf | 6'000 | 6'000 | Nur der freiwillige Einkauf. Die BVG-Beiträge 4'610 aus Lohnausweis Ziff. 10.1 sind im Nettolohn schon abgezogen. c0086 |
> | 14 / 600 | Versicherungsprämien und Sparzinsen | 4'500 | 2'500 | A = 5'280 + 1'320 + 68 − 1'800 = 4'868. Maximum B: Kanton 3'400 + 1'100 Kind = 4'500, Bund 1'800 + 700 = 2'500. Abzug ist min(A; B). Kein Zuschlag «ohne Vorsorge», da BVG und 3a abgezogen werden. sg-form-6-2025__c0002 |
> | 16.2 / 258 | Kinderbetreuung | 8'760 | 8'760 | 9'840 − 1'080 Mahlzeiten, weit unter dem Maximum (Kanton 26'700, Bund 25'800). Form. 10 beilegen. c0092 |
> | 16.4 / 223 | Weiterbildung | 400 | 340 | Kanton: Pauschale 400 ohne Nachweis ist höher als die Kosten 340. Bund: nur effektive Kosten, also 340. c0094 |
> | 17 / 226 | Zweiverdienerabzug | 0 | 0 | Nicht anwendbar, da keine Ehe |
> | 18 / 230 | **Total Abzüge** | **40'518** | **33'548** | |
> 
> Für Ziff. 16.4 ist die Eintragung nicht belegt. Ich würde 400 eintragen und die Kursquittung 340 als Aufstellung beilegen. Ob die Behörde den Bundesbetrag dann automatisch auf 340 setzt, habe ich nicht geprüft.
> 
> ## Einkommensberechnung
> 
> | Ziff. / Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 20 / 234 | Nettoeinkommen | **42'150** | **49'120** | 82'668 − Abzüge |
> | 21.1 / 650 | Krankheitskosten (Vorkolonne) | 3'600 | 3'600 | Zahnarzt 2'750 + Kostenbeteiligung 850. Die Krankenkassenprämien gehören nicht hierher. c0098 |
> | 21.1 / 238 | Selbstbehalt | 843 | 2'456 | Kanton 2 %, Bund 5 % des Nettoeinkommens |
> | 21.1 / 240 | Abzug Krankheitskosten | 2'757 | 1'144 | 3'600 − Selbstbehalt |
> | 21.3 / 244 | Zuwendungen | 0 | 0 | 80 liegt unter dem Minimum von 100. c0102 |
> | 22 / 248 | **Reineinkommen** | **39'393** | **47'976** | |
> | 23.1 / 252 | Kinderabzug vorschulpflichtig | 0 | 0 | Der Kindergarten zählt zur Schulpflicht, daher Ziff. 23.2. c0104 |
> | 23.2 / 254 | Kinderabzug Schule | 10'800 | 6'800 | Elias. Kein Abzug Ziff. 12.2, da Nadine die Alimente erhält. sg-form-32-2025__c0006 |
> | 23.3 / 256, 23.4 / 264 | Ausbildungskosten Kinder, unterstützte Personen | 0 | 0 | Nicht anwendbar |
> | 24 / 268 | **Steuerbares Einkommen** | **28'593** | **41'176** | 39'393 − 10'800 bzw. 47'976 − 6'800 |
> 
> **Bund-Tarif:** Nadine lebt mit Kind im gleichen Haushalt, daher gilt der Elterntarif. Der Steuerbetrag ermässigt sich um 263 pro Kind (bund-wl-2a-2025__c0060, bund-rs-2-210__c0016).
> 
> **Plausibilität:** Die Differenz von 12'583 zwischen Bund und Staat setzt sich so zusammen:
> - Abzüge: 6'970
> - Krankheitskosten: 1'613
> - Kinderabzug: 4'000
> 
> ## Vermögen (nur Staat)
> 
> | Ziff. / Code | Position | Betrag |
> |---|---|---|
> | 30.1 / 300 | Sparkonto Raiffeisen | 31'500 |
> | 30.4 / 306 | Motorfahrzeug | offen |
> | 33 / 322 | Total Vermögenswerte | 31'500 + Fahrzeugwert |
> | 34.1 / 504 | Privatschulden | 0 |
> | 35 / 326 | Reinvermögen | 31'500 + Fahrzeugwert |
> | 36.1 / 330 | Abzug alleinstehend | 75'000 |
> | 36.3 / 334 | Abzug minderjähriges Kind | 20'000 |
> | 37 / 338 | **Steuerbares Vermögen** | **0** |
> 
> Der Fahrzeugwert ist Anschaffungswert − 20 % pro Jahr seit Erwerb (c0111). Das steuerbare Vermögen bleibt bei 0, solange er höchstens 63'500 beträgt. Ziff. 36.2 gilt nicht (nur Ehepaare).
> 
> ## Nicht zu deklarieren oder nicht abziehbar
> 
> - **Kinderzulage 2'400:** Sie steckt schon im Lohnausweis. Nicht zusätzlich in Ziff. 3.5 eintragen, sonst wird sie doppelt erfasst.
> - **Prämienverbilligung 1'800:** Kein Einkommen. Sie wird in Form. 6 Teil A (e) von den Prämien abgezogen und ist oben in Ziff. 14 berücksichtigt.
> - **Lohnabzüge (AHV 5'890 und BVG 4'610):** Sie sind im Nettolohn berücksichtigt und nicht nochmals abzuziehen.
> - **Kita-Mahlzeiten 1'080:** Verpflegung ist in Ziff. 16.2 nicht abziehbar.
> - **Auto-Haftpflicht/Kaskoversicherung 1'020:** Motorfahrzeug- und Haftpflichtversicherungen sind in Ziff. 14 nicht abziehbar.
> - **Motorfahrzeugsteuer 410:** Es gibt keine eigene Position. Die Fahrkosten werden mit 0.70 pro km gerechnet. Dass die Steuer damit abgegolten ist, habe ich im Wiki nicht gefunden.
> - **Handy-Abo 720:** Es gibt keine eigene Position. Kein Abzug, da die Pauschale für übrige Berufskosten bereits ausgeschöpft ist.
> - **Spende Caritas 80:** Unter dem Minimum von 100. Sie wird nur abgezogen, wenn die Spenden 2025 zusammen mindestens 100 ergeben.
> - **Pensionskassen- und 3a-Guthaben:** Vorsorgeguthaben sind bis zur Fälligkeit kein Vermögen (sg-wl-2025__c0107).
> - **Verrechnungssteueranspruch (Code 999):** Keiner, da kein Abzug auf dem Zins.
> - **Nicht anwendbare Positionen:** Wertschriftenverwaltungskosten Ziff. 16.1 (kein Depot), Alimentenabzug Ziff. 12 (Nadine erhält sie), Ziff. 6.1 Code 154 und Zweiverdienerabzug Ziff. 17.
> 
> ## Annahmen und Rückfragen
> 
> 1. **Auto:** Ich habe das Auto mit der Begründung «Fehlen eines öffentlichen Verkehrsmittels» angesetzt (Form. 4 Ziff. 1.3). Der Fahrplan (erste Verbindung 06:40, Arbeitsbeginn 06:00) sollte als Beleg bereitliegen. Falls das Auto nicht anerkannt wird, entfallen diese Fahrkosten. Eine Ersatzrechnung mit den ÖV-Kosten habe ich nicht gemacht.
> 2. **Verpflegung:** Ich gehe davon aus, dass sie mittags wegen der 32 km nicht heimkehren kann.
> 3. **Kinderbetreuung:** Die Betreuung muss mit den Arbeitszeiten zusammenhängen. Beim Bund ist Betreuung ausserhalb der Arbeitszeit nicht abziehbar.
> 4. **Krankenkassenprämien:** Sind die 6'600 brutto, das heisst vor der Verbilligung? Das Ergebnis ändert sich nicht, weil der Abzug in beiden Fällen am Maximum liegt.
> 5. **Alimente:** Gehören die 9'600 ausschliesslich zu Elias? Sonst muss der Anteil für Nadine selbst in Code 154 stehen. Beim ersten Mal sind Scheidungsurteil und Zahlungsnachweis beizulegen.
> 6. **Fahrzeug:** Ich brauche Anschaffungspreis und Erwerbsjahr für Code 306.
> 7. **Beilagen:** Zwingend sind der Lohnausweis, die 3a-Bescheinigung sowie Bescheinigung und Einkaufsberechnung der Pensionskasse. Der Bank-Steuerauszug ist bei Papiereinreichung nötig.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.

## f-tg

**Frage:** Steuerjahr 2025, Kanton TG. Mandant/Haushalt: Verwitwete Rentnerin (geb. 1955, 70 Jahre), alleinstehend, wohnt im eigenen Einfamilienhaus in Frauenfeld TG (Baujahr 1986, am Wohnsitz dauernd selbst bewohnt). Keine Erwerbstätigkeit, keine Beiträge an 2. Säule oder Säule 3a.

Belege:
- AHV-Rentenbescheinigung 2025: Altersrente 12 × 2'250 = 27'000.
- Pensionskasse: Rentenbescheinigung 2025 Altersrente 12 × 900 = 10'800; Rentenbeginn 01.01.2020.
- Bank-Steuerauszug TKB per 31.12.2025: Sparkonto 48'000, Bruttozins 250 (VSt 87.50 abgezogen); Depot Schweizer Aktien Steuerwert 95'000, Bruttodividenden 2'100 (VSt 735 abgezogen).
- Liegenschaftensteuerrechnung/Schätzung EFH Frauenfeld: indexierter Mietwert aus Selbstnutzung 2025 20'400; Steuerwert 410'000.
- Hypothekarbank: Hypothek 180'000 per 31.12.2025, Hypothekarzinsen 2025 3'150.
- Handwerkerrechnungen 2025: Malerarbeiten Innenrenovation (Ersatzanstrich) 6'400; Gebäudeversicherungsprämie 520; Baumschnitt/Gartenpflege 480; Neubau Wintergarten-Anbau 31'000.
- Krankenkasse 2025: Prämien Grund- und Zusatzversicherung 6'240, keine Prämienverbilligung; Kostenbeteiligung (Franchise/Selbstbehalt) gemäss Leistungsabrechnung 1'000.
- Zahnarztrechnung (Krone) 4'440; Brille gemäss augenärztlicher Verordnung 1'400, davon von der Zusatzversicherung vergütet 300.
- Spendenquittungen: Krebsliga Thurgau 300; Pro Senectute Thurgau 250.
- Weitere Belege: Hausratversicherung 380; Serafe-Rechnung 335; Handyrechnung 2025.

Auftrag: Erstelle die Ausfüllhilfe (alle relevanten Positionen mit Ziffer/Code, Beträge Staat und Bund, Rechenweg, Fundstellen) und nenne, was nicht zu deklarieren ist.

**Soll (Referenz):** nicht_deklarieren:
- 'Wintergarten-Anbau 31''000: wertvermehrende Investition/Anlagekosten, kein Unterhalt (tg-wl-2025__c0233, bund-dbg-2025__art-34).'
- 'Hausratversicherung 380: keine Liegenschafts-Sachversicherung und keine Personenversicherung (tg-wl-2025__c0227).'
- 'Serafe-Rechnung 335 und Handyrechnung: private Lebenshaltung (bund-dbg-2025__art-34).'
- 'Von der Zusatzversicherung vergütete 300 der Brille: nicht selbst getragen (tg-wl-2025__c0203).'
- Keine Säule 3a, keine Berufskosten, kein Zweiverdienerabzug (keine Erwerbstätigkeit).
positionen:
- bezeichnung: AHV-Altersrente
  bund: 27000
  fundstellen:
  - tg-form-01-2025__c0007
  - tg-wl-2025__c0076
  - bund-dbg-2025__art-22-t1
  kanton: 27000
  rechnung: 12 × 2'250 = 27'000; zu 100 % steuerbar.
  ziffer: 3.1 Person 1 (Code 130)
- bezeichnung: Rente 2. Säule
  bund: 10800
  fundstellen:
  - tg-form-01-2025__c0007
  - tg-wl-2025__c0077
  - bund-dbg-2025__art-22-t1
  kanton: 10800
  rechnung: 12 × 900 = 10'800; Rentenbeginn 2020 → keine 80-%-Übergangsregel (nur Renten mit Beginn vor 2002), 100 % steuerbar.
  ziffer: 3.2 Person 1 (Code 132)
- bezeichnung: Wertschriften- und Zinserträge
  bund: 2350
  fundstellen:
  - tg-form-01-2025__c0008
  - tg-form-02-2025__c0006
  - tg-wl-2025__c0151
  - tg-wl-2025__c0159
  - tg-wl-2025__c0163
  - tg-stv__par-10a
  - bund-vstg__art-5-t1
  - bund-wl-2a-2025__c0056
  kanton: 2160
  rechnung: 'Spalte 8 (mit VSt): Sparzins 250 (über 200 → VSt-pflichtig) + Dividenden 2''100 = 2''350; Kanton abzüglich Vermögensverwaltungskosten pauschal (Code
    148) 2 ‰ × Depot 95''000 = 190 (Sparkonto zählt nicht) → 2''160. Bund: belegt nur effektive Depot-/Safegebühren (bund-wl-2a-2025__c0056) → 2''350; 2''160 nur
    mit ausdrücklichem Vorbehalt ebenfalls zulässig (dann Bund-Folgewerte je −190).'
  ziffer: 4 (Code 150) – Formular 2 Ziff. 9
- bezeichnung: Verrechnungssteueranspruch (Rückerstattung, kein Einkommen/Abzug)
  bund: null
  fundstellen:
  - tg-form-02-2025__c0006
  - tg-wl-2025__c0167
  - bund-vstg__art-13
  kanton: 822.5
  rechnung: 35 % × 2'350 = 822.50.
  ziffer: Formular 2 Ziff. 10
- bezeichnung: Zwischentotal der Einkünfte
  bund: 40150
  fundstellen:
  - tg-form-01-2025__c0008
  kanton: 39960
  rechnung: 27'000 + 10'800 + 2'160 = 39'960; Bund 27'000 + 10'800 + 2'350 = 40'150.
  ziffer: 6 (Code 175)
- bezeichnung: Steuerbarer Eigenmietwert EFH (Mietwert 20'400)
  bund: 16320
  fundstellen:
  - tg-form-07-2025__c0002
  - tg-wl-2025__c0225
  - tg-wl-2025__c0242
  - tg-wl-2025__c0243
  - tg-stg__par-23
  - tg-stp-23-1__c0005
  - bund-dbg-2025__art-21
  kanton: 12240
  rechnung: Selbstnutzungsabzug Kanton 40 % × 20'400 = 8'160 → 12'240; Bund 20 % × 20'400 = 4'080 → 16'320.
  ziffer: Formular 7 Liegenschaft 1 – Selbstnutzungsabzug / steuerbarer Eigenmietwert
- bezeichnung: Liegenschaftsunterhalt effektiv
  bund: 7400
  fundstellen:
  - tg-form-08-2025__c0002
  - tg-form-08-2025__c0003
  - tg-wl-2025__c0227
  - tg-wl-2025__c0228
  - tg-wl-2025__c0233
  - tg-wl-2025__c0238
  - tg-stv__par-9
  - bund-dbg-2025__art-32-t1
  - bund-dbg-2025__art-34
  - bund-lkv__art-5
  kanton: 7400
  rechnung: 'Abziehbar 6''400 + 520 + 480 = 7''400. FALLE Wintergarten 31''000 = Anbau/wertvermehrend → Spalte Anlagekosten, nicht abziehbar. Vergleich Pauschale
    20 % (Gebäude > 10 Jahre) vom steuerbaren Eigenmietwert: Kanton 2''448, Bund 3''264 → effektive Kosten höher, «Effektiv» ankreuzen.'
  ziffer: Formular 8 → Formular 7 «Unterhalts-/Betriebskosten» (effektiv)
- bezeichnung: Einkünfte aus Liegenschaften (Nettoerfolg)
  bund: 8920
  fundstellen:
  - tg-form-07-2025__c0003
  - tg-wl-2025__c0244
  - tg-wl-2025__c0245
  - tg-form-01-2025__c0009
  kanton: 4840
  rechnung: 'Nettoerfolg je Spalte separat: Kanton 12''240 − 7''400 = 4''840; Bund 16''320 − 7''400 = 8''920.'
  ziffer: 8.1 (Code 180)
- bezeichnung: Total der Einkünfte
  bund: 49070
  fundstellen:
  - tg-form-01-2025__c0009
  kanton: 44800
  rechnung: 39'960 + 4'840 = 44'800; 40'150 + 8'920 = 49'070.
  ziffer: 9 (Code 198)
- bezeichnung: Schuldzinsen
  bund: 3150
  fundstellen:
  - tg-form-04-1-2025__c0002
  - tg-wl-2025__c0173
  - tg-stg__par-34-t2
  - bund-dbg-2025__art-33-t1
  kanton: 3150
  rechnung: Hypothekarzinsen 3'150 (unter Vermögensertrag + 50'000).
  ziffer: 11 (Code 290) – via Formular 4.1
- bezeichnung: Versicherungsprämien und Zinsen von Sparkapitalien
  bund: 2700
  fundstellen:
  - tg-form-05-2-2025__c0001
  - tg-form-05-2-2025__c0002
  - tg-form-05-2-2025__c0003
  - tg-wl-2025__c0212
  - tg-stg__par-34-t3
  - bund-dbg-2025__art-33-t2
  - bund-dbg-2025__art-33-t5
  - bund-rs-2-210__c0006
  kanton: 3500
  rechnung: 'A (324): Prämien 6''240 + Sparzins 250 = 6''490. B Staat alleinstehend 3''500; Bund ohne Beiträge an Säule 2/3a 2''700 (statt 1''800). Abzug = niedrigerer
    Betrag.'
  ziffer: 14 (Code 330) – via Formular 5.2 (Codes 324/328)
- bezeichnung: Total Abzüge
  bund: 5850
  fundstellen:
  - tg-form-01-2025__c0011
  kanton: 6650
  rechnung: 3'150 + 3'500 = 6'650; 3'150 + 2'700 = 5'850.
  ziffer: 19 (Code 360)
- bezeichnung: Nettoeinkommen
  bund: 43220
  fundstellen:
  - tg-form-01-2025__c0012
  kanton: 38150
  rechnung: 44'800 − 6'650 = 38'150; 49'070 − 5'850 = 43'220.
  ziffer: 22 (Code 362)
- bezeichnung: Krankheits- und Unfallkosten
  bund: 4379
  fundstellen:
  - tg-form-05-1-2025__c0001
  - tg-form-05-1-2025__c0002
  - tg-form-05-1-2025__c0004
  - tg-wl-2025__c0197
  - tg-wl-2025__c0203
  - tg-stg__par-34-t3
  - bund-dbg-2025__art-33-t3
  kanton: 4632
  rechnung: 'A: Kostenbeteiligung 1''000 + Zahnarzt 4''440 + Brille 1''400 = 6''840; B Vergütung Dritter −300 → 6''540. Selbstbehalt 5 % von Ziff. 22: Staat 1''907.50
    → 4''632 (4''633 bzw. Rappen ebenfalls korrekt); Bund 2''161 → 4''379. Hinweis: § 34 Ziff. 10 StG nennt «Reineinkommen», Formular 5.1/WL rechnen mit Ziff. 22
    – Formular angewendet.'
  ziffer: 23.1 (Code 364) – via Formular 5.1
- bezeichnung: Freiwillige Zuwendungen
  bund: 550
  fundstellen:
  - tg-form-06-2025__c0002
  - tg-wl-2025__c0218
  - tg-stg__par-34-t4
  - bund-dbg-2025__art-33a
  kanton: 350
  rechnung: 'Total 300 + 250 = 550. Kanton: Selbstbehalt 200 → 350 (Max. 8''000, da Nettoeinkommen 38''150 bis 40''000). Bund: ab 100 voll abziehbar, 550 (unter 20
    % von 43''220).'
  ziffer: 23.2 (Code 366) – via Formular 6
- bezeichnung: Reineinkommen
  bund: 38291
  fundstellen:
  - tg-form-01-2025__c0012
  kanton: 33168
  rechnung: 38'150 − 4'632 − 350 = 33'168 (± 1 Rundung); 43'220 − 4'379 − 550 = 38'291.
  ziffer: 24 (Code 372)
- bezeichnung: Abzug für AHV-Rentner/Verwitwete (nur Kanton)
  bund: null
  fundstellen:
  - tg-form-01-2025__c0013
  - tg-wl-2025__c0116
  - tg-wl-2025__c0117
  - tg-vakp__par-1
  - tg-wl-2025__c0007
  kanton: 1000
  rechnung: 'Reineinkommen Ziff. 24 (Kanton) 33''168 → Stufe Alleinstehende 32''900–33''899 = 1''000 (4''200 − 16 × 200 je volle 1''000 über 16''900). Bund: kein
    Abzug.'
  ziffer: 25.3 (Code 388)
- bezeichnung: Steuerbares Einkommen
  bund: 38291
  fundstellen:
  - tg-form-01-2025__c0013
  kanton: 32168
  rechnung: 33'168 − 1'000 = 32'168 (± 1 Rundung); Bund keine Sozialabzüge → 38'291.
  ziffer: 26 (Code 398)
- bezeichnung: Wertschriften und Guthaben
  bund: null
  fundstellen:
  - tg-form-01-2025__c0014
  - tg-form-02-2025__c0006
  kanton: 143000
  rechnung: 48'000 + 95'000 = 143'000.
  ziffer: 30.1 (Code 410)
- bezeichnung: Liegenschaften (Steuerwert)
  bund: null
  fundstellen:
  - tg-form-01-2025__c0015
  - tg-form-07-2025__c0003
  - tg-wl-2025__c0239
  kanton: 410000
  rechnung: Steuerwert gem. Schätzung 410'000 (Formular 7 Total Steuerwerte).
  ziffer: 31 (Code 430)
- bezeichnung: Total der Vermögenswerte
  bund: null
  fundstellen:
  - tg-form-01-2025__c0015
  kanton: 553000
  rechnung: 143'000 + 410'000 = 553'000.
  ziffer: 33 (Code 464)
- bezeichnung: Schulden
  bund: null
  fundstellen:
  - tg-form-01-2025__c0015
  - tg-form-04-1-2025__c0002
  kanton: 180000
  rechnung: Hypothek 180'000 (Formular 4.1).
  ziffer: 34 (Code 466)
- bezeichnung: Reinvermögen
  bund: null
  fundstellen:
  - tg-form-01-2025__c0015
  kanton: 373000
  rechnung: 553'000 − 180'000 = 373'000.
  ziffer: 35 (Code 468)
- bezeichnung: Steuerfreier Betrag alleinstehend/verwitwet
  bund: null
  fundstellen:
  - tg-form-01-2025__c0016
  - tg-wl-2025__c0128
  kanton: 100000
  rechnung: Fix 100'000.
  ziffer: 36.2 (Code 472)
- bezeichnung: Steuerbares Vermögen gesamt
  bund: null
  fundstellen:
  - tg-form-01-2025__c0016
  kanton: 273000
  rechnung: 373'000 − 100'000 = 273'000.
  ziffer: 37 (Code 498)


**Antwort des Agenten** (127.6 s · Tools: 35 Aufrufe read, steuerwiki__formular, steuerwiki__position, steuerwiki__wert, steuerwiki__zeige, steuerwiki__suche, steuerwiki__beleg, steuerwiki__rechne):

> Ich prüfe noch die offenen Punkte (Gartenpflege, Vermögensverwaltungskosten Bund, Tabelle Abzug 25.3) und rechne danach alles durch.
> 
> **TG · Steuerjahr 2025 · Alleinstehende verwitwete Rentnerin, Frauenfeld**
> Formular: Steuererklärung 2025 TG (Formular 1) mit Hilfsblättern. Die linke Spalte gilt für Staats- und Gemeindesteuern (K), die rechte für die direkte Bundessteuer (B). Alle Beträge sind in ganzen Franken, mit `rechne` gerechnet. Status überall ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen), ausser wo anders vermerkt.
> 
> ## 1. Einkünfte
> 
> | Ziffer | Code | Position | Kanton | Bund | Beleg | Rechenweg / Regel | Fundstelle |
> |---|---|---|---|---|---|---|---|
> | 3.1 | 130 | AHV-Rente | 27'000 | 27'000 | AHV-Bescheinigung | 12 × 2'250, 100 % steuerbar | tg-wl-2025__c0076 |
> | 3.2 | 132 | PK-Rente (Bruttobetrag 10'800, **100 %**) | 10'800 | 10'800 | PK-Bescheinigung | 12 × 900. Rentenbeginn 2020, also kein 80 %-Übergangsrecht (gilt nur bei Rentenbeginn vor 2002) | tg-wl-2025__c0077 |
> | 4 | 150 | Wertschriften- und Zinserträge (Übertrag Form. 2) | 2'160 | 2'350 | TKB-Steuerauszug | Brutto 250 + 2'100 = 2'350. Kanton minus Vermögensverwaltungskosten 190, siehe 2a | tg-wl-2025__c0153 |
> | 6 / 7 | 175 | Zwischentotal Einkünfte und Übertrag | 40'… s. u. | | | | |
> | 8.1 | 180 | Einkünfte aus Liegenschaften (Form. 7) | 4'840 | 8'920 | Schätzung, Handwerkerrechnungen | siehe 2b | tg-wl-2025__c0225 |
> | 9 | 198 | **Total der Einkünfte** → Ziff. 20 | **44'800** | **49'070** | | K: 27'000 + 10'800 + 2'160 + 4'840 · B: 27'000 + 10'800 + 2'350 + 8'920 | |
> 
> Ziff. 6/7 (Code 175): Zwischentotal und Übertrag ohne Liegenschaften. K 40'… ist hier ein Tippfehler; richtig sind K 39'960 und B 40'150. Ziff. 8.1 kommt danach dazu.
> 
> **Nicht zutreffend:** Ziff. 1, 2, 3.3–3.4, 5.1–5.5 (Erwerb, Taggelder, Unterhaltsbeiträge und Ähnliches gibt es nicht).
> 
> ### 2a. Form. 2, Wertschriftenverzeichnis
> - **Sparkonto TKB:** Steuerwert 48'000 (Sp. 7). Bruttozins 250 mit Verrechnungssteuer (VSt) gehört in **Sp. 8 (A)**, weil der Zins über Fr. 200 liegt.
> - **Depot Schweizer Aktien:** Steuerwert 95'000 (Sp. 7). Bruttodividenden 2'100 in **Sp. 8 (A)**, in Franken und Rappen.
> - **Total Sp. 8:** 2'350.00.
> - **Ziff. 10, VSt-Anspruch:** 35 % × 2'350 = **822.50**. Das entspricht den Abzügen im Steuerauszug (87.50 + 735.00). Es ist eine Rückerstattung, weder Einkommen noch Abzug.
> - **Vermögensverwaltungskosten (Code 148), nur Kanton:** 2 ‰ × 95'000 = **190**. Das Sparkonto zählt nicht zur Bemessung. Die Kosten werden vom Bruttoertrag abgezogen. Quelle: tg-wl-2025__c0159.
> - **Bund:** Eine Bundespauschale ist im Wiki **nicht belegt**. Ich habe 0 eingesetzt (Bund 2'350). Weist der Steuerauszug effektive Depotgebühren aus, gehören sie in die Bundesspalte. ⚠️ Fachperson prüfen.
> 
> ### 2b. Form. 7, Liegenschaft (EFH Frauenfeld, am Wohnsitz dauernd selbstbewohnt, Baujahr 1986)
> - **Mietwert (indexiert):** 20'400.
> - **Selbstnutzungsabzug:** K 40 % = 8'160, B 20 % = 4'080. Der steuerbare Eigenmietwert beträgt K **12'240** und B **16'320**.
> - **Unterhalt:** effektiv gegen Pauschale (Gebäude über 10 Jahre alt, 20 % vom steuerbaren Eigenmietwert, Wahl je Periode). Die Pauschale wäre K 2'448 und B 3'264. Effektiv ist günstiger:
> 
> | Rechnung (Form. 8) | Betrag |
> |---|---|
> | Malerarbeiten Innenrenovation (Ersatzanstrich), Unterhalt | 6'400 |
> | Gebäudeversicherungsprämie (Besitzesabgabe) | 520 |
> | Baumschnitt/Gartenpflege (Pflege von Bäumen, abziehbar) | 480 |
> | **Total Unterhalt effektiv** | **7'400** |
> | Wintergarten-Anbau, **nicht abziehbar** (Spalte «Anlagekosten/Mehrwert») | 31'000 |
> 
> - **Nettoerfolg (Code 180):** K 12'240 − 7'400 = **4'840** · B 16'320 − 7'400 = **8'920**.
> - **Beilagen:** Rechnungskopien für Einzelbeträge ab Fr. 1'000 (Maler 6'400, Wintergarten 31'000). Quellen: tg-wl-2025__c0238, c0234, c0228, tg-stp-34-1__c0014 und c0016.
> 
> ## 2c. Vermögen (Form. 1, Seite 4)
> - **Ziff. 30.1, Code 410:** Sparkonto 48'000 + Depot 95'000 = **143'000**.
> - **Ziff. 31, Code 430:** Liegenschaft, Steuerwert **410'000**.
> - **Ziff. 33, Code 464:** Total Vermögenswerte **553'000**.
> - **Ziff. 34, Code 466:** Schulden (Hypothek) **180'000**, Übertrag aus Form. 4.1.
> - **Ziff. 35, Code 468:** Reinvermögen 553'000 − 180'000 = **373'000**.
> - **Ziff. 36.2, Code 472:** steuerfreier Abzug für Alleinstehende **100'000**.
> - **Ziff. 37, Code 498:** **steuerbares Vermögen 273'000.**
> - Es gibt kein Bundesvermögen, die Bundesspalte entfällt.
> 
> ## 3. Abzüge
> 
> | Ziffer | Code | Position | Kanton | Bund | Rechenweg / Regel | Fundstelle |
> |---|---|---|---|---|---|---|
> | 11 | 290 (Form. 4.1 C) | Schuldzinsen | 3'150 | 3'150 | Hypothekarzinsen 2025. Limite: Vermögensertrag + 50'000, also eingehalten. Gläubigerin mit Adresse und Zinssatz (rund 1.75 % = 3'150 / 180'000) angeben. Schuld 180'000 in Code 455/466 | tg-wl-2025__c0173 |
> | 14 | 330 (Form. 5.2 C) | Versicherungsprämien und Sparzinsen | **3'500** | **2'700** | A5/Code 324: KK-Prämie netto 6'240 (keine Verbilligung) + Sparzinsen 250 = 6'490. Abzug = min(6'490; Limite). Limite alleinstehend K 3'500. Bund 2'700 statt 1'800, weil keine Beiträge an 2. Säule oder 3a | tg-form-05-2-2025__c0002 |
> | 19 | 360 | **Total Abzüge** | **6'650** | **5'850** | K: 3'150 + 3'500 · B: 3'150 + 2'700 | |
> 
> **Nicht zutreffend:** Ziff. 10, 12, 13 (keine 2. Säule oder 3a), 15.1–15.6, 16, 17 und 18. Der AHV-Beitrag für Nichterwerbstätige (15.1) fällt bei einer Altersrentnerin nicht an. Das habe ich nicht aus einer Wiki-Fundstelle geprüft.
> 
> ## 4. Einkommensberechnung
> 
> | Ziffer | Code | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 20 | – | Total Einkünfte | 44'800 | 49'070 | |
> | 21 | – | Total Abzüge | 6'650 | 5'850 | |
> | 22 | 362 | **Nettoeinkommen** | **38'150** | **43'220** | |
> | 23.1 | 364 | Krankheits- und Unfallkosten (Form. 5.1 D) | 4'633 | 4'379 | A = 1'000 + 4'440 + 1'400 = 6'840. B (Zusatzversicherung) 300. A − B = 6'540. Selbstbehalt 5 % von Ziff. 22: K 1'907.50, B 2'161. K 6'540 − 1'907.50 = 4'632.50, auf 4'633 gerundet |
> | 23.2 | 366 | Freiwillige Zuwendungen (Form. 6) | 350 | 550 | Krebsliga TG 300 + Pro Senectute TG 250 = 550. Kanton: 550 − 200 Selbstbehalt = 350. Bund: ohne Selbstbehalt, weil das Total ≥ 100 ist. Maximum 20 % von Ziff. 22: K 7'630, B 8'644. Das Kantonsmaximum beträgt 8'000 (Nettoeinkommen bis 40'000), es ist nicht erreicht |
> | 24 | 372 | **Reineinkommen** | **33'167** | **38'291** | K 38'150 − 4'633 − 350 · B 43'220 − 4'379 − 550 |
> | 25.3 | 388 | Abzug AHV-Rentnerin/verwitwet (nur Kanton) | **1'000** | – | 4'200 − 200 × 16 volle Fr. 1'000 über 16'900 = 1'000. Die Tabelle in der Wegleitung bestätigt die Staffelung (c0116). Der Bund kennt keinen Abzug |
> | 26 | 398 | **Steuerbares Einkommen** | **32'167** | **38'291** | K 33'167 − 1'000 |
> 
> **Nicht zutreffend:** Ziff. 23.3, 25.1, 25.2, 25.4, 28.1 und 28.2 (keine Kinder, keine unterstützten Personen, nicht gemeinsam besteuert).
> 
> **Zur Krankheitskosten-Zeile 23.1:**
> - Zahnarzt 4'440 und Brille 1'400 (mit augenärztlicher Verordnung) sind abziehbar.
> - Die Krankenkassenprämien (6'240) gehören nicht hierher, sondern in Ziff. 14.
> - Die Zusatzversicherung hat 300 vergütet, das ist Form. 5.1 Teil B.
> - Die Rundung des Kantonsbetrags (4'632.50) kann um 1 Franken abweichen.
> 
> ## 5. Nicht zu deklarieren oder nicht abziehbar
> 
> | Beleg | Behandlung | Grund / Fundstelle |
> |---|---|---|
> | Wintergarten-Anbau 31'000 | **kein Unterhaltsabzug** | Neu-, Um- und Anbauten sind Investitionen (tg-stp-34-1__c0016). Nur in Form. 8 Spalte «Anlagekosten/Mehrwert» erfassen |
> | Hausratversicherung 380 | nicht abziehbar, nicht einreichen | Beleg «einreichen: nein» (tg-wl-2025__c0227). Sachversicherung, kein Versicherungsabzug |
> | Serafe 335 | nicht abziehbar | privater Lebensaufwand (Art. 34 lit. a DBG). Ich habe dafür keine eigene TG-Fundstelle geprüft |
> | Handyrechnung 2025 | nicht abziehbar | privater Lebensaufwand, keine Erwerbstätigkeit |
> | Krankenkassenprämien in Krankheitskosten | nicht doppelt | nur in Ziff. 14 |
> | Verrechnungssteuer 822.50 | weder Einkommen noch Abzug | Rückerstattung über Form. 2 Ziff. 10 |
> | Hypothek 180'000 | kein Einkommen | Schuld in Ziff. 34. Amortisationen wären keine Schuldzinsen |
> | Mietwert und Selbstnutzung | nur als Eigenmietwert | kein separater Wohnkostenabzug |
> 
> ## Fehlende Belege und Werte zu prüfen
> 1. **Handyrechnung 2025** liegt ohne Betrag vor. Sie ist nicht relevant, es muss nichts erfasst werden.
> 2. **Steuerwert Liegenschaft 410'000:** Der Wintergarten wurde 2025 gebaut. Die Schätzung ist möglicherweise nicht angepasst. Prüfen, ob eine Neuschätzung kommt (Steuerwert und Mietwert). Eine Aussage dazu ist nicht belegt.
> 3. **Baumschnitt/Gartenpflege 480:** nur abziehbar, soweit es um mehrjährige Pflanzen und Bäume geht. Rasen, Gemüse oder Beeren sind nicht abziehbar (c0228). Aufteilung der Rechnung prüfen.
> 4. **Spenden:** Krebsliga TG und Pro Senectute TG gegen die Liste der steuerbefreiten Institutionen der Steuerverwaltung prüfen. Quittungen unter Fr. 1'000 nur auf Verlangen beilegen.
> 5. **Krankheitskosten:** Zahnarztrechnung und Brille müssen vollständig selbst getragen sein. Leistungsabrechnung (Franchise/Selbstbehalt 1'000) mit der Steuererklärung einreichen.
> 6. **Vermögensverwaltungskosten Bund:** siehe 2a. Im Wiki ist keine Bundespauschale belegt.
> 
> ## Hinweise für die Fachperson
> - Bundesteil Eigenmietwert: Das Wiki hält für den Bund 20 % Selbstnutzungsabzug (tg-wl-2025__c0225). Der Eintrag in `position Form. 7` («Bund nicht anwendbar») widerspricht dem. Ich habe 20 % verwendet.
> - Plausibilität: Das Bundeseinkommen liegt über dem Kantonseinkommen, weil der Abzug 25.3 nur kantonal gilt, der Eigenmietwert-Abzug beim Bund tiefer ist und keine Kantonspauschale für Vermögensverwaltungskosten besteht. Das ist erklärbar.
> - Die fachliche Beurteilung bleibt bei der Fachperson.

## f-ar

**Frage:** Steuerjahr 2025, Kanton AR. Mandant/Haushalt: Ehepaar in Herisau AR (Mieter), beide unselbständig erwerbstätig mit Pensionskasse. Person 1 (Polymechaniker, 100 %), Person 2 (Pflegeassistentin in Tagesschicht, 80 %, Arbeitsort St. Gallen). Kinder im Haushalt: Lea (geb. 14.03.2021, Kita) und Jonas (geb. 02.09.2009, Kantonsschule).

Belege:
- Lohnausweis 2025 Person 1: Ziff. 8 Bruttolohn 98'000; Ziff. 9 AHV/IV/EO/ALV/NBUV 6'860; Ziff. 10.1 BVG ordentlich 5'840; Ziff. 10.2 0; Ziff. 11 Nettolohn 85'300. Feld F ANGEKREUZT (unentgeltlicher Werkbus des Arbeitgebers), Feld G ANGEKREUZT (Personalkantine). 220 Arbeitstage.
- Lohnausweis 2025 Person 2: Ziff. 8 Bruttolohn 82'000 (inkl. Kinder- und Ausbildungszulagen); Ziff. 9 5'740; Ziff. 10.1 BVG ordentlich 4'060; Ziff. 10.2 BVG-Einkauf 4'000; Ziff. 11 Nettolohn 68'200. Felder F und G nicht angekreuzt; 80 %, 176 Arbeitstage, Mittagessen auswärts.
- Pensionskasse Person 2: Bestätigung Einkauf 2025 4'000, «bezahlt via Lohnabzug».
- Jahresabonnement öV (Ostwind) Herisau–St. Gallen Person 2: 1'260.
- Krankenkassen-Prämienbescheinigung 2025 Familie (Grund- und Zusatzversicherung): 13'900; keine Prämienverbilligung.
- Säule-3a-Bescheinigungen: Person 1 7'258; Person 2 5'000.
- Kita-Rechnungen 2025 für Lea: total 14'400, davon Mittagessen 1'800; kantonaler Betreuungsbeitrag (Gutschrift) 2'400.
- Bank-Steuerauszug per 31.12.2025: Konten total 54'000, Bruttozinsen 160 (ohne VSt-Abzug); Schweizer Aktien Steuerwert 38'000, Bruttodividenden 1'250 (VSt 437.50 abgezogen).
- Spendenquittung Krebsliga Ostschweiz 300; Rechnung Jahresbeitrag Turnverein (Mitgliederbeitrag) 120.
- Schlussrechnung Staats-/Gemeinde- und Bundessteuer 2024, bezahlt 9'870; Handy-Abo 2025 960.

Auftrag: Erstelle die Ausfüllhilfe (alle relevanten Positionen mit Ziffer/Code, Beträge Staat und Bund, Rechenweg, Fundstellen) und nenne, was nicht zu deklarieren ist.

**Soll (Referenz):** nicht_deklarieren:
- 'Fahrkosten Person 1: Feld F angekreuzt → kein Abzug (ar-wl-2025__c0075).'
- PK-Einkauf Person 2 von 4'000 nicht nochmals unter 13.2 – bereits im Nettolohn (ar-wl-2025__c0035).
- Kita-Mittagessen 1'800 und kantonaler Betreuungsbeitrag 2'400 sind von den Betreuungskosten abzuziehen (ar-wl-2025__c0091).
- 'Mitgliederbeitrag Turnverein 120: keine abziehbare Zuwendung (ar-wl-2025__c0102).'
- 'Steuerrechnung 2024 von 9''870: Einkommens- und Vermögenssteuern nicht abziehbar (ar-stg__art-37, bund-dbg-2025__art-34).'
- 'Handy-Abo 960: private Lebenshaltung (ar-stg__art-37, bund-dbg-2025__art-34).'
positionen:
- bezeichnung: Haupterwerb Person 1 – Nettolohn
  bund: 85300
  fundstellen:
  - ar-wl-2025__c0026
  - ar-wl-2025__c0035
  - ar-wl-2025__c0179
  kanton: 85300
  rechnung: '98''000 − 6''860 − 5''840 = 85''300. Hinweis: Formular 1 AR hat eine Spalte; DBSt-Abweichungen nimmt die Steuerverwaltung automatisch vor.'
  ziffer: '1.1 Person 1 (Code 100 – nicht eindeutig: AR-Hauptformular nicht in den Quellen, Code nur aus verzerrtem WL-Raster)'
- bezeichnung: Haupterwerb Person 2 – Nettolohn
  bund: 68200
  fundstellen:
  - ar-wl-2025__c0026
  - ar-wl-2025__c0035
  kanton: 68200
  rechnung: 82'000 − 5'740 − 4'060 − 4'000 (BVG-Einkauf via Lohn) = 68'200 = Lohnausweis Ziff. 11.
  ziffer: 1.1 Person 2 (Code 102 – nicht eindeutig, siehe oben)
- bezeichnung: Erträge aus Wertschriften und Guthaben
  bund: 1410
  fundstellen:
  - ar-form-02-2025__c0007
  - ar-wl-2025__c0136
  - bund-vstg__art-5-t1
  kanton: 1410
  rechnung: 'Spalte A: Dividenden 1''250; Spalte B: Kontozinsen 160 (bis 200 verrechnungssteuerfrei); Total 1''410.'
  ziffer: 4.1 (Übertrag Formular 2)
- bezeichnung: VSt-Rückerstattung (kein Einkommen/Abzug)
  bund: null
  fundstellen:
  - ar-wl-2025__c0131
  - bund-vstg__art-13
  kanton: 437.5
  rechnung: 35 % × Spalte A 1'250 = 437.50.
  ziffer: Formular 2 – Verrechnungssteueranspruch
- bezeichnung: Total der Einkünfte
  bund: 154910
  fundstellen:
  - ar-wl-2025__c0030
  kanton: 154910
  rechnung: 85'300 + 68'200 + 1'410 = 154'910.
  ziffer: '7'
- bezeichnung: Fahrkosten Person 1
  bund: 0
  fundstellen:
  - ar-form-04-2025__c0001
  - ar-form-04-2025__c0002
  - ar-wl-2025__c0075
  - bund-bkv-2025__art-1
  kanton: 0
  rechnung: 'FALLE: Lohnausweis Feld F angekreuzt (unentgeltliche Beförderung durch Arbeitgeber) → kein Fahrkostenabzug.'
  ziffer: Formular 4 Person 1, Ziff. 1 (Codes 400–405)
- bezeichnung: Verpflegung verbilligt (Kantine, Feld G)
  bund: 1600
  fundstellen:
  - ar-form-04-2025__c0003
  - ar-wl-2025__c0076
  - bund-bkv-2025__art-6-t1
  - bund-bkv-2025__anhang-1
  kanton: 1600
  rechnung: 220 × 7.50 = 1'650 → Max. 1'600.
  ziffer: Formular 4 Person 1, Ziff. 2.2 (Code 410)
- bezeichnung: Übrige Berufskosten pauschal
  bund: 2559
  fundstellen:
  - ar-form-04-2025__c0003
  - ar-wl-2025__c0078
  - ar-stv__art-18
  - bund-bkv-2025__anhang-1
  kanton: 2400
  rechnung: 'Kanton: 700 + 10 % × 85''300 = 9''230 → Max. 2''400. Bund: 3 % × 85''300 = 2''559.'
  ziffer: Formular 4 Person 1, Ziff. 3.1 (Code 416)
- bezeichnung: Berufskosten Person 1 total
  bund: 4159
  fundstellen:
  - ar-form-04-2025__c0004
  kanton: 4000
  rechnung: Kanton 0 + 1'600 + 2'400 = 4'000; Bund 0 + 1'600 + 2'559 = 4'159.
  ziffer: 10.1 (Code 438)
- bezeichnung: Fahrkosten öV Person 2
  bund: 1260
  fundstellen:
  - ar-form-04-2025__c0005
  - ar-form-04-2025__c0006
  - ar-wl-2025__c0074
  - ar-stg__art-29
  - bund-dbg-2025__art-26
  kanton: 1260
  rechnung: Abo 1'260 – unter Pendlerabzug Kanton 6'000 und Bund 3'300.
  ziffer: Formular 4 Person 2, Ziff. 1.1 (Code 450) / Zwischentotal (Code 455)
- bezeichnung: Mehrkosten auswärtige Verpflegung
  bund: 2640
  fundstellen:
  - ar-form-04-2025__c0007
  - ar-wl-2025__c0076
  - bund-bkv-2025__anhang-1
  kanton: 2640
  rechnung: 176 × 15 = 2'640 (unter Max. 3'200).
  ziffer: Formular 4 Person 2, Ziff. 2.1 (Code 458)
- bezeichnung: Übrige Berufskosten pauschal
  bund: 2046
  fundstellen:
  - ar-form-04-2025__c0007
  - ar-wl-2025__c0078
  - ar-stv__art-18
  - bund-bkv-2025__anhang-1
  kanton: 2400
  rechnung: 'Kanton: 700 + 10 % × 68''200 = 7''520 → Max. 2''400. Bund: 3 % × 68''200 = 2''046.'
  ziffer: Formular 4 Person 2, Ziff. 3.1 (Code 466)
- bezeichnung: Berufskosten Person 2 total
  bund: 5946
  fundstellen:
  - ar-form-04-2025__c0008
  kanton: 6300
  rechnung: Kanton 1'260 + 2'640 + 2'400 = 6'300; Bund 1'260 + 2'640 + 2'046 = 5'946.
  ziffer: 10.2 (Code 488)
- bezeichnung: Säule 3a Person 1
  bund: 7258
  fundstellen:
  - ar-wl-2025__c0083
  - bund-bvv3__art-7
  - bund-bsv-masszahlen-2025-2026__c0003
  kanton: 7258
  rechnung: Mit 2. Säule max. 7'258; bezahlt 7'258.
  ziffer: 13.1 Person 1 (Code nicht belegt)
- bezeichnung: Säule 3a Person 2
  bund: 5000
  fundstellen:
  - ar-wl-2025__c0083
  - bund-bvv3__art-7
  - bund-bsv-masszahlen-2025-2026__c0003
  kanton: 5000
  rechnung: Bezahlt 5'000 (unter Max. 7'258).
  ziffer: 13.1 Person 2 (Code nicht belegt)
- bezeichnung: Säule 2 – Einkaufsbeitrag
  bund: 0
  fundstellen:
  - ar-wl-2025__c0035
  - ar-wl-2025__c0084
  - bund-dbg-2025__art-33-t2
  kanton: 0
  rechnung: 'FALLE: Einkauf 4''000 wurde über den Lohn abgezogen (Lohnausweis Ziff. 10.2) und ist im Nettolohn bereits berücksichtigt → kein zusätzlicher Abzug (sonst
    Doppelabzug).'
  ziffer: 13.2 Person 2 (Code nicht belegt)
- bezeichnung: Versicherungsprämien und Sparzinsen
  bund: 5100
  fundstellen:
  - ar-form-06-2025__c0001
  - ar-form-06-2025__c0002
  - ar-wl-2025__c0085
  - ar-stg__art-35-t2
  - bund-dbg-2025__art-33-t2
  - bund-dbg-2025__art-33-t5
  kanton: 7400
  rechnung: 'A: Prämien 13''900 + Sparzinsen 160 = 14''060. B Kanton: 5''400 + 2 × 1''000 = 7''400. Bund: 3''700 + 2 × 700 = 5''100. Abzug = niedrigerer Betrag.'
  ziffer: 14 (Code 600) – via Formular 6
- bezeichnung: Verwaltungskosten Wertschriften (Pauschale auf Antrag)
  bund: 0
  fundstellen:
  - ar-wl-2025__c0003
  - ar-wl-2025__c0087
  - ar-wl-2025__c0088
  - ar-wl-2025__c0179
  - bund-wl-2a-2025__c0056
  kanton: 276
  rechnung: 'Basis = Total der Spalte Steuerwerte Formular 2 = 92''000 (Konten 54''000 + Aktien 38''000; ausgenommen wären nur eigene Unternehmensaktien, private
    Darlehen, geschäftliche Bankkonti) × 3 ‰ = 276 (unter Max. 6''000). Bund: keine Bundesspalte, die Steuerverwaltung passt an; belegt sind beim Bund nur effektive
    Depot-/Safegebühren (bund-wl-2a-2025__c0056) → 0. 114 (nur Aktien) ist eine zu enge Basis.'
  ziffer: '16.1'
- bezeichnung: Kinderbetreuungskosten Lea
  bund: 10200
  fundstellen:
  - ar-form-10-2025__c0001
  - ar-form-10-2025__c0002
  - ar-wl-2025__c0089
  - ar-wl-2025__c0091
  - ar-stg__art-35-t4
  - bund-dbg-2025__art-33-t7
  - bund-dbg-2025__art-34
  kanton: 10200
  rechnung: 'FALLE: 14''400 − Mittagessen 1''800 (Lebenshaltung) − kantonaler Beitrag 2''400 = 10''200; unter Max. Kanton 25''000 / Bund 25''800.'
  ziffer: 16.2 (Formular 10)
- bezeichnung: Zweiverdienerabzug
  bund: 14100
  fundstellen:
  - ar-wl-2025__c0004
  - ar-wl-2025__c0096
  - ar-wl-2025__c0097
  - ar-stg__art-35-t3
  - ar-stg-anhang-kp__c0001
  - bund-dbg-2025__art-33-t6
  kanton: 5200
  rechnung: 'Niedrigeres Erwerbseinkommen = Person 2. Kanton: 68''200 − 6''300 − 5''000 = 56''900 → 10 % = 5''690 → Max. 5''200. Bund: 68''200 − 5''946 − 5''000 =
    57''254 → 50 % = 28''627 → Max. 14''100.'
  ziffer: 17 (Code nicht belegt)
- bezeichnung: Total der Abzüge
  bund: 51763
  fundstellen:
  - ar-wl-2025__c0065
  kanton: 45634
  rechnung: Kanton 4'000 + 6'300 + 7'258 + 5'000 + 7'400 + 276 + 10'200 + 5'200 = 45'634; Bund 4'159 + 5'946 + 7'258 + 5'000 + 5'100 + 10'200 + 14'100 = 51'763.
  ziffer: '18'
- bezeichnung: Nettoeinkommen
  bund: 103147
  fundstellen:
  - ar-wl-2025__c0099
  kanton: 109276
  rechnung: 154'910 − 45'634 = 109'276; 154'910 − 51'763 = 103'147.
  ziffer: '20'
- bezeichnung: Freiwillige Zuwendungen
  bund: 300
  fundstellen:
  - ar-form-05-2025__c0003
  - ar-wl-2025__c0102
  - ar-wl-2025__c0103
  - bund-dbg-2025__art-33a
  kanton: 300
  rechnung: Krebsliga 300 (≥ 100, unter 20 % des Nettoeinkommens). Mitgliederbeitrag Turnverein 120 ist keine Zuwendung.
  ziffer: 21.3 (Code 550 Formular 5)
- bezeichnung: Reineinkommen
  bund: 102847
  fundstellen:
  - ar-wl-2025__c0099
  kanton: 108976
  rechnung: 109'276 − 300 = 108'976; 103'147 − 300 = 102'847.
  ziffer: '22'
- bezeichnung: Kinderabzug Lea (nach Vollendung 4. Altersjahr)
  bund: 6800
  fundstellen:
  - ar-wl-2025__c0005
  - ar-wl-2025__c0104
  - ar-stg__art-38-t1
  - ar-stg-anhang-kp__c0001
  - bund-dbg-2025__art-35
  kanton: 7400
  rechnung: 'FALLE: Lea hat das 4. Altersjahr am 14.03.2025 vollendet → Stichtag 31.12.2025 Stufe 23.2 = 7''400 (nicht 23.1 = 5''300). Bund 6''800.'
  ziffer: 23.2 (Code nicht belegt)
- bezeichnung: Kinderabzug Jonas (nach Vollendung 15. Altersjahr)
  bund: 6800
  fundstellen:
  - ar-wl-2025__c0005
  - ar-stg__art-38-t1
  - ar-stg-anhang-kp__c0001
  - bund-dbg-2025__art-35
  kanton: 11600
  rechnung: Jonas 16 Jahre, Kantonsschule → Stufe 23.3 = 11'600. Bund 6'800.
  ziffer: 23.3 (Code nicht belegt)
- bezeichnung: Verheiratetenabzug Bund
  bund: 2800
  fundstellen:
  - ar-wl-2025__c0179
  - bund-dbg-2025__art-35
  - bund-rs-2-210__c0007
  kanton: null
  rechnung: 'Ehepaar in ungetrennter Ehe: 2''800 nur direkte Bundessteuer.'
  ziffer: – (nur DBSt, von Amtes wegen)
- bezeichnung: Steuerbares Einkommen gesamt
  bund: 86447
  fundstellen:
  - ar-wl-2025__c0104
  kanton: 89976
  rechnung: 108'976 − 7'400 − 11'600 = 89'976; 102'847 − 6'800 − 6'800 − 2'800 = 86'447.
  ziffer: '24'
- bezeichnung: Wertschriften und Guthaben
  bund: null
  fundstellen:
  - ar-form-02-2025__c0007
  - ar-wl-2025__c0106
  kanton: 92000
  rechnung: 54'000 + 38'000 = 92'000.
  ziffer: '30.1'
- bezeichnung: Sozialabzug Vermögen gemeinsam steuerpflichtige Ehegatten
  bund: null
  fundstellen:
  - ar-wl-2025__c0122
  kanton: 150000
  rechnung: Fix 150'000.
  ziffer: '36.2'
- bezeichnung: Sozialabzug Vermögen je minderjähriges Kind
  bund: null
  fundstellen:
  - ar-wl-2025__c0122
  kanton: 50000
  rechnung: 2 Kinder × 25'000.
  ziffer: '36.3'
- bezeichnung: Steuerbares Vermögen gesamt
  bund: null
  fundstellen:
  - ar-wl-2025__c0122
  kanton: 0
  rechnung: 92'000 − 150'000 − 50'000 < 0 → 0.
  ziffer: '37'


**Antwort des Agenten** (134.5 s · Tools: 28 Aufrufe read, steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__wert, steuerwiki__rechne):

> Ich rechne jetzt alle Beträge und Totale nach.
> 
> # Ausfüllhilfe AR · Steuerjahr 2025 (Herisau, Ehepaar, gemeinsame Veranlagung)
> 
> Das AR-Formular hat keine Bundesspalte. Die Bundesbeträge unten sind meine Parallelrechnung. Die Steuerverwaltung nimmt die Bundesanpassungen automatisch vor (ar-wl-2025__c0179). Eingetragen wird immer der Kantonswert in ganzen Franken.
> 
> Alle Positionen sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen), sofern nichts anderes steht. Die Hauptformular-Codes für Seite 3 sind im Wiki nicht verifiziert und deshalb nur als Ziffer genannt.
> 
> ## Einkünfte
> 
> | Ziffer / Code | Position | Kanton | Bund | Beleg / Rechenweg |
> |---|---|---|---|---|
> | 1.1 · 100 | Haupterwerb Person 1 | 85'300 | 85'300 | Lohnausweis Ziff. 11. 98'000 − 6'860 − 5'840 = 85'300 |
> | 1.1 · 102 | Haupterwerb Person 2 | 68'200 | 68'200 | Lohnausweis Ziff. 11. 82'000 − 5'740 − 4'060 − 4'000 = 68'200 |
> | 4.1 · 146 | Wertschriften und Guthaben (Übertrag Form. 2) | 1'410 | 1'410 | 160 Kontozins + 1'250 Dividenden, brutto |
> | **7 · 168** | **Total Einkünfte** | **154'910** | **154'910** | |
> 
> Zu Ziff. 1.1 Person 2: Die Kinder- und Ausbildungszulagen stehen schon im Bruttolohn Ziff. 8. Sie sind Lohnbestandteil (ar-wl-2025__c0032) und nichts weiter zu tun. Ziff. 3.5 ist nur für Zulagen, die eine Ausgleichskasse direkt ausbezahlt hat.
> 
> ## Form. 2 Wertschriftenverzeichnis
> 
> | Zeile | Steuerwert 31.12. | Bruttoertrag | Spalte |
> |---|---|---|---|
> | Bankkonten | 54'000 | 160 | B (Bruttozins ≤ 200, ohne VSt) |
> | Schweizer Aktien | 38'000 | 1'250 | A (VSt-pflichtig) |
> | **Total** | **92'000** → Ziff. 30.1 | **1'410** → Ziff. 4.1 | |
> 
> - **Code 999 Verrechnungssteueranspruch:** 35 % × 1'250 = **Fr. 437.50**. Das entspricht dem Abzug im Steuerauszug. Der Betrag ist eine Rückerstattung, weder Einkommen noch Abzug.
> - **Konten:** Der Zins von 160 ist trotz der 200-Fr.-Grenze steuerbar. Die Grenze betrifft nur die Verrechnungssteuer (ar-wl-2025__c0136).
> - **Steuerauszug:** Er wird vollständig beigelegt (ar-wl-2025__c0129).
> 
> ## Hilfsblatt Form. 4 Berufskosten
> 
> **Person 1 (Codes 400er-Reihe, Total 438 → Ziff. 10.1)**
> 
> | Ziffer | Kanton | Bund | Rechenweg |
> |---|---|---|---|
> | 1.1 Fahrkosten | 0 | 0 | Feld F angekreuzt (Werkbus): kein Fahrkostenabzug |
> | 2.2 Verpflegung verbilligt | 1'600 | 1'600 | Feld G angekreuzt: min(7.50 × 220 = 1'650; 1'600) |
> | 3 Übrige Berufskosten | 2'400 | 2'559 | Kanton min(700 + 10 % × 85'300; 2'400). Bund 3 % × 85'300, innerhalb 2'000–4'000 |
> | **Total** | **4'000** | **4'159** | |
> 
> **Person 2 (Codes 450er-Reihe, Total 488 → Ziff. 10.2)**
> 
> | Ziffer | Kanton | Bund | Rechenweg |
> |---|---|---|---|
> | 1.1 Fahrkosten ÖV (Code 450) | 1'260 | 1'260 | Abo Ostwind, tatsächlicher Preis. Limiten 6'000 / 3'300 nicht erreicht |
> | 2.1 Verpflegung auswärts (Code 458) | 2'640 | 2'640 | 15 × 176 Arbeitstage, max. 3'200. Tagesschicht ist keine Schichtarbeit, also kein Ziff. 2.3 |
> | 3 Übrige Berufskosten (Code 466) | 2'400 | 2'046 | Kanton min(700 + 10 % × 68'200; 2'400). Bund 3 % × 68'200 |
> | **Total** | **6'300** | **5'946** | |
> 
> Fundstellen: ar-wl-2025__c0074/0075 (Fahrkosten, Feld F), ar-form-04-2025__c0004/c0008 (Totale).
> 
> ## Abzüge
> 
> | Ziffer / Code | Position | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 10.1 · 438 | Berufskosten Person 1 | 4'000 | 4'159 | Form. 4 |
> | 10.2 · 488 | Berufskosten Person 2 | 6'300 | 5'946 | Form. 4 |
> | 13.1 | Säule 3a (Person 1 + Person 2) | 12'258 | 12'258 | 7'258 (Maximum mit 2. Säule) + 5'000. Bescheinigungen beilegen (ar-wl-2025__c0083) |
> | 13.2 | PK-Einkauf Person 2 | **0** | 0 | Die 4'000 sind via Lohnabzug schon im Nettolohn (Ziff. 10.2 Lohnausweis). Ein Abzug hier wäre doppelt. Das Wiki führt die Position als ⚠️ strittig (WL-intern widersprüchlich), die Regel gegen Doppelabzug gilt trotzdem |
> | 14 · 600 | Versicherungsprämien | 7'400 | 5'100 | Siehe Block unten |
> | 16.1 | Verwaltungskosten Wertschriften (Pauschale) | 276 | 0 ⬜ | 3 ‰ × 92'000 (ar-wl-2025__c0003). Beim Bund sind im Wiki nur effektive Verwahrungskosten belegt (bund-wl-2a-2025__c0056). Pauschale Bund nicht geprüft |
> | 16.2 · Form. 10 | Kinderbetreuung Lea | 10'200 | 10'200 | 14'400 − 1'800 Mittagessen − 2'400 Betreuungsbeitrag. Limiten 25'000 / 25'800 nicht erreicht. Lea ist unter 14, beide Eltern erwerbstätig |
> | 17 | Zweiverdienerabzug | 5'200 | 14'100 | Siehe Block unten |
> | **18** | **Total Abzüge** | **45'634** | **51'763** | |
> | **20** | **Nettoeinkommen** | **109'276** | **103'147** | 154'910 − Abzüge |
> 
> **Ziff. 14 Versicherungsprämien (Form. 6)**
> - Teil A: 13'900 Krankenkasse (Grund- und Zusatzversicherung) + 160 Sparzinsen − 0 Prämienverbilligung = 14'060.
> - Teil B Kanton: 5'400 + 2 × 1'000 = 7'400.
> - Teil B Bund (mit 2. Säule/3a): 3'700 + 2 × 700 = 5'100.
> - Der Abzug ist jeweils der niedrigere Betrag von A und B.
> - Der Kinderzuschlag gilt, weil beide Kinder einen Kinderabzug haben.
> - Fundstellen: ar-form-06-2025__c0001 und c0002.
> 
> **Ziff. 17 Zweiverdienerabzug**
> - Massgebend ist das niedrigere Erwerbseinkommen, hier Person 2.
> - Kanton: 68'200 − 6'300 − 5'000 = 56'900. 10 % davon sind 5'690, Maximum **5'200**.
> - Bund: 68'200 − 5'946 − 5'000 = 57'254. 50 % davon sind 28'627, Maximum **14'100**.
> - Der PK-Einkauf wird nicht nochmals abgezogen, weil er im Nettolohn schon enthalten ist.
> - Person 1 liegt höher (74'042 Kanton).
> - Quelle: ar-wl-2025__c0004. Der Code ist im Wiki nicht verifiziert.
> 
> ## Abzüge auf Basis Nettoeinkommen und Sozialabzüge
> 
> | Ziffer / Code | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|
> | 21.1 | Krankheitskosten | 0 | 0 | Keine Belege vorhanden |
> | 21.3 · 550 · Form. 5 | Spende Krebsliga Ostschweiz | 300 | 300 | Mindestbetrag 100 erreicht, ganze Summe abziehbar. Maximum 20 % × Nettoeinkommen (21'855 Kanton / 20'629 Bund) nicht erreicht |
> | **22** | **Reineinkommen** | **108'976** | **102'847** | Nettoeinkommen − 300 |
> | 23.2 | Kinderabzug Lea (geb. 14.03.2021, am 31.12.2025 vier Jahre alt, also nach Vollendung des 4. Altersjahrs) | 7'400 | 6'800 | Kanton ar-stg-anhang-kp__c0001 |
> | 23.3 | Kinderabzug Jonas (geb. 02.09.2009, 16 Jahre, Kantonsschule) | 11'600 | 6'800 | Kanton ar-stg-anhang-kp__c0001 |
> | 24 | Verheiratetenabzug (nur Bund) | – | 2'800 | Art. 35 DBG |
> | **24** | **Steuerbares Einkommen** | **89'976** | **86'447** | Kanton: 108'976 − 19'000. Bund: 102'847 − 13'600 − 2'800 |
> 
> Zusätzlich gilt beim Bund eine Ermässigung des Steuerbetrags von **2 × 263 = 526** (Art. 36 Abs. 2bis DBG). Sie wird automatisch berücksichtigt und nicht im Formular erfasst.
> 
> Plausibilität: Der Bund liegt 3'529 unter dem Kanton. Das erklärt sich so:
> - Der Zweiverdienerabzug ist beim Bund um 8'900 höher.
> - Die Kinderabzüge sind um 5'400 tiefer, der Versicherungsabzug um 2'300 und die Berufskosten um 159.
> - Der Verheiratetenabzug (+2'800) kommt nur beim Bund dazu.
> 
> ## Vermögen
> 
> | Ziffer / Code | Position | Betrag | Rechenweg |
> |---|---|---|---|
> | 30.1 · 300 | Wertschriften und Guthaben | 92'000 | Übertrag Form. 2: 54'000 Konten + 38'000 Aktien |
> | **33 · 322** | **Total Vermögenswerte** | **92'000** | |
> | 34.1 · 504 | Privatschulden | 0 | Keine Schulden |
> | **35 · 326** | **Reinvermögen** | **92'000** | |
> | 36.2 · 332 | Sozialabzug Ehegatten | 150'000 | In voller Höhe eintragen (ar-stg__art-51) |
> | 36.3 · 334 | Sozialabzug 2 minderjährige Kinder | 50'000 | 2 × 25'000. Beide Kinder sind minderjährig mit Kinderabzug |
> | **37 · 338** | **Steuerbares Vermögen** | **0** | 92'000 − 200'000, nicht unter 0 |
> 
> Das Vermögen wird nur im Kanton besteuert, die Bundessteuer kennt keine Vermögenssteuer. Die Guthaben der Pensionskasse und Säule 3a sind bis zur Fälligkeit kein steuerbares Vermögen und werden nicht deklariert (ar-wl-2025__c0111).
> 
> ## Nicht zu deklarieren oder nicht abziehbar
> 
> - **Handy-Abo 960:** private Lebenshaltung, kein Berufskostenabzug. Die Pauschale «übrige Berufskosten» deckt Berufsauslagen bereits ab.
> - **Turnverein-Mitgliederbeitrag 120:** Mitgliederbeiträge sind weder unter Ziff. 21.3 (ausdrücklich ausgeschlossen) noch unter 16.3 (nur politische Parteien) abziehbar.
> - **Schlussrechnung 2024 (9'870, bezahlt):** Steuern sind nicht abziehbar. Da bezahlt, auch keine Schuld unter Ziff. 34.1 und keine Schuldzinsen.
> - **PK-Einkauf Person 2 (4'000):** nicht nochmals unter Ziff. 13.2 oder 16.6 abziehen, weil er im Nettolohn enthalten ist. Die Bestätigung der Pensionskasse nur bereithalten oder beilegen.
> - **Kita-Mittagessen 1'800:** Lebenshaltungskosten, nicht abziehbar (ar-wl-2025__c0091, Art. 28a StV AR).
> - **Betreuungsbeitrag 2'400:** kein Einkommen, er mindert die abziehbaren Kosten.
> - **Krankenkassen-Zusatzversicherung:** zählt in Teil A mit. Ob sie über dem Maximum liegt, ändert nichts, weil der Deckel greift.
> - **Verrechnungssteuer 437.50:** Rückerstattung über Code 999, nicht in Einkommen oder Abzüge einrechnen.
> - **Guthaben Pensionskasse und Säule 3a:** kein Vermögen (s. o.).
> - **Person 1, Fahrkosten:** kein Abzug wegen Feld F.
> 
> ## Offene Punkte für die Fachperson
> 
> 1. **Person 1, Feld F:** Das Wiki bestätigt «kein Fahrkostenabzug» für AR 2025 (Randnotiz bei Form. 4 Ziff. 1.1). Ein Velo-Pauschalabzug (700) ist ohne Angabe zu Velonutzung nicht angesetzt.
> 2. **Person 2, Verpflegung:** Ich nehme an, dass sie mittags auswärts isst (so geschildert). Isst sie an einzelnen Tagen zu Hause, fällt der Abzug für diese Tage weg. Bei Heimfahrt über Mittag wäre der Fahrkostenabzug auf 3'200 bzw. 1'600 begrenzt.
> 3. **Ziff. 16.1 Bund:** Die Bundespauschale ist im Wiki nicht belegt. Ich habe 0 angesetzt (⬜ offen). Die Steuerverwaltung passt den Bundeswert an.
> 4. **Ziff. 13.2:** im Wiki ⚠️ strittig. Die Behandlung als «bereits im Nettolohn» ist hier die vorsichtige Lesart.
> 5. **Betreuungsbeitrag 2'400:** Ich habe ihn voll von den Betreuungskosten ohne Mittagessen abgezogen (WL Ziff. 16.2). Hat die Gutschrift Bezug zur Verpflegung, ändert sich der Betrag.
> 6. **Fahrkosten Bund Maximum 3'300:** Die ESTV-Wegleitung nennt abweichend 3'200 (Hinweis in Form. 4). Bei Person 2 (1'260) ohne Auswirkung.
> 7. **Fehlende Belege:** Prämienbescheinigung ist vorhanden. Vorjahresveranlagung, Vorjahresvermögen und Arbeitgeber-/Wohnangaben (Mietzins ist nicht deklarierbar) habe ich nicht erhalten. Einen Vermögensvergleich zum Vorjahr kann ich damit nicht machen.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

