n = int(input())

formatter = lambda x: f'{x:.4f}'

for _ in range(n):
    b, p = list(map(float, input().split()))
    BPM = (60*b) / p
    diff = BPM/b
    print(formatter(BPM - diff), formatter(BPM), formatter(BPM + diff))
    
