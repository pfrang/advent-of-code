import string
import numpy as np
f = open("input.txt", 'r')

d = f.read().splitlines()

alphabet_lower = list(string.ascii_lowercase)
alphabet_higher = list(string.ascii_uppercase)
alphabet = np.concatenate((alphabet_lower, alphabet_higher)).tolist()

sum = 0

for i in d:
    length = len(i)
    halfSentence = int(length / 2)
    firstHalf = list(i[0:halfSentence])
    secondHalf = list(i[halfSentence::])
    duplicateValueSet = set(firstHalf).intersection(secondHalf)
    duplicateValue = list(duplicateValueSet)[0]
    points = int(alphabet.index(str(duplicateValue))) + 1
    sum += points

print(sum)
