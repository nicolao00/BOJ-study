# 1215
import sys

input = sys.stdin.readline

N, M, row, col, cnt = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))
drdc = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]

diceR, diceC = [0, 0, 0, 0], [0, 0, 0]  # 위 -> 아래, 왼 -> 오 (각각 인덱스 1 이 중심)
for command in commands:
    if 0 <= row + drdc[command][0] < N and 0 <= col + drdc[command][1] < M:
        row, col = row + drdc[command][0], col + drdc[command][1]

        if command == 1:
            dice1 = diceC[0]
            for i in range(2):
                diceC[i] = diceC[i+1]
            diceR[1] = diceC[1]
            diceC[2] = diceR[3]
            diceR[3] = dice1
        elif command == 2:
            dice1 = diceC[2]
            for i in range(2, 0, -1):
                diceC[i] = diceC[i - 1]
            diceR[1] = diceC[1]
            diceC[0] = diceR[3]
            diceR[3] = dice1
        elif command == 3:
            dice3 = diceR[3]
            for i in range(3, 0, -1):
                diceR[i] = diceR[i - 1]
            diceR[0] = dice3
            diceC[1] = diceR[1]
        else:
            dice1 = diceR[0]
            for i in range(3):
                diceR[i] = diceR[i + 1]
            diceR[3] = dice1
            diceC[1] = diceR[1]

        if board[row][col]:
            diceC[1] = board[row][col]
            diceR[1] = board[row][col]
            board[row][col] = 0
        else:
            board[row][col] = diceC[1]

        print(diceR[3])