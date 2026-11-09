# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 18:19
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


**Antwort des Agenten** (176.2 s · Tools: 19 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__suche, steuerwiki__rechne):

> Ich lese zuerst das Gerüst der ZH-Erklärung 2025 und die Positionen zu den Belegen.
> 
> Die Hauptpositionen sind geklärt. Offen sind noch Verwaltungskosten (Bundesspalte), Zweiverdienerabzug, Versicherungen/Telefon als Nicht-Abzug und Kinderzulagen im Lohn.
> 
> **ZH · 2025: Ausfüllhilfe Ehepaar Winterthur (Staat | Bund)**
> 
> Kurzfassung:
> - Steuerbares Einkommen: **Staat 66'574 | Bund 64'248**. Steuerbares Vermögen: **Staat 82'000**.
> - **Krankheitskosten: 0.** Auslagen 3'090 liegen unter dem 5-%-Selbstbehalt (Staat 4'291, Bund 4'065). Der Abzug wird nicht erreicht.
> - Zwei Annahmen entscheiden über Beträge (siehe «Offene Punkte»): Heimkehr-Möglichkeit von Sandra in der Mittagspause und Verpflegungskosten von Marco für den Bund.
> 
> ### 1. Formularpositionen (Hauptformular Form. 300)
> 
> | Ziff. · Code | Position | Staat | Bund | Rechenweg · Fundstelle · Status |
> |---|---|---|---|---|
> | 1.1 · 100 / 101 | Nettolohn Marco / Sandra (LA Ziff. 11) | 103'000 / 67'200 | 103'000 / 67'200 | Ziff. 8 − (9 + 10). Sandras Kinderzulagen 4'800 sind im Lohn enthalten und steuerbar (siehe «Nicht deklarieren»). zh-wl-2025__c0032 · ☑️ |
> | 4.1 · 150 | Ertrag Wertschriften/Guthaben | 1'140 | 1'140 | Dividenden 960 (Form. 340 Kol. A) + Sparzins 180 (Kol. B). ☑️ |
> | 4.2 · 151 | Qualifizierte Beteiligungen | 0 | 0 | Annahme: keine Beteiligung ≥ 10 %. Bitte bestätigen. |
> | 7 · 199 | Total Einkünfte | 171'340 | 171'340 | 103'000 + 67'200 + 1'140 |
> | 11.1 · 220 | Berufsauslagen Marco | 10'470 | 9'590 | ÖV-Abo 4'180 (Staat) bzw. 3'300 (Bund-Plafond) + Verpflegung voll min(220 × 15; 3'200) = 3'200 + übrige 3 % von 103'000 = 3'090. Form. 360 Ziff. 1.1 Code 201 bzw. Ziff. 2.1 voll Code 208. zh-form-360-2025__c0002/c0003 · ☑️ |
> | 11.2 · 240 | Berufsauslagen Sandra | 4'036 | 4'036 | Velo-Pauschale 700 (Code 222) + Verpflegung verbilligt 176 × 7.50 = 1'320 (Code 226; Feld G gesetzt) + übrige 3 % von 67'200 = 2'016. ☑️ · Vorbehalt: siehe Offene Punkte 1 |
> | 12 · 250 | Schuldzinsen | 0 | 0 | keine |
> | 14.1 · 260 (eff. 262) | Säule 3a Marco | 7'258 | 7'258 | min(7'258; 7'258) mit 2. Säule. Form. 21 EDP. zh-wl-2025__c0081 · ☑️ |
> | 14.2 · 261 (eff. 263) | Säule 3a Sandra | 7'258 | 7'258 | wie oben |
> | 15 · 270 | Versicherungsprämien + Sparzinsen | 8'400 | 5'100 | Teil A = KK 15'840 (Code 601) + Sparzins 180 (Code 604) = 16'020. Teil B verheiratet mit 2./3a + 2 Kinder: Staat 5'800 + 2 × 1'300 = 8'400; Bund 3'700 + 2 × 700 = 5'100. Ergebnis = min(A; B). zh-form-365-2025__c0001/c0002 · ☑️ |
> | 16.1 · 280 | PK-Einkauf freiwillig (Marco) | 10'000 | 10'000 | Form. 21 EDP; Lohnausweis Ziff. 10.2 = 0, daher kein Doppelabzug. zh-wl-2025__c0092 · ☑️ |
> | 16.3 · 283 | Verwaltung Depot | 94 | 0 | Staat Pauschal min(3 ‰ × 31'200 = 93.60; 6'000) → 94, ganze Franken. Bund nur effektive Kosten mit Gebührenbeleg, sonst 0. zh-wl-2025__c0095 · ☑️ (Bund: offen) |
> | 16.6 · 376 | Fremdbetreuung Kinder | 31'900 | 32'700 | Lena: Kita 27'300 → min(27'300; 25'000) Staat / min(27'300; 25'800) Bund. Noah: Hort 6'900 unverändert. Beide Jahrgänge 2011–2025. zh-form-300-2025__c0008 · ☑️ |
> | 17 · 290 | Zweiverdiener-Abzug | 6'100 | 14'100 | Basis = niedrigeres Erwerbseinkommen nach Abzügen = Sandra 67'200 − 4'036 − 7'258 = 55'906. Staat min(55'906; 6'100). Bund min(55'906; max(50 % = 27'953; 8'600); 14'100). zh-wl-2025__c0112 · ☑️ |
> | 18 · 299 | Total Abzüge | 85'516 | 90'042 | Summe der obigen Positionen |
> | 21 · 310 | Nettoeinkommen | 85'824 | 81'298 | 171'340 − 85'516 bzw. − 90'042 |
> | 22.1 · 320 | Krankheits-/Unfallkosten | 0 | 0 | Form. 370: Selbstbehalt Krankenkasse 1'240 (Code 300) + Zahnarzt 1'850 (Code 302) = Auslagen 313 = 3'090. Schwelle 5 % = 4'291 (Staat) / 4'065 (Bund). Abzug 0. Fehlbetrag bis zur Schwelle: 1'201 bzw. 975. zh-form-370__c0002/c0004 · ☑️ |
> | 22.2 · 324 | Gemeinnützige Zuwendungen | 650 | 650 | Rotes Kreuz 400 + UNICEF 250 = 650. ≥ 100 ✓; Max 20 % von 85'824 = 17'165 ✓. Vorbehalt: Empfänger im ZH-Verzeichnis prüfen. zh-form-300-2025__c0009 · ☑️ |
> | 23 · 350 | Reineinkommen | 85'174 | 80'648 | 21 − 22.1 − 22.2 |
> | 24.1 · 370 / 372 | Kinderabzug (Haushalt) | 18'600 | 13'600 | 2 × 9'300 (Staat) bzw. 2 × 6'800 (Bund). Lena (2021), Noah (2016) minderjährig. zh-wl-2025__c0126 · ☑️ |
> | 24.3 · 365 | Abzug Ehegatten (nur Bund) | – | 2'800 | Staat nicht anwendbar. ☑️ |
> | 25 · 390 | Steuerbares Einkommen | 66'574 | 64'248 | 23 − 24.1 − 24.3 |
> | 30.1 · 400 | Wertschriften und Guthaben | 82'000 | – | 31'200 Depot (Steuerwert) + 42'500 Sparkonto + 8'300 Privatkonto. Form. 340. ☑️ |
> | 33 · 460 | Total Vermögenswerte | 82'000 | – | |
> | 34 · 470 | Schulden | 0 | – | keine (Form. 355 leer) |
> | 35 · 490 | Steuerbares Vermögen | 82'000 | – | Keine Sozialabzüge auf Vermögen. Der Bund erhebt kein Vermögen. |
> | 40 · 510 | Kapitalleistungen Vorsorge | – | – | keine, laut Auftrag |
> 
> ### 2. Hilfsblätter
> 
> - **Form. 360, Marco:** Ziff. 1.1 ÖV-Abo, Code 201, Staat 4'180 / Bund 3'300 (Plafond). Ziff. 2.1 voll, Code 208, 3'200. Ziff. 7 nicht ausfüllen, da kein Auto.
> - **Form. 360, Sandra:** Ziff. 1.2 Velo, Code 222, 700. Ziff. 2.1 verbilligt, Code 226, 1'320 (nur wenn keine Heimkehr möglich, siehe Offene Punkte 1). Lohnausweis Feld G ist angekreuzt, daher verbilligt und nicht voll.
> - **Form. 365:** Teil A: 601 = 15'840, 604 = 180, 606 = 16'020. Teil B: 611 = 5'800 (Bund 3'700), 613 = 2 × 1'300 (Bund 2 × 700), Total B Code 616 = 8'400 (Bund 5'100).
> - **Form. 370:** Teil A Ziff. 1 Code 300 = 1'240; Ziff. 2–3 Code 302 = 1'850; Total 313 = 3'090; Selbstbehalt 319 = 4'291 / 4'065; Abzug 320 = 0. Form. 370 muss nicht eingereicht werden, weil der Abzug 0 ist. Die Belege behalten.
> - **Form. 340:** Kol. A (Code 2309), Dividende 960 mit Verrechnungssteuer 336 → DA-1 (Code 2370) für die Rückforderung. Kol. B (Code 542), Sparzins 180 ohne VSt. Steuerwert Depot 31'200, Konten 42'500 und 8'300, Total Code 400 = 82'000.
> - **Lohnausweise:** beide beilegen (Pflicht, zh-wl-2025__c0032).
> 
> ### 3. Nicht zu deklarieren oder nicht abziehbar
> 
> - **Vorsorgeguthaben** (PK-Konten, Säule 3a bis Fälligkeit): kein steuerbares Vermögen, daher nicht in Ziff. 30 eintragen (zh-wl-2025__c0154).
> - **Hausrat- und Privathaftpflichtversicherung (465 CHF):** nicht abziehbar. Form. 365 Teil A kennt nur Krankenkasse, Unfall, Leben/Rente und Sparzinsen.
> - **Swisscom-Handyrechnungen (1'080 CHF):** Lebenshaltungskosten, kein Abzugsfeld. Der Wiki-Beleg ist ZStB 30.3 und betrifft das Liegenschaftsumfeld. Das Prinzip gilt hier, eine direkte Aussage zu Handyrechnungen fehlt aber.
> - **Kinderzulagen 4'800 (Sandra):** im Lohn enthalten, daher in Ziff. 1.1 steuerbar. Nicht in Ziff. 3.4 eintragen. Ziff. 3.4 gilt nur für Zulagen, die direkt von der Ausgleichskasse ausbezahlt werden (zh-wl-2025__c0055).
> - **Zahnarzt und Selbstbehalt:** Abzug 0 (Schwelle nicht erreicht). Keine Eintragung in Ziff. 22.1 nötig.
> - **Kapitalleistungen, Schuldzinsen, Parteispenden:** keine Belege, daher nicht zu deklarieren.
> 
> ### 4. Offene Punkte (Rückfragen an den Haushalt)
> 
> 1. **Sandra, Mittagspause:** Wohnort und Arbeitsort sind beide Winterthur. Kann sie in der Mittagspause nach Hause? Wenn ja, entfällt die Verpflegung 1'320 (Staat und Bund). Das Einkommen steigt um 1'320, das steuerbare Einkommen auf Staat 67'894 und Bund 65'568. Sandras Velo-Pauschale bleibt. Der Zweiverdiener-Abzug bleibt unverändert (Deckel 6'100 bzw. 14'100).
> 2. **Marco, Bund-Verpflegung:** Der Bund gewährt den Abzug nur, wenn die Hauptmahlzeit mehr als 10 Franken kostet (zh-form-360-2025, Ziff. 2.1 voll). Die Kosten des Restaurants sind nicht belegt. Mit Kosten über 10 Franken bleibt der Abzug von 3'200 bestehen. Bei 10 Franken oder weniger entfällt er, und das Bund-Einkommen steigt um 3'200.
> 3. **Depot:** Gibt es Beteiligungen ≥ 10 %? Dann Teilbesteuerung und Ziff. 4.2 prüfen.
> 4. **Vermögen:** Gibt es weitere Vermögenswerte (andere Bankkonten, Lebensversicherungen mit Rückkaufswert, Fahrzeuge), Schenkungen oder Erbvorbezüge (Ziff. 30, 50)? Diese sind nicht geprüft, weil sie nicht im Couvert liegen.
> 5. **Spendenempfänger:** Rotes Kreuz und UNICEF im ZH-Verzeichnis der steuerbefreiten Institutionen prüfen. Ist eine Institution nicht im Verzeichnis, entfällt der Abzug für sie.
> 6. **Depotgebühren:** Liegen effektive Verwahrungskosten über 94 Franken vor, sind die effektiven Kosten mit Beleg abzugsfähig. Pauschale und effektive Kosten dürfen nicht kombiniert werden.
> 
> ### 5. Quellenhinweise
> 
> - Die Lohnausweis-Regeln stammen aus der ESTV-Wegleitung 2026 (bund-wl-lohnausweis-2026). Im Wiki fehlt die 2025er Fassung. Die Regeln wurden trotzdem angewendet, weil sie qualitativ sind und keine Beträge enthalten.
> - Der Kinder-Drittbetreuungsabzug ist im Formular 2025 mit 25'000 Franken angegeben (zh-stg-2025__par-31-t4). Die VKP ZH 2024 nennt noch 10'400 Franken. Das Formular 2025 gilt.
> - Die Fachperson entscheidet über die Bewertung. Diese Ausfüllhilfe beruht auf dem Wiki-Stand und den gelieferten Belegen.

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


**Antwort des Agenten** (151.5 s · Tools: 22 Aufrufe steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__wert, steuerwiki__rechne, steuerwiki__suche):

> **SG · 2025**: Ausfüllhilfe Nadine (alleinerziehend, Wohnsitz Toggenburg, Mieterin). Haushalt mit Sohn Elias (5, Kindergarten). Alle Positionen sind ☑️ (Fundstelle geprüft, Abnahme offen), sofern nicht anders markiert. Die Tarifberechnung (Steuerbetrag) habe ich nicht gerechnet.
> 
> ## Einkünfte
> 
> | Ziff. | Code | Inhalt | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 1.1 | 100 | Nettolohn (Lohnausweis Ziff. 11) | 73'000 | 73'000 | 83'500 − 5'890 − 4'610 = 73'000. Die Kinderzulage 2'400 steckt im Lohnausweis und gehört hier hinein, nicht in Ziff. 3.5 (sg-wl-2025__c0042). |
> | 4.1 | 146 | Zins Sparkonto | 68 | 68 | Bruttozins ohne VSt. |
> | 6.1 | 156 | Kinderalimente für Elias (erhalten) | 9'600 | 9'600 | 12 × 800. Elias ist minderjährig und in ihrer Obhut (sg-wl-2025__c0068). |
> | 7 | 168 | Total Einkünfte | 82'668 | 82'668 | |
> 
> ## Abzüge
> 
> | Ziff. | Code | Inhalt | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 10.1 | 438 | Berufskosten Nadine (Total Form. 4 Ziff. 6) | 13'600 | 8'690 | Siehe Teilpositionen unten. |
> | Form. 4 Ziff. 1.3 | 404/406 | Fahrkosten Auto | 8'000 | 3'300 | 32 km × 2 × 220 Tage × 0.70 = 9'856, begrenzt auf Kanton 8'000 bzw. Bund 3'300. Begründung ankreuzen, siehe Offen-Punkt 1. |
> | Form. 4 Ziff. 2.1 | 408 | Verpflegung (Restaurant) | 3'200 | 3'200 | 15 × 220 = 3'300, begrenzt auf 3'200. Feld G ist nicht angekreuzt. |
> | Form. 4 Ziff. 3.1 | — | Pauschale übrige Berufskosten | 2'400 | 2'190 | K: 700 + 10% × 73'000 = 8'000, max. 2'400. B: 3% × 73'000 = 2'190 (min. 2'000, max. 4'000). Pauschale gewählt, weil keine höheren tatsächlichen Kosten belegt sind. |
> | 13.1 | 208 | Säule 3a | 7'258 | 7'258 | Maximum mit 2. Säule. Bescheinigung beilegen. |
> | 13.2 | 218 | Einkauf Pensionskasse (20.10.2025) | 6'000 | 6'000 | Bescheinigung und Einkaufsberechnung beilegen. Lohnausweis Ziff. 10.2 ist 0, daher kein Doppelabzug. Im Positionstext ist keine Obergrenze genannt, die habe ich nicht separat geprüft. |
> | 14 | 600 | Prämien und Sparzinsen | 4'500 | 2'500 | A = 6'600 + 68 − 1'800 (IPV) = 4'868. K: min(4'868; 3'400 + 1'100 für Elias) = 4'500. B: min(4'868; 1'800 + 700) = 2'500. Zuschlag ohne 2./3a entfällt, da beides vorhanden ist (sg-wl-2025 Ziff. 14). |
> | 16.2 | 258 | Kinderbetreuung Elias | 8'760 | 8'760 | 9'840 − 1'080 Mahlzeiten = 8'760. Limiten K 26'700, B 25'800. Erwerbstätigkeit 100 % (Kausalzusammenhang erfüllt). |
> | 16.4 | 223 | Weiterbildung (Excel-Kurs) | 340 | 340 | Beruflich bedingt, Limite 13'000. |
> | 18 | 230 | Total Abzüge | 40'458 | 33'548 | |
> 
> Nicht zutreffend bzw. 0: Ziff. 11, 12.1, 12.2 (Nadine bezahlt keine Alimente), 15, 16.1, 16.3, 16.5, 17 (Zweiverdiener, nicht verheiratet).
> 
> ## Nettoeinkommen, Krankheitskosten, Reineinkommen
> 
> | Ziff. | Code | Inhalt | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 20 | 234 | Nettoeinkommen | 42'210 | 49'120 | 82'668 − 40'458 bzw. 82'668 − 33'548 |
> | 21.1 | 650/238/240 | Krankheitskosten | 2'756 | 1'144 | Vorkolonne 850 (Kostenbeteiligung) + 2'750 (Zahnarzt) = 3'600. K: 3'600 − 2% × 42'210 (= 844.20) = 2'755.80, gerundet 2'756. B: 3'600 − 5% × 49'120 (= 2'456) = 1'144. |
> | 21.3 | 244 | Spende Caritas 80 | 0 | 0 | Unter dem Minimum von 100 (sg-stg-2025__art-46). |
> | 22 | 248 | Reineinkommen | 39'454 | 47'976 | 42'210 − 2'756; 49'120 − 1'144. |
> 
> ## Sozialabzüge und steuerbares Einkommen
> 
> | Ziff. | Code | Inhalt | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 23.1 | 252 | Kinderabzug noch nicht schulpflichtig | 0 | 0 | Elias ist schulpflichtig, weil Kindergarten zur Schulpflicht zählt (Positionstext 23.1). Bund-Hinweis: 263 Abzug vom Bundessteuerbetrag pro Kind. |
> | 23.2 | 254 | Kinderabzug Schule/Kindergarten (Elias) | 10'800 | 6'800 | Kanton 10'800 (sozialabzug.kind_schule). Bund einheitlich 6'800 pro Kind (bund-dbg-2025__art-35). |
> | 23.3 | 256 | Ausbildungskosten | 0 | 0 | Nicht zutreffend (kein Ausbildungskind). |
> | 24 | 268 | Steuerbares Einkommen | 28'654 | 41'176 | 39'454.20 − 10'800; 47'976 − 6'800. |
> 
> ## Vermögen
> 
> | Ziff. | Code | Inhalt | Kanton | Bund | Bemerkung |
> |---|---|---|---|---|---|
> | 30.1 | 300 | Sparkonto Raiffeisen | 31'500 | — | Per 31.12.2025. |
> | 30.4 | 306 | Motorfahrzeug | ⬜ | — | Zeitwert fehlt, muss ergänzt werden. |
> | 33 | 322 | Total Vermögenswerte | 31'500 + Fahrzeug | — | |
> | 35 | 326 | Reinvermögen | 31'500 + Fahrzeug | — | Keine Schulden. |
> | 36.1 | 330 | Freibetrag alleinstehend | 75'000 | — | sg-stg-2025__art-64. |
> | 36.2 | — | Freibetrag je minderjähriges Kind unter Obhut | 20'000 | — | Elias. Bund hat keine Vermögenssteuer. |
> | 37 | 338 | Steuerbares Vermögen | 0 | — | 31'500 − 95'000 < 0. Erst bei Fahrzeugwert über 63'500 entsteht steuerbares Vermögen. |
> 
> ## Offene Punkte
> 
> 1. **Fahrkosten-Begründung (grösster Betrag, K 8'000 / B 3'300).** Die erste ÖV-Verbindung fährt um 06:40, der Arbeitsbeginn ist 06:00. Ob das als „kein ÖV“ nach Form. 4 Ziff. 1.3 reicht, ist nicht geklärt. Die Begründung ist nur tragfähig, wenn kein zumutbarer ÖV vor Arbeitsbeginn besteht, oder wenn die Zeitersparnis über 60 Min./Tag liegt. Fahrplan-Nachweise beilegen. Wird die Begründung nicht anerkannt, sind nur die tatsächlichen ÖV-Kosten abziehbar. Es liegen keine Belege dafür vor, also 0.
> 2. **Kinderabzug und Unterhalt.** Für Ziff. 23.2 muss Nadine zur Hauptsache für den Unterhalt aufkommen. Der Ex zahlt 800 pro Monat. Das prüfen. Ein Kind, für das Unterhalt nach Ziff. 12.2 abgezogen wird, erhält keinen Kinderabzug beim Zahlenden.
> 3. **Widerspruch im Formular-Überblick.** Die Zeile Ziff. 24 nennt „kind_schule: Bund kein Abzug“. Der Positionstext 23.2 und bund-dbg-2025__art-35 nennen 6'800. Ich habe 6'800 eingesetzt. Fachlich bestätigen lassen.
> 4. **Motorfahrzeug-Zeitwert** (Ziff. 30.4) fehlt.
> 5. **Krankheitskosten-Belege.** Die Krankenkassen-Leistungsabrechnung und die Zahnarztrechnung auf Verlangen bereithalten.
> 6. **Annahmen:** Mittagessen auswärts (Heimkehr nicht möglich, 32 km), 220 Arbeitstage, Kostenbeteiligung 850 ist der von Nadine selbst getragene Betrag.
> 
> ## Nicht zu deklarieren
> 
> - **Auto-Haftpflicht/Kasko 1'020:** nicht abziehbar (Ziff. 14, Beachten).
> - **Motorfahrzeugsteuer 410:** Privatauto, kein Abzug vorgesehen. Die Position nennt sie nicht ausdrücklich, das habe ich nicht separat geprüft.
> - **Handy-Abo 720:** Lebenshaltung, kein Abzugstatbestand.
> - **Spende 80:** unter dem Minimum von 100.
> - **Kita-Mahlzeiten 1'080:** Verpflegung des Kindes, nicht abziehbar (Ziff. 16.2).
> - **Kinderzulage 2'400:** bereits im Nettolohn (Ziff. 1.1), kein separater Eintrag.
> - **Prämienverbilligung 1'800:** kein Abzug, sondern bereits in Ziff. 14 A.e gekürzt.
> - **Säule-3a- und Pensionskassen-Guthaben:** nicht als Vermögen deklarieren, solange sie nicht fällig sind (sg-wl-2025__c0107).
> 
> Verwendete Belege sind nicht gespeichert, es gibt keine Mandantendaten im Wiki oder in MEMORY.md.

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


**Antwort des Agenten** (141.7 s · Tools: 25 Aufrufe steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne, steuerwiki__wert):

> **TG · Steuerjahr 2025 · Ausfüllhilfe Verwitwete Rentnerin, Frauenfeld**
> 
> Beträge in CHF, ganze Franken. Spalte **Staat** = Staats- und Gemeindesteuer, **Bund** = direkte Bundessteuer. Alle Werte sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Inhalt | Staat | Bund | Rechnung / Fundstelle |
> |---|---|---|---|---|---|
> | 3.1 | 130 | AHV-Altersrente | 27'000 | 27'000 | 12 × 2'250 |
> | 3.2 | 132 | PK-Rente, 100 % | 10'800 | 10'800 | 12 × 900. Rentenbeginn 2020, daher kein Übergangsrecht (80 %). `tg-form-01-2025__c0007`, `tg-wl-2025__c0077` |
> | 4 | 150 | Wertschriften- und Zinsertrag | 2'160 | 2'350 | Bruttoertrag 250 (Zins) + 2'100 (Div.) = 2'350, beide Sp. 8 mit VSt. Abzug Verwaltungskosten Staat 190 (siehe Hilfsblatt Form. 2). `tg-form-02-2025__c0005` |
> | 8.1 | 180 | Eigenmietwert abzgl. Unterhalt | 4'840 | 8'920 | siehe Abschnitt 2 |
> | 6 | 175 | Zwischentotal Einkünfte | 39'960 | 40'150 | |
> | 9 | 198 | **Total Einkünfte** | **44'800** | **49'070** | 6 + 8.1 |
> 
> **Hilfsblatt Form. 2 (Wertschriften), Sp. 7–9 und Ziff. 10:**
> - Sparkonto: Steuerwert 48'000, Bruttozins 250 (> 200, daher Sp. 8 mit VSt 87.50).
> - Depot: Steuerwert 95'000, Bruttodividenden 2'100 (Sp. 8, VSt 735).
> - Steuerwert total (Sp. 7, Code 410): 143'000.
> - Verrechnungssteueranspruch Ziff. 10: 35 % × 2'350 = **822.50**. Der Anspruch besteht, weil der Wohnsitz am 31.12. in TG liegt und die Erträge vollständig deklariert sind. `tg-form-02-2025__c0006`
> - Verwaltungskosten Code 148: Staat min(2 ‰ × 95'000; 6'000) = **190**. Bund **0**, da nur effektive Kosten belegt sind und kein Gebührenausweis vorliegt.
> 
> ## 2. Liegenschaft (Form. 7 / Form. 8, Ziff. 8.1 und 31)
> 
> | | Staat | Bund |
> |---|---|---|
> | Mietwert selbstgenutzt (indexiert 2025) | 20'400 | 20'400 |
> | abzgl. Selbstnutzungsabzug (40 % Staat / 20 % Bund) | −8'160 | −4'080 |
> | **Steuerbarer Eigenmietwert** | **12'240** | **16'320** |
> | Pauschale 20 % (Gebäude 1986, älter als 10 Jahre) | 2'448 | 3'264 |
> | **Effektiver Unterhalt** (Malerarbeiten Ersatzanstrich 6'400 + Gebäudeversicherung 520 + Gartenpflege 480) | **7'400** | **7'400** |
> | Gewählt (höherer Abzug) | effektiv | effektiv |
> | **Nettoerfolg (Ziff. 8.1, Code 180)** | **4'840** | **8'920** |
> 
> - **Wintergarten-Anbau 31'000:** nicht abziehbar. Anbau ist wertvermehrend und gehört in Form. 8, Spalte «Anlagekosten/Mehrwert». `tg-wl-2025__c0238`, `tg-form-08-2025__c0001`
> - **Gebäudeversicherung 520:** Die Pauschale umfasst Versicherungsprämien (§ 9 Abs. 3 StV TG). Bei der effektiven Variante setze ich sie daher als Unterhalt an.
> - **Gartenpflege 480:** Im Wiki ist nicht belegt, dass Gartenpflege als Unterhalt gilt. Ohne diesen Posten wären es 6'920 effektiv, immer noch über der Pauschale. Das Ergebnis bleibt also gleich.
> - **Ziff. 31, Liegenschaften (Code 430):** Steuerwert **410'000** (rechtskräftige Schätzung).
> 
> ## 3. Abzüge
> 
> | Ziff. | Code | Inhalt | Staat | Bund | Rechnung / Fundstelle |
> |---|---|---|---|---|---|
> | 11 | 290 | Schuldzinsen Hypothek 2025 | 3'150 | 3'150 | Grenze privat = Vermögensertrag 2'350 + 50'000 eingehalten. `tg-form-01-2025__c0010` |
> | 14 | 330 | Versicherungsprämien / Sparzinsen | 3'500 | 2'700 | A = KK netto 6'240 + Sparzinsen 250 = 6'490. Staat: Limit alleinstehend 3'500. Bund: Limit alleinstehend **ohne Säule 2/3a** 2'700, da keine Beiträge an 2./3a. `tg-form-05-2-2025__c0003` |
> | 19 | 360 | **Total Abzüge** | **6'650** | **5'850** | 11 + 14 |
> 
> Hinweis zu Ziff. 14: Die Sparzinsen (250) sind laut Form. 5.2 A Ziff. 4 in der Abzugsbasis enthalten. Das Maximum wird ohnehin erreicht.
> 
> ## 4. Nettoeinkommen und Reineinkommen
> 
> | Ziff. | Code | Inhalt | Staat | Bund | Rechnung |
> |---|---|---|---|---|---|
> | 22 | 362 | **Nettoeinkommen** | **38'150** | **43'220** | 9 − 19 |
> | 23.1 | 364 | Krankheits-/Unfallkosten | 4'633 | 4'379 | Staat: A = Zahnarzt 4'440 + Brille 1'400 + Franchise/Selbstbehalt 1'000 = 6'840; B = Zusatz-Vergütung Brille 300; (A − B) = 6'540; − 5 % × 38'150 (1'907.50) = 4'632.50 → **4'633** (gerundet). Bund: 6'540 − 5 % × 43'220 (2'161) = 4'379. `tg-form-01-2025__c0012`, `tg-form-05-1-2025__c0001` |
> | 23.2 | 366 | Freiwillige Zuwendungen | 350 | 550 | Krebsliga 300 + Pro Senectute 250 = 550. Staat: 550 − 200 Selbstbehalt = 350 (Maximum 8'000 nicht erreicht). Bund: 550 (Minimum 100 erfüllt, Maximum 20 % = 8'644 nicht erreicht). `tg-form-06-2025__c0002` |
> | 24 | 372 | **Reineinkommen** | **33'167** | **38'291** | 22 − 23.1 − 23.2 |
> 
> ## 5. Sozialabzüge und steuerbares Einkommen
> 
> | Ziff. | Code | Inhalt | Staat | Bund | Rechnung / Fundstelle |
> |---|---|---|---|---|---|
> | 25.3 | 388 | Abzug AHV-Rentnerin / verwitwet | **1'000** | kein Abzug | 4'200 − 200 × 16 (33'167 − 16'900 = 16'267 → 16 volle Tausender). `tg-wl-2025__c0116`, `tg-form-01-2025__c0013` |
> | 26 | 398 | **Steuerbares Einkommen** | **32'167** | **38'291** | 24 − 25.3 |
> 
> Plausibilität: Bund über Kanton ist erwartbar, weil der Bund den Alters-Sozialabzug nicht kennt und der Eigenmietwert-Abzug beim Kanton höher ist.
> 
> ## 6. Vermögen (nur Staat)
> 
> | Ziff. | Code | Inhalt | Betrag |
> |---|---|---|---|
> | 30.1 | 410 | Wertschriften und Guthaben (Form. 2 Sp. 7) | 143'000 |
> | 31 | 430 | Liegenschaft (Steuerwert) | 410'000 |
> | 33 | 464 | **Total Vermögenswerte** | **553'000** |
> | 34 | 466 | Schulden (Hypothek per 31.12.) | 180'000 |
> | 35 | 468 | **Reinvermögen** | **373'000** |
> | 36.2 | 472 | Freibetrag alleinstehend | 100'000 |
> | 37 | 498 | **Steuerbares Vermögen** | **273'000** |
> 
> Der Bund hat keine Vermögenssteuer. Die Ziffern 30.2–30.6 bleiben leer (keine Angaben: Bargeld, Lebensversicherungen, Fahrzeuge).
> 
> ## 7. Was nicht zu deklarieren bzw. nicht abziehbar ist
> 
> - **PK-/Vorsorgeguthaben:** keine Angaben, da Rentnerin. Die Rente gehört in Ziff. 3.2, nicht ins Vermögen. Ziff. 13 (Säule 3a) bleibt leer. `tg-wl-2025__c0139`
> - **Hausratversicherung 380:** Sachversicherung, nicht abziehbar. `tg-wl-2025__c0209` (Hinweis Mobiliar-/Sachversicherungen)
> - **Serafe 335:** keine Abzugsposition im Formular gefunden. Nicht deklarieren.
> - **Handyrechnung:** Lebenshaltung, keine Position.
> - **Krankenkassenprämien:** nur in Ziff. 14, nicht in Ziff. 23.1.
> - **Wintergarten 31'000:** nicht abziehbar, siehe Abschnitt 2.
> - **Spenden unter 1'000:** keine Quittungen beilegen, nur auf Verlangen.
> 
> ## 8. Beilagen (Einreichung)
> 
> - KK-Jahresbescheinigung mit Nettoprämie (`tg-wl-2025__c0210`, WL S. 44).
> - Krankheitskosten geordnet, KK-Leistungsabrechnung, Verordnung für die Brille (Kopie).
> - Rechnungskopien für Einzelbeträge ab 1'000, falls effektiver Unterhalt: Malerarbeiten 6'400 (`tg-wl-2025__c0234`).
> - Hypothekarbestätigung per 31.12.2025 und Bank-Steuerauszug.
> - Nachweis Verwitwung/AHV-Rentenbescheinigung für Ziff. 25.3.
> 
> ## 9. Offene Punkte und Annahmen
> 
> 1. **Wintergarten-Anbau:** Die Baukosten 31'000 können einen Zuschlag zum Steuerwert auslösen. Bitte bei der Steuerverwaltung nachfragen, ob eine Meldung nötig ist (`tg-stp-23-1__c0004`). Ich habe den Steuerwert 410'000 unverändert übernommen.
> 2. **Zahnarzt 4'440:** Annahme, dass die Krankenkasse nichts vergütet hat. Falls doch, sinkt Ziff. 23.1 entsprechend.
> 3. **Depot-Verwaltungskosten:** Pauschale 190 (Staat). Ein Gebührenausweis der Bank würde den Betrag nur erhöhen, wenn er höher ausfällt.
> 4. **Rundung:** Formular nur in ganzen Franken. Ziff. 23.1 Staat 4'632.50 → 4'633.
> 5. **Alters-Abzugstabelle:** Die Wegleitung zeigt bei der Zeile «36'900–37'689» einen Druckfehler. Für 33'167 ist das nicht relevant (Formel § 1 Ziff. 3 VAKP: 1'000).
> 6. **Nicht geprüft:** Gartenpflege als Unterhalt (siehe Abschnitt 2). Die fachliche Beurteilung bleibt bei der Fachperson.
> 
> Die Angaben beruhen auf den Wiki-Quellen für TG 2025 (Formular 1, Hilfsblätter 2, 5.1, 5.2, 6, 7, 8 sowie WL TG 2025). Die Werte haben den Status ☑️ und sind noch nicht abgenommen.

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


**Antwort des Agenten** (134.2 s · Tools: 15 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__suche, steuerwiki__wert, steuerwiki__rechne):

> **Kanton AR · Steuerjahr 2025** · Ehepaar, Herisau, beide erwerbstätig, zwei Kinder (Lea 4 J., Jonas 16 J. am 31.12.2025)
> 
> Die Formularziffern stammen aus dem AR-Formular 2025 (Hauptformular). Die Codes auf Seite 3 sind nicht aus der Wegleitung verifiziert; bitte am Original prüfen. Die AR-Erklärung hat keine Bundesspalte. Die Steuerverwaltung nimmt die Abweichungen für den Bund automatisch vor. Ich habe deshalb zwei Bemessungsspalten gerechnet, die Steuerberechnung (Tarif) selbst ist nicht enthalten.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Inhalt | Kanton | Bund | Rechenweg / Fundstelle | Status |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Person 1: Nettolohn | 85'300 | 85'300 | Lohnausweis Ziff. 11 (nicht Ziff. 8) | ☑️ |
> | 1.1 | 102 | Person 2: Nettolohn | 68'200 | 68'200 | Lohnausweis Ziff. 11; Einkauf 4'000 ist bereits abgezogen | ☑️ |
> | 3.5 | 142 | Kinderzulagen | – | – | Zulagen sind in Lohnausweis Ziff. 8 enthalten, daher in 1.1. Ziff. 3.5 nur bei Direktauszahlung durch die Ausgleichskasse | ☑️ (Ziff. 3.5 Formular-Position) |
> | 4.1 | 146 | Bruttoerträge Konten 160 (Spalte B) + Aktien-Dividenden 1'250 (Spalte A) | 1'410 | 1'410 | Form. 2: A + B = 1'250 + 160; keine G/BP/BG. Erträge in Spalte A mit VSt, Konten ohne VSt | ☑️ |
> | 7 | 168 | Total Einkünfte | 154'910 | 154'910 | 85'300 + 68'200 + 1'410 | ✅ rechne |
> 
> Form. 2 zusätzlich: VSt-Anspruch 35 % × 1'250 = **437.50** (Code 999). Das Formular verlangt Rappen hier, deshalb ist der Betrag mit Rappen anzugeben.
> 
> ## 2. Abzüge
> 
> | Ziff. | Code | Inhalt | Kanton | Bund | Rechenweg / Fundstelle | Status |
> |---|---|---|---|---|---|---|
> | 10.1 | 438 (Form. 4) | Berufskosten Person 1 | 4'000 | 4'159 | Verpflegung Ziff. 2.2 (Code 410): Feld G angekreuzt, 7.50 × 220 = 1'650, Max. 1'600 → 1'600 (K und B). Fahrkosten 0, weil Feld F angekreuzt. Pauschale übrige Kosten: K 700 + 10 % × 85'300 = 9'230, Max. 2'400 → 2'400; B 3 % × 85'300 = 2'559 (Min. 2'000, Max. 4'000) | ☑️ ar-form-04-2025__c0004/c0003, ar-wl-2025__c0076 |
> | 10.2 | 488 (Form. 4) | Berufskosten Person 2 | 6'300 | 5'946 | ÖV-Abo Ziff. 1.1 (Code 450): 1'260 (K und B). Verpflegung Ziff. 2.1 (Code 458): 15 × 176 = 2'640 (Annahme, siehe Offene Punkte). Pauschale übrige: K 2'400 (700 + 10 % × 68'200 = 7'520 → Max.); B 2'046 (3 % × 68'200) | ☑️ ar-wl-2025__c0074/c0075, ar-form-04-2025__c0003 |
> | 13.1 | ⬜ | Säule 3a Person 1 | 7'258 | 7'258 | Min(bezahlt 7'258; Max. 7'258 mit 2. Säule) | ☑️ ar-wl-2025__c0003 |
> | 13.1 | ⬜ | Säule 3a Person 2 | 5'000 | 5'000 | Min(bezahlt 5'000; 7'258) | ☑️ |
> | 13.2 | ⬜ | Einkauf 2. Säule | 0 | 0 | Der Einkauf 4'000 ist bereits als Lohnausweis Ziff. 10.2 abgezogen. Nicht doppelt ansetzen | ⚠️ strittig (ar-wl-2025__c0084) |
> | 14 | ⬜ | Versicherungsprämien/Sparzinsen | 7'400 | 5'100 | A = Krankenkasse 13'900 + Sparzinsen 160 = 14'060. B Kanton = 5'400 + 2 × 1'000 = 7'400. B Bund = 3'700 + 2 × 700 = 5'100. Abzug = min(A; B) | ☑️ ar-form-06-2025__c0001/c0002 |
> | 16.2 | ⬜ | Kinderbetreuung Lea (Kita) | 10'200 | 10'200 | 14'400 − Mittagessen 1'800 − Betreuungsbeitrag 2'400 = 10'200 (≤ 25'000 / 25'800). Bund-Wert analog angenommen | ☑️ ar-form-10-2025__c0001/c0002, ar-wl-2025__c0091 |
> | 17 | ⬜ | Zweiverdienerabzug | 5'200 | 14'100 | K: 10 % des niedrigeren Einkommens (≥ 6'190) → Max. 5'200. B: 50 % (≥ 30'000) → Max. 14'100 | ☑️ ar-wl-2025__c0096/c0097; bund-dbg-2025__art-33-t6 |
> | 18 | – | Total Abzüge | 45'358 | 51'763 | Summe der Abzüge oben | ✅ rechne |
> | 20 | – | Nettoeinkommen | 109'552 | 103'147 | 154'910 − 18 | ✅ rechne |
> | 21.1 | ⬜ | Krankheitskosten | 0 | 0 | Keine Belege vorgelegt | – |
> | 21.3 | 550 | Spende Krebsliga Ostschweiz | 300 | 300 | ≥ 100 und ≤ 20 % × Nettoeinkommen (21'910) → 300 | ☑️ ar-form-05-2025__c0003; Steuerbefreiung der Empfängerin nicht geprüft |
> | 22 | – | Reineinkommen | 109'252 | 102'847 | 20 − 21 | ✅ rechne |
> 
> ## 3. Kinderabzüge und steuerbares Einkommen
> 
> | Ziff. | Inhalt | Kanton | Bund | Rechenweg / Fundstelle | Status |
> |---|---|---|---|---|---|
> | 23.2 | Lea (am 31.12. 4 Jahre; 4. bis 15. Altersjahr) | 7'400 | 6'800 | Kanton 7'400; Bund 6'800 | ☑️ ar-wl-2025__c0005 |
> | 23.3 | Jonas (16 Jahre, Kantonsschule) | 11'600 | 6'800 | Kanton 11'600; Bund 6'800 | ☑️ ar-wl-2025__c0005 |
> | 23.1 | Kind bis 4. Altersjahr | 0 | 0 | nicht zutreffend | – |
> | 23.4 | Unterstützungsabzug | 0 | 0 | nicht zutreffend | – |
> | 24 | Steuerbares Einkommen | 90'252 | 86'447 | K: 109'252 − 19'000. B: 102'847 − 13'600 (Kinder) − 2'800 (Verheiratetenabzug, nur Bund) | ✅ rechne |
> 
> ## 4. Vermögen
> 
> | Ziff. | Code | Inhalt | Kanton | Bund | Rechenweg / Fundstelle | Status |
> |---|---|---|---|---|---|---|
> | 30.1 | 300 | Konten 54'000 + Aktien 38'000 | 92'000 | – | Steuerwerte 31.12.2025 (Form. 2) | ☑️ ar-form-02-2025__c0005/c0007 |
> | 33 | 322 | Total Vermögenswerte | 92'000 | – | | ✅ |
> | 34.1/34.2 | 504/506 | Schulden | 0 | – | keine | – |
> | 35 | 326 | Reinvermögen | 92'000 | – | 92'000 − 0 | ✅ |
> | 36.2 | 332 | Sozialabzug Ehegatten | 150'000 | – | Position Formular 1 | ☑️ Fundstelle nicht einzeln abgerufen |
> | 36.3 | 334 | Sozialabzug je minderjähriges Kind (2 Kinder) | 50'000 | – | 2 × 25'000 | ☑️ wie oben |
> | 37 | 338 | Steuerbares Vermögen | 0 | – | max(92'000 − 150'000 − 50'000; 0) | ✅ rechne |
> 
> Vorsorgeguthaben (2. Säule, Säule 3a) gehören nicht ins Vermögen. Das Formular sagt, sie sind bis zur Fälligkeit steuerfrei.
> 
> ## 5. Was nicht zu deklarieren ist
> 
> - **Lohnausweis Ziff. 8 (Bruttolohn):** Eingesetzt wird nur Ziff. 11 (Nettolohn).
> - **Einkauf 4'000 (Person 2):** Bereits im Lohnausweis Ziff. 10.2 abgezogen, daher nicht in 13.2.
> - **Säule-3a- und Pensionskassen-Guthaben:** Nicht Vermögen (bis Fälligkeit).
> - **Kita-Mittagessen 1'800:** Lebenshaltungskosten, nicht abziehbar.
> - **Betreuungsbeitrag 2'400:** Wird von den Kita-Kosten abgezogen. Kein eigenes Einkommen.
> - **Turnverein-Mitgliederbeitrag 120:** Mitgliederbeiträge sind nicht abziehbar (Ziff. 21.3, Regel).
> - **Handy-Abo 960:** Private Kosten, keine Formularposition.
> - **Schlussrechnung 2024 (Steuern 9'870):** Kein Abzug vorgesehen. Im Wiki habe ich dafür keine ausdrückliche Fundstelle gefunden; bitte bei der Fachperson bestätigen.
> - **Verrechnungssteuer 437.50:** Ist ein Anspruch (Form. 2, Code 999), kein Abzug.
> - **Feld F (Werkbus, Person 1):** Kein Fahrkostenabzug.
> 
> ## 6. Offene Punkte und Annahmen
> 
> 1. **Verpflegung Person 2 (Ziff. 2.1, 2'640):** Das gilt nur, wenn Heimkehr zum Mittag nicht zumutbar ist (Herisau–St. Gallen). Ist sie zumutbar, entfällt der Abzug. Dann ändern sich die Zahlen: Ziff. 10.2 K 3'660 / B 3'306; Nettoeinkommen K 112'192 / B 105'787; steuerbares Einkommen **K 92'892 / B 89'087**.
> 2. **Kantine Person 1 (Feld G):** Ziff. 2.2 gilt nur, wenn die Verbilligung nicht so weit geht, dass keine Mehrkosten gegenüber Zuhause entstehen. Kantinenpreis prüfen.
> 3. **Konten-Zinsen 160:** In Spalte B nur, wenn jedes Konto unter 200 Franken Bruttozins hat. Pro Konto prüfen.
> 4. **Krebsliga Ostschweiz:** Steuerbefreiung prüfen (Ziff. 21.3 setzt sie voraus).
> 5. **Kita-Abzug Bund (10'200):** Analog zum Kanton angenommen.
> 6. **Einkauf 13.2:** Die Wegleitung widerspricht sich. Fachperson klären lassen.
> 7. **Codes:** Hauptformular-Codes für 13.x, 14, 16.2, 17, 21.3 nicht verifiziert.
> 8. **Steuerbetrag (Tarif):** Nicht berechnet.
> 
> ## 7. Einreichen (Belege)
> 
> - Lohnausweise beider Personen: ja.
> - Säule-3a-Bescheinigungen: ja.
> - Einkauf-Bescheinigung: ja (auch wenn 13.2 = 0).
> - Bank-Steuerauszug vollständig: ja, weil Formular 2 übertragen wird.
> - ÖV-Abo, Krankenkassen-Prämien, Kita-Rechnungen, Spendenquittung: auf Verlangen bereithalten.

