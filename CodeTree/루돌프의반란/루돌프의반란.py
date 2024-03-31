# 645(700) - 847 / 912


import sys
input = sys.stdin.readline

N, M, P, C, D = map(int, input().split())
rodulf = list(map(int, input().split()))
santa = dict()
board = [[0]*(N+1) for _ in range(N+1)] # 0: 빈칸 / 1~30: 산타 / 31: 루돌프
movement = [(-1, 0), (0, 1), (1, 0), (0, -1)]
outSanta = set()
outTmp = set()
for _ in range(P):
     n, r, c = map(int, input().split())
     santa[n] = [r, c]

for i, v in santa.items():
    board[v[0]][v[1]] = i
board[rodulf[0]][rodulf[1]] = 31

# 산타별 점수, 기절 지속 시간
score, stun = [0] * (P+1), [1001] * (P+1)

def calculDist(r, c):
    return (r-rodulf[0])**2 + (c-rodulf[1])**2

# 가까운 산타 번호 찾기
def nearSanta():
    dist = 1e9
    nearstS = -1
    for i, s in santa.items():
        if i in outSanta: continue
        tmp = calculDist(s[0], s[1])
        if dist >= tmp:
            # 거리가 같은 산타가 여럿일때
            if dist == tmp:
                if santa[nearstS] > s:
                    continue
            dist = tmp
            nearstS = i
    return nearstS


# 가까운 산타에게 이동
def moveRodol(nearS):
    drdc = [0, 0]
    board[rodulf[0]][rodulf[1]] = 0
    for i in range(2):
        if rodulf[i] > santa[nearS][i]:
            rodulf[i] -= 1
            drdc[i] -= 1
        elif rodulf[i] < santa[nearS][i]:
            rodulf[i] += 1
            drdc[i] += 1

    # 충돌 확인
    if 1 <= board[rodulf[0]][rodulf[1]] <= 30:
        hitedSanta = board[rodulf[0]][rodulf[1]]
        stun[hitedSanta] = M-1
        score[hitedSanta] += C

        hit(drdc, hitedSanta, C)

    # 루돌프 이동
    board[rodulf[0]][rodulf[1]] = 31


# 밀려나는 경우
def hit(drdc, hitedSanta, moveDist):
    # 충돌한 산타 날아감
    for _ in range(moveDist):
        for i in range(2):
            santa[hitedSanta][i] += drdc[i]
    nr, nc = santa[hitedSanta]

    # 장외된 산타 삭제
    if not (1 <= nr <= N and 1 <= nc <= N):
        outTmp.add(hitedSanta)
        return

    # 날아간 위치에 이미 산타가 있을 때
    if 1 <= board[nr][nc] <= 30:
        tmp = board[nr][nc]
        board[nr][nc] = hitedSanta
        hit(drdc, tmp, 1)
    else:
        board[nr][nc] = hitedSanta


# 산타 이동
def moveSanta():
    for key in range(1, P+1):
        [r, c] = santa[key]
        if key in outSanta: continue
        if stun[key] <= M: continue

        # candi: 이동방향
        candi = []
        dist = calculDist(r, c)
        for i, drdc in enumerate(movement):
            nr, nc = r + drdc[0], c + drdc[1]
            # 산타는 다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없습니다.
            if 1 <= nr <= N and 1 <= nc <= N and not (1 <= board[nr][nc] <= 30):
                # 루돌프와 충돌
                if board[nr][nc] == 31:
                    candi = [i, nr, nc]
                    break
                else:
                    tmp = calculDist(nr, nc)
                    if dist > tmp:
                        dist = tmp
                        candi = [i, nr, nc]

        # 이동할 곳이 있으면
        if candi:
            i, nr, nc = candi
            santa[key] = [nr, nc]
            board[r][c] = 0
            # 루돌프와 충돌
            if board[nr][nc] == 31:
                stun[key] = M - 1
                score[key] += D
                hit(movement[(i+2) % 4], key, D)
            else:
                board[nr][nc] = key


while M:
    outTmp = set()
    # 가까운 산타 찾기
    nearS = nearSanta()
    if nearS == -1:
        break
    # 가까운 산타에게 이동
    moveRodol(nearS)
    # 산타 이동
    moveSanta()


    if len(outSanta) == P:
        break

    outSanta.update(outTmp)
    # 살아남은 산타 +1점
    for i in santa.keys():
        if i in outSanta: continue
        score[i] += 1
    M -= 1
print(' '.join(map(str, score[1:])))
# 루돌프 이동 (가장 가까운 산타에게 8방향 1칸 이동)

# 산타 이동 (루돌프에게 가까이 갈 수 있으면 4방향 1칸 이동 // 기절도 고려)

# 충돌 (누가 박았냐에 따라 다름. / 밀려난 위치에 따라 1. 아웃, 2. 상호작용 발생 / 기절 적용)

# 매턴 탈락 안한 산타 + 1점