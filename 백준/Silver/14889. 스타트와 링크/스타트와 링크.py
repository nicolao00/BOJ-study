# 1218

import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ijSum = {}
for i in range(N):
    for j in range(i+1, N):
        ijSum[(i, j)] = board[i][j] + board[j][i]


answer = 1e9
def combSum(comb):
    result = 0
    for i in range(len(comb)):
        for j in range(i + 1, len(comb)):
            result += ijSum[(comb[i], comb[j])]
    return result
combination = list(combinations(range(N), N//2))
for i in range(len(combination)//2):
    team1stet = combSum(combination[i])
    team2stet = combSum(combination[len(combination)-i-1])

    answer = min(answer, abs(team1stet - team2stet))

print(answer)