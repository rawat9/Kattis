from itertools import combinations, repeat

cards = list(map(int, input().split()))

lst = []
for i in range(1, 11):
    lst += list(repeat(i, cards[i-1]))

k = int(input())

combs = list(combinations(lst, k))
strict = lambda x: all(i < j for i, j in zip(x, x[1:]))
print(len(list(filter(strict, combs))))
