n, k = list(map(int, input().split()))

overall = 0
for _ in range(k):
    rating = int(input())
    overall += rating

maximum = (overall + 3 * (n - k)) / n
minimum = (overall + (-3) * (n - k)) / n
print(minimum, maximum)
