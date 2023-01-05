# write a python program to print multiplication table using recursion

def multi(n,i):
    if i>10:
        return
    print(n, "*", i, "=", n*i)
    return multi(n,i+1)
num=int(input("enter the num"))
multi(num,1)
    
    
