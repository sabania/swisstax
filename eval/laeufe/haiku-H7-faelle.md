# OpenClaw-Testlauf: faelle-2025.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Agent: `steuerplug` · Fragen: 4 · Lauf: 2026-11-09 15:59
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


**Antwort des Agenten** (192.5 s · Tools: 26 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__suche, steuerwiki__zeige, steuerwiki__wert, steuerwiki__rechne):

> Ich prüfe zuerst das Formular ZH 2025 und die einzelnen Positionen.
> 
> Die Grundlagen sind da. Jetzt prüfe ich die offenen Punkte: Berufsauslagen, Wertschriften und Verrechnungssteuer, Kinderabzug, Krankheitskosten, Spenden, Zweiverdienerabzug und Kinderzulagen.
> 
> Die Kinderzulagen-Frage und die Berufsauslagen-Regel (Pauschale plus Fahrkosten?) brauche ich im Wortlaut. Ich öffne die Chunks und prüfe das Velo.
> 
> Die Zahlen sind geprüft. Eine Stelle fehlt noch: Der Bund behandelt die verbilligte Verpflegung (Sandras Personalrestaurant) abweichend. Ich prüfe das, bevor ich rechne.
> 
> Der Bund-Verpflegungsansatz für verbilligte Verpflegung ist gleich wie im Kanton (CHF 7.50/Tag, max. 1'600). Jetzt rechne ich alle Totale und Limiten exakt nach.
> 
> # Ausfüllhilfe ZH 2025: Ehepaar Winterthur (Marco und Sandra)
> 
> Alle Beträge in CHF. Kanton (Staat) und Bund (Bundessteuer) sind getrennt angegeben. Totale sind mit `rechne` geprüft. Die Steuerbeträge (Tarif) und der Gemeindesteuerfuss sind nicht berechnet.
> 
> ## Annahmen (bitte bestätigen)
> 
> 1. **Marco, Mittagessen:** Die Hauptmahlzeit kostet mehr als CHF 10, und die Heimkehr ist wegen Zug–Winterthur nicht möglich. Dann gilt die Verpflegung voll. Für den Bund entfällt der Abzug bei Hauptmahlzeiten bis CHF 10 (`wert bund 2025 verpflegung`, Fundstelle bund-bkv-2025__anhang-1).
> 2. **Sandra, Personalrestaurant (Feld G):** Die Heimkehr in der Pause ist nicht möglich. Dann gilt die verbilligte Verpflegung (Form. 360 Ziff. 2.1 verbilligt).
> 3. **Sandra, Velo:** ständige Benützung, daher die Pauschale von CHF 700.
> 4. **Hort-Rechnung Noah (6'900):** Die Verpflegung ist im Betrag nicht enthalten. Ist sie enthalten, siehe Punkt «Offene Punkte».
> 
> ## A. Einkünfte
> 
> | Ziff./Code | Position | Staat | Bund | Rechnung · Fundstelle | Status |
> |---|---|---|---|---|---|
> | 1.1 · Code 100 | Haupterwerb Marco (Nettolohn Lohnausweis Ziff. 11) | 103'000 | 103'000 | 118'400 − 8'110 − 7'290 = 103'000 · zh-wl-2025__c0032 | ☑️ |
> | 1.1 · Code 101 | Haupterwerb Sandra (Nettolohn Ziff. 11) | 67'200 | 67'200 | 76'800 − 5'260 − 4'340 = 67'200 (inkl. Kinderzulagen 4'800, siehe Hinweis) | ☑️ |
> | 4.1 · Code 150 | Ertrag Wertschriften/Guthaben (A + B) | 1'140 | 1'140 | A 960 (Depot, VSt 336) + B 180 (Sparkonto) · zh-form-340-2025__c0005 | ☑️ |
> | 4.2 · Code 151 | Qualifizierte Beteiligungen | 0 | 0 | keine Beteiligung ≥ 10 % angenommen (siehe Offene Punkte) | ⬜ |
> | 7 · Code 199 | Total Einkünfte | 171'340 | 171'340 | 170'200 + 1'140 | – |
> 
> **Hinweis Kinderzulagen:** Die 4'800 Kinderzulagen sind über den Lohn ausbezahlt und stehen in Lohnausweis Ziff. 8. Sie sind also steuerbar und gehören in Ziff. 1.1. Ziff. 3.4 gilt nur für Zulagen, die direkt von der Ausgleichskasse kommen (zh-wl-2025__c0055).
> 
> **Form. 340 (Wertschriften):**
> - Kolonne A (mit VSt): Depot, Bruttodividende 960. Die VSt-Rückerstattung ist 35 % × 960 = 336 (Code 540). Das stimmt mit dem Bankausweis überein.
> - Kolonne B (ohne VSt): Sparkonto Zins 180. Privatkonto 0.
> - Steuerwert (Code 400): 42'500 + 8'300 + 31'200 = 82'000.
> 
> ## B. Abzüge
> 
> | Ziff./Code | Position | Staat | Bund | Rechnung · Fundstelle | Status |
> |---|---|---|---|---|---|
> | 11.1 · Code 220 | Berufsauslagen Marco (Form. 360) | 10'470 | 9'590 | Fahrkosten ÖV-Abo 4'180 (K) / 3'300 (B, Plafond). Verpflegung voll: 15 × 220 = 3'300, max. 3'200 (K); B wie K, falls Hauptmahlzeit > CHF 10. Pauschale 3 % × 103'000 = 3'090 (min. 2'000, max. 4'000). · zh-form-360-2025__c0001, c0003, c0004; bund-dbg-2025__art-26 | ☑️ |
> | 11.2 · Code 240 | Berufsauslagen Sandra (Form. 360) | 4'036 | 4'036 | Velo-Pauschale 700 · verbilligte Verpflegung 7.50 × 176 = 1'320 (≤ 1'600; Bund gleich: bund-bkv-2025__anhang-1) · Pauschale 3 % × 67'200 = 2'016 | ☑️ |
> | 12 | Schuldzinsen | 0 | 0 | keine | – |
> | 14.1 · Code 260 | Säule 3a Marco | 7'258 | 7'258 | min(7'258; 7'258) · Formular 21 EDP · zh-form-300-2025__c0008 | ☑️ |
> | 14.2 · Code 261 | Säule 3a Sandra | 7'258 | 7'258 | min(7'258; 7'258) | ☑️ |
> | 15 · Code 270 | Versicherungsprämien/Sparzinsen | 8'400 | 5'100 | min(A; B). A = 601 KK-Prämien 15'840 + 604 Sparzins 180 = 16'020. B Staat = 5'800 + 2 × 1'300 = 8'400. B Bund = 3'700 + 2 × 700 = 5'100. | ☑️ |
> | 16.1 · Code 280 | Einkauf PK Marco (selbst bezahlt) | 10'000 | 10'000 | Ziff. 10.2 Lohnausweis = 0, daher kein Doppelabzug. Sperrfrist: kein Kapitalbezug in 3 Jahren (bestätigt). · zh-wl-2025__c0092 | ☑️ |
> | 16.6 · Code 376 | Fremdbetreute Kinder | 31'900 | 32'700 | Lena (Kita 27'300): min(27'300; 25'000) = 25'000 (K) / min(27'300; 25'800) = 25'800 (B). Noah (Hort 6'900): 6'900 (provisorisch). · zh-form-300-2025__c0008; zh-stg-2025__par-31-t4 | ☑️ |
> | 17 · Code 290 | Sonderabzug Zweiverdiener | 6'100 | 14'100 | Basis = Sandra (tieferes Erwerbseinkommen): 67'200 − 4'036 − 7'258 = 55'906. K: min(55'906; 6'100) = 6'100. B: min(55'906; max(50 % = 27'953; 8'600); 14'100) = 14'100. · zh-form-300-2025__c0008 | ☑️ |
> | 18 · Code 299 | Total Abzüge | 85'422 | 90'042 | 14'506 + 14'516 + 8'400 + 10'000 + 31'900 + 6'100 (K) · 13'626 + 14'516 + 5'100 + 10'000 + 32'700 + 14'100 (B) | – |
> 
> ## C. Einkommensberechnung
> 
> | Ziff./Code | Position | Staat | Bund | Rechnung | Status |
> |---|---|---|---|---|---|
> | 21 · Code 310 | Nettoeinkommen | 85'918 | 81'298 | 171'340 − 85'422 (K) · 171'340 − 90'042 (B) | – |
> | 22.1 · Code 320 | Krankheitskosten | 0 | 0 | Ausgaben 1'850 + 1'240 = 3'090. Schwelle 5 %: K 4'295.90 · B 4'064.90. Unter der Schwelle, daher kein Abzug. · zh-form-300-2025__c0009 | ☑️ |
> | 22.2 · Code 324 | Gemeinnützige Zuwendungen | 650 | 650 | SRK 400 + UNICEF 250. ≥ 100 ✓, ≤ 20 % von Ziff. 21 (17'183.60 K / 16'259.60 B) ✓. · zh-form-300-2025__c0009 | ☑️ |
> | 23 · Code 350 | Reineinkommen | 85'268 | 80'648 | 85'918 − 0 − 650 · 81'298 − 0 − 650 | – |
> | 24.1 · Code 370 | Kinderabzug (2 Kinder im Haushalt) | 18'600 | 13'600 | 2 × 9'300 (K) · 2 × 6'800 (B) · zh-form-300-2025__c0010 | ☑️ |
> | 24.3 · Code 365 | Abzug Ehegatten (nur Bund) | – | 2'800 | Bund-Abzug für Ehepaar. Staat: kein Abzug. | ☑️ |
> | 25 · Code 390 | Steuerbares Einkommen | 66'668 | 64'248 | 85'268 − 18'600 · 80'648 − 13'600 − 2'800 | – |
> 
> ## D. Vermögen
> 
> | Ziff./Code | Position | Staat | Bund | Rechnung | Status |
> |---|---|---|---|---|---|
> | 30.1 · Code 400 | Wertschriften und Guthaben | 82'000 | – | 42'500 (Sparkonto) + 8'300 (Privatkonto) + 31'200 (Depot) | ☑️ |
> | 37 · Code 498 | Steuerbares Vermögen | 0 | – | 82'000 < Freibetrag Ehepaar 159'000 · zh-form-300-2025__c0010 | ☑️ |
> 
> ## E. Hilfsblätter
> 
> - **Form. 340:** Depot in Kolonne A (Brutto 960, VSt-Anspruch 336, IBAN und WV unterschreiben). Sparkonto 180 und Privatkonto 0 in Kolonne B. Die VSt-Rückerstattung muss innert der Frist beantragt werden.
> - **Form. 365 Teil A:** 601 = 15'840; 604 = 180; 605 = 0; 606 = 16'020.
> - **Form. 365 Teil B:** 611 = 5'800 (K) / 3'700 (B); Kinder 613–615 = 2 × 1'300 (K) / 2 × 700 (B). Teil C → Ziff. 15 (siehe oben).
> - **Form. 360 Marco:** Ziff. 1.1 (ÖV 4'180), Ziff. 2.1 voll (3'200 K / 3'200 B bei der Annahme), Ziff. 3 Pauschale 3'090, Ziff. 6 Total 10'470 / 9'590. Ziff. 7 nicht ankreuzen (kein Auto).
> - **Form. 360 Sandra:** Ziff. 1.2 Velo 700; Ziff. 2.1 verbilligt (Code 226) 1'320; Ziff. 3 Pauschale 2'016; Total 4'036.
> - **Form. 370 (Krankheitskosten):** nicht ausfüllen (unter der Schwelle).
> - **Lohnausweis:** Marco Feld F und G nicht angekreuzt. Sandra Feld G angekreuzt (verbilligte Verpflegung).
> 
> ## F. Nicht zu deklarieren bzw. nicht abziehbar
> 
> - **Zahnarzt 1'850 und Franchise/Selbstbehalt 1'240:** nicht abziehbar, weil sie unter der 5-%-Schwelle liegen (4'296 K / 4'065 B). Die Belege müssen nicht eingereicht werden, aber aufbewahren.
> - **Swisscom-Handyrechnungen 1'080:** private Lebenshaltung. Keine Formularposition.
> - **Hausrat- und Privathaftpflicht 465:** nicht abziehbar. Ziff. 15 und Form. 365 Teil A umfassen nur Kranken-, Unfall-, Lebens-/Rentenversicherungen und Sparzinsen.
> - **Lohnausweis Ziff. 10.2 (Einkauf vom Lohn) = 0:** nicht doppelt in 16.1 erfassen (hier nicht relevant, da 0).
> - **Säule 3a Einkauf:** erst ab Steuerjahr 2026. Für 2025 nicht deklarieren (zh-wl-2025 / Ziff. 14.3 nicht vorhanden).
> - **Verrechnungssteuer Schweizer Titel:** kein DA-1 (nur bei ausländischer Quellensteuer).
> - **Kinderzulagen 4'800:** kein separater Eintrag (steckt im Lohn, Ziff. 1.1).
> 
> ## G. Offene Punkte (vor Einreichung klären)
> 
> 1. **Marco, Hauptmahlzeit > CHF 10?** Falls nein, entfällt der Bundes-Verpflegungsabzug (3'200). Das steuerbare Einkommen Bund steigt dann auf **67'448** (statt 64'248). Kanton bleibt unverändert.
> 2. **Hort-Rechnung Noah:** Verpflegung herausrechnen. Jeder herausgerechnete Franken erhöht das steuerbare Einkommen (Kanton und Bund) um denselben Betrag.
> 3. **KK-Bescheinigung:** prüfen, dass keine NBUV-Prämie (Nichtberufsunfall) enthalten ist. Die NBUV ist bereits in Lohnausweis Ziff. 9 abgezogen, ein zweiter Abzug wäre Doppelabzug.
> 4. **Spendenempfänger:** SRK und UNICEF Schweiz im Verzeichnis der steuerbefreiten Institutionen ZH bestätigen (zh-info-spenden).
> 5. **Depot:** keine qualifizierte Beteiligung ≥ 10 %. Sonst Ziff. 4.2 und Teilbesteuerung prüfen.
> 6. **Säule-3a-Guthaben:** laut Wegleitung nicht im Wertschriftenverzeichnis. Stand der 3a-Konten per 31.12. ist nicht gegeben. Freibetrag bleibt mit Puffer, wenn die Konten unter ca. 77'000 liegen.
> 7. **Quellenkonflikt Drittbetreuung:** Die VKP ZH 2024 nennt CHF 10'400. Laut StG ZH 2025 und Formular gilt für 2025 CHF 25'000. Verwendet: 25'000 (zh-stg-2025__par-31-t4).
> 
> Die fachliche Beurteilung und Abnahme bleibt bei der Fachperson. Die Wegleitung wurde als Stand 2025 geprüft. Der Status ☑️ heisst «Fundstelle geprüft, Abnahme offen».

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


**Antwort des Agenten** (172.5 s · Tools: 24 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__wert, steuerwiki__rechne):

> # Ausfüllhilfe Steuererklärung 2025, Kanton SG (Nadine, Person 1)
> 
> **Annahmen:** Wohnsitz 31.12.2025 Toggenburg SG. Nadine ist alleinstehend und allein steuerpflichtig. Elias (5) besucht den Kindergarten, und Kindergarten zählt in SG zur Schulpflicht (Ziff. 23.2). Die Beträge stehen als **Kanton | Bund**. Alle Summen sind mit `rechne` geprüft.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Code | Feld | Kanton | Bund | Rechenweg | Fundstelle | Status |
> |---|---|---|---|---|---|---|---|
> | 1.1 | 100 | Nettolohn Lohnausweis (inkl. Kinderzulage 2'400) | 73'000 | 73'000 | 83'500 − 5'890 − 4'610 (Ziff. 10.1) = 73'000. Ziff. 10.2 = 0. Feld F/G leer. | sg-form-1-2025__c0004; sg-wl-2025__c0042 | ☑️ |
> | 4.1 | 146 | Sparzinsen Raiffeisen (Form. 2, Spalte B) | 68 | 68 | Bruttozins ≤ Fr. 200 → VSt-frei, Spalte B | sg-form-2-2025__c0005; sg-wl-2025__c0135 | ☑️ |
> | 6.1 | 156 | Kinderalimente Elias (12 × 800) | 9'600 | 9'600 | Alimente für minderjähriges Kind unter Obhut → beim Empfänger steuerbar. Code 154 (für Nadine) = 0. | sg-form-1-2025__c0006; sg-wl-2025__c0068 | ☑️ |
> | **7** | **168** | **Total Einkünfte** | **82'668** | **82'668** | 73'000 + 68 + 9'600 | | |
> 
> Die Kinderzulage 2'400 steckt bereits im Nettolohn. Ziff. 3.5 darf nicht zusätzlich ausgefüllt werden.
> 
> ## 2. Abzüge
> 
> | Ziff. | Code | Feld | Kanton | Bund | Rechenweg | Fundstelle | Status |
> |---|---|---|---|---|---|---|---|
> | 10.1 | 438 | Berufskosten (Form. 4, Total Ziff. 6) | 13'600 | 8'690 | **Fahrkosten:** 2 × 32 km × 220 Tage × 0.70 = 9'856 → K max. 8'000 / B max. 3'300. **Verpflegung:** 220 × 15 = 3'300 → max. 3'200 (K und B). **Übrige:** K 700 + 10 % × 73'000 = 8'000 → max. 2'400; B 3 % × 73'000 = 2'190 (Min. 2'000, Max. 4'000). | sg-form-4-2025__c0001/c0002; sg-wl-2025__c0002; sg-wl-2025__c0080; bund-bkv-2025 Anhang 1 | ☑️ |
> | 13.1 | 208 | Säule 3a | 7'258 | 7'258 | min(7'258; Max. 7'258) | sg-form-1-2025__c0008; sg-wl-2025__c0085 | ☑️ |
> | 13.2 | 218 | Einkauf Pensionskasse (direkt bezahlt 20.10.2025) | 6'000 | 6'000 | Lohn Ziff. 10.2 = 0, daher kein Doppelabzug. Bescheinigung + Einkaufsberechnung beilegen. | sg-wl-2025__c0086 | ☑️ |
> | 14 | 600 | Prämien und Sparzinsen | 4'500 | 2'500 | A = KK brutto 6'600 + Sparzinsen 68 − IPV 1'800 = 4'868. **K:** Max. 3'400 + 1'100 (Elias) = 4'500 → min = 4'500. **B:** Max. 1'800 + 700 (Elias) = 2'500 → min = 2'500. Kein Zuschlag «ohne Vorsorge», da 3a und BVG abgezogen werden. | sg-form-6-2025__c0001/c0002; sg-stg-2025__art-45-t2 | ☑️ |
> | 16.2 | 258 | Kinderbetreuung Elias (Kita/Tagesstruktur) | 8'760 | 8'760 | 9'840 − Mahlzeiten 1'080 = 8'760. Limite 26'700 (K) / 25'800 (B). | sg-form-1-2025__c0009; sg-stg-2025__art-45-t3 | ☑️ |
> | 16.4 | 223 | Excel-Kurs Klubschule (beruflich) | 400 | 340 | K: höherer Betrag aus Kosten (340) und Pauschale ohne Nachweis (400) → 400. B: nur effektive Kosten → 340. | sg-wl-2025__c0094; sg-stg-2025__art-45-t4 | ☑️ |
> | **18** | **230** | **Total Abzüge** | **40'518** | **33'548** | 13'600 + 7'258 + 6'000 + 4'500 + 8'760 + 400 bzw. 8'690 + 7'258 + 6'000 + 2'500 + 8'760 + 340 | | |
> 
> ## 3. Nettoeinkommen bis steuerbares Einkommen
> 
> | Ziff. | Code | Feld | Kanton | Bund | Rechenweg |
> |---|---|---|---|---|---|
> | 20 | 234 | Nettoeinkommen | **42'150** | **49'120** | 82'668 − 40'518 bzw. 82'668 − 33'548 |
> | 21.1 | 650/238/240 | Krankheitskosten (Vorkolonne 3'600) | 2'757 | 1'144 | Vorkolonne = Zahnarzt 2'750 (keine Drittzahlung) + KK-Kostenbeteiligung 850. Abzug = 3'600 − Selbstbehalt. K: 2 % × 42'150 = 843 → 2'757. B: 5 % × 49'120 = 2'456 → 1'144. |
> | 21.3 | 244 | Spenden (Caritas 80) | 0 | 0 | Unter Mindestbetrag Fr. 100 (siehe Abschnitt 5). |
> | 22 | 248 | Reineinkommen | 39'393 | 47'976 | 42'150 − 2'757 bzw. 49'120 − 1'144 |
> | 23.2 | 254 | Kinderabzug Elias (Schule/Kindergarten) | 10'800 | 6'800 | Bund: einheitlicher Kinderabzug. Der Abzug vom Steuerbetrag (263) setzt die Steuerbehörde automatisch um. |
> | **24** | **268** | **Steuerbares Einkommen** | **28'593** | **41'176** | 39'393 − 10'800 bzw. 47'976 − 6'800 |
> 
> Ziff. 23.1 (Vorschulkind) und 23.3 (Ausbildungskosten) entfallen. Es gibt keine Kindergarten-Kosten, und die Kita läuft über Ziff. 16.2.
> 
> ## 4. Vermögen (nur Kanton)
> 
> | Ziff. | Code | Feld | Betrag | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 30.1 | 300 | Sparkonto Raiffeisen 31.12.2025 | 31'500 | Steuerwert laut Bankauszug (Form. 2). sg-form-1-2025__c0012 |
> | 36.1–36.3 | 330 | Sozialabzüge | 95'000 | Alleinstehend 75'000 + Kind 20'000 (Elias, für den Kinderabzug geltend gemacht wird). sg-stg-2025__art-64 |
> | 37 | 338 | Steuerbares Vermögen | **0** | 31'500 − 95'000 < 0 → 0. Bund: kein Vermögen. |
> 
> Das Ergebnis bleibt 0, solange der Steuerwert eines Motorfahrzeugs unter 63'500 liegt (Ziff. 30.4). Ein Fahrzeug fehlt in den Belegen, daher ist die Angabe offen.
> 
> ## 5. Nicht zu deklarieren
> 
> | Beleg | Grund |
> |---|---|
> | Motorfahrzeugsteuer 410 | Privataufwand, kein Abzug. Im Wiki gibt es keine Fundstelle für einen Abzug. |
> | Auto-Haftpflicht/Kasko 1'020 | Motorfahrzeug- und Sachversicherungen sind nicht abziehbar (sg-form-6 / Ziff. 14 Beachten). |
> | Handy-Abo 720 | Privataufwand. Die Pauschale für übrige Berufskosten (Ziff. 10.1) deckt die Auslagen ab; kein separater Abzug. |
> | Caritas-Spende 80 | Unter dem Mindestbetrag Fr. 100 (Ziff. 21.3). Abzug nur, wenn die Spenden 2025 insgesamt mindestens 100 erreichen. |
> | Mittagessen-Mehrkosten Kita 1'080 | Verpflegung ist nicht abziehbar, daher nur 8'760 in Ziff. 16.2. |
> | Kinderzulage 2'400 separat | Bereits im Nettolohn 73'000 enthalten. |
> | Alimente als Abzug (Ziff. 12.2) | Nadine erhält die Alimente und zieht nichts ab. Der Abzug gehört dem Ex-Mann. Er darf Elias nicht als Kinderabzug geltend machen. |
> | 3a-Guthaben und PK-Ansprüche | Steuerfrei bis zur Fälligkeit, daher nicht im Vermögen deklarieren (sg-form-2 / Ziff. 30.1). |
> | Lohnausweis Ziff. 10.2 (0) | Entfällt. |
> 
> ## 6. Offen vor Einreichung
> 
> 1. **Begründung Arbeitsweg (Form. 4 Ziff. 1.3):** Die Fahrkosten werden nur mit Begründung anerkannt (kein zumutbarer ÖV oder Zeitersparnis über 60 Min./Tag). Die erste ÖV-Verbindung um 06:40 liegt nach dem Arbeitsbeginn um 06:00. Fahrplanauskunft beilegen. **Ohne Begründung** entfallen die Fahrkosten: Kanton steuerbar 36'753, Bund 44'641.
> 2. **Kita:** Betreuungszeiten mit der Arbeitszeit vergleichen, denn der Bund zieht Betreuung außerhalb der Arbeitszeit nicht ab. Zahlungsnachweise 2025 prüfen (nicht nur Rechnungen). Formular 10 mit Name und Adresse der Betreuungsstelle ausfüllen.
> 3. **Einkauf 6'000:** Bescheinigung und Einkaufsberechnung beilegen. Kein Vorbezug von Kapital in den letzten Jahren (sonst entfällt der Abzug).
> 4. **Krankheitskosten:** Leistungsabrechnung und Aufstellung beilegen, weil auf einen Krankenkassenauszug verwiesen wird. Die 850 Kostenbeteiligung ist dem Versicherten zuzuordnen.
> 5. **Säule 3a:** Bescheinigung Form. 21 EDP beilegen.
> 6. **Fahrzeug:** Anschaffungswert und Jahr fehlen für Ziff. 30.4.
> 7. **Alimente:** Bei erstmaliger Zahlung das Scheidungsurteil oder die Trennungsvereinbarung und den Zahlungsnachweis beilegen (Ziff. 6.1/12.2).
> 8. **Alleinerziehenden-Abzug:** Im Wiki ist kein eigener Abzug gefunden. Nicht angesetzt.
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

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


**Antwort des Agenten** (145.3 s · Tools: 22 Aufrufe steuerwiki__formular, steuerwiki__ablage, steuerwiki__position, steuerwiki__suche, steuerwiki__wert, steuerwiki__rechne):

> # Ausfüllhilfe Steuerjahr 2025, Kanton TG (natürliche Person, verwitwet, Rentnerin)
> 
> Alle Beträge in CHF. **K** = Staats- und Gemeindesteuer (linke Spalte), **B** = direkte Bundessteuer (rechte Spalte). Die Positionen folgen der Formularreihenfolge. Status: ☑️ = Fundstelle geprüft, Abnahme offen.
> 
> **Annahmen (bitte bestätigen):**
> - Wohnsitz TG am 31.12.2025, alleinstehend.
> - Keine Säule-2/3a-Beiträge, keine Kinder, keine Unterstützungsabzüge.
> - Krankenkasse ohne Prämienverbilligung.
> - Depot ist selbst verwaltet, keine Beteiligung ≥ 10 %.
> - Spenden an Krebsliga TG und Pro Senectute TG sind auf der TG-Liste der abzugsfähigen Institutionen.
> 
> ## 1. Einkünfte (Seite 2)
> 
> | Ziff. | Position / Code | K | B | Rechenweg · Fundstelle · Status |
> |---|---|---|---|---|
> | 3.1 | AHV-Rente (Code 130) | 27'000 | 27'000 | 12 × 2'250, voll steuerbar. Form. 1 Ziff. 3.1 ☑️ |
> | 3.2 | Pensionskasse-Rente (Code 132, Person 1) | 10'800 | 10'800 | 12 × 900 zu 100 %. Rentenbeginn 01.01.2020, daher kein Übergangsrecht 80 %. Fundstelle tg-wl-2025__c0077 ☑️ |
> | 4 | Wertschriften- und Zinserträge (Form. 2, Sp. 8 «mit VSt») | 2'350 | 2'350 | Dividenden 2'100 + Sparzins 250. Der Sparzins liegt über 200 und gehört deshalb in Sp. 8. Code 150 ☑️ |
> | 8.1 | Einkünfte Liegenschaft (Form. 7, Code 180) | 4'840 | 13'000 | Siehe Abschnitt 2. |
> | 9 | Total Einkünfte (Übertrag Seite 3, Ziff. 20) | **44'990** | **53'150** | 27'000 + 10'800 + 2'350 + Nettoerfolg |
> 
> ## 2. Liegenschaft: Eigenmietwert und Unterhalt (Form. 7 / 8)
> 
> - **Mietwert 2025 (indexiert):** 20'400 (Liegenschaftensteuerrechnung).
> - **Selbstnutzungsabzug:** Kanton 40 %, Bund entfällt. Die Liegenschaft ist am Wohnsitz dauernd selbstbewohnt, daher gilt der Abzug. Fundstellen tg-form-07-2025__c0002 und tg-stg__par-23.
> - **Unterhalt Pauschale oder effektiv:** Das Gebäude ist von 1986, also über 10 Jahre alt. Die Pauschale beträgt 20 % (K und B). Die Pauschale ergibt 4'080 (auf 20'400) bzw. 2'448 (K auf steuerbarem EMW 12'240). Effektiv sind es 7'400. Effektiv ist also günstiger. Wahl effektiv: Form. 8 ausfüllen.
> 
> | Effektive Unterhaltskosten (Form. 8, Zeile Anlage/Unterhalt) | Betrag | Abziehbar? |
> |---|---|---|
> | Malerarbeiten, Ersatzanstrich innen | 6'400 | ja (Unterhalt) |
> | Gartenpflege / Baumschnitt | 480 | ja (Unterhalt, Garten) |
> | Gebäudeversicherungsprämie | 520 | ja (Sachversicherung der Liegenschaft, tg-wl-2025__c0227) |
> | Wintergarten-Anbau (Neubau) | 31'000 | **nein**, nur Spalte «Anlagekosten/Mehrwert» |
> | **Total abziehbar** | **7'400** | |
> 
> - **Kanton:** 20'400 × (1 − 40 %) = 12'240; 12'240 − 7'400 = **4'840**.
> - **Bund:** 20'400 − 7'400 = **13'000**.
> - Fundstellen tg-wl-2025__c0222 bis c0238, bund-lkv__art-5. Status ☑️.
> 
> ## 3. Abzüge (Seite 3)
> 
> | Ziff. | Position / Code | K | B | Rechenweg · Fundstelle |
> |---|---|---|---|---|
> | 11 | Schuldzinsen (Form. 4.1, Code 290) | 3'150 | 3'150 | Hypothekarzinsen 2025. Limite: Erträge beweglich 2'350 + 50'000 = 52'350, daher voll abziehbar. Form. 4.1 A: Hypothekarbank mit Adresse und Zinssatz angeben. Schuld 180'000 (Ziff. 34). ☑️ |
> | 14 | Versicherungsprämien und Sparzinsen (Form. 5.2, Code 324 → 330) | 3'500 | 2'700 | A = KK-Prämien 6'240 + erhaltener Sparzins 250 = 6'490. Kanton-Max für Alleinstehende 3'500. Bund-Max ohne Säule 2/3a 2'700. Ergebnis: min(6'490; 3'500) bzw. min(6'490; 2'700). Fundstelle tg-form-05-2-2025__c0002 ☑️ |
> | 15.6 | Teilbesteuerung Beteiligungen | 0 | 0 | Nur bei Beteiligung ≥ 10 %. Annahme: keine. Fundstelle tg-form-02-2025__c0008 |
> | 19 | Total Abzüge (Übertrag Ziff. 21) | **6'650** | **5'850** | 3'150 + 3'500 bzw. 3'150 + 2'700 |
> 
> **Nettoeinkommen (Ziff. 22):** K = 44'990 − 6'650 = **38'340**; B = 53'150 − 5'850 = **47'300**.
> 
> | Ziff. | Position / Code | K | B | Rechenweg · Fundstelle |
> |---|---|---|---|---|
> | 23.1 | Krankheitskosten (Form. 5.1, Code 364) | 4'623 | 4'175 | A = Zahnarzt 4'440 + Brille 1'400 + Kostenbeteiligung 1'000 = 6'840. B1 = Vergütung Zusatz 300. A − B = 6'540. Selbstbehalt 5 %: K 1'917, B 2'365. Ergebnis 6'540 − 1'917 = 4'623 bzw. 6'540 − 2'365 = 4'175. Brille in A übrige Kosten, Zeile prüfen. ☑️ |
> | 23.2 | Freiwillige Zuwendungen (Form. 6, Code 366) | 350 | 550 | Krebsliga 300 + Pro Senectute 250 = 550. K: 550 − 200 = 350 (Max 8'000, da Netto ≤ 40'000). B: 550 (ohne Selbstbehalt, Max 20 % × 47'300 = 9'460). ☑️ |
> | 23.3 | Liquidationsgewinne | 0 | 0 | n/a |
> | 24 | Reineinkommen | **33'367** | **42'575** | K: 38'340 − 4'623 − 350. B: 47'300 − 4'175 − 550. |
> 
> ## 4. Sozialabzüge (Seite 3 unten)
> 
> | Ziff. | Position / Code | K | B | Rechenweg · Fundstelle |
> |---|---|---|---|---|
> | 25.3 | Abzug AHV-Altersrente / verwitwet (Code 388) | 1'000 | – | Nur Staat. Formel: 4'200 − 200 × volle Fr. 1'000 über 16'900 = 4'200 − 200 × 16 = 1'000. Bund: kein Abzug. ☑️, siehe Vorbehalt unten. |
> | 25.4 | Verheiratete (Code 390) | – | – | n/a |
> | 26 | **Steuerbares Einkommen** (Code 398) | **32'367** | **42'575** | 33'367 − 1'000 bzw. 42'575 |
> 
> ## 5. Vermögen (Seite 4)
> 
> | Ziff. | Position / Code | Betrag | Fundstelle |
> |---|---|---|---|
> | 30.1 | Wertschriften und Guthaben (Form. 2, Code 410) | 143'000 | Depot 95'000 (Steuerwert 31.12.) + Sparkonto 48'000 |
> | 31 | Liegenschaft Steuerwert (Form. 7, Code 430) | 410'000 | Liegenschaftenschätzung |
> | 33 | Total Vermögenswerte (Code 464) | 553'000 | 30.1 bis 31 |
> | 34 | Schulden (Form. 4.1, Code 466) | 180'000 | Hypothek 31.12.2025 |
> | 35 | Reinvermögen (Code 468) | 373'000 | 553'000 − 180'000 |
> | 36.2 | Freibetrag alleinstehend (Code 472, nur Kanton) | 100'000 | |
> | **37** | **Steuerbares Vermögen** (Code 498) | **K 273'000 / B –** | 373'000 − 100'000 |
> 
> ## 6. Hilfsblätter und Anhang
> 
> - **Form. 2, Ziff. 10 (Verrechnungssteuer-Rückerstattung):** 35 % × 2'350 = **822.50** (VSt 87.50 Konto + 735 Dividenden, stimmt). Voraussetzung: Wohnsitz TG am 31.12.2025 ✓.
> - **Form. 2, Sp. 9:** leer lassen.
> - **Form. 7 / Form. 8:** ausfüllen (siehe Abschnitt 2).
> - **Form. 5.1:** Brille 1'400 und Zahnarzt 4'440 in A. Kostenbeteiligung 1'000 in A1. Vergütung Zusatzversicherung 300 in B1. Kein behinderungsbedingter Abzug (Ziff. 17).
> - **Form. 5.2:** A.1 KK-Prämien 6'240 (keine Verbilligung). A.4 Sparzins 250. Total 6'490 (Code 324).
> - **Form. 6:** Krebsliga TG 300 und Pro Senectute TG 250 einzeln mit Name und Sitz eintragen.
> 
> ## 7. Nicht zu deklarieren / nicht abziehbar
> 
> | Beleg | Betrag | Grund |
> |---|---|---|
> | Wintergarten-Anbau | 31'000 | Neubau/Anbau. Nicht Unterhalt. Nur in Form. 8, Spalte «Anlagekosten/Mehrwert». Steuerwert kann bei neuer Schätzung steigen. |
> | Hausratversicherung | 380 | Hausrat- und Privathaftpflicht sind nicht abziehbar (tg-wl-2025__c0227). Nicht in Form. 5.2. |
> | Serafe-Rechnung | 335 | Private Lebenshaltungskosten, nicht abziehbar (tg-info-faq__c0024). Nicht separat im Wiki belegt. |
> | Handyrechnung | (Betrag?) | Private Lebenshaltungskosten, nicht abziehbar (tg-info-faq__c0024). Nur beruflicher Anteil wäre relevant; hier keiner. |
> 
> Nicht als eigene Abzüge: Krankenkassen-Prämien stehen in Ziff. 14, nicht bei den Krankheitskosten. Das Sparkonto-Guthaben ist Vermögen (Form. 2 Sp. 7), nicht ein Abzug.
> 
> ## 8. Offene Punkte und Vorbehalte
> 
> 1. **Depot-Verwaltungskosten (Code 148):** Nur abziehbar, wenn die Bank das Depot verwaltet. Pauschal 2 ‰ × 95'000 = 190 (K). Depotgebühren nicht geprüft für den Bund. Klären, ob Verwaltungsmandat besteht.
> 2. **Teilbesteuerung (15.6):** Nur bei Beteiligung ≥ 10 % am Grundkapital. Annahme: keine. Bei Ja: 40 % (K) bzw. 30 % (B) Abzug.
> 3. **Altersabzug 25.3:** Die Wegleitung-Tabelle hat einen Druckfehler (Zeile «36'900–37'689»). Die Formel ergibt bei 33'367 den Wert 1'000. Gegen WL S. 25 prüfen.
> 4. **Eigenmietwert:** Mietwert 20'400 und Steuerwert 410'000 stammen aus der Liegenschaftensteuerrechnung 2026 bzw. Schätzung. Bitte gegen die rechtskräftige Schätzung 2025 prüfen. Die Eigenmietwert-Basis Bund wird im Verfahren festgesetzt.
> 5. **Pauschale vs. effektiv:** Die effektive Variante ist für K und B günstiger. Die Wahl ist je Liegenschaft und Periode frei.
> 6. **Brille und Zahnarzt:** Die genaue Zeile in 5.1 A (A2–A8) im Formular prüfen.
> 7. **Spenden:** Beide Einzelspenden sind unter 1'000, also nur auf Verlangen zu belegen. Institutionen auf der TG-Liste prüfen.
> 8. **Einzureichende Belege:** AHV-Bescheinigung (Anspruch auf Altersabzug), PK-Rentenbescheinigung (ausdrücklich verlangt, tg-wl-2025__c0078), Depotauszug (ja), Steuerauszug TKB (bedingt, falls nur als Total deklariert), Hypothekarbestätigung mit Gläubiger-Adresse und Zinssatz.
> 
> ## Ergebnis-Übersicht
> 
> | | Kanton (K) | Bund (B) |
> |---|---|---|
> | Einkünfte (Ziff. 9) | 44'990 | 53'150 |
> | Abzüge (Ziff. 19) | 6'650 | 5'850 |
> | Nettoeinkommen (Ziff. 22) | 38'340 | 47'300 |
> | Reineinkommen (Ziff. 24) | 33'367 | 42'575 |
> | **Steuerbares Einkommen (Ziff. 26)** | **32'367** | **42'575** |
> | **Steuerbares Vermögen (Ziff. 37)** | **273'000** | – |
> 
> Die Ergebnisse sind Rechenhilfe anhand der Wiki-Eckwerte. Die fachliche Beurteilung bleibt bei der Fachperson.

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


**Antwort des Agenten** (165.1 s · Tools: 23 Aufrufe steuerwiki__formular, steuerwiki__position, steuerwiki__wert, steuerwiki__suche, steuerwiki__rechne):

> # Ausfüllhilfe Steuererklärung AR 2025, Ehepaar Herisau
> 
> **Annahmen:** Kanton AR, Wohnsitz 31.12.2025 Herisau. Die Einkünfte stehen mit dem Nettolohn (Lohnausweis Ziff. 11) in Ziff. 1.1, weil die Lohnabzüge AHV/BVG darin schon enthalten sind. Lea (geb. 14.03.2021) hat am 31.12.2025 ihr 4. Altersjahr vollendet und fällt damit in Ziff. 23.2. Jonas (geb. 02.09.2009) ist 16 und in Ausbildung. Die Bundesspalte entfällt: Abweichungen für den Bund nimmt die Steuerverwaltung automatisch vor, deshalb führe ich Kanton und Bund getrennt nur dort, wo die Werte abweichen.
> 
> Die Status-Angaben stehen in Klammern: ☑️ = Fundstelle geprüft, Abnahme offen. Bei einigen Codes steht im Wiki „nicht verifiziert“, das gilt für die Codes der Ziffern 13.1, 14, 16.2, 17 und 30.1. Am Originalformular prüfen.
> 
> ## 1. Einkünfte
> 
> | Ziff. | Position | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 1.1 (Code 100) | Haupterwerb P1 | 85'300 | 85'300 | Nettolohn 98'000 − 6'860 − 5'840 = 85'300 (☑️) |
> | 1.1 (Code 102) | Haupterwerb P2 | 68'200 | 68'200 | 82'000 − 5'740 − 4'060 − 4'000 = 68'200. Zulagen sind im Lohn enthalten, daher nicht in 3.5. |
> | 4.1 | Wertschriften/Guthaben | 1'410 | 1'410 | Zinsen 160 (Spalte B, ≤ 200) + Dividenden 1'250 (Spalte A). Form. 2 ☑️ |
> | 7 | Total Einkünfte | 154'910 | 154'910 | 85'300 + 68'200 + 1'410 |
> 
> Die Verrechnungssteuer von 437.50 (35 % von 1'250) ist ein Anspruch auf Rückerstattung (Form. 2), kein Abzug. Eine Teilbesteuerung nach Ziff. 4.2 entfällt, sofern keine Beteiligung ≥ 10 % vorliegt (Annahme).
> 
> ## 2. Abzüge
> 
> | Ziff. | Position | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 10.1 (P1, Code 438) | Berufskosten P1 | 4'000 | 4'159 | Fahrkosten 0 (Lohnausweis Feld F angekreuzt, ☑️). Verpflegung Form. 4 Ziff. 2.2 (Code 410): 7.50 × 220 = 1'650, gedeckelt auf 1'600 (Bund ebenso). Pauschale Ziff. 3: Kanton 700 + 10 % × 85'300 = 9'230 → max. 2'400; Bund 3 % × 85'300 = 2'559 (Min 2'000 / Max 4'000). Quellen: Form. 4, `ar-stv__art-18`, `bund-bkv-2025__anhang-1` |
> | 10.2 (P2, Code 488) | Berufskosten P2 | 6'300 | 5'946 | ÖV-Abo 1'260 (Form. 4 Ziff. 1.1, Code 450). Mittagsverpflegung Ziff. 2.1 (Code 458): 15 × 176 = 2'640 (≤ 3'200). Pauschale: Kanton 700 + 10 % × 68'200 → max. 2'400; Bund 3 % × 68'200 = 2'046. |
> | 13.1 | Säule 3a | 12'258 | 12'258 | P1 min(7'258; 7'258) = 7'258; P2 min(5'000; 7'258) = 5'000. Beide haben eine 2. Säule. `ar-wl-2025__c0003` ☑️ |
> | 13.2 | Einkauf 2. Säule | 0 | 0 | P2 hat 4'000 Einkauf bereits im Lohn (Lohnausweis Ziff. 10.2) abgezogen. Nicht doppelt erfassen. |
> | 14 | Versicherungsprämien und Sparzinsen | 7'400 | 5'100 | Teil A: KK 13'900 + Sparzinsen 160 = 14'060. Teil B Kanton: 5'400 + 2 × 1'000 (Kinder mit Abzug) = 7'400; Bund: 3'700 + 2 × 700 = 5'100. Abzug = min(A; B). Keine Prämienverbilligung. `ar-form-06-2025__c0001/c0002` ☑️ |
> | 16.2 | Kinderbetreuung (Lea) | 10'200 | 10'200 | 14'400 − Mittagessen 1'800 − Betreuungsbeitrag 2'400 = 10'200 (≤ 25'000 / 25'800). Beide Eltern erwerbstätig. Form. 10, `ar-form-10-2025__c0001` ☑️ |
> | 17 | Zweiverdienerabzug | 5'200 | 14'100 | Kanton: E = 68'200 − 6'300 − 5'000 = 56'900; 10 % = 5'690 → max. 5'200. Bund: E = 68'200 − 5'946 − 5'000 = 57'254; 50 % = 28'627 → max. 14'100. `ar-wl-2025__c0004`, `bund-dbg-2025__art-33-t6` ☑️ |
> | 18 | Total Abzüge | 45'358 | 51'763 | 10'300 + 12'258 + 7'400 + 10'200 + 5'200 bzw. 10'105 + 12'258 + 5'100 + 10'200 + 14'100 |
> | 20 | Nettoeinkommen | 109'552 | 103'147 | 154'910 − Total Abzüge |
> 
> ## 3. Zuwendungen, Sozialabzüge, steuerbares Einkommen
> 
> | Ziff. | Position | Kanton | Bund | Rechenweg / Fundstelle |
> |---|---|---|---|---|
> | 21.3 (Code 550) | Spende Krebsliga 300 | 300 | 300 | Min. 100 erfüllt. Max. 20 % × Nettoeinkommen = 21'910 bzw. 20'629, nicht bindend. Form. 5 Teil A ☑️ |
> | 22 | Reineinkommen | 109'252 | 102'847 | 109'552 − 300 bzw. 103'147 − 300 |
> | 23.2 | Kind Lea (4–15 J.) | 7'400 | 6'800 | Bund pro Kind 6'800 |
> | 23.3 | Kind Jonas (Ausbildung) | 11'600 | 6'800 | Kanton nur bei Einkünften des Kindes ≤ 18'000 (siehe offene Punkte) |
> | 24 | Steuerbares Einkommen | 90'252 | 86'447 | Kanton: 109'252 − 19'000. Bund: 102'847 − 13'600 − 2'800 (Verheiratete) |
> 
> ## 4. Vermögen (nur Kanton)
> 
> | Ziff. | Position | Betrag | Rechenweg |
> |---|---|---|---|
> | 30.1 (Code 300) | Wertschriften und Guthaben | 92'000 | Konten 54'000 + Aktien-Steuerwert 38'000 (Form. 2). Ansprüche aus 3a/2. Säule nicht deklarieren. |
> | 33 / 35 | Total Vermögenswerte / Reinvermögen | 92'000 | keine Schulden (Mieter, keine Liegenschaft) |
> | 36.2 (Code 332) | Sozialabzug verheiratet | 150'000 | |
> | 36.3 (Code 334) | Sozialabzug je minderjähriges Kind | 2 × 25'000 | Lea und Jonas sind minderjährig |
> | 37 | Steuerbares Vermögen | 0 | max(0; 92'000 − 150'000 − 50'000) |
> 
> Die Rechnungen habe ich mit `rechne` geprüft.
> 
> ## 5. Offene Punkte vor der Abgabe
> 
> 1. **Jonas' Einkünfte:** Der Kanton-Kinderabzug von 11'600 entfällt bei eigenen Einkünften über 18'000. Bei Wegfall steigt das Kanton-steuerbare Einkommen auf 101'852. Bitte Lehrlingslohn oder Nebenjob prüfen.
> 2. **P2 Mittagsverpflegung (Ziff. 2.1, 2'640):** Angenommen, eine Heimkehr ist von St. Gallen aus nicht zumutbar. Ist sie zumutbar, fällt der Abzug weg (Kanton steuerbar 92'892, Bund 89'087).
> 3. **P1 Kantine (Ziff. 2.2, 1'600):** Der Abzug gilt nur, wenn die Kantine Mehrkosten gegenüber Zuhause verursacht. Entfällt er, steigt das steuerbare Einkommen um 1'600 (Kanton 91'852, Bund 88'047).
> 4. **Lea-Abzugsstufe:** Ich habe 23.2 angesetzt, weil sie das 4. Altersjahr vollendet hat. Liest man den Stichtag anders, ergäbe 23.1 (5'300) ein Kanton-steuerbares Einkommen von 92'352.
> 5. **Dividenden-Teilbesteuerung (Bund):** Setzt eine Beteiligung von mindestens 10 % voraus. Dazu fehlen Angaben.
> 6. **Codes:** Die Codes 13.1, 14, 16.2, 17, 21.3 und 30.1 sind im Wiki nicht durchgehend verifiziert. Am Originalformular prüfen.
> 
> ## 6. Nicht zu deklarieren
> 
> - **Steuerschlussrechnung 2024 (9'870):** Das Formular hat keine Position für Steuerzahlungen als Abzug. Ein Abzug ist nicht vorgesehen. Im Wiki habe ich dazu keine ausdrückliche Fundstelle gefunden.
> - **Handy-Abo (960):** Private Lebenshaltungskosten. Berufliche Auslagen deckt die Pauschale ab.
> - **Turnverein-Beitrag (120):** Mitgliederbeitrag, nicht abziehbar (Form. 5 „Beachten“).
> - **Kita-Mittagessen (1'800):** Verpflegung ist bei der Kinderbetreuung nicht abziehbar (`ar-wl-2025__c0091`).
> - **Lohnabzüge AHV/BVG und BVG-Einkauf 4'000:** Schon im Nettolohn enthalten, nicht erneut erfassen.
> - **Kinder- und Ausbildungszulagen P2 (im Bruttolohn):** Nicht in Ziff. 3.5 erfassen. Ziff. 3.5 gilt nur für direkt von der Ausgleichskasse ausbezahlte Zulagen.
> - **Fahrkosten P1:** Der Werkbus ist unentgeltlich (Feld F), daher kein Abzug.
> - **Verrechnungssteuer (437.50):** Keine Abzugsposition, sondern ein Rückerstattungsanspruch über Form. 2.
> 
> ## 7. Beilagen
> 
> - Lohnausweise beider Personen (Pflicht)
> - Säule-3a-Bescheinigungen (Pflicht)
> - Einkaufsbestätigung P2 (nur nötig, falls Ziff. 13.2 geltend gemacht wird; hier nicht)
> - Bank-Steuerauszug vollständig (bedingt, Form. 2)
> - Spendenbescheinigung und Prämienbescheinigung, auf Verlangen
> - Kita-Rechnungen mit Empfänger, auf Verlangen
> 
> Die fachliche Beurteilung bleibt bei der Fachperson.

