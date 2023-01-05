# Q45. Draw a flowchart to Take 10 numbers as input and create a list of the numbers from the user and update
# each element of the list according to below rule
# If it is even, then multiply it by 100
# If it is odd, then multiply it by -1
# Sample Input:
# 23
# 42
# 41
# 1
# Sample Output:
# -23
# 4200
# -41
# -1

def fun(a):
    i=1
    while i<=a:
        b=int(input("enter the num"))
        if b%2==0:
            print(b*100,"even")
        else:
            print(b*-1,"odd")
        i=i+1
a=int(input("enter the num"))
fun(a)


