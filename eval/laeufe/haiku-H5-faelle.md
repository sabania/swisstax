# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 14:55
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
  kanton: 85422
  rechnung: Staat 10'470 + 4'036 + 7'258 + 7'258 + 8'400 + 10'000 + 31'900 + 6'100 = 85'422; Bund 9'590 + 4'036 + 7'258 + 7'258 + 5'100 + 10'000 + 32'700 + 14'100
    = 90'042.
  ziffer: 18 (Code 299)
- bezeichnung: Nettoeinkommen
  bund: 81298
  fundstellen:
  - zh-form-300-2025__c0009
  kanton: 85918
  rechnung: 171'340 − 85'422 = 85'918; 171'340 − 90'042 = 81'298.
  ziffer: 21 (Code 310)
- bezeichnung: Krankheits- und Unfallkosten
  bund: 0
  fundstellen:
  - zh-wl-2025__c0117
  - zh-wl-2025__c0122
  - zh-stg-2025__par-32
  - bund-dbg-2025__art-33-t3
  kanton: 0
  rechnung: 'FALLE: Kosten 1''850 + 1''240 = 3''090 < Selbstbehalt 5 % von Ziff. 21 (Staat 4''295.90, Bund 4''064.90) → kein Abzug.'
  ziffer: 22.1 (Code 320)
- bezeichnung: Gemeinnützige Zuwendungen
  bund: 650
  fundstellen:
  - zh-wl-2025__c0121
  - zh-wl-2025__c0122
  - zh-stg-2025__par-32
  - bund-dbg-2025__art-33a
  kanton: 650
  rechnung: 400 + 250 = 650; ≥ 100 und unter 20 % von Ziff. 21 (Staat 17'183 / Bund 16'259).
  ziffer: 22.2 (Code 324)
- bezeichnung: Reineinkommen
  bund: 80648
  fundstellen:
  - zh-form-300-2025__c0009
  kanton: 85268
  rechnung: 85'918 − 0 − 650 = 85'268; 81'298 − 0 − 650 = 80'648.
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
  kanton: 66668
  rechnung: 85'268 − 18'600 = 66'668; 80'648 − 13'600 − 2'800 = 64'248.
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


**Antwort des Agenten** (157.8 s · Tools: 20 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__wert):

> ## Ausfüllhilfe Steuerjahr 2025, Kanton ZH, Ehepaar Marco und Sandra
> 
> Alle Beträge in CHF. Staat = Kanton ZH, Bund = direkte Bundessteuer. Die Zeilenbezeichnungen stammen aus dem Formular ZH 2025 (`zh-form-300-2025`). Der Status ist überwiegend ☑️ (Fundstelle geprüft, Abnahme offen).
> 
> ### Wichtigste Ergebnisse
> - **Krankheitskosten (Ziff. 22.1) sind 0 abziehbar.** Die Auslagen von 3'090 liegen unter dem Selbstbehalt von 5 % des Nettoeinkommens (Staat 4'362, Bund 4'131).
> - **Die Drittbetreuung ist auf 25'000 (Staat) bzw. 25'800 (Bund) pro Kind begrenzt.** Lena's Kita von 27'300 wird deshalb gekürzt.
> - **Der Verpflegungsabzug von Marco ist der grösste Einzelposten.** Für Sandra entfällt er, sofern sie in Winterthur nach Hause kann (siehe Prüfpunkt 2).
> 
> ### 1. Einkünfte
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb Marco | 103'000 | 103'000 | LA Ziff. 11 Nettolohn (118'400 − 8'110 − 7'290). `zh-form-300-2025__c0004`, ☑️ |
> | 1.1 | 101 | Haupterwerb Sandra | 67'200 | 67'200 | LA Ziff. 11 (76'800 − 5'260 − 4'340). Enthält Kinderzulagen 4'800, die über den Lohn ausbezahlt wurden. |
> | 4.1 | 150 | Wertschriften/Guthaben-Ertrag | 1'140 | 1'140 | Form. 340: Kol. A 960 (Dividenden, Code 539) + Kol. B 180 (Sparzins ohne VSt, Code 542). `zh-form-340-2025__c0005` |
> | 4.2 | 151 | Qualifizierte Beteiligung | 0 | 0 | Keine Beteiligung ≥ 10 % angegeben (Annahme). |
> | 7 / 19 | 199 | Total Einkünfte | 171'340 | 171'340 | 103'000 + 67'200 + 1'140 |
> 
> Verrechnungssteuer: Die VSt-Anspruch aus den Dividenden beträgt 336 (35 % von 960, Form. 340 Code 540). Die Anrechnung erfolgt im Hauptformular nach den Vorgaben des Formulars.
> 
> ### 2. Abzüge
> 
> **Hilfsblatt Berufsauslagen (Form. 360)**
> 
> | Person | Position | Code | Staat | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | Marco | ÖV-Abo Winterthur–Zug | 201 | 4'180 | 3'300 (Plafond) | Staat-Plafond 5'200 nicht erreicht; Bund-Plafond 3'300 (`zh-form-360-2025__c0001`). Feld F nicht angekreuzt, also abziehbar. |
> | Marco | Verpflegung voll (15 × 220 Tage = 3'300, max. 3'200) | 208 | 3'200 | 3'200 (Vorbehalt) | Heimkehr von Zug nicht möglich. Bund nur, wenn die Hauptmahlzeit mehr als 10 kostet (Prüfpunkt 1). `zh-form-360-2025__c0003`, `zh-wl-2025__c0066` |
> | Marco | Pauschale übrige Berufsauslagen | 212 | 3'090 | 3'090 | 3 % von 103'000, Min. 2'000, Max. 4'000 (`zh-pauschalierung-berufsauslagen-2025__c0005`, `bund-bkv-2025__anhang-1`) |
> | **Marco** | **Total Ziff. 11.1** | **220** | **10'470** | **9'590** | Bund: 3'300 + 3'200 + 3'090 |
> | Sandra | Velo-Pauschale | 222 | 700 | 700 | Eigenes Velo, Arbeitsweg Winterthur (`zh-form-360-2025__c0001`) |
> | Sandra | Verpflegung Personalrestaurant (Feld G) | 226 | 0 | 0 | Wohnort und Arbeitsort sind beide Winterthur, Heimkehr ist also möglich. Abzug nur, wenn sie nicht nach Hause kann (Prüfpunkt 2). |
> | Sandra | Pauschale übrige Berufsauslagen | 3 %-Pauschale | 2'016 | 2'016 | 3 % von 67'200 |
> | **Sandra** | **Total Ziff. 11.2** | **240** | **2'716** | **2'716** | |
> 
> **Übrige Abzüge**
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 14.1 | 260 | Säule 3a Marco | 7'258 | 7'258 | Max. mit 2. Säule. Beide haben BVG (LA 10.1). Bescheinigung 3a beilegen. `zh-form-300-2025__c0008` |
> | 14.2 | 261 | Säule 3a Sandra | 7'258 | 7'258 | Gleiche Regel |
> | 15 | 270 | Versicherungsprämien/Sparzins | 8'400 | 5'100 | Form. 365 Teil A: KK 15'840 (Code 601) + Sparzins 180 (604) = 16'020. Teil B (Max. verheiratet 5'800 / 3'700 + 2 Kinder à 1'300 / 700). Der Teil-B-Wert ist kleiner, daher gilt B. `zh-form-365-2025__c0001`, `__c0002` |
> | 16.1 | 280 | Freiwilliger PK-Einkauf Marco | 10'000 | 10'000 | Selbst bezahlt, nicht im LA (Ziff. 10.2 = 0). Einkaufsbescheinigung (Formular 21 EDP) beilegen. `zh-wl-2025__c0092` |
> | 16.6 | 376 | Fremdbetreuung Lena (Kita) | 25'000 | 25'800 | min(27'300; Limite). Kürzung auf Limite pro Kind. `zh-stg-2025__par-31-t4` |
> | 16.6 | 376 | Fremdbetreuung Noah (Hort) | 6'900 | 6'900 | Unter Limite. Hort-Verpflegung herausrechnen, falls enthalten (Prüfpunkt 3). |
> | 17 | 290 | Zweiverdienerabzug | 6'100 | 14'100 | Basis = niedrigeres Erwerbseinkommen: Sandra 67'200 − 2'716 − 7'258 = 57'226. Staat: max. 6'100. Bund: max. 14'100 (50 % = 28'613 übersteigt das Max.). `zh-form-300-2025__c0008`, `zh-wl-2025__c0112` |
> | **18** | **299** | **Total Abzüge** | **84'102** | **88'722** | Summe aller obigen Abzüge |
> 
> ### 3. Nettoeinkommen und Sozialabzüge
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 21 | 310 | Nettoeinkommen | 87'238 | 82'618 | 171'340 − 84'102 bzw. − 88'722 |
> | 22.1 | 320 | Krankheitskosten | 0 | 0 | Auslagen 3'090 (KK-Selbstbehalt 1'240 + Zahnarzt 1'850, Codes 300/302). Schwelle 5 %: 4'362 bzw. 4'131. Auslagen liegen darunter, Abzug 0. `zh-form-370__c0002` |
> | 22.2 | 324 | Gemeinnützige Zuwendungen | 650 | 650 | Rotes Kreuz 400 + UNICEF 250. Min. 100 erfüllt, Max. 20 % (17'447 bzw. 16'524) nicht erreicht. |
> | 23 | 350 | Reineinkommen | 86'588 | 81'968 | 87'238 − 650 bzw. 82'618 − 650 |
> | 24.1 | 370 | Kinderabzug Haushalt (Lena, Noah) | 18'600 | 13'600 | 2 × 9'300 bzw. 2 × 6'800 |
> | 24.3 | 365 | Ehegattenabzug | – | 2'800 | Nur Bund |
> | 25 / 27 | 390 / 398 | Steuerbares Einkommen | **67'988** | **65'568** | 86'588 − 18'600 bzw. 81'968 − 13'600 − 2'800 |
> 
> ### 4. Vermögen
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 30.1 | 400 | Wertschriften und Guthaben | 82'000 | – | Sparkonto 42'500 + Privatkonto 8'300 + Depot 31'200 (Steuerwert 31.12.2025). `zh-form-340-2025__c0005` |
> | 33 / 35 | 460 / 490 | Total Vermögen | 82'000 | – | Keine Schulden |
> | 37 | 498 | Steuerbares Vermögen ZH | 82'000 | – | Tarif 0 ‰ bis 159'000 (verheiratet): Vermögenssteuer 0 (`zh-stg-2025__par-47-t2`). Bund kennt keine Vermögenssteuer. |
> 
> Ziff. 40 (Kapitalleistungen aus Vorsorge, Code 510): 0. Keine Bezüge in den letzten drei Jahren.
> 
> ### 5. Nicht zu deklarieren oder nicht abziehbar
> 
> - **Hausrat- und Privathaftpflicht-Versicherung (465):** Sachversicherung. Abziehbar sind nur Kranken-, Unfall-, Lebens- und Rentenversicherungsprämien sowie Sparzinsen (`zh-form-365-2025__c0001`).
> - **Swisscom-Handyrechnungen (1'080):** Privatausgaben, kein Abzug.
> - **Zahnarzt 1'850 und KK-Selbstbehalt 1'240:** Auslagen zwar real, aber unter der 5 %-Schwelle. Abzug 0. Belege aufbewahren.
> - **Mittagessen Sandra (Personalrestaurant):** kein Abzug, solange Heimkehr möglich ist (siehe Prüfpunkt 2).
> - **Mittagessen Marco:** nicht als Ausgabe erfassen, sondern nur über den Verpflegungsabzug (Code 208).
> - **Lohnausweis Ziff. 9 und 10.1 (AHV/BVG):** bereits im Nettolohn, nicht nochmals unter Ziff. 16.1 oder 14 erfassen.
> - **PK-/3a-Guthaben:** nicht ins Wertschriftenverzeichnis (`zh-form-300-2025__c0011`).
> - **Mietzins:** im Formular ZH 2025 gibt es keinen Abzug und kein Feld dafür.
> - **Dividenden-Brutto 960 und Sparzins 180:** in Form. 340 erfassen, nicht in Ziff. 15 doppelt (Sparzins fliesst über Form. 365 Code 604 ein, ist also gewollt).
> 
> ### 6. Prüfpunkte vor dem Ausfüllen
> 
> 1. **Bund-Verpflegung Marco:** Der Bundesabzug von 3'200 gilt nur, wenn die Hauptmahlzeit mehr als 10 CHF kostet. Ist sie günstiger, fällt er weg. Dann sinkt Bund Ziff. 11.1 auf 6'390, und das Bund-Nettoeinkommen steigt um 3'200 auf 85'818 (steuerbares Bundeseinkommen 68'768).
> 2. **Verpflegung Sandra:** Der Abzug von 1'320 (7.50 × 176 Tage) gilt nur, wenn sie in der Mittagspause nicht nach Hause kann. Bei Wohnort = Arbeitsort in Winterthur ist das unwahrscheinlich. Für den Bund ist bei einer Personalrestaurant-Verpflegung nur der halbe Abzug möglich (zu prüfen).
> 3. **Hort-Rechnung Noah (6'900):** Falls Mittagessen enthalten ist, muss der Verpflegungsanteil heraus, weil er nicht betreuungsbedingt ist.
> 4. **Kita Lena:** Verpflegung ist laut Angabe nicht enthalten. Die Rechnung 27'300 wird auf 25'000 (Staat) bzw. 25'800 (Bund) gekürzt.
> 5. **Quellenkonflikt Drittbetreuung:** Die VKP ZH nennt für 2024 noch 10'400, das StG ZH (Nachtrag 127) für 2025 25'000. Angewendet wurde 25'000. Bitte bestätigen.
> 6. **Lohnausweis-Regeln (Feld F/G):** Die Wiki-Quelle ist die Wegleitung 2026, es gibt keine 2025-Fassung. Die Regeln sind qualitativ; bitte gegen die Wegleitung 2025 prüfen.
> 7. **Spendenempfänger:** Rotes Kreuz und UNICEF Schweiz müssen im ZH-Verzeichnis der steuerbefreiten Institutionen stehen. Ich habe das nicht geprüft.
> 8. **Kinderzulagen Sandra (4'800):** Sie sind im Lohn enthalten. Falls sie direkt von der Ausgleichskasse ausbezahlt wurden, wären sie nach Ziff. 3.4 steuerfrei und müssten herausgerechnet werden. Bitte mit der Lohnabrechnung abgleichen.
> 9. **Bankspesen (Ziff. 16.3):** keine Angaben, daher nicht berücksichtigt.
> 10. **Qualifizierte Beteiligung (≥ 10 %):** als nicht vorhanden angenommen.
> 
> ### 7. Beilagen
> 
> Lohnausweise (beide), Berufsauslagen-Formular (Form. 360, je Person), Form. 365 (Versicherungsprämien), Form. 340 (Wertschriften), Formular 370 (Krankheitskosten, Auslagen aufgelistet), Aufstellung Spenden, 3a-Bescheinigungen (je 7'258), Einkaufsbescheinigung PK (10'000), Kita-/Hort-Rechnungen (auf Verlangen), ÖV-Abo (auf Verlangen), Steuerauszug ZKB.

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


**Antwort des Agenten** (144.4 s · Tools: 22 Aufrufe steuerwiki__formular, steuerwiki__wert, steuerwiki__position, steuerwiki__suche):

> Ich starte mit dem Gesamtformular für SG 2025, damit ich die Ziffern und Limiten habe, bevor ich die einzelnen Belege zuordne.
> 
> Die Basiswerte stehen. Jetzt prüfe ich die Positionen, bei denen die Einordnung nicht offensichtlich ist: Lohn und Berufskosten, Alimente, Kinderbetreuung, Versicherungen, Krankheitskosten, Pensionskasse, Wertschriften und Spenden.
> 
> Die Positionen sind geklärt. Vor der Berechnung prüfe ich noch vier offene Punkte: Kinderabzug bei Kindergarten (Vorschule oder Schule), Alleinerziehenden-Abzug beim Bund, Steuerbarkeit der Kinderalimente beim Bund und die Abziehbarkeit von Motorfahrzeugsteuer und Autoversicherung.
> 
> # Ausfüllhilfe Steuererklärung SG 2025: Nadine (Alleinerziehend, Elias 5 J.)
> 
> **Vorbehalt:** Die Fundstellen sind von den Werkzeugen als «agent-geprüft» markiert, die fachliche Abnahme steht noch aus. Die Steuerbeträge selbst rechnet das Steueramt. Hier stehen nur die Eingaben und Zwischensummen. Kanton (SG) und Bund sind getrennt gerechnet, die Bundesanpassungen nimmt das Steueramt automatisch vor (Merkblatt 32, `sg-wl-2025__c0173`).
> 
> ## 1. Ergebnis im Überblick
> 
> | Zeile | Kanton SG | Bund |
> |---|---|---|
> | Einkünfte Total (Ziff. 7) | 82'668 | 82'668 |
> | Abzüge Total (Ziff. 18) | 40'458 | 33'548 |
> | Nettoeinkommen (Ziff. 20) | 42'210 | 49'120 |
> | Abzug Krankheitskosten (Ziff. 21.1) | 2'755.80 | 1'144 |
> | Reineinkommen (Ziff. 22) | 39'454.20 | 47'976 |
> | Kinderabzug Elias (Ziff. 23.2) | 10'800 | 6'800 |
> | **Steuerbares Einkommen (Ziff. 24)** | **28'654.20** | **41'176** |
> | Steuerbares Vermögen (Ziff. 37) | 0 (Vorbehalt, s. Abschnitt 4) | – |
> 
> ## 2. Position für Position
> 
> ### Einkünfte
> 
> | Ziff./Code | Eintrag | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | **1.1** (Code 100) | Nettolohn Lohnausweis | 73'000 | 73'000 | Bruttolohn 83'500 − AHV/ALV 5'890 − BVG 4'610 = 73'000. Der Bruttolohn enthält die Kinderzulage 2'400, sie ist also schon im Nettolohn. Keine Ziff. 3.5. Basis `sg-form-1-2025__c0004`, `sg-wl-2025__c0042` ☑️ |
> | **4.1** (Code 146) | Zinsen Sparkonto (Form. 2) | 68 | 68 | Bruttozins, keine VSt. Unter 200 Franken entfällt der VSt-Nachweis (Ziff. 36.3/Form. 6) ☑️ |
> | **6.1** (Code 156) | Kinderalimente für Elias | 9'600 | 9'600 | 12 × 800. Nadine ist Empfängerin und hat die elterliche Obhut. Beim Empfänger steuerbar (`sg-form-1-2025__c0006`, Bund: KS 30 Ziff. 14.3, `bund-ks-30__c0102`) ☑️ |
> | **6.1** (Code 154) | Alimente für Nadine selbst | 0 | 0 | Keine solchen Beiträge belegt |
> 
> ### Abzüge
> 
> | Ziff./Code | Eintrag | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | **10.1** (Code 438) → Form. 4 Ziff. 6 | Berufskosten Nadine | **13'600** | **8'690** | Fahrkosten + Verpflegung + übrige Kosten, je unten |
> | ↳ Form. 4 Ziff. 1.3 | Fahrkosten Auto | 8'000 | 3'300 | 32 km × 2 × 220 Tage × 0.70 = 9'856. Gedeckelt auf Kanton 8'000 (Zwischentotal 1.1–1.3) und Bund 3'300 (`sg-form-4-2025__c0002`, `bund-dbg-2025__art-26`) ☑️ |
> | ↳ Form. 4 Ziff. 2.1 | Verpflegung | 3'200 | 3'200 | 220 × 15 = 3'300, gedeckelt auf 3'200 (`sg-wl-2025__c0074`) ☑️ |
> | ↳ Form. 4 Ziff. 3.1 | Übrige Berufskosten (Pauschale) | 2'400 | 2'190 | Kanton: 700 + 10 % × 73'000 = 8'000, gedeckelt auf 2'400. Bund: 3 % × 73'000 = 2'190 (Min. 2'000, Max. 4'000) ☑️ |
> | **13.1** (Code 208) | Säule 3a | 7'258 | 7'258 | Erwerbstätige mit 2. Säule, Max. 7'258 erreicht. Bescheinigung beilegen (`sg-wl-2025__c0085`) ☑️ |
> | **13.2** (Code 218) | Freiwilliger PK-Einkauf | 6'000 | 6'000 | Direkt bezahlt am 20.10.2025. Lohnausweis Ziff. 10.2 = 0, also kein Doppelabzug. Einkaufsberechnung und Bescheinigung beilegen (`sg-wl-2025__c0086`) ☑️ |
> | **14** (Code 600) | Versicherungsprämien und Sparzinsen | 4'500 | 2'500 | A = KK brutto 6'600 (Nadine 5'280 + Elias 1'320) + Sparzinsen 68 − IPV 1'800 = 4'868. Kanton B: 3'400 + 1'100 (Kind) = 4'500. Bund B: 1'800 + 700 = 2'500. Keine Zuschläge (Säule 2 und 3a vorhanden). Abzug = min(A; B) ☑️ |
> | **16.2** (Code 258) | Kinderbetreuung Elias (Kita/Tagesstruktur) | 8'760 | 8'760 | 9'840 − Mahlzeiten 1'080 = 8'760. Max. 26'700 (Kanton) bzw. 25'800 (Bund). Formular 10 ausfüllen (nicht im Wiki, Regel aus Wegleitung) ☑️ |
> | **16.4** (Code 223) | Berufsorientierte Weiterbildung | 340 | 340 | Excel-Kurs, selbst bezahlt. Voraussetzung (20. Altersjahr) erfüllt. Aufstellung einreichen (`sg-form-1-2025__c0009`) ☑️ |
> | **12.1 / 12.2** | Unterhalt (Abzug für den Zahlenden) | 0 | 0 | Nadine ist Empfängerin, daher kein Abzug. Das ist die Seite des Ex-Ehemanns |
> 
> **Abzüge Kanton:** 13'600 + 7'258 + 6'000 + 4'500 + 8'760 + 340 = **40'458**
> **Abzüge Bund:** 8'690 + 7'258 + 6'000 + 2'500 + 8'760 + 340 = **33'548**
> 
> ### Einkommensberechnung
> 
> | Ziff./Code | Eintrag | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | **20** (Code 234) | Nettoeinkommen | 42'210 | 49'120 | Einkünfte − Abzüge (oben) |
> | **21.1** (Code 650/238/240) | Krankheitskosten | 2'755.80 | 1'144 | Vorkolonne 2'750 (Zahnarzt, ohne Kassenbeitrag) + 850 (Franchise/Selbstbehalt) = 3'600. Abzug = 3'600 − Selbstbehalt. Kanton 2 % × 42'210 = 844.20. Bund 5 % × 49'120 = 2'456. Form. 6 Rückseite (`sg-form-6-2025__c0003`) ☑️ |
> | **21.3** (Code 244) | Spende Caritas | 0 | 0 | 80 unter dem Minimum von 100 (`sg-form-1-2025__c0010`). Kein Abzug |
> | **22** (Code 248) | Reineinkommen | 39'454.20 | 47'976 | Nettoeinkommen − Krankheitskosten |
> | **23.2** (Code 254) | Kinderabzug Elias | 10'800 | 6'800 | Kindergarten zählt als Schule (`sg-wl-2025__c0104`, `sg-wl-2025__c0035`), daher 10'800 und nicht 7'600. Bund einheitlich 6'800 (`bund-dbg-2025__art-35`) ☑️ |
> | **23.3** (Code 256) | Ausbildungskosten | 0 | 0 | Keine Ausbildungskosten für Elias. Kita und Tagesstruktur sind keine Ausbildung |
> | **24** (Code 268) | Steuerbares Einkommen | **28'654.20** | **41'176** | Reineinkommen − Kinderabzug |
> 
> Der Bund-Steuerbetrag enthält einen Abzug von max. 263 pro Kind (`bund-dbg-2025__art-36-t4`). Das rechnet das Steueramt. Der Tarif H für Alleinerziehende (`bund-ks-45__c0045`) wird ebenfalls automatisch angewendet. Keine eigene Zahl eintragen.
> 
> ### Vermögen
> 
> | Ziff./Code | Eintrag | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | **30.1** (Code 300) | Sparkonto Raiffeisen per 31.12. | 31'500 | – | Bund hat keine Vermögenssteuer |
> | **36.1–36.3** | Freibetrag alleinstehend + Kind | −95'000 | – | 75'000 + 20'000 (Kind unter Obhut, `sg-stg-2025__art-64`) |
> | **37** (Code 338) | Steuerbares Vermögen | **0** | – | Nur gültig, wenn die Lücken unten keine weiteren Werte ergeben |
> 
> ## 3. Nicht zu deklarieren bzw. nicht abziehbar
> 
> | Beleg | Entscheid | Begründung |
> |---|---|---|
> | Lohnausweis Kinderzulage 2'400 | In Ziff. 1.1 enthalten, nicht separat | Liegt im Lohnausweis (`sg-wl-2025__c0042`) |
> | Mahlzeiten Kita 1'080 | Nicht abziehbar | Verpflegungsanteil, ist aus Ziff. 16.2 herauszurechnen |
> | Spende Caritas 80 | Nicht abziehbar | Unter dem Mindestbetrag von 100 (Ziff. 21.3) |
> | Motorfahrzeugsteuer 410 | Nicht abziehbar | Der Kilometerpauschale 0.70 deckt die Fahrzeugkosten ab. Sonst keine Abzugsposition (Art. 47 StG SG, `sg-stg-2025__art-47`) |
> | Auto-Haftpflicht/Kasko 1'020 | Nicht abziehbar | Motorfahrzeugversicherungen sind laut Ziff. 14 nicht abziehbar (`sg-wl-2025__c0088`). Auch durch Kilometerpauschale gedeckt |
> | Handy-Abo 720 | Nicht abziehbar | Privatkosten (Art. 47 StG) |
> | Alimente 9'600 als Abzug | Nicht bei Nadine | Nur für den Zahlenden (Ziff. 12.2). Nadine deklariert sie als Einkünfte (Ziff. 6.1) |
> | Kassenbeitrag IPV 1'800 | Kein Einkommen | Wird von den Prämien abgezogen (Form. 6 Teil A.e). Bei Nadine und Elias zusammen |
> | Mittagessen | Kein Abzug | Nur über Verpflegungspauschale (Ziff. 2.1). Keine Kantine, daher kein Verbilligungsabzug |
> 
> ## 4. Offene Punkte vor der Abgabe
> 
> 1. **Begründung Auto (größter Hebel).** Die Fahrkosten machen 8'000 Kanton und 3'300 Bund aus. Im Formular 4 Ziff. 1.3 muss «kein ÖV zumutbar» begründet werden. Argument: Arbeitsbeginn 06:00, erste ÖV-Verbindung erst 06:40. Fahrplanauszug beilegen. Wird die Begründung nicht anerkannt, entfallen die Fahrkosten ganz (ÖV-Kosten sind 0). Das Steuerergebnis steigt dann um rund 8'000 Kanton bzw. 3'300 Bund plus den Effekt auf den Selbstbehalt.
> 2. **Vermögen unvollständig.** Es fehlen der Kontostand der Säule 3a per 31.12.2025 (Ziff. 30.1 bzw. 30.3, je nach Kontoart) und der Verkehrswert des Autos (Ziff. 30.4). Beides kann die Vermögenssteuer auslösen, sobald es über 95'000 liegt.
> 3. **Krankheitskosten.** Es fehlen die Bruttobeträge der Arztrechnungen, die die Krankenkasse übernommen hat. Form. 6 verlangt bei Verweis auf den Kassenauszug die Detailaufstellung mit Leistungsübersicht (`sg-form-6-2025__c0003`).
> 4. **Kinderabzug.** Der Kinderabzug setzt voraus, dass Nadine überwiegend für den Unterhalt aufkommt. Der Ex-Ehemann zahlt 800 pro Monat, das sollte reichen, ist aber zu dokumentieren.
> 5. **Formular 10 (Kita).** Ausfüllen mit Vorname des Kindes, bezahlten Kosten und Name und Adresse der Betreuungsperson. Die Vorlage ist nicht im Wiki.
> 
> ## 5. Belege beilegen bzw. bereithalten
> 
> - **Einreichen (immer):** Lohnausweis; PK-Bescheinigung Einkauf mit Einkaufsberechnung (`sg-wl-2025__c0086`); Säule-3a-Bescheinigung.
> - **Einreichen (bedingt):** Scheidungsurteil bzw. Unterhaltsvereinbarung mit Zahlungsnachweisen (Ziff. 6.1); Fahrplanauszug und Fahrzeugbegründung (Form. 4 Ziff. 1.3).
> - **Auf Verlangen bereithalten:** KK-Prämienrechnung und IPV-Verfügung; Kassenauszug mit Detailaufstellung; Arztrechnungen; Kita-Rechnungen; Weiterbildungsrechnung; Spendenbestätigung (80, nicht abziehbar).
> 
> **Fazit:** Das steuerbare Einkommen beträgt **Kanton 28'654.20** und **Bund 41'176**. Das steuerbare Vermögen ist **0**, solange der Kontostand der 3a-Konten und der Fahrzeugwert fehlen. Der Hauptrisikopunkt ist die Anerkennung der Auto-Begründung.

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
  - bund-vstg__art-5-t1
  kanton: 2350
  rechnung: 'Spalte 8 (mit VSt): Sparzins 250 (über 200 → VSt-pflichtig) + Dividenden 2''100 = 2''350.'
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
  kanton: 40150
  rechnung: 27'000 + 10'800 + 2'350 = 40'150.
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
  kanton: 44990
  rechnung: 40'150 + 4'840 = 44'990; 40'150 + 8'920 = 49'070.
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
  kanton: 38340
  rechnung: 44'990 − 6'650 = 38'340; 49'070 − 5'850 = 43'220.
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
  kanton: 4623
  rechnung: 'A: Kostenbeteiligung 1''000 + Zahnarzt 4''440 + Brille 1''400 = 6''840; B Vergütung Dritter −300 → 6''540. Selbstbehalt 5 % von Ziff. 22: Staat 1''917
    → 4''623; Bund 2''161 → 4''379. Hinweis: § 34 Ziff. 10 StG nennt «Reineinkommen», Formular 5.1/WL rechnen mit Ziff. 22 – Formular angewendet.'
  ziffer: 23.1 (Code 364) – via Formular 5.1
- bezeichnung: Freiwillige Zuwendungen
  bund: 550
  fundstellen:
  - tg-form-06-2025__c0002
  - tg-wl-2025__c0218
  - tg-stg__par-34-t4
  - bund-dbg-2025__art-33a
  kanton: 350
  rechnung: 'Total 300 + 250 = 550. Kanton: Selbstbehalt 200 → 350 (Max. 8''000, da Nettoeinkommen bis 40''000). Bund: ab 100 voll abziehbar, 550 (unter 20 % von
    43''220).'
  ziffer: 23.2 (Code 366) – via Formular 6
- bezeichnung: Reineinkommen
  bund: 38291
  fundstellen:
  - tg-form-01-2025__c0012
  kanton: 33367
  rechnung: 38'340 − 4'623 − 350 = 33'367; 43'220 − 4'379 − 550 = 38'291.
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
  rechnung: 'Reineinkommen Ziff. 24 (Kanton) 33''367 → Stufe Alleinstehende 32''900–33''899 = 1''000 (4''200 − 16 × 200 je volle 1''000 über 16''900). Bund: kein
    Abzug.'
  ziffer: 25.3 (Code 388)
- bezeichnung: Steuerbares Einkommen
  bund: 38291
  fundstellen:
  - tg-form-01-2025__c0013
  kanton: 32367
  rechnung: 33'367 − 1'000 = 32'367; Bund keine Sozialabzüge → 38'291.
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


**Antwort des Agenten** (111.8 s · Tools: 22 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige):

> # Ausfüllhilfe Steuererklärung 2025 TG (Frauenfeld, alleinstehend, verwitwet, 70 J.)
> 
> Kanton (Staats-/Gemeindesteuer) und Bund sind getrennt angegeben. Der Bund hat keinen Vermögenssteuer- und keinen Sozialabzug für diesen Fall, deshalb stehen dort teils nur Einkünfte.
> 
> **Annahmen (bitte bestätigen):** Wohnsitz am 31.12.2025 in Frauenfeld. Keine Kinder, keine Unterstützungspersonen. Keine Erwerbstätigkeit und keine Beiträge an 2. Säule oder 3a. Der Zahnarzt wurde nicht von der Krankenkasse vergütet. Keine weiteren Konten, kein Bargeld, keine Lebensversicherung.
> 
> ## 1. Einkünfte
> 
> | Ziff. / Code | Position | Kanton | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|
> | 3.1 / 130 | AHV-Altersrente | 27'000 | 27'000 | 100 % steuerbar | tg-form-01-2025__c0007, tg-wl-2025__c0076 |
> | 3.2 / 132 | PK-Altersrente | 10'800 | 10'800 | Rentenbeginn 01.01.2020, daher 100 % (Übergangsrecht 80 % entfällt) | tg-wl-2025__c0077 |
> | 4 / 150 | Wertschriftenerträge, Sp. 8 mit VSt | 2'350 | 2'350 | Dividende 2'100 + Sparzins 250 brutto. Sparzins über 200, daher Sp. 8 und nicht Sp. 9 | tg-form-01-2025__c0008, tg-wl-2025__c0163 |
> | 8.1 / 180 | Eigenmietwert netto | 4'840 | 8'920 | siehe Abschnitt 1a | tg-wl-2025__c0225, tg-form-07-2025__c0002 |
> | 9 | Total Einkünfte | **44'990** | **49'070** | | |
> 
> **1a. Liegenschaft (Form. 7/8)**
> 
> | | Kanton | Bund |
> |---|---|---|
> | Mietwert selbstgenutzt (indexiert) | 20'400 | 20'400 |
> | Selbstnutzungsabzug (K 40 %, B 20 %) | −8'160 | −4'080 |
> | Steuerbarer Eigenmietwert | 12'240 | 16'320 |
> | Effektive Unterhaltskosten (siehe unten) | −7'400 | −7'400 |
> | **Nettoerfolg** | **4'840** | **8'920** |
> 
> Effektive Kosten (Form. 8, je Rechnung):
> - Malerarbeiten Ersatzanstrich 6'400: Unterhalt, abziehbar.
> - Gebäudeversicherung 520: Sachversicherung der Liegenschaft, abziehbar (tg-wl-2025__c0227).
> - Baumschnitt/Gartenpflege 480: Unterhalt, abziehbar.
> - Wintergarten-Anbau 31'000: **nicht abziehbar**. Neubau/Anbau gehört in Spalte «Anlagekosten/Mehrwert» (tg-form-08 / tg-wl-2025__c0234).
> 
> Pauschale wäre (Basis steuerbarer EMW, Gebäude älter als 10 Jahre, 20 %): Kanton 2'448, Bund 3'264. Effektiv (7'400) ist in beiden Spalten höher. **Empfehlung: effektiv**, Form. 8 ausfüllen.
> 
> ## 2. Abzüge
> 
> | Ziff. / Code | Position | Kanton | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|
> | 11 / 290 | Schuldzinsen (Form. 4.1) | 3'150 | 3'150 | Hypothekarzins 2025 voll abziehbar (Limite Vermögensertrag + 50'000 nicht erreicht) | tg-wl-2025__c0173 |
> | 14 / 330 | Versicherungsprämien/Sparzinsen (Form. 5.2) | 3'500 | 2'700 | A = KK 6'240 + Sparzins 250 = 6'490. Kanton: min(6'490; 3'500 alleinstehend). Bund: ohne 2./3a-Beiträge, min(6'490; 2'700) | tg-form-05-2-2025__c0002/c0003 |
> | 19 / 360 | Total Abzüge | **6'650** | **5'850** | | |
> 
> ## 3. Berechnung
> 
> | Ziff. | | Kanton | Bund |
> |---|---|---|---|
> | 9 / 20 | Total Einkünfte | 44'990 | 49'070 |
> | 21 | Total Abzüge | −6'650 | −5'850 |
> | 22 / 362 | **Nettoeinkommen** | **38'340** | **43'220** |
> | 23.1 / 364 | Krankheitskosten (Form. 5.1 D) | 4'623 | 4'379 |
> | 23.2 / 366 | Spenden (Form. 6) | 350 | 550 |
> | 24 / 372 | **Reineinkommen** | **33'367** | **38'291** |
> | 25.3 / 388 | Abzug AHV-Rentner/verwitwet (nur Kanton) | 1'000 | – |
> | 26 / 398 | **Steuerbares Einkommen** | **32'367** | **38'291** |
> 
> **Krankheitskosten (Form. 5.1, Ziff. 23.1)**
> - A: Zahnarzt 4'440 + Brille 1'400 + Franchise/Selbstbehalt 1'000 = 6'840 (tg-form-05-1-2025__c0001).
> - B: Brille, Vergütung Zusatzversicherung 300 (tg-form-05-1-2025__c0002).
> - A − B = 6'540. Abzug Selbstbehalt 5 % von Ziff. 22: Kanton 6'540 − 1'917 = 4'623; Bund 6'540 − 2'161 = 4'379.
> - Die Krankenkassenprämie ist **nicht** hier, sondern in Ziff. 14 (Abschnitt 2).
> 
> **Spenden (Form. 6, Ziff. 23.2)**
> - Krebsliga TG 300 + Pro Senectute TG 250 = 550.
> - Kanton: 550 − 200 Selbstbehalt = 350 (Max. 8'000 nicht erreicht).
> - Bund: 550 (ab 100, ohne Selbstbehalt; Max. 20 % = 8'644 nicht erreicht).
> 
> **AHV-Rentnerabzug (Ziff. 25.3, Kanton)**
> - Reineinkommen Kanton 33'367. Max. 4'200 − 200 × volle 1'000 über 16'900 (16 Stück) = 4'200 − 3'200 = **1'000**.
> - Wegleitungs-Tabelle hat einen Druckfehler in der Zeile «36'900–37'689». Mit der Formel rechnen (tg-form-01-2025__c0013).
> 
> ## 4. Vermögen (nur Kanton)
> 
> | Ziff. | Position | Betrag |
> |---|---|---|
> | 30.1 | Sparkonto 48'000 + Depot 95'000 | 143'000 |
> | 31 / 430 | Liegenschaft, Steuerwert | 410'000 |
> | 33 / 464 | Total Vermögen | 553'000 |
> | 34 / 466 | Hypothek | 180'000 |
> | 35 / 468 | Reinvermögen | 373'000 |
> | 36.2 / 472 | Freibetrag alleinstehend | −100'000 |
> | 37 / 498 | **Steuerbares Vermögen** | **273'000** |
> 
> Fundstellen: tg-wl-2025__c0128 (Freibetrag), tg-wl-2025__c0239 (Steuerwert).
> 
> ## 5. Nicht zu deklarieren bzw. nicht abziehbar
> 
> - **Hausratversicherung 380.** Keine Sachversicherung der Liegenschaft; nicht abziehbar (tg-wl-2025__c0227). Die Police wird nicht eingereicht (tg-wl-2025__c0227).
> - **Serafe 335 und Handyrechnung.** Lebenshaltung, kein Abzugstatbestand in Ziff. 14–23. Nicht deklarieren.
> - **Wintergarten 31'000.** Kein Unterhalt, daher kein Abzug. Nicht in Ziff. 8.1 oder 23.1. Der Anbau wirkt über den Steuerwert in Ziff. 31 (Abschnitt 6).
> - **Verrechnungssteuer 822.50** (87.50 + 735). Kein Abzug, sondern Rückforderungsanspruch über Form. 2 (35 % von 2'350; tg-wl-2025__c0167).
> - **Kapitalbeträge und Sparguthaben** gehören nicht zu den Einkünften, nur zu Ziff. 30.
> - **Krankenkassenprämie 6'240** ist Abzug in Ziff. 14, aber der Höchstbetrag begrenzt ihn (Kanton 3'500, Bund 2'700). Der Rest ist nicht abziehbar.
> - **Spenden unter 1'000 pro Zuwendung** müssen nicht eingereicht werden, nur auf Verlangen (tg-wl-2025__c0220).
> 
> ## 6. Offene Punkte vor Abgabe
> 
> 1. **Wintergarten im Steuerwert?** Prüfen, ob die Liegenschaftensteuerrechnung 2026 den Anbau (fertig 2025) enthält. Falls nicht, Ziff. 31 anpassen (tg-wl-2025__c0239).
> 2. **Bund-Selbstnutzungsabzug 20 %** stammt aus dem Wiki. Ob sich der Satz für 2025 ändert, ist dort nicht belegt. Gegen die aktuelle Bundes-Wegleitung prüfen.
> 3. **Krankenkassen-Leistungsabrechnung** für Zahnarzt/Brille prüfen. Falls die Kasse Zahnarztkosten vergütet hat, B erhöhen.
> 4. **Gemeinnützigkeit** von Krebsliga TG und Pro Senectute TG gegen die Liste der Steuerverwaltung TG prüfen.
> 5. **AHV-Abzug 1'000** gegen Wegleitung S. 25 gegenprüfen (Druckfehler in der Tabelle).
> 6. **Weitere Vermögenswerte** (Bargeld, Lebensversicherungen, zusätzliche Konten) bestätigen. Keine Angaben vorhanden, daher nicht berücksichtigt.
> 7. **Eigenmietwert-Abschaffung:** Die Volksabstimmung 2025 zur Abschaffung des Eigenmietwerts ist im Wiki nicht belegt. Sie betrifft nach meinem Kenntnisstand erst spätere Steuerjahre, muss aber für 2025 nicht gelten. Bitte prüfen.
> 
> Die Status-Angaben der Fundstellen lauten ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Abnahme durch die Fachperson steht noch aus.

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
  kanton: 45358
  rechnung: Kanton 4'000 + 6'300 + 7'258 + 5'000 + 7'400 + 10'200 + 5'200 = 45'358; Bund 4'159 + 5'946 + 7'258 + 5'000 + 5'100 + 10'200 + 14'100 = 51'763.
  ziffer: '18'
- bezeichnung: Nettoeinkommen
  bund: 103147
  fundstellen:
  - ar-wl-2025__c0099
  kanton: 109552
  rechnung: 154'910 − 45'358 = 109'552; 154'910 − 51'763 = 103'147.
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
  kanton: 109252
  rechnung: 109'552 − 300 = 109'252; 103'147 − 300 = 102'847.
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
  kanton: 90252
  rechnung: 109'252 − 7'400 − 11'600 = 90'252; 102'847 − 6'800 − 6'800 − 2'800 = 86'447.
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


**Antwort des Agenten** (142.1 s · Tools: 25 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige):

> # Ausfüllhilfe Steuererklärung 2025, Kanton Appenzell Ausserrhoden (Ehepaar, Herisau)
> 
> Alle Beträge in CHF. Die AR-Erklärung hat keine Bundesspalte. Die Steuerverwaltung nimmt die Abweichungen für die direkte Bundessteuer (DBSt) automatisch vor (ar-wl-2025__c0179). Ich habe deshalb Kanton (K) und Bund (B) getrennt gerechnet. Die Steuerbeträge selbst habe ich nicht berechnet, nur die Bemessungsgrundlagen.
> 
> **Ausgangslage:** Person 1 ist Polymechaniker mit Nettolohn 85'300. Person 2 hat einen Nettolohn von 68'200 und arbeitet in St. Gallen. Beide haben eine BVG-Kasse und Säule 3a. Die Kinder sind Lea (Jahrgang 2021, am 31.12.2025 vier Jahre alt) und Jonas (Jahrgang 2009, 16 Jahre alt).
> 
> ## 1. Einkünfte
> 
> | Ziffer (Code) | Inhalt | K | B | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 1.1 (100) | Nettolohn Person 1 | 85'300 | 85'300 | Lohnausweis Ziff. 11. Ziff. 1.1, ar-wl-2025__c0035 |
> | 1.1 (102) | Nettolohn Person 2 | 68'200 | 68'200 | Ziff. 11 (inkl. Kinder- und Ausbildungszulagen aus Ziff. 8). Ziff. 1.1 und 3.5, ar-wl-2025__c0054 |
> | 4.1 (146) | Wertschriften- und Guthabenerträge | 1'410 | 1'410 | Form. 2: Dividenden 1'250 (Spalte A, mit VSt) + Konto-Zins 160 (Spalte B). Ziff. 4.1, ar-form-02-2025__c0007 |
> | 7 (168) | Total Einkünfte | 154'910 | 154'910 | 85'300 + 68'200 + 1'410 |
> 
> Hinweise:
> - Die Kinder- und Ausbildungszulagen sind im Lohn von Person 2 enthalten. Sie gehören nicht zusätzlich unter Ziff. 3.5. Ziff. 3.5 gilt nur für Zulagen, die die Ausgleichskasse direkt auszahlt.
> - Verrechnungssteuer-Anspruch (VSt) auf den Dividenden: 35 % × 1'250 = **437.50**. Er wird im Form. 2 geltend gemacht.
> - Die Dividenden stammen aus Aktien unter 10 %. Deshalb gehen sie nicht in Ziff. 4.2 oder 16.7 (Teilbesteuerung).
> 
> ## 2. Berufskosten (Form. 4, Total in Ziff. 10)
> 
> | Position | Person 1 K | Person 1 B | Person 2 K | Person 2 B | Rechenweg |
> |---|---|---|---|---|---|
> | Ziff. 1.1 Fahrkosten ÖV | 0 | 0 | 1'260 | 1'260 | P1: Lohnausweis Feld F angekreuzt, daher kein Fahrkostenabzug. P2: Abo Herisau–St. Gallen. Code 450. ar-wl-2025__c0074/c0075 |
> | Ziff. 2.1 / 2.2 Verpflegung | 1'600 | 1'600 | 2'640 | 2'640 | P1: Feld G (Kantine) → 7.50 × 220 = 1'650, gedeckelt auf **1'600** (Ziff. 2.2). P2: 15 × 176 Arbeitstage = 2'640, unter Max. 3'200 (Ziff. 2.1). Bund gleiche Ansätze: bund-bkv-2025__anhang-1 |
> | Ziff. 3 Übrige Berufskosten | 2'400 | 2'559 | 2'400 | 2'046 | K: 700 + 10 % Nettolohn, Max. 2'400. B: 3 % Nettolohn, Min. 2'000, Max. 4'000. Ziff. 10.1 |
> | **Total Berufskosten** | **4'000** | **4'159** | **6'300** | **5'946** | P1 → Ziff. 10.1 (Code 438); P2 → Ziff. 10.2 (Code 488) |
> 
> Gesamt Berufskosten: **K 10'300 | B 10'105**
> 
> ## 3. Abzüge
> 
> | Ziffer | Inhalt | K | B | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 10.1 / 10.2 | Berufskosten | 10'300 | 10'105 | Siehe Abschnitt 2 |
> | 13.1 | Säule 3a | 12'258 | 12'258 | P1: 7'258 (Max. mit 2. Säule). P2: 5'000 (bezahlt, unter Max.). ar-wl-2025__c0003 |
> | 13.2 | BVG-Einkauf | 0 | 0 | Der Einkauf von 4'000 wurde bereits als Lohnausweis Ziff. 10.2 vom Lohn abgezogen. Probe: 82'000 − 5'740 − 4'060 − 4'000 = 68'200. Nicht doppelt abziehen (ar-wl-2025__c0084) |
> | 14 | Versicherungsprämien und Sparzinsen | 7'400 | 5'100 | A = Krankenkasse 13'900 + Sparzinsen 160 = 14'060. B: K 5'400 + 2 × 1'000 (Kinder) = 7'400. B: 3'700 + 2 × 700 = 5'100 (mit 2./3. Säule). Abzug = min(A, B). ar-form-06-2025__c0001/c0002 |
> | 16.2 | Kinderbetreuung (Lea) | 10'200 | 10'200 | 14'400 − Mittagessen 1'800 − Betreuungsbeitrag 2'400 = 10'200. Max. 25'000 (K) / 25'800 (B). Lea ist unter 14. ar-form-10-2025__c0001 |
> | 17 | Zweiverdienerabzug | 5'200 | 14'100 | Basis ist das tiefere Erwerbseinkommen (P2). K: 68'200 − 6'300 − 5'000 = 56'900; 10 % = 5'690, Max. **5'200**. B: 68'200 − 5'946 − 5'000 = 57'254; 50 % = 28'627, Max. **14'100**. ar-wl-2025__c0004 |
> | 18 | Total Abzüge | 45'358 | 51'763 | Summen der Zeilen oben |
> 
> ## 4. Netto-, Reineinkommen und steuerbares Einkommen
> 
> | Ziffer | Inhalt | K | B | Rechenweg |
> |---|---|---|---|---|
> | 7 | Total Einkünfte | 154'910 | 154'910 | Abschnitt 1 |
> | 18 | Total Abzüge | 45'358 | 51'763 | Abschnitt 3 |
> | 20 | Nettoeinkommen | 109'552 | 103'147 | 7 − 18 |
> | 21.1 | Krankheitskosten | 0 | 0 | Keine Belege vorhanden |
> | 21.3 | Spenden (Krebsliga) | 300 | 300 | Min. 100 erfüllt; Max. 20 % des Nettoeinkommens nicht erreicht. ar-form-05-2025__c0003 |
> | 22 | Reineinkommen | 109'252 | 102'847 | 20 − 21 |
> | 23.2 | Kinderabzug Lea (4.–15. Altersjahr) | 7'400 | 6'800 | K 7'400 (ar-wl-2025__c0005). B 6'800 |
> | 23.3 | Kinderabzug Jonas (ab 15. Altersjahr, Ausbildung) | 11'600 | 6'800 | K 11'600 (Kantonsschule). B 6'800 |
> | 24 | Ehegattenabzug | – | 2'800 | Nur Bund (Ziff. 24, Verheiratete) |
> | **24** | **Steuerbares Einkommen** | **90'252** | **86'447** | K: 109'252 − 19'000. B: 102'847 − 13'600 − 2'800 |
> 
> ## 5. Vermögen (nur Kanton, Bund hat keine Vermögenssteuer)
> 
> | Ziffer | Inhalt | Betrag | Rechenweg / Fundstelle |
> |---|---|---|---|
> | 30.1 (300) | Wertschriften 38'000 + Bankguthaben 54'000 | 92'000 | Steuerwert per 31.12.2025 (ar-wl-2025__c0113) |
> | 33 | Total Vermögenswerte | 92'000 | |
> | 34 | Schulden | 0 | Keine vorhanden |
> | 35 | Reinvermögen | 92'000 | |
> | 36.2 (332) | Sozialabzug Ehegatten | 150'000 | ungetrennte Ehe (ar-wl-2025__c0122) |
> | 36.3 (334) | Sozialabzug Kinder | 50'000 | 2 × 25'000 (beide minderjährig am 31.12.2025) |
> | 37 | Steuerbares Vermögen | **0** | max(0; 92'000 − 200'000) |
> 
> ## 6. Nicht zu deklarieren oder nicht abziehbar
> 
> - **Schlussrechnung 2024 Staats-, Gemeinde- und Bundessteuer (9'870):** Steuern sind nicht abziehbar (Art. 37 Abs. 1 lit. e StG AR, ar-stg__art-37).
> - **Handy-Abo (960):** Lebenshaltung, nicht abziehbar (Art. 37 Abs. 1 lit. a StG AR).
> - **Turnverein-Mitgliederbeitrag (120):** Mitgliederbeiträge sind nicht abziehbar (Ziff. 21.3, ar-wl-2025__c0102). Nur Spenden an steuerbefreite Institutionen zählen.
> - **Kita-Mittagessen (1'800):** Verpflegung ist bei Kinderbetreuung ausgeschlossen (Form. 10).
> - **Kita-Betreuungsbeitrag (2'400):** Keine Einnahme. Er wird bei den Betreuungskosten abgezogen (Form. 10).
> - **Kinderzulagen:** Sind bereits im Lohn (Nettolohn P2) enthalten. Nicht doppelt erfassen.
> - **BVG-Einkauf (4'000):** Bereits im Nettolohn abgezogen. Nicht unter Ziff. 13.2 und nicht nochmals bei Ziff. 17.
> - **Säule 3a-Guthaben (12'258):** Nicht im Vermögen, solange es nicht fällig ist. Nur Lebensversicherungen mit Rückkaufswert gehören in Ziff. 30.3.
> - **Verrechnungssteuer (437.50):** Keine Einnahme. Sie wird als Anspruch im Form. 2 geltend gemacht.
> - **Eigenmietwert / Mietzins:** Keine, da Mieter.
> - **Personalkantine (Feld G) und Werkbus (Feld F):** Keine separate Einnahme. Sie wirken nur über den Abzugsausschluss beim Fahrkosten- und Verpflegungsabzug.
> 
> ## 7. Offene Punkte und Prüfpunkte
> 
> 1. **Krebsliga Ostschweiz:** Die Spende (300) ist nur abziehbar, wenn die Institution in der Schweiz steuerbefreit ist. Bitte die Bestätigung oder den Status prüfen.
> 2. **Verpflegung Person 2:** Der Abzug von 15 pro Arbeitstag setzt Mehrkosten voraus. Im Bund entfällt er, wenn die Hauptmahlzeit höchstens 10 kostet (bund-bkv-2025__anhang-1). Die Kosten des Mittagessens fehlen noch.
> 3. **Krankheitskosten (Ziff. 21.1):** Keine Belege vorhanden. Falls Kosten angefallen sind, Form. 6 S. 2 erfassen. Der Selbstbehalt beträgt 5 % des Nettoeinkommens.
> 4. **Codes:** Die Hauptformular-Codes für Ziff. 10.2, 13.1, 14, 16.2 und 17 sind nicht verifiziert (die Formularseite 3 fehlt in der Wegleitung). Am Originalformular gegenprüfen.
> 5. **Zweiverdienerabzug:** Die Berechnung folgt der Lesart, dass der BVG-Einkauf nicht erneut vom Erwerbseinkommen abgezogen wird, weil er im Nettolohn schon enthalten ist. Das ist eine Auslegung, die eine Fachperson bestätigen sollte.
> 6. **Arbeitsort St. Gallen (Person 2):** Ich habe nicht geprüft, ob daraus Auswirkungen auf die Besteuerung entstehen. Die Wohnsitzgemeinde im Kanton AR ist massgebend. Bitte bestätigen.
> 7. **Status der Werte:** Die meisten Angaben sind laut Steuer-Wiki «agent-geprüft, Abnahme offen». Die Fachperson sollte die Abnahme vornehmen.
> 8. **Belege beilegen:** Lohnausweise beider Personen, Bescheinigungen Säule 3a (beide), Einkaufsbescheinigung mit Einkaufsberechnung, Bankauszug (Steuerauszug), Krankenkassen-Prämienrechnung, Kita-Abrechnung, Spendenquittung, ÖV-Abo.
> 
> Wenn du mir die Originalformularnummern (Seite 3) oder die fehlenden Angaben zu Mittagessen und Krankheitskosten gibst, kann ich die Liste ergänzen.

