# 452
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
lab, empty, virus  = [], [], []
drdc = [[-1, 0], [0, 1], [1, 0], [0, -1]]
answer = 0

for r in range(N):
    lab.append([])
    for c, v in enumerate(list(map(int, input().split()))):
        lab[r].append(v)
        if v == 0:
            empty.append([r, c])
        elif v == 2:
            virus.append([r, c])

for combs in combinations(empty, 3):
    after = [arr[:] for arr in lab]
    for r, c in combs: # 벽 세울 위치에 벽 세움
        after[r][c] = 1

    dq = deque(virus)
    while dq:
        r, c = dq.popleft()
        for dr, dc in drdc:
            nr, nc = r + dr, c + dc
            if (0 <= nr < N and 0 <= nc < M and after[nr][nc] == 0):
                after[nr][nc] = 2
                dq.append([nr, nc])

    result = 0
    for r in range(N):
        for c in range(M):
            if after[r][c] == 0:
                result += 1

    if result > answer:
        answer = result

print(answer)