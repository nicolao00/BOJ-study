# 926
def solution(diffs, times, limit):
    answer = 0
    
    def calculateTime(level):
        time = 0
        for i in range(len(diffs)):
            leveldiff = diffs[i] - level
            time += times[i]
            
            # 난이도가 더 높은 경우
            if leveldiff > 0:
                time += (times[i] + times[i-1]) * leveldiff 
        return time
                
    left, right = 1, 1000000000000001
    while left <= right:
        mid = (left + right) // 2
        result = calculateTime(mid)
        
        # 현재 숙련도로 충분히 클리어
        if result <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1            
            
    return answer