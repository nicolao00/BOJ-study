# 630
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
answer, baby, eatCnt = 0, 2, 0
# 보드판 테두리 생성
board = [[403]*(N+2)]
for row in range(N):
    tmp = [403] + list(map(int, input().split())) + [403]
    for col, v in enumerate(tmp[1:-1]):
        if v == 9:
            sRow, sCol = row, col
    board.append(tmp)
board.append([403]*(N+2))

board[sRow + 1][sCol + 1] = 0
visit = [[False] * (N+2) for _ in range(N+2)]
visit[sRow + 1][sCol + 1] = True

dq = deque()
candiCnt = 0
candi, tmp = [], []
dq.append((sRow + 1, sCol + 1, 0))
while dq:
    r, c, t = dq.popleft()

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        nr, nc = r + dr, c + dc
        if baby >= board[nr][nc] and not visit[nr][nc]:
            if baby == board[nr][nc] or board[nr][nc] == 0: # 빈칸이거나 아기 상어와 크기가 같으면 그냥 담칸으로 감
                tmp.append((nr, nc, t + 1))
            else: # 아기상어가 더 큰 경우
                candi.append((nr, nc, t + 1))
            visit[nr][nc] = True

    if len(dq) == 0:
        if candi:
            result = (401, 401, 401)
            for i in candi:
                if i < result:
                    result = i
            r, c, t = result
            visit = [[False] * (N + 2) for _ in range(N + 2)]
            visit[r][c] = True
            board[r][c] = 0
            eatCnt += 1
            if eatCnt == baby:
                baby += 1
                eatCnt = 0
            answer += t
            dq.append((r, c, 0))
        else:
            dq = deque(tmp)
        tmp = []
        candi = []

print(answer)