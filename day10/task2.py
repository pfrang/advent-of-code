import re
import json
import numpy
f = open('input.txt', 'r')
content = f.readlines()

score = 1
cycle = 0
sprite_position = 1
my_dict = {}

def checkforCycle():
    global sprite_position
    if(cycle == 40):
        sprite_position = 1
        print("\n")
    elif(cycle == 80):
        sprite_position = 1
        print("\n")
    elif(cycle == 120):
        sprite_position = 1
        print("\n")
    elif(cycle == 160):
        sprite_position = 1
        print("\n")
    elif(cycle == 200):
        sprite_position = 1
        print("\n")
    elif(cycle == 240):
        sprite_position = 1
        print("\n")
    if(sprite_position in [score, score +1, score+2]):
        print("#", end="")
    else:
        print(".",end="")

for row in content:
    row = row.replace('\n','')
    if("addx" in row):
        nr = int(row.split(" ")[1])
        cycle += 1
        sprite_position += 1
        checkforCycle()
        cycle += 1
        sprite_position += 1
        checkforCycle()
        score += nr
    elif("noop" in row):
        cycle += 1
        sprite_position += 1
        checkforCycle()
