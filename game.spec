# -*- mode: python ; coding: utf-8 -*-
import os
block_cipher = None


a = Analysis(['game.py'],
             pathex=['E:\\GIT\\black_jack'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

res_files = os.listdir(os.path.join(os.getcwd(), 'res'))

for file_name in res_files:
    path_to_res = os.path.join(os.getcwd(), 'res', file_name)
    a.datas.append(('res/' + file_name, path_to_res, 'DATA'))

#for dir, res in res_info.items():
#    if res:
#        for files in res:
#            path_to_res = os.path.join(cwd_path, dir, files)
#            if os.path.isfile(path_to_res):
#                a.datas.append((dir + '/' + files, path_to_res, 'DATA'))
#                print('Added %s resourse' % path_to_res)
#            else:
#                print('Not found %s resourse' % path_to_res)
#    else:
#        pass

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='game',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
