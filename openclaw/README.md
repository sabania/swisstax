# Integration in OpenClaw

Stand der Recherche: 9.11.2026, OpenClaw **v2026.11.1** (stabil) bzw. `main`. Für ≤ 2026.7.1 siehe Abschnitt «Ältere Versionen».

## Schnellstart (5 Schritte)

1. **Agent anlegen** (eigener Workspace, z.B. `~/.openclaw/workspace-steuer`) und ZIP entpacken/Repo klonen.
2. **Installieren:** `./openclaw/install.sh ~/.openclaw/workspace-steuer` – kopiert das Wiki nach `<workspace>/steuerwiki/`
   und die drei Skills nach `<workspace>/skills/` (`steuerwiki`, `steuererklaerung-np`, `steuerwiki-pflege`).
3. **Workspace-`AGENTS.md`:** Inhalt von [`AGENTS.workspace-snippet.md`](AGENTS.workspace-snippet.md) einfügen (≈ 1'500 Zeichen).
4. **Konfiguration** (`~/.openclaw/openclaw.json`, siehe unten): `memory.search.extraPaths` mit
   `{ path: "steuerwiki", pattern: "{quick,wiki,chunks}/**/*.md" }`, Embedding-Provider wählen, `maxResults: 10`.
5. **Indexieren und testen:** Gateway neu starten → `openclaw memory index --force --agent steuer` →
   `openclaw memory search "Fahrkosten Abzug ZH 2025" --agent steuer`. Danach im Chat z.B. fragen:
   «ZH 2025: In welche Ziffer gehört der Nettolohn aus dem Lohnausweis?» oder «Triagiere diese Belege …».
   Weitere Testfragen: [`../eval/fragen.yaml`](../eval/fragen.yaml).

## Was OpenClaw mit dem Wiki macht

- **Bootstrap:** In jede Sitzung wird nur die Workspace-Datei `AGENTS.md` (+ SOUL/USER/IDENTITY/MEMORY) injiziert,
  max. 20'000 Zeichen pro Datei / 60'000 total (`agents.defaults.bootstrapMaxChars` / `bootstrapTotalMaxChars`).
  → Den kompakten Routing-Block aus [`AGENTS.workspace-snippet.md`](AGENTS.workspace-snippet.md) in die
  Workspace-`AGENTS.md` kopieren. Die ausführlichen Regeln liegen in `steuerwiki/AGENTS.md` (on demand lesen).
- **Skills:** `skills/steuerwiki` (Abfrage), `skills/steuererklaerung-np` (Fall-Ablauf: Belege → Ausfüllhilfe) und `skills/steuerwiki-pflege` (Ingest/neues Jahr/Lint) nach
  `<workspace>/skills/` kopieren. Im Prompt erscheinen nur Name + Beschreibung; das `SKILL.md` wird bei Bedarf gelesen.
- **Suche (`memory_search`, Builtin «memory-core»):** hybrid (Vektor 0.7 + BM25 0.3, MMR), nur **`.md`-Dateien**,
  OpenClaw zerlegt jede Datei selbst in ~400 Tokens (~1'600 Zeichen, 80 Tokens Überlappung). Frontmatter wird als
  Text mitindexiert. **PDFs werden nie indexiert.** Die Chunk-Dateien dieses Wikis sind ≤ ~1'600 Zeichen → 1 Datei = 1 Treffer.
- **Zeitverfall:** Dateien ausserhalb `memory/` verlieren in v2026.11.1 mit 30 Tagen Halbwertszeit nach Änderungsdatum
  (mtime) an Gewicht; `extraPaths` mit `evergreen: true` gibt es erst auf `main`. Dateien mit Datumspräfix
  `YYYY-MM-DD*.md` gelten als Tagesnotizen – das Wiki verwendet keine solchen Namen.

## Empfohlene Ablage

```
<workspace>/                     (z.B. ~/.openclaw/workspace-steuer)
├── AGENTS.md                    ← Snippet aus AGENTS.workspace-snippet.md einfügen
├── skills/steuerwiki/SKILL.md   ← aus diesem Repo
├── skills/steuerwiki-pflege/SKILL.md
└── steuerwiki/                  ← dieses Repo (ZIP entpacken)
    ├── quick/ wiki/ chunks/     ← indexieren (memory_search)
    ├── sources/                 ← NICHT indexieren (Volltexte = Dubletten der Chunks), nur lesen
    └── raw/ index/ registry/ tools/ ...  ← nicht indexieren
```

Nur **eine** Darstellung indexieren: `quick/`, `wiki/` und `chunks/`. `sources/` (Volltexte) und `raw/` (PDF/HTML/XML)
bleiben lesbar (`read`), werden aber nicht indexiert – sonst erscheinen Treffer doppelt.

## Konfiguration (≥ 2026.8.1, getestet gegen die Doku v2026.11.1)

```json5
// ~/.openclaw/openclaw.json
{
  agents: {
    entries: {
      steuer: {
        workspace: "~/.openclaw/workspace-steuer",
        tools: { fs: { workspaceOnly: true } },
        memory: {
          search: {
            extraPaths: [
              { path: "steuerwiki", pattern: "{quick,wiki,chunks}/**/*.md" },
              // auf main / ab Release mit evergreen: { path: "steuerwiki", pattern: "...", evergreen: true },
            ],
            query: { maxResults: 10, minScore: 0.3 },
          },
        },
      },
    },
  },
  memory: {
    search: {
      provider: "openai",                    // oder voyage | gemini | mistral | deepinfra (BAAI/bge-m3) | local | ollama
      model: "text-embedding-3-small",       // für Deutsch besser: text-embedding-3-large, voyage-4-large oder bge-m3
      remote: { batch: { enabled: true } },  // Erstindexierung in Batches
      cache: { enabled: true },
      // store: { fts: { tokenizer: "trigram" } },  // optional: besser für deutsche Komposita (Reindex nötig, vorher testen)
    },
  },
}
```

Danach: Gateway neu starten, `openclaw memory index --force --agent steuer`, Test:
`openclaw memory search "Fahrkosten Abzug ZH 2025" --agent steuer`.

**Zeitverfall umgehen (bis `evergreen` verfügbar ist):** Nach dem Entpacken/Aktualisieren alle Wiki-Dateien auf das
gleiche Datum setzen, damit die Rangfolge innerhalb des Wikis nicht vom Änderungsdatum abhängt:
`find steuerwiki -name '*.md' -exec touch -d "2026-01-01" {} +` (die Gewichtung relativ zu Tagesnotizen bleibt).
Alternative: indexierbare Teile unter `<workspace>/memory/steuerwiki/` ablegen (immer «evergreen»), dann aber
`sources/` und `raw/` ausserhalb von `memory/` halten (alles unter `memory/` wird indexiert) – `install.sh --memory`.

## Ältere Versionen (≤ 2026.7.1)

`agents.defaults.memorySearch.extraPaths: ["steuerwiki/quick", "steuerwiki/wiki", "steuerwiki/chunks"]` (Strings,
kein `pattern`); `openclaw doctor --fix` migriert beim Update auf das neue Schema. Das QMD-Backend wurde in 2026.8.1
entfernt; qmd kann weiterhin als MCP-Server neben der Builtin-Suche laufen (`mcp.servers.qmd: {command: "qmd", args: ["mcp"]}`),
die Chunk-Frontmatter enthält dafür `qmd: {metadata: {jur, jahre, typ}}` (Filter nach Kanton/Jahr möglich).

## Datenschutz

Gesetze/Praxis sind öffentlich; Mandantenbelege gehören **nicht** in den Memory-Index. Den Dreaming-/Memory-Schreibpfad
für den Steuer-Agenten prüfen bzw. deaktivieren (`plugins.entries.memory-core.config.dreaming.enabled: false`), damit
Wiki-Ausschnitte nicht in `MEMORY.md` wandern.
