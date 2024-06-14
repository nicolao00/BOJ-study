# 1150
import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]
dr = [0, 1, 1, 1, 0]
dc = [-1, -1 ,0, 1, 1]


def dfs(r, c, d, color, cnt):
    if cnt == 6:
        return cnt
    nr, nc = r + dr[d], c + dc[d]
    if 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == color:
        return dfs(nr, nc, d, color, cnt + 1)
    return cnt

def main():
    for r in range(19):
        for c in range(19):
            if board[r][c] != 0:
                for i in range(5):
                    # 끝점이 아닐때
                    if 0 <= r+dr[i] < 19 and 0 <= c+dc[i] < 19 and 0 <= r-dr[i] < 19 and 0 <= c-dc[i] < 19 and board[r+dr[i]][c+dc[i]] == board[r-dr[i]][c-dc[i]]:
                        continue

                    if dfs(r, c, i, board[r][c], 1) == 5:
                        print(board[r][c])
                        print(*reversed(min((c+1, r+1), (c+dc[i]*4+1, r+dr[i]*4+1))))
                        return 0
    print(0)

main()