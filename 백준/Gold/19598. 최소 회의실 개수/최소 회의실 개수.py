import sys
import heapq

input = sys.stdin.readline

# 345
N = int(input())
lecture = [list(map(int, input().split())) for _ in range(N)]
lecture.sort()

room = []
for start, end in lecture:
    if room and room[0] <= start:
        heapq.heappop(room)
    heapq.heappush(room, end)

print(len(room))