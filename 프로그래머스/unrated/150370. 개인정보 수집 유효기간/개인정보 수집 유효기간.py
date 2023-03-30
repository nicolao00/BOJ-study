#1305
def solution(today, terms, privacies):
    answer = []
    valid={i.split()[0]:int(i.split()[1]) for i in terms}
    
    TY,TM,TD=(int(x) for x in today.split('.'))
    for idx,i in enumerate(privacies):
        date, option=i.split()
        YY,MM,DD=(int(x) for x in date.split('.'))

        DD-=1
        if DD<1:
            if MM==1:
                YY-=1
                MM=12
            else:
                MM-=1
            DD=28

        MM+=valid[option]
        if MM>12:
            div, mod=divmod(MM,12)
            if mod==0:
                div-=1
                mod=12
            YY,MM=YY+div, mod

        if TY>YY: answer.append(idx+1)
        elif TY==YY and TM>MM: answer.append(idx+1)
        elif TY==YY and TM==MM and TD>DD: answer.append(idx+1)
    return answer