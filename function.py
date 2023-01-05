def function(a,b):
    c=a+b
    print(c)
function(3,7)


def fun():
    print("welcome")
fun()


def evenodd(x,y,z):
    if x%2==0 and y%2==0 and z%2==0:
        print("even")
    else:
        print("odd")
evenodd(4,6,8)
evenodd(3,5,7)



def fun(x,y):
    print(x+"   "+y)
fun("email",7)



index=0
i=0
while i<=10:
    print(index,"",end="")
    index=index+i
    if index==10:
        break
    print("found at",index,"locaton")
