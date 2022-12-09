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
    best_scenic_score_at_row = 0
    for colIndex,i in enumerate(row):
        if(colIndex == 0 or colIndex == len(row) - 1 or rowIndex == 0 or rowIndex == len(content) - 1):
            continue
        value = i
        scenic_scoreLeft = 0
        scenic_scoreRight = 0
        scenic_scoreNorth = 0
        scenic_scoreSouth = 0
        for ji, j in enumerate(row[:colIndex]):
            if(j >= i):
                scenic_scoreLeft = colIndex - ji
            if(scenic_scoreLeft == 0):
                scenic_scoreLeft = len(row[:colIndex])
        for ki, k in enumerate(row[colIndex + 1:]):
            if(k >= i):
                scenic_scoreRight = ki + 1
                break
            if(scenic_scoreRight == 0):
                scenic_scoreRight = len(row[colIndex + 1:])
        for hi, h in enumerate(columns[colIndex][:rowIndex]):
            if(h >= i):
                scenic_scoreNorth = rowIndex - hi
            if(scenic_scoreNorth == 0):
                scenic_scoreNorth = len(columns[colIndex][:rowIndex])
        for ni, n in enumerate(columns[colIndex][rowIndex + 1:]):
            if(n >= i):
                scenic_scoreSouth = ni + 1
                break
            if(scenic_scoreSouth == 0):
                scenic_scoreSouth = len(columns[colIndex][rowIndex + 1:])
        scenic_score = scenic_scoreLeft * scenic_scoreRight * scenic_scoreNorth * scenic_scoreSouth
        # print(scenic_scoreLeft, scenic_scoreRight, scenic_scoreNorth, scenic_scoreSouth)
        # print(scenic_score)
        # sys.exit(0)
        if(scenic_score > best_scenic_score_at_row):
            best_scenic_score_at_row = scenic_score

    return best_scenic_score_at_row

score = 0

for index,row in enumerate(content):
    row = row.replace('\n','')
    scenic_score = checkForVisibleInRow(index,row)
    if(scenic_score > score ):
        score = scenic_score

# print(json.dumps(columns, indent=4))
print(score)
