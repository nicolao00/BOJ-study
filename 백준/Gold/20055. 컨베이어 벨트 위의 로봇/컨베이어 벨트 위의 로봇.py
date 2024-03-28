# 1006
import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
tmp = list(map(int, input().split()))
tmp.reverse()
life = deque(tmp)
exist = deque([False] * 2*N)

answer = 0
dq = deque()
while K > 0:
    answer += 1
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    life.append(life.popleft())
    exist.append(exist.popleft())

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for _ in range(len(dq)):
        curLoc = dq.popleft() - 1
        if curLoc < 0:
            curLoc = 2*N-1
        elif curLoc == N:
            exist[curLoc] = False
            continue
        nextLoc = curLoc - 1
        if nextLoc < 0: nextLoc = 2*N-1

        # 이동 못하는 경우 ( 다음 칸이 내구도 닳았거나, 다음 칸에 로봇이 있거나,
        if life[nextLoc] < 1 or exist[nextLoc]:
            dq.append(curLoc)
            continue

        # 이동함
        # 내리는 위치
        life[nextLoc] -= 1
        exist[curLoc] = False
        if nextLoc != N:
            dq.append(nextLoc)
            exist[nextLoc] = True

        if life[nextLoc] == 0:
            K -= 1


    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다. (올릴 칸 내구도 있고 and 올릴 칸에 로봇 없고)
    if life[2*N-1] >= 1 and not exist[2*N-1]:
        dq.append(2*N-1)
        exist[2*N-1] = True
        life[2*N-1] -= 1
        if life[2*N-1] == 0:
            K -= 1

print(answer)