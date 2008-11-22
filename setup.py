# from distutils.core import setup
# import py2exe
# import sys
# import logging
# import logging
# if hasattr(sys, "frozen"):
    # import logging
    # logging._srcfile = r"logging\__init__.pyo"
# setup(windows=[{"script":"atlastimedlg.py"}], options={"py2exe":{"includes":["sip"]}})
# options = {'py2exe':{'excludes':['OpenGL'],
                    # 'packages':['ctypes','logging','weakref'],
                    # 'includes':['new','distutils.util', 'sip', 'PyQt4._qt'],
                    # 'bundle_files':1}}

from distutils.core import setup
import py2exe
import glob
import sys
import os

#sys.path.insert(0, os.path.join(sys.prefix, "PyOpenGL-3.0.0b2-py2.5.egg"))

#import pkg_resources as p
# use an Environment object with a custom search path
#env = p.Environment(['.','modules','plugins'])
# for dists in env:
    # pkgs = env[dists]
    # # only activate the newest distribution available
    # dist = pkgs.pop(0)
    # print "activating ", dist
    # dist.activate()
def tree(src):
 	    list = [(root, map(lambda f: os.path.join(root, f), files)) for (root, dirs, files) in os.walk(os.path.normpath(src))]
 	    new_list = []
	    for (root, files) in list:
 	    #print "%s , %s" % (root,files)
 	        if len(files) > 0 and root.count('.svn') == 0:
 	            new_list.append((root, files))
 	    return new_list 


options = {'py2exe':{'excludes':['OpenGL','backend_gtkagg', 'backend_wxagg'],
                    'packages':['logging','matplotlib'],
					'dll_excludes': ['libgdk_pixbuf-2.0-0.dll', 'libgobject-2.0-0.dll', 'libgdk-win32-2.0-0.dll'],
                    'includes':['distutils.util', 'sip', 'matplotlib.backends.backend_qt4agg', 'PyQt4']}}

xdata_files=[ ('sqldrivers', glob.glob('sqldrivers/*.*' )),
                        'libmySQL.dll'
                    ]
matplotlib_data_files = tree('mpl-data')
setup(
	name = "Time Manager", 
	version="1.0",
	windows=[{"script":"atlastimedlg.py","icon_resources": [(0, "time.ico")]}],
	options=options,
	data_files=xdata_files + matplotlib_data_files
	)

#setup (
#        package_dir = {'test':'.'},
#        scripts = [ 'MyApp.py' ],
#        options={"py2exe" : {"includes" : ["sip", "PyQt4._qt"]}}
