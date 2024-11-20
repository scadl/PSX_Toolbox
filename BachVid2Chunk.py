import sys, os, Metashape;
doc = Metashape.app.document;
args = sys.argv;

print ('Number of arguments:', len(args));
#print ('Argument List:', str(args));
doc.open(args[1]);
files = os.listdir(args[2]);

print ("Finded files: ", str(files));

for vid in files:
    print("Processing file: ", vid);
    chunk = doc.addChunk();
    vid_lbl = vid.replace(".", "-");
    chunk.label = vid_lbl;
    save_frame = os.path.join(args[2], "frames_"+vid_lbl);
    if (os.path.isdir(save_frame)==False):
        os.mkdir(save_frame);
    if (len(args) == 4):
        chunk.importVideo(
            os.path.join(args[2], vid), 
            os.path.join(save_frame, vid_lbl+"_{filenum}.png"), 
            Metashape.FrameStep.CustomFrameStep,
            int(args[3])
        )
    else:
        chunk.importVideo(
            os.path.join(args[2], vid), 
            os.path.join(save_frame, vid_lbl+"_{filenum}.png"), 
            Metashape.FrameStep.SmallFrameStep
        )
    doc.save();
print("All videos imported according plan")
doc.save()