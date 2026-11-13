---
typ: testfall-hinweise
titel: Testakte 2025 (fiktiv) – Prüffeld SCH2 (nur für Tests, nicht ins Plugin)
jur: ch
quellen: []
status: entwurf
generiert: tools/build_quick.py, 2026-11-13
---


# SCH2 · Direkter Aufwand – Testakte 2025 (fiktiv)

> **Nur für Tests, nicht ins Plugin.** Bezüge der fiktiven Testakte 2025 (Feld `testakte_2025` in data/prueffelder/). Nicht nach quick/ oder wiki/ übernehmen und nicht als Wissen des Agenten verwenden (Überanpassung an die Messung).

Quelle: data/prueffelder/sch2.yaml (Feld testakte_2025)

## Testakte 2025 (fiktiv)
- [00_Allgemein/Saldoliste_2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Saldoliste_2025.md) – Blatt «Erfolgsrechnung» (Vorzeichen: Ertrag positiv, Aufwand negativ): direkter Aufwand 4201–4209, 4300–4305, 4400–4404, 4902; Nettoerlöse 3200, 3201, 3205, 3400, Erlösminderung 3800, Bestandesänderung angefangene Arbeiten 3900 (Vorzeichenwechsel ggü. VJ) – SCH2-102, SCH2-201 (Gesamtleistung), SCH2-202 a/d; Blatt «Bilanz» Vorräte 1201–1205/1290 – SCH2-302
- [00_Allgemein/Jahresrechnung_2025_Fiktive_Zahlen_AG_Testfassung.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Jahresrechnung_2025_Fiktive_Zahlen_AG_Testfassung.md) – Erfolgsrechnung Block «Direkter Aufwand»; Anhang Ziff. 1 (Grundsätze), Ziff. 3 (ausserordentliche Aufwände/Erträge, u.a. Lieferantenrabatt, nachträgliche Buchungen Vorjahr), Ziff. 4 (POC-Methode, Warenvorräte) – SCH2-101, SCH2-201, SCH2-202, SCH2-302
- [00_Allgemein/Hauptbuch_2025_Kontoblaetter.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Hauptbuch_2025_Kontoblaetter.md) – Gemäss Belegverzeichnis nur Bilanzkonten und Konto 8510, keine Kontoblätter 4xxx; Gegenbuchungen auf Aufwand und Lieferantenzahlungen in Geld- und Kreditorenkonten – SCH2-202 b, SCH2-301 (Kontoblätter 4xxx als PBC anfordern)
- [00_Allgemein/Kontoblaetter_Folgejahr_Jan_Feb_2026.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Kontoblaetter_Folgejahr_Jan_Feb_2026.md) – Blatt «2000 Kreditoren 2026» mit Gegenkonten 4201/4400/4401 und Leistungszeiträumen – SCH2-302, SCH2-303
- [00_Allgemein/Belegverzeichnis.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Belegverzeichnis.md) – Übersicht der gelieferten Unterlagen; Basis für PBC-Pendenzen (Lieferantenrechnungen, Margenstatistik, Budget, Liste Nahestehende) – SCH2-201, SCH2-202 c, SCH2-301
- [00_Allgemein/Unternehmensinformationen_2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Unternehmensinformationen_2025.md) – Geschäftstätigkeit (PV-Kraftwerke, Handel Solarkomponenten) für Produktkategorien und Erwartungen; Ansprechpersonen für Pendenzen – SCH2-101, SCH2-102, SCH2-201
- [H_Kreditoren/Kreditorenjournal_Januar_2026.md](../../testdaten/fiktive-zahlen-ag-2025/text/H_Kreditoren/Kreditorenjournal_Januar_2026.md) – Eingangsrechnungen Januar 2026 mit Rechnungsdatum, Leistungstext und Aufwandkonto – SCH2-302, SCH2-303
- [H_Kreditoren/Kreditoren_OP_Liste_31.12.2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/H_Kreditoren/Kreditoren_OP_Liste_31.12.2025.md) – Offene Lieferantenrechnungen per Stichtag (Rechnungen Dezember) – SCH2-303 Gegenprobe, SCH2-301 Auswahl
- [H_Kreditoren/Lieferantenrechnung_Teststein_2025-1187_Scan.md](../../testdaten/fiktive-zahlen-ag-2025/text/H_Kreditoren/Lieferantenrechnung_Teststein_2025-1187_Scan.md) – Einzelbeleg Montageleistung (Scan mit Eingangsstempel, ohne Transkription) – SCH2-303, SCH2-301
- [K_Passive_Abgrenzungen_Rueckstellungen/Passive_Abgrenzungen_und_Rueckstellungen_31.12.2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/K_Passive_Abgrenzungen_Rueckstellungen/Passive_Abgrenzungen_und_Rueckstellungen_31.12.2025.md) – Liste passive Abgrenzungen Konto 2300 – SCH2-303 Abgleich mit nachträglich eingegangenen Rechnungen; Garantierückstellungen als Bezug zu Konto 4404
- [D_Vorraete/Inventarliste_31.12.2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/D_Vorraete/Inventarliste_31.12.2025.md) – Bestände Handelswaren/Material (Konten 1201, 1202, 1205) und Wertberichtigung 1290 – SCH2-202 e, SCH2-302 Bestandesänderungen 4207–4209 (Vorzeichen beachten)
- [E_Angefangene_Arbeiten_Anzahlungen/Projektliste_Angefangene_Arbeiten_31.12.2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/E_Angefangene_Arbeiten_Anzahlungen/Projektliste_Angefangene_Arbeiten_31.12.2025.md) – Einzelkosten je Projekt und Gemeinkostenzuschlag – SCH2-201 Marge je Projekt, SCH2-302 sachliche Abgrenzung, Bestandesänderung 3900
- [J_Uebrige_kurzfristige_Verbindlichkeiten/MWST_Abrechnungen_2025_Zusammenzug.md](../../testdaten/fiktive-zahlen-ag-2025/text/J_Uebrige_kurzfristige_Verbindlichkeiten/MWST_Abrechnungen_2025_Zusammenzug.md) – Vorsteuer je Periode als andere Unterlage zur Plausibilisierung des Einkaufsvolumens – SCH2-202 e
