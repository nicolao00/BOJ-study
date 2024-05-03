# 406

def rotate90(key):
    new_arr = [[0]*len(key) for _ in range(len(key))]
    for r in range(len(key)):
        for c in range(len(key)):
            new_arr[c][len(key) - 1 - r] = key[r][c]
    return new_arr

# 키 범위 만큼 검사 진행
def keyCheck(key, lock, r, c, home):
    correct = 0
    for dr in range(len(key)):
        for dc in range(len(key)):
            nr, nc = r + dr, c + dc
            # 자물쇠 범위 밖이면 continue
            if not (0 <= nr < len(lock) and 0 <= nc < len(lock)): continue
            if (key[dr][dc] == 1 and lock[nr][nc] == 1) or (key[dr][dc] == 1 and lock[nr][nc] == 1):
                return False
            elif key[dr][dc] == 1 and lock[nr][nc] == 0:
                correct += 1

    if home == correct:
        return True

    return False


def solution(key, lock):
    answer = False
    rotatedKeys = [key]
    keyLen, lockLen = len(key), len(lock)
    home = lockLen**2
    for lst in lock:
        home -= sum(lst)

    for i in range(3):
        rotatedKeys.append(rotate90(rotatedKeys[i]))

    for r in range(-keyLen+1, lockLen):
        for c in range(-keyLen+1, lockLen):
            # 회전시킨 키들을 하나씩 검증
            for curKey in rotatedKeys:
                # 키 범위 만큼 검사 진행
                if keyCheck(curKey, lock, r, c, home):
                    return True

    return answer