import sys
from itertools import combinations

input = sys.stdin.readline

# 621
N, K = map(int, input().split())
houses = [tuple(map(int, input().split())) for _ in range(N)]

answer = 200001
for comb in combinations(range(N), K):
    result = 0
    # 모든 집 순회
    for i in range(N):
        tmp = 200001
        # 각 집에서 모든 보호소 순회
        for safe in comb:
            tmp = min(tmp, abs(houses[safe][0] - houses[i][0]) + abs(houses[safe][1] - houses[i][1]))

        result = max(result, tmp)
    answer = min(answer, result)

print(answer)