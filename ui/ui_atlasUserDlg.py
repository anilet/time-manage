# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/anilet/Bhima/python/atlas/ui/atlasUserDlg.ui'
#
# Created: Mon Nov 10 22:20:13 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_atlasUserDlg(object):
    def setupUi(self, atlasUserDlg):
        atlasUserDlg.setObjectName("atlasUserDlg")
        atlasUserDlg.resize(367, 146)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(atlasUserDlg.sizePolicy().hasHeightForWidth())
        atlasUserDlg.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QtGui.QVBoxLayout(atlasUserDlg)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imageLabel = QtGui.QLabel(atlasUserDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout.addWidget(self.imageLabel)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(17, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.userLabel = QtGui.QLabel(atlasUserDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userLabel.sizePolicy().hasHeightForWidth())
        self.userLabel.setSizePolicy(sizePolicy)
        self.userLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userLabel.setObjectName("userLabel")
        self.gridLayout.addWidget(self.userLabel, 0, 1, 1, 1)
        self.userComboBox = QtGui.QComboBox(atlasUserDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userComboBox.sizePolicy().hasHeightForWidth())
        self.userComboBox.setSizePolicy(sizePolicy)
        self.userComboBox.setMinimumSize(QtCore.QSize(130, 0))
        self.userComboBox.setObjectName("userComboBox")
        self.gridLayout.addWidget(self.userComboBox, 0, 2, 1, 1)
        self.passLabel = QtGui.QLabel(atlasUserDlg)
        self.passLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passLabel.setObjectName("passLabel")
        self.gridLayout.addWidget(self.passLabel, 1, 1, 1, 1)
        self.passLineEdit = QtGui.QLineEdit(atlasUserDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passLineEdit.sizePolicy().hasHeightForWidth())
        self.passLineEdit.setSizePolicy(sizePolicy)
        self.passLineEdit.setMinimumSize(QtCore.QSize(81, 0))
        self.passLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passLineEdit.setObjectName("passLineEdit")
        self.gridLayout.addWidget(self.passLineEdit, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(atlasUserDlg)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtGui.QSpacerItem(218, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.cancelButton = QtGui.QPushButton(atlasUserDlg)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.okButton = QtGui.QPushButton(atlasUserDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_2.addWidget(self.okButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.userLabel.setBuddy(self.userComboBox)
        self.passLabel.setBuddy(self.passLineEdit)

        self.retranslateUi(atlasUserDlg)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL("clicked()"), atlasUserDlg.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), atlasUserDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(atlasUserDlg)
        atlasUserDlg.setTabOrder(self.userComboBox, self.okButton)
        atlasUserDlg.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, atlasUserDlg):
        atlasUserDlg.setWindowTitle(QtGui.QApplication.translate("atlasUserDlg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.imageLabel.setText(QtGui.QApplication.translate("atlasUserDlg", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.userLabel.setText(QtGui.QApplication.translate("atlasUserDlg", "Select User Name", None, QtGui.QApplication.UnicodeUTF8))
        self.passLabel.setText(QtGui.QApplication.translate("atlasUserDlg", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("atlasUserDlg", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("atlasUserDlg", "&Ok", None, QtGui.QApplication.UnicodeUTF8))

