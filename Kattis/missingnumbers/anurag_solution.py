n = int(input())

numbers = []

for _ in range(n):
	number = int(input())
	numbers.append(number)

missing = sorted(set(range(1, max(numbers))) - set(numbers))

if len(missing) > 0:
	print(*missing, sep='\n')
else:
	print('good job')
