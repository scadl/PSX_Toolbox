import sys, os
import Metashape

from PySide2.QtCore import Qt
from tkinter import *
from PySide2.QtWidgets import QApplication, QDialog, QPushButton, QGridLayout, QLabel, QHBoxLayout, QLineEdit


def simple_qtPySide():

    class MyWind(QDialog):
        def __init__(self,parent):
            QDialog.__init__(self, parent)

            self.setWindowTitle("MyWindow")
            self.setGeometry(500, 250, 500, 130)
            self.setFixedSize(500, 130)

            self.btnP1 = QPushButton("&Execute")
            self.btnP1.clicked.connect(self.runAct)

            
            gridLayout_2 = QGridLayout()
            gridLayout_2.setObjectName(u"gridLayout_2")
            gridLayout_2.setContentsMargins(20, 1, 20, 1)
            self.pushButton = QPushButton()
            self.pushButton.setObjectName(u"pushButton")

            gridLayout_2.addWidget(self.pushButton, 4, 0, 1, 1)

            self.label = QLabel()
            self.label.setObjectName(u"label")

            gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

            self.horizontalLayout_2 = QHBoxLayout()
            self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
            self.lineEdit = QLineEdit()
            self.lineEdit.setObjectName(u"lineEdit")

            self.horizontalLayout_2.addWidget(self.lineEdit)

            self.pushButton_3 = QPushButton()
            self.pushButton_3.setObjectName(u"pushButton_3")

            self.horizontalLayout_2.addWidget(self.pushButton_3)


            gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

            self.horizontalLayout = QHBoxLayout()
            self.horizontalLayout.setObjectName(u"horizontalLayout")
            self.lineEdit_2 = QLineEdit()
            self.lineEdit_2.setObjectName(u"lineEdit_2")

            self.horizontalLayout.addWidget(self.lineEdit_2)

            self.pushButton_2 = QPushButton()
            self.pushButton_2.setObjectName(u"pushButton_2")

            self.horizontalLayout.addWidget(self.pushButton_2)


            gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)

            self.label_2 = QLabel()
            self.label_2.setObjectName(u"label_2")

            gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

            #layout = QGridLayout()
            #layout.setContentsMargins(20, 0, 20, 0)

            #layout.addWidget(self.btnP1, 3, 1)
            self.setLayout(gridLayout_2)
            
            self.retranslateUi(parent)

            self.exec()

        def retranslateUi(self, Dialog):
            Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
            self.pushButton.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
            self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
            self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
            self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
            self.label_2.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
            # retranslateUi
        
        def runAct(self):
            print("All videos imported according plan")
            

    app = QApplication.instance()
    parent = app.activeWindow()
    MyWind(parent)


label_path = "SCADl_Toolbox/Hello PySyde"
Metashape.app.addMenuItem(label_path, simple_qtPySide)