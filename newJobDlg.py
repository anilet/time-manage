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
logger = logging.getLogger('NewJobDlg')

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import ui.ui_newjobDlg

class NewJobDlg(QDialog,
        ui.ui_newjobDlg.Ui_newjobDlg):

    def __init__(self, parent=None):
        super(NewJobDlg, self).__init__(parent)
        self.__index = 0
        logger.debug('Setting up NewJobDlg')
        self.setupUi(self)
        logger.debug('Setting up NewJobDlg completed')
        self.setWindowTitle("New Job - Atlas Tooling")
        #model
        self.model = QSqlRelationalTableModel(self)
        self.model.setTable("jobs1")
        self.model.setRelation(5,
                QSqlRelation("jobtype", "jobTypeId", "Description"))
        self.model.setRelation(2,
                QSqlRelation("jobstatus", "ID", "Description"))
        self.model.setRelation(13,
                QSqlRelation("employee", "empl_Id", "empl_First_Name"))
        self.model.setRelation(6,
                QSqlRelation("customer", "cust_Id", "cust_Name"))
        self.model.setSort(0, Qt.AscendingOrder)
        self.model.select()
        logger.debug('setting up model')

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
        self.mapper.addMapping(self.jobNoEdit, 0)
        self.mapper.addMapping(self.quoteNoEdit, 15)
        self.mapper.addMapping(self.jobDescriptionEdit, 4)
        #self.mapper.addMapping(topicEdit, TOPIC)
        relationModel = self.model.relationModel(5)
        self.jobTypeComboBox.setModel(relationModel)
        self.jobTypeComboBox.setModelColumn(
                relationModel.fieldIndex("Description"))
        self.mapper.addMapping(self.jobTypeComboBox, 5)
        
        relationModel1 = self.model.relationModel(2)
        self.jobStatusComboBox.setModel(relationModel1)
        self.jobStatusComboBox.setModelColumn(
                relationModel.fieldIndex("Description"))
        self.mapper.addMapping(self.jobStatusComboBox, 2)
        
        relationModel2 = self.model.relationModel(13)
        self.inchargeComboBox.setModel(relationModel2)
        self.inchargeComboBox.setModelColumn(
                relationModel.fieldIndex("Description"))
        self.mapper.addMapping(self.inchargeComboBox, 13)
        
        relationModel3 = self.model.relationModel(6)
        self.customerComboBox.setModel(relationModel3)
        self.customerComboBox.setModelColumn(
                relationModel.fieldIndex("Description"))
        self.mapper.addMapping(self.customerComboBox, 6)
        
        self.mapper.toFirst()
       # self.mapper.setCurrentIndex(1)
        self.addRecord()
#        self.connect( self.userComboBox, SIGNAL('currentIndexChanged(int)'), self.enablePass )
        
    def addRecord(self):
        row = self.model.rowCount()
        self.mapper.submit()
        self.model.insertRow(row)
        self.mapper.setCurrentIndex(row)
        now = QDateTime.currentDateTime()
        self.startDate.setDateTime(now)
        self.dueDate.setDateTime(now)
        self.jobTypeComboBox.setCurrentIndex(
                self.jobTypeComboBox.findText("Select Job Type"))
        self.jobStatusComboBox.setCurrentIndex(
                self.jobStatusComboBox.findText("Select Status"))
        self.inchargeComboBox.setCurrentIndex(
                self.inchargeComboBox.findText("Select"))
        self.customerComboBox.setCurrentIndex(
                self.customerComboBox.findText("Select customer"))
                
        self.jobNoEdit.setFocus()
    
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

    
    def closeEvent(self, event):
        pass
        #self.uname = unicode(self.userComboBox.currentText())
        #settings = QSettings()
       # settings.setValue("UserName", QVariant(self.uname))
        #settings.setValue("RecentFiles", recentFiles)
        #AtlasTimeDlg. = AtlasUserDlg.userComboBox.currentText()
        #app.exec_()
