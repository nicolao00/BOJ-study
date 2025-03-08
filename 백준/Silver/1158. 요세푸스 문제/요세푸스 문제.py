# 1009
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visit = [False] * N
answer = 0
arr = []

K -= 1 # 인덱스로 쓸거라 -1함
idx = 0
while answer < N:
    cnt = 0
    while cnt <= K:
        if not visit[idx]:
            cnt += 1

        if cnt == K + 1:
            visit[idx] = True
            arr.append(str(idx + 1))
            answer += 1

        idx = (idx + 1) % N

print(f'<{", ".join(arr)}>')