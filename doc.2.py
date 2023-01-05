# write a python function to print maximum of three num

def maximum(a,b,c):
    if a>=b and a>=c:
        largest=a
    elif b>=a and b>=c:
        largest=b
    else:
        largest=c
    return largest
res=maximum(100,14,67)
print("largest num:",res)



a=int(input("enter the num"))
b=int(input("enter the num"))
c=int(input("enter the num"))
def maximum():
    if a>=b and a>=c:
        largest=a
    elif b>=a and b>=c:
        largest=b
    else:
        largest=c
    print("largest num:",largest)
maximum()


