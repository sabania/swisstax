# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 20:04
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


**Antwort des Agenten** (133.9 s · Tools: 20 Aufrufe read, steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__rechne, steuerwiki__suche, steuerwiki__wert):

> Die Berechnungen für Einkünfte, Abzüge und Nettoeinkommen stehen. Ich rechne noch Reineinkommen, Sozialabzüge, steuerbares Einkommen und Vermögen, dann folgt die Ausfüllhilfe.
> 
> **Ausfüllhilfe: Kanton ZH · Steuerjahr 2025**
> Ehepaar Marco und Sandra, Winterthur, Formular Steuererklärung ZH 2025 (Form. 300) mit Hilfsblättern 340, 360 und 365. Alle Beträge in ganzen Franken, ausser dem Verrechnungssteueranspruch. Status aller Werte: ☑️ agent-geprüft, Abnahme durch die Fachperson offen. Auf dem Formular tragen Sie Staat und Bund je in die eigene Spalte ein (zh-form-300-2025__c0007).
> 
> ## 1. Einkünfte
> 
> | Ziffer | Code | Position | Staat | Bund | Beleg und Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb Marco | 103'000 | 103'000 | Lohnausweis Ziff. 11. Kontrolle: 118'400 − 8'110 − 7'290 = 103'000 | Beleg «Lohnausweis» |
> | 1.1 | 101 | Haupterwerb Sandra | 67'200 | 67'200 | Lohnausweis Ziff. 11. Kontrolle: 76'800 − 5'260 − 4'340 = 67'200. Die Kinderzulagen von 4'800 sind darin enthalten | Beleg «Lohnausweis» |
> | 4.1 | 150 | Ertrag Wertschriften und Guthaben | 1'140 | 1'140 | Dividenden 960 (Kolonne A) + Sparzins 180 (Kolonne B) | zh-form-340-2025__c0005 |
> | 7 | 199 | **Total der Einkünfte** | **171'340** | **171'340** | 103'000 + 67'200 + 1'140 | |
> 
> **Form. 340 (Wertschriftenverzeichnis):**
> - Kolonne A: Dividenden 960 (Code 2309), VSt-Anspruch 336.00 (Code 540, = 35 % × 960).
> - Kolonne B: Sparkonto 180 (Code 542). Der Zins liegt unter 200 und hat keinen VSt-Abzug (zh-wl-2025__c0168). Das Privatkonto hat 0 Zins.
> - Steuerwerte: Sparkonto 42'500, Privatkonto 8'300, Depot 31'200. Total 82'000 (Code 400).
> - Der VSt-Anspruch von 336.00 ist weder Einkommen noch Abzug. Er wird zurückerstattet, die IBAN ist anzugeben.
> - Der Steuerauszug der Bank kann beigelegt werden, wenn im Verzeichnis darauf verwiesen wird.
> 
> Ziff. 3.4 (Kinderzulagen direkt von der Ausgleichskasse, Code 142/143) bleibt leer. Die Zulagen stecken bereits im Lohn von Sandra. Sonst wären sie doppelt erfasst.
> 
> ## 2. Abzüge
> 
> **Berufsauslagen Marco, Form. 360 (Ziff. 11.1, Code 220)**
> 
> | Form. 360 | Code | Staat | Bund | Rechnung |
> |---|---|---|---|---|
> | 1.1 ÖV-Abo Winterthur–Zug | 201 | 4'180 | 3'300 | Plafond Staat 5'200, Bund 3'300 (zh-form-360-2025__c0001) |
> | 2.1 Verpflegung voll | 208 | 3'200 | 3'200 | min(220 × 15; 3'200). Feld G nicht angekreuzt |
> | 3 Übrige Berufskosten pauschal | 212 | 3'090 | 3'090 | 3 % × 103'000, innerhalb 2'000 bis 4'000 |
> | 6 Total | 220 | **10'470** | **9'590** | |
> 
> Feld F ist nicht angekreuzt, also bleibt der Fahrkostenabzug bestehen. Das Abo wird nur beim Bund auf 3'300 gekürzt.
> 
> **Berufsauslagen Sandra, Form. 360 (Ziff. 11.2, Code 240)**
> 
> | Form. 360 | Code | Staat | Bund | Rechnung |
> |---|---|---|---|---|
> | 1.2 Velo pauschal | 222 | 700 | 700 | Pauschale, kein Beleg nötig |
> | 2.1 Verpflegung verbilligt | 226 | 1'320 | 1'320 | min(176 × 7.50; 1'600). Feld G angekreuzt |
> | 3 Übrige Berufskosten pauschal | 232 | 2'016 | 2'016 | 3 % × 67'200 |
> | 6 Total | 240 | **4'036** | **4'036** | |
> 
> **Hauptformular**
> 
> | Ziffer | Code | Position | Staat | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 11.1 | 220 | Berufsauslagen Marco | 10'470 | 9'590 | siehe oben | zh-form-360-2025__c0001 |
> | 11.2 | 240 | Berufsauslagen Sandra | 4'036 | 4'036 | siehe oben | |
> | 14.1 | 260 | Säule 3a Marco | 7'258 | 7'258 | min(7'258; 7'258) mit 2. Säule. Effektiv: Code 262 | zh-wl-2025__c0081 |
> | 14.2 | 261 | Säule 3a Sandra | 7'258 | 7'258 | wie Marco. Effektiv: Code 263 | zh-wl-2025__c0081 |
> | 15 | 270 | Versicherungsprämien | 8'400 | 5'100 | siehe unten | zh-form-365-2025__c0001, c0002 |
> | 16.1 | 280 | PK-Einkauf Marco | 10'000 | 10'000 | Einkauf direkt überwiesen, Lohnausweis Ziff. 10.2 = 0, also kein Doppelabzug | zh-wl-2025__c0092 |
> | 16.3 | 283 | Verwaltung bewegliches Privatvermögen | 94 | 0 | siehe unten | zh-wl-2025__c0095 |
> | 16.6 | 376 | Drittbetreuung Kinder | 31'900 | 32'700 | siehe unten | zh-stg-2025__par-31-t4 |
> | 17 | 290 | Sonderabzug Zweiverdiener | 6'100 | 14'100 | siehe unten | zh-wl-2025__c0112 |
> | 18 | 299 | **Total der Abzüge** | **85'516** | **90'042** | Summe der obigen Zeilen | |
> 
> **Ziff. 15, Versicherungsprämien (Form. 365)**
> - Teil A: Krankenkasse 15'840 (Code 601) + Sparzinsen 180 (Code 604). Zwischentotal 607 = 16'020. Es gibt keine IPV (Code 605 = 0), also auch Total 606 = 16'020.
> - Teil B Ziff. 1 (Code 611): Staat 5'800 und Bund 3'700, denn beide Ehegatten haben 2. Säule und 3a.
> - Teil B Ziff. 3 (Code 613 bis 615): je Kind 1'300 Staat und 700 Bund, bei zwei Kindern 2'600 bzw. 1'400.
> - Maximalabzug (B): Staat 5'800 + 2'600 = 8'400, Bund 3'700 + 1'400 = 5'100.
> - Teil C (Code 270): der niedrigere Betrag von (A) und (B), also Staat 8'400 und Bund 5'100. Die Prämien von 16'020 übersteigen beide Maxima.
> 
> **Ziff. 16.3, Vermögensverwaltungskosten (Code 283)**
> - Staat: Pauschale 3 ‰ × 31'200 (nur das Depot) = 93.60, gerundet 94. Bankguthaben zählen nicht zur Basis.
> - Bund: im Wiki ist keine Bundes-Pauschale belegt. Die Bundesspalte gilt nur für effektive Gebühren. Ohne Gebührenausweis ist sie 0. Das ist eine Vorbehaltsposition für die Fachperson, die Differenz beträgt 94.
> 
> **Ziff. 16.6, Drittbetreuung (Code 376)**
> - Das Maximum gilt pro Kind.
> - Lena: Staat min(27'300; 25'000) = 25'000, Bund min(27'300; 25'800) = 25'800. Die Differenz von 2'300 bzw. 1'500 ist nicht abziehbar.
> - Noah: 6'900 in beiden Spalten.
> - Total: Staat 31'900, Bund 32'700.
> - Die Aufstellung der bezahlten Kosten mit den Empfängern ist unaufgefordert beizulegen.
> 
> **Ziff. 17, Zweiverdienerabzug (Code 290)**
> - Basis ist das niedrigere verbleibende Erwerbseinkommen, also Sandras: 67'200 − 4'036 − 7'258 = 55'906.
> - Staat: min(55'906; 6'100) = 6'100.
> - Bund: 50 % × 55'906 = 27'953, begrenzt auf 14'100.
> 
> ## 3. Einkommensberechnung
> 
> | Ziffer | Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 19 | 199 | Total der Einkünfte | 171'340 | 171'340 | |
> | 20 | 299 | Total der Abzüge | 85'516 | 90'042 | |
> | 21 | 310 | **Nettoeinkommen** | **85'824** | **81'298** | 171'340 − Abzüge |
> | 22.1 | 320 | Krankheits- und Unfallkosten | 0 | 0 | siehe unten |
> | 22.2 | 324 | Gemeinnützige Zuwendungen | 650 | 650 | siehe unten |
> | 23 | 350 | **Reineinkommen** | **85'174** | **80'648** | |
> | 24.1 | 370 | Kinder im Haushalt (2) | 18'600 | 13'600 | 2 × 9'300 bzw. 2 × 6'800 |
> | 24.3 | 365 | Ehegattenabzug (nur Bund) | – | 2'800 | |
> | 25 / 27 | 390 / 398 | **Steuerbares Einkommen** | **66'574** | **64'248** | 85'174 − 18'600 bzw. 80'648 − 13'600 − 2'800 |
> 
> **Ziff. 22.1, Krankheitskosten:** Zahnarzt 1'850 + Kostenbeteiligung 1'240 = 3'090. Der Selbstbehalt von 5 % des Nettoeinkommens beträgt Staat 4'291.20 und Bund 4'064.90. Die Kosten liegen darunter, also ist der Abzug 0. Form. 370 braucht es nur, wenn Sie trotzdem etwas geltend machen. Die Prämien gehören nicht hierher, sie sind in Ziff. 15 erfasst.
> 
> **Ziff. 22.2, Spenden:** SRK 400 + UNICEF 250 = 650. Das liegt über der Mindestgrenze von 100 und unter dem Maximum von 20 % (Staat 17'164.80, Bund 16'259.60). Beide Empfänger sind steuerbefreit mit Sitz in der Schweiz. Beilegen: Aufstellung der Spenden.
> 
> **Bund, Abzug vom Steuerbetrag (Kinder):** 263 je Kind, also 526. Dieser Abzug wirkt erst bei der Steuerberechnung. Ich habe ihn nicht in die Formularspalten eingerechnet und die Fundstelle nicht separat geöffnet (nur im Formular-Gerüst aufgeführt).
> 
> ## 4. Vermögen
> 
> | Ziffer | Code | Position | Betrag |
> |---|---|---|---|
> | 30.1 | 400 | Wertschriften und Guthaben (Total Form. 340) | 82'000 (42'500 + 8'300 + 31'200) |
> | 33 | 460 | Total der Vermögenswerte | 82'000 |
> | 34 | 470 | Schulden | 0 |
> | 35 / 37 | 490 / 498 | Steuerbares Vermögen | 82'000 |
> 
> Das steuerfreie Vermögen steckt im Tarif, nichts abziehen. Die Ziffern 30.2 bis 32 (Bargeld, Versicherungen, Fahrzeuge, Liegenschaften und Ähnliches) sind leer, mangels Belegen aber nicht geprüft.
> 
> ## 5. Nicht zu deklarieren oder nicht abziehbar
> 
> - **Pensionskasse und Säule 3a als Guthaben:** Vorsorgeguthaben sind bis zur Fälligkeit kein steuerbares Vermögen (zh-wl-2025__c0154).
> - **Hausrat- und Privathaftpflichtversicherung (465):** kein Abzug. Form. 365 kennt nur Kranken-, Unfall-, Lebens- und Rentenversicherung sowie Sparzinsen. Eine ausdrückliche Wegleitungsstelle dazu habe ich nicht gefunden.
> - **Swisscom-Handyrechnungen (1'080):** private Kosten, nicht abziehbar. Berufliche Auslagen deckt die Pauschale in Form. 360 Ziff. 3 ab. Die Suche hat zu Handykosten keine ausdrückliche Stelle geliefert.
> - **Kinderzulagen:** nicht nochmals unter Ziff. 3.4 erfassen, sie stecken schon im Lohn von Sandra.
> - **AHV- und BVG-Beiträge im Lohnausweis (Ziff. 9, 10.1):** schon im Nettolohn abgezogen, nicht nochmals abziehen.
> - **Miete:** kein Abzug (Mieter, keine Liegenschaft).
> - **Kapitalleistungen aus Vorsorge (Ziff. 40, Code 510):** keine, nichts eintragen.
> - **Verrechnungssteuer 336:** kein Einkommen und kein Abzug, nur Rückerstattung.
> - **Kita-Anteil über dem Maximum:** 2'300 beim Staat und 1'500 beim Bund bleiben nicht abziehbar.
> - **Krankheitskosten 3'090:** unter dem Selbstbehalt, keine Auswirkung.
> - **Lena, Verpflegung in der Kita:** wird von den Eltern mitgegeben, es entsteht also kein Verpflegungsanteil.
> 
> ## 6. Offene Punkte und Hinweise für die Fachperson
> 
> 1. **Hort von Noah (6'900):** Ich habe den vollen Betrag erfasst. Verpflegung (Mittagstisch) ist nicht abziehbar (zh-zstb-34-1-bis-2025__c0023). Enthält die Rechnung einen Verpflegungsanteil, ist er abzuziehen. Dann sinken Ziff. 16.6, Netto- und steuerbares Einkommen entsprechend. Bitte Rechnung mit Aufschlüsselung nachfordern.
> 2. **Sandra, Verpflegung:** Feld G ist angekreuzt (Personalrestaurant), deshalb 7.50 × 176 = 1'320. Das ist der Standardfall. Falls sie über Mittag nach Hause geht oder nicht im Personalrestaurant isst, wäre das zu klären.
> 3. **Marco, Verpflegung:** Mit 220 Arbeitstagen × 15 ergeben sich 3'300, begrenzt auf 3'200. Das Mittagessen im Restaurant am Arbeitsort Zug ist plausibel, ein Wochenaufenthalt wurde nicht angegeben.
> 4. **PK-Einkauf Marco (10'000):** Die Sperrfrist beträgt drei Jahre. Bei einem Kapitalbezug aus der Vorsorge in dieser Zeit wird der Abzug verweigert. Aktuell gab es keinen Bezug, Marco sollte aber informiert werden. Die Bescheinigung ist beizulegen. Prüfen Sie, ob das Einkaufspotenzial reicht, das ist aus den Unterlagen nicht ersichtlich.
> 5. **Vermögensverwaltungskosten Bund (Code 283):** Bundesspalte 0, siehe oben. Die Differenz von 94 ist unwesentlich.
> 6. **Plausibilität Staat und Bund:** Das steuerbare Einkommen des Bundes liegt mit 64'248 unter dem des Staats mit 66'574. Das erklärt sich so:
>    - Höhere Bundesabzüge bei Zweiverdiener (+8'000) und Drittbetreuung (+800) und der Ehegattenabzug (+2'800).
>    - Dem stehen tiefere Bundesabzüge bei Versicherung (−3'300), Kinder (−2'000), Fahrkosten (−880) und Vermögensverwaltung (−94) gegenüber.
> 7. Die Wiki-Werte haben den Status ☑️ agent-geprüft. Die endgültige fachliche Beurteilung liegt bei der Fachperson.
> 
> **Beizulegen oder bereitzuhalten:** beide Lohnausweise, Form. 360 (Sandra und Marco), Form. 365, Form. 340 mit Bankauszug, 3a-Bescheinigungen, PK-Einkaufsbescheinigung, Aufstellung der Betreuungskosten, Spendenaufstellung (Belege auf Verlangen). ÖV-Abo-Beleg, Krankenkassenbescheinigung und Zahnarztrechnung bleiben auf Verlangen bereit.

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


**Antwort des Agenten** (110.7 s · Tools: 24 Aufrufe read, steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige, message, steuerwiki__rechne):

> **SG · Steuerjahr 2025 · Alleinerziehende (geschieden), 1 Kind, Mieterin**
> 
> Formular 1 gilt für Kanton und Bund und hat eine Spalte. Die Bundesabweichungen setzt das Steueramt automatisch um (sg-wl-2025__c0173). Die Bundesbeträge unten sind das Ergebnis dieser Anpassung. Alle Werte haben den Status ☑️ agent-geprüft, die Abnahme ist offen. Beträge sind in ganzen Franken und mit `rechne` gerechnet.
> 
> **Erfassung**
> - Nadine gilt als alleinstehend (geschieden, sg-wl-2025__c0016). Der Bund wendet für sie den Einelternfamilien-Tarif an (sg-form-32-2025__c0008).
> - Elias hat Kinderabzug und Kinderzuschläge. Weil sie Alimente erhält, hat sie keinen Abzug nach Ziff. 12.2 (sg-wl-2025__c0084).
> 
> ## Einkünfte
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb unselbständig | 73'000 | 73'000 | Nettolohn Ziff. 11. Kinderzulage 2'400 und BVG 4'610 sind schon enthalten. | Beleg Lohnausweis, sg-wl-2025__c0086 |
> | 4.1 | 146 | Wertschriften/Guthaben | 68 | 68 | Form. 2, Spalte B (ohne VSt, Zins unter Fr. 200). | sg-wl-2025__c0135 |
> | 6.1 | 156 | Unterhaltsbeiträge für minderjährige Kinder | 9'600 | 9'600 | 12 × 800. Steuerbar bei der Empfängerin. | sg-wl-2025__c0068 |
> | 7 | 168 | **Total Einkünfte** | **82'668** | **82'668** | 73'000 + 9'600 + 68 | |
> 
> Form. 2, Code 999 (Verrechnungssteueranspruch) ist 0, weil kein Ertrag in Spalte A steht.
> 
> ## Abzüge
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 10.1 | 404/406 | Fahrkosten Auto (Form. 4 Ziff. 1.3) | 8'000 | 3'300 | 32 km × 2 × 220 Tage = 14'080 km × 0.70 = 9'856, begrenzt auf Maximum Kanton bzw. Bund. | sg-form-4-2025__c0002 |
> | 10.1 | 408 | Verpflegung auswärts (Form. 4 Ziff. 2.1) | 3'200 | 3'200 | min(15 × 220 = 3'300; 3'200). Restaurant, keine Kantine, Feld G leer. | sg-form-4-2025__c0003 |
> | 10.1 | 416 | Übrige Berufskosten pauschal (Form. 4 Ziff. 3.1) | 2'400 | 2'190 | Kanton min(700 + 10 % × 73'000; 2'400). Bund min(max(3 % × 73'000; 2'000); 4'000). | sg-wl-2025__c0080 |
> | 10.1 | 438 | **Total Berufskosten (Form. 4 Ziff. 6)** | **13'600** | **8'690** | Summe der drei Zeilen oben. | |
> | 13.1 | 208 | Säule 3a | 7'258 | 7'258 | Bescheinigung; entspricht dem Maximum mit 2. Säule. | `wert sg 2025 saeule3a` |
> | 13.2 | 218 | PK-Einkauf | 6'000 | 6'000 | Bescheinigung vom 20.10.2025. Lohnausweis Ziff. 10.2 ist 0, also kein Doppelabzug. | sg-wl-2025__c0086 |
> | 14 | 600 | Versicherungsprämien/Sparzinsen | 4'500 | 2'500 | A = 5'280 + 1'320 − 1'800 (IPV) + 68 = 4'868. B Kanton = 3'400 + 1'100 (Kind) = 4'500. B Bund = 1'800 + 700 = 2'500. Abzug = min(A; B). Form. 6 Teil A: a = 6'600, d = 68, e = 1'800. | sg-form-6-2025__c0002 |
> | 16.2 | 258 | Kinderbetreuung (Form. 10) | 8'760 | 8'760 | 9'840 − 1'080 Mahlzeiten (separat ausgewiesen). Unter den Limiten 26'700 bzw. 25'800. | sg-wl-2025__c0092 |
> | 16.4 | 223 | Weiterbildung Excel-Kurs | 400 | 340 | Kanton: Pauschale 400 ist höher als die effektiven 340. Bund: nur effektive Kosten. | sg-wl-2025__c0094 |
> | 18 | 230 | **Total Abzüge** | **40'518** | **33'548** | Kanton: 13'600 + 7'258 + 6'000 + 4'500 + 8'760 + 400. Bund: 8'690 + 7'258 + 6'000 + 2'500 + 8'760 + 340. | |
> 
> Ziff. 17 (Zweiverdienerabzug), Ziff. 11 (Schuldzinsen), Ziff. 12 und Ziff. 16.1 (kein Depot) entfallen.
> 
> ## Einkommensberechnung
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 20 | 234 | **Nettoeinkommen** | **42'150** | **49'120** | 82'668 − Total Abzüge |
> | 21.1 | 650 / 238 / 240 | Krankheitskosten | 3'600 / 843 / 2'757 | 3'600 / 2'456 / 1'144 | Vorkolonne 850 + 2'750 = 3'600. Selbstbehalt Kanton 2 % × 42'150 = 843, Bund 5 % × 49'120 = 2'456. Abzug = 3'600 − Selbstbehalt. |
> | 21.3 | 244 | Spenden | 0 | 0 | 80 liegt unter der Mindestgrenze von 100 (sg-stg-2025__art-46, bund-dbg-2025__art-33a). |
> | 22 | 248 | **Reineinkommen** | **39'393** | **47'976** | 42'150 − 2'757, bzw. 49'120 − 1'144 |
> | 23.2 | 254 | Kinderabzug Schule | 10'800 | 6'800 | Elias besucht seit 08/2025 den Kindergarten und gilt damit als schulpflichtig. Ziff. 23.1 (Vorschule, 7'600) entfällt (sg-wl-2025__c0104). |
> | 24 | 268 | **Steuerbares Einkommen** | **28'593** | **41'176** | 39'393 − 10'800, bzw. 47'976 − 6'800 |
> 
> Beim Bund kommt zusätzlich der Abzug vom Steuerbetrag von höchstens Fr. 263 je Kind (Ziff. 23.2). Er wird bei der Veranlagung automatisch angewendet.
> 
> ## Vermögen
> 
> | Ziff. | Code | Position | Betrag | Rechenweg |
> |---|---|---|---|---|
> | 30.1 | 300 | Wertschriften/Guthaben (Raiffeisen-Sparkonto) | 31'500 | Steuerwert 31.12.2025 laut Steuerauszug |
> | 30.4 | 306 | Motorfahrzeug | ⬜ offen | Anschaffungswert − 20 % × Jahre seit Erwerb (sg-wl-2025__c0111). Beleg fehlt. |
> | 33 / 35 | 322 / 326 | Total Vermögenswerte / Reinvermögen | 31'500 + Auto | Keine Schulden. |
> | 36 | 330 | Sozialabzug Vermögen | 75'000 + 20'000 (Kind) = 95'000 | Voll in die eigene Ziffer eintragen. |
> | 37 | 338 | **Steuerbares Vermögen** | **0** | max(31'500 − 95'000; 0). Das gilt auch, wenn der Autowert noch dazukommt, solange das Total unter 95'000 bleibt. |
> 
> Das Vermögen wird nur im Kanton besteuert (Bund: kein Vermögenssteuerwert). Pensionskassen- und 3a-Guthaben gehören nicht ins Vermögen (sg-wl-2025__c0107).
> 
> ## Nicht zu deklarieren bzw. nicht abziehbar
> - **Motorfahrzeugsteuer 410 und Auto-Haftpflicht/Kasko 1'020:** Sie sind mit dem Kilometeransatz von 0.70 abgegolten. Bei Ziff. 14 sind Motorfahrzeug- und Haftpflichtversicherungen ausdrücklich ausgeschlossen.
> - **Handy-Abo 720:** Die Pauschale für übrige Berufskosten deckt es ab. Ein Einzelabzug ist nur bei Verzicht auf die Pauschale und mit Nachweis der beruflichen Nutzung möglich. Das lohnt sich nicht (Pauschale Kanton 2'400, Bund 2'190).
> - **Spende Caritas 80:** unter der Mindestgrenze von 100, daher kein Abzug.
> - **Kinderzulage 2'400 und BVG ordentlich 4'610:** Beides ist schon im Nettolohn berücksichtigt. Ziff. 3.5 und ein weiterer Abzug bei Ziff. 13.2 entfallen.
> - **Prämienverbilligung 1'800:** Sie ist kein Einkommen, wird aber in Form. 6 Teil A, Zeile e abgezogen (Wirkung bei Ziff. 14).
> - **Kinderabzug und Alimente:** Ziff. 12.1/12.2 ist nur für den zahlenden Ex-Mann relevant. Nadine versteuert die Alimente bei 6.1.
> - **Miete, Hausrat, Kleider:** weder Einkommen noch Vermögen.
> 
> ## Fehlende Belege und offene Punkte
> 1. **Auto-Anschaffungswert und Erwerbsjahr** für Ziff. 30.4. Das Steuerergebnis ändert sich dadurch voraussichtlich nicht.
> 2. **Beilagen:**
>    - Scheidungsurteil oder Unterhaltsvereinbarung samt Zahlungsnachweis (Ziff. 6.1, bei erstmaliger Deklaration)
>    - Form. 10 für die Kinderbetreuung (Vorname, Name und Adresse der Kita)
>    - PK-Einkaufsbescheinigung samt Einkaufsberechnung (immer)
>    - Steuerauszug Raiffeisen (Form. 2)
>    - Lohnausweis
>    - Form. 6 mit Auflistung der Zahnarzt- und Franchise-Kosten (die Leistungsabrechnung nur bei Verweis auf den Kassenauszug)
> 3. **Fahrkosten Auto (Ermessen der Behörde):** Die Begründung «Fehlen eines öffentlichen Verkehrsmittels» im Form. 4 Ziff. 1.3 stützt sich auf Arbeitsbeginn 06:00 und erste Verbindung 06:40. Ob das Steueramt das anerkennt, ist nicht belegt. Fahrplanauszug oder Arbeitgeberbestätigung bereithalten. Bei Ablehnung gälten nur die fiktiven ÖV-Kosten. Das Ergebnis müsste dann mit einem ÖV-Abo-Preis neu berechnet werden.
> 4. **Kinderbetreuung Bund:** Betreuung ausserhalb der Arbeitszeit ist beim Bund nicht abziehbar. Ich gehe davon aus, dass die Tagesstruktur-Zeiten mit Nadines Arbeitszeiten zusammenhängen. Falls ein Teil der Rechnungen darüber hinausgeht, ist der Bundesbetrag zu kürzen.
> 5. **PK-Einkauf:** Er sollte beim Einkaufspotenzial der Pensionskasse liegen. Für Kapitalbezüge gilt eine Sperrfrist von 3 Jahren, dazu habe ich keine Fundstelle geprüft.
> 6. **Status:** Alle Werte sind ☑️ agent-geprüft und von der Fachperson abzunehmen.

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


**Antwort des Agenten** (117.9 s · Tools: 31 Aufrufe read, steuerwiki__formular, steuerwiki__position, steuerwiki__zeige, steuerwiki__suche, steuerwiki__wert, steuerwiki__beleg, steuerwiki__rechne):

> Kurzer Zwischenstand: Die Positionen und Limiten für TG 2025 sind geklärt. Ich prüfe noch die nicht abziehbaren Belege (Serafe, Handy, Hausrat) und rechne dann alles exakt durch.
> 
> **TG · Steuerjahr 2025 · Ausfüllhilfe verwitwete Rentnerin, alleinstehend, Frauenfeld (EFH selbstbewohnt)**
> 
> Formular: Steuererklärung 2025 TG (Formular 1) mit Hilfsblättern 2, 4.1, 5.1, 5.2, 6, 7 und 8. Es gibt zwei Spalten, links Staat/Gemeinde und rechts Bund (tg-wl-2025__c0196). Beträge in ganzen Franken. Alle Werte haben den Status ☑️ agent-geprüft, die Abnahme durch die Fachperson ist offen.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | Staat | Bund | Beleg | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|---|
> | 3.1 | 130 | AHV-Rente | 27'000 | 27'000 | AHV-Bescheinigung | 12 × 2'250, zu 100 % steuerbar (tg-wl-2025__c0076) |
> | 3.2 | 132 | PK-Rente | 10'800 (100 %) | 10'800 (100 %) | PK-Bescheinigung | 12 × 900. Bruttobetrag und «100 %» eintragen. Rentenbeginn 2020, also kein Übergangsrecht (80 % nur bei Beginn vor 2002, tg-wl-2025__c0077) |
> | 4 | 150 | Wertschriften- und Zinserträge (Übertrag Form. 2) | 2'160 | 2'350 | TKB-Steuerauszug | Bruttoertrag 250 + 2'100 = 2'350. Kanton minus Vermögensverwaltungspauschale 190 (Code 148) = 2'160 |
> | 8.1 | 180 | Liegenschaften, Nettoerfolg (Form. 7) | 4'840 | 8'920 | Liegenschaftensteuerrechnung, Handwerkerrechnungen | siehe Abschnitt 3 |
> | 6 / 9 | 175 / 198 | Total der Einkünfte | **44'800** | **49'070** | | |
> 
> Form. 2 (Wertschriftenverzeichnis):
> - **Sparkonto:** Der Bruttozins von 250 liegt über Fr. 200. Er gehört deshalb in Spalte 8 (mit Verrechnungssteuer). Steuerwert 48'000 in Spalte 7.
> - **Depot:** Die Dividenden von 2'100 stehen ebenfalls in Spalte 8. Steuerwert 95'000 in Spalte 7.
> - **Verrechnungssteueranspruch (Ziff. 10):** 35 % × 2'350 = **822.50**. Das entspricht 87.50 + 735. Es ist eine Rückerstattung, weder Einkommen noch Abzug (tg-form-02-2025__c0006).
> - **Vermögensverwaltungspauschale Kanton:** 2 ‰ × 95'000 = 190. Das Sparkonto zählt nicht zur Bemessung (tg-wl-2025__c0159).
> - **Bund:** Eine Bundespauschale ist im Wiki nicht belegt. Ich habe die Bundesspalte deshalb ohne Pauschale gerechnet (2'350). Das ist ein Punkt für die Fachperson.
> 
> ## 2. Abzüge
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 11 | 290 | Schuldzinsen (Form. 4.1 A, Code 286) | 3'150 | 3'150 | Hypothekarzinsen 2025. Das Limit (Vermögensertrag + 50'000) ist weit unterschritten (tg-wl-2025__c0173). Gläubiger mit Adresse und Zinssatz angeben |
> | 14 | 330 | Versicherungsprämien und Sparzinsen (Form. 5.2) | 3'500 | 2'700 | Zeile 1: Krankenkasse 6'240 (keine Prämienverbilligung). Zeile 4: Sparzinsen 250. Total A5 (Code 324) = 6'490. Zulässig ist der tiefere Betrag aus A5 und B4. **Bund: 2'700**, weil keine Beiträge an Säule 2 oder 3a geleistet wurden (nicht 1'800). Kanton: 3'500 |
> | 19 | 360 | Total Abzüge | **6'650** | **5'850** | 3'150 + 3'500 bzw. 3'150 + 2'700 |
> | 22 | 362 | Nettoeinkommen | **38'150** | **43'220** | 44'800 − 6'650 bzw. 49'070 − 5'850 |
> | 23.1 | 364 | Krankheitskosten (Form. 5.1 D) | 4'632 | 4'379 | siehe unten |
> | 23.2 | 366 | Freiwillige Zuwendungen (Form. 6) | 350 | 550 | Spenden total 550. Kanton minus Selbbehalt 200 = 350. Bund: ab Fr. 100 ohne Selbstbehalt = 550. Das 20 %-Maximum (7'630 bzw. 8'644) ist nicht erreicht |
> | 24 | 372 | Reineinkommen | **33'168** | **38'291** | 38'150 − 4'632 − 350 bzw. 43'220 − 4'379 − 550 |
> 
> **Krankheitskosten (Form. 5.1)**
> - **A (selbst getragen):** Franchise/Selbstbehalt 1'000 (A1) + Zahnarzt 4'440 + Brille 1'400 = 6'840.
> - **B (Vergütungen):** 300 von der Zusatzversicherung für die Brille.
> - **Netto:** 6'540.
> - **Selbstbehalt 5 % vom Nettoeinkommen Ziff. 22:** Kanton 1'907.50, Bund 2'161.
> - **Abzug:** Kanton 4'632.50, auf 4'632 abgerundet. Bund 4'379.
> - Krankenkassenprämien gehören nicht hierher, sondern in Ziff. 14.
> 
> Beim Brillenbeleg ist die ärztliche Verordnung beizulegen.
> 
> ## 3. Liegenschaft (Form. 7 und 8, Code 180)
> 
> | Schritt | Staat | Bund |
> |---|---|---|
> | Indexierter Mietwert (Liegenschaftensteuerrechnung) | 20'400 | 20'400 |
> | Selbstnutzungsabzug (Kanton 40 %, Bund 20 %) | −8'160 | −4'080 |
> | Steuerbarer Eigenmietwert | 12'240 | 16'320 |
> | Pauschale 20 % (Gebäude 1986, älter als 10 Jahre) | 2'448 | 3'264 |
> | **Effektiv (Form. 8)** | **7'400** | **7'400** |
> | **Nettoerfolg (Code 180)** | **4'840** | **8'920** |
> 
> Der Selbstnutzungsabzug gilt, weil die Liegenschaft am Wohnsitz dauernd selbst bewohnt wird (tg-wl-2025__c0225).
> 
> Die effektiven Kosten sind höher als die Pauschale. Ich habe sie deshalb in beiden Spalten gewählt:
> - **Malerarbeiten Innenrenovation (Ersatzanstrich):** 6'400. Das ist Instandhaltung und abziehbar. Die Rechnung ist beizulegen, weil sie über Fr. 1'000 liegt (tg-wl-2025__c0234).
> - **Gebäudeversicherungsprämie:** 520. Sachversicherungsprämien der Liegenschaft sind abziehbar (tg-wl-2025__c0227).
> - **Baumschnitt/Gartenpflege:** 480. Das habe ich als Unterhalts- und Betriebskosten behandelt. Garten ist in den abgerufenen Wegleitungs-Chunks nicht ausdrücklich genannt. Das ist ein Punkt für die Fachperson.
> - **Wintergarten-Anbau 31'000:** Der Anbau ist wertvermehrend und nicht abziehbar (tg-wl-2025__c0233). Er gehört in Form. 8 in die Spalte «Anlagekosten/Mehrwert». Er erhöht eventuell künftig den Steuerwert und den Mietwert (Neuschätzung).
> 
> ## 4. Sozialabzüge und steuerbares Einkommen
> 
> | Ziff. | Code | Position | Staat | Bund | Regel |
> |---|---|---|---|---|---|
> | 25.3 | 388 | Abzug für AHV-Rentner/Verwitwete | **1'000** | kein Abzug | Reineinkommen 33'168 liegt im Band 32'900–33'899 der Tabelle (tg-wl-2025__c0116/c0117). Kontrolle: 4'200 − 200 × 16 = 1'000. Nur Kanton |
> | 25.1 / 25.2 / 25.4 | | Kinder, Unterstützte, Gemeinsame Besteuerung | – | – | nicht zutreffend |
> | 26 | 398 | **Steuerbares Einkommen** | **32'168** | **38'291** | 33'168 − 1'000 |
> 
> Plausibilität: Das Bundeseinkommen liegt um rund 6'100 höher. Das ist erklärbar durch den tieferen Selbstnutzungsabzug (+4'080), den Versicherungsabzug (−800), den Abzug 25.3 (−1'000) und die Selbstbehalt-Effekte bei Krankheitskosten und Spenden.
> 
> ## 5. Vermögen (Stichtag 31.12.2025)
> 
> | Ziff. | Code | Position | Betrag |
> |---|---|---|---|
> | 30.1 | 410 | Wertschriften und Guthaben (Übertrag Form. 2): Sparkonto 48'000 + Depot 95'000 | 143'000 |
> | 31 | 430 | Liegenschaft, Steuerwert (Form. 7) | 410'000 |
> | 33 | 464 | Total Vermögenswerte | 553'000 |
> | 34 | 466 | Schulden (Form. 4.1 A, Code 455): Hypothek | 180'000 |
> | 35 | 468 | Reinvermögen | 373'000 |
> | 36.2 | 472 | Steuerfreier Abzug alleinstehend | 100'000 |
> | 37 | 498 | **Steuerbares Vermögen** | **273'000** |
> 
> Der Freibetrag gilt nur für das Vermögen (Kanton); für den Bund gibt es keine Vermögenssteuer. Ziff. 36.1 und 36.3 sind nicht zutreffend. Die Pensionskassenrente begründet kein Vorsorgevermögen, ein Vermögen aus Säule 2/3a liegt nicht vor (tg-wl-2025__c0139).
> 
> ## 6. Was nicht zu deklarieren bzw. nicht abziehbar ist
> 
> - **Wintergarten-Anbau 31'000:** keine Unterhaltskosten (siehe Abschnitt 3).
> - **Hausratversicherung 380:** weder Liegenschaftsunterhalt noch Versicherungsabzug. Die Wegleitung nennt Hausrat- und Privathaftpflichtversicherung ausdrücklich als nicht abziehbar (tg-wl-2025__c0227). Beleg nicht einreichen.
> - **Serafe 335 und Handyrechnung:** Lebenshaltungskosten, nicht abziehbar (Art. 34 DBG, bund-dbg-2025__art-34). Die Wiki-Beleglage ist dafür allgemein («private Alltagsrechnungen»), nicht Serafe-spezifisch.
> - **Krankenkassenprämien 6'240:** nicht bei den Krankheitskosten, sondern nur in Ziff. 14.
> - **Verrechnungssteuer 822.50:** weder Einkommen noch Abzug, sondern Rückerstattung über Form. 2 Ziff. 10.
> - **Amortisationen:** keine angegeben. Sie wären ohnehin nicht abziehbar.
> - **Nicht zutreffend:** Erwerbsabzüge (Berufsauslagen, Fahrkosten), Säule 3a (Ziff. 13), Zweiverdienerabzug und Kinderabzüge.
> 
> ## 7. Fehlende Angaben und Prüfpunkte für die Fachperson
> 
> 1. **Zahnarzt 4'440:** Ich habe angenommen, dass die Krankenkasse oder Zusatzversicherung nichts vergütet hat (B nur 300 für die Brille). Bitte die Leistungsabrechnung prüfen. Die Krone darf kein Schönheitseingriff sein.
> 2. **Spenden:** Krebsliga Thurgau und Pro Senectute Thurgau müssen auf der Liste der steuerbefreiten Institutionen der Steuerverwaltung TG stehen. Das habe ich nicht geprüft.
> 3. **Vermögensverwaltungspauschale Bund:** nicht im Wiki belegt (siehe Abschnitt 1).
> 4. **Gartenpflege 480:** Abgrenzung als Unterhalt, siehe Abschnitt 3.
> 5. **Rundung Selbstbehalt Krankheitskosten:** Kanton 1'907.50, ich habe auf 4'632 abgerundet. Bei 4'633 steigt das Reineinkommen nicht, der Abzug 25.3 bleibt gleich.
> 6. **Übertragbare Unterhaltskosten 2023/2024 (Form. 8):** keine Angaben vorhanden. Prüfen, ob solche vorhanden sind.
> 7. **Eigenmietwert 20'400:** Ich habe ihn als indexierten Mietwert 2025 gemäss Liegenschaftensteuerrechnung/Schätzung übernommen. Wenn das der Mietwert vor Indexierung ist, ändert sich der Nettoerfolg.
> 8. **Belege einreichen:** Steuerauszug TKB (Pflicht, wenn die Titel nur als Total deklariert werden), Depotverzeichnis, Rechnungskopien über Fr. 1'000 (Maler), Krankheitskostenbelege und ärztliche Verordnung (Brille).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

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


**Antwort des Agenten** (142.1 s · Tools: 34 Aufrufe read, steuerwiki__formular, read, steuerwiki__position, steuerwiki__beleg, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne):

> Kurzer Zwischenstand: Die Positionen sind erfasst. Ich prüfe noch den Wortlaut zu Kinderabzug Lea (Altersgrenze 4 Jahre) und Verpflegung Person 2 und rechne dann alle Totale.
> 
> **Ausfüllhilfe AR · Steuerjahr 2025 · Ehepaar Herisau (gemeinsam veranlagt), 2 Kinder**
> 
> Formular: Steuererklärung 2025 AR (Formular 1 + Hilfsblätter 2, 4, 5, 6, 10). Das AR-Formular hat keine Bundesspalte. Man trägt einmal ein, und die Steuerverwaltung passt die Bundessteuer automatisch an (ar-wl-2025__c0179). Die Bundesbeträge unten sind deshalb Kontrollwerte und keine Eintragungen.
> 
> Status bei allen Zahlen: ☑️ agent-geprüft (Abnahme offen), sofern nichts anderes steht. Beträge in ganzen Franken.
> 
> ## Einkünfte
> 
> | Ziffer | Code | Position | Kanton | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 P1 | 100 | Nettolohn Haupterwerb | 85'300 | 85'300 | LA Ziff. 11. Probe: 98'000 − 6'860 − 5'840. | ar-wl-2025__c0035 |
> | 1.1 P2 | 102 | Nettolohn Haupterwerb | 68'200 | 68'200 | LA Ziff. 11. Probe: 82'000 − 5'740 − 4'060 − 4'000. Kinder-/Ausbildungszulagen sind in Ziff. 8 enthalten, also Lohnbestandteil. | ar-wl-2025__c0054 |
> | 4.1 | 146 | Wertschriftenerträge (Form. 2) | 1'410 | 1'410 | Zinsen 160 + Dividenden 1'250, brutto | ar-form-02-2025__c0007 |
> | **7** | 168 | **Total Einkünfte** | **154'910** | **154'910** | | |
> 
> **Form. 2 (Wertschriftenverzeichnis)**
> - Spalte A (mit VSt): Aktien, Steuerwert 38'000, Ertrag 1'250.
> - Spalte B (ohne VSt): Konten, Steuerwert 54'000, Ertrag 160. Der Zins liegt unter der Freigrenze von Fr. 200 (ar-wl-2025__c0136).
> - Code 999, Verrechnungssteueranspruch: 35 % × 1'250 = **437.50**. Das ist eine Rückerstattung, weder Einkommen noch Abzug. Rappen sind hier verlangt.
> 
> ## Abzüge
> 
> | Ziffer | Code | Position | Kanton | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 10.1 | 438 | Berufskosten P1 (Form. 4 Ziff. 6) | 4'000 | 4'159 | Fahrkosten 0 (Feld F). Verpflegung 1'600 (Ziff. 2.2, Code 410: 220 × 7.50 = 1'650, max. 1'600). Übrige: Kanton min(700 + 10 % × 85'300; 2'400) = 2'400, Bund 3 % × 85'300 = 2'559. | ar-form-04-2025__c0003, ar-wl-2025__c0075/c0076 |
> | 10.2 | 488 | Berufskosten P2 (Form. 4 Ziff. 6) | 6'300 | 5'946 | Abo 1'260 (Code 450). Verpflegung 2'640 (Ziff. 2.1, Code 458: 176 × 15). Übrige: Kanton 2'400, Bund 3 % × 68'200 = 2'046 (Minimum 2'000 greift nicht). | ar-form-04-2025__c0007 |
> | 13.1 | – | Säule 3a (P1 7'258 + P2 5'000) | 12'258 | 12'258 | Beide ≤ 7'258 (mit 2. Säule). Bescheinigungen beilegen. | ar-wl-2025__c0003/c0083 |
> | 13.2 | – | PK-Einkauf P2 | 0 | 0 | 4'000 sind schon im Nettolohn (LA Ziff. 10.2) und werden nicht nochmals abgezogen. | ar-wl-2025__c0084 |
> | 14 | 600 | Versicherungsprämien (Form. 6) | 7'400 | 5'100 | A = 13'900 + Sparzinsen 160 = 14'060. B Kanton = 5'400 + 2 × 1'000, Bund = 3'700 + 2 × 700. Abzug = kleineres von A und B. | ar-form-06-2025__c0002 |
> | 16.1 | – | Verwaltungskosten Wertschriften | 276 | 0 (siehe Hinweise) | Pauschale 3 ‰ × (54'000 + 38'000) = 276 | ar-wl-2025__c0003 |
> | 16.2 | – | Kinderbetreuung Lea (Form. 10) | 10'200 | 10'200 | 14'400 − 1'800 Mittagessen − 2'400 Betreuungsbeitrag. Maximum 25'000 bzw. 25'800. | ar-form-10-2025__c0001, ar-wl-2025__c0091 |
> | 17 | – | Zweiverdienerabzug | 5'200 | 14'100 | Niedrigeres Erwerbseinkommen ist P2. Kanton E = 68'200 − 6'300 − 5'000 = 56'900 → 10 % = 5'690, Maximum 5'200. Bund E = 57'254 → 50 % = 28'627, Maximum 14'100. | ar-wl-2025__c0004 |
> | **18** | – | **Total Abzüge** | **45'634** | **51'763** | | |
> | **20** | – | **Nettoeinkommen** | **109'276** | **103'147** | | |
> | 21.3 | 550 | Spende Krebsliga (Form. 5) | 300 | 300 | Über 100 und unter 20 % des Nettoeinkommens (Kanton Limite 21'855) | ar-form-05-2025__c0003 |
> | **22** | – | **Reineinkommen** | **108'976** | **102'847** | | |
> | 23.2 | – | Kinderabzug Lea (Kanton) | 7'400 | 6'800 | Siehe Hinweis 1 | ar-wl-2025__c0005 |
> | 23.3 | – | Kinderabzug Jonas (Kanton) | 11'600 | 6'800 | Kantonsschule, minderjährig | ar-stg-anhang-kp__c0001 |
> | – | – | Verheiratetenabzug | – | 2'800 | Nur Bund (bund-dbg-2025__art-35) | |
> | **24** | – | **Steuerbares Einkommen** | **89'976** | **86'447** | Bund: 102'847 − 13'600 − 2'800 | |
> 
> Beim Bund kommt der Steuerverwaltung zufolge noch eine Steuerbetragsermässigung von 2 × 263 = 526 dazu (bund-dbg-2025__art-36-t4). Sie wirkt im Tarif.
> 
> Krankheitskosten (Ziff. 21.1/21.2) fallen keine an.
> 
> ## Vermögen (nur Kanton, der Bund erhebt keine Vermögenssteuer)
> 
> | Ziffer | Code | Position | Betrag |
> |---|---|---|---|
> | 30.1 | 300 | Konten 54'000 + Aktien 38'000 | 92'000 |
> | 33 | 322 | Total Vermögenswerte | 92'000 |
> | 34.1 | 504 | Privatschulden | 0 |
> | 35 | 326 | Reinvermögen | 92'000 |
> | 36.2 | 332 | Sozialabzug Ehegatten | 150'000 |
> | 36.3 | 334 | 2 minderjährige Kinder mit Kinderabzug × 25'000 | 50'000 |
> | **37** | 338 | **Steuerbares Vermögen** | **0** |
> 
> Die Sozialabzüge stehen in voller Höhe in ihren Ziffern (ar-wl-2025__c0122, ar-stg__art-51). Das steuerbare Vermögen ist erst danach mindestens 0.
> 
> Die Codes für Ziff. 10.1/10.2, 13–17, 23 und 30–37 sind im Wiki nicht oder nur aus der Formular-Miniatur verifiziert. Bitte am Originalformular prüfen.
> 
> ## Nicht zu deklarieren bzw. nicht abziehbar
> 
> - **Turnverein-Mitgliederbeitrag 120:** kein Abzug. Mitgliederbeiträge sind bei Ziff. 21.3 ausgeschlossen (ar-wl-2025__c0102). Ziff. 16.3 gilt nur für politische Parteien.
> - **Handy-Abo 960:** Lebenshaltungskosten, kein Abzug. Die Pauschale für übrige Berufskosten ist schon enthalten. Ein höherer effektiver Abzug ist nicht belegt.
> - **Schlussrechnung Steuern 2024 (9'870):** Steuern sind nicht abziehbar und keine Einkünfte. Der Beleg bleibt zu den Akten.
> - **Kita-Mittagessen 1'800:** nicht abziehbar, Lebenshaltungskosten (ar-wl-2025__c0091).
> - **Kantonaler Betreuungsbeitrag 2'400:** nicht separat als Einkommen. Er wird nur als «erhaltene Beiträge» in Form. 10 abgezogen.
> - **PK-Einkauf 4'000 bei Ziff. 13.2:** nicht nochmals abziehen (siehe oben). Die PK-Bestätigung gehört trotzdem zu den Unterlagen.
> - **Pensionskassen- und Säule-3a-Guthaben:** kein steuerbares Vermögen, nicht deklarieren (ar-wl-2025__c0111).
> - **Kinder- und Ausbildungszulagen:** nicht zusätzlich in Ziff. 3.5. Sie stehen schon in Ziff. 8 des Lohnausweises.
> - **Fahrkosten P1:** 0, wegen Feld F (Werkbus).
> - **Prämienverbilligung:** keine, also kein Abzug in Form. 6 A e.
> - **Eigenmietwert, Liegenschaftsunterhalt, Schuldzinsen:** entfallen (Mieter, keine Schulden).
> 
> ## Hinweise für die Fachperson
> 
> 1. **Kinderabzug Lea (⚠️ Auslegung):** Sie hat am 14.03.2025 den 4. Geburtstag gefeiert. Ich habe daher 23.2 (7'400, «nach Vollendung des 4. Altersjahrs») gewählt. Wäre sie noch in 23.1, wären es 5'300, also 2'100 weniger Abzug. Das ändert auch die Basis der Versicherungsabzüge nicht, da beide Stufen den Zuschlag auslösen. Im Wiki ist der Wortlaut nur als Kurzübersicht belegt (ar-wl-2025__c0005). Bitte am Formular Seite 1 gegen das Geburtsjahr prüfen.
> 2. **Verpflegung P2 (Annahme):** Ich habe 2.1 mit 15 × 176 = 2'640 erfasst, weil «Mittagessen auswärts» angegeben ist. Die Wegleitung verlangt, dass die Heimkehr zum Mittagessen nicht möglich ist. Sonst gibt es den Abzug nur für Mehrkosten gegenüber zu Hause (ar-wl-2025__c0076). Rückfrage an den Mandanten: Wie lang ist die Mittagspause, und ist die Heimkehr von St. Gallen nach Herisau möglich? Falls ja, entfällt der Abzug (−2'640 bei den Berufskosten P2). Der Zweiverdienerabzug bleibt dann beim Maximum 5'200 (Bund 14'100), und das Nettoeinkommen steigt um 2'640. Für Person 2 ist keine Schichtarbeit (2.3) erfasst, weil Tagesschicht.
> 3. **Verpflegung P1:** Feld G ist angekreuzt, also der halbe Abzug (1'600). Ein Abzug 0 wäre nur zulässig, wenn die Verbilligung offensichtlich alle Mehrkosten deckt. Das ist hier nicht erkennbar, ich habe 1'600 stehen lassen.
> 4. **Ziff. 16.1 Bund:** Das Wiki belegt für den Bund nur effektive Verwahrungskosten. Keine Depotgebühren sind belegt, also Bund 0. Die Pauschale 276 trägt man im Formular ein, die Verwaltung passt die Bundessteuer an (ar-wl-2025__c0179).
> 5. **Ziff. 13.2 (⚠️ strittig):** Die Wegleitung widerspricht sich bei der Zuordnung von BVG-Beiträgen (13.2 gegenüber 16.6). Hier ohne Folge, weil der Einkauf im Nettolohn steckt.
> 6. **Zweiverdienerabzug:** Die Berechnung ist ohne Code im Wiki verifiziert. Der Einkauf 4'000 wird bei E nicht nochmals abgezogen, weil er schon im Nettolohn steckt.
> 7. **Fahrkosten-Maximum Bund:** Das Wiki nennt 3'300, die ESTV-Wegleitung nennt 3'200. Das ist hier ohne Folge, weil das Abo 1'260 beträgt.
> 8. **Beilagen:** Lohnausweise, 3a-Bescheinigungen und PK-Bescheinigung gehören immer dazu. Krankenkassenbescheinigung, Kita-Rechnungen, Abo und Spendenquittung gibt es auf Verlangen. Den Steuerauszug legt man bei, wenn dessen Gesamtbetrag ins Form. 2 übertragen wird.
> 9. **Plausibilität:** Das steuerbare Einkommen von Bund (86'447) und Kanton (89'976) ist stimmig. Die Differenz entsteht durch Zweiverdiener-, Versicherungs- und Kinderabzüge. Ich habe keine Vorjahresveranlagung zum Vergleich.
> 
> Die fachliche Beurteilung und Abnahme bleibt bei der Fachperson.

