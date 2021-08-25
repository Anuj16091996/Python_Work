import re


def PassCondition():

    number=6 #For Pending Steps
    checkcon=0
    password=str(input("Enter The Password -:  "))
    checklenght=len(password)

    for i in range(0,len(password)):
        if(len(password)==1):
            checkcon=checkcon+1
            break

        if (len(password)<=3):
            checkcon=checkcon+1
            break


        if(i==len(password)-2):
            break

        elif(password[i]==password[i+1] and password[i]==password[i+2]):
            checkcon=checkcon+1

    if(checkcon==0):
        number=number-1

    if(checklenght >=6):
        if(checklenght<=20 ):
            number=number-2


    for i in range(0,len(password)):
        if(password[i].isupper() ):
            number=number-1
            break


    for i in range(0,len(password)):
        if(password[i].islower() ):
            number=number-1
            break

    for i in range(0,len(password)):
        if(password[i].isdigit() ):
            number=number-1
            break


    # if password.islower():
    #     number=number-1





    return number






def main():

    status=True
    while status:
        Numbers=PassCondition()

        if (Numbers==0):
            print("your Password is Perfect")
            status=False

        else:
            print("Number of mistakes "+ str(Numbers) )
            print("Try Again")
            status=True







# number=len(password)
#
#
# if password.islower():
#     count=count+1
#
main()