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


**Antwort des Agenten** (169.4 s · Tools: 20 Aufrufe read, steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__suche, steuerwiki__rechne):

> Ich lese zuerst den Skill und das Formular ZH 2025.
> 
> Das Formular ist geladen. Jetzt die Belegregeln und die Positionen, die die Belege betreffen.
> 
> Die Belege sind erfasst. Jetzt die Positionen mit offenen Fragen: Velo-Codes und Berufskosten (Form. 360), Zweiverdienerabzug, Verwaltungskosten, Versicherungsabzug, Kinderzulagen und der Arbeitsort in Zug.
> 
> Die Positionen sind geklärt. Der Zweiverdienerabzug hat eine Basis nach Berufsauslagen und Säule 3a. Ich rechne jetzt alle Summen und Totale exakt nach.
> 
> # Ausfüllhilfe ZH · Steuerjahr 2025
> 
> **Mandant:** Ehepaar Marco (Person 1) und Sandra (Person 2), Winterthur, Mieter, zwei Kinder (Lena 4, Noah 9). Beträge in CHF, ganze Franken. Alle Werte sind mit `rechne` nachgerechnet.
> 
> Status: ☑️ = Fundstelle geprüft, Abnahme offen · ⚠️ = Annahme oder Klärung nötig · ⬜ = offen.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg / Beleg | Fundstelle · Status |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Nettolohn Person 1 | 103'000 | 103'000 | LA Ziff. 11: 118'400 − 8'110 − 7'290 − 0 | zh-form-300-2025__c0005 · ☑️ |
> | 1.1 | 101 | Nettolohn Person 2 | 67'200 | 67'200 | LA Ziff. 11: 76'800 − 5'260 − 4'340 − 0 (enthält Kinderzulagen 4'800) | zh-form-300-2025__c0005 · ☑️ |
> | 3.4 | 142/143 | Kinderzulagen | – | – | nicht eintragen: über den Lohn ausbezahlt, bereits in Ziff. 1 | zh-wl-2025__c0055 · ☑️ |
> | 4.1 | 150 | Bruttoertrag Wertschriften/Guthaben | 1'140 | 1'140 | Kol. A 960 (Depot) + Kol. B 180 (Sparzins, ≤ 200, ohne VSt) | zh-wl-2025__c0153 · ☑️ |
> | 4.2 | 151 | davon qualifizierte Beteiligungen (≥ 10 %) | 0 | 0 | keine Angabe, siehe offene Punkte | ⚠️ |
> | 19 | 199 | **Total Einkünfte** | **171'340** | **171'340** | 103'000 + 67'200 + 1'140 | – |
> 
> ## 2. Abzüge
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg / Beleg | Fundstelle · Status |
> |---|---|---|---|---|---|---|
> | 11.1 | 220 | Berufsauslagen Person 1 (Total Form. 360 Ziff. 6) | 10'470 | 9'590 | 201 ÖV-Abo 4'180 (Bund-Plafond 3'300); 208 Verpflegung voll: min(220 × 15; 3'200) = 3'200; 212 übrige Pauschale 3 %: 3'090 (K und B) | zh-form-360-2025__c0001, __c0003 · ☑️ |
> | 11.2 | 240 | Berufsauslagen Person 2 | 4'036 | 4'036 | 222 Velo-Pauschale 700; 226 Verpflegung verbilligt (Feld G): 7.50 × 176 = 1'320; 232 übrige 3 %: 2'016 | zh-form-360-2025__c0001 · ☑️ ⚠️ (Velo-Annahme) |
> | 14.1 | 260 (eff. 262) | Säule 3a Person 1 | 7'258 | 7'258 | min(einbezahlt 7'258; Max. mit 2. Säule) | zh-wl-2025__c0081 · ☑️ |
> | 14.2 | 261 (eff. 263) | Säule 3a Person 2 | 7'258 | 7'258 | wie oben | zh-wl-2025__c0081 · ☑️ |
> | 15 | 270 | Versicherungsprämien | 8'400 | 5'100 | Form. 365 Teil A (Code 601) = 15'840 (KK, keine IPV). Teil B: Verheiratete mit 2./3a + 1'300 bzw. 700 je Kind: K 5'800 + 2 × 1'300 = 8'400; B 3'700 + 2 × 700 = 5'100. Niedrigerer Wert. | zh-form-300-2025__c0008, zh-wl-2025__c0082 · ☑️ |
> | 16.1 | 280 | Einkauf PK Person 1 (freiwillig) | 10'000 | 10'000 | direkt überwiesen 14.11.2025; LA Ziff. 10.2 = 0, also kein Doppelabzug; keine Kapitalbezüge in 3 Jahren | zh-wl-2025__c0092 · ☑️ |
> | 16.3 | 283 | Verwaltungskosten Wertschriften | 94 | 0 | Kanton-Pauschale: 3 ‰ × 31'200 (Depot) = 93.60, gerundet 94. Bund: nur effektive Kosten, keine Depotgebühren belegt → 0 | zh-wl-2025__c0095 · ⚠️ |
> | 16.6 | 376 | Drittbetreuung (2 Kinder < 14) | 31'900 | 32'700 | Lena 27'300: min(27'300; 25'000 K / 25'800 B). Noah 6'900 (Hort): K 6'900, B 6'900 | zh-stg-2025__par-31-t4 · ☑️ / Hort ⚠️ |
> | 17 | 290 | Zweiverdienerabzug | 6'100 | 14'100 | Basis (niedrigeres Erwerbseinkommen = Person 2): 67'200 − 4'036 − 7'258 = 55'906. K min(55'906; 6'100). B min(55'906; max(50 % = 27'953; 8'600); 14'100) | zh-form-300-2025__c0008 · ☑️ |
> | 18 | 299 | **Total Abzüge** | **85'516** | **90'042** | Σ der Zeilen oben | – |
> | 21 | 310 | **Nettoeinkommen** | **85'824** | **81'298** | 171'340 − 85'516 / 171'340 − 90'042 | – |
> | 22.1 | 320 | Krankheits-/Unfallkosten | **0** | **0** | Kosten 1'850 + 1'240 = 3'090. Selbstbehalt 5 %: 4'291.20 (K) / 4'064.90 (B). Kosten liegen darunter. | zh-wl-2025__c0118 · ☑️ |
> | 22.2 | 324 | Gemeinnützige Zuwendungen | 650 | 650 | Rotes Kreuz 400 + UNICEF 250 (Sitz CH, befreit). Min. 100 erfüllt. Max. 20 %: 17'164.80 / 16'259.60, nicht erreicht. | zh-info-spenden__c0003 · ☑️ |
> | 23 | 350 | **Reineinkommen** | **85'174** | **80'648** | 85'824 − 0 − 650 / 81'298 − 0 − 650 | – |
> | 24.1 | 370 | Kinderabzug (2 Kinder) | 18'600 | 13'600 | 2 × 9'300 (K) / 2 × 6'800 (B) | ☑️ |
> | 24.3 | 365 | Verheiratetenabzug (nur Bund) | – | 2'800 | Bund-Spalte, kein kantonaler Abzug | ☑️ |
> | 25 | 390 | **Steuerbares Einkommen** | **66'574** | **64'248** | 85'174 − 18'600 / 80'648 − 13'600 − 2'800 | – |
> | 27 | 398 | Steuerbares Einkommen im Kanton ZH | 66'574 | – | identisch mit Ziff. 25 (keine Ausscheidung) | ⚠️ (siehe unten) |
> 
> **Plausibilität:** Kanton 66'574 vs. Bund 64'248, Differenz 2'326. Das ist die Abzugsdifferenz (Bund +4'526: Zweiverdiener +8'000, Drittbetreuung +800, Fahrkosten −880, Versicherung −3'300 usw.) minus Sozialabzug-Differenz (K 18'600 vs. B 16'400 = 2'200). 4'526 − 2'200 = 2'326 ✓.
> 
> ## 3. Vermögen
> 
> | Ziff. | Code | Position | Kanton | Bund | Beleg / Hinweis | Status |
> |---|---|---|---|---|---|---|
> | 30.1 | 400 | Wertschriften und Guthaben (Form. 340 Total) | 82'000 | – | Sparkonto 42'500 + Privatkonto 8'300 + Depot 31'200 (Steuerwerte 31.12.) | ☑️ |
> | 33 | 460 | Total Vermögenswerte | 82'000 | – | Σ | – |
> | 34 | 470 | Schulden | 0 | – | keine Schulden angegeben | ⬜ bestätigen |
> | 35 | 490 | Steuerbares Vermögen gesamt | 82'000 | – | 82'000 − 0; steuerfreie Tarifstufe nicht abziehen | – |
> | 37 | 498 | Steuerbares Vermögen im Kanton ZH | 82'000 | – | identisch mit Ziff. 35 | – |
> 
> **Vorsorgeguthaben** (PK Person 1 und 2, Säule 3a) gehören nicht ins Vermögen (ZH zh-wl-2025__c0154).
> 
> ## Hilfsblätter
> 
> - **Form. 340 (Wertschriften):** Kol. A Bruttoertrag 960 (Code 539), VSt-Anspruch Code 540 = 336 (35 % von 960), Kol. B 180 (Code 542), Total 1'140 → Ziff. 4.1. Steuerwerte 82'000 → Ziff. 30.1.
> - **Form. 360 (Berufsauslagen):** Codes siehe Ziff. 11.1/11.2. Person 2 Verpflegung verbilligt unter Code 226.
> - **Form. 365 (Versicherungen):** Teil A Code 601 = 15'840, Code 605 = 0, Code 606 = 15'840. Teil C Code 270 = 8'400 (K) / 5'100 (B).
> - **Form. 370 (Krankheitskosten):** nicht nötig, da kein Abzug.
> 
> ## Nicht zu deklarieren
> 
> | Position | Betrag | Grund |
> |---|---|---|
> | Swisscom-Handyrechnungen | 1'080 | Lebenshaltung, nicht abziehbar (§ 33 lit. a StG; Art. 34 lit. a DBG; zh-stg-2025__par-33) |
> | Hausrat- und Privathaftpflicht | 465 | Sachversicherung, nicht in Ziff. 15 (nur Kranken-/Lebens-/Unfall); Hausrat ist steuerfrei |
> | Zahnarzt und KK-Kostenbeteiligung | 1'850 + 1'240 | unter dem Selbstbehalt (5 % vom Nettoeinkommen), daher Abzug 0 |
> | Mietzins | – | Mieter, keine Liegenschaft, kein Abzug |
> | Kinderzulagen Person 2 | 4'800 | im Lohn enthalten, nicht zusätzlich unter Ziff. 3.4 |
> | Privatkonto-Zins | 0 | keine Zeile nötig |
> | Überschüsse über Limiten | ÖV Bund 880; Verpflegung P1 100; Kita Lena K 2'300 / B 1'500 | über Plafond, nicht abziehbar |
> 
> ## Offene Punkte und Annahmen (für die Fachperson)
> 
> 1. **Hort Noah (6'900):** Enthält die Rechnung Verpflegung (Mittagessen)? Wenn ja, nur den Betreuungsanteil abziehen, da Verpflegung nicht abziehbar ist. ⚠️
> 2. **Depot Schweizer Aktien:** Keine Angabe, ob eine Beteiligung ≥ 10 % (Code Q) besteht. Annahme: keine. Sonst Ziff. 4.2 und Teilbesteuerung 16.5 (K 50 %, B 30 %).
> 3. **Verwaltungskosten Bund (16.3):** Falls Depotgebühren ausgewiesen werden, Bund-Abzug nur effektiv. Pauschale nur für Kanton. Bund-Spalte bleibt bis dahin 0. ⚠️
> 4. **Arbeitsort Zug (Person 1):** Annahme: Lohn voll im Wohnsitzkanton ZH steuerbar, daher keine Ausscheidung Ziff. 26.1. Das Wiki belegt das nicht ausdrücklich. Fachperson bitte bestätigen. ⚠️
> 5. **Pendelweg Person 1:** Annahme: tägliche Fahrt Winterthur–Zug, kein Wochenaufenthalt. Bei Wochenaufenthalt gelten andere Regeln.
> 6. **Velo Person 2:** Annahme: ständige Benützung, daher Pauschale 700 (Code 222).
> 7. **Schulden und Motorfahrzeug (Ziff. 34, 30.4):** nicht angegeben. Bitte bestätigen, ob Schulden oder ein Auto vorhanden sind.
> 8. **Zweiverdienerabzug:** Basis nach Berufsauslagen und Säule 3a berechnet, wie im Wiki beschrieben. Abweichung nur, wenn die Fachperson eine andere Basis nimmt.
> 
> **Einreichen** (gemäss Wiki): Lohnausweise beider Personen, Säule-3a-Bescheinigungen, PK-Einkaufsbescheinigung (ZH Ziff. 16.1), Liste der Spenden (Ziff. 22.2, Bescheinigungen auf Verlangen), Formular 360, 365 und 340 mit Beilagen. Krankheitskosten-Belege entfallen.
> 
> Der Kanton (Staats- und Gemeindesteuer) und der Bund sind getrennt angegeben. Die Bundesspalte folgt den Bundesregeln, wo sie abweicht. Hinweis: Die Fachperson trägt die Verantwortung für die Erklärung.

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


**Antwort des Agenten** (147.2 s · Tools: 18 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__zeige, steuerwiki__rechne):

> Ich starte mit dem vollständigen SG-Formular 2025 und prüfe parallel die Kernpositionen.
> 
> Die Grundlagen für Lohn, Kinderbetreuung, Fahrkosten, Alimente und Prämien sind geklärt. Jetzt noch die offenen Positionen: Kinderabzug, Krankheitskosten, Verpflegung, Säule 2, Spenden, Weiterbildung, Vermögen und Zinsen.
> 
> Die Positionen sind geprüft. Bevor ich die Beträge rechne, kläre ich noch drei Punkte: die Verpflegungspauschale beim Mittagessen, die Begründung des Autoarbeitswegs und die Abziehbarkeit der Motorfahrzeugsteuer.
> 
> Die Verpflegung ist mit der Entfernung begründet. Für die Autobegründung lese ich die Zumutbarkeitsregel im Volltext nach.
> 
> SG · 2025 · Nadine (alleinerziehend, Toggenburg → St. Gallen) · Elias (5, Kindergarten)
> 
> **Vorab:** Das SG-Hauptformular 2025 hat **eine Spalte** (Kanton). Die Bundeswerte unten sind Orientierung; Abweichungen für die direkte Bundessteuer nimmt die Steuerbehörde automatisch vor (`sg-wl-2025__c0173`). Die Fahrkosten hängen an einer Begründung, die noch nicht belegt ist (siehe Punkt 1 unter «Offen»).
> 
> ## 1. Einkünfte (Formular 1)
> 
> | Ziff. | Code | Position | Kanton SG | Bund (Orientierung) | Rechenweg / Fundstelle | Status |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb unselbständig | 73'000 | 73'000 | Lohnausweis Ziff. 11 (Nettolohn). Kinderzulage 2'400 ist im Bruttolohn enthalten, daher keine eigene Zeile (Ziff. 3.5 gilt nur bei Direktzahlung durch die Ausgleichskasse). `sg-stg-2025` / Formularstruktur | ☑️ |
> | 4.1 | 146 | Wertschriften/Guthaben | 68 | 68 | Sparzinsen Raiffeisen, Bruttozins ohne VSt. Unter 200 Fr. VSt-frei → Form. 2 Abschnitt B. `sg-form-1-2025__c0006`, `sg-wl-2025__c0122` | ☑️ |
> | 6.1 | 156 | Unterhalt für minderjährige Kinder erhalten | 9'600 | 9'600 | Kinderalimente 12 × 800. Beim Empfänger steuerbar. `sg-wl-2025__c0068` | ☑️ |
> | 6.1 | 154 | Unterhalt für Steuerpflichtige | 0 | 0 | Nadine erhält keine Alimente für sich selbst | – |
> | 7 | 168 | **Total Einkünfte** | **82'668** | 82'668 | 73'000 + 68 + 9'600 | |
> 
> ## 2. Abzüge (Formular 1)
> 
> | Ziff. | Code | Position | Kanton SG | Bund (Orientierung) | Rechenweg / Fundstelle | Status |
> |---|---|---|---|---|---|---|
> | 10.1 | 438 | Berufskosten Nadine (Form. 4 Ziff. 6) | **13'600** | **8'690** | Siehe Unterpositionen unten | ☑️ |
> | 〃 | 〃 | → Fahrkosten Auto (Form. 4 Ziff. 1.3, Codes 404/406) | 8'000 | 3'300 | 32 km × 2 × 220 Tage × 0.70 = 9'856 → Kanton max. 8'000, Bund max. 3'300. Begründung nötig (Punkt 1). `sg-form-4-2025__c0002`, `wert sg 2025 fahrkosten` | ☑️ ⚠️ |
> | 〃 | 〃 | → Verpflegung (Mittagessen, Restaurant) | 3'200 | 3'200 | 15 × 220 = 3'300 → max. 3'200. Entfernung verhindert Mittagessen zu Hause. `sg-wl-2025__c0002` | ☑️ |
> | 〃 | 〃 | → übrige Berufskosten | 2'400 | 2'190 | K: 700 + 10 % × 73'000 = 8'000 → max. 2'400. B: 3 % × 73'000 = 2'190 (min. 2'000, max. 4'000). Nicht kumulierbar mit effektiven Kosten. `sg-wl-2025__c0075` | ☑️ |
> | 12.1 | 200 | Unterhalt Ex-Partner | 0 | 0 | Nadine zahlt nichts | – |
> | 12.2 | 202 | Unterhalt minderjährige Kinder | 0 | 0 | Nadine zahlt nichts. Der Ex-Ehemann deklariert die 9'600 bei sich. | – |
> | 13.1 | 208 | Säule 3a | 7'258 | 7'258 | Bescheinigung 7'258 = Maximum mit 2. Säule. `sg-form-1-2025__c0008` | ☑️ |
> | 13.2 | 218 | Säule 2 inkl. Einkauf | 6'000 | 6'000 | Freiwilliger Einkauf, direkt bezahlt 20.10.2025. Einkaufsberechnung beilegen (Pflicht). `sg-wl-2025__c0086`. **Einkaufsgrenze in der Wiki nicht belegt (⬜)** | ☑️ ⬜ |
> | 14 | 600 | Versicherungsprämien und Sparzinsen | **4'500** | **2'500** | A = KK-Prämien brutto 6'600 − IPV 1'800 + Sparzinsen 68 = **4'868**. K-Maximum: alleinstehend 3'400 + Kind 1'100 = 4'500 → min(4'868; 4'500). B-Maximum: 1'800 + Kind 700 = 2'500. Keine Zuschläge ohne Vorsorge, da 2. Säule und 3a abgezogen. Sachversicherungen (Auto-Haftpflicht/Kasko) sind nicht abziehbar. `sg-form-6-2025__c0001`, `sg-form-6-2025__c0002`, `sg-wl-2025__c0110`| ☑️ |
> | 16.2 | 258 | Kinderbetreuung Drittbetreuung | 8'760 | 8'760 | Kita/Tagesstruktur 9'840 − Mahlzeiten 1'080 = 8'760. K-Max. 26'700, B-Max. 25'800. Form. 10 mit Betreuungsperson beilegen. Bund: nur Betreuung während Arbeitszeit (Punkt 4). `sg-form-1-2025__c0009`, `sg-wl-2025__c0092` | ☑️ |
> | 16.4 | 223 | Berufsorientierte Weiterbildung | 400 | 340 | Excel-Kurs 340 (beruflich bedingt). Kanton: Pauschale 400 ohne Nachweis ist höher → 400. Bund: nur effektive Kosten → 340. `sg-wl-2025__c0094` | ☑️ |
> | 18 | 230 | **Total Abzüge** | **40'518** | **33'548** | K: 13'600 + 7'258 + 6'000 + 4'500 + 8'760 + 400. B: 8'690 + 7'258 + 6'000 + 2'500 + 8'760 + 340 | |
> 
> ## 3. Nettoeinkommen und Reineinkommen
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 20 | 234 | **Nettoeinkommen** | **42'150** | **49'120** | 82'668 − 40'518 bzw. 82'668 − 33'548 |
> | 21.1 | 650/238/240 | Krankheits-/Unfallkosten | **2'757** | **1'144** | Vorkolonne: Zahnarzt 2'750 + KK-Kostenbeteiligung 850 = 3'600. Selbstbehalt K 2 % × 42'150 = 843 → 3'600 − 843 = 2'757. B 5 % × 49'120 = 2'456 → 3'600 − 2'456 = 1'144. `sg-form-1-2025__c0010`, `sg-wl-2025__c0098` |
> | 21.3 | 244 | Freiwillige Zuwendungen | 0 | 0 | Caritas 80 Fr. liegt unter der Schwelle von 100 Fr. → kein Abzug. `sg-wl-2025__c0102` |
> | 22 | 248 | **Reineinkommen** | **39'393** | **47'976** | 42'150 − 2'757 bzw. 49'120 − 1'144 |
> | 23.1 | 252 | Kinder noch nicht schulpflichtig | 0 | 0 | Elias besucht den Kindergarten, und der gilt als Schulpflicht (→ 23.2). |
> | 23.2 | 254 | Kind in Schule/Ausbildung (Elias) | **10'800** | **6'800** | K: 10'800. B: einheitlich 6'800 pro Kind. Der Kinderabzug bleibt bei Nadine, weil sie Elias in ihrem Haushalt betreut; der Ex-Ehemann deklariert dafür Ziff. 12.2. `sg-form-1-2025__c0011`, `sg-wl-2025__c0104` |
> | 23.3 | 256 | Ausbildungskosten Kinder | 0 | 0 | Kita-Kosten gehören zu 16.2, nicht hierher |
> | 24 | 268 | **Steuerbares Einkommen** | **28'593** | **41'176** | 39'393 − 10'800 bzw. 47'976 − 6'800 |
> 
> Bund: zusätzlich Abzug vom Steuerbetrag 263 Fr. pro Kind im Haushalt (Eintrag automatisch, `sg-wl-2025__c0104`).
> 
> ## 4. Vermögen (Formular 2 / Form. 5)
> 
> | Ziff. | Code | Position | Betrag | Rechenweg / Fundstelle | Status |
> |---|---|---|---|---|---|
> | 30.1 | 300 | Wertschriften und Guthaben | **31'500** | Sparkonto Raiffeisen, Saldo 31.12.2025. `sg-form-1-2025__c0012`, `sg-wl-2025__c0121` | ☑️ |
> | 30.4 | 306 | Motorfahrzeuge | **⬜ offen** | Steuerwert des Autos per 31.12.2025 fehlt | ⬜ |
> | 33 | 322 | Total Vermögenswerte | 31'500 (+ Auto) | | |
> | 34 | 504/506 | Schulden | 0 | Keine Schulden angegeben, bitte bestätigen | ⬜ |
> | 35 | 326 | Reinvermögen | 31'500 (+ Auto) | Vermögenswerte − Schulden | |
> | 36.1 | 330 | Freibetrag alleinstehend (K) | 75'000 | Kanton | ☑️ |
> | 36.x | – | Freibetrag Kind (K) | 20'000 | Kanton, für Elias | ☑️ |
> | 37 | 338 | **Steuerbares Vermögen** | **0** | 31'500 − 95'000 → 0. **Bleibt 0, solange der Steuerwert des Autos ≤ 63'500 Fr. ist.** | |
> 
> Die Säule-3a- und Pensionskassen-Guthaben sind bis zur Fälligkeit steuerfrei und werden **nicht** in Ziff. 30 erfasst (`sg-wl-2025__c0107`).
> 
> ## 5. Offen / muss geklärt werden
> 
> 1. **Fahrkosten Auto (größter Hebel, 8'000 Fr. Kanton).** Die Wiki-Regel (StB 39 Nr. 3, `sg-stb-39-3__c0005`) verlangt bei ungünstigem Fahrplan einen zeitlichen Mehraufwand von **mehr als 60 Minuten pro Tag** für Hin- und Rückfahrt zusammen. Die erste ÖV-Verbindung um 06:40 bei Arbeitsbeginn 06:00 zeigt nur ein Fahrplanproblem, noch keinen Zeitnachteil. Nötig: ÖV-Fahrzeit Hin + Rück gegenüber Auto (Fahrplanauszug). Form. 4 Ziff. 1.3 verlangt die Begründung ausdrücklich.
>    - **Falls Mehraufwand ≤ 60 min/Tag:** Fahrkosten entfallen. Dann Kanton Abzüge 32'518, Netto 50'150, Krankheitskosten 2'597, **steuerbares Einkommen K 36'753** (+8'160). Bund Abzüge 30'248, Netto 52'420, Krankheitskosten 979, **steuerbares Einkommen B 44'641** (+3'465).
> 2. **Motorfahrzeug-Steuerwert** per 31.12.2025 (Ziff. 30.4). Bei unbekanntem Wert liegt das steuerbare Vermögen nur solange bei 0, wie er ≤ 63'500 Fr. bleibt.
> 3. **PK-Einkauf 6'000 Fr.:** Einkaufsberechnung der PK beilegen. Die maximal zulässige Einkaufssumme ist in der Wiki nicht belegt (⬜).
> 4. **Kita und Bund:** Die direkte Bundessteuer zieht Drittbetreuung ausserhalb der Arbeitszeit nicht ab (`sg-form-1`-Beachten zu 16.2). Mit Arbeitsbeginn 06:00 ist fraglich, ob die Betreuungszeiten passen. Kanton ist davon nicht betroffen, da der Ausweis vorliegt.
> 5. **Kinderabzug und Alimente:** Bitte bestätigen, dass der Ex-Ehemann die 9'600 Fr. unter Ziff. 12.2 deklariert, weil dann für Elias kein Kinderabzug beim Ex-Ehemann geltend gemacht werden darf. Bei Nadine bleibt der Kinderabzug bestehen.
> 
> ## 6. Nicht zu deklarieren
> 
> | Beleg | Grund |
> |---|---|
> | Motorfahrzeugsteuer 410 | Kein Abzug vorgesehen (in der Wiki nicht als Abzug gefunden, daher «nicht geprüft» gekennzeichnet) |
> | Auto-Haftpflicht/Kasko 1'020 | Motorfahrzeug- und Haftpflicht-Sachversicherungen sind nicht abziehbar (`sg-form-6`, Beachten zu Ziff. 14) |
> | Handy-Abo 720 | Private Lebenshaltung, kein Abzug (nicht in der Wiki belegt) |
> | Kita-Mahlzeiten 1'080 | Verpflegung ist von der Drittbetreuung ausgeschlossen (`sg-wl-2025__c0092`) |
> | Caritas-Spende 80 | Unter der Mindestgrenze von 100 Fr. (Ziff. 21.3) |
> | Prämienverbilligung 1'800 | Kein eigenes Einkommen. Wird in Ziff. 14 als Abzug von den Prämien geführt. |
> | Kinderzulage 2'400 | Ist im Nettolohn 73'000 bereits enthalten. Keine separate Zeile. |
> | Feld F/G Lohnausweis | Nicht angekreuzt, also kein Eintrag |
> | 3a- und PK-Guthaben | Steuerfrei bis zur Fälligkeit (Ziff. 30 nicht betroffen) |
> 
> ## 7. Einzureichen (Belegliste, soweit nicht auf Verlangen)
> 
> - **Lohnausweis 2025:** immer einreichen.
> - **Form. 4 mit Begründung und Fahrplanauszug** (Fahrkosten).
> - **Form. 10** für Kita/Tagesstruktur: Namen der Betreuungsperson, Adressen, bezahlte Beträge, Mahlzeiten separat.
> - **Einkaufsberechnung PK** plus Bescheinigung (immer einzureichen).
> - **Alimente:** bei erstmaliger Geltendmachung Scheidungsurteil/Trennungsvereinbarung beilegen (`sg-wl-2025__c0084`).
> - **Krankenkasse-Leistungsabrechnung** (Pflicht, wenn im Formular 6 darauf verwiesen wird).
> - **Zahnarztrechnung** 2'750 Fr. (auf Verlangen).
> - **Kontoauszug/Zinsausweis** Raiffeisen (bedingt, Bankbeleg mit VSt-Nachweis nur bei VSt-Abzug).
> 
> Hinweis: Die Angaben stammen aus dem Steuer-Wiki (Stand: Kanton SG, Steuerjahr 2025). Der Status ist ☑️ agent-geprüft, Abnahme durch eine Fachperson steht noch aus. Mandantendaten habe ich nicht gespeichert.

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


**Antwort des Agenten** (118.6 s · Tools: 19 Aufrufe steuerwiki__formular, steuerwiki__ablage, steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__rechne):

> ## Ausfüllhilfe TG · Steuerjahr 2025 · Verwitwete Rentnerin, alleinstehend
> 
> Alle Beträge in ganzen Franken (Rundung 4'632.50 → 4'633). Zahlen mit `rechne` geprüft. Die Fundstellen sind agent-geprüft (☑️): Fundstelle geprüft, Abnahme offen.
> 
> ### 1. Einkünfte
> 
> | Ziff./Code | Staat (TG) | Bund | Rechenweg · Fundstelle |
> |---|---|---|---|
> | **3.1** AHV-Rente (Code 130) | 27'000 | 27'000 | 12 × 2'250, 100 % steuerbar. tg-form-01-2025__c0007, tg-wl-2025__c0076 |
> | **3.2** PK-Rente (Code 132) | 10'800 | 10'800 | Bruttobetrag 10'800, 100 %. Rentenbeginn 01.01.2020 liegt nach 2002, daher kein 80 %-Übergangsrecht. tg-wl-2025__c0077 |
> | **4** Wertschriften/Zinsen (Code 150, Form. 2) | 2'160 | 2'350 | Sp. 8 mit VSt: Sparzinsen 250 + Dividenden 2'100 = 2'350. Staat abzüglich Vermögensverwaltungskosten Code 148: 2 ‰ × 95'000 = 190 → 2'160. Bund 0 (nur effektive Depotgebühren belegt, siehe Vorbehalt). tg-form-02-2025__c0005/c0006, tg-wl-2025__c0159 |
> | **8.1** Eigenmietwert (Code 180, Form. 7/8) | 4'840 | 8'920 | Mietwert 20'400. Bruttoertrag Staat 20'400 × (1 − 40 %) = 12'240; Bund 20'400 × (1 − 20 %) = 16'320. Unterhalt effektiv 6'400 + 520 + 480 = 7'400 (Staat: 12'240 − 7'400 = 4'840; Bund: 16'320 − 7'400 = 8'920). Die Pauschale 20 % wäre ungünstiger (Staat 2'448, Bund 3'264), daher effektiv. tg-form-07-2025__c0002, tg-form-08-2025__c0001 |
> | **9** Total Einkünfte (Code 198) | **44'800** | **49'070** | 27'000 + 10'800 + 2'160 + 4'840 bzw. 27'000 + 10'800 + 2'350 + 8'920 |
> 
> ### 2. Abzüge
> 
> | Ziff./Code | Staat | Bund | Rechenweg · Fundstelle |
> |---|---|---|---|
> | **10** Berufsauslagen | – | – | keine Erwerbstätigkeit |
> | **11** Schuldzinsen (Code 290) | 3'150 | 3'150 | Form. 4.1 A: Hypothekarzinsen 2025 (fällig) 3'150, Schuld 180'000 (Zinssatz 1.75 %). Grenze privat = Vermögensertrag + 50'000 = 2'350 + 50'000 = 52'350, eingehalten. tg-form-04-1-2025__c0002, tg-wl-2025__c0173 |
> | **13** Säule 3a | – | – | keine Beiträge, Feld leer lassen |
> | **14** Versicherungsprämien/Sparzinsen (Code 330) | **3'500** | **2'700** | Form. 5.2: KK-Prämie 6'240 (ohne Prämienverbilligung) plus Sparzinsen, Summe über dem Maximum. Maximum Staat alleinstehend 3'500. Bund alleinstehend ohne Säule 2/3a 2'700 (mit 2./3a wäre es 1'800). tg-form-05-2-2025__c0001/c0002 |
> | **19** Total Abzüge (Code 360) | **6'650** | **5'850** | 3'150 + 3'500 bzw. 3'150 + 2'700 |
> 
> ### 3. Einkommensberechnung
> 
> | Ziff./Code | Staat | Bund | Rechenweg · Fundstelle |
> |---|---|---|---|
> | **22** Nettoeinkommen (Code 362) | **38'150** | **43'220** | 44'800 − 6'650 bzw. 49'070 − 5'850 |
> | **23.1** Krankheits-/Unfallkosten (Code 364) | 4'633 | 4'379 | Form. 5.1 A: Selbstbehalt KK 1'000 + Zahnarzt 4'440 + Brille 1'400 = 6'840. Form. 5.1 B: Vergütung Zusatzversicherung 300. A − B = 6'540. Abzug über 5 %-Selbstbehalt: Staat 6'540 − 5 % × 38'150 (1'907.50) = 4'632.50 → 4'633; Bund 6'540 − 5 % × 43'220 (2'161) = 4'379. tg-form-05-1-2025__c0001/c0002 |
> | **23.2** Freiwillige Zuwendungen (Code 366) | 350 | 550 | Form. 6: Krebsliga TG 300 + Pro Senectute TG 250 = 550. Staat: 550 − 200 = 350 (Maximum 8'000, da Netto ≤ 40'000). Bund: 550 (ab 100, Maximum 20 % × 43'220 = 8'644). tg-form-06-2025__c0002, tg-wl-2025__c0220 |
> | **23.3** Liquidationsgewinne | – | – | keine |
> | **24** Reineinkommen (Code 372) | **33'167** | **38'291** | 38'150 − 4'633 − 350 bzw. 43'220 − 4'379 − 550 |
> | **25.3** AHV-/Verwitwetenabzug (Code 388) | 1'000 | – | Staat only. 4'200 − 200 × 16 (volle 1'000er über 16'900) = 1'000. Bund kein Abzug. tg-form-01-2025__c0013, tg-wl-2025__c0116 |
> | **25.1/25.2/25.4**, **28.x** Kinder-/Unterstützungs-/Ehepaarabzüge | – | – | nicht zutreffend (keine Kinder, keine Unterstützten, alleinstehend) |
> | **26** Steuerbares Einkommen (Code 398) | **32'167** | **38'291** | 33'167 − 1'000 bzw. 38'291 |
> 
> ### 4. Vermögen (nur Staat; die Bundessteuer kennt keine Vermögenssteuer)
> 
> | Ziff./Code | Betrag | Rechenweg · Fundstelle |
> |---|---|---|
> | **30.1** Wertschriften und Guthaben (Code 410) | 143'000 | Sparkonto 48'000 + Depot 95'000 (Steuerwerte 31.12.) |
> | **31** Liegenschaft (Code 430) | 410'000 | Steuerwert laut Schätzung. Form. 7 |
> | **33** Total Vermögenswerte (Code 464) | 553'000 | 143'000 + 410'000 |
> | **34** Schulden (Code 466) | 180'000 | Form. 4.1 A: Hypothek per 31.12.2025 |
> | **35** Reinvermögen (Code 468) | 373'000 | 553'000 − 180'000 |
> | **36.2** Freibetrag alleinstehend (Code 472) | 100'000 | tg-form-01-2025 Ziff. 36.2 |
> | **37** Steuerbares Vermögen (Code 498) | **273'000** | 373'000 − 100'000 |
> 
> ### 5. Hilfsblätter
> 
> - **Form. 2 Ziff. 10 (VSt-Rückerstattung):** 35 % × 2'350 = **822.50** (= 87.50 + 735, stimmt mit der Bankbescheinigung überein). Voraussetzung: Wohnsitz TG am 31.12.2025 ✓. Auszahlungskonto (IBAN) auf Seite 1 angeben.
> - **Form. 2 Sp. 7/8/9:** Sparkonto (Kontoauszug) Sp. 8 mit VSt, 250 Bruttozins; Depot (Depotauszug) Sp. 7 Steuerwert 95'000, Sp. 8 Dividenden 2'100.
> - **Form. 4.1 A:** Gläubiger Hypothekarbank mit Adresse, Zinssatz 1.75 %, Schuld 180'000, Zinsen 3'150 (Codes 455/286).
> - **Form. 5.2 A1:** KK-Prämie 6'240 deklarieren (Voraussetzung für den Versicherungsabzug).
> - **Form. 5.1 A:** Kostenbeteiligung 1'000 (Leistungsabrechnung als Nachweis), Zahnarzt 4'440, Brille 1'400 (augenärztliche Verordnung vorhanden).
> - **Form. 6:** Krebsliga TG 300 und Pro Senectute TG 250 einzeln mit Name und Sitz.
> - **Form. 7:** Mietwert 20'400, Steuerwert 410'000. Selbstnutzung am Wohnsitz ✓.
> - **Form. 8 (eine Liegenschaft):** Malerarbeiten Ersatzanstrich 6'400, Gebäudeversicherungsprämie 520, Baumschnitt/Gartenpflege 480. Rechnungen ab 1'000 als Kopie beilegen (Malerarbeiten). Wintergarten 31'000 in Spalte «Anlagekosten/Mehrwert», nicht abziehbar.
> 
> ### 6. Nicht zu deklarieren
> 
> - **Wintergarten-Anbau 31'000:** wertvermehrend, nicht abziehbar (tg-wl-2025__c0233, tg-stv__par-29). Nicht als Unterhalt, nicht im Abzug. Die Veränderung wirkt sich über die amtliche Schätzung aus, nicht über die Steuererklärung.
> - **Hausratversicherung 380 und Privathaftpflicht:** keine Abzugsposition (tg-wl-2025__c0227, Ablage «nein»).
> - **Serafe 335:** keine abzugsfähige Position gefunden. Lebenshaltungskosten sind nicht abziehbar (allgemein tg-wl-2025__c0064). Die Serafe-Gebühr selbst ist in der Suche nicht gesondert belegt.
> - **Handyrechnung:** Lebenshaltungskosten, kein Abzug (Betriebskosten wie Internet gehören zur privaten Lebensführung, tg-wl-2025__c0103).
> - **Sparzinsen 250:** nur einmal in Ziff. 4 als Ertrag. Ob sie zusätzlich in Form. 5.2 A.4 gehören, ändert nichts, da der Versicherungsabzug schon am Maximum liegt.
> - **Krankenkasse-Prämien** gehören nicht in Krankheitskosten (Form. 5.1 Regel), nur in Ziff. 14.
> - **Säule 3a / 2. Säule:** keine Beiträge, nichts zu deklarieren. Das PK-Kapital existiert nicht mehr, da sie eine Rente bezieht.
> 
> ### 7. Offene Punkte und Vorbehalte
> 
> 1. **Gemeinnützigkeit Krebsliga TG und Pro Senectute TG** gegen die Liste geprüfter Institutionen (steuerverwaltung.tg.ch) prüfen. Ohne Anerkennung entfällt Ziff. 23.2.
> 2. **Bund Vermögensverwaltungskosten:** Ohne Gebührenausweis der Bank setze ich 0. Die Kantonspauschale 190 nur mit Vorbehalt übernehmen (Fachperson entscheidet).
> 3. **Bund Gebäudeversicherungsprämie 520:** Im Wiki ist für die Bundesspalte nicht belegt, dass die Prämie als effektiver Unterhalt anerkannt wird. Bei Nichtanerkennung sinkt das Bund-Reineinkommen um 546 auf 37'745 (Ziff. 8.1 Bund 8'400, Ziff. 22 42'700, Ziff. 23.1 Bund 4'405).
> 4. **Ziff. 13.1 (Anschluss 2. Säule):** «nein» ankreuzen, da keine Beiträge. Damit gilt der Bund-Maximalbetrag 2'700 (Ziff. 14).
> 5. **Hypothekarbank:** Name, Adresse und bestätigter Zinssatz fehlen. 1.75 % ist aus 3'150 / 180'000 abgeleitet.
> 6. **Ziff. 25.3:** Die Tabelle in der Wegleitung S. 25 hat eine offensichtliche Unstimmigkeit («36'900–37'689»). Ich habe die Formel angewendet (4'200 − 200 je volle 1'000 über 16'900 = 1'000 bei 33'167). Gegen das amtliche Original prüfen.
> 7. **Steuerwert 410'000** aus der Schätzung und **Mietwert 20'400** aus der Liegenschaftensteuerrechnung 2025 bei der Erfassung gegen die Rechnung abgleichen.
> 8. **Status:** Die meisten Werte sind ☑️ agent-geprüft, die Abnahme durch eine Fachperson ist noch offen.
> 
> Haben Sie eine Belegdatei für die Liegenschaft oder die Bank, dann kann ich die Ablage nach Kategorie `belege-ablage` mit `KATEGORIEN.md` prüfen.

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


**Antwort des Agenten** (152.2 s · Tools: 14 Aufrufe steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__suche, steuerwiki__rechne):

> **AR · Steuerjahr 2025 · Ehepaar, Herisau (Mieter)**
> 
> Die AR-Erklärung hat keine Bundesspalte. Die Steuerverwaltung passt die Bundessteuer automatisch an. Die Bund-Werte unten dienen nur zur Kontrolle.
> 
> ## Offene Punkte vor dem Ausfüllen
> 
> 1. **Person 1, Feld F (Werkbus):** Ich habe keine Fahrkosten angesetzt, weil der Werkbus kein ÖV-Abzug ist (`ar-wl-2025__c0066`-Regel: Feld F → kein Fahrkostenabzug). Ungeklärt ist, ob der Naturalvorteil im Bruttolohn (Ziff. 8) enthalten ist. Das bitte beim Arbeitgeber prüfen.
> 2. **Person 2, Kinderzulagen:** Sie sind im Bruttolohn Ziff. 8 enthalten und fliessen so in den Nettolohn (Ziff. 1.1) ein. Ziff. 3.5 gilt nur für direkt von der Ausgleichskasse ausbezahlte Zulagen.
> 3. **Ziff. 13.2 (Einkauf 4'000):** Die Quellen sind widersprüchlich (⚠️). Der Einkauf ist bereits im Nettolohn abgezogen und wird deshalb nicht doppelt erfasst.
> 4. **Ziff. 16.1 (Verwaltungskosten):** Ich habe die Kantons-Pauschale auf Antrag angesetzt (276). Die Basis umfasst laut Regel auch private Bankkonten. Beim Bund gibt es nur effektive Kosten, und dafür liegen keine Belege vor.
> 5. **Dividenden:** Ich nehme an, dass die Beteiligungen unter 10 % liegen. Sonst greifen Ziff. 4.2 und 16.7 (Teilbesteuerung).
> 6. **Codes der Hauptformularziffern 10.1, 10.2, 13.2, 16.1, 17** sind laut Wiki nicht verifiziert. Vor dem Eintragen am Originalformular kontrollieren.
> 
> ## Einkünfte
> 
> | Ziff. | Inhalt | Code | Kanton | Bund (Kontrolle) | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 1.1 | Nettolohn Person 1 | 100 | 85'300 | 85'300 | Lohnausweis Ziff. 11 (98'000 − 6'860 − 5'840) · `ar-wl-2025__c0035` ☑️ |
> | 1.1 | Nettolohn Person 2 | 102 | 68'200 | 68'200 | 82'000 − 5'740 − 4'060 − 4'000 (Einkauf) · ☑️ |
> | 4.1 | Wertschriftenerträge | 146 | 1'410 | 1'410 | Zins 160 (Sp. B) + Dividende 1'250 (Sp. A) · Form. 2 · `ar-wl-2025__c0128` ☑️ |
> | 7 | Total Einkünfte | 168 | 154'910 | 154'910 | 153'500 + 1'410 · rechne ✅ |
> 
> **Form. 2 (Wertschriftenverzeichnis):** Verrechnungssteuer-Anspruch 35 % × 1'250 = **437.50** (Sp. A). Dieser Betrag wird mit Rappen ausgewiesen, weil das Formular es verlangt.
> 
> ## Abzüge
> 
> **Form. 4 (Berufskosten)**
> 
> | | Person 1 (Kanton / Bund) | Person 2 (Kanton / Bund) |
> |---|---|---|
> | Fahrkosten (Code 400 / 450) | 0 / 0 (Feld F, Werkbus) | ÖV-Abo 1'260 / 1'260 (max. 6'000 / 3'300) |
> | Verpflegung | Feld G, verbilligt (Ziff. 2.2): 220 × 7.50 = 1'650 → Limite **1'600** / 1'600 | Mehrkosten (Ziff. 2.1): 176 × 15 = 2'640 / 2'640 (max. 3'200) |
> | Übrige (Ziff. 3) | Kanton 700 + 10 % × 85'300 = 9'230 → max. **2'400** · Bund 3 % × 85'300 = **2'559** (2'000–4'000) | Kanton 700 + 10 % × 68'200 = 7'520 → max. **2'400** · Bund 3 % × 68'200 = **2'046** |
> | **Total** | **4'000 / 4'159** | **6'300 / 5'946** |
> 
> Die Pauschale für übrige Berufskosten steht jeder unselbständig erwerbenden Person zu (`ar-wl-2025__c0034`). Es gibt keine nicht ereignisbezogenen Pauschalspesen des Arbeitgebers.
> 
> **Übrige Abzüge**
> 
> | Ziff. | Inhalt | Code | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|---|
> | 10.1 | Berufskosten Person 1 | 438 | 4'000 | 4'159 | Form. 4 Total |
> | 10.2 | Berufskosten Person 2 | 488 | 6'300 | 5'946 | Form. 4 Total |
> | 13.1 | Säule 3a Person 1 | – | 7'258 | 7'258 | Max. mit 2. Säule 7'258 (Kanton und Bund) · ☑️ |
> | 13.1 | Säule 3a Person 2 | – | 5'000 | 5'000 | Unter dem Max. |
> | 13.2 | 2. Säule Einkauf | – | 0 | 0 | 4'000 bereits im Nettolohn · ⚠️ |
> | 14 | Versicherungsprämien | 600 | **7'400** | **5'100** | min(A; B). A = KK-Prämien 13'900 + Zins 160 = 14'060. B Kanton = 5'400 + 2 × 1'000, B Bund = 3'700 + 2 × 700 · `ar-form-06-2025__c0002` ☑️ |
> | 16.1 | Verwaltungskosten Wertschriften | – | **276** | 0 | Pauschale auf Antrag: 3 ‰ × 92'000 (Kanton). Bund nur effektiv, keine Belege · `ar-wl-2025__c0003` ☑️ |
> | 16.2 | Kinderbetreuung Lea (Form. 10) | – | **10'200** | **10'200** | 14'400 − Mittagessen 1'800 − Betreuungsbeitrag 2'400 · max. 25'000 / 25'800 · ☑️ |
> | 17 | Zweiverdienerabzug (Person 2 = tieferes Einkommen) | – | **5'200** | **14'100** | Kanton: E = 68'200 − 6'300 − 5'000 (3a) = 56'900 → 10 % = 5'690 → max. 5'200. Bund: E = 68'200 − 5'946 − 5'000 = 57'254 → 50 % = 28'627 → max. 14'100 · `ar-wl-2025__c0004` ☑️ |
> | 18 | Total Abzüge | – | **45'634** | **51'763** | Summe der Ziffern 10–17 · rechne ✅ |
> 
> Der Einkauf von 4'000 wird im Zweiverdienerabzug nicht zusätzlich abgezogen, weil er schon im Nettolohn steckt. Mit einem zweiten Abzug ergäbe sich dasselbe Ergebnis.
> 
> **Nettoeinkommen bis steuerbares Einkommen**
> 
> | Ziff. | Inhalt | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|
> | 20 | Nettoeinkommen | **109'276** | **103'147** | 154'910 − 45'634 / − 51'763 |
> | 21.1 | Krankheitskosten | 0 | 0 | keine Belege |
> | 21.3 | Spenden (Code 550) | **300** | **300** | Krebsliga: ≥ 100 und ≤ 20 % × Nettoeinkommen (21'855 / 20'629) · `ar-wl-2025__c0102` ☑️ |
> | 22 | Reineinkommen | **108'976** | **102'847** | 109'276 − 300 / 103'147 − 300 |
> | 23.2 | Kinderabzug Lea (4 bis 15 J.) | **7'400** | **6'800** | Lea wurde 2025 4 Jahre alt. Stichtag 31.12. · `ar-wl-2025__c0005` ☑️ |
> | 23.3 | Kinderabzug Jonas (Ausbildung, ≥ 15 J.) | **11'600** | **6'800** | Jonas ist 16 und in Ausbildung |
> | 24 | Sozialabzug Ehepaar (nur Bund) | – | **2'800** | Bund-Wert |
> | 24 | **Steuerbares Einkommen** | **89'976** | **86'447** | 108'976 − 19'000 / 102'847 − 13'600 − 2'800 · rechne ✅ |
> 
> Kinderabzug gesamt: Kanton 19'000, Bund 13'600.
> 
> ## Vermögen (nur Kanton)
> 
> | Ziff. | Inhalt | Code | Betrag | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 30.1 | Wertschriften und Guthaben | 300 | **92'000** | Konten 54'000 + Schweizer Aktien 38'000 (Steuerwert) · `ar-wl-2025__c0130` ☑️ |
> | 33 | Total Vermögenswerte | 322 | 92'000 | |
> | 34 | Schulden | 504/506 | 0 | |
> | 35 | Reinvermögen | 326 | 92'000 | |
> | 36.2 | Sozialabzug Ehepaar (Freibetrag 150'000) | 332 | 92'000 | Auf das Vermögen begrenzt |
> | 36.3 | Sozialabzug Kinder (2 × 25'000) | 334 | 0 | Restvermögen ist 0 |
> | 37 | Steuerbares Vermögen | 338 | **0** | |
> 
> Die Vorsorgeguthaben (2. Säule, 3a) gehören nicht zum Vermögen (`ar-wl-2025__c0111`).
> 
> ## Nicht zu deklarieren
> 
> - **Pensionskasse- und 3a-Guthaben:** Sie sind kein Vermögen. Nur die Beiträge erscheinen in Ziff. 13.1 und 13.2.
> - **Kita-Mittagessen 1'800:** Verpflegung ist nicht abziehbar (`ar-wl-2025__c0091`). Deshalb ist es aus den 14'400 herausgerechnet.
> - **Kita-Betreuungsbeitrag 2'400:** Er ist kein Einkommen. Er wird bei Form. 10 von den Kosten abgezogen.
> - **Mitgliederbeitrag Turnverein 120:** Mitgliederbeiträge sind nicht abziehbar (`ar-wl-2025__c0102`, Regel Ziff. 21.3).
> - **Handy-Abo 960:** Es ist Lebenshaltung und hat keine Formularposition. Dafür habe ich keine Fundstelle gefunden.
> - **Steuerschlussrechnung 2024 (9'870):** Sie hat keine Abzugsposition im Formular. Ich habe keine Fundstelle dafür geprüft, deshalb bitte bestätigen.
> - **Mietzins:** Als Mieter besteht kein Eigenmietwert (Ziff. 5), und der Mietzins ist nicht abziehbar.
> 
> ## Was schon abgedeckt ist
> 
> Die Krankenkassenprämien (13'900) sind in Ziff. 14 nur über den Pauschalbetrag berücksichtigt. Die Bankzinsen (160) stehen in Ziff. 4.1. Die Kinderzulagen sind im Nettolohn von Person 2 enthalten.
> 
> Die Angaben zu Abzügen und Ziffern stammen aus dem Steuer-Wiki (AR 2025). Die Einzelwerte sind mit Chunk-IDs belegt und grösstenteils ☑️ agent-geprüft (Abnahme durch eine Fachperson steht noch aus).

