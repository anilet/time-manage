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
logger = logging.getLogger('Settings')

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import ui.ui_settingsDlg
DBHostSettings = None 
DBPortSettings = None 
DBNameSettings = None 
DBUserSettings = None 
DBPassSettings = None
DBTypeSettings = None
updated = False

class SettingsDlg(QDialog,
        ui.ui_settingsDlg.Ui_settingsDlg):

    def __init__(self, parent=None):
        super(SettingsDlg, self).__init__(parent)
        self.__index = 0
        #logger.debug('Showing Progress')
        self.setupUi(self)
        
        #Load settings from file
#        settings = QSettings()
#        uname = settings.value("UserName").toString()
#        self.userComboBox.setCurrentIndex(self.userComboBox.findText(uname))
#        self.enablePass()
##
##    def updateUi(self):
##        enable = not self.findLineEdit.text().isEmpty()
##        self.findButton.setEnabled(enable)
##        self.replaceButton.setEnabled(enable)
##        self.replaceAllButton.setEnabled(enable)  
#        self.connect( self.userComboBox, SIGNAL('currentIndexChanged(int)'), self.enablePass )
        
    def writeConfigFile():
        global DBHostSettings, DBPortSettings, DBNameSettings, DBUserSettings, DBPassSettings, DBTypeSettings
        settings = QSettings()
        settings.setValue("DBHost", QVariant(DBHost))
        settings.setValue("DBPort", QVariant(DBPort))
        settings.setValue("DBName", QVariant(DBName))
        settings.setValue("DBUser", QVariant(DBUser))
        settings.setValue("DBPass", QVariant(DBPass))
        settings.setValue("DBType", QVariant(DBType))

    @pyqtSignature("")
    def on_okButton_clicked(self):
        global UserID
        global UserName
        if self.askPass:
            logger.debug("check password %s - %s " %(self.passLineEdit.text(), self.userComboBox.currentText()))
            query = QSqlQuery()
            query.exec_("SELECT `password` FROM `employee` "
                "WHERE `empl_First_Name` = '%s'" %self.userComboBox.currentText())
            print query.lastQuery()
            while query.next():
                if QString(query.value(0).toString()) == self.passLineEdit.text():
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
        logger.debug("Setting date to today")
        form.currentDate = now
        #MainWindow.showDetails(form)
        form.show()

    
    def closeMe(self):
        global updated
        if not updated:
            self.lblMessage.setText("Data Saved")
            updated = True
        else:
            self.close()
            
#    def hideMe(self):
#        global updated
#        if not updated:
#            self.lblMessage.setText("Data Saved")
#            updated = True
#        else:
#            self.hide()
#        
        #self.uname = unicode(self.userComboBox.currentText())
        #settings = QSettings()
       # settings.setValue("UserName", QVariant(self.uname))
        #settings.setValue("RecentFiles", recentFiles)
        #AtlasTimeDlg. = AtlasUserDlg.userComboBox.currentText()
        #app.exec_()
