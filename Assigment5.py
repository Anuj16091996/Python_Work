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





