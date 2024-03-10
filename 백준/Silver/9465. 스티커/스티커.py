# 837
import sys
input = sys.stdin.readline

testCase = int(input())
for _ in range(testCase):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    for c in range(1, n):
        dp[0][c] = max(dp[0][c-1], dp[1][c-1] + stickers[0][c])
        dp[1][c] = max(dp[1][c - 1], dp[0][c - 1] + stickers[1][c])
    print(max(dp[0][n-1], dp[1][n-1]))