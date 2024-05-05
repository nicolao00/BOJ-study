permuts = []
answer = 1e9
def solution(n, weak, dist):

    def pernutations(n, temp, visit):
        if all(visit):
            permuts.append(temp)
            return
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                pernutations(n, temp + [dist[i]], visit)
                visit[i] = False

    length = len(weak)
    pernutations(len(dist), [], [False] * len(dist))

    for i in range(length):
        weak.append(weak[i] + n)

    for start in range(length):

        def check():
            global answer
            for friend in permuts:
                cnt = 1
                position = weak[start] + friend[cnt-1]
                for i in range(start, start+length):
                    if position < weak[i]:
                        cnt += 1
                        if cnt > len(dist):
                            break
                        position = weak[i] + friend[cnt-1]
                answer = min(cnt, answer)

        check()

    if answer > len(dist):
        return -1
    return answer
