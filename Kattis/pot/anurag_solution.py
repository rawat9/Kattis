n = int(input())
total = 0 

for _ in range(n):
	num = int(input())
	last_digit = num % 10
	total += (int(str(num)[:-1]) ** last_digit)

print(total)


# Time Complexity: O(n)
# Space Complexity: O(1)