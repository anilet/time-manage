# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/anilet/Bhima/python/atlas/ui/mainWindow.ui'
#
# Created: Tue Nov 18 22:04:18 2008
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(868, 583)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/editmirror.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabTime = QtGui.QWidget()
        self.tabTime.setObjectName("tabTime")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabTime)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calenderDay = QtGui.QCalendarWidget(self.tabTime)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calenderDay.sizePolicy().hasHeightForWidth())
        self.calenderDay.setSizePolicy(sizePolicy)
        self.calenderDay.setMinimumSize(QtCore.QSize(200, 150))
        self.calenderDay.setMinimumDate(QtCore.QDate(1752, 9, 15))
        self.calenderDay.setFirstDayOfWeek(QtCore.Qt.Wednesday)
        self.calenderDay.setGridVisible(True)
        self.calenderDay.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.calenderDay.setObjectName("calenderDay")
        self.horizontalLayout.addWidget(self.calenderDay)
        self.dayChartLabel = MPL_Widget(self.tabTime)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dayChartLabel.sizePolicy().hasHeightForWidth())
        self.dayChartLabel.setSizePolicy(sizePolicy)
        self.dayChartLabel.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.dayChartLabel.setAcceptDrops(False)
 #       self.dayChartLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dayChartLabel.setObjectName("dayChartLabel")
        self.horizontalLayout.addWidget(self.dayChartLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.label_3 = QtGui.QLabel(self.tabTime)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dailyTimeGP = QtGui.QGroupBox(self.tabTime)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dailyTimeGP.sizePolicy().hasHeightForWidth())
        self.dailyTimeGP.setSizePolicy(sizePolicy)
        self.dailyTimeGP.setMinimumSize(QtCore.QSize(0, 140))
        self.dailyTimeGP.setObjectName("dailyTimeGP")
        self.verticalLayout = QtGui.QVBoxLayout(self.dailyTimeGP)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.dailyTimeGP)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inLineEdit = QtGui.QLineEdit(self.dailyTimeGP)
        self.inLineEdit.setMinimumSize(QtCore.QSize(50, 27))
        self.inLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.inLineEdit.setMaxLength(5)
        self.inLineEdit.setObjectName("inLineEdit")
        self.gridLayout.addWidget(self.inLineEdit, 0, 1, 1, 2)
        self.inComboBox = QtGui.QComboBox(self.dailyTimeGP)
        self.inComboBox.setObjectName("inComboBox")
        self.inComboBox.addItem(QtCore.QString())
        self.inComboBox.addItem(QtCore.QString())
        self.gridLayout.addWidget(self.inComboBox, 0, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.dailyTimeGP)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.outComboBox = QtGui.QComboBox(self.dailyTimeGP)
        self.outComboBox.setObjectName("outComboBox")
        self.outComboBox.addItem(QtCore.QString())
        self.outComboBox.addItem(QtCore.QString())
        self.gridLayout.addWidget(self.outComboBox, 1, 4, 1, 1)
        self.outLineEdit = QtGui.QLineEdit(self.dailyTimeGP)
        self.outLineEdit.setMinimumSize(QtCore.QSize(50, 27))
        self.outLineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.outLineEdit.setMaxLength(5)
        self.outLineEdit.setObjectName("outLineEdit")
        self.gridLayout.addWidget(self.outLineEdit, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.noBreakCheckBox = QtGui.QCheckBox(self.dailyTimeGP)
        self.noBreakCheckBox.setEnabled(False)
        self.noBreakCheckBox.setObjectName("noBreakCheckBox")
        self.verticalLayout.addWidget(self.noBreakCheckBox)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.leaveCheckBox = QtGui.QCheckBox(self.dailyTimeGP)
        self.leaveCheckBox.setObjectName("leaveCheckBox")
        self.horizontalLayout_8.addWidget(self.leaveCheckBox)
        self.leaveCombo = QtGui.QComboBox(self.dailyTimeGP)
        self.leaveCombo.setEnabled(False)
        self.leaveCombo.setObjectName("leaveCombo")
        self.leaveCombo.addItem(QtCore.QString())
        self.leaveCombo.addItem(QtCore.QString())
        self.leaveCombo.addItem(QtCore.QString())
        self.leaveCombo.addItem(QtCore.QString())
        self.leaveCombo.addItem(QtCore.QString())
        self.horizontalLayout_8.addWidget(self.leaveCombo)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.totalHourdLabel = QtGui.QLabel(self.dailyTimeGP)
        self.totalHourdLabel.setObjectName("totalHourdLabel")
        self.verticalLayout.addWidget(self.totalHourdLabel)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.totLineEdit = QtGui.QLineEdit(self.dailyTimeGP)
        self.totLineEdit.setEnabled(False)
        self.totLineEdit.setObjectName("totLineEdit")
        self.horizontalLayout_2.addWidget(self.totLineEdit)
        spacerItem = QtGui.QSpacerItem(58, 43, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.editButton = QtGui.QPushButton(self.dailyTimeGP)
        self.editButton.setEnabled(False)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_2.addWidget(self.editButton)
        self.addDailyTimeButton = QtGui.QPushButton(self.dailyTimeGP)
        self.addDailyTimeButton.setEnabled(False)
        self.addDailyTimeButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.addDailyTimeButton.setObjectName("addDailyTimeButton")
        self.horizontalLayout_2.addWidget(self.addDailyTimeButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addWidget(self.dailyTimeGP)
        self.hourView = QtGui.QTableView(self.tabTime)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hourView.sizePolicy().hasHeightForWidth())
        self.hourView.setSizePolicy(sizePolicy)
        self.hourView.setObjectName("hourView")
        self.horizontalLayout_4.addWidget(self.hourView)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtGui.QLabel(self.tabTime)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.jobFilterCombo = QtGui.QComboBox(self.tabTime)
        self.jobFilterCombo.setObjectName("jobFilterCombo")
        self.jobFilterCombo.addItem(QtCore.QString())
        self.jobFilterCombo.addItem(QtCore.QString())
        self.jobFilterCombo.addItem(QtCore.QString())
        self.verticalLayout_3.addWidget(self.jobFilterCombo)
        spacerItem1 = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.buttonDelete = QtGui.QPushButton(self.tabTime)
        self.buttonDelete.setEnabled(False)
        self.buttonDelete.setMinimumSize(QtCore.QSize(0, 41))
        self.buttonDelete.setObjectName("buttonDelete")
        self.verticalLayout_3.addWidget(self.buttonDelete)
        self.buttonNew = QtGui.QPushButton(self.tabTime)
        self.buttonNew.setEnabled(False)
        self.buttonNew.setMinimumSize(QtCore.QSize(0, 41))
        self.buttonNew.setObjectName("buttonNew")
        self.verticalLayout_3.addWidget(self.buttonNew)
        self.buttonSave = QtGui.QPushButton(self.tabTime)
        self.buttonSave.setEnabled(False)
        self.buttonSave.setMinimumSize(QtCore.QSize(0, 41))
        self.buttonSave.setObjectName("buttonSave")
        self.verticalLayout_3.addWidget(self.buttonSave)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tabTime, "")
        self.tabJobs = QtGui.QWidget()
        self.tabJobs.setObjectName("tabJobs")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabJobs)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtGui.QLabel(self.tabJobs)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.jobSearchEdit = QtGui.QLineEdit(self.tabJobs)
        self.jobSearchEdit.setObjectName("jobSearchEdit")
        self.horizontalLayout_5.addWidget(self.jobSearchEdit)
        self.clearButton = QtGui.QToolButton(self.tabJobs)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearButton.setIcon(icon1)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_5.addWidget(self.clearButton)
        self.allJobsButton = QtGui.QPushButton(self.tabJobs)
        self.allJobsButton.setObjectName("allJobsButton")
        self.horizontalLayout_5.addWidget(self.allJobsButton)
        self.currentJobsButton = QtGui.QPushButton(self.tabJobs)
        self.currentJobsButton.setObjectName("currentJobsButton")
        self.horizontalLayout_5.addWidget(self.currentJobsButton)
        self.customerComboBox = QtGui.QComboBox(self.tabJobs)
        self.customerComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.customerComboBox.setObjectName("customerComboBox")
        self.horizontalLayout_5.addWidget(self.customerComboBox)
        self.statusComboBox = QtGui.QComboBox(self.tabJobs)
        self.statusComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.statusComboBox.setObjectName("statusComboBox")
        self.horizontalLayout_5.addWidget(self.statusComboBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tableViewJob = QtGui.QTableView(self.tabJobs)
        self.tableViewJob.setObjectName("tableViewJob")
        self.verticalLayout_5.addWidget(self.tableViewJob)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtGui.QSpacerItem(568, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.openFolderButton = QtGui.QPushButton(self.tabJobs)
        self.openFolderButton.setObjectName("openFolderButton")
        self.horizontalLayout_6.addWidget(self.openFolderButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tabJobs, "")
        self.tabStat = QtGui.QWidget()
        self.tabStat.setObjectName("tabStat")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tabStat)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.statChart = MPL_Widget(self.tabStat)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statChart.sizePolicy().hasHeightForWidth())
        self.statChart.setSizePolicy(sizePolicy)
 #       self.statChart.setAlignment(QtCore.Qt.AlignCenter)
        self.statChart.setObjectName("statChart")
        self.horizontalLayout_3.addWidget(self.statChart)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.tableWidget = QtGui.QTableWidget(self.tabStat)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_6.addWidget(self.tableWidget)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tabStat, "")
        self.treeTab = QtGui.QWidget()
        self.treeTab.setObjectName("treeTab")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.treeTab)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.jobTreeView = QtGui.QTreeView(self.treeTab)
        self.jobTreeView.setObjectName("jobTreeView")
        self.horizontalLayout_7.addWidget(self.jobTreeView)
        self.groupBox = QtGui.QGroupBox(self.treeTab)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_7.addWidget(self.groupBox)
        self.tabWidget.addTab(self.treeTab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setBaseSize(QtCore.QSize(0, 10))
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 868, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuExtras = QtGui.QMenu(self.menuBar)
        self.menuExtras.setObjectName("menuExtras")
        self.menu_Help = QtGui.QMenu(self.menuBar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_Job = QtGui.QMenu(self.menuBar)
        self.menu_Job.setObjectName("menu_Job")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/filequit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/editzoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon3)
        self.actionAbout.setObjectName("actionAbout")
        self.actionNew_Job = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/filenew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Job.setIcon(icon4)
        self.actionNew_Job.setObjectName("actionNew_Job")
        self.menuExtras.addAction(self.actionExit)
        self.menuBar.addAction(self.menuExtras.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())
        self.menuBar.addAction(self.menu_Job.menuAction())
        self.label.setBuddy(self.inLineEdit)
        self.label_2.setBuddy(self.outLineEdit)
        self.label_4.setBuddy(self.jobSearchEdit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.inLineEdit, self.inComboBox)
        MainWindow.setTabOrder(self.inComboBox, self.outLineEdit)
        MainWindow.setTabOrder(self.outLineEdit, self.outComboBox)
        MainWindow.setTabOrder(self.outComboBox, self.noBreakCheckBox)
        MainWindow.setTabOrder(self.noBreakCheckBox, self.addDailyTimeButton)
        MainWindow.setTabOrder(self.addDailyTimeButton, self.buttonSave)
        MainWindow.setTabOrder(self.buttonSave, self.buttonNew)
        MainWindow.setTabOrder(self.buttonNew, self.buttonDelete)
        MainWindow.setTabOrder(self.buttonDelete, self.hourView)
        MainWindow.setTabOrder(self.hourView, self.calenderDay)
        MainWindow.setTabOrder(self.calenderDay, self.totLineEdit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Time Management", None, QtGui.QApplication.UnicodeUTF8))
        self.calenderDay.setToolTip(QtGui.QApplication.translate("MainWindow", "Click on a date to enter worked hours", None, QtGui.QApplication.UnicodeUTF8))
        self.calenderDay.setStatusTip(QtGui.QApplication.translate("MainWindow", "Click on a date to enter hours worked", None, QtGui.QApplication.UnicodeUTF8))
        self.dayChartLabel.setToolTip(QtGui.QApplication.translate("MainWindow", "Showing hours worked", None, QtGui.QApplication.UnicodeUTF8))
        self.dayChartLabel.setStatusTip(QtGui.QApplication.translate("MainWindow", "Showing graph of hours worked", None, QtGui.QApplication.UnicodeUTF8))
#        self.dayChartLabel.setText(QtGui.QApplication.translate("MainWindow", "No Image Shown", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Daily time", None, QtGui.QApplication.UnicodeUTF8))
        self.dailyTimeGP.setTitle(QtGui.QApplication.translate("MainWindow", "Daily Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Time In:", None, QtGui.QApplication.UnicodeUTF8))
        self.inLineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Enter time in in the format 12:30", None, QtGui.QApplication.UnicodeUTF8))
        self.inLineEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Enter In time in 12:30 format", None, QtGui.QApplication.UnicodeUTF8))
        self.inComboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "AM", None, QtGui.QApplication.UnicodeUTF8))
        self.inComboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "PM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Time Out:", None, QtGui.QApplication.UnicodeUTF8))
        self.outComboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "PM", None, QtGui.QApplication.UnicodeUTF8))
        self.outComboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "AM", None, QtGui.QApplication.UnicodeUTF8))
        self.outLineEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "Enter time in 12:30 format", None, QtGui.QApplication.UnicodeUTF8))
        self.outLineEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "Enter In time in 12:30 format", None, QtGui.QApplication.UnicodeUTF8))
        self.noBreakCheckBox.setStatusTip(QtGui.QApplication.translate("MainWindow", "Select if no lunch break", None, QtGui.QApplication.UnicodeUTF8))
        self.noBreakCheckBox.setText(QtGui.QApplication.translate("MainWindow", "No Lunch Break", None, QtGui.QApplication.UnicodeUTF8))
        self.leaveCheckBox.setText(QtGui.QApplication.translate("MainWindow", "Leave", None, QtGui.QApplication.UnicodeUTF8))
        self.leaveCombo.setItemText(0, QtGui.QApplication.translate("MainWindow", "Annual Leave", None, QtGui.QApplication.UnicodeUTF8))
        self.leaveCombo.setItemText(1, QtGui.QApplication.translate("MainWindow", "Sick Leave", None, QtGui.QApplication.UnicodeUTF8))
        self.leaveCombo.setItemText(2, QtGui.QApplication.translate("MainWindow", "Compensatory Leave", None, QtGui.QApplication.UnicodeUTF8))
        self.leaveCombo.setItemText(3, QtGui.QApplication.translate("MainWindow", "Loss of Pay", None, QtGui.QApplication.UnicodeUTF8))
        self.leaveCombo.setItemText(4, QtGui.QApplication.translate("MainWindow", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.totalHourdLabel.setText(QtGui.QApplication.translate("MainWindow", "Total Hours Worked", None, QtGui.QApplication.UnicodeUTF8))
        self.editButton.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.addDailyTimeButton.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Job Numbers", None, QtGui.QApplication.UnicodeUTF8))
        self.jobFilterCombo.setItemText(0, QtGui.QApplication.translate("MainWindow", "Current Jobs", None, QtGui.QApplication.UnicodeUTF8))
        self.jobFilterCombo.setItemText(1, QtGui.QApplication.translate("MainWindow", "Completed", None, QtGui.QApplication.UnicodeUTF8))
        self.jobFilterCombo.setItemText(2, QtGui.QApplication.translate("MainWindow", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTime), QtGui.QApplication.translate("MainWindow", "Ti&me Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Quick Search :", None, QtGui.QApplication.UnicodeUTF8))
        self.jobSearchEdit.setText(QtGui.QApplication.translate("MainWindow", "type here to search", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.allJobsButton.setText(QtGui.QApplication.translate("MainWindow", "All Jobs", None, QtGui.QApplication.UnicodeUTF8))
        self.currentJobsButton.setText(QtGui.QApplication.translate("MainWindow", "Current jobs", None, QtGui.QApplication.UnicodeUTF8))
        self.openFolderButton.setText(QtGui.QApplication.translate("MainWindow", "Open Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabJobs), QtGui.QApplication.translate("MainWindow", "J&obs", None, QtGui.QApplication.UnicodeUTF8))
#        self.statChart.setText(QtGui.QApplication.translate("MainWindow", "No Image Shown", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStat), QtGui.QApplication.translate("MainWindow", "S&tatistics", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.treeTab), QtGui.QApplication.translate("MainWindow", "Tree", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExtras.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Job.setTitle(QtGui.QApplication.translate("MainWindow", "Job", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Job.setText(QtGui.QApplication.translate("MainWindow", "New Job", None, QtGui.QApplication.UnicodeUTF8))

#from mpl_custom_widget import MPL_Widget
from mpl_pyqt4_widget import MPL_Widget
import resources_rc
