#!/usr/bin/env bash
# Kopiert das Steuer-Wiki in einen OpenClaw-Workspace (getestet mit OpenClaw 2026.11.2).
#
#   ./openclaw/install.sh <workspace-pfad>               (empfohlen)
#   ./openclaw/install.sh <workspace-pfad> --extrapaths  (Variante mit memory.search.extraPaths)
#
# Standard («memory»): Das ganze Wiki liegt unter <ws>/steuerwiki/ (alle Pfade aus Skills/AGENTS.md und alle relativen
# Links bleiben gültig). Die indexierbaren Teile quick/, wiki/, chunks/ liegen physisch unter <ws>/memory/steuerwiki/
# und sind von <ws>/steuerwiki/ aus verlinkt. Grund: Dateien unter memory/ (ohne Datumspräfix) gelten als «evergreen»
# und verlieren keine Relevanz durch Zeitverfall; extraPaths-Dateien dagegen schon (30 Tage Halbwertszeit nach mtime,
# `evergreen: true` für extraPaths gibt es in 2026.11.2 noch nicht). Der Memory-Indexer folgt keinen Symlinks, daher
# werden sources/ und raw/ nicht doppelt indexiert, die Links aus den Wiki-Seiten funktionieren trotzdem.
set -euo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
WS="${1:?Workspace-Pfad angeben}"
MODE="${2:-}"
mkdir -p "$WS/skills"
cp -R "$SRC/skills/steuerwiki" "$SRC/skills/steuerwiki-pflege" "$SRC/skills/steuererklaerung-np" \
      "$SRC/skills/belege-ablage" "$WS/skills/"
# L1-Werkzeug: Index bauen, falls er fehlt (nur Python-Standardbibliothek zur Laufzeit)
[ -f "$SRC/index/lookup.json" ] || python3 "$SRC/tools/build_lookup.py"
DEST="$WS/steuerwiki"
mkdir -p "$DEST"
cp -R "$SRC"/. "$DEST/"
rm -rf "$DEST/.git" "$DEST/dist"
if [ "$MODE" = "--extrapaths" ]; then
  # mtime = Installationszeitpunkt, damit alle Wiki-Dateien gleich gewichtet starten
  find "$DEST" -name '*.md' -exec touch {} +
  echo "Steuer-Wiki installiert in $DEST (extraPaths-Variante)."
  echo "Konfig: memory.search.extraPaths: [{ path: \"steuerwiki\", pattern: \"{quick,wiki,chunks}/**/*.md\" }]"
else
  MEM="$WS/memory/steuerwiki"
  rm -rf "$MEM"
  mkdir -p "$MEM"
  for d in quick wiki chunks; do
    mv "$DEST/$d" "$MEM/$d"
    ln -s "../memory/steuerwiki/$d" "$DEST/$d"
  done
  # Rückverweise, damit relative Links (../../sources/…, ../raw/…) auch aus memory/steuerwiki/ auflösen
  for x in "$DEST"/* ; do
    n="$(basename "$x")"
    case "$n" in quick|wiki|chunks) continue ;; esac
    ln -s "../../steuerwiki/$n" "$MEM/$n"
  done
  echo "Steuer-Wiki installiert: $DEST (Pfade für Skills) · indexiert wird $MEM (memory/, kein Zeitverfall)."
  echo "Keine extraPaths nötig."
fi
python3 "$DEST/tools/steuer.py" index >/dev/null 2>&1 || true   # Volltextindex index/fts.sqlite
echo "Snippet einfügen: $SRC/openclaw/AGENTS.workspace-snippet.md -> $WS/AGENTS.md"
echo "Danach: openclaw memory index --force --agent <agent-id>"
