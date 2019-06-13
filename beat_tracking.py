import madmom
import numpy as np
import sys
import subprocess

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

if __name__ == '__main__':

    filename = sys.argv[1]
    filenamePieces = filename.split(".")

    if filenamePieces[1] != 'wav' and  filenamePieces[1] != 'mp3':
        print("unsupported audio type (only support mp3,wav)")
        exit()

    if filenamePieces[1] == 'mp3' or  filenamePieces[1] == 'MP3':
        print("[Info] Automatically convert .mp3 to .wav by ffmpeg")
        subprocess.run(["ffmpeg", "-i", "{}".format(filename), "{}.wav".format(filenamePieces[0])])
    
    print("Start beat_tracking....")
    beats = beat_tracking(filename)
    write_beats(beats)
    print("Finish beat_tracking")

    print("Start downbeat_tracking")
    downbeats = downbeat_tracking(filename)
    write_downbeats(downbeats)
    print("Finish downbeat_tracking")


    
    