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

buildDepthMaps(
downscale=4, 
filter_mode=MildFiltering[, cameras], 
reuse_depth=False,                            
max_neighbors=16, 
subdivide_task=True, 
workitem_size_cameras=20,
max_workgroup_size=100[, progress])

buildUV(
mapping_mode=GenericMapping, 
page_count=1, 
texture_size=8192, 
pixel_size=0[, camera][,progress]
 )

 buildTexture(
 blending_mode=MosaicBlending, 
 texture_size=8192, 
 fill_holes=True, 
 ghosting_filter=True[, cameras], 
 texture_type=DiffuseMap[, source_model], 
 transfer_texture=True,
 workitem_size_cameras=20, 
 max_workgroup_size=100, 
 anti_aliasing=1[, progress])
'''

localizedStr = myPSX_Localizer.MyPSX_Localizer()
procRes = Results()
texSize = 2048;

def allPointToMesh():

    doc = Metashape.app.document;
    chunk = doc.chunk;

    for pc in chunk.point_clouds:
        print (">>> Processing: Key - " +str(pc.key) + " Label - " +str(pc.label))
        chunk.point_cloud = pc
        print(pc.point_count_by_class)
        try:
            chunk.buildModel(Metashape.SurfaceType.Arbitrary, Metashape.Interpolation.EnabledInterpolation, Metashape.FaceCount.MediumFaceCount, 20000, Metashape.DataSource.PointCloudData, Metashape.PointClass.Created)

            # UVMaps are required for building textures
            chunk.buildUV(Metashape.MappingMode.GenericMapping, 1, texSize);

            # Build Texture from UV and Photos (MosaicBlendeing broken from 2.1.3, using Avarege)
            chunk.buildTexture(Metashape.BlendingMode.AverageBlending, texSize)

            #Metashape.DataSource.TiePointsData
            chunk.model.label = "Model - PtCl "+pc.label
            procRes.good+=1
        except Exception as e:
            print(">>> Error: " + str(e))
            procRes.bad+=1
        doc.save();
    #Metashape.Chunk.buildPointCloud
    Metashape.app.messageBox(localizedStr.finishedComp_msg.format(goodV=str(procRes.good),badV=str(procRes.bad)))

def allTiePointsToMesh():

    doc = Metashape.app.document;
    chunk = doc.chunk;

    startComp = doc.chunk.components[0].key
    endComp = doc.chunk.components[len(doc.chunk.components)-1].key

    for comp in chunk.components:
        print (">>> Processing Component: Key - " +str(comp.key) + " Label - " +str(comp.label))                          
        try:
            # Set cycle component as current for chaunk processing
            chunk.component = comp 

            # DepthMaps Are reauried for Point Clouds and Polygoinal Meshes
            # Quality is set 1st param: 1- Ultra high, 2- High, 4- Medium, 8- Low, 16- Lowest
            chunk.buildDepthMaps(4, Metashape.FilterMode.MildFiltering, chunk.cameras, False)

            # Buald Model from TiePoints and DepthMaps
            chunk.buildModel(Metashape.SurfaceType.Arbitrary, Metashape.Interpolation.DisabledInterpolation, Metashape.FaceCount.MediumFaceCount, 20000, Metashape.DataSource.DepthMapsData)

            # UVMaps are required for building textures
            chunk.buildUV(Metashape.MappingMode.GenericMapping, 1, texSize);

            # Build Texture from UV and Photos (MosaicBlendeing broken from 2.1.3, using Avarege)
            chunk.buildTexture(Metashape.BlendingMode.AverageBlending, texSize)

            chunk.model.label = "Model - TiePD "+comp.label
            procRes.good+=1
        except Exception as e:
            print(">>> Error: " + str(e))
            procRes.bad+=1
        doc.save();
    #Metashape.Chunk.buildPointCloud
    Metashape.app.messageBox(localizedStr.finishedComp_msg.format(goodV=str(procRes.good),badV=str(procRes.bad)))