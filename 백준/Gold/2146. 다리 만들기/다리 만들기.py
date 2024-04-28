# 1243

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
# board = [[0]*(N+2)] + [[0]+list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
board = [list(map(int, input().split())) for _ in range(N)]
# 그룹별 끝값들을 저장할 딕셔너리
groupEdge = dict(set())

def makeGroup(row, col, groupNum):
    dq = deque()
    dq.append((row, col))
    while dq:
        r, c = dq.popleft()
        for dr, dc in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == 1:
                    board[nr][nc] = groupNum
                    dq.append((nr, nc))
                elif board[nr][nc] == 0:
                    groupEdge[groupNum].add((r, c))

# 그룹번호는 2부터 시작
groupNum = 1
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            groupNum += 1
            groupEdge[groupNum] = set()
            board[r][c] = groupNum
            makeGroup(r, c, groupNum)

answer = 1e9
for i in range(2, groupNum+1):
    for j in range(i+1, groupNum+1):
        for rc in groupEdge[i]:
            for nrc in groupEdge[j]:
                answer = min(abs(rc[0]-nrc[0]) + abs(rc[1] - nrc[1]) - 1, answer)

print(answer)