# 120
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
s = list(map(int, input().split()))
sensor = sorted(s)

dist = sorted([sensor[i] - sensor[i-1] for i in range(1, len(sensor))], reverse=True)
print(sum(dist[K-1:]))