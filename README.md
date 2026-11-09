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
├── AGENTS.md            Schema: Regeln für Agenten (Routing, Zitierpflicht, Pflege)   ← zuerst lesen
├── index.md             Einstiegskarte · log.md: Chronik (ingest/lint/…)
├── quick/               SCHICHT 1 – Quick Access (generiert aus data/)
│   ├── index.md             Frage → Seite, Matrix Kanton × Jahr, Datenstand/Lücken, Themen
│   ├── belege-relevanz.md   Dokument → relevant? (ja / bedingt / nein) → Belegkarte
│   ├── belege-ziffern.md    Beleg × Kanton/Jahr → Formularziffern
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
├── raw/<jur>/<jahr>/    Originale (PDF/HTML/XML) als Backup, sha256 in der Registry
├── registry/            sources.yaml (alle Quellen) · taxonomy.yaml (Schlüssel) · years.yaml · chunkplans/
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
  Steuerbuch/Steuerpraxis) · **Chunks:** 8'876 (Bund 2'890 · ZH 2'136 · SG 1'502 · TG 1'462 · AR 886) · Originale in `raw/`.
- **Daten:** 10 Werte-Dateien (73 Eckwerte je Jurisdiktion/Jahr), 8 Zuordnungsdateien, 45 Belegtypen – jede Angabe mit
  wörtlichem Zitat, maschinell geprüft. Status-Übersicht und Arbeitsliste: [`reports/offene-punkte.md`](reports/offene-punkte.md).
- **Wiki:** 31 Themenseiten, 5 Überblicke, 45 Belegkarten, Detailseiten je Kanton/Jahr, Glossar.
- **Praxistest** ([`eval/`](eval/)): 40 Treuhänder-Fragen, beantwortet von Agenten nur mit dem Wiki – alle inhaltlich korrekt
  gegenüber den Soll-Antworten (Review). Erkenntnisse sind in den Quick-Layer eingeflossen.
- **Lücken:** AR 2026 ohne Formular/Wegleitung (Gerüst, Werte teils strittig); ZH/SG 2026 nur Formular für unterjährige
  Steuerpflicht; 10 strittige Punkte für die Fachperson. `verifiziert` (✅) setzt nur die Fachperson.

Quellenbasis: die Wissensdatenbank-Dateien in `_seed/` (Recherche vom 30.10.2026) plus ergänzte Quellen (Fedlex-XML,
ESTV-Formulare 2025, Vorgängerfassungen ZStB, VKP ZH, KS 11/18). Chronik: [`log.md`](log.md).
