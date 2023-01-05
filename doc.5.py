# write a python function that takes a list and returns a new list with unique elements of first list
# l=[1,2,3,3,3,4,5]
# o/p=[1,2,3,4,5]

def remove(duplicate):
    l=[]
    for i in duplicate:
        if i not in l:
            l.append(i)
    return(l)  
duplicate=[1,2,3,3,3,4,5] 
print(remove(duplicate))



def remove(duplicate):
    l=[]
    i=0
    while i<len(duplicate):
        if duplicate[i] not in l:
            l.append(duplicate[i])
        i=i+1  
    print(l)
duplicate=[1,2,3,3,3,4,5]
remove(duplicate)

 

def func(num):
    i=0
    b=[]
    while i<len(num):
        if num[i] not in b:
            b.append(num[i])
        i=i+1
    print(b)
num=[1,2,3,3,3,4,5]
func(num)