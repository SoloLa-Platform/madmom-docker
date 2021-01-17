from tracker.tracker import track

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter, 
        description=
    """
===================================================================
Script for downbeat and beat tracking
===================================================================
    """)
    parser.add_argument('-s', '--audio_path', type=str, help="absolute path of audio file")
    parser.add_argument('-o', '--output_dir_path', type=str, help="absolute path of beats/downbeat output directory", default="./outputs/beat_tracking")
    
    return parser.parse_args()
    

if __name__ == '__main__':
    args = parse_args()
    track(args)
    
    
    