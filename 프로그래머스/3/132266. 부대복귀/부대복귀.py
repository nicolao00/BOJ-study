# 1024
# 총 지역수 / 두 지역을 왕복할 수 있는 길 정보 / 각 부대원이 위치한 서로 다른 지역들 / 강철부대의 지역
from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    distance = [1e9] * (n+1)
    distance[destination] = 0
    
    graph = [[] for _ in range(n+1)]
    for r1, r2 in roads:
        graph[r1].append(r2)
        graph[r2].append(r1)
    
    def bfs(destination):
        dq = deque()
        dq.append((destination, 0))
        while dq:
            node, d = dq.popleft()
            for newNode in graph[node]:
                if d + 1 < distance[newNode]:
                    distance[newNode] = d+1
                    dq.append((newNode, d+1))
    
    bfs(destination)
    for start in sources:
        if distance[start] == 1e9:
            answer.append(-1)
        else:
            answer.append(distance[start])
        
    
    return answer


# import heapq
# def solution(n, roads, sources, destination):
#     answer = []
    
#     graph = [[] for _ in range(n+1)]
#     for r1, r2 in roads:
#         graph[r1].append(r2)
#         graph[r2].append(r1)
    
#     def bfs(cur, dist):
#         visit = [False] * (n+1)
#         visit[start] = True
#         hq = []
#         heapq.heappush(hq, (dist, cur))
#         while hq:
#             d, node = heapq.heappop(hq)
#             for newNode in graph[node]:
#                 if newNode == destination:
#                     return d + 1
#                 if not visit[newNode]:
#                     visit[newNode] = True
#                     heapq.heappush(hq, (d+1, newNode))
        
#         return -1
    
#     for start in sources:
#         if start == destination:
#             answer.append(0)
#             continue
#         answer.append(bfs(start, 0))
        
    
#     return answer