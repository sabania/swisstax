# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 20:30
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


**Antwort des Agenten** (155.8 s · Tools: 28 Aufrufe read, steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__suche, steuerwiki__wert, message, steuerwiki__rechne):

> # Ausfüllhilfe · Kanton ZH · Steuerjahr 2025 (Form. 300 mit Hilfsblättern 340, 360, 365)
> 
> Ehepaar in Winterthur, P1 = Marco (Arbeitsort Zug), P2 = Sandra (Arbeitsort Winterthur), 2 Kinder im Haushalt. Das Formular führt zwei Spalten, Staatssteuer (K) und Bundessteuer (B). Alle Beträge sind in ganzen Franken und mit `rechne` berechnet. Status überall ☑️ (agent-geprüft, Abnahme offen), ausser wo anders vermerkt.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | K | B | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb P1 | 103'000 | 103'000 | Lohnausweis Ziff. 11 (Nettolohn, nicht Brutto 118'400) | zh-form-300-2025__c0005 |
> | 1.1 | 101 | Haupterwerb P2 | 67'200 | 67'200 | Lohnausweis Ziff. 11. Die Kinderzulagen 4'800 sind darin schon enthalten. | zh-wl-2025__c0055 |
> | 4.1 | 150 | Wertschriftenertrag (A + B) | 1'140 | 1'140 | 960 (Kolonne A) + 180 (Kolonne B) + 0 Privatkonto | zh-form-340-2025__c0005 |
> | 7 | 199 | **Total Einkünfte** | **171'340** | **171'340** | 103'000 + 67'200 + 960 + 180 | |
> 
> **Form. 340 (Wertschriftenverzeichnis):**
> - **Kolonne A (Code 2309):** Dividenden 960 brutto, mit Verrechnungssteuerabzug. Dazu der Steuerwert des Depots von 31'200.
> - **Kolonne B (Code 542):** Sparkonto-Zins 180. Er liegt unter der Grenze von 200, daher ohne Verrechnungssteuerabzug in Kolonne B. Dazu der Steuerwert von 42'500.
> - **Privatkonto:** Steuerwert 8'300, Zins 0.
> - **Verrechnungssteueranspruch (Code 540):** 35 % × 960 = 336, zu beantragen. Das ist Rückerstattung, weder Einkommen noch Abzug.
> - **Übertrag:** Total Steuerwert (Code 400) nach Ziff. 30.1, Total Ertrag (Code 150) nach Ziff. 4.1.
> 
> Nicht belegt, daher nicht eingesetzt: Kinderzulagen direkt von der Ausgleichskasse (Ziff. 3.4, Codes 142/143), Nebenerwerb, Liegenschaften.
> 
> ## 2. Berufsauslagen (Form. 360 → Ziff. 11.1 / 11.2)
> 
> | Form. 360 | Code P1 / P2 | Position | K | B | Rechenweg |
> |---|---|---|---|---|---|
> | **P1** Ziff. 1.1 | 201 | ÖV-Abo Winterthur–Zug | 4'180 | 3'300 | Plafond Kanton 5'200 / Bund 3'300. Fahrkosten-Zwischentotal Code 205. |
> | P1 Ziff. 2.1 voll | 208 | Verpflegung, Restaurant | 3'200 | 3'200 | min(220 × 15 = 3'300; 3'200). Feld G nicht angekreuzt. |
> | P1 Ziff. 3 | 212 | Übrige Berufskosten (Pauschale) | 3'090 | 3'090 | 3 % × 103'000, innerhalb min 2'000 / max 4'000 |
> | P1 Ziff. 6 → Ziff. 11.1 | 220 | **Total P1** | **10'470** | **9'590** | |
> | **P2** Ziff. 1.2 | 222 | Velo-Pauschale | 700 | 700 | ohne Beleg. Der Plafond gilt, ist aber nicht erreicht. |
> | P2 Ziff. 2.1 verbilligt | 226 | Verpflegung, Personalrestaurant | 1'320 | 1'320 | Feld G angekreuzt: min(176 × 7.50; 1'600). Kanton = Bund. |
> | P2 Ziff. 3 | 232 | Übrige Berufskosten (Pauschale) | 2'016 | 2'016 | 3 % × 67'200, über dem Minimum von 2'000 |
> | P2 Ziff. 6 → Ziff. 11.2 | 240 | **Total P2** | **4'036** | **4'036** | |
> 
> Fahrkosten und Verpflegung kommen zusätzlich zur Pauschale. Feld F ist bei beiden nicht angekreuzt, also kein Ausschluss der Fahrkosten.
> 
> Fundstellen: zh-form-360-2025__c0001, __c0002, __c0003, zh-wl-2025__c0067.
> 
> ## 3. Übrige Abzüge
> 
> | Ziff. | Code | Position | K | B | Rechenweg / Regel | Fundstelle |
> |---|---|---|---|---|---|---|
> | 14.1 | 260 (eff. 262) | Säule 3a P1 | 7'258 | 7'258 | min(7'258; 7'258). Mit 2. Säule gilt dieser Höchstbetrag. | zh-wl-2025__c0081 |
> | 14.2 | 261 (eff. 263) | Säule 3a P2 | 7'258 | 7'258 | wie P1, eigener Vertrag. Bescheinigungen (Form. 21 EDP) beilegen. | zh-wl-2025__c0081 |
> | 15 | 270 | Versicherungsprämien | 8'400 | 5'100 | siehe Form. 365 unten | zh-form-365-2025__c0001, __c0002 |
> | 16.1 | 280 | PK-Einkauf P1 | 10'000 | 10'000 | Selbst überwiesen am 14.11.2025. Lohnausweis Ziff. 10.2 ist 0, also keine Doppelerfassung. Kein Kapitalbezug in den letzten 3 Jahren, daher keine Sperrfrist. | zh-wl-2025__c0092 |
> | 16.3 | 283 | Verwaltung Wertschriften | 94 | **0** (offen, s. u.) | 3 ‰ × 31'200 = 93.60, gerundet auf 94. Basis ist nur das Depot. | zh-wl-2025__c0095 |
> | 16.6 | 376 | Fremdbetreuung Kinder | 31'900 | 32'700 | Lena: min(27'300; 25'000 K / 25'800 B). Noah: 6'900. Beide unter 14 Jahren. | zh-form-300-2025__c0008, zh-stg-2025__par-31-t4 |
> | 17 | 290 | Zweiverdienerabzug | 6'100 | 14'100 | siehe unten | zh-wl-2025__c0112 |
> | 11.1 / 11.2 | 220 / 240 | Berufsauslagen P1 + P2 | 14'506 | 13'626 | siehe Abschnitt 2 | |
> | 18 | 299 | **Total Abzüge** | **85'516** | **90'042** | Summe aller Abzüge inkl. Berufsauslagen und Zweiverdienerabzug | |
> 
> **Form. 365 (Versicherungsprämien):**
> - **Teil A:** Code 601 Krankenkasse 15'840 (Grund- und Zusatzversicherung, keine Prämienverbilligung, Code 605 = 0). Code 604 Sparzinsen 180. Total (A) Code 606 = 16'020.
> - **Teil B:** Code 611 Verheiratete mit Vorsorge 5'800 (Staat) / 3'700 (Bund), da beide Pensionskasse und 3a haben. Dazu je Kind 1'300 / 700 (Codes 613–615): 2 × 1'300 = 2'600 und 2 × 700 = 1'400. Maximum Staat 8'400, Bund 5'100.
> - **Teil C (Code 270):** das Minimum von (A) und (B), also 8'400 (K) und 5'100 (B). Die Prämien liegen deutlich über dem Maximum.
> 
> **Zweiverdienerabzug (Ziff. 17):**
> - **Basis:** das niedrigere verbleibende Erwerbseinkommen, hier P2: 67'200 − 4'036 − 7'258 = 55'906. P1 liegt bei 75'272.
> - **Kanton:** min(55'906; 6'100) = 6'100.
> - **Bund:** 50 % × 55'906 = 27'953, begrenzt auf max. 14'100, also 14'100.
> - Ob die Basis hier auf Franken genau stimmt, spielt keine Rolle, da beide Maxima weit unterschritten werden.
> 
> ## 4. Einkommensberechnung und Sozialabzüge
> 
> | Ziff. | Code | Position | K | B | Rechenweg |
> |---|---|---|---|---|---|
> | 19 | 199 | Total Einkünfte | 171'340 | 171'340 | |
> | 20 | 299 | Total Abzüge | 85'516 | 90'042 | |
> | 21 | 310 | **Nettoeinkommen** | **85'824** | **81'298** | 171'340 − Abzüge |
> | 22.1 | 320 | Krankheits- und Unfallkosten | 0 | 0 | 1'850 + 1'240 = 3'090 liegt unter dem Selbstbehalt (5 % × 85'824 = 4'291 K; 5 % × 81'298 = 4'065 B). Kein Abzug. |
> | 22.2 | 324 | Gemeinnützige Zuwendungen | 650 | 650 | 400 + 250. Über der Freigrenze von 100 und unter dem Maximum von 20 % (17'165 K; 16'260 B). Der ganze Betrag ist abziehbar. |
> | 23 | 350 | **Reineinkommen** | **85'174** | **80'648** | Netto − 650 |
> | 24.1 | 370 | Kinder im Haushalt (2) | 18'600 | 13'600 | 2 × 9'300 bzw. 2 × 6'800. Keine Altersstaffel. |
> | 24.2 | 374 | Unterstützte Personen | 0 | 0 | nicht zutreffend |
> | 24.3 | 365 | Ehegatten, nur Bund | – | 2'800 | |
> | 25 | 390 | **Steuerbares Einkommen** | **66'574** | **64'248** | 85'174 − 18'600 bzw. 80'648 − 16'400 |
> | 27 | 398 | Steuerbares Einkommen ZH / CH | 66'574 | 64'248 | keine Ausscheidung, Ziff. 26 leer |
> 
> Plausibilitätsprüfung: Das Bundeseinkommen liegt rund 2'300 unter dem Kanton. Das erklärt sich so: Der Zweiverdienerabzug ist beim Bund um 8'000 höher, ebenso der Fremdbetreuungsabzug (+800) und der Ehegattenabzug (+2'800). Dem stehen beim Bund tiefere Kinderabzüge (−5'000), ein tieferer Versicherungsabzug (−3'300), tiefere Fahrkosten (−880) und der fehlende Verwaltungskostenabzug (−94) gegenüber.
> 
> Der Kinderabzug vom Steuerbetrag beim Bund (2 × 263 = 526, Art. 36 DBG) ist kein Formularfeld. Die Steuerverwaltung rechnet ihn selbst.
> 
> ## 5. Vermögen
> 
> | Ziff. | Code | Position | Betrag | Rechenweg |
> |---|---|---|---|---|
> | 30.1 | 400 | Wertschriften und Guthaben | 82'000 | 42'500 + 8'300 + 31'200 (Übertrag Form. 340) |
> | 33 | 460 | Total Vermögenswerte | 82'000 | |
> | 34 | 470 | Schulden | 0 | |
> | 35 | 490 | Steuerbares Vermögen gesamt | 82'000 | |
> | 37 | 498 | Steuerbares Vermögen ZH | 82'000 | |
> 
> Das steuerfreie Vermögen und ein allfälliger Kinderfreibetrag wirken nur über den Tarif. ZH kennt beim Vermögen keinen Kinderabzug. Es wird nichts abgezogen.
> 
> ## 6. Nicht zu deklarieren oder nicht abziehbar
> 
> - **Swisscom-Handy (1'080), privat:** Lebenshaltungskosten. Der Formularaufbau kennt dafür keine Position. Der berufliche Anteil ist durch die Pauschale «übrige Berufskosten» abgegolten.
> - **Hausrat- und Privathaftpflichtversicherung (465):** Form. 365 sieht nur Kranken-, Unfall-, Lebens-/Rentenversicherung und Sparzinsen vor (Codes 601–604). Das Wiki belegt für Hausrat/Haftpflicht keinen Abzug. Selbst wenn sie zählten, ist das Maximum von Ziff. 15 bereits ausgeschöpft.
> - **Mietzins:** kein Abzug, keine Liegenschaft. Kein Eigenmietwert, Ziff. 6 bleibt leer.
> - **Pensionskasse- und Säule-3a-Guthaben:** bis zur Fälligkeit kein steuerbares Vermögen (zh-wl-2025__c0154).
> - **Lohnausweis-Abzüge Ziff. 9 und 10.1** (AHV 8'110 / 5'260 und BVG 7'290 / 4'340): bereits im Nettolohn, nicht nochmals abziehen.
> - **Kinderzulagen 4'800:** im Lohn enthalten, nicht zusätzlich unter Ziff. 3.4 eintragen.
> - **Verrechnungssteuer 336:** weder Einkommen noch Abzug, sie wird zurückgefordert.
> - **Krankenkassenprämien:** keine Krankheitskosten (Form. 370), sie gehören in Form. 365.
> - **Ziff. 40 Kapitalleistungen und Ziff. 50 Schenkungen/Erbschaften:** leer (keine Kapitalbezüge, keine Angaben).
> 
> ## 7. Beizulegen und aufzubewahren
> 
> - **Beilegen:** beide Lohnausweise, die zwei 3a-Bescheinigungen, die PK-Einkaufsbescheinigung, Form. 340, 360 und 365, die Spendenaufstellung, die Aufstellung der Betreuungskosten mit Empfängern.
> - **Nur auf Verlangen:** Kita- und Hort-Rechnungen, Spendenquittungen, ÖV-Abo.
> - **Bank-Steuerauszug:** nur beilegen, wenn das Wertschriftenverzeichnis darauf verweist.
> - **Form. 370 (Krankheitskosten):** nicht einreichen, da kein Abzug entsteht.
> 
> ## 8. Offene Punkte für die Fachperson
> 
> 1. **Verwaltungskosten Bund (Ziff. 16.3):** Das Wiki belegt für den Bund keine Pauschale (zh-wl-2025__c0095). Ich habe deshalb 0 eingesetzt. Wenn die Fachperson die Kantonspauschale von 94 auch für den Bund zulässt, sinkt das Bundeseinkommen um 94. Status ⬜ offen.
> 2. **Sandra, Verpflegung (Form. 360 Ziff. 2.1, Code 226):** Arbeitsort und Wohnort sind beide Winterthur, und sie fährt mit dem Velo. Ich habe den Standardfall mit Personalrestaurant angesetzt (1'320). Isst sie mittags tatsächlich zu Hause, müsste der Abzug entfallen. Das wäre eine Rückfrage an den Mandanten. Ebenso muss das Velo ständig für den Arbeitsweg benutzt werden (Pauschale 700).
> 3. **Noah, Hort/Tagesstruktur (6'900):** Enthält die Rechnung ein Mittagessen oder andere Verpflegung, ist dieser Anteil nicht abziehbar (bund-ks-30__c0044). Dann den Betrag kürzen. Bei Lenas Kita ist das ausgeschlossen, weil die Eltern die Verpflegung mitgeben.
> 4. **Spenden:** Die Steuerbefreiung von SRK und UNICEF Schweiz am Sitz ZH ist anhand der Quittungen zu prüfen. Es zählen nur Empfänger mit Sitz in der Schweiz.
> 5. **PK-Einkauf 10'000:** Ein Kapitalbezug innerhalb von drei Jahren würde den Abzug rückwirkend gefährden. Das Paar sollte das wissen.
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


**Antwort des Agenten** (162.0 s · Tools: 37 Aufrufe read, steuerwiki__formular, read, steuerwiki__position, steuerwiki__suche, steuerwiki__beleg, steuerwiki__zeige, message, steuerwiki__rechne):

> # Ausfüllhilfe SG · Steuerjahr 2025
> **Mandantin:** Nadine, alleinerziehend, 1 Kind (Elias, 5 J.). **Formular:** Steuererklärung 2025, Formular 1 mit Hilfsblättern 2, 4, 6 und 10.
> 
> Das SG-Formular hat nur eine Spalte. Die Bundesabweichungen rechnet das Steueramt automatisch (sg-wl-2025__c0173). Die Spalte «Bund» unten zeigt, was dabei herauskommt. Alle Positionen haben den Status ☑️ (Fundstelle geprüft, Abnahme offen). Alle Beträge sind mit `rechne` berechnet.
> 
> ## Einkünfte
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Nettolohn | 73'000 | 73'000 | Lohnausweis Ziff. 11, nicht Ziff. 8. Die Kinderzulage 2'400 ist darin schon enthalten. | sg-wl-2025__c0042 |
> | 4.1 | 146 | Sparzins | 68 | 68 | Form. 2, Spalte B (Bruttozins bis Fr. 200, ohne Verrechnungssteuer). Code 999 = 0. | sg-wl-2025__c0135 |
> | 6.1 | 156 | Kinderalimente | 9'600 | 9'600 | 12 × 800. In die Zeile «für minderjährige Kinder», nicht Code 154. | sg-wl-2025__c0068 |
> | **7** | **168** | **Total Einkünfte** | **82'668** | **82'668** | 73'000 + 9'600 + 68 | |
> 
> ## Abzüge
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 10.1 | 438 | Berufskosten (Total Form. 4) | 13'600 | 8'690 | siehe Detail unten | |
> | 13.1 | 208 | Säule 3a | 7'258 | 7'258 | Bescheinigung 7'258, entspricht dem Maximum mit 2. Säule | sg-wl-2025__c0085 |
> | 13.2 | 218 | PK-Einkauf | 6'000 | 6'000 | Bescheinigung, selbst bezahlt am 20.10.2025. Lohnausweis Ziff. 10.2 ist 0, also kein Doppelabzug. | sg-wl-2025__c0086 |
> | 14 | 600 | Versicherungsprämien | 4'500 | 2'500 | Form. 6, siehe Detail unten | sg-form-6-2025__c0002 |
> | 16.2 | 258 | Kinderbetreuung | 8'760 | 8'760 | Form. 10: 9'840 − 1'080 Mahlzeiten. Limite 26'700 (Kanton) bzw. 25'800 (Bund), Kind unter 14. | sg-wl-2025__c0092 |
> | 16.4 | 223 | Weiterbildung Excel-Kurs | 400 | 340 | Kanton: höherer Betrag aus Kosten (340) und Pauschale 400. Bund: nur effektive Kosten. | sg-wl-2025__c0094 |
> | **18** | **230** | **Total Abzüge** | **40'518** | **33'548** | | |
> | **20** | **234** | **Nettoeinkommen** | **42'150** | **49'120** | 82'668 − Total Abzüge | |
> 
> **Detail Ziff. 10.1 (Form. 4)**
> - **Code 404/406, Fahrkosten Privatauto:** 32 km × 2 = 64 km pro Tag × 220 Tage = 14'080 km × 0.70 = 9'856. Das Zwischentotal ist im Kanton auf 8'000 begrenzt, im Bund auf 3'300.
> - **Code 408, Verpflegung:** 15 × 220 = 3'300, begrenzt auf 3'200 (Kanton und Bund gleich). Feld G ist nicht angekreuzt, also gilt der volle Ansatz.
> - **Code 416, übrige Berufskosten (Pauschale):**
>   - Kanton: min(700 + 10 % × 73'000; 2'400) = 2'400.
>   - Bund: min(max(3 % × 73'000; 2'000); 4'000) = 2'190.
> - **Total Code 438:**
>   - Kanton: 8'000 + 3'200 + 2'400 = 13'600.
>   - Bund: 3'300 + 3'200 + 2'190 = 8'690.
> - **Fundstellen:** sg-form-4-2025__c0002 und c0003, sg-wl-2025__c0078 und c0080, sg-stb-39-3__c0004 und c0005.
> 
> **Detail Ziff. 14 (Form. 6)**
> - **A (effektiv):** 5'280 + 1'320 + Sparzins 68 − Prämienverbilligung 1'800 = 4'868.
> - **B (Maximum):**
>   - Kanton: 3'400 + 1'100 für das Kind = 4'500.
>   - Bund: 1'800 + 700 = 2'500.
> - **Abzug:** der kleinere Wert aus A und B, also 4'500 (Kanton) und 2'500 (Bund). Der Zuschlag «ohne Vorsorge» entfällt, weil Säule 3a und PK abgezogen werden.
> 
> ## Nach dem Nettoeinkommen und Sozialabzüge
> | Ziff. | Code | Position | Staat | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 21.1 | 650 / 238 / 240 | Krankheitskosten | Vorkolonne 3'600, Selbstbehalt 843, **Abzug 2'757** | Vorkolonne 3'600, Selbstbehalt 2'456, **Abzug 1'144** | Zahnarzt 2'750 + Kostenbeteiligung 850 = 3'600. Selbstbehalt Kanton 2 % × 42'150, Bund 5 % × 49'120. | sg-wl-2025__c0098 |
> | 21.3 | 244 | Spenden | 0 | 0 | Caritas 80 liegt unter der Mindestsumme von 100 | sg-wl-2025__c0102 |
> | **22** | **248** | **Reineinkommen** | **39'393** | **47'976** | | |
> | 23.2 | 254 | Kinderabzug Elias | 10'800 | 6'800 | Der Kindergarten zählt zur Schulpflicht, also 23.2 und nicht 23.1. Bund einheitlich 6'800. | sg-wl-2025__c0104 |
> | **24** | **268** | **Steuerbares Einkommen** | **28'593** | **41'176** | | |
> 
> Der Bund liegt rund 12'600 über dem Kanton. Das erklärt sich so:
> - Fahrkosten: 4'700 weniger Abzug im Bund.
> - Kinderabzug: 4'000 weniger.
> - Versicherungsabzug: 2'000 weniger.
> - Weiterbildung: 60 weniger.
> - Übrige Berufskosten: 210 weniger.
> - Krankheitskosten: 1'613 weniger.
> 
> Zusätzlich zieht der Bund 263 pro Kind direkt vom Steuerbetrag ab. Das macht die Behörde automatisch (sg-wl-2025__c0104).
> 
> ## Vermögen
> | Ziff. | Code | Position | Betrag (nur Kanton) |
> |---|---|---|---|
> | 30.1 | 300 | Sparkonto Raiffeisen (Form. 2) | 31'500 |
> | 30.4 | 306 | Motorfahrzeug | **Wert fehlt**, siehe offene Punkte |
> | 33 / 35 | 322 / 326 | Total Vermögenswerte / Reinvermögen | 31'500 (ohne Auto) |
> | 36.1 | 330 | Abzug Alleinstehende | 75'000 |
> | 36.3 | 334 | Abzug 1 minderjähriges Kind | 20'000 |
> | **37** | **338** | **Steuerbares Vermögen** | **0** (31'500 − 95'000, mindestens 0) |
> 
> Der Bund erhebt keine Vermögenssteuer. Die Sozialabzüge trägt man in voller Höhe ein.
> 
> ## Nicht zu deklarieren bzw. nicht abziehbar
> - **Motorfahrzeugsteuer 410 und Auto-Haftpflicht/Kasko 1'020:**
>   - Sie sind kein eigener Abzug. Die Fahrkosten laufen nur über den Kilometeransatz.
>   - Motorfahrzeug- und Haftpflichtversicherungen sind ausdrücklich nicht im Versicherungsabzug abziehbar (Ziff. 14, Beachten).
>   - Dass der 0.70-Satz die Motorfahrzeugsteuer mit abdeckt, habe ich nicht mit einer Fundstelle belegt.
> - **Handy-Abo 720:** kein separater Abzug. Es ist über die Pauschale 416 abgegolten. Effektive übrige Berufskosten (Form. 4 Ziff. 3.2) lohnen sich erst, wenn sie nachweislich über 2'400 liegen. Eine Fundstelle zu Handy-Abos habe ich nicht gefunden.
> - **Spende Caritas 80:** unter 100, also kein Abzug. Sie bleibt ausserhalb der Steuererklärung.
> - **Kita-Mahlzeiten 1'080:** nicht abziehbar, deshalb in Ziff. 16.2 abgezogen.
> - **Kinderzulage 2'400:** nicht separat unter Ziff. 3.5 erfassen. Sie ist schon im Nettolohn 73'000. Ziff. 3.5 gilt nur für Zulagen, die eine Ausgleichskasse direkt auszahlt.
> - **BVG-Beitrag 4'610 und AHV 5'890 aus dem Lohnausweis:** nicht nochmals abziehen. Sie sind im Nettolohn berücksichtigt.
> - **Prämienverbilligung 1'800:** kein Einkommen. Sie wird nur in Form. 6 abgezogen.
> - **Vorsorgeguthaben (PK, Säule 3a):** kein Vermögen bis zur Fälligkeit (sg-wl-2025__c0107).
> - **Nicht zutreffend:**
>   - Zweiverdienerabzug (Ziff. 17).
>   - Unterhaltsbeiträge zahlen (Ziff. 12).
>   - Schuldzinsen.
>   - Liegenschaften (sie ist Mieterin).
>   - Wertschriftenverwaltungskosten (Ziff. 16.1, nur Sparkonto, kein Depot).
> - **Zu deklarieren, obwohl man es vielleicht nicht erwartet:** Die Kinderalimente 9'600 sind für Nadine steuerbar (Ziff. 6.1).
> 
> ## Offene Punkte / Annahmen für die Fachperson
> 1. **Fahrkosten Privatauto (Ziff. 1.3):**
>    - Ich habe sie als begründeten Fall erfasst. Die erste ÖV-Verbindung ab 06:40 erreicht den Arbeitsbeginn um 06:00 nicht. Der Privatwagen ist nach Art. 18 Abs. 1bis lit. b StV nur abziehbar, wenn kein ÖV zur Verfügung steht oder dessen Benützung unzumutbar ist.
>    - Im Form. 4 ist die Begründung anzukreuzen. Die Fundstelle ist sg-stb-39-3__c0004/c0005.
>    - Sicherheitshalber eine Arbeitgeberbestätigung zum Arbeitsbeginn und zu den Dienstplänen bereithalten.
>    - Annahme: 220 Arbeitstage ohne Homeoffice-Tage.
> 2. **Auto im Vermögen (Ziff. 30.4, Code 306):**
>    - Der Fahrzeugwert fehlt. Steuerwert = Anschaffungswert − 20 % pro Jahr seit Erwerb.
>    - Das steuerbare Vermögen bleibt 0, solange der Steuerwert unter 63'500 liegt. Bitte Kaufpreis und Erwerbsjahr nachreichen.
> 3. **Krankenkassenprämien:** Ich habe 5'280 und 1'320 als Bruttoprämien gelesen. Das Ergebnis in Ziff. 14 ändert sich nicht, falls es Nettoprämien sind, weil das Maximum so oder so greift.
> 4. **Zahnarzt 2'750:** Ich nehme an, die Behandlung war medizinisch notwendig, also nicht rein kosmetisch. Das habe ich nicht geprüft. Die Rechnung bei Form. 6 aufführen. Die Kassenabrechnung nur beilegen, wenn man darauf verweist.
> 5. **Belege beilegen:**
>    - Lohnausweis.
>    - Säule-3a-Bescheinigung.
>    - PK-Bescheinigung zusammen mit der Einkaufsberechnung (sg-wl-2025__c0086).
>    - Form. 10 (Kinderbetreuung).
>    - Steuerauszug Raiffeisen.
>    - Alimenten-Nachweis. Bei erstmaliger Zahlung kommt der Auszug aus dem Scheidungsurteil dazu, in Folgejahren eine Aufstellung (sg-wl-2025__c0084).
> 6. **Kinderabzug:** Nadine erhält ihn, weil Elias bei ihr lebt und sie die Alimente bezieht. Der Ex-Mann verliert den Kinderabzug, sobald er Ziff. 12.2 abzieht (sg-wl-2025__c0104).
> 
> Die fachliche Beurteilung und Abnahme liegt bei der Fachperson.

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


**Antwort des Agenten** (172.1 s · Tools: 40 Aufrufe read, steuerwiki__formular, steuerwiki__position, steuerwiki__zeige, steuerwiki__suche, steuerwiki__beleg, steuerwiki__wert, message, steuerwiki__rechne):

> **TG · Steuerjahr 2025** · Formular: Steuererklärung 2025 TG (Formular 1, zwei Spalten Staat | Bund) mit Hilfsblättern 2, 4.1, 5.1, 5.2, 6, 7, 8.
> Mandantin: verwitwet, alleinstehend, Jg. 1955, Rentnerin mit Eigenheim in Frauenfeld. Alle Werte haben Status ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen). Beträge in ganzen Franken, alle Rechnungen mit `rechne` geprüft.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Beleg / Fundstelle |
> |---|---|---|---|---|---|
> | 3.1 | 130 | AHV-Rente | 27'000 | 27'000 | 12 × 2'250 (AHV-Bescheinigung). tg-form-01-2025__c0007 |
> | 3.2 | 132 | Rente 2. Säule | 10'800 (100 %) | 10'800 (100 %) | 12 × 900. Renten der beruflichen Vorsorge sind zu 100 % steuerbar. Der Rentenbeginn 2020 löst keine 80 %-Regel aus. tg-wl-2025__c0077 |
> | 4 | 150 | Wertschriften- und Zinserträge (Übertrag Form. 2) | **2'160** | **2'350** | Siehe 1a. |
> | 6 | 175 | Zwischentotal Einkünfte | 39'960 | 40'150 | 27'000 + 10'800 + Ziff. 4 |
> | 8.1 | 180 | Liegenschaften (Form. 7) | **4'840** | **8'920** | Siehe 1b. |
> | 9 | 198 | Total Einkünfte (→ Ziff. 20) | **44'800** | **49'070** | Ziff. 6 + Ziff. 8.1 |
> 
> **1a. Form. 2 Wertschriftenverzeichnis** (tg-wl-2025__c0153, c0159, c0167)
> - Beide Positionen gehören in Spalte 8, Erträge mit Verrechnungssteuer (VSt). Das Sparkonto hat Bruttozins 250 und liegt damit über 200.
> - Spalte 7 (Steuerwert): Sparkonto 48'000 + Depot 95'000 = 143'000.
> - Spalte 8 (Bruttoertrag): 250.00 + 2'100.00 = 2'350.00. Das Total I ist brutto zu deklarieren, nicht netto.
> - Ziff. 10 Verrechnungssteueranspruch: 35 % × 2'350 = **822.50**. Das entspricht 87.50 + 735 laut Steuerauszug. Es ist eine Rückerstattung, weder Einkommen noch Abzug.
> - Code 148 Vermögensverwaltungskosten, **nur Staat**: 2 ‰ × 95'000 = 190, Pauschale ohne Beleg. Das Sparkonto zählt nicht zur Bemessung. Staat 2'350 − 190 = 2'160.
> - Bund: Eine Bundespauschale ist im Wiki nicht belegt. Ich setze 0 an, also 2'350. Erst ein Depotgebührenausweis würde einen Bundesabzug ermöglichen.
> 
> **1b. Form. 7 und 8 Liegenschaft** (EFH Baujahr 1986, am Wohnsitz selbst bewohnt)
> - Der Selbstnutzungsabzug beträgt Staat 40 % und Bund 20 % (tg-wl-2025__c0225).
> - Steuerbarer Eigenmietwert: Staat 20'400 × 60 % = **12'240**, Bund 20'400 × 80 % = **16'320**.
> - Pauschale (Gebäude über 10 Jahre alt, 20 %): Staat 2'448, Bund 3'264. Sie ist nicht günstiger.
> - **Effektiver Unterhalt (Form. 8): 7'400** für Staat und Bund, nach tg-wl-2025__c0227 und tg-stp-34-1__c0006:
>   - Malerarbeiten (Ersatzanstrich, Instandhaltung): 6'400
>   - Gebäudeversicherung (Sachversicherung, Besitzesabgabe): 520
>   - Baumschnitt und Gartenpflege (Gartenunterhalt beim EFH abziehbar): 480
> - **Wintergarten-Anbau 31'000: nicht abziehbar.** Er ist ein Anbau und damit wertvermehrend (tg-wl-2025__c0233). In Form. 8 gehört er in die Spalte «Anlagekosten/Mehrwert».
> - Nettoerfolg: Staat 12'240 − 7'400 = **4'840**, Bund 16'320 − 7'400 = **8'920**.
> - Steuerwert Form. 7 (Code 430): 410'000.
> 
> ## 2. Abzüge
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 11 | 290 | Schuldzinsen (Form. 4.1) | 3'150 | 3'150 | Hypothekarzins 2025. Die Limite Vermögensertrag + 50'000 (rund 57'000) ist eingehalten. tg-wl-2025__c0173 |
> | 14 | 330 | Versicherungsprämien und Sparzinsen (Form. 5.2) | **3'500** | **2'700** | A1 KK-Prämien netto 6'240 (keine IPV). A4 Sparzinsen 250. A5 = 6'490. Der Abzug ist min(A5; B4). B4 Staat 3'500. B4 Bund 2'700, weil keine Beiträge an Säule 2 oder 3a geleistet wurden. tg-wl-2025__c0212 |
> | 19 | 360 | Total Abzüge (→ Ziff. 21) | **6'650** | **5'850** | 3'150 + 3'500 bzw. 3'150 + 2'700 |
> | 22 | 362 | **Nettoeinkommen** | **38'150** | **43'220** | Ziff. 9 − Ziff. 19 |
> 
> Folgende Ziffern sind nicht anwendbar: 1, 2, 10, 13 (keine 3a), 15.1 bis 15.6 (der AHV-Beitrag für Nichterwerbstätige entfällt, weil sie Rentnerin ist), 16, 17 und 18. Das ist plausibel, aber nicht mit Belegen geprüft.
> 
> ## 3. Abzüge auf Basis Nettoeinkommen und Reineinkommen
> 
> | Ziff. | Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 23.1 | 364 | Krankheitskosten (Form. 5.1 D) | **4'633** | **4'379** | Siehe unten. |
> | 23.2 | 366 | Freiwillige Zuwendungen (Form. 6) | **350** | **550** | Summe 300 + 250 = 550. Staat 550 − 200 Selbstbehalt = 350 (Maximum 8'000, da Netto ≤ 40'000). Bund: Summe ≥ 100, daher voll abziehbar (Maximum 20 % × 43'220 = 8'644). tg-wl-2025__c0220 |
> | 24 | 372 | **Reineinkommen** | **33'167** | **38'291** | Staat 38'150 − 4'633 − 350. Bund 43'220 − 4'379 − 550. |
> | 25.3 | 388 | Abzug AHV-Rentner/Verwitwete (**nur Staat**) | **1'000** | – | 4'200 − 200 × 16 volle Tausender über 16'900 (Reineinkommen 33'167, Stufe 32'900–33'899). tg-wl-2025__c0116 |
> | 26 | 398 | **Steuerbares Einkommen** | **32'167** | **38'291** | Ziff. 24 − Ziff. 25.3 |
> 
> Weitere Sozialabzüge (25.1, 25.2, 25.4, 28.1 und 28.2) kommen nicht zur Anwendung, weil keine Kinder, keine unterstützten Personen und keine gemeinsame Besteuerung vorliegen.
> 
> **Krankheitskosten, Form. 5.1** (tg-wl-2025__c0205, c0206)
> - A (selbst getragen):
>   - A1 Franchise und Selbstbehalt: 1'000
>   - Zahnarzt Krone: 4'440
>   - Brille mit Verordnung: 1'400
>   - Total A = 6'840
> - B (Vergütung Dritter): Zusatzversicherung Brille 300.
> - A − B = **6'540**.
> - Selbstbehalt 5 % des Nettoeinkommens (Ziff. 22): Staat 1'907.50, Bund 2'161.
> - Abzug: Staat 6'540 − 1'907.50 = 4'632.50, in ganzen Franken **4'633**. Bund **4'379**.
> - Die Krankenkassenprämien 6'240 gehören nicht hierher, sondern in Ziff. 14.
> 
> ## 4. Vermögen (nur Staat)
> 
> | Ziff. | Code | Position | Betrag |
> |---|---|---|---|
> | 30.1 | 410 | Wertschriften und Guthaben (Form. 2 Ziff. 9) | 143'000 |
> | 31 | 430 | Liegenschaft (Steuerwert, Form. 7) | 410'000 |
> | 33 | 464 | Total Vermögenswerte | 553'000 |
> | 34 | 466 | Schulden (Form. 4.1, Code 455) | 180'000 |
> | 35 | 468 | Reinvermögen | 373'000 |
> | 36.2 | 472 | Freibetrag Alleinstehende | 100'000 |
> | 37 | 498 | **Steuerbares Vermögen** | **273'000** |
> 
> Die Hypothek gehört in Form. 4.1 A mit Gläubiger, Adresse und Zinssatz (3'150 / 180'000 = 1.75 %).
> 
> ## 5. Nicht zu deklarieren oder nicht abziehbar
> - **Hausratversicherung 380:** nicht abziehbar, keine Einreichung. Sachversicherung für die Liegenschaft ist nur die Gebäudeversicherung (c0227).
> - **Serafe 335 und Handyrechnung:** Lebenshaltungskosten, kein Abzug (Art. 34 DBG). Die Handyrechnung ist im Wiki als privater Alltagsbeleg erfasst. Zu Serafe gibt es im Wiki keinen eigenen Beleg, das ist eine Einordnung ohne Fundstelle.
> - **Wintergarten 31'000:** kein Unterhaltsabzug.
> - **Krankenkassenprämien:** nicht bei den Krankheitskosten, nur im Versicherungsabzug (Ziff. 14).
> - **Verrechnungssteuer 822.50:** nicht als Einkommen oder Abzug erfassen, sondern in Form. 2 Ziff. 10 zurückfordern.
> - **Eigenmietwert und Unterhalt:** nicht gleichzeitig Pauschale und effektive Kosten abziehen, die Wahl gilt je Liegenschaft und Jahr.
> 
> ## 6. Belege einreichen
> - Steuerauszug oder Depotverzeichnis der TKB (c0142).
> - Rechnung der Malerarbeiten (6'400 liegt über 1'000, c0234).
> - Krankheitskosten: Kostenzusammenstellung der Krankenkasse und Zahnarztrechnung (c0206).
> - Spendenquittungen: nur ab 1'000 pro Zuwendung, hier nur auf Verlangen (c0220).
> 
> ## 7. Offene Punkte und Hinweise für die Fachperson
> 1. **Bund-Selbstnutzungsabzug 20 %:** Das Limite-Feld im Wiki sagt «Bund nicht anwendbar». Die Wegleitung (tg-wl-2025__c0225) und der Eckwert nennen 20 %. Ich habe 20 % verwendet.
> 2. **Gartenunterhalt 480 beim Bund:** Für TG ist er belegt, für den Bund nicht im Wiki geprüft. Ohne ihn wäre der effektive Unterhalt 6'920 und der Nettoerfolg Bund 9'400. Das wäre immer noch günstiger als die Pauschale 3'264.
> 3. **Bund-Verwaltungskosten:** 0 angesetzt, weil keine Depotgebühren belegt sind. Würde die Kantonspauschale 190 auch dem Bund gewährt, läge Ziff. 4 Bund bei 2'160.
> 4. **Rundung Krankheitskosten Staat:** 4'632.50 auf 4'633 aufgerundet. Die Rundungsregel ist nicht belegt, die Abweichung beträgt höchstens 1 Franken.
> 5. **Zahnarzt Krone:** Ich habe keine Kassen- oder Versicherungsvergütung angenommen. Bitte mit der Leistungsabrechnung abgleichen.
> 6. **Sparzinsen Ziff. 14:** Ich habe den Bruttozins 250 eingesetzt. Beide Ebenen sind ohnehin auf die Maximalabzüge begrenzt.
> 7. **Wintergarten:** Der Anbau führt voraussichtlich zu einer Neuschätzung von Steuerwert und Mietwert. Prüfen, ob 410'000 und 20'400 dem Stand Ende 2025 entsprechen.
> 8. **Spendenempfänger:** Krebsliga Thurgau und Pro Senectute Thurgau sind mit Name und Sitz einzutragen. Die Abzugsfähigkeit ist gegen die Liste geprüfter Institutionen zu bestätigen.
> 9. **Fehlende Angaben:** Adresse des Hypothekargläubigers, Bargeld, Motorfahrzeuge, Rückkaufswerte von Lebensversicherungen (Ziff. 30.2 bis 30.6). PK-Guthaben und Säule 3a sind nicht zu deklarieren.
> 10. **Plausibilität:** Bund liegt 6'124 über Staat (38'291 gegenüber 32'167). Das erklärt sich so:
>     - Selbstnutzungsabzug: +4'080
>     - Vermögensverwaltungskosten: +190
>     - Versicherungsabzug: +800
>     - Krankheitskosten und Spenden: +54
>     - Ziff. 25.3: +1'000
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


**Antwort des Agenten** (136.7 s · Tools: 29 Aufrufe read, steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__wert, steuerwiki__zeige, steuerwiki__suche, steuerwiki__rechne):

> Ich rechne jetzt alle Beträge nach und prüfe zwei Fundstellen: Steuern und Handy-Abo sind nicht abziehbar.
> 
> **AR · Steuerjahr 2025 · Ehepaar Herisau (gemeinsame Veranlagung), 2 Kinder**
> 
> Das AR-Formular hat keine Bundesspalte. Die Steuerverwaltung nimmt die Bundesabweichungen automatisch vor (ar-wl-2025__c0179). Ins Formular trägst du also den Kantonswert ein. Die Bundesspalte unten ist die Kontrollrechnung für die direkte Bundessteuer.
> 
> Fast alle Positionen haben den Status ☑️ (agent-geprüft, Abnahme offen). Die Hauptformular-Codes zu Ziff. 10–24 sind in der Wegleitung nicht verifiziert. Wo ein Code unten fehlt, hat das Wiki keinen gesicherten.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg / Beleg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb P1 | 85'300 | 85'300 | Lohnausweis Ziff. 11. Kontrolle: 98'000 − 6'860 − 5'840 | ar-wl-2025__c0035 |
> | 1.1 | 102 | Haupterwerb P2 | 68'200 | 68'200 | Lohnausweis Ziff. 11. Kontrolle: 82'000 − 5'740 − 4'060 − 4'000 | ar-wl-2025__c0035 |
> | 4.1 | 146 | Wertschriften/Guthaben (Übertrag Form. 2) | 1'410 | 1'410 | Konten 160 (Spalte B, ≤ 200 ohne VSt) + Dividenden 1'250 (Spalte A) | ar-wl-2025__c0136 |
> | **7** | 168 | **Total Einkünfte** | **154'910** | **154'910** | 85'300 + 68'200 + 1'410 | |
> 
> Die Kinder- und Ausbildungszulagen von P2 stehen im Bruttolohn und damit schon im Nettolohn. Sie werden nicht separat erfasst, und Ziff. 3.5 bleibt leer (3.5 gilt nur für Zulagen, die eine Ausgleichskasse direkt ausbezahlt, ar-wl-2025__c0054).
> 
> ## 2. Hilfsblatt Form. 4 (Berufskosten)
> 
> | Form. 4 | P1 Kt | P1 Bund | P2 Kt | P2 Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 1.1 Fahrkosten ÖV (400/450) | **0** | **0** | 1'260 | 1'260 | P1: Feld F angekreuzt, daher kein Abzug (ar-wl-2025__c0075). P2: Abo effektiv, unter dem Maximum (Kt 6'000 / Bund 3'300) |
> | 2.1 Verpflegung (408/458) | – | – | 2'640 | 2'640 | P2: 176 × 15 = 2'640, unter dem Maximum von 3'200 (ar-form-04-2025__c0003) |
> | 2.2 Verpflegung verbilligt (410/460) | 1'600 | 1'600 | – | – | P1: Feld G angekreuzt, 220 × 7.50 = 1'650, begrenzt auf 1'600 |
> | 3 Übrige Berufskosten (416/466) | 2'400 | 2'559 | 2'400 | 2'046 | Kt: 700 + 10 % × Nettolohn, max. 2'400. Bund: 3 % × Nettolohn (min. 2'000, max. 4'000) |
> | **6 Total** (438 / 488) | **4'000** | **4'159** | **6'300** | **5'946** | |
> 
> - Die Pauschale «übrige Berufskosten» steht beiden zu. Fahrkosten und Verpflegung kommen dazu.
> - Ziff. 2.3 (Schichtarbeit) greift bei P2 nicht. Eine Tagesschicht ist keine durchgehende Schicht- oder Nachtarbeit von mindestens 8 Stunden. 2.3 ist ausserdem nicht mit 2.1 kombinierbar.
> 
> ## 3. Abzüge
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 10.1 | 438 | Berufskosten P1 | 4'000 | 4'159 | Form. 4 Total |
> | 10.2 | 488 | Berufskosten P2 | 6'300 | 5'946 | Form. 4 Total |
> | 13.1 | – | Säule 3a (P1 7'258 + P2 5'000) | 12'258 | 12'258 | P1 am Maximum 7'258 (mit 2. Säule). P2 5'000 liegt darunter. Je eigene Bescheinigung (ar-wl-2025__c0003, c0083) |
> | 13.2 | – | PK-Einkauf | **0** | **0** | Die 4'000 stehen schon in Lohnausweis Ziff. 10.2 und damit im Nettolohn. Hier nochmals einzutragen wäre ein Doppelabzug. Die Bestätigung der PK bleibt als Beleg bereit |
> | 14 | 600 | Versicherungsprämien (Form. 6) | 7'400 | 5'100 | Kt: min(13'900; 5'400 + 2 × 1'000). Bund: min(13'900; 3'700 + 2 × 700). Der Höchstbetrag greift, die Prämien sind höher. Prämienverbilligung = 0 |
> | 16.1 | – | Verwaltungskosten Wertschriften | 276 | 0 | Kt-Pauschale 3 ‰ × 92'000 (Steuerwerte 54'000 + 38'000, inkl. Konten). Bund: nur effektive Depotspesen, kein Beleg vorhanden (bund-wl-2a-2025__c0056) |
> | 16.2 | – | Kinderbetreuung Lea (Form. 10) | 10'200 | 10'200 | 14'400 − 1'800 Mittagessen − 2'400 Betreuungsbeitrag. Lea ist unter 14, beide Eltern sind erwerbstätig. Unter dem Maximum (Kt 25'000 / Bund 25'800) |
> | 17 | – | Zweiverdienerabzug | 5'200 | 14'100 | Basis P2 (niedrigeres Einkommen). Kt: 68'200 − 6'300 − 5'000 = 56'900, davon 10 % = 5'690, begrenzt auf 5'200. Bund: 68'200 − 5'946 − 5'000 = 57'254, davon 50 % = 28'627, begrenzt auf 14'100 |
> | **18** | – | **Total Abzüge** | **45'634** | **51'763** | Summe der Zeilen oben |
> | **20** | – | **Nettoeinkommen** | **109'276** | **103'147** | 154'910 − Total Abzüge |
> | 21.1 | – | Krankheitskosten | 0 | 0 | Keine Belege eingereicht |
> | 21.3 | 550 | Zuwendungen Krebsliga | 300 | 300 | Total ≥ 100, Obergrenze 20 % × Netto (21'855), also volle 300 (ar-form-05-2025__c0003) |
> | **22** | – | **Reineinkommen** | **108'976** | **102'847** | Nettoeinkommen − 300 |
> 
> ## 4. Sozialabzüge und steuerbares Einkommen
> 
> | Ziff. | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|
> | 23.1 | Kind bis Vollendung 4. Altersjahr | – | – | Lea ist am 31.12.2025 vier Jahre alt (4. Geburtstag 14.03.2025), fällt also nicht hierunter |
> | 23.2 | Lea (4.–15. Altersjahr) | 7'400 | 6'800 | Stichtag 31.12.2025 (ar-wl-2025__c0005) |
> | 23.3 | Jonas (nach 15. Altersjahr, Ausbildung) | 11'600 | 6'800 | Jonas ist 16. Schulgeld (Kantonsschule) ist nicht zusätzlich abziehbar (ar-wl-2025__c0005) |
> | – | Verheiratetenabzug (nur Bund) | – | 2'800 | Art. 35 DBG, im Formular nicht erfasst (ar-wl-2025__c0063) |
> | **24** | **Steuerbares Einkommen** | **89'976** | **86'447** | Kt: 108'976 − 19'000. Bund: 102'847 − 16'400 |
> 
> Beim Bund kommt automatisch ein Abzug vom Steuerbetrag dazu: 263 je Kind, zusammen 526. Das ist kein Abzug vom Einkommen.
> 
> ## 5. Vermögen (nur Kanton, der Bund hat keine Vermögenssteuer)
> 
> | Ziff. | Code | Position | Betrag | Rechenweg |
> |---|---|---|---|---|
> | 30.1 | 300 | Wertschriften und Guthaben (Form. 2) | 92'000 | Konten 54'000 + Aktien 38'000 |
> | 33 | 322 | Total Vermögenswerte | 92'000 | |
> | 35 | 326 | Reinvermögen | 92'000 | Keine Schulden |
> | 36.2 | 332 | Sozialabzug Ehegatten | 150'000 | In voller Höhe eintragen |
> | 36.3 | 334 | Sozialabzug Kinder | 50'000 | 2 × 25'000, beide minderjährig mit Kinderabzug (ar-wl-2025__c0122) |
> | **37** | 338 | **Steuerbares Vermögen** | **0** | max(92'000 − 200'000; 0) |
> 
> Form. 2 Code 999 (Verrechnungssteueranspruch) = 35 % × 1'250 = **Fr. 437.50**. Das ist eine Rückerstattung, weder Einkommen noch Abzug. Der Betrag stimmt mit dem abgezogenen VSt-Betrag überein.
> 
> ## 6. Nicht zu deklarieren oder nicht abziehbar
> 
> - **Pensionskassen-Einkauf P2 (4'000) unter Ziff. 13.2:** nicht nochmals, er ist bereits im Nettolohn abgezogen.
> - **Fahrkosten P1:** Feld F (Werkbus) schliesst den Abzug aus.
> - **Kita-Mittagessen (1'800):** Lebenshaltungskosten, nicht abziehbar (ar-stv__art-28a).
> - **Betreuungsbeitrag (2'400):** mindert den Abzug und ist kein eigener Abzug.
> - **Mitgliederbeitrag Turnverein (120):** keine Zuwendung, Mitgliederbeiträge sind nicht abzugsfähig (ar-wl-2025__c0102). Er ist auch nicht Teil der 100-Fr.-Grenze.
> - **Steuerschlussrechnung 2024 (9'870):** Einkommens- und Vermögenssteuern sind nicht abziehbar (Art. 37 Abs. 1 lit. e StG AR).
> - **Handy-Abo (960):** privater Aufwand (Art. 37 Abs. 1 lit. a StG AR). Die Pauschale «übrige Berufskosten» deckt allfällige berufliche Nutzung ab.
> - **Krankenkassenprämien über dem Höchstbetrag (13'900 − 7'400):** der Mehrbetrag bleibt ohne Wirkung.
> - **Vorsorgeguthaben (PK, Säule 3a):** kein steuerbares Vermögen, nicht deklarieren (ar-wl-2025__c0111).
> - **Schulgeld Jonas:** über den Kinderabzug abgegolten.
> 
> ## 7. Offene Punkte für die Fachperson
> 
> 1. **Verpflegung P2 (Ziff. 2.1, 2'640):** Die Annahme ist, dass eine Heimkehr zum Mittagessen nicht zumutbar ist (Arbeitsort St. Gallen, Mittagessen auswärts). Das Wiki verlangt dafür «grosse Entfernung». Wird der Abzug abgelehnt, sinken die Berufskosten Kt auf 3'660. Zweiverdiener- und Nettoeinkommen verschieben sich entsprechend. **Rückfrage:** Wie lang ist die Mittagspause, und ist ein Heimweg möglich?
> 2. **Verpflegung P1 (2.2, 1'600):** Der Abzug entfällt, wenn die Kantine so billig ist, dass keine Mehrkosten gegenüber zu Hause entstehen. Das Wiki nennt dafür kein Kriterium. Ich habe den Standardabzug erfasst.
> 3. **Betreuungsbeitrag (2'400):** Ich habe angenommen, dass die 14'400 der Brutto-Rechnungstotal vor der Gutschrift sind. Sind sie bereits netto, wäre der Abzug 12'600.
> 4. **Bund 16.1:** Der Bundesabzug ist 0, weil kein Gebührenbeleg vorliegt. **Rückfrage:** Weist der Steuerauszug Depotgebühren aus? Das gilt nur, wenn sie über 276 liegen.
> 5. **Fehlende Belege und Rückfragen:** Sind Motorfahrzeuge vorhanden (Ziff. 30.4)? Das Wiki verlangt sie sonst nicht. Gibt es Krankheitskosten (Selbstbehalt 5 % × Nettoeinkommen)? Das Wiki nennt als Vergleich die Vorjahresveranlagung, sie liegt nicht vor.
> 6. **Codes:** Die Codes zu Ziff. 10.1, 13.x, 14, 16.x, 17 und 23.x sind im Wiki nicht verifiziert. Die Codes 36.2/36.3 (332/334) stammen aus einer verzerrten Miniatur und sind am Originalformular zu prüfen.
> 7. **Bund:** Der Bundesbetrag je Position ist die Kontrollrechnung nach den Wiki-Limiten. Die effektive Bundesveranlagung macht die Steuerverwaltung.
> 8. **Fachliche Beurteilung:** Sie bleibt bei der Fachperson. Alle Beträge sind mit `rechne` geprüft.

