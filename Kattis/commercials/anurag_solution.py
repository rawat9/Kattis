n, p = list(map(int, input().split()))
students = list(map(int, input().split()))

total = []
for i in range(1, len(students)-1):
    tot = students[i-1] + students[i] + students[i+1]
    total.append(tot)

ans = list(map(lambda x: p*n - x, total))
print(max(ans))
