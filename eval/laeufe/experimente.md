# Experimente und Tuning (09.11.2026)

Ziel: herausfinden, was dem OpenClaw-Steuer-Agenten am meisten hilft, und das Wiki danach einstellen.
Umgebung: OpenClaw 2026.11.2, Agent-Modell Claude über die `claude-cli`-Runtime, Wiki installiert mit `openclaw/install.sh`.

## Beobachtung vorab: wie navigiert der Agent?

Auswertung der Claude-Code-Protokolle von 47 echten Agent-Turns (Lauf A): `read` 333×, `exec` (grep/cat/ls) 38×,
`memory_search` 9×, `memory_get` 1×. Der Agent arbeitet also überwiegend **dateibasiert** (Quick-Index → Quick-Seite →
Detail/Chunk), die semantische/Volltext-Suche ist Rückfallebene. Konsequenz: Struktur, Grösse und Verlinkung des
Quick-Layers sind der wichtigste Hebel; die Suchkonfiguration ist zweitrangig, aber nicht egal.

## E1 – Retrieval: welche Suchkonfiguration findet die Belegstellen?

Testset: 29 Fragen mit belegten Gold-Fundstellen (15 aus `eval/erwartet.yaml`, 14 aus dem Blindtest). Treffer = Ergebnis ist
der Gold-Chunk oder ein Quick-/Wiki-Abschnitt, der die Gold-Chunk-ID zitiert. Werkzeug: `eval/retrieval_test.py`.
Strenges Mass (nur die exakte Belegstelle zählt) – absolute Werte sind daher tief; relevant ist der Vergleich.

| Variante | Anfrage | Hit@1 | Hit@3 | Hit@5 | Hit@10 | MRR |
|---|---|---|---|---|---|---|
| eigene BM25 (`tools/search.py`) | ganze Frage | 0.07 | 0.21 | 0.28 | 0.34 | 0.16 |
| eigene BM25 + Glossar-Erweiterung | ganze Frage | 0.10 | 0.21 | 0.24 | 0.34 | 0.17 |
| OpenClaw FTS, Tokenizer trigram | ganze Frage | 0.14 | 0.24 | 0.41 | 0.52 | 0.23 |
| OpenClaw FTS, Tokenizer unicode61 | ganze Frage | 0.10 | 0.38 | 0.52 | 0.59 | 0.26 |
| OpenClaw FTS, trigram | Stichworte | 0.17 | 0.31 | 0.38 | 0.52 | 0.27 |
| OpenClaw FTS, unicode61 | Stichworte | 0.14 | 0.38 | 0.45 | 0.59 | 0.28 |
| **OpenClaw FTS, unicode61 + angereicherte Kontextzeile** | Stichworte | **0.24** | **0.41** | **0.52** | **0.59** | **0.36** |
| OpenClaw FTS, unicode61 + angereicherte Kontextzeile | ganze Frage | 0.14 | 0.41 | 0.41 | 0.59 | 0.28 |
| OpenClaw FTS, unicode61 + Kontextzeile + Kompakt-Wegleitung/Belegkarten (Stand Lauf B) | Stichworte | 0.21 | 0.41 | 0.45 | 0.55 | 0.33 |
| OpenClaw FTS, unicode61 + Kontextzeile + Kompakt-Wegleitung/Belegkarten (Stand Lauf B) | ganze Frage | 0.10 | 0.28 | 0.34 | 0.48 | 0.23 |
| Hybrid mit lokalen Embeddings (`provider: "local"`) | – | nicht getestet: Plugin `@openclaw/llama-cpp-provider` nötig, Installation in der Testumgebung durch die Sicherheitsrichtlinie blockiert | | | | |

Angereicherte Kontextzeile = erste Zeile jedes Chunks nennt Ebene und Kanton ausgeschrieben, z.B.
«Bund · Bundesebene (direkte Bundessteuer, Bundesrecht) · Rundschreiben · Steuerjahr 2026 · RS 2-215 …» statt «Bund · Steuerjahr 2026 · …».
Häufigster Fehler vorher: Treffer aus dem falschen Kanton/Jahr (z.B. «km-Ansatz 2026 direkte Bundessteuer» → TG-Chunks).

**Entscheide:** Tokenizer-Empfehlung von trigram auf Standard (unicode61) geändert; Kontextzeilen in `tools/chunk.py`
angereichert (alle Chunks neu erzeugt, IDs und Texte unverändert). Die zusätzlichen grossen Quick-Seiten (Kompakt-Wegleitung,
Belegkarten) senken das strenge Retrieval-Mass leicht (sie konkurrieren im Volltext mit den Chunks; Unterschied ≈ 1–2 Fragen
von 29, im Rauschbereich) – im Agentenlauf überwiegt ihr Nutzen deutlich (E2). Für reine Suchanwendungen ohne Agent kann man
`pattern: "chunks/**/*.md"` indexieren.

## Lauf A – Baseline im echten OpenClaw (unabhängig bewertet)

Details: [bewertung-A.md](bewertung-A.md). Blindtest 14/14 richtig; Praxistest 38/40 richtig (inkl. korrekt «nicht abgedeckt»),
2 teilweise (falsche Nebenaussagen); Fundstellen, Kanton/Bund-Trennung und Steuerjahr in 54/54 Antworten korrekt.
Mittlere Dauer je Frage ~40 s.

Daraus abgeleitetes Tuning: Hinweise zu Gebäudealter (Bund: zu Beginn der Steuerperiode) und Bundes-Kinderabzug
(Einkommen 6'800 **und** Steuerbetrag 263) direkt in die Eckwerte; Blindtest-Referenz b03 korrigiert (indexierte Beträge).

## E2 – Kompakt-Wegleitung und Tuning im Agenten-Lauf (Lauf B)

Lauf B = gleiche 64 Fragen, gleiches Modell und Bewertungsverfahren, aber Wiki mit: Zeitmodell, angereicherten Kontextzeilen,
Kompakt-Wegleitung je Formularposition (`quick/wegleitung-<kt>-<jahr>.md`), Tuning-Hinweisen aus Lauf A, Standard-Tokenizer.
Bewertung: [bewertung-A.md](bewertung-A.md), [bewertung-B.md](bewertung-B.md).

| Testset | Lauf | n | richtig | teilweise | falsch | Fundstellen ok | Ø Dauer s | Ø Tool-Aufrufe |
|---|---|---|---|---|---|---|---|---|
| Praxistest q01–q40 | A | 40 | 38 | 2 | 0 | 40 | 41.5 | 8.8 |
| Praxistest q01–q40 | B | 40 | 39 | 1 | 0 | 40 | 40.3 | 7.8 |
| Blindtest b01–b14 | A | 14 | 14 | 0 | 0 | 14 | 36.1 | 7.6 |
| Blindtest b01–b14 | B | 14 | 14 | 0 | 0 | 14 | 43.0 | 8.4 |
| Positionstest p01–p10 | A | 10 | 9 | 1 | 0 | 10 | 46.4 | 11.6 |
| Positionstest p01–p10 | B | 10 | 10 | 0 | 0 | 10 | 49.7 | 11.3 |

- **Genauigkeit:** A 61/64 voll richtig, B 63/64. Alle drei Teilfehler aus A sind in B behoben (Gebäudealter-Regel q32,
  Bundes-Kinderabzug q38, AR ohne Bundesspalte p09). Einziger Teilfehler in B: q37 – Mietvertrag als «nein (Normalfall)» statt
  «bedingt» eingestuft (Bedingungen aber genannt). Keine falsche Antwort in beiden Läufen; Fundstellen, Kanton/Bund-Trennung
  und Steuerjahr in 64/64 korrekt.
- **Navigation** (Claude-Code-Protokolle aller Turns): In B öffnet der Agent die Kompakt-Wegleitung 89× und braucht deutlich
  weniger Detailseiten (Zuordnungs-Detail 12× statt 34×) und Chunks (236 statt 289 Zugriffe); Lesezugriffe gesamt −11 %
  (425 statt 479), Tool-Aufrufe je Praxisfrage 7.8 statt 8.8.
- **Dauer:** unverändert ~40–50 s je Frage (B lief auf zwei Instanzen parallel; Zeiten daher nur grob vergleichbar).

**Entscheid:** Lauf-B-Konfiguration ist der Standard (install.sh nach `memory/`, Tokenizer unicode61, Kompakt-Wegleitung im
Quick-Layer und im Snippet/Skill als erste Station für Positionsfragen).

## E3 – Ende-zu-Ende: vollständige Steuererklärungen (Lauf B-Stand)

4 fiktive Haushalte (ZH, SG, TG, AR 2025; je 10 Belege inkl. Fallen und irrelevanter Belege), Musterlösung mit 109 Positionen
unabhängig aus Primärquellen. Der OpenClaw-Agent erstellt die komplette Ausfüllhilfe (3–4.5 min je Fall, 19–30 Tool-Aufrufe).
Ergebnis: **103/109 Positionen korrekt**; SG, TG, AR vollständig korrekt («einreichbar nach Kontrolle»), ZH 23/29 wegen einer
einzigen Ermessensannahme (Heimkehr über Mittag) mit Folgezeilen – korrekter Wert als Variante genannt. In TG fand der Agent eine
Pauschale, die die Musterlösung übersehen hatte. Details: [bewertung-faelle.md](bewertung-faelle.md). Tuning: Regel für unklare
Sachverhalte im Skill `steuererklaerung-np`. **Nachtest ZH nach Tuning:** alle Positionen korrekt (plus eine von der Musterlösung
übersehene zulässige Pauschale) → 4/4 Fälle «einreichbar nach Kontrolle».

## E4 – Schwaches Modell (Haiku) mit Plugin: Werkzeug statt Dateisuche

Ziel: Der Agent soll auch mit einem kleinen Modell schnell und sicher arbeiten. Modell: Haiku über die `claude-cli`-Runtime,
OpenClaw 2026.11.2. Gleiche Fragen und gleiches unabhängiges Bewertungsverfahren wie oben (Opus-Prüfer gegen Referenz und
Primärquellen); jede Antwort in einer frischen Sitzung (eindeutige Sitzungs-ID).

| Lauf | Konfiguration |
|---|---|
| H0 | Haiku, Wiki als Dateien im Workspace (wie Lauf B), ohne Plugin |
| H1 | Haiku + Plugin v1 (Skills, MCP-Werkzeug `steuer`) |
| H4 | Haiku + Plugin, firmenunabhängige Ablage (`KATEGORIEN.md`), Kanton-/Jahresregel im Einstieg |
| H5 | wie H4 + robustere Wortsuche, `formular`-Gerüst, Korrekturen aus der Ursachenanalyse von H4 (siehe unten) |

| Testset | H0 | H1 | H4 | H5 | H6 | H7 |
|---|---|---|---|---|---|---|
| Praxistest q01–q40 (richtig / teilweise / falsch) | 35 / 5 / 0 | 31 / 7 / 2 | 33 / 6 / 1 | 31 / 7 / 2 | **36 / 2 / 2** | 33 / 6 / 1 |
| Blindtest b01–b14 | 14 / 0 / 0 | 14 / 0 / 0 | 13 / 1 / 0 | 14 / 0 / 0 | 13 / 1 / 0 | 13 / 1 / 0 |
| Positionstest p01–p10 | 10 / 0 / 0 | 8 / 2 / 0 | 7 / 3 / 0 | **10 / 0 / 0** | **10 / 0 / 0** | 8 / 2 / 0 |
| Ablage + Ausfüllen a01–a08 | – | – | 6 / 2 / 0 | **8 / 0 / 0** | – | – |
| Eingehende Dokumente d01–d40 (Typ, relevant, Jahr, einreichen, Kategorie) | – | – | 34 / 4 / 2 | **40 / 0 / 0** | – | – |
| Vollständige Steuerfälle ZH/SG/TG/AR (109 Positionen korrekt) | – | – | 78 | 96 | 99 | **100** (SG 24/24, AR 31/31) |
| Ø Dauer je Frage / Ø Werkzeugaufrufe (Praxistest) | 38 s / 7.2 | 29 s / 4.0 | 28 s / 4.2 | 29 s / 3.5 | 27 s / 3.4 | 28 s / 3.6 |
| Ø Dauer / Aufrufe je vollständigem Fall | – | – | 182 s / 39 | 139 s / 22 | 153 s / – | 169 s / 24 |

H6 = Stand H5 + Korrekturen aus H5 (3a-Text, Hinweis bei Nur-Bund-Abfragen, Ausfüllregeln in `formular`); H7 = H6 + Rechner
`rechne` (Haiku ruft ihn bei 9/10 Positions-Rechenaufgaben und in allen 4 Fällen selbst auf; in H7 kein Rechenfehler mehr gemeldet).
Die Praxisfragen streuen über die Läufe um ±3 (31–36); stabil verbessert sind Positionen, Ablage, Dokumente und ganze Fälle.
Die Restfehler der Fälle in H7 (ZH Tarif-Freibetrag als Abzug, TG Bund-Selbstnutzungsabzug) gingen auf das Gerüst bzw. einen zu
knappen Bundestext zurück und sind danach korrigiert.

**H8 – Kantonskürzel am Fragenanfang** («TG: …», «AR: …»), nach Ergänzung im Einstieg (Kürzel ausgeschrieben) und Hinweis bei
Nur-Bund-Abfragen: die 11 Praxisfragen mit Kürzel je zweimal (22 Antworten) → 19 richtig, 2 teilweise, 1 falsch (H5–H7: 8–10 von 11
je Lauf). Hartnäckig bleibt nur q13 («TG: … (Kanton vs. Bund)?»): Haiku liest «Kanton vs. Bund» als Bundesfrage und sucht nur
Bundesquellen, obwohl die Werkzeugausgabe auf TG verweist – Grenze des kleinen Modells bei dieser Formulierung.
**H9 – Fälle ZH und TG nach den Korrekturen aus H7:** TG 24/25 «einreichbar nach Kontrolle» (Bund-Selbstnutzungsabzug jetzt
richtig; fehlt nur das formale Zwischentotal Ziff. 6), ZH 28/29 (einzig: Tarif-Nullstufe 159'000 vom Vermögen abgezogen →
Hinweis «kein Abzug im Formular» direkt am Eckwert ergänzt).
**H10–H12 – Endstand ganze Fälle:** ZH-Einzelläufe nach weiteren Gerüst-Korrekturen (Tarif-Nullstufe nicht abziehen, Werte je
Abzug zusammengefasst): Vermögen jetzt richtig. Endlauf H12 (alle 4 Fälle): **94/109** – TG 24/25 (einreichbar), AR 30/31,
ZH 23/29, SG 17/24. Je Fall ein Grundfehler mit Folgefehlern: SG Bruttolohn statt Nettolohn (Daten korrekt, Modellfehler),
ZH Verpflegung beim Bund doppelt halbiert (Datentext «halber Abzug» danach präzisiert), AR Person 2 unter Ziff. 10.1 statt 10.2.
Danach Ausfüllregel «Nettolohn = Lohnausweis Ziff. 11; Person 1/2 je eigene Ziffer» ergänzt (nicht mehr gemessen).

**H13 – zwei Haiku-Läufe nach allen Korrekturen** (u.a. Ausfüllregeln Nettolohn/Person 1–2, «halber Abzug» präzisiert,
Werte je Abzug zusammengefasst, Tarif-Nullstufen nicht als Abzug): ganze Fälle **108/109** (ZH 29/29, SG 24/24, AR 31/31, TG 24/25;
4/4 «einreichbar nach Kontrolle») und **107/109** (ZH, SG, AR fehlerfrei; TG 23/25). Restfehler: TG Zwischentotal Ziff. 6 nicht
ausgewiesen (formal), unbelegte Nebenbemerkungen zu 3a-Vermögen (danach Ausfüllregel mit Fundstellen). Kürzelfragen q16/q24 2/2
richtig, q13 («TG: … (Kanton vs. Bund)?») bleibt bei Haiku falsch (Rückfrage nach dem Kanton trotz Kürzel).

**S1 – Sonnet mit demselben Plugin:** ganze Fälle 105/110 – ZH 29/29, SG 24/24, TG 25/25 (je «einreichbar nach Kontrolle»),
AR 27/32: Sonnet machte eine zulässige Vermögensverwaltungspauschale geltend, die der Musterlösung fehlte (Prüfer: Musterlösung
unvollständig; Abweichung nur in deren Berechnung). Positionen 9/10, Blindtest 13/14 (b06 wie Haiku: Fristerstreckung nach
Fristablauf → danach in den Daten ergänzt).

**Gesamtbild ganze Fälle mit Haiku:** 78 (H4) → 94–100/109 in fünf Läufen (H5 96, H6 99, H7 100, H12 94). Die Streuung kommt
davon, dass Haiku pro Lauf an wechselnden Stellen einen Grundfehler macht, der sich durch die Totale zieht; AR und TG sind
meist «einreichbar nach Kontrolle». Für komplette Erklärungen bleibt die Kontrolle durch die Fachperson nötig (Plausibilität
Kanton/Bund, Totale); ein grösseres Modell (Lauf B/E3) lag bei 109/109 nach Tuning.
Bewertungen: `bewertung-haiku-H5.md`, `-H6.md`, `-H7.md`; Protokolle `haiku-H5-*.md` bis `haiku-H7-*.md`.

Lesart: Mit Plugin arbeitet Haiku rund 25 % schneller und mit halb so vielen Aufrufen wie mit Dateisuche (H0). Ab H5 sind
Positionsfragen, Ablage, Dokumente und ganze Fälle klar besser als H4; die Praxisfragen liegen im Bereich der Streuung
(31–35 richtig). Die verbleibenden Fehler in H5 sind überwiegend Modellfehler bei korrekter Werkzeugausgabe: Rechenfehler
(150'000 + 20'000 = 190'000), Kanton «TG:» am Fragenanfang übergangen, Chunk-Aussage falsch wiedergegeben, unbelegte
Nebenbemerkungen. In den ganzen Fällen: ein selbst angenommener Sachverhalt (Heimkehr über Mittag → Verpflegung gestrichen,
ZH) und eine nicht angewendete Kantonspauschale (SG) – beide mit Folgefehlern; danach als Ausfüllregeln in `formular` ergänzt.

**Ursachenanalyse H4** (19 nicht voll richtige Antworten, je ein unabhängiger Analyst mit Protokoll der Werkzeugaufrufe; jede
vorgeschlagene Datenkorrektur von einem zweiten Agenten gegen die Primärquelle geprüft): Werkzeugausgabe unvollständig/irreführend 7,
Stichwort nicht gefunden 3, Anleitung 3, falsche Daten 2, Modellfehler trotz korrekter Ausgabe 4. In allen Protokollen H0–H4 lieferten
`wert` 10 % und `position` 19 % der Aufrufe nichts – der Agent fragte mit Alltagswörtern und Komposita («Kinderabzug»,
«Sparzinsen», «Kinderdrittbetreuung») oder mit Hilfsblatt-Ziffern («2.3», «Form. 360»). Ein leerer `wert`-Treffer führte in q09 über die
Volltextsuche zu einem überholten Verordnungswert.

**Werkzeugtest** (`eval/werkzeug_test.py`, deterministisch, Treffer unter den ersten 3):

| Testsatz | alter Stand | neuer Stand |
|---|---|---|
| Echte Fehlgriffe aus den Protokollen + Prüffälle der Analyse (`werkzeug-test.yaml`) | 11/46 | 46/46 |
| Holdout 1: 385 Eingaben unabhängiger Agenten (2025) | 75 % | 98 % (zum Ableiten allgemeiner Regeln benutzt) |
| Holdout 2: 270 Stichworte aus Kundenfragen (2026), nach dem Tuning erzeugt | 72 % | 95 % (danach mit Äquivalenzen 98 %) |

Änderungen: Komposita (Bestimmungs-/Grundwort, Fugen-s, allgemeine Wortteile wie «-beiträge», «-frist»), Synonyme auch für
Formularpositionen, gleichbedeutende Wörter (Velo/Fahrrad, Auto/Motorfahrzeug), Ziffern/Codes/Artikel (`Ziff. 16.6`, `Code 220`,
`Art. 36 DBG`, `Form. 360`), Rückfall auf Formularposition + Volltext statt leerer Ausgabe; neuer Befehl `formular` (alle Positionen in
Formularreihenfolge, Limiten Kanton|Bund, Standardabzüge nach Haushalt); `zeige` nennt die Geltung der Quelle; Verfahrensdokumente
ausdrücklich «kein Steuerbeleg»; Kategorie-Regel im Einstieg. Dokumenterkennung (`ablage`) unverändert: 46/46, Holdouts 93–98 % Top-1.

## Grenzen der Experimente

- Zwei Modellgrössen (Claude über claude-cli: grosses Modell in A/B/E3, Haiku in E4); andere Modelle können anders navigieren.
- Haiku-Läufe streuen von Lauf zu Lauf (gleiche Frage, andere Werkzeugwahl); Unterschiede von 1–3 Antworten sind teils Rauschen.
- Hybrid-/Vektorsuche nicht getestet (lokales Embedding-Plugin in der Testumgebung blockiert, kein Embedding-API-Schlüssel).
- 64 Fragen und 4 Fälle sind eine Stichprobe; Fragen, Musterlösungen und Bewertungen stammen von KI-Agenten (unabhängig
  voneinander, gegen Primärquellen) – eine Abnahme durch eine Fachperson (Status ✅, `tools/abnahme.py`) steht aus.
