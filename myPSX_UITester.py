import sys, os
import Metashape

from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader

def runUI():
    app = QApplication.instance()
    parent = app.activeWindow()
    qload = QUiLoader(parent)
    dialog = qload.load("untitled2.ui")
