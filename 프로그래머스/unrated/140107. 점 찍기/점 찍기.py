# 658
import math
def solution(k, d):
    answer = 0
    y=0
    for x in range(d+1):
        k2y2 = math.pow(d,2) - math.pow(k,2) * math.pow(x,2)
        if (k2y2 < 0): break;
        answer += int(math.sqrt(k2y2 // math.pow(k,2))) + 1
        
    return answer