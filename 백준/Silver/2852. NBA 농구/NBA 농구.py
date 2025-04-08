# 1021
import sys

input = sys.stdin.readline

N = int(input())
info = [input().split() for _ in range(N)]
for i in range(N):
    info[i][0] = int(info[i][0])
    info[i][1] = int(info[i][1][:2])*60 + int(info[i][1][3:])
info.append([0, 48*60])

team1 = team2 = exTime = 0
team1Time = team2Time = 0
for i in range(N):
    if info[i][0] == 1:
        team1 += 1
    else:
        team2 += 1

    if team1 > team2:
        team1Time += info[i+1][1] - info[i][1]
    elif team2 > team1:
        team2Time += info[i+1][1] - info[i][1]

team1Hour = team1Time // 60
team1Minute = team1Time % 60
team1Answer = []
if team1Hour < 10:
    team1Answer.append('0')
team1Answer.append(str(team1Hour))
team1Answer.append(':')
if team1Minute < 10:
    team1Answer.append('0')
team1Answer.append(str(team1Minute))

team2Hour = team2Time // 60
team2Minute = team2Time % 60
team2Answer = []
if team2Hour < 10:
    team2Answer.append('0')
team2Answer.append(str(team2Hour))
team2Answer.append(':')
if team2Minute < 10:
    team2Answer.append('0')
team2Answer.append(str(team2Minute))


print("".join(team1Answer))
print("".join(team2Answer))