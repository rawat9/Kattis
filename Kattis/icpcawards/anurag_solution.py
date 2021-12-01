from itertools import islice

n = int(input())
winners = {}

for i in range(n):
    university, team = input().split()
    if university in winners:
        continue
    winners[university] = team 

for winner, team in islice(winners.items(), 12):
    print(winner, team)