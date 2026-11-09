#!/usr/bin/env python3
"""Baut das installierbare Plugin «steuerwiki» (Claude-Plugin-Format; läuft in OpenClaw und Claude Code).

  python3 tools/build_plugin.py [--out dist/steuerwiki-plugin] [--tgz]

Inhalt: Skills (L1), MCP-Server mit den Tools wert/position/beleg/ablage/suche/zeige/prozess/mfiles (Zugriff auf L1/L2),
Wissensindex (index/lookup.json, index/fts.sqlite mit allen Chunks), Quick- und Wiki-Seiten (für `zeige`).
Nicht enthalten (bleiben im Repository/ZIP): raw/ (Original-PDFs), sources/, chunks/ als Einzeldateien, data/, tools zur Pflege.
Laufzeit: nur Python 3 (Standardbibliothek).

Installation OpenClaw:  openclaw plugins install <out> --force --accept-capabilities   (lokale Quelle → --force)
Installation Claude Code: /plugin install aus einem Marketplace oder `claude --plugin-dir <out>`.
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
        "description": "Steuer-Wiki Schweiz (Bund, AR, SG, TG, ZH; Steuerjahre 2025/2026): Belege prüfen, in M-Files ablegen, "
                       "Steuererklärung ausfüllen (DrTax-Positionen) – Skills und Lookup-Tools mit Fundstellen.",
        "author": {"name": "Steuer-Wiki"},
        "keywords": ["steuern", "schweiz", "steuererklaerung", "m-files", "drtax"],
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / ".mcp.json").write_text(json.dumps({"mcpServers": {"steuerwiki": {
        "command": "python3", "args": ["${CLAUDE_PLUGIN_ROOT}/tools/mcp_server.py"]}}}, indent=2), encoding="utf-8")
    for s in SKILLS:
        shutil.copytree(ROOT / "skills" / s, out / "skills" / s)
    (out / "tools").mkdir()
    for f in ("steuer.py", "mcp_server.py"):
        shutil.copy2(ROOT / "tools" / f, out / "tools" / f)
    (out / "index").mkdir()
    for f in ("lookup.json", "fts.sqlite"):
        shutil.copy2(ROOT / "index" / f, out / "index" / f)
    for d in ("quick", "wiki"):
        shutil.copytree(ROOT / d, out / d)
    for f in ("AGENTS.md", "KONZEPT.md"):
        shutil.copy2(ROOT / f, out / f)
    shutil.copy2(ROOT / "openclaw" / "AGENTS.workspace-snippet.md", out / "AGENTS.workspace-snippet.md")
    (out / "README.md").write_text(f"""# Plugin «steuerwiki» {a.version}

Steuer-Wiki Schweiz (Bund, AR, SG, TG, ZH; 2025/2026) + Firmenprozess Steuererklärung NP (consis).

- **Skills** (werden bei Bedarf geladen): {', '.join(SKILLS)}
- **Tools** (MCP-Server `steuerwiki`, in OpenClaw `steuerwiki__<name>`): wert, position, beleg, ablage, suche, zeige, prozess, mfiles
- **Wissen:** index/lookup.json (Eckwerte, Positionen, Belege, Einreichepflicht, M-Files, Prozess), index/fts.sqlite (Volltext aller
  Quellen-Chunks), quick/ und wiki/ (Seiten für `zeige`). Originale und Volltexte: Repository/ZIP.
- Voraussetzung: `python3` (nur Standardbibliothek) auf dem Gateway-Host.

## Installation OpenClaw
```bash
openclaw plugins install ./steuerwiki-plugin --force --accept-capabilities
openclaw plugins inspect steuerwiki      # Bundle capabilities: skills, mcpServers
```
Danach den Inhalt von `AGENTS.workspace-snippet.md` in die `AGENTS.md` des Agent-Workspaces einfügen (L0: immer geladener Einstieg).

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
