# 750

import sys
import heapq
input = sys.stdin.readline

N, M = int(input()), int(input())
costs = [list(map(int, input().split())) for _ in range(M)]
hq = []
for a, b, c in costs:
    heapq.heappush(hq, (c, a, b))

parent = [i for i in range(N+1)]

def find_root(x):
    if parent[x] == x:
        return x
    parent[x] = find_root(parent[x])
    return parent[x]

def union_root(x, y):
    x = find_root(x)
    y = find_root(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

# kruscal
answer = []
result = 0
while hq:
    c, a, b = heapq.heappop(hq)
    if find_root(a) == find_root(b):
        continue
    answer.append((c, a, b))
    result += c
    union_root(a, b)
    if len(answer) == N-1:
        break

print(result)