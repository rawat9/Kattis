n = int(input())

from string import ascii_lowercase as alphabet

for _ in range(n):
	phrase = input().lower()
		
	res = ""
	for char in alphabet:
		if char not in phrase:
			res += char	

	print('pangram' if res == '' else 'missing', res)
