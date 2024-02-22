#142
def solution(brown, yellow):    
    def check(b, y, v):
         return y - v * (b // 2 - v - 2)
        
    def binarySearch(b, y):
        l, r = 0, 2000
        while l <= r:
            mid = (l + r) // 2
            if check(b, y, mid) < 0:
                l = mid + 1
            elif check(b, y, mid) > 0:
                r = mid - 1
            else:
                return mid
        return -1
    
    x = binarySearch(brown, yellow)
    if x == -1:
        x = 0
        while yellow - x * (brown // 2 - x - 2) != 0:
            x += 1
    y = brown//2 - x - 2
    answer = [max(x+2,y+2), min(x+2,y+2)]
    
    return answer


# x*y = yellow
# x, y: 노랑의 가로 세로
# x+2, y+2: 갈색의 가로 세로

# x*y = yellow
# 2x + 2y + 4 = brown

# y = brown//2 - x - 2
# x(brown//2 - x - 2) = yellow

# x(3-x) = 2
# x2 - 3x + 2 = 0