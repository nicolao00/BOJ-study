import sys
from collections import deque

input = sys.stdin.readline

# 1134
N, K = map(int, input().split())
board = [[1001] * (N + 2)] + [[1001] + list(map(int, input().split())) + [1001] for _ in range(N)] + [[1001] * (N + 2)]
S, X, Y = map(int, input().split())

# 바이러스 초기 상태 설정
dq = deque()
for r in range(1, N + 1):
    for c in range(1, N + 1):
        if board[r][c] != 0:
            dq.append((board[r][c], r, c))  # (바이러스 번호, 행, 열)

# 바이러스 번호 우선순위로 정렬
dq = deque(sorted(dq))

while S > 0:
    count = len(dq)
    while count > 0:
        num, r, c = dq.popleft()
        for nr, nc in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
            if board[nr][nc] == 0:
                board[nr][nc] = num
                dq.append((num, nr, nc))
        count -= 1
    S -= 1

print(board[X][Y])