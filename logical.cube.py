# write a python function to find the cube of all positive integers

def fun(n):
    i=1
    while i<=n:
        if n>0:
            a=n*n*n
        else:
            raise valueerror
        i=i+1
    print(a)
n=int(input("enter the num"))
fun(n)



# write a python function that takes a positive integers and returns the sum of cube of all positive integers
# smaller than specifide number

def fun(n):
    sum=0
    i=1
    while i<=n:
        if n>0:
            a=n*n*n
            sum=sum+a
        else:
            raise valueerror
        i=i+1
    print(sum)
n=int(input("enter the num"))
fun(n)
