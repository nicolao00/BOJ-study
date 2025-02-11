import sys

# 1050
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
nums = [i for i in range(1, N+1)]
factory = [1] + [i for i in range(1, N+1)]

for i in range(1, N+1):
    factory[i] *= factory[i-1]

if arr[0] == 1:
    arr[1] -= 1
    answer = []
    position = N-1
    # 순서가 0이 될떄까지 반복
    while arr[1] > 0:
        tmp = arr[1] // factory[position]
        if tmp > 0:
            arr[1] %= factory[position]
        answer.append(nums[tmp])
        nums.remove(nums[tmp])
        position -= 1

    # 숫자가 0이 됐는데 값이 아직 다 안 채워졌을 경우
    while len(answer) < N:
        answer.append(nums[0])
        nums.pop(0)
    print(*answer)
else:
    answer = 0
    position = N - 1
    for i in range(1, len(arr)):
        answer += factory[position] * nums.index(arr[i])
        nums.remove(arr[i])
        position -= 1
    print(answer + 1)