import sys
input = sys.stdin.readline

# 1016
N = int(input())
board = list(map(int, input().split()))
goal = int(input())
answer = 0

board.sort()
left, right = 0, N-1
while left < right:
    result = board[left] + board[right]
    if result > goal:
        right -= 1
    elif result < goal:
        left += 1
    else:
        answer += 1
        right -= 1
        left += 1
print(answer)