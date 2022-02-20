n = int(input())

for _ in range(n):
    k, *outlets = list(map(int, input().split()))
    print(sum(outlets) - (len(outlets) - 1))
