# 1058 - 11:11 / 12:34 - 230 / 8:45
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
board, machine, dustSet = [[-1] * (C+2)], [], [] # 보드판, 공기청청기 위치, 먼지 위치(순서 O), 먼지 위치(중복 제거)
for r in range(R):
    tmp = list(map(int, input().split()))
    for c, v in enumerate(tmp):
        if v == -1:
            machine.append(r+1)
        elif v != 0:
            dustSet.append((r+1, c+1))
    board.append([-1] + tmp + [-1])
board.append([-1] * (C+2))

for _ in range(T):
    # 해당 시간에 먼지가 이동하는 로직
    changeBoard = [lst[:] for lst in board]
    for r, c in dustSet:
        dAmount = board[r][c] // 5
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if board[nr][nc] != -1:
                changeBoard[nr][nc] += dAmount
                changeBoard[r][c] -= dAmount
    board = changeBoard

    # 해당 시간에 먼지가 순환하는 로직
    r1, r2 = machine
    for r in range(r1-1, 1, -1):
        board[r][1] = board[r-1][1]
    for c in range(1, C):
        board[1][c] = board[1][c+1]
    for r in range(1, r1+1):
        board[r][C] = board[r+1][C]
    for c in range(C, 2, -1):
        board[r1][c] = board[r1][c-1]
    board[r1][2] = 0

    for r in range(r2+1, R):
        board[r][1] = board[r+1][1]
    for c in range(1, C):
        board[R][c] = board[R][c+1]
    for r in range(R, r2-1, -1):
        board[r][C] = board[r-1][C]
    for c in range(C, 2, -1):
        board[r2][c] = board[r2][c-1]
    board[r2][2] = 0

    dustSet = []
    for r, lst in enumerate(board):
        for c, v in enumerate(lst):
            if v >= 5:
                dustSet.append((r, c))

answer = 2*(R+2) + 2*(C+2) + 2 - 4 # 테두리 + 공기청정기의 -1
for lst in board:
    answer += sum(lst)
print(answer)
