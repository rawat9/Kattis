while True:
    n = int(input())

    if n == 0: break

    morning = []
    night = []

    for _ in range(n):
        time, period = input().split()

        if period == 'a.m.':
            morning.append([time, period])
            
        if period == 'p.m.':
            night.append([time, period])

    for time in morning:
        if time[0] == '12:00' and time[1] == 'a.m.':
            morning.insert(0, morning.pop(morning.index(time)))

    for time in night:
        if time[0] == '12:00' and time[1] == 'p.m.':
            night.insert(0, night.pop(night.index(time)))

    print(*list(map(lambda x: " ".join(x), morning + night)), sep='\n')
    print()
