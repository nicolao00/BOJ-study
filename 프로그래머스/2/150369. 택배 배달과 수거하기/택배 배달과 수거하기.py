
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
def solution(cap, n, deliveries, pickups):
    dmax, pmax, ans = n-1, n-1, 0
    if sum(deliveries) + sum(pickups) == 0 :
        return 0
    while dmax > -1 or pmax > -1:
        ans += 2 * max(pmax+1, dmax+1)
        dcar, pcar = cap, cap
        while dmax > -1 and dcar > 0:
            if deliveries[dmax] > dcar:
                deliveries[dmax] -= dcar
                dcar = 0
            else :
                dcar -= deliveries[dmax]
                dmax -= 1
            while dmax > -1 and deliveries[dmax] == 0 :
                dmax -= 1    
        while pmax > -1 and pcar > 0:
            if pickups[pmax] > pcar:
                pickups[pmax] -= pcar
                pcar = 0
            else :
                pcar -= pickups[pmax]
                pmax -= 1
            while pmax > -1 and pickups[pmax] == 0 :
                pmax -= 1
    return ans