import re
import json
import sys

f = open('input.txt', 'r')
content = f.readlines()

score = 1
cycle = 0
sprite_position = 0
my_dict = {}

def checkforCycle():
    global sprite_position
    if(cycle == 41):
        sprite_position = 1
        print("\n")
    elif(cycle == 81):
        sprite_position = 1
        print("\n")
    elif(cycle == 121):
        sprite_position = 1
        print("\n")
    elif(cycle == 161):
        sprite_position = 1
        print("\n")
    elif(cycle == 201):
        sprite_position = 1
        print("\n")
    elif(cycle == 241):
        sprite_position = 1
        print("\n")
    if(sprite_position in [score, score +1, score+2]):
        print("#", end="")
    else:
        print(".",end="")


for index,row in enumerate(content):
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
