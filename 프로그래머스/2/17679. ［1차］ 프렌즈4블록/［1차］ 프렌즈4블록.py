answer = 0
def solution(m, n, b):
    board = [list(lst) for lst in b]

    def check_board(r, c):
        value = board[r][c]
        if value == "0":
            return False
        for nr in range(r, r + 2):
            for nc in range(c, c + 2):
                if value != board[nr][nc]:
                    return False

        return True

    def delete_points(popPoints):
        global answer

        for r, c in popPoints:
            for nr in range(r, r + 2):
                for nc in range(c, c + 2):
                    if board[nr][nc] != "0":
                        answer += 1
                        board[nr][nc] = "0"

    def gravity(board):
        new_board = [['0'] * n for _ in range(m)]

        for c in range(n):
            idx = m-1
            for r in range(m-1, -1, -1):
                if board[r][c] != "0":
                    new_board[idx][c] = board[r][c]
                    board[r][c] = "0"
                    idx -= 1
        return new_board

    while 1:
        # 판 확인
        popPoints = []
        for r in range(m - 1):
            for c in range(n - 1):
                if check_board(r, c):
                    popPoints.append((r, c))

        # 2x2가 없을때
        if not popPoints:
            break

        # 제거
        delete_points(popPoints)

        # 중력이동
        board = gravity(board)

    return answer