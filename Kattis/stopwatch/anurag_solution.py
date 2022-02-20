n = int(input())

seconds = []
display = 0

for _ in range(n):
    time = int(input())
    seconds.append(time)

for i in range(1, len(seconds), 2):
    display += seconds[i] - seconds[i-1]

print("still running" if n % 2 != 0 else display)

