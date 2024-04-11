#! python3

# textFilesToSpreadsheet.py - takes multiple text files as input and writes them
# to spreadsheet as output, one column per text file, one row per line.
# Usage: ./textFilesToSpreadsheet.py <spreadsheet.xlsx> <textfile1.txt> <textfile2.txt> ...
#   or ./textFilesToSpreadsheet.py <textfile1.txt> <textfile2.txt> ...

import sys, openpyxl

excelFileSupplied = sys.argv[1].endswith('.xlsx')

outputFileName =  sys.argv[1] if excelFileSupplied  else 'textFileOutput.xlsx'
textFileNames = sys.argv[2:] if excelFileSupplied else sys.argv[1:]

wb = openpyxl.Workbook()
ws = wb.active

# write text files to spreadsheet
for i in range(len(textFileNames)):
    file = open(textFileNames[i], 'r')
    lines = file.readlines()
    for j in range(len(lines)):
        ws.cell(row = j + 1, column = i + 1).value = lines[j]

wb.save(outputFileName)