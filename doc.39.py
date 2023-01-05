
# maximun([4,6,2,1,9,63,-134,566]) returns 566

# maximun([5]) returns 5.
def fun(a):
    i=0
    max=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i=i+1
    print(max)
a=[4,6,2,1,9,63,-134,566]
fun(a)


# minimun([-52, 56, 30, 29, -54, 0, -110]) returns -110        
def fun(a):
    i=0
    min=0
    while i<len(a):
        if a[i]<min:
            min=a[i]
        i=i+1
    print(min)
a=[-52,56,30,29,-54,0,-110]
fun(a)
        
        
#  maximun([5]) returns 5.          
def fun(a):
    i=0
    max=0
    while i<len(a):
        if a[i]>max:
            max=a[i]
        i=i+1
    return max
a=([5])
print(fun(a))


# minimun([42, 54, 65, 87, 0]) returns 0.
def fun(a):
    i=0
    min=0
    while i<len(a):
        if a[i]<min:
            min=a[i]
        i=i+1
    print(min)
a=([42,54,65,87,0])
fun(a)