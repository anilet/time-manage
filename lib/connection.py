#!/usr/bin/env python
# Copyright (c) 2007-8 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtSql import *

def connectToMysql():
        print "Connecting to MySQL"
        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("phoenixitsolutions.com.au");
        db.setDatabaseName("management");
        db.setUserName("anilet");
        db.setPassword("02092089");
        if not db.open():
                QMessageBox.warning(None, "Phone Log",
                    QString("Database Error: %1").arg(db.lastError().text()))
                sys.exit(1)

def createFakeData():
    #import random

    print "Dropping table..."
    query = QSqlQuery()
    #query.exec_("DROP TABLE calls")
    #QApplication.processEvents()

    #print "Creating table..."
    #query.exec_("""CREATE TABLE calls (
    #            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    #            employee VARCHAR(40) NOT NULL,
    #            starttime DATETIME NOT NULL,
    #            endtime DATETIME NOT NULL,
    #            topic VARCHAR(80) NOT NULL)""")
    #topics = ("Complaint", "Information request", "Off topic",
    #          "Information supplied", "Complaint", "Complaint")
    #now = QDateTime.currentDateTime()
    #print "Populating table..."
    #query.prepare("INSERT INTO calls (employee, starttime, endtime, "
    #              "topic) VALUES (?, ?, ?, ?)")
    #for name in ('Joshan Cockerall', 'Ammanie Ingham',
    #        'Diarmuid Bettington', 'Juliana Bannister',
    #        'Oakley-Jay Buxton', 'Reilley Collinge',
    #        'Ellis-James Mcgehee', 'Jazmin Lawton',
    #        'Lily-Grace Smythe', 'Coskun Lant', 'Lauran Lanham',
    #        'Millar Poindexter', 'Naqeeb Neild', 'Maxlee Stoddart',
    #        'Rebia Luscombe', 'Briana Christine', 'Charli Pease',
    #        'Deena Mais', 'Havia Huffman', 'Ethan Davie',
    #        'Thomas-Jack Silver', 'Harpret Bray', 'Leigh-Ann Goodliff',
    #        'Seoras Bayes', 'Jenna Underhill', 'Veena Helps',
    #        'Mahad Mcintosh', 'Allie Hazlehurst', 'Aoife Warrington',
    #        'Cameron Burton', 'Yildirim Ahlberg', 'Alissa Clayton',
    #        'Josephine Weber', 'Fiore Govan', 'Howard Ragsdale',
    #        'Tiernan Larkins', 'Seren Sweeny', 'Arisha Keys',
    #        'Kiki Wearing', 'Kyran Ponsonby', 'Diannon Pepper',
    #        'Mari Foston', 'Sunil Manson', 'Donald Wykes',
    #        'Rosie Higham', 'Karmin Raines', 'Tayyibah Leathem',
    #        'Kara-jay Knoll', 'Shail Dalgleish', 'Jaimie Sells'):
    #    start = now.addDays(-random.randint(1, 30))
    #    start = now.addSecs(-random.randint(60 * 5, 60 * 60 * 2))
    #    end = start.addSecs(random.randint(20, 60 * 13))
    #    topic = random.choice(topics)
    #    query.addBindValue(QVariant(QString(name)))
    #    query.addBindValue(QVariant(start))
    #    query.addBindValue(QVariant(end))
    #    query.addBindValue(QVariant(QString(topic)))
    #    query.exec_()
    #QApplication.processEvents()

    print "Calls:"
    query.exec_("SELECT * FROM employee "
                "ORDER by empl_Id")
    while query.next():
        id = query.value(0).toInt()[0]
        employee = unicode(query.value(1).toString())
        #starttime = unicode(query.value(2).toDateTime().toString(
        #                    DATETIME_FORMAT))
        #endtime = unicode(query.value(3).toDateTime().toString(
        #                  DATETIME_FORMAT))
        #topic = unicode(query.value(4).toString())
        print "%d: %s" % (id, employee)
    QApplication.processEvents()


