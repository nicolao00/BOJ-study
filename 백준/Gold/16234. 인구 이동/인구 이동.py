# 110
import sys
from collections import deque,defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
unionLoc = defaultdict(list)  # 연합에 속한 나라 위치
unionCnt = defaultdict(int) # 연합의 총 인구 수
visit = 0

def dfs(r, c, union):
    global board, unionCnt, unionLoc, visit
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
            if L <= abs(board[r][c] - board[nr][nc]) <= R:
                visit[nr][nc] = True
                unionLoc[union].append((nr, nc))
                unionCnt[union] += board[nr][nc]
                dfs(nr, nc, union)

answer = 0
while 1:
    unionLoc = defaultdict(list)  # 연합에 속한 나라 위치
    unionCnt = defaultdict(int)  # 연합의 총 인구 수
    visit = [[False] * N for _ in range(N)]
    union = 0
    for row in range(N):
        for col in range(N):
            if not visit[row][col]:
                union += 1
                dfs(row, col, union)

    for key in unionCnt.keys():
        afterCnt = unionCnt[key] // len(unionLoc[key])
        for r, c in unionLoc[key]:
            board[r][c] = afterCnt

    if union == N**2:
        break
    answer += 1
print(answer)
