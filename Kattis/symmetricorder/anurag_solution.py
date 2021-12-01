n = 1

while True:
	names_count = int(input())
	
	if names_count == 0: break

	names = []
	for _ in range(names_count):
		name = input()
		names.append(name)

	print('SET', n)

	names = names[::2] + names[1::2][::-1]

	for name in names:
		print(name)

	n += 1
