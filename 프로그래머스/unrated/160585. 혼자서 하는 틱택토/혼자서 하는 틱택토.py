# 0220
def solution(board):
    answer = -1
    ocount=0
    xcount=0
    owin=0
    xwin=0
    

    for i in range(3):
        oRowflag=0
        oColflag=0
        xRowflag=0
        xColflag=0
        for j in range(3):
            if board[i][j]=="O":
                ocount+=1
                oRowflag+=1
            elif board[i][j]=="X":
                xcount+=1
                xRowflag+=1

            if board[j][i]=="O":
                oColflag+=1
            elif board[j][i]=="X":
                xColflag+=1

            if oRowflag==3:
                owin+=1
            if xRowflag==3:
                xwin+=1
            if oColflag==3:
                owin+=1
            if xRowflag==3:
                xwin+=1
    
    oRdialflag=0
    oLdialflag=0
    xRdialflag=0
    xLdialflag=0
    for i in range(3):
        if board[i][i]=="O":
            oRdialflag+=1
        elif board[i][i]=="X":
            xRdialflag+=1

        if board[i][2-i]=="O":
            oLdialflag+=1
        elif board[i][2-i]=="X":
            xLdialflag+=1        

    if oRdialflag==3:
        owin+=1
    if xRdialflag==3:
        xwin+=1

    if oLdialflag==3:
        owin+=1
    if xLdialflag==3:
        xwin+=1


    answer=1
    if ocount-xcount>1:
        answer=0
    if xcount>ocount:
        answer=0
    elif owin>0 and xwin>0:
        answer=0        
    elif xwin>0 and ocount>xcount:
        answer=0
    elif owin>0 and ocount==xcount:
        answer=0

    return answer