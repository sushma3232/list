# WRITE A FUNCTION CALLED FIZZ_BUZZ THAT TAKES A NUMBER


def fizz_buzz(num):
    i=0
    while i<=num:
        if num%3==0 and num%5==0:
            return "fizzbuzz"
        if num%3==0:
            return "fizz"
        if num%5==0:
            return "buzz"
        else:
            return num
        i=i+1
num=int(input("enter the num"))   
print(fizz_buzz(num))



def fizz_buzz(num):
        if num%3==0 and num%5==0:
            return "fizzbuzz"
        if num%3==0:
            return "fizz"
        if num%5==0:
            return "buzz"
        else:
            return num
num=int(input("enter the num"))
print(fizz_buzz(num))



