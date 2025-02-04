import sys
from collections import defaultdict
input = sys.stdin.readline

# 310
N = int(input())
words = [0] * N
wordsLen = [0] * N
for i in range(N):
    words[i] = defaultdict(int)
    word = input().rstrip()
    wordsLen[i] = len(word)
    for char in list(word):
        words[i][char] += 1

answer = 0
for i in range(1, N):
    # 첫번째, 두번째 단어가 더 많이 가지는 문자의 개수
    firstRemain = 0
    secondRemain = 0
    checkedCnt = 0
    for value in words[0].keys():
        # 첫번째 단어가 얼마나 다른 개수만큼 다른 문자를 가지는지
        if value in words[i]:
            checkedCnt += words[i][value]
            result = words[0][value] - words[i][value]
            if result > 0:
                firstRemain += result
            elif result < 0:
                secondRemain += abs(result)
        else:
            firstRemain += words[0][value]

    secondRemain += wordsLen[i] - checkedCnt
    if firstRemain > 0 and secondRemain > 0 and firstRemain + secondRemain <= 2:
        answer += 1
    elif firstRemain + secondRemain <= 1:
        answer += 1



print(answer)