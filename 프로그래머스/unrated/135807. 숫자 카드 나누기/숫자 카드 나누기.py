#1154
import math

def gcd(array):
    if len(array) == 1:
        return array[0]
    gcd = math.gcd(array[0], array[1])
    for i in range(2, len(array)):
        gcd = math.gcd(gcd, array[i])
    return gcd

def prime(gcd):
    big, small = [], []
    for i in range(1, int(math.sqrt(gcd))+1):
        if gcd % i == 0:
            if i != 1 : small.append(i)
            big.append(gcd // i)
    return big + list(reversed(small))

def findAnswer(case, arr, answer):
    for i in case:
        for v in arr:
            if v % i == 0:
                break
        else:
            if answer < i: answer = i
            break
    return answer

def solution(arrayA, arrayB):
    answer = 0
    gcdA = gcd(arrayA)
    gcdB = gcd(arrayB)

    caseA = prime(gcdA)
    caseB = prime(gcdB)

    answer = findAnswer(caseA, arrayB, answer)
    answer = findAnswer(caseB, arrayA, answer)

    return answer