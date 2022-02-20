while True:
    n = int(input())

    if n == 0:
        break
    
    names = []
    for _ in range(n):
        name = input()
        names.append(name)

    names.sort(key=lambda x: x[:2])
    print(*names, sep='\n')
    print()
