# 1015
def solution(k, m, score):        
    answer = 0
    appleCnt = [0 for i in range(k+1)]
    for i in score:
        appleCnt[i] += 1
    
    cnt = 0
    i = k
    while i > 0:
        if(appleCnt[i]):
            appleCnt[i] -= 1
            cnt += 1
        else :
            i-=1
        if(cnt == m):
            answer += (i * m)
            cnt = 0

    return answer


# 배열 