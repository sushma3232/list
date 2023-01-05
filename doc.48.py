# Q48. Two numbers are entered through the keyboard. Write a flowchart to find the value of the first number
# raised to the power of another.
# Sample Input
# 3
# 4
# Sample Output
# 81 (3x3x3x3)
# Sample Input
# 5
# 3
# Sample Output
# 125 (5x5x5)
# Sample Input
# 6
# 7
# Sample Output
# 279936 (6x6x6x6x6x6x6)


def power(n,e):
    i=0
    while i<=e:
        a=n**e
        i=i+1
    print(a)
power(6,7)


def power(n,e):
    i=0
    while i<=e:
        a=n**e
        i=i+1
    print(a)
n=int(input("enter the num"))
e=int(input("enter the num"))
power(n,e)


