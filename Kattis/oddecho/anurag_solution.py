n = int(input())

words = []

for _ in range(n):
	word = input()
	words.append(word)

for i in range(0, len(words), 2):
	print(words[i])
