#! python3

# csvToExcel.py - reads all the csv files in the cwd and outputs
# them as Excel files

import openpyxl, csv, os

# Loop over every csv file in the cwd
for csvFileName in os.listdir('.'):
    if not csvFileName.endswith('.csv'):
        continue
    print('writing ' + csvFileName)
    # Open the reader for the csv file
    csvFile = open(csvFileName)
    reader = csv.reader(csvFile)
    # make the excel file
    excelFileName = os.path.splitext(csvFileName)[0] + '.xlsx'
    wb = openpyxl.Workbook()
    ws = wb.active
    # write csv rows to spreadsheet
    rowIndex = 1
    for row in reader:
        colIndex = 1
        for data in row:
            ws.cell(row=rowIndex, column=colIndex).value = data
            colIndex += 1
        rowIndex += 1
    
    # save excel file
    wb.save(excelFileName)