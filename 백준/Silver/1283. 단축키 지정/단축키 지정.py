import sys

input = sys.stdin.readline

N = int(input())
options = set()

def isExist(word, i):
    if word[i].lower() not in options and word[i].upper() not in options:
        options.add(word[i].lower())
        options.add(word[i].upper())
        return True
    return False

def firstCheck(words):
    for i in range(len(words)):
        if isExist(words[i], 0):
            return i
    return -1

def secondCheck(words):
    for fIdx in range(len(words)):
        for i in range(len(words[fIdx])):
            if isExist(words[fIdx], i):
                return fIdx, i
    return -1, -1

answer = []
for _ in range(N):
    words = input().split()
    result = []
    a = firstCheck(words)
    if a != -1:
        tmp = list(words[a])
        tmp.insert(0, '[')
        tmp.insert(2, ']')
        words[a] = "".join(tmp)
        result = words
    else:
        a, b = secondCheck(words)
        if a != -1 and b != -1:
            tmp = list(words[a])
            tmp.insert(b, '[')
            tmp.insert(b + 2, ']')
            words[a] = "".join(tmp)
        result = words
    answer.append(" ".join(result))

print("\n".join(answer))
