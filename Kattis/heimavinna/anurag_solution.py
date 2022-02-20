problems = input().split(";")

count = 0
for problem in problems:
    if "-" in problem:
        upper = problem.split("-")[1]
        lower = problem.split("-")[0]
        count += int(upper) - int(lower) + 1
    else:
        count += 1

print(count)
