def strong():
    num=int(input("enter the num"))
    sum=0
    tem=num
    while tem>0:
        fac=1
        i=1
        order=tem%10
        while tem<=order:
            fac=fac*i
            i=i+1
        sum=sum+fac
        tem//=10
    if num==sum:
        print("strong num")
    else:
        print("not strong num")
strong()