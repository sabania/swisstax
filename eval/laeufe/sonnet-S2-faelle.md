# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 17:52
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


**Antwort des Agenten** (152.1 s · Tools: 36 Aufrufe read, steuerwiki__formular, read, steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, message, steuerwiki__rechne):

> # Ausfüllhilfe ZH 2025: Ehepaar Marco und Sandra, Winterthur
> 
> **Formular:** StA Form. 300 mit Hilfsblättern 340, 360 und 365. Beträge in CHF, Staatssteuer (St) und Bundessteuer (Bu) getrennt.
> **Status aller Werte:** ☑️ agent-geprüft, Abnahme durch die Fachperson offen. Alle Rechnungen sind mit `rechne` geprüft.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | St | Bu | Beleg und Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb Marco | 103'000 | 103'000 | Lohnausweis Ziff. 11 (118'400 − 8'110 − 7'290) | zh-form-300-2025__c0004 |
> | 1.1 | 101 | Haupterwerb Sandra | 67'200 | 67'200 | Lohnausweis Ziff. 11 (76'800 − 5'260 − 4'340). Die Kinderzulagen von 4'800 sind darin enthalten. | zh-form-300-2025__c0004 |
> | 4.1 | 150 | Wertschriftenertrag (Form. 340) | 1'140 | 1'140 | Kolonne A: Dividenden 960 (Verrechnungssteuer 35 % = 336, Code 540). Kolonne B: Sparzins 180 (unter 200, ohne Verrechnungssteuer). Privatkonto: 0. | zh-form-340-2025__c0005, zh-wl-2025__c0168 |
> | **7** | 199 | **Total Einkünfte** | **171'340** | **171'340** | 103'000 + 67'200 + 1'140 | |
> 
> Die Verrechnungssteuer von 336 wird im Wertschriftenverzeichnis zurückverlangt. IBAN angeben und das Verzeichnis unterschreiben.
> 
> ## 2. Abzüge
> 
> **Form. 360 Marco (Code 220 → Ziff. 11.1)**
> 
> | Teilziffer | Code | St | Bu | Rechenweg |
> |---|---|---|---|---|
> | 1.1 ÖV-Abo | 201 | 4'180 | 3'300 | Bund begrenzt auf 3'300 (Kanton 5'200). Das kürzt den Bundesabzug um 880. |
> | 2.1 Verpflegung voll | 208 | 3'200 | 3'200 | 220 Tage × 15 = 3'300, Jahresmaximum 3'200 |
> | 3 Übrige Berufskosten | 212 | 3'090 | 3'090 | 3 % × 103'000, innerhalb min. 2'000 und max. 4'000 |
> | **Total** | **220** | **10'470** | **9'590** | |
> 
> **Form. 360 Sandra (Code 240 → Ziff. 11.2)**
> 
> | Teilziffer | Code | St | Bu | Rechenweg |
> |---|---|---|---|---|
> | 1.2 Velo | 222 | 700 | 700 | Pauschale für ständige Benützung des eigenen Velos, kein Nachweis nötig |
> | 2.1 Verpflegung verbilligt | 226 | 1'320 | 1'320 | Feld G angekreuzt: 176 Tage × 7.50, Jahresmaximum 1'600 |
> | 3 Übrige Berufskosten | 232 | 2'016 | 2'016 | 3 % × 67'200, über dem Minimum von 2'000 |
> | **Total** | **240** | **4'036** | **4'036** | |
> 
> Fundstellen: zh-form-360-2025__c0001 bis c0005, zh-wl-2025__c0066, c0067, c0068, zh-pauschalierung-berufsauslagen-2025__c0004. Die Pauschale von 3 % ersetzt nur die übrigen Berufskosten. Fahrkosten und Verpflegung kommen dazu.
> 
> **Hauptformular**
> 
> | Ziff. | Code | Position | St | Bu | Rechenweg und Regel | Fundstelle |
> |---|---|---|---|---|---|---|
> | 11.1 | 220 | Berufsauslagen Marco | 10'470 | 9'590 | siehe oben | zh-form-300-2025__c0007 |
> | 11.2 | 240 | Berufsauslagen Sandra | 4'036 | 4'036 | siehe oben | zh-form-300-2025__c0007 |
> | 14.1 | 260 | Säule 3a Marco | 7'258 | 7'258 | Bescheinigung 7'258, mit 2. Säule maximal 7'258 | zh-wl-2025__c0081 |
> | 14.2 | 261 | Säule 3a Sandra | 7'258 | 7'258 | wie oben | zh-wl-2025__c0081 |
> | 15 | 270 | Versicherungsprämien und Sparzinsen (Form. 365) | 8'400 | 5'100 | Teil A: 15'840 + 180 = 16'020. Teil B St: 5'800 + 2 × 1'300 = 8'400. Teil B Bu: 3'700 + 2 × 700 = 5'100. Abzug = der tiefere Betrag von A und B. | zh-form-365-2025__c0001, c0002 |
> | 16.1 | 280 | PK-Einkauf Marco | 10'000 | 10'000 | Bescheinigung beilegen. Ziff. 10.2 im Lohnausweis ist 0, also keine Doppelzählung. | zh-wl-2025__c0092 |
> | 16.3 | 283 | Vermögensverwaltung | 93.60 | 0 | St: 3 ‰ × 31'200 (nur das Depot). Bu: keine Pauschale belegt, siehe Hinweis 5. | zh-wl-2025__c0095 |
> | 16.6 | 376 | Fremdbetreute Kinder | 31'900 | 32'700 | Lena: min(27'300; 25'000 bzw. 25'800). Noah: 6'900, unter dem Maximum. | zh-form-300-2025__c0008, zh-stg-2025__par-31-t4 |
> | 17 | 290 | Zweiverdienerabzug | 6'100 | 14'100 | Basis = tieferes Erwerbseinkommen (Sandra) = 67'200 − 4'036 − 7'258 = 55'906. St: min(55'906; 6'100). Bu: 50 % = 27'953, gedeckelt auf 14'100. | zh-wl-2025__c0112 |
> | **18** | 299 | **Total Abzüge** | **85'515.60** | **90'042** | | |
> 
> Die Krankenkassenprämie von 15'840 enthält Grund- und Zusatzversicherung und gehört in Code 601. Sie ist keine individuell verbilligte Prämie, also ist Code 605 leer.
> 
> ## 3. Nettoeinkommen bis steuerbares Einkommen
> 
> | Ziff. | Code | Position | St | Bu | Rechenweg |
> |---|---|---|---|---|---|
> | 19 / 20 | 199 / 299 | Einkünfte / Abzüge | 171'340 / 85'515.60 | 171'340 / 90'042 | |
> | **21** | 310 | **Nettoeinkommen** | **85'824.40** | **81'298** | |
> | 22.1 | 320 | Krankheitskosten | **0** | **0** | Zahnarzt 1'850 + Kostenbeteiligung 1'240 = 3'090. Selbstbehalt 5 % = 4'291.22 (St) bzw. 4'064.90 (Bu). Die Kosten liegen darunter, es gibt keinen Abzug. |
> | 22.2 | 324 | Spenden | 650 | 650 | Rotes Kreuz 400 + UNICEF 250. Mindestens 100 erreicht, Maximum 20 % × Netto (17'164.88 bzw. 16'259.60). Aufstellung beilegen. |
> | **23** | 350 | **Reineinkommen** | **85'174.40** | **80'648** | |
> | 24.1 | 370 | Kinder im Haushalt (2) | 18'600 | 13'600 | 2 × 9'300 bzw. 2 × 6'800 |
> | 24.3 | 365 | Verheiratetenabzug | – | 2'800 | nur Bundessteuer |
> | **25 / 27** | 390 / 398 | **Steuerbares Einkommen** | **66'574.40** | **64'248** | |
> 
> Fundstellen: zh-form-370__c0004, zh-wl-2025__c0122, bund-dbg-2025__art-33a, zh-wl-2025__c0126, c0135.
> 
> **Plausibilität:** Das steuerbare Einkommen Bund liegt 2'326 unter dem Kanton. Das erklären der höhere Zweiverdienerabzug (+8'000), der Verheiratetenabzug (+2'800) und die höhere Drittbetreuung (+800). Dagegen wirken der höhere Kinderabzug im Kanton (5'000), der höhere Versicherungsabzug (3'300) und die gekürzten Fahrkosten im Bund (880). Das ist stimmig.
> 
> ## 4. Vermögen
> 
> | Ziff. | Code | Position | CHF | Beleg |
> |---|---|---|---|---|
> | 30.1 | 400 | Wertschriften und Guthaben (Form. 340) | 82'000 | Sparkonto 42'500 + Privatkonto 8'300 + Depot 31'200 |
> | 33 / 35 / 37 | 460 / 490 / 498 | Total, steuerbares Vermögen (Kanton) | 82'000 | Schulden: keine belegt |
> 
> Die Bundessteuer kennt keine Vermögenssteuer. Das steuerfreie Vermögen wirkt nur im Tarif und wird nicht abgezogen (Fundstelle: Formular-Gerüst).
> 
> ## 5. Nicht zu deklarieren oder kein Abzug
> 
> - **Swisscom-Handy 1'080 (privat):** keine abziehbare Position. Ein beruflicher Anteil wäre in der 3-%-Pauschale enthalten.
> - **Hausrat- und Haftpflichtversicherung 465:** keine abziehbare Position in Form. 365 (Codes 601–604). Selbst wenn man sie berücksichtigte, bliebe der Abzug auf das Maximum begrenzt.
> - **Kinderzulagen 4'800:** nicht zusätzlich unter Ziff. 3.4 erfassen. Sie stecken schon im Nettolohn von Sandra. Ziff. 3.4 gilt nur für Zulagen, die direkt von der Ausgleichskasse ausbezahlt werden.
> - **AHV-, PK- und NBUV-Beiträge laut Lohnausweis (Ziff. 9, 10.1):** schon im Nettolohn abgezogen, nicht nochmals abziehen.
> - **PK-Guthaben und Säule-3a-Guthaben:** bis zur Fälligkeit kein Vermögen, nicht deklarieren (zh-wl-2025__c0154).
> - **Krankheitskosten 3'090:** kein Abzug, siehe Ziff. 22.1. Die Formular-370-Aufstellung ist nicht nötig.
> - **Bund, Ermässigung 263 je Kind (Art. 36 DBG):** kein Formularfeld, wird bei der Veranlagung berücksichtigt.
> - **Miete:** kein Abzug, es gibt keine Liegenschaft und keinen Eigenmietwert.
> - **Verrechnungssteuer 336:** kein Einkommen, nur als Rückforderung zu beantragen.
> 
> ## 6. Offene Punkte und Annahmen für die Fachperson
> 
> 1. **Marco, Verpflegung:** Ich nehme an, dass die Mittagspause die Heimkehr von Zug nach Winterthur nicht erlaubt. Sonst entfällt der Abzug von 3'200 (St und Bu). Beim Bund gibt es zudem keinen Abzug, wenn die Hauptmahlzeit höchstens 10 Fr. kostet. Rückfrage: Wo isst Marco in Zug, und was kostet das Mittagessen?
> 2. **Hort Noah, 6'900:** Der Betrag ist abziehbar, soweit er Betreuung ist. Verpflegung oder Schulgeld wären nicht betreuungsbedingt. Bitte die Rechnung auf einen Verpflegungsanteil prüfen und ihn gegebenenfalls kürzen.
> 3. **Kita Lena:** Die Kosten von 27'300 werden bei 25'000 (St) und 25'800 (Bu) gekappt. Die Aufstellung der bezahlten Kosten mit Empfängern ist unaufgefordert beizulegen. Die Rechnungen kommen erst auf Verlangen.
> 4. **Spenden:** Ich habe die Steuerbefreiung beider Empfänger von Ihnen übernommen. Im ZH-Verzeichnis der steuerbefreiten Institutionen habe ich sie nicht nachgeprüft. Die Spendenquittungen auf Nachfrage bereithalten.
> 5. **Vermögensverwaltungskosten Bund (Code 283):** Für den Bund ist keine Pauschale im Wiki belegt, deshalb 0. Eine Kantonspauschale in der Bundesspalte wäre nur mit Vorbehalt möglich. Der Entscheid liegt bei der Fachperson. Das Kantonsbetrag 93.60 wird im Formular ohne Rappen eingetragen, Rundung ebenfalls Fachperson.
> 6. **PK-Einkauf:** Ein Kapitalbezug innert drei Jahren nach dem Einkauf würde den Abzug rückwirkend gefährden (zh-wl-2025__c0092). Das ist für die Zukunft zu beachten.
> 7. **Vermögen:** Bargeld, Fahrzeuge, Lebens- oder Rentenversicherungen mit Rückkaufswert und Schulden sind nicht belegt. Rückfrage, ob solche Posten existieren, falls ja, in Ziff. 30.2–30.6 bzw. 34 ergänzen.
> 8. **Seite 1:** Beide Kinder mit Geburtsdatum erfassen (Lena 2021, Noah 2016), jeweils im Haushalt.
> 9. **Beizulegende Belege:** beide Lohnausweise, Form. 360 je Person, Form. 365, Form. 340 mit Steuerauszug ZKB, 3a-Bescheinigungen, PK-Einkaufsbescheinigung, Kita-/Hort-Aufstellung, Spendenliste.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

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


**Antwort des Agenten** (136.2 s · Tools: 36 Aufrufe read, steuerwiki__formular, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__wert, steuerwiki__rechne):

> Ich habe die Ziffern und Limiten aus dem Wiki beisammen. Jetzt rechne ich die Totale nach und prüfe noch Ziff. 16.1 (Verwaltungskosten Wertschriften).
> 
> # Ausfüllhilfe SG 2025: Nadine (alleinerziehend, 1 Kind)
> 
> Alle Werte sind im Wiki als ☑️ agent-geprüft geführt (Fundstelle geprüft, Abnahme offen). Das SG-Formular hat nur eine Spalte. Die Bundesabweichungen nimmt das Steueramt automatisch vor (sg-wl-2025__c0173), hier sind sie zur Kontrolle ausgewiesen. Alle Rechnungen sind mit `rechne` geprüft.
> 
> ## Einkünfte
> 
> | Ziff. / Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 1.1 / 100 | Nettolohn | 73'000 | 73'000 | Lohnausweis Ziff. 11, nicht Ziff. 8. 83'500 − 5'890 − 4'610 = 73'000. Die Kinderzulage 2'400 steckt bereits im Lohn (sg-wl-2025__c0042). |
> | 6.1 / 156 | Kinderalimente erhalten | 9'600 | 9'600 | 12 × 800. Steuerbar beim Empfänger (sg-wl-2025__c0068, bund-ks-30__c0100). Beim erstmaligen Deklarieren Scheidungsurteil und Zahlungsnachweis beilegen (sg-wl-2025__c0084). |
> | 4.1 / 146 (Form. 2) | Bruttozins Raiffeisen | 68 | 68 | Spalte B, da kein VSt-Abzug und Zins unter 200 (sg-wl-2025__c0135). |
> | **7 / 168** | **Total Einkünfte** | **82'668** | **82'668** | 73'000 + 9'600 + 68 |
> 
> ## Abzüge
> 
> **Ziff. 10.1 / Code 438: Berufskosten (Form. 4)**
> 
> Lohnausweis Feld F und G sind nicht angekreuzt, also kein Ausschluss.
> 
> | Form. 4 | Staat | Bund | Rechenweg |
> |---|---|---|---|
> | 1.3 Fahrkosten Auto (Code 404/406) | 8'000 | 3'300 | 32 km × 2 × 220 Tage = 14'080 km × 0.70 = 9'856. Gedeckelt bei Staat 8'000 und Bund 3'300 (sg-form-4-2025__c0002). Begründung ankreuzen: kein ÖV zumutbar, erste Verbindung 06:40, Arbeitsbeginn 06:00 (sg-wl-2025__c0077). |
> | 2.1 Verpflegung (Code 408) | 3'200 | 3'200 | 15 × 220 = 3'300, Maximum 3'200 (sg-wl-2025__c0078). |
> | 3.1 Übrige Berufskosten (Code 416) | 2'400 | 2'190 | Staat: min(700 + 10 % × 73'000; 2'400). Bund: 3 % × 73'000 = 2'190, Minimum 2'000 (sg-wl-2025__c0080). |
> | **6 Total** | **13'600** | **8'690** | |
> 
> **Übrige Abzüge**
> 
> | Ziff. / Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 13.1 / 208 | Säule 3a | 7'258 | 7'258 | Maximum mit 2. Säule 7'258. Bescheinigung beilegen (sg-wl-2025__c0085). |
> | 13.2 / 218 | PK-Einkauf | 6'000 | 6'000 | Selbst überwiesen, im Lohnausweis steht Ziff. 10.2 = 0, also kein Doppelabzug. Bescheinigung und Einkaufsberechnung beilegen (sg-wl-2025__c0086). Die ordentlichen BVG-Beiträge 4'610 nicht nochmals abziehen. |
> | 14 / 600 (Form. 6) | Versicherungsprämien | 4'500 | 2'500 | A = 5'280 + 1'320 + 68 Sparzins − 1'800 IPV = 4'868. Maximum B: Staat 3'400 + 1'100 Kind = 4'500, Bund 1'800 + 700 = 2'500. Abzug = min(A; B). Kein Zuschlag «ohne Vorsorge», weil 3a und BVG abgezogen werden (sg-form-6-2025__c0002). |
> | 16.2 / 258 (Form. 10) | Kinderbetreuung | 8'760 | 8'760 | 9'840 − 1'080 Mahlzeiten (sg-wl-2025__c0092). Limite 26'700 bzw. 25'800 ist nicht erreicht. |
> | 16.4 / 223 | Weiterbildung Excel-Kurs | 400 | 340 | Staat: Pauschale 400 ist höher als der effektive Betrag 340. Bund: nur effektive Kosten (sg-wl-2025__c0094). |
> | **18 / 230** | **Total Abzüge** | **40'518** | **33'548** | |
> 
> Die Berechnung der Totale: Staat 13'600 + 7'258 + 6'000 + 4'500 + 8'760 + 400 = 40'518. Bund 8'690 + 7'258 + 6'000 + 2'500 + 8'760 + 340 = 33'548.
> 
> ## Einkommensberechnung
> 
> | Ziff. / Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|
> | **20 / 234** | **Nettoeinkommen** | **42'150** | **49'120** | 82'668 − Total Abzüge |
> | 21.1 / 650, 238, 240 | Krankheitskosten (Form. 6 Rückseite) | Vorkolonne 3'600, Selbstbehalt 843, Abzug **2'757** | Vorkolonne 3'600, Selbstbehalt 2'456, Abzug **1'144** | 850 Franchise/Selbstbehalt + 2'750 Zahnarzt = 3'600. Selbstbehalt Staat 2 % × 42'150, Bund 5 % × 49'120 (sg-wl-2025__c0098). |
> | 21.3 / 244 | Spenden | 0 | 0 | 80 liegt unter der Mindestschwelle von 100. |
> | **22 / 248** | **Reineinkommen** | **39'393** | **47'976** | |
> | 23.2 / 254 | Kinderabzug Elias | 10'800 | 6'800 | Der Kindergarten zählt zur Schulpflicht, also 23.2 und nicht 23.1 (sg-wl-2025__c0104). Beim Bund kommt zusätzlich eine Steuerbetrags-Ermässigung von 263 pro Kind dazu, die das Amt automatisch macht. |
> | **24 / 268** | **Steuerbares Einkommen** | **28'593** | **41'176** | |
> 
> ## Vermögen (nur Staat)
> 
> | Ziff. / Code | Position | Betrag | Rechenweg |
> |---|---|---|---|
> | 30.1 / 300 | Sparkonto | 31'500 | Steuerwert 31.12.2025 aus Form. 2 |
> | 30.4 / 306 | Motorfahrzeug | **offen** | Anschaffungswert − 20 % pro Jahr seit Erwerb. Kaufpreis und Jahr fehlen (sg-wl-2025__c0111). |
> | 36.1 / 330, 36.3 / 334 | Sozialabzüge | 75'000 + 20'000 = 95'000 | alleinstehend plus 1 Kind (sg-stg-2025__art-64) |
> | 37 / 338 | Steuerbares Vermögen | 0 | Das Reinvermögen 31'500 liegt unter 95'000. Das ändert sich nur, wenn der Fahrzeugwert über 63'500 liegt, was unwahrscheinlich ist. |
> 
> ## Nicht zu deklarieren oder nicht abziehbar
> 
> - **Motorfahrzeugsteuer 410, Auto-Haftpflicht/Kasko 1'020:** nicht abziehbar. Motorfahrzeug- und Haftpflichtversicherungen sind bei Ziff. 14 ausdrücklich ausgeschlossen. Beim Arbeitsweg zählt nur der Kilometersatz von 0.70.
> - **Handy-Abo 720:** kein eigener Abzug. Es gilt die Pauschale für übrige Berufskosten (3.1). Dass das Handy darin enthalten ist, ist im Wiki nicht ausdrücklich belegt.
> - **Spende Caritas 80:** unter 100, kein Abzug.
> - **Kita-Mahlzeiten 1'080:** Verpflegung ist nicht abziehbar.
> - **Prämienverbilligung 1'800:** kein Einkommen, sie wird nur in Form. 6 Teil A.e von den Prämien abgezogen.
> - **Kinderzulage 2'400:** nicht separat unter Ziff. 3.5 aufführen. Sie steckt schon im Nettolohn.
> - **AHV/ALV 5'890 und ordentliche BVG 4'610:** schon im Nettolohn berücksichtigt.
> - **Krankenkassenprämien:** gehören nicht in die Krankheitskosten, sondern in Ziff. 14.
> - **Pensionskassen- und 3a-Guthaben:** kein steuerbares Vermögen (sg-wl-2025__c0107).
> - **Ziff. 16.1 Verwaltungskosten:** 0. Es gibt ein Sparkonto, kein Depot, und keine Gebühren sind belegt.
> - **Ziff. 17 Zweiverdienerabzug:** nicht anwendbar, es gibt keinen Ehepartner.
> 
> ## Offene Punkte und Annahmen
> 
> 1. **Fahrzeugwert** (Ziff. 30.4) fehlt. Bitte Anschaffungswert und Erwerbsjahr nachliefern.
> 2. **Fahrkosten mit dem Auto:** Die Begründung (ÖV ab 06:40, Arbeitsbeginn 06:00) in Form. 4 ankreuzen. Wird sie nicht akzeptiert, sind nur die ÖV-Kosten abziehbar. Dann bräuchte es den Abopreis der Strecke.
> 3. **Kinderbetreuung:** Das Formular 10 braucht Vorname des Kindes, Beträge sowie Name und Adresse der Kita. Beim Bund ist Betreuung ausserhalb der Arbeitszeit nicht abziehbar. Es ist zu prüfen, ob die Kita-Zeiten mit den Arbeitszeiten übereinstimmen. Ohne separaten Mahlzeitenausweis hätte der Staat pauschal 8 Franken pro Tag gekürzt. Hier ist er ausgewiesen.
> 4. **Prämienverbilligung:** Angenommen sind Bruttoprämien. Das Ergebnis bleibt aber auch bei Nettoprämien gleich, weil das Maximum (4'500 bzw. 2'500) greift.
> 5. **Weiterbildung (16.4):** Voraussetzung ist ein erster Abschluss auf Sekundarstufe II oder das vollendete 20. Altersjahr. Das wird als erfüllt angenommen.
> 6. **PK-Einkauf:** Es gilt ein Abzugsverbot bei Einkauf mit vorzeitig bezogenen, nicht versteuerten Kapitalleistungen. Das Einkaufspotenzial bestätigt die Einkaufsberechnung der PK.
> 7. **Kinderabzug:** Er steht Nadine zu, weil Elias bei ihr lebt und der Ex-Mann die Alimente nach Ziff. 12.2 abzieht (sg-wl-2025__c0104). Die tarifliche Behandlung als Alleinerziehende ist nicht geprüft.
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


**Antwort des Agenten** (131.3 s · Tools: 36 Aufrufe read, steuerwiki__formular, steuerwiki__position, steuerwiki__zeige, steuerwiki__wert, steuerwiki__suche, message, steuerwiki__beleg, steuerwiki__ablage, steuerwiki__rechne):

> **Ausfüllhilfe TG 2025 (Staats-/Gemeindesteuer und direkte Bundessteuer)**
> 
> Mandantin: verwitwete Rentnerin, alleinstehend, Wohnsitz Frauenfeld TG, EFH selbst bewohnt. Formular 1 hat links die Spalte Staat und rechts die Spalte Bund (tg-wl-2025__c0196). Alle Positionen haben den Status ☑️ (Fundstelle geprüft, Abnahme offen). Beträge in CHF, alle Rechnungen mit `rechne`.
> 
> ## Einkünfte
> 
> | Ziffer / Code | Position | Staat | Bund | Beleg | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 3.1 / 130 | AHV-Rente | 27'000 | 27'000 | AHV-Bescheinigung | 12 × 2'250, zu 100 % steuerbar (tg-form-01-2025__c0007, tg-wl-2025__c0076) |
> | 3.2 / 132 | PK-Rente, Bruttobetrag 10'800, 100 % | 10'800 | 10'800 | PK-Bescheinigung | Rentenbeginn 2020, daher kein 80-%-Übergangsrecht (tg-wl-2025__c0077) |
> | 4 / 150 | Wertschriften- und Zinserträge (Übertrag aus Form. 2) | 2'160 | 2'350 | TKB-Steuerauszug | siehe Form. 2 unten |
> | 6 / 175 | Zwischentotal | 39'960 | 40'150 | | |
> | 8.1 / 180 | Liegenschaften (Übertrag aus Form. 7) | 4'840 | 8'920 | Schätzung, Handwerkerrechnungen | siehe Form. 7/8 unten |
> | 9 / 198 | **Total Einkünfte** | **44'800** | **49'070** | | |
> 
> **Form. 2 (Wertschriftenverzeichnis)**
> - Sparkonto: Steuerwert 48'000, Bruttozins 250. Das ist über Fr. 200, also Spalte 8 (mit Verrechnungssteuer).
> - Depot: Steuerwert 95'000, Dividenden 2'100, ebenfalls Spalte 8.
> - Total Erträge Spalte 8: 2'350. Der Verrechnungssteueranspruch (Ziff. 10) ist 35 % davon, also **822.50**. Das entspricht 87.50 + 735, die abgezogen wurden (tg-form-02-2025__c0006, tg-wl-2025__c0167).
> - Vermögensverwaltungskosten, Code 148 (nur Staat): min(2 ‰ × 95'000; 6'000) = **190**. Das Sparkonto zählt nicht zur Bemessung. Ziff. 4 Staat ist damit 2'350 − 190 = 2'160 (tg-wl-2025__c0159).
> - Bund: Eine Bundes-Pauschale ist im Wiki nicht belegt. Ich setze die Bundesspalte deshalb ohne Abzug auf 2'350. Ein Gebührenausweis der TKB würde das ändern (Fachperson).
> 
> **Form. 7/8 (Liegenschaft)**
> - Indexierter Mietwert 20'400.
> - Selbstnutzungsabzug: Staat 40 %, Bund 20 % (tg-wl-2025__c0225, tg-stg § 23). Steuerbarer Eigenmietwert: Staat 12'240, Bund 16'320.
> - Unterhalt, Variante effektiv (Form. 8): Maler (Ersatzanstrich) 6'400 + Gebäudeversicherung 520 + Baumschnitt 480 = **7'400**.
>   - Der Baumschnitt ist abziehbar, weil er mehrjährige Pflanzen und Bäume betrifft (tg-wl-2025__c0228).
>   - Die Gebäudeversicherung ist eine Besitzesabgabe und abziehbar (tg-stp-34-1__c0014).
> - Unterhalt, Variante Pauschale: Das Gebäude ist von 1986 und damit älter als 10 Jahre, also 20 % vom steuerbaren Eigenmietwert (tg-wl-2025__c0238). Das sind Staat 2'448 und Bund 3'264.
> - Die effektiven Kosten sind in beiden Spalten höher, also gilt **effektiv**.
> - Nettoerfolg Staat: 12'240 − 7'400 = **4'840**. Nettoerfolg Bund: 16'320 − 7'400 = **8'920**.
> - Der Einzelbetrag 6'400 liegt über Fr. 1'000, die Rechnungskopie ist beizulegen (tg-wl-2025__c0234).
> 
> ## Abzüge
> 
> | Ziffer / Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 11 / 290 | Schuldzinsen (Form. 4.1, Code 286) | 3'150 | 3'150 | Gläubigerin mit Adresse und Zinssatz angeben. Limite Vermögensertrag + 50'000 ist nicht erreicht (tg-wl-2025__c0171, c0173). |
> | 14 / 330 | Versicherungsprämien und Sparzinsen (Form. 5.2) | 3'500 | 2'700 | Zeile 1: KK 6'240 (keine Prämienverbilligung); Zeile 4: Sparzinsen 250. A5 (Code 324) = 6'490. Maximum B4 (Code 328): Staat 3'500, Bund 2'700, weil keine Beiträge an Säule 2/3a (tg-form-05-2-2025__c0002). Abzug = min(6'490; B4). |
> | 19 / 360 | **Total Abzüge** | **6'650** | **5'850** | 3'150 + 3'500 bzw. 3'150 + 2'700 |
> 
> Nicht zutreffend sind die Ziffern 10, 12, 13, 15.x, 16, 17 und 18. Das sind Berufsauslagen, Unterhaltsbeiträge, Säule 3a, AHV als Nichterwerbstätige, Drittbetreuung, Weiterbildung, Behinderung und Zweiverdiener.
> 
> ## Nettoeinkommen und Abzüge darauf
> 
> | Ziffer / Code | Position | Staat | Bund |
> |---|---|---|---|
> | 22 / 362 | **Nettoeinkommen** (44'800 − 6'650 bzw. 49'070 − 5'850) | **38'150** | **43'220** |
> | 23.1 / 364 | Krankheitskosten (Form. 5.1) | 4'632.50 | 4'379 |
> | 23.2 / 366 | Freiwillige Zuwendungen (Form. 6) | 350 | 550 |
> | 24 / 372 | **Reineinkommen** | **33'167.50** | **38'291** |
> 
> **Ziff. 23.1 (Form. 5.1)**
> - Form. 5.1 A: Franchise und Selbstbehalt 1'000 + Zahnarzt 4'440 + Brille 1'400 = 6'840 (tg-form-05-1-2025__c0001).
> - Form. 5.1 B: Vergütung der Zusatzversicherung für die Brille −300. Selbst getragen sind damit 6'540.
> - Selbstbehalt 5 % vom Nettoeinkommen Ziff. 22: Staat 1'907.50, Bund 2'161.
> - Abzug Staat: 6'540 − 1'907.50 = 4'632.50. Abzug Bund: 6'540 − 2'161 = 4'379.
> - Die Krankenkassenprämien gehören nicht hierher, sondern in Ziff. 14.
> 
> **Ziff. 23.2 (Form. 6)**
> - Spenden: Krebsliga Thurgau 300 + Pro Senectute Thurgau 250 = 550.
> - Staat: Selbstbehalt 200, also 550 − 200 = 350.
> - Bund: Das Total 550 erreicht die Freigrenze von 100, daher ist der ganze Betrag abziehbar. Die Obergrenze (20 % von 43'220 = 8'644) ist nicht erreicht (bund-dbg-2025__art-33a, tg-wl-2025__c0220).
> - Die Spenden liegen unter Fr. 1'000 pro Zuwendung, Quittungen sind deshalb nur auf Verlangen vorzulegen.
> 
> ## Sozialabzüge und steuerbares Einkommen
> 
> | Ziffer / Code | Position | Staat | Bund |
> |---|---|---|---|
> | 25.3 / 388 | Abzug AHV-Rentnerin bzw. verwitwet | 1'000 | kein Abzug |
> | **26 / 398** | **Steuerbares Einkommen** | **32'167.50** | **38'291** |
> 
> - Ziff. 25.3 gilt nur für die Staatssteuer. Das Reineinkommen 33'167.50 liegt in der Tabellenzeile 32'900–33'899 der Wegleitung mit Abzug 1'000 (tg-wl-2025__c0116 und c0117; Formel 4'200 − 200 × 16 = 1'000).
> - Keine Ziff. 25.1, 25.2, 25.4, 28.1 und 28.2.
> 
> ## Vermögen (31.12.2025)
> 
> | Ziffer / Code | Position | CHF |
> |---|---|---|
> | 30.1 / 410 | Wertschriften und Guthaben: Sparkonto 48'000 + Depot 95'000 (Übertrag aus Form. 2) | 143'000 |
> | 31 / 430 | Liegenschaft, Steuerwert (Form. 7) | 410'000 |
> | 33 / 464 | Total Vermögenswerte | 553'000 |
> | 34 / 466 | Schulden: Hypothek (Form. 4.1, Code 455) | 180'000 |
> | 35 / 468 | Reinvermögen | 373'000 |
> | 36.2 / 472 | Steuerfreier Abzug alleinstehend | 100'000 |
> | **37 / 498** | **Steuerbares Vermögen** | **273'000** |
> 
> Das Vermögen gilt nur für den Kanton. Die Bundessteuer hat keine Vermögenssteuer.
> 
> ## Nicht zu deklarieren oder nicht abziehbar
> 
> - **Wintergarten-Anbau 31'000:** Das ist eine Investition und kein Unterhalt (tg-stp-34-1__c0016). Er gehört in Form. 8 in die Spalte «Anlagekosten/Mehrwert», ohne Abzug.
> - **Hausratversicherung 380:** weder Liegenschaftsunterhalt noch Ziff. 14. Der Hausrat ist auch kein Vermögen (tg-wl-2025__c0227).
> - **Serafe 335 und Handyrechnung:** Lebenshaltungskosten, nicht abziehbar.
> - **PK-Rente:** Es gibt kein Guthaben und keine Beiträge. Vorsorgeguthaben wären ohnehin kein Vermögen (tg-wl-2025__c0139).
> - **Krankenkassenprämien in Ziff. 23.1:** nicht dort, sondern nur in Ziff. 14.
> 
> ## Fehlende Belege, offene Punkte und Hinweise für die Fachperson
> 
> 1. **Hypothekargläubigerin:** Für Form. 4.1 fehlen Name und Adresse der Bank sowie der Zinssatz.
> 2. **Handyrechnung:** Ein Betrag ist nicht angegeben, sie hat keinen Einfluss auf die Erklärung.
> 3. **Wintergarten:** Ich habe nicht geprüft, ob der Anbau eine Neuschätzung des Steuerwerts auslöst. Der Steuerwert 410'000 ist aus der Schätzung übernommen. Dazu bitte nachfragen, ebenso wie der Anbau finanziert wurde (Plausibilität Vermögen und Hypothek).
> 4. **Maler «Innenrenovation»:** Ich habe den Ersatzanstrich vollständig als Unterhalt angesetzt. Enthält die Rechnung Verbesserungen oder höheren Komfort, wäre ein geschätzter Teil nicht abziehbar (tg-stp-34-1__c0016, Richtwerte im Merkblatt Liegenschaftenunterhalt).
> 5. **Zahnarzt:** Ich habe keine Vergütung angesetzt. Hat eine Zahnzusatzversicherung etwas bezahlt, muss dieser Betrag in Form. 5.1 B.
> 6. **Liegenschaftensteuerrechnung:** Falls dort eine abziehbare Besitzesabgabe (Liegenschaftensteuer) enthalten ist, gehört sie in Form. 8. Davon ist keine in den Zahlen oben enthalten.
> 7. **Bund, Vermögensverwaltungskosten:** siehe Form. 2 oben, nur mit Gebührenausweis möglich.
> 8. **Sparzinsen Form. 5.2 Zeile 4:** Ich habe den Bruttozins 250 angesetzt. Das ändert nichts am Ergebnis, weil A5 (6'490) in jedem Fall über dem Maximum liegt.
> 9. **Plausibilität:** Das steuerbare Einkommen Bund (38'291) liegt über dem Staat (32'167.50). Das ist erklärbar: Der Bund gewährt nur 20 % statt 40 % Selbstnutzungsabzug, keinen Abzug nach Ziff. 25.3 und weniger Versicherungsabzug.
> 
> Die fachliche Beurteilung und die Abnahme liegen bei der Fachperson.

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


**Antwort des Agenten** (165.0 s · Tools: 28 Aufrufe read, steuerwiki__formular, steuerwiki__position, steuerwiki__beleg, steuerwiki__suche, steuerwiki__wert, rechne, steuerwiki__rechne):

> Ich habe die Positionen und Limiten für AR 2025 beisammen und rechne jetzt die Beträge durch.
> 
> # Ausfüllhilfe Steuererklärung AR 2025: Ehepaar Herisau
> 
> Formular: Steuererklärung 2025 AR (Formular 1, Hilfsblätter 2, 4, 5, 6, 10). Das AR-Formular hat **keine Bundesspalte**. Die Steuerverwaltung rechnet die Bundessteuer automatisch um (ar-wl-2025__c0179). Du trägst also nur die **Kantonswerte** ein. Die Bundeswerte stehen unten zur Kontrolle.
> 
> Status ☑️ heisst: Fundstelle geprüft, Abnahme durch die Fachperson offen. Die Codes der Hauptformular-Seite 3 sind im Wiki nicht verifiziert. Bitte am Originalformular prüfen.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg / Beleg | Status |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb Person 1 | 85'300 | 85'300 | Lohnausweis Ziff. 11. Rechnung: 98'000 − 6'860 − 5'840. Nicht den Bruttolohn eintragen. | ☑️ |
> | 1.1 | 102 | Haupterwerb Person 2 | 68'200 | 68'200 | Lohnausweis Ziff. 11. Rechnung: 82'000 − 5'740 − 4'060 − 4'000. Die Kinder- und Ausbildungszulagen stecken schon im Lohn. | ☑️ |
> | 3.5 | 142 | Zulagen von Ausgleichskassen | 0 | 0 | Nur direkt von der Ausgleichskasse bezahlte Zulagen gehören hierhin (ar-wl-2025__c0054). | ☑️ |
> | 4.1 | 146 | Wertschriften und Guthaben | 1'410 | 1'410 | Form. 2: Zinsen 160 (Spalte B, Bruttozins ≤ 200) plus Dividenden 1'250 (Spalte A). Übertrag nach Ziff. 4.1. | ☑️ |
> | 7 | 168 | **Total Einkünfte** | **154'910** | 154'910 | 85'300 + 68'200 + 1'410 | |
> 
> ## 2. Abzüge
> 
> | Ziff. | Code | Position | Kanton | Bund (Info) | Rechenweg / Regel | Status |
> |---|---|---|---|---|---|---|
> | 10.1 | 438 | Berufskosten Person 1 (Form. 4, Ziff. 6) | 4'000 | 4'159 | Siehe Berufskosten unten | ☑️ |
> | 10.2 | 488 | Berufskosten Person 2 (Form. 4, Ziff. 6) | 6'300 | 5'946 | Siehe Berufskosten unten | ☑️ |
> | 13.1 | – | Säule 3a (Person 1 und Person 2) | 12'258 | 12'258 | 7'258 + 5'000, beide unter dem Maximum von 7'258 (mit 2. Säule). Bescheinigungen beilegen. | ☑️ |
> | 13.2 | – | Einkauf 2. Säule | **0** | 0 | Der Einkauf von 4'000 ist schon im Nettolohn abgezogen (Ziff. 10.2 im Lohnausweis). Nicht nochmals abziehen. | ⚠️ |
> | 14 | 600 | Versicherungsprämien und Sparzinsen (Form. 6) | 7'400 | 5'100 | A = 13'900 + 160 = 14'060. Limite Kanton: 5'400 + 2 × 1'000. Limite Bund: 3'700 + 2 × 700. Abzug = der kleinere Betrag. | ☑️ |
> | 16.1 | – | Verwaltungskosten Wertschriften | 276 | 0 | Pauschale 3 ‰ × 92'000, auf Antrag. Bund: nur effektive Gebühren, keine belegt. | ☑️ |
> | 16.2 | – | Kinderbetreuung Lea (Form. 10) | 10'200 | 10'200 | 14'400 − 1'800 (Mittagessen) − 2'400 (Betreuungsbeitrag). Limite Kanton 25'000, Bund 25'800. | ☑️ |
> | 17 | – | Zweiverdienerabzug | 5'200 | 14'100 | Siehe unten | ☑️ |
> | 18 | – | **Total Abzüge** | **45'634** | 51'763 | | |
> | 20 | – | **Nettoeinkommen** | **109'276** | 103'147 | 154'910 − Total Abzüge | |
> | 21.3 | 550 | Spende Krebsliga | 300 | 300 | Total ≥ 100 und ≤ 20 % des Nettoeinkommens (Kanton 21'855, Bund 20'629). Der ganze Betrag ist abziehbar. Quittung bereithalten. | ☑️ |
> | 22 | – | **Reineinkommen** | **108'976** | 102'847 | 109'276 − 300 | |
> | 23.2 | – | Kinderabzug Lea | 7'400 | 6'800 | Geboren 14.03.2021. Am 31.12.2025 ist sie 4 Jahre alt, also nach vollendetem 4. Altersjahr. | ☑️ |
> | 23.3 | – | Kinderabzug Jonas | 11'600 | 6'800 | Geboren 02.09.2009. Am 31.12.2025 ist er 16 und in Ausbildung. | ☑️ |
> | – | – | Verheiratetenabzug | – | 2'800 | Gibt es nur beim Bund (Ziff. 24). | ☑️ |
> | 24 | – | **Steuerbares Einkommen** | **89'976** | 86'447 | Kanton: 108'976 − 19'000. Bund: 102'847 − 16'400. | |
> 
> **Weitere Bundeswerte:** Der Bund zieht zusätzlich 263 je Kind direkt vom Steuerbetrag ab, also 2 × 263 = 526 (bund-dbg-2025__art-36-t4). Das ist eine eigene Entlastung und nicht dasselbe wie der Kinderabzug von 6'800.
> 
> ### Berufskosten (Form. 4)
> 
> | Position | Person 1 | Person 2 | Regel und Fundstelle |
> |---|---|---|---|
> | 1.1 Fahrkosten ÖV (Code 400 / 450) | **0** | 1'260 | Bei Person 1 ist Feld F angekreuzt (Werkbus), das schliesst den Fahrkostenabzug aus (ar-wl-2025__c0075). Bei Person 2 gilt der tatsächliche Abo-Preis, unter beiden Limiten (Kanton 6'000, Bund 3'300). |
> | 2.1 Auswärtige Verpflegung (Code 458) | – | 2'640 | 176 Tage × 15 = 2'640 (Limite 3'200). |
> | 2.2 Verpflegung verbilligt (Code 410) | 1'600 | – | Feld G angekreuzt, daher der halbe Ansatz: 220 × 7.50 = 1'650, begrenzt auf 1'600. |
> | 3 Übrige Berufskosten Kanton (Code 416 / 466) | 2'400 | 2'400 | 700 + 10 % des Nettolohns ergibt mehr als das Maximum von 2'400. |
> | 3 Übrige Berufskosten Bund | 2'559 | 2'046 | 3 % des Nettolohns, mindestens 2'000, höchstens 4'000. |
> | **Total Kanton** | **4'000** | **6'300** | |
> | **Total Bund** | 4'159 | 5'946 | |
> 
> Fundstelle für die Verpflegung und die übrigen Berufskosten: ar-form-04-2025__c0003. Die Schichtarbeit (Ziff. 2.3) trifft bei der Tagesschicht nicht zu. Sie lässt sich ohnehin nicht mit 2.1 kombinieren.
> 
> ### Zweiverdienerabzug (Ziff. 17)
> 
> Massgebend ist das niedrigere Erwerbseinkommen, also das von Person 2. Es wird nach Berufskosten und Säule 3a berechnet. Den Einkauf rechnest du nicht nochmals ab, er ist schon im Nettolohn berücksichtigt.
> - **Kanton:** E = 68'200 − 6'300 − 5'000 = 56'900. 10 % davon sind 5'690, begrenzt auf 5'200 (ar-wl-2025__c0004).
> - **Bund:** E = 68'200 − 5'946 − 5'000 = 57'254. 50 % davon sind 28'627, begrenzt auf 14'100.
> 
> ## 3. Vermögen (nur Kanton, der Bund erhebt keine Vermögenssteuer)
> 
> | Ziff. | Code | Position | Betrag | Rechenweg |
> |---|---|---|---|---|
> | 30.1 | 300 | Wertschriften und Guthaben (Form. 2) | 92'000 | Konten 54'000 + Aktien 38'000 |
> | 33 | 322 | Total Vermögenswerte | 92'000 | |
> | 34.1 | 504 | Privatschulden | 0 | Keine angegeben |
> | 35 | 326 | Reinvermögen | 92'000 | |
> | 36.2 | 332 | Sozialabzug Ehegatten | 150'000 | ar-wl-2025__c0005 |
> | 36.3 | 334 | Sozialabzug Kinder | 50'000 | 2 × 25'000. Jonas ist minderjährig und hat einen Kinderabzug (ar-stg__art-51). |
> | 37 | 338 | **Steuerbares Vermögen** | **0** | 92'000 − 200'000 ergibt kleiner als null, also 0 |
> 
> **Verrechnungssteuer (Form. 2, Code 999):** 35 % × 1'250 = **437.50** zurückfordern (ar-form-02-2025__c0007). Das entspricht dem abgezogenen Betrag.
> 
> ## 4. Nicht zu deklarieren oder nicht abziehbar
> 
> - **Mitgliederbeitrag Turnverein (120):** Mitgliederbeiträge sind keine abziehbaren Zuwendungen (Ziff. 21.3).
> - **Handy-Abo (960):** private Lebenshaltungskosten. Die Pauschale für übrige Berufskosten ist schon abgegolten.
> - **Steuerzahlung 2024 (9'870):** Steuern sind nicht abziehbar. Die Rechnung ist bezahlt, also gibt es auch keine Schuld in Ziff. 34.1. Ich habe keine Quelle gefunden, die den Abzug erlaubt. Eine offene Steuerforderung per 31.12.2025 könnte als Schuld relevant sein, dazu liegt nichts vor.
> - **Mittagessen in der Kita (1'800):** im Betreuungsabzug nicht abziehbar.
> - **Betreuungsbeitrag (2'400):** kein Einkommen. Er wird als «erhaltene Beiträge» von den Kosten abgezogen.
> - **Mietzins:** nicht abziehbar, ihr seid Mieter.
> - **Pensionskassen- und 3a-Guthaben:** bis zur Fälligkeit kein Vermögen (ar-wl-2025__c0111).
> - **Lohnausweis Ziff. 9, 10.1 und 10.2:** schon im Nettolohn abgezogen, nicht nochmals eintragen.
> - **Bruttolohn und Kinderzulagen:** nicht zusätzlich in Ziff. 3.5 erfassen.
> - **Prämienverbilligung:** gibt es nicht, also kein Abzug dafür bei Ziff. 14.
> - **Krankheitskosten (Ziff. 21.1):** keine belegt.
> 
> ## 5. Offene Punkte und Rückfragen
> 
> 1. **Ziff. 13.2 ist strittig ⚠️.** Das Wiki bestätigt, dass ein Einkauf via Lohnabzug schon im Nettolohn steckt. Die Wegleitung ist aber in sich widersprüchlich (13.2 gegen 16.6). Ich habe nichts abgezogen, damit er nicht doppelt zählt. Die Pensionskassen-Bestätigung bereithalten. Fachperson prüfen lassen.
> 2. **Verpflegung Person 2 (2'640):** Der Abzug gilt nur, wenn die Heimkehr zum Mittagessen nicht zumutbar ist (ar-wl-2025__c0076). Ich habe den Standardfall mit Mittagessen auswärts erfasst. **Rückfrage:** Ist die Heimkehr über Mittag möglich? Ohne den Abzug fallen die Berufskosten Person 2 auf 3'660, das erhöht das steuerbare Einkommen Kanton um 2'640. Der Zweiverdienerabzug bleibt bei 5'200.
> 3. **Fahrkosten Person 1:** Ich habe 0 angesetzt (Feld F). Das gilt nur, wenn der Werkbus den ganzen Arbeitsweg abdeckt.
> 4. **Verwaltungskosten Wertschriften (Ziff. 16.1):** Mit der Pauschale von 276 ist das Wiki abgedeckt. Liegen Depotgebühren vor, wären diese für den Bund relevant. Der Bund kennt nur effektive Kosten. **Fehlender Beleg:** Gebührenausweis der Bank.
> 5. **Betreuungsbeitrag 2'400:** Ich gehe davon aus, dass er die Betreuung betrifft und nicht das Mittagessen. Bitte an der Gutschrift prüfen. Ändert sich das, verschiebt sich der Abzug in Ziff. 16.2.
> 6. **Jonas:** Der Kinderabzug setzt voraus, dass seine Einkünfte unter 18'000 liegen und kein Unterhaltsbeitrag abgezogen wird. **Rückfrage:** Hat er Einkünfte (Ferienjob, Lehrlingslohn)?
> 7. **Vermögen (Ziff. 30.3, 30.4):** Es wurden keine Lebensversicherungen mit Rückkaufswert oder Motorfahrzeuge genannt. **Rückfrage:** Gibt es solche?
> 8. **Bund, Teilzeit:** Die Bundespauschale für übrige Berufskosten wird bei Teilzeit angemessen gekürzt (Wiki). Bei Person 2 (80 %) kann der Bundeswert von 2'046 tiefer ausfallen. Die Steuerverwaltung passt das automatisch an.
> 9. **Krebsliga Ostschweiz:** Ich bin davon ausgegangen, dass sie steuerbefreit und gemeinnützig ist. Das steht auf der Quittung.
> 
> Beizulegen sind die Lohnausweise beider Personen, die 3a-Bescheinigungen und der vollständige Bank-Steuerauszug. Prämien, Kita-Rechnungen, die Spendenquittung und das Abo auf Verlangen. Die fachliche Beurteilung bleibt bei der Fachperson.

