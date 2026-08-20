# -*- mode: python ; coding: utf-8 -*-
# One PDF Editor – macOS .app bundle

block_cipher = None

a = Analysis(
    ['app/main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('assets/icon_256.png', 'assets'),
        ('assets/icon_128.png', 'assets'),
        ('assets/icon_64.png', 'assets'),
        ('assets/icon_32.png', 'assets'),
        ('assets/OnePDFEditor.ico', 'assets'),
        ('assets/dashboard', 'assets/dashboard'),
        ('assets/fonts', 'assets/fonts'),
    ],
    hiddenimports=[
        'pymupdf', 'fitz',
        'PIL', 'PIL.Image', 'PIL.ImageDraw', 'PIL.ImageTk',
        'PIL.ImageEnhance', 'PIL.ImageFilter',
        'tkinter', 'tkinter.ttk', 'tkinter.filedialog',
        'tkinter.messagebox', 'tkinter.simpledialog',
        'docx',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib', 'numpy', 'scipy', 'pandas',
        'PyQt5', 'PyQt6', 'PySide2', 'PySide6',
        'IPython', 'jupyter',
        'win32api', 'win32com', 'pythoncom', 'windnd',
    ],
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='OnePDFEditor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(
    exe,
    name='OnePDFEditor.app',
    icon=None,
    bundle_identifier='studio.yumdrop.onepdfeditor',
    info_plist={
        'CFBundleName': 'One PDF Editor',
        'CFBundleDisplayName': 'One PDF Editor',
        'CFBundleShortVersionString': '1.0',
        'CFBundleVersion': '1.0',
        'NSHighResolutionCapable': True,
        'LSMinimumSystemVersion': '10.15',
    },
)
