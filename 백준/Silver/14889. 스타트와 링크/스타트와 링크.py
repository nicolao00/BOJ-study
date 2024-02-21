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

visit = {}
answer = 1e9

def combSum(comb):
    result = 0
    for i in range(len(comb)):
        for j in range(i + 1, len(comb)):
            result += ijSum[(comb[i], comb[j])]
    return result

for team1 in combinations(range(N), N//2):
    if team1 in visit: continue
    team1stet = combSum(team1)
    team2 = [i for i in range(N) if i not in team1]
    team2stet = combSum(team2)
    visit[tuple(team2)] = team2stet

    answer = min(answer, abs(team1stet - team2stet))

print(answer)