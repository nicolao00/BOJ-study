# 341 - 500
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
answer = 0

big, small = defaultdict(set), defaultdict(set)
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    small[a].add(b)
    big[b].add(a)

def find(start, dic):
    visit = [False] * (N + 1)
    visit[start] = True
    dq = deque()
    for i in dic[start]:
        dq.append(i)
    while dq:
        value = dq.popleft()
        for i in dic[value]:
            if visit[i]:
                continue
            dq.append(i)
            visit[i] = True
            dic[start].add(i)

for v in range(1, N+1):
    find(v, big)
    find(v, small)

for i in range(1, N+1):
    if len(small[i]) + len(big[i]) == N-1:
        answer += 1

print(answer)