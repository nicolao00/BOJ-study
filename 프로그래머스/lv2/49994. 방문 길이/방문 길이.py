#640
from collections import defaultdict
def solution(dirs):
    answer = 0
    # 좌측하단이 0,0
    mv = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    visited = defaultdict(list)
    row, col = 5, 5
    for direct in dirs:
        nRow, nCol = row, col
        nRow += mv[direct][0]
        nCol += mv[direct][1]
        if not (0 <= nRow <= 10 and 0 <= nCol <= 10): continue
        visited[(nRow, nCol)]
        if (row, col) not in visited[(nRow, nCol)]:
            visited[(nRow, nCol)].append((row, col))
            visited[(row, col)].append((nRow, nCol))
        row, col = nRow, nCol

    for i in visited.values(): answer += len(i)
    return answer//2