import math

def solution(number, limit, power):
    answer = 0
    mem=[]

    for i in range(1,number+1):
        num=0
        for j in range(1,int(math.sqrt(i))+1):
            if i%j==0:
                if i//j==j:
                    num+=1
                else:
                    num+=2
        if num>limit:
            mem.append(power)
        else :
            mem.append(num)
        print(num)
    
    answer=sum(mem)

    return answer