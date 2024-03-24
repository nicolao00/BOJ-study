# 1036 - 1130
import sys
input = sys.stdin.readline
from collections import defaultdict, deque

N, M = map(int, input().split())

# 순회 시작할 때 번호 매겨서 방문하는 곳에 저장

# 저장된 번호에 해당되는 방 크기 저장

def bitChange(n):
    result = []
    for i in range(4):
        result.append(str(n % 2))
        n //= 2
    result.reverse()
    return ''.join(result)

board = [list(map(bitChange, map(int, input().split()))) for _ in range(M)]
visit = [[0]*N for _ in range(M)] # 각 칸이 해당하는 방의 번호를 저장
roomSize = defaultdict(int) # 각 번호에 해당하는 방의 사이즈 저장

def roomSizeCheck(r, c, num):
    visit[r][c] = num
    dq = deque([(r, c)])

    while dq:
        r, c = dq.popleft()
        for idx, (nr, nc) in enumerate([(r+1, c), (r, c+1), (r-1, c), (r, c-1)]):
            if board[r][c][idx] == '1': # 벽인 경우
                continue
            if 0 <= nr < M and 0 <= nc < N and not visit[nr][nc]:
                visit[nr][nc] = num
                roomSize[num] += 1
                dq.append((nr, nc))


num = 1 # 방의 번호를 저장하는 변수
for r in range(M):
    for c in range(N):
        if not visit[r][c]:
            roomSize[num] = 1
            roomSizeCheck(r, c, num)
            num += 1

answer = 0
for r in range(M):
    for c in range(N):
        for idx, (nr, nc) in enumerate([(r+1, c), (r, c+1)]):
            if nr < M and nc < N and visit[r][c] != visit[nr][nc]:
                answer = max(answer, roomSize[visit[r][c]] + roomSize[visit[nr][nc]])

print(len(roomSize))
print(max(roomSize.values()))
print(answer)