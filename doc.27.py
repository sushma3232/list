
# WRITE THE FUNCTION FOR CHECK THE SPEED OF DRIVERS.THIS FUNCTION SHOULD HAVE OE PARAMETER :SPEED

def func(speed):
    if speed<=70:
        print(70,"okay")
    if speed>70:
        i=70
        while i<=70:
            point=(speed-70)//5
            if point>12:
                print(point,speed,"licence suspended")
            else:
                print(point,speed,"okay")
            i=i+1
speed=int(input("enter the speed"))
func(speed)

















