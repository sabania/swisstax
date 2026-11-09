# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 15:34
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


**Antwort des Agenten** (155.3 s · Tools: 24 Aufrufe steuerwiki__formular, steuerwiki__ablage, steuerwiki__position, steuerwiki__suche, steuerwiki__wert):

> Ich beginne mit dem vollständigen Formular ZH 2025 als Gerüst und ziehe danach die einzelnen Positionen.
> 
> Das Gerüst und die Belegablage stehen. Jetzt hole ich die Details zu den einzelnen Positionen, die dieser Fall braucht.
> 
> Die Kernpositionen sind geklärt. Mir fehlen noch Verpflegung, Spenden, Kinderabzug, Zweiverdienerabzug, Vermögen und Hausrat/Haftpflicht. Diese hole ich jetzt.
> 
> Die meisten Positionen sind geklärt. Offen sind noch die Zinsen-Zeile 604, Haftpflicht/Hausrat, Telefonkosten, Einkaufs-Grenze und 3a/PK-Guthaben im Vermögen. Ich prüfe diese Punkte zuletzt.
> 
> # Ausfüllhilfe Steuererklärung ZH 2025, Ehepaar Marco und Sandra, Winterthur
> 
> Beträge in CHF. **K** = Staatssteuer Kanton ZH, **B** = Bundessteuer. Die Werte sind Rechenvorschläge aus dem Steuer-Wiki und den gelieferten Belegen. Die fachliche Abnahme bleibt bei der Fachperson. Die Fundstellen-Status: ☑️ = Fundstelle agent-geprüft, Abnahme offen.
> 
> ## Ergebnis auf einen Blick
> 
> | Position | K | B |
> |---|---|---|
> | Einkünfte gesamt (Ziff. 19/7) | 171'340 | 171'340 |
> | Abzüge gesamt (Ziff. 18) | 85'422 | 90'042 |
> | Nettoeinkommen (Ziff. 21) | 85'918 | 81'298 |
> | Krankheitskosten (Ziff. 22.1) | 0 | 0 |
> | Spenden (Ziff. 22.2) | 650 | 650 |
> | Reineinkommen (Ziff. 23) | 85'268 | 80'648 |
> | Sozialabzüge (Ziff. 24) | 18'600 | 16'400 |
> | Steuerbares Einkommen (Ziff. 25/27) | **66'668** | **64'248** |
> | Steuerbares Vermögen (Ziff. 35/37) | **0** | – |
> 
> ## 1. Einkünfte
> 
> | Ziff./Code | Position | Betrag | Rechenweg | Fundstelle / Status |
> |---|---|---|---|---|
> | 1.1 · Code 100 | Marco, Haupterwerb | 103'000 (K/B) | Lohnausweis Ziff. 11. Kontrolle: 118'400 − 8'110 − 7'290 − 0 = 103'000 | zh-form-300-2025__c0004 · ☑️ |
> | 1.1 · Code 101 | Sandra, Haupterwerb | 67'200 (K/B) | Lohnausweis Ziff. 11. Kontrolle: 76'800 − 5'260 − 4'340 − 0 = 67'200. Die Kinderzulagen von 4'800 sind im Bruttolohn enthalten und nicht separat zu erfassen. | zh-form-300-2025__c0004 · ☑️ |
> | 3.4 | Kinder-/Familienzulagen direkt von Ausgleichskasse | 0 | Keine Bescheinigung vorhanden. Die Zulagen laufen über den Lohn. | zh-wl-2025__c0055 · ☑️ |
> | 4.1 · Code 150 | Wertschriften- und Guthaben-Ertrag | 1'140 (K/B) | Kol. A 960 (Depot, VSt 336) + Kol. B 180 (Sparkonto ohne VSt). Privatkonto 0. | zh-form-300-2025__c0006 · ☑️ |
> | 4.2 · Code 151 | Qualifizierte Beteiligungen ≥10 % | 0 | Keine Angabe dazu. Bitte bestätigen, sonst Teilbesteuerung prüfen. | ⬜ offen |
> 
> ## 2. Abzüge (Ziff. 11–17)
> 
> ### Ziff. 11.1 Marco (Code 220) und 11.2 Sandra (Code 240), Form. 360
> 
> | Form. 360 | Marco K | Marco B | Sandra K | Sandra B | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | Ziff. 1.1 ÖV-Abo (201/221) | 4'180 | 3'300 | – | – | Abo Winterthur–Zug, K max 5'200, B max 3'300 | zh-form-360-2025__c0001 · ☑️ |
> | Ziff. 1.2 Velo-Pauschale (202/222) | – | – | 700 | 700 | Sandra fährt ständig mit dem Velo. Pauschale gilt für K und B. | zh-form-360-2025__c0001 · ☑️ |
> | Ziff. 2.1 Verpflegung (206/208) | 3'200 | 3'200 | 1'320 | 1'320 | Marco: voll 15 × 220 = 3'300, begrenzt auf 3'200/Jahr. Sandra: Feld G angekreuzt, also verbilligt 7.50 × 176 = 1'320 | zh-form-360-2025__c0003 · ☑️ |
> | Ziff. 3 Übrige (212/232) | 3'090 | 3'090 | 2'016 | 2'016 | 3 % des Nettolohns, Minimum 2'000, Maximum 4'000 | zh-form-360-2025__c0004 · ☑️ |
> | **Total Ziff. 6** | **10'470** | **9'590** | **4'036** | **4'036** | | |
> 
> - Marco ist keine Verpflegung über Feld G abzugsfähig, weil Feld G bei ihm leer ist. Das Mittagessen im Restaurant wird voll abgezogen.
> - Fahrkosten-Plafond Bund 3'300 gilt für Marco. Kanton 5'200 reicht.
> 
> ### Ziff. 14.1/14.2 Säule 3a (Codes 260/261, Form. 21)
> 
> | Person | K | B | Rechenweg | Fundstelle |
> |---|---|---|---|---|
> | Marco | 7'258 | 7'258 | Mit 2. Säule: max. 7'258 | zh-wl-2025__c0081 · ☑️ |
> | Sandra | 7'258 | 7'258 | Mit 2. Säule: max. 7'258 | zh-wl-2025__c0081 · ☑️ |
> 
> Total Ziff. 14: 14'516 (K/B). Beide haben BVG-Beiträge im Lohnausweis (Ziff. 10.1).
> 
> ### Ziff. 15 Versicherungsprämien (Code 270), Form. 365
> 
> | Teil | K | B | Rechenweg |
> |---|---|---|---|
> | Teil A Ziff. 1: Krankenversicherungsprämien (601) | 15'840 | 15'840 | Grund- und Zusatz. Keine Prämienverbilligung, also Code 605 = 0. |
> | Teil B Ziff. 1: Ehepaar mit 2./3a | 5'800 | 3'700 | Marco und Sandra haben 2. Säule bzw. 3a |
> | Teil B Ziff. 3: je Kind | 2'600 | 1'400 | 2 Kinder × (1'300 K / 700 B) |
> | Teil B Summe | 8'400 | 5'100 | |
> | **Teil C: Minimum von A und B** | **8'400** | **5'100** | |
> 
> Fundstelle: zh-form-365-2025__c0001 und __c0002 · ☑️
> 
> ### Ziff. 16.1 2. Säule, Einkauf (Code 280)
> 
> | Person | K | B | Fundstelle |
> |---|---|---|---|
> | Marco, freiwilliger Einkauf (selbst überwiesen 14.11.2025) | 10'000 | 10'000 | zh-wl-2025__c0092 · ☑️ |
> 
> - Lohnausweis Ziff. 10.2 ist 0. Es gibt also keinen Doppelabzug.
> - Kein Kapitalbezug in den letzten drei Jahren, daher greift die Sperrfrist nicht.
> - Offen: Der Einkaufsbetrag muss mit dem Einkaufspotenzial aus dem Vorsorgeausweis abgeglichen werden. Das Wiki nennt dafür keine Grenze.
> 
> ### Ziff. 16.6 Fremdbetreuung (Code 376), Lena und Noah
> 
> | Kind | Kosten | K | B | Rechenweg |
> |---|---|---|---|---|
> | Lena (4 J.), Kita | 27'300 | 25'000 | 25'800 | min(Kosten; 25'000 K / 25'800 B) |
> | Noah (9 J.), Hort/Tagesstruktur | 6'900 | 6'900 | 6'900 | unter Max. |
> | **Total** | | **31'900** | **32'700** | |
> 
> Fundstelle: zh-form-300-2025__c0008 und zh-stg-2025__par-31-t4 · ☑️. Die Verordnung nennt noch 10'400. Für 2025 gilt laut Formular und StG der Betrag 25'000.
> 
> ### Ziff. 17 Sonderabzug Zweiverdiener (Code 290)
> 
> - Basis ist das niedrigere verbleibende Erwerbseinkommen. Das ist Sandra: 67'200 − 4'036 (Berufsauslagen) − 7'258 (3a) = **55'906**.
> - K: min(55'906; 6'100) = **6'100**.
> - B: 50 % × 55'906 = 27'953, begrenzt auf max. 14'100 = **14'100**.
> - Fundstelle: zh-form-300-2025__c0008 · ☑️
> 
> ### Ziff. 18 Total Abzüge
> 
> | | K | B |
> |---|---|---|
> | 11.1/11.2 | 14'506 | 13'626 |
> | 14.1/14.2 | 14'516 | 14'516 |
> | 15 | 8'400 | 5'100 |
> | 16.1 | 10'000 | 10'000 |
> | 16.6 | 31'900 | 32'700 |
> | 17 | 6'100 | 14'100 |
> | **Total** | **85'422** | **90'042** |
> 
> ## 3. Nettoeinkommen und Ziff. 22
> 
> - **Ziff. 21 Nettoeinkommen:** K = 171'340 − 85'422 = **85'918**. B = 171'340 − 90'042 = **81'298**.
> - **Ziff. 22.1 Krankheitskosten (Code 320):** Auslagen 3'090 (Zahnarzt 1'850, Selbstbehalt 1'240). Selbstbehalt 5 % = K 4'296 / B 4'065. Die Auslagen liegen darunter, daher **Abzug 0** (K und B). Fundstelle: zh-form-370__c0002 und zh-form-300-2025__c0009 · ☑️
> - **Ziff. 22.2 Spenden (Code 324):** Rotes Kreuz 400 + UNICEF 250 = 650. Minimum 100 erfüllt. Maximum 20 % des Nettoeinkommens = 17'184 K / 16'260 B, nicht begrenzend. Fundstelle: zh-form-300-2025__c0009 und zh-wl-2025__c0122 · ☑️
> 
> ## 4. Sozialabzüge (Ziff. 23–27)
> 
> | Ziff./Code | K | B | Rechenweg | Fundstelle |
> |---|---|---|---|---|
> | 24.1 Kinder im Haushalt (370) | 18'600 | 13'600 | 2 × (9'300 K / 6'800 B), Lena und Noah | zh-wl-2025__c0126 · ☑️ |
> | 24.3 Ehegatten (365) | – | 2'800 | nur Bund | zh-form-300-2025__c0009 · ☑️ |
> | 24.2 Unterstützte Personen | 0 | 0 | keine | |
> 
> - **Reineinkommen (Ziff. 23, Code 350):** K = 85'918 − 0 − 650 = **85'268**. B = 81'298 − 0 − 650 = **80'648**.
> - **Steuerbares Einkommen (Ziff. 25/27, Code 390/398):** K = 85'268 − 18'600 = **66'668**. B = 80'648 − 16'400 = **64'248**.
> 
> ## 5. Vermögen (Ziff. 30–37)
> 
> | Ziff./Code | Betrag | Rechenweg |
> |---|---|---|
> | 30.1 Wertschriften und Guthaben (400) | 82'000 | Depot 31'200 + Sparkonto 42'500 + Privatkonto 8'300 |
> | 33 Total Vermögenswerte (460) | 82'000 | |
> | 37 Freibetrag verheiratet K (498) | 159'000 | 82'000 liegt darunter |
> | **35/37 Steuerbares Vermögen K** | **0** | Keine Vermögenssteuer nach den bekannten Werten. Fundstelle: zh-form-340-2025__c0005 · ☑️ |
> 
> - Bund kennt keine Vermögenssteuer.
> - **Offen:** Die Vorsorgeguthaben (3a-Konten beider Personen und PK-Guthaben Marco) per 31.12.2025 fehlen. Ebenso fehlen Motorfahrzeuge und Bargeld. Mit Spielraum von rund 77'000 bis zum Freibetrag reicht es vermutlich, aber die Werte sind zu bestätigen.
> 
> ## 6. Verrechnungssteuer-Rückerstattung
> 
> - Form. 340 Code 540: 35 % × Kol. A (960) = **336**.
> - Der Anspruch wird mit der Steuererklärung über das Wertschriftenverzeichnis beantragt, mit IBAN.
> - Fundstelle: zh-form-340-2025__c0005 · ☑️
> 
> ## 7. Nicht zu deklarieren oder nicht abziehbar
> 
> | Beleg | Entscheid | Begründung |
> |---|---|---|
> | Kinderzulagen Sandra (4'800) | Nicht separat unter 3.4 | Sie sind bereits im Lohn (Ziff. 8/11) enthalten |
> | Zahnarzt 1'850 und KK-Selbstbehalt 1'240 | Kein Abzug, nicht als Abzug in Form. 370 eintragen | Unter dem 5-%-Selbstbehalt (Ziff. 22.1). Belege aufbewahren |
> | KK-Prämien 15'840 | Ja, unter Ziff. 15 (Form. 365 Code 601) | Keine Krankheitskosten, aber als Prämie abzugsfähig |
> | Swisscom 1'080 | Nicht abziehbar | Lebenshaltungskosten (zh-zstb-30-3__c0018 nennt Telefonabonnement als nicht abzugsberechtigt. Die Fundstelle bezieht sich auf Liegenschaften, daher nur als Hinweis.) |
> | Hausrat und Privathaftpflicht 465 | Nicht abziehbar | Das Formular kennt dafür keine Position. Die Codes 601–604 erfassen nur Kranken-, Unfall-, Lebens-/Rentenprämien und Sparzinsen. Eine Fundstelle, die diese Prämien ausdrücklich abzugsfähig macht, habe ich nicht gefunden. |
> | Sparkonto-Zins 180 | Ertrag Kol. B, nicht als Abzug | Ob zusätzlich Code 604 gilt, ist im Wiki nicht eindeutig. Auf das Ergebnis hat es keinen Einfluss, weil Teil A über dem Maximum von Teil B liegt. |
> | Privatkonto (Zins 0) | Keine Erfassung | Keine Erträge |
> | Kinderbetreuung-Verpflegungsanteil | Nicht abziehbar | Verpflegung ist nicht betreuungsbedingt. Die Kita-Verpflegung wird von den Eltern mitgegeben. Beim Hort ist der Anteil zu prüfen. |
> | Velo-Fahrkosten Marco | Nicht relevant | Marco fährt ÖV, Velo nur bei Sandra |
> | Auto-km | Nicht geltend | Kein Auto-Anspruch |
> 
> ## 8. Offene Punkte vor dem Ausfüllen
> 
> 1. **Personalrestaurant Sandra (Bund):** Der Bund gewährt den halben Verpflegungsabzug nur, wenn die Hauptmahlzeit mehr als 10 Fr. kostet. Den Preis bitte nennen. Kanton bleibt bei 1'320.
> 2. **Pauschale Sandra (Bund):** Die Bundeswegleitung verlangt eine angemessene Kürzung bei Teilzeit. Ob sie hier greift, ist offen. Der Bundesbetrag 2'016 steht daher unter Vorbehalt.
> 3. **Vorsorge-Vermögen:** 3a- und PK-Guthaben per 31.12.2025 sowie Motorfahrzeuge und Bargeld fehlen.
> 4. **Einkauf Marco:** Einkaufspotenzial aus dem Vorsorgeausweis abgleichen.
> 5. **Hort-Rechnung Noah:** Verpflegungsanteil ausweisen, falls enthalten.
> 6. **Qualifizierte Beteiligungen:** Bestätigen, dass keine Beteiligung ≥10 % besteht.
> 7. **Zahlungsnachweis:** Kita- und Hort-Rechnungen müssen 2025 bezahlt sein. Die Aufstellung mit Empfängern ist unaufgefordert beizulegen (Ziff. 16.6).
> 8. **Lohnausweis-Regeln:** Die Hinweise zu Feld F/G stammen aus der Wegleitung 2026, da für 2025 keine Fassung im Wiki liegt.
> 
> ## 9. Belege für die Einreichung
> 
> Die Einreichung richtet sich nach der Belegliste:
> 
> - **Einzureichen (ja):** Lohnausweise beider Personen, PK-Bescheinigung Einkauf, Säule-3a-Bescheinigungen, Bank-Steuerauszug ZKB.
> - **Bei Abzug beilegen:** Krankenkassen-Prämienbescheinigung (Form. 365), Spendenliste, Aufstellung der Betreuungskosten.
> - **Bedingt:** Krankenkassen-Leistungsabrechnung (nur bei Krankheitskostenabzug, hier nicht nötig), Velo- und ÖV-Nachweise auf Verlangen.
> 
> Keine Belege verlangt werden für: Swisscom, Hausrat- und Privathaftpflicht-Prämien.

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


**Antwort des Agenten** (157.1 s · Tools: 34 Aufrufe read, steuerwiki__formular, steuerwiki__beleg, steuerwiki__position, steuerwiki__wert):

> # Ausfüllhilfe Steuererklärung SG 2025: Nadine (Alleinerziehend, Elias 5 J.)
> 
> **Mandant:** Nadine, 38, alleinerziehend, Wohnsitz Toggenburg SG am 31.12.2025 · **Kanton:** SG · **Steuerjahr:** 2025 · **Formular:** SG Steuererklärung 2025, Formular 1 + Hilfsblätter 2, 4, 6, 10
> 
> Das SG-Formular hat eine Spalte für Kanton und Bund. Die Bundesbeträge stehen deshalb in der Spalte «Bund», die der Bund automatisch übernimmt. Unsichere Annahmen sind unter «Offene Punkte» aufgeführt. Die fachliche Verantwortung bleibt bei der Fachperson.
> 
> Legende Status: ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen) · ⚠️ Annahme/strittig
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg / Beleg | Fundstelle | Status |
> |---|---|---|---|---|---|---|---|
> | 1.1 | 100 | Haupterwerb unselbständig | 73'000 | 73'000 | Nettolohn Lohnausweis Ziff. 11 (83'500 − 5'890 − 4'610) | Beleg `lohnausweis` | ☑️ |
> | 4.1 | 146 | Wertschriften/Guthaben | 68 | 68 | Sparzins, Kolonne B (ohne VSt, unter 200 Fr.) | sg-form-1-2025__c0006 | ☑️ |
> | 6.1 | 156 | Unterhalt für minderjährige Kinder erhalten | 9'600 | 9'600 | 12 × 800 Kinderalimente, steuerbar beim Empfänger | sg-form-1-2025__c0006; sg-wl-2025__c0068 | ☑️ |
> | 7 | 168 | **Total Einkünfte** | **82'668** | **82'668** | 73'000 + 68 + 9'600 | | |
> 
> Der Kinderzulage von 2'400 ist im Bruttolohn (Ziff. 8) und damit im Nettolohn enthalten. Sie darf nicht zusätzlich als Familienzulage erfasst werden.
> 
> ## 2. Abzüge
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg | Fundstelle | Status |
> |---|---|---|---|---|---|---|---|
> | 10.1 | 438 | Berufskosten Person 1 (Total Form. 4 Ziff. 6) | **13'600** | **8'690** | siehe Unterpositionen unten | Form. 4; sg-form-1-2025__c0008 | ☑️ |
> | ↳ 1.3 | 404/406 | Fahrkosten Auto | 8'000 | 3'300 | 64 km/Tag × 220 Tage × 0.70 = 9'856 → Maximum 8'000 (Kanton) / 3'300 (Bund) | sg-form-4-2025__c0002; sg-wl-2025__c0077 | ☑️ ⚠️ Begründung |
> | ↳ 2.1 | 408 | Mehrkosten auswärtige Verpflegung | 3'200 | 3'200 | 15 × 220 = 3'300 → Jahresmaximum 3'200 | sg-form-4-2025__c0003 | ☑️ ⚠️ Annahme |
> | ↳ 3.1 | 418 | Pauschale übrige Berufskosten | 2'400 | 2'190 | Kanton: 700 + 10 % × 73'000 = 8'000 → Maximum 2'400. Bund: 3 % × 73'000 = 2'190 (Min. 2'000, Max. 4'000) | sg-wl-2025__c0080; bund-bkv-2025__anhang-1 | ☑️ |
> | 13.1 | 208 | Säule 3a | 7'258 | 7'258 | min(Einzahlung 7'258; Max. 7'258) | sg-wl-2025__c0085 | ☑️ |
> | 13.2 | 218 | BVG-Einkauf (direkt bezahlt 20.10.) | 6'000 | 6'000 | Lohnausweis Ziff. 10.2 = 0, daher voll hier | sg-form-1-2025__c0008; sg-wl-2025__c0086 | ☑️ ⚠️ Sperrfrist |
> | 14 | 600 | Versicherungsprämien und Sparzinsen | 4'500 | 2'500 | A = 6'600 − 1'800 (IPV) + 68 = 4'868. B Kanton: 3'400 + 1'100 (Kind) = 4'500. B Bund: 1'800 + 700 (Kind) = 2'500. min(A; B) | sg-form-1-2025__c0009; sg-form-6-2025__c0002 | ☑️ |
> | 16.2 | 258 | Kinderbetreuung Drittbetreuung (Elias) | 8'760 | 8'760 | 9'840 − 1'080 Mahlzeiten (nicht abziehbar) = 8'760; Max. 26'700 / 25'800 | sg-form-1-2025__c0009; sg-wl-2025__c0092 | ☑️ ⚠️ Bund-Zeit |
> | 16.4 | 223 | Berufsorientierte Weiterbildung (Excel-Kurs) | 400 | 340 | Kanton: höherer Wert aus 340 effektiv und 400 Pauschale ohne Nachweis (nur Kanton). Bund: nur effektiv 340 | sg-form-1-2025__c0009; sg-wl-2025__c0094 | ☑️ |
> | 18 | 230 | **Total Abzüge** | **40'518** | **33'548** | Summe der obigen Positionen | | |
> 
> **Nicht betroffen (nicht zutreffend):** Ziff. 11 Schuldzinsen, Ziff. 12.1/12.2 Unterhalt (Nadine zahlt keine Alimente), Ziff. 17 Zweiverdiener, Ziff. 15 Liegenschaften.
> 
> ## 3. Einkommensberechnung
> 
> | Ziff. | Code | Position | Kanton | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|---|
> | 20 | 234 | **Nettoeinkommen** | **42'150** | **49'120** | 82'668 − 40'518 bzw. 82'668 − 33'548 | sg-form-1-2025__c0010 |
> | 21.1 | 650/238/240 | Krankheits- und Unfallkosten | 2'757 | 1'144 | Vorkolonne 3'600 (Zahnarzt 2'750 + Franchise/Selbstbehalt 850). Selbstbehalt K 2 % × 42'150 = 843 → 2'757. Selbstbehalt B 5 % × 49'120 = 2'456 → 1'144 | sg-form-1-2025__c0010; sg-wl-2025__c0098; sg-form-6-2025__c0003 |
> | 21.3 | 244 | Freiwillige Zuwendungen (Spende Caritas) | 0 | 0 | 80 < Mindestbetrag 100 | sg-wl-2025__c0102 |
> | 22 | 248 | **Reineinkommen** | **39'393** | **47'976** | 42'150 − 2'757 bzw. 49'120 − 1'144 | |
> | 23.2 | 254 | Kinderabzug Elias (Kindergarten = Schulpflicht) | 10'800 | 6'800 | Kanton 23.2 Fr. 10'800; Bund Fr. 6'800 | sg-form-1-2025__c0011; sg-form-32-2025__c0006; bund-dbg-2025__art-35 |
> | 23.1 | 252 | Kinderabzug vor Schulpflicht | – | – | Nicht anwenden. Elias ist seit August 2025 im Kindergarten | Beachten-Hinweis 23.1 |
> | 23.3 | 256 | Ausbildungskosten Kinder | 0 | 0 | Kita ist Drittbetreuung, nicht Ausbildung | |
> | 24 | 268 | **Steuerbares Einkommen** | **28'593** | **41'176** | Kanton 39'393 − 10'800. Bund 47'976 − 6'800 | |
> 
> **Bund-Steuerbetrag:** Im Bund gibt es zusätzlich eine Ermässigung des Steuerbetrags um **263 Fr.** für Elias (bund-dbg-2025__art-36-t4). Sie wird von der Veranlagungsbehörde berücksichtigt.
> 
> **Plausibilität:** Das Bundes-Einkommen liegt rund 12'600 über dem kantonalen. Grund: Kanton hat höhere Abzüge (Fahrkosten 8'000 vs. 3'300, Versicherung 4'500 vs. 2'500, Kinderabzug 10'800 vs. 6'800, Krankheitskosten, Pauschale). Das ist konsistent mit den unterschiedlichen Limiten.
> 
> ## 4. Vermögen (nur Kanton)
> 
> | Ziff. | Code | Position | Kanton | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|
> | 30.1 | 300 | Wertschriften/Guthaben (Raiffeisen Sparkonto) | 31'500 | Steuerwert 31.12.2025 | sg-wl-2025__c0122 |
> | 30.4 | 306 | Motorfahrzeug (Privatauto) | **offen** | Steuerwert = Anschaffungswert − 20 % pro Jahr seit Kauf. **Verkehrswert/Kaufdatum fehlen** | sg-wl-2025__c0111 |
> | 33/35 | 322/326 | Total Vermögen / Reinvermögen | 31'500 + Auto | | |
> | 36.1 | 330 | Freibetrag alleinstehend 75'000 + Kind 20'000 (Obhut, Kinderabzug) | 95'000 | | sg-stg-2025__art-64 |
> | 37 | 338 | **Steuerbares Vermögen** | **0** | max(0; 31'500 + Auto − 95'000). Null, solange Auto ≤ 63'500 | |
> 
> ## 5. Nicht zu deklarieren oder nicht abziehbar
> 
> | Beleg | Betrag | Grund | Fundstelle |
> |---|---|---|---|
> | Spende Caritas St. Gallen-Appenzell | 80 | Unter Mindestschwelle 100 (Gesamtsumme aller Zuwendungen). Ziff. 21.3 bleibt leer | sg-wl-2025__c0102 |
> | Motorfahrzeug-Haftpflicht/Kasko | 1'020 | Motorfahrzeugversicherungen sind vom Abzug ausgeschlossen. Nicht in Ziff. 14 | sg-wl-2025__c0088 |
> | Motorfahrzeugsteuer | 410 | Keine Abzugsposition | Beleg `motorfahrzeug-versicherung`: «nichts abzugsrelevant» |
> | Handy-Abo | 720 | Private Lebenshaltung, nicht abziehbar (Art. 34 lit. a DBG) | bund-dbg-2025__art-34 |
> | Mahlzeiten Kita | 1'080 | Verpflegung ist Lebenshaltung. Nicht in 16.2 | sg-wl-2025__c0092 |
> | Lohnausweis Ziff. 9 (AHV etc.) und Ziff. 10.1 (BVG ordentlich) | 5'890 / 4'610 | Bereits im Nettolohn (Ziff. 1.1). Nicht nochmals abziehen | Form. 1 Ziff. 13.2 Beachten |
> | Kinderzulage 2'400 | – | Bereits in Bruttolohn/Nettolohn. Nicht separat unter Ziff. 3.5 | |
> 
> ## Offene Punkte (vor Einreichung klären)
> 
> 1. **Fahrkosten Auto, Begründung (⚠️).** Arbeitsbeginn 06:00, erste ÖV-Verbindung ab Wohnort 06:40. Die Begründung «kein zumutbares ÖV» ist bei Abfahrt ab 06:40 nachvollziehbar. Fahrplan beilegen. Wenn die Begründung nicht trägt, entfallen die Fahrkosten: Kanton −8'000, Bund −3'300. Dann steigt das steuerbare Einkommen auf ca. 36'753 (Kanton) bzw. 44'641 (Bund).
> 2. **Verpflegung (⚠️).** Die Rechnung setzt Mittagessen auswärts an allen 220 Arbeitstagen voraus. Verpflegung an Homeoffice-Tagen oder Absenzen ist nicht abziehbar.
> 3. **Krankheitskosten.** Die 850 Franken Franchise/Selbstbehalt: Wer ist versichert (Nadine oder Elias)? Ist der Zahnarzt-Betrag 2'750 schon darin enthalten? Die Leistungsübersicht der Krankenkasse ist einzureichen, da die Kasse darin verweist (sg-form-6-2025__c0003).
> 4. **Kinderbetreuung Bund.** Der Bund zieht Drittbetreuung nur innerhalb der Arbeits- oder Ausbildungszeit ab. Mit den Kita-Betreuungszeiten vergleichen. Kanton: 8'760 unverändert.
> 5. **BVG-Einkauf (⚠️).** Die 3-Jahres-Sperrfrist gilt, falls in den letzten 3 Jahren ein Kapitalbezug (WEF/Freizügigkeit) erfolgte. Dann ist der Einkauf nicht abziehbar. Einkaufsberechnung beilegen (Pflicht).
> 6. **Kinderabzug Elias.** Kindergarten zählt zur Schulpflicht, deshalb 23.2 und nicht 23.1. Das ist die Annahme nach den Beachten-Hinweisen.
> 7. **Motorfahrzeug Vermögen.** Verkehrswert und Kaufdatum (Fahrzeugausweis/Kaufvertrag) fehlen. Bei Leasing nicht im Vermögen.
> 8. **Einzureichen (Pflicht):** Lohnausweis (1 Arbeitgeber), 3a-Bescheinigung, PK-Bescheinigung inkl. Einkaufsberechnung, Steuerauszug Raiffeisen, Scheidungsurteil-Auszug (bei erstmaliger Deklaration der Alimente). Auf Verlangen: Kitarechnungen (Form. 10), KK-Prämien, Spendenbestätigung, Weiterbildungsaufstellung.
> 
> ## Fundstellen-Übersicht
> 
> - Form. 4: `sg-form-4-2025__c0001` (1.1–1.2), `c0002` (1.3), `c0003` (2.1)
> - Form. 1: `sg-form-1-2025__c0006` (4.1, 6.1), `c0008` (10.1, 13.2), `c0009` (14, 16.2, 16.4), `c0010` (20, 21.1), `c0011` (23.1–23.2)
> - Wegleitung: `sg-wl-2025__c0068`, `c0074`, `c0077`, `c0080`, `c0085`, `c0086`, `c0088`, `c0092`, `c0094`, `c0098`, `c0102`, `c0111`, `c0122`
> - Gesetz: `sg-stg-2025__art-64` (Vermögensfreibeträge), `bund-dbg-2025__art-35`, `bund-dbg-2025__art-36-t4` (263 Fr.)

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


**Antwort des Agenten** (141.4 s · Tools: 18 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige):

> Ich beginne mit dem Gesamtgerüst der Steuererklärung TG 2025 und prüfe parallel die Kernpositionen.
> 
> Die Grundlage steht. Jetzt prüfe ich die offenen Punkte: Versicherungsprämien (Form. 5.2), Hausrat, Sozialabzug für Verwitwete, Teilbesteuerung, Verrechnungssteuer, Gebäudeversicherung und die Renten.
> 
> Zwei Punkte brauche ich noch genauer: ob die Gebäudeversicherungsprämie bei Eigengebrauch abziehbar ist, und die Einordnung der PK-Rente (Ziff. 3.2).
> 
> # Ausfüllhilfe Steuererklärung 2025 TG (natürliche Person, verwitwet, AHV-Rentnerin)
> 
> **Ergebnis:** Kanton (Staats- und Gemeindesteuer) steuerbares Einkommen **Fr. 32'367**, Bund steuerbares Einkommen **Fr. 39'236**, steuerbares Vermögen Kanton **Fr. 273'000**. Alle Werte stehen auf ☑️ agent-geprüft (Fundstelle geprüft, Abnahme offen).
> 
> Alle Werte basieren auf den Angaben in der Anfrage. Offene Punkte stehen am Ende.
> 
> ## 1. Einkünfte (Formular 1)
> 
> | Ziff. / Code | Position | Kanton | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|
> | 3.1 / 130 | AHV-Altersrente | 27'000 | 27'000 | 12 × 2'250, zu 100 % steuerbar | tg-form-01-2025__c0007; tg-wl-2025__c0076 |
> | 3.2 / 132 | PK-Altersrente | 10'800 | 10'800 | 12 × 900, zu 100 % (Rentenbeginn 2020, also nicht Übergangsrecht 80 %) | tg-form-01-2025__c0007; tg-wl-2025__c0077 |
> | 4 / 150 | Zinsen Sparkonto + Dividenden (brutto) | 2'350 | 2'350 | 250 Zins + 2'100 Dividende, jeweils Bruttobetrag | tg-form-02-2025__c0005 |
> | 8.1 / 180 | Eigenmietwert, Nettoerfolg (Form. 7/8) | 4'840 | 8'920 | Kanton: 20'400 × (1 − 40 %) = 12'240 − 7'400; Bund: 20'400 × (1 − 20 %) = 16'320 − 7'400 | tg-form-07-2025__c0002; tg-wl-2025__c0225 |
> | 9 / 198 | Total Einkünfte | **44'990** | **49'070** | | |
> 
> **Eigenmietwert-Unterhalt (Form. 8):** Die effektiven Kosten (7'400) übersteigen die Pauschale. Die Pauschale beträgt 20 % (Gebäude 1986 > 10 Jahre), also Kanton 2'448 und Bund 3'264. Deshalb effektiv wählen. Die Position umfasst:
> - Malerarbeiten Ersatzanstrich 6'400 (Instandhaltung)
> - Gebäudeversicherungsprämie 520 (Sachversicherung für die Liegenschaft, abziehbar; tg-wl-2025__c0227, tg-stp-34-1__c0014)
> - Baumschnitt/Gartenpflege 480 (Garten, Instandhaltung)
> 
> **Nicht im Unterhalt:** Wintergarten-Anbau 31'000. Das ist Neubau/Anbau mit Mehrwert. Es gehört in die Spalte «Anlagekosten/Mehrwert» in Form. 8 und ist nicht abziehbar (tg-form-08-2025__c0001; tg-wl-2025__c0234).
> 
> ## 2. Abzüge
> 
> | Ziff. / Code | Position | Kanton | Bund | Rechenweg | Fundstelle |
> |---|---|---|---|---|---|
> | 11 / 290 | Schuldzinsen (Form. 4.1 A) | 3'150 | 3'150 | Hypothekarzinsen 2025 fällig; Limite Vermögenserträge + 50'000 eingehalten | tg-form-04-1-2025__c0001; tg-wl-2025__c0173 |
> | 14 / 330 | Versicherungsprämien (Form. 5.2) | 3'500 | 1'800 | A-Total 6'240 (KK netto, keine IPV) + 250 Sparzins = 6'490; Abzug = min(A; B4). B4 alleinstehend: Kanton 3'500, Bund 1'800 | tg-form-05-2-2025__c0001, __c0002 |
> | 19 / 360 | Total Abzüge | **6'650** | **4'950** | | |
> | 22 / 362 | Nettoeinkommen | **38'340** | **44'120** | 44'990 − 6'650 bzw. 49'070 − 4'950 | |
> 
> ## 3. Krankheitskosten und Spenden
> 
> **Form. 5.1 (Krankheitskosten):**
> - A (Aufwand): Selbstbehalt/Franchise 1'000 (A1), Zahnarzt 4'440, Brille 1'400. Total **6'840**. Genaue A-Zeilen im Formular prüfen.
> - B (Vergütungen): Zusatzversicherung auf Brille **300**.
> - A − B = **6'540**
> 
> **Ziff. 23.1 / Code 364 (Formel: (A − B) − 5 % × Ziff. 22):**
> 
> | | Kanton | Bund |
> |---|---|---|
> | 5 % × Nettoeinkommen | 1'917 | 2'206 |
> | Abzug (6'540 − Selbstbehalt) | **4'623** | **4'334** |
> 
> Fundstellen: tg-form-05-1-2025__c0004; tg-form-01-2025__c0012; tg-wl-2025__c0206.
> 
> **Ziff. 23.2 / Code 366 (Form. 6, Krebsliga TG 300 + Pro Senectute TG 250 = 550):**
> - Kanton: 550 − 200 Selbstbehalt = **350** (Maximum 8'000, da Netto ≤ 40'000)
> - Bund: min(550; 20 % × 44'120 = 8'824) = **550** (ab Fr. 100 ohne Selbstbehalt)
> 
> Fundstellen: tg-form-06-2025__c0002; tg-wl-2025__c0220.
> 
> ## 4. Reineinkommen und Sozialabzug
> 
> | Ziff. | Position | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|
> | 24 / 372 | Reineinkommen | **33'367** | **39'236** | Kanton 38'340 − 4'623 − 350; Bund 44'120 − 4'334 − 550 |
> | 25.3 / 388 | Abzug AHV-Rentnerin/verwitwet | **1'000** | – (kein Abzug) | 4'200 − 200 × 16 volle Fr. 1'000 über 16'900 = 1'000 |
> | 26 / 398 | Steuerbares Einkommen | **32'367** | **39'236** | |
> 
> Fundstelle Ziff. 25.3: tg-form-01-2025__c0013; tg-wl-2025__c0116. Die Wegleitungstabelle hat eine Druckfehler-Zeile («36'900–37'689»). Deshalb nach der Formel rechnen, nicht nach der Tabelle.
> 
> Keine weiteren Sozialabzüge: keine Kinder, keine unterstützten Personen, keine Ehepaar-Abzüge, kein Zweiverdienerabzug. Der Bund kennt für diesen Fall keinen Alters-/Verwitwenabzug.
> 
> ## 5. Vermögen (Kanton; Bund ohne Vermögenssteuer)
> 
> | Ziff. / Code | Position | Betrag | Fundstelle |
> |---|---|---|---|
> | 30.1 / 410 | Wertschriften und Guthaben (Form. 2, Sp. 7): Sparkonto 48'000 + Depot 95'000 | 143'000 | tg-form-02-2025__c0005 |
> | 31 / 430 | Liegenschaft, Steuerwert | 410'000 | tg-form-01-2025__c0015; tg-form-07-2025__c0002 |
> | 33 / 464 | Total Vermögenswerte | 553'000 | |
> | 34 / 466 | Schulden (Hypothek, Form. 4.1 A, Code 455) | 180'000 | tg-form-04-1-2025__c0001 |
> | 35 / 468 | Reinvermögen | 373'000 | |
> | 36.2 / 472 | Freibetrag alleinstehend | − 100'000 | |
> | 37 / 498 | **Steuerbares Vermögen** | **273'000** | |
> 
> ## 6. Verrechnungssteuer (Form. 2 Ziff. 10)
> 
> - Bruttoertrag mit VSt (Sp. 8): 250 + 2'100 = 2'350
> - Anspruch 35 %: **822.50** (87.50 + 735, wie auf den Steuerauszügen)
> - Rückerstattung nur bei Wohnsitz TG am 31.12.2025. Auszahlungskonto (IBAN) auf Seite 1 eintragen.
> 
> Fundstelle: tg-form-02-2025__c0006; tg-wl-2025__c0167.
> 
> ## 7. Nicht zu deklarieren bzw. nicht abziehbar
> 
> | Beleg | Ergebnis | Begründung |
> |---|---|---|
> | Wintergarten-Anbau 31'000 | Kein Abzug, Mehrwert | Neubau/Anbau; Form. 8 Spalte Anlagekosten/Mehrwert. Im Vermögen beachten (siehe offene Punkte) |
> | Hausratversicherung 380 | Kein Abzug | Hausrat ist nicht abziehbar (nur Sachversicherung für die Liegenschaft); keine Position in Form. 5.2 (tg-wl-2025__c0227, tg-wl-2025__c0064) |
> | Serafe 335 | Kein Abzug | Gebühr/Lebenshaltung |
> | Handyrechnung | Kein Abzug | Private Lebenshaltungskosten (tg-wl-2025__c0064, tg-info-faq__c0024) |
> | Spendenquittungen (je unter Fr. 1'000) | Abzug ja, Belege nicht beilegen | Belege erst ab Fr. 1'000 pro Zuwendung einreichen, darunter nur auf Verlangen (tg-wl-2025__c0220) |
> | Verwaltungskosten Depot | Siehe offene Punkte | Nur bei Vermögensverwaltungsmandat (2 ‰ von 95'000 = max. 190 Kanton) |
> 
> **Keine Beiträge** an 2. Säule oder 3a: keine Positionen 13.x und 15.2.
> 
> **Keine Ergänzungsleistungen** angegeben. Falls EL bezogen wurden: steuerfrei, nicht in Ziff. 3.1 aufnehmen, und auf Seite 1 «EL» ankreuzen (tg-wl-2025__c0076).
> 
> ## 8. Beilagen
> 
> - Rechnungskopie Malerarbeiten 6'400 (Einzelbetrag ab Fr. 1'000, Form. 8)
> - Krankenkassen-Leistungsabrechnung (Selbstbehalt 1'000, Vergütung 300)
> - Rechnungen Zahnarzt 4'440 und Brille 1'400 (Verordnung als Kopie)
> - Hypothekarbestätigung mit Gläubiger, Zinssatz und Restschuld 31.12.2025 (Form. 4.1)
> - Depotauszug und Steuerauszug Bank (Form. 2)
> - AHV- und PK-Rentenbescheinigung
> - Liegenschaftensteuerrechnung/Schätzung (Steuerwert und Mietwert)
> 
> ## Offene Punkte (vor Abgabe prüfen)
> 
> 1. **Wintergarten im Steuerwert:** Ist der Anbau (31'000) in der Schätzung mit Stichtag 31.12.2025 enthalten? Falls nein, muss der Steuerwert (Ziff. 31) angemessen erhöht werden (tg-wl-2025__c0239: unfertige Bauten). Der Eigenmietwert kann bei der nächsten Schätzung ebenfalls steigen.
> 2. **Vermögensverwaltung:** Liegt ein Vermögensverwaltungsmandat vor? Dann Abzug Kanton max. 190 (Code 148). Der Bundesabzug ist nicht geprüft.
> 3. **Teilbesteuerung:** Wurde kein Dividendenertrag ≥ 10 % einer Gesellschaft erzielt? Dann keine Teilbesteuerung (Ziff. 15.6). Bei ≥ 10 % Beteiligung wäre der Abzug Kanton 40 % bzw. Bund 30 % (tg-form-02-2025__c0008).
> 4. **Gemeinnützigkeit:** Sind Krebsliga TG und Pro Senectute TG auf der Liste der Steuerverwaltung TG? Ohne Liste-Eintrag entfällt der Abzug.
> 5. **Hypothek:** Gläubiger (Name, Adresse) und Zinssatz für Form. 4.1 fehlen in der Anfrage. Der Zins 3'150 bei 180'000 entspricht rund 1.75 %.
> 6. **Sozialabzug:** Der Abzug 1'000 folgt der Formel nach Wegleitung, nicht der Tabelle (Druckfehler).
> 7. **Zahnarzt/Brille-Zeilen:** Die genauen A-Zeilen in Form. 5.1 bitte am Formular nachprüfen.
> 
> Die fachliche Beurteilung und Abnahme bleibt bei der Fachperson.

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


**Antwort des Agenten** (156.5 s · Tools: 18 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__suche, steuerwiki__wert):

> ## Ausfüllhilfe Steuererklärung 2025, Kanton AR (Ehepaar, Herisau)
> 
> Kanton und Bund stehen im AR-Formular in einer Spalte. Die Bundswerte unten sind Kontrollwerte nach Bundesregeln; die Steuerverwaltung nimmt die Abweichungen automatisch vor. Hauptformular-Codes für Ziff. 10 bis 24 sind laut Wiki nicht am Originalformular verifiziert (Miniaturen der WL).
> 
> **Annahmen (bitte bestätigen):**
> - Aktien (38'000) sind unter 10 % Beteiligung → Ertrag in Ziff. 4.1, nicht 4.2/4.3.
> - Krebsliga Ostschweiz ist steuerbefreit gemeinnützig (Spendenquittung prüfen).
> - Keine Naturallohn-Hinzurechnung für Personalkantine (Feld G) und Werkbus (Feld F).
> - Keine Krankheitskosten, keine Schulden, keine Liegenschaft, keine Eigenmiete.
> 
> ### 1. Einkünfte
> 
> | Ziff. | Position | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 1.1 (Code 100) | Haupterwerb P1 | 85'300 | 85'300 | Nettolohn Lohnausweis Ziff. 11 · ar-wl-2025__c0035 |
> | 1.1 (Code 102) | Haupterwerb P2 | 68'200 | 68'200 | Ziff. 11 (inkl. Kinder-/Ausbildungszulagen aus Ziff. 8) · ar-wl-2025__c0032 |
> | 4.1 (Code 146) | Wertschriftenerträge | 1'410 | 1'410 | Zins 160 (Spalte B) + Dividende 1'250 (Spalte A) · ar-form-02-2025__c0005 |
> | 7 (Code 168) | Total Einkünfte | 154'910 | 154'910 | |
> 
> Die Kinder-/Ausbildungszulagen von P2 gehören in 1.1, nicht in 3.5. Ziff. 3.5 gilt nur für Zulagen, die direkt von der Ausgleichskasse ausbezahlt werden · ar-wl-2025__c0054.
> 
> ### 2. Abzüge
> 
> | Ziff. | Position | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 10.1 (Code 438) | Berufskosten P1 | 4'000 | 4'159 | Kanton: Fahrkosten 0 (Feld F) + Verpflegung verbilligt 1'600 (220 × 7.50 = 1'650, max 1'600) + Pauschale 2'400 (700 + 10 % von 85'300 = 9'230, max 2'400). Bund: 1'600 + Pauschale 2'559 (3 % von 85'300, Rahmen 2'000–4'000). Form. 4 Ziff. 1.1, 2.2, 3 · ar-wl-2025__c0075 |
> | 10.2 (Code 488) | Berufskosten P2 | 6'300 | 5'946 | Kanton: ÖV-Abo 1'260 (Code 450) + Verpflegung 2'640 (176 × 15, max 3'200, Code 458) + Pauschale 2'400. Bund: 1'260 + 2'640 + Pauschale 2'046 (3 % von 68'200). Form. 4 Ziff. 1.1, 2.1, 3 · ar-wl-2025__c0074 |
> | 13.1 | Säule 3a | 12'258 | 12'258 | P1 7'258 (Max. mit 2. Säule 7'258) + P2 5'000 |
> | 13.2 | Einkauf 2. Säule | **0** | **0** | Die 4'000 sind bereits im Lohnausweis Ziff. 10.2 abgezogen und im Nettolohn enthalten. Nicht doppelt abziehen · ar-wl-2025__c0084 (⚠️ WL widersprüchlich) |
> | 14 | Versicherungsprämien | 7'400 | 5'100 | Krankenkasse 13'900 + Sparzinsen 160 übersteigen die Limite. Kanton: 5'400 + 2 × 1'000 = 7'400. Bund: 3'700 + 2 × 700 = 5'100 · ar-form-06-2025__c0002, ar-wl-2025__c0085 |
> | 16.2 | Kinderbetreuung Lea | 10'200 | 10'200 | 14'400 − Mittagessen 1'800 − Betreuungsbeitrag 2'400 (Limite 25'000 / 25'800) · ar-form-10-2025__c0001, ar-wl-2025__c0091 |
> | 17 | Zweiverdiener | 5'200 | 14'100 | Kanton: 10 % von E (56'900) = 5'690, Max 5'200. Bund: 50 % von E (57'254) = 28'627, Max 14'100. Die Maxima greifen auch, wenn der Einkauf nochmals abgezogen würde · ar-wl-2025__c0004 |
> | 18 | Total Abzüge | 45'358 | 51'763 | |
> 
> ### 3. Einkommensberechnung
> 
> | Ziff. | Position | Kanton | Bund |
> |---|---|---|---|
> | 20 | Nettoeinkommen | 109'552 | 103'147 |
> | 21.1 | Krankheitskosten | 0 | 0 |
> | 21.3 | Spenden Krebsliga (Code 550) | 300 | 300 |
> | 22 | Reineinkommen | 109'252 | 102'847 |
> | 23.2 | Kind Lea (4.–15. Altersjahr) | 7'400 | 6'800 |
> | 23.3 | Kind Jonas (Kantonsschule, 16 J.) | 11'600 | 6'800 |
> | 24 | Verheiratetenabzug (nur Bund) | – | 2'800 |
> | 24 | **Steuerbares Einkommen** | **90'252** | **86'447** |
> 
> Lea hat am 14.03.2025 ihr 4. Altersjahr vollendet, deshalb Ziff. 23.2 und nicht 23.1 · ar-wl-2025__c0005. Spenden: Mindestbetrag 100 erreicht, Maximum 20 % von Ziff. 20 (Kanton 21'910, Bund 20'629) · ar-form-05-2025__c0003, Bund: bund-dbg art. 33a.
> 
> ### 4. Vermögen (Stand 31.12.2025)
> 
> | Ziff. | Position | Betrag |
> |---|---|---|
> | 30.1 (Code 300) | Konten 54'000 + Aktien Steuerwert 38'000 | 92'000 |
> | 33 / 35 | Total Vermögenswerte / Reinvermögen | 92'000 |
> | 36.2 + 36.3 | Freibetrag Ehepaar 150'000 + 2 × 25'000 Kinder | 200'000 |
> | 37 | **Steuerbares Vermögen Kanton** | **0** |
> 
> Die Bundessteuer kennt kein Vermögen. Das 3a-Guthaben per 31.12. fehlt noch (siehe offene Punkte).
> 
> ### 5. Hilfsblätter
> 
> - **Form. 2 (Wertschriften):** Konten 54'000, Spalte B (Zins 160 ohne VSt). Aktien 38'000 Steuerwert, Dividende 1'250 Bruttoertrag, Spalte A. Ziff. 999: VSt-Anspruch 35 % × 1'250 = **437.50** (Rückerstattung über die Steuererklärung). Form. 2 S. 1 (960–963): Nein, keine Erbschaft oder Schenkung.
> - **Form. 4 (Berufskosten):** wie Ziff. 10.1/10.2 oben.
> - **Form. 6 (Versicherungen):** Teil A a (KK brutto) 13'900 + Sparzinsen 160, keine Prämienverbilligung.
> - **Form. 10 (Kinderbetreuung):** Kita Lea, Rechnungen 14'400, Abzug Mittagessen 1'800, erhaltene Beiträge 2'400, abziehbar 10'200.
> - **Form. 5 (Zuwendungen):** Krebsliga 300.
> 
> ### 6. Nicht zu deklarieren
> 
> - **Einkauf 4'000 (P2) in Ziff. 13.2:** bereits über Lohnausweis Ziff. 10.2 abgezogen; Doppelabzug vermeiden.
> - **BVG-Beiträge** Lohnausweis Ziff. 10.1/10.2 (5'840 / 4'060): nur im Nettolohn, nicht separat.
> - **Kita-Mittagessen 1'800:** Verpflegung, nicht abziehbar · ar-wl-2025__c0091.
> - **Kita-Betreuungsbeitrag 2'400:** keine Einnahme, nur Kürzung der Kosten.
> - **Steuern 2024 (9'870):** keine Abzugsposition im Formular. Im Wiki fand ich keinen Chunk, der den Ausschluss ausdrücklich belegt.
> - **Handy-Abo 960:** private Lebenshaltung, keine Abzugsposition.
> - **Turnverein-Mitgliederbeitrag 120:** Mitgliederbeiträge sind nicht abziehbar (Regel Ziff. 21.3).
> - **Fahrkosten P1:** kein Abzug wegen Feld F (unentgeltlicher Werkbus) · ar-wl-2025__c0075.
> - **Kinderzulagen:** nicht zusätzlich in Ziff. 3.5, weil schon in 1.1 enthalten.
> 
> ### 7. Offene Punkte
> 
> 1. **Säule-3a-Stand 31.12.2025** beider Personen fehlt. Ohne 3a beträgt das Vermögen 92'000 und liegt unter dem Freibetrag 200'000. Liegen die 3a-Guthaben zusammen über 108'000, entsteht Kantonsvermögenssteuer.
> 2. **Eigene Einkünfte und Reinvermögen von Jonas** fehlen. Der Kinderabzug entfällt bei Einkünften über 18'000 oder Reinvermögen über 250'000 · Position 23.3.
> 3. **Beteiligungsquote der Aktien** bestätigen (sonst Ziff. 4.2/4.3 und Teilbesteuerung 16.7).
> 4. **Bund-Einkaufsregel** für die 4'000 nicht geprüft (nur Hinweis `wert bund 2025 einkauf`).
> 5. **Einreichung:** Lohnausweise, Einkaufsbescheinigung mit Einkaufsberechnung (in jedem Fall), vollständiger Bank-Steuerauszug, 3a-Bescheinigungen, Krankenkassen-Prämienbescheinigung, Kita-Rechnungen und ÖV-Abo gehören zu den Belegen; Spendenquittung und Krankenkassenbelege auf Verlangen.

