# 1011
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())


stack = deque()
top = -1
for _ in range(N):
    command = input().split()

    if command[0] == 'push':
        stack.append(int(command[1]))
        top += 1
    elif command[0] == 'pop':
        if top >= 0:
            print(stack.pop())
            top -= 1
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if top >= 0:
            print(0)
        else:
            print(1)
    else:
        if top >= 0:
            print(stack[top])
        else:
            print(-1)