import sys
sys.setrecursionlimit(10**6)

# 1004
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key=lambda x:x[2])
parent = [i for i in range(V + 1)]
answer = 0

def findParent(x):
    if parent[x] == x:
        return x

    parent[x] = findParent(parent[x]) # 경로 압축
    return parent[x]

def djk():
    global answer
    count = 0
    for i in range(E):
        a, b, c = graph[i]

        # check cycle
        A = findParent(a)
        B = findParent(b)
        if A == B:
            continue

        parent[A] = B

        count += 1
        answer += c

        if count == E - 1:
            return

djk()
print(answer)