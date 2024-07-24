import sys

input = sys.stdin.readline

N, M = map(int, input().split())
title = []
for _ in range(N):
    name, value = input().split()
    title.append((name, int(value)))

idx = 0
for cIdx in range(M):
    value = int(input())

    l, r, answer = 0, N - 1, 0
    while l <= r:
        mid = (l + r) // 2
        if title[mid][1] >= value:
            answer = mid
            r = mid - 1;
        else:
            l = mid + 1;
    print(title[answer][0])