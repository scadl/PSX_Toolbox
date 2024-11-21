import sys, os
import Metashape

from PySide2.QtCore import Qt
from tkinter import *
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader

def simple_qtPySide():

    class MyWind(QDialog):

        vidPath = ""
        vidStep = 10

        def __init__(self,parent):
            QDialog.__init__(self, parent)

            self.setWindowTitle("Batch Video Importer")
            self.setGeometry(550, 550, 350, 110)
            self.setFixedSize(350, 110)

            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)

            #self.btnP1 = QPushButton("&Execute")
            #self.btnP1.clicked.connect(self.runAct)

            #From Layout
            gridLayout = QGridLayout()
            gridLayout.setObjectName(u"gridLayout_2")
            gridLayout.setContentsMargins(10, 10, 10, 10)

            #Label 1 on main form
            self.label_1 = QLabel()
            self.label_1.setObjectName(u"label")
            gridLayout.addWidget(self.label_1, 1, 0, 1, 1)

            #Nested Horizontal Layout 1 (row) - Pathe select
            self.horizontalLayout_1 = QHBoxLayout()
            self.horizontalLayout_1.setObjectName(u"horizontalLayout_2")
            #Text Edit (Line Edit in QT) for showing path
            self.lineEdit = QLineEdit()
            self.lineEdit.setObjectName(u"lineEdit")
            self.lineEdit.setReadOnly(True)
            self.lineEdit.setEnabled(False)
            self.horizontalLayout_1.addWidget(self.lineEdit)
            #Simple Button (Push Button) for selecting folder
            self.pushButton_10 = QPushButton()
            self.pushButton_10.setObjectName(u"pushButton_3")
            self.horizontalLayout_1.addWidget(self.pushButton_10)
            #Adding Nested Horizontal Layout 1 into global Grid Layout
            gridLayout.addLayout(self.horizontalLayout_1, 2, 0, 1, 1)

            #Nested Horizontal Layout 2 (row)
            self.horizontalLayout_3 = QHBoxLayout()
            self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
            #Another Label, this time for Spinner
            self.label = QLabel()
            self.label.setObjectName(u"label")
            sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
            sizePolicy2.setHorizontalStretch(0)
            sizePolicy2.setVerticalStretch(0)
            sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
            self.horizontalLayout_3.addWidget(self.label)
            # ComboBox for predifiend step type
            self.comboBox = QComboBox()
            self.comboBox.addItem("")
            self.comboBox.addItem("")
            self.comboBox.setObjectName(u"comboBox")
            self.comboBox.setEditable(False)
            self.comboBox.setCurrentText(u"Elem1")
            self.horizontalLayout_3.addWidget(self.comboBox)
            # The spinner itself. Used to set frame step
            self.spinBox = QSpinBox()
            self.spinBox.setObjectName(u"spinBox")
            sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
            sizePolicy3.setHorizontalStretch(50)
            sizePolicy3.setVerticalStretch(50)
            sizePolicy3.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
            self.spinBox.setMinimum(1)
            self.spinBox.setMaximum(1000)
            self.spinBox.setValue(10)
            self.spinBox.setEnabled(False)
            self.horizontalLayout_3.addWidget(self.spinBox)
            #Adding Nested Horizontal Layout 2 into global Grid Layout
            gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

            # The Button, runing the whole process. Nested into "Row" 2
            self.pushButton = QPushButton()
            self.pushButton.setObjectName(u"pushButton")
            sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
            gridLayout.addWidget(self.pushButton)

            #layout = QGridLayout()
            #layout.setContentsMargins(20, 0, 20, 0)

            #layout.addWidget(self.btnP1, 3, 1)

            #Aplying Global layout to foem
            self.setLayout(gridLayout)
            
            # Setting up all lables texts
            self.pushButton.setText(u"Start Import")
            self.label_1.setText(u"Path to videos for import")
            self.pushButton_10.setText(u"...",)
            self.label.setText(u"Frame Step")

            #Binding events to requred controls
            self.pushButton_10.clicked.connect(self.selPath)
            self.pushButton.clicked.connect(self.runAct)
            self.spinBox.valueChanged.connect(self.usrSetFrame)

            self.exec()

        def usrSetFrame(self, val):
            print("Frame Step: "+str(val))
            self.vidStep = val


        def selPath(self, type):
            openDialog = QFileDialog(parent, "Select your videos path", "")
            openDialog.setFileMode(QFileDialog.Directory)
            #openDialog.setNameFilter("Images (*.png *.xpm *.jpg);;Text files (*.txt);;XML files (*.xml)")
            openDialog.setOption(openDialog.ShowDirsOnly,True)
            if openDialog.exec_():
                myFolder = openDialog.selectedFiles()[0]
                self.lineEdit.setText(myFolder)
                self.vidPath = myFolder
                print("Type "+str(type)+", Path:" + myFolder)         
            
            
        def runAct(self):
            doc = Metashape.app.document;
            args = sys.argv;

            print ('Number of arguments:', len(args));
            #print ('Argument List:', str(args));
            #doc.open(args[1]);
            files = os.listdir(self.vidPath);

            print ("Finded files: ", str(files));

            for vid in files:
                print("Processing file: ", vid);
                chunk = doc.addChunk();
                vid_lbl = vid.replace(".", "-");
                chunk.label = vid_lbl;
                save_frame = os.path.join(self.vidPath, "frames_"+vid_lbl);
                if (os.path.isdir(save_frame)==False):
                    os.mkdir(save_frame);
                if (len(args) == 4):
                    chunk.importVideo(
                        os.path.join(self.vidPath, vid), 
                        os.path.join(save_frame, vid_lbl+"_{filenum}.png"), 
                        Metashape.FrameStep.CustomFrameStep,
                        int(self.vidStep)
                )
                else:
                    chunk.importVideo(
                        os.path.join(self.vidPath, vid), 
                        os.path.join(save_frame, vid_lbl+"_{filenum}.png"), 
                        Metashape.FrameStep.SmallFrameStep
                    )
                doc.save();

            Metashape.app.messageBox("All videos imported according plan")
            doc.save()
            
            

    app = QApplication.instance()
    parent = app.activeWindow()
    MyWind(parent)

def runUI():
    app = QApplication.instance()
    parent = app.activeWindow()
    qload = QUiLoader(parent)
    dialog = qload.load("untitled2.ui")


label_path = "SCADl_Toolbox/Batch Video Import"
Metashape.app.addMenuItem(label_path, simple_qtPySide)