import sys
input = sys.stdin.readline

N, M = map(int, input().split())
videos = list(map(int, input().split()))
answer = 0

def checkSize(maxSize):
    idx = 0
    sum = 0
    count = 1
    while idx < len(videos):
        # 현재 그룹이 블루레이 크기 넘어섰을 경우
        if sum + videos[idx] > maxSize:
            if videos[idx] > maxSize:
                return False
            sum = videos[idx]
            count += 1
            if count > M:
                return False
        else:
            sum += videos[idx]
        idx += 1

    # 블루레이 총 개수도 가능하고 모든 강의 다 맞춘 경우
    return True


left, right = 1, 10000000001
while left <= right:
    mid = (left + right) // 2
    result = checkSize(mid)

    # 가능했던 경우
    if result:
        answer = mid
        right = mid - 1
    # 불가능했던 경우
    else:
        left = mid + 1
print(answer)