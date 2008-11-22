# ============================================================
# Database.py
# sql layer for all queries, handles special chars etc.
# ------------------------------------------------------------
# Copyright (C) 2004 the Kumula Team.
# Licensed under the LGPL.
# ============================================================

import os
import sys
from PyQt4.QtCore import *
#from PyQt4.QtGui import *
from PyQt4.QtSql import *

# ------------------------------------------------------------


class KDatabase(QSqlDatabase):


    def getTableName(self, aTableName):
        myTableName = QString(aTableName)
        return myTableName


    def prepareFieldName(self, str):
       # myValue = QString("`")
        myValue = QString("")
        myValue.append(str)
       # myValue.append("`")
        return myValue


    def prepareValue(self, str):
        myStr = QString(str)
        myStr.replace("\\", "\\\\")
        myStr.replace("'", "\\'")
        myStr.replace("`", "\\`")
        myValue = QString("'")
        myValue.append(myStr)
        myValue.append("'")
        return myValue



    def formatMultipleFields(self, strTuple):
        myString = QString("")
        for str in strTuple:
            myString.append(self.prepareFieldName(str))
            myString.append(",")
        return myString.left(myString.length()-1)



    def formatMultipleValues(self, strTuple):
        myString = QString("")
        for str in strTuple:
            myString.append(self.prepareValue(str))
            myString.append(",")
        return myString.left(myString.length()-1)



    def doSelect(self, table, fields, ord = "", where = {}, limit = 0):
        # 'fields' has to be a Python tuple
        # 'where' has to be a Python dictionary
        # 'limit' has to be an integer
        query = QSqlQuery()
        myStatement = QString("SELECT ")
        myStatement.append(self.formatMultipleFields(fields))
        myStatement.append(" FROM ")
        myStatement.append(self.prepareFieldName(self.getTableName(table)))

        whereCounter = 0
        for key,value in where.iteritems():
            if (whereCounter == 0):
                myStatement.append(" WHERE ")
            else:
                myStatement.append(" AND ")
            whereCounter = whereCounter + 1
            myStatement.append(self.prepareFieldName(key))
            myStatement.append("=")
            myStatement.append(self.prepareValue(value))

        if (ord != ""):
            myStatement.append(" ORDER BY ")
            myStatement.append(self.prepareFieldName(ord))
        if (limit > 0):
            myStatement.append(" LIMIT ")
            myStatement.append("%i" % limit)
        myStatement.append(";")
#        if (debugOn > 0):            
        print myStatement
        query.exec_(myStatement)
        #myQuery = self.execStatement(myStatement)
        return query



    def doInsert(self, table, values):
        # 'values' has to be a Python dictionary

        myKeys   = ()
        myValues = ()
        for key,value in values.iteritems():
            myKeys   = myKeys   + (key,)
            myValues = myValues + (value,)

        myStatement = QString("INSERT INTO ")
        myStatement.append(self.prepareFieldName(self.getTableName(table)))
        myStatement.append(" (")
        myStatement.append(self.formatMultipleFields(myKeys))
        myStatement.append(") VALUES (")
        myStatement.append(self.formatMultipleValues(myValues))
        myStatement.append(");")
        if (debugOn > 0):
            print myStatement
        # this is the one and only way for "self.lastAutoID()"!!!
        myQuery = QSqlQuery(myStatement, self)
        return myQuery



    def doUpdate(self, table, values, where, limit = 0):
        # 'values' has to be a Python dictionary
        # 'where' has to be a Python dictionary
        # 'limit' has to be an integer

        myStatement = QString("UPDATE ")
        myStatement.append(self.prepareFieldName(self.getTableName(table)))
        myStatement.append(" SET ")

        setCounter = 0
        for key,value in values.iteritems():
            if (setCounter > 0):
                myStatement.append(",")
            setCounter = setCounter + 1
            myStatement.append(self.prepareFieldName(key))
            myStatement.append("=")
            myStatement.append(self.prepareValue(value))

        whereCounter = 0
        for key,value in where.iteritems():
            if (whereCounter == 0):
                myStatement.append(" WHERE ")
            else:
                myStatement.append(" AND ")
            whereCounter = whereCounter + 1
            myStatement.append(self.prepareFieldName(key))
            myStatement.append("=")
            myStatement.append(self.prepareValue(value))

        if (limit > 0):
            myStatement.append(" LIMIT ")
            myStatement.append("%i" % limit)
        myStatement.append(";")
        if (debugOn > 0):
            print myStatement
        myQuery = self.execStatement(myStatement)
        return myQuery



    def doDelete(self, table, where, limit = 0):
        # 'where' has to be a Python dictionary

        myStatement = QString("DELETE FROM ")
        myStatement.append(self.prepareFieldName(self.getTableName(table)))

        whereCounter = 0
        for key,value in where.iteritems():
            if (whereCounter == 0):
                myStatement.append(" WHERE ")
            else:
                myStatement.append(" AND ")
            whereCounter = whereCounter + 1
            myStatement.append(self.prepareFieldName(key))
            myStatement.append("=")
            myStatement.append(self.prepareValue(value))

        if (limit > 0):
            myStatement.append(" LIMIT ")
            myStatement.append("%i" % limit)

        myStatement.append(";")
        if (debugOn > 0):
            print myStatement
        # this is the one and only way for "self.lastAutoID()"!!!
#        myQuery = self.exec(myStatement)
        return myQuery



    def doCount(self, table, where = {}):
        # 'where' has to be a Python dictionary

        myStatement = QString("SELECT COUNT(*) FROM ")
        myStatement.append(self.prepareFieldName(self.getTableName(table)))

        whereCounter = 0
        for key,value in where.iteritems():
            if (whereCounter == 0):
                myStatement.append(" WHERE ")
            else:
                myStatement.append(" AND ")
            whereCounter = whereCounter + 1
            myStatement.append(self.prepareFieldName(key))
            myStatement.append("=")
            myStatement.append(self.prepareValue(value))

        myStatement.append(";")
        if (debugOn > 0):
            print myStatement
 #       myQuery = self.execStatement(myStatement)
        count = 0
        if (myQuery.next()):
            count = myQuery.value(0).toInt()
        return count



    def lastAutoID(self):
        myID = 0
        myStatement = QString("SELECT LAST_INSERT_ID()")
        myQuery = QSqlQuery(myStatement, self)
        if myQuery.next():
            myID = myQuery.value(0).toInt()
        if (debugOn > 0):
            print "last id:", myID
        return myID



# -----------------------------------------
# this code could be used in future, maybe:
# -----------------------------------------
#        query = QSqlQuery()
#        query.prepare("INSERT INTO table (key1,key2) VALUES (:value1,:value2);")
#        query.bindValue(":value1", Value1)
#        query.bindValue(":value2", Value2)
#        query.execQuery()
# -----------------------------------------

