from itertools import product

def solution(users, emoticons):
    answer = [0,0]
    expense=[0]*len(users) # 구매액 저장할 리스트
    for percArr in product([10,20,30,40], repeat=len(emoticons)):   # 물건마다의 할인액 중복 순열
        for i in range(len(emoticons)):
            for userIdx, userInfo in enumerate(users):            
                if userInfo[0]<=percArr[i]:
                    expense[userIdx]+=emoticons[i]*((100-percArr[i])/100)
        subsc=0
        total=0         
        for userIdx, userInfo in enumerate(users):
            if userInfo[1]<=expense[userIdx]:
                subsc+=1    
            else:
                total+=expense[userIdx]
            expense[userIdx]=0

        if subsc>answer[0]:
            answer[0]=subsc
            answer[1]=int(total)
        elif subsc==answer[0] and total>answer[1]:
            answer[1]=int(total)

    return answer