# 1232
import sys
from itertools import permutations

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))


idx = N-1
while idx > 0:
    if nums[idx-1] > nums[idx]:
        for i in range(N-1, 0, -1):
            if (nums[idx-1] > nums[i]):
                nums[idx-1], nums[i] =  nums[i], nums[idx-1]
                break
        break
    else:
        idx -= 1

nums = nums[:idx] + sorted(nums[idx:], reverse=True)
if idx == 0:
    print(-1)
else:
    print(*(nums))