n = int(input())
temperature = list(map(int, input().split()))

print(len(list(filter(lambda x: x < 0, temperature))))
