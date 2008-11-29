# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/anilet/atlas/time-manage/ui/controlprogressindicator.ui'
#
# Created: Fri Nov 28 22:29:44 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ControlProgressIndicator(object):
    def setupUi(self, ControlProgressIndicator):
        ControlProgressIndicator.setObjectName("ControlProgressIndicator")
        ControlProgressIndicator.resize(400, 64)
        self.verticalLayout = QtGui.QVBoxLayout(ControlProgressIndicator)
        self.verticalLayout.setObjectName("verticalLayout")
        self.statusLabel = QtGui.QLabel(ControlProgressIndicator)
        self.statusLabel.setObjectName("statusLabel")
        self.verticalLayout.addWidget(self.statusLabel)
        self.progressBar = QtGui.QProgressBar(ControlProgressIndicator)
        self.progressBar.setProperty("value", QtCore.QVariant(775))
        self.progressBar.setMaximum(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(ControlProgressIndicator)
        QtCore.QMetaObject.connectSlotsByName(ControlProgressIndicator)

    def retranslateUi(self, ControlProgressIndicator):
        self.statusLabel.setText(QtGui.QApplication.translate("ControlProgressIndicator", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

