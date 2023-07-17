import re
import copy
from itertools import permutations
def solution(expression):
    answer = 0
    numStr = re.split(r'[-|\*|\+]', expression)
    numList = list(map(int, numStr))
    operList = [i for i in expression if re.findall('-|\*|\+',i)]
    # if not i.isdigit() / if re.match('-|\*|\+', i)

    case = set(operList)
    for priority in permutations(case, len(case)):
        nList, oList = copy.deepcopy(numList), copy.deepcopy(operList)
        for oper in priority:
            i = 0
            while oper in oList:
                if oper == oList[i] == '+':
                    nList.insert(i, nList.pop(i) + nList.pop(i))
                elif oper == oList[i] == '-':
                    nList.insert(i, nList.pop(i) - nList.pop(i))
                elif oper == oList[i] == '*':
                    nList.insert(i, nList.pop(i) * nList.pop(i))

                if oper == oList[i]:
                    oList.pop(i)
                    i = 0
                else: i += 1
        if nList[0] < 0: nList[0] *= -1
        if answer < nList[0]: answer = nList[0]

    return answer