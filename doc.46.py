# Q46. Draw a flowchart to take a list of N numbers from the user, print True if the complete list consists of
# consecutive numbers with a difference of one. Print False otherwise.
# Sample Input:
# 1 2 3 4 5 6 7
# Sample Output:
# True

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
a=[1,2,3,4,5,6,7]
print(fun(a))


# 45 46 47 48 49 51 52
# False
def fun(a):
    i=0
    result=True
    while i<len(a)-1:
        if a[i+1]-a[i]==1:
           result=True 
        else:
            result=False
            break
        i=i+1
    return result
a=[45,46,47,48,49,51,52]
print(fun(a))


# -5 -6 -7 -8
# False

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
a=[-5 ,-6 ,-7 ,-8]
print(fun(a))



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
a=[-3 ,-2 ,-1 ,0, 1]
print(fun(a))

