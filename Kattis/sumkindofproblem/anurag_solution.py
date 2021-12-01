p = int(input())

for _ in range(p):
	k, n = list(map(int, input().split()))
	print(k, (n * (n+1))//2, n**2, n*(n+1))
