import local
Interest_Rate = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]
singleSubjectTaxes = [0, 9076, 36901, 89351, 186351, 405101, 406751]
doubleSubjectTaxes = [0, 18151, 73801, 148851, 226851, 405101, 457601]
parentLonerSubjectTaxes = [0, 12951, 49401, 127551, 206601, 405101, 432201]
sub_text = local.SUB_TEXT
D_text = local.D_TEXT
Month = local.MONTH
Tax=local.TAX
Currency=local.CURRENCY
CurrencySmall=local.CURRENCYSMALL
def CountIncome():   
 annual_income = 0
 summaryN=0
 subject=int(input(sub_text)) 
 for month in range(12): 
     print('{} {}?:'.format(D_text,Month[month], end ='')) 
     income = float(input())   
     summaryN+=CountTax(subject,int(income))
     summaryN = round(summaryN,2)
     
 print(Tax,int(summaryN//1),Currency,int((summaryN%1*100)//10),CurrencySmall)
def CountTax (subject, D):
    N=0
    if subject==1:
        i=0
        while i<len(singleSubjectTaxes):
                if D-singleSubjectTaxes[i]>0 and D-singleSubjectTaxes[i+1]<0:
                    N+=Interest_Rate[i]*(D-singleSubjectTaxes[i])
                else:
                    if D-singleSubjectTaxes[i]>0 and D-singleSubjectTaxes[i+1]>0:
                        N+=Interest_Rate[i]*(singleSubjectTaxes[i+1]-singleSubjectTaxes[i])
                i+=1
    if subject==2:
        i=1
        while i<len(doubleSubjectTaxes):
                if D-doubleSubjectTaxes[i]>0 and D-doubleSubjectTaxes[i+1]<0:
                    N+=Interest_Rate[i]*(D-doubleSubjectTaxes[i])
                else:
                    if D-doubleSubjectTaxes[i]>0 and D-doubleSubjectTaxes[i+1]>0:
                        N+=Interest_Rate[i]*(doubleSubjectTaxes[i+1]-doubleSubjectTaxes[i])
                i+=1
    if subject==3:
        i=1
        while i<len(parentLonerSubjectTaxes):
                if D-parentLonerSubjectTaxes[i]>0 and D-parentLonerSubjectTaxes[i+1]<0:
                    N+=Interest_Rate[i]*(D-parentLonerSubjectTaxes[i])
                else:
                    if D-parentLonerSubjectTaxes[i]>0 and D-parentLonerSubjectTaxes[i+1]>0:
                        N+=Interest_Rate[i]*(parentLonerSubjectTaxes[i+1]-parentLonerSubjectTaxes[i])
                i+=1
    return N
CountIncome()
