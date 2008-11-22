# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/anilet/Bhima/python/atlas/ui/progressDlg.ui'
#
# Created: Fri Nov 14 21:22:44 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_progressDlg(object):
    def setupUi(self, progressDlg):
        progressDlg.setObjectName("progressDlg")
        progressDlg.setWindowModality(QtCore.Qt.ApplicationModal)
        progressDlg.resize(349, 94)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/16x16/actions/appointment-new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        progressDlg.setWindowIcon(icon)
        self.progressBar = QtGui.QProgressBar(progressDlg)
        self.progressBar.setGeometry(QtCore.QRect(10, 20, 331, 23))
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", QtCore.QVariant(23928))
        self.progressBar.setObjectName("progressBar")
        self.lblMessage = QtGui.QLabel(progressDlg)
        self.lblMessage.setGeometry(QtCore.QRect(10, 60, 341, 17))
        self.lblMessage.setObjectName("lblMessage")

        self.retranslateUi(progressDlg)
        QtCore.QMetaObject.connectSlotsByName(progressDlg)

    def retranslateUi(self, progressDlg):
        progressDlg.setWindowTitle(QtGui.QApplication.translate("progressDlg", "Saving daily time", None, QtGui.QApplication.UnicodeUTF8))
        self.lblMessage.setText(QtGui.QApplication.translate("progressDlg", "Saving data...", None, QtGui.QApplication.UnicodeUTF8))

import smeTime_rc
