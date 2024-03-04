import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
fixSeat = set([int(input()) for _ in range(M)])

D = [[0] for _ in range(N+2)]

D[0] = D[1] = 1
for i in range(2, N+1):
    D[i] = D[i-1]
    if i in fixSeat or i - 1 in fixSeat: continue
    D[i] += D[i - 2]

print(D[N])