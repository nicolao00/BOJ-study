# 1803
def solution(n, m, section):
    answer = 0
    location=0
    for i in range(len(section)):
        if location<section[i]:
            location=section[i]+m-1
            answer+=1
    return answer