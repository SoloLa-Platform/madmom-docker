# Beat tracking wrapper
This is a simple wrapper library for beat and down-beat tracking algorithm. Currently, this package only has madmom downbeat tracker
The input audio format should be .wav. But you can use ffmpeg to convert .mp3 to .wav
## Requirement
- [madmom](https://github.com/CPJKU/madmom)
- [ffmpeg](https://ffmpeg.org/)

# Usage
## Command line 
docker run -ti --rm -v $(pwd):/beat_tracker python cli.py input/test.mp3


## Module
```python
import tracker

args = tracker.TrackerArgument()
args.audio_path = 'input/slide.mp3'
args.output_dir_path = 'output/slide'
tracker.track(args)
```

# Convert wav to mp3
```shell
ffmpeg -i input.wav -vn -ar 44100 -ac 2 -b:a 192k output.mp3
```

# Build docker image
```shell
docker build -t beat_tracker:dev -f dev.dockerfile .
```
