n = int(input())

for _ in range(n):
	pair1 = input()
	pair2 = input()

	answer = ""

	for i, j in zip(pair1, pair2):
		if i != j:
			answer += "*"
		else:
			answer += "."

	print(pair1)
	print(pair2)
	print(answer)
	print()

