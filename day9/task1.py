import numpy
import re
import json
import sys

f = open('input.txt', 'r')
content = f.readlines()

d = numpy.zeros((1000,1000))

H_initial_pos = [50, 50]
T_initial_pos = [50, 50]

d[T_initial_pos[0]][T_initial_pos[1]] = 1


H_pos = H_initial_pos
T_pos = T_initial_pos

for row in content:
    row = row.replace('\n', '')
    direction = row.split(" ")[0]
    nr = int(row.split(" ")[1])
    for i in range(0, nr):

        if(direction == "R"):
                H_pos[1] += 1
        elif(direction == "L"):
                H_pos[1] -= 1
        elif(direction == "U"):
                H_pos[0] -= 1
        elif(direction == "D"):
                H_pos[0] += 1

        #diagonal check D R
        if(H_pos[0] - T_pos[0] > 1 and H_pos[1] - T_pos[1] > 0):
            T_pos[1] = T_pos[1] + 1
            T_pos[0] = T_pos[0] + 1
        elif(H_pos[0] - T_pos[0] > 0 and H_pos[1] - T_pos[1] > 1):
            T_pos[1] = T_pos[1] + 1
            T_pos[0] = T_pos[0] + 1
        #diagonal check U R
        elif(H_pos[0] - T_pos[0] < -1 and H_pos[1] - T_pos[1] > 0):
            T_pos[1] = T_pos[1] + 1
            T_pos[0] = T_pos[0] - 1
        elif(H_pos[0] - T_pos[0] < 0 and H_pos[1] - T_pos[1] > 1):
            T_pos[1] = T_pos[1] + 1
            T_pos[0] = T_pos[0] - 1
        #diagonal check D L
        elif(H_pos[0] - T_pos[0] > 1 and H_pos[1] - T_pos[1] < 0):
            T_pos[1] = T_pos[1] - 1
            T_pos[0] = T_pos[0] + 1
        elif(H_pos[0] - T_pos[0] > 0 and H_pos[1] - T_pos[1] < -1):
            T_pos[1] = T_pos[1] - 1
            T_pos[0] = T_pos[0] + 1
        #diagonal check U L
        elif(H_pos[0] - T_pos[0] < -1 and H_pos[1] - T_pos[1] < 0):
            T_pos[1] = T_pos[1] - 1
            T_pos[0] = T_pos[0] - 1
        elif(H_pos[0] - T_pos[0] < 0 and H_pos[1] - T_pos[1] < -1):
            T_pos[1] = T_pos[1] - 1
            T_pos[0] = T_pos[0] - 1
        #horizontal check
        elif(H_pos[0] - T_pos[0] > 1):
            T_pos[0] = T_pos[0] + 1
        elif(H_pos[0] - T_pos[0] < -1):
            T_pos[0] = T_pos[0] - 1
        #vertical check
        elif(H_pos[1] - T_pos[1] > 1):
            T_pos[1] = T_pos[1] + 1
        elif(H_pos[1] - T_pos[1] < -1):
            T_pos[1] = T_pos[1] - 1
        d[T_pos[0]][T_pos[1]] = 1

print(list(d.flatten()).count(1))
