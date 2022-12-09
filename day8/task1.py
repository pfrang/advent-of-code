import re
import json
import sys

f = open('input.txt', 'r')
content = f.readlines()

columns = {}

def populateColumn(row):
    for colIndex,i in enumerate(row):
        if(colIndex in columns):
            columns[colIndex].append(i)
        else:
            columns[colIndex] = [i]

for rowIndex,row in enumerate(content):
    row = row.replace('\n','')
    populateColumn(row)



def checkForVisibleInRow(rowIndex,row):
    treesVisible = 0
    for colIndex,i in enumerate(row):
        if(colIndex == 0 or colIndex == len(row) - 1 or rowIndex == 0 or rowIndex == len(content) - 1):
            treesVisible += 1
            continue
        value = i
        treesBlockingLeftCheck = 0
        treesBlockingRightCheck = 0
        treesBlockingNorthCheck = 0
        treesBlockingSouthCheck = 0
        for ji, j in enumerate(row[:colIndex]):
            if(j >= i):
                treesBlockingLeftCheck += 1
        for ki, k in enumerate(row[colIndex + 1:]):
            if(k >= i):
                treesBlockingRightCheck += 1
        for hi, h in enumerate(columns[colIndex][:rowIndex]):
            if(h >= i):
                treesBlockingNorthCheck += 1
        for ni, n in enumerate(columns[colIndex][rowIndex + 1:]):
            if(n >= i):
                treesBlockingSouthCheck += 1
        if(treesBlockingLeftCheck == 0 or treesBlockingSouthCheck == 0 or treesBlockingNorthCheck == 0 or treesBlockingRightCheck == 0):
            treesVisible += 1

    return treesVisible

score = 0

for index,row in enumerate(content):
    row = row.replace('\n','')
    score += checkForVisibleInRow(index,row)

# print(json.dumps(columns, indent=4))
print(score)
