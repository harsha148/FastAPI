import argparse
import os
import subprocess
from glob import glob

import numpy as np

if __name__ == '__main__':
    # parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
    # parser.add_argument('-v', '--version', action='version', version='1.0')
    # subparsers = parser.add_subparsers(dest='command', required=True)
    # subparsers.add_parser('run')
    # args = parser.parse_args()
    # if args.command == 'run':
    #     cmd1 = 'ffmpeg -i '
    #     in_dir = 'C:/Users/harsh/OneDrive/Desktop/20240228/rot'
    #     cmd2 = ' -vf "transpose=1" '
    #     out_dir = 'C:/Users/harsh/OneDrive/Desktop/20240228'
    #     input_vids = glob(os.path.join(in_dir, "*.{}".format('mp4')))
    #     print(f'Found the videos in input directory')
    #     print(input_vids)
    #     for in_vid in input_vids:
    #         vid_name = os.path.basename(in_vid)
    #         print(f'Rotating video:{vid_name}')
    #         cmd = cmd1 + in_vid + cmd2 + out_dir + '/' + vid_name
    #         print(f'Running command: {cmd}')
    #         # subprocess.call(['pwd'])
    #         os.system(cmd)
    p = np.array([1,2,3,4,5])
    print(p[...,1:])

