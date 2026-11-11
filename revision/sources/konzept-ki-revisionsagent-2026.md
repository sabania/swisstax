---
id: konzept-ki-revisionsagent-2026
kurz: Konzept KI-Revisionsagent
titel: Konzept KI-Revisionsagent (consis, 26.10.2026) – Grundlage Testphase 1
typ: intern
rang: 5
raw: raw/konzept-ki-revisionsagent-2026.docx
sha256: c2ae49678a100dd8ee347195f5042d14a96456bd58bfad3a8599c5cd68f9b0e3
---
# Konzept KI-Revisionsagent (consis, 26.10.2026) – Grundlage Testphase 1

## Konzept KI-Revisionsagent
Oct 26, 2026 · @Flo
### Übergabe an den AI-Partner
Dieses Konzept ist die fachliche Grundlage für die Umsetzung des KI-Revisionsagenten in der Testphase 1. Es ergänzt das Pflichtenheft um den Abgleich mit revio 4.0, die Architektur und die offenen Entscheide; bei Widersprüchen gilt das Pflichtenheft.
| Rolle | Verantwortung |
|---|---|
| consis (fachlich, FE) | Pflichtenheft, fachliche Entscheide, Testmandat mit Belegen, Abnahme der Testphase |
| enco (Technik) | Klärung mit dem Hersteller revio, Windows-Arbeitsplatz für den Agenten, Zugang zu revio Server und M-Files, Berechtigungen |
| AI-Partner (Umsetzung) | Aufbau des Agenten gemäss Pflichtenheft und Konzept, Machbarkeitstest, Testbetrieb, Protokollierung |

Beilagen
- Pflichtenheft «KI-Revisionsagent Testphase 1», Stand 20. Oktober 2026
- Revisionsakte revio 4.0 (Vorlage MUSTER AG, PDF, 185 Seiten)
- Katalog aller 538 Prüfschritte mit Kennzeichnung EP/WP und Prüfzielen (Anhang H, wird separat übergeben)
- Screenshots revio 4.0: Bereich 10 «Unterlagen zum Abschluss» und Notizen-Übersicht
### Auf einen Blick
Der KI-Revisionsagent bereitet eine eingeschränkte Revision in revio 4.0 und M-Files so weit vor, dass der Wirtschaftsprüfer nur noch kontrolliert, beurteilt und visiert. Er setzt nie ein Visum, schliesst nichts ab und gibt nichts frei.
- Aufbau: Ein Orchestrator führt das Mandat und steuert sechs Teil-Agenten entlang der Prozesse 1–6 des Pflichtenhefts. Der Zugriff auf revio 4.0, M-Files und E-Mail läuft über einen Dienstbenutzer ohne Visums- und Freigaberecht.
- Prüfprogramm: revio 4.0 hat 29 Prüffelder mit 538 Prüfschritten. Jeder Schritt trägt Prüfziele und die Kennzeichnung EP (Einzelfallprüfung) oder WP (Wirtschaftsprüfer).
- Pflichtenheft passt zu revio 4.0: Die Wesentlichkeit liegt unter 3.3, die Protokolle unter 10.9 «Unterlagen zum Abschluss».
- Wichtigster offener Entscheid: Darf der Agent WP-Schritte vorbereiten? Davon hängt auch das Pflichtenheft-Beispiel G1-305 ab.
- Nächster Schritt: Für revio ist keine API dokumentiert; Herstelleranfrage stellen und die Bedienung über die Oberfläche an einem Testmandat erproben, dann zuerst nur lesend testen.
### Ausgangslage
Grundlage sind das Pflichtenheft «KI-Revisionsagent Testphase 1» (Stand 20. Oktober 2026) und die Revisionsakte in revio 4.0. revio 4.0 wird ab 1. Januar 2027 eingesetzt; erste Revisionen sind bereits darin erfasst.
Das Pflichtenheft ist fachlich stark: Die Grenzen sind klar (kein Visum, keine Buchung, keine Freigabe), die kritische Grundhaltung ist verankert, und fehlende Daten dürfen nicht erfunden werden. Für einen Agenten müssen Formulierungen wie «risikoorientiert» oder «unter Berücksichtigung der Wesentlichkeit» aber in prüfbare Regeln übersetzt werden, sonst fällt das Ergebnis je nach Lauf anders aus.
Die Verweise des Pflichtenhefts stimmen mit revio 4.0 überein: Wesentlichkeit unter Planung 3.3, Protokolle unter 10.9. Die frühere Version revio 3.9 ist für dieses Konzept nicht mehr massgebend.
### Die Revisionsakte in revio 4.0
Der Agent arbeitet schreibend nur in den Prüffeldern (Bereich 4) und in den Unterlagen zum Abschluss (Bereich 10). Alle anderen Bereiche liest er höchstens, um seine Arbeit risikoorientiert und kritisch auszurichten.
| Bereich | Inhalt | Rolle des Agenten |
|---|---|---|
| 1 Jahresrechnung und Finanzcockpit | 1.1 Bilanz, Erfolgsrechnung, Anhang, Antrag VR; 1.2 Kennzahlen und Dashboard; 1.3 Spezialauswertungen; HB I / HB II | Import (Prozess 1); Kennzahlen für die Analytik |
| 2 Vorbereitung | 2.1 Tätigkeit und Umfeld, 2.2 Auftragsannahme und Weiterführung, 2.4 Auftragsvoraussetzungen und Unabhängigkeit | nur lesen (Empfehlung) |
| 3 Planung | 3.1 Risikobeurteilung pro Prüffeld, 3.2 Abschlussanalyse, 3.3 Wesentlichkeit, 3.4 Going concern, 3.5 Strategische Planung (Prüfungstiefe, Priorität, zugewiesene Mitarbeiter), 3.6 Auftragsteam | nur lesen; 3.3 gemäss Pflichtenheft |
| 4 Abschlussprüfung | 29 Prüffelder A1 bis T1, je mit Kontenübersicht, Prüfschritten und Abschliessender Beurteilung | Kernarbeit (Prozess 2) |
| 6 Beendigung | 6.1 Nicht nachgebuchte Fehler, 6.2 Abschliessende analytische Prüfungen, 6.3 Ereignisse nach dem Bilanzstichtag und Going concern, 6.4 Risiko-Dashboard | nur lesen; 6.2 als Leitfaden für die Plausibilisierung |
| 7 Berichterstattung | 7.1 Berichtsstrategie, 7.4 Versandfiche, 7.5 Berichtskritik | nur lesen; Vorgabe für den GVB-Entwurf |
| 9 Qualitätssicherung | 9.0 Abschliessende Beurteilung, Archivierungsreife, Schlussvermerk | keine |
| 10 Unterlagen zum Abschluss | Dokumenteneingang, 10.1 Saldenbilanz, 10.2 Umbuchungsliste, 10.3 Stille Reserven, 10.4 Jahresrechnung und Vollständigkeitserklärung, 10.5 Berichtsablage, 10.6 Korrespondenz, 10.9 Protokolle, 10.10 PBC-Liste, 10.11 Kundenbefragung | Prozess 3 (Protokoll in 10.9); Vorschläge für die PBC-Liste; Antworten aus 10.11 auswerten |

#### Notizen-Übersicht
revio 4.0 führt Notizen in vier Kategorien; dort erfasst der Agent alles, was das Pflichtenheft «unter Notizen» verlangt. Notizen löscht oder erledigt er nie.
| Kategorie | Was der Agent dort erfasst |
|---|---|
| Pendenz | Fehlende Unterlagen, ungeklärte Sachverhalte, nicht verfügbare Belege mit Konto, Datum und Betrag |
| Wesentliche Feststellungen | Hinweise auf mögliche Fehler und begründete Buchungsvorschläge (keine Verbuchung) |
| Schlussbesprechung | Punkte, die der Wirtschaftsprüfer mit dem Kunden besprechen sollte |
| Review | keine; für Rückmeldungen des Wirtschaftsprüfers |

Notizen können Beilagen erhalten («Neue Beilage»); der Agent hängt dort die verwendeten Nachweise an, wenn sie nicht direkt beim Prüfschritt liegen.
#### Aufbau eines Prüfschritts
- Nummer und Typ: 1xx Befragung, 2xx Analytische Prüfungshandlungen, 3xx Detailprüfungen, 4xx Sonstige Prüfungshandlungen.
- Prüfziele: pro Schritt hervorgehoben; der Agent hält im Textfeld fest, welche Prüfziele sein Nachweis abdeckt. EX Vorhandensein/Bestand (Existence), VO Vollständigkeit (Completeness), EN Eintritt (Occurrence), RV Rechte und Verpflichtungen, BE Bewertung, PA Periodenabgrenzung (Cut-off), DO Darstellung und Offenlegung; RI vermutlich Richtigkeit/Genauigkeit (zu bestätigen).
- Kennzeichnung: EP = Einzelfallprüfung, WP = Wirtschaftsprüfer.
- Textfeld für Feststellungen, Fundstelle und Umfang: Hier dokumentiert der Agent.
- Visum (Kürzel und Datum) pro Schritt, ✓ pro Prüffeld, «Abgeschlossen» und «Review» in der Fusszeile, Status in Bereich 10: alles bleibt beim Menschen.
### Architektur des Agenten
Ein Orchestrator hält den Mandatskontext fest und ruft pro Prozess einen Teil-Agenten auf; alle Zugriffe laufen über eine Werkzeugschicht mit eng begrenzten Rechten.
Architektur KI-Revisionsagent · Orchestrator, 6 Teil-Agenten, Werkzeugschicht
- Orchestrator mit Teil-Agenten. Teil-Agenten für Import, Prüfschritte, Unterlagen 10.9, Rapport, GVB-Bericht und PDF-Akte. Die Prüfschritte laufen über eine generische Schleife je Schritttyp; für wichtige Positionen kommen Playbooks dazu (zuerst Vorjahresabstimmung, C1 Delkredere, G1 Sachanlagen).
- Harter Mandatskontext. Zu Beginn wird ein Kontext-Schlüssel fixiert: Kunde, revio-Mandat, M-Files-Kunde, Geschäftsjahr und Stichtag. Jeder Zugriff und jede Ablage wird dagegen geprüft; bei Abweichung bricht der Agent ab und erfasst eine Pendenz.
- Werkzeugschicht.
- revio 4.0: In den Unterlagen ist keine API dokumentiert; erwähnt sind nur Datenraum, Online-Interaktion mit Mandanten und künftig XBRL für Jahresrechnungen. revio 4.0 ist eine Client-Server-Lösung: zentraler revio Server (Backend, Datenbank MongoDB) und nativer Windows-Client (Windows 10/11, Installation per MSIX). Der Client spricht über eine interne Schnittstelle mit dem Server; ob diese Schnittstelle oder ein lesender Datenbankzugriff offiziell genutzt werden darf, wird beim Hersteller geklärt und wäre robuster als die Oberfläche. Direktes Schreiben in die Datenbank ist ausgeschlossen, weil es Anwendungslogik, Historie und Support umgeht. Bis dahin wird mit Oberflächenautomation geplant: Der Agent bedient revio auf einem eigenen Windows-Arbeitsplatz (z. B. virtuelle Maschine) mit eigenem revio-Benutzer wie ein Mitarbeiter über Bildschirm, Maus und Tastatur. Das ist langsamer und bei Updates anfälliger; Updates werden deshalb auf dem Agenten-Arbeitsplatz erst nach einem Test eingespielt. PDF-Import, Kontenzuordnung, Textfeld pro Schritt, Notizen, Belegablage, Bereich 10 und PDF-Akte sind einzeln auf Machbarkeit zu testen.
- M-Files: REST-API, Suche über Metadaten (Kunde, Geschäftsjahr, Klasse) statt Volltext.
- Rechenmodul: Bilanzgleichheit, Totale, Vorjahresdifferenzen, OP-Altersstruktur, Delkredere und Kennzahlen laufen in Code, nicht im Sprachmodell.
- Dokumentenmodul: GVB-Kopien in Word erstellen und aktualisieren, ohne die Formatierung zu zerstören.
- E-Mail: in der Testphase nur Entwurf oder Versand an eine fixe WP-Adresse, nie an Kunden.
- Wissensschicht. Interne Prüfungsanweisungen, SER, Wesentlichkeitsmethodik und Muster-Arbeitspapiere als durchsuchbare Wissensbasis; Lizenz für HWP und SER vorher mit EXPERTsuisse klären.
- Leitplanken technisch erzwungen. Eigener Dienstbenutzer in revio 4.0 und M-Files ohne Recht für Visum, Abschlussstatus, Freigabe und Kundenversand; Löschrechte eingeschränkt. Optional wird der Agent in 3.5 als eigener «zugewiesener Mitarbeiter» geführt, damit seine Arbeit sichtbar ist.
- Einheitliches Ergebnis pro Prüfschritt. Prüfziel, Quellen (M-Files-ID und Version), Auswahl und Umfang mit Begründung, Ergebnis, Feststellungen, Pendenzen und Status. Daraus entsteht der Revisionsrapport automatisch.
- Protokoll (Audit Trail). Jede Aktion, Quelle, Berechnung und jeder Fehler mit Zeitstempel, abgelegt pro Mandat und Jahr in M-Files.
- Menschliche Kontrollpunkte. In der Testphase ein Halt nach dem Import, weil eine falsche Kontenzuordnung alle Folgeprüfungen verfälscht.
### Ablauf einer Revision
Der Agent arbeitet die Prozesse 1 bis 5 der Reihe nach ab; der Wirtschaftsprüfer erteilt den Auftrag, kontrolliert und entscheidet. Die PDF-Akte (Prozess 6) entsteht nur auf seine Anweisung.
Ablauf einer Revision · 6 Prozesse des Agenten, 5 Entscheide des Wirtschaftsprüfers
Gestrichelt ist der Halt nach dem Import, der nur in der Testphase gilt. Alles, was der Agent nicht klären kann, erfasst er als Pendenz und meldet es im Rapport.
### Prozesse 1–6 in revio 4.0 und M-Files
Jeder Prozess des Pflichtenhefts hat in revio 4.0 einen festen Ort; die Grenze des Agenten ist überall dieselbe: vorbereiten ja, abschliessen nie.
| Prozess | Ort | Was der Agent tut | Grenze |
|---|---|---|---|
| 1 Import Jahresrechnung | M-Files → revio 1.1 | Definitive Bilanz und ER in M-Files suchen, per PDF-Import einlesen, Vorzeichen der Passiven prüfen, Konten zuordnen, Bilanzgleichheit und Totale abstimmen | Unklare Zuordnungen als Pendenz; Halt zur Kontrolle (Testphase) |
| 2 Markierte Abschlussprüfungen | revio 4 Prüffelder | Prüfschritte nach Typ bearbeiten, Nachweise aus M-Files beschaffen, Ergebnis im Textfeld dokumentieren, Belege ablegen, Notizen erfassen | Kein Visum, kein ✓, keine Abschliessende Beurteilung |
| 3 Unterlagen zum Abschluss | revio 10.9 | Protokoll Vorjahr aus M-Files beschaffen, Zugehörigkeit prüfen, ablegen; fehlende Unterlagen als Vorschlag für die PBC-Liste (10.10) | Status bleibt offen; Anforderung beim Kunden durch den Menschen |
| 4 Revisionsrapport | E-Mail an den Wirtschaftsprüfer | Status aller Schritte (vorbereitet, mit Feststellungen, teilweise, nicht bearbeitet), offene und wesentliche Punkte zuerst, Verweis auf Schritt und Notiz | Nur an die freigegebene WP-Adresse |
| 5 GVB-Revisionsbericht | M-Files | Vorjahres-Deckblatt und -Berichtstext kopieren, Jahreszahlen, Stichtage und Jahresergebnis aktualisieren, gegen 7.1 Berichtsstrategie und 7.5 Berichtskritik prüfen | Keine Unterzeichnung, keine Datierung; Vorjahresoriginale unverändert |
| 6 PDF-Akte | revio → M-Files | Nur auf Anweisung: PDF-Akte erzeugen, prüfen, in M-Files ablegen (Klasse «Revision», Kategorie «Arbeitspapiere», Bezeichnung «AP revio») | Nichts überschreiben; Ablage mit Speicherort bestätigen |

### Bearbeitung der Prüfschritte
Der Agent behandelt jeden Prüfschritt nach demselben Ablauf und passt nur die Art der Arbeit an den Schritttyp an. Ablauf je Schritt: Ziel und Prüfziele lesen → Risiko und Strategie aus 3.1 und 3.5 berücksichtigen → Nachweise in M-Files beschaffen → Umfang nach Wesentlichkeit festlegen → prüfen → im Textfeld dokumentieren → Notizen erfassen → Visum offen lassen.
| Typ (Nummer) | Anzahl | davon EP | davon WP | Umsetzung durch den Agenten |
|---|---|---|---|---|
| Befragung (1xx) | 106 | 80 | 12 | Kann nicht selbst befragen: wertet schriftliche Antworten aus (z. B. 10.11 Kundenbefragung), sonst Frage als Pendenz; höchstens «teilweise bearbeitet» |
| Analytische Prüfungshandlungen (2xx) | 64 | 40 | 5 | Gut automatisierbar über Kontenübersicht, Kennzahlen 1.2 und Rechenmodul |
| Detailprüfungen (3xx) | 227 | 58 | 70 | Automatisierbar, wenn Belege in M-Files liegen; 320 Anhang, 321 stille Reserven und 322 Dauerakten wiederholen sich |
| Sonstige Prüfungshandlungen (4xx) | 141 | 2 | 0 | Weitergehende Handlungen (Bestätigungen, Inventur, Gutachten, Journal Entry Testing); nur auf Anweisung, physische Tätigkeiten nie |
| Total | 538 | 180 | 87 |  |

EP-Schritte (Einzelfallprüfung) sind der Kern der Agentenarbeit. Ob der Agent auch WP-Schritte (Wirtschaftsprüfer) vorbereitet oder auslässt, ist der wichtigste offene Entscheid.
#### Beispiele des Pflichtenhefts
| Beispiel | Hauptschritt | Zugehörige Schritte |
|---|---|---|
| Abstimmung Vorjahresbestände | A1-302 (EP) | A1-303 Saldi Hauptbuch (EP); P1-302 Reserven und Bilanzergebnis (EP) |
| C1 Delkredere | C1-302 (EP) | 101 OP-Liste (EP), 104 Wertberichtigungen, 202 Altersstruktur (EP), 207 Kennzahlen, 208 Verluste und Rabatte (WP), 304 Zahlungen nach Stichtag (WP), 309, 310, 303 und 321 stille Reserven |
| G1 Einkaufsfakturen | G1-305 (WP) | 301 Anlagespiegel (EP), 302 Inventarliste (EP), 403 Aktivierungsfähigkeit |

### Wesentlichkeit gemäss 3.3
Der Agent liest die Wesentlichkeit aus 3.3 und ändert sie nie; er wendet die Werte je nach Zweck unterschiedlich an. revio 4.0 berechnet sie aus einer gewählten Bezugsgrösse, einem Prozentsatz und einer Begründung.
- Toleranzwesentlichkeit (75 %): steuert Prüfumfang und Stichprobe.
- Nicht-Aufgriffsgrenze (5 %): Differenzen darunter werden nur protokolliert.
- Gesamtwesentlichkeit: Massstab für Wesentliche Feststellungen; die Summe der nicht korrigierten Fehler beurteilt der Mensch in 6.1.
- Qualitative Faktoren und besondere Umstände: Wenn erfasst, meldet der Agent auch kleinere Abweichungen.
- Plausibilität der Festlegung: Passen Bezugsgrösse, Prozentsatz und Begründung nicht zusammen, erfasst der Agent eine Pendenz.
- Änderung der Werte: Betroffene Prüfschritte werden neu beurteilt und im Rapport gekennzeichnet.
### Offene Entscheide
Acht Punkte müssen vor der Umsetzung entschieden werden, weil der Agent sonst raten müsste; der erste betrifft den Kern der Agentenarbeit. Buchungsvorschläge sind bereits geregelt: als Notiz, ohne Verbuchung (Pflichtenheft).
| Thema | Offene Frage | Zuständig |
|---|---|---|
| WP-Schritte | Darf der Agent WP-Schritte (Wirtschaftsprüfer) vorbereiten, oder lässt er sie aus? Welche Schritte gelten als «markiert» im Sinne des Pflichtenhefts? G1-305 ist WP gekennzeichnet. | consis |
| Stichprobenauswahl | Bei consis gilt pflichtgemässes Ermessen des Prüfers, keine feste Regel. Vorschlag: Der Agent wählt standardmässig alle Posten über der Toleranzwesentlichkeit, ungewöhnliche Posten (Vorzeichen, runde Beträge, Stichtagsnähe, nahestehende Personen) und einige weitere nach Risiko aus 3.1, begründet die Auswahl im Textfeld und übernimmt Vorgaben des Wirtschaftsprüfers pro Mandat oder Prüffeld. Zu bestätigen: Standardauswahl und wo der Wirtschaftsprüfer seine Vorgabe erfasst. | consis |
| Delkredere (C1) | Betriebswirtschaftliche Herleitung oder steuerlich akzeptierte ESTV-Pauschale? Umgang mit stillen Reserven (C1-303, C1-321)? Ab welchem Alter gilt eine Forderung als «alt»? | consis |
| Statusdefinitionen | Ab wann ist ein Schritt «vorbereitet» statt «teilweise bearbeitet», insbesondere bei Befragungen? | consis |
| GVB-Bericht (Prozess 5) | Nur Normalwortlaut gemäss 7.1? Vorgehen bei Einschränkung, Zusatz (z. B. Überschuldung, Rangrücktritt) oder Hinweis. | consis |
| E-Mail-Versand (Prozess 4) | Wer gibt was frei? Welche Empfängeradresse, welche Anhänge? | consis, technisch enco |
| Vorzeichen Passiven (Prozess 1) | Importoption in revio 4.0 oder Zwischenschritt über Excel? | enco mit revio |
| Datenschutz und Berufsgeheimnis | Datenstandort, Auftragsbearbeitungsvertrag, kein Training mit Mandantendaten, revDSG, Schweigepflicht nach Art. 730b OR; vor dem ersten Test mit Echtdaten regeln. | consis mit enco und AI-Partner |

### Benötigte Informationen
Der Aufbau von revio 4.0 ist bekannt; offen sind vor allem der technische Zugriff, die Hausregeln und weitere Testmandate.
#### A. revio 4.0
- ☒ Revisionsakte revio 4.0 (29 Prüffelder, 538 Schritte; EP = Einzelfallprüfung, WP = Wirtschaftsprüfer)
- ☒ Wesentlichkeit 3.3, Bereich 10 Unterlagen zum Abschluss (inkl. 10.9) und Notizen-Übersicht bekannt
- ☐ Bedeutung des Prüfzielkürzels RI bestätigen (die übrigen sieben sind geklärt)
- ☐ enco klärt: Herstelleranfrage an revio: API oder andere Automationsschnittstelle, offizielle Nutzung der Client-Server-Schnittstelle oder lesender Zugriff auf die MongoDB, Importformate (Excel/CSV, XBRL), Testumgebung, Dienstbenutzer mit eingeschränkten Rechten, Steuerung der MSIX-Updates (in den Unterlagen ist keine API dokumentiert); dazu Bildschirmaufnahme von Import, Zuordnung, Textfeld, Belegablage, Notiz und PDF-Akte
- ☐ enco klärt: Windows-Arbeitsplatz für den Agenten bereitstellen (z. B. virtuelle Maschine mit Windows 10/11 in Standardausstattung, Zugang zum revio Server), revio 4.0 per MSIX installieren, eigener revio-Benutzer und Zugriff auf M-Files
- ☐ Entscheid Leserechte: zusätzlich 2.1, 2.4, 3.1, 3.4, 3.5 und 6.2
- ☐ Entscheid, ob der Agent in 3.5 als eigener «zugewiesener Mitarbeiter» geführt wird
#### B. M-Files
- ☐ enco klärt: Version, Cloud oder On-Premises, verfügbare API
- ☐ Metadatenstruktur: Klassen, Kategorien, Eigenschaften für Kunde und Geschäftsjahr
- ☐ Typische Dokumentbezeichnungen mit Beispielen (Bilanz/ER Definitiv, OP-Listen, Anlagenbuchhaltung, Protokolle, GVB-Vorlagen), auch unsaubere Ablagen
- ☐ enco klärt: Berechtigungskonzept und Möglichkeit eines Dienstbenutzers
#### C. Fachliche Grundlagen
- ☐ Interne Prüfungsanweisungen und Hausregeln (Delkredere); Stichproben nach pflichtgemässem Ermessen, Standardauswahl des Agenten bestätigen
- ☐ 2–3 Muster-Arbeitspapiere in guter Qualität pro Beispielprüfschritt
- ☒ GVB-Deckblatt und Berichtstext: Vorlagen vorhanden, werden für den produktiven Agenten bereitgestellt
- ☐ Lizenzsituation für HWP und SER
#### D. Testmandate
- ☐ Testmandat inkl. Belege liegt vor (Stand 26.10.2026); weitere 1–2 Testmandate für den Vergleich mit der Arbeit des Revisors
- ☐ Mindestens ein schwieriger Fall mit Belegen in M-Files: fehlende Belege, Differenzen zum Vorjahr, alte Debitoren
#### E. Prozesswissen
- ☐ Bildschirmaufnahme eines Revisors, der ein Mandat bearbeitet und dabei laut mitdenkt
- ☐ Häufige Fehler und Stolpersteine aus der Praxis
#### F. Governance
- ☐ Verantwortliche Personen in Wirtschaftsprüfung und IT
- ☐ Abnahmekriterien: Wann gilt die Testphase als bestanden?
- ☐ Aufbewahrung der Agenten-Protokolle
### Vorgehen
Zuerst die technische Machbarkeit klären, dann lesend testen und erst danach schreibend arbeiten lassen.
- Machbarkeit Technik: enco klärt die Herstelleranfrage an revio (API, Importformate, Testumgebung) und den Zugriff auf M-Files. Ohne API vorab ein kurzer Machbarkeitstest der Oberflächenautomation: Import, Textfeld, Notiz und Belegablage an einem Testmandat.
- Entscheide treffen: consis entscheidet über WP-Schritte, Standardauswahl der Stichprobe, Delkredere und Statusregeln (siehe Offene Entscheide).
- Nur lesend testen: Der Agent bearbeitet ein Testmandat, schreibt den Rapport, legt aber nichts in revio oder M-Files ab. Sein Ergebnis wird mit der Arbeit des Revisors verglichen.
- Schreibend testen: Textfelder, Notizen, Belegablage, 10.9 und GVB-Kopien.
- Playbooks ausbauen: priorisiert nach Häufigkeit und Risiko der Prüfschritte, beginnend mit den EP-Schritten.
