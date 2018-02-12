Electrum-PAC - Lightweight PAC client
=====================================

::

  Licence: MIT Licence
  Author: Thomas Voegtlin
  Homepage: https://electrum-PAC.org/
  Language: Python (>= 3.6)


.. image:: https://travis-ci.org/akhavr/electrum-PAC.svg?branch=develop
    :target: https://travis-ci.org/akhavr/electrum-PAC
    :alt: Build Status





Getting started
===============

Electrum-PAC is a pure python application. If you want to use the
Qt interface, install the Qt dependencies::

Use PPA setup
-------------

If you downloaded the official package (tar.gz), you can run
Electrum-PAC from its root directory, without installing it on your
system; all the python dependencies are included in the 'packages'
directory. To run Electrum-PAC from its root directory, just do::

    ./electrum-PAC

You can also install Electrum-PAC on your system, by running this command::

Use source distribution
-----------------------

This will download and install the Python dependencies used by
Electrum-PAC, instead of using the 'packages' directory.
Dash Electrum is a pure python application. If you want to use the
Qt interface, install the Qt dependencies::

If you cloned the git repository, you need to compile extra files
before you can run Electrum-PAC. Read the next section, "Development
Version".
    sudo apt-get install python3-pyqt5

If you downloaded the official package (tar.gz), you can run
Dash Electrum from its root directory without installing it on your
system; all the python dependencies are included in the 'packages'
directory (except x11-hash).

To install x11-hash dependency in the 'packages' dir run once::

    python3 -m pip install -t packages x11-hash

To install precise tested versions of HW libs (trezor, ledeger, etc) run once::

    git clone https://github.com/akhavr/electrum-PAC
    cd electrum-PAC
    python3 -m pip install -t packages -r contrib/deterministic-build/requirements-hw.txt

To install precise tested version of pyqt5 run once::

    python3 -m pip install -t packages -r contrib/deterministic-build/requirements-binaries.txt

To run Dash Electrum from its root directory, just do::

    ./electrum-dash

You can also install Dash Electrum on your system, by running this command::

    sudo apt-get install python3-setuptools
    python3 -m pip install .[fast]

This will download and install the Python dependencies used by
Dash Electrum instead of using the 'packages' directory.
The 'fast' extra contains some optional dependencies that we think
are often useful but they are not strictly needed.

If you cloned the git repository, you need to compile extra files
before you can run Dash Electrum. Read the next section, "Development
Version".


Using Tor proxy
===============

Starting from Dash Electrum release 3.2.3.1 automatic Tor Proxy
detection and use on wallet startup is added to
`Network <docs/tor/tor-proxy-on-startup.md>`_ preferences.

To use Tor Proxy on Ubuntu set it up with::

    sudo apt-get install tor
    sudo service tor start

Other platforms setup is described at `docs/tor.md <docs/tor.md>`_

Development version
===================

Check out the code from GitHub::

    git clone https://github.com/akhavr/electrum-dash.git
    cd electrum-dash

Run install (this should install dependencies)::

    python3 -m pip install .[fast]


Compile the protobuf description file::

    sudo apt-get install protobuf-compiler
    protoc --proto_path=electrum_dash --python_out=electrum_dash electrum_dash/paymentrequest.proto

Create translations (optional)::

    sudo apt-get install python-requests gettext
    ./contrib/make_locale
