import re
import json
import numpy
f = open('input.txt', 'r')
content = f.readlines()

f2 = open('input2.txt', 'r')

score = 1
cycle = 0
my_dict = {}


d = numpy.zeros((5,40))

print(d)

def checkforCycle():
    if(cycle == 20):
        print(score)
        my_dict[20] = score * 20
    elif(cycle == 60):
        print(score)
        my_dict[60] = score * 60
    elif(cycle == 100):
        print(score)
        my_dict[100] = score * 100
    elif(cycle == 140):
        print(score)
        my_dict[140] = score * 140
    elif(cycle == 180):
        print(score)
        my_dict[180] = score * 180
    elif(cycle == 220):
        print(score)
        my_dict[220] = score * 220

for row in content:
    row = row.replace('\n','')
    if("addx" in row):
        nr = int(row.split(" ")[1])
        cycle += 1
        checkforCycle()
        cycle += 1
        checkforCycle()
        score += nr
    elif("noop" in row):
        cycle += 1
        checkforCycle()



sum = 0
for key,value in my_dict.items():
    sum += value

print(my_dict)
print(sum)
