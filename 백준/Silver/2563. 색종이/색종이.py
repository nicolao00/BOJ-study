# 1001
import sys
input = sys.stdin.readline

N = int(input())

answer = 0
visit = [[False] * 100 for _ in range(100)]
for _ in range(N):
    C, R = map(int, input().split())

    for r in range(R, R + 10):
        for c in range(C, C + 10):
            if visit[r][c]:
                answer += 1
            else:
                visit[r][c] = True

print(100*N - answer)