import sys
from collections import deque

input = sys.stdin.readline

# 1100

# 톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전
T = int(input())

wheels = [[0]] + [deque(map(int, input().rstrip())) for _ in range(T)]
right, left = 2, 6

def leftRotate(wheelNum, direct):
    if wheelNum == 1:
        return
    if wheels[wheelNum][left] != wheels[wheelNum-1][right]:
        leftRotate(wheelNum-1, -1*direct)
        wheels[wheelNum-1].rotate(-1*direct)

def rightRotate(wheelNum, direct):
    if wheelNum == T:
        return
    if wheels[wheelNum][right] != wheels[wheelNum+1][left]:
        rightRotate(wheelNum+1, -1*direct)
        wheels[wheelNum+1].rotate(-1*direct)

K = int(input())
for _ in range(K):
    wheelNum, direct = map(int, input().split())

    leftRotate(wheelNum, direct)
    rightRotate(wheelNum, direct)
    wheels[wheelNum].rotate(direct)

answer = 0
for i in range(1,T + 1):
    if wheels[i][0] == 1:
        answer += 1
print(answer)