
# WRITE A LIST OF NUMBERS,WRITE A PYTHON PROGRAMM TO COUNT POSITIVE AND NEGATIVE NUMBERS IN LIST USING FUNCTION
# L=[2,-7,5,64,-14]
# O/P:POS=2,neg=3

def num(a):
    pos_count=0
    neg_count=0
    i=0
    while i<len(a):
        if a[i]>=0:
            pos_count=pos_count+1
        else:
            neg_count=neg_count+1
        i=i+1
    print(pos_count)
    print(neg_count)
a=[2,-7,5,64,-14]
num(a)













