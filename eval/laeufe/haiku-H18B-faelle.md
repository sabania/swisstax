# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 18:48
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


**Antwort des Agenten** (172.7 s · Tools: 27 Aufrufe steuerwiki__formular, steuerwiki__wert, steuerwiki__position, steuerwiki__zeige, steuerwiki__suche, steuerwiki__rechne):

> Ich lade zuerst das Gerüst der Zürcher Erklärung 2025 und die Werte zu den Belegen.
> 
> Die Eckwerte stehen. Jetzt die Regeln zu den einzelnen Positionen: Berufskosten, Lohnausweis, Versicherung, Drittbetreuung, Einkauf, Vermögen.
> 
> Noch offen: Verpflegung (Feld G, Form. 360 Ziff. 2), Vermögensregeln, Kinderzulagen im Lohn und die Bundesregeln für Verpflegung. Ich hole sie gezielt nach.
> 
> Die Regeln sind geklärt. Jetzt rechne ich alle Summen und Totale mit dem Tool nach.
> 
> Die Variablennamen werden nicht unterstützt. Ich rechne die Totale in einzelnen Ausdrücken ohne Namen nach.
> 
> **ZH · 2025** · Ehepaar, Wohnsitz Winterthur (31.12.), zwei Kinder (4 J. und 9 J.)
> 
> **Ergebnis**
> - Staat: steuerbares Einkommen **66'574**, steuerbares Vermögen **82'000**
> - Bund: steuerbares Einkommen **64'248** (mit Vorbehalt, siehe unten)
> - Verrechnungssteueranspruch **336** (Form. 340, Code 540)
> 
> Alle Werte sind im Wiki als ☑️ agent-geprüft markiert (Fundstelle geprüft, Abnahme offen). Beträge in ganzen Franken, Rechnungen mit `rechne` geprüft.
> 
> ## 1. Einkünfte (Hauptformular)
> 
> | Ziff./Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 1.1 · 100 / 101 | Nettolohn Marco / Sandra | 103'000 / 67'200 | 103'000 / 67'200 | Lohnausweis Ziff. 11. Sandras Nettolohn enthält die Kinderzulagen von 4'800 bereits. Nicht separat in Ziff. 3.4 erfassen. · zh-wl-2025__c0032 ☑️ |
> | 4.1 · 150 | Ertrag Wertschriften/Guthaben | 1'140 | 1'140 | A 960 (Dividenden, VSt-pflichtig) + B 180 (Sparkonto ohne VSt, Zins ≤ 200). · Form. 340 ☑️ |
> | 7 · 199 | Total Einkünfte | 171'340 | 171'340 | 103'000 + 67'200 + 1'140 |
> 
> ## 2. Abzüge
> 
> **Berufsauslagen Marco (Form. 360, Code 220)**
> 
> | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|
> | Ziff. 1.1 ÖV-Abo (Code 201) | 4'180 | 3'300 | Staat: Abo-Kosten unter Plafond 5'200. Bund: Plafond 3'300. · zh-form-360-2025__c0001 ☑️ |
> | Ziff. 2.1 voll, Verpflegung (Code 208) | 3'200 | 3'200* | min(220 × 15 = 3'300; 3'200/Jahr). Mittagessen auswärts, Heimkehr nicht möglich. · zh-form-360-2025__c0003 ☑️ |
> | Ziff. 3 übrige Berufskosten (Code 212) | 3'090 | 3'090 | 3 % × 103'000, im Rahmen 2'000–4'000. · zh-form-360-2025__c0004 ☑️ |
> | **Summe Code 220** | **10'470** | **9'590** | |
> 
> *Bund-Verpflegung nur, wenn die Hauptmahlzeit mehr als CHF 10 kostet (Vorbehalt, siehe Abschnitt 6).
> 
> **Berufsauslagen Sandra (Form. 360, Code 240)**
> 
> | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|
> | Ziff. 1.2 Velo-Pauschale (Code 222) | 700 | 700 | Ständige Velobenützung, Pauschale ohne Beleg. · zh-form-360-2025__c0001 ☑️ |
> | Ziff. 2.1 verbilligt (Code 226) | 1'320 | 1'320 | Feld G angekreuzt (Personalrestaurant). min(176 × 7.50; 1'600). Nicht kumulierbar mit 2.1 voll. · zh-form-360-2025__c0003 ☑️ |
> | Ziff. 3 übrige (Code 232) | 2'016 | 2'016 | 3 % × 67'200. Bund: Teilzeit 80 % (siehe Abschnitt 6). |
> | **Summe Code 240** | **4'036** | **4'036** | |
> 
> **Weitere Abzüge**
> 
> | Ziff./Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 14.1 · 260 / 262 | Säule 3a Marco | 7'258 | 7'258 | Erwerbstätig mit PK: Maximum 7'258. · zh-wl-2025__c0081 ☑️ |
> | 14.2 · 261 / 263 | Säule 3a Sandra | 7'258 | 7'258 | Wie oben. Bescheinigung Form. 21 EDP. |
> | 15 · 270 | Versicherungsprämien und Sparzinsen | 8'400 | 5'100 | A = Krankenkasse 15'840 + Sparzins 180 = 16'020. B Staat: verheiratet 5'800 + 2 × 1'300. B Bund: 3'700 + 2 × 700. Abzug = min(A; B). Keine Prämienverbilligung. · Form. 365 ☑️ |
> | 16.1 · 280 | Einkauf PK Marco | 10'000 | 10'000 | Selbst überwiesen, Lohnausweis Ziff. 10.2 = 0, daher kein Doppelabzug. Abzugsfähig, weil nach Angabe kein Kapitalbezug in 3 Jahren (Sperrfrist). · zh-wl-2025__c0092 ☑️ |
> | 16.3 · 283 | Verwaltung Wertschriften (Depot) | 94 | 0 | Staat: 3 ‰ × 31'200 = 93.60, gerundet 94 (Pauschale, max. 6'000). Bund: nur effektive Kosten belegt, Depotgebühren fehlen. · zh-wl-2025__c0095 ☑️ |
> | 16.6 · 376 | Fremdbetreuung Kinder | 31'900 | 32'700 | Staat: Lena min(27'300; 25'000) = 25'000 + Noah min(6'900; 25'000) = 6'900. Bund: Lena min(27'300; 25'800) = 25'800 + 6'900. Beide unter 14 J., Jahrgang 2011–2025. · zh-stg-2025__par-31-t4 ☑️ |
> | 17 · 290 | Zweiverdienerabzug | 6'100 | 14'100 | Basis Sandra = 67'200 − 4'036 − 7'258 = 55'906. Staat: min(55'906; 6'100). Bund: min(55'906; max(50 % = 27'953; 8'600); 14'100). · zh-wl-2025__c0112 ☑️ |
> | **18 · 299** | **Total Abzüge** | **85'516** | **90'042** | Summe der obigen Zeilen (Staat: 10'470 + 4'036 + 14'516 + 8'400 + 10'000 + 94 + 31'900 + 6'100). |
> 
> ## 3. Nettoeinkommen und Sozialabzüge
> 
> | Ziff./Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 19–21 · 310 | Nettoeinkommen | 85'824 | 81'298 | 171'340 − 85'516 bzw. 171'340 − 90'042 |
> | 22.1 · 320 | Krankheits-/Zahnarztkosten | 0 | 0 | Kosten 3'090 (Zahnarzt 1'850 + Kostenbeteiligung 1'240). Selbstbehalt 5 % = 4'291.20 (Staat) bzw. 4'064.90 (Bund). Unter Selbstbehalt, also kein Abzug. · zh-form-370__c0004 ☑️ |
> | 22.2 · 324 | Gemeinnützige Zuwendungen | 650 | 650 | 400 (Rotes Kreuz) + 250 (UNICEF). Min. 100, max. 20 % (17'164.80 / 16'259.60). · Ziff. 22.2 🟡 (Formular, Chunk nicht einzeln geöffnet) |
> | 23 · 350 | Reineinkommen | 85'174 | 80'648 | Nettoeinkommen − 650 |
> | 24.1 · 370 | Kinderabzug (je Kind) | 18'600 | 13'600 | Staat 2 × 9'300; Bund 2 × 6'800. · zh-stg-2025__par-34 ☑️, bund-dbg-2025__art-35 ☑️ |
> | 24.3 · 365 | Ehepaarabzug (nur Bund) | – | 2'800 | Staat ZH kennt keinen Ehepaarabzug im Einkommen. · Ziff. 24.3 🟡 |
> | **25 / 27 · 390 / 398** | **Steuerbares Einkommen** | **66'574** | **64'248** | 85'174 − 18'600 bzw. 80'648 − 13'600 − 2'800 |
> 
> ## 4. Vermögen (Form. 340 und Hauptformular)
> 
> | Ziff./Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 30.1 · 400 | Wertschriften und Guthaben | 82'000 | – | Sparkonto 42'500 + Privatkonto 8'300 + Depot 31'200 (Steuerwert). Bund hat keine Vermögenssteuer. · Form. 340 Total 400 ☑️ |
> | 33 · 460 / 34 · 470 | Total Vermögenswerte / Schulden | 82'000 / 0 | – | Keine Schulden. |
> | 35 / 37 · 490 / 498 | Steuerbares Vermögen | 82'000 | – | Kein Vermögens-Sozialabzug in ZH (Kinderabzug nur beim Einkommen). · zh-stg-2025 ☑️ |
> | Form. 340 · 540 | Verrechnungssteueranspruch | 336 | – | 35 % × 960 (Kolonne A). Entspricht dem VSt-Abzug laut Bankauszug. Rückerstattung im Formular beantragen, IBAN nötig. · Form. 340 ☑️ |
> 
> Form. 340 Ziffern: Konto Sparkonto (180 Zins) → Kolonne B, Depot (Dividenden 960) → Kolonne A.
> 
> ## 5. Nicht zu deklarieren
> 
> - **Säule-3a-Guthaben und PK-Guthaben (Vorsorgekapital):** bis zur Fälligkeit steuerfrei, nicht im Wertschriftenverzeichnis aufführen. Nur die Einzahlungen gehen in Ziff. 14 bzw. 16.1 ein. · zh-wl-2025__c0154 ☑️
> - **Krankheitskosten 3'090:** kein Abzug, weil unter dem Selbstbehalt. Form. 370 und Krankenkassen-Abrechnung deshalb nicht beilegen (nur bei Abzug nötig). · zh-wl-2025__c0118 ☑️
> - **Hausrat- und Privathaftpflicht 465:** keine Position. Ziff. 15 umfasst nur Krankenkasse, Unfall, Leben/Rente und Sparzinsen. Die Grenze ist ohnehin erreicht.
> - **Swisscom-Handyrechnungen 1'080:** privat, keine Formularposition, nicht abziehbar. Eine Fundstelle habe ich nicht geprüft.
> - **Miete (Mieter):** keine Position, kein Eigenmietwert.
> - **Kinderzulagen 4'800 (Sandra):** bereits im Nettolohn enthalten, nicht zusätzlich in Ziff. 3.4 deklarieren.
> - **Prämienverbilligung:** keine vorhanden, daher nichts zu verrechnen.
> 
> ## 6. Offene Punkte und Vorbehalte
> 
> 1. **Bund Verpflegung Marco (3'200):** nur, wenn die Hauptmahlzeit mehr als CHF 10 kostet. Ohne diesen Nachweis wird Bund-Abzug 0 und das steuerbare Einkommen Bund steigt auf **67'448**. Bitte Kosten des Restaurant-Mittagessens nennen.
> 2. **Bund Pauschale Sandra (2'016, Teilzeit 80 %):** Laut Wiki ist die Pauschale bei Teilzeit «angemessen zu kürzen». Ein Kürzungssatz ist nicht belegt. Ich habe den ungekürzten Betrag angesetzt, Entscheid bei der Fachperson.
> 3. **Depot-Verwaltung Bund (16.3):** effektive Kosten nur mit Gebührenausweis der Bank abziehbar. Ohne Ausweis 0. Bitte Depotgebühren 2025 nennen.
> 4. **Qualifizierte Beteiligung (Ziff. 4.2):** Falls die Schweizer Aktien mindestens 10 % einer Gesellschaft ausmachen, gilt eine andere Teilbesteuerung. Nicht angenommen. Bitte bestätigen.
> 5. **IBAN** für die Verrechnungssteuer-Rückerstattung (336).
> 6. **Einkauf Marco (10'000):** nur gültig, wenn in den nächsten drei Jahren kein Kapitalbezug erfolgt.
> 
> **Plausibilität:** Bund-Einkommen 64'248 liegt unter dem Staat-Einkommen 66'574. Das ist plausibel wegen tieferen Kinder- und Versicherungsabzügen beim Bund und dem Bund-Ehepaarabzug. Die Vermögensbasis und Verrechnungssteuer gehen nur in den Kanton.
> 
> Ich habe keine Werte geschätzt. Für Ziff. 22.2 und 24.3 fehlt die direkte Quellenprüfung (als 🟡 markiert).

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


**Antwort des Agenten** (143.3 s · Tools: 18 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__rechne):

> ## SG · Steuerjahr 2025 · Ausfüllhilfe Nadine (alleinerziehend, Toggenburg)
> 
> Das Formular hat **eine Kantonsspalte**. Die Bundesbeträge stehen nur zur Kontrolle, die Steuerbehörde nimmt die Bundesabweichungen selbst vor (sg-wl-2025__c0173). Alle Positionen sind agent-geprüft (☑️), die Abnahme steht noch aus.
> 
> ### 1. Einkünfte
> 
> | Ziff. | Code | Position | Kanton | Bund (Kontrolle) | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 1.1 | 100 | Lohn, Nettolohn | 73'000 | 73'000 | Lohnausweis Ziff. 11, nicht Ziff. 8. Kinderzulage 2'400 ist schon im Lohn, kein eigener Eintrag. |
> | 4.1 | 146 | Sparzinsen (Form. 2, Abschnitt B, ohne VSt) | 68 | 68 | Bruttozins, Bank ohne VSt-Abzug (sg-form-1-2025__c0006) |
> | 6.1 | 154 | Unterhalt für Nadine | 0 | 0 | Kein Ehegattenunterhalt angegeben |
> | 6.1 | 156 | Kinderalimente Elias (Empfängerin) | 9'600 | 9'600 | 12 × 800. Beim Empfänger steuerbar (sg-wl-2025__c0084). |
> | 7 | 168 | Total Einkünfte | **82'668** | **82'668** | 73'000 + 68 + 9'600 |
> 
> ### 2. Abzüge
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 10.1 | 438 | Berufskosten Nadine | **13'600** | **8'690** | Summe der drei Zeilen unten |
> | ↳ 1.3 | 404/406 | Fahrkosten Auto | 8'000 | 3'300 | 32 km × 2 × 220 Tage × 0.70 = 9'856. Kanton auf Max. 8'000 gekürzt, Bund auf 3'300. Feld F nicht angekreuzt, Abzug zulässig (sg-wl-2025__c0075). Begründung siehe Offene Punkte. |
> | ↳ 2.1 | 408 | Mehrkosten auswärtige Verpflegung | 3'200 | 3'200 | Feld G nicht angekreuzt, daher Ziff. 2.1 und nicht 2.2. min(15 × 220 = 3'300; 3'200). Annahme 220 Tage (siehe unten). |
> | ↳ 3.1 | 416 | Übrige Berufskosten, Pauschale ohne Nachweis | 2'400 | 2'190 | Kanton: min(700 + 10 % × 73'000 = 8'000; 2'400). Bund: min(max(3 % × 73'000 = 2'190; 2'000); 4'000). |
> | 13.1 | 208 | Säule 3a | 7'258 | 7'258 | Max. mit 2. Säule (Lohnausweis Ziff. 10.1 = BVG ordentlich). Bescheinigung beilegen. |
> | 13.2 | 218 | Säule 2, Einkauf PK (20.10.2025) | 6'000 | 6'000 | Nicht im Lohn (Ziff. 10.2 = 0). Einkaufsberechnung beilegen. Limite im Wiki nicht gefunden (siehe Offene Punkte). |
> | 14 | 600 | Prämien und Sparzinsen | **4'500** | **2'500** | A = 5'280 + 1'320 + 68 − 1'800 (Prämienverbilligung) = 4'868. Kanton B = 3'400 + 1'100 (Kind) = 4'500 → min = 4'500. Bund B = 1'800 + 700 = 2'500 → min = 2'500. |
> | 16.2 | 258 | Kinderbetreuung Elias (Kita/Tagesstruktur) | 8'760 | 8'760 | 9'840 − 1'080 Mahlzeiten = 8'760. Max. 26'700 Kanton / 25'800 Bund (sg-form-1-2025__c0009). Formular 10 nötig. |
> | 16.4 | 223 | Weiterbildung (Excel-Kurs) | 400 | 340 | Kanton: höherer Wert aus 340 und Pauschale 400 ohne Nachweis = 400. Bund: nur effektive Kosten = 340 (sg-wl-2025__c0094). |
> | 18 | 230 | Total Abzüge | **40'518** | **33'548** | |
> 
> ### 3. Nettoeinkommen bis steuerbares Einkommen
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 20 | 234 | Nettoeinkommen | **42'150** | **49'120** | 7 − 18 |
> | 21.1 | 650 / 238 / 240 | Krankheits- und Zahnarztkosten | **2'757** | **1'144** | Vorkolonne 850 (Kostenbeteiligung) + 2'750 (Zahnarzt, nicht übernommen) = 3'600. Kanton: 3'600 − 2 % × 42'150 (843) = 2'757. Bund: 3'600 − 5 % × 49'120 (2'456) = 1'144. Leistungsabrechnung beilegen (sg-wl-2025__c0098). |
> | 21.3 | 244 | Spende Caritas | 0 | 0 | 80 liegt unter dem Minimum von 100 (sg-wl-2025__c0102). Nicht abziehbar. |
> | 22 | 248 | Reineinkommen | **39'393** | **47'976** | 20 − 21 |
> | 23.2 | 254 | Kinderabzug Elias | **10'800** | 6'800 | Kindergarten zählt zur Schulpflicht, daher 23.2 und nicht 23.1 (sg-wl-2025__c0104). Bund einheitlich 6'800. |
> | 24 | 268 | Steuerbares Einkommen | **28'593** | **41'176** | 22 − 23 |
> 
> Bund-only, ohne Formularfeld: Abzug vom Steuerbetrag 263 pro Kind, macht die Steuerbehörde.
> 
> ### 4. Vermögen
> 
> | Ziff. | Code | Position | Betrag | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 30.1 | 300 | Sparkonto Raiffeisen | 31'500 | Stand 31.12.2025 (Form. 2, Abschnitt B) |
> | 30.4 | 306 | Motorfahrzeug | ⬜ offen | Steuerwert des Autos fehlt. Ändert nichts, solange er unter 63'500 liegt (siehe unten). |
> | 33 | 322 | Total Vermögenswerte | 31'500 | zuzüglich Fahrzeug |
> | 34 | 504 / 506 | Schulden | 0 | keine angegeben |
> | 35 | 326 | Reinvermögen | 31'500 | 33 − 34 |
> | 36.1 | 330 | Sozialabzug alleinstehend | 75'000 | sg-stg-2025__art-64 |
> | 36.1–36.3 | Kind | Sozialabzug pro minderjähriges Kind | 20'000 | Elias, für den Kinderabzug geltend gemacht wird (sg-stg-2025__art-64) |
> | 37 | 338 | Steuerbares Vermögen | **0** | max(0; 31'500 − 75'000 − 20'000) |
> 
> Sozialabzüge stehen voll in ihrer Ziffer, nicht auf das Reinvermögen gekürzt. Das Vorsorgeguthaben (PK, 3a) gehört nicht zum steuerbaren Vermögen (Wiki-Regel).
> 
> ### Nicht zu deklarieren
> 
> - **Handy-Abo 720:** private Lebenshaltung, nicht abziehbar (sg-stg-2025__art-47 lit. f).
> - **Motorfahrzeugsteuer 410:** keine Formularposition. Das Wiki liefert keine Fundstelle für einen eigenen Abzug, also nicht abziehen.
> - **Haftpflicht-/Kaskoversicherung 1'020:** Motorfahrzeug- und Haftpflichtversicherungen sind bei Ziff. 14 ausdrücklich nicht abziehbar (sg-wl-2025__c0088).
> - **Kita-Mahlzeiten 1'080:** Verpflegung ist bei Drittbetreuung nicht abziehbar.
> - **Spende Caritas 80:** unter dem Minimum von 100.
> - **Prämienverbilligung 1'800:** nicht als eigener Abzug, sondern schon in Ziff. 14 Schritt A verrechnet.
> - **Kinderzulage 2'400:** schon im Nettolohn, kein Doppeleintrag.
> - **Vorsorgeguthaben PK/3a:** nicht als Vermögen erfassen.
> 
> ### Offene Punkte
> 
> 1. **Fahrkosten-Begründung (grösstes Risiko):** Der Abzug über den Auto-Kilometersatz hängt am Grund «kein ÖV». Die erste Verbindung um 06:40 reicht für 06:00 nicht. Gilt nur, wenn vor 06:00 kein ÖV fährt. Bitte prüfen, ob es eine frühere Verbindung gibt. Fahrplan beilegen. Ohne diesen Grund entfällt der Abzug.
> 2. **220 Arbeitstage bei Verpflegung:** angenommen, dass an allen Arbeitstagen auswärts gegessen wird und kein Home-Office anfällt. Bei weniger Tagen sinkt der Abzug um 15 pro Tag.
> 3. **Einkauf PK 6'000:** Einkaufsberechnung und Bescheinigung beilegen. Eine Abzugslimite für den Einkauf habe ich im Wiki nicht gefunden. Nicht geprüft.
> 4. **Fahrzeug-Steuerwert** für Ziff. 30.4 fehlt.
> 5. **Belege beilegen:** Kinderalimente (Urteil/Vereinbarung plus Zahlungsnachweise, erstmalige Angabe), Prämienverbilligungsverfügung, Leistungsabrechnung KK, Zahnarztrechnung, Kita-Rechnungen mit Formular 10, Lohnausweis, Säule-3a-Bescheinigung.
> 6. **Alleinerziehende:** Das Wiki nennt keinen eigenen Sozialabzug für Alleinerziehende in SG. Erfasst ist nur der Kinderabzug. Ein Zusatzabzug wäre nicht belegt.
> 
> Zwei Zahlen nicht aus dem Wiki: Die Kanton-Pauschale von 400 bei der Weiterbildung und die Berechnung der Krankheitskosten folgen der Wiki-Regel, sind aber nur so gut wie die Fundstelle.

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


**Antwort des Agenten** (151.8 s · Tools: 32 Aufrufe steuerwiki__formular, steuerwiki__wert, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne):

> Ich starte mit der vollständigen Formularstruktur für TG 2025 und den Eckwerten, die der Fall braucht.
> 
> Die Formularstruktur und die Eckwerte für Eigenmietwert, Versicherung, Spenden und Vermögen sind da. Jetzt die Positionen mit Rechenregeln und Belegfragen.
> 
> Die Kernpositionen sind geklärt. Offen sind noch Hausrat-, Serafe- und Gebäudeversicherungs-Behandlung, der Wintergarten-Anbau sowie das Versicherungs-Hilfsblatt.
> 
> Die Abgrenzung von Gebäudeversicherung und Hausrat stammt aus der Wegleitung. Ich prüfe die Volltexte, bevor ich rechne.
> 
> Die Wegleitung bestätigt: Sachversicherungen für die Liegenschaft sind abziehbar, Hausrat und Privathaftpflicht nicht. Jetzt rechne ich die ganze Kette exakt durch.
> 
> Das Tool nimmt keine Variablen, deshalb rechne ich die Zwischenstände numerisch nach.
> 
> TG · 2025 · Verwitwete Rentnerin, alleinstehend, Frauenfeld (Wohnsitz 31.12. TG)
> 
> Alle Beträge in ganzen Franken, wo das Formular es verlangt. Rundung: 4'632.50 → 4'633. Die Werte stammen aus dem Wiki (Status ☑️ agent-geprüft, Abnahme offen).
> 
> ## 1. Einkünfte (Formular 1, Seite 2)
> 
> | Ziffer | Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 3.1 | 130 | AHV-Altersrente | 27'000 | 27'000 | 12 × 2'250, zu 100 % steuerbar · tg-form-01-2025__c0007, tg-wl-2025__c0076 |
> | 3.2 | 132 | PK-Rente (2. Säule) | 10'800 | 10'800 | 12 × 900 zu 100 %. Rentenbeginn 2020, daher keine 80 %-Übergangsregel · tg-wl-2025__c0077 |
> | 4 | 150 | Wertschriften- und Zinserträge (Form. 2) | 2'160 | 2'350 | Siehe Hilfsblatt Form. 2 unten |
> | 8.1 | 180 | Liegenschaften, Nettoerfolg (Form. 7/8) | 4'840 | 8'920 | Siehe Hilfsblatt Liegenschaften unten |
> | 6 | 175 | Zwischentotal Einkünfte | 39'960 | 40'150 | 27'000 + 10'800 + Ziff. 4 |
> | 9 | 198 | Total Einkünfte | **44'800** | **49'070** | Ziff. 6 + Ziff. 8.1 |
> 
> Nicht ankreuzen: EL-Bezug (Seite 1), keine Ergänzungsleistungen angegeben.
> 
> ## 2. Abzüge
> 
> | Ziffer | Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 11 | 290 | Schuldzinsen (Form. 4.1) | 3'150 | 3'150 | Hypothekarzinsen 2025, Schuld 180'000 per 31.12. Grenze «Vermögenserträge + 50'000» eingehalten · tg-wl-2025__c0173 |
> | 14 | 330 | Versicherungsprämien und Sparzinsen (Form. 5.2) | 3'500 | 2'700 | Staat: min(A 6'490; 3'500). Bund: min(A 6'490; 2'700), Ansatz ohne Säule 2/3a, da keine Beiträge mehr · tg-stg__par-34-t3, bund-dbg-2025__art-33-t5 |
> | 19 | 360 | Total Abzüge | **6'650** | **5'850** | |
> 
> Form. 5.2, Teil A (A5 = Code 324): KK-Prämie netto 6'240 (keine Prämienverbilligung) + Sparzinsen 250 (Bruttozins Konto) = 6'490.
> 
> ## 3. Einkommensberechnung
> 
> | Ziffer | Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 21 | | Total Abzüge (Übertrag Ziff. 19) | 6'650 | 5'850 | |
> | 22 | 362 | Nettoeinkommen | **38'150** | **43'220** | 44'800 − 6'650 bzw. 49'070 − 5'850 |
> | 23.1 | 364 | Krankheits-/Unfallkosten (Form. 5.1 D) | 4'633 | 4'379 | (A 6'840 − B 300) − 5 % × Ziff. 22: Staat 6'540 − 1'907.50; Bund 6'540 − 2'161 · tg-form-05-1-2025__c0004 |
> | 23.2 | 366 | Freiwillige Zuwendungen (Form. 6) | 350 | 550 | Staat: 550 − 200 (Selbstbehalt), Max. 8'000 (Netto ≤ 40'000) · Bund: 550 (ab 100, Max. 20 % = 8'644) · tg-form-06-2025__c0002 |
> | 24 | 372 | Reineinkommen | **33'167** | **38'291** | 38'150 − 4'633 − 350 bzw. 43'220 − 4'379 − 550 |
> | 25.3 | 388 | Abzug AHV-Rentner/verwitwet (nur Staat) | 1'000 | – | max(0; 4'200 − 200 × 16) bei 33'167 · tg-form-01-2025__c0013, tg-wl-2025__c0116 |
> | 26 | 398 | Steuerbares Einkommen | **32'167** | **38'291** | Ziff. 24 − Ziff. 25.3 |
> 
> Keine Abzüge: 10 (keine Erwerbstätigkeit), 13 (keine Säule 3a), 15.x, 25.1/25.2/25.4 (keine Kinder, keine Unterstützten), 28.x.
> 
> Hinweis zu 25.3: Die Wegleitung-Tabelle enthält eine offensichtlich falsche Zeile («36'900–37'689»). Bei 33'167 ist sie nicht betroffen. Trotzdem gegen WL S. 25 prüfen.
> 
> ## 4. Hilfsblatt Form. 2 (Wertschriftenverzeichnis)
> 
> | Konto/Titel | Steuerwert 31.12. (Sp. 7) | Bruttoertrag mit VSt (Sp. 8) | VSt 35 % |
> |---|---|---|---|
> | Sparkonto TKB | 48'000 | 250 (Zins über 200, daher Sp. 8) | 87.50 |
> | Depot Schweizer Aktien | 95'000 | 2'100 (CH-Dividenden) | 735.00 |
> | **Total** | 143'000 | **2'350** | **822.50** |
> 
> - Ziff. 10 (Verrechnungssteueranspruch): 35 % × 2'350 = 822.50 → Rückerstattungsantrag. Voraussetzung ist der Wohnsitz TG am 31.12.2025, erfüllt · tg-form-02-2025__c0006
> - Vermögensverwaltungskosten (Code 148), nur Staat: min(2 ‰ × 95'000 = 190; 6'000) = **190** → Ziff. 4 Staat 2'350 − 190 = 2'160 · tg-form-02-2025__c0006 (☑️)
> - Bund: Pauschale nicht belegt. Nur effektive Depotgebühren, die die Bank bescheinigt. Ohne Ausweis 0. Bundesspalte Ziff. 4 = 2'350.
> 
> ## 5. Hilfsblatt Form. 7/8 (Liegenschaft Frauenfeld, Baujahr 1986)
> 
> **Eigenmietwert (Form. 7):**
> 
> | | Staat | Bund |
> |---|---|---|
> | Mietwert selbstgenutzt 2025 (indexiert) | 20'400 | 20'400 |
> | Selbstnutzungsabzug | −40 % = −8'160 | −20 % = −4'080 |
> | Steuerbarer Eigenmietwert | 12'240 | 16'320 |
> 
> Unterhalt, effektiv (Form. 8) gegen Pauschale (Gebäude > 10 Jahre = 20 %, auf den steuerbaren EMW):
> 
> | Rechnung | Betrag | Einordnung |
> |---|---|---|
> | Malerarbeiten, Ersatzanstrich Innen | 6'400 | Unterhalt, abziehbar |
> | Gebäudeversicherungsprämie | 520 | Sachversicherung der Liegenschaft, abziehbar · tg-wl-2025__c0227 |
> | Baumschnitt/Gartenpflege | 480 | Unterhalt/Betriebskosten, abziehbar · tg-wl-2025__c0227 |
> | **Total effektiv** | **7'400** | |
> | Vergleich Pauschale 20 % | Staat 2'448 · Bund 3'264 | Effektiv ist in beiden Ebenen günstiger → effektiv wählen |
> | Wintergarten-Anbau | 31'000 | **nicht abziehbar** (Anbau/Neubau, Spalte Anlagekosten/Mehrwert) · tg-wl-2025__c0233 |
> 
> Nettoerfolg (Ziff. 8.1): Staat 12'240 − 7'400 = **4'840**; Bund 16'320 − 7'400 = **8'920**.
> 
> Hilfsblatt Form. 8, Vollständigkeit: je Rechnung eine Zeile mit Rechnungsteller, Arbeit und Betrag. Rechnungskopien ab 1'000 beilegen, hier also nur für Malerarbeiten (6'400).
> 
> ## 6. Hilfsblatt Form. 5.1 (Krankheitskosten)
> 
> | Zeile | Betrag | Bemerkung |
> |---|---|---|
> | A1 Selbstbehalt/Franchise (KK) | 1'000 | Kostenbeteiligung laut Leistungsabrechnung |
> | A2 Zahnarzt (Krone) | 4'440 | Zahnersatz abziehbar |
> | A Brille (augenärztlich verordnet) | 1'400 | Apparate abziehbar, Verordnung beilegen |
> | **A9 Total** | **6'840** | |
> | B1 Vergütung Zusatzversicherung | 300 | nur der vergütete Teil |
> | **A − B** | **6'540** | |
> 
> Ziff. 23.1 nach Abzug des Selbstbehalts (5 % von Ziff. 22): Staat 4'633, Bund 4'379.
> 
> ## 7. Hilfsblatt Form. 5.2 und Form. 6
> 
> - **Form. 5.2:** A1 KK netto 6'240 (ohne IPV) · A4 Sparzinsen 250 · A5/Code 324 = 6'490 · B4 Staat 3'500 · B4 Bund 2'700 → Code 330 Staat 3'500, Bund 2'700 · tg-form-05-2-2025__c0002
> - **Form. 6 (Spenden):** Krebsliga Thurgau 300 · Pro Senectute Thurgau 250 · Total 550. Name und Sitz eintragen. Belege nur ab 1'000 pro Zuwendung. Ziff. 23.2 → Staat 350, Bund 550.
> 
> ## 8. Vermögen (nur Staat; Bund hat keine Vermögenssteuer)
> 
> | Ziffer | Code | Position | Betrag | Bemerkung |
> |---|---|---|---|---|
> | 30.1 | 410 | Wertschriften und Guthaben | 143'000 | Depot 95'000 + Konto 48'000 per 31.12. |
> | 31 | 430 | Liegenschaft, Steuerwert | 410'000 | Amtlicher Verkehrswert · tg-wl-2025__c0239 |
> | 33 | 464 | Total Vermögenswerte | 553'000 | |
> | 34 | 466 | Schulden (Hypothek) | 180'000 | Privatschulden Code 455 |
> | 35 | 468 | Reinvermögen | 373'000 | 553'000 − 180'000 |
> | 36.2 | 472 | Freibetrag alleinstehend | 100'000 | tg-stg__par-53 |
> | 37 | 498 | Steuerbares Vermögen | **273'000** | 373'000 − 100'000 |
> 
> Pensionskasse-Ansprüche sind nicht Vermögen und nicht zu deklarieren (Rente).
> 
> ## 9. Nicht zu deklarieren
> 
> - **Hausratversicherung (380):** kein Abzug. Die Wegleitung nennt Sachversicherungen für die Liegenschaft, nicht Hausrat oder Privathaftpflicht · tg-wl-2025__c0227
> - **Serafe (335):** kein Abzug. Radio-/TV-Gebühren sind weder Versicherungsprämie noch Unterhalt. Im Wiki nicht ausdrücklich belegt. Nach Formularsystematik nicht abziehbar.
> - **Handyrechnung:** private Alltagskosten, kein Abzug, keine Belege einreichen · Ziff. 15.4 / Belegtyp «Private Alltagsrechnungen: nein»
> - **Wintergarten-Anbau (31'000):** kein Abzug als Unterhalt. Nur über den Steuerwert (Ziff. 31) relevant, siehe Rückfrage 1.
> - **Gebäudeversicherung (520) und Gartenpflege (480):** nicht unter Ziff. 14 oder 15.4, sondern im Hilfsblatt Form. 8 (effektive Kosten).
> - **Verrechnungssteuer:** kein Einkommen und kein Abzug. Nur Rückerstattung über Form. 2 Ziff. 10.
> - **Kein Ansatz:** Ziff. 13 (3a), 15.2 (2. Säule), Ziff. 10 (Berufskosten), 25.1/25.2/25.4, 36.1/36.3, 28.x.
> 
> ## 10. Offene Punkte (vor dem Ausfüllen klären)
> 
> 1. **Wintergarten:** Ist der Anbau am 31.12.2025 fertig und in der Schätzung (Steuerwert 410'000) enthalten? Falls nicht, ist er angemessen dem Steuerwert zuzurechnen. Der Betrag ist mit der Liegenschaftensteuerrechnung abzugleichen, nicht mit den Anlagekosten (WL c0239).
> 2. **Weitere Vermögenswerte:** Bargeld, Lebensversicherungen mit Rückkaufswert, Fahrzeuge (Ziff. 30.2–30.6). Nicht angegeben, nicht geprüft, daher nicht in der Summe.
> 3. **Depot-Verwaltungskosten Bund:** nur mit Gebührenausweis der Bank abziehbar. Die Kantonspauschale 190 gilt nur, wenn das Depot als durch Dritte verwaltet gilt (Bankdepot, nach Wiki ja). Fachperson bestätigen lassen.
> 4. **Hypothekarbestätigung:** Zinssatz und Schuld 31.12. (180'000) von der Hypothekarbank bestätigen lassen. Der Zinssatz ist im Form. 4.1 anzugeben, er ergibt sich hier nur rechnerisch (3'150 / 180'000 ≈ 1.75 %).
> 5. **Prüfung Spendenliste:** Sind Krebsliga Thurgau und Pro Senectute Thurgau auf der Liste geprüfter Institutionen der Steuerverwaltung TG? Die Abzugsfähigkeit hängt davon ab.
> 6. **Krankenkasse:** Prämie 6'240 bestätigen und die Abwesenheit einer Prämienverbilligung 2025 belegen. Ohne KK-Deklaration kann der Versicherungsabzug entfallen.
> 7. **Belege einreichen:** Zahnarztrechnung (Krone, 4'440) als Kopie, da über 1'000. Brillenverordnung (augenärztlich). Leistungsabrechnung KK. Malerrechnung (6'400) als Kopie.
> 8. **Ausgaben ohne Belegpflicht:** die Hausrat- und Serafe-Belege brauchen nicht eingereicht zu werden.
> 
> Die Berechnung folgt der Formularstruktur TG 2025 und den Wiki-Eckwerten mit den Status ☑️ (Fundstelle geprüft, Abnahme offen). Die fachliche Beurteilung und die Abnahme bleiben bei der Fachperson.

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


**Antwort des Agenten** (150.3 s · Tools: 17 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne):

> Ich beginne mit dem Gerüst der Erklärung für AR 2025 und den Einzelpositionen, die dieser Fall braucht.
> 
> Die Grundstruktur steht. Jetzt prüfe ich die Limiten und Abzugsregeln, bei denen es auf die Details ankommt: Versicherungsprämien, Zweiverdiener, Berufskosten, Kinderzulagen und nicht abziehbare Posten.
> 
> Die Kernwerte sind belegt. Jetzt rechne ich alle Summen und Totale exakt nach, getrennt für Kanton und Bund.
> 
> Die Namen lassen sich nicht verketten, daher rechne ich die Totale mit den Zahlen aus.
> 
> # Ausfüllhilfe AR · Steuerjahr 2025
> 
> **Haushalt:** Ehepaar, Herisau AR, Mieter. Person 1 (100 %) und Person 2 (80 %, Arbeitsort St. Gallen) sind beide erwerbstätig, zwei Kinder im Haushalt.
> 
> **Wichtig vorab:** Das AR-Formular hat **keine Bundesspalte**. Die Steuerverwaltung nimmt die Abweichungen für die direkte Bundessteuer automatisch vor (ar-wl-2025__c0179). Die Bund-Beträge unten dienen deshalb als Kontrollwerte, nicht als Eintrag im Formular.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Inhalt | Kanton | Bund (Kontrolle) | Fundstelle |
> |---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb Person 1, **Nettolohn** Lohnausweis Ziff. 11 | 85'300 | 85'300 | ar-wl-2025__c0035 |
> | 1.1 | 102 | Haupterwerb Person 2, Nettolohn | 68'200 | 68'200 | ar-wl-2025__c0035 |
> | 4.1 | 146 | Bankzinsen 160 + Dividenden brutto 1'250 | 1'410 | 1'410 | Formular 4.1 |
> | 7 | 168 | Total Einkünfte | **154'910** | **154'910** | Rechnung |
> 
> Der Bruttolohn (Ziff. 8) wird nicht eingesetzt. Die Kinder- und Ausbildungszulagen von Person 2 sind laut WL steuerbar und bleiben im Nettolohn, daher kein separater Abzug (ar-wl-2025__c0032).
> 
> ## 2. Abzüge
> 
> **Ziff. 10.1 Berufskosten (Hilfsblatt Form. 4, Total Code 438)**
> 
> | Position | Person 1 Kanton | Person 1 Bund | Person 2 Kanton | Person 2 Bund |
> |---|---|---|---|---|
> | Fahrkosten | 0 (Feld F: Werkbus unentgeltlich) | 0 | 1'260 (öV-Abo, Code 450) | 1'260 |
> | Verpflegung | 1'600 (Feld G, Code 410: 220 × 7.50 = 1'650, max. 1'600) | 1'600 | 2'640 (Code 458: 176 × 15) | 2'640 |
> | Übrige Berufskosten | 2'400 (700 + 10 % = 9'230, max. 2'400) | 2'559 (3 % von 85'300) | 2'400 (700 + 10 % = 7'520, max. 2'400) | 2'046 (3 % von 68'200, min. 2'000) |
> | **Total** | **4'000** | **4'159** | **6'300** | **5'946** |
> 
> Totale Ziff. 10.1: **Kanton 10'300 · Bund 10'105** (Fundstellen: ar-wl-2025__c0074, ar-form-04-2025__c0003, ar-stv__art-18, bund-bkv-2025__anhang-1).
> 
> **Weitere Abzüge**
> 
> | Ziff. | Code | Inhalt | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 13.1 | n. verif. | Säule 3a: P1 7'258, P2 5'000 | 12'258 | 12'258 | Max. 7'258 mit 2. Säule nicht überschritten |
> | 13.2 | — | BVG-Einkauf P2 | **0** | **0** | Die 4'000 sind bereits in Lohnausweis Ziff. 10.2 abgezogen (im Nettolohn). Nicht doppelt eintragen. |
> | 14 | 600 | Versicherungsprämien Ehepaar + Kinder | **7'400** | **5'100** | Kanton 5'400 + 2 × 1'000; Bund 3'700 + 2 × 700 (ar-stg__art-35-t2, bund-dbg-2025__art-33-t2). Die tatsächlichen Prämien von 13'900 übersteigen den Abzug, daher gilt der Höchstbetrag. |
> | 16.2 | n. verif. | Kinderbetreuung Lea | **10'200** | **10'200** | 14'400 − Mittagessen 1'800 − Betreuungsbeitrag 2'400 = 10'200; unter 25'000 bzw. 25'800 (ar-form-10-2025__c0001) |
> | 17 | n. verif. | Zweiverdienerabzug | **5'200** | **14'100** | Kanton: 10 % von P2 (68'200 − 6'300) = 6'190, max. 5'200. Bund: 50 % von P2 (68'200 − 5'946), max. 14'100 (ar-stg__art-35-t3, bund-dbg-2025__art-33-t6) |
> | 18 | — | Total Abzüge | **45'358** | **51'763** | Σ |
> | 20 | — | **Nettoeinkommen** | **109'552** | **103'147** | 154'910 − Abzüge |
> | 21.3 | 550 | Spende Krebsliga Ostschweiz | 300 | 300 | Min. 100, max. 20 % (ar-stg__art-36) |
> | 22 | — | **Reineinkommen** | **109'252** | **102'847** | 109'552 − 300 |
> 
> ## 3. Sozialabzüge und steuerbares Einkommen
> 
> | Ziff. | Inhalt | Kanton | Bund | Begründung |
> |---|---|---|---|---|
> | 23.2 | Lea (Jahrgang 2021), 4. bis 15. Altersjahr | 7'400 | 6'800 | Vollendung des 4. Altersjahres am 14.03.2025 (ar-stg-anhang-kp__c0001) |
> | 23.3 | Jonas (Jahrgang 2009), ab 15 bis Volljährigkeit | 11'600 | 6'800 | Bund: einheitlich 6'800 pro Kind (bund-dbg-2025__art-35) |
> | 24 | Ehepaar | — | 2'800 | Kanton kein Abzug |
> | 24 | **Steuerbares Einkommen** | **90'252** | **86'447** | 109'252 − 19'000 bzw. 102'847 − 16'400 |
> 
> Bund-Steuerermässigung je Kind (263 Fr., bund-dbg-2025__art-36-t4) wird von der Steuerverwaltung berechnet, nicht im Formular eingetragen.
> 
> ## 4. Vermögen (Form. 2, Kanton)
> 
> | Ziff. | Code | Inhalt | Betrag |
> |---|---|---|---|
> | 30.1 | 300 | Bankkonten 54'000 + Schweizer Aktien (Steuerwert) 38'000 | 92'000 |
> | 33 | 322 | Total Vermögenswerte | 92'000 |
> | 35 | 326 | Reinvermögen (keine Schulden) | 92'000 |
> | 36.2 | 332 | Sozialabzug Ehepaar (Ziff. Freibetrag 150'000) | 150'000 |
> | 36.3 | 334 | Sozialabzug 2 minderjährige Kinder à 25'000 (Lea und Jonas) | 50'000 |
> | 37 | 338 | **Steuerbares Vermögen** | **0** (92'000 − 200'000 < 0) |
> 
> Verrechnungssteueranspruch: 35 % von 1'250 = **437.50**. Im Wertschriftenverzeichnis ausweisen, nicht als Einkommen oder Abzug.
> 
> Die Vorsorgeguthaben (3a und Pensionskasse) gehören nicht zum steuerbaren Vermögen.
> 
> ## 5. Nicht deklarieren oder nicht abziehbar
> 
> - **Handy-Abo 960:** private Lebenshaltung, kein Abzug.
> - **Steuerschlussrechnung 2024 (9'870):** Steuern sind im Formular nicht abziehbar, und es gibt keine Ziffer dafür. Eine Fundstelle habe ich nicht gefunden.
> - **Turnverein-Mitgliederbeitrag 120:** Abzug nur für Zuwendungen an steuerbefreite Organisationen (Ziff. 21.3) oder Parteien (Ziff. 16.3). Ein Mitgliederbeitrag fällt nicht darunter.
> - **Mittagessen Kita 1'800:** Verpflegung ist nicht abziehbar (ar-wl-2025__c0091).
> - **Einkauf PK 4'000 von Person 2:** bereits im Nettolohn, nicht in Ziff. 13.2 nochmals.
> - **Bruttolohn (Ziff. 8)** und **Kinderzulagen** als separater Posten: nicht einsetzen.
> - **Vorsorgeguthaben** (3a, PK): nicht im Vermögen.
> 
> ## 6. Annahmen und offene Punkte
> 
> 1. **Person 2, Verpflegung 2'640:** Setzt voraus, dass die Heimkehr zum Mittag unzumutbar ist. Wenn sie zumutbar ist, entfällt der Abzug: Kanton steuerbares Einkommen 92'892, Bund 89'087.
> 2. **Person 1, Kantine (Feld G):** Ich habe den halben Abzug von 1'600 angesetzt. Entfällt er, wenn die Kantine keine Mehrkosten gegenüber Zuhause verursacht.
> 3. **Lea:** Der Kanton-Kinderabzug ist 7'400 (nicht 5'300), weil sie ihr 4. Altersjahr am 14.03.2025 vollendet hat.
> 4. **Bankkonten 54'000:** Falls darin 3a-Vorsorgekonten sind, gehören sie nicht ins Vermögen. Bitte prüfen.
> 5. **Schweizer Aktien:** Ob es sich um ausserrhodische Beteiligungen handelt (Ziff. 36.5), habe ich nicht geprüft.
> 6. **Krebsliga Ostschweiz:** Bitte bestätigen, dass sie steuerbefreit ist (Voraussetzung für Ziff. 21.3).
> 7. **Codes:** Für Ziff. 13.1, 16.2, 17, 23 und 36 habe ich keinen verifizierten Code. Der Code ist deshalb am Originalformular zu prüfen (Seite 3 ist in der Wegleitung nicht abgebildet).
> 
> **Fazit:** Kanton steuerbares Einkommen **90'252**, steuerbares Vermögen **0**. Bund steuerbares Einkommen **86'447** (Kontrollwert, Steuerverwaltung nimmt die Anpassung vor).

