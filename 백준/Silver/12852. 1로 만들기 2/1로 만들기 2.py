# 1106
from collections import defaultdict
N = int(input())
dp = [1000000] * (N*3)
elements = defaultdict(list)
dp[N] = 0

for i in range(N, 0, -1):
    if i % 3 == 0 and dp[i//3] > dp[i] + 1:
        dp[i//3] = dp[i] + 1

    if i % 2 == 0 and dp[i//2] > dp[i] + 1:
        dp[i//2] = dp[i] + 1

    if dp[i-1] > dp[i] + 1:
        dp[i-1] = dp[i] + 1

num = 1
answer = [num]
while num < N:
    if dp[num+1] <= dp[num*2] and dp[num+1] <= dp[num*3]:
        answer.append(num+1)
        num += 1
    elif dp[num*2] <= dp[num+1] and dp[num*2] <= dp[num*3]:
        answer.append(num*2)
        num *= 2
    else:
        answer.append(num*3)
        num *= 3

answer = reversed(answer)
print(dp[1])
print(*answer)