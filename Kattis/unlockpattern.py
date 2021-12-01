# source: https://open.kattis.com/problems/unlockpattern
# Given an unlock pattern, can you calculate its length?
# We assume that the pivots are aligned on a unit grid,
# and the stroke moves in a straight line between two consecutive pivots.
from math import sqrt
'''
INPUT:
6 1 9
5 2 8
4 3 7
'''


def create_dict(r1,r2,r3):
    arr = [r1,r2,r3]
    dictio = {}
    x, y = 0, -1
    for row in arr:
        x, y = 0, y+1
        for num in row:
            dictio[num] = x, y
            x += 1
    return dictio


def distance(n1,n2, dictio):
    x1,y1 = dictio.get(n1)
    x2,y2 = dictio.get(n2)
    return sqrt((x1-x2)**2+(y1-y2)**2)


def total_distance(dictio):
    nums = sorted([int(i) for i in list(dictio.keys())])
    d = 0
    for i in range(len(nums)-1):
        d += distance(str(nums[i]), str(nums[i+1]), dictio)
    return d


if __name__ == '__main__':
    r1 = input().split()
    r2 = input().split()
    r3 = input().split()

    print(round(total_distance(create_dict(r1,r2,r3)), 10))

