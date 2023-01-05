# write a python programm to reverse a string
# str="1234abcd"
# o/p="dcba4321"

# for loop:
def reverse(s):
    str=""
    for i in s:
        str=i+str
    return str
s="1234abcd"
print(reverse(s))
    
    
# while loop:
def reverse(s):
    str=""
    i=0
    while i<len(s):
        str=s[i]+str
        i=i+1
    print(str)
reverse("1234abcd")

