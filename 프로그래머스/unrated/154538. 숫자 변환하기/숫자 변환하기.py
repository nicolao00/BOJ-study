#1727

def solution(x, y, n):
    answer = 0
    trash=1000000
    dp = [trash]*(y+1)
    dp[x]=0

    for i in range(x,y+1):
        if dp[i]==trash:
            continue
        if i+n <= y:
            dp[i+n]=dp[i]+1 if dp[i+n]>dp[i]+1 else dp[i+n]
        if i*2 <= y:
            dp[i*2]=dp[i]+1 if dp[i*2]>dp[i]+1 else dp[i*2]
        if i*3 <= y:
            dp[i*3]=dp[i]+1 if dp[i*3]>dp[i]+1 else dp[i*3]
    
    answer=-1 if dp[y]==trash else dp[y]
    
    return answer