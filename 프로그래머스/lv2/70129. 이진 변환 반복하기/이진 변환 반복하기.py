# 709

def transBinary(str):
    global transCnt, zeroCnt
    strLen = len(str)
    str = str.replace('0', '')
    transLen = len(str)

    zeroCnt += strLen - transLen
    transCnt += 1

    return format(transLen, 'b')


def solution(s):
    answer = []
    global transCnt, zeroCnt
    transCnt = zeroCnt = 0
    result = s
    while result != "1":
        result = transBinary(result)
    answer.append(transCnt)
    answer.append(zeroCnt)
    return answer