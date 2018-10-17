# -*- mode: python -*-

block_cipher = None


a = Analysis(['src/main.py'],
             pathex=['/Users/peter/dev/Peti/codenames-kivy'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['_tkinter', 'Tkinter', 'enchant', 'twisted'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Codenames',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe, Tree("./src"),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='Codenames')
app = BUNDLE(coll,
             name='Codenames.app',
             icon=None,
             bundle_identifier=None)
