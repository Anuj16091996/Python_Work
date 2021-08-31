from random import randint

def CreatingRandomIndex():
    Rows=randint(1,10)
    Colum=randint(1,10)
    x=[[randint(0,1) for _ in range(Rows)] for _ in range(Colum)] #This is Colum

    return x


def Main():
    Matrix=CreatingRandomIndex()
    for i in Matrix:
        print(i)


Main()