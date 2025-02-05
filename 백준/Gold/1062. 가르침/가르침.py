# 1021
import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())
words = [set(input().rstrip()) for _ in range(N)]
spells = set()
spells = spells.union(*words)
knowns = set(['a', 'n', 't', 'i', 'c'])
for i in knowns:
    spells.remove(i)
for word in words:
    word.remove('a')
    word.remove('n')
    word.remove('t')
    word.remove('i')
    word.remove('c')

def check(comb):
    count = 0
    for word in words:
        flag = True
        for i in word:
            if i not in comb:
                flag = False
                break
        if flag:
            count += 1
    return count

answer = 0
if len(knowns) > K:
    print(0)
elif K == 5:
    print(check(['a', 'n', 't', 'i', 'c']))
else:
    length = min(K-5, len(spells))
    for comb in combinations(spells, length):
        count = check(comb)
        answer = max(answer, count)

    print(answer)