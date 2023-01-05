

# creat a list from the user input and call the list and print even or odd

def fun(n):
    i=1
    a=[]
    while i<=n:
        b=int(input("enter the number"))
        a.append(b)
        i=i+1
    print(a)
    i=0
    while i<len(a):
        if a[i]%2==0:
            print(a[i],"even")
        else:
            print(a[i],"odd")
        i=i+1
n=int(input("enter the num"))
fun(n)
