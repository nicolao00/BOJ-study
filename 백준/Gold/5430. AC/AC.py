import sys
from collections import deque

# 1154
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    funcList = input().rstrip()
    N = int(input())
    arr = input().rstrip().split(',')
    if len(arr) > 1:
        arr[0] = arr[0][1:]
        arr[-1] = arr[-1][:-1]
    else:
        arr[0] = arr[0][1:len(arr[0])-1]

    dq = deque(arr)
    reverseFlag = False
    errorFlag = False
    for char in funcList:
        if char == 'D':
            if not dq or dq[0] == '':
                errorFlag = True
                break

            elif reverseFlag:
                dq.pop()
            else:
                dq.popleft()
        else:
            reverseFlag = not reverseFlag

    if errorFlag:
        print("error")
        continue
    if reverseFlag:
        dq.reverse()
        print("[" + ",".join(dq) + "]")
    else:
        print("[" + ",".join(dq) + "]")