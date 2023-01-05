# WRITE A python function ,if we give 9119 the function should return 811181,
# asthe square of 9 is 81 and square of 1 is 1

def fun(n):
    i=0
    while i<=n:
        r=n%10
        k=r**2
        n=n//10
        i=i+1
        print(k,end="")
n=int(input("enter the num"))
fun(n)