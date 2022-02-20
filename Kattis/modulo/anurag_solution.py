numbers = []

for _ in range(10):
    num = int(input())     
    numbers.append(num)

print(len(set(map(lambda x: x % 42, numbers))))

