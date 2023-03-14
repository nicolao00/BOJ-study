def solution(X, Y):
    answer=""
    a = [0]*10
    b = [0]*10
    
    for i in range(len(X)):
        a[int(X[i])]+=1
    
    for i in range(len(Y)): 
        b[int(Y[i])]+=1
    
    for i in range(9,-1,-1):
        while a[i] > 0 and b[i] > 0:
            a[i]-=1
            b[i]-=1
            answer+=str(i)

    if answer=="": return "-1"
    if answer[0]=="0": return "0"
    return answer
