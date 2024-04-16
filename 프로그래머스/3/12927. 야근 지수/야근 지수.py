# 929
import heapq

def solution(n, works):
    answer = 0
    pq = []
    if n >= sum(works):
        return answer
    
    for w in works:
        heapq.heappush(pq, -w)
    
    for i in range(n):
        result = heapq.heappop(pq)+1
        if result != 0:
            heapq.heappush(pq, result)
        
    while pq:
        answer += heapq.heappop(pq)**2
    return answer