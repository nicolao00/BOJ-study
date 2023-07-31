import math
from collections import Counter
def solution(weights):
    answer = 0
    total = {}
    counter = Counter(weights)
    for value in counter.values():
        if value != 1:
            answer -= math.comb(value, 2)*2
            
    sameCnt = len(weights)-len(set(weights))
    for w in weights:
        for i in range(2,5):
            if w * i in total:
                total[w * i] += 1
            else:
                total[w * i] = 1
    for value in total.values():
        if value != 1:
            answer += math.comb(value, 2)
            
    return answer