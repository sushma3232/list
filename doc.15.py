# write a function to calculate power of number raised to other:
# def power(n, e):
#     if e == 0:
#         return 1
#     elif e == 1:
#         return n
#     else:
#         return (n*power(n, e-1))
# n = 4
# p = 2
# print(power(n, p))

# # print(4**0)
# # print(4**1)
# # print(4*pow(4,2-1))


# # FOR LOOP:
# def power(n,e):
#     res=0
#     for i in range(e):
#         res *= n
#     return res
# print(pow(4,2))


# WHILE LOOP:
def power(n,e):
    i=0
    while i<=e:
        a=n**e
        i=i+1
    print(a)
power(4,2)


