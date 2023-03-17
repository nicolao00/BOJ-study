def solution(food):
    answer = ''
    for idx, val in enumerate(food):
        for i in range(val//2):
            answer+=str(idx)
    answer=answer + "0" + "".join(reversed(answer))

    return answer
