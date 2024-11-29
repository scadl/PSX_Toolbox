import sys, os
import Metashape
import myPSX_Localizer

from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader

localizedStr = myPSX_Localizer.MyPSX_Localizer()

def aboutPlugin():
    Metashape.app.messageBox(localizedStr.about_msg)

def runUI():
    app = QApplication.instance()
    parent = app.activeWindow()
    qload = QUiLoader(parent)
    dialog = qload.load("VideoImportForm.ui")
