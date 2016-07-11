#!/usr/bin/python3

import os

if __name__ == "__main__":
    if os.path.isfile('/home/pi/Desktop/code_samples/write_file.txt'):
        print('The file exists!')
    else:
        print('The file does not exist!')