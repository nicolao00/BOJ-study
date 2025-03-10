num = 1
def solution(word):
    dictionary = dict()
    answer = 0

    def dfs(idx, str):
        global num

        if len(str) >= 5:
            return

        for i in ['A', 'E', 'I', 'O', 'U']:
            str.append(i)
            dictionary["".join(str)] = num
            num += 1

            dfs(idx + 1, str)

            str.pop()

    dfs(0, [])
    answer = dictionary[word]

    return answer
