# 1009
from collections import deque
def solution(queue1, queue2):
    answer = 0
    sums = [sum(queue1), sum(queue2)]
    goal = sum(sums)//2
    if sum(sums)%2 != 0:
        return -1

    dq = [deque(queue1), deque(queue2)]
    big, small = 0, 0
    while sums[0] != sums[1] and answer <= 600000:
        if sums[0] > sums[1]:
            big, small = 0, 1
        elif sums[0] < sums[1]:
            big, small = 1, 0
        if dq[big][0] > goal:
            return -1

        tmp = dq[big].popleft()
        sums[big] -= tmp
        sums[small] += tmp
        dq[small].append(tmp)
        answer += 1

    if answer == 600001:
        return -1
    return answer