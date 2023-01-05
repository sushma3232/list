# find the sum of number digits in list.
# l=[12,67,98,34]
# o/p:[3,13,17,7]


def fun(a):
    i=0
    b=[]
    while i<len(a):
        sum=0
        while a[i]>0:
            r=a[i]%10
            sum=sum+r
            a[i]=a[i]//10
        b.append(sum)
        i=i+1
    print(b)
a=[12,67,98,34]
fun(a)


