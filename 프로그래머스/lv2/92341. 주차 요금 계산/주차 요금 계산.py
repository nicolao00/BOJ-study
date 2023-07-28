#810
import math
def solution(fees, records):
    answer = []
    carNum = set([carNum.split()[1] for carNum in records])
    # car { 차량넘버 : [누적 시간, 마지막 찍힌 시간, 마지막 찍힌 상태] }
    car = {key : [0,0,0] for key in carNum}

    for step in records:
        time, num, status = step.split()
        time = int(time[0:2])*60 + int(time[3:5])
        if status == "OUT":
            car[num][0] += time - car[num][1]
        car[num][1] = time
        car[num][2] = status

    for i in carNum:
        if car[i][2] == "IN":
            car[i][0] += 1439 - car[i][1]

    for num in carNum:
        if fees[0] > car[num][0]:
            answer.append((num, fees[1]))
        else:
            answer.append((num, fees[1] + math.ceil((car[num][0] - fees[0])/fees[2]) * fees[3]))
    answer.sort()
    return [i[1] for i in answer]