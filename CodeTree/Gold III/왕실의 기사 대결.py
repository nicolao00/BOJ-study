import sys

input = sys.stdin.readline
from collections import deque

L, N, Q = map(int, input().split())
board = [[2] * (L + 2)]
life, knight, kSize, damage, trapsInKnight = [0], [0], [0], [0] * (N + 1), [0]
commands, moveKnightLst, tmpTrapsInKnight = [], set(), []

for r in range(L):
    board.append([2] + list(map(int, input().split())) + [2])
board.append([2] * (L + 2))

for _ in range(N):
    r, c, h, w, k = map(int, input().split())
    knight.append((r, c))
    life.append(k)
    kSize.append((h, w))
for _ in range(Q):
    commands.append(list(map(int, input().split())))
drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌

# 기사가 차지하는 칸의 트랩 수 저장
for i in range(1, N + 1):
    h, w = kSize[i]
    r, c = knight[i]
    cnt = 0
    for nr in range(r, r + h):
        for nc in range(c, c + w):
            if board[nr][nc] == 1:
                cnt += 1
    trapsInKnight.append(cnt)


def moveKnight(start, d):
    hitKnight = deque()  # 부딫히는 기사 번호
    hitKnight.append(start)
    moveKnightLst.add(start)  # 움직인 기사들
    while hitKnight:
        i = hitKnight.popleft()
        h, w = kSize[i]
        r, c = knight[i]

        wallFlag = False
        nr, nc = r + drdc[d][0], c + drdc[d][1]
        if d == 0:
            for newC in range(nc, nc + w):
                # 트랩 유무
                if board[nr][newC] == 1:
                    tmpTrapsInKnight[i] += 1
                # 벽과 충돌
                elif board[nr][newC] == 2:
                    wallFlag = True
                    break
        elif d == 1:
            for newR in range(nr, nr + h):
                if board[newR][nc + w - 1] == 1:
                    tmpTrapsInKnight[i] += 1
                elif board[newR][nc + w - 1] == 2:
                    wallFlag = True
                    break
        elif d == 2:
            for newC in range(nc, nc + w):
                # 트랩 유무
                if board[nr + h - 1][newC] == 1:
                    tmpTrapsInKnight[i] += 1
                # 벽과 충돌
                elif board[nr + h - 1][newC] == 2:
                    wallFlag = True
                    break
        elif d == 3:
            for newR in range(nr, nr + h):
                if board[newR][nc] == 1:
                    tmpTrapsInKnight[i] += 1
                elif board[newR][nc] == 2:
                    wallFlag = True
                    break

        # 벽이 있으면 False로 바로 반환
        if wallFlag:
            return False

        # 이제 움직였을때 맞닿는 다른 기사 있는지 확인!
        for di in range(1, N + 1):
            if life[di] == 0 or di == i: continue

            dh, dw = kSize[di]
            dr, dc = knight[di]
            if (dr <= nr <= dr + dh - 1) or (nr <= dr <= nr + h - 1):
                if (dc <= nc <= dc + dw - 1) or (nc <= dc <= nc + w - 1):
                    hitKnight.append(di)
                    moveKnightLst.add(di)

    if hitKnight:
        return False
    else:
        return True


slife = life[:]
# 기사 번호, 방향
for i, d in commands:
    # 죽은 기사에게 명령 내리면 패스
    if life[i] == 0: continue

    moveKnightLst = set()
    tmpTrapsInKnight = trapsInKnight[:]
    # 움직였을 경우
    if moveKnight(i, d):
        for num in moveKnightLst:
            r, c = knight[num]
            h, w = kSize[num]
            if d == 0:
                for newC in range(c, c + w):
                    # 트랩 유무
                    if board[r + h - 1][newC] == 1:
                        tmpTrapsInKnight[num] -= 1
            elif d == 1:
                for newR in range(r, r + h):
                    if board[newR][c] == 1:
                        tmpTrapsInKnight[num] -= 1
            elif d == 2:
                for newC in range(c, c + w):
                    # 트랩 유무
                    if board[r][newC] == 1:
                        tmpTrapsInKnight[num] -= 1
            elif d == 3:
                for newR in range(r, r + h):
                    if board[newR][c + w - 1] == 1:
                        tmpTrapsInKnight[num] -= 1

            nr, nc = r + drdc[d][0], c + drdc[d][1]
            knight[num] = (nr, nc)

            if i != num:
                life[num] -= tmpTrapsInKnight[num]
                if life[num] < 0: life[num] = 0

        trapsInKnight = tmpTrapsInKnight

answer = 0
for i in range(1, N + 1):
    if life[i] > 0:
        answer += (slife[i] - life[i])
print(answer)