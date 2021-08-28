def Encrypted(n):
    Values=[]

    if n < 9999 and n >=999:

        num1=int(n/1000)
        num2=int(n/100)-(num1*10)
        num4=n%10
        num3=int((n/10-(num1*100))-(num2*10))

        # print(num1,num2,num3,num4)


        num1=int((num1+7)%10)
        num2=int((num2+7)%10)
        num3=int((num3+7)%10)
        num4=int((num4+7)%10)

        # print(num1,num2,num3,num4)

        Values.append(num1)
        Values.append(num2)
        Values.append(num3)
        Values.append(num4)



    return Values


def Decrypted(Values):
    NewValues=[]

    num1=Values[0]
    num2=Values[1]
    num3=Values[2]
    num4=Values[3]


    # print(num1,num2,num3,num4)

    num1=int((num1+3)%10)
    num2=int((num2+3)%10)
    num3=int((num3+3)%10)
    num4=int((num4+3)%10)

    # print(num1,num2,num3,num4)

    NewValues.append(num1)
    NewValues.append(num2)
    NewValues.append(num3)
    NewValues.append(num4)

    return NewValues








def Main():
    Status=True
    while Status:
        Number=int(input("Enter The Number -: "))
        AskUser=Encrypted(Number)
        if(len(AskUser)==0):
            print("Invalid Input")
            Status=True

        else:
            tempStr = ""
            for i in AskUser:
                tempStr = tempStr + str(i)
                #print(" "+str(i))
            print("The Encripted Number is "+tempStr)
            Status=False

    AskUsers=Decrypted(AskUser)
    tempStr = ""
    for i in AskUsers:
        tempStr = tempStr + str(i)
    print("The Decrypted Number is "+tempStr)







Main()