# USING SORT FUNCTION SORT THE GIVEN UNORDERED LIST
# I/P=[6,8,4,3,9,56,0,34,7,15]
# O/P=[0,3,4,6,7,8,9,15,34,56]


def fun(n):
    i=0
    while i<len(n):
        n.sort()
        i=i+1
    print(n)
n=[6,8,4,3,9,56,0,34,7,15]
fun(n)