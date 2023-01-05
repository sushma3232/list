# WRITE A FUNCTION TO TELL USER IF SHE IS VOTING OR NOT
# CONSIDER A MINIMUM AGE OF VOTING TO BE 18

def min(age):
    if age>=18:
        print("voting")
    else:
        print("not")
age=int(input("enter the age"))
min(age)





