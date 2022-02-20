from itertools import zip_longest

b, d, c, l = list(map(int, input().split()))

if l % b != 0 and l % d != 0 and l % c != 0: print('impossible')

first = l // b
second = l // d
third = l // c

for i,j,k in zip_longest(range(first+1), range(second+1), range(third+1), fillvalue=0):
    print(i, j, k)
    # if (i*b + j*d + k*c) == l:
        # print(i, j, k)
