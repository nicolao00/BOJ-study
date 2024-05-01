# 230
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parents = [0] + [i for i in range(1,N+1)]
edges = []
answer = 0
mstSize = 0

def find_root(a):
    if parents[a] == a:
        return a
    else:
        parents[a] = find_root(parents[a])
        return parents[a]

def union_root(a, b):
    x = find_root(a)
    y = find_root(b)

    if x != y:
        parents[x] = y

def kruscal():
    global answer, mstSize
    # 최소 가중치인 간선 선택
    for cost, a, b in edges:
        x = find_root(a)
        y = find_root(b)

    # 사이클 없을 경우만 선택
        if x == y: continue
        union_root(a, b)

        answer += cost
        mstSize += 1
    # v-1개 간선 될때까지 반복
        if mstSize == N-1:
            answer -= cost
            break


for a, b, cost in [list(map(int, input().split())) for _ in range(M)]:
    edges.append((cost, a, b))
edges.sort()

kruscal()
print(answer)


