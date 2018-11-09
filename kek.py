S_list = {0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396}
singleD = {0, 9076, 36901, 89351, 186351, 405101, 406751}
doubleD = {0, 18151, 73801, 148851, 226851, 405101, 457601}
parentD = {0, 12951, 49401, 127551, 206601, 405101, 432201}
def income (subject, D, N):
    N=0
    if subject==1:
        for i in singleD:
            if D-singleD[i]>0:
                i+=1
                N+=(singleD[i+1]-singleD[i])
    N+=(D-singleD[0])
    if subject==2:
        for i in doubleD:
            if D-doubleD[i]>0:
                i+=1
                N+=(doubleD[i+1]-doubleD[i])
    N+=(D-doubleD[0])
    if subject==3:
        for i in parentD:
            if D-parentD[i]>0:
                i+=1
                N+=(parentD[i+1]-parentD[i])
    N+=(D-parentD[0])
                
        
