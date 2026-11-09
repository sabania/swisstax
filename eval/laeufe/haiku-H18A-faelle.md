# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 18:47
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


**Antwort des Agenten** (162.2 s · Tools: 30 Aufrufe steuerwiki__formular, steuerwiki__wert, steuerwiki__position, steuerwiki__suche, steuerwiki__rechne, steuerwiki__zeige):

> Ich beginne mit dem Gerüst der Zürcher Steuererklärung 2025 und den Belegen.
> 
> Die Eckwerte sind da. Jetzt die Formularpositionen für Berufsauslagen, Vorsorge, Versicherungen, Kinderbetreuung, Krankheitskosten und Vermögen.
> 
> Die Berufsauslagen sind geklärt. Offen sind noch Verpflegung, Übrige Berufskosten, Wertschriften, Nettoeinkommen, Kinder und die Bundes-Partnerabzüge.
> 
> Die Formularpositionen sind geklärt. Zwei Punkte brauche ich noch belegt: ob die Kinderzulagen im Lohnausweis von Person 2 steuerfrei sind, und wie Telefon- und Hausratkosten zu behandeln sind. Gleichzeitig rechne ich die Totale exakt nach.
> 
> Zwei Formelzeilen waren mit Variablen formuliert und wurden nicht berechnet. Ich rechne sie mit Zahlen nach und prüfe die Kinderzulagen-Frage am Wortlaut.
> 
> **ZH · 2025** · Ehepaar, Winterthur (Mieter), 2 Kinder · Staatssteuer (ZH) und Bundessteuer getrennt.
> 
> **Ergebnis:** Steuerbares Einkommen Staat **66'574**, Bund **64'248** (vor Steuerbetrag). Steuerbares Vermögen ZH **82'000**. Verrechnungssteuer-Rückforderung **336**. Alle Zahlen stammen aus den Formularpositionen des Wiki (Status ☑️ agent-geprüft, Abnahme offen), die Rechnungen sind mit `rechne` geprüft.
> 
> ## 1. Einkünfte
> 
> | Ziff. / Code | Position | Staat | Bund | Rechnung / Fundstelle |
> |---|---|---|---|---|
> | 1.1 / 100 | Nettolohn Person 1 (Marco) | 103'000 | 103'000 | Lohnausweis Ziff. 11 (118'400 − 8'110 − 7'290 − 0) · zh-form-300-2025__c0004 |
> | 1.1 / 101 | Nettolohn Person 2 (Sandra) | 67'200 | 67'200 | Lohnausweis Ziff. 11 (76'800 − 5'260 − 4'340 − 0) · ⚠️ Kinderzulagen, siehe Abschnitt 7 |
> | 4.1 / 150 | Ertrag Wertschriften/Guthaben | 1'140 | 1'140 | Form. 340: Kol. A 960 (Dividenden) + Kol. B 180 (Sparzins ≤ 200, ohne VSt) · zh-wl-2025__c0168 |
> | 4.2 / 151 | Davon qualifizierte Beteiligungen | 0 | 0 | Keine Q-Beteiligung ≥ 10 % angegeben |
> | 7 / 199 | Total Einkünfte | **171'340** | **171'340** | |
> 
> **Form. 340:** Total Steuerwert (Code 400) = 82'000 · VSt-Anspruch (Code 540) = 35 % × 960 = **336** (stimmt mit dem Bankausweis überein) · zh-form-340-2025__c0005
> 
> ## 2. Abzüge
> 
> | Ziff. / Code | Position | Staat | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 11.1 / 220 | Berufsauslagen Person 1 | **10'470** | **9'590** | ÖV-Abo 4'180 (Form. 360 Ziff. 1.1, Code 201; Plafond Staat 5'200, Bund **3'300**) + Verpflegung voll 15 × 220 = 3'300 → Max. **3'200** (Ziff. 2.1 voll, Code 208) + Pauschale 3 % × 103'000 = 3'090 (Form. 360 Ziff. 3) · zh-form-360-2025__c0001/c0003 |
> | 11.2 / 240 | Berufsauslagen Person 2 | **4'036** | **4'036** | Velo-Pauschale 700 (Ziff. 1.2) + Verpflegung verbilligt 176 × 7.50 = 1'320 (Ziff. 2.1 verbilligt, Code 226; Feld G angekreuzt) + Pauschale 3 % × 67'200 = 2'016 |
> | 14.1 / 260 | Säule 3a Person 1 | 7'258 | 7'258 | Max. mit 2. Säule · zh-wl-2025__c0081 · Bescheinigung Form. 21 EDP |
> | 14.2 / 261 | Säule 3a Person 2 | 7'258 | 7'258 | wie oben |
> | 15 / 270 | Versicherungsprämien und Sparzinsen | **8'400** | **5'100** | Teil A: KK-Prämie 15'840 + Sparzins 180 = 16'020 (Form. 365, Code 601/604/606). Teil B: Staat 5'800 + 2 × 1'300 = 8'400; Bund 3'700 + 2 × 700 = 5'100 → **min(A; B)** · zh-form-365-2025__c0002 |
> | 16.1 / 280 | Freiwilliger PK-Einkauf Person 1 | 10'000 | 10'000 | Lohnausweis Ziff. 10.2 = 0, daher nicht doppelt. Keine Kapitalbezüge in 3 Jahren, Sperrfrist kein Thema · zh-wl-2025__c0092 |
> | 16.3 / 283 | Depot-Verwaltung | **94** | 0 | Pauschal min(3 ‰ × 31'200 = 93.60; 6'000), auf Franken gerundet. Bund: nur effektive Kosten belegt, keine Gebührenabrechnung vorhanden → 0 · zh-wl-2025__c0095 |
> | 16.6 / 376 | Fremdbetreuung Kinder | **31'900** | **32'700** | Lena: min(27'300; 25'000 bzw. 25'800) + Noah: min(6'900; …) = 6'900 · zh-stg-2025__par-31-t4 |
> | 17 / 290 | Zweiverdienerabzug | **6'100** | **14'100** | Basis = niedrigeres Erwerbseinkommen nach Berufsauslagen und 3a: 67'200 − 4'036 − 7'258 = **55'906**. Staat: min(55'906; 6'100). Bund: min(55'906; max(27'953; 8'600); 14'100) · zh-wl-2025__c0112 |
> | 12, 13, 16.2, 16.4, 16.5 | Schuldzinsen, Unterhalt, Weiterbildung, behinderungsbedingt, Parteispenden | 0 | 0 | Nicht vorhanden |
> | 18 / 299 | Total Abzüge | **85'516** | **90'042** | |
> 
> ## 3. Nettoeinkommen bis steuerbares Einkommen
> 
> | Ziff. / Code | Position | Staat | Bund | Rechenweg |
> |---|---|---|---|---|
> | 19 | Total Einkünfte | 171'340 | 171'340 | Ziff. 7 |
> | 20 | Total Abzüge | 85'516 | 90'042 | Ziff. 18 |
> | 21 / 310 | **Nettoeinkommen** | **85'824** | **81'298** | 19 − 20 |
> | 22.1 / 320 | Krankheitskosten | **0** | **0** | Gesamt 3'090 (Franchise/Selbstbehalt 1'240 · Code 300; Zahnarzt 1'850 · Code 302). Selbstbehalt 5 %: 4'291.20 (Staat) bzw. 4'064.90 (Bund) → Kosten liegen darunter, kein Abzug · zh-form-370__c0002 |
> | 22.2 / 324 | Gemeinnützige Zuwendungen | 650 | 650 | SRK 400 + UNICEF 250 ≥ 100; Grenze 20 % = 17'164.80 (Staat) bzw. 16'259.60 (Bund) · zh-form-300-2025__c0009 |
> | 23 / 350 | Reineinkommen | 85'174 | 80'648 | 21 − 22.1 − 22.2 |
> | 24.1 / 370 | Kinderabzug Lena (2021) und Noah (2016) | 18'600 | 13'600 | Staat 2 × 9'300 · Bund 2 × 6'800 · zh-stg-2025__par-34 |
> | 24.3 / 365 | Ehegattenabzug | – | 2'800 | Nur Bund · zh-form-300-2025__c0010 |
> | 25 / 390 | **Steuerbares Einkommen** | **66'574** | **64'248** | 23 − 24 |
> 
> **Bund-Steuerbetrag:** Kinderabzug vom Steuerbetrag 2 × 263 = 526 (bund-dbg-2025__art-36-t4). Der Steuerbetrag selbst ist hier nicht berechnet.
> 
> ## 4. Vermögen (nur Staat)
> 
> | Ziff. / Code | Position | Betrag | Fundstelle / Hinweis |
> |---|---|---|---|
> | 30.1 / 400 | Wertschriften und Guthaben | **82'000** | Sparkonto 42'500 + Privatkonto 8'300 + Depot 31'200 (Steuerwert 31.12.) · zh-form-300-2025__c0011 |
> | 33 / 460 | Total Vermögenswerte | 82'000 | |
> | 34 / 470 | Schulden | 0 | Mieter, keine Hypothek |
> | 35 / 490, 37 / 498 | Steuerbares Vermögen | **82'000** | Kein Vermögens-Kinderabzug in ZH · Tarif-Freibetrag nicht abziehen |
> | 40 / 510 | Kapitalleistungen Vorsorge | 0 | Keine Bezüge |
> 
> ## 5. Hilfsblätter (Beilagen)
> 
> - **Form. 360** (je Person): P1 Fahrkosten, Verpflegung voll, Übrige. P2 Velo, Verpflegung verbilligt, Übrige. Zwischentotale und Total 220 / 240.
> - **Form. 365** (Versicherungen): A: 601 KK 15'840 · 604 Sparzins 180 · 606 = 16'020. B: 611 5'800 / 3'700 · 613–615 Kinder. C: Code 270 = 8'400 / 5'100.
> - **Form. 370** (Krankheitskosten): Code 300 = 1'240 · Code 302 = 1'850 · Code 317 = 3'090 · Selbstbehalt 4'291 (Staat) → Abzug 0. Bei 0 nicht zwingend einzureichen.
> - **Form. 340** (Wertschriften): A 960 (Dividenden, Code 539, VSt 540 = 336) · B 180 (Sparkonto, Code 542) · Steuerwert 82'000.
> - **Lohnausweise** beider Personen, **Form. 21 EDP** (3a je 7'258, PK-Einkauf 10'000), **Kita-/Hort-Rechnungen**, **Spendenbescheinigungen**, **Bank-Steuerauszug**.
> 
> ## 6. Nicht zu deklarieren bzw. nicht abziehbar
> 
> - **Hausrat- und Privathaftpflicht 465:** keine Ziff. 15-Kategorie. Der Versicherungsabzug ist mit 16'020 ohnehin ausgeschöpft (Max. 8'400). Keine Wirkung. Zh-form-365-2025__c0001.
> - **Swisscom 1'080:** Lebenshaltungskosten, nicht abziehbar · zh-wl-2025__c0031.
> - **Säule 3a- und PK-Guthaben:** kein steuerbares Vermögen bis zur Fälligkeit, nicht im Wertschriftenverzeichnis aufführen · zh-wl-2025__c0154.
> - **Zahnarzt 1'850 und Kostenbeteiligung 1'240:** Abzug 0, weil unter dem 5 %-Selbstbehalt. Belege aufbewahren.
> - **Verrechnungssteuer 336:** kein Einkommen, nur Rückforderung über Form. 340.
> - **Krankenkassenprämie:** zwar deklarieren (Ziff. 15), aber nicht in Abzug aus Krankheitskosten (Form. 370 Hinweis).
> 
> ## 7. Offene Punkte und Annahmen, bitte prüfen
> 
> 1. **Kinderzulagen Person 2 (4'800 in Lohnausweis Ziff. 8):** Die Steuerfreiheit ist in den Wiki-Chunks nicht eindeutig belegt. Ist sie steuerfrei und im Nettolohn enthalten, sinkt das Einkommen: Staat steuerbar **61'774**, Bund **59'448**. Der Zweiverdienerabzug bleibt gleich. Der Selbstbehalt bleibt bei 0.
> 2. **Mittagessen Person 1 (Bund):** Die Verpflegungspauschale im Bund setzt voraus, dass die Hauptmahlzeit über 10 Fr. kostet (ZH Form. 360 Ziff. 2.1 voll, Hinweis Bund). Liegt sie darunter, entfällt Bund 3'200, steuerbar Bund **61'048**. Die Kosten des Mittagessens sind zu erfragen.
> 3. **Verpflegung Person 2:** Der Abzug 1'320 gilt nur, wenn die Mittagspause keine Heimkehr erlaubt. Wohnort und Arbeitsort sind beide Winterthur. Ist Heimkehr möglich, entfallen 1'320 in beiden Spalten.
> 4. **Hort Noah (6'900):** nur den Betreuungsanteil ansetzen. Verpflegung und Schulgeld sind nicht abziehbar (Form. 300 Ziff. 16.6).
> 5. **Depot-Gebühren:** Die Bundesspalte ist 0, da keine Gebührenabrechnung vorliegt. Liegt eine Abrechnung vor, sind effektive Kosten möglich.
> 6. **Spendenempfänger:** Das Rote Kreuz und UNICEF müssen im Verzeichnis der steuerbefreiten Institutionen ZH stehen (zh-info-spenden). Sonst entfällt der Abzug.
> 7. **Bargeld, Gold, Q-Beteiligungen:** nicht angegeben, daher 0 angenommen.
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


**Antwort des Agenten** (150.7 s · Tools: 28 Aufrufe steuerwiki__formular, steuerwiki__ablage, steuerwiki__position, steuerwiki__suche, steuerwiki__wert, steuerwiki__rechne):

> Ich fange mit dem Gerüst der SG-Erklärung 2025 an und prüfe danach die einzelnen Positionen.
> 
> Das Gerüst steht. Jetzt prüfe ich die einzelnen Positionen mit Fundstellen, zuerst die grossen Brocken.
> 
> Die Kernpositionen sind belegt. Jetzt die Hilfsblätter (Berufskosten, Versicherungen), Säule 3a, Vermögen, Weiterbildung und Spenden.
> 
> Die Kernfelder stehen. Offen sind noch Verpflegung, die Vermögens-Sozialabzüge, Abzugsfähigkeit der Nebenkosten (Motorfahrzeugsteuer, Handy, Kasko) und die Behandlung der Kostenbeteiligung.
> 
> Verpflegung ist bestätigt. Zwei Punkte brauche ich noch: die Vermögens-Sozialabzüge (Ziff. 36) und die Abzugsfähigkeit von Motorfahrzeugsteuer und Handy.
> 
> # SG · Steuerjahr 2025 · Ausfüllhilfe Nadine (Alleinerziehend, 1 Kind)
> 
> Alle Positionen sind im Wiki als ☑️ agent-geprüft markiert: Fundstelle geprüft, Abnahme durch die Fachperson offen. Die Bundesspalte steht separat, weil das SG-Formular für Kanton und Bund nur eine Spalte hat. Die Bundesabweichungen setzt die Steuerbehörde automatisch um.
> 
> ## 1. Übersicht Formularpositionen
> 
> | Ziff. | Code | Position | Kanton SG (CHF) | Bund (CHF) |
> |---|---|---|---|---|
> | 1.1 | 100 | Nettolohn Lohnausweis Ziff. 11 | 73'000 | 73'000 |
> | 4.1 | 146 | Bankzins Sparkonto (Form. 2 Sp. B) | 68 | 68 |
> | 6.1 | 156 | Kinderalimente für Elias (12 × 800) | 9'600 | 9'600 |
> | 7 | 168 | Total Einkünfte | 82'668 | 82'668 |
> | 10.1 | 438 | Berufskosten (Form. 4 Ziff. 6) | 13'600 | 8'690 |
> | 13.1 | 208 | Säule 3a | 7'258 | 7'258 |
> | 13.2 | 218 | Einkauf Pensionskasse | 6'000 | 6'000 |
> | 14 | 600 | Versicherungsprämien und Sparzinsen | 4'500 | 2'500 |
> | 16.2 | 258 | Kinderbetreuung Drittbetreuung | 8'760 | 8'760 ⚠️ |
> | 16.4 | 223 | Weiterbildung (Excel-Kurs) | 400 | 340 |
> | 18 | 230 | Total Abzüge | 40'518 | 33'548 |
> | 20 | 234 | Nettoeinkommen | 42'150 | 49'120 |
> | 21.1 | 240 | Krankheitskosten, Abzug (Vorkolonne Code 650: 3'600) | 2'757 | 1'144 |
> | 21.3 | 244 | Freiwillige Zuwendungen (Caritas 80 < Min. 100) | 0 | 0 |
> | 22 | 248 | Reineinkommen | 39'393 | 47'976 |
> | 23.2 | 254 | Kinderabzug Elias (Kindergarten = Schule) | 10'800 | 6'800 |
> | 24 | 268 | Steuerbares Einkommen | 28'593 | 41'176 |
> | 30.1 | 300 | Wertschriften und Guthaben (Sparkonto) | 31'500 | – |
> | 33 / 35 | 322 / 326 | Total Vermögen / Reinvermögen | 31'500 | – |
> | 36.1 | 330 | Sozialabzug alleinstehend | 75'000 | – |
> | 36.3 | 334 | Sozialabzug je minderjähriges Kind | 20'000 | – |
> | 37 | 338 | Steuerbares Vermögen | 0 | – |
> 
> ⚠️ Bund: Kinderbetreuung nur soweit während der Arbeitszeit, siehe Offene Punkte.
> 
> ## 2. Rechenweg und Fundstellen
> 
> **Einkünfte**
> - **1.1 (Code 100), Nettolohn 73'000.** Bruttolohn 83'500 − AHV/ALV 5'890 − BVG 4'610 = 73'000 (Lohnausweis Ziff. 11). Die Kinderzulage von 2'400 ist im Lohnausweis enthalten und darf nicht zusätzlich in Ziff. 3.5 erscheinen. Feld F und G nicht angekreuzt, daher volle Berufskosten. Fundstelle: sg-form-1-2025__c0004, sg-wl-2025__c0042.
> - **4.1 (Code 146), 68.** Bankzins ≤ Fr. 200, also Spalte B ohne VSt. Verrechnungssteueranspruch 0. Fundstelle: sg-form-2-2025__c0005, sg-wl-2025__c0135.
> - **6.1 (Code 156), 9'600.** Kinderalimente für Elias, der in Nadines Obhut lebt. Beim Empfänger steuerbar, im Formular unter 6.1 für minderjährige Kinder. Fundstelle: sg-form-1-2025__c0006, sg-wl-2025__c0068.
> 
> **Abzüge**
> - **10.1 (Code 438), Berufskosten.**
>   - Fahrkosten: 32 km × 2 × 220 Tage × 0.70 = 9'856. Kanton Max. 8'000, Bund Max. 3'300 (Form. 4 Ziff. 1.3, sg-form-4-2025__c0002).
>   - Verpflegung: min(15 × 220; 3'200) = 3'200 (Form. 4 Ziff. 2.1, sg-form-4-2025__c0003). Mittagessen auswärts, keine Kantine.
>   - Pauschale übrige: Kanton min(700 + 10% × 73'000; 2'400) = 2'400. Bund min(max(3% × 73'000; 2'000); 4'000) = 2'190 (sg-form-1-2025__c0008).
>   - Summe Kanton: 8'000 + 3'200 + 2'400 = 13'600. Bund: 3'300 + 3'200 + 2'190 = 8'690.
> - **13.1 (Code 208), Säule 3a: 7'258** (Kanton und Bund). min(7'258; 7'258). Bescheinigung beilegen (sg-form-1-2025__c0008, sg-wl-2025__c0085).
> - **13.2 (Code 218), PK-Einkauf: 6'000.** Freiwilliger Einkauf, direkt bezahlt am 20.10.2025. Lohnausweis Ziff. 10.2 = 0, daher kein Doppelabzug. Einkaufsberechnung beilegen (sg-form-1-2025__c0008, sg-wl-2025__c0086).
> - **14 (Code 600), Versicherungen und Sparzinsen.** Form. 6 Teil A: A = KK 5'280 + 1'320 + Sparzinsen 68 − Prämienverbilligung 1'800 = 4'868.
>   - Kanton B = alleinstehend 3'400 + Kind 1'100 = 4'500. Abzug min(4'868; 4'500) = **4'500**.
>   - Bund B = alleinstehend 1'800 + Kind 700 = 2'500. Abzug min(4'868; 2'500) = **2'500**.
>   - Der Zuschlag ohne Vorsorge (+500 bzw. +1'100) entfällt, weil 2. Säule und 3a abgezogen werden (sg-form-6-2025__c0001, sg-form-6-2025__c0002).
> - **16.2 (Code 258), Kinderbetreuung: 8'760.** Kita/Tagesstruktur 9'840 − Mahlzeiten 1'080 (separat ausgewiesen, nicht abziehbar). Max. 26'700 Kanton / 25'800 Bund, Elias unter 14 (sg-form-1-2025__c0009, sg-wl-2025__c0092).
> - **16.4 (Code 223), Weiterbildung.** Kanton: höherer Wert aus 340 und Pauschale 400 ohne Nachweis = 400. Bund: min(340; 13'000) = 340. Voraussetzung erfüllt, Nadine ist über 20 (sg-form-1-2025__c0009, sg-wl-2025__c0094).
> - **18 (Code 230), Total Abzüge.** Kanton 13'600 + 400 + 7'258 + 6'000 + 4'500 + 8'760 = 40'518. Bund 8'690 + 340 + 7'258 + 6'000 + 2'500 + 8'760 = 33'548.
> - **20 (Code 234), Nettoeinkommen.** Kanton 82'668 − 40'518 = 42'150. Bund 82'668 − 33'548 = 49'120.
> - **21.1 (Code 240), Krankheitskosten.** Vorkolonne (Code 650) = Zahnarzt 2'750 + Kostenbeteiligung KK 850 = 3'600.
>   - Kanton: 3'600 − 2% × 42'150 (843) = **2'757**.
>   - Bund: 3'600 − 5% × 49'120 (2'456) = **1'144**.
>   - Prämien gehören nicht hierher, sie stehen in Ziff. 14 (sg-form-1-2025__c0010, sg-form-6-2025__c0003).
> - **21.3 (Code 244), Spenden: 0.** Caritas 80 liegt unter dem Mindestbetrag von 100 (sg-form-1-2025__c0010).
> 
> **Reineinkommen und steuerbares Einkommen**
> - **22 (Code 248):** Kanton 42'150 − 2'757 = 39'393. Bund 49'120 − 1'144 = 47'976.
> - **23.2 (Code 254), Kinderabzug:** Kanton 10'800, Bund 6'800. Elias ist seit August 2025 im Kindergarten, also Schule. Bund zusätzlich automatisch Steuerbetrag-Abzug max. 263 (sg-form-1-2025__c0011, sg-form-32-2025__c0006).
> - **24 (Code 268):** Kanton 39'393 − 10'800 = **28'593**. Bund 47'976 − 6'800 = **41'176**.
> 
> **Vermögen (nur Kanton)**
> - **30.1 (Code 300):** Sparkonto 31'500 (sg-form-1-2025__c0012).
> - **33 / 35 (Code 322 / 326):** Reinvermögen 31'500 (Schulden 0).
> - **36.1 (330) 75'000 + 36.3 (334) 20'000.** Festbeträge vom Reinvermögen (sg-form-1-2025__c0013).
> - **37 (Code 338):** max(0; 31'500 − 95'000) = **0**. Bund hat keine Vermögenssteuer.
> 
> ## 3. Nicht zu deklarieren
> 
> - **Kita-Mahlzeiten 1'080.** Verpflegung ist bei der Drittbetreuung nicht abziehbar.
> - **Caritas-Spende 80.** Unter dem Mindestbetrag von 100 (Ziff. 21.3), daher 0.
> - **Motorfahrzeugsteuer 410.** Kein Abzugstatbestand im Formular. Nicht als Abzug erfassen (keine explizite Fundstelle gefunden, Status nicht bestätigt).
> - **Auto-Haftpflicht/Kasko 1'020.** Motorfahrzeug- und Haftpflichtversicherungen sind nach Ziff. 14 nicht abziehbar.
> - **Handy-Abo 720.** Private Lebenshaltung. Die Pauschale übrige Berufskosten (2'400 Kanton / 2'190 Bund) ist höher als die tatsächlichen Kosten, daher kein Gewinn über Ziff. 3.2.
> - **Krankenkassenprämien in Ziff. 21.1.** Sie gehören nach Ziff. 14, nicht in die Krankheitskosten.
> - **Kinderzulage 2'400 als Zusatzposition.** Bereits im Nettolohn Ziff. 1.1 enthalten.
> - **Säule-3a- und PK-Guthaben als Vermögen.** Ansprüche aus 2. Säule und 3a sind bis zur Fälligkeit steuerfrei und nicht zu deklarieren (sg-wl-2025__c0107).
> - **Lohnausweis Ziff. 10.2 (BVG-Einkauf).** Ist 0, kein Eintrag.
> 
> ## 4. Offene Punkte und Annahmen
> 
> 1. **Fahrkosten-Begründung (Ziff. 1.3, Kanton und Bund).** Der Abzug über Auto ist nur bei Begründung zulässig (kein zumutbarer ÖV, Zeitersparnis über 60 Min./Tag, Arbeitgeberverlangen, Arztzeugnis). Die erste ÖV-Verbindung um 06:40 gegen Arbeitsbeginn 06:00 ist ein schwaches Argument, weil die Frage ist, ob sie zumutbar ist. Ohne Begründung gilt nur der ÖV-Betrag, und ÖV-Belege wären nötig. Auswirkung: jeder Franken weniger Fahrkosten erhöht das steuerbare Einkommen etwa 1:1.
> 2. **Kinderbetreuung Bund (16.2).** Bund erlaubt nur Drittbetreuung während der Arbeitszeit. Die Betreuungszeiten der Kita/Tagesstruktur sind nicht angegeben. Der Bundesbetrag von 8'760 ist ein Maximum. Kanton unberührt. Abzugsfähige Stunden prüfen.
> 3. **Kostenbeteiligung 850 (21.1).** Annahme: Der Betrag ist von Nadine selbst getragen und nicht bereits im Zahnarzt-Betrag 2'750 enthalten. Zuordnung zu Person (Nadine oder Elias) bestätigen. Bei Verweis auf Krankenkassen-Zusammenzug ist die Leistungsübersicht Pflicht (sg-form-6-2025__c0003).
> 4. **Kinderalimente (6.1).** Bei erstmaliger Deklaration Scheidungsurteil oder Trennungsvereinbarung und Zahlungsnachweis beilegen (sg-wl-2025__c0084).
> 5. **Kinderabzug Elias (23.2) und Ex-Ehemann.** Der Ex darf die Alimente nur abziehen (12.2), wenn er Elias nicht selbst abzieht. Abstimmen, damit der Kinderabzug nur einmal geltend gemacht wird.
> 6. **Motorfahrzeug (30.4).** Das Auto muss im Vermögen erfasst werden, Anschaffungswert und Jahr fehlen. Steuerwert = Anschaffungswert − 20% pro Jahr. Das steuerbare Vermögen bleibt 0, solange der Steuerwert unter 63'500 liegt (95'000 − 31'500).
> 7. **PK-Einkauf 6'000 (13.2).** Bezug von Vorsorgekapital (WEF) in den letzten drei Jahren? Dann ist der Einkauf nicht abziehbar. Einkaufsberechnung beilegen.
> 8. **Mehrere Belege nur auf Verlangen:** Krankenkassenprämien (Form. 6), Zahnarzt-Rechnung, Excel-Kurs, Kita-Rechnungen (Form. 10, mit Name und Adresse der Betreuungsperson). Aufbewahren.
> 9. **Bank-Steuerauszug:** Komplett bei Formular 2 einreichen, auch wenn er nur Spalte B enthält.
> 
> ## 5. Einreichepflicht (Belege)
> 
> - **Ja, einreichen:** Lohnausweis, Säule-3a-Bescheinigung (Form. 21 EDP), PK-Einkaufsbescheinigung mit Einkaufsberechnung, Bank-Steuerauszug mit Formular 2.
> - **Bedingt:** Kinderalimente (nur bei Erstdeklaration, siehe 4.4), Krankenkassen-Leistungsabrechnung (zwingend, wenn Zusammenzug referenziert wird).
> - **Auf Verlangen:** Krankenkassenprämien, Zahnarzt-Rechnung, Kita-Rechnungen, Excel-Kurs, Fahrzeugausweis.
> 
> Die Berechnungen sind mit `rechne` gegengeprüft. Die Abnahme durch die Fachperson bleibt offen.

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


**Antwort des Agenten** (128.5 s · Tools: 22 Aufrufe steuerwiki__formular, steuerwiki__rechne, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__wert):

> **TG · Steuerjahr 2025** (K = Staats- und Gemeindesteuer, B = direkte Bundessteuer)
> 
> Annahmen: alleinstehend/verwitwet am 31.12.2025, Wohnsitz Frauenfeld, Eigenmietwert selbstgenutzt. Keine Erwerbstätigkeit, keine Beiträge an Säule 2 oder 3a, kein Kinder- oder Unterstützungsabzug. Beträge in ganzen Franken, ausser wo das Formular Rappen verlangt (Form. 2). Alle Summen mit `rechne` geprüft.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Position | Code | K | B | Rechenweg · Fundstelle · Status |
> |---|---|---|---|---|---|
> | 3.1 | AHV-Altersrente | 130 | 27'000 | 27'000 | 12 × 2'250, 100 % steuerbar · tg-form-01-2025__c0007 · ☑️ |
> | 3.2 | PK-Altersrente | 132 | 10'800 | 10'800 | 12 × 900, 100 % (BVG; Rentenbeginn 2020, daher kein 80 %-Übergangsrecht) · tg-form-01-2025__c0007 · ☑️ |
> | 4 | Wertschriften- und Zinserträge | 150 | 2'160 | 2'350 | Form. 2 Ziff. 9 = Bruttoertrag 2'350 − Code 148 (K 190); siehe Abschnitt 3 · ☑️ |
> | 6 | Zwischentotal Einkünfte (1–5) | 175 | 39'960 | 40'150 | 27'000 + 10'800 + Ziff. 4 |
> | 8.1 | Liegenschaft (Nettoerfolg) | 180 | 4'840 | 8'920 | siehe Abschnitt 4 · tg-form-07-2025__c0002, tg-wl-2025__c0225 · ☑️ |
> | 9 | **Total Einkünfte** | 198 | **44'800** | **49'070** | 6 + 8.1 |
> 
> ## 2. Abzüge
> 
> | Ziff. | Position | Code | K | B | Rechenweg · Fundstelle · Status |
> |---|---|---|---|---|---|
> | 11 | Schuldzinsen (Hypothek) | 290 | 3'150 | 3'150 | Form. 4.1 A: Zins 2025 fällig 3'150 (Code 286); Schuld 180'000 (Code 455). Limite Erträge + 50'000 nicht erreicht · tg-form-04-1-2025__c0001, tg-form-01-2025__c0010 · ☑️ |
> | 13.1 | Säule 3a | 314 | – | – | keine Beiträge, Feld leer |
> | 14 | Versicherungsprämien und Sparzinsen | 330 | 3'500 | 2'700 | Form. 5.2: Zeile 1 KK-Prämie 6'240 + Zeile 4 Sparzinsen 250 = A5 6'490 (Code 324). Zulässig = min(A5; B4). K: Alleinstehende 3'500. B: ohne Säule 2/3a 2'700 (Vorbehalt, siehe 6.1) · tg-form-05-2-2025__c0001/__c0002 · ☑️ |
> | 19 | **Total Abzüge** | 360 | **6'650** | **5'850** | 11 + 14 |
> 
> ## 3. Nettoeinkommen und Reineinkommen
> 
> | Ziff. | Position | Code | K | B | Rechenweg · Fundstelle · Status |
> |---|---|---|---|---|---|
> | 20 | Total Einkünfte | | 44'800 | 49'070 | Ziff. 9 |
> | 21 | Total Abzüge | | 6'650 | 5'850 | Ziff. 19 |
> | 22 | **Nettoeinkommen** | 362 | **38'150** | **43'220** | 20 − 21 |
> | 23.1 | Krankheits- und Unfallkosten | 364 | 4'633 | 4'379 | Form. 5.1: A (6'840) − B (300) = 6'540; − 5 % × Ziff. 22 (K 1'907.50; B 2'161). K gerundet 4'632.50 → 4'633 · tg-form-01-2025__c0012, tg-form-05-1-2025__c0004 · ☑️ |
> | 23.2 | Freiwillige Zuwendungen | 366 | 350 | 550 | Form. 6: K = Σ 550 − 200 = 350 (Max. 8'000 bei Netto ≤ 40'000 erfüllt). B = 550 (ab 100, Max. 20 % × 43'220 = 8'644 nicht erreicht) · tg-form-06-2025__c0002 · ☑️ |
> | 24 | **Reineinkommen** | 372 | **33'167** | **38'291** | 22 − 23.1 − 23.2 |
> | 25.3 | Abzug AHV-Rentner/verwitwet (nur K) | 388 | 1'000 | – | 4'200 − 200 × 16 (volle 1'000 über 16'900; 16'267 → 16) = 1'000. Bund: kein Abzug · tg-form-01-2025__c0013, tg-wl-2025__c0116 · ☑️ |
> | 26 | **Steuerbares Einkommen** | 398 | **32'167** | **38'291** | 24 − 25.3 |
> 
> Plausibilität: B liegt höher, weil der Selbstnutzungsabzug beim Bund nur 20 % (K 40 %) beträgt, kein Altersabzug existiert und der Versicherungsabzug tiefer ist.
> 
> ## 4. Liegenschaft (Form. 7 / Form. 8)
> 
> - **Mietwert selbstgenutzt 2025 (indexiert):** 20'400 (K und B). Quelle: Liegenschaftensteuerrechnung. Steuerwert 410'000 (Vermögen, Ziff. 31).
> - **Selbstnutzungsabzug:** K 40 % → steuerbarer EMW 12'240. B 20 % → 16'320. Gilt nur am Wohnsitz dauernd selbstbewohnt (erfüllt). · tg-form-07-2025__c0002 · ☑️
> - **Unterhalt: effektiv gewählt.** Gebäude Baujahr 1986 (über 10 Jahre), also Pauschale 20 %. K: 20 % × 12'240 = 2'448 gegenüber effektiv 7'400. B: 20 % × 16'320 = 3'264 gegenüber effektiv 7'400. Effektiv ist in beiden Ebenen günstiger. · tg-wl-2025__c0238 · ☑️
> 
> Form. 8 (effektive Kosten, je Ebene gleich):
> 
> | Rechnung | Betrag | Behandlung |
> |---|---|---|
> | Malerarbeiten Innenrenovation (Ersatzanstrich) | 6'400 | Unterhalt, abziehbar. Rechnungskopie beilegen (ab 1'000) |
> | Gebäudeversicherungsprämie | 520 | Sachversicherung der Liegenschaft, abziehbar · tg-wl-2025__c0227 |
> | Baumschnitt/Gartenpflege | 480 | Unterhalt Umgebung, abziehbar · tg-wl-2025__c0227 · ☑️ |
> | Neubau Wintergarten-Anbau | 31'000 | **nicht abziehbar**, Spalte «Anlagekosten/Mehrwert». Rechnungskopie beilegen · tg-form-08-2025__c0001 |
> | **Total Unterhalt** | **7'400** | |
> 
> Nettoerfolg: **K 12'240 − 7'400 = 4'840** (Code 180). **B 16'320 − 7'400 = 8'920.**
> 
> ## 5. Vermögen (nur K; der Bund besteuert kein Vermögen)
> 
> | Ziff. | Position | Code | K | Rechenweg |
> |---|---|---|---|---|
> | 30.1 | Wertschriften und Guthaben | 410 | 143'000 | Sparkonto 48'000 + Depot 95'000 (Steuerwerte 31.12.) |
> | 31 | Liegenschaft (Steuerwert) | 430 | 410'000 | Schätzung · Form. 7 |
> | 33 | Total Vermögenswerte | 464 | 553'000 | 143'000 + 410'000 |
> | 34 | Schulden | 466 | 180'000 | Hypothek 31.12. (Form. 4.1 A, Code 455) |
> | 35 | Reinvermögen | 468 | 373'000 | 33 − 34 |
> | 36.2 | Freibetrag alleinstehend (verwitwet) | 472 | 100'000 | fix · tg-form-01-2025__c0016 · ☑️ |
> | 37 | **Steuerbares Vermögen** | 498 | **273'000** | 35 − 36.2 |
> 
> Keine Sozialabzüge auf dem Vermögen (keine Kinder).
> 
> ## 6. Form. 2 (Wertschriftenverzeichnis)
> 
> | Titel | Sp. 7 (Steuerwert 31.12.) | Sp. 8 A (mit VSt, brutto) | VSt 35 % |
> |---|---|---|---|
> | TKB Sparkonto (Bruttozins > 200) | 48'000 | 250.00 | 87.50 |
> | Depot Schweizer Aktien (Dividenden) | 95'000 | 2'100.00 | 735.00 |
> | **Total** | 143'000 | **2'350.00** | **822.50** |
> 
> - **Ziff. 10 (VSt-Rückerstattungsanspruch):** 822.50. Rückerstattung nur bei Wohnsitz TG am 31.12. · tg-form-02-2025__c0006 · ☑️
> - **Code 148 (Vermögensverwaltungskosten):** K = min(2 ‰ × 95'000 = 190; 6'000) = **190**. Bund: nur effektive Depotgebühren belegt; ohne Gebührenausweis 0. · tg-form-02-2025__c0006, tg-wl-2025__c0159 · ☑️
> - **Ziff. 9 → Ziff. 4:** K 2'350 − 190 = 2'160. B 2'350.
> 
> ## 7. Weitere Positionen
> 
> - **Form. 5.1 Krankheitskosten (Ziff. 23.1):**
>   - A1 Kostenbeteiligung (Franchise/Selbstbehalt) gemäss Leistungsabrechnung: 1'000
>   - Zahnarzt (Zeile Zahnarzt, A2–A5): 4'440
>   - Brille (übrige Kosten, A8): 1'400
>   - Total A: 6'840
>   - B1 Vergütung durch Zusatzversicherung: 300
>   - A − B = 6'540
> - **Form. 5.2 (Ziff. 14):** Grund- und Zusatzversicherung als private KV-Prämie netto (Zeile 1, keine Prämienverbilligung) 6'240 · tg-form-05-2-2025__c0001 · ☑️
> - **Hausrat 380:** Nicht abziehbar. Hausratversicherung ist im Formular nicht vorgesehen und in der Wegleitung ausdrücklich ausgeschlossen (tg-wl-2025__c0227).
> 
> ## 8. Nicht zu deklarieren bzw. nicht abziehbar
> 
> **Nicht abziehbar, aber auch nicht separat zu deklarieren:**
> - Wintergarten-Anbau 31'000: Neubau, keine Unterhaltskosten (nur im Form. 8, Spalte Anlagekosten/Mehrwert).
> - Serafe 335, Handyrechnung: Lebenshaltungskosten, keine Formularposition. Die Wiki-Quellen beziehen sich auf Lebenshaltung allgemein; für Serafe gibt es keinen spezifischen Chunk. Das ist nicht zusätzlich belegt.
> - Hausratversicherung 380: siehe oben.
> - Gebäudeversicherung 520 und Gartenpflege 480 sind abziehbar (siehe Form. 8), nicht «nicht zu deklarieren».
> 
> **Nicht zu deklarieren (nicht Einkommen bzw. nicht steuerbar):**
> - Die Verrechnungssteuer selbst ist kein Einkommen; nur der Anspruch 822.50 (Ziff. 10) wird ausgewiesen.
> - Sparkonto- und Depotwerte sind im Vermögen (Ziff. 30.1) zu deklarieren, nicht als Einkommen doppelt.
> 
> ## 9. Offene Punkte
> 
> 1. **Anschluss 2. Säule (Ziff. 13.1 / B4 Bund):** Die Bundesgrenze beträgt 2'700 (ohne Säule 2/3a, angesetzt) oder 1'800. Bei Anschluss «ja» ergibt sich Bund 1'800, Steuerbetrag steigt. Bitte bestätigen. Kanton unverändert (3'500).
> 2. **Zeilennummern Form. 5.1:** Die Zuordnung Zahnarzt/Brille zu A2–A5 bzw. A8 ist aus der Formularbeschreibung abgeleitet. Bitte am Original-Formular gegenprüfen.
> 3. **Bund-Vermögensverwaltungskosten (Code 148):** Null, weil kein Gebührenausweis vorliegt. Falls die Bank Depotgebühren belastet, Ausweis beilegen; der Betrag mindert B-Ziff. 4.
> 4. **Rundung:** Code 364 K = 4'632.50, auf 4'633 gerundet. Ziff. 24 damit 33'167.
> 5. **Nicht angegeben, bitte prüfen:** Bargeld, Motorfahrzeuge, Lebensversicherungen mit Rückkaufswert (Ziff. 30.2–30.4). Hausrat ist als Vermögen steuerfrei (StG TG § 42).
> 6. **Sparzinsen in Form. 5.2 Zeile 4 (250):** Der Abzug ist durch den Höchstbetrag begrenzt, daher ohne Einfluss auf das Ergebnis.
> 7. **Wegleitungstabelle 25.3:** Die WL-Tabellenzeile «36'900–37'689» ist ein Druckfehler. Der Abzug wurde nach Formel berechnet (1'000 bei Reineinkommen 33'167).
> 8. **Form. 2:** Ziffernbezeichnung (17/Code 148) ist in der Wegleitung nicht einheitlich. Massgebend ist Code 148.
> 
> **Belegkopien beilegen:** Malerarbeiten 6'400, Wintergarten 31'000 (Form. 8, Einzelbeträge ab 1'000), Leistungsabrechnung KK (Franchise 1'000), Spendenquittungen nur auf Verlangen (je unter 1'000).
> 
> Nicht im Wiki: nicht geprüft für andere Kantone. Die fachliche Abnahme bleibt bei der Fachperson.

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


**Antwort des Agenten** (157.8 s · Tools: 20 Aufrufe steuerwiki__formular, steuerwiki__ablage, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__wert, steuerwiki__rechne):

> **AR · Steuerjahr 2025** · Ehepaar, Herisau (Mieter), 2 Kinder · Beträge in CHF. Kanton = Staats- und Gemeindesteuer. Bund = Werte zur Kontrolle, weil das AR-Formular keine Bundesspalte hat; die Steuerverwaltung nimmt die Bundesabweichungen automatisch vor (`ar-wl-2025__c0179`).
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg / Fundstelle | Status |
> |---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb Person 1 | 85'300 | 85'300 | Lohnausweis Ziff. 11 Nettolohn (Basis Nettolohn, nicht Brutto), `ar-wl-2025__c0035` | ☑️ |
> | 1.1 | 102 | Haupterwerb Person 2 | 68'200 | 68'200 | Lohnausweis Ziff. 11; 82'000 − 5'740 − 4'060 − 4'000 Einkauf. Kinderzulagen im Lohn sind Teil des Nettolohns (`ar-wl-2025__c0032`) | ☑️ |
> | 4.1 | 146 | Wertschriften- und Guthabenerträge | 1'410 | 1'410 | Dividende 1'250 (Spalte A, VSt 437.50) + Bankzins 160 (Spalte B). Form. 2 → 4.1, `ar-form-02-2025__c0007` | ☑️ |
> | 7 | 168 | Total Einkünfte | **154'910** | **154'910** | 153'500 + 1'410 | |
> 
> Die Verrechnungssteuer-Rückforderung von 437.50 (35 % × 1'250) gehört ins Wertschriftenverzeichnis (Form. 2), nicht ins Einkommen.
> 
> ## 2. Abzüge
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg | Status |
> |---|---|---|---|---|---|---|
> | 10.1 | 438 | Berufskosten Person 1 (Form. 4) | **4'000** | **4'159** | Fahrkosten 0 (Feld F: Sammeltransport, `ar-form-04-2025__c0001`). Verpflegung 1'600 (Feld G: Kantine, halber Abzug 7.50 × 220 = 1'650, Deckel 1'600, `ar-wl-2025__c0002`). Übrige: K 700 + 10 % = 8'530 → Deckel 2'400 (⚠️ siehe Punkt 7.1); B 3 % × 85'300 = 2'559 (min 2'000 / max 4'000) | ☑️ |
> | 10.2 | 488 | Berufskosten Person 2 (Form. 4) | **6'300** | **5'946** | ÖV-Abo 1'260 (tatsächliche Kosten). Verpflegung 15 × 176 = 2'640 (Max 3'200; `ar-form-04-2025__c0007`). Übrige: K 2'400 (Deckel, siehe 7.1); B 3 % × 68'200 = 2'046 | ☑️ |
> | 13.1 | – | Säule 3a | **12'258** | **12'258** | Person 1: 7'258 (Max mit 2. Säule, beide haben BVG). Person 2: 5'000 (unter Max). Wert aus der Formularübersicht; den Chunk habe ich nicht einzeln geöffnet | ☑️ |
> | 13.2 | – | Einkauf 2. Säule | 0 | 0 | 4'000 Einkauf ist bereits im Lohnausweis Ziff. 10.2 abgezogen (Nettolohn 68'200). Nicht doppelt abziehen (Ziff. 13.2 gilt nur «soweit nicht im Lohnausweis abgezogen») | ☑️ |
> | 14 | 600 | Versicherungsprämien | **7'400** | **5'100** | min(A; B). A = KK-Prämie 13'900 + Sparzinsen 160 = 14'060. K-B = 5'400 + 1'000 × 2 Kinder = 7'400. B-B = 3'700 + 700 × 2 = 5'100. Keine Prämienverbilligung. Kinder erfüllen 23.x (`ar-form-06-2025__c0002`, `ar-wl-2025` Ziff. 14) | ☑️ |
> | 16.2 | – | Kinderbetreuung Lea (Kita) | **10'200** | **10'200** | 14'400 − Mittagessen 1'800 − erhaltener Betreuungsbeitrag 2'400 = 10'200. Max 25'000 / 25'800; Lea unter 14, beide Eltern erwerbstätig (`ar-form-10-2025__c0001`, `ar-wl-2025__c0091`) | ☑️ |
> | 17 | – | Zweiverdienerabzug | **5'200** | **14'100** | E_K = 68'200 − 6'300 − 5'000 = 56'900 → 10 % = 5'690 → Max 5'200. E_B = 68'200 − 5'946 − 5'000 = 57'254 → 50 % = 28'627 → Max 14'100 | ☑️ |
> | 18 | – | Total Abzüge | **45'358** | **51'763** | Summe der obigen Positionen | |
> 
> Die Summen wurden mit `rechne` geprüft.
> 
> ## 3. Nettoeinkommen bis steuerbares Einkommen
> 
> | Ziff. | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|
> | 20 | Nettoeinkommen | **109'552** | **103'147** | 154'910 − 45'358 bzw. − 51'763 |
> | 21.1 | Krankheitskosten | 0 | 0 | Keine Belege angegeben |
> | 21.3 | Spenden (Code 550) | **300** | **300** | Krebsliga 300. Min 100, Max 20 % von Ziff. 20 (21'910 / 20'629). `ar-form-05-2025__c0003` |
> | 22 | Reineinkommen | **109'252** | **102'847** | 109'552 − 300 bzw. 103'147 − 300 |
> | 23.2 | Kind Lea (geb. 14.03.2021, 4. bis 15. Altersjahr) | 7'400 | 6'800 | Lea hat das 4. Altersjahr 2025 vollendet, daher nicht mehr 23.1. `ar-wl-2025__c0005` |
> | 23.3 | Kind Jonas (geb. 02.09.2009, Ausbildung) | 11'600 | 6'800 | 16 Jahre, Kantonsschule |
> | 24 | Sozialabzug verheiratet | – | 2'800 | Bund-Abzug für Ehepaare; im Kanton kein separater Abzug (laut Wiki) |
> | 24 | **Steuerbares Einkommen** | **90'252** | **86'447** | K: 109'252 − 7'400 − 11'600. B: 102'847 − 6'800 − 6'800 − 2'800 |
> 
> ## 4. Vermögen (nur Kanton)
> 
> | Ziff. | Position | Betrag | Hinweis |
> |---|---|---|---|
> | 30.1 | Wertschriften und Guthaben (Code 300), Übertrag Form. 2 | 92'000 | Konten 54'000 + Schweizer Aktien 38'000 (Steuerwert). `ar-form-02-2025__c0007` |
> | 33 | Total Vermögenswerte | 92'000 | |
> | 34 | Schulden | 0 | |
> | 35 | Reinvermögen | 92'000 | |
> | 36.2 | Sozialabzug Ehepaar | 150'000 | |
> | 36.3 | Sozialabzug je minderjähriges Kind | 50'000 | 2 × 25'000 (Lea 4 J., Jonas 16 J.) |
> | 37 | **Steuerbares Vermögen** | **0** | max(0; 92'000 − 150'000 − 50'000). Die Sozialabzüge werden in voller Höhe eingetragen |
> 
> Die Säule-3a- und Pensionskassenguthaben gehören nicht ins steuerbare Vermögen, solange sie nicht fällig sind (Wiki-Vermerk unter «Ausfüllregeln»).
> 
> ## 5. Belege beilegen oder bereithalten
> 
> - **Immer einreichen:** Lohnausweise (je Arbeitgeber), Säule-3a-Bescheinigungen (Ziff. 13.1).
> - **Bedingt:** Bank-Steuerauszug, wenn der Gesamtbetrag ins Formular 2 übertragen wird (dann vollständig beilegen).
> - **Auf Verlangen:** Krankenkassen-Prämienbescheinigung, Kita-Rechnungen, ÖV-Abo, Spendenquittung, Pensionskassen-Einkaufsbestätigung.
> 
> ## 6. Nicht zu deklarieren bzw. nicht abziehbar
> 
> - **Turnverein 120:** Mitgliederbeitrag, nicht abziehbar (Ziff. 21.3, Regel: «Mitgliederbeiträge nicht abziehbar»).
> - **Handy-Abo 960:** private Lebenshaltung, kein Einzelabzug. Die Pauschale für übrige Berufskosten deckt diese Kosten nicht gesondert ab.
> - **Schlussrechnung Steuern 2024, 9'870:** nicht abziehbar. Das Wiki enthält dazu keine Fundstelle; ich stütze mich auf den allgemeinen Grundsatz, dass Steuern kein Abzug sind. Bitte am Originalformular bestätigen.
> - **Kita-Mittagessen 1'800:** nicht Betreuungskosten (Ziff. 16.2).
> - **Lohnausweis Ziff. 9 (AHV/ALV) und Ziff. 10.1 (BVG):** bereits im Nettolohn enthalten. Nicht nochmals abziehen.
> - **Bankzins und Dividenden:** nicht als Vermögen doppelt erfassen; sie stehen unter Ziff. 4.1 (Einkommen) und 30.1 (Vermögen).
> - **Privatanteil Werkbus (Feld F) und Kantine (Feld G):** kein Fahrkostenabzug für Person 1. Feld G reduziert den Verpflegungsabzug auf den halben Satz.
> 
> ## 7. Offene Punkte und Annahmen
> 
> 1. **Übrige Berufskosten Kanton (⚠️ wichtig):** Der Wiki-Text «Fr. 700 zuzüglich 10 % des Nettolohns, max. Fr. 2'400» lässt offen, ob der Deckel die Gesamtpauschale oder nur den 10-%-Teil begrenzt. Ich habe den Gesamtdeckel (2'400 je Person) angewendet. Gilt die zweite Lesart, steigt der Abzug je Person um 700 und das steuerbare Einkommen Kanton sinkt um 1'400. Bitte am Original prüfen (`ar-wl-2025__c0002`).
> 2. **Jonas' eigene Einkünfte:** Ich habe 0 angenommen. Ab 18'000 entfällt der Kinderabzug.
> 3. **Person 2, Verpflegung:** Ich habe angenommen, dass die Hauptmahlzeit wegen Entfernung und Pausenlänge nicht zu Hause eingenommen werden kann (Herisau–St. Gallen). Der Pauschalabzug von 15 pro Tag setzt das voraus.
> 4. **Person 2, ÖV-Abo:** Ich habe angenommen, dass es nur für den Arbeitsweg genutzt wird.
> 5. **Codes:** Die Hauptformular-Codes für Ziff. 10.1/10.2, 14, 16.2 und 23 sind im Wiki nicht verifiziert. Die Ziffern stimmen; die Codes bitte am Original prüfen. Codes 438/488 stammen aus dem Hilfsblatt Form. 4.
> 6. **Bankguthaben:** Ich habe die 54'000 als Saldo per 31.12. inklusive Zinsguthaben angenommen.
> 7. **Kanton ohne Ehepaar-Sozialabzug:** Laut Wiki gibt es im Kanton AR bei Ziff. 24 keinen separaten Ehepaarabzug. Der Bund setzt 2'800 an.
> 
> Die Fachbeurteilung und die endgültige Einreichung bleiben bei der zuständigen Fachperson.

