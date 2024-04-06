# 1224 - 149 / 125 - 227 / 825
import sys
from collections import defaultdict

input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [[101] * (N + 2)]
for _ in range(N):
    board.append([101] + list(map(int, input().split())) + [101])
board.append([101] * (N + 2))
people = [tuple(map(int, input().split())) for _ in range(M)]
finish = [False] * M
finishCnt = 0
movement = 0
dist = [1e9] * M
goal = tuple(map(int, input().split()))

# 거리 초기설정
for peopleIdx, (r, c) in enumerate(people):
    dist[peopleIdx] = abs(goal[0] - r) + abs(goal[1] - c)

for _ in range(K):
    # 사람들 이동
    for peopleIdx, (r, c) in enumerate(people):
        if finish[peopleIdx]: continue
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 1 <= nr <= N and 1 <= nc <= N and board[nr][nc] == 0:
                # 탈출하는 경우
                if (nr, nc) == goal:
                    finish[peopleIdx] = True
                    finishCnt += 1
                    people[peopleIdx] = (nr, nc)
                    break

                tmp = abs(goal[0] - nr) + abs(goal[1] - nc)
                if tmp < dist[peopleIdx]:
                    dist[peopleIdx] = tmp
                    people[peopleIdx] = (nr, nc)
        # 움직임이 있는 경우
        if (r, c) != people[peopleIdx]:
            movement += 1
    # 사람이 모두 탈출
    if finishCnt == M:
        break


    # 가장 작은 정사각형의 우하단 좌표 구하기
    def findSquare(r, c, length):
        nr, nc = max(r, goal[0]), max(c, goal[1])
        sr = nr - length
        sc = nc - length
        if sr <= 0:
            nr += abs(sr) + 1
        if sc <= 0:
            nc += abs(sc) + 1
        return (nr, nc)


    # 가장 작은 정사각형 잡기
    target = 0
    targetLen = 1e9
    for peopleIdx, (r, c) in enumerate(people):
        if finish[peopleIdx]: continue
        length = max(abs(r - goal[0]), abs(c - goal[1]))

        if length < targetLen:
            target = findSquare(r, c, length)
            targetLen = length
        elif length == targetLen:
            tmpRC = findSquare(r, c, length)
            if tmpRC < target:
                target = tmpRC
                targetLen = length

    smallR, smallC = target[0] - targetLen, target[1] - targetLen
    bigR, bigC = target
    # 탈출 못한 사람 위치들을 딕셔너리로 저장
    locations = defaultdict(list)
    for peopleIdx, (r, c) in enumerate(people):
        if finish[peopleIdx]: continue
        locations[(r, c)].append(peopleIdx)
    # 사각형 회전
    changedPeople = []
    changeGoal = False
    changeBoard = [lst[:] for lst in board]
    exGoal = goal
    for dr in range(bigR - smallR + 1):
        for dc in range(bigC - smallC + 1):
            exR, exC = smallR + dr, smallC + dc
            nr, nc = smallR + dc, bigC - dr
            changeBoard[nr][nc] = board[exR][exC]
            # 이전 위치가 벽이였을 경우
            if board[exR][exC] > 0:
                changeBoard[nr][nc] -= 1
            # 이전 위치에 사람이 있었을 경우
            elif (exR, exC) in locations:
                for peopleIdx in locations[(exR, exC)]:
                    if finish[peopleIdx]: continue
                    people[peopleIdx] = (nr, nc)
                    changedPeople.append(peopleIdx)
            # 이전 위치가 목표지점이였을 경우
            elif (exR, exC) == exGoal:
                goal = (nr, nc)
                changeGoal = True
    if changeGoal:
        for peopleIdx, (r, c) in enumerate(people):
            if finish[peopleIdx]: continue
            dist[peopleIdx] = abs(goal[0] - r) + abs(goal[1] - c)
    # 이동된 사람의 dist 변경해줌
    else:
        for peopleIdx in changedPeople:
            dist[peopleIdx] = abs(goal[0] - people[peopleIdx][0]) + abs(goal[1] - people[peopleIdx][1])
    board = changeBoard

print(movement)
print(*goal)