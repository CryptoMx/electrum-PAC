# -*- mode: python -*-
import os
import os.path
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules


for i, x in enumerate(sys.argv):
    if x == '--name':
        cmdline_name = sys.argv[i+1]
        break
else:
    raise Exception('no name')

PY36BINDIR =  os.environ.get('PY36BINDIR')

hiddenimports = collect_submodules('trezorlib')
hiddenimports += collect_submodules('safetlib')
hiddenimports += collect_submodules('btchip')
hiddenimports += collect_submodules('keepkeylib')
hiddenimports += collect_submodules('websocket')
hiddenimports += [
    'electrum_pac',
    'electrum_pac.base_crash_reporter',
    'electrum_pac.base_wizard',
    'electrum_pac.plot',
    'electrum_pac.qrscanner',
    'electrum_pac.websockets',
    'electrum_pac.gui.qt',
    'PyQt5.sip',

    'electrum_pac.plugins',

    'electrum_pac.plugins.hw_wallet.qt',

    'electrum_pac.plugins.audio_modem.qt',
    'electrum_pac.plugins.cosigner_pool.qt',
    'electrum_pac.plugins.digitalbitbox.qt',
    'electrum_pac.plugins.email_requests.qt',
    'electrum_pac.plugins.keepkey.qt',
    'electrum_pac.plugins.revealer.qt',
    'electrum_pac.plugins.labels.qt',
    'electrum_pac.plugins.trezor.client',
    'electrum_pac.plugins.trezor.qt',
    'electrum_pac.plugins.safe_t.client',
    'electrum_pac.plugins.safe_t.qt',
    'electrum_pac.plugins.ledger.qt',
    'electrum_pac.plugins.virtualkeyboard.qt',
]

datas = [
    ('electrum_pac/servers.json', 'electrum_pac'),
    ('electrum_pac/servers_testnet.json', 'electrum_pac'),
    ('electrum_pac/servers_regtest.json', 'electrum_pac'),
    ('electrum_pac/currencies.json', 'electrum_pac'),
    ('electrum_pac/checkpoints.json', 'electrum_pac'),
    ('electrum_pac/locale', 'electrum_pac/locale'),
    ('electrum_pac/wordlist', 'electrum_pac/wordlist'),
]
datas += collect_data_files('trezorlib')
datas += collect_data_files('safetlib')
datas += collect_data_files('btchip')
datas += collect_data_files('keepkeylib')

# Add libusb so Trezor and Safe-T mini will work
binaries = [('../libusb-1.0.dylib', '.')]
binaries += [('../libsecp256k1.0.dylib', '.')]
binaries += [('/usr/local/lib/libgmp.10.dylib', '.')]

# https://github.com/pyinstaller/pyinstaller/wiki/Recipe-remove-tkinter-tcl
sys.modules['FixTk'] = None
excludes = ['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter']
excludes += [
    'PyQt5.QtBluetooth',
    'PyQt5.QtCLucene',
    'PyQt5.QtDBus',
    'PyQt5.Qt5CLucene',
    'PyQt5.QtDesigner',
    'PyQt5.QtDesignerComponents',
    'PyQt5.QtHelp',
    'PyQt5.QtLocation',
    'PyQt5.QtMultimedia',
    'PyQt5.QtMultimediaQuick_p',
    'PyQt5.QtMultimediaWidgets',
    'PyQt5.QtNetwork',
    'PyQt5.QtNetworkAuth',
    'PyQt5.QtNfc',
    'PyQt5.QtOpenGL',
    'PyQt5.QtPositioning',
    'PyQt5.QtQml',
    'PyQt5.QtQuick',
    'PyQt5.QtQuickParticles',
    'PyQt5.QtQuickWidgets',
    'PyQt5.QtSensors',
    'PyQt5.QtSerialPort',
    'PyQt5.QtSql',
    'PyQt5.Qt5Sql',
    'PyQt5.Qt5Svg',
    'PyQt5.QtTest',
    'PyQt5.QtWebChannel',
    'PyQt5.QtWebEngine',
    'PyQt5.QtWebEngineCore',
    'PyQt5.QtWebEngineWidgets',
    'PyQt5.QtWebKit',
    'PyQt5.QtWebKitWidgets',
    'PyQt5.QtWebSockets',
    'PyQt5.QtXml',
    'PyQt5.QtXmlPatterns',
    'PyQt5.QtWebProcess',
    'PyQt5.QtWinExtras',
]

a = Analysis(['electrum-pac'],
             hiddenimports=hiddenimports,
             datas=datas,
             binaries=binaries,
             excludes=excludes,
             runtime_hooks=['pyi_runtimehook.py'])

# http://stackoverflow.com/questions/19055089/
for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          debug=False,
          strip=False,
          upx=False,
          console=False,
          icon='icons/electrum-pac.ico',
          name=os.path.join('build/electrum-pac/electrum-pac', cmdline_name))

# trezorctl separate bin
tctl_a = Analysis([os.path.join(PY36BINDIR, 'trezorctl')],
                  hiddenimports=['pkgutil'],
                  excludes=excludes,
                  runtime_hooks=['pyi_tctl_runtimehook.py'])

tctl_pyz = PYZ(tctl_a.pure)

tctl_exe = EXE(tctl_pyz,
           tctl_a.scripts,
           exclude_binaries=True,
           debug=False,
           strip=False,
           upx=False,
           console=True,
           name=os.path.join('build/electrum-pac/electrum-pac', 'trezorctl.bin'))

coll = COLLECT(exe, #tctl_exe,
               a.binaries,
               a.datas,
               strip=False,
               upx=False,
               name=os.path.join('dist', 'electrum-pac'))

app = BUNDLE(coll,
             name=os.path.join('dist', 'Pac-Electrum.app'),
             appname="Pac-Electrum",
	         icon='electrum-pac.icns',
             version = 'ELECTRUM_VERSION')
