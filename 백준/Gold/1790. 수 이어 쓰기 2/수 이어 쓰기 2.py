import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# 1. K번째 숫자가 어떤 자릿수에 속하는지 찾기
digit = 1  # 현재 자릿수
count = 0  # 누적 자릿수의 합

while True:
    # 현재 자릿수의 숫자 개수
    numbers_in_digit = min(N, 10 ** digit - 1) - (10 ** (digit - 1) - 1)
    digit_length = numbers_in_digit * digit

    # K번째가 현재 자릿수를 포함하는 경우
    if count + digit_length >= K:
        break

    # 누적 자릿수 합 증가
    count += digit_length
    digit += 1

    # 자릿수를 초과하는 경우 처리
    if 10 ** (digit - 1) > N:
        print(-1)
        sys.exit()

# 2. 해당 자릿수에서 몇 번째 숫자인지 계산
remaining = K - count  # 현재 자릿수에서의 K번째 위치
start_number = 10 ** (digit - 1)  # 해당 자릿수의 시작 숫자
number_index = (remaining - 1) // digit  # 0-indexed 숫자 위치
target_number = start_number + number_index

# 3. 숫자가 N을 초과하면 -1 출력
if target_number > N:
    print(-1)
else:
    # K번째 숫자를 해당 숫자에서 찾아 출력
    digit_index = (remaining - 1) % digit
    print(str(target_number)[digit_index])
