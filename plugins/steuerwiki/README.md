# Plugin «steuerwiki» 1.0.0

Steuer-Wiki Schweiz (Bund, AR, SG, TG, ZH; 2025/2026): Belege prüfen (steuerrelevant?), ablegen (nach Kategorienliste), Steuererklärung ausfüllen.

- **Skills** (werden bei Bedarf geladen): belege-ablage, steuererklaerung-np, steuerwiki
- **Tools** (MCP-Server `steuerwiki`, in OpenClaw `steuerwiki__<name>`): ablage, beleg, position, wert, vergleich, suche, zeige
- **Ablage-Kategorien:** Liste der Firma als `KATEGORIEN.md` in den Workspace legen (Vorlage: kategorien/vorlage.md)
- **Wissen:** index/lookup.json (Eckwerte, Positionen, Belege, Einreichepflicht, Erkennung), index/fts.sqlite (Volltext aller
  Quellen-Chunks), quick/ und wiki/ (Seiten für `zeige`). Originale und Volltexte: Repository/ZIP.
- Voraussetzung: `python3` (nur Standardbibliothek) auf dem Gateway-Host.

## Installation Claude Code (offizieller Weg über den Marketplace im Repository)
```
/plugin marketplace add sabania/swisstax
/plugin install steuerwiki@swisstax
```
Solange der Stand nur auf dem Branch liegt: `/plugin marketplace add sabania/swisstax#claude/clever-cori-k71ld5`.
Aktualisieren: `/plugin marketplace update swisstax`, danach `/plugin update steuerwiki@swisstax` (oder Auto-Update in `/plugin`).
Tools heissen in Claude Code `mcp__plugin_steuerwiki_steuerwiki__<name>`. Für Ablagefragen `KATEGORIEN.md` ins Projektverzeichnis legen;
den Einstieg (`AGENTS.workspace-snippet.md`) optional in die `CLAUDE.md` des Projekts übernehmen.

## Installation OpenClaw
```bash
openclaw plugins install ./steuerwiki-plugin --force --accept-capabilities
openclaw plugins inspect steuerwiki      # Bundle capabilities: skills, mcpServers
```
Danach den Inhalt von `AGENTS.workspace-snippet.md` in die `AGENTS.md` des Agent-Workspaces einfügen (L0: immer geladener Einstieg)
und die Kategorienliste der Firma als `KATEGORIEN.md` in den Workspace legen (Vorlage: `kategorien/vorlage.md`).

## Test ohne Agent
```bash
python3 tools/steuer.py wert zh 2025 fahrkosten
python3 tools/steuer.py ablage "Lohnausweis 2025 Muster AG" --kanton zh
```
