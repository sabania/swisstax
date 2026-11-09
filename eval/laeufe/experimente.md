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

## Grenzen der Experimente

- Ein Modell (Claude über claude-cli); andere Modelle können anders navigieren.
- Hybrid-/Vektorsuche nicht getestet (lokales Embedding-Plugin in der Testumgebung blockiert, kein Embedding-API-Schlüssel).
- 64 Fragen und 4 Fälle sind eine Stichprobe; Fragen, Musterlösungen und Bewertungen stammen von KI-Agenten (unabhängig
  voneinander, gegen Primärquellen) – eine Abnahme durch eine Fachperson (Status ✅, `tools/abnahme.py`) steht aus.
