# Q9.Write a Python program to generate and print a list of first and last 5 elements where
# the values are square of numbers between 1 and 30 (both included).
# Output :-([1, 4, 9, 16, 25], [676, 729, 784, 841, 900]).

def fun(num):
    i=1
    x=[]
    while i<=num:
        a=i*i
        x.append(a)
        i=i+1
    print((x[:5],x[25:]))
fun(30)