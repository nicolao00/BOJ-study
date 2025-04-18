import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    visit = [[[False]*C for _ in range(R)] for _ in range(L)]
    sf, sr, sc = start
    visit[sf][sr][sc] = True
    dq = deque([[sf, sr, sc, 0]])
    while dq:
        f, r, c, d = dq.popleft()
        for df, dr, dc in [(0,0,1), (0,1,0), (0,-1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]:
            nf, nr, nc = f + df, r + dr, c + dc
            if end == (nf, nr, nc):
                print("Escaped in %d minute(s)."%(d + 1))
                return
            if 0 <= nf < L and 0 <= nr < R and 0 <= nc < C and not visit[nf][nr][nc] and board[nf][nr][nc] == '.':
                visit[nf][nr][nc] = True
                dq.append((nf, nr, nc, d + 1))
    print("Trapped!")

while(1):
    L, R, C = map(int, input().split())
    start, end = 0, 0
    if L + R + C == 0: break
    board = []
    for floor in range(L):
        tFloor = []
        for row in range(R):
            tmp = list(input().rstrip())
            for col, value in enumerate(tmp):
                if value == 'S':
                    start = (floor, row, col)
                elif value == 'E':
                    end = (floor, row, col)
            tFloor.append(tmp)
        board.append(tFloor)
        input().rstrip()

    bfs(start, end)