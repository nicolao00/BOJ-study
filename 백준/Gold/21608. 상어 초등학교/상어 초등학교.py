# 421
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
board = [[-1]*(N+2)] + [[-1] + [0]*N + [-1] for _ in range(N)] +[[-1]*(N+2)]
sequence = [] # 앉히는 학생 번호 순서
studentLike = [[] for _ in range(N**2 + 1)] # 인덱스: 학생번호 / 값: 좋아하는 학생 번호들
studentLoc = defaultdict(tuple) # 인덱스: 학생번호 / 값: 좌표

for i in range(N**2):
    info = list(map(int, input().split()))
    studentLike[info[0]] = info[1:]
    sequence.append(info[0])

for sNum in sequence:
    candi = defaultdict(int)
    for like in studentLike[sNum]: # 좋아하는 학생이 앉아있는 주변 빈공간을 딕셔너리에 추가
        if like in studentLoc:
            r, c = studentLoc[like]
            for nr, nc in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:  # 좋아하는 학생 주변 탐색
                if board[nr][nc] == 0:
                    candi[(nr, nc)] += 1

    deleteKeys = []
    if len(candi) != 0:     # 좋아하는 학생 중 앉아있는 사람이 여러명일때
        maxV = max(candi.values())
        for i, v in candi.items():
            if v < maxV:
                deleteKeys.append(i)
        for key in deleteKeys:
            candi.pop(key)

    else:                   # 좋아하는 학생이 아무도 안 앉아있을때 빈 공간을 다 추가
        for r in range(1, N+1):
            for c in range(1, N + 1):
                if board[r][c] == 0:
                    candi[(r, c)] = 0

    if len(candi) != 1:     # 1번 조건 만족하는 칸이 여러 개이면 2번 조건 실행
        for r, c in candi.keys():
            candi[(r, c)] = 0
            for nr, nc in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:  # 좋아하는 학생 주변 탐색
                if board[nr][nc] == 0:
                    candi[(r, c)] += 1

    maxKV = ((400, 400), -1)
    for key, value in candi.items(): # 3번 조건
        if maxKV[1] < value:
            maxKV = (key, value)
        elif maxKV[1] == value:
            if maxKV[0] > key:
                maxKV = (key, value)

    row, col = maxKV[0]
    board[row][col] = sNum
    studentLoc[sNum] = (row, col)

answer = 0
for r in range(1, N+1):
    for c in range(1, N + 1):
        student = board[r][c]
        count = 0
        for nr, nc in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:  # 좋아하는 학생 주변 탐색
            if board[nr][nc] in studentLike[student]:
                count += 1
        if count == 2:
            count = 10
        elif count == 3:
            count = 100
        elif count == 4:
            count = 1000
        answer += count

print(answer)