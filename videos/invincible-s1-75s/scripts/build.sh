#!/bin/sh
# build index.html, then duck the music under the voice (carve)
set -e
cd "$(dirname "$0")/.."
python3 scripts/make_audio.py
python3 scripts/build_scenes.py
V=""; for i in 01 02 03 04 05 06 07 08 09 10; do V="$V --voice vo$i"; done
node /root/.claude/plugins/cache/hyperframes/hyperframes/0.8.169/skills/hyperframes-audio/scripts/carve.mjs --comp index.html --bed bgm $V --core "${CORE:?set CORE to a dir with @hyperframes/core}"
