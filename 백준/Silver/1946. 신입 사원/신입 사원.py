import sys

# 934
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores.sort(key=lambda x : x[0])

    highest = 100001
    answer = N
    for i in range(N):
        # 두 심사 모두 더 낮은 점수일 때
        if highest < scores[i][1]:
            answer -= 1
        else:
            highest = scores[i][1]
    print(answer)