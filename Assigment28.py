
# For PlainDrome Number
# To find The Range of it
def DecodingNumber(Num):
    FinalValues=[]

    for i in range(0,Num):
        Temp=i
        Stack=[]


        while Temp>0:
            LastDigit=int(Temp%10)
            Stack.append(LastDigit)
            Temp=(Temp-LastDigit)/10

        Lenght_Stack=len(Stack)
        Number=0
        Increment=0
        while Lenght_Stack>0:
            if Lenght_Stack==1:
                MultiplyNumber=1

            else:
                MultiplyNumber=10

            for j in range(0,Lenght_Stack-2):
                MultiplyNumber*=10

        # print(MultiplyNumber)
            Number+=(Stack[Increment]*(MultiplyNumber))

        # print(Number)
            Increment=Increment+1
            Lenght_Stack=Lenght_Stack-1
        # print(Number)

        if(Number==i):
            FinalValues.append(Number)




    return FinalValues

# Finding the nearst values
def NearestVales(FinalValues):
    Lenght=len(FinalValues)-1
    MaxValues=FinalValues[Lenght]

    return MaxValues



def Main():
    Number=789
    Stack=DecodingNumber(Number)
    Stack_Last_value=NearestVales(Stack)

    print("The Nearest PlainDrome Number to "+ str(Number)+" is "+ str(Stack_Last_value) )



Main()