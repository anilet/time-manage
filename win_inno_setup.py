# A setup script showing how to extend py2exe.
#
# In this case, the py2exe command is subclassed to create an installation
# script for InnoSetup, which can be compiled with the InnoSetup compiler
# to a single file windows installer.
#
# By default, the installer will be created as dist\Output\setup.exe.

from distutils.core import setup
import matplotlib
import py2exe
import sys
import glob
import os

#Build tree of files given a dir (for appending to py2exe data_files)
#Taken from http://osdir.com/ml/python.py2exe/2006-02/msg00085.html
def tree(src):
    list = [(root, map(lambda f: os.path.join(root, f), files)) for (root, dirs, files) in os.walk(os.path.normpath(src))]
    new_list = []
    for (root, files) in list:
    #print "%s , %s" % (root,files)
        if len(files) > 0 and root.count('.svn') == 0:
            new_list.append((root, files))
    return new_list 

################################################################

class InnoScript:
    def __init__(self,
                 name,
                 lib_dir,
                 dist_dir,
                 windows_exe_files = [],
                 lib_files = [],
                 version = ""):
        self.lib_dir = lib_dir
        self.dist_dir = dist_dir
        if not self.dist_dir[-1] in "\\/":
            self.dist_dir += "\\"
        self.name = name
        self.version = version
        self.windows_exe_files = [self.chop(p) for p in windows_exe_files]
        self.lib_files = [self.chop(p) for p in lib_files]

    def chop(self, pathname):
        assert pathname.startswith(self.dist_dir)
        return pathname[len(self.dist_dir):]
    
    def create(self, pathname="dist\\Delphos.iss"):
        self.pathname = pathname
        ofi = self.file = open(pathname, "w")
        print >> ofi, "; WARNING: This script has been created by py2exe. Changes to this script"
        print >> ofi, "; will be overwritten the next time py2exe is run!"
        print >> ofi, r"[Setup]"
        print >> ofi, r"AppName=%s" % self.name
        print >> ofi, r"AppVerName=%s %s" % (self.name, self.version)
        print >> ofi, r"DefaultDirName={pf}\%s" % self.name
        print >> ofi, r"DefaultGroupName=%s" % self.name
        print >> ofi, r"VersionInfoVersion=%s" % self.version
        print >> ofi, r"VersionInfoCompany=Ecotrust/COBI/WWF"
        print >> ofi, r"VersionInfoDescription=Delphos"
        print >> ofi, r"VersionInfoCopyright=Ecotrust"
        print >> ofi, r"AppCopyright=Ecotrust"
        print >> ofi, r"InfoAfterFile=README.TXT"
        print >> ofi, r"LicenseFile=LICENSE.TXT"
        print >> ofi, r"WizardImageBackColor=clBlack"
        print >> ofi, r"WizardImageFile=images\delphos_vert.bmp"
        print >> ofi, r"WizardSmallImageFile=images\delphos_upper_right.bmp"
        print >> ofi, r"SetupIconFile=images\delphos_icon.ico"
        print >> ofi

        print >> ofi, r"[Files]"
        for path in self.windows_exe_files + self.lib_files:
            if (path == '.\\Delphos.exe.log'):
                #Special case need world write access to error log
                print >> ofi, r'Source: "%s"; DestDir: "{app}\%s"; Flags: ignoreversion; Permissions: users-modify' % (path, os.path.dirname(path))
            else:
                print >> ofi, r'Source: "%s"; DestDir: "{app}\%s"; Flags: ignoreversion' % (path, os.path.dirname(path))

        print >> ofi, r'Source: lib\MSVCP71.dll; DestDir: {app}\lib; Flags: ignoreversion'
        print >> ofi

        print >> ofi, r"[Icons]"
        for path in self.windows_exe_files:
            print >> ofi, r'Name: "{group}\%s"; Filename: "{app}\%s"; IconFilename: "{app}\images\delphos_icon.ico"; WorkingDir: {app}' % \
                  (self.name, path)
                  
        print >> ofi, r'Name: "{group}\Delphos Fisheries Documentation - English"; Filename: "{app}\documentation\fisheries\english\documentation.html"'
        print >> ofi, r'Name: "{group}\Delphos Fisheries Documentation - Spanish"; Filename: "{app}\documentation\fisheries\spanish\documentation.html"'                  
        
        print >> ofi, 'Name: "{group}\Uninstall %s"; Filename: "{uninstallexe}"' % self.name

    def compile(self):
        try:
            import ctypes
        except ImportError:
            try:
                import win32api
            except ImportError:
                import os
                os.startfile(self.pathname)
            else:
                print "Ok, using win32api."
                win32api.ShellExecute(0, "compile",
                                                self.pathname,
                                                None,
                                                None,
                                                0)
        else:
            print "Cool, you have ctypes installed."
            res = ctypes.windll.shell32.ShellExecuteA(0, "compile",
                                                      self.pathname,
                                                      None,
                                                      None,
                                                      0)
            if res < 32:
                raise RuntimeError, "ShellExecute failed, error %d" % res


################################################################

from py2exe.build_exe import py2exe

class build_installer(py2exe):
    # This class first builds the exe file(s), then creates a Windows installer.
    # You need InnoSetup for it.
    def run(self):
        # First, let py2exe do it's work.
        py2exe.run(self)

        lib_dir = self.lib_dir
        dist_dir = self.dist_dir
        
        # create the Installer, using the files py2exe has created.
        script = InnoScript("Delphos 0.4",
                            lib_dir,
                            dist_dir,
                            self.windows_exe_files,
                            self.lib_files)
        print "*** creating the inno setup script***"
        script.create()
        print "*** compiling the inno setup script***"
        script.compile()
        # Note: By default the final setup.exe will be in an Output subdirectory.

######################## py2exe setup options ########################################

zipfile = r"lib\shardlib"

options = {
    "py2exe": {
        "compressed": 1,
        "optimize": 2,
        "includes": ['sip', 'PyQt4', 'matplotlib.numerix.random_array', 'matplotlib.backends.backend_tkagg', 'sqlalchemy.databases.sqlite'],
        "excludes": ['backend_gtkagg', 'backend_wxagg'],
        "dll_excludes": ['libgdk_pixbuf-2.0-0.dll', 'libgobject-2.0-0.dll', 'libgdk-win32-2.0-0.dll'],
        "packages": ["sqlalchemy", "matplotlib", "pytz", "PyQt4"],
        "dist_dir": "dist",
    }
}

matplotlib_data_files = tree('lib\matplotlibdata')
tcl_data_files = tree("lib\\tcl")
doc_data_files = tree('documentation')
sample_data_files = tree('sample')
base_files = [(".",[".\\LICENSE.txt", ".\\README.txt", ".\\Delphos.exe.log"])]
lib_files = [("lib",["lib\\MSVCP71.dll"])]
image_files = [("images",["images\\delphos_icon.ico","images\\delphos_upper_right.bmp","images\\delphos_vert.bmp"])]
data_files = matplotlib_data_files + tcl_data_files + doc_data_files + sample_data_files + base_files + lib_files + image_files 
 
setup(
    options = options,
    # The lib directory contains everything except the executables and the python dll.
    zipfile = zipfile,
    windows=[{"script": "Delphos.py"}],
    # use out build_installer class as extended py2exe build command
    cmdclass = {"py2exe": build_installer},
    data_files = data_files
)
