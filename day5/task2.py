import re
import json
f = open('input.txt', 'r')
content = f.readlines()

starting_arr = [' 1   2   3   4   5   6   7   8   9']

startingPoint = {}

def stripKeys(input):
    h = input
    nrs = re.findall(r'\d+', h)
    for i in nrs:
        startingPoint[i] = []

def stripValues(input):
    for rowIndex,i in enumerate(input):
        columns = i.replace('    ',' ').replace('\n','').split(' ')
        for colIndex, i in enumerate(columns):
            if(i != ""):
                startingPoint[str(colIndex + 1)].append(i)

def populateStartingKeys(input):
    keys = input[len(input) - 1]
    stripKeys(keys)
    values = input[0: len(input) - 1]
    stripValues(values)

def shuffleBoxes(row):
    nrs = re.findall('\d+', row)
    amount = int(nrs[0])
    fromnr = str(nrs[1])
    tonr = str(nrs[2])
    itemsToRemove = startingPoint[fromnr][0:amount]
    startingPoint[fromnr] = startingPoint[fromnr][amount::]
    startingPoint[tonr] = itemsToRemove + startingPoint[tonr]


startTask = False
for index,i in enumerate(content):
    if(i.splitlines() == starting_arr):
        populateStartingKeys(content[0:index + 1])
    if(startTask == True):
        shuffleBoxes(i)
    if(i.splitlines() == ['']):
        startTask = True
