#!/usr/bin/env python2

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum-PAC requires Python version >= 2.7.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-PAC.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-PAC.png'])
    ]

setup(
    name="Electrum-PAC",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'pyaes',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'protobuf',
        'dnspython',
        'jsonrpclib',
        'PySocks>=1.6.6',
        'trezor>=0.6.3',
        'x11_hash>=1.4',
    ],
    dependency_links=[
        'git+https://github.com/akhavr/x11_hash@1.4#egg=x11_hash-1.4',
        'git+https://github.com/electrum-dash/python-trezor@v0.6.13#egg=trezor',
    ],
    packages=[
        'electrum_PAC',
        'electrum_PAC_gui',
        'electrum_PAC_gui.qt',
        'electrum_PAC_plugins',
        'electrum_PAC_plugins.audio_modem',
        'electrum_PAC_plugins.cosigner_pool',
        'electrum_PAC_plugins.email_requests',
        'electrum_PAC_plugins.hw_wallet',
        'electrum_PAC_plugins.keepkey',
        'electrum_PAC_plugins.labels',
        'electrum_PAC_plugins.ledger',
        'electrum_PAC_plugins.trezor',
        'electrum_PAC_plugins.digitalbitbox',
        'electrum_PAC_plugins.virtualkeyboard',
    ],
    package_dir={
        'electrum_PAC': 'lib',
        'electrum_PAC_gui': 'gui',
        'electrum_PAC_plugins': 'plugins',
    },
    package_data={
        'electrum_PAC': [
            'currencies.json',
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['electrum-PAC'],
    data_files=data_files,
    description="Lightweight $PAC Wallet",
    author="akhavr",
    license="MIT License",
    url="https://paccoin.net",
    long_description="""Lightweight $PAC Wallet"""
)
