# 1113

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [[0] * C for _ in range(R)]
for r in range(R):
    value = int(input())
    for c in range(C):
        board[r][c] = value // 10**(C-c-1)
        value %= 10 ** (C - c-1)

length = min(R-1, C-1)
while length >= 0:
    def check():
        for r in range(0, R - length):
            for c in range(0, C - length):
                if board[r][c] == board[r+length][c] == board[r][c + length] == board[r + length][c + length]:
                    print((length + 1) * (length + 1))
                    return True

    if check():
        break

    length -= 1