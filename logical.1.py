
# print sum of digits of a number untill the number become single digit
def digSum(n):
    sum = 0
     
    while(n > 0 or sum > 9):
     
        if(n == 0):
            n = sum
            sum = 0
         
        sum += n % 10
        n //= 10
     
    return sum
n =int(input("enter the num"))
print (digSum(n))



def sum_of_digits(n):
    s = 0

    while n:
        s += n % 10
        n //= 10

    if s > 9:
        return sum_of_digits(s)

    return s

n = int(input("Enter an integer: "))
print(sum_of_digits(n))