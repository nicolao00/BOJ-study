# 1118
from collections import deque
def solution(ingredient):
    answer = ham = 0
    ham_set = [1,2,3,1]
    dq = []
    
    for food in ingredient:
        dq.append(food)
        dq_len=len(dq)
        if dq_len>=4:
            if ham_set==dq[dq_len-4:dq_len]:
                answer+=1
                for i in range(4):
                    dq.pop()

    return answer
