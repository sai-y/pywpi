#!/usr/bin/python3

import glob
import shutil

if __name__ == "__main__":

    for file in glob.glob('txt_files/file1[0-9][0-9].txt'):
    	shutil.move(file, '.')

    for file in glob.glob('file1[0-9][0-9].txt'):
    	shutil.copy(file, 'cpy_files')