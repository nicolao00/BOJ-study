import sys
from collections import deque

# 947
input = sys.stdin.readline
p, m = map(int, input().split())

dq = deque()
dqPlayers = dict()
isRoomFull = dict()

# def popDeque(roomLevel):
#     for rL in dq:
#         if roomLevel == rL:
#             print("Started!")
#             for l, v in dqPlayers[roomLevel]:
#                 print(l, v)

for i in range(p):
    l, n = input().split()
    l = int(l)

    for i, roomLevel in enumerate(dq):
        if i in isRoomFull and isRoomFull[i]:
            continue
        if l-10 <= roomLevel <= l+10:
            dqPlayers[i].append((l, n))
            if len(dqPlayers[i]) == m:
                isRoomFull[i] = True
                # popDeque(roomLevel)
            break
    else:
        dq.append(l)
        dqPlayers[len(dq)-1] = [(l, n)]
        if len(dqPlayers[len(dq)-1]) == m:
            isRoomFull[len(dq)-1] = True
            # popDeque(l)
        else:
            isRoomFull[len(dq)-1] = False

for i, level in enumerate(dq):
    if isRoomFull[i]:
        print("Started!")
    else:
        print("Waiting!")
    for l, n in sorted(dqPlayers[i], key=lambda x:x[1]):
        print(l, n)


# 2 1
# 10 a
# 10 b