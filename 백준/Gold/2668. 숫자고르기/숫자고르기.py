import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
answer = []
special = []

for i in range(N):
    if i + 1 == arr[i]: # 인덱스와 값이 같은 특이 케이스
        special.append(arr[i])
        continue
    init = i + 1
    result = [i + 1]
    current = arr[i] - 1
    visit = [0 for _ in range(N)]
    visit[i] = 1

    while visit[current] == 0:
        visit[current] = 1
        result.append(current + 1)
        if arr[current] == init:
            init = 0
            break
        current = arr[current] - 1

    if init == 0:
        answer += result

answer += special
answer = set(sub for sub in answer)
print(len(answer))
for i in sorted(answer):
    print(i)