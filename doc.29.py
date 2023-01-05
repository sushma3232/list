# WRITE A FUNCTION THAT FETURNS THE SUN OF MULTIPLIES OF 3 AND 5 BETWEEN 0AND LIMIT.(parameter)
# for example ,if the limit is 20,it should te sum of 3,5,6,9,10,12,15,18,20


        
def fun():
    sum=0
    i=0
    while i<=b:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    print(sum)
b=int(input("enter the num"))
fun()


