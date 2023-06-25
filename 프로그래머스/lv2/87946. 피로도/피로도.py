# 1133

from itertools import permutations

def solution(k, dungeons):
    answer = -1

    dungLen = len(dungeons)
    for count in range(dungLen, 0, -1):
        permutList = list(permutations([i for i in range(0, dungLen)], count))
        for stepList in permutList:
            stemina = k
            flag = True
            for step in stepList:
                if stemina < dungeons[step][0]:
                    flag = False
                    break
                stemina -= dungeons[step][1]
            if flag:
                answer = count
                return answer