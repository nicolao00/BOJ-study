from collections import deque
def solution(numbers):
    answer = deque()
    dq = deque(numbers)
    large = deque()
    while dq:
        temp = dq.pop()
        while large and temp >= large[-1]:
            large.pop()
        if large:
            answer.append(large[-1])
        else:
            answer.append(-1)
        large.append(temp)

    return list(reversed(answer))