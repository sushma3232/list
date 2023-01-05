# print even numbers from a given list
# l=[1,2,3,4,5,6,7,8,9]
# output:[2,4,6,8]

# for loop:
def even(a):
    l=[]
    for i in a:
        if i%2==0:
           l.append(i) 
    return l
a=[1,2,3,4,5,6,7,8,9]
print(even(a))


# whileloop:
def even(a):
    l=[]
    i=0
    while i<len(a):
        if a[i]%2==0:
            l.append(a[i])
        i=i+1
    print(l)
a=[1,2,3,4,5,6,7,8,9]
even(a)


 
#  # we can also print even no's using lambda exp.

a= [10, 21, 4, 45, 66, 93, 11]
even_num = list(filter(lambda x: (x % 2 == 0), a))
 
print("Even numbers in the list: ", even_num)
