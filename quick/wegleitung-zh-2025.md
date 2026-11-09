---
typ: wegleitung-kompakt
titel: Kompakt-Wegleitung ZH 2025
jur: zh
jahre:
- 2025
generiert: tools/build_quick.py aus data/zuordnung/zh/2025.yaml (2026-11-09)
---

# Kompakt-Wegleitung Kanton Zürich (ZH) – Steuerjahr 2025

> Je Formularposition: **Rein** (welche Dokumente → welches Feld) · **Rechnen** (Kurzformel) · **Limite** (Kanton / Bund) · **Beachten**. Volle Regel, Bund-Hinweis und wörtliche Zitate: ↗ Detail. Formular: Steuererklärung 2025 Kanton Zürich (StA Form. · [Tabelle](zuordnung-zh-2025.md) · [Eckwerte](werte-zh-2025.md) · [Gültigkeit 2025](gueltigkeit-2025.md)

> **Hinweis:** Codes bezeichnen Zeilen, nicht Spalten.

**Abschnitte:** Einkünfte (22) · Abzüge (19) · Einkommensberechnung (13) · Vermögen (15) · Weitere Angaben (4) · Hilfsblatt Berufskosten (Form. 360) (11) · Hilfsblatt Versicherungsprämien (Form. 365) (6) · Hilfsblatt Wertschriftenverzeichnis (Form. 340) (5) · Hilfsblatt Schulden (Form. 355) (2) · Hilfsblatt Liegenschaften (Form. 350) (5) · Hilfsblatt Krankheitskosten (Form. 370) (8) · Hilfsblatt Weiterbildung (Form. 367) (1) · Lohnausweis-Regeln (5)

## Einkünfte

### 1.1 · Haupterwerb unselbständig, Person 1 / Person 2 (Code 100/101) ☑️
- **Rein:** Lohnausweis (je Arbeitgeber) → Ziff. 11 Nettolohn / Rente · Lohnausweis → Ziff. 8 Bruttolohn, Ziff. 9 AHV/IV/EO/ALV/NBUV, Ziff. 10.1/10.2 BVG (Plausibilität)
- **Rechnen:** je Person: Σ LA Ziff. 11 (= Ziff. 8 − Ziff. 9 − Ziff. 10.1 − Ziff. 10.2) aller Haupterwerbe → Code 100 (P1) / 101 (P2); Kanton = Bund
- **Beachten:** Erwerbslücken ausdrücklich bezeichnen (zeigt, dass keine Einkommensbescheinigung vergessen wurde).
- **Beachten:** BVG-Einkauf im LA (Ziff. 10.2) ist schon abgezogen – nicht nochmals in Ziff. 16.1 (Code 280).
- **Beachten:** Zum Lohn gehören auch Spesen ohne entsprechende Ausgaben, Naturalbezüge, Mitarbeiterbeteiligungen.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#1-1-einkommen-unselbstaendig-haupterwerb) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md)

### 1.2 · Nebenerwerb unselbständig inkl. Behörden-/VR-Entschädigungen, Person 1 / Person 2 (Code 102/103) ☑️
- **Rein:** Lohnausweis Nebenerwerb → Ziff. 11 Nettolohn · Lohnausweis → Ziff. 6 Verwaltungsratsentschädigungen; Honorarabrechnung (Behörde, Vorstand, Tantiemen, Lizenzen) · Aufstellung effektive Auslagen (nur wenn > Pauschale)
- **Rechnen:** Σ LA Ziff. 11 Nebenerwerbe → 102 (P1) / 103 (P2); Auslagen Form. 360 Ziff. 5: max(800; min(20 % × Nebeneinkünfte; 2’400)) → 216|217 (P2: 236|237); Kanton = Bund
- **Limite (Kanton / Bund):** Pauschale in % der Nebeneinkünfte: 20 % / 20 % · Pauschale Minimum (CHF): CHF 800 / CHF 800 · Pauschale Maximum (CHF): CHF 2'400 / CHF 2'400
- **Beachten:** Im vereinfachten Verfahren (BG gegen Schwarzarbeit) abgerechnete Einkünfte nicht hier – nur Bescheinigung beilegen.
- **Beachten:** Behördenentschädigungen: Verfügung der Finanzdirektion ZStB 17.3 beachten.
- **Beachten:** Effektive Auslagen > Pauschale: Aufstellung beilegen, auf Verlangen voller Nachweis.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#1-2-einkommen-unselbstaendig-nebenerwerb) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md)

### 1.2 · Im vereinfachten Verfahren abgerechnete Einkünfte (Bescheinigung AHV-Ausgleichskasse) ☑️
- **Rein:** Bescheinigung der AHV-Ausgleichskasse (vereinfachtes Abrechnungsverfahren) → nur als Beilage
- **Rechnen:** Kein Betrag in Ziff. 1.2 (Code 102/103) für Einkünfte mit Quellensteuer nach BG gegen die Schwarzarbeit; nur Bescheinigung beilegen
- **Beachten:** Nur für tatsächlich im vereinfachten Verfahren abgerechnete Löhne; übrige Nebenlöhne → Ziff. 1.2 (Lohnausweis).
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#1-2-einkommen-vereinfachtes-verfahren) · [WL ZH 2025 S. 10](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0033.md)

### 2.1 · Selbständige Erwerbstätigkeit Haupterwerb, Person 1 / Person 2 (Code 120/121) ☑️
- **Rein:** Jahresrechnung (Bilanz, Erfolgsrechnung, Anhang, unterzeichnet) + Kontoblätter Privat-/Eigenkapitalkonten · Hilfsblatt A (kaufm./vereinfachte Buchführung) → Ziff. 5 Code 1750; Landwirtschaft: Hilfsblatt B bzw. G · Abrechnung persönliche AHV/IV/EO-Beiträge → HB A Ziff. 4.1 (1741) aufrechnen, Abzug Ziff. 16.1 · Liquidation: Hilfsformular «Liquidationsgewinn bei Aufgabe der selbständigen Erwerbstätigkeit» (Abzug Ziff. 16.5)
- **Rechnen:** HB A: Reingewinn 1810 ± Korrekturen 1811–1815 = AHV-Einkommen 1740 + AHV/IV/EO 1741 − Wertschriftenerträge im WV 1742 − weitere 1743 = 1750 → 120/121
- **Beachten:** Eigene BVG-Beiträge im Geschäft nur wie AG-Anteil Personal (sonst Hälfte, ohne Einkäufe); Rest, Einkäufe, 3a in der StE.
- **Beachten:** Grundstückgewinn Geschäftsvermögen: Bund voll; Staat freizustellenden Teil in Ziff. 16.5 (Kolonne Staat) abziehen.
- **Beachten:** Liquidationsgewinn (Aufgabe nach vollendetem 55. Altersjahr/Invalidität, letzte 2 GJ): gesondert, Abzug Ziff. 16.5.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#2-1-einkommen-selbstaendig) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md)

### 2.2 · Selbständige Erwerbstätigkeit Nebenerwerb, Person 1 / Person 2 (Code 122/123) ☑️
- **Rein:** Hilfsblatt A (Nebenerwerb, Code 1692/1693) → Ziff. 5 Einkünfte (Code 1750) · bzw. eigene Aufstellung der Nebentätigkeit (statt Hilfsblatt) · Kauf-/Verkaufsabrechnungen Wertschriften/Liegenschaften (nur bei Tätigkeit über schlichte Vermögensverwaltung hinaus)
- **Rechnen:** Ergebnis Hilfsblatt A Ziff. 5 (1750) bzw. Aufstellung → Code 122 (P1) / 123 (P2); Kanton = Bund (Ausnahme Grundstückgewinn, s. beachten)
- **Beachten:** Veräusserungsgewinne Wertschriften/Liegenschaften nur, wenn Tätigkeit die schlichte Vermögensverwaltung übersteigt.
- **Beachten:** Grundstückgewinn: Staat freizustellenden Teil in Ziff. 16.5 abziehen; Liegenschaftenhändler: § 221 Abs. 2 StG.
- **Beachten:** Unselbständige Nebenerwerbe (mit Lohnausweis) gehören in Ziff. 1.2, nicht hierher.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#2-2-einkommen-selbstaendig) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md)

### 3.1 · AHV-/IV-Renten (100 %), Person 1 / Person 2 (Code 130/131) ☑️
- **Rein:** Rentenbescheinigung AHV bzw. IV (Ausgleichskasse) → Jahresbetrag 2025 je Person
- **Rechnen:** Σ AHV-/IV-Renten 2025 × 100 % je Person → Code 130 (P1) / 131 (P2); Kästchen AHV oder IV ankreuzen; Kanton = Bund
- **Beachten:** EL, Hilflosenentschädigung, Pflegebeiträge an AHV-/IV-Bezüger sind steuerfrei – nicht hier erfassen.
- **Beachten:** Renten aus 2. Säule/3a/Arbeitgeber/UVG gehören in Ziff. 3.2 (Code 134–137).
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#3-1-einkommen-sozialversicherung-ahv-iv) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md)

### 3.2 · Renten / Pensionen (2. Säule, 3a, Arbeitgeber, UVG, Militärversicherung), Person 1 / 2 (Code 134/135 bzw. 136/137; … ☑️
- **Rein:** Rentenbescheinigung Pensionskasse/Versicherer → Bruttorente 2025 (Vorkolonne «Betrag») · Rentenbeginn und Eigenbeitragsanteil (nur für 80 %-Altfälle) · Bescheinigung SUVA/UVG-Versicherer, Militärversicherung, Arbeitgeber, 3a-Stiftung
- **Rechnen:** Hauptkolonne = Betrag × Prozente: Vorkolonnen 960/961 → 134, 962/963 → 135 (P1), 964/965 → 136, 966/967 → 137 (P2); i.d.R. 100 %
- **Beachten:** 80 %: Rentenbeginn vor 1987 bzw. 1987–2001 mit Vorsorgeverhältnis schon Ende 1985 (Bund: 1986) und Eigenbeitrag ≥ 20 %.
- **Beachten:** UVG 60 % (Prämien allein selbst) bzw. 80 % (≥ 20 % selbst) nur bei Nichtberufsunfall vor 1986; AG, 3a, MV 100 %.
- **Beachten:** MV steuerfrei: Invaliden-/Hinterlassenenrenten mit Beginn vor 1994, Integritätsschadensrenten, Genugtuung.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#3-2-einkommen-vorsorge-renten) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md)

### 3.2 (Leibrenten) · Leibrenten / Verpfründung (private, Versicherer, ausländisch) – Code 134–137 ⚠️
- **Rein:** Steuerbescheinigung des Versicherers (Leibrentenversicherung) → steuerbarer Ertragsanteil · Private/ausländische Leibrente, Verpfründung: Leibrentenvertrag (Kopie) + ESTV-Berechnungssatz der Steuerperiode · Zahlungsnachweis erhaltene Rente 2025 → Gesamtbetrag (Vorkolonne «Betrag»)
- **Rechnen:** Vorkolonne = Gesamtrente; Hauptkolonne = Ertragsanteil lt. Versicherer bzw. Rente × Berechnungssatz / 100; «Prozente» leer. Bund: Art. 22 Abs. 3 DBG
- **Beachten:** STRITTIG: StG § 22 Abs. 3 = 40 %, WL 2025 = flexibler Ertragsanteil (StHG Art. 72 → WL); Fachperson entscheidet.
- **Beachten:** Bund lit. b: Überschussleistungen 70 %; lit. c (ausländ. LRV, Leibrenten-/Verpfründungsvertrag): Rendite zehnj. BO + 0,5 Pp.
- **Beachten:** Bescheinigung bzw. Vertragskopie zwingend mit der Steuererklärung einreichen.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#3-2-leibrenten-einkommen-vorsorge-uebrige-renten) · [WL ZH 2025 S. 11](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0052.md)

### 3.3 · Erwerbsausfallentschädigungen aus Arbeitslosenversicherung, direkt ausbezahlt (Code 140/141) ☑️
- **Rein:** Bescheinigung der Arbeitslosenkasse → Jahresbetrag 2025 direkt ausbezahlter Entschädigungen je Person
- **Rechnen:** Σ direkt von der Arbeitslosenkasse ausbezahlte Erwerbsausfallentschädigungen 2025 → Code 140 (P1) / 141 (P2); Kanton = Bund
- **Beachten:** Nur direkt ausbezahlte Entschädigungen; über den Arbeitgeber (Lohnausweis) abgerechnete nicht doppelt erfassen.
- **Beachten:** Bescheinigung beilegen.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#3-3-einkommen-ersatz-taggelder) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md)

### 3.4 · Taggelder KV/UV/IV/MV, EO und Mutterschaftsentschädigung, direkt ausbezahlt (Code 142/143) ☑️
- **Rein:** Taggeldabrechnung/Bescheinigung KV, UV, IV, MV → Jahresbetrag direkt ausbezahlter Taggelder · Bescheinigung Ausgleichskasse → EO-/Mutterschaftsentschädigung (direkt ausbezahlt)
- **Rechnen:** Σ direkt ausbezahlte Taggelder + EO/Mutterschaftsentschädigung (+ direkt ausbezahlte Familienzulagen) je Person → Code 142 (P1) / 143 (P2)
- **Beachten:** Nur wenn nicht im Lohnausweis bescheinigt und mit dem Lohn in Ziff. 1 übertragen.
- **Beachten:** Bescheinigung bei der Versicherungseinrichtung verlangen und beilegen.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#3-4-einkommen-ersatz-taggelder) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md)

### 3.4 · Kinder- und Familienzulagen, direkt von der Ausgleichskasse ausbezahlt (Code 142/143) ☑️
- **Rein:** Bescheinigung der Familienausgleichskasse → direkt ausbezahlte Kinder-/Familienzulagen 2025
- **Rechnen:** Σ direkt von der Ausgleichskasse ausbezahlte Kinder-/Familienzulagen → Code 142 (P1) / 143 (P2), zusammen mit Taggeldern
- **Beachten:** Über den Arbeitgeber (Lohnausweis) ausbezahlte Zulagen sind bereits im Lohn Ziff. 1 – nicht doppelt.
- **Beachten:** Bescheinigung beilegen.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#3-4-einkommen-ersatz-familienzulagen) · [WL ZH 2025 S. 12](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0055.md)

### 3 (steuerfrei) · Steuerfreie Unterstützungsleistungen (EL, Hilflosenentschädigung, Pflegebeiträge) – nicht deklarieren ☑️
- **Rein:** Verfügung/Bescheid EL, Hilflosenentschädigung, Pflegebeiträge, Beihilfen, Gemeindezuschüsse → nicht übertragen (nur Abgrenzung)
- **Rechnen:** Kein Betrag in Ziff. 3 (nicht steuerbar); gilt für Unterstützungen an Bezüger von AHV-/IV-/UVG-Leistungen
- **Beachten:** Steuerfrei auch (MV): Invaliden-/Hinterlassenenrenten mit Beginn vor 1994, Integritätsschadensrenten, Genugtuung.
- **Beachten:** AHV-/IV-Renten selbst bleiben zu 100 % steuerbar (Ziff. 3.1).
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#3-steuerfrei-info-steuerfreie-leistungen) · [WL ZH 2025 S. 12](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0053.md)

### 4.1 · Ertrag aus Wertschriften, Guthaben und Lotterien (Code 150) – Total Bruttoertrag A + B laut Wertschriftenverzeichnis ☑️
- **Rein:** (e)Steuerauszug Bank → Bruttoerträge Kol. A/B und Steuerwerte 31.12.2025 (Import in Online-Steuererklärung möglich) · Zinsausweise Konti, Dividenden-/Fondsabrechnungen; Kursliste ESTV (steuerbare Werte Anlagefonds) · Krypto: Wallet-Kontoauszug per Ende Steuerperiode → Steuerwert (ESTV-Jahresendsteuerkurs) · Ausländ. Dividenden/Zinsen mit Quellensteuer-Anrechnung → Formular DA-1 (Total Bruttoertrag in Kol. B)
- **Rechnen:** Form. 340: Total Bruttoertrag 150 = Zwischentotal A 539 + B 542 → Ziff. 4.1; VSt-Anspruch 540 = 35 % × 539; Steuerwert 400 → Ziff. 30.1
- **Beachten:** Kol. A = mit VSt (CH-Zinsen > CHF 200, CH-Dividenden/Fonds); Kol. B = ohne VSt (Zins bis CHF 200, ausländische Titel).
- **Beachten:** Kinder Jg. 2008 und jünger beim Elternteil; Vorsorgeguthaben (2. Säule, 3a) nicht ins WV.
- **Beachten:** Thesaurierte Fondserträge und Gratisaktien (ab 1.1.2020) steuerbar; gesondert ausgewiesene Fonds-Kapitalgewinne (PV) frei.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#4-1-einkommen-wertschriften) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md)

### 4.1 (Lotterie) · Lotterie-/Grossspiel-/Sportwettengewinne (im Wertschriftenverzeichnis, Kolonne A/B) ☑️
- **Rein:** Gewinnbescheinigung Lotteriegesellschaft / Bank bzw. Auszahlungsabschnitt Post → Bruttogewinn (Original beilegen) · Kontoauszug Online-Spielbank → Gewinne und effektive Einsätze
- **Rechnen:** Grossspiele/Online-Spielbanken je Gewinn: max(0; Gewinn − Kanton 1’033’000 / Bund 1’070’400); Verkaufsförderung: Gewinn > Kanton 1’000 / Bund 1’100 → ganzer Gewinn
- **Limite (Kanton / Bund):** Grossspielgewinne steuerfrei bis (CHF): CHF 1'033'000 / CHF 1'070'400 · Lotterie-/Kleingewinne steuerfrei bis (CHF): CHF 1'000 / CHF 1'100
- **Beachten:** Mit VSt → Kol. A; ausländ. Geldspiele und Naturaltreffer → Kol. B (Naturalgewinne: Freigrenze Kanton 1’000 / Bund 1’100).
- **Beachten:** 16.5: Einsatzkosten 5 %, max. Kanton 5’200 / Bund 5’400; Online-Spielbank eff. Einsätze, max. Kanton 25’800 / Bund 26’800
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#4-1-lotterie-einkommen-lotterie-gewinne) · [WL ZH 2025 S. 26](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0167.md)

### 4.2 · Davon aus qualifizierten Beteiligungen (Code 151) – Erträge aus Beteiligungen ≥ 10 % ☑️
- **Rein:** Steuerauszug / Dividendenabrechnung bzw. Ausschüttungsbescheinigung (nicht kotiert) → Bruttoausschüttung · Nachweis Beteiligungsquote (≥ 10 % Grund-/Stammkapital) → Code Q im WV · Formular «Qualifizierte Beteiligungen im Privatvermögen» → Teilbesteuerungsabzug Ziff. 16.5
- **Rechnen:** Σ Bruttoausschüttungen mit Code Q (Kol. A + B) → Code 151 («davon», bereits in 150); Teilbesteuerungsabzug Ziff. 16.5 (Code 284): Kanton 50 % / Bund 30 %
- **Beachten:** Ziff. 4.2 nicht zusätzlich zu Ziff. 4.1 addieren (Davon-Position).
- **Beachten:** Q im Geschäftsvermögen: Ertrag in Ziff. 2 (HB A); soweit im WV aufgeführt, in HB A Code 1742 abziehen.
- **Beachten:** Gratis abgegebene Mitarbeiteraktien: kein Teilbesteuerungsabzug.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#4-2-einkommen-beteiligungen-qualifiziert) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md)

### 5.1 · Unterhaltsbeiträge vom geschiedenen / getrennten Ehegatten (Code 160) ☑️
- **Rein:** Scheidungsurteil / Trennungsvereinbarung → vereinbarter Unterhalt · Bank-/Zahlungsbelege → Jahressumme 2025 erhalten; Name/Adresse Alimentenzahler/in
- **Rechnen:** Σ 2025 erhaltene Unterhaltsbeiträge für die Person selbst (voll) → Code 160; Kanton = Bund
- **Beachten:** Gilt für geschiedene, gerichtlich oder tatsächlich getrennt lebende Ehegatten/Partner.
- **Beachten:** Kinderalimente separat in Ziff. 5.2 (161); Gegenstück beim Zahler: Abzug Ziff. 13.1 (Code 254).
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#5-1-einkommen-unterhaltsbeitraege) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md)

### 5.2 · Unterhaltsbeiträge für minderjährige Kinder (bis Monat der Volljährigkeit) (Code 161) ☑️
- **Rein:** Scheidungsurteil / Unterhaltsvertrag → Kinderunterhalt je Kind · Zahlungsbelege bzw. Abrechnung Alimentenbevorschussung → Beträge bis Monat des 18. Geburtstags
- **Rechnen:** Σ je Kind: erhaltene Alimente + Bevorschussungen bis und mit Monat, in dem das Kind 18 wird → Code 161; Kanton = Bund
- **Beachten:** Zahlungen nach dem Monat des 18. Geburtstags nicht mehr als Einkommen deklarieren.
- **Beachten:** Gilt auch für ledige Steuerpflichtige; Gegenstück beim Zahler: Abzug Ziff. 13.2 (Code 255).
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#5-2-einkommen-unterhaltsbeitraege) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md)

### 5.3 · Ertrag aus Geschäfts- und Korporationsanteilen / unverteilten Erbschaften (Code 162) ☑️
- **Rein:** Abrechnung Geschäfts-/Korporationsanteil → Ertrag und Beteiligungsquote · Erbschaft: Erbbescheinigung/Aufstellung Erbengemeinschaft → Erbquote, Erträge ab Folgetag des Todestags
- **Rechnen:** Geschäfts-/Korporationsanteil: Ertrag × Beteiligungsquote → Code 162; unverteilte Erbschaft: Erträge (Folgetag Todestag bis 31.12.) × Erbquote → WV (150) bzw. LV (188)
- **Beachten:** Erbschaftsvermögen anteilig zum Steuerwert 31.12. (WV/LV); Schulden und Schuldzinsen anteilig → Schuldenverzeichnis.
- **Beachten:** Aufstellung beilegen: Erblasser (Todesdatum), Erben mit Quoten, Vermächtnisse, Werte/Erträge, Kosten, Schulden.
- **Beachten:** Erbengemeinschaft wird nicht separat besteuert; jeder Erbe nach seiner Erbquote.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#5-3-einkommen-erbschaften-unverteilt) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md)

### 5.4 · Weitere Einkünfte, nähere Bezeichnung (Code 163) ☑️
- **Rein:** Aufstellung/Belege: im Lohnausweis nicht ausgewiesene Trinkgelder, wiederkehrende Zahlungen bei Tod oder bleibenden Nachteilen · Bestätigung Bundesbeitrag an vorbereitende Kurse auf eidg. Prüfungen + effektive Weiterbildungskosten
- **Rechnen:** Σ übrige steuerbare Einkünfte inkl. Naturalbezüge → Code 163; Bundesbeitrag nur soweit > geltend gemachte effektive Weiterbildungskosten
- **Beachten:** Grundsätzlich alle wiederkehrenden und einmaligen Einkünfte steuerbar; Ausnahmen nur gesetzlich steuerfreie.
- **Beachten:** Bei Unsicherheit über die Steuerbarkeit: zuständiges Gemeindesteueramt.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#5-4-einkommen-uebrige) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md)

### 5.5 · Kapitalabfindungen für wiederkehrende Leistungen (Code 164) ☑️
- **Rein:** Bescheinigung/Abrechnung der auszahlenden Stelle → Abfindungsbetrag und abgegoltene Anzahl Monate
- **Rechnen:** Abfindung → Code 164; Anzahl Monate → Vorkolonne (1641); Satzbestimmung zum Betrag der jährlichen Leistung
- **Beachten:** Kapitalleistungen aus Vorsorge nicht hier → Seite 4, Ziff. 40.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#5-5-einkommen-kapitalabfindung-wiederkehrend) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md)

### 6 · Nettoertrag aus Liegenschaften (Code 188) – Übertrag aus Liegenschaftenverzeichnis ☑️
- **Rein:** Liegenschaftenbewertung Gemeindesteueramt (Weisung ZStB 21.1) → Eigenmietwert · Mieterspiegel / Verwaltungsabrechnung → Miet- und Pachtzinse (ohne Entschädigungen Heizung/Warmwasser/Treppenhausreinigung) · Rechnungen Unterhalt, Versicherungsprämien, Drittverwaltung → effektive Kosten (Aufstellung) · Baurechtsvertrag/-zinsbelege → Baurechtszinsen (Aufstellung)
- **Rechnen:** Je Liegenschaft: Erträge 5701 + 5711 = 5721 − Unterhalt pauschal 5731 bzw. effektiv 5741 = 5751; Σ 5751… + 578 = 3953 → Code 188
- **Limite (Kanton / Bund):** Gebäude bis 10 Jahre (%): 20 % / 10 % · Gebäude über 10 Jahre (%): 20 % / 20 %
- **Beachten:** Pauschale Kanton 20 % / Bund 10 % (Gebäude ≤ 10 J. bei Periodenbeginn) bzw. 20 %; nicht bei vorwiegend Geschäftsnutzung.
- **Beachten:** EMW: EFH 3,50 % / StWE 4,25 % des Land- und Zeitbauwerts; eigene Wohnung im eigenen MFH 70 % der Marktmiete.
- **Beachten:** Mit Pauschale keine weiteren Abzüge ausser Baurechtszinsen; Wohnrecht/Nutzniessung: EMW 100 % beim Berechtigten.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#6-einkommen-liegenschaften-mietertrag) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md)

### 7 · Total der Einkünfte (Code 199) ☑️
- **Rein:** Übertrag aus Ziff. 1–6 (Seite 2)
- **Rechnen:** Σ Hauptkolonnen Ziff. 1–6: 100–103, 120–123, 130/131, 134–137, 140–143, 150, 160–164, 188 (ohne 151 «davon», Vorkolonnen 960–967, 1641) = 199 → Ziff. 19
- **Beachten:** Ziff. 1–7 einspaltig; Ziff. 19 je Kolonne Staat/Bund – Staat-Korrekturen z. B. via Ziff. 16.5 (Kolonne Staatssteuer).
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#7-berechnung-total) · [Formular 300 ZH 2025 S. 2](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md)

## Abzüge

### 11.1 / 11.2 · Berufsauslagen bei unselbständiger Erwerbstätigkeit, Person 1 (Code 220) / Person 2 (Code 240) ☑️
- **Rein:** Form. 360 «Berufsauslagen» je Person → Ziff. 6 Total: P1 Code 220 → Ziff. 11.1, P2 Code 240 → Ziff. 11.2 · Lohnausweis → Ziff. 11 Nettolohn (Basis Pauschale), Felder F/G, Spesen · ÖV-Abo, km-Nachweis/Begründung Auto, Arbeitstage, Mietvertrag Zimmer (Wochenaufenthalt)
- **Rechnen:** Fahrkosten 201 Abo + 202 Velo + 204 Auto/Motorrad = Zwischentotal 205 (max. Kanton 5’200 / Bund 3’300) + Verpflegung 206/208/210 + übrige 212|213 + Wochenaufenthalt 2860 + Nebenerwerb 216|217 = 220 → Ziff. 11.1; P2: 221 + 222 + 224 = 225 … = 240 → Ziff. 11.2; bei Auto/Motorrad (weisses Kontrollschild) Begründung Ziff. 7 ankreuzen (P1 2041–2044 / P2 2241–2244)
- **Limite (Kanton / Bund):** Maximalabzug pro Person (CHF): CHF 5'200 / CHF 3'300 · Pauschale in % des Nettolohns: 3 % / 3 % · Pauschale Minimum (CHF): CHF 2'000 / CHF 2'000 · Pauschale Maximum (CHF): CHF 4'000 / CHF 4'000 · Ansatz pro km (CHF): CHF 0.70 / CHF 0.70
- **Beachten:** Vom Arbeitgeber vergütete Auslagen nicht abziehbar; mit Geschäftsfahrzeug keine Fahrkosten.
- **Beachten:** Auto 70 Rp./km nur ausnahmsweise (kein ÖV, > 1 Std. Zeitersparnis, AG-Verlangen, Krankheit): Begründung Ziff. 7.
- **Beachten:** Übrige Kosten pauschal 3 % Nettolohn (min. 2’000, max. 4’000) bzw. effektiv mit vollem Nachweis.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#11-1-11-2-berechnung-total) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md)

### 12 · Schuldzinsen (Code 250) ☑️
- **Rein:** Zinsausweis Bank / Hypothekarbestätigung → Schuldzinsen 2025 und Schuld per 31.12. · Privatdarlehen: Vertrag + Zinsbelege (Name/Adresse Gläubiger) · Form. 355 → Total private Schuldzinsen (3201) → Ziff. 12; Total Privatschulden (3200) → Ziff. 34
- **Rechnen:** min(Σ private Schuldzinsen 2025; Bruttoertrag bewegl. + unbewegl. Privatvermögen inkl. EMW + 50’000) → Code 250 (Spalten Staat/Bund; Regel gleich)
- **Beachten:** Nicht abziehbar: Amortisationen, Leasingraten (inkl. Zinsanteile); Geschäftsschuldzinsen bereits in Ziff. 2.
- **Beachten:** Baurechtszinsen → Liegenschaftenverzeichnis (Unterhaltskosten), fallen nicht unter die Begrenzung.
- **Beachten:** Bund: kein Abzug für Zinsen auf Darlehen der eigenen Kapitalgesellschaft zu nicht drittüblichen Bedingungen.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#12-abzug-schuldzinsen) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md)

### 13.1 · Unterhaltsbeiträge an geschiedenen / getrennt lebenden Ehegatten (Code 254) ☑️
- **Rein:** Scheidungs-/Trennungsurteil bzw. Vereinbarung → Unterhalt für den Ehegatten persönlich · Bank-/Zahlungsbelege → Σ 2025 effektiv bezahlte Beiträge (Einreichung auf Verlangen; im Zweifel beilegen, vgl. Formularhinweis unter Ziff. 13.3)
- **Rechnen:** Σ 2025 bezahlte periodische Unterhaltsbeiträge an geschiedenen/getrennten Ehegatten → voll (Code 254; Kanton = Bund)
- **Beachten:** Empfänger versteuert sie in Ziff. 5.1 (Korrespondenzprinzip)
- **Beachten:** Nur periodische Beiträge: Kapitalabfindung gilt als Schuldentilgung, nicht abziehbar; Naturalleistungen (Miete, KK-Prämien, Schuldzinsen) gleichgestellt. Fundstelle nur Bundespraxis (KS 30 Ziff. 14.1.2, WL 2a); WL ZH 2025 äussert sich nicht, eine ZH-Abweichung ist nicht belegt.
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#13-1-abzug-unterhaltsbeitraege) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md)

### 13.2 · Unterhaltsbeiträge für minderjährige Kinder (Code 255) ☑️
- **Rein:** Urteil/Unterhaltsvertrag → Kinderalimente je Kind · Zahlungsbelege mit Monatszuordnung → bezahlt bis und mit Monat des 18. Geburtstags (Einreichung auf Verlangen; im Zweifel beilegen, vgl. Formularhinweis unter Ziff. 13.3)
- **Rechnen:** Σ bezahlte Kinderalimente je Kind bis und mit dem Monat, in dem das Kind 18 wird (Code 255; Kanton = Bund)
- **Beachten:** Ab Folgemonat kein Abzug; stattdessen Kinderabzug Ziff. 24.1 (Erstausbildung, Unterhalt zur Hauptsache)
- **Beachten:** Wer Alimente für das minderjährige Kind leistet, erhält keinen Kinderabzug für dieses Kind
- **Beachten:** Bund: nur familienrechtlich geschuldete, effektiv bezahlte Alimente; freiwillige nicht
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#13-2-abzug-unterhaltsbeitraege) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md)

### 13.3 · Rentenleistungen / dauernde Lasten, abzugsfähig: Ertragsanteil (Code 256) ⚠️
- **Rein:** Leibrenten-/Verpfründungsvertrag → vereinbarte Leistung · Überweisungsbelege → Σ 2025 bezahlte Rente (Vorkolonne Code 2561) · ESTV-Berechnungssatz der Steuerperiode (www.estv.admin.ch)
- **Rechnen:** Code 256 = bezahlte Leibrente/Verpfründung (Vorkolonne 2561) × ESTV-Berechnungssatz (in %); gem. WL Kanton = Bund
- **Beachten:** STRITTIG Kanton: StG § 31 Abs. 1 lit. b = 40 Prozent der bezahlten Leibrenten; WL = ESTV-Satz → Fachperson
- **Beachten:** WL «Neu 2025»: bisher pauschal 40 % Ertragsanteil, ab 1.1.2025 flexibel an Anlagebedingungen angepasst
- **Beachten:** Beweiskräftige Belege einreichen (Leibrenten-/Verpfründungsvertrag, Überweisungsbelege)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#13-3-abzug-uebrige) · [WL ZH 2025 S. 15](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0078.md)

### 14.1 / 14.2 · Beiträge Säule 3a, Person 1 (Code 260, eff. 262) / Person 2 (Code 261, eff. 263) ☑️
- **Rein:** 3a-Bescheinigung Bankstiftung/Versicherung → 2025 einbezahlter Betrag (eff. Code 262/263) · Seite 1 «Ordentliche Beiträge an die Pensionskasse?» / Lohnausweis Ziff. 10.1 → Limite wählen · Ohne 2. Säule: Erwerbseinkommen (Ziff. 1 und 2)
- **Rechnen:** je Person: mit 2. Säule min(einbezahlt; 7’258); ohne 2. Säule min(einbezahlt; 20 % × Erwerbseinkommen; 36’288) → Code 260/261 (Kanton = Bund)
- **Limite (Kanton / Bund):** Maximum mit 2. Säule (CHF): CHF 7'258 / CHF 7'258 · Maximum ohne 2. Säule (CHF): CHF 36'288 / CHF 36'288 · ohne 2. Säule in % des Erwerbseinkommens: 20 % / 20 %
- **Beachten:** Nur 2025 tatsächlich bezahlte Beiträge; Bescheinigung beilegen
- **Beachten:** Ehegatten je eigener Vertrag und Abzug; Mitarbeit im Betrieb des Partners nur bei echtem Arbeitsverhältnis
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#14-1-14-2-abzug-vorsorge-saeule3a) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md)

### 14.3 (ab 2026) · Einkauf (Nachzahlung) Säule 3a – im Formular 2025 nicht vorhanden –
- **Rein:** – (Formular ZH 2025: Ziff. 14 nur Person 1/2, keine Einkaufszeile)
- **Rechnen:** Steuerjahr 2025: kein Eintrag (Formular ohne Einkaufszeile)
- **Beachten:** Einkauf nur für Lücken der zehn Vorjahre; Lücken vor der BVV-3-Änderung vom 6. November 2024 nicht einkaufbar
- **Beachten:** Jahreslücke = max. möglicher 3a-Beitrag des Jahres − effektiv einbezahlt; je Jahreslücke nur ein Einkauf
- **Beachten:** Im Einkaufsjahr voller ordentlicher Beitrag nötig; Einkauf max. 8 Prozent des oberen BVG-Grenzbetrags
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#14-3-ab-2026-abzug-vorsorge-saeule3a-einkauf) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md)

### 15 · Versicherungsprämien und Zinsen von Sparkapitalien (Code 270) ☑️
- **Rein:** KK-Prämienbescheinigung → bezahlte Prämien, i. d. R. nach Prämienverbilligung (Form. 365 Code 601) · Unfall-/Lebens-/Rentenversicherung → bezahlte Prämien (Codes 602/603) · Wertschriften- und Guthabenverzeichnis → Zinsen von Sparkapitalien (Code 604) · Verfügung Prämienverbilligung → Code 605, soweit nicht schon in 601 verrechnet
- **Rechnen:** min(A; B) je Spalte → Code 270; A (606) = Σ 601–604 − 605; B (616) = Max. Verh./übrige (mit/ohne 2./3a) + je Kind/Unterstützte Kanton 1’300 / Bund 700
- **Limite (Kanton / Bund):** Versicherungsabzug gemeinsam Besteuerte (CHF): CHF 5'800 / CHF 3'700 · Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): CHF 8'700 / CHF 5'550 · Versicherungsabzug übrige Steuerpflichtige (CHF): CHF 2'900 / CHF 1'800 · Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): CHF 4'350 / CHF 2'700 · Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): CHF 1'300 / CHF 700
- **Beachten:** Max. Kanton 5’800 Verh. / 2’900 übrige (ohne 2./3a: 8’700 / 4’350); Bund 3’700 / 1’800 (5’550 / 2’700)
- **Beachten:** «Ohne 2./3a» nur, wenn weder Steuerpflichtige noch Arbeitgeber Beiträge an 2. Säule/3a leisteten
- **Beachten:** Halber Kinderabzug: Zuschlag Kanton 650 / Bund 350 je Kind
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#15-abzug-versicherungspraemien) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md)

### 16.1 · Beiträge an 2. Säule inkl. Einkäufe, soweit nicht im Lohnausweis abgezogen (Code 280) ☑️
- **Rein:** Bescheinigung Vorsorgeeinrichtung (Formular 21 EDP) → selbst überwiesene Beiträge/Einkäufe · Lohnausweis Ziff. 10.1/10.2 → bereits vom Lohn abgezogen (nicht nochmals)
- **Rechnen:** Σ selbst bezahlte PK-Beiträge/Einkäufe gem. Bescheinigung, soweit nicht in Lohnausweis Ziff. 10.1/10.2 (Code 280; Kanton = Bund)
- **Beachten:** Einkäufe nicht abziehbar, soweit innerhalb von drei Jahren ein Kapitalbezug erfolgt
- **Beachten:** Vom Lohn abgezogene Beiträge nur im Lohnausweis, selbst überwiesene nur im Formular 21
- **Beachten:** Bescheinigung der Vorsorgeeinrichtung beilegen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#16-1-abzug-vorsorge-saeule2-einkauf) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md)

### 16.1 · Beiträge an AHV/IV (z. B. Nichterwerbstätige, Selbständige ohne Abzug im Hilfsblatt) (Code 280) ☑️
- **Rein:** Beitragsverfügung/-rechnung Ausgleichskasse (Nichterwerbstätige) → AHV/IV/EO-Beiträge · Selbständige: Hilfsblatt A Ziff. 4.1 (Code 1741) → persönliche AHV/IV/EO-Beiträge
- **Rechnen:** Σ AHV/IV/EO-Beiträge gem. Bescheinigung, soweit Einkünfte Ziff. 1 und 2 nicht bereits darum gekürzt (Code 280; Kanton = Bund)
- **Beachten:** Bescheinigung beilegen
- **Beachten:** Bund-WL: Arbeitgeberbeiträge für privates Dienstpersonal nicht abziehbar
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#16-1-abzug-ahv-nichterwerbstaetige) · [WL ZH 2025 S. 16](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0092.md)

### 16.2 · Berufsorientierte Aus- und Weiterbildungskosten (Code 292) ☑️
- **Rein:** Kursrechnungen + Zahlungsbelege → Total der Kosten (Form. 367 Code 2900/2903) · Bestätigung Arbeitgeber/Dritte bzw. Lohnausweis Ziff. 13.3 → Beiträge Dritter (Code 2901/2904)
- **Rechnen:** je Person (Spalten Person 1 / Person 2): 2902/2905 = 2900/2903 − 2901/2904; zulässiger Abzug 2920 (Person 1) / 2921 (Person 2) = min(selbstgetragen; Block Staatssteuer 12’400 bzw. Block Bundessteuer 13’000); je Block 292 = 2920 + 2921
- **Limite (Kanton / Bund):** Maximum (CHF): CHF 12'400 / CHF 13'000
- **Beachten:** Nur mit Abschluss Sek. II oder ab vollendetem 20. Lebensjahr; nicht Ausbildung bis zum ersten Sek.-II-Abschluss
- **Beachten:** Zeitpunkt: Fälligkeit bzw. Zahlung, nicht der Kursbesuch
- **Beachten:** Formular 367 vollständig ausgefüllt beilegen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#16-2-abzug-weiterbildung) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md)

### 16.3 · Kosten für die Verwaltung des beweglichen Privatvermögens (Code 283) ☑️
- **Rein:** Depot-/Verwaltungsgebührenabrechnung Bank → effektive Verwaltungs- und Verwahrungskosten · Wertschriftenverzeichnis → Steuerwert der durch Dritte verwalteten Wertschriften
- **Rechnen:** Pauschal min(3 ‰ × Steuerwert drittverwalteter Wertschriften; 6’000) oder höhere effektive Kosten mit vollem Nachweis (Code 283)
- **Beachten:** Nicht abziehbar: Kosten für Erwerb und Veräusserung von Wertschriften
- **Beachten:** Abziehbar auch: weder rückforderbare noch anrechenbare ausländische Quellensteuern
- **Beachten:** Details: Weisung Zürcher Steuerbuch Nr. 30.1
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#16-3-abzug-verwaltungskosten-wertschriften) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md)

### 16.4 · Behinderungsbedingte Kosten (Code 3160) ☑️
- **Rein:** Rechnungen Pflege, Betreuung, Hilfsmittel, Transporte, Heim → Form. 370 S. 2 Teil A (Code 3120) · KK-/Versicherungsabrechnung, Hilflosenentschädigung, Anteil Lebenshaltung → Teil B (Code 3150) · Verfügung Hilflosenentschädigung (Grad) bzw. Nachweis Gehörlosigkeit/Dialyse → Pauschale (Code 3103)
- **Rechnen:** Effektiv: A (3120) − B (3150) = 3155; oder Pauschale (3103): HE leicht 2’500 / mittel 5’000 / schwer 7’500; Gehörlose, Dialyse 2’500 → Code 3160 (Kanton = Bund)
- **Beachten:** B enthält Anteil Lebenshaltungskosten (Kosten, die auch ohne Behinderung angefallen wären)
- **Beachten:** Hilfe im Haushalt/Kinderbetreuung nur, soweit über dem Abzug Ziff. 16.6
- **Beachten:** Kein Selbstbehalt (anders als Krankheitskosten Ziff. 22.1, Rückseite Form. 370); eine Aufstellung je Steuererklärung
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#16-4-abzug-behinderungskosten) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md)

### 16.5 · Beiträge und Zuwendungen an politische Parteien (Code 284, Aufstellung) ☑️
- **Rein:** Spendenbestätigungen / Beitragsrechnungen der Partei → Σ Mitgliederbeiträge und Zuwendungen 2025
- **Rechnen:** Kanton: min(Σ; 20’600 ungetrennte Ehe / 10’300 übrige); Bund: min(Σ; 10’600) für alle → Ziff. 16.5 (Code 284)
- **Limite (Kanton / Bund):** Maximum (CHF), ggf. alleinstehend: CHF 10'300 / CHF 10'600 · Maximum gemeinsam Besteuerte (CHF): CHF 20'600 / n/a
- **Beachten:** Nur Parteien im Parteienregister, in einem kantonalen Parlament oder mit mind. 3 % Stimmen bei letzten Parlamentswahlen
- **Beachten:** Aufstellung (Code 284) und Belege beilegen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#16-5-abzug-parteispenden) · [WL ZH 2025 S. 17](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0100.md)

### 16.5 · Weitere Abzüge: Teilbesteuerung qualifizierte Beteiligungen (Abzug 50 % Staat / 30 % Bund) ☑️
- **Rein:** Dividendenbeleg / Steuerauszug → Bruttoausschüttung, im Wertschriftenverzeichnis mit Code «Q» · Formular «Qualifizierte Beteiligungen im Privat-/Geschäftsvermögen» → nicht steuerbarer Teil
- **Rechnen:** Privatvermögen: Kanton 50 % / Bund 30 % × Bruttoertrag qual. Beteiligungen; Geschäftsvermögen: gleiche Sätze nach Abzug des zurechenbaren Aufwands → Code 284
- **Beachten:** Qualifiziert = mindestens 10% des Grund- oder Stammkapitals
- **Beachten:** Ertrag ungekürzt (brutto) in Kolonne A bzw. B deklarieren
- **Beachten:** Gratis abgegebene Mitarbeiteraktien: kein Abzug
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#16-5-abzug-teilbesteuerung-beteiligungen) · [WL ZH 2025 S. 17](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md)

### 16.5 · Weitere Abzüge (Freitext, Code 284): Liquidationsgewinne, Grundstückgewinn-Freistellung, Einsatzkosten Geldspiele ☑️
- **Rein:** Hilfsformular «Liquidationsgewinn bei Aufgabe der selbständigen Erwerbstätigkeit» → Liquidationsgewinn aus Ziff. 2.1/2.2 · Gewinnabrechnung Geldspiele / Online-Spielerkonto → Gewinne bzw. abgebuchte Einsätze · Hilfsblatt STAF (Form. 547) → Patentbox/F&E-Zusatzabzug
- **Rechnen:** Geldspiel je Gewinn: min(5 % × Gewinn; Kanton 5’200 / Bund 5’400); Online-Spielbank: Einsätze, max. Kanton 25’800 / Bund 26’800; Liquidationsgewinn: voll
- **Beachten:** Liquidationsgewinn nur bei definitiver Aufgabe nach vollendetem 55. Altersjahr oder wegen Invalidität
- **Beachten:** Nur Staatssteuer: freizustellenden Teil des Grundstückgewinns abziehen
- **Beachten:** Patentbox/F&E: Form. 547 vollständig beilegen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#16-5-abzug-uebrige) · [WL ZH 2025 S. 17](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0105.md)

### 16.6 · Abzug für fremdbetreute Kinder (Jahrg. 2011–2025) (Code 376) ☑️
- **Rein:** Rechnungen Kita/Hort/Tagesfamilie + Zahlungsnachweise → Betreuungskosten je Kind · Seite 1 Kinder → Geburtsdatum (Jahrg. 2011–2025)
- **Rechnen:** je Kind < 14 J.: min(nachgewiesene Kosten; Kanton 25’000 / Bund 25’800) → Code 376; Konkubinat mit gemeinsamer Sorge: je max. Kanton 12’500 / Bund 12’900
- **Limite (Kanton / Bund):** Maximum pro Kind (CHF): CHF 25'000 / CHF 25'800 · Altersgrenze Kind: 14 Jahre / 14 Jahre
- **Beachten:** Nur Kosten im direkten Zusammenhang mit Erwerb, Ausbildung oder Erwerbsunfähigkeit; Kind im gleichen Haushalt
- **Beachten:** Andere als hälftige Aufteilung nachweisen; gilt auch bei alternierender Obhut mit gemeinsamer Sorge
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#16-6-abzug-drittbetreuung) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md)

### 17 · Sonderabzug bei Erwerbstätigkeit beider Ehegatten / Partner (Code 290) ☑️
- **Rein:** Übertrag: Erwerbseinkommen je Ehegatte (Ziff. 1–2) · abzüglich je Person Berufsauslagen (Ziff. 11), Säule 3a (Ziff. 14), Einkäufe 2. Säule / AHV nicht via Lohnausweis (Ziff. 16.1)
- **Rechnen:** Basis = niedrigeres verbleibendes Erwerbseinkommen; Kanton: min(Basis; 6’100); Bund: min(Basis; max(50 % × Basis; 8’600); 14’100) → Code 290
- **Limite (Kanton / Bund):** Minimum (CHF): n/a / CHF 8'600 · Maximum bzw. fixer Betrag (CHF): CHF 6'100 / CHF 14'100 · Satz (% des tieferen Erwerbseinkommens): n/a / 50 %
- **Beachten:** Nur Ehegatten in ungetrennter Ehe, beide erwerbstätig; nur einmal beanspruchbar
- **Beachten:** Erhebliche Mitarbeit im Betrieb des Ehegatten: Kanton vom gemeinsamen Einkommen; Bund i. d. R. hälftig aufteilen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#17-abzug-zweiverdiener) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md)

### 18 · Total der Abzüge (Code 299) ☑️
- **Rein:** Übertrag aus Ziff. 11–17 (je Spalte Staatssteuer / Bundessteuer)
- **Rechnen:** Σ Ziff. 11.1 bis 17 je Spalte (Code 299); Übertrag in Ziffer 20
- **Beachten:** Staats- und Bundessteuer-Spalte getrennt summieren (unterschiedliche Maxima)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#18-berechnung-total) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md)

## Einkommensberechnung

### 19 · Total der Einkünfte (Code 199) ☑️
- **Rein:** Übertrag aus Ziff. 7 (Total der Einkünfte)
- **Rechnen:** = Ziffer 7 je Spalte (Staatssteuer / Bundessteuer), Code 199
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#19-berechnung-total) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md)

### 20 · Total der Abzüge (Code 299) ☑️
- **Rein:** Übertrag aus Ziff. 18 (Total der Abzüge)
- **Rechnen:** = Ziffer 18 je Spalte (Code 299); wird von Ziffer 19 abgezogen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#20-berechnung-total) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md)

### 21 · Nettoeinkommen (Code 310) ☑️
- **Rein:** Rechenzeile: Ziff. 19 − Ziff. 20
- **Rechnen:** = Ziffer 19 − Ziffer 20 je Spalte (Code 310)
- **Limite (Kanton / Bund):** Selbstbehalt in % des Nettoeinkommens: 5 % / 5 % · Maximum in % des (Rein-)Einkommens: 20 % / 20 %
- **Beachten:** Basis für Selbstbehalt Krankheitskosten 5 % (Ziff. 22.1) und Spendenlimite 20 % (Ziff. 22.2), je Spalte
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#21-berechnung-total) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md)

### 22.1 · Krankheits- und Unfallkosten (Code 320) – über Selbstbehalt 5 % des Nettoeinkommens ☑️
- **Rein:** KK-Leistungsabrechnung / Kostenzusammenstellung → Selbstbehalt gemäss Abrechnung (Form. 370 Code 300) · Rechnungen Arzt/Medikamente, Zahnarzt, Pflegepersonal, Spital, verordnete Therapien → Codes 301–305 · Vergütungen KK/Versicherungen → Code 308; Anteil Lebenshaltungskosten (z. B. Ernährung) → Code 311
- **Rechnen:** C (314) = A (317) − B (318); 313 = C und/oder D (Diät-Pauschale 2500, Code 315); Abzug 320 = 313 − 5 % × Ziff. 21 (319), je Spalte
- **Limite (Kanton / Bund):** Selbstbehalt in % des Nettoeinkommens: 5 % / 5 %
- **Beachten:** Nicht abziehbar: Prävention (Fitness), Fahrkosten zu Arzt/Spital, eigene Pflege, Wellness, Schönheit, Psychoanalysen
- **Beachten:** Auch für unterhaltene Personen; eine Aufstellung je Steuererklärung, Belege geordnet beilegen
- **Beachten:** Diät-Pauschale nur bei andauernder, lebensnotwendiger Diät (z. B. Zöliakie)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#22-1-abzug-krankheitskosten) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md)

### 22.2 · Gemeinnützige Zuwendungen (Code 324) ☑️
- **Rein:** Spendenbescheinigungen / Liste aller einzelnen Zuwendungen → Σ Geld und übrige Vermögenswerte (Sachspenden)
- **Rechnen:** Σ ≥ 100 → min(Σ; 20 % × Ziff. 21) je Spalte (Code 324); Σ unter 100 → kein Abzug (Kanton = Bund)
- **Limite (Kanton / Bund):** Mindestbetrag (CHF): CHF 100 / CHF 100 · Maximum in % des (Rein-)Einkommens: 20 % / 20 %
- **Beachten:** Empfänger ZH: im Verzeichnis der steuerbefreiten Institutionen; andere Kantone: dort abklären
- **Beachten:** Nicht abziehbar: Schulgeld, Arbeitsleistungen, Zuwendungen ins Ausland oder für religiöse Zwecke
- **Beachten:** Liste beilegen; Spendenbescheinigung auf Nachfrage vorweisen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#22-2-abzug-spenden) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md)

### 23 · Reineinkommen (Code 350) ☑️
- **Rein:** Rechenzeile: Ziff. 21 − Ziff. 22.1 − Ziff. 22.2
- **Rechnen:** = Ziff. 21 − 22.1 − 22.2 je Spalte (Code 350)
- **Beachten:** Danach Sozialabzüge Ziff. 24.1 bis 24.3 → steuerbares Einkommen Ziff. 25 (Code 390)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#23-berechnung-total) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md)

### 24.1 · Abzug für Kinder in Ihrem Haushalt (Code 370) ☑️
- **Rein:** Seite 1 «Kinder in Ihrem Haushalt» → Geburtsdatum, Schule/Lehrfirma, Unterhaltsbeiträge des anderen Elternteils · Lehr-/Schulbestätigung → berufliche Erstausbildung volljähriger Kinder · Urteil/Vereinbarung → elterliche Sorge, Unterhaltsbeiträge
- **Rechnen:** Anzahl Kinder × Kanton 9’300 / Bund 6’800 (Code 370/372); halb 4’650 / 3’400 bei gemeinsamer Sorge ohne Unterhaltsbeiträge (erhalten bzw. abgezogen)
- **Limite (Kanton / Bund):** Kinderabzug Grundbetrag (CHF): CHF 9'300 / CHF 6'800
- **Beachten:** Stichtag 31. Dezember 2025: minderjährig (Jahrgänge 2008–2025) oder in Erstausbildung, Unterhalt zur Hauptsache
- **Beachten:** Wer Unterhaltszahlungen für das minderjährige Kind leistet, erhält keinen Kinderabzug
- **Beachten:** Kinder ausserhalb des Haushalts: separate Zeile Code 372
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#24-1-sozialabzug-kinder) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md)

### 24.1 · Abzug für Kinder ausserhalb Ihres Haushaltes (Code 372) ☑️
- **Rein:** Formular S. 1 «Kinder ausserhalb Ihres Haushaltes» → Name, Geburtsdatum, Adresse, Schule/Lehrfirma, voraussichtlich bis · Nachweis geleisteter Unterhaltsbeiträge → volljähriges Kind: Hauptunterhalt belegen · Lehrvertrag bzw. Schulbestätigung → volljähriges Kind in beruflicher Erstausbildung
- **Rechnen:** Je Kind: gem. Sorge ohne Alimentenabzug → ½: Kanton 4'650 / Bund 3'400; Alimente od. keine Sorge → kein Abzug; volljährig + Hauptunterhalt → Kanton 9'300 / Bund 6'800
- **Limite (Kanton / Bund):** Kinderabzug Grundbetrag (CHF): CHF 9'300 / CHF 6'800
- **Beachten:** Stichtag 31. Dezember 2025: minderjährig = Jg. 2008–2025 (§ 34 Abs. 2 StG / Art. 35 Abs. 2 DBG)
- **Beachten:** Volljährige (Kanton, ZStB 34.1): Lehrvertrag od. Schule ≥ halbtags, ≥ ein halbes Jahr; auf Unterstützung angewiesen
- **Beachten:** Kinderabzug und Abzug Kinderalimente (Ziff. 13.2) schliessen sich aus
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#24-1-sozialabzug-kinder-2) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md)

### 24.2 · Abzug für unterstützte Personen (Code 374) ☑️
- **Rein:** Bestätigung der unterstützten Person → Art, Zeitpunkt, Höhe der Unterstützung (beilegen) · Zahlungsbelege (Ausland: Post-/Bankbelege) → auf Verlangen · Formular S. 1 → Name, Geburtsjahr, Adresse, Unterstützungsbetrag pro Jahr
- **Rechnen:** Je Person: Unterstützung ≥ 2'800 → Kanton 2'800; ≥ 6'800 → Bund 6'800 (fixer Abzug, nicht die effektive Leistung)
- **Limite (Kanton / Bund):** Unterstützungsabzug (CHF): CHF 2'800 / CHF 6'800
- **Beachten:** Nur für erwerbsunfähige/beschränkt erwerbsfähige, unterstützungsbedürftige Personen; Leistungen hinreichend nachweisen
- **Beachten:** Ausgeschlossen: Ehegatte, Kinder mit Kinderabzug, Personen, für die Alimente abgezogen werden
- **Beachten:** Bedürftigkeit (Kanton, ZStB 34.1, Wohnsitz CH): Eink. < 15'000 + Verm. < 50'000; verh. < 22'000 + < 100'000
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#24-2-sozialabzug-unterstuetzung) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md)

### 24.3 · Abzug für Ehegatten / Partner – nur Bundessteuer (Code 365) ☑️
- **Rein:** Formular S. 1 → Zivilstand am 31. Dezember 2025
- **Rechnen:** Kanton: kein Abzug («—») / Bund: 2'800 pauschal bei rechtlich und tatsächlich ungetrennter Ehe → Code 365
- **Limite (Kanton / Bund):** Verheiratetenabzug (CHF, Bund): n/a / CHF 2'800
- **Beachten:** Nur Spalte Bundessteuer ausfüllen
- **Beachten:** Eingetragene Partnerschaft wird gleich behandelt wie die Ehe
- **Beachten:** Verhältnisse am Ende der Steuerperiode massgebend (Art. 35 Abs. 2 DBG)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#24-3-sozialabzug-verheiratete) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md)

### 25 · Steuerbares Einkommen gesamt (Code 390) ☑️
- **Rein:** Übertrag Ziff. 23 Reineinkommen (Code 350), je Spalte Staat / Bund · Übertrag Ziff. 24.1–24.3 Sozialabzüge (Codes 370, 372, 374, 365)
- **Rechnen:** Ziff. 23 − (24.1 + 24.2 + 24.3), getrennt Spalte Staatssteuer / Bundessteuer → Code 390
- **Beachten:** Ziff. 24.3 nur in Spalte Bundessteuer abziehen
- **Beachten:** Teilweise Steuerpflicht: Sozialabzüge anteilmässig (§ 34 Abs. 3 StG / Art. 35 Abs. 3 DBG)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#25-berechnung-total) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md)

### 26.1 / 26.2 · Davon auf steuerbare Einkünfte in anderen Kantonen (Code 394) bzw. im Ausland (Code 396) ☑️
- **Rein:** Interkantonale/internationale Steuerausscheidung (eigene Berechnung, sonst durch Steueramt) · Liegenschaftenverzeichnis → Liegenschaften ausserhalb ZH bzw. im Ausland; Betriebsstätten
- **Rechnen:** Anteil von Ziff. 25 gemäss Ausscheidung: andere Kantone → Code 394 (nur Staat), Ausland → Code 396 (Staat und Bund); sonst leer
- **Beachten:** 26.1 nur Spalte Staatssteuer, 26.2 Spalten Staat und Bund (Layout Form. 300 S. 3)
- **Beachten:** Gesamtes in- und ausländisches Einkommen deklarieren; ohne eingereichte Ausscheidung nimmt sie das Steueramt vor
- **Beachten:** Teilweise Steuerpflicht: Sozialabzüge anteilmässig, für die Satzbestimmung voll (§ 34 Abs. 3 StG)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#26-1-26-2-berechnung-total) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md)

### 27 · Steuerbares Einkommen im Kanton Zürich bzw. in der Schweiz (Code 398) ☑️
- **Rein:** Übertrag Ziff. 25 (Code 390) und Ziff. 26.1/26.2 (Codes 394/396)
- **Rechnen:** Staat: Ziff. 25 − 26.1 − 26.2 / Bund: Ziff. 25 − 26.2 → Code 398; ohne Ausscheidung = Ziff. 25
- **Beachten:** Kapitalleistungen aus Vorsorge (Ziff. 40) nicht enthalten – gesondert besteuert
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#27-berechnung-total) · [Formular 300 ZH 2025 S. 3](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md)

## Vermögen

### 30.1 · Wertschriften und Guthaben (Code 400) – Total Steuerwert laut Wertschriftenverzeichnis ☑️
- **Rein:** Bank-Steuerauszug / eSteuerauszug → Steuerwerte und Erträge je Titel/Konto (eSteuerauszug importierbar) · Depotauszug → Bestand 31.12.2025; Kurs gem. ESTV-Kursliste 31.12.2025 · Konto-/Zinsausweis → Saldo 31.12.2025 (voller Forderungsbetrag) · Krypto: Wallet-Auszug per Ende Steuerperiode → ESTV-Jahresendsteuerkurs
- **Rechnen:** Übertrag Form. 340 «Total Steuerwert» (Code 400) = Σ Steuerwerte 31.12.2025; Fremdwährung zu ESTV-Devisenkursen 31.12.2025
- **Beachten:** Kinder Jg. 2008 und jünger mitdeklarieren, Jg. 2007 und älter selbst; berufliche Vorsorge und 3. Säule a nicht aufführen
- **Beachten:** Kennzeichnen: G Geschäfts-, N Nutzniessungsvermögen, E Erbschaft 2025, S Schenkung 2025, Q Beteiligung ≥ 10 %
- **Beachten:** Nichtkotierte Titel: Verkehrswert, sonst vorläufig letzter bekannter Steuerwert (KS Nr. 28)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#30-1-vermoegen-wertschriften-guthaben) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md)

### 30.2 · Bargeld, Gold und andere Edelmetalle (Code 404) ☑️
- **Rein:** Eigene Aufstellung Bargeld (CHF und ausländische Banknoten) per 31. Dezember 2025 · Bestandsnachweis Goldmünzen/Edelmetalle per 31. Dezember 2025
- **Rechnen:** Σ Bargeld CHF + (ausländische Banknoten, Goldmünzen, Edelmetalle × Tageskurs per 31. Dezember 2025) → Code 404
- **Beachten:** Bankguthaben (Sparhefte, Salärkonti) gehören in Ziff. 30.1 (Wertschriftenverzeichnis)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#30-2-vermoegen-bargeld-edelmetalle) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md)

### 30.3 · Lebens- und Rentenversicherungen, Steuerwert (Code 406) ☑️
- **Rein:** Steuerwertbescheinigung der Versicherung per 31.12.2025 → Steuerwert (Rückkaufswert) je Police · Police → Versicherungsgesellschaft, Abschlussjahr, Ablaufsjahr (Formularspalten)
- **Rechnen:** Σ bescheinigte Steuerwerte (Rückkaufswerte) aller rückkaufsfähigen Lebens-/Rentenversicherungen → Total Code 406
- **Beachten:** Policen der Säule 3a bis Fälligkeit der Versicherungssumme steuerfrei – nicht einsetzen
- **Beachten:** Rentenversicherung: Rückkaufswert auch nach Rentenbeginn steuerbar; nicht rückkaufsfähige nicht
- **Beachten:** Bescheinigung der Versicherungsgesellschaft beilegen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#30-3-vermoegen-lebensversicherungen) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md)

### 30.4 · Motorfahrzeuge (Code 412) ☑️
- **Rein:** Kaufvertrag/Rechnung → Kaufpreis und Kaufjahr (Formularfelder) · Leasingvertrag → Fahrzeug nicht deklarieren
- **Rechnen:** Verkehrswert: Kaufpreis, pro Jahr − 40 % des Restwertes (Regel); Σ aller privaten Motorfahrzeuge → Code 412
- **Beachten:** Nur private Fahrzeuge; geleaste nicht deklarieren
- **Beachten:** Massgebend ist der aktuelle Verkehrswert (§ 39 Abs. 1 StG); 40 %-Regel ist Richtwert («in der Regel»)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#30-4-vermoegen-fahrzeuge) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md)

### 30.5 · Geschäfts- und Korporationsanteile (Code 414) ☑️
- **Rein:** Aufstellung über Kapital und Ertrag der Geschäfts-/Korporationsanteile (Beilage) · Gesellschafts-/Korporationsunterlagen → eigene Beteiligungsquote
- **Rechnen:** Σ (Wert Geschäft bzw. Korporation × eigene Beteiligungsquote) → Code 414
- **Beachten:** Unverteilte Erbschaft: Liegenschaftsanteil → Liegenschaftenverzeichnis, Wertschriften/Guthaben → WV
- **Beachten:** Erbengemeinschaft: Aufstellung (Erblasser, Erben/Erbquoten, Vermögen, Erträge, Schulden) beilegen
- **Beachten:** Anteile an Kapitalgesellschaften/Genossenschaften ins WV (≥ 10 % mit «Q» kennzeichnen)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#30-5-vermoegen-erbschaften-beteiligungen) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md)

### 30.6 · Übrige Vermögenswerte (Code 416) ☑️
- **Rein:** Eigene Aufstellung mit näherer Bezeichnung (z. B. Gemälde, Sammlungen, Schmuck, Boote, Flugzeuge) · Kaufbelege/Schätzungen → Verkehrswert per 31. Dezember 2025
- **Rechnen:** Σ Verkehrswerte per 31. Dezember 2025 (§ 39 Abs. 1 StG) → Code 416
- **Beachten:** Hausrat und persönliche Gebrauchsgegenstände nicht besteuert (§ 38 Abs. 4 StG)
- **Beachten:** Nutzniessungsvermögen versteuert der Nutzniesser (§ 38 Abs. 2 StG)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#30-6-vermoegen-uebrige) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md)

### 31.1 · Liegenschaften zum Verkehrswert besteuert (Code 421) – Total Liegenschaftenverzeichnis ☑️
- **Rein:** Liegenschaftenbewertung des Gemeindesteueramts → Vermögenssteuerwert EFH/Stockwerkeigentum zu Wohnzwecken · Mietzinseinnahmen 2025 → Bruttojahresertrag (MFH, Geschäftshaus, StWE zu Geschäftszwecken) · Liegenschaftenverzeichnis Form. 350 → Spalte Verkehrswert, Total Code 3951
- **Rechnen:** Σ Steuerwerte Form. 350 (Code 3951) → Code 421: EFH/StWE Wohnen = Bewertung Gemeinde; MFH/Geschäft = Bruttojahresertrag 2025 × 100 / 7,05
- **Beachten:** Bruttoertrag inkl. Marktmietwert eigengenutzter Wohnung, ohne Heizung, Warmwasser, Kehricht-, Wasser-/Abwassergebühren
- **Beachten:** Nutzniessung: 100 % beim Nutzniesser; Wohnrecht: 100 % beim Eigentümer
- **Beachten:** Keine Bewertung erhalten → Gemeindesteueramt fragen; auch ausserkantonale/ausländische Liegenschaften erfassen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#31-1-vermoegen-liegenschaften) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md)

### 31.2 · Liegenschaften zum Ertragswert besteuert – Land- oder Forstwirtschaft (Code 422) ☑️
- **Rein:** Liegenschaftenverzeichnis Form. 350 → Spalte Ertragswert Land-/Forstwirtschaft, Total Code 3952
- **Rechnen:** Σ Ertragswerte land-/forstwirtschaftlicher Liegenschaften inkl. erforderlicher Gebäude (Form. 350 Code 3952) → Code 422
- **Beachten:** Auch landwirtschaftlich genutzte Flächen des erweiterten Umschwungs von Wohn-/Geschäftsliegenschaften
- **Beachten:** Veräusserung/Entfremdung: ergänzende Vermögenssteuer auf Differenz Ertrags-/Verkehrswert (max. 20 Jahre, 1 ‰)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#31-2-vermoegen-liegenschaften) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md)

### 32 · Eigenkapital Selbständigerwerbender ohne Geschäftswertschriften (Code 430) ☑️
- **Rein:** Hilfsblatt A Ziff. 10.4 (kaufmännische Buchführung) → Eigenkapital · Hilfsblatt A Ziff. 14.4 (vereinfachte Buchführung) → Eigenkapital · Jahresrechnung (Bilanz, Erfolgsrechnung, Anhang) bzw. Aufstellung Aktiven/Passiven → Beilage
- **Rechnen:** Übertrag Eigenkapital Hilfsblatt A (Ziff. 10.4 bzw. 14.4) ohne Geschäftswertschriften → Code 430
- **Beachten:** Geschäftswertschriften nicht hier, sondern im WV mit «G» kennzeichnen
- **Beachten:** Immaterielle Güter und bewegliches Geschäftsvermögen zum Einkommenssteuerwert (§ 39 Abs. 2 StG)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#32-vermoegen-uebrige) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md)

### 33 · Total der Vermögenswerte (Code 460) ☑️
- **Rein:** Übertrag Ziff. 30.1–30.6, 31.1, 31.2 und 32
- **Rechnen:** Σ Ziff. 30.1 bis 30.6 + 31.1 + 31.2 + 32 → Code 460
- **Beachten:** Gesamtes in- und ausländisches Vermögen einbeziehen; Ausscheidung erst in Ziff. 36
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#33-berechnung-total) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md)

### 34 · Schulden (Code 470) ☑️
- **Rein:** Saldo-/Zinsbestätigung Bank per 31.12.2025 → Hypotheken, Kredite (Form. 355) · Darlehensvertrag + Saldo 31.12.2025 → private Darlehen (Gläubiger mit Adresse, Zinssatz) · Schuldenverzeichnis Form. 355 → Total Privatschulden Code 3200
- **Rechnen:** Σ Privatschulden inkl. Grundpfandschulden am 31. Dezember (Form. 355 Code 3200) → Code 470; Zinsen Code 3201 → Ziff. 12
- **Beachten:** Solidar-/Bürgschaftsschulden nur soweit selbst zu tragen (§ 46 StG)
- **Beachten:** Gläubiger mit genauer Adresse und Zinssatz zwingend; vollständiges Verzeichnis beilegen
- **Beachten:** Unverteilte Erbschaft: Schulden und Schuldzinsen anteilmässig
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#34-schulden-privat) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md)

### 35 · Steuerbares Vermögen gesamt (Code 490) ☑️
- **Rein:** Übertrag Ziff. 33 (Code 460) und Ziff. 34 (Code 470)
- **Rechnen:** Ziff. 33 − Ziff. 34 → Code 490 (Reinvermögen)
- **Beachten:** Unterjährige Steuerpflicht: Vermögenssteuer nach Dauer der Steuerpflicht
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#35-berechnung-total) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md)

### 36.1 / 36.2 · Davon auf steuerbare Vermögenswerte in anderen Kantonen (Code 494) bzw. im Ausland (Code 496) ☑️
- **Rein:** Steuerausscheidung (eigene Berechnung, sonst durch Steueramt) · Liegenschaftenverzeichnis → Liegenschaften ausserhalb ZH bzw. im Ausland
- **Rechnen:** Anteil von Ziff. 35 gemäss Ausscheidung: andere Kantone → Code 494, Ausland → Code 496; sonst leer
- **Beachten:** Gesamtes in- und ausländisches Vermögen trotzdem vollständig deklarieren
- **Beachten:** Ohne eingereichte Ausscheidung nimmt das Steueramt sie vor
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#36-1-36-2-berechnung-total) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md)

### 37 · Steuerbares Vermögen im Kanton Zürich (Code 498) ☑️
- **Rein:** Übertrag Ziff. 35 (Code 490) und Ziff. 36.1/36.2 (Codes 494/496)
- **Rechnen:** Ziff. 35 − 36.1 − 36.2 → Code 498; Tarif: 0 ‰ auf ersten 80'000 (Grundtarif) / 159'000 (Verheiratetentarif), kein Abzug eintragen
- **Beachten:** Bund: keine Vermögenssteuer
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#37-berechnung-total) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md)

### — (Tarif) · Steuerfreies Vermögen: kein Formularfeld, ergibt sich aus der 0‰-Stufe des Vermögenssteuertarifs ☑️
- **Rein:** Kein Beleg; ergibt sich aus Ziff. 37 und Zivilstand/Kinder (Seite 1)
- **Rechnen:** Nichts eintragen; 0 ‰ auf den ersten 80'000 (Grundtarif) bzw. 159'000 (Verheiratetentarif) von Ziff. 37
- **Limite (Kanton / Bund):** Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): CHF 80'000 / n/a · Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): CHF 159'000 / n/a
- **Beachten:** Verheiratetentarif auch für Verwitwete, Getrennte, Geschiedene, Ledige, die mit Kindern zusammenleben
- **Beachten:** Nicht gemeinsam besteuerte Eltern, je ½ Kinderabzug: Verheiratetentarif nur, wer Kindesunterhalt hauptsächlich trägt
- **Beachten:** Verhältnisse am Ende der Steuerperiode massgebend (§ 47 Abs. 3 StG); Bund: keine Vermögenssteuer
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#tarif-vermoegen-sozialabzug) · [StG ZH § 47](../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-47-t1.md)

## Weitere Angaben

### 40 · Kapitalleistungen aus Vorsorge (Code 510) ☑️
- **Rein:** Auszahlungsbescheinigung (AHV/IV, 2. Säule, Freizügigkeitskonto/-police, Säule 3a) → Datum, Betrag, Art · Bei mehreren Leistungen: Aufstellung beilegen, Gesamtbetrag eintragen · Bescheinigung Arbeitgeber-Kapitalleistung mit Vorsorgecharakter bzw. Kapital bei Tod/bleibenden Nachteilen → Betrag
- **Rechnen:** Σ Kapitalleistungen 2025 (100 %) → Code 510; Steuer gesondert: Kanton Satz von 1/20 als Jahresleistung, einfache Staatssteuer mind. 2 % / Bund 1/5 Tarif
- **Limite (Kanton / Bund):** Steuersatz/Tarif (separate Jahressteuer): Satz für 1/20 der Leistung, einf. Staatssteuer mind. 2 % / 1/5 der Tarife Art. 36 DBG, keine Sozialabzüge
- **Beachten:** Steuerfrei: Stellenwechsel-Leistung, die innert Jahresfrist in eine andere 2.-Säule-Einrichtung eingebracht wird
- **Beachten:** Gesondert vom übrigen Einkommen besteuert; keine Sozialabzüge, stets volle Jahressteuer
- **Beachten:** Auszahlungsdatum angeben (Formularfeld)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#40-einkommen-kapitalleistung-vorsorge) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0013.md)

### 50.1 / 50.2 · Schenkungen, Erbvorbezug, Erbschaften, Beteiligung an Erbengemeinschaften: erhalten (Code 516) / ausgerichtet (Code 519) ☑️
- **Rein:** Schenkungs-/Erbvorbezugsvertrag → Datum, Wert, Name, Adresse, Verwandtschaftsgrad · Erbbescheinigung/Teilungsvertrag → Erbanfall 2025 (Datum, Wert) · Unverteilte Erbschaft: Aufstellung (Erblasser, Erben/Erbquoten, Vermögen, Erträge, Schulden)
- **Rechnen:** Je Vorgang Datum + Wert: erhalten → Code 516, ausgerichtet → Code 519; Vermögen per Ende 2025 und Erträge der Steuerperiode normal deklarieren
- **Beachten:** Schenkungssteuererklärung innert dreier Monate – entfällt bei Ehegatte/Partner, Nachkommen, Gelegenheitsgeschenk ≤ 5'000
- **Beachten:** Datum steuert Vermögenssteuer: Erbgang → Erblasser bis Erbgang, Erbe danach; Schenkung → ganzes Jahr Beschenkter
- **Beachten:** Auch bei noch nicht erfolgter Erbteilung angeben
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#50-1-50-2-info-schenkungen-erbschaften) · [Formular 300 ZH 2025 S. 4](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0014.md)

### Seite 1 · Personalien, Kinder (Jg. 2008–2025 / in Erstausbildung), unterstützte Personen, Pensionskassenbeiträge ja/nein ☑️
- **Rein:** Vorjahresveranlagung / Zivilstandsdokumente → Personalien, Zivilstand, Konfession per 31.12.2025 · Lehrvertrag / Schulbestätigung → Kinder: Schule/Lehrfirma, voraussichtlich bis · Bestätigung der unterstützten Person → Unterstützungsbetrag pro Jahr · Je Person: ordentliche Beiträge an Pensionskasse (2. Säule) ja/nein
- **Rechnen:** Keine Rechnung; Grundlage für 24.1–24.3 (Unterstützung ≥ Kanton 2'800 / Bund 6'800); PK ja/nein → 3a-Maximum (Ziff. 14) und Versicherungsabzug (Ziff. 15)
- **Limite (Kanton / Bund):** Unterstützungsabzug (CHF): CHF 2'800 / CHF 6'800
- **Beachten:** Eingetragene Partnerschaft wird gleich behandelt wie die Ehe
- **Beachten:** Ledig/geschieden/getrennt: angeben, ob der andere Elternteil Unterhaltsbeiträge leistet
- **Beachten:** Kinder Jg. 2007 und älter versteuern Vermögen und Ertrag selbst
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#seite-1-personalien) · [Formular 300 ZH 2025 S. 1](../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0002.md)

### Seite 1 / 4 · Einreichung, Frist, Unterschrift, Beilagen ☑️
- **Rein:** Aufforderung/Steuererklärung 2025 + Wertschriftenverzeichnis → Einreichung bis 31. März 2026 (online oder Scan-Center) · Lohnausweise, ALK-Taggeld-, Renten-, PK-/3a-Bescheinigungen → bereitlegen bzw. beilegen (Checkliste WL) · Zins-/Dividendengutschriften, Depot-Steuerverzeichnisse, Kauf-/Verkaufsbelege → bereitlegen für WV · Fristerstreckungsgesuch → Gemeindesteueramt (vor Fristablauf)
- **Rechnen:** Frist 31. März 2026; Erstreckung nur auf rechtzeitiges Gesuch, längstens 30. November des Folgejahres (darüber nur ausserordentliche Gründe)
- **Limite (Kanton / Bund):** Einreichefrist Steuererklärung: Steuererklärung 2025 (natürliche Personen) bis 31. März 2026 einreiche… / n/a · Regel (Private / Treuhänder), Kosten: Gesuch vor Fristablauf beim Gemeindesteueramt; rechtzeitige Gesuche we… / n/a
- **Beachten:** Erstes rechtzeitiges Erstreckungsgesuch gilt ohne gegenteiligen Entscheid als bewilligt; Mahnfristen nicht erstreckbar
- **Beachten:** Belege nur auf Verlangen (insb. Liegenschaftskosten, Spenden); Papier-SE: Kopien A4, keine CD/DVD
- **Beachten:** Persönlich unterzeichnen; online: Ehegatten bestätigen gemeinsam elektronisch, Beilagen elektronisch
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#seite-1-4-verfahren-einreichung) · [WL ZH 2025 S. 7](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0017.md)

## Hilfsblatt Berufskosten (Form. 360)

### Form. 360 Ziff. 1.1 · Abonnementkosten öffentliche Verkehrsmittel (Code 201 Person 1 / 221 Person 2) ☑️
- **Rein:** Lohnausweis → Feld F (unentgeltliche Beförderung) prüfen · GA/ÖV-Abo für wöchentliche Heimkehr bei Wochenaufenthalt → ebenfalls hier (Ziff. 1)
- **Rechnen:** Σ notwendige Abokosten im Jahr; Zwischentotal Ziff. 1 ≤ Kanton CHF 5'200 / Bund CHF 3'300
- **Limite (Kanton / Bund):** Maximalabzug pro Person (CHF): CHF 5'200 / CHF 3'300
- **Beachten:** Kein Abzug, soweit vom AG vergütet (z. B. LA Feld F unentgeltliche Beförderung) oder bei Geschäftsfahrzeug
- **Beachten:** Plafond gilt inkl. Fahrkosten des Wochenaufenthalts (Kanton 5'200 / Bund 3'300)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-360-ziff-1-1-abzug-berufskosten-fahrkosten) · [Formular 360 ZH 2025 S. 1](../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0001.md)

### Form. 360 Ziff. 1.2 · Fahrrad, Kleinmotorrad (gelbes Kontrollschild) pauschal CHF 700 (Code 202 Person 1 / 222 Person 2) ☑️
- **Rein:**  → –
- **Rechnen:** Pauschale CHF 700/Jahr je Person (Kanton = Bund); zählt zum Zwischentotal Ziff. 1 (≤ Kanton 5'200 / Bund 3'300)
- **Limite (Kanton / Bund):** Pauschale (CHF): CHF 700 / CHF 700 · Maximalabzug pro Person (CHF): CHF 5'200 / CHF 3'300
- **Beachten:** Nur bei ständiger Benützung
- **Beachten:** Bund: tatsächliche Kosten zusätzlich nicht abziehbar
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-360-ziff-1-2-abzug-berufskosten-fahrkosten) · [Formular 360 ZH 2025 S. 1](../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0001.md)

### Form. 360 Ziff. 1.3 · Auto / Motorrad (weisses Kontrollschild), CHF –.70 bzw. –.40 pro km (Code 204 Person 1 / 224 Person 2; Zwischentotal … ☑️
- **Rein:** Fahrzeugausweis → Kontrollschild weiss (Auto/Motorrad), geleast ja/nein · Arbeitszeitnachweis → Arbeitsort, Arbeitstage, Fahrten pro Tag, km · AG-Bestätigung/Arztzeugnis → Begründung Ziff. 7 (Code 2041–2044)
- **Rechnen:** Nur ausnahmsweise (kein ÖV-Anschluss ≥ 1 km, Zeitersparnis > 1 Std., ständige dienstliche Benützung gegen Entschädigung, …
- **Limite (Kanton / Bund):** Ansatz pro km (CHF): CHF 0.70 / CHF 0.70 · Ansatz pro km (CHF): CHF 0.40 / CHF 0.40 · massgebende Arbeitstage pro Jahr: 240 Tage / n/a · Maximalabzug pro Person (CHF): CHF 5'200 / CHF 3'300
- **Beachten:** Nur ausnahmsweise: Haltestelle ≥ 1 km entfernt/kein ÖV, > 1 Std. Zeitersparnis, auf Verlangen des AG, Krankheit
- **Beachten:** Mittagsheimfahrt max. Verpflegungsabzug (Kanton ≤ 3'200/Jahr; Bund ≤ 15/Tag), dafür kein Verpflegungsabzug
- **Beachten:** Geschäftsfahrzeug: kein Fahrkostenabzug; Bund: km-Abzug nur ohne verfügbares/zumutbares ÖV
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-360-ziff-1-3-abzug-berufskosten-fahrkosten) · [Formular 360 ZH 2025 S. 1](../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0002.md)

### Form. 360 Ziff. 7 · Begründung private Motorfahrzeugbenützung ankreuzen: 2041 Fehlen ÖV, 2042 Zeitersparnis über 1 Std., 2043 ständige … ☑️
- **Rein:** Fahrplan/Distanz zur Haltestelle → Code 2041 (ÖV fehlt) bzw. 2042 (Zeitersparnis) · Arbeitgeberbestätigung → Code 2043 · Arztzeugnis → Code 2044 (Person 2: 2241–2244)
- **Rechnen:** Zutreffende Begründung ankreuzen (fehlender ÖV, > 1 Std.
- **Beachten:** 2041: Wohn- oder Arbeitsstätte ≥ 1 km von nächster Haltestelle oder kein ÖV bei Arbeitsbeginn/-ende
- **Beachten:** 2042: > 1 Std. Zeitersparnis (Haustür–Arbeitsplatz retour); 2043: AG verlangt/entschädigt Fahrzeug, Arbeitsweg unbezahlt
- **Beachten:** Unentgeltliches Geschäftsfahrzeug mit pauschaler Fahrkostenberechnung (ZStB 17.1): kein Fahrkostenabzug
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-360-ziff-7-abzug-berufskosten-fahrkosten) · [Formular 360 ZH 2025 S. 1](../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md)

### Form. 360 Ziff. 2.1 (verbilligt) · Mehrkosten Verpflegung bei verbilligter Verpflegung (Kantine, Lunch-Checks): CHF 7.50/Tag, max. CHF 1’600/Jahr (Code … ☑️
- **Rein:** Lohnausweis → Feld G (Kantinenverpflegung/Lunch-Checks) angekreuzt · Arbeitszeitnachweis → Anzahl Arbeitstage mit auswärtiger Verpflegung
- **Rechnen:** min(Arbeitstage × 7.50; 1’600) → Code 206 (Person 2: Code 226), Spalte Staatssteuer und Bundessteuer; Regelfall Kantine/Lunch-Checks: Kanton = Bund (Ausnahmen Bund nach BKV Art. 6 Abs. 2/3, s. beachten: Barbeitrag beim Bund kein halber Abzug, kein Abzug unter Naturalbezugsansätzen)
- **Limite (Kanton / Bund):** Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): CHF 7.50 / CHF 7.50 · Verpflegung bei Verbilligung pro Jahr (CHF): CHF 1'600 / CHF 1'600
- **Beachten:** Nur wenn die Arbeitspause die Heimkehr nicht ermöglicht und trotzdem Mehrkosten entstehen
- **Beachten:** Nicht kumulierbar mit 2.1 voll, 2.2 Schicht oder Mittagsheimfahrt (dann entfällt Verpflegungsabzug)
- **Beachten:** Bund: halber Abzug bei Verbilligung anders als in bar (Gutscheine) oder AG-Kantine; kein Abzug unter Naturalbezugsansatz
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-360-ziff-2-1-verbilligt-abzug-berufskosten-verpflegung) · [Formular 360 ZH 2025 S. 1](../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md)

### Form. 360 Ziff. 2.1 (voll) · Mehrkosten Verpflegung, Verpflegung voll zu Lasten Arbeitnehmer: CHF 15/Tag, max. CHF 3’200/Jahr (Code 208 Person 1 / … ☑️
- **Rein:** Lohnausweis → Feld G nicht angekreuzt (keine Verbilligung) · Arbeitszeitnachweis → Arbeitstage mit auswärtiger Hauptmahlzeit
- **Rechnen:** Wenn die Verpflegung in anderen Gaststätten voll zu Lasten des Arbeitnehmers geht: CHF 15 pro Arbeitstag, bei ständiger auswärtiger …
- **Limite (Kanton / Bund):** Verpflegungsmehrkosten pro Arbeitstag (CHF): CHF 15 / CHF 15 · Verpflegungsmehrkosten pro Jahr (CHF): CHF 3'200 / CHF 3'200
- **Beachten:** Nur wenn Arbeitspause die Heimkehr nicht ermöglicht (Bund: grosse Entfernung oder kurze Essenspause)
- **Beachten:** Nicht kumulierbar mit 2.1 verbilligt, 2.2 Schicht oder Mittagsheimfahrt
- **Beachten:** Bund: kein Abzug mangels Mehrkosten, wenn die Hauptmahlzeit maximal 10 Fr. kostet
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-360-ziff-2-1-voll-abzug-berufskosten-verpflegung) · [Formular 360 ZH 2025 S. 1](../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md)

### Form. 360 Ziff. 2.2 · Mehrkosten bei durchgehender, mind. achtstündiger Schicht- / Nachtarbeit: CHF 15/Schichttag, max. CHF 3’200/Jahr (Code … ☑️
- **Rein:** Arbeitgeberbescheinigung → Anzahl Tage mit durchgehender, mind. achtstündiger Schicht-/Nachtarbeit (Feld «Anzahl Tage»)
- **Rechnen:** Pro ausgewiesenem Schichttag CHF 15, bei ständiger Schicht-/Nachtarbeit max. CHF 3’200 pro Jahr; gestaffelte Arbeitszeit gleichgestellt, …
- **Limite (Kanton / Bund):** Schicht-/Nachtarbeit pro Tag (CHF): CHF 15 / CHF 15 · Verpflegungsmehrkosten pro Jahr (CHF): CHF 3'200 / CHF 3'200
- **Beachten:** Gestaffelte (unregelmässige) Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zu Hause möglich
- **Beachten:** Nicht kumulierbar mit Ziff. 2.1 (verbilligt oder voll)
- **Beachten:** Bund: AG muss Schichttage und Arbeitsort auf Verlangen bescheinigen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-360-ziff-2-2-abzug-berufskosten-verpflegung) · [Formular 360 ZH 2025 S. 1](../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md)

### Form. 360 Ziff. 3 · Übrige Berufskosten: pauschal 3 % des Nettolohns, mind. CHF 2’000, max. CHF 4’000 (Code 212) bzw. effektiv (Code 213) … ☑️
- **Rein:** Lohnausweis → Ziff. 11 Nettolohn (= Brutto − AHV/IV/EO/ALV − PK-Beiträge − NBUV) · Bei effektiv: Aufstellung + Belege (Berufskleider, Werkzeuge/EDV, Fachliteratur, Arbeitszimmer, Verbandsbeiträge)
- **Rechnen:** Berufskleider, Berufswerkzeuge (inkl. EDV), Fachliteratur, privates Arbeitszimmer, Berufsverbandsbeiträge.
- **Limite (Kanton / Bund):** Pauschale in % des Nettolohns: 3 % / 3 % · Pauschale Minimum (CHF): CHF 2'000 / CHF 2'000 · Pauschale Maximum (CHF): CHF 4'000 / CHF 4'000 · Regel: Keine separate Homeoffice-/Arbeitszimmer-Pauschale: Kosten eines priva… / Privates Arbeitszimmer: nur als Teil der Pauschale 'übrige Berufskoste…
- **Beachten:** Effektiv statt Pauschale nur mit Aufstellung und Nachweis im vollen Umfang
- **Beachten:** Privates Arbeitszimmer/Homeoffice in Pauschale enthalten, keine separate Pauschale
- **Beachten:** Bund: Pauschale bei Teilzeit oder unterjähriger Erwerbstätigkeit angemessen kürzen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-360-ziff-3-abzug-berufskosten-uebrige) · [Formular 360 ZH 2025 S. 1](../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0004.md)

### Form. 360 Ziff. 4 · Mehrkosten bei auswärtigem Wochenaufenthalt (Code 2860 Person 1 / 2861 Person 2) ☑️
- **Rein:** Mietvertrag/Mietzinsquittungen → Zimmermiete am Arbeitsort · Aufstellung → Arbeitstage am Wochenaufenthaltsort (Abendessen) · ÖV-Abo/GA wöchentliche Heimkehr → unter Ziff. 1 (nicht hier)
- **Rechnen:** Zusätzlich: Mehrkosten Abendessen CHF 15 pro Arbeitstag bzw. max. CHF 3’200 im Jahr bei ganzjährigem Wochenaufenthalt, Zimmermiete, Kosten …
- **Limite (Kanton / Bund):** Unterkunft (Regel): Auswärtiger Wochenaufenthalt: Mehrkosten Unterkunft = Mietzins für ein… / Mehrkosten Unterkunft: ortsübliche Auslagen für ein Zimmer (nicht eine… · Mehrkosten Verpflegung pro Jahr (CHF): CHF 3'200 / CHF 6'400 · Maximalabzug pro Person (CHF): CHF 5'200 / CHF 3'300
- **Beachten:** Nur Zimmer (nicht Wohnung); Bund: ortsübliche Zimmerkosten
- **Beachten:** Heimkehr i.d.R. nur ÖV, zählt zum Fahrkostenplafond Ziff. 1 (Kanton 5'200 / Bund 3'300)
- **Beachten:** Bund: Verpflegung total CHF 30/Tag, ganzjährig max. 6'400; nicht zusätzlich zu Art. 6 BKV; kein Nachweis höherer Kosten
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-360-ziff-4-abzug-berufskosten-wochenaufenthalt) · [Formular 360 ZH 2025 S. 1](../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0004.md)

### Form. 360 Ziff. 5 · Auslagen bei Nebenerwerb: pauschal 20 %, mind. CHF 800, max. CHF 2’400 (Code 216) bzw. effektiv (Code 217) (Person 2: … ☑️
- **Rein:** Lohnausweis(e) Nebenerwerb → Einkünfte aus allen Nebenbeschäftigungen · Bei effektiv: detaillierte Aufstellung + Nachweise
- **Rechnen:** Gilt für sämtliche Auslagen bei unselbständigem Nebenerwerb (inkl. Fahrkosten, Verpflegung): 20 % der Einkünfte aus allen …
- **Limite (Kanton / Bund):** Pauschale in % der Nebeneinkünfte: 20 % / 20 % · Pauschale Minimum (CHF): CHF 800 / CHF 800 · Pauschale Maximum (CHF): CHF 2'400 / CHF 2'400
- **Beachten:** Pauschale deckt sämtliche Auslagen inkl. Fahrkosten und Verpflegung des Nebenerwerbs
- **Beachten:** Nur unselbständiger Nebenerwerb; Behördenentschädigungen: Verfügungen ZStB 17.3
- **Beachten:** Bund: Basis = Nebeneinkünfte netto (nach Sozialversicherungsbeiträgen), gleiche Grenzen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-360-ziff-5-abzug-berufskosten-nebenerwerb) · [Formular 360 ZH 2025 S. 1](../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0004.md)

### Form. 360 Ziff. 6 · Total der Berufsauslagen (Code 220 Person 1 / 240 Person 2) → Steuererklärung Ziff. 11.1 / 11.2 ☑️
- **Rein:** Übertrag Form. 360 Ziff. 1–5, je Spalte Staatssteuer / Bundessteuer
- **Rechnen:** Code 220 = Zwischentotal Ziff. 1 (≤ Kanton 5'200 / Bund 3'300) + Ziff. 2 + 3 + 4 + 5 → HF S. 3 Ziff. 11.1; Person 2: Code 240 → Ziff. 11.2
- **Limite (Kanton / Bund):** Maximalabzug pro Person (CHF): CHF 5'200 / CHF 3'300
- **Beachten:** Je Person eigene Seite (P1 / P2); Ehegatten nach Massgabe ihrer Beschäftigung
- **Beachten:** Nur nicht vom Arbeitgeber vergütete Auslagen; Formular vollständig ausgefüllt beilegen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-360-ziff-6-berechnung-total) · [Formular 360 ZH 2025 S. 1](../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md)

## Hilfsblatt Versicherungsprämien (Form. 365)

### Form. 365 Teil A Ziff. 1–4 · Bezahlte Prämien: private Krankenversicherung (601), Unfall (602), Lebens-/Rentenversicherung (603), Zinsen von … ☑️
- **Rein:** KK-Prämienabrechnung/Jahresbescheinigung → bezahlte Prämien (nach IPV-Verrechnung) Code 601 · Prämienrechnungen private Unfall- (602), Lebens-/Rentenversicherung (603) · Wertschriftenverzeichnis → Zinsen von Sparkapitalien (604)
- **Rechnen:** Σ 601–604 = Zwischentotal 607; − IPV 605 = Total (A) 606
- **Beachten:** Nur tatsächlich bezahlte Prämien; IPV meist mit KK-Prämie verrechnet → reduzierte Prämie in 601
- **Beachten:** NBUV ist im Nettolohn (Lohnausweis) bereits abgezogen → nicht nochmals erfassen
- **Beachten:** (A) einspaltig; Begrenzung erst in Teil B/C getrennt Kanton / Bund
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-365-teil-a-ziff-1-4-abzug-versicherungspraemien) · [Formular 365 ZH 2025 S. 1](../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md)

### Form. 365 Teil A Ziff. 6 · Abzüglich erhaltene Prämienverbilligungen (Code 605); Total (A) (Code 606) ☑️
- **Rein:** KK-Prämienabrechnung → verrechnete Prämienverbilligung (dann in 601 netto) · IPV-Verfügung/Auszahlungsbeleg → nicht verrechnete Prämienverbilligung → Code 605
- **Rechnen:** (A) 606 = Zwischentotal 607 − IPV 605 (nur soweit nicht schon in 601 gekürzt)
- **Beachten:** Auch IPV für die unterhaltenen Kinder anrechnen
- **Beachten:** Kein Doppelabzug: IPV entweder in 601 gekürzt oder hier abziehen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-365-teil-a-ziff-6-abzug-versicherungspraemien) · [Formular 365 ZH 2025 S. 1](../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md)

### Form. 365 Teil B Ziff. 1 · Maximalabzug Verheiratete: CHF 5’800 / 8’700 (Staat), CHF 3’700 / 5’550 (Bund) (Code 611) ☑️
- **Rein:** Lohnausweis → Ziff. 10.1 ordentliche Beiträge 2. Säule (ja/nein) · 3a-Bescheinigung → Beiträge Säule 3a geleistet (ja/nein) · Steuererklärung S. 1 → Zivilstand (ungetrennte Ehe)
- **Rechnen:** Mit Beiträgen 2./3a: Kanton CHF 5'800 / Bund CHF 3'700; ohne: + Hälfte = Kanton 8'700 / Bund 5'550 (Code 611)
- **Limite (Kanton / Bund):** Versicherungsabzug gemeinsam Besteuerte (CHF): CHF 5'800 / CHF 3'700 · Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): CHF 8'700 / CHF 5'550
- **Beachten:** Gilt für rechtlich und tatsächlich ungetrennte Ehe
- **Beachten:** Erhöhung nur, wenn weder Steuerpflichtige noch Arbeitgeber Beiträge an 2. Säule oder 3a geleistet haben
- **Beachten:** Kinder-/Unterstützungszuschlag separat in B.3 addieren
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-365-teil-b-ziff-1-abzug-versicherungspraemien) · [Formular 365 ZH 2025 S. 1](../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md)

### Form. 365 Teil B Ziff. 2 · Maximalabzug übrige Steuerpflichtige: CHF 2’900 / 4’350 (Staat), CHF 1’800 / 2’700 (Bund) (Code 612) ☑️
- **Rein:** Lohnausweis → Ziff. 10.1 ordentliche Beiträge 2. Säule (ja/nein) · 3a-Bescheinigung → Beiträge Säule 3a geleistet (ja/nein) · Steuererklärung S. 1 → Zivilstand (nicht in ungetrennter Ehe)
- **Rechnen:** Mit Beiträgen 2./3a: Kanton CHF 2'900 / Bund CHF 1'800; ohne: + Hälfte = Kanton 4'350 / Bund 2'700 (Code 612)
- **Limite (Kanton / Bund):** Versicherungsabzug übrige Steuerpflichtige (CHF): CHF 2'900 / CHF 1'800 · Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): CHF 4'350 / CHF 2'700
- **Beachten:** Alle nicht in ungetrennter Ehe Lebenden (Ledige, Verwitwete, Geschiedene, Getrennte)
- **Beachten:** Erhöhung nur, wenn weder Steuerpflichtige noch Arbeitgeber Beiträge an 2. Säule oder 3a geleistet haben
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-365-teil-b-ziff-2-abzug-versicherungspraemien) · [Formular 365 ZH 2025 S. 1](../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md)

### Form. 365 Teil B Ziff. 3 · Zusätzlicher Abzug je Kind / unterstützungsbedürftige Person: CHF 1’300 Staat, CHF 700 Bund (Code 613–615) ☑️
- **Rein:** Steuererklärung S. 1 → Anzahl Kinder bzw. unterstützte Personen mit Kinder-/Unterstützungsabzug
- **Rechnen:** Kinder × Kanton CHF 1'300 / Bund 700 (613); unterstützte Personen × 1'300 (614) / 700 (615); halber Kinderabzug 650 / 350; (B) 616 = B.1 bzw. B.2 + B.3
- **Limite (Kanton / Bund):** Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): CHF 1'300 / CHF 700
- **Beachten:** Nur für Kinder/Personen, für die ein Kinder- oder Unterstützungsabzug zusteht
- **Beachten:** Halber Kinderabzug → halber Zuschlag (Kanton 650 / Bund 350)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-365-teil-b-ziff-3-abzug-versicherungspraemien) · [Formular 365 ZH 2025 S. 1](../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md)

### Form. 365 Teil C · Abzug = niedrigerer Betrag von (A) und (B) (Code 270) → Steuererklärung Ziff. 15 ☑️
- **Rein:** Übertrag (A) Code 606 und (B) Code 616 aus Form. 365
- **Rechnen:** Code 270 = min((A); (B)) je Spalte Kanton / Bund → HF S. 3 Ziff. 15
- **Beachten:** (A) einspaltig; (B) und Abzug C getrennt nach Staats- und Bundessteuer
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-365-teil-c-berechnung-total) · [Formular 365 ZH 2025 S. 1](../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0003.md)

## Hilfsblatt Wertschriftenverzeichnis (Form. 340)

### Form. 340 Kolonne A · Werte mit Verrechnungssteuerabzug – Bruttoertrag A (Code 2309-xx; Zwischentotal 539) ☑️
- **Rein:** Bank-Steuerverzeichnis → Steuerwert 31.12.2025 + Bruttoertrag A · Zins-/Dividendengutschriften → Bruttoertrag vor 35 % VSt · Festgeld-/Kassenobligationen-Abrechnungen, Ausschüttungsbescheinigungen nicht kotierter Titel → beilegen
- **Rechnen:** Bruttoertrag A = Σ Erträge mit VSt-Abzug (brutto); Zwischentotal 539; VSt-Anspruch 540 = 35 % × Total A
- **Beachten:** Kundenguthaben nur bei Bruttozins > CHF 200 in A, sonst Kolonne B
- **Beachten:** Steuerwert: CH-Titel gemäss ESTV-Kursliste 31.12.2025; inländische Fonds: auch thesaurierte Erträge steuerbar
- **Beachten:** Gratisaktien bei Ausgabe steuerbar; Q-Beteiligungen brutto (ungekürzt) erfassen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-340-kolonne-a-einkommen-wertschriften) · [Formular 340 ZH 2025 S. 3](../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md)

### Form. 340 Kolonne B · Werte ohne Verrechnungssteuerabzug – Bruttoertrag B (Code 542) ☑️
- **Rein:** Bank-Steuerauszug → Erträge ohne VSt (Zins ≤ CHF 200, ausländische Titel/Fonds) · Ausländische Ertragsabrechnungen → Bruttoertrag in CHF (Tageskurs) · Wallet-Auszug per Jahresende → Krypto-Steuerwert (ESTV-Jahresendkurs) · Darlehensverträge, STWEG-Abrechnung, Vergütungszinsen → Erträge
- **Rechnen:** Bruttoertrag B = Σ Erträge ohne VSt-Abzug (Fremdwährung × Tageskurs); Zwischentotal 542; Total A + B = 539 + 542 = Code 150 → HF Ziff. 4.1
- **Limite (Kanton / Bund):** Lotterie-/Kleingewinne steuerfrei bis (CHF): CHF 1'000 / CHF 1'100
- **Beachten:** Steuerwerte ausländischer Titel/Guthaben zu ESTV-Devisenkursen 31.12.2025 umrechnen
- **Beachten:** Natural-/Sachgewinne: Freigrenze Kanton CHF 1'000 / Bund CHF 1'100 (darüber ganz steuerbar)
- **Beachten:** Ausländische Fonds/SICAV wie inländische (thesauriert steuerbar), aber in Kolonne B
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-340-kolonne-b-einkommen-wertschriften) · [WL ZH 2025 S. 26](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0168.md)

### Form. 340 Totale · Total Steuerwert (Code 400) und Verrechnungssteueranspruch 35 % (Code 540) ☑️
- **Rein:** Summen Kolonnen Steuerwert, A, B inkl. Beiblätter (2350/2352, 2360/2362) und DA-1 (2370/2371) · Steuerauszug → Kontrolle VSt-Betrag (35 % auf Kolonne A)
- **Rechnen:** Total Steuerwert 400 → HF S. 4 Ziff. 30.1; Total A + B 150 → HF S. 2 Ziff. 4.1; VSt-Anspruch 540 = 35 % × Total A, auf 5 Rappen runden
- **Beachten:** VSt-Rückerstattung wird mit der Steuererklärung beantragt (WV mit Verrechnungsantrag); IBAN angeben
- **Beachten:** Anspruch erlischt, wenn nicht innert dreier Jahre nach Ablauf des Fälligkeitsjahres gestellt
- **Beachten:** WV unterschreiben (Bestätigung VSt-Abzug auf Kolonne A); Q-Ertrag 151 → Ziff. 4.2
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-340-totale-verrechnungssteuer-rueckerstattung) · [Formular 340 ZH 2025 S. 3](../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md)

### Form. 340 DA-1 · Anrechnung ausländischer Quellensteuern / Übertrag ab Formular DA-1 (Code 2370/2371) ☑️
- **Rein:** Ertragsabrechnungen ausländischer Titel → Bruttoertrag (100 %), ausländische Quellensteuer · Bankbelege/Sammelausweise US-Titel → zusätzlicher Steuerrückbehalt USA · Formular DA-1 Seite 3 Totale → WV-Zeile «Übertrag ab Formular DA-1» (2370/2371)
- **Rechnen:** DA-1-Totale → WV-Zeile 2370/2371, Bruttoertrag in Kolonne B; Anrechnung nur, wenn Σ nicht rückforderbare ausl. Quellensteuer > CHF 100
- **Beachten:** ≤ CHF 100, quellensteuerfrei oder voll rückforderbar: nicht ins DA-1, nur WV Kolonne B
- **Beachten:** Steuerrückbehalt USA: kein Mindestbetrag, ohne Bankbelege keine Rückerstattung
- **Beachten:** Anspruch erlischt drei Jahre nach Ablauf der Fälligkeitsperiode; DA-1 inkl. Abrechnungen beilegen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-340-da-1-verrechnungssteuer-rueckerstattung) · [WL ZH 2025 S. 27](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0171.md)

### Form. 340 Code Q/G/N/E/S · Kennzeichnung: G Geschäftsvermögen, N Nutzniessung, E Erbschaft, S Schenkung, Q qualifizierte Beteiligung ≥ 10 % ☑️
- **Rein:** Beteiligungsnachweis/Steuerauszug → Quote ≥ 10 % am Kapital → Code Q · Erbteilungs-/Schenkungsunterlagen → 2025 erhaltene Werte → Code E / S · Nutzniessungs-/Geschäftsunterlagen → Code N / G
- **Rechnen:** Kennzeichnung je Zeile; Σ Erträge Q = Code 151 → HF Ziff. 4.2; Abzug HF Ziff. 16.5 (Privatvermögen) = Q-Ertrag × Kanton 50 % / Bund 30 %; E/S → HF Ziff. 50
- **Beachten:** Q-Erträge ungekürzt (brutto), in A oder B je nach VSt-Pflicht; Formular «Qualifizierte Beteiligungen» beilegen
- **Beachten:** Kinder Jg. 2008 und jünger im WV der Eltern; Jg. 2007 und älter eigenes WV
- **Beachten:** Nutzniessungsvermögen (N) beim Nutzniesser; 2. Säule/3a-Ansprüche bis Fälligkeit nicht im WV
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-340-code-q-g-n-e-s-einkommen-beteiligungen-qualifiziert) · [WL ZH 2025 S. 24](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0155.md)

## Hilfsblatt Schulden (Form. 355)

### Form. 355 Spalte Schuld · Privatschulden inkl. Grundpfandschulden am 31. Dezember – Total (Code 3200) → Ziff. 34 ☑️
- **Rein:** Hypothekar-/Kreditbestätigung per 31. Dezember → Saldo, Gläubiger mit Adresse, Zinssatz · Private Darlehensverträge → Saldo per 31. Dezember, Gläubiger · Zinsbelege → Spalte Schuldzinsen (Code 3201)
- **Rechnen:** Σ Schulden per 31. Dezember (CHF ohne Rappen) = Code 3200 → HF S. 4 Ziff. 34 (Code 470); Σ Schuldzinsen 3201 → HF S. 3 Ziff. 12 (Code 250)
- **Beachten:** Bei Schulden vollständiges Verzeichnis einreichen; Gläubiger mit genauer Adresse und Zinssatz unerlässlich
- **Beachten:** Schuldzinsen ohne Amortisationen und Leasingraten
- **Beachten:** Unverteilte Erbschaft: Schulden und Schuldzinsen anteilmässig
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-355-spalte-schuld-schulden-privat) · [Formular 355 ZH S. 1](../chunks/zh/2025/zh-form-355/zh-form-355__c0001.md)

### Form. 355 Spalte Schuldzinsen · Schuldzinsen des Jahres – Total (Code 3201) → Ziff. 12 ☑️
- **Rein:** Zinsabrechnung/Hypothekarbestätigung Bank 2025 → Schuldzinsen je Gläubiger (Spalte Schuldzinsen) · Darlehens-/Kreditvertrag, Zinsbestätigung privater Gläubiger → Name, Vorname, Adresse Gläubiger + Zins · Saldobestätigung per 31.12.2025 → Spalte «Schuld am 31. Dezember» (Total 3200 → Ziff. 34, Code 470)
- **Rechnen:** Σ Schuldzinsen (3201) → Ziff. 12 (250); max. Ertrag bewegl. + unbewegl. Privatvermögen (inkl. EMW) + 50’000 (Kanton = Bund; Bund: Teilbest.-Beteiligungen zu 70 %)
- **Beachten:** Nicht abziehbar: Amortisationen, Leasingraten (inkl. Zinsanteil); Bund: Baukreditzinsen (= Anlagekosten)
- **Beachten:** Baurechtszinsen nicht hier, sondern beim Liegenschaftsunterhalt (nicht unter der 50’000-Begrenzung)
- **Beachten:** Nur soweit nicht schon unter Ziff. 2 abgezogen; Bund: im Jahr 2025 fällig gewordene Zinsen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-355-spalte-schuldzinsen-abzug-schuldzinsen) · [Formular 355 ZH S. 1](../chunks/zh/2025/zh-form-355/zh-form-355__c0002.md)

## Hilfsblatt Liegenschaften (Form. 350)

### Form. 350 Seite 1 · Steuerwert: Verkehrswert (Codes 5541–55410; Total 3951 → Ziff. 31.1) / Ertragswert Land- und Forstwirtschaft (Codes … ☑️
- **Rein:** Bewertungsmitteilung Gemeindesteueramt (EFH/StWE zu Wohnzwecken) → Spalte Verkehrswert (5541 ff.) · Mieterspiegel/Ertragsaufstellung 2025 (MFH, Geschäftshaus) → Bruttojahresertrag für Ertragswertformel (Spalte Verkehrswert) · Bewertung land-/forstwirtschaftliche Liegenschaft → Spalte Ertragswert (5531 ff.) · Erbschafts-/Nutzniessungs-/Wohnrechtsunterlagen → Anteil bzw. Zuordnung der Liegenschaft
- **Rechnen:** EFH/StWE Wohnen: Wert gem. Bewertung (ZStB 21.1); MFH/Geschäftshaus/StWE Geschäft = Bruttojahresertrag 2025 × 100 / 7,05; 3951 → Ziff. 31.1 (421); 3952 → 31.2 (422)
- **Beachten:** Alle Liegenschaften deklarieren, auch in anderen Kantonen/Ausland; ohne Bewertung → Gemeindesteueramt fragen
- **Beachten:** Bruttojahresertrag inkl. Marktmietwert eigener Wohnung, ohne NK (Heizung, Warmwasser, Treppenhaus usw.)
- **Beachten:** Nutzniessung: 100 % beim Nutzniesser; Wohnrecht: 100 % beim Eigentümer; Bund: keine Vermögenssteuer
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-350-seite-1-vermoegen-liegenschaften) · [Formular 350 ZH S. 1](../chunks/zh/2025/zh-form-350/zh-form-350__c0002.md)

### Form. 350 Seite 2 Spalte Eigenmietwert · Eigenmietwert / Miet- und Pachtzinseinnahmen (Codes 5701–57010 Wohnungen/Zimmer/Garagen; 5711–57110 gewerblich; Total … ☑️
- **Rein:** Bewertungs-/Eigenmietwertmitteilung Gemeindesteueramt → Eigenmietwert EFH/StWE (Spalte Wohnungen, 5701 ff.) · Mieterspiegel/Verwaltungsabrechnung 2025 → Mietzinsen Wohnungen/Garagen (5701 ff.) bzw. gewerblich (5711 ff.) · Vergleichsmiete bei Drittvermietung → Eigenmietwert der eigenen Wohnung im MFH/Geschäftshaus · Wohnrechts-/Nutzniessungsvertrag → Eigenmietwert beim Berechtigten
- **Rechnen:** 5721 = 5701 + 5711 (EMW + Miet-/Pachtzinsen ohne NK-Entschädigungen); EMW: EFH 3,50 % / StWE 4,25 % × Land- + Zeitbauwert; eigene Wohnung im MFH = 70 % × Drittmiete
- **Beachten:** Mieterspiegel je vermietete Liegenschaft beilegen (oder Verwaltungsrechnung; sonst Beiblatt)
- **Beachten:** NK-Entschädigungen (Heizung, Warmwasser, Treppenhaus) nur bis zu den tatsächlichen Aufwendungen ausklammern
- **Beachten:** EFH/StWE: EMW gem. Weisung 2009 (ZStB 21.1), Bewertung vom Gemeindesteueramt; individuelle Schätzung: 60–70 % Marktmiete
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-350-seite-2-spalte-eigenmietwert-einkommen-liegenschaften-eigenmietwert) · [Formular 350 ZH S. 2](../chunks/zh/2025/zh-form-350/zh-form-350__c0006.md)

### Form. 350 Seite 2 Spalte Unterhalts- und Verwaltungskosten · Unterhalts- und Verwaltungskosten: pauschal (Codes 5731–57310) oder effektiv (Codes 5741–57410) ☑️
- **Rein:** Handwerker-/Unterhaltsrechnungen 2025 → effektive Kosten (5741 ff.) · Prämienrechnungen Gebäude-/Sachversicherung → effektive Kosten · Verwaltungs-/StWE-Abrechnung (Verwaltung durch Dritte) → effektive Kosten · Total Mietertrag/Eigenmietwert ohne NK (5721 ff.) → Basis Pauschale (5731 ff.)
- **Rechnen:** Pauschale (5731) = Bruttoertrag ohne NK × Kanton 20 % / Bund 10 % (Gebäude ≤ 10 J.) bzw. 20 %; ODER eff. (5741); 5751 = 5721 – Unterhalt; Σ 3953 → Ziff. 6 (188)
- **Limite (Kanton / Bund):** Gebäude bis 10 Jahre (%): 20 % / 10 % · Gebäude über 10 Jahre (%): 20 % / 20 %
- **Beachten:** Wahl je Liegenschaft und Steuerperiode; keine Pauschale bei vorwiegend geschäftlich genutzter Liegenschaft
- **Beachten:** Bei Pauschale keine weiteren Abzüge ausser Baurechtszinsen; bei Unternutzung Pauschale vom EMW nach Einschlag
- **Beachten:** Effektiv: Aufstellung (Datum, Art, Empfänger, Betrag); Abzug bei Fälligkeit oder Zahlung – einmal gewählt beibehalten
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-350-seite-2-spalte-unterhalts-und-verwaltungskosten-abzug-liegenschaft-unterhalt) · [Formular 350 ZH S. 2](../chunks/zh/2025/zh-form-350/zh-form-350__c0007.md)

### Form. 350 / Ziff. 16 Unterhalt · Investitionen Energiesparen / Umweltschutz, Rückbaukosten Ersatzneubau, Denkmalpflege, Baurechtszinsen ☑️
- **Rein:** Rechnungen Energiespar-/Umweltschutzmassnahmen (bestehende Gebäude) + Subventionsentscheid → effektive Kosten (5741 ff.) · Separate Rückbauabrechnung (Demontage, Abbruch, Abtransport, Entsorgung) → effektive Kosten · Rechnungen denkmalpflegerischer Arbeiten (gesetzlich/behördlich angeordnet) → effektive Kosten · Baurechtsvertrag/Zinsbelege → Aufstellung Baurechtszinsen
- **Rechnen:** (Energie/Umwelt + Denkmalpflege) – Subventionen + Rückbau → eff. (5741 ff.) + Baurechtszinsen; Rest Energie/Rückbau bei negativem Reineinkommen → zwei Folgeperioden
- **Beachten:** Nur bei effektiven Kosten (Pauschale schliesst aus); Energiesparmassnahmen bei Neubauten nicht abziehbar
- **Beachten:** Ersatzneubau: gleiche Person, gleiches Grundstück, gleichartige Nutzung; Übertrag nur für Kosten ab 2020
- **Beachten:** Bund: Baurechtszins nicht abziehbar, wenn der tiefere, nur auf dem Zeitbauwert berechnete EMW beansprucht wird
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-350-ziff-16-unterhalt-abzug-liegenschaft-energie-umwelt) · [StG ZH § 30](../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-30-t1.md)

### Form. 350 / WL Eigenmietwert · Einschlag auf dem Eigenmietwert bei tatsächlicher Unternutzung (Unternutzungsabzug) ☑️
- **Rein:** Eigenmietwertmitteilung Gemeindesteueramt → errechneter Eigenmietwert · Antrag mit Nachweis der dauernd ungenutzten Räume (z. B. nach Wegzug der Kinder) → Einschlag gem. ZStB 21.2
- **Rechnen:** EMW nach Einschlag = errechneter EMW – angemessener Einschlag; Unterhaltspauschale vom EMW nach Einschlag rechnen
- **Beachten:** Kanton: keine Unternutzung bei vier bis sechs Zimmern und zwei oder mehr Bewohnern; nur Ausnahmefälle
- **Beachten:** Bund: nur dauernd unbenutzte Räume (Nachweis Stpfl.); nicht Gäste-/Arbeitszimmer, Besuchszimmer Kinder, Zweitwohnung
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-350-wl-eigenmietwert-sozialabzug-eigenmietwert) · [WL ZH 2025 S. 28](../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0183.md)

## Hilfsblatt Krankheitskosten (Form. 370)

### Form. 370 S.1 Teil A Ziff. 1 · Selbstbehalt gemäss Abrechnung Krankenkasse und Versicherung (Code 300) ☑️
- **Rein:** Leistungsabrechnungen/Jahresübersicht Krankenkasse und Versicherungen 2025 → Selbstbehalt (Code 300) · Kosten- und Prämienzusammenstellung der Krankenkasse → Beilage zu Form. 370
- **Rechnen:** Code 300 = Σ Selbstbehalte gem. Abrechnungen Krankenkasse/Versicherung 2025, alle Personen addiert → Total (A) Code 317
- **Beachten:** Krankenkassenprämien sind keine Krankheitskosten (Bund) → Form. 365 (601) / Ziff. 15 (270)
- **Beachten:** Kosten mehrerer Personen addieren; pro Steuererklärung nur eine Aufstellung
- **Beachten:** Weitere, nicht in Ziff. 1 enthaltene Kosten in Codes 301–307 erfassen (keine Doppelerfassung)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-370-s-1-teil-a-ziff-1-abzug-krankheitskosten) · [Formular 370 ZH S. 1](../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md)

### Form. 370 S.1 Teil A Ziff. 2–3 · Arzt und verordnete Medikamente (Code 301), Zahnarztkosten (Code 302) ☑️
- **Rein:** Arztrechnungen, Apothekenbelege (ärztlich verordnete Medikamente) → Code 301 · Zahnarztrechnungen → Code 302 · Vergütungsabrechnung Krankenkasse/Versicherung zu diesen Rechnungen → Teil B (Code 308)
- **Rechnen:** 301/302 = Σ selbst bezahlte Rechnungen, soweit nicht schon in Code 300; Vergütungen Dritter in Teil B (308) abziehen
- **Beachten:** Nicht: Prävention (Fitness), Fahrten zum Arzt, nicht verordnete Akupunktur, eigene Pflege, Wellness, Schönheit
- **Beachten:** Fahrkosten nur ausnahmsweise: Ambulanz, Fahrten zu auswärtigen Kuren/Therapien, ÖV/Privatwagen unzumutbar
- **Beachten:** Belege geordnet beilegen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-370-s-1-teil-a-ziff-2-3-abzug-krankheitskosten) · [Formular 370 ZH S. 1](../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md)

### Form. 370 S.1 Teil A Ziff. 4–7 · Pflegepersonal (Code 303), Spital/Heilstätten (Code 304), verordnete Therapien/Kuraufenthalte (Code 305), Übrige (Code … ☑️
- **Rein:** Rechnungen Spitex/Pflegepersonal (entgeltliche Leistungen Dritter) → Code 303 · Spital-/Heilstättenrechnungen → Code 304 · Rechnungen + ärztliche Verordnung für Therapien/Kuraufenthalte → Code 305 · Rechnungen medizinische Apparate, Korrekturgläser → freie Zeile 7 (Code 307)
- **Rechnen:** Total (A) Code 317 = 300 + 301 + 302 + 303 + 304 + 305 + 307
- **Beachten:** Eigene Pflegeleistungen nicht abziehbar; nur entgeltliche Leistungen Dritter
- **Beachten:** Heim ohne Behinderung: Pflege, med. Leistungen, Hilfsmittel hier; mit Behinderung → Form. 370 S. 2 (Ziff. 16.4)
- **Beachten:** Anteil Lebenshaltung (z. B. Ernährung) in Teil B Code 311 abziehen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-370-s-1-teil-a-ziff-4-7-abzug-krankheitskosten) · [Formular 370 ZH S. 1](../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md)

### Form. 370 S.1 Teil B · Vergütungen Dritter und Anteil Lebenshaltungskosten: Krankenkasse/Versicherungen (Code 308), Lebenshaltungskosten (Code … ☑️
- **Rein:** Leistungsabrechnungen Krankenkasse/Zusatz-/Unfallversicherung → Code 308 · Spital-/Heimrechnung (Pensions-/Verpflegungsanteil) → Anteil Lebenshaltung Code 311 · Leistungen Haftpflichtversicherung → 308; Hilfswerke, Stiftungen → freie Zeile 3 (Code 312)
- **Rechnen:** Total (B) Code 318 = 308 + 311 + 312, nur soweit nicht bereits unter A abgezogen
- **Beachten:** Lebenshaltungsanteil = Kosten, die auch ohne Krankheit oder Unfall angefallen wären
- **Beachten:** Bund: EL für Krankheitskosten (Art. 3d ELG) anrechnen, jährliche EL (Art. 3a ELG) nicht
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-370-s-1-teil-b-abzug-krankheitskosten) · [Formular 370 ZH S. 1](../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md)

### Form. 370 S.1 Teil C/D · Auslagen netto (C, Code 314) bzw. Pauschale Diät CHF 2500 (D, Code 315) ☑️
- **Rein:** Übertrag Total (A) 317 und (B) 318 aus Form. 370 → Auslagen netto C (314) · Ärztliche Bestätigung andauernde, lebensnotwendige Diät (z. B. Zöliakie) → Pauschale D (315) · Belege Mehrkosten ärztlich angeordnete Diät/Spezialnahrung → effektiv in Teil A
- **Rechnen:** C (314) = A (317) – B (318); D (315) = 2’500 anstelle effektiver Diät-Mehrkosten (Kanton = Bund); → Total C und/oder D (313)
- **Beachten:** Pauschale nur bei andauernder, lebensnotwendiger Diät; nicht zusätzlich zu effektiven Diät-Mehrkosten
- **Beachten:** Bund: bei Diabetes nur effektive Mehrkosten, keine Pauschale
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-370-s-1-teil-c-d-abzug-krankheitskosten) · [Formular 370 ZH S. 1](../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md)

### Form. 370 S.1 Teil E · Berechnung: Total Auslagen (313) abzüglich Selbstbehalt 5 % des Nettoeinkommens (319) = Abzug (320) → Ziff. 22.1 ☑️
- **Rein:** Form. 370 Total der Auslagen (313) → Spalten Staats- und Bundessteuer · Steuererklärung Ziff. 21 Nettoeinkommen (Code 310) je Spalte → Basis Selbstbehalt
- **Rechnen:** 319 = 5 % × Nettoeinkommen Ziff. 21 (310), je Spalte Staat / Bund; Abzug 320 = 313 – 319 (nur positiver Rest) → Ziff. 22.1
- **Limite (Kanton / Bund):** Selbstbehalt in % des Nettoeinkommens: 5 % / 5 %
- **Beachten:** Nettoeinkommen = Einkünfte – Aufwendungen §§ 26–31 StG bzw. Art. 26–33 DBG (Staat ≠ Bund)
- **Beachten:** Behinderungsbedingte Kosten ohne Selbstbehalt → Ziff. 16.4, nicht hier
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-370-s-1-teil-e-abzug-krankheitskosten) · [Formular 370 ZH S. 1](../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md)

### Form. 370 S.2 Teil A/B · Behinderungsbedingte Kosten: effektive Aufwendungen (Codes 3100–3120) und Vergütungen Dritter (Codes 3130–3150) ☑️
- **Rein:** Rechnungen Pflege/Betreuung, Therapien, Hilfsmittel, Transporte, Wohnungsanpassung → Code 3100 · Rechnungen Heim-/Entlastungsaufenthalt (Pension + Pflege) → Code 3101 · Abrechnungen Krankenkasse/Versicherungen → 3130; Verfügung Hilflosenentschädigung → 3131 · IV-/HE-Verfügung, Pflegeeinstufung Heim (BESA/RAI), ärztl. Fragebogen (Bund) → Nachweis Behinderung
- **Rechnen:** A (3120) = 3100 + 3101 + 3102; B (3150) = 3130 + 3131 + 3132 + 3133; Heim 3132: Kanton 2’000 × Monate / Bund Existenzminimum Art. 93 SchKG od. kant. Richtlinie
- **Beachten:** Nur bei Behinderung i. S. BehiG (u. a. HE-/IV-Bezüger; Pflege ≥ 60 Min./Tag; ZH-Heim ab BESA-/RAI-Stufe 4)
- **Beachten:** Heim ohne Behinderung → Krankheitskosten (S. 1); Haushalt-/Kinderbetreuung nur soweit über Abzug Ziff. 16.6
- **Beachten:** Heim: Pflegetaxen KVG und Hilflosenentschädigungen abziehen; eine Aufstellung pro Steuererklärung
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-370-s-2-teil-a-b-abzug-behinderungskosten) · [Formular 370 ZH S. 2](../chunks/zh/2025/zh-form-370/zh-form-370__c0005.md)

### Form. 370 S.2 Teil C/D · Total abzugsberechtigte Kosten (Code 3155) bzw. Pauschale (Code 3103) → Ziff. 16.4 ☑️
- **Rein:** Übertrag A (3120) und B (3150) aus Form. 370 S. 2 → C (3155) · Verfügung Hilflosenentschädigung (Grad) → Pauschale D (3103) · Nachweis Gehörlosigkeit bzw. Dialysepflicht → Pauschale D (3103)
- **Rechnen:** Entweder 3155 = 3120 – 3150 ODER Pauschale 3103: HE leicht 2’500 / mittel 5’000 / schwer 7’500; Gehörlose, Dialyse 2’500 (Kanton = Bund) → Ziff. 16.4 (3160)
- **Beachten:** Kein Selbstbehalt (anders als Krankheitskosten Ziff. 22.1)
- **Beachten:** Pauschale anstelle der effektiven Kosten (nicht kumulieren); Art der Pauschale angeben
- **Beachten:** Bund: Kinder zusätzlich zum Kinderabzug; übrige Unterstützte nur effektive Kosten, soweit über Unterstützungsabzug
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-370-s-2-teil-c-d-abzug-behinderungskosten) · [Formular 370 ZH S. 2](../chunks/zh/2025/zh-form-370/zh-form-370__c0006.md)

## Hilfsblatt Weiterbildung (Form. 367)

### Form. 367 · Total der Kosten (Code 2900/2903), Beitrag Arbeitgeber/Dritte (2901/2904), Selbstgetragene Kosten (2902/2905), … ☑️
- **Rein:** Kursrechnungen/Zahlungsbelege 2025 → Total der Kosten (2900/2903) · Lohnausweis Ziff. 13.3 → Beitrag Arbeitgeber (2901/2904) · Bestätigungen Beiträge Bund/Branchenverbände → Beitrag weiterer Stellen (2901/2904)
- **Rechnen:** Je Person: 2902/2905 = 2900/2903 – 2901/2904; Abzug 2920/2921 (Person 1/Person 2) = min(selbstgetragen; Kanton 12’400 / Bund 13’000); 292 = 2920 + 2921 je Block Staats-/Bundessteuer → Ziff. 16.2
- **Limite (Kanton / Bund):** Maximum (CHF): CHF 12'400 / CHF 13'000
- **Beachten:** Nur mit Abschluss Sek. II oder ab vollendetem 20. Lebensjahr; nicht Ausbildung bis zum ersten Sek.-II-Abschluss
- **Beachten:** Massgebend ist Fälligkeit bzw. Zahlung, nicht der Kursbesuch
- **Beachten:** Formular 367 vollständig ausgefüllt beilegen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#form-367-abzug-weiterbildung) · [Formular 367 ZH 2025 S. 1](../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md)

## Lohnausweis-Regeln

### Lohnausweis Feld F · Unentgeltliche Beförderung zwischen Wohn- und Arbeitsort → kein Fahrkostenabzug (Form. 360 Ziff. 1) ☑️
- **Rein:** Lohnausweis Feld F (Kreuz) → kein Fahrkostenabzug in Form. 360 Ziff. 1 · Lohnausweis Ziff. 2.2 (Privatanteil Geschäftswagen) → im Bruttolohn; Fahrkostenabzug entfällt
- **Rechnen:** Feld F ⇒ Form. 360 Ziff. 1 (Codes 201–205) leer; Geschäftsfahrzeug mit pauschaler Fahrkostenberechnung (Bund 0,9 % Kaufpreis/Monat; Kanton ZStB 17.1) ⇒ kein Abzug
- **Beachten:** Feld F u. a. bei Geschäftsfahrzeug, Sammeltransport, Vergütung effektiver Autokilometer an Aussendienst
- **Beachten:** Wer über ein Geschäftsfahrzeug verfügt, kann keine Fahrkosten abziehen (Kanton und Bund)
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#lohnausweis-feld-f-abzug-berufskosten-fahrkosten) · [WL Lohnausweis 2026 S. 8](../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md)

### Lohnausweis Feld G · Kantinenverpflegung / Lunch-Checks → reduzierter Verpflegungsabzug (Form. 360 Ziff. 2.1 verbilligt, Code 206) ☑️
- **Rein:** Lohnausweis Feld G (Kreuz) → Form. 360 Ziff. 2.1 verbilligt (Code 206) · Lohnausweis ohne Feld G, Verpflegung voll zulasten AN → Form. 360 Ziff. 2.1 (Code 208) · Lohnausweis Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt» → Folge für Abzug prüfen
- **Rechnen:** Feld G ⇒ Code 206 = min(Arbeitstage × 7.50; 1’600) statt Code 208 = min(Arbeitstage × 15; 3’200); Beträge Kanton = Bund (Bund: halber Abzug)
- **Limite (Kanton / Bund):** Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): CHF 7.50 / CHF 7.50 · Verpflegung bei Verbilligung pro Jahr (CHF): CHF 1'600 / CHF 1'600 · Verpflegungsmehrkosten pro Arbeitstag (CHF): CHF 15 / CHF 15 · Verpflegungsmehrkosten pro Jahr (CHF): CHF 3'200 / CHF 3'200
- **Beachten:** Feld G auch bei Lunch-Checks, verbilligtem Personalrestaurant (Nutzung egal), 40–60 % Aussendienst mit Essensgeld
- **Beachten:** Kanton: Barbeitrag gilt als Verbilligung; Bund: halber Abzug nur bei Gutscheinen oder Kantine/Personalrestaurant
- **Beachten:** Bund: kein Abzug mangels Mehrkosten, wenn Hauptmahlzeiten max. 10 Fr. kosten
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#lohnausweis-feld-g-abzug-berufskosten-verpflegung) · [WL Lohnausweis 2026 S. 8–9](../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md)

### Lohnausweis Ziff. 10.2 · Beiträge für den Einkauf in die berufliche Vorsorge – bereits vom Lohn abgezogen → nicht nochmals unter Ziff. 16.1 … ☑️
- **Rein:** Lohnausweis Ziff. 10.2 (vom Lohn abgezogener Einkauf) → bereits im Nettolohn Ziff. 11; kein Abzug Ziff. 16.1 · Formular 21 EDP der Vorsorgeeinrichtung (selbst bezahlter Einkauf) → Ziff. 16.1 (Code 280) · Einkaufsbescheinigung der Vorsorgeeinrichtung → Beilage zur Steuererklärung
- **Rechnen:** LA Ziff. 11 = Ziff. 8 – (Ziff. 9 + 10); Ziff. 16.1 (Code 280) = nur nicht vom Lohn abgezogene Einkäufe gem. Formular 21 EDP
- **Beachten:** Einkauf nicht abziehbar, soweit innerhalb von drei Jahren ein Kapitalbezug erfolgt
- **Beachten:** Ziff. 10.2 enthält auch vom AG übernommene AN-Beiträge, sofern in LA Ziff. 7 aufgeführt
- **Beachten:** Bescheinigung der Vorsorgeeinrichtung über abziehbare Einkäufe mit der Steuererklärung einreichen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#lohnausweis-ziff-10-2-abzug-vorsorge-saeule2-einkauf) · [WL Lohnausweis 2026 S. 14–15](../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md)

### Lohnausweis Ziff. 13.3 · Beiträge des Arbeitgebers an berufsorientierte Aus- und Weiterbildung → Form. 367 «Beitrag Arbeitgeber» ☑️
- **Rein:** Lohnausweis Ziff. 13.3 → Form. 367 «Beitrag Arbeitgeber» (2901/2904) · Kursrechnungen (auch auf AN-Namen, vom AG vergütet) → Total der Kosten (2900/2903) · Auskunft AG über direkt an Bildungsinstitut bezahlte Beträge (nicht im Lohnausweis)
- **Rechnen:** Selbstgetragen (2902/2905) = Total (2900/2903) – Beiträge AG/Dritte (2901/2904); Abzug = min(selbstgetragen; Kanton 12’400 / Bund 13’000)
- **Limite (Kanton / Bund):** Maximum (CHF): CHF 12'400 / CHF 13'000
- **Beachten:** Direkt an Dritte (z. B. Bildungsinstitut) bezahlte AG-Beiträge fehlen im LA – nicht als eigene Kosten erfassen
- **Beachten:** Vergütete Rechnungen auf den Namen des AN sind immer in Ziff. 13.3 bescheinigt
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#lohnausweis-ziff-13-3-abzug-weiterbildung) · [WL Lohnausweis 2026 S. 18](../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md)

### Lohnausweis Ziff. 15 · Bemerkungen: Anzahl Schichttage u. a. → Grundlage für Schichtarbeitsabzug (Form. 360 Ziff. 2.2, Code 210) ☑️
- **Rein:** Lohnausweis Ziff. 15 (Anzahl Schichttage) → Form. 360 Ziff. 2.2 (Code 210) · Arbeitgeberbescheinigung Schicht-/Nachttage und Arbeitsort → Nachweis
- **Rechnen:** Code 210 = min(Schichttage × 15; 3’200) (Kanton = Bund); nicht kumulierbar mit Verpflegungsabzug Ziff. 2.1 (Codes 206/208)
- **Limite (Kanton / Bund):** Schicht-/Nachtarbeit pro Tag (CHF): CHF 15 / CHF 15
- **Beachten:** Durchgehende, mind. achtstündige Schicht-/Nachtarbeit; gestaffelte Arbeitszeit gleich, wenn Mahlzeiten nicht zu Hause
- **Beachten:** LA Ziff. 15 freiwillig; Bund: AG muss Schichttage und Arbeitsort auf Verlangen bescheinigen
- ↗ [Detail](../wiki/zh/zuordnung-zh-2025-detail.md#lohnausweis-ziff-15-abzug-berufskosten-verpflegung) · [WL Lohnausweis 2026 S. 18–19](../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md)
