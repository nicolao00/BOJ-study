# 306 -347
from collections import deque
import heapq
def solution(board):
    answer = 1e9
    visit = [[[1e9] * len(board) for _ in range(len(board))] for _ in range(4)]
    visit[0][0][0] = visit[1][0][0] = visit[2][0][0] = visit[3][0][0] = 0
    hq = []
    # r, c, weight, direct(상,우,하,좌)
    heapq.heappush(hq, (0, 0, 0, -1))
    while hq:
        weight, r, c, direct = heapq.heappop(hq)
        for curDirect, (nr, nc) in enumerate([(r-1, c), (r, c+1), (r+1, c), (r, c-1)]):
            if 0 <= nr < len(board) and 0 <= nc < len(board) and not board[nr][nc]:
                curWeight = weight + 6
                
                # 직선인 경우
                if direct == -1 or direct == curDirect or (direct+2)%4 == curDirect:
                    curWeight = weight + 1
                
                # 도착
                if nr == len(board)-1 and nc == len(board)-1:
                    answer = min(answer, curWeight)
                    visit[curDirect][nr][nc] = curWeight
                    
                # 기존 경로보다 짧으면
                elif curWeight <= visit[curDirect][nr][nc]:
                    heapq.heappush(hq, (curWeight, nr, nc, curDirect))
                    visit[curDirect][nr][nc] = curWeight
                
    return answer*100

# # 가중치를 +1이 아닌 직선, 코너에 따라 다르게 주면 됨 100, 500
# 0 0 0 0 0
# 0 1 1 1 0
# 0 0 1 0(17) 0
# 1 0 0 0 1
# 1 1 1 0 0