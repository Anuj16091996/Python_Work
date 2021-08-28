<<<<<<< HEAD
from random import randint

def random_number ():
    return randint(0, 9)

def guess_multiply (inputNumUser, n1, n2):
    if inputNumUser == (n1 * n2):
        print("very good")
        return True
    else:
        print("No. try again")
        return False

# Repeat until Answer is correct
condition=True
while condition:
    # Generate Random Numbers
    n1= random_number()
    n2= random_number()
    # input number and validate
    while True:
        try:
            (inputNumUser)= int(input('how much is '+str(n1)+' times '+str(n2)+'?: '))
            break
        except ValueError:
            print('Only integer numbers please!')
    condition= guess_multiply(inputNumUser, n1, n2)
=======
import random
from random import randint

Questions=['How much was the first income of Brad pit','How much you weight']
i=0
while i<len(Questions):

    value=randint(0,99)
    # print(value)
    status=True

    while status:

        user=int(input(Questions[i]+" :-" ))

        if user==value:
            print("very good")
            i=i+1
            status=False

        elif user>value:
            print("To High")
            print("No. try again")

        elif user<value:
            print("To Low")
            print("No. try again")





>>>>>>> a378a7c9fcf5f39d3f68e49a3f546cc79d4213bd
