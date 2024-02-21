# 200 - 239

import sys
input = sys.stdin.readline

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

board = [[False]*(101) for _ in range(101)]

def stackFun(stack, row, col, generation):
    r, c = row, col
    for d in stack[::-1]:
        d = (d + 1) % 4
        r += dr[d]
        c += dc[d]
        board[r][c] = True
        if generation < g:
            stack.append(d)

    if generation < g:
        stackFun(stack, r, c, generation + 1)


for c, r, d, g in info:
    stack = [d]
    board[r][c] = True
    r += dr[d]
    c += dc[d]
    board[r][c] = True
    if g > 0:
        stackFun(stack, r, c, 1)

answer = 0
for r in range(100):
    for c in range(100):
        if board[r][c] and board[r+1][c] and board[r][c+1] and board[r+1][c+1]:
            answer += 1
print(answer)