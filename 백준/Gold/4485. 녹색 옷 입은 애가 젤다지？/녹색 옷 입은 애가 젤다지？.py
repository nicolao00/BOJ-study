#205

import sys, heapq
input = sys.stdin.readline
test = 0
while N := int(input()):
    test += 1
    turnel = []
    for _ in range(N):
        turnel.append(list(map(int, input().split())))
    dp = [[1e9]*N for _ in range(N)]
    dp[0][0] = turnel[0][0]
    h = []
    heapq.heappush(h, (dp[0][0], 0, 0))
    while h:
        cost, r, c = heapq.heappop(h)
        if r == N-1 and c == N-1:
            print(f'Problem {test}: {dp[N - 1][N - 1]}')
            break
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and dp[nr][nc] > cost + turnel[nr][nc]:
                dp[nr][nc] = cost + turnel[nr][nc]
                heapq.heappush(h, (dp[nr][nc], nr, nc))