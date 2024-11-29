import sys, os
import Metashape

from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader

def aboutPlugin():
    Metashape.app.messageBox("This plugin built for Metasahpe 2.1.3 and pySide 2 by\nKarnaushenko Alexander Dmitrievich (scadl) at November 2024")

def runUI():
    app = QApplication.instance()
    parent = app.activeWindow()
    qload = QUiLoader(parent)
    dialog = qload.load("VideoImportForm.ui")
