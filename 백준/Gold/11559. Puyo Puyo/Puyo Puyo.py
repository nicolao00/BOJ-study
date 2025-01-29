import sys
from collections import deque
input = sys.stdin.readline

# 1058
board = [list(input().rstrip()) for _ in range(12)]

def find_bb(c):

    return r
        

answer = 0
while True:
    visit = [[False] * 6 for _ in range(12)]

    # 연쇄 확인 후 적용
    flag = False
    for r in range(12):
        for c in range(6):
            # 이미 방문했거나 빈칸이면 패스
            if visit[r][c] or board[r][c] == '.':
                continue

            visit[r][c] = True
            dq = deque()
            dq.append((r, c))
            count = 1
            changedRC = deque()
            changedRC.append((r, c))
            while dq:
                cr, cc = dq.popleft()
                for nr, nc in [(cr + 1, cc), (cr, cc + 1), (cr - 1, cc), (cr, cc - 1)]:
                    if 0 <= nr < 12 and 0 <= nc < 6 and not visit[nr][nc] and board[nr][nc] == board[r][c]:
                        count += 1
                        dq.append((nr, nc))
                        changedRC.append((nr, nc))
                        visit[nr][nc] = True

            # 연쇄
            if count >= 4:
                for nr, nc in changedRC:
                    board[nr][nc] = '.'
                flag = True

    # 변경된 지점이 없으면 종료
    if not flag:
        break

    # 중력 적용
    for c in range(6):
        # 바닥으로부터 가장 위에 있는 뿌요
        bottomR = 11
        bbR = 10
        while bottomR >= 0 and bbR >= 0 and bottomR > bbR:
            # 바닥을 찾아서 (.을 찾아서)
            while bottomR >= 0 and board[bottomR][c] != '.':
                bottomR -= 1
            if bottomR < 0:
                break

            # 하늘에 있는 가장 첫번쨰 뿌요를 찾아서
            bbR = bottomR - 1
            while bbR >= 0 and board[bbR][c] == '.':
                bbR -= 1
            if bbR < 0:
                break

            board[bottomR][c] = board[bbR][c]
            board[bbR][c] = '.'

    answer += 1

print(answer)
