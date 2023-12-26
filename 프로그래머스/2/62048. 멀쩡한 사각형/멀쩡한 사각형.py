import math

def solution(w, h):
    answer = w * h
    
    exY = 0
    
    if w == h:
        return answer - w
    
    if w == 1 or h == 1:
        return 0
    
    for i in range(1, w+1):
        Y = h*i/w
        answer -= math.ceil(Y) - exY
        exY = math.floor(Y)
    return answer