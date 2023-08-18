def solution(targets):
    answer = 1
    targets.sort()
    rStart, rEnd = targets[0]
    for mStart, mEnd in targets:
        if mStart >= rEnd:
            answer += 1
            rStart, rEnd = mStart, mEnd
        rStart, rEnd = max(rStart, mStart), min(rEnd, mEnd)

    return answer