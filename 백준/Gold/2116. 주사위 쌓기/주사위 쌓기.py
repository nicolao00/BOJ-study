import sys
input = sys.stdin.readline

N = int(input())
dices, pair = [], [5, 3, 4, 1, 2, 0]
answer = 0

for i in range(N): dices.append(list(map(int, input().split())))

for start in range(6):
    idx, result = start, 0
    for cnt in range(N):
        maxNum = 0
        for i, v in enumerate(dices[cnt]):
            if idx == i or pair[idx] == i: continue
            maxNum = max(maxNum, v)
        result += maxNum
        if cnt + 1 != N: idx = dices[cnt + 1].index(dices[cnt][pair[idx]])
    answer = max(answer, result)

print(answer)