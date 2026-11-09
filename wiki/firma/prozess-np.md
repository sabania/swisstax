---
typ: thema
titel: Steuerprozess Natürliche Personen (consis)
jur: multi
jahre:
- 2025
- 2026
quellen:
- steuerprozess-np-2026-10-27
status: entwurf
generiert: tools/build_firma.py (2026-11-09)
---

# Steuerprozess Natürliche Personen (consis)

> Quelle: Prozessbeschrieb «Steuerprozess Natürliche Personen», Stand 2026-10-27, Version 9 ([PDF](../../firma/quellen/steuerprozess-np-2026-10-27.pdf)) · Status: [{'name': 'Offen', 'bedingung': 'Prozessobjekt erstellt (1.1., ein Objekt pro Mandat und Vorjahr)', 'setzt': 'M-Files'}, {'name': 'Offen (Steuerkunde)', 'bedingung': 'automatischer Übergang mit Bedingung (bestehender Steuerkunde)', 'setzt': 'M-Files'}, {'name': 'Offen (Laufkundschaft)', 'bedingung': 'automatischer Übergang mit Bedingung (Laufkundschaft)', 'setzt': 'M-Files'}, {'name': 'Reset Workflow', 'bedingung': 'Neustart eines Prozesses, führt zurück auf «Offen»', 'setzt': 'nur Mensch', 'pflicht': 'KI erkennt den Neustart und protokolliert ihn'}, {'name': 'Unterlagen erhalten', 'bedingung': 'sofort, sobald Unterlagen eingegangen und abgelegt sind (erster Beleg abgelegt)', 'setzt': 'KI', 'pflicht': 'Feld «Unterlagen erhalten» = Eingangsdatum (nie überschreiben); direkt danach Vorjahresabgleich, Vollständigkeit, Kundenpendenzen'}, {'name': 'in Arbeit (St)', 'bedingung': 'direkt nach der Pendenzenermittlung, mit Beginn der Erfassung in DrTax', 'setzt': 'KI', 'pflicht': 'Erfassung DrTax, QK, Plausibilisierung Vermögensentwicklung, Entwurf'}, {'name': 'zur Kontrolle', 'bedingung': 'Entwurf-PDF in Kategorie «Deklaration» und Flag «Steuerberechnung erstellt»', 'setzt': 'KI / SB', 'pflicht': '«Zugewiesen an» = Prüfer (ML); M-Files mailt an Prüfer; Protokoll-Agent starten'}, {'name': 'zur Fertigstellung / Versand', 'bedingung': 'Prüfung und Besprechung abgeschlossen', 'setzt': 'nur ML', 'pflicht': 'Kundenpendenzen nachführen'}, {'name': 'In Excel-Fristenliste austragen', 'bedingung': 'Einreichung erfolgt (online oder Post)', 'setzt': 'nur ML / SB', 'pflicht': 'Fristenliste und Kopie an Kunde auslösen'}, {'name': 'Physische ULA zurückschicken', 'bedingung': 'Datum «erledigt» eingetragen', 'setzt': 'KI', 'pflicht': 'prüfen, ob physischer Eingang markiert (ULA = Unterlagen)'}, {'name': 'Abgeschlossen', 'bedingung': 'Rücksendung bestätigt oder nur digitaler Eingang', 'setzt': 'SEK / SB, KI bei rein digital'}]. Werkzeug: `steuer prozess …`. Steuerrecht dazu: Quick-Layer und Wiki; M-Files-Ablage: [mfiles-ablage.md](mfiles-ablage.md).

## Grundsätze

- **M-Files ist zentral und Master:** Jeder Schritt führt Status, Felder, Flags und QK-Checkboxen im Prozessobjekt «Steuererklärung NAT» nach. M-Files ist Master für Kundenstammdaten (Name, Adresse) und für die Zuständigkeit (ML = Feld «Prüfer», SB = Feld «Sachbearbeiter»). Die KI liest diese Angaben, ändert sie aber nie.
- **Grenze der KI:** Einreichung, Antworten und Einsprachen an das Steueramt sowie der Status «In Excel-Fristenliste austragen» nur durch ML (in der Regel) oder SB.
- **KI handelt selbst:** In M-Files setzt die KI Status, Felder, Flags, QK-Checkboxen und Metadaten selbst (Entscheid 02.10.2026). Jede Aktion wird zwingend protokolliert.
- **Keine echten Kundendaten:** Entwicklung und Tests nur mit «Muster Hans» (alleinstehend) und «Hans und Anna Muster» (verheiratet).
- **Nie schätzen:** Unsichere Werte nie schätzen → Pendenz an SB; fehlende Belege blockieren die Erfassung nicht.

**Rollen:** **ML** = Mandatsleiter/in = Feld «Prüfer» im Prozessobjekt (prüft, bespricht, setzt Status «zur Fertigstellung / Versand») · **SB** = Sachbearbeiter/in = Feld «Sachbearbeiter» (Freigaben, Versand, Kundenkontakt, Entscheid bei Abweichungen) · **SEK** = Sekretariat (Scan, Rücksendung physischer Unterlagen) · **FE** = Prozessverantwortung, Prüfkorb (gebündelt), Kill-Switch, Tagesbericht · **KI** = Agenten A1–A10

**Gesamtablauf:** Am 1.1. erzeugt M-Files für jedes Mandat (alleinstehend oder Ehepaar) ein Prozessobjekt «Steuererklärung NAT» für das Vorjahr. Schritte 0–4 laufen im Workflow «Steuererklärung nat» (ID 122); Schritt 5 (Veranlagung) und 6 (provisorische Rechnung) ohne Workflow-Status, Dokumente werden trotzdem abgelegt und jede Aktion protokolliert. Mengengerüst ca. 400 Mandate, im Schnitt 15 Belege, rund 6'000 Belege pro Jahr, Spitze zu Jahresbeginn. Nachlieferungen jederzeit über Schritt 1.

## Statusmodell (M-Files-Workflow «Steuererklärung nat», ID 122)

| Status | Bedingung für Eintritt | wer setzt | Pflichtaktion |
|---|---|---|---|
| Offen | Prozessobjekt erstellt (1.1., ein Objekt pro Mandat und Vorjahr) | M-Files | – |
| Offen (Steuerkunde) | automatischer Übergang mit Bedingung (bestehender Steuerkunde) | M-Files | – |
| Offen (Laufkundschaft) | automatischer Übergang mit Bedingung (Laufkundschaft) | M-Files | – |
| Reset Workflow | Neustart eines Prozesses, führt zurück auf «Offen» | nur Mensch | KI erkennt den Neustart und protokolliert ihn |
| Unterlagen erhalten | sofort, sobald Unterlagen eingegangen und abgelegt sind (erster Beleg abgelegt) | KI | Feld «Unterlagen erhalten» = Eingangsdatum (nie überschreiben); direkt danach Vorjahresabgleich, Vollständigkeit, Kundenpendenzen |
| in Arbeit (St) | direkt nach der Pendenzenermittlung, mit Beginn der Erfassung in DrTax | KI | Erfassung DrTax, QK, Plausibilisierung Vermögensentwicklung, Entwurf |
| zur Kontrolle | Entwurf-PDF in Kategorie «Deklaration» und Flag «Steuerberechnung erstellt» | KI / SB | «Zugewiesen an» = Prüfer (ML); M-Files mailt an Prüfer; Protokoll-Agent starten |
| zur Fertigstellung / Versand | Prüfung und Besprechung abgeschlossen | nur ML | Kundenpendenzen nachführen |
| In Excel-Fristenliste austragen | Einreichung erfolgt (online oder Post) | nur ML / SB | Fristenliste und Kopie an Kunde auslösen |
| Physische ULA zurückschicken | Datum «erledigt» eingetragen | KI | prüfen, ob physischer Eingang markiert (ULA = Unterlagen) |
| Abgeschlossen | Rücksendung bestätigt oder nur digitaler Eingang | SEK / SB, KI bei rein digital | – |

Kein Rückweg von «zur Kontrolle» nach «in Arbeit (St)»; zurück nach «Offen» nur über «Reset Workflow» (nur Mensch). Testphase: Kopie wflow.SteuererklrungNatTest (ID 152).

## Schritt 1 · Eingang Steuerunterlagen

- **Status:** Offen → Unterlagen erhalten · **Auslöser:** neues E-Mail mit Anhang, Upload Kundenportal, neues DeepBox-Dokument, neue Scan-Datei
- **Agent:** A1 Eingang und Klassifizierung, A2 Prozessobjekt · **Output:** Beleg mit Metadaten in M-Files, Status und Datum gesetzt, Protokoll; sonst Prüfkorb · Prozessbeschrieb S. 7, 8, 9, 10
- **Eingangskanäle:** K1 Info-Postfach info@ (Microsoft Graph, Service-Konto) · K2 Postfach SB / ML (freigegebener Ordner) · K3 M-Files-Kundenportal (Upload liegt schon in M-Files) · K4 DeepBox (technischer Zugang, kein persönliches 2FA) · K5 Post (Sekretariat scannt, Scanner Innenzone/West, Ziel vermutlich M-Files Scaneingang) · K6 Sekretariat (persönlich abgegeben, Scan)

| Nr. | Tätigkeit | wer | System | Regel / Detail |
|---|---|---|---|---|
| 1.1 | Anhang als steuerrelevant erkennen | KI | M365 | Lohnausweis, Bank- und Wertschriftenausweise, 3a, Versicherungen, Liegenschaft, Krankheitskosten, Spenden, Jahresrechnung Einzelfirma, Hauptformular, Veranlagung, Steuerrechnung, provisorische Rechnung. Gilt für K1/K2: nicht relevant → E-Mail unberührt lassen. |
| 1.2 | Physischen Eingang markieren | KI | M-Files | bei K5 und K6; Grundlage für Status «Physische ULA zurückschicken» |
| 1.3 | Datei holen, Ereignis-ID vergeben | KI | alle | Ereignis-ID macht Verarbeitung wiederholbar ohne Doppelablage |
| 1.4–1.5 | Lesbarkeit prüfen, OCR | KI | – | Passwortschutz oder defekte Datei → Prüfkorb |
| 1.6 | Sammel-PDF trennen | KI | – | ein Beleg = eine Datei (Online-Übermittlung DrTax) |
| 1.7 | Dublettenprüfung | KI | M-Files | gleicher Inhalt → nicht ablegen, nur protokollieren |
| 1.8–1.9 | Mandant bestimmen | KI | M-Files | 1. Name auf dem Dokument, 2. Absender der Lieferung; mehrdeutig → Prüfkorb; keine Mandantennummern. Mandant = «Nachname Vorname» (z.B. Muster Hans); Ehepaar = ein Mandant. |
| 1.9a | Neue Steuererklärung ohne Kunde in M-Files | KI | M-Files, M365 | Entscheide 22. und 27.10.2026: KI legt den Mandanten in M-Files an (Name, Adresse gemäss Dokument) und meldet an die Zuteilungsverantwortlichen (siehe firma/konfiguration.yaml); diese teilen ML und SB zu, die KI nie. Danach Ablage und normaler Ablauf. Nachlieferungen in derselben Meldung ergänzen. |
| 1.10 | Sonderfälle ausschliessen | KI | – | Juristische Personen → Prüfkorb (nicht Teil dieses Prozesses) |
| 1.11–1.12 | Jahr, Dokumentart, Kategorie | KI | M-Files | Steuerjahr = Bescheinigungsjahr des Belegs. Zuerst Klasse im Bereich ST – Steuern (StE, Veranlagung + def. Steuerrechnung, Prov. Steuerrechnung, Kontoauszug, Auflage/Buchprüfung, Einsprache/Rekurs …), dann Kategorie. Grundlage: Zuordnungsliste Anhang F (data/firma/mfiles.yaml); sonst Ablagemuster ähnlicher Dokumente übernehmen; nur Werte aus der aktuellen M-Files-Werteliste, über IDs. |
| 1.13 | Sicherheit prüfen | KI | – | Mandant, Jahr und Kategorie sicher über Schwellwert? Schwellwert in der Testphase festlegen; darunter Prüfkorb statt Ablage |
| 1.14 | Ablage | KI | M-Files | Klasse (z.B. StE), Adresse «Nachname Vorname», Jahr, Kategorie, Beschreibung (z.B. «Lohnausweis Arbeitgeber», «Hauptformular»). Grundstückgewinn-, Erbschafts- und Schenkungssteuer: eigene Klassen, Meldung an ML. |
| 1.15 | Weiterleiten nach Typ | KI | – | Veranlagung, Rechnung, Nachfrage → Schritt 5; provisorische Rechnung → Schritt 6; Steuerbeleg/Hauptformular → 1.16 |
| 1.16–1.17 | Prozessobjekt nachführen | KI | M-Files | bei «Offen»: Status «Unterlagen erhalten» und Feld Unterlagen erhalten = Eingangsdatum; sonst (Nachlieferung) mit Kundenpendenzen-Details abgleichen, erledigte Positionen streichen, alle erledigt → Flag zurücksetzen; Status bleibt |
| 1.18 | Protokoll | KI | M-Files | Kanal, Datei, Mandant, Jahr, Kategorie, Sicherheit, Aktion, Ergebnis |

**Pruefkorb:** Prüfkorb = Grund, Vorschlag KI, Dokument-Link, gebündelt an FE. Anlässe: Datei nicht lesbar/Passwort, Mandant mehrdeutig, juristische Person, Sicherheit unter Schwellwert.

## Schritt 2 · Verarbeitung der Unterlagen – sofort nach Eingang

- **Status:** Unterlagen erhalten → in Arbeit (St) → zur Kontrolle · **Auslöser:** Status «Unterlagen erhalten» – sofort, ohne Wartezeit und ohne Mindestbestand an Belegen (Entscheid 26.10.2026)
- **Agent:** A3 Vollständigkeit, A4 Erfassung DrTax, A5 QK und Vermögensvergleich, A6 Entwurf · **Output:** Kundenpendenzen direkt nach Erhalt, Erfassung DrTax, Vermögensplausibilisierung, Entwurf-PDF in M-Files, Status «zur Kontrolle» · Prozessbeschrieb S. 11, 12, 13

| Nr. | Tätigkeit | wer | System | Regel / Detail |
|---|---|---|---|---|
| 2.1 | Status «Unterlagen erhalten» | KI | M-Files | Feld «Unterlagen erhalten» = Eingangsdatum (nie überschreiben); aus «Offen», «Offen (Steuerkunde)» oder «Offen (Laufkundschaft)» |
| 2.2 | Vorjahresabgleich, Soll-Belegliste | KI | M-Files | Vorjahresdeklaration (PDF, bis StE 2024 aus kantonaler Software), Vorjahresbelege (StE: Belege eingereicht, WSVZ, Liegenschaften), Einschätzung Vorjahr (Veranlagung + def. Steuerrechnung) → Soll-Belegliste |
| 2.3 | Vollständigkeit, Kundenpendenzen ermitteln | KI | M-Files | Flag «Kundenpendenzen offen» + Details (Liste); QK «StE mit Vorjahr / mit Einschätzung Vorjahr überprüft»; bei Nachlieferungen neu prüfen, Erledigtes streichen, Flag zurücksetzen wenn alles da |
| 2.4 | Einforderung fehlender Unterlagen | KI | M365 | E-Mail nur als Entwurf an die SB gemäss M-Files; Versand nach Freigabe SB (bis Entscheid Fragen 24 / 31) |
| 2.5 | Direkt in DrTax abfüllen, Status «in Arbeit (St)» | KI | DrTax, M-Files | Mandant über Namen suchen (eindeutig → weiter; nicht vorhanden → anlegen mit Stammdaten aus M-Files (Master); mehrdeutig → Prüfkorb). Beleg für Beleg mit Beleg-Referenz je Position; unsichere Werte nie schätzen → Pendenz an SB; fehlende Belege blockieren nicht |
| 2.6 | Prüfpunkte | KI | DrTax, M-Files | ausländische Quellensteuer, Steuerausscheidung (Kategorie Steuerausscheidung), Steuerfaktoren → Checkboxen |
| 2.7 | Plausibilisierung Vermögensentwicklung | KI | DrTax, M-Files | Vermögensvergleich (zentral) → Checkbox; ungeklärte Differenz in Notiz; wesentliche Veränderungen ab ± CHF 20'000 Einkommen / ± CHF 50'000 Vermögen → Feld «Wesentliche Veränderungen zum Vorjahr» abfüllen |
| 2.8 | Steuerberechnung, Entwurf ablegen, «zur Kontrolle» | KI | DrTax, M-Files | Flag «Steuerberechnung erstellt»; Entwurf als PDF: Klasse StE, Kategorie Deklaration, Beschreibung «Entwurf TT.MM.JJJJ»; «Zugewiesen an» = Prüfer; offene Pendenzen bleiben im Flag |

**Hinweis:** Schnittstelle DrTax noch offen (Ringler Informatik AG): Variante A Datenimport über Hersteller-Schnittstelle, Variante B strukturierte Erfassungsliste für SB. Die Online-Übermittlung darf für das KI-Konto nie verfügbar sein.

## Schritt 3 · Prüfung durch ML und Besprechung mit dem Kunden

- **Status:** zur Kontrolle → zur Fertigstellung / Versand · **Auslöser:** Status «zur Kontrolle»
- **Agent:** A7 Protokoll (Besprechung) · **Output:** Besprechungsprotokoll, Feld «Wesentliche Veränderungen», Pendenzen, Status durch ML · Prozessbeschrieb S. 14, 15, 16

| Nr. | Tätigkeit | wer | System | Regel / Detail |
|---|---|---|---|---|
| 3.1 | M-Files sendet E-Mail an Prüfer ML | M-Files | – |  |
| 3.2 | Daten sammeln | KI | – | Entwurf, Vorjahr, Einschätzung Vorjahr, QK-Felder, Kundenpendenzen |
| 3.3 | Besprechungsprotokoll-Entwurf | KI | – | 1 Einkünfte · 2 Vermögen · 3 Abzüge · 4 Schulden · 5 Weitere Punkte · 6 Steuerplanung als Vorschlag |
| 3.4 | Protokoll ablegen | KI | – | Beschreibung «Besprechungsprotokoll Entwurf TT.MM.JJJJ» |
| 3.5 | Feld Wesentliche Veränderungen zum Vorjahr nachführen | KI | – |  |
| 3.6–3.7 | ML prüft Entwurf und Protokoll; Risikobeurteilung Ja/Nein (bei Ja separater Prozess ML) | ML | – |  |
| 3.8 | Korrekturen nötig? | ML | – | ja → Korrekturauftrag an SB/KI, Status bleibt «zur Kontrolle» (kein Rückweg im Workflow), zurück zu Schritt 2 ab 2.8 |
| 3.9–3.10 | Besprechung mit dem Kunden (persönlich, Telefon, Sitzung; ML oder SB); ML ergänzt Protokoll mit Entscheiden des Kunden | ML/SB | – |  |
| 3.11 | Neue Pendenzen aus Besprechung? | KI | – | ja → Flag Kundenpendenzen und Details, KI trägt nach Angabe ML ein |
| 3.12 | ML setzt Status «zur Fertigstellung / Versand», Zuweisung an SB | nur ML | – |  |

**Aufbau Besprechungsprotokoll:**

- **Kopf:** Mandant (z.B. Hans und Anna Muster), Steuerjahr, Datum, ML, SB – Quelle Prozessobjekt
- **1 Einkünfte:** Vergleich Vorjahr je Einkunftsart, wesentliche Abweichungen mit Begründung oder Frage an den Kunden – DrTax aktuell und Vorjahr
- **2 Vermögen:** Vergleich Vorjahr, Ergebnis Vermögensvergleich, nicht erklärte Differenz – DrTax, QK
- **3 Abzüge:** neue, weggefallene oder veränderte Abzüge – DrTax
- **4 Schulden:** Veränderungen Hypotheken und übrige Schulden, Schuldzinsen – DrTax
- **5 Weitere Punkte:** Abweichungen zur Einschätzung Vorjahr, offene Kundenpendenzen, Steuerausscheidung, Quellensteuer-Rückforderung – Prozessobjekt, QK
- **6 Steuerplanung:** Hinweise als Vorschlag gekennzeichnet; Entscheid ML – KI-Vorschlag
- **regel:** Wesentlich ist eine Abweichung ab ± CHF 20'000 beim Einkommen bzw. ± CHF 50'000 beim Vermögen. Das Protokoll enthält nie Daten anderer Mandanten.

## Schritt 4 · Fertigstellung, Einreichung, Fristenliste und Abschluss

- **Status:** zur Fertigstellung / Versand → Abgeschlossen · **Auslöser:** Status «zur Fertigstellung / Versand»; danach Status «In Excel-Fristenliste austragen» durch ML / SB
- **Agent:** A1 Nachlieferungen, A3 Pendenzen, A4 Ergänzung DrTax, A8 Fristen und Abschluss · **Output:** finale StE, Fristenliste nachgeführt, Kopie beim Kunden, Rücksendung, Status «Abgeschlossen» · Prozessbeschrieb S. 17, 18, 19

| Nr. | Tätigkeit | wer | System | Regel / Detail |
|---|---|---|---|---|
| 4.1–4.5 | Pendenzen erledigen | KI | M-Files, DrTax | Flag Kundenpendenzen offen? ja → auf Nachlieferung warten (alle Kanäle aus Schritt 1); nach 14 Tagen Erinnerung an Kunde als E-Mail-Entwurf, Freigabe SB; fehlt weiterhin → Erinnerung an SB/ML; Nachlieferung zuordnen, mit Details abgleichen, Erledigtes streichen; Werte in DrTax ergänzen, Steuerberechnung neu. Erinnerungsintervall offen (Frage 23); Flag zurücksetzen, wenn alle Positionen erledigt |
| 4.6 | Finale StE ablegen | KI / SB | M-Files | Kategorie «Deklaration», Beschreibung «Steuererklärung final»; Freigabequittung vom Kunden unterzeichnet? nein → Meldung an SB, keine Einreichung |
| 4.7 | Einreichung | nur ML / SB | DrTax / Post | primär online aus DrTax, sonst Post. Die KI hat technisch keine Übermittlungsrechte |
| 4.8 | Übermittlungsbestätigung | KI | M-Files | Kategorie «Übermittlungsbestätigung» |
| 4.9 | Status «In Excel-Fristenliste austragen» | nur ML / SB | M-Files | bestätigt die Einreichung; für das KI-Konto gesperrt. Fristen: Steuerperiode 2025 Excel in M-Files, ab 01.01.2027 in DrTax |
| 4.10 | Fristenliste nachführen | KI | Excel in M-Files | «Fristenliste Natürliche Personen»; nur Spalte «erledigt» (= Datum) schreiben, nur wenn Zeile des Mandanten eindeutig, sonst Prüfkorb; M-Files-Versionierung nutzen |
| 4.11 | Kopie an Kunde | KI | Kundenportal, M365, DeepBox | Kanal gemäss SB: Kundenportal → Flag Kundenportal auf finaler StE setzen (Name der Eigenschaft offen, T11); E-Mail → E-Mail-Entwurf mit Kopie, Freigabe SB |
| 4.12–4.14 | Rücksendung und Abschluss | SEK / SB, KI | M-Files | Status «Physische ULA zurückschicken»; physischer Eingang markiert? ja → Aufgabe an Sekretariat, Unterlagen per Post zurück, Rücksendung bestätigt → «Abgeschlossen»; nein (nur digital) → KI setzt «Abgeschlossen» |

## Schritt 5 · Kontrolle Veranlagung und Steuerrechnung

- **Status:** ohne Workflow-Status · **Auslöser:** Eingang Veranlagung, Steuerrechnung, Nachfrage oder Auflage (meist per Post an consis)
- **Agent:** A9 Veranlagung · **Output:** Ablage, Kontrolle gegen eingereichte Deklaration, E-Mail an SB bei Abweichung, Veranlagung immer an den Kunden · Prozessbeschrieb S. 20, 21, 22, 23

| Nr. | Tätigkeit | wer | System | Regel / Detail |
|---|---|---|---|---|
| 5.1 | Dokumenttyp | KI | – | Veranlagung → 5.2; Nachfrage/Auflage → 5.4 E-Mail an SB mit Frist und Dokument-Link; Steuerrechnung allein (z.B. TG) → mit geprüfter Veranlagung verknüpfen → 5.3 |
| 5.2 | Kontrolle je Position | KI | – | eingereichte Deklaration und Veranlagung laden; Kontrolle je Position Kanton/Gemeinde und Bund, steuerbar und satzbestimmend, Einkommen, Vermögen, Abzüge, Schulden; Vergleichstabelle ablegen (Position, deklariert, veranlagt, Differenz) |
| 5.4 | Abweichung melden | KI | – | Jede Abweichung (auch CHF 1) und jede Nachfrage → E-Mail an zuständige SB gemäss M-Files (Entscheid 27.10.2026, T12). Betreff «Veranlagung [Jahr] Hans und Anna Muster – Abweichung CHF [Betrag]»; Inhalt: Kanton/Bund, Vergleichstabelle, Begründung Steueramt, Links auf beide Dokumente, Frist als Datum, Vorschlag KI. Aktuell zusätzlich an FE. |
| 5.5–5.7 | Entscheid SB | SB / ML | – | SB entscheidet: selbst intervenieren (klärt mit Kunde oder Steueramt) oder ML beiziehen; Einsprache nur ML / Steuerexperte, Frist gemäss Rechtsmittelbelehrung (in der Regel 30 Tage) |
| 5.3 | Steuerrechnung prüfen | KI | – | SG: Schlussrechnung liegt mit Veranlagung vor; TG: Rechnung folgt später, Veranlagung vorab weiterleiten; ZH, AR: für den Testlauf weggelassen (Rechnung einzeln prüfen nach dem Testlauf) |
| 5.8–5.9 | Veranlagung an den Kunden | KI / SB | – | immer, auch bei Übereinstimmung (Frage 27); Kanal gemäss SB: E-Mail-Entwurf mit Freigabe SB oder Flag Kundenportal; Fall erledigt, Protokoll; Zahlung: nur Indiz über Kontoauszug |

**Ablage:** Klasse «Veranlagung + def. Steuerrechnung» (Bund, Kanton/Gemeinde, Kapitalleistung), Nachfragen «Auflage/Buchprüfung», Einsprachen «Einsprache/Rekurs», Kontoauszüge «Kontoauszug». Antworten an das Steueramt nur SB oder ML.

## Schritt 6 · Provisorische Steuerrechnung

- **Status:** ohne Workflow-Status · **Auslöser:** Eingang provisorische Rechnung, Jahresbeginn, meist per Post an consis als Vertreterin
- **Agent:** A10 Provisorische Rechnung · **Output:** Schreiben «gutgeheissen» über die SB (Brief oder E-Mail gemäss SB) oder Meldung zur Detailprüfung · Prozessbeschrieb S. 24, 25

| Nr. | Tätigkeit | wer | System | Regel / Detail |
|---|---|---|---|---|
| 6.1 | Ablage | KI | – | Klasse «Prov. Steuerrechnung» (Bund, Kanton/Gemeinde, Kapitalleistung) |
| 6.2 | Werte lesen und vergleichen | KI | – | Einkommen und Vermögen aus provisorischer Rechnung lesen; Faktoren der zuletzt eingereichten StE laden |
| 6.3 | Entscheid | KI | – | Einkommen innerhalb ± 20'000 und Vermögen innerhalb ± 50'000? ja → 6.3b Entwurf «gutgeheissen» aus M-Files-Vorlage (Muster anderer Mandanten ohne deren Daten) → 6.4 Anfrage an SB Brief oder E-Mail → 6.5 SB entscheidet Kanal, prüft und versendet; nein → 6.3a Meldung an SB mit Vergleich und Differenzen → Detailprüfung SB/ML, evtl. Antrag auf Anpassung (nur SB/ML) |

**Regel:** Entscheid 27.10.2026 (Frage 31): Die provisorischen Rechnungen laufen immer über die SB. Ob Brief oder E-Mail, hängt von der SB bzw. vom Kunden ab – die KI fragt die SB an.

## Ablauf jeder KI-Aktion (gilt für alle Schritte)

1. Ereignis (neues Dokument, Statuswechsel, Zeitplan) → Orchestrator: Ereignis-ID, Mandant, Steuerjahr, zuständiger Agent
2. ML und SB in M-Files eingetragen? nein → Prüfkorb; ja → Empfänger für Meldungen, Freigaben, Aufgaben
3. Ereignis schon verarbeitet? ja → verwerfen, protokollieren
4. Lock auf Prozessobjekt (höchstens ein Agent gleichzeitig)
5. Agent bereitet Aktion vor → Aktion erlaubt? (Berechtigungsliste und Zustandsautomat) nein → Prüfkorb
6. Ergebnis sicher? nein → Prüfkorb (Grund, Vorschlag, Link); ja → Schreiben in M-Files, DrTax, Fristenliste oder Entwurf in M365
7. Protokoll: Zeit, Agent, Ereignis-ID, Mandant, Jahr, Aktion, alt → neu, Sicherheit, Ergebnis; Lock lösen
8. Tagesbericht an FE, Systemfehler sofort; Kill-Switch durch FE stoppt alle Agenten

## Agenten

| ID | Agent | Schritte | Auslöser |
|---|---|---|---|
| A1 | Eingang und Klassifizierung | 1, 4.2, 5.1, 6.1 | neues E-Mail, Portal- oder DeepBox-Dokument, Scan |
| A2 | Prozessobjekt (Status, Felder, Flags) | 1–4 | Ablage durch A1, Statuswechsel |
| A3 | Vollständigkeit und Kundenpendenzen | 2.4–2.7, 4.1–4.4 | Status «in Arbeit (St)», Nachlieferung |
| A4 | Erfassung DrTax | 2.2–2.9, 4.5 | Status «in Arbeit (St)» |
| A5 | Qualitätskontrolle | 2.10–2.15 | Erfassung abgeschlossen |
| A6 | Steuerberechnung und Entwurf | 2.16–2.18, 4.6 | QK abgeschlossen |
| A7 | Besprechungsprotokoll | 3.2–3.5 | Status «zur Kontrolle» |
| A8 | Fristen und Abschluss | 4.8–4.14 | Status «In Excel-Fristenliste austragen» (durch Mensch gesetzt) |
| A9 | Veranlagung | 5 | Eingang Veranlagung, Rechnung, Nachfrage |
| A10 | Provisorische Rechnung | 6 | Eingang provisorische Rechnung |

> Die Schrittnummern der Agententabelle (S. 27, z.B. A5 «2.10–2.15») stimmen nicht mit der Nummerierung der Schritttabelle 2.1–2.8 (S. 13) überein → mit FE klären.
