import sys

for line in sys.stdin:
    a, b = list(map(int, line.split()))
    if a > b:
        print(a - b)
    else:
        print(b - a)
