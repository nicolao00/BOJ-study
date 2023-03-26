def solution(wallpaper):
    answer = []
    lux=51
    luy=51
    rdx=-1
    rdy=-1
    for row in range(len(wallpaper)):
        for idx, value in enumerate(wallpaper[row]):
            if value=="#":
                if lux>row:
                    lux=row
                if row+1<=len(wallpaper) and rdx<row+1:
                    rdx=row+1
                if luy>idx:
                    luy=idx
                if idx+1<=len(wallpaper[row]) and rdy<idx+1:
                    rdy=idx+1
    answer.append(lux)
    answer.extend([luy,rdx,rdy])
    return answer