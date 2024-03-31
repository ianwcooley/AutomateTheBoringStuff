#! python3

# selectiveCopy.py - walks through a folder tree and searches for files with
# a certain file extension (such as .pdf or .jpg). It copies these files from
# whatever location they are in to a new folder.
# Usage: ./selectiveCopy.py <extension> <search folder> <output folder>

import sys, os, shutil

extension, searchFolder, outputFolder = sys.argv[1:4]

# throw error and exit program if search folder doesn't exist
if not os.path.exists(searchFolder):
    print("Error: search folder doesn't exist")
    sys.exit()

# make output folder if it doesn't exist
if not os.path.exists(outputFolder):
    os.mkdir(outputFolder)

for foldername, subfolders, filenames in os.walk(searchFolder):
    for filename in filenames:
        if filename.endswith(extension):
            filepath = os.path.join(foldername, filename)
            shutil.copy(filepath, outputFolder)