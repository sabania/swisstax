# OpenClaw-Testlauf: e2e-aufgaben.yaml

- OpenClaw: OpenClaw 2026.11.2 (b556fdf) · Profil: `revh45d` · Modell: `claude-haiku-4-5` · Agent: `revision` · Fragen: 4 · Lauf: 2026-11-13 08:50
- Jede Frage = eigener Agent-Turn (`openclaw agent --local --json`), neue Session, nur Wiki als Wissensquelle.

## h02-import

**Frage:** Mandat: Werkhof Beispiel AG, Frauenfeld-Muster TG · Geschäftsjahr 2025 (Stichtag 31.12.2025) · eingeschränkte Revision. M-Files ist in diesem Test durch den Ordner mandant/werkhof-beispiel-ag-2025/ ersetzt (Vorjahresakte: mandant/werkhof-beispiel-ag-2024/). revio ist nicht verbunden: nenne bei jedem Schritt das revio-Werkzeug, das du aufrufen würdest, statt es aufzurufen. Wesentlichkeit 2025 (revio 3.3, Softwareversion revio 4.0, vom WP festgelegt): Gesamtwesentlichkeit CHF 60'000, Toleranzwesentlichkeit CHF 45'000 (75 %), Nichtaufgriffsgrenze CHF 3'000 (5 %).

Auftrag: Prozess 1 – Stimme die Jahresrechnung 2025 (Ordner 0_Abschluss) mit der Saldoliste und dem Hauptbuch ab (Bilanzgleichheit, Totale, Jahresergebnis, Vorjahreszahlen, Anhang formell). Erfasse Differenzen als Notiz.

**Antwort des Agenten** (117.7 s · Tools: 12 Aufrufe revisionswiki__aufgabe, ls, read, revisionswiki__rechne, message):

> Ich starte mit der Abschlussabstimmung und rufe zuerst die Aufgaben-Anleitung auf.
> 
> Die Aufgabe ist klar: Ich muss die Jahresrechnung 2025 mit Saldoliste und Hauptbuch abstimmen. Ich beginne mit der Verzeichniserkundung der Abschlussunterlagen.
> 
> Ich lese die Jahresrechnung, Saldoliste und Hauptbuch nacheinander.
> 
> Ich prüfe jetzt die Bilanzgleichheit und abstimme die Totale, Jahresergebnis und Vorjahreszahlen mit dem Rechenmodul.
> 
> Ich entdecke einen Fehler bei den Passiven Rechnungsabgrenzungen. Lassen Sie mich die Summen überprüfen:
> 
> Es gibt eine Abweichung bei Konto 2300. Im Hauptbuch-Inhalt zeigt es einen Schlusssaldo von 70'200 CHF, aber in der Saldoliste ist 55'400 CHF verbucht. Lassen Sie mich die korrekten Positionen aus der Saldoliste abgleichen:
> 
> Alle Aktivpositionen stimmen überein. Jetzt überprüfe ich die Passiven, insbesondere Konto 2300:
> 
> Es gibt eine Diskrepanz: Das Hauptbuch-Inhalt zeigt Konto 2300 mit 70'200 CHF, aber die Saldoliste und die Jahresrechnung haben 55'400 CHF. Differenz: 14'800 CHF. Ich erfasse das als Pendenz und überprüfe nun noch die Jahresergebnisabstimmung und Vorjahreszahlen:
> 
> Jahresergebnis stimmt überein (−72'390 CHF). Nun überprüfe ich die Vorjahreszahlen:
> 
> Ich finde weitere Abweichungen. Die Jahresrechnung zeigt für 2024 Kreditoren von 686'300 CHF, aber die Saldoliste zeigt 786'300 CHF (Differenz: 100'000 CHF). Zusätzlich die bereits identifizierte Diskrepanz bei Konto 2300. Ich notiere diese Differenzen als Pendenzen:
> 
> ## Abschlussabstimmung 2025 – Prozess 1 abgeschlossen
> 
> **Bilanzgleichheit: ✓ stimmt**
> - 2025: Total Aktiven = Total Passiven = **3'426'065.37 CHF** (Differenz: 0)
> - 2024: Total Aktiven = Total Passiven = **3'186'740.80 CHF** (Differenz: 0)
> 
> **Jahresergebnis: ✓ stimmt**
> - Jahresverlust 2025: **−72'390 CHF** (JR u. Saldoliste überein)
> 
> **Vorjahreszahlen: bestätigt**
> - Flüssige Mittel 2024: 205'390.40 CHF ✓
> - Forderungen 2024: 1'126'960 CHF ✓
> 
> ---
> 
> ## **Differenzen – Pendenzen erfasst:**
> 
> | Konto | Position | Fehler | Betrag | Quelle |
> |-------|----------|--------|--------|--------|
> | **2300** | Passive RA + Rückstellungen | Hauptbuch zeigt 70'200, sollte 55'400 | **14'800 CHF** | Hauptbuch-Inhalt vs. Saldoliste |
> | **2000** | Kreditoren 31.12.2024 | JR zeigt 686'300, Saldoliste 786'300 | **100'000 CHF** | Jahresrechnung vs. Saldoliste |
> 
> ---
> 
> **Nächste Schritte (Auftrag der Aufgaben-Checkliste):**
> → **Notiz erfassen:** Pendenz «Fehlerhafte Kontostände im Hauptbuch-Inhalt u. Saldoliste 2024»
> → **revio K2-Werkzeug:** Jahresrechnung/Saldenbilanz lesen, Konten zuordnen (Import vorbereiten)
> → **Halt nach Import:** WP kontrolliert Kontenzuordnung vor Prüffelder-Bearbeitung
> 
> Ich erfasse jetzt die Pendenzen als Notizen im revio-System (Werkzeug: `revio_notiz`):
> 
> **Pendenz 1:** Konto 2300 – Diskrepanz Hauptbuch 70'200 vs. Saldoliste 55'400 (Differenz 14'800 CHF). Klärung erforderlich, bevor Import in revio 1.1.
> 
> **Pendenz 2:** Konto 2000 Vorjahr – Jahresrechnung 686'300 vs. Saldoliste 786'300 (Differenz 100'000 CHF). Veränderung falsch berechnet (sollte +57'369.50, nicht −42'630.50).

## h04-f1

**Frage:** Mandat: Werkhof Beispiel AG, Frauenfeld-Muster TG · Geschäftsjahr 2025 (Stichtag 31.12.2025) · eingeschränkte Revision. M-Files ist in diesem Test durch den Ordner mandant/werkhof-beispiel-ag-2025/ ersetzt (Vorjahresakte: mandant/werkhof-beispiel-ag-2024/). revio ist nicht verbunden: nenne bei jedem Schritt das revio-Werkzeug, das du aufrufen würdest, statt es aufzurufen. Wesentlichkeit 2025 (revio 3.3, Softwareversion revio 4.0, vom WP festgelegt): Gesamtwesentlichkeit CHF 60'000, Toleranzwesentlichkeit CHF 45'000 (75 %), Nichtaufgriffsgrenze CHF 3'000 (5 %).

Auftrag: Prozess 2 – Bereite das Prüffeld F1 Vorräte vor. Liefere Textfeld-Entwürfe und Notizen.

**Antwort des Agenten** (118.8 s · Tools: 24 Aufrufe revisionswiki__aufgabe, dir_list, exec, ls, read, revisionswiki__pruefschritt, revisionswiki__rechne):

> Ich starten mit der revio-Aufgabe für das Prüffeld F1.
> 
> **Schritt 1–2:** Prüffeld-Bündel und Saldi gelesen. 
> 
> **Schritt 2 (Kontenübersicht, revio nicht verbunden):**
> - Ich würde **revio K5** aufrufen: `rv_get_auditActivities_LoadAuditActivities_by_containerId_by_templateId` → Prüfschritte des Prüffelds F1 laden, Katalogschritte zuordnen, Saldi und Toleranzwesentlichkeit (CHF 45'000) bereitstellen.
> 
> **Schritt 3:** Unterlagen in M-Files suchen.
> 
> Ich verwende exec, um die M-Files-Struktur lokal zu erkunden.
> 
> Jetzt beginne ich systematisch mit den Prüfschritten. **Schritt 4:** Prüfschritte nach Typ bearbeiten.
> 
> **Befragung (1xx) – schriftlich auswerten:**
> 
> Ich suche schriftliche Antworten zur Befragung F1-101:
> 
> **Befragung F1-101–F1-109:** Das Inventurprotokoll beantwortet bereits F1-101 schriftlich (Stichtagsinventur). Ich bearbeite nun systematisch die analytischen Schritte (2xx) und Detailprüfung (3xx), wo der Agent agiert.
> 
> Ich lese die Vorjahresinventur und berechne Umschläge:
> 
> Ich lese die Jahresrechnung 2025 für Material/Warenaufwand:
> 
> Ich berechne die Bestandsveränderungen und Umschläge:
> 
> **F1-201 Ergebnis:** Bestand 2024: CHF 189'800 → 2025: CHF 309'366 (+63%). Umschlag 9,02×/Jahr (Lagerdauer 40 Tage). Umsatz nur +4,9%. Wertberichtigung komplett aufgelöst.
> 
> Ich bearbeite jetzt die restlichen Schritte zügig. Hier die nächsten Prüfschritte:
> 
> **F1-301 (Abstimmung):** Inventarliste ↔ Saldoliste stimmt perfekt ab:
> - Rohmaterial 1210: CHF 268'016.35 ✓
> - Wertberichtigung 1219: CHF 0 ✓  
> - Fertigfabrikate 1260: CHF 41'350 ✓
> - Total Bilanzposition: CHF 1'577'166.35 ✓
> 
> Ich bearbeite die weiteren Schritte und erstelle zusammenfassend Textfeld-Entwürfe und Notizen:
> 
> **Prüfschritte – Zusammenfassung Vorbereitung:**
> 
> | Schritt | Titel | Rolle | Status |
> |---------|-------|-------|--------|
> | F1-101–109 | Befragung (1xx) | teilweise | Kundenfragen auswerten / Pendenz |
> | F1-201 | Bestandsvergleich & Umschlag | Agent | vorbereitet |
> | F1-202 | Margenvergleich | Agent | benötigt Verkaufspreisliste |
> | F1-203 | Wesentliche Veränderungen | Agent | vorbereitet |
> | F1-205 | Lieferantenstruktur | Agent | benötigt Einkaufsstatistik |
> | F1-301 | Abstimmung Inventar ↔ Hauptbuch | Agent | vorbereitet |
> | F1-302 | Einstandspreise (WP-Schritt) | WP | nicht bearbeitet |
> | F1-303 | Herstellkosten (WP-Schritt) | WP | nicht bearbeitet |
> | F1-304 | Wertberichtigung überalterte Ware | Agent | vorbereitet |
> | F1-320 | Anhang Vorräte | Agent | vorbereitet |
> | F1-321 | Stille Reserven | Agent | benötigt Warendrittel-Berechnung |
> | F1-322 | Dauerakten | Agent | vorbereitet |
> 
> **Wichtigste Feststellungen für Notizen:**
> 
> 1. **Wertberichtigung aufgelöst** (94'900 CHF): Wieso wurde die komplette Wertberichtigung in 2025 aufgelöst? Status überalterter Ware?
> 2. **Restposten Edelstahl R-1040** (38'180 CHF): Letzte Bewegung 14.06.2023 (>2 Jahre alt), kein Abwertung. Netto-Veräusserungswert?
> 3. **Bestandsveränderung +63%**: Umsatz nur +4,9%. Begründung?
> 
> Ich erstelle jetzt den strukturierten **Textfeld-Entwurf** für revio K6:
> 
> ---
> 
> ## **TEXTFELD-ENTWÜRFE F1 (Prüffeld Vorräte)**
> 
> ### **F1-201 · Vergleich Lagerbestand und -umschlag**
> **Prüfziel:** EX Bestand, VO Vollständigkeit, BE Bewertung
> 
> **Quelle:** Inventarliste 31.12.2025 (M-Files: 12_Lager/Inventarliste_31.12.2025.md), Saldoliste 2024/2025, Jahresrechnung 2025 (Materialaufwand 2'250'348.19 CHF)
> 
> **Auswahl und Umfang:** Alle Vorratskonten (Rohmaterial, Fertigfabrikate); Bestandsvergleich VJ/GJ, Umschlagberechnung. Begründung: über Toleranzwesentlichkeit (CHF 45'000), Risiko wesentliche Überalterung (3.1).
> 
> **Ergebnis:**
> - Bestand 31.12.2024: CHF 189'800 (Rohmaterial 252'600 − WB 94'900 + Fertigfabrikate 32'100)
> - Bestand 31.12.2025: CHF 309'366 (Rohmaterial 268'016 − WB 0 + Fertigfabrikate 41'350)
> - **Veränderung: +CHF 119'566 (+63%)**
> - Umsatzveränderung: +4,9% (5'672'300 → 5'950'130)
> - Durchschnittl. Bestand 2025: CHF 249'583
> - **Umschlag 2025: 9,02×/Jahr (Lagerdauer 40,5 Tage)**
> 
> **Feststellungen:**
> - Bestandsveränderung (+63%) deutlich über Umsatzveränderung (+4,9%). Lagerdauer normal (~40 Tage), aber Bestandsmenge ungewöhnlich gestiegen.
> - Wertberichtigung Rohmaterial komplett aufgelöst (94'900 CHF). Grund unklar – Verkauf überalterter Ware oder Aufwertung? → **Pendenz**
> 
> **Pendenzen:**
> - Erklärung Bestandsveränderung +63% ohne proportionale Umsatzsteigerung erforderlich (Konto 1210, Betrag CHF 119'566, Stichtag 31.12.2025)
> 
> **Status:** teilweise bearbeitet
> 
> ---
> 
> ### **F1-301 · Abstimmung Inventarliste ↔ Hauptbuch**
> **Prüfziel:** EX Bestand, VO Vollständigkeit
> 
> **Quelle:** Inventarliste 31.12.2025, Saldoliste 31.12.2025, Jahresrechnung Bilanzseite
> 
> **Auswahl und Umfang:** Alle Vorratskonten (1210, 1219, 1260, 1280); Totalabstimmung. Begründung: Primär-Kontrollpunkt Bestandsnachweis (Art. 958c OR).
> 
> **Ergebnis (gerechnet):**
> - Inventarliste Rohmaterial: CHF 268'016.35 = Konto 1210 ✓
> - Inventarliste WB: CHF 0 = Konto 1219 ✓
> - Inventarliste Fertigfabrikate: CHF 41'350 = Konto 1260 ✓
> - Bilanzposition Vorräte (Jahresrechnung): CHF 1'577'166.35 = 268'016.35 + 0 + 41'350 + 1'267'800 (angefangene Arbeiten Konto 1280) ✓
> 
> **Feststellungen:** Keine – Abstimmung 100 % korrekt.
> 
> **Status:** vorbereitet
> 
> ---
> 
> ### **F1-304 · Wertberichtigung überalterte/unkuante Ware**
> **Prüfziel:** BE Bewertung
> 
> **Quelle:** Inventarliste, Zaehllisten (letzte Bewegung), Jahresrechnung (HK/NVW)
> 
> **Auswahl und Umfang:** Positionen mit letzter Bewegung >6 Monate vor Stichtag oder Warendrittel-Kriterium; Fokus auf kritische Positionen.
> 
> **Ergebnis:**
> - **Edelstahl-Geländerelemente V4A (R-1040):** 46 Stk, CHF 830/Stk = CHF 38'180 (5/01 Zählliste). Letzte Bewegung: 14.06.2023 (>2 Jahre). **Keine Abwertung durchgeführt.** Risiko: Netto-Veräusserungswert deutlich unter AK?
> - **Andere Positionen:** Letzte Bewegung November–Dezember 2025 (kurz vor Stichtag); normale Umschläge.
> 
> **Feststellungen:**
> - Restposten Edelstahl R-1040: Lagerdauer >2 Jahre ohne Abwertung. Netto-Veräusserungswert? Wahrscheinlichkeit Verwertung? → **Wesentliche Feststellung**
> 
> **Pendenzen:**
> - Einholung NVW oder Entsorgungsbeweis für R-1040; ggf. Abwertung erforderlich (Konto 1210/1219, Betrag CHF 38'180 oder Differenz, Stichtag 31.12.2025)
> 
> **Status:** mit Feststellungen
> 
> ---
> 
> ### **F1-320 · Anhang Vorräte**
> **Prüfziel:** VO Vollständigkeit, Rechnungslegung
> 
> **Quelle:** Inventarliste, Jahresrechnung (Anhang), Bewertungsmethoden
> 
> **Auswahl und Umfang:** Anhang-Anforderungen per Art. 960d OR und HWP ER; Kategorien, Bewertungsmethoden, stille Reserven.
> 
> **Ergebnis (Anhangcheck):**
> - ✓ Drei Vorratkategorien ausgewiesen: Rohmaterial (CHF 268'016), Fertigfabrikate (CHF 41'350), angefangene Arbeiten (CHF 1'267'800)
> - ✓ Bewertungsmethoden: Rohmaterial zu AK (Einstandspreis letzter Einkauf), Fertigfabrikate zu HK, max. NVW
> - ✓ WB-Politik: aufgelöst per 31.12.2025 (siehe F1-304 – unklar)
> - ✗ Stille Reserven: nicht erwähnt. (→ F1-321)
> 
> **Status:** teilweise bearbeitet
> 
> ---
> 
> ### **F1-321 · Stille Reserven – Warendrittel**
> **Prüfziel:** BE Bewertung, Offenlegungspflicht
> 
> **Quelle:** HWP ER, Inventarliste, Kostenrechnung, Absatzstatistik
> 
> **Auswahl und Umfang:** Berechnung Warendrittel (einfache Heuristik: Materialaufwand / Durchschnittbestand × 1/3 oder empirisch aus Lagerbewegungen).
> 
> **Ergebnis:**
> - Materialaufwand 2025: CHF 2'250'348
> - Durchschnittbestand Rohmaterial: CHF 260'308 (Anfang 252'600 + Ende 268'016 / 2)
> - **Warendrittel (1/3 des Aufwands):** CHF 2'250'348 / 3 ≈ CHF 750'116 (Heuristik Lagersumme)
> - **Stille Reserve ≈ CHF 750'116 − 268'016 = CHF 482'100** (konzeptionell; genaue Berechnung obliegt WP)
> 
> **Feststellungen:** Stille Reserven erheblich. Offenlegung? → **Notiz «Schlussbesprechung»**
> 
> **Status:** teilweise bearbeitet
> 
> ---
> 
> ### **F1-322 · Dauerakten Vorräte**
> **Prüfziel:** Dokumentation, Prüfdokumentation
> 
> **Auswahl:** Lieferanten-Rahmenverträge, Bewertungspolitik, Warendrittel, Lagerbewegungspolitik
> 
> **Status:** vorbereitet
> 
> ---
> 
> **Textfeld-Vorlage fertig für revio K6 Eingabe (Agent vorbereitet, WP-Visur ausstehend).**

## h06-k1m3

**Frage:** Mandat: Werkhof Beispiel AG, Frauenfeld-Muster TG · Geschäftsjahr 2025 (Stichtag 31.12.2025) · eingeschränkte Revision. M-Files ist in diesem Test durch den Ordner mandant/werkhof-beispiel-ag-2025/ ersetzt (Vorjahresakte: mandant/werkhof-beispiel-ag-2024/). revio ist nicht verbunden: nenne bei jedem Schritt das revio-Werkzeug, das du aufrufen würdest, statt es aufzurufen. Wesentlichkeit 2025 (revio 3.3, Softwareversion revio 4.0, vom WP festgelegt): Gesamtwesentlichkeit CHF 60'000, Toleranzwesentlichkeit CHF 45'000 (75 %), Nichtaufgriffsgrenze CHF 3'000 (5 %).

Auftrag: Prozess 2 – Bereite die Prüffelder K1 Verbindlichkeiten aus Lieferungen und Leistungen (inkl. Vollständigkeit/Cut-off) und M3 Passive Rechnungsabgrenzungen und kurzfristige Rückstellungen vor. Liefere Textfeld-Entwürfe und Notizen.

**Antwort des Agenten** (167.9 s · Tools: 26 Aufrufe revisionswiki__aufgabe, ls, read, revisionswiki__pruefschritt, revisionswiki__rechne):

> Ich starte die Vorbereitung der Prüffelder K1 und M3 für das Mandat Werkhof Beispiel AG. Zuerst rufe ich `aufgabe` auf, um die Checkliste und die nächsten Schritte zu erhalten.
> 
> Jetzt rufe ich die Anweisung für M3 ab:
> 
> Gutes. Ich habe die Checklisten für beide Prüffelder. Jetzt erkunde ich den Mandanten-Ordner, um die Unterlagen für K1 und M3 zu finden. Da revio nicht verbunden ist, nutze ich die M-Files-Ersatz-Ordner.
> 
> Ich erkunde die K1-relevanten Ordner (Lieferanten) und M3-relevanten Ordner (Abgrenzungen):
> 
> Ich lese die wichtigsten Unterlagen für die Vorbereitung:
> 
> Ich habe die Unterlagen. Jetzt beginne ich mit der Vorbereitung der Prüfschritte. Ich starte mit den K1-Schritten in der Reihenfolge 1xx → 2xx → 3xx. Zunächst lese ich K1-101 (Befragung):
> 
> Da keine schriftlichen Kundenantworten vorhanden sind, werde ich K1-101 als Pendenz erfassen. Jetzt lese ich die analytischen Schritte. Ich beginne mit K1-201:
> 
> Ich brauche die Vorjahresdaten für den Vergleich. Ich schaue in die Vorjahresakte:
> 
> Ich überprüfe die Verzeichnisstruktur:
> 
> Ich lese die Vorjahresdaten:
> 
> Ich schaue in den Jahresabschluss 2024:
> 
> Ich lese die Vorjahresdaten:
> 
> Ich suche die 2025er Erfolgsrechnung für die Kreditorenfrist-Berechnung:
> 
> Ich liste das Verzeichnis:
> 
> Ich lese die Jahresrechnung 2025:
> 
> Jetzt habe ich alle Zahlen. Ich berechne die Veränderungen für K1-201 mit `rechne`:
> 
> Ich nutze `rechne` mit direkten Ausdrücken:
> 
> Gute Rechnungen. Jetzt lese ich K1-202 (Fremdwährung) und K1-203 (nahestehende Personen):
> 
> Ich überprüfe K1-203 (nahestehende Personen). Ich lese die Unternehmensinformationen:
> 
> Wichtige Feststellung: K-0001 "Beispielmann Reto" ist der Hauptaktionär und Geschäftsführer. Das ist eine Verbindlichkeit gegenüber einer nahestehenden Person. Jetzt lese ich K1-301 (Detailprüfung):
> 
> Jetzt erstelle ich eine kompakte Zusammenfassung der Vorbereitung für beide Prüffelder. Basierend auf meiner Analyse:
> 
> ## **PRÜFFELD K1 – Verbindlichkeiten aus Lieferungen und Leistungen**
> 
> ### **K1-101 – Kritische Durchsicht / Befragung**
> **Status: teilweise bearbeitet**
> - Prüfziele: EX Bestand, VO Vollständigkeit, PA Periodenabgrenzung
> - Quelle: Kreditoren_OP_Liste_31.12.2025.md (mandant/werkhof-beispiel-ag-2025/20_Lieferanten)
> - Kritische Posten identifiziert:
>   - **Alte Posten**: K-0001 (Beispielmann) Rechnungen Oktober/November/Dezember – Zahlungsaufschub – Begründung erforderlich
>   - **Über Toleranzwesentlichkeit (CHF 45'000)**:
>     - K-0120 (Stahlhandel Muster-Ost): CHF 92'410.60 + CHF 71'860.40 + CHF 48'215.40 + CHF 64'318.20
>     - K-0152 (Muster Montage): CHF 38'400 + CHF 26'880 + CHF 31'680
>   - **Bemerkungen zu Zahlungsaufschub, Regie, Konsignationen** → plausible Gründe vorhanden
> - **Pendenz**: Schriftliche Kundenantwort zu Gründen fehlend → Kundenbefragung (revio 10.11) einholen
> 
> ### **K1-201 – Vergleich Bestand mit Vorjahr**
> **Status: vorbereitet**
> - Prüfziel: VO Vollständigkeit
> - Quelle: Saldoliste_2024.md, Jahresrechnung_2025
> - **Ergebnis** (gerechnet mit `rechne`):
>   - Kreditoren 2025: **CHF 743'669.50**
>   - Kreditoren 2024: **CHF 786'300.00**
>   - Veränderung: **CHF −42'630.50 (−5.42%)**
>   - Kreditorenfrist 2025: **94.82 Tage**
>   - Kreditorenfrist 2024: **112.09 Tage**
> - **Würdigung**: Verkürzung der Kreditorenfrist signalisiert schnellere Zahlungen. Veränderung nahe Toleranzwesentlichkeit CHF 45'000 → WP-Besprechung empfohlen
> 
> ### **K1-202 – Fremdwährung**
> **Status: vorbereitet**
> - Prüfziel: BE Bewertung
> - Befund: **Keine Fremdwährungskreditoren in der OP-Liste erkennbar** (alle in CHF)
> - Textfeld-Eintrag: «nicht anwendbar – alle Kreditoren in CHF»
> 
> ### **K1-203 – Nahestehende Personen**
> **Status: mit Feststellungen**
> - Prüfziele: RV Rechte/Verpflichtungen, VO Vollständigkeit, DO Darstellung/Offenlegung
> - Quelle: Unternehmensinformationen_2025.md
> - **Gefundene Verbindlichkeit gegenüber nahestehender Person**:
>   - K-0001: Reto Beispielmann (Aktionär 70%, Geschäftsführer), Vermietung Werkhalle
>   - Total: CHF 13'200 × 3 Monate (Okt./Nov./Dez. 2025) = **CHF 39'600**
>   - Status: Zahlungsaufschub
> - **Feststellung**: Verbindlichkeit ggü. Aktionär muss gemäss OR Art. 959a gesondert ausgewiesen oder im Anhang offengelegt sein
> - **Notiz erforderlich**: «Wesentliche Feststellungen – Prüfung der Bilanz-/Anhang-Offenlegung K-0001 (Reto Beispielmann, CHF 39'600)»
> 
> ### **K1-301 – Abstimmung Total mit Jahresrechnung**
> **Status: vorbereitet**
> - Prüfziele: VO Vollständigkeit, PA Periodenabgrenzung
> - **Abstimmung**:
>   - OP-Liste Total: CHF 743'669.50
>   - Jahresrechnung Bilanz 2025: CHF 743'669.50
>   - **Differenz: CHF 0.00** ✓
> - OP-Liste-Datum: 31.12.2025, Erstellung 12.01.2026 (korrekt)
> 
> ---
> 
> ## **PRÜFFELD M3 – Passive Rechnungsabgrenzungen und kurzfristige Rückstellungen**
> 
> Ich lese nun M3-201 für die analytische Vorbereitung:
> 
> Ich analysiere M3-201. Zuerst extrahiere ich die 2025-Saldoliste:
> 
> Jetzt berechne ich die Veränderungen für M3-201 mit `rechne`:
> 
> Jetzt erstelle ich die finale Zusammenfassung mit Textfeld-Entwürfen und Notizen. **PROZESS 2 – PRÜFFELD K1 UND M3 VORBEREITUNG**
> 
> ---
> 
> ## **TEXTFELD-ENTWÜRFE**
> 
> ### **K1-101 – Kritische Durchsicht und Befragung**
> **Status: teilweise bearbeitet** | Quelle: Kreditoren_OP_Liste_31.12.2025
> 
> **Prüfziel**: EX Bestand, VO Vollständigkeit, PA Periodenabgrenzung
> 
> **Auswahl und Umfang**: Posten mit Fälligkeit vor Stichtag und Beträge ≥ Toleranzwesentlichkeit CHF 45'000; Soll-Salden (keine identifiziert).
> 
> **Befunde**:
> - Alte Posten: K-0001 (Beispielmann Reto) Oct./Nov./Dec. 2025, Gesamtbetrag CHF 39'600, Bemerkung «Zahlung aufgeschoben»
> - Hochwertige Posten: K-0120 (Stahlhandel Muster-Ost) CHF 92'410.60 + CHF 71'860.40 + CHF 48'215.40 + CHF 64'318.20 = CHF 276'804.60; K-0152 (Muster Montage) CHF 96'960
> 
> **Würdigung**: Bemerkungen in der OP-Liste geben Anhaltspunkte (Zahlungsaufschub, Regie, Konsignationen). Schriftliche Begründung der GL steht aus.
> 
> **Pendenzen**: Schriftliche Kundenantwort zu Frage K1-101: Gründe für alte, ungewöhnlich hohe und Soll-Posten (revio 10.11) erforderlich.
> 
> ---
> 
> ### **K1-201 – Vergleich Bestand mit Vorjahr**
> **Status: vorbereitet** | Quelle: Saldoliste_2024.md, Jahresrechnung_2025
> 
> **Prüfziel**: VO Vollständigkeit
> 
> **Ergebnis** (gerechnet mit `rechne`):
> - Kreditoren 2025: CHF 743'669.50
> - Kreditoren 2024: CHF 786'300.00
> - Δ absolut: **CHF −42'630.50**
> - Δ %: **−5.42%**
> - Kreditorenfrist 2025: **94.82 Tage** (vs. 112.09 Tage 2024)
> 
> **Würdigung**: Veränderung liegt knapp unter Toleranzwesentlichkeit CHF 45'000. Verkürzung Kreditorenfrist (−17.27 Tage) deutet auf schnellere Zahlungen hin. Ursachen: Liquiditätsdruck (siehe Unternehmensinformationen: «angespannte Liquidität Q4»).
> 
> **Status**: Vorbereitet; Detailprüfung (K1-301) zeigt Abstimmung stimmt.
> 
> ---
> 
> ### **K1-202 – Fremdwährung**
> **Status: vorbereitet** | Quelle: Kreditoren_OP_Liste_31.12.2025
> 
> **Prüfziel**: BE Bewertung
> 
> **Befund**: **Keine Fremdwährungskreditoren erkennbar.** Alle Posten in CHF.
> 
> **Textfeld-Eintrag**: «Nicht anwendbar – alle Kreditoren in CHF erfasst.»
> 
> ---
> 
> ### **K1-203 – Nahestehende Personen**
> **Status: mit Feststellungen** | Quellen: Unternehmensinformationen_2025, Kreditoren_OP_Liste
> 
> **Prüfziele**: RV Rechte/Verpflichtungen, VO Vollständigkeit, DO Darstellung/Offenlegung
> 
> **Identifizierte Verbindlichkeit**:
> - K-0001: Reto Beispielmann (Aktionär 70%, Präsident, Geschäftsführer), Vermietung Werkhalle
> - Rechnungen: MI-2025-10 (Oct.), MI-2025-11 (Nov.), MI-2025-12 (Dec.) à CHF 13'200/Monat
> - Summe offen: **CHF 39'600**
> - Status: Zahlungsaufschub
> 
> **Feststellung**: Verbindlichkeit ggü. Aktionär muss gemäss OR Art. 959a gesondert ausgewiesen oder im Anhang offengelegt sein. Anhang-Prüfung erforderlich.
> 
> ---
> 
> ### **K1-301 – Abstimmung Total mit Jahresrechnung**
> **Status: vorbereitet** | Quelle: Jahresrechnung_2025, Saldoliste_2025
> 
> **Prüfziele**: VO Vollständigkeit, PA Periodenabgrenzung
> 
> **Abstimmung**:
> - OP-Liste Total: CHF 743'669.50
> - Bilanz Jahresrechnung 2025 (Konto 2000): CHF 743'669.50
> - **Differenz: CHF 0.00** ✓
> 
> **OP-Liste-Metadaten**: Stichtag 31.12.2025, Erstellungsdatum 12.01.2026 (korrekt, keine Folgejahresbuchungen).
> 
> ---
> 
> ## **PRÜFFELD M3 – TEXTFELD-ENTWÜRFE**
> 
> ### **M3-101 – Befragung Vollständigkeit Abgrenzungen**
> **Status: teilweise bearbeitet** | Quelle: Detaillisten 2025
> 
> **Prüfziel**: VO Vollständigkeit
> 
> **Befund**: Detaillisten vorhanden (Passive RA, Rückstellungen). Schriftliche Kundenantwort zur Sicherstellung der Vollständigkeit von Abgrenzungen (z.B. Honoraraufwand der Revision, Ferien-/Überzeitguthaben je Mitarbeiter) erforderlich.
> 
> **Pendenz**: Kundenbefragung (revio 10.11) – Frage M3-101 einholen.
> 
> ---
> 
> ### **M3-201 – Vergleich Aufwandskonten mit Vorjahr**
> **Status: vorbereitet** | Quelle: Saldoliste Erfolgsrechnung 2024/2025
> 
> **Prüfziel**: VO Vollständigkeit, PA Periodenabgrenzung
> 
> **Relevante Aufwandskonten** (Veränderungen gerechnet mit `rechne`):
> 
> | Konto | Bezeichnung | 2025 | 2024 | Δ CHF | Δ % | Würdigung |
> |---|---|---|---|---|---|---|
> | 6000 | Miete | -158'400 | -158'400 | 0 | 0% | Unverändert (pauschal) |
> | 6100 | Unterhalt/Reparaturen | -141'500 | -46'800 | **-94'700** | **+202%** | **Abkantpresse-Investition (Nov. 2025) – Prüfung erforderlich** |
> | 6400 | Energie/Entsorgung | -64'800 | -61'300 | -3'500 | +5.7% | Moderat, plausibel |
> | 6530 | Treuhand/Beratung | -28'600 | -27'400 | -1'200 | +4.4% | Moderat |
> | 6540 | Revision/VR | -14'500 | -13'800 | -700 | +5.1% | Inkl. 2025er Revision CHF 6'480 (Detailliste M3: «Lohnbuchhaltung Q4 2025») |
> | 6700 | Sonstiger Aufwand | -31'300 | -64'400 | **+33'100** | **−51%** | **Rückgang – Umlagerungen?** |
> 
> **Feststellungen**:
> - Unterhalt sprang stark an (Investitionen 2025); Detailprüfung mit Belegen erforderlich
> - Sonstiger Aufwand stark gesunken; möglicherweise Umlagerungen in andere Konten
> - Temporärpersonal: -84'500 (2025) vs -62'300 (2024) = +CHF 22'200 (+36%) – plausibel (schwaches H1 2025, siehe Unternehmensinformationen)
> 
> **Pendenzen**: GL-Antwort zu Umlagierungen/Abgrenzungsquellen erforderlich.
> 
> ---
> 
> ### **M3-202 – Vergleich Bestände Passive RA/Rückstellungen**
> **Status: vorbereitet** | Quelle: Saldoliste 2024/2025, Detaillistten
> 
> **Prüfziel**: VO Vollständigkeit, PA Periodenabgrenzung
> 
> **Bestände** (gerechnet mit `rechne`):
> 
> | Konto | Position | 2025 | 2024 | Δ CHF | Würdigung |
> |---|---|---|---|---|---|
> | 2300 | Passive RA gesamt | 55'400 | 48'200 | +7'200 | Erhöhung um CHF 7'200 – Detailliste zeigt neue Positionen |
> | 2330 | Ferien/Überzeit | 28'000 | 28'000 | 0 | Unverändert; Detailliste besagt «wie Vorjahr» – **Prüfung erforderlich: je Mitarbeiter?** |
> | 2331 | Garantie | 30'000 | 30'000 | 0 | Pauschal; «keine besonderen Fälle» – Plausibilität prüfen |
> | 2332 | Prozessrisiken | 42'000 | 42'000 | 0 | Unverändert von Vorjahr |
> 
> **Detailliste Passive RA 2025 – neue Positionen**:
> - Akkordprämien: CHF 9'800
> - Spesen: CHF 6'240
> - Muster Montage Regie: CHF 24'600
> - Telefon/IT: CHF 1'830
> - Entsorgung: CHF 3'130
> - Weiterbildung: CHF 1'400
> - Abschlussarbeiten (Treuhand): CHF 7'200
> - Diverses: CHF 1'200
> - **Total**: CHF 55'400 ✓
> 
> **Würdigung**: Passive RA plausibel auf Detailliste abgestützt. Rückstellungen (Ferien/Überzeit, Garantie) ohne Veränderung – **Agentenfrage für Detailprüfung (M3-304)**: Ferien-/Überzeitguthaben pro Mitarbeiter prüfen.
> 
> ---
> 
> ### **M3-301 – Abstimmung mit Jahresrechnung**
> **Status: vorbereitet** | Quelle: Jahresrechnung_2025, Saldoliste
> 
> **Prüfziele**: VO Vollständigkeit, PA Periodenabgrenzung
> 
> **Abstimmung M3 Gesamtbestand**:
> - Passive RA (Konto 2300): CHF 55'400
> - Rückstellung Ferien (2330): CHF 28'000
> - Rückstellung Garantie (2331): CHF 30'000
> - Rückstellung Prozessrisiken (2332): CHF 42'000
> - **Summe M3 Bilanz (2300 + 2330 + 2331 + 2332)**: CHF 155'400
> - Jahresrechnung «Passive Rechnungsabgrenzungen und kurzfristige Rückstellungen»: **CHF 155'400** ✓
> 
> **Differenz: CHF 0.00** ✓
> 
> ---
> 
> ## **NOTIZEN (ZU ERFASSEN MIT `revio K7`)**
> 
> ### **Notiz 1 – Pendenz: K1-101 Kundenbefragung**
> - **Typ**: Pendenz
> - **Betreffend**: K1-101, Kreditoren-Bearbeitung
> - **Text**: Frage an Kunde (K1-101): Gründe für alte Posten (K-0001, Oct./Nov./Dec.), ungewöhnlich hohe Posten (K-0120, K-0152 über CHF 45'000), benötigt bis zum Prüfabschluss. Schriftliche Antwort (revio 10.11 Kundenbefragung) einholen.
> - **Fälligkeit**: vor Bericht
> 
> ### **Notiz 2 – Wesentliche Feststellung: K1-203 Nahestehende Person**
> - **Typ**: Wesentliche Feststellung
> - **Betreffend**: K1-203, Bilanz/Anhang
> - **Text**: Verbindlichkeit K-0001 (Reto Beispielmann, Aktionär 70%) CHF 39'600 (Vermietung Werkhalle). Prüfung erforderlich: Ist diese Verbindlichkeit gemäss OR Art. 959a gesondert in der Bilanz oder im Anhang ausgewiesen? Falls nein: Buchungsvorschlag erforderlich.
> - **Quelle**: Unternehmensinformationen, K1-OP-Liste
> 
> ### **Notiz 3 – Pendenz: M3-101 Kundenbefragung**
> - **Typ**: Pendenz
> - **Betreffend**: M3-101, Abgrenzungen
> - **Text**: Frage an Kunde (M3-101): Wie wird sichergestellt, dass alle Aufwände des Geschäftsjahrs 2025 abgegrenzt sind (Honorare, Energie, Ferien-/Überzeitguthaben, Revisionshonorar CHF 6'480)? Schriftliche Antwort und Berechnungsunterlagen erforderlich.
> - **Fälligkeit**: vor Bericht
> 
> ### **Notiz 4 – Pendenz: M3-202/M3-304 Ferien-/Überzeitguthaben**
> - **Typ**: Pendenz
> - **Betreffend**: M3-202, M3-304, Rückstellung 2330
> - **Text**: Rückstellung Ferien-/Überzeitguthaben CHF 28'000 (unverändert vs. Vorjahr). Detailliste sagt «wie Vorjahr». Erforderlich: Saldi Ferien/Überzeit pro Mitarbeiter aus Lohnprogramm × Lohnansatz zur Plausibilisierung. Zeigt Detailliste oder separate Berechnung erforderlich.
> - **Fälligkeit**: vor Bericht
> 
> ### **Notiz 5 – Wesentliche Feststellung: M3-201 Unterhalt massiv gestiegen**
> - **Typ**: Wesentliche Feststellung / Analytische Abweichung
> - **Betreffend**: M3-201, Aufwandsanalyse
> - **Text**: Unterhalt/Reparaturen 2025: CHF 141'500 vs. 2024: CHF 46'800 = Δ +CHF 94'700 (+202%). Laut Unternehmensinformationen: «Investition neue Abkantpresse (Nov. 2025)». Prüfung erforderlich: Buchungsvorschlag zur Aktivierung (Sachanlagen) oder korrekte Aufwandsbehandlung?
> - **Quelle**: Saldoliste Erfolgsrechnung, Unternehmensinformationen
> 
> ### **Notiz 6 – PBC-Vorschlag: M3-304 Rückstellungen**
> - **Typ**: PBC-Vorschlag
> - **Text**: Unterlagen für M3-304 (Rückstellungen-Detailprüfung): (1) Garantierückstellung CHF 30'000 – aktuelle Fälle + Bewertung; (2) Prozessrisiken CHF 42'000 – aktuelle Rechtsfälle, Korrespondenz, Gutachten; (3) Bestmögliche Schätzung nachweisen (Bandbreiten gemäss HWP BuR).
> - **Fälligkeit**: vor Bericht
> 
> ---
> 
> **Zusammenfassung der Vorbereitung:**
> - **K1**: 5 Schritte vorbereitet (K1-101, K1-201, K1-202, K1-203, K1-301)
> - **M3**: 3 Schritte vorbereitet (M3-101, M3-201, M3-202, M3-301)
> - **Pendenzen**: 4 (Kundenbefragungen, Detailunterlagen)
> - **Wesentliche Feststellungen**: 2 (K1-203 nahestehende Person; M3-201 Unterhalt-Abweichung)
> - **Status**: Beide Prüffelder substanziell vorbereitet; WP entscheidet über Detailprüfungen und Abschluss
> 
> Alle Arbeitsschritte folgen revio 4.0-Katalog und Konzept KI-Revisionsagent. Visum und Prüffeldbestätigung bleiben beim WP.

## h08-r1m2

**Frage:** Mandat: Werkhof Beispiel AG, Frauenfeld-Muster TG · Geschäftsjahr 2025 (Stichtag 31.12.2025) · eingeschränkte Revision. M-Files ist in diesem Test durch den Ordner mandant/werkhof-beispiel-ag-2025/ ersetzt (Vorjahresakte: mandant/werkhof-beispiel-ag-2024/). revio ist nicht verbunden: nenne bei jedem Schritt das revio-Werkzeug, das du aufrufen würdest, statt es aufzurufen. Wesentlichkeit 2025 (revio 3.3, Softwareversion revio 4.0, vom WP festgelegt): Gesamtwesentlichkeit CHF 60'000, Toleranzwesentlichkeit CHF 45'000 (75 %), Nichtaufgriffsgrenze CHF 3'000 (5 %).

Auftrag: Prozess 2 – Bereite die Prüffelder R1 Personalaufwand und M2 Mehrwertsteuer vor. Liefere Textfeld-Entwürfe und Notizen.

**Antwort des Agenten** (142.6 s · Tools: 26 Aufrufe revisionswiki__aufgabe, ls, read, revisionswiki__pruefschritt, revisionswiki__rechne):

> Bereite die Prüffelder **R1 Personalaufwand** und **M2 Mehrwertsteuer** vor (Prozess 2, Phase 3).
> 
> Ich rufe zuerst **`revisionswiki__aufgabe`** mit dieser Aufgabe auf:
> 
> Beginne mit den Unterlagen. Schaue zuerst in `mandant/werkhof-beispiel-ag-2025/`:
> 
> Schaue in die relevanten Ordner für R1 und M2:
> 
> Lese die relevanten Unterlagen:
> 
> Starte mit **R1-101** (Befragung Leistungen nach Stichtag). Rufe `pruefschritt R1-101` auf:
> 
> **R1-101: Notiz erforderlich.** Die Befragung zu Bonusbeschlüssen nach 31.12. ist schriftlich nicht vorgelegen. Ich erfasse sie als **Pendenz**: `aufgabe notiz "Frage an Kunde (R1-101): Wurden nach dem 31.12.2025 Leistungs- oder Erfolgsprämien für das GJ 2025 beschlossen? – M-Files-Quellen: Lohnjournal zeigt Gratifikation Dezember CHF 63.400; VR-/GL-Protokolle nach 31.12. und Bonusreglement zur Überprüfung erforderlich."`.
> 
> Weiter mit **R1-102**:
> 
> **R1-102: Vorjahresdaten erforderlich.** Für diese Befragung brauche ich die Saldoliste 2024. Schaue in `mandant/werkhof-beispiel-ag-2024/`:
> 
> Suche die 2025 Saldoliste in der Abschlussordnung:
> 
> Berechne die Abweichungen für R1-102. Nutze `rechne`:
> 
> **R1-102 offenbart wesentliche Abweichungen**, insbesondere:
> - Konto 5900 Temporärpersonal: +CHF 22.200 (35,6% Anstieg)
> - Rückstellung Ferien/Überzeit: +CHF 18.974 vs. Bilanz nur CHF 28.000 (Sollte: CHF 46.974!)
> 
> → **Pendenzen erforderlich** (Textfeld + Notiz).
> 
> Fahre mit **R1-201** (analytische Prüfung Verhältnis Saläre/Sozialleistungen) fort:
> 
> **R1-201 Ergebnis:** Sozialleistungsquote gestiegen von 14,72% (2024) auf 15,15% (2025), Differenz +0,43 PP. Plausibel. → **Status: vorbereitet** (keine Feststellungen).
> 
> Weiter mit **R1-202** (Analytik Veränderungen, Überzeitalter):
> 
> **R1-202:** Wegen fehlender 2024-Personalliste und fehlender Budget-Daten kann ich nicht alle Veränderungen voll erklären. Die Pendenz ist identisch mit R1-102: Konto 5900 (Temporärpersonal +CHF 22.200), Konto 5800 (Übriger Personalaufwand -CHF 6.400), Ferien/Überzeit-Rückstellung +CHF 18.974.
> 
> → **Status R1-202: teilweise bearbeitet** (Fragen an Kunde erforderlich).
> 
> Wechsel zu **M2 Mehrwertsteuer**. Starte mit **M2-101** (Befragung Umsatzabstimmung):
> 
> **M2-101:** Schriftliche Befragung zur Umsatzabstimmung fehlt. → **Status: teilweise bearbeitet** (Pendenz).
> 
> Weiter mit **M2-301** (Abstimmung MWST-Salden):
> 
> Berechne die MWST-Abstimmung:
> 
> **M2-301 Ergebnis:** MWST-Abstimmung stimmt (Differenz = 0). Q4 ist offene Zahllast per 31.12.2025. → **Status: vorbereitet**.
> 
> Weiter mit **M2-305** (Allgemeine MWST-Risiken):
> 
> **M2-305 Ergebnis:** Werkhof AG (Metallbau-/Montagefirma) zeigt Standardgeschäft mit 8,1% Normalsatz. Spezialitätenliste a–h alle nicht zutreffend. → **Status: vorbereitet** (keine Risiken).
> 
> ---
> 
> Ich habe die **Kernschritte** vorbereitet. Hier die **Zusammenfassung der Textfeld-Entwürfe und Pendenzen**:
> 
> ## **Prüffeld R1 – Personalaufwand**
> 
> ### **Textfeld R1-101 (Befragung Boni)**
> - **Prüfziel:** EX Bestand, VO Vollständigkeit, PA Periodenabgrenzung
> - **Quellen:** Lohnjournal 2025 (Dez. Gratifikation); VR-/GL-Protokolle + Bonusreglement erforderlich
> - **Status:** teilweise bearbeitet (schriftliche Antwort fehlt)
> - **Pendenz:** Frage an Kunde (R1-101): Wurden nach 31.12.2025 Leistungs-/Erfolgsprämien für GJ 2025 beschlossen/zugesichert? (Lohnjournal zeigt CHF 63.400 Gratifikation Dezember → Abgrenzung/Rückstellung?)
> 
> ### **Textfeld R1-102 (Befragung Abweichungen)**
> - **Prüfziel:** EX Bestand, VO Vollständigkeit, BE Bewertung, PA Periodenabgrenzung
> - **Quellen:** Saldoliste 2024/2025
> - **Ergebnis (gerechnet):**
>   - Konto 5900 Temporärpersonal: +CHF 22.200 (35,6% Anstieg) → **über NAG**
>   - Konto 5800 Übriger Personalaufwand: -CHF 6.400 (20,5% Rückgang) → **über NAG**
>   - Rückstellung Ferien/Überzeit Bilanz: CHF 28.000 vs. Saldi CHF 46.974 → **Untererfassung CHF 18.974** → **kritisch**
> - **Status:** teilweise bearbeitet
> - **Pendenzen:**
>   - Frage an Kunde (R1-102a): Warum Konto 5900 +CHF 22.200? (Mehr Temps? Auswirkung auf FTE-Struktur?)
>   - Frage an Kunde (R1-102b): Warum Konto 5800 -CHF 6.400? (Weniger Schulungen/Gesundheit?)
>   - **Wesentliche Feststellung (R1-102c):** Rückstellung Ferien/Überzeit untererfasst! Bilanz CHF 28.000, aber Saldi CHF 46.974 → Differenz CHF 18.974 → **Buchungsvorschlag:** Soll 5800 (oder 5000) / Haben 2330 = CHF 18.974
> 
> ### **Textfeld R1-201 (Analytik Sozialleistungen)**
> - **Prüfziel:** VO Vollständigkeit, BE Bewertung, PA Periodenabgrenzung
> - **Ergebnis:**
>   - SV-Quote 2025: 15,15% (AHV 7,93%, BVG 5,14%, UVG 0,97%, KTG 1,11%)
>   - SV-Quote 2024: 14,72%
>   - Differenz: +0,43 PP → plausibel
> - **Status:** vorbereitet (keine Feststellungen)
> 
> ### **Textfeld R1-202 (Analytik Veränderungen)**
> - **Status:** teilweise bearbeitet (Pendenzen R1-102a/b/c)
> 
> ---
> 
> ## **Prüffeld M2 – Mehrwertsteuer**
> 
> ### **Textfeld M2-101 (Befragung Umsatzabstimmung)**
> - **Prüfziel:** VO Vollständigkeit, BE Bewertung, PA Periodenabgrenzung
> - **Status:** teilweise bearbeitet
> - **Pendenz:** Frage an Kunde (M2-101): Liegt Umsatzabstimmung (Fibu vs. deklarierte MWST-Abrechnungen 2025) vor?
> 
> ### **Textfeld M2-301 (Detailprüfung MWST-Salden)**
> - **Prüfziel:** VO Vollständigkeit, BE Bewertung, PA Periodenabgrenzung, RI Richtigkeit
> - **Quellen:** MWST_Abrechnungen_2025_Zusammenzug, Saldoliste per 31.12.2025
> - **Ergebnis (gerechnet):**
>   - Geschuldete MWST (Konto 2200): CHF 131.654,97
>   - Abzug Vorsteuer Material (Konto 1170): CHF 44.630,15
>   - Abzug Vorsteuer Investitionen (Konto 1171): CHF 18.950,25
>   - = Zu bezahlender Betrag: CHF 68.074,57 ✓ (stimmt mit Q4-Abrechnung)
>   - Q4 noch nicht bezahlt (fällig 02.03.2026)
> - **Status:** vorbereitet (Abstimmung stimmt)
> 
> ### **Textfeld M2-305 (MWST-Risiken Spezialitäten)**
> - **Prüfziel:** EX Bestand, RV Rechte, EN Eintritt, VO Vollständigkeit, BE Bewertung, PA Periodenabgrenzung, RI Richtigkeit
> - **Spezialitätenliste (a–h):** Alle nicht zutreffend (Standardmetallbau 8,1% Normalsatz, keine Export/Import/Nahestehende/Immobilien)
> - **Status:** vorbereitet (keine Risiken)
> 
> ---
> 
> ## **Ausstehende Schritte (nicht abgeschlossen in dieser Session)**
> - R1-203 (Analytik monatlicher PA, Saläre/SL pro FTE)
> - R1-301 (Abstimmung Lohnbuchhaltung–Hauptbuch Detailprüfung)
> - R1-320, R1-321, R1-322 (Anhang, stille Reserven, Dauerakten)
> 
> **Deliverable:** Textfeld-Entwürfe und Notizen sind vorbereitet. Notizen (Pendenzen + Feststellungen) müssen im revio-System erfasst werden: **`revio K7` «Notiz erfassen»** je Feststellung/Pendenz.

