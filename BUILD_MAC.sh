#!/bin/bash
# Build One PDF Editor for macOS (run on a Mac, or use GitHub Actions)
set -e
cd "$(dirname "$0")"
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m PyInstaller --noconfirm OfflinePDFEditor-mac.spec
echo "Done: dist/OnePDFEditor.app"
