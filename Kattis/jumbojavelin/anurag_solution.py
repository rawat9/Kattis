N = int(input())

combined_length = 0

for _ in range(N):
    length = int(input())
    combined_length += length

print(combined_length - (N-1))
