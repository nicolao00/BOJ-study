def solution(a):
    answer = 0

    leftMin = [1e9] * len(a)
    rightMin = [1e9] * (len(a)+1)
    for i in range(len(a)):
        leftMin[i] = min(leftMin[i-1], a[i])
        rightMin[len(a) -1 -i] = min(rightMin[len(a)-i], a[len(a) -1 -i])

    for i, v in enumerate(a):
        left, right = max(0, i-1), min(i+1, len(a)-1)

        # 큰 A 작, 없 A 작 /  기회썼으면 안됨
        if leftMin[left] >= v and rightMin[right] < v:
            answer += 1

        # 작 A 큰, 작 A 없/ 기회썼으면 안됨
        elif leftMin[left] < v and rightMin[right] >= v:
            answer += 1

        # not 작 A 작 (큰 A 큰, 그외...) / 기회써도 되고 안써도 됨
        elif not (leftMin[left] < v and rightMin[right] < v):
            answer += 1



    return answer
