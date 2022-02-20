n = int(input())

for _ in range(n):
    a, b, c = list(map(int, input().split()))

    if (a + b == c) or (a * b == c) or (abs(a - b) == c) or (b / a) == float(c) or (a / b) == float(c):
        print('Possible')
    else:
        print('Impossible')
