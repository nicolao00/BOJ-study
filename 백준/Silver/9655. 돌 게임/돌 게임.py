# 621
import sys
input = sys.stdin.readline

a = input().rstrip()
N = int(a[-1])
if N % 2 == 1:
    print("SK")
else:
    print("CY")