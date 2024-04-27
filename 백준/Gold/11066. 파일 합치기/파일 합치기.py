# 640

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    fSize = [0] + list(map(int, input().split()))
    sums = [0] * (K + 1)
    sums[1] = fSize[1]
    for i in range(2, K+1):
        sums[i] = sums[i - 1] + fSize[i]

    # dp[i][j] : i부터 j까지의 최소 합
    dp = [[0]*(K+1) for _ in range(K+1)]

    # 길이
    for d in range(2, K+1):
        # 시작점
        for s in range(1, K-d+2):
            dp[s][s+d-1] = min(dp[s][bound] + dp[bound+1][s+d-1] for bound in range(s, s+d-1)) + (sums[s+d-1] - sums[s-1])

    print(dp[1][K])