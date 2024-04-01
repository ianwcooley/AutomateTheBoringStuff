#! python3

# fileNumberGaps.py - considers all files in a single folder with a given 
# prefix and identical suffix, e.g. spam001.txt, spam003.txt, etc. and if
# there are any gaps in the numbering, renames files so that there are no
# gaps. Conversely, can also create gaps in such numberings so that new 
# files can be added (assuming we've closed any other gaps already).

# Assumes a 0-padded numbering system, with the number of place values
# determined by the largest number, e.g. if largest number is 473, then 
# file 9 will be represented as 009, file 27 as 027, etc., as this will
# keep the files in order when we list the directory.

# Usage: ./fileNumberGaps.py close <folder> <prefix> <suffix> - closes gaps
#        ./fileNumberGaps.py open <folder> <prefix> <suffix> <start> <size>
#            - creates gap of "size" at "start" index

import sys, os, shutil, re

#################
# "close" case:
#################
if len(sys.argv) == 5:
    folder, prefix, suffix = sys.argv[2:5]
    fileNames = [fileName for fileName in os.listdir(folder) \
             if fileName.startswith(prefix) and fileName.endswith(suffix)]
    # regex to find the number of each file:
    numberPattern = prefix + "(.*?)" + suffix
    # sort the file names by their numberings:
    fileNames.sort(key = lambda fileName: int(re.search(numberPattern, fileName).group(1)))
    # find largest number, so we can pad the smaller numbers with 0s if need be
    numDigits = len(str(len(fileNames)))
    
    # get new file names:
    newFileNames = []
    for i in range(len(fileNames)):
        oldNumberString = re.search(numberPattern, fileNames[i]).group(1)
        newNumberString = str(i+1)
        while len(newNumberString) < numDigits:
            newNumberString = '0' + newNumberString
        newFileNames.append(re.sub(oldNumberString, newNumberString, fileNames[i]))
    
    # change file names to new file names:
    for i in range(len(fileNames)):
        filePath = os.path.join(folder, fileNames[i])
        newFilePath = os.path.join(folder, newFileNames[i])
        shutil.move(filePath, newFilePath)
   
###############
# "open" case:
###############
elif len(sys.argv) == 7:
    folder, prefix, suffix = sys.argv[2:5]
    start, size = map(int, sys.argv[5:7]) 
    fileNames = [fileName for fileName in os.listdir(folder) \
             if fileName.startswith(prefix) and fileName.endswith(suffix)]
    # regex to find the number of each file:
    numberPattern = prefix + "(.*?)" + suffix
    # sort the file names by their numberings:
    fileNames.sort(key = lambda fileName: int(re.search(numberPattern, fileName).group(1)))
    # find largest number, so we can pad the smaller numbers with 0s if need be
    numDigits = len(str(len(fileNames) + size))

    # get new file names:
    newFileNames = []
    for i in range(len(fileNames)):
        oldNumberString = re.search(numberPattern, fileNames[i]).group(1)
        newNumberString = str(i+1) if i < start else str(i+1 + size)
        while len(newNumberString) < numDigits:
            newNumberString = '0' + newNumberString
        newFileNames.append(re.sub(oldNumberString, newNumberString, \
                            fileNames[i]))
   
    # change file names to new file names:
    for i in range(len(fileNames)):
        filePath = os.path.join(folder, fileNames[i])
        newFilePath = os.path.join(folder, newFileNames[i])
        shutil.move(filePath, newFilePath)
    