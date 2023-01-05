# WRITE a python function to find the list with maximum and minimum length
# l=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# o/p:maximum length of list(3)


def fun(a):
    i=0
    max_l=0
    min_l=10
    while i<len(a):
        n=a[i]
        c=len(n)
        if c>max_l:
           max_l=c
           e=a[i]
        elif c<min_l:
           min_l=c
           f=a[i]
        i=i+1
    print("max len:","(",max_l,",",e,")")
    print("min len:","(",min_l,",",f,")")
a =[[1,3],[0],[9,11],[13,15,17]]
fun(a)


