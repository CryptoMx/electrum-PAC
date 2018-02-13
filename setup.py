#!/usr/bin/env python3

# python setup.py sdist --format=zip,gztar

import os
import sys
import platform
import importlib.util
import argparse
import subprocess

from setuptools import setup, find_packages
from setuptools.command.install import install

MIN_PYTHON_VERSION = "3.6.1"
_min_python_version_tuple = tuple(map(int, (MIN_PYTHON_VERSION.split("."))))


if sys.version_info[:3] < _min_python_version_tuple:
    sys.exit("Error: Dash Electrum requires Python version >= %s..." % MIN_PYTHON_VERSION)

with open('contrib/requirements/requirements.txt') as f:
    requirements = f.read().splitlines()

with open('contrib/requirements/requirements-hw.txt') as f:
    requirements_hw = f.read().splitlines()

# load version.py; needlessly complicated alternative to "imp.load_source":
version_spec = importlib.util.spec_from_file_location('version', 'electrum_dash/version.py')
version_module = version = importlib.util.module_from_spec(version_spec)
version_spec.loader.exec_module(version_module)

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    icons_dirname = 'pixmaps'
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        icons_dirname = 'icons'
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-PAC.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-PAC.png'])
    ]

extras_require = {
    'hardware': requirements_hw,
    'fast': ['pycryptodomex'],
    'gui': ['pyqt5'],
}
extras_require['full'] = [pkg for sublist in list(extras_require.values()) for pkg in sublist]


setup(
    name="Electrum-PAC",
    version=version.ELECTRUM_VERSION,
    python_requires='>={}'.format(MIN_PYTHON_VERSION),
    install_requires=requirements,
    extras_require=extras_require,
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
        '': ['*.txt', '*.json', '*.ttf', '*.otf'],
        'electrum_PAC': [
            'currencies.json',
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ],
        'electrum_dash.gui': [
            'icons/*.*',
            'icons/radio/*.*',
            'icons/checkbox/*.*',
        ],
    },
    scripts=['electrum-PAC'],
    data_files=data_files,
    description="Lightweight $PAC Wallet",
    author="akhavr",
    maintainer_email="akhavr@khavr.com",
    license="MIT License",
    url="https://paccoin.net",
    long_description="""Lightweight $PAC Wallet"""
)
