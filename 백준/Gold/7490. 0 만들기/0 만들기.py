# 303
import sys

input = sys.stdin.readline

answer = []
def dfs(idx):
    if idx == 2*N-1:
        result = "".join(board)
        if eval(result.replace(" ", "")) == 0:
            answer.append(result)
            answer.append('\n')
        return

    for oper in [' ', '+', '-']:
        tmp = board[idx]
        board[idx] = oper
        dfs(idx+2)
        board[idx] = tmp

for _ in range(int(input())):
    N = int(input())
    board = []
    for i in range(1,N + 1):
        board.append(str(i))
        board.append('ㅅ')
    board.pop()

    dfs(1)
    answer.append('\n')

answer.pop()
answer.pop()
print("".join(answer))