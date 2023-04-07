from collections import deque

visited=[]
dir=[(1,0),(0,1),(-1,0),(0,-1)]
dq=deque()

def bfs(maps):
    day=0
    while dq:
        row, col = dq.popleft()
        day += int(maps[row][col])
        for d in dir:
            dr, dc = row + d[0], col + d[1]
            if not(0<=dr<len(maps) and 0<=dc<len(maps[0])):
                continue                
            if maps[dr][dc]!='X' and visited[dr][dc] == 0:
                dq.append((dr, dc))
                visited[dr][dc]=1
    return day

def solution(maps):
    answer = []
    row,col = len(maps), len(maps[0])
    for _ in range(row):
        visited.append([0]*col)
    
    for i in range(row):
        for j in range(col):
            if maps[i][j]!='X' and visited[i][j] == 0:
                dq.append((i,j))
                visited[i][j]=1
                answer.append(bfs(maps))

    if not answer:
        answer.append(-1)
    else:
        answer.sort()

    return answer