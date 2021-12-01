name = input()

ans = ""
prev = ""
for letter in name:
	if letter != prev:
		ans += letter
	prev = letter

print(ans)

