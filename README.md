# Steuer-Wiki Schweiz – Wissensbasis für einen KI-Steuerexperten (natürliche Personen)

Strukturierte, zitierfähige Wissensbasis für die Erstellung von Steuererklärungen natürlicher Personen:
**Bund** (DBG, StHG, VStG/VStV, Verordnungen, ESTV-Kreis-/Rundschreiben, Wegleitungen) und die Kantone
**Appenzell Ausserrhoden, St. Gallen, Thurgau, Zürich**, Steuerjahre **2025 und 2026** – erweiterbar um weitere Jahre.

Aufgebaut nach dem **LLM-Wiki-Muster** (Andrej Karpathy, April 2026): unveränderliche Rohquellen → vom LLM gepflegtes,
verlinktes Markdown-Wiki → Schema-Datei (`AGENTS.md`) mit den Regeln. Ergänzt um **Hybrid-RAG-Chunks**
(`bund|kanton / jahr / dokument / chunk`) und einen **Quick-Access-Layer** für die zwei Kernfragen der Praxis:

1. **Welche Dokumente eines Mandanten sind steuerrelevant – welche nicht?** → [`quick/belege-relevanz.md`](quick/belege-relevanz.md)
2. **Je Kanton und Jahr: welcher Beleg / welche Zahl gehört in welche Formularposition, welche Limite gilt?**
   → `quick/zuordnung-<kanton>-<jahr>.md` und `quick/werte-<jurisdiktion>-<jahr>.md` (Einstieg: [`quick/index.md`](quick/index.md))

> Die Wissensbasis unterstützt Fachpersonen; sie ersetzt keine fachliche Beurteilung. Jede Zahl ist mit Fundstelle und
> Prüfstatus versehen (🟡 extrahiert · ☑️ agent-geprüft · ✅ verifiziert durch Fachperson · ⚠️ strittig).

## Aufbau

```
├── AGENTS.md            Schema: Regeln für Agenten (Routing, Zitierpflicht, Zeitmodell, Pflege)   ← zuerst lesen
├── KONZEPT.md           Konzept und Aufbau ausführlich (Schichten, Hierarchie, Zeitmodell, Nachvollziehbarkeit, Tests)
├── index.md             Einstiegskarte · log.md: Chronik (ingest/lint/…)
├── quick/               SCHICHT 1 – Quick Access (generiert aus data/)
│   ├── index.md             Frage → Seite, Matrix Kanton × Jahr, Datenstand/Lücken, Themen
│   ├── belege-relevanz.md   Dokument → relevant? (ja / bedingt / nein) → Belegkarte
│   ├── belege-ziffern.md    Beleg × Kanton/Jahr → Formularziffern
│   ├── wegleitung-<kt>-<jahr>.md  Kompakt-Wegleitung je Ziffer: Rein · Rechnen · Limite · Beachten (↗ Detail)
│   ├── gueltigkeit-<jahr>.md      welche Fassung jeder Quelle für Steuerjahr X gilt (Zeitmodell)
│   ├── zuordnung-<kt>-<jahr>.md   Ziffer · Position · Beleg · Kurzregel · Limite Kanton/Bund (↗ Detail)
│   ├── werte-<jur>-<jahr>.md      Eckwerte mit Fundstelle und Status (↗ Detail)
│   └── vergleich-<jahr>.md        alle Jurisdiktionen nebeneinander
├── data/                Single Source of Truth für den Quick-Layer (YAML, jede Angabe mit Chunk-ID + wörtlichem Zitat)
├── wiki/                SCHICHT 2 – Detailwissen
│   ├── themen/              31 Querschnittsthemen (Fahrkosten, Säule 3a, Liegenschaften …) mit Fundstellen
│   ├── belege/              45 Belegkarten (Erkennen an, Was extrahieren, Hinweise je Kanton, Ziffern, Quellen)
│   ├── glossar.md           Alltags- ↔ Fachbegriffe
│   └── <jur>/               Überblick (Verfahren/Fristen), zuordnung-…-detail / werte-…-detail (volle Regel + Zitate),
│                            Quellenkatalog, Zusammenfassungen je Quelle (quellen/)
├── sources/<jur>/<jahr>/<id>.md          SCHICHT 3 – Volltexte (verbatim, Seitenmarker)
├── chunks/<jur>/<jahr>/<id>/<id>__….md   SCHICHT 3 – RAG-Chunks (≤ ~1'500 Zeichen, Kontextzeile, Metadaten)
├── index/chunks.jsonl   alle Chunks + Metadaten + Text (für externe Vektor-/BM25-Indizes)
├── index/abhaengigkeiten.json   Quelle → Chunk → Daten-Eintrag → Seite (tools/impact.py)
├── raw/<jur>/<jahr>/    Originale (PDF/HTML/XML) als Backup, sha256 in der Registry
├── registry/            sources.yaml (alle Quellen inkl. Zeitbezug, gilt_ab/bis, Versionskette) · taxonomy.yaml · glossar.yaml · chunkplans/
├── tools/               Python-Pipeline (fetch → convert/laws → chunk → build_index → build_quick → lint)
├── skills/              AgentSkills/OpenClaw: steuerwiki (Abfrage), steuererklaerung-np (Fall-Ablauf), steuerwiki-pflege (Pflege)
├── openclaw/            Integrationsanleitung, Konfig-Snippets, install.sh
└── reports/             Lint- und Prüfberichte
```

`<jur>` = `bund | ar | sg | tg | zh`; `<jahr>` = erstes Steuerjahr der Fassung oder `dauernd` (jahresunabhängig:
Kreisschreiben, Merkblätter, Steuerbuch-Praxis). Massgeblich ist das Feld `jahre` in Registry/Frontmatter.

## Quellen und Formate

| Quelle | Format | Verarbeitung |
|---|---|---|
| Bundesrecht (DBG, StHG, VStG, VStV, BKV, LKV, QStV, VKP, BVV 3, WEFV) | **Akoma-Ntoso-XML** von Fedlex (SPARQL) | 1 Chunk pro Artikel, je Steuerjahr die gültige Konsolidierung |
| Kantonale Gesetze/Verordnungen | LexWork-JSON (SG, TG, AR) bzw. PDF (ZH) | 1 Chunk pro Artikel/§ |
| Wegleitungen, Kreisschreiben, Rundschreiben, Merkblätter, Formulare | PDF | verbatim (pdftotext -layout) + **semantischer Chunk-Plan durch Agenten** (`registry/chunkplans/`) |
| Zürcher Steuerbuch, Thurgauer Steuerpraxis, Info-Seiten | HTML | Hauptinhalt → Markdown, Chunks an Überschriften |

Alle Quellen mit URL, Abrufdatum, sha256 und Gültigkeit: [`registry/sources.yaml`](registry/sources.yaml);
lesbar je Jurisdiktion: `wiki/<jur>/<jur>-quellen.md`.

## Nutzung durch einen Agenten

- **OpenClaw** (getestet mit 2026.11.2): `./openclaw/install.sh <workspace>` → Snippet in die Workspace-`AGENTS.md` →
  `openclaw memory index --force --agent <id>`. Indexiert werden `quick/`, `wiki/`, `chunks/` unter `memory/steuerwiki/`
  (kein Zeitverfall), nicht `sources/`/`raw/`. Details, Konfiguration und Testprotokoll: [`openclaw/README.md`](openclaw/README.md).
- **Andere Agenten (Claude Code, Codex …):** `AGENTS.md` ist das Schema; `skills/steuerwiki/SKILL.md` beschreibt den Abfrageablauf.
- **Eigenes Hybrid-RAG:** `index/chunks.jsonl` (ein Datensatz pro Chunk: `id, jurisdiktion, jahre, typ, dokument, titel,
  pfad, artikel, ziffer, seiten, quelle_url, kontext, text, stichworte, positionen, …`). Empfehlung: BM25 (deutscher
  Stemmer/Dekompounding) + multilinguales Embedding (z.B. bge-m3, Qwen3-Embedding, text-embedding-3-large), Filter
  auf `jurisdiktion ∈ {kanton, bund}` und `jahre ∋ Steuerjahr`, Kontextzeile (`kontext`) mit einbetten. qmd liest die
  Filter direkt aus der Chunk-Frontmatter (`qmd: metadata`).

## Pipeline / Pflege

```bash
pip install requests pyyaml beautifulsoup4 lxml markdownify   # + poppler-utils (pdftotext)
python3 tools/fetch.py              # Originale laden (Registry), sha256-Änderungen melden (--refresh)
python3 tools/convert.py            # PDF/HTML -> sources/
python3 tools/laws.py resolve --jahre 2025 2026 && python3 tools/fetch.py && python3 tools/laws.py convert
python3 tools/validate_plan.py <id> # Chunk-Plan (vom Agenten erstellt) prüfen
python3 tools/chunk.py              # -> chunks/
python3 tools/build_index.py        # -> index/*.jsonl, wiki/<jur>/<jur>-quellen.md
python3 tools/build_quick.py        # data/ -> quick/
python3 tools/lint.py               # Prüfungen (Zitate wörtlich im Chunk, Links, Hashes) -> reports/lint.md
```

### Neues Steuerjahr hinzufügen (z.B. 2027)

1. `python3 tools/new_year.py --jahr 2027 --von 2026` → Gerüst `data/*/…/2027.yaml` (gleiche Schlüssel, Werte leer)
   und Checkliste `reports/neues-jahr-2027.md` der zu beschaffenden Nachfolgequellen.
2. Neue Quellen in `registry/sources.yaml` eintragen (`ordner_jahr: '2027'`, `jahre: [2027]`), dann
   `fetch.py` → `convert.py` → Chunk-Plan (Agent) → `chunk.py`; Bundesrecht: `laws.py resolve --jahre 2027`.
3. Werte/Zuordnungen 2027 mit Zitat aus den 2027-Quellen füllen (Agent mit Skill `steuerwiki-pflege`), Wiki-Themen ergänzen.
4. `build_index.py` → `build_quick.py` → `lint.py`; Fachperson verifiziert; `log.md` ergänzen.

Unveränderte Gesetzesfassungen werden nicht dupliziert (eine Konsolidierung = ein Eintrag mit mehreren `jahre`).

## Stand (09.11.2026)

- **Quellen:** 285 (Gesetze/Verordnungen als XML/JSON je Artikel, Wegleitungen, Formulare, Merkblätter, Kreis-/Rundschreiben,
  Steuerbuch/Steuerpraxis), jede mit Zeitbezug, Gültigkeit und Versionskette · **Chunks:** 8'876 · Originale in `raw/`.
- **Daten:** 10 Werte-Dateien (73 Eckwerte je Jurisdiktion/Jahr), 8 Zuordnungsdateien (724 Positionen mit Kompakt-Wegleitung
  rein/berechnung/beachten), 45 Belegtypen – jede Angabe mit wörtlichem, maschinell geprüftem Zitat; alle extrahierten Angaben
  zweitgeprüft. Arbeitsliste für die Fachperson: [`reports/offene-punkte.md`](reports/offene-punkte.md).
- **Wiki:** 31 Themenseiten, 5 Überblicke, 45 Belegkarten, Detailseiten mit Zitaten, Gültigkeitsseiten je Jahr, Glossar.
- **Getestet in OpenClaw 2026.11.2** (echte Agent-Turns, unabhängig bewertet): 63/64 Fragen voll richtig (Praxis-, Blind- und
  Positionstest), 0 falsch; Fundstellen, Kanton/Bund-Trennung und Steuerjahr 64/64. Ende-zu-Ende: 4 vollständige
  Steuererklärungen (ZH/SG/TG/AR 2025), 103/109 Positionen korrekt, 3 von 4 «einreichbar nach Kontrolle» – siehe [`eval/laeufe/`](eval/laeufe/).
- **Abnahme durch die Fachperson (ausstehend):** priorisierte Checklisten `reports/abnahme-checkliste-2025.md` / `-2026.md`
  (Wert, Chunk-Link, Zitat; Häkchen → `tools/abnahme.py uebernehmen`), Entscheidungsvorlage zu den 10 strittigen Punkten
  `reports/entscheidungsvorlage-strittig.md` (je Quellen, Rang, Empfehlung). Status ✅ setzt nur die Fachperson.
- **Lücken 2026:** reguläre Formulare/Wegleitungen 2026 noch nicht publiziert (Stand 09.11.2026); ZH/SG 2026 stützen sich auf
  die UJ-Fassungen (Hauptformular und Hilfsblätter), AR 2026 ist ein Gerüst.

Quellenbasis: die Wissensdatenbank-Dateien in `_seed/` (Recherche vom 30.10.2026) plus ergänzte Quellen (Fedlex-XML,
ESTV-Formulare 2025, Vorgängerfassungen ZStB, VKP ZH, KS 11/18). Chronik: [`log.md`](log.md).
