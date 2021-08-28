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