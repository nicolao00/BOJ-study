# 947
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
special = {}

for _ in range(N+M):
    cur, dest = map(int, input().split())
    special[cur] = dest

def bfs():
    visit = [False] * 101
    dq = deque([(1, 0)])
    while dq:
        n, w = dq.popleft()
        for next in range(n + 1, n + 7):
            if next <= 100 and not visit[next]:
                if next in special:
                    dq.append((special[next], w + 1))
                elif next == 100:
                    print(w + 1)
                    return
                else:
                    dq.append((next, w + 1))
                    visit[next] = True

bfs()