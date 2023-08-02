#255

from collections import Counter, defaultdict
def solution(topping):
    answer = 0
    sis = defaultdict(int)
    sis[topping[0]]
    bro = Counter(topping[1:len(topping)])
    broLen = len(bro)
    if len(sis) == broLen: answer += 1

    for i in range(1, len(topping)-1):
        sis[topping[i]] += 1
        bro[topping[i]] -= 1
        if bro[topping[i]] == 0:
            bro.pop(topping[i])
            broLen -= 1
        if len(sis) == broLen: answer += 1

    return answer
