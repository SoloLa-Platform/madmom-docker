# Madmom Beat/Downbeat tracking in Docker Environment

## Basic Usage
docker run -ti --rm -v E:\workplace\projects\solola\madmom-docker:/madmom-docker/ ^ madmom_beat_tracking:prod python beat_tracking.py -s /madmom-docker/input/slide.wav -o /madmom-docker/output/slide

## Detail
docker run -ti --rm -v E:\workplace\projects\solola\madmom-docker:/madmom-docker/ ^ madmom_beat_tracking:prod python beat_tracking.py -h
