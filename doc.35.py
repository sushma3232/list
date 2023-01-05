
# Q35. Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.
# Rules:-
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.
# Examples: (Input --> Output


def fun(age):
        if age<=14:
            print("kids drink toddy")
        if age>14 and age<18:
            print("teans drinks coke")
        if age>=18 and age<21:
            print("young adults drink bear")
        if age>=21:
            print("adults drinks whisky")
age=int(input("enter the num"))
fun(age)





