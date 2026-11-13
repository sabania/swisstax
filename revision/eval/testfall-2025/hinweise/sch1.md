---
typ: testfall-hinweise
titel: Testakte 2025 (fiktiv) – Prüffeld SCH1 (nur für Tests, nicht ins Plugin)
jur: ch
quellen: []
status: entwurf
generiert: tools/build_quick.py, 2026-11-13
---


# SCH1 · Betrieblicher Ertrag – Testakte 2025 (fiktiv)

> **Nur für Tests, nicht ins Plugin.** Bezüge der fiktiven Testakte 2025 (Feld `testakte_2025` in data/prueffelder/). Nicht nach quick/ oder wiki/ übernehmen und nicht als Wissen des Agenten verwenden (Überanpassung an die Messung).

Quelle: data/prueffelder/sch1.yaml (Feld testakte_2025)

## Testakte 2025 (fiktiv)
- [00_Allgemein/Saldoliste_2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Saldoliste_2025.md) – Blatt «Erfolgsrechnung»: Ertragskonten 3200/3201/3205/3400, Erlösminderungen 3800/3802, Bestandesänderung 3900 (−300'000, VJ +480'000) sowie Waren-/Materialaufwand 42xx–44xx inkl. 4207–4209 mit Vorjahr – SCH1-102, 201, 202a/d, 304/305. Auffällig: 3800 Skonti 0 (VJ −50'000, Wegfall klären), 3205 «Ertrag Allgemein» 30'000 neu, 8100 Betriebsfremder Ertrag 460'000 (VJ 60'000) – Klassierung SCH1-102/305, Schnittstelle SCH5
- [00_Allgemein/Jahresrechnung_2025_Fiktive_Zahlen_AG_Testfassung.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Jahresrechnung_2025_Fiktive_Zahlen_AG_Testfassung.md) – Erfolgsrechnung (Block «Betrieblicher Ertrag» inkl. 3900 im Total, Finanz-, Liegenschafts-, betriebsfremder und a.o. Ertrag) und Anhang Ziff. 1 Grundsätze, Ziff. 3 a.o. Positionen (u.a. Lieferantenrabatt als a.o. Ertrag), Ziff. 4a POC – SCH1-101, 304, 305
- [00_Allgemein/Hauptbuch_2025_Kontoblaetter.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Hauptbuch_2025_Kontoblaetter.md) – Blatt «1100»: monatliche Fakturen-Sammelbuchungen und Dezember-Einzelfakturen mit Gegenkonto 3200 (Fakturen-Soll, Stichprobe, Cut-off) sowie Buchung DL-2025-01 (Darlehen an Aktionär auf Debitorenkonto, 150'000) – Fall für SCH1-155 und 202e; Blatt «1301»/Buchung AB-31 zu 3900; Blatt «8510» a.o. Ertrag – SCH1-202b/e, 301, 302, 303, 401, 155. Kontoblätter der Ertragskonten selbst fehlen (PBC)
- [00_Allgemein/Kontoblaetter_Folgejahr_Jan_Feb_2026.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Kontoblaetter_Folgejahr_Jan_Feb_2026.md) – Blätter «1100» und «3200» Januar/Februar 2026 (Fakturen, Gutschrift GS-2026-003, Ausbuchung AB-2026-01 zu Fakturen 2025 – Ereignisse nach dem Stichtag) – SCH1-302, 303; Blatt «2000 Kreditoren 2026» (Montage 24.11.–19.12.2025 und Gerüst Dezember 2025, erst im Januar 2026 gebucht) – Cut-off Materialaufwand SCH1-101, 201
- [00_Allgemein/Unternehmensinformationen_2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Unternehmensinformationen_2025.md) – Zweck (PV-Kraftwerke, Handel Solarkomponenten) für Produktkategorien und Retourenrisiko, Rahmenvertrag, Buchhaltungssoftware mit Debitorenmodul, Ansprechpersonen – SCH1-101, 201, 401
- [00_Allgemein/Belegverzeichnis.md](../../testdaten/fiktive-zahlen-ag-2025/text/00_Allgemein/Belegverzeichnis.md) – Abgleich vorhandener Unterlagen; fehlende Ertragskontoblätter, Umsatz-/Margenstatistik, Budget, Lieferpapiere als PBC-Pendenz
- [B_Forderungen_aus_LuL/Debitorenrechnung_RE-2025-0481.md](../../testdaten/fiktive-zahlen-ag-2025/text/B_Forderungen_aus_LuL/Debitorenrechnung_RE-2025-0481.md) – Beleg zu Dezember-Faktura (Kontoblatt 1100) – SCH1-301, 303
- [B_Forderungen_aus_LuL/Debitorenrechnung_RE-2025-0461.md](../../testdaten/fiktive-zahlen-ag-2025/text/B_Forderungen_aus_LuL/Debitorenrechnung_RE-2025-0461.md) – Beleg Ausgangsrechnung – SCH1-301
- [B_Forderungen_aus_LuL/Debitorenrechnung_RE-2026-0004.md](../../testdaten/fiktive-zahlen-ag-2025/text/B_Forderungen_aus_LuL/Debitorenrechnung_RE-2026-0004.md) – Akontorechnung Etappe 2 (Rechnungsdatum 05.01.2026, Ausführung Januar 2026), per 31.12.2025 auf 1100/3200 gebucht; Betrag inkl. MWST – Risikohinweis für weiter gehende Handlungen SCH1-301, 303, 202e
- [B_Forderungen_aus_LuL/Debitoren_OP_Liste_31.12.2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/B_Forderungen_aus_LuL/Debitoren_OP_Liste_31.12.2025.md) – Belegdaten und Bemerkungen der offenen Posten für Cut-off und Kontenkonstellationen auf dem Debitorenkonto (u.a. DL-2025-01) – SCH1-303, 155
- [E_Angefangene_Arbeiten_Anzahlungen/Projektliste_Angefangene_Arbeiten_31.12.2025.md](../../testdaten/fiktive-zahlen-ag-2025/text/E_Angefangene_Arbeiten_Anzahlungen/Projektliste_Angefangene_Arbeiten_31.12.2025.md) – Grundlage Bestandesänderung 3900, Bewertungsmethode und Fertigstellungsgrad je Projekt (Abgleich mit Anhang Ziff. 4a POC und POCM-Voraussetzungen), Abgrenzung Umsatz vs. angefangene Arbeiten – SCH1-201, 202, 303, 305; Schnittstelle F2
- [E_Angefangene_Arbeiten_Anzahlungen/Abnahmeprotokoll_P-2025-03_Fiktivia.md](../../testdaten/fiktive-zahlen-ag-2025/text/E_Angefangene_Arbeiten_Anzahlungen/Abnahmeprotokoll_P-2025-03_Fiktivia.md) – Leistungsnachweis (Inbetriebnahme/Abnahme) für Realisationszeitpunkt – SCH1-301, 303
- [H_Kreditoren/Kreditorenjournal_Januar_2026.md](../../testdaten/fiktive-zahlen-ag-2025/text/H_Kreditoren/Kreditorenjournal_Januar_2026.md) – Eingangsrechnungen Januar 2026 mit Leistungen 2025 – Cut-off Waren-/Materialaufwand für SCH1-101, 201 (Schnittstelle SCH2, K1)
- [J_Uebrige_kurzfristige_Verbindlichkeiten/MWST_Abrechnungen_2025_Zusammenzug.md](../../testdaten/fiktive-zahlen-ag-2025/text/J_Uebrige_kurzfristige_Verbindlichkeiten/MWST_Abrechnungen_2025_Zusammenzug.md) – Deklarierter Umsatz je Quartal (Ziff. 200) für Umsatzabstimmung – SCH1-202e, 301
- [K_Passive_Abgrenzungen_Rueckstellungen/Aktennotiz_Rechtsfall_Kunstrasen_Fiktiv_AG.md](../../testdaten/fiktive-zahlen-ag-2025/text/K_Passive_Abgrenzungen_Rueckstellungen/Aktennotiz_Rechtsfall_Kunstrasen_Fiktiv_AG.md) – Mängelrüge eines Kunden als Hintergrund für Erlösminderungen/Gutschriften nach dem Stichtag (GS-2026-003) – SCH1-102, 302
