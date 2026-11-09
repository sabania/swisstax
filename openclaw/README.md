# Integration in OpenClaw

**Getestet** am 9.11.2026 mit OpenClaw **2026.11.2** (`npm i openclaw@2026.11.2`, Node ≥ 24.16): Installation mit
`install.sh`, `openclaw config validate`, Indexierung (9'240 Dateien → 14'197 Such-Chunks in ~90 s, FTS), `openclaw memory
search` und echte Agent-Turns (`openclaw agent --local`) mit Claude über die `claude-cli`-Runtime. Protokoll der
Testfragen: [`../eval/openclaw-lauf.md`](../eval/openclaw-lauf.md).

## Empfohlen: als Plugin installieren (Skills + Tools + Wissen)

Getestet mit OpenClaw 2026.11.2 und Haiku/Sonnet über die `claude-cli`-Runtime.

```bash
python3 tools/build_plugin.py --tgz                     # → dist/steuerwiki-plugin/ (und .tgz, ≈ 7 MB)
openclaw plugins install dist/steuerwiki-plugin --force --accept-capabilities   # lokale Quelle → --force
openclaw plugins inspect steuerwiki                     # Format: bundle (claude) · Bundle capabilities: skills, mcpServers
cat openclaw/AGENTS.workspace-snippet.md >> <workspace>/AGENTS.md                # L0-Einstieg (≈ 2 KB)
openclaw agent --agent <id> --message "TG 2025: maximaler Fahrkostenabzug?"     # → 1 Aufruf steuerwiki__wert
```

- Das Plugin bringt 4 Skills (`steuerwiki`, `steuerprozess-eingang`, `steuererklaerung-np`, `steuerprozess-ablauf`) und den
  MCP-Server `steuerwiki` mit den Tools `steuerwiki__wert`, `__position`, `__beleg`, `__ablage`, `__suche`, `__zeige`,
  `__prozess`, `__mfiles`. Voraussetzung: `python3` auf dem Gateway-Host (nur Standardbibliothek).
- **Kein `tools.fs.workspaceOnly` für diesen Agenten setzen.** OpenClaw legt Plugin-Skills unter `<state>/plugin-skills/` ab und
  der Agent liest sie mit dem OpenClaw-Tool `read`; `workspaceOnly: true` sperrt genau diesen Pfad («Path escapes sandbox root»),
  die Skills wären dann nicht nutzbar (getestet 2026.11.2). Isolation stattdessen über einen eigenen Betriebssystem-Benutzer bzw.
  die OpenClaw-Sandbox des Gateways.
- `memory_search`/Indexierung sind für das Plugin nicht nötig (eigene Volltextsuche `suche`). Wer zusätzlich `memory_search`
  über das Wiki will, installiert parallel den Workspace-Weg unten.
- Format: Claude-Plugin (`.claude-plugin/plugin.json`, `.mcp.json`, `skills/`). Ein reines `plugin.json` (Agent-Plugins-Format)
  wurde in 2026.11.2 nicht als solches erkannt; das Claude-Format funktioniert und ist zugleich in Claude Code nutzbar.
- Update: neu bauen, `openclaw plugins install … --force --accept-capabilities` erneut ausführen (neue Sitzungen sehen den Stand).

## Alternative: Workspace-Installation (Dateien + memory_search)

Das Werkzeug funktioniert auch hier per exec: `python3 steuerwiki/tools/steuer.py <befehl> …`.

## Schnellstart Workspace (5 Schritte)

1. **Agent anlegen** mit eigenem Workspace, z.B. `~/.openclaw/workspace-steuer`, und ZIP entpacken / Repo klonen.
2. **Installieren:** `./openclaw/install.sh ~/.openclaw/workspace-steuer`
   - legt das ganze Wiki nach `<ws>/steuerwiki/` (alle Pfade aus Skills/Regeln gültig),
   - legt die indexierbaren Teile `quick/`, `wiki/`, `chunks/` physisch nach `<ws>/memory/steuerwiki/` (mit Symlinks in
     beide Richtungen, damit relative Links auf `sources/` und `raw/` funktionieren),
   - kopiert die Skills `steuerwiki`, `steuerprozess-eingang`, `steuererklaerung-np`, `steuerprozess-ablauf`, `steuerwiki-pflege` nach `<ws>/skills/`.
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
        // tools: { fs: { workspaceOnly: true } },  // nur bei reiner Workspace-Installation möglich; mit Plugin weglassen (Skills!)
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
      // store.fts.tokenizer: Standard "unicode61" belassen – im Retrieval-Test besser als "trigram" (eval/laeufe/experimente.md)
    },
  },
}
```

- **Kein `extraPaths` nötig**, weil das Wiki unter `memory/` liegt (wird standardmässig indexiert).
- **Ohne Embedding-Schlüssel:** `provider: "none"` (reine Volltextsuche; so wurde getestet) oder `provider: "local"` – dieser
  braucht in 2026.11.2 zuerst das Plugin: `openclaw plugins install @openclaw/llama-cpp-provider` (lädt dann
  `embeddinggemma-300m` ~0.3 GB von HuggingFace; im Test nicht installiert, siehe Experimente). Ein explizit gesetzter
  Remote-Provider ohne Schlüssel fällt **nicht** auf FTS zurück – dann liefert `memory_search` nichts.
- **Tokenizer:** Standard (`unicode61`) belassen. Retrieval-Test (29 Fragen mit belegten Fundstellen): unicode61 Hit@10 59 %
  vs. trigram 52 %; mit angereicherten Chunk-Kontextzeilen MRR 0.36 statt 0.28.
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
- **Tools im Agent-Turn (Test, 47 Turns):** `read` 333×, `exec` (grep/cat) 38×, `memory_search` 9× – der Agent navigiert
  hauptsächlich über Dateien und Links (quick → wiki → chunks); die Suche ist Rückfallebene. Darum zählt die Struktur des
  Quick-Layers mehr als die Suchkonfiguration.
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
