# 914
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

mod = 1000000000
dp = [[0]*(K+1) for _ in range(N+1)]
# 정수 1개만 더하는거
for i in range(N+1):
    dp[i][1] = 1
# n이 0일때
for i in range(K+1):
    dp[0][i] = 1

for k in range(1, K+1):
    for n in range(1, N+1):
        dp[n][k] = (dp[n][k-1] + dp[n-1][k]) % mod

print(dp[N][K])