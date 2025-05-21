import sys
from collections import defaultdict
input = sys.stdin.readline

# 140
N, target, P = map(int, input().split())
scores = list(map(int, input().split()))

answer = 1
sameCnt = 0
last = 0
for score in scores:
    if answer > P:
        break

    if score > target:
        # 이전 값과 현재 값이 동일하지 않을 때
        if last != score:
            last = score
        answer += sameCnt + 1
        sameCnt = 0
    elif score == target:
        sameCnt += 1
    else:
        break

if answer + sameCnt > P:
    print(-1)
else:
    print(answer)