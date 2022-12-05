import string
import numpy as np
f = open("input.txt", 'r')

d = f.read().splitlines()


def getRange(rng):
    nums = rng.split("-")
    num1 = int(nums[0])
    num2 = int(nums[1])
    return range(num1, num2 + 1)

def getNums(nums):
    splitNums = nums.split("-")
    return [int(splitNums[0]), int(splitNums[1])]

def checkIfNumExistInRange(firstElf, secondElf):
    rng1 = getRange(firstElf)
    rng2 = getRange(secondElf)
    for i in rng1:
        if(i in rng2):
            print(f'{i} exists in {rng2} 1')
            return 1
    for i in rng2:
        if(i in rng1):
            print(f'{i} exists in {rng1} 2')
            return 1
    return 0



sum = 0

for i in d:
    line = i.split(",")
    firstElf = line[0]
    secondElf = line[1]
    exists = checkIfNumExistInRange(firstElf, secondElf)
    sum += exists
print(sum)
