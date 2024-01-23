import sys
input = sys.stdin.readline
from collections import deque

Irow, Icol = map(int, input().split())
answer = 1000001
visit = [[[False] * (Icol+2) for _ in range(Irow+3)] for _ in range(2)]
board = [[-1] * (Icol+2)]

for r in range(1, Irow+1):
    board.append([-1])
    for value in list(input().strip()):
        board[r].append(int(value))
    board[r].append(-1)
board.append([-1]*Icol)

def bfs():
    global Irow, Icol, answer, board, visit

    visit[0][1][1] = True
    dq = deque([[1, 1, 1, 0]])
    while dq:
        r, c, cnt, flag = dq.popleft()
        if r == Irow and c == Icol:
            answer = cnt
            return
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 1 <= nr <= Irow and 1 <= nc <= Icol and not visit[flag][nr][nc]:
                if board[nr][nc] == 0:
                    visit[flag][nr][nc] = True
                    dq.append([nr, nc, cnt + 1, flag])
                else:
                    if flag:
                        continue
                    visit[1][nr][nc] = True
                    dq.append([nr, nc, cnt + 1, 1])

bfs()
if answer == 1000001:
    print(-1)
else:
    print(answer)