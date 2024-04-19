# 1022 - 1121 / 218
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    answer = N
    visit = [False]*(N+1)
    totalLen = 1

    def check(start, cur, d):
        global answer, totalLen

        nxt = nums[cur]
        result = -1
        # 끝점과 시작점이 같을 때
        if nxt == start:
            answer -= d+1
        # 시작점과 끝점이 처음부터 같을 때
        elif cur == nxt:
            answer -= 1
        # 다음점이 방문되지 않았을 떄
        elif not visit[nxt]:
            visit[nxt] = True
            totalLen += 1
            result = check(start, nxt, d + 1)
        else:
            return nxt

        # 끝점이 시작점과 같지 않으나 현지점과 같을 떄
        if result == cur:
            answer -= (totalLen - d)

        return result



    for i in range(N):
        if not visit[i+1]:
            totalLen = 1
            visit[i + 1] = True
            check(i+1, i+1, 0)

    print(answer)