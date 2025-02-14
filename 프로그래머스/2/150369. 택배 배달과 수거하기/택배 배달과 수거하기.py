def solution(cap, n, deliveries, pickups):
    answer = 0
    dCap, pCap = 0, 0  # 배달 및 수거 용량

    for i in range(n - 1, -1, -1):
        dCap -= deliveries[i]
        pCap -= pickups[i]

        while dCap < 0 or pCap < 0:
            answer += (i + 1) * 2
            dCap += cap
            pCap += cap

    return answer
