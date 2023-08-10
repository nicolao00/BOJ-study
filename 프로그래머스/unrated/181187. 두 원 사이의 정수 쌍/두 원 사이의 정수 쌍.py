import math
# 1126
def solution(r1, r2):
    answer = 0
    # x: [0 ~ 작은 원의 반지름]
    for x in range(r1 + 1):
        r2Max = int(math.sqrt((pow(r2, 2) - pow(x, 2))))
        r1Max = math.sqrt((pow(r1, 2) - pow(x, 2)))
        answer += r2Max - int(r1Max)
        if r1Max == int(r1Max): answer += 1
    print(answer)

    # x: (작은 원의 반지름 ~ 큰 원 반지름]
    for x in range(r1 + 1, r2 + 1):
        answer += int(math.sqrt((pow(r2, 2) - pow(x, 2)))) + 1
    print(answer)
    answer *= 4
    answer -= 4 * (r2 - r1 + 1)
    return answer