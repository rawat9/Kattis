n = int(input())

result = ""

for _ in range(n):
    r, e, c = list(map(int, input().split()))
    if (e - c) > r: 
        result = "advertise"
    elif (e - c) == r:
        result = "does not matter"
    else:
        result = "do not advertise"

    print(result)
