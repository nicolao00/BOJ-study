# 433
import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
hq = []

for card in cards:
    heapq.heappush(hq, card)

for _ in range(m):
    result = heapq.heappop(hq) + heapq.heappop(hq)
    heapq.heappush(hq, result)
    heapq.heappush(hq, result)
print(sum(hq))