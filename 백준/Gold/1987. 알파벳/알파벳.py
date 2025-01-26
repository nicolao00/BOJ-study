import sys
from collections import deque
input = sys.stdin.readline

# 1222
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visit = set(board[0][0])
answer = 1

def dfs(r, c):
    global answer
    answer = max(answer, len(visit))
    if answer == 26:
        return 

    for nr, nc in [(r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)]:
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in visit:
            visit.add(board[nr][nc])
            dfs(nr, nc)
            visit.remove(board[nr][nc])

dfs(0, 0)
print(answer)