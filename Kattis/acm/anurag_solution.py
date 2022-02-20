from itertools import groupby

hashmap = {}
score = 0
temp = []
while True:
    sets = input()
    if sets == "-1":
        break

    minutes, problem, result = sets.split()
    temp.append(problem + "-" + result)

    if result == "right":
        hashmap[problem] = int(minutes)

temp.sort(key=lambda x: x[0])
items = [list(g) for _, g in groupby(temp, lambda x: x[0])]
correct_answers = list(filter(lambda x: x[-1][-5:] == "right", items))

for answer in correct_answers:
    score += (len(answer) - 1) * 20

print(len(correct_answers), score + sum(hashmap.values()))
