# Integration in OpenClaw

**Getestet** am 9.11.2026 mit OpenClaw **2026.11.2** (`npm i openclaw@2026.11.2`, Node ≥ 24.16): Installation mit
`install.sh`, `openclaw config validate`, Indexierung (9'240 Dateien → 14'197 Such-Chunks in ~90 s, FTS), `openclaw memory
search` und echte Agent-Turns (`openclaw agent --local`) mit Claude über die `claude-cli`-Runtime. Protokoll der
Testfragen: [`../eval/openclaw-lauf.md`](../eval/openclaw-lauf.md).

## Schnellstart (5 Schritte)

1. **Agent anlegen** mit eigenem Workspace, z.B. `~/.openclaw/workspace-steuer`, und ZIP entpacken / Repo klonen.
2. **Installieren:** `./openclaw/install.sh ~/.openclaw/workspace-steuer`
   - legt das ganze Wiki nach `<ws>/steuerwiki/` (alle Pfade aus Skills/Regeln gültig),
   - legt die indexierbaren Teile `quick/`, `wiki/`, `chunks/` physisch nach `<ws>/memory/steuerwiki/` (mit Symlinks in
     beide Richtungen, damit relative Links auf `sources/` und `raw/` funktionieren),
   - kopiert die Skills `steuerwiki`, `steuererklaerung-np`, `steuerwiki-pflege` nach `<ws>/skills/`.
3. **Workspace-`AGENTS.md`:** Inhalt von [`AGENTS.workspace-snippet.md`](AGENTS.workspace-snippet.md) einfügen (≈ 1'500 Zeichen).
4. **Konfiguration** `~/.openclaw/openclaw.json` (Beispiel unten) und `openclaw config validate`.
5. **Indexieren und testen:**
   ```bash
   openclaw memory index --force --agent steuer          # ~1–2 min (FTS); mit Embeddings je nach Provider länger
   openclaw memory status --agent steuer                 # erwartet: Indexed 9240/9240 files
   openclaw memory search "Fahrkosten Abzug ZH 2025" --agent steuer
   openclaw agent --agent steuer --message "ZH 2025: Lohnausweis Feld F angekreuzt – Fahrkostenabzug?"
   ```
   Weitere Testfragen: [`../eval/fragen.yaml`](../eval/fragen.yaml), [`../eval/blindtest-fragen.yaml`](../eval/blindtest-fragen.yaml).

## Konfiguration (getestet mit 2026.11.2)

```json5
// ~/.openclaw/openclaw.json
{
  agents: {
    ownership: "explicit",              // Pflicht, sobald mehr als ein Agent konfiguriert ist
    entries: {
      steuer: {
        workspace: "~/.openclaw/workspace-steuer",
        tools: { fs: { workspaceOnly: true } },
        memory: { search: { query: { maxResults: 10, minScore: 0.3 } } },
        // model: "anthropic/claude-sonnet-5-5",   // oder anderes Modell; siehe «Modell» unten
      },
    },
  },
  memory: {
    search: {
      provider: "openai",                    // | voyage | gemini | mistral | deepinfra | ollama | "local" (GGUF, ohne API-Key) | "none" (nur Volltext/FTS)
      model: "text-embedding-3-small",       // für Deutsch besser: text-embedding-3-large, voyage-4-large oder bge-m3
      cache: { enabled: true },
      store: { fts: { tokenizer: "trigram" } },   // empfohlen für Deutsch (Komposita); bei Wechsel Reindex
    },
  },
}
```

- **Kein `extraPaths` nötig**, weil das Wiki unter `memory/` liegt (wird standardmässig indexiert).
- **Ohne Embedding-Schlüssel:** `provider: "none"` (reine Volltextsuche, im Test brauchbar: die richtigen Chunks erscheinen
  oben, wenn die Anfrage Fachbegriffe enthält – Glossar `wiki/glossar.md` hilft) oder `provider: "local"` (lädt
  `embeddinggemma-300m` ~0.3 GB von HuggingFace, hybride Suche ohne Cloud). Ein explizit gesetzter Remote-Provider
  ohne Schlüssel fällt **nicht** auf FTS zurück – dann liefert `memory_search` nichts.
- **Modell:** beliebig. Getestet mit Claude über die `claude-cli`-Runtime (Claude Code auf dem Gateway-Host angemeldet):
  `agents.defaults.models: { "anthropic/claude-sonnet-5-5": { agentRuntime: { id: "claude-cli" } } }`.

## Was OpenClaw mit dem Wiki macht (beobachtet im Test)

- **Bootstrap:** Pro Sitzung wird nur die Workspace-`AGENTS.md` (+ SOUL/USER/IDENTITY/MEMORY) injiziert (max. 20'000
  Zeichen/Datei). Darum der kompakte Routing-Block im Snippet; die ausführlichen Regeln liegen in `steuerwiki/AGENTS.md`.
- **Skills:** Im Prompt erscheinen Name + Beschreibung; das `SKILL.md` liest der Agent bei Bedarf.
- **Suche (`memory_search`, Builtin «memory-core»):** hybrid (Vektor + BM25, MMR) bzw. nur FTS bei `provider: "none"`;
  nur `.md`-Dateien; OpenClaw zerlegt jede Datei selbst (~400 Tokens). Die Chunk-Dateien dieses Wikis sind ≤ ~1'600
  Zeichen → 1 Datei ≈ 1 Treffer. PDFs werden nie indexiert. **Symlinks werden nicht verfolgt** (deshalb keine Dubletten aus
  `sources/`).
- **Tools im Agent-Turn (Test):** `memory_search`, `memory_get`, `read`, `ls` – der Agent folgt den Links quick → wiki → chunks.
- **Zeitverfall:** Dateien über `extraPaths` verlieren mit 30 Tagen Halbwertszeit nach Änderungsdatum (mtime) an Gewicht
  (im Test: Score 0.0007 statt 0.92 bei mtime vor 10 Monaten). `evergreen: true` für extraPaths wird von 2026.11.2 **abgelehnt**
  («Unrecognized key»), ist aber in der Doku für neuere Versionen beschrieben. Dateien unter `memory/` ohne Datumspräfix
  verfallen nicht (Score 0.95) → darum installiert `install.sh` standardmässig nach `memory/`.

## Variante mit extraPaths

`./openclaw/install.sh <ws> --extrapaths` legt alles nach `<ws>/steuerwiki/` (mtime = Installationszeit) und braucht:

```json5
memory: { search: { extraPaths: [ { path: "steuerwiki", pattern: "{quick,wiki,chunks}/**/*.md" } ] } }
// ab einer Version mit evergreen-Support: { path: "steuerwiki", pattern: "...", evergreen: true }
```

Nachteil bis `evergreen` verfügbar ist: Zeitverfall gegenüber anderen Memory-Einträgen (innerhalb des Wikis bleibt die
Rangfolge gleich). Nach Updates des Wikis neu indexieren: `openclaw memory index --force --agent steuer`.

## Ältere Versionen (≤ 2026.7.1)

`agents.defaults.memorySearch.extraPaths: ["steuerwiki/quick", "steuerwiki/wiki", "steuerwiki/chunks"]` (Strings, kein
`pattern`); `openclaw doctor --fix` migriert beim Update. Das QMD-Backend wurde in 2026.8.1 entfernt; qmd kann als
MCP-Server laufen (`mcp.servers.qmd: {command: "qmd", args: ["mcp"]}`), die Chunk-Frontmatter enthält dafür
`qmd: {metadata: {jur, jahre, typ}}`.

## Datenschutz

Gesetze/Praxis sind öffentlich; Mandantenbelege gehören **nicht** in `memory/`. Dreaming/Promotion für den Steuer-Agenten
deaktivieren (`plugins.entries.memory-core.config.dreaming.enabled: false`), damit Mandantendaten aus Sitzungen nicht in
`MEMORY.md`/`memory/` wandern.
