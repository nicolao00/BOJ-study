#852
from collections import deque
def solution(order):
    idx = 0
    mainBelt = deque([i for i in range(1, len(order)+1)])
    sideBelt = deque()

    while idx < len(order):
        if sideBelt and sideBelt[-1] == order[idx]:
            sideBelt.pop()
            idx += 1
        elif not mainBelt:
            break

        if mainBelt:
            if mainBelt[0] == order[idx]:
                mainBelt.popleft()
                idx += 1
            else:
                sideBelt.append(mainBelt.popleft())

    return idx
