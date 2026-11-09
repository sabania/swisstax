# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuermem` · Fragen: 4 · Lauf: 2026-11-09 09:38
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


**Antwort des Agenten** (265.2 s · Tools: 30 Aufrufe read, ls, memory_search, exec):

> Ich lese noch die restlichen Wegleitungs-Abschnitte (Krankheitskosten, Lohnausweis-Regeln) und die Belegkarten, dann rechne ich den Fall.
> 
> Ich prüfe gerade noch die Drittbetreuungs-Regel (Verpflegung/Hort) und die Zweiverdiener-Basis, dann rechne ich alles durch.
> 
> # Ausfüllhilfe Steuerjahr 2025 · Kanton ZH · Ehepaar Marco und Sandra, Winterthur
> 
> **Rahmen:** Staat/Gemeinde (Staat) und direkte Bundessteuer (Bund) sind getrennt gerechnet. Formulare: Form. 300 mit Hilfsblättern 340, 360, 365 und 367. Alle Werte haben Status ☑️ (agent-geprüft); ✅ ist keiner verifiziert, die fachliche Abnahme steht aus. Quellen: `quick/wegleitung-zh-2025.md`, `werte-zh-2025.md`, `werte-bund-2025.md`, jeweils mit Chunk-Fundstelle.
> 
> Ein Punkt beeinflusst die Totale: **Sandras Verpflegungsabzug** (Ziff. 11.2) ist offen. Ich habe ihn im Basisfall mit 0 gerechnet (Begründung unter den Berufsauslagen). Als Variante ergibt er +1'320 Abzug.
> 
> ## 1. Einkünfte (Form. 300 S. 2)
> 
> | Ziff. / Code | Position | Staat | Bund | Rechenweg · Fundstelle |
> |---|---|---|---|---|
> | 1.1 / 100 | Haupterwerb Marco | 103'000 | 103'000 | LA Ziff. 11. Kontrolle: 118'400 − 8'110 − 7'290 = 103'000 ✓. [zh-form-300-2025__c0004] |
> | 1.1 / 101 | Haupterwerb Sandra | 67'200 | 67'200 | LA Ziff. 11. Kontrolle: 76'800 − 5'260 − 4'340 = 67'200 ✓. Die Kinderzulagen 4'800 sind im Lohn enthalten und nicht separat zu erfassen. |
> | 4.1 / 150 | Wertschriften- und Guthabenertrag (Form. 340) | 1'140 | 1'140 | Kolonne A: Dividenden 960 (VSt 336 = 35 % ✓). Kolonne B: Sparzins 180 (Zins ≤ 200, ohne VSt). Privatkonto: Zins 0. [zh-form-340-2025__c0005] |
> | Form. 340 / 540 | VSt-Anspruch | 336.00 | – | 35 % × 960. Rückforderung mit dem Wertschriftenverzeichnis beantragen (IBAN angeben). |
> | **7 / 199** | **Total Einkünfte** | **171'340** | **171'340** | 103'000 + 67'200 + 1'140 |
> 
> ## 2. Berufsauslagen (Form. 360, Total → Ziff. 11.1 / 11.2)
> 
> **Marco (Code 220):**
> 
> | Ziff. / Code | Staat | Bund | Rechenweg · Fundstelle |
> |---|---|---|---|
> | 1.1 / 201 ÖV-Abo | 4'180 | 3'300 | Feld F leer, also abziehbar. Plafond Staat 5'200 / Bund 3'300 (Zwischentotal 205). [zh-wl-2025__c0065] |
> | 2.1 voll / 208 Verpflegung | 3'200 | 3'200 | Feld G leer, Restaurant, Heimkehr Winterthur–Zug unmöglich. 220 × 15 = 3'300, gedeckelt auf 3'200. [zh-pauschalierung-berufsauslagen-2025__c0004; zh-wl-2025__c0066] |
> | 3 / 212 übrige Pauschale | 3'090 | 3'090 | 3 % × 103'000 (Min 2'000, Max 4'000). […__c0005] |
> | **Total 220** | **10'470** | **9'590** | |
> 
> **Sandra (Code 240; Codes der Person-2-Spalte, jeweils +20 gegenüber Person 1):**
> 
> | Ziff. / Code | Staat | Bund | Rechenweg · Fundstelle |
> |---|---|---|---|
> | 1.2 / 222 Velo-Pauschale | 700 | 700 | Ständige Benützung, ohne Beleg. [zh-pauschalierung-berufsauslagen-2025__c0001] |
> | 2.1 verbilligt / 226 Verpflegung | 0 (bedingt) | 0 (bedingt) | Feld G angekreuzt, also nur der reduzierte Ansatz 7.50 pro Tag. Voraussetzung ist aber, dass die Pause die Heimkehr nicht ermöglicht. Wohn- und Arbeitsort sind beide Winterthur, daher Basisfall 0 (siehe Offene Punkte). |
> | 3 / 232 übrige Pauschale | 2'016 | 2'016 | 3 % × 67'200 = 2'016 (Min 2'000 ✓). |
> | **Total 240** | **2'716** | **2'716** | Variante mit Verpflegung: 176 × 7.50 = 1'320, also Total 4'036. |
> 
> ## 3. Abzüge (Form. 300 S. 3)
> 
> | Ziff. / Code | Position | Staat | Bund | Rechenweg · Fundstelle |
> |---|---|---|---|---|
> | 11.1 / 220 | Berufsauslagen Marco | 10'470 | 9'590 | siehe oben |
> | 11.2 / 240 | Berufsauslagen Sandra | 2'716 | 2'716 | siehe oben |
> | 14.1 / 260 | Säule 3a Marco | 7'258 | 7'258 | min(7'258; Max mit 2. Säule 7'258). PK-Beiträge laut LA Ziff. 10.1 ✓. [zh-wl-2025__c0081; BSV Masszahlen] |
> | 14.2 / 261 | Säule 3a Sandra | 7'258 | 7'258 | wie oben |
> | 15 / 270 | Versicherungsprämien (Form. 365) | 8'400 | 5'100 | A (606): KK 15'840 + Sparzins 180 = 16'020, ohne IPV. B (616): Staat 5'800 + 2 × 1'300; Bund 3'700 + 2 × 700. Abzug = min(A; B) = B. «Mit Vorsorge»-Maxima, da 2. Säule und 3a bezahlt wurden. [zh-form-365-2025__c0001, __c0002; zh-wl-2025__c0086] |
> | 16.1 / 280 | PK-Einkauf Marco | 10'000 | 10'000 | Formular 21 EDP. LA Ziff. 10.2 = 0, daher nicht doppelt. Bezahlt am 14.11.2025. Kein Kapitalbezug in den letzten 3 Jahren ✓. |
> | 16.6 / 376 | Drittbetreuung | 31'900 | 32'700 | Lena: Staat min(27'300; 25'000) = 25'000, Bund min(27'300; 25'800) = 25'800. Noah: 6'900 (< 14 Jahre, unter dem Maximum). [zh-stg-2025__par-31-t4; zh-wl-2025__c0107] |
> | 17 / 290 | Zweiverdienerabzug | 6'100 | 14'100 | Basis Sandra = 67'200 − 2'716 − 7'258 = 57'226. Staat min(57'226; 6'100). Bund min(max(50 % = 28'613; 8'600); 14'100). [zh-stg-2025__par-31-t5; zh-wl-2025__c0112] |
> | **18 / 299** | **Total Abzüge** | **84'102** | **88'722** | |
> 
> Nicht belegt, daher leer: Ziff. 12 Schuldzinsen, 13 Unterhalt, 16.2 Weiterbildung, 16.4 Behinderung, 16.5 Parteien.
> 
> ## 4. Einkommensberechnung und Sozialabzüge
> 
> | Ziff. / Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|
> | 21 / 310 | Nettoeinkommen | 87'238 | 82'618 | 171'340 − Abzüge |
> | 22.1 / 320 | Krankheitskosten | **0** | **0** | Kosten 1'850 + 1'240 = 3'090. Selbstbehalt 5 %: Staat 4'361.90 / Bund 4'130.90. Die Kosten liegen darunter, also kein Abzug. |
> | 22.2 / 324 | Spenden | 650 | 650 | SRK 400 + UNICEF 250 = 650 (≥ 100; Limite 20 % × Ziff. 21). [zh-stg-2025__par-32] |
> | 23 / 350 | Reineinkommen | 86'588 | 81'968 | |
> | 24.1 / 370 | Kinder im Haushalt | 18'600 | 13'600 | 2 × 9'300 bzw. 2 × 6'800. Lena (2021) und Noah (2016) sind minderjährig. [zh-stg-2025__par-34] |
> | 24.3 / 365 | Verheiratetenabzug | – | 2'800 | nur Spalte Bund |
> | **25 / 390** | **Steuerbares Einkommen** | **67'988** | **65'568** | Mit der Variante «Sandra Verpflegung» sind es 66'668 / 64'248. |
> 
> ## 5. Vermögen (Form. 300 S. 4, nur Staat)
> 
> | Ziff. / Code | Position | Betrag | Rechenweg |
> |---|---|---|---|
> | 30.1 / 400 | Wertschriften und Guthaben | 82'000 | Sparkonto 42'500 + Privatkonto 8'300 + Depot 31'200 |
> | 33 / 460 | Total Vermögenswerte | 82'000 | |
> | 34 / 470 | Schulden | 0 | keine belegt |
> | 35 / 490, 37 / 498 | Steuerbares Vermögen | 82'000 | Kein Abzug eintragen. Der Freibetrag von 159'000 (Verheiratetentarif) wirkt über den Tarif, die Vermögenssteuer dürfte 0 sein. [zh-stg-2025__par-47-t2] |
> 
> Der Bund erhebt keine Vermögenssteuer. Ziff. 40 (Kapitalleistungen) und Ziff. 50 (Schenkungen/Erbschaften) bleiben leer. Auf Seite 1 sind beide Kinder einzutragen (Jg. 2021 und 2016), und «Pensionskassenbeiträge: ja» ist für beide anzukreuzen.
> 
> ## 6. Nicht zu deklarieren bzw. kein Abzug
> 
> - **Swisscom-Handy 1'080:** privater Lebenshaltungsaufwand. Ein beruflicher Anteil ist in der Pauschale «übrige Berufskosten» enthalten.
> - **Hausrat- und Privathaftpflichtversicherung 465:** nicht abziehbar und nicht Teil des Versicherungsabzugs.
> - **Zahnarzt 1'850 und Kostenbeteiligung 1'240:** unter dem Selbstbehalt, also Abzug 0. Form. 370 ist nicht nötig, Belege aufbewahren.
> - **Krankenkassenprämien:** keine Krankheitskosten, sie laufen nur über Ziff. 15.
> - **Mietzins Winterthur:** nicht abziehbar.
> - **Kinderzulagen 4'800:** bereits im Lohn, nicht nochmals in Ziff. 3.4.
> - **Kita-Verpflegung** (Eltern geben sie mit): kein Thema, die Rechnung ist reine Betreuung.
> - **PK- und 3a-Guthaben:** nicht ins Wertschriftenverzeichnis und nicht ins Vermögen.
> - **Bund, Abzug vom Steuerbetrag je Kind (CHF 263):** kein Formularfeld, rechnet das Steueramt. [bund-dbg-2025__art-36-t4]
> - **Bezahlte Steuern:** nicht abziehbar.
> 
> ## 7. Offene Punkte und Rückfragen an die Mandanten
> 
> 1. **Sandra, Mittagessen:** Sandra arbeitet in Winterthur und wohnt dort, und sie fährt mit dem Velo. Die Wegleitung gewährt den Abzug nur, wenn die Arbeitspause die Heimkehr nicht ermöglicht [zh-wl-2025__c0066]. Wie lang ist die Pause? Falls Heimkehr nicht möglich, +1'320 (Ziff. 11.2 / Code 226). Für den Bund zusätzlich klären, was die Mahlzeit im Personalrestaurant kostet: bis CHF 10 gibt es dort keinen Abzug (Art. 6 Abs. 3 BKV).
> 2. **Marco, Verpflegung:** Der Abzug erreicht das Maximum bei 214 oder mehr Tagen mit auswärtigem Mittagessen. Gab es Homeoffice-Tage? Dann sinkt der Abzug unter 3'200.
> 3. **Noah, Hort 6'900:** Ist ein Mittagstisch oder Schulgeld enthalten? Das wäre auszuscheiden (Verpflegung ist nicht betreuungsbedingt). Für Lena und Noah Rechnungen mit Zahlungsnachweis einreichen. Gibt es städtische Betreuungsbeiträge, die die Kosten mindern?
> 4. **PK-Einkauf:** Bescheinigung (Formular 21 EDP) mit der Steuererklärung einreichen. Beachten, dass ein Kapitalbezug innert 3 Jahren nach dem Einkauf den Abzug gefährdet.
> 5. **Weitere Vermögenswerte und Schulden:** Gibt es Kinderkonti (Jg. 2008 und jünger gehören ins Wertschriftenverzeichnis der Eltern), Bargeld, Fahrzeuge, Krypto, rückkaufsfähige Lebensversicherungen, Kredite oder Leasing?
> 6. **Familienzulagen:** Wurden weitere Zulagen direkt von der Ausgleichskasse ausbezahlt (Ziff. 3.4)? Hat auch Marcos Arbeitgeber Zulagen bezahlt?
> 7. **Depot-Verwaltungskosten (Ziff. 16.3 / Code 283):** Das Depot-Total ist 31'200. Die Pauschale beträgt 3 ‰ × 31'200 = 93.60 (Staat, ohne Nachweis) [zh-wl-2025__c0095]. Sie ist hier nicht eingerechnet und nur sinnvoll, wenn die Bank das Depot verwaltet oder verwahrt. Der Bund-Pauschalbetrag ist im Wiki nicht erfasst.
> 8. **Vorjahresveranlagung 2024** anfordern: Plausibilisierung der Vermögensentwicklung und wiederkehrende Korrekturen.
> 9. **Spenden:** Sind SRK und UNICEF im Verzeichnis der steuerbefreiten Institutionen geführt? Quittungen als Liste beilegen.
> 
> ## 8. Hinweise für SB/ML
> 
> - **Bund-Fahrkostenplafond:** Gesetz und RS 2-210 nennen 3'300, die ESTV-WL 2a 2025 S. 6 nennt noch «3200». Ich habe 3'300 gerechnet, das Gesetz geht vor [bund-dbg-2025__art-26]. Die Differenz beträgt 100 beim Bund und nur bei Marco.
> - **Übrige Berufskosten Sandra:** Die Basis ist LA Ziff. 11 inkl. Kinderzulagen. Ohne Zulagen würde das Minimum 2'000 greifen (Differenz −16). Das Wiki regelt das nicht.
> - **Krankheitskosten:** Die Schwelle liegt bei Staat ca. 1'272 / Bund ca. 1'041 über den heutigen 3'090. Weitere Kosten (Brille, Therapien) können den Abzug auslösen. Prüfen, ob die Zahnarztrechnung in der KK-Abrechnung doppelt enthalten ist.
> - **Robustheit:** Zweiverdiener- und Versicherungsabzug sind gedeckelt, die Varianten ändern sie nicht.
> - **Nicht gerechnet:** Steuerbeträge und Tarif. Gemeindesteuerfuss und Kirchensteuer fehlen.

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


**Antwort des Agenten** (177.7 s · Tools: 26 Aufrufe read, exec):

> Ich lese gerade die SG-2025-Wegleitung und die Eckwerte. Als Nächstes folgen die Ziffern 20–24, die Hilfsblätter (Berufskosten, Krankheitskosten, Zuwendungen) und die Belegrelevanz.
> 
> Ich prüfe noch die Regel «Fehlen eines öffentlichen Verkehrsmittels» bei den Fahrkosten (StB 39 Nr. 3), danach rechne ich alles zusammen.
> 
> Die Ausfüllhilfe für Nadine (SG, Steuerjahr 2025) steht unten. Grundlage sind die Kompakt-Wegleitung SG 2025, die Eckwerte SG und Bund 2025 und die zitierten Chunks im Wiki. Alle verwendeten Wiki-Werte sind ☑️ (agent-geprüft); keiner ist ✅ verifiziert. Die fachliche Abnahme liegt bei SB/ML.
> 
> Zur Spaltenlogik: Im SG-Hauptformular trägt Nadine nur die Kantonswerte ein. Die Bundesabweichungen setzt das Steueramt automatisch um (WL SG 2025, Form. 4 Ziff. 6 und Form. 5, Teil B). Die Bundsspalte zeigt, was dabei herauskommen muss.
> 
> **Mandant:** N. (alleinerziehend, geschieden) · **Kanton:** SG · **Steuerjahr:** 2025 · **Formular:** Form. 1 mit Hilfsblättern 2, 4, 5, 6 und 10
> 
> ## Einkünfte
> 
> | Ziffer | Code | Position | Staat | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb unselbständig | 73'000 | 73'000 | Lohnausweis Ziff. 11. Rechnung: 83'500 − 5'890 − 4'610 = 73'000. Die Kinderzulage 2'400 steckt schon im Bruttolohn (nicht zusätzlich in Ziff. 3.5). Feld F/G leer, also keine Kürzung. | [Form. 1 S. 2](steuerwiki/chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0004.md) |
> | 4.1 / Form. 2 | 146 | Sparzins Raiffeisen | 68 | 68 | Form. 2 Abschnitt B (Bankzins ≤ 200 ohne VSt). Trotzdem deklarieren. | [Form. 1 S. 2](steuerwiki/chunks/sg/2025/sg-form-1-2025/sg-form-1-2025__c0006.md) |
> | 6.1 | **156** | Kinderalimente (Elias, minderjährig) | 9'600 | 9'600 | 12 × 800, voll steuerbar, Zahlungsnachweise. Code 156 (Kinder), nicht 154. | [WL SG 2025 S. 21](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0068.md), Art. 23 lit. f DBG |
> | **7** | 168 | **Total Einkünfte** | **82'668** | **82'668** | 73'000 + 68 + 9'600 | |
> 
> ## Abzüge
> 
> | Ziffer | Code | Position | Staat | Bund | Rechenweg / Regel | Fundstelle |
> |---|---|---|---|---|---|---|
> | 10.1 / Form. 4 | 404/406 | Fahrkosten Privatauto | **8'000** | **3'300** | 32 km × 2 × 220 = 14'080 km × 0.70 = 9'856. Das übersteigt das Maximum (Staat 8'000, Bund 3'300). Begründung «Fehlen eines öffentlichen Verkehrsmittels» (Form. 4 Ziff. 1.3). | [Form. 4 S. 1](steuerwiki/chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0002.md), [StB 39 Nr. 3 Ziff. 2.2.2](steuerwiki/chunks/sg/dauernd/sg-stb-39-3/sg-stb-39-3__c0004.md) |
> | | 408 | Verpflegung auswärts (Restaurant) | 3'200 | 3'200 | min(15 × 220 = 3'300; 3'200). Feld G leer, also voller Satz (Ziff. 2.1, nicht 2.2). | [WL SG 2025 S. 24](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0078.md) |
> | | 416 | Übrige Berufskosten (Pauschale) | 2'400 | 2'190 | Staat: min(700 + 10 % × 73'000; 2'400). Bund: 3 % × 73'000 = 2'190 (zwischen 2'000 und 4'000). | [Form. 4 S. 1](steuerwiki/chunks/sg/2025/sg-form-4-2025/sg-form-4-2025__c0003.md), [BKV Anhang](steuerwiki/chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__anhang-1.md) |
> | **10.1** | **438** | **Total Berufskosten** | **13'600** | **8'690** | 8'000 + 3'200 + 2'400 bzw. 3'300 + 3'200 + 2'190 | |
> | 13.1 | 208 | Säule 3a | 7'258 | 7'258 | Bescheinigung = Maximum mit 2. Säule (7'258) | [WL SG 2025 S. 26](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0085.md) |
> | 13.2 | 218 | PK-Einkauf (direkt bezahlt 20.10.2025) | 6'000 | 6'000 | Lohnausweis Ziff. 10.2 = 0, also kein Doppelabzug. Bescheinigung (Form. 21 EDP) und Einkaufsberechnung beilegen. | [WL SG 2025 S. 26](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0086.md) |
> | 14 / Form. 6 | 600 | Versicherungsprämien | **4'500** | **2'500** | A = 5'280 + 1'320 + 68 (Sparzins) − 1'800 (IPV) = 4'868. Staat: Maximum 3'400 + 1'100 (1 Kind) = 4'500. Bund: 1'800 + 700 = 2'500. Kein Zuschlag «ohne Vorsorge», da 3a/PK abgezogen. | Art. 45 Abs. 1 lit. g StG, [Art. 45-t2](steuerwiki/chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-45-t2.md), [Eckwerte Bund](steuerwiki/quick/werte-bund-2025.md) |
> | 16.2 / Form. 10 | 258 | Kinderdrittbetreuung (Kita) | 8'760 | 8'760 | 9'840 − 1'080 (Mahlzeiten separat ausgewiesen) = 8'760. Das liegt unter dem Maximum (Staat 26'700, Bund 25'800). | [WL SG 2025 S. 28](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0092.md) |
> | 16.4 | 223 | Weiterbildung (Excel-Kurs) | **400** | **340** | Staat: Pauschale 400 ohne Nachweis, günstiger als die effektiven 340. Bund: nur effektive Kosten. | [WL SG 2025 S. 29](steuerwiki/chunks/sg/2025/sg-wl-2025/sg-wl-2025__c0095.md) |
> | **18** | 230 | **Total Abzüge** | **40'518** | **33'548** | | |
> 
> ## Einkommensberechnung
> 
> | Ziffer | Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 20 | 234 | Nettoeinkommen | 42'150 | 49'120 | 82'668 − 40'518 bzw. 82'668 − 33'548 |
> | 21.1 / Form. 6 Rückseite | 650 / 238 / 240 | Krankheitskosten | **2'757** | **1'144** | Vorkolonne 850 (Kostenbeteiligung) + 2'750 (Zahnarzt) = 3'600. Staat: Selbstbehalt 2 % × 42'150 = 843, also 3'600 − 843. Bund: 5 % × 49'120 = 2'456, also 3'600 − 2'456. |
> | 21.3 | 244 | Freiwillige Zuwendungen | 0 | 0 | Caritas 80 liegt unter dem Mindestbetrag von 100 (siehe unten). |
> | 22 | 248 | Reineinkommen | 39'393 | 47'976 | |
> | **23.2** | **254** | Kinderabzug Elias | **10'800** | **6'800** | Kindergarten zählt zur Schulpflicht, daher 23.2 und nicht 23.1 (7'600). Bund: zusätzlich 263 Abzug vom Steuerbetrag. |
> | **24** | 268 | **Steuerbares Einkommen** | **28'593** | **41'176** | Vor Rundung; Rundungsregeln ungeprüft. |
> 
> Der Bund-Wert in Ziff. 24 ist nur Richtgrösse. Für den Tarif gilt Art. 36 Abs. 2bis DBG (Elterntarif, 263 je Kind vom Steuerbetrag, [DBG Art. 36](steuerwiki/chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-36-t4.md)). Beim Staat greift das Splitting für Alleinerziehende mit Kindern (Art. 50 Abs. 4 StG, [Art. 50](steuerwiki/chunks/sg/2025/sg-stg-2025/sg-stg-2025__art-50.md)). Die Steuerberechnung selbst habe ich nicht gemacht.
> 
> ## Vermögen (nur Staat/Gemeinde)
> 
> | Ziffer | Code | Position | Betrag | Hinweis |
> |---|---|---|---|---|
> | 30.1 / Form. 2 | 300 | Sparkonto Raiffeisen per 31.12.2025 | 31'500 | Steuerwert laut Steuerauszug |
> | 30.4 | 306 | Privatauto | **offen** | Anschaffungswert − 20 % × Anschaffungswert × Jahre seit Erwerb. Kaufpreis und Jahr fehlen. |
> | 36.1 + 36.3 | 330 / 334 | Sozialabzüge | 75'000 + 20'000 | Alleinstehend plus 1 minderjähriges Kind |
> | 37 | 338 | Steuerbares Vermögen | voraussichtlich 0 | 31'500 + Auto liegt unter 95'000, solange das Auto weniger als 63'500 wert ist |
> 
> ## Was nicht zu deklarieren bzw. nicht abziehbar ist
> 
> - **Motorfahrzeugsteuer 410, Auto-Haftpflicht/Kasko 1'020:** Lebenshaltungs- bzw. Sachversicherungskosten, nicht abziehbar. Der Fahrkostenabzug (Fr. 0.70/km) ist die einzige Abzugsposition fürs Auto ([Belegkarte Motorfahrzeug-Versicherung](steuerwiki/wiki/belege/beleg-motorfahrzeug-versicherung.md), Wegleitung Ziff. 14).
> - **Handy-Abo 720:** private Lebenshaltung, durch die Pauschale «übrige Berufskosten» abgegolten ([Belegkarte Privatrechnungen](steuerwiki/wiki/belege/beleg-privatrechnungen-alltag.md)).
> - **Spende Caritas 80:** unter dem Mindestbetrag von 100 (Staat und Bund), also kein Abzug.
> - **Kinderzulage 2'400:** schon im Lohnausweis enthalten, nicht nochmals unter Ziff. 3.5 (Code 142).
> - **AHV 5'890 und BVG 4'610:** bereits im Nettolohn abgezogen, nicht erneut bei Ziff. 13.2 oder 14.
> - **Kita-Mahlzeiten 1'080:** nicht abziehbar, aus Ziff. 16.2 ausgeschieden.
> - **Mietzins:** nicht abziehbar.
> - **PK- und 3a-Guthaben:** bis zur Fälligkeit steuerfrei, nicht im Vermögen deklarieren (Wegleitung Ziff. 30.1).
> - **Nicht anwendbar:**
>   - Zweiverdienerabzug (Ziff. 17): Nadine ist nicht verheiratet.
>   - Alimentenabzug (Ziff. 12.2): Nadine erhält die Alimente, sie zahlt keine.
>   - Kinderabzug 23.1: Elias ist schulpflichtig.
>   - Ausbildungskosten 23.3: gilt nicht für den Kindergarten.
>   - Unterstützungsabzug (Ziff. 23.4): kein Fall.
>   - Schichtabzug (Ziff. 2.3): Arbeitsbeginn 06:00 ist keine achtstündige Schicht- oder Nachtarbeit, und Lohnausweis Ziff. 15 enthält keine Schichttage.
> 
> ## Offene Punkte / Rückfragen an die Mandantin
> 
> 1. **Fahrkosten-Begründung:** Fahrplanauszug beilegen (erste Verbindung 06:40, Arbeitsbeginn 06:00). StB 39 Nr. 3 Ziff. 2.2.2 akzeptiert Privatauto, wenn kein öV zur Verfügung steht. Ob 06:40 gegenüber 06:00 als «nicht zur Verfügung» genügt, beurteilt die Fachperson (Ermessen).
> 2. **KK-Prämien brutto?** Sind 5'280 und 1'320 die Bruttoprämien vor IPV? Wenn die IPV schon abgezogen ist, zählt sie doppelt. Der Abzug bleibt wegen der Kappung auf 4'500 bzw. 2'500 gleich, solange die Prämien brutto mindestens 4'432 betragen.
> 3. **Auto:** Kaufpreis und Erwerbsjahr für Ziff. 30.4 erfragen.
> 4. **Zahnarzt 2'750:** Nur Heilbehandlung ist abziehbar. Ästhetische Anteile ausscheiden (Rechnung prüfen).
> 5. **Kita:** Name und Adresse der Betreuungsperson für Form. 10. Beim Bund nur Betreuung während der Arbeitszeit abziehbar; Rechnungen auf Zeiten ausserhalb der Arbeit prüfen.
> 6. **Weitere Spenden:** Sind weitere Zuwendungen da? Ab einer Summe von 100 wären alle abziehbar.
> 7. **Weiterbildung:** Voraussetzung (Sek-II-Abschluss oder Alter 20) ist bei 38 Jahren erfüllt. Zusammenhang zum Beruf muss glaubhaft sein.
> 8. **Alimente:** Urteil bzw. Konvention bereithalten. Die Alimente werden nur bis zum Monat der Volljährigkeit besteuert.
> 
> ## Hinweise für SB/ML
> 
> - **Bund-Fahrkosten 3'300:** DBG Art. 26 und RS 2-210 nennen 3'300. Die ESTV-Wegleitung 2a 2025 S. 6 nennt noch 3'200 ([WL 2a S. 6](steuerwiki/chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0042.md)). Ich habe das Gesetz verwendet; der Widerspruch bleibt offen.
> - **PK-Einkauf:** Die 3-jährige Sperrfrist für Kapitalbezüge (Art. 79b Abs. 3 BVG) gilt ([Thema PK-Einkauf](steuerwiki/wiki/themen/pensionskasse-einkauf-wef.md)). Die Mandantin darf bis Oktober 2028 kein Kapital beziehen, sonst wird der Abzug korrigiert.
> - **3a-Einkauf (BVV 3 Art. 7a):** nicht angewendet. SG 2025 hat dazu keinen Wert (⬜, «für 2025 nicht anwendbar»).
> - **Weiterbildung:** Die Pauschale 400 gilt nur für Kanton und Gemeinde. Das Steueramt setzt beim Bund automatisch die effektiven 340 ein.
> - **Rundung:** Die Rundungsregeln für das steuerbare Einkommen habe ich nicht geprüft.

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


**Antwort des Agenten** (210.2 s · Tools: 22 Aufrufe read, ls, exec):

> # Ausfüllhilfe Steuererklärung 2025: Kanton TG (Frauenfeld), verwitwete Rentnerin, alleinstehend
> 
> Formular 1 TG 2025 mit Hilfsblättern 2, 4.1, 5.1, 5.2, 6, 7 und 8. Quelle der Ziffern und Codes: `quick/wegleitung-tg-2025.md`. Alle Beträge in CHF.
> 
> Der Status ist durchgehend ☑️ (Fundstelle geprüft, fachliche Abnahme steht aus). Davon abweichend sind markiert:
> - ⚠ = Annahme oder Rückfrage nötig.
> - 🟡 = nur extrahiert.
> 
> Die Steuerberechnung (Tarif, Steuerfuss) war nicht verlangt und fehlt. Bei Rappenbeträgen gilt die Rundung des Formulars bzw. der eFisc-Software.
> 
> ## 1. Seite 1 (Personalien)
> - Zivilstand verwitwet (Stand 31.12.2025), Jg. 1955. Keine Kinder, keine unterstützten Personen. Kein Ergänzungsleistungs-Bezug.
> - Wohnsitz Frauenfeld TG am 31.12.2025, ganzjährig steuerpflichtig.
> - Quelle: Formular 1 TG 2025 S. 1 (`tg-form-01-2025__c0002`).
> 
> ## 2. Einkünfte
> 
> | Ziffer / Code | Position | Staat | Bund | Beleg | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 3.1 / 130 | AHV-Rente | 27'000 | 27'000 | AHV-Bescheinigung | 12 × 2'250, zu 100 % | `tg-form-01-2025__c0007` |
> | 3.2 / 132 | PK-Rente | 10'800 | 10'800 | PK-Bescheinigung | 12 × 900, Bruttobetrag, Satz 100 % | `tg-form-01-2025__c0007` |
> | 4 / 150 (Form. 2) | Wertschriften- und Zinsertrag | 2'160 | 2'160 | TKB-Steuerauszug | 250 + 2'100 = 2'350 brutto, minus Vermögensverwaltungskosten 190 | `tg-form-02-2025__c0005`, `__c0006` |
> | 6 und 7 / 175 | Zwischentotal | 39'960 | 39'960 | | 27'000 + 10'800 + 2'160 | `tg-form-01-2025__c0008` |
> | 8.1 / 180 (Form. 7) | Nettoerfolg Liegenschaft | 4'840 | 8'920 | Schätzung, Rechnungen | siehe Abschnitt 3 | `tg-form-01-2025__c0009` |
> | 9 und 20 / 198 | Total der Einkünfte | 44'800 | 48'880 | | 39'960 + 4'840 bzw. 39'960 + 8'920 | `tg-form-01-2025__c0009` |
> 
> **Hilfsblatt Wertschriftenverzeichnis (Formular 2)**
> 
> | Posten | Spalte 7 (Steuerwert) | Spalte 8 (Bruttoertrag mit VSt) |
> |---|---|---|
> | TKB-Sparkonto | 48'000 | 250 |
> | Depot Schweizer Aktien | 95'000 | 2'100 |
> | Total | 143'000 | 2'350 |
> 
> - **Spalte 8:** Der Bruttozins von 250 liegt über 200, deshalb Spalte 8 und nicht 9.
> - **Verrechnungssteuer-Rückerstattung (Ziff. 10):** 35 % × 2'350 = 822.50. Das stimmt mit den abgezogenen 87.50 + 735 überein.
> - **Auszahlung:** Das Konto steht in Formular 1 S. 1.
> - **Vermögensverwaltungskosten (Code 148):** 2 ‰ × 95'000 = 190. Die Bankguthaben zählen für die Pauschale nicht mit.
> - **Fundstelle:** `tg-wl-2025__c0159`, `__c0160`.
> - **⚠ Annahme:** Das Depot gilt als durch die Bank verwaltet. Der Depotgebühren-Ausweis ist anzufordern.
> - **⚠ Bund:** Das Wiki hat für den Bund keine eigene Pauschale (Art. 32 DBG, `bund-dbg-2025__art-32-t1`). Formular 2 liefert nur ein Total für beide Spalten, deshalb wurde derselbe Betrag verwendet.
> 
> ## 3. Liegenschaft (Formular 7 und 8)
> 
> Baujahr 1986, selbst bewohnt am Wohnsitz.
> 
> | | Staat | Bund |
> |---|---|---|
> | Mietwert selbstgenutzt (indexiert, 2025) | 20'400 | 20'400 |
> | Selbstnutzungsabzug (Staat 40 %, Bund 20 %) | −8'160 | −4'080 |
> | Steuerbarer Eigenmietwert | 12'240 | 16'320 |
> | Unterhalt effektiv (siehe unten) | −7'400 | −7'400 |
> | **Nettoerfolg (Ziff. 8.1, Code 180)** | **4'840** | **8'920** |
> 
> Fundstellen:
> - Selbstnutzungsabzug: `tg-wl-2025__c0225`, `__c0243`.
> - Unterhalt: Form. 7 `tg-form-07-2025__c0002`, Form. 8 `tg-form-08-2025__c0001`.
> 
> **Unterhalt, effektiv (Formular 8)**
> 
> | Rechnung | Betrag | Beurteilung |
> |---|---|---|
> | Malerarbeiten (Ersatzanstrich) | 6'400 | abziehbar (Instandhaltung und Ersatz ohne Mehrwert, `tg-wl-2025__c0227`) |
> | Gebäudeversicherung | 520 | abziehbar (Sachversicherungsprämie für die Liegenschaft, `tg-wl-2025__c0227`) |
> | Baumschnitt / Gartenpflege | 480 | abziehbar, soweit mehrjährige Pflanzen und Bäume betroffen sind (`tg-wl-2025__c0228`) |
> | **Total abziehbar** | **7'400** | |
> | Wintergarten-Anbau | 31'000 | **nicht abziehbar** (Anbau, wertvermehrend, `tg-wl-2025__c0233`) |
> 
> **Pauschale statt effektiv?**
> - Das Gebäude ist älter als 10 Jahre, also gilt der Satz 20 % (`tg-wl-2025__c0238`, `tg-stv__par-9`, `bund-lkv__art-5`).
> - Staat: 20 % × 12'240 = 2'448. Bund: 20 % × 16'320 = 3'264.
> - Effektiv (7'400) ist in beiden Spalten höher. Die Wahl gilt pro Liegenschaft und Jahr.
> - Die Rechnung über 6'400 ist als Kopie beizulegen (Einzelbeträge ab 1'000).
> 
> ## 4. Abzüge
> 
> | Ziffer / Code | Position | Staat | Bund | Beleg | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 11 / 290 (Form. 4.1 A: Code 286) | Schuldzinsen | 3'150 | 3'150 | Hypothekarbestätigung | Zinsen 2025 fällig; Schuld 180'000 per 31.12. nach Ziff. 34. Limite Vermögensertrag + 50'000, weit unterschritten. | `tg-form-04-1-2025__c0001` |
> | 14 / 330 (Form. 5.2) | Versicherungsprämien | 3'500 | 2'700 | KK-Bestätigung | Siehe unten | `tg-form-05-2-2025__c0001` bis `__c0003`, `tg-stg__par-34-t3`, `bund-rs-2-210__c0006` |
> | 19 und 21 / 360 | Total Abzüge | 6'650 | 5'850 | | 3'150 + 3'500 bzw. 3'150 + 2'700 | |
> | 22 / 362 | Nettoeinkommen | 38'150 | 43'030 | | 44'800 − 6'650 bzw. 48'880 − 5'850 | |
> 
> **Versicherungsprämien (Formular 5.2)**
> - Zeile A1: Krankenkassenprämien 6'240, ohne Prämienverbilligung.
> - Zeile A4: erhaltene Sparzinsen 250. Das ist der Bruttozins aus Formular 2.
> - Zeile A5 (Code 324): 6'490.
> - Staat: min(6'490; 3'500) = 3'500.
> - Bund: Weil keine Beiträge an 2. Säule oder 3a geleistet wurden, gilt der Ansatz 2'700 statt 1'800. Es ergibt sich min(6'490; 2'700) = 2'700.
> - Das Maximum ist in beiden Spalten ausgeschöpft.
> - Nicht in den Versicherungsabzug gehören die Kostenbeteiligung (1'000), die als Krankheitskosten laufen, und die Hausratversicherung.
> 
> ## 5. Krankheitskosten (Formular 5.1, Ziff. 23.1, Code 364)
> 
> | Posten | Betrag |
> |---|---|
> | A1 Franchise und Selbstbehalt | 1'000 |
> | Zahnarzt (Krone) | 4'440 |
> | Brille (augenärztliche Verordnung) | 1'400 |
> | **Total A** | **6'840** |
> | B Vergütung Zusatzversicherung (Brille) | −300 |
> | **A − B** | **6'540** |
> 
> | | Staat | Bund |
> |---|---|---|
> | Selbstbehalt 5 % × Ziff. 22 | −1'907.50 | −2'151.50 |
> | **Abzug Ziff. 23.1** | **4'632.50** | **4'388.50** |
> 
> Fundstellen: `tg-form-05-1-2025__c0001` bis `__c0004`, `tg-wl-2025__c0197`, `__c0206`, `__c0207`, `tg-stg__par-34-t3`, `bund-dbg-2025__art-33-t3`.
> 
> ## 6. Spenden (Formular 6, Ziff. 23.2, Code 366)
> 
> Krebsliga Thurgau 300 plus Pro Senectute Thurgau 250 ergibt 550. Beide sind einzeln mit Name und Sitz aufzuführen.
> 
> | | Staat | Bund |
> |---|---|---|
> | Rechenweg | 550 − 200 Selbstbehalt; Ziff. 22 ≤ 40'000, also Maximum 8'000 | 550 (ab 100, ohne Selbstbehalt); Maximum 20 % × 43'030 = 8'606 |
> | **Abzug** | **350** | **550** |
> 
> Fundstellen: `tg-form-06-2025__c0002`, `tg-stg__par-34-t4`, `bund-dbg-2025__art-33a`.
> ⚠ Ob beide Organisationen auf der TG-Liste der steuerbefreiten Institutionen stehen, ist im Wiki nicht prüfbar.
> 
> ## 7. Reineinkommen und Sozialabzüge
> 
> | Ziffer / Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|
> | 24 / 372 | Reineinkommen | 33'167.50 | 38'091.50 | Ziff. 22 − 23.1 − 23.2 |
> | 25.3 / 388 | Abzug AHV-Rentner / verwitwet | 1'000 | – | Nur Staat. 4'200 − 200 × 16 volle Tausender über 16'900. WL-Tabelle Zeile 32'900–33'899 = 1'000. |
> | 25.1, 25.2, 25.4, 28 | Kinder, Unterstützte, Verheiratetenabzug, Gutschriften | – | – | Nicht anwendbar |
> | 26 / 398 | **Steuerbares Einkommen** | **32'167.50** | **38'091.50** | |
> 
> Fundstellen: `tg-vakp__par-1`, `tg-wl-2025__c0116`, `__c0117`.
> 
> Beim Staat liegt das Reineinkommen 732.50 unter der nächsten Stufe (33'900 ergäbe 800).
> 
> ## 8. Vermögen (nur Staat)
> 
> | Ziffer / Code | Position | Betrag | Beleg und Rechenweg |
> |---|---|---|---|
> | 30.1 / 410 | Wertschriften und Guthaben | 143'000 | Form. 2, Total Spalte 7 (48'000 + 95'000) |
> | 31 / 430 | Liegenschaft (Form. 7) | 410'000 | Steuerwert laut Schätzung |
> | 33 / 464 | Total Vermögenswerte | 553'000 | |
> | 34 / 466 | Schulden (Form. 4.1, Code 455) | 180'000 | Hypothek per 31.12.2025 |
> | 35 / 468 | Reinvermögen | 373'000 | 553'000 − 180'000 |
> | 36.2 / 472 | Abzug alleinstehend (verwitwet) | −100'000 | |
> | 37 / 498 | **Steuerbares Vermögen** | **273'000** | |
> 
> Fundstellen: `tg-form-01-2025__c0014` bis `__c0016`, `tg-stg__par-53`.
> 
> ## 9. Nicht zu deklarieren oder nicht abziehbar
> 
> | Posten | Betrag | Grund |
> |---|---|---|
> | Wintergarten-Anbau | 31'000 | Kein Unterhalt (Anbau, wertvermehrend). Nicht in Formular 8 als Abzug führen (`tg-wl-2025__c0233`). |
> | Hausratversicherung | 380 | Weder Liegenschaftsunterhalt (`tg-wl-2025__c0227`) noch Versicherungsabzug (`beleg-hausrat-haftpflicht-police`). Die Höchstgrenze ist ohnehin erreicht. |
> | Serafe | 335 | Lebenshaltungskosten, kein Abzug (`beleg-privatrechnungen-alltag`). |
> | Handyrechnung | – | Lebenshaltungskosten, kein Abzug (`beleg-privatrechnungen-alltag`). |
> | Verrechnungssteuer | 822.50 | Nicht als Einkommen. Sie wird über die Rückerstattung in Formular 2 Ziff. 10 geltend gemacht. Die Erträge sind brutto zu deklarieren. |
> | Hausrat, Bargeld, Hypothekar-Amortisation | – | Hausrat ist vermögenssteuerfrei. Amortisationen sind kein Zins. |
> | 2. Säule und Säule 3a | – | Nicht fällige Guthaben wären steuerfrei, bei der Rentnerin aber nicht vorhanden. |
> | Ziff. 13 (3a), 15.2 (PK-Einkauf), 15.1 (AHV Nichterwerbstätige), 10.x (Berufsauslagen) | – | Nicht anwendbar. Es ist keine Erwerbstätigkeit und keine 2. Säule/3a-Einzahlung belegt. |
> | Teilbesteuerungsabzug Ziff. 15.6 | – | Nur bei Beteiligungen ab 10 %. Für ein Streudepot nicht anzunehmen. |
> 
> ## 10. Offene Punkte und Rückfragen an die Mandantin
> 
> 1. **Wintergarten:**
>    - War er am 31.12.2025 fertig?
>    - Ist er im Steuerwert von 410'000 enthalten?
>    - Ist die Schätzung vor oder nach der Fertigstellung erfolgt?
>    - Bei unfertigen Bauten sind noch nicht geschätzte Investitionen angemessen zum Steuerwert hinzuzurechnen (Wegleitung Ziff. 31, Form. 1 S. 4). Eine Neuschätzung erhöht künftig Steuerwert und Mietwert.
> 2. **Malerarbeiten:** Betreffen sie nur bestehende Räume (Ersatz)? Anstriche im Anbau gehören zu den Anlagekosten und wären nicht abziehbar.
> 3. **Garten:** Sind in den 480 nur Baumschnitt und Pflege mehrjähriger Pflanzen enthalten? Rasen- und Gemüsepflege sind nicht abziehbar (`tg-wl-2025__c0228`).
> 4. **Zeitliche Abgrenzung:** Sind alle Unterhaltsrechnungen in der Steuerperiode 2025 angefallen?
> 5. **Zahnarzt:** Hat die Zusatzversicherung oder jemand anderes die Krone (4'440) mitbezahlt? Falls ja, ist die Vergütung in Formular 5.1 Teil B abzuziehen. Die Krankenkassen-Leistungsabrechnung ist beizulegen.
> 6. **Depotgebühren:** Den Ausweis der TKB anfordern. Er dient als Beleg für die Pauschale von 190 oder für höhere effektive Kosten.
> 7. **Spenden:** Gegen die TG-Liste der steuerbefreiten Institutionen prüfen.
> 8. **Weitere Vermögenswerte:** Fahrzeug, Bargeld, Lebens- und Rentenversicherungen mit Rückkaufswert, andere Konten (auch Postkonto oder Kleinstkonten)? Im Belegsatz fehlen sie.
> 9. **Vorjahresveranlagung 2024:** Sie fehlt zur Plausibilisierung. In Formular 8 wären allenfalls übertragbare Unterhaltskosten 2023/2024 zu prüfen. Weil der Nettoerfolg positiv ist, spielt das 2025 voraussichtlich keine Rolle.
> 
> ## 11. Hinweise für SB/ML
> 
> - **Plausibilisierung:**
>   - Sparkonto: 250 auf 48'000 ergeben rund 0.5 %.
>   - Dividende: 2'100 auf 95'000 ergeben rund 2.2 %.
>   - Hypothekarzins: 3'150 auf 180'000 ergeben 1.75 %.
>   - Mietwert: 20'400 auf 410'000 ergeben rund 5 %.
>   - Die Verrechnungssteuer stimmt exakt auf 35 %.
>   - Die PK-Rente hat Beginn 2020, also gilt der Satz 100 % ohne Übergangsrecht.
> - **Bund, Versicherungsabzug:** Der Ansatz 2'700 setzt voraus, dass 2025 keinerlei Beiträge an 2. Säule oder 3a geleistet wurden.
> - **Krankheitskosten:** Die Bemessungsgrösse ist Ziff. 22 je Spalte. Das Gesetz sagt «Reineinkommen», die Wegleitung «Nettoeinkommen Ziff. 22». Hier wurde nach Wegleitung gerechnet.
> - **Eigenmietwert-Abzug im Bund:** Das Wiki führt 20 % als kantonale Vollzugspraxis. Es sind bundesrechtlich keine Werte hinterlegt, die dem widersprechen.
> - **Steuerbetrag:** Er wurde nicht berechnet. Für Staat und Gemeinde fehlt zudem der Steuerfuss der Gemeinde Frauenfeld im Wiki. Der Kantonssteuerfuss 109 % ist nur 🟡 extrahiert.
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


**Antwort des Agenten** (218.3 s · Tools: 19 Aufrufe read, exec):

> Ich lese gerade die AR-2025-Kompakt-Wegleitung (Rest: Zweiverdiener, Vermögen, Berufskosten-Hilfsblatt, Wertschriften, Kita) und prüfe danach die Detailregeln. Dann folgt die Ausfüllhilfe.
> 
> # Ausfüllhilfe Steuererklärung AR 2025: Ehepaar Herisau (Mieter)
> 
> **Mandant:** Ehepaar Herisau, 2 Kinder · **Kanton:** AR · **Steuerjahr:** 2025 · **Formular:** Steuererklärung AR 2025 (Hauptformular + Form. 2, 4, 5, 6, 10).
> Das AR-Formular hat keine eigene Bundesspalte. Die Bundesabweichungen setzt die Steuerverwaltung automatisch (WL AR 2025 S. 33, `ar-wl-2025__c0179`). Die Bundesbeträge stehen hier nur zur Kontrolle.
> 
> Alle Zeilen sind ☑️ (agent-geprüft, fachliche Abnahme steht aus), ausser wo anders vermerkt. Die Codes des Hauptformulars sind teils nicht verifiziert, weil das Hauptformular nicht im Wiki liegt. Dort steht «–».
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | Kanton | Bund | Beleg | Rechenweg / Regel | Fundstelle |
> |---|---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb P1 | 85'300 | 85'300 | LA P1 Ziff. 11 | Nettolohn 98'000 − 6'860 − 5'840 = 85'300 | `ar-wl-2025__c0035` |
> | 1.1 | 102 | Haupterwerb P2 | 68'200 | 68'200 | LA P2 Ziff. 11 | 82'000 − 5'740 − 4'060 − 4'000 = 68'200. Die Zulagen sind im Lohn enthalten. | `ar-wl-2025__c0035` |
> | 4.1 | 146 | Wertschriften und Guthaben (Übertrag Form. 2) | 1'410 | 1'410 | Bank-Steuerauszug | Spalte A: Dividenden 1'250 brutto (VSt 437.50). Spalte B: Kontozinsen 160 (≤ 200, ohne VSt). | `ar-form-02-2025__c0007` |
> | 7 | 168 | **Total Einkünfte** | **154'910** | **154'910** | | 85'300 + 68'200 + 1'410 | |
> 
> Form. 2, Verrechnungssteuer (Code 999): 35 % × 1'250 = **437.50** Rückforderung. Das entspricht dem abgezogenen Betrag und ist plausibel. Die Rückforderung ist an den Wohnsitz AR am 31.12. gebunden.
> 
> ## 2. Abzüge
> 
> **Berufskosten (Form. 4)**
> 
> | Position | P1 Kt. | P1 Bund | P2 Kt. | P2 Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 Fahrkosten ÖV (Code 400/450) | **0** | 0 | 1'260 | 1'260 | P1: Feld F angekreuzt (Werkbus gratis), also kein Abzug. P2: effektives Abo, unter der Limite 6'000 (Kt.) bzw. 3'300 (Bund). | `ar-form-04-2025__c0001`, `…c0003`; `bund-dbg-2025__art-26` |
> | 2.2 Verpflegung verbilligt (Code 410) | 1'600 | 1'600 | – | – | P1: Feld G angekreuzt. 7.50 × 220 = 1'650, begrenzt auf 1'600. | `ar-wl-2025__c0076`; `ar-stv__art-16` |
> | 2.1 Verpflegung auswärts (Code 458) | – | – | 2'640 | 2'640 | P2: 15 × 176 Tage = 2'640 (Max. 3'200). | `ar-form-04-2025__c0003`; `bund-bkv-2025__anhang-1` |
> | 3 Übrige Berufskosten (Code 416/466) | 2'400 | 2'559 | 2'400 | 2'046 | Kt.: 700 + 10 % × Nettolohn, max. 2'400 (beide am Maximum). Bund: 3 % × 85'300 bzw. 68'200 (min. 2'000, max. 4'000). | `ar-stv__art-18`; `bund-bkv-2025__anhang-1` |
> | **6 Total** (Code 438 / 488) | **4'000** | **4'159** | **6'300** | **5'946** | → Ziff. 10.1 (P1), Ziff. 10.2 (P2) | |
> 
> **Übrige Abzüge**
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg / Regel | Fundstelle |
> |---|---|---|---|---|---|---|
> | 13.1 | – | Säule 3a | 12'258 | 12'258 | P1 7'258 (= Maximum mit 2. Säule), P2 5'000. Beide haben eine 2. Säule, daher je eigener Abzug. | `ar-stg__art-35-t2`; `bund-bsv-masszahlen-2025-2026__c0003` |
> | 13.2 | – | PK-Einkauf P2 | **0** | 0 | ⚠️ Die 4'000 stehen im Lohnausweis Ziff. 10.2 und sind bereits im Nettolohn 68'200 abgezogen. Hier nicht nochmals eintragen. | `ar-wl-2025__c0084`; `reports/entscheidungsvorlage-strittig.md` |
> | 14 | 600 | Versicherungsprämien (Form. 6) | 7'400 | 5'100 | A = 13'900 (keine Prämienverbilligung) > Maximum. Kt.: 5'400 + 2 × 1'000. Bund: 3'700 + 2 × 700. | `ar-stg__art-35-t2`; `bund-dbg-2025__art-33-t5`; `ar-form-06-2025__c0002` |
> | 16.2 | – | Kinderbetreuung Lea (Form. 10) | 10'200 | 10'200 | 14'400 − 1'800 Mittagessen − 2'400 Betreuungsbeitrag = 10'200 (Limite 25'000 bzw. 25'800, Kind unter 14). | `ar-form-10-2025__c0001`; `ar-wl-2025__c0091`; `bund-dbg-2025__art-33-t7` |
> | 17 | – | Zweiverdienerabzug | 5'200 | 14'100 | Tieferes Erwerbseinkommen = P2 (Kt. 68'200 − 6'300 − 5'000 = 56'900). Kt.: 10 % = 5'690, Maximum 5'200. Bund: 50 % liegt über dem Maximum 14'100. | `ar-wl-2025__c0004`, `…c0096/97`; `bund-dbg-2025__art-33-t6` |
> | 18 | – | **Total Abzüge Ziff. 10–17** | **45'358** | **51'763** | Summe der obigen Positionen | |
> | 20 | – | **Nettoeinkommen** | **109'552** | **103'147** | 154'910 − Total Abzüge | |
> | 21.3 | 550 | Spende Krebsliga (Form. 5 A) | 300 | 300 | ≥ 100 und unter 20 % des Nettoeinkommens, daher voll abziehbar. | `ar-stg__art-36`; `ar-form-05-2025__c0003` |
> | 22 | – | **Reineinkommen** | **109'252** | **102'847** | Nettoeinkommen − 300 | |
> 
> ## 3. Sozialabzüge
> 
> Stichtag ist der 31.12.2025. Lea (geb. 14.03.2021) hat ihr 4. Altersjahr am 14.03.2025 vollendet und fällt deshalb unter **23.2** (7'400), nicht unter 23.1.
> 
> | Ziff. | Position | Kanton | Bund | Fundstelle |
> |---|---|---|---|---|
> | 23.2 | Lea, 4–15 Jahre | 7'400 | 6'800 | `ar-wl-2025__c0005`; `ar-stg-anhang-kp__c0001` |
> | 23.3 | Jonas (geb. 2009, 16 J., Kantonsschule) | 11'600 | 6'800 | `ar-wl-2025__c0005` |
> | – | Verheiratetenabzug (nur Bund) | – | 2'800 | `bund-dbg-2025__art-35` |
> | 24 | **Steuerbares Einkommen** | **90'252** | **86'447** | Reineinkommen − Sozialabzüge (Kt. 19'000, Bund 16'400) |
> 
> Beim Bund kommen zusätzlich 2 × CHF 263 Abzug vom Steuerbetrag hinzu (`bund-dbg-2025__art-36-t4`). Den Abzug erfasst die Verwaltung.
> 
> ## 4. Vermögen (nur Kanton)
> 
> | Ziff. | Code | Position | Betrag | Fundstelle |
> |---|---|---|---|---|
> | 30.1 | 300 | Konten 54'000 + CH-Aktien 38'000 (Form. 2) | 92'000 | `ar-form-02-2025__c0007` |
> | 33 / 35 | 322 / 326 | Total Vermögenswerte und Reinvermögen (keine Schulden angegeben) | 92'000 | |
> | 36.2 | 332 | Sozialabzug Ehepaar | 150'000 | `ar-stg__art-51` |
> | 36.3 | 334 | 2 minderjährige Kinder mit Kinderabzug × 25'000 | 50'000 | `ar-wl-2025__c0122` |
> | 37 | 338 | **Steuerbares Vermögen** | **0** | 92'000 − 200'000, nicht negativ |
> 
> Das Vermögen ist trotzdem vollständig zu deklarieren.
> 
> ## 5. Nicht zu deklarieren bzw. nicht abziehbar
> 
> - **Steuerschlussrechnung 2024 (9'870):** Bezahlte Steuern sind nicht abziehbar (Art. 34 lit. e DBG, Belegkarte Steuerrechnung).
> - **Handy-Abo (960):** Lebenshaltung, nicht abziehbar. Die berufliche Nutzung ist mit der Pauschale «übrige Berufskosten» abgegolten.
> - **Turnverein-Mitgliederbeitrag (120):** Mitgliederbeiträge sind keine abziehbaren Zuwendungen (Form. 5 A).
> - **PK-Einkauf 4'000:** nicht nochmals bei 13.2 und nicht bei 16.6 (Doppelabzug).
> - **Kinder- und Ausbildungszulagen in Ziff. 8 von P2:** bereits im Nettolohn, nicht zusätzlich bei Ziff. 3.5 (Code 142).
> - **Kita:** Mittagessen (1'800) nicht abziehbar, Betreuungsbeitrag (2'400) abziehen.
> - **Werkbus P1:** kein Fahrkostenabzug.
> - **Mietzins:** nicht abziehbar. Es gibt keinen Eigenmietwert und kein Form. 7.
> - **Krankenkassenprämien:** gehören nur zu Ziff. 14, nicht zu den Krankheitskosten 21.1.
> - **Guthaben Säule 3a und Pensionskasse:** nicht als Vermögen deklarieren.
> - **Verrechnungssteuer 437.50:** kein Abzug, sondern Rückforderung (Code 999).
> 
> ## 6. Offene Punkte und Rückfragen an den Mandanten
> 
> 1. **P1, Feld G:** Isst er tatsächlich in der Kantine bzw. auswärts? Der Abzug 1'600 setzt Mehrkosten gegenüber zu Hause voraus.
> 2. **P2, Verpflegung:** Die Voraussetzung ist, dass eine Heimkehr zum Mittagessen wegen Entfernung oder kurzer Pause nicht zumutbar ist. Herisau–St. Gallen ist ein Ermessensfall für SB/ML.
>    - «Tagesschicht» ist keine Schicht- oder Nachtarbeit nach Form. 4 Ziff. 2.3.
>    - 2.3 wäre ohnehin nicht mit 2.1 kombinierbar und würde denselben Betrag ergeben.
> 3. **Lohnausweise:** Fehlen Spesen (Ziff. 13) oder Bemerkungen (Ziff. 15)? Nicht ereignisbezogene Pauschalspesen schliessen die Pauschale «übrige Berufskosten» aus. Zudem ist der AHV-Satz bei beiden exakt 7.0 % vom Bruttolohn. Bei P2 wäre zu klären, ob die Zulagen AHV-pflichtig verbucht wurden.
> 4. **Kita:** Ist der Rechnungstotal von 14'400 brutto vor der Gutschrift? Sonst würde der Betreuungsbeitrag doppelt abgezogen. Bitte die Verfügung zum Betreuungsbeitrag und die Fahrkosten zur Kita liefern (zählen mit).
> 5. **Jonas:** Hat er eigene Einkünfte über 18'000 oder Reinvermögen über 250'000? Dann entfiele der Kinderabzug 23.3 (`ar-wl-2025__c0005`, Beachten-Hinweise). Schulgelder und Schulweg sind zusätzlich nicht abziehbar.
> 6. **Vermögen vollständig?** Fehlen Motorfahrzeug (Ziff. 30.4), Bargeld, Gold, Krypto, rückkaufsfähige Lebensversicherung, Schulden oder Schuldzinsen? Bei Schulden braucht es Form. 5 A.
> 7. **Krankheitskosten:** Es liegen keine Belege vor. Der Selbstbehalt von 5 % entspricht rund 5'478 (Kt.) bzw. 5'157 (Bund). Erst darüber gäbe es einen Abzug.
> 8. **Wertschriften-Verwaltungskosten (Ziff. 16.1):** Nicht in den Totals enthalten.
>    - Entweder effektive Depotgebühren laut Steuerauszug oder Pauschale auf Antrag (3 ‰, max. 6'000).
>    - Die Basis ist «Total Steuerwerte» laut WL (`ar-wl-2025__c0087`). Daraus ergeben sich 276 (92'000) oder 114 (nur Depot 38'000), die Basis ist zu klären.
>    - Für den Bund ist die Regel in den AR-Quellen nicht belegt.
> 9. **Annahmen:**
>    - Dividenden stammen aus einer Beteiligung unter 10 % (kein Code BP).
>    - Die Zinsen von 160 liegen je Konto unter 200 (Spalte B).
> 10. **Vorjahresveranlagung 2024** fehlt. Damit liesse sich die Vermögensentwicklung plausibilisieren (92'000 gegenüber Vorjahr).
> 11. **Spendenquittung Krebsliga:** Die Steuerbefreiung der Organisation ist zu bestätigen. Die Quittung beilegen, falls verlangt.
> 
> ## 7. Hinweise für SB/ML
> 
> - **Ziff. 13.2 ist im Wiki ⚠️ strittig.** Die WL ist in sich widersprüchlich: 13.2 oder 16.6 für BVG-Beträge, die nicht im Nettolohn abgezogen sind. Hier ist das irrelevant, weil der Einkauf bereits im Nettolohn steckt. Die Bescheinigung der PK samt Einkaufsberechnung gehört trotzdem in die Beilagen. Danach gilt die 3-Jahres-Sperre für den Kapitalbezug (MB AR 08, `ar-mb-08__c0002`). Die Bundesregeln zum Einkauf sind in den AR-Quellen nicht belegt.
> - **Codes des Hauptformulars** (Seite 3/4) sind laut Wiki nicht am Original verifiziert. Vor der Eingabe am Formular bzw. in der Software prüfen.
> - **Zweiverdienerabzug:** Das Ergebnis ist unempfindlich gegenüber der Frage, ob der Einkauf nochmals von E abgezogen wird. Kt. 5'200 und Bund 14'100 greifen in jedem Fall.
> - Die Bundessteuer rundet das steuerbare Einkommen bei der Veranlagung. Dazu liegt im Wiki keine Fundstelle vor, deshalb habe ich es nicht eingerechnet.

