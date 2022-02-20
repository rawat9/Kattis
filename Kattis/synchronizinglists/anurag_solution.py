while True:
    n = int(input())

    if n == 0:
        break

    numbers = []
    for _ in range(2 * n):
        num = int(input())
        numbers.append(num)

    first, second = numbers[:n], numbers[n:]
    zipped = dict(zip(sorted(first), sorted(second)))
    print(*[zipped[f] for f in first], sep='\n')
    print()
