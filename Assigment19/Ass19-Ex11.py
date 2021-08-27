
def CheckRightAngle(a,b,c):

    if((a*a) + (b*b)==(c*c)):
        print("These integers could form the sides of a right-angled triangle.")

    elif((b*b) + (c*c)==(a*a)):
        print("These integers could form the sides of a right-angled triangle.")

    elif((c*c) + (a*a)==(b*b)):
        print("These integers could form the sides of a right-angled triangle.")


    else:
        print("These Integers Could Not Form Right Angled Triangle")


def Main():
    CheckRightAngle(4,5,3)

Main()
