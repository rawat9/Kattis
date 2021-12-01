friend_score = int(input())
friend_answers = input()
my_answers = input()
total = len(my_answers)

match = sum(i == j for i, j in zip(friend_answers, my_answers))

print(friend_score + (total - match) if match >= friend_score else match + (total - friend_score))

