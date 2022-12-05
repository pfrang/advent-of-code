
f = open('input.txt', 'r')
content = f.readlines()

outcomes = {
    "['A X']": 4,
    "['A Z']": 3,
    "['A Y']": 8,
    "['B X']": 1,
    "['B Z']": 9,
    "['B Y']": 5,
    "['C X']": 7,
    "['C Z']": 6,
    "['C Y']": 2,
}

outComeTask2 = {
    "['A X']": 3,
    "['A Z']": 8,
    "['A Y']": 4,
    "['B X']": 1,
    "['B Z']": 9,
    "['B Y']": 5,
    "['C X']": 2,
    "['C Z']": 7,
    "['C Y']": 6,
}

score = 0

for i in content:
    k = i.splitlines()
    score += outComeTask2[str(k)]

print(score)

# a = "Rock"
# b = "Paper"
# c = "Scissors"

# x = "rock" : 1
# y = "paper" : 2
# z = "scissors": 3
