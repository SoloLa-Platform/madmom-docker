# env: windows git bash
# execution location: solola/madmon_beat_tracking
# input audio location: locate at same directory with beat_tracking.py, e.g. test.mp3
# output: output/[filename]/beats.txt &　output/[filename]/downbeats.txt e.g. 　output/test/downbeats.txt 
docker run -ti --rm -v E:\workplace\projects\solola\solola\madmom_beat_tracking:/madmom madmom:test python beat_tracking.py test.mp3
