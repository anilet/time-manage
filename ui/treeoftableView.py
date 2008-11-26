#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import lib.treeoftable

class ServerModel(lib.treeoftable.TreeOfTableModel):

    def __init__(self, parent=None):
        super(ServerModel, self).__init__(parent)
        print "in servermodel"

    def data(self, index, role):
        if role == Qt.DecorationRole:
            node = self.nodeFromIndex(index)
            if node is None:
                return QVariant()
            if isinstance(node, lib.treeoftable.BranchNode):
                if index.column() != 0:
                    return QVariant()
#                filename = node.toString().replace(" ", "_")
#                parent = node.parent.toString()
#                if parent and parent != "USA":
#                    return QVariant()
#                if parent == "USA":
#                    filename = "USA_" + filename
                filename = os.path.join(os.path.dirname(__file__),
                                        "images", "filenew.png")
                pixmap = QPixmap(filename)
                if pixmap.isNull():
                    return QVariant()
                return QVariant(pixmap)
        return lib.treeoftable.TreeOfTableModel.data(self, index, role)


class TreeOfTableWidget(QTreeView):

    def __init__(self, parent=None):
        super(TreeOfTableWidget, self).__init__(parent)
        self.setSelectionBehavior(QTreeView.SelectRows)
        self.setUniformRowHeights(True)
        headers = ["Job Status", "Number", "Date"]
        print "in Treeof TableWidget"
        model = ServerModel(self)
        self.setModel(model)
        self.model().headers = headers
        try:
            model.load()
        except IOError, e:
            pass
            #QMessageBox.warning(self, "Server Info - Error")
        self.connect(self, SIGNAL("activated(QModelIndex)"),
                     self.activated)
        self.connect(self, SIGNAL("expanded(QModelIndex)"),
                     self.expanded)
        self.expanded()


    def currentFields(self):
        return self.model().asRecord(self.currentIndex())


    def activated(self, index):
        self.emit(SIGNAL("activated"), self.model().asRecord(index))


    def expanded(self):
        for column in range(self.model().columnCount(QModelIndex())):
            self.resizeColumnToContents(column)


#class MainForm(QMainWindow):
#
#    def __init__(self, parent=None):
#        super(MainForm, self).__init__(parent)
#        headers = ["Job Status", "Number", "Date"]
#        print "in Mainform"
#        if nesting != 3:
#            if nesting == 1:
#                headers = ["Country/State (US)", "City", "Provider",
#                           "Server"]
#            elif nesting == 2:
#                headers = ["Country/State (US)/City", "Provider",
#                           "Server"]
#            elif nesting == 4:
#                headers = ["Country/State (US)/City/Provider/Server"]
#            headers.append("IP")
#
#        self.treeWidget = TreeOfTableWidget()
#        self.treeWidget.model().headers = headers
#        self.setCentralWidget(self.treeWidget)
#
#        QShortcut(QKeySequence("Escape"), self, self.close)
#        QShortcut(QKeySequence("Ctrl+Q"), self, self.close)
#
#        self.connect(self.treeWidget, SIGNAL("activated"),
#                     self.activated)
#
#        self.setWindowTitle("Job Numbers")
#        self.statusBar().showMessage("Ready...", 5000)


#    def picked(self):
#        return self.treeWidget.currentFields()
#
#
#    def activated(self, fields):
#        self.statusBar().showMessage("*".join(fields), 60000)


#app = QApplication(sys.argv)
##nesting = 3
##if len(sys.argv) > 1:
##    try:
##        nesting = int(sys.argv[1])
##    except:
##        pass
##    if nesting not in (1, 2, 3, 4):
##        nesting = 3
#
#form = MainForm()
#form.resize(750, 550)
#form.show()
#app.exec_()
#print "*".join(form.picked())

