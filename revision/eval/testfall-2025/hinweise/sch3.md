---
typ: testfall-hinweise
titel: Testakte 2025 (fiktiv) – Prüffeld SCH3 (nur für Tests, nicht ins Plugin)
jur: ch
quellen: []
status: entwurf
generiert: tools/build_quick.py, 2026-11-13
---


# SCH3 · Übriger betrieblicher Aufwand – Testakte 2025 (fiktiv)

> **Nur für Tests, nicht ins Plugin.** Bezüge der fiktiven Testakte 2025 (Feld `testakte_2025` in data/prueffelder/). Nicht nach quick/ oder wiki/ übernehmen und nicht als Wissen des Agenten verwenden (Überanpassung an die Messung).

Quelle: data/prueffelder/sch3.yaml (Feld testakte_2025)

## Testakte 2025 (fiktiv)
- [00_Allgemein/Saldoliste_2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Saldoliste_2025.md) – Blatt Erfolgsrechnung: 46 Konten 6000–6790, Summe 2025 −827'040 / 2024 −1'360'062 (nachgerechnet = JR); grosse Sprünge u.a. 6530 −5'000 (VJ −180'000), 6565 −90'000 (VJ −300'000), 6540 −50'000 (VJ −20'000), 6310 −2'500 (VJ −16'000); 7500 Untermiete 0 (VJ 150'000) (SCH3-101, -201, -202)
- [00_Allgemein/Jahresrechnung_2025_Fiktive_Zahlen_AG_Testfassung.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Jahresrechnung_2025_Fiktive_Zahlen_AG_Testfassung.md) – Total Übriger betrieblicher Aufwand zur Abstimmung (SCH3-201); Anhang Ziff. 3: a.o. Ertrag u.a. Rabatt Lieferanten 17'763, Rückerstattungen/Gutschriften L&L 10'851, Rückerstattung Nebenkosten Büro 10'684; a.o. Aufwand «Betriebshaftpflicht – Differenzzahlung Lohn» −20'499 → Ausweis/Aufwandminderung prüfen (SCH3-202d, -303); Ziff. 7 Mietverbindlichkeiten 2'752'680 (= 8 × 344'085)
- [00_Allgemein/Hauptbuch_2025_Kontoblaetter.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Hauptbuch_2025_Kontoblaetter.md) – Keine Kontoblätter 6xxx (Pendenz, SCH3-202b/-303); Gegenkontenanalyse: 1011 am 19.12.2025 BA-1213 «Miete 01/2026» 39'129.85 direkt auf 6000 (Periodenabgrenzung, SCH3-302); 8510 KR-0930 «Rückerstattung Nebenkosten Büro (Abrechnung 2024)» 10'684 (Ausweis, SCH3-303)
- [C_Uebrige_kurzfristige_Forderungen/Mietvertrag_Gewerbehaus_Auszug.md](../../testdaten/fiktive-zahlen-ag-2025/text/C_Uebrige_kurzfristige_Forderungen/Mietvertrag_Gewerbehaus_Auszug.md) – Erwartungswert Miete 344'085 + 12 × 2'500 Nebenkosten-Akonto = 374'085 vs. Konto 6000 527'000 (Differenz 152'915 erklären lassen: Indexierung, Vorauszahlung 01/2026, Parkplätze/Untermiete; SCH3-202d); Belegabstimmung (SCH3-301); fest bis 31.12.2033 für Anhangangabe
- [F_Aktive_Rechnungsabgrenzung/Aktive_Rechnungsabgrenzungen_31.12.2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/F_Aktive_Rechnungsabgrenzung/Aktive_Rechnungsabgrenzungen_31.12.2025.md) – Konto 1300 nur Versicherung 8'400 und Softwarelizenz 11'600 (Total 20'000); keine Abgrenzung der vorausbezahlten Miete 01/2026 (SCH3-302)
- [K_Passive_Abgrenzungen_Rueckstellungen/Passive_Abgrenzungen_und_Rueckstellungen_31.12.2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/K_Passive_Abgrenzungen_Rueckstellungen/Passive_Abgrenzungen_und_Rueckstellungen_31.12.2025.md) – Konto 2300: Strom 3'200, Telefon 1'800, Treuhand 10'000 (Total 15'000); kein Revisionshonorar ersichtlich → Frage (SCH3-302); Rückstellungsspiegel für Fehlklassierung im Aufwand (SCH3-303)
- [H_Kreditoren/Kreditorenjournal_Januar_2026.md](../../testdaten/fiktive-zahlen-ag-2025/text/H_Kreditoren/Kreditorenjournal_Januar_2026.md) – Eingangsrechnungen Januar 2026 mit Rechnungsdatum, Leistungstext und Aufwandkonto; für SCH3 nur ITF-26-0004 «Support Januar 2026» (6570, 1'430, betrifft 2026) (SCH3-302)
- [00_Allgemein/Kontoblaetter_Folgejahr_Jan_Feb_2026.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Kontoblaetter_Folgejahr_Jan_Feb_2026.md) – Kontoblatt 2000 Kreditoren Januar 2026 (neue Rechnung) für die Durchsicht auf Aufwand des Berichtsjahres (SCH3-302)
- [H_Kreditoren/Kreditoren_OP_Liste_31.12.2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/H_Kreditoren/Kreditoren_OP_Liste_31.12.2025.md) – Offene Kreditoren per 31.12.2025 zum Abgleich der Folgejahresrechnungen (Vollständigkeit, SCH3-302)
- [00_Allgemein/Belegverzeichnis.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Belegverzeichnis.md) – Kein Budget, keine Aufwand-Kontoblätter, keine Eingangsrechnungen zu 6xxx und keine noch nicht verbuchten Rechnungen → PBC-Pendenzen (SCH3-202b/c, -301, -302, -303)
- [J_Uebrige_kurzfristige_Verbindlichkeiten/MWST_Abrechnungen_2025_Zusammenzug.md](../../testdaten/fiktive-zahlen-ag-2025/text/J_Uebrige_kurzfristige_Verbindlichkeiten/MWST_Abrechnungen_2025_Zusammenzug.md) – Zusammenzug ohne Angabe zur Bezugsteuer; Abrechnung Bezugsteuer/Privatanteile (z.B. Software 6565) erfragen, Schnittstelle M2
- [00_Allgemein/Unternehmensinformationen_2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Unternehmensinformationen_2025.md) – Ansprechpersonen für Befragungen (SCH3-101); Organe/Nahestehende für Durchsicht Konto 6540 und Leistungen an Nahestehende (SCH3-303)
