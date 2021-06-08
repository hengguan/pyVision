# -*- coding: utf-8 -*-

import functools
import math
import os
import os.path as osp
import re
import webbrowser

import imgviz
from qtpy import QtCore
from qtpy.QtCore import Qt
from qtpy import QtGui
from qtpy import QtWidgets

# from labelme import __appname__
# from labelme import PY2
# from labelme import QT5

# from . import utils
from gui.config import get_config
# from labelme.label_file import LabelFile
# from labelme.label_file import LabelFileError
# from labelme.logger import logger
# from labelme.shape import Shape
# from labelme.widgets import BrightnessContrastDialog
# from labelme.widgets import Canvas
# from labelme.widgets import LabelDialog
# from labelme.widgets import LabelListWidget
# from labelme.widgets import LabelListWidgetItem
# from labelme.widgets import ToolBar
# from labelme.widgets import UniqueLabelQListWidget
# from labelme.widgets import ZoomWidget


# FIXME
# - [medium] Set max zoom value to something big enough for FitWidth/Window

# TODO(unknown):
# - [high] Add polygon movement with arrow keys
# - [high] Deselect shape when clicking and already selected(?)
# - [low,maybe] Preview images on file dialogs.
# - Zoom is too "steppy".


LABEL_COLORMAP = imgviz.label_colormap(value=200)


class MainWindow(QtWidgets.QMainWindow):

    FIT_WINDOW, FIT_WIDTH, MANUAL_ZOOM = 0, 1, 2

    def __init__(self, config=None):

        # see labelme/config/default_config.yaml for valid configuration
        # if config is None:
        #     config = get_config()
        # self._config = config
        super().__init__()
        self.title = 'pyvision'
        self.left = 10
        self.top = 10
        self.width = 1080
        self.height = 720
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
        
        # exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        # exitButton.setShortcut('Ctrl+Q')
        # exitButton.setStatusTip('Exit application')
        # exitButton.triggered.connect(self.close)
        # fileMenu.addAction(exitButton)
    
        self.show()

