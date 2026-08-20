One PDF Editor — macOS (MacBook)
================================
Use GitHub Actions (macos-latest) OR build on a Mac.

A) GitHub Actions (recommended)
-------------------------------
1. Upload to GitHub (include):
   - app/main.py
   - OfflinePDFEditor-mac.spec
   - .github/workflows/build-macos.yml
   - requirements.txt
   - assets/ (fonts, dashboard, icons)

2. Actions → "Build macOS APP" → Run workflow

3. Download artifact: OnePDFEditor-macOS.zip
   Unzip → OnePDFEditor.app

4. First open on Mac:
   Right-click OnePDFEditor.app → Open
   (or System Settings → Privacy & Security → Allow)

B) Build on a Mac
-----------------
  chmod +x BUILD_MAC.sh
  ./BUILD_MAC.sh
  open dist/OnePDFEditor.app

Notes
-----
- Windows-only features: windnd drag-drop, MS Word COM convert, Windows print dialog
- On Mac: open files via Open button; Print opens Preview
- Command+O / Command+S shortcuts work
