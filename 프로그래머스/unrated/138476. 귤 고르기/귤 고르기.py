
# 749
def solution(k, tangerine):
    answer = 0
    tangerineDic = {}
    for size in tangerine:
        if size in tangerineDic:
            tangerineDic[size] += 1
        else:
            tangerineDic[size] = 1
    cnt = 0
    for answer, orangeSize in enumerate(sorted(tangerineDic.items(), key=lambda x: x[1], reverse=True)):
        cnt += orangeSize[1]
        if k <= cnt:
            return answer + 1
