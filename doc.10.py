# creat a function that takes 2 positive integers in form of a string
# "4","5="9
# "34","5"="39


def fun(a,b):
    i=0
    while i<len(a):
        num=int(a)+int(b)
        i=i+1
    return(num)
print(fun("4","5"))

 


