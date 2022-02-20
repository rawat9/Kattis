reverse = lambda x: x[::-1]
n, m = list(map(reverse, input().split()))
print(n if n > m else m)
