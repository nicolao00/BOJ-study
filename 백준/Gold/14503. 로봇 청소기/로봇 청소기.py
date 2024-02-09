#329
import sys
from collections import deque
input = sys.stdin.readline

drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N, M = map(int, input().split())
sRow, sCol, sD = map(int, input().split())
board = [[1]*(M+2)]
for _ in range(N):
        board.append([1] + list(map(int, input().split())) + [1])
board.append([1]*(M+2))

answer = 1
dq = deque([(sRow+1, sCol+1, sD)])
board[sRow+1][sCol+1] = 2
while dq:
        r, c, d = dq.popleft()
        flag = False
        for dd in range(-1, -5, -1):
                nd = d + dd
                if nd < 0: nd = nd + 4
                nr, nc = r + drdc[nd][0], c + drdc[nd][1]
                if board[nr][nc] == 0:
                        flag = True
                        dq.append((nr, nc, nd))
                        board[nr][nc] = 2
                        answer += 1
                        break
        if not flag:
                nr, nc = r - drdc[d][0], c - drdc[d][1]
                if board[nr][nc] == 1: break
                else: dq.append((nr, nc, d))
print(answer)