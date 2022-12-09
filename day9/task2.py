import numpy
import re
import json
import sys

f = open('input.txt', 'r')
content = f.readlines()

d = numpy.zeros((1000,1000))

T_initial_pos = [50, 50]
HEAD_POS = [50, 50]

d[T_initial_pos[0]][T_initial_pos[1]] = 1



dict = {
    "T_1_pos": [50, 50],
    "T_2_pos": [50, 50],
    "T_3_pos" : [50, 50],
    "T_4_pos" : [50, 50],
    "T_5_pos" : [50, 50],
    "T_6_pos" : [50, 50],
    "T_7_pos" : [50, 50],
    "T_8_pos" : [50, 50],
    "T_9_pos" : [50, 50]
}



def adjustKnots(base, tail):
    if(base[0] - tail[0] > 1 and base[1] - tail[1] > 0):
        tail[1] = tail[1] + 1
        tail[0] = tail[0] + 1
    elif(base[0] - tail[0] > 0 and base[1] - tail[1] > 1):
        tail[1] = tail[1] + 1
        tail[0] = tail[0] + 1
    #diagonal check U R
    elif(base[0] - tail[0] < -1 and base[1] - tail[1] > 0):
        tail[1] = tail[1] + 1
        tail[0] = tail[0] - 1
    elif(base[0] - tail[0] < 0 and base[1] - tail[1] > 1):
        tail[1] = tail[1] + 1
        tail[0] = tail[0] - 1
    #diagonal check D L
    elif(base[0] - tail[0] > 1 and base[1] - tail[1] < 0):
        tail[1] = tail[1] - 1
        tail[0] = tail[0] + 1
    elif(base[0] - tail[0] > 0 and base[1] - tail[1] < -1):
        tail[1] = tail[1] - 1
        tail[0] = tail[0] + 1
    #diagonal check U L
    elif(base[0] - tail[0] < -1 and base[1] - tail[1] < 0):
        tail[1] = tail[1] - 1
        tail[0] = tail[0] - 1
    elif(base[0] - tail[0] < 0 and base[1] - tail[1] < -1):
        tail[1] = tail[1] - 1
        tail[0] = tail[0] - 1
    #horizontal check
    elif(base[0] - tail[0] > 1):
        tail[0] = tail[0] + 1
    elif(base[0] - tail[0] < -1):
        tail[0] = tail[0] - 1
    #vertical check
    elif(base[1] - tail[1] > 1):
        tail[1] = tail[1] + 1
    elif(base[1] - tail[1] < -1):
        tail[1] = tail[1] - 1


keys = list(dict.keys())

for row in content:
    row = row.replace('\n', '')
    direction = row.split(" ")[0]
    nr = int(row.split(" ")[1])
    for i in range(0, nr):
        if(direction == "R"):
                HEAD_POS[1] += 1
        elif(direction == "L"):
                HEAD_POS[1] -= 1
        elif(direction == "U"):
                HEAD_POS[0] -= 1
        elif(direction == "D"):
                HEAD_POS[0] += 1
        adjustKnots(HEAD_POS, dict["T_1_pos"])
        for index,key in enumerate(dict):
            if(key == 'T_9_pos'):
                continue
            else:
                key1 = keys[index]
                key2 = keys[index + 1]
                adjustKnots(dict[key1], dict[key2])
        value1 = dict["T_9_pos"][0]
        value2 = dict["T_9_pos"][1]
        d[value1, value2] = 1

print(list(d.flatten()).count(1))
