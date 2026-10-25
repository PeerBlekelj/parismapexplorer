#!/usr/bin/env bash
# Download the Basel scan of the Truschet & Hoyau plan (public domain, ~98 MB) into source/.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p source
curl -fL -A "parismapexplorer/0.1 (https://github.com/PeerBlekelj/parismapexplorer)" -o source/basel.jpg \
  "https://upload.wikimedia.org/wikipedia/commons/c/cb/Map_of_Paris_by_Truschet_and_Hoyau_-_Basel_University_Library.jpg"
