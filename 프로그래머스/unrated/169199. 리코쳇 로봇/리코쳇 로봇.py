# 300
from collections import deque

mv = [(0,1), (1,0), (0,-1), (-1, 0)]


def solution(board):
    answer, lst, dq = -1, [], deque()

    for i,v in enumerate(board):
        startIdx = v.find('R')
        if startIdx != -1:
            dq.append([i, startIdx, 0])
        lst.append(list(v))
    visited = [[0 for _ in range(len(lst[0]))] for _ in range(len(lst))]

    while dq:
        row, col, walk = dq.popleft()
        for mvY, mvX in mv:
            nRow, nCol = row, col
            # 이동 가능한만큼 미끄러져감
            while 0 <= nRow + mvY < len(lst) and 0 <= nCol + mvX < len(lst[0]) and lst[nRow + mvY][nCol + mvX] != 'D':
                    nRow += mvY
                    nCol += mvX
            if nRow == row and nCol == col: continue
            if lst[nRow][nCol] == 'G': return walk + 1
            if visited[nRow][nCol]: continue
            dq.append([nRow, nCol, walk + 1])
            visited[nRow][nCol] = 1

    return answer