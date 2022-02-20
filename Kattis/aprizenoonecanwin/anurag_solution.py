n, x = list(map(int, input().split()))
prices = list(map(int, input().split()))

prices.sort()

for i in range(1, len(prices)):
    prices[i] = prices[i] + prices[i-1]

print(prices)
