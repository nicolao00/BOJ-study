
def solution(storey):
    answer = 0
    
    while storey:
        storey, step=divmod(storey,10)
        if step > 5 or (step==5 and storey%10>=5):
            storey+=1
            answer+=10-step
        else:
            answer+=step
    return answer

