---
typ: testfall-hinweise
titel: Testakte 2025 (fiktiv) – Prüffeld SCH4 (nur für Tests, nicht ins Plugin)
jur: ch
quellen: []
status: entwurf
generiert: tools/build_quick.py, 2026-11-13
---


# SCH4 · Finanzaufwand und Finanzertrag – Testakte 2025 (fiktiv)

> **Nur für Tests, nicht ins Plugin.** Bezüge der fiktiven Testakte 2025 (Feld `testakte_2025` in data/prueffelder/). Nicht nach quick/ oder wiki/ übernehmen und nicht als Wissen des Agenten verwenden (Überanpassung an die Messung).

Quelle: data/prueffelder/sch4.yaml (Feld testakte_2025)

## Testakte 2025 (fiktiv)
- [00_Allgemein/Saldoliste_2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Saldoliste_2025.md) – Blatt «Erfolgsrechnung» Konten 6900–6970 (2025/2024): SCH4-101, SCH4-201 Vorjahresvergleich und Klassierung nach Natur; Blatt «Bilanz» verzinsliche Positionen (2100, 2170, 2400, 2450–2455) für SCH4-202 und Fremdwährungskonten (1012, 1014, 1031, 1032) für SCH4-203
- [00_Allgemein/Jahresrechnung_2025_Fiktive_Zahlen_AG_Testfassung.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Jahresrechnung_2025_Fiktive_Zahlen_AG_Testfassung.md) – ER Abschnitte «Finanzaufwand»/«Finanzertrag»: Ertragskonten 6960 Ertrag Finanzanlagen (VJ 10'200), 6970 Zinsertrag und 6944 Währungsgewinne stehen im «Total Finanzaufwand» → Verrechnungsprüfung SCH4-201 (6942/6944: Ausnahme gleiche Währung prüfen); Anhang Darlehen/Zinsverbindlichkeiten nahestehender Parteien und Rangrücktritt für SCH4-202; CHF-Rechnungslegung (keine Pflicht zur Angabe der Umrechnungskurse, SCH4-203)
- [00_Allgemein/Hauptbuch_2025_Kontoblaetter.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Hauptbuch_2025_Kontoblaetter.md) – Nur Bilanzkonten: Gegenbuchungen auf 69xx in Blatt 1010 (Zins Festvorschuss, Kommission Bankgarantien, Zins DL-2021-044), 1011/1012/1014 (Kontoführungsgebühren, Kursbewertung KB-12 auf 6942/6944 – Stichtagsbewertung Sichtguthaben, gilt als realisiert), 1013/1176 (Zinsgutschrift brutto, VSt), 2170/2170k (Zinsen Aktionärsdarlehen), 2400, 2451–2455 für SCH4-202, SCH4-203, SCH4-301, SCH4-302; Kontoblätter der Erfolgskonten 69xx fehlen (PBC)
- [00_Allgemein/Unternehmensinformationen_2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Unternehmensinformationen_2025.md) – Geschäftsmodell (Handel mit Solarkomponenten), Banken, Ansprechpersonen für Befragungen: SCH4-101, SCH4-203
- [00_Allgemein/Belegverzeichnis.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Belegverzeichnis.md) – Übersicht vorhandener Unterlagen für Belegabstimmung und PBC-Abgleich: SCH4-301
- [I_Bank_und_Aktionaersdarlehen/Darlehensvertrag_Aktionaer_A.md](../../testdaten/fiktive-zahlen-ag-2025/text/I_Bank_und_Aktionaersdarlehen/Darlehensvertrag_Aktionaer_A.md) – Betrag, Auszahlungsdatum, Zinssatz, Zinsfälligkeit: Erwartungswert Zinsaufwand SCH4-202, Belegabstimmung SCH4-301
- [I_Bank_und_Aktionaersdarlehen/Darlehensvertrag_Aktionaer_B.md](../../testdaten/fiktive-zahlen-ag-2025/text/I_Bank_und_Aktionaersdarlehen/Darlehensvertrag_Aktionaer_B.md) – Konditionen Aktionärsdarlehen B: SCH4-202, SCH4-301
- [I_Bank_und_Aktionaersdarlehen/Darlehensvertrag_Aktionaer_D.md](../../testdaten/fiktive-zahlen-ag-2025/text/I_Bank_und_Aktionaersdarlehen/Darlehensvertrag_Aktionaer_D.md) – Konditionen Aktionärsdarlehen D (Tranchen mit unterschiedlichen Auszahlungsdaten): SCH4-202, SCH4-301
- [I_Bank_und_Aktionaersdarlehen/Darlehensvertrag_Aktionaer_E.md](../../testdaten/fiktive-zahlen-ag-2025/text/I_Bank_und_Aktionaersdarlehen/Darlehensvertrag_Aktionaer_E.md) – Konditionen Aktionärsdarlehen E: SCH4-202, SCH4-301
- [I_Bank_und_Aktionaersdarlehen/Rangruecktritt_Aktionaer_A.md](../../testdaten/fiktive-zahlen-ag-2025/text/I_Bank_und_Aktionaersdarlehen/Rangruecktritt_Aktionaer_A.md) – Einschluss der Zinsen, Zinsverzicht/Stundung während Überschuldung: Erwartung Zinsaufwand SCH4-202, Ausweis Zinsverbindlichkeiten
- [I_Bank_und_Aktionaersdarlehen/Rangruecktritt_Aktionaer_B.md](../../testdaten/fiktive-zahlen-ag-2025/text/I_Bank_und_Aktionaersdarlehen/Rangruecktritt_Aktionaer_B.md) – Wie A: SCH4-202
- [I_Bank_und_Aktionaersdarlehen/Rangruecktritt_Aktionaer_D.md](../../testdaten/fiktive-zahlen-ag-2025/text/I_Bank_und_Aktionaersdarlehen/Rangruecktritt_Aktionaer_D.md) – Wie A: SCH4-202
- [A_Fluessige_Mittel/Bankbestaetigung_Fiktiva_Regionalbank_31.12.2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/A_Fluessige_Mittel/Bankbestaetigung_Fiktiva_Regionalbank_31.12.2025.md) – Vorliegende Bankbestätigung auswerten (keine eigene Einholung): Festvorschuss und Darlehen mit Zinssätzen, Garantien (Kommissionen): SCH4-202, SCH4-301
- [A_Fluessige_Mittel/Bankbestaetigung_Testbank_Ostschweiz_31.12.2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/A_Fluessige_Mittel/Bankbestaetigung_Testbank_Ostschweiz_31.12.2025.md) – Vorliegende Bankbestätigung auswerten: Zinssatz Sparkonto, Bewertungskurs EUR per 31.12.2025: SCH4-202, SCH4-203
- [A_Fluessige_Mittel/Kontoauszug_Fiktiva_1010_CHF_Dezember_2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/A_Fluessige_Mittel/Kontoauszug_Fiktiva_1010_CHF_Dezember_2025.md) – Zins- und Kommissionsbelastungen 4. Quartal: Belegabstimmung SCH4-301
- [A_Fluessige_Mittel/Kontoauszug_Testbank_1012_EUR_Dezember_2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/A_Fluessige_Mittel/Kontoauszug_Testbank_1012_EUR_Dezember_2025.md) – Devisenkurs EUR/CHF per 31.12.2025, Gebühren: SCH4-203, SCH4-301
- [A_Fluessige_Mittel/Kontoauszug_Fiktiva_1014_EUR_Dezember_2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/A_Fluessige_Mittel/Kontoauszug_Fiktiva_1014_EUR_Dezember_2025.md) – Devisenkurs EUR/CHF per 31.12.2025, Gebühren: SCH4-203, SCH4-301
- [A_Fluessige_Mittel/Kontoauszug_Testbank_1013_Reserve_2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/A_Fluessige_Mittel/Kontoauszug_Testbank_1013_Reserve_2025.md) – Zinsgutschrift und VSt Reservekonto: SCH4-202, SCH4-301
- [B_Forderungen_aus_LuL/Darlehensvertrag_Gesellschaft_an_Aktionaer_A.md](../../testdaten/fiktive-zahlen-ag-2025/text/B_Forderungen_aus_LuL/Darlehensvertrag_Gesellschaft_an_Aktionaer_A.md) – Darlehen CHF 150'000 an Aktionär A (VR-Präsident) ab 15.10.2025, Zins 1.0 % p.a. «zahlbar mit Rückzahlung», ohne Sicherheit: aufgelaufener Zinsertrag 2025 abzugrenzen (Konto 6970 = 0) und Drittvergleich (HWP ER Rz 176/177) für SCH4-202; ESTV-Abgleich nur als steuerlicher Hinweis an WP
