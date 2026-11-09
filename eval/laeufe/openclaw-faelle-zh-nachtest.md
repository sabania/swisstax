# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuermem` · Fragen: 1 · Lauf: 2026-11-09 09:45
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


**Antwort des Agenten** (214.8 s · Tools: 23 Aufrufe read, ls, exec, message):

> Ausfüllhilfe Steuererklärung 2025, Kanton ZH, Ehepaar Marco und Sandra (Winterthur). Rechenwege und Fundstellen sind unten aufgeführt. Alle Positionen sind ☑️ agent-geprüft, die fachliche Abnahme steht aus. Offen sind sieben Punkte, die ich unten aufliste.
> 
> Formular: Steuererklärung 2025 ZH (Form. 300) mit den Hilfsblättern 360, 365 und 340. Staat und Bund sind getrennt gerechnet. Chunk-IDs stehen als `WL` (Wegleitung ZH 2025), `F300`, `StG` und `DBG`.
> 
> ## 1. Einkünfte (Staat = Bund)
> 
> | Ziff. | Code | Position | Betrag | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|
> | 1.1 | 100 | Marco, Haupterwerb | 103'000 | Lohnausweis Ziff. 11. Kontrolle: 118'400 − 8'110 − 7'290 − 0 = 103'000 ✓ | F300 c0004 |
> | 1.1 | 101 | Sandra, Haupterwerb | 67'200 | Lohnausweis Ziff. 11. Kontrolle: 76'800 − 5'260 − 4'340 = 67'200 ✓ | F300 c0004 |
> | 4.1 | 150 | Ertrag Wertschriften und Guthaben | 1'140 | Form. 340: Kol. A 960 (Dividenden mit VSt) + Kol. B 180 (Sparzins ohne VSt). Das Privatkonto hat 0 Zins. VSt-Anspruch (Code 540) = 35 % × 960 = **336** | F300 c0006, WL |
> | 7 / 19 | 199 | **Total Einkünfte** | **171'340** | | |
> 
> Kinderzulagen (4'800) stecken bereits im Lohn von Sandra. Sie kommen nicht nochmals in Ziff. 3.4.
> 
> ## 2. Abzüge
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 11.1 | 220 | Berufsauslagen Marco (Form. 360) | **10'470** | **9'590** | Siehe Detail unten | WL c0060–c0069 |
> | 11.2 | 240 | Berufsauslagen Sandra (Form. 360) | **4'036** | **4'036** | Siehe Detail unten | WL c0060–c0069 |
> | 14.1 | 260 / eff. 262 | Säule 3a Marco | 7'258 | 7'258 | Maximum mit 2. Säule | WL c0081 |
> | 14.2 | 261 / eff. 263 | Säule 3a Sandra | 7'258 | 7'258 | Maximum mit 2. Säule | WL c0081 |
> | 15 | 270 | Versicherungsprämien und Sparzinsen | **8'400** | **5'100** | A = 15'840 + 180 = 16'020. B Staat = 5'800 + 2×1'300; B Bund = 3'700 + 2×700. Der niedrigere Betrag gilt. | WL c0084–c0086, StG § 31 |
> | 16.1 | 280 | PK-Einkauf Marco | 10'000 | 10'000 | Lohnausweis Ziff. 10.2 = 0, also kein Doppelabzug | F300 c0008 |
> | 16.3 | 283 | Vermögensverwaltungskosten | 94 | 94 | Pauschale 3 ‰ × 31'200 = 93.60 (offener Punkt 6) | WL c0095 |
> | 16.6 | 376 | Drittbetreuung Kinder | **31'900** | **32'700** | Lena: Staat min(27'300; 25'000), Bund min(27'300; 25'800). Noah: 6'900 bei beiden (offener Punkt 3). | WL c0106–c0108, StG § 31, DBG Art. 33 |
> | 17 | 290 | Zweiverdienerabzug | **6'100** | **14'100** | Basis Sandra = 67'200 − 4'036 − 7'258 = 55'906 (tieferes Einkommen; Marco 75'272). Staat fix 6'100. Bund 50 % = 27'953, begrenzt auf 14'100. | WL c0111–c0113 |
> | 18 | 299 | **Total Abzüge** | **85'516** | **90'136** | | |
> 
> **Detail Berufsauslagen Marco (Code 220)**
> 
> - **Fahrkosten (201):** ÖV-Abo 4'180. Das Lohnausweis-Feld F ist nicht angekreuzt, also ist der Abzug zulässig.
>   - Staat: 4'180 (Maximum 5'200).
>   - Bund: begrenzt auf **3'300**.
> - **Verpflegung (208), Mittagessen im Restaurant:** 220 Tage × 15 = 3'300, begrenzt auf **3'200**. Das gilt für Staat und Bund. Feld G ist nicht angekreuzt.
> - **Übrige Berufskosten (212):** 3 % × 103'000 = **3'090**. Die Grenzen 2'000 und 4'000 greifen nicht.
> - **Summe:** Staat 4'180 + 3'200 + 3'090 = 10'470. Bund 3'300 + 3'200 + 3'090 = 9'590.
> 
> **Detail Berufsauslagen Sandra (Code 240)**
> 
> - **Velo (222):** Pauschale 700.
> - **Verpflegung (206, verbilligt wegen Feld G):** 176 × 7.50 = **1'320** (Maximum 1'600). Dieser Betrag beruht auf einer Annahme, siehe offener Punkt 1.
> - **Übrige Berufskosten (212):** 3 % × 67'200 = **2'016**.
> - **Summe:** 700 + 1'320 + 2'016 = 4'036.
> 
> Fundstellen Berufskosten: Fahrkostenmaximum WL c0065 (Staat 5'200, Bund 3'300). Verpflegung WL c0066. Pauschale 3 % WL c0067/c0068. Velo-Pauschale `zh-pauschalierung-berufsauslagen-2025__c0001`. Verpflegung `…__c0004`.
> 
> ## 3. Einkommensberechnung
> 
> | Ziff. | Code | Position | Staat | Bund |
> |---|---|---|---|---|
> | 21 | 310 | Nettoeinkommen (171'340 − Abzüge) | **85'824** | **81'204** |
> | 22.1 | 320 | Krankheitskosten | **0** | **0** |
> | 22.2 | 324 | Gemeinnützige Zuwendungen | **650** | **650** |
> | 23 | 350 | Reineinkommen | **85'174** | **80'554** |
> | 24.1 | 370 | Kinderabzug 2 × (Staat 9'300 / Bund 6'800) | 18'600 | 13'600 |
> | 24.3 | 365 | Verheiratetenabzug (nur Bund) | — | 2'800 |
> | 25 / 27 | 390 / 398 | **Steuerbares Einkommen** | **66'574** | **64'154** |
> 
> - **Krankheitskosten:** Zahnarzt 1'850 + Franchise und Selbstbehalt 1'240 = 3'090. Der Selbstbehalt beträgt 5 % von Ziff. 21, also 4'291 beim Staat und 4'060 beim Bund. Die Kosten liegen darunter, also gibt es keinen Abzug. Fundstelle: StG § 32, Form. 370 (`zh-form-370__c0004`).
> - **Spenden:** Rotes Kreuz 400 + UNICEF 250 = 650. Das liegt über dem Mindestbetrag von 100 und unter 20 % des Nettoeinkommens. Die Aufstellung ist beizulegen. Fundstelle: WL c0122, `zh-info-spenden__c0003`.
> - **Kinderabzug:** Fundstelle StG § 34, DBG Art. 35. Beide Kinder sind unter 18, also Abzug voll.
> - **Bund, nicht deklarierbar:** Der Abzug vom Steuerbetrag von 263 pro Kind rechnet die Verwaltung selbst (DBG Art. 36).
> 
> ## 4. Vermögen (nur Staat, der Bund hat keine Vermögenssteuer)
> 
> | Ziff. | Code | Position | Betrag |
> |---|---|---|---|
> | 30.1 | 400 | Sparkonto 42'500 + Privatkonto 8'300 + Depot (Steuerwert) 31'200 | **82'000** |
> | 33 / 35 / 37 | 460 / 490 / 498 | Total Vermögen, Schulden 0 | **82'000** |
> 
> Das liegt unter der 0-‰-Stufe für Verheiratete von 159'000 (StG § 47, `zh-stg-2025__par-47-t2`). Es fällt keine Vermögenssteuer an. Das Privatkonto gehört trotz 0 Zins ins Verzeichnis.
> 
> ## 5. Nicht zu deklarieren oder nicht abziehbar
> 
> - **Handyrechnungen Swisscom (1'080):** private Lebenshaltung. Berufliche Anteile sind in der Pauschale «übrige Berufskosten» enthalten.
> - **Hausrat- und Privathaftpflichtversicherung (465):** nicht abziehbar. Sie zählen nicht zum Versicherungsabzug und ändern ihn auch nicht, weil die Prämien ohnehin über dem Maximum liegen.
> - **Miete Winterthur:** Lebenshaltung, kein Abzug.
> - **PK-Guthaben und 3a-Guthaben:** nicht ins Wertschriftenverzeichnis aufnehmen.
> - **Kinderzulagen:** nicht separat erfassen (siehe Abschnitt 1).
> - **Prämien über dem Maximum:** 16'020 gegenüber 8'400 beim Staat und 5'100 beim Bund. Der Rest verfällt.
> - **Betreuungskosten Lena über dem Maximum:** 2'300 beim Staat und 1'500 beim Bund. Der Rest verfällt.
> - **Bei der Steuererklärung leer:** Ziff. 3 (Renten und Taggelder), Ziff. 6 (Liegenschaften), Ziff. 12 (Schuldzinsen), Ziff. 16.2 (Weiterbildung), Ziff. 40 (Kapitalleistungen aus Vorsorge, keine in den letzten drei Jahren), Ziff. 50.
> 
> ## 6. Offene Punkte und Rückfragen an die Mandanten
> 
> 1. **Sandra, Verpflegung 1'320:** Ich habe den Standardfall deklariert (Feld G angekreuzt, halber Satz). Der Abzug steht aber nur zu, wenn die Mittagspause die Heimkehr nicht erlaubt (WL c0066). Wohn- und Arbeitsort sind beide Winterthur. Frage: Reicht die Pause für den Heimweg? Wenn ja, entfällt der Abzug. Dann steigt das steuerbare Einkommen um 1'320 in Staat und Bund.
> 2. **Marco, Verpflegung:** Die 3'200 sind bei 214 Arbeitstagen ausgeschöpft. Bitte bestätigen lassen, dass er an mindestens 214 Tagen auswärts isst und nicht im Homeoffice war.
> 3. **Hortrechnung Noah (6'900):** Ist ein Mittagstisch oder Verpflegungsanteil enthalten? Verpflegung ist nicht abziehbar (`beleg-kinderbetreuung-rechnungen`). Bitte Rechnung prüfen und den Anteil herausrechnen. Fragen, ob Betreuungsgutscheine oder Subventionen erhalten wurden.
> 4. **Krankheitskosten:** Es fehlen noch rund 1'200 (Staat) bzw. 970 (Bund) bis zum Selbstbehalt. Zusätzliche Kosten (Brille, Medikamente, Therapien, Zahnspange) abfragen und in Form. 370 sammeln.
> 5. **PK-Einkauf 10'000:** Bescheinigung (Form. 21 EDP) beilegen. Bei einem Kapitalbezug innert drei Jahren, zum Beispiel für Wohneigentum, wird der Abzug aufgerückt (Wegleitung zu Ziff. 16.1).
> 6. **Vermögensverwaltung (94):** Die Pauschale gilt nur für durch Dritte verwaltete Wertschriften. Ob der Bund eine eigene Pauschale hat, ist im Wiki nicht belegt (ZStB 30.1 fehlt im Wiki). Betrag ist gering. Besser den Depotgebührenausweis der ZKB verlangen und die effektiven Kosten prüfen.
> 7. **Fehlende Angaben:**
>    - Gibt es ein Motorfahrzeug? (Ziff. 30.4)
>    - Gibt es Kinderkonten, Bargeld, rückkaufsfähige Lebensversicherungen oder Krypto?
>    - Vorjahresveranlagung zur Plausibilisierung des Vermögens anfordern.
>    - Namen, Geburtsdaten und Schule der Kinder für Seite 1.
> 
> ## Hinweise für SB/ML
> 
> - **Fahrkostenmaximum Bund:** Das Gesetz und die ZH-Wegleitung nennen 3'300. Die ESTV-Wegleitung 2a 2025 S. 6 nennt noch 3'200 (`bund-wl-2a-2025__c0042`). Das Gesetz geht vor, im Wiki als «prüfen» markiert.
> - **Plausibilität Sozialabgaben:** AHV, ALV und NBUV liegen bei beiden Lohnausweisen bei rund 6.85 % des Bruttolohns. Das ist stimmig.
> - **Steuerbetrag:** Ich habe keinen Steuerbetrag berechnet, weil das nicht verlangt war.

