#! /Library/Frameworks/Python.framework/Versions/3.12/bin/python3
# printTable.py - takes a list of lists of strings and prints it
# in a well-organized table with each column right-justified

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    numCols = len(data)
    numRows = len(data[0])

    colWidths = [0] * numCols  
    for i in range(numCols):
        for j in range(numRows):
            strLength = len(data[i][j])
            if strLength > colWidths[i]:
                colWidths[i] = strLength

    formattedRows = [''] * numRows
    for j in range(numRows):
        for i in range(numCols):
            formattedRows[j] += data[i][j].rjust(colWidths[i]+1)
        print(formattedRows[j])

printTable(tableData)
        
    

