# write a function bmithat calculates body mass index
# (bmi=weight/height)

def func(weight,height):
    bmi=weight/height
    if bmi>30:
        return "obese"
    if bmi<=25.0:
        return "normal"
    if bmi<=30:
        return "over weight"
    if bmi<=18.5:
        return "under weight"
weight=int(input("enter the weight"))
height=int(input("enter the height"))
print(func(weight,height))

