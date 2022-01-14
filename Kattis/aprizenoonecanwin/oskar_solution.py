def solution():
    n, min_total = map(lambda x: int(x), input().split(' '))
    prices = list(map(lambda x: int(x), input().split(' ')))

    prices = sorted(prices)

    total_items = 1

    if len(prices) > 1:
        for i in range(1, len(prices)):
            if prices[i-1] + prices[i] <= min_total:
                total_items += 1

    return total_items


print(solution())
