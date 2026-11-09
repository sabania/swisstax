# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 16:52
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


**Antwort des Agenten** (127.9 s · Tools: 28 Aufrufe read, steuerwiki__formular, read, steuerwiki__position, steuerwiki__suche, steuerwiki__wert, steuerwiki__zeige, steuerwiki__rechne):

> Ich habe die Positionen und Limiten im Steuer-Wiki nachgeschlagen und rechne jetzt die Totale exakt durch.
> 
> # Ausfüllhilfe ZH 2025, Ehepaar Marco und Sandra, Winterthur
> 
> Formular: Steuererklärung 2025 Kanton Zürich (Form. 300) mit Hilfsblättern 340, 360, 365 und 370. Das Formular hat zwei Spalten, Staatssteuer (K) und Bundessteuer (B). Status aller Werte: ☑️ agent-geprüft, Abnahme durch die Fachperson offen.
> 
> ## Einkünfte
> 
> | Ziffer | Code | Position | K | B | Rechenweg und Fundstelle |
> |---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb Marco | 103'000 | 103'000 | Nettolohn laut Lohnausweis Ziff. 11. Er stimmt mit 118'400 − 8'110 − 7'290 überein. `zh-form-300-2025__c0004` |
> | 1.1 | 101 | Haupterwerb Sandra | 67'200 | 67'200 | 76'800 − 5'260 − 4'340 = 67'200. Die Kinderzulagen von 4'800 stecken schon im Lohn und werden nicht separat erfasst oder abgezogen. |
> | 4.1 | 150 | Wertschriftenertrag | 1'140 | 1'140 | Form. 340 Kolonne A: Dividenden 960 (VSt 336 = 35 %). Kolonne B: Sparzins 180 (unter 200, ohne VSt). `zh-form-340-2025__c0005` |
> | 7 | 199 | **Total Einkünfte** | **171'340** | **171'340** | 103'000 + 67'200 + 960 + 180 |
> 
> Im Form. 340 beantragen Sie die Verrechnungssteuer von 336 (Code 540) zur Rückerstattung. Dort tragen Sie auch den Steuerwert von 82'000 ein (Sparkonto 42'500 + Privatkonto 8'300 + Depot 31'200).
> 
> ## Abzüge
> 
> | Ziffer | Code | Position | K | B | Rechenweg und Fundstelle |
> |---|---|---|---|---|---|
> | 11.1 | 220 | Berufsauslagen Marco (Form. 360) | 10'470 | 9'590 | ÖV-Abo (Code 201): K 4'180, B 3'300, weil der Bundesplafond 3'300 beträgt. Verpflegung voll (Code 208): min(220 × 15; 3'200) = 3'200. Übrige (Code 212): 3 % × 103'000 = 3'090. |
> | 11.2 | 240 | Berufsauslagen Sandra (Form. 360) | 4'036 | 4'036 | Velo pauschal (Code 222) 700. Verpflegung verbilligt, Feld G (Code 226): 176 × 7.50 = 1'320. Übrige (Code 232): 3 % × 67'200 = 2'016. |
> | 14.1 | 260/262 | Säule 3a Marco | 7'258 | 7'258 | Limite mit 2. Säule 7'258. `zh-wl-2025__c0081` |
> | 14.2 | 261/263 | Säule 3a Sandra | 7'258 | 7'258 | wie oben |
> | 15 | 270 | Versicherungsprämien (Form. 365) | 8'400 | 5'100 | Teil A: 15'840 (Code 601) + 180 Sparzins (Code 604) = 16'020. Teil B: K 5'800 + 2 × 1'300, B 3'700 + 2 × 700. Der tiefere Betrag gilt, also Teil B. |
> | 16.1 | 280 | PK-Einkauf Marco | 10'000 | 10'000 | Lohnausweis Ziff. 10.2 ist 0, also nichts doppelt. Bescheinigung beilegen. `zh-wl-2025__c0092` |
> | 16.6 | 376 | Fremdbetreuung | 31'900 | 32'700 | Lena: min(27'300; 25'000 K / 25'800 B). Noah: 6'900 voll. Das Maximum gilt pro Kind. `zh-stg-2025__par-31-t4` |
> | 17 | 290 | Zweiverdienerabzug | 6'100 | 14'100 | Basis: tieferes Erwerbseinkommen (Sandra) 67'200 − 4'036 − 7'258 = 55'906. K: min(55'906; 6'100). B: 50 % = 27'953, gedeckelt auf 14'100. `zh-form-300-2025__c0008` |
> | 18 | 299 | **Total Abzüge** | **85'422** | **90'042** | |
> 
> ## Nettoeinkommen und Sozialabzüge
> 
> | Ziffer | Code | Position | K | B | Rechenweg und Fundstelle |
> |---|---|---|---|---|---|
> | 21 | 310 | **Nettoeinkommen** | **85'918** | **81'298** | 171'340 − Total Abzüge |
> | 22.1 | 320 | Krankheitskosten | 0 | 0 | Kosten 3'090 (Zahnarzt 1'850 + Franchise/Selbstbehalt 1'240). Der Selbstbehalt von 5 % beträgt K 4'295.90 und B 4'064.90. Er wird nicht überschritten, also kein Abzug. |
> | 22.2 | 324 | Gemeinnützige Zuwendungen | 650 | 650 | SRK 400 + UNICEF 250. Das Minimum von 100 ist erreicht. Das Maximum von 20 % (K 17'183.60, B 16'259.60) ist nicht überschritten. `zh-wl-2025__c0122` |
> | 23 | 350 | **Reineinkommen** | **85'268** | **80'648** | |
> | 24.1 | 370 | Kinderabzug (2 Kinder im Haushalt) | 18'600 | 13'600 | 2 × 9'300 bzw. 2 × 6'800. Keine Altersstaffel im ZH. `zh-wl-2025__c0126` |
> | 24.3 | 365 | Verheiratetenabzug (nur Bund) | – | 2'800 | |
> | 25 / 27 | 390 / 398 | **Steuerbares Einkommen** | **66'668** | **64'248** | 85'268 − 18'600 bzw. 80'648 − 16'400 |
> 
> Beim Bund ermässigt sich der Steuerbetrag zusätzlich um 2 × 263 = 526 (Art. 36 DBG). Das geschieht im Tarif, nicht im Formular.
> 
> ## Vermögen
> 
> | Ziffer | Code | Position | Betrag |
> |---|---|---|---|
> | 30.1 | 400 | Wertschriften und Guthaben | 82'000 |
> | 34 | 470 | Schulden | 0 |
> | 35 / 37 | 490 / 498 | **Steuerbares Vermögen** | **82'000** |
> 
> Der Steuerfreibetrag wirkt nur im Tarif und wird nicht abgezogen.
> 
> ## Nicht zu deklarieren oder nicht abzugsfähig
> 
> - **Swisscom-Handyrechnungen (1'080):** private Lebenshaltung, kein Abzug.
> - **Hausrat- und Privathaftpflichtversicherung (465):** Form. 365 Teil A nennt nur Kranken-, Unfall-, Lebens- und Rentenversicherung sowie Sparzinsen (`zh-form-365-2025__c0001`). Ich habe keine Wiki-Fundstelle, die Sachversicherungen ausdrücklich ausschliesst. Die Einordnung ist daher eine Ableitung, die Sie prüfen sollten. Sie ändert nichts am Ergebnis, weil der Abzug ohnehin am Maximum liegt.
> - **Krankenkassenprämien über dem Maximum:** 16'020 gegenüber 8'400 (K) bzw. 5'100 (B). Der Überhang ist nicht abziehbar. Prämien sind auch keine Krankheitskosten (Form. 370 Ziff. 1).
> - **Kinderzulagen 4'800:** nicht separat erfassen, siehe Ziff. 1.1 Sandra.
> - **Verpflegung in der Kita von Lena:** laut Rechnung nicht enthalten, und Verpflegung gehört nicht zur Betreuung (Ziff. 16.6).
> - **Ziff. 40 (Kapitalleistungen aus Vorsorge):** nichts einzutragen.
> - **Nicht angefallen:** Schuldzinsen (Ziff. 12), Liegenschaften (Ziff. 6 und 31), Verwaltungskosten (Ziff. 16.3, keine Depotgebühren belegt), Weiterbildung.
> - **Fahrkosten Marco:** Lohnausweis Feld F ist nicht angekreuzt, also ist der Abzug zulässig.
> 
> ## Beizulegen
> 
> - Beide Lohnausweise
> - Bescheinigungen Säule 3a
> - Bescheinigung PK-Einkauf
> - Aufstellung der Betreuungskosten (Ziff. 16.6) und Aufstellung der Zuwendungen (Ziff. 22.2)
> - Form. 360 für beide Personen und Form. 365
> - Form. 340 mit dem Bank-Steuerauszug
> 
> ## Annahmen und Rückfragen an die Fachperson
> 
> 1. **Sandra, Verpflegung (1'320):** Ich habe den Standardfall mit Feld G erfasst (176 Tage × 7.50). Der Abzug gilt nur, wenn die Heimkehr in der Mittagspause nicht möglich ist. Arbeitsort und Wohnort sind beide Winterthur. Bitte klären Sie, ob Sandra über Mittag nach Hause gehen könnte. Wenn ja, entfällt der Abzug, das Nettoeinkommen steigt um 1'320 und die Krankheitskosten bleiben ohne Abzug.
> 2. **Marco, Verpflegung (3'200):** Beim Bund gibt es keinen Abzug, wenn die Hauptmahlzeit höchstens 10 Fr. kostet. Ich nehme an, dass sie mehr kostet.
> 3. **PK-Einkauf:** Bestätigen Sie, dass seit 2022 kein Kapitalbezug erfolgt ist (Sperrfrist drei Jahre) und dass der Einkauf das Einkaufspotenzial laut Bescheinigung nicht übersteigt. Beides ist angegeben, aber nicht geprüft.
> 4. **Plausibilität:** Das steuerbare Einkommen beim Bund (64'248) liegt 2'420 unter dem des Kantons (66'668). Das ist erklärbar durch den Zweiverdienerabzug (+8'000), den Verheiratetenabzug (+2'800) und die höhere Betreuungslimite (+800). Dagegen wirken der tiefere Fahrkostenplafond (−880), der tiefere Versicherungsabzug (−3'300) und der tiefere Kinderabzug (−5'000).
> 
> Zum Schluss noch kurz: Ich bin Ihr neuer Assistent. Wie möchten Sie mich nennen?

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


**Antwort des Agenten** (122.2 s · Tools: 30 Aufrufe read, steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__wert, message, steuerwiki__rechne):

> # Ausfüllhilfe SG 2025: Nadine (alleinerziehend, 1 Kind)
> 
> Formular: Steuererklärung 2025 Formular 1 mit Hilfsblättern Form. 2, 4, 6 und 10. Es gibt eine Spalte für Kanton und Bund. Die Bundesbeträge setzt das Steueramt automatisch um (sg-wl-2025__c0173). Ich weise sie hier trotzdem getrennt aus. Alle Werte haben den Status ☑️ agent-geprüft, die Abnahme durch die Fachperson ist offen.
> 
> ## Einkünfte
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb unselbständig | 73'000 | 73'000 | Lohnausweis Ziff. 11 (Nettolohn). 83'500 − 5'890 − 4'610 = 73'000. Die Kinderzulage 2'400 ist darin enthalten. | Beleg `lohnausweis` |
> | 6.1 | 156 | Unterhaltsbeiträge für minderjährige Kinder | 9'600 | 9'600 | 12 × 800 laut Kontoauszug. Beim Empfänger steuerbar. | sg-form-1-2025__c0006, sg-wl-2025__c0068 |
> | 4.1 | 146 | Wertschriften/Guthaben | 68 | 68 | Bruttozins Raiffeisen. Bis Fr. 200 gehört er in Form. 2 Spalte B, ohne Verrechnungssteuer. | sg-wl-2025__c0135 |
> | **7** | 168 | **Total Einkünfte** | **82'668** | **82'668** | 73'000 + 9'600 + 68 | |
> 
> ## Abzüge
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 10.1 | 438 | Berufskosten (Total Form. 4 Ziff. 6) | 13'600 | 8'690 | Aufteilung siehe unten | sg-form-4-2025__c0002/c0003 |
> | 13.1 | 208 | Säule 3a | 7'258 | 7'258 | Bescheinigung 7'258 entspricht dem Maximum mit 2. Säule. | `wert sg 2025 saeule3a` |
> | 13.2 | 218 | PK-Einkauf | 6'000 | 6'000 | Bescheinigung, direkt bezahlt am 20.10.2025. Lohnausweis Ziff. 10.2 ist 0, also kein Doppelabzug. | sg-wl-2025__c0086 |
> | 14 | 600 | Versicherungsprämien (Form. 6) | 4'500 | 2'500 | A = 5'280 + 1'320 + 68 − 1'800 = 4'868. B Staat = 3'400 + 1'100 = 4'500. B Bund = 1'800 + 700 = 2'500. Es gilt der niedrigere Betrag. | sg-form-6-2025__c0002 |
> | 16.2 | 258 | Kinderbetreuung Drittbetreuung (Form. 10) | 8'760 | 8'760 | 9'840 − 1'080 Mahlzeiten. Das liegt unter dem Maximum (Staat 26'700, Bund 25'800). | sg-wl-2025__c0092 |
> | 16.4 | 223 | Weiterbildung (Excel-Kurs) | 400 | 340 | Staat: Pauschale 400 ist höher als die effektiven 340. Bund: nur effektive Kosten. | sg-wl-2025__c0094 |
> | **18** | 230 | **Total Abzüge** | **40'518** | **33'548** | | |
> | **20** | 234 | **Nettoeinkommen** | **42'150** | **49'120** | 82'668 − Total Abzüge | |
> 
> **Berufskosten, Form. 4:**
> 
> | Form. 4 | Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 1.3 | 404/406 | Fahrkosten Privatauto | 8'000 | 3'300 | 32 × 2 × 220 = 14'080 km × 0.70 = 9'856, begrenzt auf das Maximum (Staat 8'000, Bund 3'300) |
> | 2.1 | 408 | Auswärtige Verpflegung | 3'200 | 3'200 | min(220 × 15 = 3'300; 3'200) |
> | 3.1 | 416 | Übrige Berufskosten pauschal | 2'400 | 2'190 | Staat: min(700 + 10 % × 73'000; 2'400). Bund: 3 % × 73'000 = 2'190, innerhalb 2'000–4'000. |
> | 6 | 438 | Total | 13'600 | 8'690 | |
> 
> Form. 4 Ziff. 1.3 verlangt eine Begründung. Ankreuzen: «Fehlen eines öffentlichen Verkehrsmittels» (erste öV-Verbindung 06:40, Arbeitsbeginn 06:00). Lohnausweis Feld F und Feld G sind nicht angekreuzt, also gilt Ziff. 2.1 und nicht 2.2.
> 
> ## Abzüge auf Basis Nettoeinkommen und Sozialabzüge
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 21.1 | 650 / 238 / 240 | Krankheitskosten (Form. 6 Rückseite) | 2'757 | 1'144 | Vorkolonne 850 + 2'750 = 3'600. Selbstbehalt Staat 2 % × 42'150 = 843, Bund 5 % × 49'120 = 2'456. | sg-wl-2025__c0098 |
> | 21.3 | 244 | Zuwendungen | 0 | 0 | 80 liegt unter der Mindestsumme von 100 (Staat und Bund). | sg-wl-2025__c0102, bund-dbg-2025__art-33a |
> | **22** | 248 | **Reineinkommen** | **39'393** | **47'976** | 42'150 − 2'757 bzw. 49'120 − 1'144 | |
> | 23.2 | 254 | Kinderabzug (Kind in Schule) | 10'800 | 6'800 | Elias besucht seit August 2025 den Kindergarten. Der Kindergarten zählt zur Schulpflicht, daher 23.2 und nicht 23.1 (7'600). | sg-form-1-2025__c0011, sg-wl-2025__c0104 |
> | **24** | 268 | **Steuerbares Einkommen** | **28'593** | **41'176** | 39'393 − 10'800 bzw. 47'976 − 6'800 | |
> 
> Beim Bund kommt der Abzug vom Steuerbetrag dazu (263 pro Kind, nur Bund). Ihn setzt das Steueramt automatisch um.
> 
> Dass das Bundeseinkommen höher ist, ist plausibel. Es entsteht durch die tieferen Bundeslimiten bei Fahrkosten, Versicherung und Kinderabzug und das höhere Selbstbehalt-Prozent.
> 
> ## Vermögen (nur Staat)
> 
> | Ziff. | Code | Position | Betrag | Bemerkung |
> |---|---|---|---|---|
> | 30.1 | 300 | Sparkonto Raiffeisen | 31'500 | Steuerwert 31.12.2025 |
> | 30.4 | 306 | Motorfahrzeug | ⬜ offen | Der Wert fehlt: Anschaffungswert − 20 % pro Jahr seit Erwerb. |
> | 36.1 / 36.3 | 330 / 334 | Sozialabzüge Vermögen | 75'000 + 20'000 | alleinstehend plus 1 minderjähriges Kind |
> 
> Solange der Autowert unter 63'500 liegt, ist das steuerbare Vermögen (Ziff. 37) 0. Der Bund erhebt keine Vermögenssteuer.
> 
> ## Nicht zu deklarieren oder nicht abziehbar
> 
> - **Motorfahrzeugsteuer 410 und Auto-Haftpflicht/Kasko 1'020:** Die Autokosten sind mit 0.70 Fr./km abgegolten. Haftpflicht- und Motorfahrzeugversicherungen sind bei Ziff. 14 ausdrücklich nicht abziehbar.
> - **Handy-Abo 720:** Das ist mit der Pauschale für übrige Berufskosten abgegolten. Effektiv wäre es nur günstiger, wenn alle übrigen Kosten die Pauschale übersteigen. Hier sind es 720 gegenüber 2'400 beziehungsweise 2'190.
> - **Spende Caritas 80:** Sie liegt unter der Mindestsumme von 100.
> - **Kita-Mahlzeiten 1'080:** Verpflegung ist bei Ziff. 16.2 nicht abziehbar.
> - **BVG ordentlich 4'610 und AHV/ALV 5'890:** Sie sind im Nettolohn schon berücksichtigt.
> - **Kinderzulage 2'400:** Sie steckt im Lohnausweis und wird nicht separat unter 3.5 erfasst.
> - **Prämienverbilligung 1'800:** Sie ist kein Einkommen. Sie wird in Form. 6 Teil A als Zeile e abgezogen.
> - **Krankenkassenprämien 6'600:** Sie gehören zu Ziff. 14 und nicht zu 21.1.
> - **Zweiverdienerabzug (Ziff. 17), Unterhaltsabzug (12.2) und Verwaltungskosten (16.1):** Nadine ist nicht verheiratet, sie bezieht die Alimente, und es gibt kein Depot und keine Gebührenbelege.
> 
> ## Fehlende Belege und offene Punkte für die Fachperson
> 
> 1. **Auto-Wert (Ziff. 30.4):** Der Kaufpreis und das Erwerbsjahr fehlen.
> 2. **Fahrkosten (Annahme):** Ich habe die Begründung «kein öV» als anerkannt angenommen. Ohne sie wären nur die fiktiven öV-Kosten abziehbar (StB 39 Nr. 3, Ziff. 2.1), und dafür liegt kein Beleg vor. Der Staatsabzug würde dann sinken.
> 3. **Arbeitstage (Annahme):** 220 Arbeitstage für Fahrkosten und Verpflegung, ohne Home-Office oder Absenzen. Bitte mit Nadine bestätigen.
> 4. **Einzureichende Belege:**
>    - Lohnausweis, Bescheinigung PK-Einkauf mit Einkaufsberechnung, Säule-3a-Bescheinigung.
>    - Bei erstmaliger Zahlung ein Auszug aus dem Scheidungsurteil mit den Zahlungsnachweisen für die Alimente (sg-wl-2025__c0084).
>    - Form. 10 für die Kita.
>    - Form. 6 mit der KK-Leistungsübersicht und der Zahnarztrechnung.
> 5. **Tarif:** Der Bund kennt einen Einelternfamilien-Tarif (Formular 32). Das ist keine Deklaration, es wirkt nur im Tarif. Ich habe es nicht weiter geprüft.
> 
> Nebenbei: Ich bin hier neu eingerichtet. Wie möchtest du mich nennen?

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


**Antwort des Agenten** (143.6 s · Tools: 40 Aufrufe read, steuerwiki__formular, steuerwiki__position, steuerwiki__wert, steuerwiki__zeige, steuerwiki__suche, message, steuerwiki__beleg, steuerwiki__rechne):

> # Ausfüllhilfe TG 2025 – verwitwete Rentnerin, alleinstehend, Frauenfeld
> 
> Formular: Steuererklärung 2025 TG (Formular 1) mit Hilfsblättern 2, 4.1, 5.1, 5.2, 6, 7 und 8. Es hat zwei Spalten, links Staat/Gemeinde (K) und rechts direkte Bundessteuer (B). Fundstellen sind Chunk-IDs. Status ☑️ heisst: Fundstelle agent-geprüft, Abnahme durch die Fachperson offen. Alle Beträge sind in CHF und mit `rechne` gerechnet.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | K | B | Beleg | Rechenweg / Regel | Fundstelle |
> |---|---|---|---|---|---|---|---|
> | 3.1 | 130 | AHV-Rente | 27'000 | 27'000 | AHV-Bescheinigung | 12 × 2'250, zu 100 % steuerbar | tg-wl-2025__c0076 ☑️ |
> | 3.2 | 132 | PK-Rente (Satz 100 %) | 10'800 | 10'800 | PK-Bescheinigung | 12 × 900. Rentenbeginn 2020, daher kein Übergangsrecht (80 % gilt nur bei Beginn vor 2002). | tg-wl-2025__c0077 ☑️ |
> | 4 | 150 | Wertschriftenertrag, Übertrag aus Form. 2 Ziff. 9 | 2'160 | 2'350 | TKB-Steuerauszug | Brutto 250 + 2'100 = 2'350. K abzüglich 190 Verwaltungskosten, siehe 1a. | tg-wl-2025__c0163 ☑️ |
> | 6 | 175 | Zwischentotal | 39'960 | 40'150 | | | |
> | 8.1 | 180 | Liegenschaft, Nettoerfolg aus Form. 7 | 4'840 | 8'920 | siehe 1b | | tg-wl-2025__c0225 ☑️ |
> | **9** | 198 | **Total Einkünfte** | **44'800** | **49'070** | | | |
> 
> ### 1a. Form. 2 Wertschriftenverzeichnis
> 
> - **Sparkonto (Sp. 7 Steuerwert 48'000):** Der Zins von 250 liegt über 200, die Verrechnungssteuer (VSt) ist abgezogen. Er gehört daher in **Spalte 8** (mit VSt) (tg-wl-2025__c0153).
> - **Aktiendepot (Sp. 7 Steuerwert 95'000):** Die Dividenden von 2'100 gehören in **Spalte 8**.
> - **Verrechnungssteuer-Anspruch (Ziff. 10):** 35 % × 2'350 = **822.50**. Das deckt sich mit den abgezogenen 87.50 + 735 (tg-form-02-2025__c0006).
> - **Vermögensverwaltungskosten (Code 148):** Pauschal 2 ‰ × 95'000 = **190** (nur K). Voraussetzung ist, dass die TKB das Depot verwaltet bzw. verwahrt (tg-wl-2025__c0159 ☑️).
> - **Bund:** Die Bundeswegleitung nennt nur die effektiven Depotspesen (bund-wl-2a-2025__c0056). Eine Pauschale ist im Wiki nicht belegt. Deshalb steht für B **0** und der Punkt ist ⬜ offen, bis eine Depotgebührenabrechnung vorliegt.
> - Der Steuerauszug ist beizulegen, wenn die Titel nur als Total deklariert werden (tg-wl-2025__c0168).
> 
> ### 1b. Form. 7 und Form. 8 (selbstbewohntes EFH, Baujahr 1986)
> 
> **Eigenmietwert:** 20'400 abzüglich Selbstnutzungsabzug K 40 % bzw. B 20 % (tg-wl-2025__c0225).
> - K: 20'400 × 0.6 = **12'240**
> - B: 20'400 × 0.8 = **16'320**
> 
> **Unterhalt: effektiv statt Pauschale.** Die Pauschale beträgt 20 % (Gebäude über 10 Jahre alt) auf dem steuerbaren Eigenmietwert (tg-wl-2025__c0238).
> 
> | Vergleich | K | B |
> |---|---|---|
> | Pauschale 20 % | 2'448 | 3'264 |
> | Effektiv (siehe Form. 8) | **7'400** | **7'400** |
> 
> Effektiv ist günstiger, die Wahl gilt je Liegenschaft und Jahr.
> 
> **Form. 8, abziehbar (7'400):**
> 
> | Rechnung | Betrag | Begründung |
> |---|---|---|
> | Malerarbeiten, Ersatzanstrich | 6'400 | Instandhaltung (tg-wl-2025__c0227) |
> | Gebäudeversicherung | 520 | Sachversicherung der Liegenschaft (tg-wl-2025__c0227) |
> | Baumschnitt/Gartenpflege | 480 | Pflege von Bäumen und mehrjährigen Pflanzen (tg-wl-2025__c0228) |
> 
> **Nicht abziehbar:** Wintergarten-Anbau 31'000. Er ist ein Anbau/Mehrwert und gehört in die Spalte «Anlagekosten/Mehrwert» (tg-wl-2025__c0233).
> 
> Rechnungen ab 1'000 sind beizulegen: Malerarbeiten und Wintergarten, falls Letzterer im Form. 8 aufgeführt wird (tg-wl-2025__c0234).
> 
> **Nettoerfolg (Ziff. 8.1):** K 12'240 − 7'400 = **4'840**; B 16'320 − 7'400 = **8'920**.
> 
> ## 2. Abzüge
> 
> | Ziff. | Code | Position | K | B | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 11 | 290 | Schuldzinsen aus Form. 4.1 (Code 286) | 3'150 | 3'150 | Die Obergrenze (Vermögensertrag + 50'000) ist nicht erreicht. Der Hypozins gehört **nicht** in Form. 7. | tg-wl-2025__c0173 ☑️ |
> | 14 | 330 | Versicherungsprämien und Sparzinsen (Form. 5.2) | 3'500 | 2'700 | Total A5 = 6'240 + 250 = 6'490. Der Abzug ist das Minimum aus A5 und B4: K 3'500, B 2'700. | tg-form-05-2-2025__c0002 ☑️ |
> | **19** | 360 | **Total Abzüge** | **6'650** | **5'850** | | |
> 
> **Zu Ziff. 14:**
> - **Prämien:** Die 6'240 stehen in Zeile 1. Eine Prämienverbilligung gab es nicht.
> - **Sparzinsen:** Die 250 stehen in Zeile 4.
> - **Bund:** Der Ansatz 2'700 (statt 1'800) gilt, weil keine Beiträge an Säule 2/3a geleistet wurden. Er ist nicht mit dem Normalansatz kumulierbar.
> - **Nicht in Zeile 2/3:** Hausrat- und Haftpflichtversicherung gehören nicht in Form. 5.2.
> 
> **Weitere Abzüge:** Keine. Es gibt keine Säule 3a, keine PK-Einkäufe, keine Berufsauslagen und keine Drittbetreuung.
> 
> ## 3. Nettoeinkommen und Abzüge darauf
> 
> | Ziff. | Code | Position | K | B |
> |---|---|---|---|---|
> | **22** | 362 | **Nettoeinkommen** (44'800 − 6'650 bzw. 49'070 − 5'850) | **38'150** | **43'220** |
> | 23.1 | 364 | Krankheitskosten (Form. 5.1 D) | 4'632.50 | 4'379 |
> | 23.2 | 366 | Freiwillige Zuwendungen (Form. 6) | 350 | 550 |
> | **24** | 372 | **Reineinkommen** | **33'167.50** | **38'291** |
> 
> **Krankheitskosten (Form. 5.1):**
> 
> | Posten | Betrag | Fundstelle |
> |---|---|---|
> | A1 Franchise/Selbstbehalt | 1'000 | tg-form-05-1-2025__c0001 |
> | Zahnarzt (Krone) | 4'440 | |
> | Brille (ärztlich verordnet) | 1'400 | |
> | **Total A** | **6'840** | |
> | B Vergütung Zusatzversicherung | − 300 | |
> | **A − B** | **6'540** | |
> 
> - Selbstbehalt 5 % des Nettoeinkommens: K 1'907.50, B 2'161.
> - Abzug: K 6'540 − 1'907.50 = **4'632.50**; B 6'540 − 2'161 = **4'379**.
> - Die Krankenkassenprämien (6'240) sind hier nicht abziehbar, sie gehören in Ziff. 14.
> - Die Krankenkassen-Leistungsabrechnung ist beizulegen, sobald der Abzug geltend gemacht wird (tg-wl-2025__c0206).
> 
> **Spenden (Form. 6):** Krebsliga Thurgau 300 + Pro Senectute Thurgau 250 = **550**.
> - K: 550 − 200 Selbstbehalt = **350**. Die Obergrenze 8'000 gilt bei Netto ≤ 40'000, hier 38'150.
> - B: Das Total liegt über 100, daher ist der ganze Betrag abziehbar: **550** (Obergrenze 20 % × 43'220 = 8'644).
> - Belege sind erst ab 1'000 pro Zuwendung einzureichen, sonst nur auf Verlangen (tg-wl-2025__c0220).
> 
> ## 4. Sozialabzüge und steuerbares Einkommen
> 
> | Ziff. | Code | Position | K | B |
> |---|---|---|---|---|
> | 25.3 | 388 | AHV-Rentnerin bzw. verwitwet (nur Staat) | **1'000** | kein Abzug |
> | **26** | 398 | **Steuerbares Einkommen** | **32'167.50** | **38'291** |
> 
> - **Zu 25.3:** Das Reineinkommen K von 33'167.50 liegt im Bereich 32'900–33'899 der WL-Tabelle (tg-wl-2025__c0116/c0117). Das ergibt 4'200 − 200 × 16 = 1'000. Der Abzug wird **einmal** gewährt, auch wenn Rentnerin und verwitwet zusammentreffen.
> - **Entfällt:** Ziff. 25.4 (verheiratet), 25.1 und 25.2 (Kinder, Unterstützte) und 28.1/28.2 (Kinder).
> 
> ## 5. Vermögen (nur Staat)
> 
> Der Bund erhebt keine Vermögenssteuer.
> 
> | Ziff. | Code | Position | Betrag | Beleg |
> |---|---|---|---|---|
> | 30.1 | 410 | Wertschriften und Guthaben (Form. 2: 48'000 + 95'000) | 143'000 | TKB-Steuerauszug |
> | 31 | 430 | Liegenschaft, Steuerwert (Form. 7) | 410'000 | Schätzung |
> | 33 | 464 | Total Vermögenswerte | 553'000 | |
> | 34 | 466 | Schulden (Form. 4.1, Code 455: Hypothek) | 180'000 | Hypothekarbank |
> | 35 | 468 | Reinvermögen | 373'000 | |
> | 36.2 | 472 | Freibetrag alleinstehend | − 100'000 | tg-stg__par-53 ☑️ |
> | **37** | 498 | **Steuerbares Vermögen** | **273'000** | |
> 
> ## 6. Was nicht zu deklarieren bzw. nicht abziehbar ist
> 
> - **Wintergarten-Anbau 31'000:** wertvermehrend, kein Unterhalt. Er wird in Form. 8 nur in der Spalte «Anlagekosten/Mehrwert» erfasst und ist nicht abziehbar.
> - **Krankenkassenprämien 6'240:** nur über Ziff. 14 (begrenzt), nicht als Krankheitskosten.
> - **Hausratversicherung 380:** Lebenshaltungskosten, ausdrücklich nicht abziehbar (tg-wl-2025__c0227). Sie ist auch kein Liegenschaftsunterhalt.
> - **Serafe 335 und Handyrechnung:** Lebenshaltungskosten, kein Abzug (Art. 34 DBG). Für Serafe habe ich im Wiki keine eigene Beleg-Karte gefunden, die Einordnung beruht auf der allgemeinen Alltagsrechnungs-Regel.
> - **Handwerker-Rechnungen und Spendenquittungen unter 1'000:** nur auf Verlangen einreichen.
> - **Hypothekarzinsen 3'150:** nicht in Form. 7, sondern nur in Ziff. 11 (kein Doppelabzug).
> - **Ergänzungsleistungen:** keine bezogen, entfällt.
> 
> ## 7. Offene Punkte und Hinweise für die Fachperson
> 
> 1. **Vermögensverwaltung Bund (⬜ offen):** Eine Bundes-Pauschale ist im Wiki nicht belegt, B steht daher auf 0. Wenn die TKB Depotspesen ausweist, wäre dort der effektive Betrag einzusetzen.
> 2. **Vermögensverwaltung K:** Die 190 setzen voraus, dass die TKB das Depot verwahrt bzw. verwaltet. Das ist eine Annahme.
> 3. **Hypothek:** Die Schuld von 180'000 und die Zinsen von 3'150 brauchen in Form. 4.1 den Gläubiger mit genauer Adresse und den Zinssatz. Ohne diese Angaben ist der Abzug gefährdet (tg-wl-2025__c0171). Das ist ein fehlender Beleg.
> 4. **Wintergarten:** Prüfen, ob Steuerwert (410'000) und indexierter Mietwert (20'400) schon den Anbau berücksichtigen. Sonst droht eine Neuschätzung.
> 5. **Gartenpflege:** Die 480 sind nur als Baum- und Gehölzpflege abziehbar. Ist Rasen- oder Gemüsegarten enthalten, müsste ein Teil gekürzt werden.
> 6. **Spenden:** Beide Organisationen sind als steuerbefreite gemeinnützige Institutionen mit Sitz in der Schweiz zu bestätigen, z. B. über die Liste der Steuerverwaltung TG.
> 7. **Rundung:** Die Krankheitskosten ergeben 4'632.50, das Reineinkommen 33'167.50. Das Formular verlangt allenfalls ganze Franken.
> 8. **Nicht erwähnt, daher ⬜ offen:** Motorfahrzeug (30.4), Bargeld/Gold (30.2), Rückkaufswert Lebensversicherung (30.3), Vorjahresvergleich.
> 9. **Plausibilität:** Das steuerbare Einkommen B liegt um etwa 6'100 über K (38'291 gegenüber 32'167.50). Das ist erklärbar: Selbstnutzungsabzug 20 % statt 40 % (+3'840), Verwaltungskosten (+190), Versicherungsabzug (−800), Krankheitskosten (+253.50), Spenden (+200) und Ziff. 25.3 (+1'000).
> 10. **Verrechnungssteuer:** Im Steuerauszug stimmen 87.50 + 735 mit dem berechneten Anspruch von 822.50 überein.
> 
> Die fachliche Beurteilung bleibt bei der zuständigen Fachperson.
> 
> Ich bin übrigens dein neuer Assistent: Wie möchtest du mich nennen?

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


**Antwort des Agenten** (157.9 s · Tools: 38 Aufrufe read, steuerwiki__formular, read, steuerwiki__position, steuerwiki__beleg, steuerwiki__wert, steuerwiki__suche, message, steuerwiki__rechne, steuerwiki__zeige):

> Variablennamen mit Folgeverweisen und Wörter wie «max» im Namen gingen nicht; ich rechne mit Zahlen direkt.
> 
> # Ausfüllhilfe AR 2025, Ehepaar Herisau
> 
> AR hat im Formular keine Bundesspalte. Die Steuerverwaltung nimmt die Bundesabweichungen automatisch vor (ar-wl-2025__c0179). Die Bundesbeträge unten sind deshalb Kontrollwerte, einzutragen ist nur eine Zahl pro Ziffer. Ein Betrag in der Spalte «Kanton» gilt für beide, wenn nur einer steht.
> 
> Alle Werte haben den Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Hauptformular-Codes für 13.1, 13.2, 14, 16.x, 17 und 23.x sind im Wiki nicht verifiziert und deshalb leer.
> 
> ## Einkünfte
> 
> | Ziffer | Code | Position | Kanton | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb Person 1 | 85'300 | 85'300 | Nettolohn Lohnausweis Ziff. 11 (nicht Brutto) | ar-wl-2025__c0035 |
> | 1.1 | 102 | Haupterwerb Person 2 | 68'200 | 68'200 | Ziff. 11. Die Kinder- und Ausbildungszulagen sind in Ziff. 8 und damit im Nettolohn enthalten, also nicht zusätzlich erfassen (Ziff. 3.5 gilt nur für direkt von der Ausgleichskasse bezahlte Zulagen). | c0032, c0054 |
> | 4.1 | 146 | Erträge Wertschriften und Guthaben (Form. 2) | 1'410 | 1'410 | 160 Zinsen + 1'250 Bruttodividenden | ar-form-02-2025__c0007 |
> | 7 | 168 | **Total Einkünfte** | **154'910** | **154'910** | 85'300 + 68'200 + 160 + 1'250 | |
> 
> Form. 2: Die Dividenden gehören in Spalte A. Der Verrechnungssteueranspruch (Code 999) beträgt 35 % × 1'250 = **437.50**. Die Kontozinsen von 160 liegen unter Fr. 200 und gehören in Spalte B (c0136), wenn sie auf ein Konto bzw. eine Bank entfallen.
> 
> ## Abzüge
> 
> **Berufskosten (Form. 4)**
> 
> | Ziffer / Code | Person 1 Kanton | Person 1 Bund | Person 2 Kanton | Person 2 Bund |
> |---|---|---|---|---|
> | 1.1 Fahrkosten ÖV (400 / 450) | 0 | 0 | 1'260 | 1'260 |
> | 2.1 Verpflegung auswärts (458) | – | – | 2'640 | 2'640 |
> | 2.2 Verpflegung verbilligt (410) | 1'600 | 1'600 | – | – |
> | 3 Übrige Berufskosten, Pauschale (416 / 466) | 2'400 | 2'559 | 2'400 | 2'046 |
> | **Total (438 → Ziff. 10.1 / 488 → Ziff. 10.2)** | **4'000** | **4'159** | **6'300** | **5'946** |
> 
> - **Fahrkosten Person 1:** null, weil Feld F (Werkbus) angekreuzt ist.
> - **Verpflegung Person 1:** Feld G ergibt den halben Abzug von 7.50 Fr. pro Tag. 7.50 × 220 = 1'650, begrenzt auf 1'600.
> - **Verpflegung Person 2:** 15 × 176 = 2'640 (Limite 3'200). Das ist der Standardfall.
> - **Übrige Berufskosten Kanton:** 700 + 10 % des Nettolohns, höchstens 2'400. Beide Personen erreichen die Obergrenze.
> - **Übrige Berufskosten Bund:** 3 % des Nettolohns (min. 2'000, max. 4'000). Person 1: 85'300 × 3 % = 2'559. Person 2: 68'200 × 3 % = 2'046.
> - **Fundstellen:** ar-form-04-2025__c0003, ar-wl-2025__c0074, c0075, c0076.
> 
> **Übrige Abzüge**
> 
> | Ziffer | Position | Kanton | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|
> | 13.1 | Säule 3a | 12'258 | 12'258 | Person 1 7'258 (Maximum), Person 2 5'000. Je Person unter dem Maximum mit 2. Säule. | ar-wl-2025__c0003, c0083 |
> | 13.2 | PK-Einkauf | **0** | 0 | Die 4'000 stehen als Ziff. 10.2 schon im Nettolohn (82'000 − 5'740 − 4'060 − 4'000 = 68'200). Sie dürfen nicht nochmals abgezogen werden, auch nicht unter 16.6. | ar-wl-2025__c0084 |
> | 14 | Versicherungsprämien | 7'400 | 5'100 | Kanton: min(13'900 + 160 Sparzinsen; 5'400 + 2 × 1'000) = 7'400. Bund: min(14'060; 3'700 + 2 × 700) = 5'100. | ar-form-06-2025__c0002 |
> | 16.1 | Verwaltungskosten Wertschriften (Pauschale) | 114 | 114 | 3 ‰ × 38'000 | ar-wl-2025__c0003 |
> | 16.2 | Kinderbetreuung Lea (Form. 10) | 10'200 | 10'200 | 14'400 − 1'800 Mittagessen − 2'400 Betreuungsbeitrag. Die Limiten 25'000 bzw. 25'800 sind nicht erreicht. | ar-form-10-2025__c0001, ar-wl-2025__c0091 |
> | 17 | Zweiverdienerabzug | 5'200 | 14'100 | Niedrigeres Erwerbseinkommen (Person 2): Kanton 68'200 − 6'300 − 5'000 = 56'900, davon 10 % = 5'690, begrenzt auf 5'200. Bund 68'200 − 5'946 − 5'000 = 57'254, davon 50 % = 28'627, begrenzt auf 14'100. | ar-wl-2025__c0004 |
> | 18 | **Total Abzüge** | **45'472** | **51'877** | 4'000 + 6'300 + 12'258 + 7'400 + 114 + 10'200 + 5'200 bzw. 4'159 + 5'946 + 12'258 + 5'100 + 114 + 10'200 + 14'100 | |
> 
> ## Einkommensberechnung
> 
> | Ziffer | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|
> | 20 | **Nettoeinkommen** | **109'438** | **103'033** | 154'910 − Total Abzüge |
> | 21.3 (Code 550) | Spende Krebsliga | 300 | 300 | Mindestgrenze 100 erreicht, also ganzer Betrag abziehbar. Die 20 %-Limite liegt bei 21'887 bzw. 20'606. Eintrag über Form. 5 Teil A. |
> | 22 | **Reineinkommen** | **109'138** | **102'733** | Nettoeinkommen − 300 |
> | 23.2 | Kinderabzug Lea | 7'400 | 6'800 | Lea ist nach dem 31.12.2025 4 Jahre alt (vollendet am 14.03.2025). |
> | 23.3 | Kinderabzug Jonas | 11'600 | 6'800 | Jonas ist 16 und in Ausbildung. |
> | 24 | Verheiratetenabzug | – | 2'800 | Nur Bund (Art. 35 DBG). |
> | 24 | **Steuerbares Einkommen** | **90'138** | **86'333** | Kanton 109'138 − 19'000. Bund 102'733 − 13'600 − 2'800. |
> 
> Beim Bund kommt in der Steuerberechnung noch eine Ermässigung des Steuerbetrags von 2 × 263 = 526 dazu (c art-36-t4). Sie wird automatisch berücksichtigt.
> 
> ## Vermögen (nur Kanton)
> 
> | Ziffer | Position | Betrag | Rechenweg |
> |---|---|---|---|
> | 30.1 (Code 300) | Wertschriften und Guthaben | 92'000 | 54'000 Konten + 38'000 Aktien |
> | 33 / 35 | Total Vermögenswerte / Reinvermögen | 92'000 | Keine Schulden (34.1 = 0) |
> | 36.2 (332) | Sozialabzug Ehepaar | 150'000 | |
> | 36.3 (334) | Sozialabzug Kinder | 50'000 | 2 × 25'000. Jonas ist minderjährig und hat einen Kinderabzug. |
> | 37 | **Steuerbares Vermögen** | **0** | 92'000 − 200'000, nicht unter null |
> 
> Der Sozialabzug übersteigt das Vermögen. Wie der Überhang behandelt wird, habe ich nicht geprüft.
> 
> ## Nicht zu deklarieren bzw. nicht abziehbar
> 
> - **PK-Einkauf 4'000:** schon im Nettolohn, kein Abzug unter 13.2 oder 16.6.
> - **Kita-Mittagessen 1'800:** Lebenshaltungskosten, nicht abziehbar (c0091).
> - **Kantonaler Betreuungsbeitrag 2'400:** nicht als Einkommen erfassen, er reduziert nur die Betreuungskosten in Form. 10.
> - **Turnverein 120:** Mitgliederbeiträge sind nicht abzugsfähig (21.3 gilt nur für uneigennützige Zuwendungen, c0102). 16.3 betrifft nur politische Parteien.
> - **Handy-Abo 960:** privat. Berufliche Nutzung ist mit der Pauschale für übrige Berufskosten (Form. 4 Ziff. 3) abgegolten.
> - **Steuern 2024 (9'870):** Steuern sind nicht abziehbar. Eine eigene Fundstelle dazu habe ich im Wiki nicht gefunden (allgemeine Regel).
> - **Kinderzulagen von Person 2:** keine separate Deklaration unter 3.5.
> - **Werkbus und Kantine Person 1:** Fahrkosten null, Verpflegung nur der halbe Abzug.
> - **Kontozinsen 160:** deklarieren, auch ohne Verrechnungssteuerabzug.
> 
> ## Hinweise für die Fachperson
> 
> 1. **Verpflegung Person 2 (2'640):** Die Arbeit in St. Gallen und die Heimkehr über Mittag sind nicht belegt. Ist die Heimkehr zumutbar, fällt Ziff. 2.1 weg. Dann sind die Berufskosten 3'660 (Kanton) bzw. 3'306 (Bund). Das Total Abzüge und der Zweiverdienerabzug bleiben wegen der Obergrenzen gleich. Rückfrage an den Mandanten nötig.
> 2. **Ziff. 2.3 (Schichtarbeit):** «Tagesschicht» erfüllt sie nicht ohne weiteres. Sie bräuchte durchgehend mindestens 8 Stunden und eine Bescheinigung im Lohnausweis Ziff. 15. 2.1 und 2.3 sind nicht kumulierbar, der Betrag wäre gleich.
> 3. **Verwaltungskostenpauschale:** Ich habe nur die Aktien als Basis genommen (114). Zählen die Konten mit, wären es 3 ‰ × 92'000 = 276. Die Basis ist im Wiki nicht eindeutig. Für den Bund habe ich keine eigene Quelle geprüft.
> 4. **Krankheitskosten (21.1):** Es sind keine Selbstbehalte oder Franchisen belegt. Falls es welche gibt, nachfordern. Zahnarzt oder Brille gehören auch dazu.
> 5. **Bund Berufskostenpauschale Person 2:** Bei Teilzeit kann sie gekürzt werden (Wiki: «angemessen kürzen»). Die Mindestgrenze 2'000 wird mit 2'046 knapp überschritten, ich habe nichts gekürzt.
> 6. **Zu bestätigen:**
>    - Die Krebsliga ist steuerbefreit.
>    - Jonas hat keine eigenen Einkünfte über 18'000 und kein Reinvermögen über 250'000.
>    - Person 1 hat kein Velo oder Motorrad für den Arbeitsweg.
> 7. **Belege beilegen:** Lohnausweise (immer), 3a-Bescheinigungen (immer), Steuerauszug bei Übertrag ins Form. 2. Krankenkasse, ÖV-Abo, Kita, Spende und Vereinsbeitrag nur auf Verlangen.
> 
> Nebenbei: Ich bin hier neu eingerichtet. Wie möchtest du mich nennen?

