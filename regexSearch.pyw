#! /Library/Frameworks/Python.framework/Versions/3.12/bin/python3

# regexSearch.py - opens all .txt files in a user-supplied folder and 
# searches for any line that contains a match of a user-supplied 
# regular expression. The results are then printed to the screen.

import sys, os, re

# ANSI escape codes to highlight regex matches found when outputing strings
GREEN_HIGHLIGHT = '\033[32m'
RED_HIGHLIGHT = '\033[31m'
BLUE_HIGHTLIGHT = '\033[34m'
MAGENTA_HIGHLIGHT = '\033[35m'
CYAN_HIGHLIGHT = '\033[36m'
END_HIGHLIGHT = '\033[0m'  # Reset to default
def highlightMatch(match):
    return f"{GREEN_HIGHLIGHT}{match.group(0)}{END_HIGHLIGHT}"

# listTextFilePaths does a deep search for all the .txt files in a directory
# and returns a list of their paths
def listTextFilePaths(directory):
    textFilePaths = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith('.txt'):
                textFilePaths.append(os.path.join(root, name))
    return textFilePaths

# Ask for user input:
print('This program opens all .txt files in a given folder and searches them for a given regular expression.')
print('Enter folder to search through:')
folderPath = input()
textFilePaths = listTextFilePaths(folderPath)
print('Enter regular expression to search for:')
regexString = input()
regex = re.compile(regexString)

# list of dictionaries containing the text file path, the number of matches
# found in that text file, and the lines containing the matches
allFileMatches = []

totalNumMatches = 0

# Get matches:
for textFilePath in textFilePaths:
    matchDict = { 'filePath': textFilePath, 'numMatches': 0, 'matchedLines': []}
    file = open(textFilePath)
    lines = file.readlines()
    for i in range(0, len(lines)):
        matches = regex.findall(lines[i])
        if len(matches) > 0:
            matchDict['matchedLines'].append({ \
            'lineNumber': i, \
            'numMatchesInLine': 0, \
            'line': lines[i] })
        for match in matches:
            matchDict['matchedLines'][-1]['numMatchesInLine'] += 1
            matchDict['numMatches'] += 1
            totalNumMatches += 1
            matchDict['matchedLines'][-1]['line'] = \
                re.sub(regexString, highlightMatch, \
                matchDict['matchedLines'][-1]['line'])

    allFileMatches.append(matchDict)

# Print output:
print('\n')
print(BLUE_HIGHTLIGHT + 'Total matches: ' + str(totalNumMatches) + END_HIGHLIGHT)
print('\n')
for fileMatch in allFileMatches:
    if fileMatch['numMatches'] > 0:
        print(RED_HIGHLIGHT + fileMatch['filePath'] + END_HIGHLIGHT)
        print( BLUE_HIGHTLIGHT + 'Matches:' + str(fileMatch['numMatches']) + END_HIGHLIGHT)
        for line in fileMatch['matchedLines']:
            print('\t' + RED_HIGHLIGHT + 'Line number: ' + str(line['lineNumber']) + END_HIGHLIGHT + BLUE_HIGHTLIGHT + ' Matches: ' + str(line['numMatchesInLine']) + END_HIGHLIGHT)
            print('\t' + line['line'] + '\n')




