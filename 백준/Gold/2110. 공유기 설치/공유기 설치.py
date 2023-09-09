# 1040
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
homeList = []
for _ in range(N):
    homeList.append(int(input()))
homeList.sort()

def getWifi(dist):
    cnt, location = 0, homeList[0]
    for v in homeList:
        if location > v: continue
        else:
            location = v + dist
            cnt += 1
    return cnt


wifiCnt = answer = 0
left, right = 1, homeList[-1] - homeList[0]

while left <= right:
    mid = (left + right)//2
    wifiCnt = getWifi(mid)
    if wifiCnt >= C:
        left = mid + 1
        answer = mid
    else :
        right = mid - 1
print(answer)