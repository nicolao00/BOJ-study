# 537-642 / 809

import sys
input = sys.stdin.readline
from collections import defaultdict

# n은 격자의 크기, m은 플레이어의 수, k는 라운드의 수
n, m, k = map(int, input().split())
# 총의 위치가 담긴 보드
gboard = defaultdict(list)
for r in range(n):
    for c, v in enumerate(list(map(int, input().split()))):
        if v > 0:
            gboard[(r, c)].append(v)
# (x, y)는 플레이어의 위치, d는 방향, s는 플레이어의 초기 능력치
players = [list(map(int, input().split())) for _ in range(m)]
# 플레이어 위치가 담길 보드
pboard = [[-1]*n for _ in range(n)]
for pIdx, (r, c, d, s) in enumerate(players):
    players[pIdx][0], players[pIdx][1] = r-1, c-1
    pboard[r-1][c-1] = pIdx
# 플레이어가 소유한 총의 능력치
playersGun = [0]*m
# 플레이어가 획득한 점수
playersScore = [0]*m
drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# 어차피 한 칸에 총은 가장 큰 총만 남겨두면 돼서 한칸에는 가장 큰 총 하나만 저장하고 있으면 됨!!!!

# 사람 이동
def movePerson(pIdx):
    r, c, d, s = players[pIdx]
    nr, nc = r + drdc[d][0], c + drdc[d][1]
    if not (0 <= nr < n and 0 <= nc < n):
        d = (d + 2) % 4
        players[pIdx][2] = d
        nr, nc = r + drdc[d][0], c + drdc[d][1]
    # 일단 움직인 사람 위치 비워놓음 (이동완료되면 채워야함!)
    pboard[r][c] = -1

    # 2. 플레이어가 없다면
    if pboard[nr][nc] == -1:
        # 해당 칸에 총이 있는지 확인
        if (nr, nc) in gboard:
            # 바닥의 총 교환할지 결정
            swapGun(pIdx, nr, nc)
        pboard[nr][nc] = pIdx
        players[pIdx][0], players[pIdx][1], players[pIdx][2] = nr, nc, d

        # 2-1 만약 이동한 방향에 플레이어가 있는 경우에는 두 플레이어가 싸움 (해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교)
    else:
        fight(pIdx, nr, nc)

    # 이동한 사람의 위치 저장해줘야함 (마지막에 하자)
    # players와 pboard 둘다 변경해줘야함.
    # 총 바꾼 것도 적용해야함.



# 바닥에 있는 총과 교환
def swapGun(pIdx, r, c):
    if (r, c) not in gboard:
        return
    if gboard[(r, c)][-1] > playersGun[pIdx]:
        tmp = gboard[(r, c)][-1]
        if playersGun[pIdx] > 0:
            gboard[(r,c)][-1] = playersGun[pIdx]
            gboard[(r,c)].sort()
        else:
            gboard[(r,c)].pop()
            if len(gboard[(r,c)]) == 0:
                gboard.pop((r, c))
        playersGun[pIdx] = tmp


# 플레이어 대결
def fight(pIdx, r, c):
    newPidx = pboard[r][c]
    winPlayer, losePlayer = -1, -1
    if playersGun[newPidx] + players[newPidx][3] > playersGun[pIdx] + players[pIdx][3]:
        winPlayer, losePlayer = newPidx, pIdx
    elif playersGun[pIdx] + players[pIdx][3] > playersGun[newPidx] + players[newPidx][3]:
        winPlayer, losePlayer = pIdx, newPidx
    else:
        if players[newPidx][3] > players[pIdx][3]:
            winPlayer, losePlayer = newPidx, pIdx
        elif players[pIdx][3] > players[newPidx][3]:
            winPlayer, losePlayer = pIdx, newPidx
    playersScore[winPlayer] += abs(playersGun[newPidx] + players[newPidx][3]-(playersGun[pIdx] + players[pIdx][3]))

    # 2-2-2. 진 플레이어는 본인이 가지고 있는 총을 해당 격자에 내려놓고, 해당 플레이어가 원래 가지고 있던 방향대로 한 칸 이동합니다. 만약 이동하려는 칸에 다른 플레이어가 있거나 격자 범위 밖인 경우에는 오른쪽으로 90도씩 회전하여 빈 칸이 보이는 순간 이동합니다. 만약 해당 칸에 총이 있다면, 해당 플레이어는 가장 공격력이 높은 총을 획득하고 나머지 총들은 해당 격자에 내려 놓습니다.
    if playersGun[losePlayer] != 0:
        gboard[(r,c)].append(playersGun[losePlayer])
        gboard[(r,c)].sort()
        playersGun[losePlayer] = 0
    for i in range(4):
        nd = (players[losePlayer][2] + i) % 4
        nr, nc = r + drdc[nd][0], c + drdc[nd][1]
        if 0 <= nr < n and 0 <= nc < n and pboard[nr][nc] == -1:
            pboard[nr][nc] = losePlayer
            players[losePlayer][0], players[losePlayer][1] = nr, nc
            players[losePlayer][2] = ((players[losePlayer][2] + i) % 4)
            if (nr, nc) in gboard:
                playersGun[losePlayer] = gboard[(nr, nc)][-1]
                gboard[(nr, nc)].pop()
                if len(gboard[(nr, nc)]) == 0:
                    gboard.pop((nr, nc))
            players[losePlayer][2] = nd
            break

    # 2-2-3. 이긴 플레이어는 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득하고, 나머지 총들은 해당 격자에 내려 놓습니다.
    swapGun(winPlayer, r, c)
    players[winPlayer][0], players[winPlayer][1] = r, c
    pboard[r][c] = winPlayer


for _ in range(k):
    # 1. 본인이 향하고 있는 방향대로 한 칸만큼 이동 (격자를 벗어나는 경우에는 정반대 방향)
    for pIdx in range(len(players)):
        movePerson(pIdx)
print(*playersScore)