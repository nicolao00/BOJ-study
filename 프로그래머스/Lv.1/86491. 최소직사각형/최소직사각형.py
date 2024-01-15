# 923

def solution(sizes):
    big, small = 0, 0
    for w, h in sizes:
        maxValue = max(w, h)
        minValue = min(w, h)
        if maxValue > big:
            big = maxValue
        if minValue > small:
            small = minValue

    return big * small
