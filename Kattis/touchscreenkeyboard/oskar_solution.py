import math


class Solution:
    def __init__(self):
        pass

    def solve(self):
        keyboard = []
        for i in range(3):
            keyboard.append(list(map(int, input().split(' '))))

        paths = {}

        for i in range(3):
            for j in range(3):
                paths[keyboard[i][j]] = [i, j]

        sorted_keys = sorted(paths.keys())

        distance = 0
        for i in range(1, len(sorted_keys)):
            x1 = paths[sorted_keys[i-1]][0]
            y1 = paths[sorted_keys[i-1]][1]
            x2 = paths[sorted_keys[i]][0]
            y2 = paths[sorted_keys[i]][1]
            distance += math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

        print(distance)


solution = Solution()
solution.solve()
