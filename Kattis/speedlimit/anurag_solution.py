while True:
	n = int(input())

	if n == -1: break

	currSpeed, currTime = [], []

	for i in range(n):
		speed, time = list(map(int, input().split()))
		currSpeed.append(speed)
		currTime.append(time)
	
	firstSpeed = currSpeed[0]
	firstTime = currTime[0]
	distance = firstSpeed * firstTime

	for x, y in zip(range(1, len(currSpeed)), range(1, len(currTime))):
		diff = currTime[y] - currTime[y-1]
		distance += (currSpeed[x] * diff) 

	print(distance, 'miles')
