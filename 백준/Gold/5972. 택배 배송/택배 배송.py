# 722
import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
pq = []
# 연결된 노드
graph = dict(list())
for i in range(1, N+1):
    graph[i] = []
# 노드간의 소의 수
dist = dict()
# 시작점부터 해당 지점까지의 누적거리
sum = [1e9] * (N+1)

for _ in range(M):
    n1, n2, d = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    a1, a2 = min(n1, n2), max(n1, n2)
    if (a1, a2) in dist:
        dist[(a1, a2)] = min(dist[(a1, a2)], d)
    else:
        dist[(a1, a2)] = d

heapq.heappush(pq, (0, 1, 1))
while pq:
    d, n1, n2 = heapq.heappop(pq)
    for nextN in graph[n2]:
        if n1 != nextN and d + dist[min(n2, nextN), max(n2, nextN)] < sum[nextN]:
            sum[nextN] = d + dist[min(n2, nextN), max(n2, nextN)]
            heapq.heappush(pq, (sum[nextN], n2, nextN))

print(sum[N])