import sys, os
import Metashape
import myPSX_Localizer

class Results:
    good = 0
    bad = 0

'''
buildModel(
surface_type=Arbitrary, 
interpolation=EnabledInterpolation, 
face_count=HighFaceCount,
 face_count_custom=200000, 
 source_data=DepthMapsData[, classes], 
 vertex_colors=True,
 vertex_confidence=True, 
 volumetric_masks=False, 
 keep_depth=True, 
 replace_asset=False,
 split_in_blocks=False[, blocks_crs], 
 blocks_size=250[, blocks_origin],
 clip_to_boundary=False, 
 export_blocks=False, 
 build_texture=True, 
 output_folder='',
 max_workgroup_size=100[, progress]
 trimming_radius=10[, cameras][, frames]
'''

def allPointToMesh():

    localizedStr = myPSX_Localizer.MyPSX_Localizer()
    procRes = Results()

    doc = Metashape.app.document;
    chunk = doc.chunk;

    for pc in chunk.point_clouds:
        print (">>> Processing: Key - " +str(pc.key) + " Label - " +str(pc.label))
        chunk.point_cloud = pc
        print(pc.point_count_by_class)
        try:
            chunk.buildModel(Metashape.SurfaceType.Arbitrary, Metashape.Interpolation.EnabledInterpolation, Metashape.FaceCount.MediumFaceCount, 20000, Metashape.DataSource.PointCloudData, Metashape.PointClass.Created)
            #Metashape.DataSource.TiePointsData
            chunk.model.label = "Model - PtCl "+pc.label
            procRes.good+=1
        except Exception as e:
            print(">>> Error: " + str(e))
            procRes.bad+=1
    #Metashape.Chunk.buildPointCloud
    Metashape.app.messageBox(localizedStr.finishedComp_msg.format(goodV=str(procRes.good),badV=str(procRes.bad)))