n = int(input())

numbers = []

for _ in range(n):
	number = int(input())
	numbers.append(number)

print(*reversed(numbers), sep='\n')
