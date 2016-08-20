# ----------------------------------
# Copyright 2016, Benedikt J. Daurer
# plusminus is distributed under the terms of the MIT license
# -----------------------------------------------------------
import os, sys
import numpy as np
import pyqtgraph as pg
from PyQt4 import QtCore, QtGui, uic

currdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currdir)
Ui_mainwindow, base = uic.loadUiType(currdir + '/ui/mainwindow.ui', from_imports=False)

class PlusMinusGui(QtGui.QMainWindow, Ui_mainwindow):
    """TODO: needs a docstring"""

    def __init__(self, plusminus, theme):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self._pm = plusminus
        self._init_style(theme)
        self._init_icons()
        self._init_toolbar()
        self._init_connections()
        self._init_shortcuts()
        self._init_canvas()
        
    def _init_style(self, theme):
        """Define the style."""
        if theme == 'default':
            filename = os.path.dirname(os.path.realpath(__file__)) + '/qss/default.qss'
        elif theme == 'black':
            filename = os.path.dirname(os.path.realpath(__file__)) + '/qss/black.qss'
        elif theme == 'white':
            filename = os.path.dirname(os.path.realpath(__file__)) + '/qss/white.qss'
        with open(filename) as f:
            self.setStyleSheet(f.read()) 
        
    def _init_icons(self):
        """Initialize icons."""
        self._icon_left_gray  = QtGui.QIcon(currdir + '/icons/arrow_left.svg')
        self._icon_right_gray = QtGui.QIcon(currdir + '/icons/arrow_right.svg')
        self._icon_down_gray  = QtGui.QIcon(currdir + '/icons/thumb_down_gray.svg')
        self._icon_down_red   = QtGui.QIcon(currdir + '/icons/thumb_down_red.svg')
        self._icon_up_gray    = QtGui.QIcon(currdir + '/icons/thumb_up_gray.svg')
        self._icon_up_green   = QtGui.QIcon(currdir + '/icons/thumb_up_green.svg')
        
    def _init_toolbar(self):
        """Initialize toolbar."""
        self.left.setIcon(self._icon_left_gray)
        self.right.setIcon(self._icon_right_gray)
        self.down.setIcon(self._icon_down_gray)
        self.up.setIcon(self._icon_up_gray)

    def _init_connections(self):
        """Initialize connections."""
        self.left.clicked.connect(self._on_trigger_left)
        self.right.clicked.connect(self._on_trigger_right)
        self.up.toggled.connect(self._on_trigger_up)
        self.down.toggled.connect(self._on_trigger_down)
        self._pm.update.connect(self._on_update)

    def _init_shortcuts(self):
        """Initialize shortcuts."""
        self.left.setShortcut("left")
        self.right.setShortcut("right")
        self.up.setShortcut("up")
        self.down.setShortcut("down")
        
    def _init_canvas(self):
        """Initialize canvas."""
        self.canvas.ci.layout.setContentsMargins(0, 0, 0, 0)
        self.canvas.ci.layout.setSpacing(0)
        self.canvas.ci.border = (0,0,0)
        self.view = self.canvas.addViewBox(row=0, col=0, lockAspect=True, enableMouse=False, invertY=True)
        self.imageitem = pg.ImageItem(self._pm.image, autoDownsample=True)
        self.view.addItem(self.imageitem)
        self.view.autoRange(padding=0.02)
        self.view.enableAutoRange(self.view.XYAxes)
        aspect = float(self._pm.image.shape[0]/self._pm.image.shape[1])
        self.resize(0.95*self._pm.height*aspect,self._pm.height)
        
    def resizeEvent(self, event):
        """Overwrites QtGui.QMainWindow.resizeEvent and                                                                                                                           
        additionally calls QtGui.QApplication.processEvents()."""
        QtGui.QMainWindow.resizeEvent(self, event)
        QtGui.QApplication.processEvents()    
        
    @QtCore.pyqtSlot()        
    def _on_trigger_left(self):
        self._pm.prev()
        
    @QtCore.pyqtSlot()
    def _on_trigger_right(self):
        self._pm.next()
        
    @QtCore.pyqtSlot(bool)
    def _on_trigger_up(self, active=True):
        if active:
            self.up.setIcon(self._icon_up_green)
            self.down.setChecked(False)
            self._pm.plus()
        else:
            self.up.setIcon(self._icon_up_gray)

    @QtCore.pyqtSlot(bool)
    def _on_trigger_down(self, active=True):
        if active:
            self.down.setIcon(self._icon_down_red)
            self.up.setChecked(False)
            self._pm.minus()
        else:
            self.down.setIcon(self._icon_down_gray)

    @QtCore.pyqtSlot()
    def _on_update(self):
        self.imageitem.setImage(self._pm.image, autolevels=False)
        self.view.autoRange()
        if self._pm.status is None:
            self.up.setChecked(False)
            self.down.setChecked(False)
        else:
            self.up.setChecked(self._pm.status)
            self.down.setChecked(not self._pm.status)
        
        
class PlusMinus(QtCore.QObject):
    update = QtCore.pyqtSignal()
    
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.height = 1000
        self.image  = np.random.random((100,100))
        self.status = None 
            
    def next(self):
        print "Clicked on next, now update"
        self.image = np.random.random((100,100))
        self.status = None
        self.update.emit()

    def prev(self):
        print "Clicked on prev, now update"
        self.image  = np.random.random((100,100))
        self.status = None
        self.update.emit()
            
    def plus(self):
        print "Thumbs up (plus)"
        self.status = True

    def minus(self):
        print "Thumbs down (minus)"
        self.status = False

def opengui(plusminus=None, theme='default'):
    if plusminus is None:
        plusminus = PlusMinus()
    app = QtGui.QApplication([])
    frame = PlusMinusGui(plusminus, theme)
    frame.show()
    app.exec_()

# Debugging
if __name__ == '__main__':
    opengui()
