# -*- mode: python -*-

block_cipher = None


a = Analysis(['Crawl.py'],
             pathex=['C:\\Users\\Administrator.EXHS-2715dom\\PycharmProjects\\CrwalDaily'],
             binaries=[],
             datas=[('C:\\Users\\Administrator.EXHS-2715dom\\PycharmProjects\\CrwalDaily\\venv\\lib\\python3.7\\site-packages\\docx\\templates',"docx/templates")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Crawl',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
