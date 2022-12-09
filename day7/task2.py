import json
import re

f = open('input.txt', 'r')
content = f.readlines()

d = {}
level = 0
currentFolder = ""
nr = 0
currentPath = []
joinString = ""
for index,row in enumerate(content):
    row = row.replace('\n','')
    if(row.split(" ")[1] == "ls" or row.split(" ")[0] == "dir"):
        continue
    if("cd .." in row):
        level -= 1
        currentPath = currentPath[: -1]
    elif(re.search(r'cd .+', row)):
        level += 1
        currentFolder = row.split(" ")[len(row.split(" ")) - 1]
        currentPath.append(currentFolder)
        joinString = '/'.join(currentPath)
        if(joinString not in d):
            d[joinString] = 0
    else:
        # nr = int(re.findall('\d+', row)[0])
        nr = int(row.split(" ")[0])
        d[joinString] += nr
        for index2,i in enumerate(currentPath[:-1]):
            partialString = '/'.join(currentPath[:-index2 - 1])
            d[partialString] += nr




# print(json.dumps(d,indent=4))



outerMostDirectorySpace = d['/']
neededSpace = outerMostDirectorySpace - 40000000
validNums = []

print(neededSpace)

for key,value in d.items():
    if(value > neededSpace):
        validNums.append(value)

print(sorted(validNums))
