#923
import sys
from collections import deque

input = sys.stdin.readline

H, W = map(int, input().split())
heights = list(map(int, input().split()))
dq = deque()

# 가로 인덱스, 높이, 체크중인 높이
answer = 0
minH, maxH = 500, 0

for i in heights:
    if i < minH:
        minH = i
    elif i > maxH:
        maxH = i

for i, v in enumerate(heights):
    dq.append([i, v])

for h in range(minH, maxH + 1):
    size = len(dq)
    exIndex = -1
    for _ in range(size):
        i, v = dq.popleft()
        if v <= h:
            continue
        if exIndex != -1:
            answer += i - (exIndex + 1)
        exIndex = i
        dq.append([i, v])

print(answer)