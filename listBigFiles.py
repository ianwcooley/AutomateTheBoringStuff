#! python3

# listBigFiles.py - prints to screen all files larger than the provided size
# within a given folder
# Usage: ./listBigFiles.py <size in bytes> <folder>

import sys, os, shutil

size = int(sys.argv[1])
folder = sys.argv[2]

# throw error and exit program if folder doesn't exist
if not os.path.exists(folder):
    print("Error: folder '" + folder + "' doesn't exist")
    sys.exit()

for foldername, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        filepath = os.path.join(foldername, filename)
        filesize = os.path.getsize(filepath)
        if filesize > size:
            print(filesize, filepath)
