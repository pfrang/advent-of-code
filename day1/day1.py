f = open('input.txt', 'r')
content = f.readlines()


a = {"person 1": []}
index = 1
for i in content:
    if(i.splitlines() == ['']):
        index += 1
        a[f'person {index}'] = []
    else:
        a[f'person {index}'].append(int(i.splitlines()[0]))

for i in a:
    a[i] = sum(a[i])

sortDict = sorted(a.items(), key=lambda kv: kv[1])

print(sortDict)
