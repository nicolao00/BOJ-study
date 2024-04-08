# 224-427
import sys

input = sys.stdin.readline

from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# 그룹이 적힌 보드 판
groupBoard = [[0] * N for _ in range(N)]
# 그룹 번호
groupIdx = 1
# 각 그룹에 적힌 칸의 수
numCnt = [0]
# 각 그룹의 숫자
groupNum = [0]
# [그룹번호, 마주치는 그룹번호] = 공유하는 변의 수
shareCnt = dict()


def bfs(r, c):
    # 현재 카운트하고있는 숫자
    curNum = board[r][c]
    dq = deque()
    dq.append((r, c))
    # 현재 카운트하고있는 번호가 몇갠지 센다.
    # 이때 주변이 다른 값이라면 shareCnt += 1 해준다.(두번 체크되니 다 끝나고 /2 해주면 될듯 -> 체크하는걸 visit안에 넣으면 그럴일 없다 !!)
    while dq:
        r, c = dq.popleft()
        for nr, nc in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
            if 0 <= nr < N and 0 <= nc < N:
                newNum = board[nr][nc]
                nGroupIdx = groupBoard[nr][nc]
                # 현재 카운트하고 있는 번호와 같으면 해당칸에 같은 그룹 번호 매기고, 그 번호의 칸 수 카운트 +1
                if not visit[nr][nc] and newNum == curNum:
                    groupBoard[nr][nc] = groupIdx
                    numCnt[groupIdx] += 1
                    dq.append((nr, nc))
                    visit[nr][nc] = True
                # 현재 카운트하고 있는 번호와 다르다고 nr,nc 칸의 그룹도 다를 경우, 현재 카운트하고 있는 번호와 공유하는 변의 수 + 1
                if newNum != curNum and nGroupIdx != 0:
                    if (groupIdx, nGroupIdx) in shareCnt:
                        shareCnt[(groupIdx, nGroupIdx)] += 1
                    elif (nGroupIdx, groupIdx) in shareCnt:
                        shareCnt[(nGroupIdx, groupIdx)] += 1
                    else:
                        shareCnt[(nGroupIdx, groupIdx)] = 1

point = 0
for step in range(4):
    visit = [[False] * N for _ in range(N)]
    groupBoard = [[0] * N for _ in range(N)]
    groupIdx = 1
    numCnt = [0]
    groupNum = [0]
    shareCnt = dict()

    for r in range(N):
        for c in range(N):
            if not visit[r][c]:
                visit[r][c] = True
                numCnt.append(1)
                groupBoard[r][c] = groupIdx
                groupNum.append(board[r][c])
                bfs(r, c)
                groupIdx += 1

    for (g1, g2), cnt in shareCnt.items():
        point += ((numCnt[g1] + numCnt[g2]) * groupNum[g1] * groupNum[g2] * cnt)

    if step == 3: continue
    newBoard = [lst[:] for lst in board]
    half = N // 2
    for i in range(N):
        newBoard[half][i] = board[i][half]
        newBoard[i][half] = board[half][N-i-1]

    for i in range(half):
        for j in range(half):
            newBoard[j][half-i-1] = board[i][j]
            newBoard[j][half + 1 + half - i - 1] = board[i][half + 1 + j]
            newBoard[half + 1 + j][half - i - 1] = board[half + 1 + i][j]
            newBoard[half + 1 + j][half + 1 + half - i - 1] = board[half + 1 + i][half + 1 + j]

    board = newBoard

print(point)