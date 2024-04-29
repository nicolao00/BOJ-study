# 1002
import sys
import heapq
input = sys.stdin.readline
from collections import deque

N, M, X = map(int, input().split())
board = [[] for _ in range(N+1)]
moveTime = dict()
for _ in range(M):
    start, end, time = map(int, input().split())
    board[start].append(end)
    moveTime[(start, end)] = time

def bfs(start, goal):
    global answer
    visit = [False] * (N+1)
    visit[start] = True
    dq = []
    heapq.heappush(dq, (0, start))
    while dq:
        t, i = heapq.heappop(dq)
        visit[i] = True
        if i == goal:
            return t
        for nextI in board[i]:
            if not visit[nextI]:
                heapq.heappush(dq, (t + moveTime[(i, nextI)], nextI))


answer = 0
for idx in range(1, N+1):
    if idx == X: continue
    answer = max(answer, bfs(idx, X) + bfs(X, idx))

print(answer)