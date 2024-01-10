# 1025
import sys, copy
from collections import deque
input = sys.stdin.readline

start = list(map(int, input().rstrip().split()))
answer = set()
visit = {}

visit[tuple([0, 0, start[2]])] = True
dq = deque([[0, 0, start[2]]])
while dq:
    bottle = dq.popleft()
    if bottle[0] == 0:
        answer.add(bottle[2])
    for i, water in enumerate(bottle):
        if water == 0:
            continue
        for remainI, remainW in enumerate(bottle):
            if i == remainI:
                continue
            if remainW == start[remainI]: # 이미 가득찬 물병
                continue

            tmp = bottle[:]
            if start[remainI] - remainW >= water: # 부족한 양보다 줄 수 있는 물이 더 적을 때
                tmp[i] = 0
                tmp[remainI] += water
            else:
                tmp[i] = water - (start[remainI] - remainW)
                tmp[remainI] = start[remainI]

            if visit.get(tuple(tmp)):
                continue
            dq.append(tmp)
            visit[tuple(tmp)] = True


print(*sorted(answer))