# 918 - 925 / 313
def solution(n):
    answer = []
    board = [[0]*i for i in range(1, n+1)]
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    
    r, c, d = -1, 0, 0
    for value in range(1, (n*(n+1))//2 + 1):
        nr, nc = r + dr[d], c + dc[d]
        # 만약 해당 칸이 0이 아니면 최신화
        if not (0 <= nr < n and 0 <= nc < n) or board[nr][nc] != 0:
            d = (d+1)%3
            nr, nc = r + dr[d], c + dc[d]
        board[nr][nc] = value
        r, c = nr, nc
    
    for lst in board:
        for i in lst:
            answer.append(i)
            
    return answer