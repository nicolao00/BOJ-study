# 44 125
import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
fruitCnt = defaultdict(int)

answer = 0
l = r = 0
for l in range(N):
    while r < N and (len(fruitCnt) < 2 or (len(fruitCnt) == 2 and arr[r] in fruitCnt)):
        fruitCnt[arr[r]] += 1
        r += 1

    answer = max(answer, (r-1) - l + 1)
    fruitCnt[arr[l]] -= 1
    if fruitCnt[arr[l]] <= 0:
        fruitCnt.pop(arr[l])

print(answer)