# 816 34 / 850 38
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split())) + [0]
M = int(input())
B = list(map(int, input().split())) + [0]

sumA, sumB = defaultdict(int), defaultdict(int)
for l in range(N):
    tmp = A[l]
    sumA[tmp] += 1
    r = l+1
    while r < N:
        tmp += A[r]
        sumA[tmp] += 1
        r += 1

for l in range(M):
    tmp = B[l]
    sumB[tmp] += 1
    r = l+1
    while r < M:
        tmp += B[r]
        sumB[tmp] += 1
        r += 1

aValues = list(sumA.keys())
bValues = list(sumB.keys())
aValues.sort(), bValues.sort()

answer = 0
for aV in aValues:
    l, r = 0, len(sumB)-1
    result = T - aV
    while l <= r:
        mid = (l + r)//2
        if bValues[mid] < result:
            l = mid + 1
        elif bValues[mid] > result:
            r = mid - 1
        else:
            answer += (sumA[aV] * sumB[bValues[mid]])
            break

print(answer)