# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/anilet/python/python/atlas/ui/atlasTime.ui'
#
# Created: Sun Sep 28 20:18:10 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_atlasTimeDlg(object):
    def setupUi(self, atlasTimeDlg):
        atlasTimeDlg.setObjectName("atlasTimeDlg")
        atlasTimeDlg.resize(885, 618)
        self.verticalLayout_4 = QtGui.QVBoxLayout(atlasTimeDlg)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.headLabel = QtGui.QLabel(atlasTimeDlg)
        self.headLabel.setObjectName("headLabel")
        self.horizontalLayout_5.addWidget(self.headLabel)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.userLabel = QtGui.QLabel(atlasTimeDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userLabel.sizePolicy().hasHeightForWidth())
        self.userLabel.setSizePolicy(sizePolicy)
        self.userLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userLabel.setObjectName("userLabel")
        self.horizontalLayout_4.addWidget(self.userLabel)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.timeCalendar = QtGui.QCalendarWidget(atlasTimeDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeCalendar.sizePolicy().hasHeightForWidth())
        self.timeCalendar.setSizePolicy(sizePolicy)
        self.timeCalendar.setGridVisible(True)
        self.timeCalendar.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.timeCalendar.setObjectName("timeCalendar")
        self.verticalLayout_2.addWidget(self.timeCalendar)
        self.dailyTimeGP = QtGui.QGroupBox(atlasTimeDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dailyTimeGP.sizePolicy().hasHeightForWidth())
        self.dailyTimeGP.setSizePolicy(sizePolicy)
        self.dailyTimeGP.setMinimumSize(QtCore.QSize(0, 140))
        self.dailyTimeGP.setObjectName("dailyTimeGP")
        self.verticalLayout = QtGui.QVBoxLayout(self.dailyTimeGP)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtGui.QLabel(self.dailyTimeGP)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.inLineEdit = QtGui.QLineEdit(self.dailyTimeGP)
        self.inLineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.inLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.inLineEdit.setMaxLength(5)
        self.inLineEdit.setObjectName("inLineEdit")
        self.horizontalLayout_3.addWidget(self.inLineEdit)
        self.inComboBox = QtGui.QComboBox(self.dailyTimeGP)
        self.inComboBox.setObjectName("inComboBox")
        self.inComboBox.addItem(QtCore.QString())
        self.inComboBox.addItem(QtCore.QString())
        self.horizontalLayout_3.addWidget(self.inComboBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.dailyTimeGP)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.outLineEdit = QtGui.QLineEdit(self.dailyTimeGP)
        self.outLineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.outLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.outLineEdit.setMaxLength(5)
        self.outLineEdit.setObjectName("outLineEdit")
        self.horizontalLayout_3.addWidget(self.outLineEdit)
        self.outComboBox = QtGui.QComboBox(self.dailyTimeGP)
        self.outComboBox.setObjectName("outComboBox")
        self.outComboBox.addItem(QtCore.QString())
        self.outComboBox.addItem(QtCore.QString())
        self.horizontalLayout_3.addWidget(self.outComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.noBreakCheckBox = QtGui.QCheckBox(self.dailyTimeGP)
        self.noBreakCheckBox.setObjectName("noBreakCheckBox")
        self.verticalLayout.addWidget(self.noBreakCheckBox)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.totalHourdLabel = QtGui.QLabel(self.dailyTimeGP)
        self.totalHourdLabel.setObjectName("totalHourdLabel")
        self.horizontalLayout_7.addWidget(self.totalHourdLabel)
        self.addDailyTimeButton = QtGui.QPushButton(self.dailyTimeGP)
        self.addDailyTimeButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.addDailyTimeButton.setObjectName("addDailyTimeButton")
        self.horizontalLayout_7.addWidget(self.addDailyTimeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.dailyTimeGP)
        self.statGP = QtGui.QGroupBox(atlasTimeDlg)
        self.statGP.setMinimumSize(QtCore.QSize(0, 171))
        self.statGP.setObjectName("statGP")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.statGP)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dateLabel = QtGui.QLabel(self.statGP)
        self.dateLabel.setObjectName("dateLabel")
        self.gridLayout.addWidget(self.dateLabel, 0, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.statGP)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.dayLable = QtGui.QLabel(self.statGP)
        self.dayLable.setObjectName("dayLable")
        self.gridLayout.addWidget(self.dayLable, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.statGP)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.weekLabel = QtGui.QLabel(self.statGP)
        self.weekLabel.setObjectName("weekLabel")
        self.gridLayout.addWidget(self.weekLabel, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.statGP)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.monthLabel = QtGui.QLabel(self.statGP)
        self.monthLabel.setObjectName("monthLabel")
        self.gridLayout.addWidget(self.monthLabel, 3, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.statGP)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.yearLabel = QtGui.QLabel(self.statGP)
        self.yearLabel.setObjectName("yearLabel")
        self.gridLayout.addWidget(self.yearLabel, 4, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.statGP)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.hourView = QtGui.QTableView(atlasTimeDlg)
        self.hourView.setObjectName("hourView")
        self.horizontalLayout_8.addWidget(self.hourView)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtGui.QPushButton(atlasTimeDlg)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtGui.QPushButton(atlasTimeDlg)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.helpTextBrowser = QtGui.QTextBrowser(atlasTimeDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helpTextBrowser.sizePolicy().hasHeightForWidth())
        self.helpTextBrowser.setSizePolicy(sizePolicy)
        self.helpTextBrowser.setMaximumSize(QtCore.QSize(16777215, 100))
        self.helpTextBrowser.setFrameShape(QtGui.QFrame.Box)
        self.helpTextBrowser.setFrameShadow(QtGui.QFrame.Plain)
        self.helpTextBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.helpTextBrowser.setObjectName("helpTextBrowser")
        self.verticalLayout_3.addWidget(self.helpTextBrowser)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.line = QtGui.QFrame(atlasTimeDlg)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtGui.QSpacerItem(648, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.buttonBox = QtGui.QDialogButtonBox(atlasTimeDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.retranslateUi(atlasTimeDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), atlasTimeDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), atlasTimeDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(atlasTimeDlg)

    def retranslateUi(self, atlasTimeDlg):
        atlasTimeDlg.setWindowTitle(QtGui.QApplication.translate("atlasTimeDlg", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.headLabel.setText(QtGui.QApplication.translate("atlasTimeDlg", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.userLabel.setText(QtGui.QApplication.translate("atlasTimeDlg", "Select User", None, QtGui.QApplication.UnicodeUTF8))
        self.dailyTimeGP.setTitle(QtGui.QApplication.translate("atlasTimeDlg", "Daily Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("atlasTimeDlg", "Time In:", None, QtGui.QApplication.UnicodeUTF8))
        self.inLineEdit.setToolTip(QtGui.QApplication.translate("atlasTimeDlg", "Enter time in in the format 12:30", None, QtGui.QApplication.UnicodeUTF8))
        self.inComboBox.setItemText(0, QtGui.QApplication.translate("atlasTimeDlg", "AM", None, QtGui.QApplication.UnicodeUTF8))
        self.inComboBox.setItemText(1, QtGui.QApplication.translate("atlasTimeDlg", "PM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("atlasTimeDlg", "Time Out:", None, QtGui.QApplication.UnicodeUTF8))
        self.outLineEdit.setToolTip(QtGui.QApplication.translate("atlasTimeDlg", "Enter time in 12:30 format", None, QtGui.QApplication.UnicodeUTF8))
        self.outComboBox.setItemText(0, QtGui.QApplication.translate("atlasTimeDlg", "PM", None, QtGui.QApplication.UnicodeUTF8))
        self.outComboBox.setItemText(1, QtGui.QApplication.translate("atlasTimeDlg", "AM", None, QtGui.QApplication.UnicodeUTF8))
        self.noBreakCheckBox.setText(QtGui.QApplication.translate("atlasTimeDlg", "No Lunch Break", None, QtGui.QApplication.UnicodeUTF8))
        self.totalHourdLabel.setText(QtGui.QApplication.translate("atlasTimeDlg", "Total Hours Worked", None, QtGui.QApplication.UnicodeUTF8))
        self.addDailyTimeButton.setText(QtGui.QApplication.translate("atlasTimeDlg", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.statGP.setTitle(QtGui.QApplication.translate("atlasTimeDlg", "Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.dateLabel.setText(QtGui.QApplication.translate("atlasTimeDlg", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("atlasTimeDlg", "Total Hours for Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.dayLable.setText(QtGui.QApplication.translate("atlasTimeDlg", "day", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("atlasTimeDlg", "Total Hours for the Week", None, QtGui.QApplication.UnicodeUTF8))
        self.weekLabel.setText(QtGui.QApplication.translate("atlasTimeDlg", "week", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("atlasTimeDlg", "Total Hours for the Month", None, QtGui.QApplication.UnicodeUTF8))
        self.monthLabel.setText(QtGui.QApplication.translate("atlasTimeDlg", "month", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("atlasTimeDlg", "Total hours for the year:", None, QtGui.QApplication.UnicodeUTF8))
        self.yearLabel.setText(QtGui.QApplication.translate("atlasTimeDlg", "year", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("atlasTimeDlg", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("atlasTimeDlg", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.helpTextBrowser.setHtml(QtGui.QApplication.translate("atlasTimeDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\';\">Please select a date from the calendar to see the hours worked</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI\';\"><span style=\" font-weight:600; color:#0000ff;\">Doubble click</span> on a date to edit/enter worked hours</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

