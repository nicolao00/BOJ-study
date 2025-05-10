import sys
input = sys.stdin.readline

# 1156
sound = input().rstrip()

# 각 알파벳을 가지고 있는 현재 존재하는? 오리 개수 저장 (a[]면 a까지 울은 오리의 개수)
duckCount = {'q':0, 'u':0, 'a':0, 'c':0, 'k':0}
quack = "quack"
flag = False
answer = 0
for word in list(sound):
    if word == 'q':
        duckCount[word] += 1
    else:
        idx = 0
        while quack[idx] != word:
            idx += 1
        if duckCount[quack[idx - 1]] > 0:
            duckCount[quack[idx - 1]] -= 1
            duckCount[word] += 1
        else:
            flag = True
            break

    sums = 0
    for v in duckCount.values():
        sums += v
    answer = max(answer, sums - duckCount['k'])

remainFlag = False
for k, v in duckCount.items():
    if k == 'k':
        continue
    if v > 0:
        remainFlag = True
        break

if not flag and not remainFlag:
    print(answer)
else:
    print(-1)