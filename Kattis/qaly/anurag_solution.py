n = int(input())

qaly = 0
for i in range(n):
    lst_input = input().split()
    ql = float(lst_input[0])
    period = float(lst_input[1])
    qaly += ql * period
    
print(qaly)


# Time Complexity: O(n)
# Space Complexity: O(1)
