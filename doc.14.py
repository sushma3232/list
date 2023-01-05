# write a function to check if a number is prime or not
def func(a):
    count=0
    i=1
    while i<=a:
        if a%i==0:
            count=count+1
        i=i+1
    if count==2:
        print("prime")
    else:
        print("not prime")
a=int(input("enter the num"))
func(a)
