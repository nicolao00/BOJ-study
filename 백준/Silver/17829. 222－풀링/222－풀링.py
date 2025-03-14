# 107
import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

while len(nums) > 1:
    newNums = []
    for r in range(0, len(nums), 2):
        row = []
        for c in range(0, len(nums), 2):
            tmp = [nums[r][c], nums[r][c + 1], nums[r + 1][c], nums[r + 1][c + 1]]
            tmp.sort()
            row.append(tmp[2])
        newNums.append(row)

    nums = newNums

print(nums[0][0])