#! python3

# spreadSheetToTextFiles.py - does the reverse of textFilesToSpreadSheet.py.
# That is, it takes a spreadsheet and writes each column to a text file, one line
# per cell in the column. It takes a directory to store the textfiles in as a
# second (optional) argument
# Usage: ./spreadSheetToTextFiles.py <spreadsheetFile.xlsx> <dirName>

import sys, openpyxl, os

# Get spreadsheet (input) and directory to store text files (output) in:
spreadSheetFileName = sys.argv[1]
wb = openpyxl.load_workbook(spreadSheetFileName)
ws = wb.active

dirName = sys.argv[2] if len(sys.argv) > 2  else 'textFilesFromSpreadSheet'
if not os.path.exists(dirName):
    os.mkdir(dirName)

# write spreadsheet to text files
for colIndex in range(1, ws.max_column + 1):
    textFileName = os.path.join(dirName, 'textFile' + str(colIndex) + '.txt')
    textFile = open(textFileName, 'w')
    text = ''
    for rowIndex in range(1, ws.max_row + 1):
        line = ws.cell(row = rowIndex, column = colIndex).value
        if not line is None:
            text += line + '\n'
    textFile.write(text)
    textFile.close()
