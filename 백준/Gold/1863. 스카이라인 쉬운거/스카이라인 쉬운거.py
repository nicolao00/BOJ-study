import sys 
from collections import deque
input = sys.stdin.readline

# 111
N = int(input())
answer = 0

dq = deque()
for _ in range(N):
    X, Y = map(int, input().split())

    if Y == 0:
        dq = deque()
        continue

    ## 현재 높이가 마지막 높이 클 경우
    if len(dq) == 0 or dq[-1] < Y:
        answer += 1
        dq.append(Y)
    elif dq[-1] == Y:
        continue
    ## 현재 높이가 마지막 높이보다 작을 경우
    else:
        while dq and dq[-1] > Y:
            dq.pop()
        if len(dq) == 0 or dq[-1] < Y:
            answer += 1
            dq.append(Y)
print(answer)