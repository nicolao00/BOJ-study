def solution(sequence, k):
    answer = []
    length = len(sequence)

    right, result = 0, 0
    for left in range(length):
        while result < k and right < length:
            result += sequence[right]
            right += 1
        if result == k:
            answer.append([left, right-1])
        result -= sequence[left]
        left += 1

    return sorted(answer, key=lambda x: x[1] - x[0])[0]