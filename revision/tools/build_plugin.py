#!/usr/bin/env python3
"""Baut das installierbare Plugin «revisionswiki» (Claude-Plugin-Format; läuft in OpenClaw und Claude Code).

  python3 revision/tools/build_plugin.py [--out plugins/revisionswiki] [--version 1.0.0] [--tgz]

Inhalt: Skills (revision, revision-pruefschritt, revision-mandat), MCP-Server mit 15 Tools (tools/revision.py),
Wissen (index/lookup.json, index/fts.sqlite mit allen Chunks), quick/ und wiki/ (für `zeige`), Einstieg für AGENTS.md/CLAUDE.md,
Vorschlag Werkzeugrechte revio-MCP (openclaw/revio-tool-policy.json).
Nicht enthalten: raw/ (Originale), sources/, chunks/ als Einzeldateien, data/, Testdaten, Pflege-Tools.
INTERN: EXPERTsuisse-Werke (HWP, SER, SA-CH, Q&A, Muster) sind an consis lizenziert; revio ist proprietär – nicht weitergeben.
"""
from __future__ import annotations
import argparse, json, shutil, subprocess, sys, tarfile
from pathlib import Path

R = Path(__file__).resolve().parents[1]
ROOT = R.parent
SKILLS = ["revision", "revision-pruefschritt", "revision-mandat"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "plugins" / "revisionswiki"))
    ap.add_argument("--version", default="1.0.0")
    ap.add_argument("--tgz", action="store_true")
    a = ap.parse_args()
    out = Path(a.out)
    subprocess.run([sys.executable, str(R / "tools" / "build_lookup.py")], check=True)
    if out.exists():
        shutil.rmtree(out)
    (out / ".claude-plugin").mkdir(parents=True)
    (out / ".claude-plugin" / "plugin.json").write_text(json.dumps({
        "name": "revisionswiki",
        "version": a.version,
        "description": "Revisions-Wiki Schweiz (eingeschränkte Revision, SER/HWP/OR) für den KI-Revisionsagenten in revio 4.0: Prüfschritte "
                       "vorbereiten, Prüffelder, Prozess, Werte, revio-MCP-Zuordnung – Skills und Lookup-Tools mit Fundstellen. INTERN (consis).",
        "author": {"name": "Revisions-Wiki"},
        "keywords": ["revision", "eingeschraenkte-revision", "ser", "revio", "wirtschaftspruefung", "schweiz"],
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / ".mcp.json").write_text(json.dumps({"mcpServers": {"revisionswiki": {
        "command": "python3", "args": ["${CLAUDE_PLUGIN_ROOT}/tools/mcp_server.py"]}}}, indent=2), encoding="utf-8")
    for s in SKILLS:
        shutil.copytree(R / "skills" / s, out / "skills" / s)
    (out / "tools").mkdir()
    for f in ("revision.py", "mcp_server.py"):
        shutil.copy2(R / "tools" / f, out / "tools" / f)
    (out / "index").mkdir()
    for f in ("lookup.json", "fts.sqlite"):
        shutil.copy2(R / "index" / f, out / "index" / f)
    for d in ("quick", "wiki"):
        shutil.copytree(R / d, out / d)
    for f in ("AGENTS.md", "KONZEPT.md"):
        if (R / f).exists():
            shutil.copy2(R / f, out / f)
    shutil.copy2(R / "openclaw" / "AGENTS.workspace-snippet.md", out / "AGENTS.workspace-snippet.md")
    if (R / "openclaw" / "revio-tool-policy.json").exists():
        shutil.copy2(R / "openclaw" / "revio-tool-policy.json", out / "revio-tool-policy.json")
    (out / "README.md").write_text(f"""# Plugin «revisionswiki» {a.version} – INTERN

Wissensbasis für den KI-Revisionsagenten (consis): eingeschränkte Revision nach SER, HWP ER, OR; revio 4.0 (29 Prüffelder,
538 Prüfschritte); Zuordnung zum revio-MCP. Der Agent **bereitet vor** – Visum, Abschluss, Freigabe, Bericht bleiben beim WP.

- **Skills:** {', '.join(SKILLS)}
- **Tools** (MCP-Server `revisionswiki`): pruefschritt, prueffeld, prozess, regeln, revio, wert, rechne, wesentlichkeit,
  kapitalverlust, revisionspflicht, unterlagen, fragen, thema, suche, zeige
- **Wissen:** index/lookup.json (Katalog, Prüffeld-Wissen, Prozess, Werte, Regeln, revio-Zuordnung), index/fts.sqlite (Volltext
  aller Quellen-Chunks), quick/ und wiki/ (Seiten für `zeige`).
- **revio-Rechte:** `revio-tool-policy.json` (Vorschlag allow/deny je revio-MCP-Werkzeug; `revio_call` sperren).
- Voraussetzung: `python3` (nur Standardbibliothek).

**Lizenz/Vertraulichkeit:** EXPERTsuisse-Werke (HWP, SER, SA-CH, Q&A, Muster) sind an consis lizenziert, revio ist proprietär –
Plugin nur intern verwenden, nicht weitergeben. Keine Mandantendaten im Plugin.

## Installation Claude Code (Marketplace im Repository)
```
/plugin marketplace add sabania/swisstax
/plugin install revisionswiki@swisstax
```
Solange der Stand nur auf dem Branch liegt: `/plugin marketplace add sabania/swisstax#claude/clever-cori-k71ld5`.
Tools heissen `mcp__plugin_revisionswiki_revisionswiki__<name>`. Einstieg (`AGENTS.workspace-snippet.md`) in die `CLAUDE.md` übernehmen.

## Installation OpenClaw
```bash
openclaw plugins install ./revisionswiki --force --accept-capabilities
openclaw plugins inspect revisionswiki
```
Danach `AGENTS.workspace-snippet.md` in die `AGENTS.md` des Agent-Workspaces einfügen. Tools heissen `revisionswiki__<name>`.

## Test ohne Agent
```bash
python3 tools/revision.py hilfe
python3 tools/revision.py pruefschritt C1-302
python3 tools/revision.py revio 10.9
```
""", encoding="utf-8")
    n = sum(1 for f in out.rglob("*") if f.is_file())
    size = sum(f.stat().st_size for f in out.rglob("*") if f.is_file()) / 1e6
    print(f"Plugin: {out} · {n} Dateien · {size:.1f} MB")
    if a.tgz:
        tgz = out.with_suffix(".tgz")
        with tarfile.open(tgz, "w:gz") as t:
            t.add(out, arcname=out.name)
        print(f"Archiv: {tgz} ({tgz.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
