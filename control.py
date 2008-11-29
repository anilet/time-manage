#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2007-8 Phoenix IT Solutions. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

#import logging
#FORMAT = '[%(levelname)-7s] [%(name)-35s] - %(message)s' 
#logging.basicConfig(level=logging.DEBUG, format=FORMAT)
#logger = logging.getLogger('ControlProgressIndicator')

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

import ui.ui_controlprogressindicator

updated = False

class ControlProgressIndicator(QFrame,
        ui.ui_controlprogressindicator.Ui_ControlProgressIndicator):

    def __init__(self, parent=None):
        super(ControlProgressIndicator, self).__init__(parent)
        self.__index = 0
        #logger.debug('Showing Progress')
        #self.setWindowFlags(Qt.Popup) 
        self.setupUi(self)
        self.setWindowModality( Qt.ApplicationModal );
        self.resize( 400, 100 );
        self.setWindowFlags( Qt.FramelessWindowHint | Qt.Dialog );
      #ui.setupUi( this );

        self.setFrameShadow( QFrame.Plain );
        self.setFrameShape( QFrame.Box );
        self.updated = False
        timer = QTimer(self)
        #self.connect(timer, SIGNAL("timeout()"), self.closeMe)
        self.connect(timer, SIGNAL("timeout()"), self.hideMe)
        #self.connect( self.tabWidget, SIGNAL('selected(QString)'), self.tabChanged )
        timer.start(1000)

    def closeMe(self):
        global updated
        if not updated:
            #self.lblMessage.setText("Data Saved")
            updated = True
        else:
            self.close()
            
#    def hideMe(self):
#        global updated
#        if not updated:
#            self.statusLabel.setText("Data Saved")
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
