import subprocess
import sys
import os

total_args = len(sys.argv)
cmd_args = str(sys.argv)

if total_args == 3:
    root1, ext1 = os.path.splitext(sys.argv[1])
    root2, ext2 = os.path.splitext(sys.argv[2])
    if ext1 == '.mp3' and ext2 == '.wav':
        subprocess.call(['ffmpeg', '-i', sys.argv[1], "output/"+sys.argv[2]])
    else:
        print "extensions must be .wav and .mp3"
else:
    print "please use sintax"
    print "python mp3towav.py <name_file.mp3> <name_file.wav>"
