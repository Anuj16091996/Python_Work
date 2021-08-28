def CalculateCubeSquare():

    Status=True

    while Status:
        n=int(input("Write The Number-: "))
        if(n>0 and n<10):
            Square=n*n;
            Cube=n*n*n
            print("Square of "+str(n)+" is "+str(Square))
            print("Cube of "+str(n)+" is "+str(Cube))
            Status=False

        else:

            print("Try Again ")
            Status=True


def Main():
    CalculateCubeSquare()



Main()