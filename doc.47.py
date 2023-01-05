# Q47. Draw a flowchart to take a list of 7 numbers from the user, print True if the complete list consists of
# consecutive numbers with any constant difference between numbers. Print False otherwise.
# Input:
# 2 4 6 8
# Output:
# True

def fun(a):
    i=0
    result=True
    while i<len(a)-1:
        if a[i+1]-a[i]==2:
           result=True 
        else:
            result=False
        i=i+1
    return result
a=[2,4,6,8]
print(fun(a))

# -5 -6 -7 -8
# True
def fun(a):
    i=0
    result=True
    while i<len(a)-1:
        if a[i+1]-a[i]==-1:
           result=True 
        else:
            result=False
        i=i+1
    return result
a=[-5,-6,-7,-8]
print(fun(a))

# 1,2,4,6
# false
def fun(a):
    i=0
    result=True
    while i<len(a)-1:
        if a[i+1]-a[i]==1:
           result=True 
        else:
            result=False
        i=i+1
    return result
a=[1,2,4,6]
print(fun(a))

# 3,6,9,12,16
# false
def fun(a):
    i=0
    result=True
    while i<len(a)-1:
        if a[i+1]-a[i]==3:
           result=True 
        else:
            result=False
        i=i+1
    return result
a=[3,6,9,12,16]
print(fun(a))

