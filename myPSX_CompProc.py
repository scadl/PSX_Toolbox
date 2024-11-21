import sys, os
import Metashape

from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader

def showMyComponentProcessorDialog():
    class myComponentProcessor(QDialog):
        def __init__(self,parent):
            QDialog.__init__(self, parent)

            self.setWindowTitle("Batch Component Processor (by SCADl)")
            self.setGeometry(550, 550, 350, 110)
            self.setFixedSize(350, 110)

            self.exec()

    app = QApplication.instance()
    parent = app.activeWindow()
    myComponentProcessor(parent)
