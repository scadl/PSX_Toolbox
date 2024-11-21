import Metashape
import myPSX_VideoImport
import myPSX_CompProc
import myPSX_UITester

Metashape.app.addMenuItem("SCADl_Toolbox/Batch Video Import", myPSX_VideoImport.showMyBatchVideoImportDialog)
Metashape.app.addMenuItem("SCADl_Toolbox/Batch Component Processor", myPSX_CompProc.showMyComponentProcessorDialog)
Metashape.app.addMenuItem("SCADl_Toolbox/QT UI Loader", myPSX_UITester.runUI)
