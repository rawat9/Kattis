n = int(input())

for _ in range(n):
	instructions = input().split()

	if instructions[0] == 'Simon' and instructions[1] == 'says':
		print(" " + " ".join(instructions[2:]))
