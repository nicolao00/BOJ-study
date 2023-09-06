N = int(input())
dices = []
sixIdxs = [0] * N
answer = 0

def makePair(idx):
    if idx == 0: idx = 5
    elif idx == 1: idx = 3
    elif idx == 2: idx = 4
    elif idx == 3: idx = 1
    elif idx == 4: idx = 2
    else: idx = 0
    return idx

for i in range(N):
    dices.append(list(map(int, input().split())))
    six = dices[i].index(6)
    sixIdxs[i] = [six, makePair(six)]

for i in range(6):
    idx, result = i, 0
    for cnt in range(N):
        # if idx == sixIdxs[cnt][0] or idx == sixIdxs[cnt][1]: result += 5
        # else: result += 6
        temp = 0
        for i, v in enumerate(dices[cnt]):
            if idx == i or makePair(idx) == i: continue
            temp = max(temp, v)
        result += temp
        # 윗면 아랫면 교체
        if cnt + 1 != N: idx = dices[cnt + 1].index(dices[cnt][makePair(idx)])
    answer = max(answer, result)

print(answer)