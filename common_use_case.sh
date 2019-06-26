# env: windows cmd.exe 
# execution location: solola/madmon_beat_tracking
# input audio location: locate at same directory with beat_tracking.py, e.g. test.mp3
# output: output/[filename]/beats.txt &　output/[filename]/downbeats.txt e.g. 　output/test/downbeats.txt 

# docker image: madmom_beat_tracking:prod
# only mount input & output dir
docker build -t madmom_beat_tracking:prod -f production.dockerfile .

docker run -ti --rm -v E:\workplace\projects\solola\madmom-docker\input:/madmom-docker/input^
-v E:\workplace\projects\solola\madmom-docker\output:/madmom-docker/output^
madmom_beat_tracking:prod python beat_tracking.py input/test.mp3

# docker image: madmom_beat_tracking:dev
# mount source codes
docker build -t madmom_beat_tracking:dev -f dev.dockerfile .

docker run -ti --rm -v E:\workplace\projects\solola\madmom-docker:/madmom-docker/^ 
madmom_beat_tracking:dev python beat_tracking.py input/test.mp3

