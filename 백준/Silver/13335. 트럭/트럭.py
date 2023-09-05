from collections import deque

n, w, L = map(int, input().split())
truckList = deque(map(int, input().split()))
onBridge = deque()
onBridge.append([truckList.popleft(), w])
bridgeWeight, time = onBridge[0][0], 1

while onBridge:
    time += 1
    for truck in onBridge: truck[1] -= 1
    if onBridge[0][1] == 0:
        bridgeWeight -= onBridge[0][0]
        onBridge.popleft()

    if truckList and bridgeWeight + truckList[0] <= L:
        onBridge.append([truckList[0], w])
        bridgeWeight += truckList[0]
        truckList.popleft()

print(time)