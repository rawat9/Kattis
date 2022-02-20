N = int(input())

def factorial(n):
    fact = 1
    for num in range(2, n+1):
        fact *= num
    return fact

for _ in range(N):
    num = int(input())
    print(factorial(num) % 10)
