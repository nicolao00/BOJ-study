def solution(n, k, enemy):
    answer = 0

    sortE=[0]*len(enemy)
    left=0
    right=len(enemy)
    while left<right:
        mid=(left+right)//2
        total=0
        sortE[0:mid+1]=sorted(enemy[0:mid+1],reverse=True)
        #total=sum(sortE[k:mid+1])
        for i in range(k, mid+1):
            total+=sortE[i]
        if n > total:
            left=mid+1
            answer=mid+1
        elif n < total:
            right=mid
        else: 
            answer=mid+1
            break

    return answer