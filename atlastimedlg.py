#!/usr/bin/env python
# Copyright (c) 2007-8 Phoenix IT Solutions. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

import logging
FORMAT = '[%(levelname)-7s] [%(name)-35s] - %(message)s' 
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger('timemanagement')

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import sys
import os
import platform
import datetime
import time

from math import *
from string import *
import qrc_resources
#sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), ".", "ui"))
#sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), ".", "lib"))
#sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), ".", "images"))
import ui.ui_atlasTime
import ui.ui_atlasUserDlg
import ui.ui_mainWindow
from newJobDlg import   NewJobDlg
from progressDlg import   ProgressDlg
from settingsDlg import   SettingsDlg
from lib.database import KDatabase
import lib.treeoftable
#import lib.treeoftableView
#from pylab import *
#import numpy.numarray as na
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, NullFormatter
#from  matplotlib.pyplot  import *


ID, FNAME, LNAME, POSITION = range(4)
WORKID = 0
JOBNO = 1
PROCESSID = 2
DATE = 3
WDAY = 3
WMONTH = 4
WYEAR = 5 
EMPLID = 6
HOUR = 7
OVERTIME = 8
NOTES = 9
ACQUIRED = 1
WIDH = 20
WIDH1 = 80
EMPLOYEEID =""
__version__ = "1.0.0"
# Global variables
ProgramName = None    # QString
ProgramPath = None    # QString
UserName    = None    # QString
UserID = None
UserPath    = None    # QString
ProgParams  = {}      # Dictionary of QString

DB              = None    # KDatabase

Program = None   # QApplication
Splash  = None   # QLabel
MainWin = None   # QMainWindow

# Database access parameters
DBHost = None
DBPort = None
DBName = None
DBUser = None
DBPass = None
DBType = None

#others
monthChanged = False
dailyTimeDirty = False
currentMonth = None
currentDate = None
inTimeText = None
outTimeText = None
dataEntered = False
dataSaved = False
dailyTimeCalculated = False
timeCardInDatabase = False
jobDataSaved = False
firstRun = True
jobFilled = False
chartDrawn = False
customerComboChanged = False
statusComboChanged = False
debug = False

def initDatabase():
    if debug:
        logger.debug('initialising database')
    global DB, DBHost, DBPort, DBName, DBUser, DBPass, DBType
    DB=KDatabase.addDatabase(DBType)
    if DBHost == "":
        DBHost, status = QInputDialog.getText(\
            None,
            "Enter Database server address",
            "Server",
            QLineEdit.Normal)

    DB.setHostName(DBHost)
    if DBName == "":
        #QString name 
        DBName, status  =  QInputDialog.getText(\
            None,
            "Enter database name",
            "Database",
            QLineEdit.Normal)
        logger.debug(DBName)
    DB.setDatabaseName(DBName)
    if DBUser == "":
        DBUser, status = QInputDialog.getText(\
            None,
            "Enter database User",
            "User",
            QLineEdit.Normal)

    DB.setUserName(DBUser)
    if DBPass == "":
        DBPass, status = QInputDialog.getText(\
            None,
            "Enter password",
            "Password",
            QLineEdit.Normal)

    DB.setPassword(DBPass)
        

    if DB.open():
        writeConfigFile(0)
#        print "Successfully opened '%s' on '%s' for '%s'." % (DBName,DBHost,ProgramName)
        return 1
    else:
#        QMessageBox.critical(None,
#            self.trUtf8("Error opening Database"),
#            self.trUtf8("""Could not open database"""),
#            QMessageBox.StandardButtons(\
#                QMessageBox.Close))
    
        ErrorMsg = QString("Couldn't access<br>database <b>")
        ErrorMsg.append(DBName)
        ErrorMsg.append("</b><br>as <b>")
        ErrorMsg.append(DBUser)
        ErrorMsg.append("</b><br>on <b>")
        ErrorMsg.append(DBHost)
        ErrorMsg.append("</b><br>Using <b>")
        ErrorMsg.append(DBType)
        ErrorMsg.append("</b><br>with  <b>")
        ErrorMsg.append(QString("Database Error: %1").arg(DB.lastError().text()))
        ErrorMsg.append("</b>!")
        QMessageBox.critical(None , "Error " , ErrorMsg)
        sys.exit(1)
#                QMessageBox.warning(None, "Phone Log",
#                    QString("Database Error: %1").arg(db.lastError().text()))
#                
    
def initPathsAndNames():
    #global ProgramName,ProgramPath
    global UserName,UserPath
    #global Program
    if debug:
        logger.debug('initialising paths and names')
    # initalize program path
    ProgramName = QString(sys.argv[0])
    uPro =  sys.argv[0]
    if debug:
        print ProgramName
    ProgramName = ProgramName.right(ProgramName.length()-uPro.rfind("/") - 1)
    if debug:
        print ProgramName
    #ProgramName = "Time Management"
    ProgramName = ProgramName.left(uPro.rfind("."))
    print ProgramName
    ProgramPath = QString(os.path.dirname(os.path.abspath(sys.argv[0])))
    uPath  = os.path.dirname(os.path.abspath(sys.argv[0]))
    if debug:
        print ProgramPath
    ProgramPath = ProgramPath.left(uPath.rfind("/"))
    if debug:
        print ProgramPath
    # initialize user path
    UserPath = QString(os.path.expanduser("~"))
    uuPath = os.path.expanduser("~")
    UserName = UserPath.right(UserPath.length()-uuPath.rfind("/")-1)
    if debug:
        print UserName
    # initialize applicatiro
    Program = QApplication(sys.argv)

    for i in range(len(sys.argv)):
        if (i > 0):
            (key,value) = string.split(sys.argv[i], "=")
            ProgParams[key] = QString(value)

def readConfigFile(errorHandling):
    global ProgramName
    #global MainWin
    global UserPath,  UserID,  UserName
    global DBHost, DBPort, DBName, DBUser, DBPass, DBType
    #global AppBrowser, AppEmail, AppPDF
   # global LANG
    #global uiWinDim, uiTearOff, uiTextProgMenu, uiToolButtons, uiIconSet
    settings = QSettings()
    #print "in config"
    try:
        
        UserName = settings.value("UserName").toString()
        DBHost = settings.value("DBHost").toString()
        #DBHost = settings.value("DBHost", "61.9.143.196").toString()
        DBName = settings.value("DBName").toString()
        DBPort = settings.value("DBPort").toString()
        DBUser = settings.value("DBUser").toString()
        DBPass = settings.value("DBPass").toString()
        DBType = settings.value("DBType").toString()
        if debug:
            print "Printing from configuration %s, %s, %s, %s, %s, %s" % (DBHost, DBName,  DBPass,  DBPort,  DBType,  DBUser)
    except:
        # set default values (needed by Configurator)...
#        DBHost     = QString("")
#        DBName     = QString("")
        DBHost     = QString("61.9.143.196")
        #DBHost     = QString("192.168.0.23")
        DBName     = QString("")
        DBPort     = QString("3306")
        DBUser     = QString("")
        DBPass     = QString("")
        DBType     = QString("QMYSQL")
        # ...and do error handling (if needed)
        #print "Printing from default %s, %s, %s, %s, %s, %s" % (DBHost, DBName,  DBPass,  DBPort,  DBType,  DBUser)
        if (errorHandling != 0):
            QMessageBox.critical(None,
                self.trUtf8("Could not open Configuration"),
                self.trUtf8("""Could not open Configuration ,There seems to be an error"""),
                QMessageBox.StandardButtons(\
                    QMessageBox.Close),
                QMessageBox.Close)

def writeConfigFile(errorHandling):
    global ProgramName
    #global MainWin
    global UserPath,  UserID,  UserName
    global DBHost, DBPort, DBName, DBUser, DBPass, DBType
    #global AppBrowser, AppEmail, AppPDF
   # global LANG
    #global uiWinDim, uiTearOff, uiTextProgMenu, uiToolButtons, uiIconSet
    settings = QSettings()
    settings.setValue("DBHost", QVariant(DBHost))
    settings.setValue("DBPort", QVariant(DBPort))
    settings.setValue("DBName", QVariant(DBName))
    settings.setValue("DBUser", QVariant(DBUser))
    settings.setValue("DBPass", QVariant(DBPass))
    settings.setValue("DBType", QVariant(DBType))
    
class JobDelegate(QSqlRelationalDelegate):
    if debug:
        logger.debug('inside job delegate')
    def __init__(self, parent=None):
        super(JobDelegate, self).__init__(parent)


    def paint(self, painter, option, index):
        myoption = QStyleOptionViewItem(option)
        if index.column() == DATE:
            myoption.displayAlignment |= Qt.AlignRight|Qt.AlignVCenter
        if index.column() == JOBNO:
            myoption.displayAlignment |= Qt.AlignCenter|Qt.AlignVCenter
        if index.column() == HOUR:
            myoption.displayAlignment |= Qt.AlignRight|Qt.AlignVCenter
        QSqlRelationalDelegate.paint(self, painter, myoption, index)


    def createEditor(self, parent, option, index):
#        if index.column() ==WDAY:
#            editor = QLineEdit(parent)
#            editor.setText("9")
##            editor.setInputMask("9999")
##            editor.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
#            return editor
#        else:
            return QSqlRelationalDelegate.createEditor(self, parent,
                                                       option, index)

    def setEditorData(self, editor, index):
 #       if index.column() == PROCESSID:
#            text = index.model().data(index, Qt.DisplayRole).toString()
#            editor.setText(text)
#        else:
            QSqlRelationalDelegate.setEditorData(self, editor, index)


    def setModelData(self, editor, model, index):
#        if index.column() == WDAY:
#            tct= "9"
#            model.setData(index, QVariant(tct))
#        else:
            QSqlRelationalDelegate.setModelData(self, editor, model,
                                                index)

    

#def connectToMysql():
#        #print "Connecting to MySQL"
#        db = QSqlDatabase.addDatabase("QMYSQL")
#        db.setHostName("phoenixitsolutions.com.au");
#        db.setDatabaseName("timemanagement");
#        db.setUserName("anilet");
#        db.setPassword("02092089");
#        if not db.open():
#                QMessageBox.warning(None, "Phone Log",
#                    QString("Database Error: %1").arg(db.lastError().text()))
#                sys.exit(1)
    
class AtlasUserDlg(QDialog,
        ui.ui_atlasUserDlg.Ui_atlasUserDlg):

    def __init__(self, parent=None):
        super(AtlasUserDlg, self).__init__(parent)
        self.__index = 0
        self.setupUi(self)
        self.askPass = False
       # self.updateUi()
        self.setWindowTitle("Select Username - Atlas Tooling")
        self.okToContinue = True
        
        self.imageLabel.setPixmap(QPixmap.fromImage(QImage(":password.png")))
#        self.passLineEdit.setVisible(False)
#        self.passLabel.setVisible(False)
        query = QSqlQuery()
        query.exec_("SELECT `empl_First_Name`,`empl_Position`,`password` FROM `employee` "
                "WHERE `is_Active` = 1 ORDER by `empl_Id`")
        while query.next():
            name = QString(query.value(0).toString())
            self.userComboBox.addItem(name)
        #Load settings from file
        settings = QSettings()
        uname = settings.value("UserName").toString()
        self.userComboBox.setCurrentIndex(self.userComboBox.findText(uname))
        self.enablePass()
#
#    def updateUi(self):
#        enable = not self.findLineEdit.text().isEmpty()
#        self.findButton.setEnabled(enable)
#        self.replaceButton.setEnabled(enable)
#        self.replaceAllButton.setEnabled(enable)  
        self.connect( self.userComboBox, SIGNAL('currentIndexChanged(int)'), self.enablePass )
        
    def enablePass(self):
        if debug:
            logger.debug(self.userComboBox.currentText())
        if self.userComboBox.currentText() == "Anil":
            self.passLineEdit.setVisible(True)
            self.passLabel.setVisible(True)
            self.askPass = True
        else:
            self.passLineEdit.setVisible(False)
            self.passLabel.setVisible(False)
            self.askPass = False

    @pyqtSignature("")
    def on_okButton_clicked(self):
        global UserID
        global UserName
        if self.askPass:
            if debug:
                logger.debug("check password %s - %s " %(self.passLineEdit.text(), self.userComboBox.currentText()))
            query = QSqlQuery()
            query.exec_("SELECT `password` FROM `employee` "
                "WHERE `empl_First_Name` = '%s'" %self.userComboBox.currentText())
            if debug:
                print query.lastQuery()
            while query.next():
                if QString(query.value(0).toString()) == self.passLineEdit.text():
                    if debug:
                        logger.debug(" password ok")
                    QMessageBox.information(None,
                        self.trUtf8("Password OK"),
                        self.trUtf8("""Password OK"""),
                        QMessageBox.StandardButtons(\
                            QMessageBox.Ok))

        
        self.userName = unicode(self.userComboBox.currentText())
        UserName = unicode(self.userComboBox.currentText())
        settings = QSettings()
        settings.setValue("UserName", QVariant(self.userName))
        UserID = form.getUserID()
        #print  "calling from OK Button" + unicode(self.userComboBox.currentText())
        
        #self._statusBarLabel.setText(
        #form._statusBarLabel.setText(str(self.userName) + ', Please select a date from the Calendar below')
        # AtlasTimeDlg.userLabel.setText("Test")
        now = QDate.currentDate()
        MainWindow._setMonthFilter(form, now)
        MainWindow.uname = self.userName
        form._dateLabel.setText("Selected Date : %s-%s-%s." % (now.day(),  now.month(),  now.year()  ))
        form._userLabel.setText('Login as ' + str(self.userName))
        if debug:
            logger.debug("Setting date to today")
        form.currentDate = now
        #MainWindow.showDetails(form)
        form.show()

    
    def closeEvent(self, event):
        pass
        #self.uname = unicode(self.userComboBox.currentText())
        #settings = QSettings()
       # settings.setValue("UserName", QVariant(self.uname))
        #settings.setValue("RecentFiles", recentFiles)
        #AtlasTimeDlg. = AtlasUserDlg.userComboBox.currentText()
        #app.exec_()

class MainWindow(QMainWindow,
        ui.ui_mainWindow.Ui_MainWindow):
        
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        global currentMonth,  currentDate, debug
        global monthChanged
        if debug:
            logger.debug('initialising mainwindow')
        self.__index = 0
        self._isTimeViewInit = False
        self._isJobsViewInit = False
        self.setWindowFlags(Qt.Window |  Qt.WindowMinimizeButtonHint) 
        self.setupUi(self)
        now = datetime.datetime.now()
        date = self.calenderDay.selectedDate()
        currentDate = self.calenderDay.selectedDate()
       # self.updateUi()
        self.__statusBar = self.statusBar()
        self.__statusBar.setSizeGripEnabled(False)
        self.setWindowTitle("Time Management - Atlas Tooling")
        #status bar widgets
        self._userLabel = QLabel(self.__statusBar)
        self._dateLabel = QLabel(self.__statusBar)
        self._statusBarLabel = QLabel(self.__statusBar)
        self._messageLabel = QLabel(self.__statusBar)
    
        self.__statusBar.addPermanentWidget(self._dateLabel)
        self.__statusBar.addPermanentWidget(self._userLabel)
        #self.__statusBar.addWidget(self._statusBarLabel)
        self.__statusBar.addWidget(self._messageLabel)
        self.__statusBar.showMessage("Selected Date : %s-%s-%s." % (date.day(),  date.month(),  date.year()  ), 5000)
        #self._dateLabel.setText("Selected Date : %s-%s-%s." % (date.day(),  date.month(),  date.year()  ))
        #self._statusLayout = QHBoxLayout(self.__statusBar)
        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.calenderDay.setMaximumDate(now)
        settings = QSettings()
        self.uname = settings.value("UserName").toString()
        size = settings.value("MainWindow/Size",
                              QVariant(QSize(600, 500))).toSize()
        self.resize(size)
        position = settings.value("MainWindow/Position",
                                  QVariant(QPoint(0, 0))).toPoint()
        self.move(position)
        punctuationRe = QRegExp(r"^[0-9]{0,2}[:.,]{1,1}[0-5]{0,1}[0-9]{0,1}$")
 #       punctuationRe = QRegExp(r"[0-9][0-9][:.,][0-9][0-9]")
        outWordList = QStringList()
        inWordList = QStringList()
        inWordList << "00:00"<< "00:30"<< "1:00"<< "1:30" << "2:00" << "2:30" << "3:00" << "3:30" << "4:00" << "4:30" << "5:00" << "5:30" << "6:00" << "7:30" << "7:00" << "8:00" << "8:30" << "9:00" << "9:30" << "10:00" << "10:30" << "11:00" << "11:30" << "12:00" << "12:30" << "00.00"<< "00.30"<< "1.00"<< "1.30" << "2.00" << "2.30" << "3.00" << "3.30" << "4.00" << "4.30" << "5.00" << "5.30" << "6.00" << "7.30" << "7.00" << "8.00" << "8.30" << "9.00" << "9.30" << "10.00" << "10.30" << "11.00" << "11.30" << "12.00" << "12.30"
        outWordList << "00:00"<< "00:30"<< "1:00"<< "1:30" << "2:00" << "2:30" << "3:00" << "3:30" << "4:00" << "4:30" << "5:00" << "5:30" << "6:00" << "7:00" << "7:30" << "8:00" << "8:30" << "9:00" << "9:30" << "10:00" << "10:30" << "11:00" << "11:30" << "12:00" << "12:30"<< "00.00"<< "00.30"<< "1.00"<< "1.30" << "2.00" << "2.30" << "3.00" << "3.30" << "4.00" << "4.30" << "5.00" << "5.30" << "6.00" << "7.30" << "7.00" << "8.00" << "8.30" << "9.00" << "9.30" << "10.00" << "10.30" << "11.00" << "11.30" << "12.00" << "12.30"
        inCompleter = QCompleter(inWordList, self)
        completionMode = QCompleter.InlineCompletion
        inCompleter.setCompletionMode(completionMode)
        self.inLineEdit.setCompleter(
                inCompleter)
        outCompleter = QCompleter(outWordList, self)
        completionMode = QCompleter.InlineCompletion
        outCompleter.setCompletionMode(completionMode)
        self.outLineEdit.setCompleter(
                outCompleter)
        self.inLineEdit.setValidator(
                QRegExpValidator(punctuationRe, self))
        self.outLineEdit.setValidator(
                QRegExpValidator(punctuationRe, self))
        
        #Begin table 

        self.hourModel = QSqlRelationalTableModel(self)
        self.hourModel.setTable("work")
        self.hourModel.setRelation(JOBNO,
                QSqlRelation("activejobs", "job_No", "job_No"))
        self.hourModel.setRelation(PROCESSID,
                QSqlRelation("processes", "id", "description"))
        self.hourModel.setSort(WORKID, Qt.DescendingOrder)
        self.hourModel.setHeaderData(JOBNO, Qt.Horizontal,
                QVariant("Job No"))
        self.hourModel.setHeaderData(PROCESSID, Qt.Horizontal,
                QVariant("Process Description"))
        self.hourModel.setHeaderData(HOUR, Qt.Horizontal,
                QVariant("Time"))
        self.hourModel.setHeaderData(9, Qt.Horizontal,
                QVariant("Un-Attended"))
        self.hourModel.setFilter(QString("FK_empl_Id = %1").arg(str(UserID)))
        currentMonth = date.month()
        if debug:
            logger.debug("Current Month is %s " % currentMonth)
        #self._setMonthFilter(date)
        pydate = date.toPyDate()
        self.hourModel.setFilter("worked_Day = %s and worked_Month = %s and worked_Year = %s" % (pydate.day, pydate.month, pydate.year))
        self.hourModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.hourModel.select()
        self.hourView.setModel(self.hourModel)
        self.hourView.setItemDelegate(JobDelegate(self))
        self.hourView.setSelectionMode(QTableView.SingleSelection)
        self.hourView.setSelectionBehavior(QTableView.SelectRows)
        self.hourView.setColumnHidden(WORKID, True)
        self.hourView.setColumnHidden(WDAY, True)
        self.hourView.setColumnHidden(WMONTH, True)
        self.hourView.setColumnHidden(WYEAR, True)
        self.hourView.setColumnHidden(EMPLID, True)
        self.hourView.setColumnHidden(OVERTIME, True)
        self.hourView.setColumnWidth(HOUR, WIDH)
        self.hourView.resizeColumnsToContents()
        self.hourView.setColumnWidth(JOBNO, WIDH1)
        self.hourView.horizontalHeader().setStretchLastSection(True)
        #End table
        
        #self.connect(self.calenderDay, SIGNAL('selectionChanged()'), self.showDetails)
        self.connect(self.calenderDay, SIGNAL('selectionChanged()'), self.dateChanged)
        #self.connect(self.calenderDay, SIGNAL('selectionChanged()'), self.checkDailyTime)
        self.calenderDay.connect( self.calenderDay, SIGNAL( 'clicked(QDate)'), self._setMonthFilter )
        self.connect(self.addDailyTimeButton, SIGNAL('clicked()'), self.saveDailyTime)
        self.connect(self.inLineEdit,
                     SIGNAL('editingFinished()'), self.calculateDailyWorkedHours)
#        self.connect(self.inCompleter,
#                     SIGNAL('activated(QString)'), self.setDirty)
        self.connect(self.outLineEdit,
                     SIGNAL('editingFinished()'), self.calculateDailyWorkedHours)
        self.connect(self.noBreakCheckBox,
                     SIGNAL("stateChanged(int)"), self.calculateDailyWorkedHours)
        self.connect(self.buttonNew, SIGNAL("clicked()"), self.addWork)
        self.connect(self.buttonDelete, SIGNAL("clicked()"), self.deleteWork)
        self.connect(self.hourView, SIGNAL("clicked(QModelIndex)"), self.enableDeleteWork)
        #self.connect(self.buttonSave, SIGNAL("clicked()"), self.setDataModel)
        self.connect(self.buttonSave, SIGNAL("clicked()"), self.submit)
        
        self.connect( self.tabWidget, SIGNAL('selected(QString)'), self.tabChanged )
#        self.connect(self.hourView.selectionModel(),
#                SIGNAL("currentRowChanged(QModelIndex,QModelIndex)"),
#                self.EnbleSave)
        self.connect( self.hourView.selectionModel(), 
                     SIGNAL('dataChanged(QModelIndex,QModelIndex)'), 
                     self.EnbleSave )
        self.connect( self.customerComboBox, SIGNAL('currentIndexChanged(int)'), self.customerComboBoxCurrentIndexChanged )
        self.connect( self.customerComboBox, SIGNAL('activated(int)'), self.customerComboBoxActivated )
#        self.connect( self.statusComboBox, SIGNAL('currentIndexChanged(QString)'), self.jobsTabSetFilter )
#        #void QComboBox::currentIndexChanged ( const QString & text )
        self.dirty = True
        self._isTimeViewInit = True
        firstRun = False
        self.EnbleNew()
#        #fileSaveAction = self.createAction("&Save", self.fileSave,
#                QKeySequence.Save, "filesave", "Save the image")
#        #filePrintAction = self.createAction("&Print", self.filePrint,
#                QKeySequence.Print, "fileprint", "Print the image")
#        #fileQuitAction = self.createAction("&Quit", self.close,
#                "Ctrl+Q", "filequit", "Close the application")
        helpAboutAction = self.createAction("&About Time Manager",
                self.helpAbout)
        helpHelpAction = self.createAction("&Help", self.helpHelp,
                QKeySequence.HelpContents)
        jobAction = self.createAction("&Job", self.createJob)
        settingsAction = self.createAction("&Settings",  self.openSettings)
    
        #self.jobMenu = self.menuBar().addMenu("&Job")
        #self.fileMenuActions = (fileQuitAction)
        #self.connect(self.fileMenu, SIGNAL("aboutToShow()"),
 #                    self.updateFileMenu)
    
        #helpMenu = self.menuBar().addMenu("&Help")
        self.addActions(self.menu_Help, (helpAboutAction, helpHelpAction))
        self.addActions(self.menu_Job, (jobAction, ))
        self.addActions(self.menuSettings, (settingsAction, ))
        




    def createAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action


    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    @pyqtSignature("")
    def on_editButton_clicked(self):
        self.updateUi(True)
        
    @pyqtSignature("")
    def on_deleteTimeButton_clicked(self):
        self.deleteDailyTime()
        
    @pyqtSignature("")
    def on_allJobsButton_clicked(self):
        stat = ""
        self.customerComboBox.setCurrentIndex(self.customerComboBox.findText("All Customers"))
        self.statusComboBox.setCurrentIndex(self.statusComboBox.findText("All Jobs"))
        self.jobsTabSetFilter(stat)
    
    @pyqtSignature("")
    def on_currentJobsButton_clicked(self):
        stat = "P"
        self.customerComboBox.setCurrentIndex(self.customerComboBox.findText("All Customers"))
        self.statusComboBox.setCurrentIndex(self.statusComboBox.findText("Current Jobs"))
        self.jobsTabSetFilter(stat)
        

    def customerComboBoxCurrentIndexChanged(self):
        global customerComboChanged
        if customerComboChanged:
            if debug:
                logger.debug("Calling filter on customer")
            stat = "O"
            self.jobsTabSetFilter(stat)
    
#statusComboChanged = False
#    @pyqtSignature("")
#    def on_currentJobsButton_clicked(self):
#        stat = "P"
#        self.jobsTabSetFilter(stat)
#        

    def customerComboBoxActivated(self):
        if debug:
            logger.debug("Custome combobox changed")
        global customerComboChanged
        customerComboChanged = True

#self.connect( self.customerComboBox, SIGNAL('currentIndexChanged(QString)'), self.jobsTabSetFilter )
    def setDirty(self):
        global inTimeText, outTimeText
        global dailyTimeDirty
        if not (self.inLineEdit.text() == inTimeText or self.outLineEdit.text() == outTimeText):
            dailyTimeDirty = True
            if debug:
                logger.debug("Text changed")
        else:
            dailyTimeDirty = False
            if debug:
                logger.debug("Text not changed")
    
    def helpAbout(self):
        QMessageBox.about(self, "Time Management",
                """<b>Time Manager</b> v %s
                <p>Copyright &copy; 2007 Phoenix IT Solutions. 
                All rights reserved.
                <p>Manage time entry.
                <p>Python %s - Qt %s - PyQt %s on %s""" % (
                __version__, platform.python_version(),
                QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))


    def helpHelp(self):
#        form = helpform.HelpForm("index.html", self)
#        form.show()
        pass
    
    def createJob(self):
        jobForm = NewJobDlg(self)
        jobForm.show()
        #pass
    def openSettings(self):
        settingsForm = SettingsDlg(self)
        settingsForm.show()
    
    def dateChanged(self):
        global UserID
        global monthChanged
        global currentMonth,  currentDate
        global dailyTimeDirty
        if debug:
            logger.debug('date changed UserID is %s' %UserID)
        self. setDirty()
        if dailyTimeDirty:
            reply = QMessageBox.question(self,
                "Atlas Time Manager - Unsaved Changes",
                "Save unsaved changes?",
                QMessageBox.Yes|QMessageBox.No|
                QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                pass
            elif reply == QMessageBox.Yes:
                self.saveDailyTime()
        if debug:
            logger.debug('Filtering with ID')
        self.hourModel.setFilter(QString("FK_empl_Id = %1").arg(UserID))
        #self.hourModel.setFilter("FK_empl_Id = %s" %UserID)
        date = self.calenderDay.selectedDate()
        currentDate = date
        form._dateLabel.setText("Selected Date : %s-%s-%s." % (date.day(),  date.month(),  date.year()  ))
        pydate = date.toPyDate() 
        newMonth = date.month()
        if debug:
            print "New month is %s " % newMonth
        if not currentMonth is  newMonth:
            monthChanged = True
            currentMonth = newMonth
            if debug:
                print "Month changed"
        else:
            monthChanged = False
            if debug:
                print "Month not changed"
        #self.hourModel.setFilter("worked_Day = %s and worked_Month = %s and worked_Year = %s" % (pydate.day, pydate.month, pydate.year))
        self.checkDailyTime()
    
    def saveDailyTime(self):
        if debug:
            logger.debug('saving daily time ')
        global currentDate,  timeCardInDatabase, chartDrawn, DB
        global inTimeText ,  outTimeText , dailyTimeCalculated 
        if not DB.isOpen():
                DB.open()
        query = QSqlQuery()
        timeIn = self.inLineEdit.text()
        timeOut = self.outLineEdit.text()
        date = currentDate
        if debug:
            logger.debug('Current date is %s' % date)
        pydate = date.toPyDate()   
        dt_D  =  str(pydate.day)
        dt_M = str(pydate.month)
        dt_Y = str(pydate.year )
        if   self.noBreakCheckBox.isChecked() :
            lBreak = "0"
        else:
            lBreak = "1"
        entered ="0"
        totTime = self.totLineEdit.text()
        if not dailyTimeCalculated:
            self.calculateDailyWorkedHours()
        if not timeCardInDatabase:
            if debug:
                logger.debug("Inserting to timecard")
            query.prepare("INSERT INTO timecard (FK_empl_Id,time_In,time_Out,worked_Day,worked_Month,worked_Year,isDataEntered,lunchBreak,totHours) "
                      "VALUES (:id, :in, :out, :dt_D, :dt_M, :dt_Y, :dtEntered, :lBreak, :totHour)")
            query.bindValue(":id", QVariant(self.getUserID()))
            query.bindValue(":in", QVariant(timeIn))
            query.bindValue(":out", QVariant(timeOut))
            query.bindValue(":dt_D", QVariant(dt_D))
            query.bindValue(":dt_M", QVariant(dt_M))
            query.bindValue(":dt_Y", QVariant(dt_Y))
            query.bindValue(":dtEntered", QVariant(entered))
            query.bindValue(":lBreak", QVariant(lBreak))
            query.bindValue(":totHour", QVariant(totTime))
        else:
            if debug:
                logger.debug("Updating timecard")
            query.prepare("UPDATE timecard SET time_In = :in ,time_Out = :out,lunchBreak = :lBreak, totHours = :totHour "
                      " WHERE worked_Day = :dt_D and worked_Month = :dt_M and worked_Year = :dt_Y and FK_empl_Id = :id")
            query.bindValue(":in", QVariant(timeIn))
            query.bindValue(":out", QVariant(timeOut))
            query.bindValue(":dt_D", QVariant(dt_D))
            query.bindValue(":dt_M", QVariant(dt_M))
            query.bindValue(":dt_Y", QVariant(dt_Y))
            query.bindValue(":lBreak", QVariant(lBreak))
            query.bindValue(":totHour", QVariant(totTime))
            query.bindValue(":id", QVariant(self.getUserID()))
        query.exec_()
        if debug:
            print query.lastQuery()
#        query.exec_("insert into timecard(FK_empl_Id,time_In,time_Out,worked_Date,isDataEntered) "
#            "values  ('%s' ,%s,%s, '%s-%s-%s',0)" % (self.getUserID(),timeIn, timeOut,  pydate.year, pydate.month, pydate.day) )
        if not query.isActive():
            QMessageBox.warning(self, "Daily time sheet -- Database Error",
                    "Failed to open database %s" % (query.lastError().text()))
        else:
            #if not progressForm:
            app.setOverrideCursor(QCursor(Qt.WaitCursor))
            progressForm = ProgressDlg(self)
            progressForm.lblMessage.setText("Saving data......")
            progressForm.show()
            chartDrawn = False
            self.monthGraphDataForMatplot()
            app.restoreOverrideCursor()
#            QMessageBox.information(self, "Daily time sheet -- Data entered", "In and out time entered for %s-%s-%s. <br> Please enter the job details now" % (pydate.day,  pydate.month,  pydate.year  ))
            timeCardInDatabase = True
        inTimeText = self.inLineEdit.text()
        outTimeText = self.outLineEdit.text()
        self._setMonthFilter( date, 1)
        self.updateUi()
    
    def deleteDailyTime(self):
        if debug:
            logger.debug('Deleting daily time ')
        global currentDate,  timeCardInDatabase, chartDrawn, DB
        if not DB.isOpen():
                DB.open()
        query = QSqlQuery()
        date = currentDate
        pydate = date.toPyDate()   
        dt_D  =  str(pydate.day)
        dt_M = str(pydate.month)
        dt_Y = str(pydate.year )
        if  timeCardInDatabase:
            res = QMessageBox.question(None,
                self.trUtf8("Do you want to delete the details"),
                self.trUtf8("""Do you want to delete the details for  %s""" %date),
                QMessageBox.StandardButtons(\
                    QMessageBox.Cancel | \
                    QMessageBox.No | \
                    QMessageBox.Yes),
                QMessageBox.No)
            if res == QMessageBox.Yes:
                query.prepare("DELETE from timecard where FK_empl_Id=:id and worked_Day=:dt_D and worked_Month=:dt_M and worked_Year=:dt_Y ")
                query.bindValue(":id", QVariant(self.getUserID()))
                query.bindValue(":dt_D", QVariant(dt_D))
                query.bindValue(":dt_M", QVariant(dt_M))
                query.bindValue(":dt_Y", QVariant(dt_Y))
                query.exec_()
        if debug:
            print query.lastQuery()
#        query.exec_("insert into timecard(FK_empl_Id,time_In,time_Out,worked_Date,isDataEntered) "
#            "values  ('%s' ,%s,%s, '%s-%s-%s',0)" % (self.getUserID(),timeIn, timeOut,  pydate.year, pydate.month, pydate.day) )
        if not query.isActive():
            QMessageBox.warning(self, "Daily time sheet -- Database Error",
                    "Failed to open database %s" % (query.lastError().text()))
        else:
            #if not progressForm:
            app.setOverrideCursor(QCursor(Qt.WaitCursor))
            progressForm = ProgressDlg(self)
            progressForm.lblMessage.setText("Deleting data......")
            progressForm.show()
            chartDrawn = False
            self.monthGraphDataForMatplot()
            app.restoreOverrideCursor()
            timeCardInDatabase = False
        inTimeText = self.inLineEdit.text()
        outTimeText = self.outLineEdit.text()
        self._setMonthFilter( date, 1)
        self.updateUi()

    def updateUi(self, enable = False):
        global timeCardInDatabase,  jobDataSaved
        if jobDataSaved:
            self.buttonSave.setEnabled(False)
        else:
            self.buttonSave.setEnabled(True)
        if timeCardInDatabase:
            if not(self.inLineEdit.text().isEmpty() or \
                          self.outLineEdit.text().isEmpty()):
                self.addDailyTimeButton.setEnabled(False)
                self.editButton.setEnabled(True)
                self.deleteTimeButton.setEnabled(True)
                self.inLineEdit.setEnabled(False)
                self.inComboBox.setEnabled(False)
                self.outLineEdit.setEnabled(False)
                self.outComboBox.setEnabled(False)
                self.noBreakCheckBox.setEnabled(False)
                self.buttonNew.setEnabled(True)
                self.buttonDelete.setEnabled(False)
            else:
                #self.addDailyTimeButton.setEnabled(True)
                self.editButton.setEnabled(False)
                self.deleteTimeButton.setEnabled(False)
                self.inLineEdit.setEnabled(True)
                self.inComboBox.setEnabled(True)
                self.outLineEdit.setEnabled(True)
                self.outComboBox.setEnabled(True)
                #self.noBreakCheckBox.setEnabled(True)
                self.buttonNew.setEnabled(True)
                self.totalHourdLabel.setText("Enter Time in and Time out")
                self.buttonDelete.setEnabled(False)
                #self._messageLabel.setText("Please enter Time in and Time out")
        else:
            if not(self.inLineEdit.text().isEmpty() and \
                           self.outLineEdit.text().isEmpty()):
                self.addDailyTimeButton.setEnabled(True)
            
            self.editButton.setEnabled(False)
            self.deleteTimeButton.setEnabled(False)
            self.inLineEdit.setEnabled(True)
            self.inComboBox.setEnabled(True)
            self.outLineEdit.setEnabled(True)
            self.outComboBox.setEnabled(True)
            #self.noBreakCheckBox.setEnabled(True)
            self.buttonNew.setEnabled(True)
            self.totalHourdLabel.setText("Enter Time in and Time out")
            #self.__statusBar.showMessage("Enter Time in and Time out", 5000)
            self._messageLabel.setText("Please enter Time in and Time out")
            self.buttonDelete.setEnabled(False)
        if enable:
            self.addDailyTimeButton.setEnabled(True)
            self.editButton.setEnabled(False)
            self.deleteTimeButton.setEnabled(False)
            self.inLineEdit.setEnabled(True)
            self.inComboBox.setEnabled(True)
            self.outLineEdit.setEnabled(True)
            self.outComboBox.setEnabled(True)
            self.noBreakCheckBox.setEnabled(True)
    
    def showImage(self, percent=None):
            #factor = percent / 100.0
            width = self.image.width()
            height = self.image.height()
            image = self.image.scaled(width, height, Qt.KeepAspectRatio)
            self.headLabel.setPixmap(QPixmap.fromImage(image))
    
    def showDetails(self):
        #self.calenderDay.selectedDate = today()
        date = self.calenderDay.selectedDate()
        #self.dateLabel.setText(str(date.toString()))
        pydate = date.toPyDate()   
       # self.userID = self.getUserID()
        #print "Printing from Show Details and User ID = %s" % self.userID
        # day        

    def reformatCalendarPage(self, date):
        if debug:
            logger.debug('reformatting calendar')
        mayFirstFormat = QTextCharFormat() 
        #color = QColor(255, 0, 0, 127) #red
        color = QColor(184, 255, 197, 255)
        #mayFirstFormat.setForeground(Qt.red)
        mayFirstFormat.setBackground(color) 
        #date = QDate(2008, 10, 20)
        self.calenderDay.setDateTextFormat(date,mayFirstFormat )
        #QDate date(calendar->yearShown(), calendar->monthShown(), 1);
        #calendar->setDateTextFormat(QDate(date.year(), 5, 1), mayFirstFormat);
        #date.setDate(date.year(), date.month(), 1)
        #calendar->setDateTextFormat(date, firstFridayFormat)
        
    def getUserID(self):
        #print "Printing from getUserID and user is %s" %user
        if debug:
            logger.debug('initialising user ID id' )
        settings = QSettings()
        user = settings.value("UserName").toString()
        query = QSqlQuery()
        query.exec_("SELECT empl_Id FROM employee "
                "where empl_First_Name = '%s'" % user)
        while query.next():
            ID = ""
            ID = QString(query.value(0).toString())
            #print ID
            if debug:
                logger.debug('user ID is %s'%ID )
            return ID
    
    def checkDailyTime(self):
        if debug:
            logger.debug('checking daily time ')
        global UserID, DB
        global timeCardInDatabase, jobDataSaved
        global inTimeText ,  outTimeText
        date = self.calenderDay.selectedDate()
        #for checking 
        self.inLineEdit.setText("")
        self.outLineEdit.setText("")
        self.totLineEdit.setText("")
        self.noBreakCheckBox.setChecked(False)
        self.leaveCheckBox.setChecked(False)
        #self.leaveCheckBox.setEnabled(False)
        timeCardInDatabase = False
        dailyTimeCalculated = False
        jobDataSaved = False
        query = QSqlQuery()
        if not DB.isOpen():
            DB.open()
        query.exec_("select time_In,time_Out,isDataEntered,lunchBreak from timecard  where FK_empl_Id = '%s' and worked_Day = %s and worked_Month = %s and worked_Year = %s"  % (UserID, date.day(), date.month(), date.year()))
        
        while query.next():
            self.inLineEdit.setText(QString(query.value(0).toString()))
            self.outLineEdit.setText(QString(query.value(1).toString()))
            timeCardInDatabase = True
            jobDataSaved = True
            if query.value(3).toString() == "0":
                self.noBreakCheckBox.setChecked(True)
            self.calculateDailyWorkedHours()
            #        else:
        self.updateUi()
        inTimeText = self.inLineEdit.text()
        outTimeText = self.outLineEdit.text()

    def validate(self):
        if debug:
            logger.debug('validating date ')
        it = unicode(self.inLineEdit.text())
        ot = unicode(self.outLineEdit.text())
        #startSplit = split(inTime,":")
        #endSplit = split(outTime,":")
        s ="."
        t = ","
        try:
            if len(it) == 0:
                raise InEmptyError,  ("You must enter In Time.")
            else:
                if s in it:
                    it.replace(".", ":")
                elif t in it:
                    it.replace(",", ":")
            if debug:
                print "In time %s" %it
        except InEmptyError,  e:
            QMessageBox.warning(self,  "In Time Error",  unicode(e))
            self.inLineEdit.selectAll()
            self.inLineEdit.setFocus()
            return
    def calculateDailyWorkedHours(self):
        if debug:
            logger.debug('calculating hours ')
        global dailyTimeCalculated
        dailyTimeCalculated = False
        inTime = unicode(self.inLineEdit.text())
        outTime = unicode(self.outLineEdit.text())
        self.addDailyTimeButton.setEnabled(False)
        self.noBreakCheckBox.setEnabled(False)
       # self.updateUi()
#        try:
#            inc = time.strptime(inTime,"%H%M")
#            outc = time.strptime(outTime,"%H%M")
#        #splits time input into usable chunks
            
        if not len(inTime) == 0 and not len(outTime) == 0 :
#            try:
            if ((":" in inTime)  or  ("." in inTime )or ("," in inTime)):
                if debug:
                    logger.debug('intime does  have delimiters')
                inTime = inTime.replace(",", ":")
                inTime = inTime.replace(".", ":")
                if debug:
                    logger.debug('intime is %s' %inTime)
#            elif "." in inTime:
#                startSplit = split(inTime,".")
#            elif "," in inTime:
#                startSplit = split(inTime,",")
            else:
                if debug:
                    logger.debug('intime does not have delimiters')
                inTime = ":".join((inTime, "00"))
                if debug:
                    logger.debug('intime does not have delimiters %s' %inTime)
            if ((":" in outTime)  or  ("." in outTime )or ("," in outTime)):
                outTime = outTime.replace(",", ":")
                outTime = outTime.replace(".", ":")
                if debug:
                    logger.debug('outtime is %s' %outTime)
            else:
                outTime = ":".join((outTime, "00"))
            if debug:
                logger.debug('intime is %s and outTime is %s' %(inTime ,  outTime)   )
            if inTime.endswith(":"):
                inTime = "".join((inTime, "00"))
            if outTime.endswith(":"):
                outTime = "".join((outTime, "00"))
            self.inLineEdit.setText(inTime)
            self.outLineEdit.setText(outTime)
            startSplit = split(inTime,":")
            endSplit = split(outTime,":")
#            endSplit = split(outTime,":")
            #converts strings to usable integers
            sh = int(startSplit[0])
            sm = int(startSplit[1])
            eh = int(endSplit[0])
            em = int(endSplit[1])
            #in time format
            st = unicode(self.inComboBox.currentText())
            et = unicode(self.outComboBox.currentText())
            #sh, sm, st = 12, 30, 'pm'
           # eh, em, et = 6, 0, 'pm'
            # First, adjust "hour reported" to real "hour of day"
            if sh < 12 and st.lower() == 'pm': sh += 12
            if sh == 12 and st.lower() == 'am': sh = 0  # Early morning
            if eh < 12 and et.lower() == 'pm': eh += 12
            if eh == 12 and et.lower() == 'am': eh = 0  # Early morning
            # Calculate minute-of-day
            smin = sh * 60 + sm
            emin = eh * 60 + em
            # Delta time in  minutes
            dmin = emin - smin
            if dmin < 0: dmin += 1440  # Wrapped around midnight?
            if  not self.noBreakCheckBox.isChecked() :
                dmin -= 30
            # Delta time in hours
            dtime = dmin / 60.
            #print dtime # 5.5 hours from minutes 780->1050 (12:30-18:00).
            date = self.calenderDay.selectedDate()
            self.totalHourdLabel.setText("You worked <b> %.2f hours</b> on  %s-%s-%s " % (dtime, date.day(),date.month(), date.year()))
            self.totLineEdit.setText(str(dtime))
            self.addDailyTimeButton.setEnabled(True)
            self.noBreakCheckBox.setEnabled(True)
            dailyTimeCalculated = True
    
    def tabChanged(self, name):
        if debug:
            print name
        global jobFilled 
        DB = KDatabase()
        if name=="tabTime":
            if not self._isTimeViewInit:
                self._dayModel = QtSql.QSqlTableModel(self);
            self._dayModel.setTable("perhour");
            self._dayModel.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit);
            self._dayModel.select();
            self._dayModel.removeColumns(0,3)
            self.tableViewDay.setModel(self._dayModel)
            self.tableViewDay.verticalHeader().hide()
            self._isDayViewInit == True
            self._setDateFilter( self.calenderDay.selectedDate() )
            self._messageLabel.setText("Showing Worked hours details")
            self.calenderDay.connect( self.calenderDay, QtCore.SIGNAL( 'clicked(QDate)'), self._setDateFilter )
        if name=="J&obs":
            if not DB.isOpen():
                DB.open()
            if not jobFilled:
                if debug:
                    logger.debug("job tab was not activated before")
                customers = DB.doSelect("customer", ("cust_Name", ))
                while customers.next():
                    if not (customers.value(0).toString() == "Atlas Special"):
                        self.customerComboBox.addItem(customers.value(0).toString())
                self.customerComboBox.addItem("All Customers")
                self.customerComboBox.setCurrentIndex(self.customerComboBox.findText("All Customers"))
                stat = DB.doSelect("jobstatus", ("Description", ))
                while stat.next():
                    self.statusComboBox.addItem(stat.value(0).toString())
                self.statusComboBox.addItem("Current Jobs")
                self.statusComboBox.addItem("All Jobs")
                self.statusComboBox.setCurrentIndex(self.statusComboBox.findText("Current Jobs"))
    #            aItem = KListViewItemWithID(self.lvAddresses, quAddresses.value(0).toString())
    #            aItem.setText(0, quAddresses.value(1).toString())
                #if not self._isJobsViewInit:
                self._messageLabel.setText("Showing current jobs details")
                self._jobModel = QSqlRelationalTableModel();
                self._jobModel.setTable("jobs1");
                self._jobModel.setRelation(2,
                    QSqlRelation("jobstatus", "ID", "Description"))
                self._jobModel.setRelation(6,
                    QSqlRelation("customer", "cust_Id", "cust_Name"))
                self._jobModel.setEditStrategy(QSqlTableModel.OnManualSubmit);
                self._jobModel.setSort(0, Qt.AscendingOrder)
                #setup header
                self._jobModel.setHeaderData(0, Qt.Horizontal,
                    QVariant("Job No"))
                self._jobModel.setHeaderData(1, Qt.Horizontal,
                    QVariant("Status"))
                self._jobModel.setHeaderData(2, Qt.Horizontal,
                    QVariant("Status"))
                self._jobModel.setHeaderData(6, Qt.Horizontal,
                    QVariant("Customer"))
                self._jobModel.setHeaderData(4, Qt.Horizontal,
                    QVariant("Description"))
                self._jobModel.setHeaderData(7, Qt.Horizontal,
                    QVariant("Cust Order No"))
                self._jobModel.setHeaderData(8, Qt.Horizontal,
                    QVariant("Start Date"))
                self._jobModel.setHeaderData(9, Qt.Horizontal,
                    QVariant("Due Date"))
                self._jobModel.setHeaderData(13, Qt.Horizontal,
                    QVariant("Toolmaker"))
    #            self._jobModel.setHeaderData(12, Qt.Horizontal,
    #                QVariant("Remarks"))
    #            self._jobModel.setHeaderData(13, Qt.Horizontal,
    #                QVariant("Invoice No"))
                self._jobModel.select();
                
                #self._jobModel.removeColumns(0,2)
                self.tableViewJob.setModel(self._jobModel)
                self.tableViewJob.verticalHeader().hide()
                self.tableViewJob.setAlternatingRowColors(True)
                self.tableViewJob.setSelectionMode(QTableView.SingleSelection)
                #self.tableViewJob.editTriggers(QAbstractItemView.NoEditTriggers)
                self.tableViewJob.setSelectionBehavior(QTableView.SelectRows)
                st = "P"
                if debug:
                    logger.debug("Status = %s" %st)
                self._jobModel.setFilter("stat='%s'" %(st))
                #self._jobModel.setFilter("cust_Name='Bosch' AND Description = 'Completed'" )
    #            currentMonth = date.month()
    #            print "Current Month is %s " % currentMonth
    #            pydate = date.toPyDate()
    #            self._jobModel.setFilter("worked_Day = %s and worked_Month = %s and worked_Year = %s" % (pydate.day, pydate.month, pydate.year))
    #            self.tableViewJob.setColumnHidden(WORKID, True)
    #            self.tableViewJob.setColumnHidden(WDAY, True)
    #            self.tableViewJob.setColumnHidden(WMONTH, True)
    #            self.tableViewJob.setColumnHidden(WYEAR, True)
    #            self.tableViewJob.setColumnHidden(EMPLID, True)
    #            self.tableViewJob.setColumnHidden(OVERTIME, True)
                #self.tableViewJob.setColumnWidth(HOUR, WIDH)
                self.tableViewJob.setColumnHidden(1, True)
                self.tableViewJob.setColumnHidden(3, True)
                self.tableViewJob.setColumnHidden(5, True)
                self.tableViewJob.setColumnHidden(11, True)
                self.tableViewJob.setColumnHidden(10, True)
                self.tableViewJob.setColumnHidden(12, True)
                #self.tableViewJob.setColumnHidden(13, True)
                self.tableViewJob.setColumnHidden(14, True)
                self.tableViewJob.setColumnHidden(15, True)
                self.tableViewJob.setColumnHidden(16, True)
                self.tableViewJob.setColumnHidden(17, True)
                self.tableViewJob.setColumnHidden(18, True)
                self.tableViewJob.setColumnHidden(19, True)
                self.tableViewJob.resizeColumnsToContents()
                #self.tableViewJob.setColumnWidth(JOBNO, WIDH1)
                self.tableViewJob.horizontalHeader().setStretchLastSection(True)
                jobFilled = True
                
        if name=="S&tatistics":
            import calendar
            global UserID, chartDrawn,  monthChanged
            if (not chartDrawn) or monthChanged:
                if debug:
                    logger.debug("Drawing chart")
                self.statChart.canvas.figure.clf()
                self.statChart.canvas.axis = self.statChart.canvas.figure.add_subplot(111)
                self.statChart.canvas.axis.set_xlabel('Date')   
                self.statChart.canvas.axis.set_ylabel('Hours')   
                self.statChart.canvas.axis.set_title('Hours Graph')   
                self.statChart.canvas.axis.grid(True)  
                date = self.calenderDay.selectedDate()
            #for checking 
                month  = date.month()
                year = date.year()
                dates = []
                dates1 = []
                hoursWorked = []
                hoursEntered = []
                val  = 0
                maxdt  = calendar.mdays[month]
        #        print maxdt
                maxdt = maxdt + 1
                query = QSqlQuery()
                query1 = QSqlQuery()
                for t in range(1, maxdt):
                    dates.append(t)
                    dates1.append(t+.5)
                    query.exec_("SELECT totHours FROM timecard WHERE worked_Month=%s AND worked_Year=%s and  worked_Day=%s and FK_empl_Id =%s " % (month, year, t, UserID))
                    query1.exec_("select sum(`work`.`worked_Hours`) AS `hours` from work WHERE worked_Month=%s AND worked_Year=%s and  worked_Day=%s and FK_empl_Id =%s " % (month, year, t, UserID))
        
                        #print "Query successful  %s" %t
                    if query.isActive():
                        query.first()
                        if query.first():
                            date = QDate(year, month, t)
                            #self.reformatCalendarPage(date)
                            hoursWorked.append( query.value(0).toDouble()[0] )
                            #hoursEntered.append( query.value(0).toDouble()[0] )
                            #data.append(10)
                            #print "Printing from if with value %s " %data
                        else:
                            if t == (maxdt-1):
                                hoursWorked.append(.01)
                                #hoursEntered.append(.01)
                            else:
                                hoursWorked.append(val)
                                #hoursEntered.append(val)
                    if query1.isActive():
                        query1.first()
                        if query1.first():
                            date = QDate(year, month, t)
                            #self.reformatCalendarPage(date)
                            #hoursWorked.append( query1.value(0).toDouble()[0] )
                            hoursEntered.append( query1.value(0).toDouble()[0] )
                            #data.append(10)
                            #print "Printing from if with value %s " %data
                        else:
                            if t == (maxdt-1):
                                #hoursWorked.append(.01)
                                hoursEntered.append(.01)
                            else:
                                #hoursWorked.append(val)
                                hoursEntered.append(val)
#                print "Dates %s" %dates
#                print "hoursWorked %s" %hoursWorked
#                print "hoursEntered %s" %hoursEntered
                width = 0.45 # the width of the bars
                #self.statChart.canvas.clear()
                p1 = self.statChart.canvas.axis.bar(dates, hoursWorked, width=width, color = 'y') 
                p2 = self.statChart.canvas.axis.bar(dates1, hoursEntered, width, color='r') 
                self.statChart.canvas.axis.legend( (p1[0], p2[0]),  ('Worked Hours', 'Data Entered') )
                #self.statChart.canvas.axis.plot(x, y, 'o')
                
                self.statChart.canvas.draw()
            chartDrawn = True
    def jobsTabSetFilter(self, filter):
        if debug:
            logger.debug("Filter is %s" %filter)
        customer = self.customerComboBox.currentText()
        stat = self.statusComboBox.currentText()
        if stat == "All Jobs":
             filter = ""   
        elif stat == "Current Jobs":
            filter = "P"
        if filter == "":
            self._jobModel.setFilter("")
        
        elif filter == "P":
            self._jobModel.setFilter("stat='%s'" %(filter))
        elif filter == "O":
            self._jobModel.setFilter("cust_Name='%s' AND Description = '%s'" %(customer, stat))
    
    def okToContinue(self):
        if self.dirty:
            pass
#            reply = QMessageBox.question(self,
#                            "Atlas Time Manager - Unsaved Changes",
#                            "Save unsaved changes?",
#                            QMessageBox.Yes|QMessageBox.No|
#                            QMessageBox.Cancel)
#            if reply == QMessageBox.Cancel:
#                return False
#            elif reply == QMessageBox.Yes:
#                #self.fileSave()
#                pass/time
        return True   
    
    def closeEvent(self, event):
        writeConfigFile()
    
    def addWork(self):
        if debug:
            logger.debug('adding new row to work ')
        global jobDataSaved
        jobnoFilter = ""
#        global currentMonth, UserID, currentDate
#        day = currentDate.day()
#        month = currentDate.month()
#        year = currentDate.year()
#        #self._dayModel.setFilter("day = %s AND month = %s and year = %s and FK_empl_Id = %s" % (day,month,year,  UserID))
#        stat = self.jobFilterCombo.currentText()
#        #stat = self.statusComboBox.currentText()
#        filter = "" 
#        if stat == "All Jobs":
#             filter = ""   
#        elif stat == "Current Jobs":
#            filter = "P"
#        elif stat ==    "Completed":
#            filter = "P"
#        if filter == "":
#            self.hourModel.setFilter("day = %s AND month = %s and year = %s and FK_empl_Id = %s and stat='%s'" % (day,month,year,  UserID, filter))
#            #self.hourModel.setFilter("")
#        elif filter == "P":
        #self.hourModel.setFilter("stat='P'")
##        elif filter == "O":
##            self.hourModel.setFilter("cust_Name='%s' AND Description = '%s'" %(customer, stat))
            
        self.buttonSave.setEnabled(True)
        jobnoFilter = unicode(self.jobFilterCombo.currentText())
        #row = self.hourModel.rowCount()
        #self.hourModel.insertRow(row)
        row = self.hourView.currentIndex().row() \
            if self.hourView.currentIndex().isValid() else self.hourModel.rowCount()
        date = self.calenderDay.selectedDate()
#        row = self.hourModel.rowCount()
#            
#        QSqlDatabase.database().transaction()
        self.hourModel.insertRow(row)
        index = self.hourModel.index(row, WDAY)
        data =  date.day()
        self.hourModel.setData(index,QVariant(data) ,(Qt.EditRole))
        index = self.hourModel.index(row, WMONTH)
        data =  date.month()
        self.hourModel.setData(index,QVariant(data) ,(Qt.EditRole))
        index = self.hourModel.index(row, WYEAR)
        data =  date.year()
        self.hourModel.setData(index,QVariant(data) ,(Qt.EditRole))
        index = self.hourModel.index(row, EMPLID)
        data =  UserID
        self.hourModel.setData(index,QVariant(data) ,(Qt.EditRole))
        
#        index = self.hourModel.index(row, 2)
#        data =  "Bench"
#        self.hourModel.setData(index,QVariant(data) ,(Qt.EditRole))
        
        index = self.hourModel.index(row, JOBNO)
        self.hourView.setCurrentIndex(index)
#        if index.column() == WDAY:
#            date = self.calenderDay.selectedDate()
#            data =  date.day()
#            if (self.hourModel.setData(index ,Qvariant(data) , Qt.DisplayRole)):
#                print "Error setData %s" % (hourModel.lastError()).text()
#        assetid = 1
#        #query = QSqlQuery()
#        query.exec_("SELECT MAX(id) FROM assets")
#        if query.next():
#            assetid = query.value(0).toInt()[0]
#        query.prepare("INSERT INTO work (FK_job_No,FK_process_ID,worked_Day,worked_Month,worked_Year,FK_empl_Id ) "
#                      "VALUES (:assetid, :date, :actionid)")
#        query.bindValue(":assetid", QVariant(assetid + 1))
#        query.bindValue(":date", QVariant(QDate.currentDate()))
#        query.bindValue(":actionid", QVariant(ACQUIRED))
#        query.exec_()
#        QSqlDatabase.database().commit()
        jobDataSaved = False
        self.hourView.edit(index)

    def addRecord(self):
        row = self.hourModel.rowCount()
        self.hourModel.insertRow(row)
        index = self.hourModel.index(row, JOBNO)
        self.hourView.setCurrentIndex(index)
        self.hourView.edit(index)
        
    def setDataModel(self):
        index = self.hourView.currentIndex()
        if debug:
            print "Index %s" % index
     
    def EnbleSave(self):
        if debug:
            logger.debug('Enablng save button ')
        self.buttonSave.setEnabled(True)
    
    def EnbleNew(self):
        if debug:
            logger.debug('Enablng new button ')
        self.buttonNew.setEnabled(True)
        
    def printDoc(self):
        #active = self.activeMdiChild()
        self.printer.printView( self)
    
    def submit(self):
        global jobDataSaved , chartDrawn
        if debug:
            logger.debug('saving new row ')
        row = self.hourView.currentIndex().row() #\
       #    if self.hourView.currentIndex().isValid() else 0
       # date = self.calenderDay.selectedDate()
#        row = self.hourModel.rowCount()
#            
#        QSqlDatabase.database().transaction()
      #  self.hourModel.insertRow(row)
        index = self.hourModel.index(row, JOBNO)
      #  data =  date.day()
        if  (self.hourModel.data(index,(Qt.EditRole)) == "" ):
            if debug:
                print "You need to enter data"
    #        index = self.hourModel.index(row, WMONTH)
    #        data =  date.month()
    #        self.hourModel.setData(index,QVariant(data) ,(Qt.EditRole))
    #        index = self.hourModel.index(row, WYEAR)
    #        data =  date.year()
    #        self.hourModel.setData(index,QVariant(data) ,(Qt.EditRole))
    #        index = self.hourModel.index(row, EMPLID)
    #        data =  UserID
    #        self.hourModel.setData(index,QVariant(data) ,(Qt.EditRole))
    #        index = self.hourModel.index(row, JOBNO)
    #        self.hourView.setCurrentIndex(index)
           # self.setModelData(editor, hourModel, WDAY)
        if self.hourModel.submitAll():
            jobDataSaved = True
            #if not progressForm:
            app.setOverrideCursor(QCursor(Qt.WaitCursor))
            progressForm = ProgressDlg(self)
            progressForm.lblMessage.setText("Saving data......")
            progressForm.show()
            chartDrawn = False
            self.monthGraphDataForMatplot()
            app.restoreOverrideCursor()
#            QMessageBox.information(None,
#                self.trUtf8("Success"),
#                self.trUtf8("""Successfully entered data"""),
#                QMessageBox.StandardButtons(\
#                    QMessageBox.Ok))
        else:
            jobDataSaved = False
            if debug:
                print "Error setData %s" % (self.hourModel.lastError()).text()
            QMessageBox.warning(None,
                self.trUtf8("Failed"),
                self.trUtf8("Failed to enter  data with error %s"% (self.hourModel.lastError()).text()),
                QMessageBox.StandardButtons(\
                    QMessageBox.Ok))

    def enableDeleteWork(self):
        index = self.hourView.currentIndex()
        if  index.isValid():
            self.buttonDelete.setEnabled(True)
        else:
            self.buttonDelete.setEnabled(False)
    
    def deleteWork(self):
        index = self.hourView.currentIndex()
        if not index.isValid():
            return
        QSqlDatabase.database().transaction()
        record = self.hourModel.record(index.row())
        hourid = record.value(ID).toInt()[0]
        logrecords = 1
        msg = QString("<font color=red>Delete</font>"
                      "<br> record from database") 
        msg += "?"
        if QMessageBox.question(self, "Delete Data", msg,
                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
            QSqlDatabase.database().rollback()
            return
        self.hourModel.removeRow(index.row())
        self.hourModel.submitAll()
        QSqlDatabase.database().commit()
    
    def closeEvent(self, event):
        if debug:
            logger.debug('Closing')
        if self.okToContinue():
            if debug:
                logger.debug('Saving settings')
            #self.uname = unicode(self.userLabel.text())
            settings = QSettings()
            #settings.setValue("UserName", QVariant(self.uname))
            #settings.setValue("RecentFiles", recentFiles)
            settings.setValue("MainWindow/Size", QVariant(self.size()))
            settings.setValue("GraphWidth", QVariant(self.dayChartLabel.size().width()))
            settings.setValue("GraphHeight", QVariant(self.dayChartLabel.size().height()))
            settings.setValue("MainWindow/Position",
                    QVariant(self.pos()))
            #settings.setValue("MainWindow/State",
             #       QVariant(self.saveState()))
        else:
            event.ignore()
    
    def _setDateFilter(self, date):
        if debug:
            logger.debug('setting date filter')
        global currentMonth, UserID
        day = date.day()
        month = date.month()
        year = date.year()
        self._dayModel.setFilter("day = %s AND month = %s and year = %s and FK_empl_Id = %s" % (day,month,year,  UserID))
        data,axis = self._db.dayGraphData(date)
        self._updateGraph( data, axis, self.dayChartLabel )

    def _setMonthFilter(self,date, updated = 0):
        if debug:
            logger.debug('setting month filter')
        global monthChanged, UserID
        global firstRun
        pydate = date.toPyDate()
        #self.hourModel.setFilter(QString("worked_Date = = %1").arg(dt))
        month = date.month()
        #year = date.year()
        self.hourModel.setFilter("worked_Day = %s and worked_Month = %s and worked_Year = %s and FK_empl_Id = %s" % (pydate.day, pydate.month, pydate.year,  UserID))
        #self._monthModel.setFilter("month = %s and year = %s" % (month,year))
        if monthChanged:
            #print "Calling graph"
            #data,axis = self.monthGraphData(date)
            #print data
            #print axis
            #self._updateGraph( data, axis, self.dayChartLabel )
            self.monthGraphDataForMatplot()
        if firstRun:
            if debug:
                print "First run"
            #data,axis = self.monthGraphData(date)
            #print data
            #print axis
            #self._updateGraph( data, axis, self.dayChartLabel )
            self.monthGraphDataForMatplot()
            firstRun = False
        if updated == 1:
            if debug:
                print "Updating"
            #data,axis = self.monthGraphData(date)
            #print data
            #print axis
            #self._updateGraph( data, axis, self.dayChartLabel )
            self.monthGraphDataForMatplot()
	

    def _updateGraph(self, data, axis, labelWidget ):
        if debug:
            logger.debug('updating graph')
        global firstRun
        if firstRun:
            if debug:
                logger.debug('Width at firstrun')
            settings = QSettings()
            width = settings.value("GraphWidth", QVariant(500)).toInt()
            height = settings.value("GraphHeight", QVariant(268)).toInt()
            if debug:
                print width, height
            if width =="" or height == "":
                if debug:
                    logger.debug('width is empty')
                width =labelWidget.size().width()
                height = labelWidget.size().height()
        else:
            width =labelWidget.size().width()
            height = labelWidget.size().height()
        width = min(width,600)
        height = min(height, 268)
        if debug:
            print width, height
        #print "Printing width %i" %width
        mxData = 15
        chart = StackedVerticalBarChart(width, height, y_range=(0,mxData))
        #chart = StackedVerticalBarChart(width, labelWidget.size().height(), y_range=(0,int(max(data)*1.1)))
        chart.set_bar_width( ((width-50)/len(data))-3 )
    #chart.set_colours(['00ff00', '00ff00'])
        chart.add_data(data)
        #chart.fill_linear_gradient(Chart.CHART,90,90,'00ff00','00ff00')
        #chart.set_axis_range(Axis.LEFT,0,int(max(data)*1.1))
        chart.set_axis_range(Axis.LEFT,0,15)
        chart.set_axis_labels(Axis.BOTTOM, axis)
        if sys.platform == "win32":
            img = "C:\gasmon_chart.png"
        else:
            img = "/tmp/gasmon_chart.png"
        try:
            img = "chart.png"
            chart.download(img)
            self._googleUrl = chart.get_url() 
            pixmap = QPixmap( img )
            labelWidget.setPixmap(pixmap)
            #labelWidget.setPixmap(pixmap)
            #labelWidget.setPixmap(QPixmap.fromImage(QImage(":chart.png")))
        except:
            #labelWidget.setPixmap()
            labelWidget.setPixmap(QPixmap.fromImage(QImage(":chart.png")))
    
    def dayGraphData(self, date):
        if debug:
            logger.debug('updating day graph data')
        year = date.year()
        month = date.month()
        day = date.day()
        query = QSqlQuery()
        query.exec_("SELECT hour,duration FROM perhour WHERE year=%s AND day=%s AND month=%s" % (year,day,month))
        data = []
        axis = []
        while  query.next():
            axis.append( query.value(0).toInt()[0] )
            data.append( query.value(1).toInt()[0] )
        return data,axis

#    def monthGraphData(self, date):
#        year = date.year()
#        month = date.month()
#        day = date.day()
#        query = QSqlQuery()
#        query.exec_("SELECT worked_Day,totHours FROM timecard WHERE worked_Month=%s AND worked_Year=%s and FK_empl_Id =%s order by worked_Day" % (month, year, self.getUserID()))
#        data = []
#        axis = []
#        val  = 0
#        for i in range(32):
#            axis.append(i)
#        t = 1
#        found = False
#        for t in range(1, 32):
#            print t
#            found = False
#            while query.next() and found == False:
#                query.seek(t-1)
#                if  (query.value(0).toInt()[0] == t):
#                    data.append( query.value(1).toDouble()[0] )
#                    found = True
#                else:
#                    data.append(val)
#                    found = False
#                    break
#            else:
#                data.append(val)
##                if found:
##                    break
#              
##            for i in range(32):
##                axis.append(i)
##                print  (query.value(0).toInt()[0])
##                data.append( query.value(1).toDouble()[0] )
#                
##            axis.append( query.value(0).toInt()[0] )
##            data.append( query.value(1).toDouble()[0] )
#        return data,axis
        
    def monthGraphData(self, date):
            import calendar
            if debug:
                logger.debug('monthgraph data ')
            global UserID
            year = date.year()
            month = date.month()
            day = date.day()
            maxdt  = calendar.mdays[month]
            if debug:
                print maxdt
            maxdt = maxdt + 1
            query = QSqlQuery()
            data = []
            axis = []
            val  = 0
            for t in range(1, maxdt):
                query.exec_("SELECT totHours FROM timecard WHERE worked_Month=%s AND worked_Year=%s and  worked_Day=%s and FK_empl_Id =%s " % (month, year, t, UserID))
                #print "Query successful  %s" %t
                if query.isActive():
                    query.first()
                    if query.first():
                        date = QDate(year, month, t)
                        self.reformatCalendarPage(date)
                        data.append( query.value(0).toDouble()[0] )
                        #print "Printing from if with value %s " %data
                    else:
                        data.append(val)
                        #print "Calling with 0 value"
                axis.append(t)
            return data,axis
    
    def monthGraphDataForMatplot(self):
            import calendar
            global UserID, chartDrawn,  monthChanged
            if (not chartDrawn) or monthChanged:
                if debug:
                    logger.debug("Drawing chart")
                self.dayChartLabel.canvas.figure.clf()
                self.dayChartLabel.canvas.axis = self.dayChartLabel.canvas.figure.add_subplot(111)
                self.dayChartLabel.canvas.figure.subplots_adjust(left=0.06, bottom=0.15, right=0.95, top=0.90)
                self.dayChartLabel.canvas.axis.set_xlabel('Date')   
                self.dayChartLabel.canvas.axis.set_ylabel('Hours')   
                self.dayChartLabel.canvas.axis.set_title('Hours Graph')   
                self.dayChartLabel.canvas.axis.grid(True)  
                xmin, xmax = 1, 31
                ymin, ymax = 0, 14
                self.dayChartLabel.canvas.axis.axis([1, 31, 0, 15])
                majorFormatter = NullFormatter()
                minorLocatorX = MultipleLocator(1)
                minorLocatorY = MultipleLocator(1)
                minorFormattor = FormatStrFormatter('%d')
                self.dayChartLabel.canvas.axis.yaxis.set_minor_locator(minorLocatorY)
                self.dayChartLabel.canvas.axis.xaxis.set_minor_locator(minorLocatorX)
                self.dayChartLabel.canvas.axis.yaxis.set_minor_formatter(minorFormattor) 
                self.dayChartLabel.canvas.axis.xaxis.set_major_formatter(majorFormatter) 
                self.dayChartLabel.canvas.axis.yaxis.set_major_formatter(majorFormatter) 
                self.dayChartLabel.canvas.axis.xaxis.set_minor_formatter(minorFormattor) 
                self.dayChartLabel.canvas.axis.xaxis.grid(True, which='minor')
                #self.dayChartLabel.canvas.axis.axis([1, 31, 0, 15])
                date = self.calenderDay.selectedDate()
            #for checking 
                month  = date.month()
                year = date.year()
                dates = []
                dates1 = []
                hoursWorked = []
                hoursEntered = []
                val  = 0
                maxdt  = calendar.mdays[month]
        #        print maxdt
                maxdt = maxdt + 1
                query = QSqlQuery()
                query1 = QSqlQuery()
                for t in range(1, maxdt):
                    dates.append(t)
                    dates1.append(t+.5)
                    query.exec_("SELECT totHours FROM timecard WHERE worked_Month=%s AND worked_Year=%s and  worked_Day=%s and FK_empl_Id =%s " % (month, year, t, UserID))
                    query1.exec_("select sum(`work`.`worked_Hours`) AS `hours` from work WHERE worked_Month=%s AND worked_Year=%s and  worked_Day=%s and FK_empl_Id =%s " % (month, year, t, UserID))
        
                        #print "Query successful  %s" %t
                    if query.isActive():
                        query.first()
                        if query.first():
                            date = QDate(year, month, t)
                            self.reformatCalendarPage(date)
                            hoursWorked.append( query.value(0).toDouble()[0] )
                            #hoursEntered.append( query.value(0).toDouble()[0] )
                            #data.append(10)
                            #print "Printing from if with value %s " %data
                        else:
                            if t == (maxdt-1):
                                hoursWorked.append(.01)
                                #hoursEntered.append(.01)
                            else:
                                hoursWorked.append(val)
                                #hoursEntered.append(val)
                    if query1.isActive():
                        query1.first()
                        if query1.first():
                            date = QDate(year, month, t)
                            #self.reformatCalendarPage(date)
                            #hoursWorked.append( query1.value(0).toDouble()[0] )
                            hoursEntered.append( query1.value(0).toDouble()[0] )
                            #data.append(10)
                            #print "Printing from if with value %s " %data
                        else:
                            if t == (maxdt-1):
                                #hoursWorked.append(.01)
                                hoursEntered.append(.01)
                            else:
                                #hoursWorked.append(val)
                                hoursEntered.append(val)
#                print "Dates %s" %dates
#                print "hoursWorked %s" %hoursWorked
#                print "hoursEntered %s" %hoursEntered
                width = 0.45 # the width of the bars
                #self.dayChartLabel.canvas.clear()
 #               labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "31"]
 #               xlocations = na.array(range(len(dates)))+0.5
                #bar(xlocations, data, yerr=error, width=width)
#                mpl.yticks(range(0, 8))
                #self.dayChartLabel.canvas.figure.xticks(xlocations+ width/2)
 #               xlim(1, xlocations[-1]+width*2)
 #               gca().get_xaxis().tick_bottom()
 #               gca().get_yaxis().tick_left()
                p1 = self.dayChartLabel.canvas.axis.bar(dates, hoursWorked, width=width, color = 'y') 
#                p2 = self.dayChartLabel.canvas.axis.bar(dates1, hoursEntered, width, color='r') 
 #               p1 = self.dayChartLabel.canvas.axis.bar(xlocations, hoursWorked, width=width, color = 'y') 
                p2 = self.dayChartLabel.canvas.axis.bar(dates1, hoursEntered, width, color='r') 
                self.dayChartLabel.canvas.axis.legend( (p1[0], p2[0]),  ('Worked Hours', 'Data Entered') )
                #self.dayChartLabel.canvas.axis.plot(x, y, 'o')
                
                self.dayChartLabel.canvas.draw()
            chartDrawn = True
    
if __name__ == "__main__":
    import sys
    if debug:
            logger.debug('qt version %s, pyqt version %s' % (QT_VERSION_STR, 
                                                   PYQT_VERSION_STR))
    app = QApplication(sys.argv)
    app.setOrganizationName("Phoenix IT Solutions.")
    app.setOrganizationDomain("phoenixitsolutions.com.au")
    app.setApplicationName("Time Management")
    app.setWindowIcon(QIcon(":/editzoom.png"))
    readConfigFile(0)
    initDatabase()
    form = MainWindow()
    userForm = AtlasUserDlg()
    userForm.show()
    form.checkDailyTime()
    app.exec_()
    #print form.text()

