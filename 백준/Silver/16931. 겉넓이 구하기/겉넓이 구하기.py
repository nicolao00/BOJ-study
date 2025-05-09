import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 위 아래
answer = N*M*2

# 앞면에서 봤을 때
for r in range(N):
    answer += board[r][0]
    for c in range(1, M):
        answer += max(0, board[r][c] - board[r][c-1])
    answer += board[r][M-1]
    for c in range(M-2, -1, -1):
        answer += max(0, board[r][c] - board[r][c+1])




for c in range(M):
    answer += board[0][c]
    for r in range(1, N):
        answer += max(0, board[r][c] - board[r-1][c])
    answer += board[N-1][c]
    for r in range(N-2, -1, -1):
        answer += max(0, board[r][c] - board[r+1][c])

print(answer)