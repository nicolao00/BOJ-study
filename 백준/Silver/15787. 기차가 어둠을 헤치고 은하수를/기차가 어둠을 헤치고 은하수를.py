import sys

# 854
input = sys.stdin.readline

N, M = map(int, input().split())
trains = [[0]*21 for _ in range(N+1)]
answer = set()

for _ in range(M):
    lst = list(map(int, input().split()))
    
    if lst[0] == 1:
        trains[lst[1]][lst[2]] = 1
    elif lst[0] == 2:
        trains[lst[1]][lst[2]] = 0
    elif lst[0] == 3:
        for i in range(20, 0, -1):
            trains[lst[1]][i] = trains[lst[1]][i-1]
        trains[lst[1]][1] = 0
    else:
        for i in range(1, 20):
            trains[lst[1]][i] = trains[lst[1]][i+1]
        trains[lst[1]][20] = 0

for i in range(1, N+1):
    answer.add(''.join(map(str, trains[i])))

print(len(answer))