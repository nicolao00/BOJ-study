# 329
import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
base = dict()
# 각 idx의 플레이어가 가야하는 편의점 위치
store = [0] * (m + 1)
player = [0] * (m + 1)
# 끝난 플레이어
finish = [False] * (m + 1)
board = [[-1] * (n + 2)]
# 편의점 움직임이 끝나면 이동 불가한 칸
cantMoveStore = []
# 입주 움직임이 끝나면 이동 불가한 칸
cantMoveBase = []
for r in range(n):
    tmp = list(map(int, input().split()))
    for c, v in enumerate(tmp):
        if v == 1:
            base[(r + 1, c + 1)] = False
    board.append([-1] + tmp + [-1])
board.append([-1] * (n + 2))

for i in range(1, m + 1):
    store[i] = tuple(map(int, input().split()))
time = 0
playerCnt = m


# [1] 사람들 편의점으로 이동
def moveStore(peopleIdx):
    global playerCnt
    r, c = player[peopleIdx]
    dist = 1e9
    candi = (r, c)
    for nr, nc in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
        if board[nr][nc] != -1:
            if (nr, nc) == store[peopleIdx]:
                candi = (nr, nc)
                break
            tmp = calDist((nr, nc), store[peopleIdx])
            if tmp < dist:
                dist = tmp
                candi = (nr, nc)

    player[peopleIdx] = candi
    # 편의점에 도착했다면
    if player[peopleIdx] == store[peopleIdx]:
        finish[peopleIdx] = True
        playerCnt -= 1
        cantMoveStore.append(candi)


# [3] 베이스 캠프 입성
def goToBase(peopleIdx):
    dist = 1e9
    candiBase = (1e9, 1e9)
    for baseRC, used in base.items():
        # 이미 사용된 베이스면 패스
        if used: continue
        result = calDist(baseRC, store[peopleIdx])
        if result < dist or (result == dist and baseRC < candiBase):
            candiBase = baseRC
            dist = result

    base[candiBase] = True
    player[peopleIdx] = candiBase
    cantMoveBase.append(candiBase)


# 최단거리 반환
def calDist(baseRC, goal):
    r, c = baseRC
    gr, gc = goal
    dq = deque()
    dq.append((r, c, 0))
    visit = [[False] * (n + 2) for _ in range(n + 2)]
    visit[r][c] = True

    while dq:
        r, c, d = dq.popleft()
        for nr, nc in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
            if nr == gr and nc == gc:
                return d + 1
            if board[nr][nc] != -1 and not visit[nr][nc]:
                visit[nr][nc] = True
                dq.append((nr, nc, d + 1))
    return 1e9

# 플레이어들 다 입성할때까지 반복
while time < m:
    time += 1
    cantMoveStore = []
    cantMoveBase = []

    for playerIdx in range(1, time):
        # 이미 도착한 사람이면 패스
        if finish[playerIdx]: continue
        # [1] 사람들 편의점으로 이동
        # [2] 편의점 도착 시 그 칸 통행 불가
        moveStore(playerIdx)

    # 편의점 이동 후 이동 불가된 칸 적용
    for r,c in cantMoveStore:
        board[r][c] = -1

    # [3] 베이스 캠프 입성 (입성 후 격자안 사람 모두 이동 후부터 통행 불가)
    goToBase(time)

    # 캠프 입성 후 이동 불가된 칸 적용
    for r, c in cantMoveBase:
        board[r][c] = -1


# 플레이가 전부 도착할때까지 반복
while playerCnt > 0:
    time += 1
    cantMoveStore = []

    for peopleIdx in range(1, m+1):
        if finish[peopleIdx]: continue
        moveStore(peopleIdx)

    if playerCnt == 0: break

    # 이동 불가된 칸 적용
    for r, c in cantMoveStore:
        board[r][c] = -1

print(time)