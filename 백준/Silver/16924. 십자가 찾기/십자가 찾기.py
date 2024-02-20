import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]
starsVisit = {}
for r, row in enumerate(board):
    for c, element in enumerate(row):
        if element == '*':
            starsVisit[(r, c)] = False

def check(r, c):
    crossIdx = 1
    while 1:
        visit = []
        for dr, dc in [(-crossIdx, 0), (crossIdx, 0), (0, -crossIdx), (0, crossIdx)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if board[nr][nc] != '*':
                    return crossIdx-1
                visit.append((nr, nc))
            else:
                return crossIdx-1
        for element in visit:
            starsVisit[element] = True
        crossIdx += 1

answer = []
for key in starsVisit.keys():
    r, c = key
    result = check(r, c)
    if result:
        answer.append((r + 1, c + 1, result))
        starsVisit[(r, c)] = True


if all(starsVisit.values()) and len(answer) <= R * C:
    print(len(answer))
    for x, y, s in answer:
        print(f'{x} {y} {s}')
else:
    print(-1)
