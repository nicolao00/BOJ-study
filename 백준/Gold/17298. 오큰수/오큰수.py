# 125
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = deque()
for i, value in enumerate(arr):
    # 스택에 저장된 값보다 크면 스택에 저장된 값 빼고, 뺀 값이 속한 인덱스에 현재값 저장
    while stack and stack[-1][0] < value:
        _, sIdx = stack.pop()
        arr[sIdx] = value
    stack.append((value, i))

while stack:
    _, i = stack.pop()
    arr[i] = -1

print(*arr)