# 838
N = int(input())
like = int(input())

frames = dict()  # [추천 횟수, 들어온 시간]
for i, v in enumerate(list(map(int, input().split()))):
    if v in frames:
        frames[v][0] += 1

    else:
        if len(frames) >= N:
            tmp = [1e9, 0]
            popkey = 1e9
            for key, value in frames.items():
                if (value[0] < tmp[0]) or (value[0] == tmp[0] and value[1] < tmp[1]):
                    tmp = value
                    popkey = key
            frames.pop(popkey)
        frames[v] = [1, i]
print(*sorted(frames.keys()))