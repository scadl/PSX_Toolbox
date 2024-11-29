import Metashape
import myPSX_VideoImport
import myPSX_CompProc
import myPSX_UITester

Metashape.app.removeMenuItem("SCADl_Toolbox")

Metashape.app.addMenuItem("SCADl_Toolbox/Batch Video Import", myPSX_VideoImport.showMyBatchVideoImportDialog)
Metashape.app.addMenuItem("SCADl_Toolbox/Show Component keys", myPSX_CompProc.updateCompNamesWKeys)
Metashape.app.addMenuItem("SCADl_Toolbox/Batch Component Processor", myPSX_CompProc.showMyComponentProcessorDialog)
#Metashape.app.addMenuSeparator("SCADl_Toolbox/---------------/")
Metashape.app.addMenuItem("SCADl_Toolbox/- About this plugin -", myPSX_UITester.aboutPlugin)


