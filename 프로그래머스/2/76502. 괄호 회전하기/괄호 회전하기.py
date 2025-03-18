# 1225
from collections import deque

def solution(s):
    answer = 0

    dq = deque(s)
    for _ in range(len(s)):
        successFlag = True
        stack = deque()
        for value in dq:
            if value == ')':
                if not stack or stack.pop() != '(':
                    successFlag = False
                    break
            elif value == '}':
                if not stack or stack.pop() != '{':
                    successFlag = False
                    break
            elif value == ']':
                if not stack or stack.pop() != '[':
                    successFlag = False
                    break
            else:
                stack.append(value)
        if successFlag and not stack:
            answer += 1

        dq.append(dq.popleft())

    return answer