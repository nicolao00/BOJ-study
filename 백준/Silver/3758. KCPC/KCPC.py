# 1125
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    teamCnt, problemCnt, myTeamId, logCnt = map(int, input().split())

    teamProblemScore = [[0] * (problemCnt+1) for _ in range(teamCnt + 1)]
    teamProblemTryCnt = [0] * (teamCnt + 1)
    teamLastProblemTime = [0] * (teamCnt + 1)
    for i in range(logCnt):
        teamId, problemNum, score = map(int, input().split())
        teamProblemScore[teamId][problemNum] = max(teamProblemScore[teamId][problemNum], score)
        teamProblemTryCnt[teamId] += 1
        teamLastProblemTime[teamId] = i

    teamInfo = []
    for i in range(1, teamCnt + 1):
        teamTotalScore = sum(teamProblemScore[i])
        teamInfo.append([teamTotalScore, teamProblemTryCnt[i], teamLastProblemTime[i], i])

    teamInfo.sort(key = lambda o1 : (-o1[0], o1[1], o1[2]))

    for i in range(teamCnt):
        if teamInfo[i][3] == myTeamId:
            print(i + 1)