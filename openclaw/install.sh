#!/usr/bin/env bash
# Kopiert das Steuer-Wiki in einen OpenClaw-Workspace.
#   ./openclaw/install.sh <workspace-pfad> [--memory]
#   --memory : indexierbare Teile (quick, wiki, chunks + index.md, AGENTS.md) nach <ws>/memory/steuerwiki/ (immer «evergreen»),
#              Volltexte/Originale nach <ws>/steuerwiki-archiv/ (nicht indexiert). Standard: alles nach <ws>/steuerwiki/.
set -euo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
WS="${1:?Workspace-Pfad angeben}"
MODE="${2:-}"
mkdir -p "$WS/skills"
cp -R "$SRC/skills/steuerwiki" "$SRC/skills/steuerwiki-pflege" "$WS/skills/"
if [ "$MODE" = "--memory" ]; then
  DEST="$WS/memory/steuerwiki"; ARCH="$WS/steuerwiki-archiv"
  mkdir -p "$DEST" "$ARCH"
  cp -R "$SRC/quick" "$SRC/wiki" "$SRC/chunks" "$SRC/index.md" "$SRC/AGENTS.md" "$DEST/"
  cp -R "$SRC/sources" "$SRC/raw" "$SRC/index" "$SRC/registry" "$SRC/data" "$SRC/tools" "$SRC/README.md" "$ARCH/"
  echo "Hinweis: Links aus memory/steuerwiki nach sources/ bzw. raw/ zeigen nun auf $ARCH (relativ nicht auflösbar)."
else
  DEST="$WS/steuerwiki"
  mkdir -p "$DEST"
  cp -R "$SRC"/. "$DEST/"
  rm -rf "$DEST/.git"
fi
find "$DEST" -name '*.md' -exec touch -d "2026-01-01" {} +
echo "Steuer-Wiki installiert in $DEST. Snippet einfügen: $SRC/openclaw/AGENTS.workspace-snippet.md -> $WS/AGENTS.md"
echo "Danach: openclaw memory index --force --agent <agent-id>"
