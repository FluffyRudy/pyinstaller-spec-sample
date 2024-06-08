# <filename>.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['/home/<user>/Documents/<project_name>/main.py'],
    pathex=['/home/<user>/Documents/<project_name>'],
    binaries=[],
    datas=[
      ('/home/<user>/Documents/<project_name>/graphics/', 'graphics'),
      ('/home/<user>/Documents/<project_name>/maps/tmx/', 'maps/tmx'),
      ('/home/<user>/Documents/<project_name>/maps/tsx/', 'maps/tsx'),
      ('/home/<user>/Documents/<project_name>/audio/', 'audio')
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='<project_name>_game',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='<project_name>',
)
