# Difficulty: 1.4

from math import sqrt

n = int(input())

for _ in range(n):
	message = input()

	m = int(sqrt(len(message)))

	matrix = []	

	for i in range(0, len(message), m):
		row = list(message[i:i+m])
		matrix.append(row)

	result = list(zip(*matrix))
	answer = ""
	
	for col in reversed(result):
		answer += ("".join(col))

	print(answer)
