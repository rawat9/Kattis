from collections import defaultdict

names = defaultdict(int)
while True:
    name = input() 
    if name == '***':
        break
    names[name] += 1

candidate = max(names.values())
n = sum(value == candidate for value in names.values())
print('Runoff!' if n > 1 else max(names, key=names.get))
