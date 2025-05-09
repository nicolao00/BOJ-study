from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
s = [[0]*(M+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]

base, front, side = N*M, 0, 0
for n in range(1, N+1):
    for m in range(1, M+1):
        front += max(0, s[n][m]-s[n-1][m])
        side  += max(0, s[n][m]-s[n][m-1])

print((base+front+side)*2)