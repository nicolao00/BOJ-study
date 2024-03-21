# 855 - 945
import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list('X'*(C+2))]
for _ in range(R):
    board.append(list('X' + input().rstrip() + 'X'))
board.append(list('X'*(C+2)))
biber, waters = deque(), set()
visit = [[False]*(C+2) for _ in range(R+2)]

for r, lst in enumerate(board):
    for c, v in enumerate(lst):
        if v == '*':
            waters.add((r, c))
        elif v == 'S':
            biber.append((r, c))

def biberCheck():
    for _ in range(len(biber)):
        r, c = biber.popleft()
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if board[nr][nc] == 'D':
                print(answer)
                biber.clear()
                return True
            if not visit[nr][nc] and board[nr][nc] == '.':
                visit[nr][nc] = True
                biber.append((nr, nc))
    return False

answer = 0
flag = False
while 1:
    if len(biber) == 0:
        break
    answer += 1
    tmp = set()
    for r, c in waters:
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if board[nr][nc] == '.':
                board[nr][nc] = '*'
                tmp.add((nr, nc))
    waters = waters | tmp
    flag = biberCheck()
if not flag:
    print("KAKTUS")

# 물먼저 확장
# 고슴도치 이동
