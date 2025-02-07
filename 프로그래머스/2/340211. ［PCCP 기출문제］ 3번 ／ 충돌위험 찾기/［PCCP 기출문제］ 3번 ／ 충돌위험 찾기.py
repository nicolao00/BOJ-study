# 925
from collections import deque


def solution(points, routes):
    answer = 0

    dq = deque()
    visit = set()
    visitAgain = set()
    for i, num in enumerate(routes):
        # 로봇 번호, 다음에 도달한 포인트의 idx(번호 아님), 현재 좌표
        dq.append([i, 1, points[num[0] - 1][0], points[num[0] - 1][1]])
        # 충돌 발생
        if (points[num[0] - 1][0], points[num[0] - 1][1]) in visit:
            visitAgain.add((points[num[0] - 1][0], points[num[0] - 1][1]))
        else:
            visit.add((points[num[0] - 1][0], points[num[0] - 1][1]))
    answer += len(visitAgain)

    # 더이상 남은 로봇이 없을 때까지
    while dq:
        robotCnt = len(dq)
        visit = set()
        visitAgain = set()

        # 현재 시점에서의 존재하는 로봇 모두 이동
        for i in range(robotCnt):
            robotNum, nextPointIdx, r, c = dq.popleft()
            nr, nc = r, c

            nextPoint = points[routes[robotNum][nextPointIdx] - 1]
            if nextPoint[0] > r:
                nr += 1
            elif nextPoint[0] < r:
                nr -= 1
            elif nextPoint[1] > c:
                nc += 1
            elif nextPoint[1] < c:
                nc -= 1

            # 목적지 도달
            if nextPoint[0] == nr and nextPoint[1] == nc:
                # 종점에 도달한 로봇은 패스
                if len(routes[robotNum]) > nextPointIdx + 1:
                    dq.append([robotNum, nextPointIdx + 1, nr, nc])
            else:
                dq.append([robotNum, nextPointIdx, nr, nc])

            #충돌 발생
            if (nr, nc) in visit:
                visitAgain.add((nr, nc))
            else:
                visit.add((nr, nc))
        answer += len(visitAgain)

    return answer