#539
from collections import deque

change = [[0,1], [1,0], [-1,0], [0,-1]]
def solution(maps):
    dq = deque()
    totalRow, totalCol = len(maps), len(maps[0])
    # 해당 칸에 가기 위한 가장 짧은 거리를 저장하는 dist
    dist = [[99999] * totalCol for _ in range(totalRow)]
    dist[0][0] = 1
    dq.append((0,0))
    while dq:
        row, col = dq.popleft()
        weight = dist[row][col]
        for cRow, cCol in change:
            nRow = cRow + row
            nCol = cCol + col
            if 0 <= nRow < totalRow and 0 <= nCol < totalCol and maps[nRow][nCol] and weight + 1 < dist[nRow][nCol]:
                # 해당 칸이 벽이 아니고 and 지금 가는 경로가 해당 칸을 가는 최적의 경로인 경우만 queue에 저장
                dist[nRow][nCol] = weight + 1
                dq.append((nRow, nCol))

    if dist[totalRow - 1][totalCol - 1] == 99999:
        return -1
    answer = dist[totalRow - 1][totalCol - 1]
    return answer