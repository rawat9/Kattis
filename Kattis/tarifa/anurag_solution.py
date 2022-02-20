x = int(input())
n = int(input())

avail = 0

for _ in range(n):
    p = int(input())

    avail += (x - p)

print(avail + x)
