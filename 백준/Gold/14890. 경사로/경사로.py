# 922
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
slide = []
# 경사로 놓고는 놓은 위치 표시해놓는 자료구조 필요!

# 행부터 시작해서 현재칸
# 현재칸 > 다음칸 : 다음칸 놓을 수 있냐 판단(방법은 다음칸=현재칸 해놓고 쭉 확인. 확인중에 안되면 현재 행 종료, 확인 끝나면 마지막 현재칸 = 다음칸 해놓고 마저 탐색)
# 이때 경사로 놓을 수 있으면 현재칸부터 다음칸 까지 새로운 배열에 True로 설정
# 현재칸 < 다음칸 :
# 반복문 다 돌렸을때 마지막 칸이면 answer + 1


# 열방향으로 경사로를 놓을 수 있는지 확인하는 함수
def rowSlideCheck(start, row, flag):
    # 현재칸이 다음칸보다 1만큼 클 때
    if flag == 1:
        # 경사로가 범위가 벗어날 때
        if start + L >= N: return False

        # 경사로 놓을 수 있는지 확인
        if not all(board[row][start] == board[row][start + i] + 1 and not slide[start+i] for i in range(1, L + 1)):
            return False

        # 경사로 설치
        for i in range(start+1, start + 1 + L):
            slide[i] = True

    # 현재칸이 다음칸보다 1만큼 작을 때
    else:
        # 경사로가 범위가 벗어날 때
        if start - 1*L < 0: return False

        # 경사로 놓을 수 있는지 확인
        if not all(board[row][start] == board[row][start + i] + 1 and not slide[start+i] for i in range(-1, -1*L - 1, -1)):
            return False

        # 경사로 설치
        for i in range(start-1, start - 1*L - 1, -1):
            slide[i] = True
    return True

# 행방향으로 경사로를 놓을 수 있는지 확인하는 함수
def colSlideCheck(start, col, flag):
    # 현재칸이 다음칸보다 1만큼 클 때
    if flag == 1:
        # 경사로가 범위가 벗어날 때
        if start + L >= N: return False

        # 경사로 놓을 수 있는지 확인
        if not all(board[start][col] == board[start + i][col] + 1 and not slide[start+i] for i in range(1, L + 1)):
            return False

        # 경사로 설치
        for i in range(start+1, start + 1 + L):
            slide[i] = True

    # 현재칸이 다음칸보다 1만큼 작을 때
    else:
        # 경사로가 범위가 벗어날 때
        if start - 1*L < 0: return False

        # 경사로 놓을 수 있는지 확인
        if not all(board[start][col] == board[start + i][col] + 1 and not slide[start+i] for i in range(-1, -1*L - 1, -1)):
            return False

        # 경사로 설치
        for i in range(start-1, start - 1*L - 1, -1):
            slide[i] = True
    return True



answer = 0
# 열방향으로 검사
for row in range(N):
    slide = [False] * N
    curBlock = 0    # cur 현재 보고있는 칸

    # 현재 보고 있는 칸이 마지막일때까지 진행
    while curBlock < N-1:
        # 현재칸과 다음칸이 같을때
        if board[row][curBlock] == board[row][curBlock+1]: curBlock += 1

        # 현재칸이 다음칸보다 1만큼 클 때
        elif board[row][curBlock] == board[row][curBlock+1] + 1:
            if not rowSlideCheck(curBlock, row, 1):
                break
            curBlock += L

        # 현재칸이 다음칸보다 1만큼 작을 때
        elif board[row][curBlock] == board[row][curBlock+1] - 1:
            if not rowSlideCheck(curBlock+1, row, -1):
                break
            curBlock += 1
        else: break

    if curBlock == N-1:
        answer += 1
    else:
        for i in range(N):
            slide[i] = False


# 행방향으로 검사
for col in range(N):
    slide = [False] * N
    curBlock = 0    # cur 현재 보고있는 칸

    # 현재 보고 있는 칸이 마지막일때까지 진행
    while curBlock < N-1:
        # 현재칸과 다음칸이 같을때  
        if board[curBlock][col] == board[curBlock+1][col]: curBlock += 1

        # 현재칸이 다음칸보다 1만큼 클 때
        elif board[curBlock][col] == board[curBlock+1][col] + 1:
            if not colSlideCheck(curBlock, col, 1):
                break
            curBlock += L

        # 현재칸이 다음칸보다 1만큼 작을 때 
        elif board[curBlock][col] == board[curBlock+1][col] - 1:
            if not colSlideCheck(curBlock+1, col, -1):
                break
            curBlock += 1
        else: break

    if curBlock == N-1:
        answer += 1

print(answer)