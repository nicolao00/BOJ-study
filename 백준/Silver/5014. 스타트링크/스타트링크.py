import sys
from collections import deque

# 1047
input = sys.stdin.readline

# 총 층수, 현 위치, 목표 지점, 위로 몇칸, 아래로 몇칸
F, S, G, U, D = map(int, input().split())

visit = [False] * (F + 1)
visit[S] = True

dq = deque()

def start():
    while dq:
        current, dist = dq.popleft()
        up = current + U
        down = current - D
        if up == G or down == G:
            print(dist + 1)
            return True

        if up <= F and not visit[up]:
            visit[up] = True
            dq.append((up, dist + 1))

        if down >= 1 and not visit[down]:
            visit[down] = True
            dq.append((down, dist + 1))

    return False

if S == G:
    print(0)
else:
    dq.append((S, 0))
    if not start():
        print("use the stairs")



