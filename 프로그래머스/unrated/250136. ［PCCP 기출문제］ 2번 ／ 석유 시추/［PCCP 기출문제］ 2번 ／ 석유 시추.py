#15분 946-1003 / 1109
import sys
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(10**7)

# def dfs(nh, nw, count):
#     global w, h, land, visit
#     if visit[nh][nw]:
#         return
#
#     visit[h][w] = 1
#     for dh in range(-1, 0, 1, 0):
#         for dw in range(0, 1, 0, -1):
#             tmph, tmpw = dh + nh, dw + nw
#             if not (0 <= tmph < h and 0 <= tmpw < w):
#                 continue
#             land[tmph][tmpw] = dfs(tmph, tmpw, count + 1)
#             return

def bfs(localh, localw):
    dq = deque([(localh, localw)])
    visit[localh][localw] = 1
    widGroup = set([localw])
    count = 1
    while dq:
        nh, nw = dq.popleft()
        for dh, dw in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            tmph, tmpw = dh + nh, dw + nw
            if not (0 <= tmph < h and 0 <= tmpw < w) or visit[tmph][tmpw] or land[tmph][tmpw] == 0:
                continue
            count += 1
            dq.append([tmph, tmpw])
            visit[tmph][tmpw] = 1
            widGroup.add(tmpw)

    for i in widGroup:
        diction[i] += count


def solution(l):
    global w, h, land, visit, diction
    diction = defaultdict(int)
    answer = 0

    land = l
    w = len(land[0])
    h = len(land)

    visit = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if visit[i][j] or land[i][j] == 0:
                continue
            bfs(i, j)
    answer = max(diction.values())
    return answer