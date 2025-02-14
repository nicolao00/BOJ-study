# 548 - 640
endIdxD = endIdxP = answer = 0


def solution(cap, n, deliveries, pickups):
    global endIdxD, endIdxP, answer
    endIdxD = endIdxP = n - 1
    answer = 0

    def delivery():
        global endIdxD, answer

        # 상자가 있는 최초의 집
        startIdx = -1
        capacity = 0
        # 최대 상자 개수를 채우거나 더이상 배달할 집이 없을 때 까지
        while endIdxD >= 0 and capacity <= cap:
            if startIdx == -1 and deliveries[endIdxD] != 0:
                startIdx = endIdxD
            # 최대 보유 상자 개수 이내
            if capacity + deliveries[endIdxD] <= cap:
                capacity += deliveries[endIdxD]
                deliveries[endIdxD] = 0
                endIdxD -= 1
            # 최대 보유 상자 개수 초과
            else:
                deliveries[endIdxD] -= cap - capacity
                break

        return startIdx

    def pickup(startIdx):
        global endIdxP, answer

        # 배달한 택배가 없을 때 (이동)
        isMoved = True
        if startIdx == -1:
            isMoved = False
        newStartIdx = -1

        capacity = 0
        while endIdxP >= 0 and capacity <= cap:
            if newStartIdx == -1 and pickups[endIdxP] != 0:
                newStartIdx = endIdxP
            if capacity + pickups[endIdxP] <= cap:
                capacity += pickups[endIdxP]
                pickups[endIdxP] = 0
                endIdxP -= 1
            else:
                pickups[endIdxP] -= cap - capacity
                break

        if not isMoved:
            return newStartIdx

        return newStartIdx

    curLoc = -1
    while endIdxD >= 0 or endIdxP >= 0:
        deliverIdx = pickupIdx = -1
        # 끝지점부터 배달
        if endIdxD >= 0:
            deliverIdx = delivery()

        # 끝지점부터 수거
        if endIdxP >= 0:
            pickupIdx = pickup(deliverIdx)

        farIdx = max(deliverIdx, pickupIdx)

        if farIdx == -1:
            curLoc = -1
        else:
            answer += 2 * (farIdx + 1)
        curLoc = -1

    return answer