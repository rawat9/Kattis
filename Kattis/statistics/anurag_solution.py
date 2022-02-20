import sys

i = 1
for line in sys.stdin:
    n, *data = list(map(int, line.split()))
    print(f'Case {i}:', min(data), max(data), max(data) - min(data))
    i += 1
