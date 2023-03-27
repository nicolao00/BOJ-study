# 1050
def solution(babbling):
    answer = 0
    spell = ["aya", "ye", "woo", "ma"]

    i=0
    while i<len(babbling):
        exWord=""
        j=0
        while j<len(spell):
            if babbling[i].find(spell[j], 0, len(spell[j])) != -1:
                if spell[j]==exWord:
                    break
                babbling[i]=babbling[i].replace(spell[j],"",1)
                exWord=spell[j]
                j=0
            else:
                j+=1
        i+=1

    for word in babbling:
        if word=="":
            answer+=1
    print(babbling)
    return answer