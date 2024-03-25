# 809
import sys
input = sys.stdin.readline
from collections import deque

N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
level = list(map(int, input().split()))

for test in range(Q):
    wid = 2**level[test]
    cpBoard = [lst[:] for lst in board]

    # 회전
    for r in range(0, 2**N, wid):
        for c in range(0, 2**N, wid):
            for dr in range(wid):
                for dc in range(wid):
                    nr, nc = r + dr, c + dc
                    board[r + dc][c + wid-1 - dr] = cpBoard[nr][nc]

    # 얼음 녹는 과정
    tmpBoard = [lst[:] for lst in board]
    for r in range(2 ** N):
        for c in range(2 ** N):
            if board[r][c] > 0:
                cnt = 0
                for nr, nc in [(r, c - 1), (r-1, c), (r, c + 1), (r + 1, c)]:
                    if 0 <= nr < 2**N and 0 <= nc < 2**N and board[nr][nc] > 0:
                        cnt += 1
                if cnt < 3:
                    tmpBoard[r][c] -= 1
    board = tmpBoard

answer = 0
for lst in board:
    answer += sum(lst)
print(answer)

def bfs(r, c):
    cnt = 1
    visit[r][c] = True
    dq = deque([(r, c)])
    while dq:
        r, c = dq.popleft()
        for nr, nc in [(r, c - 1), (r - 1, c), (r, c + 1), (r + 1, c)]:
            if 0 <= nr < 2 ** N and 0 <= nc < 2 ** N and not visit[nr][nc] and board[nr][nc] > 0:
                visit[nr][nc] = True
                cnt += 1
                dq.append((nr, nc))
    return cnt

maxSize = 0
# 가장 큰 덩어리 찾기
visit = [[False]*(2**N) for _ in range(2**N)]
for r in range(2 ** N):
    for c in range(2 ** N):
        if board[r][c] > 0 and not visit[r][c]:
            maxSize = max(maxSize, bfs(r, c))
print(maxSize)