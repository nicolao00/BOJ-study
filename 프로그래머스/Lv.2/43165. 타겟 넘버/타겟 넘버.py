# 1156
answer = 0
sums = [0] * 21
def dfs(idx, numbers, target, result):
    global answer
    if idx == len(numbers):
        if result == target:
            answer += 1
        return

    dfs(idx + 1, numbers, target, result + numbers[idx])
    dfs(idx + 1, numbers, target, result - numbers[idx])




def solution(numbers, target):
    dfs(0, numbers, target, 0)
    return answer