import Metashape
import myPSX_VideoImport
import myPSX_CompProc
import myPSX_UITester
import myPSX_Localizer

localizedStr = myPSX_Localizer.MyPSX_Localizer()
Metashape.app.removeMenuItem("SCADl_Toolbox")

Metashape.app.addMenuItem("SCADl_Toolbox/"+localizedStr.menu_item_1, myPSX_VideoImport.showMyBatchVideoImportDialog)
Metashape.app.addMenuItem("SCADl_Toolbox/"+localizedStr.menu_item_2, myPSX_CompProc.updateCompNamesWKeys)
Metashape.app.addMenuItem("SCADl_Toolbox/"+localizedStr.menu_item_3, myPSX_CompProc.showMyComponentProcessorDialog)
#Metashape.app.addMenuSeparator("SCADl_Toolbox/---------------/")
Metashape.app.addMenuItem("SCADl_Toolbox/"+localizedStr.menu_item_4, myPSX_UITester.aboutPlugin)


