import sys

input = sys.stdin.readline

R, C, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
prefix_sums = [[0] * (C+1) for _ in range(R+1)]

for r in range(1, R+1):
    for c in range(1, C+1):
        prefix_sums[r][c] = prefix_sums[r-1][c] + prefix_sums[r][c-1] - prefix_sums[r-1][c-1] + board[r-1][c-1]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    print((prefix_sums[r2][c2] - prefix_sums[r2][c1-1] - prefix_sums[r1-1][c2] + prefix_sums[r1-1][c1-1])//((r2-r1+1) * (c2-c1+1)))