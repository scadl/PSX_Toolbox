
import sys, os
import Metashape
import myPSX_Localizer

from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from enum import Enum

class procType(Enum):
    PointCloudONLY = 1
    TexturedMeshFromPontCloud = 2
    TexturedMeshFromComponents = 3


def showMyComponentProcessorDialog():
    class myComponentProcessor(QDialog):

        qual = 4;
        startComp = 0;
        endComp = 0;
        myProcType = procType;

        def __init__(self,parent):
            QDialog.__init__(self, parent)

            self.setWindowTitle(localizedStr.menu_item_3)
            self.setGeometry(550, 550, 250, 130)
            self.setFixedSize(350, 130)

            #Form Main Layout
            gridLayout = QGridLayout()
            gridLayout.setObjectName(u"gridLayout_2")
            gridLayout.setContentsMargins(10, 10, 10, 10)

            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)

            hBoxLayout = QHBoxLayout()
            hBoxLayout.setObjectName(u"hbox")
            hBoxLayout.setSizeConstraint(QLayout.SetMaximumSize)

            doc = Metashape.app.document;

            #Label 1 on main form
            self.label_1 = QLabel()
            self.label_1.setObjectName(u"label1")
            hBoxLayout.addWidget(self.label_1)

            #Spinner 1
            self.spinBox_1 = QSpinBox()
            self.spinBox_1.setObjectName(u"spinBox_1")
            self.spinBox_1.valueChanged.connect(self.usrSetStart)
            hBoxLayout.addWidget(self.spinBox_1)

            #Label 2 on main form
            self.label_2 = QLabel()
            self.label_2.setObjectName(u"label2")
            hBoxLayout.addWidget(self.label_2)

            #Spinner 2
            self.spinBox_2 = QSpinBox()
            self.spinBox_2.setObjectName(u"spinBox_2")
            self.spinBox_2.valueChanged.connect(self.usrSetEnd)
            hBoxLayout.addWidget(self.spinBox_2)

            gridLayout.addLayout(hBoxLayout, 0, 0, 1, 1)

            hBoxLayout2 = QHBoxLayout()
            hBoxLayout2.setObjectName(u"hbox2")
            hBoxLayout2.setSizeConstraint(QLayout.SetMaximumSize)

            #Label 3 on main form
            self.label_3 = QLabel()
            self.label_3.setObjectName(u"label3")
            hBoxLayout2.addWidget(self.label_3)

            # ComboBox for predifiend step type
            self.comboBox = QComboBox()
            self.comboBox.setObjectName(u"comboBox")
            self.comboBox.setEditable(False)
            self.comboBox.currentIndexChanged.connect(self.setQual)
            hBoxLayout2.addWidget(self.comboBox)

            gridLayout.addLayout(hBoxLayout2, 1, 0, 1, 1)

            self.checkBox = QCheckBox()
            self.checkBox.setObjectName(u"checkBox")
            self.checkBox.stateChanged.connect(self.setNetMode)
            self.checkBox.setEnabled(False)
            gridLayout.addWidget(self.checkBox)

            hBoxLayout3 = QHBoxLayout()
            hBoxLayout3.setObjectName(u"horizontalLayout_3")

            # The Button, runing the whole process. Nested into "Row" 2
            self.pushButton = QPushButton()
            self.pushButton.setObjectName(u"pushButton")
            self.pushButton.setEnabled(True)
            #sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
            self.pushButton.setSizePolicy(sizePolicy)
            hBoxLayout3.addWidget(self.pushButton)

            self.pushButton2 = QPushButton()
            self.pushButton2.setObjectName(u"pushButton2")
            self.pushButton2.setEnabled(True)
            #sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
            self.pushButton2.setSizePolicy(sizePolicy)
            hBoxLayout3.addWidget(self.pushButton2)

            self.pushButton3 = QPushButton()
            self.pushButton3.setObjectName(u"pushButton3")
            self.pushButton3.setEnabled(True)
            #sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
            self.pushButton3.setSizePolicy(sizePolicy)
            hBoxLayout3.addWidget(self.pushButton3)

            gridLayout.addLayout(hBoxLayout3, 6, 0, 1, 1);

            if (len(doc.chunk.components)<=0):
                self.pushButton.setEnabled(False) 
                self.spinBox_1.setEnabled(False)
                self.spinBox_2.setEnabled(False)
                Metashape.app.messageBox(localizedStr.emptyChunk_msg)
                self.close()
            else:
                self.pushButton.clicked.connect(self.runAct)
                self.pushButton2.clicked.connect(self.runAct)
                self.pushButton3.clicked.connect(self.runAct)


            self.pushButton.setText(localizedStr.startCompProc)
            self.label_1.setText(localizedStr.comProcLbl_1)
            self.label_2.setText(localizedStr.comProcLbl_2)
            self.label_3.setText(localizedStr.comProcLbl_Qual)
            self.checkBox.setText(localizedStr.compProcUseNet)
            self.comboBox.addItem(localizedStr.compProcQaulItem[0])
            self.comboBox.addItem(localizedStr.compProcQaulItem[1])
            self.comboBox.addItem(localizedStr.compProcQaulItem[2])
            self.comboBox.addItem(localizedStr.compProcQaulItem[3])
            self.comboBox.addItem(localizedStr.compProcQaulItem[4])
            self.comboBox.setCurrentIndex(2)

            self.startComp = doc.chunk.components[0].key
            self.endComp = doc.chunk.components[len(doc.chunk.components)-1].key
            startKey = doc.chunk.components[0].key
            endKey = doc.chunk.components[len(doc.chunk.components)-1].key
            self.spinBox_1.setMinimum(startKey)
            self.spinBox_1.setMaximum(endKey)
            self.spinBox_1.setValue(startKey)
            self.spinBox_2.setMinimum(startKey)
            self.spinBox_2.setMaximum(endKey)
            self.spinBox_2.setValue(endKey)
            
            #Aplying Global layout to form
            self.setLayout(gridLayout)
            self.exec()

        def setNetMode(self, val):

            print("Net mode: "+str(val))
            if val > 0:
                #print(Metashape.app.settings.language)
                Metashape.app.settings.network_enable = True
            else: 
                Metashape.app.settings.network_enable = False

        def setQual(self, val):
                        
            #(1- Ultra high, 2- High, 4- Medium, 8- Low, 16- Lowest
            if val == 0:
                self.qual = 1
            elif val == 1:
                self.qual = 2
            elif val == 2:
                self.qual = 4
            elif val == 3:
                self.qual = 8
            elif val == 4:
                self.qual = 16
            print("Selected qauality: Ind:"+str(val)+", val:"+str(self.qual))


        def usrSetStart(self, val):
            #print("User start component: "+str(Val))
            self.startComp = val

        def usrSetEnd(self, val):
            #print("User end component: "+str(Val))
            self.endComp = val

        def runAct(self):

            doc = Metashape.app.document;
            chunk = doc.chunk;
            good = 0;
            bad = 0;

            '''
            buildPointCloud(source_data=DepthMapsData, point_colors=True, point_confidence=False,
                            keep_depth=True, max_neighbors=100, uniform_sampling=True, 
                            points_spacing=0.1[,asset ], subdivide_task=True, workitem_size_cameras=20, 
                            max_workgroup_size=100, replace_asset=False[, frames][, progress]
            buildDepthMaps(downscale=4, filter_mode=MildFiltering[, cameras], reuse_depth=False,
                            max_neighbors=16, subdivide_task=True, workitem_size_cameras=20,
                            max_workgroup_size=100[, progress])
            '''

            print(">>> Components: "+str(len(chunk.components))+" Selected diapazone: "+str(self.startComp)+"-"+str(self.endComp))

            for comp in chunk.components:
                print (">>> Processing Component: Key - " +str(comp.key) + " Label - " +str(comp.label))
                if (comp.key >= self.startComp and comp.key <= self.endComp):                    
                    chunk.component = comp
                    #(1- Ultra high, 2- High, 4- Medium, 8- Low, 16- Lowest
                    try:
                        chunk.buildDepthMaps(2,Metashape.FilterMode.MildFiltering, chunk.cameras,False)
                        chunk.buildPointCloud(Metashape.DataSource.DepthMapsData,True)
                        chunk.point_cloud.label = "densePoints - "+comp.label+" key "+str(comp.key)
                        good += 1
                    except Exception as e:
                        print(">>> Error: " + str(e))
                        bad += 1
                else:
                    print("Component Key - " +str(comp.key) + " not in diapazone")
                doc.save();

            if(good == 0 and bad == 0):
                Metashape.app.messageBox(localizedStr.noComponents_msg)
                updateCompNamesWKeys()
            else:
                Metashape.app.messageBox(localizedStr.finishedComp_msg.format(goodV=str(good),badV=str(bad)))


    app = QApplication.instance()
    parent = app.activeWindow()
    localizedStr = myPSX_Localizer.MyPSX_Localizer()
    myComponentProcessor(parent)


def updateCompNamesWKeys():
    app = QApplication.instance()
    doc = Metashape.app.document;
    chunk = doc.chunk;
    for comp in chunk.components:
        comp.label += " Key "+ str(comp.key)

    Metashape.app.messageBox(localizedStr.compMarksOk)