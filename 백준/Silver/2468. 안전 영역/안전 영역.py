# 850
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
location = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
for lst in location:
    maxV = max(maxV, max(lst))

def bfs(r, c):
    dq = deque([(r, c)])
    while dq:
        r, c = dq.popleft()
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and location[nr][nc] > height and not visit[nr][nc]:
                dq.append((nr, nc))
                visit[nr][nc] = True

answer = 0
for height in range(maxV):
    result = 0
    visit = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if location[row][col] > height and not visit[row][col]:
                result += 1
                bfs(row, col)
    if result == 0: break
    answer = max(result, answer)
print(answer)