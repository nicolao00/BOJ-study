import sys

# 836
input = sys.stdin.readline

N, M = map(int, input().split())
length = [int(input()) for _ in range(N)]
left, right = 1, max(length)*M

def check(time):
    result = 0
    for l in length:
        result += time // l
    return result

answer = 0
while left <= right:
    mid = (left + right) // 2
    result = check(mid)

    if result >= M:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
print(answer)