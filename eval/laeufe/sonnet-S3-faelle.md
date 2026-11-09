# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 18:23
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


**Antwort des Agenten** (165.2 s · Tools: 28 Aufrufe read, steuerwiki__formular, read, steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__beleg, steuerwiki__ablage, steuerwiki__rechne, message):

> **ZH · Steuerjahr 2025 – Ausfüllhilfe Ehepaar Marco und Sandra (Winterthur)**
> Formular: StA Form. 300 mit Hilfsblättern 340, 360, 365. Alle Werte aus dem Wiki sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Beträge in ganzen Franken, alle Rechnungen mit `rechne` geprüft. «K» steht für Staatssteuer, «B» für Bundessteuer. Gilt der Betrag für beide Spalten, steht «K = B».
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | K | B | Beleg / Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 P1 | 100 | Haupterwerb Marco | 103'000 | 103'000 | Lohnausweis Ziff. 11. Kontrolle: 118'400 − 8'110 − 7'290 = 103'000 | zh-form-300-2025__c0004 |
> | 1.1 P2 | 101 | Haupterwerb Sandra | 67'200 | 67'200 | Lohnausweis Ziff. 11. Kontrolle: 76'800 − 5'260 − 4'340 = 67'200. Die Kinderzulagen (4'800) sind im Lohn enthalten, nicht nochmals unter 3.4 erfassen. | zh-form-300-2025__c0004, zh-wl-2025__c0055 |
> | 4.1 | 150 | Ertrag Wertschriften und Guthaben | 1'140 | 1'140 | Form. 340, siehe unten | zh-form-340-2025__c0005 |
> | **7** | **199** | **Total Einkünfte** | **171'340** | **171'340** | 103'000 + 67'200 + 1'140 | |
> 
> **Form. 340 (Wertschriftenverzeichnis):**
> - **Kolonne A:** Dividenden 960 (Verrechnungssteuer abgezogen).
> - **Kolonne B:** Zins Sparkonto 180. Der Zins liegt unter CHF 200 und ohne Abzug, deshalb Kolonne B. Privatkonto 0.
> - **Verrechnungssteueranspruch (Code 540):** 35 % × 960 = **336**. Das entspricht dem Steuerauszug. Mit Steuerauszug und IBAN beantragen.
> - **Totale:** Total A + B = 1'140 (Code 150). Total Steuerwert = 82'000 (Code 400).
> 
> ## 2. Abzüge
> 
> **Form. 360 Berufsauslagen** (K = B, ausser beim Fahrkosten-Plafond)
> 
> | Ziff. Form. 360 | Marco (Code) | K | B | Sandra (Code) | K = B |
> |---|---|---|---|---|---|
> | 1.1 ÖV-Abo | 201 | 4'180 | 4'180 | – | – |
> | 1.2 Velo-Pauschale | – | – | – | 222 | 700 |
> | Zwischentotal Fahrkosten | 205 | 4'180 | **3'300** (Plafond Bund) | 225 | 700 |
> | 2.1 Verpflegung | 208 (voll): min(220 × 15; 3'200) | 3'200 | 3'200 | 226 (verbilligt, Feld G): 176 × 7.50 | 1'320 |
> | 3 Übrige Berufskosten, 3 % vom Nettolohn | 212: 3 % × 103'000 | 3'090 | 3'090 | 232: 3 % × 67'200 (über Minimum 2'000) | 2'016 |
> | **6 Total** | **220** | **10'470** | **9'590** | **240** | **4'036** |
> 
> - **Marco, Feld F:** nicht angekreuzt, also ist der Fahrkostenabzug zulässig.
> - **Sandra, Velo:** Die Pauschale 700 gilt ohne Beleg, aber nur bei ständiger Benützung.
> - **Fundstellen:** zh-form-360-2025__c0001, c0003, c0004; zh-wl-2025__c0062, c0066, c0069.
> 
> **Hauptformular**
> 
> | Ziff. | Code | Position | K | B | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 11.1 | 220 | Berufsauslagen Marco | 10'470 | 9'590 | Übertrag Form. 360 | zh-form-300-2025__c0007 |
> | 11.2 | 240 | Berufsauslagen Sandra | 4'036 | 4'036 | Übertrag Form. 360 | zh-form-300-2025__c0007 |
> | 14.1 | 260 / eff. 262 | Säule 3a Marco | 7'258 | 7'258 | min(7'258; 7'258). Mit 2. Säule gilt der kleine Höchstbetrag. | zh-wl-2025__c0081 |
> | 14.2 | 261 / eff. 263 | Säule 3a Sandra | 7'258 | 7'258 | wie oben | zh-wl-2025__c0081 |
> | 15 | 270 | Versicherungsprämien und Sparzinsen | 8'400 | 5'100 | Form. 365, siehe unten | zh-form-365-2025__c0001, c0002 |
> | 16.1 | 280 | PK-Einkauf Marco | 10'000 | 10'000 | Bescheinigung Einkauf. Lohnausweis Ziff. 10.2 = 0, also keine Doppelerfassung. | zh-wl-2025__c0092 |
> | 16.3 | 283 | Vermögensverwaltung (Depot) | 94 | 0 | K: 3 ‰ × 31'200 = 93.60. B: siehe Hinweis Fachperson. Nur das Depot zählt, nicht die Bankguthaben. | zh-wl-2025__c0095 |
> | 16.6 | 376 | Fremdbetreute Kinder | 31'900 | 32'700 | Lena: K min(27'300; 25'000), B min(27'300; 25'800). Noah: 6'900. K = 25'000 + 6'900, B = 25'800 + 6'900. | zh-stg-2025__par-31-t4 |
> | 17 | 290 | Zweiverdienerabzug | 6'100 | 14'100 | Basis = Sandra: 67'200 − 4'036 − 7'258 = 55'906. K: min(55'906; 6'100). B: min(max(50 %; 8'600); 14'100) = 14'100. | zh-wl-2025__c0112 |
> | **18** | **299** | **Total Abzüge** | **85'516** | **90'042** | Summe der Zeilen oben | |
> 
> **Form. 365 (Versicherungsabzug):**
> - **Teil A (bezahlte Prämien):** Ziff. 1 Code 601 Krankenkasse 15'840 plus Ziff. 4 Code 604 Zinsen Sparkapital 180 ergibt 16'020 (Code 607). Keine Prämienverbilligung, also Code 605 = 0, Total A (Code 606) = 16'020.
> - **Teil B (Maximalabzug):** Verheiratet mit Beiträgen an 2. Säule und 3a (Code 611): K 5'800, B 3'700. Zuschlag 2 Kinder (Code 613–615): K 2 × 1'300 = 2'600, B 2 × 700 = 1'400. Maximum K 8'400, B 5'100.
> - **Teil C (Code 270):** Abzug = der niedrigere Betrag von A und B, also K 8'400 und B 5'100. Die Prämien von 16'020 liegen darüber, die Maximalbeträge greifen.
> - Hausrat und Haftpflicht gehören nicht dazu (siehe Abschnitt 5).
> 
> **Nicht zutreffend (leer lassen):** Ziff. 1.2 Nebenerwerb, 2 Selbständigkeit, 3 Renten und Taggelder, 4.2 qualifizierte Beteiligungen, 5 weitere Einkünfte, 6 Liegenschaften (Mieter), 12 Schuldzinsen, 13 Unterhaltsbeiträge, 16.2 Weiterbildung, 16.4 behinderungsbedingte Kosten, 16.5 Parteispenden.
> 
> ## 3. Einkommensberechnung und Sozialabzüge
> 
> | Ziff. | Code | Position | K | B | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 19 / 20 | 199 / 299 | Total Einkünfte / Total Abzüge | 171'340 / 85'516 | 171'340 / 90'042 | Übertrag | |
> | **21** | **310** | **Nettoeinkommen** | **85'824** | **81'298** | 171'340 − Abzüge | |
> | 22.1 | 320 | Krankheitskosten | **0** | **0** | Siehe unten | zh-form-370__c0004 |
> | 22.2 | 324 | Gemeinnützige Zuwendungen | 650 | 650 | 400 + 250. Mindestens 100 erreicht, Maximum 20 % × 85'824 = 17'164. Bund gleiche Regel. | zh-wl-2025__c0122 |
> | **23** | **350** | **Reineinkommen** | **85'174** | **80'648** | Nettoeinkommen − 650 | |
> | 24.1 | 370 | Kinder im Haushalt (2) | 18'600 | 13'600 | 2 × 9'300 bzw. 2 × 6'800. Keine Altersstaffel in ZH. | zh-wl-2025__c0126 |
> | 24.3 | 365 | Ehegatten (nur Bund) | – | 2'800 | Nur Bundesspalte ausfüllen. | zh-wl-2025__c0135 |
> | **25 / 27** | **390 / 398** | **Steuerbares Einkommen** | **66'574** | **64'248** | K: 85'174 − 18'600. B: 80'648 − 13'600 − 2'800. | |
> 
> - **22.1 Krankheitskosten:** Zahnarzt 1'850 plus Franchise und Selbstbehalt 1'240 ergibt 3'090. Der Selbstbehalt beträgt 5 % des Nettoeinkommens, also K 4'291 und B 4'065. Die Kosten liegen darunter, es gibt keinen Abzug. Form. 370 ist nicht nötig.
> - **Plausibilität K/B:** Das Bundeseinkommen liegt unter dem kantonalen, weil beim Bund der Zweiverdienerabzug (+8'000), die Betreuungskosten (+800) und der Verheiratetenabzug (+2'800) höher ausfallen. Dagegen wirken Fahrkosten-Plafond (−880), Versicherung (−3'300) und Kinderabzug (−5'000). Das ist nachvollziehbar.
> 
> ## 4. Vermögen (nur Staat)
> 
> | Ziff. | Code | Position | Betrag | Rechenweg |
> |---|---|---|---|---|
> | 30.1 | 400 | Wertschriften und Guthaben | 82'000 | Sparkonto 42'500 + Privatkonto 8'300 + Depot 31'200 |
> | 33 | 460 | Total Vermögenswerte | 82'000 | |
> | 34 | 470 | Schulden | 0 | |
> | 35 / 37 | 490 / 498 | Steuerbares Vermögen | 82'000 | 82'000 − 0 |
> 
> Das volle Vermögen eintragen, im Formular gibt es keinen Freibetrag. Der Tarif sieht für Verheiratete 0 ‰ auf den ersten 159'000 vor (zh-stg-2025__par-47-t2). Bei 82'000 fällt voraussichtlich keine Vermögenssteuer an. Beim Bund gibt es keine Vermögenssteuer. Alle übrigen Vermögenspositionen (Bargeld, Motorfahrzeuge usw.) sind leer, solange nichts vorhanden ist.
> 
> ## 5. Nicht zu deklarieren oder kein Abzug
> 
> - **Swisscom-Handyrechnungen (1'080):** private Lebenshaltungskosten, nicht abziehbar (Art. 34 lit. a DBG, bund-dbg-2025__art-34). Keine Steuerbeleg-Kategorie.
> - **Hausrat- und Privathaftpflichtversicherung (465):** gehört nicht zu den abzugsfähigen Versicherungsprämien, nicht im Form. 365 erfassen.
> - **Pensionskasse und Säule 3a:** Guthaben sind bis zur Fälligkeit kein Vermögen, nicht aufführen (zh-wl-2025__c0154).
> - **Lohnausweis Ziff. 9 und 10.1** (AHV und BVG): bereits im Nettolohn abgezogen, kein separater Abzug.
> - **Kinderzulagen im Lohnausweis (4'800):** nicht zusätzlich unter Ziff. 3.4 erfassen.
> - **Kita-Verpflegung (von den Eltern mitgegeben):** nicht abziehbar. Die Verpflegung ist in der Kita-Rechnung nicht enthalten.
> - **Krankheitskosten (3'090):** kein Abzug, weil unter dem Selbstbehalt (siehe Abschnitt 3).
> - **Verrechnungssteuer 336:** kein Abzug, sondern ein Rückerstattungsanspruch (Code 540).
> - **Bund, Abzug vom Steuerbetrag für Kinder** (2 × 263 = 526, bund-dbg-2025__art-36-t4): wird bei der Steuerberechnung berücksichtigt, im Formular nichts eintragen.
> - **Vermögensfreibetrag 159'000:** Tarifwirkung, kein Formularfeld.
> 
> ## 6. Annahmen, offene Punkte und Hinweise für die Fachperson
> 
> 1. **Sandra, Verpflegung (1'320, Code 226):** Arbeitsort und Wohnort sind beide Winterthur. Der Abzug gilt nur, wenn die Heimkehr über Mittag nicht möglich ist. Ich habe den Standardfall erfasst, weil Feld G angekreuzt ist und sie im Personalrestaurant isst. Rückfrage: Geht sie über Mittag manchmal oder regelmässig nach Hause? Falls ja, entfällt der Abzug (−1'320 bei den Berufsauslagen). Das ändert den Zweiverdienerabzug nicht, weil dieser auf den Höchstbetrag begrenzt bleibt.
> 2. **Noah, Hort (6'900):** Die Verpflegung ist nicht abziehbar. Rückfrage: Enthält die Rechnung einen Mittagstisch-Anteil? Dieser Anteil ist von 16.6 zu kürzen. Bei Lena ist die Rechnung als «reine Betreuung» bestätigt. Ausserdem wird eine Aufstellung der Betreuungskosten mit Empfängern unaufgefordert beigelegt (zh-zstb-34-1-bis-2025__c0023).
> 3. **Marco, Verpflegung (208):** 220 Tage × 15 = 3'300 wird auf 3'200 begrenzt. Das setzt voraus, dass er in Zug nicht über Mittag heimkehren kann. Das ist bei Winterthur–Zug plausibel.
> 4. **16.3 Verwaltungskosten, Bundesspalte:** Im Wiki ist für den Bund nur der effektive Depotgebührenabzug belegt, keine Pauschale. Ohne Gebührenausweis habe ich B = 0 gesetzt. Setzt man die Kantonspauschale mit Vorbehalt auch beim Bund an, ergäben sich 94 mehr Abzug und etwas tieferes Bundeseinkommen. Das ist ein Ermessensentscheid der Fachperson. Mit Gebührenbeleg wäre der höhere effektive Betrag möglich.
> 5. **PK-Einkauf (10'000, Code 280):** Der Abzug setzt voraus, dass der Einkauf im Rahmen des Einkaufspotenzials liegt (Bescheinigung der PK). Nach Auskunft gab es in den letzten drei Jahren keine Kapitalbezüge. Ein Kapitalbezug innert drei Jahren nach dem Einkauf würde den Abzug gefährden (zh-wl-2025__c0092).
> 6. **Sparzins in Form. 365 Ziff. 4 (Code 604):** Ich habe 180 eingesetzt. Auf das Ergebnis hat das keinen Einfluss, weil der Maximalabzug greift.
> 7. **Bund, übrige Berufskosten bei Teilzeit (Sandra):** Das Wiki weist darauf hin, dass der Bund die Pauschale bei Teilzeit angemessen kürzt. Ich habe 3 % von 67'200 = 2'016 eingesetzt. Bitte prüfen, ob beim Bund eine Kürzung vorgenommen wird.
> 8. **Vorjahresvergleich:** Es lag keine Vorjahreserklärung vor, der Vermögensvergleich ist nicht möglich.
> 9. **Rückfrage zum Vermögen:** Besitzt der Haushalt Motorfahrzeuge, Bargeld, Lebensversicherungen mit Rückkaufswert oder Schulden? Nichts davon ist in den Belegen enthalten.
> 10. **Beilagen:** Beide Lohnausweise, Form. 360 für beide, Form. 365, Form. 340 mit Steuerauszug ZKB, Bescheinigungen Säule 3a, Bescheinigung PK-Einkauf, Aufstellung Drittbetreuung und Spendenliste. Spendenbelege und Kita-Rechnungen erst auf Verlangen.
> 11. **Spenden:** Das Wiki verlangt, dass die Empfänger im ZH-Verzeichnis der steuerbefreiten Institutionen stehen. SRK und UNICEF Schweiz und Liechtenstein haben Sitz in der Schweiz. Das Verzeichnis habe ich nicht abgefragt.
> 
> Die fachliche Beurteilung und die Abnahme bleiben bei der Fachperson.

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


**Antwort des Agenten** (128.6 s · Tools: 30 Aufrufe read, steuerwiki__formular, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__wert, steuerwiki__rechne):

> Ich rechne jetzt alle Positionen nach und prüfe noch zwei Fundstellen (Auto-Fixkosten, Handy).
> 
> **Nadine (Mandantin) · Kanton SG · Steuerjahr 2025.** Formular 1 mit Hilfsblättern Form. 2, 4, 6 und 10. Das Formular hat nur eine Spalte. Die Bundeswerte setzt die Steuerbehörde automatisch um (sg-wl-2025__c0173). Die Bundesbeträge unten sind deshalb die Werte, die das Amt anwendet.
> Status überall ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen), sofern nichts anderes steht.
> 
> ## Ausfüllhilfe
> 
> ### Einkünfte
> | Ziff. | Code | Position | Kanton | Bund | Beleg / Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Nettolohn Haupterwerb | 73'000 | 73'000 | Lohnausweis Ziff. 11 (83'500 − 5'890 − 4'610). Die Kinderzulage 2'400 steckt im Bruttolohn und ist damit erfasst. Ziff. 3.5 bleibt leer. | sg-wl-2025__c0042 |
> | 4.1 | 146 | Wertschriften und Guthaben | 68 | 68 | Raiffeisen-Steuerauszug, Form. 2 Abschnitt B (Zins ≤ 200, kein VSt-Abzug) | sg-form-2-2025__c0006 |
> | 6.1 | 156 | Kinderalimente (minderjähriges Kind in Obhut) | 9'600 | 9'600 | Kontoauszüge, 12 × 800. Bei der Empfängerin steuerbar. Bei erstmaliger Zahlung Urteil/Vereinbarung beilegen, sonst Aufstellung. | sg-wl-2025__c0068, c0084 |
> | 7 | 168 | **Total Einkünfte** | **82'668** | **82'668** | 73'000 + 68 + 9'600 | |
> 
> ### Abzüge
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 10.1 | 438 | Berufskosten (Form. 4) | 13'600 | 8'690 | siehe Form. 4 unten | |
> | 13.1 | 208 | Säule 3a | 7'258 | 7'258 | Einzahlung = Maximum mit 2. Säule | sg-wl-2025__c0085 |
> | 13.2 | 218 | PK-Einkauf | 6'000 | 6'000 | Ziff. 10.2 im Lohnausweis ist 0, also ist der Einkauf nicht im Nettolohn und hier vollständig abziehbar. Die BVG-Beiträge Ziff. 10.1 (4'610) sind schon im Nettolohn und werden nicht nochmals abgezogen. | sg-wl-2025__c0086 |
> | 14 | 600 | Versicherungsprämien und Sparzinsen (Form. 6) | 4'500 | 2'500 | A = 5'280 + 1'320 + 68 − 1'800 = 4'868. B Kanton = 3'400 + 1'100 (Kind) = 4'500. B Bund = 1'800 + 700 = 2'500. Abzug = min(A; B). | sg-form-6-2025__c0002 |
> | 16.2 | 258 | Kinderbetreuung Elias (Form. 10) | 8'760 | 8'760 | 9'840 − 1'080 Mahlzeiten. Unter den Limiten von 26'700 / 25'800. | sg-wl-2025__c0092 |
> | 16.4 | 223 | Berufsorientierte Weiterbildung (Excel-Kurs) | 400 | 340 | Kanton: höherer Betrag aus Kosten (340) und Pauschale 400. Bund nur effektive Kosten. | sg-wl-2025__c0094 |
> | 18 | 230 | **Total Abzüge** | **40'518** | **33'548** | | |
> 
> Der Versicherungsabzug ist in beiden Fällen durch das Maximum begrenzt. Der Zuschlag «ohne Vorsorge» entfällt, weil 3a und 2. Säule abgezogen werden.
> 
> **Form. 4 (Berufskosten):**
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 1.3 | 404/406 | Fahrkosten Privatauto | 8'000 | 3'300 | 32 km × 2 × 220 = 14'080 km × 0.70 = 9'856, gekappt auf das Maximum. Begründung ankreuzen: kein ÖV (Arbeitsbeginn 06:00, erste Verbindung 06:40). Fahrzeugausweis bereithalten. |
> | 2.1 | – | Auswärtige Verpflegung | 3'200 | 3'200 | 220 × 15 = 3'300, gekappt auf 3'200. Volle Pauschale, weil keine Kantine und Feld G nicht angekreuzt ist (sg-wl-2025__c0078). |
> | 3.1 | 416 | Übrige Berufskosten pauschal | 2'400 | 2'190 | Kanton: min(700 + 10 % × 73'000; 2'400). Bund: min(max(3 % × 73'000; 2'000); 4'000). |
> | 6 | 438 | **Total Berufskosten** | **13'600** | **8'690** | |
> 
> ### Einkommensberechnung
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 20 | 234 | **Nettoeinkommen** | **42'150** | **49'120** | 82'668 − Abzüge |
> | 21.1 | 650 / 238 / 240 | Krankheitskosten | 2'757 | 1'144 | Vorkolonne (Code 650) = 850 + 2'750 = 3'600. Selbstbehalt Kanton 2 % × 42'150 = 843, Bund 5 % × 49'120 = 2'456. |
> | 21.3 | 244 | Spenden | 0 | 0 | 80 liegt unter dem Minimum von 100. |
> | 22 | 248 | **Reineinkommen** | **39'393** | **47'976** | |
> | 23.2 | 254 | Kinderabzug Elias (Schule ab Kindergarten) | 10'800 | 6'800 | Kindergarten zählt zur Volksschule, also nicht Ziff. 23.1 (sg-wl-2025__c0104). |
> | 24 | 268 | **Steuerbares Einkommen** | **28'593** | **41'176** | |
> 
> Ziff. 12.2 und 23.4 sind nicht relevant. Der Kinderabzug ist zulässig, weil Nadine Alimente erhält und nicht zahlt. Beim Bund kommt zusätzlich der Abzug vom Steuerbetrag von höchstens Fr. 263 pro Kind hinzu (`steuerbetrag.abzug_kind`, sg-form-32-2025__c0006). Den setzt das Amt automatisch an.
> 
> ### Vermögen
> | Ziff. | Code | Position | Betrag | Hinweis |
> |---|---|---|---|---|
> | 30.1 | 300 | Sparkonto Raiffeisen | 31'500 | Steuerauszug 31.12. |
> | 30.4 | 306 | Motorfahrzeug | ⬜ offen | Steuerwert = Anschaffungswert − 20 % pro Jahr seit Erwerb (sg-wl-2025__c0111). Anschaffungspreis und Erwerbsjahr fehlen. |
> | 33 | 322 | Total Vermögenswerte | 31'500 + Auto | |
> | 34.1 | 504 | Privatschulden | 0 | |
> | 35 | 326 | Reinvermögen | 31'500 + Auto | |
> | 36 | 330 | Sozialabzug allein 75'000 + Kind 20'000 | 95'000 | Beide Zeilen separat ausfüllen. Der Vermögensfreibetrag gilt nur im Kanton. |
> | 37 | 338 | **Steuerbares Vermögen** | **0** | Gilt, solange der Autowert unter 63'500 liegt. |
> 
> PK-Guthaben und Säule 3a sind bis zur Fälligkeit kein Vermögen und werden nicht deklariert (sg-wl-2025__c0107).
> 
> ## Nicht zu deklarieren oder nicht abziehbar
> - **Spende Caritas (80):** unter der Mindestsumme von 100 (Kanton und Bund).
> - **Motorfahrzeugsteuer (410) und Auto-Haftpflicht/Kasko (1'020):** nicht als Versicherungsabzug (Ziff. 14: Motorfahrzeug- und Haftpflichtversicherungen sind ausgeschlossen, sg-form-6-2025). Auch nicht als Berufskosten zusätzlich: Die Fahrkosten laufen über den Kilometeransatz. Dass dieser die Fixkosten ausdrücklich abdeckt, habe ich in den geprüften Quellen nicht gefunden. Es ist ein Rückschluss aus dem Kostensatz-Ansatz.
> - **Handy-Abo (720):** Privatkosten. Berufliche Nutzung ist mit der Pauschale für übrige Berufskosten (Ziff. 3.1) abgegolten. Mit Einzelnachweis müsste man auf Ziff. 3.2 wechseln und alle übrigen Kosten belegen, das lohnt sich hier nicht.
> - **Mittagessen und Mahlzeiten Kita (1'080):** Die Kita-Mahlzeiten sind nicht abziehbar (Ziff. 16.2). Das Mittagessen von Nadine ist in der Pauschale 2.1 enthalten.
> - **Krankenkassenprämien:** Sie gehören nicht in Ziff. 21.1, nur in Ziff. 14. Die IPV (1'800) ist in Form. 6 Zeile e bereits abgezogen.
> - **Kinderzulage (2'400):** nicht separat unter Ziff. 3.5 erfassen, sie ist im Lohn enthalten.
> - **Zweiverdienerabzug (Ziff. 17):** entfällt, weil Nadine nicht verheiratet ist.
> - **Verwaltungskosten Wertschriften (Ziff. 16.1):** entfällt, weil es nur ein Sparkonto gibt und kein Depot.
> - **Verrechnungssteuer:** keine, weil der Zins unter 200 liegt.
> - **Alimente (Ziff. 12.2):** Das ist die Zahlerseite. Bei Nadine kommen sie nur in Ziff. 6.1 vor.
> 
> ## Offene Punkte und Rückfragen
> 1. **Auto fehlt** (Ziff. 30.4): Anschaffungspreis und Erwerbsjahr nachliefern.
> 2. **Krankheitskosten:** Die Kostenbeteiligung 850 habe ich vollständig Nadine zugerechnet. Anteil Elias und Nadine bitte aus der Leistungsabrechnung bestätigen. Beides ist abziehbar, solange Nadine die Kosten selbst getragen hat. Der Zahnarzt 2'750 steht in Form. 6 Rückseite. Bei Verweis auf den Kassenauszug muss die detaillierte Leistungsübersicht beiliegen.
> 3. **PK-Einkauf:** Bescheinigung und Einkaufsberechnung der PK immer beilegen (Ziff. 13.2). Hinweis für die Fachperson: Nach einem Einkauf besteht eine Sperrfrist für Kapitalbezüge. Dazu habe ich keine Fundstelle geprüft.
> 4. **Fahrkosten:** Die erste öV-Verbindung ab Wohnort um 06:40 sollte mit einem Fahrplanauszug belegt werden. Ohne Beleg verlangt das Amt unter Umständen die Begründung nach. Bei einer Ablehnung würden nur die fiktiven öV-Kosten abgezogen (Form. 4 Ziff. 1.3, Beachten). Home-Office-Tage sind auszuschliessen. Die 220 Arbeitstage laut Lohnausweis passen.
> 5. **Excel-Kurs:** Die berufsorientierte Weiterbildung setzt einen ersten Abschluss auf Sek. II oder das vollendete 20. Altersjahr voraus (bei 38 Jahren erfüllt). Aufstellung mit Datum, Bezeichnung und Betrag für Ziff. 16.4 vorbereiten. Kanton 400 ist die Pauschale ohne Nachweis, der Nachweis 340 liegt darunter.
> 6. **Kinderbetreuung (Form. 10):** Mahlzeiten sind separat ausgewiesen, deshalb entfällt die Pauschalkürzung (8 Fr./Tag). Beim Bund ist Betreuung ausserhalb der Arbeitszeit nicht abziehbar. Das trifft bei 100 % Pensum eher nicht zu, ist aber bei Tagesstruktur-Rechnungen für Ferien- oder Freitage zu prüfen. Vorbehalt: Form. 10 ist im Wiki nicht hinterlegt, die Regel stammt aus der Wegleitung (sg-wl-2025__c0092).
> 7. **Kilometeransatz:** Der Ansatz 75 Rp. im StB 39 Nr. 3 gilt erst ab 2026. Für 2025 gilt 70 Rp. Das Ergebnis ändert sich nicht, weil das Maximum greift.
> 8. **Plausibilität:** Das steuerbare Einkommen Bund (41'176) liegt über dem Kanton (28'593). Die Differenz ist erklärbar durch Fahrkosten (4'700), Pauschale übrige Kosten (210), Versicherung (2'000), Kinderabzug (4'000), Selbstbehalt Krankheitskosten (Bund 5 % statt 2 %) und Weiterbildung (60).
> 
> Die fachliche Beurteilung bleibt bei der Fachperson. Ich habe die Werte mit `rechne` geprüft.

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


**Antwort des Agenten** (149.9 s · Tools: 35 Aufrufe read, steuerwiki__formular, read, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__beleg, steuerwiki__wert, steuerwiki__rechne):

> Ich prüfe noch Serafe/Handy (der Beleg-Treffer war unpassend), die Vermögensverwaltungspauschale und rechne dann alle Totale mit `rechne`.
> 
> **TG · Steuerjahr 2025** (Formular 1, Staats-, Gemeinde- und direkte Bundessteuer). Mandantin: verwitwet, alleinstehend, Rentnerin, Jg. 1955. Alle Beträge in ganzen Franken. Alle Werte stehen auf ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Die Totale sind mit `rechne` gerechnet.
> 
> ## 1. Hauptformular (Formular 1)
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Regel | Fundstelle |
> |---|---|---|---|---|---|---|
> | 3.1 | 130 | AHV-Rente | 27'000 | 27'000 | 12 × 2'250, 100 % steuerbar | wl c0076 |
> | 3.2 | 132 | PK-Rente (Bruttobetrag 10'800, Prozent 100) | 10'800 | 10'800 | 12 × 900. Rentenbeginn 2020, daher kein Übergangsrecht (80 %) | wl c0077 |
> | 4 | 150 | Wertschriften-/Zinserträge (aus Form. 2) | 2'160 | 2'350 | 250 + 2'100 = 2'350 brutto. Staat minus Verwaltungspauschale 190 | wl c0163 |
> | 6 | 175 | Zwischentotal Einkünfte | 39'960 | 40'150 | 27'000 + 10'800 + Ziff. 4 | |
> | 7 | – | Übertrag Ziff. 6 | 39'960 | 40'150 | | |
> | 8.1 | 180 | Liegenschaften, Nettoerfolg (Form. 7) | 4'840 | 8'920 | siehe Abschnitt 2 | wl c0224/c0225 |
> | 9 | 198 | **Total Einkünfte** | **44'800** | **49'070** | 39'960 + 4'840 bzw. 40'150 + 8'920 | |
> | 11 | 290 | Schuldzinsen (Form. 4.1) | 3'150 | 3'150 | Hypothekarzins 2025. Limite: Vermögensertrag + 50'000, eingehalten | wl c0173 |
> | 14 | 330 | Versicherungsprämien und Sparzinsen (Form. 5.2) | 3'500 | 2'700 | siehe Abschnitt 3 | tg-form-05-2-2025 c0002 |
> | 19 | 360 | **Total Abzüge** | **6'650** | **5'850** | 3'150 + 3'500 bzw. 3'150 + 2'700 | |
> | 20 / 21 | – | Total Einkünfte / Total Abzüge | 44'800 / 6'650 | 49'070 / 5'850 | Übertrag Ziff. 9 und 19 | |
> | 22 | 362 | **Nettoeinkommen** | **38'150** | **43'220** | | |
> | 23.1 | 364 | Krankheits- und Unfallkosten (Form. 5.1 D) | 4'632 | 4'379 | 6'540 − 5 % × Ziff. 22. Staat: 6'540 − 1'907.50 = 4'632.50, gerundet 4'632. Bund: 6'540 − 2'161 | wl c0206 |
> | 23.2 | 366 | Freiwillige Zuwendungen (Form. 6) | 350 | 550 | Staat 550 − 200 Selbstbehalt. Bund ohne Selbstbehalt, da ≥ 100. Maximum 20 % Netto bzw. 8'000, nicht erreicht | wl c0220 |
> | 23.3 | 368 | Liquidationsgewinne | – | – | nicht zutreffend | |
> | 24 | 372 | **Reineinkommen** | **33'168** | **38'291** | 38'150 − 4'632 − 350 bzw. 43'220 − 4'379 − 550 | |
> | 25.1 / 25.2 / 25.4 | 380–390 | Kinder, Unterstützte, gemeinsam Besteuerte | – | – | nicht zutreffend | |
> | 25.3 | 388 | AHV-Rentnerin / verwitwet (nur Staat) | 1'000 | kein Abzug | 4'200 − 200 × 16 volle Tausender über 16'900. Bestätigt durch die WL-Tabelle: Band 32'900–33'899 ergibt 1'000. Nur einmal, obwohl zwei Gründe (AHV und Witwe) | wl c0116/c0117 |
> | 26 | 398 | **Steuerbares Einkommen** | **32'168** | **38'291** | 33'168 − 1'000 | |
> | 30.1 | 410 | Wertschriften und Guthaben (Form. 2) | 143'000 | – | 95'000 Depot + 48'000 Sparkonto | |
> | 31 | 430 | Liegenschaften (Form. 7) | 410'000 | – | Steuerwert | wl c0239 |
> | 33 | 464 | Total Vermögenswerte | 553'000 | – | | |
> | 34 | 466 | Schulden (Form. 4.1) | 180'000 | – | Hypothek per 31.12. | |
> | 35 | 468 | Reinvermögen | 373'000 | – | 553'000 − 180'000 | |
> | 36.2 | 472 | Steuerfreier Abzug Alleinstehende | 100'000 | – | | |
> | 37 | 498 | **Steuerbares Vermögen** | **273'000** | – | 373'000 − 100'000 | |
> 
> Der Bund hat keine Vermögenssteuer, daher keine Bundesspalte beim Vermögen. Die Ziffern 1–2, 5, 10, 12–13, 15–18, 25.1/25.2/25.4, 28 und 30.2–32.6 sind nicht zutreffend. Zu 30.2–30.6 fehlen Angaben, siehe Abschnitt 5.
> 
> **Plausibilität:** Das Bundeseinkommen liegt 6'123 über dem Staatseinkommen. Das erklären der Selbstnutzungsabzug (Bund 20 % statt Staat 40 %), der fehlende Rentnerabzug 25.3 beim Bund und der höhere Versicherungsabzug beim Bund. Das ist stimmig.
> 
> ## 2. Hilfsblatt Form. 7 und 8 (Liegenschaft Frauenfeld)
> 
> | Posten | Staat | Bund | Rechenweg |
> |---|---|---|---|
> | Mietwert Selbstnutzung (indexiert) | 20'400 | 20'400 | Liegenschaftensteuerrechnung / Schätzung |
> | Selbstnutzungsabzug | −8'160 (40 %) | −4'080 (20 %) | nur am Wohnsitz dauernd selbstbewohnt (wl c0225) |
> | Steuerbarer Eigenmietwert | 12'240 | 16'320 | |
> | Unterhalt **effektiv** (Form. 8) | −7'400 | −7'400 | Maler 6'400 + Gebäudeversicherung 520 + Baumschnitt/Garten 480 |
> | **Nettoerfolg → Ziff. 8.1 (Code 180)** | **4'840** | **8'920** | |
> | Steuerwert → Ziff. 31 (Code 430) | 410'000 | | |
> 
> **Pauschale oder effektiv:** Das Gebäude (Baujahr 1986) ist älter als 10 Jahre, die Pauschale beträgt also 20 % (wl c0238). Sie wird vom steuerbaren Eigenmietwert berechnet und liegt bei 2'448 (Staat) bzw. 3'264 (Bund). Die effektiven Kosten von 7'400 sind höher, deshalb ist effektiv günstiger. Die Wahl gilt je Liegenschaft und Jahr.
> 
> **Form. 8:**
> - Die Malerarbeiten (Ersatzanstrich) sind Unterhalt. Der Einzelbetrag liegt über 1'000, die Rechnungskopie ist beizulegen (wl c0234).
> - Die Gebäudeversicherungsprämie ist als «Besitzesabgabe» abziehbar (StP 34 Nr. 1 c0014, wl c0227).
> - Baumschnitt und Pflege mehrjähriger Pflanzen und Bäume sind abziehbar (wl c0228).
> - Der Wintergarten-Anbau (31'000) ist wertvermehrend und kein Unterhalt. Er gehört in die Spalte «Anlagekosten/Mehrwert», der Abzug ist 0 (Form. 8 / wl c0234).
> 
> ## 3. Hilfsblätter Form. 2, 4.1, 5.1, 5.2, 6
> 
> **Form. 2 (Wertschriftenverzeichnis)**
> - Das Sparkonto hat Sp. 7 = 48'000. Der Bruttozins von 250 liegt über 200, gehört also in Sp. 8 (mit Verrechnungssteuer).
> - Das Depot hat Sp. 7 = 95'000 und Sp. 8 = 2'100 (CH-Dividenden).
> - Total Sp. 8 = 2'350. Ziff. 10 Verrechnungssteueranspruch: 35 % × 2'350 = 822.50. Das deckt sich mit dem Steuerauszug (87.50 + 735 = 822.50). Der Antrag setzt vollständige Deklaration voraus (wl c0167).
> - Code 148 Vermögensverwaltungskosten: Staat Pauschale min(2 ‰ × 95'000; 6'000) = 190 (wl c0159). Die Bank-Sparkonten zählen nicht zur Bemessung. Bund: 0, siehe offene Punkte.
> 
> **Form. 4.1 A (Schulden)**
> - Hypothek 180'000 (Code 455), Zinsen 3'150 (Code 286).
> - Zusammenzug: Code 466 = 180'000 und Code 290 = 3'150.
> 
> **Form. 5.1 (Krankheitskosten)**
> - A (selbst getragen): Franchise und Selbstbehalt 1'000 (A1), Zahnarzt 4'440 (A3), Brille 1'400 (Sehhilfen sind abziehbar, tg-info-faq c0025). Total A = 6'840.
> - B (Vergütungen): Zusatzversicherung für die Brille 300. Total B = 300.
> - A − B = 6'540. Davon der 5 %-Selbstbehalt auf Ziff. 22 (Staat 1'907.50, Bund 2'161) ergibt Code 364.
> 
> **Form. 5.2 (Versicherungen)**
> - Zeile 1: Krankenkasse 6'240 (keine Prämienverbilligung). Zeile 4: Sparzinsen 250. A5 = 6'490.
> - B4 Staat = 3'500 (alleinstehend). Abzug = min(6'490; 3'500) = **3'500**.
> - B4 Bund = 2'700. Der Bund erlaubt 2'700 statt 1'800, wenn keine Beiträge an Säule 2/3a geleistet wurden (StP 34 Nr. 27 Ziff. 2.2, wie in `position 14` ausgewiesen). Abzug = min(6'490; 2'700) = **2'700**.
> - Ob die Sparzinsen brutto (250) oder netto (162.50) einzusetzen sind, ist ohne Wirkung, weil A5 in beiden Fällen über dem Maximum liegt.
> 
> **Form. 6 (Zuwendungen)**
> - Krebsliga Thurgau 300 und Pro Senectute Thurgau 250, Total 550. Quittungen sind erst ab 1'000 je Zuwendung beizulegen (wl c0220).
> 
> ## 4. Nicht zu deklarieren oder nicht abziehbar
> 
> - **Hausratversicherung (380):** nicht abziehbar, auch nicht als Liegenschaftskosten. Der Hausrat selbst ist steuerfrei und nicht anzugeben (wl c0227).
> - **Serafe (335) und Handyrechnung:** private Lebenshaltungskosten, keine Formularposition. Das Wiki hat dazu keinen ausdrücklichen Treffer. Die Einordnung als Lebenshaltung ist meine Beurteilung, die Fachperson kann sie bestätigen.
> - **Krankenkassenprämien (6'240):** nicht als Krankheitskosten in Form. 5.1. Sie wirken nur im Versicherungsabzug Ziff. 14.
> - **Wintergarten (31'000):** kein Unterhaltsabzug, siehe Abschnitt 2.
> - **Hypothek-Amortisation:** nicht abziehbar (kommt in den Belegen nicht vor).
> - **Keine Angaben für die Mandantin:** Abzüge für Säule 3a, 2. Säule, Berufskosten, AHV-Beiträge Nichterwerbstätige (Ziff. 15.1) und Kinder. Es gibt keine Beiträge und keine Erwerbstätigkeit.
> - **PK-/Vorsorgeguthaben:** keine vorhanden, wären auch nicht zu deklarieren.
> 
> ## 5. Offene Punkte und Rückfragen für die Fachperson
> 
> 1. **Wintergarten-Anbau:** War er am 31.12.2025 fertig oder im Bau? Unfertige oder noch nicht geschätzte Investitionen sind beim Steuerwert angemessen zuzurechnen (Ziff. 31, wl c0239). Der Steuerwert von 410'000 und der Mietwert von 20'400 sind aus den Belegen übernommen. Ob eine Neuschätzung folgt, ist nicht geprüft.
> 2. **Verwaltungskosten Bund:** Eine Bundespauschale ist im Wiki nicht belegt, deshalb steht 0. Weist die TKB Depotgebühren aus, sind diese effektiv in der Bundesspalte abziehbar. Die Kantonspauschale beim Bund anzusetzen wäre nur mit Vorbehalt vertretbar, sie würde das Bundeseinkommen um 190 senken.
> 3. **Hypothek:** Gläubiger mit genauer Adresse und Zinssatz sind zwingend anzugeben (Form. 4.1, wl c0171). Beides fehlt in den Belegen.
> 4. **Gartenpflege (480):** Abziehbar ist nur die Pflege mehrjähriger Pflanzen und Bäume. Fallen Rasen- oder Gemüsearbeiten an, ist der Betrag zu kürzen (wl c0228). Ich habe den Betrag voll angesetzt.
> 5. **Zahnarzt (4'440):** Ich habe angenommen, dass keine Vergütung durch Kasse oder Zusatzversicherung erfolgte. Bei einer Vergütung wäre sie in B einzusetzen.
> 6. **Spenden:** Der Abzug setzt steuerbefreite gemeinnützige Institutionen mit Sitz in der Schweiz voraus. Dass Krebsliga Thurgau und Pro Senectute Thurgau anerkannt sind, habe ich nicht gegen die Liste der Steuerverwaltung geprüft.
> 7. **Rundung Selbstbehalt Staat:** 4'632.50 ist auf 4'632 gerundet. Eine andere Rundung ändert das Ergebnis um 1 Franken, das Reineinkommen bleibt im selben Abzugsband von Ziff. 25.3.
> 8. **Vermögen:** Zu Motorfahrzeugen, Bargeld und Edelmetallen (Ziff. 30.2), Lebensversicherungen mit Rückkaufswert (30.3) und übrigen Werten (30.6) fehlen Angaben. Es wurde nichts angesetzt.
> 9. **Einzureichende Beilagen:**
>    - Steuerauszug TKB: Pflicht, wenn die Titel nur als Total deklariert werden.
>    - Rechnungskopie Malerarbeiten.
>    - Belege zu den Krankheitskosten: Leistungsabrechnung der Kasse, Zahnarzt- und Brillenrechnung.
>    - Auszahlungskonto (IBAN) für die Verrechnungssteuer-Rückerstattung auf Seite 1.
> 10. **Vorjahresvergleich:** Ohne Vorjahresveranlagung nicht möglich. Steuerwert, Hypothek und Wertschriften sollten gegen 2024 abgeglichen werden.
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


**Antwort des Agenten** (155.7 s · Tools: 32 Aufrufe read, steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__wert, steuerwiki__rechne):

> Ich prüfe noch die letzten offenen Punkte (Alterstufe Lea, Vermögensfreibeträge, Bund-Werte), dann rechne ich alles durch.
> 
> # Ausfüllhilfe AR · Steuerjahr 2025 · Ehepaar Herisau (gemeinsame Veranlagung)
> 
> Das AR-Formular hat keine Bundesspalte. Die Steuerverwaltung rechnet die Bundesabweichungen automatisch (ar-wl-2025__c0179). Ich weise Kanton und Bund trotzdem getrennt aus, damit die Abweichungen sichtbar sind. In die Formularfelder kommt jeweils der Kantonswert.
> 
> Alle Status sind ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen), ausser wo anders vermerkt. Alle Beträge sind mit `rechne` gerechnet. Hauptformular-Codes für Seite 3 sind teils nicht verifiziert und stehen dann ohne Code.
> 
> ## 1. Einkünfte
> 
> | Ziffer / Code | Position | Kanton | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|
> | 1.1 · 100 | Nettolohn Person 1 | 85'300 | 85'300 | 98'000 − 6'860 − 5'840 = Lohnausweis Ziff. 11 | ar-wl-2025__c0035 |
> | 1.1 · 102 | Nettolohn Person 2 | 68'200 | 68'200 | 82'000 − 5'740 − 4'060 − 4'000 = Lohnausweis Ziff. 11 | ar-wl-2025__c0035 |
> | 4.1 · 146 | Wertschriften- und Guthabenerträge | 1'410 | 1'410 | Zinsen 160 (Spalte B, Bruttozins ≤ 200) + Dividenden 1'250 (Spalte A) | ar-form-02-2025__c0007, ar-wl-2025__c0136 |
> | **7 · 168** | **Total der Einkünfte** | **154'910** | **154'910** | 85'300 + 68'200 + 1'410 | |
> 
> - Die Kinder- und Ausbildungszulagen in Ziff. 8 von Person 2 sind steuerbar und im Nettolohn enthalten. Sie werden nicht separat erfasst, und Ziff. 3.5 bleibt leer (ar-wl-2025__c0032, c0054).
> - Der Einkauf (Ziff. 10.2, 4'000) ist im Nettolohn bereits abgezogen.
> 
> ## 2. Abzüge
> 
> ### Form. 4, Berufskosten (Hilfsblatt)
> 
> | Form. 4 | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|
> | **Person 1** | | | | |
> | 1.1 · 400 | Fahrkosten | 0 | 0 | Feld F angekreuzt (unentgeltlicher Werkbus), daher kein Abzug |
> | 2.2 · 410 | Verpflegung verbilligt (Feld G) | 1'600 | 1'600 | min(7.50 × 220 = 1'650; 1'600) |
> | 3 · 416 | Übrige Berufskosten (Pauschale) | 2'400 | 2'559 | Kanton: min(700 + 10 % × 85'300; 2'400). Bund: 3 % × 85'300 (min 2'000, max 4'000) |
> | 6 · 438 | **Total Berufskosten Person 1** | **4'000** | **4'159** | Übertrag in Ziff. 10.1 |
> | **Person 2** | | | | |
> | 1.1 · 450 | ÖV-Abo Herisau–St. Gallen | 1'260 | 1'260 | Effektive Kosten; Maximum Kanton 6'000, Bund 3'300 |
> | 2.1 · 458 | Auswärtige Verpflegung | 2'640 | 2'640 | 15 × 176 Tage (Maximum 3'200); Feld G nicht angekreuzt |
> | 3 · 466 | Übrige Berufskosten (Pauschale) | 2'400 | 2'046 | Kanton: min(700 + 10 % × 68'200; 2'400). Bund: 3 % × 68'200 (min 2'000, max 4'000) |
> | 6 · 488 | **Total Berufskosten Person 2** | **6'300** | **5'946** | Übertrag in Ziff. 10.2 |
> 
> Fundstellen: ar-form-04-2025__c0003 und c0004, ar-wl-2025__c0074 bis c0077.
> 
> - Die Fahrkosten-Pauschale und die Verpflegung kommen zusätzlich zur Pauschale für übrige Berufskosten.
> - Bund bei Teilzeit: Die Pauschale ist angemessen zu kürzen. Bei Person 2 ist 3 % × 68'200 = 2'046 auch nach einer Kürzung des Minimums auf 80 % (1'600) massgebend. Die Zahl bleibt also gleich.
> - Person 2 arbeitet in Tagesschicht, daher gilt Ziff. 2.3 (Schichtarbeit) nicht.
> 
> ### Hauptformular
> 
> | Ziffer / Code | Position | Kanton | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|
> | 10.1 · 438 | Berufskosten Person 1 | 4'000 | 4'159 | Form. 4 Ziff. 6 | ar-form-04-2025__c0004 |
> | 10.2 · 488 | Berufskosten Person 2 | 6'300 | 5'946 | Form. 4 Ziff. 6 | ar-form-04-2025__c0008 |
> | 13.1 | Säule 3a (Person 1 + Person 2) | 12'258 | 12'258 | 7'258 + 5'000, je ≤ 7'258 (mit 2. Säule). Bescheinigungen beilegen. | ar-wl-2025__c0003 |
> | 13.2 | PK-Einkauf Person 2 | 0 | 0 | Bereits im Nettolohn abgezogen (Ziff. 10.2 Lohnausweis, «via Lohnabzug»). Nicht doppelt abziehen. | ⚠️ siehe Hinweise |
> | 14 · 600 | Versicherungsprämien und Sparzinsen | 7'400 | 5'100 | A = 13'900 + 160 = 14'060, keine Prämienverbilligung. B Kanton: 5'400 + 2 × 1'000. B Bund: 3'700 + 2 × 700. Abzug = min(A; B). | ar-form-06-2025__c0002 |
> | 16.1 | Verwaltungskosten Wertschriften | 276 | 0 | Kanton: Pauschale auf Antrag, 3 ‰ × 92'000 (Konten 54'000 + Aktien 38'000). Bund: nur effektive Verwahrungskosten, kein Beleg vorhanden. | ar-wl-2025__c0003, c0089, bund-wl-2a-2025__c0056 |
> | 16.2 | Kinderbetreuung Lea (Form. 10) | 10'200 | 10'200 | 14'400 − 1'800 (Mittagessen) − 2'400 (Betreuungsbeitrag). Maximum 25'000 (Kanton) bzw. 25'800 (Bund). | ar-form-10-2025__c0001 |
> | 17 | Zweiverdienerabzug | 5'200 | 14'100 | Kanton: niedrigeres Erwerbseinkommen E2 = 68'200 − 6'300 − 5'000 = 56'900, 10 % = 5'690, Maximum 5'200. Bund: E2 = 68'200 − 5'946 − 5'000 = 57'254, 50 % = 28'627, Maximum 14'100. | ar-wl-2025__c0004 |
> | **18** | **Total der Abzüge** | **45'634** | **51'763** | | |
> | **20** | **Nettoeinkommen** | **109'276** | **103'147** | 154'910 − Abzüge | |
> 
> - Kinderbetreuung Ziff. 16.2 bei Jonas: keine, er ist über 14 Jahre alt.
> - Die Kita-Rechnungen sind auf Verlangen vorzulegen. Der Empfänger muss ersichtlich sein.
> 
> ### Nach dem Nettoeinkommen
> 
> | Ziffer / Code | Position | Kanton | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|
> | 21.3 · 550 | Spende Krebsliga Ostschweiz (Form. 5 S. 2 Teil A) | 300 | 300 | Total ≥ 100 (Freigrenze), daher voll abziehbar. Maximum 20 % × Nettoeinkommen = 21'855 (Kanton) bzw. 20'629 (Bund). | ar-form-05-2025__c0003, bund-dbg-2025__art-33a |
> | 21.1 | Krankheitskosten | – | – | Keine Belege vorhanden | |
> | **22** | **Reineinkommen** | **108'976** | **102'847** | | |
> 
> Voraussetzung für den Spendenabzug: Die Krebsliga muss als steuerbefreite Institution anerkannt sein. Auf der Quittung prüfen.
> 
> ### Sozialabzüge
> 
> | Ziffer | Position | Kanton | Bund | Fundstelle |
> |---|---|---|---|---|
> | 23.2 | Lea, geb. 14.03.2021 (4. Altersjahr vollendet am 14.03.2025) | 7'400 | 6'800 | ar-wl-2025__c0005 |
> | 23.3 | Jonas, geb. 02.09.2009, 16 Jahre, Ausbildung | 11'600 | 6'800 | ar-wl-2025__c0005 |
> | 24 | Verheiratetenabzug | – | 2'800 | Abzug nur Bund |
> | **24** | **Steuerbares Einkommen** | **89'976** | **86'447** | 108'976 − 19'000 bzw. 102'847 − 16'400 |
> 
> Zusätzlich gilt beim Bund ein Abzug vom Steuerbetrag von 263 je Kind (2 × 263 = 526). Er wird automatisch vorgenommen und nicht im Formular erfasst.
> 
> ## 3. Vermögen (nur Kanton)
> 
> | Ziffer / Code | Position | Betrag | Beleg / Rechenweg |
> |---|---|---|---|
> | 30.1 · 300 | Wertschriften und Guthaben (Übertrag Form. 2) | 92'000 | 54'000 + 38'000 |
> | 33 · 322 | Total Vermögenswerte | 92'000 | |
> | 34.1 · 504 | Privatschulden | 0 | |
> | 35 · 326 | Reinvermögen | 92'000 | |
> | 36.2 · 332 | Sozialabzug Ehepaar | 150'000 | |
> | 36.3 · 334 | Sozialabzug 2 minderjährige Kinder | 50'000 | 2 × 25'000 (Lea und Jonas) |
> | 37 · 338 | Steuerbares Vermögen | 0 | Die Sozialabzüge (200'000) übersteigen das Reinvermögen. |
> 
> Die Ziffern 36.2 und 36.3 sind trotz steuerbarem Vermögen 0 auszufüllen.
> 
> ## 4. Form. 2, Wertschriftenverzeichnis
> 
> - **Spalte A (mit VSt):** Dividenden Schweizer Aktien, Steuerwert 38'000, Bruttoertrag 1'250.
> - **Spalte B (ohne VSt):** Konten, Steuerwert 54'000, Bruttozins 160 (≤ 200 je Jahr).
> - **Verrechnungssteueranspruch (Code 999):** 35 % × 1'250 = 437.50. Das Formular verlangt hier Franken und Rappen.
> - **Ziff. 4.1:** 1'410. **Ziff. 30.1:** 92'000.
> - Den Steuerauszug vollständig beilegen. Die Sparzinsen 160 gehören auch in Form. 6, Teil A d.
> 
> ## 5. Nicht zu deklarieren bzw. nicht abziehbar
> 
> - **Steuerschlussrechnung 2024 (9'870):** nicht abziehbar, keine Formularposition. Fundstelle dazu habe ich nicht geprüft.
> - **Handy-Abo (960):** kein eigener Abzug. Es fällt unter die Pauschale für übrige Berufskosten (Form. 4 Ziff. 3). Pauschale und effektive Kosten gehen nicht kumuliert.
> - **Mitgliederbeitrag Turnverein (120):** nicht abziehbar, Mitgliederbeiträge zählen nicht als Zuwendung (Ziff. 21.3, ar-form-05-2025__c0003).
> - **Kita Mittagessen (1'800):** nicht abziehbar, Verpflegung ist von Ziff. 16.2 ausgeschlossen.
> - **BVG-Einkauf 4'000 (Person 2) in Ziff. 13.2:** nicht nochmals erfassen, bereits im Nettolohn.
> - **Fahrkosten Person 1:** nichts deklarieren, Feld F.
> - **Pensionskassen- und Säule-3a-Guthaben:** kein steuerbares Vermögen, nicht deklarieren (ar-wl-2025__c0111).
> - **Zulagen in Ziff. 8 von Person 2:** nicht separat deklarieren, im Nettolohn enthalten.
> 
> ## 6. Annahmen und Hinweise für die Fachperson
> 
> 1. **Verpflegung Person 2 (2'640):** Ich habe den Standardfall erfasst: Heimkehr zum Mittagessen nicht möglich, 176 Tage. Wenn sie über Mittag nach Hause fahren kann, entfallen oder reduzieren sich die Mehrkosten (ar-wl-2025__c0076). **Rückfrage:** Ist die Mittagspause zu kurz für die Heimfahrt Herisau–St. Gallen? Die Fahrkosten 1'260 bleiben davon unberührt.
> 2. **Ziff. 13.2:** Dieser Wiki-Eintrag ist ⚠️ strittig, weil die Wegleitung widersprüchlich ist (13.2 oder 16.6). Hier betrifft es nur die Doppelerfassung: Weil der Einkauf im Nettolohn steckt, kommt kein Betrag in 13.2 oder 16.6. Die PK-Bestätigung (4'000) kann trotzdem beigelegt werden.
> 3. **Verwaltungskosten 276:** Ich habe die Pauschale angesetzt, weil keine Gebührenbelege vorliegen. Sie muss beantragt werden. Wenn die effektiven Depot- und Safegebühren höher sind, diese verwenden. Beim Bund ist nur der effektive Betrag belegt.
> 4. **Alterstufe Lea:** Ich lese «nach Vollendung des 4. Altersjahrs» als Stand 31.12.2025. Lea ist am 14.03.2025 vier geworden, daher gilt 23.2 (7'400) statt 23.1 (5'300).
> 5. **Betreuungsbeitrag 2'400:** Ich habe ihn als «erhaltene Beiträge» in Form. 10 abgezogen. Wenn die Kita-Rechnung die Beiträge bereits berücksichtigt, wäre der Abzug 12'600. Bitte prüfen.
> 6. **Fahrzeuge (Ziff. 30.4):** In den Belegen ist kein Motorfahrzeug genannt. **Rückfrage:** Besitzt der Haushalt eines? Ein Fahrzeug wäre beim Vermögen zu deklarieren.
> 7. **Fehlende Belege:** Keine Krankheitskosten, keine Schuldzinsen und kein Eigenmietwert, weil Mieter. Der Lohnausweis Ziff. 13 und 15 wurde nicht geliefert.
> 8. **Codes Hauptformular:** Seite 3 ist in der Wegleitung nicht abgebildet. Die Codes für 13.1, 14, 16.1, 17 und 24 sind unverifiziert und am Originalformular zu prüfen.
> 9. **Plausibilität:** Das steuerbare Einkommen beim Bund (86'447) liegt unter dem des Kantons (89'976). Das ist stimmig: Der Zweiverdienerabzug und der Verheiratetenabzug beim Bund sind höher, bei Versicherung und Kinderabzug ist der Bund tiefer.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

