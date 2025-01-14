import sys

input = sys.stdin.readline

# 814 - 853 957
N = int(input())
board = [0] + list(map(int, input().split()))
sums = [0] * (N+1)

for s in range(1, N+1):
    sums[s] = sums[s-1] + board[s]

answer = 0
for i in range(1,N+1):
    # a = sums[i] - board[i] + max((sums[i] - sums[1] - board[1]), (sums[i] - sums[2] - board[2]))
    a = (sums[i] - board[1] + max(sums[i] - sums[t] - board[t] for t in range(2, i))) if i > 2 else 0
    b = sums[i] + (sums[N-1] - sums[i-1]) - board[1]
    # c = (sums[N] - sums[i-1]) + max((sums[N-1]-sums[i-1] - board[N-1]), (sums[N-2]-sums[i-1] - board[N-2]))
    c = ((sums[N-1] - sums[i - 1]) + max(sums[t] - sums[i-1] - board[t+1] for t in range(i, N-1))) if N - 1 > i else 0
    answer = max(answer, max(c, max(a, b)))
print(answer)