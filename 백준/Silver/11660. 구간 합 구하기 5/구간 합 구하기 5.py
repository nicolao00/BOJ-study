# 850

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [[0] * (N + 1)]
for _ in range(N):
    board.append([0] + list(map(int, input().split())))
test = [list(map(int, input().split())) for _ in range(M)]
stackSum = [[0] * (N + 1)]
for _ in range(N):
    stackSum.append([0] * (N + 1))

# 각 칸까지의 누적합 구하기
for i in range(1, N+1):
    for j in range(1, N+1):
        stackSum[i][j] = stackSum[i-1][j] + stackSum[i][j-1] - stackSum[i-1][j-1] + board[i][j]
answer = []
for x1, y1, x2, y2 in test:
    answer.append(stackSum[x2][y2] - stackSum[x2][y1-1] - stackSum[x1-1][y2] + stackSum[x1-1][y1-1])
print("\n".join(map(str, answer)))

