max_grades = []
for _ in range(5):
    grades = list(map(int, input().split()))
    max_grades.append(sum(grades))

print(max_grades.index(max(max_grades)) + 1, max(max_grades))
