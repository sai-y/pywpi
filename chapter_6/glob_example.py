#!/usr/bin/python3

import glob

if __name__ == "__main__":
	# List all files
    for file in glob.glob('/home/pi/Desktop/code_samples/chapter_6'):
    	print file
