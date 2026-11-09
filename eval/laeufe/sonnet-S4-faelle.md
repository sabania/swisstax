# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 19:08
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


**Antwort des Agenten** (153.2 s · Tools: 31 Aufrufe read, steuerwiki__formular, read, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__wert, steuerwiki__rechne):

> # Ausfüllhilfe: Kanton ZH · Steuerjahr 2025 (Ehepaar, Winterthur)
> 
> Formular: StA Form. 300 mit Hilfsblättern 340, 360, 365 und 370. Beträge in ganzen Franken, Staat und Bund getrennt. Alle Totale sind mit `rechne` berechnet. Status je Zeile: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen), sofern nicht anders vermerkt.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Marco, Nettolohn | 103'000 | 103'000 | Lohnausweis Ziff. 11. Der BVG-Einkauf (Ziff. 10.2) ist 0. | zh-wl-2025__c0032 |
> | 1.1 | 101 | Sandra, Nettolohn | 67'200 | 67'200 | Lohnausweis Ziff. 11. Die Kinderzulagen von 4'800 sind darin enthalten und steuerbar. Sie kommen nicht in Ziff. 3.4. | zh-wl-2025__c0032, c0055 |
> | 4.1 | 150 | Ertrag aus Wertschriften und Guthaben (Form. 340, A + B) | 1'140 | 1'140 | Kolonne A: Dividenden 960 (Code 2309, mit VSt). Kolonne B: Sparzins 180 (Code 542, Zins unter 200, ohne VSt). Privatkonto: 0. | zh-form-340-2025__c0005, zh-wl-2025__c0168 |
> | Form. 340 | 540 | Verrechnungssteueranspruch | 336.00 | – | 35 % × 960. Das ist eine Rückforderung, kein Einkommen. | zh-form-340-2025__c0005 |
> | **7** | **199** | **Total der Einkünfte** | **171'340** | **171'340** | 103'000 + 67'200 + 1'140 | |
> 
> ## 2. Abzüge
> 
> **Berufsauslagen Form. 360**
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 360/1.1 | 201 | Marco, ÖV-Abo | 4'180 | 3'300 | Plafond Staat 5'200, Bund 3'300. Feld F ist nicht angekreuzt. |
> | 360/2.1 voll | 208 | Marco, Verpflegung | 3'200 | 3'200 | min(220 × 15; 3'200). Feld G ist nicht angekreuzt. |
> | 360/3 | 212 | Marco, übrige Berufskosten | 3'090 | 3'090 | 3 % × 103'000 (Minimum 2'000, Maximum 4'000) |
> | 360/6 → **11.1** | **220** | **Total Marco** | **10'470** | **9'590** | Fahrkosten-Zwischentotal: Code 205. |
> | 360/1.2 | 222 | Sandra, Velo-Pauschale | 700 | 700 | Pro Jahr bei ständiger Benützung, ohne Beleg. Zwischentotal: Code 225. |
> | 360/2.1 verbilligt | 226 | Sandra, Verpflegung | 1'320 | 1'320 | Feld G ist angekreuzt, also min(176 × 7.50; 1'600). |
> | 360/3 | 232 | Sandra, übrige Berufskosten | 2'016 | 2'016 | 3 % × 67'200 |
> | 360/6 → **11.2** | **240** | **Total Sandra** | **4'036** | **4'036** | |
> 
> Fundstellen: zh-form-360-2025__c0001, c0003, c0004; zh-wl-2025__c0062, c0063, c0066, c0069.
> 
> **Hauptformular**
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 14.1 | 260 (eff. 262) | Säule 3a Marco | 7'258 | 7'258 | Formular 21 EDP. Mit 2. Säule gilt das Maximum 7'258. | zh-wl-2025__c0081 |
> | 14.2 | 261 (eff. 263) | Säule 3a Sandra | 7'258 | 7'258 | wie oben | zh-wl-2025__c0081 |
> | 15 | 270 | Versicherungsprämien (Form. 365) | 8'400 | 5'100 | Siehe unten. | zh-form-365-2025__c0001, c0002 |
> | 16.1 | 280 | PK-Einkauf Marco | 10'000 | 10'000 | Selbst überwiesen am 14.11.2025 und nicht im Lohnausweis (10.2 = 0). Bescheinigung beilegen. | zh-wl-2025__c0092 |
> | 16.3 | 283 | Verwaltungskosten Depot | 94 | 0 ⚠️ | Staat: 3 ‰ × 31'200 = 93.60. Das Bankguthaben zählt nicht zur Basis. Für den Bund ist keine Pauschale belegt (nur effektive Depotgebühren). | zh-wl-2025__c0095 |
> | 16.6 | 376 | Fremdbetreute Kinder | 31'900 | 32'700 | Siehe unten. | zh-stg-2025__par-31-t4; zh-form-300-2025__c0008 |
> | 17 | 290 | Sonderabzug Zweiverdiener | 6'100 | 14'100 | Siehe unten. | zh-wl-2025__c0112 |
> | **18** | **299** | **Total der Abzüge** | **85'516** | **90'042** | Summe aus 11.1, 11.2, 14.1, 14.2, 15, 16.1, 16.3, 16.6 und 17 | |
> 
> **Form. 365, Versicherungsprämien**
> - Teil A: Krankenkasse (Code 601) 15'840, Sparzinsen (Code 604) 180, Prämienverbilligung (Code 605) 0. Daraus ergibt sich Total A (Code 606) = 16'020.
> - Teil B: Verheiratete mit 2. Säule und 3a (Code 611) 5'800 Staat / 3'700 Bund. Zuschlag für 2 Kinder (Codes 613–615): 2'600 Staat / 1'400 Bund. Maximum B = 8'400 / 5'100.
> - Teil C (Code 270): min(A; B) = 8'400 Staat / 5'100 Bund.
> 
> **Ziff. 16.6, Kinderbetreuung (pro Kind)**
> - Lena: min(27'300; 25'000) = 25'000 Staat. Bund: min(27'300; 25'800) = 25'800.
> - Noah (Jg. 2016): 6'900 in beiden Spalten.
> 
> **Ziff. 17, Zweiverdienerabzug**
> - Basis ist Sandras verbleibendes Erwerbseinkommen: 67'200 − 4'036 − 7'258 = 55'906.
> - Staat: min(55'906; 6'100) = 6'100.
> - Bund: 50 % = 27'953, begrenzt auf 14'100.
> 
> ## 3. Einkommensberechnung
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 19 / 20 | 199 / 299 | Total Einkünfte / Total Abzüge | 171'340 / 85'516 | 171'340 / 90'042 | |
> | **21** | **310** | **Nettoeinkommen** | **85'824** | **81'298** | |
> | 22.1 | 320 | Krankheitskosten | 0 | 0 | Kosten 1'240 + 1'850 = 3'090. Selbstbehalt 5 %: 4'291.20 (Staat) bzw. 4'064.90 (Bund). Der Selbstbehalt wird nicht erreicht. Form. 370 ist nicht nötig. |
> | 22.2 | 324 | Gemeinnützige Zuwendungen | 650 | 650 | 400 + 250. Mindestens 100 und höchstens 20 % des Nettoeinkommens (17'164.80 Staat). Aufstellung beilegen. |
> | **23** | **350** | **Reineinkommen** | **85'174** | **80'648** | |
> | 24.1 | 370 | Kinder im Haushalt | 18'600 | 13'600 | 2 × 9'300 bzw. 2 × 6'800 |
> | 24.3 | 365 | Verheiratetenabzug (nur Bund) | – | 2'800 | |
> | **25 / 27** | **390 / 398** | **Steuerbares Einkommen** | **66'574** | **64'248** | |
> 
> Plausibilität: Das Bundeseinkommen liegt 2'326 unter dem Staatseinkommen. Hauptgründe sind der höhere Zweiverdienerabzug (+8'000) und der Verheiratetenabzug (+2'800). Dagegen wirken die tieferen Bundeslimiten bei Versicherung, Fahrkosten und Kinderabzug.
> 
> Zum Steuerbetrag: Der Bund kennt laut Gerüst einen Kinderabzug vom Steuerbetrag von 263 je Kind. Das sind 526 für beide Kinder. Er wird bei der Veranlagung berücksichtigt, nicht im Formular erfasst.
> 
> ## 4. Vermögen
> 
> | Ziff. | Code | Position | Betrag | Beleg |
> |---|---|---|---|---|
> | 30.1 | 400 | Wertschriften und Guthaben (Form. 340) | 82'000 | Sparkonto 42'500 + Privatkonto 8'300 + Depot 31'200 |
> | 33 | 460 | Total Vermögenswerte | 82'000 | |
> | 34 | 470 | Schulden | 0 | |
> | **35 / 37** | **490 / 498** | **Steuerbares Vermögen** | **82'000** | Das steuerfreie Vermögen wirkt nur im Tarif. Es wird nichts abgezogen. |
> 
> Die Ziffern 30.2 bis 32 und 36 entfallen. Ziff. 40 (Kapitalleistungen) ist nicht auszufüllen. Es gab keine Bezüge in den letzten 3 Jahren.
> 
> ## 5. Nicht zu deklarieren oder nicht abziehbar
> 
> - **Pensionskasse und Säule 3a, Guthaben:** Sie sind bis zur Fälligkeit kein steuerbares Vermögen (zh-wl-2025__c0154). Nur der Einkauf und die 3a-Einzahlungen sind Abzüge.
> - **Lohnabzüge AHV, BVG ordentlich und NBUV:** Sie sind im Nettolohn schon abgezogen und gehören nicht in Ziff. 15 oder 16.1.
> - **Kinderzulagen von 4'800:** Sie sind im Lohnausweis enthalten und stehen nicht zusätzlich in Ziff. 3.4.
> - **Verrechnungssteuer von 336:** Sie wird zurückgefordert und ist weder Einkommen noch Abzug. Eine DA-1 ist nicht nötig, weil keine ausländische Quellensteuer anfällt.
> - **Krankenkassenprämien als Krankheitskosten:** Prämien sind keine Krankheitskosten (bund-ks-11__c0004). Sie stehen nur in Form. 365.
> - **Swisscom-Handyrechnungen von 1'080 (privat):** Das sind Lebenshaltungskosten. Berufliche Nutzung ist mit der Pauschale der übrigen Berufskosten abgegolten.
> - **Hausrat und Privathaftpflicht von 465:** Form. 365 sieht nur Kranken-, Unfall-, Lebens- und Rentenversicherung sowie Sparzinsen vor. Ich habe keine ausdrückliche Fundstelle zu Sachversicherungen gefunden. Das ist daher nur aus der Systematik des Formulars abgeleitet und nicht geprüft.
> - **Miete:** Es gibt keinen Abzug und keine Liegenschaftsangaben.
> - **Krankheitskosten (3'090):** Sie liegen unter dem Selbstbehalt. Der Abzug ist 0, ein Formular 370 ist nicht einzureichen.
> 
> ## 6. Annahmen und offene Punkte für die Fachperson
> 
> 1. **Sandra, Verpflegung (Code 226, 1'320):** Ich habe den Standardfall erfasst, weil Feld G angekreuzt ist. Der Abzug gilt nur, wenn die Heimkehr über Mittag nicht möglich ist. Wohn- und Arbeitsort sind beide Winterthur. Falls sie über Mittag heimkehren kann, entfallen die 1'320, und das Nettoeinkommen steigt entsprechend. Rückfrage: Ist die Mittagspause zu kurz für die Heimkehr?
> 2. **Noah, Hort (6'900):** Die Rechnung darf keine Verpflegung enthalten (zh-form-300-2025__c0008). Falls ein Mittagstisch oder Essen eingerechnet ist, muss dieser Teil abgezogen werden. Rückfrage: Enthält die Hortrechnung Verpflegung?
> 3. **Depotgebühren (Ziff. 16.3):** Falls der Steuerauszug Depotgebühren ausweist, sind effektive Kosten im Bund abziehbar. Im Kanton gilt die höhere Variante, wenn sie nachgewiesen ist. Bund 0 ist ein offener Punkt (⚠️).
> 4. **Marco, Verpflegung Bund:** Sie ist kein Abzug, wenn die Hauptmahlzeit höchstens 10 Fr. kostet. Bei Restaurant-Mittagessen ist das unwahrscheinlich, aber nicht belegt.
> 5. **Sandra, Pauschale übrige Berufskosten (Bund):** Die Pauschale ist bei Teilzeit angemessen zu kürzen. Ich habe 3 % × 67'200 = 2'016 eingesetzt. Das liegt knapp über dem Minimum von 2'000.
> 6. **PK-Einkauf:** Der Abzug entfällt, soweit innert 3 Jahren ein Kapitalbezug erfolgt. Der Einkauf ist auf die Einkaufssumme laut Reglement begrenzt, das habe ich nicht geprüft.
> 7. **Einzureichen:**
>    - Lohnausweise
>    - Formular 21 EDP (Säule 3a und PK-Einkauf)
>    - Form. 360 und 365
>    - Aufstellung der Betreuungskosten und der Spenden
>    - Wertschriftenverzeichnis (Form. 340) mit Steuerauszug
>    - Belege nur auf Verlangen
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


**Antwort des Agenten** (137.8 s · Tools: 28 Aufrufe read, steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne):

> Ich habe die Positionen für SG 2025 geprüft und rechne jetzt die Totale nach.
> 
> **SG · Steuerjahr 2025 · Ausfüllhilfe Nadine (alleinerziehend, 1 Kind)**
> Formular: Steuererklärung 2025 Formular 1 mit Hilfsblättern Form. 2, 4, 6, 10. Es gibt eine Spalte für Kanton und Bund. Das Steueramt rechnet die Bundesabweichungen automatisch (sg-wl-2025__c0173). Die Bundesbeträge unten sind also meine Berechnung der Abweichungen, nicht Formulareinträge. Alle Beträge in Fr., Status ☑️ (Fundstelle geprüft, Abnahme offen), ausser wo anders angegeben.
> 
> ### Einkünfte
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb unselbständig | 73'000 | 73'000 | Lohnausweis Ziff. 11 (Nettolohn). Die Kinderzulage 2'400 ist in Ziff. 8 enthalten und deshalb schon eingerechnet. | sg-wl-2025 / beleg lohnausweis |
> | 4.1 | 146 | Wertschriften und Guthaben | 68 | 68 | Form. 2, Spalte B (Zins ≤ 200, ohne Verrechnungssteuer). Es gibt keinen Anspruch auf Verrechnungssteuer, also kein Code 999. | sg-wl-2025__c0135 |
> | 6.1 | 156 | Unterhaltsbeiträge für minderjährige Kinder | 9'600 | 9'600 | 12 × 800, steuerbar bei Nadine. | sg-wl-2025__c0068 |
> | **7** | 168 | **Total Einkünfte** | **82'668** | **82'668** | 73'000 + 68 + 9'600 | |
> 
> ### Abzüge
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | Form. 4 1.3 | 404/406 | Fahrkosten Auto | 8'000 | 3'300 | 32 km × 2 × 220 = 14'080 km × 0.70 = 9'856. Maximum Kanton 8'000, Bund 3'300. Begründung ankreuzen: «Fehlen eines öffentlichen Verkehrsmittels». | sg-form-4-2025__c0002, sg-wl-2025__c0077 |
> | Form. 4 2.1 | 408 | Auswärtige Verpflegung | 3'200 | 3'200 | min(220 × 15 = 3'300; 3'200) | sg-wl-2025__c0078 |
> | Form. 4 3.1 | 416 | Übrige Berufskosten (Pauschale) | 2'400 | 2'190 | Kanton min(700 + 10 % × 73'000; 2'400). Bund min(max(3 % × 73'000; 2'000); 4'000). | sg-wl-2025__c0080 |
> | **10.1** | 438 | **Berufskosten (Form. 4 Ziff. 6)** | **13'600** | **8'690** | Summe der drei Zeilen oben | |
> | 13.1 | 208 | Säule 3a | 7'258 | 7'258 | Bescheinigung, entspricht dem Maximum mit 2. Säule. | `wert sg 2025 saeule3a` |
> | 13.2 | 218 | PK-Einkauf | 6'000 | 6'000 | Bescheinigung und Einkaufsberechnung beilegen. Die BVG-Beiträge 4'610 (Ziff. 10.1) stehen schon im Nettolohn. Ziff. 10.2 ist 0, also kein Doppelabzug. | sg-wl-2025__c0086 |
> | 14 | 600 | Versicherungsprämien und Sparzinsen (Form. 6) | 4'500 | 2'500 | A = 5'280 + 1'320 − 1'800 + 68 = 4'868. B Kanton = 3'400 + 1'100 (Kind) = 4'500. B Bund = 1'800 + 700 = 2'500. Es gilt der niedrigere Betrag von A und B. Weil BVG und 3a abgezogen werden, gibt es keinen Zuschlag ohne Vorsorge. | sg-form-6-2025__c0002 |
> | 16.2 | 258 | Kinderbetreuung (Form. 10) | 8'760 | 8'760 | 9'840 − 1'080 (Mahlzeiten separat ausgewiesen). Das liegt unter den Limiten 26'700 bzw. 25'800. | sg-wl-2025__c0092 |
> | 16.4 | 223 | Weiterbildung | 400 | 340 | Kanton: höherer Betrag aus effektiv 340 und Pauschale 400 (nur Kanton). Bund: effektiv 340. | sg-wl-2025__c0094 |
> | 17 | 226 | Zweiverdienerabzug | – | – | Nicht anwendbar (kein Ehepaar). | |
> | **18** | 230 | **Total Abzüge** | **40'518** | **33'548** | | |
> | **20** | 234 | **Nettoeinkommen** | **42'150** | **49'120** | 82'668 − Total Abzüge | |
> 
> ### Abzüge auf Basis Nettoeinkommen und Sozialabzüge
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 21.1 | 650 / 238 / 240 | Krankheitskosten | Vorkolonne 3'600, Selbstbehalt 843, Abzug **2'757** | Vorkolonne 3'600, Selbstbehalt 2'456, Abzug **1'144** | 850 + 2'750 = 3'600. Selbstbehalt Kanton 2 % × 42'150, Bund 5 % × 49'120. |
> | 21.3 | 244 | Spenden | 0 | 0 | Caritas 80 liegt unter der Mindestsumme 100. |
> | **22** | 248 | **Reineinkommen** | **39'393** | **47'976** | |
> | 23.2 | 254 | Kinderabzug (Kindergarten gehört zur Schulpflicht, nicht 23.1) | 10'800 | 6'800 | Beim Bund kommt zusätzlich ein Abzug vom Steuerbetrag von max. 263 hinzu (Steueramt). |
> | **24** | 268 | **Steuerbares Einkommen** | **28'593** | **41'176** | |
> 
> Die Unterhaltsbeiträge für Elias hat der Ex-Mann zu zahlen und abzuziehen (Ziff. 12.2). Das Kind erhält deshalb bei ihm keinen Kinderabzug (sg-wl-2025__c0104).
> 
> ### Vermögen (nur Kanton, der Bund erhebt keine Vermögenssteuer)
> | Ziff. | Code | Position | Betrag |
> |---|---|---|---|
> | 30.1 | 300 | Sparkonto Raiffeisen (Form. 2, Steuerwert 31.12.) | 31'500 |
> | 30.4 | 306 | Motorfahrzeug | ⬜ **Wert fehlt** (Anschaffungspreis und Jahr nötig) |
> | 33 / 35 | 322 / 326 | Total Vermögenswerte / Reinvermögen | 31'500 (+ Fahrzeug) |
> | 36.1 | 330 | Sozialabzug alleinstehend | 75'000 |
> | 36.3 | 334 | Sozialabzug minderjähriges Kind | 20'000 |
> | **37** | 338 | **Steuerbares Vermögen** | **0** (31'500 − 95'000 ist kleiner als 0). Das gilt auch mit Fahrzeug, solange Sparkonto und Fahrzeug zusammen unter 95'000 liegen. |
> 
> ### Nicht zu deklarieren oder nicht abziehbar
> - **Motorfahrzeugsteuer 410 und Auto-Versicherung 1'020:** Der Ansatz 0.70/km deckt sie ab. Haftpflicht- und Kaskoversicherung sind in Ziff. 14 ausdrücklich nicht abziehbar.
> - **Handy-Abo 720:** Es ist privat, und die Pauschale für übrige Berufskosten deckt es ab. Ein Mehrbetrag bräuchte einen Nachweis der beruflichen Nutzung.
> - **Kita-Mahlzeiten 1'080:** Verpflegung ist bei der Drittbetreuung nicht abziehbar.
> - **Spende Caritas 80:** unter der Freigrenze von 100. Das gilt für Kanton und Bund.
> - **Prämienverbilligung 1'800:** kein Einkommen, wird in Form. 6 von den Prämien abgezogen.
> - **Kinderzulage 2'400:** ist schon im Nettolohn enthalten, nicht nochmals unter Ziff. 3.5 erfassen.
> - **AHV-Beitrag 5'890 und BVG 4'610:** schon im Nettolohn abgezogen.
> - **Guthaben der 2. Säule und der Säule 3a:** kein steuerbares Vermögen (sg-wl-2025__c0107).
> - **Vermögensverwaltungskosten (Ziff. 16.1):** keine, da kein Depot vorhanden ist.
> 
> ### Fehlende Belege und offene Punkte
> - **Fahrzeugwert für Ziff. 30.4:** ⬜ Anschaffungswert abzüglich 20 % pro Jahr seit Erwerb. Der Wert ändert das steuerbare Vermögen nicht.
> - **Form. 10 (Kinderbetreuung):** Name und Adresse der Kita, bezahlte Kosten. Die Mahlzeiten müssen separat ausgewiesen bleiben.
> - **PK-Einkauf:** Bescheinigung und Einkaufsberechnung sind zwingend beizulegen (sg-wl-2025__c0086).
> - **Alimente:** Bei erstmaliger Zahlung ist ein Auszug aus dem Scheidungsurteil beizulegen, sonst eine Aufstellung (sg-wl-2025__c0084).
> 
> ### Hinweise für die Fachperson
> 1. **Fahrkosten Auto (grösste Ermessensposition).** Die Begründung ist «Fehlen eines öffentlichen Verkehrsmittels» (Arbeitsbeginn 06:00, erste Verbindung 06:40). Die Wegleitung lässt Auto-Kosten nur zu, «insoweit» die Benützung nicht zugemutet werden kann (sg-wl-2025__c0077). Die Rückfahrt könnte das Steueramt mit dem öV prüfen. Bei teilweiser Ablehnung wären nur Hin- oder Rückfahrt mit Auto und der Rest zu öV-Tarif abziehbar. Beim Bund wäre das Maximum von 3'300 wohl trotzdem erreicht. Ich habe keinen öV-Preis und rechne deshalb mit dem Standardfall. Rückfrage an Nadine: Gibt es abends einen zumutbaren öV zurück nach Hause?
> 2. **Auswärtige Verpflegung 3'200.** Das ist angenommen für 220 Tage ohne Home-Office, weil Heimkehr bei 32 km nicht möglich ist. Bei weniger Tagen gilt 15 pro Tag.
> 3. **Kinderbetreuung Bund (Ziff. 16.2).** Der Bund lässt Betreuung ausserhalb der Arbeitszeit nicht zu. Ich habe die Kita-Kosten als erwerbsbedingt angenommen. Klären, ob Tagesstruktur-Zeiten ohne Arbeit enthalten sind, etwa an Ferientagen.
> 4. **Zahnarzt 2'750.** Er gilt nur, wenn es sich um eine medizinisch notwendige Behandlung handelt (nicht kosmetisch). Die Rechnung gehört in Form. 6 Rückseite, die KK-Abrechnung ist beizulegen, falls darauf verwiesen wird.
> 5. **Tarif (nicht geprüft).** Das Steueramt ordnet Alleinerziehende mit Kind in den Elterntarif ein (Quelle: sg-stv__art-55, sg-form-32-2025__c0008, nur Titelzeilen gelesen). Das habe ich nicht weiter geprüft, es hat auf die Ausfüllhilfe keinen Einfluss.
> 6. **Plausibilität.** Das Bundeseinkommen (41'176) liegt über dem Kantonseinkommen (28'593). Das erklärt sich durch die tieferen Bundesmaxima bei Fahrkosten (3'300 statt 8'000) und Versicherung (2'500 statt 4'500), die tiefere Bundespauschale bei übrigen Berufskosten, den Kinderabzug (6'800 statt 10'800) und den höheren Selbstbehalt bei Krankheitskosten (5 % statt 2 %).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

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


**Antwort des Agenten** (155.8 s · Tools: 34 Aufrufe read, steuerwiki__formular, steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, message, steuerwiki__beleg, steuerwiki__rechne):

> # Ausfüllhilfe: Kanton TG · Steuerjahr 2025
> 
> Mandantin: Rentnerin, 70, alleinstehend (verwitwet), Wohnsitz Frauenfeld. Formular 1 mit den Hilfsblättern 2, 4.1, 5.1, 5.2, 6, 7 und 8. Das TG-Formular hat zwei Spalten (Staat | Bund). Alle Beträge sind in ganzen Franken, mit `rechne` gerechnet. Status bei allen Werten: ☑️ agent-geprüft. Die Fachperson nimmt ab.
> 
> ## 1. Einkünfte
> 
> | Ziffer / Code | Position | Staat | Bund | Rechenweg · Beleg | Fundstelle |
> |---|---|---|---|---|---|
> | 3.1 / 130 | AHV-Rente | 27'000 | 27'000 | 12 × 2'250, zu 100 % steuerbar | tg-wl-2025__c0076 |
> | 3.2 / 132 | PK-Rente | 10'800 (100 %) | 10'800 (100 %) | 12 × 900. Beginn 2020, also kein 80 %-Übergangsrecht | tg-wl-2025__c0077 |
> | 4 / 150 | Wertschriften- und Zinserträge (Übertrag Form. 2) | 2'160 | 2'350 | siehe Form. 2 unten | tg-wl-2025__c0153, c0159 |
> | 6 / 175 | Zwischentotal | 39'960 | 40'150 | 27'000 + 10'800 + Ziff. 4 | |
> | 8.1 / 180 | Liegenschaft, Nettoerfolg (Form. 7) | 4'840 | 8'920 | siehe Form. 7 unten | tg-wl-2025__c0225 |
> | 9 / 198 | **Total Einkünfte** | **44'800** | **49'070** | Ziff. 6 + 8.1 | |
> 
> **Form. 2 (Wertschriftenverzeichnis):**
> - Spalte 8 (mit Verrechnungssteuer, Franken und Rappen): Sparkonto TKB Zins 250.00, Steuerwert 48'000. Der Zins liegt über Fr. 200, also Spalte 8.
> - Spalte 8: Depot Dividenden 2'100.00, Steuerwert 95'000. Total Bruttoertrag 2'350.00, Total Steuerwert 143'000.
> - Ziff. 10, Verrechnungssteueranspruch: 35 % × 2'350 = **822.50**. Das stimmt mit dem abgezogenen Betrag überein (87.50 + 735). Es ist eine Rückerstattung, weder Einkommen noch Abzug (tg-wl-2025__c0167).
> - Vermögensverwaltungskosten, Code 148, Staat: min(2 ‰ × 95'000; 6'000) = **190**. Das Sparkonto zählt nicht zur Bemessung. Staat: 2'350 − 190 = 2'160.
> - Bund: Im Wiki ist nur eine Abzugsmöglichkeit für effektive Depotgebühren belegt, keine Pauschale. Ohne Gebührenausweis gilt daher 0, also 2'350. Siehe Hinweis 3.
> 
> **Form. 7 (Liegenschaft, Baujahr 1986, am Wohnsitz dauernd selbst bewohnt):**
> - Mietwert indexiert 20'400. Selbstnutzungsabzug Staat 40 % und Bund 20 %.
> - Steuerbarer Eigenmietwert: Staat 12'240, Bund 16'320 (tg-wl-2025__c0224, c0225).
> - Unterhalt, Wahl Pauschale oder effektiv je Liegenschaft: Die Pauschale beträgt 20 %, weil das Gebäude älter als 10 Jahre ist (tg-wl-2025__c0238).
>   - Pauschale: Staat 2'448, Bund 3'264.
>   - Effektiv (Form. 8): Malerarbeiten Ersatzanstrich 6'400 + Gebäudeversicherung 520 + Baumschnitt/Gartenpflege 480 = **7'400**.
>   - Effektiv ist günstiger, Staat und Bund (Differenz 4'952 bzw. 4'136). Beleg c0227, c0228, c0233.
> - Nettoerfolg: Staat 12'240 − 7'400 = **4'840**. Bund 16'320 − 7'400 = **8'920**.
> - Die Rechnung über 6'400 liegt über Fr. 1'000 und muss in Kopie beigelegt werden (tg-wl-2025__c0234).
> - Der Wintergarten-Anbau (31'000) ist wertvermehrend und nicht abziehbar. In Form. 8 gehört er in die Spalte «Anlagekosten/Mehrwert» (tg-wl-2025__c0233).
> 
> ## 2. Abzüge, Nettoeinkommen, Reineinkommen, steuerbares Einkommen
> 
> | Ziffer / Code | Position | Staat | Bund | Rechenweg · Beleg | Fundstelle |
> |---|---|---|---|---|---|
> | 11 / 290 | Schuldzinsen (Form. 4.1 A: Schuld 180'000 = Code 455, Zinsen 3'150 = Code 286) | 3'150 | 3'150 | Limite Vermögensertrag + 50'000, deutlich eingehalten | tg-wl-2025__c0171, c0173 |
> | 14 / 330 | Versicherungsprämien und Sparzinsen (Form. 5.2) | 3'500 | 2'700 | A1 Krankenkasse 6'240 + A4 Sparzinsen 250 = 6'490 (Code 324). Höchstbetrag B4: Staat 3'500, Bund 2'700 (alleinstehend ohne Säule 2/3a). Abzug = min(6'490; B4) | tg-form-05-2-2025__c0002 |
> | 19 / 360 | **Total Abzüge** | **6'650** | **5'850** | 3'150 + Ziff. 14 | |
> | 22 / 362 | **Nettoeinkommen** | **38'150** | **43'220** | Ziff. 20 − Ziff. 21 | |
> | 23.1 / 364 | Krankheitskosten (Form. 5.1 D) | 4'633 | 4'379 | A: Franchise/Selbstbehalt 1'000 + Zahnarzt 4'440 + Brille 1'400 = 6'840. B: Zusatzversicherung −300. Netto 6'540. Selbstbehalt 5 % × Ziff. 22: Staat 1'907.50, Bund 2'161. Staat 4'632.50, gerundet 4'633 | tg-wl-2025__c0205 |
> | 23.2 / 366 | Freiwillige Zuwendungen (Form. 6) | 350 | 550 | Krebsliga TG 300 + Pro Senectute TG 250 = 550. Staat: 550 − 200 Selbstbehalt = 350 (Höchstbetrag 8'000, da Ziff. 22 ≤ 40'000). Bund: ab 100, ohne Selbstbehalt, Höchstbetrag 20 % × 43'220 = 8'644, also 550 | tg-wl-2025__c0220 |
> | 24 / 372 | **Reineinkommen** | **33'167** | **38'291** | Staat 38'150 − 4'633 − 350. Bund 43'220 − 4'379 − 550 | |
> | 25.3 / 388 | AHV-Rentner/Witwe, nur Staat | 1'000 | – | Alleinstehend, Reineinkommen 33'167 liegt im Band 32'900–33'899, Abzug 1'000. Er wird nur einmal gewährt, auch wenn sie zugleich Witwe ist | tg-wl-2025__c0116, c0117 |
> | 26 / 398 | **Steuerbares Einkommen** | **32'167** | **38'291** | Ziff. 24 − Ziff. 25.3 | |
> 
> Die übrigen Einkommensziffern treffen nicht zu: 1.x, 2.x, 5.x, 10.x, 12, 13 (Säule 3a), 15.1 bis 15.6, 16, 17 (keine Behinderung), 18 (Zweiverdiener), 25.1/25.2/25.4 und 28.
> 
> Plausibilität: Das steuerbare Einkommen Bund liegt 6'124 über dem Kanton. Das erklären der geringere Selbstnutzungsabzug (4'080), der Abzug 25.3 nur im Kanton (1'000), die Versicherungsabzüge (800), die Vermögensverwaltungskosten (190) und die Differenzen bei Krankheitskosten und Spenden (254 bzw. −200).
> 
> ## 3. Vermögen (nur Staat, Bund hat keine Vermögenssteuer)
> 
> | Ziffer / Code | Position | Staat | Rechenweg |
> |---|---|---|---|
> | 30.1 / 410 | Wertschriften und Guthaben (Übertrag Form. 2) | 143'000 | 48'000 + 95'000 |
> | 31 / 430 | Liegenschaft, Steuerwert (Form. 7) | 410'000 | gemäss Schätzung (tg-wl-2025__c0239) |
> | 33 / 464 | Total Vermögenswerte | 553'000 | |
> | 34 / 466 | Schulden (Form. 4.1 C, Hypothek) | 180'000 | |
> | 35 / 468 | Reinvermögen | 373'000 | 553'000 − 180'000 |
> | 36.2 / 472 | Steuerfreier Abzug Alleinstehende | 100'000 | |
> | 37 / 498 | **Steuerbares Vermögen** | **273'000** | 373'000 − 100'000 |
> 
> ## 4. Nicht zu deklarieren oder nicht abziehbar
> 
> - **Hausratversicherung 380:** keine Liegenschaftsversicherung und nicht in Ziff. 14. Sie wird nicht eingereicht (tg-wl-2025__c0227).
> - **Serafe 335:** Lebenshaltungskosten, nicht abziehbar. Das Wiki führt dafür keinen eigenen Beleg-Typ, die Einordnung stützt sich auf Art. 34 lit. a DBG sinngemäss.
> - **Handyrechnung:** privater Alltagsaufwand, nicht steuerrelevant. Die Mandantin hat keine Berufskosten.
> - **Wintergarten 31'000:** wertvermehrend, kein Unterhalt (siehe oben).
> - **Krankenkassenprämien 6'240:** nur in Ziff. 14, nicht zusätzlich in den Krankheitskosten. Die Franchise von 1'000 steht nur in den Krankheitskosten, nicht doppelt.
> - **Verrechnungssteuer 822.50:** weder Einkommen noch Abzug, nur Rückerstattungsantrag in Form. 2.
> - **Spendenquittungen:** liegen unter Fr. 1'000 pro Zuwendung, also nicht einreichen, nur auf Verlangen (c0220).
> - **Ziff. 13, 15.1, 15.2:** nicht zutreffend, da keine 2./3a-Beiträge anfallen (AHV-Rentnerin, keine Erwerbstätigkeit).
> 
> ## 5. Beilagen und Rückfragen
> 
> **Beilagen:**
> - Steuerauszug TKB, mit Depotverzeichnis.
> - Rechnung der Malerarbeiten (6'400).
> - Kostenzusammenstellung der Krankenkasse, Zahnarzt- und Brillenrechnungen.
> 
> **Fehlende oder zu klärende Angaben:**
> 1. **Hypothek:** Name und Adresse der Gläubigerbank sowie Zinssatz sind im Form. 4.1 zwingend. Rechnerisch ergibt 3'150 / 180'000 etwa 1.75 %, der Satz aus der Bescheinigung ist massgebend.
> 2. **Gartenpflege 480:** abziehbar ist die Pflege mehrjähriger Pflanzen und Bäume (tg-wl-2025__c0228). Bitte die Rechnung aufschlüsseln. Falls sie nicht abziehbar wäre, bleibt der effektive Abzug mit 6'920 immer noch über der Pauschale.
> 3. **Zahnarzt 4'440:** Prüfen, ob die Kasse oder Zusatzversicherung etwas vergütet hat. Dann müsste B in Form. 5.1 höher ausfallen.
> 4. **Liegenschaftsrechnung:** Weist sie eine für 2025 fällige Besitzesabgabe aus (Betrag nicht angegeben), wäre diese zusätzlich in Form. 8 abziehbar (c0227).
> 5. **Spendenempfänger:** Name und Sitz einzeln in Form. 6 angeben. Steuerbefreiung der beiden Organisationen über die Liste der Steuerverwaltung TG prüfen.
> 6. **PK-Rentenbescheinigung:** bestätigt 100 % steuerbar, ohne Kapitalleistung.
> 
> ## Hinweise für die Fachperson
> 
> 1. **Eigenmietwert:** Der Mietwert von 20'400 ist als indexierter Wert 2025 gemäss Beleg übernommen. Die Prozentsätze stammen aus der Wegleitung (Staat 40 %, Bund 20 %).
> 2. **Neuschätzung:** Ob der Wintergarten-Anbau zu einer Neuschätzung oder Mutation des Steuerwerts führt, ist nicht geprüft. Ziff. 31 steht mit 410'000 gemäss Schätzung.
> 3. **Vermögensverwaltungskosten Bund:** Im Wiki ist keine Bundes-Pauschale belegt, deshalb 2'350. Würde die Fachperson 190 auch für den Bund akzeptieren, sänke Ziff. 4 Bund auf 2'160. Das Nettoeinkommen Bund würde dann um 190 sinken, die Krankheitskosten Bund um 9 steigen (5 % Selbstbehalt entfällt entsprechend).
> 4. **Rundung:** Der Krankheitskostenabzug Staat von 4'632.50 ist auf 4'633 gerundet. Das ändert den Abzug 25.3 nicht.

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


**Antwort des Agenten** (159.9 s · Tools: 30 Aufrufe read, steuerwiki__formular, steuerwiki__position, steuerwiki__beleg, steuerwiki__wert, steuerwiki__suche, message, steuerwiki__rechne):

> **Ausfüllhilfe: Kanton AR · Steuerjahr 2025** (Ehepaar, gemeinsame Veranlagung, Herisau)
> 
> Das AR-Formular hat keine Bundesspalte (ar-wl-2025__c0179). Ins Formular kommt der Kantonswert, und die Steuerverwaltung passt den Bund automatisch an. Die Bundesspalte unten ist meine Kontrollrechnung. Alle Beträge sind mit `rechne` gerechnet, Status je Wert ☑️ (Fundstelle geprüft, Abnahme offen), sofern nicht anders vermerkt. Mehrere Hauptformular-Codes sind im Wiki nicht verifiziert und deshalb weggelassen.
> 
> ### Einkünfte
> | Ziff. (Code) | Position | Kanton | Bund | Beleg · Rechenweg · Fundstelle |
> |---|---|---|---|---|
> | 1.1 (100) | Haupterwerb Person 1 | 85'300 | 85'300 | Lohnausweis Ziff. 11. Rechnung: 98'000 − 6'860 − 5'840 = 85'300. |
> | 1.1 (102) | Haupterwerb Person 2 | 68'200 | 68'200 | Lohnausweis Ziff. 11. Rechnung: 82'000 − 5'740 − 4'060 − 4'000 = 68'200. Die Familienzulagen stecken im Lohn und werden nicht separat erfasst (ar-wl-2025__c0032). Ziff. 3.5 gilt nur für direkt von der Ausgleichskasse bezahlte Zulagen (c0054). |
> | 4.1 (146) | Wertschriftenerträge | 1'410 | 1'410 | Form. 2: Dividenden 1'250 in Spalte A, Zinsen 160 in Spalte B. Spalte B gilt für Guthaben bis 200 Franken Zins pro Jahr (ar-wl-2025__c0147). |
> | 7 (168) | **Total Einkünfte** | **154'910** | **154'910** | 153'500 + 1'410 |
> 
> ### Abzüge
> | Ziff. (Code) | Position | Kanton | Bund | Rechenweg · Fundstelle |
> |---|---|---|---|---|
> | 10.1 (438) | Berufskosten Person 1 | 4'000 | 4'159 | Form. 4, siehe unten. |
> | 10.2 (488) | Berufskosten Person 2 | 6'300 | 5'946 | Form. 4, siehe unten. |
> | 13.1 | Säule 3a | 12'258 | 12'258 | 7'258 + 5'000. Beide Beträge liegen im Maximum von 7'258 für Personen mit 2. Säule (ar-wl-2025__c0003). Die Bescheinigungen sind beizulegen. |
> | 13.2 | PK-Einkauf | 0 | 0 | Der Einkauf von 4'000 ist schon im Nettolohn abgezogen (Lohnausweis Ziff. 10.2). Ein zweiter Abzug wäre doppelt. |
> | 14 (600) | Versicherungsprämien | 7'400 | 5'100 | Form. 6 A: 13'900 + 160 Sparzinsen = 14'060, keine Prämienverbilligung. Form. 6 B: Kanton 5'400 + 2×1'000, Bund 3'700 + 2×700. Der niedrigere Wert gilt, hier also das Maximum (ar-form-06-2025__c0002). |
> | 16.1 | Wertschriften-Verwaltungskosten | 276 | 0 | Kantonspauschale auf Antrag: 3 ‰ × 92'000. Die Basis sind die Steuerwerte inklusive privater Bankkonten. Beim Bund sind nur effektive Verwahrungskosten belegt (bund-wl-2a-2025__c0056). Dafür liegt kein Beleg vor, siehe Hinweise. |
> | 16.2 | Kinderbetreuung Lea (Form. 10) | 10'200 | 10'200 | 14'400 − 1'800 Mittagessen − 2'400 Betreuungsbeitrag. Limite 25'000 Kanton, 25'800 Bund. Lea ist unter 14 und beide Eltern sind erwerbstätig (ar-form-10-2025__c0001, ar-wl-2025__c0091). |
> | 17 | Zweiverdienerabzug | 5'200 | 14'100 | Niedrigeres Erwerbseinkommen ist Person 2. Kanton: 10 % × 56'900 = 5'690, auf das Maximum 5'200 begrenzt. Bund: 50 % × 57'254 = 28'627, auf das Maximum 14'100 begrenzt (ar-wl-2025__c0004). |
> | 18 | **Total Abzüge** | **45'634** | **51'763** | |
> | 20 | **Nettoeinkommen** | **109'276** | **103'147** | 154'910 − Total Abzüge |
> 
> ### Berufskosten (Form. 4)
> | Posten | P1 Kanton | P1 Bund | P2 Kanton | P2 Bund | Regel · Fundstelle |
> |---|---|---|---|---|---|
> | Fahrkosten (Code 400/450) | 0 | 0 | 1'260 | 1'260 | P1: Feld F angekreuzt (Werkbus), also kein Abzug. P2: tatsächliches ÖV-Abo (ar-wl-2025__c0074/0075). |
> | Verpflegung | 1'600 (Ziff. 2.2, Code 410) | 1'600 | 2'640 (Ziff. 2.1, Code 458) | 2'640 | P1: Feld G angekreuzt, 7.50 × 220 = 1'650, auf 1'600 begrenzt. P2: 15 × 176 Tage (ar-form-04-2025__c0003). |
> | Übrige Berufskosten (Code 416/466) | 2'400 | 2'559 | 2'400 | 2'046 | Kanton: 700 + 10 % des Nettolohns, höchstens 2'400. Bund: 3 % des Nettolohns, mindestens 2'000, höchstens 4'000. |
> | **Total** | **4'000** | **4'159** | **6'300** | **5'946** | |
> 
> ### Nach dem Nettoeinkommen
> | Ziff. (Code) | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|
> | 21.1 | Krankheitskosten | 0 | 0 | Keine Belege. Der Selbstbehalt wäre 5 % × 109'276 = 5'463.80. |
> | 21.3 (550) | Spende Krebsliga (Form. 5) | 300 | 300 | Das Total liegt über der Freigrenze von 100 und unter 20 % des Nettoeinkommens (21'855 Kanton, 20'629 Bund). Der Bund-Wert ist `wert bund 2025 spenden` (Art. 33a DBG). |
> | 22 | **Reineinkommen** | **108'976** | **102'847** | 109'276 − 300 bzw. 103'147 − 300 |
> | 23.2 | Kinderabzug Lea | 7'400 | 6'800 | Lea ist am 31.12.2025 vier Jahre alt, die Stufe «nach dem 4. bis zum 15. Altersjahr» gilt. |
> | 23.3 | Kinderabzug Jonas | 11'600 | 6'800 | Jonas ist 16 und in Ausbildung. |
> | 24 | Verheiratetenabzug | – | 2'800 | Nur Bund (Art. 35 DBG). |
> | 24 | **Steuerbares Einkommen** | **89'976** | **86'447** | Kanton: 108'976 − 19'000. Bund: 102'847 − 16'400. |
> 
> Der Bund ermässigt den Steuerbetrag zusätzlich um 2 × 263 = 526. Das macht die Steuerverwaltung automatisch. Der Unterschied zwischen Kanton und Bund ist plausibel: Der Bund hat den höheren Zweiverdienerabzug (+8'900) und die tieferen Versicherungs- und Kinderabzüge.
> 
> ### Vermögen (nur Kanton)
> | Ziff. (Code) | Position | Betrag | Hinweis |
> |---|---|---|---|
> | 30.1 (300) | Wertschriften und Guthaben | 92'000 | 54'000 Konten + 38'000 Aktien (Form. 2). |
> | 33 (322) | Total Vermögenswerte | 92'000 | |
> | 34.1 (504) | Privatschulden | 0 | Keine Angaben. |
> | 35 (326) | Reinvermögen | 92'000 | |
> | 36.2 (332) | Sozialabzug Ehepaar | 150'000 | |
> | 36.3 (334) | Sozialabzug Kinder | 50'000 | 2 × 25'000. Jonas ist am 31.12.2025 minderjährig, hat 2025 aber Jahrgang 2009 (ar-wl-2025__c0122). |
> | 37 (338) | **Steuerbares Vermögen** | **0** | 92'000 − 200'000 = −108'000, mindestens 0. |
> 
> Form. 2, Verrechnungssteueranspruch (Code 999): 35 % × 1'250 = 437.50. Das ist eine Rückerstattung, weder Einkommen noch Abzug.
> 
> ### Nicht zu deklarieren oder nicht abziehbar
> - **PK-Einkauf 4'000:** nicht nochmals unter 13.2 abziehen, er steckt im Nettolohn.
> - **AHV/ALV/NBUV und BVG ordentlich:** schon im Nettolohn. Einzutragen ist Ziff. 11 und nicht der Bruttolohn Ziff. 8.
> - **PK- und 3a-Guthaben:** bis zur Fälligkeit kein Vermögen (ar-wl-2025__c0111).
> - **Verrechnungssteuer 437.50:** siehe oben.
> - **Kita-Mittagessen 1'800:** Lebenshaltung, nicht abziehbar (ar-wl-2025__c0091).
> - **Turnverein 120:** Mitgliederbeitrag, bei den Zuwendungen nicht abziehbar (21.3).
> - **Handy-Abo 960:** private Lebenshaltung. Berufskosten sind mit der Pauschale abgegolten, einen höheren effektiven Nachweis gibt es nicht.
> - **Steuerschlussrechnung 2024 (9'870):** Steuern sind nicht abziehbar. Das ist die allgemeine Regel, im Wiki habe ich dazu keine Fundstelle gefunden.
> - **Miete und Kantonsschulkosten Jonas:** kein Abzug. Zusätzlich zum Kinderabzug sind Schulgelder nicht abziehbar (23.3).
> 
> ### Hinweise für die Fachperson
> 1. **Verpflegung Person 2 (Ziff. 2.1, 2'640):** Ich habe den Standardfall erfasst, weil «Mittagessen auswärts» angegeben ist. Dieser Abzug setzt aber voraus, dass die Heimkehr über Mittag nicht zumutbar ist (Herisau–St. Gallen). Wenn sie zumutbar wäre, entfielen 2'640. Dann wären die Berufskosten von Person 2 3'660 (Kanton) bzw. 3'306 (Bund), das Nettoeinkommen läge bei 111'916 bzw. 105'787, und der Zweiverdienerabzug bliebe am Maximum. Bitte beim Mandanten nachfragen.
> 2. **Kita:** Ich habe angenommen, dass die 14'400 der Bruttobetrag vor der Gutschrift sind. Sind es bereits Nettokosten, dürfen die 2'400 nicht nochmals abgezogen werden.
> 3. **Ziff. 16.1 Bund:** Es sind keine Depot- oder Verwahrungsgebühren belegt. Der Bundesabzug steht deshalb bei 0. Gebühren aus dem Steuerauszug wären nachzutragen.
> 4. **Zinsen 160:** Ich habe Spalte B angenommen. Bitte prüfen, ob kein einzelnes Konto über 200 Franken Zins liegt.
> 5. **Jonas:** Der kantonale Kinderabzug entfällt bei eigenen Einkünften über 18'000 oder Reinvermögen über 250'000 (23.3). Dazu liegen keine Angaben vor.
> 6. **Fehlende Angaben und Belege:** Vorjahresveranlagung zum Vermögensvergleich, Motorfahrzeuge (30.4), Bargeld (30.2), Schulden, Krankheits- und Zahnarztkosten, Bankgebühren. Fehlendes blockiert die übrigen Positionen nicht.
> 7. **Beilagen:** Beizulegen sind beide Lohnausweise und beide 3a-Bescheinigungen. Die PK-Bestätigung ist bereitzuhalten. Auf Verlangen: Kita-Rechnungen, Spendenquittung, Prämienbescheinigung, ÖV-Abo.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

