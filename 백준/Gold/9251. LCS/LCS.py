# 908 - 1002
import sys
input = sys.stdin.readline
str1 = input().rstrip()
str2 = input().rstrip()

dp = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
for st2 in range(1, len(str2)+1):
    for st1 in range(1, len(str1)+1):
        if str2[st2-1] == str1[st1-1]:
            dp[st2][st1] = dp[st2-1][st1-1] + 1
        else:
            dp[st2][st1] = max(dp[st2][st1-1], dp[st2-1][st1])
print(dp[len(str2)][len(str1)])