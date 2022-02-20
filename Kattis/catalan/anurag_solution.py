from math import factorial

n = int(input())

for _ in range(n):
    x = int(input())

    catalan = factorial(2 * x) // (factorial(x + 1) * factorial(x))
    print(catalan)
