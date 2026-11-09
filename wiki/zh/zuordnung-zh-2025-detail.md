---
typ: zuordnung-detail
titel: Zuordnung ZH 2025 – Detail
jur: zh
jahre:
- 2025
generiert: tools/build_quick.py aus data/zuordnung/zh/2025.yaml (2026-11-09)
---

# ZH 2025: Zuordnung Beleg → Ziffer – Detail

> Kompaktansicht: [quick/zuordnung-zh-2025.md](../../quick/zuordnung-zh-2025.md) · Formular: Steuererklärung 2025 Kanton Zürich (StA Form. 300, Hauptformular) + Hilfsblätter Form. 340 (Wertschriften- und Guthabenverzeichnis), 350 (Liegenschaftenverzeichnis), 355 (Schuldenverzeichnis), 360 (Berufsauslagen), 365 (Versicherungsprämien), 367 (Aus- und Weiterbildungskosten), 370 (Krankheits-/Unfallkosten, behinderungsbedingte Kosten) · Quelle der Wahrheit: `data/zuordnung/zh/2025.yaml`

> **Hinweis:** Codes bezeichnen Zeilen, nicht Spalten. Hauptformular und Form. 365: ein Code je Zeile für beide Spalten. Form. 360: derselbe Code in beiden Spalten (z.B. 206); Person 2 hat eigene Codes (226 usw.). Ein Codepaar «X/Y» heisst je nach Blatt Person 1/Person 2 (Form. 360 206/226; Form. 367: Spalten Person 1/Person 2, 2900/2903) oder Staat/Bund (Form. 365: 614 Staat 1’300 / 615 Bund 700) – massgebend ist die Bezeichnung der Position. Belege: zh-form-360-2025__c0003 «Mehrkosten entstehen: pro Arbeitstag CHF 7.50 / im Jahr CHF 1’600 206 3211 206» («3211» = Layoutartefakt der Eingabefelder, kein Code; Spaltenlage per raw/zh/2025/zh-form-360-2025.pdf S. 1 geprüft); zh-form-360-2025__c0008 «Mehrkosten entstehen: pro Arbeitstag CHF 7.50 / im Jahr CHF 1’600 226»; zh-form-365-2025__c0002 «Zusätzlicher Abzug für jede unterstützungsbed. Person Anzahl: 700 615»; zh-form-367-2025__c0001 «Bezeichnung Person 1 Person 2».

## Einkünfte

<a id="1-1-einkommen-unselbstaendig-haupterwerb"></a>
### Ziff. 1.1 – Haupterwerb unselbständig, Person 1 / Person 2 (Code 100/101)

- **Schlüssel:** `einkommen.unselbstaendig.haupterwerb` (Unselbständige Erwerbstätigkeit – Haupterwerb (Nettolohn)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn / Rente)
- **Rein:** Lohnausweis (je Arbeitgeber) → Ziff. 11 Nettolohn / Rente · Lohnausweis → Ziff. 8 Bruttolohn, Ziff. 9 AHV/IV/EO/ALV/NBUV, Ziff. 10.1/10.2 BVG (Plausibilität)
- **Rechnen:** je Person: Σ LA Ziff. 11 (= Ziff. 8 − Ziff. 9 − Ziff. 10.1 − Ziff. 10.2) aller Haupterwerbe → Code 100 (P1) / 101 (P2); Kanton = Bund
- **Regel:** Nettolohn gemäss Lohnausweis Ziff. 11 einsetzen (nach Abzug AHV/IV/EO/ALV, laufender BVG-Beiträge und NBUV-Prämien); Lohnausweis beilegen; Erwerbslücken ausdrücklich bezeichnen. Je Person eine Zeile (P1 = 100, P2 = 101). Lohnausweis-Felder F, G, 10.2, 13.3, 15 beachten (siehe Abschnitt Lohnausweis-Regeln).
- **Beachten:** Erwerbslücken ausdrücklich bezeichnen (zeigt, dass keine Einkommensbescheinigung vergessen wurde).
- **Beachten:** BVG-Einkauf im LA (Ziff. 10.2) ist schon abgezogen – nicht nochmals in Ziff. 16.1 (Code 280).
- **Beachten:** Zum Lohn gehören auch Spesen ohne entsprechende Ausgaben, Naturalbezüge, Mitarbeiterbeteiligungen.
- **Bund:** Gleiche Zeile für Staats- und Bundessteuer (eine Spalte, kein Unterschied).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Haupterwerb Person 1 Lohnausweis»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Person 2 Lohnausweis 101»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0032.md) `zh-wl-2025__c0032` – «In der Steuererklärung ist der Nettolohn (d.h. der Lohn nach Abzug von AHV/IV/EO- und»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0034.md) `zh-wl-2025__c0034` – «8. Bruttolohn total / Rente»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0034.md) `zh-wl-2025__c0034` – «Beiträge AHV/ IV/ EO /ALV/ NBUV»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0035.md) `zh-wl-2025__c0035` – «10.2 Beiträge für den Einkauf»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0035.md) `zh-wl-2025__c0035` – «11. Nettolohn / Rente»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0035.md) `zh-wl-2025__c0035` – «13. Spesenvergütungen – Allocations pour frais»
  - [WL ZH 2025 S. 19](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0114.md) `zh-wl-2025__c0114` – «16.1 Beiträge an die AHV, IV und 2. Säule, sofern nicht unter Ziff. 1 und 2 abgezogen   280»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0030.md) `zh-wl-2025__c0030` – «als Spesenvergütungen bezeichnete Leistungen, denen keine entsprechenden Ausgaben»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0031.md) `zh-wl-2025__c0031` – «Mitarbeiterbeteiligungen (wie Aktien, Optionen, Anwartschaften).»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0032.md) `zh-wl-2025__c0032` – «Unentgeltliche Beförderung zwischen Wohn- und Arbeitsort»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0032.md) `zh-wl-2025__c0032` – «Kantinenverpflegung / Lunch-Checks»

<a id="1-2-einkommen-unselbstaendig-nebenerwerb"></a>
### Ziff. 1.2 – Nebenerwerb unselbständig inkl. Behörden-/VR-Entschädigungen, Person 1 / Person 2 (Code 102/103)

- **Schlüssel:** `einkommen.unselbstaendig.nebenerwerb` (Unselbständige Erwerbstätigkeit – Nebenerwerb (inkl. VR-/Behördenentschädigungen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn / Rente) des Nebenerwerbs-Lohnausweises
- **Rein:** Lohnausweis Nebenerwerb → Ziff. 11 Nettolohn · Lohnausweis → Ziff. 6 Verwaltungsratsentschädigungen; Honorarabrechnung (Behörde, Vorstand, Tantiemen, Lizenzen) · Aufstellung effektive Auslagen (nur wenn > Pauschale)
- **Rechnen:** Σ LA Ziff. 11 Nebenerwerbe → 102 (P1) / 103 (P2); Auslagen Form. 360 Ziff. 5: max(800; min(20 % × Nebeneinkünfte; 2’400)) → 216|217 (P2: 236|237); Kanton = Bund
- **Regel:** Sämtliche Einkünfte aus unselbständigen Nebenerwerbstätigkeiten (Dienstleistungen jeder Art, Amtstätigkeit, Verwaltungsrats-/Vorstandshonorare, Tantiemen, Lizenzen, Autorenrechte) einsetzen. Berufsauslagen dazu: Pauschale 20 % (Form. 360 Ziff. 5, Code 216/217) oder effektiv.
- **Beachten:** Im vereinfachten Verfahren (BG gegen Schwarzarbeit) abgerechnete Einkünfte nicht hier – nur Bescheinigung beilegen.
- **Beachten:** Behördenentschädigungen: Verfügung der Finanzdirektion ZStB 17.3 beachten.
- **Beachten:** Effektive Auslagen > Pauschale: Aufstellung beilegen, auf Verlangen voller Nachweis.
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Auslagen bei Nebenbeschäftigung in unselbständiger Stellung (inkl. Fahrkosten, Verpflegung): 20 % der Einkünfte aus allen Nebenbeschäftigungen, mind. CHF 800, höchstens CHF 2'400.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge))**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Minimum Nebenerwerbspauschale: CHF 800.)** · Bund **CHF 800 (Minimum Pauschale Nebenerwerb)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Maximum Nebenerwerbspauschale: CHF 2'400.)** · Bund **CHF 2'400 (Maximum Pauschale Nebenerwerb)**
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Nebenerwerb Person 1 Lohnausweis 102»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Vergütungen für Amtstätigkeit, Verwaltungsrats- und Vorstands»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0033.md) `zh-wl-2025__c0033` – «Hier sind sämtliche Einkünfte aus unselbständigen Nebenerwerbstätigkeiten aufzuführen»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0035.md) `zh-wl-2025__c0035` – «11. Nettolohn / Rente»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0034.md) `zh-wl-2025__c0034` – «6. Verwaltungsratsentschädigungen – Indemnités des membres de l’administration»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0072.md) `zh-wl-2025__c0072` – «20% der Einkünfte aus allen Nebenbeschäftigungen, insgesamt mindestens jedoch CHF 800 und höchstens CHF 2’400.»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0072.md) `zh-wl-2025__c0072` – «Behörden des Kantons und der Gemeinden (ZStB 17.3)»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0062.md) `zh-wl-2025__c0062` – «20% der Einkünfte aus Nebenerwerb, mind. CHF 800 und höchstens CHF 2‘400   216»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0069.md) `zh-wl-2025__c0069` – «bzw. effektiv   gemäss Aufstellung   217»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0009.md) `zh-form-360-2025__c0009` – «20% der Einkünfte aus Nebenerwerb, mind. CHF 800 und höchstens CHF 2‘400   236»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0009.md) `zh-form-360-2025__c0009` – «bzw. effektiv   gemäss Aufstellung   237»

<a id="1-2-einkommen-vereinfachtes-verfahren"></a>
### Ziff. 1.2 – Im vereinfachten Verfahren abgerechnete Einkünfte (Bescheinigung AHV-Ausgleichskasse)

- **Schlüssel:** `einkommen.vereinfachtes_verfahren` (Vereinfacht abgerechnete Erwerbseinkünfte (nur Information)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der AHV-Ausgleichskasse (kein Lohnausweis)
- **Rein:** Bescheinigung der AHV-Ausgleichskasse (vereinfachtes Abrechnungsverfahren) → nur als Beilage
- **Rechnen:** Kein Betrag in Ziff. 1.2 (Code 102/103) für Einkünfte mit Quellensteuer nach BG gegen die Schwarzarbeit; nur Bescheinigung beilegen
- **Regel:** Einkünfte, für die im vereinfachten Verfahren (Bundesgesetz gegen die Schwarzarbeit) abgerechnet wurde, nicht als Lohn aufführen; die Bescheinigung der AHV-Ausgleichskasse ist der Steuererklärung beizulegen.
- **Beachten:** Nur für tatsächlich im vereinfachten Verfahren abgerechnete Löhne; übrige Nebenlöhne → Ziff. 1.2 (Lohnausweis).
- **Quellen:**
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0033.md) `zh-wl-2025__c0033` – «gegen die Schwarzarbeit bezahlt wurden. Der Steuererklärung ist jedoch die Bescheinigung»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0033.md) `zh-wl-2025__c0033` – «Nicht aufzuführen sind solche Einkünfte, für welche Quellensteuern gemäss dem Bundesgesetz»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0034.md) `zh-wl-2025__c0034` – «der AHV-Ausgleichskasse beizulegen.»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Nebenerwerb Person 1 Lohnausweis 102»

<a id="2-1-einkommen-selbstaendig"></a>
### Ziff. 2.1 – Selbständige Erwerbstätigkeit Haupterwerb, Person 1 / Person 2 (Code 120/121)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsblatt A (Reingewinn nach Steuerkorrekturen) bzw. Hilfsblatt B/G (Landwirtschaft)
- **Rein:** Jahresrechnung (Bilanz, Erfolgsrechnung, Anhang, unterzeichnet) + Kontoblätter Privat-/Eigenkapitalkonten · Hilfsblatt A (kaufm./vereinfachte Buchführung) → Ziff. 5 Code 1750; Landwirtschaft: Hilfsblatt B bzw. G · Abrechnung persönliche AHV/IV/EO-Beiträge → HB A Ziff. 4.1 (1741) aufrechnen, Abzug Ziff. 16.1 · Liquidation: Hilfsformular «Liquidationsgewinn bei Aufgabe der selbständigen Erwerbstätigkeit» (Abzug Ziff. 16.5)
- **Rechnen:** HB A: Reingewinn 1810 ± Korrekturen 1811–1815 = AHV-Einkommen 1740 + AHV/IV/EO 1741 − Wertschriftenerträge im WV 1742 − weitere 1743 = 1750 → 120/121
- **Regel:** Ergebnis aus Hilfsblatt A einsetzen (inkl. qualifizierte Beteiligungen im Geschäftsvermögen und Liquidationsgewinne). Bei kaufmännischer Buchführung unterzeichnete Jahresrechnung (Bilanz, Erfolgsrechnung, Anhang) einreichen. Liquidationsgewinne (ab 55 / Invalidität) werden gesondert besteuert und unter Ziff. 16.5 wieder abgezogen.
- **Beachten:** Eigene BVG-Beiträge im Geschäft nur wie AG-Anteil Personal (sonst Hälfte, ohne Einkäufe); Rest, Einkäufe, 3a in der StE.
- **Beachten:** Grundstückgewinn Geschäftsvermögen: Bund voll; Staat freizustellenden Teil in Ziff. 16.5 (Kolonne Staat) abziehen.
- **Beachten:** Liquidationsgewinn (Aufgabe nach vollendetem 55. Altersjahr/Invalidität, letzte 2 GJ): gesondert, Abzug Ziff. 16.5.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Haupterwerb Person 1 Hilfsblatt»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0039.md) `zh-wl-2025__c0039` – «reichen Sie eine unterzeichnete Jahresrechnung (Einzelabschluss»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0043.md) `zh-wl-2025__c0043` – «Solche Liquidationsgewinne können unter Ziffer 16.5 wieder von den Einkünften abgezogen werden»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0040.md) `zh-wl-2025__c0040` – «Reingewinn bzw. -verlust gemäss Erfolgsrechnung»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0041.md) `zh-wl-2025__c0041` – «Naturalbezüge und Privatanteile an den Unkosten   1814»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0041.md) `zh-wl-2025__c0041` – «Weitere Korrekturen   1815»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0041.md) `zh-wl-2025__c0041` – «Subtotal = Einkünfte aus selbständiger Erwerbstätigkeit für AHV-Zwecke   1740»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0041.md) `zh-wl-2025__c0041` – «Persönliche AHV/IV/EO-Beiträge (in Ziff. 16.1 der Steuererklärung abzuziehen)   1741»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0041.md) `zh-wl-2025__c0041` – «Abzüglich verbuchte Bruttoerträge von Geschäftswertschriften und -guthaben,»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0042.md) `zh-wl-2025__c0042` – «Einkünfte aus selbständiger Erwerbstätigkeit   1750»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0042.md) `zh-wl-2025__c0042` – «Als Geschäftsanteil gilt derjeni-»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0043.md) `zh-wl-2025__c0043` – «an die gebundene Selbstvorsor-»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0039.md) `zh-wl-2025__c0039` – «Auszüge (= Kontoblätter aus»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0044.md) `zh-wl-2025__c0044` – «der Bundessteuer Gewinne auf Grundstücken des Geschäftsvermögens vollumfänglich der»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0044.md) `zh-wl-2025__c0044` – «Für die Staatssteuer ist der bei der Einkommenssteuer freizustellende Teil des Grundstückgewinns in Ziffer 16.5»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0043.md) `zh-wl-2025__c0043` – «werbstätigkeit nach dem vollendeten 55. Altersjahr oder wegen Unfähigkeit zur Weiterführung»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0038.md) `zh-wl-2025__c0038` – «Führen Sie einen Landwirtschaftsbetrieb? Dann verwenden Sie bitte das Hilfsblatt B»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0036.md) `zh-wl-2025__c0036` – «dem Hilfsblatt A für Selbständigerwerbende mit kaufmännischer Buchführung oder dem»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0103.md) `zh-wl-2025__c0103` – ««Liquidationsgewinn bei Aufgabe der selbständigen Erwerbstätigkeit» erforderlich.»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0043.md) `zh-wl-2025__c0043` – «infolge Invalidität stille Reserven, die in den letzten zwei Geschäftsjahren realisiert worden sind,»

<a id="2-2-einkommen-selbstaendig"></a>
### Ziff. 2.2 – Selbständige Erwerbstätigkeit Nebenerwerb, Person 1 / Person 2 (Code 122/123)

- **Schlüssel:** `einkommen.selbstaendig` (Selbständige Erwerbstätigkeit (Haupt-/Nebenerwerb, Landwirtschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsblatt bzw. Aufstellung des Nebenerwerbs
- **Rein:** Hilfsblatt A (Nebenerwerb, Code 1692/1693) → Ziff. 5 Einkünfte (Code 1750) · bzw. eigene Aufstellung der Nebentätigkeit (statt Hilfsblatt) · Kauf-/Verkaufsabrechnungen Wertschriften/Liegenschaften (nur bei Tätigkeit über schlichte Vermögensverwaltung hinaus)
- **Rechnen:** Ergebnis Hilfsblatt A Ziff. 5 (1750) bzw. Aufstellung → Code 122 (P1) / 123 (P2); Kanton = Bund (Ausnahme Grundstückgewinn, s. beachten)
- **Regel:** Sämtliche Einkünfte aus selbständigen Nebenerwerbstätigkeiten angeben (Hilfsblatt bzw. Aufstellung); Gewinne aus Wertschriften-/Liegenschaftsverkäufen nur, soweit über die schlichte Vermögensverwaltung hinaus (siehe WL).
- **Beachten:** Veräusserungsgewinne Wertschriften/Liegenschaften nur, wenn Tätigkeit die schlichte Vermögensverwaltung übersteigt.
- **Beachten:** Grundstückgewinn: Staat freizustellenden Teil in Ziff. 16.5 abziehen; Liegenschaftenhändler: § 221 Abs. 2 StG.
- **Beachten:** Unselbständige Nebenerwerbe (mit Lohnausweis) gehören in Ziff. 1.2, nicht hierher.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Nebenerwerb Person 1 Hilfsblatt»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0047.md) `zh-wl-2025__c0047` – «Hier sind sämtliche Einkünfte aus selbständigen Nebenerwerbstätigkeiten anzugeben»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0038.md) `zh-wl-2025__c0038` – «Nebenerwerb   1692   Person 1   1693   Person 2»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0042.md) `zh-wl-2025__c0042` – «Einkünfte aus selbständiger Erwerbstätigkeit   1750»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0048.md) `zh-wl-2025__c0048` – «stammen, welche die schlichte Vermögensverwaltung übersteigt.»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0049.md) `zh-wl-2025__c0049` – «stückgewinns in Ziffer 16.5 der Steuererklärung, Kolonne Staatssteuer, abzuziehen.»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0049.md) `zh-wl-2025__c0049` – «werden Personen, die mit Liegenschaften handeln, speziell auf § 221 Abs. 2 Steuergesetz»

<a id="3-1-einkommen-sozialversicherung-ahv-iv"></a>
### Ziff. 3.1 – AHV-/IV-Renten (100 %), Person 1 / Person 2 (Code 130/131)

- **Schlüssel:** `einkommen.sozialversicherung.ahv_iv` (AHV-/IV-Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung AHV/IV (Ausgleichskasse, Jahresbescheinigung der Renten) → Rentenbescheinigung AHV/IV (Jahresbetrag)
- **Rein:** Rentenbescheinigung AHV bzw. IV (Ausgleichskasse) → Jahresbetrag 2025 je Person
- **Rechnen:** Σ AHV-/IV-Renten 2025 × 100 % je Person → Code 130 (P1) / 131 (P2); Kästchen AHV oder IV ankreuzen; Kanton = Bund
- **Regel:** AHV-/IV-Renten sind zu 100 % steuerbar; Jahresbetrag einsetzen, Haken AHV oder IV setzen.
- **Beachten:** EL, Hilflosenentschädigung, Pflegebeiträge an AHV-/IV-Bezüger sind steuerfrei – nicht hier erfassen.
- **Beachten:** Renten aus 2. Säule/3a/Arbeitgeber/UVG gehören in Ziff. 3.2 (Code 134–137).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «AHV- / IV-Renten (100%) Person 1»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0050.md) `zh-wl-2025__c0050` – «AHV- und IV-Renten [ Ziffer 3.1]»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0053.md) `zh-wl-2025__c0053` – «Beihilfen, Arbeitslosenhilfen und Gemeindezuschüsse, welche Bezügern von AHV-, IV- und»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «3.2   Renten / Pensionen»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0053.md) `zh-wl-2025__c0053` – «ausgerichtet werden, sind nicht steuerbar.»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0050.md) `zh-wl-2025__c0050` – «Renten und Pensionen [ Ziffer 3.2]»

<a id="3-2-einkommen-vorsorge-renten"></a>
### Ziff. 3.2 – Renten / Pensionen (2. Säule, 3a, Arbeitgeber, UVG, Militärversicherung), Person 1 / 2 (Code 134/135 bzw. 136/137; Vorkolonnen 960–967)

- **Schlüssel:** `einkommen.vorsorge.renten` (Renten/Pensionen 2. Säule und Säule 3a) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Rentenbescheinigung Pensionskasse / Versicherer: Bruttorente (Betrag) und steuerbarer Anteil (Prozente)
- **Rein:** Rentenbescheinigung Pensionskasse/Versicherer → Bruttorente 2025 (Vorkolonne «Betrag») · Rentenbeginn und Eigenbeitragsanteil (nur für 80 %-Altfälle) · Bescheinigung SUVA/UVG-Versicherer, Militärversicherung, Arbeitgeber, 3a-Stiftung
- **Rechnen:** Hauptkolonne = Betrag × Prozente: Vorkolonnen 960/961 → 134, 962/963 → 135 (P1), 964/965 → 136, 966/967 → 137 (P2); i.d.R. 100 %
- **Regel:** Vorkolonne «Betrag» = Gesamtrente, Hauptkolonne = steuerbarer Teil. 2. Säule i.d.R. 100 % (80 % nur bei Rentenbeginn vor 1.1.1987 bzw. 1987–2001 mit Eigenbeitrag ≥ 20 %); Renten aus Säule 3a, vom Arbeitgeber und Militärversicherung 100 %; UVG-Renten 100 % (60 %/80 % nur Altfälle vor 1986).
- **Beachten:** 80 %: Rentenbeginn vor 1987 bzw. 1987–2001 mit Vorsorgeverhältnis schon Ende 1985 (Bund: 1986) und Eigenbeitrag ≥ 20 %.
- **Beachten:** UVG 60 % (Prämien allein selbst) bzw. 80 % (≥ 20 % selbst) nur bei Nichtberufsunfall vor 1986; AG, 3a, MV 100 %.
- **Beachten:** MV steuerfrei: Invaliden-/Hinterlassenenrenten mit Beginn vor 1994, Integritätsschadensrenten, Genugtuung.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «3.2 Renten / Pensionen»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0050.md) `zh-wl-2025__c0050` – «in allen übrigen Fällen:»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0051.md) `zh-wl-2025__c0051` – «Renten aus anerkannten Formen der gebundenen Selbstvorsorge (3. Säule a)»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0052.md) `zh-wl-2025__c0052` – «Bei nicht zu 100% steuerbaren Renten ist in den Vorkolonnen der Steuererklärung der»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0051.md) `zh-wl-2025__c0051` – «berufsunfalls ausgerichtet wird und die Prämien ausschliesslich vom Ver-»

<a id="3-2-leibrenten-einkommen-vorsorge-uebrige-renten"></a>
### Ziff. 3.2 (Leibrenten) – Leibrenten / Verpfründung (private, Versicherer, ausländisch) – Code 134–137

- **Schlüssel:** `einkommen.vorsorge.uebrige_renten` (Übrige Renten (Leibrenten, ausländische Renten, Militär-/Unfallversicherung)) · **Status:** ⚠️ strittig
- **Beleg → Feld:** Rentenbescheinigung Pensionskasse / Versicherung (2. Säule, 3a, Leibrente) → Steuerbescheinigung des Versicherers (steuerbarer Ertragsanteil) bzw. Leibrentenvertrag + ESTV-Berechnungssatz
- **Rein:** Steuerbescheinigung des Versicherers (Leibrentenversicherung) → steuerbarer Ertragsanteil · Private/ausländische Leibrente, Verpfründung: Leibrentenvertrag (Kopie) + ESTV-Berechnungssatz der Steuerperiode · Zahlungsnachweis erhaltene Rente 2025 → Gesamtbetrag (Vorkolonne «Betrag»)
- **Rechnen:** Vorkolonne = Gesamtrente; Hauptkolonne = Ertragsanteil lt. Versicherer bzw. Rente × Berechnungssatz / 100; «Prozente» leer. Bund: Art. 22 Abs. 3 DBG
- **Regel:** Gesamtbetrag in Vorkolonne «Betrag», steuerbarer Ertragsanteil in die Hauptkolonne; Kolonne «Prozente» leer lassen. Ertragsanteil: Bescheinigung des Versicherers bzw. Rente x ESTV-Berechnungssatz / 100. STRITTIG: StG § 22 Abs. 3 (Fassung 2025) nennt 40 %, WL 2025 den flexiblen Ertragsanteil – Fachperson entscheidet.
- **Beachten:** STRITTIG: StG § 22 Abs. 3 = 40 %, WL 2025 = flexibler Ertragsanteil (StHG Art. 72 → WL); Fachperson entscheidet.
- **Beachten:** Bund lit. b: Überschussleistungen 70 %; lit. c (ausländ. LRV, Leibrenten-/Verpfründungsvertrag): Rendite zehnj. BO + 0,5 Pp.
- **Beachten:** Bescheinigung bzw. Vertragskopie zwingend mit der Steuererklärung einreichen.
- **Bund:** Bund: Ertragsanteil nach Art. 22 Abs. 3 DBG (lit. a/b Leibrentenversicherungen mit Versichererbescheinigung; lit. c ausländische Leibrentenversicherungen sowie Leibrenten- und Verpfründungsverträge, Satz r + 0,5 Prozentpunkte).
- **Bemerkung:** Widerspruch Gesetz vs. Wegleitung: StG ZH § 22 Abs. 3 (zh-stg-2025, Nachtrag 127) = 40 Prozent; WL ZH 2025 (c0025, c0052) = flexibler Ertragsanteil seit 1.1.2025 (bisher pauschal 40 %). Rangfolge Gesetz > Wegleitung, aber StG-Fassung im Wiki möglicherweise nicht auf Stand. Praxis der Wegleitung (Bescheinigung des Versicherers) anwenden und Fachperson informieren. Gegenprobe Prüfung: StHG Art. 7 Abs. 2 (Fassung 2025) kennt den flexiblen Ertragsanteil; nach Art. 72 Abs. 2 StHG gilt Bundesrecht direkt, wenn das kantonale Recht widerspricht – das spricht für die Wegleitung (Versichererbescheinigung/ESTV-Satz). Endentscheid bleibt bei der Fachperson (status strittig).
- **Quellen:**
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0052.md) `zh-wl-2025__c0052` – «Leibrenten sowie Einkünfte aus Verpfründung»
  - [WL ZH 2025 S. 9](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0025.md) `zh-wl-2025__c0025` – «Ab dem 1.1.2025 wird der steuerbare Ertragsanteil flexibel an die Anlagebedingungen angepasst»
  - [StG ZH § 22](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-22.md) `zh-stg-2025__par-22` – «Leibrenten sowie Einkünfte aus Verpfründung sind zu 40 Prozent steuerbar.»
  - [StHG Art. 7](../../chunks/bund/2025/bund-sthg/bund-sthg__art-7-t3.md) `bund-sthg__art-7-t3` – «Leibrentenversicherungen sowie Leibrenten- und Verpfründungsverträge sind im Umfang ihres Ertragsanteils steuerbar»
  - [StHG Art. 72](../../chunks/bund/2025/bund-sthg/bund-sthg__art-72.md) `bund-sthg__art-72` – «Nach ihrem Inkrafttreten finden die Bestimmungen dieses Gesetzes direkt Anwendung, wenn ihnen das kantonale Steuerrecht widerspricht»
  - [DBG Art. 22](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-22-t3.md) `bund-dbg-2025__art-22-t3` – «Bei Überschussleistungen aus Leibrentenversicherungen, die dem VVG unterstehen, entspricht der Ertragsanteil 70 Prozent dieser Leistungen.»
  - [DBG Art. 22](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-22-t3.md) `bund-dbg-2025__art-22-t3` – «um 0,5 Prozentpunkte erhöhten annualisierten Rendite zehnjähriger Bundesobligationen (r)»
  - [DBG Art. 22](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-22-t2.md) `bund-dbg-2025__art-22-t2` – «Leibrentenversicherungen sowie Leibrenten- und Verpfründungsverträge sind im Umfang ihres Ertragsanteils steuerbar.»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0052.md) `zh-wl-2025__c0052` – «Berechnungsformel: Erhaltene Leibrente / Verpfründung x Berechnungssatz (in %)»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0052.md) `zh-wl-2025__c0052` – «bescheinigung ist zusammen mit der Steuererklärung einzureichen.»
  - [DBG Art. 22](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-22-t3.md) `bund-dbg-2025__art-22-t3` – «Bei Leistungen aus ausländischen Leibrentenversicherungen, aus Leibrenten- und aus Verpfründungsverträgen»

<a id="3-3-einkommen-ersatz-taggelder"></a>
### Ziff. 3.3 – Erwerbsausfallentschädigungen aus Arbeitslosenversicherung, direkt ausbezahlt (Code 140/141)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Arbeitslosenkasse (Jahresbetrag)
- **Rein:** Bescheinigung der Arbeitslosenkasse → Jahresbetrag 2025 direkt ausbezahlter Entschädigungen je Person
- **Rechnen:** Σ direkt von der Arbeitslosenkasse ausbezahlte Erwerbsausfallentschädigungen 2025 → Code 140 (P1) / 141 (P2); Kanton = Bund
- **Regel:** Nur direkt von der Arbeitslosenkasse ausbezahlte Entschädigungen hier; vom Arbeitgeber ausbezahlte Taggelder stehen bereits im Lohnausweis. Bescheinigungen beilegen.
- **Beachten:** Nur direkt ausbezahlte Entschädigungen; über den Arbeitgeber (Lohnausweis) abgerechnete nicht doppelt erfassen.
- **Beachten:** Bescheinigung beilegen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «3.3 Erwerbsausfallentschädigungen aus Arbeitslosenversicherung»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0054.md) `zh-wl-2025__c0054` – «Die entsprechenden Bescheinigungen sind beizulegen.»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «3.3: Direkt ausbezahlte Erwerbs»

<a id="3-4-einkommen-ersatz-taggelder"></a>
### Ziff. 3.4 – Taggelder KV/UV/IV/MV, EO und Mutterschaftsentschädigung, direkt ausbezahlt (Code 142/143)

- **Schlüssel:** `einkommen.ersatz.taggelder` (Erwerbsausfallentschädigungen (ALV, KV, UV, IV-Taggelder, EO, Mutterschaft)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Taggeldbescheinigung (ALV, Kranken-/Unfall-/IV-/Militärversicherung, EO/Mutterschaft) → Bescheinigung der Versicherung / Ausgleichskasse (Jahresbetrag)
- **Rein:** Taggeldabrechnung/Bescheinigung KV, UV, IV, MV → Jahresbetrag direkt ausbezahlter Taggelder · Bescheinigung Ausgleichskasse → EO-/Mutterschaftsentschädigung (direkt ausbezahlt)
- **Rechnen:** Σ direkt ausbezahlte Taggelder + EO/Mutterschaftsentschädigung (+ direkt ausbezahlte Familienzulagen) je Person → Code 142 (P1) / 143 (P2)
- **Regel:** Taggelder aus Kranken-, Unfall-, Invaliden- und Militärversicherung sowie EO/Mutterschaftsentschädigung sind steuerbar. Hier nur eintragen, wenn nicht im Lohnausweis enthalten; Bescheinigung verlangen und beilegen.
- **Beachten:** Nur wenn nicht im Lohnausweis bescheinigt und mit dem Lohn in Ziff. 1 übertragen.
- **Beachten:** Bescheinigung bei der Versicherungseinrichtung verlangen und beilegen.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «3.4 Kinder- und Familienzulagen, Mutterschaftsentschädigungen, Taggelder»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0055.md) `zh-wl-2025__c0055` – «Taggelder aus Kranken-, Unfall- und Invalidenversicherung, aus Militärversicherung sowie die»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «Person 1   Bescheinigung 142»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0055.md) `zh-wl-2025__c0055` – «eine Bescheinigung über diese Einkünfte und reichen Sie diese mit der Steuererklärung ein.»

<a id="3-4-einkommen-ersatz-familienzulagen"></a>
### Ziff. 3.4 – Kinder- und Familienzulagen, direkt von der Ausgleichskasse ausbezahlt (Code 142/143)

- **Schlüssel:** `einkommen.ersatz.familienzulagen` (Kinder- und Familienzulagen, die nicht im Lohnausweis enthalten sind) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der Familienausgleichskasse (nicht im Lohnausweis enthalten)
- **Rein:** Bescheinigung der Familienausgleichskasse → direkt ausbezahlte Kinder-/Familienzulagen 2025
- **Rechnen:** Σ direkt von der Ausgleichskasse ausbezahlte Kinder-/Familienzulagen → Code 142 (P1) / 143 (P2), zusammen mit Taggeldern
- **Regel:** Nur Zulagen eintragen, die nicht über den Lohnausweis abgerechnet wurden, sondern direkt von der Ausgleichskasse kamen.
- **Beachten:** Über den Arbeitgeber (Lohnausweis) ausbezahlte Zulagen sind bereits im Lohn Ziff. 1 – nicht doppelt.
- **Beachten:** Bescheinigung beilegen.
- **Quellen:**
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0055.md) `zh-wl-2025__c0055` – «von Ausgleichskassen direkt ausbezahlten Kinder- und Familienzulagen und Mutterschafts-»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «Person 1   Bescheinigung 142»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «3.4   Kinder- und Familienzulagen, Mutterschaftsentschädigungen, Taggelder»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0055.md) `zh-wl-2025__c0055` – «eine Bescheinigung über diese Einkünfte und reichen Sie diese mit der Steuererklärung ein.»

<a id="3-steuerfrei-info-steuerfreie-leistungen"></a>
### Ziff. 3 (steuerfrei) – Steuerfreie Unterstützungsleistungen (EL, Hilflosenentschädigung, Pflegebeiträge) – nicht deklarieren

- **Schlüssel:** `info.steuerfreie_leistungen` (Steuerfreie Leistungen (Ergänzungsleistungen, Hilflosenentschädigung, Überbrückungsleistungen – nur Angabe)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Verfügung/Jahresabrechnung Ergänzungsleistungen (EL) zur AHV/IV → Verfügung / Bescheid der Ausgleichskasse (nur zur Abgrenzung)
- **Rein:** Verfügung/Bescheid EL, Hilflosenentschädigung, Pflegebeiträge, Beihilfen, Gemeindezuschüsse → nicht übertragen (nur Abgrenzung)
- **Rechnen:** Kein Betrag in Ziff. 3 (nicht steuerbar); gilt für Unterstützungen an Bezüger von AHV-/IV-/UVG-Leistungen
- **Regel:** Ergänzungsleistungen, Hilflosenentschädigungen, Pflegebeiträge, Beihilfen, Arbeitslosenhilfen und Gemeindezuschüsse für Bezüger von AHV/IV/UVG-Leistungen sind nicht steuerbar und werden nicht als Einkommen eingesetzt.
- **Beachten:** Steuerfrei auch (MV): Invaliden-/Hinterlassenenrenten mit Beginn vor 1994, Integritätsschadensrenten, Genugtuung.
- **Beachten:** AHV-/IV-Renten selbst bleiben zu 100 % steuerbar (Ziff. 3.1).
- **Quellen:**
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0053.md) `zh-wl-2025__c0053` – «Beihilfen, Arbeitslosenhilfen und Gemeindezuschüsse, welche Bezügern von AHV-, IV- und»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0053.md) `zh-wl-2025__c0053` – «ausgerichtet werden, sind nicht steuerbar.»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0051.md) `zh-wl-2025__c0051` – «Invaliden- und Hinterlassenenrenten, die vor dem 1. Januar 1994 zu laufen»
  - [WL ZH 2025 S. 11](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0051.md) `zh-wl-2025__c0051` – «Integritätsschadensrenten und Genugtuungsleistungen»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «AHV- / IV-Renten (100%) Person 1»

<a id="4-1-einkommen-wertschriften"></a>
### Ziff. 4.1 – Ertrag aus Wertschriften, Guthaben und Lotterien (Code 150) – Total Bruttoertrag A + B laut Wertschriftenverzeichnis

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Wertschriftenverzeichnis (Form. 340) Total Bruttoertrag A + B (Code 150); Basis: Steuerauszug / Zinsausweise
- **Rein:** (e)Steuerauszug Bank → Bruttoerträge Kol. A/B und Steuerwerte 31.12.2025 (Import in Online-Steuererklärung möglich) · Zinsausweise Konti, Dividenden-/Fondsabrechnungen; Kursliste ESTV (steuerbare Werte Anlagefonds) · Krypto: Wallet-Kontoauszug per Ende Steuerperiode → Steuerwert (ESTV-Jahresendsteuerkurs) · Ausländ. Dividenden/Zinsen mit Quellensteuer-Anrechnung → Formular DA-1 (Total Bruttoertrag in Kol. B)
- **Rechnen:** Form. 340: Total Bruttoertrag 150 = Zwischentotal A 539 + B 542 → Ziff. 4.1; VSt-Anspruch 540 = 35 % × 539; Steuerwert 400 → Ziff. 30.1
- **Regel:** Brutto-Erträge aller Konti, Wertschriften, Fonds, Dividenden (inkl. thesaurierte Erträge, Gratisaktien) im WV erfassen; Total A + B nach Ziff. 4.1 übertragen. Ertrag aus Nutzniessung zu 100 %. Vermögen und Ertrag der Kinder (Jg. 2008 und jünger) gehören in dieses Verzeichnis.
- **Beachten:** Kol. A = mit VSt (CH-Zinsen > CHF 200, CH-Dividenden/Fonds); Kol. B = ohne VSt (Zins bis CHF 200, ausländische Titel).
- **Beachten:** Kinder Jg. 2008 und jünger beim Elternteil; Vorsorgeguthaben (2. Säule, 3a) nicht ins WV.
- **Beachten:** Thesaurierte Fondserträge und Gratisaktien (ab 1.1.2020) steuerbar; gesondert ausgewiesene Fonds-Kapitalgewinne (PV) frei.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «Ertrag aus Wertschriften, Guthaben und Lotterien Wertschriftenverzeichnis 150»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Total Bruttoertrag A + B 150»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0056.md) `zh-wl-2025__c0056` – «ist zu 100% einzutragen.»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Total Steuerwert   400»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Steuererklärung Seite 4, Ziffer 30.1»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Zwischentotal Bruttoerträge   539   542»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «35% von Total Bruttoertrag A   540»
  - [Formular 340 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0003.md) `zh-form-340-2025__c0003` – «1. Kundenguthaben deren Bruttozins CHF 200.– nicht übersteigt»
  - [Formular 340 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0003.md) `zh-form-340-2025__c0003` – «3. Ausländische Wertschriften aller Art»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0162.md) `zh-wl-2025__c0162` – «Dies gilt auch für Kundenguthaben mit einem Bruttozins von mehr als»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0154.md) `zh-wl-2025__c0154` – «minderjährigen Kinder des Jahrgangs 2008 und jüngeren sowie das Vermögen, an dem Sie»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0154.md) `zh-wl-2025__c0154` – «Leistungen steuerfrei und nicht im Wertschriftenverzeichnis aufzuführen.»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0166.md) `zh-wl-2025__c0166` – «Neben den ausgeschütteten sind auch zurückbehaltene (thesaurierte) Erträge steuerbar.»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0166.md) `zh-wl-2025__c0166` – «sie gesondert ausgewiesen werden und sich die Anteile im Privatvermögen befinden.»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0164.md) `zh-wl-2025__c0164` – «Erträge aus Gratisaktien sind seit dem 1.1.2020»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0153.md) `zh-wl-2025__c0153` – «Sie können diesen eSteuerauszug in die Online-»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0159.md) `zh-wl-2025__c0159` – «Für Bitcoin und weitere geläufige Kryptowährungen publiziert die ESTV einen Jahresendsteuer-»
  - [WL ZH 2025 S. 27](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0171.md) `zh-wl-2025__c0171` – «sind im Antragsformular DA-1 aufzufüh-»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0004.md) `zh-form-340-2025__c0004` – «Steuerwert am 31.12.2025»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0166.md) `zh-wl-2025__c0166` – «baren Werte der Kursliste der ESTV entnommen werden.»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0159.md) `zh-wl-2025__c0159` – «(Wallet), Stand per Ende der Steuerperiode, zu erfolgen.»
  - [WL ZH 2025 S. 27](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0171.md) `zh-wl-2025__c0171` – «wobei das Total Bruttoertrag unter «B, Werte ohne Verrech-»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Übertrag Bruttoertrag A in Kolonne Bruttoertrag B   +   539»

<a id="4-1-lotterie-einkommen-lotterie-gewinne"></a>
### Ziff. 4.1 (Lotterie) – Lotterie-/Grossspiel-/Sportwettengewinne (im Wertschriftenverzeichnis, Kolonne A/B)

- **Schlüssel:** `einkommen.lotterie_gewinne` (Lotterie-/Geldspielgewinne (steuerbarer Teil)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lotterie-/Lottogewinn-Bescheinigung (Swisslos, Casino, Online-Spielbank, Wettbewerbsgewinn) → Gewinnbescheinigung Lotteriegesellschaft / Bank / Auszahlungsabschnitt Post
- **Rein:** Gewinnbescheinigung Lotteriegesellschaft / Bank bzw. Auszahlungsabschnitt Post → Bruttogewinn (Original beilegen) · Kontoauszug Online-Spielbank → Gewinne und effektive Einsätze
- **Rechnen:** Grossspiele/Online-Spielbanken je Gewinn: max(0; Gewinn − Kanton 1’033’000 / Bund 1’070’400); Verkaufsförderung: Gewinn > Kanton 1’000 / Bund 1’100 → ganzer Gewinn
- **Regel:** Gewinne aus Grossspielen und Online-Spielbankenspielen sind bis CHF 1’033’000 (Staat) bzw. CHF 1’070’400 (Bund) steuerfrei; Gewinne aus Verkaufsförderungs-Lotterien bis CHF 1’000 (Staat) bzw. CHF 1’100 (Bund) steuerfrei, bei Überschreitung ganzer Gewinn steuerbar (Freigrenze). Einsatzkosten: siehe Ziff. 16.5.
- **Beachten:** Mit VSt → Kol. A; ausländ. Geldspiele und Naturaltreffer → Kol. B (Naturalgewinne: Freigrenze Kanton 1’000 / Bund 1’100).
- **Beachten:** 16.5: Einsatzkosten 5 %, max. Kanton 5’200 / Bund 5’400; Online-Spielbank eff. Einsätze, max. Kanton 25’800 / Bund 26’800
- **Limiten:**
  - Grossspielgewinne steuerfrei bis (CHF): Kanton **CHF 1'033'000 (Einzelne Gewinne aus bewilligten Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'033'000; Spielbankengewinne (Landspielbanken) und Kleinspiele sind generell steuerfrei.)** · Bund **CHF 1'070'400 (Einzelne Gewinne aus Grossspielen und Online-Spielbankenspielen steuerfrei bis CHF 1'070'400)**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'000 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei, sofern die Grenze von CHF 1'000 nicht überschritten wird.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'100)**
- **Bund:** Bund: Freibetrag Grossspiele CHF 1’070’400, Freigrenze Verkaufsförderung CHF 1’100.
- **Quellen:**
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0167.md) `zh-wl-2025__c0167` – «sind bis zu einem Betrag von CHF 1’033’000 bei»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0167.md) `zh-wl-2025__c0167` – «zu einem Betrag von CHF 1’000 (Staatssteuer) bzw. CHF 1’100 (Bundessteuer) steuerfrei»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0168.md) `zh-wl-2025__c0168` – «Gewinne aus ausländischen Spielbanken, Lotterien und Sportwetten sind steuerbar.»
  - [Formular 340 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0003.md) `zh-form-340-2025__c0003` – «4. Gewinne aus ausländischen Spielbanken, Lotterien und Sportwetten sowie Naturaltreffer»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0105.md) `zh-wl-2025__c0105` – «Von den steuerbaren Gewinnen aus nicht steuerfreien Geldspielen können 5%, jedoch höchs»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0105.md) `zh-wl-2025__c0105` – «tens CHF 5’200 (Staatssteuer) bzw. CHF 5’400 (Bundessteuer), als Einsatzkosten abgezogen»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0105.md) `zh-wl-2025__c0105` – «die effektiven Einsätze, maximal jedoch CHF 25’800 (Staatssteuer) bzw. CHF 26’800 (Bundes-»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.5 Weitere Abzüge (z.B. Beiträge an politische Parteien)»
  - [WL ZH 2025 S. 27](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0169.md) `zh-wl-2025__c0169` – «Natural- und Sachgewinne sind bis zu einem Betrag von CHF 1’000 (Staatssteuer) bzw.»

<a id="4-2-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. 4.2 – Davon aus qualifizierten Beteiligungen (Code 151) – Erträge aus Beteiligungen ≥ 10 %

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Wertschriftenverzeichnis: Ertrag-Total aus qualifizierten Beteiligungen (Code Q) – Bruttobetrag der Ausschüttung
- **Rein:** Steuerauszug / Dividendenabrechnung bzw. Ausschüttungsbescheinigung (nicht kotiert) → Bruttoausschüttung · Nachweis Beteiligungsquote (≥ 10 % Grund-/Stammkapital) → Code Q im WV · Formular «Qualifizierte Beteiligungen im Privatvermögen» → Teilbesteuerungsabzug Ziff. 16.5
- **Rechnen:** Σ Bruttoausschüttungen mit Code Q (Kol. A + B) → Code 151 («davon», bereits in 150); Teilbesteuerungsabzug Ziff. 16.5 (Code 284): Kanton 50 % / Bund 30 %
- **Regel:** Beteiligungen von mindestens 10 % mit Code Q kennzeichnen, Bruttoausschüttung ungekürzt in Kolonne A oder B erfassen und das Total nochmals in Ziff. 4.2 (Code 151) angeben (Teilbesteuerungsabzug siehe Ziff. 16.5).
- **Beachten:** Ziff. 4.2 nicht zusätzlich zu Ziff. 4.1 addieren (Davon-Position).
- **Beachten:** Q im Geschäftsvermögen: Ertrag in Ziff. 2 (HB A); soweit im WV aufgeführt, in HB A Code 1742 abziehen.
- **Beachten:** Gratis abgegebene Mitarbeiteraktien: kein Teilbesteuerungsabzug.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «4.2 Davon aus qualifizierten Beteiligungen»
  - [Formular 340 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0003.md) `zh-form-340-2025__c0003` – «qualifizierten Beteiligungen 151»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0165.md) `zh-wl-2025__c0165` – «Sie sind ungekürzt, d.h. mit dem Bruttobetrag der Ausschüttung,»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.5 Weitere Abzüge (z.B. Beiträge an politische Parteien)»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md) `zh-wl-2025__c0104` – «zug für qualifizierte Beteiligungen im Privatvermögen beträgt 50%»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md) `zh-wl-2025__c0104` – «qualifizierte Beteiligungen im Privatvermögen beträgt 30%»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md) `zh-wl-2025__c0104` – «Bei gratis abgegebenen Mitarbeiteraktien kann kein Abzug vorgenommen werden.»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Total Bruttoertrag A + B   150»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0163.md) `zh-wl-2025__c0163` – «Bei nicht kotierten Titeln ist stets die Bescheinigung über»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «2: Inklusive Erträge aus qualifizierten Beteiligungen im»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0041.md) `zh-wl-2025__c0041` – «soweit im Wertschriftenverzeichnis enthalten»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.5 Weitere Abzüge (z.B. Beiträge an politische Parteien)   Aufstellung   284»

<a id="5-1-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.1 – Unterhaltsbeiträge vom geschiedenen / getrennten Ehegatten (Code 160)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil bzw. Vereinbarung; Jahressumme der erhaltenen Zahlungen
- **Rein:** Scheidungsurteil / Trennungsvereinbarung → vereinbarter Unterhalt · Bank-/Zahlungsbelege → Jahressumme 2025 erhalten; Name/Adresse Alimentenzahler/in
- **Rechnen:** Σ 2025 erhaltene Unterhaltsbeiträge für die Person selbst (voll) → Code 160; Kanton = Bund
- **Regel:** Erhaltene Unterhaltsbeiträge für die Person selbst sind voll als Einkommen anzugeben (Name/Adresse des Zahlers eintragen).
- **Beachten:** Gilt für geschiedene, gerichtlich oder tatsächlich getrennt lebende Ehegatten/Partner.
- **Beachten:** Kinderalimente separat in Ziff. 5.2 (161); Gegenstück beim Zahler: Abzug Ziff. 13.1 (Code 254).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «Unterhaltsbeiträge vom geschiedenen / getrennten Ehegatten / Partn.»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0057.md) `zh-wl-2025__c0057` – «Unterhaltsbeiträge (Alimente), die den geschiedenen, gerichtlich oder tatsächlich getrennt»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «Name/Adresse Alimentenzahler/in   5.   Übrige Einkünfte und Gewinne»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «13.1 Unterhaltsbeiträge an den geschiedenen oder getrennt lebenden Ehegatten / Partn.   254»

<a id="5-2-einkommen-unterhaltsbeitraege"></a>
### Ziff. 5.2 – Unterhaltsbeiträge für minderjährige Kinder (bis Monat der Volljährigkeit) (Code 161)

- **Schlüssel:** `einkommen.unterhaltsbeitraege` (Erhaltene Unterhaltsbeiträge (Alimente) für sich und Kinder) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil, Alimenten-Bevorschussung; Zahlungen bis und mit Monat des 18. Geburtstags
- **Rein:** Scheidungsurteil / Unterhaltsvertrag → Kinderunterhalt je Kind · Zahlungsbelege bzw. Abrechnung Alimentenbevorschussung → Beträge bis Monat des 18. Geburtstags
- **Rechnen:** Σ je Kind: erhaltene Alimente + Bevorschussungen bis und mit Monat, in dem das Kind 18 wird → Code 161; Kanton = Bund
- **Regel:** Kinderalimente nur bis und mit dem Monat der Volljährigkeit deklarieren; Alimentenbevorschussungen gleichgestellt. Spätere Zahlungen nicht mehr als Einkommen.
- **Beachten:** Zahlungen nach dem Monat des 18. Geburtstags nicht mehr als Einkommen deklarieren.
- **Beachten:** Gilt auch für ledige Steuerpflichtige; Gegenstück beim Zahler: Abzug Ziff. 13.2 (Code 255).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «5.2 Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit)»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0057.md) `zh-wl-2025__c0057` – «Den Alimenten gleichgestellt sind Alimentenbevorschussungen.»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0057.md) `zh-wl-2025__c0057` – «Ehegatten oder ledige Steuerpflichtige für Kinder erhalten»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0057.md) `zh-wl-2025__c0057` – «dem das Kind das 18. Altersjahr erreicht»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «13.2 Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit)   255»

<a id="5-3-einkommen-erbschaften-unverteilt"></a>
### Ziff. 5.3 – Ertrag aus Geschäfts- und Korporationsanteilen / unverteilten Erbschaften (Code 162)

- **Schlüssel:** `einkommen.erbschaften_unverteilt` (Einkünfte aus unverteilten Erbschaften/Vermögensmassen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung (Erbengemeinschaft / Gesellschaftsanteil); Quote des Steuerpflichtigen
- **Rein:** Abrechnung Geschäfts-/Korporationsanteil → Ertrag und Beteiligungsquote · Erbschaft: Erbbescheinigung/Aufstellung Erbengemeinschaft → Erbquote, Erträge ab Folgetag des Todestags
- **Rechnen:** Geschäfts-/Korporationsanteil: Ertrag × Beteiligungsquote → Code 162; unverteilte Erbschaft: Erträge (Folgetag Todestag bis 31.12.) × Erbquote → WV (150) bzw. LV (188)
- **Regel:** Einkünfte aus Geschäfts- und Korporationsanteilen anteilmässig nach Beteiligungsquote. Unverteilte Erbschaften: Einkommen ab dem auf den Todestag folgenden Tag anteilmässig; Wertschriften-/Liegenschaftserträge gehören ins WV bzw. Liegenschaftenverzeichnis.
- **Beachten:** Erbschaftsvermögen anteilig zum Steuerwert 31.12. (WV/LV); Schulden und Schuldzinsen anteilig → Schuldenverzeichnis.
- **Beachten:** Aufstellung beilegen: Erblasser (Todesdatum), Erben mit Quoten, Vermächtnisse, Werte/Erträge, Kosten, Schulden.
- **Beachten:** Erbengemeinschaft wird nicht separat besteuert; jeder Erbe nach seiner Erbquote.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «Ertrag aus Geschäfts- und Korporationsanteilen Aufstellung 162»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0058.md) `zh-wl-2025__c0058` – «Einkünfte aus Geschäfts- und Korporationsanteilen sind von den Inhabern anteilmässig ent-»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0149.md) `zh-wl-2025__c0149` – «Das Einkommen aus unverteilten Erb-»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0150.md) `zh-wl-2025__c0150` – «Die Schulden und Schuldzinsen der unverteilten Erbschaft sind anteilmässig in der Steuer-»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0151.md) `zh-wl-2025__c0151` – «Namen, Adressen und Erbquoten sämtlicher Erben»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0149.md) `zh-wl-2025__c0149` – «Erbengemeinschaften werden nicht separat besteuert.»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0149.md) `zh-wl-2025__c0149` – «Zu deklarieren sind die Einkünfte, welche ab dem auf den Todestag folgenden Tag bis zum»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0149.md) `zh-wl-2025__c0149` – «Wertschriften und Guthaben sind im Wertschriftenverzeichnis aufzuführen.»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0149.md) `zh-wl-2025__c0149` – «Erträge aus Liegenschaften sowie die angefallenen Unterhalts- und Ver-»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0150.md) `zh-wl-2025__c0150` – «Das Vermögen aus unverteilten Erbschaften ist mit dem per 31.12. gültigen Steuerwert an-»

<a id="5-4-einkommen-uebrige"></a>
### Ziff. 5.4 – Weitere Einkünfte, nähere Bezeichnung (Code 163)

- **Schlüssel:** `einkommen.uebrige` (Übrige Einkünfte (Provisionen, Trinkgelder, Mitarbeiterbeteiligungen, Lizenzen …)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung (z. B. im Lohnausweis nicht ausgewiesene Trinkgelder, Renten bei Tod/Nachteilen, Bundesbeiträge Prüfungskurse)
- **Rein:** Aufstellung/Belege: im Lohnausweis nicht ausgewiesene Trinkgelder, wiederkehrende Zahlungen bei Tod oder bleibenden Nachteilen · Bestätigung Bundesbeitrag an vorbereitende Kurse auf eidg. Prüfungen + effektive Weiterbildungskosten
- **Rechnen:** Σ übrige steuerbare Einkünfte inkl. Naturalbezüge → Code 163; Bundesbeitrag nur soweit > geltend gemachte effektive Weiterbildungskosten
- **Regel:** Auffangzeile für alle weiteren steuerbaren Einkünfte inkl. Naturalbezüge; Bundesbeiträge an Prüfungsvorbereitungskurse nur soweit sie die effektiven Weiterbildungskosten übersteigen.
- **Beachten:** Grundsätzlich alle wiederkehrenden und einmaligen Einkünfte steuerbar; Ausnahmen nur gesetzlich steuerfreie.
- **Beachten:** Bei Unsicherheit über die Steuerbarkeit: zuständiges Gemeindesteueramt.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «Weitere Einkünfte, nähere Bezeichnung:»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0058.md) `zh-wl-2025__c0058` – «Bitte beachten Sie, dass grundsätzlich alle wiederkehrenden und einmaligen Einkünfte, mit»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0058.md) `zh-wl-2025__c0058` – «wiederkehrende Zahlungen bei Tod oder für bleibende körperliche oder gesundheitliche Nach-»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0058.md) `zh-wl-2025__c0058` – «effektiven berufsorientierten Aus- und Weiterbildungskosten übersteigen.»

<a id="5-5-einkommen-kapitalabfindung-wiederkehrend"></a>
### Ziff. 5.5 – Kapitalabfindungen für wiederkehrende Leistungen (Code 164)

- **Schlüssel:** `einkommen.kapitalabfindung_wiederkehrend` (Kapitalabfindungen für wiederkehrende Leistungen (Rentensatz)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bescheinigung der auszahlenden Stelle (Betrag und Anzahl Monate)
- **Rein:** Bescheinigung/Abrechnung der auszahlenden Stelle → Abfindungsbetrag und abgegoltene Anzahl Monate
- **Rechnen:** Abfindung → Code 164; Anzahl Monate → Vorkolonne (1641); Satzbestimmung zum Betrag der jährlichen Leistung
- **Regel:** Die Abfindung wird zur Satzbestimmung auf den Betrag der jährlichen Leistung umgerechnet; Anzahl Monate in der Vorkolonne angeben. Kapitalleistungen aus Vorsorge gehören NICHT hierher, sondern in Ziff. 40.
- **Beachten:** Kapitalleistungen aus Vorsorge nicht hier → Seite 4, Ziff. 40.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «Kapitalabfindungen für wiederkehrende Leistungen»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0059.md) `zh-wl-2025__c0059` – «Diese werden bei der Ermittlung des Steuersatzes zu dem Betrag eingesetzt, welcher der»

<a id="6-einkommen-liegenschaften-mietertrag"></a>
### Ziff. 6 – Nettoertrag aus Liegenschaften (Code 188) – Übertrag aus Liegenschaftenverzeichnis

- **Schlüssel:** `einkommen.liegenschaften.mietertrag` (Mietertrag/übrige Liegenschaftserträge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung), Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Liegenschaftenverzeichnis (Form. 350) Seite 2: Nettoertrag aus Liegenschaften (Code 3953)
- **Rein:** Liegenschaftenbewertung Gemeindesteueramt (Weisung ZStB 21.1) → Eigenmietwert · Mieterspiegel / Verwaltungsabrechnung → Miet- und Pachtzinse (ohne Entschädigungen Heizung/Warmwasser/Treppenhausreinigung) · Rechnungen Unterhalt, Versicherungsprämien, Drittverwaltung → effektive Kosten (Aufstellung) · Baurechtsvertrag/-zinsbelege → Baurechtszinsen (Aufstellung)
- **Rechnen:** Je Liegenschaft: Erträge 5701 + 5711 = 5721 − Unterhalt pauschal 5731 bzw. effektiv 5741 = 5751; Σ 5751… + 578 = 3953 → Code 188
- **Regel:** Erträge (Eigenmietwert, Mietzinsen) abzüglich Unterhalts- und Verwaltungskosten (pauschal oder effektiv) je Liegenschaft im Form. 350 berechnen; nur der Nettobetrag kommt in Ziff. 6. Unterhaltskosten sind hier bereits abgezogen (kein Doppelabzug in Ziff. 16).
- **Beachten:** Pauschale Kanton 20 % / Bund 10 % (Gebäude ≤ 10 J. bei Periodenbeginn) bzw. 20 %; nicht bei vorwiegend Geschäftsnutzung.
- **Beachten:** EMW: EFH 3,50 % / StWE 4,25 % des Land- und Zeitbauwerts; eigene Wohnung im eigenen MFH 70 % der Marktmiete.
- **Beachten:** Mit Pauschale keine weiteren Abzüge ausser Baurechtszinsen; Wohnrecht/Nutzniessung: EMW 100 % beim Berechtigten.
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **20 % (Pauschalabzug für Unterhalts- und Verwaltungskosten von Liegenschaften des Privatvermögens: 20 % des Brutto-Mietertrags bzw. Mietwerts; Wahl pro Liegenschaft und Steuerperiode; nicht bei vorwiegend geschäftlich genutzten Liegenschaften.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Gleicher Pauschalsatz unabhängig vom Gebäudealter: 20 % des Brutto-Mietertrags bzw. Mietwerts.)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «6. Nettoertrag aus Liegenschaften Liegenschaftenverzeichnis 188»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0004.md) `zh-form-350__c0004` – «Nettoertrag aus Liegenschaften 3953»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0059.md) `zh-wl-2025__c0059` – «Erträge aus Liegenschaften sowie die Unterhaltskosten sind im Formular»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0003.md) `zh-form-350__c0003` – «Liegenschaftenerträge und Unterhaltskosten»
  - [WL ZH 2025 S. 29](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0185.md) `zh-wl-2025__c0185` – «reinigung, soweit diese die tatsächlichen Aufwendungen nicht übersteigen) und beträgt 20%»
  - [WL ZH 2025 S. 29](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0185.md) `zh-wl-2025__c0185` – «unten) keine weiteren Abzüge geltend gemacht werden.»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0184.md) `zh-wl-2025__c0184` – «Ein Pauschalabzug ist jedoch nicht zulässig, wenn die Liegen-»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0178.md) `zh-wl-2025__c0178` – «Für Einfamilienhäuser: 3,50% des Land- und Zeitbauwertes»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0179.md) `zh-wl-2025__c0179` – «Für Stockwerkeigentum: 4,25% des Land- und Zeitbauwertanteils»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0006.md) `zh-form-350__c0006` – «selbst genutzten Wohnung im Mehrfamilien- und Geschäftshaus (ohne Stockwerkeigentum) sind 70% des Mietzinses einzusetzen»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0183.md) `zh-wl-2025__c0183` – «wohnrechts- bzw. nutzniessungsberechtigte Person zu versteuern.»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0183.md) `zh-wl-2025__c0183` – «ist der Eigenmietwert zu 100% durch die»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0177.md) `zh-wl-2025__c0177` – «gestützte Liegenschaftenbewertung wird Ihnen vom Gemeindesteueramt der Liegenschaften-»
  - [WL ZH 2025 S. 29](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0194.md) `zh-wl-2025__c0194` – «Zusätzlich zu den Unterhalts- und Verwaltungskosten können (bei der Staats- und direkten»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0006.md) `zh-form-350__c0006` – «ohne Entschädigungen der Mieter für Heizung, Warmwasser und Treppenhausreinigung»

<a id="7-berechnung-total"></a>
### Ziff. 7 – Total der Einkünfte (Code 199)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 1–6)
- **Rein:** Übertrag aus Ziff. 1–6 (Seite 2)
- **Rechnen:** Σ Hauptkolonnen Ziff. 1–6: 100–103, 120–123, 130/131, 134–137, 140–143, 150, 160–164, 188 (ohne 151 «davon», Vorkolonnen 960–967, 1641) = 199 → Ziff. 19
- **Regel:** Rechenzeile: Übertrag auf Seite 3, Ziffer 19.
- **Beachten:** Ziff. 1–7 einspaltig; Ziff. 19 je Kolonne Staat/Bund – Staat-Korrekturen z. B. via Ziff. 16.5 (Kolonne Staatssteuer).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «7. Total der Einkünfte, zu übertragen auf Seite 3, Ziffer 19»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Haupterwerb Person 1 Lohnausweis»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0004.md) `zh-form-300-2025__c0004` – «Person 2 bzw. Aufstellung 123»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «3.1   AHV- / IV-Renten (100%) Person 1   AHV   IV   130»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «Person 2   966 113211   967 111 137»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0005.md) `zh-form-300-2025__c0005` – «Person 2   Bescheinigung   143»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «19.   Total der Einkünfte   Übertrag von Seite 2, Ziffer 7   199»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0044.md) `zh-wl-2025__c0044` – «Für die Staatssteuer ist der bei der Einkommenssteuer freizustellende Teil des Grundstückgewinns in Ziffer 16.5»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «5.5 Kapitalabfindungen für wiederkehrende Leistungen   1641 1 1 Monate 164»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «6.  Nettoertrag aus Liegenschaften   Liegenschaftenverzeichnis 188»

## Abzüge

<a id="11-1-11-2-berechnung-total"></a>
### Ziff. 11.1 / 11.2 – Berufsauslagen bei unselbständiger Erwerbstätigkeit, Person 1 (Code 220) / Person 2 (Code 240)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Formular 360 Ziff. 6 «Total der Berufsauslagen» (Staats- und Bundessteuer getrennte Spalten)
- **Rein:** Form. 360 «Berufsauslagen» je Person → Ziff. 6 Total: P1 Code 220 → Ziff. 11.1, P2 Code 240 → Ziff. 11.2 · Lohnausweis → Ziff. 11 Nettolohn (Basis Pauschale), Felder F/G, Spesen · ÖV-Abo, km-Nachweis/Begründung Auto, Arbeitstage, Mietvertrag Zimmer (Wochenaufenthalt)
- **Rechnen:** Fahrkosten 201 Abo + 202 Velo + 204 Auto/Motorrad = Zwischentotal 205 (max. Kanton 5’200 / Bund 3’300) + Verpflegung 206/208/210 + übrige 212|213 + Wochenaufenthalt 2860 + Nebenerwerb 216|217 = 220 → Ziff. 11.1; P2: 221 + 222 + 224 = 225 … = 240 → Ziff. 11.2; bei Auto/Motorrad (weisses Kontrollschild) Begründung Ziff. 7 ankreuzen (P1 2041–2044 / P2 2241–2244)
- **Regel:** Pro Person Formular «Berufsauslagen» (Form. 360) ausfüllen und beilegen; Total in Ziff. 11.1/11.2 übertragen. Staats- und Bundessteuer-Spalte können abweichen (Fahrkosten-Plafond). Vom Arbeitgeber vergütete Berufsauslagen sind nicht abziehbar.
- **Beachten:** Vom Arbeitgeber vergütete Auslagen nicht abziehbar; mit Geschäftsfahrzeug keine Fahrkosten.
- **Beachten:** Auto 70 Rp./km nur ausnahmsweise (kein ÖV, > 1 Std. Zeitersparnis, AG-Verlangen, Krankheit): Begründung Ziff. 7.
- **Beachten:** Übrige Kosten pauschal 3 % Nettolohn (min. 2’000, max. 4’000) bzw. effektiv mit vollem Nachweis.
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, bei der Staatssteuer höchstens CHF 5'200 pro Jahr (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **3 % (Übrige Berufsauslagen (Berufskleider, Werkzeuge inkl. EDV, Fachliteratur, privates Arbeitszimmer, Berufsverbandsbeiträge): 3 % des Nettolohns, mind. CHF 2'000, höchstens CHF 4'000. Nachweis höherer Kosten möglich (volle Belegpflicht).)** · Bund **3 % (Übrige Berufskosten (Art. 26 Abs. 1 lit. c DBG): Pauschale 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; anstelle der Pauschale ist der Nachweis höherer tatsächlicher übriger Berufskosten möglich. Fahrkosten (lit. a, max. 3'300 gemäss DBG 2025; WL 2a 2025 nennt 3'200 – Widerspruch siehe berufskosten.fahrkosten.max) und Verpflegung (lit. b) werden zusätzlich abgezogen. Bei Teilzeit/Teiljahr angemessen kürzen.)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **CHF 2'000 (Minimum der Pauschale für übrige Berufsauslagen: CHF 2'000.)** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 4'000 (Maximum der Pauschale für übrige Berufsauslagen: CHF 4'000.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.70 (Privatauto nur ausnahmsweise (kein öV, Zeitersparnis über 1 Std., Einsatz auf Verlangen des Arbeitgebers, Krankheit/Gebrechlichkeit): CHF 0.70 pro Fahrkilometer.)** · Bund **CHF 0.70 (Privatauto: Abzug pro Fahrkilometer CHF 0.70, nur wenn kein öffentliches Verkehrsmittel verfügbar/zumutbar (Steuerjahr 2025))**
- **Bund:** Bundessteuer-Spalte separat (Fahrkostenplafond CHF 3’300 statt CHF 5’200).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «11.1 Person 1 Berufsauslagen 220»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0060.md) `zh-wl-2025__c0060` – «Formular «Berufsauslagen» beizulegen und können ihre Berufsauslagen, soweit sie nicht vom»
  - [LS 631.33 (bis 2025) S. 3–4](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0007.md) `zh-pauschalierung-berufsauslagen-2025__c0007` – «Soweit Berufsauslagen vom Arbeitgeber vergütet werden, steht»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0061.md) `zh-wl-2025__c0061` – «▸ max. CHF 5'200   ▸ max. CHF 3'300»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0061.md) `zh-wl-2025__c0061` – «pro Arbeitstag CHF 7.50 / im Jahr CHF 1’600   206»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0061.md) `zh-wl-2025__c0061` – «pro Arbeitstag CHF 15 / im Jahr CHF 3’200   208»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0061.md) `zh-wl-2025__c0061` – «pauschal   3% des Nettolohnes gem. Lohnausweis, mind. CHF 2’000, höchstens CHF 4’000»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0069.md) `zh-wl-2025__c0069` – «Mehrkosten bei auswärtigem Wochenaufenthalt (gemäss Aufstellung, siehe Wegleitung)»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0069.md) `zh-wl-2025__c0069` – «Total der Berufsauslagen   220»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «Bei der Staatssteuer ist der Fahrkostenabzug auf CHF 5’200 beschränkt.»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «Bei der direkten Bundessteuer ist der Fahrkostenabzug auf CHF 3’300 beschränkt.»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «Arbeitnehmende, die über ein Geschäftsfahrzeug verfügen, können keine Fahrkosten in Ab-»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «11.2 Person 2   Berufsauslagen   240»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0004.md) `zh-form-360-2025__c0004` – «bzw. effektiv   gemäss Aufstellung   213»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0004.md) `zh-form-360-2025__c0004` – «Mehrkosten bei auswärtigem Wochenaufenthalt (gemäss Aufstellung, siehe Wegleitung)   2860»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0010.md) `zh-form-360-2025__c0010` – «Total der Berufsauslagen   240»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0064.md) `zh-wl-2025__c0064` – «Die Kosten für das private Motorfahrzeug können nur ausnahmsweise geltend gemacht»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «Zeitersparnis von über 1 Stunde bei Benützung des privaten Motorfahrzeuges   2042»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0032.md) `zh-wl-2025__c0032` – «Kantinenverpflegung / Lunch-Checks»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0002.md) `zh-form-360-2025__c0002` – «Zwischentotal   205  3211»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0007.md) `zh-form-360-2025__c0007` – «Zwischentotal   225  3211»

<a id="12-abzug-schuldzinsen"></a>
### Ziff. 12 – Schuldzinsen (Code 250)

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen) → Schuldenverzeichnis (Form. 355) Total private Schuldzinsen (Code 3201); Zinsausweis/Hypothekarbestätigung per 31.12.
- **Rein:** Zinsausweis Bank / Hypothekarbestätigung → Schuldzinsen 2025 und Schuld per 31.12. · Privatdarlehen: Vertrag + Zinsbelege (Name/Adresse Gläubiger) · Form. 355 → Total private Schuldzinsen (3201) → Ziff. 12; Total Privatschulden (3200) → Ziff. 34
- **Rechnen:** min(Σ private Schuldzinsen 2025; Bruttoertrag bewegl. + unbewegl. Privatvermögen inkl. EMW + 50’000) → Code 250 (Spalten Staat/Bund; Regel gleich)
- **Regel:** Private Schuldzinsen sind abziehbar bis zur Höhe der steuerbaren Vermögenserträge (inkl. Eigenmietwert) plus CHF 50’000. Amortisationen und Leasingraten sind nicht abziehbar. Baurechtszinsen gehören zu den Liegenschaftskosten (Form. 350), nicht hierher.
- **Beachten:** Nicht abziehbar: Amortisationen, Leasingraten (inkl. Zinsanteile); Geschäftsschuldzinsen bereits in Ziff. 2.
- **Beachten:** Baurechtszinsen → Liegenschaftenverzeichnis (Unterhaltskosten), fallen nicht unter die Begrenzung.
- **Beachten:** Bund: kein Abzug für Zinsen auf Darlehen der eigenen Kapitalgesellschaft zu nicht drittüblichen Bedingungen.
- **Bund:** Gleich: Art. 33 Abs. 1 lit. a DBG (Vermögenserträge + CHF 50’000).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «12. Schuldzinsen (soweit nicht schon unter Ziff. 2 abgezogen) Schuldenverzeichnis 250»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0074.md) `zh-wl-2025__c0074` – «mögen (inkl. Eigenmietwert) und weiterer CHF 50’000 nicht übersteigen.»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0073.md) `zh-wl-2025__c0073` – «abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t1.md) `zh-stg-2025__par-31-t1` – «die privaten Schuldzinsen im Umfang der nach den §§ 20, 20 a und 21 steuerbaren Vermögenserträge und weiterer Fr. 50 000»
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0002.md) `zh-form-355__c0002` – «Total Privatschulden / private Schuldzinsen   3200 / 3201»
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0002.md) `zh-form-355__c0002` – «Steuererklärung Seite 4, Ziffer 34   Steuererklärung Seite 3, Ziffer 12»
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0001.md) `zh-form-355__c0001` – «Name, Vorname und Adresse des Gläubigers»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0074.md) `zh-wl-2025__c0074` – «Baurechtszinsen sind bei den Liegenschaftenunterhaltskosten geltend zu machen»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «Nicht abzugsfähig sind Schuldzinsen für Darlehen, die eine Kapitalgesellschaft einer an ihrem Kapital massgeblich beteiligten»

<a id="13-1-abzug-unterhaltsbeitraege"></a>
### Ziff. 13.1 – Unterhaltsbeiträge an geschiedenen / getrennt lebenden Ehegatten (Code 254)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Scheidungs-/Trennungsurteil + Zahlungsnachweise (Jahressumme)
- **Rein:** Scheidungs-/Trennungsurteil bzw. Vereinbarung → Unterhalt für den Ehegatten persönlich · Bank-/Zahlungsbelege → Σ 2025 effektiv bezahlte Beiträge (Einreichung auf Verlangen; im Zweifel beilegen, vgl. Formularhinweis unter Ziff. 13.3)
- **Rechnen:** Σ 2025 bezahlte periodische Unterhaltsbeiträge an geschiedenen/getrennten Ehegatten → voll (Code 254; Kanton = Bund)
- **Regel:** Für den Ehegatten persönlich bestimmte Beiträge voll abziehbar. Zahlungsnachweise: Die WL nennt für 13.1/13.2 keine Beilagepflicht (Belege nur, wenn ausdrücklich verlangt). Der Formularhinweis «sämtliche Zahlungsnachweise» steht unter Ziff. 13.3 und wird in der WL auf Leibrenten/Verpfründungen bezogen. Der Bezug auf 13.1/13.2 ist nicht eindeutig (raw/zh/2025/zh-form-300-2025.pdf S. 3) → Nachweise auf Verlangen, im Zweifel beilegen, Fachperson entscheidet. Der Empfänger deklariert die Beiträge in Ziff. 5.1.
- **Beachten:** Empfänger versteuert sie in Ziff. 5.1 (Korrespondenzprinzip)
- **Beachten:** Nur periodische Beiträge: Kapitalabfindung gilt als Schuldentilgung, nicht abziehbar; Naturalleistungen (Miete, KK-Prämien, Schuldzinsen) gleichgestellt. Fundstelle nur Bundespraxis (KS 30 Ziff. 14.1.2, WL 2a); WL ZH 2025 äussert sich nicht, eine ZH-Abweichung ist nicht belegt.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «13.1 Unterhaltsbeiträge an den geschiedenen oder getrennt lebenden Ehegatten / Partn. 254»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0075.md) `zh-wl-2025__c0075` – «Ehegatten persönlich bestimmt sind, können voll abgezogen werden.»
  - [WL ZH 2025 S. 12](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0057.md) `zh-wl-2025__c0057` – «lebenden Ehegatten persönlich zukommen, sind von diesen als Einkommen anzugeben.»
  - [KS 30 S. 30–31](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0094.md) `bund-ks-30__c0094` – «Aus dem hier geltenden Korrespondenzprinzip ergibt»
  - [KS 30 S. 30–31](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0095.md) `bund-ks-30__c0095` – «Infolgedessen kann der als Kapitalleistung gezahlte Betrag zum Unterhalt des»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0051.md) `bund-wl-2a-2025__c0051` – «Den Alimenten gleichgesetzt sind Naturalleistungen wie Miete,»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0051.md) `bund-wl-2a-2025__c0051` – «Unterhaltsbeiträge, die in Form einer Kapitalabfindung erbracht»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «Mit der Steuererklärung 2025 sind sämtliche Zahlungsnachweise einzureichen.»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0080.md) `zh-wl-2025__c0080` – «Leibrenten und Verpfründungen einzureichen (insbesondere Leibrenten- bzw.»
  - [WL ZH 2025 S. 32](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0207.md) `zh-wl-2025__c0207` – «Die Belege zu den Aufstellungen und Formularen sind nur dann zusammen mit der Steuererklärung einzureichen, wenn dies ausdrücklich verlangt ist.»

<a id="13-2-abzug-unterhaltsbeitraege"></a>
### Ziff. 13.2 – Unterhaltsbeiträge für minderjährige Kinder (Code 255)

- **Schlüssel:** `abzug.unterhaltsbeitraege` (Bezahlte Unterhaltsbeiträge (Alimente) und Renten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Unterhaltsvereinbarung / Scheidungsurteil / Zahlungsnachweis Alimente (bezahlte und erhaltene Unterhaltsbeiträge) → Urteil/Vereinbarung + Zahlungsnachweise bis und mit Monat des 18. Geburtstags
- **Rein:** Urteil/Unterhaltsvertrag → Kinderalimente je Kind · Zahlungsbelege mit Monatszuordnung → bezahlt bis und mit Monat des 18. Geburtstags (Einreichung auf Verlangen; im Zweifel beilegen, vgl. Formularhinweis unter Ziff. 13.3)
- **Rechnen:** Σ bezahlte Kinderalimente je Kind bis und mit dem Monat, in dem das Kind 18 wird (Code 255; Kanton = Bund)
- **Regel:** Abziehbar bis und mit dem Monat der Volljährigkeit; danach steht dem Zahlenden stattdessen der Kinderabzug zu (Ziff. 24.1). Spätere Zahlungen nicht mehr abziehbar.
- **Beachten:** Ab Folgemonat kein Abzug; stattdessen Kinderabzug Ziff. 24.1 (Erstausbildung, Unterhalt zur Hauptsache)
- **Beachten:** Wer Alimente für das minderjährige Kind leistet, erhält keinen Kinderabzug für dieses Kind
- **Beachten:** Bund: nur familienrechtlich geschuldete, effektiv bezahlte Alimente; freiwillige nicht
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «13.2 Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit)»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0076.md) `zh-wl-2025__c0076` – «werden, in dem das Kind das 18. Altersjahr erreicht.»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0076.md) `zh-wl-2025__c0076` – «an Stelle des Abzuges steht dann dem Zahlenden der Kinderabzug zu»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0077.md) `zh-wl-2025__c0077` – «(siehe Ziffer 24.1).»
  - [WL ZH 2025 S. 20](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0129.md) `zh-wl-2025__c0129` – «geltend machen, wenn Sie Unterhaltsbeiträge leisten und damit für den Unterhalt des Kindes zur Hauptsache aufkommen.»
  - [WL ZH 2025 S. 20](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0129.md) `zh-wl-2025__c0129` – «können Sie keinen Kinderabzug geltend machen;»
  - [KS 30 S. 32](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0100.md) `bund-ks-30__c0100` – «jedoch nicht für freiwillig erbrachte Alimente»
  - [KS 30 S. 32](../../chunks/bund/dauernd/bund-ks-30/bund-ks-30__c0100.md) `bund-ks-30__c0100` – «müssen sie effek- tiv bezahlt worden sein.»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «Mit der Steuererklärung 2025 sind sämtliche Zahlungsnachweise einzureichen.»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0080.md) `zh-wl-2025__c0080` – «Leibrenten und Verpfründungen einzureichen (insbesondere Leibrenten- bzw.»
  - [WL ZH 2025 S. 32](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0207.md) `zh-wl-2025__c0207` – «Die Belege zu den Aufstellungen und Formularen sind nur dann zusammen mit der Steuererklärung einzureichen, wenn dies ausdrücklich verlangt ist.»

<a id="13-3-abzug-uebrige"></a>
### Ziff. 13.3 – Rentenleistungen / dauernde Lasten, abzugsfähig: Ertragsanteil (Code 256)

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ⚠️ strittig
- **Beleg → Feld:** – → Leibrentenvertrag / Verpfründungsvertrag; Zahlungsnachweise
- **Rein:** Leibrenten-/Verpfründungsvertrag → vereinbarte Leistung · Überweisungsbelege → Σ 2025 bezahlte Rente (Vorkolonne Code 2561) · ESTV-Berechnungssatz der Steuerperiode (www.estv.admin.ch)
- **Rechnen:** Code 256 = bezahlte Leibrente/Verpfründung (Vorkolonne 2561) × ESTV-Berechnungssatz (in %); gem. WL Kanton = Bund
- **Regel:** Bezahlte Leibrenten und Verpfründungen: abziehbar ist der Ertragsanteil = bezahlte Rente x ESTV-Berechnungssatz / 100; Betrag der Leistung in Vorkolonne, abzugsfähiger Ertragsanteil in Hauptkolonne. STRITTIG für die Staatssteuer: StG § 31 Abs. 1 lit. b nennt 40 % der bezahlten Leibrenten.
- **Beachten:** STRITTIG Kanton: StG § 31 Abs. 1 lit. b = 40 Prozent der bezahlten Leibrenten; WL = ESTV-Satz → Fachperson
- **Beachten:** WL «Neu 2025»: bisher pauschal 40 % Ertragsanteil, ab 1.1.2025 flexibel an Anlagebedingungen angepasst
- **Beachten:** Beweiskräftige Belege einreichen (Leibrenten-/Verpfründungsvertrag, Überweisungsbelege)
- **Bund:** Bund: Art. 33 Abs. 1 lit. b DBG – Ertragsanteil nach Art. 22 Abs. 3 lit. c DBG.
- **Bemerkung:** Wie Ziff. 3.2 (Leibrenten): StG ZH § 31 Abs. 1 lit. b (zh-stg-2025) = 40 Prozent der bezahlten Leibrenten; WL 2025 (c0078) = Ertragsanteil nach ESTV-Satz. Bund (bund-dbg-2025__art-33-t1): «der Ertragsanteil nach Artikel 22 Absatz 3 Buchstabe c». Fachperson entscheidet für die Staatssteuer. Gegenprobe Prüfung: Bundesrecht (Art. 33 Abs. 1 lit. b DBG) und StHG gelten nach Art. 72 Abs. 2 StHG direkt, falls kantonales Recht widerspricht; Fachperson entscheidet.
- **Quellen:**
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0078.md) `zh-wl-2025__c0078` – «Abzugsfähig ist der Ertragsanteil der bezahlten Leibrenten und Verpfründungen.»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t1.md) `zh-stg-2025__par-31-t1` – «die dauernden Lasten sowie 40 Prozent der bezahlten Leibrenten»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «der Ertragsanteil nach Artikel 22 Absatz 3 Buchstabe c der Leistungen aus Leibrenten- und aus Verpfründungsverträgen»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «13.3 Rentenleistungen CHF 2561»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «abzugsfähig: Ertragsanteil 256»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0079.md) `zh-wl-2025__c0079` – «Berechnungsformel: Bezahlte Leibrente / Verpfründung x Berechnungssatz (in %)»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0080.md) `zh-wl-2025__c0080` – «Leibrenten und Verpfründungen einzureichen (insbesondere Leibrenten- bzw.»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0052.md) `bund-wl-2a-2025__c0052` – «Bezahlte Leibrente / Verpfründung x Berechnungssatz (in %)»
  - [WL ZH 2025 S. 9](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0025.md) `zh-wl-2025__c0025` – «Bei Leibrenten wurde bisher ein Anteil von 40% als pauschaler Ertragsanteil besteuert.»
  - [WL ZH 2025 S. 9](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0025.md) `zh-wl-2025__c0025` – «dem 1.1.2025 wird der steuerbare Ertragsanteil flexibel an die Anlagebedingungen angepasst.»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0078.md) `zh-wl-2025__c0078` – «ist anhand des jährlich von der Eidgenössischen Steuerverwaltung ESTV publizierten Satzes zu»

<a id="14-1-14-2-abzug-vorsorge-saeule3a"></a>
### Ziff. 14.1 / 14.2 – Beiträge Säule 3a, Person 1 (Code 260, eff. 262) / Person 2 (Code 261, eff. 263)

- **Schlüssel:** `abzug.vorsorge.saeule3a` (Beiträge Säule 3a (inkl. Einkäufe ab 2026)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → Bescheinigung der Bankstiftung / Versicherung (im Jahr 2025 tatsächlich einbezahlter Betrag)
- **Rein:** 3a-Bescheinigung Bankstiftung/Versicherung → 2025 einbezahlter Betrag (eff. Code 262/263) · Seite 1 «Ordentliche Beiträge an die Pensionskasse?» / Lohnausweis Ziff. 10.1 → Limite wählen · Ohne 2. Säule: Erwerbseinkommen (Ziff. 1 und 2)
- **Rechnen:** je Person: mit 2. Säule min(einbezahlt; 7’258); ohne 2. Säule min(einbezahlt; 20 % × Erwerbseinkommen; 36’288) → Code 260/261 (Kanton = Bund)
- **Regel:** Nur im Jahr 2025 tatsächlich einbezahlte Beiträge. Mit 2. Säule: max. CHF 7’258; ohne 2. Säule: 20 % des Erwerbseinkommens, max. CHF 36’288. Beide erwerbstätigen Ehegatten je einzeln (eigener Vorsorgevertrag). Mitarbeit im Betrag des Ehegatten nur bei echtem Arbeitsverhältnis. Bescheinigung beilegen.
- **Beachten:** Nur 2025 tatsächlich bezahlte Beiträge; Bescheinigung beilegen
- **Beachten:** Ehegatten je eigener Vertrag und Abzug; Mitarbeit im Betrieb des Partners nur bei echtem Arbeitsverhältnis
- **Limiten:**
  - Säule 3a – Maximum mit 2. Säule (CHF): Kanton **CHF 7'258 (Säule 3a: Erwerbstätige mit Pensionskasse (2. Säule): max. CHF 7'258 (Bemessungsjahr 2025).)** · Bund **CHF 7'258 (Säule 3a: Höchstabzug mit Zugehörigkeit zur 2. Säule (8 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – Maximum ohne 2. Säule (CHF): Kanton **CHF 36'288 (Säule 3a: Erwerbstätige ohne 2. Säule: 20 % des Erwerbseinkommens, max. CHF 36'288.)** · Bund **CHF 36'288 (Säule 3a: Höchstabzug ohne 2. Säule (max. 36'288, 40 % des oberen BVG-Grenzbetrags))**
  - Säule 3a – ohne 2. Säule in % des Erwerbseinkommens: Kanton **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. CHF 36'288).)** · Bund **20 % (Säule 3a ohne 2. Säule: 20 % des Erwerbseinkommens (max. CHF 36'288))**
- **Bund:** Gleiche Höchstbeträge (BVV 3); gleiche Zeile für Staat und Bund.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «14. Beiträge an anerkannte Formen der geb. Selbstvorsorge (3. Säule a)»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0081.md) `zh-wl-2025__c0081` – «für Steuerpflichtige, die einer Einrichtung der beruflichen Vorsorge (2. Säule) angehören,»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0081.md) `zh-wl-2025__c0081` – «höchstens 20% des Erwerbseinkommens, maximal aber CHF 36’288.»
  - [ZStB 31.1 (bis 2026) S. 1](../../chunks/zh/2025/zh-zstb-31-1-bis-2026/zh-zstb-31-1-bis-2026__c0002.md) `zh-zstb-31-1-bis-2026__c0002` – «ab 2025 7 258 36 288»
  - [Formular 300 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0002.md) `zh-form-300-2025__c0002` – «Pensionskasse (2. Säule)?»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0035.md) `zh-wl-2025__c0035` – «10.1 Ordentliche Beiträge»

<a id="14-3-ab-2026-abzug-vorsorge-saeule3a-einkauf"></a>
### Ziff. 14.3 (ab 2026) – Einkauf (Nachzahlung) Säule 3a – im Formular 2025 nicht vorhanden

- **Schlüssel:** `abzug.vorsorge.saeule3a_einkauf` (Einkauf (Nachzahlung) Säule 3a – ab Steuerjahr 2026) · **Status:** – na
- **Beleg → Feld:** Bescheinigung Säule 3a (Formular 21 EDP, Bank-/Versicherungsstiftung) → –
- **Rein:** – (Formular ZH 2025: Ziff. 14 nur Person 1/2, keine Einkaufszeile)
- **Rechnen:** Steuerjahr 2025: kein Eintrag (Formular ohne Einkaufszeile)
- **Regel:** Das Formular 300 für 2025 hat keine Zeile 14.3 (Ziff. 14 nur Person 1/2). 3a-Einkäufe sind erst ab dem Steuerjahr 2026 (Beitragslücken ab 2025) abziehbar – für Steuerjahr 2025 nicht deklarieren.
- **Beachten:** Einkauf nur für Lücken der zehn Vorjahre; Lücken vor der BVV-3-Änderung vom 6. November 2024 nicht einkaufbar
- **Beachten:** Jahreslücke = max. möglicher 3a-Beitrag des Jahres − effektiv einbezahlt; je Jahreslücke nur ein Einkauf
- **Beachten:** Im Einkaufsjahr voller ordentlicher Beitrag nötig; Einkauf max. 8 Prozent des oberen BVG-Grenzbetrags
- **Bemerkung:** Formular 300 ZH 2025 (zh-form-300-2025__c0008) enthält nur Ziff. 14.1/14.2; Einkauf 3a wird in der Zuordnung ZH 2026 behandelt.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «Beiträge an anerkannte Formen der geb. Selbstvorsorge (3. Säule a)»
  - [BVV 3 Übergangsbestimmung zur Änderung vom 6. November 2024](../../chunks/bund/2025/bund-bvv3/bund-bvv3__uebergang-disp-u3.md) `bund-bvv3__uebergang-disp-u3` – «die vor Inkrafttreten der Änderung vom 6. November 2024 entstanden sind, können nicht mit einem Einkauf ausgeglichen werden.»
  - [BVV 3 Art. 7a](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7a-t1.md) `bund-bvv3__art-7a-t1` – «in den zehn dem Einkauf vorangehenden Jahren nicht alle für sie maximal zulässigen Beiträge einbezahlt haben;»
  - [BVV 3 Art. 7a](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7a-t1.md) `bund-bvv3__art-7a-t1` – «den für sie zulässigen Beitrag nach Artikel 7 Absatz 1 vollständig einbezahlen.»
  - [BVV 3 Art. 7a](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7a-t1.md) `bund-bvv3__art-7a-t1` – «auf keinen Fall jedoch höher als 8 Prozent des oberen Grenzbetrags nach Artikel 8 Absatz 1 BVG.»
  - [MB 21 EDP S. 5](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0014.md) `bund-mb-21edp__c0014` – «In der Ziffer 3 sind Einkäufe in die Säule 3a zu bescheinigen.»
  - [MB 21 EDP S. 5](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0014.md) `bund-mb-21edp__c0014` – «aus der Differenz zwischen dem maximal für die steuerpflichtige Person möglichen Säule»
  - [BVV 3 Art. 7a](../../chunks/bund/2025/bund-bvv3/bund-bvv3__art-7a-t2.md) `bund-bvv3__art-7a-t2` – «Für den Ausgleich einer Beitragslücke eines bestimmten Jahres (Jahresbeitragslücke) ist nicht mehr als ein Einkauf zulässig.»

<a id="15-abzug-versicherungspraemien"></a>
### Ziff. 15 – Versicherungsprämien und Zinsen von Sparkapitalien (Code 270)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Formular 365 Teil C (Code 270): niedrigerer Betrag von (A) bezahlte Prämien und (B) Maximalabzug
- **Rein:** KK-Prämienbescheinigung → bezahlte Prämien, i. d. R. nach Prämienverbilligung (Form. 365 Code 601) · Unfall-/Lebens-/Rentenversicherung → bezahlte Prämien (Codes 602/603) · Wertschriften- und Guthabenverzeichnis → Zinsen von Sparkapitalien (Code 604) · Verfügung Prämienverbilligung → Code 605, soweit nicht schon in 601 verrechnet
- **Rechnen:** min(A; B) je Spalte → Code 270; A (606) = Σ 601–604 − 605; B (616) = Max. Verh./übrige (mit/ohne 2./3a) + je Kind/Unterstützte Kanton 1’300 / Bund 700
- **Regel:** Im Form. 365 Teil A bezahlte Prämien (KK, Unfall, Leben/Rente, Sparzinsen, abzüglich Prämienverbilligung) mit Teil B (Maximalabzug) vergleichen; der niedrigere Betrag nach Ziff. 15. Erhaltene Prämienverbilligung ist abzuziehen, soweit nicht schon in den Prämien berücksichtigt.
- **Beachten:** Max. Kanton 5’800 Verh. / 2’900 übrige (ohne 2./3a: 8’700 / 4’350); Bund 3’700 / 1’800 (5’550 / 2’700)
- **Beachten:** «Ohne 2./3a» nur, wenn weder Steuerpflichtige noch Arbeitgeber Beiträge an 2. Säule/3a leisteten
- **Beachten:** Halber Kinderabzug: Zuschlag Kanton 650 / Bund 350 je Kind
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'800 (Versicherungsprämien und Sparzinsen, in ungetrennter Ehe Lebende, MIT Beiträgen an 2. Säule/Säule 3a: max. CHF 5'800 (Staatssteuer).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 8'700 (Gemeinsam Besteuerte ohne Beiträge an 2. Säule und Säule 3a: Abzug erhöht sich um die Hälfte, max. CHF 8'700.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an Säule 2/3a (Erhöhung um die Hälfte))**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'900 (Übrige Steuerpflichtige MIT Beiträgen an 2. Säule/Säule 3a: max. CHF 2'900 (Staatssteuer).)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 4'350 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule/3a: max. CHF 4'350 (2'900 + die Hälfte).)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an Säule 2/3a)**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'300 (Zusätzlicher Versicherungsabzug von CHF 1'300 für jedes Kind oder jede unterstützungsbedürftige Person, für die ein Abzug nach § 34 Abs. 1 geltend gemacht werden kann (Bund: CHF 700).)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
- **Bund:** Bundessteuer-Spalte mit tieferen Maxima (Form. 365 Teil B).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «15. Versicherungsprämien, Zinsen von Sparkapitalien Versich.prämien 270»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0082.md) `zh-wl-2025__c0082` – «Der zulässige Abzug für Versicherungsprämien und Sparzinsen ist im Formular Versicherungs-»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0003.md) `zh-form-365-2025__c0003` – «Der niedrigere Betrag: (A) oder (B) 270»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md) `zh-form-365-2025__c0001` – «1. Private Krankenversicherungsprämien 601»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md) `zh-form-365-2025__c0001` – «6. Abzüglich erhaltene Prämienverbilligungen 605»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «Zusätzlicher Abzug für jedes Kind Anzahl: 1’300 700 613»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0083.md) `zh-wl-2025__c0083` – «Rentenversicherungen sowie Zinsen von Sparkapitalien (gemäss Wertschriften- und Gut»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0086.md) `zh-wl-2025__c0086` – «Wenn von den Steuerpflichtigen oder ihrem Arbeitgeber keine Beiträge an Einrichtun-»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0091.md) `zh-wl-2025__c0091` – «CHF 650 für jedes Kind, für das der steuerpflichtigen Person ein halber Kinderabzug-»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0091.md) `zh-wl-2025__c0091` – «CHF 350 für jedes Kind, für das der steuerpflichtigen Person ein halber Kinderabzug zusteht.»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «Total der Abzüge für Versicherungsprämien und Zinsen von Sparkapitalien (B) 616»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md) `zh-form-365-2025__c0001` – «Total bezahlte Versicherungsprämien und Zinsen von Sparkapitalien (A) 606»

<a id="16-1-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. 16.1 – Beiträge an 2. Säule inkl. Einkäufe, soweit nicht im Lohnausweis abgezogen (Code 280)

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Bescheinigung der Vorsorgeeinrichtung (Formular 21 EDP) – nur selbst bezahlte, nicht vom Lohn abgezogene Beiträge/Einkäufe
- **Rein:** Bescheinigung Vorsorgeeinrichtung (Formular 21 EDP) → selbst überwiesene Beiträge/Einkäufe · Lohnausweis Ziff. 10.1/10.2 → bereits vom Lohn abgezogen (nicht nochmals)
- **Rechnen:** Σ selbst bezahlte PK-Beiträge/Einkäufe gem. Bescheinigung, soweit nicht in Lohnausweis Ziff. 10.1/10.2 (Code 280; Kanton = Bund)
- **Regel:** Nur Einkäufe/Beiträge eintragen, die NICHT bereits im Lohnausweis (Ziff. 10.1/10.2) vom Lohn abgezogen sind. Einkäufe sind nicht abziehbar, soweit innert drei Jahren ein Kapitalbezug erfolgt (Sperrfrist). Bescheinigung beilegen.
- **Beachten:** Einkäufe nicht abziehbar, soweit innerhalb von drei Jahren ein Kapitalbezug erfolgt
- **Beachten:** Vom Lohn abgezogene Beiträge nur im Lohnausweis, selbst überwiesene nur im Formular 21
- **Beachten:** Bescheinigung der Vorsorgeeinrichtung beilegen
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.1 Beiträge an die AHV, IV und 2. Säule, sofern nicht unter Ziff. 1 und 2 abgezogen 280»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0092.md) `zh-wl-2025__c0092` – «Weiter ist zu beachten, dass Einkäufe steuerlich nicht zum Abzug zugelassen»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0092.md) `zh-wl-2025__c0092` – «werden, soweit innerhalb von drei Jahren ein Kapitalbezug erfolgt.»
  - [MB 21 EDP S. 2–3](../../chunks/bund/dauernd/bund-mb-21edp/bund-mb-21edp__c0006.md) `bund-mb-21edp__c0006` – «alle vom Arbeitnehmer aus eigenen Mitteln aufgebrachten, aber ihm nicht vom Lohn abgezogenen Beiträge nur im Formular 21 angegeben werden dürfen»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0035.md) `zh-wl-2025__c0035` – «10.2 Beiträge für den Einkauf»

<a id="16-1-abzug-ahv-nichterwerbstaetige"></a>
### Ziff. 16.1 – Beiträge an AHV/IV (z. B. Nichterwerbstätige, Selbständige ohne Abzug im Hilfsblatt) (Code 280)

- **Schlüssel:** `abzug.ahv_nichterwerbstaetige` (AHV/IV/EO-Beiträge Nichterwerbstätiger u.ä.) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** AHV-Beitragsverfügung / Rechnung für Nichterwerbstätige (Ausgleichskasse) → AHV-Beitragsverfügung / Bescheinigung der Ausgleichskasse
- **Rein:** Beitragsverfügung/-rechnung Ausgleichskasse (Nichterwerbstätige) → AHV/IV/EO-Beiträge · Selbständige: Hilfsblatt A Ziff. 4.1 (Code 1741) → persönliche AHV/IV/EO-Beiträge
- **Rechnen:** Σ AHV/IV/EO-Beiträge gem. Bescheinigung, soweit Einkünfte Ziff. 1 und 2 nicht bereits darum gekürzt (Code 280; Kanton = Bund)
- **Regel:** AHV-/IV-Beiträge nur abziehen, soweit die unter Ziff. 1 und 2 deklarierten Einkünfte nicht schon um diese Beiträge gekürzt wurden. Bescheinigung beilegen.
- **Beachten:** Bescheinigung beilegen
- **Beachten:** Bund-WL: Arbeitgeberbeiträge für privates Dienstpersonal nicht abziehbar
- **Quellen:**
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0092.md) `zh-wl-2025__c0092` – «Beiträge an die AHV und IV, soweit die unter Ziffern 1 und 2 der Steuererklärung deklarierten»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.1 Beiträge an die AHV, IV und 2. Säule, sofern nicht unter Ziff. 1 und 2 abgezogen 280»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0041.md) `zh-wl-2025__c0041` – «Persönliche AHV/IV/EO-Beiträge (in Ziff. 16.1 der Steuererklärung abzuziehen) 1741»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0052.md) `bund-wl-2a-2025__c0052` – «Beiträge Nichterwerbstätiger an die AHV, IV und EO.»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0052.md) `bund-wl-2a-2025__c0052` – «Nicht zulässig ist der Abzug von Arbeitgeberbeiträgen für das private Dienstpersonal.»

<a id="16-2-abzug-weiterbildung"></a>
### Ziff. 16.2 – Berufsorientierte Aus- und Weiterbildungskosten (Code 292)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Formular 367 (selbstgetragene Kosten nach Abzug Arbeitgeberbeitrag) + Kursrechnungen / Zahlungsnachweise
- **Rein:** Kursrechnungen + Zahlungsbelege → Total der Kosten (Form. 367 Code 2900/2903) · Bestätigung Arbeitgeber/Dritte bzw. Lohnausweis Ziff. 13.3 → Beiträge Dritter (Code 2901/2904)
- **Rechnen:** je Person (Spalten Person 1 / Person 2): 2902/2905 = 2900/2903 − 2901/2904; zulässiger Abzug 2920 (Person 1) / 2921 (Person 2) = min(selbstgetragen; Block Staatssteuer 12’400 bzw. Block Bundessteuer 13’000); je Block 292 = 2920 + 2921
- **Regel:** Selbst getragene Kosten (nach Abzug Beiträge Dritter, z. B. Arbeitgeber/Bund) bis max. CHF 12’400 (Staat) bzw. CHF 13’000 (Bund), sofern Abschluss Sek. II vorliegt oder 20. Altersjahr vollendet und nicht Ausbildung bis zum ersten Sek.-II-Abschluss. Massgebend ist Fälligkeit/Zahlung, nicht der Kursbesuch. Lohnausweis Ziff. 13.3 beachten.
- **Beachten:** Nur mit Abschluss Sek. II oder ab vollendetem 20. Lebensjahr; nicht Ausbildung bis zum ersten Sek.-II-Abschluss
- **Beachten:** Zeitpunkt: Fälligkeit bzw. Zahlung, nicht der Kursbesuch
- **Beachten:** Formular 367 vollständig ausgefüllt beilegen
- **Beachten:** Codes 2920/2921 = Person 1 / Person 2 (nicht Staat/Bund); Staats- und Bundessteuer stehen in getrennten Blöcken mit denselben Codes
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 12'400 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung, selbst getragene Kosten: max. CHF 12'400 (Staatssteuer), sofern Abschluss Sek. II vorliegt oder 20. Lebensjahr vollendet (und nicht Ausbildung bis zum ersten Sek.-II-Abschluss).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Bund:** Bund: max. CHF 13’000 je Person (Form. 367 Block «Bundessteuer»: 2920 = Person 1, 2921 = Person 2; 2920 + 2921 → Code 292 in der Bundessteuer-Spalte Ziff. 16.2). (Layout: raw/zh/2025/zh-form-367-2025.pdf S. 1)
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.2 Berufsorientierte Aus- und Weiterbildungskosten Hilfsblatt 292»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0093.md) `zh-wl-2025__c0093` – «betrag von CHF 12’400 bei der Staatssteuer bzw. CHF 13’000 bei der Bundessteuer, sofern ein»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t4.md) `zh-stg-2025__par-31-t4` – «die Kosten der berufsorientierten Aus- und Weiterbildung, einschliesslich Umschulungskosten, bis zum Gesamtbetrag von Fr. 12 400»
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Beitrag Arbeitgeber oder weiterer Stellen (Bund, Branchenverbände etc.)»
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Zulässiger Abzug (max. je CHF 13’000) 2920 / 2921»
  - [KS 42 S. 9](../../chunks/bund/dauernd/bund-ks-42/bund-ks-42__c0025.md) `bund-ks-42__c0025` – «bescheinigt der Arbeitgeber diese Vergütung im Lohnausweis in Ziffer 13.3»
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Zulässiger Abzug (max. je CHF 12’400) 2920 / 2921»
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Bezeichnung Person 1 Person 2»

<a id="16-3-abzug-verwaltungskosten-wertschriften"></a>
### Ziff. 16.3 – Kosten für die Verwaltung des beweglichen Privatvermögens (Code 283)

- **Schlüssel:** `abzug.verwaltungskosten_wertschriften` (Vermögensverwaltungskosten bewegliches Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.) → Depotgebührenausweis / Steuerauszug (Verwaltungs- und Verwahrungskosten Dritter)
- **Rein:** Depot-/Verwaltungsgebührenabrechnung Bank → effektive Verwaltungs- und Verwahrungskosten · Wertschriftenverzeichnis → Steuerwert der durch Dritte verwalteten Wertschriften
- **Rechnen:** Pauschal min(3 ‰ × Steuerwert drittverwalteter Wertschriften; 6’000) oder höhere effektive Kosten mit vollem Nachweis (Code 283)
- **Regel:** Verwaltungs-/Verwahrungskosten durch Dritte abziehbar, nicht aber Erwerbs-/Veräusserungskosten (Courtagen, Stempel). Pauschal 3 ‰ des Steuerwerts der durch Dritte verwalteten Wertschriften, max. CHF 6’000, oder höhere effektive Kosten mit Nachweis.
- **Beachten:** Nicht abziehbar: Kosten für Erwerb und Veräusserung von Wertschriften
- **Beachten:** Abziehbar auch: weder rückforderbare noch anrechenbare ausländische Quellensteuern
- **Beachten:** Details: Weisung Zürcher Steuerbuch Nr. 30.1
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.3 Kosten für die Verwaltung des beweglichen Privatvermögens 283»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0095.md) `zh-wl-2025__c0095` – «können 3‰ des Steuerwerts dieser durch Dritte verwalteten Wertschriften, maximal»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0095.md) `zh-wl-2025__c0095` – «jedoch CHF 6’000, abgezogen werden.»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0094.md) `zh-wl-2025__c0094` – «rückforderbaren noch anrechenbaren ausländischen Quellensteuern abgezogen werden.»

<a id="16-4-abzug-behinderungskosten"></a>
### Ziff. 16.4 – Behinderungsbedingte Kosten (Code 3160)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Formular 370 Seite 2 «Aufstellung über behinderungsbedingte Kosten» (Total abzugsberechtigte Kosten, Code 3155 / Pauschale 3103)
- **Rein:** Rechnungen Pflege, Betreuung, Hilfsmittel, Transporte, Heim → Form. 370 S. 2 Teil A (Code 3120) · KK-/Versicherungsabrechnung, Hilflosenentschädigung, Anteil Lebenshaltung → Teil B (Code 3150) · Verfügung Hilflosenentschädigung (Grad) bzw. Nachweis Gehörlosigkeit/Dialyse → Pauschale (Code 3103)
- **Rechnen:** Effektiv: A (3120) − B (3150) = 3155; oder Pauschale (3103): HE leicht 2’500 / mittel 5’000 / schwer 7’500; Gehörlose, Dialyse 2’500 → Code 3160 (Kanton = Bund)
- **Regel:** Behinderungsbedingte Kosten (Behindertengleichstellungsgesetz), soweit selbst getragen; Vergütungen Dritter (Krankenkasse, Hilflosenentschädigung, Anteil Lebenshaltungskosten) abziehen. Formular 370 Rückseite einreichen. Kein Selbstbehalt, zu unterscheiden von Krankheitskosten Ziff. 22.1.
- **Beachten:** B enthält Anteil Lebenshaltungskosten (Kosten, die auch ohne Behinderung angefallen wären)
- **Beachten:** Hilfe im Haushalt/Kinderbetreuung nur, soweit über dem Abzug Ziff. 16.6
- **Beachten:** Kein Selbstbehalt (anders als Krankheitskosten Ziff. 22.1, Rückseite Form. 370); eine Aufstellung je Steuererklärung
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.4 Behinderungsbedingte Kosten Hilfsblatt 3160»
  - [Formular 370 ZH S. 2](../../chunks/zh/2025/zh-form-370/zh-form-370__c0006.md) `zh-form-370__c0006` – «Total der abzugsberechtigten Kosten 3155»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t3.md) `zh-stg-2025__par-31-t3` – «die behinderungsbedingten Kosten des Steuerpflichtigen»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0016.md) `zh-zstb-32-1__c0016` – «Anstelle des Abzugs der effektiven, selbst getragenen Kosten können behinderte Personen einen jährlichen Pauschalabzug in folgender Höhe geltend machen:»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0016.md) `zh-zstb-32-1__c0016` – «Bezüger einer Hilflosenentschädigung schweren Grades: Fr. 7’500.-»
  - [KS 11 S. 10](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0025.md) `bund-ks-11__c0025` – «Bezüger einer Hilflosenentschädigung mittleren Grades: CHF 5'000.--»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0013.md) `zh-zstb-32-1__c0013` – «soweit die Auslagen den Abzug für Drittbetreuungskosten gemäss Ziffer 16.6 der Steuererklärung übersteigen»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0014.md) `zh-zstb-32-1__c0014` – «sowie allfällige Anteile für Lebenshaltungskosten (Kosten, die auch ohne Behinderung angefallen wären) übersteigen.»
  - [Formular 370 ZH S. 2](../../chunks/zh/2025/zh-form-370/zh-form-370__c0005.md) `zh-form-370__c0005` – «Aufstellung über Krankheits- und Unfallkosten siehe Rückseite»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0004.md) `zh-zstb-32-1__c0004` – «Für den Abzug der behinderungsbedingten Kosten besteht kein solcher Selbstbehalt.»
  - [Formular 370 ZH S. 2](../../chunks/zh/2025/zh-form-370/zh-form-370__c0005.md) `zh-form-370__c0005` – «Pro Steuererklärung ist nur eine Aufstellung einzureichen.»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «Seite 3, Ziffer 22.1»

<a id="16-5-abzug-parteispenden"></a>
### Ziff. 16.5 – Beiträge und Zuwendungen an politische Parteien (Code 284, Aufstellung)

- **Schlüssel:** `abzug.parteispenden` (Mitgliederbeiträge und Zuwendungen an politische Parteien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bestätigung Mitgliederbeiträge und Zuwendungen an politische Parteien → Spendenbestätigung der Partei (Parteienregister / Kantonsparlament / ≥ 3 % Wähleranteil)
- **Rein:** Spendenbestätigungen / Beitragsrechnungen der Partei → Σ Mitgliederbeiträge und Zuwendungen 2025
- **Rechnen:** Kanton: min(Σ; 20’600 ungetrennte Ehe / 10’300 übrige); Bund: min(Σ; 10’600) für alle → Ziff. 16.5 (Code 284)
- **Regel:** Staatssteuer max. CHF 20’600 (in ungetrennter Ehe) bzw. CHF 10’300 (übrige); Bundessteuer max. CHF 10’600 (für alle). Nur Parteien im Parteienregister, mit Sitz im kantonalen Parlament oder mit mind. 3 % Stimmen.
- **Beachten:** Nur Parteien im Parteienregister, in einem kantonalen Parlament oder mit mind. 3 % Stimmen bei letzten Parlamentswahlen
- **Beachten:** Aufstellung (Code 284) und Belege beilegen
- **Limiten:**
  - Parteispenden – Maximum (CHF), ggf. alleinstehend: Kanton **CHF 10'300 (Mitgliederbeiträge und Zuwendungen an politische Parteien (im Parteienregister eingetragen, im kantonalen Parlament vertreten oder mind. 3 % Wähleranteil): max. CHF 10'300 für übrige Steuerpflichtige.)** · Bund **CHF 10'600 (Mitgliederbeiträge und Zuwendungen an politische Parteien bis CHF 10'600)**
  - Parteispenden – Maximum gemeinsam Besteuerte (CHF): Kanton **CHF 20'600 (Parteispenden gemeinsam Besteuerte (ungetrennte Ehe): max. CHF 20'600.)** · Bund **n/a – Bund kennt nur einen Gesamtbetrag von CHF 10'600 (Art. 33 Abs. 1 lit. i DBG); keine Verdoppelung für Ehepaare in der Quelle.**
- **Bund:** Bund: max. CHF 10’600 für Verheiratete und Übrige (Art. 33 Abs. 1 lit. i DBG).
- **Quellen:**
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0100.md) `zh-wl-2025__c0100` – «Höchstbetrag von CHF 20’600 für in ungetrennter Ehe lebende Steuerpflichtige und von»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0100.md) `zh-wl-2025__c0100` – «Der Höchstbetrag für solche Abzüge beträgt CHF 10’600.»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t3.md) `zh-stg-2025__par-31-t3` – «bis zum Gesamtbetrag von Fr. 20 600 für in ungetrennter Ehe lebende Steuerpflichtige und von Fr. 10 300 für die übrigen Steuerpflichtigen»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.5 Weitere Abzüge (z.B. Beiträge an politische Parteien) Aufstellung 284»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0098.md) `zh-wl-2025__c0098` – «wahlen mindestens 3% der Stimmen erreicht haben.»
  - [WL 2a 2025 S. 7–8](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0053.md) `bund-wl-2a-2025__c0053` – «Die Belege sind beizufügen.»

<a id="16-5-abzug-teilbesteuerung-beteiligungen"></a>
### Ziff. 16.5 – Weitere Abzüge: Teilbesteuerung qualifizierte Beteiligungen (Abzug 50 % Staat / 30 % Bund)

- **Schlüssel:** `abzug.teilbesteuerung_beteiligungen` (Teilbesteuerungsabzug qualifizierte Beteiligungen (wo als Abzugszeile geführt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Formular «Qualifizierte Beteiligungen im Privatvermögen / Geschäftsvermögen» + Dividendenbeleg
- **Rein:** Dividendenbeleg / Steuerauszug → Bruttoausschüttung, im Wertschriftenverzeichnis mit Code «Q» · Formular «Qualifizierte Beteiligungen im Privat-/Geschäftsvermögen» → nicht steuerbarer Teil
- **Rechnen:** Privatvermögen: Kanton 50 % / Bund 30 % × Bruttoertrag qual. Beteiligungen; Geschäftsvermögen: gleiche Sätze nach Abzug des zurechenbaren Aufwands → Code 284
- **Regel:** Nicht steuerbarer Teil der in Ziff. 4.2 deklarierten Erträge aus qualifizierten Beteiligungen: Privatvermögen 50 % (Staat) bzw. 30 % (Bund); gratis abgegebene Mitarbeiteraktien: kein Abzug. Betrag in Ziff. 16.5 (Staats-/Bundessteuer-Spalte unterschiedlich).
- **Beachten:** Qualifiziert = mindestens 10% des Grund- oder Stammkapitals
- **Beachten:** Ertrag ungekürzt (brutto) in Kolonne A bzw. B deklarieren
- **Beachten:** Gratis abgegebene Mitarbeiteraktien: kein Abzug
- **Bund:** Bund: 30 % statt 50 %.
- **Quellen:**
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md) `zh-wl-2025__c0104` – «Privatvermögen beträgt 50%, für qualifizierte Beteiligungen»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md) `zh-wl-2025__c0104` – «Privatvermögen beträgt 30%, für qualifizierte Beteiligungen»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md) `zh-wl-2025__c0104` – «Bei gratis abgegebenen Mitarbeiteraktien kann kein Abzug vorgenommen werden.»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0165.md) `zh-wl-2025__c0165` – «Beteiligungen, die mindestens 10% des Grund- oder Stammkapitals einer Kapitalgesellschaft»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0165.md) `zh-wl-2025__c0165` – «Code «Q» zu bezeichnen. Sie sind ungekürzt, d.h. mit dem Bruttobetrag der Ausschüttung,»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.5 Weitere Abzüge (z.B. Beiträge an politische Parteien) Aufstellung 284»

<a id="16-5-abzug-uebrige"></a>
### Ziff. 16.5 – Weitere Abzüge (Freitext, Code 284): Liquidationsgewinne, Grundstückgewinn-Freistellung, Einsatzkosten Geldspiele

- **Schlüssel:** `abzug.uebrige` (Übrige Abzüge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Aufstellung / Hilfsformular (z. B. Liquidationsgewinn-Formular, Spielgewinn-Abrechnung)
- **Rein:** Hilfsformular «Liquidationsgewinn bei Aufgabe der selbständigen Erwerbstätigkeit» → Liquidationsgewinn aus Ziff. 2.1/2.2 · Gewinnabrechnung Geldspiele / Online-Spielerkonto → Gewinne bzw. abgebuchte Einsätze · Hilfsblatt STAF (Form. 547) → Patentbox/F&E-Zusatzabzug
- **Rechnen:** Geldspiel je Gewinn: min(5 % × Gewinn; Kanton 5’200 / Bund 5’400); Online-Spielbank: Einsätze, max. Kanton 25’800 / Bund 26’800; Liquidationsgewinn: voll
- **Regel:** Liquidationsgewinne aus Ziff. 2.1 (gesonderte Besteuerung), freizustellender Teil des Grundstückgewinns (Staatssteuer), 5 % Einsatzkosten bei Geldspielgewinnen (max. CHF 5’200 Staat / CHF 5’400 Bund), Patentbox/F&E-Zusatzabzug (Form. 547).
- **Beachten:** Liquidationsgewinn nur bei definitiver Aufgabe nach vollendetem 55. Altersjahr oder wegen Invalidität
- **Beachten:** Nur Staatssteuer: freizustellenden Teil des Grundstückgewinns abziehen
- **Beachten:** Patentbox/F&E: Form. 547 vollständig beilegen
- **Quellen:**
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0105.md) `zh-wl-2025__c0105` – «Für die Staatssteuer ist der bei der Einkommenssteuer freizustellende Teil des Grund»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0105.md) `zh-wl-2025__c0105` – «Selbständig Erwerbende, welche die Patentbox oder den Zusatzabzug für Forschungs- und»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0043.md) `zh-wl-2025__c0043` – «Solche Liquidationsgewinne können unter Ziffer 16.5 wieder von den Einkünften abgezogen werden»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0103.md) `zh-wl-2025__c0103` – ««Liquidationsgewinn bei Aufgabe der selbständigen Erwerbstätigkeit» erforderlich.»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0102.md) `zh-wl-2025__c0102` – «nach dem vollendeten 55. Altersjahr»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0105.md) `zh-wl-2025__c0105` – «tens CHF 5’200 (Staatssteuer) bzw. CHF 5’400 (Bundessteuer), als Einsatzkosten abgezogen»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0105.md) `zh-wl-2025__c0105` – «die effektiven Einsätze, maximal jedoch CHF 25’800 (Staatssteuer) bzw. CHF 26’800 (Bundes-»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t5.md) `zh-stg-2025__par-31-t5` – «Von den einzelnen Gewinnen aus der Teilnahme an Geldspielen»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0101.md) `zh-wl-2025__c0101` – «Bundessteuer werden bei definitiver Aufgabe der selbständigen Erwerbstätigkeit»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t5.md) `zh-stg-2025__par-31-t5` – «vom Online-Spielerkonto abgebuchten Spieleinsätze»

<a id="16-6-abzug-drittbetreuung"></a>
### Ziff. 16.6 – Abzug für fremdbetreute Kinder (Jahrg. 2011–2025) (Code 376)

- **Schlüssel:** `abzug.drittbetreuung` (Kinderdrittbetreuungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen Kinderbetreuung (Kita/Krippe, Tagesstätte, Tagesmutter, Hort, Tagesschule) → Rechnungen/Quittungen Kita, Tagesfamilie, Hort etc. mit Zahlungsnachweis (Name Kind, Zeitraum)
- **Rein:** Rechnungen Kita/Hort/Tagesfamilie + Zahlungsnachweise → Betreuungskosten je Kind · Seite 1 Kinder → Geburtsdatum (Jahrg. 2011–2025)
- **Rechnen:** je Kind < 14 J.: min(nachgewiesene Kosten; Kanton 25’000 / Bund 25’800) → Code 376; Konkubinat mit gemeinsamer Sorge: je max. Kanton 12’500 / Bund 12’900
- **Regel:** Nachgewiesene Kosten für jedes Kind unter 14 Jahren im gleichen Haushalt, max. CHF 25’000 (Staat) bzw. CHF 25’800 (Bund) pro Kind; Kosten müssen in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit stehen. Konkubinat mit gemeinsamer Sorge: je halber Abzug (max. CHF 12’500 Staat / CHF 12’900 Bund). Verpflegung/Schulgeld nicht betreuungsbedingt.
- **Beachten:** Nur Kosten im direkten Zusammenhang mit Erwerb, Ausbildung oder Erwerbsunfähigkeit; Kind im gleichen Haushalt
- **Beachten:** Andere als hälftige Aufteilung nachweisen; gilt auch bei alternierender Obhut mit gemeinsamer Sorge
- **Limiten:**
  - Kinderdrittbetreuungskosten – Maximum pro Kind (CHF): Kanton **CHF 25'000 (Nachgewiesene Kinderdrittbetreuungskosten: max. CHF 25'000 pro Kind (Staatssteuer), wenn Kind unter 14, im gleichen Haushalt, und Kosten in direktem Zusammenhang mit Erwerbstätigkeit, Ausbildung oder Erwerbsunfähigkeit.)** · Bund **CHF 25'800 (Nachgewiesene Drittbetreuungskosten pro Kind bis max. CHF 25'800 (Kind unter 14, im gleichen Haushalt, Zusammenhang mit Erwerbstätigkeit/Ausbildung/Erwerbsunfähigkeit))**
  - Kinderdrittbetreuung – Altersgrenze Kind: Kanton **14 Jahre (Kind darf das 14. Altersjahr noch nicht vollendet haben.)** · Bund **14 Jahre (Kind, das das 14. Altersjahr noch nicht vollendet hat)**
- **Bund:** Bund: max. CHF 25’800 pro Kind (Art. 33 Abs. 3 DBG).
- **Bemerkung:** Hinweis: Die VKP ZH ab 2024 (zh-vkp-2024-zstb__c0005) nennt noch Fr. 10 400 für § 31 Abs. 1 lit. j; für 2025 gilt gemäss StG ZH Nachtrag 127 (zh-stg-2025__par-31-t4), Formular und WL der Betrag CHF 25’000 – die Verordnung 10’400 ist überholt und nicht anzuwenden.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.6 Abzug für fremdbetreute Kinder (Jahrg. 2011-2025) max. 25’000 / 25’800 376»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t4.md) `zh-stg-2025__par-31-t4` – «die nachgewiesenen Kosten, jedoch höchstens Fr. 25 000, für die Drittbetreuung jedes Kindes»
  - [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0107.md) `zh-wl-2025__c0107` – «CHF 25’800 (Bundessteuer) pro Kind. Für jedes Kind, welches das 14. Altersjahr noch nicht»
  - [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0109.md) `zh-wl-2025__c0109` – «machen. Der halbe Abzug beträgt je höchstens CHF 12’500 (Staatssteuer) bzw. CHF 12’900»
  - [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0110.md) `zh-wl-2025__c0110` – «eine andere Aufteilung ist von den Eltern nachzuweisen. Dasselbe gilt für Eltern mit Kindern unter alternierender Obhut»
  - [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0108.md) `zh-wl-2025__c0108` – «steuerpflichtigen Person, die für seinen Unterhalt sorgt, im gleichen Haushalt leben.»

<a id="17-abzug-zweiverdiener"></a>
### Ziff. 17 – Sonderabzug bei Erwerbstätigkeit beider Ehegatten / Partner (Code 290)

- **Schlüssel:** `abzug.zweiverdiener` (Zweiverdienerabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Berechnung aus verbleibendem niedrigerem Erwerbseinkommen (Ziff. 1–2 abzüglich Berufsauslagen, 3a, 2.-Säule-Einkäufe, nicht über Lohnausweis berücksichtigte AHV/BVG)
- **Rein:** Übertrag: Erwerbseinkommen je Ehegatte (Ziff. 1–2) · abzüglich je Person Berufsauslagen (Ziff. 11), Säule 3a (Ziff. 14), Einkäufe 2. Säule / AHV nicht via Lohnausweis (Ziff. 16.1)
- **Rechnen:** Basis = niedrigeres verbleibendes Erwerbseinkommen; Kanton: min(Basis; 6’100); Bund: min(Basis; max(50 % × Basis; 8’600); 14’100) → Code 290
- **Regel:** Nur für in ungetrennter Ehe lebende, beide erwerbstätige Ehegatten, einmal pro Paar. Staatssteuer: max. CHF 6’100 (vom niedrigeren verbleibenden Erwerbseinkommen, bei Mitarbeit vom gemeinsamen). Bundessteuer: 50 % des niedrigeren Erwerbseinkommens, mind. CHF 8’600, max. CHF 14’100; unter CHF 8’600 Abzug in Höhe des Einkommens.
- **Beachten:** Nur Ehegatten in ungetrennter Ehe, beide erwerbstätig; nur einmal beanspruchbar
- **Beachten:** Erhebliche Mitarbeit im Betrieb des Ehegatten: Kanton vom gemeinsamen Einkommen; Bund i. d. R. hälftig aufteilen
- **Limiten:**
  - Zweiverdienerabzug – Minimum (CHF): Kanton **n/a – ZH: kein Minimum; liegt das tiefere Erwerbseinkommen unter CHF 6'100, wird nur dieser tiefere Betrag abgezogen (WL ZH 2025 Ziff. 17).** · Bund **CHF 8'600 (Zweiverdienerabzug Minimum)**
  - Zweiverdienerabzug – Maximum bzw. fixer Betrag (CHF): Kanton **CHF 6'100 (Zweiverdienerabzug bei ungetrennter Ehe: CHF 6'100 vom (niedrigeren) Erwerbseinkommen; bei erheblicher Mitarbeit im Geschäft des Ehegatten vom gemeinsamen Erwerbseinkommen; ist dieses tiefer, nur der tiefere Betrag.)** · Bund **CHF 14'100 (Zweiverdienerabzug Maximum)**
  - Zweiverdienerabzug – Satz (% des tieferen Erwerbseinkommens): Kanton **n/a – ZH: fixer Abzug von CHF 6'100 (bzw. tieferes Erwerbseinkommen), kein Prozentsatz (§ 31 Abs. 2 StG). Der Prozentsatz-Mechanismus gilt nur beim Bund.** · Bund **50 % (Zweiverdienerabzug: 50 % des niedrigeren Erwerbseinkommens (bei Ehegatten in ungetrennter Ehe mit beidseitigem Erwerbseinkommen))**
- **Bund:** Bund: 50 % des niedrigeren Erwerbseinkommens, mind. CHF 8’600, max. CHF 14’100 (Art. 33 Abs. 2 DBG).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «17. Sonderabzug bei Erwerbstätigkeit beider Ehegatten/Partn.»
  - [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0112.md) `zh-wl-2025__c0112` – «Der Abzug beträgt max. CHF 6’100 und steht wie folgt zu:»
  - [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0113.md) `zh-wl-2025__c0113` – «mens, jedoch mind. CHF 8’600 und max. CHF 14’100;»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t5.md) `zh-stg-2025__par-31-t5` – «Fr. 6100 abgezogen»
  - [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0111.md) `zh-wl-2025__c0111` – «Massgebend für die Berechnung ist das verbleibende niedrigere Erwerbseinkommen,»
  - [WL ZH 2025 S. 18](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0111.md) `zh-wl-2025__c0111` – «beider Ehegatten kann nur einmal beansprucht werden.»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «11. Berufsauslagen bei unselbständiger Erwerbstätigkeit»

<a id="18-berechnung-total"></a>
### Ziff. 18 – Total der Abzüge (Code 299)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 11–17)
- **Rein:** Übertrag aus Ziff. 11–17 (je Spalte Staatssteuer / Bundessteuer)
- **Rechnen:** Σ Ziff. 11.1 bis 17 je Spalte (Code 299); Übertrag in Ziffer 20
- **Regel:** Rechenzeile; Übertrag in Ziffer 20.
- **Beachten:** Staats- und Bundessteuer-Spalte getrennt summieren (unterschiedliche Maxima)
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «18. Total der Abzüge, zu übertragen in Ziffer 20»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «11. Berufsauslagen bei unselbständiger Erwerbstätigkeit»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «20. Total der Abzüge Übertrag von Ziffer 18»

## Einkommensberechnung

<a id="19-berechnung-total"></a>
### Ziff. 19 – Total der Einkünfte (Code 199)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Übertrag Seite 2, Ziffer 7
- **Rein:** Übertrag aus Ziff. 7 (Total der Einkünfte)
- **Rechnen:** = Ziffer 7 je Spalte (Staatssteuer / Bundessteuer), Code 199
- **Regel:** Rechenzeile: Übertrag von Ziff. 7.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «19. Total der Einkünfte Übertrag von Seite 2, Ziffer 7»
  - [WL ZH 2025 S. 19](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0114.md) `zh-wl-2025__c0114` – «Hier werden die Ergebnisse gemäss Ziffer 7 eingetragen.»

<a id="20-berechnung-total"></a>
### Ziff. 20 – Total der Abzüge (Code 299)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Übertrag Ziffer 18
- **Rein:** Übertrag aus Ziff. 18 (Total der Abzüge)
- **Rechnen:** = Ziffer 18 je Spalte (Code 299); wird von Ziffer 19 abgezogen
- **Regel:** Rechenzeile: Übertrag von Ziff. 18; Subtraktion von Ziff. 19.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «20. Total der Abzüge Übertrag von Ziffer 18»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «18. Total der Abzüge, zu übertragen in Ziffer 20»

<a id="21-berechnung-total"></a>
### Ziff. 21 – Nettoeinkommen (Code 310)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 19 – Ziff. 20)
- **Rein:** Rechenzeile: Ziff. 19 − Ziff. 20
- **Rechnen:** = Ziffer 19 − Ziffer 20 je Spalte (Code 310)
- **Regel:** Rechenzeile; Basis für den Selbstbehalt Krankheitskosten (5 %) und die Obergrenze gemeinnütziger Zuwendungen (20 %).
- **Beachten:** Basis für Selbstbehalt Krankheitskosten 5 % (Ziff. 22.1) und Spendenlimite 20 % (Ziff. 22.2), je Spalte
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen nach §§ 26–31 verminderten steuerbaren Einkünfte (Nettoeinkommen, Ziff. 21) übersteigen. Behinderungsbedingte Kosten ohne Selbstbehalt (§ 31 lit. i).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen insgesamt max. 20 % der um die Aufwendungen nach §§ 26–31 verminderten steuerbaren Einkünfte (Nettoeinkommen).)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «21. Nettoeinkommen 310»
  - [WL ZH 2025 S. 19](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0115.md) `zh-wl-2025__c0115` – «Hier werden die bisher errechneten Abzüge (Ziffer 18) von den Einkünften abgezogen.»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «22.1 Krankheits- und Unfallkosten»

<a id="22-1-abzug-krankheitskosten"></a>
### Ziff. 22.1 – Krankheits- und Unfallkosten (Code 320) – über Selbstbehalt 5 % des Nettoeinkommens

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten), Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Formular 370 Seite 1, Teil E: Abzug (Code 320) nach Selbstbehalt
- **Rein:** KK-Leistungsabrechnung / Kostenzusammenstellung → Selbstbehalt gemäss Abrechnung (Form. 370 Code 300) · Rechnungen Arzt/Medikamente, Zahnarzt, Pflegepersonal, Spital, verordnete Therapien → Codes 301–305 · Vergütungen KK/Versicherungen → Code 308; Anteil Lebenshaltungskosten (z. B. Ernährung) → Code 311
- **Rechnen:** C (314) = A (317) − B (318); 313 = C und/oder D (Diät-Pauschale 2500, Code 315); Abzug 320 = 313 − 5 % × Ziff. 21 (319), je Spalte
- **Regel:** Selbst getragene Kosten (Franchise/Selbstbehalt, Arzt, Zahnarzt, Pflege, Spital, Therapien) abzüglich Vergütungen Dritter, soweit sie 5 % des Nettoeinkommens (Ziff. 21) übersteigen; Staats- und Bundessteuer je mit eigenem Netto. Nicht abziehbar: Prävention, Fahrkosten, Wellness etc. Diät-Pauschale CHF 2500 bei dauernder lebensnotwendiger Diät. Formular 370 und Belege beilegen.
- **Beachten:** Nicht abziehbar: Prävention (Fitness), Fahrkosten zu Arzt/Spital, eigene Pflege, Wellness, Schönheit, Psychoanalysen
- **Beachten:** Auch für unterhaltene Personen; eine Aufstellung je Steuererklärung, Belege geordnet beilegen
- **Beachten:** Diät-Pauschale nur bei andauernder, lebensnotwendiger Diät (z. B. Zöliakie)
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen nach §§ 26–31 verminderten steuerbaren Einkünfte (Nettoeinkommen, Ziff. 21) übersteigen. Behinderungsbedingte Kosten ohne Selbstbehalt (§ 31 lit. i).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Bund:** Bund: Selbstbehalt 5 % des Nettoeinkommens nach Bundessteuer-Spalte (Art. 33 Abs. 1 lit. h DBG).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «22.1 Krankheits- und Unfallkosten Hilfsblatt 320»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «abzüglich Selbstbehalt (5% von Ziffer 21 der»
  - [StG ZH § 32](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-32.md) `zh-stg-2025__par-32` – «diese 5 Prozent der um die Aufwendungen gemäss §§ 26–31 verminderten steuerbaren Einkünfte übersteigen»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «1. Selbstbehalt gemäss Abrechnung Krankenkasse und Versicherung 300»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «Total der Aufwendungen (A) 317»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «Total der Vergütungen Dritter (B) 318»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «CHF 2500 geltend gemacht wer-»
  - [WL ZH 2025 S. 19](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0117.md) `zh-wl-2025__c0117` – «den sind oder für von ihnen unterhaltene Personen aufgewendet wurden»
  - [WL ZH 2025 S. 19](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0118.md) `zh-wl-2025__c0118` – «Viele Krankenkassen geben auf Verlangen jährlich Kosten- und Prämienzusammenstellungen»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «Total der Auslagen (C) 314»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0001.md) `zh-form-370__c0001` – «Pro Steuererklärung ist nur eine Aufstellung einzureichen.»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «Die Belege sind geordnet»

<a id="22-2-abzug-spenden"></a>
### Ziff. 22.2 – Gemeinnützige Zuwendungen (Code 324)

- **Schlüssel:** `abzug.spenden` (Freiwillige Zuwendungen an gemeinnützige Institutionen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Spendenbescheinigung / Spendenquittung gemeinnützige Organisation (Jahresübersicht) → Spendenbestätigung (Empfänger im Verzeichnis steuerbefreiter Institutionen) + Aufstellung
- **Rein:** Spendenbescheinigungen / Liste aller einzelnen Zuwendungen → Σ Geld und übrige Vermögenswerte (Sachspenden)
- **Rechnen:** Σ ≥ 100 → min(Σ; 20 % × Ziff. 21) je Spalte (Code 324); Σ unter 100 → kein Abzug (Kanton = Bund)
- **Regel:** Freiwillige Leistungen an steuerbefreite juristische Personen mit Sitz in der Schweiz bzw. Bund/Kantone/Gemeinden: mind. CHF 100 pro Jahr (gesamthaft), max. 20 % des Nettoeinkommens (Ziff. 21). Aufstellung beilegen; Belege auf Verlangen.
- **Beachten:** Empfänger ZH: im Verzeichnis der steuerbefreiten Institutionen; andere Kantone: dort abklären
- **Beachten:** Nicht abziehbar: Schulgeld, Arbeitsleistungen, Zuwendungen ins Ausland oder für religiöse Zwecke
- **Beachten:** Liste beilegen; Spendenbescheinigung auf Nachfrage vorweisen
- **Limiten:**
  - Freiwillige Zuwendungen – Mindestbetrag (CHF): Kanton **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen mit Sitz in der Schweiz / öffentliche Hand: abzugsfähig, wenn sie in der Steuerperiode insgesamt mind. CHF 100 erreichen.)** · Bund **CHF 100 (Freiwillige Zuwendungen an steuerbefreite juristische Personen (CH) bzw. Gemeinwesen: mindestens CHF 100 im Steuerjahr)**
  - Freiwillige Zuwendungen – Maximum in % des (Rein-)Einkommens: Kanton **20 % (Freiwillige Zuwendungen insgesamt max. 20 % der um die Aufwendungen nach §§ 26–31 verminderten steuerbaren Einkünfte (Nettoeinkommen).)** · Bund **20 % (Maximum 20 % der um die Aufwendungen (Art. 26–33) verminderten Einkünfte (Nettoeinkommen Ziff. 20))**
- **Bund:** Bund: Art. 33a DBG – ebenfalls mind. CHF 100 und max. 20 % der um die Aufwendungen verminderten Einkünfte.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «22.2 Gemeinnützige Zuwendungen Aufstellung 324»
  - [WL ZH 2025 S. 19](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0122.md) `zh-wl-2025__c0122` – «die Zuwendungen in der Steuerperiode CHF 100 erreichen und soweit sie insgesamt 20%»
  - [WL ZH 2025 S. 19](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0122.md) `zh-wl-2025__c0122` – «des Nettoeinkommens (Ziffer 21 der Steuererklärung) nicht übersteigen.»
  - [ZH Spenden](../../chunks/zh/dauernd/zh-info-spenden/zh-info-spenden__c0003.md) `zh-info-spenden__c0003` – «Die Zuwendungen in einem Jahr gesamthaft mindestens CHF 100 betragen.»
  - [ZH Spenden](../../chunks/zh/dauernd/zh-info-spenden/zh-info-spenden__c0004.md) `zh-info-spenden__c0004` – «Zuwendungen an Organisationen im Kanton Zürich können abgezogen werden, wenn diese im Zürcher Verzeichnis der steuerbefreiten Institutionen aufgelistet sind.»
  - [ZH Spenden](../../chunks/zh/dauernd/zh-info-spenden/zh-info-spenden__c0005.md) `zh-info-spenden__c0005` – «Dann müssen Sie bei der Steuerverwaltung des Kantons nachfragen, in dem die Organisation ihren Sitz hat.»
  - [ZH Spenden](../../chunks/zh/dauernd/zh-info-spenden/zh-info-spenden__c0006.md) `zh-info-spenden__c0006` – «Legen Sie der Steuererklärung deshalb eine Liste mit allen einzelnen Zuwendungen bei.»
  - [ZH Spenden](../../chunks/zh/dauernd/zh-info-spenden/zh-info-spenden__c0007.md) `zh-info-spenden__c0007` – «Sie können zum Beispiel kein Schulgeld abziehen.»
  - [ZH Spenden](../../chunks/zh/dauernd/zh-info-spenden/zh-info-spenden__c0007.md) `zh-info-spenden__c0007` – «Auch freiwillige Arbeitsleistungen können Sie nicht abziehen.»
  - [ZH Spenden](../../chunks/zh/dauernd/zh-info-spenden/zh-info-spenden__c0008.md) `zh-info-spenden__c0008` – «Das gilt auch für Zuwendungen an Organisationen im Ausland.»
  - [ZH Spenden](../../chunks/zh/dauernd/zh-info-spenden/zh-info-spenden__c0007.md) `zh-info-spenden__c0007` – «Sie können nur freiwillige Leistungen von Geld oder anderen Vermögenswerten abziehen.»

<a id="23-berechnung-total"></a>
### Ziff. 23 – Reineinkommen (Code 350)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 21 – 22.1 – 22.2)
- **Rein:** Rechenzeile: Ziff. 21 − Ziff. 22.1 − Ziff. 22.2
- **Rechnen:** = Ziff. 21 − 22.1 − 22.2 je Spalte (Code 350)
- **Regel:** Rechenzeile.
- **Beachten:** Danach Sozialabzüge Ziff. 24.1 bis 24.3 → steuerbares Einkommen Ziff. 25 (Code 390)
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «23. Reineinkommen (Ziffer 21 abzüglich Ziffern 22.1 und 22.2) 350»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «Steuerbares Einkommen gesamt (Ziffer 23 abz. Ziff. 24.1 bis 24.3) 390»

<a id="24-1-sozialabzug-kinder"></a>
### Ziff. 24.1 – Abzug für Kinder in Ihrem Haushalt (Code 370)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Kinder Jg. 2008–2025 oder in beruflicher Erstausbildung); Stand 31.12.2025
- **Rein:** Seite 1 «Kinder in Ihrem Haushalt» → Geburtsdatum, Schule/Lehrfirma, Unterhaltsbeiträge des anderen Elternteils · Lehr-/Schulbestätigung → berufliche Erstausbildung volljähriger Kinder · Urteil/Vereinbarung → elterliche Sorge, Unterhaltsbeiträge
- **Rechnen:** Anzahl Kinder × Kanton 9’300 / Bund 6’800 (Code 370/372); halb 4’650 / 3’400 bei gemeinsamer Sorge ohne Unterhaltsbeiträge (erhalten bzw. abgezogen)
- **Regel:** Staatssteuer CHF 9’300 pro Kind, Bundessteuer CHF 6’800 pro Kind (Verhältnisse am Ende der Steuerperiode). Verheiratete/verwitwete: voll; Alleinerziehende: voll bei alleinigem Sorgerecht bzw. bei gemeinsamem Sorgerecht mit erhaltenen Unterhaltsbeiträgen, sonst halb (CHF 4’650 / 3’400). Volljährige Kinder nur in beruflicher Erstausbildung mit überwiegendem Unterhalt.
- **Beachten:** Stichtag 31. Dezember 2025: minderjährig (Jahrgänge 2008–2025) oder in Erstausbildung, Unterhalt zur Hauptsache
- **Beachten:** Wer Unterhaltszahlungen für das minderjährige Kind leistet, erhält keinen Kinderabzug
- **Beachten:** Kinder ausserhalb des Haushalts: separate Zeile Code 372
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 9'300 (Kinderabzug je Kind: CHF 9'300 (minderjährige Kinder unter elterlicher Sorge/Obhut; volljährige in beruflicher Erstausbildung, deren Unterhalt zur Hauptsache bestritten wird). Bei nicht gemeinsam besteuerten Eltern mit gemeinsamer Sorge hälftig.)** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
- **Bund:** Bund: CHF 6’800 pro Kind (Art. 35 Abs. 1 lit. a DBG).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «Abzug für Kinder in Ihrem Haushalt (gemäss Seite 1) 9’300»
  - [WL ZH 2025 S. 20](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0126.md) `zh-wl-2025__c0126` – «CHF 9’300 pro Kind CHF 6’800 pro Kind»
  - [StG ZH § 34](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-34.md) `zh-stg-2025__par-34` – «a. als Kinderabzug: für minderjährige Kinder unter elterlicher Sorge oder Obhut des Steuerpflichtigen sowie»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «6800 Franken für jedes minderjährige oder in der beruflichen oder schulischen Ausbildung stehende Kind»
  - [Formular 300 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0003.md) `zh-form-300-2025__c0003` – «Kinder der Jahrgänge 2008-2025 oder in beruflicher Erstausbildung stehende Kinder, deren Unterhalt Sie bestreiten:»
  - [WL ZH 2025 S. 20](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0127.md) `zh-wl-2025__c0127` – «das am 31. Dezember 2025 minderjährig ist»
  - [WL ZH 2025 S. 20](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0128.md) `zh-wl-2025__c0128` – «pro Kind (CHF 4’650) pro Kind (CHF 3’400)»
  - [WL ZH 2025 S. 20](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0123.md) `zh-wl-2025__c0123` – «Für die Festsetzung der Sozialabzüge sind die Verhältnisse am Ende der Steuerperiode»
  - [WL ZH 2025 S. 20](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0129.md) `zh-wl-2025__c0129` – «können Sie keinen Kinderabzug geltend machen;»
  - [WL ZH 2025 S. 20](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0128.md) `zh-wl-2025__c0128` – «Sie keine steuerbare Unterhaltsbeiträge für das Kind erhalten.»
  - [WL ZH 2025 S. 20](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0129.md) `zh-wl-2025__c0129` – «Sie keine an den anderen Elternteil geleistete Unterhaltsbeiträge für das Kind abziehen,»

<a id="24-1-sozialabzug-kinder-2"></a>
### Ziff. 24.1 – Abzug für Kinder ausserhalb Ihres Haushaltes (Code 372)

- **Schlüssel:** `sozialabzug.kinder` (Kinder-/Ausbildungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Kinder ausserhalb des Haushalts, Adresse); Nachweis Unterhalt
- **Rein:** Formular S. 1 «Kinder ausserhalb Ihres Haushaltes» → Name, Geburtsdatum, Adresse, Schule/Lehrfirma, voraussichtlich bis · Nachweis geleisteter Unterhaltsbeiträge → volljähriges Kind: Hauptunterhalt belegen · Lehrvertrag bzw. Schulbestätigung → volljähriges Kind in beruflicher Erstausbildung
- **Rechnen:** Je Kind: gem. Sorge ohne Alimentenabzug → ½: Kanton 4'650 / Bund 3'400; Alimente od. keine Sorge → kein Abzug; volljährig + Hauptunterhalt → Kanton 9'300 / Bund 6'800
- **Regel:** Nicht zusammenlebende Eltern: halber Kinderabzug (CHF 4’650 / 3’400) bei gemeinsamem Sorgerecht ohne abgezogene Unterhaltsbeiträge; wer Kinderalimente bezahlt (Ziff. 13.2) oder kein Sorgerecht hat: kein Kinderabzug. Volljährige Kinder in Erstausbildung: ganzer Abzug, wenn Unterhaltsbeiträge den Hauptunterhalt decken.
- **Beachten:** Stichtag 31. Dezember 2025: minderjährig = Jg. 2008–2025 (§ 34 Abs. 2 StG / Art. 35 Abs. 2 DBG)
- **Beachten:** Volljährige (Kanton, ZStB 34.1): Lehrvertrag od. Schule ≥ halbtags, ≥ ein halbes Jahr; auf Unterstützung angewiesen
- **Beachten:** Kinderabzug und Abzug Kinderalimente (Ziff. 13.2) schliessen sich aus
- **Limiten:**
  - Kinderabzug Grundbetrag (CHF): Kanton **CHF 9'300 (Kinderabzug je Kind: CHF 9'300 (minderjährige Kinder unter elterlicher Sorge/Obhut; volljährige in beruflicher Erstausbildung, deren Unterhalt zur Hauptsache bestritten wird). Bei nicht gemeinsam besteuerten Eltern mit gemeinsamer Sorge hälftig.)** · Bund **CHF 6'800 (Kinderabzug pro minderjähriges oder in Ausbildung stehendes Kind; bei getrennter Besteuerung hälftig, wenn gemeinsame elterliche Sorge und keine Unterhaltsbeiträge)**
- **Bund:** Bund: CHF 6’800 bzw. halb CHF 3’400.
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «Abzug für Kinder ausserhalb Ihres Haushaltes (gem. S. 1) 9’300»
  - [WL ZH 2025 S. 20](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0129.md) `zh-wl-2025__c0129` – «können Sie die Hälfte des Kinderabzugs geltend»
  - [Formular 300 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0003.md) `zh-form-300-2025__c0003` – «Vorname, Name Geburtsdatum Adresse Schule / Lehrfirma Voraussichtlich bis»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0130.md) `zh-wl-2025__c0130` – «13.2 Unterhaltsbeiträge für minderjährige Kinder (bis zum Monat der Volljährigkeit)»
  - [ZStB 34.1 (bis 2025) S. 2–3](../../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0005.md) `zh-zstb-34-1-bis-2025__c0005` – «wenn ein Lehrvertrag abgeschlossen»
  - [ZStB 34.1 (bis 2025) S. 2–3](../../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0005.md) `zh-zstb-34-1-bis-2025__c0005` – «mindestens halbtags stattfindet und sich ohne Unterbruch auf wenigs»
  - [ZStB 34.1 (bis 2025) S. 2–3](../../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0005.md) `zh-zstb-34-1-bis-2025__c0005` – «sich in Erstausbildung befindende Kind auf die Unterstützungsleistun»
  - [StG ZH § 34](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-34.md) `zh-stg-2025__par-34` – «werden nach den Verhältnissen am Ende der Steuerperiode oder der Steuerpflicht festgelegt»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «Die Sozialabzüge werden nach den Verhältnissen am Ende der Steuerperiode (Art. 40) oder der Steuerpflicht festgesetzt.»

<a id="24-2-sozialabzug-unterstuetzung"></a>
### Ziff. 24.2 – Abzug für unterstützte Personen (Code 374)

- **Schlüssel:** `sozialabzug.unterstuetzung` (Unterstützungsabzug) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Bestätigung der unterstützten Person (Art, Zeitpunkt, Höhe der Unterstützung) + Zahlungsbelege auf Verlangen
- **Rein:** Bestätigung der unterstützten Person → Art, Zeitpunkt, Höhe der Unterstützung (beilegen) · Zahlungsbelege (Ausland: Post-/Bankbelege) → auf Verlangen · Formular S. 1 → Name, Geburtsjahr, Adresse, Unterstützungsbetrag pro Jahr
- **Rechnen:** Je Person: Unterstützung ≥ 2'800 → Kanton 2'800; ≥ 6'800 → Bund 6'800 (fixer Abzug, nicht die effektive Leistung)
- **Regel:** Für erwerbsunfähige / beschränkt erwerbsfähige Personen, wenn mindestens in der Höhe des Abzugs unterstützt wird: Staat CHF 2’800, Bund CHF 6’800. Nicht für Ehegatten, nicht für Kinder mit Kinderabzug, nicht bei gleichzeitigem Abzug von Alimenten.
- **Beachten:** Nur für erwerbsunfähige/beschränkt erwerbsfähige, unterstützungsbedürftige Personen; Leistungen hinreichend nachweisen
- **Beachten:** Ausgeschlossen: Ehegatte, Kinder mit Kinderabzug, Personen, für die Alimente abgezogen werden
- **Beachten:** Bedürftigkeit (Kanton, ZStB 34.1, Wohnsitz CH): Eink. < 15'000 + Verm. < 50'000; verh. < 22'000 + < 100'000
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'800 (Unterstützungsabzug je erwerbsunfähige/beschränkt erwerbsfähige Person, an deren Unterhalt mindestens in Höhe des Abzugs beigetragen wird (nicht für Ehegatten und Kinder mit Abzug nach lit. a oder § 31 lit. c).)** · Bund **CHF 6'800 (Unterstützungsabzug pro erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mindestens in Höhe des Abzugs unterstützt; nicht für Ehegatten und Kinder mit Kinderabzug)**
- **Bund:** Bund: CHF 6’800 (Art. 35 Abs. 1 lit. b DBG).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «24.2 Abzug für unterstützte Personen Bestätigung»
  - [StG ZH § 34](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-34.md) `zh-stg-2025__par-34` – «b. als Unterstützungsabzug: für erwerbsunfähige oder beschränkt erwerbsfähige Personen, an deren Unterhalt der»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0135.md) `zh-wl-2025__c0135` – «leistung mindestens in der Höhe des Unterstützungsabzuges von CHF 2’800.»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0135.md) `zh-wl-2025__c0135` – «leistung mindestens in der Höhe des Unterstützungsabzuges von CHF 6’800.»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0134.md) `zh-wl-2025__c0134` – «Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der erfolgten Unterstützungen einzureichen»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0134.md) `zh-wl-2025__c0134` – «Zahlungsbelege (bei Zahlungen ins Ausland Post- oder Bankbelege)»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0134.md) `zh-wl-2025__c0134` – «wenn für die gleiche Person Unterhaltsbeiträge (Alimente) in Abzug gebracht werden»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0134.md) `zh-wl-2025__c0134` – «nen gewährt werden, welche infolge körperlicher oder geistiger Gebrechen oder aus anderen»
  - [Formular 300 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0003.md) `zh-form-300-2025__c0003` – «Staatssteuer CHF 2’800 Bundessteuer CHF 6‘800 unterstützen:»
  - [ZStB 34.1 (bis 2025) S. 6](../../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0016.md) `zh-zstb-34-1-bis-2025__c0016` – «Steuerbares Einkommen von weniger als Fr. 15 000 und steuerba»
  - [ZStB 34.1 (bis 2025) S. 6](../../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0016.md) `zh-zstb-34-1-bis-2025__c0016` – «res Vermögen von weniger als Fr. 50 000, falls sie alleinstehend ist»
  - [ZStB 34.1 (bis 2025) S. 6](../../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0016.md) `zh-zstb-34-1-bis-2025__c0016` – «Steuerbares Einkommen von weniger als Fr. 22 000 und steuerba»
  - [ZStB 34.1 (bis 2025) S. 6](../../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0016.md) `zh-zstb-34-1-bis-2025__c0016` – «res Vermögen von weniger als Fr. 100 000, falls sie verheiratet sind»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0134.md) `zh-wl-2025__c0134` – «Die Unterstützungsleistungen sind hinreichend nachzuweisen.»
  - [ZStB 34.1 (bis 2025) S. 6](../../chunks/zh/2025/zh-zstb-34-1-bis-2025/zh-zstb-34-1-bis-2025__c0016.md) `zh-zstb-34-1-bis-2025__c0016` – «Als bedürftig kann eine Person mit Wohnsitz in der Schweiz grund»

<a id="24-3-sozialabzug-verheiratete"></a>
### Ziff. 24.3 – Abzug für Ehegatten / Partner – nur Bundessteuer (Code 365)

- **Schlüssel:** `sozialabzug.verheiratete` (Verheiratetenabzug (Bund)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Zivilstand am 31.12.2025 (Seite 1)
- **Rein:** Formular S. 1 → Zivilstand am 31. Dezember 2025
- **Rechnen:** Kanton: kein Abzug («—») / Bund: 2'800 pauschal bei rechtlich und tatsächlich ungetrennter Ehe → Code 365
- **Regel:** Nur bei der direkten Bundessteuer: CHF 2’800 für in rechtlich und tatsächlich ungetrennter Ehe lebende Steuerpflichtige. Die Staatssteuer kennt keinen Verheiratetenabzug (Tarifsplitting über Verheiratetentarif).
- **Beachten:** Nur Spalte Bundessteuer ausfüllen
- **Beachten:** Eingetragene Partnerschaft wird gleich behandelt wie die Ehe
- **Beachten:** Verhältnisse am Ende der Steuerperiode massgebend (Art. 35 Abs. 2 DBG)
- **Limiten:**
  - Verheiratetenabzug (CHF, Bund): Kanton **n/a – Verheiratetenabzug existiert nur bei der direkten Bundessteuer (Bund-Datei); ZH Staatssteuer kennt Verheiratetentarif statt Abzug.** · Bund **CHF 2'800 (Verheiratetenabzug für Ehepaare in rechtlich und tatsächlich ungetrennter Ehe)**
- **Bund:** Nur Bund: CHF 2’800 (Art. 35 Abs. 1 lit. c DBG).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «24.3 Abzug für Ehegatten / Partn.»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0135.md) `zh-wl-2025__c0135` – «Bei der Bundessteuer gibt es für alle in rechtlich und tatsächlich ungetrennter Ehe lebenden»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «2800 Franken für Ehepaare, die in rechtlich und tatsächlich ungetrennter Ehe leben.»
  - [WL ZH 2025 S. 33](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0212.md) `zh-wl-2025__c0212` – «Die eingetragene Partnerschaft gleichgeschlechtlicher Paare wird»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «Die Sozialabzüge werden nach den Verhältnissen am Ende der Steuerperiode (Art. 40) oder der Steuerpflicht festgesetzt.»
  - [Formular 300 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0002.md) `zh-form-300-2025__c0002` – «Personalien, Berufs- und Familienverhältnisse am 31. Dezember 2025»

<a id="25-berechnung-total"></a>
### Ziff. 25 – Steuerbares Einkommen gesamt (Code 390)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 23 – 24.1 bis 24.3)
- **Rein:** Übertrag Ziff. 23 Reineinkommen (Code 350), je Spalte Staat / Bund · Übertrag Ziff. 24.1–24.3 Sozialabzüge (Codes 370, 372, 374, 365)
- **Rechnen:** Ziff. 23 − (24.1 + 24.2 + 24.3), getrennt Spalte Staatssteuer / Bundessteuer → Code 390
- **Regel:** Rechenzeile.
- **Beachten:** Ziff. 24.3 nur in Spalte Bundessteuer abziehen
- **Beachten:** Teilweise Steuerpflicht: Sozialabzüge anteilmässig (§ 34 Abs. 3 StG / Art. 35 Abs. 3 DBG)
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «25. Steuerbares Einkommen gesamt (Ziffer 23 abz. Ziff. 24.1 bis 24.3) 390»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0132.md) `zh-wl-2025__c0132` – «Reineinkommen (Ziffer 21 abzüglich Ziffern 22.1 und 22.2) 350»
  - [StG ZH § 34](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-34.md) `zh-stg-2025__par-34` – «Bei teilweiser Steuerpflicht werden die Sozialabzüge gemäss Abs. 1 anteilmässig gewährt.»
  - [DBG Art. 35](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-35.md) `bund-dbg-2025__art-35` – «Bei teilweiser Steuerpflicht werden die Sozialabzüge anteilsmässig gewährt.»

<a id="26-1-26-2-berechnung-total"></a>
### Ziff. 26.1 / 26.2 – Davon auf steuerbare Einkünfte in anderen Kantonen (Code 394) bzw. im Ausland (Code 396)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Steuerausscheidung / Ausscheidungsberechnung (nur bei interkantonalem / internationalem Sachverhalt)
- **Rein:** Interkantonale/internationale Steuerausscheidung (eigene Berechnung, sonst durch Steueramt) · Liegenschaftenverzeichnis → Liegenschaften ausserhalb ZH bzw. im Ausland; Betriebsstätten
- **Rechnen:** Anteil von Ziff. 25 gemäss Ausscheidung: andere Kantone → Code 394 (nur Staat), Ausland → Code 396 (Staat und Bund); sonst leer
- **Regel:** Nur bei Einkünften in anderen Kantonen oder im Ausland (Liegenschaften, Betriebsstätten) ausfüllen; sonst leer lassen.
- **Beachten:** 26.1 nur Spalte Staatssteuer, 26.2 Spalten Staat und Bund (Layout Form. 300 S. 3)
- **Beachten:** Gesamtes in- und ausländisches Einkommen deklarieren; ohne eingereichte Ausscheidung nimmt sie das Steueramt vor
- **Beachten:** Teilweise Steuerpflicht: Sozialabzüge anteilmässig, für die Satzbestimmung voll (§ 34 Abs. 3 StG)
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «26.1 Auf steuerbare Einkünfte in anderen Kantonen 394»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «26.2 Auf steuerbare Einkünfte im Ausland 396»
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0015.md) `zh-wl-2025__c0015` – «gesamte in- und ausländische Einkommen und Vermögen zu deklarieren»
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0015.md) `zh-wl-2025__c0015` – «Das Steueramt nimmt die erforderliche Ausscheidung vor, soweit eine solche nicht mit der»
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0015.md) `zh-wl-2025__c0015` – «eine Liegenschaft oder Betriebsstätte erworben oder aufgegeben»
  - [StG ZH § 34](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-34.md) `zh-stg-2025__par-34` – «Für die Satzbestimmung werden sie voll angerech»

<a id="27-berechnung-total"></a>
### Ziff. 27 – Steuerbares Einkommen im Kanton Zürich bzw. in der Schweiz (Code 398)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 25 – 26)
- **Rein:** Übertrag Ziff. 25 (Code 390) und Ziff. 26.1/26.2 (Codes 394/396)
- **Rechnen:** Staat: Ziff. 25 − 26.1 − 26.2 / Bund: Ziff. 25 − 26.2 → Code 398; ohne Ausscheidung = Ziff. 25
- **Regel:** Rechenzeile: massgebend für Staats- und Bundessteuertarif.
- **Beachten:** Kapitalleistungen aus Vorsorge (Ziff. 40) nicht enthalten – gesondert besteuert
- **Quellen:**
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «27. Steuerbares Einkommen im Kanton Zürich bzw. in der Schweiz 398»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «26.1 Auf steuerbare Einkünfte in anderen Kantonen 394»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «25. Steuerbares Einkommen gesamt (Ziffer 23 abz. Ziff. 24.1 bis 24.3) 390»
  - [WL ZH 2025 S. 22–23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0145.md) `zh-wl-2025__c0145` – «Kapitalleistungen werden gesondert vom übrigen Einkommen besteuert.»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0013.md) `zh-form-300-2025__c0013` – «Kapital- aus AHV / IV aus Einrichtung der beruflichen Vorsorge (2. Säule)»

## Vermögen

<a id="30-1-vermoegen-wertschriften-guthaben"></a>
### Ziff. 30.1 – Wertschriften und Guthaben (Code 400) – Total Steuerwert laut Wertschriftenverzeichnis

- **Schlüssel:** `vermoegen.wertschriften_guthaben` (Wertschriften und Guthaben (Bank-/Postkonten, Depot, Krypto)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Wertschriftenverzeichnis (Form. 340) Total Steuerwert (Code 400); Steuerauszug per 31.12.2025
- **Rein:** Bank-Steuerauszug / eSteuerauszug → Steuerwerte und Erträge je Titel/Konto (eSteuerauszug importierbar) · Depotauszug → Bestand 31.12.2025; Kurs gem. ESTV-Kursliste 31.12.2025 · Konto-/Zinsausweis → Saldo 31.12.2025 (voller Forderungsbetrag) · Krypto: Wallet-Auszug per Ende Steuerperiode → ESTV-Jahresendsteuerkurs
- **Rechnen:** Übertrag Form. 340 «Total Steuerwert» (Code 400) = Σ Steuerwerte 31.12.2025; Fremdwährung zu ESTV-Devisenkursen 31.12.2025
- **Regel:** Steuerwert per 31.12.2025 (Schlusskurs letzter Handelstag Dezember, ESTV-Kursliste), Guthaben zum vollen Forderungsbetrag, Kryptowährungen zum ESTV-Jahresendkurs. PK-/Vorsorgeguthaben der 2. Säule und 3a sind steuerfrei und nicht aufzuführen.
- **Beachten:** Kinder Jg. 2008 und jünger mitdeklarieren, Jg. 2007 und älter selbst; berufliche Vorsorge und 3. Säule a nicht aufführen
- **Beachten:** Kennzeichnen: G Geschäfts-, N Nutzniessungsvermögen, E Erbschaft 2025, S Schenkung 2025, Q Beteiligung ≥ 10 %
- **Beachten:** Nichtkotierte Titel: Verkehrswert, sonst vorläufig letzter bekannter Steuerwert (KS Nr. 28)
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.1 Wertschriften und Guthaben Wertschriftenverzeichnis 400»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Total Steuerwert 400»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0156.md) `zh-wl-2025__c0156` – «Für den Steuerwert per Ende des Kalenderjahres ist der Schlusskurs des letzten Börsenhan-»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0159.md) `zh-wl-2025__c0159` – «Guthaben sind mit dem vollen Forderungsbetrag anzugeben.»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0154.md) `zh-wl-2025__c0154` – «sind bis zur Fälligkeit der Leistungen steuerfrei und nicht im Wertschriftenverzeichnis aufzuführen»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0153.md) `zh-wl-2025__c0153` – «Sie können diesen eSteuerauszug in die Online-»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0156.md) `zh-wl-2025__c0156` – «aufgeführten Devisenkursen per 31.12.2025 vorzunehmen»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0159.md) `zh-wl-2025__c0159` – «Für Bitcoin und weitere geläufige Kryptowährungen publiziert die ESTV einen Jahresendsteuer»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0159.md) `zh-wl-2025__c0159` – «Der Nachweis hat mittels Kontoauszug der digitalen Brieftasche»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0154.md) `zh-wl-2025__c0154` – «minderjährigen Kinder des Jahrgangs 2008 und jüngeren»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0154.md) `zh-wl-2025__c0154` – «Vermögen und Ertrag von Personen des Jahrgangs 2007 (und älter) sind durch diese»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0155.md) `zh-wl-2025__c0155` – «mit Q Beteiligungen von mindestens 10 Prozent am Aktien-, Grund- oder Stammkapital»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0155.md) `zh-wl-2025__c0155` – «mit E die Werte, die Sie 2025 aus Erbschaften übernommen haben»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0157.md) `zh-wl-2025__c0157` – «Nichtkotierte Wertpapiere sind zum Verkehrswert anzugeben; wenn dieser nicht bekannt»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0157.md) `zh-wl-2025__c0157` – «Kreisschreiben Nr. 28»

<a id="30-2-vermoegen-bargeld-edelmetalle"></a>
### Ziff. 30.2 – Bargeld, Gold und andere Edelmetalle (Code 404)

- **Schlüssel:** `vermoegen.bargeld_edelmetalle` (Bargeld, Gold, Edelmetalle) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Eigene Aufstellung / Bestandsnachweis per 31.12.
- **Rein:** Eigene Aufstellung Bargeld (CHF und ausländische Banknoten) per 31. Dezember 2025 · Bestandsnachweis Goldmünzen/Edelmetalle per 31. Dezember 2025
- **Rechnen:** Σ Bargeld CHF + (ausländische Banknoten, Goldmünzen, Edelmetalle × Tageskurs per 31. Dezember 2025) → Code 404
- **Regel:** Bargeld und Edelmetalle zum Steuerwert; ausländische Banknoten, Goldmünzen und Edelmetalle zum Tageskurs.
- **Beachten:** Bankguthaben (Sparhefte, Salärkonti) gehören in Ziff. 30.1 (Wertschriftenverzeichnis)
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.2 Bargeld, Gold und andere Edelmetalle»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0138.md) `zh-wl-2025__c0138` – «Ausländische Banknoten, Goldmünzen und Edelmetalle sind zum Tageskurs anzugeben.»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «Steuerwert am 31. Dezember 2025»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0152.md) `zh-wl-2025__c0152` – «Wenn Sie Wertschriften oder Guthaben besitzen, wozu unter anderem auch Sparhefte, Salär»

<a id="30-3-vermoegen-lebensversicherungen"></a>
### Ziff. 30.3 – Lebens- und Rentenversicherungen, Steuerwert (Code 406)

- **Schlüssel:** `vermoegen.lebensversicherungen` (Lebens-/Rentenversicherungen (Rückkaufswert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.) → Steuerwertbescheinigung der Versicherungsgesellschaft per 31.12.2025 (Total)
- **Rein:** Steuerwertbescheinigung der Versicherung per 31.12.2025 → Steuerwert (Rückkaufswert) je Police · Police → Versicherungsgesellschaft, Abschlussjahr, Ablaufsjahr (Formularspalten)
- **Rechnen:** Σ bescheinigte Steuerwerte (Rückkaufswerte) aller rückkaufsfähigen Lebens-/Rentenversicherungen → Total Code 406
- **Regel:** Nur rückkaufsfähige Lebens-/Rentenversicherungen: bescheinigter Steuerwert (Rückkaufswert) einsetzen; Bescheinigung beilegen. Policen der gebundenen Selbstvorsorge (3a) bis zur Fälligkeit steuerfrei.
- **Beachten:** Policen der Säule 3a bis Fälligkeit der Versicherungssumme steuerfrei – nicht einsetzen
- **Beachten:** Rentenversicherung: Rückkaufswert auch nach Rentenbeginn steuerbar; nicht rückkaufsfähige nicht
- **Beachten:** Bescheinigung der Versicherungsgesellschaft beilegen
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.3 Lebens- und Rentenversicherungen (Steuerwert gem. Bescheinigung der Versicherungsges.)»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0139.md) `zh-wl-2025__c0139` – «Rückkaufsfähige Lebens- und Rentenversicherungen unterliegen der Vermögenssteuer. Aus-»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0139.md) `zh-wl-2025__c0139` – «bescheinigten Wert abzustellen.»
  - [StG ZH § 45](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-45.md) `zh-stg-2025__par-45` – «mit ihrem Rückkaufswert. Ihnen gleichgestellt sind rückkaufsfähige Rentenversicherungen.»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0139.md) `zh-wl-2025__c0139` – «Bei rückkaufsfähigen Rentenversicherungen unterliegt der Rückkaufswert auch nach Beginn»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0139.md) `zh-wl-2025__c0139` – «abgeschlossene Vorsorgepolicen sind bis zur Fälligkeit der Versicherungssumme steuerfrei.»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0139.md) `zh-wl-2025__c0139` – «nigung ist mit der Steuererklärung einzureichen»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «Versicherungsgesellschaft Abschlussjahr Ablaufsjahr Steuerwert»

<a id="30-4-vermoegen-fahrzeuge"></a>
### Ziff. 30.4 – Motorfahrzeuge (Code 412)

- **Schlüssel:** `vermoegen.fahrzeuge` (Motorfahrzeuge) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Kaufvertrag / Fahrzeugausweis (Kaufpreis, Kaufjahr)
- **Rein:** Kaufvertrag/Rechnung → Kaufpreis und Kaufjahr (Formularfelder) · Leasingvertrag → Fahrzeug nicht deklarieren
- **Rechnen:** Verkehrswert: Kaufpreis, pro Jahr − 40 % des Restwertes (Regel); Σ aller privaten Motorfahrzeuge → Code 412
- **Regel:** Aktueller Verkehrswert; in der Regel Wertverminderung 40 % des Restwertes pro Jahr. Geleaste Fahrzeuge nicht deklarieren.
- **Beachten:** Nur private Fahrzeuge; geleaste nicht deklarieren
- **Beachten:** Massgebend ist der aktuelle Verkehrswert (§ 39 Abs. 1 StG); 40 %-Regel ist Richtwert («in der Regel»)
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.4 Motorfahrzeuge: Kaufpreis: Kaufjahr: 412»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0140.md) `zh-wl-2025__c0140` – «beträgt die Wertverminderung pro Jahr 40% des Restwertes. Nicht deklariert werden müssen»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0140.md) `zh-wl-2025__c0140` – «Das private Motorfahrzeug ist mit dem aktuellen Verkehrswert zu deklarieren.»
  - [StG ZH § 39](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-39.md) `zh-stg-2025__par-39` – «Das Vermögen wird zum Verkehrswert bewertet.»

<a id="30-5-vermoegen-erbschaften-beteiligungen"></a>
### Ziff. 30.5 – Geschäfts- und Korporationsanteile (Code 414)

- **Schlüssel:** `vermoegen.erbschaften_beteiligungen` (Anteile an unverteilten Erbschaften, Geschäftsvermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Aufstellung (Beteiligungsquote, Steuerwert)
- **Rein:** Aufstellung über Kapital und Ertrag der Geschäfts-/Korporationsanteile (Beilage) · Gesellschafts-/Korporationsunterlagen → eigene Beteiligungsquote
- **Rechnen:** Σ (Wert Geschäft bzw. Korporation × eigene Beteiligungsquote) → Code 414
- **Regel:** Anteilmässig nach Beteiligungsquote; Anteile an unverteilten Erbschaften: Vermögen mit Steuerwert per 31.12. anteilmässig, Belege beilegen.
- **Beachten:** Unverteilte Erbschaft: Liegenschaftsanteil → Liegenschaftenverzeichnis, Wertschriften/Guthaben → WV
- **Beachten:** Erbengemeinschaft: Aufstellung (Erblasser, Erben/Erbquoten, Vermögen, Erträge, Schulden) beilegen
- **Beachten:** Anteile an Kapitalgesellschaften/Genossenschaften ins WV (≥ 10 % mit «Q» kennzeichnen)
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.5 Geschäfts-/Korporationsanteile Aufstellung 414»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0140.md) `zh-wl-2025__c0140` – «Geschäfts- und Korporationsanteile sind von den Inhabern anteilmässig entsprechend ihrer»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0150.md) `zh-wl-2025__c0150` – «Das Vermögen aus unverteilten Erbschaften ist mit dem per 31.12. gültigen Steuerwert an-»
  - [WL ZH 2025 S. 31](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0205.md) `zh-wl-2025__c0205` – «Inhaber von Geschäfts- und Korporationsanteilen • Aufstellung über Kapital und Ertrag.»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0150.md) `zh-wl-2025__c0150` – «Liegenschaften ist im Liegenschaftenverzeichnis einzutragen»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0150.md) `zh-wl-2025__c0150` – «Wertschriften und Guthaben sind im Wertschriftenverzeichnis aufzuführen»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0151.md) `zh-wl-2025__c0151` – «Namen, Adressen und Erbquoten sämtlicher Erben»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0151.md) `zh-wl-2025__c0151` – «Auflistung sämtlicher Schulden und Schuldzinsen der unverteilten Erbschaft»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0155.md) `zh-wl-2025__c0155` – «mit Q Beteiligungen von mindestens 10 Prozent am Aktien-, Grund- oder Stammkapital»

<a id="30-6-vermoegen-uebrige"></a>
### Ziff. 30.6 – Übrige Vermögenswerte (Code 416)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Eigene Aufstellung (Schätzwert / Versicherungswert)
- **Rein:** Eigene Aufstellung mit näherer Bezeichnung (z. B. Gemälde, Sammlungen, Schmuck, Boote, Flugzeuge) · Kaufbelege/Schätzungen → Verkehrswert per 31. Dezember 2025
- **Rechnen:** Σ Verkehrswerte per 31. Dezember 2025 (§ 39 Abs. 1 StG) → Code 416
- **Regel:** z. B. Gemälde, Sammlungen, Kunst- und Schmuckgegenstände, Boote, Flugzeuge; nähere Bezeichnung angeben. Hausrat ist steuerfrei.
- **Beachten:** Hausrat und persönliche Gebrauchsgegenstände nicht besteuert (§ 38 Abs. 4 StG)
- **Beachten:** Nutzniessungsvermögen versteuert der Nutzniesser (§ 38 Abs. 2 StG)
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.6 Übrige Vermögenswerte; nähere Bezeichnung: 416»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0140.md) `zh-wl-2025__c0140` – «Übrige Vermögenswerte sind zum Beispiel Gemälde- und andere Sammlungen, Kunst- und»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0140.md) `zh-wl-2025__c0140` – «Der Hausrat ist steuerfrei.»
  - [StG ZH § 39](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-39.md) `zh-stg-2025__par-39` – «Das Vermögen wird zum Verkehrswert bewertet.»
  - [StG ZH § 38](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-38.md) `zh-stg-2025__par-38` – «Hausrat und persönliche Gebrauchsgegenstände werden nich t besteuert.»
  - [StG ZH § 38](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-38.md) `zh-stg-2025__par-38` – «Nutzniessungsvermögen wird dem Nutzniesser zugerechnet.»

<a id="31-1-vermoegen-liegenschaften"></a>
### Ziff. 31.1 – Liegenschaften zum Verkehrswert besteuert (Code 421) – Total Liegenschaftenverzeichnis

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftenverzeichnis (Form. 350) Seite 1: Total Steuerwert Verkehrswert (Code 3951) – Bewertung des Gemeindesteueramts
- **Rein:** Liegenschaftenbewertung des Gemeindesteueramts → Vermögenssteuerwert EFH/Stockwerkeigentum zu Wohnzwecken · Mietzinseinnahmen 2025 → Bruttojahresertrag (MFH, Geschäftshaus, StWE zu Geschäftszwecken) · Liegenschaftenverzeichnis Form. 350 → Spalte Verkehrswert, Total Code 3951
- **Rechnen:** Σ Steuerwerte Form. 350 (Code 3951) → Code 421: EFH/StWE Wohnen = Bewertung Gemeinde; MFH/Geschäft = Bruttojahresertrag 2025 × 100 / 7,05
- **Regel:** Steuerwert Einfamilienhaus/Stockwerkeigentum gemäss zugestellter Bewertung des Gemeindesteueramts (Weisung ZStB 21.1); Mehrfamilien-/Geschäftshaus = Ertragswert (Bruttojahresertrag x 100 / 7,05). Nutzniessung/Wohnrecht: voller Wert beim Berechtigten bzw. Eigentümer.
- **Beachten:** Bruttoertrag inkl. Marktmietwert eigengenutzter Wohnung, ohne Heizung, Warmwasser, Kehricht-, Wasser-/Abwassergebühren
- **Beachten:** Nutzniessung: 100 % beim Nutzniesser; Wohnrecht: 100 % beim Eigentümer
- **Beachten:** Keine Bewertung erhalten → Gemeindesteueramt fragen; auch ausserkantonale/ausländische Liegenschaften erfassen
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «31.1 Zum Verkehrswert besteuert Liegenschaftenverzeichnis 421»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0196.md) `zh-wl-2025__c0196` – «tenbewertung wird Ihnen vom Gemeindesteueramt der Liegenschaftengemeinde zugestellt.»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0198.md) `zh-wl-2025__c0198` – «Vermögenssteuerwert = Bruttojahresertrag x 100 / 7,05»
  - [Formular 350 ZH S. 1](../../chunks/zh/2025/zh-form-350/zh-form-350__c0002.md) `zh-form-350__c0002` – «Total 3952 13213211 3951 113213211»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0197.md) `zh-wl-2025__c0197` – «folgt: Vermögenssteuerwert = Ertragswert.»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0198.md) `zh-wl-2025__c0198` – «Für die Berechnung des Vermögenssteuerwertes ist der Bruttojahresertrag des Jahres 2025»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0198.md) `zh-wl-2025__c0198` – «der Liegenschaft (einschliesslich Marktmietwert einer allfällig selbstgenutzten Wohnung, jedoch»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0196.md) `zh-wl-2025__c0196` – «Falls Sie noch keine Bewertung erhalten haben, erkundigen Sie sich bitte beim zuständigen»
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0015.md) `zh-wl-2025__c0015` – «gesamte in- und ausländische Einkommen und Vermögen zu deklarieren»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0195.md) `zh-wl-2025__c0195` – «Als Vermögenssteuerwert von Einfamilienhäusern und Stockwerkeigentum zu Wohnzwecken»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0197.md) `zh-wl-2025__c0197` – «Geschäftshäusern sowie Stockwerkeigentum zu Geschäftszwecken»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0200.md) `zh-wl-2025__c0200` – «ist der Vermögenssteuerwert zu 100% durch die nutzniessungsberechtigte Person zu versteuern»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0200.md) `zh-wl-2025__c0200` – «ist der Vermögenssteuerwert zu 100% durch den Eigentümer zu versteuern»
  - [Formular 350 ZH S. 1](../../chunks/zh/2025/zh-form-350/zh-form-350__c0001.md) `zh-form-350__c0001` – «Ertragswert Verkehrswert Land- oder Forstwirtschaft»

<a id="31-2-vermoegen-liegenschaften"></a>
### Ziff. 31.2 – Liegenschaften zum Ertragswert besteuert – Land- oder Forstwirtschaft (Code 422)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Liegenschaftenverzeichnis (Form. 350) Seite 1: Total Ertragswert (Code 3952)
- **Rein:** Liegenschaftenverzeichnis Form. 350 → Spalte Ertragswert Land-/Forstwirtschaft, Total Code 3952
- **Rechnen:** Σ Ertragswerte land-/forstwirtschaftlicher Liegenschaften inkl. erforderlicher Gebäude (Form. 350 Code 3952) → Code 422
- **Regel:** Land- und forstwirtschaftliche Liegenschaften zum Ertragswert; Total aus dem Liegenschaftenverzeichnis übertragen.
- **Beachten:** Auch landwirtschaftlich genutzte Flächen des erweiterten Umschwungs von Wohn-/Geschäftsliegenschaften
- **Beachten:** Veräusserung/Entfremdung: ergänzende Vermögenssteuer auf Differenz Ertrags-/Verkehrswert (max. 20 Jahre, 1 ‰)
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «31.2 Zum Ertragswert besteuert (Land- oder Forstwirtschaft) Liegenschaftenverzeichnis 422»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0200.md) `zh-wl-2025__c0200` – «Das Total der Vermögenssteuerwerte von land- und forstwirtschaftlichen Liegen-»
  - [Formular 350 ZH S. 1](../../chunks/zh/2025/zh-form-350/zh-form-350__c0002.md) `zh-form-350__c0002` – «Total 3952 13213211 3951 113213211»
  - [StG ZH § 40](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-40.md) `zh-stg-2025__par-40` – «Land- oder forstwirtschaftlich genutzte Grundstücke werden mit Einschluss der erforderlichen Gebäude zum Ertragswert bewertet.»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0199.md) `zh-wl-2025__c0199` – «sowie landwirtschaftlich genutzte Flächen des erweiterten Umschwungs von Wohn- und»
  - [StG ZH § 43](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-43.md) `zh-stg-2025__par-43` – «jedoch höchstens für 20 Jahre, erhoben»
  - [StG ZH § 43](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-43.md) `zh-stg-2025__par-43` – «wird bezogen zum Steuersatz von 1 Promille»
  - [Formular 350 ZH S. 1](../../chunks/zh/2025/zh-form-350/zh-form-350__c0001.md) `zh-form-350__c0001` – «Ertragswert Verkehrswert Land- oder Forstwirtschaft»
  - [StG ZH § 41](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-41.md) `zh-stg-2025__par-41` – «der bisherigen land- oder forstwirtschaftlichen Bewirtschaftung entfremdet, wird vom Eigentümer eine ergänzende Vermögenssteuer erhoben»

<a id="32-vermoegen-uebrige"></a>
### Ziff. 32 – Eigenkapital Selbständigerwerbender ohne Geschäftswertschriften (Code 430)

- **Schlüssel:** `vermoegen.uebrige` (Übrige Vermögenswerte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Jahresrechnung Selbständigerwerbende (Bilanz, Erfolgsrechnung, Einnahmen-Ausgaben-Rechnung, Privatkonten) → Hilfsblatt A (Eigenkapital Ziff. 10.4 bzw. 14.4)
- **Rein:** Hilfsblatt A Ziff. 10.4 (kaufmännische Buchführung) → Eigenkapital · Hilfsblatt A Ziff. 14.4 (vereinfachte Buchführung) → Eigenkapital · Jahresrechnung (Bilanz, Erfolgsrechnung, Anhang) bzw. Aufstellung Aktiven/Passiven → Beilage
- **Rechnen:** Übertrag Eigenkapital Hilfsblatt A (Ziff. 10.4 bzw. 14.4) ohne Geschäftswertschriften → Code 430
- **Regel:** Eigenkapital laut Hilfsblatt A (kaufmännische Buchführung Ziff. 10.4, vereinfachte Ziff. 14.4) ohne Geschäftswertschriften (diese im WV mit Code G).
- **Beachten:** Geschäftswertschriften nicht hier, sondern im WV mit «G» kennzeichnen
- **Beachten:** Immaterielle Güter und bewegliches Geschäftsvermögen zum Einkommenssteuerwert (§ 39 Abs. 2 StG)
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «32. Eigenkapital Selbständigerwerbender ohne Geschäftswertschriften Hilfsblatt A 430»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0141.md) `zh-wl-2025__c0141` – «Selbständigerwerbende mit kaufmännischer Buchführung übertragen das Eigenkapital laut»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0141.md) `zh-wl-2025__c0141` – «Selbständigerwerbende mit vereinfachter Buchführung übertragen das Eigenkapital laut Hilfs»
  - [WL ZH 2025 S. 31](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0204.md) `zh-wl-2025__c0204` – «Unterzeichnete Jahresrechnung (Bilanz, Erfolgsrechnung und Anhang) für Steuerpflichtige»
  - [WL ZH 2025 S. 31](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0204.md) `zh-wl-2025__c0204` – «Aufstellungen über Aktiven und Passiven, Einnahmen und Ausgaben sowie Privatentnahmen»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0155.md) `zh-wl-2025__c0155` – «mit G das Geschäftsvermögen»
  - [StG ZH § 39](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-39.md) `zh-stg-2025__par-39` – «Immaterielle Güter und bewegliches Vermögen, die zum Geschäftsvermögen der steuerpflichtigen Person gehören»

<a id="33-berechnung-total"></a>
### Ziff. 33 – Total der Vermögenswerte (Code 460)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Summe Ziff. 30–32)
- **Rein:** Übertrag Ziff. 30.1–30.6, 31.1, 31.2 und 32
- **Rechnen:** Σ Ziff. 30.1 bis 30.6 + 31.1 + 31.2 + 32 → Code 460
- **Regel:** Rechenzeile.
- **Beachten:** Gesamtes in- und ausländisches Vermögen einbeziehen; Ausscheidung erst in Ziff. 36
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «33. Total der Vermögenswerte 460»
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0015.md) `zh-wl-2025__c0015` – «gesamte in- und ausländische Einkommen und Vermögen zu deklarieren»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.1 Wertschriften und Guthaben Wertschriftenverzeichnis 400»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0011.md) `zh-form-300-2025__c0011` – «30.6 Übrige Vermögenswerte; nähere Bezeichnung: 416»

<a id="34-schulden-privat"></a>
### Ziff. 34 – Schulden (Code 470)

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung) → Schuldenverzeichnis (Form. 355) Total Privatschulden (Code 3200); Saldobestätigung Bank per 31.12.2025
- **Rein:** Saldo-/Zinsbestätigung Bank per 31.12.2025 → Hypotheken, Kredite (Form. 355) · Darlehensvertrag + Saldo 31.12.2025 → private Darlehen (Gläubiger mit Adresse, Zinssatz) · Schuldenverzeichnis Form. 355 → Total Privatschulden Code 3200
- **Rechnen:** Σ Privatschulden inkl. Grundpfandschulden am 31. Dezember (Form. 355 Code 3200) → Code 470; Zinsen Code 3201 → Ziff. 12
- **Regel:** Alle Privatschulden inkl. Grundpfandschulden per 31.12.2025 mit Gläubiger (genaue Adresse), Betrag und Zinssatz im Schuldenverzeichnis aufführen und Total übertragen; Verzeichnis beilegen.
- **Beachten:** Solidar-/Bürgschaftsschulden nur soweit selbst zu tragen (§ 46 StG)
- **Beachten:** Gläubiger mit genauer Adresse und Zinssatz zwingend; vollständiges Verzeichnis beilegen
- **Beachten:** Unverteilte Erbschaft: Schulden und Schuldzinsen anteilmässig
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «34. Schulden Schuldenverzeichnis 470»
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0002.md) `zh-form-355__c0002` – «Total Privatschulden / private Schuldzinsen 3200 / 3201»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0141.md) `zh-wl-2025__c0141` – «einzureichen. Unerlässlich ist insbesondere die Angabe des Gläubigers mit genauer Adresse»
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0001.md) `zh-form-355__c0001` – «Privatschulden inkl. Grundpfandschulden Schuld am 31. Dezember Schuldzinsen»
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0002.md) `zh-form-355__c0002` – «Steuererklärung Seite 4, Ziffer 34 Steuererklärung Seite 3, Ziffer 12»
  - [StG ZH § 46](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-46.md) `zh-stg-2025__par-46` – «andere Schulden, wie Solidar- und Bürgschaftsschulden, nur insoweit, als sie vom Steuerpflichtigen getragen werden müssen»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0150.md) `zh-wl-2025__c0150` – «Die Schulden und Schuldzinsen der unverteilten Erbschaft sind anteilmässig in der Steuer»

<a id="35-berechnung-total"></a>
### Ziff. 35 – Steuerbares Vermögen gesamt (Code 490)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 33 – 34)
- **Rein:** Übertrag Ziff. 33 (Code 460) und Ziff. 34 (Code 470)
- **Rechnen:** Ziff. 33 − Ziff. 34 → Code 490 (Reinvermögen)
- **Regel:** Rechenzeile.
- **Beachten:** Unterjährige Steuerpflicht: Vermögenssteuer nach Dauer der Steuerpflicht
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «35. Steuerbares Vermögen gesamt 490»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «34. Schulden Schuldenverzeichnis 470»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «33. Total der Vermögenswerte 460»
  - [StG ZH § 38](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-38.md) `zh-stg-2025__par-38` – «Der Vermögenssteuer unterliegt das gesamte Reinvermögen.»
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0014.md) `zh-wl-2025__c0014` – «Die Vermögenssteuer wird nach der Dauer der Steuerpflicht erhoben.»

<a id="36-1-36-2-berechnung-total"></a>
### Ziff. 36.1 / 36.2 – Davon auf steuerbare Vermögenswerte in anderen Kantonen (Code 494) bzw. im Ausland (Code 496)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Steuerausscheidung (nur bei interkantonalem / internationalem Sachverhalt)
- **Rein:** Steuerausscheidung (eigene Berechnung, sonst durch Steueramt) · Liegenschaftenverzeichnis → Liegenschaften ausserhalb ZH bzw. im Ausland
- **Rechnen:** Anteil von Ziff. 35 gemäss Ausscheidung: andere Kantone → Code 494, Ausland → Code 496; sonst leer
- **Regel:** Nur bei Vermögen in anderen Kantonen oder im Ausland ausfüllen.
- **Beachten:** Gesamtes in- und ausländisches Vermögen trotzdem vollständig deklarieren
- **Beachten:** Ohne eingereichte Ausscheidung nimmt das Steueramt sie vor
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «36.1 Auf steuerbare Vermögenswerte in anderen Kantonen 494»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «36.2 Auf steuerbare Vermögenswerte im Ausland 496»
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0015.md) `zh-wl-2025__c0015` – «gesamte in- und ausländische Einkommen und Vermögen zu deklarieren»
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0015.md) `zh-wl-2025__c0015` – «Das Steueramt nimmt die erforderliche Ausscheidung vor, soweit eine solche nicht mit der»

<a id="37-berechnung-total"></a>
### Ziff. 37 – Steuerbares Vermögen im Kanton Zürich (Code 498)

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile (Ziff. 35 – 36)
- **Rein:** Übertrag Ziff. 35 (Code 490) und Ziff. 36.1/36.2 (Codes 494/496)
- **Rechnen:** Ziff. 35 − 36.1 − 36.2 → Code 498; Tarif: 0 ‰ auf ersten 80'000 (Grundtarif) / 159'000 (Verheiratetentarif), kein Abzug eintragen
- **Regel:** Rechenzeile: massgebend für den Vermögenssteuertarif.
- **Beachten:** Bund: keine Vermögenssteuer
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 80'000 (Vermögenssteuer Grundtarif: 0 ‰ für die ersten CHF 80'000 steuerbares Vermögen (steuerfrei; kein separater Sozialabzug).)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 159'000 (Verheiratetentarif (auch Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern): 0 ‰ für die ersten CHF 159'000 steuerbares Vermögen.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «37. Steuerbares Vermögen im Kanton Zürich 498»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «35. Steuerbares Vermögen gesamt 490»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «36.1 Auf steuerbare Vermögenswerte in anderen Kantonen 494»
  - [StG ZH § 47](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-47-t1.md) `zh-stg-2025__par-47-t1` – «0‰ für die ersten Fr. 80 000»
  - [StG ZH § 47](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-47-t2.md) `zh-stg-2025__par-47-t2` – «0‰ für die ersten Fr. 159 000»

<a id="tarif-vermoegen-sozialabzug"></a>
### Ziff. — (Tarif) – Steuerfreies Vermögen: kein Formularfeld, ergibt sich aus der 0‰-Stufe des Vermögenssteuertarifs

- **Schlüssel:** `vermoegen.sozialabzug` (Steuerfreie Beträge / Sozialabzüge auf dem Vermögen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → –
- **Rein:** Kein Beleg; ergibt sich aus Ziff. 37 und Zivilstand/Kinder (Seite 1)
- **Rechnen:** Nichts eintragen; 0 ‰ auf den ersten 80'000 (Grundtarif) bzw. 159'000 (Verheiratetentarif) von Ziff. 37
- **Regel:** Das Formular 300 enthält keine Zeile für einen Vermögens-Sozialabzug. Der steuerfreie Betrag ergibt sich aus der ersten Tarifstufe (0‰): Grundtarif Fr. 80 000, Verheiratetentarif Fr. 159 000. Es ist nichts einzutragen. Der Verheiratetentarif gilt auch für Alleinstehende, die mit Kindern im Sinn von § 34 Abs. 1 lit. a zusammenleben (§ 47 Abs. 2).
- **Beachten:** Verheiratetentarif auch für Verwitwete, Getrennte, Geschiedene, Ledige, die mit Kindern zusammenleben
- **Beachten:** Nicht gemeinsam besteuerte Eltern, je ½ Kinderabzug: Verheiratetentarif nur, wer Kindesunterhalt hauptsächlich trägt
- **Beachten:** Verhältnisse am Ende der Steuerperiode massgebend (§ 47 Abs. 3 StG); Bund: keine Vermögenssteuer
- **Limiten:**
  - Steuerfreies Vermögen / Sozialabzug alleinstehend (CHF): Kanton **CHF 80'000 (Vermögenssteuer Grundtarif: 0 ‰ für die ersten CHF 80'000 steuerbares Vermögen (steuerfrei; kein separater Sozialabzug).)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
  - Steuerfreies Vermögen / Sozialabzug gemeinsam Besteuerte (CHF): Kanton **CHF 159'000 (Verheiratetentarif (auch Verwitwete, Getrennte, Geschiedene, Ledige mit Kindern): 0 ‰ für die ersten CHF 159'000 steuerbares Vermögen.)** · Bund **n/a – Die direkte Bundessteuer erfasst nur das Einkommen (Art. 1 ff. DBG); Vermögenssteuer ist rein kantonal.**
- **Bund:** Bund: keine Vermögenssteuer.
- **Bemerkung:** Beträge aus § 47 StG (Fassung Nachtrag 127, Stand 1.1.2025); VKP 2024 (zh-vkp-2024-zstb) nennt dieselben Werte.
- **Quellen:**
  - [StG ZH § 47](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-47-t1.md) `zh-stg-2025__par-47-t1` – «0‰ für die ersten Fr. 80 000»
  - [StG ZH § 47](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-47-t2.md) `zh-stg-2025__par-47-t2` – «0‰ für die ersten Fr. 159 000»
  - [StG ZH § 47](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-47-t2.md) `zh-stg-2025__par-47-t2` – «sowie für verwitwete, gerichtlich oder tatsächlich getrennt lebende, geschiedene und ledige Steuerpflichtige, die mit Kindern»
  - [StG ZH § 47](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-47-t2.md) `zh-stg-2025__par-47-t2` – «hat derjenige Elternteil Anspruch auf den Verheiratetentarif, der den Unterhalt des Kindes aus seinen versteuer»
  - [StG ZH § 47](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-47-t2.md) `zh-stg-2025__par-47-t2` – «Der Tarif wird nach den Verhältnissen am Ende der Steuerperiode oder der Steuerpflicht festgelegt.»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «37. Steuerbares Vermögen im Kanton Zürich 498»
  - [StG ZH § 47](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-47-t2.md) `zh-stg-2025__par-47-t2` – «Bei nicht gemeinsam besteuerten Eltern, die mit Kindern unte r gemeinsamer elterlicher Sorge zusammenleben und denen der Kinderabzug je zur Hälfte zusteht»

## Weitere Angaben

<a id="40-einkommen-kapitalleistung-vorsorge"></a>
### Ziff. 40 – Kapitalleistungen aus Vorsorge (Code 510)

- **Schlüssel:** `einkommen.kapitalleistung_vorsorge` (Kapitalleistungen aus Vorsorge (separate Besteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Bescheinigung über Kapitalleistung aus Vorsorge (Pensionskasse, Freizügigkeit, Säule 3a, Todesfall-/Invaliditätskapital) → Auszahlungsbescheinigung der Vorsorgeeinrichtung (Datum, Betrag, Art)
- **Rein:** Auszahlungsbescheinigung (AHV/IV, 2. Säule, Freizügigkeitskonto/-police, Säule 3a) → Datum, Betrag, Art · Bei mehreren Leistungen: Aufstellung beilegen, Gesamtbetrag eintragen · Bescheinigung Arbeitgeber-Kapitalleistung mit Vorsorgecharakter bzw. Kapital bei Tod/bleibenden Nachteilen → Betrag
- **Rechnen:** Σ Kapitalleistungen 2025 (100 %) → Code 510; Steuer gesondert: Kanton Satz von 1/20 als Jahresleistung, einfache Staatssteuer mind. 2 % / Bund 1/5 Tarif
- **Regel:** Sämtliche 2025 ausgerichteten Kapitalleistungen aus AHV/IV, 2. Säule, Freizügigkeit, Säule 3a sowie Arbeitgeberleistungen mit Vorsorgecharakter und Kapitalzahlungen bei Tod/bleibenden Nachteilen angeben (bei mehreren Gesamtbetrag + Aufstellung). 100 % steuerbar, gesondert besteuert (Staat: Satz einer Jahresleistung von 1/20, mind. 2 %; Bund: 1/5 der Tarife). Steuerfrei: Stellenwechsel-Leistungen, die innert Jahresfrist in eine andere Vorsorgeeinrichtung eingekauft werden.
- **Beachten:** Steuerfrei: Stellenwechsel-Leistung, die innert Jahresfrist in eine andere 2.-Säule-Einrichtung eingebracht wird
- **Beachten:** Gesondert vom übrigen Einkommen besteuert; keine Sozialabzüge, stets volle Jahressteuer
- **Beachten:** Auszahlungsdatum angeben (Formularfeld)
- **Limiten:**
  - Kapitalleistungen aus Vorsorge – Steuersatz/Tarif (separate Jahressteuer): Kanton **Kapitalleistungen aus Vorsorge (§ 22) gesondert zum Satz, der sich bei einer jährlichen Leistung von einem Zwanzigstel der Kapitalleistung ergäbe (Rentensatz 1/20); einfache Staatssteuer mindestens 2 % (Mindestsatz); stets volle Jahressteuer; keine Sozialabzüge nach § 34.** · Bund **Kapitalleistungen aus Vorsorge (Art. 22 DBG) und Zahlungen bei Tod/bleibenden Nachteilen werden gesondert besteuert (volle Jahressteuer, Steuerjahr des Zuflusses); Steuer = ein Fünftel der Tarife nach Art. 36 Abs. 1, 2 und 2bis erster Satz DBG (Bruchteil 1/5); keine Sozialabzüge.**
- **Bund:** Bund: Steuer zu einem Fünftel der Tarife (Art. 36 Abs. 1 und 2 DBG).
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0013.md) `zh-form-300-2025__c0013` – «aus Einrichtung der beruflichen Vorsorge (2. Säule)»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0144.md) `zh-wl-2025__c0144` – «Kapitalleistungen aus Vorsorge sind zu 100% steuerbar.»
  - [WL ZH 2025 S. 22–23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0145.md) `zh-wl-2025__c0145` – «Die Steuer wird zu einem Fünftel der Tarife nach Artikel 36 Abs. 1 und 2 DBG berechnet.»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0144.md) `zh-wl-2025__c0144` – «Sind mehrere Kapitalleistungen aus Vorsorge angefallen, ist eine Aufstellung einzureichen»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0143.md) `zh-wl-2025__c0143` – «Arbeitgebers mit Vorsorgecharakter und sämtliche Kapitalzahlungen bei Tod und für bleibende»
  - [WL ZH 2025 S. 22–23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0145.md) `zh-wl-2025__c0145` – «eine jährliche Leistung von einem Zwanzigstel der Kapitalleistung(en)»
  - [WL ZH 2025 S. 22–23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0145.md) `zh-wl-2025__c0145` – «die einfache Staatssteuer beträgt jedoch mindestens 2%»
  - [WL ZH 2025 S. 22–23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0145.md) `zh-wl-2025__c0145` – «Jahresfrist zum Einkauf in eine andere Einrichtung der beruflichen Vorsorge (2. Säule)»
  - [WL ZH 2025 S. 22–23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0145.md) `zh-wl-2025__c0145` – «Kapitalleistungen werden gesondert vom übrigen Einkommen besteuert.»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0013.md) `zh-form-300-2025__c0013` – «aus Freizügigkeitskonto / ‑police aus anerkannter Form der geb. Selbstvorsorge (3. Säule a)»

<a id="50-1-50-2-info-schenkungen-erbschaften"></a>
### Ziff. 50.1 / 50.2 – Schenkungen, Erbvorbezug, Erbschaften, Beteiligung an Erbengemeinschaften: erhalten (Code 516) / ausgerichtet (Code 519)

- **Schlüssel:** `info.schenkungen_erbschaften` (Erhaltene/ausgerichtete Schenkungen und Erbschaften (Angaben)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Erbschaft/Schenkung (Erbteilungsvertrag, Nachlassinventar, Schenkungsvertrag, Erbbescheinigung) → Schenkungsvertrag / Erbbescheinigung / Teilungsvertrag (Datum, Wert, Name, Verwandtschaftsgrad)
- **Rein:** Schenkungs-/Erbvorbezugsvertrag → Datum, Wert, Name, Adresse, Verwandtschaftsgrad · Erbbescheinigung/Teilungsvertrag → Erbanfall 2025 (Datum, Wert) · Unverteilte Erbschaft: Aufstellung (Erblasser, Erben/Erbquoten, Vermögen, Erträge, Schulden)
- **Rechnen:** Je Vorgang Datum + Wert: erhalten → Code 516, ausgerichtet → Code 519; Vermögen per Ende 2025 und Erträge der Steuerperiode normal deklarieren
- **Regel:** Alle 2025 erhaltenen bzw. ausgerichteten Schenkungen, Erbvorbezüge und Vermögensanfälle von Todes wegen angeben (auch bei nicht erfolgter Erbteilung). Besondere Schenkungssteuererklärung nicht nötig bei Zuwendungen an Ehegatten/Partner, Nachkommen und Gelegenheitsgeschenken bis CHF 5’000.
- **Beachten:** Schenkungssteuererklärung innert dreier Monate – entfällt bei Ehegatte/Partner, Nachkommen, Gelegenheitsgeschenk ≤ 5'000
- **Beachten:** Datum steuert Vermögenssteuer: Erbgang → Erblasser bis Erbgang, Erbe danach; Schenkung → ganzes Jahr Beschenkter
- **Beachten:** Auch bei noch nicht erfolgter Erbteilung angeben
- **Quellen:**
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0014.md) `zh-form-300-2025__c0014` – «2025 erhalten von Wert: 516»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0146.md) `zh-wl-2025__c0146` – «Hier sind alle Schenkungen, Erbvorbezüge und Vermögensanfälle von Todes wegen (auch»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0148.md) `zh-wl-2025__c0148` – «bei Gelegenheitsgeschenken, die den Wert von je CHF 5’000 nicht übersteigen.»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0014.md) `zh-form-300-2025__c0014` – «Name, Adresse und Verwandtschaftsgrad einsetzen»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0014.md) `zh-form-300-2025__c0014` – «2025 ausgerichtet an Wert: 519»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0147.md) `zh-wl-2025__c0147` – «hat der Empfänger innert dreier Monate nach Vollzug der Schenkung oder des Erb»
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0016.md) `zh-wl-2025__c0016` – «In der Steuererklärung 2025 ist das Vermögen per Ende 2025 einzutragen.»
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0016.md) `zh-wl-2025__c0016` – «ab Erbgang bis Ende 2025 (Steuerpflicht des Erben/Vermächtnisnehmers)»
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0016.md) `zh-wl-2025__c0016` – «Bei Schenkung oder Erbvorbezug wird die Vermögenssteuer für das ganze Jahr beim»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0151.md) `zh-wl-2025__c0151` – «Namen, Adressen und Erbquoten sämtlicher Erben»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0146.md) `zh-wl-2025__c0146` – «wenn die Erbteilung noch nicht erfolgt ist»

<a id="seite-1-personalien"></a>
### Ziff. Seite 1 – Personalien, Kinder (Jg. 2008–2025 / in Erstausbildung), unterstützte Personen, Pensionskassenbeiträge ja/nein

- **Schlüssel:** `personalien` (Personalien, Familienverhältnisse, Kinder, unterstützte Personen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Vorjahresveranlagung / Steuerveranlagungsverfügung / Einschätzungsentscheid → Vorjahresveranlagung, Zivilstandsdaten, Schul-/Lehrbestätigungen
- **Rein:** Vorjahresveranlagung / Zivilstandsdokumente → Personalien, Zivilstand, Konfession per 31.12.2025 · Lehrvertrag / Schulbestätigung → Kinder: Schule/Lehrfirma, voraussichtlich bis · Bestätigung der unterstützten Person → Unterstützungsbetrag pro Jahr · Je Person: ordentliche Beiträge an Pensionskasse (2. Säule) ja/nein
- **Rechnen:** Keine Rechnung; Grundlage für 24.1–24.3 (Unterstützung ≥ Kanton 2'800 / Bund 6'800); PK ja/nein → 3a-Maximum (Ziff. 14) und Versicherungsabzug (Ziff. 15)
- **Regel:** Verhältnisse per 31.12.2025 (Zivilstand, Konfession, Kinder inkl. Ausbildung und ob der andere Elternteil Unterhalt leistet, unterstützte Personen mit Unterstützungsbetrag). Die Angabe «ordentliche Beiträge an die Pensionskasse ja/nein» bestimmt Maximalabzug Versicherungsprämien (Ziff. 15) und 3a-Berechtigung.
- **Beachten:** Eingetragene Partnerschaft wird gleich behandelt wie die Ehe
- **Beachten:** Ledig/geschieden/getrennt: angeben, ob der andere Elternteil Unterhaltsbeiträge leistet
- **Beachten:** Kinder Jg. 2007 und älter versteuern Vermögen und Ertrag selbst
- **Limiten:**
  - Unterstützungsabzug (CHF): Kanton **CHF 2'800 (Unterstützungsabzug je erwerbsunfähige/beschränkt erwerbsfähige Person, an deren Unterhalt mindestens in Höhe des Abzugs beigetragen wird (nicht für Ehegatten und Kinder mit Abzug nach lit. a oder § 31 lit. c).)** · Bund **CHF 6'800 (Unterstützungsabzug pro erwerbsunfähige/beschränkt erwerbsfähige Person, wenn mindestens in Höhe des Abzugs unterstützt; nicht für Ehegatten und Kinder mit Kinderabzug)**
- **Quellen:**
  - [Formular 300 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0002.md) `zh-form-300-2025__c0002` – «Personalien, Berufs- und Familienverhältnisse am 31. Dezember 2025»
  - [Formular 300 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0003.md) `zh-form-300-2025__c0003` – «Kinder der Jahrgänge 2008-2025 oder in beruflicher Erstausbildung stehende Kinder, deren Unterhalt Sie bestreiten:»
  - [WL ZH 2025 S. 33](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0212.md) `zh-wl-2025__c0212` – «Die eingetragene Partnerschaft gleichgeschlechtlicher Paare wird»
  - [Formular 300 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0003.md) `zh-form-300-2025__c0003` – «Geburtsdatum Schule oder Lehrfirma Voraussichtlich Leistet der andere Elternteil»
  - [Formular 300 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0003.md) `zh-form-300-2025__c0003` – «Staatssteuer CHF 2’800 Bundessteuer CHF 6‘800 unterstützen:»
  - [Formular 300 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0002.md) `zh-form-300-2025__c0002` – «Ordentliche Beiträge an die»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0154.md) `zh-wl-2025__c0154` – «Vermögen und Ertrag von Personen des Jahrgangs 2007 (und älter) sind durch diese»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «24.1 Abzug für Kinder in Ihrem Haushalt (gemäss Seite 1)»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0010.md) `zh-form-300-2025__c0010` – «24.3 Abzug für Ehegatten / Partn.»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0130.md) `zh-wl-2025__c0130` – «15. Versicherungsprämien, Zinsen von Sparkapitalien»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0081.md) `zh-wl-2025__c0081` – «für Steuerpflichtige, die einer Einrichtung der beruflichen Vorsorge (2. Säule) angehören»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0086.md) `zh-wl-2025__c0086` – «erhöht sich der Abzug um die Hälfte»
  - [WL ZH 2025 S. 21](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0134.md) `zh-wl-2025__c0134` – «Bestätigung der unterstützten Person über Art, Zeitpunkt und Höhe der erfolgten Unterstützungen einzureichen»

<a id="seite-1-4-verfahren-einreichung"></a>
### Ziff. Seite 1 / 4 – Einreichung, Frist, Unterschrift, Beilagen

- **Schlüssel:** `verfahren.einreichung` (Einreichung, Unterschrift, Beilagen, Fristen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerrechnung / Akontorechnung / Schlussrechnung (Staats-, Gemeinde- und Bundessteuer) → Aufforderung / Steuererklärung (Frist), Beilagen gemäss Checkliste
- **Rein:** Aufforderung/Steuererklärung 2025 + Wertschriftenverzeichnis → Einreichung bis 31. März 2026 (online oder Scan-Center) · Lohnausweise, ALK-Taggeld-, Renten-, PK-/3a-Bescheinigungen → bereitlegen bzw. beilegen (Checkliste WL) · Zins-/Dividendengutschriften, Depot-Steuerverzeichnisse, Kauf-/Verkaufsbelege → bereitlegen für WV · Fristerstreckungsgesuch → Gemeindesteueramt (vor Fristablauf)
- **Rechnen:** Frist 31. März 2026; Erstreckung nur auf rechtzeitiges Gesuch, längstens 30. November des Folgejahres (darüber nur ausserordentliche Gründe)
- **Regel:** Steuererklärung 2025 bis 31. März 2026 einreichen (Fristerstreckung vor Ablauf beim Gemeindesteueramt beantragen; Mahnfristen nicht erstreckbar). Belege zu den Aufstellungen/Formularen nur beilegen, wenn ausdrücklich verlangt (insb. Liegenschaftskosten und Spenden erst auf Verlangen). Unterschrift Person 1 und 2.
- **Beachten:** Erstes rechtzeitiges Erstreckungsgesuch gilt ohne gegenteiligen Entscheid als bewilligt; Mahnfristen nicht erstreckbar
- **Beachten:** Belege nur auf Verlangen (insb. Liegenschaftskosten, Spenden); Papier-SE: Kopien A4, keine CD/DVD
- **Beachten:** Persönlich unterzeichnen; online: Ehegatten bestätigen gemeinsam elektronisch, Beilagen elektronisch
- **Limiten:**
  - Einreichefrist Steuererklärung: Kanton **Steuererklärung 2025 (natürliche Personen) bis 31. März 2026 einreichen (online oder Scan-Center).** · Bund **n/a – Natürliche Personen reichen die kantonale Steuererklärung ein, die auch die direkte Bundessteuer abdeckt; Frist/Erstreckung kantonal (Art. 124 Abs. 2 DBG: 'fristgemäss').**
  - Fristerstreckung – Regel (Private / Treuhänder), Kosten: Kanton **Gesuch vor Fristablauf beim Gemeindesteueramt; rechtzeitige Gesuche werden entsprechend dem Gesuch bewilligt, längstens bis 30. November des Folgejahres; erstes Gesuch gilt ohne gegenteiligen Entscheid als stillschweigend bewilligt; darüber hinaus nur aus ausserordentlichen Gründen (berufliche Belastung des Vertreters genügt nicht). Von Amtes wegen bis 30. September für Selbständige und Ausserkantonale. Mahnfristen nicht erstreckbar. Abgelaufene Fristen können nicht erstreckt werden.** · Bund **n/a – Bund: keine eigene Regel; es gilt das kantonale Verfahren der Steuererklärung.**
- **Quellen:**
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0017.md) `zh-wl-2025__c0017` – «Die Steuererklärung ist bis am 31. März 2026 einzureichen.»
  - [WL ZH 2025 S. 32](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0207.md) `zh-wl-2025__c0207` – «Die Belege zu den Aufstellungen und Formularen sind nur dann zusammen mit der»
  - [ZStB 132.1](../../chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0022.md) `zh-zstb-132-1__c0022` – «Die Steuererklärung ist zusammen mit dem Wertschriftenverzeichnis bis 31. März des der Steuerperiode folgenden Kalenderjahres online oder dem Scan-Center einzureichen.»
  - [ZStB 132.1](../../chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0024.md) `zh-zstb-132-1__c0024` – «Rechtzeitig eingereichten Fristerstreckungsgesuchen ist längstens bis 30. November des der Steuerperiode folgenden Kalenderjahres zu entsprechen.»
  - [ZStB 132.1](../../chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0025.md) `zh-zstb-132-1__c0025` – «Fristerstreckungsgesuche sind abzuweisen, ausser es können ausserordentliche Gründe glaubhaft gemacht werden.»
  - [ZStB 132.1](../../chunks/zh/dauernd/zh-zstb-132-1/zh-zstb-132-1__c0026.md) `zh-zstb-132-1__c0026` – «Rechtzeitig eingereichte erstmalige Fristerstreckungsgesuche gelten ohne gegenteiligen schriftlichen Entscheid als stillschweigend bewilligt.»
  - [WL ZH 2025 S. 32](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0208.md) `zh-wl-2025__c0208` – «prüfen Sie, ob Sie alle erforderlichen Unterlagen vor sich haben, insbesondere:»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0032.md) `zh-wl-2025__c0032` – «Bitte vergessen Sie nicht, Ihre Lohnausweise der Steuererklärung beizulegen.»
  - [WL ZH 2025 S. 32](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0207.md) `zh-wl-2025__c0207` – «Belegkopien sind im Format A4 einzureichen.»
  - [WL ZH 2025 S. 31](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0201.md) `zh-wl-2025__c0201` – «Elektronische Datenträger wie CD, DVD usw. können aus Sicherheitsgründen nicht angenommen werden»
  - [StG ZH § 133](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-133.md) `zh-stg-2025__par-133` – «persönlich unterzeichnen und samt den vorgeschriebenen Beilagen fristgemäss der zuständigen Behörde einreichen»
  - [V elektr. Einreichung ZH § 8](../../chunks/zh/2025/zh-v-einreichung/zh-v-einreichung__par-8.md) `zh-v-einreichung__par-8` – «Gemeinsam steuerpflichtige Ehegatten und eingetragene Partnerinnen und Partner geben die elektronische Bestätigung gemeinsam ab.»
  - [V elektr. Einreichung ZH § 8](../../chunks/zh/2025/zh-v-einreichung/zh-v-einreichung__par-8.md) `zh-v-einreichung__par-8` – «Die erforderlichen Beilagen sind zusammen mit der Steuererklärung elektronisch einzureichen.»

## Hilfsblatt Berufskosten (Form. 360)

<a id="form-360-ziff-1-1-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1.1 – Abonnementkosten öffentliche Verkehrsmittel (Code 201 Person 1 / 221 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** ÖV-Abonnement (GA, Streckenabo, Verbundabo, Halbtax nur ergänzend) – Arbeitsweg → ÖV-Abo-Beleg (Jahreskosten, Wohn- und Arbeitsort); Lohnausweis Feld F
- **Rein:** Lohnausweis → Feld F (unentgeltliche Beförderung) prüfen · GA/ÖV-Abo für wöchentliche Heimkehr bei Wochenaufenthalt → ebenfalls hier (Ziff. 1)
- **Rechnen:** Σ notwendige Abokosten im Jahr; Zwischentotal Ziff. 1 ≤ Kanton CHF 5'200 / Bund CHF 3'300
- **Regel:** Notwendige Abonnementskosten bei ständiger ÖV-Benützung. Zusammen mit Ziff. 1.2/1.3 Plafond CHF 5’200 (Staat) / CHF 3’300 (Bund). Kein Abzug bei Lohnausweis Feld F (unentgeltliche Beförderung).
- **Beachten:** Kein Abzug, soweit vom AG vergütet (z. B. LA Feld F unentgeltliche Beförderung) oder bei Geschäftsfahrzeug
- **Beachten:** Plafond gilt inkl. Fahrkosten des Wochenaufenthalts (Kanton 5'200 / Bund 3'300)
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, bei der Staatssteuer höchstens CHF 5'200 pro Jahr (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Bund:** Bund: Plafond CHF 3’300.
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0001.md) `zh-form-360-2025__c0001` – «1.1 Abonnementkosten für öffentliche Verkehrsmittel 201»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0062.md) `zh-wl-2025__c0062` – «die notwendigen Abonnementskosten»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0006.md) `zh-form-360-2025__c0006` – «1.1 Abonnementkosten für öffentliche Verkehrsmittel 221»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0032.md) `zh-wl-2025__c0032` – «Unentgeltliche Beförderung zwischen Wohn- und Arbeitsort»
  - [LS 631.33 (bis 2025) S. 3–4](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0007.md) `zh-pauschalierung-berufsauslagen-2025__c0007` – «Soweit Berufsauslagen vom Arbeitgeber vergütet werden, steht der steuerpflichtigen Person kein Abzug zu.»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «Arbeitnehmende, die über ein Geschäftsfahrzeug verfügen, können keine Fahrkosten in Abzug bringen.»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0071.md) `zh-wl-2025__c0071` – «Diese sind unter Ziffer 1 des Berufsauslagenblatts in Abzug zu bringen.»
  - [LS 631.33 (bis 2025) S. 2](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0003.md) `zh-pauschalierung-berufsauslagen-2025__c0003` – «unter Einbezug der Fahrkosten bei auswärtigem Wochenaufenthalt, können höchstens Fr. 5200 im Jahr abgezogen werden.»
  - [BKV Art. 9](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-9.md) `bund-bkv-2025__art-9` – «Sie sind bis zum Maximalbetrag nach Artikel 5 Absatz 1 abziehbar.»

<a id="form-360-ziff-1-2-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1.2 – Fahrrad, Kleinmotorrad (gelbes Kontrollschild) pauschal CHF 700 (Code 202 Person 1 / 222 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → –
- **Rechnen:** Pauschale CHF 700/Jahr je Person (Kanton = Bund); zählt zum Zwischentotal Ziff. 1 (≤ Kanton 5'200 / Bund 3'300)
- **Regel:** Pauschal CHF 700 pro Jahr bei ständiger Benützung eigenes Fahrrad/Kleinmotorrad mit gelbem Kontrollschild; kein Belegnachweis nötig.
- **Beachten:** Nur bei ständiger Benützung
- **Beachten:** Bund: tatsächliche Kosten zusätzlich nicht abziehbar
- **Limiten:**
  - Velo/Kleinmotorrad/E-Bike – Pauschale (CHF): Kanton **CHF 700 (Ständige Benützung eines Fahrrads, Motorfahrrads oder Kleinmotorrads (gelbes Kontrollschild): Pauschale CHF 700 pro Jahr.)** · Bund **CHF 700 (Pauschale pro Jahr für Fahrrad, Motorfahrrad und Motorrad mit gelbem Kontrollschild; tatsächliche Kosten zusätzlich nicht abziehbar)**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, bei der Staatssteuer höchstens CHF 5'200 pro Jahr (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0001.md) `zh-form-360-2025__c0001` – «1.2 Fahrrad, Kleinmotorrad (gelbes Kontrollschild) pauschal CHF 700»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0063.md) `zh-wl-2025__c0063` – «Kontrollschild im Jahr CHF 700»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0006.md) `zh-form-360-2025__c0006` – «1.2 Fahrrad, Kleinmotorrad (gelbes Kontrollschild) pauschal CHF 700 222»
  - [LS 631.33 (bis 2025) S. 1](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0001.md) `zh-pauschalierung-berufsauslagen-2025__c0001` – «b. bei ständiger Benützung eines Fahrrades,»

<a id="form-360-ziff-1-3-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 1.3 – Auto / Motorrad (weisses Kontrollschild), CHF –.70 bzw. –.40 pro km (Code 204 Person 1 / 224 Person 2; Zwischentotal 205 Person 1 / 225 Person 2)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Fahrzeugausweis, Arbeitsort, Arbeitstage, km pro Fahrt; Begründung Ziff. 7 (Code 2041–2044)
- **Rein:** Fahrzeugausweis → Kontrollschild weiss (Auto/Motorrad), geleast ja/nein · Arbeitszeitnachweis → Arbeitsort, Arbeitstage, Fahrten pro Tag, km · AG-Bestätigung/Arztzeugnis → Begründung Ziff. 7 (Code 2041–2044)
- **Regel:** Nur ausnahmsweise (kein ÖV-Anschluss ≥ 1 km, Zeitersparnis > 1 Std., ständige dienstliche Benützung gegen Entschädigung, Krankheit/Gebrechlichkeit mit Arztzeugnis): Auto 70 Rp./km, Motorrad weiss 40 Rp./km, in der Regel max. 240 Tage; sonst nur ÖV-Abo. Mittagsheimfahrt max. soviel wie Verpflegungsabzug (dafür entfällt dieser). Geschäftsfahrzeug: kein Fahrkostenabzug. Zwischentotal auf CHF 5’200 (Staat) / CHF 3’300 (Bund) begrenzt.
- **Beachten:** Nur ausnahmsweise: Haltestelle ≥ 1 km entfernt/kein ÖV, > 1 Std. Zeitersparnis, auf Verlangen des AG, Krankheit
- **Beachten:** Mittagsheimfahrt max. Verpflegungsabzug (Kanton ≤ 3'200/Jahr; Bund ≤ 15/Tag), dafür kein Verpflegungsabzug
- **Beachten:** Geschäftsfahrzeug: kein Fahrkostenabzug; Bund: km-Abzug nur ohne verfügbares/zumutbares ÖV
- **Limiten:**
  - Fahrkosten Auto – Ansatz pro km (CHF): Kanton **CHF 0.70 (Privatauto nur ausnahmsweise (kein öV, Zeitersparnis über 1 Std., Einsatz auf Verlangen des Arbeitgebers, Krankheit/Gebrechlichkeit): CHF 0.70 pro Fahrkilometer.)** · Bund **CHF 0.70 (Privatauto: Abzug pro Fahrkilometer CHF 0.70, nur wenn kein öffentliches Verkehrsmittel verfügbar/zumutbar (Steuerjahr 2025))**
  - Fahrkosten Motorrad – Ansatz pro km (CHF): Kanton **CHF 0.40 (Motorrad mit weissem Kontrollschild, nur in den gleichen Ausnahmefällen wie beim Auto: CHF 0.40 pro Fahrkilometer.)** · Bund **CHF 0.40 (Motorrad mit weissem Kontrollschild: CHF 0.40 pro Fahrkilometer (Steuerjahr 2025))**
  - Fahrkosten – massgebende Arbeitstage pro Jahr: Kanton **240 Tage (Kilometerabrechnung (Auto/Motorrad, weisses Kontrollschild) in der Regel auf 240 Arbeitstage begrenzt (gemäss Formular Berufsauslagen).)** · Bund **n/a – Bund kennt keine Festlegung massgebender Arbeitstage; abziehbar sind die tatsächlichen notwendigen Kosten bis zum Maximalbetrag (Art. 26 Abs. 1 lit. a DBG).**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, bei der Staatssteuer höchstens CHF 5'200 pro Jahr (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Bund:** Bund: Plafond CHF 3’300 (eigene Spalte, Zwischentotal Code 205).
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0002.md) `zh-form-360-2025__c0002` – «Auto: CHF -.70 pro km Motorrad: CHF -.40 pro km»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0064.md) `zh-wl-2025__c0064` – «für Auto 70 Rp. pro Fahrkilometer.»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «Bei der Staatssteuer ist der Fahrkostenabzug auf CHF 5’200 beschränkt.»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «Bei der direkten Bundessteuer ist der Fahrkostenabzug auf CHF 3’300 beschränkt.»
  - [StG ZH § 26](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-26.md) `zh-stg-2025__par-26` – «a. die notwendigen Kosten bis zu einem Höchstbetrag von Fr. 5200 für Fahrten zwischen Wohn- und Arbeitsstätte»
  - [LS 631.33 (bis 2025) S. 2](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0003.md) `zh-pauschalierung-berufsauslagen-2025__c0003` – «Für Hin- und Rückfahrt über Mittag sind in diesen Fällen höchstens Fr. 3200 im Jahr»
  - [WL 2a 2025 S. 6](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0044.md) `bund-wl-2a-2025__c0044` – «doch zusammen höchstens 15 Fr. im Tag berechnet werden»
  - [BKV Art. 5](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-5.md) `bund-bkv-2025__art-5` – «sofern kein öffentliches Verkehrsmittel zur Verfügung steht oder dessen Benützung objektiv nicht zumutbar ist»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «Fehlen eines öffentlichen Verkehrsmittels (siehe Wegleitung) 2041»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «(Arztzeugnis beilegen) 2044»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0007.md) `zh-form-360-2025__c0007` – «224 13211 224 13211»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0007.md) `zh-form-360-2025__c0007` – «Zwischentotal 225 3211 225 3211»

<a id="form-360-ziff-7-abzug-berufskosten-fahrkosten"></a>
### Ziff. Form. 360 Ziff. 7 – Begründung private Motorfahrzeugbenützung ankreuzen: 2041 Fehlen ÖV, 2042 Zeitersparnis über 1 Std., 2043 ständige Benützung während der Arbeitszeit auf Verlangen und gegen Entschädigung des AG, 2044 Krankheit/Gebrechlichkeit (Arztzeugnis) (Person 2: 2241–2244); Geschäftsfahrzeug

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Fahrzeugausweis (Fahrzeugschein) / Kontrollschild-Nachweis, Fahrtenaufstellung für Auto oder Motorrad auf dem Arbeitsweg → Arbeitgeberbestätigung / Arztzeugnis; Lohnausweis Feld F bei Geschäftsfahrzeug
- **Rein:** Fahrplan/Distanz zur Haltestelle → Code 2041 (ÖV fehlt) bzw. 2042 (Zeitersparnis) · Arbeitgeberbestätigung → Code 2043 · Arztzeugnis → Code 2044 (Person 2: 2241–2244)
- **Regel:** Zutreffende Begründung ankreuzen (fehlender ÖV, > 1 Std. Zeitersparnis, ständige Benützung auf Verlangen und gegen Entschädigung des Arbeitgebers, Krankheit/Gebrechlichkeit mit Arztzeugnis). Wer ein Geschäftsfahrzeug hat, kann keine Fahrkosten abziehen.
- **Beachten:** 2041: Wohn- oder Arbeitsstätte ≥ 1 km von nächster Haltestelle oder kein ÖV bei Arbeitsbeginn/-ende
- **Beachten:** 2042: > 1 Std. Zeitersparnis (Haustür–Arbeitsplatz retour); 2043: AG verlangt/entschädigt Fahrzeug, Arbeitsweg unbezahlt
- **Beachten:** Unentgeltliches Geschäftsfahrzeug mit pauschaler Fahrkostenberechnung (ZStB 17.1): kein Fahrkostenabzug
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «Fehlen eines öffentlichen Verkehrsmittels (siehe Wegleitung) 2041»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «Zeitersparnis von über 1 Stunde bei Benützung des privaten Motorfahrzeuges   2042»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «Ständige Benützung während der Arbeitszeit auf Verlangen und gegen Entschädigung des Arbeitgebers   2043»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «Arbeitnehmende, die über ein Geschäftsfahrzeug verfügen, können keine Fahrkosten in Abzug bringen.»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0010.md) `zh-form-360-2025__c0010` – «Fehlen eines öffentlichen Verkehrsmittels (siehe Wegleitung) 2241»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0064.md) `zh-wl-2025__c0064` – «nächsten Haltestelle mindestens 1 km entfernt ist oder bei Arbeitsbeginn oder -ende kein»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0064.md) `zh-wl-2025__c0064` – «eine Zeitersparnis von über einer Stunde (gemessen von der Haustür zum Arbeitsplatz und zurück)»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0064.md) `zh-wl-2025__c0064` – «keine Entschädigung erhält (Bestätigung des Arbeitgebers ist beizulegen)»
  - [LS 631.33 (bis 2025) S. 2](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0003.md) `zh-pauschalierung-berufsauslagen-2025__c0003` – «Wird bei einer unentgeltlichen Nutzung eines Geschäftsfahrzeugs für Fahrten zwischen Wohn- und Arbeitsstätte sowie für weitere private»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0064.md) `zh-wl-2025__c0064` – «auf Verlangen und gegen Entschädigung des Arbeitgebers das private Motorfahrzeug tatsächlich ständig während der Arbeitszeit benützt»

<a id="form-360-ziff-2-1-verbilligt-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 360 Ziff. 2.1 (verbilligt) – Mehrkosten Verpflegung bei verbilligter Verpflegung (Kantine, Lunch-Checks): CHF 7.50/Tag, max. CHF 1’600/Jahr (Code 206 Person 1 / 226 Person 2)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Spesenreglement des Arbeitgebers (genehmigtes Spesenreglement, Spesenabrechnung, Pauschalspesen) → Lohnausweis Feld G (Kantine/Lunch-Checks); Arbeitstage am Arbeitsort
- **Rein:** Lohnausweis → Feld G (Kantinenverpflegung/Lunch-Checks) angekreuzt · Arbeitszeitnachweis → Anzahl Arbeitstage mit auswärtiger Verpflegung
- **Rechnen:** min(Arbeitstage × 7.50; 1’600) → Code 206 (Person 2: Code 226), Spalte Staatssteuer und Bundessteuer; Regelfall Kantine/Lunch-Checks: Kanton = Bund (Ausnahmen Bund nach BKV Art. 6 Abs. 2/3, s. beachten: Barbeitrag beim Bund kein halber Abzug, kein Abzug unter Naturalbezugsansätzen)
- **Regel:** Wenn die Verpflegung vom Arbeitgeber verbilligt wird (Kantine, Personalrestaurant, Barbeitrag, Essensgutscheine) und trotzdem Mehrkosten entstehen: CHF 7.50 pro Arbeitstag, bei ständiger auswärtiger Verpflegung max. CHF 1’600 pro Jahr. Nur wenn die Heimkehr in der Mittagspause nicht möglich ist. Nicht kumulierbar mit 2.1 voll und 2.2 Schicht.
- **Beachten:** Nur wenn die Arbeitspause die Heimkehr nicht ermöglicht und trotzdem Mehrkosten entstehen
- **Beachten:** Nicht kumulierbar mit 2.1 voll, 2.2 Schicht oder Mittagsheimfahrt (dann entfällt Verpflegungsabzug)
- **Beachten:** Bund: halber Abzug bei Verbilligung anders als in bar (Gutscheine) oder AG-Kantine; kein Abzug unter Naturalbezugsansatz
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Verpflegung durch Arbeitgeber verbilligt (Kantine, Personalrestaurant, Barbeitrag, Essensgutscheine) und trotzdem Mehrkosten: CHF 7.50 pro Arbeitstag.)** · Bund **CHF 7.50 (Halber Abzug CHF 7.50 pro Hauptmahlzeit, wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei ständiger auswärtiger Verpflegung mit Verbilligung: CHF 1'600 pro Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: CHF 1'600 pro Jahr)**
- **Bemerkung:** Codes 206 (Person 1, Staat und Bund) / 226 (Person 2, Staat und Bund). «3211» in den Formular-Zitaten ist ein Layoutartefakt der Eingabefelder, kein Code (raw/zh/2025/zh-form-360-2025.pdf S. 1).
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md) `zh-form-360-2025__c0003` – «wenn die Verpflegung durch den Arbeitgeber verbilligt wird und dem Arbeitnehmer trotzdem»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md) `zh-form-360-2025__c0003` – «Mehrkosten entstehen: pro Arbeitstag CHF 7.50 / im Jahr CHF 1’600 206 3211 206 3211»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0066.md) `zh-wl-2025__c0066` – «– wenn die Verpflegung durch den Arbeitgeber verbilligt wird (Kantine, Personalrestaurant,»
  - [LS 631.33 (bis 2025) S. 2–3](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0004.md) `zh-pauschalierung-berufsauslagen-2025__c0004` – «Die vorstehenden Abzüge dürfen nicht kumuliert werden.»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0032.md) `zh-wl-2025__c0032` – «Kantinenverpflegung / Lunch-Checks»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0008.md) `zh-form-360-2025__c0008` – «pro Arbeitstag CHF 7.50 / im Jahr CHF 1’600 226 3211 226 3211»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «Dafür entfällt der Verpflegungsabzug (Ziffer 2.1).»
  - [BKV Art. 6](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-6-t1.md) `bund-bkv-2025__art-6-t1` – «Kein Abzug ist mangels Mehrkosten zulässig, wenn der Arbeitgeber bei der Bewertung von Naturalbezügen»
  - [BKV Art. 6](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-6-t1.md) `bund-bkv-2025__art-6-t1` – «Nur der halbe Abzug ist zulässig, wenn die Verpflegung vom Arbeitgeber anders als in bar verbilligt wird (Abgabe von Gutscheinen)»

<a id="form-360-ziff-2-1-voll-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 360 Ziff. 2.1 (voll) – Mehrkosten Verpflegung, Verpflegung voll zu Lasten Arbeitnehmer: CHF 15/Tag, max. CHF 3’200/Jahr (Code 208 Person 1 / 228 Person 2)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis (kein Feld G); Arbeitstage am Arbeitsort
- **Rein:** Lohnausweis → Feld G nicht angekreuzt (keine Verbilligung) · Arbeitszeitnachweis → Arbeitstage mit auswärtiger Hauptmahlzeit
- **Regel:** Wenn die Verpflegung in anderen Gaststätten voll zu Lasten des Arbeitnehmers geht: CHF 15 pro Arbeitstag, bei ständiger auswärtiger Verpflegung max. CHF 3’200 pro Jahr. Voraussetzung: Arbeitspause lässt Heimkehr nicht zu.
- **Beachten:** Nur wenn Arbeitspause die Heimkehr nicht ermöglicht (Bund: grosse Entfernung oder kurze Essenspause)
- **Beachten:** Nicht kumulierbar mit 2.1 verbilligt, 2.2 Schicht oder Mittagsheimfahrt
- **Beachten:** Bund: kein Abzug mangels Mehrkosten, wenn die Hauptmahlzeit maximal 10 Fr. kostet
- **Limiten:**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswärtige Verpflegung, wenn voll zulasten der steuerpflichtigen Person: CHF 15 pro Arbeitstag (nicht kumulierbar mit Fahrkosten über Mittag).)** · Bund **CHF 15 (Mehrkosten auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (i.d.R. Mittagessen); ausschliesslich Pauschale, wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei ständiger auswärtiger Verpflegung (voll zulasten): CHF 3'200 pro Jahr.)** · Bund **CHF 3'200 (Bei ständiger auswärtiger Verpflegung CHF 3'200 pro Jahr (voller Abzug))**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md) `zh-form-360-2025__c0003` – «pro Arbeitstag CHF 15 / im Jahr CHF 3’200»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0066.md) `zh-wl-2025__c0066` – «pro Arbeitstag CHF 15, bei ständiger»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0032.md) `zh-wl-2025__c0032` – «Kantinenverpflegung / Lunch-Checks»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0008.md) `zh-form-360-2025__c0008` – «pro Arbeitstag CHF 15 / im Jahr CHF 3’200 228»
  - [BKV Art. 6](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-6-t1.md) `bund-bkv-2025__art-6-t1` – «wegen grosser Entfernung zwischen Wohn- und Arbeitsstätte oder wegen kurzer Essenspause eine Hauptmahlzeit nicht zu Hause einnehmen kann»
  - [WL 2a 2025 S. 6–7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0046.md) `bund-wl-2a-2025__c0046` – «Kein Abzug ist mangels Mehrkosten zu gewähren, wenn»
  - [LS 631.33 (bis 2025) S. 2–3](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0004.md) `zh-pauschalierung-berufsauslagen-2025__c0004` – «Die vorstehenden Abzüge dürfen nicht kumuliert werden.»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «Dafür entfällt der Verpflegungsabzug (Ziffer 2.1).»

<a id="form-360-ziff-2-2-abzug-berufskosten-verpflegung"></a>
### Ziff. Form. 360 Ziff. 2.2 – Mehrkosten bei durchgehender, mind. achtstündiger Schicht- / Nachtarbeit: CHF 15/Schichttag, max. CHF 3’200/Jahr (Code 210 Person 1 / 230 Person 2)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 (Anzahl Schichttage); Dienstplan
- **Rein:** Arbeitgeberbescheinigung → Anzahl Tage mit durchgehender, mind. achtstündiger Schicht-/Nachtarbeit (Feld «Anzahl Tage»)
- **Regel:** Pro ausgewiesenem Schichttag CHF 15, bei ständiger Schicht-/Nachtarbeit max. CHF 3’200 pro Jahr; gestaffelte Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause eingenommen werden können. Anzahl Tage eintragen. Nicht kumulierbar mit Ziff. 2.1.
- **Beachten:** Gestaffelte (unregelmässige) Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zu Hause möglich
- **Beachten:** Nicht kumulierbar mit Ziff. 2.1 (verbilligt oder voll)
- **Beachten:** Bund: AG muss Schichttage und Arbeitsort auf Verlangen bescheinigen
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Durchgehende, mindestens achtstündige Schicht-/Nachtarbeit: CHF 15 pro ausgewiesenem Schichttag, bei ständiger Schicht-/Nachtarbeit CHF 3'200 pro Jahr. Gestaffelte (unregelmässige) Arbeitszeit gleichgestellt, wenn Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich.)** · Bund **CHF 15 (Durchgehende Schicht-/Nachtarbeit (gestaffelte Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich): CHF 15 pro ausgewiesenem Tag, bei ganzjähriger Schicht-/Nachtarbeit CHF 3'200 pro Jahr)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei ständiger auswärtiger Verpflegung (voll zulasten): CHF 3'200 pro Jahr.)** · Bund **CHF 3'200 (Bei ständiger auswärtiger Verpflegung CHF 3'200 pro Jahr (voller Abzug))**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md) `zh-form-360-2025__c0003` – «pro ausgewiesenem Schichttag CHF 15 / im Jahr CHF 3’200»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0066.md) `zh-wl-2025__c0066` – «gewiesenen Schichttag CHF 15, bei ständiger Schicht- oder Nachtarbeit im Jahr»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0008.md) `zh-form-360-2025__c0008` – «pro ausgewiesenem Schichttag CHF 15 / im Jahr CHF 3’200 230»
  - [BKV Art. 6](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-6-t2.md) `bund-bkv-2025__art-6-t2` – «Der Arbeitgeber muss die Anzahl Tage mit Schicht- oder Nachtarbeit sowie den Arbeitsort auf Verlangen bescheinigen.»

<a id="form-360-ziff-3-abzug-berufskosten-uebrige"></a>
### Ziff. Form. 360 Ziff. 3 – Übrige Berufskosten: pauschal 3 % des Nettolohns, mind. CHF 2’000, max. CHF 4’000 (Code 212) bzw. effektiv (Code 213) (Person 2: 232 / 233)

- **Schlüssel:** `abzug.berufskosten.uebrige` (Übrige Berufskosten (Pauschale oder effektiv, inkl. Arbeitszimmer)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 11 (Nettolohn als Basis); bei effektiv: Aufstellung + Belege
- **Rein:** Lohnausweis → Ziff. 11 Nettolohn (= Brutto − AHV/IV/EO/ALV − PK-Beiträge − NBUV) · Bei effektiv: Aufstellung + Belege (Berufskleider, Werkzeuge/EDV, Fachliteratur, Arbeitszimmer, Verbandsbeiträge)
- **Regel:** Berufskleider, Berufswerkzeuge (inkl. EDV), Fachliteratur, privates Arbeitszimmer, Berufsverbandsbeiträge. Pauschale 3 % des Nettolohns gemäss Lohnausweis (mind. CHF 2’000 / max. CHF 4’000); höhere effektive Kosten nur mit Aufstellung und vollem Nachweis (dann Pauschale entfällt).
- **Beachten:** Effektiv statt Pauschale nur mit Aufstellung und Nachweis im vollen Umfang
- **Beachten:** Privates Arbeitszimmer/Homeoffice in Pauschale enthalten, keine separate Pauschale
- **Beachten:** Bund: Pauschale bei Teilzeit oder unterjähriger Erwerbstätigkeit angemessen kürzen
- **Limiten:**
  - Übrige Berufskosten – Pauschale in % des Nettolohns: Kanton **3 % (Übrige Berufsauslagen (Berufskleider, Werkzeuge inkl. EDV, Fachliteratur, privates Arbeitszimmer, Berufsverbandsbeiträge): 3 % des Nettolohns, mind. CHF 2'000, höchstens CHF 4'000. Nachweis höherer Kosten möglich (volle Belegpflicht).)** · Bund **3 % (Übrige Berufskosten (Art. 26 Abs. 1 lit. c DBG): Pauschale 3 % des Nettolohns, min. CHF 2'000, max. CHF 4'000; anstelle der Pauschale ist der Nachweis höherer tatsächlicher übriger Berufskosten möglich. Fahrkosten (lit. a, max. 3'300 gemäss DBG 2025; WL 2a 2025 nennt 3'200 – Widerspruch siehe berufskosten.fahrkosten.max) und Verpflegung (lit. b) werden zusätzlich abgezogen. Bei Teilzeit/Teiljahr angemessen kürzen.)**
  - Übrige Berufskosten – Pauschale Minimum (CHF): Kanton **CHF 2'000 (Minimum der Pauschale für übrige Berufsauslagen: CHF 2'000.)** · Bund **CHF 2'000 (Minimum der Pauschale übrige Berufskosten)**
  - Übrige Berufskosten – Pauschale Maximum (CHF): Kanton **CHF 4'000 (Maximum der Pauschale für übrige Berufsauslagen: CHF 4'000.)** · Bund **CHF 4'000 (Maximum der Pauschale übrige Berufskosten)**
  - Arbeitszimmer/Homeoffice – Regel: Kanton **Keine separate Homeoffice-/Arbeitszimmer-Pauschale: Kosten eines privaten Arbeitszimmers sind in der Pauschale für übrige Berufsauslagen (3 % des Nettolohns, CHF 2'000–4'000) enthalten; höhere effektive Kosten nur bei vollem Nachweis.** · Bund **Privates Arbeitszimmer: nur als Teil der Pauschale 'übrige Berufskosten' bzw. bei Nachweis höherer Kosten abziehbar; Kosten (Miete, Heizung, Beleuchtung) nur, wenn das Zimmer für die Berufsarbeit benützt werden muss. Gelegentliche Arbeit in der Privatwohnung gibt keinen Abzug**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0004.md) `zh-form-360-2025__c0004` – «3% des Nettolohnes gem. Lohnausweis, mind. CHF 2’000, höchstens CHF 4’000»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0069.md) `zh-wl-2025__c0069` – «so sind diese Berufsauslagen in vollem Umfange nachzuweisen.»
  - [LS 631.33 (bis 2025) S. 3](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0005.md) `zh-pauschalierung-berufsauslagen-2025__c0005` – «Der Nettolohn entspricht dem Bruttolohn nach»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0035.md) `zh-wl-2025__c0035` – «11. Nettolohn / Rente – Salaire net / Rente – Salario netto / Rendita»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0009.md) `zh-form-360-2025__c0009` – «bzw. effektiv gemäss Aufstellung 233»
  - [BKV Art. 7](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-7.md) `bund-bkv-2025__art-7` – «Der Pauschalabzug ist angemessen zu kürzen, wenn die unselbständige Erwerbstätigkeit bloss während eines Teils des Jahres oder als Teilzeitarbeit ausgeübt wird.»

<a id="form-360-ziff-4-abzug-berufskosten-wochenaufenthalt"></a>
### Ziff. Form. 360 Ziff. 4 – Mehrkosten bei auswärtigem Wochenaufenthalt (Code 2860 Person 1 / 2861 Person 2)

- **Schlüssel:** `abzug.berufskosten.wochenaufenthalt` (Mehrkosten Wochenaufenthalt) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Mietvertrag Wohnung (Mietzinsbestätigung, Nebenkostenabrechnung des Mieters) → Mietvertrag Zimmer am Arbeitsort; Aufstellung
- **Rein:** Mietvertrag/Mietzinsquittungen → Zimmermiete am Arbeitsort · Aufstellung → Arbeitstage am Wochenaufenthaltsort (Abendessen) · ÖV-Abo/GA wöchentliche Heimkehr → unter Ziff. 1 (nicht hier)
- **Regel:** Zusätzlich: Mehrkosten Abendessen CHF 15 pro Arbeitstag bzw. max. CHF 3’200 im Jahr bei ganzjährigem Wochenaufenthalt, Zimmermiete, Kosten der wöchentlichen Heimkehr (i.d.R. nur ÖV-Abo, unter Ziff. 1 abziehen).
- **Beachten:** Nur Zimmer (nicht Wohnung); Bund: ortsübliche Zimmerkosten
- **Beachten:** Heimkehr i.d.R. nur ÖV, zählt zum Fahrkostenplafond Ziff. 1 (Kanton 5'200 / Bund 3'300)
- **Beachten:** Bund: Verpflegung total CHF 30/Tag, ganzjährig max. 6'400; nicht zusätzlich zu Art. 6 BKV; kein Nachweis höherer Kosten
- **Limiten:**
  - Wochenaufenthalt – Unterkunft (Regel): Kanton **Auswärtiger Wochenaufenthalt: Mehrkosten Unterkunft = Mietzins für ein Zimmer; Heimkehr in der Regel nur Kosten öffentlicher Verkehrsmittel (z. B. GA), unter Fahrkosten (Ziff. 1) abzuziehen; Abendessen CHF 15 pro Arbeitstag.** · Bund **Mehrkosten Unterkunft: ortsübliche Auslagen für ein Zimmer (nicht eine Wohnung) abziehbar; Fahrkosten der regelmässigen Heimkehr bis zum Maximalbetrag nach Art. 5 Abs. 1 BKV**
  - Wochenaufenthalt – Mehrkosten Verpflegung pro Jahr (CHF): Kanton **CHF 3'200 (Mehrkosten Verpflegung (Abendessen) bei ganzjährigem Wochenaufenthalt: CHF 15 pro Arbeitstag, max. CHF 3'200 pro Jahr.)** · Bund **CHF 6'400 (Auswärtiger Wochenaufenthalt: Verpflegung CHF 30 pro Tag, max. CHF 6'400 pro Jahr; bei Verbilligung CHF 22.50 pro Tag bzw. CHF 4'800 pro Jahr; Nachweis höherer Kosten ausgeschlossen)**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, bei der Staatssteuer höchstens CHF 5'200 pro Jahr (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0004.md) `zh-form-360-2025__c0004` – «Mehrkosten bei auswärtigem Wochenaufenthalt (gemäss Aufstellung, siehe Wegleitung) 2860»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0071.md) `zh-wl-2025__c0071` – «Arbeitstag oder bei ganzjährigem Wochenaufenthalt CHF 3’200 im Jahr abgezogen werden.»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0071.md) `zh-wl-2025__c0071` – «Als Mehrkosten für auswärtige Unterkunft kann der Mietzins für ein Zimmer abgezogen»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0009.md) `zh-form-360-2025__c0009` – «Mehrkosten bei auswärtigem Wochenaufenthalt (gemäss Aufstellung, siehe Wegleitung) 2861»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0070.md) `zh-wl-2025__c0070` – «4. Zusätzliche Mehrkosten bei auswärtigem Wochenaufenthalt»
  - [BKV Art. 9](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-9.md) `bund-bkv-2025__art-9` – «Als notwendige Mehrkosten der Unterkunft sind die ortsüblichen Auslagen für ein Zimmer abziehbar.»
  - [BKV Art. 9](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-9.md) `bund-bkv-2025__art-9` – «Der Nachweis höherer Kosten ist ausgeschlossen.»
  - [WL 2a 2025 S. 6](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0043.md) `bund-wl-2a-2025__c0043` – «nur ein Zimmer (nicht eine Wohnung)»
  - [WL 2a 2025 S. 6](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0044.md) `bund-wl-2a-2025__c0044` – «pro Hauptmahlzeit, somit 30 Fr. im Tag, bei ganzjährigem»
  - [LS 631.33 (bis 2025) S. 2](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0003.md) `zh-pauschalierung-berufsauslagen-2025__c0003` – «unter Einbezug der Fahrkosten bei auswärtigem Wochenaufenthalt, können höchstens Fr. 5200 im Jahr abgezogen werden.»
  - [WL 2a 2025 S. 6](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0044.md) `bund-wl-2a-2025__c0044` – «Wochenaufenthalt 6400 Fr. im Jahr»
  - [BKV Art. 6](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-6-t2.md) `bund-bkv-2025__art-6-t2` – «Der Pauschalabzug nach Absatz 1 oder 2 kann nicht gleichzeitig mit jenem nach Artikel 9 Absatz 2 beansprucht werden.»
  - [BKV Art. 9](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-9.md) `bund-bkv-2025__art-9` – «Sie sind bis zum Maximalbetrag nach Artikel 5 Absatz 1 abziehbar.»

<a id="form-360-ziff-5-abzug-berufskosten-nebenerwerb"></a>
### Ziff. Form. 360 Ziff. 5 – Auslagen bei Nebenerwerb: pauschal 20 %, mind. CHF 800, max. CHF 2’400 (Code 216) bzw. effektiv (Code 217) (Person 2: 236 / 237)

- **Schlüssel:** `abzug.berufskosten.nebenerwerb` (Berufskosten Nebenerwerb) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis des Nebenerwerbs; bei effektiv: Aufstellung
- **Rein:** Lohnausweis(e) Nebenerwerb → Einkünfte aus allen Nebenbeschäftigungen · Bei effektiv: detaillierte Aufstellung + Nachweise
- **Regel:** Gilt für sämtliche Auslagen bei unselbständigem Nebenerwerb (inkl. Fahrkosten, Verpflegung): 20 % der Einkünfte aus allen Nebenbeschäftigungen, insgesamt mind. CHF 800 und max. CHF 2’400; höhere effektive Auslagen mit detaillierter Aufstellung und Nachweis.
- **Beachten:** Pauschale deckt sämtliche Auslagen inkl. Fahrkosten und Verpflegung des Nebenerwerbs
- **Beachten:** Nur unselbständiger Nebenerwerb; Behördenentschädigungen: Verfügungen ZStB 17.3
- **Beachten:** Bund: Basis = Nebeneinkünfte netto (nach Sozialversicherungsbeiträgen), gleiche Grenzen
- **Limiten:**
  - Nebenerwerb – Pauschale in % der Nebeneinkünfte: Kanton **20 % (Auslagen bei Nebenbeschäftigung in unselbständiger Stellung (inkl. Fahrkosten, Verpflegung): 20 % der Einkünfte aus allen Nebenbeschäftigungen, mind. CHF 800, höchstens CHF 2'400.)** · Bund **20 % (Nebenerwerb: Pauschale 20 % der Nettoeinkünfte (nach Abzug der Sozialversicherungsbeiträge))**
  - Nebenerwerb – Pauschale Minimum (CHF): Kanton **CHF 800 (Minimum Nebenerwerbspauschale: CHF 800.)** · Bund **CHF 800 (Minimum Pauschale Nebenerwerb)**
  - Nebenerwerb – Pauschale Maximum (CHF): Kanton **CHF 2'400 (Maximum Nebenerwerbspauschale: CHF 2'400.)** · Bund **CHF 2'400 (Maximum Pauschale Nebenerwerb)**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0004.md) `zh-form-360-2025__c0004` – «bzw. effektiv gemäss Aufstellung 217»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0072.md) `zh-wl-2025__c0072` – «20% der Einkünfte aus allen Nebenbeschäftigungen, insgesamt mindestens»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0072.md) `zh-wl-2025__c0072` – «jedoch CHF 800 und höchstens CHF 2’400.»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0009.md) `zh-form-360-2025__c0009` – «pauschal 20% der Einkünfte aus Nebenerwerb, mind. CHF 800 und höchstens CHF 2‘400 236»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0009.md) `zh-form-360-2025__c0009` – «bzw. effektiv gemäss Aufstellung 237»
  - [WL 2a 2025 S. 6–7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0045.md) `bund-wl-2a-2025__c0045` – «kann ein Pauschalabzug von 20 % der Nebeneinkünfte (Netto-»
  - [WL 2a 2025 S. 6–7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0046.md) `bund-wl-2a-2025__c0046` – «einkommen nach Abzug der Sozialversicherungsbeiträge), min-»

<a id="form-360-ziff-6-berechnung-total"></a>
### Ziff. Form. 360 Ziff. 6 – Total der Berufsauslagen (Code 220 Person 1 / 240 Person 2) → Steuererklärung Ziff. 11.1 / 11.2

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Formular 360
- **Rein:** Übertrag Form. 360 Ziff. 1–5, je Spalte Staatssteuer / Bundessteuer
- **Rechnen:** Code 220 = Zwischentotal Ziff. 1 (≤ Kanton 5'200 / Bund 3'300) + Ziff. 2 + 3 + 4 + 5 → HF S. 3 Ziff. 11.1; Person 2: Code 240 → Ziff. 11.2
- **Regel:** Total übertragen nach Hauptformular Seite 3, Ziff. 11.1 (Person 1) bzw. 11.2 (Person 2).
- **Beachten:** Je Person eigene Seite (P1 / P2); Ehegatten nach Massgabe ihrer Beschäftigung
- **Beachten:** Nur nicht vom Arbeitgeber vergütete Auslagen; Formular vollständig ausgefüllt beilegen
- **Limiten:**
  - Fahrkosten – Maximalabzug pro Person (CHF): Kanton **CHF 5'200 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten, bei der Staatssteuer höchstens CHF 5'200 pro Jahr (inkl. Fahrkosten bei auswärtigem Wochenaufenthalt).)** · Bund **CHF 3'300 (Fahrkosten Wohn-/Arbeitsstätte: notwendige Kosten bis max. CHF 3'300 pro Person und Jahr (Steuerjahr 2025))**
- **Quellen:**
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «6. Total der Berufsauslagen 220»
  - [Formular 360 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0010.md) `zh-form-360-2025__c0010` – «6. Total der Berufsauslagen 240»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0002.md) `zh-form-360-2025__c0002` – «Zwischentotal 205 3211 205 3211»
  - [LS 631.33 (bis 2025) S. 3–4](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0007.md) `zh-pauschalierung-berufsauslagen-2025__c0007` – «für jeden Ehegatten nach Massgabe seiner Beschäftigung berechnet»
  - [LS 631.33 (bis 2025) S. 3–4](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0007.md) `zh-pauschalierung-berufsauslagen-2025__c0007` – «Soweit Berufsauslagen vom Arbeitgeber vergütet werden, steht der steuerpflichtigen Person kein Abzug zu.»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0060.md) `zh-wl-2025__c0060` – «Unselbständigerwerbende haben der Steuererklärung ein vollständig und genau ausgefülltes»

## Hilfsblatt Versicherungsprämien (Form. 365)

<a id="form-365-teil-a-ziff-1-4-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil A Ziff. 1–4 – Bezahlte Prämien: private Krankenversicherung (601), Unfall (602), Lebens-/Rentenversicherung (603), Zinsen von Sparkapitalien (604)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung), Versicherungsbescheinigung Rückkaufswert (Lebens-/Rentenversicherung, Steuerwert 31.12.), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post) → Jahresprämienrechnung/Prämienbescheinigung KK (Grundversicherung + Zusatz), Prämien Unfall (nicht NBUV via Lohnausweis), Lebens-/Rentenversicherung; Sparzinsen aus Steuerauszug/WV
- **Rein:** KK-Prämienabrechnung/Jahresbescheinigung → bezahlte Prämien (nach IPV-Verrechnung) Code 601 · Prämienrechnungen private Unfall- (602), Lebens-/Rentenversicherung (603) · Wertschriftenverzeichnis → Zinsen von Sparkapitalien (604)
- **Rechnen:** Σ 601–604 = Zwischentotal 607; − IPV 605 = Total (A) 606
- **Regel:** Tatsächlich im Jahr 2025 bezahlte Prämien für Kranken-, Unfall-, Lebens- und Rentenversicherung sowie Zinsen von Sparkapitalien (gemäss WV). Im Lohnausweis bereits abgezogene Prämien (NBUV) nicht nochmals.
- **Beachten:** Nur tatsächlich bezahlte Prämien; IPV meist mit KK-Prämie verrechnet → reduzierte Prämie in 601
- **Beachten:** NBUV ist im Nettolohn (Lohnausweis) bereits abgezogen → nicht nochmals erfassen
- **Beachten:** (A) einspaltig; Begrenzung erst in Teil B/C getrennt Kanton / Bund
- **Quellen:**
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md) `zh-form-365-2025__c0001` – «1. Private Krankenversicherungsprämien 601»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md) `zh-form-365-2025__c0001` – «4. Zinsen von Sparkapitalien 604»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0083.md) `zh-wl-2025__c0083` – «Tatsächlich bezahlte Einlagen, Prämien und Beiträge für private Kranken-, Unfall-, Lebens- und»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0032.md) `zh-wl-2025__c0032` – «der laufenden Beiträge an Personalvorsorgeeinrichtungen sowie der Prämien an die obligatorische Nichtberufsunfallversicherung»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «Maximaler Abzug für Versicherungsprämien und Zinsen von Sparkapitalien Staatssteuer Bundessteuer»

<a id="form-365-teil-a-ziff-6-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil A Ziff. 6 – Abzüglich erhaltene Prämienverbilligungen (Code 605); Total (A) (Code 606)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Prämienrechnung / Jahresbescheinigung (Grund- und Zusatzversicherung) → Prämienrechnung/Bescheinigung Krankenversicherer (Verrechnung IPV), IPV-Verfügung
- **Rein:** KK-Prämienabrechnung → verrechnete Prämienverbilligung (dann in 601 netto) · IPV-Verfügung/Auszahlungsbeleg → nicht verrechnete Prämienverbilligung → Code 605
- **Rechnen:** (A) 606 = Zwischentotal 607 − IPV 605 (nur soweit nicht schon in 601 gekürzt)
- **Regel:** Individuelle Prämienverbilligung wird meist mit den KK-Prämien verrechnet: dann die um die Verbilligung reduzierten Prämien in Ziffer 1 eintragen; sonst hier abziehen (kein Doppelabzug).
- **Beachten:** Auch IPV für die unterhaltenen Kinder anrechnen
- **Beachten:** Kein Doppelabzug: IPV entweder in 601 gekürzt oder hier abziehen
- **Quellen:**
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md) `zh-form-365-2025__c0001` – «6. Abzüglich erhaltene Prämienverbilligungen 605»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0084.md) `zh-wl-2025__c0084` – «Prämienverbilligungen der Krankenversicherer, die für den Steuerpflichtigen und die von»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md) `zh-form-365-2025__c0001` – «(soweit nicht schon unter Ziffer 1. berücksichtigt)»

<a id="form-365-teil-b-ziff-1-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil B Ziff. 1 – Maximalabzug Verheiratete: CHF 5’800 / 8’700 (Staat), CHF 3’700 / 5’550 (Bund) (Code 611)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Pensionskasse ja/nein, Säule 3a bezahlt)
- **Rein:** Lohnausweis → Ziff. 10.1 ordentliche Beiträge 2. Säule (ja/nein) · 3a-Bescheinigung → Beiträge Säule 3a geleistet (ja/nein) · Steuererklärung S. 1 → Zivilstand (ungetrennte Ehe)
- **Rechnen:** Mit Beiträgen 2./3a: Kanton CHF 5'800 / Bund CHF 3'700; ohne: + Hälfte = Kanton 8'700 / Bund 5'550 (Code 611)
- **Regel:** Verheiratete in ungetrennter Ehe: CHF 5’800 (Staat) / CHF 3’700 (Bund) mit Beiträgen an 2. Säule oder 3a; ohne solche Beiträge um die Hälfte erhöht (CHF 8’700 / CHF 5’550).
- **Beachten:** Gilt für rechtlich und tatsächlich ungetrennte Ehe
- **Beachten:** Erhöhung nur, wenn weder Steuerpflichtige noch Arbeitgeber Beiträge an 2. Säule oder 3a geleistet haben
- **Beachten:** Kinder-/Unterstützungszuschlag separat in B.3 addieren
- **Limiten:**
  - Versicherungsabzug gemeinsam Besteuerte (CHF): Kanton **CHF 5'800 (Versicherungsprämien und Sparzinsen, in ungetrennter Ehe Lebende, MIT Beiträgen an 2. Säule/Säule 3a: max. CHF 5'800 (Staatssteuer).)** · Bund **CHF 3'700 (Versicherungsprämien und Sparkapitalzinsen, Ehepaare mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug gemeinsam Besteuerte ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 8'700 (Gemeinsam Besteuerte ohne Beiträge an 2. Säule und Säule 3a: Abzug erhöht sich um die Hälfte, max. CHF 8'700.)** · Bund **CHF 5'550 (Ehepaare ohne Beiträge an Säule 2/3a (Erhöhung um die Hälfte))**
- **Bund:** Bund: CHF 3’700 / 5’550.
- **Quellen:**
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «die Beiträge an die 2. oder 3. Säule a geleistet haben 5’800 3’700»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «oder: sofern weder Beiträge an die 2. noch an die 3. Säule a geleistet wurden 8’700 5’550»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t2.md) `zh-stg-2025__par-31-t2` – «bis zum Gesamtbetrag von Fr. 5800 für in ungetrennter Ehe lebende Steuerpflichtige und von Fr. 2900 für die übrigen Steuerpflichtigen»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t2.md) `bund-dbg-2025__art-33-t2` – «3700 Franken für Ehepaare, die in rechtlich und tatsächlich ungetrennter Ehe leben,»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0035.md) `zh-wl-2025__c0035` – «10.1 Ordentliche Beiträge – Cotisations ordinaires – Contributi ordinari»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0086.md) `zh-wl-2025__c0086` – «CHF 5’800 für verheiratete Personen in rechtlich und tatsächlich ungetrennter Ehe.»
  - [WL ZH 2025 S. 15](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0086.md) `zh-wl-2025__c0086` – «CHF 3’700 für verheiratete Personen in rechtlich und tatsächlich ungetrennter Ehe.»

<a id="form-365-teil-b-ziff-2-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil B Ziff. 2 – Maximalabzug übrige Steuerpflichtige: CHF 2’900 / 4’350 (Staat), CHF 1’800 / 2’700 (Bund) (Code 612)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Pensionskasse ja/nein, Säule 3a bezahlt)
- **Rein:** Lohnausweis → Ziff. 10.1 ordentliche Beiträge 2. Säule (ja/nein) · 3a-Bescheinigung → Beiträge Säule 3a geleistet (ja/nein) · Steuererklärung S. 1 → Zivilstand (nicht in ungetrennter Ehe)
- **Rechnen:** Mit Beiträgen 2./3a: Kanton CHF 2'900 / Bund CHF 1'800; ohne: + Hälfte = Kanton 4'350 / Bund 2'700 (Code 612)
- **Regel:** Alle übrigen Steuerpflichtigen (nicht in ungetrennter Ehe): CHF 2’900 (Staat) / CHF 1’800 (Bund), ohne Beiträge an 2. Säule/3a um die Hälfte erhöht (CHF 4’350 / CHF 2’700).
- **Beachten:** Alle nicht in ungetrennter Ehe Lebenden (Ledige, Verwitwete, Geschiedene, Getrennte)
- **Beachten:** Erhöhung nur, wenn weder Steuerpflichtige noch Arbeitgeber Beiträge an 2. Säule oder 3a geleistet haben
- **Limiten:**
  - Versicherungsabzug übrige Steuerpflichtige (CHF): Kanton **CHF 2'900 (Übrige Steuerpflichtige MIT Beiträgen an 2. Säule/Säule 3a: max. CHF 2'900 (Staatssteuer).)** · Bund **CHF 1'800 (Übrige Steuerpflichtige (Ledige, Verwitwete, Geschiedene, Getrennte) mit Beiträgen an Säule 2/3a)**
  - Versicherungsabzug übrige ohne Beiträge 2. Säule/3a (CHF): Kanton **CHF 4'350 (Übrige Steuerpflichtige ohne Beiträge an 2. Säule/3a: max. CHF 4'350 (2'900 + die Hälfte).)** · Bund **CHF 2'700 (Übrige Steuerpflichtige ohne Beiträge an Säule 2/3a)**
- **Bund:** Bund: CHF 1’800 / 2’700.
- **Quellen:**
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «die Beiträge an die 2. oder 3. Säule a geleistet haben 2’900 1’800»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «oder: sofern weder Beiträge an die 2. noch an die 3. Säule a geleistet wurden 4’350 2’700»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t2.md) `bund-dbg-2025__art-33-t2` – «1800 Franken für die übrigen Steuerpflichtigen;»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0035.md) `zh-wl-2025__c0035` – «10.1 Ordentliche Beiträge – Cotisations ordinaires – Contributi ordinari»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0088.md) `zh-wl-2025__c0088` – «CHF 2’900 für alle übrigen Steuerpflichtigen.»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0088.md) `zh-wl-2025__c0088` – «Wenn von den Steuerpflichtigen oder ihrem Arbeitgeber keine Beiträge an»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0090.md) `zh-wl-2025__c0090` – «CHF 1’800 für alle übrigen Steuerpflichtigen.»

<a id="form-365-teil-b-ziff-3-abzug-versicherungspraemien"></a>
### Ziff. Form. 365 Teil B Ziff. 3 – Zusätzlicher Abzug je Kind / unterstützungsbedürftige Person: CHF 1’300 Staat, CHF 700 Bund (Code 613–615)

- **Schlüssel:** `abzug.versicherungspraemien` (Versicherungsprämien und Zinsen von Sparkapitalien) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Angaben Seite 1 (Kinder, unterstützte Personen mit Kinder-/Unterstützungsabzug)
- **Rein:** Steuererklärung S. 1 → Anzahl Kinder bzw. unterstützte Personen mit Kinder-/Unterstützungsabzug
- **Rechnen:** Kinder × Kanton CHF 1'300 / Bund 700 (613); unterstützte Personen × 1'300 (614) / 700 (615); halber Kinderabzug 650 / 350; (B) 616 = B.1 bzw. B.2 + B.3
- **Regel:** Für jedes Kind oder jede unterstützungsbedürftige Person mit Anspruch auf Kinder-/Unterstützungsabzug: CHF 1’300 (Staat) / CHF 700 (Bund); bei halbem Kinderabzug CHF 650 / CHF 350. Anzahl eintragen; Total (B) = Code 616.
- **Beachten:** Nur für Kinder/Personen, für die ein Kinder- oder Unterstützungsabzug zusteht
- **Beachten:** Halber Kinderabzug → halber Zuschlag (Kanton 650 / Bund 350)
- **Limiten:**
  - Versicherungsabzug Zuschlag pro Kind/unterstützte Person (CHF): Kanton **CHF 1'300 (Zusätzlicher Versicherungsabzug von CHF 1'300 für jedes Kind oder jede unterstützungsbedürftige Person, für die ein Abzug nach § 34 Abs. 1 geltend gemacht werden kann (Bund: CHF 700).)** · Bund **CHF 700 (Zuschlag pro Kind bzw. unterstützungsbedürftige Person mit Abzug nach Art. 35 Abs. 1 lit. a/b DBG)**
- **Bund:** Bund: CHF 700 bzw. 350.
- **Quellen:**
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «Zusätzlicher Abzug für jedes Kind Anzahl: 1’300 700 613»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0091.md) `zh-wl-2025__c0091` – «CHF 650 für jedes Kind, für das der steuerpflichtigen Person ein halber Kinderabzug-»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0091.md) `zh-wl-2025__c0091` – «CHF 350 für jedes Kind, für das der steuerpflichtigen Person ein halber Kinderabzug zusteht.»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «Total der Abzüge für Versicherungsprämien und Zinsen von Sparkapitalien (B) 616»

<a id="form-365-teil-c-berechnung-total"></a>
### Ziff. Form. 365 Teil C – Abzug = niedrigerer Betrag von (A) und (B) (Code 270) → Steuererklärung Ziff. 15

- **Schlüssel:** `berechnung.total` (Berechnungs-/Totalzeilen (Nettoeinkommen, Reineinkommen, steuerbares Einkommen/Vermögen, Totale)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Formular 365
- **Rein:** Übertrag (A) Code 606 und (B) Code 616 aus Form. 365
- **Rechnen:** Code 270 = min((A); (B)) je Spalte Kanton / Bund → HF S. 3 Ziff. 15
- **Regel:** Der niedrigere der Beträge (A) bezahlte Prämien / (B) Maximalabzug; Staat und Bund getrennt rechnen; Übertrag in Ziff. 15.
- **Beachten:** (A) einspaltig; (B) und Abzug C getrennt nach Staats- und Bundessteuer
- **Quellen:**
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0003.md) `zh-form-365-2025__c0003` – «Der niedrigere Betrag: (A) oder (B) 270»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md) `zh-form-365-2025__c0001` – «Total bezahlte Versicherungsprämien und Zinsen von Sparkapitalien (A) 606»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0002.md) `zh-form-365-2025__c0002` – «Total der Abzüge für Versicherungsprämien und Zinsen von Sparkapitalien (B) 616»

## Hilfsblatt Wertschriftenverzeichnis (Form. 340)

<a id="form-340-kolonne-a-einkommen-wertschriften"></a>
### Ziff. Form. 340 Kolonne A – Werte mit Verrechnungssteuerabzug – Bruttoertrag A (Code 2309-xx; Zwischentotal 539)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Depotauszug / Wertschriftenverzeichnis der Bank (Titelbestand per 31.12.) → Steuerauszug / Zinsausweis / Dividendenabrechnung (Bruttoertrag, 35 % VSt abgezogen)
- **Rein:** Bank-Steuerverzeichnis → Steuerwert 31.12.2025 + Bruttoertrag A · Zins-/Dividendengutschriften → Bruttoertrag vor 35 % VSt · Festgeld-/Kassenobligationen-Abrechnungen, Ausschüttungsbescheinigungen nicht kotierter Titel → beilegen
- **Rechnen:** Bruttoertrag A = Σ Erträge mit VSt-Abzug (brutto); Zwischentotal 539; VSt-Anspruch 540 = 35 % × Total A
- **Regel:** Konti, Kassenobligationen, inländische Aktien/Fonds/Obligationen mit Verrechnungssteuerabzug (auch Kundenguthaben mit Bruttozins über CHF 200). Bruttoertrag in Kolonne A; Steuerwert per 31.12. in Kolonne Steuerwert. Anspruch Verrechnungssteuer = 35 % von Total Bruttoertrag A (Code 540).
- **Beachten:** Kundenguthaben nur bei Bruttozins > CHF 200 in A, sonst Kolonne B
- **Beachten:** Steuerwert: CH-Titel gemäss ESTV-Kursliste 31.12.2025; inländische Fonds: auch thesaurierte Erträge steuerbar
- **Beachten:** Gratisaktien bei Ausgabe steuerbar; Q-Beteiligungen brutto (ungekürzt) erfassen
- **Quellen:**
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Zwischentotal Bruttoerträge 539 542»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0162.md) `zh-wl-2025__c0162` – «Die Zinsen und Dividenden schweizerischer Wertpapiere sind der schweizerischen Verrech-»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0162.md) `zh-wl-2025__c0162` – «nungssteuer unterworfen. Dies gilt auch für Kundenguthaben mit einem Bruttozins von mehr als»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0156.md) `zh-wl-2025__c0156` – «der amtlichen Steuerkursliste 31.12.2025 der Eidgenössischen»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0166.md) `zh-wl-2025__c0166` – «Neben den ausgeschütteten sind auch zurückbehaltene (thesaurierte) Erträge steuerbar.»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0164.md) `zh-wl-2025__c0164` – «Erträge aus Gratisaktien sind seit dem 1.1.2020»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0165.md) `zh-wl-2025__c0165` – «Sie sind ungekürzt, d.h. mit dem Bruttobetrag der Ausschüttung,»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0163.md) `zh-wl-2025__c0163` – «Bei nicht kotierten Titeln ist stets die Bescheinigung über»
  - [Formular 340 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0003.md) `zh-form-340-2025__c0003` – «A Werte mit Verrechnungssteuerabzug, deren Erträge um 35% eidg. Verrechnungssteuer»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0168.md) `zh-wl-2025__c0168` – «(Zinsertrag bis und mit CHF 200)»

<a id="form-340-kolonne-b-einkommen-wertschriften"></a>
### Ziff. Form. 340 Kolonne B – Werte ohne Verrechnungssteuerabzug – Bruttoertrag B (Code 542)

- **Schlüssel:** `einkommen.wertschriften` (Ertrag aus Wertschriften und Guthaben (gem. Wertschriftenverzeichnis)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug), Kontoauszug / Zins- und Saldobescheinigung (Sparkonto, Privatkonto, Festgeld, Post), Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA), Krypto-Auszug (Exchange-/Wallet-Auszug, Jahresendbestand) → Steuerauszug / ausländische Abrechnungen / Zinsbescheinigungen
- **Rein:** Bank-Steuerauszug → Erträge ohne VSt (Zins ≤ CHF 200, ausländische Titel/Fonds) · Ausländische Ertragsabrechnungen → Bruttoertrag in CHF (Tageskurs) · Wallet-Auszug per Jahresende → Krypto-Steuerwert (ESTV-Jahresendkurs) · Darlehensverträge, STWEG-Abrechnung, Vergütungszinsen → Erträge
- **Rechnen:** Bruttoertrag B = Σ Erträge ohne VSt-Abzug (Fremdwährung × Tageskurs); Zwischentotal 542; Total A + B = 539 + 542 = Code 150 → HF Ziff. 4.1
- **Regel:** Erträge ohne Verrechnungssteuerabzug: Kundenguthaben bis CHF 200 Zins, Darlehen, ausländische Wertschriften (Umrechnung zu Kursliste-Devisenkursen), Stockwerkeigentümer-Anteile, Vergütungszinsen, ausländische Spielbanken/Lotterien/Sportwetten. Total A + B = Code 150.
- **Beachten:** Steuerwerte ausländischer Titel/Guthaben zu ESTV-Devisenkursen 31.12.2025 umrechnen
- **Beachten:** Natural-/Sachgewinne: Freigrenze Kanton CHF 1'000 / Bund CHF 1'100 (darüber ganz steuerbar)
- **Beachten:** Ausländische Fonds/SICAV wie inländische (thesauriert steuerbar), aber in Kolonne B
- **Limiten:**
  - Lotterie-/Kleingewinne steuerfrei bis (CHF): Kanton **CHF 1'000 (Einzelne Gewinne aus Lotterien und Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei, sofern die Grenze von CHF 1'000 nicht überschritten wird.)** · Bund **CHF 1'100 (Einzelne Gewinne aus Lotterien/Geschicklichkeitsspielen zur Verkaufsförderung steuerfrei bis CHF 1'100)**
- **Quellen:**
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0168.md) `zh-wl-2025__c0168` – «Kundenguthaben, wenn der Zins nicht um die eidg. Verrechnungssteuer gekürzt wurde»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Total Bruttoertrag A + B 150»
  - [WL ZH 2025 S. 27](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0170.md) `zh-wl-2025__c0170` – «Devisen ausgerichteten Erträge solcher Wertschriften sind zum Tageskurs in Schweizer»
  - [WL ZH 2025 S. 27](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0170.md) `zh-wl-2025__c0170` – «aber in Kolonne B zu deklarieren.»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0156.md) `zh-wl-2025__c0156` – «der amtlichen Steuerkursliste aufgeführten Devisenkursen per 31.12.2025 vorzunehmen.»
  - [WL ZH 2025 S. 25](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0159.md) `zh-wl-2025__c0159` – «Der Nachweis hat mittels Kontoauszug der digitalen Brieftasche (Wallet), Stand per Ende der Steuerperiode, zu erfolgen.»
  - [WL ZH 2025 S. 27](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0169.md) `zh-wl-2025__c0169` – «CHF 1’100 (Bundessteuer) überschritten, so ist der gesamte Gewinn steuerbar (Freigrenze).»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «4.1 Ertrag aus Wertschriften, Guthaben und Lotterien Wertschriftenverzeichnis 150»

<a id="form-340-totale-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 340 Totale – Total Steuerwert (Code 400) und Verrechnungssteueranspruch 35 % (Code 540)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Steuerauszug (Verrechnungssteuer-Betrag)
- **Rein:** Summen Kolonnen Steuerwert, A, B inkl. Beiblätter (2350/2352, 2360/2362) und DA-1 (2370/2371) · Steuerauszug → Kontrolle VSt-Betrag (35 % auf Kolonne A)
- **Rechnen:** Total Steuerwert 400 → HF S. 4 Ziff. 30.1; Total A + B 150 → HF S. 2 Ziff. 4.1; VSt-Anspruch 540 = 35 % × Total A, auf 5 Rappen runden
- **Regel:** Total Steuerwert → Ziff. 30.1 (Seite 4); Total Bruttoertrag A + B → Ziff. 4.1 (Seite 2). Die 35 % Verrechnungssteuer auf Kolonne A werden mit der Steuerrechnung verrechnet bzw. zurückerstattet (Bankverbindung angeben).
- **Beachten:** VSt-Rückerstattung wird mit der Steuererklärung beantragt (WV mit Verrechnungsantrag); IBAN angeben
- **Beachten:** Anspruch erlischt, wenn nicht innert dreier Jahre nach Ablauf des Fälligkeitsjahres gestellt
- **Beachten:** WV unterschreiben (Bestätigung VSt-Abzug auf Kolonne A); Q-Ertrag 151 → Ziff. 4.2
- **Quellen:**
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «35% von Total Bruttoertrag A 540»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Total Steuerwert 400»
  - [WL ZH 2025 S. 34](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0220.md) `zh-wl-2025__c0220` – «5 Rappen zu runden.»
  - [ZStB 133.1 (Aufforderung 2026) S. 5–6](../../chunks/zh/2025/zh-zstb-133-1-aufforderung-2026/zh-zstb-133-1-aufforderung-2026__c0016.md) `zh-zstb-133-1-aufforderung-2026__c0016` – «Natürliche Personen beantragen die Rückerstattung der Verrechnungssteuer zusammen mit der Steuererklärung»
  - [ZStB 133.1 (Aufforderung 2026) S. 5–6](../../chunks/zh/2025/zh-zstb-133-1-aufforderung-2026/zh-zstb-133-1-aufforderung-2026__c0016.md) `zh-zstb-133-1-aufforderung-2026__c0016` – «Der Anspruch auf Rückerstattung erlischt, wenn er nicht innert dreier Jahre nach Ablauf des»
  - [Formular 340 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0001.md) `zh-form-340-2025__c0001` – «Bankverbindung für Rückerstattungen»
  - [Formular 340 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0001.md) `zh-form-340-2025__c0001` – «allen unter Kolonne A angegebenen Erträgen die eidg. Verrechnungssteuer zu meinen oder zu Lasten der von mir vertretenen Steuer»
  - [Formular 340 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0003.md) `zh-form-340-2025__c0003` – «Steuererklärung Seite 2, Ziffer 4.2»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «4.1 Ertrag aus Wertschriften, Guthaben und Lotterien Wertschriftenverzeichnis 150»

<a id="form-340-da-1-verrechnungssteuer-rueckerstattung"></a>
### Ziff. Form. 340 DA-1 – Anrechnung ausländischer Quellensteuern / Übertrag ab Formular DA-1 (Code 2370/2371)

- **Schlüssel:** `verrechnungssteuer.rueckerstattung` (Rückforderung Verrechnungssteuer (Wertschriftenverzeichnis), DA-1) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Dividenden-/Zinsabrechnung Ausland mit Quellensteuer (inkl. DA-1, USA) → Formular DA-1 (Antrag Anrechnung ausländischer Quellensteuern) + Dividendenabrechnung
- **Rein:** Ertragsabrechnungen ausländischer Titel → Bruttoertrag (100 %), ausländische Quellensteuer · Bankbelege/Sammelausweise US-Titel → zusätzlicher Steuerrückbehalt USA · Formular DA-1 Seite 3 Totale → WV-Zeile «Übertrag ab Formular DA-1» (2370/2371)
- **Rechnen:** DA-1-Totale → WV-Zeile 2370/2371, Bruttoertrag in Kolonne B; Anrechnung nur, wenn Σ nicht rückforderbare ausl. Quellensteuer > CHF 100
- **Regel:** Ausländische Dividenden/Zinsen mit Quellensteuer-Anrechnung im DA-1 aufführen; Totalbeträge in die Zeile «Übertrag ab Formular DA-1» (Bruttoertrag unter Kolonne B). Keine Anrechnung, wenn die nicht rückforderbaren ausländischen Steuern insgesamt CHF 100 nicht übersteigen.
- **Beachten:** ≤ CHF 100, quellensteuerfrei oder voll rückforderbar: nicht ins DA-1, nur WV Kolonne B
- **Beachten:** Steuerrückbehalt USA: kein Mindestbetrag, ohne Bankbelege keine Rückerstattung
- **Beachten:** Anspruch erlischt drei Jahre nach Ablauf der Fälligkeitsperiode; DA-1 inkl. Abrechnungen beilegen
- **Quellen:**
  - [WL ZH 2025 S. 27](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0171.md) `zh-wl-2025__c0171` – «ren. Die Totalbeträge des DA-1 übertragen Sie in die Zeile «Übertrag ab Formular DA-1» im»
  - [WL ZH 2025 S. 27](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0171.md) `zh-wl-2025__c0171` – «insgesamt den Betrag von CHF 100 nicht übersteigen, wird keine Anrechnung ausländischer»
  - [Formular 340 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0005.md) `zh-form-340-2025__c0005` – «Übertrag ab Formular DA-1 2370 2371»
  - [WL DA-1/DA-3 2025 S. 1](../../chunks/zh/2025/zh-wl-da1-2025/zh-wl-da1-2025__c0007.md) `zh-wl-da1-2025__c0007` – «Die Total-Werte auf Seite 3 des Formulars DA-1 sind in die angegebenen Ziffern des»
  - [WL DA-1/DA-3 2025 S. 1](../../chunks/zh/2025/zh-wl-da1-2025/zh-wl-da1-2025__c0007.md) `zh-wl-da1-2025__c0007` – «Das vollständig ausgefüllte Formular DA-1 (inkl. sämtlicher Ertragsabrechnungen) muss nur der»
  - [WL DA-1/DA-3 2025 S. 2](../../chunks/zh/2025/zh-wl-da1-2025/zh-wl-da1-2025__c0010.md) `zh-wl-da1-2025__c0010` – «Die ausländischen Kapitalerträge müssen brutto (zu 100 %) deklariert bzw. versteuert werden.»
  - [WL DA-1/DA-3 2025 S. 2](../../chunks/zh/2025/zh-wl-da1-2025/zh-wl-da1-2025__c0012.md) `zh-wl-da1-2025__c0012` – «Dividenden und Zinsen, die überhaupt keiner Steuer im Quellenstaat unterliegen oder»
  - [WL DA-1/DA-3 2025 S. 2](../../chunks/zh/2025/zh-wl-da1-2025/zh-wl-da1-2025__c0013.md) `zh-wl-da1-2025__c0013` – «Für Positionen ohne Belege wird die Rückerstattung des zusätzlichen Steuerrückbehalts abgelehnt.»
  - [WL DA-1/DA-3 2025 S. 2](../../chunks/zh/2025/zh-wl-da1-2025/zh-wl-da1-2025__c0013.md) `zh-wl-da1-2025__c0013` – «des zusätzlichen Steuerrückbehalts kein Mindestbetrag von CHF 100.–»
  - [WL DA-1/DA-3 2025 S. 2](../../chunks/zh/2025/zh-wl-da1-2025/zh-wl-da1-2025__c0011.md) `zh-wl-da1-2025__c0011` – «Der Anspruch erlischt, wenn er nicht innert drei Jahren nach Ablauf der Steuerperiode, in der die Erträgnisse fällig geworden sind»

<a id="form-340-code-q-g-n-e-s-einkommen-beteiligungen-qualifiziert"></a>
### Ziff. Form. 340 Code Q/G/N/E/S – Kennzeichnung: G Geschäftsvermögen, N Nutzniessung, E Erbschaft, S Schenkung, Q qualifizierte Beteiligung ≥ 10 %

- **Schlüssel:** `einkommen.beteiligungen_qualifiziert` (Erträge aus qualifizierten Beteiligungen (Teilbesteuerung)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Steuerauszug der Bank / Post (inkl. eSteuerauszug) → Steuerauszug / Erb- und Schenkungsunterlagen
- **Rein:** Beteiligungsnachweis/Steuerauszug → Quote ≥ 10 % am Kapital → Code Q · Erbteilungs-/Schenkungsunterlagen → 2025 erhaltene Werte → Code E / S · Nutzniessungs-/Geschäftsunterlagen → Code N / G
- **Rechnen:** Kennzeichnung je Zeile; Σ Erträge Q = Code 151 → HF Ziff. 4.2; Abzug HF Ziff. 16.5 (Privatvermögen) = Q-Ertrag × Kanton 50 % / Bund 30 %; E/S → HF Ziff. 50
- **Regel:** Besondere Vermögenswerte mit Code kennzeichnen (Q → Ziff. 4.2 und Teilbesteuerungsabzug Ziff. 16.5; E/S → Ziff. 50). Vermögen/Ertrag Kinder Jg. 2008 und jünger sind im Verzeichnis der Eltern, Jg. 2007 und älter selbst zu deklarieren.
- **Beachten:** Q-Erträge ungekürzt (brutto), in A oder B je nach VSt-Pflicht; Formular «Qualifizierte Beteiligungen» beilegen
- **Beachten:** Kinder Jg. 2008 und jünger im WV der Eltern; Jg. 2007 und älter eigenes WV
- **Beachten:** Nutzniessungsvermögen (N) beim Nutzniesser; 2. Säule/3a-Ansprüche bis Fälligkeit nicht im WV
- **Quellen:**
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0155.md) `zh-wl-2025__c0155` – «mit Q Beteiligungen von mindestens 10 Prozent am Aktien-, Grund- oder Stammkapital an»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0154.md) `zh-wl-2025__c0154` – «minderjährigen Kinder des Jahrgangs 2008 und jüngeren sowie das Vermögen, an dem Sie»
  - [Formular 340 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-340-2025/zh-form-340-2025__c0003.md) `zh-form-340-2025__c0003` – «qualifizierten Beteiligungen 151»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «4.2 Davon aus qualifizierten Beteiligungen»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md) `zh-wl-2025__c0104` – «für qualifizierte Beteiligungen im Privatvermögen beträgt 50%»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md) `zh-wl-2025__c0104` – «qualifizierte Beteiligungen im Privatvermögen beträgt 30%»
  - [WL ZH 2025 S. 26](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0165.md) `zh-wl-2025__c0165` – «Sie sind ungekürzt, d.h. mit dem Bruttobetrag der Ausschüttung,»
  - [WL ZH 2025 S. 31](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0206.md) `zh-wl-2025__c0206` – «Formular «Qualifizierte Beteiligungen im Privatvermögen», bzw. Formular «Qualifizierte»
  - [WL ZH 2025 S. 7](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0016.md) `zh-wl-2025__c0016` – «Seite 4 unter Ziffer 50 der Steuererklärung»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.5 Weitere Abzüge (z.B. Beiträge an politische Parteien)»
  - [WL ZH 2025 S. 17](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0104.md) `zh-wl-2025__c0104` – «Nicht steuerbarer Teil der Erträge aus qualifizierten Beteiligungen bei den Staats-»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0154.md) `zh-wl-2025__c0154` – «sind bis zur Fälligkeit der Leistungen steuerfrei und nicht im Wertschriftenverzeichnis aufzuführen.»
  - [WL ZH 2025 S. 24](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0154.md) `zh-wl-2025__c0154` – «sowie das Vermögen, an dem Sie die Nutzniessung haben.»

## Hilfsblatt Schulden (Form. 355)

<a id="form-355-spalte-schuld-schulden-privat"></a>
### Ziff. Form. 355 Spalte Schuld – Privatschulden inkl. Grundpfandschulden am 31. Dezember – Total (Code 3200) → Ziff. 34

- **Schlüssel:** `schulden.privat` (Private Schulden (Hypotheken, Darlehen, Kredite)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen), Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung) → Bankbestätigung/Hypothekarbestätigung per 31.12.2025 (Gläubiger, Saldo, Zinssatz)
- **Rein:** Hypothekar-/Kreditbestätigung per 31. Dezember → Saldo, Gläubiger mit Adresse, Zinssatz · Private Darlehensverträge → Saldo per 31. Dezember, Gläubiger · Zinsbelege → Spalte Schuldzinsen (Code 3201)
- **Rechnen:** Σ Schulden per 31. Dezember (CHF ohne Rappen) = Code 3200 → HF S. 4 Ziff. 34 (Code 470); Σ Schuldzinsen 3201 → HF S. 3 Ziff. 12 (Code 250)
- **Regel:** Pro Gläubiger Name/Adresse, Schuldbetrag per 31.12. in CHF ohne Rappen eintragen; Total nach Seite 4, Ziff. 34.
- **Beachten:** Bei Schulden vollständiges Verzeichnis einreichen; Gläubiger mit genauer Adresse und Zinssatz unerlässlich
- **Beachten:** Schuldzinsen ohne Amortisationen und Leasingraten
- **Beachten:** Unverteilte Erbschaft: Schulden und Schuldzinsen anteilmässig
- **Quellen:**
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0001.md) `zh-form-355__c0001` – «Privatschulden inkl. Grundpfandschulden Schuld am 31. Dezember Schuldzinsen»
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0002.md) `zh-form-355__c0002` – «Total Privatschulden / private Schuldzinsen 3200 / 3201»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0141.md) `zh-wl-2025__c0141` – «Werden Schulden deklariert, ist ein vollständiges Schuldenverzeichnis mit der Steuererklärung einzureichen.»
  - [WL ZH 2025 S. 22](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0141.md) `zh-wl-2025__c0141` – «Unerlässlich ist insbesondere die Angabe des Gläubigers mit genauer Adresse sowie des Zinssatzes.»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0073.md) `zh-wl-2025__c0073` – «abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den»
  - [WL ZH 2025 S. 23](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0150.md) `zh-wl-2025__c0150` – «Die Schulden und Schuldzinsen der unverteilten Erbschaft sind anteilmässig in der Steuer-»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «34. Schulden Schuldenverzeichnis 470»
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0002.md) `zh-form-355__c0002` – «Steuererklärung Seite 4, Ziffer 34 Steuererklärung Seite 3, Ziffer 12»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «12. Schuldzinsen (soweit nicht schon unter Ziff. 2 abgezogen) Schuldenverzeichnis 250»

<a id="form-355-spalte-schuldzinsen-abzug-schuldzinsen"></a>
### Ziff. Form. 355 Spalte Schuldzinsen – Schuldzinsen des Jahres – Total (Code 3201) → Ziff. 12

- **Schlüssel:** `abzug.schuldzinsen` (Private Schuldzinsen) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Kredit-/Darlehensvertrag, Privatkredit, Lombard-, Konsum- oder Familiendarlehen (Zinsbescheinigung), Hypothekarbestätigung / Zinsbescheinigung der Bank (Hypothekar- und Baukreditzinsen) → Zinsabrechnung der Bank für 2025
- **Rein:** Zinsabrechnung/Hypothekarbestätigung Bank 2025 → Schuldzinsen je Gläubiger (Spalte Schuldzinsen) · Darlehens-/Kreditvertrag, Zinsbestätigung privater Gläubiger → Name, Vorname, Adresse Gläubiger + Zins · Saldobestätigung per 31.12.2025 → Spalte «Schuld am 31. Dezember» (Total 3200 → Ziff. 34, Code 470)
- **Rechnen:** Σ Schuldzinsen (3201) → Ziff. 12 (250); max. Ertrag bewegl. + unbewegl. Privatvermögen (inkl. EMW) + 50’000 (Kanton = Bund; Bund: Teilbest.-Beteiligungen zu 70 %)
- **Regel:** Bezahlte Schuldzinsen 2025 pro Gläubiger; Total nach Seite 3, Ziff. 12 (Begrenzung Vermögensertrag + CHF 50’000 beachten, Baurechtszinsen separat im Liegenschaftenverzeichnis).
- **Beachten:** Nicht abziehbar: Amortisationen, Leasingraten (inkl. Zinsanteil); Bund: Baukreditzinsen (= Anlagekosten)
- **Beachten:** Baurechtszinsen nicht hier, sondern beim Liegenschaftsunterhalt (nicht unter der 50’000-Begrenzung)
- **Beachten:** Nur soweit nicht schon unter Ziff. 2 abgezogen; Bund: im Jahr 2025 fällig gewordene Zinsen
- **Quellen:**
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0002.md) `zh-form-355__c0002` – «Total Privatschulden / private Schuldzinsen 3200 / 3201»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0074.md) `zh-wl-2025__c0074` – «mögen (inkl. Eigenmietwert) und weiterer CHF 50’000 nicht übersteigen.»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0073.md) `zh-wl-2025__c0073` – «abzugsberechtigt sind Amortisationen (Schuldrückzahlungen) sowie Leasingraten (mit den»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0073.md) `zh-wl-2025__c0073` – «darin enthaltenen Zinsanteilen).»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0074.md) `zh-wl-2025__c0074` – «Baurechtszinsen sind bei den Liegenschaftenunterhaltskosten geltend zu machen»
  - [WL ZH 2025 S. 14](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0074.md) `zh-wl-2025__c0074` – «siehe Seite 29) und fallen nicht unter die oben genannte Beschränkung.»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0007.md) `zh-form-300-2025__c0007` – «Schuldzinsen (soweit nicht schon unter Ziff. 2 abgezogen)»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «34.   Schulden   Schuldenverzeichnis 470»
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0001.md) `zh-form-355__c0001` – «Privatschulden inkl. Grundpfandschulden   Schuld am 31. Dezember   Schuldzinsen»
  - [Formular 355 ZH S. 1](../../chunks/zh/2025/zh-form-355/zh-form-355__c0001.md) `zh-form-355__c0001` – «Name, Vorname und Adresse des Gläubigers»
  - [DBG Art. 33](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-33-t1.md) `bund-dbg-2025__art-33-t1` – «die privaten Schuldzinsen im Umfang der nach den Artikeln 20, 20a und 21 steuerbaren Vermögenserträge und weiterer 50 000 Franken»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0048.md) `bund-wl-2a-2025__c0048` – «Die im Jahr 2025 fällig gewordenen Schuldzinsen sind wie folgt»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0049.md) `bund-wl-2a-2025__c0049` – «werden nur zu 70 % in die Berechnung einbezogen.»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0049.md) `bund-wl-2a-2025__c0049` – «Zu beachten ist, dass Baukreditzinsen als Anlagekosten gelten»
  - [WL 2a 2025 S. 7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0049.md) `bund-wl-2a-2025__c0049` – «und somit nicht vom Einkommen abziehbar sind.»
  - [StG ZH § 31](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-31-t1.md) `zh-stg-2025__par-31-t1` – «die privaten Schuldzinsen im Umfang der nach den §§ 20, 20 a und 21 steuerbaren Vermögenserträge und weiterer Fr. 50 000»

## Hilfsblatt Liegenschaften (Form. 350)

<a id="form-350-seite-1-vermoegen-liegenschaften"></a>
### Ziff. Form. 350 Seite 1 – Steuerwert: Verkehrswert (Codes 5541–55410; Total 3951 → Ziff. 31.1) / Ertragswert Land- und Forstwirtschaft (Codes 5531–55310; Total 3952 → Ziff. 31.2)

- **Schlüssel:** `vermoegen.liegenschaften` (Liegenschaften (Steuerwert)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Liegenschaftsbewertung des Gemeindesteueramts / Steuerwert-Mitteilung
- **Rein:** Bewertungsmitteilung Gemeindesteueramt (EFH/StWE zu Wohnzwecken) → Spalte Verkehrswert (5541 ff.) · Mieterspiegel/Ertragsaufstellung 2025 (MFH, Geschäftshaus) → Bruttojahresertrag für Ertragswertformel (Spalte Verkehrswert) · Bewertung land-/forstwirtschaftliche Liegenschaft → Spalte Ertragswert (5531 ff.) · Erbschafts-/Nutzniessungs-/Wohnrechtsunterlagen → Anteil bzw. Zuordnung der Liegenschaft
- **Rechnen:** EFH/StWE Wohnen: Wert gem. Bewertung (ZStB 21.1); MFH/Geschäftshaus/StWE Geschäft = Bruttojahresertrag 2025 × 100 / 7,05; 3951 → Ziff. 31.1 (421); 3952 → 31.2 (422)
- **Regel:** Pro Liegenschaft Ort, Art, Fläche und Steuerwert eintragen. EFH/StWE zu Wohnzwecken: Wert gemäss Bewertung des Gemeindesteueramts (ZStB 21.1); MFH/Geschäftshäuser: Ertragswert = Bruttojahresertrag 2025 x 100 / 7,05; Anteile an unverteilten Erbschaften anteilmässig.
- **Beachten:** Alle Liegenschaften deklarieren, auch in anderen Kantonen/Ausland; ohne Bewertung → Gemeindesteueramt fragen
- **Beachten:** Bruttojahresertrag inkl. Marktmietwert eigener Wohnung, ohne NK (Heizung, Warmwasser, Treppenhaus usw.)
- **Beachten:** Nutzniessung: 100 % beim Nutzniesser; Wohnrecht: 100 % beim Eigentümer; Bund: keine Vermögenssteuer
- **Quellen:**
  - [Formular 350 ZH S. 1](../../chunks/zh/2025/zh-form-350/zh-form-350__c0002.md) `zh-form-350__c0002` – «Total 3952 13213211 3951 113213211»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0197.md) `zh-wl-2025__c0197` – «folgt: Vermögenssteuerwert = Ertragswert.»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0198.md) `zh-wl-2025__c0198` – «Vermögenssteuerwert = Bruttojahresertrag x 100 / 7,05»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0174.md) `zh-wl-2025__c0174` – «Es sind alle Liegenschaften zu deklarieren, auch jene in anderen Kantonen oder im Ausland.»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0195.md) `zh-wl-2025__c0195` – «Als Vermögenssteuerwert von Einfamilienhäusern und Stockwerkeigentum zu Wohnzwecken»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0196.md) `zh-wl-2025__c0196` – «festgelegte Wert in das Liegenschaftenverzeichnis einzutragen»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0196.md) `zh-wl-2025__c0196` – «Falls Sie noch keine Bewertung erhalten haben, erkundigen Sie sich bitte beim zuständigen»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0197.md) `zh-wl-2025__c0197` – «familienhäusern und Geschäftshäusern sowie Stockwerkeigentum zu Geschäftszwecken wie»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0198.md) `zh-wl-2025__c0198` – «einschliesslich Marktmietwert einer allfällig selbstgenutzten Wohnung, jedoch»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0198.md) `zh-wl-2025__c0198` – «ohne Entschädigungen für Heizung, Warmwasser, Treppenhausreinigung»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0199.md) `zh-wl-2025__c0199` – «Geschäftsliegenschaften, werden zum Ertragswert bewertet.»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0200.md) `zh-wl-2025__c0200` – «Besteht an einer Liegenschaft eine Nutzniessung, ist der Vermögenssteuerwert zu 100% durch»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0200.md) `zh-wl-2025__c0200` – «Bei Liegenschaften, auf denen ein Wohnrecht lastet, ist der Vermögenssteuerwert zu 100%»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «31.1 Zum Verkehrswert besteuert»
  - [Formular 300 ZH 2025 S. 4](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0012.md) `zh-form-300-2025__c0012` – «31.2 Zum Ertragswert besteuert (Land- oder Forstwirtschaft)»
  - [DBG Art. 1](../../chunks/bund/2025/bund-dbg-2025/bund-dbg-2025__art-1.md) `bund-dbg-2025__art-1` – «eine Einkommenssteuer von den natürlichen Personen;»

<a id="form-350-seite-2-spalte-eigenmietwert-einkommen-liegenschaften-eigenmietwert"></a>
### Ziff. Form. 350 Seite 2 Spalte Eigenmietwert – Eigenmietwert / Miet- und Pachtzinseinnahmen (Codes 5701–57010 Wohnungen/Zimmer/Garagen; 5711–57110 gewerblich; Total 5721–57210)

- **Schlüssel:** `einkommen.liegenschaften.eigenmietwert` (Eigenmietwert selbstbewohnter Liegenschaft) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung), Mietverträge / Mietzinsabrechnung / Mietzinsaufstellung (vermietete Liegenschaft, Garage, Ferienwohnung) → Mieterspiegel / Ertragsaufstellung; Eigenmietwert-Verfügung des Gemeindesteueramts
- **Rein:** Bewertungs-/Eigenmietwertmitteilung Gemeindesteueramt → Eigenmietwert EFH/StWE (Spalte Wohnungen, 5701 ff.) · Mieterspiegel/Verwaltungsabrechnung 2025 → Mietzinsen Wohnungen/Garagen (5701 ff.) bzw. gewerblich (5711 ff.) · Vergleichsmiete bei Drittvermietung → Eigenmietwert der eigenen Wohnung im MFH/Geschäftshaus · Wohnrechts-/Nutzniessungsvertrag → Eigenmietwert beim Berechtigten
- **Rechnen:** 5721 = 5701 + 5711 (EMW + Miet-/Pachtzinsen ohne NK-Entschädigungen); EMW: EFH 3,50 % / StWE 4,25 % × Land- + Zeitbauwert; eigene Wohnung im MFH = 70 % × Drittmiete
- **Regel:** Eigenmietwert selbstgenutzter Räume (EFH 3,50 % bzw. StWE 4,25 % des Land- und Zeitbauwerts gemäss Weisung; selbstbewohnte Wohnung im eigenen MFH/Geschäftshaus 70 % des erzielbaren Mietzinses) plus sämtliche Miet-/Pachtzinseinnahmen (Garagen, Abstellplätze, Reklame) ohne Heizungs-/Warmwasser-/Treppenhaus-Entschädigungen bis zu den tatsächlichen Aufwendungen. Mieterspiegel je vermietete Liegenschaft beilegen. Wohnrecht/Nutzniessung: 100 % beim Berechtigten.
- **Beachten:** Mieterspiegel je vermietete Liegenschaft beilegen (oder Verwaltungsrechnung; sonst Beiblatt)
- **Beachten:** NK-Entschädigungen (Heizung, Warmwasser, Treppenhaus) nur bis zu den tatsächlichen Aufwendungen ausklammern
- **Beachten:** EFH/StWE: EMW gem. Weisung 2009 (ZStB 21.1), Bewertung vom Gemeindesteueramt; individuelle Schätzung: 60–70 % Marktmiete
- **Bemerkung:** Eigenmietwert-Berechnungssätze EFH/StWE hier aus WL 2025; die Weisung 2009 (zh-weisung-liegenschaften-2009, ZStB 21.1) ist die massgebende Grundlage – bei Zweifel dort prüfen.
- **Quellen:**
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0006.md) `zh-form-350__c0006` – «Als Eigenmietwert der selbst genutzten Wohnung im Mehrfamilien- und Geschäftshaus (ohne Stockwerkeigentum) sind 70% des Mietzinses einzusetzen»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0176.md) `zh-wl-2025__c0176` – «Geschäftshaus (ohne Stockwerkeigentum) sind 70% des Mietzinses einzusetzen, der bei»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0178.md) `zh-wl-2025__c0178` – «Für Einfamilienhäuser: 3,50% des Land- und Zeitbauwertes»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0179.md) `zh-wl-2025__c0179` – «Für Stockwerkeigentum: 4,25% des Land- und Zeitbauwertanteils»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0183.md) `zh-wl-2025__c0183` – «Besteht ein Wohnrecht oder eine Nutzniessung, ist der Eigenmietwert zu 100% durch die»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0003.md) `zh-form-350__c0003` – «Eigenmietwert / Miet- und Pachtzinseinnahmen»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0003.md) `zh-form-350__c0003` – «1 5701 5711 5721»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0180.md) `zh-wl-2025__c0180` – «Für jede vermietete Liegenschaft ist eine detaillierte Ertragsaufstellung (Mieterspiegel)»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0177.md) `zh-wl-2025__c0177` – «periode 2009 (ZStB 21.1) festgelegte Eigenmietwert einzusetzen»
  - [WL ZH 2025 S. 30](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0196.md) `zh-wl-2025__c0196` – «tenbewertung wird Ihnen vom Gemeindesteueramt der Liegenschaftengemeinde zugestellt.»
  - [Weisung 2009 ZH S. 16](../../chunks/zh/2025/zh-weisung-liegenschaften-2009/zh-weisung-liegenschaften-2009__c0035.md) `zh-weisung-liegenschaften-2009__c0035` – «auf 60% des Marktmietwerts festzulegen, wenn der Formelwert»
  - [Weisung 2009 ZH S. 16](../../chunks/zh/2025/zh-weisung-liegenschaften-2009/zh-weisung-liegenschaften-2009__c0035.md) `zh-weisung-liegenschaften-2009__c0035` – «auf 70% des Marktmietwerts festzusetzen, wenn der Formelwert»

<a id="form-350-seite-2-spalte-unterhalts-und-verwaltungskosten-abzug-liegenschaft-unterhalt"></a>
### Ziff. Form. 350 Seite 2 Spalte Unterhalts- und Verwaltungskosten – Unterhalts- und Verwaltungskosten: pauschal (Codes 5731–57310) oder effektiv (Codes 5741–57410)

- **Schlüssel:** `abzug.liegenschaft.unterhalt` (Liegenschaftsunterhalt (Pauschale oder effektiv), Verwaltungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen), Nebenkosten-, Versicherungs- und Verwaltungsabrechnungen Liegenschaft (Gebäudeversicherung, Grundstücksteuern, Hauswart, Verwalter) → Unterhaltsrechnungen, Versicherungsprämien Gebäude, Verwaltungsabrechnung (bei effektiv: detaillierte Aufstellung)
- **Rein:** Handwerker-/Unterhaltsrechnungen 2025 → effektive Kosten (5741 ff.) · Prämienrechnungen Gebäude-/Sachversicherung → effektive Kosten · Verwaltungs-/StWE-Abrechnung (Verwaltung durch Dritte) → effektive Kosten · Total Mietertrag/Eigenmietwert ohne NK (5721 ff.) → Basis Pauschale (5731 ff.)
- **Rechnen:** Pauschale (5731) = Bruttoertrag ohne NK × Kanton 20 % / Bund 10 % (Gebäude ≤ 10 J.) bzw. 20 %; ODER eff. (5741); 5751 = 5721 – Unterhalt; Σ 3953 → Ziff. 6 (188)
- **Regel:** Wahl pro Liegenschaft und Steuerperiode: Pauschalabzug 20 % des Brutto-Mietertrags bzw. Brutto-Mietwerts (abzüglich Heizungs-/Warmwasser-Entschädigungen) – dann keine weiteren Abzüge ausser Baurechtszinsen – oder tatsächliche Kosten mit Aufstellung (Datum, Art, Empfänger, Betrag). Pauschale nicht bei vorwiegend geschäftlich genutzten Liegenschaften. Resultat: Verbleibender Ertrag (Code 5751–57510), Total Nettoertrag Code 3953 → Ziff. 6.
- **Beachten:** Wahl je Liegenschaft und Steuerperiode; keine Pauschale bei vorwiegend geschäftlich genutzter Liegenschaft
- **Beachten:** Bei Pauschale keine weiteren Abzüge ausser Baurechtszinsen; bei Unternutzung Pauschale vom EMW nach Einschlag
- **Beachten:** Effektiv: Aufstellung (Datum, Art, Empfänger, Betrag); Abzug bei Fälligkeit oder Zahlung – einmal gewählt beibehalten
- **Limiten:**
  - Liegenschaftsunterhalt Pauschale – Gebäude bis 10 Jahre (%): Kanton **20 % (Pauschalabzug für Unterhalts- und Verwaltungskosten von Liegenschaften des Privatvermögens: 20 % des Brutto-Mietertrags bzw. Mietwerts; Wahl pro Liegenschaft und Steuerperiode; nicht bei vorwiegend geschäftlich genutzten Liegenschaften.)** · Bund **10 % (Pauschalabzug Unterhaltskosten: 10 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude bis 10 Jahre alt (zu Beginn der Steuerperiode); Wahlrecht je Periode und Liegenschaft)**
  - Liegenschaftsunterhalt Pauschale – Gebäude über 10 Jahre (%): Kanton **20 % (Gleicher Pauschalsatz unabhängig vom Gebäudealter: 20 % des Brutto-Mietertrags bzw. Mietwerts.)** · Bund **20 % (Pauschalabzug: 20 % des Brutto-Mietertrags bzw. Brutto-Eigenmietwerts, Gebäude über 10 Jahre alt)**
- **Bemerkung:** Pauschale 20 % gilt in ZH unabhängig vom Gebäudealter (keine Staffelung nach Gebäudealter, keine Werte-Schlüssel liegenschaft.pauschale_neu/alt belegt).
- **Quellen:**
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0007.md) `zh-form-350__c0007` – «Die Abzüge für die Unterhalts- und Verwaltungskosten können für jede Liegenschaft entweder auf Grund einer Pauschale»
  - [ZStB 30.2](../../chunks/zh/dauernd/zh-zstb-30-2/zh-zstb-30-2__c0002.md) `zh-zstb-30-2__c0002` – «Dieser Pauschalabzug beträgt 20 % vom Brutto-Mietertrag bzw. -Mietwert.»
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0184.md) `zh-wl-2025__c0184` – «pflichtigen können für jede Liegenschaft zwischen dem Abzug der tatsächlichen Kosten und»
  - [StG ZH § 30](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-30-t2.md) `zh-stg-2025__par-30-t2` – «Der Steuerpflichtige kann für Liegenschaften des Privatvermögens anstelle der tatsächlichen Kosten und Prämien einen Pauschalabzug geltend machen.»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode bis zehn Jahre alt ist: 10 Prozent des Brutto-Mietertrags»
  - [LKV Art. 5](../../chunks/bund/2025/bund-lkv/bund-lkv__art-5.md) `bund-lkv__art-5` – «wenn das Gebäude zu Beginn der Steuerperiode mehr als zehn Jahre alt ist: 20 Prozent des Brutto-Mietertrags»
  - [WL ZH 2025 S. 29](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0185.md) `zh-wl-2025__c0185` – «Liegenschaften abzüglich Entschädigungen für Heizung, Warmwasser und Treppenhaus»
  - [WL ZH 2025 S. 29](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0185.md) `zh-wl-2025__c0185` – «Wird der Pauschalabzug beansprucht, können (mit Ausnahme der Baurechtszinsen, siehe»
  - [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0038.md) `zh-zstb-30-3__c0038` – «ist der Pauschalabzug vom Eigenmietwert nach Abzug des Einschlages zu berechnen»
  - [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0029.md) `zh-zstb-30-3__c0029` – «hat der Abzug entweder im Zeitpunkt der Fälligkeit oder im Zeitpunkt der Zahlung der Schuld zu erfolgen»
  - [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0029.md) `zh-zstb-30-3__c0029` – «An der einmal getroffenen Wahl ist festzuhalten.»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0003.md) `zh-form-350__c0003` – «Gewerblich / geschäft-   Total   Verwaltungskosten   Verbleibender Ertrag»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0004.md) `zh-form-350__c0004` – «Nettoertrag aus Liegenschaften»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0004.md) `zh-form-350__c0004` – «erklärung Seite 2, Ziffer 6»
  - [Formular 300 ZH 2025 S. 2](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0006.md) `zh-form-300-2025__c0006` – «Nettoertrag aus Liegenschaften»

<a id="form-350-ziff-16-unterhalt-abzug-liegenschaft-energie-umwelt"></a>
### Ziff. Form. 350 / Ziff. 16 Unterhalt – Investitionen Energiesparen / Umweltschutz, Rückbaukosten Ersatzneubau, Denkmalpflege, Baurechtszinsen

- **Schlüssel:** `abzug.liegenschaft.energie_umwelt` (Investitionen Energiesparen/Umweltschutz, Rückbaukosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Handwerker- und Unterhaltsrechnungen Liegenschaft (Reparaturen, Renovationen, Energiespar-/Umweltschutzmassnahmen) → Rechnungen, Subventionsbescheide (Abzug nur nicht subventionierter Teil)
- **Rein:** Rechnungen Energiespar-/Umweltschutzmassnahmen (bestehende Gebäude) + Subventionsentscheid → effektive Kosten (5741 ff.) · Separate Rückbauabrechnung (Demontage, Abbruch, Abtransport, Entsorgung) → effektive Kosten · Rechnungen denkmalpflegerischer Arbeiten (gesetzlich/behördlich angeordnet) → effektive Kosten · Baurechtsvertrag/Zinsbelege → Aufstellung Baurechtszinsen
- **Rechnen:** (Energie/Umwelt + Denkmalpflege) – Subventionen + Rückbau → eff. (5741 ff.) + Baurechtszinsen; Rest Energie/Rückbau bei negativem Reineinkommen → zwei Folgeperioden
- **Regel:** Den Unterhaltskosten gleichgestellt: Investitionen für Energiesparen/Umweltschutz und Rückbaukosten im Hinblick auf den Ersatzneubau, soweit nicht subventioniert und bei der direkten Bundessteuer abzugsfähig; nicht berücksichtigter Teil in den zwei folgenden Steuerperioden abziehbar. Denkmalpflegerische Arbeiten und Baurechtszinsen abziehbar. Bei Pauschale nicht zusätzlich (ausser Baurechtszinsen).
- **Beachten:** Nur bei effektiven Kosten (Pauschale schliesst aus); Energiesparmassnahmen bei Neubauten nicht abziehbar
- **Beachten:** Ersatzneubau: gleiche Person, gleiches Grundstück, gleichartige Nutzung; Übertrag nur für Kosten ab 2020
- **Beachten:** Bund: Baurechtszins nicht abziehbar, wenn der tiefere, nur auf dem Zeitbauwert berechnete EMW beansprucht wird
- **Bund:** Bund: Art. 32 Abs. 2 DBG (Energiespar-/Umweltschutzinvestitionen, Rückbaukosten) – Abzug auch bei Staatssteuer nur soweit bei Bund abzugsfähig.
- **Quellen:**
  - [StG ZH § 30](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-30-t1.md) `zh-stg-2025__par-30-t1` – «Den Unterhaltskosten sind Investitionen, die dem Energiesparen und dem Umweltschutz dienen, und die Rückbaukosten im Hinblick auf den Ersatzneubau gleichgestellt»
  - [StG ZH § 30](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-30-t1.md) `zh-stg-2025__par-30-t1` – «sind in den zwei nachfolgenden Steuerperioden abziehbar»
  - [StG ZH § 30](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-30-t2.md) `zh-stg-2025__par-30-t2` – «Die den Erträgen aus Liegenschaften gegenüberstehenden Baurechtszinsen können abgezogen werden.»
  - [WL ZH 2025 S. 29](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0188.md) `zh-wl-2025__c0188` – «soweit diese Massnahmen nicht subventioniert sind»
  - [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0023.md) `zh-zstb-30-3__c0023` – «Energiesparende Massnahmen, die anlässlich der Erstellung von Neubauten vorgenommen werden, sind steuerlich nicht abzugsfähig.»
  - [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0024.md) `zh-zstb-30-3__c0024` – «kann kein weiterer Abzug für Aufwendungen für Massnahmen zur rationellen Energieverwendung»
  - [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0026.md) `zh-zstb-30-3__c0026` – «Demontage-, Abbruch-, Abtransport- und Entsorgungskosten»
  - [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0026.md) `zh-zstb-30-3__c0026` – «durch dieselbe steuerpflichtige Person vorgenommen werden wie der Rückbau;»
  - [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0026.md) `zh-zstb-30-3__c0026` – «auf dem gleichen Grundstück errichtet werden wie das vorbestehende Gebäude»
  - [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0026.md) `zh-zstb-30-3__c0026` – «eine gleichartige Nutzung aufweisen, wie das vorbestehende Gebäude;»
  - [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0029.md) `zh-zstb-30-3__c0029` – «Die Übertragung ist möglich für ab der Steuerperiode 2020 angefallene Kosten.»
  - [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0030.md) `zh-zstb-30-3__c0030` – «Ein Übertrag erfolgt, sofern das Reineinkommen negativ ist.»
  - [Formular 350 ZH S. 2](../../chunks/zh/2025/zh-form-350/zh-form-350__c0003.md) `zh-form-350__c0003` – «Gewerblich / geschäft-   Total   Verwaltungskosten   Verbleibender Ertrag»
  - [WL ZH 2025 S. 29](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0194.md) `zh-wl-2025__c0194` – «Der Baurechtszins ist bei der direkten Bundessteuer nicht abzugsberechtigt, wenn für die»

<a id="form-350-wl-eigenmietwert-sozialabzug-eigenmietwert"></a>
### Ziff. Form. 350 / WL Eigenmietwert – Einschlag auf dem Eigenmietwert bei tatsächlicher Unternutzung (Unternutzungsabzug)

- **Schlüssel:** `sozialabzug.eigenmietwert` (Einschlag/Abzug auf dem Eigenmietwert (kantonal)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Schätzungsprotokoll / Steuerwert- und Eigenmietwert-Verfügung Liegenschaft (amtliche Schätzung, Liegenschaftssteuerrechnung) → Antrag an Gemeindesteueramt; ZStB 21.2
- **Rein:** Eigenmietwertmitteilung Gemeindesteueramt → errechneter Eigenmietwert · Antrag mit Nachweis der dauernd ungenutzten Räume (z. B. nach Wegzug der Kinder) → Einschlag gem. ZStB 21.2
- **Rechnen:** EMW nach Einschlag = errechneter EMW – angemessener Einschlag; Unterhaltspauschale vom EMW nach Einschlag rechnen
- **Regel:** Nur in Ausnahmefällen bei Verminderung des Wohnbedürfnisses (z. B. Wegzug der Kinder); bei vier bis sechs Zimmern liegt keine Unternutzung vor, wenn zwei oder mehr Personen darin wohnen. Wird von der Behörde beim Eigenmietwert berücksichtigt (keine eigene Zeile im Formular).
- **Beachten:** Kanton: keine Unternutzung bei vier bis sechs Zimmern und zwei oder mehr Bewohnern; nur Ausnahmefälle
- **Beachten:** Bund: nur dauernd unbenutzte Räume (Nachweis Stpfl.); nicht Gäste-/Arbeitszimmer, Besuchszimmer Kinder, Zweitwohnung
- **Quellen:**
  - [WL ZH 2025 S. 28](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0183.md) `zh-wl-2025__c0183` – «Auf den errechneten Eigenmietwerten kann in Ausnahmefällen ein Einschlag gewährt werden,»
  - [Weisung 2009 ZH S. 11–12](../../chunks/zh/2025/zh-weisung-liegenschaften-2009/zh-weisung-liegenschaften-2009__c0025.md) `zh-weisung-liegenschaften-2009__c0025` – «Darüber hinaus kann auf dem Eigenmietwert ein angemessener»
  - [ZStB 30.3](../../chunks/zh/dauernd/zh-zstb-30-3/zh-zstb-30-3__c0038.md) `zh-zstb-30-3__c0038` – «ist der Pauschalabzug vom Eigenmietwert nach Abzug des Einschlages zu berechnen»
  - [WL 2a 2025 S. 4–5](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0029.md) `bund-wl-2a-2025__c0029` – «nen Räume dauernd nicht benutzt werden. Der Nachweis der»
  - [WL 2a 2025 S. 4–5](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0029.md) `bund-wl-2a-2025__c0029` – «Eine weniger intensive Nutzung berechtigt nicht zum Abzug.»
  - [WL 2a 2025 S. 5](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0030.md) `bund-wl-2a-2025__c0030` – «wenn Räume nur gelegentlich genutzt werden (Arbeits-,»
  - [WL 2a 2025 S. 5](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0030.md) `bund-wl-2a-2025__c0030` – «wenn Räume ausgezogener Kinder weiterhin für Besuche»
  - [WL 2a 2025 S. 5](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0030.md) `bund-wl-2a-2025__c0030` – «für Ferienhäuser und andere Zweitwohnungen.»

## Hilfsblatt Krankheitskosten (Form. 370)

<a id="form-370-s-1-teil-a-ziff-1-abzug-krankheitskosten"></a>
### Ziff. Form. 370 S.1 Teil A Ziff. 1 – Selbstbehalt gemäss Abrechnung Krankenkasse und Versicherung (Code 300)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Leistungsabrechnung/Jahresübersicht Krankenkasse (Franchise + Selbstbehalt)
- **Rein:** Leistungsabrechnungen/Jahresübersicht Krankenkasse und Versicherungen 2025 → Selbstbehalt (Code 300) · Kosten- und Prämienzusammenstellung der Krankenkasse → Beilage zu Form. 370
- **Rechnen:** Code 300 = Σ Selbstbehalte gem. Abrechnungen Krankenkasse/Versicherung 2025, alle Personen addiert → Total (A) Code 317
- **Regel:** Franchise und Selbstbehalt gemäss Krankenkassenabrechnung; Prämien selbst sind NICHT Krankheitskosten (siehe Ziff. 15).
- **Beachten:** Krankenkassenprämien sind keine Krankheitskosten (Bund) → Form. 365 (601) / Ziff. 15 (270)
- **Beachten:** Kosten mehrerer Personen addieren; pro Steuererklärung nur eine Aufstellung
- **Beachten:** Weitere, nicht in Ziff. 1 enthaltene Kosten in Codes 301–307 erfassen (keine Doppelerfassung)
- **Quellen:**
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «1. Selbstbehalt gemäss Abrechnung Krankenkasse und Versicherung 300»
  - [KS 11 S. 4](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0004.md) `bund-ks-11__c0004` – «Keine Krankheitskosten stellen weiter die Krankenkassenprämien dar.»
  - [Formular 365 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-365-2025/zh-form-365-2025__c0001.md) `zh-form-365-2025__c0001` – «1. Private Krankenversicherungsprämien»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «15. Versicherungsprämien, Zinsen von Sparkapitalien»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0001.md) `zh-form-370__c0001` – «diese zu addieren und gesamthaft»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0001.md) `zh-form-370__c0001` – «Pro Steuererklärung ist nur eine»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «ab, welche die Deklaration der»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «mit dem ausgefüllten Formular»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «In obiger Ziffer 1 nicht enthaltene, weitere Aufwendungen:»

<a id="form-370-s-1-teil-a-ziff-2-3-abzug-krankheitskosten"></a>
### Ziff. Form. 370 S.1 Teil A Ziff. 2–3 – Arzt und verordnete Medikamente (Code 301), Zahnarztkosten (Code 302)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Arzt-/Zahnarztrechnungen, Apothekenbelege (nur nicht von KK/Versicherung vergütete Beträge)
- **Rein:** Arztrechnungen, Apothekenbelege (ärztlich verordnete Medikamente) → Code 301 · Zahnarztrechnungen → Code 302 · Vergütungsabrechnung Krankenkasse/Versicherung zu diesen Rechnungen → Teil B (Code 308)
- **Rechnen:** 301/302 = Σ selbst bezahlte Rechnungen, soweit nicht schon in Code 300; Vergütungen Dritter in Teil B (308) abziehen
- **Regel:** Nur die vom Steuerpflichtigen selbst getragenen Kosten; bereits unter Ziffer 1 erfasste Beträge nicht nochmals. Nicht abzugsfähig: Präventivmassnahmen, Fahrkosten zum Arzt, nicht verordnete Akupunktur, eigene Pflegeleistungen, Schlankheitskuren, Wellness, Schönheitsbehandlungen, Psychoanalysen.
- **Beachten:** Nicht: Prävention (Fitness), Fahrten zum Arzt, nicht verordnete Akupunktur, eigene Pflege, Wellness, Schönheit
- **Beachten:** Fahrkosten nur ausnahmsweise: Ambulanz, Fahrten zu auswärtigen Kuren/Therapien, ÖV/Privatwagen unzumutbar
- **Beachten:** Belege geordnet beilegen
- **Quellen:**
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «2. Arzt und vom Arzt verordnete Medikamente 301»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «3. Zahnarztkosten 302»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «Nicht abzugsfähig sind A. Aufwendungen Auslagen für: – Präventivmassnahmen»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0007.md) `zh-zstb-32-1__c0007` – «Akupunktur und andere naturheilärztliche Behandlungen, sofern nicht verordnet»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0007.md) `zh-zstb-32-1__c0007` – «Auslagen für Ambulanzen oder Fahrten zu auswärtigen Kuren oder Therapien»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0007.md) `zh-zstb-32-1__c0007` – «öffentlichen Verkehrsmittels oder des Privatwagens als unzumutbar erscheint.»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «In obiger Ziffer 1 nicht enthaltene, weitere Aufwendungen:»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «Die Belege sind geordnet»

<a id="form-370-s-1-teil-a-ziff-4-7-abzug-krankheitskosten"></a>
### Ziff. Form. 370 S.1 Teil A Ziff. 4–7 – Pflegepersonal (Code 303), Spital/Heilstätten (Code 304), verordnete Therapien/Kuraufenthalte (Code 305), Übrige (Code 307); Total (A) Code 317

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Rechnungen Spital, Spitex, Therapie, Kuraufenthalt (ärztlich verordnet)
- **Rein:** Rechnungen Spitex/Pflegepersonal (entgeltliche Leistungen Dritter) → Code 303 · Spital-/Heilstättenrechnungen → Code 304 · Rechnungen + ärztliche Verordnung für Therapien/Kuraufenthalte → Code 305 · Rechnungen medizinische Apparate, Korrekturgläser → freie Zeile 7 (Code 307)
- **Rechnen:** Total (A) Code 317 = 300 + 301 + 302 + 303 + 304 + 305 + 307
- **Regel:** Entgeltliche Leistungen Dritter (nicht Pflege durch Angehörige), Spitalaufenthalte, ärztlich verordnete Therapien und Kuren; Belege geordnet beilegen.
- **Beachten:** Eigene Pflegeleistungen nicht abziehbar; nur entgeltliche Leistungen Dritter
- **Beachten:** Heim ohne Behinderung: Pflege, med. Leistungen, Hilfsmittel hier; mit Behinderung → Form. 370 S. 2 (Ziff. 16.4)
- **Beachten:** Anteil Lebenshaltung (z. B. Ernährung) in Teil B Code 311 abziehen
- **Quellen:**
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «4. Pflegepersonal (entgeltliche Leistungen von Drittpersonen) 303»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «5. Kosten für Aufenthalt in Spitälern und Heilstätten usw. 304»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0002.md) `zh-form-370__c0002` – «6. Ärztlich verordnete Therapien, Kuraufenthalte usw. 305»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0006.md) `zh-zstb-32-1__c0006` – «Medizinische Apparate, Korrekturgläser etc.»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0007.md) `zh-zstb-32-1__c0007` – «Eigene Pflegeleistungen»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0008.md) `zh-zstb-32-1__c0008` – «so können im Rahmen des Abzugs der Krankheits- und Unfallkosten die Kosten für Pflege- und medizinische Leistungen, Hilfsmittel, Pflegeartikel etc. geltend gemacht werden»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0017.md) `zh-zstb-32-1__c0017` – «In der Steuererklärung sind die behinderungsbedingten Kosten in Ziffer 16.4»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «2. Anteil Lebenshaltungskosten (z. B. Ernährung)»

<a id="form-370-s-1-teil-b-abzug-krankheitskosten"></a>
### Ziff. Form. 370 S.1 Teil B – Vergütungen Dritter und Anteil Lebenshaltungskosten: Krankenkasse/Versicherungen (Code 308), Lebenshaltungskosten (Code 311), Übrige (Code 312); Total (B) Code 318

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Krankenkassen-Leistungsabrechnung / Kosten- und Selbstbehaltszusammenstellung → Vergütungsabrechnungen Krankenkasse/Zusatzversicherung/Unfallversicherung
- **Rein:** Leistungsabrechnungen Krankenkasse/Zusatz-/Unfallversicherung → Code 308 · Spital-/Heimrechnung (Pensions-/Verpflegungsanteil) → Anteil Lebenshaltung Code 311 · Leistungen Haftpflichtversicherung → 308; Hilfswerke, Stiftungen → freie Zeile 3 (Code 312)
- **Rechnen:** Total (B) Code 318 = 308 + 311 + 312, nur soweit nicht bereits unter A abgezogen
- **Regel:** Abzuziehen sind Leistungen der Kranken-/Unfallversicherung und Dritter sowie der Anteil Lebenshaltungskosten bei Heim-/Spitalaufenthalt (z. B. Ernährung), soweit nicht bereits unter A abgezogen.
- **Beachten:** Lebenshaltungsanteil = Kosten, die auch ohne Krankheit oder Unfall angefallen wären
- **Beachten:** Bund: EL für Krankheitskosten (Art. 3d ELG) anrechnen, jährliche EL (Art. 3a ELG) nicht
- **Quellen:**
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «1. Krankenkasse / Versicherungen 308»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «2. Anteil Lebenshaltungskosten (z. B. Ernährung) 311»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0006.md) `zh-zstb-32-1__c0006` – «allfällige Anteile für Lebenshaltungskosten (Kosten, die auch ohne Krankheit oder Unfall angefallen wären) abzuziehen»
  - [KS 11 S. 10–11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0026.md) `bund-ks-11__c0026` – «SUVA, Militärversicherung, Krankenkasse, Haftpflicht- und private Unfallversicherung»
  - [KS 11 S. 10–11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0026.md) `bund-ks-11__c0026` – «werke und Stiftungen etc.) zur Zahlung verbleiben.»
  - [KS 11 S. 10–11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0026.md) `bund-ks-11__c0026` – «hingegen diejenigen Ergänzungsleistungen, welche zur Vergütung von Krankheits- und»
  - [KS 11 S. 10–11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0026.md) `bund-ks-11__c0026` – «Jährliche Ergänzungsleistungen aufgrund»

<a id="form-370-s-1-teil-c-d-abzug-krankheitskosten"></a>
### Ziff. Form. 370 S.1 Teil C/D – Auslagen netto (C, Code 314) bzw. Pauschale Diät CHF 2500 (D, Code 315)

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → Ärztliche Bestätigung dauernde lebensnotwendige Diät (z. B. Zöliakie)
- **Rein:** Übertrag Total (A) 317 und (B) 318 aus Form. 370 → Auslagen netto C (314) · Ärztliche Bestätigung andauernde, lebensnotwendige Diät (z. B. Zöliakie) → Pauschale D (315) · Belege Mehrkosten ärztlich angeordnete Diät/Spezialnahrung → effektiv in Teil A
- **Rechnen:** C (314) = A (317) – B (318); D (315) = 2’500 anstelle effektiver Diät-Mehrkosten (Kanton = Bund); → Total C und/oder D (313)
- **Regel:** Auslagen netto = Total Aufwendungen (A) – Vergütungen Dritter (B). Bei ärztlich angeordneter Diät/Spezialnahrung Mehrkosten abziehbar; anstelle der tatsächlichen Kosten bei andauernder lebensnotwendiger Diät Pauschale CHF 2500.
- **Beachten:** Pauschale nur bei andauernder, lebensnotwendiger Diät; nicht zusätzlich zu effektiven Diät-Mehrkosten
- **Beachten:** Bund: bei Diabetes nur effektive Mehrkosten, keine Pauschale
- **Quellen:**
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «Total der Auslagen (C) 314»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0003.md) `zh-form-370__c0003` – «CHF 2500 geltend gemacht wer-»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0006.md) `zh-zstb-32-1__c0006` – «Anstelle des Abzugs der tatsächlichen Mehrkosten kann bei andauernden, lebensnotwendigen Diäten eine Pauschale von Fr. 2'500.- geltend gemacht werden»
  - [KS 11 S. 5–6](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0009.md) `bund-ks-11__c0009` – «ten eine Pauschale von CHF 2'500.-- geltend gemacht werden. An Diabetes erkrankte Per-»
  - [KS 11 S. 5–6](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0009.md) `bund-ks-11__c0009` – «sonen können jedoch nur die effektiven Mehrkosten zum Abzug bringen.»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «Total der Auslagen»

<a id="form-370-s-1-teil-e-abzug-krankheitskosten"></a>
### Ziff. Form. 370 S.1 Teil E – Berechnung: Total Auslagen (313) abzüglich Selbstbehalt 5 % des Nettoeinkommens (319) = Abzug (320) → Ziff. 22.1

- **Schlüssel:** `abzug.krankheitskosten` (Krankheits- und Unfallkosten (über Selbstbehalt)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Formular 370 (Staats- und Bundessteuer getrennt)
- **Rein:** Form. 370 Total der Auslagen (313) → Spalten Staats- und Bundessteuer · Steuererklärung Ziff. 21 Nettoeinkommen (Code 310) je Spalte → Basis Selbstbehalt
- **Rechnen:** 319 = 5 % × Nettoeinkommen Ziff. 21 (310), je Spalte Staat / Bund; Abzug 320 = 313 – 319 (nur positiver Rest) → Ziff. 22.1
- **Regel:** Selbstbehalt 5 % von Ziffer 21 der Steuererklärung (Nettoeinkommen) getrennt für Staats- und Bundessteuer abziehen; Resultat nach Seite 3, Ziff. 22.1.
- **Beachten:** Nettoeinkommen = Einkünfte – Aufwendungen §§ 26–31 StG bzw. Art. 26–33 DBG (Staat ≠ Bund)
- **Beachten:** Behinderungsbedingte Kosten ohne Selbstbehalt → Ziff. 16.4, nicht hier
- **Limiten:**
  - Krankheitskosten – Selbstbehalt in % des Nettoeinkommens: Kanton **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen nach §§ 26–31 verminderten steuerbaren Einkünfte (Nettoeinkommen, Ziff. 21) übersteigen. Behinderungsbedingte Kosten ohne Selbstbehalt (§ 31 lit. i).)** · Bund **5 % (Krankheits- und Unfallkosten abziehbar, soweit sie 5 % der um die Aufwendungen (Art. 26–33) verminderten steuerbaren Einkünfte übersteigen; behinderungsbedingte Kosten (BehiG) ohne Selbstbehalt)**
- **Quellen:**
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «abzüglich Selbstbehalt (5% von Ziffer 21 der»
  - [Formular 370 ZH S. 1](../../chunks/zh/2025/zh-form-370/zh-form-370__c0004.md) `zh-form-370__c0004` – «Abzug 320»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «21.   Nettoeinkommen   310»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0009.md) `zh-form-300-2025__c0009` – «22.1 Krankheits- und Unfallkosten»
  - [StG ZH § 32](../../chunks/zh/2025/zh-stg-2025/zh-stg-2025__par-32.md) `zh-stg-2025__par-32` – «5 Prozent der um die Aufwendungen gemäss §§ 26–31 verminderten steuerbaren Einkünfte übersteigen»
  - [KS 11 S. 11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0030.md) `bund-ks-11__c0030` – «halt von 5 % der um die Aufwendungen (Art. 26 – 33 DBG) verminderten steuerbaren Ein-»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0004.md) `zh-zstb-32-1__c0004` – «Für den Abzug der behinderungsbedingten Kosten besteht kein solcher Selbstbehalt.»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0017.md) `zh-zstb-32-1__c0017` – «In der Steuererklärung sind die behinderungsbedingten Kosten in Ziffer 16.4»

<a id="form-370-s-2-teil-a-b-abzug-behinderungskosten"></a>
### Ziff. Form. 370 S.2 Teil A/B – Behinderungsbedingte Kosten: effektive Aufwendungen (Codes 3100–3120) und Vergütungen Dritter (Codes 3130–3150)

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Arzt-, Zahnarzt-, Spital- und Therapierechnungen (Krankheits- und Unfallkosten) → IV-/Hilflosenentschädigungs-Bescheide, Rechnungen Heim-/Entlastungsaufenthalt, Hilfsmittel
- **Rein:** Rechnungen Pflege/Betreuung, Therapien, Hilfsmittel, Transporte, Wohnungsanpassung → Code 3100 · Rechnungen Heim-/Entlastungsaufenthalt (Pension + Pflege) → Code 3101 · Abrechnungen Krankenkasse/Versicherungen → 3130; Verfügung Hilflosenentschädigung → 3131 · IV-/HE-Verfügung, Pflegeeinstufung Heim (BESA/RAI), ärztl. Fragebogen (Bund) → Nachweis Behinderung
- **Rechnen:** A (3120) = 3100 + 3101 + 3102; B (3150) = 3130 + 3131 + 3132 + 3133; Heim 3132: Kanton 2’000 × Monate / Bund Existenzminimum Art. 93 SchKG od. kant. Richtlinie
- **Regel:** Effektive Kosten bei Empfängern von IV-Leistungen etc. (3100) und bei Heim-/Entlastungsaufenthalten (3101); abzuziehen: Krankenkasse/Versicherungen (3130), Hilflosenentschädigungen (3131), Anteil Lebenshaltungskosten (3132). Pro Steuererklärung nur eine Aufstellung.
- **Beachten:** Nur bei Behinderung i. S. BehiG (u. a. HE-/IV-Bezüger; Pflege ≥ 60 Min./Tag; ZH-Heim ab BESA-/RAI-Stufe 4)
- **Beachten:** Heim ohne Behinderung → Krankheitskosten (S. 1); Haushalt-/Kinderbetreuung nur soweit über Abzug Ziff. 16.6
- **Beachten:** Heim: Pflegetaxen KVG und Hilflosenentschädigungen abziehen; eine Aufstellung pro Steuererklärung
- **Quellen:**
  - [Formular 370 ZH S. 2](../../chunks/zh/2025/zh-form-370/zh-form-370__c0005.md) `zh-form-370__c0005` – «1. behinderungsbedingte Kosten bei Empfängern von IV-Leistungen etc. 3100»
  - [Formular 370 ZH S. 2](../../chunks/zh/2025/zh-form-370/zh-form-370__c0005.md) `zh-form-370__c0005` – «2. Hilflosenentschädigungen 3131»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0009.md) `zh-zstb-32-1__c0009` – «Personen mit Behinderungen im Sinne des Behindertengleichstellungsgesetzes vom 13. Dezember 2002»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0011.md) `zh-zstb-32-1__c0011` – «Bezüger von Leistungen auf Grund des Bundesgesetzes über die Invalidenversicherung (IVG)»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0011.md) `zh-zstb-32-1__c0011` – «Heimbewohner und Spitex-Patienten, bei denen ein täglicher Pflege- und Betreuungsaufwand von 60 Minuten und mehr anfällt.»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0011.md) `zh-zstb-32-1__c0011` – «im BESA-System (BewohnerInnen-Einstufungs- und Abrechnungssystem) ab BESA-Stufe»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0011.md) `zh-zstb-32-1__c0011` – «im RAI/RUG-System (Resident Assessment Instrument) ab Stufe 4»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0013.md) `zh-zstb-32-1__c0013` – «Pflege, Betreuung, Begleitung, Gebärden- und Taubblindendolmetscher, Therapien, Blindenhunde»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0013.md) `zh-zstb-32-1__c0013` – «soweit die Auslagen den Abzug für Drittbetreuungskosten gemäss Ziffer 16.6 der Steuererklärung übersteigen»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0008.md) `zh-zstb-32-1__c0008` – «Liegt bei einem Aufenthalt in einem Alters- und Pflegeheim keine Behinderung im Sinne des Abzugs der behinderungsbedingten Kosten vor»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0015.md) `zh-zstb-32-1__c0015` – «Im Kanton Zürich sind dafür monatlich Fr. 2'000.- abzuziehen»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0015.md) `zh-zstb-32-1__c0015` – «ferner um die Vergütungen für Pflegeleistungen (Pflegetaxen) nach KVG sowie die Hilflosenentschädigungen»
  - [KS 11 S. 8](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0017.md) `bund-ks-11__c0017` – «nach den Richtlinien über die Berechnung des Existenzminimums gemäss Art.»
  - [KS 11 S. 8](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0017.md) `bund-ks-11__c0017` – «93 SchKG oder nach entsprechenden kantonalen Richtlinien»
  - [KS 11 S. 11–12](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0031.md) `bund-ks-11__c0031` – «Dieser Fragebogen kann bei Geltendmachung von»

<a id="form-370-s-2-teil-c-d-abzug-behinderungskosten"></a>
### Ziff. Form. 370 S.2 Teil C/D – Total abzugsberechtigte Kosten (Code 3155) bzw. Pauschale (Code 3103) → Ziff. 16.4

- **Schlüssel:** `abzug.behinderungskosten` (Behinderungsbedingte Kosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** – → Rechenzeile Formular 370 Seite 2
- **Rein:** Übertrag A (3120) und B (3150) aus Form. 370 S. 2 → C (3155) · Verfügung Hilflosenentschädigung (Grad) → Pauschale D (3103) · Nachweis Gehörlosigkeit bzw. Dialysepflicht → Pauschale D (3103)
- **Rechnen:** Entweder 3155 = 3120 – 3150 ODER Pauschale 3103: HE leicht 2’500 / mittel 5’000 / schwer 7’500; Gehörlose, Dialyse 2’500 (Kanton = Bund) → Ziff. 16.4 (3160)
- **Regel:** Entweder Total der abzugsberechtigten Kosten (A – B) oder Pauschale (Art angeben; Pauschalen siehe Merkblatt des kantonalen Steueramtes zu Krankheits-, Unfall- und behinderungsbedingten Kosten, Ziff. 3, ZStB 32.1); Übertrag nach Seite 3, Ziff. 16.4.
- **Beachten:** Kein Selbstbehalt (anders als Krankheitskosten Ziff. 22.1)
- **Beachten:** Pauschale anstelle der effektiven Kosten (nicht kumulieren); Art der Pauschale angeben
- **Beachten:** Bund: Kinder zusätzlich zum Kinderabzug; übrige Unterstützte nur effektive Kosten, soweit über Unterstützungsabzug
- **Quellen:**
  - [Formular 370 ZH S. 2](../../chunks/zh/2025/zh-form-370/zh-form-370__c0006.md) `zh-form-370__c0006` – «Total der abzugsberechtigten Kosten 3155»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0016.md) `zh-zstb-32-1__c0016` – «Anstelle des Abzugs der effektiven, selbst getragenen Kosten können behinderte Personen einen jährlichen Pauschalabzug»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0016.md) `zh-zstb-32-1__c0016` – «Nierenkranke, die sich einer Dialyse unterziehen müssen.»
  - [KS 11 S. 10](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0025.md) `bund-ks-11__c0025` – «Bezüger einer Hilflosenentschädigung schweren Grades:»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.4 Behinderungsbedingte Kosten»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0004.md) `zh-zstb-32-1__c0004` – «Für den Abzug der behinderungsbedingten Kosten besteht kein solcher Selbstbehalt.»
  - [KS 11 S. 11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0028.md) `bund-ks-11__c0028` – «Diese Kosten können zusätzlich zum Kinderabzug»
  - [KS 11 S. 11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0029.md) `bund-ks-11__c0029` – «in dem Umfang abzugsfähig, in dem sie den Unterstützungsabzug gemäss Art. 213 Abs. 1»
  - [KS 11 S. 11](../../chunks/bund/dauernd/bund-ks-11/bund-ks-11__c0029.md) `bund-ks-11__c0029` – «Es können nur die effektiven Kosten zum Abzug gebracht werden.»
  - [ZStB 32.1](../../chunks/zh/dauernd/zh-zstb-32-1/zh-zstb-32-1__c0017.md) `zh-zstb-32-1__c0017` – «die Krankheits- und Unfallkosten in Ziffer 22.1 einzutragen»

## Hilfsblatt Weiterbildung (Form. 367)

<a id="form-367-abzug-weiterbildung"></a>
### Ziff. Form. 367 – Total der Kosten (Code 2900/2903), Beitrag Arbeitgeber/Dritte (2901/2904), Selbstgetragene Kosten (2902/2905), Zulässiger Abzug (2920/2921 → Code 292) (Spalten Person 1 / Person 2)

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren), Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Kursrechnungen, Zahlungsnachweise; Lohnausweis Ziff. 13.3 (Arbeitgeberbeitrag an den Arbeitnehmer)
- **Rein:** Kursrechnungen/Zahlungsbelege 2025 → Total der Kosten (2900/2903) · Lohnausweis Ziff. 13.3 → Beitrag Arbeitgeber (2901/2904) · Bestätigungen Beiträge Bund/Branchenverbände → Beitrag weiterer Stellen (2901/2904)
- **Rechnen:** Je Person: 2902/2905 = 2900/2903 – 2901/2904; Abzug 2920/2921 (Person 1/Person 2) = min(selbstgetragen; Kanton 12’400 / Bund 13’000); 292 = 2920 + 2921 je Block Staats-/Bundessteuer → Ziff. 16.2
- **Regel:** Je Person: Total Kosten – Beiträge Arbeitgeber/Bund/Branchenverbände = selbstgetragene Kosten; zulässiger Abzug max. CHF 12’400 (Staatssteuer) bzw. CHF 13’000 (Bundessteuer) → Ziff. 16.2. Im Lohnausweis Ziff. 13.3 ausgewiesene Arbeitgeberbeiträge sind als Beitrag Dritter anzugeben.
- **Beachten:** Nur mit Abschluss Sek. II oder ab vollendetem 20. Lebensjahr; nicht Ausbildung bis zum ersten Sek.-II-Abschluss
- **Beachten:** Massgebend ist Fälligkeit bzw. Zahlung, nicht der Kursbesuch
- **Beachten:** Formular 367 vollständig ausgefüllt beilegen
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 12'400 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung, selbst getragene Kosten: max. CHF 12'400 (Staatssteuer), sofern Abschluss Sek. II vorliegt oder 20. Lebensjahr vollendet (und nicht Ausbildung bis zum ersten Sek.-II-Abschluss).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Bund:** Bund: max. CHF 13’000 je Person (Block «Bundessteuer», Codes 2920/2921 = Person 1/Person 2).
- **Quellen:**
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Beitrag Arbeitgeber oder weiterer Stellen (Bund, Branchenverbände etc.)»
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Zulässiger Abzug (max. je CHF 12’400)»
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Zulässiger Abzug (max. je CHF 13’000)»
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Bezeichnung Person 1 Person 2»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0093.md) `zh-wl-2025__c0093` – «Abschluss auf der Sekundarstufe II vorliegt oder das 20. Lebensjahr vollendet ist»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0093.md) `zh-wl-2025__c0093` – «nicht um die Ausbildungskosten bis zum ersten Abschluss auf der Sekundarstufe II handelt.»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0093.md) `zh-wl-2025__c0093` – «ist die Fälligkeit bzw. die Zahlung und nicht der Kursbesuch»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0093.md) `zh-wl-2025__c0093` – «Der Steuererklärung ist ein vollständig ausgefülltes Formular»

## Lohnausweis-Regeln

<a id="lohnausweis-feld-f-abzug-berufskosten-fahrkosten"></a>
### Ziff. Lohnausweis Feld F – Unentgeltliche Beförderung zwischen Wohn- und Arbeitsort → kein Fahrkostenabzug (Form. 360 Ziff. 1)

- **Schlüssel:** `abzug.berufskosten.fahrkosten` (Fahrkosten Wohn-/Arbeitsstätte) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld F (Kreuz) / Ziff. 2.2 Privatanteil Geschäftsfahrzeug
- **Rein:** Lohnausweis Feld F (Kreuz) → kein Fahrkostenabzug in Form. 360 Ziff. 1 · Lohnausweis Ziff. 2.2 (Privatanteil Geschäftswagen) → im Bruttolohn; Fahrkostenabzug entfällt
- **Rechnen:** Feld F ⇒ Form. 360 Ziff. 1 (Codes 201–205) leer; Geschäftsfahrzeug mit pauschaler Fahrkostenberechnung (Bund 0,9 % Kaufpreis/Monat; Kanton ZStB 17.1) ⇒ kein Abzug
- **Regel:** Ist Feld F angekreuzt (Geschäftsfahrzeug, Sammeltransport, Autokilometervergütung an Aussendienst, Autopauschale, geschäftlich notwendiges GA), entstehen dem Arbeitnehmer keine Arbeitswegkosten: kein Fahrkostenabzug in Form. 360 Ziff. 1. Wer ein Geschäftsfahrzeug hat, kann keine Fahrkosten abziehen. Ein GA ohne geschäftliche Notwendigkeit ist zum Marktwert in Lohnausweis Ziff. 2.3 zu deklarieren; Feld F ist dann nicht anzukreuzen.
- **Beachten:** Feld F u. a. bei Geschäftsfahrzeug, Sammeltransport, Vergütung effektiver Autokilometer an Aussendienst
- **Beachten:** Wer über ein Geschäftsfahrzeug verfügt, kann keine Fahrkosten abziehen (Kanton und Bund)
- **Bemerkung:** Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen.
- **Quellen:**
  - [WL Lohnausweis 2026 S. 8](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0010.md) `bund-wl-lohnausweis-2026__c0010` – «das zur Verfügung stellen eines Geschäftsfahrzeugs durch den Arbeitgeber»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0005.md) `zh-form-360-2025__c0005` – «Arbeitnehmende, die über ein Geschäftsfahrzeug verfügen, können keine Fahrkosten in Abzug bringen.»
  - [LS 631.33 (bis 2025) S. 2](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0003.md) `zh-pauschalierung-berufsauslagen-2025__c0003` – «zwischen Wohn- und Arbeitsstätte geltend gemacht werden.»
  - [WL ZH 2025 S. 10](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0033.md) `zh-wl-2025__c0033` – «2.2 Privatanteil Geschäftswagen»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0065.md) `zh-wl-2025__c0065` – «Arbeitnehmende, die über ein Geschäftsfahrzeug verfügen, können keine Fahrkosten in Ab-»
  - [BKV Art. 5a](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-5a.md) `bund-bkv-2025__art-5a` – «gelten 0,9 Prozent des Kaufpreises des Fahrzeugs als monatliches Einkommen aus dieser Nutzung»
  - [BKV Art. 5a](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-5a.md) `bund-bkv-2025__art-5a` – «anstelle der Abrechnung über die tatsächlichen Kosten der privaten Nutzung und des Fahrkostenabzugs nach Artikel 5»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0001.md) `zh-form-360-2025__c0001` – «Abonnementkosten für öffentliche Verkehrsmittel»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0002.md) `zh-form-360-2025__c0002` – «Auto, Motorrad (weisses Kontrollschild) in der Regel begrenzt auf 240 Tage»
  - [LS 631.33 (bis 2025) S. 2](../../chunks/zh/2025/zh-pauschalierung-berufsauslagen-2025/zh-pauschalierung-berufsauslagen-2025__c0003.md) `zh-pauschalierung-berufsauslagen-2025__c0003` – «Zwecke eine pauschale Fahrkostenberechnung (vgl. Zürcher Steuer-»

<a id="lohnausweis-feld-g-abzug-berufskosten-verpflegung"></a>
### Ziff. Lohnausweis Feld G – Kantinenverpflegung / Lunch-Checks → reduzierter Verpflegungsabzug (Form. 360 Ziff. 2.1 verbilligt, Code 206)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Feld G (Kreuz) / Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt»
- **Rein:** Lohnausweis Feld G (Kreuz) → Form. 360 Ziff. 2.1 verbilligt (Code 206) · Lohnausweis ohne Feld G, Verpflegung voll zulasten AN → Form. 360 Ziff. 2.1 (Code 208) · Lohnausweis Ziff. 15 «Mittagessen durch Arbeitgeber bezahlt» → Folge für Abzug prüfen
- **Rechnen:** Feld G ⇒ Code 206 = min(Arbeitstage × 7.50; 1’600) statt Code 208 = min(Arbeitstage × 15; 3’200); Beträge Kanton = Bund (Bund: halber Abzug)
- **Regel:** Feld G angekreuzt (Lunch-Checks, verbilligtes Personalrestaurant, auch wenn Nutzung unbekannt) → nur der reduzierte Verpflegungsabzug CHF 7.50/Tag (max. CHF 1’600/Jahr), nicht CHF 15/3’200. Bei > 60 % auswärtiger Tätigkeit mit Mittagessensentschädigung ist im Lohnausweis ausschliesslich unter Ziff. 15 der Hinweis «Mittagessen durch Arbeitgeber bezahlt» anzubringen (WL Lohnausweis 2026); die Folge für den Verpflegungsabzug ist in den vorliegenden Quellen nicht ausdrücklich belegt – nicht belegt, Fachperson prüfen.
- **Beachten:** Feld G auch bei Lunch-Checks, verbilligtem Personalrestaurant (Nutzung egal), 40–60 % Aussendienst mit Essensgeld
- **Beachten:** Kanton: Barbeitrag gilt als Verbilligung; Bund: halber Abzug nur bei Gutscheinen oder Kantine/Personalrestaurant
- **Beachten:** Bund: kein Abzug mangels Mehrkosten, wenn Hauptmahlzeiten max. 10 Fr. kosten
- **Limiten:**
  - Verpflegung bei Verbilligung (Kantine/Lunch-Checks) pro Tag (CHF): Kanton **CHF 7.50 (Verpflegung durch Arbeitgeber verbilligt (Kantine, Personalrestaurant, Barbeitrag, Essensgutscheine) und trotzdem Mehrkosten: CHF 7.50 pro Arbeitstag.)** · Bund **CHF 7.50 (Halber Abzug CHF 7.50 pro Hauptmahlzeit, wenn der Arbeitgeber die Verpflegung verbilligt (Gutscheine) oder Kantine/Personalrestaurant/Gaststätte des Arbeitgebers)**
  - Verpflegung bei Verbilligung pro Jahr (CHF): Kanton **CHF 1'600 (Bei ständiger auswärtiger Verpflegung mit Verbilligung: CHF 1'600 pro Jahr.)** · Bund **CHF 1'600 (Halber Abzug bei Verbilligung: CHF 1'600 pro Jahr)**
  - Verpflegungsmehrkosten pro Arbeitstag (CHF): Kanton **CHF 15 (Mehrkosten auswärtige Verpflegung, wenn voll zulasten der steuerpflichtigen Person: CHF 15 pro Arbeitstag (nicht kumulierbar mit Fahrkosten über Mittag).)** · Bund **CHF 15 (Mehrkosten auswärtige Verpflegung: CHF 15 pro Hauptmahlzeit (i.d.R. Mittagessen); ausschliesslich Pauschale, wenn Hauptmahlzeit wegen Entfernung/kurzer Pause nicht zu Hause eingenommen werden kann)**
  - Verpflegungsmehrkosten pro Jahr (CHF): Kanton **CHF 3'200 (Bei ständiger auswärtiger Verpflegung (voll zulasten): CHF 3'200 pro Jahr.)** · Bund **CHF 3'200 (Bei ständiger auswärtiger Verpflegung CHF 3'200 pro Jahr (voller Abzug))**
- **Bemerkung:** Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen.
- **Quellen:**
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Dieses Feld ist anzukreuzen, wenn dem Arbeitnehmer Lunch-Checks (vgl. Rz 18) abgege»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – ««Mittagessen durch Arbeitgeber bezahlt»»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0066.md) `zh-wl-2025__c0066` – «– wenn die Verpflegung durch den Arbeitgeber verbilligt wird (Kantine, Personalrestaurant,»
  - [WL Lohnausweis 2026 S. 8–9](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0012.md) `bund-wl-lohnausweis-2026__c0012` – «Bei Arbeitnehmern, die mehr als 60 % der Arbeitszeit ausserhalb ihrer üblichen»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md) `zh-form-360-2025__c0003` – «Mehrkosten entstehen: pro Arbeitstag CHF 7.50 / im Jahr CHF 1’600»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md) `zh-form-360-2025__c0003` – «wenn die Verpflegung voll zu Lasten des Arbeitnehmers geht: pro Arbeitstag CHF 15 / im Jahr CHF 3’200»
  - [BKV Art. 6](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-6-t1.md) `bund-bkv-2025__art-6-t1` – «Nur der halbe Abzug ist zulässig, wenn die Verpflegung vom Arbeitgeber anders als in bar verbilligt wird»
  - [WL 2a 2025 S. 6–7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0046.md) `bund-wl-2a-2025__c0046` – «Kein Abzug ist mangels Mehrkosten zu gewähren, wenn»
  - [WL 2a 2025 S. 6–7](../../chunks/bund/2025/bund-wl-2a-2025/bund-wl-2a-2025__c0046.md) `bund-wl-2a-2025__c0046` – «die Hauptmahlzeiten die steuerpflichtige Person maximal»

<a id="lohnausweis-ziff-10-2-abzug-vorsorge-saeule2-einkauf"></a>
### Ziff. Lohnausweis Ziff. 10.2 – Beiträge für den Einkauf in die berufliche Vorsorge – bereits vom Lohn abgezogen → nicht nochmals unter Ziff. 16.1 abziehen

- **Schlüssel:** `abzug.vorsorge.saeule2_einkauf` (Beiträge/Einkäufe 2. Säule (soweit nicht im Lohnausweis abgezogen)) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Bescheinigung Einkauf Pensionskasse (2. Säule, Formular 21 EDP) → Lohnausweis Ziff. 10.2 (Einkauf, im Nettolohn Ziff. 11 bereits berücksichtigt); separat bezahlte Einkäufe: Formular 21 EDP der Vorsorgeeinrichtung
- **Rein:** Lohnausweis Ziff. 10.2 (vom Lohn abgezogener Einkauf) → bereits im Nettolohn Ziff. 11; kein Abzug Ziff. 16.1 · Formular 21 EDP der Vorsorgeeinrichtung (selbst bezahlter Einkauf) → Ziff. 16.1 (Code 280) · Einkaufsbescheinigung der Vorsorgeeinrichtung → Beilage zur Steuererklärung
- **Rechnen:** LA Ziff. 11 = Ziff. 8 – (Ziff. 9 + 10); Ziff. 16.1 (Code 280) = nur nicht vom Lohn abgezogene Einkäufe gem. Formular 21 EDP
- **Regel:** Ziff. 10.2 ist vom Bruttolohn schon abgezogen (Nettolohn = Brutto – Ziff. 9 und 10); NICHT zusätzlich in Ziff. 16.1 abziehen. Nur vom Arbeitnehmer selbst bezahlte (nicht vom Lohn abgezogene) Einkäufe werden von der Vorsorgeeinrichtung mit Formular 21 EDP bescheinigt und in Ziff. 16.1 deklariert. Sperrfrist 3 Jahre bei Kapitalbezug beachten.
- **Beachten:** Einkauf nicht abziehbar, soweit innerhalb von drei Jahren ein Kapitalbezug erfolgt
- **Beachten:** Ziff. 10.2 enthält auch vom AG übernommene AN-Beiträge, sofern in LA Ziff. 7 aufgeführt
- **Beachten:** Bescheinigung der Vorsorgeeinrichtung über abziehbare Einkäufe mit der Steuererklärung einreichen
- **Bemerkung:** Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen.
- **Quellen:**
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0036.md) `bund-wl-lohnausweis-2026__c0036` – «In diesem Feld sind die im Bruttolohn enthaltenen, dem Arbeitnehmer vom Lohn abgezoge»
  - [WL Lohnausweis 2026 S. 14–15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0037.md) `bund-wl-lohnausweis-2026__c0037` – «Vom Arbeitnehmer selber entrichtete, d. h. nicht vom Lohn abgezogene Einkaufsbeiträge an»
  - [WL Lohnausweis 2026 S. 15](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0038.md) `bund-wl-lohnausweis-2026__c0038` – «vom Bruttolohn total (Ziffer 8) das Total der Abzüge (Ziffer 9 und 10) abgezogen wird.»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0092.md) `zh-wl-2025__c0092` – «werden, soweit innerhalb von drei Jahren ein Kapitalbezug erfolgt.»
  - [Formular 300 ZH 2025 S. 3](../../chunks/zh/2025/zh-form-300-2025/zh-form-300-2025__c0008.md) `zh-form-300-2025__c0008` – «16.1 Beiträge an die AHV, IV und 2. Säule, sofern nicht unter Ziff. 1 und 2 abgezogen»

<a id="lohnausweis-ziff-13-3-abzug-weiterbildung"></a>
### Ziff. Lohnausweis Ziff. 13.3 – Beiträge des Arbeitgebers an berufsorientierte Aus- und Weiterbildung → Form. 367 «Beitrag Arbeitgeber»

- **Schlüssel:** `abzug.weiterbildung` (Berufsorientierte Aus- und Weiterbildungskosten) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare), Rechnungen und Belege Aus- und Weiterbildung (Kurse, Lehrgänge, Umschulung, Prüfungsgebühren) → Lohnausweis Ziff. 13.3 (Vergütungen an den Arbeitnehmer; direkt an Bildungsinstitut bezahlte Beträge werden nicht bescheinigt)
- **Rein:** Lohnausweis Ziff. 13.3 → Form. 367 «Beitrag Arbeitgeber» (2901/2904) · Kursrechnungen (auch auf AN-Namen, vom AG vergütet) → Total der Kosten (2900/2903) · Auskunft AG über direkt an Bildungsinstitut bezahlte Beträge (nicht im Lohnausweis)
- **Rechnen:** Selbstgetragen (2902/2905) = Total (2900/2903) – Beiträge AG/Dritte (2901/2904); Abzug = min(selbstgetragen; Kanton 12’400 / Bund 13’000)
- **Regel:** Ziff. 13.3 als «Beitrag Arbeitgeber oder weiterer Stellen» im Form. 367 von den Gesamtkosten abziehen; nur die selbst getragenen Kosten sind abziehbar. Direkt an Dritte (Bildungsinstitut) bezahlte Arbeitgeberbeiträge stehen nicht im Lohnausweis – beim Arbeitgeber nachfragen und ebenfalls abziehen.
- **Beachten:** Direkt an Dritte (z. B. Bildungsinstitut) bezahlte AG-Beiträge fehlen im LA – nicht als eigene Kosten erfassen
- **Beachten:** Vergütete Rechnungen auf den Namen des AN sind immer in Ziff. 13.3 bescheinigt
- **Limiten:**
  - Aus- und Weiterbildungskosten – Maximum (CHF): Kanton **CHF 12'400 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung, selbst getragene Kosten: max. CHF 12'400 (Staatssteuer), sofern Abschluss Sek. II vorliegt oder 20. Lebensjahr vollendet (und nicht Ausbildung bis zum ersten Sek.-II-Abschluss).)** · Bund **CHF 13'000 (Berufsorientierte Aus- und Weiterbildung inkl. Umschulung bis CHF 13'000 (erster Abschluss Sek II oder 20. Lebensjahr vollendet))**
- **Bemerkung:** Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen.
- **Quellen:**
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «In diesem Feld sind alle effektiven Vergütungen des Arbeitgebers für berufsorientierte Aus-»
  - [WL Lohnausweis 2026 S. 18](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0048.md) `bund-wl-lohnausweis-2026__c0048` – «Nicht anzugeben sind Vergütungen, die direkt an»
  - [Formular 367 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-367-2025/zh-form-367-2025__c0001.md) `zh-form-367-2025__c0001` – «Beitrag Arbeitgeber oder weiterer Stellen (Bund, Branchenverbände etc.)»
  - [WL ZH 2025 S. 16](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0093.md) `zh-wl-2025__c0093` – «(d.h. reduziert um die Beiträge Dritter wie z. B. Arbeitgeber, Bund, Branchenverbände etc.)»

<a id="lohnausweis-ziff-15-abzug-berufskosten-verpflegung"></a>
### Ziff. Lohnausweis Ziff. 15 – Bemerkungen: Anzahl Schichttage u. a. → Grundlage für Schichtarbeitsabzug (Form. 360 Ziff. 2.2, Code 210)

- **Schlüssel:** `abzug.berufskosten.verpflegung` (Mehrkosten auswärtige Verpflegung / Schichtarbeit) · **Status:** ☑️ agent-geprueft
- **Beleg → Feld:** Lohnausweis (Formular 11, auch für Nebenerwerb/VR-Honorare) → Lohnausweis Ziff. 15 «Bemerkungen» (Anzahl im Kalenderjahr geleisteter Schichttage)
- **Rein:** Lohnausweis Ziff. 15 (Anzahl Schichttage) → Form. 360 Ziff. 2.2 (Code 210) · Arbeitgeberbescheinigung Schicht-/Nachttage und Arbeitsort → Nachweis
- **Rechnen:** Code 210 = min(Schichttage × 15; 3’200) (Kanton = Bund); nicht kumulierbar mit Verpflegungsabzug Ziff. 2.1 (Codes 206/208)
- **Regel:** Der Arbeitgeber kann die Anzahl geleisteter Schichttage in Ziff. 15 (Bemerkungen) bescheinigen (freiwillige Angabe); Schichtarbeitsabzug CHF 15 pro ausgewiesenem Schichttag (max. CHF 3’200/Jahr), mind. achtstündige durchgehende Schicht-/Nachtarbeit. Ziff. 15 kann zudem freiwillig die Höhe der im Bruttolohn enthaltenen Kinderzulagen und Krankenkassenbeiträge nennen.
- **Beachten:** Durchgehende, mind. achtstündige Schicht-/Nachtarbeit; gestaffelte Arbeitszeit gleich, wenn Mahlzeiten nicht zu Hause
- **Beachten:** LA Ziff. 15 freiwillig; Bund: AG muss Schichttage und Arbeitsort auf Verlangen bescheinigen
- **Limiten:**
  - Schicht-/Nachtarbeit pro Tag (CHF): Kanton **CHF 15 (Durchgehende, mindestens achtstündige Schicht-/Nachtarbeit: CHF 15 pro ausgewiesenem Schichttag, bei ständiger Schicht-/Nachtarbeit CHF 3'200 pro Jahr. Gestaffelte (unregelmässige) Arbeitszeit gleichgestellt, wenn Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich.)** · Bund **CHF 15 (Durchgehende Schicht-/Nachtarbeit (gestaffelte Arbeitszeit gleichgestellt, wenn beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause möglich): CHF 15 pro ausgewiesenem Tag, bei ganzjähriger Schicht-/Nachtarbeit CHF 3'200 pro Jahr)**
- **Bemerkung:** Quelle ist die ESTV-Wegleitung zum Lohnausweis (Formular 11) in der Fassung 2026 (bund-wl-lohnausweis-2026); im Wiki ist keine 2025er Fassung vorhanden. Es handelt sich um qualitative Deklarationsregeln ohne Beträge; ob sich die Regel für 2025 geändert hat, ist durch die Fachperson zu prüfen.
- **Quellen:**
  - [WL Lohnausweis 2026 S. 18–19](../../chunks/bund/2026/bund-wl-lohnausweis-2026/bund-wl-lohnausweis-2026__c0051.md) `bund-wl-lohnausweis-2026__c0051` – «nen Kinderzulagen, die Anzahl im Kalenderjahr geleisteter Schichttage und die Höhe der im»
  - [WL ZH 2025 S. 13](../../chunks/zh/2025/zh-wl-2025/zh-wl-2025__c0066.md) `zh-wl-2025__c0066` – «gewiesenen Schichttag CHF 15, bei ständiger Schicht- oder Nachtarbeit im Jahr»
  - [Formular 360 ZH 2025 S. 1](../../chunks/zh/2025/zh-form-360-2025/zh-form-360-2025__c0003.md) `zh-form-360-2025__c0003` – «pro ausgewiesenem Schichttag CHF 15 / im Jahr CHF 3’200»
  - [BKV Art. 6](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-6-t2.md) `bund-bkv-2025__art-6-t2` – «Der Schichtarbeit ist die gestaffelte (unregelmässige) Arbeitszeit gleichgestellt, sofern beide Hauptmahlzeiten nicht zur üblichen Zeit zu Hause eingenommen werden können.»
  - [BKV Art. 6](../../chunks/bund/2025/bund-bkv-2025/bund-bkv-2025__art-6-t2.md) `bund-bkv-2025__art-6-t2` – «Der Arbeitgeber muss die Anzahl Tage mit Schicht- oder Nachtarbeit sowie den Arbeitsort auf Verlangen bescheinigen.»
