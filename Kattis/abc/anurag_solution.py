integers = sorted(map(int, input().split()))
order = input()

result = []
for letter in order:
    if letter == "A":
        result.append(integers[0])
    elif letter == "B":
        result.append(integers[1])
    elif letter == "C":
        result.append(integers[-1])

print(*result)
