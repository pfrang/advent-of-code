import string
import numpy as np
from itertools import islice
f = open("input.txt", 'r')

d = f.read().splitlines()

alphabet_lower = list(string.ascii_lowercase)
alphabet_higher = list(string.ascii_uppercase)
alphabet = np.concatenate((alphabet_lower, alphabet_higher)).tolist()

sum = 0

lines = []
index = 1

firstLine = []
secondLine = []
thirdLine = []

def findDUplicates(arr1, arr2, arr3):
    duplicateValue = 0
    for i in arr1:
        if i in arr2 and i in arr3:
            # print(f'{i} exists')
            duplicateValue = i
            break
    for i in arr2:
        if i in arr1 and i in arr3:
            # print(f'{i} exists')
            duplicateValue = i
            break
    for i in arr3:
        if i in arr1 and i in arr2:
            # print(f'{i} exists')
            duplicateValue = i
            break
    return duplicateValue


for i in d:
    if(index == 1):
        firstLine = i
        index += 1
        continue
    if(index == 2):
        secondLine = i
        index += 1
        continue
    if index == 3:
        thirdLine = i
        duplicateValue = findDUplicates(firstLine, secondLine, thirdLine)
        print(np.concatenate((list(firstLine), list(secondLine), list(thirdLine))).tolist())
        print(duplicateValue)
        points = int(alphabet.index(str(duplicateValue))) + 1
        sum += points
        index = 1
        lines = []
        firstLine = []
        secondLine = []
        thirdLine = []
        index = 1
        continue

print(sum)
