import Metashape
import myPSX_VideoImport
import myPSX_CompProc
import myPSX_UITester
import myPSX_Localizer
import myPSX_MeshBuilder

localizedStr = myPSX_Localizer.MyPSX_Localizer()
Metashape.app.removeMenuItem("SCADl_Toolbox")

#Metashape.app.addMenuSeparator("SCADl_Toolbox/-------Semi-Automatic--------")
Metashape.app.addMenuItem("SCADl_Toolbox/"+localizedStr.menu_item_1, myPSX_VideoImport.showMyBatchVideoImportDialog)
Metashape.app.addMenuItem("SCADl_Toolbox/"+localizedStr.menu_item_3, myPSX_CompProc.showMyComponentProcessorDialog)
#Metashape.app.addMenuSeparator("SCADl_Toolbox/-------Automatic--------")
Metashape.app.addMenuItem("SCADl_Toolbox/"+localizedStr.menu_item_2, myPSX_CompProc.updateCompNamesWKeys)
Metashape.app.addMenuItem("SCADl_Toolbox/"+localizedStr.menu_item_5, myPSX_MeshBuilder.allPointToMesh)
#Metashape.app.addMenuItem("SCADl_Toolbox/"+localizedStr.menu_item_6, myPSX_MeshBuilder.allTiePointsToMesh)
#Metashape.app.addMenuSeparator("SCADl_Toolbox/---------------")
Metashape.app.addMenuItem("SCADl_Toolbox/"+localizedStr.menu_item_4, myPSX_UITester.aboutPlugin)


