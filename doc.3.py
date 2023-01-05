# write a python function to print sum of all the numbers in a list
# l=[8,2,3,0,7]
# o/p=20


# while loop:
def sum1(*a):
    sum=0
    z=list(a)
    i=0
    while i<len(z):
        sum+=z[i]
        i=i+1
    print(sum)
sum1(8,2,3,0,7)


# # for loop:
def sum(*numbers):
    total=0
    for x in numbers:
        total+=x
    return total
print(sum(8,2,3,0,7))


# method-2:
def sum1(num):
    i=0
    sum=0
    while i<len(num):
        sum=sum+num[i]
        i=i+1
    print(sum)
num=[8,2,3,0,7]
sum1(num)