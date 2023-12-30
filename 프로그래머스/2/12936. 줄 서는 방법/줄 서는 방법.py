from collections import deque
def solution(n, k):
    answer = []
    numlist = deque(i for i in range(1, n + 1))
    dp = [1, 1] + [0] * (n-1)
    for i in range(1, n+1):
        dp[i] = dp[i-1] * i

    for i in range(n-1, -1, -1):
        div = (k-1) // dp[i]
        k %= dp[i]
        answer.append(numlist[div])
        numlist.remove(numlist[div])

    return answer