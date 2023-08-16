def solution(cards):
    groups = []
    for i in range(len(cards)):
        group = []
        while cards[i] != 0:
            group.append(cards[i])
            temp = cards[i]
            cards[i] = 0
            i = temp - 1
            if cards[i] == 0: groups.append(len(group))
    groups.sort(reverse=True)
    if len(groups) == 1: return 0
    return groups[0] * groups[1]