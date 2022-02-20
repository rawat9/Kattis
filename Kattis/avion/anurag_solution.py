i = 1
res = []
for _ in range(5):
    blimp = input()
    if 'FBI' in blimp:
        res.append(i)
    i += 1
    
print('HE GOT AWAY!' if len(res) == 0 else " ".join(map(str, res)))
