# 1208

import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
board, house, chicken = [], [], []
for r in range(N):
    tmp = list(map(int, input().split()))
    for c, v in enumerate(tmp):
        if v == 0: continue
        elif v == 1: house.append((r, c))
        else: chicken.append((r, c))
    board.append(tmp)

chkToHome = []
for r, c in chicken:
    tmp = []
    for r2, c2 in house:
        tmp.append(abs(r-r2) + abs(c-c2))
    chkToHome.append(tmp)

answer = 100000
for comb in combinations(range(len(chicken)), M):
    distance = [1000] * len(house)
    for chkIdx in comb:
        for homeIdx, dist in enumerate(chkToHome[chkIdx]):
            if distance[homeIdx] > dist:
                distance[homeIdx] = dist
    answer = min(answer, sum(distance))

print(answer)

# 각 치킨 집마다 집까지의 거리들 다 저장해둠