# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/anilet/python/atlas/ui/login.ui'
#
# Created: Sat Oct 11 23:47:39 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_atlasUserDlg(object):
    def setupUi(self, atlasUserDlg):
        atlasUserDlg.setObjectName("atlasUserDlg")
        atlasUserDlg.resize(411,167)
        self.verticalLayout = QtGui.QVBoxLayout(atlasUserDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.imageLabel = QtGui.QLabel(atlasUserDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout_3.addWidget(self.imageLabel)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userLabel = QtGui.QLabel(atlasUserDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userLabel.sizePolicy().hasHeightForWidth())
        self.userLabel.setSizePolicy(sizePolicy)
        self.userLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userLabel.setObjectName("userLabel")
        self.horizontalLayout.addWidget(self.userLabel)
        self.userComboBox = QtGui.QComboBox(atlasUserDlg)
        self.userComboBox.setObjectName("userComboBox")
        self.horizontalLayout.addWidget(self.userComboBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtGui.QFrame(atlasUserDlg)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(218,17,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cancelButton = QtGui.QPushButton(atlasUserDlg)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.pushButton_2 = QtGui.QPushButton(atlasUserDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.userLabel.setBuddy(self.userComboBox)

        self.retranslateUi(atlasUserDlg)
        QtCore.QMetaObject.connectSlotsByName(atlasUserDlg)

    def retranslateUi(self, atlasUserDlg):
        atlasUserDlg.setWindowTitle(QtGui.QApplication.translate("atlasUserDlg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.imageLabel.setText(QtGui.QApplication.translate("atlasUserDlg", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.userLabel.setText(QtGui.QApplication.translate("atlasUserDlg", "Select User Name", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("atlasUserDlg", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("atlasUserDlg", "&Ok", None, QtGui.QApplication.UnicodeUTF8))

