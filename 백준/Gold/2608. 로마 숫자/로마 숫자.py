# # 2336-2357 / 150
# import sys
#
# input = sys.stdin.readline
# customDict = dict()
# customDict['I'] = 1
# customDict['V'] = 5
# customDict['X'] = 10
# customDict['L'] = 50
# customDict['C'] = 100
# customDict['D'] = 500
# customDict['M'] = 1000
#
# customDict['IV'] = 1
# customDict['IX'] = 9
# customDict['XL'] = 40
# customDict['XC'] = 90
# customDict['CD'] = 400
# customDict['CM'] = 900
#
# sumAB = 0
# def caculate(str):
#     global sumAB
#
#     idx = 0
#     while idx < len(str):
#         # 작은 수가 앞 온 경우
#         if idx + 1 < len(str) and customDict[str[idx]] < customDict[str[idx + 1]]:
#             if str[idx:idx+2] in customDict:
#                 sumAB += customDict[str[idx:idx+2]]
#                 idx += 1
#         else:
#             sumAB += customDict[str[idx]]
#         idx += 1
#
# A = input().rstrip()
# caculate(A)
# B = input().rstrip()
# caculate(B)
# print(sumAB)
#
# answer = []
# while sumAB > 0:
#
roman_to_int = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}
int_to_roman = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

def roman_to_decimal(s):
    total = 0
    prev = 0
    for ch in reversed(s):
        val = roman_to_int[ch]
        if val < prev:
            total -= val
        else:
            total += val
            prev = val
    return total

def decimal_to_roman(num):
    res = ''
    for val, sym in int_to_roman:
        while num >= val:
            res += sym
            num -= val
    return res

a = input().strip()
b = input().strip()
sum_decimal = roman_to_decimal(a) + roman_to_decimal(b)
print(sum_decimal)
print(decimal_to_roman(sum_decimal))
