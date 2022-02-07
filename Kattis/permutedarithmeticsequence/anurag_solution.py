n = int(input())

def isAP(sequence):
    isValid = True
    diff = sequence[1] - sequence[0]
    
    for i in range(len(sequence)-1):
        if sequence[i+1] - sequence[i] != diff:
            isValid = False
    return isValid


for _ in range(n):
    m, *seq = list(map(int, input().split()))

    result = isAP(sorted(seq))
    if result:
        if result != isAP(seq): 
            print('permuted arithmetic')
        else:
            print('arithmetic')
    else:
        print('non-arithmetic')
