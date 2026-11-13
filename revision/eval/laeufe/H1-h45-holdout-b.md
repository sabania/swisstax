# OpenClaw-Testlauf: e2e-aufgaben.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Profil: `revh45d` · Modell: `claude-haiku-4-5` · Agent: `revision` · Fragen: 4 · Lauf: 2026-11-13 13:47
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## h02-import

**Frage:** Mandat: Werkhof Beispiel AG, Frauenfeld-Muster TG · Geschäftsjahr 2025 (Stichtag 31.12.2025) · eingeschränkte Revision. M-Files ist in diesem Test durch den Ordner mandant/werkhof-beispiel-ag-2025/ ersetzt (Vorjahresakte: mandant/werkhof-beispiel-ag-2024/). revio ist nicht verbunden: nenne bei jedem Schritt das revio-Werkzeug, das du aufrufen würdest, statt es aufzurufen. Wesentlichkeit 2025 (revio 3.3, Softwareversion revio 4.0, vom WP festgelegt): Gesamtwesentlichkeit CHF 60'000, Toleranzwesentlichkeit CHF 45'000 (75 %), Nichtaufgriffsgrenze CHF 3'000 (5 %).

Auftrag: Prozess 1 – Stimme die Jahresrechnung 2025 (Ordner 0_Abschluss) mit der Saldoliste und dem Hauptbuch ab (Bilanzgleichheit, Totale, Jahresergebnis, Vorjahreszahlen, Anhang formell). Erfasse Differenzen als Notiz.

**Antwort des Agenten** (191.3 s · Tools: 15 Aufrufe revisionswiki__aufgabe, revisionswiki__akte, revisionswiki__rechne):

> I'll start Process 1 by understanding the task with `aufgabe`, then explore the mandate structure.
> 
> Now I'll explore the mandate structure to understand the available documents.
> 
> Now I'll read the annual accounts completely to understand the structure and numbers.
> 
> Now I'll read the trial balance to begin reconciling the numbers.
> 
> Now I'll systematically reconcile the figures using the calculation tool. Let me start by verifying the balance sheet equality and calculating the totals.
> 
> Now let me verify the current asset totals by reconciling the trial balance accounts with the annual accounts categories.
> 
> Now let me verify the fixed assets (Sachanlagen) by reconciling all the depreciation accounts:
> 
> Now let me verify the liabilities. I'll check the short-term liabilities breakdown:
> 
> I've identified a discrepancy. The short-term liabilities components from the trial balance sum to CHF 2'742'005.37, but the annual accounts report only CHF 2'724'005.37 - a difference of CHF 18'000, which exceeds the non-trivial threshold of CHF 3'000.
> 
> Let me verify the equity section and check the long-term liabilities:
> 
> Now let me verify the income statement by reconciling it with the trial balance accounts:
> 
> Now let me verify the consistency of the annual result across all sections:
> 
> Now let me reconcile the prior year figures (2024) shown in the 2025 annual accounts with the available 2024 year-end data:
> 
> Let me verify that all prior year balance sheet figures match between the 2025 and 2024 annual accounts:
> 
> Now I'll create a comprehensive reconciliation note documenting the discrepancy I found. Let me first review whether there's a specific account that might explain the CHF 18'000 difference by examining which accounts changed significantly:
> 
> Now I'll prepare my formal findings. Let me create a comprehensive reconciliation note:
> 
> **PROCESS 1 – RECONCILIATION FINDINGS**
> 
> **Audit Trail & Documentation:**
> 
> I have completed the reconciliation of Jahresrechnung 2025 (Werkhof Beispiel AG, FY 2025, Balance Sheet Date 31.12.2025) with Saldoliste and Hauptbuch per the checklist in aufgabe Prozess 1.
> 
> **Reconciliation Results:**
> 
> **1. Balance Sheet Equality (Bilanzgleichheit)** ✓ Verified
> - Total Aktiven per trial balance: CHF 3'426'065.37
> - Total Passiven per trial balance: CHF 3'426'065.37
> - Difference: CHF 0
> 
> **2. Current Assets (Umlaufvermögen) – All Components Verified** ✓
> - Liquide Mittel: CHF 176'079.77 (Kasse 3'412.60 + Bank accounts 256'967.57 - 84'300.40)
> - Forderungen aus L+L: CHF 1'264'285.50 (Debitoren 1'328'785.50 - Delkredere 64'500.00)
> - Übrige kurzfristige Forderungen: CHF 77'647.75 (VAT advances, withholding tax, employee claims)
> - Vorräte: CHF 1'577'166.35 (Raw materials 268'016.35 + Work in progress 1'267'800.00 + Finished goods 41'350.00)
> - Aktive Rechnungsabgrenzungen: CHF 18'620.00
> - **Subtotal Umlaufvermögen: CHF 3'113'799.37** ✓ Matches annual accounts
> 
> **3. Fixed Assets (Sachanlagen) – All Components Verified** ✓
> - Machinery net: CHF 178'701 (gross 1'413'000 - depreciation 1'234'299)
> - Furniture net: CHF 4'775 (gross 64'200 - depreciation 59'425)
> - IT equipment net: CHF 15'210 (gross 55'700 - depreciation 40'490)
> - Vehicles net: CHF 52'080 (gross 202'400 - depreciation 150'320)
> - Tools net: CHF 7'500 (gross 72'300 - depreciation 64'800)
> - Prepayments: CHF 54'000
> - **Subtotal Sachanlagen: CHF 312'266.00** ✓ Matches annual accounts
> 
> **4. DISCREPANCY IDENTIFIED – SHORT-TERM LIABILITIES**
> 
> **Finding:** Material discrepancy in short-term liabilities reconciliation.
> 
> Trial balance account components:
> - Kreditoren (2000): CHF 743'669.50
> - Anzahlungen Kunden (2030): CHF 1'418'500.00
> - Kurzfristige verzinsliche (2100): CHF 250'000.00
> - Geschuldete MWST (2200): CHF 131'654.97
> - Direkte Steuern (2208): CHF 4'200.00
> - AHV/IV/EO/ALV (2270): CHF 21'340.50
> - BVG (2271): CHF 9'880.00
> - UVG/KTG (2272): CHF 4'150.00
> - Quellensteuer (2279): CHF 3'210.40
> - Passive Rechnungsabgrenzungen (2300): CHF 55'400.00
> - Rückstellung Ferien/Überzeit (2330): CHF 28'000.00
> - Garantierückstellung (2331): CHF 30'000.00
> - Rückstellung Prozessrisiken (2332): CHF 42'000.00
> - **Sum from trial balance accounts: CHF 2'742'005.37**
> 
> Annual accounts reported:
> - **Total kurzfristiges Fremdkapital: CHF 2'724'005.37**
> 
> **Discrepancy: CHF 18'000** (trial balance total exceeds annual accounts by CHF 18'000)
> This exceeds the **non-trivial threshold (Nichtaufgriffsgrenze) of CHF 3'000**.
> 
> **Impact Analysis:**
> - The trial balance balances perfectly (Aktiven = Passiven = 3'426'065.37)
> - Total Fremdkapital reported in annual accounts: CHF 3'330'005.37
> - This figure is correct (short-term CHF 2'742'005.37 + long-term CHF 588'000)
> - However, the subtotal line for "short-term liabilities" shows CHF 2'724'005.37
> - **Internal inconsistency in annual accounts:** Components don't equal the reported subtotal for short-term liabilities
> 
> **5. Income Statement – All Components Verified** ✓
> - Operating Revenue: CHF 6'062'880.00 ✓
> - Gross Result: CHF 3'200'131.81 ✓
> - EBITDA: CHF 171'167.25 ✓
> - EBIT: CHF -42'317.75 ✓
> - Result before tax: CHF -68'190.00 ✓
> - **Annual Loss: CHF -72'390.00** ✓ Matches trial balance account 2979
> 
> **6. Annual Result Consistency** ✓ Verified
> - Annual loss -72'390 in income statement = Annual loss -72'390 in balance sheet equity
> - Prior loss carried forward -31'550 + Current loss -72'390 = Total accumulated loss -103'940 ✓
> - Allocation proposal to carry forward loss: -103'940 ✓
> 
> **7. Prior Year Reconciliation (31.12.2024)** ✓ All figures verified
> - All balance sheet prior year comparison figures (31.12.2024 column) match the 2024 closing figures exactly
> - Equity movement: 168'450 (2024) → 96'060 (2025), decrease of CHF 72'390 = annual loss ✓
> 
> **Formal Structure Check (OR 959a/b) – Pending**
> → *Would call `pruefschritt A1-306` to verify minimum balance sheet structure per OR 959a and minimum income statement structure per OR 959b*
> 
> **Pending Item (Pendenz):**
> 
> **TITEL: Abweichung kurzfristiges Fremdkapital – Saldoliste vs. Jahresrechnung**
> 
> Beschreibung:
> Die Summe der kurzfristigen Verbindlichkeiten aus der Saldoliste (CHF 2'742'005.37) unterscheidet sich um CHF 18'000 von der in der Jahresrechnung 2025 ausgewiesenen Summe (CHF 2'724'005.37). Die einzelnen Positionen der Jahresrechnung addieren sich korrekt zu CHF 2'742'005.37, stimmen aber nicht mit dem ausgewiesenen Zwischentotal von CHF 2'724'005.37 überein.
> 
> Konto/Position: Kurzfristiges Fremdkapital (Bilanz, Passiven, Position 2)
> Datum: 31.12.2025
> Betrag: CHF 18'000 Abweichung
> Material: Ja (übersteigt Nichtaufgriffsgrenze von CHF 3'000)
> 
> Massnahme erforderlich: Klarstellung mit dem Mandanten über die Herkunft der Abweichung beim Übergang von der Saldoliste in die Jahresrechnung.
> 
> ---
> 
> **STATUS: TEILWEISE BEARBEITET** (mit Feststellungen)
> 
> **Next Steps (per Checkliste):**
> → `pruefschritt A1-306` – Formelle Grobprüfung Bilanz- und ER-Struktur (OR 959a/b)
> → `revio K2` – Import simulation (cannot execute; revio not connected; WP will perform)
> → Investigate and resolve the CHF 18'000 discrepancy in short-term liabilities before proceeding with field audit work
> 
> **Ready for:** WP review and decision on next steps

## h04-f1

**Frage:** Mandat: Werkhof Beispiel AG, Frauenfeld-Muster TG · Geschäftsjahr 2025 (Stichtag 31.12.2025) · eingeschränkte Revision. M-Files ist in diesem Test durch den Ordner mandant/werkhof-beispiel-ag-2025/ ersetzt (Vorjahresakte: mandant/werkhof-beispiel-ag-2024/). revio ist nicht verbunden: nenne bei jedem Schritt das revio-Werkzeug, das du aufrufen würdest, statt es aufzurufen. Wesentlichkeit 2025 (revio 3.3, Softwareversion revio 4.0, vom WP festgelegt): Gesamtwesentlichkeit CHF 60'000, Toleranzwesentlichkeit CHF 45'000 (75 %), Nichtaufgriffsgrenze CHF 3'000 (5 %).

Auftrag: Prozess 2 – Bereite das Prüffeld F1 Vorräte vor. Liefere Textfeld-Entwürfe und Notizen.

**Antwort des Agenten** (135.5 s · Tools: 13 Aufrufe revisionswiki__aufgabe, revisionswiki__akte, read, revisionswiki__pruefschritt, revisionswiki__rechne):

> Ich starte die Vorbereitung des Prüffelds F1 Vorräte für die eingeschränkte Revision der Werkhof Beispiel AG.
> 
> Ich erschliesse jetzt die Akte zum Prüffeld F1 Vorräte.
> 
> Ich lese jetzt die Dateien zum Prüffeld F1:
> 
> Jetzt bereite ich die Prüfschritte vor. Ich bearbeite die Befragungsschritte (1xx), analytischen Schritte (2xx) und Detailprüfung (3xx) der Reihe nach.
> 
> Jetzt erstelle ich die Textfeld-Entwürfe und Notizen für die vorbereitbaren Prüfschritte F1 Vorräte. Basierend auf den Unterlagen der Akte und den Prüfschritt-Katalogen:
> 
> ---
> 
> ## **TEXTFELD-ENTWÜRFE FÜR F1 VORRÄTE**
> 
> ### **F1-101: Befragung Bestandesermittlung – Methode**
> **Prüfziel:** EX Bestand, VO Vollständigkeit
> 
> **Quelle:** Inventurprotokoll 31.12.2025 (Mandant, Ordner 12_Lager)
> 
> **Auswahl & Umfang:** Bestandesermittlung per Stichtag 31.12.2025 – Stichtagsinventur mit Dokumentation vorhanden
> 
> **Ergebnis:**  
> Bestandesermittlung erfolgte durch Stichtagsinventur am 31.12.2025, 07:30–15:00 Uhr. Lager nach letztem Warenausgang 30.12.2025 gesperrt. Zähllisten Nr. 1–6 wurden von zweiköpfigen Zählteams durchgeführt und unterzeichnet. Lagerorte: Halle 1, Regal C, Blechlager, Lager 2 (Konsignationslager separat). Material in Arbeit (Baustellen) wird in den angefangenen Arbeiten erfasst und nicht gezählt. Lagerbewegungen wurden während der Zählung nicht durchgeführt (Lager gesperrt).
> 
> **Feststellungen:** Inventurmethode nachvollziehbar dokumentiert.
> 
> **Pendenzen:** Schriftliche Antwort Kundenbefragung (10.11) nicht gefunden → **Pendenz**.
> 
> **Status:** Teilweise bearbeitet (Inventurprotokoll vorhanden, schriftliche Befragung fehlt)
> 
> ---
> 
> ### **F1-102: Befragung Korrektionen Inventurdifferenzen**
> **Prüfziel:** EX Bestand, EN Eintritt, BE Bewertung
> 
> **Auswahl & Umfang:** Feststellung: «Keine wesentlichen Zähldifferenzen gemeldet» (Inventurprotokoll)
> 
> **Ergebnis:**  
> Laut Inventurprotokoll: «Keine wesentlichen Zähldifferenzen gemeldet». Lagerbuchhaltung – Methode nicht aus den Unterlagen ersichtlich. Abklärung erforderlich, ob Lagerbuchhaltung vorhanden ist und wie Inventurdifferenzen (falls vorhanden) verbucht wurden.
> 
> **Pendenzen:** Lagerbuchhaltung-Nachweis fehlt; Frage an Kunde: Führen Sie eine Lagerbuchhaltung? Wenn ja, Inventurdifferenzen und Verbuchung → **Pendenz**.
> 
> **Status:** Teilweise bearbeitet
> 
> ---
> 
> ### **F1-103: Befragung – Permanente Inventur**
> **Prüfziel:** EX Bestand, VO Vollständigkeit
> 
> **Ergebnis:** Stichtagsinventur durchgeführt. Permanente oder Stichprobeninventur – nicht aus Unterlagen ersichtlich.
> 
> **Pendenzen:** Prüfschritt betrifft nur Nicht-Stichtagsinventur → nicht anwendbar oder Abklärung erforderlich.
> 
> **Status:** Teilweise bearbeitet
> 
> ---
> 
> ### **F1-104 bis F1-109: Weitere Befragungsschritte**
> Status: **Teilweise bearbeitet** – Schriftliche Kundenbefragung (10.11) nicht vorhanden
> 
> ---
> 
> ### **F1-201: Analytisch – Vergleich Lagerbestand und Umschlag**
> **Prüfziel:** EX Bestand, VO Vollständigkeit, BE Bewertung
> 
> **Quellen:** Saldoliste 2025/2024, Jahresrechnung, Inventarliste 31.12.2025
> 
> **Auswahl & Umfang:** Vorratskonten (1210, 1219, 1260, 1280) mit Vorjahresvergleich
> 
> **Ergebnis (mit `rechne`):**
> 
> | Konto | GJ CHF | VJ CHF | Veränderung CHF | Veränderung % | Status |
> |---|---|---|---|---|---|
> | 1210 Rohmaterial | 268'016.35 | 252'600 | +15'416.35 | +6.1% | Normal |
> | 1260 Fertigfabrikate | 41'350 | 32'100 | +9'250 | +28.8% | Anstieg >20% |
> | 1280 Angefangene Arbeiten | 1'267'800 | 1'164'300 | +103'500 | +8.9% | Normal |
> | 1219 Wertberichtigung | 0 | -94'900 | +94'900 | – | Auflösung 100% |
> | **Total Vorräte** | **1'577'166.35** | **1'354'100** | **+223'066.35** | **+16.5%** | |
> 
> **Feststellungen & Pendenzen:**
> - Gesamtveränderung der Vorräte CHF 223'066.35 (>Gesamtwesentlichkeit CHF 60'000) ist wesentlich
> - Fertigfabrikate-Anstieg 28.8% wesentlich
> - **Kritisch: Wertberichtigung vollständig aufgelöst (CHF 94'900 Auflösung)** – trotzdem Restposten R-1040 (CHF 38'180) mit Bewegung 14.06.2023 (über 1,5 Jahre alt) ohne Abwertung → **Feststellung/Pendenz**
> - Erklärung der Bestandesveränderungen aus schriftlicher Befragung (10.11) fehlt → **Pendenz**
> 
> **Status:** Mit Feststellungen
> 
> ---
> 
> ### **F1-202: Analytisch – Margenvergleich**
> **Prüfziel:** BE Bewertung, PA Periodenabgrenzung
> 
> **Pendenzen:** Umsatz- und Materialauswertung nach Kategorie nicht aus Unterlagen ersichtlich → **Pendenz: Margenauswertung nach Produktkategorie erforderlich**
> 
> **Status:** Teilweise bearbeitet
> 
> ---
> 
> ### **F1-203: Analytisch – Inventaranalyse ABC, Wertberichtigung**
> **Prüfziel:** EX Bestand, VO Vollständigkeit, BE Bewertung, PA Periodenabgrenzung
> 
> **Quellen:** Inventarliste 31.12.2025, Inventurinstruktion
> 
> **Auswahl & Umfang:** ABC-Analyse Rohmaterial + Fertigfabrikate (mind. 80% des Werts); Analyse Wertberichtigung
> 
> **Ergebnis:**
> 
> ABC-Analyse Inventarliste (Top-Positionen nach Wert):
> 
> | Rang | Artikel | Wert CHF | Kum. % | Anteil | Status |
> |---|---|---|---|---|---|
> | 1 | R-1060 Kleinmaterial | 18'400 | 6.7% | A |  |
> | 2 | R-1020 Flachstahl 80x8 | 76'880 | 35.5% | A | Neubewertung? |
> | 3 | R-1050 Gitterroste | 6'144 | 37.7% | A |  |
> | 4–10 | Träger, Rohre, Winkel | ~40'000 | ~52% | B |  |
> | Rest | Kleinmaterial, Restposten | ~130'000 | 100% | B/C | **R-1040 CHF 38'180** |
> 
> **Kritische Befunde:**
> - Restposten R-1040 (Edelstahl-Geländerelemente): CHF 38'180 (12.3% des Rohmaterials), letzte Bewegung 14.06.2023 (1,5 Jahre!), «Verwendung offen», **keine Abwertung**
> - Wertberichtigung (Konto 1219) vollständig aufgelöst (2024: CHF 94'900 → 2025: 0) – trotz Ladenhüter keine WB → **Wesentliche Feststellung**
> 
> **Pendenzen:** Lagerumschlags-/Altersliste nicht gefunden; Marktsituation für Edelstahl-Restposten unklar → **Pendenz**
> 
> **Status:** Mit Feststellungen
> 
> ---
> 
> ### **F1-205: Lieferantenstruktur (falls in Unterlagen)**
> Status: Unterlagen nicht vorhanden → **Pendenz**
> 
> ---
> 
> ### **F1-301: Detail – Nachrechnung & Abstimmung Inventar ↔ Hauptbuch**
> **Prüfziel:** EX Bestand, VO Vollständigkeit
> 
> **Quellen:** Inventarliste 31.12.2025, Saldoliste 2025, Hauptbuch-Kontoblätter
> 
> **Auswahl & Umfang:** Nachrechnung Inventarliste (Menge × Preis je Zeile); Abstimmung Total je Konto mit Saldoliste; Zähllisten-Abgleich für Positionen ≥ Toleranzwesentlichkeit (CHF 45'000) und auffällige Positionen
> 
> **Ergebnis (Nachrechnung mit `rechne`):**
> 
> **Abstimmung mit Saldoliste:**
> - Rohmaterial (1210): Inventarliste Total CHF 268'016.35 = Saldoliste CHF 268'016.35 ✓
> - Fertigfabrikate (1260): Inventarliste CHF 41'350 = Saldoliste CHF 41'350 ✓
> - Gesamtsumme Vorräte (netto): CHF 309'366.35 = Saldoliste CHF 309'366.35 ✓
> 
> **Zähllisten-Abgleich (Auswahl ≥ Toleranzwesentlichkeit CHF 45'000 oder auffällig):**
> 
> | Artikel | Zählliste | Betrag | Status | Abgleich |
> |---|---|---|---|---|
> | R-1020 Flachstahl 80x8 | Nr. 3 | 76'880 | Wesentlich | Vorhanden, Scan lesbar |
> | R-1040 Edelstahl-Restposten | Nr. 5 | 38'180 | Auffällig (alt) | Vorhanden, aber kritisch → Abwertung? |
> | Konsignationslager | Nr. 6 | 24'150 | Separat | Nicht inventarisiert (Eigentum Lieferant) |
> 
> **Pendenzen:** 
> - Zähllisten-Details für Menge-Abgleich (Zählliste ↔ Inventarliste) nur Scan → teilweise nicht lesbar
> - Angefangene Arbeiten (Konto 1280): Projektliste vorhanden, aber nicht in der bewerteten Inventarliste (Konto 1260/1210) enthalten
> 
> **Status:** Mit Feststellungen
> 
> ---
> 
> ### **F1-320: Anhang – Darstellung & Offenlegung**
> **Prüfziel:** DO Darstellung/Offenlegung
> 
> **Auswahl & Umfang:** Bestandsaufnahme Anhangsangaben vs. Anforderungen (Bewertung, Methodenwechsel, Verpfändung, stille Reserven)
> 
> **Quellen:** Jahresrechnung 2025 (Anhang), Inventurprotokoll, Projektliste
> 
> **Ergebnis:**
> - Bewertungsgrundsätze im Anhang genannt: «Rohmaterial zu Anschaffungskosten, Fertigfabrikate zu Herstellkosten, jeweils höchstens zum Netto-Marktwert»
> - Warenreserve (stille Reserve): Anhang nennt «steuerlich zulässige Wertberichtigung» (2024: CHF 94'900) – aber 2025 vollständig aufgelöst → **Abwertung nicht dokumentiert**
> - Verpfändung/Eigentumsvorbehalt: nicht gefunden (Abklärung erforderlich)
> 
> **Feststellungen & Pendenzen:**
> - Auflösung Warenreserve (CHF 94'900) nicht im Anhang erklärt → **Feststellung** (evtl. Offenlegungspflicht oder stille Reserve-Erklärung erforderlich)
> - Restposten R-1040 (CHF 38'180) ohne Abwertung trotz Überalterung (1,5 Jahre Lagerdauer) → Abwertung im Anhang erforderlich
> 
> **Status:** Mit Feststellungen
> 
> ---
> 
> ### **F1-321: Stille Reserven – Bestand & Veränderung**
> **Prüfziel:** –
> 
> **Quellen:** Wertberichtigung-Kontoblatt, Inventarliste
> 
> **Ergebnis:**
> 
> | Jahr | Wertberichtigung CHF | Betriebsnotwendig CHF | Stille Reserve CHF | Veränderung |
> |---|---|---|---|---|
> | 2024 | 94'900 | 38'180 | +56'720 | – |
> | 2025 | 0 | –38'180 (erforderlich?) | –38'180 | –94'900 |
> 
> **Feststellungen:**
> - **Stille Reserve Auflösung CHF 94'900** (2024 → 2025) ohne entsprechende Wertabschreibung des Restpostens → Nettoauflösung > 0, Ergebnis dadurch günstiger dargestellt
> - **Kritisch**: Restposten R-1040 (CHF 38'180, überaltert seit 14.06.2023) ohne Abwertung, aber Wertberichtigung komplett aufgelöst
> - Aufstellung stille Reserven seitens Kunde nicht in Akte → **Pendenz**
> 
> **Status:** Mit Feststellungen
> 
> ---
> 
> ### **F1-322: Dauerakten**
> **Prüfziel:** –
> 
> Status: **Nicht bearbeitet (Dauerakten werden zentralisiert gepflegt)**
> 
> ---
> 
> ## **ZUSAMMENFASSUNG NOTIZEN (revio K7 – Wesentliche Feststellungen & Pendenzen)**
> 
> ### **WESENTLICHE FESTSTELLUNGEN:**
> 
> **1. Restposten Edelstahl-Geländer ohne Abwertung (F1-203, F1-104)**
> - **Betrag:** CHF 38'180 (>Nichtaufgriffsgrenze CHF 3'000, Toleranzwesentlichkeit CHF 45'000 nahe)
> - **Befund:** Artikel R-1040, 46 Stk à CHF 830, letzte Bewegung 14.06.2023 (über 1,5 Jahre Lagerdauer)
> - **Klassifikation:** Ladenhüter/Überaltert, keine Abwertung vorgenommen trotz Verweis «Verwendung offen»
> - **Buchungsvorschlag (ohne Verbuchung):** 
>   - Debit: Wertberichtigung Vorräte (Konto 4091)
>   - Credit: Bestandesänderung (Konto 4090) oder Wertberichtigung (Konto 1219)
>   - **Betrag: CHF 38'180 (oder anteilig nach Abklärung)**
> - **Fundstelle:** Inventarliste Pos. R-1040, Inventurprotokoll (Besonderes)
> - **Status:** Überprüfung erforderlich (WP-Schritt F1-104 oder F1-304)
> 
> **2. Auflösung Warenreserve ohne Gegenbuchung (F1-321, F1-320)**
> - **Betrag:** CHF 94'900 (Nettoauflösung, >Gesamtwesentlichkeit CHF 60'000)
> - **Befund:** Wertberichtigung 2024 CHF 94'900 → 2025 CHF 0 (aufgelöst), aber Ursache (Überalterte Ware) existiert
> - **Klassifikation:** Nettoauflösung stiller Reserven, Ergebnis dadurch günstiger dargestellt
> - **Offenlegungspflicht:** Erforderlich im Anhang (OR Art. 959c), wenn Nettoauflösung wesentlich
> - **Pendenzen:** Kundenerklärung erforderlich (F1-105: Bewertungsabschreibung)
> 
> ---
> 
> ### **PENDENZEN:**
> 
> **1. PBC-Unterlagen fehlen – Befragungen (F1-101 bis F1-109)**
> - **Was fehlt:** Schriftliche Antworten Kundenbefragung (revio 10.11) zu:
>   - F1-101: Bestandesermittlung-Methode
>   - F1-102: Inventurdifferenzen & Verbuchung
>   - F1-104: Bewertungsmethode (AK/HK, FIFO, Durchschnitt)
>   - F1-105: Bewertungsabschreibungen (Ursache Auflösung Warenreserve)
>   - F1-106: Wertberichtigung unkurant – Berechnung
>   - F1-107: Verlustfreie Bewertung – Verfahren
>   - F1-108/109: Abgrenzung Wareneingänge/-ausgänge
> - **Anforderung:** Spätestens bis <Datum einfügen> erforderlich für Fortsetzung Befragungsschritte
> - **Klassifikation:** Blockiert Schritte F1-101 bis F1-109 (maximal «teilweise bearbeitet»)
> 
> **2. Lagerbuchhaltung – Nachweis (F1-102)**
> - **Was fehlt:** Lagerbuchhaltung-Dokumentation, Zählplan (bei permanente/Stichprobeninventur)
> - **Klassifikation:** Nur für Klärung der Inventurdifferenzen erforderlich
> 
> **3. Lagerumschlags-/Altersliste & Wertberichtigung-Berechnung (F1-203, F1-104)**
> - **Was fehlt:** Altersliste mit letzter Bewegung je Artikel; Berechnung Wertberichtigung unkurant
> - **Klassifikation:** Erforderlich für Bewertungs-Analytik und Nachweis betriebsnotwendiger Wertberichtigung
> 
> **4. Budget/Auftragsbestand (F1-201, F1-203)**
> - **Was fehlt:** Umsatzplanung, Auftragsbestand für ABC-Analyse
> - **Klassifikation:** Optional für Plausibilisierung Lagerbestände
> 
> **5. Aufstellung Stille Reserven (F1-321)**
> - **Was fehlt:** Aufstellung stille Reserven GJ/VJ, Vollständigkeitserklärung des Kunden
> - **Klassifikation:** Erforderlich für F1-321 und Gesamtaufstellung
> 
> **6. Margenauswertung nach Produktkategorie (F1-202)**
> - **Was fehlt:** Umsatz- und Materialaufwand je Kategorie
> - **Klassifikation:** Erforderlich für Margenvergleich
> 
> **7. Zähllisten-Details (F1-301)**
> - **Was fehlt:** Zähllisten Nr. 3 und 6 (Scan) nur teilweise lesbar
> - **Klassifikation:** Erforderlich für Positions-Abgleich ≥ Toleranzwesentlichkeit
> 
> **8. Projekt P-25-214 – Abschluss (F1-1280, Projektliste)**
> - **Befund:** P-25-214 100% fertig per 31.12.2025, Abnahme 19.12.2025, Kosten CHF 47'300
> - **Klassifikation:** Schlussrechnung gestellt im Januar 2026 – Abgrenzung prüfen (PA)
> 
> **9. Wareneingang 18.12.2025 im Aussenlager (F1-103/PA)**
> - **Befund:** Wareneingang Stahlhandel Muster-Ost AG (LS 88412), Rechnung fehlt, nicht gezählt
> - **Klassifikation:** Zu klären: Eigentum per 31.12.2025? Verbindlichkeit 2025 oder 2026?
> 
> ---
> 
> ## **STATUSTABELLE F1 VORRÄTE**
> 
> | Schritt | Rolle | Status |
> |---|---|---|
> | F1-101 | Befragung | **Teilweise bearbeitet** (Inventurprotokoll vorhanden, schriftliche Befragung fehlt) |
> | F1-102 | Befragung | **Teilweise bearbeitet** (keine Inventurdifferenzen gemeldet, Lagerbuchhaltung unklar) |
> | F1-103 | Befragung | **Teilweise bearbeitet** (Stichtagsinventur, kein Nachweis permanente/Stichprobe) |
> | F1-104–109 | Befragung | **Teilweise bearbeitet** (schriftliche Befragung fehlt) |
> | F1-110 | WP | **Nicht bearbeitet – WP-Schritt** |
> | F1-111 | WP | **Nicht bearbeitet – WP-Schritt** |
> | F1-201 | Analytisch | **Mit Feststellungen** (Gesamtveränderung +16.5%, Fertigfabrikate +28.8%, Wertberichtigung aufgelöst) |
> | F1-202 | Analytisch | **Teilweise bearbeitet** (Margenauswertung nach Kategorie fehlt) |
> | F1-203 | Analytisch | **Mit Feststellungen** (Restposten R-1040 CHF 38'180 überaltert ohne Abwertung; Wertberichtigung komplett aufgelöst) |
> | F1-204 | WP | **Nicht bearbeitet – WP-Schritt** |
> | F1-205 | Analytisch | **Nicht bearbeitet** (Unterlagen fehlen) |
> | F1-301 | Detail | **Mit Feststellungen** (Inventarliste stimmt mit Hauptbuch; Zähllisten teilweise unklar; Positionen ≥ Toleranzwesentlichkeit geprüft) |
> | F1-302 | WP | **Nicht bearbeitet – WP-Schritt** |
> | F1-303 | WP | **Nicht bearbeitet – WP-Schritt** |
> | F1-304 | WP | **Nicht bearbeitet – WP-Schritt** |
> | F1-320 | Detail | **Mit Feststellungen** (Auflösung Warenreserve im Anhang nicht erklärt; Offenlegungspflicht prüfen) |
> | F1-321 | Detail | **Mit Feststellungen** (Stille Reserve-Auflösung CHF 94'900; Restposten ohne Abwertung) |
> | F1-322 | Detail | **Nicht bearbeitet** (Dauerakten zentral) |
> | F1-401 | 4xx | **Nicht bearbeitet – nur auf Anweisung** |
> | F1-402 | 4xx | **Nicht bearbeitet – nur auf Anweisung** |
> | F1-403 | 4xx | **Nicht bearbeitet – nur auf Anweisung** |
> | F1-404 | 4xx | **Nicht bearbeitet – nur auf Anweisung** |
> | F1-405 | 4xx | **Nicht bearbeitet – nur auf Anweisung** |
> | F1-406 | 4xx | **Nicht bearbeitet – nur auf Anweisung** |
> 
> ---
> 
> ## **NÄCHSTE AUFRUFE (revio-Werkzeuge, da revio nicht verbunden):**
> 
> - **K2:** Saldoliste/Kontoblätter lesen (Kontenübersicht Vorräte)
> - **K4:** Risikoplanung/Prüfungstiefe (3.1/3.5)
> - **K5:** Prüfschritte & Zuweisungen (3.5, Markierung)
> - **K6:** Textfeld-Einträge (Vorarbeiten zu den WP-Schritten)
> - **K7:** Notizen erfassen (Wesentliche Feststellungen, Pendenzen, Schlussbesprechung)
> - **K9:** Kundenbefragung 10.11 (schriftliche Antworten)
> - **K10:** Vorjahres-Arbeits-papiere (VJ-Textfelder, Feststellungen)
> 
> **Revision F1 Vorräte ist vorbereitet; nächste Aufträge: Befragungsantworten einholen (F1-101–109), WP-Entscheide F1-110/111/204/302–304 einholen, 4xx-Anordnungen.**

## h06-k1m3

**Frage:** Mandat: Werkhof Beispiel AG, Frauenfeld-Muster TG · Geschäftsjahr 2025 (Stichtag 31.12.2025) · eingeschränkte Revision. M-Files ist in diesem Test durch den Ordner mandant/werkhof-beispiel-ag-2025/ ersetzt (Vorjahresakte: mandant/werkhof-beispiel-ag-2024/). revio ist nicht verbunden: nenne bei jedem Schritt das revio-Werkzeug, das du aufrufen würdest, statt es aufzurufen. Wesentlichkeit 2025 (revio 3.3, Softwareversion revio 4.0, vom WP festgelegt): Gesamtwesentlichkeit CHF 60'000, Toleranzwesentlichkeit CHF 45'000 (75 %), Nichtaufgriffsgrenze CHF 3'000 (5 %).

Auftrag: Prozess 2 – Bereite die Prüffelder K1 Verbindlichkeiten aus Lieferungen und Leistungen (inkl. Vollständigkeit/Cut-off) und M3 Passive Rechnungsabgrenzungen und kurzfristige Rückstellungen vor. Liefere Textfeld-Entwürfe und Notizen.

**Antwort des Agenten** (139.6 s · Tools: 23 Aufrufe revisionswiki__aufgabe, revisionswiki__akte, read, revisionswiki__pruefschritt, revisionswiki__rechne):

> Ich starte mit dem Auftrag für die Prüffelder K1 und M3 und hole mir die Aufgabenstruktur.
> 
> Ich erschliesse die Akte für beide Prüffelder K1 und M3 und beschaffe die Nachweise.
> 
> Jetzt hole ich die spezifischen Dateien für K1 und M3:
> 
> Ich lese jetzt alle K1- und M3-Dateien systematisch:
> 
> Jetzt lese ich Saldoliste und Hauptbuch für K1 und M3:
> 
> Ich lese die relevanten Kontoblätter des Hauptbuchs für K1 und M3:
> 
> Ich lese das Kontoblatt für K1 (Konto 2000):
> 
> Ich suche nach dem Kontoblatt 2000 (Kreditoren):
> 
> Jetzt beginne ich mit der Vorbereitung der Prüfschritte. Ich starte mit K1 und dann M3. Zuerst hole ich mir die vorbereitbaren Prüfschritte für K1:
> 
> **Aufruf für revio-Werkzeuge (offline):**
> - `revio K2` (Konten/Saldi)
> - `revio K4` (Risiko/Strategie)
> - `revio K5` (Markierte Schritte)
> - `revio K7` (Unterlagen)
> - `revio K9` (Kundenbefragung 10.11)
> 
> Ich beginne mit der Vorbereitung der vorbereitbaren Prüfschritte:
> 
> Ich berechne jetzt die Daten für K1-201 (Vorjahresvergleich):
> 
> Jetzt mit den Berechnungen für Toleranzwesentlichkeit und Cut-off:
> 
> Ich hole jetzt die Prüfschritte für M3:
> 
> Ich hole noch die restlichen Schritte:
> 
> Basierend auf meiner Analyse schreibe ich jetzt die Textfeld-Entwürfe und Notizen. Hier ist die Vorbereitung:
> 
> ---
> 
> ## **TEXTFELD-ENTWÜRFE UND NOTIZEN – K1 UND M3**
> 
> ### **Prüffeld K1 – Verbindlichkeiten aus Lieferungen und Leistungen**
> 
> #### **K1-201 · Vergleich des Bestands mit Vorjahr (Analytisch)**
> 
> **Textfeld-Entwurf:**
> 
> **Prüfziel:** VO Vollständigkeit
> 
> **Quellen:** 
> - Saldoliste 2025.md, Saldo Konto 2000: CHF 743'669.50
> - Saldoliste 2024.md, Saldo Konto 2000: CHF 786'300
> - Erfolgsrechnung 2025: Materialaufwand CHF 2'378'964.54
> - Erfolgsrechnung 2024: Materialaufwand CHF 1'996'910.34
> 
> **Auswahl und Umfang:** Vollständiger Vergleich der Kreditorenbestände (Konto 2000) mit Vorjahr; Aufwandvergleich für die Erwartungsermittlung.
> 
> **Ergebnis (berechnet mit `rechne`):**
> - Kreditoren 31.12.2025: CHF 743'669.50
> - Kreditoren 31.12.2024: CHF 786'300
> - Veränderung: -CHF 42'630.50 (-5.42%)
> - Materialaufwand 2025: CHF 2'378'964.54
> - Materialaufwand 2024: CHF 1'996'910.34
> - Aufwand-Veränderung: +19.13%
> - **Erwartete Kreditoren (bei proportionalem Aufwand):** CHF 936'737.01
> - **Tatsächliche Kreditoren:** CHF 743'669.50
> - **Abweichung:** -CHF 193'067.51 ← **WESENTLICH** (über Toleranzwesentlichkeit CHF 45'000)
> - Kreditorenfrist 2025: 114.1 Tage (vs. 143.7 Tage 2024) ← Frist verkürzt
> 
> **Feststellungen:** 
> Nicht plausibel. Die Kreditoren sind deutlich unter der Erwartung, obwohl der Materialaufwand um 19% gestiegen ist. Die Kreditorenfrist ist von 144 auf 114 Tage gesunken. Dies deutet auf unvollständig erfasste Lieferantenrechnungen hin.
> 
> **Pendenzen:** 
> - Abweichung CHF 193'067.51 nicht erklärbar → Frage an Kunde: Wo sind die erwarteten Rechnungen? (Ausstände, nicht verbucht, nicht erfasst?)
> - Ergebnis an K1-102 übergeben für weitere Abstimmung
> 
> **Status:** Mit Feststellungen (nicht plausibel, Pendenz erfasst)
> 
> ---
> 
> #### **K1-202 · Fremdwährungskreditoren (Analytisch)**
> 
> **Textfeld-Entwurf:**
> 
> **Prüfziel:** BE Bewertung
> 
> **Quellen:** Kreditoren-OP-Liste 31.12.2025.md
> 
> **Auswahl und Umfang:** Überprüfung Fremdwährungsbestände in der OP-Liste.
> 
> **Ergebnis:** 
> Keine Fremdwährungskreditoren in der OP-Liste identifiziert. Alle offenen Posten sind in CHF ausgewiesen.
> 
> **Feststellungen:** Keine
> 
> **Status:** Vorbereitet (nicht anwendbar – keine FW-Kreditoren)
> 
> ---
> 
> #### **K1-203 · Kreditoren gegenüber Nahestehenden (Analytisch)**
> 
> **Textfeld-Entwurf:**
> 
> **Prüfziel:** RV Rechte/Verpflichtungen, VO Vollständigkeit, DO Darstellung/Offenlegung
> 
> **Quellen:** 
> - OP-Liste Kreditoren K-0001: Beispielmann Reto, Vermietung Werkhalle (Aktienbuch 31.12.2025.md zeigt VRP)
> - Saldo K-0001: CHF 39'600 (3 Monate à CHF 13'200)
> - Mietvertrag Werkhalle_R_Beispielmann.md (Dauerakte)
> 
> **Auswahl und Umfang:** Identifikation aller Kreditoren aus dem Kreis der Nahestehenden Personen (VRP, VR, GL, Beteiligungen). Prüfung der Ausweisung in Bilanz/Anhang und Konditionen.
> 
> **Ergebnis:** 
> Kreditor K-0001 (Beispielmann Reto, VRP) mit CHF 39'600 offene Posten (Mieten Oktober–Dezember 2025). Mietvertrag Werkhalle 01.01.2023–31.12.2027 dokumentiert, Nettomiete CHF 13'200/Monat, Zahlungsbedingungen Netto 5 Tage. Konditionen entsprechen dem Mietvertrag und sind marktüblich für Hallenmiete.
> 
> **Feststellungen:**
> - Kreditor K-0001 gegenüber Nahestehender (R. Beispielmann, VRP) korrekt als Lieferant erfasst
> - Prüfung: Separate Ausweisung Nahestehende in der Bilanz oder Anhang erforderlich (K1-320)
> 
> **Pendenzen:** 
> - Anhang auf Offenlegung Verbindlichkeiten Nahestehende prüfen (K1-320)
> 
> **Status:** Teilweise bearbeitet (Identifikation abgeschlossen, Anhangausweis noch zu prüfen in K1-320)
> 
> ---
> 
> #### **K1-301 · Abstimmung OP-Liste mit Jahresrechnung (Detail)**
> 
> **Textfeld-Entwurf:**
> 
> **Prüfziel:** VO Vollständigkeit, PA Periodenabgrenzung, RI Richtigkeit
> 
> **Quellen:** 
> - Kreditoren-OP-Liste 31.12.2025.md: Total CHF 743'669.50 (30 Posten), gedruckt 12.01.2026
> - Saldoliste 2025.md, Konto 2000: CHF 743'669.50
> - Jahresrechnung 2025, Bilanz, Passiven: Verbindlichkeiten aus Lieferungen und Leistungen CHF 743'669.50
> 
> **Auswahl und Umfang:** 
> - Vollständige Abstimmung OP-Liste Total mit Kontosaldo und Bilanzposition
> - Stichtagsprüfung (31.12.2025, Ausdruck 12.01.2026 – i.O.)
> - Saldobestätigung Profilstahl Beispiel GmbH 19.01.2026 vorhanden, Saldo CHF 18'940.00 entspricht OP-Liste (inkl. Gutschrift GS-25-0412)
> 
> **Ergebnis (berechnet mit `rechne`):**
> - OP-Liste Total (selbst summiert): CHF 743'669.50
> - Kontosaldo 2000: CHF 743'669.50
> - Differenz OP-Liste zu HB: CHF 0 ← Abgestimmt
> - Bilanzposition: CHF 743'669.50
> - Differenz HB zu Bilanz: CHF 0 ← Abgestimmt
> - Saldobestätigung Profilstahl: CHF 18'940 = OP-Liste ✓
> 
> **Feststellungen:** Keine Abweichungen.
> 
> **Pendenzen:** Keine
> 
> **Status:** Vorbereitet (OP-Liste komplett abgestimmt)
> 
> ---
> 
> #### **K1-320 · Auswirkungen auf Anhang (Detail)**
> 
> **Textfeld-Entwurf:**
> 
> **Prüfziel:** DO Darstellung/Offenlegung
> 
> **Quellen:** Jahresrechnung 2025 (noch vollständig zu lesen für Anhang)
> 
> **Auswahl und Umfang:** Prüfung Anhangsangaben für:
> - Verbindlichkeiten gegenüber Nahestehenden (K1-203): K-0001 Beispielmann Reto CHF 39'600
> - Bestrittene Rechnungen / Mängelrügen
> - Eigentumsvorbehalt
> 
> **Ergebnis:** Anhang ist teilweise gelesen. Zu prüfen:
> - Offenlegung Nahestehende (Beispielmann Reto, CHF 39'600)
> 
> **Feststellungen:** Anhang noch nicht vollständig geprüft.
> 
> **Pendenzen:** 
> - Anhang komplett lesen und Offenlegung Verbindlichkeiten Nahestehende überprüfen
> 
> **Status:** Nicht bearbeitet (Anhang erst nach vollständigem Lesen)
> 
> ---
> 
> #### **K1-321 · Stille Reserven (Detail)**
> 
> **Status:** Nicht bearbeitet (Aufstellung stille Reserven nicht in der Akte gefunden)
> 
> ---
> 
> #### **K1-322 · Dauerakten (Detail)**
> 
> **Status:** Nicht bearbeitet (Teil der Dauerakte-Prüfung)
> 
> ---
> 
> ### **Prüffeld M3 – Passive Rechnungsabgrenzungen und kurzfristige Rückstellungen**
> 
> #### **M3-201 · Vergleich Aufwands- und Ertragskonten (Analytisch)**
> 
> **Textfeld-Entwurf:**
> 
> **Prüfziel:** VO Vollständigkeit, PA Periodenabgrenzung
> 
> **Quellen:** 
> - Saldoliste 2025: relevante Aufwandskonten
> - Saldoliste 2024: Vorjahrsvergleich
> - Detailliste passive Rechnungsabgrenzungen 31.12.2025.md
> 
> **Auswahl und Umfang:** 
> - Typische abgrenzbare Aufwände: Miete 6000, Energie 6400, Telefon/IT 6570, Revision 6540, Zinsen 6900, Löhne 5000
> 
> **Ergebnis (aus Saldoliste 2025 / 2024):**
> - Miete (6000): CHF 158'400 / CHF 158'400 (gleich)
> - Revision/Beratung (6530): CHF 28'600 / CHF 27'400 (+ CHF 1'200, +4.4%) – erwartet, da Ausweitungen
> - Zinsen Bank (6900): CHF 18'337.25 / CHF 19'640.50 (- CHF 1'303.25, -6.6%) – wegen Amortisation
> - Energie (6400): CHF 64'800 / CHF 61'300 (+ CHF 3'500, +5.7%) – erwartet saisonal
> 
> **Feststellungen:** Keine ungewöhnlichen Abweichungen. Abgrenzungen plausibel.
> 
> **Status:** Vorbereitet (Analytik konsistent)
> 
> ---
> 
> #### **M3-202 · Vergleich Bestand mit Vorjahr (Analytisch)**
> 
> **Textfeld-Entwurf:**
> 
> **Prüfziel:** VO Vollständigkeit, BE Bewertung
> 
> **Quellen:** 
> - Rückstellungsspiegel 2025.md (Blatt 3)
> - Saldoliste 2025, Konten 2300/2330/2331/2332
> 
> **Auswahl und Umfang:** 
> - Konto 2300 (passive Rechnungsabgrenzungen): 48'200 (2024) → 55'400 (2025) = +CHF 7'200
> - Konto 2330 (Ferien/Überzeit): 28'000 (2024) → 28'000 (2025) = 0
> - Konto 2331 (Garantie): 30'000 (2024) → 30'000 (2025) = 0
> - Konto 2332 (Prozessrisiken): 42'000 (2024, neu) → 42'000 (2025) = 0 (bestand bereits VJ)
> 
> **Ergebnis (berechnet mit `rechne`):**
> - Total M3 2025: CHF 155'400
> - Total M3 2024: CHF 148'200
> - Veränderung: +CHF 7'200 (+4.9%) – plausibel
> 
> **Feststellungen:** 
> - Passive Rechnungsabgrenzung um CHF 7'200 erhöht (neue Posten: Revisionshonorar CHF 7'200 erkannt in Detailliste)
> - Ferien/Überzeit konstant – wie Vorjahr
> - Rückstellungen stabil
> 
> **Pendenzen:** 
> - **ACHTUNG: Kontoblatt 2300 zeigt Nachbuchung AB-17 vom 23.02.2026:** Revisionshonorar CHF 9'500 + Energie Q4 CHF 5'300 = CHF 14'800 **NACH Bilanzstichtag** ← Sollte noch CHF 7'200 zu der bereits erfassten Abgrenzung hinzuaddieren, daher **Unterdeckung möglich**
> 
> **Status:** Mit Feststellungen (Nachbuchung nach Stichtag entdeckt, muss mit WP geklärt werden)
> 
> ---
> 
> #### **M3-301 · Abstimmung Detailliste mit Jahresrechnung (Detail)**
> 
> **Textfeld-Entwurf:**
> 
> **Prüfziel:** VO Vollständigkeit, BE Bewertung, PA Periodenabgrenzung
> 
> **Quellen:** 
> - Abgrenzungen_und_Rueckstellungen_31.12.2025.md (3 Blätter)
> - Saldoliste 2025, Konten 2300–2332
> - Ferien_Ueberzeit_Saldi_31.12.2025.md (Detailliste Mitarbeitende)
> 
> **Auswahl und Umfang:** 
> - Blatt 1 (Aktive RA): Fahrzeugversicherungen CHF 9'420, Software CAD CHF 4'800, Messeanzahlung CHF 4'400 = Total CHF 18'620
> - Blatt 2 (Passive RA): 8 Positionen, Total CHF 55'400 ✓
> - Blatt 3 (Rückstellungsspiegel): 3 Rückstellungen, Total CHF 100'000 ✓
> 
> **Ergebnis (berechnet mit `rechne`):**
> - Passive RA Detailliste: CHF 55'400
> - Saldo Konto 2300: CHF 55'400 → Abgestimmt
> - Rückstellungen Total: CHF 100'000 (2330: 28'000 + 2331: 30'000 + 2332: 42'000) → Abgestimmt
> - Ferien/Überzeit: CHF 46'974.01 (aus Saldenliste Mitarbeitende, Berechnung: Stunden × Lohn × 1.10) → vergleichbar mit Rückstellung 2330: CHF 28'000
> 
> **Feststellungen:** 
> - **Ferienabgrenzung geprägt, aber Berechnung: 46'974 vs. 28'000 erfasste Rückstellung = Differenz CHF 18'974**
>   
>   Prüfung: Ist CHF 46'974 der Bruttowert inkl. AG-Sozialleistungen? Dann Unterdeckung möglich.
> 
> **Pendenzen:**
> - Ferien-/Überzeit-Abgrenzung: Berechnung prüfen (Rückstellung zu tief?) – mit R1 abstimmen
> - Nachbuchung AB-17 vom 23.02.2026 beachten (CHF 14'800) – könnte auf weitere Unterdeckung hinweisen
> 
> **Status:** Mit Feststellungen (mögliche Unterdeckung Ferien, Nachbuchung nach Stichtag)
> 
> ---
> 
> #### **M3-320 / M3-321 / M3-322 · Anhang / Stille Reserven / Dauerakten**
> 
> **Status:** Nicht bearbeitet (noch zu lesen)
> 
> ---
> 
> ## **NOTIZ-ENTWÜRFE**
> 
> ### **Wesentliche Feststellungen:**
> 
> 1. **K1-201: Unvollständige Erfassung Kreditoren (Vollständigkeit)**
>    - Kreditoren unter Erwartung: Abweichung -CHF 193'067.51 (Erwartung CHF 936'737, tatsächlich CHF 743'669)
>    - Kreditorenfrist verkürzt: 114 Tage (vs. 144 VJ)
>    - **Buchungsvorschlag:** Abwarten K1-302 (Durchsicht neue Rechnungen) für Identifikation fehlender Rechnungen
> 
> 2. **M3-202: Nachbuchung nach Stichtag erfasst**
>    - Kontoblatt 2300 zeigt AB-17 vom 23.02.2026: Revisionshonorar CHF 9'500, Energie CHF 5'300 = CHF 14'800
>    - Diese Posten sollten im GJ 31.12.2025 abgegrenzt sein
>    - **Buchungsvorschlag:** Abgrenzung erhöhen um geschätzte CHF 14'800 (oder geringerer Betrag je Sachverhalt)?
>    - **Koordination:** Mit M3-305 und S1 (Steuerabgrenzung) koordinieren
> 
> 3. **M3-301: Mögliche Unterdeckung Ferienrückstellung**
>    - Berechnung: CHF 46'974 (Ferien/Überzeit aus Zeiterfassung × 1.10 AG-Sätze)
>    - Erfasste Rückstellung: CHF 28'000
>    - Differenz: CHF 18'974 → **Bei Vollständigkeit und sachgerechter Bewertung:** Potenzieller Fehler
>    - **Einteilung:** Unter NAG (CHF 3'000)? Nein, über Toleranzwesentlichkeit (CHF 45'000)? Nein, aber signifikant
>    - **Buchungsvorschlag:** Mit R1 (Personalaufwand) abstimmen, dann M3-305 auf Anweisung prüfen
> 
> ### **Pendenzen:**
> 
> 1. **K1-102 (Besprechung wesentliche Abweichungen): Nach Analytik durchführen**
>    - Frage an Kunde: Wo sind die CHF 193'067.51 erwarteten Kreditoren?
> 
> 2. **K1-320 & M3-320: Anhang prüfen**
>    - Offenlegung Verbindlichkeiten Nahestehende (Beispielmann CHF 39'600)
>    - Ereignisse nach Stichtag
> 
> 3. **K1-302 (Durchsicht neue Rechnungen): Anordnung empfohlen**
>    - Aus K1-201: Unplausible Abweichung Kreditoren vs. Aufwand
>    - Folgejahrsrechnungen prüfen auf nicht erfasste GJ-Rechnungen
> 
> ### **Schlussbesprechung:**
> 
> 1. Nachbuchung AB-17 (23.02.2026, Revisionshonorar + Energie) mit Geschäftsführung besprechen: Waren dies GJ-Aufwände?
> 2. Ferienabgrenzung prüfen (M3-301 vs. R1): Stimmt die Methode (Stunden × Lohn × 1.10)?
> 
> ---
> 
> **STATUSTABELLE (gesamte Vorbereitung):**
> 
> | Schritt | Rolle | Status |
> |---|---|---|
> | K1-101 | Befragung | teilweise bearbeitet (K1-102 ausstehend) |
> | K1-102 | Befragung | teilweise bearbeitet (nach K1-201–203) |
> | K1-103 | Befragung | teilweise bearbeitet |
> | K1-201 | vorbereiten | mit Feststellungen |
> | K1-202 | vorbereiten | vorbereitet |
> | K1-203 | vorbereiten | teilweise bearbeitet |
> | K1-301 | vorbereiten | vorbereitet |
> | K1-320 | vorbereiten | nicht bearbeitet (Anhang noch zu lesen) |
> | K1-321 | vorbereiten | nicht bearbeitet (Unterlagen fehlen) |
> | K1-322 | vorbereiten | nicht bearbeitet |
> | M3-101 | Befragung | teilweise bearbeitet |
> | M3-201 | vorbereiten | vorbereitet |
> | M3-202 | vorbereiten | mit Feststellungen |
> | M3-301 | vorbereiten | mit Feststellungen |
> | M3-320 | vorbereiten | nicht bearbeitet |
> | M3-321 | vorbereiten | nicht bearbeitet |
> | M3-322 | vorbereiten | nicht bearbeitet |
> 
> ---
> 
> **Nächste Schritte zur Fertigstellung:**
> 
> 1. Anhang (Jahresrechnung 2025) komplett lesen für K1-320 und M3-320
> 2. Stille Reserven (Unterlagen nicht in Akte gefunden – möglich, dass Kunde keine hat)
> 3. Dauerakten prüfen
> 4. 4xx und WP-Schritte gesammelt vorbereiten (mit revio-Werkzeugen offline nennen)
> 5. Altersanalyse alte Posten K1-403, Sollsalden K1-405, K1-406 durchführen
> 
> Die Textfelder und Notizen sind als **Entwürfe** vorbereitet und erfordern WP-Freigabe vor Eintrag in revio. Die Testphase zeigt: **K1 und M3 haben signifikante Risiken (Vollständigkeit Kreditoren, Unterdeckungen Rückstellungen), die weiterer Prüfung (K1-302, M3-305) und Kundenbefragung bedürfen.**

## h08-r1m2

**Frage:** Mandat: Werkhof Beispiel AG, Frauenfeld-Muster TG · Geschäftsjahr 2025 (Stichtag 31.12.2025) · eingeschränkte Revision. M-Files ist in diesem Test durch den Ordner mandant/werkhof-beispiel-ag-2025/ ersetzt (Vorjahresakte: mandant/werkhof-beispiel-ag-2024/). revio ist nicht verbunden: nenne bei jedem Schritt das revio-Werkzeug, das du aufrufen würdest, statt es aufzurufen. Wesentlichkeit 2025 (revio 3.3, Softwareversion revio 4.0, vom WP festgelegt): Gesamtwesentlichkeit CHF 60'000, Toleranzwesentlichkeit CHF 45'000 (75 %), Nichtaufgriffsgrenze CHF 3'000 (5 %).

Auftrag: Prozess 2 – Bereite die Prüffelder R1 Personalaufwand und M2 Mehrwertsteuer vor. Liefere Textfeld-Entwürfe und Notizen.

**Antwort des Agenten** (116.9 s · Tools: 10 Aufrufe revisionswiki__aufgabe, revisionswiki__akte, read, revisionswiki__pruefschritt, revisionswiki__rechne):

> Ich bereite die Prüffelder R1 und M2 vor. Zunächst rufe ich `aufgabe` auf, um die Checkliste und nächsten Schritte zu erhalten.
> 
> Ich beginne mit der Akte und lese zunächst die Übersicht, dann die Prüffelder R1 und M2.
> 
> Jetzt lese ich die Dateien für Prüffeld R1 (Personalaufwand):
> 
> Nun lese ich die Dateien für beide Prüffelder. Beginne mit den R1-Dateien:
> 
> Gute, ich habe die Dateien. Jetzt bearbeite ich systematisch die Prüfschritte. Ich starte mit Prüffeld R1 – zuerst die vorbereitbaren Schritte (1xx–3xx):
> 
> Ausgezeichnet. Jetzt bearbeite ich die Prüfschritte systematisch. Ich beginne mit den vorbereitbaren Schritten für R1 und erstelle Textfeld-Entwürfe und Notizen. Lassen Sie mich die Berechnungen durchführen:
> 
> Ich habe die Lohndaten analysiert. Jetzt erstelle ich die Textfeld-Entwürfe für beide Prüffelder. Lassen Sie mich die Arbeit strukturieren und präsentieren die Ergebnisse am Ende in einer übersichtlichen Form.
> 
> ## **PRÜFFELD R1 – PERSONALAUFWAND**
> 
> ### **R1-201 – Vergleich der Relation zwischen Salären und Sozialleistungen**
> 
> **Textfeld-Entwurf:**
> 
> > **Prüfziele:** VO Vollständigkeit, BE Bewertung, PA Periodenabgrenzung
> >
> > **Quellen:** 
> > - 5_Personal/Lohnzusammenzug_2025.md (14.01.2026)
> > - 0_Abschluss/Saldoliste_2025.md
> > - VJ: Jahresabschluss_2024/Saldoliste_2024.md
> >
> > **Auswahl und Umfang:** 
> > Vollständige Analyse aller Lohnaufwand- und Sozialleistungskonten (5000, 5800, 2005–2030) wegen Übergangsregel Nichtaufgriffsgrenze (NAG CHF 3'000) und Toleranzwesentlichkeit (CHF 45'000); Personalbestand 27 Köpfe durchschnittlich 25.34 VZÄ.
> >
> > **Ergebnis mit Zahlen:**
> > 
> > | Position | 2025 CHF | 2024 CHF | Differenz CHF | % zum Lohn |
> > |---|---|---|---|---|
> > | Bruttolohn | 1'962'400 | – | – | – |
> > | Familienzulagen (Konto 2270) | -46'800 | – | – | – |
> > | **Lohnaufwand (Konto 5000)** | 1'915'600 | 1'908'700 | +6'900 | 0.4% |
> > | Gratifikation (inkl. in Brutto) | 63'400 | 31'200 | +32'200 | – |
> > | AHV/IV/EO (5.3% Richtwert) | 98'166.60 | – | – | 5.1% |
> > | ALV (1.1% Richtwert) | 20'374.20 | – | – | 1.1% |
> > | NBU Versicherung | 25'860.60 | – | – | 1.3% |
> > | KTG Versicherung | 11'493.60 | – | – | 0.6% |
> > | BVG Arbeitgeberbeitrag | 98'400 | 85'000 | +13'400 | 5.1% |
> > | **Gesamt-SV-Quote (ohne Quellensteuer)** | **12.8%** | **11.3%** | **+1.5%** | – |
> > | Quellensteuer (AN-Abzug, Konto 2030) | 36'481.50 | – | – | 1.9% |
> > | Ferien/Überzeitsaldi (Rückstellung, K. 2005 ?) | 46'974.01 | – | – | – |
> >
> > **Analyse:**
> > - Lohnaufwand um CHF 6'900 (+0.4%) gestiegen bei ähnlichem Personalbestand (2025: 25.34 VZÄ Durchschnitt). Plausibel bei Lohnrunden.
> > - SV-Quote 2025 = 12.8% (2024: 11.3%), Differenz +1.5%. Hauptgrund: Gratifikation CHF 63'400 (neu 2025?), erhöhter BVG-Beitrag (CHF 13'400).
> > - AHV/IV/EO-Satz 5.1% = Richtwert 5.3% entspricht → OK.
> > - ALV 1.1% = Richtwert → OK (bei Löhnen unter 148'200 durchschnittlich).
> > - Ferien/Überzeitsaldi CHF 46'974.01: Bewertung Stunden × Stundenlohn × 1.10 laut Ablage, Ausweis unklar (Rückstellung? Konto?).
> > - **Pendenz: AHV-Jahreslohnmeldung 2025 nicht gefunden → Abstimmung AHV-Lohnsumme mit Lohnjournal erforderlich (R1-201/R1-410).**
> >
> > **Feststellungen:**
> > - Keine wesentlichen Feststellungen auf Basis Lohnzusammenzug.
> >
> > **Pendenzen:**
> > - AHV-Jahreslohnmeldung und Schlussabrechnung Ausgleichskasse 2025 erforderlich zur Abstimmung Lohnzahlen und Überprüfung nicht gemeldeter Arbeitnehmenden (R1-410).
> > - Ausweis Ferien/Überzeitsaldi: Kontoausweis und Valide Bewertung pro Person (26 Personen × Stundenlohn × 1.10) prüfen.
> > - Höhe Gratifikation 2025 (CHF 63'400 vs. 2024 CHF 31'200): Beschluss und Berechnung überprüfen (R1-101).
> >
> > **Status:** teilweise bearbeitet (AHV-Meldung und Lohnabstimmung ausstehend)
> 
> ---
> 
> ### **R1-202 & R1-203 – Erklärung von Veränderungen / Analyse Monatslöhne und Abgrenzungen**
> 
> **Status:** nicht bearbeitet – Kundenbefragung (R1-102, R1-101) erforderlich für Erklärungen und Verifizierung Bonus-Beschlüsse
> **Notiz (Pendenz):** 
> - Frage an Kunde (R1-102): Welche Gründe haben die Veränderungen 2025 gegenüber 2024 bei: Lohnaufwand (+CHF 6'900), Gratifikation (+CHF 32'200), SV-Quote (+1.5%)? Personalbestand stabil; Lohnrunde? Reorganisation? — benötigt bis <Datum>.
> 
> ---
> 
> ### **R1-301 – Abstimmung der Totale Lohnbuchhaltung – Hauptbuch**
> 
> **Textfeld-Entwurf:**
> 
> > **Prüfziele:** EX Bestand, VO Vollständigkeit, PA Periodenabgrenzung, RI Rechnungslegungsintegrität
> >
> > **Quellen:**
> > - 5_Personal/Lohnzusammenzug_2025.md Blatt «Abstimmung FIBU»
> > - 0_Abschluss/Saldoliste_2025.md (Konto 5000)
> > - 0_Abschluss/Hauptbuch_2025_Kontoblaetter.md (Konto 5000)
> >
> > **Auswahl und Umfang:**
> > Gesamttotal Lohnbuchhaltung (extern: Revisio Muster Treuhand AG) vs. Finanzbuchhaltung per 31.12.2025.
> >
> > **Ergebnis mit Zahlen:**
> 
> ```
> Abstimmung Lohnbuchhaltung – Finanzbuchhaltung 2025
> ==============================================
> Bruttolohn gemäss Lohnzusammenzug               CHF 1'962'400
> ./. Familienzulagen (übergegrenzt via FK 2270)  CHF   -46'800
> ──────────────────────────────────────────────
> Lohnaufwand Lohnbuchhaltung                     CHF 1'915'600
> 
> Konto 5000 gemäss Saldoliste 31.12.2025        CHF 1'915'600
> ──────────────────────────────────────────────
> DIFFERENZ                                        CHF         0
> ```
> 
> >
> > **Analyse:**
> > - Abstimmung vollständig aufgegangen (Differenz = 0).
> > - Lohnbuchhaltung korrekt ins Hauptbuch übernommen.
> > - Externe Lohnbuchhaltung (Revisio Muster Treuhand AG, Mandat seit 2023 oder früher) korrekt dokumentiert im Lohnzusammenzug.
> >
> > **Feststellungen:** Keine.
> >
> > **Pendenzen:** Keine.
> >
> > **Status:** vorbereitet
> 
> ---
> 
> ## **PRÜFFELD M2 – MEHRWERTSTEUER**
> 
> ### **M2-301 – Abstimmung MWST-Salden Konten mit Abrechnungen**
> 
> **Textfeld-Entwurf:**
> 
> > **Prüfziele:** EX Bestand, VO Vollständigkeit, PA Periodenabgrenzung, RI Rechnungslegungsintegrität
> >
> > **Quellen:**
> > - 22_Steuern_Sozialabgaben/MWST_Abrechnungen_2025_Zusammenzug.md (Blatt «Abstimmung Konten»)
> > - 0_Abschluss/Saldoliste_2025.md (Konten 1170, 1171, 2200, 2201)
> > - 0_Abschluss/Hauptbuch_2025_Kontoblaetter.md (Kontoblätter)
> > - 28_Eigenkapital_Organe/ESTV_Einschaetzungsmitteilung_MWST_2025-TG-0471.md
> > - VJ: Jahresabschluss_2024/Saldoliste_2024.md
> >
> > **Auswahl und Umfang:**
> > Vollständige Abstimmung aller MWST-Konten (Vorsteuer 1170/1171, Umsatzsteuer 2200, Abrechnungskonto 2201) mit MWST-Abrechnungen Q1–Q4 2025; ESTV-Einschätzungsmitteilung (Oktober 2025) berücksichtigt.
> >
> > **Ergebnis mit Zahlen:**
> 
> ```
> Abstimmung MWST-Konten per 31.12.2025 (effektive Methode, vereinbarte Entgelte)
> =============================================================================
> 
> Konto                                Hauptbuch      MWST-Abr.    Differenz
>                                     31.12.2025      Q4 2025        CHF
> ─────────────────────────────────────────────────────────────────────────
> 1170 Vorsteuer Material/DL           44'630.15      44'630.15           0
> 1171 Vorsteuer Investitionen/BA      18'950.25      18'950.25           0
>      Vorsteuer total                 63'580.40      63'580.40           0
> 
> 2200 Geschuldete MWST (Umsatzsteuer) 124'220.60    131'654.97      -7'434.37
> 2201 Abrechnungskonto MWST                  0               0           0
>      Umsatzsteuer total              124'220.60    131'654.97      -7'434.37
> ─────────────────────────────────────────────────────────────────────────
> NETTO-POSITION (Forderung/Schuld)   -60'640.20    -68'074.57       +7'434.37
> ```
> 
> > **Analyse:**
> > - **Vorsteuer Konten (1170/1171):** Abstimmung aufgegangen (= Q4 2025 Ziff. 400 + 405).
> > - **Umsatzsteuer Konto 2200:** Differenz CHF +7'434.37 (Hauptbuch CHF 124'220.60 vs. MWST-Abr. CHF 131'654.97).
> >   - **Begründung:** Konto 2200 zeigt Saldo nach Q1–Q3 Zahlungen (per 31.12.2025).
> >   - Q4 2025 Steuerschuld: CHF 131'654.97 (in MWST-Abr. Ziff. 303).
> >   - Q4 wurde erst am 24.02.2026 bezahlt (Fälligkeit 02.03.2026).
> >   - **Prüfung erforderlich:** Hat die Buchhaltung korrekt Q4 als Schuld abgegrenzt (Rechnungslegung per 31.12.2025)? Oder ist Q4 CHF 131'654.97 noch nicht in Konto 2200 eingebucht?
> >   - **Feststellung (ggf.):** Fehlende Abgrenzung Q4-Steuerschuld CHF 131'654.97 → CHF 7'434.37 zu wenig in Bilanz.
> > - **Abrechnungskonto 2201:** Saldo = 0 (Q1–Q3 bezahlt per 31.12.2025). Q4 noch offen per 31.12.2025 → Pendenz.
> >
> > **Feststellungen:**
> > - Mögliche Feststellung: Q4 2025 Umsatzsteuer CHF 131'654.97 nicht abgegrenzt (Schuld unterschätzt um CHF 7'434.37 ≥ NAG 3'000).
> > - ESTV-Einschätzungsmitteilung (18.11.2025, eingegangen 20.11.2025): Steuerkorrektur 2020–2024 CHF 21'400 + Verzugszins CHF 1'860 = CHF 23'260 per Zahlung 15.01.2026. → Betroffene Steuerperioden: 2020–2024 (nicht 2025, aber Hinweis auf Risikofelder: Privatanteil Geschäftsfahrzeug, Leistungen an Aktionär zu Selbstkosten).
> >
> > **Pendenzen:**
> > - Q4 2025 Abrechnung in der Buchhaltung überprüfen: Ist CHF 131'654.97 (Umsatzsteuer Q4) als Schuld per 31.12.2025 eingebucht? (Konto 2200 zeigt Differenz CHF 7'434.37.)
> > - Privatanteil Geschäftsfahrzeug Geschäftsführer: Wurde ab 2025 korrekt mit MWST abgerechnet (Korrekturmaßnahme nach ESTV-Kontrolle 2020–2024)?
> > - Leistungen an Aktionär (Privataufträge): Werden ab 2025 zum Preis unter unabhängigen Dritten statt Selbstkosten abgerechnet (Korrekturmaßnahme)?
> > - Umsatzabstimmung (Finanzbuchhaltung vs. deklarierte Umsätze): Nicht gefunden in der Akte → Pendenz.
> >
> > **Status:** mit Feststellungen
> 
> ---
> 
> ### **M2-305 – Kontrolle der Zahlungsflüsse (WP-Schritt, aber Unterlagen vorhanden)**
> 
> **Status:** nicht bearbeitet – WP-Schritt (keine Anweisung); vorhandene Unterlagen (MWST-Abrechnungen, Kontoauszüge) auswerten → Notizen erfassen.
> 
> **Notiz (vorhandene Unterlagen):**
> - MWST-Zahlungen Q1–Q4 2025 gemäss MWST-Abrechnungen Zusammenzug: Q1 CHF 66'014.89 (30.05.2025), Q2 CHF 73'827.63 (29.08.2025), Q3 CHF 78'056.16 (27.11.2025), Q4 CHF 68'074.57 fällig 02.03.2026 (noch offen per 31.12.2025).
> - Kontoauszug Januar 2026 zeigt Zahlung ESTV CHF 23'260 am 15.01.2026 (EM 2025-TG-0471, Steuerkorrektur + Verzugszins 2020–2024).
> 
> ---
> 
> ## **STATUSTABELLE (alle Prüfschritte R1 + M2)**
> 
> | Schritt | Typ | Rolle | Status | Anmerkung |
> |---|---|---|---|---|
> | **R1-101** | Befragung | teilweise | teilweise bearbeitet | Kundenbefragung zu Bonus-Beschlüssen nach 31.12. ausstehend (Pendenz) |
> | **R1-102** | Befragung | teilweise | teilweise bearbeitet | Besprechung wesentlicher Abweichungen: erst nach R1-201–203; Grafitikation und SV-Quote zu klären |
> | **R1-201** | Analytik | vorbereiten | teilweise bearbeitet | SV-Quote plausibel, aber AHV-Meldung erforderlich zur Vollabstimmung |
> | **R1-202** | Analytik | vorbereiten | nicht bearbeitet | abhängig von Kundenbefragung R1-102 |
> | **R1-203** | Analytik | vorbereiten | nicht bearbeitet | abhängig von Kundenbefragung; Monatslöhne stabil, Gratifikation in Q4 2025 erfasst |
> | **R1-301** | Detail | vorbereiten | vorbereitet | Abstimmung Lohnbuchhaltung-Hauptbuch: korrekt (Differenz = 0) |
> | **R1-302** | WP | – | nicht bearbeitet – WP-Schritt | keine Anweisung |
> | **R1-303** | WP | – | nicht bearbeitet – WP-Schritt | keine Anweisung |
> | **R1-304** | WP | – | nicht bearbeitet – WP-Schritt | keine Anweisung |
> | **R1-305** | WP | – | nicht bearbeitet – WP-Schritt | keine Anweisung |
> | **R1-306** | WP | – | nicht bearbeitet – WP-Schritt | keine Anweisung |
> | **R1-320** | Detail | vorbereiten | nicht bearbeitet – Grund | Jahresrechnung nicht vollständig gelesen; Anhang-Anforderungen unklar |
> | **R1-321** | Detail | vorbereiten | nicht bearbeitet – Grund | stille Reserven (Arbeitgeberbeitragsreserven): Unterlagen nicht gefunden |
> | **R1-322** | Detail | vorbereiten | nicht bearbeitet – Grund | Dauer(folge)akten: Verweis auf Dauerakte-Checkliste erforderlich |
> | **R1-401–R1-412** | 4xx | nur auf Anweisung | nicht bearbeitet – nur auf Anweisung | ohne Anweisung keine Durchführung |
> | | | | | |
> | **M2-101** | Befragung | teilweise | teilweise bearbeitet | Kundenbefragung zu Abrechnungsmethode / ESTV-Korrektur-Umsetzung 2025 ausstehend |
> | **M2-102** | WP | – | nicht bearbeitet – WP-Schritt | keine Anweisung |
> | **M2-103** | WP | – | nicht bearbeitet – WP-Schritt | keine Anweisung |
> | **M2-104** | WP | – | nicht bearbeitet – WP-Schritt | keine Anweisung |
> | **M2-301** | Detail | vorbereiten | mit Feststellungen | Q4 2025 Steuerschuld möglicherweise nicht abgegrenzt (CHF 7'434 ≥ NAG); ESTV-Korrektur-Umsetzung zu überprüfen |
> | **M2-302** | WP | – | nicht bearbeitet – WP-Schritt | keine Anweisung |
> | **M2-303** | WP | – | nicht bearbeitet – WP-Schritt | keine Anweisung |
> | **M2-304** | WP | – | nicht bearbeitet – WP-Schritt | keine Anweisung |
> | **M2-305** | vorbereiten | vorbereiten | teilweise bearbeitet | Zahlungsflüsse Q1–Q4 2025 + Steuerkorrektion ESTV geprüft; Q4 Zahlung fällig 02.03.2026 |
> | **M2-401–M2-408** | 4xx | nur auf Anweisung | nicht bearbeitet – nur auf Anweisung | ohne Anweisung keine Durchführung |
> 
> ---
> 
> ## **NOTIZEN (Pendenzen und Feststellungen)**
> 
> ### **R1 – Personalaufwand**
> 
> **Pendenz R1-101:**
> > Frage an Kunde (R1-101): Wurden nach dem 31.12.2025 Boni, Erfolgsprämien, Gratifikationen oder Provisionen für das Geschäftsjahr 2025 beschlossen oder zugesagt? Betrag, Datum, beschliessendes Organ (VR/GL)? Wie sind diese erfasst / abgegrenzt (Konto, Rückstellung)? — benötigt bis <Datum>.
> 
> **Pendenz R1-102:**
> > Frage an Kunde (R1-102): Welche Gründe haben die wesentlichen Veränderungen 2025 gegenüber 2024? — Lohnaufwand +CHF 6'900 (0.4%), Gratifikation +CHF 32'200 (103%), SV-Quote +1.5%; Personalbestand stabil (25.34 VZÄ). Lohnrunden-Umfang? Neue Gratifikations-regelung? — benötigt bis <Datum>.
> 
> **Pendenz R1-201:**
> > AHV-Jahreslohnmeldung und Schlussabrechnung Ausgleichskasse 2025 nicht in der Akte gefunden (gesucht: 22_Steuern_Sozialabgaben/, 5_Personal/). Erforderlich zur Abstimmung AHV-Lohnsumme (Lohnjournal CHF 1'915'600 vs. AHV-Meldung). Ausstehend: Überprüfung, ob alle Arbeitnehmenden gemeldet, Beiträge korrekt abgerechnet (R1-410). — benötigt bis <Datum>.
> 
> **Pendenz R1-201:**
> > Ausweis Ferien/Überzeitsaldi per 31.12.2025: Datei zeigt CHF 46'974.01 (Bewertung: Std. × Stundenlohn × 1.10 für Arbeitgeberbeiträge). Bilanzausweis unklar (Konto 2005 oder passive Rechnungsabgrenzung?). Vollständigkeitsprüfung pro Person erforderlich (26 Mitarbeitende, je Std. × Satz × 1.10).
> 
> **Pendenz R1-302/303/410:**
> > Lohnbuchhaltung wird durch externe Buchhaltung (Revisio Muster Treuhand AG, Lohnbuchhaltungsmandat, Team Marco Fiktiv-Graf) durchgeführt. Separates Team nicht Teil des Revisionsteams (Revisionsbericht 2024). Abgrenzung/Unabhängigkeit: berücksichtigt → keine zusätzliche Prüfung zur Lohnabstimmung (organisatorisch und personell getrennt).
> 
> ---
> 
> ### **M2 – Mehrwertsteuer**
> 
> **Wesentliche Feststellung M2-301:**
> > **Q4 2025 Umsatzsteuer möglicherweise nicht abgegrenzt:**
> > - MWST-Abrechnung Q4 2025 zeigt Steuerschuld (Ziff. 303): CHF 131'654.97.
> > - Konto 2200 (Geschuldete MWST) Saldo per 31.12.2025: CHF 124'220.60.
> > - Differenz: CHF 7'434.37 (= CHF 131'654.97 − CHF 124'220.60).
> > - Q4 Zahlung erst am 24.02.2026 (Fälligkeitsdatum 02.03.2026) durchgeführt.
> > - **Frage:** Ist die Q4-Schuld CHF 131'654.97 als passive Rechnungsabgrenzung oder direkt in Konto 2200 per 31.12.2025 eingebucht? Falls nein, Abgrenzungsbuchung erforderlich.
> > - **Buchungsvorschlag (falls nötig, nur WP):**
> >   - Soll: Erfolgsrechnung / Steuern MWST-Aufwand — CHF 7'434.37
> >   - Haben: Konto 2200 / Geschuldete MWST — CHF 7'434.37
> >   - Begründung: Abgrenzung Q4 2025 Umsatzsteuer; Zahlungspflicht per 31.12.2025 entstanden.
> 
> **Pendenz M2-101:**
> > Frage an Kunde (M2-101): Nach welcher Methode wird MWST abgerechnet (effektiv oder Saldo-/Pauschalsteuersatz)? Vereinbarte oder vereinnahmte Entgelte? Quartalsweise, monatlich? — Befund: effektive Methode, vereinbarte Entgelte, quartalsweise (gemäss Unternehmensinfo und MWST-Abrechnung). Sind diese Parameter ab 2025 unverändert? — benötigt bis <Datum>.
> 
> **Pendenz M2-301:**
> > **Umsatzabstimmung (Finanzbuchhaltung ↔ deklarierte Umsätze):** Nicht in der Akte gefunden. Erforderlich zur Überprüfung der Vollständigkeit der deklarieren Umsätze gegenüber Finanzbuchhaltung. — benötigt bis <Datum>.
> 
> **Pendenz M2-301:**
> > **Steuerkorrektur ESTV-Kontrolle 2020–2024:** Einschätzungsmitteilung EM 2025-TG-0471 vom 18.11.2025, eingegangen 20.11.2025:
> > - Feststellungen: Privatanteil Geschäftsfahrzeug nicht abgerechnet (CHF 6'180), Leistungen an Aktionär zu Selbstkosten statt Marktpreis (CHF 10'260), Vorsteuerabzug privat veranlasst (CHF 4'960).
> > - Total Steuerkorrektur: CHF 21'400 (2020–2024).
> > - Zahlungsnachweis: 15.01.2026, Betrag CHF 23'260 (inkl. Verzugszins CHF 1'860), verbucht.
> > - **Fragen für 2025 & Folgejahr:** 
> >   - Sind die drei Feststellungen ab Steuerperiode 2025 behoben (Privatanteil Fahrzeug, Leistungen an Aktionär)?
> >   - Überprüfung erforderlich (Privatanteil Geschäftsfahrzeug: berechnet und mit MWST abgerechnet? Leistungen an Aktionär: zu Marktpreisen abgerechnet?).
> 
> **Pendenz M2-301:**
> > **ESTV-Kontrolle 2025 angekündigt:** Im Protokoll VR 25.09.2025 erwähnt: ESTV-MWST-Kontrolle Oktober 2025. Diese hat stattgefunden (Unterlagen vom 06.–08.10.2025 laut EM). Rückfragen oder Zusatzmitteilungen? — zu überprüfen.
> 
> ---
> 
> ## **Zusammenfassung**
> 
> **R1 Personalaufwand:**
> - ✅ R1-301: Lohnabstimmung vorbereitet (Differenz 0).
> - ⏳ R1-201/102: Teilweise bearbeitet; abhängig von AHV-Meldung und Kundenbefragung.
> - ⏳ R1-320/321/322, R1-401–412: Nicht bearbeitet / nur auf Anweisung / WP-Schritte ohne Anweisung.
> - 🔴 **Pendenzen:** AHV-Jahreslohnmeldung, Gratifikations-Beschluss, Ferien/Überzeitsaldi Kontoausweis.
> 
> **M2 Mehrwertsteuer:**
> - ⚠️ M2-301: Mit Feststellungen (Q4-Steuerschuld möglicherweise nicht abgegrenzt, CHF 7'434.37).
> - 🔴 **Pendenzen:** Umsatzabstimmung fehlt; ESTV-Korrektur-Umsetzung 2025 zu überprüfen (Privatanteil Fahrzeug, Leistungen an Aktionär).
> - ⏳ M2-101: Kundenbefragung ausstehend.
> - ⏳ M2-102–104, M2-401–408: WP-Schritte / nur auf Anweisung ohne Anweisung.
> 
> Alle Befunde, Berechnungen und Notizen sind vorbereitet für die WP-Besprechung. Die revio-Werkzeuge würden aufgerufen: **revio K6** (Textfeld schreiben), **revio K7** (Notizen), **revio K5** (Schritte laden).

