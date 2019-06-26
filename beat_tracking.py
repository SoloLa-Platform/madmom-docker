import madmom
import numpy as np
import sys
import subprocess
import os

def downbeat_tracking(audioPath):
    proc = madmom.features.DBNDownBeatTrackingProcessor(beats_per_bar=[
        4, 4], fps=100)
    act = madmom.features.RNNDownBeatProcessor()(audioPath)
    # print(proc(act))
    beats = proc(act)
    return beats


def write_downbeats(beats, OUTPUT_PATH="downbeats.txt"):
    with open(OUTPUT_PATH, 'w') as f:
        for i, v in enumerate(beats):
            f.write("{},{}\n".format(v[0], v[1]))

def beat_tracking(fp):
    
    proc = madmom.features.beats.DBNBeatTrackingProcessor(fps=100)
    act =  madmom.features.beats.RNNBeatProcessor()(fp)
    # print(proc(act))
    beats = proc(act)
    return beats

def write_beats(beats, OUTPUT_PATH = "beats.txt"):

    with open(OUTPUT_PATH, 'w') as f:
        for i,v in enumerate(beats):
            f.write("{},{}\n".format(i,v))

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

if __name__ == '__main__':
    

    OUTPUT_PREFIX = "./output/"

    filePath = sys.argv[1]
    filePathPieces = os.path.basename(filePath).split(".")
    print("\n")
    print(filePathPieces)

    if filePathPieces[1] != 'wav' and  filePathPieces[1] != 'mp3':
        print("unsupported audio type (only support mp3,wav)")
        exit()

    if filePathPieces[1] == 'mp3' or  filePathPieces[1] == 'MP3':
        print("[Info] Automatically convert .mp3 to .wav by ffmpeg")
        # subprocess.run(["ffmpeg", "-i", "{}".format(filePath), "{}.wav".format(filePathPieces[0])])
    
    outputDir = "{}{}/".format(OUTPUT_PREFIX, filePathPieces[0])
    create_folder(outputDir)

    print("Start beat_tracking....")
    beats = beat_tracking(filePath)
    write_beats(beats, "{}/beats.txt".format(outputDir))
    print("Finish beat_tracking")

    print("Start downbeat_tracking")
    downbeats = downbeat_tracking(filePath)
    write_downbeats(downbeats, "{}/downbeats.txt".format(outputDir))
    print("Finish downbeat_tracking")


    
    