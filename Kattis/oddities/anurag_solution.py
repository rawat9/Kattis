tc = int(input())

for _ in range(tc):
    n = int(input())
    print(f"{n} is even" if n % 2 == 0 else f"{n} is odd")
