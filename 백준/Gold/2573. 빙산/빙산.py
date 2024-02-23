# 223
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board, ice = [], {}
for r in range(N):
    temp = list(map(int, input().split()))
    for c, v in enumerate(temp):
        if v == 0: continue
        ice[(r, c)] = 4  # 빙산 좌표 : 개수, 이웃한 바다 개수
    board.append(temp)


def seaCheck(ice):
    dq = deque(ice.keys())
    while dq:
        r, c = dq.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if board[nr][nc] != 0:
                ice[(r, c)] -= 1


answer = 0
seaCheck(ice)

while len(ice):
    # 얼음판을 녹이는 과정
    poplst = []
    for r, c in ice.keys():
        board[r][c] -= ice[(r, c)]
        if board[r][c] <= 0:
            board[r][c] = 0
            poplst.append((r, c))

    # 녹는 과정에서 바다가 된 얼음 처리하는 과정
    for r, c in poplst:
        ice.pop((r, c))
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in ice:
                ice[(nr, nc)] += 1

    answer += 1

    visit = [[False] * M for _ in range(N)]
    if len(ice) == 0:
        print(0)
        break
    startR, startC = list(ice.keys())[0]
    visit[startR][startC] = True
    check = 1
    dqVisit = deque()
    dqVisit.append(((startR, startC)))
    while dqVisit:
        r, c = dqVisit.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in ice and not visit[nr][nc]:
                visit[nr][nc] = True
                check += 1
                dqVisit.append((nr, nc))

    if check != len(ice):
        print(answer)
        break