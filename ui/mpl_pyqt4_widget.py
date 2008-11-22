#!/usr/bin/env python
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt4 import NavigationToolbar2QT as NavigationToolbar
#from matplotlib.numerix import arange
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.pyplot as mpl

from pylab import *
from PyQt4.QtSql import *
#import numpy as N
#import numpy.numarray as na


class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width = 2, height = 4, dpi = 100, sharex = None, sharey = None):
        self.figure = Figure(figsize = (width, height), dpi=dpi, facecolor = '#FFFFFF')
        #self.figure = Figure()
        import calendar
        #xtick.major.size     : 4      # major tick size in points
#xtick.minor.size     : 2      # minor tick size in points
#xtick.major.pad      : 4      # distance to major tick label in points
#xtick.minor.pad      : 4      # distance to the minor tick label in points
#xtick.color          : k      # color of the tick labels
#xtick.labelsize      : medium # fontsize of the tick labels
#xtick.direction      : in     # direction: in or out
        mpl.rcParams['xtick.minor.size'] = 3
        mpl.rcParams['ytick.labelsize'] =6
        mpl.rcParams['xtick.labelsize'] =6 
        
        #minorLocator = MultipleLocator(1.0)
        #minorFormattor = FormatStrFormatter('%0.1f')
        
        self.axis = self.figure.add_subplot(111)
        self.axis.set_xlabel('Date')   
        self.axis.set_ylabel('Hours')   
        self.axis.set_title('Hours Graph')   
        self.axis.grid(True)  
        xmin, xmax = 1, 31
        ymin, ymax = 0, 14
        #mpl.
        self.axis.axis([1, 31, 0, 15])
        FigureCanvas.__init__(self, self.figure)
#self.fc = FigureCanvas(self.fig)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

	def format_labels(self):
		self.axis.set_title(self.PlotTitle)
		self.axis.title.set_fontsize(8)
		self.axis.set_xlabel(self.xtitle, fontsize = 8)
		self.axis.set_ylabel(self.ytitle, fontsize = 8)
		labels_x = self.axis.get_xticklabels()
		labels_y = self.axis.get_yticklabels()

		for xlabel in labels_x:
			xlabel.set_fontsize(6)
		for ylabel in labels_y:
			ylabel.set_fontsize(6)
			ylabel.set_color('b')

	def sizeHint(self):
		w, h = self.get_width_height()
		return QSize(w, h)

	def minimumSizeHint(self):
		return QSize(8, 8)

	def sizeHint(self):
		w, h = self.get_width_height()
		return QSize(w, h)

	def minimumSizeHint(self):
		return QSize(8, 8)


class MPL_Widget(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.canvas = MyMplCanvas()
        #self.toolbar = NavigationToolbar(self.canvas, self.canvas)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.canvas)
        #self.vbox.addWidget(self.toolbar)
        self.setLayout(self.vbox)

