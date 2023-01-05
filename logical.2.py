# remove integers from a string using python function:
def fun(str):
    b=[]
    i=0
    while i<len(str):
        if str[i].isdigit():
            b.append(str[i])
        i=i+1
    print(b)
str = "12abc20yz68"
fun(str)


# print sum of numbers in a string: 
def fun(str):
    b=[]
    i=0
    while i<len(str):
        if str[i].isdigit():
            b.append(str[i])
        i=i+1
    print(b)
    j=0
    sum=0
    while j<len(b):
       sum=sum+int(b[j])
       j=j+1
    print(sum)    
str = "12abc20yz68"
fun(str)


# print the sum of numbers 
def fun(str):
    b=[]
    i=0
    while i<len(str)-1:
        if str[i].isdigit() and str[i+1].isdigit():
            c=int(str[i]+str[i+1])
            b.append(c)
        i=i+1
    print(b)
    j=0
    sum=0
    while j<len(b):
       sum=sum+(b[j])
       j=j+1
    print(sum)
str = "12abc20yz68"
fun(str)

 
       


