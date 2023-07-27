def solution(want, number, discount):
    answer = 0

    totalLen = len(discount) - sum(number)
    for sIdx in range(totalLen + 1):
        lst = discount[sIdx : sIdx+sum(number)]
        for idx, element in enumerate(want):
            if lst.count(element) < number[idx]:
                break
        else:
            answer += 1

    return answer