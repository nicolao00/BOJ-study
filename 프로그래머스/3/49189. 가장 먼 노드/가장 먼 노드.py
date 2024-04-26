from collections import deque
def solution(n, edge):
    answer = 0
    longgest = 0
    
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visit = [False] *(n+1)
    visit[1] = True
    
    dq = deque()
    dq.append((1, 0))
    
    
    while dq:
        node, dist = dq.popleft()
        for newNode in graph[node]:
            if not visit[newNode]:
                visit[newNode] = True
                dq.append((newNode, dist+1))
                if longgest < dist + 1:
                    longgest = dist + 1
                    answer = 1
                else:
                    answer += 1
    
    return answer