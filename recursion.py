
# find factorial of a number using recursion

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print(fact(10))


# recursive error
# example 1:
# def fun():
#     print("hello")
#     fun()
# fun()

# example 2:


# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n*fact(n-1)
# print(fact(1000))



# # sum of first "n" natural numbers using recursion
# def my_function(n):
#     if n==0:
#         return 0
#     else:
#         return my_function(n-1)+n
# n=int(input("enter the num"))
# answer=my_function(n)
# print(answer)



