grades = list(map(int, input().split()))
score = int(input())

if score >= grades[0]:
    print("A")
elif score >= grades[1]:
    print("B")
elif score >= grades[2]:
    print("C")
elif score >= grades[3]:
    print("D")
elif score >= grades[4]:
    print("E")
else:
    print("F")
