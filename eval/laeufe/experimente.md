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
| Hybrid mit lokalen Embeddings (`provider: "local"`) | – | nicht getestet: Plugin `@openclaw/llama-cpp-provider` nötig, Installation in der Testumgebung durch die Sicherheitsrichtlinie blockiert | | | | |

Angereicherte Kontextzeile = erste Zeile jedes Chunks nennt Ebene und Kanton ausgeschrieben, z.B.
«Bund · Bundesebene (direkte Bundessteuer, Bundesrecht) · Rundschreiben · Steuerjahr 2026 · RS 2-215 …» statt «Bund · Steuerjahr 2026 · …».
Häufigster Fehler vorher: Treffer aus dem falschen Kanton/Jahr (z.B. «km-Ansatz 2026 direkte Bundessteuer» → TG-Chunks).

**Entscheide:** Tokenizer-Empfehlung von trigram auf Standard (unicode61) geändert; Kontextzeilen in `tools/chunk.py`
angereichert (alle Chunks neu erzeugt, IDs und Texte unverändert).

## Lauf A – Baseline im echten OpenClaw (unabhängig bewertet)

Details: [bewertung-A.md](bewertung-A.md). Blindtest 14/14 richtig; Praxistest 38/40 richtig (inkl. korrekt «nicht abgedeckt»),
2 teilweise (falsche Nebenaussagen); Fundstellen, Kanton/Bund-Trennung und Steuerjahr in 54/54 Antworten korrekt.
Mittlere Dauer je Frage ~40 s.

Daraus abgeleitetes Tuning: Hinweise zu Gebäudealter (Bund: zu Beginn der Steuerperiode) und Bundes-Kinderabzug
(Einkommen 6'800 **und** Steuerbetrag 263) direkt in die Eckwerte; Blindtest-Referenz b03 korrigiert (indexierte Beträge).

## E2 – Kompakt-Wegleitung und Tuning im Agenten-Lauf (Lauf B)

*(wird nach Lauf B ergänzt)*
