# 350
from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline

k = int(input())
lst = deque(input().split())
minA, maxA = 9999999999, -9999999999


def check(numList):
    for i, v in enumerate(lst):
        if v == '<':
            if not(numList[i] < numList[i+1]): return False
        elif v == '>':
            if not(numList[i] > numList[i+1]): return False
    return True


for numList in permutations([i for i in range(k+1)], k + 1):
    if check(numList): minA = min(minA, int(''.join(map(str, numList))))

for numList in permutations([i for i in range(9-k, 10)], k + 1):
    if check(numList): maxA = max(maxA, int(''.join(map(str, numList))))

maxA, minA = str(maxA), str(minA)
if len(maxA) != k + 1: print('0' + maxA)
else : print(maxA)
if len(minA) != k + 1: print('0' + minA)
else : print(minA)