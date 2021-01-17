from context import tracker

if __name__ == "__main__":
    args = tracker.TrackerArgument()
    args.audio_path = 'input/slide.mp3'
    args.output_dir_path = 'output/slide'
    tracker.track(args)
    
