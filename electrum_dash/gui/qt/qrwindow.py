#!/usr/bin/env python
#
# Electrum - lightweight Bitcoin client
# Copyright (C) 2014 Thomas Voegtlin
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget

from .qrcodewidget import QRCodeWidget

<<<<<<< refs/remotes/upstream/master:electrum_dash/gui/qt/qrwindow.py
from electrum_dash.i18n import _
=======
from electrum_PAC_gui.qt.qrcodewidget import QRCodeWidget
from electrum_PAC.i18n import _
>>>>>>> Rebranding for PAC:gui/qt/qrwindow.py


class QR_Window(QWidget):

    def __init__(self, win):
        QWidget.__init__(self)
        self.win = win
<<<<<<< refs/remotes/upstream/master:electrum_dash/gui/qt/qrwindow.py
        self.setWindowTitle('Dash Electrum - '+_('Payment Request'))
        self.setMinimumSize(800, 800)
        self.setFocusPolicy(Qt.NoFocus)
=======
        self.setWindowTitle('Electrum-PAC - '+_('Payment Request'))
        self.setMinimumSize(800, 250)
        self.address = ''
        self.label = ''
        self.amount = 0
        self.setFocusPolicy(QtCore.Qt.NoFocus)

>>>>>>> Rebranding for PAC:gui/qt/qrwindow.py
        main_box = QHBoxLayout()
        self.qrw = QRCodeWidget()
        main_box.addWidget(self.qrw, 1)
        self.setLayout(main_box)
