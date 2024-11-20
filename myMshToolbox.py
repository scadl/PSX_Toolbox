import sys, os, Metashape

from PySide2.QtCore import Qt
from tkinter import *
from PySide2.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QWidget, QGridLayout

def simple_qtPySide():

    class MyWind(QDialog):
        def __init__(self,parent):
            QDialog.__init__(self, parent)

            self.setWindowTitle("MyWindow")
            self.setGeometry(500, 250, 500, 300)
            self.setFixedSize(500, 300)

            self.btnP1 = QPushButton("&Execute")
            self.btnP1.clicked.connect(self.runAct)

            layout = QGridLayout()
            layout.setContentsMargins(20, 0, 20, 0)

            layout.addWidget(self.btnP1, 3, 1)
            self.setLayout(layout)
            
            self.exec()
        
        def runAct(self):
            print("All videos imported according plan")

    app = QApplication.instance()
    parent = app.activeWindow()
    MyWind(parent)


label_path = "scadl/Hello"
Metashape.app.addMenuItem(label3, simple_qtPySide)