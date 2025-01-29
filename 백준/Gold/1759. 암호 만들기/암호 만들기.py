import sys
from collections import deque

# 839
input = sys.stdin.readline

L, C = map(int, input().split())

words = list(input().split())
words.sort()

mo = set(['a', 'e', 'i', 'o', 'u'])
answer = []
dq = deque()

def dfs(idx):
    if len(dq) >= L:
        str = "".join(dq)
        count = 0;
        for i in range(len(str)):
            if str[i] in mo:
                count += 1

        if count >= 1 and len(dq) - count >= 2:
            answer.append(str)
            answer.append('\n')
        return

    for i in range(idx, C):
        dq.append(words[i])
        dfs(i + 1)
        dq.pop()


dfs(0)
sys.stdout.write("".join(answer))