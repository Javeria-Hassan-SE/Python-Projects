# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['feedback.py'],
    pathex=['C:\\Users\\HP\\PycharmProjects\\Feedback'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
a.datas += [('logo.jpg','C:\\Users\\HP\\PycharmProjects\\Feedback\\logo.jpg', "DATA"),
	('navttc-logo.png','C:\\Users\\HP\\PycharmProjects\\Feedback\\navttc-logo.png', "DATA"),
	('pytogsheets-358505-07ea97ee0197.json','C:\\Users\\HP\\PycharmProjects\\Feedback\\pytogsheets-358505-07ea97ee0197.json', "DATA")]

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Feedback',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='C:\\Users\\HP\\PycharmProjects\\Feedback\\navttc-logo.png',
)
