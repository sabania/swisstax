#!/usr/bin/env python3
"""Baut das installierbare Plugin «steuerwiki» (Claude-Plugin-Format; läuft in OpenClaw und Claude Code).

  python3 tools/build_plugin.py [--out dist/steuerwiki-plugin] [--tgz]

Inhalt: Skills (L1), MCP-Server mit den Tools ablage/beleg/position/wert/vergleich/suche/zeige (Zugriff auf L1/L2),
Wissensindex (index/lookup.json, index/fts.sqlite mit allen Chunks), Quick- und Wiki-Seiten (für `zeige`).
Nicht enthalten (bleiben im Repository/ZIP): raw/ (Original-PDFs), sources/, chunks/ als Einzeldateien, data/, tools zur Pflege.
Laufzeit: nur Python 3 (Standardbibliothek).

Installation OpenClaw:  openclaw plugins install <out> --force --accept-capabilities   (lokale Quelle → --force)
Installation Claude Code: Marketplace im Repository (.claude-plugin/marketplace.json → plugins/steuerwiki); Plugin-Ordner bauen mit
  python3 tools/build_plugin.py --out plugins/steuerwiki   (nach jeder Datenänderung, Version in plugin.json erhöhen: --version x.y.z)
"""
from __future__ import annotations
import argparse, json, shutil, subprocess, sys, tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ["belege-ablage", "steuererklaerung-np", "steuerwiki"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "dist" / "steuerwiki-plugin"))
    ap.add_argument("--tgz", action="store_true")
    ap.add_argument("--version", default="1.0.0")
    a = ap.parse_args()
    out = Path(a.out)
    subprocess.run([sys.executable, str(ROOT / "tools" / "build_lookup.py")], check=True)
    if out.exists():
        shutil.rmtree(out)
    (out / ".claude-plugin").mkdir(parents=True)
    (out / ".claude-plugin" / "plugin.json").write_text(json.dumps({
        "name": "steuerwiki",
        "version": a.version,
        "description": "Steuer-Wiki Schweiz (Bund, AR, SG, TG, ZH; Steuerjahre 2025/2026): Belege prüfen und ablegen, "
                       "Steuererklärung ausfüllen (Formularpositionen) – Skills und Lookup-Tools mit Fundstellen.",
        "author": {"name": "Steuer-Wiki"},
        "keywords": ["steuern", "schweiz", "steuererklaerung", "belege", "ablage"],
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    srv = {"command": "python3", "args": ["${CLAUDE_PLUGIN_ROOT}/tools/mcp_server.py"]}
    (out / ".mcp.json").write_text(json.dumps({"mcpServers": {"steuerwiki": srv}}, indent=2), encoding="utf-8")
    for s in SKILLS:
        shutil.copytree(ROOT / "skills" / s, out / "skills" / s)
    (out / "tools").mkdir()
    for f in ("steuer.py", "mcp_server.py"):
        shutil.copy2(ROOT / "tools" / f, out / "tools" / f)
    (out / "index").mkdir()
    for f in ("lookup.json", "fts.sqlite", "quellen.jsonl"):
        shutil.copy2(ROOT / "index" / f, out / "index" / f)
    for d in ("quick", "wiki"):
        shutil.copytree(ROOT / d, out / d)
    (out / "kategorien").mkdir()
    shutil.copy2(ROOT / "kategorien" / "vorlage.md", out / "kategorien" / "vorlage.md")   # nur die Vorlage, keine Firmenliste
    for f in ("AGENTS.md", "KONZEPT.md"):
        shutil.copy2(ROOT / f, out / f)
    shutil.copy2(ROOT / "openclaw" / "AGENTS.workspace-snippet.md", out / "AGENTS.workspace-snippet.md")
    (out / "README.md").write_text(f"""# Plugin «steuerwiki» {a.version}

Steuer-Wiki Schweiz (Bund, AR, SG, TG, ZH; 2025/2026): Belege prüfen (steuerrelevant?), ablegen (nach Kategorienliste), Steuererklärung ausfüllen.

- **Skills** (werden bei Bedarf geladen): {', '.join(SKILLS)}
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
""", encoding="utf-8")
    n = sum(1 for _ in out.rglob("*") if _.is_file())
    size = sum(f.stat().st_size for f in out.rglob("*") if f.is_file()) / 1e6
    print(f"Plugin: {out} · {n} Dateien · {size:.1f} MB")
    if a.tgz:
        tgz = out.with_suffix(".tgz")
        with tarfile.open(tgz, "w:gz") as t:
            t.add(out, arcname=out.name)
        print(f"Archiv: {tgz} ({tgz.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
