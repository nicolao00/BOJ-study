from collections import deque
def solution(plans):
    answer = []
    stack = deque()

    for assign in plans:
        assign[1] = int(assign[1][:2]) * 60 + int(assign[1][3:5])
        assign[2] = int(assign[2])
    plans.sort(key=lambda x: x[1])

    # 다음에 들어올 과제 인덱스
    elementIdx = 1
    currentTime = plans[0][1]
    stack.append(plans[0])

    while stack:
        assign = stack.pop()
        print(assign, currentTime)
        # 아직 과제가 다 안들어왔을때
        if elementIdx != len(plans):
            # 현재 과제가 끝나기전에 다음 과제가 들어올때
            if currentTime + assign[2] > plans[elementIdx][1]:
                assign[2] -= plans[elementIdx][1] - currentTime
                stack.append(assign)
                stack.append(plans[elementIdx])
                currentTime = plans[elementIdx][1]
                elementIdx += 1
            else:
                answer.append(assign[0])
                currentTime += assign[2]
            if not stack:
                stack.append(plans[elementIdx])
                currentTime = plans[elementIdx][1]
                elementIdx += 1

        # 과제가 모두 들어왔을 때
        else:
            answer.append(assign[0])

    return list(answer)