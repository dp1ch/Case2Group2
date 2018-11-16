# string constants 

def n(income): 
 return 0 
def S(n): 
 return 0 
def taxes(n): 
 D(n) 
 S(n)
 return
#N=S(n)*(D(n+1)-D(n))+sum() 

#types=n(income()) 
#tax=taxes(types)
"""Case-study #2 Progressive tax
Developers:
Pichuev D (0%), Grasmik R (0%) 
""" 
import local
S_list = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]
singleD = [0, 9076, 36901, 89351, 186351, 405101, 406751]
doubleD = [0, 18151, 73801, 148851, 226851, 405101, 457601]
parentD = [0, 12951, 49401, 127551, 206601, 405101, 432201]
sub_text = local.SUB_TEXT
D_text = local.D_TEXT
Month = local.MONTH
def income():   
 #name_month = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"] 
 annual_income = 0
 sumN=0
 subject=int(input(sub_text)) 
 for month in range(12): 
     print('{} {}?:'.format(D_text,Month[month], end ='')) 
     income = float(input())   
     sumN+=N(subject,int(income))
 print(local.TAX,sumN)
     #annual_income += income 
 #return(annual_income) #D
def N (subject, D):
    N=0
    if subject==1:
        i=0
        while i<len(singleD):
                if D-singleD[i]>0 and D-singleD[i+1]<0:
                    N+=S_list[i]*(D-singleD[i])
                else:
                    if D-singleD[i]>0 and D-singleD[i+1]>0:
                        N+=S_list[i]*(singleD[i+1]-singleD[i])
                i+=1
    if subject==2:
        i=1
        while i<len(doubleD):
                if D-doubleD[i]>0 and D-doubleD[i+1]<0:
                    N+=S_list[i]*(D-doubleD[i])
                else:
                    if D-doubleD[i]>0 and D-doubleD[i+1]>0:
                        N+=S_list[i]*(doubleD[i+1]-doubleD[i])
                i+=1
    if subject==3:
        i=1
        while i<len(parentD):
                if D-parentD[i]>0 and D-parentD[i+1]<0:
                    N+=S_list[i]*(D-parentD[i])
                else:
                    if D-parentD[i]>0 and D-parentD[i+1]>0:
                        N+=S_list[i]*(parentD[i+1]-parentD[i])
                i+=1
    return N

#N(int(input(sub_text)), int(income()))
income()
