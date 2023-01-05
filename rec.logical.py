# calculate sum of list of numbers

def fun(list):
    if len(list)==1:
        return list[0]
    else:
        return list[0]+fun(list[1:])
print(fun([1,3,5,7,9]))