# ============================================================
# KUMULA.py
# central library with necessary routines for each KUMULA program
# ------------------------------------------------------------
# Copyright (C) 2003-2005 the Kumula Team.
# Licensed under the LGPL.
# ============================================================

import sys
import os
import os.path
import string

#from ConfigParser import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

#from ClientSelectDlg import KClientSelectDlg
#from ClientInterface import KClientInterface

from Database import KDatabase
#from CountryInterface import KCountryInterface
#from DocumentInterface import KDocumentInterface
#from SettingsInterface import KSettingsInterface


# ------------------------------------------------------------

# Global variables
ProgramName = None    # QString
ProgramPath = None    # QString
UserName    = None    # QString
UserPath    = None    # QString
ProgParams  = {}      # Dictionary of QString

#ClientID     = QString("")   # QString
#ClientName   = QString("")   # QString
#ClientNeeded = 0             # Boolean

# central database object and interfaces
DB              = None    # KDatabase
#CountryIntf     = None    # KCountryInterface
#ClientIntf      = None    # KClientInterface
#DocumentIntf    = None    # KDocumentInterface
#GlobalSettings  = None    # KSettingsInterface
#ProgramSettings = None    # KSettingsInterface

# Global objects
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

# External applications
#AppBrowser = None
#AppEmail   = None
#AppPDF     = None

# UI language
LANG = None

# UI parameters
uiWinDim       = 0
uiTearOff      = 0
uiTextProgMenu = 0
uiToolButtons  = 0
uiIconSet      = None


# ============================================================


# ------------------------------------------------------------
# Paths relative to the $KUMULA/bin directory
#
#fileConfig   = "~/.kumularc"
#dirExec      = QString("/bin/")
#dirMenuIcons = QString("/graphics/actions/")
#dirToolIcons = QString("/graphics/actions/")
#dirProgIcons = QString("/graphics/programs/")
#dirSplashes  = QString("/graphics/splash/")
#dirLanguages = QString("/i18n/")
#dirLibs      = QString("/lib/")


# ------------------------------------------------------------
# OLD ICON ROUTINES - DEPRECATED
# get the icons stored in KUMULADIR/graphics/...


#def getIcon(aFileName, aIconType):
#    global ProgramPath, dirProgIcons, dirMenuIcons, dirToolIcons
#
#    myFile = QString(ProgramPath)
#    if aIconType == 0:
#        myFile.append(dirProgIcons)
#    elif aIconType == 1:
#        myFile.append(dirMenuIcons)
#    else:
#        myFile.append(dirToolIcons)
#    myFile.append(aFileName)
#    myFile.append(".png")
#    result = QPixmap(myFile)
#    return result
#
#def getProgIcon(aFileName):
#    return getIcon(aFileName, 0)
#
#def getMenuIcon(aFileName):
#    return getIcon(aFileName, 1)
#
#def getToolIcon(aFileName):
#    return getIcon(aFileName, 2)
#
#
## ------------------------------------------------------------
## NEW ICON ROUTINES
## get the icons stored in KUMULADIR/graphics/ProgramName/
#
#
#def getIconDir():
#    global ProgramPath, ProgramName, uiIconSet
#    myDirName = os.path.join(ProgramPath.ascii(), "graphics", uiIconSet.ascii(), ProgramName.ascii())
#    return myDirName
#
#
#def getIconByName(aName):
#    myName = aName + ".png"
#    myPixmapFile = QString(os.path.join(getIconDir(), myName))
#    return QPixmap(myPixmapFile)
#
#def getProgramIcon():
#    myPixmapFile = QString(os.path.join(getIconDir(), "program.png"))
#    return QPixmap(myPixmapFile)
#
#
#def getMenuBarIcon(anIconName, sysMenu=0):
#    myFileName = QString("m_")
#    myFileName.append(anIconName)
#    myFileName.append(".png")
#    if (sysMenu == 0):
#        myPixmapFile = QString(os.path.join(getIconDir(), myFileName.ascii()))
#    else:
#        myPixmapFile = QString(os.path.join(getIconDir(), "..", myFileName.ascii()))
#    return QPixmap(myPixmapFile)
#
#def getSideBarIcon(anIconName):
#    myFileName = QString("s_")
#    myFileName.append(anIconName)
#    myFileName.append(".png")
#    return QPixmap(QString(os.path.join(getIconDir(), myFileName.ascii())))
#
#def getToolBarIcon(anIconName):
#    myFileName = QString("t_")
#    myFileName.append(anIconName)
#    myFileName.append(".png")
#    return QPixmap(QString(os.path.join(getIconDir(), myFileName.ascii())))
#
#
#
#
## ------------------------------------------------------------
## getLanguage
## gets language informations from a QM file
#
#def getLanguage(aLanguage):
#    global ProgramPath, ProgramName, dirLanguages
#
#    myFile = ProgramPath
#    myFile.append(dirLanguages)
#    myFile.append(ProgramName)
#    myFile.append("/")
#    myFile.append(aLanguage)
#    myFile.append(".qm")
#    f = open(myFile, "r")
#    result = QLanguage(f.readlines())
#    f.close()
#    return result


def readSetting(aParser, aGroup, aName, default):
    getted = QString(aParser.get(aGroup, aName))
    if (getted):
        myResult = QString(getted)
    else:
        myResult = QString(default)
    return myResult


def readConfigFile(errorHandling):
    global ProgramName
    global MainWin
    global UserPath
    global DBHost, DBPort, DBName, DBUser, DBPass, DBType
#    global AppBrowser, AppEmail, AppPDF
#    global LANG
    global uiWinDim, uiTearOff, uiTextProgMenu, uiToolButtons, uiIconSet
    
    myCfgFile = QString(UserPath)
    myCfgFile.append("/.kumularc")
    try:
        cfg = ConfigParser()
        cfg.read(myCfgFile.latin1())
        LANG       = readSetting(cfg, "language", "lang", "EN")
        DBHost     = readSetting(cfg, "database", "host", "localhost")
        DBName     = readSetting(cfg, "database", "name", "kumula")
        DBPort     = readSetting(cfg, "database", "port", "3306")
        DBUser     = readSetting(cfg, "database", "user", "root")
        DBPass     = readSetting(cfg, "database", "pass", "")
        DBType     = readSetting(cfg, "database", "type", "QMYSQL3")
        AppBrowser = readSetting(cfg, "applications", "browser", "mozilla")
        AppEmail   = readSetting(cfg, "applications", "email", "mozilla")
        AppPDF     = readSetting(cfg, "applications", "pdfview", "gv")
        uiWinDim       = int(readSetting(cfg, "ui", "windim", "1").ascii())
        uiTearOff      = int(readSetting(cfg, "ui", "tearoff", "0").ascii())
        uiTextProgMenu = int(readSetting(cfg, "ui", "textprogmenu", "0").ascii())
        uiToolButtons  = int(readSetting(cfg, "ui", "toolbuttons", "0").ascii())
        uiIconSet      = readSetting(cfg, "ui", "iconset", "Crystal")
    except:
        # set default values (needed by Configurator)...
        LANG       = QString("EN")
        DBHost     = QString("localhost")
        DBName     = QString("kumula")
        DBPort     = QString("3306")
        DBUser     = QString("root")
        DBPass     = QString("")
        DBType     = QString("QMYSQL3")
        AppBrowser = QString("mozilla")
        AppEmail   = QString("mozilla")
        AppPDF     = QString("gv")
        uiWinDim       = 1
        uiTearOff      = 1
        uiTextMenuProg = 1
        uiToolButtons  = 0
        uiIconSet      = QString("Crystal")
        # ...and do error handling (if needed)
        if (errorHandling != 0):
            ErrorMsg = QString("Couldn't read configuration file<br><b>")
            ErrorMsg.append(myCfgFile)
            ErrorMsg.append("!</b><br><br>Do you want to run <b>Configurator</b> now?")
            if (QMessageBox.critical(MainWin, "Error", ErrorMsg, QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes):
                runKumulaApp("configurator", {'caller':ProgramName})
            sys.exit(0)


def initDatabase():
    global DB, DBHost, DBPort, DBName, DBUser, DBPass, DBType
    global MainWin, ProgramName

    DB = KDatabase(DBType, DBName, Program)
    DB.setDatabaseName(DBName)
    DB.setUserName(DBUser)
    DB.setPassword(DBPass)
    DB.setHostName(DBHost)

    if DB.open():
#        print "Successfully opened '%s' on '%s' for '%s'." % (DBName,DBHost,ProgramName)
        return 1
    else:
        ErrorMsg = QString("Couldn't access<br>database <b>")
        ErrorMsg.append(DBName)
        ErrorMsg.append("</b><br>as <b>")
        ErrorMsg.append(DBUser)
        ErrorMsg.append("</b><br>on <b>")
        ErrorMsg.append(DBHost)
        ErrorMsg.append("</b>!")
        QMessageBox.critical(MainWin, "Error", ErrorMsg)
        return 0



def getAutoID(aTable, anIDfield, aTemplate, aTitle):

    def getParamLength(aTemplate, aParam):
        leftStr = QString("%%")
        leftStr.append(aTemplate)
        leftStr.append("(")
        if (aTemplate.find(leftStr) > 0):
            return 1
            # ....

    myAutoID = QString(aTemplate)
#    myAutoID.replace("%%")
    # ...
    return myAutoID



def getUserName(aUserID):
    global DB

    myName = QString("")
    myForename = QString("")
    quUser = DB.doSelect("users", ("name","forename"), "", {"userid":aUserID}, 1)
    while quUser.next():
        myName     = quUser.value(0).toString()
        myForename = quUser.value(1).toString()
    myUserName = QString(myName)
    myUserName.append(", ")
    myUserName.append(myForename)
    return myUserName



# ------------------------------------------------------------
# runKumulaApp
# executes a program of the Kumula Suite (parameters are possible)


def runKumulaApp(aName, aParams={}):
    global ProgramPath, dirExec
    myExec = QString(ProgramPath)
    myExec.append(dirExec)
    myExec.append(aName)
    myExec.append(".py")
    myParamStr = QString("")
    for key,value in aParams.iteritems():
        myParamStr.append(key)
        myParamStr.append("=")
        myParamStr.append(value)
    runExternalApp(myExec, myParamStr)

def isAppInstalled(aName):
    global ProgramPath, dirExec
    myExec = QString(ProgramPath)
    myExec.append(dirExec)
    myExec.append(aName)
    myExec.append(".py")
    if QFile.exists(myExec):
        return 1
    else:
        return None


# ------------------------------------------------------------
# runExternalApp
# executes an external program (parameters are possible)


def runExternalApp(aName, aParam):
# Variant 1: Use Python for executing
    myExec = QString(aName)
    myExec.append(" ")
    myExec.append(aParam)
    os.popen2(myExec.latin1())
# Variant 2: Use Qt for executing
#    proc = QProcess()
#    proc.addArgument(aName)
#    proc.addArgument(aParam)
#    proc.start()
# ^^^ History will show which is more effective
#    print aName, aParam

    
# ------------------------------------------------------------
# initPathsAndNames
# sets important paths and names, necessary for the real init()
# and used by "lighter" programs, e.g. "configurator".

def initPathsAndNames():
    global ProgramName,ProgramPath
    global UserName,UserPath
    global Program
 
    # initalize program path
    ProgramName = QString(sys.argv[0])
    uPro =  sys.argv[0]
    print ProgramName
    ProgramName = ProgramName.right(ProgramName.length()-uPro.rfind("/") - 1)
    print ProgramName
    #ProgramName = "Time Management"
    ProgramName = ProgramName.left(uPro.rfind("."))
    print ProgramName
    ProgramPath = QString(os.path.dirname(os.path.abspath(sys.argv[0])))
    uPath  = os.path.dirname(os.path.abspath(sys.argv[0]))
    print ProgramPath
    ProgramPath = ProgramPath.left(uPath.rfind("/"))
    print ProgramPath
    # initialize user path
    UserPath = QString(os.path.expanduser("~"))
    uuPath = os.path.expanduser("~")
    UserName = UserPath.right(UserPath.length()-uuPath.rfind("/")-1)
    print UserName
    # initialize applicatiro
    Program = QApplication(sys.argv)

    for i in range(len(sys.argv)):
        if (i > 0):
            (key,value) = string.split(sys.argv[i], "=")
            ProgParams[key] = QString(value)




def showSplashScreen():
    global Splash, ProgramPath, ProgramName, dirSplashes

    screen = QApplication.desktop().screenGeometry()
    filename = QString(ProgramPath)
    filename.append(dirSplashes)
    filename.append(ProgramName)
    filename.append('.png')
    splashpic = QPixmap(filename)
    Splash = QLabel(None, "splash", 
        Qt.WDestructiveClose | Qt.WStyle_Customize | Qt.WStyle_NoBorder |\
        Qt.WX11BypassWM | Qt.WStyle_StaysOnTop)
    Splash.setFrameStyle(QFrame.NoFrame)
    Splash.setPixmap(splashpic)
    Splash.adjustSize()
    Splash.setCaption(ProgramName)
    Splash.move(QPoint(screen.center().x() - Splash.width()/2, 
                       screen.center().y() - Splash.height()/2))
    Splash.show()
    Splash.repaint(0)
    QApplication.flush()


def hideSplashScreen():
    global Splash
    if Splash:
        del Splash


# ------------------------------------------------------------
# init
# sets important parameters for the program

def init(needClient=0, needDMS=0):

    global ProgramName, ProgramPath
    global Program
    global UserPath, UserName
    global ProgParams
    global DB, CountryIntf, ClientIntf, DocumentIntf
    global GlobalSettings, ProgramSettings
    global ClientID, ClientName, ClientNeeded

    initPathsAndNames()
    readConfigFile(1)
    if (initDatabase() == 0):
        sys.exit(1)

    GlobalSettings = KSettingsInterface(DB, "", UserName)
    if GlobalSettings.readInt("", "showSplash", 0) == 1:
        showSplashScreen()

    ProgramSettings = KSettingsInterface(DB, ProgramName, UserName)
    CountryIntf     = KCountryInterface(DB)
    ClientIntf      = KClientInterface(DB)
    DocumentIntf    = KDocumentInterface(DB)

    ClientNeeded = needClient
    if (needClient == 1):
        try:
            ClientID   = ProgParams["client"]
            ClientName = ClientIntf.getClientName(ClientID)
        except:
            ClientID = QString("")
            ClientName = QString("")

        if (ClientName == ""):
            # if none arguments given (or client not found), let the user select a client
            myDlg = KClientSelectDlg()
            hideSplashScreen()
            if (myDlg.exec_loop() == QDialog.Accepted):
                ClientID   = myDlg.listClients.selectedItem().text(0)
                ClientName = myDlg.listClients.selectedItem().text(1)
            else:
                sys.exit(0)




# ------------------------------------------------------------
# run
# executes the application
    
def run():
    global Program, MainWin, Splash

    Program.setMainWidget(MainWin)
    Program.connect(Program, SIGNAL("lastWindowClosed()"),
                    Program, SLOT("quit()"))
    hideSplashScreen()
    MainWin.show()
    Program.exec_loop()
    sys.exit(0)


