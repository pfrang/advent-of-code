import re
import json
import string
import pandas as pd

f = open('input.txt', 'r')
content = f.readlines()

alphabet_lower = list(string.ascii_lowercase)
alphabet_higher = list(string.ascii_uppercase)

steps = 0
starting_position = 0
end_position = 0
for rowIndex,row in enumerate(content):
    row = row.replace('\n', '')
    for colIndex,value in enumerate(row):
        if value  == "S":
            starting_position = [rowIndex, colIndex]
        elif value == "E":
            end_position = [rowIndex, colIndex]

current_position = starting_position

print(content[1,1])

df = pd.DataFrame(f)

while current_position != end_position:
    right_position = [starting_position[0], starting_position[1] + 1]
    left_position = [starting_position[0], starting_position[1] - 1]
    up_position = [starting_position[0] - 1, starting_position[1]]
    down_position = [starting_position[0] + 1, starting_position[1]]
    possible_positions = [right_position, left_position, up_position, down_position]
    viable_positions = []
    current_value = content[current_position]
    curr_index = alphabet_lower.index()
    for i in possible_positions:
        for rowIndex,row in enumerate(content):
            row = row.replace('\n', '')
            for colIndex,value in enumerate(row):
                if value  == "S":
                    starting_position = [rowIndex, colIndex]
                elif value == "E":
                    end_position = [rowIndex, colIndex]
