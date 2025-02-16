# 348 - 408 428
def solution(n, left, right):
    answer = []
    
    while left <= right:
        r = left // n + 1
        c = left % n + 1
        
        answer.append(max(r, c))
        left += 1
        
    return answer