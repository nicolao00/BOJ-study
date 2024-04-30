# 129
import sys
from math import sqrt, floor
input = sys.stdin.readline

N = int(input())
stars = [tuple(map(float, input().split())) for _ in range(N)]

def calDist(a, b):
    return sqrt((stars[a][0] - stars[b][0])**2 + (stars[a][1] - stars[b][1])**2)

# 부모 루트 찾기
def find_root(a):
    if parents[a] == a:
        return a
    else:
        parents[a] = find_root(parents[a])
    return parents[a]

# 루트 노드 병합
def union_root(a, b):
    x = find_root(a)
    y = find_root(b)

    if x != y:
        parents[x] = y

def kruskal():
    global answer, mst
    for cost, (x, y) in edges:
        # 싸이클 안만드는지 확인
        if find_root(x) == find_root(y): continue

        # 싸이클 안만들면 mst에 추가
        mst += 1
        answer += cost
        # Parent 관계 갱신
        union_root(x, y)
        # 정점 개수 v에 대해 v-1개 간선 찾으면 종료
        if mst == N-1:
            break


# 가중치, 초기 부모 노드 설정
mst = 0
answer = 0
edges = []
parents = [i for i in range(N)]
for i in range(N):
    for j in range(i+1, N):
        edges.append((calDist(i, j), (i, j)))

edges.sort()

kruskal()
print(round(answer, 2))