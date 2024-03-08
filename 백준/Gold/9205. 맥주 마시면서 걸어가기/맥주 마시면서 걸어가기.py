import sys
from collections import deque
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n = int(input())
    hR, hC = map(int, input().split())
    convin = [list(map(int, input().split())) for _ in range(n)]
    gR, gC = map(int, input().split())
    dq = deque([(hR, hC)])

    visit = {(hR, hC): True}
    for r, c in convin:
        visit[(r, c)] = False

    flag = False
    while dq:
        r, c = dq.popleft()
        if abs(r-gR) + abs(c-gC) <= 1000:
            flag = True
            break
        for cR, cC in convin:
            if not visit[(cR, cC)] and abs(r-cR) + abs(c-cC) <= 1000:
                visit[(cR, cC)] = True
                dq.append((cR, cC))
    if flag:
        print("happy")
    else:
        print("sad")


