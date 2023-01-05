# find the length of the string without using len():
def string_length(my_string):
    count=0
    for char in my_string:
        count+=1
    return count
string_input=input("enter the string")
length=string_length(string_input)
print("length is",length)





def string_length(my_string):
    count=0
    i=0
    while i<len(string_input):
        count+=1
        i=i+1
    return count
string_input=input("enter the string")
length=string_length(string_input)
print("length is",length)