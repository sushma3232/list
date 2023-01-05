
# INPUT=["I","N","D","H","U"]
# OUTPUT=["U","H","D","N","I"]

def fun(num):
    i=0
    while i<len(num):
        num.reverse()
        i=i+1
    print(num)
num=["I","N","D","H","U"]
fun(num)


# INPUT="INDHU"
# OUTPUT="UHDNI"
def fun(n):
    i=-1
    b=""
    while i>=-len(n):
        c=n[i]
        b=b+c
        i=i-1
    print(b)
n="INDHU"
fun(n)


