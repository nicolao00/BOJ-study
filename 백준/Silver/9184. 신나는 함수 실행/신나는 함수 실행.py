import sys

input = sys.stdin.readline

# 832

cases = dict()

def dfs(a, b, c):
    if (a, b, c) in cases:
        return cases[(a,b,c)]

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        if (20, 20, 20) not in cases:
            cases[(20, 20, 20)] = dfs(20, 20, 20)
        return cases[(20, 20, 20)]

    elif a < b and b < c:
        if (a, b, c - 1) not in cases:
            cases[(a, b, c - 1)] = dfs(a, b, c - 1)

        if (a, b - 1, c - 1) not in cases:
            cases[(a, b - 1, c - 1)] = dfs(a, b - 1, c - 1)

        if (a, b - 1, c) not in cases:
            cases[(a, b - 1, c)] = dfs(a, b - 1, c)
        return cases[(a, b, c - 1)] + cases[(a, b - 1, c - 1)] - cases[(a, b - 1, c)]

    else:
        if (a - 1, b, c) not in cases:
            cases[(a - 1, b, c)] = dfs(a - 1, b, c)

        if (a - 1, b - 1, c) not in cases:
            cases[(a - 1, b - 1, c)] = dfs(a - 1, b - 1, c)

        if (a - 1, b, c - 1) not in cases:
            cases[(a - 1, b, c - 1)] = dfs(a - 1, b, c - 1)

        if (a - 1, b - 1, c - 1) not in cases:
            cases[(a - 1, b - 1, c - 1)] = dfs(a - 1, b - 1, c - 1)

        return cases[(a - 1, b, c)] + cases[(a - 1, b - 1, c)] + cases[(a - 1, b, c - 1)] - cases[(a - 1, b - 1, c - 1)]

answer = []
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c== -1:
        break
    result = dfs(a, b, c)
    answer.append("w({}, {}, {}) = {}\n".format(a, b, c, result))

print("".join(answer))