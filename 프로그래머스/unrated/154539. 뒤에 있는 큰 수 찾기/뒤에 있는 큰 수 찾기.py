
def solution(numbers):
    answer=[-1]*len(numbers)
    for i in range(len(numbers)-1, -1, -1):
        for j in range(i-1, -1, -1):
            if numbers[i] <= numbers[j]: break
            answer[j] = numbers[i]
            
    return answer
                   