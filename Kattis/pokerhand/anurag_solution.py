from collections import Counter

cards = input().split()


counter = Counter([ card[0] for card in cards ])
print(max(counter.values()))
