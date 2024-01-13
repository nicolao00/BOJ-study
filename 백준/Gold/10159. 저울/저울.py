# 320 10159
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
compared = [N-1] * (N+1)
biglst = [[] for _ in range(N+1)]
visit = [False] * (N+1)

for _ in range(M):
    big, small = map(int, input().split())
    biglst[big].append(small)

def dfs(start, curr):
    visit[curr] = True
    for small in biglst[curr]:
        if not visit[small]:
            compared[start] -= 1
            compared[small] -= 1
            dfs(start, small)

for i in range(1, N+1):
    visit = [False] * (N+1)
    dfs(i, i)

for i in range(1, N + 1):
    print(compared[i])