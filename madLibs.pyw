#! /Library/Frameworks/Python.framework/Versions/3.12/bin/python3

# madLibs.pyw - reads in text files and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears. The results
# are printed to the screen and saved to a new text file

# Usage: ./mcb.pyw <source file> <dest file>

import sys, re

if len(sys.argv) != 3:
    sys.exit()

sourceFile = open(sys.argv[1])
destFile = open(sys.argv[2], 'w')

sourceText = sourceFile.read()

# pos: parts of speech
posRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

wordsToReplace = posRegex.findall(sourceText)
for word in wordsToReplace:
    if word == 'ADJECTIVE' or word == 'ADVERB':
        print('Enter an ' + word.lower() + ':')
    else:
        print('Enter a ' + word.lower() + ':')
    replacement = input()
    sourceText = re.sub(word, replacement, sourceText, count=1)

print(sourceText)
destFile.write(sourceText)

sourceFile.close()
destFile.close()