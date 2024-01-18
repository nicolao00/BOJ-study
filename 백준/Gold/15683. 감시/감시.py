# 305
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
initBoard = [list(map(int, input().split())) for _ in range(N)]
drdc = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]
cctvlst = []
initEmpty = 0


def fillEmpty(board, result, cnt):
    global answer

    if cnt == len(cctvlst):
        answer = min(answer, result)
        return

    arr = []
    r, c = cctvlst[cnt]
    if board[r][c] == 1:
        arr = [[0], [1], [2], [3]]
    elif board[r][c] == 2:
        arr = [[0, 2], [1, 3]]
    elif board[r][c] == 3:
        arr = [[0, 1], [1, 2], [2, 3], [3, 0]]
    elif board[r][c] == 4:
        arr = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]
    elif board[r][c] == 5:
        arr = [[0, 1, 2, 3]]

    for case in arr:
        boardTmp = [tmp[:] for tmp in board]
        tmpResult = result
        for idx in case:
            dr, dc = drdc[idx]
            nr, nc = r + dr, c + dc
            while (0 <= nr < N and 0 <= nc < M and boardTmp[nr][nc] != 6):
                if boardTmp[nr][nc] == 0:
                    boardTmp[nr][nc] = -1
                    tmpResult -= 1
                nr += dr
                nc += dc
        fillEmpty(boardTmp, tmpResult, cnt + 1)




for r in range(N):
    for c in range(M):
        if initBoard[r][c] == 0:
            initEmpty += 1
        elif initBoard[r][c] != 6:
            cctvlst.append((r, c))

answer = initEmpty
fillEmpty([arr[:] for arr in initBoard], initEmpty, 0)
print(answer)