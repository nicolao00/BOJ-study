# 908 - 1002
import sys
input = sys.stdin.readline
str1 = input().rstrip()
str2 = input().rstrip()
answer = []
dp = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
for st2 in range(1, len(str2)+1):
    for st1 in range(1, len(str1)+1):
        if str2[st2-1] == str1[st1-1]:
            dp[st2][st1] = dp[st2-1][st1-1] + 1
        else:
            dp[st2][st1] = max(dp[st2][st1-1], dp[st2-1][st1])

s2, s1 = len(str2)-1, len(str1)-1
while s1 >= 0 and s2 >= 0:
    if dp[s2 + 1][s1] != dp[s2 + 1][s1 + 1] and dp[s2 + 1][s1 + 1] != dp[s2][s1 + 1]:
        answer.append(str1[s1])
        s2 -= 1
        s1 -= 1
    elif dp[s2 + 1][s1 + 1] == dp[s2][s1 + 1]:
        s2 -= 1
    elif dp[s2 + 1][s1] == dp[s2 + 1][s1 + 1]:
        s1 -= 1

print(dp[len(str2)][len(str1)])
print("".join(reversed(answer)))
