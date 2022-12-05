import string
import numpy as np
f = open("input.txt", 'r')

d = f.read().splitlines()

# def isNumberWithinRange(num, range):

def getRange(rng):
    nums = rng.split("-")
    num1 = int(nums[0])
    num2 = int(nums[1])
    return range(num1, num2 + 1)

def getNums(nums):
    splitNums = nums.split("-")
    return [int(splitNums[0]), int(splitNums[1])]

def checkIfNumExistInRange(firstElf, secondElf):
    nums1 = getNums(firstElf)
    rng1 = getRange(secondElf)
    nums2 = getNums(secondElf)
    rng2 = getRange(firstElf)
    if nums1[0] in rng1 and nums1[1] in rng1:
        print(f'{nums1[0]} - {nums1[1]} is fully contained in {rng1} 1')
        return 1
    elif nums2[0] in rng2 and nums2[1] in rng2:
        print(f'{nums2[0]} - {nums2[1]} is fully contained in {rng2} 2 ')
        return 1
    else:
        return 0


sum = 0

for i in d:
    line = i.split(",")
    firstElf = line[0]
    secondElf = line[1]
    exists = checkIfNumExistInRange(firstElf, secondElf)
    sum += exists

print(sum)
