tc = int(input())

for _ in range(tc):
    students, *grades = list(map(int, input().split()))
    average = sum(grades) / students
    result = (len(list(filter(lambda x: x > average, grades))) / students) * 100
    print(f"{result:.3f}%")
